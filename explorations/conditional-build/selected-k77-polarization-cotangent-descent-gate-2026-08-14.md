---
artifact_type: exact_source_configuration_and_cotangent_descent_result
created: 2026-08-14
status: SOURCE_EPSILON_OWNS_DEPENDENT_DIM40_POLARIZATION_ORBIT__COTANGENT_DESCENT_IFF_SPLIT_CHARGES_VANISH__ACTUAL_ENDPOINT_CHARGE_DECOMPOSITION_OPEN
source_return: SOURCE_OWNS_FULL_LABELLED_MOVING_FRAME_AND_ACTION_ENDPOINT_MOMENTUM__REPO_DERIVES_DEPENDENT_SPLIT_ORBIT_AND_COTANGENT_DESCENT_CRITERION__SOURCE_SILENT_W_MIRROR_SELECTION_AND_REDUCED_BFV_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-polarization-cotangent-descent.json
canon_verdict_change: none
---

# Selected K77 polarization cotangent-descent gate

## Result first

The 40-dimensional moving W/mirror polarization does **not** require a new
independent field at configuration level. The source already owns the full
moving labelled Clifford frame through `epsilon`. Projecting its four labelled
base directions gives the dependent orbit

```text
Spin(7,7)/H_split,  dim = 91 - 51 = 40,
```

and the induced projector obeys `delta P=[X,P]`. Composing this orbit with the
repository-derived W recipe gives the covariant families
`Spin(7,7) x_H W` and `Spin(7,7) x_H mirror` with zero new configuration
coordinates. This corrects the v0.251 wording that the source owns no
polarization field: the source does not print W or select a member, but its
existing `epsilon` field owns the required moving carrier as a dependent
composite.

The correction does not yet close preboundary ownership. A full-frame endpoint
covector descends to `T*(Spin(7,7)/H_split)` if and only if it annihilates all
51 split-stabilizer directions. Equivalently, its charge has only the forty
mixed components. The canonical cotangent-lift moment map

```text
mu_X(P,Pi) = <Pi,[X,P]>
```

automatically vanishes on the stabilizer and can be nonzero on mixed
directions. A generic source-frame endpoint momentum need not satisfy that
condition. The selected action has a live unrestricted boundary moment map,
but its exact 51+40 charge decomposition has not been computed. Therefore the
configuration owner is now constructed while the reduced preboundary owner
remains an exact, decidable gate.

## Layer 0

| object | result | not established |
| --- | --- | --- |
| source `epsilon` | full moving labelled Clifford frame | observation section or W selection |
| split orbit | dependent 40-dimensional quotient of that frame | new independent edge field |
| W/mirror family | equal associated families under the orbit | selected luminous member |
| full-frame endpoint momentum | source-action preboundary covector | automatically reduced coset momentum |
| stabilizer annihilation | necessary and sufficient cotangent-descent condition | verified property of the actual endpoint bank |
| local orbit moment map | exact cotangent-lift formula | BFV charge algebra/master equation |

The source-owned labelled frame, the physical observation section, and the
codimension-one analytic boundary remain distinct. The observation section is
topology-dependent, and the codimension-ten observed copy is not itself the
Green boundary.

## Exact theorem

Let `P0` project the K77 vector space onto the labelled base axes
`{0,7,8,9}`. For the 91 bivector generators of `so(7,7)`, the orbit
differential is

```text
d pi_e(X) = [X,P0].
```

Its kernel is exactly
`so(1,3)+so(6,4)`, dimension 51, and its forty mixed columns are independent.
Thus the source-frame orbit has tangent dimension 40 and the induced projector
is a dependent field. The projector identity differentiates to
`P deltaP + deltaP P = deltaP`, which the exact certificate verifies.

Dualizing gives the sharp preboundary condition. A covector on the 91 frame
directions is pulled back from the orbit precisely when it annihilates the
kernel. The probe constructs both a mixed-only positive control and a covector
with one split component; the first descends and the second raises the row
space rank by one. No dynamical assumption enters this theorem.

## Broad route-changing lens census

- **Principal-bundle geometry — selected:** project the already-owned frame
  before adding any field; this removes forty false datum costs.
- **Representation theory — decisive:** the same 51/40 stabilizer split that
  preserves W controls the orbit differential.
- **Variational bicomplex — decisive successor:** configuration ownership does
  not imply that the source endpoint covector is basic.
- **Symplectic geometry — selected:** cotangent reduction turns the vague
  ownership question into the exact 51-charge annihilation test.
- **BRST/BFV — strict ceiling:** the local moment map is not a closed
  91-ghost master complex, and stabilizer charge cannot be silently discarded.
- **Source criticism — corrective:** source `epsilon` owns the carrier, while
  W, mirror selection, charge decomposition and analytic domain remain
  repository/unbuilt layers.
- **Analytic/PDE — deferred:** no codimension-one boundary, closedness,
  Lopatinski/Calderon condition or propagation estimate follows.
- **Philosophy of science — anti-fitting:** dependency on an existing field is
  cheaper and more faithful than installing forty compensators, but does not
  count as physical selection.

The structural orbit/cotangent route dominated direct BFV construction because
it first determines which variables are independent and the exact obstruction
to reduced momentum. The fallback independent-coset route is unnecessary at
configuration level. It revives only if the source-frame equivariance fails;
the exact rank/equivariance controls show that it does not.

## Hostile boundary

The strongest overclaim is that the source action now owns the complete
polarization dynamics. It does not. The source owns `epsilon`; the repository
derives the split projection and W functor. The actual endpoint momentum may
carry split-stabilizer charge, in which case it cannot descend to the coset
without additional constraints, reduction, or an edge completion.

The strongest contrary reading is that no physical W field was derived. That
is correct and compatible with the result: a covariant dependent family is not
a selected member or physical cohomology. The mirror family is equally owned.
Global sections may be obstructed, and the physical observation and analytic
boundary burdens remain.

## Progress and next gate

No ledger verdict, residue, datum, quotient, generation count, canon claim or
public posture changes. Four rows move in distance only: configuration-field
ownership closes, while reduced preboundary/BFV ownership remains open.

Next decompose the **actual selected action endpoint momentum** into its 51
split and 40 mixed charge components on the source `epsilon` orbit. If every
split component vanishes, construct the reduced orbit moment map and then the
91-ghost BFV master equation. If any split component survives, derive the
corresponding constraint/reduction or retain the larger edge completion. Do
not choose W or mirror, declare the orbit physical cohomology, or begin the
analytic domain before the charge test closes.

## Reproduction

```sh
python tests/channel-swings/selected_k77_polarization_cotangent_descent_gate_probe.py
```

The exact probe passes all declared checks and validates the machine-readable
registry.
