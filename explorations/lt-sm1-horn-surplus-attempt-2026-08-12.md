---
artifact_type: exploration
doc_type: construction_result
status: exploration
created: 2026-08-12
brief_version: "1.3"
target_claim: SC-ACT-04
ledger_row: LT-SM1
repo_head_pinned_for_reading: 0b2b0453a0afb831cbcb70f70352f65b120043b8
repo_head_at_probe_run: f078fcbb66ff9d99b933022c28852eb7fcf65c96  # hourly automation advanced HEAD mid-run
head_advance_impact: "LT-SM1 byte-identical in v0.216 and the new v0.231; ledger residue unchanged; NEXT-STEPS.md line numbers shifted +14, so all probe anchors were converted from line numbers to markers"
repo_access: READ-ONLY (hourly automation owns the conditional-build ledgers; nothing written into the repo)
work_item: LT-SM1-CONSTRAINT-SURPLUS-ATTEMPT
probe: lt_sm1_surplus_probe.py (co-located; exit 0, both planted controls pass)
title: "LT-SM1 surplus attempt: the horns ARE finitely enumerable (zeta_F in {0,1}), so the row is not mistyped at step 1 -- but the surplus is UNCOMPUTABLE. Exactly ONE of ten candidate constraints is both expressible and discriminating, and it is weak; and the free-parameter count of the fundamental horn is not agreed inside the repo (packet charges g_A^{-2} independently at 7.2; W229's own title says Z_U sets g_A). Both sides of the subtraction are unresolved, so no horn earns a positive surplus. The planted permissive control inflates expressibility 4/10 -> 10/10 and a naive written-parameters-only matcher selects the UNBUILT horn, which is the B5 failure mode in its dual form."
grade: "EXACT for the enumeration (|H| = 2, verified against packet:498 and the ledger's own residue.open_discrete_forks) and for the expressibility computation (mechanical, planted-tested, reproducible). The discrimination column is a DECLARED READING of quoted artifact statuses, not a computation, and is graded SCOPED throughout. No row is closed, no claim moves, no coefficient is derived."
construction: "program-native throughout per GEOMETER-VS-PHYSICS-OBJECTS.md; the one imported object is the Sakharov/Jacobson induced-kinetic-term stance, which is named as PORTED where it appears and is shown below to be a HOMONYM of the zeta_F fork rather than a resolution of it."
kill_conditions_declared_before_computation: true
canon_verdict_change: none
priority_change: none
outcome: "SURPLUS-UNCOMPUTABLE (verdict c), with a secondary TYPING observation (partial d)"
binds: nothing
---

# LT-SM1: does constraint surplus fix the `zeta_F` horn?

**Disposition for the wave: this is evidence, not a ledger edit.** Nothing here
is written into `gu-formalization`. The row's disposition is the wave's.

**HEAD advanced mid-run.** Reading began at `0b2b045`; the hourly automation
committed `f078fcb` ("Classify source-natural I2B primalizer") while this ran,
touching `NEXT-STEPS.md`, `lab/process/CURRENT-RESEARCH-CONTEXT.md` and adding ledger
**v0.231**. Impact checked, not assumed:

- `LT-SM1` is **byte-identical** in `v0.216` and `v0.231` (all nine fields).
- `v0.231` still has **1** `FINITE_CHOICE` row and **0** `ONE_BIT` rows across 84 rows.
- `residue.open_discrete_forks = 9`, `open_fork_horn_product = 1152`,
  `quotients_ranked = 5` — all unchanged, so the section 6 "N5 has not run"
  reading survives the new ledger.
- `NEXT-STEPS.md` line numbers shifted **+14**. Every probe anchor was therefore
  converted from a line number to a **content marker**, and the probe aborts
  loudly (`ANCHOR NOT FOUND ... probe VOID`) rather than silently reading the
  wrong window if a marker ever moves. Citations below are given at `f078fcb`.

---

## 0. Structure-first prediction, recorded BEFORE computing

Per brief item 15. Written before the constraint enumeration was run, from three
facts already in hand at that point: `packet:1120` states *"No constraint surplus
is reported at N1"*; the B5 audit returned `SURPLUS-UNCOMPUTABLE` on a
structurally similar question; and `AGENTS.md:44` (P-H29) disqualifies the one
result that looked like it killed a horn.

| # | prediction | outcome |
|---|---|---|
| **P1** | The constraint side comes out at or near **zero**. The repo has not built the objects a YM-sector constraint would need. | **AGREEMENT.** 4/10 expressible at the probe's default window, but only **1** discriminating, and that one is weak. |
| **P2** | A naive matcher will **reward the unbuilt horn**, because a term that is not written has no written parameters. | **AGREEMENT, and sharper than predicted.** The naive matcher picks `zeta_F=0` (surplus `0` vs `-1`). |
| **P3** | Verdict **(c) SURPLUS-UNCOMPUTABLE**. | **AGREEMENT.** |
| **P4** | *(implicit in P2)* The single real constraint, if one exists, would also point at the unbuilt horn. | **SURPRISE — polarity inverted.** The one discriminating constraint (`C5`, SM-6's Higgs mechanism) points at `zeta_F = 1`, i.e. the **opposite** direction from the naive matcher's bias. |

**The P1/P2/P3 match is a certificate**; the P4 inversion is the run's one
genuine surprise and is the thing a wave should look at first. A matcher bias and
the only real constraint pointing in opposite directions is exactly the
configuration in which reading the raw number would have produced a confident
wrong answer.

---

## 1. Five-lens pre-flight (run INLINE)

### Lens 1 — gauge / Yang-Mills field theory. Basis: DIRECT. Confidence: high.

The object is `(zeta_F / 2 g_A^2) \int_Y kappa_g(F_A, *_G F_A)` at
`unified-source-datum-packet-v0-2026-07-30.md:470`, with
`zeta_F \in {0,1}` declared at `:498`. Field-theoretically the two horns are not
symmetric and the asymmetry is the whole problem:

- `zeta_F = 1` writes a **tree-level** coupling. Its coefficient `g_A^{-2}` is a
  free normalization at the scale where the action is written.
- `zeta_F = 0` asserts the term is **generated**. A generated `1/g^2` is a
  regulator-dependent loop coefficient (this is the Sakharov mechanism the repo
  ports elsewhere). It is not free — it is *determined by the regulator*, which
  is a different object that must itself be supplied.

**The lens's binding contribution:** counting "written parameters" treats the
generated coefficient as costing nothing. It does not. It relocates the cost into
the regulator sector, and `packet:858` records that **"No regulator is called
admissible on the noncompact Krein problem"**. So `zeta_F = 0` does not have zero
parameters; it has an undefined number of them, with the object that would define
them recorded as non-existent.

### Lens 2 — variational / action structure. Basis: DIRECT. Confidence: high.

`W229`'s parent action (`W229-close-a2-source-action-znu-completion-2026-07-14.md:55-62`)
is displayed **without** an `F_A^2` term, yet its `E_A` field equation at `:81`
reads

```
g_A^{-2} D_A* F_A - c_theta theta + J_IG + J_cross + J_Psi + J_section = 0
```

The `g_A^{-2} D_A* F_A` leg can only come from varying a written `F_A^2` term.
**`W229` is silently on the `zeta_F = 1` horn** while calling its own route "the
induced-Yang-Mills route." The text bridges this with "plus the Yang-Mills
variation" at `:79` — an added term, undeclared in the displayed parent.

This is not a nitpick. It is exactly the AGENTS.md discipline item 3 failure
("every undeclared choice silently consumes surplus"), occurring inside the
artifact that a wave would most likely cite as having already settled the horn.

### Lens 3 — source criticism. Basis: DIRECT. Confidence: high.

Target claim **`SC-ACT-04`** (`lab/sources/source-claim-register.yaml:653-668`),
polarity ASSERTS, adherence ADHERED:

> *A second-order Lagrangian `I^B_2 = ||Upsilon^B_omega||^2` yields a
> Yang-Mills-Maxwell-like equation with bosonic source, more efficiently written
> as `D*_omega Upsilon_omega = 0`.* (draft-2021 p.45, eq (9.14))

The source's Yang-Mills object is the **second layer**, a norm square of the
first-layer Euler residual. `gu-two-layer-action-source-reinspection-2026-08-04.md`
enumerates **three** honest second-layer readings (bosonic residual norm; total
residual norm; Dirac-square/path adapter) and grades the released wording as
*"'replacement,' 'generalizing,' and 'looks like,' not an identity with the
observed Standard Model action."*

**The packet's binary is posed on an object with no layer typing.** Grepping
`unified-source-datum-packet-v0-2026-07-30.md` for `layer` / `first-layer` /
`second-layer` / `two-layer` returns **zero hits** (verified). So the horn set
`{0,1}` is well-defined *on the packet* and under-resolved *against the source*.

**FRAME-SENSITIVE.** "Select the `zeta_F` horn" compresses to "pick 0 or 1."
That compression misleads: the source's own architecture is a trichotomy that the
packet's bit does not carry, and the reinspection has already ruled that the
reading which *could* select a coefficient (the Dirac-square/path adapter) has
neither of its two required objects built.

### Lens 4 — Layer-0 semantics. Basis: DIRECT. Confidence: high. **This lens changes the answer.**

The brief flagged "Yang-Mills," "kinetic term" and "normalization" as homonym
risks. All three bite, and one bite is decisive.

| phrase | sense A | sense B | the bite |
|---|---|---|---|
| **"induced Yang-Mills"** | `zeta_F = 0`: the `F_A^2` term is **not a written summand** of the source action (`packet:498`; `cb-b:636-639`) | `W180`/`W203`/`W229`/`W236`/`W182`: the connection **distortion** `theta` has no fundamental kinetic term, so `theta` becomes a functional of the record current and its kernel is promoted from algebraic to the differential operator `D_A* D_A` — "induced-YM" names the *shape of theta's kernel* (PORTED Sakharov/Jacobson) | **Different fields.** Sense A is about `A`; sense B is about `theta = A - Gamma(eps_IG) - U`. A wave reading the five-artifact W-stack as evidence that GU has already chosen `zeta_F = 0` would be wrong — and `W229`'s `E_A` (Lens 2) shows that stack actually standing on `zeta_F = 1`. |
| **"kinetic term"** | the YM term `kappa_g(F_A, *_G F_A)` (`U2` gates it) | the gradient term `\|D_A U\|^2` with stiffness `Z_U` (`U4`; itself already flagged as a homonym in `NAMES.md`-adjacent form at `cb-b:189`) | `Z_U` is charged separately from `g_A^{-2}` in `packet:1106`, so these are two coefficients, not one |
| **"normalization"** | `g_A^{-2}`, this row's coefficient | the rank-3 normalization group `{kappa, Z_U, source_norm}` of `PRED-NORM-RANK` (`U5`) | `cb-b:604-616` records the *unrun* question of whether DC-H2's length-squared is the same object as `ell^2 = Z_U kappa`; until it runs, "the imported-scale count" is 1 or at least 2 and the ledger "cannot honestly state how many independent scales GU must import" |

**Recommended `NAMES.md` row (for the wave, not written by me):**
`"induced Yang-Mills"` — sense 1: the `zeta_F=0` horn (is the `F_A^2` term
written?); sense 2: the Sakharov stance on `theta`'s kernel (`D_A*D_A` vs
algebraic). Bite: five W-artifacts carry sense 2 and one of them (`W229:81`)
silently assumes sense-1 **`zeta_F = 1`** in its `E_A` equation.

### Lens 5 — adversarial refutation. Basis: PRINCIPLE. Confidence: high.

Three attacks on my own result, run before reporting it.

1. *"You found a discriminating constraint (`C5`), so declare `zeta_F = 1`."*
   **Refused.** `C5` is `cb-b`'s own typing of SM-6 as "DETERMINED GIVEN `U2`
   (that the Yang-Mills term is fundamental)" (`cb-b:939`). But the mechanism it
   depends on is the expansion `||F_A||^2 = ||d_{A_0}a||^2 + 2<F_{A_0},a^a> +
   ||a^a||^2` (`cb-b:929-935`), and **that expansion is a property of the
   symbol, not of its provenance** — an *induced* `||F_A||^2` expands the same
   way. So `C5` discriminates only in the weak sense that the packet's N1 action
   *supplies* the expandable term today only under `zeta_F=1`. That is a
   statement about what is written, not about what is true. Graded SCOPED.
2. *"`FUNDAMENTAL-YM-W177-VERTICAL-RESPONSE-KILLED` (`NEXT-STEPS.md:4228` at `f078fcb`) kills
   `zeta_F = 1`. Declare `zeta_F = 0`."*
   **Disqualified, by the repo's own rule.** `AGENTS.md:44` (register `P-H29`):
   *"a null or kill verdict read from finite-difference numerics is not citable
   until certified with exact/analytic derivatives."* `CURRENT-STATE.yaml:64`
   lists recertification of exactly the RB6/RB7/W177 nulls as still open, and
   `CURRENT-STATE.yaml:69-70` says outright that RB7's *"published numbers are
   FD-band reads and are not citable."* The brief independently forbids it.
   **This is the single most load-bearing exclusion in the run**: without P-H29
   the horn would look decided against `zeta_F=1`, and it is not.
3. *"Your `C5` and your `C4` point opposite ways, so just take the stronger."*
   **Refused.** `C4` is disqualified (not weak — *inadmissible*), so there is no
   contest to adjudicate. Reporting a 1-vs-1 tie would smuggle an inadmissible
   number back in.

**Kill claim status: NONE-NOT-A-KILL.** No claim ID in
`lab/sources/source-claim-register.yaml` is falsified by this run. `SC-ACT-04` is
the target and it stands ADHERED; this investigation narrows what can be *inferred* from it,
which is not a kill.

---

## 2. Anti-redo (brief item 5), run before any derivation

`python3 lab/process/novelty-check.py "zeta_F horn selection" "induced Yang-Mills" "fundamental versus induced" "gauge kinetic surplus" "LT-SM1"` -> **exit 1, 1138 prior hits.** Near hits were read, not just counted:

| prior art | what it already owns | why this investigation is not a redo |
|---|---|---|
| `explorations/b5-constraint-surplus-audit-2026-07-29.md` | the surplus method, the distinctive-object proxy, the planted-control discipline, the `SURPLUS-UNCOMPUTABLE` outcome type | it audits the **B5 phase residual**, a different object; LT-SM1 was never its subject |
| `W180`, `W203`, `W229`, `W230`, `W236`, `W182`, `W161`, `W167` | the Sakharov induced-kinetic-term stance, ported and named | Lens 4: these are **sense B** of "induced Yang-Mills" and do not select `zeta_F` |
| `cb-b-lagrangian-terms-2026-08-05.md:207, 627-670` | the `U2` fork declaration and the SM-1 row | declares the fork; does **not** count constraints or parameters against it |
| `explorations/rung1-finite-coefficient-enumeration-2026-07-29.md` | finite-coefficient enumeration method | different coefficient family |
| `explorations/rb7-...-2026-07-30.md`, `NEXT-STEPS.md:4140-4218` | the `zeta_F=1` / `zeta_F=0` branch instructions and the W177 response | branch *instructions*, unexecuted for `zeta_F=0` ("Test `zeta_F=0` separately", step 3, `NEXT-STEPS.md:4213` at `f078fcb`; was `:4199` at `0b2b045`) |

Mechanism-word searches (not just proper nouns) run: `induced gauge`, `fermion
determinant`, `Sakharov`, `norm square`, `second layer`, `regulator`,
`branching dictionary`. **`grep -rn "LT-SM1"` outside the ledger JSONs returns
exactly 3 hits**, all of them scaffold/crosswalk mentions
(`post-donor-crosswalk-five-wave-scaffold-2026-08-05.md:89`,
`cross-theory-mechanism-donor-crosswalk-2026-08-05.md:73`,
`lab/process/hostile-reviews/2026-08-05-cross-theory-mechanism-donor-crosswalk-review.md:18`),
none of which computes a surplus. **No prior art on this row's surplus.**

---

## 3. Horn identification

### 3.1 The horns, exactly

**CONFIRMED** (verified against files):

| horn | statement | citation |
|---|---|---|
| **H1** | `zeta_F = 1` — Yang-Mills is **fundamental**: `(1/2 g_A^2) \int_Y kappa_g(F_A, *_G F_A)` is a written summand of the N1 ambient bulk action `S_Y^{(0)}` | `packet:470, 498`; `cb-b:627, 636-637` |
| **H2** | `zeta_F = 0` — Yang-Mills is **induced**: "the gauge kinetic term is not a written term at all but a consequence of the fermion determinant and the `\|II\|^2` sector" | `cb-b:637-639`, citing `packet:498` |

**`|H| = 2`. The set IS finitely enumerable from the record**, so the step-1 stop
condition does **not** fire and this investigation proceeds. Two independent corroborations:

- `packet:1117` charges a `discrete forks` category listing `YM` by name.
- The ledger's own `residue` block records `open_discrete_forks: 9` with
  `open_fork_horn_product: 1152 = 2^7 * 3^2` — consistent with the YM fork being
  one of seven binary forks. **COMPUTED**: `1152 = 2^7 * 3^2` exactly.

### 3.2 Two scope fences on the enumeration

**SCOPED.** `cb-b:637-639`'s gloss of H2 ("fermion determinant and the `|II|^2`
sector") is **cb-b's interpretation**. The packet at `:498` says only
*"`\zeta_F\in\{0,1\}` carries the fundamental-versus-induced Yang--Mills fork"*
and nothing more (verified: `grep -n -i induced` on the packet returns 6 hits,
none of which elaborates the H2 mechanism). So H2's *content* is one artifact
deep, not source-anchored.

**SCOPED, and this is the sharper fence.** The source's own architecture
(`SC-ACT-04`) is a **two-layer** construction in which the YM-like equation comes
from `I^B_2 = ||Upsilon^B_omega||^2`. That is neither "written with a free
`g_A^{-2}`" nor "loop-induced from the fermion determinant" — it is a third
reading, and `gu-two-layer-action-source-reinspection-2026-08-04.md:57-70`
enumerates it as one of three. The packet's binary is posed on an object carrying
**no layer typing at all** (grep-verified, zero hits). A wave that "selects the
horn" therefore selects within the packet's frame, not within the source's.

---

## 4. Per-horn surplus

Probe: `lt_sm1_surplus_probe.py` (co-located, exit `0`). Exact arithmetic only
(`int` / `fractions.Fraction`); no float appears anywhere in the computation.

### 4.1 Free parameters, DECLARED BEFORE the subtraction (AGENTS.md discipline item 3)

| horn | reading | free parameters introduced | citation |
|---|---|---|---|
| H1 | **packet** | **1** — `g_A^{-2}`, charged in the 7.2 parameter ledger under `local action coefficients` | `packet:1106` |
| H1 | **W229** | **0** — `Z_U` "sets the induced YM coupling `g_A`"; "the COMPLETE action carries exactly TWO normalization scales `{kappa, Z_U}`" | `W229:9` (frontmatter title), `:158` |
| H2 | **written only** | **0** — the term is absent, so it writes no coefficient | `packet:498` by construction |
| H2 | **+ undeclared** | **>= 1** — the induction that must produce the term imports a regulator; `packet:1115` charges two regulator families, and `packet:858` records **"No regulator is called admissible on the noncompact Krein problem"** | `packet:851-858, 1115` |

**CONFIRMED, and it is the run's second finding: the repo does not agree with
itself on H1's parameter count.** `packet:1106` charges `g_A^{-2}` as an
independent local action coefficient; `packet:1118` lists exactly two things as
"derived, not independently charged" (`m_R` and `ell^2 = Z_U kappa`) and
`g_A^{-2}` is **not** among them. `W229`'s own title says `Z_U` sets `g_A`. These
cannot both be right. This is a `VERIFIED_REPO_DISCONNECT` of the same shape
DC-H2 reported between `W230`'s text and `W203`'s `KER4`
(`dc-h2:9`, frontmatter).

### 4.2 Constraint side: ten candidates, mechanically tested

Expressibility uses the B5-tightened distinctive-object proxy (length `>= 3`, or
colon-qualified slot name). "Discriminating" means the constraint distinguishes
`zeta_F=1` from `zeta_F=0` rather than being satisfied or failed identically by
both — a constraint both horns fail is not a constraint *on the choice*.

| id | candidate constraint | expressible | discriminating | recorded status |
|---|---|---|---|---|
| `C1` | three SM couplings from branching one `g_A` | EXPR | no | **UNBUILT** (`M-M4`; `improvement-register:177` "Build after J2"; `cb-b:684` "the row `M-M4` would move") |
| `C2` | perturbative anomaly cancellation (SM-9) | OUT | no | **FORK-STRANDED** on `SIGNATURE-AMBIENT` (`cb-b:85`) |
| `C3` | a massless photon in the spectrum | EXPR | no | `OPEN_PHOTON_KERNEL` — "no massless-photon kernel exists" (`cb-b:665-666`); **fails under both horns** |
| `C4` | fundamental-YM slice stationarity | EXPR | **DISQUALIFIED** | `FUNDAMENTAL-YM-W177-VERTICAL-RESPONSE-KILLED` (`NEXT-STEPS:4228`) — **not citable, P-H29** (`AGENTS.md:44`; `LANE-STATE:64, 69-70`) |
| `C5` | SM-6 Higgs mechanism needs `\|\|F_A\|\|^2` to expand | EXPR | **YES (weak)** | "DETERMINED GIVEN `U2` (that the Yang-Mills term is fundamental)" (`cb-b:939`) |
| `C6` | Schur/equivariance forcing of relative coefficients | OUT | no | forces the `theta`/`eta` **ultralocal kernel**, a different sector (`W203:196-209`) |
| `C7` | DC-H2 congruence-orbit exclusion | OUT | no | a **negative** result: deletes candidate selectors, is not one (`dc-h2:229-236`) |
| `C8` | "the second-layer norm square selects the coefficient" | OUT | no | **DEAD ON ARRIVAL** — "does not become an independent coefficient constraint merely by being second order" (`reinspection:51-55`; `cb-b:192`) |
| `C9` | `A`- and `U`-equations must select the same orbit | EXPR | no | **UNBUILT** (`NEXT-STEPS:4215-4218`, listed as a future step) |
| `C10` | source fidelity `SC-ACT-04` | EXPR | no | ADHERED, but the source's architecture is the **third** reading; under-resolved on `{0,1}` |

**COMPUTED:** expressible strict **4 / 10** at the probe's default read window;
discriminating and expressible **1 / 10**; disqualified by P-H29 **1**.

**Window-sensitivity certificate (COMPUTED).** The *expressible* count is an
artifact of how much surrounding prose the anchor reads; the *discriminating*
count is not:

| read window (lines before/after marker) | expressible | discriminating |
|---|---|---|
| `-0 / +0` | 1 / 10 | 0 / 10 |
| `-2 / +6` | 4 / 10 | **1 / 10** |
| `-4 / +12` (default) | 4 / 10 | **1 / 10** |
| `-8 / +24` | 6 / 10 | **1 / 10** |
| `-20 / +60` | 8 / 10 | **1 / 10** |

Expressibility swings 1 to 8; **discrimination is invariant at 1 across every
non-degenerate window**, and discrimination is the only column the surplus
consumes. The surplus table below is therefore window-independent.

### 4.3 The surplus table

| horn | reading | independent expressible constraints | free parameters | **surplus** |
|---|---|---|---|---|
| **H1** `zeta_F = 1` | packet parameter count | 1 | 1 | **0** |
| **H1** `zeta_F = 1` | W229 parameter count | 1 | 0 | **+1** |
| **H2** `zeta_F = 0` | written parameters only | 0 | 0 | **0** |
| **H2** `zeta_F = 0` | + undeclared regulator | 0 | >= 1 | **<= -1** |

All four values exact integers. **No horn has a positive surplus under an agreed
parameter count.** The only `+1` in the table sits on the W229 reading, which is
the reading that contradicts `packet:1106` — so it is not available.

### 4.4 Independence ranking (AGENTS.md discipline item 2: "the usually-illusory part")

The one constraint I counted is `C5`. Is it independent of anything else counted?
Trivially yes — it is the only one. The live risk runs the other way: are any of
the nine I *rejected* secretly the same constraint, which would mean I over-counted
the rejection side? Ranked:

- `C1` and `C10` both reduce to "the reduction `Y^14 -> X^4` is unbuilt." **One
  constraint, not two.** Rejecting both costs nothing since neither counted.
- `C6`, `C7`, `C8` are three faces of one theorem-shaped fact: **scale-blind
  conditions cannot supply a scale.** `C7` (DC-H2) states it as a theorem, `C8`
  (the "square" homonym) as its instance for norm squares, `C6` (Schur) as the
  positive residue it leaves. Counting them as three independent exclusions would
  have inflated the *rejection* side threefold. Counted as **one**.
- `C3` and `C9` are both "the vacuum/orbit structure is unbuilt." **One.**
- `C2` is genuinely separate (a different fork's stranding).
- `C4` is genuinely separate and is disqualified rather than rejected.

**Independence-collapsed rejection count: 5 distinct reasons, not 9.** This does
not change the surplus (rejected constraints contribute 0 either way) but it does
change the *reopener*: there are five things to fix, not nine, and two of them
(`C1`/`C10`'s reduction, `C3`/`C9`'s vacuum) are the same unbuilt object family.

---

## 5. Controls

### 5.1 Planted controls (mandatory, run before any number was read)

| control | expectation | result |
|---|---|---|
| `N1` a planted constraint that genuinely cites `zeta_F`/`g_A^{-2}`/`F_A`/`packet:498` | classifies EXPRESSIBLE | **PASS** |
| `N2` a planted unrelated constraint (mapping-torus orientation cocycle / KO twist) | classifies OUTSIDE | **PASS** |

Both fire correctly, so the investigation is not void. (B5's first execution failed `N2`
and was voided; that precedent is why these run first.)

### 5.2 The deliberately permissive control (brief item 3)

Re-run with a matcher that admits bare single-character identifiers (`F`, `A`,
`g`, `U`, `Y`, `S`, `2`) — reproducing precisely the failure that voided B5's
first run:

- expressible **4 / 10 -> 10 / 10** (inflation `+6`);
- the planted **unrelated** row `N2` also classifies **EXPRESSIBLE**.

**The control returns: the permissive matcher classifies everything, including
the plant it must reject.** So the strict `6/10` is not an artifact of a stingy
matcher — it is what survives a matcher that is demonstrably capable of
over-firing. **My surplus matcher is not inflating.**

### 5.3 The naive-matcher control (added; not requested, and it is the one that matters)

A matcher that counts only *written* parameters and skips expressibility entirely
returns `H1 = -1`, `H2 = 0` and **selects `zeta_F = 0`, the horn whose supporting
construction does not exist.**

This is the B5 inflation lesson in its **dual** form, and it is worth stating as a
transferable rule:

> A permissive matcher inflates the constraint side. An **absent term** deflates
> the parameter side. Both make a surplus look better than it is, and the second
> systematically favours whichever horn is *less built*.

Against this, note polarity: the one genuinely discriminating constraint (`C5`)
points at `zeta_F = 1`. **The bias and the evidence point opposite ways.**

---

## 6. Verdict

### **(c) SURPLUS-UNCOMPUTABLE.** Grade: CONFIRMED for the computation; SCOPED for the discrimination reading.

Not (a): no horn has positive surplus under an agreed parameter count.
Not (b): "multiple horns survive" would overstate it — it is not that both horns
pass a test, it is that there is essentially no test.
Not (d) as the primary verdict: the horns **are** finitely enumerable
(`|H| = 2`), so the row is not mistyped in the way that would have stopped this
run at step 1.

**Both sides of the subtraction are unresolved:**

1. **Constraint side.** Exactly **1 of 10** candidates is expressible *and*
   discriminating, and it is weak — `C5` discriminates only over *what is written
   in the packet today*, since the `||F_A||^2` expansion that carries SM-6's
   mechanism is a property of the symbol and survives an induced term.
2. **Parameter side.** H1's free-parameter count is **1 (packet:1106) or 0
   (W229:9)** and the repo does not adjudicate. H2's is **0 written or `>= 1`
   undeclared**, with the regulator that would define it recorded as
   non-admissible (`packet:858`).

### The missing bridge, named precisely (the reopener)

The packet named it itself, and it has not been built:

> *"No constraint surplus is reported at N1. Gauge, field redefinition,
> normalization, functional, topology, domain, and discrete-search quotients have
> not yet been ranked. ... **N5 must debit their functional freedom before
> reporting surplus.** The packet exists so N3/N5 can compute that rank."*
> — `packet:1120-1126`

Status check at pinned HEAD: `N3` ran
(`unified-source-datum-variational-emission-map-2026-07-30.md`, graded
"FORMULA-BUILT PARTIAL"). The ledger's `residue.quotients_ranked` is **5**, and
its own scope note says none of the five "is a full algebraic super-IG descent,
global coupled `Y14` interacting positive physical quotient, or **booked global
continuous-residue reduction**." **N5 has not run.** Until it does, the
denominator of every surplus on this action is unranked by the packet's own
contract, and LT-SM1's surplus is not merely unknown — it is **not yet defined**.

**Smallest sufficient reopener** (following B5's "one bridge suffices" shape):
make **one** constraint expressible *and discriminating* on the `zeta_F` bit. The
natural first candidate is **`C1` via `M-M4`**, the branching dictionary — it is
`I=M, E=M`, its `J2`/Sage gate is recorded **de facto satisfied**
(`improvement-register:257`: "SageMath 10.9 installed and in routine use"), it
discharges five registered open items from one build
(`science-council:362-374`), and a computed `g_1:g_2:g_3` branching would be the
first quantity that a *fundamental* `g_A` and an *induced* `g_A` need not agree
on. Second candidate: **recertify the RB6/RB7/W177 nulls with exact derivatives**
(`M-C2`), which would convert `C4` from inadmissible to decisive **in whichever
direction it actually lands** — note it currently *reads* against `zeta_F=1`,
i.e. against the direction `C5` points, so this is a genuine test and not a
confirmation.

### Would the row move?

**No.** LT-SM1 stays `NEEDS / FINITE_CHOICE`. Nothing here supplies the horn.

### Secondary observation: a partial (d), reported not asserted

Three typing notes for the wave, none of which changes the verdict:

1. **The row bundles two reason-kinds.** Its `summary` is "Yang-Mills kinetic
   term **and relative normalization**", but `reason_kind` is single-valued. The
   kinetic-term half is a finite choice; the normalization half is a
   **`REAL_PARAMETER`** (`g_A^{-2}`, plus the unbuilt 1-to-3 branching). The
   `distance` field ("select the `zeta_F`/Yang-Mills horn") addresses only the
   finite half. A wave splitting LT-SM1 into `LT-SM1a` (FINITE_CHOICE, the bit)
   and `LT-SM1b` (REAL_PARAMETER, the normalization) would make both halves
   independently dischargeable; as one row, discharging it requires both, which
   is why it has not moved.
2. **`ONE_BIT` exists in the taxonomy and is used zero times in 84 rows**
   (COMPUTED). A 2-element choice is exactly `ONE_BIT`. `FINITE_CHOICE`
   legitimately covers a 2-set, so this is not an error — but LT-SM1 being the
   sole `FINITE_CHOICE` row *and* `ONE_BIT` being empty suggests the two kinds
   have not been distinguished in practice.
3. **The `revival_trigger` presupposes its own answer.** It reads *"a source-action
   choice fixed by surplus constraints"* — but `packet:1120` (the same
   source-action document) states that no surplus is reported and that `N5` must
   run first. The trigger names an instrument the record says is not yet
   calibrated. Suggested reformulation for the wave: *"N5 quotient-ranking
   complete, or one constraint made discriminating on `zeta_F`."*

---

## 7. What a wave must verify independently

Ordered by how much of the above collapses if the item fails.

1. **`W229:81`'s `g_A^{-2} D_A* F_A` leg.** If that term is in `E_A`, `W229` is
   on `zeta_F = 1` while self-describing as the induced route (Lens 2). Verify by
   reading `W229:55-90` and asking whether the displayed `S_parent` at `:55-62`
   can produce it. **If I am wrong here, Lens 4's homonym table loses its sharpest
   example** — though the homonym itself survives, since senses A and B are
   defined on different fields regardless.
2. **The `g_A^{-2}` charging disconnect.** `packet:1106` (charged) vs
   `packet:1118` (derived list, which omits it) vs `W229:9` ("`Z_U` ... sets the
   induced YM coupling `g_A`"). **If `g_A^{-2}` is in fact derived from `Z_U`,
   H1's surplus is `+1` and the verdict moves toward (a).** This is the single
   highest-leverage check in the investigation and I could not settle it from the record.
3. **`C5`'s strength.** Does SM-6's Mexican-hat mechanism genuinely require a
   *fundamental* `||F_A||^2`, or does an induced one serve? I graded it weak on
   the symbol-vs-provenance argument. A field theorist should overrule me if the
   induced coefficient's scale dependence breaks the `lambda`-fixed-by-`g_A`
   relation that `cb-b:947-956` calls "the sharpest parameter reduction in the
   cluster."
4. **The three-reading fence.** Confirm the packet carries no layer typing
   (`grep -n -i "layer" explorations/unified-source-datum-packet-v0-2026-07-30.md`
   — I get zero hits). If the packet's `S_Y^{(0)}` is *intended* as the first
   layer only, then `SC-ACT-04`'s second-layer YM is a separate object and the
   `U2` fork may be posed on the wrong layer entirely.
5. **`N5` status.** I read `residue.quotients_ranked = 5` and its scope note as
   "N5 has not run." Confirm against `lab/process/` run records; if N5 *has* run
   somewhere I did not find, the missing bridge is different and the reopener
   changes.
6. **The horn count.** `1152 = 2^7 * 3^2` is consistent with seven binary forks
   but does not prove the YM fork is one of them. Confirm the YM fork is binary
   in whatever enumerates the nine.

---

## 8. Three-charge self-hostile review

### Charge 1 — Where did I overclaim?

- **`C5` as "discriminating."** This is the weakest joint in the investigation and it is
  load-bearing for the surplus table (it is the entire constraint side). I
  counted it because `cb-b:939` types SM-6 that way in its own words, then
  immediately argued in Lens 5 that the typing may not survive scrutiny. Counting
  a constraint I partly disbelieve is a real tension. **Mitigation, stated
  plainly: if `C5` is dropped, every surplus in the table drops by 1 and H1's
  best case falls to `0`. The verdict (c) does not change — it strengthens.**
- **"The repo does not agree with itself" on `g_A^{-2}`.** I verified both
  statements exist. I did **not** verify they are genuinely contradictory rather
  than scoped to different truncations — `W229` might mean "`Z_U` sets the
  *induced* coupling on the `zeta_F=0` branch" while `packet:1106` charges the
  *fundamental* one. That reading would dissolve the disconnect. I flag it and
  do not resolve it; item 2 of section 7 is where a wave should look.
- **The `1152 = 2^7 * 3^2` corroboration** is suggestive arithmetic, not proof
  that the YM fork is binary. The binary claim rests on `packet:498`
  (`\zeta_F\in\{0,1\}`), which is sufficient on its own; the factorization adds
  nothing load-bearing and I should not lean on it.

### Charge 2 — What did I fail to check?

- **I did not read the `cb-d-parameterizing-the-unknown-2026-08-05.md` parameter
  count in full** (only its line 487, which re-lists the 12 local action
  coefficients). If CB-D ranks `g_A^{-2}`'s independence, it would settle item 2
  of section 7 and I missed it.
- **I did not open the nine open discrete forks individually.** I inferred the YM
  fork's membership from `packet:1117`'s named `YM` entry rather than from
  whatever canonical list backs `open_discrete_forks: 9`. I did not find that
  list.
- **I did not examine the 2021 draft PDF directly.** `SC-ACT-04` is
  extraction-graded `newly-extracted` at p.45 eq (9.14); I took the register's
  word. For a claim this load-bearing to the source-fidelity lens, a wave should
  verify the locus.
- **I did not test whether an induced `||F_A||^2` actually preserves the
  `lambda`-`g_A` relation.** That is a computation (one-loop coefficient scale
  dependence) I could have attempted and did not; it is exactly what would settle
  `C5`.
- **I did not check `absorbed/`, `runs/`, or `_local/`** for prior LT-SM1 surplus
  work. My anti-redo grep covered `explorations/`, `lab/`, `canon/`, `tests/`,
  `papers/`, `docs/` (novelty-check's surfaces) plus a repo-wide `LT-SM1` grep.

### Charge 3 — What would change my verdict?

**Empty lists are stated explicitly where they are empty.**

Would move to **(a) the choice IS fixed**:
- `M-M4` built, yielding a `g_1:g_2:g_3` branching that one horn reproduces and
  the other cannot; **or**
- the `g_A^{-2}` disconnect resolved in `W229`'s favour (`g_A` derived from
  `Z_U`), giving H1 surplus `+1` against H2's `<= -1`; **or**
- `N5`'s quotient ranking completed such that H2's induction cost becomes
  countable and exceeds its constraints.

Would move to **(d) mistyped as the primary verdict**:
- a demonstration that the packet's `S_Y^{(0)}` is the *first* layer only, making
  `U2` a fork on an object that does not host the source's YM term at all. Then
  LT-SM1's `distance` names the wrong choice and the row needs re-posing, not
  deciding.

Would move to **ROUTE_KILLED for `zeta_F = 1`**:
- exact-derivative recertification of the RB6/RB7/W177 nulls (`M-C2`) confirming
  `FUNDAMENTAL-YM-W177-VERTICAL-RESPONSE-KILLED`. Note this would also **overturn
  `C5`'s direction**, so it is a genuine two-sided test.

Would **not** move me:
- any further FD-band numeric on the YM branch (P-H29, and the brief);
- any argument of the form "the second-layer norm square selects the coefficient"
  (`C8`, dead as a class);
- any symmetry-of-the-pairing or self-adjointness condition offered as a scale
  supplier (DC-H2's congruence-orbit theorem excludes the entire type);
- more artifacts adopting the Sakharov stance on `theta` (Lens 4: wrong homonym
  sense; they do not touch `zeta_F`).

**Empty lists:** claims killed by this investigation — **none** (`NONE-NOT-A-KILL`). Claim
IDs whose status changes — **none**. Ledger rows moved — **none**. Canon entries
touched — **none**. Repo files written — **none**. New free objects introduced —
**none** (every object named here is already charged in `packet:1104-1120`).
