---
title: "K2042: Exponential instability and complete characteristic dynamics of the sextic model"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed classical action and selected transport sector only; no general three-dimensional PDE or physical-fermion conclusion
scripts:
  - tests/channel-swings/k2042_sextic_transport_instability.py
  - tests/channel-swings/k2042_sextic_transport_instability_probe.py
---

# K2042: Exponential instability and complete characteristic dynamics of the sextic model

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


```gu-typed-objects
result: nonlinear equilibrium instability, complete transfer orbit and global characteristic solutions
carrier: K2038 real1408 graph with two selected complex eigenlines LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Euclidean graph norm and skew kinetic T ON=declared_graph
real_structure: real commuting fields; complex coordinates represent orthogonal real planes
grading: sign-even sextic polynomial, not Grassmann parity
action_owner: repository-construction -- fixed K2038 action and full variational lift
target: causal transport and stability demands on the specified nonlinear model MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The norm-preserving sextic from
[K2040](k2040-nonlinear-resonance-selection-2026-10-24.md) has a nonzero
equilibrium with exponential linear instability and an explicit finite-amplitude
escape orbit. Nevertheless the homogeneous flow and a nontrivial spatial
characteristic sector are globally complete. This separates positive norm,
causal propagation, completeness and perturbation stability on one fixed model.
It supplies a finite-energy spatial example, not only a homogeneous diagnostic.

## 1. Fixed model and actual equations

Keep [K2038](k2038-observed-action-compression-2026-10-24.md)'s real graph,
positive norm, skew T, and symmetric spatial Clifford matrices Cj commuting
with T. Choose one complex coordinate z in frequency1 and w in frequency2.
In orthogonal real coordinates, J is multiplication by i and T=diag(J,2J).
Set V=Re(z^2 conjugate(w)^4), with zero potential dependence on other coordinates.
The reduced action has equation Du=-T^-1 grad V. Direct real differentiation gives

    z_dot = 2i conjugate(z) w^4,
    w_dot = 2i z^2 conjugate(w)^3.                         (1)

These are homogeneous equations; D replaces the dot in the characteristic
sector below. Their total norm |z|^2+|w|^2 is conserved. This is the actual
inverse-frequency convention, not a guessed complex Hamilton equation.
The full variational extension in K2038 section5 applies to this polynomial:
it has degree6 and identically zero auxiliary-auxiliary Hessian. Its inherited
proof is reused; the ambient action is not reselected or recertified here.

SC-OP-04 ASSERTS the candidate independent-four-field operator grammar;
SC-OP-05 is UNCERTAIN about a selected southeast rival. SC-META-53 is
UNCERTAIN about physical positivity, and SC-META-56 DISAVOWS requiring an odd
action as the graded-structure prerequisite. None selects our commuting
one-field reduction. LT-SM8/LT-GR6b, source register, physics ledger and canon
remain unchanged. This is a backward test of stability/causal-domain demands
on an explicitly conditional action, with no physical parity or quantum credit.

## 2. Saddle and nonlinear departure

For every real h>0, z=0,w=h is an equilibrium. Write z=x+iy,w=a+ib.
The exact real Jacobian there is

    [[0,2h^4,0,0], [2h^4,0,0,0], [0,0,0,0], [0,0,0,0]].

The eigenvalues are +2h^4,-2h^4,0,0. A positive eigenvalue alone is not our
nonlinear conclusion: an invariant plane gives an explicit departure.
Put z=exp(i*pi/4) X, w=Y real, X,Y>0. Equation(1) becomes

    X_dot=2 X Y^4,  Y_dot=-2 X^2 Y^3,
    M=X^2+Y^2 constant,  q=X^2/M,
    q_dot=4 M^2 q(1-q)^2.                                (2)

On 0<q<1 define H(q)=log(q/(1-q))+1/(1-q). Then H'>0,
H maps (0,1) onto R, and

    H(q(t))=H(q(0))+4M^2 t.                              (3)

Thus this orbit exists for all real t and transfers from (X,Y)=(0,sqrt(M))
to (sqrt(M),0) asymptotically. There is no finite-time singularity. Near the
initial equilibrium X grows with exponent2M^2; at the other end
Y^2 is asymptotic to1/(4M t). These follow directly from the logarithmic and
simple-pole terms in H, respectively.

Take X(0)=epsilon, Y(0)=sqrt(M-epsilon^2). Its distance from the equilibrium
(0,sqrt(M)) tends to zero, whereas at

    t_epsilon=[H(1/2)-H(epsilon^2/M)]/(4M^2)

its X coordinate equals sqrt(M/2). This proves Lyapunov instability, with
escape time (1/(2M^2))*log(sqrt(M)/epsilon)+O(1) for fixed M. All those
solutions have the same conserved norm. The example is stronger than the
linear-in-time tangent shear of K2038, but does not contradict boundedness.

## 3. A genuine global spatial sector

Fix one spatial direction, with matrix C1. In every T-frequency space,
C1 is a complex-linear self-adjoint involution. Another Cj anticommutes
with C1 and commutes with T, so it is a complex-linear isomorphism between
the +1 and -1 eigenspaces. Both signs therefore occur. Choose the z and w
complex lines above in the SAME sign c=+1 or c=-1 eigenspace. Their real
four-plane is invariant under T and C1, and the gradient of V stays in it.
It need not be invariant under the other Cj: the fields are independent of
the other two spatial variables, so those derivative terms vanish.

On T^3, or R x T^2 with fields depending only on the R coordinate, the full
graph PDE restricted to this plane is exactly

    (partial_t+c partial_x)(z,w)=G(z,w),
    u(t,x)=Phi_t(u0(x-c t)),                            (4)

where Phi is the homogeneous flow of(1). For every smooth bounded initial
profile with bounded derivatives, (4) gives a unique smooth solution in this
sector at every finite positive and negative time. The pointwise norm equals
|u0(x-c t)|, and compact support on R translates exactly. The latter gives
finite L2 norm on R x T^2, with the transverse torus of finite volume.
This is not an L2(R^3) plane-wave claim.

For a quantitative continuation estimate, on |u|<=R the real Hessian of
Re(z^2 conjugate(w)^4) has operator norm at most30R^4: differentiate its six
linear factors twice and bound each of the30 ordered terms by
R^4|v||w|. Since ||T^-1||=1 on the chosen planes,

    |partial_x u(t,x)| <= exp(30R^4|t|)|u0'(x-c t)|.     (5)

The variational integral equation and Gronwall's elementary integral
inequality give(5); higher derivatives solve successive linear inhomogeneous
variational equations with coefficients bounded on the same compact ball.
This proves finite-horizon smooth continuation. It is not uniform-in-time
regularity, scattering, or existence for unrestricted3D data.

At the constant background the spatial Fourier exponents are
-ick+2h^4,-ick-2h^4,-ick,-ick. Growth is bounded in k; this is a genuine
nonlinear instability, not an arbitrarily high-frequency ill-posedness claim.
The torus embeds the homogeneous departure in every usual smooth/Sobolev norm.

## 4. Finite-energy spatial instability

The conclusion need not rely on a nonzero homogeneous background. Choose a
smooth compactly supported real background Y_bg(x) equal to sqrt(M) on an
interval, and z_bg=0. Its exact solution is the translated profile. Choose a
smooth cutoff chi supported where Y_bg=sqrt(M), equal to1 on a smaller interval.
Let X0=epsilon*chi and Y0=sqrt(Y_bg^2-epsilon^2*chi^2) on that plateau,
using Y_bg elsewhere. The definitions agree smoothly; for epsilon small they
approach the background in every fixed smooth/Sobolev norm.

On the smaller interval, every characteristic follows(2) with the same M and
same q0. At t_epsilon its X component is sqrt(M/2). The L2 distance from the
translated background is therefore at least sqrt(M/2) times the square root
of that interval's length (and transverse torus volume). The solutions remain
smooth, bounded, compactly supported in x and norm-conserving throughout.
This establishes nonlinear instability within finite-energy characteristic
data, while preserving causal speed and completeness in that sector.

## 5. Released successor: a forward-global opposite-speed sector

One can also choose the z line in C1=+1 and the w line in C1=-1. The real
phase plane z=exp(i*pi/4)X,w=Y stays invariant under both transport and
nonlinearity. The resulting genuinely two-speed system is

    X_t+X_x=2 X Y^4,   Y_t-Y_x=-2 X^2 Y^3.               (6)

For arbitrary smooth real bounded initial X,Y with bounded derivatives, it
has a global smooth FORWARD solution. To prove this, along each left-moving
characteristic Y has constant sign and nonincreasing absolute value. With
B=||Y0||_infinity and A=||X0||_infinity, right-moving characteristics give

    |Y(t,x)|<=B,  |X(t,x)|<=A exp(2 B^4 t),  t>=0.       (7)

These bounds prevent finite forward-time amplitude blowup. For completeness,
local existence is obtained by the two characteristic integral equations:
on a bounded amplitude ball their polynomial right sides are Lipschitz, so
iteration is a contraction for a sufficiently short time. Spatial derivatives
satisfy the linear characteristic system with coefficient matrix

    [[2Y^4,8XY^3],[-4XY^3,-6X^2Y^2]].

On every finite time interval(7) bounds these coefficients. Summing the two
supremum integral inequalities gives a finite Gronwall bound; higher
spatial derivatives have the same linear highest-order system with bounded
lower-order forcing. Thus the local smooth solution continues over each
finite forward horizon. This is a continuation proof, not inference from
conserved L2 norm alone.

The exact current is

    partial_t(X^2+Y^2)+partial_x(X^2-Y^2)=0.

Compact support propagates inside speed-one cones, so on R x T2 such data
remain finite energy with conserved total norm. This does not identify the
solution with independently transported homogeneous orbits: characteristics
of the two fields now intersect. The monotone component is the extra fact
that closes forward continuation. Reversing time reverses that monotonicity;
no backward-global result for this opposite-speed sector, no arbitrary phase
result, and no unrestricted3D global theorem is claimed.

## 6. Verification and remaining scope

The producer differentiates the real sextic, verifies norm cancellation,
computes the equilibrium Jacobian and Fourier determinant, derives(2)-(3),
and verifies the two-speed derivative coefficients. Forward continuation
uses the explicit monotonicity/characteristic argument in section5.
The separate checker reconstructs derivatives by exact polynomial interpolation
of the original complex product using rational arithmetic:19 polynomial
fixtures,48 Jacobian entries,3 transfer-plane fixtures and4 primitive fixtures.
The continuum and all-time statements are proved above, not by those samples.
Four faults alter a force coefficient, saddle sign, reported growth coefficient
and the actual kinetic frequency; the last produces a nonzero norm source.
The growth-coefficient fault checks consistency with the independently computed
Jacobian. Clean baselines precede faults. Raw graph/Clifford identities are
hash-pinned K2038 reuse, not a new full-matrix replay.

Same-author derivation and separate implementations are internal checks, not
external specialist or proof-assistant certification and not a novelty claim.
The strongest overclaim would be replacing the invariant spatial sector with
all3D data or treating real commuting fields as source fermions. Neither occurs.
The next mathematical fork is arbitrary relative phases in the opposite-speed
system, its backward-time continuation, or transverse perturbations; the next source fork is the actual
independent-dual/parity and physical-observation bridge. Norm conservation
alone can no longer be used to promise nonlinear stability of this sextic.
