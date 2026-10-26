---
title: "K2080: Local CAR detection and an all-outcome Bell construction"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: provisional conditional mathematics pending specialist review; no GU verdict or novelty claim
scripts:
  - tests/channel-swings/k2080_local_car_detector.py
  - tests/channel-swings/k2080_local_car_detector_probe.py
---

# K2080: Local CAR detection and an all-outcome Bell construction

**PROVISIONAL.** Written construction and same-author checks only. Field-relevant
specialist review is pending. This does not replace an accepted scientific verdict.

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
result: same-carrier local number detector with vacuum error and a finite-radius even-local Bell candidate
carrier: complex massive Dirac1408 one-particle space and imported sea CAR representation LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive L2 inner product and supplied quasifree sea ON=declared_complex_completion
real_structure: complex CAR; no source-real identification
grading: fermion parity distinct from energy sign and source grading
action_owner: repository-construction -- free Dirac flow and declared local observable algebra
target: vacuum response, local records and Bell lower bound MAP-TYPE=intertwiner
```

## 1. New question on the same carrier

[K2077](k2077-controlled-detector-response-2026-10-25.md) constructs a one-particle
ancilla instrument and a Bell experiment on two explicitly supplied tensor copies.
Its claim ceiling correctly stops before a local-field realization. Here supply
the CAR algebra of the SAME H=L2(R3,C4 tensor C352),
H0=alpha.D+m beta, P=1_(H0>0), Q=I-P, and the gauge-invariant quasifree
sea omega_Q with omega_Q(a*(f)a(g))=<g,Qf>. The convention is annihilation
antilinear in f and inner product linear in its second argument, so
{a(f),a*(g)}=<f,g>. Expectation formulas below for diagonal occupations are
unambiguous. CAR and this sea are imports, not source-derived quantization.

K1892's causal algebra uses a different16-to4 construction; it is background,
not this carrier identification. K1896/1897 concern external scattering
implementability, not the detector effect constructed below. Standard CAR
representation context is discussed by
[Binnenhei](https://arxiv.org/abs/physics/9701009); no novelty claim is made.
SC-OP-04 ASSERTS candidate grammar; OP-05 and META-53 remain UNCERTAIN;
META-56 DISAVOWS an odd-action prerequisite. LT-SM8/GR6b and all source,
physics-ledger and canon verdicts are unchanged.

For tests supported in disjoint spatial regions the CAR scalar products
vanish. Even polynomials therefore commute. Free finite speed extends this
to unequal times at support distance greater than the time difference.
This is exact locality of the declared free even CAR net; positive-energy
compression alone would not give it. No split-property tensor factorization
of continuum local algebras is assumed.

## 2. Exact local effect, vacuum clicks and signal

For normalized compact f in H, n_f=a*(f)a(f) is an even local orthogonal
projection: n_f^2=n_f by CAR. Put nu=<f,Qf>. On the sea its click probability
is nu. On the normalized one-electron state a*(psi)Omega_Q, with psi in P H,
its covariance is Q+|psi><psi|, so

    p_e=nu+|<f,psi>|^2,   p_vac=nu.                   (1)

Take0<=chi<=1, chi=1 on B_L, smooth and compact in B_(L+rho), and
f=chi psi/||chi psi||. Write tau=||1_(B_L^c)psi||<1 and
b=||chi psi||, a=<psi,chi psi>/b, both real nonnegative. Since
chi>=chi^2, a>=b>=sqrt(1-tau^2). Because P contains the direction psi,

    nu<=1-a^2<=tau^2,
    1-p_e<=1-a^2<=tau^2,
    ||f-psi||<=sqrt(2)tau.                            (2)

Thus local algebraic detection and arbitrarily small vacuum/false-negative
error coexist on this preparation. K2060 proves that no nonzero compact
vector is entirely of either massive energy sign. Hence0<nu<1 for nonzero
compact f, even when tau is very small. This is not an exact vacuum-silent
detector. Subtracting the vacuum mean does not fix that: n_f-nu I has the
negative eigenvalue -nu. It is not a positive click effect.

The Lueders instrument {n_f,I-n_f} is a legitimate even-local algebraic
instrument, retaining both outcomes. At spacelike separation, each Kraus
operator commutes with every remote even observable, so the complete
nonselective channel leaves that observable exactly unchanged in every state.
Selective correlations can change and do not imply signaling.

## 3. Two local spin readouts without discarding empty or double occupancy

Use an internal two-dimensional multiplicity factor commuting with the Dirac
matrices. For a normalized spatial Dirac spinor f and a unit Pauli direction
n, let v_+,v_- be the two spin eigenvectors and set

    S_n(f)=n_(f tensor v_+) - n_(f tensor v_-).

The spectrum is{-1,0,+1}; ||S_n||<=1. Empty and double-occupied modes produce
0 and remain in the data. The spectral projections are polynomials in the
local even number operators and give a complete local instrument. In the
sea the restricted two-mode covariance is nu I2, so

    omega_Q(S_n)=0,  omega_Q(S_n^2)=2nu(1-nu).         (3)

Zero mean does not mean no vacuum noise. On a single added electron psi tensor v,
the mean is a^2 <v,n.sigma v>, with a as in(2); the sea contribution cancels
between the two spin channels, not at the level of individual click events.

## 4. A constructive same-field Bell consumer

Let phi_A,phi_B be two translated copies of K2077's positive Gaussian Dirac
spinor, each normalized with norm tail<=tau outside its radius-L ball. Choose
centers D>2(L+rho) and0<tau<=1/4. Since the two B_L balls are disjoint,
splitting the overlap integral into B_L(A) and its complement gives

    |c|=|<phi_A,phi_B>|<=2tau.

Set u_A=phi_A and u_B=(phi_B-c phi_A)/sqrt(1-|c|^2). Both remain positive
energy and are exactly orthonormal. Their norm tails outside the respective
B_L balls obey

    tau_A<=tau,
    tau_B<=(tau+|c|)/sqrt(1-|c|^2)
          <=3tau/sqrt(1-4tau^2)<4tau.                (4)

Choose chi_A,chi_B as above with disjoint compact supports and define
f_j=chi_j u_j/||chi_j u_j||. Then f_A,f_B are exactly orthogonal by support,
and delta_j=||f_j-u_j||<=sqrt(2)tau_j. The localized tests may therefore
be used in exact commuting even algebras, without approximating commutation.

In the sea representation form the normalized two-electron singlet

    Psi=[a*(u_A up)a*(u_B down)-a*(u_A down)a*(u_B up)]Omega_Q/sqrt(2).

Its norm and spin action follow from CAR and a(u_j v)Omega_Q=0. Fermion order
is fixed as A before B. Ideal S_n(u_A), S_n(u_B) act as Pauli observables on
this logical two-electron subspace. The usual singlet directions attain
CHSH magnitude2sqrt(2). This is a supplied state, not an automatically
prepared vacuum resource or an observed GU prediction.

The CAR norm identity ||a(f)-a(u)||=||f-u|| and product expansion imply

    ||n_f-n_u||<=2||f-u||,
    ||S_n(f)-S_n(u)||<=4||f-u||.                      (5)

For contractions, each two-site correlation changes by at most
4(delta_A+delta_B). Four CHSH terms consequently give

    |CHSH_local| >=2sqrt(2)-16(delta_A+delta_B)
                  >2sqrt(2)-80sqrt(2)tau
                  >14/5-120tau.                      (6)

The bounds2sqrt(2)>14/5 and sqrt(2)<3/2 make the final bound rational.
At L=2000/m, rho=1/m and tau<1/500, choose D=4003/m. Then

    |CHSH_local|>64/25>2.

This is an all-outcome, even-local free-field algebra construction on one
CAR system. Empty/double occupancy gives0; no projection onto a two-electron
local subspace and no success conditioning occurs in the observed record.
Site A's local vacuum number click is <=tau^2; site B's is <16tau^2.
The exact local hidden-variable CHSH bound2 still holds for all outcomes
in[-1,1]. The same-field construction differs from K2077's two-copy model
and does not silently identify their states or instruments.

## 5. Follow-through: finite vacuum energy of the local measurement

Unlike a spatial multiplication phase acting on every continuum mode, a
single normalized test f gives a rank-one one-particle reflection
r=I-2|f><f|. Its CAR implementer is the actual bounded local even unitary
R=I-2n_f. Direct CAR conjugation proves R a(g) R=a(rg). The nonselective
binary Lueders channel is exactly the half-mixture of identity and conjugation
by R. Its vacuum covariance is therefore C=(Q+r Q r)/2. No infinite sea
energy is subtracted: define particle and hole excitation energies from the
positive operators P C P and Q(I-C)Q separately.

Writing f_+=Pf, f_-=Qf, nu=||f_-||^2, direct rank-one multiplication gives

    N_particles=2nu(1-nu), N_holes=2nu(1-nu),
    E_exc=2nu e_+ +2(1-nu)e_-,                       (7)
    e_+=<f_+,|H0|f_+>, e_-=<f_-,|H0|f_->.

Thus the nonselective measurement has total vacuum excitation number
4nu(1-nu), not zero even though its mean spin can vanish. For f in H1,
e_+<=||H0f|| sqrt(1-nu) and e_-<=||H0f|| sqrt(nu), so

    E_exc<=4||H0f|| sqrt(nu)<=4||H0f|| tau.            (8)

The smooth cutoff guarantees f in H1. Its derivative lies outside B_L, giving

    ||H0f|| <= [||H0psi||+2tau/rho]/sqrt(1-tau^2).     (9)

For the single Gaussian at L=2000/m and rho=1/m this is <201m/100.
Equations(7)--(9) give E_exc<201m/12500 and total excitation number<1/62500.
This bounds postmeasurement free excitation energy in the imported sea,
not the controller's work, detector energy or full energy distribution.

The two internal spin modes are orthogonal both before and after energy
projection: Q is identity on the multiplicity qubit. Performing both binary
number instruments and then recording their difference is one explicit
four-outcome local implementation of the ternary readout. At vacuum its
particle/hole and energy contributions add, so the corresponding bounds
double. Empty and double occupancy both report0, with their underlying
outcomes retained. For site B use its Gram-Schmidt tail and free H0 norm;
(4), (8), (9) give finite bounds without replacing it by the original
unorthogonalized Gaussian. Sequential measurement of both sites is also
finite-energy: its one-particle reflections differ from identity by finite
rank with H1 range; products preserve that property. No additive two-site
energy formula is asserted without accounting for cross-region sea covariance.

This identifies an important difference from K1896's ultraviolet-divergent
multiplication kicks: a smooth compact smeared rank-one mode is a different
operator with an explicitly finite-rank commutator with the sea. It does not
silently repair that old kick. The local algebraic instrument is normal and
finite-energy in the chosen sea, but its point-local apparatus implementation
still remains open.

## 6. What the construction supplies and what it does not

The compact f_j define spatially smeared bilinear observables, with kernels
supported in B_(L+rho) times that same ball. They belong to the local field
algebra, but that does not produce a point-local Hamiltonian coupling that
measures them in finite time. An instantaneous whole-ball gate is not a
relativistically implemented apparatus. Smooth temporal smearing, apparatus
propagation and its readout error require a separate construction. K2079's
finite-species scattering result does not supply a shared two-state memory.

Likewise this result does not select a GU real structure, interacting positive
quotient, physical state preparation, or total apparatus/source energy.
Its contribution is a concrete candidate bridge from the declared massive
one-particle space to local field observables, with vacuum noise, localization
errors and a nonpostselected Bell consumer all on the same carrier. The next
useful test is an explicitly local finite-duration detector coupling or an
obstruction to implementing these smeared instruments under named resources.

## Verification and hostile charges

The producer emits exact conservative constants, covariance constraints and
input hashes. The separate probe constructs Jordan-Wigner CAR matrices from
scratch, checks a filled-sea Slater state and added electron, local spin noise,
fermion signs, a two-electron singlet, commuting even observables and the
complete local instrument. Rational inequalities check the radius, tail,
orthogonalization and CHSH accounting. Baseline-first faults alter the CAR
representation, subtract the vacuum to fake a positive effect, omit noise or
misstate Bell constants; each must fail its mathematical assertion. These
finite controls establish their finite algebra, not continuum localization.
The written CAR/support/Gram-Schmidt estimates are the continuum argument.
Same-author hostile review checks the strongest overclaim (apparatus or GU
realization), contrary construction (vacuum clicks and species/memory mismatch),
and weakest reproducibility seam (logical singlet versus actual local outcomes).
Independent field-relevant specialist acceptance remains pending. No novelty,
external-expert or proof-assistant certification is claimed.
