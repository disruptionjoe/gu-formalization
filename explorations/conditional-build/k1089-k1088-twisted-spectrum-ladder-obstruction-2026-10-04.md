---
title: "K1089 twisted-spectrum common-ladder obstruction"
status: active_research
doc_type: conditional_twisted_spectrum_obstruction
created: 2026-10-04
claim_ceiling: exact flat-circle counterexample to a universal spatial ladder
manifest: lab/process/k1089-k1088-twisted-spectrum-ladder-obstruction.json
probe: tests/channel-swings/k1089_k1088_twisted_spectrum_ladder_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1089 twisted-spectrum common-ladder obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> complex flat-bundle counterexample, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_OBSTRUCTION`.

```gu-typed-objects
result: distinct flat holonomies obstruct one shared spatial ladder despite parallel commuting coefficients
carrier: two flat Hermitian line bundles over S1 LAYER=observed CHIRALITY=N/A
pairing: positive L2 Hermitian pairing ON=conditional_connection_hessian
real_structure: complex Hermitian counterexample
grading: two holonomy sectors and their covariant Fourier modes
action_owner: repository-construction -- not a GU connection
target: K1088 common-ladder condition MAP-TYPE=evaluation
```

Take the direct sum of flat circle connections
`nabla_alpha=d/dx+i alpha` with `alpha=0` and `alpha=1/2`. Their holonomies are
`+1` and `-1`. With parallel positive commuting `B=I` and `C=diag(1,4)`,

```text
omega_1,n^2=n^2+1,
omega_2,n^2=(n+1/2)^2+4.
```

The first restricted Laplacian begins `{0,1,1}` while the second begins
`{1/4,1/4,9/4}`. The total Hessian has an orthogonal branch eigenbasis, but
not a tensor-product basis built from one common scalar spatial eigenbasis and
fixed internal vectors. K1083's shared Fourier ladder survives curvature only
when cross-sector connection and boundary spectra are also identified.

The producer passes `12/12`; the hostile probe rejects `11/11` holonomy,
spectrum, product-basis and ownership mutations. This exact complex control is
not a claim about GU's source connection or physical spectrum.
