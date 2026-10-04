---
title: "K1026 spacelike interval uncertainty certificate"
status: active_research
doc_type: conditional_spacelike_interval_certificate
created: 2026-10-04
claim_ceiling: robust sufficient spacelike-separation condition for supplied event-coordinate uncertainty sets
manifest: lab/process/k1026-k1025-spacelike-interval-uncertainty-certificate.json
probe: tests/channel-swings/k1026_k1025_spacelike_interval_uncertainty_certificate_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1026 spacelike interval uncertainty certificate

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: robust spacelike-separation margin for uncertain event coordinates
carrier: pairs of Minkowski events with spatial-ball and clock-interval uncertainty LAYER=observed CHIRALITY=N/A
pairing: Euclidean spatial distance and coordinate-time separation ON=repository_quantum_control
real_structure: real event coordinates with supplied deterministic error radii
grading: exact sufficient interval theorem with sharp aligned-error boundary
action_owner: UNTYPED -- coordinates, clocks and the physical spacetime regime are not GU owned
target: causal-record audit interface MAP-TYPE=evaluation
```

For nominal spatial separation `L_nom`, spatial error radii `r_A,r_B`,
nominal time difference `Delta t_nom`, clock error radii `tau_A,tau_B`, and
signal speed bound `c`, every admitted event pair is spacelike when

```text
L_nom-r_A-r_B > c(|Delta t_nom|+tau_A+tau_B).
```

The left side is the reverse-triangle lower bound on actual distance; the
right side is the triangle upper bound on actual time separation. Their
difference is the robust margin. Collinear inward spatial errors and aligned
clock errors attain both bounds, so this uncertainty-set condition is sharp.

A positive margin certifies the whole supplied event box. Zero or negative
margin is merely inconclusive: it does not prove that influence occurred.
Nothing here supplies measured coordinates, calibrated clocks, a Minkowski
regime, or a GU locality theorem.
