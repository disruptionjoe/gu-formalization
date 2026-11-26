#!/usr/bin/env bash
set -euo pipefail
paper_dir="$(cd "$(dirname "$0")" && pwd)"
repo_dir="$(git -C "$paper_dir" rev-parse --show-toplevel)"
build_dir="$repo_dir/_local/symmetry-rigidity-finite-jets-build"
mkdir -p "$build_dir"
# Uses only installed Tectonic resources. A fresh installation must populate its bundle cache first.
tectonic --only-cached --keep-logs --outdir "$build_dir" "$paper_dir/manuscript.tex"
cp "$build_dir/manuscript.pdf" "$paper_dir/manuscript.pdf"
