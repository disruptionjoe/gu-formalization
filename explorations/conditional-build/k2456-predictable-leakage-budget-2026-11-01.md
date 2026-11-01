---
title: "K2456 Predictable leakage costs with endpoint-safe stopping certificates"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional same-use-risk supermartingale with justified predictable budgets; no measured routing or native GU state"
---

# K2456 Predictable leakage costs with endpoint-safe stopping certificates

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
result: K2456
carrier: classical histories and the original conditional test/use states on positive Hilbert programs LAYER=toy CHIRALITY=N/A
pairing: binary probability kernels, positive Hilbert trace and conditional Cauchy-Schwarz ON=declared_carrier
real_structure: real probabilities and normalized complex positive states
grading: test versus use, actual versus auxiliary one-step kernels, predictable versus observed data
action_owner: repository-construction -- supplied conditional mathematical experiment
target: stopping-safe original predictable actual-use risk with finite support-safe cost MAP-TYPE=evaluation
```

## Result and relation to prior work

A predictable accumulated likelihood-moment budget gives a stopping-safe
certificate directly under the actual law. Smoothing an auxiliary test mean
makes the cost finite even when the actual use risk is one and the test risk
is smaller, where K2453's exact-use reference has infinite relative entropy.
The price is a residual leakage allowance and a weaker finite-sample rate.
No test record alone establishes these budgets or the unobserved use risks.

This uses the same frozen conditional use state and private-controller
requirements as K2450/K2453. It neither replaces that state by a source
marginal nor models quantum memory as hidden classical labels. The framework
of time-uniform bounds from nonnegative supermartingales is established
[Howard et al.](https://arxiv.org/abs/1808.03204). The complete specialized
argument below makes no novelty claim. SC-META-53 remains UNCERTAIN;
LT-SM8, source, ledger 0.263 and canon are unchanged. This is conditional
probability on supplied positive Hilbert resources, not a GU quotient.

## 1. One-step construction on the same actual risk

At each pre-round history fix predictable values pi in (0,1), a=pT and
b=pU in [0,1], and choose eta in (0,1). Here a is actual test failure
probability; b is the failure probability of the trusted effect on the
actual normalized use-branch state. Fix these functions including versions
at any needed null histories. Choose k>0 predictably. Define

    d=(b-a)_+, q=a+(1-eta)d, delta=eta d,
    h=b-delta, L=1-delta,
    c_delta=log(1+pi*(1-exp(-k))*L/(1-pi))/L.

Then 0<=h<=L, q>=h, L>0. The one-step auxiliary law keeps routing and
all conditional continuation kernels fixed and replaces only the test
Bernoulli mean a by q. Actual P is absolutely continuous with respect to
this Q: if a!=q then q is strictly between zero and one; if a=q the laws
coincide, including endpoints. No physical auxiliary quantum experiment
is asserted. A one-step calculation suffices; global path densities are
unnecessary.

Let U indicate use, T indicate test, and X the observed test failure.
Set m=exp(U*c_delta*h-T*k*X). Under Q,

    E_Q m=(1-pi)*exp(c_delta*h)+pi*(1-q+q*exp(-k))<=1.

Indeed q>=h and the chord of exp on [0,L] give the bound, with equality
at h=0 or L in the matching extreme case. For the conditional likelihood
ratio ell=dP/dQ, let

    v=(a-q)^2/[q(1-q)],  v=0 when a=q in {0,1}.

Direct summation gives E_Q ell^2=1+pi*v. Cauchy-Schwarz gives

    E_P sqrt(m/(1+pi*v))
      = E_Q[ell*sqrt(m)]/sqrt(1+pi*v) <=1.

Therefore the product N_n of these nonnegative multipliers starts at one
and is a P-supermartingale even with adaptive history-dependent states,
routing, eta and k. Put B_n=sum_(t<=n) log(1+pi_t*v_t). Ville's inequality
(or the elementary stopped-supermartingale argument followed by increasing
finite horizons) gives, with probability at least 1-alpha, simultaneously
for every n,

    sum U_t*c_delta,t*(b_t-delta_t)
       <= sum T_t*k_t*X_t + B_n + 2 log(1/alpha).          (1)

Consequently the same event covers any stopping time. B_n is predictable
but need not be observable from the transcript; an independently justified
upper bound can replace it. Fitting a, b or B from the same test counts
without a valid additional argument is not licensed. Predeclared mixtures
or union bounds can compare tuning choices; arbitrary retrospective choice
with the full alpha for each cannot.

For zero failures take k=infinity, replace c_delta by
log(1+pi*L/(1-pi))/L, and let m become zero on a test failure.
The product remains absorbing at zero. Equation (1) with the failure term
omitted then applies only to prefixes with F_n=0. It cannot restart after
forgetting failures without a separately justified construction.

## 2. Released bounded-cost consequence on actual uses

Fix pi, eta and k. At any prefix with N_U=sum U_t>0, let B be any justified
upper bound on B_n. It may be a random time-varying bound if B_n<=B holds pathwise almost surely,
since (1) holds simultaneously. A confidence-qualified budget requires
adding its failure probability to the final allowance. Products of nonnegative factors imply

    sum v_t <= (exp(B_n)-1)/pi <= (exp(B)-1)/pi.

Also delta_t=eta*|q_t-a_t|/(1-eta)
<=eta*sqrt(v_t)/(2(1-eta)). Cauchy-Schwarz over the actually used rounds
and monotonicity of log(1+x L)/L give

    A(B)=eta/[2(1-eta)]*sqrt((exp(B)-1)/pi),
    c0=log(1+pi*(1-exp(-k))/(1-pi)),
    mean_used b <= min(1, A(B)/sqrt(N_U)
          + [k F_n+B+2 log(1/alpha)]/(c0*N_U)).           (2)

This conclusion keeps the original use-weighted predictable risk. It is
not a posterior guarantee on a final transcript, a future resource or a
coherent joint multiround state. For zero failures use c0=-log(1-pi).
A fixed all-prefix bound B gives risk O(N_U^-1/2), hence trace-distance
and a statistical heralded-output contribution O(N_U^-1/4) under the usual
square-root transfer. Fixed calibration and operation errors leave a floor;
the full output rate applies only when those errors also vanish.
When B=0 the residual allowance vanishes and risk is O(1/N_U), although
the Cauchy-Schwarz construction still pays twice the logarithmic threshold.
K2448 remains sharper when exact branch equality is justified.

Fixed nonzero harmful leakage with fixed pi and eta has a uniformly positive
cost increment and makes B_n grow linearly. Positive but shrinking costs
need not do so.
The theorem does not erase a constant leakage floor. Endpoint a=0,b=1 gives
q=1-eta and v=(1-eta)/eta, finite but costly. Harmless a>=b gives q=a,
v=delta=0. Omitting B_n can destroy the supermartingale: pi=eta=1/2,
a=0,b=1,k=infinity gives uncorrected conditional mean
(1+sqrt(3/2))/2>1. Dropping the residual delta likewise invalidates the
claimed risk; smoothing changes the cost and allowance together.

## 3. Same original heralded consumer

Suppose the complete trusted verifier has proved gap nu and calibration
allowance beta_t on each use-branch state, so its infidelity is at most
(b_t+beta_t)/nu. If beta_bar bounds the actual-use average of beta_t,
K2444/K2450 give the success-weighted mean output allowance

    C*sqrt((mean_used b+beta_bar)/nu)+kappa/qherald.

Here qherald>0 is the ideal heralding probability; C is the ideal
program-to-output constant; kappa is the completed-operation error.
The controller starts privately and has no current-resource E/test data;
prior classical history may choose it. Compare the same history-selected
ideal controllers. Actual mean success must be nonzero; a sufficient condition
is sqrt(Q)/2+kappa<qherald, where Q=min(1,(mean_used b+beta_bar)/nu).
This does not certify a final
transcript-conditioned or joint-process error.

For target tau>kappa/qherald set
D=nu*((tau-kappa/qherald)/C)^2-beta_bar>0. Under zero failures and a justified
fixed B, a sufficient actual-use count is

    H=(B+2 log(1/alpha))/(-log(1-pi)),
    N_U >= ceil(((A(B)+sqrt(A(B)^2+4*D*H))/(2*D))^2).     (3)

The exact probe evaluates (3) with both original K2454 gaps and prospective
pi=eta=1/2, alpha=.05, B=10^-6, beta_bar=10^-8,
kappa=10^-6, qherald=1/4, C=2 and tau=.01. The sufficient counts are 1,411,060 and 1,444,981 actual uses, respectively.
K2457 separately composes the new phase-averaged gap with the same theorem.
These are hypothetical design inputs, not measured apparatus, calibrated secrecy or realized use counts.
Rarer use routing changes both the cost budget and the required resource
number; an expected number of launches is not a stopping-safe count.

## 4. Evidence and limitations

The probe enumerates an exact rational adaptive history tree, including
actual crossing events, and uses Arb256 for conditional multiplier and
prospective consumer bounds. It also checks support endpoints, genuinely
incorrect omitted-budget and omitted-residual controls, persistent costs,
and data-dependent branch histories. Finite controls do not prove the
universal statement; the written conditional Cauchy-Schwarz argument does.
Independent internal specialist review is not external-expert or proof-assistant
certification. Required calibrated risk bounds remain an external input.

[Probe](../../tests/channel-swings/k2456_predictable_leakage_budget_probe.py)
and [report](../../lab/process/k2456-predictable-leakage-budget.json).
