---
title: "K1127 K887 T=0 gauge-carrier correction"
status: active_research
doc_type: correction
created: 2026-10-05
claim_ceiling: exact native-coordinate gauge-carrier correction
manifest: lab/process/k1127-k887-t0-gauge-carrier-correction.json
probe: tests/channel-swings/k1127_k887_t0_gauge_carrier_correction_probe.py
target_claim: SC-ACT-06
---

# K1127 K887 T=0 gauge-carrier correction

> **GU-COMPARATOR-ROUTING — scope before inference.** This separates the
> native source-action gauge carrier from a frozen connection-only control.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: corrected native T=0 action-owned gauge carrier
carrier: native (g,T) variables versus frozen connection-only radial slice LAYER=source-print+toy BRIDGE=typed_separation CHIRALITY=N/A
pairing: NONE
real_structure: real infinitesimal diffeomorphism columns
grading: exact carrier correction; no physical quotient
action_owner: source-action -- rank-four metric diffeomorphism image only
target: SC-ACT-06 MAP-TYPE=evaluation
```

The native variable is the connection difference `T=varpi-B_LC(g)`. It
transforms tensorially. At `T=0`, the source action therefore owns the
rank-four metric diffeomorphism columns already recorded by K720, not an
independent `d chi` distortion column.

K887's `16384`-dimensional radial control and rank-`8191` response remain
exact on their declared connection-only slice. They are not the action-owned
T=0 gauge image and cannot establish a Noether/gauge-descent failure for the
native `(g,T)` Hessian. The producer passes `13/13`; the hostile probe rejects
`13/13` mutations. No protected status moves.
