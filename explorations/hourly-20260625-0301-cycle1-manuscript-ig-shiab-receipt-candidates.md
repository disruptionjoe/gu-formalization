---
title: "Hourly 20260625 0301 Cycle 1 Manuscript IG Shiab Receipt Candidates"
date: "2026-06-25"
run: "hourly-20260625-0301"
cycle: 1
lane: 2
doc_type: manuscript_ig_shiab_receipt_candidates
artifact_id: "ManuscriptIGShiabReceiptCandidateSearch_V1"
verdict: "CONDITIONAL_QUARANTINED_STRONG_CANDIDATE_ZERO_ACCEPTED_IG_RECEIPTS"
owned_path: "explorations/hourly-20260625-0301-cycle1-manuscript-ig-shiab-receipt-candidates.md"
companion_audit: "tests/hourly_20260625_0301_cycle1_manuscript_ig_shiab_receipt_candidates_audit.py"
---

# Hourly 20260625 0301 Cycle 1 Manuscript IG/Shiab Receipt Candidates

## 1. Verdict

Verdict: **conditional** for future routing, with the current IG receipt
candidate **quarantined**.

The local 2021 manuscript PDF is acquired and searchable:

```text
source_id: GU-MEDIA-2021-DRAFT-RELEASE
local_path: Geometric_UnityDraftApril1st2021.pdf
sha256: 3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4
page_count: 69
```

The search found a strong primary-source IG/Shiab codomain candidate on PDF
pages 41-44, supported by the inhomogeneous gauge group machinery on pages
31-40 and summary/projection language on pages 54-57. It did **not** find an
accepted `PrimarySourceReceiptInstance_V1` for:

```text
SourceForcedCodomainSelectorForK_IG
```

The manuscript emits a Shiab operator type and formula, but not the
source-forced selector rule, representation context, and rival-elimination
object required to promote the row from candidate to accepted receipt.

Decision:

```text
candidate_status: quarantined
accepted_receipt_count: 0
target_import_clean: true
target_import_or_proof_promotion_allowed: false
proof_restart_allowed: false
```

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the controlling discipline: source search is
legitimate Mission A work, but compatibility, hosted structure, or target-facing
success cannot be treated as derivation.

`process/runbooks/five-lane-frontier-run.md` supplies the lane contract:
produce a decision-grade artifact, name the first exact obstruction, and avoid
claim promotion from suggestive source adjacency.

`PrimarySourceReceiptIntakeProtocol_V1` supplies the receipt requirements:
accepted source kind, exact locator, emitted object, emitted formula or rule,
representation context, empty target data, and `accepted_for_routing` status.
Intake alone never promotes a GU claim.

`RepoLocalPrimaryGUSourceReceiptMap_V1` supplies the current global state:
zero accepted primary source receipts, with IG blocked at
`SourceForcedCodomainSelectorForK_IG`.

`TargetImportGuardReceiptAudit_V1` supplies the import control. This lane did
not use DESI, dark-energy, FLRW, rank, generation, VZ, CHSH, or other
downstream target data to select candidates.

The local PDF extraction directly supplied the page-level query log below.
Search families covered:

| query family | query variants | manuscript result |
|---|---|---|
| Shiab / ship-in-a-bottle | `Shiab`, `Ship In a Bottle`, `ship` | strongest positive cluster on pp. 41-44; appendix on pp. 65-66 |
| observerse / endogenous / metric bundle | `Observerse`, `endogenous`, `Y 14`, `bundle of metrics`, `Met(X)` | substrate and pullback context on pp. 16-26, 50-55, 64 |
| projection / pi | `projection`, `projection map`, `pi/π`, `pullback`, `pull back` | projection maps on pp. 37-38 and projection-removal summary on pp. 55-57 |
| domain/codomain/selector terms | `codomain`, `domain`, `selector`, `select`, `chosen`, `choice`, `settled on`, `Bianchi` | no literal `codomain`, `domain`, or `selector`; selection-adjacent `choice/settled/Bianchi` on pp. 42-43 |
| inhomogeneous gauge group | `Inhomogeneous Gauge`, `gauge group`, `semi-direct`, `G = H`, `N =` | source machinery on pp. 31-40, summary on p. 64 |

## 3. The Strongest Positive Result

The strongest positive result is:

```text
ManuscriptIGShiabCodomainCandidate_V1
```

with exact locators:

| locator | source-emitted object | receipt value |
|---|---|---|
| PDF p. 32, section 5.2, eqs. 5.3-5.7 | `H`, `A = Conn(P_H)`, `N = Omega^1(Y, ad(P_H))`, affine difference map | supplies IG ambient spaces |
| PDF p. 33, section 5.3-5.4, eqs. 5.8-5.11 | `G = H semidirect N`, explicit multiplication, left/right actions on `A` | supplies inhomogeneous gauge group action context |
| PDF p. 37, section 6.3, eqs. 6.10-6.12 | `pi_A0: G -> N` as a projection map in a homogeneous principal fibration | projection-adjacent support, not a `K_IG` selector |
| PDF p. 40, section 7.1-7.2, eqs. 7.1-7.6 | `delta o mu_A0: G -> N`, augmented torsion, map chain ending in `N` | supports source/codomain context for IG fields |
| PDF p. 41, section 8 | ship-in-a-bottle construction for gauge-covariant contraction | direct IG/Shiab motivation |
| PDF p. 42, section 8.2, eq. 8.7 vicinity | family of invariant-subspace data and operator-choice discussion | strongest selector-adjacent evidence, but also names the missing selector notes |
| PDF p. 43, section 9.1, eqs. 9.1-9.3 | typed Shiab operator `Omega^2(Y 7,7, ad) -> Omega^{d-1}(Y 7,7, ad)` and explicit Einstein/Ricci-like contraction formula | strongest positive domain/codomain candidate |
| PDF p. 44, section 9.1, eqs. 9.4-9.6 | bosonic action using the Shiab operator and EL form in `Omega^{d-1}(ad) oplus Omega^d(ad)` | action/EL adjacency; not the selector itself |
| PDF pp. 55-57, section 12.1/12.4, eqs. 12.2-12.7 | projection-removal summary and comparison with Einstein-Ricci projection | downstream projection context; not source-forced selection |
| PDF pp. 65-66, appendix | wedge, Hodge star, contraction, bracket, symmetric product, volume-form tools | construction toolkit only |

Short paraphrase: the manuscript gives the inhomogeneous gauge group, action on
connections, projection-to-`N` maps, and a Shiab contraction operator whose
displayed type has a source and target. This is strong enough to preserve as a
candidate receipt row. It is not strong enough to accept as the required
`SourceForcedCodomainSelectorForK_IG`.

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1
```

The obstruction appears inside the strongest positive window. On PDF page 42,
section 8.2 says the operator choice was remembered as representation-theoretic
and Bianchi-based; on PDF page 43, the note attached to the displayed Shiab
operator says the author once had calculations that selected the operator but
cannot presently locate them.

That means the manuscript emits:

```text
candidate Shiab operator family
one displayed typed Shiab operator
one explicit contraction formula
```

but does not emit:

```text
source-forced selector rule
representation/highest-weight selection computation
Bianchi selection criterion in executable form
rival-elimination or projection-loss rule
family identity to SourceForcedCodomainSelectorForK_IG
```

The literal query pass also matters: the PDF text contains no hits for
`codomain`, `domain`, or `selector`. The map type on page 43 supplies a domain
and target mathematically, but the source does not name or force a codomain
selector.

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The constructive next object is:

```text
AuthorManuscriptIGSelectorIdentityPacket_V1
```

Minimum fields:

| field | required content |
|---|---|
| `source_id` | `GU-MEDIA-2021-DRAFT-RELEASE` |
| `candidate_locators` | PDF pp. 32-33, 37-38, 40-44, 55-57, 65-66 |
| `selected_domain` | exact source-emitted domain of the IG/Shiab witness |
| `selected_codomain` | exact source-emitted codomain/target |
| `selector_rule` | source-emitted representation/Bianchi/projector rule selecting the object |
| `rival_eliminators` | source-emitted exclusion of rival natural contractions, projections, or lower-order alternatives |
| `family_identity_check` | proof that the selected object is `SourceForcedCodomainSelectorForK_IG` |
| `target_import_screen` | empty `target_data_seen`; no DESI/FLRW/dark-energy/VZ/QFT target choice |
| `acceptance_status` | `accepted_for_routing`, `quarantined`, `rejected`, or `missing` |

If the packet recovers the missing representation-theory/Bianchi selector from
primary manuscript-adjacent material, the candidate can be reconsidered for
`accepted_for_routing`. If it does not, the right negative object is a scoped
`missing` row for the selector object, not a no-go theorem for GU.

## 6. What This Means For The Relevant GU Claim

Allowed claim:

```text
The 2021 manuscript contains exact IG/Shiab candidate locators, including a
typed Shiab contraction formula and inhomogeneous-gauge source machinery.
```

Forbidden promotions:

```text
SourceForcedCodomainSelectorForK_IG is accepted.
K_IG is selected by the manuscript.
The displayed Shiab target is the final GU codomain.
The projection map pi_A0 is the IG codomain selector.
Ship-in-a-bottle language is a proof object.
Any non-IG family object is claimed by this lane.
Any downstream proof, target recovery, or physics claim restarts from this row.
```

The GU-relevant impact is priority, not proof. The manuscript makes the
IG/Shiab route source-real enough to mine further, but the route remains blocked
at the exact source-forced selector object.

## 7. Next Meaningful Proof Or Computation Step

Run a sequential source-identity pass:

1. Re-extract the formula windows on PDF pp. 32-33, 37-38, 40-44, 55-57, and
   65-66.
2. Normalize the displayed Shiab type and formula against the
   `SourceForcedCodomainSelectorForK_IG` schema.
3. Build a rival list: exterior derivative, scalar/divergence contraction,
   symmetric derivative, projection-dependent contraction, and lower-order
   dressed classes.
4. Search only source-side text/formulas for a Bianchi, representation-theory,
   projection-loss, or rival-elimination selector.
5. If found, instantiate one `PrimarySourceReceiptInstance_V1` candidate with
   `target_data_seen: []`; if not found, instantiate a scoped missing/negative
   selector row.

Proof work remains stopped until source intake and family identity both pass.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "ManuscriptIGShiabReceiptCandidateSearch_V1",
  "run": "hourly-20260625-0301",
  "cycle": 1,
  "lane": 2,
  "verdict": "CONDITIONAL_QUARANTINED_STRONG_CANDIDATE_ZERO_ACCEPTED_IG_RECEIPTS",
  "verdict_class": "conditional",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0301-cycle1-manuscript-ig-shiab-receipt-candidates.md",
    "companion_audit": "tests/hourly_20260625_0301_cycle1_manuscript_ig_shiab_receipt_candidates_audit.py"
  },
  "source": {
    "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
    "source_kind": "author_manuscript_or_draft",
    "local_path": "Geometric_UnityDraftApril1st2021.pdf",
    "sha256": "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
    "page_count_observed": 69,
    "pdf_text_extracted_with": "pypdf"
  },
  "family_scope": {
    "families_claimed": [
      "IG"
    ],
    "non_IG_families_claimed": false,
    "required_object": "SourceForcedCodomainSelectorForK_IG"
  },
  "query_families_searched": [
    {
      "family": "shiab_ship",
      "variants": [
        "Shiab",
        "Ship In a Bottle",
        "Ship in a Bottle",
        "ship"
      ],
      "hit_pages": [
        2,
        3,
        18,
        34,
        41,
        42,
        43,
        44,
        54,
        56,
        58,
        63,
        65
      ]
    },
    {
      "family": "observerse_endogenous_metric_bundle",
      "variants": [
        "Observerse",
        "endogenous",
        "U14",
        "U^14",
        "Y 14",
        "bundle of metrics",
        "Met(X)"
      ],
      "hit_pages": [
        2,
        16,
        17,
        18,
        21,
        25,
        26,
        29,
        44,
        50,
        51,
        55,
        57,
        58,
        59,
        61,
        64
      ]
    },
    {
      "family": "projection_pi",
      "variants": [
        "projection",
        "projection map",
        "pi/π",
        "pullback",
        "pull back"
      ],
      "hit_pages": [
        2,
        3,
        9,
        11,
        12,
        14,
        15,
        16,
        17,
        21,
        25,
        26,
        37,
        38,
        54,
        55,
        56,
        57,
        58,
        62,
        64,
        65
      ]
    },
    {
      "family": "domain_codomain_selector",
      "variants": [
        "codomain",
        "domain",
        "selector",
        "select",
        "chosen",
        "choice",
        "settled on",
        "Bianchi"
      ],
      "literal_absences": [
        "codomain",
        "domain",
        "selector"
      ],
      "hit_pages": [
        3,
        4,
        6,
        9,
        10,
        11,
        15,
        16,
        17,
        19,
        20,
        21,
        22,
        25,
        26,
        30,
        32,
        35,
        36,
        37,
        38,
        42,
        43,
        55,
        57,
        59,
        65
      ]
    },
    {
      "family": "inhomogeneous_gauge_group",
      "variants": [
        "Inhomogeneous Gauge",
        "inhomogeneous",
        "gauge group",
        "semi-direct",
        "G = H",
        "N ="
      ],
      "hit_pages": [
        2,
        12,
        14,
        15,
        31,
        32,
        33,
        34,
        35,
        37,
        39,
        40,
        41,
        42,
        47,
        55,
        60,
        64,
        69
      ]
    }
  ],
  "candidate_rows": [
    {
      "row_id": "PrimarySourceReceiptInstance_V1_candidate:IG:GU-MEDIA-2021-DRAFT-RELEASE:pp41-44:Shiab",
      "candidate_status": "quarantined",
      "acceptance_status": "quarantined",
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "source_kind": "author_manuscript_or_draft",
      "page_locators": [
        "PDF page 41 section 8",
        "PDF page 42 section 8.2",
        "PDF page 43 equations 9.1-9.3",
        "PDF page 44 equations 9.4-9.6"
      ],
      "short_paraphrase": "The manuscript displays a Shiab operator family and a typed contraction from ad-valued two-forms to a degree d-1 ad-valued target, with an Einstein/Ricci-like formula.",
      "emitted_object_type": "operator_candidate",
      "emitted_formula_or_rule": "Shiab contraction formula and typed map, but not a source-forced selector rule",
      "representation_context": "Spin(7,7), invariant subspaces, inhomogeneous gauge group element epsilon in H subset G",
      "target_data_seen": [],
      "target_import_clean": true,
      "family_identity_passed": false,
      "accepted_for_routing": false,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false,
      "first_missing_field": "source_forced_selector_rule_and_family_identity"
    },
    {
      "row_id": "SourceLocatorCandidate_V1:IG:GU-MEDIA-2021-DRAFT-RELEASE:pp32-40:inhomogeneous-gauge",
      "candidate_status": "quarantined",
      "acceptance_status": "quarantined",
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "source_kind": "author_manuscript_or_draft",
      "page_locators": [
        "PDF page 32 equations 5.3-5.7",
        "PDF page 33 equations 5.8-5.11",
        "PDF page 37 equations 6.10-6.12",
        "PDF page 40 equations 7.1-7.6"
      ],
      "short_paraphrase": "The manuscript defines the inhomogeneous gauge group, its actions on connections, projection to N, and augmented torsion maps.",
      "emitted_object_type": "source_context",
      "emitted_formula_or_rule": "G/H/N/A and projection-to-N machinery, not the K_IG codomain selector",
      "representation_context": "connection affine space A modeled on N and inhomogeneous gauge group G",
      "target_data_seen": [],
      "target_import_clean": true,
      "family_identity_passed": false,
      "accepted_for_routing": false,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false,
      "first_missing_field": "selector_rule_for_K_IG"
    },
    {
      "row_id": "RejectedSelectorCandidate_V1:IG:GU-MEDIA-2021-DRAFT-RELEASE:literal-domain-codomain-selector-absence",
      "candidate_status": "missing",
      "acceptance_status": "missing",
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "source_kind": "author_manuscript_or_draft",
      "page_locators": [],
      "short_paraphrase": "The literal terms codomain, domain, and selector do not occur in the extracted PDF text.",
      "emitted_object_type": "negative_control",
      "emitted_formula_or_rule": "no literal codomain/domain/selector rule found",
      "representation_context": "the page 43 typed map is still considered separately as a mathematical domain-target candidate",
      "target_data_seen": [],
      "target_import_clean": true,
      "family_identity_passed": false,
      "accepted_for_routing": false,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false,
      "first_missing_field": "literal_or_equivalent_source_forced_selector"
    },
    {
      "row_id": "RejectedSupportRow_V1:IG:GU-MEDIA-2021-DRAFT-RELEASE:observerse-endogenous",
      "candidate_status": "rejected",
      "acceptance_status": "rejected",
      "family": "IG",
      "required_object": "SourceForcedCodomainSelectorForK_IG",
      "source_kind": "author_manuscript_or_draft",
      "page_locators": [
        "PDF page 16 definition 3.1",
        "PDF page 25 equation 3.37",
        "PDF page 50 endogenous-generation note",
        "PDF page 55 Y14 summary",
        "PDF page 64 Witten-summary assertions"
      ],
      "short_paraphrase": "Observerse, pullback, Y14, and endogenous-generation language provide GU substrate context but do not emit an IG/Shiab selector.",
      "emitted_object_type": "context_only",
      "emitted_formula_or_rule": "none for SourceForcedCodomainSelectorForK_IG",
      "representation_context": "Observerse and pullback setting",
      "target_data_seen": [],
      "target_import_clean": true,
      "family_identity_passed": false,
      "accepted_for_routing": false,
      "proof_restart_allowed": false,
      "claim_promotion_allowed": false,
      "first_missing_field": "IG_selector_emitted_object"
    }
  ],
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "target_import_or_proof_promotion_flags": {
    "target_data_seen_nonempty": false,
    "target_import_used": false,
    "accepted_for_routing_any": false,
    "proof_restart_allowed": false,
    "claim_promotion_allowed": false
  },
  "strongest_positive_result": "PDF pages 41-44 emit a Shiab operator family and displayed typed contraction formula, supported by inhomogeneous gauge machinery on pages 32-40.",
  "first_exact_obstruction": {
    "id": "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
    "missing": true,
    "description": "The source says the operator was selected using representation/highest-weight and Bianchi considerations, but those calculations are not located or emitted in executable form.",
    "blocks_acceptance_for": "SourceForcedCodomainSelectorForK_IG"
  },
  "constructive_next_object": {
    "id": "AuthorManuscriptIGSelectorIdentityPacket_V1",
    "required_fields": [
      "selected_domain",
      "selected_codomain",
      "source_forced_selector_rule",
      "representation_or_Bianchi_selection_computation",
      "rival_eliminators",
      "family_identity_to_SourceForcedCodomainSelectorForK_IG",
      "target_import_screen"
    ]
  },
  "no_claim_promotions": {
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "K_IG_selected_by_manuscript": false,
    "displayed_Shiab_target_final": false,
    "pi_A0_is_IG_codomain_selector": false,
    "ship_in_bottle_is_proof_object": false,
    "non_IG_family_claimed": false,
    "proof_restart_allowed": false
  },
  "next_meaningful_step": "Build AuthorManuscriptIGSelectorIdentityPacket_V1 from the exact page windows and either instantiate an accepted_for_routing source selector candidate or a scoped missing selector row."
}
```
