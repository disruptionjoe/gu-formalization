---
title: "K1147 closed-range Hausdorff cohomology"
status: active_research
doc_type: exact_hilbert_cohomology_closed_range_gate
created: 2026-10-05
claim_ceiling: exact closed-range and Hausdorff-quotient criterion; no source BV/BFV range theorem
manifest: lab/process/k1147-closed-range-hausdorff-cohomology.json
probe: tests/channel-swings/k1147_closed_range_hausdorff_cohomology_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1147 closed-range Hausdorff cohomology

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem tests the
> topology of a supplied Hilbert complex. It does not construct the source
> gauge differential or identify the quotient with physical states. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact closed-range gate for Hausdorff degree-zero Hilbert cohomology
carrier: Hilbert complex G0 --d--> V --Q--> C LAYER=source-print CHIRALITY=N/A
pairing: inherited Hilbert topology on ker Q modulo im d ON=degree-zero-cohomology
real_structure: real or complex Hilbert complex; source real form not supplied
grading: gauge image, constrained cycles and topological quotient
action_owner: comparator -- d and Q require a separately source-owned complex
target: K1145 positive-nonzero-cohomology gate MAP-TYPE=quotient
```

Algebraic `Qd=0` only gives the vector-space quotient

```text
H0_alg = ker Q / im d.
```

With the inherited Hilbert topology, this quotient is Hausdorff exactly when
`im d` is closed in `ker Q`. For a bounded diagonal family of finite-fibre
maps, closed range is equivalent to a uniform positive lower bound on all
nonzero singular values.

The failure control is exact. On `ell2(N)`, let `d` multiply the `n`th
coordinate by `1/n`. Its range contains all finite-support sequences and is
dense, but it is not closed. The vector `y_n=1/n` belongs to `ell2`; its
finite truncations lie in the range and converge to `y`, while its only formal
preimage is `x_n=1`, which is not in `ell2`. Consequently the quotient by
`im d` is non-Hausdorff even though every finite fibre has a perfectly valid
algebraic image. The constant symbol `d_n=1` supplies the closed-range control.
The producer passes `12/12`; the hostile probe rejects `10/10` mutations.
