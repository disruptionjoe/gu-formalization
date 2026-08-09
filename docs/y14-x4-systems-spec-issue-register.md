---
title: "Y14/X4 systems spec: issue register (25 persona seats x 3 issues, severity-graded)"
doc_type: issue_register
status: open
created: 2026-08-09
companion_to: docs/y14-x4-systems-spec.md
spec_version_at_filing: "1.0"
grade: "PROCESS ARTIFACT. Contains no physics claims. Every issue is about the DOCUMENT, not about GU.
  Personas run inline per house convention; no issue here changes a verdict, a claim status, or canon."
claim_status_change: none
canon_verdict_change: none
---

# Issue register — `docs/y14-x4-systems-spec.md` v1.0

75 issues, three per persona seat, filed against the frozen 1.0 baseline. **1.0 ships with all of them
open, by design** — the baseline was saved to make subsequent change diffable, not because it was finished.

## Severity scale

Tuned to this repository's actual risk model rather than a generic P0-P3 ladder. The dominant hazard here
is not that the document is wrong; it is that its analogy content gets cited as result.

| level | meaning |
|---|---|
| **S1** | **Miscitation hazard.** A reader could lift something from this document and use it as a result it is not. Highest severity because it is the exact failure mode the repository's grading discipline exists to prevent. |
| **S2** | **Load-bearing error or omission.** Something stated is wrong, rests on a retracted or mistyped object, or is missing such that a conclusion in the document is unsupported. |
| **S3** | **Rework.** Causes confusion or wasted effort; no wrong conclusion. |
| **S4** | **Hygiene.** Cosmetic. |

---

## Cluster A — Physics

**1. Representation theorist**
- **S1** — Sec 7.3 states `(+96,-96,0)` with no accompanying statement that multiplicity is not index. A reader can lift it as a count. This is the documented Layer-0 failure mode, reproduced in the spec.
- **S2** — Sec 2.3 stops at `ker Gamma = 1664` with no Casimir split, so a reader cannot tell where matter lives and may attach "generation" to the wrong summand.
- **S3** — No Casimir check constant (`-11.25`), so a re-derivation has nothing to verify against.

**2. Four-dimensional geometer**
- **S2** — Sec 3.3 states `dim Lambda^2 V = 91` with no derivation; `C(14,2)` is not obvious to the audience this document targets, inviting a wrong recount.
- **S3** — The `Lambda^2_+` origin of every 3 in the document is missing, which makes Sec 9.3's "count not in schema" read as unmotivated rather than structural.
- **S4** — "4-dimensional" is used for both `X4` and the base of `Lambda^2` without distinction.

**3. Krein / ghost-parity physicist**
- **S1** — Sec 7.6 lists `[P,S]=0` under invariants that "MUST hold" while noting it is unverified. An unverified assumption inside a MUST list will be read as holding.
- **S2** — The document never states the state space is doubled. Structural, not cosmetic; see the rollup.
- **S3** — "Ghosts kept and graded" is stated but not explained enough for a reader to avoid defaulting to the SUSY-removal picture.

**4. Reality-class / parity physicist**
- **S1** — Sec 2.3 lists both forks and the document never commits downstream, so any number a reader lifts may be from the wrong horn. This is precisely the "do not import K95 coefficients into K77" warning, violated by omission.
- **S2** — D5 is filed as a defect when it is a *theorem about method*: complexified computations are provably incapable of deciding the fork. It should constrain future work, not sit in a defect table.
- **S3** — No `p-q mod 8` reality-class table.

**5. Index / source-action physicist**
- **S1** — Sec 6 states "Einstein-Hilbert is induced, not added" without scoping it as the program-native construction. Directly citable as a result it is not.
- **S2** — Sec 6 presents the Gauss identity as "the reconciliation equation," but the document's own text says it holds **as a tautology for any section**. A tautology carries no dynamical content; the framing overstates it.
- **S3** — The source action's own field equations are absent.

---

## Cluster B — Computation

**6. Type theorist**
- **S1** — `[ANALOGY]` rows are formatted identically to `[MATH]` rows inside the same tables. Visual parity invites exactly the miscitation the grading was introduced to prevent.
- **S2** — `[UNSPECIFIED]` conflates *free parameter* (a property, closable never) with *unbuilt object* (a gap, closable in principle). A reader cannot tell which gaps are reachable.
- **S3** — No type signatures for `pi`, `sigma`, `Phi`.

**7. Parity accountant**
- **S1** — The retired `{2,7,13}` argument is not recorded anywhere, so a reader could re-derive and re-publish a known non-sequitur.
- **S2** — `chi = chi_interior + chi_external` is absent, so Sec 9.3's externality claim appears in the document with no visible support.
- **S3** — No parity table (interior even, observed odd).

**8. Compiler engineer**
- **S1** — **No staleness detection.** The document snapshots canon files with a documented high correction rate (W2-01, SHIAB-01/05, DARK-ENERGY-01..06, RFAIL-02/03) and has no mechanism to detect when a source moves underneath it. It will rot silently and keep looking authoritative.
- **S2** — No source revision pins; `follows:` lists paths but not states.
- **S3** — Free parameters are never aggregated into one count.

**9. Quantum-error-correction / operator algebra**
- **S1** — Sec 7 mixes proven, computed and assumed invariants under one "MUST hold" heading with no marking.
- **S3** — Access structure (what is observable versus structurally not) is absent.
- **S4** — No test-file references for the certified constants.

**10. Complexity theorist**
- **S2** — The document claims roughly a third of itself is `[UNSPECIFIED]` but never counts, so its own headline claim is unfalsifiable as written.
- **S3** — No statement of what would make the document wrong.
- **S4** — Compressible (documentation) versus irreducible (analysis) gaps are unmarked.

---

## Cluster C — MMO

**11. Character-slot designer**
- **S2** — The absent count field appears only in Sec 9. Someone reading Sec 2 as "the schema" gets a schema that silently omits its most contested field.
- **S3** — No "what the reader must supply" section.
- **S3** — "Observer" is undefined.

**12. Instancing engineer**
- **S1** — The doubling is absent, so a reader takes "three generations" from Sec 9.3 and never learns the substrate holds six in mirror pairs. Highest-value omission in the document.
- **S2** — `(+96,-96,0)` appears only in Sec 7, where it reads as a constraint to preserve rather than as the shape of the state space.
- **S3** — Primary/mirror is not a first-class relation in the object inventory.

**13. Interest-management engineer**
- **S2** — Sec 3.4 declares the network analogy broken, then the document keeps using "read path," "transport" and "codec" afterward. Internally inconsistent with its own warning.
- **S3** — No statement of what is observable at what scale.
- **S3** — "Observer" undefined, blocking any area-of-interest reading.

**14. Netcode / authority engineer**
- **S1** — Sec 5 says no global operator exists and Sec 9.2 says the sequencer is missing. Read together without a note, a reader concludes the system is *inconsistent* rather than *AP*. Needs an explicit "this is a classification, not a defect."
- **S2** — The selector is typed as a missing function rather than as a missing authority.
- **S3** — No reconciliation trigger: nothing says when selection occurs.

**15. Loot-table / seed designer**
- **S2** — The observables the spec must eventually explain (masses, mixings) are never listed, so the document has no acceptance criteria for its own completion.
- **S3** — Drawn versus designed quantities are unmarked.
- **S4** — The mass hierarchy is unmentioned.

---

## Cluster D — Networking

**16. VLAN / tagging engineer**
- **S2** — No statement of which quantities vary by generation and which do not. For the audience this document targets, that is the single most useful table, and it is absent.
- **S3** — Flavor-changing processes unmentioned.
- **S4** — The header/payload framing is introduced and not carried through.

**17. Protocol-versioning engineer**
- **S1** — **No version-compatibility contract with sources.** If canon corrects, the document silently disagrees with it and nothing states which wins. Combined with issue 8's S1, this is the document's most likely long-run failure.
- **S2** — K77/K95 are not versioned as two protocol states with a migration note.
- **S2** — No deprecation policy for retracted results; the W94 incident is recorded as an anecdote rather than a rule.

**18. Multipath / ECMP engineer**
- **S3** — Degeneracy is never stated as a property: the three are *exactly* equal-cost in everything but mass.
- **S3** — What breaks the tie is unstated.
- **S4** — Whether the three are independent is unstated.

**19. Wire-format / endianness engineer**
- **S2** — D6 is named without a proposed format. A defect listed twice and never fixed is worse than one not listed, because the listing reads as handling.
- **S3** — Generation index ordering is undefined; nothing says which is "first."
- **S4** — No conversion rule at boundaries.

**20. Firewall / boundary engineer**
- **S1** — Sec 10 says "not a closed system" and Sec 9 lists the gaps, but nowhere does the document state that the firewall-boundary reading is **the repository's primary falsification target, to be attacked**. A reader takes it as the house position rather than the house hypothesis. Serious, because canon is explicit on this point and the spec inverts its posture.
- **S2** — The boundary object's interface is unspecified.
- **S3** — No list of what the boundary must supply (parity, count, scale).

---

## Cluster E — Sharding

**21. Shard-key designer**
- **S1** — Sec 9.3's "count is external" can be read as settled. It is external **by structure modulo an open analytic residual**, and that qualifier lives in Sec 9.5, far from the claim.
- **S2** — Schema facts and deployment facts are interleaved throughout rather than separated.
- **S3** — No acceptance criteria for what would count as a valid external datum.

**22. Replication engineer**
- **S2** — Replication factor 2 is never stated as derived, so a reader cannot tell that the 2 and the 3 have different provenance.
- **S2** — `96 = 3 x 2 x 16` is absent from Sec 2.
- **S3** — No read/write path per replica.

**23. Consistency / CAP theorist**
- **S1** — **"AP" is an analogy label applied to mathematical objects, and Sec 5 formats it as a classification with a table.** Highest miscitation risk in the document; someone will cite "GU is AP" as a finding.
- **S2** — Sec 4.3 concludes you cannot state a convergence criterion, which undercuts Sec 5's claim that eventual consistency holds. Unresolved internal tension, and the Sec 4.3 inference is unsourced.
- **S3** — The mixing-as-residual conjecture is not quarantined into a speculative appendix.

**24. Composite-key engineer**
- **S2** — The CRT two-arena split `pi_3^s = Z/24 = Z/8 + Z/3` is absent, so the document cannot explain to a reader why no obstruction has ever touched the count.
- **S2** — No "which arena does this live in" field for future findings.
- **S3** — The `Hom(Z/3, Z) = 0` blocker is absent.

**25. Resharding / migration engineer**
- **S1** — No provenance or retraction section. The document inherits corrected results and a reader cannot tell what was retracted, when, or by whom.
- **S2** — No K95 -> K77 migration note.
- **S3** — No statement of what a future re-derivation must preserve.

---

## Rollup

**15 S1, 26 S2, 24 S3, 10 S4.**

### Two root causes generate most of the S1s

**Root cause 1 — the document does not visually distinguish its own confidence tiers.** `[ANALOGY]` rows
look like `[MATH]` rows (6); the AP classification is formatted as a result (23); unverified assumptions sit
inside a MUST-hold invariant list (3, 9); a hypothesis under active attack is presented as the house
position (20); a claim with an open analytic residual is stated without its qualifier nearby (21); and the
retired `{2,7,13}` argument is not recorded as retired (7). Six S1s, one cause: **grading exists in the
document but is not enforced by its layout.**

**Root cause 2 — the document has no contract with its sources.** No staleness detection (8), no version
compatibility (17), no provenance or retraction section (25). Three S1s, one cause: **the document snapshots
a fast-correcting corpus and cannot tell when it has gone stale.** Given the correction rate visible in
canon, this is the issue most likely to actually bite.

The remaining S1s are content: the doubling is missing (12), the selector is mistyped (14), the fork is
uncommitted (4), multiplicity-vs-index is unstated (1), and the induced-gravity claim is unscoped (5).

### Recommended ordering for 1.1

1. **Enforce the grading in layout** — one change, retires six S1s. Separate `[ANALOGY]` content into
   visibly distinct blocks; move the AP classification behind an explicit "this is a lens" banner.
2. **Add a source contract** — pin revisions, add a staleness note, add a retraction section. Retires
   three S1s.
3. **Model the doubling and retype the selector** — the two content changes carried over from the
   improvement pass; these are MAJOR (they change what the document says), so they land as 2.0, not 1.1.
4. Everything else batches into 1.x by cluster.

### Note on what this register is not

No issue here is a finding about Geometric Unity. All 75 are about a document. The register is filed so the
spec's known defects are legible from outside rather than living in one session's context.

---

# Addendum — coverage sweep, 2026-08-09 (filed against 1.0, actioned in 1.1)

A sweep of the spec against all 57 `canon/` files. Distinct from the 75 issues above: those are about
document quality, these are about **coverage** — canon results the spec does not represent at all.

## Actioned in 1.1

- **APS residual mis-stated (S1, was a live error in a published document).** 1.0 Sec 9.5 claimed the
  function-space RS APS + family-index statement is "not closed," while listing in `follows:` the canon file
  that closes it. `canon/function-space-index-conservation-residual-closure-RESULTS.md` discharges all three
  residuals at computed + independently re-verified grade. **Corrected in 1.1**; the real residual is
  `model -> true-RS-Y14-bundle` transfer.
- **"Totally null" homonym guard (S2).** Sweep reported this as refuted by
  `canon/hessian-z3-carrier-occupancy-RESULTS.md`. **Checked directly: not refuted.** That file targets the
  *flat modulus / zero mode* reading (`ker(B) = 0`, spectrum `{+1 x96, -1 x96}`, `B^2 = I`), which the spec
  never makes. "Totally null" here means *totally isotropic subspace*, ordinary for a balanced `(+n,-n)`
  form. Both hold, of different objects. Guard note added in 1.1 so no later reader collapses them.
  **This is itself a Layer-0 instance and is logged as one.**
- **`mu_DW` provenance (S3).** No `canon/` referent; grade rests on `GEOMETER-VS-PHYSICS-OBJECTS.md` and
  `papers/candidates/`. Caveat added in 1.1.

## In-scope coverage gaps — canon results absent from the spec (ranked)

| # | result | file | note |
|---|---|---|---|
| G1 | Good-stable compactification no-go | `canon/good-stable-compactification-no-go-RESULTS.md` | a theorem about `Sp(32,32;H)`, the exact arena the spec names |
| G2 | `ker(Gamma)` Casimir split; the 192-dim `j=1` carrier | `canon/source-action-seiberg-witten-RESULTS.md` | spec quotes 1664 but never names the carrier every downstream theorem runs on. **Highest priority** |
| G3 | The Seiberg-Witten source action itself | `canon/source-action-seiberg-witten-{RESULTS,construction}.md` | the object Sec 9.6 routes into |
| G4 | `Omega^{Pin+}_14 = Z/2` | `canon/pin14-bordism-derivation-RESULTS.md` | a dimension-14 bordism fact about `Y14` |
| G5 | Bulk RS index (`I_{3/2} = 21 sigma/8`; `ind Q = -38`) | `canon/rs-function-space-framework-SPEC.md`, `canon/gamma-traceless-38-adjudication-RESULTS.md` | spec has boundary eta, no bulk index |
| G6 | Two-arena rep-theory core (Lean-checked) | `canon/two-arena-rep-theory-core-RESULTS.md` | `dim Hom(S+ (x) S+, Lambda^0) = 0`; `pi_3^s = Z/24` |
| G7 | Order-3 equivariant rho | `canon/order3-equivariant-rho-RESULTS.md` | first nonzero order-3 spectral class in the program |
| G8 | Boundary e-invariant on `RP^3`, tangential-vs-gauge fork | `canon/boundary-einvariant-and-the-tangential-fork.md` | unresolved fork on the spec's own fiber homotopy type |
| G9 | Signed-readout boundary theorem; OC1/OC2 undischarged | `canon/signed-readout-boundary-theorem-RESULTS.md` | the analytic layer under Sec 2.2's "ends" row |
| G10 | Antilinear index-nullity theorem | `canon/antilinear-bound-RESULTS.md` + `-nonkrein-` | operates on the 192 carrier |
| G11 | Enum-completeness + KO ladder + two-primary lemma | `canon/enum-completeness-class-c-RESULTS.md`, `canon/ko-degree-obstruction-ladder-RESULTS.md`, `canon/two-primary-lemma.md` | the backing for Sec 9.3 |
| G12 | Willmore section equation for `sigma` | `canon/schwarzschild-weak-field-rfail.md` | the section's own field equation; spec has the Gauss identity but not this |
| G13 | Normal-bundle deflation `14 = 4 + 10` (H4b), Higgs `= ||F||^2` (H5), `Dirac^2 = Lichnerowicz` (H6) | `docs/NEXT-FRONTIER-HYPOTHESES.md` | unbuilt, in scope |
| G14 | Lean certificate surface | `Lean/GUFormalization/*.lean` | spec cites w2 and 2-torsion without noting which are machine-checked |
| G15 | Six-axis protocol is L1-L7 + Layer-0 | `canon/six-axis-specification-protocol.md` | how the spec's no-gos should be framed |

## Reported contradictions NOT yet verified — do not act on these without checking

The sweep reported five further contradictions. **Only the two above were verified by direct read; one of
those turned out not to be a contradiction at all.** Given that hit rate, the remainder are logged as
unverified leads, not findings.

- **C3** — `Sp(32,32;H)` may not be settled: `canon/anchor-scale-graded-ig-algebra-RESULTS.md` reportedly
  names an open real-form fork (`u(64,64)` vs centerless quaternionic `g_H`).
- **C4** — ghost keep-and-grade `[P,S] = 0` reportedly near-closed **negative**
  (`canon/ghost-parity-krein-synthesis.md` 2026-07-06 update; `canon/swing-ghost-parity-no-chiral-selection.md`).
  If true this is material for Sec 7.6 and for the selector story.
- **C5** — "families index 2-torsion 3-free" may be too strong; nonzero order-3 classes reported in the
  equivariant/Nikulin sector.
- **C6** — frame-triviality metatheorem reportedly **fails on the 192-dim carrier** while holding on 1792.
- **C7** — `mu_DW` has no canon referent. **Verified and actioned in 1.1.**

Each wants a direct read before it moves anything.
