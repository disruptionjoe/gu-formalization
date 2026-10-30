---
title: "K2296 Stochastic drift of the retained pump"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conserving circuit and phase law; no hardware or GU certification
scripts:
  - tests/channel-swings/k2296_stochastic_pump_drift_probe.py
---

# K2296 Stochastic drift of the retained pump

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2296 Stochastic drift of the retained pump
carrier: complex bosonic field and coherent or displaced-thermal pump with classical residual phase LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert pairing and trace norm ON=declared_carrier
real_structure: complex Hilbert adjoint and real phase distribution
grading: total charge Q=N_all+2K; no native Clifford transfer
action_owner: repository-construction -- supplied charge conserving circuit
target: full recorded instrument with original retained pump MAP-TYPE=evaluation
```

## Result and assumptions

[K2293](k2293-moment-controlled-positive-pump-2026-10-30.md) proves a drift-free error delta<9.272e-12 for its specified full recorded instrument, retaining its original pump. Here a centered Gaussian residual phase of variance v=10^-42 gives total error<9.327e-12 for the coherent consumer, and<9.928e-12 for its n=1 displaced-thermal consumer. Both stay below10^-11. Correlated drift across waits has a different calibration cost from independent noise. This supplies a conditional stochastic budget, not a microscopic controller or feasible actuator.

Write D=half trace distance. Every ACTUAL gate and calibration realization used here conserves Q=N_all+2K. The recorded circuit is fixed independently of the phase draw (or independently averaged); records and any external reference are retained. Noise depending on gate errors does not automatically satisfy the upper-bound hypothesis. Phase randomness is unobserved and averaged; a separately retained classical noise flag requires a different joint target and can have a larger distance. Initial fields are the same fresh vacuum registers, and the pump is coherent |sqrt(mu)> or D(sqrt(mu))tau_nD†. No arbitrary-input diamond norm claim is made.

SC-META-53 remains UNCERTAIN; positive Hilbert space and the controller are supplied. Source-native GU positivity, ledger0.263, physical control cost and energetic catalysis are unchanged.

## 1. Mixed-state lower bound and exact phase law

An idle rotation exp(-i Phi Q) commutes through the conserving circuit. The coherent pump rotates by exp(-2i Phi). For Phi~N(m,v), define

    p(lambda;m,v)=E exp[-4lambda sin² Phi]
       =E_{K,K' iid Poisson(lambda)} exp[-2v(K-K')²] cos[2m(K-K')]. (1)

This convergent Poisson expectation is an exact formula, with no large-mu approximation. It equals the overlap with the original pure pump when lambda=mu. The projector on that original state gives

    D(actual noisy output, original target)>=1-p(mu;m,v)-delta.    (2)

The target's pump is an independent unchanged factor; contractivity carries the drift-free error through the noise, and pump partial trace gives(2). It is incorrect to replace 1-p by sqrt(1-p): the noisy output is mixed. A deterministic phase has the distinct pure-state equality sqrt(1-exp[-4mu sin²m]).

For m=0, put Z=K-K'. Its moments are EZ²=2lambda and EZ⁴=2lambda+12lambda². The global bounds 1-y<=exp(-y)<=1-y+y²/2 for y>=0 imply

    4lambda v-(4lambda+24lambda²)v² <=1-p<=4lambda v.              (3)

If v<=1/[2(1+6lambda)], then 1-p>=2lambda v. These bounds are Gaussian-law specific; variance alone is insufficient for general phase laws.

## 2. Upper bound through the complete circuit

The Gaussian channel G_v has generator -[Q,[Q,.]]/2. For an initial pure state, including a purification of a mixed pump, trace-norm contractivity gives

    D(G_v(rho),rho)<=v/4 ||[Q,[Q,rho]]||_1
                 <=v/2 (sqrt(E(Q-EQ)^4)+Var Q).                  (4)

Expand the double commutator about EQ. The two Q²rho terms each have trace norm sqrt(E(Q-EQ)^4), and the middle rank-one term has norm VarQ. Finite fourth moment permits finite spectral truncation and trace-class convergence, proving(4) on this unbounded number operator. Move the noise to the input through the fixed conserving channel and use its contractivity, then add delta. For the coherent pump this gives

    D<=delta+2v[mu+sqrt(mu+3mu²)].                                (5)

For nonzero mean, a sufficient bound adds 2sqrt(mu)|m|, with m reduced modulo pi, by the deterministic rotation bound. Thus centered stochastic variance costs order mu*v, whereas deterministic residual phase costs order sqrt(mu)*|m|. Averaging is essential.

## 3. Displaced-thermal extension

For rho_alpha=D(alpha)tau_nD† and mu=|alpha|², the Gaussian overlap is

    Tr(rho_alpha rho_beta)=exp[-|alpha-beta|²/(2n+1)]/(2n+1).

Since the largest eigenvalue of rho_alpha is1/(n+1), M=(n+1)rho_alpha is an effect. Testing it yields

    D>= (n+1)/(2n+1) [1-p(mu/(2n+1);m,v)]-delta.                  (6)

This is a mixed-state measurement witness, not the pure overlap formula. A purification in(4) gives the sufficient centered bound

    D<=delta+2v[kappa2+sqrt(kappa4+3kappa2²)],                     (7)

where kappa_j are pump-number cumulants. The displaced thermal moment generating function is

    E exp(tK)=[1+n(1-exp t)]^-1
              exp[mu(exp t-1)/(1+n(1-exp t))].

For n=1, kappa2=3mu+2, kappa4=75mu+26, so the central fourth moment is27mu²+111mu+38. These are rederived by the probe; no coherent-moment substitution is used.

Using delta=9.272e-12 as conservative upper bound and v=10^-42 gives(5)<9.327e-12 at mu=10^28 and(7)<9.928e-12 at mu=4*10^28. Exact rational square-root upper enclosures verify these budgets. The phase channel preserves every number expectation. Thus the inherited actual E(N_all+1)²<6,300,000 and field error<.008 survive, as does pump depletion12.8±.004 from initial mu (coherent) or mu+1 (thermal). No claim of total engineering energy or returned energy is implied.

## 4. Correlation, positive realization, and repairs

For jointly Gaussian residual increments, the total variance is1^T Sigma 1. With W waits and per-wait variance s², independent increments yield Ws²; perfectly common increments yield W²s². At W=4*10^20 correction waits, total standard deviation10^-21 permits iid per-wait standard deviation5*10^-32, but perfectly common per-wait standard deviation2.5*10^-42. Negative correlations change this account; no white-noise assumption is free.

An unbounded additive Gaussian rate or duration cannot also stay nonnegative almost surely. The model here is a WRAPPED Gaussian residual phase. For example, supply a nonnegative integrated area A=(a+X) mod pi+ell*pi, X Gaussian, ell a nonnegative integer, then a known positive modular correction for nominal a. On the actual even-Q support this realizes the same wrapped residual channel. The construction supplies a phase law, not a physical Gaussian actuator. The correction's own drift belongs in its total residual. A distribution supported on pi*Z gives exact identity on this support even with large variance; it refutes any law-free version of(3).

A known constant beta>0 drift can instead be repaired by pausing other dynamics for s=(pi*k-phi)/beta>=0, k=ceil(phi/pi), so total phase is a multiple of pi. This includes the extra wait's phase. Pump-only compensation fails to remove the field rotation and is not a repair of the same full instrument. Unknown Q drift cannot be echoed using only admitted controls: every toggling-frame U†QU equals Q. New information, resources or a different target are required.

As a countercontrol, vacuum fields with a number-state pump occupy one Q sector; the conserving circuit stays there and every Q rotation is scalar. Noise then has zero effect. This changes the required phase-sensitive preparation and target; it does not repair the original detector (see [K2281](k2281-thermal-pump-preparation-2026-10-29.md)).

## Verification and next condition

The proof uses exact characteristic functions, Poisson/cumulant identities, a trace-class semigroup bound and contractivity. Finite coherent and thermal matrices check independent overlap and mixed-distance controls; they do not prove the universal theorem. Genuine changed-channel, covariance, cumulant and false-pure-formula controls fail the same predicates. Next requires an experimentally justified residual phase/covariance and calibration/isolation model, including all new waits; more supplied variance choices cannot establish hardware feasibility. No novelty, Lean or external-expert certification.
