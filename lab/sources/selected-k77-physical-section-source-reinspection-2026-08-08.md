---
artifact_type: source_reinspection
created: 2026-08-08
gate: ACTUAL_Y14_OBSERVATION_SECTION_JET_INTEGRABILITY_AND_PHYSICAL_FAITHFULNESS
overall_disposition: SOURCE_CORRECTS_ARBITRARY_X_GLOBAL_SECTION__SOURCE_CONFIRMS_LOCAL_SECTION_PULLBACK_GRAMMAR__SOURCE_SILENT_PHYSICAL_FAITHFULNESS_BV_QUOTIENT
---

# Source reinspection: physical observation section and faithfulness

## Result

The live queue had over-composed three claims: existence of a local observation
section, existence of a global Lorentz metric section on arbitrary `X`, and
faithfulness of ordinary pullback on the action Euler image.  The sources own
only the first and the observation grammar.

In the 2020 Portal/Oxford presentation, Weinstein says that only two fields
know about `X`: the connection `theta` and a section `sigma` used to communicate
between `U` and `X`.  He later says most fields live on `Y` and are observed by
pullback as if they lived on `X`.  This is `SOURCE-CONFIRMS` for section and
pullback grammar.

The 2025 Weinstein--Curt exchange is decisive for the global qualifier.  At
`01:18:06--01:19:15`, asked whether the metric bundle is trivial, Weinstein
says it depends on topology, rejects the statement that GU already has the
relevant global section, and distinguishes the local `iota` notation from the
disputed global `gimmel` recollection.  The exchange is not a polished theorem,
but it is enough to block attribution of arbitrary-`X` global-section
existence to Weinstein.

```text
SOURCE-CORRECTS: arbitrary-X/global observation-section attribution
SOURCE-CONFIRMS: local section and pullback observation grammar
SOURCE-SILENT:   faithful Euler reception, conormal constraint, BV quotient,
                 global BFV phase space and common analytic domain
```

## Layer-0 consequence

The phrase “one temporal dimension” has two possible types:

1. a requested signature label; or
2. an already supplied Lorentz structure/reduction on `X`.

The first does not construct a global Lorentz metric.  The second is sufficient
starting structure, but then global admissibility has been supplied rather
than derived from a bare spin four-manifold.  This is a sector condition, not
an external source-action selector and not P1/P2/P3.

Likewise, source-level “pullback” establishes how fields are observed.  It
does not print the inverse-transpose equation dual or prove that the action
Euler image avoids the conormal kernel.  Those are repository constructions
and tests.

## Source loci

- `lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md`,
  `01:16:36` and `02:21:07`.
- `lab/sources/transcripts/toe-weinstein-gu-40-years.md`,
  `01:18:06--01:19:15`.
- `papers/drafts/Transcript into the impossible.md`, section/pullback passage
  beginning “A metric is a section of its own bundle of metrics.”

No source verdict is used as mathematical proof.  The companion construction
supplies the topology and rank/action-image arguments independently.
