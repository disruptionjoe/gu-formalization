---
title: "HQW-LEAD credibility pass on the located-not-forced paper (H04 + H05)"
status: exploration
doc_type: exploration
team: "QW-LEADPAPER (HQW-LEAD)"
date: "2026-07-14"
grade: "review-support (credibility/honesty; no science/canon change)"
targets: ["W189 register H04 (premise-flag map)", "W189 register H05 (per-claim GU-dependency table)"]
paper: "papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.tex"
---

# HQW-LEAD credibility pass (2026-07-14)

Two register quick wins on the repo's strongest paper (`located-not-forced`, arXiv-ready, GU-independent
theorem core). Five personas inline (author-editor, hostile referee, rep-theory checker, reproducibility
engineer, honesty auditor), then synthesis. Honest grading; no science/canon change; no external action; no
promotion (arXiv submission stays Joe-gated).

## What changed

1. **Full deliverable** -- `papers/candidates/located-not-forced/review/HQW-LEAD-premise-flag-map-and-gu-dependency-2026-07-14.md`
   (new): the H04 premise-flag map (17 loci) and the H05 per-claim GU-dependency table (21 claims), with the
   five-persona sign-offs.

2. **One `.tex` edit** -- a single exploration-grade **reinforcing** remark added to Section `sec:thm2`
   (after the "external by structure" paragraph): GU's own metric-compatible connection curvature `F_A` on
   `Y^{14}=Met(X^4)` is `so(9,5)`-valued, hence leakage-free on `ker Γ`, hence provably cannot force an odd
   count from inside -- so the forcing datum must be external and non-metric (W177, 2026-07-14). This
   *reinforces* the external-datum framing already carried by the paper; it changes no verdict, grade, or
   claim, and is marked exploration-grade with a real exit status. No caveat clause was added anywhere,
   because none was missing (see H04 result).

## H04 result (premise-flag map)

**17/17 count/"located" loci already carry the premise flag** (torsion-count premise / `Hom(Z/3,Z)=0` /
external-open-residual caveat / explicit grade tag). **No overstating sentence was found; zero caveat clauses
had to be added.** The paper's flagging is exhaustive across title, abstract, every contribution item, both
theorem sections, the carrier section, the decider, the open-conjecture section, the status table, and the
conclusion. Rep-theory checker confirmed the premise is correctly stated (`Hom(Z/3,Z)=0`, the CRT split, the
integer-index vs torsion-count contrast) and is a genuine premise, not a smuggled result.

## H05 result (GU-dependency table)

**FULLY-GU-INDEPENDENT: 15** substantive claims plus the GU-independent cores of 3 more; **CONDITIONAL-ON-GU: 2**
(the Λ²₊-twist identification, reconstruction-grade; the literal integer, open/gated on GU's unbuilt source
action); **GU-MOTIVATION-ONLY: 2** (sector provenance; the Pati--Salam chain selection). The entire
theorem-grade and computed-grade core is GU-independent; nothing the paper asserts as *established* is
conditional on GU being correct. This makes the RESEARCH-POSTURE credibility case explicit for a referee: the
paper survives GU falling away.

## Reproducibility anchors run this pass

- `papers/candidates/located-not-forced/reproduce_all.py` -> 31/31 load-bearing checks, exit 0 (150.8s).
- `tests/W177_connection_curvature_c2.py` -> 17/17, exit 0 (the GU-native-curvature reinforcement).

## Binding compliance

No science change (only a reinforcing exploration-grade remark + a referee-facing dependency table). No canon
change. No external action. No promotion. Zero em dashes.
