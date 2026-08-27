---
artifact_type: exploration_result
doc_type: functorial_class_map_gate
created: 2026-08-27
status: exploration
claim_verdict: FUNCTORIAL_STATEMENT_CLOSED__GU_CLASS_REALIZATION_UNDEFINED
title: "Pin-plus invertible field theory: the exact class-map truth table for M-M12"
grade: "PRIMARY-SOURCE-SCOPED FUNCTORIAL STATEMENT plus EXACT finite-group certificate. The ambient group Omega^Pin+_14 = Z/2 is inherited from the repository's promoted derivation. No GU cycle, anomaly character, operator family, firewall protection or physical boundary theory is constructed."
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
row_change: M-M12_EXECUTED_AT_FUNCTORIAL_CLASS_MAP_TYPING_CEILING
scripts:
  - tests/channel-swings/pin14_invertible_field_theory_class_map.py
---

# Pin-plus invertible field theory and the GU class map

## Result

M-M12's functorial statement is now explicit. At the ordinary closed-manifold
shadow, an invertible Pin-plus topological field theory supplies a multiplicative
phase on bordism classes. For the already-derived ambient group
`G = Omega^Pin+_14 = Z/2`, there are exactly two `U(1)`-valued characters: the
trivial character and the sign character.

| character | class 0 | class 1 |
| --- | ---: | ---: |
| trivial | +1 | +1 |
| sign | +1 | -1 |

The only nontrivial phase requires both a nontrivial character and a realized
generator class. A nonzero ambient bordism group is not itself an anomaly, and
a nontrivial invertible theory does not detect a cycle that has not been
constructed. The current GU class remains undefined: no complete program-native
closed/Fredholm Pin-plus 14-cycle, deck action, orientation-line datum, bordism
class map and generator detector is present.

Thus the precise current statement is conditional: if `chi_GU` is the sign
character and `c_GU` is the generator, then `chi_GU(c_GU)=-1`; otherwise this
Pin-plus route supplies no nontrivial phase. This closes the requested
axiomatization and sharpens `ANOMALY-DESCENT T1` to the construction of `c_GU`
and the relevant character. It does not establish that the firewall has a
Pin-plus anomaly home. Other protection mechanisms are outside this packet.

Scope: bordism-to-character typing and exact finite-group logic. No source
claim, scientific-ledger row, canon verdict, prediction, confirmation or public
posture changes.

```gu-typed-objects
result: the closed-manifold invertible-field-theory shadow on Omega^Pin+_14=Z/2 has trivial and sign characters, and only the sign character evaluated on a realized generator gives phase -1
carrier: Pin-plus degree-14 bordism classes in the already-derived ambient group; the GU class is UNTYPED LAYER=toy CHIRALITY=N/A
pairing: character evaluation chi(c) ON=Omega^Pin+_14
real_structure: Pin-plus tangential structure is required; the program-native lift is UNTYPED
grading: bordism degree 14; boundary-relative degree shifts are not identified with a GU cycle
action_owner: repository-construction states the functorial interface; source-action ownership of a GU class is UNTYPED
target: M-M12 functorial anomaly/class-realization question MAP-TYPE=evaluation
```

## Preflight bookend

### Object and claim typing

- `G`: the ambient Pin-plus bordism group, already derived in repository canon.
- `chi`: a multiplicative `U(1)`-valued phase on closed bordism classes, the
  partition-function shadow used here rather than a reconstruction of the
  complete extended theory.
- `c_GU`: the proposed GU bordism/operator-family class. It is not the ambient
  group and is currently undefined.
- Relative boundary theory: a theory defined relative to an ambient/invertible
  theory in the Freed--Teleman sense. No GU relative functor is constructed.
- Claim ceiling: state and exhaust the exact logical interface; do not infer a
  GU anomaly or physical wall.

### Primary-source custody

- Daniel S. Freed and Michael J. Hopkins, *Reflection positivity and invertible
  topological phases*, arXiv `1604.06527`: reflection-positive invertible field
  theories are classified through stable homotopy and Thom/bordism spectra for
  a fixed symmetry type.
- Daniel S. Freed and Constantin Teleman, *Relative quantum field theory*,
  arXiv `1212.1692`: anomalous/boundary theories may be formulated relative to
  an ambient field theory; this does not assign a GU class.
- Repository input: `canon/pin14-bordism-derivation-RESULTS.md` derives the
  ambient `Z/2` and keeps class realization open;
  `tests/channel-swings/pin_smith_class_realization_gate.py` inventories the
  missing program-native interface.

The sources were checked before the statement was frozen. The exact `Z/2`
character table is elementary repository-owned arithmetic.

### Routes considered

1. Ambient group equals anomaly: rejected because a receptacle, character and
   particular cycle are distinct objects.
2. Nontrivial character detects an undefined cycle: rejected because evaluation
   is undefined until the class exists.
3. Trivial phase proves no possible protection: rejected because it only
   removes this declared invertible-anomaly route.
4. Freeze the full truth table and missing interface: selected.

## Exact certificate

`tests/channel-swings/pin14_invertible_field_theory_class_map.py` proves the two
characters and their exact `(+1,+1,+1,-1)` truth table; an undefined class emits
no phase; the ten-candidate inventory has no complete program-native input; and
4/4 planted group/class, zero/generator, undefined/evaluated and
trivial/protected conflations are caught after a clean baseline.

## Postflight bookend

- Intended effect: make M-M12 executable without using the nonzero ambient
  group as a surrogate for GU class realization.
- Actual effect: the functorial shadow and exact truth table are closed; the GU
  class, character and physical relative theory remain unbuilt.
- Strongest overclaim: saying the firewall has no home globally. This packet
  decides only this Pin-plus invertible-anomaly route.
- Strongest contrary route: a future source-owned compact/Fredholm cycle plus
  Pin-plus lift, deck/orientation data and nontrivial detector can still realize
  the generator and phase `-1`.
- Weakest seam: the full extended classification is cited, while the executable
  certifies only its ordinary closed-manifold character shadow.
- Next condition: reopen only when `c_GU` or its equivalent Fredholm/relative
  field-theory object is constructed with all required ownership and domain data.
