#!/usr/bin/env python3
"""Add one benchmark dossier to benchmark-constitution (AISLE-style intake)."""
from __future__ import annotations
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACC = "2026-11-10"
CJK = re.compile(r"[\u4e00-\u9fff]")

ZH_LABELS = {
  "basic_info": ("基本信息", [
    ("name","简称"),("full_name","全称"),("version","基准版本"),("paper_version","论文版本"),
    ("release_date","发布日期"),("section","主板块"),("subfields","领域标签"),("license","许可证"),
    ("paper_url","论文或技术报告"),("code_url","官方代码"),("dataset_url","数据地址"),
    ("official_homepage","官方主页"),("paper_title","论文题名")]),
  "organization": ("发起与维护", [
    ("initiators","发起方"),("partners","协作机构"),("authors","作者"),("maintainer","当前维护方"),("funders","资助方")]),
  "design_goals": ("设计目标", [
    ("capabilities","要测的能力"),("gap_in_prior_benchmarks","现有基准的缺口")]),
  "construction": ("构建方式", [
    ("question_sources","题目来源"),("author_background","出题人背景"),("review_process","审核流程"),
    ("quality_control","质量控制"),("decontamination","去污染")]),
  "data_format": ("数据形式", [
    ("size","题量"),("question_types","题型"),("modalities","模态"),("languages","语言"),
    ("difficulty","难度"),("public_hidden_split","公开与隐藏划分")]),
  "evaluation": ("评测方法", [
    ("metrics","指标"),("scoring","评分方式"),("prompt_settings","提示设置"),
    ("official_scripts","官方评测脚本"),("comparability_warning","可比性说明")]),
  "latest_status": ("最新情况", [
    ("checked_at","核验日期"),("latest_dataset_version","最新数据版本"),("paper_revision_history","论文修订"),
    ("saturation","饱和情况"),("contamination_and_issues","污染与争议"),("derivatives","衍生基准")]),
  "leaderboard": ("榜单快照", [
    ("snapshot_date","快照日期"),("official_url","官方榜"),("third_party_url","第三方榜"),
    ("results","结果快照"),("coverage_note","覆盖说明")]),
  "contact": ("联系方式", [
    ("public_emails","公开邮箱"),("github_issues","代码讨论"),("official_social","官方社交账号"),("privacy_policy","隐私政策")]),
  "original_files": ("原始文件", [
    ("paper_pdf_url","论文PDF"),("sha256","文件校验"),("pdf_bytes","文件大小"),
    ("drive_folder","文件夹"),("other_documents","其他文件")]),
}

EN_LABELS = {
  "basic_info": ("Basic information", [
    ("name","Short name"),("full_name","Full name"),("version","Version"),("paper_version","Paper version"),
    ("release_date","Release date"),("section","Section"),("subfields","Tags"),("license","License"),
    ("paper_url","Paper or report"),("code_url","Code"),("dataset_url","Dataset"),
    ("official_homepage","Homepage"),("paper_title","Paper title")]),
  "organization": ("Origin and maintenance", [
    ("initiators","Initiators"),("partners","Partners"),("authors","Authors"),("maintainer","Maintainer"),("funders","Funders")]),
  "design_goals": ("Design goals", [
    ("capabilities","Capabilities tested"),("gap_in_prior_benchmarks","Gap in prior benchmarks")]),
  "construction": ("Construction", [
    ("question_sources","Question sources"),("author_background","Author background"),("review_process","Review process"),
    ("quality_control","Quality control"),("decontamination","Decontamination")]),
  "data_format": ("Data format", [
    ("size","Size"),("question_types","Question types"),("modalities","Modalities"),("languages","Languages"),
    ("difficulty","Difficulty"),("public_hidden_split","Public and hidden split")]),
  "evaluation": ("Evaluation", [
    ("metrics","Metrics"),("scoring","Scoring"),("prompt_settings","Prompt settings"),
    ("official_scripts","Official scripts"),("comparability_warning","Comparability note")]),
  "latest_status": ("Current status", [
    ("checked_at","Checked on"),("latest_dataset_version","Latest data version"),("paper_revision_history","Paper revisions"),
    ("saturation","Saturation"),("contamination_and_issues","Contamination and disputes"),("derivatives","Related benchmarks")]),
  "leaderboard": ("Leaderboard snapshot", [
    ("snapshot_date","Snapshot date"),("official_url","Official board"),("third_party_url","Third-party board"),
    ("results","Results snapshot"),("coverage_note","Coverage note")]),
  "contact": ("Contact", [
    ("public_emails","Public email"),("github_issues","Code discussion"),("official_social","Official social accounts"),("privacy_policy","Privacy policy")]),
  "original_files": ("Original files", [
    ("paper_pdf_url","Paper PDF"),("sha256","Checksum"),("pdf_bytes","File size"),
    ("drive_folder","Folder"),("other_documents","Other documents")]),
}

SECTION_EN = {
  "化学": "Chemistry", "生物与医学": "Biology and medicine", "综合科学": "General science",
  "物理": "Physics", "多模态": "Multimodal", "Agent": "Agent", "安全": "Safety", "材料": "Materials",
}

def F(value, urls, status=None):
  d = {"value": value, "sources": [{"url": u, "accessed": ACC} for u in urls]}
  if status is not None:
    d["status"] = status
  return d

def fmt_val(v):
  if isinstance(v, list):
    if v and isinstance(v[0], dict) and "change" in v[0]:
      return "；".join(f"{x['date']}：{x['change']}" for x in v)
    return "；".join(str(x) for x in v)
  if isinstance(v, dict):
    return json.dumps(v, ensure_ascii=False)
  return str(v)

def src_line(field, prefix="来源"):
  parts = [f"[{i}]({s['url']})" for i, s in enumerate(field["sources"], 1)]
  word = "访问" if prefix == "来源" else "accessed"
  return f"{prefix}: {' '.join(parts)} ({word} {field['sources'][0]['accessed']})"

def write_md(path, title, summary, dossier, labels, en_values=None, prefix="来源", changelog_line="2026-11-10：初次收录。"):
  lines = [f"# {title}", "", summary, ""]
  for section_key, (heading, fields) in labels.items():
    lines.append(f"## {heading}")
    lines.append("")
    sec = dossier[section_key]
    for key, label in fields:
      field = sec[key]
      if en_values is not None:
        raw = en_values[key]
        val = "; ".join(raw) if isinstance(raw, list) else str(raw)
      else:
        val = fmt_val(field["value"])
      lines.append(f"**{label}**：{val}")
      lines.append("")
      lines.append(src_line(field, prefix=prefix))
      lines.append("")
  lines.append("## 变更记录" if prefix == "来源" else "## Changelog")
  lines.append("")
  lines.append(changelog_line)
  lines.append("")
  path.write_text("\n".join(lines), encoding="utf-8")

def intake(spec: dict):
  bid = spec["id"]
  assert re.fullmatch(r"[a-z0-9-]+", bid), bid
  urls = spec["urls"]
  primary = spec.get("primary_urls") or urls[:3]
  zh = spec["zh"]  # field values
  en = spec["en"]
  summary_zh = spec["summary_zh"]
  summary_en = spec["summary_en"]
  section = zh["section"]
  tags_zh = zh["subfields"] if isinstance(zh["subfields"], list) else [t.strip() for t in zh["subfields"].replace("；",";").split(";") if t.strip()]
  index_tags = spec.get("index_tags") or ([section] + [t for t in tags_zh if t != section])[:6]
  name = zh["name"]

  def z(key, status_if_pending=False):
    val = zh[key]
    st = None
    if val in ("待核实", "未公开") or (isinstance(val, str) and val.startswith("待核实")):
      st = "待核实" if val != "未公开" else "未公开"
    u = zh.get(f"_{key}_urls") or primary
    return F(val, u, status=st)

  dossier = {
    "id": bid,
    "schema_version": "0.1.0",
    "editorial_status": "",
    "basic_info": {k: z(k) for k in ["name","full_name","version","paper_version","release_date","section","subfields","license","paper_url","code_url","dataset_url","official_homepage","paper_title"]},
    "organization": {k: z(k) for k in ["initiators","partners","authors","maintainer","funders"]},
    "design_goals": {k: z(k) for k in ["capabilities","gap_in_prior_benchmarks"]},
    "construction": {k: z(k) for k in ["question_sources","author_background","review_process","quality_control","decontamination"]},
    "data_format": {k: z(k) for k in ["size","question_types","modalities","languages","difficulty","public_hidden_split"]},
    "evaluation": {k: z(k) for k in ["metrics","scoring","prompt_settings","official_scripts","comparability_warning"]},
    "latest_status": {k: z(k) for k in ["checked_at","latest_dataset_version","paper_revision_history","saturation","contamination_and_issues","derivatives"]},
    "leaderboard": {k: z(k) for k in ["snapshot_date","official_url","third_party_url","results","coverage_note"]},
    "contact": {k: z(k) for k in ["public_emails","github_issues","official_social","privacy_policy"]},
    "original_files": {k: z(k) for k in ["paper_pdf_url","sha256","pdf_bytes","drive_folder","other_documents"]},
    "drive_pdf": F({}, primary),
    "changelog": F([{"date": ACC, "change": "初次收录"}], primary),
  }
  # ensure checked_at
  dossier["latest_status"]["checked_at"] = F(ACC, primary)

  (ROOT / "data/benchmarks" / f"{bid}.json").write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
  write_md(ROOT / "content/benchmarks" / f"{bid}.md", name, summary_zh, dossier, ZH_LABELS, prefix="来源", changelog_line="2026-11-10：初次收录。")
  write_md(ROOT / "content/en/benchmarks" / f"{bid}.md", name if not CJK.search(name) else en["name"], summary_en, dossier, EN_LABELS, en_values=en, prefix="Sources", changelog_line="2026-11-10: Initial filing.")

  # lexicon
  lex_path = ROOT / "data/en/lexicon.json"
  lex = json.loads(lex_path.read_text(encoding="utf-8"))
  lex[summary_zh] = summary_en
  for k, zv in zh.items():
    if k.startswith("_"): continue
    ev = en.get(k)
    if ev is None: continue
    if isinstance(zv, list):
      # whole joined string already via fmt; also each tag
      joined = fmt_val(zv)
      if CJK.search(joined):
        lex[joined] = en.get("subfields") if k == "subfields" else (ev if isinstance(ev, str) else "; ".join(ev) if isinstance(ev, list) else str(ev))
      if k == "subfields":
        en_tags = en["subfields"] if isinstance(en["subfields"], list) else [x.strip() for x in str(en["subfields"]).replace("；",";").split(";") if x.strip()]
        for a, b in zip(zv, en_tags):
          if CJK.search(str(a)):
            lex[str(a)] = b
    elif isinstance(zv, str) and CJK.search(zv):
      lex[zv] = ev if isinstance(ev, str) else str(ev)
  for a, b in (spec.get("lexicon") or {}).items():
    lex[a] = b
  # common tags
  for a, b in {
    "湿实验": "wet lab",
    "初次收录": "Initial filing",
    "新基准": "New benchmark",
  }.items():
    lex.setdefault(a, b)
  lex_path.write_text(json.dumps(lex, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

  # index
  idx = json.loads((ROOT / "data/index.json").read_text(encoding="utf-8"))
  if any(b["id"] == bid for b in idx["benchmarks"]):
    raise SystemExit(f"index already has {bid}")
  idx["benchmarks"].append({
    "id": bid,
    "name": name,
    "section": section,
    "tags": index_tags,
    "summary": summary_zh,
    "json": f"data/benchmarks/{bid}.json",
    "content": f"content/benchmarks/{bid}.md",
    "drive_pdf": {},
    "drive_intro": {},
    "sources": [{"url": u, "accessed": ACC} for u in primary],
    "last_checked": ACC,
  })
  idx["count"] = len(idx["benchmarks"])
  idx["generated_at"] = ACC
  ps = idx.get("per_section") or {}
  ps[section] = ps.get(section, 0) + 1
  idx["per_section"] = ps
  (ROOT / "data/index.json").write_text(json.dumps(idx, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

  # master-index
  with open(ROOT / "data/master-index.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
  header, body = rows[0], rows[1:]
  if not any(r and r[0] == name for r in body):
    paper = zh.get("paper_url") if zh.get("paper_url") not in ("待核实", "未公开") else "待核实"
    tags_cell = " / ".join(tags_zh[:4])
    body.append([name, section, tags_cell, summary_zh, paper if isinstance(paper, str) else "待核实", ""])
  with open(ROOT / "data/master-index.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(body)

  # registry
  reg = json.loads((ROOT / "data/registry/registry.json").read_text(encoding="utf-8"))
  existing = next((x for x in reg["items"] if x.get("id") == bid), None)
  entry = {
    "id": bid,
    "name": name,
    "aliases": spec.get("aliases") or [],
    "domain": section,
    "subdomain": spec.get("subdomain"),
    "description_zh": summary_zh,
    "organization": spec.get("organization") or zh.get("initiators", "")[:120],
    "release_date": zh.get("release_date") if zh.get("release_date") != "待核实" else None,
    "paper_url": zh.get("paper_url") if zh.get("paper_url") not in ("待核实", "未公开") else None,
    "arxiv_id": spec.get("arxiv_id"),
    "doi": spec.get("doi"),
    "github_url": zh.get("code_url") if zh.get("code_url") not in ("待核实", "未公开") else None,
    "hf_dataset": spec.get("hf_dataset"),
    "homepage": zh.get("official_homepage") if zh.get("official_homepage") not in ("待核实", "未公开") else None,
    "leaderboard_url": zh.get("official_url") if zh.get("official_url") not in ("待核实", "未公开") else None,
    "task_format": spec.get("task_format"),
    "size": spec.get("size"),
    "license": zh.get("license") if zh.get("license") not in ("待核实", "未公开") else None,
    "sources": [{"url": u, "accessed": ACC} for u in primary],
    "discovered_via": spec.get("discovered_via") or "官方页面 / 论文检索",
    "homepage_note_zh": None,
    "metrics": {
      "citations": None,
      "gh_stars": spec.get("gh_stars"),
      "hf_downloads": spec.get("hf_downloads"),
      "hf_likes": spec.get("hf_likes"),
      "provenance": spec.get("metrics_provenance") or [],
      "paper_eligible": bool(spec.get("arxiv_id") or (zh.get("paper_url") not in (None, "待核实", "未公开"))),
      "collected_at": ACC,
    },
    "audit_history": [],
  }
  # leaderboard key mismatch - use snapshot official_url from zh
  entry["leaderboard_url"] = zh.get("official_url") if zh.get("official_url") not in ("待核实", "未公开") else entry["homepage"]
  if existing:
    existing.update(entry)
  else:
    reg["items"].append(entry)
  reg["count"] = len(reg["items"])
  reg["generated_at"] = ACC
  (ROOT / "data/registry/registry.json").write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

  # impact
  imp = json.loads((ROOT / "data/impact/index.json").read_text(encoding="utf-8"))
  if not any(u.get("id") == bid for u in imp.get("unscored", [])) and not any(u.get("id") == bid for u in imp.get("ranking", [])):
    peers = spec.get("nearest_benchmarks") or ["aisle", "biobasicsbench", "lab-bench"]
    imp["unscored"].append({
      "rank": None,
      "id": bid,
      "name": name,
      "domain": section,
      "release_date": entry["release_date"],
      "score": None,
      "observed_score": None,
      "components": {k: None for k in ["citations_total","citation_velocity","github","huggingface","model_adoption","evaluator_adoption","community","novelty","quality","distinctiveness","headroom","maintenance"]},
      "raw": {
        "citations": None,
        "gh_stars": spec.get("gh_stars"),
        "hf_downloads": spec.get("hf_downloads"),
        "hf_likes": spec.get("hf_likes"),
        "paper_eligible": entry["metrics"]["paper_eligible"],
        "collected_at": ACC,
        "nearest_benchmarks": peers,
      },
      "flags": ["insufficient_evidence", "early_signal", "provisional"],
      "confidence": {"coverage": 0.0, "label": "low", "official_rank_eligible": False, "rank_eligible": False, "note": "覆盖度是证据完备程度，不是统计置信区间"},
      "provenance": [],
      "assessment": {},
      "assessment_review": None,
    })
    imp["generated_at"] = ACC
    (ROOT / "data/impact/index.json").write_text(json.dumps(imp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

  print(json.dumps({"ok": True, "id": bid, "section": section, "index_count": idx["count"]}, ensure_ascii=False))

if __name__ == "__main__":
  spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
  intake(spec)
