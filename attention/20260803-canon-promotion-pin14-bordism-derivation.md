# Canon Promotion Notice: Pin+ degree-14 bordism derivation (Omega^{Pin+}_14 = Z/2)
<!-- promotion commit: d7da216 -->

- **Kind:** awareness notice — promotion already executed, not a request for approval
- **Source repo:** gu-formalization
- **Promoted by:** register-execution agent (branch `agent/operator-anomaly-big-swing`; register item M-M11, lab/process/improvement-register-2026-08-03.md; audit topo-10/HB-06)
- **Date:** 2026-08-03
- **Commit:** (uncommitted at filing time — this session is edit-only; the executing orchestrator commits and should backfill the hash)

## What was promoted
- Artifact(s): `explorations/pin14-smith-route-audit-2026-07-22.md` (result held there at exact-but-recited grade) -> `canon/pin14-bordism-derivation-RESULTS.md` (+ `CANON.md` row: "Canon Entry Added 2026-08-03", derivation grade, internal tier, GU-independent)
- Grade change: exploration with recited multiplicity -> canon (public-spine framing) at DERIVATION grade. The chain: `Omega^{Pin+}_14 ~= reduced Omega^Spin_13(BZ/2)` (Smith, using `Omega^Spin_13 = Omega^Spin_14 = 0`); ABP splitting `MSpin ~= ko v Sigma^8 ko v Sigma^8 ko<2>` through degree 15, calibrated against known `Omega^Spin_8..12` (and reproducing the degree-13/14 vanishings); `ko~_13(BZ/2) = ko~_5(BZ/2) = 0` (degrees 4,5,6 mod 8 vanish); `ko<2>~_5(BZ/2) ~= (tau_{<=1}ko)~_6(BZ/2) ~= H~_5(BZ/2;Z/2) = Z/2` since `Sq^2 = C(5,2) = 0 mod 2` on `H^5(RP^infty)`; cross-check `~= Omega^{Pin-}_12 = Z/2` (ABP exponent + Kirby-Taylor, now corroboration only). Plus the coprimality remark: 14-dim Pin wall `Z/2` is CRT-disjoint from the 13-dim framed receptacle `Z/3` — the Pin flavor cannot contaminate the count.
- Verdict touched? **NO — canon framing only.** The generation count stays OPEN; the GU class-realization question stays OPEN and is explicitly restated as open in the canon file.

## The case FOR
All six Promotion-Rule criteria are addressed in the canon file's own six-criteria block: scope is the ambient group only; the proof is the five-step chain with named falsification targets (a missed MSpin summand below degree 16, a nonzero ko-term, a k-invariant error, a Smith degree-bookkeeping error); assumptions are the cited structural theorems with 2-locality justified by the AHSS 2-primarity of `Omega~^Spin_*(BZ/2)`; failure modes are named with their mitigations (the seven-row calibration table; `H~_6(BZ/2;Z) = 0` making the answer depend only on the computed `Sq^2` map; the independent Step-5 cross-check); no internal work-artifact dependency; and the consistency sweep left no stale stronger status (the July exploration carries a same-day promotion/supersession note; the type gate's honest self-description is quoted, not upgraded). Decisively: this promotion satisfies the repo's OWN binding gate — the 2026-07-21 planted-toy rule ("reciting a published |Omega^{Pin+}_14| ... would be exactly the planted-toy over-claim — genuinely reconstruct or report BLOCKED", `explorations/pin14-anomaly-number-2026-07-21.md:186` and the portfolio T1 line) — by computing the multiplicity that was previously recited from Kirby-Taylor's table.

## The case AGAINST (steelmanned)
Strongest honest objection: the derivation still *cites* computed literature (the ABP splitting itself, the `ko_*(BZ/2)` vanishing pattern, the ABP Pin exponent), so a hostile reader could call it "recitation one level down." Response checked rather than waved away: the anti-recitation gate bans reciting *the answer*; every cited input here is a general structural theorem or a different computation, none is `Omega^{Pin+}_14`, and the one former answer-recitation (KT `A(14) = 1`) is demoted to a cross-check of a quantity Steps 2-3 compute. Second objection: the runnable gate (`pin14_smith_degree_gate.py`) is a literal-tautology type gate (audit P-H10), so the promotion has no derivation-grade certificate. Response: the canon file says exactly that, claims nothing from the gate beyond bookkeeping, and leaves the literal-derivation gate to the P-H10 campaign. Third: the truncated ABP wedge could miss a summand below degree 16; the calibration table against `Omega^Spin_8..14` is the check, and the Step-5 cross-check is independent of the splitting entirely. Weakest load-bearing dependency: the `ko<2>` k-invariant convention (`Sq^2`); mitigated by `H~_6(BZ/2;Z) = 0` and the cross-check.

## How the call was made
FOR outweighed AGAINST because the register (M-M11) and the audit (HB-06) had already identified the gap as *status mislabeling* (recitation carried at derivation-adjacent confidence), and the missing derivation was assembled and internally cross-checked two independent ways that agree (Steps 2-4 vs Step 5). The objections were retired by scoping: the canon file's input ledger separates computed / cited-structural / cited-table-cross-check explicitly, so no reader can mistake the epistemic status of any step.

## Risks
Downstream consumers of the *value* Z/2: the M-M12/Freed-Teleman probe ("is GU's class the nontrivial element of `Omega^{Pin+}_14`"), the anomaly/firewall-home discussion, and the coprimality argument now cited by the count program. If the derivation later proves wrong the blast radius is small: the value itself is independently in Kirby-Taylor's published table (so consumers of the value are safe); what would fall is only the derivation-grade label and the anti-recitation credit. The class-realization gap is explicitly open, so no physics claim rides on this.

## Support
- `tests/channel-swings/pin14_smith_degree_gate.py` — exit 0; bookkeeping/type gate ONLY (its own receipt; audit P-H10) — checks the Smith degree shifts, not the derivation.
- No Lean content; no new certificate added (deliberate — see the canon file's Support section; a literal-derivation gate is P-H10 campaign work).
- Same-day consistency edits: `CANON.md` row; promotion note in `explorations/pin14-smith-route-audit-2026-07-22.md`; the coprimality remark cross-referenced by `explorations/rho-invariant-two-primary-immunity-lemma-2026-08-03.md` (which uses `Omega~^Spin_13(BZ/2) = Z/2` as its degree-13 exponent input).

## Reversal
Revert the promotion commit (delete `canon/pin14-bordism-derivation-RESULTS.md`, strike the 2026-08-03 `CANON.md` section, strike the promotion note at the end of `explorations/pin14-smith-route-audit-2026-07-22.md`, remove this notice). The July exploration then again holds the result at exact-but-recited grade. No downstream migration required: no verdict, paper draft, or other canon file consumes the derivation-grade label (as opposed to the value).

<!-- System Attention indexes the owner-source pointer as unread. Runtime may archive the
pointer envelope only after the pointer appears in the Attention awareness index.
Envelope filing to ../../../repos/private/system-runtime/mailboxes/system-attention/ is the
orchestrator's step (this session is scoped to this repository only). -->
