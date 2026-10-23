---
title: "K1968: Finite exact joint thermal dimension and energy programs"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional independent mathematics; no GU identification, novelty or external certification
scripts:
  - tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py
  - tests/channel-swings/k1968_joint_thermal_finite_dimension_program_probe.py
---

# K1968: Joint dimension and energy constraints reduce to finite exact programs

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
result: complete finite parametric optimization of the joint energy and physical-dimension return infimum
carrier: fixed extreme four-state Schur channel and four-level bath; finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real pinched energy populations
grading: energy resonance components; no source chirality
action_owner: repository-construction -- fixed exact channel
target: arbitrary-spectrum energy-budget optimization at bounded physical dimension MAP-TYPE=intertwiner
```

## 1. Exact problem and what is new

Use [K1943](k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md)'s
fixed extreme four-state Schur channel, independent registers, exact additive
conservation, bath energies0,1,2,3 and Gibbs weights proportional to t^b,
0<t<1. Catalyst Hamiltonians are nonnegative, nondegenerate, finite and have
ground0. Let F_d(E) be the infimum of worst-input catalyst MARGINAL half trace
distance among protocols of physical dimension at most d and initial mean
energy at most E. Coherent preparations are allowed. This is not state rank,
product return, repeated-use error, approximate channel or a GU identification.

For every fixed integer d>=3, F_d(E) is EXACTLY a finite minimum of linear
program values, including arbitrary noncommensurate spectra and disconnected
components. For rational t and E the answer is rational and has an executable
exact certificate. As a function of E>=1 it is continuous, nonincreasing and
piecewise affine with finitely many pieces (rational breakpoints for rational
t). It need not be convex. The theorem concerns an infimum: colliding
component levels in a limiting pattern do not prove physical attainment.
No efficient complexity bound or closed formula uniform in d is asserted.

[K1939](k1939-physical-catalyst-resource-frontier-2026-10-22.md) already solved
the two-occupied-energy curve. [K1941](k1941-finite-dimension-catalyst-optimizer-2026-10-22.md)
solved dimension alone by minimum shell completion; translating that completion
was explicitly not an energy optimizer. [K1966](k1966-sharp-thermal-support-size-2026-10-22.md)
solved t=1/2 support/dimension endpoints and their energy threshold. The new
step is finite completeness under BOTH resources, without a guessed energy
cutoff, loss of disconnected protocols or a convexity assumption.

## 2. Compact the full physical spectrum, not just occupied paths

For an actual finite physical spectrum A, join two levels whenever their
difference is1,2 or3. Each connected component has one common fractional
part; translating its minimum to0 yields an integer set A_c with consecutive
gaps in{1,2,3}. If it has k_c levels, its span is at most3(k_c-1). The original
component minimum is a nonnegative offset a_c. Distinct components cannot
share a bath/catalyst energy shell: shared shells require one of those three
differences. This also treats integer-lattice components separated by a gap
of at least4. Completely unoccupied components can be omitted for an
at-most-dimension problem.

There are only finitely many possible translated shapes with sum k_c<=d:
for each k_c there are exactly3^(k_c-1) gap words. Keep components TAGGED even
when their translated numerical levels coincide. In each shape choose an
occupied subset S_c. It is admissible precisely when, on every shell e,

    k_e=#{a in A_c: e-a in{0,1,2,3}},
    n_e=#{s in S_c: e-s in{0,1,2,3}},
    2 n_e <= k_e.                                      (1)

K1941 proves necessity and full-shell sufficiency. In particular occupied
paths obey adjacent gap sums>=4; inadmissible triples are never admitted.
Every occupied level is at least1 in a translated shape: at level0 its
bath-ground shell would have only one physical position. Summing rank bounds
with the lowest-shell strictness gives total support<=floor((d-1)/2).
No physical energies are discarded just because their preparation weight is0.

The canonical pattern uses the positions e in S_c as its energy coefficients.
Its mean energy is no greater than the actual mean, since each a_c>=0.
Return and shell construction are translation-invariant within a component.
Covariant pinching from K1933 preserves energy and dimension while producing
a feasible diagonal comparison with no larger return. Thus every actual,
possibly coherent protocol maps to a feasible canonical pattern with no
larger energy and a certified lower bound on its return.

## 3. Exact linear programs for each pattern

For an edge from i to j at distance g in{1,2,3} within one tag, set

    L_g=(sum_(b=0)^(3-g) t^b)/(sum_(b=0)^3 t^b), H_g=t^g L_g,
    x=H_g p_i, y=L_g p_j.

Add(y-x)_+ to I_i and(x-y)_+ to I_j. Other tags never interact. K1943's sharp
all-input return, attained by actual shell unitaries for a diagonal preparation,
is

    R(p)= (1/2) sum_i (p_i-I_i)_+.                       (2)

Enumerate the two signs of x-y on every edge. On each closed orientation
cell the I_i are linear, with the chosen sign inequalities imposed. Add
variables z_i>=0, z_i>=p_i-I_i, p_i>=0, and

    sum p_i=1, sum e_i p_i<=E; minimize (1/2)sum z_i.    (3)

Zero p_i are permitted. They only reduce actual support; the declared
completion remains adequate. Every orientation is included, with ties covered
by both cells. Empty cells require exact infeasibility evidence. Minimize(3)
over ALL finite patterns with sum|A_c|<=d and all orientations. Call the
result V_d(E). The preceding physical reduction proves F_d(E)>=V_d(E).

This formulation is finite for every d. It is not a finite sample of spectra
or a restricted rooted-family bound. The executable small-d reference uses
an equivalent exact vertex arrangement: split each orientation further by
the signs of p_i-I_i. Within each compact probability polytope both E and R
are affine. Its projected lower faces connect projected vertices, so rational
vertex enumeration plus a finite lower envelope gives the ENTIRE budget
curve. Taking a single convex hull across different cells would be invalid.

## 4. Physical recovery at the SAME dimension and exact energy budget

A canonical tagged optimum might repeat a numerical physical level between
tags. It is not silently interpreted as a degenerate physical catalyst.
Shift a tag containing a minimum occupied site by0 and the others by distinct sufficiently small positive
fractions, avoiding the finite set of integral differences. All physical
levels become distinct; all internal shell multiplicities stay unchanged;
no new intertag shell appears; the dimension is unchanged and ground0 remains.
The mean energy rises by a quantity tending to0.

If the canonical preparation already has strict energy slack, choose shifts
inside that slack. If its mean equals E and its smallest positively occupied
level e_min is less than E, move a vanishing amount of population to that
SAME already occupied site after shifting. For small enough shifts its actual
energy is still less than E; interpolation reaches mean E exactly: transfer delta=(e_shift-E)/(e_shift-e_min) to that site.
The denominator stays positive and delta tends to0. No new
level, support, pure flag or extra dimension is added. Formula(2) is a
continuous piecewise-linear function of p. The repaired return therefore
converges to the canonical optimum, and K1943 supplies a physical conserving
unitary for each repaired preparation.

The remaining case e_min=E forces all positive canonical populations to have
the same numerical energy. There is then at most one occupied site in each
tag and no occupied resonance edge, so R=1/2. The single physical shape
{0,1,2} with occupied level1 attains1/2 at every E>=1. Thus it supplies that
boundary value directly. These alternatives prove

    F_d(E)=V_d(E), d>=3,E>=1.                            (4)

For E<1 no protocol exists. Padding an actual witness by remote empty levels
also handles exactly d in place of at-most d, without changing energy or
return. The proof of(4) establishes an infimum when shifts are needed; it
does not assert an optimum exists in the nondegenerate-spectrum class.

## 5. Released global consequences

For a fixed pattern, the feasible probability simplex is compact and R(p)
is continuous. Its minimum under an energy budget is nonincreasing and
continuous for E>=min S: at an interior budget move a vanishing amount of
mass to a minimum-energy site to approximate from below, while compactness
gives the opposite semicontinuity. At the boundary E=min S, every occupied
tag has just one numerical energy and R=1/2. This argument works across
orientation changes; one must NOT assert each orientation becomes feasible
at min S. Those individual cells can have higher minimum energy.

The finitely many polyhedral cells prove piecewise affinity. Every newly
feasible pattern enters at return1/2, already supplied by the singleton.
Their finite minimum is therefore continuous on[1,infinity). Rational data
give rational vertices, affine pieces and crossing points. An optimal basis,
primal/dual pair or complete vertex representation certifies any rational
query; this is decidability by finite exact arithmetic, not polynomial time.

Convexity need not survive a dimension cap. K1939's existing d=5 case has
F_5(6/5)=9/20, F_5(11/5)=3/10, but F_5(3/2)=9/20, strictly above their
linear interpolation. K1960's unrestricted-dimension convexification is
consistent: block mixing needs more physical levels. A budgeted-dimension
program must count each shifted component's physical completion separately.
For t=1/2 and N=floor((d-1)/2)>=7, K1966 supplies the exact eventual plateau
F_d(E)=R_N iff E>=E_N. Formula(4) determines the previously open INTERIOR
by a finite computation, without claiming a simple closed expression for it.

## 6. Complete small-d curves and a genuinely unattained fixed-dimension infimum

The exact enumeration completes F_d for EVERY E>=1 for d=3,...,8 at t=1/2.
For d3/4 it is1/2. For d5/6 it recovers K1939. The new d7 and d8 curves
are below; each row applies until the next endpoint, with the last row
continuing forever. Adjacent formulas agree exactly at every breakpoint.

|d|energy interval|F_d(E)|
|---|---|---|
|7|[1,6/5]|3/4-E/4|
|7|[6/5,113/91]|45/76-9E/76|
|7|[113/91,409/273]|81/182|
|7|[409/273,18/11]|49/100-3E/100|
|7|[18/11,11/5]|17/20-E/4|
|7|[11/5,19/8]|15/28-3E/28|
|7|[19/8,317/104]|9/32|
|7|[317/104,67/19]|79/140-13E/140|
|7|[67/19,infinity)|9/38|
|8|[1,6/5]|3/4-E/4|
|8|[6/5,113/91]|45/76-9E/76|
|8|[113/91,121/91]|81/182|
|8|[121/91,11/5]|2/3-E/6|
|8|[11/5,infinity)|same as d7|

One consequence cannot be inferred from the old support-only optimum:

    F_8(3/2)=5/12, and NO physical protocol attains it.  (5)

The independent complete single-component check gives a strict value above
5/12 at that budget. Two populated physical components must cost at least3
levels each; the only nontrivial d8 split is a singleton dimension3 plus a
two-occupied-level dimension5 component. Its pair has gap2. The canonical
return-energy lower envelope contains the line2/3-E/6, obtained by mixing
the singleton endpoint(1,1/2) with the pair endpoint(11/5,3/10).
The independent check solves both actual tagged orientation programs, as well
as every single-component competitor. The line is NOT a global lower bound on
the pair curve: its low-root vertex(6/5,9/20) lies below it. An attempted global
secant assertion failed this exact control and was withdrawn before acceptance.
One cannot mix the low-root and high-root pair preparations as separate tags
without spending ten physical levels. The full tagged programs, not an assumed
convex hull or global secant, certify the stated eight-level answer.

If both components have positive weight in a nondegenerate actual spectrum,
their normalized shapes cannot both start at0: they would share physical
levels0,1,2. At least one has strictly positive offset. Translating each
component down therefore strictly reduces mean energy. Since the canonical
F_8(E) is strictly decreasing just below3/2, an actual protocol at E<=3/2
has return strictly above5/12. Zero mass on either component reduces to the
already excluded single-component case. Pinching transfers this exclusion
to coherent initial preparations too.

An explicit approaching sequence keeps EXACTLY eight physical levels:

    A={0,1,2} union {epsilon,1+epsilon,...,4+epsilon},
    S={1,1+epsilon,3+epsilon},
    w=(1/2)/(6/5+epsilon),
    p=(1-w,2w/5,3w/5), 0<epsilon<1.

Choose nonintegral epsilon. The mean is exactly3/2, and the all-input return
is1/2-w/5>5/12, tending to5/12. These are actual finite conserving full-channel
unitaries by the shell construction; two explicit rational epsilons are
checked. K1943 already exhibited this family as an improvement. Here the
complete joint lower bound proves its optimal infimum and nonattainment,
which were not established by the earlier upper construction.

## 7. Exact executable evidence and hostile review

The producer enumerates physical shapes and complete orientation/deficit
cells, uses exact rational vertices and projects their energy-return segments.
Safe pruning compares the SAME relative occupied spectrum: a no-larger
physical completion at no-higher offset dominates without changing return or
interacting with another tag. The independent probe instead enumerates
coordinate subsets, reconstructs shell multiplicities, and certifies fixed
budgets with independently assembled rational primal/dual or Farkas data.
Full complex shell unitaries verify physical attainments. Finite cases check
the implementation; sections2-5 carry the all-d quantifier.

The producer covers3,276 physical shapes and the complete small-d frontier
in the companion JSON. The independent probe passes38,088 exact LP/census
obligations and1,494 physical shell controls, with five mathematical-input
faults rejected. No external expert or proof-assistant certification is claimed.
The strongest overclaim attempts are a convex hull across cells, identifying
occupied support with matrix rank, dropping unoccupied physical positions,
merging translated tags into degeneracy, or repairing energy by adding an
unbudgeted singleton component. The construction above avoids each effect.

[Ng et al.](https://arxiv.org/abs/1405.3039) establish prior dimension/energy
constraints in thermal catalysis; its abstract was rechecked, and no novelty
claim is made. This is an imported positive finite quantum model.
SC-META-53 remains UNCERTAIN and LT-SM8/LT-GR6b/AC-F1 remain NEEDS.
No source, physics-ledger, canon or public GU verdict changes.
