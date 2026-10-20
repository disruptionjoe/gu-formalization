---
title: "K1864: A local action for causal trace removal, with scalar and vacuum costs"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: INTERNAL-TRACE-PROJECTOR-PURE-GR-SCREEN
target_claim_verdict: EXCLUDED-FOR-THE-STATED-UNSCREENED-SCALAR-TENSOR-COMPLETION
claim_ceiling: supplied scalar-tensor completion and its scoped weak-field and global-domain restrictions; no native GU adapter or novelty
---

# Causal trace removal has a local scalar-tensor completion

K1863's retarded trace projector is realized by the linear response of a local
scalar-tensor action with specified initial data. The completion has a healthy
additional scalar near its positive constant background. It is not pure GR:
its weak-field, negligible-pressure matter response has gamma=1/2. Its exact
flat constant-vacuum configurations require a quadratic scalar that cannot stay
positive on all Minkowski space and cannot be spatially periodic. Thus the
local variational repair is real, but neither a pure-GR response nor a globally
regular positive-coupling vacuum screen follows.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: local variational realization of retarded trace removal and its scalar, weak-field and global vacuum consequences
carrier: real four-dimensional Lorentz metrics and positive real scalar Phi with supplied conserved matter LAYER=toy CHIRALITY=N/A
pairing: Lorentz contraction and invariant volume ON=real_metric_scalar_fields
real_structure: signature minus-plus-plus-plus, real scalar, positive Phi branch
grading: tensor rank and linear perturbation order only
action_owner: repository-construction -- supplied Brans-Dicke omega-zero comparator, not native I1B
target: retarded linear metric response, weak-field potentials and exact flat vacuum solutions MAP-TYPE=evaluation
```

## 1. Question, reuse and input ownership

[K1863](k1863-conserved-screening-causality-2026-10-20.md) defines, on a flat
zero-past domain,

```
Pi f = eta f - partial partial G_Box f,
Q_ret T = T - Pi(tr T)/3,
```

where G_Box is the retarded inverse of Box. It proves conservation, causal
support and idempotence, leaving an action and positive-state interpretation
open. The question here is the cost of one explicit local completion. An
ordinary metric-only action cannot be obtained merely by inserting a retarded
kernel into a symmetric quadratic form. That observation does not forbid a
local action with extra dynamical fields and retarded initial data.

The action below is the familiar omega=0 Brans-Dicke theory, not a new gravity
theory. [Brans and Dicke (1961)](https://doi.org/10.1103/PhysRev.124.925) provide
the scalar-tensor family. W220 already used Brans-Dicke as a conventional PPN
control; it granted pure GR in its GU comparison. We reuse that distinction.
The new repository connection is to the exact K1863 response, followed by its
boundary/positivity and repair tests. No claim of novelty is made.

SC-ACT-01/02 and SC-COS-50/51/54 remain ASSERTS; SC-META-53 remains UNCERTAIN.
The added Phi is neither the native ad-valued displacement one-form nor the
metric on Y=Met(X). The local I1B Hessian and K1861 equation-dual injection
problem remain separate. LT-GR1b, LT-GR2c/2d/2e/6b and LT-GR10 do not move.
Reverse demands are causal conserved response, variational ownership and
acceptable matter response; choosing a comparator to meet them grants no
source derivation or held-out confirmation credit.

## 2. Local action and the retarded sector

Set kappa>0 and take compactly supported variations, or boundary terms/data
that cancel the ordinary metric variation boundary term. The bulk action is

```
S = (1/(2 kappa)) integral sqrt(-g) Phi R + S_m[g,matter].       (1)
```

Matter is minimally coupled in this Jordan metric and has no direct Phi
coupling. Variation in Phi and g respectively gives

```
R=0,
Phi G_mn + (g_mn Box - nabla_m nabla_n)Phi = kappa T_mn.       (2)
```

The scalar is not absent merely because (1) has no explicit kinetic term.
Tracing (2) and using R=0 gives 3 Box Phi=kappa T.
Linearize about g=eta, Phi=1 and zero matter. With chi=Phi-1,

```
Box chi=kappa tau/3,
G^(1)(h)=kappa T-(eta Box-partial partial)chi.                (3)
```

For smooth past-supported conserved T on Minkowski space or the flat
R x T3 cylinder, choose chi's zero-past solution chi=kappa G_Box tau/3.
Then (3) is exactly G^(1)=kappa Q_ret T. Harmonic metric data can also be
chosen retarded as in K1863. Both fields propagate causally. On the cylinder,
retain K1863's zero integrated charge conditions; no positive uniform density
is inserted into its flat retarded problem.

The full action admits homogeneous scalar waves. Their exclusion from this
response is an initial-data choice, not removal of a degree of freedom. Vary
first, then select retarded solutions. Substituting a retarded solution into
an ordinary action before variation generally symmetrizes the kernel and
need not give (3). This construction proves local action ownership for this
comparator only, without a metric-only nonlocal variational claim.

## 3. Positivity and the independent weak-field test

On Phi>0 let g_E=Phi g. After the conformal curvature identity and integration
of its boundary divergence, the gravitational action becomes

```
S_E=(1/(2 kappa)) integral sqrt(-g_E)
       [R_E-(3/2)g_E^(mn)partial_m ln(Phi) partial_n ln(Phi)]. (4)
```

Thus varphi=sqrt(3/(2 kappa)) ln(Phi) has the ordinary positive-energy
massless scalar kinetic term in signature (-+++), in addition to the usual
Einstein spin-two sector. This is a local classical sign statement near a
regular positive background, not a proof of quantum UV completion or global
stability. Matter couples to Phi^(-1)g_E and therefore excites this scalar.

For a weak, static, nonrelativistic isolated source on R3, at leading order
T00=rho and Tij=0, tau=-rho. This is an asymptotically flat static experiment,
separate from the cylinder's zero-past source class. For a point-mass exterior
write U_E=kappa M/(8 pi r). The linear equations give

```
chi=kappa M/(12 pi r)=(2/3)U_E,
h00=2U_E+chi=(8/3)U_E,
hij=(2U_E-chi)delta_ij=(4/3)U_E delta_ij.
```

The Newton-calibrated potential is U_N=4U_E/3, hence gamma=1/2. This fails
an exact pure-GR gamma=1 requirement for this unscreened, massless comparator.
No fresh experimental bound or GU falsification is claimed. Pressure,
strong-field sensitivities and different asymptotic data are outside this
leading weak-field calculation.

Equivalently, for conserved test tensors the metric exchange numerator is

```
T:T' - (1/3)tau tau'
 = [T:T'-(1/2)tau tau'] + (1/6)tau tau'.                    (5)
```

Longitudinal terms vanish against the conserved probe. The extra positive
scalar residue is not a ghost cancellation. Traceless sources cannot see it;
traceful matter can. This directly consumes the projector construction rather
than counting rank five as five physical gravitational polarizations.

## 4. Executed kinetic and mass repairs change the question

Add the Brans-Dicke kinetic term -omega (nabla Phi)^2/Phi to (1), keeping
constant omega and the same background/data. The scalar response becomes
chi=kappa G_Box tau/(2omega+3). Let c=1/(2omega+3). Then

```
Q_c T=T-c Pi tau,
tr(Q_c T)=(1-3c)tau,
Q_c^2 T-Q_c T=c(3c-1)Pi tau,
gamma=(1-c)/(1+c)=(omega+1)/(omega+2).                     (6)
```

The positive scalar branch has 2omega+3>0. Exact nontrivial trace removal
and exact idempotence force c=1/3, hence omega=0 and gamma=1/2. The c=0
limit is GR with no scalar trace subtraction. Large positive omega approaches
GR but changes the original projector; it is not a same-assumption rescue.
These statements apply to this one-scalar, constant-omega family, not every
possible causal gravitational completion.

Alternatively add a potential U(Phi) with U(1)=U'(1)=0 and U''(1)=3m²>0.
The scalar equation linearizes to (Box-m²)chi=kappa tau/3. In the metric row
replace G_Box by G_(Box-m²). Its trace is

```
tr(Q_m T) = -m² G_(Box-m²) tau.                            (7)
```

A formal Fourier mode with Box eigenvalue z has scalar trace transfer
-m²/(z-m²). It approaches1 at z=0 and0 at large |z|, away from the pole.
Thus the scalar mass suppresses the extra static force at long range and
restores the trace response there; it does not implement low-frequency
vacuum trace removal. Exact idempotence is lost. For the static weak-field
point source the relative scalar correction is exp(-mr)/3, giving
`gamma(r)=[1-exp(-mr)/3]/[1+exp(-mr)/3]` at linear order. This is a
changed, Yukawa-range comparator, not an eternal-source use of a zero-past
inverse and not a nonlinear screening theorem.

## 5. Exact constant vacuum: local cancellation is not a global positive model

Return to U=0, omega=0. Let T_mn=-rho eta_mn with constant rho and require
the Jordan metric to be exactly Minkowski. The full nonlinear equations (2)
reduce, without linearization in Phi, to

```
Box Phi=-4 kappa rho/3,
partial_m partial_n Phi=-(kappa rho/3)eta_mn.
```

On connected all-Minkowski space every C2 solution is therefore

```
Phi(x)=Phi0+b_m x^m-(kappa rho/6)eta_mn x^m x^n.            (8)
```

The difference from this quadratic has zero Hessian and is affine. For
rho>0, a spatial ray drives Phi to minus infinity; for rho<0, a timelike
ray does. Affine terms cannot repair that leading sign. Thus no nonzero
rho solution remains Phi>0 on all Minkowski space. On R x T3 periodicity is
already impossible: integrating any spatial second derivative gives zero,
whereas (8) requires its constant value -kappa rho/3. This is an exact
domain obstruction in this action, not a claim about all cosmologies.

A bounded patch admits Phi>0 by choosing Phi0 sufficiently large; (8)
is a genuine local countercontrol to an overbroad no-solution statement.
But its boundary/initial data and effective coupling vary with rho. It is
not a fixed-data relaxation mechanism or a selected vacuum magnitude.
A curved metric or a different potential is another branch. For a fixed
potential and a constant-scalar flat branch, U'(Phi)=0 and U(Phi)=-2kappa rho;
an isolated fixed critical point cannot accommodate arbitrary vacuum shifts.
No nonlinear varying-scalar classification for such potentials is claimed.

## 6. Review, reproducibility and next decision

The analytic argument covers action variation, retarded data, conformal sign,
static matter response, repair scope and the all-space/periodic proof. The
producer and separate rational probe check the conformal linear Einstein
identity, conserved projector algebra, kinetic/mass trace transfers, exchange,
weak-field ratios and quadratic Hessian. Each fault changes a mathematical
input; a clean baseline precedes failed-assertion mutation detection.

```
sage -python tests/channel-swings/k1864_causal_scalar_tensor_completion.py
python3 tests/channel-swings/k1864_causal_scalar_tensor_completion_probe.py
```

Inline hostile review rejects four overclaims: retarded response is not a
symmetric metric-only Hessian; no explicit Jordan kinetic term does not mean
no scalar; scalar-flat R=0 does not imply Riemann-flat or pure GR; and a
positive finite patch is not an all-space positive solution. Homogeneous
scalar waves, matter pressure, source-model admissibility and altered
boundary data remain explicit. No independent-person, proof-assistant or
external peer verification is claimed.

This resolves one missing action candidate and follows it through two
independent requirements on the same completion: causal response survives,
pure-GR matter response and global positive flat vacuum screening fail at the
stated scopes. The next useful native task is the actual I1B distortion and
observation adapter. A different reverse-selected completion must explain
its traceful matter response and global initial/boundary data; merely
increasing omega or inserting a scalar mass changes the projector as above.
