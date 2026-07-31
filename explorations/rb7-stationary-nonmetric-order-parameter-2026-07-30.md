---
title: "RB7: trace reversal completes a non-abelian triplet to a Cartan four-plane, but the written finite sector makes it an unstable saddle"
status: "completed exploration; exact finite stationary classification and W177 tensor-response kill"
date: "2026-07-30"
run_id: "GUH-20260731T033558Z-rb7-stationary-nonmetric-order-parameter"
probe: "tests/channel-swings/rb7_stationary_nonmetric_order_parameter_probe.py"
grade: "EXACT GENERIC FINITE TRUNCATION / CONTROLLED LOCAL NUMERICS. For generic nonzero coefficients, the full anisotropic homogeneous Euler system, stationary branches, Hessians, Gram words, Cartan inertia, and raw-Frobenius control are exact; degenerate coefficient cases are stated separately. The W177 residual tensor, mixed Gram, and support-incidence counterexample are finite numerical controls. No full coupled stationary solution, stable order parameter, complex flag, physical Hessian, mass, vacuum, cosmological value, anomaly, index, or count is claimed."
---

# RB7 stationary non-metric order parameter

## Result

RB7 finds the first source-action-shaped route that reaches the right
**Cartan support**, and then finds exactly why the current written terms do
not yet make it physical.

The trace-reversed fibre splits as
\[
V=\mathbb Rt\oplus V_0,
\qquad
\operatorname{sig}(V)=(6,4),
\qquad
\operatorname{sig}(V_0)=(6,3),
\]
with the trace line \(t\) negative. The smallest compact non-abelian
homogeneous connection, an \(\mathfrak{su}(2)\) triplet supported on a
negative three-plane \(E\subset V_0\), has nonzero stationary points in the
finite Yang--Mills-plus-quadratic-distortion action. At the isotropic
stationary point,
\[
\mathbb Rt\oplus E
\]
is a genuine maximal negative four-plane. The raw Frobenius comparator makes
the same trace line positive, so the corresponding four-plane has inertia
\((1,3)\), not \((0,4)\). Trace reversal is therefore exactly load-bearing
for the \(3+1\) Cartan completion.

But the nonzero point is a saddle, not a stable order parameter. For
\(\alpha,m^2>0\) on the negative support, its anisotropic Hessian has
eigenvalues
\[
\{-m^2,-m^2,2m^2\}.
\]
The two negative modes change the three singular values and are not gauge.
More strongly, a commuting one-component field has zero Yang--Mills quartic
term while its negative quadratic term runs to \(-\infty\). Every generic
nonzero stationary branch of this truncation is unstable.

The emitted endomorphisms also stop one step short:
\[
H_\theta=-r^2P_E,
\qquad
H_F=2r^4P_E
\]
at the isotropic negative triplet. They commute exactly, so
\[
Q=[H_\theta,H_F]=0
\]
and no polar complex structure can be formed. \(H_\theta\) also has a
seven-dimensional zero sector. It carries the triplet through
\(\operatorname{im}\Phi\), but does not satisfy RB5's robust zero-gap
spectral-ownership gate.

The attempt to use the actual W177 Yang--Mills Euler covector as a first
target-blind connection descent fails earlier. The complete residual is
stable,
\[
\|E_{\rm YM}\|=3.19904137
\]
in the historical deterministic frame, but its vertical connection-form
component has central auxiliary norm only
\[
0.00361491
\]
against a direct-divergence/Codazzi discrepancy
\[
0.00372577.
\]
Its signal-to-floor ratio is \(0.9702\), and its norm changes from
\(0.00823939\) to \(0.00166594\) across the frozen derivative scales. It is
numerical-floor structure, not an admissible source response.

The stable residual lives instead in the base-form/mixed-adjoint block. A
target-blind mixed Gram preserves that signal but evaluates to
\[
H_{\rm mix}
\simeq
0.28125(I+T_{\rm tr})
=0.5625P_{\rm traceless}
\]
with relative fit residual \(4.13\times10^{-7}\). It is another stable
\(1+9\) nonselector and resolves no nonzero commutator above the declared
floor.

The combined RB7 boundary is:

```text
W177 VERTICAL EULER RESPONSE:      KILLED ON FUNDAMENTAL-YM SLICE BELOW FLOOR
W177 STABLE MIXED GRAM:            TYPED CONDITIONALLY / 1+9 NONSELECTING
HOMOGENEOUS SU(2) CRITICAL POINT:  EXACT / NONZERO / SADDLE
TRACE + NEGATIVE TRIPLET:          EXACT MAXIMAL NEGATIVE FOUR-PLANE
RAW-FROBENIUS COMPARATOR:          (1,3), NOT CARTAN-NEGATIVE
H_theta/H_F ON THE TRIPLET:        EXACT / COMMUTING / ZERO-SECTOR; GAP CLOSED
Q POLAR OWNER:                     FAILS, Q=0
BASE-INDUCED RB4 INCIDENCE:        NOT SELECTED; CODIMENSION-15 SUBLOCUS
STABLE SOURCE-DERIVED FLAG:        OPEN
```

No new external datum is accepted. P1/P2/P3 remain unchanged.

## Plain English

This swing found a real reason the trace reversal matters beyond signature
bookkeeping.

The simplest non-abelian connection can occupy three negative directions in
the traceless part of the metric fibre. Trace reversal supplies one more
negative direction, the trace itself. Together they make exactly the
negative four-dimensional space that the later Pati--Salam/Cartan
construction wants. Without trace reversal, the trace has the wrong sign and
the four-dimensional space fails.

That is genuine progress: the desired four-plane can now arise from a very
small source-shaped field pattern rather than being inserted as a projector.

The current finite action does not hold it there. The Yang--Mills quartic
only penalizes noncommuting fields. A field can escape along a commuting
direction, where that quartic disappears, while the indefinite quadratic
term keeps decreasing. The attractive-looking symmetric triplet is
therefore a mountain pass: stable in the radial direction, unstable in two
shape directions.

The same symmetry also explains why the complex structure does not appear.
Both matrices emitted by the triplet only see “inside the triplet” versus
“outside it.” They are diagonal in the same split, so their commutator is
zero.

The next move is consequently not to add a hand-chosen Mexican-hat
potential. The unreduced source curvature already contains terms that the
homogeneous truncation dropped:
\[
F^0,\quad D^0\Phi,\quad\text{and}\quad -C\Phi.
\]
Those terms can remain nonzero even along a commuting field and can therefore
lift the runaway using geometry already present in the action. They must be
tested together with the parent \(P_{\rm IG},D_AU\) sector and the moving
section \(II_s\). That is the next highest-information construction.

## 1. Layer 0

| phrase | RB7 object | distinct object |
| --- | --- | --- |
| vertical fibre | \(V=\operatorname{Sym}^2T^*X\) with DeWitt \((6,4)\) | the exterior numerical ten |
| W177 Euler residual | the conditional ambient-YM Ricci--Codazzi tensor | the matter/record current \(J\) |
| first descent | a fixed-\(U,\epsilon_{\rm IG}\) \(A\)-correction | a solved nonlinear stationary distortion |
| stationary | a critical point of the frozen homogeneous matrix action | a solution of the full \(A,U,\epsilon,s,P,Z,G,\) BV system |
| negative triplet | the support of \(\Phi:V\to\mathfrak{su}(2)\) | three generations or a supplied observer |
| Cartan support | \(\mathbb Rt\oplus E\), a negative four-plane | a complex structure or physical compactification |
| \(H_\theta,H_F\) | composite Gram endomorphisms | a mass/physical fluctuation Hessian |
| \(Q\) | \([H_\theta,H_F]\) | charge conjugation, Dirac operator, or a supplied \(J\) |
| orbit dimension | a field-support degeneracy | an index, family number, or external-datum count |

On the isolated source-free, parent-free, fundamental-Yang--Mills plus
quadratic-distortion slice with fixed \(U,\epsilon_{\rm IG}\),
\[
\delta A
=-\kappa\frac{\zeta_F}{g_A^2}
\mathcal R_{G,\kappa_{\mathfrak g}}(D_A^!F_A)
\]
is the first connection descent only when the reference also satisfies
\(A_0=\Gamma(\epsilon_{\rm IG})+U\), hence \(\theta_0=0\). Otherwise the
formula is an algebraic target for \(\theta\), not a connection increment.
Calling it \(\delta\theta\) is allowed only on that frozen reference slice.
If \(\theta\) is W203's independent Gaussian auxiliary field, its source is
\(J\), not the W177 residual. The N1 \(U\)-equation schematically contains
\[
-\kappa^{-1}\theta+J+D_A^!P_{\rm IG}+\cdots=0;
\]
it forces \(\theta=0\) only on the same source-free, parent-free slice.
Track A does not include the bridge/current, full-20 curvature-current,
defect, or other parent terms of the complete \(A\)-equation.

The W177 component norms below are deterministic orthonormal-frame auxiliary
norms in indefinite signature. They are used for scale/floor controls, not
promoted to positive invariant energies.

## 2. Track A: the actual W177 response

The represented Yang--Mills covector is
\[
E_{MJ,L}
=\nabla_M\operatorname{Ric}_{LJ}
-\nabla_J\operatorname{Ric}_{LM},
\qquad
E_{MJ,L}=-E_{JM,L}.
\]
The antisymmetric pair \(M,J\) is the tangent-representation adjoint slot.
The last index \(L\) is the connection one-form coindex.

The declared response restricts \(L\) vertically:
\[
e_{MN i}=E_{MN,L}\iota_i{}^L,
\qquad
X_i{}^M{}_N=G^{MP}e_{PNi}.
\]
With the vector-representation convention
\[
\kappa_{\mathfrak g}(X,Y)
=-\frac12\operatorname{tr}(XY),
\]
the upper- and lower-index Riesz descriptions agree:
\[
\Theta^i=-c(G_V)^{ij}X_j,
\qquad
\Theta_i=G^V_{ij}\Theta^j=-cX_i.
\]
The scale \(c=\kappa\zeta_F/g_A^2\) would give the exact scaling laws
\[
H_\theta\mapsto c^2H_\theta,
\qquad
H_F\mapsto c^4H_F,
\qquad
Q\mapsto c^6Q.
\]
No eigenspace may therefore be obtained by fitting its magnitude.

### 2.1 The restricted signal fails

| quantity | scale 0.75 | scale 1.00 | scale 1.25 |
| --- | ---: | ---: | ---: |
| full historical-frame residual | 3.19904935 | 3.19904137 | 3.19903939 |
| vertical-form residual | 0.00823939 | 0.00361491 | 0.00166594 |
| vertical direct/Codazzi discrepancy | 0.00865502 | 0.00372577 | 0.00179771 |

At the central scale:

```text
vertical signal/floor:             0.9702446
vertical relative scale spread:    1.81843
vertical/full residual ratio:      0.00113
```

The gate is therefore killed before \(H_\theta,H_F,Q\) spectra are read.
The fact that the full residual is stable does not rescue a component that
the proposed adapter does not retain.

### 2.2 Signal-preserving mixed comparator

The stable signal has a base form coindex and a mixed base--vertical adjoint
pair. Define conditionally
\[
T_{aib}=E_{a i,b}
\]
and
\[
B^{\rm mix}_{ij}
=g^{aa'}g^{bb'}T_{aib}T_{a'jb'},
\qquad
H_{\rm mix}=G_V^{-1}B^{\rm mix}.
\]
This adapter is target-blind but is not the vertical connection response
that Track A sought.

It is stable:

```text
mixed block norm:                  2.26206240
mixed/full relation:               sqrt(2) * mixed = full
fit coefficients:                  0.28125001 I + 0.28125005 T_tr
relative fit residual:             4.1281e-7
trace commutator norm:             5.1220e-7 < 2e-5 resolution
```

Thus preserving the signal returns the traceless projector rather than a
triplet.

## 3. Track B: exact homogeneous stationary classification

On the fundamental-Yang--Mills branch \(\zeta_F=1\), freeze the base,
\(U,\epsilon_{\rm IG}\), section, parent, and derivatives. With
\[
F=\frac12F_{ij}e^i\wedge e^j,
\]
write
\[
m^2=\kappa^{-1},
\qquad
\alpha=\zeta_Fg_A^{-2},
\]
up to the declared invariant-pairing convention. W203 conditionally pins
\(\kappa>0\) on the accepted C-positive record sector and leaves its
magnitude normalization-owned. The fundamental-YM sign, \(g_A^{-2}\), and
the native adjoint-pairing restriction remain charged forks. The negative-
support branch is therefore conditional on that C-positive gate and the
fundamental-YM sign branch.

Let \(E_\sigma\subset V_0\) be a definite three-plane of sign
\(\sigma=\pm1\), and let
\[
\Phi_i=r_a e_i{}^aT_a,
\qquad
[T_a,T_b]=\epsilon_{ab}{}^cT_c.
\]
The complete anisotropic potential is
\[
V(r_1,r_2,r_3)
=\frac{\mu}{2}\sum_ar_a^2
+\frac{\alpha}{2}
\left(
r_1^2r_2^2+r_2^2r_3^2+r_3^2r_1^2
\right),
\qquad
\mu=\sigma m^2.
\]
Its Euler equations are
\[
E_a
=r_a\left[\mu+\alpha(r_b^2+r_c^2)\right]=0.
\]

For \(\alpha\mu\ne0\):

- the origin always exists;
- if \(\alpha\mu>0\), no nonzero branch exists;
- if \(\alpha\mu<0\), three rank-two branches exist with
  \[
  r_a^2=r_b^2=-\frac{\mu}{\alpha},
  \qquad r_c=0;
  \]
- one full triplet magnitude exists with
  \[
  r_1^2=r_2^2=r_3^2=-\frac{\mu}{2\alpha}.
  \]

The action values are
\[
V_{\rm rank\,2}=-\frac{\mu^2}{2\alpha},
\qquad
V_{\rm rank\,3}=-\frac{3\mu^2}{8\alpha}.
\]

Their Hessian spectra are
\[
\operatorname{spec}\mathcal H_{\rm rank\,3}
=\{-2\mu,\mu,\mu\},
\]
\[
\operatorname{spec}\mathcal H_{\rm rank\,2}
=\{2\mu,-2\mu,-\mu\}.
\]
Every nonzero generic branch is a saddle. When
\(\alpha,m^2>0,\sigma=-1\), the full triplet spectrum is
\[
\{-m^2,-m^2,2m^2\}.
\]

The boundedness classification is even sharper:

- if \(\mu<0\), commuting fields give
  \(V(R,0,0)=\mu R^2/2\to-\infty\);
- if \(\alpha<0\), noncommuting large fields make the quartic run to
  \(-\infty\);
- if \(\mu,\alpha\ge0\), no strictly stabilized or selected nonzero triplet
  exists.

The degenerate \(\mu=0,\alpha>0\) branch has flat abelian coordinate-axis
minima, not a triplet.

For completeness:

- if \(\mu=0,\alpha<0\), the coordinate axes remain stationary but have
  transverse negative modes;
- if \(\alpha=0,\mu\ne0\), only the origin is stationary; and
- if \(\alpha=\mu=0\), every configuration is flat, so nonzero triplets are
  not strictly stabilized or selected.

## 4. What trace reversal really buys

At the negative isotropic triplet:
\[
H_\theta=-r^2P_E,
\qquad
H_F=2r^4P_E,
\qquad
[H_\theta,H_F]=0.
\]

The trace line is DeWitt-negative and orthogonal to
\(E\subset V_0\), so
\[
\operatorname{sig}\left(
G_V\big|_{\mathbb Rt\oplus E}
\right)
=(0,4).
\]
This is an honest maximal negative four-plane.

Under raw Frobenius:
\[
\operatorname{sig}\left(
G_{\rm raw}\big|_{\mathbb Rt\oplus E}
\right)
=(1,3).
\]
Thus trace reversal supplies exactly the missing negative line. It does not
supply stability, a base observer, or \(J\).

## 5. Support incidence and remaining continuous structure

All maximal negative triplets in \(V_0\) lie in one orbit
\[
\operatorname{Gr}_3^-(V_0)
=O(6,3)/(O(6)\times O(3)),
\qquad
\dim=18.
\]
The RB4 base-induced map
\[
[u]\longmapsto u^\flat\odot u^\perp
\]
has a three-dimensional image. Assuming the already-tested immersion, it is
a codimension-fifteen incidence submanifold inside the same orthogonal-group
orbit, not a second orbit class.

The executable plants:

- an RB4 mixed triplet, for which every tensor has rank at most two; and
- a generic negative triplet in the same \(O(6,3)\) orbit, containing a
  tensor with normalized determinant \(0.00814506\).

The generic triplet therefore fails a necessary base-induced incidence
condition. The current finite action is invariant across the full
eighteen-dimensional support orbit and does not select the RB4 sublocus.
The number fifteen is an incidence codimension, not a physical datum count
before the full gauge/source quotient.

## 6. Constraint surplus

The frozen isotropic finite fit has:

```text
radial amplitude before stationarity:             1
independent radial stationarity equation:          1
new fitted coefficients:                           0
carried coefficient ratio m^2/alpha:               1
conditional frozen-ratio equation/amplitude balance: 0
radial surplus if m^2/alpha remains adjustable:      -1
negative-triplet support orbit dimension:         18
RB4 base-induced image dimension:                  3
base-incidence codimension:                       15
```

The zero balance is conditional on freezing the carried
\(m^2/\alpha\) ratio. Because that ratio remains program-unfixed on this
branch, treating it as adjustable gives one equation minus two free
coordinates, hence surplus \(-1\). The radial count alone would misleadingly
call the fit exact. The full
anisotropic equations add two independent shape directions and make the
point a saddle. The polar constraint then fails because \(Q=0\), and the
support-incidence constraint is not selected.

There is therefore no successful full-fit surplus to report. The failure is
not “shaped to fit teaches nothing”; it is a computed failure under surplus:
the proposed point clears radial stationarity and Cartan inertia but fails
anisotropic stability, spectral gap, polar invertibility, and base incidence.

## 7. Five-leg disposition

| leg | RB7 advance | still open |
| --- | --- | --- |
| SM/Yukawa | first source-shaped trace-plus-triplet Cartan support; trace reversal shown load-bearing | stable/base-induced support, \(J\), complex volume, \(\mathbb Z_6\), hypercharge, zero-order Yukawa placement |
| quantum/Krein/BV | exact indefinite Gram adjoints and exact \(Q=0\) polar kill; anisotropic instability exposed | stable stationary background, nonzero polar owner, chain-rule BV complex, CME, common domain, physical state space |
| gravity/cosmology | actual W177 Euler tensor decomposed; vertical descent killed at its own floor | coupled moving metric/connection/section solution and cosmological value |
| UV/causality | no frozen projector or positive-Hilbert replacement introduced | curved subprincipal/common-cone and global reduction |
| P3/index/count | triplet and four-plane explicitly fire no count inference | P3 domain/pushforward remains separate and unchanged |

## 8. Action and datum ledger

| object | RB7 status |
| --- | --- |
| P1/P2 orientation line | unchanged |
| P3 relative real-\(KO\) input | unchanged and separate |
| frozen complex--Cartan flag | still an unaccepted continuous fallback |
| fundamental-YM W177 vertical residual response | killed below restricted numerical floor on isolated source-free/parent-free slice |
| W177 stable mixed response | conditional \(1+9\) nonselector |
| homogeneous \(\mathfrak{su}(2)\) triplet | exact nonzero stationary saddle in finite truncation |
| trace plus triplet Cartan support | exact kinematic construction, not stable or base-selected |
| \(H_\theta,H_F\) | exact, commuting, zero on the complement |
| \(Q=[H_\theta,H_F]\) | exact zero; polar branch fails |
| stable source-derived flag | open |
| physical flag Hessian | ineligible |

No action-spec row is promoted merely by this saddle construction.

## 9. Fired and retained kills

Fired:

1. the isolated fundamental-YM W177 vertical Euler response as an admissible selector;
2. radial stationarity as evidence of stability;
3. stability of every generic nonzero homogeneous branch;
4. polar ownership from the homogeneous \(H_\theta,H_F\);
5. automatic incidence of a generic negative triplet with the RB4
   base-induced family;
6. raw Frobenius as a substitute for trace reversal; and
7. any count, mass, vacuum, or cosmological reading.

Retained:

1. the exact trace-plus-triplet Cartan mechanism;
2. source-owned background and nonholonomic curvature terms;
3. the parent \(P_{\rm IG},D_AU\) sector;
4. moving-section \(II_s\) and \(II_0\) rivals;
5. RB5 spectral/polar calculus for a later noncommuting stable survivor; and
6. all P1/P2/P3 and five-leg non-regression obligations.

## 10. Next highest-information construction

RB7.1 should continue the stationary-construction stage by restoring the
smallest terms that can survive the commuting runaway without appending a
fitted potential:
\[
F_{ij}
=F^0_{ij}
+D_i^0\Phi_j-D_j^0\Phi_i
+[\Phi_i,\Phi_j]
-C_{ij}{}^K\Phi_K.
\]

In dependency order:

1. On the fundamental-YM branch \(\zeta_F=1\), extract the actual W177
   vertical \(F^0_{ij}\), vertical covariant
   derivative, and adapted-frame structure coefficients \(C_{ij}{}^K\),
   retaining scale/floor controls and the ambient/X4 Layer-0 fork.
2. Insert the anisotropic triplet into the complete displayed curvature
   rather than only \([\Phi,\Phi]\). Derive the full finite potential and
   all discarded-field leakage equations before solving.
3. Separately carry the \(\zeta_F=0\) branch through the parent, full-20,
   and section terms; no W177 curvature stabilization transfers to that
   branch.
4. Add the already-written parent equations
   \[
   P_{\rm IG}=Z_UD_AU
   \]
   and the fixed-\(U\) versus varied-\(U\) distinction. A candidate survives
   only if the \(A\)- and \(U\)-equations agree on one orbit.
5. Vary the actual written section functional
   \[
   \alpha_{II}|II_s|^2+\beta_0|II_s^0|^2
   \]
   through the explicit normal--vertical graph and derive its leakage and
   coupling equations. Only afterward evaluate
   \(H_{II}=II_sII_s^\dagger\) and
   \(H_{II_0}=II_s^0(II_s^0)^\dagger\) as emitted spectral words. Test
   whether the section equations lift the two anisotropy modes and the
   fifteen-dimensional base-incidence deficit.
6. For every stable full-Euler survivor, recompute
   \(H_\theta,H_F,H_{II}\), all pairwise \(Q\)'s, gaps, polar branches, and
   support incidence.
7. Only then run the full chain-rule BV, SM/Yukawa, global complex-volume,
   gravity/cosmology, causality, and P3 non-regression gates.

The next decisive question is:

```text
DO THE SOURCE-OWNED BACKGROUND, NONHOLONOMIC, PARENT, AND SECTION TERMS
LIFT THE COMMUTING RUNAWAY AND SELECT A BASE-INCIDENT NONCOMMUTING
STABLE ORBIT, OR DOES THE CARTAN SUPPORT STILL REQUIRE EXTERNAL STRUCTURE?
```

## Validation

The executable passes all 29 preregistered tensor, floor, frame, stationary,
anisotropy, Hessian, Gram, polar, trace-reversal, incidence, and surplus
controls:

```text
python3 -B tests/channel-swings/rb7_stationary_nonmetric_order_parameter_probe.py
```

No canon, claim-status, or public-posture change is made.
