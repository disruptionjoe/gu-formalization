---
title: "K1975: Ten levels are necessary and sufficient to approach the global thermal chord"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1975_thermal_sharp_dimension_threshold.py
  - tests/channel-swings/k1975_thermal_sharp_dimension_threshold_probe.py
---

# K1975: Ten levels are necessary and sufficient to approach the global thermal chord

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
result: sharp physical dimension threshold10 on the entire open exposed energy segment
carrier: fixed extreme four-state channel, bath t=1/2 and finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real energy populations
grading: bath resonance components, not density rank or chirality
action_owner: repository-construction -- fixed conditional model
target: joint physical dimension and exact mean energy MAP-TYPE=intertwiner
```

## 1. Sharp joint resource threshold

Use [K1950](k1950-global-catalyst-energy-certificates-2026-10-22.md)'s fixed
extreme four-state Schur channel, faithful bath t=1/2 with energies0,1,2,3,
exact full-channel simulation, independent initial registers, finite
nonnegative nondegenerate catalyst energies with ground0, mean-energy budget E,
and worst-input catalyst MARGINAL half trace distance. Let F_d(E) be the
infimum with at most d physical catalyst levels, as in K1968.
For EVERY6/5<E<11/5:

    F_d(E)>63/100-3E/20                  for3<=d<=9,
    F_d(E)=63/100-3E/20                  ford>=10.       (1)

The strict gap for any fixed d<=9 and interior E is positive, not merely
nonattainment. The d>=10 equality is an infimum and is NEVER attained by any
finite nondegenerate catalyst at an interior E, even allowing coherent
preparations. At either endpoint only five levels are needed. Thus the
minimum dimension for arbitrarily accurate approach to the global segment
jumps from5 at its endpoints to10 everywhere in its interior.
This closes a structural larger-d question without computing another table
of sampled energy values or re-proving the earlier all-d finite algorithm.

## 2. Lower bound: compact tagged programs and exposed faces

Reuse K1950's exact GLOBAL dual R+(3/20)E>=63/100. Its independently checked
optimal-face census, including a strict high-energy tail coefficient, shows
that EVERY normalized equality component has occupied energies{1,3} and
one of only two populations:

    A=(9/10,1/10), (e_A,r_A)=(6/5,9/20),
    B=(2/5,3/5),   (e_B,r_B)=(11/5,3/10).              (2)

These are exact full optimal faces, not solver-selected sample vertices.
K1968's complete fixed-d canonical/tagged formulation is a finite union of
compact population polytopes: physical connected shapes have span<=3(d-1),
integer gaps1,2,3, finitely many occupied supports and finitely many tags.
Nonnegative offsets may be lowered to0 for the infimum; coincident canonical
tags are kept distinct and charged their actual separate physical dimensions.
Its exact-budget physicalization proves this compactified minimum equals F_d.
K1972 permits at most two populated physical components but is not needed to
assume global convexity at fixed d.

If F_d(E) equaled the global line at an interior E, a canonical minimizer
would exist in that finite compact union. The positive dual slope requires
its energy to equal E. Every positive-weight tag must itself saturate the
global dual, so by(2) it must be type A or B. A single tag cannot have an
interior energy. Both types must have positive weight, and each physical
tag needs at least2*2+1=5 levels by K1966's shell bound. They cost at least10.
For d<=9 equality is impossible in the COMPACT minimization, hence the
value is strictly greater. This is why global nonattainment alone would not
have sufficed to prove the first line of(1).

Zero population tags can be dropped. Coherent preparations are covered by
covariant pinching preserving energy/dimension and improving return. Two
identical copies of A or B cannot produce an interior energy. A connected
shape with extra zero sites cannot evade the complete optimal-face statement.
The proof makes no claim that the positive gap is uniform as E approaches
an endpoint; it must vanish there.

## 3. Upper bound: exactly ten actual levels and exact energy

For0<epsilon<1 choose the physical catalyst spectrum

    {0,1,2,3,4} union {epsilon,1+epsilon,...,4+epsilon}.

It has10 DISTINCT energies and two nonresonant bath components. Put weight
1-w on preparation A in the first ladder and w on preparation B in the
shifted ladder, with

    w=(E-6/5)/(1+epsilon).

For every interior E this lies strictly between0 and1. The four occupied
levels are1,3,1+epsilon,3+epsilon, with probabilities
((1-w)9/10,(1-w)/10,2w/5,3w/5). Each five-level ladder meets every exact
shell rank requirement; the inherited complete shell unitary construction
therefore implements the full channel for all inputs. Mean energy is EXACTLY E.
The exact marginal return is

    R_epsilon=9/20-(3/20)w,
    R_epsilon-[63/100-3E/20]
        =(3/20)(E-6/5)epsilon/(1+epsilon)>0.            (3)

Letting epsilon decrease to0 proves equality of infima at d10. Empty remote
levels extend it to every d>10 without changing preparation or return.
K1950's nonattainment theorem still applies: at epsilon0 the two canonical
spectra collide, which is excluded. A free external classical flag or
spectral degeneracy is not being smuggled into the physical model.

## 4. Quantitative accuracy and resource consequence

Let A_E=(3/20)(E-6/5). For a requested positive return gap delta<A_E,
choosing

    0<epsilon<=min(1/2, delta/(A_E-delta))              (4)

guarantees gap<=delta with exactly10 levels and exact energy. For larger
delta any sufficiently small positive epsilon works. This charges approach
to arbitrarily fine spectral separation, not growing physical dimension.
The model places no lower bound on energy spacing. If a new spacing constraint
is imposed, (1)'s sufficiency does not automatically transfer; (3) gives
one family's actual sensitivity, not a universal spacing lower bound.

At E=3/2 the limiting return is81/200. The previously exact dimension-eight
value5/12 exceeds it by7/600. Dimension nine also has a strict gap by section2,
although its explicit value is not computed here. The threshold is10, not
"at most13" from a three-component budget-repair construction. The exact-budget
weight adjustment eliminates that extra singleton while preserving physical
nondegeneracy.

## 5. Verification and remaining frontier

The producer checks57 exact ten-level families across the entire open segment.
The separate probe checks805 energy/edge-return/shell/dimension obligations,
rejects four mathematical faults, and replays664 exact lower-dual/optimal-face
obligations from the relevant K1950 bank only. No unchanged unrelated banks
are rerun. General strictness follows the compactness and face argument above,
not the finite energy samples.
No novelty, external expert acceptance or formal certification claimed.
Unrestricted sharp subleading price, explicit d9 curve, minimum-spacing
constraints, approximate channels and product return remain distinct frontiers.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/AC-F1 remain NEEDS. No native GU
identification, source, physics-ledger or canon verdict moves.
