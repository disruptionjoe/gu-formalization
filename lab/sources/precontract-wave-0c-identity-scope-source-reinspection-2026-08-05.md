---
artifact_type: source_reinspection
created: 2026-08-05
named_gate: PRECONTRACT-0C-TYPED-IDENTITY-AND-THEOREM-SCOPE
source_collision: SOURCE-CORRECTS
---

# Source reinspection: two Shiabs, one spinor vertex, and no supplied adapter

## Collision result

The repo's phrase “GU's written Shiab `(1,0,1,0)`” conflates two source
surfaces.

| surface | source content | earned typing |
| --- | --- | --- |
| 2021 draft equations `9.2–9.3` | displayed Shiab built from invariant `Phi1/Phi2`, used in the bosonic/translation Euler system | `Omega²(ad P) -> Omega¹³(ad P)` |
| Portal `01:34:34–01:40:08`, `01:47:01–01:52:21` | a degree-changing adjoint operator suite; derivation/Bianchi behavior is load-bearing | confirms the adjoint suite and intent, not a product selector or spinor formula |
| UCSD 2025 `00:32:07–00:37:41` | a rolled Dirac/de Rham/RS gadget and an underdefined symbol returning spinor-valued two-forms to one-forms | hosts an `Omega²(E)->Omega¹(E)` motif; it does not print or select `(1,0,1,0)` |
| canon reconstruction | Clifford contraction `Phi_S(alpha tensor s)=sum e^a tensor c(i_a alpha)s` | a natural spinor-valued map `Omega²(S)->Omega¹(S)`; existence exact, attribution/selection open |
| SA-C2 / W125 T3 | `contract-(1/6)wedge`, the gamma-traceless interaction vertex | exact pointwise spinor-map line, deliberately replacing the canon contraction in that candidate |

## Disposition

`SOURCE-CORRECTS` the statement that Eric's one written Shiab is both the pure
spinor contraction and the adjoint degree-13 map. The public corpus instead
supports two related roles and supplies no equation identifying them.

The source does support the *program* of relating the bosonic and fermionic
complexes through a common obstruction. That motivates an adapter search. It
does not license an equality before the representation action, Hodge map,
spin-curvature injection/retraction and trace reversal are written down.

Consequently:

- SHIAB-04 and W125 T3 are the same **spinor-map line**.
- The `g=1` projector facet of SA-C2 and the Porrati–Rahman analytic template
  are different objects.
- The spinor-map line and the adjoint degree-13 Shiab remain distinct as
  written; an exact Riemann-restricted trace-reversal adapter is constructible,
  but the source does not provide the full-domain adapter.
