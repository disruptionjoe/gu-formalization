---
title: "K992 K991 qutrit horn separator"
status: active_research
doc_type: conditional_phase_horn_separator
created: 2026-10-04
claim_ceiling: exact pairwise separation after imported system enlargement only
manifest: lab/process/k992-k991-qutrit-horn-separator.json
probe: tests/channel-swings/k992_k991_qutrit_horn_separator_probe.py
target_claim: NONE-NOT-A-KILL
---

# K992 minimal qutrit horn separator

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact gap-one separator for the named Brownian and compound-Poisson phase horns
carrier: supplied qutrit with Q=diag(-1,0,1) LAYER=observed CHIRALITY=N/A
pairing: imported positive matrix trace pairing and phase expectation ON=repository_stochastic_model
real_structure: computational-basis conjugation with real symmetric phase laws
grading: charge gaps one and two
action_owner: UNTYPED -- no GU action owns the qutrit charge sector or phase law
target: pairwise microscopic-horn discriminator MAP-TYPE=evaluation
```

For K986 Brownian diffusion,

```text
psi_B(n)=-(gamma/2)n^2.
```

For the K987 symmetric `+/-theta` compound-Poisson family,

```text
psi_theta(n)=gamma[cos(n theta)-1]/sin(theta)^2.
```

The gap-two exponents agree exactly:

```text
psi_B(2)=psi_theta(2)=-2 gamma.
```

At gap one,

```text
psi_B(1)=-gamma/2,
psi_theta(1)=-gamma/(1+cos(theta)).
```

For every finite nonzero `0<theta<=pi/2`, the jump exponent is strictly more
negative. Thus the qutrit separates every named finite-angle K987 horn from
K986 without access to the microscopic record. Dimension three is minimal for
simultaneously carrying unit and double charge gaps.

This does not contradict K988: the qutrit is a declared system enlargement,
not another intervention on the original qubit. Its charge generator,
preparations and gap-one coherence readout remain imported.
