---
title: "Research Posture"
status: canon
doc_type: canon
updated_at: "2026-06-28"
---

# Research Posture

## North star: find the truth, using a bold conjecture as the engine

This program optimizes for one thing: **discovering what is true** about the mathematics and physics in
its reach. It is not a campaign to prove Geometric Unity, to disprove it, to vindicate or refute Eric
Weinstein, or to make this program look right or wrong. Those are all the wrong target.

Geometric Unity is the **guiding idea**, and it earns that role precisely because it is a bold, high
-information, contested claim. Bold conjectures of this kind are the ones that, when they pay off, move
science in leaps rather than increments; and even when they do not pay off whole, interrogating them
surfaces real structure. GU is a strong, arguably scientifically irresponsible claim from an obviously
capable thinker, and the community genuinely disputes whether it is even well posed. That is exactly what
makes it a good **generative test case**: it is rich enough to spawn precise, falsifiable hypotheses, and
contested enough that resolving them teaches us something either way.

So the method is: take GU as the provocation, manufacture **falsifiable hypotheses** from it, drive each
one to a verdict (survives re-checking, or is killed), and keep only what survives. The surviving
structure is frequently **GU-independent** -- representation-theoretic, index-theoretic, no-go-structural
facts that stand on their own once GU has done its job of pointing at them. That is a feature, not a
disappointment: the scaffold is allowed to fall away.

```text
We do not optimize to prove GU, to disprove GU, or to adjudicate anyone.
We optimize to find what is true, using GU as the engine that generates the questions.
```

## Two products, of equal standing

1. **True structure.** Whatever mathematical or physical structure survives the falsification drive,
   reported at its honest grade (proof / reconstruction / evidence / speculation), GU-dependent or not.
   The GU-independent results are often the strongest, because they do not require anyone to buy GU.
2. **A reliable truth-seeking method.** The discipline itself -- bold conjecture, falsifiable hypotheses,
   adversarial verification, clean kills, keep-what-survives -- is a deliverable. (Process discipline is
   never offered as physics evidence; it is offered as method.)

Neither product is "a verdict on GU." A verdict on GU (true, false, or a precise boundary explaining why a
reconstruction can or cannot exist) is a possible *byproduct*, and every such byproduct is a scientific
success. None of them is the goal.

## Current lead hypotheses (the questions GU is generating now)

These are hypotheses under active drive, to be ATTACKED not defended. They are instruments, not commitments:

- **The Firewall-Boundary Hypothesis** -- whether a successful reconstruction converges on a constrained
  boundary / interface object rather than a closed internal completion. Full statement and falsification
  criteria: `canon/firewall-boundary-hypothesis.md`.
- **The matter / generation-multiplicity line** -- what GU's Rarita-Schwinger sector does and does not fix
  about generation count and chirality. Current state: a native multiplicity-3 exists (H1) but is vectorlike
  and kinematically un-chiralizable (T1a); the self-dual route is canonical (H3) and the only odd route
  (M3); the chiral count is one specified missing ingredient. See `canon/ghost-parity-krein-synthesis.md`,
  `canon/leg3-closure-and-spinor-2smoothness.md`, and the prepublish tracker.

When a lead hypothesis is resolved, it is retired and the truth it surfaced is kept; the program does not
become attached to any one of them.

## Discipline does not weaken

The conjecture is bold; the standards are not lower. Every live claim still needs: explicit assumptions;
reconstruction / proof / speculation labels; falsification or rollback conditions; dependency tracking;
correction logs when verdicts change; promotion criteria before canon; independent verification where
feasible; no-go-theorem assumption audits.

```text
Take the conjecture seriously enough to attack it precisely.
Demand that every mathematical step earn its place.
Keep only what survives the attack.
```

## Constructive obstruction protocol

When a derivation blocks, do not stop at "this blocks." Ask: what object would remove the obstruction?
what stronger structure would make the theorem applicable? is the obstruction intrinsic or only relative to
the current formulation? what invariant would have to exist if the conjecture were pointing at something
real? what computation distinguishes a genuine construction from a rescue? A precise failure is progress.

## Guardrails

Do not become advocates -- for GU, against GU, or for this program. Forbidden moves: inflate verdicts; call
compatibility a derivation; rescue failed arguments through optimism; redefine failures as successes; hide
imported target data inside a reconstruction; treat process discipline as physics evidence; and -- the
guardrail this revision adds -- frame the work as adjudicating GU or anyone, rather than as finding the
truth GU helps us reach.

## Success criterion

The program succeeds when it converges on true structure (at honest grade) and a method that reliably finds
it. Whether that structure vindicates GU, falsifies a GU branch, or turns out to be GU-independent is not
the measure of success; the truth and the method are. The failure mode is optimizing for caution,
appearance, local elegance, or for any verdict, instead of for what is true.

## Machine-readable posture

```json
{
  "artifact": "RESEARCH_POSTURE",
  "version": "2026-06-28",
  "north_star": "find_the_truth",
  "optimization_target": "true_structure_and_a_reliable_truth_seeking_method",
  "guiding_conjecture": {
    "name": "Geometric_Unity",
    "role": "generative_test_case",
    "rationale": "bold_high_information_contested_conjecture_that_spawns_falsifiable_hypotheses",
    "not_the_goal": true
  },
  "not_targets": [
    "prove_GU_true",
    "prove_GU_false",
    "vindicate_or_refute_Weinstein",
    "make_this_program_look_right_or_wrong",
    "any_verdict_as_an_end"
  ],
  "method": [
    "take_bold_conjecture_as_provocation",
    "manufacture_falsifiable_hypotheses",
    "drive_each_to_a_verdict",
    "adversarially_verify",
    "kill_cleanly",
    "keep_only_what_survives_often_GU_independent"
  ],
  "products": [
    "true_structure_at_honest_grade",
    "reliable_truth_seeking_method"
  ],
  "byproducts_all_successes": [
    "GU_reconstruction_deriving_new_physics",
    "precise_explanation_why_a_reconstruction_cannot_exist",
    "GU_independent_mathematics"
  ],
  "discipline_preserved": [
    "explicit_assumptions",
    "falsification_conditions",
    "reconstruction_vs_proof_labeling",
    "correction_logs",
    "dependency_tracking",
    "promotion_criteria",
    "independent_verification",
    "no_go_assumption_audits"
  ],
  "forbidden_moves": [
    "advocacy_for_or_against_GU",
    "verdict_inflation",
    "compatibility_as_derivation",
    "optimistic_rescue_of_failed_arguments",
    "failure_redefined_as_success",
    "target_data_hidden_as_reconstruction",
    "process_discipline_as_physics_evidence",
    "framing_work_as_adjudicating_GU_rather_than_finding_truth"
  ]
}
```
