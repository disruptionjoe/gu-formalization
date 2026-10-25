---
title: "K2075: Thermal population rigidity and minimum physical dimension41"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical result only; no GU source verdict, canon promotion or novelty certification
scripts:
  - tests/channel-swings/k2075_thermal_equality_rigidity.py
  - tests/channel-swings/k2075_thermal_equality_rigidity_probe.py
---

# K2075: Thermal population rigidity and minimum physical dimension41

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
result: exact optimizer population and minimum physical dimension
carrier: fixed four-state bath and finite/countable nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: classical nonnegative populations and marginal return ON=declared_bath_catalyst
real_structure: exact real rational population data
grading: occupied energies and resonance components
action_owner: repository-construction -- inherited shell-capacity model
target: attainment of the fixed-bath energy-constrained optimum MAP-TYPE=intertwiner
```

[Conditional mathematical theorem, internal verification.] In K2074's OPEN energy
interval, at every spacing1/2<delta<=1, the unique attaining occupied population
measure is K2068's N20 affine family on energies1,3,...,39. The minimum physical
catalyst dimension is exactly41. The theorem classifies occupied populations, not
implementing channels or all spectra with additional empty levels. Endpoint ties
are excluded. This is independent mathematics, not a GU prediction or source verdict.

## 1. Inputs and what is new

[K2074](k2074-subdivided-incoming-thermal-bound-2026-10-25.md) proves the exact
finite/countable optimum a-tE, with

    a=178897536881397/603186054075536,
    t=4369812550533/603186054075536>0.

Its JSON gives the exact interval, approximately(2.4800787763,2.5075721054).
It already forces genuine low cell187, support[1,3,5,7,9,11], offset0, saturated
energy, and13 necessary/41 sufficient physical levels. This note resolves the
remaining high-component and tail equality conditions. It reuses the corrected
cell188 coverage and full671-cell theorem; it does not rerun the discarded candidate
or optimize the already-closed return value.

We inherit K2054's terminal-deletion inequality, K2059's Bellman transfer, K2072's
physical placement and K2070's ORIGINAL theta0 cell187 certificate. The latter
must not be replaced by K2074's weaker attempted common-weight cell187 fit.
The inherited bank and piecewise arrangements are pinned; their completeness and
physical applicability remain load-bearing premises, distinct from new arithmetic.

## 2. Excluding all high components

Use the fixed pair(a,t) above and the compulsory high offset ell=25/2 for cell187.
Every normalized retained high vertex has positive slack; the smallest is

    gamma=25501739398440510383/979482165945423944760.

Every high suffix cost cap remains valid: raising the offset from the inherited10
to25/2 lowers the Bellman intercept, so each high Bellman value decreases. The
producer checks these caps directly as well.

The margin multiplies RETAINED mass, not total component mass. Affine interpolation
within each actual deficit-sign cell proves positive slack for any high component
with positive retained mass. A component entirely above the retained cutoff has a
positive root margin, at least

    gamma_root=3661955709573038111854597/10381420612163588388107744.

It multiplies the positive root population; Bellman/deletion handles its suffix.
Past cutoff64 the reward a-t*n is negative and Bellman is zero, so the root
inequality only strengthens. Every nonzero component has either retained mass or
an actual first occupied atom (positive spacing and a lower energy bound ensure
this). Thus equality has no high component. Nonnegative component slacks cannot
cancel in a countable mixture. Energy not spent and dropped low offset each cause
t times their respective nonnegative energy contribution, so equality retains
K2074's energy saturation and zero offset.

## 3. Low cone and the only three-terminal contact

Enumerate every permitted actual one-, two- and three-terminal piecewise vertex
with the SAME(a,t). There are759 vertices and329 rays. The unique maximal price is

    beta=57467869320797/301593027037768,
    gaps=(2,2,2), (p13,p15,p17)/p11=(3/2,9/4,27/8).

The second price is180592949475691/1206372108151072. All recession directions are
strict: their minimum slack is31109548066029/150796513518884. Shorter terminal
paths are included; a triple's third reward is its Bellman value, not just a-t*n.
The origin/zero suffix has price0<beta. Hence equality forces that triple and its
positive populations; the piecewise affine maximum cannot also be achieved along
a flat recession direction.

For cell187 the low inequality is R_low>=a*M_low-t*E_low+beta*p11.
Its only zero-slack bank vertices are33 and35. Normalize by retained mass and
choose the ACTUAL dominance and deficit-sign subcell containing the population.
R_low and the displayed slack are affine there. Convex interpolation through that
subcell's vertices forces every positively weighted vertex to be33 or35. Thus the
unnormalized low population lies in their positive cone. Zero coordinates are
classified by actual support as required by K2074; they create no extra equality
cell. On this cone p11>=p9/4, so incoming flow at11 is zero. The actual incoming
deficit equals p11: the theta0 worst-incoming estimate is attained here, not merely
presumed tight.

## 4. Additive suffix slack proves the full tail

Retain the prefix through n0=17, with incoming gap d0=2. Write a further connected
suffix as p_j at n_j, gap d_j=n_j-n_(j-1). Let

    w_j=a-t*n_j, G_j=G(n_j,d_j),
    x_j=(p_j-k_(d_j)*p_(j-1))_+,
    y_j=(k_(d_j)*p_(j-1)-p_j)_+,
    k_1=7/29, k_2=1/9, k_3=1/23,
    c_1=29/135, c_2=9/50, c_3=23/90.

D_j is the actual return change on adding the terminal j to its prefix, equivalent
to descending deletion after later terminals have gone. K2054 proves D_j>=c_d*x_j.
Define h_j=G_j-w_j-k_(d_(j+1))*G_(j+1), with terminal h_m=G_m-w_m.
The Bellman recurrence makes h_j>=0. The EXACT identity is

    Delta+G0*p0-sum_(j=0..m) w_j*p_j
      =sum_(j>=1)(D_j-c_d*x_j)
       +sum_(j>=1)(c_d-G_j)*x_j
       +sum_(j>=0)h_j*p_j+sum_(j>=1)G_j*y_j.       (1)

Here Delta=sum D_j=R_full-R_prefix17. Substitute
p_j=k_d*p_(j-1)+x_j-y_j to verify the telescope; all summands are nonnegative.
Every reachable continuation after17 has n>=19. All such caps are STRICT:

    c_d-G(n,d)>=12171961184103/3769912837972100>0.

The minimum is at(19,2); for n>=41, G=0 and the margin is c_d. Thus equality in(1)
forces x_j=0. At each positive Bellman value, y_j=0 forces p_j=k_d*p_(j-1).
From17 through37 the unique maximizing successor is gap2, with value strictly
above stopping; a positive predecessor therefore forces the next atom. At39,
G39=w39>0 and later Bellman values vanish. Since40<a/t<41, any further positive
atom at n>=41 has h_j=-w_j>0 and is excluded. The required suffix is consequently
19,21,...,39, with successive ratio1/9. A disconnected suffix would be a high
component and was already excluded.

For a countable path, finite prefixes give Delta=sum D_j by the inherited l1
continuity of raw return. Bellman has finite support below41; positive spacing
leaves finitely many atoms there. There is therefore no boundary term at infinity.
Finite first moment gives sum |w_j|p_j<infinity, and nonnegative slack sums pass
monotonically to the same identity. An infinite collection of small positive slacks
cannot give equality. This is a proof for countable catalysts, not a finite-sample
inference.

## 5. Unique normalization, physical minimum and a stability consequence

Extend each of low vertices33/35 by the forced triple and tail. Their normalized
energies are the two distinct endpoints

    11836234695567/4865270085667,
    991560367479/368093049355.

The full K2074 closed interval lies strictly between these. Normalization and
saturated energy therefore uniquely determine positive coefficients in the extended
cone. Exact rational elimination reproduces ALL20 K2068 affine population pairs.
Every occupied population is positive on the open interval. The complete support
is1,3,...,39; no countable competitor attains with a different population measure.

For every adjacent occupied pair y,y+2, the shared bath shells y+2 and y+3 each
have two occupied inputs and require four distinct physical catalyst states in the
original shell-capacity model. Those shells force levels y-1,...,y+3. Taking the
union over pairs1,3 through37,39 forces ALL physical levels0,...,40. Thus d>=41.
K2068 explicitly realizes the same populations and return on those41 levels, so
this lower bound is attained. It does not count only the20 occupied levels.
For an actual permitted channel, R_physical>=R_raw>=a-tE; optimum attainment forces
raw equality, so the argument applies without claiming channel uniqueness.

Equation(1) also yields a quantitative consequence. If a suffix's nonnegative dual
slack (left side) is at most epsilon, its total excess above the zero-loss edge
threshold satisfies sum x_j<=epsilon/mu, with mu the strict cap margin above.
Likewise sum h_j*p_j<=epsilon and sum G_j*y_j<=epsilon. These are exact weighted
stability bounds for the stated suffix, not an unproved uniform distance bound to
the optimizer. High retained mass is bounded by epsilon/gamma when its TOTAL
component certificate slack is at most epsilon; use the separate root bound for
wholly erased components. Tiny populations must not be rounded to zero in a
minimum-dimension claim.

## 6. Verification and scope

Producer: exact price/ray/low/high/root/cap census, finite-support Bellman policy,
two-cone mass/energy solve and equality of all20 affine populations. Separate probe:
raw bath losses, independent Bellman recursion, explicit finite telescoping identity,
physical-shell necessity, actual feasible channel return and corrupted mathematical
inputs. Geometry banks are pinned reuse, not regenerated or recounted as new proofs.
Independent internal thermal review checks the equality and countable transfer.
No external specialist or proof-assistant verification, source/ledger/canon change,
optimizer-channel uniqueness, or novelty certification is claimed. Exact interval
endpoints and other spacing/energy phases remain separate questions.
