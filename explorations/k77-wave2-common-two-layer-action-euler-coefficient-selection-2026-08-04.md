---
title: "K77 Wave 2: the common norm-square layer is built, but its redundancy cannot select the trace-q coefficient"
status: active_research
doc_type: construction_result
created: 2026-08-04
gate: RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD
grade: "Field-theoretic two-layer formula with exact finite variational control; exact actual-K77 principal-family, cancellation-rank, all-covector anticommutator-scalarity, and quadratic-square-span certificates. Full moving K77 Euler evaluation, path adapter, independent second-layer target, observation, and physics remain open."
canon_verdict_change: none
---

# K77 Wave 2: common two-layer action and coefficient selection

## Result first

The source-guided two-layer action is now written in one typed formula and its
variational logic is exact. It does **not** select the remaining trace-`q`
coefficient by itself.

Let `c=(alpha,beta)` and let the first-layer Einstein--Dirac candidate be

\[
 S_1[c;\Phi],\qquad
 \Upsilon_c=\frac{\delta S_1}{\delta\Phi}.
\]

The source's norm-square second layer gives the common action

\[
 S_{\rm 2L}[c;\Phi]
 =S_1[c;\Phi]
 +\frac{\kappa_2}{2}
   \langle\Upsilon_c,G_\Phi^{-1}\Upsilon_c\rangle.
\]

At fixed pairing its field Euler operator is

\[
 E_\Phi S_{\rm 2L}
 =\Upsilon_c
 +\kappa_2 H_c^!G^{-1}\Upsilon_c,
 \qquad H_c=D_\Phi\Upsilon_c.
\]

A moving Hodge/Krein/density pairing adds the separately owned term

\[
 \frac{\kappa_2}{2}
 (D_\Phi G^{-1})^!(\Upsilon_c,\Upsilon_c).
\]

Consequently every first-layer solution `Upsilon_c=0` is automatically a
two-layer solution for every value of `c`. That is not a defect invented by
the reconstruction; Weinstein explicitly says the second-order equations are
redundant on the first-order equations. It means the norm-square layer cannot
spend a coupling freedom on the first-order solution locus.

The actual K77 calculation sharpens what remains:

- `gamma(q)A` and `A gamma(q)` have exact rank two, so no nonzero projective
  combination cancels the entire middle principal arrow;
- their anticommutator is scalar on spinors for a basis of all fourteen
  covectors and therefore for every covector;
- their commutator contains non-scalar even Clifford content; and
- the self-derived square
  `D(alpha,beta)^times D(alpha,beta)` has three independent quadratic
  coefficient tensors.

The scalar anticommutator is a serious Laplace-type lead. It is not yet a
selection theorem because the released source does not identify the K77
left/right placements with the spoken up-over/over-up paths or supply the
independent second-layer target to which the three quadratic tensors must be
matched.

Exact certificate:

```text
8 source + 22 type + 14 exact + 7 planted = 51 PASS
```

The honest frontier is therefore no longer “write a source action.” The common
two-layer formula exists. The next missing object is the **actual two-complex
path adapter and independent square-root target**.

## Plain English

Eric's “square” has two very different possible meanings.

The first is straightforward: write the first equations, square their size,
and add that as another action term. We have now done that carefully. It makes
a legitimate second-order theory, and it generates extra field equations, but
it cannot choose between the remaining operator coefficients because any
solution of the original equations already makes the squared term vanish.

The second meaning is stronger: two different paths through the geometry
should compose to the same independently defined higher-order object, with
bad derivative pieces canceling. That kind of square-root identity really
could choose a coefficient. Eric points directly at it when he talks about
up-and-back versus up-and-over and over-and-up. But he also says that this was
unfinished. The repository had not yet separated these two meanings of
“square.” It now does.

This is progress because it stops us from repeatedly asking a redundant
norm-square to do a selector's job. It also identifies the exact construction
that might do the job: build both paths, compose them, and compare the result
to the three-coordinate K77 quadratic square family.

## 0. Layer 0

| phrase | object used here | object kept distinct |
| --- | --- | --- |
| first layer | `S_1`, the action candidate | `Upsilon=delta S_1`, its Euler residual |
| second layer | norm square of `Upsilon` | an independently postulated ordinary SM Yang--Mills--Higgs action |
| square | residual norm, operator composition, or deformation-differential square | amplitudes double copy or numerical squaring |
| coefficient selection | an equation involving only `alpha:beta`, owned by the geometry | field equations whose form merely depends on the coupling |
| coupling | fixed structural parameter in the action | a new modulus added to the field/BV complex |
| Higgs/Yukawa | vertical connection and curvature-norm support upstairs | observed `SU(2)` doublet, `Lambda^0` mass channel, VEV, masses, and family matrices |
| cancellation | actual equality/composition of two paths | naming `gamma(q)A` and `A gamma(q)` “over” and “up” without a map |

The construction uses the program-native indefinite/Krein pairing and
trace-reversed metric fibre. It does not replace them by a positive Hilbert
norm. The ordinary Standard Model action remains a downstream comparison
target rather than an imported definition.

## 1. Source collision

The paired source receipt is
[`gu-two-layer-action-source-reinspection-2026-08-04.md`](../lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md).

The load-bearing dispositions are:

```text
SOURCE-CONFIRMS:
  first Einstein--Dirac layer;
  second norm-square layer;
  second-order redundancy on first-order solutions;
  curvature-norm quadratic/quartic Higgs-like grammar;
  unfinished up/back/over cancellation burden

SOURCE-CORRECTS:
  Curt's one-layer minimal-coupling presentation

SOURCE-SILENT:
  exact K77 alpha:beta coefficient;
  coefficient as a dynamical modulus;
  K77 left/right placements as the spoken paths;
  independent K77 second-layer target;
  physical Higgs/Yukawa reduction
```

Curt remains valuable here: his Iceberg walk-through locates the zero-order
connection term in the fermionic operator. Weinstein's later answer determines
that this locator must be embedded in a separate second-layer architecture.

## 2. Inline divergent specialist pre-assessment

| lens | efficient charge | disposition |
| --- | --- | --- |
| primary-source professor | separate stated architecture from missing formula | three rival readings retained |
| differential geometry | use one moving connection/distortion owner | no duplicate field or bridge |
| variational bicomplex | differentiate the written norm-square | exact chain-rule formula |
| Krein/operator theory | retain indefinite pairing and moving-pairing term | no positivity/domain claim |
| gauge/Higgs engineering | expand curvature support without naming a physical Higgs | construction target only |
| fermion/Yukawa | keep upstairs zero-order coupling distinct from observed scalar channel | adapter remains open |
| representation theory | compute quadratic tensor span before matching | exact rank three |
| symplectic/BV | do not vary a coupling without a modulus owner | optional rival only |
| exact computation | use exact ranks and exact five-point polynomial derivatives | 51 checks, seven plants |
| science council | prefer the missing independent target over a fitted coefficient | next gate retyped |

## 3. The common action and actual Euler derivative

Take the already frozen first-layer architecture schematically as

\[
\begin{aligned}
S_1[c;\Phi]={}&I^B_{\rm act}[B(\epsilon),T,\mathscr S_\epsilon]
+S_F[D_c(A_\epsilon,q),\bar\chi,\chi]\\
&+I_{\rm defects}+I_{|II|^2}+S_{\rm BV,even},\\
D_c={}&D_0+\alpha\,\gamma(q)A+\beta\,A\gamma(q).
\end{aligned}
\]

`q=g/2` remains a composite of the metric fibre, so its variation is routed
back into the metric/soldering Euler row. `A_epsilon=B(epsilon)+T` remains one
connection owner. The fermion current is emitted once by `S_F`; the second
layer differentiates that same residual and does not add a separate
`-<T,J>` bridge.

For moving pairing `G_Phi`, the complete formal field derivative is

\[
\begin{aligned}
E_\Phi S_{\rm 2L}
={}&\Upsilon_c
+\kappa_2 H_c^!G_\Phi^{-1}\Upsilon_c\\
&+\frac{\kappa_2}{2}
(D_\Phi G_\Phi^{-1})^!(\Upsilon_c,\Upsilon_c).
\end{aligned}
\]

The finite exact action control includes one shared connection, two fermionic
components, independent barred variables, an indefinite pairing, and the
complete Hessian. A five-point exact derivative, valid for the quartic action,
agrees coefficientwise with `Upsilon+H^!G Upsilon`. Omitting the Hessian term
is a planted failure.

This does not claim that every moving K77 field coefficient has now been
expanded. It certifies the variational architecture those coefficients must
obey and prevents the source's printed residual from being substituted for
the derivative of the written two-layer action.

## 4. Why fixed-coupling field equations do not select a coupling

In the source-faithful field list, `alpha` and `beta` are coefficients, not
fields. Therefore the Euler complex contains rows for the geometry, connection,
fermions, section, and ghosts/backgrounds, but no `E_alpha` or `E_beta` row.
The field equations depend on `c`; dependence is sensitivity, not selection.

More strongly, on `Upsilon_c=0`, every term supplied by differentiating the
norm square vanishes. Thus the source's redundancy statement is an exact
factorization:

\[
\Upsilon_c=0\quad\Longrightarrow\quad
E_\Phi S_{\rm 2L}=0
\]

for every `c`, including the moving-pairing contribution. The second layer can
add other critical points, but it cannot distinguish coefficients on the
first-order solution locus merely by being present.

## 5. Optional coefficient-modulus rival

One can enlarge the theory by declaring the ratio `r=alpha/beta` a field or
global modulus and varying it. This is a legitimate rival, not source
faithfulness.

The exact control fixes `beta=1` and computes `partial_r S_2L=0` on two
independent held-out field configurations. The roots are

\[
r_A=\frac{173}{13},\qquad r_B=\frac1{38}.
\]

Their disagreement is the intended discriminator. It does not prove that no
more elaborate modulus potential can select `r`; it proves that stationarity
of the present two-layer action is field-dependent rather than a universal
geometry-owned coefficient. A modulus route now owes its own field-space,
kinetic/potential, symmetry, BV, and datum invoice.

## 6. Actual K77 square and cancellation alternatives

Let

\[
L(\xi)=\gamma(q)A(\xi),\qquad
R(\xi)=A(\xi)\gamma(q).
\]

### 6.1 Literal middle-arrow cancellation

The two-column system `(L,R)` has exact rank two on the held-out non-null
covector. Therefore

\[
\alpha L+\beta R=0
\]

has only the zero coefficient. The source's up-over/over-up cancellation
cannot be identified with literal cancellation of this single middle arrow.

### 6.2 Laplace-type lead

For every covector, exact Clifford algebra gives

\[
L+R=\{\gamma(q),A\}
\]

scalar on the spinor factor, while `L-R` contains non-scalar even Clifford
content. This makes `alpha=beta` a genuine candidate for a Laplace-type
square-root condition. It is not promoted because Laplace type constrains the
**composed full operator**, not one middle symbol in isolation.

### 6.3 Self-derived square

The composed family is

\[
D_c^\times D_c
=\alpha^2 L^\times L
+\alpha\beta(L^\times R+R^\times L)
+\beta^2R^\times R.
\]

Applying these three tensors to one exact dense K77 field yields rank three.
Since an evaluation of operators cannot increase rank, this proves the three
operator tensors themselves are independent on the tested principal family.
But this entire quadratic family is self-derived: each `c` produces its own
square. Selection requires an independent target

\[
K_{\rm 2L}^{\rm native}
=D_c^\times D_c
\]

whose three coordinates, path identities, or equivalent invariant conditions
are constructed without using `c` to define the target.

## 7. Constraint surplus and construction disposition

| item | independent coefficient constraints |
| --- | ---: |
| bosonic residual norm | 0 |
| total residual norm at fixed coupling | 0 |
| self-derived Dirac square | 0 |
| optional modulus stationarity | 0 universal; field-dependent roots only |
| source-owned path/target match | unbuilt |

The invoice remains

\[
\text{surplus}=0-1=-1.
\]

This is not a return to “we need a source action.” The action architecture is
written and its non-selection mechanism is understood. The missing object is
strictly smaller:

```text
the actual up/back/over path maps
+ their independent second-layer composition target
+ the identification, if any, with the K77 trace-q family
```

P1/P2/P3 are not used. No new external datum is proposed.

## 8. Source-action specification consequences

- `SA-G9`: the shared-connection action architecture remains compatible with
  one matter current, but the full observed matter-coupled linearization is
  not claimed.
- `SA-Y1`: an upstairs zero-order connection term is present, but the observed
  `Lambda^0` scalar-channel adapter remains open.
- `SA-Y8`: no Majorana scalar or fixed locus is inserted.
- `SA-C2/SA-U4`: predecessor construction terms remain carried; this gate does
  not re-adjudicate them.
- Higgs potential: curvature-norm quadratic/quartic support is a construction
  directive, not yet a vacuum, mass, or observed potential.

No row class moves merely because the common formula has been written.

## 9. Held-out boundary

This result does not construct or claim:

- the complete moving K77 Hessian/Green/preboundary evaluation;
- the actual two-complex path maps or independent target;
- the observed Standard Model gauge/Higgs/Yukawa action;
- a Higgs doublet, VEV, mass, Yukawa matrix, particle, pole, or scattering law;
- observation/quotient, analytic domain, positivity, or BFV phase space;
- physical chirality, anomaly cancellation, family index, or count;
- P1/P2/P3 consumption; or
- Wave 3 admission.

## 10. Next gate

```text
K77_TWO_LAYER_UP_OVER_PATH_ADAPTER_AND_INDEPENDENT_SQUARE_ROOT_TARGET
```

Use the draft deformation diagrams and Portal's `02:03:07` description to
type the two complexes' actual up, back, and over maps. Compose both routes on
the same moving K77 bundle, compute their principal and zero-order difference,
and derive an independent second-layer target from the bosonic
Shiab/curvature residual. Only then compare that target with the rank-three
`(alpha^2,alpha beta,beta^2)` square family. If the target match has projective
rank one, the coefficient closes; if rank zero, the family survives; if
inconsistent, revise the path/operator construction rather than declaring the
whole carrier dead. Wave 3 remains closed.
