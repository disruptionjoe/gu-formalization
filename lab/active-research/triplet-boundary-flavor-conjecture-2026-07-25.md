---
title: "Triplet--Boundary--Flavor Conjecture"
date: "2026-07-25"
status: active_research
doc_type: staged_conjecture
claim_id: GEN-TBF-01
verdict: "OPEN_GATED; TRIPLET_LOCATED; PHYSICAL_SELECTION_AND_FLAVOR_DERIVATION_OPEN"
owned_path: "lab/active-research/triplet-boundary-flavor-conjecture-2026-07-25.md"
depends_on:
  - "VERIFICATION.md"
  - "GEOMETER-VS-PHYSICS-OBJECTS.md"
  - "canon/leg3-closure-and-spinor-2smoothness.md"
  - "canon/families-e-invariant-order3-monodromy-RESULTS.md"
  - "canon/two-primary-lemma.md"
  - "explorations/generation-sector/ten-lens-three-generation-mechanism-synthesis-2026-07-25.md"
---

# Triplet--Boundary--Flavor Conjecture

## Conjecture

Four-dimensional self-dual geometry supplies a canonical triplet carrier; a
separately derived boundary/source-action spectral mechanism selects one
chiral, physically accessible sector from each mirror pair; and symmetry
breaking plus renormalization-group dynamics differentiates the surviving
sectors into the observed masses and mixings.

This is a staged research conjecture. It is not a derivation of three
generations and does not change the standing generation-count verdict.

## Why it is frontstage

The conjecture packages three questions that prior generation work often
collapsed:

| gate | question | present grade |
|---|---|---|
| `TBF-A — carrier` | Why is there a natural triplet representation? | structurally located in the self-dual `SU(2)_+` / `Lambda^2_+` route |
| `TBF-B — physical selection` | Why do three protected chiral/light/access-enabled families survive the vectorlike carrier? | open; load-bearing |
| `TBF-C — differentiation` | Why do the survivors have the observed masses and mixings? | open; downstream |

The current carrier `3E_+ + 3E_- + X` is vectorlike. Representation dimension
three does not imply net chiral count three. A bare `Z/3` class does not imply
an integer count because `Hom(Z/3,Z)=0`. The conjecture is frontstage because
it makes those missing implications explicit and targetable.

## Promotion boundary

Promotion to `active_research` means only:

1. the three-stage decomposition is now an owned, frontstage research object;
2. its assumptions, proof targets, controls, and failure modes are explicit;
3. agents should not report success at `TBF-A` as closure of `TBF-B` or
   `TBF-C`; and
4. the next action is the target-blind construction of the source-action
   spectral packet below.

It does **not** promote the conjecture to canon, theorem, prediction,
scientific verdict, paper seed, or current Lane-1 priority.

## Required proof packet

```text
OrderThreeSourceActionSpectralPacket_V0 =
  (physical_carrier,
   source_action,
   order_three_action,
   operator_and_domain,
   grading_and_real_structure,
   fredholm_or_APS_certificate,
   equivariant_rho_or_eta,
   independent_integer_observable,
   pairing_map,
   target_blind_controls)
```

Every field must be supplied by one coherent physical construction. An
equivariant invariant computed on a proxy operator cannot be silently moved to
GU's physical carrier.

## Target-blind return contract

The packet must be able to return:

| return | meaning |
|---|---|
| `SOURCE_ACTION_UNDEFINED` | no physical source action has been constructed |
| `ACTION_DEFINED_OPERATOR_UNDEFINED` | source data exists but does not determine a valid operator/domain |
| `SPECTRAL_CLASS_ZERO` | the fine order-three spectral class vanishes |
| `INTEGER_PAIRING_UNDEFINED` | no lawful bridge to an independently defined integer count exists |
| `INTEGER_COUNT_NONTHREE` | the construction returns an integer other than three |
| `THREE_TARGET_IMPORTED` | three entered through a chosen flux, rank, normalization, threshold, or completion |
| `THREE_VECTORLIKE_ONLY` | multiplicity three exists but net chirality remains zero |
| `THREE_CHIRAL_DERIVED` | a protected integer-three chiral count follows without target import |

Only the final return advances `TBF-B`, and even then it does not establish
`TBF-C`.

## Assumptions that must remain visible

1. the physical real form, compact/complexified carrier, Krein structure, and
   grading are typed rather than interchanged;
2. the order-three action is source-owned and exists before its spectral value
   is inspected;
3. Fredholm, APS, boundary, or end conditions are physical parts of the
   construction rather than free tuning knobs;
4. the integer observable is independently meaningful as a physical chiral or
   accessible-family count;
5. observer access or regional certification may characterize selection but
   cannot substitute for the missing operator; and
6. flavor parameters and resource budgets are frozen before held-out
   phenomenology is evaluated.

## Failure modes

- representation multiplicity is reported as physical family count;
- order-three torsion is reported as integer three;
- K3 arithmetic is divided by a chosen generation unit;
- flux, rank, boundary condition, threshold, or code dimension is fixed to
  three after the target is known;
- a positive-Hilbert or compact proxy is substituted for the physical
  split-signature/Krein problem without a transport theorem;
- mirrors are declared inaccessible without an interventionally complete
  access/capability model;
- a general Yukawa matrix is presented as a flavor derivation; or
- one failed formalization is mistaken for exhaustion of the staged
  conjecture.

## Kill conditions

`TBF-B` is closed negative if a construction-class no-go proves that every
admissible source-owned operator on the physical carrier has zero net chiral
index, or that every natural order-three refinement has zero/nonintegral
pairing with every independently justified count.

The integrated conjecture is also closed negative if integer three can arise
only through target-selected inputs, or if the triplet carrier is physically
idle in every complete intervention class.

## Next action

Use
`conditional-source-action-toy-construction-program-2026-07-26.md` as the
graded build ladder. First complete the finite coefficient-class enumeration,
then construct the imposed-wall control and dynamical-wall comparator, and
only then attempt the regulator and program-native lift. These toys may
establish conditional hosting, dynamic physical selection, or a transport
obstruction; they do not become GU's source action merely by reproducing the
target.

The eventual target remains
`OrderThreeSourceActionSpectralPacket_V0` from the actual GU source-action and
B5 operator/domain campaign. Do not begin with a desired `rho`, `eta`, flux,
rank, K3 quotient, or count. The cheapest informative result is a well-typed
`UNDEFINED`, `ZERO`, `NONTHREE`, `TARGET_IMPORTED`, or transport-failure return
because each removes a large class of false closures.

## Promotion-criteria audit

| criterion | result |
|---|---|
| clear scope | yes: carrier, selection, and differentiation are separately typed |
| proof/falsification target | yes: the source-action spectral packet and its return contract |
| explicit assumptions | yes: physical carrier, action, domain, index, count, and flavor budget |
| known failure modes | yes: target import, proxy substitution, vectorlike conflation, and unrestricted flavor fit |
| executable next action independent of hidden work artifacts | yes: construct the missing public-repository scientific object; no private artifact is load-bearing |
| stale stronger wording removed or superseded | yes at promotion: generation count remains `OPEN / located-not-forced`; no canon or verdict surface is strengthened |
