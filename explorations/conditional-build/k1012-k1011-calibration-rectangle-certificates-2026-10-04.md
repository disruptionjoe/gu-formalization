---
title: "K1012 calibration-rectangle certificates"
status: active_research
doc_type: conditional_calibration_uncertainty_theorem
created: 2026-10-04
claim_ceiling: simultaneous rectangular confidence propagation inside the imported noisy-Bell model only
manifest: lab/process/k1012-k1011-calibration-rectangle-certificates.json
probe: tests/channel-swings/k1012_k1011_calibration_rectangle_certificates_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1012 calibration-rectangle certificates

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: monotone lower and upper decisions from a simultaneous (p,V) calibration rectangle
carrier: imported common-contrast noisy-Bell parameter wedge LAYER=observed CHIRALITY=N/A
pairing: joint confidence event plus monotone phase functions ON=repository_quantum_control
real_structure: real interval bounds clipped to 0<=V<=p<=1
grading: sufficient certification exclusion or honest inconclusion
action_owner: UNTYPED -- calibration streams confidence allocation and systematic errors are unowned
target: finite-uncertainty phase classification MAP-TYPE=evaluation
```

Suppose one declared simultaneous event of confidence at least `1-alpha`
places the calibrated coordinates in

```text
p in [p_L,p_U],             V in [V_L,V_U].
```

Both K1011 statistics are coordinatewise nondecreasing on the physical wedge.
Therefore the same event gives four rigorous one-sided decisions:

```text
p_L+2V_L>1        certifies entanglement,
p_U+2V_U<=1       excludes entanglement inside the model,
p_L^2+V_L^2>1    certifies optimized-CHSH violation,
p_U^2+V_U^2<=1   excludes optimized-CHSH violation inside the model.
```

Failure of one of these sufficient tests is inconclusive, not evidence for its
opposite. The rectangle
`p in [79/100,81/100]`, `V in [31/100,33/100]` certifies entanglement and
excludes optimized CHSH throughout. The rectangle
`p in [99/100,1]`, `V in [39/100,41/100]` certifies both.

The theorem does not manufacture the simultaneous event. Shot allocation,
drift, calibration dependence and systematic coverage remain separately
owned obligations. No GU apparatus, score or protected verdict is produced.
