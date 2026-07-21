---
title: "CONSTRUCTION swing PRONG 3 (VERIFY-THE-OTHER-WAY / back-gate): hostile audit of the INDEPENDENT consequences Prongs 1 & 2 claimed. RESULT POSIT-PRODUCTIVE (narrow). C2's sigma_|_tau independence GENUINELY TRACKS the posit -- it HOLDS for the global closure-monodromy posit (Z/6 direct product) and FAILS for the shard-INTERNAL posit (order-24 coupling), so it is FORCED BY the posit, NOT re-hosted Q3 -- but it tracks only at global-vs-internal granularity and verifies an ANALOGOUS independence (sigma _|_ SHARD-rotation Z/3), not Q3's object-level sigma _|_ GENERATION-trit (a DIFFERENT Z/6, with sigma OUTSIDE Q3's); 'verifies Q3' is therefore contingent on keeping the two Z/3's distinct. C3 (one globally consistent arrow) is a RE-HOST of the banked Cech-H^1 one-arrow via the new P1 route -- it verifies but adds a derivation path, not a new reason. Prong-1's Cech descent obstruction and Prong-2's fixed-point/section count are the SAME degree-1 Z/2 holonomy class (descent-sections == Phi-fixed-points == w1(L_time) at deg 1) -- strong internal coherence, tempered by both prongs drawing on the shared banked TI H^1(finality sheaf). NO forced consequence contradicts a banked fact; two contingent seams flagged (non-identification of the two Z/3's; which arrow is 'the' global one). Falsifiable = C3's odd-parity descent-defect prediction (already banked). sigma kept as a POSIT throughout."
status: active_research
doc_type: exploration
created: 2026-07-21
mode: CONSTRUCTION/posit-declared (back-gate)
prereg: explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
outcome: POSIT-PRODUCTIVE (narrow) -- one tracking forcing (C2 independence) + the cross-prong H^1 structure; C3 is a re-host; no contradiction
probe: tests/channel-swings/construction_prong3_verify_probe.py
probe_exit: 0
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
inputs:
  - explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
  - explorations/construction-prong1-structural-2026-07-21.md
  - explorations/construction-prong2-dynamical-2026-07-21.md
  - explorations/decision-tree-Q3-one-anchor-vs-two-2026-07-21.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/shard-cycle-prong1-geometry-2026-07-21.md
---

# Construction Prong 3 -- VERIFY THE OTHER WAY (the back-gate)

## 0. Mode and one-line verdict (read first)

This is the **hostile back-gate**. Both construction prongs reported positive
"wins." Construction mode's one failure mode is a consequence that is secretly
**the posit (or a banked fact) re-inserted, dressed as forced.** For every win the
decisive test is the prereg's own rule:

> does the consequence **TRACK the posit** -- change when you change the posit
> (=> genuinely forced BY it) -- or hold **REGARDLESS** (=> a re-hosted banked
> fact wearing the posit's costume)?

`sigma` is kept **labelled as a POSIT** throughout; nothing here derives its value.

> **Verdict: `POSIT-PRODUCTIVE` (narrow).** The construction earns its keep on
> **one** genuine track-the-posit forcing plus **one** structural result, but
> the headline "verifies Q3 / verifies one-arrow" framing is **downgraded**:
>
> - **C2 (the `Z/6 = Z/2 x Z/3` independence) GENUINELY TRACKS the posit.** It
>   HOLDS for the global closure-monodromy posit (`<Q,R> = Z/6`, direct) and
>   **FAILS** for the shard-INTERNAL posit (`order-24` semidirect coupling). So
>   the independence is **forced BY the posit's global character, not re-hosted
>   Q3.** **But** (a) it tracks only at **global-vs-internal** granularity (any
>   global `Z/2` gives `Z/6`; the closure-monodromy is not singled out), and (b)
>   it verifies an **ANALOGOUS** independence -- `sigma _|_` the **SHARD-rotation**
>   `Z/3` -- **not** Q3's object-level `sigma _|_` the **GENERATION-trit**. Prong-1's
>   `Z/6` (`sigma x` shard-rotation) is a **DIFFERENT group** from Q3's `Z/6`
>   (deck-admissibility `x` trit, with `sigma` OUTSIDE it). "Verifies Q3" is
>   therefore **contingent** on keeping the two `Z/3`s distinct.
> - **C3 (one globally consistent arrow) is a RE-HOST.** It re-derives the banked
>   Cech-`H^1` descent one-arrow via the new P1 route, with the same mechanism and
>   the same 4-of-8/6-of-16 prediction. It verifies and adds a **route**, not a
>   new **reason**.
> - **The two prongs' `H^1` are the SAME object.** Prong-1's Cech descent
>   obstruction and Prong-2's fixed-point/section count are the **same degree-1
>   `Z/2` holonomy class** (`descent-sections == Phi-fixed-points == w1(L_time)`
>   at deg 1). Strong internal coherence -- tempered by the honest note that both
>   prongs draw on the shared banked TI `H^1`(finality sheaf).
> - **CONTRADICTION SWEEP: none.** No forced consequence contradicts a banked
>   fact. Two contingent seams flagged (S1 the two `Z/3`s must stay distinct; S2
>   the two prongs name different "global arrows").
>
> Probe `tests/channel-swings/construction_prong3_verify_probe.py`,
> foreground, pure enumeration, two-run byte-identical, **EXIT 0**, `A=1 B=1 H=1
> S=1 ALL PASS`.

---

## 1. C2 -- the key check: does `sigma _|_ tau` TRACK the posit, or is it re-hosted Q3?

### 1.1 The attack

Prong 1's payoff is C2: positing `sigma =` the closure monodromy of three
**isomorphic** sheaves FORCES `Z/6 = Z/2 x Z/3` as a **direct product** with
`sigma` independent of the `Z/3` shard-rotation, and Prong 1 calls this "verifies
Q3 `sigma _|_ tau`." The hostile question: is the **independence** genuinely
FORCED by the posit, or does it hold **regardless** (=> it is just Q3, re-hosted)?

The suspicion is sharp because **Prong-1's own probe never varied the posit.** Its
`[G]` test builds the `Z/2` as `Q = kron(eye(3), Qsgn)` -- a global sign on a
tensor factor **disjoint** from the shard-label -- so `[Q,R] = 0` is **baked in by
that tensor choice.** A test that only checks `[Q,R]=0` on that construction has no
power to tell "forced" from "modelled that way." The right test is the prereg's:
**vary the posit, watch the independence.**

### 1.2 The deterministic tracking probe (the gap filled)

The probe builds **both** posits as concrete permutation groups and compares
(probe `[A]`):

- **CORRECT posit P2** (`sigma =` ONE **global** closure monodromy). State
  `= (shard-label, deck-sign)`. `R` (shard-`Z/3`) rotates the label; `Q` (`sigma`-
  `Z/2`) flips the deck-sign. Disjoint factors:
  - `[Q,R] = 0`; `<Q,R> = Z/6` (**order 6, direct product**); `sigma` is
    **R-invariant** (`R` never touches the deck bit). **Independence HOLDS.**
- **VARIED posit** (`sigma =` a **shard-INTERNAL** orientation, one bit per shard).
  State `= (shard-label, o0, o1, o2)`. The shard-rotation now **also permutes the
  three per-shard orientations** (`o0,o1,o2) -> (o2,o0,o1`); `Q_i` flips `o_i`:
  - `[R, Q0] != 0`; `<R, Q0, Q1, Q2> = (Z/2)^3 semidirect Z/3` (**order 24**);
    a fixed shard-internal datum is **NOT R-invariant** (new `o0 =` old `o2`).
    **Independence FAILS** -- the "sigma" is a genuine `Z/3`-module.

> **`C2_tracks_the_posit = True`.** The independence FLIPS when the posit's
> global-vs-internal character flips (`|G| = 6` vs `24`; indep `True` vs `False`).
> So the `sigma _|_` shard-rotation independence is **FORCED BY the posit**, not
> held regardless. **C2 is NOT merely re-hosted Q3.** [probe `[A]`]

This is a real result and it is the strongest thing the construction produces: the
independence is a genuine consequence of the posit's **global** character. The
mechanism it adds beyond the banked Q3 is a **reason**: a monodromy valued in the
**abelian** deck group is fixed by the diagram's cyclic permutation (cyclic-shift
of edge-signs leaves their product invariant), so the extension **splits**; a
per-shard datum is instead **permuted** by that same rotation and cannot split off.
That reason is not in Q3; it is forced by P1+P2.

### 1.3 The two honest downgrades (why this is *narrow*)

**Downgrade 1 -- granularity (probe `[B]`).** The tracking distinguishes only
**global vs internal.** Within the global class, **any** single `Z/2` on the
disjoint factor commutes with `R` and gives `Z/6` -- the closure-monodromy is
**not** singled out from any other global bit. So C2 forces "*independence GIVEN
`sigma` is global*," a **relational/shape** fact, not a new **number** and not a
fingerprint of the specific closure-orientation. This matches Prong 1's own honest
self-assessment ("relational/orientation facts... not a new number forced from
`sigma`").

**Downgrade 2 -- it is the WRONG `Z/3` for Q3 (probe `[S1]`).** Q3's `tau` is the
**generation trit** -- the `Z/3` on the internal `S^3` fibre that controls the
**fermion generation count** (Q3 sec. 1, 5). Prong-1's `Z/3` is the **shard-
rotation** -- the cyclic relabelling of the three **epistemic** shards
subjective/intersubjective/objective. These are both "3" but are **different
objects with no established identification.** Consequently:

- Prong-1's `Z/6 = {sigma_Krein} x {shard-rotation Z/3}`.
- Q3's `Z/6 = {deck-admissibility Z/2} x {generation-trit Z/3}`, with **`sigma`
  OUTSIDE it** (Q3's verdict: the discrete external input is at least
  `Z/2_Krein x Z/6_gen`, the two `Z/2`s **distinct**).

These are **different groups.** Prong 1 puts `sigma` **inside** a `Z/6`; Q3 keeps
`sigma` **outside** its `Z/6`. The construction therefore does **not** reconstruct
Q3's actual ledger; it builds a **new** `Z/6` that shares the abstract shape
`Z/2 x Z/3`. Prong 1 is honest about this ("verifies the **shape**, not an
**object-level identity** shard-`Z/3` = generation-`tau`"), but its "concrete
instance of Q3's escape clause / demonstrates Q3-independence survives base-uniting"
does more rhetorical work than the math: the shard-cycle unites S/I/O, a **third**
base, not Q3's `F` vs `S^3` union.

**Net C2:** a genuine track-the-posit forcing that adds a structural **reason**
(abelian-deck split) -- so it clears the prereg's `POSIT-PRODUCTIVE` bar (which
explicitly allows "a reason/structure" as the "something beyond") -- but its
connection to Q3 is by **analogy/shape**, contingent on the two `Z/3`s staying
distinct, **not** a verification of Q3's object-level claim. Reported straight,
not inflated.

---

## 2. C3 -- one globally consistent arrow: forcing or re-host?

C3: P1 (isomorphic sheaves glued in a cycle) forces `sigma` to **be** the Cech
`H^1` descent obstruction; the relative orientation `c_ij = sigma_i sigma_j` is an
`alpha`-even 1-cocycle with vanishing coboundary; on triangles `c12 c23 c31 = +1`
identically, forbidding 4 of 8 odd-parity configs => "one globally consistent
record arrow."

- **Tracks the posit?** Yes, of **P1**: the descent structure follows from
  isomorphic-sheaf gluing; drop P1 and there is no descent problem of this form.
- **Adds a reason beyond the banked one-arrow?** **No.** The banked one-arrow
  (Prong-3 `F-FALSIFIABLE-CONSISTENT`; council Members 2/5's cup-product / Cech-
  `H^1` descent rule; the 6-of-16 / 4-of-8 forbidden-configuration prediction)
  **already is** exactly this Cech-`H^1` descent mechanism, with exactly this
  prediction. Prong 1 states as much ("This is **precisely** the banked one
  globally consistent record arrow"). So C3 re-derives the banked result's **own
  mechanism** through the new P1 route. It adds a **derivation path**, not a new
  **reason** and not a new **prediction.**

**Verdict on C3: a RE-HOST** (verifies, tracks P1, but the reason and the
falsifiable content are the banked one-arrow's, not new). It supports coherence;
it is not the independent new forcing that would, on its own, earn
`POSIT-PRODUCTIVE`.

---

## 3. Cross-prong `H^1` coherence -- same object or coincidental naming?

Prong 1: `sigma =` the Cech `H^1` gluing obstruction on the shard-cycle (three
isomorphic sheaves glue **iff** composite monodromy trivial **iff** `sigma = +1`).
Prong 2: the fixed-point count `=` `H^1`(finality sheaf) (`h=0 =>` `H^1` vanishes,
2 sections; `h=1 =>` `H^1 != 0`, 0 sections). Are these the **same** `H^1`?

The probe computes each **independently** as a function of the monodromy `g in
Z/2` (probe `[H]`):

| `g` (`sigma`) | Prong-1 descent sections | Prong-2 `Phi` fixed points |
|---|---|---|
| `0` (`+1`, trivial) | **2** | **2** |
| `1` (`-1`, flip) | **0** | **0** |

> `descent-sections == Phi-fixed-points` for both `g` (`H1_tables_identical =
> True`), and both `= (2 if g==0 else 0) = ` the value keyed on
> `w1(L_time) = g` at degree 1 (`same_H1_object = True`).

They are the **SAME object**: the first cohomology / global-section count of the
**same rank-1 `Z/2` local system** on the **same** `S->I->O->S` loop, with the
**same** monodromy `= sigma`, vanishing **iff** `sigma = +1`. Cech "do the sheaves
glue" and Lawvere "does a global orientation section exist" are two computations of
one class. It also coheres with the **banked** `sigma = w1(L_time)` (shard-cycle-
prong1): `w1` **is** the degree-1 `Z/2` characteristic class classifying that local
system / orientation double cover. So **three** routes -- structural descent,
dynamical fixed-point count, banked `w1` -- land on **one** degree-1 `Z/2` holonomy
class. This is the construction's most solid structural yield: **`sigma` is
uniformly an `H^1`/holonomy class, cross-confirmed.**

**Honest temper (not a defect, but stated):** both prongs **cite the same banked
TI apparatus** (`DRIVING-HYPOTHESIS-OBSERVER-ISSUANCE.md`'s "shared reality =
global section iff `H^1`(finality sheaf) vanishes"; the triple
`objectivity <=> causal-invariance <=> H^1 = 0`). Prong 2 says outright "this **IS**
the TI `H^1`(finality sheaf) computation." So the agreement is **two views of the
posit both correctly reducing to a shared banked object**, i.e. **convergence-on-a-
shared-object**, not fully independent triangulation. It is genuine coherence (the
same `H^1`, not two coincidentally-named ones), just not two-from-scratch.

---

## 4. Contradiction sweep

Every forced consequence checked against the banked facts (probe `[S]`):

| consequence | banked fact | result |
|---|---|---|
| C1 realization map `f` pinned `pi_1`-nontrivial | shard-cycle-prong1: `f` free | **consistent** -- the POSIT supplies the free bit; GU still doesn't pin it |
| C2 `Z/6 = Z/2 x Z/3`, `sigma _|_` shard-`Z/3` | Q3 `sigma _|_ tau` | **consistent, contingent** (S1 below) |
| C3 descent one-arrow | banked one-arrow | **consistent** (re-host) |
| C4 null-stratum branch locus / ~8% | UNESTABLISHED (Prong 0/1/A) | **consistent** (scaffold, matches) |
| P2 IC-1 alpha-even issuance arrow | one-global-arrow | **consistent** (S2 below) |
| P2 never-unique fixed-point count | Q2-FREE (sigma external) | **consistent, reinforces** (S3) |
| P2 IC-4 generations alpha-even spectators | Q3 (gen deck != sigma) | **consistent** |

**No flat contradiction.** Two contingent seams a hostile reader must see:

- **S1 (the two `Z/3`s must stay distinct).** Consistency of C2 with Q3 **requires**
  shard-`Z/3` `!=` generation-trit. If a future move **identified** them (and kept
  Q3's generation `Z/6 =` deck-`Z/2` `x` trit), then Prong-1's `Z/6` would force
  `sigma` into the **deck-admissibility slot** -- but Q3 proved `sigma != ` the
  deck-admissibility bit (different observables; free coin vs one-sided constraint).
  So **identifying the two `Z/3`s WOULD contradict Q3** (`S1_would_contradict_if_
  identified = True`). Prong 1 does not identify them, so it is safe -- but the
  safety is **contingent**, and this is exactly where "verifies Q3" is doing
  unearned work.

- **S2 (which arrow is "the" global one).** Prong-1/C3 locates the one global arrow
  in the **`alpha`-ODD record direction** (glues iff `sigma = +1`, conditional).
  Prong-2/IC-1 locates it in the **`alpha`-EVEN issuance index** (monotone
  **regardless** of `sigma`, unconditional). These are **two distinct arrows**, so
  there is **no contradiction** -- but the prongs' "one arrow" consequences are
  **not the same object**, and the banked one-arrow is best read as the `alpha`-even
  issuance monotonicity (Prong-2's placement). A naming seam, reconcilable, worth
  recording.

- **S3.** Prong-2's never-unique count (`2` or `0`, never `1`) **reinforces**
  Q2-FREE: the dynamics never uniquely fix `sigma`, so it stays external. No
  tension.

**Contradiction sweep: clean. The posit is NOT contradicted.**

---

## 5. Consolidated verdict and the falsifiable/scaffold split

### 5.1 Verdict

**`POSIT-PRODUCTIVE` (narrow).** By the prereg's criterion -- "at least one
consequence genuinely tracks the posit AND verifies AND adds something beyond the
banked fact (a reason/structure)" -- the construction clears the bar on:

1. **C2's independence** genuinely **tracks the posit** (global => `Z/6`
   independence; shard-internal => order-24 coupling) and **adds a reason** (the
   abelian-deck split: monodromy `_|_` permutation because the deck is abelian).
   That reason is not in the banked Q3.
2. **The cross-prong `H^1` structure**: `sigma` is uniformly the **same degree-1
   `Z/2` holonomy class** from descent, from the fixed-point count, and from the
   banked `w1(L_time)` -- a structural fact the construction organizes and
   confirms.

The verdict is **narrow / qualified** because the two headline "verifications" are
weaker than presented: C2 verifies an **analogous** independence (`sigma _|_`
shard-`Z/3`), **not** Q3's object-level `sigma _|_` generation-trit (a different
`Z/6`), and its tracking is only global-vs-internal; **C3 is a re-host** of the
banked Cech-`H^1` one-arrow. The construction **organizes** the banked
`sigma`/`tau`/arrow/`H^1` structure into one coherent object and shows it is
self-consistent, discriminating (the planted shard-internal control dies for two
independent reasons -- Prong-1's `alpha`-even blindness **and** this prong's order-24
coupling), and posit-tracking -- but in construction mode it does **not**, and must
not, derive `sigma`'s value.

Not `POSIT-CONTRADICTED`: the sweep is clean. Not a pure `POSIT-COHERENT-SCAFFOLD`
either: C2's tracking-plus-reason is a genuine new forcing, not only a re-host.

### 5.2 Directly falsifiable (route to the FALSIFICATION-BATTERY)

- **C3's descent-defect prediction** -- an observed **odd-parity orientation defect
  over a contractible region** falsifies "one globally consistent arrow" (the
  4-of-8 / 6-of-16 forbidden set). This is the one directly falsifiable
  consequence -- **but it is the banked one-arrow's own prediction**, so it is
  **already in the battery**; the construction adds a derivation route, not a new
  battery entry.
- **IC-2's half-frequency record-rate relation** (orientation orbit period =
  `2x` loop period in the flip sector) is quasi-observable but qualitative --
  battery-adjacent, not a sharp new test.

### 5.3 Scaffold (keep; name the downstream test)

- **C1** (realization map `f` pinned `pi_1`-nontrivial) -- names the downstream
  object `f`; the residue is only "forced-once-posited."
- **C2's shape** -- to connect shard-`Z/3` to the generation-trit needs the
  **operator-grade base-uniting map** Q3 sec. 4 named (`S^3` and `F` onto one base
  under `sgn_K`); does not exist at fixture grade.
- **C4** (null-stratum identity + `~8%`) -- gated on the open **N2 operator-lift**.
- **IC-3** (non-uniqueness `<=>` null-seam re-freeing) -- qualitative; the `~8%`
  is not reproduced.
- **IC-4** (generations `alpha`-even spectators) -- consistency, near-restatement.
- **The operator-grade lift** of Prong-2's fixed-point count -- rides on the same
  **product-uniformity** theorem as the static Lawvere leg. No new gate.

---

## 6. Boundary

Exploration tier, CONSTRUCTION mode, back-gate. `sigma` kept **labelled as a
POSIT** throughout; nothing here derives its value. Only this artifact and its
probe (`tests/channel-swings/construction_prong3_verify_probe.py`, foreground,
pure enumeration, no numpy, no network, **two-run byte-identical**, **EXIT 0**,
`A=1 B=1 H=1 S=1 ALL PASS`) were written. The probe fills the exact gap the Prong-1
probe left: it **varies the posit** (global closure-monodromy vs shard-internal)
and watches whether C2's independence tracks it. GU otherwise read-only; Prongs 1/2
and all banked-fact artifacts consumed read-only, not edited. **No commit, no
push.** No edit to any claim / canon / verdict / ledger / LANE-STATE /
research-portfolio / NEXT-STEPS / prereg / frozen-packet file, or any other agent's
artifact. `claim_status_change: none`, `canon_verdict_change: none`,
`public_posture_change: none`, no external actions. All work is conditional at
exploration grade; nothing here is a GU verdict, and the externality of `sigma`
remains the program's closed premise, nowhere re-derived.
