---
title: "K2322 Protected-reference compiler"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2322_protected_reference_compiler_probe.py
---

# K2322 Protected-reference compiler

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2322
carrier: fixed total-N two-mode shell with pilot loss, protected reference, lower loss sectors and neutral final flag LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form, trace distance and offdiagonal control norm ON=declared_carrier
real_structure: complex adjoint; positive real amplitudes for the explicit schedule
grading: total photon number and sensing occupation n
action_owner: repository-construction -- K2320 Markov loss and K2315 occupation-neighbor controls
target: arbitrary-stock exact conditional preparation, reachability threshold and resource/error bounds MAP-TYPE=evaluation
```

## Fixed task and the completed gap

Use [K2320](k2320-lossy-selective-calibration-2026-10-30.md)'s pilot-only loss sqrt(gamma)a_P, protected reference, no replenishment before a final total-number flag, and deterministic preparation. Start at |0,N>. Controls preserve total number, connect only adjacent sensing occupations n, and have ||H_off||<=hbar J, J>0; arbitrary diagonal controls are allowed. Lower shells have number-preserving extensions, with no return to shell N after a loss. The environment is inaccessible. The target is [K2312](k2312-relational-finite-calibration-2026-10-30.md)'s positive sine vector

    c_n=sqrt(2/(N+2)) sin[(n+1)pi/(N+2)], n=0,...,N.

All rates, selective controls, phases, timing and a perfect final shell test are supplied. This is occupation locality, not spatial locality or a microscopic device model. Imported positive quantum mechanics is not native GU quantization; SC-META-53 remains UNCERTAIN and ledger0.263 unchanged.

The exact normalized no-jump target is reachable in finite time **if and only if gamma<4J**, for every integer N>=1. Below threshold an explicit backward elimination compiles a forward sequence of at most N physical pulses. It compensates the loss of ALL spectator amplitudes; using loss-free Givens angles would not do so. This solves the arbitrary-stock conditional preparation gap, with a resource bound, rather than inferring it from the one-photon case.

## Backward anti-loss elimination is a calculation, not an allowed operation

Write gamma>=0, a=gamma/(4J)<1, nu=J sqrt(1-a²). Starting at c, process k=N,N-1,...,1. On pair (k-1,k) use the real antisymmetric matrix

    B_k = [[0,J],[-J,0]].

The backward calculation evolves x'=B_k x+(gamma/2)n x, all other control entries zero. Its inverse is a physically allowed forward no-jump pulse with amplitude generator -B_k-(gamma/2)n, hence H=-i hbar B_k, ||H_off||=hbar J. Anti-loss is never applied experimentally and no negative damping is assumed.

Let the current positive pair be (x,y), with angle theta=atan2(y,x). Common gain drops out of the ratio and

    theta'=-J+(gamma/4)sin(2theta).

The denominator J-(gamma/4)sin2theta is positive on [0,pi/2]. Eliminate y after

    tau_k=integral_0^theta du/[J-(gamma/4)sin2u]
         =atan2(nu*y, J*x-gamma*y/4)/nu.                  (1)

atan2 takes its value in [0,pi]; a one-argument arctangent is wrong when its denominator is negative. Zero y needs zero time. On this pair the backward exponential is

    exp[gamma(2k-1)t/4] {I cos(nu t)+C sin(nu t)/nu},
    C=[[-gamma/4,J],[-J,gamma/4]], C²=-nu² I.            (2)

The higher-occupation component y is zero at (1); the lower-occupation component x remains positive. Spectator j scales by exp(gamma*j*t/2); zeros above k remain zero. After all stages the backward vector equals C0|0>, C0>=1. Invert those stages in reverse order (forward pairs k=1,...,N). The actual physical no-jump output is exactly c/C0. Its normalized output is c and

    p=C0^-2=exp[-gamma E], E=integral_0^T <n>_conditional dt. (3)

The final N-shell flag identifies precisely this branch. All lost outcomes count as failed launches; (3) is not a statement about using lossy branches for estimation.

## Time and photon-exposure bounds

Every stage obeys

    tau_k<=tau_max=(pi/2+arcsin a)/(J sqrt(1-a²))
                   <=pi/[2(J-gamma/4)],
    T<=N tau_max.                                           (4)

The first identity integrates over the complete quarter-circle. A sharper exposure bound uses the active support. During backward stage k, support is at most k and the pair's normalized upper fraction is sin²theta. Thus <n><=k-1+sin²theta, even with arbitrary spectator weights below k-1. The normalized forward path is exactly the reverse of this backward path. By theta to pi/2-theta symmetry,

    E_k <= integral_0^(pi/2) (k-1+sin²u)du/[J-gamma sin2u/4]
         =(k-1/2)tau_max,
    E <= N² tau_max/2 <= pi N²/(4J-gamma),
    p >= exp[-gamma N² tau_max/2].                           (5)

The bound is uniform in positive target amplitudes; it is not claimed optimal. K2320's independent necessary exposure bound for the exact sine endpoint remains E>=N²/(8J). The necessary and achieved bounds therefore agree in N²/J scaling at small gamma/J, without solving time- or survival-optimal control for N>1.

For a permitted failure epsilon in (0,1), L=-log(1-epsilon), a necessary condition for this exact-sine flagged preparation is

    gamma/J <= 8L/N².

An explicit conservative sufficient condition from (5) is

    gamma/J <= 4L/(pi N²+L),                                (6)

which automatically implies gamma<4J. A log-free still sufficient condition replaces L by epsilon. For the K2312 stock N=3*10^27, epsilon=1/172 is the inherited sufficient all-launch confidence loss budget; epsilon=5*10^-13 is the separate inherited actual-record average-error loss budget. Equation (6) prices achievable preparation, not a measured rate relation or hardware feasibility. It improves on treating N as occupied throughout every pulse, but does not remove the quadratic exposure burden.

## Necessity: a whole-control-class population barrier

The threshold is not merely a limitation of the sequence. Cut the shell into n=0 and n>=1 and write normalized tail mass q=sin²theta. Its tail conditional mean mu>=1. For ANY permitted control, the head-tail cross block has norm at most hbar J (only edge 0 to1 crosses). Hamiltonian population flow is at most 2J sqrt(q(1-q)), while conditioning on no pilot loss contributes -gamma mu q(1-q). Therefore wherever 0<q<1,

    theta' <= J-(gamma/4)mu sin2theta
            <= J-(gamma/4)sin2theta.                       (7)

Arbitrary diagonal phases and all within-tail controls cannot improve this bound. Starting at theta=0, for gamma>4J the first zero of the right side is theta_bar=asin(4J/gamma)/2<pi/4; comparison prevents crossing it. At gamma=4J, speed vanishes quadratically at pi/4, so integral dtheta/[J(1-sin2theta)] diverges and no finite-time path reaches it. This follows also from the scalar comparison solution and covers nonmonotone paths; endpoint differentiation at q=0 is handled by continuity. Bounded measurable controls give absolutely continuous trajectories.

The sine target has q_s=1-2 sin²[pi/(N+2)]/(N+2)>=1/2, with equality only at N=1. Thus (7) forbids the exact sine endpoint in finite time for gamma>=4J. With

    q_bar=(1-sqrt(1-(4J/gamma)²))/2,

any reachable normalized no-jump state at gamma>=4J has trace distance at least q_s-q_bar from the sine target, by the two-outcome head/tail measurement. At the critical rate this is a positive approximation obstruction for N>=2; for N=1 it gives zero, consistent with asymptotic approach. This is a bound on this initial state, loss placement, number-conserving adjacent control and exact conditional target. It is not a universal phase-sensing impossibility or an optimal error formula.

## Released follow-through: actual errors and a vulnerable storage interval

Let K_i be the ideal physical no-jump contractions and Ktilde_i the implemented no-jump contractions on the same shell. If ||Ktilde_i-K_i||<=e_i and eta=sum e_i, telescoping gives raw output error <=eta. Put sqrt(p)=1/C0. When eta<sqrt(p),

    ptilde >= (sqrt(p)-eta)²,
    D(normalized actual,c) <= eta/sqrt(p).                    (8)

For the distance bound, distance from the ideal vector sqrt(p)c to the complex line through the actual vector is sqrt(p) times the sine of their angle and cannot exceed their vector distance. These are errors of the ACTUAL lossy contractions; a unitary-only pulse bound does not automatically bound drift, rate and timing errors. Errors that add gain or invalidate the final flag require another model.

For example, if a common duration and only Hamiltonian/rate errors are present, contractive Duhamel gives e_i<=integral[||Delta H_i||/hbar+N|Delta gamma_i|/2]dt. Summed error controls the full compiled endpoint even when controls fail to commute. This gives a concrete tolerance interface for calibration and rate uncertainty; it does not grant physically available tolerances.

To combine exact (3) with K2312's ideal single-query/retained-pump task, explicitly grant instantaneous ideal query, readout and inverse actuation immediately after the preparation flag, with independent working pump untouched during preparation. Then success>=p*(43/45) and actual-record average error<9.491e-12+(1-p). With (8), success>=(sqrt(p)-eta)²*(43/45-eta/sqrt(p)) when the bracket is positive, and average error<=9.491e-12+1-(sqrt(p)-eta)²+eta/sqrt(p). The independent pilot affects the working output only through its classical outcome distribution: the fixed-phase good-event set and each outcome's bounded error cost in [0,1] are unchanged, so total-variation distance changes either risk by at most eta/sqrt(p), as in K2309. This is not a generic joint-output perturbation theorem. These are sufficient, distinct goals, charging failures at worst cost1. A noninstantaneous arbitrary readout is not covered.

A specified pilot-only pure-loss storage interval T_o with no Hamiltonian can be included exactly. Known diagonal phases may also be canceled by the supplied diagonal controls; unknown phases are not covered. Backward-compile the normalized pretilted target

    b_n=exp(gamma n T_o/2)c_n/Z, Z=||exp(gamma n T_o/2)c||.

It remains positive. After storage its normalized no-jump state is c; total survival is p_prep/Z². Place the final N-shell flag AFTER storage so it detects losses during both intervals; a preparation-only flag cannot herald the later no-loss branch. Since Z²<=exp(gamma N T_o), total exposure is bounded by the right side of (5) plus N T_o. The phase query commutes with this storage if granted separately. General lossy/noncommuting readout and physical reset still need their own complete instrument, rather than the equal-loss scalar survival shortcut. The uncorrected storage counterexample in K2320 remains valid.

## Charged renewal and what is still unpriced

For the full pilot-loss process, expected lost photons per attempt are ell=gamma integral E[n_P(t)]dt. Since the total shell population never exceeds N, ell<=gamma N T, and ell<=N(1-p) because no-loss attempts lose zero and every failed attempt loses at most N. Neither ell=N(1-exp(-gamma T)) nor exp(-gamma N T) is an equality here; those belong to different loss placements. For iid complete-duration attempts with exact stock restoration after each flag, expected replaced photons until success are ell/p<=N(1-p)/p, and replacement charge is twice that. This is a renewal identity, not permission to repeat a single-query experiment without charging the new queries.

The neutral outcome-memory/reset burden of K2320 survives. A thermal reservoir, Hamiltonian spectrum and microscopic relation gamma(J), selector implementation and clock/readout error are still absent. Exact formal controllability does not establish feasibility at N=3e27. No novel metrology optimum, external-expert verification or native GU verdict is claimed. The standard no-jump formalism is inherited from K2320; the all-stock construction and barrier are proved above and checked by independent finite controls in the companion probe.
