---
title: "K1184 native Upsilon admission audit"
status: active_research
doc_type: source_native_candidate_admission_audit
created: "2026-10-05"
claim_ceiling: admission audit only; no global complex, positivity, or claim-status change
manifest: lab/process/k1184-native-upsilon-admission-audit.json
probe: tests/channel-swings/k1184_native_upsilon_admission_audit_probe.py
target_claim: SC-ACT-06
---

# K1184 native Upsilon admission audit

> **GU-COMPARATOR-ROUTING — scope before inference.** This audits one
> source-native finite-symbol response against the existing I1B admission
> packet. It does not identify that response with a physical constraint or
> quotient. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: admission audit of the full raw Upsilon response J
carrier: K132 coupled metric-plus-distortion principal carrier LAYER=source-print CHIRALITY=N/A
pairing: selected I1B Hessian plus candidate response kernel ON=frozen-symbol-carrier
real_structure: complexified finite-symbol rank only
grading: source ownership, complement rank, gauge annihilation, radical capture and functional obligations
action_owner: source-action -- I1B/Upsilon packet
target: SC-ACT-06 and K1150 functional admission MAP-TYPE=evaluation
```

`J` passes three preliminary gates: source ownership on the frozen carrier,
measured causal complement rank, and annihilation of the owned metric gauge
image. It fails the two decisive finite-symbol gates: it leaves
`98308/98308/98311` radical dimensions after gauge, and even the favorable
rank-98 predecessor can reduce those only to `98210/98210/98213`.

The remaining K1150 obligations stay open rather than being scored as passes:
one complete graph domain, closed range, a uniform positive quotient gap,
maximal skew-adjoint evolution, and preserved boundary traces. Radical capture
already fails, so none can promote the candidate to a physical quotient.

SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains `UNCERTAIN`, and
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. The hostile probe rejects `10/10`
mutations.
