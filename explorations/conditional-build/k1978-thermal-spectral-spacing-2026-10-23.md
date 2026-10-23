---
title: "K1978: Positive spacing restores attainment and has a sharp feasibility threshold"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1978_thermal_spectral_spacing.py
  - tests/channel-swings/k1978_thermal_spectral_spacing_probe.py
---

# K1978: Positive spacing restores attainment and has a sharp feasibility threshold

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
result: attained fixed-spacing optimum, strict compact-uniform chord gap, sharp spacing2 feasibility and exact energy edge
carrier: finite nondegenerate catalyst and fixed four-level bath t=1/2 LAYER=toy CHIRALITY=N/A
pairing: positive trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving unitaries, real ordered energies with minimum gap delta
grading: physical bath resonance components, not density rank
action_owner: repository-construction -- changed minimum-spacing resource model
target: dimension/energy/spacing-constrained exact channel simulation MAP-TYPE=intertwiner
```

## 1. Freeze a changed physical resource model

Use [K1975](k1975-thermal-sharp-dimension-threshold-2026-10-23.md)'s exact
extreme four-state channel and bath energies0,1,2,3 at t=1/2. Require at most
d finite nondegenerate catalyst levels, ground0, mean energy AT MOST E, and
now add a fixed positive minimum gap delta between consecutive energies.
The return is worst-input catalyst marginal half trace distance. Independent
initial registers and exact full-channel simulation remain required.

For every fixed d and delta>0, IF this constrained feasible set is nonempty,
its infimal return is attained by an actual physical protocol. For every
6/5<E<11/5 at which it is feasible, its attained minimum is STRICTLY ABOVE
63/100-3E/20. For fixed d,delta the positive gap is uniform on each compact
subinterval of that open energy interval, over its feasible budgets.

This is an at-most-energy theorem; it does not assert attainment on a
noncompact exact-energy shell after adding arbitrarily remote zero-weight
levels. No universal explicit numerical lower-gap constant is supplied.
The result uses real physical spectra with possible NEW resonances in a limit,
not coincident tagged spectra or degenerate catalyst levels.

## 2. A bounded representative for every protocol

Sort the actual energies e_i. Join two levels if their difference is1,2 or3;
let the connected components be c. Within each component

    e_i=x_c+n_i, min n_i=0, n_i integer,
    0<=n_i<=3(d-1)=S.

The span bound follows from a simple connecting path with at most d-1 edges.
Every original total bath/catalyst energy shell belongs to one component:
a shared shell makes two catalyst energies differ by an integer of size<=3.
Shifting each component by a constant therefore preserves all its old shell
unitaries and all channel/output matrices in the identified basis.

Keep the GLOBAL order of the levels. New component offsets y_c must obey

    y_c>=0,
    y_(c(i+1)) >= y_(c(i))+delta+n_i-n_(i+1).              (1)

The original x is feasible. Add a root with zero-weight edges to every
component and take longest-path potentials in this lower-bound graph.
Feasibility excludes positive directed cycles. A longest path can be chosen
simple after deleting nonpositive cycles. Its at most d-1 non-root edges
have weight<=delta+S. Consequently

    0<=y_c<=(d-1)(delta+S), y_c<=x_c,
    0<=e_i'=y_c+n_i <=H=(d-1)(delta+S)+S.                 (2)

Every inequality holds by the path extension property. The component with
original ground0 keeps offset0, since its lower bound is0 and y<=x.
The new spectrum keeps spacing>=delta, distinctness and order, and decreases
EVERY level's energy. This standard
[difference-constraint argument](https://live.ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/a9e76885a78c729f2375e14830caebf2_MIT6_046JS12_lec07.pdf)
is applied to actual component offsets rather than to abstract tags.

Different components may now acquire a resonance. That is allowed: their
old shell subspaces remain orthogonal and their old unitary blocks form a
block-diagonal conserving unitary inside the enlarged shell. No old equality
is broken. The protocol's channel, catalyst state matrix and return are
unchanged; mean energy cannot increase (even for a coherent preparation,
energy depends only on diagonal populations).

Thus every feasible protocol has an equally good representative in[0,H].
This is why a mean-energy bound suffices despite arbitrarily high empty or
very weakly populated original levels.

## 3. Compactness gives an actual minimum and strict uniform gaps

For each actual dimension n<=d, ordered spectra in[0,H] with e_0=0 and gaps
>=delta form a compact set. Density matrices and finite unitaries form compact
sets. Conservation [U,H_total]=0, exact implementation of the target channel
and the mean-energy inequality are closed conditions. The return, a maximum
of trace distances over a compact system-state set, is continuous in these
finite-dimensional data. The finite union over n<=d is compact. Compression
shows that minimizing there loses no value, proving attainment when nonempty.

New resonances do not spoil closedness of the commutator condition. Nor is
there a limiting collision, since delta>0. One may alternatively pinch the
initial catalyst in its energy basis: covariance preserves the exact channel
and energy while convexity cannot worsen return. Coherent protocols therefore
do not evade the inherited global dual or nonattainment statements.

K1950/K1975 prove no finite nondegenerate protocol at an interior energy can
attain the global exposed line. If a protocol has actual mean e<=E, its dual
bound R>=63/100-3e/20 is strictly larger than the E-line when e<E. If e=E,
the existing interior nonattainment excludes equality. The compact minimum
therefore has a positive gap. Add E in any compact interior interval to the
compact minimization to obtain a UNIFORM positive gap over feasible budgets.
Empty feasible sets are not assigned an attained value or a finite gap.

## 4. Executed successor: exact spacing threshold and minimum-energy edge

The bath shell indexed b=1 of any occupied catalyst energy e has at least
two environment directions: the target channel's minimum Kraus rank is2.
A distinct catalyst partner e+q must satisfy q=1-b' for some b' in{0,1,2,3}.
If delta>1, the ONLY permitted nonzero gap is q=-2. Similarly the b=2 shell
forces q=+2. Thus EVERY occupied e has physical levels e-2 and e+2 whenever
delta>1. In particular e>=2, and no exact protocol can have mean energy<2.
If delta>2 even the required gap2 is forbidden: exact implementation is
IMPOSSIBLE for every finite d and every energy budget in this model.

The threshold is sharp. The three physical levels{0,2,4}, pure preparation
at2, meet every rank-two shell requirement: for total energies2,3,4,5 there
are exactly two available environment directions. The existing complete shell
unitary construction implements the whole channel. Its optimal marginal
return is1/2, calculated by the actual bath-label formula; the result is not
a Gibbs-population-ratio guess. An initial guessed3/5 was rejected by this
exact computation and corrected before accepting the witness.

For every1<delta<=2 and d>=3, this protocol is feasible at mean2. Since all
occupied energies must be>=2, a budget2 forces the preparation to be supported
only at the nondegenerate level2. The shell formula then has return>=1/2,
attained by the witness. Hence the exact energy-edge result is

    F_(d,delta)(2)=1/2,  F_(d,delta)(E)=infeasible for E<2
    (d>=3, 1<delta<=2).

This follows for coherent preparations too by pinching; at exact minimum mean
only one energy can carry population. Additional empty levels cannot improve
the pure-support bound. No all-E curve for delta in(1,2] is claimed.

## 5. Executed successor: a matching vanishing-spacing upper rate

For0<delta<=1/2 and d>=10 reuse the ACTUAL two ladders
{0,...,4} union {delta,...,4+delta}. Their minimum spacing is delta.
At every6/5<E<11/5 set w=(E-6/5)/(1+delta), mixing the prior typeA/B
preparations. The mean is exactly E and the return gap is exactly

    R_delta-[63/100-3E/20]
      =(3/20)(E-6/5)delta/(1+delta)>0.                   (3)

Thus fixed positive spacing forbids arbitrary approach at fixed dimension,
but the constrained infimum converges to the global line as delta decreases
to0, with explicit O(delta) UPPER error for d>=10. This is not a matching
universal linear lower rate or an optimum claim for this family.

## 6. Validation and limits

The producer checks24 exact compression cases with remote unused levels,
27 physical ten-level families, and the threshold witness. A separate probe
checks3387 rational ordering, energy, old-shell-preservation, bath-return,
rank and spacing obligations, with four mathematical faults rejected after
its baseline. The universal theorem is the analytic compression/compactness
and shell argument above; finite examples are not its proof. The source
results for complete shell realization and global exposed faces are reused,
not recounted as newly verified whole banks.

Strongest overclaim: compactness without controlling unoccupied levels;
section2 supplies the missing bound. Strongest contrary case: new resonances
at a limit; they permit the old block-diagonal unitary and preserve closedness.
Weakest remaining quantitative seam: the strict lower gap is nonconstructive
and need not be linear in delta; (3) supplies only an upper rate. Computing
that constrained frontier is newly meaningful, while replaying fixed-d
unconstrained nonattainment is not.

Conditional independent mathematics only; no external expert/formal acceptance
or novelty claim. SC-META-53 remains UNCERTAIN. LT-SM8/LT-GR6b/AC-F1/RA-F1,
source, physics-ledger and canon verdicts stay unchanged.
