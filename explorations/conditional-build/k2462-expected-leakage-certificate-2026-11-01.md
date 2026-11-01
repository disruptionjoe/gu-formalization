---
title: "K2462 Expected leakage budgets support stopping-safe actual-use risk"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional all-prefix expected-budget theorem; no budget inferred from tests or measured GU realization"
---

# K2462 Expected leakage budgets support stopping-safe actual-use risk

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
result: K2462
carrier: actual classical history kernels and the unchanged normalized use states LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and positive-Hilbert trusted-effect pairing ON=declared_carrier
real_structure: real probabilities and exact real algebra; complex positive states only in the supplied quantum model
grading: original tensor slots or classical histories and test/use branches; no imported physical grading
action_owner: repository-construction -- supplied conditional mathematical models
target: Expected leakage budgets support stopping-safe actual-use risk MAP-TYPE=evaluation
```

## Result and exact premise

K2459 required a pathwise bound on accumulated leakage cost. Here a uniform
bound on its **expectation** suffices, with an explicit larger confidence
penalty. The risk remains the original predictable risk on actual used
systems. The result includes support endpoints where the exact-use
reference in K2453 has infinite directional relative entropy.

The guarantee is under the stated initial law. It is not automatically
conditional on an initial selector or a final passing transcript. No experiment,
observed leakage estimate or native GU state is supplied. SC-META-53 remains
UNCERTAIN; LT-SM8, ledger0.263 and canon are unchanged.

## 1. Stopped compensated-process theorem

Reuse K2459's independently proved one-step bound on the same a,b,pi,eta,k:

    d=(b-a)_+, q=a+(1-eta)d, v=(a-q)^2/[q(1-q)],
    A=pi(1-exp(-k)), c=log(1+A/(1-pi)),
    J=A-(1-pi)c, C=(A+eta J)^2/[4J(1-eta)^2].

At coincident endpoints set v=0. All choices may be predictable, with
0<pi,eta<1 and k>0. Define

    Z_n=sum U_t c_t b_t - sum T_t k_t X_t,
    H_n=sum log(1+C_t v_t), M_n=exp(Z_n-H_n).

M is a nonnegative supermartingale with M_0=1. At k=infinity use its
limit: M becomes zero forever after a test failure; Z=-infinity there.
H stays nonnegative and increasing. Assume, under the actual initial law,

    sup_n E H_n <= K_H < infinity.                       (1)

A bound at just one fixed horizon licenses only that horizon. Monotone
convergence makes (1) equivalent to E H_infinity<=K_H.

For L>0 let E_N be a crossing Z_n>=L by N. Stop at the first crossing or N,
and let p=P(E_N)>0. Bounded optional stopping, then conditional Jensen, give

    1 >= E[M_sigma 1_E]
      >= p exp(L-E[H_sigma 1_E]/p)
      >= p exp(L-K_H/p).                                (2)

Here H_sigma<=H_N, so its expectation is bounded by (1). For p=0 there is
nothing to prove. The function p exp(L-K_H/p) is strictly increasing on
p>0. Taking L=log(1/epsilon)+K_H/epsilon yields p<=epsilon. Letting N
increase proves the same event bound over all finite prefixes, hence at
arbitrary stopping times. The proof does not condition the final claim on
passing or on the realized expensive mode.

For fixed pi,eta,k, K2459 proves H_n<=gamma B_n with
B_n=sum log(1+pi v_t), gamma=max(1,C/pi). Thus E B_infinity<=K licenses
K_H=gamma K. With probability at least1-epsilon, every N_U>0 satisfies

    mean_actual_used b <= min(1,
      [k F+log(1/epsilon)+gamma K/epsilon]/(c N_U)).       (3)

At infinite k this formula applies to zero-failure prefixes only. Fixed
expected K still gives O(1/N_U) risk and O(1/sqrt(N_U)) statistical output
error; systematic calibration/operation floors remain. An externally
confidence-qualified bound on the applicable expected-cost quantity spends
its own failure probability; arbitrary conditioning on a calibration event
does not preserve (1). Persistent
leakage generally accumulates cost. Passing tests do not establish (1).

## 2. Unbounded pathwise cost, finite expectation: exact example

Set pi=eta=1/2,k=infinity and use conservative C=3, justified by K2459's
rigorous C<3. An initial independent selector chooses a bad mode with
probability1/1000. In the other mode set a=b=1 until first test failure,
then a=b=0. In bad mode draw N with P(N=n)=2^(-n-1), n>=0; set a=0,b=1
for N rounds, then a=b=0. Routing remains fresh and independent. The selector and sampled N are included
in the initial history; the stated kernels are therefore predictable. The
expectation guarantee remains unconditional over that initial history.

The endpoint cost per bad round is log4. E N=1, hence
E H_infinity=log4/1000, while H has no finite deterministic almost-sure
upper bound. At epsilon=1/10 the threshold lies strictly between3log2
and4log2. Good-mode crossing needs four initial uses, probability1/16.
Bad-mode uses U before N has generating function

    E z^U = sum 2^(-n-1)((1+z)/2)^n = 2/(3-z),

so P(U>=4)=1/81. The exact unconditional crossing probability is

    999/(1000*16)+1/(1000*81)=16187/259200 < 1/10.

On the positive-probability harmful histories b=1,a=0, directional
KL(Ber(a)||Ber(b)) is infinite. This finite expected-cost example therefore
is not an application of the finite-budget K2453 theorem. Conditioning
on the initial expensive N can destroy the asserted expectation cap.

## 3. Why expectation cannot be substituted into a pathwise theorem

Choose bad mode with probability1/10, run exactly40 rounds with a=0,b=1,
and otherwise use a=b=0. Then E H=4log4. Substituting that expectation
as a pathwise cap into a Ville threshold gives L_bad=log20+4log4.
Crossing occurs exactly when Binomial(40,1/2)>=13, with probability

    (1/10) sum_(u=13)^40 binom(40,u)/2^40
       =272597931681/2748779069440 > 1/20.

The proper expected threshold is log20+80log4 and cannot be reached in
40 uses. This is a failed actual guarantee, not just a metadata mutation.
Restarting after a failed test likewise violates the absorbing process.

The confidence penalty is sharp for the abstract compensated-process class:
let E have probability p, M_1=1_E/p, H_1=0, then at time2 choose predictable
H_2=(K_H/p)1_E and M_2=M_1. M is a nonnegative martingale. For K_H>0,
the threshold L=log(1/p)+K_H/p is first reached on E at time2 and E H_2=K_H.
Thus crossing probability equals p. This does not prove sharpness within
binary test/use implementations; the abstract construction need not realize
K2459's particular one-step factors.

## 4. Released original-output consumer

Retain K2459's complete trusted-effect gap nu, actual-use calibration average
beta_bar, privately initialized controller with no current-resource test/E
data, fixed history-selected ideal controller, operation error kappa,
ideal heralding qherald>0 and separately positive actual mean success.
For tau>kappa/qherald, put

    D=nu*((tau-kappa/qherald)/C_out)^2-beta_bar > 0.
    N_U >= ceil([log(1/epsilon)+gamma K/epsilon]/[-log(1-pi)*D]).

Using K=10^-6 as an independently justified EXPECTED original-budget cap,
pi=eta=1/2, epsilon=.05, beta_bar=10^-8, kappa=10^-6, qherald=1/4,
C_out=2 and tau=.01 gives432985 uses at gap2/5 and384833 at gap9/20.
Arb256 checks both rounded counts, preceding-integer failure, and the
separate positive-success condition. These are prospective conditional
budgets, not measurements. K2459's smaller pathwise-premise counts remain
valid under its stronger premise; neither theorem universally dominates
K2453 under its different directional-information hypothesis.

Universal evidence is the written stopping/Jensen proof. Exact probability
identities, contrary laws and interval prospective calculations are separate
finite evidence. Independent internal review is not external-expert,
proof-assistant or novelty certification.

## Released actual binary lower bound: expected penalty is necessary

The order K_H/epsilon is necessary in the ACTUAL test/use process, not just
in the abstract compensated-supermartingale class. Let u=1-pi,c=-log(u),
and use an initial rare selector of probability p>epsilon, included in the
initial filtration. Safe mode has a=b=0. Rare mode uses a=0,b=1 until the
m-th actual use, then switches to a=b=0. This rule is predictable, all tests
pass, and every rare path reaches the stopping time tau_m almost surely.
At its endpoint v_*=(1-eta)/eta and h_*=log(1+C v_*).
The waiting time is negative-binomial, with E tau_m=m/u. Consequently

    P(sup_n Z_n >= c m)=p,
    E H_infinity=p h_* m/u,
    c m = rho K_H/p, rho=c u/h_*.                       (8)

Thus a uniform epsilon-tail threshold cannot have a leading coefficient
below rho on K_H/epsilon as p decreases to epsilon and m increases. This
is a genuine scale lower bound, not a proof that the theorem's coefficient1
is sharp for binary processes. The initial selector does not grant a
conditional guarantee after one sees its outcome. There is no finite
pathwise cost cap: arbitrarily many tests may precede each actual use.

For pi=eta=1/2 and the valid conservative C=3, h_*=log4 and rho=1/4.
With epsilon=1/20,p=1/10,m=10, exactly one tenth of paths hit10log2,
while K_H=2log4. Hence the threshold K_H/(8epsilon)=10log2 fails the
one-twentieth tail requirement. The one-use waiting-time PGF is uz/(1-pi z);
its m-th power has mean m/u. The probe checks exact finite geometric
remainders, endpoint admissibility, expected cost and these ratios.
This resolves the possible removal of the inverse-confidence penalty;
improving its binary constant remains a separate optimization question.

[Probe](../../tests/channel-swings/k2462_expected_leakage_certificate_probe.py) and [report](../../lab/process/k2462-expected-leakage-certificate.json).
