# Batch build brief (2026-11-07)
Build full Benchmark Atlas entries for the slugs assigned to you, following /workspace/benchmark-atlas/CONSTITUTION.md strictly (Chapter 2: every fact + number has source URL + access date; unknown = 待核实/未公开; never estimate). Use the shortlist entry in data/shortlist-2026h2.json for each slug (name, section, subfield, 2026-H2 evidence) and mirror the exact format of existing entries (e.g. data/benchmarks/gpqa.json, content/benchmarks/gpqa.md) and schema/benchmark.schema.json.

Per slug:
1. FIRST verify the benchmark really exists with an official paper/site/repo. If it can't be verified, do NOT create it; list it in your report as unverified.
2. Write data/benchmarks/<slug>.json (all 11 chapter-4 sections, sources per field, include the 2026-H2 evidence under 最新情况, leaderboard snapshot from official leaderboard + Artificial Analysis/Epoch/LMArena where they track it, with model version + date) and content/benchmarks/<slug>.md (Chinese intro, paraphrased).
3. Google Drive (user-Google-drive connector), root 'Benchmark Atlas' id 1t7oyeKp0N9ZZf7pO3WpAor6ztUYVVgqQ: create the section subfolder if missing (look for an existing one with the exact section name first; natural-science section folders already exist), then a folder 板块_简称_版本, upload the paper PDF (base64 create_file) and a Chinese intro Google Doc. Put drive_pdf {id, webViewLink} in the JSON.
4. Do NOT edit data/index.json, data/news.json, drive-manifest.json, or the master Sheet (other batches run in parallel). Instead write data/batches/<batch-name>.json: list of {slug, json_path, md_path, drive_folder, drive_pdf, drive_doc, todo_fields_count} plus unverified/dropped slugs with reasons, and any notable sourced news items (dated) found along the way.
5. Validate your JSON files against the schema.
Report: built slugs, unverified/dropped slugs and why, notable conflicts, and count of 待核实 fields.
