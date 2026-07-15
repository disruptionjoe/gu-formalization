---
title: "Structurally Forced, Internally Undecidable (DRAFT, adversarially corrected)"
status: draft
doc_type: draft_marker
created: 2026-07-14
updated: 2026-07-14
promotion: "Joe-gated. Do not promote, submit, post, or publish without explicit approval."
---

# Structurally Forced, Internally Undecidable -- draft audit

The original headline thesis did not survive the requested adversarial hardening. The folder remains under its established slug for continuity, but the manuscript is now titled *Invariant metrics and fundamental symmetries for compact stabilizers: an adversarial correction of the proposed GU grading-sign argument*.

## Contents

- [`draft-skeleton.md`](draft-skeleton.md) contains the corrected finite-dimensional theorem, written proofs, GU application audit, method-independence audit, literature positioning, and verified bibliography.
- [`HARDENING-REPORT.md`](HARDENING-REPORT.md) records each claim's disposition, the seven-item register outcome, external dependencies, and candidate-readiness verdict.
- [`tests/general_krein_grading_sign.py`](tests/general_krein_grading_sign.py) is a 77-assertion regression check for the corrected theorem and counterexamples. It is draft-local and is not wired into the repository greens gate.

## Current verdict

- For `O(p) x O(q)`, the admissible commuting fundamental symmetry is unique. There is no free `Z/2`.
- For a proper compact subgroup, a shared irreducible constituent across positive and negative sectors produces a continuous homogeneous space of admissible fundamental symmetries. Its real dimension is `sum dim_R(D_lambda) a_lambda b_lambda`.
- The former non-coincidence hypothesis is now fully characterized in finite dimensions. It is the exact uniqueness condition for the admissible fundamental symmetry, but it does not force one invariant scale per diagonal block.
- GU's constructed `SO(9) x SO(5)` surrogate satisfies non-coincidence and therefore lies in the unique case. The actual interacting GU good-stable stabilizer and observable algebra are not derived.
- W203 proves only a one-dimensional ultralocal `so(9,5)` kernel, conditional on W154. The nonlocal source action is not built.
- The five methods are not independent. The honest inventory is one invariant-theory theorem, one conditional Helmholtz lemma, one unbuilt BRST route, and two analogies.
- No formal undecidability theorem is present. The justified phrase is "underdetermined by the specified invariance data," and only in the nonunique cases of the corrected theorem.
- bar (b) and H59 remain OPEN. No canon or verdict changed.

## Machine check

From the repository root:

```
python -u papers/drafts/structurally-forced-internally-undecidable/tests/general_krein_grading_sign.py
```

Expected result: `77/77 checks passed` and exit code 0.

## Seven-item hardening register outcome

1. **General-theorem gap: closed in finite dimensions, with the old claim killed.** The compact-stabilizer moduli space and its exact residual dimension are proved. Canonical uniqueness and a proper-subgroup continuous counterexample are tested. Infinite-dimensional Krein spaces remain outside scope.
2. **Prior art and novelty: completed as an internal literature sweep, with major downgrades.** Metric and `C` nonuniqueness, observable-dependent metric selection, physical-state reconstruction, and indefinite-sector prescriptions are prior art. All retained citations have a publisher, DOI, or arXiv record. An outside specialist novelty review is still required before candidate status.
3. **Written methods and independence: completed as an audit, not as five proofs.** The valid theorem and conditional lemma are written out. The BRST construction is unbuilt. Lawvere and topos are analogies. The multi-formalism-independence claim is withdrawn.
4. **Independent reader: cannot be closed inside the GU repository.** A Krein/PT-symmetric-QFT expert and a real-representation-theory expert should review the theorem, scope, and prior art. A logic expert should confirm the removal of the independence framing.
5. **Structural owner identification: not established and kept gated.** No cross-repository identity is asserted. The actual GU `C`, stabilizer, and observable algebra must be built before any owner claim can be tested.
6. **Venue positioning: provisionally resolved.** The corrected general theorem is likely standard background. A future paper would need a derived GU application and would fit math-ph or hep-th. The present draft is not suitable for submission.
7. **Source-action completion context: clarified.** "Forced" applies only to the W203 ultralocal bridge kernel, conditional on W154. It does not apply to an unbuilt nonlinear or nonlocal action.

## Remaining blockers

The following cannot honestly be converted into editorial cleanup:

1. derive the physical GU good-stable stabilizer and its isotypic decomposition from the native dynamics;
2. construct the interacting grading or metric operator on the relevant state space;
3. complete the H59 keep-and-grade requirements, including `[P,S] = 0` and projected unitarity;
4. complete or replace the W154-dependent source-action bridge beyond the ultralocal kernel;
5. obtain outside specialist review of the finite-dimensional classification and novelty; and
6. if an independence claim is desired, state a formal theory and prove genuine model separation rather than use toy analogies.

The single biggest remaining risk is that the native GU stabilizer and interacting observable algebra may not resemble the compact 14-frame surrogate. Until they are derived, the paper has no established GU grading-sign result.

## Governance

This is draft-tier only. It was not promoted, submitted, posted, deployed, or otherwise published. Promotion and publication remain Joe-gated. bar (b) and H59 remain OPEN.
