---
title: "K2453 Stopping-safe use-risk certification from a total information budget"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional predictable use-risk certificate under an expected total directional divergence budget; no observed secrecy or physical reference experiment"
---

# K2453 Stopping-safe use-risk certification from a total information budget

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
result: K2453
carrier: classical experiment histories with supplied predictable test/use quantum-state risks LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, binary relative entropy and real probabilities ON=declared_carrier
real_structure: normalized complex positive states and real conditional probability kernels
grading: actual versus auxiliary law, classical history, test/use branches and stopping times
action_owner: repository-construction -- supplied conditional mathematical model
target: same predictable actual-use risk and original heralded consumer MAP-TYPE=evaluation
```

## Result and scope

A finite expected *total* directional discrepancy between the actual test
failure probabilities and the actual use-branch hypothetical failure
probabilities suffices to transfer K2448's stopping-safe certificate. The cost
inflates the nominal confidence threshold; it need not impose K2450's fixed
worst-history leakage floor when the total cost remains bounded. Persistent
leakage can instead make the total cost grow and destroy that advantage.

The construction preserves K2450's predictable use-branch state. It does not
replace that state by a source marginal or by a hidden classical quantum
state. Its reference measure is a mathematical law of classical histories,
not a proposed physical hidden-route experiment. The divergence budget and
use risks must be independently justified; observed test counts do not
establish them. No measured performance, GU physical quotient, novelty or
global sample optimality is asserted. SC-META-53 remains UNCERTAIN; source,
ledger0.263 and canon are unchanged.

This composes the established nonnegative-supermartingale framework of
[Howard et al.](https://arxiv.org/abs/1808.03204) with elementary relative-entropy
change of measure. Probability comparison by relative entropy is established
information-theoretic machinery; see, for context,
[Atar and Merhav](https://arxiv.org/abs/1412.6769). Complete arguments for the
particular construction and inverse bound follow below.

## 1. The common scientific object and auxiliary law

Let P be the actual experiment law. Its classical pre-round history H_t
contains every classical input on which routing, testing, the controller,
stopping or calibration depends. Quantum memory is not replaced by classical
hidden variables. At each specified history h fix

    pi_t(h) in (0,1),  pT_t(h), pU_t(h) in [0,1].            (1)

Here pT is the actual test-branch failure probability, and pU is the failure
probability of the same trusted effect on the actual normalized use-branch
conditional state, exactly as in K2450. On test observe X in {0,1}; on use
there is no test observation. The order of the classical history transition
is: choose the route, produce X on test, then generate any additional
classical transcript with a specified conditional continuation kernel.
All these kernels, including versions at null histories needed below, are
fixed mathematical objects, not fitted after observing the run. Finite or
countable histories suffice; standard Borel histories work with specified
regular conditional kernels.

Construct Q on this same history space as follows. Keep the initial law,
route kernel pi, and every conditional continuation kernel. On test replace
Bernoulli(pT_t(h)) by Bernoulli(pU_t(h)); use transitions are unchanged. Extend
the kernels and risks consistently to Q-reachable P-null histories. Under Q
the *same frozen function* pU_t(h) is the binary test mean. Consequently

    R_n = sum_(t<=n) U_t pU_t(H_t),  F_n = sum T_t X_t       (2)

are the same measurable functions under both laws. Under P, R_n is the
desired predictable use-risk sum. Under Q it is an algebraic risk process;
no assertion that Q admits the actual device's quantum realization is needed.
This distinction also avoids asserting that the actual memory conditional
state would remain unchanged after changing physical test outcomes.

On each finite prefix the likelihood ratio factors only at test outcomes.
The chain rule therefore gives, with natural logarithms,

    D(P_n || Q_n)
      = E_P sum_(t<=n) pi_t(H_t) kl(pT_t(H_t) || pU_t(H_t)), (3)

where kl(a||b)=a log(a/b)+(1-a)log((1-a)/(1-b)), with its
continuous endpoint conventions. The expectation is under P. In particular,
pU=0 with pT>0 or pU=1 with pT<1 at a positive-P history makes the cost
infinite. A finite budget requires the corresponding support condition.

For a finite horizon N assume the right side of (3) at N is at most a
declared deterministic K. For an unbounded stopping-safe result assume that
bound for *every* finite prefix. Equivalently the expected infinite sum of
nonnegative costs is at most K. A stopped experiment can use its expected
total cost through its specified stopping time, with absorbing transitions
after stopping. A bound at one fixed horizon does not certify an unbounded
future. A realized path sum, an expected cost under Q, a per-round average,
or a post hoc estimate cannot silently replace the premise.

## 2. Ideal crossing event and sharp probability transfer

For fixed pi and predeclared k>0 put

    c = log(1+pi(1-exp(-k))/(1-pi)),
    M_n = exp(c R_n-k F_n).                                (4)

Under Q, conditional expectation of its multiplier is

    (1-pi) exp(c pU)+pi(1-pU+pU exp(-k)) <= 1,

by the chord of exp on [0,1]. Thus Q(max_(n<=N) M_n >=1/alpha)
is at most alpha for 0<alpha<1. This is precisely K2448's elementary argument
on the frozen common risk, not a claim that M is a P-supermartingale.
Predictable pi_t,k_t work with the corresponding weighted exponent.
For k=infinity use c_inf=-log(1-pi) and

    M_n^inf = exp(c_inf R_n) 1{F_n=0};                      (5)

the process is absorbing at zero after the first failure. A countable
predeclared grid with weights summing to at most one gives a Q-event union
with probability at most alpha when each candidate uses alpha times its
weight. Transfer that union once; do not give each candidate the full
actual failure allowance and select retrospectively.

For any common event E with Q(E)=q<=alpha and D(P||Q)<=K, let p=P(E).
Partitioning the likelihood ratio into E and its complement and applying
convexity of x log x proves

    kl(p||q) <= D(P||Q) <= K.                              (6)

If p<=alpha there is nothing to prove. Otherwise q<=alpha<p implies
kl(p||q)>=kl(p||alpha), since the derivative in q is
(q-p)/(q(1-q)). Also kl(p||alpha) is strictly increasing for p>alpha.
Therefore

    P(E) <= b(K,alpha),                                    (7)

where b(0,alpha)=alpha; if 0<K<log(1/alpha), b is the unique
root in (alpha,1) of kl(b||alpha)=K; and b=1 for
K>=log(1/alpha). Endpoint q=0 forces p=0 when K is finite.

Apply this separately to the increasing finite-prefix crossing events E_N.
Under the every-prefix budget, P(E_N)<=b(K,alpha) uniformly, and continuity
of probability yields the same bound for E=infinite union E_N. This proves
time-uniform validity without requiring an infinite-path density theorem or
an optional-stopping interchange for relative entropy. All stopping times
are covered by this common event.

The event-transfer bound itself is sharp: take a two-point space,
Q(E)=alpha and P(E)=b. Then D(P||Q)=kl(b||alpha). More
generally preserve the same conditional law within E and E-complement.
This sharpness is for the general probability-transfer problem, not a claim
that every b is attainable by every particular quantum routing protocol.

## 2a. Released strengthening: charge only harmful branch discrepancy

The exact-equality reference above is sufficient but can charge harmless excess
failures on the test branch. Define instead the auxiliary test mean

    qstar_t(h)=max(pT_t(h),pU_t(h)).

Keep the same initial, routing and continuation kernels and the same frozen
actual-use risk. Since qstar>=pU, the conditional multiplier under this new
reference is no larger than the multiplier used in (4). Thus the complete
crossing/transfer proof remains valid with the smaller cost

    Kplus >= E_P sum pi_t J(pT_t,pU_t),
    J(a,b)=0 if a>=b, and kl(a||b) if a<b.                 (7a)

This is the minimum pointwise divergence cost among auxiliary Bernoulli test
means q>=pU with the other kernels held fixed: kl(a||q) is minimized at q=a
when feasible, otherwise at q=b, by derivative (q-a)/(q(1-q)). It is not an
optimality claim over arbitrary reference experiments or certificates.
Only harmful under-testing is charged. For example pT>0,pU=0 now costs zero;
pT<1,pU=1 still has infinite cost. The latter reflects a support failure of
this reference argument, not impossibility of every alternative certificate.
All formulas below also hold after replacing K by a justified Kplus. An
all-prefix expected budget is still required; the improvement cannot infer
unobserved use risks or erase persistent harmful leakage for free.

## 3. Design inversion and original program consumer

For a desired actual failure allowance 0<epsilon<1, any nominal alpha<epsilon
satisfying kl(epsilon||alpha)>=K gives b(K,alpha)<=epsilon.
An explicit conservative choice, avoiding numerical inversion, is

    h(epsilon)=-epsilon log epsilon-(1-epsilon)log(1-epsilon),
    L=(K+h(epsilon))/epsilon,
    alpha=exp(-L).                                        (8)

Indeed kl(epsilon||alpha)=epsilon log(1/alpha)-h(epsilon)
-(1-epsilon)log(1-alpha)>=K. The inequality points toward
*smaller* alpha. Omitting binary entropy or replacing K by D(Q||P) is invalid.
At K=0, choosing alpha=epsilon is sharper than (8).

With probability at least 1-epsilon under P, all zero-failure prefixes with
N_U>0 satisfy

    R_n/N_U <= min(1,L/(c_inf N_U)).                        (9)

For finite k replace L by kF+L and c_inf by c. For a zero-failure candidate
with grid weight w, replace L by L+log(1/w); this is the nominal grid
allocation before one transfer of its event union.

K2447's pure extension and trusted gap nu, with effect allowance beta_t on
the actual use-branch state, imply

    mean_used infidelity <= Q_U=min(1,(B_U+beta_bar)/nu).

K2444's original r-slot qubit consumer then has normalized success-weighted
mean output distance at most min(1,C sqrt(Q_U)+kappa/q), with
q=4^(-r), C=2^(2r-1), and nonzero actual mean success;
(1/2)sqrt(Q_U)+kappa<q suffices. The ideal benchmark uses the same
history-selected controllers on the actual use indices. It is not an
independently regenerated ideal trajectory, a final-transcript conditional
state guarantee, or a mean of separately normalized outputs.
The controller has fresh private initialization independent of the current
resource conditional on the declared history. Prior classical test history
may select it; current-resource test outcomes and environment E data are not
disclosed to the use controller. On use, discard E and dephase the program
flag as in the original consumer.

For tolerance tau in (0,1), fixed finite total K, tau>kappa/q and

    D = nu*((tau-kappa/q)/C)^2-beta_bar > 0,

the sufficient actual-use count for (8)--(9) is

    N_U >= ceil((K+h(epsilon))/(epsilon*c_inf*D)).           (10)

The probe prices the original one/two-slot examples with pi=1/2,
epsilon=.05, K=.01 nats, nu=1/2, beta_bar=10^-7, kappa=10^-6,
tau=.01; it verifies the integer ceiling, predecessor failure and positive
success. These are prospective designs, not observations. Total emitted
resources include tests; ideal heralding still costs 4^r attempts on average.
The same probe also composes (10) with K2454's released fully local two-setting
verifier, using its actual original-law gaps
`(1-sqrt(27/127))/2` and `(1-sqrt(15/67))/2` for the respective one-slot
programs, under the same beta_bar, K, epsilon, kappa and tolerance. This
substitution changes the sampling allowance only: coherent F/E custody,
twelve conditional E projection settings, trusted Fourier/X measurements and
conditional calibration are still required. Two setting families do not mean
two elementary hardware settings or unchanged physical implementation cost.
If K itself grows with the planned horizon, solve (10) with that K(N) rather
than holding it fixed. No disappearance of persistent leakage is claimed.

Unconditional simultaneous validity does not become the same confidence
conditional on an acceptance event A. All that follows without more premises
is P(E|A)<=min(1,epsilon/P(A)); a proven P(A)>=s gives epsilon/s.
Taking A=E realizes conditional failure one. This probability-conditioning
limit is separate from the consumer's quantum success normalization.

## 4. Why the reference and information direction matter

If a *declared classical* source label Z has branch laws muT,muU and common
conditional quantum states rho_(h,z), a shared trusted binary effect is a
classical channel z -> Bernoulli(tr(E rho_(h,z))). Data processing gives

    kl(pT||pU) <= D(muT||muU).                             (11)

Hence E_P sum pi D(muT||muU)<=K is a sufficient stronger budget.
This is about an actual declared ensemble, not an ontic decomposition of
arbitrary quantum memory. The binary-risk theorem itself needs no such label.

A product-of-marginals source reference instead prices conditional mutual
information I(route:Z|H), but its hidden-route test mean is
pbar=pi*pT+(1-pi)*pU. That is a different scientific risk from pU.
For pi=1/2, test source always good and use source always bad, pT=0,
pU=1 and pbar=1/2. Mutual information is only log 2, whereas the required
directional test-to-use KL is infinite. This does not refute mutual-information
theorems for their own common event; it refutes using their budget for this
use-reference construction or silently exchanging pbar and pU.

Likewise KL between an observed transcript and an arbitrary ideal observed
transcript need not control a scientific event involving a latent state or
risk. Two experiments can have identical route/test records (all tests pass)
and different use states (all good versus all bad). Their record KL is zero.
There is no common risk event with both asserted interpretations unless an
appropriate extension and its KL bound are supplied. Our full classical
history construction instead fixes pU(h) under both measures; it does not
assert that transcript similarity alone establishes that function.

## 5. Rare histories, failures and evidence

As a concrete finite-total-cost contrast with a uniform leakage bound, let an
initial recorded flag B have probability eta=1/1024 under both laws. Only at
the first round on B=1 set pT=0,pU=1/2, with pi=1/2. All other rounds have
pT=pU=0. Then

    sup_history (pU-pT)=1/2,
    E_P sum pi kl(pT||pU) = eta*(log 2)/2.                 (12)

K2450 with the constant worst-history delta=1/2 cannot certify mean risk below
that floor. K2453 has finite K and (9) tends to zero as N_U grows. K2450 with
the *known varying* delta_t is also useful; this is not universal dominance
over all K2450 certificates. The example demonstrates that a small expected
total cost need not mean a small discrepancy at every history. More generally
a finite-horizon rare bad-history flag with pU=1-eta', pT=0 produces cost
eta*pi*N*log(1/eta'), finite for eta'>0. Exact pU=1 breaks finite support;
replacing it by a value strictly below one is substantive, not cosmetic.

The finite probe independently enumerates an adaptive nontrivial experiment
under P and Q, verifies common-event crossing masses, the full path-space
KL/chain-cost identity and the event data-processing inequality. Separate
controls check the sharp binary event, the entropy and KL-direction mistakes,
nonzero costs on rare histories, source-marginal risk mismatch, unchanged
record laws with changed use states, conditional-acceptance amplification and
interval-certified original-consumer counts. Finite checks support the
written universal arguments, not vice versa. Internal independent review is
not external-expert or proof-assistant certification.

[Exact probe](../../tests/channel-swings/k2453_use_reference_information_budget_probe.py),
[report](../../lab/process/k2453-use-reference-information-budget.json).
