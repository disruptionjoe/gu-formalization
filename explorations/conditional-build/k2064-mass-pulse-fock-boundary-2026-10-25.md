---
title: "K2064: Mass pulses, excitation density and the fixed-sea boundary"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive1408 graph and supplied spectral or CAR criterion only; no GU physical quotient or novelty claim
scripts:
  - tests/channel-swings/k2064_mass_pulse_fock_boundary.py
  - tests/channel-swings/k2064_mass_pulse_fock_boundary_probe.py
---

# K2064: Mass pulses, excitation density and the fixed-sea boundary

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
result: continuum and finite-volume CAR criteria, ultraviolet asymptotics, smooth repair and intermediate-time obstruction
carrier: complexified real1408 observed graph on R3 or stated three-torus LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed universal positive metric transported to standard L2 ON=declared_observed_graph
real_structure: real Clifford C_j and real skew M with beta=-i M
grading: instantaneous energy signs and separately imported CAR sea, not source fermionic parity
action_owner: repository-construction -- K2058 conditional graph with externally supplied mass and optional correction
target: moving sector and many-particle admissibility for the declared construction MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] On the same massive1408 graph, a nonzero homogeneous mass pulse with nonzero energy-sign mixing fails implementation in the fixed free-sea Fock representation on R3. Smooth switching can make excitation number and energy DENSITIES finite, but cannot remove the infinite-volume obstruction. On a torus smooth switching does give finite count and energy. Exact moving-sector transport from K2063 repairs the equal-mass endpoint, yet a nonconstant mass excursion still fails fixed-sea implementation at intermediate times. These distinctions constrain one precise imported quantization criterion; they do not settle GU.

The CAR criterion is established theory, reused from [K1896](k1896-local-phase-vacuum-boundary-2026-10-21.md) and [Binnenhei, Implementation of Endomorphisms of the CAR Algebra](https://arxiv.org/abs/physics/9701009): a one-particle unitary is implementable in the polarized CAR representation iff both energy off-diagonal blocks are Hilbert-Schmidt. K1896 treats spatial phase multiplication, and K1897 treats smooth compact SPACETIME scalar potentials. Their spatial localization hypotheses do not apply to a spatially homogeneous mass pulse. [K2061](k2061-common-asymptotic-sector-2026-10-25.md) already proves the pulse singular values and common-state theorem; these are reused, not rediscovered.

## 1. Same carrier, new independent criterion

Use H_mu(p)=A(p)+mu beta, mu>0, and P_mu=(I+H_mu/E_mu)/2 on L2(R3,C1408), with the same Clifford matrices and positive metric as K2063. Each spectral fiber has complex dimension g=704. Choose the negative-energy sea P_-=I-P_mu; CAR, that sea, and homogeneous external mass are explicit imports. For scattering S set B=P_- S P_mu. Particle and hole blocks have equal finite-fiber singular values. Their common scalar squared amplitude is rho(p) for scalar mass profiles.

This is not the source's graded-IG parity, a BV quotient or an interacting vacuum construction. SC-OP-04 ASSERTS candidate grammar, OP-05 remains UNCERTAIN about its rival, META-53 remains UNCERTAIN about positivity and META-56 DISAVOWS the odd-action prerequisite. LT-SM8/LT-GR6b, source verdicts and physics ledger remain unchanged.

## 2. Continuum volume obstruction versus density

Every homogeneous propagator is a matrix Fourier multiplier. A nonzero bounded multiplier on nonatomic L2 is not compact: choose a positive-measure region and measurable unit fiber section where its output norm exceeds c>0, partition that region into infinitely many disjoint positive-measure subsets, and normalize the sections on those subsets. They are orthonormal and their images are orthogonal with norm at least c. Thus it cannot be Hilbert-Schmidt.

Therefore homogeneous S is implementable in this fixed sea on R3 iff its off-diagonal multiplier vanishes almost everywhere. Finite-fiber unitarity makes vanishing of one off-diagonal block equivalent to vanishing of the other. For a nonzero finite rectangular pulse, K2061 gives rho>0 almost everywhere, so implementation fails. This result alone does NOT identify an ultraviolet divergence: any nonzero smooth compact-momentum mixing multiplier also fails by infinite volume.

A separately meaningful cutoff number density is the thermodynamic limit of torus number divided by its volume, at fixed momentum cutoff:

    n_+(Lambda)=g/(2pi)^3 integral_|p|<=Lambda rho(p) d^3p.

For continuous symbols the finite-cutoff limit is a Riemann sum. Particle-plus-hole energy density is

    e_pair(Lambda)=g/(2pi)^3 integral_|p|<=Lambda
                                      2E_mu(p) rho(p) d^3p.       (1)

These are densities, not finite traces on continuum L2. The uncut integrals can be finite or infinite independently of the preceding global obstruction.

## 3. Exact rectangular-pulse ultraviolet asymptotics

For m=mu+lambda during time tau>0 and mu outside, lambda!=0, K2061 supplies

    rho(r)=lambda^2 r^2/[(r^2+mu^2)(r^2+(mu+lambda)^2)]
                     *sin^2(tau sqrt(r^2+(mu+lambda)^2)).        (2)

The removable zero denominator uses sin(tau E)/E at E=0. At large r,

    r^2 rho(r)=lambda^2 sin^2(tau r)+O(1/r).

The error follows from E_(mu+lambda)=r+O(1/r), the Lipschitz bound on sin^2, and the rational prefactor. Since integral_0^Lambda sin^2(tau r)dr=Lambda/2+O(1),

    n_+(Lambda)/Lambda -> g lambda^2/(4pi^2),
    e_pair(Lambda)/Lambda^2 -> g lambda^2/(4pi^2).              (3)

For the second line use integral_0^Lambda r sin^2(tau r)dr=Lambda^2/4+O(Lambda). The error above contributes at most O(Lambda), lower order than Lambda^2. Both coefficients use g=704; total particle-plus-hole COUNT has twice the first coefficient. The limit fixes tau>0 before Lambda tends to infinity. Taking tau=0 first instead gives zero; these limits cannot be interchanged. No assertion about all lattice-resonant torus square pulses is required for(3).

## 4. Sudden change: a clean finite-volume ultraviolet control

Compare two positive masses a!=b at one instantaneous jump. The identity map between the two instantaneous splittings has squared off-block amplitude

    nu(r)=[1-(r^2+a b)/(sqrt(r^2+a^2)sqrt(r^2+b^2))]/2,
    r^2 nu(r) -> (a-b)^2/4.                                  (4)

Thus on a three-torus sum_k g nu(|2pi k/L|) diverges: for large nonzero k it is bounded below by a positive constant times |k|^-2, whose three-dimensional lattice sum diverges. This proves inequivalence of the two free-mass polarizations there as well as on R3. A finite momentum cutoff makes the count finite, but is a changed resource model. Equal masses give zero and are a required control.

## 5. Smooth temporal switching: exact high-frequency estimate

Let real m(t) be C3 on[a,b], equal to the same positive constant mu outside, with m',m'' zero at both endpoints. It may cross zero inside: the following high-frequency estimate uses r>=1, not a uniform mass gap. Reduce each radial block to h_r=r sigma1+m(t)sigma3. Its instantaneous basis is smooth for r>0. Let E=sqrt(r^2+m^2), theta=atan2(r,m), and define

    f=dot(theta)/2=-r m'/(2E^2),
    g0=f/(2E)=-r m'/(4E^3),
    h0=dot(g0)/(2E)=-r m''/(8E^4)+3r m(m')^2/(8E^6).

Write Phi(t)=integral_a^t E(u)du. In the dynamical-phase basis, initialized by alpha(a)=1,beta(a)=0,

    alpha'=f exp(2iPhi) beta, beta'=-f exp(-2iPhi) alpha.

Unitarity gives |alpha|,|beta|<=1. Integrate the beta integral twice by parts using (exp(-2iPhi))'=-2iE exp(-2iPhi). Endpoint flatness annihilates both boundary terms g0 alpha and h0 alpha. The resulting exact expression is

    beta(b)=integral_a^b exp(-2iPhi)
                  [h0' alpha+h0 alpha'+i g0 alpha']dt.

In particular the g0 alpha' feedback term is retained. Taking absolute values yields

    |beta(b,r)| <= integral_a^b (|dot(h0)|+|h0 f|+|g0 f|)dt.    (5)

The exact derivative is

    dot(h0)= -r m'''/(8E^4)
       +r[10m m' m''+3(m')^3]/(8E^6)
       -18r m^2(m')^3/(8E^8).                                (6)

Using E>=r>=1 in(5) gives |beta(b,r)|<=C3/r^3 with the explicit finite constant

    C3=integral_a^b [ |m'''|/8
        +(10|m m' m''|+3|m'|^3)/8
        +18m^2|m'|^3/8
        +( |m''|+3|m|(m')^2 )|m'|/16
        +(m')^2/8 ]dt.                                       (7)

This is deliberately conservative, not an optimal regularity threshold. For r<1 use unitarity |beta|<=1. Consequently the continuum number and energy densities in(1) are finite, as are torus particle/hole counts and total positive free excitation energy. Indeed the tails are bounded by r^-6 in squared amplitude; the number integrand is O(r^-4) and the energy integrand O(r^-3). Lattice sums converge by the same shell count. Moments weighted by E^q converge for0<=q<3 under this bound; no all-moments claim is made.

For an explicit nontrivial positive-mass smooth example take mu=1 and a square pulse lambda=1, tau=pi/(2sqrt(5)). At r=1 equation(2) gives rho=1/10. Replace its indicator by any smooth f0 supported in(0,tau),0<=f0<=1, equal to1 on[epsilon,tau-epsilon], and set m=1+f0. Choose epsilon<min(tau/2,1/(4sqrt(10))). Duhamel bounds the propagator difference by2epsilon, so its transition amplitude at r=1 stays greater than1/(2sqrt(10)). Hence the smooth pulse has nonzero mixing on an open momentum set. It has finite excitation densities and torus energy/count, while still failing continuum fixed-sea implementation by section2. This prevents an unwarranted conclusion that smoothing repairs infinite volume.

## 6. Composition with exact tracking: endpoints versus the whole path

Add K2063's K_cd for a positive C1 mass path, and suppose m starts and ends at mu. Exact transport gives U P_mu U*=P_mu at the final endpoint. Free factors do not change this. Both scattering off-blocks are zero, the fixed-sea endpoint automorphism is implementable, and its free particle/hole excitation count is zero. This is an actual repair of the endpoint criterion, paid for by the explicit nonlocal correction, not a rescue of the unchanged local pulse.

At an intermediate time with m(t)!=mu,

    U(t,a) P_mu U(t,a)*=P_m(t).

Fixed-sea implementability would require P_m(t)-P_mu Hilbert-Schmidt. On R3 this is a nonzero multiplier and fails. On a torus equation(4) gives its ultraviolet divergence. Thus exact instantaneous-vacuum transport does not give a unitary time path in the original single Fock representation, even when the equal-mass endpoint is implementable. A family of changing representations or a cutoff is an additional choice, not selected here. Nor do these statements prohibit algebraic CAR evolution.

## 7. Explicit finite-resource repair

On the finite torus momentum subspace |p|<=Lambda all one-particle spaces are finite-dimensional, so every unitary has finite off-block Hilbert-Schmidt norm and a CAR implementer. If N_Lambda is the number of retained momentum vectors, then

    N_particles <=704 N_Lambda,
    E_pair <=1408 sum_(retained p) E_mu(p)
            <=1408 N_Lambda sqrt(Lambda^2+mu^2).

These are worst-case finite-cutoff bounds, not ultraviolet limits. K2063's exact interpolation constructs a finite-order differential formula for transitionless tracking on precisely this cutoff space. Equal-mass endpoints have zero excitation, and intermediate times now admit implementation in the one finite sea representation. This satisfies the conjunction only after a declared finite cutoff; its spatial projection is nonlocal. No source or observation selects Lambda, L or their admissible error here.

## 8. Review, reproducibility and remaining input

The producer checks exact finite Clifford overlap and pulse algebra, derivative coefficients, dimension factors and density antiderivatives. A separate Pauli/symbolic probe checks the integration-by-parts coefficients, high-frequency expansions, equal-mass controls and genuine formula faults. Written proofs carry nonatomic noncompactness, lattice convergence/divergence, uniform smooth bounds and functional implementation conclusions. Same-author checking is not external specialist or proof-assistant certification.

The principal hostile cases are zero pulse/duration, resonances, finite volume, smooth switching, finite cutoff, unequal endpoint masses and intermediate-time representation change. Each has a distinct result above. No source, canonical ledger or public physics verdict changes. The next meaningful bridge must specify whether the physical requirement is endpoint scattering, instantaneous sectors, a fixed representation, local algebraic evolution or a finite resource approximation, and justify that choice against observations. Repeating generic mixing or fixed-local rigidity would not supply it.
