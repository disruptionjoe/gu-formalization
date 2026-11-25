---
title: "Reproducing the Computational Certificates"
status: process
doc_type: reproduction-guide
updated_at: "2026-11-25"
---

# Reproducing the computational certificates

This repository uses standalone Python **certificates** for computational checks.
Their scope varies: exact identities, finite controls, stored-report replay,
numerical evidence and reporting checks are not interchangeable. This guide
reproduces the discovered Python checks; each result's verification statement
names the larger claim and any separately supplied proof or source bridge.

## What you need

- **Python 3.9+** (developed/verified on 3.14). Standard library only for many certs.
- **numpy, scipy, sympy** for the certs that do linear algebra / symbolic checks.
  For an exact reproduction of the maintained numeric environment, use the
  hash-pinned lock:
  ```
  pip install --require-hashes -r requirements.lock
  ```
  The verified numeric versions are NumPy 2.5.1, SciPy 1.18.0, SymPy 1.14.0,
  and mpmath 1.3.0. `requirements.txt` remains a convenient unpinned declaration
  of numeric and YAML dependencies, but it is not the exact reproduction
  surface. Many certificates check exact or structural facts; others use
  declared floating-point tolerances, which is why `requirements.lock` records
  the tested builds.

  Python CI uses CPython3.14 and these same numeric pins on Ubuntu. That is a
  package-version match, not an assertion that Linux wheels or BLAS behavior are
  identical to the maintained macOS-arm64 environment. CI prints its interpreter
  and installed package versions. The separate `requirements-tools.lock` pins
  PyYAML6.0.3 for YAML context readers and process gates on standard CPython3.14
  Linux x86_64/macOS arm64; its two wheel hashes do not cover every platform.

  On a Homebrew-managed Python (macOS), that bare `pip install` is refused: the interpreter is
  PEP 668 "externally managed." Use a venv, or certs that import `scipy`/`sympy` will fail with
  `ModuleNotFoundError` and the sweep reports `RED` for an environment reason rather than a
  mathematical one:
  ```
  python3 -m venv _local/cas-venv
  ./_local/cas-venv/bin/pip install --only-binary=:all: --require-hashes -r requirements.lock -r requirements-tools.lock
  ./_local/cas-venv/bin/python scripts/reproduce_all.py --quick --tracked-only
  ```
- **Lean 4.32.0-rc1 via [elan](https://github.com/leanprover/elan)** — *only* for the separate Lean
  checks under `Lean/` (`lean-toolchain` pins the version). The Python harness below does **not**
  run Lean; the Lean legs are checked independently and their toolchain status is noted inline in
  the relevant certs (e.g. `papers/drafts/hardening-pass-2026-07-03/A1-arithmetic-certificate.py`).

### Optional: certified numerics and CAS

Neither is needed to reproduce the current certificate suite. Both are listed because specific
named gates in this repository cite them as their resolution path — see
`lab/process/computational-toolchain.md` for the inventory and its boundary (a tool being
installed changes no claim, verdict, or grade).

- **python-flint** (FLINT 3 / Arb) for rigorous interval arithmetic, graded `ARB-CERT`:
  ```
  python3 -m venv _local/cas-venv
  ./_local/cas-venv/bin/pip install --require-hashes -r requirements-optional.txt
  ```
  This file *is* hash-pinned, unlike `requirements.txt`: enclosure certificates assert bounds
  rather than exact identities, so the arithmetic backend is load-bearing for the claim.

- **SageMath 10.9** for Lie-theoretic branching/multiplicity and Gröbner bases, graded
  `CAS-VERIFIED`. On macOS, `brew install --cask sage` — note it installs a `.pkg` and so needs
  an interactive terminal for the `sudo` prompt. The binary lives inside the app bundle rather
  than on `PATH`:
  ```
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage
  ```
  All tooling here is open source (SageMath GPL v3, python-flint MIT, FLINT LGPL-3.0-or-later),
  so external replication needs no paid license.

## Run everything in one step

```
python scripts/reproduce_all.py            # all certs: tests/ + paper/draft certs
python scripts/reproduce_all.py --quick    # only tests/ (skips the slower paper certs)
python scripts/reproduce_all.py --quick --tracked-only  # committed tests/ certs only
```

Useful flags:

- `--quick` — run only `tests/` (the core certificate suite), skipping the paper/draft certs.
- `--timeout N` — per-certificate timeout in seconds (default 180). One slow or hung cert cannot
  stall the whole run; it is recorded as `TIMEOUT` and the sweep continues.
- `--tracked-only` - discover only Git-tracked certificates. This is useful for local or
  scheduled validation when unrelated untracked work-in-progress exists under `tests/`.
- `--list` — print which certificates would run, without running them.
- `-k SUBSTR` - run only certs whose repository-relative slash path contains `SUBSTR` (e.g. `-k krein`).

The harness discovers every `*.py` under `tests/` (and, in full mode, the paper/draft certs), runs
each in a fresh subprocess, and prints a `PASS/FAIL/TIMEOUT/ERROR` table with totals, the slowest
certs, and a final `GREEN`/`RED` verdict. **Exit code is 0 iff every certificate passed.** Scratch
and cache directories (`__pycache__`, `.pytest_cache`, archived `research-cycles`) are skipped.
With `--tracked-only`, untracked local files under the certificate roots are also skipped.
The discovery scope itself is guarded by `python process_gates/reproduce_harness_scope_audit.py`,
which is a process check and not part of the mathematical certificate sweep.

The harness does not modify any certificate — it only shells out to `python <cert>.py`.

## What a green run means (and does not)

A green (exit 0) run means **every discovered check in the printed scope exited
successfully**, on the reported Python and environment. Some checks rederive
mathematical facts; others confirm finite instances or replay saved evidence.
Some have a differently written sibling `verify/` check, which runs separately.
Read each certificate's scope and the linked `VERIFICATION.md` entry before
inferring what was established.

These are internal checks. The harness does not run Lean, certify every written
analytic proof, validate imported source premises, or establish GU physics.
Manifest/prose consistency, numerical evidence and exact computation remain
separate evidence kinds under the existing probe discipline. See `CANON.md` and
`RESEARCH-POSTURE.md` for the claim boundary.

## How certificates map to claims

- **`tests/README.md`** is the manifest: it maps each directory/group of certs to the claim it
  supports (e.g. `generation-sector/` — Krein signature `(+96,-96)`, net chiral index `chi = 0`;
  `source-action/`, `gu-independent/`, `boundary-eta/`, etc.). The three paper-cited, frozen files
  for the lead paper "Located, Not Forced" are named there.
- **`CANON.md`** and **`RESEARCH-STATUS.md`** state the claims themselves and their tier.
- Paper text: `papers/candidates/located-not-forced/`.

If a cert fails on your machine, report it: the path printed in the `NOT PASSING` list plus the last
lines of its output (which the harness echoes) are enough to reproduce and discuss the discrepancy.
