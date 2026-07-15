---
title: "Drafting Factory Paper Seed Handoff"
status: active
doc_type: runbook
scope: cross-repo-coordination
created: 2026-07-15
---

# Drafting Factory paper seed handoff

Drafting Factory owns paper seeds, cross-paper priority, publication-lane capacity, and drafting. GU owns
its research truth, proof grades, corrections, native-versus-forced judgments, and source hardening.

## On discovery

As soon as a GU run identifies a credible paper-shaped opportunity, send a `Status: proposed` note to
`CapacityOS/system/mailboxes/drafting-factory/`. Do not wait for candidate-grade hardening. Include:

- a stable seed slug and working title;
- the pinned GU revision and durable source pointers;
- the possible contribution, audience, and publication lane;
- the verbatim current grade and every load-bearing condition;
- known overlap, merge, or novelty risks;
- an explicit statement that no drafting, promotion, publication, or external action is authorized.

A seed is not a claim that the paper is worth producing. It lets Drafting Factory deduplicate and compare
the opportunity at negligible cost.

If a one-writable-repository child run cannot write the mailbox, place the complete payload under
`paper_seed_proposal` in the receipt. The parent or daily steward routes it before unrelated paper work.

## On a factory hardening request

Drafting Factory sends GU a mailbox proposal only when it has capacity, selects the seed, and intends to
spend production effort if the named source gaps close. A useful request identifies the intended lane, exact
proof/citation/novelty/reproducibility/scope gaps, desired frozen return, grade ceiling, and real deadline.

The daily GU steward treats this as a valid priority signal, not a command. GU may accept, defer, narrow, or
reject it based on scientific impact and the protected portfolio. If accepted, GU returns a frozen
provenance-bearing packet. Drafting Factory must not infer a proof-grade or native-versus-forced upgrade from
draft readiness.

## JoeOps boundary

Do not send routine paper seeds to JoeOps. Use JoeOps only when Joe's decision, external eyes, publication
authority, paid or outside expertise, or genuine cross-program coordination is required.
