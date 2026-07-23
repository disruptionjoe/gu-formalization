# V15-1 physical-signature transfer audit

This directory contains a bounded executable comparison of three distinct
objects:

1. the existing compact/complexified `(4,0)+(5,5)` selected carrier;
2. one complex self-dual half of the physical `(3,1)+(6,4)` split; and
3. the real-form-stable Lorentzian closure obtained by adjoining the physical
   conjugate anti-self-dual half.

The distinction is load-bearing. The second object has complex dimension
`192`, but is not preserved by physical conjugation and is null for the
program-native invariant Krein form. The third object is preserved by physical
conjugation, has complex dimension `384`, and carries Krein signature
`(192,192)`. No positive-Hilbert form is substituted.

From the repository root:

```sh
../../../_local/venvs/research-compute/bin/python \
  tests/lorentzian-transfer/physical_signature_transfer_audit.py
```

Add `--json` for the runtime result. The script recomputes the carrier,
real-form action, Krein restrictions, physical conjugation behavior, and
class-C Hom-space census, then compares them with `V15-1-receipt.json`.

Scope exits are explicit: this does not construct the true `Y14` source action,
a physical-state projector, a positive-Hilbert completion, or a Fredholm/net
handedness index.
