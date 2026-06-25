---
title: "Hourly 20260625 0502 Cycle 1 Oxford Portal Exact Source Locator Execution"
date: "2026-06-25"
run: "hourly-20260625-0502"
cycle: 1
lane: 1
doc_type: oxford_portal_exact_source_locator_execution
artifact_id: "OxfordPortalExactSourceLocatorExecution_V1"
verdict: "BLOCKED_ZERO_ACCEPTED_PRIMARY_SOURCE_RECEIPTS"
owned_path: "explorations/hourly-20260625-0502-cycle1-oxford-portal-exact-source-locator-execution.md"
companion_audit: "tests/hourly_20260625_0502_cycle1_oxford_portal_exact_source_locator_execution_audit.py"
---

# Hourly 20260625 0502 Cycle 1 Oxford Portal Exact Source Locator Execution

## 1. Verdict

Verdict: **blocked**.

The official Oxford/Portal surfaces are accessible and contain timestamped
formal-adjacent GU locators. They do **not** promote any exact locator into an
accepted `PrimarySourceReceiptInstance_V1` for the four blocked family objects:

| family | required object | execution decision |
|---|---|---|
| IG | `SourceForcedCodomainSelectorForK_IG` | no accepted receipt; projection/Shiab vocabulary does not source-force a codomain selector for `K_IG` |
| RS | `source.action_or_operator for d_RS,-1` | no accepted receipt; Rarita-Schwinger content is named, but no action/operator/Noether/BRST rule for `d_RS,-1` is emitted |
| QFT | `P_fin^b: F_phys^b(O) -> K_b` | no accepted receipt; no finite projector or finite extraction map is located |
| DGU/VZ | `operator_source_primary_action_or_EL for D_GU^epsilon 0/1` | no accepted receipt; swervature/displasion gives an equation-shaped positive locator, but not an actual `D_GU^epsilon` 0/1 action, operator, Euler-Lagrange equation, principal symbol, coefficients, or source certificate |

Current accepted receipts are zero. Proof restart remains blocked. No GU claim
is promoted.

## 2. What Was Derived Directly From Repo/Source Surfaces

Repo-derived constraints:

- `RESEARCH-POSTURE.md` permits constructive search but forbids turning
  compatibility, source-adjacent phrasing, or target imports into proof.
- `process/runbooks/five-lane-frontier-run.md` requires an exact verdict,
  exact obstruction, and next object rather than a summary-only note.
- `OxfordPortalReceiptMiningPacket_V1` had already established Oxford/Portal
  as the first official public surface to mine, but with zero accepted family
  receipts.
- `OxfordPortalExactLocatorBatch_V1` had specified the exact family query plan.
  This lane executed that plan against reachable official public pages rather
  than only preserving the batch specification.
- `RepoLocalPrimaryGUSourceReceiptMap_V1` already had all four Oxford/Portal
  rows at `accepted_receipt_count = 0` and `proof_restart_allowed = false`.
- `sources/media-index.md` identifies `GU-MEDIA-2013-OXFORD` as the primary
  public lecture surface and `GU-MEDIA-2020-PORTAL-SPECIAL` as the official
  release surface for the Oxford recording plus preface/post-lecture material.

Official source surfaces checked:

- `https://geometricunity.org/2013-oxford-lecture/`
- `https://theportal.group/a-portal-special-presentation-geometric-unity-a-first-look/`
- `https://geometricunity.org/`

The official Oxford page says the 2020 public video has three sections:
preface, lecture proper, and a supplementary PowerPoint presentation. It also
says the PowerPoint reviews the lecture's major concepts in more up-to-date
notation. That makes the page a valid exact-locator search surface.

## 3. The Strongest Positive Locator Or Construction Attempt

The strongest positive locator is the Oxford/Portal PowerPoint section
`GU Equations: Swervature and Displasion`, especially the timestamp range around
`02:35:10` to `02:36:12`.

Short locator evidence:

- Oxford official page, `02:33:43`: one "ship in a bottle (shiab) operator" is
  described, with many possible Shiab operators and a choice depending on the
  target contraction.
- Oxford official page, `02:35:10`: the swerved curvature is described as
  Shiab applied to the curvature tensor; the source says it generally "does not
  work out to be exact" as a Lagrangian differential.
- Oxford official page, `02:36:12`: the condensed equation is that swervature
  equals displasion, a replacement for Einstein equations on `Y` before pullback
  to `X`.
- Portal Group transcript, `02:40:19` to `02:41:16`: the Einsteinian
  replacement must be pulled back to `X`; Yang-Mills/Maxwell is described as
  coming from a Dirac square; the Dirac piece is deferred elsewhere and contains
  Rarita-Schwinger field content.

This is a real positive locator because it is source-native, timestamped, and
operator/equation-adjacent. It still fails receipt acceptance because the
required receipt object is not merely a named equation-shaped idea. For DGU/VZ,
the required object is an actual source primary action, operator, or
Euler-Lagrange object for `D_GU^epsilon` 0/1 with enough formula/rule content
to check identity. The locator does not provide that object.

The RS-positive locator is weaker but nonzero: Portal Group/Oxford around
`02:38:53` to `02:41:16` names Rarita-Schwinger/spin-3/2 content and says the
Dirac piece contains Rarita-Schwinger field content. It does not emit a
source-side differential, action, Noether identity, BRST operator, or quotient
operator for `d_RS,-1`.

No positive locator was found for `P_fin^b`. No positive locator was found for a
source-forced `K_IG` codomain selector, although Shiab/projection language
remains a discovery anchor.

## 4. The First Exact Obstruction Or Missing Proof/Source Object

The first exact obstruction is:

```text
No official Oxford/Portal locator inspected in this lane emits an exact
PrimarySourceReceiptInstance_V1 row with:
source kind, exact locator, exact fragment, source-emitted required family
object, emitted formula or rule, no target import, accepted routing, and family
identity check.
```

The obstruction is not public-page access. The official pages were reachable.
The obstruction is receipt-level content:

- IG blocks at `exact_locator_emitting_required_object`.
- RS blocks at `emitted_formula_or_rule`.
- QFT blocks at `exact_locator_emitting_required_object`.
- DGU/VZ blocks at `emitted_formula_or_rule` and then at
  `family_identity_check_to_D_GU_epsilon_0_1`.

The DGU/VZ attempted positive locator is especially useful because it is close
enough to prevent a vague "not searched" blocker. The searched source emits a
GU equation-shaped public description, but not the actual `D_GU^epsilon` 0/1
operator/action/EL source object required by the repository's current proof
gate.

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The next object is:

```text
OxfordPortalPrimarySourceReceiptInstanceCandidate_V1
```

It must be a row, not a narrative note. Minimum fields:

| field | requirement |
|---|---|
| `source_id` | one of `GU-MEDIA-2013-OXFORD`, `GU-MEDIA-2020-PORTAL-SPECIAL`, `GU-POD-2020-PORTAL-SPECIAL` |
| `exact_locator` | timestamp plus section heading or stable transcript anchor |
| `exact_fragment_short` | short source fragment only, not a long transcript excerpt |
| `family` | exactly one of `IG`, `RS`, `QFT`, `DGU_VZ` |
| `required_object` | one of the four blocked objects |
| `emitted_formula_or_rule` | a source-emitted formula, operator, action, EL equation, selector, projector, or differential rule |
| `target_import_excluded` | true |
| `family_identity_check` | explicit mathematical check against the required family object |
| `acceptance_status` | `accepted_for_routing` only if the emitted object and identity check both pass |

For the strongest DGU/VZ candidate, the constructive test is to capture the
image/formula attached to the `02:35:10` and `02:36:12` PowerPoint anchors and
ask whether the displayed equation contains enough formula data to instantiate
an operator/action/EL certificate. Transcript text alone is insufficient.

## 6. What This Means For The Relevant GU Claim

The Oxford/Portal execution leaves the GU reconstruction program exactly at the
receipt gate:

- It supports continued mining of Oxford/Portal as a source surface.
- It does not derive `K_IG`, `d_RS,-1`, `P_fin^b`, or `D_GU^epsilon` 0/1.
- It does not restart IG, RS, QFT, or DGU/VZ proof work.
- It does not close VZ evasion, finite QFT extraction, generation/rank claims,
  or any downstream physical recovery claim.

The claim-level consequence is narrow but important: source-native
operator/equation vocabulary exists on the official public surface, but the
repo still lacks an accepted source-emitted family object. Compatibility with
later reconstruction objects remains compatibility only.

## 7. Next Meaningful Source/Proof Computation Step

The next meaningful step is a visual/formula capture pass for the official
Oxford/Portal PowerPoint image anchors:

1. Capture the images adjacent to `02:33:43`, `02:35:10`, `02:36:12`,
   `02:38:53`, and `02:40:19`.
2. Transcribe only formula-level content needed for a receipt candidate.
3. Build candidate rows for the DGU/VZ and RS families first.
4. Reject or accept each row under the target-import guard and family identity
   check.

If that image/formula pass still does not emit an actual operator/action/EL or
RS action/operator rule, Oxford/Portal can be demoted from "first exact-locator
execution" to "source-native terminology/provenance surface" for these four
blocked family objects.

## 8. Execution Notes

Browsing/source fetching was available. The official public pages were fetched
successfully. Only short locator evidence is recorded here. No long transcript
excerpt is required for the decision.

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "OxfordPortalExactSourceLocatorExecution_V1",
  "run_id": "hourly-20260625-0502",
  "cycle": 1,
  "lane": 1,
  "verdict": "BLOCKED_ZERO_ACCEPTED_PRIMARY_SOURCE_RECEIPTS",
  "verdict_class": "blocked",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0502-cycle1-oxford-portal-exact-source-locator-execution.md",
    "companion_audit": "tests/hourly_20260625_0502_cycle1_oxford_portal_exact_source_locator_execution_audit.py",
    "artifact_id": "OxfordPortalExactSourceLocatorExecution_V1"
  },
  "source_surfaces": [
    {
      "source_id": "GU-MEDIA-2013-OXFORD",
      "url": "https://geometricunity.org/2013-oxford-lecture/",
      "access_status": "fetched_public_page",
      "surface_role": "primary public lecture and transcript surface"
    },
    {
      "source_id": "GU-MEDIA-2020-PORTAL-SPECIAL",
      "url": "https://geometricunity.org/",
      "access_status": "fetched_public_page",
      "surface_role": "official release landing page"
    },
    {
      "source_id": "GU-POD-2020-PORTAL-SPECIAL",
      "url": "https://theportal.group/a-portal-special-presentation-geometric-unity-a-first-look/",
      "access_status": "fetched_public_transcript_page",
      "surface_role": "Portal Group transcript of public release"
    }
  ],
  "required_family_coverage": [
    {
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "strongest_locator": "Oxford/Portal Shiab and projection vocabulary around 02:33:43 and pullback language around 02:40:19",
      "acceptance_status": "blocked",
      "first_missing_field": "exact_locator_emitting_required_object",
      "accepted_receipt_count": 0,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false
    },
    {
      "family": "RS",
      "required_object": "source.action_or_operator for d_RS,-1",
      "strongest_locator": "Oxford/Portal Rarita-Schwinger and Dirac-piece locator around 02:38:53 to 02:41:16",
      "acceptance_status": "blocked",
      "first_missing_field": "emitted_formula_or_rule",
      "accepted_receipt_count": 0,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false
    },
    {
      "family": "QFT",
      "required_object": "P_fin^b: F_phys^b(O) -> K_b",
      "strongest_locator": "none found on fetched official Oxford/Portal text surfaces",
      "acceptance_status": "blocked",
      "first_missing_field": "exact_locator_emitting_required_object",
      "accepted_receipt_count": 0,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false
    },
    {
      "family": "DGU_VZ",
      "required_object": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
      "strongest_locator": "Oxford/Portal GU Equations: Swervature and Displasion around 02:35:10 to 02:36:12",
      "acceptance_status": "blocked",
      "first_missing_field": "emitted_formula_or_rule_and_family_identity_check_to_D_GU_epsilon_0_1",
      "accepted_receipt_count": 0,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false
    }
  ],
  "strongest_positive_locator": {
    "family": "DGU_VZ",
    "locator": "official Oxford/Portal transcript, PowerPoint section GU Equations: Swervature and Displasion, 02:35:10-02:36:12",
    "positive_content": "source-native equation-shaped swervature/displasion language on Y before pullback to X",
    "why_not_accepted": "does not emit an actual D_GU^epsilon 0/1 action operator Euler-Lagrange equation principal symbol coefficient set or family identity certificate"
  },
  "first_exact_obstruction": {
    "id": "accepted PrimarySourceReceiptInstance_V1/family identity check",
    "missing": true,
    "description": "No fetched official Oxford/Portal locator emits a source-emitted required family object with emitted formula or rule, target-import exclusion, accepted routing, and family identity check."
  },
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "no_claim_promotion": true,
  "constructive_next_object": {
    "id": "OxfordPortalPrimarySourceReceiptInstanceCandidate_V1",
    "entry_type": "PrimarySourceReceiptInstance_V1_candidate",
    "minimum_test": "capture official PowerPoint image/formula anchors and test whether any emitted formula instantiates a family object without target import"
  },
  "next_meaningful_step": "capture and transcribe formula-level content from the official Oxford/Portal PowerPoint image anchors around 02:33:43, 02:35:10, 02:36:12, 02:38:53, and 02:40:19, then run target-import and family-identity checks",
  "forbidden_promotions": [
    "IG selects K_IG",
    "RS source-derived d_RS,-1 is established",
    "QFT P_fin^b is supplied",
    "DGU/VZ actual D_GU^epsilon 0/1 is identified",
    "Oxford/Portal exact locator execution permits proof restart",
    "source-native equation vocabulary is an accepted PrimarySourceReceiptInstance_V1"
  ]
}
```
