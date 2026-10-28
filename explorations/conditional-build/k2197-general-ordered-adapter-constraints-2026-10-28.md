---
title: "K2197 Ordered general-adapter constraints and a real support-family exclusion"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: one four-real-parameter normal-trivector support family of fixed normalized adapters
scripts:
  - tests/channel-swings/k2197_general_ordered_adapter_constraints_probe.py
---

# K2197 Ordered general-adapter constraints

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
result: K2197 ordered four-parameter real fixed-adapter exclusion
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and scope

No nonzero real port in the four-parameter family below admits a fixed normalized adapter.
Generic members have BOTH nonzero commutator and anticommutator: this is not
another commuting or anticommuting stratum. A general ordered pencil identity
is also derived without either simplification. The exclusion uses two exact
coefficients of the necessary contraction of all ten original equations, then
closes every parameter face and singular-pencil case. It does not exclude all
general noncommuting ports, complex parameters or changed adapters.

The object and source ceilings remain those of K2169/K2171/K2195. SC-OP-04
ASSERTS candidate four-field grammar, not these adapters; SC-GEO-55 ASSERTS
rotated-LC displacement, not ordinary torsion. No source, full16cell/full20,
K-C, physical quotient, native2+1/chirality, ledger0.263 or canon change.
No GU falsification, novelty or proof-assistant/external-expert claim.

## 1. A fully ordered norm-one pencil

Write R=v+3t, bar(R)=v-3t, P=R+6bar(R)=7v-15t and S=5R+2bar(R)=7v+9t.
Here bar is K2169's tangent-volume sign automorphism, NOT Clifford reversion.
It is multiplicative and involutive. For a nonzero candidate port, P is invertible by the original adapter
necessity. Set Y=P^-1 bar(P). Then

    Y invertible, bar(Y)=Y^-1, P^-1 S=(I+4Y)/5.

Let A and B denote K2171's ordered Euler coefficients:

    A=3K(bar(R)^2)+34bar(R)^2+36Rbar(R)+8bar(R)R-24R^2,
    B=184R^2+140Rbar(R)+184bar(R)R+194bar(R)^2
      +24K(bar(R)R)+15K(bar(R)^2).

The necessary filter A(P^-1 S)=B implies the paired relations

    4A Y=5B-A,
    (5bar(B)-bar(A))Y=4bar(A).

The second follows by applying bar to the first and multiplying on the right
by Y. No product can be commuted, no individual port inverse is assumed, and
these necessary relations are not a complete original-row solution test.

## 2. A genuinely general noncommuting family

Use normal orthogonal generators n1,...,n10, the first four of positive
square and the last six negative, on the existing W(3,1)+N(4,6) split. Put

    A0=n123, B0=n145, C0=n126,
    w=a A0+b B0, u=c A0+d C0, v=I_N w, t=Omega u,

with real a,b,c,d. A0²=-1, B0²=C0²=1;
[A0,B0]=[B0,C0]=0 and {A0,C0}=0. Therefore w² is nonscalar when ab!=0,
while u²=-c²+d² is scalar. Generically both [v,t] and {v,t} are nonzero.
K2177 excludes the class where BOTH port squares are scalar, not this whole
family. K2195 excludes {v,t}=0, not its generic members.

Define

    k=-49a²+49b²+225c²-225d²,
    Y0=98ab A0B0-210ad Omega I_N A0C0,
    delta=(49a²+49b²+225c²-225d²)^2-(210ac)^2.

Exact Clifford multiplication gives P²=k+Y0,
Y0²=-196a²(49b²-225d²) and (k+Y0)(k-Y0)=delta I.
Thus for delta!=0, P^-1=P(k-Y0)/delta. Conversely, if delta=0 and P were
invertible, P²(k-Y0)=0 would give k-Y0=0. The scalar and nonscalar blade
supports force k=Y0=0, contradicting invertibility. No singular-pencil branch
is omitted when denominators are cleared.

## 3. Two coefficients exclude the open parameter chart

Let F=delta[A(P^-1 S)-B], using the ordered coefficients in section1.
The exact coefficient of n36 in F is

    8064 a² c d (49a²+259b²-495c²+495d²),

and the coefficient of n2456 is

    -8064 a b c d (259a²+49b²+495c²-495d²).

For abcd!=0, simultaneous vanishing forces the two brackets to vanish.
Their sum is308(a²+b²), impossible over the reals. These are necessary
coefficients of the exact full-row contraction, not numerical sampled fits.

## 4. All faces and useful follow-through

If a=0 or b=0, both squares are scalar; the existing K2177 theorem excludes
that face. If d=0, [w,u]=0 and therefore {v,t}=0; K2195 excludes that face.
These include all boundary intersections with a nonzero total port. The zero
total port remains the known positive control and is not excluded.

It remains to treat c=0 with abd!=0. Put L=49a²+49b²-225d², so delta=L²
and L!=0. In the ordered Omega times normal-blade basis, F has coefficients

    Omega*n124578910: +1008 a d L (21a²+29b²-69d²),
    Omega*n1378910:    144 b d L (7a²-49b²+153d²).

The first coefficient changes sign if expressed in the corresponding sorted
full14 blade; the zero equation does not. Multiplying the first bracket by153
and the second by69 and adding yields3696a²+1056b²=0, again impossible.
The complete real support family is excluded. Real nonnegativity is essential;
this proof deliberately makes no complex-family claim.

## Verification and next condition

The probe constructs the parameter polynomial in exact sparse full Cl77,
checks inverse/denominator and displayed coefficients, and independently
replays all ten original rows at three genuinely noncommuting rational
fixtures. Every fixture fails all ten rows; their Euler contraction agrees
with the symbolic ordered filter. Exact basis identities, polynomial proofs
and finite fixtures are separate evidence kinds. Mutations corrupt signs,
coefficients and original-row contractions and must fail after a green baseline.
Prior scalar-square and anticommuting banks are reused by pointer.

The paired Y relations apply more broadly, but a general classification still
requires additional ordered constraints or an actual all-ten-row solution.
Do not repeat this support family or infer a general no-go from it. Compare
other genuinely noncommuting supports with changed principal/core
constructions; K2021 already supplies the degree-dual map and K2199
classifies all local zeroth-order bilinear pairing freedom for the fixed
full fourteen-direction principal operator.
