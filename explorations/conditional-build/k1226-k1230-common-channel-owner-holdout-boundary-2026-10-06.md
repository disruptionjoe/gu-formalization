---
title: "K1226--K1230 common-channel owner and holdout boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: INTERNAL_CONDITIONAL_MATHEMATICS
direction: observed_to_native
claim_effect: none
---

# K1226--K1230 common-channel owner and holdout boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: common-channel apparatus schema, physical frame-gauge boundary, drift witnesses and sealed Bell holdout
carrier: imported qubit preparations, effects, affine channel and Bell-pair trials LAYER=observed CHIRALITY=N/A
pairing: imported trace/Born state-effect pairing ON=repository_quantum_control
real_structure: real Bloch frames related by SO(3), with affine transfer M and translation t
grading: calibration records versus blinded holdout records
action_owner: UNTYPED -- no GU or instantiated apparatus owner for any operational primitive
target: owner-instance and cross-branch holdout boundary MAP-TYPE=evaluation
```

## Question and ceiling

K1221--K1225 identify a general qubit CPTP channel from twelve independent
linear statistics inside a declared preparation/effect frame. They do not show
that nominal state labels, effects and the fitted channel share one physical
owner, stay fixed across Bell and process trials, or close loss and locality
systematics. This packet makes that ownership demand executable and freezes a
holdout without pretending that a protocol is already data.

All quantum primitives remain imported. This work changes no source claim,
physics-ledger row, canon, paper or public posture, and it earns no GU
prediction or confirmation credit.

## K1226: common-owner flight card

One owner instance must bind both branches with the same
`channel_device_id`, channel-configuration hash, basis-map identifier,
calibration epoch and clock epoch.

The calibration branch interleaves the six preparations `+/-X`, `+/-Y`,
`+/-Z` with the three signed effects `X,Y,Z`. The Bell branch prepares a named
`Phi+` source, applies that same channel module to the first arm before analyzer
choice, and records both settings, outcomes, times, heralds and inclusion bits.
The trial schedule is sealed and randomized across branches. The holdout
settings, count budget, inclusion rule and decision threshold are blinded
before the calibration fit.

An instance additionally needs immutable raw events, independent preparation
and measurement calibration or a self-consistent gate-set account, basis
registration, drift/memory bounds, source-fidelity evidence, loss and detector
models, timing and setting-leakage controls, and a systematic error budget.
A written flight card supplies none of those measurements.

## K1227: the physical SPAM-frame gauge

For a signed effect direction `e`, input Bloch vector `r`, and affine channel,
`y=e^T(Mr+t)`. Every physical rotation `R in SO(3)` gives another coordinate
description

```text
r'=Rr,   e'=Re,   M'=R M R^T,   t'=Rt
```

with exactly the same probabilities `e'^T(M'r'+t')=e^T(Mr+t)`.

The exact rational control rotates the `gamma=3/4`, `p=2/3` generalized-
amplitude-damping channel through a rational `3-4-5` rotation mixing `x` and
`z`. Both descriptions are CPTP and all eighteen axial probability
coordinates agree, while both `M` and `t` coordinates change. Thus even the
twelve-statistic optimum in K1224 does not authenticate the physical basis or
SPAM owner. Optimized CHSH is invariant under this common rotation, but an
apparatus-level claim still requires the basis and owner records.

## K1228: stability, drift, loss and locality witnesses

In each randomized block define

```text
h_ij=[y_i(+e_j)+y_i(-e_j)]/2=t_i,
d_ij=[y_i(+e_j)-y_i(-e_j)]/2=M_ij.
```

The six within-block residuals `h_ij-h_i0`, for three output components and
two extra input axes, test preparation-conditioned inconsistency. Cross-block
differences of `h` and `d` expose changes in the fitted `t` and `M`. An exact
control plants one `1/100` transfer drift and one `-1/200` translation drift;
both are recovered while every within-block relation remains zero. This also
shows why within-block consistency alone does not prove stability.

For the ideal one-arm-channel Bell model, the remote marginal is `1/2` for
every local setting. But postselected coincidences do not self-validate
locality. The flight card therefore requires raw attempt counts and a sealed
inclusion rule before scoring either no-signalling or the holdout.

## K1229: sealed off-frame Bell holdout

Fit `M,t` only from the six axial preparations and three Pauli effects. Seal
the off-axis analyzer pair `a=(3/5,0,4/5)`, `b=(0,4/5,3/5)` before unblinding
Bell coincidences. Under the declared `Phi+`/Born model,

```text
p(x,y|a,b)=[1+x a.t+xy a^T M diag(1,-1,1)b]/4.
```

For K1223's rational affine control, `a.t=3/13` and the correlation is
`99/1625`, giving, in outcome order `(--),(-+),(+-),(++)`,

```text
1349/6500, 1151/6500, 1901/6500, 2099/6500.
```

Before unseal, freeze `alpha`, `N_holdout`, `epsilon_systematic`, the event
inclusion rule and schedule digest. With empirical frequencies `f_xy`, score

```text
max_xy |f_xy-p_xy|
  <= sqrt(log(8/alpha)/(2 N_holdout)) + epsilon_systematic.
```

The statistical term is the four-outcome union of Hoeffding bounds. No
holdout refit is allowed. Passing validates this common-owner model only;
failing rejects the instantiated composition or its error budget. Neither
outcome is a GU result.

## K1230: integrated boundary

The protocol schema, at least one exact physical SPAM gauge, observable drift
checks and a quantitative holdout preregistration now exist. An instantiated
physical owner does not. The next input is one completed K1226 flight card with
hardware identities, immutable randomized schedule, calibrated SPAM or a
self-consistent gate set, raw calibration and Bell events, drift/loss/locality
bounds, count budget and systematic-error ceiling. Only then may K1229 be
unsealed and scored without refitting.

Delayed-choice entanglement swapping remains a distinct reserved, unscored
family. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains `UNCERTAIN`; and
LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`.

## Reproduction and hostile controls

Five producers pass `58/58` declared controls. Five probes reject `48/48`
hostile mutations. The checks cover the owner-schema/instance distinction,
eighteen exact probability equalities under the physical frame gauge, two
planted drift coordinates, the normalized four-outcome holdout table, the
no-refit rule and every protected-status firewall.
