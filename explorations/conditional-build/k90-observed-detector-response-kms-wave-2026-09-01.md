---
title: "K90 observed detector-response KMS wave"
status: active_research
doc_type: reverse_scaffold_detector_response_ownership_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact repository-owned finite leading-response weights for one stationary bosonic mode and two-level detector, positive-frequency vacuum orientation, occupation-one KMS detailed-balance ratio and independent covariance/switching/interaction/Born owner accounting; no source-selected covariance or detector interaction, continuum Hadamard state, derived Born rule, complete positive instrument, nonperturbative unitary detector dynamics, Bell prediction, confirmation, or verdict
manifest: lab/process/k90-observed-detector-response-kms-wave.json
probe: tests/channel-swings/k90_observed_detector_response_kms_probe.py
---

# K90 observed detector-response KMS wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: exact finite positive-frequency and KMS detector-response ownership control above the K89 quasifree availability result
carrier: one repository-selected stationary bosonic mode tensor one two-level detector LAYER=observed CHIRALITY=N/A
pairing: leading quadratic transition weight from the supplied mode covariance, switching profile and monopole interaction ON=repository_owned_finite_response_control
real_structure: complex mode amplitudes with conjugate transition weights
grading: detector ground/excited energy grading and bosonic occupation number
action_owner: repository-construction
target: stationary covariance and detector interaction data to excitation/deexcitation response weights MAP-TYPE=evaluation
```

## Result first

K89 supplied one positive quasifree characteristic functional but no detector
dynamics or Born response. To separate those owners, take one stationary mode
and a two-level detector with matching positive gap. Couple them through a
repository-selected linear monopole interaction at four equally weighted
quarter-turn times. With coupling `g=1/8`, the resonant phase sum is four and
the counterrotating phase sum is zero:

```text
|sum_(t=0)^3 1|^2       = 16,
|sum_(t=0)^3 (-1)^t|^2 = 0.                              (1)
```

At leading quadratic order, a mode with occupation `n` therefore gives

```text
R_up(n)   = g^2 n 16,
R_down(n) = g^2 (n+1) 16.                               (2)
```

For the vacuum, `(R_up,R_down)=(0,1/4)`: the selected positive-frequency
orientation suppresses excitation while allowing deexcitation. At `n=1`,

```text
(R_up,R_down)=(1/4,1/2),
R_up/R_down=1/2=n/(n+1)=exp(-beta omega)                 (3)
```

for the named thermal parameter `exp(beta omega)=2`. Reversing spectral
orientation swaps the vacuum roles; deleting one switching endpoint makes the
counterrotating sum nonzero; changing occupation changes the detailed-balance
ratio; and setting `g=1` produces a leading response weight larger than one.

## Ownership result

Equations (1)--(3) do not derive a detector law from a covariance alone. They
require four separately supplied objects:

1. the stationary mode covariance and positive-frequency orientation;
2. the four-time switching profile;
3. the monopole interaction and its coupling; and
4. the interpretation of the response weight as a probability.

The first three are repository selections in this packet. The fourth is an
imported Born interpretation. Altering any one changes the result while the
others remain fixed. KMS detailed balance therefore constrains a supplied
state/interaction package; it does not select that package or derive the
measurement postulate.

## Hostile review and boundary

The strongest overclaim would call the finite response table a source-selected
Hadamard/Born detector theory. The strongest contrary constructions are the
orientation reversal, switching-endpoint loss, occupation mutation and large-
coupling control. The weakest seam is the source-owned covariance, local
interaction, switching/record map and complete positive instrument on the same
functional causal domain as the Green pair.

The exact probe passes `24/24`; its hostile selftest catches `21/21` spectral,
switching, thermal, coupling, owner and promotion mutations. No source
covariance or interaction, continuum Hadamard condition, derived Born rule,
nonperturbative detector unitary, Bell prediction, confirmation, canon or
public posture moves.

## Next condition

Construct the source physical covariance and detector coupling on the same
common BFV/Green domain. Prove microlocal admissibility, local switching and a
complete positive record instrument, then determine whether the Born
probability rule and KMS response are derived, uniquely selected or still
imported.
