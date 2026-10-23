---
title: "K1961: Curved conservative connections on the fixed positive core"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional raw-core dynamics; no source-selected interaction or physical mass
scripts:
  - tests/channel-swings/k1961_curved_core_connections.py
  - tests/channel-swings/k1961_curved_core_connections_probe.py
---

# K1961: Nonzero curvature survives the mass obstruction

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
result: actual noncommuting core-preserving rotations, curved conservative evolution and flat global holonomy
carrier: K1951 conditional real1920 with fixed positive128 core LAYER=toy CHIRALITY=N/A
pairing: inherited positive matrix H and spatial L2 energy ON=fixed_core
real_structure: real Cl(7,7); complexification only for Fourier spectral analysis
grading: intrinsic Clifford grading, not observed chirality
action_owner: repository-construction -- modified zero-southeast raw operator
target: observed-four-direction covariant evolution MAP-TYPE=intertwiner
```

## 1. Actual raw construction

[K1959](k1959-full-direction-even-connection-2026-10-22.md) excludes a
conservative anticommuting Dirac mass in its tensorial connection class. It
also exhibits a removable one-generator potential. That does not classify
all surviving connections as flat. Here is a curved counterexample to that
possible extension, using the SAME raw map and fixed positive core.

Let J,L,H,C_i be K1951/K1959's injection, left inverse, positive energy and
three observed principal matrices. Write A_i=D_0^(-1)D_(7,8,9). For
(a,b)=(1,2),(2,3),(1,3), construct the actual raw tensorial action

    Q_ab=I15 tensor(gamma_a gamma_b)+V_ab tensor I128,
    (V_ab)_ab=2, (V_ab)_ba=-2,
    R_ab=L Q_ab J.

Exact raw reconstruction proves

    Q_ab J=J R_ab,   A_i Q_ab J=J C_i R_ab,
    [C_i,R_ab]=0,    H R_ab+R_ab^T H=0,    R_ab^2=-I.

The indices1,2,3 are positive Clifford directions in this declared convention.
Writing R=R_12, S=R_23 and T=R_13 gives

    RS=T, SR=-T, T^2=-I, [R,S]=2T.

These are actual induced matrices, not freely planted quotient coefficients.
The real span of R,S,T is a non-Abelian compact three-dimensional Lie algebra.
The calculation proves its faithful action on this core; it does not classify
the full91-dimensional preserving image from K1959.

## 2. Curvature, energy and the missing mass gap

For arbitrary real coefficient functions let each A_mu be a linear combination
of R,S,T. Use the convention nabla_mu=partial_mu+A_mu and the equation

    nabla_t psi=sum_i C_i nabla_i psi,
    partial_t psi=sum_i C_i partial_i psi+V psi,
    V=sum_i C_i A_i-A_0.                              (1)

The raw realization takes the corresponding tensorial coefficients in observed
directions7,8,9 and the negative temporal coefficient in direction0. Linearity
of the checked identities proves raw-core invariance for these functions.
Every term of V is H-skew: C_i is H-self-adjoint and commutes with every A_mu.
Thus arbitrary such prescribed connections preserve the positive L2 energy.
They do not thereby satisfy a source field equation or a dynamical gauge action.

Take constant A_1=-R,A_2=-S,A_3=A_0=0. Its connection curvature is

    F_12=partial_1 A_2-partial_2 A_1+[A_1,A_2]=2T,
    F_12^2=-4I, rank F_12=128.

It cannot be gauged to the zero connection on an open set: curvature transforms
by conjugation, so nonzero curvature cannot become zero. This statement is about
connection/frame gauge equivalence, not every conceivable nonlocal equivalence
of evolution operators. A finite loop control uses the exact unitary rotations
U=(3I+4R)/5 and W=(3I+4S)/5; UWU^(-1)W^(-1) is nonidentity.

Curvature does NOT supply a relativistic mass gap. At zero momentum the
constant evolution coefficient V=-C_1 R-C_2 S satisfies

    V^2=-2I+2 C_1 C_2 T, rank V=64.

The involution C_1 C_2 T has both signs, so64 zero modes survive. On the torus
these include constant modes; on R3, localized large-scale wave packets give
spectral values approaching zero. This explicit curved example remains gapless.
It also fails the anticommuting Dirac-mass equations, consistently with K1959.

## 3. Common domain and causal propagation

On R3 or the flat three-torus, assume the real connection coefficients are
continuous in time with values in W^(1,infinity) in space, locally bounded in
that norm on every finite time interval. These assumptions are part of the
construction, not consequences of the source. The free generator sum C_i partial_i
is skew-adjoint in the H-inner product with domain H1, because the checked
Clifford relations give (sum C_i k_i)^2=|k|^2 I.

Duhamel iteration with the bounded multiplication V converges on each finite
time interval: the j-th term is bounded by (integral ||V||)^j/j!.
Uniqueness and reverse-time construction give an invertible evolution. Taking
the H-inner product of(1), first on smooth data and then by density, gives
zero derivative of the L2 energy, so this evolution is unitary. Differentiating
in space gives an inhomogeneous term (partial_i V)psi; its boundedness and
Gronwall's inequality preserve H1, with the same argument backward in time.
This proves a strongly continuous unitary propagator with common H1 domain.

For a real unit normal n, H-self-adjoint C(n)=sum n_i C_i has eigenvalues
plus/minus1, hence |psi^* H C(n)psi|<=psi^*H psi. The local energy identity is
partial_t(psi^*H psi)=div(psi^*H C psi); the zero-order term cancels pointwise.
Integrating over an exterior expanding cone proves speed at most1. Approximation
and the energy estimate extend this to H1 and L2 data. Thus nonzero prescribed
curvature is compatible with positive causal evolution in this model.
Neither this linear PDE theorem nor its finite matrices construct the source
interacting positive physical quotient.

## 4. Flat holonomy is a separate global obstruction

On the torus of periods2pi, take A_1=aR, all other A_mu=0. Curvature vanishes.
Locally G(x)=exp(-a x_1 R) removes the connection, but G is periodic exactly
when a is an integer, since R^2=-I. The loop holonomy exp(-2pi aR) therefore
prevents a single-valued periodic gauge removal for noninteger a.

After complexification, R has eigenvalues i sigma, sigma=plus/minus1, and
commutes with the C_i. Fourier modes k in Z3 then have evolution frequencies

    omega=plus/minus sqrt((k_1+sigma a)^2+k_2^2+k_3^2).

Both signs occur: the commuting Clifford representation on each R-eigenspace
contains the two signs of any nonzero C(k). The spectral distance from zero is
dist(a,Z), in particular1/2 at a=1/2. This is a finite-volume holonomy gap;
on R3 continuous k_1 cancels sigma a, so it is not a local Dirac mass. K1959's
periodic gauge theorem is unchanged: phi=a x_1 is not a single-valued torus
function when the required gauge is nonperiodic. Global domain conditions
matter even for a flat connection.

## 5. Evidence, source scope and remaining question

The producer checks32 exact matrix identities. The separate probe rebuilds
the raw Clifford matrices with signed bits, reconstructs J,L and the opposite
side time inverse, and checks30 algebraic identities including the64-dimensional
zero-frequency kernel. Four actual input faults are detected after a clean
baseline: generator reversal, half the vector-slot action, a commuting
replacement, and an energy-symmetric potential. Pin/identity checks are
reporting checks. The continuum propagation, domain and Fourier conclusions
are the analytic arguments above, not consequences of a check count.

Strongest overclaim: calling the constructed connection source-selected or
interpreting curvature as mass. Strongest contrary witness: this curved
connection has zero-frequency modes, while a flat torus connection can have
a global gap. Weakest transfer seam: raw invariance and common domain; both
are separately stated and checked/proved. Internal review found no remaining
contradiction within this scope; no external expert or formal proof acceptance
is claimed.

SC-OP-04 ASSERTS a candidate four-field grammar; SC-MAS-01 ASSERTS a stylized
constant-curvature mass. SC-GEO-55 ASSERTS displacement from gauge-rotated
Levi-Civita; SC-META-53 remains UNCERTAIN on unbounded-spectrum handling.
Nothing here identifies these prescribed connections with those source objects.
The source full20/barred maps, physical quotient, source background and mass
observable remain open; LT-SM8/LT-GR6b/AC-F1 do not change.
The next useful discrimination is the actual source-compatible connection or
changed-input map and its physical demand, not another example of a freely
chosen conservative potential.
