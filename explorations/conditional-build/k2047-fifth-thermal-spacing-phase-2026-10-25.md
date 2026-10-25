---
title: "K2047: Two final interlaced thermal phases and a critical resource collapse"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unrestricted finite/countable thermal model for the stated energy interval and spacing at most one half; wider spacing remains open
scripts:
  - tests/channel-swings/k2047_fifth_thermal_spacing_phase.py
  - tests/channel-swings/k2047_fifth_thermal_spacing_phase_probe.py
---

# K2047: Two final interlaced thermal phases and a critical resource collapse

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
result: fifth and sixth exact thermal phases, sharp internal transition and critical resource laws
carrier: four-state bath and finite/countable pure-point catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex states with nonnegative real populations
grading: exact bath energy shells and occupied components
action_owner: repository-construction -- inherited energy-conserving shell channels
target: exact optimum and physical resource necessity MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The unrestricted thermal optimum on
E in [1575/653,675/181] is now explicit through spacing delta=1/2.
There are two further phases above2/5. Their internal boundary
5652/11755 is a real change of optimizer, certified by a physical rival.
The endpoint1/2 is also a packing boundary for these constructions, but
this does not by itself prove a discontinuity or the next wide-spacing phase.

This result reuses the complete cutoff-eleven arrangement of
[K2045](k2045-third-thermal-spacing-phase-2026-10-25.md), including its
independent enumeration. It does not re-enumerate or claim new completeness
for that unchanged bank. New work comprises whole-interval supporting lines,
actual attainment, equality geometry, resource necessity and the critical
half-spacing follow-through.

## 1. The exact formulas

Keep the four-state bath with energies0,1,2,3 and probabilities(8,4,2,1)/15,
the same exact-shell channel, nonnegative physical catalyst energies with
minimum spacing delta, and mean-energy budget E. Write named pairs as
(energy,return):

    A=(1575/653,729/2612), T=(28361/11755,6561/23510),
    B=(675/181,81/362), U=(3043/815,729/3260),
    C=(19/8,9/32), Q=(37/10,9/40), R=(67/19,9/38).

For P_delta=(EP+delta,RP), let l(P,S;E) denote the straight line through
P,S evaluated at E, and define

    fAT=l(A,T), fTB=l(T,B_delta), fTU=l(T,U_delta),
    fCQ=l(C_delta,Q), fQB=l(Q,B).

Then the exact unrestricted finite/countable optimum is

    F_delta(E)=min(max(fAT,fTB),max(fCQ,fQB)),
                 2/5<=delta<=5652/11755;                 (1)
    F_delta(E)=min(max(fAT,fTU),max(fCQ,fQB)),
                 5652/11755<=delta<=1/2.                (2)

The fAT segment runs from EA to ET. Next the selected left ray, TB or TU,
runs to its unique crossing with CQ. CQ runs from that crossing to EQ;
QB runs from EQ to EB. The exact crossing is obtained by equating the two
line coefficients. Endpoint-cleared inequalities put it strictly between
EC+delta and EQ, and hence to the right of ET. Taking all five lines in one
minimum would incorrectly extrapolate beyond available physical segments.

The new diagonal U has probabilities(324,486,729,81,9,1)/1630 on
occupied levels1,3,5,7,9,11, with required completion0,...,12.
R has(4,6,9)/19 on1,3,5, with completion0,...,6. The earlier A,B,T,C,Q
are exactly K2045's diagonals. U is a vertex already present in that bank;
its role as a globally optimal shifted component is the new result.

## 2. Attainment and whole-domain lower bound

The TB and TU segments use low T and high B or U at offset delta.
CQ uses low Q and shifted C. Their spectra are unions of consecutive integer
completions at offsets0 and delta. For0<delta<=1/2 the union spacing is at
least delta. The components have distinct fractional residues, share no bath
shell, and their population-weighted energies and returns add exactly.
The A/T and Q/B segments are single connected components: common maximizing
bath labels and common deficit signs prove affinity over each full population
segment. Direct endpoint agreement alone would not do so.

For each of the671 orientation cells of the pinned complete arrangement,
choose a valid supporting line from each pair

    (AT,CQ), (AT,QB), (left,CQ), (left,QB).

A valid line supports every vertex of that low cell. Every line also supports
every vertex of every high component after adding delta to its energy, and
lies strictly below zero at canonical energy12. The choices are fixed across
each entire closed spacing interval in(1) or(2). Multiplication by the positive
line denominator makes each tested difference affine in delta; checking both
endpoints proves the whole interval. The saved certificate supplies all cell
assignments. Its20975 vertex values are independently recomputed from actual
bath-label maxima in the new checker.

The forced-ground result of
[K2043](k2043-chamber-offset-frontier-2026-10-25.md) says at most one occupied
component can have original offset less than delta. It includes first-gap1
components whose canonical root is2; their unoccupied ground is physically
forced. That result is reused, not replaced by an assumed occupied minimum.
The actual exceptional component has one orientation cell. Each pair thus
provides a global lower bound by its smaller line. The distributive identity

    max_ij min(L_i,R_j)=min(max_i L_i,max_j R_j)

combines the four bounds into(1) or(2). When no low component is present,
every line is already available. Different parts of one component may not
independently choose incompatible cells.

The inherited unnormalized erasure proof transfers this finite bank to all
finite/countable spectra. Explicitly, for a line f(e)=alpha-s e with s>0,
component mass m, erased mass q above canonical11, erased energy h>=12q,
original offset d and required offset ell in{0,delta},

    R_component >= alpha*m-s*e_actual
        +(12s-alpha+s*ell)*q+s*(h-12q)+s*m*(d-ell).       (3)

All corrections are nonnegative; the first is strictly positive for q>0.
Original offsets are kept and unused budget also adds nonnegative slack.
Finite mean, positive summands and inherited l1 continuity justify the
countable sum. This is the exact transfer that allows a finite certificate to
prove the unrestricted optimum; small tail probability alone is insufficient.

## 3. Sharp internal transition and released optimizer family

At delta*=5652/11755, T, B_delta and U_delta are collinear. For every
sufficiently close larger delta, the actual low-T/high-U construction beats
(1) at E=3, where the competing right branch is strictly higher. The checker
uses delta*+10^-6, evaluates the complete bath channel and verifies the energy
and mixture mass. Cleared affine differences make the immediate direction
rigorous. Thus delta* is a physical phase boundary, not failure of a chosen
cutoff or merely a better coefficient of an unused line.

At the critical spacing, B and U share a return chamber. Every interpolated
B/U diagonal is a legitimate high component, and its shifted chord to low T
lies on the same supporting line. This produces a continuous critical family;
no interpolation of incompatible population chambers is inferred. For positive
U weight that high component uses13 physical levels; at pure B it uses11.
The result describes this family, not all critical optimizing unitaries.

## 4. Strict-spacing equality and minimum resources

Strictly inside each phase, the complete zero-vertex sets are:

- AT: low A,T; no high zero.
- TB: low T and high B.
- TU: low T and high U.
- CQ: low Q and high C.
- QB: low C,Q,B; no high zero.

A component attaining a supporting line must belong to a compatible face
spanned by these zero vertices. Positive tail and offset margins eliminate
tails, surplus shifts and unused budget. Every positive odd population requires
its consecutive completion: shared input shells force all four outgoing
levels. Distinct fractional residues cannot merge the two completions.
The resulting sharp minima are

| Energy region | Fifth phase | Sixth phase |
|---|---:|---:|
| E=EA | 11 | 11 |
| EA<E<=ET | 13 | 13 |
| ET<E<left/right crossing | 24 | 26 |
| crossing<=E<EQ | 16 | 16 |
| E=EQ | 9 | 9 |
| EQ<E<=EB | 11 | 11 |

At the crossing both constructions attain and sixteen is smaller. Above EQ,
every QB equality face needs positive B weight because the other zero vertices
have smaller energy, forcing all five odd inputs and eleven physical levels.
These are necessary physical-level counts, not merely sizes of examples.
No statement about all optimal coherent states or channel unitaries follows.

## 5. Half-spacing contact: a smaller optimizer at E=7/2

At delta=1/2 the low point R lies on CQ. R/Q share one return chamber, so their
entire connected segment is feasible and lies on that line. At E=ER, R itself
uses seven levels; from ER to EQ the connected R/Q population uses nine.
These are actual new optimizers at the boundary, not a continuation below it.

There is a further low equality vertex W on support(1,3,5,7,10,11), with
populations(6/17,9/17,1/17,1/68,1/34,1/68), energy95/34 and return39/136.
It cannot simply be added to the R/Q segment: its bath-shell maximizing labels
are incompatible with both R and Q. The exact complete half-CQ equality census
contains only Q,R,W as low vertices and C as high vertex. No cell contains W
with R or Q. The direct checker tests this against all shared shell labels.
W requires fourteen consecutive completion levels0,...,13, but neither W
alone nor W mixed with C_half reaches energy7/2, since both endpoint energies
are below7/2.

At E=7/2 the right line is strictly better than the left and is CQ. Therefore
equality must use a low R/Q face and high C; low R and Q both have energy above
7/2, so the high component has positive mass. A low R/C_half mixture is feasible:
its high-C mass is (ER-7/2)/(ER-EC-1/2), strictly between zero and one.
Each component requires seven levels, and the half-integer residues are
distinct. Fourteen physical levels attain the optimum. Any equality solution
needs at least these two seven-level completions. Thus the minimum at E=7/2
drops from sixteen at strict sixth-phase spacing to FOURTEEN at1/2.
The W check is essential to this necessity argument; ignoring degenerate
critical vertices would have left the lower bound unproved.

## 6. Beyond one half: exact construction failure, open frontier

If two consecutive completions overlap at distinct residues with offset
d in(0,1), their adjacent union gaps include d and1-d. Both cannot exceed1/2.
Thus the offset-delta T/U and Q/C constructions used here cannot continue to
delta>1/2. The checker plants delta501/1000 and rejects the physical spacing.
The same issue affects R/C_half if one merely increases the required spacing.
This is an exact packing obstruction for these realizations. It is NOT proof
that the optimal value jumps, that no different spectrum works, or that the
supporting-line relaxation remains tight above1/2. A new wide-spacing program
must optimize actual relative translations and available completions before
booking a new phase. The known single-component R/Q channels remain feasible
at those wider spacings up to1; their energy domain must still be respected.

## 7. Evidence and limitations

The producer certifies two whole intervals, equality sets and a realizable
transition rival using the unchanged K2045 bank by hash. The separate checker
reconstructs20975 vertex returns from physical bath labels, replays62 physical
mixture/segment controls, four full common-cell segment proofs,41 new completion
removals, the actual boundary rival, two half-cell incompatibilities and the
packing failure above half. Four mathematical/reference faults are rejected
after a clean baseline: fifth-phase overextension, U's return, rival mass and
omitted equality. The finite fixtures are controls; the continuum, countable
and resource statements use the written arguments above. K2045's626412-basis
dual enumeration and K2037/K2043's support/erasure/ground proofs are explicit
reuse, not newly counted work.

The hostile concerns are whole-energy feasibility, original offsets in(3),
confusing cutoff failure with a physical boundary, and critical equality
vertices outside the odd chain. Each is addressed explicitly. Checks are
same-author internal work, not independent specialist, proof-assistant or
novelty acceptance. This is a GU-independent thermal model; source claims,
physics-ledger rows and canon remain unchanged. Next compare a genuine
wide-spacing packing program with near5/4 resource necessity, exact capped
continuum wings and source-faithful dynamical/observation constructions.
