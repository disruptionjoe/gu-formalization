---
title: "Eric/Curt Wave 3D-B2C15O: source-coordinate return and selected (9,5) coefficient-fixture stabilizer"
status: active_research
doc_type: construction_result
created: 2026-08-01
branch: agent/null-clifford-omega1-repair
run: historical-investigation
registry: lab/process/eric-curt-wave3d-b2c15o-native-y14-background-stabilizer.json
probe: tests/channel-swings/eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py
grade: "B2C15O PARTIAL CONSTRUCTION PASS WITH SOURCE-COORDINATE CORRECTION AND SCOPED ALGEBRAIC FIXTURE. On the literal equations-9.2-to-9.3 epsilon-family Shiab branch, the displayed source coordinates are fixed-(epsilon,varpi,g), not fixed-(A,epsilon_red,g). Exact return gives E_varpi=E_T and changes the metric equation by +(D_g Gamma)^!E_T relative to B2C15N's fixed-A equation. The correction and its Green companion are nonzero; reusing the fixed-A metric equation gives a nonzero Helmholtz defect, while the corrected system passes and retains realized order table [[1,2,2],[2,2,3],[2,3,2]]. Equality of the literal epsilon family with equation 9.4's odot_omega remains unverified. A trace-reversed-carrier-compatible algebraic fixture is built from a realizable four-dimensional constant-curvature metric two-jet and explicit affine B/constant-T germs. Inside diagonal Spin(9,5), the selected coefficient-tuple isotropy is 36, its intersection with the one non-null xi=e0 stabilizer is 36, and a held-out compatible tuple has isotropy 28. These are not full Zorro/DeWitt Y14 action-jet or ambient Sp stabilizers. Exact Clifford-word and independent 128-by-128 right-H/Krein/C-plus checks pass. Source epsilon versus quotient epsilon_red, the odot-family fork, the Zorro/DeWitt total-space jet, the (7,7)-to-(9,5) port, full native fixed-varpi coefficients, global pushforward/domain, BV, and physics remain open."
canon_verdict_change: none
---

# B2C15O source coordinates and selected coefficient-fixture stabilizer

## Result first

B2C15O found a source-coordinate correction before attempting another atlas.
The correction is mathematically live and changes which metric equation belongs
to Eric's displayed action.

The source uses

\[
\omega=(\epsilon,\varpi),
\qquad
B=\Gamma(g)+q_g(\epsilon),
\qquad
T=\varpi-q_g(\epsilon),
\]

so the total connection is

\[
A_{\rm tot}=B+T=\Gamma(g)+\varpi.
\]

B2C15N instead used independent total-connection coordinates
`(A,epsilon_red,g)` with `T=A-B`. Its theorem remains correct in those
coordinates, but holding `A` fixed while varying `g` is not holding source
`varpi` fixed.

Starting from the independent endpoint covectors `(E_B,E_T)` and selecting
the literal equations-9.2-to-9.3 epsilon-family branch, the source-coordinate
return is

\[
\boxed{E_\varpi=E_T,}
\]

\[
\boxed{
E_\epsilon=C_\epsilon+(D_\epsilon q)^!(E_B-E_T),
}
\]

and

\[
\boxed{
E_g^{\rm src}
=C_g+(D_g\Gamma+D_gq)^!E_B-(D_gq)^!E_T.
}
\]

Therefore

\[
\boxed{
E_g^{\rm src}-E_g^{A\text{-fixed}}
=(D_g\Gamma)^!E_T.
}
\]

The executable noncentral fixture proves this correction is nonzero. Direct
variation equals the corrected bulk tuple plus a nonzero preboundary term, and
the corrected owner linearization obeys exact integrated Helmholtz reciprocity.

## Plain English

We had been wiggling the total connection while keeping it fixed as the metric
moved. Eric's variables keep the gauge potential *relative to the metric
connection* fixed instead. When the metric moves, the total connection then
moves with its Levi--Civita part. That missing motion contributes an additional
metric source.

It does not change the highest derivative orders in this finite example, but it
does change the actual equation. So the previous order table survives this
test, while the previous metric equation cannot be called the literal
source-coordinate equation.

The second result is a scoped stabilizer warning. The trace direction alone
leaves a large symmetry. Once this selected curvature/distortion coefficient
tuple is fixed, its isotropy shrinks. A held-out compatible tuple has a second
isotropy dimension. This earns the need to stratify such algebraic candidate
tuples; it does not yet compute the stabilizer of a GU Zorro/DeWitt action jet
or prevent the trace group from acting on the larger ambient family.

## Layer 0

| object | type | status |
| --- | --- | --- |
| source `varpi` | ad-valued one-form relative to `Gamma(g)` | source explicit |
| total `A_tot=Gamma+varpi` | full endpoint connection | derived source coordinate |
| `B=Gamma+q_g(epsilon)` | gauge-rotated reference connection | source explicit / normalized |
| `T=varpi-q` | homogeneous displacement | source explicit |
| B2C15N `A` | independent total endpoint connection | distinct coordinate choice |
| source `epsilon` | H-valued gauge transformation / Stueckelberg coordinate | source explicit |
| repository `epsilon_red` | quotient reduction coordinate with tangent `m` | **HOMONYM**; bridge open |
| selected algebraic coefficient fixture | realizable four-dimensional metric two-jet plus explicit affine `B`/constant-`T` germs in the active carrier | constructed here |
| GU Zorro/DeWitt total-space jet | image of the metric-bundle metric-to-LC-to-spin chain, including vertical and mixed jets | not constructed |
| global action background | descended smooth fields plus support/domain | not constructed |
| physical vacuum | owner Euler solution plus observation/domain conditions | not constructed |

The fixed graph owner called `z` in the finite coordinate calculation certifies
the chain rule for a generic `q` graph. It is not an identification of source
`epsilon` with repository `epsilon_red`.

## Literal epsilon-family branch and the unresolved odot fork

Equations 9.2--9.3 literally display an epsilon-family candidate:

- draft equations 9.2--9.3 define the contraction as
  `Shiab_epsilon`, using the epsilon-conjugated invariant forms and Hodge star;
- equation 9.4 abbreviates the action coefficient as `odot_omega`;
- the pp.56--57 summary says the Shiab depends on the gauge transformation.

On that selected literal branch,

\[
D_\varpi\mathscr S=0
\]

because no `varpi` occurs in the displayed formula. But the present source
receipt does not prove that equation 9.4's abbreviated `odot_omega` is
definitionally identical to equations 9.2--9.3's epsilon family. Therefore a
genuinely omega-dependent branch remains separately priced. Under
`A_tot=Gamma+varpi`, its translation derivative would modify the existing
varpi equation, not add a second varpi owner.

This does not prove that the displayed Shiab is the unique or final source
choice, and it does not port the source `(7,7)` presentation to the active
trace-reversed `(9,5)` real form.

## Exact coordinate-return fixture

The B2C15N graph splits as

\[
B=\Gamma(g)+q(z,g)
\]

with

\[
\Gamma(g)=H_0g+H_1g',
\qquad
q=G_0z+G_1z'+M g z'.
\]

The source pullback replaces

\[
A=\varpi+\Gamma(g),
\qquad
T=\varpi-q.
\]

Automatic Euler differentiation and the assembled endpoint return agree
exactly. On the held noncentral polynomial background:

```text
direct variation = -43290707 / 16632
bulk             =  -5347571 / 16632
preboundary      =       -6844 / 3
```

and `direct = bulk + preboundary`.

The coordinate correction has the isolated Green companion

\[
\Theta_\Gamma=(H_1^TE_T)\,\delta g,
\]

and the exact preboundary identity

\[
\Theta_{\rm src}
=\Theta_{A\text{-fixed}}\big|_{\delta A=\delta\varpi+D_g\Gamma\,\delta g}
+\Theta_\Gamma.
\]

The compactly supported Hessian pairing is

```text
6740763397 / 1784742960
```

in both orders. Reusing the fixed-`A` metric equation in the source tuple gives
the exact nonzero Helmholtz defect

```text
79042325 / 279351072
```

so the correction is not bookkeeping. It is live, but the realized
grouped order matrix remains

\[
\begin{pmatrix}
1&2&2\\
2&2&3\\
2&3&2
\end{pmatrix}_{(\varpi, q, g)}.
\]

This is a useful non-result: coordinate choice changes the equation without
necessarily changing its highest-order skeleton.

## One trace-reversed-carrier-compatible algebraic fixture

The selected fixture is fixed before a conormal or determinant is inspected.

1. At one four-dimensional normal-coordinate point, the metric zero-jet is
   `eta` and the spin orientation is fixed; the metric is not globally flat.
2. The active carrier is split into four observed and ten vertical directions.
3. The trace-reversed DeWitt/gimmel metric gives
   `(3,1)+(6,4)=(9,5)` and a negative trace direction.
4. A unit constant-sectional-curvature algebraic Riemann tensor supplies a
   realizable four-dimensional normal-coordinate metric two-jet. In the
   probe's convention its spin curvature is exactly
   `(1/2) gamma_left gamma_right`.
5. The distortion is the lexicographically first pair of exact native,
   right-H/Krein/C-compatible grade-three Clifford blades with a nonzero
   commutator, placed in two independent one-form legs.
6. The explicit radial-gauge affine germ
   `B_j(y)=(1/2) sum_i F_ij y^i` and constant `T` give, at the origin,
   `F_B=dB`, `D_B T=0`, and `F_A=F_B+q(T,T)`. Nonzero-`D_B T` and independently
   assigned-`F_A` plants both fail the shortened identity.

The exact support witnesses are

```text
F_B              grade 2
q(T,T)           grade 2
S_tr(F_B)        grade 2
S_tr(q(T,T))     grade 6
```

Every Clifford coefficient in `F_B`, `T`, `q(T,T)`, `F_A`, and both
trace-adapted outputs passes exact combinatorial right-quaternionic,
Krein-skew, and C-plus word identities. An independent native `128 x 128`
matrix realization also gives zero defect. Live plants reject wrong
conjugation/dagger/transpose signs, corrupted beta/right-H/C-plus words, a
positive-Hilbert replacement, a forbidden grade, and an imaginary phase.

This is not yet proved to be in the image of GU's specific Zorro/DeWitt
total-space metric jet. Its vertical and mixed LC curvature, moving Shiab,
density, lowerer, graph, and complete owner-Hessian coefficients remain open.

## Selected diagonal-Spin isotropy calculation

The exact Lie-kernel chain is:

| fixed data | stabilizer dimension |
| --- | ---: |
| observed `4+10` split | 51 |
| split plus negative trace line | 42 |
| split, trace, constant-curvature metric jet | 42 |
| selected coefficient tuple | 36 |
| selected tuple intersected with the one non-null `xi=e0` stabilizer | 36 |
| held-out compatible noncommuting coefficient tuple | 28 |

These kernels are computed only inside the 91-dimensional diagonal
`spin(9,5)` subalgebra, not the full `sp(32,32;H)` algebra. For the one tested
non-null conormal, vector and covector fixing are identified using the metric
dual. A future pointwise symbol chart would need an object of the form

\[
K^k_{y,\xi}
=\operatorname{Stab}(j^k_y\bar\Phi)
\cap\operatorname{Stab}(\xi),
\]

but the present calculation is only its selected-tuple diagonal-Spin
comparator. It does not determine disconnected components, full ambient
stabilizers, conormal families, global sheets, or the global gauge
automorphism group. The `36` and `28` values show at least two isotropy types
among these algebraically compatible candidate tuples; GU admissibility of a
full background remains unproved.

## Source disposition

- `SOURCE-CONFIRMS`: draft pp.43--44 equations 9.1--9.5 own
  `(epsilon,varpi,g)`, the completed first action, and the displayed varpi
  variation.
- `SOURCE-CONFIRMS`: draft pp.56--57 equations 12.4--12.7 make `varpi`
  relative to `nabla^g` and write `T` as the difference from the
  gauge-rotated metric connection.
- `SOURCE-IMPLIES-FOR-LITERAL-BRANCH`: equations 9.2--9.3 display an
  epsilon-dependent Shiab, so `D_varpi Shiab=0` on that literal family.
- `SOURCE-SILENT`: whether equation 9.4's `odot_omega` is identical to that
  epsilon family or supplies a genuinely omega-dependent rival.
- `SOURCE-CONFIRMS`: Portal/Oxford `02:23:30--02:23:52` gives the Zorro
  metric-to-LC-to-Y-metric-to-spin-connection chain.
- `SOURCE-CONFIRMS`: TOE `02:19:17--02:20:33` places gauge-rotated
  Levi--Civita in the contorsion slot.
- `SOURCE-CORRECTS`: B2C15N's fixed-`A` metric equation is not the displayed
  source's fixed-`varpi` metric equation.
- `SOURCE-SILENT`: the source-epsilon to quotient-reduction tangent bridge,
  active `(9,5)` port, full native fixed-varpi coefficient, true background
  selection, global metric pushforward, BV quotient, and domain.

## External datum

P1/P2/P3 are unchanged and unused. They have the wrong types to provide the
coordinate map, the source-epsilon/reduction bridge, a background jet,
stabilizer, contraction port, global pushforward, quotient, or domain.

## What this does not claim

The selected fixture is a local algebraic construction test, not a stationary solution or
vacuum. It does not prove:

- a global `Y14` action background or observation section;
- the complete full-carrier `E_B`, `E_T`, or fixed-varpi metric coefficient;
- the GU Zorro/DeWitt total-space jet or its full ambient/action stabilizer;
- a complete support/rank atlas under any actual action-jet stabilizer;
- a source-derived tangent/BV differential;
- a Green domain, hyperbolicity, positivity, or unitarity;
- Standard Model, generation, cosmological, dark-matter, or PP3 output.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`, and
`TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.

## Next gate

`ECW3D-B2C15P-SOURCE-EPSILON-REDUCTION-TANGENT-BRIDGE-AND-NATIVE-FIXED-VARPI-COEFFICIENT`:

1. type the manuscript's H-valued epsilon tangent and the repository's
   quotient reduction tangent on the tilted inhomogeneous-gauge graph;
2. prove a relating map or retain them as rival owner systems;
3. resolve or explicitly branch equation 9.4's `odot_omega`, then port the
   selected epsilon-Shiab candidate from its source presentation to
   the active trace-reversed `(9,5)` right-H/Krein carrier, or record the exact
   obstruction;
4. construct the GU Zorro/DeWitt total-space metric/LC/spin jet and the full
   native fixed-varpi `E_B,E_T,E_g` coefficient, then recompute support/orders
   under its actual ambient action-jet/conormal-family stabilizer;
5. only then revisit polynomial rank charts, BV, or a global metric
   pushforward/domain.

## Artifacts

- Probe:
  `tests/channel-swings/eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py`
- Registry:
  `lab/process/eric-curt-wave3d-b2c15o-native-y14-background-stabilizer.json`
- Predecessor:
  `explorations/eric-curt-wave3d-b2c15n-full-owner-euler-moving-atlas-2026-08-01.md`
