---
title: "K2228 Continuum energy-form detector control with retained drift"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied fixed canonical-mode continuum control; no local apparatus, energy convergence or GU realization
scripts:
  - tests/channel-swings/k2228_continuum_energy_form_detector_control_probe.py
---

# K2228 Continuum energy-form detector control with retained drift

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
result: K2228 fixed canonical continuum mode energy-form control theorem
carrier: supplied positive massive scalar boson Fock space with one record and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free energy form ON=declared_carrier
real_structure: conjugation-real canonical smearing and complex adjoint
grading: boson occupation and binary record; not spinor chirality
action_owner: repository-construction -- externally switched positive mode controls
target: complete recorded energy-constrained channel with physical free drift MAP-TYPE=intertwiner
```

This is the same supplied canonical mode used by K2160/K2223, including its
Bogoliubov creation part. It is not a GU physical quotient or source-selected
operator. Direct mode controls are supplied and nonlocal. The result proves
convergence in reference-uniform half trace distance on input energy balls;
it does not prove convergence of output energy or an autonomous apparatus.

## Independent preflight/rerank

K2225 solves finite oscillator chains but its site-number bound contains ultraviolet zero-point Z, w_max and kappa. Its divergent bound is not a lower bound. K2223 already exactly realizes the same continuum instrument by replacing the total free Hamiltonian; merely repeating dilation/pulses is duplicate. Highest useful successor: retain H=dGamma(omega), prove full energy-domain estimates using only the fixed mode's weighted one-particle norms. Direct controls are supplied finite-mode/nonlocal controls, not adjacent-site or point-local interactions. This changes the control-locality assumption explicitly. Prior searches of k21*/k22* detector notes found no such arbitrary-energy continuum retained-drift result. Relevant path: K2154 -> K2225 finite-chain; K2151 -> K2160 -> K2219 -> K2223 same canonical instrument and positive pulses. No registered claim kill.

## Setup and constants

Let omega>=m>0 on one-particle Hilbert space, commute with conjugation, H=dGamma(omega), G=H+1, and h,j real with ||h||^2-||j||^2=1, h,j in Dom omega^(1/2). These h,j are Bogoliubov coefficient vectors, not K2160's normalized Schmidt physical modes. Set b=a(h)+a*(j), n=b*b. For a normalized real canonical smear f and scale nu>0,

 h=(sqrt(nu) omega^-1/2+omega^1/2/sqrt(nu))f/2,
 j=(sqrt(nu) omega^-1/2-omega^1/2/sqrt(nu))f/2.

Thus f in Dom omega suffices (mass gap makes negative powers harmless). For the physical Klein-Gordon dispersion omega=sqrt(-Delta+m^2), Schwartz smears qualify; arbitrary positive omega requires checking its domain. To identify exactly the K2151/K2160 instrument, freeze its scale nu=sqrt(<f,omega f>/<f,omega^-1 f>). The theorem permits other positive nu, but they generally define a different number observable and do not inherit that optimizer. The physical Q,P of K2160 are rescaled to Qtilde=sqrt(nu)Q,Ptilde=P/sqrt(nu); their diagonal squeeze is identical to the physical Q->sQ,P->P/s.

 u=||omega^-1/2 h||+||omega^-1/2 j||,
 B^2=u^2+||j||^2, Bplus=sqrt(B^2+1),
 eta=||omega^1/2 h||+||omega^1/2 j||, A=eta Bplus.

For any psi in Q(H), including record/reference coefficients,
 ||b psi||<=u||H^1/2 psi||+||j||||psi||<=B||G^1/2 psi||,
 ||b*psi||<=Bplus||G^1/2 psi||.
The creation vacuum term ||j||^2 is essential, not discardable.

## Energy transport lemma, including arbitrary measurable effects

For the number/oscillator unitaries below, initially on a common core where these commutators exist, a(k)-<k,h>b+<k,j>b* commutes with U. Hence
 [a(k),U]=<k,h>[b,U]-<k,j>[b*,U].
The minus sign is forced by CCR. Integrating the annihilation-energy identity gives
 ||H^1/2 Upsi|| <= ||H^1/2 psi|| + ||omega^1/2 h|| ||[b,U]psi|| + ||omega^1/2 j|| ||[b*,U]psi||.
This identity is initially justified on the finite-mode oscillator tensor factor and finite physical-energy vectors, then by closure; no invariance of span(h,j) under omega is required.

For bounded real theta_n=asin sqrt(e_n), 0<=e_n<=1, define Delta=sup_n |theta_(n+1)-theta_n|<=pi/2. No smooth extension or monotonicity required. U_m(t)=exp(-it(theta(n) sigma_y+pi/2)) satisfies
 ||[b,U_m(t)]psi||<=Delta |t| ||bpsi||,
 ||[b*,U_m(t)]psi||<=Delta |t| ||b*psi||,
by the exact adjacent occupation shift and the matrix exponential Lipschitz estimate for the SAME Pauli generator. Thus ||G^1/2 U_m(t)psi|| <=(1+A Delta |t|)||G^1/2 psi||. Splitting the group into n steps and taking n->infinity gives exp(A Delta |t|).

For K_s=(Ptilde^2/s+s Qtilde^2)/2, the Heisenberg generator on (b,b*) has row absolute sum r_s=max(s,1/s). Its exponential obeys ||M_s(t)-I||_infty<=exp(r_s|t|)-1. Consequently each commutator norm is <=Bplus(exp(r_s|t|)-1)||G^1/2 psi||. The same subdivision argument gives exp(A r_s |t|). Conditional finite record blocks use r=max_r max(s_r,1/s_r). Final K_1 has r=1. Scalar phases do not affect these bounds. These are bounds on the G norm; expectation growth has twice the exponent.

## Positive plateaus and same target

K_m=theta(n) sigma_y+pi/2, duration1; conditional K_s, duration pi/2; K_1 duration3pi/2. All K_l>=0, and the same K2223 pulse ordering gives recorded Kraus S_r sqrt(e_r(n)). Define
 T0=1+2pi, R=max_r max(s_r,1/s_r),
 L=exp(2A[Delta+(pi/2)R+3pi/2]).
Use actual H+Lambda K_l for durations d_l/Lambda. Ideal uses Lambda K_l. H is never canceled or switched off. Ideal/actual mean G stays <=L(E+1) for marginal input energy<=E.

## Domain proof (avoid a real-time form-Trotter gap)

0<=K_m<=pi G and 0<=K_s<=r_s(n+1/2)<=r_s(B^2+1/2)G. Thus H+Lambda K_l is the positive closed form sum on Q(H), with form norm equivalent to G; no equality of operator domains is claimed.

To prove actual energy growth, clip omega by omega_R=min(omega,R). H_R=dGamma(omega_R) commutes with H, so each free evolution preserves G exactly. For quadratic K_l, H_R+Lambda K_l is essentially self-adjoint on finite-particle vectors: its sector norm grows at most linearly in occupation, and it changes occupation by at most2; analytic-vector estimates apply. For bounded K_m use bounded perturbation. Ordinary unitary Trotter for these operator sums combines the exact free G conservation with the ideal pulse bound. Its bound is independent of the subdivision and of R. Pass the subdivision limit by strong convergence and lower semicontinuity of G. Then positive forms H_R+Lambda K_l increase to the closed form H+Lambda K_l; monotone form convergence gives strong resolvent and unitary convergence, so the G bound survives. This is analytic approximation, not an occupation cutoff.

Both ideal and actual propagators preserve V=Q(H) and are strongly continuous there. For ideal, use a(k)(U_t-I)psi=(U_t-I)a(k)psi+[a(k),U_t]psi: the integrated first term vanishes by strong continuity and dominated convergence, and the second is O(t) by the commutator bounds; actual follows from conservation of the equivalent plateau form norm. Both forms are bounded V->V*. The weak Schrödinger product rule therefore gives the ideal/actual overlap derivative in dual form, with common K terms canceling:
 |d<psi_I,psi_A>/dt|=|h[psi_I,psi_A]| <=sqrt(<H>_I <H>_A)<=L(E+1).
Integrate over T=T0/Lambda, purify inputs, and contract common record pinching:
 delta_E <=min(1,sqrt(2L(E+1)T0/Lambda)).
All field output and every outcome/reference retained. No energy variance. Actual <H> <=L(E+1)-1. Trace-distance convergence does not imply endpoint mean energy converges to K2219 E_star.

## Work and uniformity

Take a_m=pi, a_s=R(B^2+1/2), a_1=B^2+1/2. For switched additive controls zero at endpoints,
 W_signed=<H>_out-<H>_in,
 sum_switch |<Delta(Lambda K)>|<=2Lambda(a_m+a_s+a_1)L(E+1).
This is absolute MEAN switching exchange, not stochastic absolute work or optimal total apparatus expense. Fresh reset can be composed by K2226 with channel contractivity and appropriate later-cycle energy budgets.

The constants depend only on weighted norms of the SAME fixed mode and squeeze bounds, not total UV mode count, tr omega, or sup omega. More generally any family with uniformly bounded A,B,R,Delta has a uniform guarantee. For exhausting spectral projections P_J increasing strongly to I and commuting with omega and conjugation (for example `1_[m,J](omega)`), f_J=P_J f/||P_J f|| ->f in Dom omega, so the constants converge and are uniformly bounded eventually. This alone is not a quantitative comparison between different target modes; the theorem already applies directly to the continuum fixed mode. Direct mode controls are externally supplied nonlocal interactions; no finite propagation/locality conclusion.

## Concrete exact fixture and genuine UV spectator followthrough

For omega=diag(1,9), f=(1,1)/sqrt2, nu=3, h=(2,2)/sqrt6,j=(1,-1)/sqrt6. Then ||h||²=4/3,||j||²=1/3, B²=2, eta²=15,A²=45. Add any orthogonal spectator one-particle space with any positive unbounded frequency operator; h,j have zero spectator component, so ALL constants stay exactly the same. This gives a real unlimited UV-spectrum consumer, though not a continuum-local detector. It embeds the K2158/K2160 exact fixture (unused third frequency4 is a spectator), and retains exactly its numerical optimum if that is the declared fixture. A generic continuum smear has its own moments and does not inherit E_star or N=1/3.

## Hostile review ceiling / weakest seams

1. Generic form-sum real-time Trotter cannot be silently assumed; spectral clipping above repairs it.
2. Bounded theta is sufficient only because exact adjacent shifts of this single-mode number calculus are used; do not infer arbitrary bounded operators preserve Q(H).
3. Canonical b is Bogoliubov (j!=0); dropping creation term or replacing it by a(h) changes the object and invalidates the optimized instrument.
4. Uniform H-input bounds do not imply energy-output convergence; no claim that net actual work tends to E_star.
5. Fixed-mode direct controls are not adjacent-site positive controls or a causal apparatus. The locality assumption is explicitly supplied/relaxed.
6. Finite exact probes support algebra/constants; infinite-Fock and common form-domain theorem is written mathematics, independently reviewed internally; it is not established by finite samples.

## Evidence and reproducibility

The analytic energy/domain proof above is distinct from the exact finite
Bogoliubov, occupation-shift, squeeze-order and spectator controls in the
[probe](../../tests/channel-swings/k2228_continuum_energy_form_detector_control_probe.py).
The [report](../../lab/process/k2228-continuum-energy-form-detector-control.json)
binds the note, code and reused input notes. Genuine faults alter five
mathematical inputs, not the acceptance predicates. No novelty, external
expert, proof-assistant or empirical claim is made. Energy-constrained channel
norms are standard; see [Shirokov](https://arxiv.org/abs/1706.00361).
