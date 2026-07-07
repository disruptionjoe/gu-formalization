#!/usr/bin/env python3
r"""reproduce_all.py — one-step reproducibility harness for the gu-formalization certificates.

Every computational claim in this repo is backed by a standalone Python "certificate": a script
with hard `assert`s and a printed VERDICT that exits 0 on pass and nonzero on failure (see
tests/README.md). Each certificate remains directly runnable, and this harness is the central
runner for sweeping them in one step. It discovers every such certificate, runs each in a fresh
subprocess with a timeout, and prints a PASS/FAIL/TIMEOUT/ERROR summary table with totals. It
exits nonzero iff any certificate did not pass, so a green run == every computational claim
re-derived from scratch on your machine.

It changes NOTHING: it only imports the standard library and shells out to `python <cert>.py`.

USAGE
    python scripts/reproduce_all.py            # all certs: tests/ + paper/draft certs
    python scripts/reproduce_all.py --quick    # only tests/ (skips the slower paper certs)
    python scripts/reproduce_all.py --quick --tracked-only
                                            # local/scheduled sweep of committed certs only
    python scripts/reproduce_all.py --timeout 300   # per-cert timeout in seconds (default 180)
    python scripts/reproduce_all.py --list     # just list what would run, don't run it
    python scripts/reproduce_all.py -k krein   # only certs whose path contains "krein"

EXIT CODE
    0  every discovered certificate passed
    1  at least one certificate FAILED / TIMED OUT / ERRORED
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time

# Repo root = parent of the directory holding this script.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directory trees to sweep for certificates.
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
# Paper/draft certificate roots (skipped under --quick). Only dirs that exist are used.
PAPER_CERT_DIRS = [
    os.path.join(REPO_ROOT, "papers", "drafts", "hardening-pass-2026-07-03"),
    os.path.join(REPO_ROOT, "papers", "candidates"),
]

# Path fragments that mark a directory as non-certificate scratch/cache; never run these.
SKIP_DIR_FRAGMENTS = ("__pycache__", ".cache", ".pytest_cache", ".git", "hourly-cycles")

# Statuses
PASS, FAIL, TIMEOUT, ERROR = "PASS", "FAIL", "TIMEOUT", "ERROR"


def repo_rel(path):
    """Return a repository-relative slash path."""
    return os.path.relpath(path, REPO_ROOT).replace("\\", "/")


def tracked_certificate_files(roots):
    """Return absolute tracked *.py files under roots according to Git."""
    pathspecs = [
        repo_rel(root).rstrip("/")
        for root in roots
        if os.path.isdir(root)
    ]
    if not pathspecs:
        return set()

    proc = subprocess.run(
        ["git", "ls-files", "-z", "--", *pathspecs],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "git ls-files failed")

    tracked = set()
    for rel in proc.stdout.split("\0"):
        if not rel or not rel.endswith(".py") or os.path.basename(rel) == "__init__.py":
            continue
        parts = rel.replace("\\", "/").split("/")
        if any(part in SKIP_DIR_FRAGMENTS for part in parts):
            continue
        tracked.add(os.path.abspath(os.path.join(REPO_ROOT, *parts)))
    return tracked


def discover(roots, tracked_only=False):
    """Yield absolute paths of candidate certificate *.py files under the given roots, sorted."""
    found = []
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            # prune skip dirs in place so os.walk doesn't descend into them
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_FRAGMENTS]
            if any(frag in dirpath.replace("\\", "/").split("/") for frag in SKIP_DIR_FRAGMENTS):
                continue
            for fn in filenames:
                if fn.endswith(".py") and fn != "__init__.py":
                    found.append(os.path.join(dirpath, fn))

    if tracked_only:
        tracked = tracked_certificate_files(roots)
        found = [path for path in found if os.path.abspath(path) in tracked]

    # de-dupe (roots can overlap) and sort for a stable, reviewable order
    return sorted(set(found))


def run_cert(path, timeout):
    """Run one certificate in a subprocess. Return (status, seconds, tail_of_output)."""
    start = time.monotonic()
    try:
        proc = subprocess.run(
            [sys.executable, path],
            cwd=os.path.dirname(path),  # certs may read sibling files by relative path
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return TIMEOUT, time.monotonic() - start, ""
    except Exception as exc:  # pragma: no cover - launcher failure, not a cert failure
        return ERROR, time.monotonic() - start, f"{type(exc).__name__}: {exc}"
    elapsed = time.monotonic() - start
    if proc.returncode == 0:
        return PASS, elapsed, ""
    tail = (proc.stderr or proc.stdout or "").strip().splitlines()
    return FAIL, elapsed, "\n".join(tail[-6:])


def main(argv=None):
    ap = argparse.ArgumentParser(description="Run every computational certificate and summarize.")
    ap.add_argument("--quick", action="store_true",
                    help="run only tests/ (skip the slower paper/draft certs)")
    ap.add_argument("--timeout", type=float, default=180.0,
                    help="per-certificate timeout in seconds (default 180)")
    ap.add_argument("--list", action="store_true", dest="list_only",
                    help="list the certificates that would run, then exit")
    ap.add_argument("--tracked-only", action="store_true",
                    help="discover only Git-tracked certificates; useful for local/scheduled "
                         "runs when untracked work-in-progress exists under tests/")
    ap.add_argument("-k", dest="filter", default=None,
                    help="only run certs whose path contains this substring")
    args = ap.parse_args(argv)

    roots = [TESTS_DIR] if args.quick else [TESTS_DIR] + PAPER_CERT_DIRS
    certs = discover(roots, tracked_only=args.tracked_only)
    if args.filter:
        certs = [c for c in certs if args.filter in c.replace("\\", "/")]

    if not certs:
        print("No certificates discovered. (Are you in the repo? Looked under tests/ and papers/.)")
        return 1

    rel = lambda p: os.path.relpath(p, REPO_ROOT).replace("\\", "/")

    if args.list_only:
        for c in certs:
            print(rel(c))
        scope = "quick: tests/ only" if args.quick else "full: tests/ + paper certs"
        if args.tracked_only:
            scope += "; tracked only"
        print(f"\n{len(certs)} certificate(s) would run ({scope}).")
        return 0

    print("=" * 78)
    print(f"gu-formalization reproducibility harness  —  {len(certs)} certificate(s)")
    mode_label = "quick (tests/ only)" if args.quick else "full (tests/ + paper certs)"
    if args.tracked_only:
        mode_label += " tracked-only"
    print(f"mode: {mode_label}   timeout: {args.timeout:g}s/cert   python: {sys.version.split()[0]}")
    print("=" * 78)

    results = []  # (status, seconds, relpath, tail)
    t0 = time.monotonic()
    for i, c in enumerate(certs, 1):
        status, secs, tail = run_cert(c, args.timeout)
        results.append((status, secs, rel(c), tail))
        marker = {PASS: "ok  ", FAIL: "FAIL", TIMEOUT: "TIME", ERROR: "ERR "}[status]
        print(f"[{i:3d}/{len(certs)}] {marker} {secs:6.1f}s  {rel(c)}")
        if status != PASS and tail:
            for line in tail.splitlines():
                print(f"            | {line}")
    total_secs = time.monotonic() - t0

    counts = {PASS: 0, FAIL: 0, TIMEOUT: 0, ERROR: 0}
    for status, *_ in results:
        counts[status] += 1

    print("=" * 78)
    print("SUMMARY")
    print(f"  PASS    : {counts[PASS]}")
    print(f"  FAIL    : {counts[FAIL]}")
    print(f"  TIMEOUT : {counts[TIMEOUT]}")
    print(f"  ERROR   : {counts[ERROR]}")
    print(f"  TOTAL   : {len(results)}   wall: {total_secs:.1f}s")

    bad = [(s, secs, rp) for (s, secs, rp, _) in results if s != PASS]
    if bad:
        print("-" * 78)
        print("NOT PASSING:")
        for s, secs, rp in bad:
            print(f"  {s:8s} {secs:6.1f}s  {rp}")

    # Surface the slowest few so a reviewer knows where the time went.
    slow = sorted(results, key=lambda r: r[1], reverse=True)[:5]
    print("-" * 78)
    print("SLOWEST:")
    for status, secs, rp, _ in slow:
        print(f"  {secs:6.1f}s  {rp}")
    print("=" * 78)
    verdict = "GREEN — every certificate reproduced." if not bad else \
              f"RED — {len(bad)} certificate(s) did not pass (see above)."
    print(f"VERDICT: {verdict}")
    print("=" * 78)

    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(main())
