---
title: "K2216 Global detector localization and exterior certificate"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all global minimizers localized and stationary-minimizer tiles excluded; global uniqueness remains unproved
scripts:
  - tests/channel-swings/k2216_detector_exterior_certificate_probe.py
---

# K2216 Global detector localization and exterior certificate

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
result: K2216 Global detector localization and exterior certificate
carrier: supplied positive scalar Fock detector at exact contrast1/2 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert form and scalar moments ON=declared_carrier
real_structure: real effects and positive outcome squeezes
grading: occupation number; no physical chirality
action_owner: repository-construction -- conditional supplied operator or instrument
target: global minimizer localization and exact exterior test MAP-TYPE=intertwiner
```

## Result and exact inference boundary

Every joint GLOBAL half-contrast minimizer of the supplied detector lies in

    G=(9/10,111/100) x (17/25,91/100), ordered (s1,s0).  (1)

This holds for all cap-feasible infinite profiles, not just the certified
local enclosure C. On the closed rectangle G, a rational tile with center c,
halfwidths h1,h0, and any valid all-tail fixed-squeeze dual D(c) contains no
global minimizer whenever

    D(c)-8 h1²-16 h0² > U,                             (2)

where U is a feasible energy upper bound. This is a stationary GLOBAL MINIMIZER
exclusion, not a lower bound on every profile energy at every point in the tile.

The exact consumer clips the existing complete61-tile dual-input bank to G,
recomputes center duals and the stronger anisotropic correction, and exports
all exclusions and retained tiles in [the report](../../lab/process/k2216-detector-exterior-certificate.json).
The clipped cover has55 tiles:32 are rigorously excluded and23 retained.
Excluded area is2730653/81920000; retained area is1226083/81920000, less
than31 percent of G and less than7 percent of the former square.
These are areas in squeeze-coordinate space, not probability or confidence.
It checks exact cover and disjoint interiors. Retained tiles are unresolved,
not evidence of another minimizer. No complete exterior separation and no
global uniqueness are asserted. The useful next calculation is now confined
to that explicit retained union.

## 1. All-profile moment bounds

Use p_n=(3/4)4^-n, x_n=p_n e_n, y_n=p_n-x_n, 0<=e_n<=1, and
sum(3n-1)x_n=d=1/2. Put w=sum x_n and M_x=sum n x_n. Then

    d=3 M_x-w, M_x<=1/3  => w<=1/2,
    d-2w=sum 3(n-1)x_n <= sum_(n>=2)3(n-1)p_n=1/4
      => w>=1/8.                                     (3)

The negative n=0 term is discarded only in the upper bound. The lower
endpoint is attained by e0=0,e1=1/3,e_n=1 for n>=2. Therefore

    R_x=M_x+w/2=(1+5w)/6 in [13/48,7/12],
    R_y=5/6-R_x=(4-5w)/6 in [1/4,9/16].               (4)

For either branch z, mass a, moment M_z and coherence
T(z)=sum(n+1)sqrt(z_n z_(n+1)), Cauchy gives

    T(z)²<=M_z(M_z+a)=R_z²-a²/4.

Both ratios a/R increase with w in their respective formulas:
6w/(1+5w) and 6(1-w)/(4-5w). Hence

    T_x/R_x<=4sqrt(10)/13, T_y/R_y<=4sqrt(2)/9.         (5)

These are whole-tail inequalities. No probability is fixed in addition to
contrast, and cap-boundary profiles were retained.

## 2. Squeeze localization

The exact energy is A(s1)R_x+A(s0)R_y-(40/3)(s1 T_x+s0 T_y)+35/18,
where A(s)=41s²/6+3/(2s²) and A''=41/3+9/s⁴>0. Each branch has a unique
minimizing positive squeeze solving A'(s)=(40/3)T/R. Nonnegative coherence
forces s>=(9/41)^(1/4)>17/25. Exact squared comparisons using (5) give
s1<111/100 and s0<91/100.

At a joint global minimizer, the inherited K2194 strict-monotonicity theorem
applies. Since sqrt(e_n e_(n+1))>=e_n,

    T_x >= (M_x+w)/2,
    T_x/R_x >= (8w+1)/(10w+2) >= 8/13.

A'(9/10)<(40/3)(8/13), so s1>9/10. This completes (1).
The stricter first lower bound uses optimizer monotonicity; it is not claimed
for all nonoptimal profiles after separate squeeze minimization. Existence
of a global optimizer and monotonicity are inherited, not newly proved here.
The rectangle area is483/10000, versus19321/90000 for the former square
[2/3,113/100]^2: a reduction greater than77 percent before tile exclusion.

## 3. Stationary-minimizer Taylor certificate

For a FIXED profile, the squeeze Hessian has zero mixed entry. Equations (4)
and monotonic decrease of A'' give throughout G

    R_x A''(s1) <= (7/12)A''(9/10)<16,
    R_y A''(s0) <= (9/16)A''(17/25)<32.                (6)

If a global minimizer (xg,sg) were in a tile, its squeeze derivative vanishes.
Taylor expansion for its OWN fixed profile from sg to the center c yields

    D(c)<=E(xg,c)<=Eglobal+8h1²+16h0².

Since Eglobal<=U, (2) is a contradiction. No reduced-value Hessian or global
convexity was assumed. The already-known negative-curvature profiles prevent
that shortcut. A stationary quadratic at a tile corner checks the exact
halfwidth and Taylor1/2 factors in the executable consumer.

The complete clipped cover is a finite union of closed rectangles with
pairwise disjoint interiors, all contained in closed G, and exactly its area.
Those properties certify coverage: any uncovered point in G has a relatively
open positive-area neighborhood because the finite union is closed. Shared
faces remain included. Removing or duplicating a tile fails the check.

## 4. Upgrade criterion and exact remaining seam

Let B be K2210's tiny certified squeeze rectangle. If a complete cover of
G minus int(B), including shared faces, passes (2), every global minimizer
lies in B. K2213's unique B minimizer is then the unique global minimizer over
ALL positive squeezes. This is a precise consuming theorem for the existing
local result, not a declaration that the exterior computation has passed.

With a fixed feasible U, termination requires a strict exterior margin
inf_(G minus int B)V(s)>U. Uniqueness alone supplies a gap above E*, which
may still lie below the supplied U. Alternatively, refine an explicitly
convergent feasible upper sequence for the B optimum together with the
complete rational dual approximations of K2196 and subdivision; IF the global
minimizer is uniquely in int(B), compactness and the positive exterior gap
then give eventual separation. A second global minimum or equality outside B
prevents this strict proof. A finite pilot cannot distinguish those cases.

No broader convex envelope is inferred from the old frozen coordinate boxes.
Such a proof requires fresh profile/tail admission and uniform Schur bounds.
Arbitrary extrapolated profiles can supply dual slopes only after positivity
checks; interpolation accuracy is never assumed.

## Evidence and scientific scope

The new universal moment/localization and Taylor proofs, fresh exact clipped
bank consumption, and inherited existence/monotonicity/uniqueness certificates
are distinct evidence. The consumer hashes the inherited inputs and checks
all tails with the existing exact dual formula; it does not rerun unchanged
boundary or Schur banks. Faults change a genuine tail constant or halfwidth,
or remove coverage. No numerical search result is promoted to proof.

This supplied detector's output-field energy excludes apparatus, preparation
and reset. Source claims, ledger0.263, scalar saturation/inverse and prior
energy brackets retain their scope. No GU physics, novelty, proof-assistant
or external-expert claim follows. Global comparison over the retained tiles
and a complete stable apparatus remain separate substantive constructions.
