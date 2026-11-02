---
title: "K2488 Markov reset errors: phase boundary, exact filtering and spacing repair"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematical result on the stated original or supplied carrier; no native GU or measured implementation claim"
---

# K2488 Markov reset errors: phase boundary, exact filtering and spacing repair

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
result: K2488
carrier: original 108-dimensional positive-Hilbert programs and explicitly supplied canonical instruments LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation as explicitly distinguished below ON=declared_carrier
real_structure: complex adjoint for quantum matrices; real probabilities for classical laws
grading: target and complement or absorbing classical trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Correlated classical flags, sharp full-carrier filtering and charged spacing repair MAP-TYPE=evaluation
```

## Result and Layer 0

Low marginal flag error alone does not guarantee useful filtering. On the same
original 108-dimensional positive-Hilbert Q/T verifier as K2484/K2486, a
stationary binary Markov flag process gives an exact phase boundary:

    uv < (1-u)^2 : uniform purification;
    uv = (1-u)^2 : a nonzero parity-dependent worst-case floor;
    uv > (1-u)^2 : worst-case conditional infidelity tends to one.

These statements assume 0<u<v<1, ideal retained-system controls and storage,
and classical flag errors independent of the initial system/reference. The
stationary marginal condition eta=u/(u+v)<1/2 alone does not distinguish these cases. Testing
every second flag repairs the latter two regimes in this declared model.
It costs extra transitions/storage and does not calibrate a real apparatus.

SC-META-53 remains UNCERTAIN. Ledger0.263 LT-SM8/LT-GR6b still owe the native
interacting positive quotient and domain. Source polarity, ledger, canon and
GU physical credit are unchanged. This is a conditional instrument result,
not a source-action result, novelty claim or measured implementation.
K2486's iid proof and shared-bit counterexample remain valid at their scope.

## 1. Law and exact full-carrier effect

Let hidden bits E_j say whether the ideal binary outcome is swapped. Start
in pi=(v,u)/(u+v); before conditioning on any measurement records, the bits
follow H=[[1-u,u],[v,1-v]], independently of the initial system/reference.
Given the whole bit sequence the recorded-accept Kraus map at test j is
R_j rho R_j for E_j=0, and (I-R_j)rho(I-R_j) for E_j=1. R_j alternates Q,T.
Stop at the first recorded rejection. This declares the complete memory
instrument, not just its single-use effect or its stationary marginal.

Use K2486's reducing sectors P,Z,Y,A,B,N of dimensions1,1,1,8,10,87 and angle
r=27/127 or15/67. P is the target, (Z,Y) the principal two-plane, A is Q-only,
B T-only, N common-null. Write a=1-u, b=1-v and

    K = [[a*r, u*(1-r)], [v*(1-r), b*r]],
    d(n)=diag(pi) K^(n-1) (1,1)^T,
    t_n=pi0*a^(n-1),
    A_n=pi0*u^floor(n/2)*v^floor((n-1)/2),
    B_n=pi1*v^floor(n/2)*u^floor((n-1)/2),
    N_n=pi1*b^(n-1).

For n>=1 the all-pass effect is exactly

    E_n=t_n P+d_0(n) Z+d_1(n) Y+A_n A+B_n B+N_n N.       (1)

Proof: conditional on the first ideal outcome the first measurement dephases
Z/Y. Every subsequent pair of rank-one eigenvectors has squared overlap r
when its bit is unchanged, 1-r otherwise. Multiplying that overlap by the
Markov transition gives K; weighting the first bit by pi gives (1). Common
sectors require respectively constant-zero, alternating01, alternating10,
and constant-one words. Cross-sector coherences do not affect the trace or
target population; the reducing projectors preserve that statement even with
an arbitrary retained reference. Target unnormalized mass is exactly t_n F.

Put w_n=max(d_0,d_1,A_n,B_n,N_n). For F>=F0>0 the sharp conditional
infidelity is

    e_n=(1-F0)w_n/[F0*t_n+(1-F0)w_n].                  (2)

A mixture of target and a unit vector in the maximizing bad sector attains it.
The exact finite expression, including all sectors, is the consumer; the
principal plane need not be the worst sector. n=0 has E_0=I. Independence of
successive flags is recovered when u=eta,v=1-eta.

## 2. Necessary and sufficient purification, including the critical floor

K has strictly positive entries. Its larger eigenvalue is

    lambda+=(r*(a+b)+sqrt(r^2*(a-b)^2+4uv*(1-r)^2))/2.

The principal-plane rate is lambda+, common-null rate b<a, and alternating
sector rate sqrt(uv). The positive eigenvector has positive overlap with
both entries of d, so its exponential rate is exact. When uv<a^2,

 det(a I-K)=(1-r)[(1-r)(a^2-uv)+r*a*(v-u)] > 0.

Also a exceeds both diagonal entries ar,br. Consequently lambda+<a.
Together with b<a and sqrt(uv)<a this proves w_n/t_n ->0. Conversely,
A_(2k+1)/t_(2k+1)=(uv/a^2)^k. This proves necessity and supercritical
failure for a fixed target/A mixture, not merely a cap-dependent worst state.

At uv=a^2, lambda+<a and b<a still hold. For odd n the A and B coefficients divided by t_n equal1 and u/v,
respectively; for even n both equal u/a. Hence the
worst conditional error has limits 1-F0 on odd caps and
(1-F0)u/[F0*a+(1-F0)u] on even caps. The hypothesis v>u implies u<a
at this boundary, but both limits are nonzero for F0<1.

Exact examples: u=2/5,v=9/10, eta=4/13 is critical; u=1/2,v=3/4,
eta=2/5 is supercritical. The corresponding iid model with the same eta
purifies, so replacing the actual joint process by its marginals is invalid.
Reducible u=v=0 is outside the theorem; K2486's frozen common-bit model
has its separate permanent floor. No conclusion about arbitrary coherent
quantum memory follows from a classical two-state model.

### Released marginal threshold within this Markov class

The failure examples cannot be moved to arbitrarily small eta. Fix
k=eta/(1-eta) in(0,1), so u=k*v with0<v<1. The ratio
uv/(1-u)^2=k*v^2/(1-k*v)^2 is strictly increasing in v and its supremum
is k/(1-k)^2. Therefore every admissible chain with that eta purifies iff

    eta <= eta_crit=(5-sqrt(5))/10, approximately0.276393.

At equality the supremum critical ratio1 occurs only at excluded v=1;
every individual interior chain still purifies. No common finite cap or rate
over the whole class is promised even below the threshold: v approaching0
at fixed eta approaches the frozen-bit process.
Above eta_crit, the exact critical choice v=1/(k+sqrt(k)) lies inside(0,1),
and increasing v gives supercritical chains; sufficiently small v purifies.
This is sharp only within this stationary two-state classical model, not a
marginal-only guarantee against arbitrary correlated flags (K2486's frozen
common-bit counterexample remains). Calibration uncertainty can use the
original robust inequality u_max*v_max<(1-u_max)^2, provided every admissible
parameter pair remains0<u<v<1; it guarantees purification, not a shared rate
without further margins. Fixed-cap guarantees still evaluate exact(1)-(2).

## 3. Positive persistence and a charged universal spacing repair

If u+v<=1 then every entry of H is <=a=1-u: b<a, v<=a, u<a.
Every extension of an accepted projection word contracts trace, and each
extension weight is <=a times its previous word weight. Summing its two
orthogonal outcomes gives E_(n+1)<=a E_n in Loewner order. Since
t_(n+1)=a t_n, normalized accepted bad mass decreases for every input.
Also uv<a^2, so it tends to zero. Under antipersistence u+v>1, normalized
A-sector survival rises from an even cap to the following odd cap by v/a>1;
monotonicity fails even for some subcritical processes.

Let t=1-u-v. Use one flag, allow m Markov transitions, then use the next
flag, with exact storage and no intervening measurements on the retained
system. The sampled chain is H^m, with

    u_m=eta*(1-t^m), v_m=(1-eta)*(1-t^m).

For every even m, 0<u_m<v_m<1 and u_m+v_m<=1. Thus m=2 already guarantees
purification for every chain in the stated irreducible eta<1/2 class. It is a
model-specific constructive repair; it does not assert that waiting performs
these transitions on actual hardware. Substitute u_m,v_m in (1)-(2) for the
sharp finite-cap guarantee. Larger m is not automatically cheaper or faster.
Per used flag target survival rate is 1-u_m, per underlying transition rate
is (1-u_m)^(1/m). Initial target factor is pi0, not one.

For positive persistence the asymptotic full bad rate is
beta=max(b,lambda+); sqrt(uv) is no larger than their maximum. Indeed if
b>=sqrt(uv) this is immediate; otherwise the characteristic polynomial of K
at x=sqrt(uv) satisfies
f_K(x)/r=(1-r)*x*(2x-a-b)+r*(x-a)*(x-b).
Here ab-uv=t>=0 implies x<=sqrt(ab)<a. If b<x, the first term is
nonpositive by AM-GM and the second strictly negative; thus lambda+>x. The b/theta crossover follows from
f_K(b)=(1-r)[b^2-uv-r*t]; b exceeds both diagonal entries only when
needed for that eigenvalue comparison. This last expression is a diagnostic;
use the explicit max, not an unchecked sign shortcut.

## 4. Costs, cap choice and renewal boundary

For rho, set q_j=Tr(E_j rho), q_0=1. With nonnegative test prices c_j,
initial preparation cost c_p, and price d per chain transition between used
flags, exact one-attempt expected cost through cap n is

    C_n=c_p+sum_(j=1)^n c_j q_(j-1)
               +m*d*sum_(j=1)^(n-1) q_j.             (3)

The second sum charges transitions only after accepted tests, when another
test is actually attempted; no charge after terminal rejection/success.
It is not a count of successful trials alone. A pure target with unit test
prices and no other costs has C_n=1+pi0*(1-a^(n-1))/u.

If attempts independently restart both the input and the same chain law,
expected total cost until an accepted output is C_n/q_n (renewal identity).
Without that restart premise, a first-attempt C/q is not a renewal theorem.
q_n decreases because all-pass events are nested; C_n increases for positive
prices, so C_n/q_n increases with cap. Earliest feasible cap minimizes this
cost among deterministic feasible caps for each fixed input, and hence also
their worst-input supremum. Fidelity feasibility itself need not be monotone
under antipersistence; search finite caps in order, not by binary search.

The exact worst renewal cost for F>=F0 occurs at a vertex of the convex
sector-weight polytope: the pure target or F0 P+(1-F0)V for each of Z,Y,A,B,N.
Both C and q are affine and q>0; a ratio at a mixture is a denominator-weighted
average of vertex ratios. This proves the finite maximization, and keeps the
pure-target vertex (which cannot be dropped without comparison).

## Evidence and remaining work

The probe uses exact rational transfer and independent sequential selective
measurement on the principal two-plane, original-angle/rank authentication,
sharp sector states, both transition regimes, cost sums, renewal mixtures and
spacing identities. Finite tests support the written universal word/spectral
argument; they are not a continuum proof or independent theorem count.
Read-only specialist and adversarial reviews apply before acceptance.

Next: test a calibrated complete-memory transition/reset/storage model against
the exact criterion and prices. General quantum memory, unknown input-chain
correlation, storage errors, and cross-attempt nonrenewal remain separate.
No hardware, physical GU, external-expert or proof-assistant certification.

[Probe](../../tests/channel-swings/k2488_markov_flag_filtering_probe.py) and
[report](../../lab/process/k2488-markov-flag-filtering.json).

Standard chain background: [University of Washington, Markov chains](https://faculty.washington.edu/yenchic/26A_stat516/Lec3_DTMC_p1.html). The instrument-specific phase proof above is derived here; standard chain theory alone does not supply it.
