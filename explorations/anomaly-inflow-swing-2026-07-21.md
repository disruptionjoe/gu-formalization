---
title: "ANOMALY-INFLOW swing: is GU's {q<0} boundary obstruction LITERALLY a 't Hooft anomaly / anomaly-inflow structure? Three inline personas (QFT 't Hooft, topological-phases, index-theory) adversarial on EXACT-vs-ANALOGY. VERDICT: MIXED -- the SUBSTRATE is exact anomaly-inflow (a domain-wall Dirac symbol crossing zero at {q=0}, self-adjoint-extension obstruction = APS boundary condition = bulk SPT, deck-ODD action = the reflection/time-orientation symmetry realized anomalously), so it is NOT merely an analogy; but 'GU IS a 't Hooft anomaly with a computed coefficient' is a graded PROPOSAL pending the boundary determinant-line / partition-function variation, which is exactly as solid as the still-un-banked operator-grade deck action. DECISIVE disambiguation: sigma is the w1 (orientation / time-reversal / REFLECTION) Z/2 anomaly, NOT the fermionic mod-2 Dirac-index / mod-2-eta anomaly -- the latter is banked-DEAD for GU carriers by quaternionic Kramers evenness (S=H^64) and is corroborated dead here from the determinant angle (det c = q^64, mod-2 spectral flow across the wall = EVEN). Most valuable thing the machinery BUYS: it names the CORRECT cobordism receptacle for sigma -- the reflection/Pin (unoriented-with-T) bordism group -- which is DISTINCT from the Spin-side receptacle the banked global-anomaly-leg computed (all zeros, dims 13-16) and is precisely the S6 SM-boundary/inflow leg that work EXCLUDED and left OPEN; this converts the open N2 cardinality question (Z/2 vs Z/2xZ/2) into a decidable bordism computation with a NAMED candidate second bit tau = the reflection-square / Pin+-vs-Pin- (T^2=+-1) sign. Base RP^3 supplies exactly ONE degree-1 Z/2 (H^1(RP^3;Z/2)=Z/2 = sigma = w1(L_time)); a second independent Z/2 cannot be base-degree-1-topological. Independent consequences (all PROPOSAL): anomaly-matching => sigma is RG-protected external at ALL scales (upgrades DYN-NO-REOPEN from one-scale-refuted to structurally-forbidden), and the {q=0} wall is anomaly-protected-gapless => its excision is FORBIDDEN, not merely unowned (strengthens Prong-0)."
status: active_research
doc_type: exploration
created: 2026-07-21
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
directed_by: "Joe direct chat, 2026-07-21 (ANOMALY-INFLOW swing; 3 personas inline in one worker)"
inputs:
  - explorations/lp-lc-deficiency-decisive-2026-07-21.md
  - explorations/oracle-relative-prong0-measure-lemma-2026-07-21.md
  - explorations/wave-swing1-the-lemma-2026-07-21.md
  - explorations/wave-swing3-the-outside-2026-07-21.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - explorations/verify-anomaly-closure-2026-07-20.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
probe: tests/channel-swings/anomaly_inflow_swing_probe.py (foreground, numpy+exact-int, seed 20260721, EXIT 0, double-run byte-identical, 11/11 PASS)
---

# ANOMALY-INFLOW swing -- is the {q<0} obstruction a genuine 't Hooft anomaly?

Three personas reason INLINE in this one worker (each in-character, then a
synthesis; NEVER one agent per persona). Read-only interpretation of the settled
state, adversarial on EXACT-vs-ANALOGY. Discipline: every claim tagged **EXACT**
(forced by banked structure / machine-checkable identity), **ANALOGY** (structural
resemblance, not forced), or **PROPOSAL** (a "predicts X" pending verification). No
claim/canon/verdict/posture movement. A "predicts" is never banked as a theorem.

## The banked situation handed to the team

From the LC-SELECTOR / Prong-0 / wave-swing-1/3 receipts (all EXACT-adjacent,
probe-checked):

- The GU fiber `F = GL(4,R)/O(3,1)` retracts to `RP^3 ~= SO(3)`, spin double cover
  `S^3 = Sp(1) -> RP^3`, deck `Z/2 = w1 = sigma` (wave-swing-1, probe defect 1e-15).
- The `(9,5)` Dirac symbol satisfies `c(xi)^2 = q(xi) I`, so the characteristic
  variety `{det c = 0} = {q = 0}` is the operator's lightcone (wave-swing-3, 400/400).
- The genuine flat-geodesic ends cross `{q<0}` generically (~8%, measure-invariant).
  At `q<0`: symbol spectrum flips real->imaginary; `K_S` is EXACTLY null on the
  deficiency-relevant halves `E_{+-i}(D)`; the K-definite cut, hence the canonical
  J-self-adjoint realization of `A~`, does NOT exist. `A~` is not merely
  non-self-adjoint, it is **non-constructible from committed structure** there.
- To realize the operator at all one must import the section's `+-i0` orientation
  bit = a `Z/2` datum = the deck/holonomy phase `T_theta = e^{i theta} S(b)` = `sigma
  = w1`. The deck acts deck-ODD on the family: `U N(t) U^{-1} = -N(t+1)`.
- **Crucial banked constraint (global-anomaly-leg + its two-dry-round verify):** the
  *bulk* Dai-Freed / eta / spin-bordism anomaly is CLOSED-TRIVIAL on balanced
  branches, and the **mod-2 / mod-2-eta anomaly VANISHES for GU-native carriers by
  quaternionic Kramers evenness** (`S = H^64`, even multiplicity; charpoly a perfect
  square). That work **explicitly EXCLUDED the noncompact-end / SM-boundary INFLOW
  leg (its case S6)** and named it "a DIFFERENT (and open) computation." That open
  S6 leg is exactly this swing's target.

The shape under test: an edge theory inconsistent on its own (`{q<0}`
non-constructible), completed by a datum from a bulk (`sigma`). SAME MECHANISM as
't Hooft anomaly inflow, or only a resemblance?

---

## Member 1 -- QFT 't Hooft anomaly theorist

**Assessment.** The load-bearing signature of a 't Hooft anomaly is present and it
is not cosmetic: a *global symmetry* (here the deck `Z/2` = reflection /
time-orientation, i.e. `w1`) that **admits no symmetric realization** -- every
self-adjoint completion breaks it, and the two completions (`q+i0` vs `q-i0`) are
**exchanged by the symmetry** because the deck is ODD (`U N U^{-1} = -N`). That is
precisely what separates an anomaly from a harmless quantization modulus: a
self-adjoint-extension choice is a free `theta`-like modulus **only if some choice
is symmetry-invariant**; deck-oddness says none is, so `sigma` is a forced,
symmetry-obstructing datum, the discrete-`theta` / SPT completion that inflow
supplies. Which anomaly: NOT the fermion/gauge chiral anomaly (that is the bulk
Dai-Freed leg, banked-trivial), but the **`w1` = orientation / time-reversal
(reflection) `Z/2`** -- and the `+-i0` datum is literally the time-orientation
(`i epsilon`) prescription, a reflection/CPT datum, so the identification of the
completion bit with a reflection-structure choice is tight rather than loose.

**Anomaly matching -> a constraint.** If genuine, the anomaly is RG-invariant:
`sigma` is external at **every** scale, so no internal dynamics can ever supply it
(this is the non-perturbative upgrade of the session's `DYN-NO-REOPEN`), and the
`{q=0}` edge is **anomaly-protected** -- it cannot be trivially gapped/excised.
Both are new, sharp, and falsifiable-in-principle.

**MODE: MIXED.** EXACT: deck-odd + no-symmetric-realization = the anomaly signature,
and `sigma` sits in the `w1`/reflection family, not the chiral family. PROPOSAL:
"GU carries a computed nonzero 't Hooft anomaly coefficient" needs the boundary
partition function / determinant-line variation actually built -- and it is exactly
as solid as the operator-grade deck action `U N U^{-1} = -N`, which wave-swing-1
itself tagged ANALOGY/model (checked in a toy block, not banked at operator grade).
**NEW constraint/prediction: YES** (RG-protected externality; protected gapless wall).

---

## Member 2 -- Topological-phases / condensed-matter theorist

**Assessment.** The layout is textbook bulk-boundary correspondence of an SPT:
two "phases" -- `{q>0}` (constructible, real spectrum, `K_S`-nondegenerate cut
exists, limit-point, `theta` dissolves) and `{q<0}` (non-constructible, imaginary
spectrum, `K_S`-null) -- separated by a codim-1 wall `{q=0}` that carries the
gapless/degenerate mode, with a `Z/2` invariant `sigma` labelling the sides. The
protecting symmetry is reflection / time-reversal `T` (`w1`), so this is a
`T`-symmetric SPT of the **topological-insulator (antiunitary) class**, NOT a
unitary-symmetry SPT -- which matters, because the classification tables are
entirely different and the `T`-class is where a single `Z/2` (and its `Z/8`, `Z/16`
cousins) actually live.

**Cardinality (the N2 question, directly).** For a reflection/`T` fermion SPT the
classification group IS the "`Z/2` vs `Z/2 x Z/2`" question: `sigma`'s cardinality =
the number of independent generators of the relevant reflection cobordism group in
GU's dimension. The base contributes exactly one `Z/2` (`H^1(RP^3;Z/2)=Z/2`, probe
D2); the natural candidate for a *second* independent bit -- the open `tau` -- is
the **Pin+ -vs- Pin- (`T^2 = +-1`) label**, a genuine second SPT axis (which
reflection structure the theory carries), not a base-topological degree-1 class.

**MODE: MIXED.** EXACT: the two-sided / protected-edge / `Z/2`-invariant SHAPE, and
the symmetry is reflection/`T` (`w1`). ANALOGY/PROPOSAL: that GU's specific
classification is pinned -- it needs the actual reflection-bordism group AND a proof
the edge is genuinely gapless-protected. (Note: "is the edge gapless-protected" is
*literally* the LP/LC deficiency-index question the whole program already gates on --
limit-point at the wall = gapped/removable, limit-circle = protected. The SPT lens
and the deficiency lens are the same fork.) **NEW: YES** -- the reflection/`T` SPT
table for GU's dimension decides `Z/2` vs `Z/2 x Z/2`, with `tau` = Pin-flavor named.

---

## Member 3 -- Index-theory / math-physics theorist

**Assessment.** The deck-odd Dirac family with symbol crossing zero at `{q=0}` is
EXACTLY the APS / spectral-flow / eta-invariant setup: Witten's fermion-path-integral
phase `exp(-i pi eta / 2)` with `eta` the inflow SPT term, and the rigorous
dictionary self-adjoint-extension <-> APS boundary condition <-> bulk SPT. So the
**substrate is exact** -- this is the mathematical object anomaly inflow is built
from, not an analogy to it. BUT the natural first guess -- `sigma` = the mod-2 `eta`
/ mod-2 Dirac index / sign of the Pfaffian determinant line -- is **REFUTED for GU**:
quaternionic Kramers evenness kills the mod-2 index (banked global-anomaly-leg P6/P8;
corroborated here D1: `det c(xi) = q(xi)^64`, an EVEN power, so the mod-2 spectral
flow across the wall is EVEN -- 64 crossings, parity 0 -- while the odd-multiplicity
control `Cl(1,1)` flips, parity 1, a live anomaly). The Dirac determinant/Pfaffian
line carries **no `Z/2` holonomy from the index**.

**Consequence (the relocation).** Since `sigma` is a `Z/2` that IS nonzero yet is
NOT the fermionic mod-2 index, its cobordism receptacle is **not** the Spin-bordism
the banked leg computed (`Omega^spin_{13,14,15} = 0`, all dead) but the
**reflection / Pin (unoriented-with-`T`) bordism group** -- a genuinely DIFFERENT,
UNCOMPUTED receptacle, generically nonzero in low dimensions (`Omega^{pin+}`,
`Omega^{pin-}` carry `Z/2`, `Z/8`, `Z/16` where the Spin side is zero). `sigma`'s
cardinality = the torsion of that group for GU's structure. Base gives one `Z/2`
(D2); the second bit is the Pin+/Pin- split.

**MODE: MIXED (with a REFUTATION inside).** EXACT: the APS/`eta`/self-adjoint-
extension substrate; and the Kramers kill of the mod-2 index (`sigma != mod-2 eta`).
PROPOSAL: `sigma` = a specified nonzero class in a named reflection-bordism group.
**NEW: YES** -- relocates `sigma` from the computed-zero Spin receptacle to the
uncomputed reflection/Pin receptacle, and gives the cardinality as that group's torsion.

---

## SYNTHESIS

### Verdict: MIXED -- exact inflow SUBSTRATE, graded-PROPOSAL 't Hooft anomaly, in the w1/reflection family

The three lenses converge. **It is not merely an analogy:** the substrate --
domain-wall Dirac symbol crossing zero at `{q=0}`, self-adjoint-extension
obstruction = APS boundary condition = bulk SPT, deck-ODD action = the symmetry
realized with no invariant completion -- is *the* mathematical structure that
anomaly inflow is made of, and the pieces are banked/probe-checked (EXACT). **But it
is not yet an EXACT theorem that GU has a 't Hooft anomaly:** "a computed nonzero
anomaly coefficient of a specified symmetry" needs the boundary determinant-line /
partition-function variation built, and that is exactly as solid as the operator-
grade deck action `U N U^{-1} = -N`, which is still an un-banked model (wave-swing-1
tagged it ANALOGY). So the honest grade is **genuine anomaly-inflow STRUCTURE
(EXACT), genuine 't Hooft anomaly (PROPOSAL)**.

**Which anomaly -- decisively.** It is the **`w1` (orientation / time-reversal /
reflection) `Z/2` anomaly**, NOT the fermionic mod-2 Dirac-index / mod-2-eta anomaly.
The latter is banked-DEAD by quaternionic Kramers evenness and is corroborated dead
here from the determinant angle (`det c = q^64`, even). This disambiguation is the
swing's sharpest EXACT contribution: it uses a banked no-go to KILL the natural
index-theory reading and forces `sigma` into the reflection/`T` family, where the
`+-i0` = time-orientation identification is tight.

### Does it constrain sigma's cardinality (the N2 question)? SHARPENS, does not CLOSE

The single most valuable thing the machinery BUYS: **it names the correct cobordism
receptacle for `sigma` -- the reflection / Pin (unoriented-with-`T`) bordism group --
which is DISTINCT from the Spin-side receptacle the banked global-anomaly-leg
computed (all zeros, dims 13-16) and is precisely the S6 SM-boundary/inflow leg that
work EXCLUDED and left OPEN.** This converts the open N2 cardinality question
(`Z/2` vs `Z/2 x Z/2`) from a guess into a **decidable bordism computation** with a
**named candidate second bit `tau` = the reflection-square / Pin+ -vs- Pin- (`T^2 =
+-1`) sign**. Concretely:

- **EXACT sub-result (probe D2):** the base `RP^3` supplies exactly ONE degree-1
  `Z/2` -- `H^1(RP^3;Z/2) = Z/2`, whose generator is `sigma = w1(L_time)` (note
  `RP^3` is orientable, `w1(T RP^3)=0`, so `sigma` is the tautological *line*'s `w1`,
  not the tangent's). A second independent `Z/2` **cannot** be base-degree-1-
  topological. So if the answer is `Z/2 x Z/2`, the second factor is forced to be a
  non-base-degree-1 datum -- the Pin-flavor / reflection-square is the natural, and
  arguably only clean, candidate.
- **What is still OPEN:** the actual value (one generator or two) = the torsion of
  GU's reflection/Pin bordism receptacle in the right dimension, uncomputed. The
  banked work computed only the Spin side. So the N2 question is now WELL-POSED with
  a named second generator, not closed.

Net: **the machinery sharpens N2 (names the receptacle and the candidate `tau`) but
does not decide it.** That is the honest deliverable, and it is strictly more than
"open guess": `tau` is no longer nameless.

### The single most valuable thing unlocked (one line)

**A specific, decidable computation:** the reflection/Pin bordism group that is
`sigma`'s true receptacle -- the S6 inflow leg the Spin-side closure explicitly
skipped. Its torsion decides `Z/2` vs `Z/2 x Z/2`; the Spin-side zeros do NOT bound
it (different structure group), so the banked triviality result says *nothing* about
`sigma`, and that non-implication is itself worth banking.

### Independent consequences (flagged; all PROPOSAL)

1. **Anomaly matching => RG-protected externality.** If `sigma` is a genuine anomaly
   it is an RG invariant: external at ALL scales, unremovable by any internal
   dynamics. This upgrades `DYN-NO-REOPEN` (internal supply refuted at one scale) to
   "internal supply is structurally FORBIDDEN at every scale." (PROPOSAL; needs the
   anomaly established, not just its shape.)
2. **Anomaly-protected gapless edge => excision FORBIDDEN, not merely unowned.**
   This is the sharpest independent bite. Prong-0 / LP-LC leave the `LP-FORCED`
   escape open in principle -- it "only" needs an *unowned* excision of the `{q<0}`
   stratum. A nonzero reflection anomaly would make that edge **anomaly-protected
   gapless**: excising it is not unowned, it is **impossible** (the anomaly must be
   matched somewhere). If the anomaly is established, `LP-FORCED` is not just
   un-purchased, it is ruled out -- a strict strengthening of Prong-0's confirmation.
   (PROPOSAL; the conditional is exactly "is the reflection anomaly nonzero.")
3. **The two-sided ultrahyperbolic BVP is the (d+1) inflow bulk.** wave-swing-3's
   two-sided BVP / two-time scaffold is, in this language, the anomaly-inflow bulk
   whose SPT term completes the edge -- one seam, two names. (ANALOGY, coherent.)

### The strongest ANALOGY-only counter (steelman, why the verdict is MIXED not EXACT)

A self-adjoint-extension ambiguity is generically NOT an anomaly -- it is a choice
of boundary condition, a `theta`-like modulus. It becomes an anomaly ONLY via the
"no symmetric completion" fact, which rests entirely on the deck-ODD operator action
`U N U^{-1} = -N(t+1)`. That action is, at present, an operator-side MODEL (checked
in a toy, tagged ANALOGY in wave-swing-1), not a banked operator-grade theorem. So
the anomaly reading is exactly as solid as that deck action -- no more. This is why
the verdict cannot be EXACT: the one fact that promotes "boundary-condition modulus"
to "'t Hooft anomaly" is itself un-banked. The reflection-family identification and
the mod-2-index REFUTATION are firmer (EXACT); the anomaly promotion is the
PROPOSAL, and its single decisive reopener is banking the operator-grade deck action.

## Honest ledger

- **EXACT (banked / machine-corroborated):** the APS / spectral-flow /
  self-adjoint-extension <-> SPT substrate; `sigma` is NOT the mod-2 Dirac-index /
  mod-2-eta anomaly (quaternionic Kramers evenness; `det c = q^64`, mod-2 spectral
  flow across `{q=0}` EVEN, probe D1); `H^1(RP^3;Z/2) = Z/2` so the base orientation
  datum is a single `Z/2` = `sigma = w1(L_time)` (probe D2); the Spin-side bordism
  zeros do NOT bound the reflection/Pin receptacle (different structure group).
- **PROPOSAL (a "predicts", pending verification):** GU carries a genuine nonzero
  't Hooft anomaly (needs the boundary determinant-line variation + the operator-grade
  deck action); `sigma`'s receptacle is a specific reflection/Pin bordism group whose
  torsion decides `Z/2` vs `Z/2 x Z/2`; candidate second bit `tau` = the reflection-
  square / Pin+ -vs- Pin- sign; anomaly-matching => RG-protected externality; the
  `{q=0}` edge is anomaly-protected-gapless => excision forbidden (strengthens Prong-0).
- **REFUTED / does not survive:** `sigma` = the mod-2 Dirac index / mod-2-eta / sign
  of the Pfaffian line (dead by Kramers evenness, two independent routes); "the bulk
  Dai-Freed anomaly is the relevant one" (it is trivial and it is the wrong -- Spin --
  receptacle; the live leg is the excluded S6 inflow leg).
- **Falls (do not ship):** "GU's obstruction IS a 't Hooft anomaly" stated flat
  (it is a graded PROPOSAL); "the machinery pins `sigma`'s cardinality" (it names the
  receptacle and the candidate `tau`; it does not compute the group).

## Boundary

Exploration tier. Only two NEW files were written -- this document and the probe
`tests/channel-swings/anomaly_inflow_swing_probe.py` (foreground, seed 20260721,
numpy + exact-int, EXIT 0, double-run byte-identical, 11/11 PASS; D1 corroborates
the mod-2-index kill from the determinant angle with an odd-multiplicity positive
control, D2 pins the base cardinality). GU otherwise read-only. No commit, no push.
No edit to LANE-STATE, research-portfolio, NEXT-STEPS, the LP-LC receipt, Prong-0,
wave-swing-1/3, the global-anomaly-leg pair, the sector-relative theory, or any
other agent's artifact, or any claim/canon/verdict/ledger file. No claim-status,
canon-verdict, paper-status, or public-posture change; the externality of
`sigma`/`tau`/`theta` and the verdicts `LC-SELECTOR`, `P0-FAILS-OBSTRUCTED`,
CLOSED-trivial (Spin bulk) are consumed, not moved. The swing's contribution: the
`{q<0}` obstruction is genuine anomaly-inflow STRUCTURE (EXACT) but a graded-PROPOSAL
't Hooft anomaly, of the `w1`/reflection type (NOT the mod-2 index, banked-dead); the
machinery's value is naming `sigma`'s true receptacle -- the uncomputed reflection/Pin
bordism (the excluded S6 leg) -- which makes the N2 cardinality question decidable
with a named candidate second bit `tau` = the reflection-square sign, and which yields
two PROPOSAL-grade independent consequences (RG-protected externality; anomaly-
forbidden excision of the `{q=0}` wall).
