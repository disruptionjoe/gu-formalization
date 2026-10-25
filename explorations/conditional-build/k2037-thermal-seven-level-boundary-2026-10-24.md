---
title: "K2037: Three unrestricted thermal phases from short exact certificates"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact independent thermal mathematics; subsequent phase and countable optimum remain open
scripts:
  - tests/channel-swings/k2037_thermal_seven_level_boundary.py
  - tests/channel-swings/k2037_thermal_seven_level_boundary_probe.py
---

# K2037: Three unrestricted thermal phases from short exact certificates

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
result: three global thermal phases, sharp dimensions and a failed convex interpolation
carrier: four-state bath times finite/countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex physical states with real nonnegative diagonal populations
grading: bath shells and resonance components, not fermionic grading
action_owner: repository-construction -- inherited energy-conserving shell channel
target: exact return frontier and physical resource count MAP-TYPE=intertwiner
```

## 1. Three complete phases, for every positive spacing through one

[Verified conditional mathematics.] In the unchanged bath with energies0,1,2,3
and populations(8,4,2,1)/15, these are the unrestricted finite/countable optima
for **every0<delta<=1**:

| Budget interval | F(E) | Minimum physical levels in the strict interior |
|---|---|---|
| [11/5,19/8] | 3(5-E)/28 | 7 |
| [19/8,349/145] | 9(7-E)/148 | 9 |
| [349/145,1575/653] | 81(9-E)/1912 | 11 |

At the shared boundaries the smaller adjacent optimizer applies:5 levels at
11/5,7 at19/8,9 at349/145, and11 at1575/653. The optimal diagonal is unique
throughout each closed interval, including shared endpoints. This does not
classify coherences, unused empty levels or implementing unitaries.

Unlike the preceding wide-spacing phases, the proof here does not use a
spacing-sensitive component-placement argument. A single global supporting
line for each phase applies to every normalized component. This extends the
seven-level candidate in K2035 to an exact theorem and then settles two
successors. It is independent optimization, not a GU prediction or a claim of
external novelty. Source, physics ledger and canon remain unchanged.

## 2. A short proof transfer replaces a large search

For each (N,A,C)=(5,15/28,3/28),(7,63/148,9/148),
(9,729/1912,81/1912), exact finite enumeration proves

    R(p)+C e(p)>=A m(p)                              (1)

for all canonical connected supports through integer energy N. Here m is
unnormalized mass. All admissible gap words have gaps1,2,3 with adjacent gaps
summing at least4. Their minimal starting point is max(1,3-first_gap), and
an isolated input starts at1. The shell-capacity theorem supplies this
canonical class; arbitrary translations only increase energy.

For each edge orientation the return is a sum of clipped affine deficits.
Enumerate every coordinate, edge-sign and deficit hyperplane intersection
on sum p=1,p>=0, retaining exactly the orientation-compatible vertices.
A linear inequality on every arrangement vertex holds on every cell.
The complete banks have15,55 and183 orientation cells at N=5,7,9. No floating
optimizer or inferred dimension cutoff establishes this inequality.

Now erase every occupied canonical level above N. K2020 proves that this
cannot increase the unnormalized return, including countable supports by
its l1 argument. If q is erased mass and h its energy, h>=(N+1)q, so(1) gives

    R>=A-C e+C(h-(N+1)q)+kappa q,
    kappa=C(N+1)-A=C>0.                             (2)

This proves the supporting line at every mean, not only inside the attained
phase. For any collection of occupied components with offsets d_i>=0,
write e for their total actual physical mean and E>=e for the budget.
Homogeneity and summation give

    R>=A-C E+C(E-e)+C sum_i m_i d_i
       +C sum_i[h_i-(N+1)q_i]+kappa sum_i q_i.       (3)

The canonical support reduction applies componentwise; multiple components
inside one integer physical ladder are allowed. Offsets are measured from
the common nonnegative physical ground. At most one occupied component can
have zero offset; every other component pays a strictly positive translation
cost. Countable components follow by nonnegative summation and finite energy.
No upper bound on dimension or intercomponent separation is assumed.

Thus equality has saturated energy, no tail, no translation and only one
occupied component. Equation(3) also controls near-optimal tail mass and
offset-weighted population. It is this positive tail coefficient that makes
the short finite proof global. Erasing and then normalizing without its mass
factor would be invalid.

## 3. Equality, attainment and sharp resources

The complete equality vertex sets each contain only their two adjacent
endpoint diagonals. In order they are

    e=11/5:       (p1,p3)=(2/5,3/5),
    e=19/8:       (p1,p3,p5)=(3/8,9/16,1/16),
    e=349/145:    (p1,p3,p5,p7)=(54,81,9,1)/145,
    e=1575/653:   (p1,p3,p5,p7,p9)=(486,729,81,9,1)/1306.

On each interval linearly interpolate its two endpoint populations using
u=(E-e_left)/(e_right-e_left). The independent physical checker verifies a
shared maximizing bath label in every shell and compatible deficit signs
at both endpoints. Those linear inequalities hold throughout the interval,
proving actual attainment, not merely a chord in the lower convex hull.
Conversely, every equality face in every cell is generated by the same two
diagonals; energy fixes the interpolation uniquely.

In an interior optimizer every odd input1,3,...,N is populated. Each adjacent
pair shares two bath shells with two incoming occupied states. The required
four outgoing states force all four physical completion levels in each shell.
Their union is exactly0,...,N+1. Therefore N+2 physical levels are necessary
and the consecutive completion attains them at any delta<=1. Endpoint zero
populations correctly reduce the minimum dimension to the previous value.

## 4. A failed successor and why its failure matters

A fourth exact global supporting line also follows from the cutoff-nine bank:

    R>=1053/2768-(2907/69200)E.                      (4)

Its tail coefficient at erased energy10 is549/13840>0. Its equality vertices
occur at E=1575/653 and E=675/181, the latter with populations
(36,54,81,9,1)/181 on1,3,5,7,9. But the midpoint of these two diagonals has
actual return267057/945544, while(4) gives237735/945544. The gap is
29322/945544>0. These endpoints lie in different return-orientation regions.
A convex chord lower bound is not automatically an attainable phase.
The implementation found and preserved this failure before making a claim.
Further unconstrained convex-hull expansion is therefore not the next proof.

A separate genuine successor family remains useful. On odd inputs1,3,...,
take unnormalized weights1 at1 and(3/2)9^-j at3+2j, j=0,...,m.
Normalize them and complete every physical integer level through the final
input plus1. Exact controls for m=1,...,12 verify physical return p3/2, increasing
mean and decreasing return. The same geometric series gives the countable
completion

    Z=43/16,    mean=415/172,    R=12/43.

The geometric tail makes the l1 return passage legitimate. These are feasible
upper constructions; no global optimality or sharp countable-dimension claim
is inferred. The countable return lies21/2380480 above the global supporting
line(4) at its mean, so a real gap in current bounds remains.

## 5. Verification and continuation

The primary exact cofactor census is replayed by a separate bath-label
construction and rational nullspace enumeration. Both check complete
orientation coverage, every vertex, the two equality diagonals per phase,
physical shell feasibility and whole-interval interpolation. Actual controls
change normalization, completion and supporting intercept; return corruption
and the strict tail-gap requirement are checked separately. Inherited
shell-capacity and zero-loss-erasure theorems are reused by pinned evidence.
Internal separate implementations are not external review or proof-assistant
certification.

The next thermal question is the actual frontier above1575/653: minimize the
nonconvex return cells or find an appropriate component construction instead
of treating(4)'s long chord as an optimum. The finite/countable tail family
and its explicit residual gap are useful controls. Near5/4 accumulation,
earlier21-phase edges and exact capped continuum marginals remain separate
research options.
