---
title: "K1082 positive functional Hamiltonian"
status: active_research
doc_type: conditional_functional_hamiltonian_conservation_theorem
created: 2026-10-04
claim_ceiling: exact constant-coefficient energy-domain theorem for the repository-owned candidate
manifest: lab/process/k1082-k1081-functional-hamiltonian.json
probe: tests/channel-swings/k1082_k1081_functional_hamiltonian_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1082 positive functional Hamiltonian

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> Hamiltonian construction, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_HAMILTONIAN`.

```gu-typed-objects
result: the K1081 Hessian generates an energy-skew first-order flow on one Sobolev energy domain
carrier: H1(T3;R^r) direct-sum L2(T3;R^r) LAYER=observed CHIRALITY=N/A
pairing: E(q,p)=<q,Hq>+<p,p> ON=candidate_action
real_structure: real classical phase space
grading: position and canonical-momentum blocks
action_owner: repository-construction -- K1036 candidate only
target: functional Hamiltonian generator on the energy domain MAP-TYPE=homomorphism
```

For the positive self-adjoint `H` from K1081, define

```text
K(q,p) = (p,-Hq),
D(K) = H2(T3;R^r) direct-sum H1(T3;R^r).
```

The block identity from K1076 now holds on an actual generator domain: `K` is
skew for the energy pairing, so smooth solutions conserve `E`. With `B,C>0`
the energy is coercive; if `C` is merely semidefinite, the zero-mode radical
must be treated separately rather than called positive by fiat.

Three exact modal controls at squared frequencies `1,3,7` have zero energy
defect. The producer passes `10/10`; the hostile probe rejects `12/12` domain,
generator, positivity, ownership and scope mutations. No nonlinear
interacting BV domain or dissipative resource follows.
