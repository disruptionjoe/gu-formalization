---
title: "K2060: Positive-energy preservation, localization and asymptotic sectors"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional changed observed graph; no source-selected physical quotient or quantization
scripts:
  - tests/channel-swings/k2060_positive_energy_localization.py
  - tests/channel-swings/k2060_positive_energy_localization_probe.py
---

# K2060: Positive-energy preservation, localization and asymptotic sectors

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
result: fixed positive-energy coefficient classification, exact mixing and localization/scattering limits
carrier: complexification of real1408 observed graph with both ambient64 halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed universal positive Hermitian metric P and massive spectral projectors ON=declared_observed_graph
real_structure: real skew coefficient algebra, complex Hilbert evolution and independent dual anti-involution
grading: Hamiltonian energy signs, not source field parity or family count
action_owner: repository-construction -- K2038 changed coefficient class and K2058 universal dynamics
target: invariant positive-energy Hilbert subspaces and local coefficients MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] In K2058's actual observed graph, constant
allowed perturbations preserve a fixed massive positive-energy sector exactly
when they commute with all spatial matrices and the mass matrix. This reduces
the compatible real Lie algebra from dimension169984 to10624. Even survivors
need an additional operator-norm bound for nonnegative restricted Hamiltonian.
Nonconstant bounded periodic or integrably decaying local coefficients cannot
preserve that fixed sector. An allowed mass pulse can transfer a mode entirely
to the negative sector. A compactly supported nonzero massive positive-energy
state does not exist on R3. Time-integrable potentials instead admit transported
incoming/outgoing subspaces; these need not agree.

These are conditional Dirac-type results, not a source-selected physical
quotient, source correction, CAR quantization or validation of GU.

## 1. Fixed object, signs and prior-work collision

Freeze [K2058](k2058-universal-positive-dynamics-2026-10-25.md)'s real1408
graph and one of its universal fixed positive metrics P. The real symmetric
C_j anticommute and square to I. The real skew M squares to-I, anticommutes
with each C_j and commutes with the fixed nondegenerate skew kinetic T.
Allowed perturbations W obey W^T=-W and [T,W]=0. Put

    beta=-iM, H_mu(p)=C.p+mu*beta, E_mu(p)=sqrt(|p|^2+mu^2),
    Pi_+(p)=(I+H_mu(p)/E_mu(p))/2, mu>0.

The PDE with N=mu M+W has Hamiltonian H_mu+V, V=-iW. All these operators
commute with P. The fixed isometry P^(1/2) reduces all assertions below to
the ordinary Hilbert norm, with no varying-metric defect.

[K1896](k1896-local-phase-vacuum-boundary-2026-10-21.md) already owns scalar
phase-kick mixing, Dirac-sea nonimplementability and its smooth-pulse repair
in a rank4 model. We do not repeat those as new results. The present advance
is the complete coefficient classification in the actual1408 graph, the
local-multiplier rigidity proof, energy bound, mass-pulse formula and explicit
asymptotic-subspace alternative. Free localization is known territory; see
[Barat and Kimball](https://arxiv.org/abs/quant-ph/0111060),
[Hegerfeldt](https://arxiv.org/abs/quant-ph/9806036), and
[Beck](https://arxiv.org/abs/2305.18118). The proofs below establish only their
stated hypotheses; no theorem or novelty is imported from these references.

SC-OP-04 ASSERTS candidate four-independent-field grammar; SC-OP-05 remains
UNCERTAIN about a southeast rival; SC-META-53 remains UNCERTAIN about
positivity; SC-META-56 DISAVOWS an odd-action prerequisite. None selects this
mass, metric, positive sector, parity or quotient. LT-SM8/LT-GR6b unchanged.

## 2. Complete constant-coefficient preservation and dimension

For constant allowed W, the fixed free sector is preserved for all times iff

    [W,C_j]=0 for j=1,2,3 and [W,M]=0.                  (1)

A self-adjoint Hamiltonian preserves a closed subspace for its two-sided
unitary group iff it commutes with its orthogonal projector. Thus preservation
is [W,Pi_+(p)]=0 for every p. Sending p=Rn to infinity gives [W,C.n]=0;
evaluating at p=0 gives [W,beta]=0. Conversely these relations commute with
every Pi_+(p). The same argument on a torus uses lattice rays and p=0.

Here is the complete real dimension, not just an example subalgebra. The four
real Clifford generators C1,C2,C3,M generate Cl(3,1)=M4(R). An explicit model
is X tensor I, Z tensor X, Z tensor Z, Z tensor J, where X=[[0,1],[1,0]],
Z=diag(1,-1), J=[[0,1],[-1,0]]. Its16 words have rank16. The real T-frequency
blocks have dimensions576,576,64,64,64,64, inherited from K2038/K2058. Each
is R4 tensor R^m with m=144,144,16,16,16,16. Since T commutes with the full
Clifford algebra, its normalized complex structure acts only on multiplicity.
The Euclidean-skew commutant of both Clifford and this structure is therefore

    u(72) + u(72) + u(8) + u(8) + u(8) + u(8),
    dimension 2*72^2+4*8^2=10624.

The compact involution is justified by the orthogonal Clifford representation:
C_j are symmetric and M skew; equivalent copies can be chosen orthogonally,
so skewness reduces to the ordinary multiplicity inner product. This removes
159360 of the prior169984 directions, without changing that prior algebra's
valid norm-conservation claim. Raw1920-to1408 compression and T multiplicities
are hash-pinned inherited inputs, not a new dense exhaustive calculation.

## 3. Preservation still does not guarantee nonnegative energy

A constant survivor has Hermitian V=-iW on the multiplicities. Since W is
real skew, its eigenvalues occur in conjugate pairs and V's extreme eigenvalues
are plus/minus ||W||. The positive free sector has both Clifford-positive
spin degrees for every multiplicity eigenvector. Hence the spectral infimum of
H_mu+V on that sector is exactly

    mu-||W||.

It is nonnegative iff ||W||<=mu; it has a uniform positive gap iff ||W||<mu.
On R3 the infimum at p=0 need not be an L2 eigenvalue; on the torus p=0 is an
actual mode. This is a norm ball inside the survivor algebra, not another Lie
subalgebra. Conserved positive norm alone did not supply this energy bound.

## 4. Rigidity of local multipliers

Let V(x) be a bounded Hermitian periodic matrix multiplier on the3-torus.
Alternatively on R3 assume V(x)=V0+W0(x), with W0 in L1 intersect L-infinity.
If it preserves the fixed free positive projector, then V is constant and
commutes with all C_j and beta. This includes the admitted local coefficient
class; the proof actually permits arbitrary Hermitian matrix multipliers.

For any nonzero Fourier wave vector k, its coefficient A satisfies

    Q(p) A=A Q(p-k), Q(p)=H_mu(p)/E_mu(p).

This follows from the kernel of the projector commutator; on R3 continuity
of the Fourier transform turns almost-everywhere equality into equality.
Along p=Rn, the leading limit gives [A,C.n]=0. The next coefficient is

    mu[beta,A]+A(C.k-(n.k)C.n)=0.                       (2)

Take n parallel k to get [beta,A]=0, then n perpendicular k to get A C.k=0.
Since (C.k)^2=|k|^2 I, A=0. On a torus, integer ray directions are dense;
parallel/perpendicular lattice directions suffice for these limits, with
continuity filling the leading commutators. On R3 the continuous transform
of W0 vanishes off zero and therefore at zero too. Thus W0=0 almost everywhere.
The zero Fourier coefficient obeys the constant classification.

For autonomous self-adjoint H, preservation for all positive and negative
times is equivalent to this commutation. For nonautonomous coefficients,
preservation by EVERY U(t,s) implies commutation almost everywhere in time
by differentiating the interaction-picture evolution. Preservation at one
isolated final time does not imply this classification. We make no claim for
arbitrary bounded nonperiodic multipliers outside the stated R3 class, or for
potential-dependent moving projectors.

## 5. Allowed mass pulse: exact and quantitative mixing

For W=lambda M during a time interval, V=lambda beta. The full Hamiltonian
is H_(mu+lambda). Clifford anticommutation gives, for any u in Pi_+(p),

    ||Pi_- exp(-it H_(mu+lambda)(p))u||^2 / ||u||^2
      = lambda^2 |p|^2 / (E_mu(p)^2 E_(mu+lambda)(p)^2)
          * sin^2(E_(mu+lambda)(p)t).                  (3)

At a zero denominator take the continuous sine quotient. Indeed the off-block
part of H_(mu+lambda) is lambda Pi_- beta Pi_+, whose squared compression is
lambda^2 |p|^2/E_mu^2 times Pi_+. This proves(3) for every positive vector,
not just a selected polarization. It also shows p=0 has no mixing unless
one changes the definition of the sector after the pulse.

With lambda=-2mu and |p|=mu the coefficient is1. At time pi/(2sqrt(2)mu),
transfer is complete. This mass reversal is still in the admitted norm-
conserving class. A torus requires an available momentum of that magnitude;
on R3 a plane wave is not L2, but normalized packets concentrated near that
momentum approach unit transfer. This is a conditional counterexample, not
a claim that a GU interaction realizes such a pulse.

More generally for bounded time-dependent V, let
b(t)=||Pi_- V(t) Pi_+||. After removing the two diagonal unitary blocks, an
initial unit positive vector has negative norm y satisfying
D^+ y<=b sqrt(1-y^2), with the integrated version at zeros. Thus

    ||Pi_- U(t,s)psi_+|| <= sin(min(pi/2, integral_s^t b(r)dr))||psi_+||,

for t>=s. This improves the elementary integral bound when the integral is
small. The reversal example at the chosen mode saturates it before full
transfer: its diagonal blocks vanish and b=sqrt(2)mu. The bound needs only
bounded perturbations of the free group, not spatial H1 regularity.

## 6. Compact-support obstruction on R3

No nonzero compactly supported L2 vector lies entirely in either massive free
energy sector. Compact support implies L1 and an entire Fourier transform.
Fix real transverse momenta p2,p3 and write F(z)=Fourier(psi)(z,p2,p3),
G(z)=H_mu(z,p2,p3)F(z). Every component is entire. On real z the projector
condition gives G=plus/minus sqrt(z^2+c) F, c=mu^2+p2^2+p3^2>0. Squaring each
component and using analytic continuation gives

    G_j(z)^2=(z^2+c)F_j(z)^2.

At the simple root z=i sqrt(c), a nonzero entire F_j gives an odd zero order
on the right, while a square has even order. This is impossible. Hence each
F_j is identically zero, for every real transverse pair, and psi=0.
Continuity extends the initial almost-everywhere Fourier identity. The proof
is not valid for a massless zero-transverse slice, which is why mu>0 is fixed.

K2058's full two-sign evolution and its finite propagation statement remain
intact. Positive projection is nonlocal; this support obstruction supplies no
superluminal signaling claim. The periodic space has no analogous compact-
support conclusion stated here.

## 7. Released alternative: transported asymptotic sectors

Assume integral_R ||V(t)|| dt<infinity on the Hilbert space, with the admissible
bounded Hermitian potentials above. K2058 gives the unitary propagator U(t,s).
Duhamel bounds imply the operator-norm Cauchy property of

    Omega_+=lim_(t->+infinity) exp(itH_mu) U(t,0),
    Omega_-=lim_(t->-infinity) exp(itH_mu) U(t,0).

The same estimate for adjoints implies these norm limits are unitary, rather
than merely isometries. Thus every L2 state scatters at both ends. Define

    P_asym,+/- (0)=Omega_+/-^* Pi_+ Omega_+/-,
    P_asym,+/- (t)=U(t,0) P_asym,+/- (0) U(0,t).

These are exact transported positive incoming/outgoing subspaces. Their
operator-norm distance from the free Pi_+ is at most twice the corresponding
future/past tail integral of ||V||. This follows by comparing the asymptotic
interaction-picture unitary based at t with identity and conjugating Pi_+.
They depend on the potential and are generally nonlocal. They are not the
instantaneous positive spectral projector of H(t), and their energy need not
be pointwise positive at intermediate times.

The scattering operator S=Omega_+ Omega_-^* need not commute with Pi_+.
A finite-duration pulse from(3), with free propagation outside, demonstrates
nonzero off-diagonal scattering. Smooth time profiles can approximate it in
L1 operator norm; K2058's perturbation estimate preserves nonzero transfer.
Consequently the incoming and outgoing transported positive sectors need
not be the same. This constructive alternative does not automatically solve
a common physical-state domain or CAR implementability problem.

## 8. Reproduction, hostile checks and limits

The producer verifies50 exact algebra/projector controls, including actual
128-spinor factors, the16-word real Clifford basis and rational pulse cases.
The separate same-author probe uses a complex Pauli realization and47 exact
controls, rejecting six targeted mathematical faults. The initial probe's
unsimplified symbolic invertibility expression was repaired by simplification;
that was a test-harness issue, not a changed mathematical result.

Written proofs establish dimension exhaustiveness, local rigidity, localization,
leakage and asymptotic existence; finite matrix tests alone cannot do so.
Hostile review distinguishes real from complex dimension, norm from energy,
fixed from transported projectors, torus modes from R3 packets and operator-
norm limits from strong isometries. No independent specialist, proof-assistant
or novelty certification. Run both named scripts; producer --write rebuilds
the JSON certificate. Raw graph/source/physics/canon records are unchanged.

The fixed-sector local-coefficient question is resolved on the stated classes.
A source-selected dual, field parity and physical quotient remain additional
work; no theorem here supplies those data. Future nonlinear or nonintegrable
interaction claims require genuinely new estimates and explicit domains.
