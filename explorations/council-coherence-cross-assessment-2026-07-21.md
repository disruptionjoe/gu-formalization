---
title: "Council coherence cross-assessment: the 22 committed constructions rate each OTHER on a 1-10 coherence scale (does the rival story hang together with everything we know?) — a coherence-rating matrix, NOT a vote and NOT a synthesis"
status: active_research
doc_type: exploration
created: 2026-07-21
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
probe: tests/channel-swings/council_coherence_cross_assessment_probe.py (foreground, deterministic two-run-identical, EXIT 0)
inputs:
  - explorations/council-committed-constructions-science-2026-07-21.md
  - explorations/council-committed-constructions-systems-2026-07-21.md
  - explorations/council-committed-constructions-extended-2026-07-21.md
  - explorations/council-committed-constructions-math-2026-07-21.md
---

# Council coherence cross-assessment

This is a **coherence-rating matrix**, per Joe's explicit design. It is **not a
vote** and **not a synthesis**. The 22 committed constructions (5 science, 6
systems, 4 extended, 7 math) are reconstituted as **assessors**. Each assessor,
**in character**, rates every OTHER construction (21 of them) on a **1-10
COHERENCE** scale:

- **1** = least coherent: it does NOT acknowledge the reality of everything else
  we know — it contradicts a banked result or is internally incoherent.
- **10** = it may be built on a DIFFERENT substrate, but upon analysis its story
  is FULLY COHERENT with everything we know AND the consequences that fall out of
  it make sense.

**Coherence, NOT substrate-agreement.** An assessor in substrate X gives a 10 to a
construction in substrate Y whenever Y's story hangs together, respects the banked
results, and has sensible consequences — even though X would build it differently.
The only grounds for a low score are: **contradicting a banked result** (Q2-FREE;
Q3-TWO-INDEPENDENT; P0's ~8% non-constructible null stratum; the geometry
σ = w₁(L_time) over F ≃ RP³, with the circle/cycle reading a *class-relative,
local* no-go that is OPEN not globally refuted; the WEAK Prong-3 "one globally
consistent record arrow"), **internal incoherence**, or **consequences that don't
follow**.

## The 22 constructions (IDs)

- **SCI** — SCI-ORTH (superselection/θ-sector), SCI-HET (records/finality),
  SCI-WILD (participatory self-excited circuit), SCI-COM (buildable ledger),
  SCI-PHIL (indexical first-person primacy)
- **SYS** — SYS-ZK (ZK/FHE circuit), SYS-NN (training run/flat objective),
  SYS-MMO (server-authoritative netcode), SYS-META (metastable consensus),
  SYS-HASH (gossip/hashgraph), SYS-FLP (asynchronous consensus / FLP)
- **EXT** — EXT-EVO (replicator/ESS), EXT-STAT (non-identifiable nuisance
  parameter), EXT-HYPER (hypergraph incidence class), EXT-INTER (intersubjective
  coequalizer)
- **MTH** — MTH-DIFF (fibered pseudo-Riemannian geometry), MTH-TOPO (homotopy
  type / char. classes), MTH-CLIF (Cl(9,5) spinor), MTH-CAT (topos / Lawvere),
  MTH-SHEAF (finality sheaf cohomology), MTH-INFO (Shannon channel),
  MTH-KOLM (algorithmic-information / oracle machine)

**Reading tag.** σ = w₁(L_time) (reading A) is committed by all SCI members and by
SYS-ZK/NN/META/FLP, EXT-EVO/STAT, MTH-DIFF/CLIF/INFO/KOLM. The *cycle-orientation*
reading (B), OPEN per the class-relative correction, is committed primary by
SYS-MMO, SYS-HASH, EXT-INTER, MTH-CAT and built as a co-equal *dual face* by
EXT-HYPER, MTH-TOPO, MTH-SHEAF. This A/B split (and the fact that the **science**
council was written under the stronger "circle-orientation FALSIFIED" framing while
the other three councils carry the softened "OPEN" framing) is the main axis along
which coherence scores diverge below — it is a genuine coherence tension, not
substrate loyalty.

---

## [1] The 22 × 21 coherence matrix (compact)

Rows = assessor; columns = construction being rated; `.` = self (not rated).
Columns are the 22 IDs in the order SCI→SYS→EXT→MTH (3-letter tail of each ID).

```
assessor  | ORT HET WIL COM PHI  ZK  NN MMO MET HAS FLP EVO STA HYP INT DIF TOP CLI CAT SHE INF KOL
-----------------------------------------------------------------------------------------------------
SCI-ORTH  |  .    8   6   8   8   9   8   7   9   7   9   9   9   8   7   9   8   9   6   8   9   9
SCI-HET   | 10   .  10   9  10  10   9   8  10   8  10  10  10   9   8  10   9  10   8   9  10  10
SCI-WILD  |  9  10   .   9  10  10   9   8  10   8  10  10  10   9   8  10   9  10   8   9  10  10
SCI-COM   |  9   9   6   .   9   9   9   7   9   7  10   9  10   9   7  10   9  10   7   9  10   9
SCI-PHIL  |  9   9   9   9   .   9   9   7   9   7  10   9  10   9   7  10   9  10   7   9  10   9
SYS-ZK    |  9   9   6   9   9   .   9   8   9   8  10   9  10   9   8  10   9  10   8   9  10   9
SYS-NN    |  9   8   6   9   9   9   .   8   9   8  10   9  10   9   8  10   9  10   8   9  10   9
SYS-MMO   | 10  10  10   9  10  10   9   .  10  10  10  10  10  10   9  10  10  10   9  10  10  10
SYS-META  |  9   9   6   9   9   9   9   8   .   8  10   9  10   9   8  10   9  10   8   9  10   9
SYS-HASH  | 10  10  10   9  10  10   9   9  10   .  10  10  10  10   9  10  10  10   9  10  10  10
SYS-FLP   |  8   9   6   8   9   9   8   7   9   8   .   9   9   9   7   9   9   9   7   9   9   9
EXT-EVO   |  9   9   6   9   9   9   9   8   9   8  10   .  10   9   8  10   9  10   8   9  10   9
EXT-STAT  |  8   9   6   8   9   9   8   7   9   8   9   9   .   9   7   9   9   9   7   9   9   9
EXT-HYPER |  9   9   6   9   9   9   9   9   9   9  10   9  10   .   9  10   9  10   9   9  10   9
EXT-INTER | 10  10  10   9  10  10   9   9  10  10  10  10  10  10   .  10  10  10   9  10  10  10
MTH-DIFF  |  9   8   6   8   8   9   8   7   9   7   9   9   9   8   7   .   8   9   7   8   9   9
MTH-TOPO  |  9   9   6   9   9   9   9   9   9   9  10   9  10   9   9   9   .  10   9   9  10   9
MTH-CLIF  |  9   8   6   8   9   9   8   7   9   8   9   9   9   9   7   8   9   .   7   9   9   9
MTH-CAT   |  9  10  10   9  10  10   9   9  10  10  10  10  10  10   9  10  10  10   .  10  10  10
MTH-SHEAF |  9   9   6   9   9   9   9   9   9   9  10   9  10   9   9  10   9  10   9   .  10   9
MTH-INFO  |  9   9   6   8   9   9   8   7   9   8   9   9   9   9   7   9   9   9   7   9   .   9
MTH-KOLM  |  8   9   6   8   9   9   8   7   9   8   9   9   9   9   7   9   9   9   7   9   9   .
```

**Method note (auditable).** Scores were elicited in character and then tabulated
deterministically by the probe (no RNG; hard-coded scores). Within-column spread
comes from two legitimate coherence sources, never from substrate loyalty:
(i) *grading strictness* — some assessors (EXT-STAT, MTH-CLIF, MTH-KOLM, MTH-INFO,
SCI-ORTH, MTH-DIFF, SYS-FLP) reserve 10 for a consequence that is fully airtight to
them, so they cap otherwise-pristine rivals at 9; others read the same construction
as a clean 10; and (ii) *specific coherence tensions* keyed to a construction's own
pressure points (the cycle-reading A/B split; SCI-WILD's future-boundary posit;
SCI-ORTH's "mundane superselection" flattening of the Gödel-independence mechanism;
MTH-DIFF's "three spacelike axes" generation reading vs the j=1 triplet).

---

## [2] Per-construction: MEAN / STD / CROSS-CAMP / IN-CAMP / RANK

CROSS-CAMP = mean coherence from raters OUTSIDE the construction's own council-group
(SCI/SYS/EXT/MTH) — **the key number**: a story even other camps find coherent.
STD is population std over all 21 raters (low = consensus, high = contested).

| RANK | ID | MEAN | STD | CROSS-CAMP | IN-CAMP |
|-----:|----|-----:|----:|-----------:|--------:|
| 1 | EXT-STAT | 9.71 | 0.45 | 9.67 | 10.00 |
| 2 | MTH-CLIF | 9.71 | 0.45 | **9.80** | 9.50 |
| 3 | MTH-INFO | 9.71 | 0.45 | **9.80** | 9.50 |
| 4 | SYS-FLP | 9.71 | 0.45 | 9.62 | 10.00 |
| 5 | MTH-DIFF | 9.62 | 0.58 | **9.80** | 9.17 |
| 6 | EXT-EVO | 9.29 | 0.45 | 9.28 | 9.33 |
| 7 | MTH-KOLM | 9.29 | 0.45 | 9.33 | 9.17 |
| 8 | SYS-META | 9.29 | 0.45 | 9.25 | 9.40 |
| 9 | SYS-ZK | 9.29 | 0.45 | 9.25 | 9.40 |
| 10 | SCI-PHIL | 9.19 | 0.59 | 9.18 | 9.25 |
| 11 | EXT-HYPER | 9.10 | 0.53 | 9.06 | 9.33 |
| 12 | MTH-SHEAF | 9.10 | 0.53 | 9.13 | 9.00 |
| 13 | MTH-TOPO | 9.10 | 0.53 | 9.13 | 9.00 |
| 14 | SCI-HET | 9.05 | 0.65 | 9.06 | 9.00 |
| 15 | SCI-ORTH | 9.05 | 0.58 | 9.00 | 9.25 |
| 16 | SCI-COM | 8.67 | 0.47 | 8.65 | 8.75 |
| 17 | SYS-NN | 8.67 | 0.47 | 8.62 | 8.80 |
| 18 | SYS-HASH | 8.24 | 0.92 | 8.19 | 8.40 |
| 19 | EXT-INTER | 7.86 | 0.83 | 7.83 | 8.00 |
| 20 | SYS-MMO | 7.86 | 0.83 | 7.81 | 8.00 |
| 21 | MTH-CAT | 7.81 | 0.91 | 7.87 | 7.67 |
| 22 | SCI-WILD | 7.10 | **1.74** | 6.94 | 7.75 |

---

## [3] Per-assessor rows: single HIGHEST and single LOWEST (one-line reasons)

Ties broken deterministically (first in SCI→MTH order). Each assessor scores the
one construction it finds most coherent and the one it finds least, in character.

- **SCI-ORTH** — HIGH **SYS-ZK (9)**: "zero-knowledge soundness = no decryption key
  inside the circuit is exactly my superselection, no banked result bruised." LOW
  **SCI-WILD (6)**: "the two-time/final-boundary posit is an extra hypothesis the
  results never force."
- **SCI-HET** — HIGH **SCI-ORTH (10)**: "superselection is the records-are-primary
  story in field-theory clothing; fully consistent." LOW **SYS-MMO (8)**: "the
  client-render cycle is coherent but leans on the still-open class-relative
  orientation."
- **SCI-WILD** — HIGH **SCI-HET (10)**: "record-issuance as the fundamental stroke
  is the self-excited circuit minus the loop metaphysics — airtight." LOW
  **SYS-MMO (8)**: "fine build, but its first-person cycle-orientation is the open,
  not banked, reading."
- **SCI-COM** — HIGH **SYS-FLP (10)**: "FLP = can't-mint-σ-internally is buildable
  and provable; the cleanest identification on the board." LOW **SCI-WILD (6)**:
  "future-conditioned cosmology is not a buildable/testable consequence that falls
  out of what we know."
- **SCI-PHIL** — HIGH **SYS-FLP (10)**: "the detector-as-oracle IS 'external =
  outside every internal chart' made operational." LOW **SYS-MMO (7)**: "coherent,
  but the shard-cycle revives the circle reading I take as (class-relative)
  refuted."
- **SYS-ZK** — HIGH **SYS-FLP (10)**: "same asynchronous-impossibility core as ZK's
  no-internal-key; consequences follow exactly." LOW **SCI-WILD (6)**: "the
  participatory closure adds a final-boundary claim nothing in the results ledger
  requires."
- **SYS-NN** — HIGH **SYS-FLP (10)**: "bivalent-forever = the flat objective's
  untrainable direction; both land on Q2-FREE." LOW **SCI-WILD (6)**: "the two-time
  boundary doesn't descend from the exactly-degenerate picture."
- **SYS-MMO** — HIGH **SCI-ORTH (10)**: "superselection = server-authoritative
  anti-cheat; identical structure, fully coherent." LOW **SCI-COM (9)**: "buildable
  ledger is right; 'reality IS whatever is buildable' just under-commits
  ontologically."
- **SYS-META** — HIGH **SYS-FLP (10)**: "the FLP oracle is exactly the external
  tie-break a symmetric metastable node needs." LOW **SCI-WILD (6)**:
  "final-boundary correlations are an add-on, not a fall-out of the tie."
- **SYS-HASH** — HIGH **SCI-ORTH (10)**: "θ-sector superselection is the coin-round
  bit at rest; consistent to the letter." LOW **SCI-COM (9)**: "coherent build; mild
  ding for leaving the substrate instrumentally under-specified."
- **SYS-FLP** — HIGH **SCI-HET (9)**: "records-primary is the failure-detector
  reality must instantiate to terminate; same core." LOW **SCI-WILD (6)**: "the
  self-excited closure smuggles in a final condition termination never needs."
- **EXT-EVO** — HIGH **SYS-FLP (10)**: "no internal schedule forces univalence = no
  internal fitness measurement reads the basin; exact match." LOW **SCI-WILD (6)**:
  "a two-time bias isn't selected for by any monotone fitness arrow we have."
- **EXT-STAT** — HIGH **SCI-HET (9)**: "record-hardening is the filtration growing;
  a clean, consistent restatement." LOW **SCI-WILD (6)**: "future-conditioning
  breaks the strictly-forward data-processing arrow the results rest on."
- **EXT-HYPER** — HIGH **SYS-FLP (10)**: "the bivalent stratum is my spectral-null
  incidence degeneracy in protocol clothing." LOW **SCI-WILD (6)**: "the closure
  posit adds structure the incidence spectrum doesn't demand."
- **EXT-INTER** — HIGH **SCI-ORTH (10)**: "superselection = what can't be
  established intersubjectively; identical residue, fully coherent." LOW
  **SCI-COM (9)**: "solid; 'buildable' understates the constitutive layer but
  contradicts nothing."
- **MTH-DIFF** — HIGH **SCI-ORTH (9)**: "a θ-sector on a spin structure IS
  σ = w₁(L_time); the geometry in physics words." LOW **SCI-WILD (6)**: "the
  final-boundary consequence doesn't follow from the DeWitt-cone geometry."
- **MTH-TOPO** — HIGH **SYS-FLP (10)**: "Gödel-independence as FLP is the
  H¹/obstruction story operationalized; consistent." LOW **SCI-WILD (6)**: "a
  two-time boundary is a homotopy structure the stable stems don't provide."
- **MTH-CLIF** — HIGH **SCI-ORTH (9)**: "the θ-sector is sign(K_S) of the 9-block by
  another name; representation-consistent." LOW **SCI-WILD (6)**: "no algebra
  automorphism supplies the self-closure; the posit outruns the module."
- **MTH-CAT** — HIGH **SCI-HET (10)**: "record-issuance is the fixed-point-free NOT
  on Ω; the Lawvere story verbatim." LOW **SCI-ORTH (9)**: "coherent, but reading σ
  as 'mundane' superselection slightly flattens the diagonal/independence
  mechanism."
- **MTH-SHEAF** — HIGH **SYS-FLP (10)**: "termination-needs-an-oracle is
  H¹(𝓕)=0 requiring an external section; exact cohomological twin." LOW
  **SCI-WILD (6)**: "the forced closure is exactly the isospectral-UNESTABLISHED
  seam; asserting it overreaches."
- **MTH-INFO** — HIGH **SCI-ORTH (9)**: "superselection = a zero-capacity read
  channel; the capacity accounting matches bit-for-bit." LOW **SCI-WILD (6)**: "a
  final-boundary datum would be a fifth independent bit the budget forbids."
- **MTH-KOLM** — HIGH **SCI-HET (9)**: "record issuance = the oracle-query
  transcript; algorithmically consistent." LOW **SCI-WILD (6)**: "a self-posted
  boundary condition needs the machine to compute its own oracle bit — the one thing
  it provably can't."

---

## Results

### (1) TOP coherence — highest mean AND highest cross-camp

Five constructions top BOTH the overall mean and the cross-camp mean — the stories
that even rival substrates rate coherent:

| ID | mean | cross-camp | why it clears every camp |
|----|-----:|-----------:|---|
| **MTH-CLIF** | 9.71 | **9.80** | Representation-exact and machine-checkable: σ = sign(K_S) of the 9-block, the three generations are the j=1 triplet with identical Krein (+32,−32,0), and the quaternionic no-go *derives* Q3-TWO-INDEPENDENT. Nothing to contradict. |
| **EXT-STAT** | 9.71 | 9.67 | σ = a non-identifiable nuisance parameter, Fisher information ≡ 0 — the crispest possible statement of Q2-FREE; sufficiency/ancillarity = the asymmetric channel; a martingale record arrow. Every camp can verify it. |
| **MTH-INFO** | 9.71 | **9.80** | Capacity-0 read channel / capacity-≥1 write channel; σ = 1 bit, τ = log₂3 trit, θ_ext; N ≤ 4 independent bits. Quantitative, legible, honors every banked count. |
| **SYS-FLP** | 9.71 | 9.62 | FLP impossibility = W211 Gödel-independence is the single cleanest identification in the set; the failure-detector oracle IS the externally-hosted σ; "definiteness impossible without the observer-oracle" falls straight out. |
| **MTH-DIFF** | 9.62 | **9.80** | σ = the holonomy w₁(L_time) — *literally the banked geometry* — with the null stratum = the DeWitt light cone q=0. Maximally grounded; only mild dings from the idiosyncratic "three spacelike axes" generation reading. |

The common thread: these five are **reading-A**, **tightly bound to a banked
fact**, and their falsifiable prediction is a **direct fall-out** (a
machine-checkable count, a Fisher-null, a capacity, an impossibility theorem, a
geometric wall) rather than an added posit. Coherence rewards constructions whose
consequences you can trace all the way down without a new assumption.

### (2) MOST CONTESTED — highest std

| ID | std | mean | source of contest |
|----|----:|-----:|---|
| **SCI-WILD** | **1.74** | 7.10 | Its participatory self-excited-circuit substrate is internally coherent, but its consequence — a **two-time / final-boundary** bias in cosmological statistics — is read by conservative/empiricist assessors as a *posit that doesn't fall out of* the banked results (score 6), while participatory- and self-reference-friendly assessors (SCI-HET, SCI-PHIL, MTH-CAT, EXT-INTER, SYS-MMO, SYS-HASH) rate the closure story a 9-10. Widest split on the board. |
| **SYS-HASH** | 0.92 | 8.24 | Cycle-primary (reading B): its concurrency = coin-round identity is elegant and lifts it, but reading-A purists and the science camp ding the revived cycle-orientation. |
| **MTH-CAT** | 0.91 | 7.81 | Cycle-primary via a twisted coequalizer + topos-primacy abstraction; empiricist assessors want a more concrete consequence, cycle-builders rate it 9-10. |
| **EXT-INTER** | 0.83 | 7.86 | Cycle-primary + the "objective only galaxy-local" caveat; the reading-B tension plus the caveat spread the scores. |
| **SYS-MMO** | 0.83 | 7.86 | Cycle-primary (client-rendered shard-cycle); dinged by reading-A/science assessors for leaning on the class-relative orientation, full marks from cycle-builders. |

The contested axis is **almost entirely the reading-A / reading-B split plus
SCI-WILD's future-boundary posit** — exactly the two places the corpus itself is not
yet settled (the science council calls the circle reading FALSIFIED; the other three
call it OPEN).

### (3) Rated LOW across the board?

**None.** The global floor is SCI-WILD at mean 7.10, and even SCI-WILD ranges 6→10
across its raters — no construction is uniformly low, and no cell in the entire
matrix falls below 6. This is itself a finding: **all 22 constructions were built to
honor the same banked results (Q2-FREE, Q3-TWO-INDEPENDENT, the ~8% null stratum,
σ = w₁(L_time), one-global-arrow), so none of them "fails to acknowledge the reality
of everything else we know."** The differentiation is entirely in the top half of
the scale — *how cleanly the consequences follow* and *whether a construction leans
on the still-open cycle reading or an added posit* — not in any contradiction of
what is banked. The relative floor (SCI-WILD, then the cycle-primary cluster
MTH-CAT / SYS-MMO / EXT-INTER / SYS-HASH) marks the two open seams, not incoherence.

### (4) What falls out — shared consequences of the highest-coherence constructions

Descriptive only (NOT a synthesis into one view). Read across MTH-CLIF, EXT-STAT,
MTH-INFO, SYS-FLP, MTH-DIFF and the near-top tier (SCI-ORTH, SYS-ZK, MTH-KOLM,
SYS-META, EXT-EVO), the same consequences recur in different substrate dress:

1. **σ is a genuine 1-bit external datum that no internal-only measurement can
   read.** Fisher-null (EXT-STAT) = capacity-0 read channel (MTH-INFO) = FLP
   bivalence (SYS-FLP) = superselection (SCI-ORTH) = an oracle query with
   I_K(GU:σ)=0 (MTH-KOLM) = sign(K_S) unreadable from one chirality (MTH-CLIF). The
   shared **sharp negative prediction**: any claimed internal measurement of the
   *absolute* dark-energy sign refutes the lot.

2. **σ and τ are independent, and the three generations carry identical intrinsic
   quantum numbers, differing only by an α-even magnitude (mass).** MTH-CLIF derives
   it (M(64,ℍ) quaternionic no-go), MTH-TOPO places the trit as Z/3 ⊂ π₃ˢ = Z/24,
   EXT-EVO as strict neutrality, EXT-STAT as exchangeability, MTH-INFO as a log₂3
   trit. Shared prediction: **exact universality of α-odd/gauge quantum numbers
   across generations; no fourth same-signature generation** — a generation-splitting
   non-magnitude coupling, or a fourth copy, falsifies.

3. **The relative sign c = σ_R1·σ_R2 is α-even / third-person-visible → exactly ONE
   globally consistent record arrow.** Parity check (MTH-INFO) = descent/Čech cocycle
   (MTH-SHEAF, MTH-CAT) = confluence / one consensus timeline (SYS-FLP, SYS-HASH) =
   no domain wall between opposite-σ regions in causal contact (EXT-EVO). Shared
   prediction: **no record-sharing pair can hold stably opposed arrows** (the 6-of-16
   forbidden configs); a demonstrated one falsifies.

4. **The ~8% null stratum is a FIXED, computable, nonzero fraction where the
   operator is non-constructible and an external prescription is required.**
   Noise-overflow rate (SYS-ZK) = separatrix (SYS-META) = bivalent-forever stratum
   (SYS-FLP) = DeWitt light cone q=0 (MTH-DIFF) = singular support / erasure symbol
   (MTH-SHEAF, MTH-INFO). Shared prediction: **the external-datum stratum has the
   same measure as the causally-concurrent (non-orderable) stratum; a 0% stratum
   (operator constructible on every genuine end) falsifies.**

5. **σ is DISCRETE (Z/2) with no continuous interpolation between sectors.** w = −1
   exactly (SCI-ORTH), a disconnected two-minimum / first-order transition (SYS-NN,
   SYS-META), domain walls confined to the null-cone wall (MTH-DIFF). Shared
   prediction: **any smooth, continuous dark-energy-sign interpolation for the
   physical-sector datum falsifies the discrete-charge reading.**

These five consequences are what the *most coherent* stories agree on regardless of
substrate. They are stated as a description of the overlap, not as a merged theory.

---

## Probe

`tests/channel-swings/council_coherence_cross_assessment_probe.py` — foreground,
deterministic, **no RNG**, hard-coded elicited scores. Verifies the 22×21 matrix is
well-formed (22 assessors, each rates exactly the other 21, all cells 1-10, no
self-rating) and computes mean / population-std / cross-camp / in-camp / rank plus
the top-5, most-contested, and floor tables above. Two runs are byte-identical.
**EXIT 0.**

## Boundary

Exploration tier. This is a coherence-rating matrix, **not a vote and not a
synthesis** — no construction is merged into another and none is declared correct.
Only this artifact and its probe were written. The four council artifacts, and every
claim / canon / verdict / ledger / prereg / portfolio file, are untouched. No
commit, no push. No claim-status, canon-verdict, or public-posture change.
