---
title: "Computational Toolchain: what is available, and which named gates it unblocks"
status: process
doc_type: toolchain-inventory
created: 2026-08-02
updated: 2026-08-26
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
| Python 3.14 + numpy / scipy / sympy | available | The tracked certificate harness. `requirements.lock` pins the maintained numeric environment; `requirements.txt` remains the unpinned direct-dependency declaration. |
| Lean 4.32.0-rc1 + mathlib | available | Finite proof kernels. Toolchain and mathlib revision both pinned. |
| python-flint 0.9.0 (FLINT 3 / Arb) | **available** | Certified interval / ball arithmetic. `requirements-optional.txt`, hash-pinned. |
| SageMath 10.9 | **available** (2026-08-03) | Lie-theoretic CAS. App bundle at `/Applications/SageMath-10-9.app`; binary path below. |

### python-flint

Installed into a local venv, kept out of Git per `AGENTS.md`:

```
python3 -m venv _local/cas-venv
./_local/cas-venv/bin/pip install --require-hashes -r requirements-optional.txt
```

Verified on Python 3.14 / macOS arm64. Unlike `requirements.txt`, this file is
hash-pinned: certified-numerics certificates assert rigorous enclosures rather
than exact identities, so the arithmetic backend is load-bearing for the claim.

### SageMath — installed 2026-08-03

Installed WITHOUT the `.pkg`/sudo route: the Homebrew cask stages the complete
app bundle in the Caskroom, and only the optional `.pkg` step needs root. The
bundle was verified working in place, copied to `/Applications` (admin-group
writable, no sudo), and de-quarantined. The `sage` binary is not on `PATH`:

```
/Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage
```

Verified: `SageMath version 10.9, Release Date: 2026-05-04`, and a first live
gate computation — FC-MULT's multiplicity of `V(omega_6)` in
`V(omega_2) (x) V(omega_6)` for `D_7` returns **1** (dims 91/64 sanity-checked).
That number confirms the reconstruction-grade multiplicity-1 assumption behind
shiab uniqueness; FORMAL discharge of the gate still requires a committed
certificate script plus the claim-status workflow — the number here is
informational, not a filed result.

Sage bundles Singular (Gröbner bases via `.groebner_basis()`) and can pull QEPCAD
as an optional package, so it covers both the Lie-theory and the real-algebraic-
geometry needs below in one install.

## Historical CAS gates and current custody

These are **existing** repository items that named a CAS computation as an
upgrade path. The status column distinguishes algebraic work now closed by the
M-M4 dictionary from gates whose real blocker is semantic, action-owned, or
still genuinely computational. Citations are to `DERIVATION-PROGRESS.md` line
numbers at the time of writing.

| Gate | Current custody | Bears on |
|---|---|---|
| `OQ-RK1` (:1255) | **SPEC-blocked, not CAS-bound.** `tests/oq_rk1_e_rs_eff_assembly.py` returns `BLOCKED_NEEDS_SPEC` because `Pi_RS^phys` / `E_RS^eff` do not exist. The filed decomposition cannot select the physical summand. | `rank_H(S_RS^+)` = 4 vs 8. |
| `FC2` (:1555) | **Still CAS-bound** at its stated algebraic ceiling: explicitly verify the proposed `E^{-1}` formula. | Velo--Zwanziger E-block invertibility. |
| `FC-MULT`, `FC-IRR`, `FC-HW`, `OQ-CG-2` (:1987) | **Algebraic CAS work executed by M-M4.** The exact D7 cache and 60/60 Sage certificate close the branching, highest-weight, multiplicity, dimension, duality, and compact-reality computations. Physical/source conclusions remain separately typed. | SC1-OQ1A algebraic inputs and Shiab existence/uniqueness controls. |
| `OQ1` / `FC-LIE` (:1969, :2052) | **Algebraic D5 controls executed by M-M4; physical selection remains non-CAS.** The dictionary proves `Sym^2(16+) = 10 + 126+`, `Lambda^2(16+) = 120`, `Lambda^5(10) = 126+ + 126-`, and the named `16+ tensor 144+/-` decompositions. It supplies no GU real form, action owner, source-native Higgs/VEV bridge, or physical selector. | Higgs-emergence comparator and bridge question. |
| gimmel curvature (:616) | **Still CAS-bound**: the explicit gimmel Riemann tangential projection has not been filed. | `R_fail` / Einstein-emergence chain. |

Practical note: LiE is effectively unmaintained. Sage's `WeylCharacterRing` with
`branching_rule`, or GAP's `SLA` package, is the maintained equivalent for the
branching and multiplicity items. Two of the gates above (`FC-MULT`, `OQ-RK1`) can
return an answer that *weakens* a current claim; they are not confirmation errands.

## Certified numerics: `ARB-CERT`

The RB campaign's stability and residual controls are graded "CONTROLLED LOCAL
NUMERICS" — float comparisons without error bounds. python-flint makes suitable
quantities rigorous enclosures at arbitrary precision.

**CORRECTION 2026-08-03.** The worked example that previously stood here
enclosed the RB7 auxiliary-norm ratio `0.00361491/0.00372577` to 60 digits.
That was the wrong target: the 2026-08-03 numerical-robustness audit showed
both inputs are finite-difference artifacts (the exact value of the vertical
residual is 0; the quoted digits are machine-dependent at the second decimal),
so the enclosure certified two decimal literals, not the computed tensor.
Rigorous enclosure of a discretization artifact converts a soft error into a
hard-looking one — enclose only quantities whose discretization error is
controlled or absent. A correct worked target from the same campaign is the
RB7 mixed-Gram identity `H_mix = (9/32)(I + T_tr)`, which is an exact rational
statement (verify symbolically in sympy, or enclose the residual of the
identity, which converges to zero under exact derivatives).

This upgrades grade without changing method or conclusion where the target is
sound. See the ledger vocabulary in `lean-verification-lane-LEDGER.md`.

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
