#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-$HERE/.venv/bin/python}"
# Authorized environment variables only. Never load credential files.
mkdir -p "$HERE/cache"
exec 9>"$HERE/cache/pipeline.lock"
flock -n 9 || { printf '%s\n' 'A BCI pipeline is already running'; exit 1; }
"$PYTHON" "$HERE/metadata.py" --offline
"$PYTHON" "$HERE/enrich.py" "$@"
"$PYTHON" "$HERE/metadata.py" --offline
DATE_ARGS=()
for ARG in "$@"; do [[ "$ARG" != --offline ]] || DATE_ARGS+=(--offline); done
"$PYTHON" "$HERE/arxiv_dates.py" "${DATE_ARGS[@]}"
"$PYTHON" "$HERE/compute.py"
"$PYTHON" "$HERE/write_report.py"
