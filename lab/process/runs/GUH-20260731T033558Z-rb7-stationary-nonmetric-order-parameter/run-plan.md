---
run_id: GUH-20260731T033558Z-rb7-stationary-nonmetric-order-parameter
status: completed
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-RB7
starting_revision: 2fbf97512c60
opened_at: 2026-07-31T03:35:58Z
completed_at: 2026-07-31T11:15:27Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
---

# RB7 stationary non-metric order parameter

## Target

Continue the source-action/external-datum construction at the exact RB6
boundary. Do not ask again whether a flag, external datum, or source action is
missing. Test two finite ways the already-written Yang--Mills, distortion, and
trace-reversed fibre terms could begin to produce the flag:

1. use the actual W177 ambient Yang--Mills Euler covector as the first
   target-blind Gaussian/Newton distortion response and evaluate its emitted
   \(H_\theta,H_F,Q\);
2. solve the smallest exact homogeneous non-abelian stationary truncation of
   the written Yang--Mills plus quadratic-distortion sector and determine what
   trace reversal does and does not force.

The first track is an off-shell first correction, not a stationary solution.
The second is stationary only inside its declared homogeneous finite
truncation, not in the complete GU field space.

## Repository preflight and non-duplication

RB4 already constructs the conditional observer family
\[
W_4(u)=\mathbb Rt\oplus(u^\flat\odot u^\perp).
\]
RB5 supplies conditional spectral/polar calculus. RB6 proves that invariant
W177 curvature words collapse to the nonselecting
\(\operatorname{span}\{I,T_{\rm tr}\}\), while
\(H_\theta,H_F,H_{II}\) and their commutators are type-complete but
unevaluated.

The June source-critical rank-one Pati--Salam certificates already specify a
conditional target orbit and explicitly do not source-select it. RB7 will not
repackage that certificate as a new construction. It uses the RB4
base-induced family only as a downstream incidence test after the source
orbits have been computed.

The unrelated untracked B5 native-packet source audit remains outside this
run's write boundary.

## Construction fork

Load-bearing objects are program-native:

- \(V=\operatorname{Sym}^2T^*X\), not
  \(\Lambda^2\oplus\Lambda^3\);
- the trace-reversed DeWitt form of signature \((6,4)\), not the raw
  Frobenius \((7,3)\) control;
- the W177 gimmel Levi--Civita connection only on its conditional ambient
  Yang--Mills branch;
- invariant adjoint/Krein contractions and indefinite adjoints; and
- \(P_1/P_2/P_3\) kept separate from every rank and stationary multiplicity.

Standard homogeneous Yang--Mills matrix reduction is used only as a finite
action truncation and is never silently upgraded to the complete GU action.

## Layer 0

| phrase | RB7 object | not identified with it |
| --- | --- | --- |
| source response | the Riesz-raised W177 ambient-YM Euler covector on the conditional branch | a full stationary solution or the record/matter current |
| Newton distortion | the first Gaussian correction \(\theta_R\propto-\mathcal R E_{\rm YM}(A_0)\) | an exactly solved nonlinear connection |
| stationary | a critical point of the frozen homogeneous finite action | stationarity of the full moving metric/connection/section/BV action |
| vertical triplet | the support of a minimal compact non-abelian homogeneous connection | three generations or a supplied observer |
| negative three-plane | a maximal negative support in the traceless DeWitt fibre | the RB4 base-induced \(u^\flat\odot u^\perp\) until the incidence equations pass |
| Cartan four-plane | trace line plus a source-selected negative triplet | a complex structure, hypercharge, or physical compactification |
| \(H_\theta,H_F\) | source-emitted DeWitt-self-adjoint Gram endomorphisms | a physical Hessian |
| \(Q\) | their DeWitt-skew commutator | charge conjugation, Dirac operator, or a supplied \(J\) |
| rank/multiplicity | a finite spectral or ansatz dimension | index, family number, generation count, or P3 |

The W177 residual is represented as a one-form valued in the tangent
\(\mathfrak{so}(9,5)\) algebra only under the already-declared spin-lift
identification. Its norm alone is not a direction; RB7 must reconstruct and
retain the tensor before forming a Gram operator.

## Ratified L1--L7 packet

| axis | RB7 class |
| --- | --- |
| L1 | smooth local associated bundles over the specific smooth \(Y^{14}\); homogeneous track is a finite local truncation |
| L2 | no computational observer; RB4 observers occur only in the post-computation incidence test |
| L3 | smooth invariant DeWitt/adjoint contractions and a finite polynomial matrix action |
| L4 | ambient pseudo-Riemannian \((9,5)\); no global causal-order claim |
| L5 | specific-object construction, not an RG or universality-class claim |
| L6 | no coordination loop |
| L7 | indefinite DeWitt/Krein functional; no probability rule or positive energy inferred |

## Track A: frozen residual-response grammar

At the deterministic W177 point reconstruct the full Ricci--Codazzi
Yang--Mills covector
\[
E_{MJ,L}=\nabla_M\operatorname{Ric}_{LJ}
         -\nabla_J\operatorname{Ric}_{LM}.
\]
The antisymmetric pair \(M,J\) is the tangent-representation adjoint slot and
\(L\) is the connection one-form coindex. Restrict only \(L\) through the
canonical vertical inclusion, raise the density-dual slots with the native DeWitt and
\(\mathfrak{so}(9,5)\) pairings, and set
\[
\theta_R=-\kappa\,\mathcal R_{G_V,\kappa_{\mathfrak g}}
E_{\rm YM}(A_0).
\]
The overall nonzero \(\kappa\) rescales the following Gram operators and may
not be tuned to alter an eigenspace:
\[
B^\theta_{ij}=\kappa_{\mathfrak g}((\theta_R)_i,(\theta_R)_j),
\qquad
H_\theta=G_V^{-1}B^\theta.
\]

For the algebraic curvature response use the predeclared homogeneous
quadratic part only,
\[
F^\theta_{ij}=[(\theta_R)_i,(\theta_R)_j],
\quad
B^{F^\theta}_{ij}
=G_V^{k\ell}\kappa_{\mathfrak g}
(F^\theta_{ik},F^\theta_{j\ell}),
\quad
H_{F^\theta}=G_V^{-1}B^{F^\theta},
\]
and
\[
Q_R=[H_\theta,H_{F^\theta}].
\]
This does not replace the full
\(F_{A_0+\theta_R}=F_{A_0}+D_{A_0}\theta_R+\theta_R\wedge\theta_R\).
It is a zero-derivative response diagnostic.

New fitted numerical parameters: **zero**. One existing nonzero scale
\(\kappa\) is carried; scale-free ranks, inertias, normalized commutators,
and incidence tests must be invariant under its magnitude.

## Track B: frozen homogeneous stationary ansatz

Use the smallest compact non-abelian Lie algebra
\(\mathfrak h=\mathfrak{su}(2)\) with an invariant positive adjoint pairing.
Let \(E_\sigma\subset V_0\) be a definite three-plane in the traceless
DeWitt fibre, with sign \(\sigma=\pm1\), and let
\(\{e_a\}\) and \(\{T_a\}\) be orthonormal frames satisfying
\([T_a,T_b]=\epsilon_{ab}{}^cT_c\). Freeze
\[
\Phi_i(r)=r\,e_i{}^aT_a,
\qquad
F_{ij}=[\Phi_i,\Phi_j].
\]
No \(u,P_W,J\), selected eigenvector, Standard Model label, P3, index, or
count may enter the ansatz.

The exact reduced action is
\[
V_\sigma(r)
=\frac{m^2}{2}G_V^{ij}\kappa(\Phi_i,\Phi_j)
+\frac{\alpha}{4}G_V^{ik}G_V^{j\ell}
\kappa(F_{ij},F_{k\ell})
=\frac32\sigma m^2r^2+\frac32\alpha r^4.
\]

Pre-solution continuous shape parameters:

```text
amplitude r:                                      1
new fitted action coefficients:                   0
carried existing coefficient ratio m^2/alpha:     1 scale ratio
negative-three-plane orbit in V0(6,3):           dimension 18
base-induced RB4 suborbit:                        dimension 3
relative non-base-induced orientation moduli:     dimension 15
```

The support orbit is a field orbit, not fifteen fitted coefficients.
Nevertheless, if the complete source equations do not remove the
fifteen-dimensional relative orbit, it remains continuous physical or
external structure rather than a selected RB4 observer family.

Required hostile comparators:

1. commuting/abelian homogeneous fields, for which \(F=0\);
2. positive versus negative definite triplet support;
3. raw Frobenius \((7,3)\), whose trace line has the opposite sign;
4. an anisotropic triplet \((r_1,r_2,r_3)\) before imposing equality; and
5. the exterior numerical ten, marked `NOT-TRANSFERABLE` rather than forced
   through a false identification.

## Pre-registered expected verdict

```text
TRACK A:
  EXPECT THE FULL W177 EULER TENSOR TO BREAK THE 1+9 ISOTROPY AND EMIT
  NONTRIVIAL H WORDS, BUT DO NOT EXPECT A FIRST NEWTON RESPONSE TO BE
  STATIONARY OR TO LAND EXACTLY ON THE RB4 BASE-INDUCED ORBIT.

TRACK B:
  EXPECT TRACE REVERSAL PLUS POSITIVE YM/GAUSSIAN COEFFICIENTS TO ADMIT A
  NONZERO COMPACT SU(2) TRIPLET ONLY ON A NEGATIVE TRACELESS THREE-PLANE,
  SO THE CANONICAL NEGATIVE TRACE LINE CAN COMPLETE A 3+1 CARTAN SUPPORT.
  EXPECT THE ISOTROPIC H_THETA AND H_F WORDS TO COMMUTE, LEAVING J OPEN.

OWNERSHIP:
  EXPECT A REAL SOURCE-SHAPED CARTAN START, NOT A COMPLETE SOURCE-DERIVED
  COMPLEX-CARTAN FLAG OR A CLOSED GU VACUUM.
```

## Kill conditions

1. Abort Track A if the reconstructed residual tensor does not reproduce the
   prior norm and Bianchi/control-floor separation.
2. Reject any residual-response adapter that omits a required DeWitt or
   adjoint musical map.
3. Reject scale-dependent eigenspaces or a result obtained by tuning
   \(\kappa\).
4. Reject a stationary claim for Track A; it is a first response only.
5. Reject a Track B nonzero solution unless it satisfies the complete
   anisotropic finite Euler equations, not only the radial equation.
6. Reject a Cartan-support claim unless the selected triplet is
   negative-definite and independent of the canonical trace line.
7. Report generic negative triplets and the RB4 base-induced triplets as one
   \(O(6,3)\) orbit with different incidence status: the RB4 image is a
   special dimension-three submanifold, not a second orthogonal-group orbit.
8. Reject \(Q\)-ownership if the commutator is zero, singular, or lacks the
   positive-real polar branch.
9. Reject raw-Frobenius promotion if it lacks a negative trace line.
10. Do not infer a Standard Model group, Yukawa texture, VEV, mass,
    cosmological value, anomaly, physical Hessian, index, generation, or
    count.

## Constraint-surplus rule

The finite ansatz is informative only through separately reported ranks:

- free coefficient/shape parameters before stationarity;
- independent finite Euler equations;
- stationary orbit dimension after gauge;
- base-induced-incidence codimension;
- independent spectral/inertia/polar constraints; and
- surviving moduli.

Do not collapse inequalities, gauge directions, or repeated eigenvalue
conditions into independent equations merely to inflate surplus.

## Five-leg boundary

| leg | permitted RB7 conclusion |
| --- | --- |
| SM/Yukawa | source-shaped Cartan support and base-induced incidence only; no SM group or zero-order Yukawa placement |
| quantum/Krein/BV | exact indefinite adjoints and \(Q\) polar eligibility; no CME, domain, physical state space, or mass Hessian |
| gravity/cosmology | trace-reversal dependence and first cancellation direction; no full stationary metric/section solution or cosmological prediction |
| UV/causality | pointwise/homogeneous order parameter only; no curved subprincipal or common-cone upgrade |
| P3/index/count | P3 unchanged and separate; triplet/rank/four-plane dimensions are not counts |

## Planned outputs

- `tests/channel-swings/rb7_stationary_nonmetric_order_parameter_probe.py`
- `explorations/rb7-stationary-nonmetric-order-parameter-2026-07-30.md`
- scoped updates to the N3 boundary, `NEXT-STEPS.md`,
  `explorations/README.md`, and `tests/README.md`

No canon, claim-status, or public-posture change is authorized.

## Pre-execution source-ownership and hostile correction

The parallel audit fires before either track is evaluated and narrows the
preregistered interpretation.

For Track A, the isolated source-free, parent-free
fundamental-Yang--Mills-plus-quadratic-distortion connection equation gives
the first correction
\[
\delta A
=-\kappa\,\frac{\zeta_F}{g_A^2}
\mathcal R_{G,\kappa_{\mathfrak g}}
\left(D_A^!F_A\right).
\]
It may be represented as \(\delta A=\delta\theta\) only when that frozen
reference also has
\(A_0=\Gamma(\epsilon_{\rm IG})+U\), hence \(\theta_0=0\). Otherwise it is
an algebraic target for \(\theta\), not a connection increment. If
\(\theta\) is instead treated as W203's auxiliary variable, its source is
the matter/record current \(J\), not the W177 Yang--Mills residual. The full
N1 \(U\)-equation contains parent and source terms and forces \(\theta=0\)
only on the same source-free, parent-free slice. Track A is therefore graded
as a connection-descent concomitant, not an independently generated
stationary distortion.

For Track B, with
\[
F=\tfrac12F_{ij}e^i\wedge e^j,
\]
the finite coefficients are
\[
m^2=\kappa^{-1},
\qquad
\alpha=\zeta_Fg_A^{-2},
\]
up to the declared invariant-pairing convention. The Yang--Mills term exists
only on the \(\zeta_F=1\) branch. W203 conditionally pins \(\kappa>0\) on
the accepted C-positive record sector, while its magnitude remains
normalization-owned. The fundamental-YM sign, \(g_A^{-2}\), and native
adjoint-pairing restriction remain charged forks, so positive and negative
branches must both be reported.

The anisotropic equations, not only the radial equation, are mandatory:
\[
V=\frac{\sigma m^2}{2}\sum_ar_a^2
+\frac{\alpha}{2}\sum_{a<b}r_a^2r_b^2,
\qquad
E_a=r_a\left[\sigma m^2+\alpha(r_b^2+r_c^2)\right].
\]
Every nonzero generic stationary branch is a saddle. For the intended
\(\alpha,m^2>0,\sigma=-1\) branch, commuting one-component directions have
zero quartic term and run to \(-\infty\). Thus the finite track may establish
a kinematically valid trace-plus-triplet Cartan support at a saddle, but it
cannot establish a stable order parameter. Its \(H_\theta,H_F\) commute
throughout the anisotropic ansatz, and \(H_\theta\) has a seven-dimensional
zero sector, so both the polar and robust spectral-ownership gates are
expected to fire.

The next stationary-construction continuation, if these kills fire, must on
\(\zeta_F=1\) first evaluate source-owned terms already present in the
unreduced curvature,
\[
F_{ij}
=F^0_{ij}+D_i^0\Phi_j-D_j^0\Phi_i
+[\Phi_i,\Phi_j]-C_{ij}{}^K\Phi_K,
\]
together with the \(P_{\rm IG},D_AU\) parent and the actual section
functional. These terms can survive along commuting directions and therefore
can test stability without appending an arbitrary potential. The
\(\zeta_F=0\) branch must be tested separately through parent/full-20/section
terms. The written section action is
\(\alpha_{II}|II_s|^2+\beta_0|II_s^0|^2\); its variation must precede use
of \(II_sII_s^\dagger\) as an emitted spectral word.

## Execution result

### Track A

The full historical-frame W177 residual is stable:

```text
scale 0.75: 3.19904935
scale 1.00: 3.19904137
scale 1.25: 3.19903939
```

The vertically restricted connection-form component is not:

| scale | vertical residual | vertical direct/Codazzi discrepancy |
| ---: | ---: | ---: |
| 0.75 | 0.00823939 | 0.00865502 |
| 1.00 | 0.00361491 | 0.00372577 |
| 1.25 | 0.00166594 | 0.00179771 |

At the central scale its signal/floor ratio is `0.9702446`, and its relative
scale spread is `1.81843`. Kill conditions 1--4 fire before a spectrum is
read.

The stable base-form/mixed-adjoint comparator carries the full signal and
gives
\[
H_{\rm mix}
\simeq0.28125(I+T_{\rm tr})
=0.5625P_{\rm traceless}
\]
with central relative fit residual `4.1281e-7`. Its trace commutator norm is
`5.1220e-7`, below the declared `2e-5` resolution. It is a stable \(1+9\)
nonselector.

Track-A verdict:

```text
VERTICAL-RESPONSE-KILLED-BELOW-NUMERICAL-FLOOR
SIGNAL-PRESERVING-MIXED-GRAM-NONSELECTING
```

### Track B

For the \(\alpha=m^2=1,\sigma=-1\) representative:

```text
rank-three Hessian: [-1, -1, 2]
rank-two Hessian:   [-2,  1, 2]
```

Both nonzero branches are saddles. The commuting one-component direction is
unbounded below. On the isotropic triplet,
\[
H_\theta=-r^2P_E,
\qquad
H_F=2r^4P_E,
\qquad
Q=0.
\]
The native trace-plus-triplet restriction has inertia \((0,4)\); raw
Frobenius gives \((1,3)\). A planted base-induced triplet passes the
rank-two-tensor incidence control, while a generic negative triplet in the
same \(O(6,3)\) orbit has normalized determinant obstruction
`0.00814506`. The support orbit is dimension `18`; the RB4 image is
dimension `3`.

Track-B verdict:

```text
KINEMATIC-CARTAN-SUPPORT-AT-NONZERO-SADDLE
NO-STABLE-SELECTION
Q-ZERO
BASE-INCIDENCE-UNSELECTED
```

No action row, datum, claim status, canon verdict, or public posture moves.
P1/P2/P3 remain unchanged.

## Validation receipt

Passed:

```text
python3 -B tests/channel-swings/rb7_stationary_nonmetric_order_parameter_probe.py
python3 -B tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py
python3 -B tests/channel-swings/rb5_epsilon_flag_ownership_spectral_hessian_probe.py
python3 -B tests/channel-swings/rb4_observer_cartan_moving_family_probe.py
python3 -B tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
python3 -B tests/channel-swings/unified_source_variation_probe.py
python3 -B tests/channel-swings/unified_source_datum_packet_v0_probe.py
python3 -B tests/channel-swings/vertical_source_action_reduction_probe.py
python3 -B tests/channel-swings/w177_ym_residual_and_mode_closure_probe.py
python3 -m py_compile tests/channel-swings/rb7_stationary_nonmetric_order_parameter_probe.py
```

The RB7 probe passes 30/30 controls. The inherited validation chain passes.
