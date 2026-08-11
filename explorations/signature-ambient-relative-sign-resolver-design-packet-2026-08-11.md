---
title: "Design packet: a relative-sign resolver for SIGNATURE-AMBIENT"
status: active_research
doc_type: resolver_design_packet
artifact_type: resolver_design_packet
created: 2026-08-11
run_id: RUN-20260811-141240-gu-signature-ambient-resolver-design
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
target_fork: SIGNATURE-AMBIENT
relates_to:
  - explorations/campaign-altitude-route-review-2026-08-11.md (rank-4(a) proposal)
  - explorations/source-signature-notation-is-mirrored-2026-08-08.md
  - explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md
designer_certificate: tests/channel-swings/signature_ambient_relative_sign_design_certificate.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
row_change: none
registry_change: none
binding: >-
  Design input for a future resolver wave. This packet names no fork
  disposition, updates no registry row, and moves no verdict; the executing
  wave owns every disposition under the full checking contract. Division of
  labor per the standing assist model: the design and the designer's
  certificate are supplied here; the wave implements the decisive checks
  independently and certifies or refutes them.
hostile_review: lab/process/hostile-reviews/2026-08-11-signature-ambient-resolver-design-review.md
---

# Design packet: a relative-sign resolver for `SIGNATURE-AMBIENT`

`SIGNATURE-AMBIENT` is the program's deepest live fork (depth over
threshold, flagged every run) and has had **no named resolver** since both
M-H9 and the declared-base route were falsified on 2026-08-08. This packet
designs a replacement from what those two failures jointly proved: absolute
signature pairs are convention-dependent in this construction, so **only
quantities invariant under uniform relabeling can discriminate.** The route
below reduces the fork to one such quantity — a single relative-sign bit
that each source display wears on its face — and specifies bounded exact
checks plus extraction steps that one wave can execute.

## Pre-flight assessment

Failure modes this design could commit, and the mitigations applied:

1. **Repeating the dead resolvers' mistake** (targeting convention-dependent
   data). Mitigation: the discriminating quantity is the balance of a
   uniform display's block sum — an unordered-pair invariant, unchanged
   under mirroring the whole display. The packet states why each dead
   resolver could not have worked in these terms.
2. **Designer-bug propagation** (M-H9's failure lived in its designer's own
   machinery). Mitigation: the designer's certificate (green, exact
   rational arithmetic, planted controls) certifies every numeric claim
   here, including the caveat that demoted this packet's own first draft
   (T6); the executing wave must still implement its checks independently.
3. **Layer-0 equivocation** across the same-neighborhood objects. Mitigation:
   the object table below; the wave re-runs it as its Layer-0 precondition.
4. **Source overreach.** Verbatim-extracted displays are distinguished from
   transcript-narration bridges, and the outcome grades are set by which
   anchor the wave secures (formula, uniform-reading presumption, or
   neither).
5. **Fan-out underestimation.** Resolution in either direction touches the
   settled `REAL-CLIFFORD-FORM` row's pressure note and the eleven files
   carrying the mixed-notation acknowledgment; the outcome table routes
   both explicitly.

## Layer-0 object table (run before the wave, per the six-axis precondition)

| term | object A | object B | rule for this route |
|---|---|---|---|
| "ambient signature" | the induced metric signature on the chimeric total space / pullback `ג∗(TY)` | the real Clifford algebra the source computes spinors in (`REAL-CLIFFORD-FORM`, settled `Cl(7,7)=M128(R)`) | this route resolves A only; the registry marks B distinct; B's pressure note is routed in the outcome table, never silently discharged |
| "(1,3) vs (3,1)" | a writing convention (which count is first) | the geometric base component (`g` vs `-g`) | neither is this route's discriminator; the route reads only unordered-pair balances, which both readings preserve |
| "the fiber form" | the transcript's raw/traceless/trace-flipped sequence | the draft's normal-bundle metric on `N_ג` (eq 12.19) | identified by the source's own narration of one construction; the wave re-confirms from the draft text and grades the identification (C3) |
| "the p.61 display" | the signature typing used here | the carrier-split third option (same display read as a carrier claim, unadjudicated) | same line, different question; this route types signatures only and leaves the carrier-split fork untouched |

## State of the fork, compressed

- The source's transcript notation is the mirror of the repository's,
  proven three-for-three with an evenness control
  (`explorations/source-signature-notation-is-mirrored-2026-08-08.md`).
- The transcript's spoken blocks — vertical `(4,6)`, horizontal `(1,3)` —
  sum to a balance-4 total in any uniform reading; its asserted total
  `(7,7)` is balance-0. Eleven repository files carry the mixed-notation
  sum that bridges that gap (the standing red gate).
- The 2021 draft's own display, eqs (12.18)-(12.19) p.61, verbatim in
  `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`:
  `ג : X^{1,3} → Y^{7,7}` and `ג∗(TY^{7,7}) = TX^{1,3} ⊕ N^{6,4}_ג`,
  with "for Spin(1,3)×Spin(6,4)" in §2.2 of the same extraction.
- The repository's exact computations of the narrated fiber sequence give
  plus-first `(7,3)` raw, `(6,3)` traceless, `(6,4)` trace-flipped.
- `dc-h1`: only the relative sign is well posed; the absolute ordered pair
  is monodromy-dependent.

## Forced-form derivation

**Step 1 — the mechanics that killed both resolvers.** The fiber forms are
even in the base metric (`G[-g] = G[g]`: every term is quadratic in
`g^{-1}`), while the horizontal block is odd (`(-g)^{-1} = -(g^{-1})`).
The composite total is therefore not sign-covariant, and the absolute pair
assigned to the total depends on labeling freedom that is pure convention
at base level. Any resolver targeting an absolute pair (M-H9's endpoint
pair; the declared-base retyping) computed a quantity with no invariant
content. Certified: T2; consistent with dc-h1 and M-H9's recorded
cancellation.

**Step 2 — the two-bit invariant reduction.** After Step 1, the fork's
entire well-posed content is two mirror-invariant bits:

- **Bit 1 (relative block sign):** whether the horizontal and vertical
  blocks enter the fourteen-dimensional total with the same or opposite
  effective sign. Equivalently, and this is the operative form: **the
  balance `|p−q|` of any uniformly read block sum.** On fourteen
  dimensions, balance 0 pins the unordered pair `{7,7}` exactly and
  balance 4 pins `{9,5}` exactly (certified: T6) — and these unordered
  pairs are precisely the registry's two horns. Note `(7,7)` is
  self-mirror: a balance-0 verdict is convention-free with no residue.
- **Bit 2 (trace regime):** which side of the `lam = 1/4` degeneracy the
  vertical form sits on. The exact portrait of the DeWitt-type family
  `a<h,h>_g − b(tr_g h)^2`: traceless sector fixed at nine dimensions with
  `|p−q| = 3`, trace direction flipping at `b/a = 1/4`; for positive
  normalization the achievable set is `{(7,3),(6,4)}` (certified: T1).
  Both sources' fiber labels, under any reading, land on trace-flipped
  members (balance-2 ten-dimensional forms), fixing bit 2 = flipped —
  consistent with the repository's `(6,4)`-both-ways computations.

**Step 3 — reading bit 1 off the sources.** Each source's uniform display
carries its balance on its face, no convention knowledge required
(certified: T4):

- The **draft's printed equation** (12.19) sums `TX^{1,3} ⊕ N^{6,4}` to
  `Y^{7,7}`: internally consistent and **balance 0** as written and
  mirrored. A single printed equation line carries the uniform-reading
  presumption; a mixed-notation reading of one displayed line requires
  positive evidence, none of which is on record.
- The **transcript's spoken blocks** balance to 4 while its asserted total
  is balance 0 — a one-bit internal inconsistency, already typed
  `SOURCE-UNTYPED` at the last step by the iceberg reinspection.

Primary-source discipline then gives the resolution candidate: **bit 1 =
opposite; the ambient unordered signature is `{7,7}`** — at
primary-display uniform-reading grade, upgradeable to formula grade by C3
below, with the transcript's spoken horizontal typed as flipped relative to
the draft (an error class the mirror artifact's mechanics fully explain).

**Step 4 — corroboration, and the caveat that demoted it.** Under positive
normalization of the family, the achievable set `{(7,3),(6,4)}` is
mirror-asymmetric (T3), which would let each label self-type its writing
convention: the transcript's `(3,7)/(3,6)/(4,6)` type minus-first —
re-deriving the proven mirror through an independent path — and the
draft's `(6,4)` types plus-first, implying a mostly-minus base and total
`(7,7)` (T5). **This argument is corroborating only.** With a free overall
sign on the fiber form the full portrait `{(7,3),(6,4),(3,7),(4,6)}` is
mirror-symmetric (certified: T6), so a bare label does not fix the
convention; only relative data does. The same degeneracy is a scope note
on the 2026-08-08 mirror artifact's "notation is the only explanation
left": notation-mirror and global form-negation are indistinguishable from
signature labels alone. Its operative conclusions are unaffected — every
sum balance used here is invariant across that ambiguity, which is exactly
why this route reads balances and not labels.

## The decisive wave (Wave A) — checks the executing run implements independently

- **C1 (family portrait certificate).** Exact ten-dimensional signatures
  of the `a,b` family over both Lorentzian conventions: the positive-
  normalization set `{(7,3),(6,4)}`, fixed traceless `(6,3)`, degeneracy
  exactly at `b/a = 1/4`, fiber evenness, horizontal oddness, and the
  negated-family portrait. Independent implementation, not a rerun of the
  designer's certificate.
- **C2 (balance tables).** Draft display balance 0 and transcript blocks
  balance 4, as written and mirrored; the planted mixed-notation sum
  reaches balance 0 and **must be flagged** — the control that proves the
  wave can catch the failure mode the eleven files committed.
- **C3 (extraction confirm and grade).** Confirm the verbatim
  eqs (12.18)-(12.19) and the `Spin(1,3)×Spin(6,4)` pairing; search the
  draft §12.9 region and adjacent displays for any formula for the `N_ג`
  metric or the chimeric total metric. A displayed formula fixing the
  relative block sign upgrades outcome (a) to formula grade; a displayed
  formula contradicting balance 0 triggers outcome (b); no formula leaves
  the uniform-reading presumption carrying the result.
- **C4 (planted controls).** The mixed-sum control (C2); a
  negated-vertical control (the balance verdict must be unchanged, per
  T6); a not-in-family label control. A route whose controls cannot fire
  is not a resolver.

## Outcome table (dispositions owned by the wave, not this packet)

- **(a) C1-C2 green and C3 secures formula or uniform-reading anchor.**
  `SIGNATURE-AMBIENT` resolves to the **`{7,7}` horn** at the secured
  grade; `named_resolver` is filled with this route and its certificates.
  No claim is made about writing conventions or the base component — the
  balance verdict needs neither. Consequences the wave must route: (1) the
  `REAL-CLIFFORD-FORM` pressure note dissolves — the settlement's
  `Cl(7,7)` is now backed by the primary display's own consistent
  arithmetic rather than assertion alone; (2) the eleven-file red gate
  repairs to a corrected acknowledgment ("the draft's uniform display
  asserts opposite relative block sign, total `{7,7}`; the previously
  recorded sum mixed conventions"), a change to what seven waves declared
  and therefore carrying its own hostile review; (3) **Wave C transfer
  audit**: identify which K77 sign-sensitive certificates (symmetrizer
  positivity, the `12 w± ℓ∓ = 11` reciprocal signs, Krein inertias)
  consumed a same-sign composite assumption anywhere, and re-run exactly
  those under the resolved relative sign — rank facts transfer, sign facts
  need not.
- **(b) C3 finds a displayed formula asserting a same-sign composite**
  (balance 4). The draft then contradicts its own eq (12.19) sum; this
  route is refuted as a resolver and the contradiction escalates as an
  over-determined row per the finder-escalates rule. That outcome would
  itself be major information.
- **(c) C3 finds no formula and the panel judges the uniform-reading
  presumption insufficient.** `SOURCE-UNDERDETERMINED`: the fork re-types
  rather than resolves — the registry records the exact open datum as one
  relative-sign bit, horn selection is typed as the author's stated choice
  (the v0.89 posture), and the depth liability is priced by an explicit
  fork-posture entry with a wake condition (a new source display fixing
  the bit). This is the route review's rank-4(b) landing, reached with the
  freedom exactly characterized.

## Why the two dead resolvers could not have worked

M-H9 computed an absolute endpoint pair; the declared-base route read an
absolute notation disagreement. Step 1 shows absolute pairs carry no
invariant content here, and Step 2 shows the entire well-posed fork is two
bits, of which the balance bit decides the horn. Both dead resolvers
computed quantities orthogonal to those bits; both died by cancellation or
by mirror. This route reads only unordered-pair balances and
family-portrait invariants, which survive every relabeling the
construction permits.

## Prior art

In-repo: the mirror certificate and its evenness control (2026-08-08);
dc-h1 (2026-08-04); the iceberg reinspection's `SOURCE-UNTYPED` last step
(2026-07-31); the draft §11-12 verbatim extraction (2026-08-03); M-H9's
register post-mortem. New relative to those: the two-bit invariant
reduction, the balance-reads-the-bit mechanism with the `{7,7}`
self-mirror pin, the certified family portrait including the negation
caveat, and the outcome-graded wave design. Literature note for the wave's
own verification: the indefinite DeWitt supermetric and its trace-sector
sign flip are classical (DeWitt 1967 and the supermetric-signature
literature); confirm citations independently before writing them into any
disposition.

## What this packet does not do

No registry row, fork disposition, verdict, residue, canon, or posture
changes; no edit to the eleven files; no `REAL-CLIFFORD-FORM` action. The
packet supplies design, derivation, certificates, and an outcome-graded
wave specification. The executing wave owns every disposition under the
full pre-flight / hostile-review contract, and the two-phase rule governs
anything that later approaches canon.

## Verify status manifest (absorption protocol)

- Step 1 (mechanics), Step 2 (two-bit reduction, portrait, balance pins):
  **CONFIRMED** — designer's certificate green (T1, T2, T4, T6), exact
  arithmetic, both conventions, planted controls firing.
- Step 3 (draft display balance 0; transcript one-bit inconsistency):
  **CONFIRMED** as arithmetic (T4); the uniform-reading presumption on the
  draft's printed line is **SCOPED** — a presumption with stated upgrade
  and defeat conditions (C3), not a certified fact.
- Step 4 (label corroboration): **SCOPED** — valid under positive
  normalization only; demoted by the certified T6 caveat and carried as
  corroboration.
- Outcome table and wave design: **PROPOSED** — the cadence schedules Wave
  A per the route review's rank-4(a), or declines with reasons per the
  absorption protocol.
