---
title: "K2471 Exact optimal uniform-confidence stopping coefficient"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional sharp expected-budget coefficient; no inferred leakage or physical experiment"
---

# K2471 Exact optimal uniform-confidence stopping coefficient

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
result: K2471
carrier: original predictable binary test/use laws and success-weighted conditional output model LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and supplied positive-Hilbert output pairing ON=declared_carrier
real_structure: real probabilities and real nonnegative adapted processes
grading: classical histories and test/use branches
action_owner: repository-construction -- supplied conditional mathematical models
target: Exact optimal uniform-confidence stopping coefficient MAP-TYPE=evaluation
```

## Result: the variational gap closes

In K2468's original half-test/half-use absorbing-failure experiment, the
optimal expected-original-budget coefficient, uniformly over confidence levels,
is exactly

    c=log 2, C=(1+c)^2/[4(1-c)]=2.335604558... .

The supremum is not attained at any finite pair 0<=a<b<=1. It is approached
as b decreases to zero with a/b=(3c-1)/(3-c). This settles the scalar
optimization left open in K2468; its entropy argument and actual-law sharpness
reduction are reused, not recounted as new proofs. No fixed-small-confidence
optimality, inferred leakage budget, apparatus or native GU conclusion follows.
SC-META-53 remains UNCERTAIN; ledger0.263 and source polarities are unchanged.

## 1. A logarithm bound that retains accumulated slack

For 0<=a<=1, define k=1-c and

    L(a)=c*a+3*k*a*(1-a)/(3+2*a).

Then log(1+a)>=L(a), with equality at 0 and 1. To prove this, set
H=log(1+a)-L. Direct differentiation gives

    H'(a)=a*Q(a)/[(1+a)(3+2*a)^2],
    Q(a)=(21-30*c)+(28-40*c)*a+(6-10*c)*a^2.

The exact bounds 56/81<c<25/36 give Q(0)>1/6, Q(1)<-25/81,
and leading coefficient<-74/81. Thus Q has exactly one positive root,
in (0,1): its two roots have opposite signs. H first increases, then
decreases, and H(0)=H(1)=0. This proves the inequality throughout the
closed interval. It avoids K2468's refuted derivative shortcut along a=r*b.

## 2. Positive-square proof on the whole triangle

For d=b-a>0, a>=0, a+d<=1, put

    den=(2*a+d)*(2-2*a-d)>0, v=d^2/den,
    w=log(1+v/2), N=c*b-log(1+a),
    t=2/3, h=3*c-1, z=1-c/3,
    Nbar=c*d-k*a*(1-a)/(1+t*a).

Section1 gives N<=Nbar. Since log(1+x)>=x/(1+x) for x>=0,
w>=v/(2+v). The following exact polynomial identity supplies the missing
uniform estimate:

    2*k*(1+t*a)*den*[2*C*v-Nbar*(2+v)]
      =[4*k*a*(1-a)-(h+2*z*a)*d]^2
       +a*d^2*(A+B*a)+2*k*c*(1+t*a)*d^3,
    A=(8/3)*(1+c-3*c^2),
    B=(-18+84*c-82*c^2)/9.

A and B decrease on c in[56/81,25/36], and evaluating the right endpoint
gives A>=107/162 and B>=511/5832. Every right-hand summand is nonnegative;
the cubic is strictly positive for d>0. Therefore

    N < 2*C*v/(2+v) <= 2*C*w.

Taking positive parts gives psi=[N]_+/2<C*w for every a<b. For a>=b,
psi=0 by concavity of log, including endpoint degeneracies. Consequently
K2468's exact variational supremum is at most C. Its existing actual binary
first-use-or-failure law with a=r*b and b→0 attains C as a limit at the stated
r. Hence the supremum is exactly C and no finite pair attains it.

## 3. Sharp operational inequality and released consumer

Keep the original predictable laws, fresh routing, absorbing test failure,
Z=log(2)*sum(use*b), B=sum log(1+v/2), and actual-law expectation. For
E B_infinity<=K, the all-prefix crossing threshold is now

    L=log(1/epsilon)+C*K/epsilon.

Crossing before failure has probability at most epsilon. No smaller constant
works uniformly over all experiments and all epsilon in(0,1). The sharpness
sequence uses epsilon just below 1/(1+a), hence approaches1; it does not
prove optimality for an independently fixed small epsilon. K2468's sharper
entropy budget J remains separate and can still outperform a B-only bound.
Pathwise budgets and other routing probabilities retain their own theorems.

For the inherited positive-success output allowance
 e=(tau-kappa/qherald)/Cout>0 and D=nu*e^2-beta>0, a sufficient count is

    Nuse=ceil([log(1/epsilon)+C*K/epsilon]/[log(2)*D]).

The probe computes this for both inherited verifier gaps2/5 and9/20,
compares with the previous5/2 bound, and checks the positive actual-success
premise at the same hypothetical output parameters. These are conditional
prospective counts; neither leakage nor complete-effect calibration is learned
from all-pass data. Universal evidence is the derivative sign argument,
polynomial identity, entropy theorem and actual-law limiting construction.
Finite symbolic identities and Arb256 numerical consumers verify their
coefficients; they are not independent theorem counts or proof-assistant,
external-expert, novelty or experimental certification.

[Probe](../../tests/channel-swings/k2471_sharp_stopping_coefficient_probe.py) and
[report](../../lab/process/k2471-sharp-stopping-coefficient.json).
