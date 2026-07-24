#!/bin/sh

set -eu

run_update=false
run_cache=false

while [ "$#" -gt 0 ]; do
    case "$1" in
        --update)
            run_update=true
            ;;
        --cache)
            run_cache=true
            ;;
        *)
            printf '%s\n' "usage: $0 [--update] [--cache]" >&2
            exit 64
            ;;
    esac
    shift
done

if ! command -v lake >/dev/null 2>&1; then
    printf '%s\n' "Lake is not installed or not on PATH. Install Lean/elan, then rerun this script." >&2
    exit 127
fi

if ! command -v shlock >/dev/null 2>&1; then
    printf '%s\n' "shlock is required for the host-local Lean/Lake build lock." >&2
    exit 127
fi

# All macOS/POSIX-host GU Lean invocations use this wrapper. The host-local
# shlock claim prevents compliant direct-chat and scheduled GU runs on this
# host from starting overlapping local builds. It does not coordinate another
# host or cloud runner; the workspace contract still forbids those overlaps.
lock_root="${TMPDIR:-/tmp}/CapacityOS-locks"
lock_path="${lock_root}/lean-build.lock"
mkdir -p "$lock_root"

if ! shlock -p "$$" -f "$lock_path"; then
    printf '%s\n' "Another Lean/Lake build holds the CapacityOS lock: $lock_path" >&2
    exit 75
fi

cleanup() {
    rm -f "$lock_path"
}
trap cleanup EXIT HUP INT TERM

if [ "$run_update" = true ]; then
    lake update
fi

if [ "$run_cache" = true ]; then
    lake exe cache get
fi

# Lake 5 no longer accepts the historical `lake build -j1` form. The wrapper's
# host-local exclusive claim serializes GU Lean builds on this machine.
lake build
