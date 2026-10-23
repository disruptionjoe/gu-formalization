---
title: "K1972: Two populated components suffice at every finite dimension"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1972_thermal_two_component_reduction.py
  - tests/channel-swings/k1972_thermal_two_component_reduction_probe.py
---

# K1972: Two populated components suffice at every finite dimension

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
result: exact physical two-component dominance, dimension-charged connected-cell reduction and an open interval of nonattainment
carrier: fixed extreme four-state Schur channel and finite nondegenerate catalyst with four-level bath LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input catalyst marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real energy populations
grading: energy resonance components, not density-matrix rank or source chirality
action_owner: repository-construction -- fixed exact channel
target: all finite joint physical-dimension and mean-energy budgets MAP-TYPE=intertwiner
```

## 1. An all-d structural reduction

Use exactly [K1968](k1968-joint-thermal-finite-dimension-program-2026-10-22.md)'s
model and F_d(E). Every finite physical protocol, including a coherent initial
preparation, is dominated by a physical protocol with AT MOST TWO populated
bath-resonance components: no greater physical dimension, no greater initial
mean energy, and no greater worst-input marginal return error.

This is an exact physical dominance statement, stronger than an infimum-only
reduction. There may still be unoccupied levels in the physical completion;
they are not dropped merely because their populations vanish. Two components
is not two occupied energies, two eigenvectors of a density matrix or a new
free classical flag. The result holds for every0<t<1 in the same bath model.

The result eliminates arbitrary multi-component partitions from the joint
resource optimization. K1968's finite shape completeness and K1960's global
convexification are reused. The argument is elementary finite linear programming;
it does not claim new general convex geometry.

## 2. Exact dominance proof, with dimension and coherent states retained

First apply K1943/K1968's covariant pinching and sharp shell construction.
This preserves physical spectrum and mean energy and gives a diagonal protocol
whose sharp return is no larger than the original. Let its populated physical
resonance components be indexed by j. In component j keep its ACTUAL spectrum,
its normalized preparation, its mean energy e_j, its physical dimension d_j
and its sharp normalized return r_j fixed. Let w_j be its population weight.
The exact return formula is homogeneous and has no intercomponent edges:

    e=sum_j w_j e_j,    R=sum_j w_j r_j,   sum_j w_j=1. (1)

The sharp shell unitaries have a common input-independent worst-return value;
we are not replacing the supremum of an arbitrary sum by the sum of suprema.
The pinned construction, rather than an unproved assumption about arbitrary
protocols, licenses(1).

Minimize sum w_j r_j over w_j>=0, sum w_j=1, sum w_j e_j<=E, retaining the
original budget. A compact simplex slice has an optimal extreme point with
at most two positive entries. Direct proof: for any three positive entries,
there is a nonzero vector z supported there with sum z=0 and sum e z=0.
Choose its sign so sum r z<=0 and move until a weight reaches0. Repeat.
If the three energies coincide, use z=(1,-1,0). This preserves mean exactly,
never increases return, and finishes with at most two entries.

Use the original component spectra and their full shell unitaries, reweighting
the initial state. Remove only entire zero-weight components, including their
unused completions. The remaining spectra are still nondegenerate and have no
new resonances; their dimension is no larger. If the ground0 was in a removed
component, translate the entire surviving spectrum down by its minimum. This
preserves conservation and return while decreasing mean energy and restoring
ground0. This constructs an actual admissible dominating protocol without a
collision limit or added flag. Exactly-d padding, if desired, adds empty remote
levels and changes neither mean nor return.

With m independent linear resource budgets the same argument gives at most
m+1 components (rank of the active resource matrix gives the sharper bound).
For this extension one may retain the original unused ground level and all
original physical levels, avoiding any assumption that translating energies
improves a different resource. It presupposes those resources are affine under this actual block
mixing; it does not assert that channel error or repeated-use cost is affine.

## 3. Connected-cell formula and dimension-charged chords

Let G_k(E) be the best return among ONE connected physical bath-resonance
component using at most k levels, normalized to ground0. K1968 bounds its span
by3(k-1), so its finite collection of probability orientation/deficit cells
is compact. G_k is attained and piecewise affine for E>=1.

To obtain F_d it suffices to combine single connected cells and pairs with
physical costs k+l<=d. For a fixed pair of cells, normalized populations have
energy and return affine within each cell. Any point is a convex combination
of its cell vertices. Optimizing the component weights and vertex weights
under one energy inequality again has at most two positive vertex weights.
If both vertices come from one cell, combine them INSIDE that same connected
component, charging its physical cost once. If they come from different
components, charge the SUM of their costs and use their chord.

Therefore the exact budget frontier is the lower envelope of:

1. all connected-cell energy/return segments and their horizontal budget rays;
2. every chord between connected-cell vertices whose two physical costs sum
   to at most d, plus their endpoint budget rays already supplied by item1.

One must not convexify two DIFFERENT cells inside one physical component:
return need not be affine between them. When their chord is used as two tags,
its dimension cost is charged twice. This retains K1968's nonconvex d5 curve.

The normalized two-tag spectra can coincide. For the INFIMUM formula, use
K1968's arbitrarily small fractional shifts and exact-budget population repair
within the already-counted support. If all positive occupied sites share the
minimum energy, the value is1/2 and the three-level singleton realizes it.
This proves exact-budget equality without inventing a zero-energy flag.
The connected formula reduces complexity but gives no polynomial-time claim.

## 4. Released complete nonattainment interval at dimension eight

At t=1/2, enumerate connected cells only, then add dimension-charged vertex
chords. The result recovers EVERY piece of F_d for d3 through8 in K1968.
There are690 connected cells and136 distinct cost/energy/return vertices;
these are finite implementation counts, not the proof of the all-d theorem.

The full new physical consequence is:

    F_8(E)=2/3-E/6,   121/91<E<11/5,
    and no nondegenerate physical protocol attains it.  (2)

The separate connected curve G_8(E) is strictly greater throughout this open
interval, not just at E=3/2. The exact piecewise affine comparison records its
breakpoints and positive gaps. Any attaining protocol would therefore need
two populated components. At d8 the only improving pair is a three-level
singleton and a five-level gap-two component; a second nontrivial pair costs
at least ten levels. Their normalized spectra overlap, so both cannot retain
zero offset in a nondegenerate actual spectrum. At least one positive-weight
component has a positive offset. Removing offsets strictly lowers mean energy
while leaving return unchanged, contradicting the strictly decreasing canonical
F_8 immediately below E. Pinching extends the exclusion to coherent preparations.

A single physical family approaches EVERY point of the open interval:

    A={0,1,2} union {epsilon,1+epsilon,...,4+epsilon},
    p=(1-w,2w/5,3w/5) on (1,1+epsilon,3+epsilon),
    w=(E-1)/(6/5+epsilon),       0<epsilon<1 nonintegral.

It has exactly eight physical levels, mean exactly E, and return
1/2-w/5>2/3-E/6 tending to the infimum. Both endpoints of(2) are attained by
connected competitors, so the open-interval qualification is essential.
The previously rejected global secant is NOT reinstated: this line is only
the dimension-eight frontier on the stated interval. The d5 low-root vertex
(6/5,9/20) remains below its extrapolation.

## 5. Verification, prior art and hostile boundaries

The producer reuses the pinned complete shape inventory but enumerates only
connected probability cells and the new dimension-charged chords, exactly
recovering all six earlier budget curves. Whole affine-piece comparisons
certify the open connected gap. The independent probe implements a different
null-vector weight-elimination algorithm on128 rational multi-component
instances, checks energy/return/normalization/dimension, and separately verifies
the interval and exact-budget approaching families. It passes730 rational
controls and rejects four genuine mathematical faults after a clean baseline.
The general proof is section2; examples do not establish its universal quantifier.

[Winkler's extreme-point work](https://pubsonline.informs.org/doi/abs/10.1287/moor.13.4.581)
is prior context for finite-moment support reduction; its abstract was checked.
The present physical transfer, nondegenerate-spectrum limits and exact dimension
charges are stated explicitly. No novelty or external expert/formal acceptance
is claimed. Strongest overclaim would infer global convexity at fixed d or
finite attainment from the canonical tagged optimization. Neither is asserted.
The unrestricted sharp subleading energy-price coefficient and larger-d closed
interior laws remain open. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/AC-F1
remain NEEDS. No source, physics-ledger or canon verdict changes.
