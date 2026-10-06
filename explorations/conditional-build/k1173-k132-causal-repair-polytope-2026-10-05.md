---
title: "K1173 K132 causal repair polytope"
status: active_research
doc_type: source_i1b_causal_three_resource_boundary
created: 2026-10-05
claim_ceiling: strongest-favorable finite-symbol repair floors; no source repair constructed
manifest: lab/process/k1173-k132-causal-repair-polytope.json
probe: tests/channel-swings/k1173_k132_causal_repair_polytope_probe.py
target_claim: SC-ACT-06
---

# K1173 K132 causal repair polytope

> **GU-COMPARATOR-ROUTING — scope before inference.** This grants the joint
> finite epsilon channel its unproved full rank `98`. The grant is only the
> most favorable baseline; actual overlap or rank loss raises every floor.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: causal repair-resource polytope for the selected K132 parent
carrier: K132 g-plus-T field symbol of dimension 229386 LAYER=source-print CHIRALITY=N/A
pairing: selected I1B Hessian plus a future quotient pairing ON=causal-covector-strata
real_structure: native real variables with finite ranks after complexification
grading: Hessian image, rank-four gauge image and favorable joint epsilon channel
action_owner: source-action -- repair resources unowned
target: LT-SM8/LT-GR6b/RA-F1/AC-F1 MAP-TYPE=evaluation
```

Using K132 Hessian ranks `130912/130912/122748`, current gauge rank four and
the strongest favorable joint-channel ceiling `98`, K1171 gives the remaining
causal deficits

`98372 / 98372 / 106536`.

For added actual ranks `(Delta h,Delta g,Delta c)`, every successful packet
must lie in the half-space

`Delta h + Delta g + Delta c >= deficit`.                     (2)

The three single-axis corners are exact lower bounds:

- constraint-only total ranks `98470/98470/106634`;
- gauge-only total ranks `98376/98376/106540`; and
- changed-parent Hessian rank at least `229284` on every stratum.

These are necessary ranks only. They supply no action owner, cochain,
propagation, radical equality, common domain, closed range, positive gap or
maximal generator. Protected verdicts do not move. Producer and hostile probe
pass `12/12` and `12/12`.
