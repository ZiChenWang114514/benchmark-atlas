#!/usr/bin/env python3
"""Clean purged dossier text and write locale dictionaries."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CJK = re.compile(r"[\u4e00-\u9fff]")

VISUAL_ZH = {
    "visual.menu": "菜单",
    "visual.close": "关闭",
    "visual.statDossiers": "档案",
    "visual.statNews": "动态",
    "visual.statRanked": "探索性排序",
    "visual.statHeat": "热度上榜",
    "visual.statAll": "全部条目",
    "visual.statThin": "证据不足",
    "visual.statListed": "上榜基准",
    "visual.statModels": "窗口模型",
    "visual.impactTabRanked": "探索性排序",
    "visual.impactTabThin": "证据不足",
    "visual.searchBenchmarks": "搜索名称或领域",
    "visual.heatSearch": "搜索基准",
    "visual.allDomains": "全部领域",
    "visual.prev": "上一页",
    "visual.next": "下一页",
    "visual.nullTip": "未取得",
    "visual.unranked": "未赋名次",
    "visual.colRank": "名次",
    "visual.colName": "基准",
    "visual.colDomain": "领域",
    "visual.colScore": "综合分",
    "visual.evQuality": "质量",
    "visual.evCommunity": "社区",
    "visual.evHeadroom": "未饱和",
    "visual.evGithub": "代码",
    "visual.emptyFilter": "没有符合条件的条目",
    "visual.showing": "显示",
    "visual.rows": "条",
    "visual.footerAbout": "公开阅读页",
    "visual.footerAboutTitle": "关于",
    "visual.footerSections": "栏目",
    "visual.footerSources": "来源",
    "visual.snapshot": "数据快照",
    "visual.dossierLink": "档案",
    "visual.reported": "次数",
    "visual.share": "份额",
    "visual.models": "模型",
    "visual.organization": "机构",
    "visual.release": "发布",
    "visual.source": "来源",
    "visual.open": "打开",
    "visual.reportedModels": "报告它的模型",
    "visual.scriptNote": "启用脚本后可搜索、筛选并分页浏览全部条目。",
    "visual.repo": "仓库",
}
VISUAL_EN = {
    "visual.menu": "Menu",
    "visual.close": "Close",
    "visual.statDossiers": "Dossiers",
    "visual.statNews": "News",
    "visual.statRanked": "Exploratory rank",
    "visual.statHeat": "Heat list",
    "visual.statAll": "All entries",
    "visual.statThin": "Insufficient evidence",
    "visual.statListed": "Listed benchmarks",
    "visual.statModels": "Window models",
    "visual.impactTabRanked": "Exploratory ranking",
    "visual.impactTabThin": "Insufficient evidence",
    "visual.searchBenchmarks": "Search name or domain",
    "visual.heatSearch": "Search benchmarks",
    "visual.allDomains": "All domains",
    "visual.prev": "Previous",
    "visual.next": "Next",
    "visual.nullTip": "Not observed",
    "visual.unranked": "Unranked",
    "visual.colRank": "Rank",
    "visual.colName": "Benchmark",
    "visual.colDomain": "Domain",
    "visual.colScore": "Score",
    "visual.evQuality": "Quality",
    "visual.evCommunity": "Community",
    "visual.evHeadroom": "Headroom",
    "visual.evGithub": "Code",
    "visual.emptyFilter": "No matching entries",
    "visual.showing": "Showing",
    "visual.rows": "rows",
    "visual.footerAbout": "Public reading pages",
    "visual.footerAboutTitle": "About",
    "visual.footerSections": "Sections",
    "visual.footerSources": "Sources",
    "visual.snapshot": "Snapshot",
    "visual.dossierLink": "Dossier",
    "visual.reported": "Reports",
    "visual.share": "Share",
    "visual.models": "Model",
    "visual.organization": "Organization",
    "visual.release": "Released",
    "visual.source": "Source",
    "visual.open": "Open",
    "visual.reportedModels": "Models reporting it",
    "visual.scriptNote": "Enable scripts to search, filter, and page through every entry.",
    "visual.repo": "Repository",
}


def clean_text(value: str) -> str:
    if not isinstance(value, str):
        return value
    value = value.replace("Humanity's", "Humanity’s")
    value = value.replace("（；", "（")
    value = value.replace("；）", "）")
    value = value.replace("（）", "")
    value = value.replace("， / UTC+8", "")
    value = value.replace("， UTC+8", "")
    value = value.replace(" / UTC+8", "")
    value = value.replace("UTC+8", "")
    value = value.replace("中文介绍 Google Doc", "中文介绍")
    value = value.replace(
        "本批已查看所列官方材料，但尚未完成该字段的精确核验；不表示官方未公开。",
        "该字段尚未完成精确核验，不表示官方未公开。",
    )
    value = value.replace("不冒充评测运行日", "不是评测运行日")
    value = value.replace("不冒充数据集独立发布日期", "不是数据集的独立发布日期")
    value = value.replace("不冒充数据集单独首发日", "不是数据集的单独发布日")
    value = re.sub(r"(?:\s+[·•・]\s*|\s*[·•・]\s+)", "，", value)
    value = re.sub(r"，{2,}", "，", value)
    value = re.sub(r"。{2,}", "。", value)
    return value


def walk(node):
    if isinstance(node, str):
        return clean_text(node)
    if isinstance(node, list):
        return [walk(item) for item in node]
    if isinstance(node, dict):
        return {key: walk(item) for key, item in node.items()}
    return node


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_near(text: str, anchor: str, old: str, new: str, window: int = 700) -> str:
    out = []
    index = 0
    while True:
        found = text.find(anchor, index)
        if found < 0:
            out.append(text[index:])
            break
        end = found + len(anchor)
        slot = text.find(old, end, end + window)
        if slot < 0:
            out.append(text[index:end])
            index = end
            continue
        out.append(text[index:slot])
        out.append(new)
        index = slot + len(old)
    return "".join(out)


def clean_files() -> None:
    for path in list((ROOT / "data/benchmarks").glob("*.json")) + list((ROOT / "content/benchmarks").glob("*.md")):
        original = path.read_text(encoding="utf-8")
        updated = clean_text(original)
        if path.suffix == ".json":
            # Keep JSON valid if a string replacement touched structure. Strings only were changed.
            json.loads(updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
    for relative in ["data/index.json", "data/news.json", "data/trending.json", "docs/impact-methodology.md", "CONSTITUTION.md"]:
        path = ROOT / relative
        original = path.read_text(encoding="utf-8")
        updated = clean_text(original)
        if path.suffix == ".json":
            json.loads(updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
    # Terminal-Bench Science is general science, not physics.
    anchors = [
        (ROOT / "data/benchmarks/terminal-bench-science.json", '"id": "terminal-bench-science"', '"value": "物理"', '"value": "综合科学"'),
        (ROOT / "data/index.json", '"id": "terminal-bench-science"', '"section": "物理"', '"section": "综合科学"'),
        (ROOT / "data/trending.json", '"slug": "terminal-bench-science"', '"section": "物理"', '"section": "综合科学"'),
        (ROOT / "data/registry/registry.json", '"id": "terminal-bench-science"', '"domain": "物理"', '"domain": "综合科学"'),
        (ROOT / "data/impact/index.json", '"id": "terminal-bench-science"', '"domain": "物理"', '"domain": "综合科学"'),
        (ROOT / "data/frontier/heat.json", '"benchmark_id": "terminal-bench-science"', '"domain": "其他"', '"domain": "综合科学"'),
        (ROOT / "data/frontier/normalization.json", '"id": "terminal-bench-science"', '"domain": "其他"', '"domain": "综合科学"'),
    ]
    for path, anchor, old, new in anchors:
        text = path.read_text(encoding="utf-8")
        updated = replace_near(text, anchor, old, new)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
    md = ROOT / "content/benchmarks/terminal-bench-science.md"
    text = md.read_text(encoding="utf-8")
    text = re.sub(r"(### 主板块\n\n)物理\n", r"\1综合科学\n", text)
    text = text.replace("说明：编辑主板块归档，不据此限制跨学科覆盖。", "说明：综合科学基准，覆盖多个学科，不归入物理。")
    md.write_text(text, encoding="utf-8")
    dossier_path = ROOT / "data/benchmarks/terminal-bench-science.json"
    dossier_text = dossier_path.read_text(encoding="utf-8")
    dossier_text = dossier_text.replace(
        "编辑主板块归档，不据此限制跨学科覆盖。",
        "综合科学基准，覆盖多个学科，不归入物理。",
    )
    dossier_path.write_text(dossier_text, encoding="utf-8")
    index = json.loads((ROOT / "data/index.json").read_text(encoding="utf-8"))
    counts: dict[str, int] = {}
    for item in index["benchmarks"]:
        counts[item["section"]] = counts.get(item["section"], 0) + 1
    block = json.dumps(counts, ensure_ascii=False, indent=1)
    path = ROOT / "data/index.json"
    text = path.read_text(encoding="utf-8")
    updated, n = re.subn(r'"per_section": \{[^}]+\}', '"per_section": ' + block, text, count=1)
    if n != 1:
        raise SystemExit("could not update per_section")
    path.write_text(updated, encoding="utf-8")
    constitution = (ROOT / "CONSTITUTION.md").read_text(encoding="utf-8")
    constitution = constitution.replace("《Benchmark 数据库收集宪法》", "《基准数据库收集宪法》")
    constitution = constitution.replace("AI 评测 benchmark", "人工智能评测基准")
    constitution = constitution.replace("每个 benchmark", "每个基准")
    constitution = constitution.replace("现有 benchmark", "现有基准")
    constitution = constitution.replace("衍生 benchmark", "衍生基准")
    constitution = constitution.replace("新 benchmark", "新基准")
    constitution = constitution.replace("该 benchmark", "该基准")
    constitution = constitution.replace("宪法修改须经你确认，并记录版本号和修改日期。", "宪法修改须记录版本号和修改日期。")
    (ROOT / "CONSTITUTION.md").write_text(constitution, encoding="utf-8")


def build_dictionaries() -> None:
    zh_path = ROOT / "site/src/i18n/zh.json"
    en_path = ROOT / "site/src/i18n/en.json"
    zh = json.loads(zh_path.read_text(encoding="utf-8"))
    zh.update(VISUAL_ZH)
    en_src = ROOT / "scripts/i18n/en_ui.json"
    en = json.loads(en_src.read_text(encoding="utf-8"))
    en.update(VISUAL_EN)
    missing = [key for key in zh if key not in en]
    extra = [key for key in en if key not in zh and not key.startswith("visual.")]
    if missing or extra:
        raise SystemExit(f"locale key mismatch missing={missing[:12]} extra={extra[:12]} missing_count={len(missing)}")
    ordered_zh = {key: zh[key] for key in zh}
    ordered_en = {key: en[key] for key in zh}
    zh_path.write_text(json.dumps(ordered_zh, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    en_path.write_text(json.dumps(ordered_en, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def collect_strings() -> list[str]:
    found: set[str] = set()

    def add(value: str) -> None:
        if isinstance(value, str) and CJK.search(value):
            found.add(value)

    def walk_add(node) -> None:
        if isinstance(node, str):
            add(node)
        elif isinstance(node, list):
            for item in node:
                walk_add(item)
        elif isinstance(node, dict):
            for key, item in node.items():
                if key in {"section", "domain", "url", "webViewLink", "sha256"}:
                    continue
                walk_add(item)

    for path in (ROOT / "data/benchmarks").glob("*.json"):
        walk_add(json.loads(path.read_text(encoding="utf-8")))
    index = json.loads((ROOT / "data/index.json").read_text(encoding="utf-8"))
    for item in index["benchmarks"]:
        add(item.get("summary", ""))
        add(item.get("citation_note", "") or "")
        for tag in item.get("tags") or []:
            add(tag)
        for evidence in item.get("cited_2026h2_evidence") or []:
            add(evidence.get("note") or "")
    for item in json.loads((ROOT / "data/news.json").read_text(encoding="utf-8")):
        add(item.get("title", ""))
        add(item.get("body", ""))
        add(item.get("type") or "")
    trending = json.loads((ROOT / "data/trending.json").read_text(encoding="utf-8"))
    add(trending.get("note") or "")
    for item in trending.get("items") or []:
        add(item.get("rationale") or "")
        for evidence in item.get("evidence") or []:
            add(evidence.get("what") or "")
    quality = json.loads((ROOT / "data/quality-report.json").read_text(encoding="utf-8"))
    for item in quality.get("deferred") or []:
        add(item.get("name") or "")
        add(item.get("reason") or "")
    heat = json.loads((ROOT / "data/frontier/heat.json").read_text(encoding="utf-8"))
    add(((heat.get("window") or {}).get("rule")) or "")
    impact = json.loads((ROOT / "data/impact/index.json").read_text(encoding="utf-8"))
    add(impact.get("publication_warning_zh") or "")
    for dimension in impact.get("dimensions") or []:
        add(dimension.get("name_zh") or "")
        add(dimension.get("description_zh") or "")
    for path in (ROOT / "content/benchmarks").glob("*.md"):
        lead = path.read_text(encoding="utf-8").split("\n## ", 1)[0]
        for line in lead.splitlines():
            add(line.strip())
    return sorted(found, key=len)


def main() -> None:
    clean_files()
    build_dictionaries()
    strings = collect_strings()
    work = ROOT / "data/en/work"
    work.mkdir(parents=True, exist_ok=True)
    chunk_size = 400
    chunks = [strings[index : index + chunk_size] for index in range(0, len(strings), chunk_size)]
    for index, chunk in enumerate(chunks):
        (work / f"chunk-{index:02d}.json").write_text(json.dumps(chunk, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"strings={len(strings)} chunks={len(chunks)}")


if __name__ == "__main__":
    main()
