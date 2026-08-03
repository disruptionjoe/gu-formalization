#!/bin/sh

set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/../../../.." && pwd)
cd "$repo_root"

if ! command -v lake >/dev/null 2>&1; then
    printf '%s\n' "Lake is not installed or not on PATH." >&2
    exit 127
fi

if ! command -v shlock >/dev/null 2>&1; then
    printf '%s\n' "shlock is required by the repository's serialized Lean-build policy." >&2
    exit 127
fi

lock_root="${TMPDIR:-/tmp}/CapacityOS-locks"
lock_path="$lock_root/lean-build.lock"
mkdir -p "$lock_root"

if ! shlock -p "$$" -f "$lock_path"; then
    printf '%s\n' "Another Lean/Lake build holds the lock: $lock_path" >&2
    exit 75
fi

cleanup() {
    rm -f "$lock_path"
}
trap cleanup EXIT HUP INT TERM

ELAN_NO_UPDATE_CHECK=1 lake build \
    +GUFormalization.CompactImageObstructions \
    +GUFormalization.CompactImageObstructionsAxioms

ELAN_NO_UPDATE_CHECK=1 lake env lean \
    Lean/GUFormalization/CompactImageObstructionsAxioms.lean
