---
title: "K2049: A physical packing transition above half spacing"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: unrestricted finite/countable thermal model for1/2<delta<=1 and17/5<=E<=675/181
scripts:
  - tests/channel-swings/k2049_wide_spacing_packing.py
  - tests/channel-swings/k2049_wide_spacing_packing_probe.py
---

# K2049: A physical packing transition above half spacing

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
result: three exact wide-spacing energy segments, a strict jump and resource drop
carrier: four-state bath and finite/countable pure-point catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex states with nonnegative real populations
grading: exact bath energy shells and occupied components
action_owner: repository-construction -- inherited exact energy-conserving shell channels
target: wide-spacing optimum and physical resource necessity MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Physical spacing strictly greater than
one half changes the optimum. On the entire rectangle

    1/2 < delta <= 1,   17/5 <= E <= 675/181,

the unrestricted finite/countable thermal optimum is independent of delta
and has three connected-component segments. At E=7/2 its value jumps upward
by exactly1/1540 from the half-spacing value, while the necessary number of
physical catalyst levels drops from14 to7. This resolves a real packing
transition, not just failure of the old fractional-offset construction.

## 1. Fixed model and exact answer

Keep [K2047](k2047-fifth-thermal-spacing-phase-2026-10-25.md)'s bath with
energies0,1,2,3 and populations(8,4,2,1)/15, exact energy-shell channels,
nondegenerate nonnegative pure-point catalyst energies, minimum physical
spacing delta and mean budget E. Keep its return objective unchanged.
Define population vectors at consecutive odd inputs:

    X=(8,12,3)/23 on1,3,5: (EX,RX)=(59/23,15/46),
    R=(4,6,9)/19 on1,3,5: (ER,RR)=(67/19,9/38),
    Q=(1/5,3/10,9/20,1/20) on1,3,5,7: (EQ,RQ)=(37/10,9/40),
    B=(36,54,81,9,1)/181 on1,3,5,7,9: (EB,RB)=(675/181,81/362).

Then

    F_delta(E) = (79-13E)/140   for17/5<=E<=67/19,
                 (21-3E)/44    for67/19<=E<=37/10,
                 (81-9E)/212   for37/10<=E<=675/181.       (1)

Each segment is attained by interpolating the two named populations in ONE
common return chamber, completing the physical spectrum to the consecutive
integers0,...,6,0,...,8 or0,...,10. The direct shared-maximizer and deficit-sign
checks prove affinity over the entire interpolation, not just endpoints.
These spectra obey every delta<=1. No new fractional translation is required.

## 2. New packing lemma on the original spectrum

Use the canonical connected occupied-component supports and retained original
offsets d_i of K2037/K2043. For a component with d_i<1, its physical spectrum
forces BOTH d_i and d_i+1:

- first gap1: canonical root2 and the shared shell3 force all four levels0..3;
- first gap2: canonical root1 and the same shared shell force0..3;
- first gap3, or an isolated input: the shell at root1 admits only levels0,1
  because the alternatives are negative; both are needed by shell capacity.

Translate by d_i throughout. The last argument remains valid for d_i<1,
which is the new threshold; it does not require d_i<delta. Bath partners
always differ by integers, so another fractional residue cannot repair a
missing required partner. Canonical compression retains the original lower
boundary offset; it does not move a missing physical ground into existence.

If two distinct offsets satisfy0<=d_i<d_j<1, their two forced pairs give
physical gaps d_j-d_i and1-(d_j-d_i). One is at most1/2. This contradicts
delta>1/2. If their offsets are equal, their first occupied roots differ by
at most1 and share a bath shell, so they are the same occupied component.
Consequently AT MOST ONE component has offset below1; every other component
pays at least1 on its entire mass. This is stronger than the old offset-delta
bound and is discontinuous at delta=1/2, where interlacing is possible.

This lemma does not say all spectra have one fractional residue or one
component. High translated components remain allowed and must still enter
the lower bound.

## 3. Cellwise exact lower certificate and countable transfer

Reuse K2045's cutoff-eleven bank:671 orientation cells and20975 vertex records,
independently enumerated over626412 bases. Its bytes are pinned; enumeration
is not repeated. For each energy interval in(1) and each possible low cell,
the certificate assigns one affine line g(e)=alpha-s e, s>0, such that

    R(v)>=g(e(v)) on that low cell,
    R(v)>=g(e(v)+1) on EVERY high cell,
    g(12)<=0, g(13)<=0,
    g(E)>=the stated line in(1) on the whole energy interval. (2)

The last difference is affine, so exact endpoint checks prove the complete
interval. The producer uses convex hulls only to find these witnesses. The
separate checker evaluates the explicit inequalities directly, using actual
bath-label maxima to reconstruct all20975 vertex values. No optimization
solver or claimed optimum is an input to those checks.

For an unnormalized component of mass m, original energy e_actual and offset
d, let ell=0 for the exceptional low component and ell=1 for the others.
Erase mass q above canonical11 with canonical energy h>=12q. The inherited
zero-loss erasure and(2) give

    R_component >= alpha*m-s*e_actual
        +(12s-alpha+s*ell)*q+s*(h-12q)+s*m*(d-ell).       (3)

Every correction is nonnegative. Sum over components and add unused-budget
slack s*(E-e_actual_total). For the actual low cell use its assigned g;
if no low component exists, any assignment works. Then(2) proves(1).
Finite mean and the inherited l1 continuity justify countable sums; original
offsets and energy tails are retained. This is the whole-domain bridge from
the finite bank, not an inference from a small tail probability.

Some unused supporting lines pass through(12,0). Their non-strict tail margin
is sufficient for the lower bound. Equality arguments below use the target
line itself, whose tail and high-offset margins are strictly positive; these
two statements must not be conflated.

## 4. Equality, physical resources and the actual jump

For energies strictly inside each of the three intervals in(1), equality
forces the assigned line to equal the target line: otherwise its affine
excess is positive in the interval interior. All high-component target-line
margins are strictly positive, as are tail margins. Thus equality has one
unshifted, untruncated component and uses its full energy budget. The complete
low equality vertices, restricted to cells supporting the target, are

    XR: X,R;   RQ: R,Q;   QB: C,Q,B,
    C=(3/8,9/16,1/16), energy19/8, return9/32.

Below ER but above17/5, both X/R inputs keep all three occupied odd levels.
Between ER and EQ a positive Q weight forces four odd levels. Above EQ,
only B has energy exceeding EQ among the QB zero vertices, so positive B
weight forces five odd levels. Shared two-input shells force each consecutive
physical completion. Hence the strict-interval minimum numbers of physical
levels are7,9 and11, respectively. These are necessity statements, not just
sizes of examples. At ER and EQ the explicit pure R and Q attain with7 and9;
no exhaustive critical optimizer classification is claimed here.

At E=7/2, strictly inside XR, (1) gives67/280 and exactly7 necessary levels.
K2047's proved half-spacing value is21/88 with exactly14 necessary levels.
Their difference is

    67/280 - 21/88 = 1/1540 > 0.                          (4)

Thus both the right-limit jump in optimal cost and the14-to7 resource drop
are actual properties of the unrestricted model. The optimum is constant in
delta over(1/2,1] at this energy, so a near-boundary sample is unnecessary.
The seven-level realization at7/2 is the exact X/R interpolation.

## 5. Limits and next construction

This result does not determine the entire lower-energy region between A and
17/5. For example, the cutoff-eleven relaxation at E=5/2 uses a fictitious
line from T to(12,0); this tail endpoint is not an attained physical channel.
It is preserved as a failed tightness route, not labeled the true optimum.
Further progress there needs a sharper tail argument or actual low-component
packing optimization. Spacing above1 also lies outside the present realization.
The three energy segments and full open-closed spacing range are exactly the
claimed scope; the proof of at most one offset below1 is not a claim that all
other components can be discarded without the supporting certificate.

The separate probe reconstructs the bank through physical bath labels, checks
all new support lines, actual whole-chamber interpolation and physical
completions, plants forbidden ground-pair interlacings and rejects four
coefficient/population/jump faults after a clean baseline. Written proofs
supply the unbounded/countable and spacing claims. Raw bank completeness and
erasure are hash-pinned reuse; this is same-author internal checking, not
external, proof-assistant or novelty certification. Source claims, the physics
ledger and canon remain unchanged.
