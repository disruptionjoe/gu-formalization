---
title: "RB6: invariant gimmel curvature supplies typed but nonselecting vertical operators; the written source fields admit a formula-complete symmetry-breaking route"
status: "completed exploration; exact typing and invariant-algebra obstruction, conditional ambient numerics, action-field evaluation open"
date: "2026-07-30"
run_id: "GUH-20260731T021900Z-rb6-target-blind-spectral-grammar"
---

# RB6 target-blind spectral grammar

## Result

RB6 changes the source-ownership boundary in both directions.

First, the earlier statement that curvature had no typed adapter to the
native vertical endomorphism bundle was too coarse. On
\[
Y=\operatorname{Met}(X),
\qquad
VY\simeq\pi^*\operatorname{Sym}^2T^*X,
\]
the vertical inclusion and trace-reversed DeWitt metric canonically turn
vertical restrictions of symmetric covariant two-tensors into
DeWitt-self-adjoint endomorphisms. In particular the conditional W177 gimmel
geometry supplies
\[
H_{\rm Ric}=G_V^{-1}\operatorname{Ric}_{VV},
\qquad
H_{R^2}=G_V^{-1}B_{VV},
\qquad
B_{IJ}=R_{IABC}R_J{}^{ABC}.
\]
These are target-blind, type-complete geometric concomitants. Under the
explicit conditional identification
\(A_0=\operatorname{spinlift}(\nabla^{\rm gimmel})\) and the tangent
representation invariant pairing, the all-leg and vertical-only
curvature-square words are also the first evaluable action-owned
Yang--Mills curvature Gram operators, up to invariant-pairing normalization.
They use no observer, flag, chosen four-plane, or Standard Model label.

Second, those invariant concomitants are too symmetric to select the RB4
flag. At the W177 point, and at three independent nearby Lorentzian fibre
points, the evaluated vertical operators lie to finite-difference precision
in the two-dimensional commutative algebra
\[
\operatorname{span}\{I,T_{\rm tr}\},
\]
where \(T_{\rm tr}\) is the canonical trace-reversal involution. The fitted
identities are
\[
H_{\rm Ric}
=-\frac12 I-\frac34T_{\rm tr},
\]
\[
H_{R^2}
=\frac78 I+\frac98T_{\rm tr},
\]
and the vertical-only curvature square is
\[
H_{R_V^2}
=\frac34(I+T_{\rm tr}).
\]
Relative numerical residuals are between approximately \(10^{-8}\) and
\(4.2\times10^{-7}\), including the nearby-point controls.

Consequently the fitted representatives of all target-blind commutators in
this invariant grammar vanish:
\[
[H_{\rm Ric},T_{\rm tr}]
=[H_{\rm Ric},H_{R^2}]
=[T_{\rm tr},H_{R^2}]
=0.
\]
The raw commutator norms are \(3.7\times10^{-7}\) to
\(8.4\times10^{-7}\), below the declared \(2\times10^{-5}\) concomitant
resolution and comparable to the finite-difference floor. Thus no nonzero
source-derived \(Q\) is resolved. Conditional on the declared
isotropy-natural W177 branch, the representation argument in Section 3
places the continuum words exactly in this commuting algebra. The numeric
fit alone does not prove exact zero. No polar complex structure follows.

The sign spectra are equally decisive:

| word | trace-line eigenvalue | traceless eigenvalue | negative rank |
| --- | ---: | ---: | ---: |
| \(I\) | \(1\) | \(1\) | 0 |
| \(T_{\rm tr}\) | \(-1\) | \(1\) | 1 |
| \(H_{\rm Ric}\) | \(1/4\) | \(-5/4\) | 9 |
| \(H_{\rm Ein}=H_{\rm Ric}-\frac12RI\) | \(21/4\) | \(15/4\) | 0 |
| restricted ambient \(H_{\rm Ric}-\frac1{14}RI\) | \(27/28\) | \(-15/28\) | 9 |
| vertical-tracefree \(H_{\rm Ric}-\frac1{10}\operatorname{tr}_V(H_{\rm Ric})I\) | \(27/20\) | \(-3/20\) | 9 |
| \(H_{R^2}\) | \(-1/4\) | \(2\) | 1 |
| \(H_{R_V^2}\) | \(0\) | \(3/2\) | gap closed |

Here the measured scalar curvature is \(R\simeq-10\). No predeclared word
returns rank four. More strongly, the rank-nine negative sector is the
tracefree fibre, whose DeWitt inertia is \((6,3)\), not a negative-definite
four-plane. The invariant zero-order curvature algebra therefore cannot
produce
\[
W_4(u)
=\mathbb Rt\oplus(u^\flat\odot u^\perp).
\]

This does **not** kill the source-action route. It identifies what the source
must do: break the residual Lorentz isotropy with a non-metric field. The
actually written distortion, independent connection, curvature, and section
geometry already admit formula-level target-blind endomorphisms:
\[
B^\theta_{ij}
=\kappa_{\mathfrak g}(\theta_i,\theta_j),
\qquad
H_\theta=G_V^{-1}B^\theta,
\]
\[
B^F_{ij}
=G_V^{k\ell}\kappa_{\mathfrak g}(F_{ik},F_{j\ell}),
\qquad
H_F=G_V^{-1}B^F,
\]
and, after the declared normal--vertical graph identification,
\[
B^{II}_{ij}
=g^{\mu\rho}g^{\nu\sigma}
II_{\mu\nu,i}II_{\rho\sigma,j},
\qquad
H_{II}=G_V^{-1}B^{II}.
\]
Each \(B\) is symmetric, so each \(H\) is DeWitt-self-adjoint. Two
independently generated words then give the exact target-blind
DeWitt-skew candidate
\[
Q_{ab}=[H_a,H_b],
\qquad
Q_{ab}^{\dagger_{G_V}}=-Q_{ab}.
\]

These formulas are action-owned at field/formula grade. Their retained
values, coupled stationary background, normal--vertical identification,
uniform spectral gap, and polar branch are not built. RB6 therefore replaces
`NO-TYPED-H/Q-ADAPTER` with the sharper boundary:

```text
INVARIANT W177 H WORDS:          TYPED / EVALUATED / NONSELECTING
INVARIANT W177 Q WORDS:          NO NONZERO RESOLVED; ISOTROPY FIT COMMUTES
ACTION-FIELD H WORDS:            TYPED AT FORMULA GRADE / UNEVALUATED
ACTION-FIELD COMMUTATOR Q:       TYPED AT FORMULA GRADE / POLAR OPEN
PHYSICAL HESSIAN AT W177:        ALREADY KILLED BY NONSTATIONARITY
SOURCE-DERIVED FLAG:             OPEN AT STATIONARY-ORBIT GATE
```

P1/P2 and P3 remain unchanged. A frozen flag remains a new continuous
external spurion, but it is not yet required: the written source fields now
have an explicit type-correct route by which a dynamical flag could emerge.

## Plain English

The previous swing showed that the old soldering field does not secretly
contain the Standard Model-like flag. It then asked whether the source action
could manufacture the flag from the spectra of operators \(H\) and \(Q\).

This swing found the first honest operators.

Curvature and trace reversal naturally make matrices on the actual
ten-dimensional metric fibre. Nothing had to be inserted by hand to type
them. But they only distinguish “the trace” from “everything traceless.”
They do not distinguish the three mixed time--space directions inside the
traceless nine. All their commutators therefore vanish, so they cannot make
the required complex structure either.

That failure is informative rather than terminal. It says a perfectly
isotropic metric background cannot do the selecting. The source action must
use one of its non-metric fields—its distortion, independent curvature, or
moving-section geometry—as an order parameter. Those fields can be converted
into \(H\) without using the answer, and two such \(H\)'s automatically
produce a correctly skew \(Q\) by commutation.

So the remaining question is no longer whether a typed source route exists.
It is whether the coupled source equations select a stationary noncommuting
pair whose spectrum has the required rank, signature, gap, and polar
properties without tuning those properties in afterward.

## 1. Layer 0

| shared phrase | object used here | distinct object |
| --- | --- | --- |
| ten-dimensional fibre | \(VY=\operatorname{Sym}^2T^*X\) | \(\Lambda^2\oplus\Lambda^3\) exterior ten |
| trace reversal | the DeWitt metric/involution on the symmetric fibre | a selected Cartan four-plane |
| vertical restriction | restriction of covariant slots along the canonical vertical inclusion | a global horizontal projector |
| \(H\) | DeWitt-self-adjoint endomorphism built from a tensor concomitant | a physical fluctuation Hessian |
| \(Q\) | commutator of two independently built self-adjoint words | charge conjugation, Dirac operator, or a supplied \(J\) |
| W177 curvature | gimmel Levi--Civita curvature on a conditional ambient branch | the independent \(X^4\) IG curvature |
| action-owned | constructed from a varied field by a written formula | evaluated on a stationary source solution |
| negative rank | dimension of a sign-projector image | metric inertia, particle multiplicity, index, or generation count |
| stationarity | zero of the declared Euler system | use of a geometrically distinguished background |

The bundle sequence
\[
0\longrightarrow VY\longrightarrow TY\longrightarrow\pi^*TX
\longrightarrow0
\]
is canonical. A global splitting is not. The W177 gimmel/Levi--Civita branch
supplies the horizontal structure used in its ambient computations. The
vertical covariant restrictions above do not require that choice.

The W177 Yang--Mills result applies only after conditionally identifying the
gimmel spin connection with the ambient Yang--Mills connection. It does not
transfer to the independent \(X^4\) IG connection or the full coupled action.

## 2. Frozen grammar and forbidden information

Before reading any spectrum, the executable freezes:

```text
I
T_tr
G_V^-1 Ric_VV
G_V^-1 (Ric_VV - R G_V / 2)
G_V^-1 (Ric_VV - R G_V / 14)
G_V^-1 Ric_VV - tr_V(G_V^-1 Ric_VV) I / 10
G_V^-1 (R_IABC R_J^ABC)_VV
G_V^-1 (vertical-only R_iabc R_j^abc)
all pairwise commutators of the independent H words
```

The zero threshold is frozen at zero with a numerical gap tolerance. The
following are forbidden from candidate construction:

```text
u, P_W, J, Omega_C, epsilon_flag, a chosen 6+4 block,
rank four, selected eigenvectors, target-labelled gamma matrices,
Standard Model labels, hypercharge, P3, index, or count data.
```

Ranks, inertias, and gaps are measured only after these expressions are
named.

The program-native side is load-bearing: actual
\(\operatorname{Sym}^2T^*X\), trace-reversed DeWitt \((6,4)\), and
indefinite adjoints. Raw Frobenius \((7,3)\) and the exterior numerical ten
remain hostile comparators. No negative result obtained here is silently
transferred to the exterior construction.

## 3. Why the invariant algebra collapses

At a Lorentzian metric \(g\), the stabilizer \(O(3,1)\) acts on
\[
\operatorname{Sym}^2T^*X
=\mathbb R g\oplus\operatorname{Sym}^2_0T^*X.
\]
The trace line and tracefree nine are inequivalent multiplicity-one
summands. Any natural zero-order endomorphism built only from the invariant
metric and its homogeneous curvature acts by one scalar on each summand.
Equivalently it lies in
\[
\operatorname{span}\{P_{\rm tr},I-P_{\rm tr}\}
=\operatorname{span}\{I,T_{\rm tr}\}.
\]

Conditional on the curvature word being natural under this point
stabilizer, this explains the stable coefficients measured at the W177
point and nearby points. It supports an exact continuum commutator result on
that branch; the executable itself reports only the finite-resolution
statement.

It also identifies the missing representation. The target four-plane is
\[
\mathbb Rt\oplus(u^\flat\odot u^\perp).
\]
The trace line is invariant, but the additional three-dimensional summand
requires a timelike direction \(u\), or an equivalent anisotropic
order-parameter field. Metric curvature alone cannot choose it while
preserving the full point stabilizer.

## 4. Evaluable W177 candidates

The deterministic W177 point gives:

```text
vertical DeWitt inertia:                 (6,4)
raw Frobenius inertia:                   (7,3)
scalar curvature:                       approximately -10
H_Ric fit residual to span{I,T}:         approximately 4.2e-7
H_R2 fit residual to span{I,T}:          approximately 8.1e-8
raw commutator norms:                    3.7e-7 to 8.4e-7
declared concomitant resolution:         2.0e-5
fitted identity/trace commutators:       exactly zero
```

The nearby-point repetition preserves the same fitted coefficients within
the finite-difference floor. This is evidence for the homogeneous-space
identity, not a global spectral-section theorem.

Canonical shifts make the ambiguity visible. Ricci, Einstein, restricted
ambient-tracefree Ricci, and curvature-square return different sign
projectors with negative ranks \(9,0,9,1\). The vertical-only curvature
square closes the gap on the trace line. None returns rank four, and the
rank-nine sector has the wrong DeWitt inertia.

This is a stronger rejection than “we did not guess the right contraction.”
The entire invariant algebra visible to this grammar has only the trace and
tracefree eigenspaces.

## 5. Formula-complete action-field route

### 5.1 Distortion and retained vertical connection

For
\[
\theta\in\Omega^1(Y,\operatorname{ad}P)
\]
and invariant adjoint pairing \(\kappa_{\mathfrak g}\), restrict the form
coindex vertically and define
\[
B^\theta_{ij}
=\kappa_{\mathfrak g}(\theta_i,\theta_j).
\]
Symmetry of \(\kappa_{\mathfrak g}\) makes \(B^\theta\) a symmetric
covariant vertical two-tensor. Therefore
\[
H_\theta=G_V^{-1}B^\theta
\]
is exactly DeWitt-self-adjoint. The same construction applies to the
retained coefficient \(v=\operatorname{res}^V(A-A_0)\), once its actual
reduction is supplied.

### 5.2 Independent IG curvature

For the vertical--vertical part of the independent connection curvature,
\[
B^F_{ij}
=G_V^{k\ell}\kappa_{\mathfrak g}(F_{ik},F_{j\ell})
\]
is symmetric by antisymmetry of \(F\), symmetry of \(G_V\), and symmetry of
\(\kappa_{\mathfrak g}\). Thus
\[
H_F=G_V^{-1}B^F
\]
is another action-field self-adjoint word. It is not the W177 Ricci
endomorphism and need not commute with \(H_\theta\).

### 5.3 Moving section

After specifying the normal--vertical graph identification for a section
\(s:X\to Y\), let
\[
II_{\mu\nu}{}^i
\]
be its vertical second fundamental form. Contracting the base coindices
gives the symmetric vertical tensor
\[
B^{II}_{ij}
=g^{\mu\rho}g^{\nu\sigma}
II_{\mu\nu,i}II_{\rho\sigma,j},
\]
and hence \(H_{II}=G_V^{-1}B^{II}\).

This construction uses the actual symmetric metric fibre. It does not
identify the section Hessian with a connection-field Hessian or a mass
matrix.

### 5.4 Complex-structure candidate

For any two independently generated self-adjoint words,
\[
Q_{ab}=[H_a,H_b]
\]
satisfies
\[
Q_{ab}^{\dagger_{G_V}}
=[H_b,H_a]
=-Q_{ab}.
\]
This supplies the type RB5 requires without inserting \(J\).

Type is not polar admissibility. A survivor must still have:

- nonzero determinant;
- a real diagonalizable/definitizable branch;
- positive real spectrum for \(-Q^2\);
- a uniform inverse-square-root gap;
- smooth global transport; and
- compatibility with the eventual determinant-volume and fermion lift.

The invariant W177 words fail at the first condition because no nonzero
commutator is resolved and their fitted isotropy representatives commute.
The action-field words are unevaluated.

## 6. Stationarity and Hessian boundary

The July 29 source-owned-reduction packet already evaluated
\[
D_{A_0}^*F_{A_0}
\]
at the deterministic W177 point under the conditional isolated ambient
Yang--Mills branch. RB6 re-runs rather than reimplements that test:

```text
residual norms:
  3.1990493528
  3.1990413676
  3.1990393896

relative spread:                    3.114e-6
signal / numerical-control floor:  858.6
verdict:                            W177-AMBIENT-YM-NONSTATIONARY
```

Therefore no curvature word evaluated at that background is a physical mass
Hessian. The result does not say the full coupled source action is
nonstationary: additional Euler terms could cancel the isolated
Yang--Mills residual, and the \(X^4\) IG connection remains a Layer-0
homonym.

## 7. Constraint-surplus reading

The evaluated invariant grammar has no fitted continuous coefficient. It
faces the independently frozen demands:

- negative spectral rank four;
- negative-definite DeWitt inertia on that image;
- a nonzero uniform gap;
- an invertible admissible \(Q\); and
- a stationary source background.

It fails before any fit.

The action-field grammar is different. The values of
\(\theta,F,II_s\), the stationary orbit, and their reductions are not yet
fixed. Their free-parameter rank and the independent Euler/spectral
constraint rank are therefore unknown:

```text
ACTION-FIELD CONSTRAINT SURPLUS: UNCOMPUTABLE
```

This is not grounds for the orthodox claim that a constructed fit would
teach nothing. The next swing must declare a finite ansatz and its parameter
count before solving the action equations. If the stationary equations and
five-leg constraints leave positive surplus, a successful flag would be
informative even though the ansatz was built to test that possibility.

## 8. Five-leg disposition

| leg | RB6 advance | still open |
| --- | --- | --- |
| SM/Yukawa | exact type route from source fields to \(H_a,Q_{ab}\); invariant metric words cannot select \(W_4\) | stationary flag, complex volume, \(\mathbb Z_6\), hypercharge, fermion/Yukawa placement |
| quantum/Krein/BV | all adjoints use native DeWitt/Krein geometry; composite \(Q\) is exactly skew | polar branch, chain-rule Euler/BV maps, common domain, CME, physical state space |
| gravity/cosmology | trace reversal stays load-bearing; isolated W177 background remains nonstationary | coupled stationary metric/connection/section solution and cosmological value |
| UV/causality | no change to moving Clifford plane or \(g=1\) principal packet | curved subprincipal/common-cone and global reduction |
| P3/index/count | P3 remains a separate relative real-\(KO\) input | common domain/pushforward; no spectral rank is a count |

## 9. Datum and action ledger

| object | RB6 status |
| --- | --- |
| P1/P2 orientation line | unchanged |
| P3 relative real-\(KO\) input | unchanged and separate |
| frozen complex--Cartan flag | still a new continuous external spurion |
| \(H_{\rm Ric},T_{\rm tr}\) | geometry-owned, typed, evaluated, nonselecting |
| all-leg and vertical-only \(H_{R^2}\) | geometry-owned and, under the conditional W177 ambient-YM identification, action-owned curvature Gram words; evaluated and nonselecting |
| \(H_\theta,H_F,H_{II}\) beyond W177 | action-field formula constructed; retained values and stationary orbit unbuilt |
| \(Q=[H_a,H_b]\) | exact skew formula constructed; no nonzero W177 invariant branch resolved; action-field polar branch open |
| physical flag Hessian | ineligible |

No new external datum is accepted in RB6.

## 10. Fired and retained kills

Fired:

1. W177 invariant-curvature ownership of the rank-four Cartan split;
2. a resolved nonzero \(Q\) from the invariant W177 grammar, with exact zero
   additionally supported on the declared isotropy-natural branch;
3. the W177 background as an isolated ambient Yang--Mills stationary point;
4. any mass, count, or Standard Model reading from the displayed spectra;
5. the claim that no type-complete \(H\) adapter exists at all.

Retained:

1. source selection through non-metric distortion/IG-curvature/section
   fields;
2. the conditional RB5 spectral and polar calculus;
3. a refined independently varied flag field;
4. the frozen-flag fallback as explicit continuous external data; and
5. all P1/P2/P3 and five-leg non-regression obligations.

## 11. Next highest-information construction

RB7 should build the smallest stationary non-metric order-parameter ansatz,
not enumerate more invariant curvature contractions:

1. Write \(H_\theta,H_F,H_{II}\) directly into the N3 field/action ledger,
   including every vertical restriction, adjoint pairing, coefficient, and
   chain-rule derivative.
2. Freeze a finite symmetry-breaking ansatz for
   \((\theta,F,II_s)\) without \(u,P_W,J\), a chosen rank, or target-labelled
   basis elements. Declare its free-parameter count first.
3. Derive the coupled connection/distortion/section Euler equations and
   solve for stationary orbits capable of cancelling the W177 residual.
4. Only on those orbits, measure the spectra and inertias of the predeclared
   \(H_a\), and test every \(Q_{ab}\) for invertibility and the positive-real
   polar branch.
5. Compare equally natural contractions and compute the actual constraint
   surplus.
6. If one orbit survives uniquely or with finite residual data, propagate
   the composite derivatives into the full BV equations and run the global
   complex-volume, Yukawa, gravity/cosmology, causality, and P3 gates.

The decisive next question is:

```text
DO THE WRITTEN SOURCE EQUATIONS SELECT A NONCOMMUTING STATIONARY
DISTORTION/CURVATURE/SECTION ORBIT, OR MUST THE FLAG BE SUPPLIED?
```

## Validation

The RB6 executable passes all 29 predeclared, type, spectral, covariance,
polar, hostile, and stationarity controls. The validation sweep also passes:

```text
RB5 conditional spectral/polar calculus and Hessian classifier
RB4 moving observer/Cartan geometry
RB3b trace-reversed full-20 join
N3 unified source variation
unified source/datum packet
vertical source-action reduction
W177 stationarity
W246 self-adjointization ambiguity
VG-V3 J commutant
W240 and W243 compactification corridors
root test inventory
Python compilation
diff hygiene
```

The executable is
[`tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py`](../tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py).

## Nonclaims

RB6 does not construct a stationary solution, source-derived flag, physical
compactification, Standard Model group, determinant volume, Yukawa sector,
VEV, mass, cosmological prediction, anomaly cancellation, CME solution,
common analytic domain, index, generation, or count.
