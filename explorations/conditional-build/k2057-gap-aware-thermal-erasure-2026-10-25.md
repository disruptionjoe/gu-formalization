---
title: "K2057: Sharp gap-aware tail stability and its thermal certificate"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional thermal return and attached-tail bounds; no exact optimum, source or physics verdict
scripts:
  - tests/channel-swings/k2057_gap_aware_thermal_erasure.py
  - tests/channel-swings/k2057_gap_aware_thermal_erasure_probe.py
---

# K2057: Sharp gap-aware tail stability and its thermal certificate

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
result: sharp loss coefficient for gap-aware erasure and a stronger whole-energy lower certificate
carrier: finite or countable positive-spacing catalyst supports for the four-state thermal channel LAYER=toy CHIRALITY=N/A
pairing: diagonal classical marginal return ON=declared_thermal_population_model
real_structure: nonnegative real populations and exact rational arithmetic
grading: energy-support gaps, not spinor or Grassmann parity
action_owner: repository-construction -- K1935 thermal channel and K2054 erasure
target: unnormalized tail loss and unrestricted finite/countable lower bound MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] At bath parameter t=1/2, the actual legal
sequence of support gaps strengthens K2054's erasure bound to

    q <= B + (25/4) Delta <= (14/55)b + (25/4) Delta.       (1)

Here q is erased mass, Delta is the actual UNNORMALIZED loss of return, b is
retained attachment population and B uses its incoming/outgoing gap constraints.
The loss coefficient25/4 is sharp. This result is consumed below in a strictly
stronger finite/countable thermal lower certificate at spacing1/2<delta<=1.
It does not solve that unrestricted optimum.

## 1. Existing inputs and the new question

[K1935](k1935-arbitrary-support-thermal-return-2026-10-22.md) and
[K1956](k1956-finite-energy-thermal-gap-2026-10-22.md) already supply legal path
geometry and invisible-tail rewards. [K2054](k2054-quantitative-terminal-erasure-2026-10-25.md)
supplies the incoming-aware terminal response and sharp excess coefficient.
The new work is their quantitative composition and finite-certificate use,
not rediscovery of the Bellman constants or a new basis enumeration.

Each connected support component is an increasing path, with edge gaps d in
{1,2,3} and consecutive gaps satisfying d+e>=4. At t=1/2 write

    k=(7/29,1/9,1/23), c=(29/135,9/50,23/90).

For an erased terminal population u with predecessor p, its actual return loss
is at least c_d (u-k_d p)_+. The predecessor's incoming flow is allowed;
K2054 proves this for every such flow, not only an isolated pair. A component
root has no predecessor and loses p_root/2 when finally removed.

## 2. Gap-aware propagation and sharp loss coefficient

The exact invisible-tail rewards, according to first outgoing gap, are

    A=(14/55,1/8,3/55),
    A_d=k_d(1+max_{e:d+e>=4}A_e).

These equations bound every finite path by backward induction. Products of
k_d are bounded by(7/29)^n, so the remainder vanishes and the same bounds hold
for infinite paths. Repetition of gap2 and alternation of1,3 achieve them.
After a vertex whose incoming gap is d, the allowed continuation reward is

    beta_d=max_{e:d+e>=4} A_e=(3/55,1/8,14/55).

Set x_j=(p_j-k_dj p_(j-1))_+. Recursively substitute
p_j<=k_dj p_(j-1)+x_j. The initial retained population contributes at most its
permitted outgoing reward times that population; each x_j contributes at most
(1+beta_dj)x_j to erased mass. All terms are nonnegative, so

    q <= B+sum_j(1+beta_dj)x_j,
    (1+beta_d)/c_d=(54/11,25/4,54/11).

Descending deletion gives Delta>=sum_j c_dj x_j. A wholly erased root
contributes at most(69/55)p_root and loses p_root/2; its ratio138/55 is smaller
than25/4. Sum over components to obtain(1). No entirely erased multi-input
component is falsely assigned return q/2. Positive spacing makes bounded
energy intervals finite. Apply the finite inequalities to truncations, then
use nonnegative-series convergence and inherited l1 continuity of the return.
This proves the countable assertion without selecting a highest infinite vertex.

The boundary reward is sharp for invisible geometric tails on each admissible
periodic gap pattern. To prove sharpness of25/4, retain populations a at1 and b
at3, where0<a<=4b. Add p_(5+2j)=(3b/2)9^(-j), j>=0. Every deletion beyond
energy5 is invisible, and deletion of the first tail vertex has Delta=b/4;
the incoming flow into b is zero. Meanwhile q=27b/16 and B=b/8, so

    q-B=(25/4)Delta.

The mean energy is finite. Normalizing the entire state preserves equality
by homogeneity; nonnegative integer shell completion gives physical supports
for spacing<=1. Finite truncations approach equality. Sharpness of this
auxiliary inequality does not imply sharpness of the relaxed global bound.

## 3. Consume the actual boundary state in the cutoff-eleven bank

First canonicalize each FULL component, preserving its original offset and
initial gap; then erase the suffix above canonical energy11. Keep each bank
cell's fixed support s even on zero-population faces. If z is
its last canonical energy and r its last gap, define

    B(v)=p_last * max{A_g: g in{1,2,3}, z+g>=12, r+g>=4},

with empty maximum zero and no incoming-gap condition for a singleton.
Thus B=0 below9. At9 its coefficient is3/55. At10 it is3/55 if r=1 and1/8
otherwise. At11 it is beta_r. Using a possible rather than actual attachment
overestimates B and is safe. Recompressing an individual zero face before
computing B would destroy the linear interpolation functional and is forbidden.

For any0<=eta<=4/25, (1) and Delta>=0 imply Delta>=eta(q-B).
For each possible low cell choose one triple(a,s,eta), s<0, and prove

    R(v)-eta B(v)>=a+s e(v) on that low cell,
    R(v)-eta B(v)>=a+s(e(v)+1) on EVERY high cell,
    a+12s<=eta, a+13s<=eta.                              (2)

The complete inherited arrangement bank includes the deficit hyperplanes.
Hence R and B are affine on each subcell, and checking all vertices proves(2)
throughout; convexity alone would not suffice for a lower bound from vertices.

For a component of offset d, total mass m, erased mass q and canonical tail
energy h>=12q, take ell=0 for the at-most-one d<1 component and ell=1 for all
others, using K2049's spacing packing theorem. Combine(2) and erasure:

    R_component >= a*m+s*e_actual
       +q[eta-a-s(12+ell)]+(-s)(h-12q)+(-s)(d-ell)m.

Every correction is nonnegative. Wholly erased components obey the same
estimate with B=0. Use the low cell's one triple for ALL high components,
sum, and apply the upper energy budget with s<0. Countable transfer follows
from finite truncation and l1 continuity as above. This is an attached-tail
argument, not a fictitious zero-return tail inserted into the optimization.

## 4. Exact result and released whole-energy interval

At E=5/2 the new certificate and released witness prove

    243396/878731 <= F_delta(5/2) <= 67173/240731.

The lower gain over K2054 is 14526009041/1395933964741400. The improved upper
gain over K2053 is 1270845/6613362032. The remaining
width 434034987/211537792361 is positive; no optimum is claimed.

For every1/2<delta<=1 and 2843/1165<=E<=77294135/28446113,

    F_delta(E)>= 295884/878731 - (104976/4393655) E.

The interval endpoint is a certificate-envelope crossing, not an asserted
physical phase transition. The physical upper family on this interval is

    U(E)=11501/33582-(434/16791)E, E<=91135/37292;
    U(E)=(70083-1164E)/240731, E>=91135/37292.

The first family is valid from2843/1165 to91135/37292; the second extends
to25725/8836. Their meeting values coincide. Compared with the previous
upper line, improvement is strict after the shared first endpoint.

### Exact ceiling of the present affine relaxation

The grid bottleneck is cell188. Solve its three active constraints exactly:
low vertex57 has(e,R,B)=(28361/11755,6561/23510,1/94040);
high cell180 vertex56 has(e+1,R,B)=(3858/815,729/3260,1/13040);
the tail constraint has(e,R,B)=(12,0,-1). They give

    (a,s,eta)=(295884/878731,-104976/4393655,219708/4393655).

All low/high/tail inequalities hold, and every other cell assignment exceeds
this objective at5/2. Positive dual weights

    (2174675/2259594,2674015/71177211,1867/142354422)

sum to1, average energy to5/2, cancel B, and average R to243396/878731.
Thus averaging the three constraints proves that no affine certificate of
form(2) for this cell can exceed the new bound. The displayed feasible
assignment attains it. This proves optimality of THIS RELAXATION at5/2,
not the physical optimum or uniqueness of the triple.

The dual mixture is not a physical witness: its positive odd low support and
high support translated by1 place occupied energies1,2,3 in the same bath
shell3, violating the inherited two-input capacity. A stronger certificate
must use compatible component placement or stronger boundary-tail energy
coupling; merely refining eta cannot improve this relaxation at5/2.

### Construct the new physical witness rather than only lowering a certificate

Take K2053's same six-odd-input population segment. If its final population
at11 is b, append p_(11+2j)=b/9^j for j>=1. K2054's exact zero-loss criterion
shows every later deletion is invisible; finite truncations and l1 continuity
therefore retain the original UNNORMALIZED return. Added mass is b/8 and
added energy is53b/32. Normalize the WHOLE state and retune the original
segment parameter to restore the desired mean. At E=5/2 the original
segment parameter is23045/192436, strictly between0 and1. The normalized
occupied prefix1,3,5,7,9,11 is

    (88572,132858,14762,1873,992,1488)/240731,

and its tail is1488/(240731*9^j) at11+2j, j>=1. Its total mass is1,
mean5/2, and return67173/240731. The full nonnegative integer spectrum
supplies shell completion for any spacing<=1. Countable finite mean is
allowed by the declared model; this does not establish a finite minimizer.

A tangible finite improvement needs only one added occupied point. The
15-level spectrum0,...,14 with occupied odd1,...,13 populations

    (16416,24624,2736,348,186,279,31)/44620

has mean5/2 and return24903/89240, already below the old upper. This is a
sufficient size for this witness, not a proven minimum or optimal size.

For the whole-energy upper family, append full invisible tails to both
K2053 segment endpoints. Normalization maps their means to91135/37292
and25725/8836. Homogeneity/projective reparameterization maps the original
positive segment onto the segment between the normalized endpoint profiles;
the inherited fixed-cell return is affine along it. Eliminating the segment
parameter gives the second line above. To cover the small first interval,
attach a fraction0<=lambda<=1 of the same invisible tail to the original
left endpoint. Its first edge remains below threshold, so erasure is still
invisible. Normalize, eliminate lambda, and obtain the first line. This is
one compatible physical family, not independent fits of energy and return.

### Near-saturation forces where loss can occur

Let delta_j be each actual descending terminal deletion loss and let
D=B+25Delta/4-q>=0. The same proof gives the stronger quantitative statement

    D >= (59/44) sum_(gap1 or gap3) delta_j
            +(823/220) sum_(erased roots) delta_root.

Indeed25/4-(1+beta_d)/c_d is59/44 for d1,3 and zero for d2; the root
margin is25/4-138/55=823/220. Consequently small D forces non-gap2
loss and root loss small. Equality permits positive terminal losses only
at gap2 with u=3p/2,p>0 and zero incoming predecessor flow. These are
NECESSARY conditions; all propagation and Bellman slack must also vanish.
Invisible gap1/3 populations are not excluded. This is erasure rigidity,
not an optimality or finite-resource necessity theorem.

## 5. Reproduction, hostile review and limits

The producer solves exact two-dimensional hull certificates for a declared
finite eta set, replaces its bottleneck by the exact contact solution, and
stores all671 cell assignments plus a matching three-contact dual ceiling. The separate
probe uses raw bath-label maxima, checks every20975 vertex value and all
low/high/tail inequalities, checks292 finite physical tail/saturation controls,
checks the new finite/countable witness, both upper-family pieces and
near-equality inequalities, and rejects ten mathematical faults in loss,
boundary, sharp mass, intercept, eta, slope, tail energy, upper line, rigidity and dual weights. The prior626412-basis completeness is pinned reuse.

The proof carries arbitrary populations, sharpness and countability; fixtures
are not universal proofs. Independent internal derivation and integrating
hostile review check incoming flow, roots, illegal consecutive gaps, fixed
zero faces and common-cell transfer. No external or novelty certification.
Source, physics ledger and canon are unchanged. Strongest next competitor is
a better physical witness or a certificate retaining component compatibility
and boundary-tail energy coupling; do not
call the remaining positive gap equality or re-enumerate a settled bank.

Run both named scripts from the repository root; the producer's --write option
rebuilds its JSON artifact. No mutation of inherited inputs is needed.
