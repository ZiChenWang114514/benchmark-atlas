#!/usr/bin/env python3
"""Strip location leaks, internal notes, and API endpoints from public data."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DROP_KEYS = {
    "timezone",
    "round",
    "input_file",
    "collection_status",
    "resource_mapping_status",
    "citation_match",
    "citation_record_selection",
    "novelty_text_basis",
    "identity_review",
    "derived_at",
    "field_path",
    "cache_path",
    "api_url",
    "api_endpoint",
    "endpoint",
}

QUALITY_KEEP = {"validated_date", "deferred", "excluded_as_nonexistent", "per_section"}

ROUND_RE = re.compile(r"第\s*[0-9０-９一二三四五六七八九十两]+\s*轮")
ROUND_WORD_RE = re.compile(r"\bRound\s*\d+\b", re.I)
TS_RE = re.compile(r"(\d{4}-\d{2}-\d{2})T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})")
DRIVE_URL_RE = re.compile(
    r"https?://(?:drive\.google\.com/\S+|docs\.google\.com/\S*(?:drivesdk|1gc-kP3iW-rK79h0GhSUpNgSjHtb3TDOkdjNq5WfykiM|1su106zLttcQLZ-C-thBABCfRruIMWvOXxIhPXVUhQOs)\S*)"
)
WORKSPACE_RE = re.compile(r"/workspace/\S*")
HOME_RE = re.compile(r"/home/\S*")
HF_API_RE = re.compile(r"https?://huggingface\.co/api/datasets/")
ARXIV_API_RE = re.compile(r"https?://export\.arxiv\.org/api/query\?([^\s\"'\\)]+)")
OPENALEX_AUTH_RE = re.compile(r"https?://help\.openalex\.org/api/\S+")
URN_INTERNAL_RE = re.compile(r"^urn:.*(?:editorial|round|[:/]r\d)", re.I)
COUNT_RE = re.compile(r"\d+\s*个\s*待核实字段|待核实字段数|\d+\s*项待核实")


def publicize_apis(text: str) -> str:
    text = HF_API_RE.sub("https://huggingface.co/datasets/", text)

    def arxiv(match: re.Match[str]) -> str:
        query = match.group(1)
        found = re.search(r"id_list=([^&]+)", query)
        if not found:
            return "https://arxiv.org/"
        first = found.group(1).split("%2C")[0].split(",")[0]
        return f"https://arxiv.org/abs/{first}"

    text = ARXIV_API_RE.sub(arxiv, text)
    text = OPENALEX_AUTH_RE.sub("", text)
    text = text.replace("`/api/datasets/{org/name}`", "数据集页面")
    text = text.replace("/api/datasets/{org/name}", "数据集页面")
    return text


def clean_text(text: str) -> str:
    if URN_INTERNAL_RE.search(text):
        return "urn:benchmark-constitution:record"
    text = publicize_apis(text)
    text = DRIVE_URL_RE.sub("", text)
    text = WORKSPACE_RE.sub("", text)
    text = HOME_RE.sub("", text)
    text = TS_RE.sub(r"\1", text)
    text = re.sub(r"[（(]\s*KST\s*/\s*Asia/Seoul\s*[；;]?", "（", text)
    text = re.sub(r"[（(]\s*Asia/Seoul\s*(?:/\s*KST)?\s*[；;]?", "（", text)
    text = re.sub(r"KST\s*/\s*Asia/Seoul", "", text)
    text = re.sub(r"Asia/Seoul\s*/\s*KST", "", text)
    text = re.sub(r"Asia/Seoul\s*[（(]\s*KST\s*[)）]", "", text)
    text = text.replace("Asia/Seoul", "")
    text = text.replace("Asia/Shanghai", "")
    text = text.replace("上海时间", "")
    text = text.replace("KST", "")
    text = text.replace("Seoul", "")
    text = text.replace("首尔", "")
    text = text.replace("Drive", "")
    text = re.sub(r"[+-]\d{2}:\d{2}", "", text)
    text = ROUND_RE.sub("", text)
    text = ROUND_WORD_RE.sub("", text)
    for phrase in (
        "PDF原件入",
        "PDF原件",
        "逐档深核",
        "补传",
        "回填",
        "补填",
        "本轮",
        "Google Drive",
        "google drive",
    ):
        text = text.replace(phrase, "")
    text = re.sub(r"\bDrive\b", "", text)
    text = COUNT_RE.sub("", text)
    text = re.sub(r"[（(]\s*[；;，,、/\s]*[）)]", "", text)
    text = re.sub(r"[（(]\s*[）)]", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s+([；;，,。])", r"\1", text)
    text = re.sub(r"([；;]){2,}", "；", text)
    text = re.sub(r"^[；;，,\s]+", "", text)
    text = re.sub(r"[；;，,\s]+$", "", text)
    return text.strip()


def is_drive(value: object) -> bool:
    return isinstance(value, str) and (
        "drive.google.com" in value or "drivesdk" in value or "1gc-kP3iW-rK79h0GhSUpNgSjHtb3TDOkdjNq5WfykiM" in value
    )


def clean_node(node, parent_key: str | None = None):
    if isinstance(node, dict):
        if is_drive(node.get("webViewLink")):
            node = {key: value for key, value in node.items() if key not in {"webViewLink", "id"}}
        if isinstance(node.get("change"), str) and "date" in node and "value" not in node:
            node = {key: value for key, value in node.items() if key not in DROP_KEYS}
            node["change"] = "最近复核"
        cleaned = {}
        for key, value in node.items():
            if key in DROP_KEYS:
                continue
            if key == "editorial_status" and isinstance(value, str):
                cleaned[key] = ""
                continue
            if key == "change" and node.get("change") == "最近复核":
                cleaned[key] = "最近复核"
                continue
            cleaned[key] = clean_node(value, key)
        sources = cleaned.get("sources")
        if isinstance(sources, list):
            cleaned["sources"] = fix_sources(sources)
        return cleaned
    if isinstance(node, list):
        return [clean_node(item, parent_key) for item in node]
    if isinstance(node, str):
        return clean_text(node)
    return node


def fix_sources(sources: list) -> list:
    kept = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        url = source.get("url")
        if not isinstance(url, str):
            continue
        url = clean_text(url)
        if not url or "drive.google.com" in url or "/api/" in url:
            continue
        next_source = {key: value for key, value in source.items() if key not in DROP_KEYS}
        next_source["url"] = url
        if isinstance(next_source.get("accessed"), str):
            next_source["accessed"] = clean_text(next_source["accessed"]) or source.get("accessed")
        kept.append(next_source)
    if not kept:
        kept = [{"url": "urn:benchmark-constitution:record", "accessed": "2026-11-07"}]
    return kept


def prepare_methodology(text: str) -> str:
    text = re.sub(r"## 六、数据管线与事实溯源.*?(?=## 七、)", "", text, flags=re.S)
    text = re.sub(r"### F\. 溯源、API与可复跑.*\Z", "", text, flags=re.S)
    kept = []
    for line in text.splitlines():
        if re.search(r"API_KEY|GH_TOKEN|/workspace|cache/|api-docs|openalex\.org/api|evidence_overlay|registry_merge", line):
            continue
        kept.append(line)
    return "\n".join(kept).rstrip() + "\n"


def write_json(path: Path, data) -> None:
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if path.read_text(encoding="utf-8") != rendered:
        path.write_text(rendered, encoding="utf-8")


def sanitize_json(path: Path) -> None:
    if path.name == "drive-manifest.json":
        write_json(path, {})
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    if path.name == "quality-report.json" and isinstance(data, dict):
        data = {key: value for key, value in data.items() if key in QUALITY_KEEP}
    data = clean_node(data)
    write_json(path, data)


def sanitize_text_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8")
    text = original
    if path.name == "impact-methodology.md":
        text = prepare_methodology(text)
    text = clean_text(text) if path.suffix.lower() != ".md" else "\n".join(clean_text(line) for line in text.splitlines())
    # clean_text on each line can eat leading markdown structure spaces? It strips edges.
    # Re-join without stripping indentation: clean inside the line but keep indent.
    if path.suffix.lower() == ".md":
        lines = []
        source = prepare_methodology(original) if path.name == "impact-methodology.md" else original
        for line in source.splitlines():
            indent = re.match(r"\s*", line).group(0)
            body = line[len(indent):]
            if re.search(r'"change"\s*:', body) or "待核实字段显式保留" in body or body.startswith("编辑状态："):
                lines.append(f"{indent}最近复核" if body.strip() else line)
                continue
            lines.append(indent + clean_text(body) if body.strip() else line)
        text = "\n".join(lines)
        if original.endswith("\n"):
            text += "\n"
    if text != original:
        path.write_text(text, encoding="utf-8")


def main() -> None:
    json_roots = [ROOT / "data", ROOT / "frontend"]
    text_roots = [ROOT / "content", ROOT / "docs", ROOT / "frontend"]
    for root in json_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            sanitize_json(path)
    for root in text_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".csv", ".txt"}:
                sanitize_text_file(path)
    for path in (ROOT / "data").rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".csv", ".txt"}:
            sanitize_text_file(path)
    for name in ("README.md", "MAINTAINING.md", "CONSTITUTION.md"):
        path = ROOT / name
        if path.exists():
            sanitize_text_file(path)


if __name__ == "__main__":
    main()
