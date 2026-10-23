---
title: "K1995: Exact central circulation improves the feasible pulse norm"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1995_central_marginal_cycle_improvement.py
  - tests/channel-swings/k1995_central_marginal_cycle_improvement_probe.py
---

# K1995: Exact central circulation improves the feasible pulse norm

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
result: explicit exact-marginal capped central variation and strict regional nonoptimality certificate
carrier: K1991 central rectangle inside the actual width9 characteristic strip LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue L2 pulse norm and unchanged row/column marginals ON=characteristic_strip
real_structure: real bounded measurable controls at amplitude23/100
grading: paired row and ramp intervals, not source chirality
action_owner: repository-construction -- fixed scalar transport problem
target: explicit feasible central improvement and global norm upper bound MAP-TYPE=intertwiner
```

## Result and boundary

The explicit central pulse of [K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md)
is NOT the minimum-norm central solution. A four-rectangle circulation, together
with its reflected partner, gives an explicit new pulse with exactly the same
row and column marginals and the same amplitude cap. Its squared norm is lower
by more than0.0005495118. Applied to the actual algebraic phase and combined
with the inherited feasible wings, this gives

    2.34940177149 < ||v_dagger||^2 < 2.7541718523,
    ||v_dagger - w_1989|| < 0.636216.

The lower certificate and comparison witness come from
[K1989](k1989-capped-pulse-dual-certificates-2026-10-23.md).
The improvement is in pulse L2 norm, not the already optimal phase energy.
This is an exact feasible central formula and a whole-pulse upper certificate
using existing wing existence. It does not supply explicit wings, a global
minimum-norm formula, regularity, source identification or a new GU verdict.
K1991 explicitly left central optimality open, so its feasibility and earlier
bound remain valid. This answers that open optimality question negatively.

## 1. An exact circulation on the actual central rectangle

Reuse K1991 coordinates x=u/t in[-1,1], the two ramp coordinates y in[-1,0]
and[0,1], dz=2t dy, and the middle strip3<=z<=6. Its pulse q0=v/M is

    f(x)=(3+4t)x/(3+4tx),
    q0(x,y)=sign(y) if |y|>|x|,
            -sign(x)f(|x|) otherwise,
    q0(x,middle)=-sign(x)f(|x|).

Here t is the same isolated root of101t^4-102t^3-168t^2+392t-138,
9/20<t<23/50, and M=23/100. No surrogate marginal is used.

Let a=1/4,b=1/2,h=1/2,l=1/4. For each x in(a,b), pair row x with row x+h.
Use the two equal-width positive ramp intervals I=(0,l) and J=(b,b+l).
The four old values, in row-major order, are

    [-f(x), 1; -f(x+h), -f(x+h)].

Put e(x)=1-f(x+h), and add

    [+e(x), -e(x); -e(x), +e(x)].                      (1)

On negative rows and negative ramp columns impose the odd reflection
q(-x,-y)=-q(x,y); elsewhere retain q0, including the entire middle strip.
Values on interval endpoints may retain q0, since all identities are a.e.
This defines the pulse completely on the central rectangle.

Each row gains and loses e times the same physical width2tl, so its integral
is unchanged. In each affected column the paired row intervals have equal
length and the substitution x2=x1+h identifies their e functions exactly;
their column changes cancel. Reflected intervals cancel in the same way.
Therefore BOTH continuum marginals, and hence the existing phase and plateau
data, remain exact. There is no numerical residual or subsequent cap repair.

## 2. Cap and optimal amplitude in this particular family

The new four values are

    [-f(x)+e, 1-e; -1, -f(x+h)+e].                    (2)

Since0<=f<=1, 0<=e<1/5, and f(x)>=0, all four lie in[-1,1].
For the first entry, -f+e>=-1 and -f+e<=1/5; the last is1-2f(x+h).
Thus the amplitude cap holds everywhere a.e., including reflected cells.
This variation moves saturation from part of the upper row to the lower row;
it does not assume slack on the forced outer regions.

More generally replace e in(1) by any nonnegative measurable amplitude eta(x).
The lower-left cell enforces eta<=1-f(x+h)=e. The squared-norm decrease
of the four values is

    g(x,eta)=2eta(1+f(x))-4eta^2.                     (3)

For0<=eta<=e<1/5, its derivative2(1+f)-8eta is positive. Hence eta=e is
pointwise optimal among these nonnegative circulations on the FIXED four
intervals. This is not a global optimality claim or optimization over interval
endpoints. Equation(3) is strictly positive for a<x<b, proving q0 nonoptimal.
The old pulse remains a valid feasible witness.

## 3. Exact norm transfer and verification

A ramp rectangle has area element du dz=2t^2 dx dy. Summing the four cells
and their negative reflected partners gives the exact norm decrease

    Delta = 4M^2 t^2 l int_a^b [2e(x)(1+f(x))-4e(x)^2] dx.       (4)

The producer encloses this rational integral on2048 intervals using rational
arithmetic and the isolated algebraic t interval. Each interval contribution
is rounded OUTWARD to denominator10^30 before summing, preventing denominator
explosion without changing enclosure direction. The result is

    0.0005495118646081 < Delta < 0.0005513080380521.

Subtract the lower endpoint from K1991's rigorous whole-pulse upper bound.
Subtract the inherited K1989 lower certificate again to obtain its strong
Fenchel distance certificate. The new bounds at the top follow with outward
rounding. No implication about smooth-pulse phase energy is taken.

The separate probe derives(3) symbolically, uses monotonicity of f in both x
and t to obtain an independent1024-cell integral enclosure, and checks exact
row/column cancellation and cap on rational controls. Its1157 mixed symbolic,
interval and cycle obligations pass. The producer has2800 rational controls.
Three altered integral, upper-transfer and distance inputs are rejected by
mathematical assertions after a green baseline. Counts do not establish the
continuum statement: equations(1)-(4) do.

Strongest overclaim: calling a fixed-family optimum the central or global
optimizer. Strongest contrary case: tightening the cap destroys a generic
marginal correction; equations(1)-(2) prove that this one is feasible directly.
Weakest remaining seam: explicit nonconcave wings and full central optimization.
The next useful construction must address one of those questions or preserve
both marginals under a larger certified optimization, rather than merely add
decimal places to(4). Same-author internal checks are not specialist review,
proof-assistant certification or novelty evidence. Source, physics-ledger and
canon verdicts remain unchanged; SC-META-53 remains UNCERTAIN.
