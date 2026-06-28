---
title: "Research Posture"
status: canon
doc_type: canon
updated_at: "2026-06-24"
---

# Research Posture

This repository is a Geometric Unity reconstruction program.

The working hypothesis is:

```text
Geometric Unity is substantially correct, and the task is to determine whether
that hypothesis can be rigorously reconstructed, extended, or falsified through
systematic mathematical research.
```

This is a research hypothesis, not a proof claim. It does not say that GU has already been
proved, that Eric Weinstein's existing presentation is complete, or that every current
reconstruction in this repository is correct.

## Primary research question (2026-06-28): the Firewall-Boundary Hypothesis

The repository's PRIMARY falsification target is now whether every successful reconstruction
converges on a firewall-like BOUNDARY object (a constrained boundary condition / adapter at which
the geometry terminates) rather than on a CLOSED internal completion. This supersedes the prior
default that the correct endpoint of the reconstruction must be a closed mathematical system; that
default is now itself on trial. The hypothesis is to be ATTACKED, not defended. Full statement,
explicit falsification criteria, and current evidence status: `canon/firewall-boundary-hypothesis.md`.

## Optimization Target

The repository optimizes for discovering whether the GU hypothesis is true.

It should not optimize mainly for appearing maximally conservative, neutral, or
peer-review-safe. Caution is useful only when it improves truth-tracking. The primary
question for future work is:

```text
If GU is fundamentally correct, what mathematical structures must exist,
and how do we discover them?
```

That means future work should be constructive as well as critical:

- propose new mathematical objects when existing ones are insufficient;
- search aggressively for class exits, stronger categories, and richer formulations;
- treat low-confidence but high-information directions as legitimate if they are precise;
- kill failed directions cleanly when their assumptions, computations, or reductions fail.

## Discipline Does Not Weaken

The hypothesis is bolder than a neutral map. The standards are not weaker.

Every live mathematical or physical claim still needs:

- explicit assumptions;
- reconstruction/proof/speculation labels;
- falsification or rollback conditions;
- dependency tracking;
- correction logs when verdicts change;
- promotion criteria before canon claims;
- independent verification where feasible;
- no-go theorem assumption audits.

The correct posture is:

```text
Assume the hypothesis is worth pursuing.
Demand that every mathematical step earn its place.
```

## Mission A: GU Reconstruction Program

Mission A is primary.

Assume GU is substantially correct as a working hypothesis. Attempt to reconstruct:

- the missing mathematics;
- the missing derivations;
- the missing physical reductions;
- the missing categorical language;
- the missing analytic machinery.

Known objections should be treated as one of three things:

- an obstruction to overcome by a stronger construction;
- an obstruction to formalize as a precise theorem-class boundary;
- a genuine falsifier of the GU hypothesis or of a specific GU reconstruction branch.

The objective is not defending GU. The objective is discovering whether a rigorous
reconstruction exists.

## Mission B: Independent Mathematical Contributions

Mission B is secondary but valuable.

Some tools developed here may survive independently of GU. Examples include:

- the signed-readout theorem;
- the no-go class-relative framework;
- the six-axis specification protocol;
- reusable reconstruction methodology;
- substrate-versus-shadow analysis;
- other mathematical machinery that remains useful even if a GU branch fails.

These outputs should continue to be developed and published on their own merits. They are
not the primary purpose of this repository.

## Priority Rule

Do not confuse confidence, evidence, importance, and expected value.

A direction can have low confidence and high expected value if it would strongly clarify
the central GU hypothesis. Such directions are worth investigating when they are
mathematically well specified and have clear failure conditions.

A direction can also be elegant, clean, and publishable while doing little to decide
whether GU succeeds. Those directions may belong under Mission B, but they should not crowd
out Mission A.

Research priority should optimize for information gain about the GU reconstruction
hypothesis.

## Constructive Obstruction Protocol

When a derivation blocks, do not stop at:

```text
This blocks the current derivation.
```

Ask:

- What mathematical object would remove this obstruction?
- What stronger structure would make this theorem applicable?
- Is the obstruction intrinsic, or only relative to the current formulation?
- Can the hypothesis be reconstructed inside a richer category?
- What invariant would have to exist if GU were true?
- What computation would distinguish construction from rescue?

The answer may still be failure. A precise failure is progress.

## Guardrails

Do not become advocates.

Forbidden moves:

- inflate verdicts;
- call compatibility a derivation;
- rescue failed arguments through optimism;
- redefine failures as successes;
- hide imported target data inside a reconstruction;
- treat process discipline as physics evidence.

## Success Criterion

The repository succeeds if it converges toward either:

1. a rigorous mathematical reconstruction that genuinely derives new physics from GU; or
2. a precise mathematical explanation of why such a reconstruction cannot exist.

Both outcomes are scientific successes.

The failure mode is optimizing for caution, appearance, or local elegance instead of
maximizing the ability to learn whether GU is true.

## Machine-Readable Posture

```json
{
  "artifact": "RESEARCH_POSTURE",
  "version": "2026-06-24",
  "primary_mission": "GU_RECONSTRUCTION_PROGRAM",
  "working_hypothesis": "Geometric_Unity_is_substantially_correct_and_should_be_reconstructed_extended_or_falsified_systematically",
  "not_claims": [
    "GU_already_proved",
    "existing_GU_presentation_complete",
    "current_reconstructions_all_correct"
  ],
  "optimization_target": "information_gain_about_whether_GU_is_true",
  "mission_a": {
    "name": "GU Reconstruction Program",
    "priority": "primary",
    "stance": "assume_GU_substantially_correct_as_working_hypothesis",
    "outputs": [
      "missing_mathematics",
      "missing_derivations",
      "missing_physical_reductions",
      "missing_categorical_language",
      "missing_analytic_machinery"
    ]
  },
  "mission_b": {
    "name": "Independent Mathematical Contributions",
    "priority": "secondary",
    "examples": [
      "signed_readout_theorem",
      "no_go_class_relative_framework",
      "six_axis_specification_protocol",
      "reconstruction_methodology",
      "substrate_shadow_analysis"
    ]
  },
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
    "advocacy",
    "verdict_inflation",
    "compatibility_as_derivation",
    "optimistic_rescue_of_failed_arguments",
    "failure_redefined_as_success",
    "target_data_hidden_as_reconstruction"
  ],
  "success_criteria": [
    "rigorous_GU_reconstruction_deriving_new_physics",
    "precise_explanation_of_why_GU_reconstruction_cannot_exist"
  ]
}
```
