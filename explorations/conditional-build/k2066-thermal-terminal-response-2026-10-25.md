---
title: "K2066: Incoming-aware thermal terminal response"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite/countable thermal certificate; no exact optimum or GU physics verdict
scripts:
  - tests/channel-swings/k2066_thermal_terminal_response.py
  - tests/channel-swings/k2066_thermal_terminal_response_probe.py
---

# K2066: Incoming-aware thermal terminal response

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: exact incoming-aware terminal envelope and improved global thermal lower certificate
carrier: four-state thermal channel and nondegenerate positive-spacing catalyst supports LAYER=toy CHIRALITY=N/A
pairing: classical diagonal marginal return ON=declared_thermal_population_model
real_structure: nonnegative real populations; rational certificates
grading: occupied energy and support gaps, not field parity
action_owner: repository-construction -- K1935 model and K2054 terminal loss
target: finite and countable energy-constrained return MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] For K2059's four-state thermal model, bath
weights(8,4,2,1)/15, spacing1/2<delta<=1 and mean-energy budget E=5/2,

    549971760412002337513926417/1976871225373814177206100780
        <= F_delta(5/2) <= 11561805/41518097,
    0.27820312894078675 <= F_delta(5/2) <= 0.27847627505663375.

The remaining width is approximately0.000273146116, about25.10 percent smaller
than K2059's bracket. The upper witness is unchanged, hash-pinned reuse. Five low
assignments are strengthened; all671 alternatives are checked against the reported
line. The new bottleneck is164, whose already valid K2059 line is now the global
minimum. This is a better certificate, not an exact optimum, dimension theorem,
novelty claim or GU verdict.

## 1. What was missing from the old terminal price

[K2054](k2054-quantitative-terminal-erasure-2026-10-25.md) gives the exact deletion
response, including incoming flow. [K2059](k2059-energy-aware-thermal-tail-2026-10-25.md)
uses its sharp incoming-independent coefficient in a Bellman bound. That coefficient
cannot be uniformly increased. The new calculation retains the incoming flow in
the first erased terminal's priced response, while reusing the established bound
at every deeper terminal. This is a mathematical refinement of the existing model,
not a source-state or observation construction. Source register, physics ledger,
canon, and all prior status values remain unchanged.

At bath ratio0<theta<1, gap d in{1,2,3}, write

    Z=1+theta+theta^2+theta^3,
    L=(1+...+theta^(3-d))/Z, H=theta^d L,
    k=H/(1+L), c=(1+H-L)(1+L)/(2(1+H+L)).

Let p>=0 be the retained parent population, c0>=0 its incoming flow, u>=0 a new
terminal population, and A=(p-c0)_+. For an actual path with incoming gap r and
previous population b, c0=(H_r b-L_r p)_+. It is not an independently adjustable
optimization input. With y_+=max(0,y), the unnormalized return increment is

    2Delta=(p-c0-(Lu-Hp)_+)_+
               +(u-(Hp-Lu)_+)_+ -(p-c0)_+.                 (1)

Keep the fixed cell support and incoming gap on its zero-population faces.
Recompressing individual vertices would change the function being interpolated.

## 2. Complete response and a sharp joint correction

Directly expanding(1), with all breakpoint orders valid, gives

    Delta=0                              for 0<=u<=kp;
    Delta=((1+L)u-Hp)/2                   for kp<=u<=Hp/L;
    Delta=((1-L)u+Hp)/2                   for Hp/L<=u<=(A+Hp)/L;
    Delta=(u-A)/2                        for u>=(A+Hp)/L.  (2)

Zero-length intervals, p=0 and A=0 are included. The function is continuous and
homogeneous, but is not globally convex: the middle slope drops. Put

    x=(u-kp)_+, alpha=L(1+L)/(1+H+L), beta=H/(1+H+L).

Then the incoming-aware inequality is

    Delta >= c x + min(alpha x, beta(p-A)).                 (3)

Below Hp/L the surplus Delta-cx is exactly alpha x. Above it, the surplus has
negative slope (1-L)/2-c until u=(A+Hp)/L and positive slope1/2-c afterwards.
Its minimum there is beta(p-A). This proves(3). The alpha and beta coefficients
are separately attained on the first rising interval and at the latter corner,
respectively, with the other branch of the minimum chosen larger. When A=p the
old sharp equality survives, so(3) is not permission to raise c universally.
For theta=1/2,d=2: k=1/9,c=9/50,alpha=18/25,beta=1/10.

## 3. Exact priced envelope, including its sharp validity boundary

For0<=g<=1/2 the entire optimization in u is explicit:

    P_g(p,A)=sup_(u>=0)(g u-Delta)
      =max(g k p,
           (g-1/2)H p/L + [1/2+(g-1/2)/L] A).             (4)

The candidates are u=kp and u=(A+Hp)/L. Every other segment has constant slope;
the final slope g-1/2 is nonpositive. At g=1/2 a constant final segment is allowed.
For g>1/2 the supremum is infinite, so the cap is necessary. For g=c, equation(4)
reduces to gkp for every A<=p. If A=0 it reduces to gkp for every g<=1/2: saturated
incoming flow permits a higher first-terminal reward without raising deeper caps.

The exact no-extra-boundary-cost condition is

    (2g-1+L)A <= H[1-2g/(1+L)]p, with g<=1/2.             (5)

This is more useful than a sampled improvement at one population. It specifies
when incoming flow absorbs the increase in the tail's energy price.

## 4. Whole-cell and countable transfer

Reuse K2059's legal gaps d+e>=4, its compulsory physical ladder/offset proof, and
the complete671-cell bank with20975 vertices. For a fixed retained support s ending
at z, allowed outgoing d satisfy z+d>=12 and the incoming-gap condition. Define

    G(n,d)=max(0,a-t*n+max_(e:d+e>=4) k_e G(n+e,e)),
    cutoff64, t>0, a<=65t; G=0 beyond64.                  (6)

Here t is an energy price, not theta. The first erased states have energies at
most z+3. Every deeper state has energy at least z+4, because the first two gaps
sum to at least4. Thus they are disjoint sets even when several first gaps are
allowed. Require only G<=1/2 on first states, but retain G(n,d)<=c_d on every
reachable deeper state. Let

    B_s(p,b)=max(0, max_allowed_d P_(G(z+d,d))(p,A)).        (7)

If there is no allowed outgoing edge, B_s=0 and the low-cell inequality MUST
still be checked. Cell152 is an explicit regression for this case.

Delete an actual finite tail from the far end. The incoming flow at the first
edge depends only on the retained prefix. Deeper deletion losses are paid by
G_j(p_j-k_j p_(j-1))_+, using(6) exactly as in K2059. Telescoping gives

    sum_tail(a-t*n_j)p_j - Delta_total
       <= G_first u-Delta_first <= B_s(p,b).              (8)

No signed reward is multiplied by a population inequality. The first edge's exact
response is used once, and its deeper costs remain paid separately.

For every vertex of the low cell check R>=a-t*energy+B_s. On each fixed orientation
cell c0 is affine; A=max(0,p-c0) is convex. If g>=(1-L)/2, the coefficient of A in
the second branch of(4) is nonnegative, so P_g is convex. If g<(1-L)/2 that branch
is nonpositive and dominated by gkp, so P_g is affine. Maxima preserve convexity.
The bank includes the return-deficit subcell vertices where R is affine. Therefore
R-a+t*energy-B_s is concave on each such subcell, and nonnegativity at its vertices
proves it throughout. No new vertex enumeration is required.

High components retain K2059's SAME a,t and safe offset
ell=max(1,s_penultimate+1), or1 for a singleton. Recompute G_high with a-t*ell,
retain every cost cap, every wholly-erased-root bound1/2, and check all high-bank
vertices with their old boundary coefficient max k_d G_high. Combining these
inequalities gives the homogeneous statement R>=a*mass-t*energy. This covers
multiple components; improving only the low contact would not suffice.

For countable finite-mean populations apply the finite inequalities without
renormalizing. Positive spacing gives a finite prefix below cutoff11. Mass, energy
and return converge by the inherited l1-continuity argument, yielding the same
bound. There is no highest infinite terminal or interchange of an uncontrolled
optimization and limit. The physical upper construction and completeness of the
bank remain explicit hash-pinned prerequisites.

## 5. Certified result and active successor

The former bottleneck188 has support[1,3,5,7,9,11], contact57 proportional to
[4374,6561,729,81,9,1]. Its terminal incoming flow equals its last population,
so A=0. Relaxing the first cap therefore has real value. The new exact assignments
for152,187,188,212,235 are recorded in the certificate; every one is checked
against all high vertices and actual Bellman maxima. The global minimum becomes
the unchanged line of164:

    L(E)=299844642382569393201125217/988435612686907088603050390
         -(49717524353136448888324017/4942178063434535443015251950) E.

Every one of the671 assignments dominates this line on the certified interval

    91135/37292 <= E <= 1902504111222032340789/758668264726977861095.

The first-terminal scout for164 returns the same bound, with active deeper cap
(14,2). Thus the new response genuinely improves the whole bound but does not
solve the remaining coupled-tail problem. A promising next construction carries
exact incoming response through two erased vertices, retaining the second incoming
flow, or supplies a better physically feasible population. Another uniform c
increase is ruled out by its retained sharp fixture. A failed search is not a
proof that every possible certificate is exhausted.

## 6. Reproduction, repaired failures and review

Run the producer with `--write` only to regenerate its declared JSON certificate;
without that flag it reproduces and compares. It searches an explicit price box
0<=t<=1 with rational lower-envelope optimization, adds actual Bellman-policy cuts,
and accepts only a fully verified candidate. The price box is a search choice,
not a physical assumption or claim of optimality. The iteration bound is an
algorithmic failure diagnostic, never a certificate on failure.

The first frozen-policy candidate failed a deeper cap. Recomputing actual policies
and adding cuts repaired it. A no-attachment cell then exposed an omitted zero-
boundary low inequality; it was restored and the false candidate discarded. The
separate checker tests that case even when the allowed-edge list is empty. No
unverified candidate contributes to the reported bound.

The final producer certifies five replacement assignments. The separately
implemented probe passes1692 exact raw-response controls,105150 low/high vertex
inequalities and all671 line/interval comparisons. Five mathematical faults are
discriminated: a lost response half-factor, wrong incoming envelope, inflated
no-attachment intercept, false global lower value and over-cap reward. These are
finite exact controls; the universal response, convexity, tail and countable
statements rely on the written proof above. The earlier bank's626412-basis
completeness and physical upper construction are reused, not rerun or counted as
new verification. Independent internal proof review checked transfer and scope;
no external, proof-assistant or novelty certification is claimed.
