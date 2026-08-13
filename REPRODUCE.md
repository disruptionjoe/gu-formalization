# Reproducing the computational certificates

This repository backs every load-bearing computational claim with a **certificate**: a standalone
script that re-derives the claim from scratch, checks it with hard `assert`s, prints a VERDICT, and
exits nonzero if anything fails. This guide lets an outside skeptic re-run all of them in one step.

## What you need

- **Python 3.9+** (developed/verified on 3.14). Standard library only for many certs.
- **numpy, scipy, sympy** for the certs that do linear algebra / symbolic checks:
  ```
  pip install -r requirements.txt
  ```
  (Verified versions: numpy 2.4.6, scipy 1.18.0, sympy 1.14.0. Pins are not required — the
  certificates check exact and structural facts, not floating-point tolerances.)

  On a Homebrew-managed Python (macOS), that bare `pip install` is refused: the interpreter is
  PEP 668 "externally managed." Use a venv, or certs that import `scipy`/`sympy` will fail with
  `ModuleNotFoundError` and the sweep reports `RED` for an environment reason rather than a
  mathematical one:
  ```
  python3 -m venv _local/cas-venv
  ./_local/cas-venv/bin/pip install -r requirements.txt
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

A green (exit 0) run means: **on your machine, from your Python, every computational claim in the
suite re-derived from scratch and every internal cross-check passed.** Many certs also carry an
independent re-check under a sibling `verify/` directory (a second, differently-written derivation
of the same fact); those run as their own certificates in the sweep.

Honesty boundary: these are **internal-tier** results — *reproduced*, not *independently
peer-reviewed*. A green run says the arithmetic and structural claims are self-consistent and
machine-checkable; it does **not** assert the physics of Geometric Unity, and it is not a substitute
for external review. See `CANON.md` ("Canon means: safe to cite as the current public spine of the
project. It does not mean proved physics.") and `RESEARCH-POSTURE.md`.

## How certificates map to claims

- **`tests/README.md`** is the manifest: it maps each directory/group of certs to the claim it
  supports (e.g. `generation-sector/` — Krein signature `(+96,-96)`, net chiral index `chi = 0`;
  `source-action/`, `gu-independent/`, `boundary-eta/`, etc.). The three paper-cited, frozen files
  for the lead paper "Located, Not Forced" are named there.
- **`CANON.md`** and **`RESEARCH-STATUS.md`** state the claims themselves and their tier.
- Paper text: `papers/candidates/located-not-forced/`.

If a cert fails on your machine, report it: the path printed in the `NOT PASSING` list plus the last
lines of its output (which the harness echoes) are enough to reproduce and discuss the discrepancy.
