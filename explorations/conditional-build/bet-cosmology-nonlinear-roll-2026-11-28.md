---
title: 'Nonlinear wedge cosmology: apparent w=-1 can hide growing curvature'
status: exploration
doc_type: structural-result
created: '2026-11-28'
program_target: BET-COSMOLOGY
tier: T1
expected_delta: Decide the nonlinear endpoints of the actual growing scalar mode across the owned positive-reference moment class
actual_delta: One expanding branch reaches F=0 in finite Jordan time with finite metric data; the other has unbounded curvature with w_kin tending to minus one; stable-manifold exceptions remain
class_covered: Leading order-h local4D own-wedge action, constant positive conformal moments, h>0, vacuum spatially flat FLRW, F>0 scalar-tensor chart and constraint-admitted expanding growing-mode cones
premises:
- Owned full metric action and moment cone from wedge-shiab-einstein-reduction-2026-11-27.md
- The GU* reduction and reference class are conditional, not selected by source GU
- No matter, radiation, acoustic ruler, physical Newton identification or source one-form stress map is supplied
- Nonlinear asymptotics are statements about the leading truncation, not permission to use it beyond its regime of validity
source_bridge:
  status: conditional
  reason: SC-COS-50/51/52 assert variable dark energy and an adjoint one-form construction; they do not identify it with this scalar-tensor reduction or select its reference/state
kill_condition: Full constraint preservation or positive-F nonlinear cone proof fails; a potential-only or linear-sign argument cannot establish an endpoint exclusion
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Lane C only; no scientific matrix or physics-ledger absorption
---

# Result

program_target: BET-COSMOLOGY
tier: T1
expected_delta: Test whether the owned tachyon can end in a regular finite-scale rolling state without a new action or reference prescription.
actual_delta: Both genuine growing-mode branches leave every compact positive-F endpoint class, in different ways; transient rolling and the stable separatrix survive.

| State | Precisely what is established |
|---|---|
| **ESTABLISHED** | For every admitted positive moment triple, the full leading vacuum FLRW equations have two forward-invariant growing-mode cones. The lower-F cone reaches F=0 in finite Jordan proper time with finite H, R and Rdot. The upper cone has H proportional to time and R proportional to time squared asymptotically, while w_kin approaches -1 from below. |
| **RULED OUT** | A finite positive-F curvature endpoint for either of those two growing-mode cones within the unchanged leading model. No nonconstant periodic orbit stays inside the positive-F chart. |
| **ESTABLISHED survivors** | The exact de Sitter state, its local stable manifold, finite-duration slow transients, and regular Jordan continuation through F=0 as a mathematical ODE. Other actions/reference signs and physical state restrictions remain distinct routes. |
| **NOT MODELED / UNDETERMINED** | Source GU's dark-energy history, full14D or higher-h fate, the physical interpretation of F=0, observed w_DE, measured Newton coupling, matter/radiation/CMB/DESI consistency, or validity of arbitrarily large curvature in the leading reduction. |

```gu-typed-objects
result: full-row nonlinear vacuum FLRW endpoint theorem
carrier: real reduced four-metric and its scalar curvature plus positive conformal reference moments LAYER=observed BRIDGE=conditional-leading-wedge-reduction CHIRALITY=N/A
pairing: Lorentzian metric variation and mathematical Einstein-frame scalar variables; not a physical quantum norm ON=reduced_bosonic_metric
real_structure: (-+++) and inherited K95 connection-metric coefficients; no K77 sign transfer
grading: curvature and perturbation order, not family chirality
action_owner: repository-construction -- same reviewed leading4D GU* own-wedge action
target: constrained cosmological solutions and their proper-time asymptotics MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING:** the f(R) variables below describe a proved FLRW subsector of the declared reduced metric action. They are not the source's adjoint one-form, a Kaluza–Klein scalar or an observed dark-energy fluid. The positive-sign f(R) control is a comparator only. [Required routing](../../lab/methods/source-native-comparator-routing.md).

**Custody:** GU basis `fe84a56dc903824e4f28877c07b0627157228aeb`. [Probe](../../tests/program-focus/bet_cosmology_nonlinear_roll_probe.py), [certificate](../../lab/process/bet-cosmology-nonlinear-roll-certificates.json), [finite Lean cores](../../Lean/GUFormalization/CosmologyRoll.lean), [evidence](../../lab/process/bet-cosmology-nonlinear-roll.json), [independent review](../../lab/process/hostile-reviews/2026-11-28-cosmology-nonlinear-roll-review.md).41 exact controls and six finite Lean lemmas do not formalize global ODE or asymptotic analysis.

## Source relevance and reuse

[SC-COS-50/51/52](../../lab/sources/source-claim-register.yaml) retain ASSERTS polarity. SC-COS-50 is TOE2025 02:14:44 with the continuing-DESI qualification and automatic-identity demand; SC-COS-51 is 02:22:20, the adjoint-one-form replacement; SC-COS-52 is UCSD2025 00:02:05 with completion00:25:56–00:27:00. They do not supply the action/reduction/matter map assumed here. The source target is not a generic scalar quintessence model.

The [reviewed reduction](wedge-shiab-einstein-reduction-2026-11-27.md) and [last growth result](bet-cosmology-wedge-growth-2026-11-27.md) already own the sign, full linear scalar row and exact growth/H range. This wave reuses them; its delta is the constrained nonlinear endpoint. [July and sibling reconciliation](sibling-import-adjudication-2026-11-27.md) keeps W153/W157's differently normalized bending owner separate. W159's action/shape, RG and gradient-saturation escapes are already recorded and remain different tests; no old coefficient, DBI speed cap or healthy mixed-operator verdict is imported. DU's rolling interpretation was conjectural and its later target superseded. It supplies no nonlinear equation here.

The standard FLRW and conformal-frame method is described by [De Felice–Tsujikawa, §§2.1–2.3](https://arxiv.org/abs/1002.4928); the primary text's F>0 frame condition is retained. The action-specific discriminant, complete constraint, cone arguments and asymptotic coefficients below are derived directly. No novelty or observational-fit claim is made.

## 1. Exact owner and assumptions

Use only the already reviewed **leading order-h local4D own-wedge metric
action**, with constant nonzero positive conformal moments and h>0:

```
S4=integral sqrt(-g) [AQ Ric²+(5/2)AQ R²+AR R+A0],
AQ=h m0/2, AR=-99h m1/4, A0=2115h m2/16,
m0>0, m1>0, m1²<=m0m2<infinity.
```

Signature is(-+++); use the accepted BH curvature convention,
R_FLRW=6(Hdot+2H²), and □ on homogeneous scalars is-d²/dt²-3H d/dt.
All Jordan times below are proper times of this same reduced metric.

Define positive constants

```
b=17AQ/6=17h m0/12,
a=-AR=99h m1/4,
c=A0=2115h m2/16,
D=4bc-a²,
mu²=a/(6b)=99m1/(34m0),
F=f'(R)=2bR-a,   f(R)=bR²-aR+c,
F*=D/a,   R*=2c/a,   H*=sqrt(R*/12).
```

With z=m1²/(m0m2),
`a²/(4bc)=(3267/3995)z<=3267/3995<1`, hence D>0 and F*>0.
Equivalently
`D=(3h²/16)(3995m0m2-3267m1²)` and
`F*=h(3995m0m2-3267m1²)/(132m1)`.

This model is a declared GU* reduction, not a source-selected observed
action. No matter, radiation, physical Newton normalization, source one-form
stress map or early-universe ruler is added. F>0 names the conformal/response
sector being analyzed; F is not automatically a measured Newton coupling,
especially with the owned Weyl-squared term still in the full action.

## 2. Full metric-row binding and the Jordan constrained system

The owned4D identity gives
`AQ Ric²+(5/2)AQ R² = (AQ/2)C²-(AQ/2)E4+bR²`.
On every spatially flat FLRW metric C vanishes, so its Bach variation
vanishes. The constant-coefficient Euler term has zero local bulk metric
variation under the held compact-variation/boundary convention. Therefore
the vacuum f(R) equations are the full local metric rows in this symmetry
class, not merely an action restricted before variation.

Write w=Fdot. The exact autonomous Jordan system is

```
Hdot=(F+a)/(12b)-2H²,
Fdot=w,
wdot=mu²(F-F*)-3Hw.
```

Its Friedmann constraint is

```
C(H,F,w)=3F H²-U(F)/2+3Hw=0,
U(F)=(F+a)²/(4b)-c =R F-f.
```

Direct differentiation, using
`3mu²(F-F*)=F R-2f`, gives `Cdot=-4H C`. Thus a constraint-admitted initial
state remains admitted. In this FLRW class the00 row and trace supply the
remaining spatial row; no independent metric equation is discarded.

All cone statements below quantify only constraint-admitted initial states.
They are not assertions that H,F,w can be chosen independently. They are
nonempty: U(F*)=F*R*/2>0, and near F* the positive constraint root

`H=[-w+sqrt(w²+(2/3)F U(F))]/(2F)`

exists for either sign of a sufficiently small nonzero w. The two sides
of the local unstable manifold described in section7 lie in these cones.

## 3. Lower cone: finite positive-F exit, not an automatic singularity

Assume `0<F_i<F*`, `w_i<0`, H_i>0. Put v=-w>0. Until F reaches0,

`vdot=mu²(F*-F)-3Hv`.

At v0 its derivative is positive; at H0,
`Hdot=(F+a)/(12b)>0`. Thus v,H stay positive and F decreases. Define

```
Hmax=max(H_i,sqrt((F_i+a)/(24b))),
c0=mu²(F*-F_i)>0,
m=min(v_i,c0/(3Hmax))>0.
```

The H equation gives H<=Hmax. Consequently
`vdot+3Hmax v>=c0`, and exact integrating-factor comparison gives

`v(t)>=v_i exp(-3Hmax t)+[c0/(3Hmax)](1-exp(-3Hmax t))>=m`.

Hence F(t)<=F_i-mt. The first F=0 crossing occurs at a time
`0<T0<=F_i/m<infinity`.

There is no earlier hidden finite-time blow-up in these variables. On any
interval with F>0, `vdot<=mu²F*`, so v<=v_i+mu²F*t. H,F,v are bounded up to
the displayed finite bound. Their polynomial ODE has bounded derivatives
there and continues to the first crossing. The constraint at that point
implies the exact relation

`H(T0) v(T0)=D/(24b)>0`.

Thus the crossing is transverse. R=(F+a)/(2b), Rdot=-v/(2b), H and Hdot
remain finite. In particular the flat-FLRW Riemann invariants, which depend
on H² and Hdot, remain finite. The Jordan ODE is regular at F0 and has a
local continuation across it. What ends is this F>0 Einstein-frame/response
sector. A physical singularity, a full-PDE continuation or a measured
Newton sign change does not follow from this calculation.

## 4. Einstein-frame normalization for the upper cone

Assume `F_i>F*`, w_i>0, H_i>0. At w0 the acceleration is positive, and at
H0 the derivative of H is positive. Thus this cone is invariant while it
exists. U(F)>0 on F>=F*, so the positive expanding constraint root exists.

Multiply the entire vacuum action by1/2, which changes no vacuum equation.
For the scalar calculation use the mathematical reference F_ref=1 in the
held units and set

```
g_E=F g_J,  dt_E=sqrt(F)dt_J,
phi=sqrt(3/2) log F,  alpha=sqrt(2/3),
H_E=(H_J+w_J/(2F))/sqrt(F),
p=dphi/dt_E.
```

This is a change of variables, not a new physical Planck scale or reference
measure. A different constant F_ref only rescales the auxiliary Einstein
units; the Jordan conclusions below are unchanged. The half-normalized
scalar action is `integral sqrt(-g_E)[R_E/2-(dphi)²/2-V]`, where

```
V(F)=(R F-f)/(2F²)=[1+2a/F-D/F²]/(8b),
V_infinity=1/(8b), H_infinity=1/sqrt(24b).
```

The Weyl term causes no FLRW row in either frame. In this cone H_E>0 and
p>0. The exact equations are

```
3H_E²=p²/2+V,
dH_E/dt_E=-p²/2,
dp/dt_E=-3H_E p-V_phi,
dF/dt_E=alpha F p,
V_phi=alpha a/(4bF)(F*/F-1).
```

V has a unique critical point on F>0, the maximum F*. On F>F*, V>V_infinity
and V_phi<0. Positivity of V also gives
`H_J=sqrt(F)(H_E-p/sqrt(6))>0`, consistent with the Jordan cone proof.

## 5. Upper-cone global continuation and asymptotic proof

Let E=p²/2+V=3H_E². Then
`E'=-3H_E p²<=-3H_infinity p²` and E>=V_infinity. Thus H_E and p are bounded,
and `integral_0^infinity p² dt_E<infinity` once global continuation is shown.
Because phi>=phi_i>phi*, the potential and its derivative are bounded; p'
is bounded. On every finite Einstein-time interval phi advances at most
linearly, so the smooth ODE has no finite-time escape and continues for
all future Einstein time. The bounded p' makes p uniformly continuous;
its square integrability then implies p->0.

If phi had a finite limit, it would be strictly greater than phi*. Its
limiting negative V_phi would make p' uniformly positive once p is small,
contradicting p->0. Hence F->infinity. Therefore V->V_infinity and
H_E->H_infinity.

For the exact rate put z=F p. Differentiation gives

`z'=-(3H_E-alpha p)z+alpha a/(4b)(1-F*/F)`.

The damping coefficient tends to3H_infinity>0, and the forcing tends to
alpha a/(4b)>0. For completeness: subtract
`z_infinity=alpha a/(12bH_infinity)`; the resulting equation is
`(z-z_infinity)'=-gamma(t)(z-z_infinity)+epsilon(t)`, with gamma eventually
bounded below by a positive constant and epsilon->0. Variation of constants
first bounds z and then makes its limsup deviation arbitrarily small.
Thus z->z_infinity and z'->0. In particular

```
F'_E -> v_infinity=alpha z_infinity=a/(18b H_infinity)>0,
F''_E ->0,
F(t_E)/t_E ->v_infinity.
```

Jordan time satisfies
`t_J=integral dt_E/sqrt(F) ~2sqrt(t_E/v_infinity)`, so t_J also tends to
infinity. The exact conversions yield

```
F/t_J² ->v_infinity²/4=a²/(54b),
H_J/t_J ->v_infinity H_infinity/2=a/(36b)=mu²/6,
R_J/t_J² ->v_infinity²/(8b)=a²/(108b²)=mu^4/3.
```

To justify Hdot_J, rather than differentiate an asymptotic equivalence,
use the exact identity

`Hdot_J=(F'_E H_E-F''_E)/2-(F'_E)²/(2F)`.

It follows from H_J=sqrt(F)H_E-F'_E/(2sqrt(F)) and H'_E=-p²/2.
Consequently `Hdot_J ->a/(36b)>0`. Hence

`w_kin+1=-2Hdot_J/(3H_J²) ~ -4/(mu² t_J²)`.

The model approaches w_kin=-1 from below while H and R diverge at infinite
Jordan proper time. It does not approach another finite-curvature de Sitter
endpoint. Calling this physical dark energy or applying the leading
curvature expansion indefinitely would require missing assumptions.

## 6. No cycles and compact omega limits in the positive-F region

The exact identity H'_E=-p²/2 is a Lyapunov identity even when the Einstein
Hubble parameter is negative. A periodic orbit within the valid F>0 chart
would force the integral of p² over a period to vanish, hence p=0 and
V_phi=0; it is an equilibrium. There are no nonconstant cycles.

More precisely, suppose a forward trajectory is precompact in a region
where F is bounded away from0 and the transformed variables are bounded.
H_E is monotone with a finite limit. On its nonempty invariant omega-limit
set H_E is constant, so p=0. Invariance then forces V_phi=0 and F=F*.
The constraint gives H_E=plus or minus sqrt(V(F*)/3). The limiting sign
is fixed by the limit of H_E, so the omega-limit set is a single de Sitter
equilibrium. In the expanding Jordan region it is the expanding one.

This compactness hypothesis is essential: the upper branch escapes to
F=infinity and the lower branch reaches the chart boundary. The theorem
does not classify every initial state, every transient turn or every
possible continuation through F0.

## 7. The actual local separatrix and allowed growing-mode states

At F*,p0 the Einstein potential has
`V_phiphi(F*)=-a/(6bF*)=-mu²/F*<0`. The expanding constrained Einstein
system in(phi,p) therefore has the two real eigenvalues

`lambda_±=[-3H_E* plus/minus sqrt(9H_E*²+4mu²/F*)]/2`,

one positive and one negative. The ordinary smooth stable-manifold theorem
gives a one-dimensional local stable manifold and a one-dimensional local
unstable manifold. On the unstable eigenline p=lambda_+ delta phi, so the
two nonlinear unstable branches lie respectively in the upper and lower
cones once sufficiently close to the equilibrium. This supplies actual
constraint-compatible nonlinear versions of the two linear growing signs.
The stable manifold is the local separatrix; it and the exact equilibrium
are genuine exceptional finite-endpoint states, not ruled out.

No assertion that these two cones exhaust all initial data is made. States
starting outside them can approach the saddle on its stable manifold or
turn before entering a cone; the compact-omega-limit statement above is
the separately quantified global restriction.

## 8. Verification and claim ceiling

The41 exact controls verify the action coefficients/moment bound,
the Legendre and potential derivatives, Cdot=-4HC, cone boundary signs,
the left crossing equation, z' identity, F'/H asymptotic constants and
the scalar mass sign. The owned full-row FLRW/Bach-zero seam is retained.
A conventional positive-AR f(R) model calibrates the healthy scalar sign;
it is a countercontrol outside this class, not a proposed repair. The
already-owned signed-reference escape remains separately scoped. Global continuation and asymptotic
comparison remain reviewed analytic proofs, not finite tests alone.

This answers a new nonlinear endpoint question for the declared leading
vacuum FLRW model. The older W153/157/159 and W79/W122 objects have different
coefficients or owners; DU supplies no action/field/stress identification.
No source-selected reference, measured Newton constant, physical w_DE,
matter/radiation history, CMB/DESI fit,14D nonlinear evolution, higher-h
control, quantum positivity or matrix/ledger verdict is obtained.

Standard Einstein-frame background: De Felice–Tsujikawa,
https://arxiv.org/abs/1002.4928. The normalization and model-specific
identities above are explicit so the proof does not depend on an unstated
frame or gravitational-unit convention.

## Decision and continuation

This gives a conditional model signature: the upper branch can mimic a near-minus-one *kinematic ratio* while its expansion rate and curvature keep growing. The exact asymptotic limit is not a small perturbation of a finite-scale de Sitter endpoint. It must not be advertised as DESI agreement, physical phantom matter or a quantum ghost. On the lower branch the positive-F frame fails, but the original Jordan equations and metric can continue; that is a typed boundary, not a manufactured singularity.

This class theorem does not meet BET-COSMOLOGY's empirical kill or success criterion. Matter, radiation, acoustic normalization, the observed stress map, reference/state selection and the regime of validity remain required before data fitting. Arbitrarily long near-de Sitter transients can be arranged by moving initial data toward the stable separatrix; no source-selected duration or initial amplitude is claimed. The independent Weyl-squared perturbation/physical-state problem remains open even though its metric variation vanishes on exact FLRW.

No action, measure, potential or physical state is added. W2's historical10 families /4 obligations /net6 /0 source-selected predictions is unchanged and is not a parameter count for the wedge family. This is one LC cosmology wave on an already-owned family; the spent wedge3/3 and CW2b5/5 construction budgets stay spent. Counter128 returns to the already-queued main-line antilinear/PT step3. The current bet remains active,7 of24 runs used; no new stop or approval rule is introduced. Lane-B re-derivation is required before any scientific matrix or ledger credit.
