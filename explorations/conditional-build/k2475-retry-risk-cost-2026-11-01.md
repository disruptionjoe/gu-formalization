---
title: "K2475 Sharp repeated-verifier error, completion and cost"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "sharp abstract retry interface only; quantum realization and measured conditional calibration remain open"
---

# K2475 Sharp repeated-verifier error, completion and cost

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
result: K2475
carrier: classical terminal attempts supplied by separately justified complete quantum instruments LAYER=toy CHIRALITY=N/A
pairing: conditional probability on every reached history ON=declared_carrier
real_structure: real coefficients and probabilities in the stated conditional models
grading: homogeneous degrees or classical reached-attempt histories as stated
action_owner: repository-construction -- supplied conditional mathematical models
target: Repeated capped verification interface MAP-TYPE=evaluation
```

## Result and explicit interface

Budget abort alone does not authorize retrying at unchanged risk. If each
reached attempt has conditional wrong-output probability<=alpha and output
probability>=p>0, stopping at the first output gives conditional-on-output
error<=min(1,alpha/p), including finite attempt caps. The exact worst-case
wrong-output probability by m attempts is

    V_m=alpha/qstar * [1-(1-qstar)^m],
    qstar=max(alpha,p), 0<=alpha<=1, 0<p<=1.             (1)

Expected attempts<=1/p and expected cost<=S+K/p if K bounds the ENTIRE cost
of each attempt and S is a one-time setup. These are sharp abstract classical
interface bounds. Arbitrary quantum memory or reuse of a state need not meet
the premises. K2472 supplies budget capping, not the required completion lower
bound or conditional calibration. SC-META-53 remains UNCERTAIN; source,
ledger0.263 and physical GU credit are unchanged.

## 1. Reached-history theorem without independence

Let R_i mean attempt i is reached. Before it, freeze predictable bounds
alpha_i,p_i,K_i. Conditional on every reached history, require

    f_i=P(wrong output | history)<=alpha_i,
    q_i=P(any output | history)>=p_i,
    cost_i<=K_i.

Wrong output, correct output and no output are disjoint exhaustive terminal
outcomes. Every attempt terminates; stop at first output. The wrong event must
have the same intended meaning across attempts. Nonnegative sums and
conditional expectation give

    P(wrong output)<=E sum_i 1_Ri alpha_i,
    E cost<=S+E sum_i 1_Ri K_i.                          (2)

No independence or optional-stopping integrability assumption is needed for
these inequalities; an infinite right side is simply uninformative.
If alpha_i<=rho p_i for all reached histories, f_i<=rho q_i. Summing the
disjoint terminal events gives

    P(wrong output by m)<=rho P(output by m).           (3)

Thus conditioning on output costs at most rho whenever its probability is
positive. An aggregate error bound alone would instead need a total output
lower bound; the local ratio premise is stronger.

## 2. Sharp constant bounds and actual costs

For constant alpha,p,K, define T as the uncapped first-output index,
continuing after every no-output attempt. Then P(T>m)<=(1-p)^m and E T<=1/p.
The capped attempt count is N_m=min(T,m), for integer m>=1. An unlimited sequence
completes almost surely; finite cap m completes with probability at least
1-(1-p)^m and costs at most S+mK. Equation(3) gives rho=min(1,alpha/p).
For 0<=alpha<=p, independent attempts with probabilities
(wrong,correct,none)=(alpha,p-alpha,1-p) give equality for the error/output ratio, finite completion and expected
attempt count; exact charges give equality in expected cost. The pathwise
cap S+mK is attained only when m attempts can actually be reached. For alpha>=p, (alpha,0,1-alpha) attains eventual wrong-output1;
it need not also attain the worst completion delay.

The exact finite-horizon risk follows by backward induction with V_0=0:

    V_m=max_(p<=q<=1) [min(alpha,q)+(1-q)V_(m-1)].

For q<=alpha the expression increases with q; for q>=alpha it decreases
(or is constant at V_(m-1)=0). Hence qstar=max(alpha,p) is an optimizer,
proving (1). A fixed three-outcome law attains it, so adaptive correlations
cannot exceed it under the conditional premises. This sharpness is only for
the abstract class, not an assertion that original Q/T effects realize every
three-outcome vector.

To target conditional error<=eta, the sufficient design inequality is
alpha<=eta p. To target noncompletion<=delta, choose integer m with
(1-p)^m<=delta (p1 permits m1); fund S+mK. Include reset, preparation,
calibration acquisition and abort in K, or price separately if genuinely
one-time. Repeating the same bounded-spending protocol does not yield a fixed
pathwise total cost without an attempt cap.

## 3. Composition with budget abort and shared calibration

K2472 gives capped completion>=s-delta only if uncapped completion>=s and
loss<=delta hold on every reached history. For s>delta set p=s-delta and
retain the unchanged per-attempt unconditional error alpha. Fresh setting
laws, whole-instrument calibration, leakage and controller assumptions must
survive prior no-output selection. Upper pass caps alone supply no positive p.

If these premises hold only on a single common good-calibration event G with
P(G^c)<=zeta with 0<=zeta<1, require them under the law conditioned on G, for every reached
history. At finite horizon m, let c_m=1-(1-p)^m and rho=min(1,alpha/p).
Then

    P(wrong output) <= zeta+(1-zeta)V_m,
    P(output) >= (1-zeta)c_m,
    P(wrong | output) <= [zeta+rho(1-zeta)c_m]
                         /[zeta+(1-zeta)c_m].           (4)

For the ratio proof, write good output mass g>=(1-zeta)c_m and bad output
mass b<=zeta. Error<=rho g+b, and (rho g+b)/(g+b) is maximized at the
smallest g and largest b. This bound is sufficient, not a joint-sharpness
claim for all three displays. It prevents treating a shared calibration
failure as a fresh independent event each attempt. A global cost cap S+mK
still applies if K is valid on bad histories too. Without that premise no
bad-event cost expectation is bounded.

## 4. Released conditional certificate consumer

For a target conditional-on-output error eta in(0,1), define

    rho_max=eta-(1-eta)zeta/[(1-zeta)c_m].

If rho_max>0, taking 0<alpha<=p rho_max makes (4) at most eta. This sufficient
positive-risk finite-count interface requires eta>zeta/[zeta+(1-zeta)c_m];
equality allows abstract alpha0 but not the displayed logarithmic count. As m grows the floor tends
to zeta. Failure of this sufficient design is not impossibility for a
particular device whose bad-calibration behavior is better known.

Suppose, additionally, the entire K2471 certificate applies on every reached
history under the good-calibration law, with an independently justified
expected original leakage budget K_B and its positive output allowance D>0.
Its sufficient per-attempt use count is then

    Nuse=ceil([log(1/alpha)+C K_B/alpha]/[log(2) D]),
    C=(1+log2)^2/[4(1-log2)].

This is a composition of conditional interfaces. The actual cost cap K must
fund that attempt, including preparation, resets, calibration and a valid
budget-abort loss; p must be justified for that same capped attempt. Choosing
p and K independently of the count does not establish a device design.
The probe supplies eta1/100,zeta1/1000,p7/10,m4,K_B1/1000000,D1/100 as a
mathematical parameter example. It computes rho_max, alpha and Nuse, checks
the exact conditional ratio and calibration floor, and retains count/cost
feasibility as a separate input. No emitted-resource cost is equated to the
use count.

## 5. Concrete selection counterexamples

Let U be uniform. Attempt1: wrong U<1/10, correct1/10<=U<9/10, no output
otherwise. Potential attempt2: wrong U>=9/10, correct otherwise. Each
standalone marginal error is1/10 and completion>=9/10. Retrying yields
error1/5>1/9, because the reached second history is entirely wrong. Marginal
calibration cannot replace reached-history calibration.

A shared latent event of probability p makes every potential attempt output,
and its complement makes every attempt return none. Marginal completion is
p each time, yet P(T>m)=1-p forever. Fresh routing by itself does not remove
this shared failure. Finally, ignoring per-attempt setup understates cost by
that charge times the expected number of attempts, not once.

Universal evidence is conditional expectation, local error/output domination,
backward induction and event composition. Exact rational finite/adaptive trees
and contrary latent-variable laws test the actual formulas. Internal review
is not external-expert, proof-assistant, novelty or measured-device evidence.

[Probe](../../tests/channel-swings/k2475_retry_risk_cost_probe.py) and
[report](../../lab/process/k2475-retry-risk-cost.json).
