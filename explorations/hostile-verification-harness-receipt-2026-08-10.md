---
title: "Hostile-verification harness receipt: three load-bearing results attacked by independent seat pairs plus judges. Three SCOPED, zero REFUTED, zero clean CONFIRMED. The T1-T4 scramble is CARRIER-BLIND (the 192 is pointwise invariant under the whole scramble family); 'W and mirror remain identical' outruns its license; the 40 SM-neutral states get a clean rep-theoretic identity (one per irrep) and an embedding-independence upgrade"
artifact_type: run_receipt
created: 2026-08-10
status: THREE_SCOPED__T1T4_SCRAMBLE_FAMILY_IS_CARRIER_BLIND_P192_EQUALS_P6_TENSOR_I32__W_MIRROR_IDENTITY_CLAUSE_OUTRUNS_LICENSE__40_STATES_ARE_ONE_PER_IRREP_AND_O10_CONJUGACY_INDEPENDENT__MASS_SCRAMBLE_DESIGN_MUST_CHANGE
grade: "EXECUTED: 9 agents (3 targets x 2 diverse seats + 3 judges), 0 errors, ~1.16M subagent tokens, all
  read-only, hourly undisturbed. Seat A rebuilds imported NOTHING. Judges resolved seat disagreements by
  checking decisive facts themselves, including OVERRULING one seat's evidential-record charge after finding
  the sweep files it missed. Verdicts and corrected-claim language below are the judges', quoted."
canon_verdict_change: none
follows:
  - explorations/run-scramble-T1-T4-ambient-not-carrier-2026-08-09.md
  - explorations/conditional-build/conditional-physics-ledger-v0.139.md
  - canon/generation-carrier-identification-scope-correction-2026-08-10.md
---

# Hostile-verification harness: verdicts

## V1 — the T1-T4 scramble result: SCOPED, with a THEOREM-GRADE sharpening

**All headline numbers reproduced from scratch** (independent JW rep, independent K and volume element,
zero repo imports): baseline zeros literal, break ranges matching, the wandering signature set matching, the
`ghost_parity_krein.py:76` silent Hermitization confirmed by feeding the replica non-Hermitian input.

**The sharpening, missed by the original run and by my own framing:** the scramble family is
**CARRIER-BLIND**. The 192 is a **pointwise fixed subspace** of every internal replacement
`(s3 (x) s3) (x) M`:

- `||P' - P0||_F <= 2e-13` across 23 independent runs in three separate builds;
- `P_192 = P6 (x) I32` exactly (`rank(P6) = 6`), provable by Schur;
- hence every scrambled K-spectrum has **exact multiplicity 6**, and **every scrambled signature is
  0 mod 6** — the published wandering set `(96,96),(102,90),(90,102),(108,84)` is itself
  `6 x {(16,16),(17,15),(15,17),(18,14)}`, a prediction the original data contained and nobody checked.

So scrambled T1-T4 values measure **rebuilt ambient operators restricted to a fixed subspace** and carry
**zero carrier-side information**. "Breaking is necessary but not sufficient" UNDERSTATES: the scramble
cannot see the carrier at all. Timelike-blindness and the `T4 = 6 Tr(Omega_int)` identity are corollaries of
the same factorization, not independent findings.

**Judge overruled one seat charge:** seat A alleged the note claimed 32 runs against a record of 14; the
judge located `sweep2_results.json` / `sweep2_graded.py` in the same scratchpad that seat A missed and
counted the record adequate. Residual record defects are real but minor (one range endpoint mixes run
classes; the T1 deviations are spectral-radius-self-normalized without saying so).

**CONSEQUENCE, and it is immediate: the planned mass-scramble design must change.** Any mass functional
built from rebuilt gammas restricted to the 192 reduces to `6 x (32-dim arithmetic)` and its breaking will
carry zero carrier information, exactly like T1-T4. The design must (i) add the projector-invariance check
`||P' - P0||` up front, (ii) run the random-graded-subspace null, and (iii) if it wants to see the carrier,
couple to the subspace nontrivially — i.e. deform base-internal anticommutation, at the already-fenced cost
of `su(2)_+`.

## V2 — the hourly's v0.138 -> v0.139 chain: SCOPED, arithmetic fully holds

Ranks, residuals, and the rank-one quotient condition (`alpha = beta` on the two restricted horns,
`alpha = -beta` on the full-U odd coset) all reproduce. The hourly's own hostile reviews were checked and are
substantive, not rubber stamps.

**The single material defect is one clause in one place.** The v0.139 ledger's own migration text stops at
the licensed strength — "no invariant W or mirror graph." **`NEXT-STEPS.md` adds "; W and mirror remain
identical", which outruns the license.** The judge's corrected sentence:

> "The current q-repaired conditional rival therefore has no invariant W or mirror graph — the rank-64
> lower-left obstruction blocks every southeast completion, not just the zero one — and the gate fails
> exactly symmetrically for W and its mirror, **which remain separable by base-side labels but selected by
> no criterion tested.**"

That is a statement about **one candidate failing**, not about the pair being identical — consistent with,
and not stronger than, the 2026-08-09 finding that the mirror is indistinguishable *by every criterion so
far tried*. Also owed: a machine-token retype (`w_equals_mirror` -> `w_mirror_fingerprints_equal`) in the
gate JSON and its three emitting probes, so the fingerprint semantics stop encoding the overstatement.

## V3 — the canon scope-correction: SCOPED, with an upgrade and a homonym catch

**The 40 SM-neutral states survive a second, independent construction by a different route** (direct
Cartan/root assignment, no CAR ladder) **and gain two upgrades**:

1. **Embedding-independence**: the count holds for any embedding in the O(10)-conjugacy class of the SM
   `su(3)+su(2)+u(1)_Y` — so 40 is a fact about `ker(Gamma)`, not about one convention.
2. **A clean identity**: the 40 are **exactly one SM-singlet per irrep** — the `nu^c` (right-handed-neutrino)
   direction of each 16-type irrep (`32 = 512/16`) and one per 144-type irrep (`8 = 1152/144`). A
   representation count, stated as such.

**The homonym catch (canon-grade):** the canon file's byproduct sentence says the states sit in "the explicit
fixed carrier" — **with "carrier" read as W, the sentence is FALSE**, since the 8 states at Casimir `-21.25`
are 144-type and cannot lie in W. Same-letter collision, seventh of its kind, this one inside a canon file
promoted today. The judge's corrected sentence types "neutral" as SM-singlet (all 12 generators, not merely
Cartan charges) and scopes the location correctly.

Also surfaced, needs the hourly's eyes: **the canon-cited absorption gate dies on an AssertionError**
(needle "action-owned reduction plus carrier discrimination") — 8 of 9 carrier-stack gates exit 1 on the
current tree. Whether that is a stale needle or a real breakage is the hourly's call; flagged, not fixed.

## Owed edits (absorption pattern — flagged for the hourly, not applied)

1. `NEXT-STEPS.md` v0.139 block: replace "; W and mirror remain identical" with the corrected clause above.
2. `lab/process/selected-k77-southeast-zero-graph-gate.json` + three emitting probes: fingerprint-token
   retype.
3. `canon/generation-carrier-identification-scope-correction-2026-08-10.md` lines 34-36: the corrected
   40-states sentence (SM-singlet definition, one-per-irrep identity, O(10)-conjugacy independence, "not W"
   scoping); lines 22-24: type the split as unconditional substrate arithmetic vs W-conditional theorems.
4. `explorations/run-scramble-T1-T4-ambient-not-carrier-2026-08-09.md` title/status: add the carrier-blind
   sharpening; disclose the self-normalization; split the T4 range by run class.
5. The absorption-gate AssertionError (item above).
6. **The mass-scramble redesign requirement** — the most consequential item; see V1.

## Meta-result

Ten hostile verifies have now run across two days at two model tiers: **ten SCOPED-or-REFUTED, zero clean
CONFIRMED — and zero arithmetic failures.** The signature is stable: this repository's computations are
reliable and its *sentences* are not. The marginal token is best spent exactly where it was spent here — on
independent rebuilds and licensed-strength audits — and the two claim-strength defects this harness caught
(the identity clause; the carrier homonym) were both on surfaces promoted within the last 24 hours.
