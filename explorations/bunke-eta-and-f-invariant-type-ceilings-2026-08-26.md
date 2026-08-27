---
artifact_type: exploration_result
doc_type: primary_source_topology_specialization
created: 2026-08-26
status: exploration
claim_verdict: ETA_E_DICTIONARY_EXISTS__INTEGER_BRIDGE_ABSENT__F_ROUTE_MISTYPED
title: "Bunke eta/e dictionary and f-invariant domain: exact type ceilings for M-H8 and M-M6"
grade: "PRIMARY-SOURCE SPECIALIZATION plus exact arithmetic/type certificate. Bunke's universal eta invariant derives Adams e as a special case. Bunke--Naumann's cited f-invariant has an even stable-stem domain and requires codimension-two almost-complex corner data. No universal-eta value, f-invariant value, GU class map, integer count or physical identification is constructed."
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
row_change: M-H8_AND_M-M6_EXECUTED_AT_TYPE_CEILING
scripts:
  - tests/channel-swings/bunke_eta_f_invariant_type_ceiling.py
---

# Bunke eta/e dictionary and f-invariant domain

## Result

M-H8 is right that the missing dictionary exists, but its proposed consequence
must be narrowed. Bunke's universal eta invariant is a bordism invariant from
APS eta data, and the paper explicitly derives the Adams `e`-invariant as a
special case. Thus the repository may not say that no eta-to-e dictionary
exists.

That dictionary does not turn a torsion detector into an integer generation
count. A nonzero class in `Z/3` can map nontrivially to `Q/Z` (the two nonzero
characters take values `1/3` and `2/3`), while every group homomorphism
`Z/3 -> Z` is zero because `Z` is torsion-free. The universal-eta/e route can
detect or characterize torsion; it supplies no canonical integer-cardinality
map. Gap (iii), the order/class-to-count dictionary, therefore remains open.

M-M6's requested “first number on the `RP3 x S6` model” is not admissible
under the cited Bunke--Naumann theorem. Their `f`-invariant is displayed on
`F^2 pi_m^S / F^3 pi_m^S` for `m=2k-2`, hence even `m`, and its geometric
recipe requires the framed input to occur as a codimension-two corner of an
almost-complex manifold. The filed model has dimension `3+6=9`; the registered
`alpha_1 beta_1` posit has degree `3+10=13`. Neither odd degree lies in the
displayed even domain, the two objects are not dimensionally identical, and no
owned adapter or corner supplies the missing input. No first number exists to
compute on the present packet.

Scope: secondary/tertiary index-theory typing and exact torsion arithmetic.
No source claim, generation count, GU class realization, canonical verdict,
ledger row, prediction or public posture changes.

```gu-typed-objects
result: Bunke universal eta specializes to Adams e, but no torsion-to-integer count map follows; the filed RP3-times-S6 model and alpha1-beta1 posit are outside the cited f-invariant input as currently typed
carrier: framed stable-homotopy or bordism class with the exact orientation and corner data required by the cited invariant LAYER=toy CHIRALITY=N/A
pairing: NONE
real_structure: NONE
grading: stable-stem degree and Adams-Novikov filtration are explicit and not interchangeable with manifold-factor dimensions
action_owner: repository-construction applying standard mathematics; no GU source action is supplied
target: M-H8 eta/e specialization and M-M6 first-number proposal MAP-TYPE=not-a-map
```

## Preflight bookend

### Object and claim typing

- `eta^univ`: Bunke's universal bordism invariant obtained from APS eta data.
- `e`: Adams' torsion-valued secondary invariant, recovered as a special case.
- `f`: Laures' tertiary invariant as specialized by Bunke--Naumann on the
  stated filtration-two, even-stem domain.
- `RP3 x S6`: a 9-dimensional working model, not a 13-dimensional link.
- `alpha_1 beta_1`: the registered degree-13 stable-stem posit.
- Integer generation count: a cardinality in `Z`, not a value in `Q/Z` or a
  divided-congruence quotient.
- Claim ceiling: correct the existence/domain statements and reject the
  current computation request; do not claim the underlying torsion class is
  absent or physically realized.

### Primary-source custody

- Ulrich Bunke, *On the topological contents of eta invariants*, arXiv
  `1103.4217v3`, abstract and the Adams-e specialization: the universal
  eta-based bordism invariant has Adams `e`, rho and String-bordism invariants
  as special cases.
- Ulrich Bunke and Niko Naumann, *The f-invariant and index theory*, arXiv
  `0808.0257`, introduction and Definition 5.2: the paper relates its analytic
  and topological tertiary invariants to Laures' `f`, with input
  `F^2 pi_m^S/F^3 pi_m^S` for even `m=2k-2`; the geometric recipe requires a
  codimension-two corner of an almost-complex manifold.

The source check was done before derivation. The repository already carried
the paper identifiers but had not specialized their domains to the filed
objects.

### Routes considered

1. **Declare universal eta equal to an integer count.** Rejected by codomain:
   torsion-valued detection and integer cardinality are distinct typed maps.
2. **Compute `f` on `RP3 x S6`.** Rejected by degree and missing-corner input.
3. **Treat `3+6` as `3+10`.** Rejected by exact dimension arithmetic and the
   existing M-M28 link-model fence.
4. **Record the exact type ceilings.** Selected; it closes the current register
   actions without inventing a new object.

## Exact certificate

`tests/channel-swings/bunke_eta_f_invariant_type_ceiling.py` proves:

- `dim(RP3 x S6)=9`, while the registered product degree is `3+10=13`;
- every displayed `f`-domain degree `m=2k-2` is even, so neither 9 nor 13 is
  admitted by this theorem;
- `Hom(Z/3,Z)=0`, while `Hom(Z/3,Q/Z)` has the expected three characters;
- the filed `e_R=1/12` has order 12 and 3-primary projection `1/3` of order 3;
- a detector value `1/3 mod Z` is not an integer count; and
- 4/4 planted false-dimension, false-domain, nontrivial-integer-map and
  codomain-conflation mutations are caught.

## Hostile review and maximum conclusion

1. **Strongest overclaim.** “No eta route can see odd torsion” would be false;
   the filed `e_R=1/12` itself contains a nonzero 3-primary component.
2. **Strongest contrary route.** A differently defined detector, suspension,
   product construction or correctly typed corner may still detect the
   13-stem. This result rejects only the current Bunke--Naumann application.
3. **Weakest seam.** The paper specializations are theorem-applied rather than
   re-proved from spectrum-level foundations. The exact certificate guards the
   repository's arithmetic and typing, not the original theorems.

Disposition:

- M-H8: `EXECUTED` at the specialization/type ceiling. The dictionary exists;
  the integer-count bridge does not follow.
- M-M6: `EXECUTED` at the domain-typing ceiling. The proposed present-model
  computation is inadmissible and returns no `f` value.

## Postflight bookend

- Intended effect: decide whether the two register proposals license their
  stated topology computations.
- Actual effect: one dictionary is confirmed and narrowed; one computation is
  rejected before execution by two independent type failures.
- Controls: exact degree/codomain certificate plus four planted mutations.
- Compatible work left: a correctly typed even-stem corner packet or another
  invariant on an owned 13-dimensional carrier; neither currently exists.
- Capacity/closure: the registered questions reach their current decision
  ceilings. No protected correction or canon edit is absorbed.
- Next conditions: reopen M-H8 only on an explicit physical/count adapter;
  reopen M-M6 only on an owned input satisfying the chosen invariant's exact
  degree, framing and corner hypotheses.
