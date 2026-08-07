---
title: "Eric/Curt Wave 3D-B2C15R2: full linear-bridge BCH, covariant split-action candidate, and order-lowered curvature owner"
status: active_research
doc_type: construction_result
created: 2026-08-02
branch: agent/null-clifford-omega1-repair
run: RUN-20260802-104349-gu-formalization-ecw3d-b2c15r2-direct
registry: lab/process/eric-curt-wave3d-b2c15r2-full-bch-action-gauge-curvature-adjoint.json
probe: tests/channel-swings/eric_curt_wave3d_b2c15r2_full_bch_action_gauge_curvature_adjoint_probe.py
grade: "PARTIAL CONSTRUCTION PASS WITH FULL LINEAR-BRIDGE BCH, PROJECTED COVARIANT SPLIT-ACTION CANDIDATE, ORDER-THREE CURVATURE CANCELLATION, LIVE A2-Z0 SUBROUTE, AND OBSERVATION-SUPPORT STOP"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# B2C15R2 full BCH, covariant split-action candidate, and curvature adjoint

## Result first

B2C15R2 repairs the three largest weaknesses left by B2C15Q.

First, the current linear grade-3/11 distortion bridge can be summed exactly,
not merely through its quadratic term. With

\[
u=c_3A+c_{11}*A,\qquad \Delta=c_3^2-c_{11}^2,
\]

the complete homogeneous connection is

\[
q_{\rm MC}=-\Delta\,\operatorname{pr}_2
\left[\operatorname{ad}_A\,
\phi(\Delta\operatorname{ad}_A^2)dA\right],
\qquad
\phi(z)=\sum_{k\ge0}\frac{z^k}{(2k+2)!}.
\]

Thus the full controlled linear bridge depends only on `Delta`, and both
`c11=+c3` and `c11=-c3` vanish to every order. This is not a global theorem
about arbitrary nonlinear reductions: an explicit grade-seven completion
breaks same-`Delta` equality.

Second, the new bare `lambda_red <q_red,Shiab(F)>` term proposed in B2C15Q is
rejected. A connection must be covariantized relative to another connection:

\[
K_u=-\Delta\operatorname{pr}_2\left[
\operatorname{ad}_A\phi(\Delta\operatorname{ad}_A^2)D_BA\right],
\qquad q_B=B+K_u.
\]

`q_B` transforms as a projected reduced `h/Spin` connection candidate and
`K_u` tensorially in the controlled reduced fixture. Full source `H/Sp`
equivariance remains conditional on the same-bundle embedding. The candidate
action move is the coefficient-free split

\[
(B,T)\longmapsto(B+K_u,T-K_u)
\]

inside Weinstein's already written first-action grammar, holding the total
connection fixed. No `lambda_red` is added. The finite action calculation in
this gate tests a generic split direction, not yet the derived `K_u(T)` in
that finite model; the actual substitution remains part of the next gate.

Third, the apparent order-three Zorro/curvature symbol cancels. Its top block
is a pure-gauge metric variation killed by the curvature symbol. The full
`A2 o Z0` curvature-principal subroute is live at order two, but the complete
effective order-two symbol still needs `A1 o Z1` and all subprincipal terms;
they could alter or cancel that summand. The surviving stop is now geometric
rather than algebraic: `q_B` has not yet been embedded and descended
in the source adjoint bundle, and no canonical support or selected equation
lift has turned the upstairs thirteen-form into a four-dimensional equation.

## Plain English

The distortion really can generate a connection-like correction, and for the
linear bridge we now know its entire nonlinear formula. Its type-compatible
candidate placement needs no new coupling: move the same tensorial amount
from the distortion slot to the connection slot, leaving their physical sum
unchanged. A generic finite comparator proves such split directions need not
be empty bookkeeping. It does not yet prove that the action notices the
specific derived `K_u(T)`.

The remaining problem is to prove that this local correction is an honest
global field in the same bundle as Weinstein's connection, and then to say
how its upstairs equation becomes an observed equation without choosing an
arbitrary cutoff on a noncompact fibre. The external datum cannot force those
maps because it has the wrong type, so P1/P2/P3 remains intact.

## Layer 0

| object | type | status |
| --- | --- | --- |
| source `T` | homogeneous connection difference/distortion | source explicit |
| `u(T)` | reduction coordinate in the grade-3/11 quotient | repository candidate |
| `q_MC` | homogeneous Maurer--Cartan `h`-part | exact for the linear bridge |
| `q_B` | connection covariantized relative to `B` | exact conditional same-bundle formula |
| `K_u=q_B-B` | tensorial connection difference | exact conditional same-bundle formula |
| split substitution | `(B,T)->(B+K_u,T-K_u)` at fixed total connection | candidate grammar; generic finite comparator only |
| raw thirteen-form pullback | pullback to `X4` | zero by degree |
| fibre Gysin | ten-fibre integration | four legs eligible, support open |
| equation-dual | dual of a specified observation lift | distinct and unbuilt physically |

The source redundancy `Xi=D_omega Upsilon` is also not an off-shell Noether
identity, and a field pullback is not automatically an Euler-covector
pushdown.

## Source collision

- `SOURCE-CONFIRMS`: the written first action pairs `T` with the completed
  Shiab residual and contains the fixed `1/2` and `1/3` segment weights.
- `SOURCE-CONFIRMS`: the fibre pairing is trace-reversed Frobenius and fields
  are described using observation sections.
- `SOURCE-CORRECTS`: `Xi=D_omega Upsilon` is a redundancy target, not a
  supplied Ward identity; field observation is not a supplied Euler pushdown.
- `SOURCE-CORRECTS`: source `T`, `q_MC`, `q_B`, and `K_u` are not synonyms.
- `SOURCE-SILENT`: the repository reduction, BCH resummation, coefficient
  pair, covariant split embedding, selected observation lift/support law, BV,
  and analytic domain.

The source tells us which grammar to respect. The executable construction,
not the attribution, supplies the new mathematics.

## Full linear-bridge BCH theorem

The active Clifford volume satisfies `nu^2=1`, and every one of the `364`
grade-three blades obeys `*A=nu A=-A nu`. Exact nested-commutator checks give

\[
\operatorname{ad}_u^{2k+1}(du)
=\Delta^{k+1}\operatorname{ad}_A^{2k+1}(dA).
\]

Summing the convergent exponential series yields the displayed full formula.
For `A=e012` and `dA=e013`,

\[
q_{\rm MC}=\frac{1-\cos(2\sqrt\Delta)}2e_{23}
=\left(\Delta-\frac{\Delta^2}{3}
+\frac{2\Delta^3}{45}-\frac{\Delta^4}{315}+\cdots\right)e_{23}.
\]

The reduction is reductive, not symmetric:
`[e012,e345]=2e012345` is a live grade-six bracket. A separate fixed
grade-seven completion also prevents overgeneralization: same-`Delta` pairs
produce `2/3 e23` and `2/27 e23` in its quadratic-plus-quartic connection.
The theorem therefore covers fixed coefficients, parallel Hodge/volume, and
the linear bridge with the same Hodge pair in `du`; the full `m`-part, varying
Hodge, nonlinear odd grades, global logarithm chart, and source identity stay
open.

The same grade-six witness is also a type check on the covariant formula: the
unprojected commutator is not generally `h`-valued. The required `pr2` removes
that impostor, and the executable gate verifies this projection commutes with
all `91` reduced grade-two `h/Spin` generators. This is not full source
`H/Sp` equivariance, which belongs to the same-bundle descent gate.

## Covariant action placement

Replacing `dA` by `D_BA` supplies the missing gauge cocycle. Exact finite
nonconstant-gauge tests show that `q_B` has the affine connection law while
`K_u` transforms tensorially; the raw-`dA` route fails.

The split grammar is tested with an independently chosen noncentral direction
in a finite G2 model. At split scales
`-2,-1,0,1,2`, the action values are `115/2,32,23/2,2,19/2`, giving central
first response `-15`. The total endpoint connection and curvature are fixed,
common-conjugation covariance passes, and the source `1/2` and `1/3` weights
retain their exact affine-segment meaning. The action changes, so the move is
not automatically a trivial reparameterization. Because that finite `K,dK`
is not computed from the bridge's `u(T),D_Bu`, this is a generic split-action
comparator, not the actual derived-`K_u` source-action substitution.

The leading `K_u` owner also has an exact Green return:

```text
direct 331/28 = bulk 415/28 + boundary (-3).
```

What is not yet proved is that the reduced `h`-connection embeds into the
same source adjoint bundle on every patch and descends on overlaps. Nor has
the full entire-series `K_u` been substituted into the finite action or
differentiated through every source action slot. Physical constraint surplus
is therefore `UNCOMPUTED`.

## Curvature owner: order three cancels

The principal Zorro cross-block is `xi symmetric-product v`, a pure-gauge
total-metric variation. The curvature principal symbol kills it exactly.
The differentiated observed base Riemann symbol retains rank `6` for both
spacelike and null held-out covectors. The full `A2 o Z0` principal-curvature
block must also move the ten-dimensional trace-reversed DeWitt fibre metric;
after frame/spin conversion and trace-adapted Shiab its ranks are `10` and `4`.
Thus the third-order symbol is zero and one second-order summand is live.
The complete effective second-order symbol remains open until `A1 o Z1` and
the subprincipal coefficient terms are assembled, because they land at the
same order and could modify or cancel this summand.

An exact variable-density, moving-Krein-lowerer sequential Green comparator
gives

```text
direct 30871333/360360
= bulk 89610013/360360 + inner boundary 146 + outer boundary (-309).
```

The direct order-two formal adjoint equals `Zorro^! curvature^!`; its cubic
coefficient is zero and its quadratic coefficient has rank `2` in the
fixture. Dropping either boundary, freezing the density, or replacing the
Krein lowerer by a positive identity fails. Separately, order-one moving
coefficient slots can differentiate background curvature to a total-metric
third jet, as `-(g''p)'=-g'''p-g''p'` shows. Since native Zorro already depends
on the base first jet, that is generically a base-metric fourth-jet ceiling.
This scalar comparator fixes its own sequential adjoint identity; it neither
assembles nor fixes the complete native effective second-order coefficient.

## Observation and support stop

The actual thirteen Shiab legs split into four `(horizontal 3, vertical 10)`
and nine `(horizontal 4, vertical 9)` terms. Ordinary fibre integration keeps
exactly the four former terms. A compact unit-volume ten-torus is a useful
normalization control, not the Lorentz-metric fibre.

The real fibre is noncompact and homogeneous. Any invariant scalar cutoff is
constant, so an invariant compactly supported cutoff must be zero. A nonzero
Gysin map consequently needs dynamical decay/proper support or additional
observation structure.

An equation-dual is a distinct route. A horizontal normalized lift selects
the four Gysin legs; a soldered vertical block also sees the other nine.
Dual overlap descent passes in the finite patch control, while covariant
rather than dual transport fails. Even `R L=1` leaves upstairs leakage, so a
left inverse alone does not select the physical equation.

## External datum and scope

P1/P2/P3 remains unchanged and unused. P1/P2 is an orientation line over a
configuration loop, not an orientation, support kernel, bundle embedding, or
equation lift on the metric fibre. Spending it here would hide rather than
solve the missing construction.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`; `TG-1 AND TG-2 AND TG-3`
remains `NOT_PROMOTED`. This gate claims no BV/BFV phase space, analytic
domain, stationary vacuum, Standard Model recovery, generation count,
cosmological prediction, or public/canon/status change.

## Next gate

`ECW3D-B2C15R3-SAME-BUNDLE-COVARIANT-SPLIT-NATIVE-FIRST-VARIATION-AND-OBSERVATION-SUPPORT`

1. Embed `q_B/K_u` into the source adjoint bundle and prove patch descent.
2. Substitute full `K_u` into the actual first action and derive every native
   source-coordinate Euler, Green, gauge, and Ward return.
3. Assemble `A1 o Z1` and all subprincipal curvature/coefficient terms to
   determine the complete effective order-two symbol and any cancellations.
4. Derive dynamical decay/proper support or a geometrically selected equation
   lift with descent and no leakage, without spending P1/P2/P3.
5. Only then compute physical response rank and constraint surplus.
6. Keep nonlinear odd-grade completion as a rival if the linear route remains
   blind to `c3:c11` beyond `Delta`.
