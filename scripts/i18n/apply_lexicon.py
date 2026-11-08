#!/usr/bin/env python3
"""Merge chunk translations and render English dossier markdown."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CJK = re.compile(r"[\u4e00-\u9fff]")
HEADINGS = {
    "## 基本信息": "## Basic information",
    "## 发起与维护": "## Origin and maintenance",
    "## 设计目标": "## Design goals",
    "## 构建方式": "## Construction",
    "## 数据形式": "## Data format",
    "## 评测方法": "## Evaluation",
    "## 最新情况": "## Current status",
    "## 榜单快照": "## Leaderboard snapshot",
    "## 联系方式": "## Contact",
    "## 原始文件": "## Original files",
    "## 变更记录": "## Changelog",
}


def load_lexicon() -> dict[str, str]:
    lexicon: dict[str, str] = {
        "待核实": "Unverified",
        "未公开": "Not disclosed",
    }
    work = ROOT / "data/en/work"
    for path in sorted(work.glob("chunk-*.en.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise SystemExit(f"{path} is not an object")
        lexicon.update({str(key): str(value) for key, value in data.items()})
    return lexicon


def translate_line(line: str, lexicon: dict[str, str]) -> str:
    stripped = line.strip()
    if stripped in HEADINGS:
        return HEADINGS[stripped]
    if stripped in lexicon:
        prefix = line[: len(line) - len(line.lstrip())]
        return prefix + lexicon[stripped]
    return line


def main() -> None:
    lexicon = load_lexicon()
    (ROOT / "data/en").mkdir(exist_ok=True)
    (ROOT / "data/en/lexicon.json").write_text(json.dumps(lexicon, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    out_dir = ROOT / "content/en/benchmarks"
    out_dir.mkdir(parents=True, exist_ok=True)
    missing = 0
    total = 0
    for path in sorted((ROOT / "content/benchmarks").glob("*.md")):
        lines = []
        for line in path.read_text(encoding="utf-8").splitlines():
            total += 1
            translated = translate_line(line, lexicon)
            if CJK.search(translated) and translated.strip() not in {"",}:
                # Proper names may remain. Count lines that are still mostly Chinese prose.
                cjk = len(CJK.findall(translated))
                if cjk > 8:
                    missing += 1
            lines.append(translated)
        (out_dir / path.name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    sources = []
    for chunk in (ROOT / "data/en/work").glob("chunk-*.json"):
        if chunk.name.endswith(".en.json"):
            continue
        sources.extend(json.loads(chunk.read_text(encoding="utf-8")))
    covered = sum(1 for item in sources if item in lexicon)
    print(f"lexicon={len(lexicon)} coverage={covered}/{len(sources)} prose_lines_still_long_cjk={missing}/{total}")


if __name__ == "__main__":
    main()
