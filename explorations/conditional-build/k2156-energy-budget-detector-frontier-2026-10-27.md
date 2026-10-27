---
title: "K2156 The fixed-mode energy-budget detector frontier"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical quotient or GU recovery
scripts:
  - tests/channel-swings/k2156_energy_budget_detector_frontier_probe.py
---

# K2156 The fixed-mode energy-budget detector frontier

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2156 attained convex detector frontier with certified finite approximation and sharp budget endpoints
carrier: fixed K2151 scalar Fock vacuum and photon-added one-particle signal, one canonical oscillator binary diagonal effects LAYER=toy CHIRALITY=N/A
pairing: positive global Hilbert form and vacuum probabilities ON=declared_carrier
real_structure: real effects in[0,1] and positive square-root Kraus amplitudes
grading: canonical oscillator occupation, distinct from GU or fermion grading
action_owner: repository-construction -- supplied massive scalar free Hamiltonian and fixed signal
target: optimize detection contrast over all diagonal nondemolition instruments at fixed output vacuum field energy MAP-TYPE=intertwiner
```

## Result and fixed scope

[K2153](k2153-diagonal-detector-energy-2026-10-27.md) minimizes field excitation
for fixed detector effects. Here the effects vary under an energy budget. The
result is an attained concave optimal-contrast curve, an explicit finite convex
program with a rigorous geometric tail bound, a certified nonzero-budget
example, a sharp small-budget asymptote and the exact budget where unconstrained
optimal discrimination is first reached. This solves the stated infinite
optimization through uniformly certified finite programs; no closed formula
for every intermediate budget is claimed.

Keep the same mode and named photon-added signal as
[K2151](k2151-optimal-local-mode-discrimination-2026-10-27.md): z in(0,1),
p_n=(1-z)z^n, q_0=0, q_n=n(1-z)^2 z^(n-1), E_sum>0. For binary click effects
e_n in[0,1], positive square-root Kraus attain the minimum over every countable
diagonal nondemolition realization. With normalized budget b=B/E_sum, define

    w_n=(n+1)z^(n+1), S=sum w_n=z/(1-z)^2, a=(1-z)/z,
    h(x,y)=2[1-sqrt(xy)-sqrt((1-x)(1-y))],
    C(e)=sum w_n h(e_n,e_(n+1)),
    Delta(e)=sum(q_n-p_n)e_n=a sum w_n(e_(n+1)-e_n),
    V(b)=max {Delta(e): C(e)<=b}.                         (1)

B is unconditional GLOBAL vacuum output field energy. It is not energy spent
preparing the signal, operating a controller, reading a record, or resetting
an apparatus. The carrier, signal and positive dynamics are supplied; there is
no GU physical-state or measurement derivation here.

## Existence and convexity

The geometric mean is jointly concave, so h and C are convex in the EFFECTS.
Since 0<=h<=2 and sum w_n<infinity, the energy series converges uniformly on
the compact product [0,1]^N. The absolutely summable objective also converges
uniformly. C and Delta are continuous in product topology; the feasible set
is compact and nonempty. Thus V is attained for every b>=0, is nondecreasing
and concave. At b=0, every adjacent effect is equal, so V(0)=0.
Convex mixing of effects followed by square-root realization is not generally
a classical mixture of the original instruments, as K2153 already demonstrates.

## Uniformly certified finite program

For integer M>=1, restrict e_n=e_M for n>=M. Put

    C_M=sum_(n=0)^(M-1) w_n h(e_n,e_(n+1)),
    Delta_M=sum_(n=0)^M c_n e_n,
    c_n=q_n-p_n (n<M), c_M=M(1-z)z^(M-1).

Let V_M be its maximum under C_M<=b. For M>=floor(z/(1-z)),

    V_M(b) <= V(b) <= V_M(b)+R_M,
    R_M=(M+1)(1-z)z^M.                                  (2)

Indeed, replace any infinite feasible effect's tail by its e_M. This deletes
nonnegative energy edges n>=M. Its contrast change is
sum_(n>M)(q_n-p_n)(e_n-e_M); all these coefficients are nonnegative under the
stated M condition and their sum is R_M. The finite subclass gives the other
inequality. This is uniform in b; an oscillating arbitrary tail is covered.

The finite problem is a second-order-cone program: introduce u_n,v_n>=0 with
u_n^2<=e_n e_(n+1), v_n^2<=(1-e_n)(1-e_(n+1)), and
2 sum w_n(1-u_n-v_n)<=b. Maximize c.e. Choosing both positive square roots
shows equivalence, not merely relaxation.

## A solver-independent certificate and its actual consumer

For any interior rational point x and rational lambda>=0, define

    g=c-lambda grad C_M(x),
    U=lambda b+c.x-lambda C_M(x)
          +sum_i max(g_i(1-x_i),-g_i x_i).

Convexity implies C_M(e)>=C_M(x)+grad C_M(x).(e-x). For a feasible e this
bounds c.e by U, because a linear function takes its box maximum at a corner.
Therefore V(b)<=U+R_M. The derivative used is

    partial_x h(x,y)=-sqrt(y/x)+sqrt((1-y)/(1-x)).

No KKT optimality or solver success flag is assumed. x need not be feasible.
Any interval-certified feasible y provides lower bound L=c.y. Boundary
optima cause no derivative problem because the certificate point x is interior.
Shrinking an almost-feasible x to y=(1-rho)x+rho/2 gives
C_M(y)<=(1-rho)C_M(x) and scales its contrast by1-rho.

The companion probe embeds a rational M=12 candidate for z=1/4,b=1/10,
found by numerical stationarity search and then checked independently with
outward Arb arithmetic at256 bits. It takes rho=10^-30, checks the actual
energy of y against the budget, and evaluates the tangent upper certificate.
It proves the conservative full infinite-frontier bracket

    0.51042093979 < V(1/10) < 0.510421521.                (3)

The constant-tail Kraus sqrt(y_n),sqrt(1-y_n) is an explicit feasible detector,
not merely a dual obstruction. R_12=0.00000058114528656005859375 explains
nearly all the gap. Its optimum equal-prior error lies between
0.2447892395 and0.244789530105. Candidate search is numerical evidence; the
rational input and interval certificate establish(3) without rerunning a solver.

## Sharp small-budget behavior and a stricter finite-budget bound

Let t=sqrt(b/S), theta_n=min(pi/4+nt,pi/2), e_n=sin^2 theta_n. Every adjacent
angle step is in[0,t], so

    C(e)=2 sum w_n[1-cos(theta_(n+1)-theta_n)]<=S t^2=b.

For each fixed n, (e_(n+1)-e_n)/t tends to1 as t tends to0, and is between0
and1 by the derivative bound for sin^2. Dominated convergence gives
Delta/t -> aS. Together with K2153's V(b)<=sqrt(b/z), this proves

    lim_(b downarrow0) V(b)/sqrt(b/z)=1.                  (4)

This is an actual clipped-angle construction; no varying mode or varying
signal is used. It does not attain the simple square-root bound at finite b.
In fact, for 0<=b<=2S,

    V(b) <= sqrt(b/z-(1-z)^2 b^2/(4z^2)).                 (5)

For adjacent theta, |Delta e|<=sqrt(h(1-h/4)). The function on the right is
concave and increasing for h in[0,2]. Weighted Jensen and C<=b give(5).
Always also impose the K2151 unrestricted total-variation ceiling. Every
square-root binary instrument has C<=2S; budgets beyond that need no use of(5).

## Exact saturation budget, including likelihood ties

Let N=z/(1-z), k=floor(N)+1. The maximum unrestricted contrast is
Dmax=k(1-z)z^(k-1). For noninteger N, equality forces the unique sharp
threshold e_n=1_(n>=k), so the smallest saturation budget is

    b_sat=2k z^k.                                        (6)

For integer N=ell>=1, only e_ell=t is free at this contrast. Lower effects
are0 and higher effects1. The two nonzero energy edges have equal weight
A=ell z^ell=(ell+1)z^(ell+1), so

    C=2A[2-sqrt(1-t)-sqrt(t)],
    t_opt=1/2, b_sat=2ell z^ell(2-sqrt(2)).                (7)

Thus V(b)=Dmax iff b>=b_sat; below it strict inequality follows from attained
maximality and the necessary form of every unrestricted optimizer. For z=1/4,
Dmax=3/4,b_sat=1/2. For z=1/2, Dmax=1/2,b_sat=2-sqrt2, less than the sharp
threshold cost1. A hard threshold misses the optimal tie instrument.

## Controls, limits and next work

Exact controls cover geometric sums, summation by parts, constant-tail
objective and energy, tie/non-tie saturation and positive square-root versus
classical realization. Interval controls certify the actual candidate and
box-tangent bounds. Mutations change weights, tail coefficient, signal,
budget/dual data and the tie effect, not the checks themselves. The infinite
compactness, convexity, tail, Jensen and asymptotic proofs are independently
reviewed separately from finite checks. No external certification or novelty claim.

The fixed-mode diagonal frontier is now computable with an explicit global
error bound, rather than merely bounded below by energy cost. A new detector
question should change the operation algebra, signal or resource objective
explicitly, or build a stable autonomous apparatus with preparation/reset costs.
Those are not implicit corollaries of output-field-energy optimality.
