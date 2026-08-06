---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.15"
machine_source: lab/process/conditional-physics-ledger-v0.15.json
predecessor: lab/process/conditional-physics-ledger-v0.14.json
status: APPEND_ONLY_FIRST_INTERACTION_AND_GLOBAL_ZERO_MODE_UPDATE
---

# Conditional physics ledger v0.15

## Progress meter

```text
Ledger v0.15 — 82/82 active target rows mapped (100% of denominator)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Free TT spectral grading: positive at quadratic grade, no scalar-sign extension
                               through the first action-owned cubic
Finite local dark-energy horns: constant mode cannot screen
Conditional global horn: constant shifts screened by Q=1-Pi0
Missing owner: normalized covariant domain/measure functional ell
Residue — 84 continuous real before quotient + >=19 function-valued
          + 9 open discrete forks
Quotients ranked: 4 scoped; no global physical residue reduction booked
```

Coverage, verdict counts and global residue are unchanged. Six row distances
move. The fourth ranked quotient is the finite zero-mode complement after a
normalized functional is supplied; it is not an actual ambient `Y14` physical
quotient and does not reduce the global parameter ledger.

## The positivity target is now the interacting C-operator

The predecessor's free two-field TT pencil admits a canonical spectral
involution `P` with positive majorant. The existing scalar horn contains the
first owned interaction `theta h^2`. In the `P` eigenbasis,

```text
h = q0 + qm,
V3 = c theta (q0^2 + 2 q0 qm + qm^2).
```

The mixed monomial requires `theta` odd, while the diagonal monomials require
it even. No scalar sign extends the free `P`. This is a route kill, not a
physical-theory kill: field-mixing involutions, nonlinear gradings and the
nonlocal interacting `C` remain open.

Source reinspection also removes a false dependency. Super-IG is an algebraic
global-descent problem—odd bracket into connection one-forms, equivariance,
Jacobi and real form. Weinstein does not require an odd action to do GU.
Therefore the interacting positivity/BV problem and super-IG descent now run
as separate Build targets.

## The full finite-local constant-mode class is closed

For every finite local derivative polynomial

```text
K(D) = a + c1 D + ... + cN D^N,   D(1)=0,
```

the constant mode sees only `a`. If `a != 0`, the response is
`R=2 rho/a`; if `a=0`, a nonzero constant source fails the kernel solvability
condition. More local derivatives cannot screen vacuum shifts.

This is stronger than the predecessor's one-horn calculation and still
narrower than a global no-go. Boundary conditions, normalized global
constraints and nonlocal operators are outside the local class.

## A global projector works, but exposes a datum

Given a normalized functional `ell(1)=1`, define

```text
Pi0 f = 1 ell(f),
Q = 1 - Pi0.
```

Then `Q(rho+delta)=Q rho` for every constant `delta`. On the finite connected
transitive control, the self-adjoint invariant `Pi0` is unique and has rank
one; `Q` has rank `n-1` and commutes with the Laplacian. Four weights minus
four independent normalization/symmetry constraints leaves zero freedom.

But the finite domain and invariant measure were supplied before that count.
A noncompact Lorentzian spacetime has no normalized translation-invariant
volume. The next constructive burden is therefore exact:

```text
derive or supply ell: observable functions -> R,
ell(1)=1,
with covariance, positivity, domain and observation-descent rules,
then insert Q into one action.
```

This type is not identified with `P2_datum`. P1/P2/P3 remain unused.

## Row movements

| row | verdict/kind retained | distance now |
| --- | --- | --- |
| `LT-GR2b` | `SAME/DERIVED_PARTIAL` | interacting field-mixing/nonlocal `C`; scalar-sign extension killed |
| `LT-GR2c` | `NEEDS/MISSING_CONSTRUCTION` | derive/supply covariant normalized functional and action placement |
| `LT-GR2d` | `NEEDS/MISSING_CONSTRUCTION` | select global functional without fitting the shift; conditional `Q` response is exact |
| `LT-GR3` | `DIFFERS/STRUCTURAL_DIFFERENCE` | full cubic interacting `C` or general obstruction |
| `LT-GR5` | `DIFFERS/STRUCTURAL_DIFFERENCE` | nonlinear augmented-torsion positive metric |
| `LT-SM8` | `NEEDS/PROVEN_UNSUPPLYABLE` | even interacting physical quotient; super-IG separately algebraic |

`LT-GR1`, `LT-GR2e`, `LT-GR6` and every other row do not change.

## Next gates

1. Construct the first perturbative interacting `C` on the existing even-BV
   carrier, or extend the obstruction to the full cubic vertex bank.
2. Globalize the mixed super-IG bracket to the actual `H`-bundle with real
   form, equivariance, Jacobi and observation descent.
3. Derive or explicitly supply the normalized observer/domain functional and
   place its projector in one action.
4. Only then derive action-owned FLRW perturbations and held-out `w(z)`.

Evidence:

- `first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md`;
- `first_interaction_krein_global_zero_mode_probe.py`;
- `first_interaction_krein_global_zero_mode_independent.sage`;
- `first-interaction-krein-global-zero-mode-source-reinspection-2026-08-05.md`;
  and
- `2026-08-05-first-interaction-krein-global-zero-mode-review.md`.
