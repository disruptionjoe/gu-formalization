---
title: "K1024 adversarial trial-record correction"
status: active_research
doc_type: conditional_record_integrity_certificate
created: 2026-10-04
claim_ceiling: memory-robust CHSH certificate under a supplied deterministic record-error budget
manifest: lab/process/k1024-k1023-record-corruption-certificate.json
probe: tests/channel-swings/k1024_k1023_record_corruption_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1024 adversarial trial-record correction

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: deterministic record-integrity correction to the sequential CHSH certificate
carrier: true and recorded binary win sequences on event-ready trials LAYER=observed CHIRALITY=N/A
pairing: Hamming distance between true and recorded win strings ON=repository_quantum_control
real_structure: bounded real adapted process plus deterministic error budget
grading: exact pathwise inequality and finite-shot consequence
action_owner: UNTYPED -- record production and its audit are not GU owned
target: complete statistical and systematic score boundary MAP-TYPE=evaluation
```

Let `W_i` be the true all-trials CHSH win indicator and `W_tilde_i` its
recorded value. If an audit supplies the deterministic bound

```text
sum_i |W_tilde_i-W_i| <= R,
```

then pathwise `sum_i W_tilde_i <= sum_i W_i+R`. For any predictable local
ceilings `b_i`, arbitrary inter-trial memory therefore obeys the certificate

```text
w_hat_recorded > average_i(b_i) + R/n
                 + sqrt(log(1/alpha)/(2n)).
```

Combining K1021 yields

```text
w_hat_recorded > 3/4 + average_i(epsilon_i) + R/n
                 + sqrt(log(1/alpha)/(2n)).
```

The `R/n` term is sharp without more structure: an adversary can flip `R`
losing records into wins. This result does not supply the audit, exclude
unrecorded trials, or prove that a physical data path meets the bound.
