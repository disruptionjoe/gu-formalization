---
artifact_type: exploration
status: exploration
doc_type: ledger-advancement-delta
created: 2026-08-15
work_item: LA-3
channel: conditional_ledger_advancement
base_revision: a148ed80
target_claim: "NONE — no GU source claim is targeted, attacked or defended. The object adjudicated is the CONDITION STRING carried by ledger rows AC-D1..AC-D5 (`distance: none after the chiral 16 shadow is selected`) and their revival trigger."
title: "LA-3: the 'chiral 16 shadow' is a fork-1 conventional comparator, and — independently — the chirality half of the grant is INERT while the completeness half is STRICTLY TOO STRONG. Computed exactly on the signed multiplicity lattice Z^6 of the 16's own SM constituents: the five 4D SM anomaly channels are LINEAR functionals of rank 4, not 5 (exact relation 2 D1 - 27 D2 - 36 D3 - 9 D4 + 9 D5 = 0), so AC-D1..AC-D5 are four independent facts and one corollary; the anomaly-free set is the rank-2 SATURATED lattice L = Z.(15 of SU(5)) (+) Z.(nu^c), exhaustively verified over [-3,3]^6 with zero solutions outside; L is a SUBGROUP, so it is closed under chirality flip and contains 0, and a chiral 16 and the EMPTY content return the identical anomaly vector. ZERO ROWS ADVANCE. The deliverable is the typed-bridge specification, and its finding is sharper than 'unbuilt': bridge-burden items 5 and 6 are UNSATISFIABLE for these rows because the transported observable is constant on the entire admissible set, so a bridge would not move them even once built. All discriminating power lives upstream in RA-A3/RA-B1..RA-B5."
grade: "EXACT sympy Rational linear algebra over Q on a 5x6 functional matrix plus exhaustive integer search over [-3,3]^6 (117649 points); no float is load-bearing anywhere. 41/41 checks, exit 0 (26 [E] exact results, 15 [C] controls that must fire). Non-vacuity established four ways: seven live controls that MUST return nonzero (drop e^c breaks D4 and D5; quark doublets alone break D1; one d^c triplet breaks D1; one extra u^c breaks D3; one extra L breaks D2; swapping n_L and n_e breaks D5); two hypercharge MUTATION controls (Y(e^c)=1/2 and Y(Q)=1/3 both destroy the zero, and the first raises the rank to 5 and collapses the kernel to dim 1); an ARENA control (drop nu^c and the kernel falls to rank 1); and two ARENA-EXTENSION controls proving the rank-4 result is arena-specific, not a universal fact about the five SM channels (adding one exotic Y=1/2 singlet or one exotic Y=-1/6 triplet restores rank 5). NOT: a 14D statement, a claim about the unbuilt reduction, a generation count, a chirality-production claim, a real-form statement, a source-native result, or any verdict movement."
disposition: CHIRAL_16_SHADOW_IS_A_FORK1_CONVENTIONAL_COMPARATOR__CHIRALITY_CLAUSE_OF_THE_GRANT_IS_EXACTLY_INERT__COMPLETENESS_CLAUSE_IS_STRICTLY_TOO_STRONG__REVIVAL_TRIGGER_IS_FALSE_AS_STATED__FIVE_ROWS_ARE_RANK_4_NOT_5__ZERO_ROWS_ADVANCE__TYPED_BRIDGE_SPECIFIED_AND_SHOWN_NON_INFORMATIVE_AT_ITEMS_5_AND_6
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_touched: [AC-D1, AC-D2, AC-D3, AC-D4, AC-D5]
rows_advanced: 0
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/process/conditional-physics-ledger-v0.258.json
  - explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
  - explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md
  - tests/one-residual/sm_mirror_anomaly_free.py
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - canon/exhaustiveness-by-type-RESULTS.md
  - CURRENT-STATE.yaml
scripts:
  - lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-grant-probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# LA-3 — the chiral 16 shadow is the comparator, and the grant does no work

**Headline, stated before anything else: zero rows advance, and that is the
correct outcome.** Five rows were nominated as free upgrades. They are not
upgrades, they are not five, and they are not free. What is delivered instead
is (a) a routing verdict, (b) three exact corrections to what those rows say
about themselves, and (c) a typed-bridge specification whose finding is
stronger than "unbuilt".

---

## 0. Prior art, swept by mechanism, and what this file does not re-claim

Swept by mechanism (anomaly coefficient, cubic Casimir, hypercharge trace,
multiplicity, content lattice, chirality, comparator routing), not by label.

| already owned | owner | what it owns |
|---|---|---|
| a complete chiral `16` has vanishing `SU(3)^3`, `SU(2)^2U(1)`, `SU(3)^2U(1)`, `U(1)_Y^3`, `grav^2U(1)` | `explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md`; `tests/one-residual/sm_mirror_anomaly_free.py` | the five zeros themselves, on a fixed complete `16` |
| `d^abc = 0` and `Tr T^a = 0` on the `16`, the vector `10`, and `10 (x) 16 = 144 (+) 16` of `so(6,4)`; RS spin factors `(3,4,5)` / `(-21,-20,-19)`; the fork→anomaly map is CONSTANT on GU's content | **AC-1**, `tests/channel-swings/joe_directed_anomaly_cancellation_probe.py` | the group-theoretic mechanism, the RS layer, and the selector-power route-kill |
| the 14D local content system: rank 5 on a 15-dim lattice, kernel dim 10, `W = 0` **derived**; and the Group-D scoping sentence *"the residue on this group is entirely `U4`, not the anomaly conditions"* | `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md` | the rows' own upstream evidence file, including the fact that the whole residue is `U4` |
| the `144` is a **mirror** of multiplicity exactly one; the `2+1` is **forced but subtractive and unlabelled**; the degree-3 anomaly invariant is **blind** to the `144` | **HE-1** | why "select a chiral 16" is not a neutral request |
| `PH-K1-KINEMATIC`: every block of `ker Gamma` is separately chirality-balanced (`192+192`, `576+576`, `64+64`) | `cb-c` row F2; `explorations/chirality-grading-and-77-rerun-2026-08-03.md` | the block-side confirmation that the bulk is balanced |
| the comparator/source-native boundary and its six-item bridge burden | `lab/methods/source-native-comparator-routing.md` (mandatory, 2026-08-14) | fork 1 and the inference rule this file applies |
| "nothing routes around SG4"; SG4 is the unique open decider | `canon/gu-forces-field-space-declaration-RESULTS.md`, `canon/exhaustiveness-by-type-RESULTS.md` | the owner of the field-space declaration |

**Honest accounting: the five zeros and their group-theoretic cause are
entirely owned, and this file re-claims none of them.** AC-1's zeros are used
as *inputs*, cited, never re-derived.

Two things the sweep found **not** owned, and they are what LA-3 adds:

1. **The multiplicity lattice was never computed.** Every in-repo 4D anomaly
   computation evaluates the channels on *one fixed content* (a complete `16`,
   or `16 (+) 16bar`). No artifact asks the quantified question the ledger rows
   actually pose — *which contents are anomaly-free?* — even though both the
   `distance` string ("complete 16s") and the `revival_trigger` ("a physical
   carrier not equal to complete 16s") quantify over contents. `cb-c` computed
   the analogous object in **14D** (rank 5 on `Z^15`); the **4D** analogue is
   absent. It is computed here.
2. **The rows' condition string was never routed.** The routing boundary is one
   day old and the rows predate it. Nobody has asked whether "the chiral 16
   shadow" is a source-native object or a fork-1 comparator.

---

## 1. PREFLIGHT — six specialist lenses, run inline

Standing rule: N lenses means N sections written here, never N subagents. The
work list below is **re-derived from `conditional-physics-ledger-v0.258.json`
directly**, not inherited.

### 1.0 Re-derived pool

84 rows. By `(verdict, reason_kind)`: 20 `NEEDS/MISSING_CONSTRUCTION`,
17 `SAME/DERIVED`, **12 `SAME/DERIVED_CONDITIONAL`**, 9 `DIFFERS/PREDICTION`,
7 `DIFFERS/STRUCTURAL_DIFFERENCE`, **3 `SAME/DERIVED_PARTIAL`**, 3
`OVER_DETERMINED/GENUINE_FALSIFICATION`, 3 `NEEDS/REAL_PARAMETER`, 2
`NEEDS/EXTERNAL_DATUM`, 2 `OVER_DETERMINED/STALE_PREMISE`, and 6 singletons.

The **advancement pool** — rows one grant away from `SAME/DERIVED` — is the 12
`DERIVED_CONDITIONAL` plus the 3 `DERIVED_PARTIAL`, i.e. **15 rows**, and it
partitions into exactly four grant-classes:

| grant-class | rows | the named grant |
|---|---|---|
| **G-EMB** | `RA-A3`, `RA-B1`, `RA-B2`, `RA-B3`, `RA-B4`, `RA-B5` (6) | "the stabilizer / the embedding is selected" |
| **G-SHADOW** | `AC-D1`..`AC-D5` (5) | "the chiral 16 shadow is selected" |
| **G-REPLICA** | `RA-F2` (1) | action parent + physical replica cohomology |
| **G-BUILD** | `LT-GR2`, `LT-GR2b`, `LT-SM5` (3) | build a magnitude / a K77 relative index / a physical placement |

### 1.1 Lens A — comparator-routing auditor

Fork 1 of the mandatory boundary names its comparator as *"three repeated
four-dimensional chiral spin-1/2 families derived from an ordinary compact
family index, anomaly count or net chiral index."* The phrase "the **chiral**
16 shadow" is a net-chirality selection on a 4D spin-1/2 multiplet. That is the
comparator, verbatim. **Proposed route: decide the routing question first and
refuse to touch the rows until it is decided.** The auditor also fixes the
inference rule that binds the rest of this file: the boundary's mandatory
sentence is *symmetric* — a comparator result "does **not** become evidence
**for or against**" the source-native mechanism — so a *favourable* comparator
result is as barred from advancing a GU row as an adverse one is from
retreating it. This lens ranks `G-SHADOW` **last**, not first.

### 1.2 Lens B — anomaly / index theorist

Every 4D perturbative gauge anomaly coefficient is a **linear** functional of
signed multiplicities. **Proposed route: stop evaluating the channels on one
content and compute the whole solution set.** Two predictions, both pre-declared:
(i) the zero set is a *subgroup*, hence closed under chirality flip and
containing `0`, so no channel can see net chirality; (ii) with the `16`'s
hypercharges fixed, the five channels are probably **not** independent, because
`SO(10)`-completeness is a single condition wearing five hats. Both are decided
below. This lens is the one taken.

### 1.3 Lens C — source-fidelity reader

`CURRENT-STATE.yaml`, standing text: *"Weinstein's total theory remains
explicitly non-chiral; the open physics burden is low-curvature luminous/dark
chiral-looking decoupling through a nonstandard operator or owned BV/domain,
**not a net-chirality target**."* **Proposed route: check whether the grant is
something the source ever asks for.** It is not. Selecting a chiral 16 shadow
is a request the source explicitly declines to make; the source's own object is
a decoupling, not a selection. This lens issues the binding warning that
granting `G-SHADOW` would grant something the source disavows — the exact shape
of the error `gu-kills-must-name-their-target-claim` was written to prevent,
inverted.

### 1.4 Lens D — representation theorist

The `16`'s SM constituents are six irreps. **Proposed route: build the exact
`5 x 6` functional matrix and read rank, kernel, saturation and the explicit
dependency relation.** Warning attached: any rank statement is a fact about the
**arena**, not about the five channels as such, so it must be paired with an
arena-extension control or it will be over-read. That control is run.

### 1.5 Lens E — epistemics / grant-hygiene lens

"The chiral 16 shadow is selected" is not one grant, it is a **bundle**:
(i) a 14→4 reduction exists at all; (ii) it delivers complete `so(6,4)`-module
content; (iii) the SM embedding is the selected one; (iv) the surviving content
is chiral. **Proposed route: unbundle before valuing.** Immediate consequence,
visible without any computation: clause (iii) *is* the grant of `G-EMB`, which
is six other rows in the same pool at the same status. So `AC-D1..AC-D5` are
**strictly downstream of `RA-A3` and `RA-B1..RA-B5`** — they cannot advance
before those do, and they carry one extra clause on top. Clause (i) is `U4`,
which `cb-c` grades **T2** and explicitly declines to move.

### 1.6 Lens F — honesty auditor

Binding conditions, fixed **before** computing:

- (a) Any zero must be accompanied by a control that returns nonzero on the same
  machinery, or it is not reportable. Rule 5 of the charge forbids vacuously-true
  assertions, and "a vectorlike content is anomaly-free" is the canonical vacuous
  assertion in this exact area — AC-1's own Lens 4 flagged it.
- (b) The five zeros are W222's and AC-1's. Cite, never re-claim.
- (c) The channel's product is *visible, honest, small* wins. **"Five free
  upgrades" is the overclaim this route is built to produce**, and it must be
  attacked in the postflight rather than defended.
- (d) If the honest answer is zero rows, say zero rows in the first sentence.

### 1.7 Ranking, what moved, and the cheapest kill-or-switch

Ranking the four grant-classes by (routing status) x (grant is a single object
vs a bundle) x (is the grant already owned by another row):

| rank | class | why |
|---|---|---|
| 1 | **G-EMB** (6 rows) | single source-native grant, one object, upstream of everything else in the pool |
| 2 | **G-BUILD** (3 rows) | honest missing construction, no comparator, no dominance |
| 3 | **G-REPLICA** (1 row) | single grant but blocked on action parent |
| 4 | **G-SHADOW** (5 rows) | **dominated** by G-EMB *and* carries a fork-1 comparator clause on top |

> **What moved in the ranking.** `AC-D1..AC-D5` were handed to me as the top of
> the pool ("five free upgrades"). They re-rank to **last of four classes**, for
> two independent reasons that were both invisible from the row text: they are
> *dominated* (their clause (iii) is literally the grant of six other pool rows
> at the same status), and they are *routed out* (their clause (iv) is fork 1's
> comparator). `G-EMB` moves from unranked to rank 1 and is the class that
> should receive the next swing.

**Cheapest kill-or-switch, declared before computing.** One test decides the
whole route: *is the anomaly-free set closed under negation?* If yes, the
functionals are blind to net chirality, the chirality clause of the grant is
inert, and the route is a routing finding rather than an advancement — reported
as such and stopped. If no — if some channel is sensitive to the sign of the
multiplicity vector — then chirality selection is doing real work, `G-SHADOW`
is not merely a comparator import, and the route switches immediately to
computing how much work. The answer is **yes**, in the strongest possible form
(the zero set is a subgroup containing `0`).

**One credible contrary route, declared before computing.** The best chance for
the rows: if the anomaly-free lattice turned out to be exactly rank 1, spanned
by the complete `16` alone, then "complete 16s" would be **necessary** as well
as sufficient, the revival trigger would be exactly right, and the rows would
be carrying real information about which contents are admissible. This is a
live possibility — the arena control below shows that on the arena *without*
`nu^c` the lattice **is** rank 1. It is closed by direct computation, not by
appeal to a theorem.

---

## 2. THE SWING

### 2.1 The routing verdict, decided first

**Verdict: `CONVENTIONAL_COMPARATOR`. "The chiral 16 shadow" is the fork-1
comparator, not a source-native object.** Three independent grounds:

1. **Textual identity with fork 1.** The boundary's comparator is a chiral 4D
   spin-1/2 family selected by an ordinary chirality/index datum. "The chiral 16
   shadow is selected" is that sentence with `16` substituted for "family".
2. **The source disavows the selection.** `CURRENT-STATE.yaml`: the total theory
   *remains explicitly non-chiral* and the burden is a decoupling, "not a
   net-chirality target". The grant asks the source for the one thing it says it
   does not supply.
3. **The repository's own derivation runs the other way.** `cb-c` row A4
   **derives** `W = 0` for the 14D bulk rather than assuming it, and `cb-c` row
   F2 records that every block of `ker Gamma` is separately chirality-balanced,
   so *"any chiral subsector of GU's RS carrier must be a projection that does
   not respect the block decomposition."* The shadow is not lying around waiting
   to be selected; selecting it requires breaking a block structure the
   repository has computed twice by unrelated routes.

Under the boundary's mandatory rule this settles the advancement question on its
own: **granting `G-SHADOW` cannot advance these rows toward GU truth**, because
the rule is explicitly symmetric ("evidence for or against"). Everything in §2.2
is *independent additional* evidence that reaches the same place from inside the
comparator.

### 2.2 The exact computation — the 4D SM multiplicity lattice

Probe: `la3-chiral-16-shadow-grant-probe.py`, **41/41 checks, exit 0**
(26 `[E]` exact results, 15 `[C]` controls). `sympy.Rational` throughout;
no float is load-bearing.

The six SM constituents of a `16` are taken as basis directions of `Z^6` with
**signed** multiplicities (a negative entry is the conjugate irrep — standard
all-left-handed-Weyl bookkeeping, conventions validated against
`tests/one-residual/sm_mirror_anomaly_free.py` before use). The five channels
are then exact linear functionals:

```text
                     n_Q     n_u     n_d     n_L    n_e   n_nu
  D1  SU(3)^3          2      -1      -1       0      0      0
  D2  SU(2)^2 U(1)   1/4       0       0    -1/4      0      0
  D3  SU(3)^2 U(1)   1/6    -1/3     1/6       0      0      0
  D4  U(1)_Y^3      1/36    -8/9     1/9    -1/4      1      0
  D5  grav^2 U(1)      1      -2       1      -1      1      0
```

**Result 1 — the five rows are rank 4, not 5.** The system has rank exactly 4.
There is exactly one linear relation, and its support is **all five channels**,
so *any one of the five may be dropped*:

```text
   2 D1  -  27 D2  -  36 D3  -  9 D4  +  9 D5  =  0        (exact, on this arena)
```

`AC-D1..AC-D5` are therefore **four independent facts and one corollary**.
Which one is the corollary is a labelling choice, not a fact.

**Result 2 — the anomaly-free set is a rank-2 saturated lattice.**

```text
   L  =  Z . (15 of SU(5))  (+)  Z . (nu^c)
       =  { n : n_Q = n_u = n_d = n_L = n_e,  n_nu free }
```

Verified by **exhaustive integer search over `[-3,3]^6`** (117649 points): 49
anomaly-free vectors found, **0 outside `L`**.

**Result 3 — "complete 16s" is SUFFICIENT but NOT NECESSARY.** The complete
`16` is `(1,1,1,1,1,1) ∈ L`, but it spans only a **rank-1** sublattice.
`L / Z.(16)` is infinite cyclic. Explicit witness, all five channels exactly
zero: **one `15` plus seven SM singlets**, `(1,1,1,1,1,7)`, which is not an
integer multiple of the `16`.

**Result 4 — total chirality-blindness.** All five functionals are linear, so
their common zero set is a **subgroup**: it contains `0`, it is closed under
`n → -n`, and it contains every vectorlike doubling `n ⊕ (-n)`. Certified
directly: *a chiral `16` and the **empty** content return the identical anomaly
vector* `(0,0,0,0,0)`. **No SM anomaly channel can see net chirality.**

**Controls that fire (all `[C]`, each must be nonzero or the machinery is
blind).** Drop `e^c` → `D4 = D5 = -1`. Quark doublets alone → `D1 = 2`. One
`d^c` triplet alone → `D1 = -1`. One extra `u^c` on a `16` → `D3 = -1/3`. One
extra `L` → `D2 = -1/4`. Swap `n_L`/`n_e` → `D5 = -2`.

**Mutation controls.** Setting `Y(e^c) = 1/2` destroys the zero (`11/8`),
raises the rank to **5** and collapses the kernel to **dim 1**. Setting
`Y(Q) = 1/3` destroys the zero (`29/18`). So the zeros and the rank-4 relation
are properties of the *actual hypercharges*, not of the construction.

**Arena controls — the essential scoping.** On the arena `{Q,u,d,L,e}` with
`nu^c` removed, the kernel falls to **rank 1** (exactly the `15`): the
pre-declared contrary route was live and is closed by computation. Conversely,
adding **one** exotic direction (a `Y=1/2` singlet, or a `Y=-1/6` colour
triplet) restores rank **5** and destroys the relation. **The rank-4 result is
a fact about this arena, not a universal fact about the five SM channels.**

**Manifest, not claimed as a check:** the matrix above is built *only* from the
`(Y, colour, isospin)` data that `RA-A3` and `RA-B1..RA-B5` record. Given those
six rows plus completeness, `AC-D1..AC-D5` are determined. They add **no
independent information** over the embedding rows.

### 2.3 Row-by-row disposition

| row | summary | requested change | advances? |
|---|---|---|---|
| `AC-D1` | 4D `SU(3)^3` cancels | condition + trigger corrected | **NO** |
| `AC-D2` | 4D `SU(2)^2U(1)` cancels | condition + trigger corrected | **NO** |
| `AC-D3` | 4D `SU(3)^2U(1)` cancels | condition + trigger corrected | **NO** |
| `AC-D4` | 4D `U(1)_Y^3` cancels | condition + trigger corrected; flagged **dependent** | **NO** |
| `AC-D5` | 4D mixed `grav^2U(1)` cancels | condition + trigger corrected | **NO** |

**Zero rows advance.** `SAME/DERIVED_CONDITIONAL` is retained on all five, and
`mapping_grade: EXACT` is retained on all five. The grant is not discharged: the
14→4 reduction (`U4`, grade **T2**) is still required for a 4D theory to exist
at all, and the SM embedding is still required and is still `G-EMB`'s open grant.

What changes is only what the rows **say about themselves**:

1. **The condition string is wrong in two directions at once.** Its chirality
   clause is *inert* (Result 4) and its completeness clause is *strictly too
   strong* (Result 3). Proposed replacement, carrying the grant explicitly as
   the rules require rather than laundering it:
   > `none after (U4) a 14->4 reduction exists and (RA-A3, RA-B1..B5) the SM embedding is selected, and the 4D content lies in the rank-2 lattice L = Z.(15) (+) Z.(nu^c); the chirality clause of the previous string is inert and is withdrawn`
2. **The revival trigger is false as stated.** "A physical carrier not equal to
   complete 16s" does **not** revive these rows: `(1,1,1,1,1,7)` is not equal to
   complete `16`s and cancels exactly. Proposed replacement:
   > `a physical carrier whose SM multiplicity vector lies outside L, or an arena containing a hypercharge outside the 16's`
3. **The family is rank 4.** Whichever single row is designated the corollary,
   five rows are carrying four facts.

### 2.4 THE TYPED BRIDGE — specification, and why it would not help

The routing boundary's bridge burden has six items. Filled in for `G-SHADOW`:

| # | what the bridge must type | state for this grant |
|---|---|---|
| 1 | the two carriers and their real structures | **UNOWNED, and this is the sharp one.** GU side: the source-action fermion carrier on `Y^14`, a signed content vector in `Z^15` over `Omega^p(Y^14, /S)` (`cb-c`, `U1` at grade T3), on the **settled** `Cl(7,7) = M_128(R)` horn — a **real** module. Comparator side: a chiral `16`, a **complex** module. The bridge must exhibit where the complex structure comes from. Nothing in the repository supplies it. |
| 2 | the map induced by observation/reduction | **`U4`, grade T2, explicitly not moved** by `cb-c`. The bridge must give the actual 14→4 pushforward and say which `Omega^p` slots survive. |
| 3 | the action term / variational owner on both sides | **SG4**, the source action's field-space declaration — `canon/gu-forces-field-space-declaration-RESULTS.md` records it as the *unique* open decider; the fermionic action is never stabilised (draft eq 10.10, "Caveat Emptor"). The bridge must name the term that makes the 4D content chiral. |
| 4 | quotient, boundary, analytic domain | **Open by standing text.** `CURRENT-STATE.yaml`: *"a proper stabilizer-aware Koszul–Tate/ghost-for-ghost resolution and the analytic domain remain open, so no luminous/mirror physical selection follows."* |
| 5 | the observable whose value is transported | **UNSATISFIABLE.** The observable is the five-vector of anomaly coefficients. Its value is `(0,0,0,0,0)` on *every* element of `L`, including `0` and including every vectorlike content. A map that is constant on its whole domain transports no information. |
| 6 | why the comparator's failure condition pulls back | **UNSATISFIABLE.** The comparator's failure condition is `content ∉ L`. `L` is a subgroup containing `0`, so the condition never fires on the exactly-balanced bulk that `cb-c` A4 **derives** (`W = 0`) and that `PH-K1-KINEMATIC` confirms block-by-block. GU passes the comparator's test for free, and for the wrong reason. |

> **The finding, and it is stronger than "the bridge is unbuilt": for
> `AC-D1..AC-D5` a typed bridge is NOT MERELY MISSING — even once built it
> would not move these rows**, because items 5 and 6 are unsatisfiable in
> principle. The observable is constant on the entire admissible set. This is a
> route-kill on the strategy "advance the AC-D rows by building a bridge", not a
> kill on any GU claim.

**The constructive corollary, and it is the actionable output.** The mutation
controls locate exactly where the discriminating power does live: changing a
single hypercharge (`Y(e^c): 1 → 1/2`, `Y(Q): 1/6 → 1/3`) destroys the zeros and
raises the rank. **The embedding is the discriminating datum; the anomaly rows
inherit all of their content from it.** Bridge effort should therefore be routed
to `G-EMB` — `RA-A3` and `RA-B1..RA-B5` — where the transported observable
(*which irreps at which hypercharges*) is provably **not** constant on the
admissible set, and where a bridge would do real work.

---

## 3. POSTFLIGHT — specialist lenses, run inline

### 3.1 Strongest overclaim available, and why it is rejected

**"Five free upgrades."** Attacked on five independent grounds, each fatal
alone:

1. **Not five.** Rank 4. Exactly one linear relation, `2D1 - 27D2 - 36D3 - 9D4
   + 9D5 = 0`, with all five channels in its support. Any four imply the fifth.
2. **Not free.** The grant contains `U4` at grade **T2** — the entire unbuilt
   14→4 reduction. `cb-c`'s own Group-D scoping already said this in terms:
   *"the residue on this group is entirely `U4`, not the anomaly conditions."*
   Nothing here discharges `U4`.
3. **Not theirs to take.** Clause (iii) of the bundle is literally the grant of
   `RA-A3` and `RA-B1..RA-B5`. Advancing `AC-D` while those stay conditional
   would double-count one grant across eleven rows.
4. **Not upgrades.** The direction the grant *could* be cheapened (drop the
   inert chirality clause) is exactly the direction that makes the rows
   vacuous — a vectorlike content is anomaly-free for free, which is the
   canonical empty statement in this area and the thing Rule 5 forbids.
5. **Routed out.** Fork 1. A comparator result is barred from advancing a GU row
   in *either* direction.

A softer overclaim also rejected: **"the rows should be re-graded `SAME/DERIVED`
for consistency with `AC-C2`."** `AC-C2` (4D `SU(2)_L` doublet count is even) is
already `SAME/DERIVED` on the near-identical grant *"none after the 16 is
observed"*. That is a real inconsistency inside the ledger's own
`ANOMALY_CONSISTENCY` axis and it is **flagged, not exploited** — arguing for
advancement from an inconsistent precedent is laundering. Under the routing
boundary the consistent resolution runs the *other* way (`AC-C2`'s grant is also
a fork-1 import), but `AC-C2` is not my row and I request no change to it. It is
filed as a conflict key.

### 3.2 Strongest contrary reading

**"You have proved the rows are cheap, not that they are blocked. `L` is bigger
than the `16`; GU's content is in `L`; so the rows are satisfied under a
*weaker* grant than recorded, which is an advance."**

This is the best argument against the finding and it is half right. The grant
*is* weaker than recorded — that is Result 3, and it is one of the three
corrections filed. What it misses is that the weakening moves in the wrong
direction for the ledger's purpose. `L` is a **subgroup**, so weakening the
grant to "content ∈ `L`" admits the empty content and every vectorlike content.
The rows become cheaper and simultaneously stop saying anything: the price of
the weaker grant is exactly the row's discriminating content, which AC-1 had
already measured to be zero by a different route (the fork→anomaly map is
constant). A row that is easier to satisfy *because* its condition admits
everything has not advanced.

A second contrary reading, weaker but worth recording: **"the arena is too
small — GU's actual content includes the `144`, whose SM decomposition has
exotic charges outside `Z^6`."** Correct, and conceded as a scope ceiling
(§3.4). It does not rescue the rows: HE-1 established the `144` is a **mirror**
of multiplicity one whose contribution is *subtractive*, and AC-1 computed
`d^abc = 0` and `Tr T^a = 0` on `10 (x) 16 = 144 (+) 16` directly, so the larger
arena is anomaly-free too — by the same group-theoretic mechanism, with the same
zero discriminating power.

### 3.3 Weakest seam

**Propagation, not reproduction.** The probe is deterministic, exact,
exhaustively searched, controlled and mutation-tested. The seam is that
"`L` is bigger than the `16`" is one compression away from *"GU's anomaly
conditions are easier to satisfy than we thought"*, which would be a frame
regression across the routing boundary in the favourable direction. The
operative sentence that must travel with the result:

> `L` is a **subgroup**. It contains `0`. Being in `L` is not an achievement —
> the empty content is in `L`, and so is every vectorlike content. The rank-2
> lattice is a statement about how little the five channels constrain, not about
> how much GU satisfies.

A second, narrower seam: the rank-4 relation is **arena-relative**. It holds on
the `16`'s own six SM constituents and dies the moment one exotic hypercharge is
added (both arena-extension controls). Any relay that states "the five SM
anomaly conditions are rank 4" without the arena qualifier is wrong.

### 3.4 Ceilings, stated plainly

- **Arena.** `Z^6` over the `16`'s own SM constituents. The `144`'s exotic
  charges (`±4/3`, `±5/3`, `±2`, per HE-1 / draft §14.3) lie outside it. Results
  1–3 are arena-scoped; Result 4 (linearity ⇒ subgroup ⇒ chirality-blindness) is
  not, since it follows from linearity alone.
- **Complex reps, one real form unaddressed.** All computation is on complex SM
  charge data. The `Cl(7,7)`/`Cl(9,5)` real-form fork is untouched, and it is
  precisely bridge item 1.
- **No count.** No number here is a generation count. `n_g` never appears.
- **Nothing 14D.** Not a statement about `I_16`, Dai–Freed, bordism, or the
  14D local system. Those are owned elsewhere and are consumed, not moved.
- **Not a GU kill.** No GU source claim is targeted. The object adjudicated is a
  ledger condition string.

---

## 4. THE VERSIONLESS DELTA

Against base revision **`a148ed80`**. Emitted, not applied: this artifact edits
no ledger, no `CURRENT-STATE.yaml`, no `NEXT-STEPS.md`, no canon. The JSON
below conforms to `lab/process/conditional-evidence-deltas/delta.schema.json`
and is for the canonical owner to file — I am not permitted to write to
`lab/process/`.

```json
{
  "schema_version": "1.0",
  "delta_id": "LA3-CHIRAL-16-SHADOW-COMPARATOR-2026-08-15",
  "status": "pending",
  "base": {
    "ledger_ref": "lab/process/conditional-physics-ledger-v0.258.json",
    "ledger_sha256": "540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047"
  },
  "affected_rows": ["AC-D1", "AC-D2", "AC-D3", "AC-D4", "AC-D5"],
  "result_refs": [
    "lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md",
    "lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-grant-probe.py",
    "lab/methods/source-native-comparator-routing.md",
    "lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md",
    "lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md",
    "explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md"
  ],
  "source_disposition": "The source is not asked for anything and gives nothing up. CURRENT-STATE.yaml's standing text records that Weinstein's total theory remains explicitly non-chiral and that the burden is a low-curvature luminous/dark decoupling, NOT a net-chirality target. The condition 'the chiral 16 shadow is selected' is therefore the fork-1 conventional comparator of lab/methods/source-native-comparator-routing.md, not a source-native object, and under that boundary's symmetric rule it cannot advance a GU row in either direction.",
  "claim_ceiling": "Exact rational linear algebra on the 5x6 SM anomaly functional matrix over the signed multiplicity lattice Z^6 of the 16's own SM constituents, plus exhaustive integer search over [-3,3]^6, with live controls, two hypercharge mutations, one arena control and two arena-extension controls. 41/41, exit 0. NOT a 14D statement, NOT a claim about the unbuilt 14->4 reduction, NOT a generation count, NOT a chirality-production claim, NOT a real-form statement, NOT a source-native result, and NOT a verdict, canon, count, posture or mapping-grade movement. The five zeros themselves are owned by W222 and AC-1 and are cited, not re-claimed.",
  "proposed_effect": {
    "summary": "ZERO ROWS ADVANCE, and that is the finding. AC-D1..AC-D5 retain SAME / DERIVED_CONDITIONAL and mapping_grade EXACT. Three corrections are proposed to what the rows say about themselves, all of which make the family smaller and more honest rather than larger: (1) the condition string's chirality clause is EXACTLY INERT, because the five anomaly channels are linear functionals whose common zero set is a subgroup - closed under chirality flip, containing 0, and giving a chiral 16 and the EMPTY content the identical anomaly vector; (2) the condition string's completeness clause is STRICTLY TOO STRONG, because the anomaly-free set is the rank-2 saturated lattice L = Z.(15 of SU(5)) (+) Z.(nu^c), of which the complete 16 spans only a rank-1 sublattice, with explicit witness (1,1,1,1,1,7); hence the recorded revival trigger 'a physical carrier not equal to complete 16s' is FALSE AS STATED and must become 'outside L'; (3) the five rows are RANK 4, not 5, via the exact arena-relative relation 2 D1 - 27 D2 - 36 D3 - 9 D4 + 9 D5 = 0 whose support is all five channels, so the family carries four independent facts and one corollary. The grant is not discharged: U4 (grade T2) is still required, and clause (iii) of the grant IS the open grant of RA-A3 and RA-B1..RA-B5, so AC-D1..AC-D5 are strictly downstream of six other DERIVED_CONDITIONAL rows in the same pool. The typed bridge is specified against all six items of the routing boundary's bridge burden, and items 5 and 6 are shown UNSATISFIABLE: the transported observable is constant on the entire admissible set, so a bridge would not move these rows even once built. Discriminating power is located upstream in the embedding, by hypercharge mutation.",
    "requested_row_changes": [
      "AC-D1..AC-D5 distance only: replace 'none after the chiral 16 shadow is selected' with 'none after (U4) a 14->4 reduction exists and (RA-A3, RA-B1..B5) the SM embedding is selected, and the 4D content lies in the rank-2 lattice L = Z.(15) (+) Z.(nu^c); the chirality clause is inert and is withdrawn'. Verdict SAME, reason_kind DERIVED_CONDITIONAL and mapping_grade EXACT are all PRESERVED unchanged.",
      "AC-D1..AC-D5 revival_trigger only: replace 'a physical carrier not equal to complete 16s' with 'a physical carrier whose SM multiplicity vector lies outside L = Z.(15) (+) Z.(nu^c), or an arena containing a hypercharge outside the 16's' - the recorded trigger is false as stated, with explicit counterexample (1,1,1,1,1,7).",
      "AC-D4 note only: flag as the dependent channel of the rank-4 family, or designate another member of the relation's support; five rows carry four independent facts.",
      "AC-D1..AC-D5 evidence only: add this artifact and its probe alongside cb-c-anomaly-conditions-2026-08-05.md:D1..D5.",
      "NO verdict change, NO reason_kind change, NO mapping_grade change, NO count change, NO canon or CURRENT-STATE or NEXT-STEPS effect. Zero rows advance."
    ]
  },
  "conflict_keys": [
    "AC-D1", "AC-D2", "AC-D3", "AC-D4", "AC-D5",
    "AC-C2",
    "RA-A3", "RA-B1", "RA-B2", "RA-B3", "RA-B4", "RA-B5",
    "U4-REDUCTION-AND-CHIRALITY-PRODUCTION",
    "CHIRAL-16-SHADOW-GRANT",
    "SOURCE-NATIVE-COMPARATOR-ROUTING-FORK-1"
  ],
  "integration": null
}
```

**Flagged for the integrator, not requested:** `AC-C2` ("4D `SU(2)_L` doublet
count is even") is graded `SAME/DERIVED` on the near-identical grant *"none
after the 16 is observed"*, while `AC-D1..AC-D5` are `DERIVED_CONDITIONAL` on
*"none after the chiral 16 shadow is selected"*. One of these gradings is wrong.
Under the routing boundary the consistent resolution is that both grants are
fork-1 imports and both rows should carry the condition. `AC-C2` is outside my
scope and no change to it is requested; it is listed as a conflict key so the
inconsistency is not integrated blind.
