---
title: "K2041: Exact small-spacing thermal frontier and its second-order boundary layer"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact finite/countable optimum on a stated small-spacing interval; wider phases open
scripts:
  - tests/channel-swings/k2041_exact_small_spacing_frontier.py
  - tests/channel-swings/k2041_exact_small_spacing_frontier_probe.py
---

# K2041: Exact small-spacing thermal frontier and its second-order boundary layer

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
result: exact small-spacing optimum, equality spectra and nonuniform second-order law
carrier: four-state bath times arbitrary finite or countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex physical states with nonnegative real diagonal populations
grading: energy shells and connected resonance components
action_owner: repository-construction -- inherited energy-conserving shell-channel class
target: unrestricted return frontier and sharp physical dimension MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] Let

    EA=1575/653, RA=729/2612, EB=675/181, RB=81/362,
    Delta=EB-EA=155700/118193,
    C=2907/69200, L(E)=1053/2768-C*E.

For the exact finite/countable model of K2037/K2039,

    F_delta(E)=L(E)+min{
        C*delta*(E-EA)/(Delta+delta),
        C*delta*(EB-E)/(Delta-delta)},                 (1)

whenever 0<delta<=1/23508 and EA<=E<=EB. This determines an actual
positive-spacing optimum, not only an asymptotic squeeze. Its two placements
switch at E=(EA+EB+delta)/2. For strict 0<delta<1/23508 every interior
optimizer requires at least22 physical levels, attained by the two-component
construction; each endpoint requires11. The cutoff1/23508 is a sufficient
certificate range, not a proved physical phase boundary.

## 1. Inputs and the two realizations

Keep the bath energies0,1,2,3 and populations(8,4,2,1)/15, the same shell
channel, nonnegative physical energies, normal finite-mean preparation and
minimum physical spacing delta. Countable means countable pure-point
nondegenerate catalysts with the inherited exact spectral-projection channel
convention. No GU mechanism or source claim is under test.

[K2039](k2039-thermal-component-undercut-2026-10-24.md) supplies the
endpoints on odd inputs1,3,5,7,9:

    A=(486,729,81,9,1)/1306,
    B=(36,54,81,9,1)/181.

Each has physical completion0,...,10. Placing A at offset0 and B at delta
gives the first branch in (1). Reversing those offsets gives the second
branch wherever E>=EA+delta. The second branch wins only at
E>=(EA+EB+delta)/2, where that feasibility condition holds since delta<Delta.
The two fractional residues cannot share bath shells, so the return is
exactly the mass-weighted return. The22 completion levels have gaps delta
and1-delta. Both realizations are valid for the present delta<=1/23508<1/2.
This part is inherited construction, not a new channel theorem.

## 2. Preserve the chamber and offset labels in the lower proof

Use K2037's complete cutoff-nine arrangement bank:183 edge-orientation cells,
3137 vertex records. Subdivide by deficit signs before convex decomposition,
so return is affine in the chamber actually containing a given population.
All such chamber vertices are in that bank. Only A and B have zero defect

    g(v)=R(v)+C e(v)-1053/2768,

and no orientation cell contains both. K2039 already established the
unnormalized erasure and decomposition identity. Denote by alpha,beta the
retained contact masses, z_v the other vertex masses, q the erased tail mass,
h its canonical energy, vtail=h-10q, D the offset-weighted physical mass,
and ell the unused energy budget. With kappa=549/13840>0,

    alpha+beta+sum z_v+q=1,
    E=alpha EA+beta EB+sum e(v)z_v+10q+vtail+D+ell,
    G:=R-L(E)>=sum g(v)z_v+kappa q+C(vtail+D+ell).  (2)

All quantities on the right are nonnegative except explicit differences
introduced below. Countable sums converge under the finite-mean hypothesis;
no small-tail-mass/energy interchange is made. Each vertex piece retains
its original component offset, not a separately reset energy origin.

A component carrying contact mass has actual occupied root1+d. Distinct
such components have roots separated by at least delta, and a component
can carry only one contact type. Therefore one of these alternatives holds:

    A-case: D>=delta*beta,
    B-case: D>=delta*alpha.                          (3)

Indeed at most one contact-carrying component has offset below delta. If it
carries A, every B component pays delta; if it carries B, every A component
pays delta. If none does, both inequalities hold. Noncontact components may
only increase D. This is the physical spacing step; a convex envelope with
freely co-located components would not prove it.

## 3. Two exact supporting inequalities

Put x=E-EA, kA=C*delta/(Delta+delta), kB=C*delta/(Delta-delta).
In the A-case subtract kA*x from (2). The remainder is bounded below by

    sum [g(v)-kA*(e(v)-EA)] z_v
      +[kappa-kA*(10-EA)]q
      +(C-kA)(vtail+ell+D)-kA*Delta*beta.            (4)

The D term and last term are nonnegative together because
(C-kA)*delta=kA*Delta and (3). In the B-case subtract kB*(Delta-x):

    sum [g(v)-kB*(EB-e(v))] z_v
      +[kappa+kB*(10-EB)]q
      +(C+kB)(vtail+ell+D)-kB*Delta*alpha.           (5)

Again (C+kB)*delta=kB*Delta makes the offset terms nonnegative. It remains
to check the actual finite vertex coefficients and strict tail coefficients.
For every positive-defect vertex, the relevant limiting spacings are

    delta_A(v)=Delta*g(v)/(C*(e(v)-EA)-g(v)),
    delta_B(v)=Delta*g(v)/(C*(EB-e(v))+g(v)),         (6)

when the respective denominator is positive; a nonpositive denominator
imposes no additional upper bound. Exact evaluation of the whole bank gives

    min delta_A = 9/28417 at (e,R)=(37/10,9/40),
    min delta_B = 1/23508 at (e,R)=(349/145,81/290).

The tail coefficients in (4),(5) are strictly positive at delta=1/23508,
and remain positive below it. Thus (4) proves G>=kA*x in the A-case, and
(5) proves G>=kB*(Delta-x) in the B-case. Every protocol falls into at least
one case, so it obeys the minimum of the two lower bounds. The realizations
in Section1 attain it. This proves (1), including arbitrary finite/countable
dimension, without a compactness argument or an assumed optimizer.

The first failed coefficient at1/23508 concerns an unshifted bad vertex in
this relaxation. It does not prove that the corresponding physical component
can realize equality alongside the exceptional contact. Treating this
certificate limit as a new phase transition would be an overclaim.

## 4. Equality and sharp physical dimension

Take 0<delta<1/23508 and EA<E<EB. Every positive-defect coefficient in
(4),(5) is strictly positive; the same holds for the tail coefficients.
Equality therefore forces z_v=q=vtail=ell=0. It also forces equality in
the applicable offset bound. In the A-case all A mass is at offset0 and all
B mass at offset delta; in the B-case the offsets are reversed. Both types
have positive mass in the winning branch. Distinct components cannot share
the same physical root, so exactly one populated component of each type
remains. A single component cannot mix both endpoint types because their
orientations are incompatible. Energy fixes the mass uniquely.

Below the switch there is exactly the A-low placement; above it exactly
the B-low placement; at the switch both placements attain the same return.
This classifies optimizing diagonals up to extra unoccupied physical levels
and nonunique channel implementations, not all channels themselves.

Within each endpoint every odd input1,3,5,7,9 is populated. Adjacent inputs
share shells with two incoming states, which require four distinct outgoing
bath/catalyst states. Those shells force each physical level0,...,10.
Fractional levels cannot replace an integer shell partner. Different offset
components have disjoint completions, hence22 is necessary and sufficient.
At E=EA or EB the appropriate single endpoint has dimension11, also minimal.
At delta=1/23508 formula (1) is proved, but the strict equality classification
and resource minimum are not asserted: an additional zero coefficient in
the relaxation requires separate analysis.

## 5. Second order, a moving switch, and failure of uniform second order

For a fixed E below the midpoint M=(EA+EB)/2, expansion of the exact first
branch gives

    F_delta(E)=L(E)+C*(E-EA)*delta/Delta
                         -C*(E-EA)*delta^2/Delta^2+O(delta^3).

Above M, the second-order coefficient is +C*(EB-E)/Delta^2. Exactly at M,
the first branch remains the winner for every positive delta, so the
coefficient is -C/(2*Delta). The second-order coefficient jumps across M.
The maximum excess over L is exactly C*delta/2, attained at the moving
switch M+delta/2.

There is no uniform expansion over the whole closed interval with this
fixed pointwise second-order coefficient and o(delta^2) remainder: the
normalized defects are continuous functions of E, whereas their proposed
uniform limit is discontinuous. This does not contradict K2039's uniform
first-order O(delta^2) remainder.

The transition layer is explicit. At E=M+theta*delta, subtract the first-order
term a(E)*delta with a(E)=C*min(E-EA,EB-E)/Delta and divide by delta^2.
For fixed real theta the limit is

    (C/Delta)*clamp(2*theta-1/2, -1/2, 1/2).          (7)

It joins the two outer coefficients continuously on 0<=theta<=1/2.
This follows directly by inserting x=Delta/2+theta*delta into (1), not by
fitting sampled spacings. It settles the second-order question at fixed
energy and identifies the precise obstruction to a uniform fixed coefficient.

## 6. A genuine larger-spacing rival, separate from certificate failure

The first candidate check tried the previous nine-level endpoint
D=(54,81,9,1)/145 at (ED,RD)=(349/145,81/290), shifted above unshifted B,
immediately beyond1/23508. It did NOT improve the original construction.
That failed attempt is preserved: it demonstrates why a failed support
coefficient alone is not a physical counterexample.

The actual comparison of these two physical rays has threshold

    delta_rival=2/181.

At that value (RA-RB)/(EB-EA-delta)=(RD-RB)/(EB-ED-delta).
Above it, the shifted-D/unshifted-B construction gives smaller return than
the shifted-A/unshifted-B ray on their common energy interval. At delta=4/181
and E=(EA+3EB)/4 it also beats the minimum of the two original A/B rays.
The exact rational20-level witness is in the machine record and physically
replayed by the separate checker. Thus the A/B formula cannot hold for every
spacing below1/2. Neither2/181 nor1/23508 is claimed to be the FIRST physical
transition; the intervening optimum remains open.

## 7. Verification, scope, and continuation

The producer evaluates all3137 vertex coefficients, strict tail coefficients
and the offset identities. A separate checker reconstructs every vertex's
return from physical bath-label maxima, checks18 full separated protocols,
removes each of the22 endpoint completion levels to test necessity, and
replays the20-level rival with normalization, energy, spacing and capacity.
Four clean-baseline faults change the certificate range, endpoint return,
rival mass and rival return. The endpoint-return mutation initially escaped
because no direct endpoint comparison was present; that check was repaired
and the clean baseline and all faults were rerun. This failure was not counted
as detection.

Completeness of the inherited arrangement and the erasure theorem are pinned
K2037/K2039 evidence; this run newly checks all bank values and the changed
proof transfer, not the original census generator. The countable conclusion
rests on the nonnegative first-moment argument in (2)-(5). Equality, the
second-order limits and sharp dimensions have the explicit proofs above.
Internal distinct implementations and same-author hostile review are not
external review, proof-assistant certification or a novelty claim.

The next thermal question is the actual first spacing transition or a larger
exact interval using chamber-aware offsets; a relaxed bad vertex is not yet
a realizable competitor. Near5/4 resource necessity and exact capped-wing
continuum marginals remain substantive alternatives. Source and physics
ledger verdicts remain unchanged.
