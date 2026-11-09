# GU Formalization contributor instructions

This public repository owns Geometric Unity / Observerse research truth:
claims, grades, derivations, corrections, exact computations, proof artifacts,
source records, papers, and branch-relative current state.

## Start here

0. **Research priority.** Read `program_focus` at the top of
   `CURRENT-STATE.yaml` first and follow its `run_selection` exactly. Write
   the preflight fields (target, tier, expected delta, kill condition) before
   doing any work, and the postflight fields after. Every run names a matrix
   cell, intersection, bet or LB-CLASS task as its target; work not attached to a
   target is out of scope, and step 5 of `run_selection` always supplies one,
   so this never authorizes zero work. External
   review is not a pathway in this program: do not propose it, plan for it or
   wait on it. Older steering text in NEXT-STEPS, RESEARCH-STATUS and the
   agenda's `latest_result_*` keys is history, not instruction.
1. Read `GEOMETER-VS-PHYSICS-OBJECTS.md` before identifying same-named
   geometric and physics constructions.
2. Before reading particle-physics verdicts in `CURRENT-STATE.yaml`, read
   `lab/methods/source-native-comparator-routing.md`. For Higgs/VEV,
   family-index, chirality, Majorana/126, anomaly, symmetry-breaking or
   vector-mass reasoning, also read the source-native pointers it names. A
   conventional comparator binds only the conventional model it states. It is
   not evidence against Weinstein's source-native mechanism, may not move a
   hypothesis vote or
   become the default successor, and may be reused only after an explicit
   typed bridge is proved. New or materially revised comparator artifacts must
   carry the routing notice required by that method and be registered in
   `lab/process/source-native-comparator-routing-registry.json`.
3. Read `CURRENT-STATE.yaml` for the branch-relative result, evidence, exact
   next condition, contribution path, and `what_needs_joe`.
4. Read `lab/specifications/six-axis/six-axis-template.md`; Layer 0 semantic
   alignment precedes L1--L7.
5. Follow `RESEARCH-POSTURE.md`, `VERIFICATION.md`, and `CONTRIBUTING.md`.

## Scientific integrity

- Preserve the distinction among source-confirmed, repository-derived,
  reconstructed, conditional, speculative, negative, and open claims.
- Never infer a count from a multiplicity or decomposition without the required
  index/grade map.
- State the carrier, pairing or form, real structure, grading, action owner,
  target object, assumptions, controls, and claim ceiling for a new result.
- A null or kill read from finite differences is not citable until certified
  analytically, exactly, by interval arithmetic, or by another stated rigorous
  bound.
- Preserve negative results, counterexamples, superseded routes, and correction
  history. Apply `lab/methods/claim-status-consistency.md` to status changes.
- Before writing a verdict about a registered claim, apply
  `explorations/claim-indexed-verdict-doctrine-2026-08-12.md`. Never say a
  critic, critique, or objection is "correct" or "sound" without binding that
  judgment to the exact object analyzed; a correct computation on one object
  does not settle a differently scoped claim.
- Before assuming a fork horn or citing a blocker, check
  `lab/process/path-dependencies.md` for a chain covering it.
- New findings do not promote themselves to `canon/` or `CANON.md`. A later
  independent verification must check both the result and proposed wording.
- No publication, account action, submission, or other external effect occurs
  without the maintainer's exact authorization.

## Standing independent review request

For routine scientific acceptance, the maintainer explicitly requests and
authorizes read-only specialist subagents with relevant mathematical or physical
expertise to independently review concrete candidate results. This standing
request does not require renewed chat approval for each review. Review depth
follows `program_focus.review_tiers`: Tier 1 (decides a matrix cell, moves a
ledger row, changes class C, or is a kill) gets two specialists, one hostile
reviewer and a Lean check; Tier 2 (lane-C results, newly constrained cells)
gets one specialist; Tier 3 (scaffolding, probes, bookkeeping) gets exact
probes and gates only. Reviewers load
the applicable source-native prerequisites above, challenge the strongest
overclaim and counterconstruction, and inspect the weakest reproducibility seam.
They do not edit owner truth, change governance, or take external actions; the
lead agent integrates findings and serializes local verification.

Permission to review is not acceptance. Keep a candidate provisional until its
required independent review and native checks pass; internal agent review is
not external-expert or proof-assistant certification. An unavailable review
restricts acceptance and claims that depend on it, not safely separable research.

## Repository boundary

The repository contains only native research truth and the procedures needed
to interpret, reproduce, validate, critique, and contribute to it. Research
priority and work eligibility are set in-repo by `program_focus` and the
method contract. Scheduling, orchestration, model choice, private review
composition, and service history are external and are not authority for a
scientific claim.

## Validation and durability

Run the narrow exact probes named by the affected artifact, the relevant
`process_gates/` checks, and `git diff --check`. Keep scratch and generated
caches in `_local/`. A coherent authorized change is committed and pushed to
the current branch only after native validation passes.
