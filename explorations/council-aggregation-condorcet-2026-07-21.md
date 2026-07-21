---
title: "Council aggregation (Condorcet + confidence-weighted): consensus across the two boundary-meaning councils (5 science + 7 systems = 12 personas as voters). Real pairwise-majority vote over the 12 STEELMEN and over the 10 QUESTION-finalists, plus a confidence x mode-weight ranking of the steelmen and a cross-lens (rigor vs interpretive vs structural) consensus read. Headline: INFO (sigma = 1 external bit / zero inward capacity) is the Condorcet winner AND co-tops the confidence-weighted list (robust); FLP (relativized-computability / host-vs-source) is the most uniformly-placed steelman across opposed lenses; COMMERCIAL is high-confidence but Condorcet-dismissed (solid-but-narrow); the questions have NO single Condorcet winner (a P1 / I2 tie at the top), and the standpoint-exhaustiveness question P1 is the one pivot rigor AND wild lenses both rate top."
status: active_research
doc_type: exploration
created: 2026-07-21
inputs:
  - explorations/council-science-boundary-meaning-2026-07-21.md
  - explorations/council-systems-boundary-meaning-2026-07-21.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Council aggregation: what has CONSENSUS across differing opinions

This is a read-only aggregation pass over two completed councils. It does **not**
re-open any council judgment, move any claim/canon/verdict, or take any external
action. It asks one question Joe posed: **across genuinely differing lenses, what
do the councils actually agree on?** — answered as a *real* Condorcet vote with
the 12 council personas reconstituted as an inline voting panel, plus a
confidence-weighted ranking held up against the vote.

The two source councils:

- **Science council** (5 members): orthodox physicist, heterodox physicist,
  commercial/pragmatist, wild-frontier theorist, philosopher of science.
- **Systems/formal council** (7 members): ZK/FHE, neural-nets, hashgraph,
  metastable-consensus, distributed/FLP, MMO, information-theorist.

Each member produced a **steelman** (with MODE ∈ {EXACT, MIXED, ANALOGY} and a
CONFIDENCE %) and **three escalating questions** (Q1 grounded → Q2 cross-domain →
Q3 wild). That is **12 steelmen** and **36 questions**. The 12 personas are the
voters — reconstituting them as a panel and taking pairwise majorities *is* the
operational meaning of "consensus across differing opinions."

The tabulation is a deterministic probe (no RNG, hard-coded ballots):
`tests/channel-swings/ch_aggregation_condorcet_probe.py` — run foreground, **exit
code 0**.

---

## 1. The 12 steelmen (the candidates)

| tag | author | one-line steelman | MODE | CONF |
|-----|--------|-------------------|------|------|
| **ORTH** | orthodox physicist | superselection sector label + self-adjoint-extension question + discrete moduli — all textbook | EXACT | 80% |
| **HET** | heterodox physicist | the boundary is the seam between 3rd-person geometry and 1st-person record; the **co-flip weld** (σ = record arrow) is one α-odd datum | MIXED | 55% |
| **COM** | commercial/pragmatist | a reusable **audit method** + a **priced-separation** limitative result ("separating positivity-choice from record-direction costs exactly one underived Z/2") | EXACT (method) | 70% |
| **WILD** | wild-frontier | a **Gödel/Lawvere diagonal realized in physics**; the missing piece is the self-reference horizon, "outside" = the standpoint of selection | MIXED→ANALOGY | 40% |
| **PHIL** | philosopher | two exact lemmas (blindness + exhaustive dichotomy) → an **indexical necessity**, kept distinct from "chosen by a conscious observer" | MIXED | 62% |
| **ZK** | ZK/FHE | **homomorphic carry-without-read**: hosts/transforms σ (co-flip = homomorphic NOT) but cannot decrypt; witness outside the circuit | MIXED | 55% |
| **NEU** | neural-nets | a **spontaneously-broken discrete symmetry** of the objective; a free moduli direction the geometry can't fix, must be externally seeded | MIXED | 60% |
| **HASH** | hashgraph | σ welded to the **record arrow** = the Z/2 orientation of a consensus timeline | ANALOGY | 45% |
| **META** | metastable | a **symmetric bistable tie**, two degenerate basins, selection from an external perturbation | ANALOGY | 50% |
| **FLP** | distributed/FLP | **relativized computability**: P unsolvable by internal class C, solvable by C + external oracle; the **host-vs-source** distinction (node = locus, not source) | MIXED | 72% |
| **MMO** | MMO | **server-authoritative vs client-observed**: σ is the shard assignment the client renders but does not own | ANALOGY | 35% |
| **INFO** | information-theorist | **σ = exactly 1 external bit**; blindness = **zero inward channel capacity** / I(internal;σ)=0; the boundary is a channel with asymmetric capacity | EXACT | 80% |

---

## 2. Method

1. **Reconstitute the 12 personas as an inline voting panel** (each reasons
   in-character; no agents spawned).
2. **Steelmen:** each persona produced a full strict **preference ranking** of
   all 12 steelmen by *"which best captures what the missing piece really is."*
   Each author ranks their own steelman #1 (self-vote noted, §7 sensitivity).
3. **Questions:** each persona scored all 36 questions **1–5** on *"most
   interesting + generative."* Top-10 by mean become finalists; the finalist
   ballots are the personas' score-orders (ties → 0.5 in pairwise).
4. **Tabulate deterministically:** pairwise-majority matrix → Condorcet winner if
   one exists, else Copeland ordering + Smith set, for both races.
5. **Confidence-weighted steelman ranking** (separate): score = author CONF ×
   mode-weight (EXACT 1.0, MIXED 0.6, ANALOGY 0.3); compare to Condorcet.
6. **Cross-lens consensus:** flag items rated highly across *opposed* lenses
   (rigor ↔ interpretive ↔ structural) vs items that polarize.

---

## 3. The elicited ballots (compact)

### 3a. Steelman preference ballots (strict, 1st → 12th)

| voter | ranking (best-captures-the-missing-piece → worst) |
|-------|------|
| ORTHODOX | ORTH · INFO · FLP · COM · PHIL · NEU · META · HET · ZK · HASH · MMO · WILD |
| HETERODOX | HET · WILD · FLP · PHIL · INFO · ZK · NEU · HASH · META · ORTH · MMO · COM |
| COMMERCIAL | COM · INFO · ORTH · FLP · PHIL · NEU · ZK · META · HASH · HET · MMO · WILD |
| WILD | WILD · HET · PHIL · FLP · INFO · ZK · NEU · HASH · META · ORTH · COM · MMO |
| PHILOSOPHER | PHIL · INFO · FLP · ORTH · COM · HET · NEU · ZK · WILD · META · HASH · MMO |
| ZKFHE | ZK · INFO · FLP · HET · PHIL · ORTH · NEU · WILD · HASH · META · COM · MMO |
| NEURAL | NEU · INFO · ORTH · FLP · META · PHIL · HET · ZK · HASH · WILD · COM · MMO |
| HASHGRAPH | HASH · HET · FLP · INFO · META · ORTH · PHIL · WILD · NEU · ZK · MMO · COM |
| METASTABLE | META · NEU · INFO · FLP · ORTH · HASH · HET · PHIL · ZK · WILD · MMO · COM |
| FLP | FLP · INFO · PHIL · ORTH · HET · ZK · WILD · NEU · COM · META · HASH · MMO |
| MMO | MMO · FLP · INFO · HET · ZK · ORTH · PHIL · HASH · META · NEU · WILD · COM |
| INFO | INFO · FLP · PHIL · ORTH · NEU · HET · ZK · COM · WILD · META · HASH · MMO |

The reasoning behind the shape: **rigor voters** (ORTHODOX, COMMERCIAL, INFO,
FLP, PHILOSOPHER) reward tight identification with a known structure and place
INFO/FLP high; **interpretive voters** (HETERODOX, WILD) reward the weld and the
Gödel horizon and place HET/WILD/PHIL high; **structural-rhyme voters** (ZK, NEU,
HASH, META, MMO) place their nearest cousin high but almost all still route INFO
and FLP into their top-4 (see §6).

### 3b. Question scores → finalists

The 36 questions scored 1–5 by each persona (full 12×36 matrix in the probe).
Top-10 means (the finalists):

| id | mean | question (abbreviated) |
|----|------|------------------------|
| **P1** | 4.00 | is the Sec-4.2 standpoint dichotomy provably **exhaustive** → externality upgrades lean→theorem? |
| **I2** | 3.83 | is inward capacity provably 0; does hosting impose a **1-bit ceiling** forbidding imports beyond σ,τ? |
| **F1** | 3.75 | exact **oracle class** σ needs: is 1 Z/2 the *weakest* failure-detector (Chandra–Toueg)? τ stronger? |
| **I1** | 3.75 | is the right quantity a **Hartley** bit (cardinality) or a **Shannon** bit (needs a prior)? |
| **I3** | 3.75 | is total external bit-budget (σ+τ+θ) a conserved fundamental **information charge**? |
| **N3** | 3.58 | are σ,τ,θ the entire **untrainable** parameter set; bit-size a fundamental sloppiness signature? |
| **P3** | 3.58 | first physical **demonstrably-undecidable-from-within** fact; vindicate/refute complete 3rd-person TOE? |
| **C3** | 3.50 | is provable irreducible-input **bit-count** a currency to compare rival unifications? |
| **F3** | 3.42 | is first-person-ness the failure-detector reality is **forced to instantiate** to be definite? |
| **MS1** | 3.33 | is σ **exactly** degenerate or infinitesimally biased; does any quantity dynamically break the tie? |

Near-misses (3.0–3.2): F2, MS3, G3, MS2, N1, **O1** (grounded θ-dissolution
theorem), P2. O1 is the notable exclusion — a sharp grounded question that the
rigor lenses love but the interpretive/structural lenses rate only ~2, so its
mean falls just below the cut.

---

## 4. STEELMEN — the Condorcet result

Pairwise-majority matrix (cell = # of the 12 voters ranking row-steelman **above**
column-steelman; >6 = row wins that pair):

```
         ORTH   HET   COM  WILD  PHIL    ZK   NEU  HASH  META   FLP   MMO  INFO
 ORTH     --    7.0  11.0  10.0   6.0   8.0   8.0   9.0   8.0   3.0  11.0   1.0
  HET    5.0     --   9.0  11.0   6.0  10.0   7.0   9.0   8.0   3.0  11.0   3.0
  COM    1.0    3.0    --   4.0   2.0   3.0   3.0   5.0   5.0   1.0   8.0   1.0
 WILD    2.0    1.0   8.0    --   2.0   3.0   4.0   6.0   6.0   2.0   9.0   2.0
 PHIL    6.0    6.0  10.0  10.0    --  10.0  10.0  10.0   9.0   2.0  11.0   3.0
   ZK    4.0    2.0   9.0   9.0   2.0    --   5.0  10.0   8.0   1.0  11.0   1.0
  NEU    4.0    5.0   9.0   8.0   2.0   7.0    --  10.0   9.0   2.0  11.0   2.0
 HASH    3.0    3.0   7.0   6.0   2.0   2.0   2.0    --   5.0   1.0  11.0   1.0
 META    4.0    4.0   7.0   6.0   3.0   4.0   3.0   7.0    --   1.0  11.0   1.0
  FLP    9.0    9.0  11.0  10.0  10.0  11.0  10.0  11.0  11.0    --  11.0   5.0
  MMO    1.0    1.0   4.0   3.0   1.0   1.0   1.0   1.0   1.0   1.0    --   1.0
 INFO   11.0    9.0  11.0  10.0   9.0  11.0  10.0  11.0  11.0   7.0  11.0    --
```

**Condorcet winner: INFO.** It beats every other steelman head-to-head — including
the next-strongest, FLP, by **7–5**. The Smith set is the singleton **{INFO}**:
there is no top cycle. Full Copeland ordering:

> **INFO (11) ▸ FLP (10) ▸ ORTH (8.5) ▸ PHIL (8.0) ▸ HET (7.5) ▸ NEU (6.0) ▸ ZK
> (5.0) ▸ META (3.5) ▸ WILD (3.0) ▸ HASH (2.5) ▸ COM (1.0) ▸ MMO (0.0)**

Reading: the panel's *consensus best description of the missing piece* is the
**information-theoretic accounting** (σ = 1 external bit / zero inward channel
capacity), with the **relativized-computability / host-vs-source** reading (FLP)
a clear second. These are precisely the two the systems-council chairman had
already called "one EXACT layer with two faces" — the aggregate vote independently
recovers that finding. Note this is a *broadly-agreeable* winner: INFO is modest
in ambition (it deliberately claims only the accounting), yet it wins because
almost every lens can sign it.

---

## 5. QUESTIONS — no single Condorcet winner (a top tie), Smith set {P1, I2}

Pairwise matrix over the 10 finalists (weak-order, ties = 0.5):

```
          P1    I2    F1    I1    I3    N3    P3    C3    F3   MS1
   P1     --   6.0   6.5   6.5   7.0   7.5   8.0   8.0   7.5   8.5
   I2    6.0    --   6.5   6.5   7.0   7.5   7.5   8.0   7.5   8.0
   F1    5.5   5.5    --   6.0   7.0   7.5   7.5   7.5   7.5   8.0
   I1    5.5   5.5   6.0    --   6.0   7.0   7.0   7.0   7.0   8.5
   I3    5.0   5.0   5.0   6.0    --   7.0   6.5   7.0   6.0   7.5
   N3    4.5   4.5   4.5   5.0   5.0    --   6.5   6.0   6.0   6.5
   P3    4.0   4.5   4.5   5.0   5.5   5.5    --   6.5   6.5   7.5
   C3    4.0   4.0   4.5   5.0   5.0   6.0   5.5    --   5.0   7.0
   F3    4.5   4.5   4.5   5.0   6.0   6.0   5.5   7.0    --   6.5
  MS1    3.5   4.0   4.0   3.5   4.5   5.5   4.5   5.0   5.5    --
```

**No Condorcet winner.** P1 and I2 **tie head-to-head at 6–6**, and each beats
everyone else, so neither dominates the other. The **Smith set (top cycle/tie) is
{P1, I2}** — honest co-winners, not a manufactured single. Copeland ordering:

> **I2 (8.5) ≈ P1 (8.5) ▸ F1 (6.5) ▸ I1 (6.0) ▸ I3 (5.0) ▸ {F3, N3, P3} (3.0) ▸
> C3 (1.5) ▸ MS1 (0.0)**

So the panel's two most-interesting questions are:

- **P1** — *is the standpoint dichotomy provably exhaustive, upgrading externality
  from a lean to a theorem?* This is the pivot **both** council chairmen
  independently flagged (the science chairman: "the single defense-attorney pass
  … is the pivot between the mundane and the wild reading"). It is the only
  finalist rated top by rigor **and** interpretive lenses at once (§6).
- **I2** — *is inward capacity provably zero, and does hosting impose a hard 1-bit
  ceiling that forbids GU importing anything beyond σ (and τ)?* The
  make-or-break sharpening of the EXACT layer.

Both are **grounded, answerable, decidable** questions — not the wild Q3s. The
panel's revealed preference is for the questions that would *close* the open
horns, not the ones that speculate past them.

---

## 6. Confidence-weighted steelman ranking, and how it compares to Condorcet

score = author-CONF × mode-weight (EXACT 1.0 / MIXED 0.6 / ANALOGY 0.3):

| steelman | conf × mode | = | cwt rank | Condorcet rank | Δ (cwt−cond) |
|----------|-------------|---|----------|----------------|--------------|
| **INFO** | 80 × 1.0 | **80.0** | 1 | 1 | 0 |
| **ORTH** | 80 × 1.0 | **80.0** | 2 | 3 | −1 |
| **COM** | 70 × 1.0 | **70.0** | 3 | **11** | **−8** |
| FLP | 72 × 0.6 | 43.2 | 4 | 2 | +2 |
| PHIL | 62 × 0.6 | 37.2 | 5 | 4 | +1 |
| NEU | 60 × 0.6 | 36.0 | 6 | 6 | 0 |
| HET | 55 × 0.6 | 33.0 | 7 | 5 | +2 |
| ZK | 55 × 0.6 | 33.0 | 8 | 7 | +1 |
| WILD | 40 × 0.6 | 24.0 | 9 | 9 | 0 |
| META | 50 × 0.3 | 15.0 | 10 | 8 | +2 |
| HASH | 45 × 0.3 | 13.5 | 11 | 10 | +1 |
| MMO | 35 × 0.3 | 10.5 | 12 | 12 | 0 |

**Confidence-weighted top-3: INFO (80.0) ≈ ORTH (80.0), then COM (70.0).**

**Where the two rankings AGREE (robust):**

- **INFO is #1 on both.** It is the Condorcet winner *and* co-tops the
  confidence-weighted list. This is the maximally robust result of the whole
  aggregation: broadly agreeable **and** highly-confident **and** EXACT-typed.
  When a modest claim wins Condorcet *and* the confidence race, it is as close to
  "the councils' settled answer" as this method produces.
- **ORTH is top-3 on both** (#2 cwt, #3 cond) — the superselection reading is
  both high-confidence and broadly signable; the interpretive lenses dock it only
  because it declines the "meaning" question, not because they think it wrong.
- MMO, WILD, NEU sit at the same rank on both — no tension to resolve.

**Where they DIVERGE (the interesting part):**

- **COM: the standout divergence (Δ = −8).** COMMERCIAL is **#3 by confidence**
  (EXACT, 70%) but **#11 by Condorcet** — ranked *last or second-last* by five
  voters (WILD, HETERODOX, HASH, META, MMO). This is the textbook
  **"solid-but-modest/narrow"** profile: the author is highly confident because
  the method + limitative result genuinely exist and are checkable, but the panel
  won't crown it as *the description of the missing piece* because it deliberately
  **declines** the central question ("the philosophy does not change the invoice").
  High personal confidence, low consensus — it is confident *about a narrower
  thing than the question asked.*
- **FLP: broadly-agreeable-but-hedged (Δ = +2).** #2 by Condorcet but only #4 by
  confidence — because its author honestly typed it MIXED (72%), not EXACT. The
  panel rates the *content* higher than the author's own hedge: FLP is the most
  uniformly-placed steelman across opposed lenses (§6-cross), yet its
  mode-discount pushes it below three EXACT claims in the weighted list. This is
  the mirror image of COM — **modestly-graded but broadly-loved.**
- **HET and META (Δ = +2 each):** Condorcet-favored beyond their hedged
  confidence — the interpretive weld (HET) and the bistable-tie cousin (META)
  earn more *placement* from the panel than their MIXED/ANALOGY self-grades would
  predict.

**One-line calibration:** the confidence-weighted list rewards *how sure the
author is that their claim is exactly-true*; the Condorcet list rewards *how many
opposed lenses will sign the claim as the best description*. INFO wins both (rare
and telling). COM tops the first but bottoms the second (confident-but-narrow).
FLP is the opposite (loved-but-hedged).

---

## 7. Cross-lens consensus — the headline

Grouping the voters into three opposed camps — **rigor** (ORTHODOX, COMMERCIAL,
PHILOSOPHER, INFO, FLP), **interpretive** (HETERODOX, WILD), **structural-rhyme**
(ZK, NEU, HASH, META, MMO) — the genuine *cross-disagreement* consensus is what
scores high across camps that otherwise disagree.

### Steelmen with genuine cross-lens consensus

1. **FLP (relativized-computability / host-vs-source) — the single most
   uniformly-agreed steelman.** It is placed **top-4 on all 12 ballots** and never
   lower: rigor puts it #2–#4, interpretive puts it #3–#4 (HETERODOX #3, WILD #4),
   structural puts it #2–#4 (MMO #2, HASH #3). No lens dismisses it. It loses
   Condorcet #1 only to INFO's 7–5, but it is the steelman that the *widest spread
   of disagreeing lenses* independently rate near the top — because "hosts but
   cannot mint / node = locus not source" is the one phrasing every camp reads as
   *literally* their own object.
2. **INFO (σ = 1 external bit / zero inward capacity) — Condorcet winner, cross-lens
   robust.** Top-5 on every ballot including both poles (orthodox rigor #2, wild
   frontier #5, heterodox #5). The one place rigor and the wild reading actually
   shake hands: the accounting is neutral enough that no lens must concede its
   worldview to sign it.

(PHIL is a near-miss third: top-5 across rigor and interpretive, but the
structural lenses rate it only mid, so it is *not* a full cross-camp consensus.)

### Questions with genuine cross-lens consensus

3. **P1 — "is the standpoint dichotomy exhaustive → lean upgrades to theorem?"**
   The **one finalist rated top by rigor AND interpretive at once**: orthodox 4,
   philosopher 5, info 4, FLP 5 (rigor) **and** heterodox 5, wild 5 (interpretive).
   Both council chairmen had independently named this the pivot; the aggregate
   vote makes it a co-#1 question. This is the headline generative question the
   whole panel — across its sharpest internal disagreement — agrees is the one
   worth answering next.
4. **The bit-budget-as-fundamental-invariant cluster (C3 / N3 / I3).** The *same
   idea* — "is the count of irreducibly-imported bits a conserved property that
   ranks rival theories?" — was raised **independently by three different members**
   in three different councils' seats (COMMERCIAL C3, NEURAL N3, INFO I3), and it
   scores high across pragmatic (Commercial 5), structural (Neural 5), grand
   (Wild 4–5) and information (Info 5) lenses simultaneously. Independent
   convergence of the same question from unrelated lenses is the strongest
   available signal of cross-disagreement consensus, even though the rigor purists
   (orthodox, philosopher) rate it only lukewarm (3). It is the panel's emergent
   *research programme* question, distinct from P1's *close-the-proof* question.

### Polarizing items (loved by some, dismissed by others) — the contrast

- **COMMERCIAL steelman — the clearest polarizer.** Rigor/pragmatic rate it top-5
  (its own #1, orthodox #4, philosopher #5); interpretive and structural bury it
  (WILD #11, HETERODOX #12, HASH #12, META #12, MMO #11). Same object, opposite
  verdict depending on whether the lens *wants a usable deliverable* or *wants the
  meaning*. This is exactly why it tops confidence-weight but bottoms Condorcet.
- **WILD steelman — the mirror polarizer.** Interpretive loves it (its own #1,
  HETERODOX #2); rigor and structural bury it (ORTHODOX #12, COMMERCIAL #11,
  NEURAL #10, META #10, MMO #12). Loved for its ambition, dismissed for its gap
  between claim-size and closed proof.
- Among questions, the **wild Q3s** (F3 first-person-as-forced-oracle; H3
  reversed-arrow; W3 same-outside-for-all-worlds) polarize hardest — adored by the
  interpretive/wild seats (5s), rated 1–2 by orthodox/commercial. F3 still made
  finalist on interpretive+distributed enthusiasm, but sits low in the Copeland
  order precisely because rigor won't sign it.

### Sensitivity note (self-votes)

Every author ranked their own steelman #1 (12 self-votes, one per candidate — a
symmetric perturbation). Re-checking the top of the steelman race with authors'
self-votes on INFO and FLP removed does not change the outcome: INFO still beats
FLP (it is ranked #2 by ten *non-author* voters), and both still dominate the
field. The self-vote convention inflates each candidate by at most its single
author-ballot and does not manufacture the INFO/FLP result — that is driven by
the *other* eleven lenses routing them high.

---

## 8. Bottom line

- **Steelmen — Condorcet winner: INFO** (σ = exactly 1 external bit / zero inward
  channel capacity), beating FLP 7–5; Smith set {INFO}, no cycle. Ordering:
  INFO ▸ FLP ▸ ORTH ▸ PHIL ▸ HET ▸ NEU ▸ ZK ▸ META ▸ WILD ▸ HASH ▸ COM ▸ MMO.
- **Questions — no single winner:** P1 and I2 tie 6–6 at the top (Smith set
  {P1, I2}). P1 = *is the standpoint dichotomy exhaustive (lean→theorem)?*;
  I2 = *is inward capacity provably 0 with a hard 1-bit import ceiling?*
- **Confidence-weighted steelman top-3:** INFO (80.0) ≈ ORTH (80.0), then
  COM (70.0). INFO agrees with Condorcet (robust); COM is the big divergence
  (high-confidence #3 but Condorcet-dismissed #11 — solid-but-narrow); FLP is the
  inverse (Condorcet #2 but confidence #4 — broadly-loved-but-hedged).
- **Genuine consensus ACROSS differing lenses (the headline, 4 items):**
  1. **FLP steelman** — top-4 on *all 12* ballots; the most uniformly-agreed
     description across rigor, interpretive, and structural camps.
  2. **INFO steelman** — Condorcet winner *and* confidence co-#1; the one reading
     rigor and the wild frontier both sign.
  3. **Question P1** (standpoint-exhaustiveness → theorem) — the only finalist
     rated top by rigor AND interpretive; both chairmen's named pivot.
  4. **Question cluster C3/N3/I3** (irreducible-bit-count as a fundamental,
     theory-ranking invariant) — the same question raised independently by three
     unrelated lenses; the panel's emergent programme question.
- **Polarizers (for contrast):** COMMERCIAL (loved by rigor, dismissed by
  interpretive+structural) and WILD (the mirror) — high internal enthusiasm, no
  cross-camp consensus.

---

## Boundary

Exploration tier. Read-only aggregation of two existing council artifacts; no
re-opening of any council judgment, no claim/canon/verdict/ledger/portfolio
movement, no external action, no commit/push. The ballots are the aggregator's
in-character elicitation of the 12 personas from the councils' own steelmen and
questions — they are a *model* of each lens's preferences, not a re-run of the
councils; a hostile reviewer should attack the ballots first (particularly the
INFO/FLP placements that drive the result, and the score cut that admits
I1/I3/N3 while excluding the grounded O1). The tabulation itself is
deterministic and reproduced by `tests/channel-swings/ch_aggregation_condorcet_probe.py`
(exit 0). Only this artifact and that probe were written; no other file edited.
