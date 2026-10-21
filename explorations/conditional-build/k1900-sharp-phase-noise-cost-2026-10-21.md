---
title: "K1900: Sharp energy costs for arbitrary phase noise"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional massless R1 channel-phase optimization; no universal thermodynamic bound or scalar 3D transfer
scripts:
  - tests/channel-swings/k1900_sharp_phase_noise_cost.py
  - tests/channel-swings/k1900_sharp_phase_noise_cost_probe.py
---

# K1900: Sharp energy costs for arbitrary phase noise

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: sharp arbitrary-law coherence cost and simultaneous neutral-dephasing constructions with necessary history rank
carrier: rank-four massless R1 target with two components per transport direction LAYER=toy CHIRALITY=N/A
pairing: positive L2 and fixed free polarized CAR sea ON=conditional_massless_target
real_structure: real phase profiles and classical probability laws
grading: CAR parity and right-left transport channels
action_owner: repository-construction -- supplied smooth scalar spacetime potential and noise law
target: energy versus bounded neutral coherence optimization MAP-TYPE=intertwiner
```

## 1. What is new relative to the binary bound

[K1898](k1898-stochastic-pulse-energy-coherence-2026-10-21.md) gives Gaussian
and binary bounds but does not optimize over probability laws or profiles.
Here arbitrary random real phases satisfy a sharp lower bound; finite
smearings and several simultaneous coherence demands have explicit recovery
constructions. A binary optimum for ONE coherence need not optimize complete
three-mode dephasing.

Use h=-ic diag(1,1,-1,-1) partial_x on L2(R,C4), with c=1/24.
Let a random compact smooth scattering phase Phi_r multiply each direction
by exp(-iPhi_r). Its positive free sea energy is exactly

```
Ebar = c/(2pi) sum_r E[||Phi_r'||_2^2].               (1)
```

Equation(1), including multiplicity two and particles plus holes, is reused
from K1898. The probability law and the free sea are imported. SC-META-53
remains UNCERTAIN; SC-OP-04 ASSERTS candidate grammar and SC-MAS-01/
SC-CHI-02 ASSERT a stylized mass toy, not this reduction. LT-SM8, LT-GR6b,
AC-F1, source and canon verdicts do not move.

## 2. A global arbitrary-law inequality, including wrapped phases

For any real random variable X with finite second moment and
z=E exp(iX), eta=|z| in[0,1],

```
E X^2 >= [acos eta]^2.                              (2)
```

The bound also holds trivially with infinite left side. For a specified REAL
signed z one can strengthen it to [acos z]^2 with angle in[0,pi].
For modulus only, (2) is sharp: X=+/-acos eta equally likely attains it.
No Gaussian assumption or small-phase approximation is used.

Proof: define F(u)=cos sqrt(u) for 0<=u<=pi^2, and F(u)=-1 thereafter.
F is convex and nonincreasing. In the first interval
F''(u)=(sin x-x cos x)/(4x^3)>=0, x=sqrt u, because the numerator's
derivative is x sin x>=0 on[0,pi]; the limiting derivative at pi^2 is0,
matching the constant extension. Also cos X>=F(X^2) for EVERY real X.
Jensen gives Re z>=F(E X^2). If E X^2<pi^2, invert the decreasing cosine:
E X^2>=[acos(Re z)]^2>=[acos |z|]^2. Otherwise the conclusion is immediate.
This proof explicitly controls phases outside the principal interval.
For 0<acos eta<pi/2, equality requires |X| constant and equal +/- weights;
eta=0 uses +/-pi/2. eta=1 has the zero-cost realization X=0.
A deterministic nonzero phase has |z|=1 and incurs energy without coherence
loss; signed visibility and loss of modulus must not be confused.

## 3. Spatial cost and bounded observable version

For z<w, d=w-z, put X=Phi_r(w)-Phi_r(z). Cauchy--Schwarz and(2) imply

```
Ebar >= c/(2pi d) [acos |E exp(iX)|]^2.               (3)
```

The other transport direction contributes nonnegative energy. For a genuine
bounded neutral observable a*(f0)a(f1), require Phi_r to be constant on the
supports of normalized disjoint compact packets f0,f1. Let g>0 be the gap
between their support intervals, and let X be their plateau phase difference.
Then its scattering channel multiplies the observable by E exp(iX), and
(3) holds with d replaced by g. This is an exact scalar multiplier of a
bounded CAR observable, not an unsmeared field claim.

This bound is the INFIMUM in the following explicitly specified class:
smooth compact phase profiles, arbitrary classical laws, arbitrary
outer support size, fixed plateau supports and gap. Take theta=acos eta,
X=+/-theta equally likely; interpolate linearly over the gap and remain
constant on the packet intervals. The derivative cost of the connecting
ramp is theta^2/g. Return the exterior constants to zero over tails of length
L; their extra cost is O(theta^2/L). Smooth the corners in shrinking regions
inside the gap/tails, retaining exact plateau values, with derivative costs
converging to the piecewise-linear value. The other channel has zero phase.
This supplies smooth compact approximants with exact visibility eta and costs
converging to(3). Section4.1 makes them realizable by a common scalar potential
with a zero-integral adjustment that costs arbitrarily little additional energy. There is generally no compact smooth minimizer: equality
would demand constant slope up to flat plateaux and zero-cost nonzero tails.
The infimum is not a finite-support minimum or a fixed-duration amplitude bound.

## 4. These profiles have actual causal finite-duration generators

To realize independently specified Phi_+,Phi_-, choose a real smooth g(t)
supported strictly inside(0,T) with integral1 and the Hermitian multiplication
potential

```
V(t,x)=g(t)[P_+^dir Phi_+(x-ct)+P_-^dir Phi_-(x+ct)]. (4)
```

P_r^dir are the constant transport-direction projectors, NOT spectral
positive-energy projections. Along x=z+rct, the integrated potential is
Phi_r(z), giving precisely the scattering phases used above. Every history
is smooth compact in spacetime, gives unitary evolution on H1, preserves
characteristic speed c and has finite energy by(1). A finite mixture is a
normal causal CAR channel. The radius of the constructed support can grow
with the recovery sequence; T can be fixed but no fixed amplitude or spatial
support constraint is imposed.

Equation(4) is channel-diagonal MATRIX potential, generally not K1898's
common scalar potential. By itself it proves sharpness only in an enlarged
class. The following separate construction removes that extra assumption for
the one-direction costs used here. It does not infer arbitrary independent
channel control or repair the three-dimensional energy divergence.

### 4.1 Released scalar steering, with its exact integral constraint

For any scalar V, the two characteristic phases have equal spatial integral:
Fubini and translation invariance give integral Phi_+=integral Phi_-=integral V.
Thus Phi_+=phi, Phi_-=0 requires integral phi=0. This is an actual range
condition, not a reason to assume all phase profiles are inaccessible.

Let phi be real compact smooth with integral zero. Define a compact smooth
antiderivative f with -2c f'=phi. With the same g above put

```
F(t,x)=g(t)f(x-ct),
V(t,x)=(partial_t-c partial_x)F
      =g'(t)f(x-ct)-2c g(t)f'(x-ct).                 (4a)
```

On a LEFT-moving characteristic V is exactly the time derivative of F, whose
endpoint values vanish, so Phi_-=0. On a RIGHT-moving characteristic,
integral V= f(z) integral g' -2c f'(z) integral g=phi(z).
This is an exact real scalar smooth compact spacetime potential at any fixed
T>0. It gives precisely the desired one-direction scattering phase and no
phase in the other direction. No instantaneous pulse limit or altered
transport cone is used. During the pulse the unused direction need not have
zero phase; the assertion concerns the final scattering map.

The zero-integral condition does not raise the infimum for the specified
plateau demands. For any already constructed compact smooth profile phi_0
with integral A, choose a unit-integral compact smooth bump b, put its support
far from the packets and original profile, and add
b_L(x)=-(A/L)b((x-x_L)/L). Its integral is -A and its derivative cost is
A^2 L^-3 ||b'||_2^2. Choose L after each original recovery profile so this
cost tends to zero, with disjoint support ensuring no cross term. Plateau
values and all visibilities are unchanged. Apply(4a) to each finite noise
history. Therefore(3),(5),(7) are sharp infima even for common SCALAR smooth
spacetime potentials, with unrestricted spatial support and amplitude.
This does not establish sharpness for separable V(t,x)=xi(t)theta(x), fixed
support/amplitude, or three-dimensional massive targets.

## 5. Released multi-coherence result

Choose n+1 ordered plateau packets in ONE direction, with gaps g_j>0.
Let adjacent visibilities be eta_j in[0,1]. Applying(2) separately to the
random phase increments Delta_j gives the additive sharp lower bound

```
Ebar >= c/(2pi) sum_(j=1..n) (acos eta_j)^2/g_j.       (5)
```

Use INDEPENDENT increments Delta_j=+/-theta_j, theta_j=acos eta_j,
set plateau phases cumulatively and use the same smooth ramp/tail recovery.
Then adjacent coherence is eta_j exactly and nonadjacent coherence is

```
eta_(k,l)=product_(j=k+1..l) eta_j.                   (6)
```

Thus all nearest-neighbor lower bounds can be approached simultaneously in
the scalar class constructed by(4a). One random global phase on all packets changes no neutral
coherence, and can be used to reduce tail cost but cannot lower ramp cost.
The matrix C_kl=E exp(i(Phi_l-Phi_k)) is positive semidefinite with unit
diagonal, since it is a Gram matrix of random phase vectors. Arbitrary
pairwise requests need not be jointly feasible: C01=C12=1 forces the first
three phase factors equal almost surely and hence C02=1, ruling out C02=0.
Pairwise lower bounds alone are not a complete feasibility test.

### Three completely dephased modes: binary noise is insufficient

For three packets set eta_1=eta_2=0, so theta_1=theta_2=pi/2.
Four equiprobable independent sign histories give C=I_3 by(6), and

```
inf Ebar = c pi/8 (1/g_1+1/g_2).                     (7)
```

A binary mixture has Gram rank at most2 and cannot produce I_3 at all.
More generally M deterministic histories have Gram rank<=M; complete
n-mode phase dephasing requires at least n histories.
Three histories CAN dephase three modes (third-root phase vectors), but
cannot achieve the lower bound(7). At equality in the phase-law bounds,
Delta_1 and Delta_2 must each be +/-pi/2 with balanced marginals. Write the
four sign probabilities p++,p+-,p-+,p--. C02=0 then requires same and
opposite signs to have equal total probability; together with the marginals
this forces all four probabilities=1/4. Hence an optimal phase law has at
least four distinct increment pairs. This is a statement about the sharp
phase-law equality, not a quantitative gap for every three-history recovery
sequence. We do not claim the latter without a separate compactness argument.

A useful three-history control uses plateau phases (0,0,0),
(0,2pi/3,-2pi/3), (0,-2pi/3,2pi/3), taking equivalent unwrapped lifts
on each history to minimize adjacent increments: the latter two can instead
be (0,2pi/3,4pi/3) and (0,-2pi/3,-4pi/3).
The adjacent mean square is 8pi^2/27, versus pi^2/4 for the optimal four
histories. For equal gaps this control costs 32/27 times(7). Its nonadjacent
phases still yield I_3; changing lifts cannot alter coherence. We state a
control, not the optimum within all three-history laws.

## 6. What the sharp result changes

Complete coherence loss has finite infimum in this conditional class. The
Gaussian cost -log eta diverges at eta=0 because a finite-variance Gaussian
characteristic function never vanishes; it is not a universal cost of
complete decoherence. For 0<eta<1 the binary arbitrary-law optimum is below
the Gaussian cost with the same spatial lower-bound factor. This is an
explicit operational distinction between noise laws, not thermodynamics.
The n-mode construction also shows why minimizing one coherence and then
reusing one common binary clock can fail for a larger observable algebra.

Remaining questions have new constraints: fixed spatial support/amplitude,
separable time-space scalar controls, nonadjacent prescribed coherence matrices,
physical bath selection, and a native GU observation map. The exact noise
law and scalar generator are imported; no 3D transfer, physical
vacuum selection, native prediction, novelty or external acceptance is claimed.

## 7. Verification

The analytic convexity and smooth recovery arguments carry the continuum
optimization. Producer and separate probe check derivative signs, phase
probabilities, PSD/rank, finite CAR dephasing, ramp costs, transport and
coefficient controls; mathematical mutations follow a passing baseline.
Hostile review checks signed versus modulus visibility, phase wrapping,
infimum versus attained minimum, finite packet plateaux, channel-diagonal versus scalar potentials and their integral range condition,
pairwise versus joint feasibility, and history rank.
