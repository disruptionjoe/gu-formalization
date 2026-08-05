---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.5"
machine_source: lab/process/conditional-physics-ledger-v0.5.json
predecessor: lab/process/conditional-physics-ledger-v0.4.json
status: APPEND_ONLY_CURRENT_I1B_T0_OWNER_KILLED__CONDITIONAL_PRE_SHIAB_DEFECT_ACTION_NONNULL_BV_SYMBOL_EXACT__GLOBAL_SOLDERING_WELD_AND_NULL_DOMAIN_OPEN
---

# Conditional physics ledger v0.5

## Progress meter

```text
Ledger v0.5 — 82/82 active target rows mapped (100% of current denominator)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Current I1B T=0 pre-Shiab owner: killed at the selected-Shiab value Hessian
Repaired fixed-slot non-null even-BV quotient: rank 16 exact
Residue — 83 continuous real + >=19 function-valued + 10 open discrete forks
Quotients ranked: 1 conditional/local; no global residue reduction booked
```

Coverage, verdict counts and global residue are unchanged. `LT-GR2c` moved
closer: the old action-owned horn is now ruled out at a precise value locus,
and an explicit repaired horn has an exact local quotient. The repair still
needs a global equivariant soldering map, a nonduplicating nonlinear action
weld and a null/Green domain before it can count as physical recovery.

## Row movements

| row | verdict/kind | v0.5 result | distance |
| --- | --- | --- | --- |
| `LT-GR2b` variable distortion/VEV | `SAME/DERIVED_PARTIAL` | source `theta` and action `T=A-B` are the same connection-difference object up to the tilted trivialization; the ambient Euler row is action-owned | select a nonzero vacuum branch and carry it through the observed equation dual |
| `LT-GR2c` curvature covariation | `NEEDS/MISSING_CONSTRUCTION` | current `I1B` cannot own the pre-Shiab receiver at `T=0`; a repaired fixed-gravitational-slot action has an exact non-null `4 -> 20 -> 20 -> 4` even-BV symbol complex and quotient rank 16 | construct global `sigma_epsilon`, weld the term into the one action, and derive nonlinear/null-domain closure |
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

## The repaired horn and its missing soldering map

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
two-tensor. A gravitational soldering map `sigma_epsilon` is therefore
load-bearing. The repository owns the moving `epsilon_IG` field and fixed-frame
gravitational slots, but not yet a global ten-dimensional equivariant map. The
tautological trace vector supplies only one line. Consequently this action is
`PUT_IN_BY_CONSTRUCTION` only on the fixed-slot conditional horn; the ledger
row remains `NEEDS/MISSING_CONSTRUCTION` globally.

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

1. `LT-GR1b/LT-GR2c`: construct the global equivariant
   `epsilon_IG` gravitational soldering map `sigma_epsilon` and weld the
   repaired horn nonduplicatingly into the one bulk/defect action.
2. `LT-GR2b/c/d` plus `LT-SM8`: extend the exact local even-BV complex through
   nonlinear Ward/BV closure and the null characteristic/Green domain.
3. `LT-GR2b/d`: only then construct/select a nonzero vacuum branch and repeat
   the independent vacuum-shift test.
4. `LT-GR2e`: derive FLRW and perturbations from that action-owned branch.

Evidence, controls and source return:
`pre-shiab-gauss-defect-action-bv-symbol-2026-08-05.md` and
`pre-shiab-gauss-defect-action-bv-source-reinspection-2026-08-05.md`.
The new repaired-action/BV claim is `SOURCE-SILENT`; it is not attributed to
Weinstein or Curt.
