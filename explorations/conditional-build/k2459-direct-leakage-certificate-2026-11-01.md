---
title: "K2459 Direct compensation removes the leakage smoothing residual"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional original actual-use risk bound with a justified predictable budget; no measured leakage or GU physical quotient"
---

# K2459 Direct compensation removes the leakage smoothing residual

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
result: K2459
carrier: actual classical history kernels and normalized use-branch states on supplied positive Hilbert programs LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and positive Hilbert trace ON=declared_carrier
real_structure: real binary probabilities and complex positive states
grading: actual test versus use, predictable versus observed, statistical versus systematic error
action_owner: repository-construction -- supplied conditional experiment
target: time-uniform original predictable actual-use risk and success-weighted output MAP-TYPE=evaluation
```

## Result and scope

Under exactly K2456's fixed-parameter, independently justified accumulated
leakage-budget premise, a direct compensated exponential gives actual-use
risk O(1/N_U), improving the earlier O(1/sqrt(N_U)) bound. It eliminates the
smoothing residual from the risk, with a larger constant on the leakage budget.
This is not a uniform numerical dominance claim for every finite budget.
It is a conditional probability result, not an inference of leakage from
passing tests, an experimental certificate or a native GU construction.
SC-META-53 remains UNCERTAIN; LT-SM8, ledger0.263 and canon unchanged.

The nonnegative-supermartingale framework is established; the complete
specialized proof follows. No novelty, proof-assistant or external-expert
certification is claimed. K2456 remains valid as a separate bound.

## 1. Direct one-step theorem

At each pre-round history, freeze the actual test failure probability a,
the trusted-effect failure probability b on the actual normalized use-branch
state, test probability pi in (0,1), smoothing eta in (0,1), and k>0.
All may depend predictably on previous classical history. Keep versions at
needed null histories fixed, as in K2456. Define

    d=(b-a)_+, q=a+(1-eta)d,
    v=(a-q)^2/[q(1-q)],

with v=0 when a=q at either endpoint. Harmful d>0 puts q strictly inside
(0,1), so v is always finite. Set

    r=1-exp(-k), A=pi*r,
    c=log(1+A/(1-pi)), J=A-(1-pi)c>0,
    C=(A+eta*J)^2/[4J(1-eta)^2].                         (1)

With U the use indicator, T the test indicator and X its binary failure,

    E_actual exp(U*c*b-T*k*X) <= 1+C*v.                  (2)

This does not replace b by an auxiliary risk. To prove it, expand the
exponential chord deficit for b in[0,1]:

    1+b(exp(c)-1)-exp(cb)
      =b(1-b) sum_(m>=2) c^m/m! sum_(j=0)^(m-2) b^j
      >=b(1-b)(exp(c)-1-c).

Hence the matching-branch conditional mean is at most1-J*b(1-b).
If a>=b, the actual mean is no larger and v=0. Otherwise q=b-eta*d,

    q(1-q)=b(1-b)+eta*d*(2b-1)-eta^2*d^2
          <=b(1-b)+eta*d,

so b(1-b)>=(1-eta)^2*d^2/v-eta*d. Substitution gives

    E_actual exp(U*c*b-T*k*X)
       <=1+(A+eta*J)d-J(1-eta)^2*d^2/v <=1+C*v,

by completing the square. This covers b=1,a<1, where the unsmoothed
exact-use reference can have infinite relative entropy.

## 2. Stopping and the original budget

The product of exp(U_t*c_t*b_t-T_t*k_t*X_t)/(1+C_t*v_t)
is an actual-law nonnegative supermartingale starting at one. Thus with
probability at least1-alpha, simultaneously at every finite prefix,

    sum U_t*c_t*b_t <= sum T_t*k_t*X_t
               + sum log(1+C_t*v_t)+log(1/alpha).        (3)

The event covers arbitrary stopping times by the usual increasing-horizon
argument. At k=infinity set r=1, c=-log(1-pi), and put the multiplier zero
on a test failure; it remains absorbing. The version of (3) without the
failure term applies only to prefixes with no failures. It cannot restart
by discarding a failure.

For fixed pi,eta,k define gamma=max(1,C/pi). For every v>=0,

    log(1+C*v) <= gamma*log(1+pi*v),                     (4)

by log monotonicity if C<=pi, or (1+x)^gamma>=1+gamma*x
otherwise. A justified bound B on K2456's original sum log(1+pi*v_t)
therefore gives, at N_U>0,

    mean_actual_used b <= min(1,
       [k*F+gamma*B+log(1/alpha)]/(c*N_U)).              (5)

A pathwise time-varying upper bound is permitted; a confidence-qualified
budget spends its own failure probability. The budget is not observable
from test counts alone. Fixed B and zero failures give risk O(1/N_U),
and a statistical trace/output contribution O(1/sqrt(N_U)). Fixed
calibration and completed-operation errors still impose their own floors.
Persistent harmful leakage has growing cost and cannot claim a fixed B.
This result and expected-KL K2453 use different hypotheses.

For pi=eta=1/2,k=infinity, J=(1-log2)/2,
C=(1/2+J/2)^2/J, gamma=2C. The probe encloses these constants and
uses a larger rational C=3 for an exactly rational adaptive crossing tree.
It checks a genuine positive crossing probability against Ville's bound;
it does not treat finite enumeration as the universal proof.

## 3. Necessary cost order and sharper optional envelope

The linear order in v is necessary near a supported endpoint. With b=1,
a=1-epsilon, 0<epsilon<1,

    v=(1-eta)^2*epsilon/[eta*(1-eta*epsilon)],
    actual mean =1+A*epsilon.

Any bound actual mean<=1+K*v+o(v) therefore needs
K>=A*eta/(1-eta)^2. Our C is conservative, not minimax. Omitting
compensation fails at a=0,b=1. Reusing K2456's denominator unchanged
also fails: pi=eta=1/2,k=infinity,a=1/2,b=1 gives mean5/4,
v=1/3, but1+pi*v=7/6. The larger coefficient in (4) is essential.

If an independent per-step upper bound v<=V is available, an exact robust
one-step envelope reduces to a scalar compact maximization. For q in[0,1],
put

    dmax(q)=min(q/(1-eta), (1-q)/eta,
                sqrt(V*q*(1-q))/(1-eta)).

The exact supremum Dstar(V) is the maximum over q of

    (1-pi)exp(c*(q+eta*dmax))
       +pi*(1-r*(q-(1-eta)*dmax)).                       (6)

The three constraints are precisely a>=0,b<=1,v<=V for harmful pairs;
the mean increases with d at fixed q. Harmless pairs give at most1,
already attained at endpoints. Thus Dstar(0)=1,
Dstar(V)<=min(1+C*V,1+A), with equality1+A for
V>=(1-eta)/eta, attained at a=0,b=1. No numerical global optimizer or
optimal C is claimed. This reduction is useful only if a tighter envelope
changes an actual design decision; a grid is not a certificate.

## 4. Original heralded consumer

Retain K2456's trusted complete verifier gap nu, actual-use calibration
average beta_bar, private controller with no current-resource test/E data,
same history-selected ideal controllers, completed-operation error kappa,
ideal heralding qherald>0, and positive actual mean success. The output bound is

    C_out*sqrt((mean_used b+beta_bar)/nu)+kappa/qherald.

For target tau>kappa/qherald set
D=nu*((tau-kappa/qherald)/C_out)^2-beta_bar>0. Under zero
failures a sufficient count is

    N_U >= ceil((gamma*B+log(1/alpha))/[-log(1-pi)*D]).    (7)

This is success-weighted mean output, not a posterior guarantee on the final
transcript, future device or joint coherent process. The probe composes (7)
with prior gap2/5, giving432,973 sufficient actual uses; K2460 uses its separately certified changed-order gap.
All numerical allowances are prospective, not measured apparatus evidence.
The sufficient positive-success condition sqrt(Q)/2+kappa<qherald,
Q=min(1,(mean_used b+beta_bar)/nu), is checked too.

Independent internal specialist review checks the written proof. Contrary
controls act on actual multipliers/fixtures, not prose assertions. The
probe records finite, interval and analytic evidence separately.

[Probe](../../tests/channel-swings/k2459_direct_leakage_certificate_probe.py) and [report](../../lab/process/k2459-direct-leakage-certificate.json).
