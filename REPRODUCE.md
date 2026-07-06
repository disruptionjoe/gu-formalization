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
- **Lean 4.32.0-rc1 via [elan](https://github.com/leanprover/elan)** — *only* for the separate Lean
  checks under `Lean/` (`lean-toolchain` pins the version). The Python harness below does **not**
  run Lean; the Lean legs are checked independently and their toolchain status is noted inline in
  the relevant certs (e.g. `papers/drafts/hardening-pass-2026-07-03/A1-arithmetic-certificate.py`).

## Run everything in one step

```
python scripts/reproduce_all.py            # all certs: tests/ + paper/draft certs
python scripts/reproduce_all.py --quick    # only tests/ (skips the slower paper certs)
```

Useful flags:

- `--quick` — run only `tests/` (the core certificate suite), skipping the paper/draft certs.
- `--timeout N` — per-certificate timeout in seconds (default 180). One slow or hung cert cannot
  stall the whole run; it is recorded as `TIMEOUT` and the sweep continues.
- `--list` — print which certificates would run, without running them.
- `-k SUBSTR` — run only certs whose path contains `SUBSTR` (e.g. `-k krein`).

The harness discovers every `*.py` under `tests/` (and, in full mode, the paper/draft certs), runs
each in a fresh subprocess, and prints a `PASS/FAIL/TIMEOUT/ERROR` table with totals, the slowest
certs, and a final `GREEN`/`RED` verdict. **Exit code is 0 iff every certificate passed.** Scratch
and cache directories (`__pycache__`, `.pytest_cache`, archived `hourly-cycles`) are skipped.
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
