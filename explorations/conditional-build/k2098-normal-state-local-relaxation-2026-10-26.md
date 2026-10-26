---
title: "K2098: Finite-mode local relaxation for every normal sea state"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, massive apparatus, GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2098_normal_state_local_relaxation_probe.py
---

# K2098: Finite-mode local relaxation for every normal sea state

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
result: conditional operational theorem with explicitly supplied representation and controls
carrier: free massive infinite-volume sea CAR with arbitrary globally normal density LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: stated CAR adjoint and particle-hole split only where used; no source derivation
grading: fermion parity, charge and energy signs remain distinct
action_owner: repository-construction -- supplied free dynamics and controls
target: conditional operational state and measurement constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and Layer0 boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd action.
These supplied positive CAR models are not source operator9.16. K2021 already
constructs local R0/R1 but does not source-select these dynamics, observations
or states. LT-SM8/LT-GR6b retain action/observation/quotient/positivity debts.
Source-register, physics-ledger and canon verdicts remain unchanged. No new
substrate pathway or source mechanism is asserted. The results supply scoped
reverse-scaffold constraints and conditional mathematical constructions.

## 1. A finite observable algebra is different from a compact operator

[K2095](k2095-normal-stationary-state-selection-2026-10-26.md) proves a Cesaro
result for operators compact on the FULL free sea Fock space. An occupation
n_f is generally not such an operator. Here prove a different, pointwise
finite-mode state theorem, using the actual one-particle absolutely continuous
spectrum rather than the full-Fock compact-operator argument.

Supply the same positive free massive Dirac CAR representation: excitation
space K=H_positive direct-sum conjugate(H_negative), vacuum Omega, generator
L=dGamma(omega), omega(p)=sqrt(v^2|p|^2+m^2), m,v>0, finite multiplicity,
Lebesgue measure on R3. Let Q be the sea covariance and P=I-Q. The physical
field has sea representation

    b(f)=a(Pf)+a*(conjugate(Qf)),                          (1)

with the conventional antilinear annihilator and conjugate hole space.
Fix any finite-dimensional subspace F of the physical one-particle space,
and its finite matrix algebra CAR(F). The tests in F are fixed before time
tends to infinity. No entire bounded spatial-region algebra is finite dimensional.

**Theorem.** For EVERY globally normal density rho on this sea Fock space,
including nonquasifree densities and infinite mean particle number/energy,

    || rho_t restricted to CAR(F)-omega_sea restricted to CAR(F) ||_1 ->0
                              as |t|->infinity.           (2)

Here rho_t=exp(-itL)rho exp(itL), and the norm is the trace norm of density
matrices on the finite CAR algebra; T_F is one half of this norm.
This is not global trace-norm convergence, uniform relaxation, preparation of
a fresh pure memory, or a derivation of the chosen representation/state.

## 2. Explicit proof and a useful quantitative bound

Let K_F=span{Pf,conjugate(Qf): f in F} inside K, taking the particle and hole
vectors in their separate summands. Its dimension is at most2 dim(F).
Equation(1) puts CAR(F) inside the excitation algebra CAR(K_F). In the Fock
factorization with K_F first, this is a subalgebra of the first matrix factor;
fermionic parity signs on the complement do not affect that assertion.
The sea vacuum is the excitation vacuum on K_F.

For any normal state rho and any finite-dimensional L0 subset K, let p0 be
its probability of no excitation in L0. Vacuum fidelity and the pure-state
trace-distance bound imply

    half trace distance on CAR(L0) <=sqrt(1-p0)
                       <=sqrt(Tr(rho dGamma(P_L0))).      (3)

The second inequality follows from I-|vac_L0><vac_L0|<=N_L0. Restriction to
CAR(F) cannot increase distinguishability. For rho with finite mean total
excitation number, its one-particle density gamma is positive trace class,
Tr gamma=Tr rho N. Hence, with an orthonormal basis e1,...,er of K_F,

    T_F(t) <= min(1,sqrt(q_F(t))),
    q_F(t)=sum_j <exp(it omega)e_j, gamma exp(it omega)e_j>.
                                                                  (4)

All matrix elements of exp(it omega) tend to zero. To see this without an
assumed dispersive rate, write <u,U_t w> as the oscillatory integral of the
L1 momentum density u* w. In radial coordinates the change of variables
E=sqrt(v^2 r^2+m^2) gives an L1 energy density on(m,infinity); the point r=0
has zero measure. Riemann-Lebesgue proves weak convergence U_t->0. Finite
multiplicity and the two excitation summands preserve it. A compact positive
gamma then makes each expectation in(4) tend to zero: approximate gamma in
operator norm by finite rank and use weak convergence. Thus(2) holds whenever
Tr rho N is finite. The proof uses no Wick factorization and no assumption
that rho itself is quasifree or stationary.

For general globally normal rho, let P_M project onto total excitation number
at most M and set rho_M=P_M rho P_M /Tr(rho P_M) when nonzero. P_M increases
strongly to I, so rho_M->rho in trace norm (for instance use purification and
p_M->1). rho_M has mean number at most M. Dynamics and algebra restriction
are trace-norm contractions, uniformly in t. Approximate rho by rho_M first,
then take t large in its proven finite-number bound. This proves(2) without
requiring a finite mean number or energy of rho.

This extends a different earlier result, [K98](k98-observed-finite-temperature-quasifree-local-forgetting-wave-2026-09-02.md),
which concerns a rank-one quasifree perturbation of a half-line thermal state.
It neither repeats that Bessel calculation nor extends the present theorem to
all thermal representations or interactions. The common local/global warning
survives, while the representation, continuum and nonquasifree scope differ.

### A quantitative successor under a stated spectral regularity budget

Equation(4) also yields a usable clock when the missing regularity is supplied.
Let gamma=sum_k lambda_k |psi_k><psi_k| with lambda_k>=0 and finite trace.
For each detector basis vector e_j, let a_kj(E) be the energy-density function
of <psi_k,exp(it omega)e_j>. Assume its zero extension to R is in W^(1,1)(R)
and that

    C_F=sum_(k,j) lambda_k ||a_kj prime||_L1^2 < infinity. (5)

The zero-extension assumption includes the threshold boundary, not merely
smoothness for E>m. Integration by parts has no boundary term and gives
|<psi_k,exp(it omega)e_j>|<=||a_kj prime||_1/|t|. Substitution into(4) yields

    T_F(t)<=min(1,sqrt(C_F)/|t|), t nonzero.                (6)

For a finite-rank gamma it is enough to check finitely many such density
norms. For an infinite-rank gamma the summability in(5) is essential.
No rate for arbitrary normal states, energy-only ball, or source dynamics is
inferred. In the time-shift counterfamily below, a_kj gains an oscillatory
energy phase whose derivative budget can grow with T; hence(6) is consistent
with the absence of a uniform energy-only clock. The exact probe integrates
the explicit density a(E)=(E-m)exp(-(E-m)) for E>=m and checks its Fourier
modulus/decay, distinct from proving(5) for an arbitrary detector.

## 3. Released consequence: persistent global information and no uniform clock

Unitary invariance gives T(rho_t,P_Omega)=T(rho,P_Omega) for all t. A pure
excitation remains globally at distance1 while every fixed finite physical
CAR restriction converges to the sea restriction, which is usually mixed.
In particular, local return does not purify the detector modes. At any fixed
time the full algebra can still carry the information outside the chosen tests.

No uniform convergence rate over all normal states follows, even with an
energy cap that admits the following fixed wavepacket. Take a normalized position-space spinor f in C_c^infinity(R3,C^d)
with Pf nonzero. It has finite one-particle energy, as does Pf because the
spectral projection P commutes with omega. Put
ell=Pf/||Pf|| in the particle summand. The excitation a*(ell)Omega changes
<n_f> from nu=<f,Qf> to1. For any requested late time T, choose the initial
state with excitation exp(iT omega)ell. At T it returns to ell, so the same
fixed n_f distinguishes it from sea by1-nu>0. The mean excitation energy is
the fixed <ell,omega ell>, independent of T. These are different initial
states as T varies. Thus(2) is pointwise in rho, not a uniform energy-ball
statement. A moving detector following an excitation likewise need not relax.
Spatial localization bounds on the initial state could support rates, but
are new hypotheses; finite energy alone supplies no common relaxation time.

A further consequence concerns every fixed element A of the physical CAR
C*-algebra, not just a preselected finite detector. Finite polynomials in a
finite set of smearings are norm dense in that algebra. Approximate A in
operator norm by such a polynomial B. Both states have norm1, so the error
in the difference of expectations is at most2||A-B||, uniformly in t. Apply
(2) to B, then improve the approximation. Thus rho_t(A)->omega_sea(A) for
EVERY fixed CAR element. This is weak-star convergence of states on the CAR
C*-algebra, not state-norm convergence, not convergence for a time-varying A,
and not an extension to every operator in its von Neumann closure. The full
Fock vacuum projector is not supplied as a CAR norm-limit by this argument.

A bound one-particle mode would invalidate the weak-decay premise. A finite-box
energy eigenmode is an exact countercontrol. Neither finite matrices nor
energy-spectrum range alone proves the absolutely continuous continuum claim.

## 4. Verification and next condition

The analytic proof supplies the universal theorem. Exact finite CAR controls
check a nonquasifree correlated mixture, a separate coherent pair, local vacuum
probability versus occupation, and physical particle/hole CAR signs and one-mode
occupation. An explicit absolutely continuous spectral density is integrated and its
Fourier amplitude is checked for its modulus and decay; an atomic stationary state supplies the
spectral countercontrol. State/data mutations change these objects before
verification. The controls do not prove general subalgebra restriction or
continuum decay. A physically stronger successor would prove a rate under
explicit localization or an interacting scattering hypothesis in the actual
source-selected observed algebra. Current source/physics/canon status remains
unchanged.
