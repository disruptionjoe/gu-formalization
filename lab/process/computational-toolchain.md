---
title: "Computational Toolchain: what is available, and which named gates it unblocks"
status: process
doc_type: toolchain-inventory
created: 2026-08-02
updated: 2026-08-02
claim_status_change: none
canon_change: none
---

# Computational toolchain

## Purpose and boundary

This file records which computational tools the repository can actually run, and
which **already-named** failure conditions and open questions cite a tool as their
stated resolution path.

**Availability of a tool is not a result.** Nothing in this file changes a claim,
a verdict, a grade, or a canon status. A gate that reads "reconstruction grade
pending CAS verification" stays at reconstruction grade until the computation is
actually run and its certificate lands. What changes when a tool is installed is
only the *type* of the blocker: from "we do not have the instrument" to "we have
not yet run it." Those are different, and the ledgers should not confuse them.

The second boundary is Layer-0 (`AGENTS.md`): a CAS returns a **multiplicity or a
decomposition**. Reading that as a **count** is the exact recurring failure this
repository has already had to retract once. Run Layer-0 before arguing from any
CAS decomposition to a physical count.

## Current toolchain

| Tool | Status | Purpose |
|---|---|---|
| Python 3.14 + numpy / scipy / sympy | available | The 780-certificate harness. `requirements.txt`, pin-free by design. |
| Lean 4.32.0-rc1 + mathlib | available | Finite proof kernels. Toolchain and mathlib revision both pinned. |
| python-flint 0.9.0 (FLINT 3 / Arb) | **available** | Certified interval / ball arithmetic. `requirements-optional.txt`, hash-pinned. |
| SageMath 10.9 | **NOT INSTALLED** | Lie-theoretic CAS. Cask fetched; `.pkg` needs an authorized install (below). |

### python-flint

Installed into a local venv, kept out of Git per `AGENTS.md`:

```
python3 -m venv _local/cas-venv
./_local/cas-venv/bin/pip install --require-hashes -r requirements-optional.txt
```

Verified on Python 3.14 / macOS arm64. Unlike `requirements.txt`, this file is
hash-pinned: certified-numerics certificates assert rigorous enclosures rather
than exact identities, so the arithmetic backend is load-bearing for the claim.

### SageMath — install is pending an authorized run

The Homebrew cask exists and the payload downloads, but it installs a `.pkg` that
requires `sudo`; a non-interactive session cannot supply the password. It must be
run from a terminal by the operator:

```
brew install --cask sage
```

The `sage` binary then lives inside the app bundle, not on `PATH`:

```
/Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage
```

Sage bundles Singular (Gröbner bases via `.groebner_basis()`) and can pull QEPCAD
as an optional package, so it covers both the Lie-theory and the real-algebraic-
geometry needs below in one install.

## Gates whose stated resolution path is a CAS

These are **existing** repository items. Each already names a CAS computation as
its upgrade path; none is resolved by this file. Citations are to
`DERIVATION-PROGRESS.md` line numbers at the time of writing.

| Gate | What the repo already says | Bears on |
|---|---|---|
| `OQ-RK1` (:1255) | "Decisive circularity-free gate: CAS computation of `rank(Pi_RS * E_+ * Pi_RS)` in `M(64,H)`, which would return 4 or 8 directly." | `rank_H(S_RS^+)` = 4 vs 8 — Candidate A vs the undismissed Candidate B. Generation-sector. |
| `FC2` (:1555) | "Explicit CAS computation confirming the proposed `E^{-1}` formula." | Velo-Zwanziger E-block invertibility — the precondition holding 14D at `CONDITIONALLY_EVADED`. |
| `FC-MULT` (:1987) | "Reconstruction grade pending LiE verification: if LiE returns multiplicity > 1, `dim_H Hom > 1` and uniqueness weakens." | Shiab uniqueness. Can weaken the claim, not only confirm it. |
| `FC-IRR` (:1987) | "A formal proof requires the `D_7` branching law or a LiE weight computation." | Irreducibility of `ker(c)`, SC1-OQ1A §3.3 Step 3. |
| `FC-HW` (:1987) | Highest-weight assignment `omega_1 + omega_7` for `ker(c)`, reconstruction grade. | SC1-OQ1A. |
| `OQ-CG-2` (:1987) | "LiE/SageMath numerical verification is the upgrade path to RESOLVED." | SC1-OQ1A aggregate verdict, currently `CONDITIONALLY_RESOLVED`. |
| `OQ1` / `FC-LIE` (:1969, :2052) | "Upgrade to verified requires CAS computation in LiE or SageMath" — multiplicity of `(1,2,2)` in `adj(Sp(16))\|_{G_PS}`. | Higgs emergence gate. |
| gimmel curvature (:616) | "The single remaining gap is the explicit CAS computation of the gimmel Riemann tensor tangential projection." | `R_fail` / Einstein-emergence chain. |

Practical note: LiE is effectively unmaintained. Sage's `WeylCharacterRing` with
`branching_rule`, or GAP's `SLA` package, is the maintained equivalent for the
branching and multiplicity items. Two of the gates above (`FC-MULT`, `OQ-RK1`) can
return an answer that *weakens* a current claim; they are not confirmation errands.

## Certified numerics: `ARB-CERT`

The RB campaign's stability and residual controls are graded "CONTROLLED LOCAL
NUMERICS" — float comparisons without error bounds. python-flint makes those
rigorous enclosures at arbitrary precision. Worked example, the RB7 auxiliary-norm
comparison:

```python
from flint import arb, ctx
ctx.prec = 200
a, b = arb('0.00361491'), arb('0.00372577')
assert a < b                      # certified, not a float comparison
a / b                             # [0.97024507685659608617815914562627 +/- 4.71e-60]
```

This upgrades grade without changing method or conclusion. See the ledger
vocabulary in `lean-verification-lane-LEDGER.md`.

## Deliberately not adopted

- **Z3 / SMT** — considered for the B5 five-field packet and rejected. B5 is a
  construction gap, not a search problem: the 1024 phase assignments are already
  fully enumerated into 39 orbits, and a solver cannot supply a Green form or a
  closed symmetry-compatible domain. (Note: `tests/hessian-z3/` is `Z/3`, the
  cyclic group, not the solver.)
- **Adams spectral sequence software (`ext`)** — the ambient
  `Omega^{Pin+}_14 ~= Z/2` audit is already closed; the open piece is the GU class
  map, which `ext` does not compute. Revisit only if `ANOMALY-DESCENT-HARDENING`
  T1 scope changes.
- **xAct / xTensor** — technically strong for the Willmore-EL and Codazzi work,
  but requires Mathematica. External replication is a named residual on the
  published LNF package; a proprietary dependency would put a paywall in front of
  it. Cadabra2 (GPL v3) is the free equivalent if the variational lane resumes.

All adopted and candidate tools are open source: SageMath GPL v3, python-flint
MIT, FLINT LGPL-3.0-or-later, GAP GPL v2+, Singular GPL, Cadabra2 GPL v3,
Lean + mathlib Apache 2.0.
