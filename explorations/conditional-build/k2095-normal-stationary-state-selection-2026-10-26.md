---
title: "K2095: Normal stationary states in the free infinite-volume sea representation"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, continuum apparatus, GU verdict or external certification
scripts:
  - tests/channel-swings/k2095_normal_stationary_state_selection_probe.py
---

# K2095: Normal stationary states in the free infinite-volume sea representation

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
result: conditional apparatus and state theorem with explicit countercontrols
carrier: free massive infinite-volume sea excitation Fock representation LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: supplied positive Hilbert metric ON=declared_complex_completion
real_structure: supplied particle-hole symmetry where invoked, not source derived
grading: parity, charge, energy sign and representation remain separate
action_owner: repository-construction -- free dynamics and explicitly supplied controls
target: conditional operational constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and Layer0 boundary

SC-OP-04 ASSERTS a candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd action.
The supplied positive massive CAR model is not source operator9.16. LT-SM8 and
LT-GR6b retain their actual action/observation/quotient/state debts. K2021 already
constructs local R0/R1; it does not source-select the present dynamics or controls.
Source-register, physics-ledger and canon verdicts remain unchanged. These are
conditional reverse-scaffold constraints, not GU predictions, novelty claims or
external/proof-assistant certification. No new substrate pathway is asserted.

## 1. An alternative to the quasifree selection premise

K2088/K2092 use quasifreeness plus operational ground tests. Here impose a
DIFFERENT strong premise: the state is globally normal in a supplied free sea
Fock representation. It is represented by a positive trace-class density rho
of trace1 on F(K), where K contains positive-energy particles and conjugate
negative-energy holes. The excitation dynamics is

    L=dGamma(omega), omega(p)=sqrt(v^2 |p|^2+m^2), m>0,v>0,

with finite internal multiplicity and momentum Lebesgue measure on R3.
No bound states, finite box, interaction or zero mode is included. Denote its
vacuum by Omega and P0=|Omega><Omega|. Normality here is GLOBAL, not local
normality of an algebraic state. No source or finite-density argument supplies it.

**Theorem.** If exp(-itL) rho exp(itL)=rho for every real t, then rho=P0.
No quasifreeness, particle-hole complement, ground-test positivity, or finite
mean energy of rho is required. Selecting the representation/dynamics is still
an external assumption, so this is not a derivation of the physical vacuum.

## 2. Explicit spectral and compactness proof

On every n>=1 excitation sector, L is multiplication by
sum_j sqrt(v^2 |p_j|^2+m^2), restricted to antisymmetric functions. For each
fixed p2,...,pn, a level set in p1 is a sphere, point, or empty; all have
three-dimensional Lebesgue measure zero. Fubini shows every total-energy level
set has product measure zero. There are no L2 eigenvectors in that sector.
Finite internal multiplicity and the countable Fock direct sum preserve this
conclusion. The ONLY point spectral subspace is the one-dimensional vacuum.
A spectral range [m,infinity) alone would not prove this; the actual dispersion
and measure are essential.

A positive trace-class rho is compact. Every positive eigenvalue of rho has
a finite-dimensional eigenspace, invariant under exp(-itL) by stationarity.
The restricted strongly continuous unitary group diagonalizes into characters
exp(-itE); its eigenvectors therefore are genuine L-eigenvectors (and lie in
Dom L). They must all lie in the vacuum space. The spectral expansion of rho
and trace1 then give rho=P0. This avoids an unjustified product L*rho or energy
trace, so infinite mean energy does not invalidate the proof.

## 3. Released consequence: compact diagnostics disperse, global states do not

For any normal density rho, not necessarily stationary, and any compact
operator A on the FULL Fock Hilbert space,

    lim_(T->infinity) (1/T) integral_0^T Tr(rho_t A) dt
       = Tr(rho P0) <Omega,A Omega>.                         (1)

For rank-one A and pure rho this is the Cesaro average of the squared Fourier
transform of the finite complex spectral measure <a,E_L(.)psi>. The bounded
Cesaro kernel tends to0 off the diagonal and1 on it. Dominated convergence
against the product total variation measure leaves exactly the common atoms;
here only the vacuum atom. Polarization gives rank-one offdiagonals, finite
sums give finite-rank A, and norm approximation gives compact A. Approximate
rho by its finite spectral expansion; the trace-tail error is uniformly bounded
by ||A|| times that tail, so all normal densities follow. Vacuum coherences are
included and average away. This proves(1) without assuming pointwise decay.

Compact does NOT mean every finite-mode CAR observable: n_f generally has
infinite rank on full Fock. Equation(1) supplies no local thermalization theorem
for all such detectors. Its limit is vacuum weight times vacuum expectation,
not vacuum expectation unless that weight is1. Meanwhile

    T(rho_t,P0)=T(rho,P0)

is constant by unitary invariance. An excitation can escape every compact test
on average while remaining globally distinguishable from vacuum.

## 4. Approximate stationarity and finite-volume countercontrols

There is no uniform robust version inferred from stationarity over a finite
laboratory interval. Fix e0>m and0<delta<e0-m. Choose a normalized one-particle
wavepacket in a nonempty energy shell[e0-delta,e0+delta]. For its pure rho,

    T(rho_t,rho)<=||(exp(-itL)-exp(-ite0))psi||
                 <=min(2,delta |t|),
    hence T(rho_t,rho)<=min(1,delta |t|),  T(rho,P0)=1.       (2)

The phase estimate uses |exp(-ix)-1|<=|x|; the final min1 is the separate
trace-distance bound. Mean energy is at most e0+delta and does not diverge as
delta shrinks. Thus arbitrarily accurate finite-window stationarity coexists
with maximal vacuum distance. No compactness/uniform localization across this
family is claimed; shrinking the energy shell spreads the wavepacket spatially.

A concrete rate consumer makes the nonuniformity visible. In the massive
one-particle spectral representation, choose a radial wavepacket with uniform
energy probability density on[e0-delta,e0+delta]. The positive radial Jacobian
away from threshold permits this normalized choice: with radial Jacobian
J(E)=4*pi*E*sqrt(E^2-m^2)/v^3, take one fixed spin component with
amplitude[2*delta*J(omega(p))]^-1/2 inside that shell. Its return probability is
sinc^2(delta t). Splitting the time integral at1/delta and using
sinc^2(x)<=min(1,1/x^2) gives the rank-one compact diagnostic bound

    (1/T) integral_0^T |<psi,exp(-itL)psi>|^2 dt
        <= min(1,2/(delta T)).                              (3)

The prior pure-state distance estimate also gives the lower bound
1-(delta*T)^2/3 for this averaged survival. Thus it tends to1 as delta tends
to0 at fixed T, and tends to0 as T grows for each fixed delta. The pure state
stays globally distance1 from vacuum. There is no class-wide decay rate over
this bounded-energy family of states AND their matched rank-one probes. Both
state and probe vary with delta; a rate depending on one fixed compact probe
is not excluded.

A finite box instead has energy eigenmodes and stationary excited densities,
including nonquasifree mixtures. Infinite-volume thermal/shifted-sea states of
K2086/88 are not counterexamples: if stationary and distinct, they cannot be
normal densities in THIS representation. Finite density or local normality does
not establish global normality; finite-energy claims require their own state
and representation definition. The two-mode nonquasifree neutral-ground rival
of K2092 likewise has atomic spectral structure and is not a contradiction.

## 5. Checks and next comparison

The exact probe checks finite-box stationary nonquasifree rivals, an exact
finite-window fidelity value, spectral atom weights, a continuum shell Fourier
value and variance, and the elementary split-integral upper envelope. It tests the shape of the
argument; it cannot prove absence of eigenvalues on R3 or universal compact
operator convergence by sampling. Those claims rest on sections2--3 and
independent specialist review. Mutants change states, spectral phases and
normalizations while keeping predicates fixed.

This closes a nonquasifree selector only under explicit global normality in a
free continuum representation. It does not repair source-selected observation,
interacting positivity or K2092's uniform operational ground test. Next compare
an actual source-algebra/dynamics bridge or a finite-local-test stability theorem
with the remaining continuum apparatus and thermal163/164 constructions.
