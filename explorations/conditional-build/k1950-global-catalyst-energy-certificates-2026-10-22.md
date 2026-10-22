---
title: "K1950: Finite global duals and a sharp mean-energy frontier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional mathematics; no native GU identification, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1950_global_catalyst_energy_certificates.py
  - tests/channel-swings/k1950_global_catalyst_energy_certificates_probe.py
---

# K1950: Finite global duals and a sharp mean-energy frontier

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
result: finite certificates for global penalized catalyst return, three sharp energy segments and nonattainment
carrier: fixed four-state extreme Schur channel, faithful four-level Gibbs bath, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex channel and unitary; energy-diagonal optimization via covariant pinching
grading: exact additive energy shells, no physical chirality
action_owner: repository-construction -- conditional energy-conserving shell protocol
target: unrestricted catalyst mean-energy return infimum MAP-TYPE=intertwiner
```

## Result and scope

For the fixed channel/bath model of
[K1943](k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md), a finite
exact program can certify a GLOBAL affine energy bound, without a truncation
error. Every positive energy penalty has a sufficient finite cutoff. This
turns the earlier convergent hierarchy into a finite exact method for its
positive-slope supporting lines.

At bath parameter t=1/2, the unrestricted mean-energy infimum is now exactly

    Rstar(E) = 3/4-E/4,            1 <= E <= 6/5,
    Rstar(E) = 63/100-3E/20,       6/5 <= E <= 11/5,
    Rstar(E) = 15/28-3E/28,       11/5 <= E <= 19/8.     (1)

The first and third segments are attained by finite nondegenerate catalysts. The second
segment is attained at its endpoints; at EVERY strict interior energy its
value is an infimum which no finite nondegenerate catalyst attains, including
coherent preparations. For example Rstar(3/2)=81/200 and Rstar(2)=33/100.
These numbers were previously only finite-cutoff upper bounds. No evaluated
formula beyond19/8 or efficient all-energy algorithm is asserted.

Assumptions stay fixed: exact full-channel simulation for all inputs; faithful
bath energies0,1,2,3 with weights t^b/Z; independent initial registers;
nonnegative finite nondegenerate catalyst spectrum with ground0; mean initial
energy E; worst-input CATALYST MARGINAL half trace distance. Product return,
repeated use, degenerate catalysts and approximate channels are different
problems. This is independent conditional mathematics. SC-META-53 is UNCERTAIN;
LT-SM8, LT-GR6b and AC-F1 remain NEEDS. Native GU, source, ledger and canon
postures do not change.

## 1. The homogeneous return functional

Reuse K1943's all-input shell theorem. For occupied support S and nonnegative
weights p, not necessarily normalized, an edge between s and s+d, d=1,2,3,
has weights x=H_d p_s, y=L_d p_(s+d), where

    L_d=(1+t+...+t^(3-d))/Z, H_d=t^d L_d.

Its incoming excess is(y-x)_+ at the lower site and(x-y)_+ at the upper.
The exact optimal marginal return functional is

    R(p)=1/2 sum_s(p_s-I_s)_+.                           (2)

It is homogeneous and additive over disconnected resonance components.
Complete shell unitaries attain(2) on every physically completed support.
For coherent initial preparations the diagonal value is a lower bound by
covariant pinching, not a prescribed-state equality theorem. Pinching preserves
energy and exact channel simulation, so the unrestricted optimum may be
computed using diagonal preparations. These are reused results, not new
claims inferred from the linear programs below.

## 2. A one-sided tail inequality

Split at an arbitrary cutoff K, with p_low keeping energies <=K and p_high
having total mass delta. No renormalization is performed. Every connected
resonance component is an increasing path with gaps1,2,3 and adjacent gap
sums at least4. Its low-energy vertices form a prefix. There is at most ONE
edge crossing from that prefix to the removed suffix.

On a retained site, restoring the high population can increase its incoming
excess by at most L_d times the high endpoint population. Each high vertex
has at most one lower retained neighbor, and L_d<=1. Since u->u_+ is
1-Lipschitz and the high-site terms in(2) are nonnegative,

    R(p) >= R(p_low)-delta/2.                            (3)

The proof sums actual edge contributions, not a dimension-dependent
continuity estimate. It works for arbitrary fractional spectra and
unnormalized weights. The independent bath-label tests exercise crossing
edges and several temperatures; the path and Lipschitz argument establishes
the universal statement.

## 3. Finite global energy-penalty certificate

Suppose every canonical connected support with maximum energy <=K obeys

    R(p)+lambda sum_s s p_s >= a sum_s p_s, lambda>0.     (4)

Canonical offsets are exactly K1943's `max(1,3-first_gap)`, with singleton
energy1. Every physical component can be translated down to that offset
without changing its return, so(4) holds for every retained fractional
component as well. Summing(4) and applying(3) gives

    R(p)+lambda E >= a + sum_(s>K)(lambda s-a-1/2)p_s.   (5)

Therefore the FINITE certificate(4) is global whenever

    lambda K >= a+1/2.                                 (6)

This is an exact lower bound, not a cutoff approximation. The same finite
program supplies a physical canonical attaining protocol for the penalized
objective when a is its minimum. Thus it computes the exact global value

    a(lambda)=inf_protocol [return+lambda mean_energy].

A sufficient cutoff always exists. The energy1 singleton gives
`a<=1/2+lambda`, so any integer `K>=1+1/lambda` guarantees(6) for the finite
minimum. Enumerate finitely many gap words and all orientation cells of(2);
on each cell solve a linear program in p and nonnegative deficits z, with
objective `sum z/2+lambda sum s p`, normalized p. Rational t,lambda give
fully rational primal/dual certificates. This may be exponentially expensive;
finite exactness is not an efficiency claim.

A useful follow-through is the complete scalar dual representation

    Rstar(E)=sup_(lambda>=0) [a(lambda)-lambda E].         (7)

K1943 established convexity, monotonicity and continuity of Rstar on[1,infinity).
Supporting-line separation gives(7); a(0) is the known bath floor infimum.
For interior E, rational positive slopes are sufficient by continuity of
the finite concave a on(0,infinity), with the zero-slope limit if needed.
This representation identifies which finite certificate can settle a chosen
energy question. It does not promise one finite slope attains the supremum
at every E or provide a closed all-E formula.

## 4. Three exact global supporting lines

The stored certificate covers ALL15 cells through K=5 at lambda=1/4 and
ALL103 cells through K=8 at lambda=3/20, and ALL671 cells through K=11
at lambda=3/28. It verifies exact nonnegative primal
weights, every orientation/deficit inequality, dual signs, coefficient
domination, and primal-dual equality. The minima and tail margins are

| lambda | K | a | lambda K-a-1/2 |
|---|---:|---|---|
|1/4|5|3/4|0|
|3/20|8|63/100|7/100|
|3/28|11|15/28|1/7|

Floating HiGHS only discovers candidates. Rational replay accepts them, and
an independent checker enumerates integer supports as subsets and reconstructs
coefficients directly from coincident bath labels. It does not call the
producer's path generator, cell builder or return formula.

For 1<=E<=6/5, take support{1,3} with weights
`((3-E)/2,(E-1)/2)`. Direct substitution in(2) gives3/4-E/4; a full ladder
0,...,6 supplies physical shell completion and the exact full complex
unitaries. Thus the first lower line is attained throughout that interval.

For the second line the two endpoint protocols are

    A: p=(9/10,1/10), energy6/5, return9/20;
    B: p=(2/5,3/5),   energy11/5, return3/10.

Both use support{1,3}. Mixtures of disconnected fractionally shifted copies
approach their convex segment. K1943's strict-slack physicalization keeps the
spectrum nondegenerate and the energy budget exact. Combining the global
lower bound with this limit proves the second formula in(1).

For 11/5<=E<=19/8, set theta=(E-11/5)/(19/8-11/5) and use support{1,3,5}
with weights

    p=(1-theta)*(2/5,3/5,0)+theta*(3/8,9/16,1/16).

These remain in one orientation cell. Their return is15/28-3E/28, matching
the third global line. The physical ladder0,...,8 and complete shell unitaries
attain it throughout the interval. Exact full-unitary checks include
E=11/5,9/4,23/10,19/8. Thus finite attainment resumes at the third segment.

## 5. Why the second interior segment is not attained

This is stronger than observing that the example uses a limit. For lambda3/20,
(5) has STRICT positive tail coefficient at every energy>K, so equality
forbids all such population. Translating a component down to its canonical
offset also strictly lowers the penalized cost unless that offset is already
minimal. Thus every component of an equality protocol must already be
canonical and must attain a=63/100 in the finite census.

For EACH optimal orientation cell, the independent certificate collects the
constraints with strictly signed dual multipliers and the zero variables
with strictly positive reduced cost. With normalization, their exact matrix
has full column rank. Hence the optimal preparation in that cell is unique.
The complete census yields ONLY A and B above, with all additional listed
support weights zero. This is an exact optimal-face proof, not a solver's
choice of one endpoint.

Every equality component would therefore occupy the SAME two energies1,3.
Two disconnected components cannot both do so in a nondegenerate catalyst.
There can be only one actual equality component, giving energy6/5 or11/5,
never an interior value. A protocol with energy below the stated interior
budget cannot attain its bound either, because lambda>0 makes the lower
line strictly larger at lower energy. A coherent attaining protocol would
pinch to a diagonal attaining one at the same energy, which is impossible.
This proves nonattainment across the declared finite nondegenerate class.

Degeneracy would permit orthogonal component labels at identical energies,
and is explicitly outside the theorem. This explains the role of that
assumption instead of treating a classical mixture as a free external flag.

## 6. Actual finite consumers and energy inversion

At E=3/2 use weight w=7/10 of protocol A and1-w of B, shifted by epsilon
and2epsilon. Their mean becomes E+(2-w)epsilon. Mix them with the unshifted
energy1 singleton using

    scale=(E-1)/(E-1+(2-w)epsilon).

The resulting nondegenerate physical spectrum and complete full-channel
unitaries have EXACT mean E and return

    scale*(81/200)+(1-scale)/2.

The gap above the infimum is exactly

    (2-w)epsilon/(E-1+(2-w)epsilon)*(1/2-81/200).         (8)

The report verifies complete shells for epsilon1/100,1/1000,1/10000,
yielding returns11/27,4063/10026,40513/100026 respectively. In particular
81/200 is a real infimum with explicit finite near-minimizers, not the return
of an inadmissible degenerate construction.

Equation(1) also gives sharp necessary energy thresholds. For a return
budget r in[9/20,1/2], the minimum energy is3-4r and is attained. For
r in(3/10,9/20), the infimum required energy is(63-100r)/15, but equality
energy is not attained by any finite nondegenerate protocol. Budgets above
that threshold can approach the frontier closely enough to satisfy the
return constraint. The endpoint r=3/10 is attained at11/5; r=9/20 at6/5.
For r in[9/32,3/10], the minimum energy is5-(28/3)r and is attained.
These are consequences for this exact-channel/marginal-return model, not
universal thermodynamic laws or repeatability claims.

## 7. Verification, prior work and next question

Producer:21733 exact controls and789 global cells, including physical full
complex unitaries and Gram matrices. Independent probe:4898 exact controls
from bath-label enumeration, separate path census, dual reconstruction,
optimal-face rank and tail cases. Four actual mathematical input faults
(dual value, preparation, penalty and multiplier) are rejected after a green
baseline; two identity/pin faults are separately reported. Infinite support,
nonattainment and dual representation rely on the explicit proofs above.
This is internal verification, not external expert or proof-assistant acceptance.

[Ng et al., Limits to catalysis in quantum thermodynamics](https://arxiv.org/abs/1405.3039)
already study dimension and mean-energy constraints through convex relaxations.
No novelty is claimed. The target-specific new result is the one-sided
homogeneous tail certificate, its finite global penalty computation and the
matched low-energy frontier with a precise nonattainment boundary.

Beyond E=19/8, new smaller-slope certificates or structural path compression
are useful. The sufficient cutoff grows as1/lambda; blindly enumerating
large trees is not automatically the best method. Compare an analytic
state-space recurrence with the independent scalar primal/cut match and a
source-compatible principal-symbol construction before expanding.
