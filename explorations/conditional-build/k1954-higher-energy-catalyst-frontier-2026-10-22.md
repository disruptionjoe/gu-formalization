---
title: "K1954: A priced thermal tail and higher-energy catalyst frontier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-channel conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1954_higher_energy_catalyst_frontier.py
  - tests/channel-swings/k1954_higher_energy_catalyst_frontier_probe.py
---

# K1954: Price the omitted thermal population

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
result: global thermal tail relaxation, sharp mean-energy segments and a physical secant counterexample
carrier: fixed extreme four-state Schur channel, faithful four-level bath, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex shell unitaries, rational diagonal population certificates
grading: additive energy shells; not physical chirality
action_owner: repository-construction -- exactly conserving conditional channel
target: unrestricted mean-energy return infimum MAP-TYPE=intertwiner
```

## 1. Fixed model and new question

Keep [K1952](k1952-catalyst-path-energy-extension-2026-10-22.md)'s exact
Schur channel, bath parameter t=1/2, bath energies 0,1,2,3, independent initial
registers and exact energy conservation. The catalyst has a finite
nondegenerate nonnegative spectrum with ground 0. The budget is its initial
mean energy at most E; return is the worst-input catalyst MARGINAL half trace
distance. Coherent preparations are included in the lower bound through
K1943's pinching comparison. Joint product return, repeatability, approximate
channels and degenerate spectra are different problems.

The previously evaluated global frontier ended at 675/181. Complete path
searches suggested extensions, with no assumed gap2 optimality. The exact
certificates below settle two new intervals. A plausible third secant fails
on a longer physical path; it is explicitly rejected rather than extrapolated.

## 2. A stronger collapsed-tail inequality

For a path population p, K1943's exact optimal return is

    R(p)=1/2 sum_i (p_i-I_i)_+,
    I_low+=(L_d p_high-H_d p_low)_+,
    I_high+=(H_d p_low-L_d p_high)_+.

K1935 proves the homogeneous global floor

    R(p) >= r_inf sum p,   r_inf=t^2/(1+t^2)^2.          (1)

This floor is reused, not rederived or counted as a new result.
Keep each canonical path through the first vertex h above cutoff K and
collapse every population at h or beyond to delta at h. Let ell denote the preceding path vertex (not necessarily energy h-1).
As in K1952, the retained low-site deficits can only decrease, and the
collapsed energy can only decrease.

There is also a price for the omitted high part. Isolate the original tail
from the last low vertex. Its return is at least r_inf delta by(1). Restoring
the edge from ell can reduce only the first tail deficit, by at most
`H_d p_ell/2`, since its incoming amount is at most H_d p_ell.
The positive-part function is1-Lipschitz. The actual tail contribution
therefore obeys

    tail_return >= max(0, r_inf delta-H_d p_ell/2).       (2)

Consequently

    T_priced = retained_collapsed_low_deficits/2
                + max(0,r_inf delta-H_d p_ell/2)
             <= R(p).                                 (3)

This holds for every orientation and every tail length. The isolated tail
still satisfies the shell support constraints; removing occupied inputs
cannot violate them. The lower bound does not pretend that the collapsed
tail is a physical catalyst. For disconnected components, apply(3) to each
and add homogeneously. Positive fractional offsets only raise a positive
energy penalty. Thus a complete finite certificate for
`T_priced+lambda E >= a` proves `R+lambda E >= a` for arbitrary finite
spectra, including all dimensions.

In the finite LP, retain a terminal deficit variable z_h with cost z_h/2 and
replace its usual deficit inequality by

    2 r_inf delta-H_d p_ell-z_h <= 0, z_h>=0.            (4)

K1952 omitted that terminal cost entirely. This is an actual strengthening,
not an unsupported physical tail truncation. It does not claim polynomial
complexity or a closed all-energy solution.

## 3. New rational frontier

The two supporting lines are:

|Energy interval|Return infimum|
|---|---|
|[675/181,3043/815]|891/2632-(81/2632)E|
|[3043/815,54787/14671]|9477/30208-(729/30208)E|

Their finite banks include EVERY complete path and first-crossing prefix,
EVERY edge orientation, primal feasibility, signed dual multipliers and exact
coefficient domination. Floating optimization only discovers active sets;
acceptance reconstructs rational solutions and checks every inequality.
The independent checker derives coefficients directly from overlapping bath
labels and enumerates integer subsets instead of recursive gap words.

## 4. Attainment and a rejected finite-window extrapolation

The successive endpoint preparations on consecutive odd energies are:

- A: support 1,3,5,7,9 with weights (36,54,81,9,1)/181.
- B: support 1,3,5,7,9,11 with weights (324,486,729,81,9,1)/1630.
- C: support 1,3,5,7,9,11,13 with weights (2916,4374,6561,729,81,9,1)/14671.

Pad the shorter endpoint with a zero final weight. For each pair A,B and
B,C, both endpoint edge imbalances have compatible signs; after choosing
those signs, both endpoint deficits also have compatible signs. Every
imbalance and deficit is affine along the interpolation. Consequently the
entire segment stays in one piecewise-linear sign region and its exact
return is the affine interpolation. This proves attainment for EVERY energy
in both intervals, not just the sampled protocols. The exact supporting
line gives the matching lower bound. The physical consumers reconstruct
full complex shell unitaries, including empty levels and every channel
matrix unit, for endpoints and two interior samples per interval.

A finite hull with occupied energies at most14 suggested a third secant

    R_candidate(E)=31271/107400-(1943/107400)E,
    54787/14671 <= E <= 4781/923.

That is NOT the global frontier. A finite nondegenerate catalyst with
occupied energies 1,3,5,7,9,11,13,15, physical spectrum 0,...,18 and weights

    (26244,39366,59049,6561,729,81,9,1)/132040

has

    E=246549/66020, R=59049/264080,
    R_candidate(E)-R=1063/7090548000 > 0.

The same full shell construction realizes this exact channel and return.
Thus this is a physical counterexample to the secant extrapolation, not a
failure of a truncated proof. It does NOT contradict either new supporting
line or any prior K1952 segment. Higher-energy globality and any subsequent
attainment transition remain open. No third segment is promoted.

The first smaller tail cutoffs12 and14 did not certify the two lines.
The final certificate uses cutoffs14 and16 respectively, with18047 and63615
orientation cells (81662 total); those cutoffs are
proof devices only. The mathematical statement quantifies over arbitrary
finite spectra via(1)--(4).

For a target return r between the endpoint values of either proved segment,
the minimum energy is exactly `(a-r)/lambda`. The line gives necessity and
the affine shell family attains it. This resource inversion introduces no
joint-return or repeat-use guarantee.

## 5. Limits, verification and next question

The independent finite certificate tests, mathematical fault injections,
physical shell consumers, the rejected-secant witness and analytic tail proof have different roles.
Identity and pin checks certify reporting only. The argument for arbitrary
spectra is(1)--(4), together with the inherited exact channel/path bridge.
This is internal verification; no external specialist acceptance, novelty
or proof-assistant certification is claimed.

The closest general prior context is Ng et al.,
[Limits to catalysis in quantum thermodynamics](https://arxiv.org/abs/1405.3039),
on catalyst-return restrictions under dimension and mean-energy bounds.
Its abstract was rechecked; this work does not claim that its fixed-channel
rational certificates are a new general thermodynamic law.

The uncomputed frontier above 54787/14671, efficient path optimization, the
sharp large-energy approach to the known thermal floor, and independent
scalar pulse/cut matching remain distinct open mathematical questions.
SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b and AC-F1 remain NEEDS.
Source, physics-ledger and canon verdicts remain unchanged. No GU physical
operator, observable, curvature drive or thermal bath is identified here.
