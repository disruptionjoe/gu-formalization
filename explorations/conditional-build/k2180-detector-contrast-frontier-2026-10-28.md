---
title: "K2180 Extremal repair and geometric detector convergence"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2180_detector_contrast_frontier_probe.py
---

# K2180 Extremal repair and geometric detector convergence

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2180 geometric exact and threshold approximation with extremal convex repair
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

Extremal convex repair improves the previous O(sqrt(K)2^-K) approximation to
O(K4^-K), uniformly away from maximal contrast. It also gives a direct
threshold-energy approximation, local Lipschitz bounds and integrates the known algebraic
maximal-contrast endpoint. The rational epsilon consumer needs K12 instead of
K20 at tolerance1e-4 and K107 instead of K208 at1e-60. These are prospective
error budgets, not new computed optimal energies.

This is GU-independent mathematics of the same supplied positive scalar Fock
model and binary diagonal effects followed by outcome-conditioned real squeezes.
The cost is vacuum output FIELD energy; apparatus, clock, preparation, switching
and reset are excluded. SC-META-53 remains UNCERTAIN; source, ledger0.263,
LT-SM8/LT-GR6b and canon do not move. Occupation grading is not source chirality.
No arbitrary-channel, physical quotient, novelty or external acceptance claim.

[K2178](k2178-effective-detector-approximation-2026-10-28.md)'s older theorem
remains valid. This result removes its avoidable coordinate-repair loss.
[K2176](k2176-detector-certified-convergence-2026-10-27.md) remains the actual
released numerical energy enclosure. No global optimizer is implemented here.

## Definitions and uniform squeeze restriction

p_n=(3/4)4^-n; q_n=3n-1; x_n=p_n e_n; 0<=x<=p; y=p-x; d(x)=sum q_n x_n.
R(x)=sum(n+1/2)x_n; T(x)=sum(n+1)sqrt(x_n x_(n+1)); R(x)+R(y)=5/6.
E(x;s1,s0)=R(x)A(s1)+R(y)A(s0)-(40/3)[s1T(x)+s0T(y)]+35/18,
A(s)=41s^2/6+3/(2s^2).

The range of d is [-3/4,3/4]. The positive extremum r+ has r+_0=0 and r+_n=p_n for n>=1. The negative extremum r-=p-r+ is its complement. Every coefficient q_n is nonzero, so equality at either extreme uniquely determines its profile.

The squeeze interval S=[2/3,113/100] works for ALL cap-feasible profiles. Summing 2sqrt(ab)<=a+b with weights(n+1) gives T<=R. For R>0 the branch minimizer solves A'(s)=(40/3)T/R in[0,40/3], A''>0, A'(2/3)=-73/72<0, and A'(113/100)>40/3. Thus it belongs to S. When R=0 the branch vanishes and any representative squeeze in S may be chosen. This restricts a representative optimum; a vanished branch still permits arbitrary unused squeezes.

At fixed s in S^2, E is convex in x, because both coherences are concave. K2178's common bounds -31/10<=E<=185/18 apply to all capped profiles, so the common range width W=602/45. Convexity implies for any capped x,r and alpha in[0,1]:
 E((1-alpha)x+alpha r;s)<=E(x;s)+W alpha.
This is convexity BEFORE minimizing over squeeze pairs. No convexity of the minimized exact frontier is asserted.

## Exact-contrast geometric approximation

Let F(d)=min{E(x;s):d(x)=d, 0<=x<=p, s in S^2}, |d|<3/4. Fix eta=3/4-|d|>0 (or any smaller positive lower margin).
For K>=2 retain K2178's exact quantities:
 B_K=3(K+1)4^-(K+1),
 D_K=(K+11/6)4^-(K+1),
 H_K=(K+4/3)4^-K/2,
 tau_K=4D_K+(452/15)H_K.

Let P_K(d) be capped heads x0,...,xK with d-B_K<=h=sum_(0..K)q_n x_n<=d. Append the exact half tail v_n=p_n/2 for n>K. Let m_K(d) be the minimum of this full-tail energy over P_K(d) and S^2. This is the SAME finite relaxation as K2178 at d=1/2.

Claim:
 m_K(d)-tau_K <= F(d) <= m_K(d)+rho_K(eta),
 rho_K(eta)=W B_K/(2eta).

Lower side: a true feasible profile has tail contrast in[0,B_K], so its head belongs to P_K(d). Replacement by a half tail changes energy by at most tau_K, exactly as K2178.

Upper side: every v in P_K(d) has c=d(v) in[d-B_K/2,d+B_K/2]. If c=d do nothing. If c<d set r=r+, alpha=(d-c)/(3/4-c). If c>d set r=r-, alpha=(c-d)/(c+3/4). These denominators are positive; d is between c and the chosen endpoint, so alpha in[0,1]. Denominators are at least eta; hence alpha<=B_K/(2eta). The repaired w=(1-alpha)v+alpha r is capped by convexity of the box and d(w)=d exactly. Its eventual tail is constant (1+alpha)/2 in the upward case and (1-alpha)/2 in the downward case. The upper bound follows from fixed-squeeze convexity and the width W.

No coordinate correction, cap margin, optimizer tail, tangent-gradient bound or square-root continuity loss is needed. The error is O(K4^-K), uniformly for d in a fixed closed subinterval of(-3/4,3/4). K2178's O(sqrt(K)2^-K) remains a valid older bound; this new repair improves it rather than correcting its theorem.

For d=1/2, eta=1/4 and rho_K=(1204/45)B_K.

## Threshold consumer

For 0<=d<3/4 define V(d)=min{E(x;s):d(x)>=d}. Outcome complement and squeeze swap show the same V for |d(x)|>=d. This is a threshold value, distinct from F(d).

Define capped relaxed heads by h>=d-B_K, append the half tail, and minimize full energy to obtain m_K^threshold(d). The true threshold optimizer's retained head lies in this set. Any relaxed full profile v has c=d(v)>=d-B_K/2. If c>=d it already meets the threshold. Otherwise use exactly the upward extremal repair above, with alpha=(d-c)/(3/4-c)<=B_K/[2(3/4-d)]. Therefore
 m_K^threshold(d)-tau_K <= V(d) <= m_K^threshold(d)+W B_K/[2(3/4-d)].

This directly approximates the threshold problem, without a contrast grid and without assuming threshold saturation F(d)=V(d). Both finite problems have rational data for rational d, and the same 3K+7-variable polynomial encoding of degree at most three as K2178 (the contrast inequalities change but the objective encoding does not).

V is nondecreasing by nesting of feasible sets. Further, for 0<=d<d'<3/4,
 0<=V(d')-V(d)<=W(d'-d)/(3/4-d).
Proof: take a minimizer at d. If its actual contrast c>=d', it is already feasible. Otherwise mix toward r+, with alpha=(d'-c)/(3/4-c). Since c>=d and the displayed ratio decreases with c, alpha<=(d'-d)/(3/4-d). Apply the same convex upper bound.

Similarly, |F(d')-F(d)|<=W|d'-d|/eta for d,d' in[-3/4+eta,3/4-eta], using the appropriate extremal repair in both directions. This proves local Lipschitz continuity, NOT exact-frontier monotonicity or convexity.

## Endpoint and continuity

The maximal-contrast energy was already certified by
[K2162, section5](k2162-feedback-detector-frontier-2026-10-27.md#5-exact-endpointsaturation-consumers)
and K2160. The formulas below rederive that known endpoint for this continuity
and approximation interface; they are not a new saturation-energy discovery.

At d=3/4 both F and V equal the energy of r+ after optimizing its two squeezes. Its moments are R1=11/24,R0=3/8,T1=7/24,T0=0. Thus s0=(9/41)^(1/4), A(s0)=sqrt(41), and s1 is the unique positive root
 451s1^4-280s1^3-99=0,
with uniqueness most cleanly proved from strictly increasing A'. The exact algebraic endpoint is
 Emax=(11/24)A(s1)+(3/8)sqrt(41)-(35/9)s1+35/18.
The negative endpoint follows by outcome swap. Above 3/4 the threshold is infeasible. Never substitute eta=0 into the repair bound; use the endpoint formula.

Continuity up to the endpoints is available without an effective endpoint modulus. For F(dj) with dj approaching 3/4, compactness extracts minimizing profiles/squeezes with limit profile r+ and continuous energy, giving liminf>=Emax. Mixing r+ with any fixed lower-contrast profile at the minimizing endpoint squeezes gives feasible exact contrasts approaching 3/4 and energies approaching Emax, giving limsup<=Emax. V continuity follows either from its nested compact minimizers or the same argument. This compactness continuity is not a quantitative endpoint approximation rate.

## Rational terminating epsilon consumer

For rational d strictly inside the contrast range and rational eps>0, increase K>=2 until tau_K+rho_K<=eps/2. All numbers in this cutoff test are rational; no enclosure-precision floor remains. Set J so 15/2^J<=eps/2. Exact real-algebraic decisions for m_K<a on its nonempty compact finite domain, with bisection starting[-4,11], yield [ell,u] width<=15/2^J. Then [ell-tau_K,u+rho_K] encloses F(d) or V(d), respectively, with width<=eps. No practical quantifier-elimination implementation or complexity bound is asserted; this is a terminating exact-arithmetic interface. Finite energy radicals still require certified treatment in any implemented optimizer.

At d=1/2:
 eps=1/10000: K12,J19; tau~1.279844178093805e-5, rho~1.554886500040691e-5, final width<0.00005695754.
 eps=1/1000000: K16,J25; final width<0.0000005914183.
 eps=10^-60: K107,J205; final width<4.401483e-61.
These are prospective error budgets conditional on solving the finite problem to the specified precision, NOT new numerical bounds for the actual detector energy. K2176 remains the actual released energy bracket.

Given a field-energy budget B, the threshold enclosure certifies d attainable when its upper bound is<=B and certifies d unattainable when its lower bound>B. The unresolved interval must be reported honestly. There is no promise of a terminating exact yes/no answer when V(d)=B, or an arbitrarily narrow exact inverse-budget contrast interval without handling possible plateaus. The monotone threshold Lipschitz statement does not exclude plateaus.

## Verification and limits

Run `tests/channel-swings/k2180_detector_contrast_frontier_probe.py`; `--write`
regenerates its dependency-hashed report. Exact controls exercise the actual
repair in both directions, cap-boundary heads, unchanged high-contrast threshold
profiles, all occupation tails, endpoint polynomial and rational error budgets.
Faults change repair direction, tail weight, moment/sign data, relaxed constraints,
error constants and endpoint coherence. Each is rejected only after a green
baseline. Universal compactness/convexity arguments are separately reconstructed
in independent internal review; finite controls do not certify them by sampling.

The optimized exact frontier is NOT proved convex or monotone. Threshold
monotonicity follows from set inclusion, not exact-contrast saturation. Its
possible plateaus and equality cases still constrain inverse-budget decisions.
No effective endpoint-uniform rate as eta approaches zero, practical finite
solver, full-energy optimizer uniqueness, or total apparatus work is supplied.

The strongest contrary route is a stable autonomous physical-smear controller
with explicit preparation/reset; its resource model is not contained in this
field-output calculation. For the present instrument the next numerical gate
is an actual certified finite optimizer or matching primal/dual scheme, with
coverage and conditioning proved. More cutoff calculations alone do not supply
that optimizer.

Geometric-mean concavity and convex mixing are standard; see
[Boyd and Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf).
The model-specific caps, contrast, tail constants and repairs are proved above.
No proof-assistant or external-expert certification is claimed.
