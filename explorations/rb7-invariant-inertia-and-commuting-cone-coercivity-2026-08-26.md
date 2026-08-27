---
title: "RB7 invariant inertia and commuting-cone coercivity"
status: active_research
doc_type: construction_result
created: "2026-08-26"
grade: "EXACT FINITE HOMOGENEOUS CLASSIFICATION; NO FULL ACTION OR PHYSICAL VACUUM"
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
ledger_edit: none
cache: lab/process/rb7-invariant-inertia-and-commuting-cone-coercivity.json
scripts:
  - tests/channel-swings/rb7_invariant_inertia_and_commuting_cone_coercivity_probe.py
---

# RB7 invariant inertia and commuting-cone coercivity

Scope: this result binds only the incumbent three-amplitude homogeneous
truncation and the already-frozen exact mixed Gram. It does not construct or
select the full GU action, a stable vacuum, a physical fluctuation operator, a
mass, a family count, a complex flag, or a source-native particle mechanism.

```gu-typed-objects
result: M-H11 generalized-inertia and candidate-coercivity disposition
carrier: incumbent negative three-plane inside the trace-reversed metric fibre; LAYER=toy CHIRALITY=N/A
pairing: restricted DeWitt form G=-I_3 and exact mixed Gram (9/32)(I+T_tr) ON=frozen-negative-triplet-and-metric-fibre
real_structure: real homogeneous amplitude slice
grading: full-trace line versus nine-dimensional traceless fibre
action_owner: N/A; incumbent finite truncation only
target: invariant pencil inertia and commuting-kernel test MAP-TYPE=evaluation
```

## Result

M-H11 is executed at its finite homogeneous claim ceiling, with two separate
conclusions.

First, for

\[
V(r_1,r_2,r_3)=\frac{\mu}{2}\sum_i r_i^2+
\frac{\alpha}{2}\sum_{i<j}r_i^2r_j^2,
\qquad \mu=-m^2<0,\quad \alpha>0,
\]

the isotropic nonzero branch has \(r_i^2=m^2/(2\alpha)\) and Hessian

\[
H=m^2\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}.
\]

Its ordinary Hessian inertia is `(1 positive, 2 negative, 0 zero)`. On the
negative triplet the restricted DeWitt form is \(G=-I_3\), so the generalized
pencil has

\[
\operatorname{spec}(G^{-1}H)=\{-2m^2,m^2,m^2\},
\qquad \operatorname{inertia}(H,G)=(2,1,0).
\]

The probe also performs a nonorthogonal simultaneous congruence and verifies
the same characteristic pencil. The old list of plain Hessian eigenvalues was
not itself the invariant datum, but its saddle conclusion survives: both the
ordinary Hessian and the generalized pencil are indefinite. The correction is
therefore “one generalized negative direction,” not “two invariant unstable
directions.”

Second, the exact candidate Gram is

\[
K=\frac{9}{32}(I+T_{\rm tr})
=\frac{9}{16}P_{\rm traceless}.
\]

It has rank nine and kernel equal to the full-trace line. In the frozen
homogeneous slice \(D^0=C=0\), put one nonzero field component on that trace
line and set the other field components to zero. This is a nonzero commuting
configuration, while its exact candidate-Gram energy is zero. Hence

\[
\ker D^0\cap\ker C\cap\{\text{commuting}\}\cap\ker K\ne\{0\}.
\]

The proposed Gram therefore fails the necessary coercivity condition. It
cannot by itself stabilize the incumbent model or justify RB7.1. Source-owned
derivative, curvature, parent-action, or section terms would have to remove
that witness before a coercivity claim could be reopened.

## Hostile review and continuation

The strongest possible overread would treat `G=-I_3` as the full fibre or
promote the mixed Gram into an action term. Neither move is made. The metric is
only the already-selected negative three-plane, and the Gram is tested as the
named candidate rather than declared source-owned.

The exact positive controls reconstruct the stationary branch, both inertias,
the congruent pencil, Gram rank and trace kernel. Planted mutations reject the
old generalized-inertia count, a false full-rank Gram, an erased trace witness
and a false coercivity conclusion. The remaining scientific continuation is a
genuinely owned term that closes the displayed kernel intersection; repeating
this candidate or the incumbent saddle computation is not progress.

No source claim, ledger row, canon verdict, prediction, confirmation, paper,
priority or public posture moves.
