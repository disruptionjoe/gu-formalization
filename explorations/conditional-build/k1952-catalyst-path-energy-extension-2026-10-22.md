---
title: "K1952: Collapsed-tail certificates extend the sharp catalyst energy frontier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional mathematics; no native GU identification, novelty, expert acceptance or formal proof
scripts:
  - tests/channel-swings/k1952_catalyst_path_energy_extension.py
  - tests/channel-swings/k1952_catalyst_path_energy_extension_probe.py
---

# K1952: A finite tail relaxation with exact global consumers

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: finite collapsed-tail global duals, three new sharp energy segments and finite nonattainment
carrier: fixed extreme four-state Schur channel, faithful four-level bath and finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex shell unitaries; rational energy-diagonal optimization after pinching
grading: additive energy shells, not physical chirality
action_owner: repository-construction -- exactly conserving conditional channel protocol
target: unrestricted catalyst mean-energy return infimum MAP-TYPE=intertwiner
```

## 1. Result and unchanged model

[K1950](k1950-global-catalyst-energy-certificates-2026-10-22.md) established
the global return infimum through mean energy19/8. The next three segments,
at the same bath parameter t=1/2, are exactly:

| Energy interval | Rstar(E) | Attainment |
|---|---|---|
|[19/8,349/145]|63/148-(9/148)E|finite throughout|
|[349/145,1575/653]|729/1912-(81/1912)E|finite throughout|
|[1575/653,675/181]|1053/2768-(2907/69200)E|finite endpoints; strict interior not attained|

Thus the evaluated frontier now reaches675/181, approximately3.7293.
The new junctions are genuine: direct interpolation from the old19/8
endpoint to the previously known higher-energy witnesses misses them.

Assumptions remain exact full-channel simulation for all inputs, faithful
bath energies0,1,2,3 with Gibbs weights t^b/Z, independent initial registers,
nonnegative finite nondegenerate catalyst spectrum with ground0, mean initial
energy at most E, and worst-input catalyst **marginal** half trace distance.
Coherent preparations are included in the lower bound by the covariant
pinching argument of K1943. This is not product return, repeatability,
approximate-channel simulation, degenerate catalysts or a general
thermodynamic law. Source, physics-ledger and canon verdicts do not change.
SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b and AC-F1 remain NEEDS.

## 2. Collapse the omitted population, not the proof obligation

Reuse K1943's shell theorem and path classification. A connected canonical
occupied support has successive gaps d in{1,2,3}, adjacent gap sums at least4,
and initial energy `max(1,3-first_gap)`; singleton energy1. Its homogeneous
optimal return is

    R(p)=1/2 sum_i (p_i-I_i)_+,
    I_low+=(L_d p_high-H_d p_low)_+,
    I_high+=(H_d p_low-L_d p_high)_+,
    L_d=(1+...+t^(3-d))/Z, H_d=t^d L_d.                   (1)

These reused theorems provide the bridge from arbitrary spectra and exact
channels to paths. Equal dimensions or a linear program alone would not.

Fix a cutoff K and keep each component's prefix through the FIRST vertex
h above K. Replace all population from h onward by its total delta at h.
Keep the ordinary incoming-excess formula on every retained low vertex,
but omit the return deficit at h entirely. Denote that relaxed return by T.
Then, for every original component,

    T <= R(p),
    sum_(i<h) s_i p_i+s_h delta <= sum_i s_i p_i.         (2)

Proof: only the last low site can receive an edge from the removed suffix.
Replacing its adjacent high population by the larger delta can only increase
its incoming excess, hence can only decrease its positive deficit. Every
other low deficit is unchanged. Dropping all high deficits also decreases
the return. Every high energy is at least s_h, proving the second inequality.
No renormalization, dimension-continuity estimate or presumed tail sign is
used. The merged high state is a relaxation, not a physical catalyst.

For each complete canonical path ending at or below K and each canonical
first-crossing prefix, enumerate edge orientations and solve the finite
linear program for `T+lambda energy`, with normalized nonnegative weights.
Crossing cells omit exactly the final deficit inequality and final deficit
cost. Their final population is delta. The largest coordinate is at most K+3.
If every such program has value at least a, (2) proves

    R(p)+lambda E >= a                                  (3)

for arbitrary finite spectra. Disconnected components add homogeneously;
noncanonical fractional offsets only increase the positive energy penalty.
This proves globality directly. It needs neither a physical merged-tail
witness nor the old sufficient condition `lambda K>=a+1/2`.

This remains a finite potentially exponential method. It is an effective
reduction for these certificates, not a general polynomial-time algorithm
or an evaluated all-energy formula.

## 3. Three complete global certificates

|lambda|a|K|Complete and crossing orientation cells|
|---|---|---|---|
|9/148|63/148|10|1471|
|81/1912|729/1912|12|5087|
|2907/69200|1053/2768|12|5087|

All11645 cells have rational primal and dual evidence. Each dual has the
proper sign and exact coefficient domination; its objective equals its
stored primal objective and is at least a. The independent verifier enumerates
integer subsets rather than recursively generated paths and reconstructs
edge coefficients from coincident bath labels. It checks the crossing
boundary as well as the complete paths.

Floating HiGHS discovers active supports. Acceptance reconstructs primal
and dual solutions by exact rational linear systems using active constraints
and zero reduced costs, then checks every inequality. Direct rounding first
produced a tiny negative dual slack and was rejected. This was not accepted
as a tolerance-sized proof error.

K8 was inadequate: its terminal relaxation permits an artificially cheap
geometrically growing tail. Increasing K to10 or12 closed the bound. The
relaxed negative result did not become a physical protocol. For comparison,
K1950's older sufficient cutoff condition would require K16,21,21 for these
three slopes. The new certificate's scope is global despite the smaller K.

## 4. Exact finite protocols on the first two new segments

The four relevant preparations have supports1,3,5,... and weights:

|Name|Weights|Energy|Return|
|---|---|---|---|
|A|(3/8,9/16,1/16)|19/8|9/32|
|B|(54/145,81/145,9/145,1/145)|349/145|81/290|
|C|(243/653,729/1306,81/1306,9/1306,1/1306)|1575/653|729/2612|
|D|(36/181,54/181,81/181,9/181,1/181)|675/181|81/362|

Append zeros to the shorter support and linearly interpolate A to B, or B
to C. The edge orientations and deficit signs are compatible at both ends;
their linear inequalities remain valid throughout. Substitution into(1)
therefore gives the respective line in the result table. These upper bounds
match(3), establishing the exact frontier.

The producer constructs complete complex shell unitaries on the actual
physical ladders0,...,10 and0,...,12. It checks all four channel vectors,
all their Gram entries, unitarity, marginals and mean energies at endpoints
and rational interior values. The interval proof is the affine sign-cell
argument; a few samples alone would not prove it.

## 5. The long connecting segment is an unattained infimum

For the third certificate, every cell attaining a has a uniquely fixed
population. This is proved by exact equality-face linear algebra: constraints
with strictly signed dual multipliers and variables with positive reduced
cost, together with normalization, determine EVERY population coordinate.
The complete census leaves only C and D. In every optimal crossing cell the
merged population delta is zero.

Consequently an actual equality protocol has no population beyond K, and
no component can have a positive upward offset: either would contradict
the equality constraints or add strictly positive lambda times energy.
Every equality component is therefore precisely C or D at canonical
energies1,3,5,7,9. Two distinct resonance components cannot both occupy
those same energies in a nondegenerate catalyst. Thus equality occurs only
at their two endpoint energies, never at a strict interior budget.
Pinching a coherent hypothetical attaining protocol would yield an attaining
diagonal one at the same energy, which has just been excluded.

Nevertheless the infimum is exact. For an interior energy E, take weight
w=(E_D-E)/(E_D-E_C) of C and1-w of D, shift their spectra upward by epsilon
and2epsilon, and mix with the unshifted energy1 singleton using

    scale=(E-1)/(E-1+(2-w)epsilon).

The distinct fractional offsets prevent cross-component resonances and
physical degeneracy. The resulting finite protocol has exactly energy E and
return `scale*Rstar(E)+(1-scale)/2`, strictly above the line and converging
to it. Full physical shell matrices are checked at E=3 for two rational
positive epsilons. This is a family of actual finite approximations, not an
unpriced classical label or an inadmissible degenerate equality example.

## 6. Resource consumers, prior work and limits

On either of the first two new segments, inversion gives the attained
minimum energy `(a-r)/lambda` for return budget r in its image. On the
third segment, the same expression is the infimum required energy; at strict
interior return budgets it is not attained. A slightly larger energy budget
permits a sufficiently small positive epsilon in the explicit construction.
Endpoint attainment is preserved. These conclusions concern the fixed
channel model and marginal return only.

The closest general context remains Ng et al.,
[Limits to catalysis in quantum thermodynamics](https://arxiv.org/abs/1405.3039),
which studies catalyst return limitations under dimension and mean-energy
constraints. Its general subject is prior work; no novelty claim is made
for the present target-specific rational certificates. K1943/K1950 supply
the exact channel/path bridge used here.

Use Sage Python on the producer and probe. Default producer execution replays
the stored certificates; `--discover --write` rebuilds them from active-set
search. The independent baseline precedes missing-prefix, dual, population
and terminal-energy faults; reporting identity/pin checks are separate.
The finite exact tests certify the stored algebra. The arguments(1)--(3)
and equality/physicalization reasoning establish the arbitrary-spectrum
conclusions. This is internal verification, not external expert acceptance
or formal proof-assistant certification.

Beyond675/181, the global finite-certificate method still applies, but no
closed frontier is claimed. A changed active path or thermal parameter
requires new exact certificates. General efficient path optimization,
degenerate-spectrum resource costs, approximate-channel tradeoffs and the
independent scalar pulse/cut match remain separate mathematical questions.
