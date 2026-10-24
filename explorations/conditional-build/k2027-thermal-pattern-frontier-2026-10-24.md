---
title: "K2027: All-size connected thermal frontier and sharp17-level dimension"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact connected occupied-component thermal optimum; multiple components, arbitrary bath temperatures and GU identification remain open
scripts:
  - tests/channel-swings/k2027_thermal_pattern_frontier.py
  - tests/channel-swings/k2027_thermal_pattern_frontier_probe.py
---

# K2027: All-size connected thermal frontier and sharp17-level dimension

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: all-size connected thermal frontier, unique optimal diagonal and exact17-level minimum
carrier: inherited four-state thermal bath times finite or countable catalyst with one connected occupied resonance component LAYER=toy CHIRALITY=N/A
pairing: positive bath and catalyst states with upper mean-energy budget ON=declared_bath_catalyst
real_structure: complex physical state space and rational diagonal populations
grading: bath energy labels and catalyst resonance graph, not Clifford grades
action_owner: repository-construction -- exact extreme channel and energy-conserving shell unitaries
target: sharp return, equality and resource bounds on the declared component class MAP-TYPE=intertwiner
```

## 1. The larger class is now solved

Freeze the inherited exact extreme channel, bath energies0,1,2,3 with
probabilities(8,4,2,1)/15, nonnegative nondegenerate catalyst spectrum with
physical ground0, and mean energy at most E. Let the positive diagonal
population have **one connected resonance component**: two occupied levels
are adjacent when their difference is1,2 or3. For every finite or countable
catalyst in this class, every0<delta<=1 and7/5<=E<=8/5, the exact optimum is

    F(E)=(985095-61407 E)/2040416.                       (1)

The same affine diagonal populations from K2025's m=3 family attain (1),
with full physical spectrum0,...,16. Every optimizer in this connected class
has exactly that diagonal population, mean E and canonical offset zero.
**Seventeen physical levels are necessary and sufficient in this class.**
Optional unoccupied levels, coherences and implementing unitaries are not
claimed unique.

[K2025](k2025-wide-spacing-ladder-program-2026-10-24.md) proved only its
explicit geometric-tail family's optimum. This result covers all allowed
connected gap patterns, arbitrary lengths, holed physical completions, and
countable tails. It is still **not the unrestricted frontier with multiple
occupied components**. A physical spectrum may contain extra unoccupied
levels without violating the one-occupied-component assumption.

## 2. Finite exact certificate covering every pattern through20

The inherited [K2015 shell-rank structure](k2015-finite-thermal-ray-separation-2026-10-24.md)
makes a connected occupied support a path. Its gaps are1,2,3, adjacent gap
sums are at least4, and its smallest physical occupied energy is at least
max(1,3-first_gap), or1 for a singleton. Translating to that canonical offset
leaves return unchanged and reduces mean. No consecutive physical completion
is assumed for this lower bound; all physically feasible holed completions
are included in this support relaxation.

Enumerate every such canonical support with maximum energy at most20, every
edge orientation, and every nonnegative population, including zero-population
faces. Supports with first energy2 cannot have mean at most8/5 and are
excluded by that exact inequality. There are163329 remaining orientation
cells. Zero faces are essential even when they disconnect a labeled support;
retaining them enlarges the lower-bound class safely.

For a fixed orientation, let I(p) be incoming excess, with edge coefficients

    gap d                 1      2      3
    earlier coefficient   7/15   3/15   1/15
    later coefficient    14/15  12/15   8/15.

The exact sharp diagonal return is R(p)=sum (p_i-I_i(p))_+/2. Introduce
z_i>=0 and z_i>=(p_i-I_i(p))/2. Together with the orientation inequalities,
p>=0, sum p=1, and the energy interval, this is a linear program with
objective sum z_i. No deficit-sign subdivision or vertex omission occurs.

Write a=985095/2040416, c=61407/2040416, l=7/5, u=8/5 and b=1/41. The two
certified inequalities on every cell are

    R+b e >= F(l)+b l       when e<=l,
    R+c e >= a             when l<=e<=u.                (2)

Infeasible sections instead carry an exact minimum-energy or maximum-energy
dual certificate. These are326658 exact rational certificates, two per cell.
Each feasible dual has nonpositive inequality multipliers, a free normalization
multiplier, and nonnegative reduced costs. Multiplying by any feasible primal
vector proves its recorded lower bound. All denominators are cleared and the
acceptance checks use integer arithmetic. A numerical optimizer proposed the
duals; exact feasibility and lower-bound checks alone admit them.

The machine-readable report stores the complete ordered certificate bank as
base85(zlib(UTF-8 JSON)). Its hash checks transport, while the actual dual
inequalities establish the proof. The producer replays the bank without any
optimizer. The separate checker derives deficits from bath-label shell
maximizers and uses its own gap-word enumeration. Both verify every cell and
section, not a sample. Compression changes neither the coverage nor the proof.

## 3. Why the finite certificate controls all lengths

Extend the lower bound to1<=x<=u by

    G(x)=F(l)+b(l-x) for x<=l,
         F(x)       for l<=x<=u.                       (3)

It is continuous and decreasing, with slope magnitudes b and c, and c>b>0.
The initial attempt with b=1/37 was false. The actual physical population
(729,81,9,1)/820 on occupied energies1,3,5,7 and full spectrum0,...,8 has
mean256/205 and return729/1640, below that stronger backward line. It is
retained in the report as a failed proof-transfer witness. The weaker b=1/41
passes the complete bank through20.

[K2020](k2020-posttransition-tail-and-resources-2026-10-24.md) proves that
upper-tail erasure cannot increase **unnormalized** sharp return, uniformly
for faithful baths. Its local terminal formula and countable l1 limit apply
unchanged here. For an arbitrary connected catalyst let e<=E be its mean,
q its diagonal mass at actual energies above20, and h that tail's energy.
The retained normalized mean x=(e-h)/(1-q) lies in[1,E]; q<1. The retained
prefix is still a connected path. Any remaining canonical translation only
lowers its energy, so (2),(3) apply even with a nonzero original offset.
Homogeneity, erasure, and G's slope floor give

    R_original >= (1-q) G(x)
               >= F(E)+b(E-e)+b(h-20q)+kappa(E)q,
    kappa(E)=(20-E)/41-F(E)
            >=2719011/209142640 >0.                    (4)

The first inequality also uses the inherited coherent-to-diagonal lower
bound when the original catalyst has coherence. Countable tails are handled
by finite truncation followed by the established l1 continuity of the sharp
return; no highest occupied vertex is assumed. The finite certificate thus
proves (1) in the entire declared finite/countable connected class.

For an epsilon-optimal protocol, with kappa0=2719011/209142640,

    q<=epsilon/kappa0,
    h<=(20/kappa0+41)epsilon,
    E-e<=41 epsilon.                                   (5)

These are unconditional tail and energy-slack bounds for this class. At exact
optimality the tail vanishes and the mean saturates E. Strict monotonicity also
forces the canonical translation to zero. No global dimension bound for
near-optimizers follows merely from their small tail mass.

## 4. Attainment, equality and minimum physical dimension

Use the m=3 populations in K2025 equations(3),(4), on occupied energies
1,3,5,7,9,11,13,15. The report gives exact endpoint populations at7/5 and8/5
and the midpoint control. Linear interpolation preserves every shell
maximizer and deficit sign. Thus the population, mean and sharp return are
affine on the entire interval and attain (1). The full integer spectrum0,...,16
satisfies every shell-capacity inequality and has spacing1, so it works for
every0<delta<=1. This is a physically feasible shell-unitary construction,
not a diagonal relaxation substituted for exact channel realization.

Only11 orientation-cell duals can have equality in the second bound of(2).
Complementary slackness sets variables with positive reduced costs to zero
and makes inequalities with negative dual multipliers tight. Append
normalization and the exact mean E. For every one of these11 systems, the
rational row space implies the same affine population at every support energy;
all other energies have population zero. A separate right-kernel calculation
checks those implications, including endpoint degeneracies. Combined with
(4), this classifies every optimal diagonal in the full connected class.

All eight listed populations are positive throughout the closed interval.
Every overlap shell receiving two occupied bath inputs requires four physical
catalyst levels. The union of the four candidates in those overlap shells is
exactly{0,...,16}. Hence each of those17 physical levels is compulsory, and
the displayed spectrum attains the bound. This establishes a minimum dimension
here without inferring it from a sufficient witness size. It says nothing
about a lower-dimensional optimum using several occupied components.

## 5. Hostile review, reproducibility and next uncertainty

Strongest overclaim: (1) solves all spectra. The connected occupied-component
condition is load-bearing; mixing several resonant components changes placement
and energy costs and has not been certified. Strongest contrary attempt: the
first backward tail line failed on an actual physical nine-level catalyst;
it was replaced before any all-size claim. Strongest reproduction seam:
solver tolerances and an incomplete pattern bank. The retained exact duals,
separate bath-label reconstruction, complete gap-word coverage and11 equality
systems address that seam. Five faults change dual, normalization, completion
or return data and must fail actual equations. Provenance hashes are counted
separately from mathematical certificates.

All verification is internal and same-author through distinct implementations;
there is no external specialist, proof-assistant or novelty certification. No
source, physics-ledger or canon verdict changes. The next thermal problem is
whether multiple components with their actual physical placement can beat
(1), or whether a component-aware lower certificate proves they cannot.
Further lengthening of a single connected component is settled here.
