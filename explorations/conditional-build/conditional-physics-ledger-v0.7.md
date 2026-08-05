---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.7"
machine_source: lab/process/conditional-physics-ledger-v0.7.json
predecessor: lab/process/conditional-physics-ledger-v0.6.json
status: APPEND_ONLY_K77_GLOBAL_FULL_CHIMERIC_CLIFFORD_REDUCTION_CONSTRUCTED__PRIMARY_INDEPENDENT_X_SUPPORT_HORN_SELECTED__LAMBDA_DEF_ALIAS_NONLINEAR_BV_NULL_GREEN_DOMAIN_OPEN
---

# Conditional physics ledger v0.7

## Progress meter

```text
Ledger v0.7 — 82/82 active target rows mapped (100% of current denominator)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Current I1B T=0 pre-Shiab owner: killed at the selected-Shiab value Hessian
Repaired fixed-slot non-null even-BV quotient: rank 16 exact
K77 global full gamma_epsilon Clifford frame: constructed from admitted/source-owned data
K77 sigma_epsilon: global rank 10 with exact adjoint right inverse/projector
Primary support: one bulk action plus independent X action; no transverse profile
Residue — 83 continuous real lower bound (84 if lambda_def is independent)
           + >=19 function-valued + 11 open discrete forks
Quotients ranked: 1 conditional/local; no global residue reduction booked
```

Coverage, verdict counts and global residue are unchanged. `LT-GR2c` moved
closer again. On the oriented/time-oriented K77 branch, the active spin
structure on `X`, tautological Lorentz metric, chimeric spinor extension and
source-owned `epsilon` construct the global **full labelled** Clifford frame
`gamma_epsilon = Ad(epsilon^-1) gamma_0`. This discharges the previous global
reduction condition and globalizes the coefficient-free rank-ten receiver.

The source-guided support choice is one bulk action plus independently typed
`X` terms, joined by the canonical current pushforward `s_!`. It needs no
transverse profile or normal-density trivialization. The remaining relative
coefficient `lambda_def` is an unresolved alias: either it is the existing
`kappa_1`/source normalization or it is one additional real. It is not silently
booked. Nonlinear BV and the null/trace-compatible Krein-Green domain remain
open before this can count as physical recovery.

## Row movements

| row | verdict/kind | v0.7 result | distance |
| --- | --- | --- | --- |
| `LT-GR2b` variable distortion/VEV | `SAME/DERIVED_PARTIAL` | source `theta` and action `T=A-B` are the same connection-difference object up to the tilted trivialization; the ambient Euler row is action-owned | select a nonzero vacuum branch and carry it through the observed equation dual |
| `LT-GR2c` curvature covariation | `NEEDS/MISSING_CONSTRUCTION` | current `I1B` cannot own the pre-Shiab receiver at `T=0`; the repaired local action has an exact non-null quotient; the K77 global full `gamma_epsilon` frame and rank-ten `sigma_epsilon` are exact; the primary independent-`X` support horn is selected without a profile | adjudicate the `lambda_def` normalization alias, assemble the nonlinear primitive/owners, then derive null/Green-domain closure |
| `LT-GR2d` scale and stability | `NEEDS/PROVEN_UNABLE_BY_CURRENT_ACTION` | the current homogeneous action transfers an independent vacuum shift into `T`, but does not hold observed curvature fixed, fix the common amplitude or remove the free gain | derive a separate vacuum-selection/non-equilibrium rule stable under independent shifts |

The new `PROVEN_UNABLE_BY_CURRENT_ACTION` reason is intentionally narrower
than `PROVEN_UNSUPPLYABLE`. It says the built action cannot do the job at the
tested homogeneous value locus; it does not forbid an additional source-owned
term, global constraint, boundary condition or non-equilibrium mechanism.

## What the current action cannot do

At the homogeneous `T=0` value locus, the current `I1B` curvature term is
schematically

```text
<T, S_s(R)> + (kappa/2)<T,*T>.
```

Thus `E_T=S_s(R)` there. Moving the section, density or selected Shiab still
leaves an explicit factor of `T` in the curvature contribution. The exact
rank-ten observed Riemann-kernel witness has `S_s(R)=0` while restriction-first
`G_4` is nonzero. This is now an action-level failure rather than the earlier
circular demand that new geometry factor through an old receiver. It kills
only the selected `T=0` `I1B` ownership route, not nonzero `T`, another Shiab,
a nonregular parent, or a repaired action.

## The repaired horn and its global soldering map

Conditionally, replace the localized gravitational vertical-transgression horn
by

```text
I_pre = integral_X [
  <sigma_epsilon(v_T), G4(res_H P_R Fbar + Q(II_s))>_DW
  + (kappa_1/2)<sigma_epsilon(v_T),sigma_epsilon(v_T)>_DW
] mu_s.
```

The DeWitt subscript is the trace-reversed Frobenius pairing; its exact inertia
on `Sym2(R^4)` is `(6,4)`. The raw coefficient `v_T` is not itself a symmetric
two-tensor. Conditional on a full moving Clifford soldering isometry, the
missing arrow is now

```text
sigma_epsilon(v_T) = pr_V pi1_epsilon(v_T(q)),  q=g/2.
```

Although `q` spans one line, evaluation of arbitrary endomorphisms on nonzero
`q` is surjective. Exact K77 arithmetic gives receiver/projector rank ten.
The `B`-skew coefficient sign cancels the negative DeWitt norm of `q`, so the
right inverse is an isometry and the projector is orthogonal.

The global full reduction now exists on the admitted branch. The splitting
principle gives

```text
w1(Sym2 E) = w1(E),       w2(Sym2 E) = w1(E)^2,
w1(C) = 0,                w2(C) = pi* w2(TX).
```

The supplied spin structure on `X` therefore induces the relevant
`Spin(7,7)` lift, and the source construction of `P_H` from the chimeric
spinor/Krein frame carrier supplies the target bundle. The source `epsilon`
moves the global reference Clifford multiplication as
`gamma_epsilon = Ad(epsilon^-1) gamma_0`. This is a dependent construction;
`epsilon` is not being renamed as `gamma_epsilon`.

On one common stratum the projector splits both the curvature pairing and the
quadratic gain exactly, allowing one gravitational sector to be replaced
without appending another copy. For cross-dimensional support the primary horn
keeps one bulk action and an independently typed `X` action, using `s_!`; this
requires no transverse profile or normal-density trivialization. It does not
prove that the relative coefficient `lambda_def` equals an existing source
normalization. That alias question, nonlinear closure and the analytic domain
keep the ledger row at `NEEDS/MISSING_CONSTRUCTION`.

## Exact local BV result and boundary

At flat observation background and a fixed gravitational slot, the field pair
`(h,v)` lies in `Sym2 + Sym2`, dimension 20. For each tested non-null rational
covector, the diffeomorphism tangent has rank four, the Einstein symbol has
rank six, and the repaired Hessian has rank sixteen. Exact arithmetic gives

```text
0 -> R^4 --d0--> R^20 --J_pre--> R^20 --d0*--> R^4 -> 0,
ker J_pre = im d0,       im J_pre = ker d0*.
```

The five-coefficient covariant second-order ansatz is also fixed, up to scale,
to the Einstein line by Ward plus Bianchi constraints. This is an actual
differential and quotient calculation, not rank subtraction.

Two planted physics controls prevent overpromotion. At zero gain the Hessian
rank falls to twelve and leaves four extra kernel directions. At a null
covector, six non-gauge characteristic kernel directions survive. No global
residue reduction is booked, and no nonlinear CME/BFV, Green domain, physical
degree count, vacuum selection, screening, FLRW solution or `w(z)` prediction
is claimed.

## Vacuum-shift control

For one active mode the current action linearizes schematically to

```text
c + kappa*t + rho_vac = 0.
```

This is rank one. It makes `t` follow a shift, but `c` remains a free
coordinate, and a free `kappa` remains a free normalization. Holding `c=0`
requires a second independent equation; the homogeneous `B` variation does
not supply it. This is field tracking—the limited two-problems-to-one win—not
radiative screening or a first-principles magnitude derivation.

## Next work

1. `LT-GR1b/LT-GR2c/LT-SM8`: assemble the global `gamma_epsilon` nonlinear
   even Ward/BV primitive-owner ledger, test whether `lambda_def` is the
   existing `kappa_1`/source normalization or an additional real, and construct
   the null trace-compatible closed Krein/Green domain.
2. `LT-GR2b/c/d` plus `LT-SM8`: carry the selected independent-`X` support horn
   through moving `P`, moving `q`, section, Hodge/density and preboundary
   owners, then resolve the six non-gauge null-characteristic directions.
3. `LT-GR2b/d`: only then construct/select a nonzero vacuum branch and repeat
   the independent vacuum-shift test.
4. `LT-GR2e`: derive FLRW and perturbations from that action-owned branch.

Evidence, controls and source return:
`k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md`
and
`k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md`.
The return is `SOURCE-CORRECTS`: Weinstein's sources own the active spin
structure, chimeric-spinor construction of `P_H`, Clifford/exterior adjoint
typing and epsilon rotation needed for the global construction. The exact
characteristic-class and receiver proofs remain this repo's work, not a source
attribution.
