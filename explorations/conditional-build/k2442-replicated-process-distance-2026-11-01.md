---
title: "K2442 A two-copy certificate that cannot hide drift by averaging"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional independent replicas or priced pair defect; tested predictable mean distances only"
---

# K2442 A two-copy certificate that cannot hide drift by averaging

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
result: K2442
carrier: pairs of normalized original flagged process Choi states on dimension N=12^r LAYER=toy CHIRALITY=N/A
pairing: Hilbert-Schmidt loss, trace norm and strategy distance ON=declared_carrier
real_structure: complex positive Hermitian states and completely positive causal maps
grading: declared temporal slots and classical flags
action_owner: repository-construction -- supplied conditional mathematical model
target: noncancelling mixed-target certification and correlated-pair counterexamples MAP-TYPE=evaluation
```

## Result

Signed tomography can hide opposite errors around the original mixed instrument. A trusted **pair** of conditionally independent copies supplies a nonnegative squared-distance score and thereby certifies the mean of individual process errors. The pair-independence assumption is essential: an explicit correlated original-instrument pair has identical marginals, valid TP constraints and score zero while both marginals are wrong.

The squared-Hilbert-Schmidt testing idea is established, including [Fanizza, Salvia and Giovannetti](https://quantum-journal.org/papers/q-2023-09-11-1105/). This result specializes a fully stated drift/replica interface to the original instruments and proves its exact failure modes and conditional consumers. No novelty, measured replica mechanism or native GU identification is claimed. SC-META-53 remains UNCERTAIN; ledger0.263/source/canon unchanged.

## 1. Why one-copy nonnegative losses fail here

The original target sigma is strictly positive on its rank9 support. The supported TP affine family has29 nonzero tangent directions (K2438/K2439). Every one-copy expected score is affine in rho. If it is nonnegative on this feasible family and zero at sigma, evaluating sigma±tH for small positive t forces its linear part to vanish on every supported TP tangent H. It cannot identify sigma. A positive zero-failure effect is even more directly blind: zero at sigma forces it to annihilate its entire support.

This is a scoped impossibility for a universally nonnegative affine expected loss. It does not prohibit signed tomography, nonlinear processing of many independent observations, or tests under additional promises.

## 2. Exact pair loss and measurements

Set c=Tr(sigma²), let S exchange the two full program registers, and define

    H_sigma = S-sigma tensor I-I tensor sigma+c I.
    Tr[H_sigma(rho tensor rho)] = ||rho-sigma||_2² = q_rho.    (1)

The eigenvalues, in a sigma eigenbasis with eigenvalues lambda_i, are
1-2lambda_i+c on |ii>, and ±1-lambda_i-lambda_j+c for i<j. All lie in[-2,2]: for different indices lambda_i+lambda_j<=1, and c<=1. For the diagonal vector1-2lambda_i+c >=(1-lambda_i)²>=0. Hence a trusted measurement score X has |X|<=2 and second moment<=4. q_rho lies in[0,2].

Classical flags do not require coherent superposition of flags. On the block-diagonal pair carrier, replace S by its dephased version: read both flag strings, use quantum-register SWAP when they agree, and zero swap contribution otherwise. The sigma terms are block diagonal and commute with this compressed swap. A joint spectral measurement therefore realizes the expectation and the same norm bound. This requires trusted pair operations/eigenbasis measurements, not merely old one-copy Pauli counts.

Condition on history **before the entire pair emission**. The premise is Omega_t=rho_t tensor rho_t. It permits arbitrary drift with t but not merely equality of marginals or independence after conditioning on a hidden label not present in the declared filtration.

## 3. Confidence and preparation accounting

For X_t from(1), centered increments are bounded by4 and conditional variance by4. With L_n=log(2n(n+1)/alpha), the usual scalar Freedman union gives simultaneously at every n:

    mean q_t <= mean X_t + sqrt(8L_n/n)+8L_n/(3n).             (2)

If D(Omega_t,rho_t tensor rho_t)<=xi_t, score bias is at most4xi_t. If both actual marginals equal rho_t exactly, the linear terms cancel and the bound improves to2xi_t because only S remains. Add a trusted observable-norm error eta_t. Require the implemented score to remain in[-2,2] (bounded calibration preserves the concentration premise). Add these mean allowances to(2), then clip the resulting upper bound to[0,2] on its confidence event, calling it Q. A negative unrounded upper bound is an inconsistency event; no negative physical loss is inferred.

Cauchy-Schwarz and Jensen now yield

    mean D(rho_t,sigma) <= min(1,sqrt(N Q)/2),
    mean delta_strategy <= min(1,C sqrt(N Q)/2),              (3)

when every rho_t is a normalized causal comb. For the original r-slot flagged process N=12^r. K2441 equation(2a) sharpens K2438's conservative factor to C=min(K²,D²/d_A1)=2^(2r-1). If sigma and **every actual rho_t share the same declared support subspace P** of dimension9^r, independently established, N=9^r is permitted. Individual ranks, unrelated supports or target support alone do not suffice.

When measured resource preparation is imperfect and the actual output states need not be causal Choi states, K2432's transfer to each ideal Bell-input comb with its same initial memory marginal costs mean f(qprep_t)<=f(e), where f(e)=(e+sqrt(4e-3e²))/2. The ideal-process mean bound is

    min(1,C[sqrt(N Q)/2+f(e)]).                              (4)

Replica defect is inside Q; preparation transfer is outside its square root. No calibration independence is needed for a unioned1-alpha-beta confidence statement. Neither error is silently set to zero by matching observed marginals.

## 4. Exact original correlated counterfeit

In each original law take H supported solely in the plus flag block as Z_R tensor Y_B, t=1/100000, and

    rho=sigma+tH,
    Omega=sigma tensor sigma+t(sigma tensor H+H tensor sigma)
         =rho tensor rho-t² H tensor H.                      (5)

H is Hermitian, trace zero, has output partial trace zero, operator norm1 and squared Hilbert-Schmidt norm4. The original support minimum is
mu=min(1-w,w(1-l)/16): it equals73/41600 and111/8320 for the two laws. Thus rho is positive, and congruence of Omega by the inverse square root of sigma on its support bounds it below1-2|t|/mu>0. No large symbolic eigenvalue computation is needed.

Both pair marginals are rho; each is TP, and tracing both pair outputs gives I4/4. Omega is exchange-symmetric and is also a valid parallel TP channel Choi state. Nevertheless

    Tr(H_sigma Omega)=0,
    ||rho-sigma||_2²=4t²,
    D(rho,sigma)=2|t|>0.                                     (6)

This is a counterfeit of the **independence premise**, not of the theorem. Direct score and marginals cannot certify their own tensor factorization. Conversely the true independent pair has score4t²; alternating sigma±tH gives perfect signed average tomography but the same positive pair score in every round.

## 5. Released successor: hidden use and adaptive choices

Emit the same conditional pair before a private test/use coin of probability pi. On tests measure H_sigma; on use retain its first marginal as the program, discarding the second. For exact independent replicas define q_t=||rho_t-sigma||_2², U=1-T, a=(1-pi)/pi,

    Z_t=a T_t X_t-U_t q_t,
    E(Z_t|past)=0,
    |Z_t|<=b=max(2a,2), E Z_t²<=v=4pi a²+4(1-pi).

With N_U>0, hat q_U=a sum T_t X_t/N_U and the same L_n as(2),

    (sum U_t q_t)/N_U <= hat q_U+[sqrt(2nvL_n)+2bL_n/3]/N_U.   (7)

Pair/readout bias beta_t<=4xi_t+eta_t adds
sum(1-pi)beta_t/N_U; use b'=b+(1-pi)beta_max when centering. The second moment v still applies if scores remain bounded by2. If an approximate pair is defined relative to rho_t tensor rho_t but the actual retained marginal differs, also add its mean trace-distance defect after the square root. Any preparation, retained-marginal or operation allowance used here must bound its average over the **actual used indices** (or hold uniformly per round). A full-sample mean bound alone does not certify that selected subset. Under exact equal marginals no extra term is needed; this is distinct from the factor2 score improvement.

Equations(3) and(7) bound mean state distance at the **actual used indices**. Therefore controller T_t may now depend on pre-batch classical history: each fresh private controller initialization remains independent of the current resource and device. K2441's completed-program map for each T_t contracts its own state's distance; averaging gives total success-output difference at most2e where e=sqrt(N Q_U)/2 plus trusted operation and any marginal-defect allowances. Since the target success is the same q=D^-2 for every controller,

    D(normalized mean actual success,
      mean ideal controller output) <= e/(q-e), e<q.          (8)

This is the normalized mean subchannel with success weighting. It compares to the target outputs for the same history-selected controllers, not a recursively generated ideal-history distribution. It is not a final-transcript conditional or across-batch joint-process theorem. Correlation with an external quantum data memory remains an independent missing premise. Arbitrary within-batch adaptation is allowed via K2441.

## 6. Consequences and costs

For causal combs the mean squared strategy distance is at most C² N Q/4. Thus the fraction of tested/used indices with distance>=tau is at most min(1,C² N Q/(4tau²)). A probability weighting bounded by R/n gives mean strategy distance at most min(1,C sqrt(N R Q)/2). These follow from the same nonnegative losses; signed tomography cannot supply them. Add any separately priced preparation transfer before making claims about counterfactual ideal processes.

Near zero empirical score, the simple bound has n^(-1/4) distance scaling. The report evaluates direct and hidden-use one-slot sufficient budgets at n=10^12 with alpha=.05, zero empirical residual and ideal calibration. It also prices nonzero pair/readout error floors. These are prospective examples, not achieved precision or a sample-optimal test. Two copies, trusted pair measurements, routing isolation and marginal/private-data independence are real added resources. Increasing samples does not remove a replica bias floor.

[Probe](../../tests/channel-swings/k2442_replicated_process_distance_probe.py), [report](../../lab/process/k2442-replicated-process-distance.json). Exact original-law controls, spectral identities, martingale moments and rigorous numerical allowances supplement the universal proofs. Independent internal review is not proof-assistant or external-expert certification. The next practical requirement is independently evidenced replicas or another noncancellation mechanism; no test here provides that evidence for itself.
