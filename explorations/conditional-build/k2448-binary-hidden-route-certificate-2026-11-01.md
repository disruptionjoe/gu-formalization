---
title: "K2448 Stopping-safe binary certification on actual use indices"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "time-uniform predictable used-risk bound under hidden routing; no final-transcript or future-device guarantee"
---

# K2448 Stopping-safe binary certification on actual use indices

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
result: K2448
carrier: arbitrary history-dependent resources with a binary trusted test and independent private test/use choice LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and trace distance ON=declared_carrier
real_structure: complex Hermitian positive states and real probabilities
grading: coherent environment, recorded flags, ordered slots and private route
action_owner: repository-construction -- supplied conditional mathematical model
target: noncancelling used-risk confidence and heralded consumer MAP-TYPE=evaluation
```

## Result

Binary tests admit a sharper hidden-route certificate than a range-only square-root concentration bound. It remains valid at arbitrary stopping times and under arbitrary predictable drift. The zero-failure bound has mean loss O(1/N_U), hence K2447's mean resource-distance allowance O(1/sqrt(N_U)); it has no per-time union penalty. It does not assume independent emitted states.

This uses the established nonnegative-supermartingale/Ville framework of [Howard et al.](https://arxiv.org/abs/1808.03204). The elementary conditional calculation below is the complete argument for this specific process; no novelty or globally optimal sample complexity is asserted. SC-META-53 remains UNCERTAIN. These are supplied positive-Hilbert/statistical interfaces; source, ledger0.263 and canon remain unchanged.

## 1. Experiment and filtration

Before round t, fix the classical past filtration, the current emitted and isolated resource's conditional state and any history-selected controller. The binary test's conditional failure probability is p_t in[0,1]. Only then choose a secret independent test route T_t with fixed probability pi in(0,1); put U_t=1-T_t. On test observe X_t in{0,1} with conditional mean p_t. On use there is no test outcome; retain the resource for the declared consumer. Define

    F_n=sum_(t<=n) T_t X_t,
    N_U=sum U_t,
    Q_n=sum U_t p_t.                                      (1)

Q_n is a latent predictable risk sum sampled on actual use indices, not an observed failure count. Test/use effects must act on the same pre-route conditional resource. The device may have memory and adapt to past history. Custody, route secrecy, and all unpriced post-routing alterations remain real assumptions. Later outcomes may update knowledge of a past quantum state; they do not turn this result into a final-transcript conditional state theorem.

## 2. Exponential process and sharp coefficient

Predeclare k>0 and

    c(k)=log[1+pi/(1-pi)(1-exp(-k))].                       (2)

M_n=exp(c Q_n-k F_n) is a nonnegative supermartingale starting at one. Conditional on the past,

    E[M_t/M_(t-1)]
      =(1-pi)exp(c p_t)+pi[1-p_t+p_t exp(-k)]<=1.           (3)

Indeed exp(c p)<=1+p(exp(c)-1) for0<=p<=1, and(2) makes the remaining coefficient vanish. This proves the result without distributional or cross-round independence assumptions beyond the route and conditional binary mean. The coefficient is maximal within this fixed-k exponential family: p=1 forces (1-pi)exp(c)+pi exp(-k)<=1. This is not global optimality among every confidence sequence.

For completeness, the maximal inequality follows by stopping at the first M_n>=1/alpha and a finite horizon: the stopped nonnegative supermartingale has expectation<=1, so crossing probability<=alpha; increase the horizon. Thus with probability at least1-alpha, simultaneously for all n with N_U>0,

    Q_n/N_U <= B_k=(k F_n+log(1/alpha))/(c(k) N_U).          (4)

Values above one are safely capped at one. Optional stopping requires no additional penalty because the event is already simultaneous.

## 3. Zero failures and adaptive tuning

Define directly, rather than dividing by infinity,

    c_inf=-log(1-pi),
    M_n^inf=exp(c_inf Q_n) 1{F_n=0}.                       (5)

While alive its conditional factor is (1-pi)exp(c_inf p)+pi(1-p)<=1 by the same chord argument. After any failure it is zero forever. Consequently, simultaneously at every n for which F_n=0 and N_U>0,

    Q_n/N_U<=log(1/alpha)/(c_inf N_U).                     (6)

If p_t=1 always, surviving m consecutive uses has probability(1-pi)^m and Q=m. This exactly realizes the zero-failure exponent; claiming a larger coefficient fails on this elementary experiment. Equation(6) makes no finite bound after a failure.

For retrospective tuning, predeclare a finite or countable collection k_j in(0,infinity], weights w_j>0 with sum w_j<=1, and use alpha_j=alpha w_j. The union of crossing events has probability<=alpha, so minimize the corresponding valid bounds after seeing data. If the infinite-k candidate is included, give it its own weight and use it only when F_n=0. Giving every candidate the full alpha and selecting the most flattering result is not justified. The probe uses three declared candidates, including infinity, with weights1/3.

## 4. Calibrated loss and original program consumer

K2447 supplies a pure extension P of the original mixed program, with infidelity e_t. A trusted verification gap nu and conditional effect allowance beta_t give

    e_t<=(p_t+beta_t)/nu,
    mean_used e_t<=Q_U=min(1,(B+mean_used beta_t)/nu).       (7)

The binary probability in(1)--(6) is the actual measured failure probability, not the desired ideal infidelity. This separation prevents readout error from disappearing in a zero-count observation. A degenerate accepting subspace is not a pure-state witness; no conversion to distance is allowed without K2447's rank-one bridge.

For an r-slot qubit target, q=4^(-r), lambda=1/2 and C=2^(2r-1). K2444 gives normalized mean successful-output error <=C sqrt(Q_U)+kappa/q, with nonzero actual mean success; lambda sqrt(Q_U)+kappa<q guarantees it. kappa includes separately priced completed use-operation errors. The output benchmark uses the same history-selected controller on the ideal target, averaged over the actual use indices. It is not an independently regenerated ideal trajectory or a mean of individually normalized outputs.

Prospective example, not observations: pi=1/2, alpha=.05, zero failures, N_U=1,000,000, three-candidate simultaneous grid, nu=1/2 (the explicit two-setting K2447 verifier), beta=10^-7 and kappa=10^-6. For one original qubit slot, the infinite candidate uses log60/log2 and gives output allowance below0.70%. For two slots, N_U=10,000,000 with the same errors gives allowance below0.95%. Exact Arb256 calculations in the report verify the values and positive-success margins. Total emitted joint programs equal the actual test-plus-use count; N_U is a condition, not a deterministic launch count. Product-slot acceptance tests cost at most r trusted tests each, and ideal successes require4^r attempts on average. No giant correlated blocks or independent replicas are required, but coherent purification access and trusted operations are strictly stronger premises.

For a nontrivial target tolerance0<tau<1, a necessary condition for this sufficient bound to reach tau with finite zero-count sampling is

    mean_used beta < nu[(tau-kappa/q)/C]^2,                (8)

with tau>kappa/q; otherwise no amount of zero-count sampling makes this particular sufficient bound meet tau. The strict inequality leaves positive sampling allowance. It is a limitation of the certificate/error budget, not a lower bound on all possible experiments. For a fixed zero-failure candidate with weight w_inf and a frozen actual-use calibration budget beta_bar, solving(6)--(8) gives

    N_U >= ceil(log[1/(alpha w_inf)] /
        {c_inf*(nu*((tau-kappa/q)/C)^2-beta_bar)}).

The denominator must be positive. The probe checks the integer ceiling and its predecessor.

## 5. Hostile controls and remaining scope

The probe exhausts a small adaptive rational-probability binary tree and checks conditional supermartingale decrease, stopping/crossing probability and the absorbing zero-failure process. A separate constant-bad tree has strictly positive finite-k crossing mass from depth six, avoiding a vacuous zero-crossing check. It also checks positive-error prospective original consumers, grid allocation, the p=1 endpoint and altered c. These finite controls support the universal proof; they do not replace it.

A route-aware producer can send perfect test resources and bad use resources, producing zero failures while use error is one. A late disclosure can reveal the branch of an earlier mixed state, invalidating a retrospective reading of its predictable state. A projector onto a multidimensional subspace accepts orthogonal vectors, defeating a fixed-target-distance claim. Each is an actual changed experiment/object, not a problem with the theorem under its premises.

The mathematical confidence and coherent-resource interface now compose. Applying them needs actual trusted joint custody/access, coherent flag/environment preservation, known verification effect, independent route, storage/control costs and outcomes. If these cannot be supplied, the theorem does not certify the existing measured instrument by itself. K2445's no-purification alternative remains available, and the native source-to-physics and mixed hook convergence questions remain distinct.

[Exact probe](../../tests/channel-swings/k2448_binary_hidden_route_certificate_probe.py), [report](../../lab/process/k2448-binary-hidden-route-certificate.json). Written universal arguments, finite exact controls and prospective numerical budgets are separate evidence. Internal independent review is not external-expert or proof-assistant certification.
