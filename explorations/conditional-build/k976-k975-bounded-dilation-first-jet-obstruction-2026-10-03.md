---
title: "K976 K975 bounded-dilation first-jet obstruction"
status: active_research
doc_type: conditional_bounded_dilation_first_jet_result
created: 2026-10-03
claim_ceiling: exact first-jet no-go under four declared bounded product-dilation hypotheses only
manifest: lab/process/k976-k975-bounded-dilation-first-jet-obstruction.json
probe: tests/channel-swings/k976_k975_bounded_dilation_first_jet_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K976 bounded-dilation first-jet obstruction

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: bounded autonomous product-state Hamiltonian dilations have Hamiltonian-only reduced first jets
carrier: finite system Hilbert space tensor a fixed environment Hilbert space LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert adjoint, fixed environment state and partial trace ON=repository_bounded_dilation
real_structure: complex conjugation in chosen Hilbert bases
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction, not Weinstein source or GU action
target: microscopic owner of the K956 dissipative dephasing generator MAP-TYPE=evaluation
```

Let

```text
Phi_t(rho)=Tr_E(e^{-itH}(rho tensor sigma_E)e^{itH})
```

with a fixed normalized environment state and bounded time-independent
self-adjoint `H`. Expanding at zero and tracing the environment gives

```text
Phi'_0(rho)=-i[H_eff,rho],
H_eff=Tr_E(H(I tensor sigma_E)).
```

Thus the reduced first jet is a derivation. K956's positive-rate generator
`L(rho)=gamma(Z rho Z-rho)` is not. An exact two-dimensional witness avoids
any representation choice: `L` vanishes on both computational-basis
projectors, so a commutator representing it would need a diagonal effective
Hamiltonian; on `|+><+|`, that commutator has purely imaginary antisymmetric
off-diagonal entries, whereas `L(|+><+|)` has real symmetric entries `-gamma`.

The theorem closes only the joint bounded/product/fixed/autonomous/
differentiable horn. It does not exclude unbounded generators and their domain
limits, correlated or input-dependent assignments, fresh ancillas, resets,
time-dependent driving, non-Hamiltonian primitives or nondifferentiable
singular limits. No GU physical quotient or action has been constructed.
