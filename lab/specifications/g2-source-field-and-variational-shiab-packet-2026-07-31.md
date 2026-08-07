---
title: "G2 source field space and native variational-Shiab packet"
status: active_research
doc_type: specification
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: lab/process/runs/GUH-20260731T143243Z-g2-field-space-native-variational-shiab/run-plan.md
probe: tests/channel-swings/g2_native_variational_shiab_probe.py
grade: "CONDITIONAL NATIVE FIELD/ACTION CONSTRUCTION. The selected graph field space, trace-adapted density-dual contraction, translated-curvature identity, and exact slot-symmetrized Euler map are constructed. The fixed-linear source simplification fails on the native candidate and is not used. Complete metric/reduction/boundary Euler terms and BV--BFV/Noether closure remain for G3."
---

# G2 source field and variational-Shiab packet

## 1. Layer-0 types

| object | type | may not be replaced by |
| --- | --- | --- |
| `S_spin` | `Lambda2 V* tensor S -> V* tensor S` | the bosonic action map |
| `S_epsilon` | `Omega2(ad P) -> Omega13(ad* P)` | a spinorial map or an undualized one-form |
| `E_T` | density-dual Euler covector in `Omega13(ad* P)` | `T`, `S(F)`, or a connection one-form without the pseudo-musical |
| `epsilon_red` | moving LC-equipped reduction | a gauge parameter |
| `B` | graph composite `A_LC(epsilon_red,g_DW)` | an independently varied connection in the selected branch |
| `A` | free endpoint connection, source-side `varpi` reconstruction | an adjoint one-form before an affine origin is declared |
| `T` | derived difference `A-B` | N1's `A-Gamma-U` without a map for `U` |

## 2. Selected field and dependency graph

The G2 source branch uses

```text
free endpoint:       A in Conn(P)
varied reduction:    epsilon_red
complete metric:     g_X and the induced trace-reversed g_DW
graph connection:    B = A_LC(epsilon_red,g_DW)
derived distortion:  T = A-B
graph contraction:   S_epsilon = S_tr(epsilon_red,g_DW,K,kappa_g)
gauge parameter:     g in Gau(P), not a physical field
```

The observation section and boundary/domain data remain fields or supplied
interfaces of the complete theory. Their exact variation is deferred to G3
and G4, but their dependency arrows are not omitted.

The selected source branch does not simultaneously contain the N1
Yang--Mills/parent/current-bridge family. `Gamma_epsilon^A0` remains a hostile
reference comparator; `A0` is not added as another free connection.

The gauge laws are inherited from G1:

\[
A\mapsto g\boldsymbol\cdot A,
\quad
\epsilon_{\rm red}\mapsto g\epsilon_{\rm red},
\quad
B(g\epsilon)=g\boldsymbol\cdot B(\epsilon),
\quad
T\mapsto\operatorname{Ad}_gT.
\]

## 3. Native density-dual Shiab candidate

G2 adopts the already executed RB1c trace-line candidate rather than
repeating the killed same-`Lambda2` route. In compressed notation,

\[
\mathscr S_{\epsilon}^{\rm tr}(F)
=\kappa_{\mathfrak g}^{\flat}\,
\pi_{\mathfrak{sp}}
\left[c(t_{\rm tr}(\epsilon))
\mathscr S_{\epsilon}^{\rm raw}(F)\right],
\]

\[
\mathscr S_{\epsilon}^{\rm raw}(F)
=
\Phi_1(\epsilon)\wedge *F
-\frac12*
\left[
\Phi_1(\epsilon)\wedge*
(\Phi_2(\epsilon)\wedge*F)
\right].
\]

It has the required type

\[
\mathscr S_{\epsilon}^{\rm tr}:
\Omega^2(Y,\operatorname{ad}P)
\longrightarrow
\Omega^{13}(Y,\operatorname{ad}^*P).
\]

The inherited exact controls establish:

- output degree thirteen;
- native Krein-skew/right-`H` carrier;
- moving-soldering covariance;
- nonzero generic full-adjoint response;
- nonzero scalar algebraic-Riemann response after the trace adapter; and
- dependence on the native negative trace line and `(9,5)` Hodge signs.

The unadapted grade-three map remains a live detector of non-Riemannian
curvature but vanishes on the full algebraic-Riemann representation. The
trace-adapted map is selected here because the source action must remain able
to see the gravity stratum.

No continuous left/right ordering is reopened. The bounded RB1c ordering
family already failed its cyclic gate.

## 4. Written first-order action

Let `q` be the symmetric polarization of the connection quadratic term, so

\[
F_{B+T}=F_B+D_BT+q(T,T).
\]

Define

\[
\boxed{
I_1^{\rm var}
=
\int_Y T\wedge\mathscr S_\epsilon^{\rm tr}
\left(F_B+\frac12D_BT+\frac13q(T,T)\right)
+\frac{\kappa_1}{2}\int_YT\wedge\flat_1T.
}
\]

This is a fourteen-form action grammar. `flat_1` includes the declared
DeWitt/Krein/adjoint density dual. It is not a positive Riesz map.

## 5. Exact variational completion

Write

\[
L_{B,\epsilon}
=\mathscr S_\epsilon^{\rm tr}\circ D_B
:
\Omega^1(\operatorname{ad}P)
\to\Omega^{13}(\operatorname{ad}^*P).
\]

Let `L^!` be its boundary-aware formal transpose. Define

\[
C_\epsilon(x,y,z)
=\int_Yx\wedge\mathscr S_\epsilon^{\rm tr}(q(y,z))
\]

and its complete slot symmetrization

\[
C_\epsilon^{\rm sym}(x,y,z)
=\frac1{6}\sum_{\sigma\in S_3}
C_\epsilon(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)}).
\]

Define the two-input density-dual Euler map `M_epsilon` by

\[
\int_Yx\wedge M_\epsilon(y,z)
=C_\epsilon^{\rm sym}(x,y,z).
\]

At fixed `B,epsilon,g_DW` and modulo the displayed Green flux, the exact
`T` Euler covector is

\[
\boxed{
E_T^{\rm var}
=
\mathscr S_\epsilon^{\rm tr}(F_B)
+\frac12(L_{B,\epsilon}+L_{B,\epsilon}^{!})T
+M_\epsilon(T,T)
+\kappa_1\flat_1T.
}
\]

This is not a fit. It is the Fréchet derivative of the written functional.
The coefficients `1/2` and `1/3` divide by the number of varying slots:

- the quadratic term has two slots and emits the symmetric part of `L`;
- the cubic term has three slots and emits the complete symmetric
  polarization.

The exact finite fixture verifies this derivative by rational Richardson
elimination of the cubic central-difference remainder.

## 6. When the source's compressed equation is valid

The source-side expression

\[
E_T^{\rm source}
=\mathscr S_\epsilon^{\rm tr}(F_{B+T})
+\kappa_1\flat_1T
\]

equals the exact Euler covector only if both Helmholtz conditions hold:

\[
\frac12(L+L^!)T
=\mathscr S_\epsilon^{\rm tr}(D_BT),
\]

\[
M_\epsilon(T,T)
=\mathscr S_\epsilon^{\rm tr}(q(T,T)).
\]

An invariant Chern--Simons control satisfies these identities. The moving
noncentral contraction and the inherited native trace-adapted candidate do
not. Therefore the compressed source `Upsilon` is killed for the selected
native map, while `I_1^var` and `E_T^var` survive.

The factorization failure is structural. RB1c and the G2 plant exhibit
`y,z` with zero polarized curvature but a nonzero symmetrized Euler response.
No one-input linear `S(q(y,z))` can represent that response. The two-input
map `M_epsilon` must remain explicit.

## 7. Graph-chain and epsilon response

Because `T=A-B`,

\[
\delta T=\delta A-\delta B.
\]

`B` is not varied independently. For a reduction variation,

\[
\delta_\epsilon B
=D_\epsilon A_{\rm LC}[\delta\epsilon],
\qquad
\delta_\epsilon T=-\delta_\epsilon B.
\]

The same variation moves

\[
t_{\rm tr},\Phi_1,\Phi_2,*,\pi_{\mathfrak{sp}},
\kappa_{\mathfrak g}^{\flat},\operatorname{vol}_{G_{\rm DW}}.
\]

Hence `E_epsilon` contains both the graph-chain response through `B,T` and
`D_epsilon S_epsilon`. The exact fixture proves that a moving insertion has a
nonzero explicit response and that omitting `delta T=-delta B` breaks the
endpoint chain rule.

The metric and section variations have analogous graph terms. G2 declares
them; G3 must compute them together with the boundary potential.

## 8. Boundary and BV--BFV handoff

The formal transpose `L^!` is not an instruction to discard a total
derivative. It is defined by

\[
\int_Yx\wedge L(y)-\int_Yy\wedge L^!(x)
=\int_{\partial Y}\mathcal G_L(x,y).
\]

G3 must produce `mathcal G_L`, the complete presymplectic potential, the
moving four-dimensional defect corner term, and the coupled gauge identity.
Until then, the formula for `E_T^var` is a bulk-plus-declared-flux packet,
not a closed boundary value problem.

## 9. Field ledger passed to G3

| object | G2 policy | G3 obligation |
| --- | --- | --- |
| `A` | free connection | compute `E_A`; at fixed graph fields its direct contribution is `E_T` |
| `epsilon_red` | varied reduction | full `B,T,S,K,G,density` chain rule |
| `g_X/g_DW` | varied complete-theory metric | Hodge, trace, LC, density, and induced-gravity response |
| `B` | graph composite | no independent `E_B`; return response through its owners |
| `T` | derived `A-B` | use exact `E_T^var`, not compressed source `Upsilon` |
| `S_epsilon` | graph composite | include its first variation and adjoint/Green form |
| observation section/defect | retained | boundary/corner and distributional response |
| P1/P2/P3 | external ledger | unused in G2; never action coefficients |

## 10. Surplus and result boundary

No positive global surplus is claimed. Fixed source guidance supplies
`1/2,1/3`; the native trace line supplies the adapter without a new local
direction. Still unpriced are the overall relative normalization, `kappa_1`,
global reduction component, domain/boundary condition, stationary orbit,
physical projections, and P3.

G2 constructs a differentiable source-action grammar and its true bulk Euler
geometry. It does not establish complete differentiability on the G4 domain,
Noether/BV closure, N1 equivalence, a vacuum, Standard Model realization,
index, count, cosmological amplitude, or PP3.
