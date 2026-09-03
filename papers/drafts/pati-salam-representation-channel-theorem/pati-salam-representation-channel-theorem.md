---
title: "A Pati-Salam Representation-Channel Theorem for the Adjoint Square"
author: "Joseph Hernandez"
status: draft
document_role: draft
operational_state: working
claim_verdict: exact
updated_at: "2026-09-02"
---

# A Pati-Salam Representation-Channel Theorem for the Adjoint Square

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

The Pati-Salam background restriction remains a scoped comparator inside that
representation-grade route.

~~~gu-typed-objects
result: PATI-SALAM-REPRESENTATION-CHANNEL-THEOREM
carrier: paired-real family spinor F_R from 16+ plus 16-, paired-real gamma-kernel partner Z_R from 144+ plus 144-, and the internal adjoint A_R=so(6,4), after complexification to the frozen D5 support tables
pairing: conjugate-paired multiplicity-one 45 lines at cubic order and common-irrep intersections of F tensor Z with Sym^2(A) or Lambda^2(A) at quadratic-adjoint order
real_structure: Spin(6,4) conjugation exchanges the plus/minus complex halves and pairs the two same-label cubic lines; neither complex line alone is promoted to the real coupling
grading: polynomial degree in the internal adjoint insertion; the source field remains an ad-valued one-form, so internal tensor symmetry does not select the one-form-leg contraction
action_owner: source-print owns only the connection/operator grammar; repository construction owns the representation support theorem; coefficient, contraction, background and physical operator remain source/action unowned
target: MAP-TYPE exact finite representation theorem separating symmetric 54/210 Pati-Salam owners from alternating 45/945 non-owners without physical instantiation
~~~

## Abstract

The same-label D5 product of the family 16 and gamma-kernel partner 144 has
multiplicity-one support

    45 + 54 + 210 + 945 + 1050.

The exact adjoint-square decompositions are

    Sym^2(45)     = 1 + 54 + 210 + 770,
    Lambda^2(45) = 45 + 945.

Their intersections therefore split exactly into symmetric owners 54 and 210
and alternating owners 45 and 945. Under the held Pati-Salam restriction
counts, 54 and 210 each have one singlet while 45 and 945 have none. Thus the
first quadratic-adjoint Pati-Salam-preserving representation channels are
exactly the symmetric 54 and 210 channels; the alternating square supplies no
such owner. The same data also preserve a cubic adjoint-45 channel while
obstructing a nonzero linear Pati-Salam-preserving adjoint background.

This is an exact theorem about frozen representation supports and
multiplicities. It neither chooses between the two symmetric channels nor
constructs the source coefficient, one-form contraction, family covector,
stationary background, physical vertex, mass, observed sector, or prediction.

## Frozen objects and premises

Let F denote one complex 16 half and Z the same-label complex 144 half. Let A
be the complexified D5 adjoint 45 of the paired-real source carrier. The
complete antecedent is:

1. **Family/partner support.** F tensor Z has multiplicity-one support
   {45,54,210,945,1050}; it contains no scalar.
2. **Adjoint-square support.** Sym^2(A) has multiplicity-one support
   {1,54,210,770}, while Lambda^2(A) has support {45,945}.
3. **Pati-Salam counts.** The singlet multiplicities on
   (45,54,210,945,1050) are (0,1,1,0,0).
4. **Paired-real interpretation.** The plus and minus same-label complex
   products each contain one 45, and real conjugation pairs those two lines.
5. **Source typing.** The actual connection perturbation is an element of
   Omega^1(Y,ad P). The internal adjoint calculation does not erase or contract
   its one-form leg.
6. **Nonselection boundary.** No source-owned coefficient, symmetric versus
   alternating form-leg contraction, family covector, stationary background,
   physical operator, observation map or observable is supplied.

Premises 1–4 are the already-owned exact Q5/HE-4/adjoint-square results.
Premises 5–6 state the type and ownership boundary needed to prevent
representation availability from becoming a physical interaction claim.

## Theorem

**Pati-Salam representation-channel theorem.** Under premises 1–6:

1. F tensor Z intersects Sym^2(A) in exactly {54,210}, with multiplicity one
   for each owner.
2. F tensor Z intersects Lambda^2(A) in exactly {45,945}, with multiplicity one
   for each owner.
3. The Pati-Salam-fixed subspace has multiplicity one in each symmetric owner
   54 and 210 and multiplicity zero in both alternating owners 45 and 945.
   Therefore exactly two quadratic-adjoint Pati-Salam-preserving
   representation owners occur, both in the symmetric channel.
4. The cubic internal adjoint channel is available, but its adjoint 45 has no
   Pati-Salam singlet. Hence a nonzero linear Pati-Salam-preserving adjoint
   background cannot activate that channel.
5. Representation support supplies no unique quadratic owner, relative
   coefficient, family, source-action vertex or physical consequence.

## Proof

By premise 1 and premise 2,

    {45,54,210,945,1050} intersect {1,54,210,770}
      = {54,210},

and

    {45,54,210,945,1050} intersect {45,945}
      = {45,945}.

Every displayed constituent has multiplicity one in its parent support, so
the common constituents have multiplicity one. Premise 3 assigns one
Pati-Salam singlet to 54 and 210 and none to 45 or 945. Filtering the two
intersections by positive singlet multiplicity therefore gives {54,210} and
the empty set respectively. This proves statements 1–3.

The cubic internal invariant factors through the multiplicity-one adjoint 45
inside each same-label 16 tensor 144 product. Premise 4 pairs the conjugate
complex lines into the real coupling space. But premise 3 gives no
Pati-Salam-fixed vector in 45, proving statement 4.

Finally, the two symmetric owners are distinct multiplicity-one lines. Their
existence defines a two-channel allowed space; it does not define a preferred
nonzero vector in that space or a relation between its coefficients. Equivalent
family copies carry the same allowed space and are not distinguished by these
representations. Premises 5–6 also retain the one-form leg and withhold every
map required to instantiate a source or physical operator. Statement 5
follows. ∎

## Preflight, prior art, and route choice

Object-level retrieval preceded construction. The 2026-08-31 source-native
adjoint/144 exploration already derived the degree ladder. Q5 owns the
multiplicity-one D5 summands, HE-4 owns the Pati-Salam counts, the upstream
Python probe recomputes both adjoint squares from the exact weight character,
and SourceNativeAdjointCoupling.lean checks the finite intersection theorem
from supplied supports. This package contributes the self-contained theorem,
premise/reopener ledger, independent composition certificate and reproduction
boundary; it does not claim a new decomposition calculation.

The structural route dominates a broad matrix or Clebsch search because the
question is support and singlet multiplicity. Clebsch normalization becomes
load-bearing only for a coefficient-complete action term. A conventional 126
VEV route is a different object and is unnecessary here. The source-native
connection one-form remains explicit throughout.

## Hostile review

**Strongest overclaim.** “The 54 or 210 generates a Pati-Salam-preserving mass.”
Refused. The theorem proves only that two representation owners are available.
It supplies neither owner selection nor a nonzero coefficient, background,
physical vertex, observation map, spectrum or mass.

**Strongest contrary construction.** A source equation may select an
alternating form-leg contraction, a different barred/unbarred pairing, or a
coefficient relation not represented by the bare internal product. Such a
construction would reopen the physical application. It does not change this
finite theorem unless it changes one of the frozen supports or singlet counts.

**Strongest mistyping risk.** Symmetric versus alternating here refers to the
two internal adjoint factors. The source fields also carry one-form legs. No
identification between internal symmetry and the physical wedge/contraction is
made.

**Weakest reproducibility seam.** The independent certificate freezes the
upstream decomposition tables instead of recalculating weight characters. The
capsule therefore reruns the character-based upstream probe and the existing
Lean intersection kernel. Neither certificate constructs Clebsch coefficients.

## What this settles—and what it does not

The package settles the requested exact split: 54 and 210 are precisely the
symmetric quadratic owners with Pati-Salam singlets; 45 and 945 are precisely
the alternating common owners and have none. It also makes the nonselection
content explicit: channel availability is not coefficient or family
selection.

It does not construct equation 9.16, choose a source-action term, contract the
one-form legs, normalize a Clebsch map, select a family or owner, produce a
stationary background, derive symmetry breaking or vector mass, classify an
observed sector, predict a scale or threshold, confirm or falsify Geometric
Unity, or promote a publication candidate.

## Reproduction

Run:

~~~sh
python3 papers/drafts/pati-salam-representation-channel-theorem/reproduce_all.py
~~~

The integrated certificate runs its clean baseline before ten hostile premise
mutations, then the capsule reruns the upstream character calculation and Lean
kernel.
