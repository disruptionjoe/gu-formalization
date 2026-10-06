---
title: "K1221--K1225 affine qubit-channel process-frame boundary"
status: active_research
doc_type: conditional_research_result
created: "2026-10-06"
classification: INTERNAL_CONDITIONAL_MATHEMATICS
direction: observed_to_native
claim_effect: none
---

# K1221--K1225 affine qubit-channel process-frame boundary

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
result: all-qubit-CPTP Bell/CHSH and affine-process-frame identifiability boundary
carrier: imported affine qubit channel and Bell-Choi output LAYER=observed CHIRALITY=N/A
pairing: imported trace/Born state-effect pairing ON=repository_quantum_control
real_structure: real 3x3 Bloch-transfer matrix plus real 3-vector translation
grading: two-body Bell correlations versus one-body marginals and full process data
action_owner: UNTYPED -- no GU owner for the channel, state, pairing, frames or apparatus
target: cross-anchor calibration and process-frame demand MAP-TYPE=evaluation
```

## Question and ceiling

K1216--K1220 proved the Bell/optimized-CHSH calibration boundary for unital
qubit channels. This packet asks whether unitality is actually load-bearing,
where a nonunital affine translation appears in the Bell output, and which
linearly independent process-frame statistics identify the full channel.

Everything remains an imported finite-dimensional control. The CPTP channel,
Bell preparation, trace/Born pairing, input/output frames, locality, apparatus
and systematics are not supplied by GU. No calibration anchor earns prediction
or confirmation credit, and delayed-choice entanglement swapping remains the
reserved unscored holdout.

## K1221: affine translation decouples from Bell correlations

Write any trace-preserving qubit channel in Bloch form

```text
r_out = M r_in + t,
```

where `M` is real `3x3` and `t` is real. The Bell state `Phi+` has vanishing
local Bloch vectors and correlation matrix `D=diag(1,-1,1)`. Applying the
channel to its first subsystem gives

```text
rho_out = 1/4 [I tensor I + (t dot sigma) tensor I
               + sum_ij (M D)_ij sigma_i tensor sigma_j].
```

Thus the first local Bloch vector is `t`, the second is zero, and the two-body
correlation tensor is still

```text
T = M D,          T T^T = M M^T.
```

The optimized CHSH score therefore remains

```text
S_max = 2 sqrt(s_1^2+s_2^2)
```

for the two largest singular values of `M`, independently of `t`. Unitality
was not a necessary hypothesis for K1216's correlation identity.

The sharp one-direction interval also remains `2|V| <= S_max <= 2sqrt(2)`.
Trace-distance contraction gives `||M||<=1` for every CPTP channel, and the
unital endpoint channels from K1217 remain members of the larger class.

## K1222: translation-blind physical controls

Generalized amplitude damping has

```text
M = diag(sqrt(1-gamma), sqrt(1-gamma), 1-gamma),
t_z = gamma (2p-1).
```

At `gamma=3/4`, the three channels `p=0,1/2,1` are CPTP, share
`M=diag(1/2,1/2,1/4)`, and have translations `-3/4,0,3/4`. They therefore
share the complete Bell correlation tensor and

```text
S_max^2/4 = 1/2,
```

while their first output marginals differ. Bell correlations identify no
affine translation even inside one standard physical channel family.

## K1223: a sufficient affine process frame

Prepare the six axial input states with Bloch vectors `+e_j` and `-e_j`, and
measure all three signed output Pauli components. The eighteen raw readouts are

```text
y_i(+e_j) = t_i + M_ij,
y_i(-e_j) = t_i - M_ij.
```

Therefore

```text
M_ij = [y_i(+e_j)-y_i(-e_j)]/2,
t_i  = [y_i(+e_j)+y_i(-e_j)]/2.
```

The nine antisymmetric half-differences determine `M`, hence the Bell score.
Any one input-axis pair supplies the three translations. The other two copies
are consistency checks, so the eighteen raw values reduce to twelve
independent statistics with six affine consistency relations.

The exact control composes `gamma=3/4` amplitude damping with rational input
and output rotations. It has

```text
M = [[3/10, -2/5,    0],
     [2/13,  3/26, -3/13],
     [24/65, 18/65, 5/52]],
t = [0, -9/13, 15/52],
```

and all three paired preparations reconstruct the same translation exactly.

## K1224: the linear-identifiability floor

Trace-preserving Hermiticity-preserving qubit maps form a real affine
parameter space of dimension twelve: nine entries of `M` and three of `t`.
Its CPTP subset has relative interior because the completely depolarizing
channel has a positive-definite Choi matrix. Any linear measurement map of
rank below twelve has a nonzero kernel direction. Sufficiently small positive
and negative perturbations of the depolarizing Choi matrix along that direction
remain CPTP and return identical measured statistics. Fewer than twelve
independent linear statistics cannot identify the full affine channel.

The unital transfer subspace has dimension nine and the same interior argument
shows that fewer than nine independent linear statistics cannot identify its
full `M`. K1223's twelve-statistic frame and its nine centered transfers meet
these dimension floors. This is not a claim that every nonlinear scalar
invariant requires full tomography; optimized CHSH needs only the two leading
singular values once those data are independently owned.

## K1225: all-CPTP calibration boundary

Inside the frozen qubit-CPTP/Bell-Choi/Born class:

- affine translation affects a local marginal but not Bell correlations or
  optimized CHSH;
- one directional read retains the sharp interval
  `2|V| <= S_max <= 2sqrt(2)`;
- three same-axis reads remain insufficient;
- nine centered transfer statistics determine `M` and the imported Bell score;
- three additional marginal statistics determine `t`; and
- twelve independent linear statistics identify the full affine process and
  meet the dimension lower bound.

K1211--K1215 remains the Pauli/principal-axis subcase. K1216--K1220 remains
exact with its unitality assumption now known to be unnecessary for the
Bell-correlation theorem. K1004 remains a dephasing-horn theorem and K1009 a
distinct common-contrast model.

The next physical input is not another channel-class generalization. It is a
typed common owner for the CPTP channel, Bell preparation, paired process
frame, Born state/effect pairing, locality, apparatus and systematics, followed
by a predeclared holdout. Do not consume delayed-choice entanglement swapping
before that ownership packet exists.

No source, ledger, canon, paper, public posture, prediction, confirmation or
protected verdict moves. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53 remains
`UNCERTAIN`; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain `NEEDS`.

## Reproduction and hostile controls

Five producers pass `54/54` declared controls. Five probes reject `46/46`
hostile mutations. The checks cover the affine Choi decomposition, a physical
translation-blind family, exact paired-frame reconstruction, the two dimension
floors, the ownership firewall and the held-out-family boundary.
