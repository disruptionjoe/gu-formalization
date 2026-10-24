---
title: "K2015: Complete cutoff-nine return-cone separation"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2015_finite_thermal_ray_separation.py
  - tests/channel-swings/k2015_finite_thermal_ray_separation_probe.py
---

# K2015: Complete cutoff-nine return-cone separation

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
result: complete exact low-energy cone vertices and directional surplus certificates
carrier: exact extreme four-state channel and nondegenerate finite or countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance with upper mean-energy budget ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real diagonal populations
grading: bath resonance components, not source chirality
action_owner: repository-construction -- unchanged K2008 thermal class
target: explicit global spacing window and resource stability MAP-TYPE=intertwiner
```

## 1. Decision and scope

The previous ten-level theorem, K2014, supplied no numerical regime. This
census supplies the quantitative separation needed to evaluate one, without
enumerating every physical spectrum with 25 levels. It is an exact finite
polyhedral computation on occupied supports through energy nine, at bath
ratio t=1/2. The unrestricted conclusion is separately proved in
[K2016](k2016-explicit-unrestricted-thermal-window-2026-10-24.md).

Reuse the precise channel, nondegenerate spectrum, faithful four-level bath,
independent registers, exact conservation and marginal return of
[K1943](k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md).
Coherent preparations are covered only through its covariant pinching
reduction; the formula below is the sharp diagonal return, not an assertion
about the return of every prescribed coherent state/unitary.

For a normalized canonical component let e be its mean, R its return and

    z = R + (3/20)e - 63/100.

K1950 proves z>=0 globally and its two equality preparations are
A=(9/10,1/10) and B=(2/5,3/5), both on occupied support {1,3}, with means
6/5 and 11/5. Those results are reused, not newly inferred from samples.
The new complete finite census gives:

| Quantity | Exact result |
| --- | --- |
| Canonical occupied supports through 9 | 26 |
| Edge-orientation cells | 183 |
| Active hyperplane bases examined | 37,666 |
| Normalized vertex records, with shared-boundary duplicates across cells | 3,137 |
| Minimum strictly positive vertex surplus | 9/7700 |
| Minimum z/(e-6/5) over non-equality vertices with e>6/5 | 81/12940 |
| Minimum z/(11/5-e) over non-equality vertices with e<11/5 | 9/7540 |

The last two numbers are more useful than a generic determinant-height bound:
they retain the distance from the two equality energies. This replaces an
unexecuted general threshold algorithm by explicit rational certificates.

## 2. Complete support and cone enumeration

The inherited shell-rank theorem makes every connected occupied support an
increasing path with gaps in {1,2,3} and adjacent gap sums at least four.
Its least allowed occupied offset is max(1,3-first_gap), or one for a
singleton. Canonical supports through nine have at most five occupied sites.
Every physical low-energy component translates down to one of these supports;
its residual offset is nonnegative. Zero population coordinates are retained.
They may split the effective occupied graph; omitting them would miss faces.

At t=1/2 the integer lower/upper edge coefficients, divided by 15, are

    gap d:       1    2    3
    L numerator:14   12    8
    H numerator: 7    3    1.

Fix the winner sign on every edge. Its incoming excess vector I is linear.
The sharp return is R(p)=sum_i max(p_i-I_i,0)/2. Refine the orientation cone
by the deficit hyperplanes p_i-I_i=0. On each resulting homogeneous cone,
R and mean are linear. Intersect with sum p_i=1 and p_i>=0.

Every vertex of every normalized refined cone has n-1 independent active
homogeneous hyperplanes selected from coordinate zeros, edge ties and
deficit zeros. The producer enumerates ALL such subsets, computes their
integer cofactor null vectors, normalizes by the sum, and retains vectors
satisfying nonnegativity and the edge inequalities. The deficit signs need
not be guessed: each retained point belongs to a sign region, while every
actual region vertex is encountered. Extra boundary representations only
duplicate vertices; they do not alter extrema. Singular bases or zero
normalizing sums yield no normalized vertex.

This is a completeness argument plus exhaustive exact execution, not random
sampling, a floating optimizer success flag, or a fixed collection of example
protocols. Integer determinant arithmetic and rational comparisons decide
all candidate coordinates and inequalities. Every refined normalized cone
is a compact polytope; its points are convex combinations of these vertices.
The list covers occupied-support cones, NOT all 25-level physical spectra.

## 3. Directional certificates and consumers

Put c_A=81/12940 and c_B=9/7540. Every enumerated vertex other than B obeys

    z >= c_A(e-6/5),                                    (1)

and every vertex other than A obeys

    z >= c_B(11/5-e).                                   (2)

Vertices on the other side of the relevant energy endpoint have nonpositive
right-hand side, so the inequality follows from z>=0. The remaining equality
type satisfies its relevant inequality at zero. For all positive-surplus
vertices the stated exact ratios prove (1)-(2).

The c_A witness is support {1,3,6}, populations (23/59,69/118,3/118), mean
271/118, return 69/236 and surplus 81/11800. The c_B witness has populations
(69/77,23/231,1/231), mean 94/77, return 69/154 and surplus 9/7700.

On a fixed physical spectrum and one refined cone per occupied component,
lift probabilities to weights on its normalized rays. Normalization and
one upper energy constraint admit an optimal vertex with at most two rays.
Offsets stay fixed and nonnegative during this step, so it is a physically
valid population change, not a free classical flag. If the pair omits B,
summing (1) and using the energy budget gives

    R - B(E) >= c_A(E-6/5),  B(E)=63/100-3E/20,          (3)

because 3/20-c_A>0. If it omits A, (2) gives

    R - B(E) >= c_B(11/5-E).                            (4)

For clarity, with canonical mean e0, offset contribution X>=0 and actual
mean e=e0+X<=E, the identity is
R-B(E)=sum w z+(3/20)(E-e0). In (3) the residual coefficient is
3/20-c_A; in (4) it is 3/20+c_B. Both are nonnegative. Large offsets
therefore cannot evade the certificates. A pair of two non-equality rays
satisfies both; a single ray is included as a zero-weight pair.

A and B cannot occupy one edge-orientation cone: the gap-two quantity
3p_1-12p_3 is positive at A and negative at B. A surviving A/B pair uses
different components. Its actual occupied minima are distinct physical
levels, hence their offsets differ by at least the imposed spacing.
This is the physical distinction needed by K2016; convexifying A and B in
one uncharged component would falsely erase the spacing penalty.

For any low-energy cone decomposition with surplus g=R-B(E), the total
weight beta on non-equality rays satisfies beta<=g/(9/7700). Also
0<=E-e0<=g/(3/20). These are decomposition/energy concentration bounds,
not closeness to a unique unitary or physical spectrum. Keeping actual
component labels is essential; coincident canonical labels are not an
allowed spectral identification.

## 4. Released full compatibility certificate through spacing 4/15

The coarse directional inequalities deliberately forget cone compatibility
and physical offset cost. Retaining them improves the low-support theorem
from 3/380 to the INCLUDED endpoint 4/15, uniformly for 6/5<E<11/5.
The new exact interval program checks all 698 distinct (energy,return) ray
points, all two-component ordered assignments, and all pairs in the SAME
refined cone of one component. Same-cone membership requires no opposite
sign on any deficit row as well as the fixed edge orientation. Different
cells cannot be convexified freely.

A common physical marker justifies offset packing for arbitrary ray types.
If a canonical component's first occupied energy is one, offset+one is an
actual occupied level. If its first energy is two, its first gap is one;
the shell at offset+three contains two occupied bath inputs and requires
all four physical positions offset+{0,1,2,3}. Again offset+one is physical.
Thus different components' canonical offsets differ by at least delta.
Both are nonnegative. Translating the lower to zero and the higher to delta
weakly reduces both means. Replacing physical completion by integer ladders
through the respective last occupied energy plus three remains admissible
and introduces no cross resonance for 0<delta<=1/2. For a single component,
its residual offset can similarly be removed. No dimension restriction is
imposed here, and all physical levels remain charged.

At fixed delta, each two-ray energy/return chord is affine in E on its
feasible interval. The target G is the minimum of two affine functions,
meeting at E_m=17/10+delta/2 with G(E_m)=3/8. A chord can fall below G only
at its own endpoints, at E_m, or at the budget endpoints 6/5 and 11/5.
The latter two are already covered by the global supporting line. For one
ray at e+b delta (b=0 or1), testing against each applicable branch of G and
multiplying by 1+delta or 1-delta gives an affine numerator. For a pair
(e,R,b),(f,S,k), oriented with e+b delta<=E_m<=f+k delta, the chord test is

    R(f+k delta-E_m)+S(E_m-e-b delta)
      -(3/8)(f-e+(k-b)delta) >= 0.                       (5)

This too is affine in delta. Its feasible parameter domain is the intersection
of [0,4/15] with two affine half-lines. Checking both endpoints of that
interval proves the whole interval, including singular coincident-energy
endpoints (individual ray tests cover their actual return). Single-ray
branch-feasibility intervals are handled in the same way.

Complete execution passes 337 single-ray B-branch intervals, 83 A-branch
intervals, 194,017 separated-ray intervals and 4,818 compatible same-cone
intervals. These are exhaustive interval obligations, not samples. The
independent replay derives parameter events geometrically from moving ray
energies and independently reconstructed bath/deficit coefficients; affine
numerators cannot change sign between these events without an endpoint
failure. It agrees on the entire range.

Hence the exact optimum in the class with all occupied energies at most nine
is G throughout 0<delta<=4/15. A seven-level unshifted preparation on
{1,3,5}, with populations (81,9,1)/91, has E=113/91 and R=81/182. Its
return beats G at every 4/15<delta<=1/2. Its actual physical spectrum is
{0,...,6}, so this is a feasible counterexample in that low-support class,
not an incompatible chord. Thus 4/15 is the SHARP uniform onset endpoint for
the low-support class. It is only an upper bound for an unrestricted uniform
onset; K2016 proves the unrestricted interval through 1/15. The seven-level
state is a reused physical object, while its exact threshold comparison is
the present consuming result. No novelty claim is made.

## 5. Independent implementation and hostile review

The separate checker enumerates supports as subsets of {1,...,9}, reconstructs
retention coefficients by coincident bath labels, and solves active bases
with rational Gaussian elimination. It does not import the producer's gap-word
generator, incoming-excess matrices, determinant routine or return function.
It reproduces all 3,137 vertex records and the three exact margins. Four
fault controls comprise one omitted-cell coverage corruption and three
mathematical corruptions (return factor, positive margin, directional slope).
Three dependency hashes are provenance checks, counted separately.

An attempted sharper interpretation was rejected: the c_B extremizing ray
and B do NOT share a return cone. Their actual half mixture has strictly
larger return than the average of their returns. Thus these directional
constants need not locate the sharp physical spacing threshold. K2016 uses
them only as sufficient bounds. The contrary mixture is an executed control,
not a rescue of a failed optimum claim.

Internal checking is same-author separate implementation. No independent
specialist, proof-assistant acceptance or novelty claim is made. No source,
physics-ledger or canon verdict changes. SC-META-53 remains UNCERTAIN and
LT-SM8/LT-GR6b remain NEEDS. This is GU-independent conditional mathematics.

Reproduce from the repository root:

```text
python tests/channel-swings/k2015_finite_thermal_ray_separation.py --write
python tests/channel-swings/k2015_finite_thermal_ray_separation.py
python tests/channel-swings/k2015_finite_thermal_ray_separation_probe.py
```
