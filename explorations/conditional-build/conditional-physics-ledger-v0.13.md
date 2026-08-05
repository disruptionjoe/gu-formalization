---
artifact_type: conditional_physics_ledger_view
created: 2026-08-05
version: "0.13"
machine_source: lab/process/conditional-physics-ledger-v0.13.json
predecessor: lab/process/conditional-physics-ledger-v0.12.json
status: APPEND_ONLY_SELECTED_BRANCH_GAUSS_HESSIAN_AND_COMMON_DEFECT_KREIN_GREEN_DOMAIN_EXACT__OPPOSITE_RESIDUE_PARTNER_CLASSIFIED__PHYSICAL_COHOMOLOGY_AND_TWO_FIELD_COSMOLOGY_OPEN
---

# Conditional physics ledger v0.13

## Progress meter

```text
Ledger v0.13 — 82/82 active target rows mapped (100% of current denominator)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Selected branch, radial Cl1: eigenvalue -kappa_1
Selected branch, Gauss trace/traceless: 100/117 and 124/117 times kappa_1
Gauss native inertia: (54,46); nondegenerate but indefinite
Observed TT: one massless pole + partner mass^2=124*alpha_II*kappa_1/117
Pole residues: +1/alpha_II and -1/alpha_II
Common domain: coupled normally-hyperbolic observed defect Krein/Green complex
Residue — 84 continuous real before quotient + >=19 function-valued
          + 9 open discrete forks
Quotients ranked: 2 local/defect symbol quotients; physical cohomology open
```

Coverage, verdict counts and residue are unchanged. The material movement is
inside seven row distances: the selected branch is now linearized on the
correct gravitational carrier, one common observed Green domain is closed,
and the distinct partner is classified by mass sign and residue rather than
left as an unnamed extra pole.

## What changed

The predecessor's `-14*kappa_1` radial Hessian is real, but it lives in the
invariant Clifford-one branch direction. The second fundamental form lives in
the Clifford-two Gauss carrier. Direct differentiation of the same selected
action gives

```text
trace II:      (100/117)*kappa_1 times the native pairing
traceless II:  (124/117)*kappa_1 times the native pairing.
```

The full Gauss pairing has inertia `(54,46)`, split as trace `(6,4)` and
traceless `(48,42)`. Therefore the radial negative mode cannot be imported as
the gravitational sign. The gravitational Hessian is nondegenerate but still
indefinite for either sign of `kappa_1`.

On the TT sector the exact two-field pencil is

```text
[[alpha_II*z, z], [z, (124/117)*kappa_1]]
```

with one massless pole and partner
`m_GU^2=(124/117)*alpha_II*kappa_1`. The residues are opposite. This is a
ghost warning on a positive-Hilbert reading; in the native Krein setting it is
a concrete BV/physical-cohomology gate, not an automatic rejection and not a
sign that may be ignored.

Keeping `(h,v)` coupled makes the operator second order. Its kinetic matrix
has determinant `-1`, so multiplication by its inverse gives a scalar wave
principal symbol plus a `K`-self-adjoint lower-order endomorphism. On the
inherited globally hyperbolic observed defect, harmonic gauge therefore gives
one common advanced/retarded Krein/Green domain. The ambient `(7,7)` problem
remains open.

## Stress, current and totalization

At a stationary solution, linearizing the complete even Ward identity gives

```text
R^! H = 0 = H R.
```

For a connection that depends on metric/soldering data, one scalar action
forces

```text
T_reduced = E_g^direct + (D_g A)^! J_A.
```

This types the current/stress chain and preserves Hessian reciprocity. The
Gauss insertion adjoint owns the `II` equation, but the actual full
metric/coframe derivative of the unified connection is still required before
the whole Hilbert tensor is reconstructed from the connection side. The
source return is `SOURCE-CORRECTS`: Weinstein's material names an unfinished
up-and-back path, not a literal current-equals-stress formula.

## Direct shift versus the actual magnitude argument

Adding a direct algebraic source `rho` to the selected invariant branch gives

```text
dt/drho at t* = 1/(14*kappa_1).
```

That branch responds rather than screens. This is not a refutation of
Weinstein's actual dark-energy magnitude argument, which identifies a
dark-energy field with a curvature-side field and claims two unexplained
values reduce to one. The next cosmology gate must build and count that
two-field system directly.

## Row movements

| row | v0.13 disposition | distance now |
| --- | --- | --- |
| `LT-GR1` | `SAME/DERIVED_CONDITIONAL` | full metric/coframe soldering derivative and physical cohomology |
| `LT-GR2b` | `SAME/DERIVED_PARTIAL` | curved/background BV quotient; Gauss Hessian is exact but indefinite |
| `LT-GR2c` | `NEEDS/MISSING_CONSTRUCTION` | actual two-field curvature/VEV equation and physical partner quotient |
| `LT-GR2d` | `NEEDS/MISSING_CONSTRUCTION` | rank the two-field parameter reduction and independent-shift response |
| `LT-GR3` | `DIFFERS/STRUCTURAL_DIFFERENCE` | decide the exact opposite-residue partner in BV physical cohomology |
| `LT-GR5` | `DIFFERS/STRUCTURAL_DIFFERENCE` | complete the augmented-torsion physical spectrum |
| `LT-GR6` | `DIFFERS/STRUCTURAL_DIFFERENCE` | instantiate the direct-plus-soldered chain with full `D_g A` |

All other rows, external P1/P2/P3, canon, Lane count and public posture remain
unchanged.

## Next gate

```text
CONSTRUCT_SELECTED_BRANCH_FULL_METRIC_COFRAME_SOLDERING_DERIVATIVE_AND_BV_PHYSICAL_COHOMOLOGY_FOR_THE_OPPOSITE_RESIDUE_PARTNER__IN_PARALLEL_BUILD_THE_OBSERVED_TWO_FIELD_CURVATURE_VEV_FLRW_PARAMETER_COUNT_AND_SHIFT_RESPONSE
```

Evidence:

- `selected-branch-linearized-totalization-current-green-domain-2026-08-05.md`;
- `selected_branch_linearized_totalization_domain_probe.py`;
- `selected_branch_linearized_totalization_domain_independent.sage`; and
- `2026-08-05-selected-branch-totalization-domain-review.md`.
