---
artifact_type: exploration
created: 2026-08-05
title: "Pre-contract Wave 0B: the advertised three-trace rerun is ill-typed; the ambient kill survives locally, while observed gravity needs a new adapter"
grade: "EXACT local linear-algebra/type theorem plus primary-source collision. It does not construct the observed receiver, settle the full-domain Shiab, or recover gravity."
named_gate: PRECONTRACT-0B-TRACE-REVERSAL-ROBUSTNESS
gate_before: THREE_TRACE_HORNS_ASSUMED_COMPARABLE__BUILD_PRIMACY_UNDECIDED
gate_after: VERTICAL_TRACE_IS_UPSTREAM_AND_ALREADY_ACTIVE__AMBIENT_TO_OBSERVED_NAIVE_RESTRICTION_FAILS__ADAPTER_REQUIRED_BEFORE_BUILD_PRIMACY
route_disposition: TEMPORARILY_LEAD_WITH_COMPOSE_PLUS_SOURCE_TO_BUILD_OBSERVED_ADAPTER__THEN_RESUME_BUILD
source_collision: SOURCE-CORRECTS
fork_assumed: none
search_space_dim: "2 irreducible curvature response classes plus the rank-one fibre-metric update"
free_object_delta: 1
residue_touched:
  - "LT-GR1b:T2"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Pre-contract Wave 0B: trace-reversal robustness

## Result first

The proposed three-horn robustness test cannot be run as stated because its
three entries are different typed operations.

1. The **vertical Frobenius trace reversal** is a bilinear form on the
   ten-dimensional metric fibre `W = Sym²T*X`. It changes the ambient metric,
   Hodge star, Clifford raising, formal adjoint and action pairing. The active
   K77 calculation already uses it: raw fibre inertia `(7,3)` becomes `(6,4)`,
   and horizontal `(1,3)` plus that fibre is `(7,7)`.
2. The **ambient Einstein contraction** is a map from fourteen-dimensional
   algebraic Riemann curvature to `Sym²T*Y`. This is the object used by K77-B2
   and the principal-Bianchi selector.
3. The **observed Einstein contraction** is a map from four-dimensional
   curvature to `Sym²T*X`, after a section/reduction. The repo has not built the
   equation-level adapter that would make it comparable to item 2.

So the vertical operation is not an alternative horn to the ambient one; it is
already an upstream input to it. The observed operation is downstream and
requires an unbuilt adapter.

An exact control also kills the tempting fallback “just restrict the ambient
Einstein tensor to the observed four-plane.” On constant curvature, restriction
of `G_14` is `26` times `G_4`; on a horizontal traceless-Ricci fixture it is `6`
times `G_4`. Because `26 != 6`, no common scalar normalization makes the square
commute. A nontrivial projection, correction or mixed horizontal/vertical
receiver is required.

## Layer 0

| name | actual object | domain -> codomain | disposition |
| --- | --- | --- | --- |
| vertical Frobenius reversal | `B_0 -> B_1/2` on fibre metric variations | `Sym²T*X x Sym²T*X -> R` | upstream metric owner; already active in K77 |
| ambient Einstein contraction | `R -> Ric_14(R) - 1/2 Scal_14(R) g_Y` | `Riem(TY) -> Sym²T*Y` | exact ambient comparator |
| observed Einstein contraction | `r -> Ric_4(r) - 1/2 Scal_4(r) g_X` | `Riem(TX) -> Sym²T*X` | physical target after observation |
| same-action transgression | cubic Helmholtz/cyclic identity using the action pairing | fields and variations -> top density | depends on the same Hodge/pairing owners; not coefficient-only |

Layer 0 therefore rejects a three-value switch statement. The correct diagram
has multiple arrows and must be tested for commutation.

## Exact calculation

Let `H` be a Lorentzian four-plane and `V = H + W` have dimension fourteen.
For constant sectional curvature `K`,

`G_n = -((n-1)(n-2)/2) K g`.

Thus `G_14|H = -78 K g_H` while `G_4 = -3 K g_H`, a ratio of `26`.

For a trace-free symmetric tensor `S` supported on `H`, use the ambient
Kulkarni–Nomizu curvature

`R_14 = (S KN g_V)/(14-2)`.

Its ambient Ricci tensor is `S`, hence `G_14|H = S`. Restricting the curvature
first gives four-dimensional Ricci `(4-2)/(14-2) S = S/6`, hence
`G_4(R_14|H) = S/6`, a ratio of `6`.

The incompatible ratios are an exact obstruction to a scalar adapter. They do
not prove no richer observer/vertical adapter exists.

## What happens to GR-1b

The ambient displayed-family obstruction remains exact:

- principal Bianchi selects `comm/symi/symi` among the eight printed product
  assignments;
- its ambient Riemann restriction equals `-2 G_14`;
- the same displayed cubic transgression forces that factorized map to zero.

But the ledger must not promote this into a falsification of observed GU
gravity. Its correct compositional typing is:

```text
verdict: OVER_DETERMINED
reason_kind: SCOPE_ERROR
scope: DISPLAYED_FACTORIZED_AMBIENT_14D_ANSATZ
distance: construct one equation-level observed receiver and rerun the full
          pairing/adjoint/transgression square
revival_trigger: an exact source-natural adapter with nonzero scalar and
                 traceless-Ricci response
```

Inside its declared ambient scope, the no-survivor result is still a genuine
displayed-ansatz kill. The `SCOPE_ERROR` diagnosis attaches to reading that
local kill as the observed-physics row.

## Channel decision

Do **not** preassign Build primacy yet. Build has constructed and killed a real
ambient object, but the North-Star question is an observed four-dimensional
equation. The cheapest decisive next work is compositional/source construction:

1. specify the equation receiver after Hodge/Krein primalization;
2. include the horizontal/vertical soldering and moving-section owners;
3. demand a commuting variational/transgression square;
4. then return the resulting target to Build.

This is a temporary ordering decision, not a demotion of construction.

## Kill and revival boundaries

- **Killed:** treating the three trace operations as values of one switch;
  treating naive restriction as the observed adapter; treating the vertical
  metric reversal as an unused rival to the active ambient calculation.
- **Alive:** a non-scalar, source-natural observed receiver; a full-domain
  nonfactorized Shiab; a coupled horizontal/vertical correction; the ambient
  construction as a component of that larger square.
- **Untouched:** particle content, P1/P2/P3, generation count, physical GR,
  Green domains, anomaly cancellation and cosmology.
