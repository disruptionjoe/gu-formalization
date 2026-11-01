---
title: "K2450 Stopping-safe certification with bounded test/use leakage"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional time-uniform branch-risk theorem; no inference of secrecy from test records"
---

# K2450 Stopping-safe certification with bounded test/use leakage

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
result: K2450
carrier: branch-conditional quantum resources or binary risks with predictable route probabilities LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace distance and real conditional probabilities ON=declared_carrier
real_structure: supplied real exact coefficients or complex positive Hilbert states as explicitly typed below
grading: past filtration, test and actual-use branches
action_owner: repository-construction -- supplied conditional mathematical model
target: robust used-risk confidence and original heralded consumer MAP-TYPE=evaluation
```

## Result

Perfect test/use indistinguishability can be replaced by a stated bound on the conditional difference of the two branches. The resulting certificate has an unavoidable leakage floor and an exact optimal exponent within a specified exponential family. This makes the routing premise quantitative; it does not measure or establish that premise. The general supermartingale framework is established [Howard et al.](https://arxiv.org/abs/1808.03204); the conditional calculation below is self-contained, with no novelty claim.

These are supplied positive-Hilbert and statistical models. SC-META-53 remains UNCERTAIN; no native GU physical quotient or empirical observation is supplied. Source, ledger0.263 and canon are unchanged.

## 1. Conditional experiment

Before round t and conditional on its classical history, specify pi_t in(0,1), test risk pT_t, use risk pU_t, and a predictable certified delta_t in[0,1] satisfying

    pU_t <= pT_t+delta_t.                                 (1)

The route has conditional test probability pi_t. On test observe binary X_t of conditional mean pT_t; on use retain the resource. Branch states may differ, and arbitrary dependence on earlier history is permitted. Here pU is the hypothetical failure probability of the same trusted test on the use-branch state, not an observed use outcome. It is predictable conditional on history and branch type.

A sufficient quantum premise is D(rhoU_t,rhoT_t)<=delta_t for same-history normalized branch states and the same binary effect. Variational trace distance implies(1). If effects differ by operator norm eta_t, replace delta by min(1,delta+eta). Average state distance, a global route-guessing advantage, or earlier device calibration does not automatically establish this per-history bound. The certificate concerns predictable states at actual use indices, not states conditioned on a final transcript or future devices.

## 2. Sharper shifted-risk process

For delta<1 put L=1-delta, h=(pU-delta)_+, r=1-exp(-k), k>0 and

    c_delta=log(1+pi r L/(1-pi))/L.                        (2)

Then h<=L and pT>=h. The conditional multiplier satisfies

    (1-pi)exp(c_delta h)+pi(1-r pT)
       <=(1-pi)[1+h(exp(c_delta L)-1)/L]+pi(1-rh)=1.

The inequality is the exponential chord on[0,L]. Consequently

    M_n=exp(sum U_t c_t h_t -sum T_t k_t X_t)              (3)

is a nonnegative supermartingale. Parameters pi,delta,k may be selected predictably from the past; selection using the current unobserved branch/outcome is excluded. For delta=1 set h=0,c=0: that round contributes no information.

Stopping at the first M_n>=1/alpha, then increasing finite horizons, proves that with probability at least1-alpha, simultaneously for all n,

    sum U_t c_t h_t <= sum T_t k_t X_t+log(1/alpha).       (4)

For constant parameters and N_U>0,

    mean_used pU <= min(1,delta+(kF+log(1/alpha))/(c_delta N_U)). (5)

For varying delta,c with strictly positive c_min among actual uses, replace delta by its actual-use mean and divide the right side of(4) by c_min N_U. Keeping(4) weighted can be stronger. A round with c=0 prevents this particular unweighted conversion; it cannot be silently dropped from the mean. Predictable tuning is allowed; choosing retrospectively among complete processes requires an alpha allocation or valid mixture as in K2448.

## 3. Zero failures, exact sharpness, and impossibility floor

Take k=infinity directly: r=1 and define M_inf=exp(sum U_t c_inf,t h_t)1{F=0}, omitting the finite-k failure sum. After the first failure the process stays zero. Equations(4)--(5) with no kF term hold only at zero failures. The coefficient is maximal within this shifted-risk exponential family: pT=L,pU=1 forces(1-pi)exp(cL)+pi(1-rL)<=1.

For zero failures with these risks, the probability of reaching m uses before any test failure is

    [(1-pi)/(1-pi+pi L)]^m=exp(-c_delta L m).

This includes any number of passing tests and exactly saturates the exponent. The risks are physically realized by commuting qubit states rhoU=|bad><bad|, rhoT=delta|good><good|+L|bad><bad| and failure effect |bad><bad|; their trace distance is delta.

There is an unavoidable identification floor: choose pT=0,pU=delta. Route and test records have exactly the same law as pT=pU=0, while use risk differs by delta. No certificate based solely on those records can uniformly converge below delta under only(1). With delta=1 it cannot infer any nontrivial use quality. This is a model-class information obstruction, not a claim that extra use data or stronger custody guarantees cannot help.

For comparison, retaining K2448's original c0=log(1+pi r/(1-pi)) gives the exact smallest deterministic all-round compensation

    d0=log(1+pi r delta),
    exp(sum U c0 pU-sum T kX-sum d0).                    (6)

Piecewise convexity in pT reduces the largest conditional factor to pT=0,L,1; these give(1-pi)exp(c0 delta)+pi,1+pi r delta,1. The middle is maximal by the chord inequality. This sharp compensation theorem concerns(6), not global dominance: the shifted actual-use process and(6) need not dominate pathwise. Both are reusable, but the shifted process exposes the correct delta floor.

## 4. Original program consumer and feasibility

Use any trusted verifier for K2447's original pure extension with gap nu, actual conditional effect allowance beta_t, and the same effect interpretation on the use branch. Then mean used infidelity is at most Q=min(1,(B_U+beta_bar)/nu), with B_U from(5). K2444's r-slot qubit heralded consumer gives

    output distance <= min(1,C sqrt(Q)+kappa/q),
    q=4^(-r), C=2^(2r-1),

provided actual mean success is nonzero; (1/2)sqrt(Q)+kappa<q suffices. This is the success-weighted normalized mean with the same history-selected ideal controllers. It is neither a final-transcript process theorem nor the mean of individually normalized outputs.

At zero failures, target tolerance tau in(0,1) requires this certificate's strict asymptotic allowance

    delta+beta_bar < nu[(tau-kappa/q)/C]^2,  tau>kappa/q.   (7)

With positive denominator D=nu[(tau-kappa/q)/C]^2-delta-beta_bar, sufficient actual-use count is ceil(log(1/alpha)/(c_delta D)). This is a prospective design threshold, not observations or a sample-complexity lower bound. The probe checks one/two-slot original consumers using the existing nu=1/2, delta=beta=10^-7, kappa=10^-6, alpha=.05 and tau=.01, including predecessor integer failure. K2451's fully local verifier may be substituted only with its actual smaller proved gap and separately calibrated errors; free gap substitution is invalid.

## 5. Evidence and remaining inputs

The probe checks exact rational endpoint factors, strict failures when compensation or leakage is omitted, a complete adaptive finite tree, quantum trace-distance witnesses, nontrivial crossing events and Arb256 budget intervals. Universal time validity comes from the proof, not finite enumeration. Actual per-history branch separation, effect calibration, coherent custody and use-operation data remain missing. The new theorem prices those assumptions instead of treating secrecy as an observed outcome.

[Exact probe](../../tests/channel-swings/k2450_route_leakage_certificate_probe.py), [report](../../lab/process/k2450-route-leakage-certificate.json). Universal proofs, finite original-object checks and prospective budgets are separate evidence. Internal independent review is not external-expert or proof-assistant certification.
