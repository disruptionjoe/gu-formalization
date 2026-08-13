---
title: "Eric/Curt Wave 3D-B2C15M: moving Shiab, weighted Euler, and a polynomial rank chart"
status: active_research
doc_type: construction_result
created: 2026-08-01
branch: agent/null-clifford-omega1-repair
run: historical-investigation
registry: lab/process/eric-curt-wave3d-b2c15m-moving-shiab-exact-g2-weighted-euler.json
probe: tests/channel-swings/eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py
grade: "B2C15M PARTIAL CONSTRUCTION PASS. The native trace-adapted Shiab now has an exact vertical-Spin-frame covariance certificate in all 91 stabilizer directions plus representative quotient-tangent checks, and a complete local symmetric-Clifford-gauge metric derivative on all ten physical metric owners; the metric response map has rank 10. Moving formal-adjoint/Green, nonzero six-slot-DM, residual-zero, and separately live off-shell correction controls pass. Three distinct Douglis--Nirenberg order-cap skeletons are frozen for the compressed source square, exact variational square, and first-action owner system. On the complete positive-plus-trace conormal chart xi(a)=e0+a t, every frozen coefficient is reconstructed quadratically and held-out checked; gcds of all maximal minors prove rank 8165 for a^2 != 1 and 6097 at the two null roots. The full first-action owner Euler coefficients, moving-family polynomial rank atlas, other trace-stabilizer charts, coefficientwise right-H/Krein/reality certificate, BV quotient, and domain remain open."
canon_verdict_change: none
---

# B2C15M moving Shiab, weighted Euler, and polynomial rank chart

## Result first

This swing closes two genuine gaps and sharply narrows a third.

First, “moving Shiab” is no longer one unnamed correction. Vertical Spin-frame
motion obeys the differentiated naturality identity in every one of the 91
stabilizer directions. Actual quotient motion is checked separately on seven
grade-generating tangent representatives against all six curvature grades;
this is representative evidence, not an 8,165-direction enumeration or a
global overlap theorem. Metric motion is constructed separately from the ten actual
`D_g G_Y` owners. In a declared symmetric Clifford gauge, every owner
differentiates the Clifford relation, preserves the Hodge-square sign, and
returns the trace gamma, both `Phi` tensors, four Hodge occurrences, and the
single density contribution. The resulting exact metric-response map has
rank `10`.

Second, the named B2C15R conormal census has become an honest polynomial
theorem on one complete trace-stabilizer chart. For

\[
\xi(a)=e_0+a t,\qquad q(\xi)=1-a^2,
\]

the frozen fixed-Shiab coefficient has rank

\[
\operatorname{rank}K_{\rm fix}(\xi(a))=
\begin{cases}
8165,&a^2\ne1,\\
6097,&a=\pm1.
\end{cases}
\]

This is certified by every maximal minor in every independent support block,
not by one selected determinant or finitely many ranks.

Third, the correct order of the remaining action problem is now fixed. The
compressed source square, exact variational square, and full first-action
owner Euler system have separate Douglis--Nirenberg ledgers. The moving
geometric coefficients are algebraic in the owner variation and therefore do
not raise the already-earned top graph weights. But this gate does **not**
pretend that an order table is the missing full owner Euler coefficient. That
coefficient is the next construction.

## Plain English

The prior swing found that the connection itself did not contain a missing
derivative term. That left a concern: perhaps the Shiab contraction changes
when the metric and reduction change, and those changes could alter the main
field equation.

They do change it. We can now write those changes term by term. Moving the
reduction produces exactly the covariance response it should; moving the ten
metric components gives ten independent responses. None introduces a higher
derivative than the connection graph already carried, so the leading-order
equation found in the previous swings survives.

We also replaced “the rank seems to drop on a null example” with a real
polynomial statement on one full family of covectors. Away from two exactly
identified null values, every mode survives. At those values, exactly 2,068
directions drop. Other null families still need their own chart; this result
does not collapse them together.

## Layer 0: five different equations

The word “Euler” was hiding five objects:

| object | meaning | status here |
| --- | --- | --- |
| `Upsilon_B_src` | compressed 2021 source residual | retained separately |
| `E_T_var` | exact partial-`T` Euler covector of the selected G2 first action | retained separately |
| `Euler(I2_src)` | Euler operator of the source residual square | weighted ledger frozen |
| `Euler(I2_var)` | Euler operator of the exact variational residual square | weighted ledger frozen |
| `Euler_owner(I1_G2)` | full owner tuple after `B=A_LC(epsilon,g)`, `T=A-B` | order ledger frozen; coefficients still open |

The last object cannot be read off from `DE_T_var`. Direct-`B` terms and the
`T=A-B` chain can cancel. B2C15M therefore does not call its weighted skeleton
a completed owner equation.

Likewise, these moving objects remain separate:

- `D Shiab[delta epsilon,delta g] F` and `Shiab(D F)`;
- `D(L^!)` and `(DL)^!`;
- the six-slot `DM` and `(D Shiab)q`;
- `DR_res` and every Shiab slot;
- the native LC branch and the A0 lower-filtered comparator.

## Differentiated naturality

For vertical Spin-frame motion the efficient identity is

\[
D\mathscr S[\chi]F
=\operatorname{ad}_\chi^*\mathscr S(F)
-\mathscr S(\operatorname{ad}_\chi F).
\]

The probe constructs the moving trace and `Phi` terms independently and then
checks

\[
D\mathscr S[\chi]F+\mathscr S([F,\chi])
=[\mathscr S(F),\chi]
\]

for all `91 x 6 = 546` direction/grade pairs. Of those, `492` have a live
moving-family response. The full-adjoint projection and invariant internal
lowerer commute with these Spin actions, so their derivatives are proved zero
in this co-moving trivialization rather than silently frozen.

This establishes vertical-lift compatibility. A separate `7 x 6 = 42`
representative check establishes the same infinitesimal identity on
grade-generating quotient tangents, with `34` live responses. It does not
enumerate the full quotient, prove global overlap descent, identify quotient
motion with a gauge differential, or supply a BV complex.

## Ten-owner metric derivative

The trace-adapted family is

\[
\mathscr S(F)=\pi_{\mathfrak{sp}},c(t_{\rm tr})
\left(\Phi_1\wedge *F-
\frac12*\left[\Phi_1\wedge*(\Phi_2\wedge *F)\right]\right).
\]

The declared symmetric Clifford gauge uses

\[
D\gamma_a=\frac12h_{ac}g^{cb}\gamma_b,
\]

which is verified directly through

\[
\{D\gamma_a,\gamma_b\}+\{\gamma_a,D\gamma_b\}=2h_{ab}
\]

for every generator pair and every physical metric owner.

The normalized DeWitt trace vector also moves with the metric. Its derivative
is constructed from the inverse DeWitt frame and checked to preserve the
trace-vector norm. Since
`Phi2_ab = gamma_a gamma_b - g_ab`, its derivative includes the scalar
correction `-h_ab`; an exact regression asserts that every resulting
`D Phi2_ab` is a pure Clifford bivector with no scalar contamination.

The Hodge derivative is

\[
(D_h*)\alpha=*
\left(\frac12\operatorname{tr}(g^{-1}h)\alpha
-h^\sharp\!\cdot\alpha\right).
\]

The first term is the volume/density response; it is counted once inside the
Hodge map. The implementation separately returns:

1. trace-gamma motion;
2. `D Phi1` in the first term;
3. the first Hodge variation;
4. `D Phi1` in the nested term;
5. `D Phi2`;
6. inner Hodge variation;
7. middle Hodge variation;
8. outer Hodge variation.

All ten owner responses are nonzero on the multi-grade plant and their joint
response matrix has rank `10`. Several individual slots legitimately vanish
for some owners; the complete sum does not.

This is a repository construction in a declared Clifford trivialization. The
source does not supply this gauge or its derivatives.

## Formal adjoint, DM, and the Hessian boundary

An exact variable-density Green fixture proves

\[
D(L^!)\ne(DL)^!
\]

when the input/output lowerers and density move. The full one-parameter family
and its moving endpoint satisfy the differentiated Green identity, with a
nonzero endpoint derivative. This prevents the common shortcut of
differentiating only the displayed differential operator.

The `DM` code differentiates all six permutations of the cubic trilinear
form. A deterministic exact witness has owner `0` and grades `(2,2,2)`, with
`DM=-sqrt(2)/4`; the tempting compact `(D Shiab)q` slot gives instead
`-3sqrt(2)/8`. Thus the moving trilinear term is live and cannot be replaced
by one displayed slot. This is still a witness, not a complete all-grade
coefficient theorem.

For either residual square

\[
I_2=\frac12\langle E,R_{\rm res}E\rangle,
\]

the exact finite nonlinear fixture establishes:

- at a nontrivial residual-zero point, with nonlinear and moving-`R` data
  still live, the Hessian is exactly `J^T R J`;
- off shell, the residual-times-second-variation and moving-primalizer
  corrections are separately live and each has exact rank two; their sum is
  the rank-two difference between the full Hessian and `J^T R J`.

Therefore B2C15R's Gram is a genuine residual-zero normal comparator, not the
full off-shell Hessian.

## Three weighted order-cap ledgers

With owners ordered `(A, epsilon, g)`, the frozen tables are:

```text
source residual square
  row weights    (1,1,1)
  column weights (1,1,1)
  order caps     [[2,2,2],[2,2,2],[2,2,2]]

exact variational residual square
  row weights    (1,2,2)
  column weights (1,2,2)
  order caps     [[2,3,3],[3,4,4],[3,4,4]]

first G2 action owner system
  row weights    (0,1,1)
  column weights (1,2,2)
  order caps     [[1,2,2],[2,3,3],[2,3,3]]
```

Each cap equals its row plus column weight. These are preregistered
Douglis--Nirenberg skeletons, not realized principal orders: nonzero owner
coefficients and direct-`B`/`T` cancellations remain unaudited. The active
first-action coefficient matrix still must be
assembled from the direct-`B`, `T=A-B`, moving-Shiab, moving-pairing, and
metric-density chains.

## Polynomial chart theorem

Every `K_fix(xi(a))` entry is degree at most two because one `xi` enters the
curvature wedge and another enters the graph pairing. Values at
`a=-1,0,1` reconstruct every coefficient exactly; `a=2` is held out and
passes across the complete matrix.

The support graph splits into components with at most two owner columns. The
gcd of **all** maximal minors in every two-column block is

\[
(a-1)(a+1),
\]

while every remaining one-column block has gcd `1`.

| grade | generic rank | two-column blocks | rank at `a=+/-1` |
| ---: | ---: | ---: | ---: |
| 3 | 364 | 66 | 298 |
| 6 | 3003 | 792 | 2211 |
| 7 | 3432 | 924 | 2508 |
| 10 | 1001 | 220 | 781 |
| 11 | 364 | 66 | 298 |
| 14 | 1 | 0 | 1 |
| **total** | **8165** | **2068** | **6097** |

Thus the exceptional polynomial is exactly the chart norm
`q(xi)=1-a^2`, up to sign.

This theorem covers the positive trace-stabilizer chart only. It does not
cover:

- pure trace;
- negative trace-orthogonal norm;
- orthogonal nonzero null;
- nonzero-null-plus-trace degeneracies.

In particular, `(q,trace)` still cannot distinguish pure trace from a
nonzero-null perpendicular component with the same pair of values.

## Source disposition

- `SOURCE-CONFIRMS`: draft p.44 eq.9.4 supplies the first-action
  `F_B + 1/2 D_B T + 1/3[T,T]` grammar.
- `SOURCE-CONFIRMS`: Portal/Oxford `01:43:32--01:45:53` says curvature alone
  is not exact and requires the quadratic “eddy” completion.
- `SOURCE-CORRECTS`: TOE `01:36:35--01:36:56` corrects “projection” to
  “contraction”; the repository must not impose a projector identity.
- `SOURCE-CORRECTS`: the compressed 2021 residual is not the exact Euler
  covector of the selected noncyclic native action.
- `SOURCE-SILENT`: the selected trace-adapted Shiab sheet, symmetric Clifford
  gauge, moving slots, residual primalizer, `D(L^!)`, all-grade `DM`, weighted
  owner coefficients, polynomial loci, BV quotient, and domain.
- `WATCH-ONLY`: TOE `02:44:06--02:45:13` describes the modern two-connection
  `D^2` as unreleased. It supplies none of the missing equations.

## External datum and constraint surplus

P1/P2/P3 are unchanged and unused. They have the wrong type to select a
Clifford trivialization, moving coefficient, formal adjoint, weighted action
branch, polynomial locus, BV differential, or domain.

The native moving family adds no fitted local coefficient once the symmetric
Clifford gauge is declared. The gauge declaration itself is a construction
choice whose equivalence under alternative spin-frame trivializations has not
yet been globally proved. Global constraint surplus therefore remains
uncomputed.

## What remains open

- the full first-action owner Euler coefficient, not merely its weights;
- coefficientwise right-`H`, Krein, and reality checks for the moving family;
- moving-Shiab polynomial support, including possible cross-grade coupling;
- the negative, nonzero-null, and pure-trace polynomial charts;
- the complete all-grade `DM` coefficient beyond the nonzero exact witness;
- the A0 lower-filtered formal-adjoint/Green comparator;
- a source-derived tangent/BV differential and observation-descended quotient;
- the prolonged moving preboundary form and common analytic domain.

## Next gate

`ECW3D-B2C15N-FULL-FIRST-ACTION-OWNER-EULER-AND-MOVING-POLYNOMIAL-ATLAS`:

1. assemble the direct-`B`, `T=A-B`, moving-Shiab, moving-lowerer, density,
   and graph chains into the full first-action owner Euler coefficient;
2. verify weighted Helmholtz symmetry and coefficientwise right-`H`, Krein,
   and reality identities;
3. recompute the support graph after moving terms and certify its maximal
   minors rather than importing the frozen same-grade decomposition;
4. complete the negative, nonzero-null, and pure-trace charts while retaining
   the zero/nonzero-null tag;
5. only then construct the weighted characteristic kernel and test whether a
   source-derived BV tangent owns any part of it.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. The conjunctive promotion
gate `TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.

## Validation

The final probe passes `71 exact + 4 source receipts + 12 type-level + 12
planted = 99` checks. The two polynomial hostile controls prove that the
held-out point catches a cubic hidden at the three interpolation inputs and
that a root of one selected maximal minor can disappear from the gcd of all
maximal minors. The type-level rows are explicit scope declarations,
not independent computational evidence.
