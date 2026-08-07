---
title: "Eric/Curt Wave 2b: first-layer term quotient and ablation"
status: construction_result
doc_type: exploration
created: 2026-07-31
run: lab/process/runs/GUH-20260731T184714Z-curt-77-wave2b-term-rank/run-plan.md
source_note: lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md
registry: lab/process/eric-curt-wave2b-term-rank-ablation.json
probe: tests/channel-swings/eric_curt_wave2b_term_rank_ablation_probe.py
grade: "EXACT for the frozen first-layer free-jet quotient, coefficient dimensions, support-ablation rank, and signature arithmetic. RECONSTRUCTION for the source-preferred dual-horizontal `(7,7)` completion. No ported `(7,7)` action or physical recovery."
---

# Wave 2b first-layer term rank and ablation

## Result first

Curt's transcript makes the vertical-sign comparator the scientifically
relevant `(7,7)` branch: he explicitly decomposes the symmetric fibre into
trace/traceless pieces and chooses the trace-line sign giving vertical
`(4,6)`. The transcript then invokes representation theory—especially the
split `Spin(7,7)` spinor carrier—as the reason for following that branch.

It does **not** type the last sign conversion. Spoken vertical `(4,6)` plus
spoken horizontal `(1,3)` gives `(5,9)` under one ordered convention. The
minimal consistent reconstruction is that the dual-horizontal contribution
enters as `(3,1)`, giving

\[
(4,6)+(3,1)=(7,7).
\]

Therefore `R77_VERTICAL_FLIP` is now the source-preferred completion;
`R77_BASE_FLIP` remains only a hostile comparator. The source convention is
still open, so no lane or carrier is selected.

On that corrected branch ordering, the frozen G2 first-layer action class has
exact quotient rank **four**:

\[
\begin{aligned}
M_1&=\int T\wedge\mathscr S_r(F_B),\\
M_2&=\int T\wedge\mathscr S_r(D_BT),\\
M_3&=\int T\wedge\mathscr S_r(q(T,T)),\\
M_4&=\int T\wedge\flat_r(T).
\end{aligned}
\]

The written source/G2 action is the two-parameter raw slice

\[
\lambda\left(1,\frac12,\frac13,\frac{\kappa_1}{2}\right)
\]

inside this four-dimensional coefficient space. Modulo overall nonzero scale,
it is one-dimensional, parameterized by `kappa_1`.

## Why the term list is complete in the frozen class

The frozen class contains the existing G2 graph fields `A,epsilon,g` with

\[
B=A_{\rm LC}(\epsilon,g),\qquad T=A-B,
\]

one density-dual contraction `S_r` or `flat_r`, at most one covariant
derivative, and at most the written cubic distortion order. Gauge covariance
forbids a naked connection. Degree fourteen forces the outer homogeneous
one-form to be `T`; the input of `S_r` must be an adjoint-valued two-form.
The available two-form jets are

\[
F_B,\qquad D_BT,\qquad q(T,T).
\]

Writing the same geometry relative to `A` adds no generators:

\[
F_A=F_B+D_BT+q(T,T),
\]

\[
D_AT=D_BT+2q(T,T).
\]

The six obvious `A/B`-written candidates therefore have two independent
relations and quotient rank `6-2=4`.

This is not a claim about every local action imaginable. The following are
deliberately owned downstream:

- observation and equation-dual terms — Wave 3;
- odd kinetic, zero-order, and current terms — Wave 4;
- curvature/residual squares — Wave 5;
- Higgs extraction, stationary potentials, and physical modes — Waves 6--10.

## Carrier result

The formula rank is four on every branch, but operator existence is not.

| branch | verdict |
|---|---|
| active real `(9,5)` | all four G2/G3 realizations already exist at their current conditional grade |
| source-preferred real `(7,7)` | same four schemas; Hodge, Clifford, Krein/reality, Shiab, pseudo-musical, adjoints, and domain remain unported |
| base-flip `(7,7)` | hostile arithmetic comparator, not transcript-preferred |
| common complexification | four complex schemas but no real action, adjoint, or physical domain |

Thus term-rank equality does not repair the carrier fork.

## Exact ablation

Within the frozen class, the four terms carry four independent structural
jobs:

| term removed | exact lost support | what this still does not prove |
|---|---|---|
| `M1` | curvature seed | Einstein or Yang--Mills recovery |
| `M2` | first-jet distortion response | physical hyperbolicity/propagation |
| `M3` | nonabelian distortion self-interaction | selected gauge group or Higgs potential |
| `M4` | algebraic displacement contrast | VEV, dark-energy stress, or scale |

The incidence matrix is the `4x4` identity and has rank four. Every term is
necessary for the four-job first-layer packet, but this is **not positive
constraint surplus**. Four independent directions carrying four independent
presence obligations gives support-grade surplus zero. Moreover, presence is
an inequality (`coefficient != 0`), not a numerical equation.

It would be invalid to compute `4-2=2` from the four support rows and the
two-dimensional source coefficient slice. The source ratios are architectural
input; the four ablation rows do not independently measure or determine them.

Physical constraint surplus remains unavailable until Wave 3 supplies the
observation/equation-dual/domain map and later waves supply the odd and
second-layer actions. That is a typed scope boundary, not a return to “no
source action.”

## Physics-family handoff

- Gravity and gauge geometry have first-layer parent support, but no observed
  equation is recovered.
- Odd current and matter are absent by frozen-field policy and remain Wave 4.
- Higgs/Yukawa remains the `varpi/T` fork in Wave 6.
- The displacement term can host a later cosmological candidate, but contains
  no stress tensor, stationary state, sign, or scale by itself.
- P1/P2/P3 remain unconsumed.

## Wave 2 exit and next swing

Wave 2 now exits for the **frozen G2 first-layer class**: primitive ownership,
term quotient, coefficient dimensions, and support ablation are all explicit.
This releases Wave 3:

`ECW3-G4-OBSERVATION` must construct `L,R,L^vee,L^!,sharp_Y,sharp_X`, global
descent, nonlinear leakage, a closed Krein domain, quotient, and preboundary
reduction. It should work on the active branch while carrying the precise
`(7,7)` port ledger, not pretending those operators have transferred.

## Nonclaims

No source sign convention is fully recovered, no `(7,7)` action is ported, no
carrier or coefficient is selected, and no Einstein, Yang--Mills, Higgs,
matter, quantum, generation, or cosmological result is claimed.
