---
title: "K1142 constraint propagation defect certificate"
status: active_research
doc_type: exact_constraint_leakage_certificate
created: 2026-10-05
claim_ceiling: exact finite-dimensional propagation-defect certificate; no source map or functional closure
manifest: lab/process/k1142-constraint-propagation-defect-certificate.json
probe: tests/channel-swings/k1142_constraint_propagation_defect_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1142 constraint propagation defect certificate

> **GU-COMPARATOR-ROUTING — scope before inference.** This certificate detects
> leakage of a supplied constraint kernel. It does not turn a fitted projector
> or row evolution into source truth. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact basis-independent propagation leakage map
carrier: finite real field fibre with full-row-rank Q and supplied G LAYER=source-print CHIRALITY=N/A
pairing: auxiliary positive coordinate pairing defining P=I-Q*(QQ*)^-1Q ON=constraint-domain
real_structure: real matrices
grading: constrained kernel versus constraint rows
action_owner: comparator -- certificate evaluates a separately owned Q and G
target: K1140 propagation gate MAP-TYPE=evaluation
```

With the K1138 projector

```text
P = I - Q* (Q Q*)^-1 Q,
```

define the leakage map `E=QGP`. Because `im P=ker Q`,

```text
E=0  iff  G(ker Q) is contained in ker Q.                        (1)
```

For any kernel basis `Z`, the equivalent certificate is `QGZ=0`. Replacing
`Z` by `ZM` with invertible `M` preserves zero and rank, so the verdict is
basis independent. In the K1141 fixture the propagating generator gives the
zero row, while the single off-kernel entry gives `E=(0,1,0)`, rank one and
exact squared Frobenius norm one. The norm depends on the auxiliary coordinate
pairing; zero and rank do not. This supplies an exact falsifier for a proposed
finite symbol map, not a common functional domain or source derivation. The
producer passes `12/12`; the hostile probe rejects `10/10` mutations.
