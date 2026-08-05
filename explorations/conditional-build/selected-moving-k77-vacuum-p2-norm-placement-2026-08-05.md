---
artifact_type: construction_result
created: 2026-08-05
status: P2_NORM_DERIVED_FULL_II_ON_CANONICAL_GAUSS_SECTOR__SELECTED_NONCYCLIC_K77_INVARIANT_ALGEBRAIC_STATIONARY_BRANCH_EXACT__SPECIAL_PRINTED_ENDPOINT_COINCIDENCE__PHYSICAL_STABILITY_TOTALIZATION_AND_GREEN_DOMAIN_OPEN
lane: "1"
functional_channels: [COMPOSE, SOURCE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
fork_assumed: SIGNATURE_AMBIENT_K77__ADMITTED_X_SPIN_AND_SOURCE_P_H__SELECTED_DISPLAYED_COMM_SYMI_SYMI_SHIAB
source_return: SOURCE-CONFIRMS
free_object_delta: "zero fields, data, selectors, scales, potentials or boundary conditions; P2_norm is retired as a free action fork while P2_datum is untouched"
scripts:
  - tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py
  - tests/channel-swings/selected_moving_k77_vacuum_p2_norm_independent.sage
registry: lab/process/selected-moving-k77-vacuum-p2-norm-placement.json
---

# Selected moving-K77 algebraic vacuum and full-II action norm

## Result first

Two predecessor gates move.

First, the written augmented-torsion action selects the **full second
fundamental form norm**, not the mean-curvature trace-square, on the canonical
Gauss gravitational sector. The missing map is not the previously built
vertical rank-ten `q` receiver. It is the horizontal off-diagonal connection
block

\[
 \operatorname{Sym}^2H^*\otimes V
 \longrightarrow H^*\otimes\mathfrak{so}(H\oplus V),
 \qquad H\cong\mathbb R^{1,3},\quad V\cong\mathbb R^{6,4}.
\]

It has rank 100, an exact metric-adjoint left inverse, and an orthogonal
projector. The source action pairing pulls back exactly to the nondegenerate
rank-100 ordered `II` norm. Tracing first produces rank ten. Therefore the
action-norm premise called `P2_norm` is no longer one free bit in the selected
canonical K77 construction. The unrelated external-datum ledger object
`P2_datum` is unchanged and unused.

Second, the selected non-cyclic moving K77 Shiab has a nonzero invariant
algebraic stationary branch. At flat reference connection, constant fields and
fixed metric, put

\[
 T=t\Phi_1,\qquad
 \bar F=\frac13T^2.
\]

Direct evaluation of the **scalar action**, including the one-third eddy and
therefore its Fréchet companion, gives

\[
 \boxed{I(t)=1456t^3+7\kappa_1t^2},
 \qquad
 \boxed{t_*= -\frac{\kappa_1}{312}}. \tag{1}
\]

All 196 grade-one and all 196 Hodge-dual grade-thirteen translation
derivatives vanish exactly at `t_*`. Spin invariance then closes the full
algebraic adjoint gradient: these are the only invariant lines in
`C* tensor Cl(C)`. A co-moving epsilon-orbit derivative also vanishes.

This is not yet a stable physical vacuum. The radial Hessian is

\[
 I''(t_*)=-14\kappa_1. \tag{2}
\]

For positive `kappa_1` the nonzero branch is radially unstable. Moreover the
derivative/constraint, totalization/current and common Krein/Green domain are
still unbuilt. The exact achievement is a selected-action **algebraic
stationary branch**, not a cosmological vacuum, magnitude, screening result or
prediction.

## Plain English

The action already contained the deciding information. Its quadratic term
measures the whole difference between two connections. Once the part of that
connection difference which bends the observed four-manifold is written
correctly, the action measures every component of the bending tensor. It does
not first squeeze that tensor down to its trace. So the earlier “full bending
or trace only?” choice was not an external bit after all; it was an uncomposed
piece of the existing action.

The same selected action also has a very natural nonzero stationary shape:
the augmented torsion is proportional to GU's canonical Clifford-valued
one-form `Phi1`. The proportionality is fixed by the already-present
coefficient `kappa_1`. But this stationary shape sits on top of the hill in
the radial direction for the naïve positive sign. It tells us the nonlinear
selected action is not empty; it does not yet tell us which configurations
are physically allowed or stable.

## 1. Layer 0

| name | object here | not identified with |
| --- | --- | --- |
| augmented torsion `T` | full adjoint-valued one-form, difference of two connections | ordinary torsion or an `II` tensor supplied in advance |
| horizontal Gauss receiver | symmetric vertical output of `T_mu` acting on tangent `h_nu` | the vertical `q=g/2` coefficient receiver |
| `II_s` | full normal-valued symmetric two-tensor from the Gauss formula | mean curvature `H=tr II` |
| `P2_norm` | former binary: full action norm versus trace-before-norm | external-datum ledger `P2_datum` |
| selected action Euler | derivative of the written scalar action | globally killed source-printed shortcut |
| algebraic branch | constant flat-reference zero-jet stationary field | closed-domain PDE solution or stable physical vacuum |
| epsilon orbit | simultaneous motion of `T` and `Phi` by conjugation | a selector for epsilon's physical value |
| Einstein recovery | one simple massless pole with plus/cross | one pole total or viability of the distinct GU partner |

The crucial correction is the first receiver row. The prior rank-ten map acts
on **vertical one-form coefficients** and evaluates them on `q`. The Gauss map
needed for `II` acts on the **horizontal connection coefficient** and applies
that endomorphism to tangent vectors. Equal target dimensions would not make
these maps the same.

## 2. Divergent pre-assessment and preregistered kills

Ten lightweight lenses were run before construction:

| lens | danger | disposition |
| --- | --- | --- |
| differential geometry | reuse the wrong rank-ten receiver | replaced by the Gauss off-diagonal connection block |
| representation theory | check one tensor rather than the whole carrier | rank-100 receiver/right inverse built |
| Clifford/Krein geometry | silently use a positive coefficient norm | invariant indefinite trace pairing retained |
| variational analysis | use the source-printed endpoint | scalar action differentiated directly |
| gauge geometry | call epsilon covariance vacuum selection | orbit derivative separated from branch selection |
| invariant theory | solve only the radial ansatz | both possible invariant gradient lines checked |
| hyperbolic PDE | call algebraic stationarity a physical solution | Green/domain gate kept open |
| mathematical physics | erase the massive partner or instability | both retained as GU-facing information |
| source criticism | use a nearby “norm square” phrase as proof | exact released action and carrier located |
| epistemic breadth | protect a superseded cyclic or K95 object | selected K77 non-cyclic map and current global frame used |

Pre-registered kills fired twice. The vertical rank-ten receiver was rejected
as the wrong object. Later, the expected negative control at the stationary
branch failed: the source-printed endpoint also vanishes there. That special
coincidence is recorded below rather than explained away.

## 3. The complete Gauss connection block

Write `C=H plus V` with metrics `g_H` and `g_V`. For
`II in Sym2(H*) tensor V`, define for each base index `mu` a map
`B_mu:H->V` by

\[
 B_\mu(h_\nu)=II_{\mu\nu}.
\]

Its metric-skew completion is

\[
 \iota(II)_\mu=
 \begin{pmatrix}
 0&-g_H^{-1}B_\mu^Tg_V\\
 B_\mu&0
 \end{pmatrix}
 \in\mathfrak{so}(H\oplus V). \tag{3}
\]

Conversely, for a general horizontal connection difference `A_mu`, define

\[
 R(A)_{\mu\nu}
 =\frac12\left[
 \operatorname{pr}_V(A_\mu h_\nu)
 +\operatorname{pr}_V(A_\nu h_\mu)
 \right]. \tag{4}
\]

The exact coordinate calculation proves

\[
 R\iota=1_{100},\qquad
 P=\iota R,\qquad
 P^2=P,\qquad \operatorname{rank}P=100. \tag{5}
\]

With

\[
 \beta(A,B)=-\frac12\operatorname{tr}(AB),
\]

the source action's coefficient pairing satisfies

\[
 \sum_\mu g_H^{\mu\mu}\,
 \beta\bigl(\iota(II)_\mu,\iota(II)_\mu\bigr)
 =\sum_{\mu,\nu,a}
 g_H^{\mu\mu}g_H^{\nu\nu}g_V^{aa}II_{\mu\nu a}^2. \tag{6}
\]

Matrix form sharpens this to

\[
 \iota^TH_T\iota=H_{II},\qquad
 R=H_{II}^{-1}\iota^TH_T,\qquad
 P^TH_T=H_TP. \tag{7}
\]

Thus the full norm is not merely nonzero on a sample; it is the orthogonal
restriction of the written connection norm to the complete Gauss carrier.

The trace-first rival is

\[
 H_a=\sum_\mu g_H^{\mu\mu}II_{\mu\mu a}.
\]

Its quadratic form has rank ten. Equation (6) has rank 100. Ninety
traceless-`II` directions disappear if one traces first. No convention,
coefficient rescaling or invariant-pairing normalization can turn those ranks
into one another.

## 4. Consequence for the action-norm fork

The source fixes three ingredients:

1. `T` is the full difference of two connections;
2. the action contains `kappa_1 <T,*T>/2` with no trace operation; and
3. the modern connection is measured relative to the gauge-rotated
   Levi-Civita connection.

H21 supplies the remaining Gauss identity in the canonical sector:
the horizontal normal block is the full `II_s`. Equations (3)--(7) now prove
that the written action norms that complete block. Therefore:

```text
P2_norm = DERIVED_FULL_II_ON_CANONICAL_GAUSS_SECTOR
P2_datum = UNCHANGED_UNUSED
```

This is conditional in the ordinary sense of the whole GU build: it uses the
admitted K77 branch, supplied spin structure, source `P_H`, constructed global
Clifford frame and canonical Gauss connection sector. It is not a free
conditional horn inside that construction anymore.

The predecessor's observed TT matrix consequently moves from a hypothetical
full-norm branch to the construction-selected Gauss placement:

\[
 J_{TT}=\begin{pmatrix}\alpha_{II}z&z\\z&\kappa_1\end{pmatrix},
 \qquad
 \det J_{TT}=z(\alpha_{II}\kappa_1-z). \tag{8}
\]

Equation (8) contains one simple massless Einstein pole and the distinct
massive GU partner. It is not yet a final physical propagator because the
common quotient/domain and partner sign remain open.

## 5. The selected invariant stationary branch

For flat `B`, constant `T` and fixed metric/epsilon, the path-average curvature
is

\[
 \bar F=\frac13T^2.
\]

The selected `comm/symi/symi` Shiab gives the exact invariant contractions

\[
 \langle\Phi_1,S(\Phi_1^2)\rangle=4368,
 \qquad
 \langle\Phi_1,*\Phi_1\rangle=14. \tag{9}
\]

The one-third path-average factor converts (9) into (1). This calculation
differentiates the scalar action directly, so the derivative contains both
the direct Shiab row and the Fréchet-adjoint response of `T^2`.

### Full algebraic gradient

Solving only `dI/dt=0` would be insufficient. At `kappa_1=1`, the exact probe
checks every one of the 196 basis directions in
`C* tensor Cl1(C)` and every one of the 196 directions in
`C* tensor Cl13(C)`. All vanish.

At `T=t Phi1`, the derivative is Spin-invariant. In
`C* tensor Cl(C) congruent C* tensor Lambda* C`, invariant lines can only
occur through the identity `C->C` and its Hodge dual `C->Lambda13 C`.
Therefore the two complete basis banks close the full algebraic adjoint
gradient, not merely the ansatz direction.

### Moving epsilon

For an exact bivector generator `chi`, co-move

\[
 \delta T=[T,\chi],\qquad
 \delta\Phi_i=[\Phi_i,\chi].
\]

The cubic and quadratic orbit derivatives both vanish. Hence the family

\[
 T_*^\epsilon=-\frac{\kappa_1}{312}\Phi_1^\epsilon
\]

is gauge-natural. This is covariance of one branch, not a new rule selecting
epsilon.

## 6. The surprising printed-endpoint coincidence

The preregistered expectation was that the source-printed endpoint would be
nonzero at the action stationary branch. It is zero:

\[
 S(T_*^2)+*\kappa_1T_*=0. \tag{10}
\]

Equation (10) is a special invariant-line coincidence. It does not restore
the printed endpoint globally. The predecessor already has an exact
non-cyclic matrix fixture on which

\[
 S(\bar F)+L_T^!S^!T+*\kappa_1T
 \ne S(F_A)+*\kappa_1T.
\]

The correct report is therefore: the branch solves the actual scalar action;
it also happens to lie in the printed rival's zero set. Neither implication
extends to the full field space.

## 7. Stability and physical boundary

Equation (2) makes the first stability statement exact. For positive
`kappa_1`, the nonzero branch is a radial maximum. For another sign, the
ambient Krein pairing is still indefinite, so a one-direction Hessian sign
cannot establish stability.

Still open:

- derivative and connection-background perturbations around `T_*`;
- the complete action-owned degree-14 totalization and current-to-stress map;
- nonlinear constraint propagation and BV/CME;
- a trace-compatible closed physical Krein/Green/BFV domain;
- sign and physical residue of the distinct massive partner;
- stable branch selection and independent vacuum-shift screening;
- FLRW reduction, dark-energy magnitude and held-out observables.

## 8. Constraint surplus and progress

| quantity | result |
| --- | ---: |
| new fields/data/selectors | 0 |
| fitted coefficients | 0 |
| Gauss receiver rank | 100 |
| trace-first rank | 10 |
| full-norm directions retained beyond trace | 90 |
| stationary coefficient choices | 0; `-1/312` derived |
| external P1/P2/P3 consumed | 0 |
| action-norm open forks retired | 1 (`P2_norm`) |
| stable physical vacua proved | 0 |

The norm result has strong surplus: a parameter-free rank-100 map must obey
right-inverse, metric-adjoint, projector, skewness and norm identities; all do.
The stationary result is also overconstrained relative to its zero new
freedom: one derived coefficient passes the radial equation, 392 transverse
basis derivatives and an epsilon-orbit derivative.

## 9. Seven-axis audit

| layer | result | boundary |
| --- | --- | --- |
| Layer 0 | horizontal Gauss map, vertical q-receiver, two P2 names, two Euler rows and two vacuum grades separated | no homonym promotion |
| L1 source | full `T` carrier and unprojected quadratic term confirmed | rank-100 map and `-1/312` are repo-derived |
| L2 algebra | rank-100 receiver/right inverse/projector and 100-vs-10 norm theorem exact | overall invariant normalization remains a coefficient |
| L3 geometry | uses constructed global K77 frame and Gauss connection sector | arbitrary noncanonical connection background not identified with `II` |
| L4 variation | scalar selected action and full algebraic invariant gradient exact | derivative/background variations and totalization open |
| L5 covariance | co-moving epsilon orbit exact | nonlinear BV/CME and epsilon physical selection open |
| L6 analytic | radial Hessian exact | closed common Krein/Green domain and stability open |
| L7 physics | full-norm massless-plus-massive pole structure construction-selected | partner viability, cosmology, magnitude and predictions open |

## 10. Hostile disposition and next gate

The two-sided hostile pass accepts the norm theorem and algebraic branch after
four corrections:

1. it forbids identifying the vertical rank-ten receiver with the Gauss map;
2. it renames the action premise `P2_norm` and external datum `P2_datum`;
3. it restores the one-third path-average coefficient, changing the branch
   from an initial scratch value `-kappa_1/936` to `-kappa_1/312`; and
4. it reports the printed-endpoint coincidence instead of forcing the
   expected negative control.

The next gate is now narrower:

```text
CLOSE_SELECTED_BRANCH_LINEARIZED_TOTALIZATION_STRESS_CURRENT_AND_COMMON_KREIN_GREEN_DOMAIN__THEN_CLASSIFY_MASSIVE_PARTNER_STABILITY_AND_TEST_VACUUM_SHIFT_SCREENING
```

The next wave should linearize the complete action-owned Euler/degree-14
totalization around `T_*`, construct the connection-current-to-Hilbert-stress
chain on that same background, and close one common physical domain. It may
not return to “external datum/source action missing,” spend `P2_datum`, or
replace the distinct partner with pure-GR one-pole-total reflex.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py
DOT_SAGE=/private/tmp/gu-selected-k77-vacuum-p2-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_moving_k77_vacuum_p2_norm_independent.sage
```

Main receipt: `53/53 PASS` (`22 exact + 7 planted + 7 repo + 3 source +
14 type`). Independent Sage reconstruction passes.
