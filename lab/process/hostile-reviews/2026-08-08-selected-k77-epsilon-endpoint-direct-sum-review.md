---
artifact_type: hostile_review
created: 2026-08-08
status: PASS_WITH_MATERIAL_SCOPE_REPAIR__ENDPOINT_AND_DIRECT_SUM_EXACT__ACTION_MOMENTUM_WELD_OPEN
subject: selected-k77-epsilon-endpoint-direct-sum-2026-08-08.md
---

# Hostile review: K77 epsilon endpoint direct sum

## Review result

The exact local endpoint and direct-sum results survive.  The initial stronger
reading—"epsilon now owns the v0.70 edge pair"—does not.  It was one inference
ahead of the artifacts and was removed before ledger migration.

## Divergent lenses

| lens | attack | result |
| --- | --- | --- |
| symplectic geometry | Does the direct-sum kernel equal, rather than merely contain, the endpoint gauge orbit? | Yes: rank 16, kernel eight, endpoint orbit rank eight; tenfold scalar quotient is `40/40`. |
| variational bicomplex | Are the two oriented endpoint coefficients action-derived? | v0.25 derives `i_n(E_B-E_T)` and v0.69 derives `p=KT`, but their equality is not yet coefficientwise constructed. Material repair. |
| principal-bundle geometry | Are arbitrary global endpoint values being assumed? | No. The result is restricted to a collar and the identity-component/local trace map. |
| PDE/domain theory | Is two-endpoint evaluation surjective on the stated domain? | Yes locally by affine interpolation; no global trace/domain theorem is claimed. |
| groupoid geometry | Did the construction quietly restore the one-holonomy compression? | No. It uses two independent endpoint copies and preserves independent momenta. |
| representation theory | Is a `GL(2,Q)` fixture being promoted to the K77 gauge group? | No. It certifies a universal matrix cotangent identity; K77 ownership remains the prior `U(64,64)` result. |
| source criticism | Does Weinstein identify epsilon with BFV edge modes? | No. Source confirms epsilon and the primitive chain and is silent on the BFV identification. |
| Krein/operator theory | Is symplectic nondegeneracy being called positivity or a common domain? | No. Both remain open. |
| exact-computation audit | Do planted diagonal endpoint, inert cotangent and wrong-orientation controls fire? | Yes. Main exact and independent Sage routes pass. |
| truth-propagation audit | Was the Run defending a gap already solved elsewhere? | Partly. v0.25 already supplied the two endpoint evaluations; v0.73 had not composed them. |

## Two-sided hostile charges

### Where the summary outran the artifact

The first draft identified the epsilon Green coefficients `e0,e2` with the
contact momenta `p0,p2` because their types and endpoint signs matched.  The
artifacts name different derivatives: `i_n(E_B-E_T)` and `KT`.  The exact
symbolic comparison establishes the weld **condition**, not the weld.  The
status, report, registry and next gate were repaired accordingly.

### Where rigor defended a superseded or mistyped object

The v0.73 successor asked to derive two continuum endpoint evaluations.  The
v0.25 primitive-epsilon Green identity had already done that.  Rebuilding it
would have been depth-first rigor on a stale queue item.  The present Run
books the composition and preserves only the unresolved coefficient weld.

## Symplectic disposition

The direct-sum form is a valid local characteristic quotient and exactly
recovers the v0.70 `40/40` class.  This does not establish that the source
epsilon field supplies the extra edge one-form in the selected action.  Until
`i_n(E_B-E_T)=p_KT` is computed under the same receiver and orientation, the
v0.70 edge coordinates remain a conditional extension rather than existing
field traces.

## Acceptance

```text
endpoint trace theorem: PASS, local collar only
direct-sum dressing: PASS, exact 40/40
single-holonomy no-go: RETAINED
epsilon action ownership: OPEN, narrowed to coefficient weld
source disposition: CONFIRMS ingredients / SILENT identification
verdict or residue movement: NONE
P1/P2/P3: UNUSED
```

The result is accepted with the material scope repair retained.
