---
title: "K991 K990 charge harmonic channel theorem"
status: active_research
doc_type: conditional_phase_channel_result
created: 2026-10-04
claim_ceiling: exact finite-charge random-phase channel theorem only
manifest: lab/process/k991-k990-charge-harmonic-channel-theorem.json
probe: tests/channel-swings/k991_k990_charge_harmonic_channel_theorem_probe.py
target_claim: NONE-NOT-A-KILL
---

# K991 charge-harmonic channel theorem

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact diagonalization of a supplied random-phase channel by charge-basis matrix units
carrier: finite complex Hilbert space with supplied integer charge operator Q LAYER=observed CHIRALITY=N/A
pairing: imported positive trace pairing and classical expectation ON=repository_stochastic_model
real_structure: computational-basis conjugation with real phase variable
grading: charge difference q_j-q_k on each matrix unit E_jk
action_owner: UNTYPED -- no GU action owns Q or the phase process
target: finite-charge harmonic observability of the K956 phase family MAP-TYPE=evaluation
```

Let `Q|j>=q_j|j>` and `U_x=exp(-ixQ)`. Direct conjugation gives

```text
U_x E_jk U_x* = exp[-ix(q_j-q_k)] E_jk.
```

Therefore an arbitrary phase law acts by

```text
E_jk -> phi_t(q_j-q_k) E_jk,
phi_t(n)=E exp(-inX_t).
```

For stationary independent increments, `phi_t(n)=exp[t psi(n)]`. Observable
harmonics are exactly the charge differences. The original K956 qubit has
charges `-1,+1`, so it samples only the nonzero harmonic `n=2`; it does not
determine `psi(1)` or the rest of the characteristic exponent. The supplied
three-charge spectrum `-1,0,1` samples `n=1` and `n=2` simultaneously.

This is a carrier-neutral structural theorem. The finite charge spectrum,
positive state/effect pairing, phase law and characteristic exponent remain
imported, and no GU physical quotient or action is constructed.
