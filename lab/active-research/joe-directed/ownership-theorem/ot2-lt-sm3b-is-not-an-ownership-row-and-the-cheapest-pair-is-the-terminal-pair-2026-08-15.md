---
artifact_type: exploration
status: exploration
doc_type: ownership-predicate-application
created: 2026-08-15
work_item: OT-2
channel: ownership_theorem
route: APPLY__PREDICATE_TO_NAMED_ROW_PLUS_EXACT_DEMAND_REDERIVATION
base_revision: a148ed80
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
ledger_edit: none -- versionless delta, for the canonical owner to disposition
target_claim: "OT-1-2026-08-15-SEC4-CHEAPEST-ROW -- OT-1 section 4 and section 5 Lens Q5 item 3: `2 rows -- LT-GR1b and LT-SM3b -- carry an O1-level production demand with no certified pairing demand and no parent demand. These are the only two a pure ownership theorem could reach without the datum named in section 2. LT-SM3b is O1-alone and is therefore the cheapest ownership row on the axis.` and `LT-SM3b is the cheapest ownership row on the axis -- O1-only, no pairing, no translation leg. If any single ownership move is attempted, that is the one whose obstruction is smallest.` (lab/active-research/joe-directed/ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md sections 4 and 5). This is an INTERNAL CHANNEL claim about the ledger and about OT-1's own classifier, not a canon claim and not a GU physics claim."
target_claim_verdict: REFUTED_AT_THE_ROW__PREDICATE_SURVIVES -- `LT-SM3b` is not `O1`-alone, is not the cheapest ownership row, and is not an ownership row at its gate at all; `LT-GR1b` survives as ownership-gated. The predicate `OWN` itself is not challenged and is used as written.
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
title: "OT-2: the predicate was applied to `LT-SM3b` and the row DID NOT MOVE, for a reason that is not about ownership. Re-derived from its own evidence file rather than its ledger summary, `LT-SM3b`'s demand is three conjuncts, not two; two of the three are already discharged inside that evidence file; the residual conjunct -- `extend the Riemann adapter through the action` -- returns `O1 = FAIL` by CHOSEN CONTRACTION and DECLARED REDUCTION, `O3a = PASS`, `O3b = FAIL` by domain non-stability, `O4 = ILL-TYPED` on a pairing demand that exists only in the evidence file and is invisible in the ledger row, `O5 = NOT PRODUCED` at `p = 0`. Composite **`NOT OWNED`, no subscript producible**. The row is `OVER_DETERMINED / STALE_PREMISE` -- terminal -- and its gate is `revival_trigger`, which asks for a PRIMARY SOURCE fact and is arithmetically unsatisfiable at the declared fixed-frame convention because `gamma_trace(pure contraction) = 1 != 0` exactly. `OWN` is the wrong instrument for this row at any budget. `LT-GR1b`, by contrast, names an ownership theorem inside its own revival trigger and IS ownership-gated -- so OT-1's pair is not a pair. Underneath, OT-1's `O1` token set is shown to carry ZERO tokens that are both discriminating (>=2 rows) and demand-bearing: every STRONG `O1` hit in OT-1 section 4, including the one that produced `cheapest row`, is a single-row verbatim lift of that row's own demand string."
grade: "EXACT integer / fractions.Fraction arithmetic; rank over Q by fraction-free elimination; no float constructed anywhere; assert_no_float sweeps the whole result dict. 128/128 checks, exit 0, via tests/channel-swings/joe_directed_ot2_lt_sm3b_ownership_application.py run from the repository root under _local/cas-venv. Split 34 [C] controls that must fire, 86 [E] exact results, 8 [R] reproductions. Failure path tested by three independent source mutations, each producing a distinct, non-overlapping failure set: adapter scalar -2 -> -3 (1 fail), Riemann dimension off-by-one (8+ fails), LT-SM3b O4 retyped NOT_TRIGGERED (2 fails). New exact content: the Riemann-adapter domain fraction in closed form `(d+1)/(3(d-1))`, equal to 5/9 on X^4 and 5/13 on Y^14, with 16 and 5096 unconstrained fibre directions respectively; the trace-reversal operator as `diag(1-d/2, 1)` reproducing `-2 * (13,1) -> (156,-2)` exactly at `d = 14` and at no other tested `d`; `det[[13,1],[156,-2]] = -182 != 0`. NOT: a ledger edit, a verdict change, a physics derivation, an adjudication between action parents, a challenge to OT-1's invariant-form theorem, or a claim that any GU quantity is owned."
disposition: PREDICATE_APPLIED__LT_SM3b_DID_NOT_MOVE__COMPOSITE_NOT_OWNED_NO_SUBSCRIPT__ROW_IS_TERMINAL_AND_ITS_GATE_IS_SOURCE_ATTRIBUTION_NOT_OWNERSHIP__REVIVAL_TRIGGER_ARITHMETICALLY_UNSATISFIABLE_AT_FIXED_CONVENTION__OT1_SEC4_CHEAPEST_ROW_CLAIM_REFUTED__LT_GR1b_SURVIVES_AS_THE_ONLY_OWNERSHIP_GATED_ROW_IN_THE_PAIR__A_OWN_REACHABLE_NOW_COUNT_GOES_2_TO_1__OT1_O1_TOKEN_SET_HAS_ZERO_DISCRIMINATING_DEMAND_BEARING_TOKENS
rows_touched_structurally: [LT-SM3b, LT-GR1b, LT-GR1, LT-GR3, LT-GR6, LT-SM5, LT-SM7]
rows_advanced: 0
rows_retyped_within_channel: [LT-SM3b]
depends_on:
  - lab/active-research/joe-directed/ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md
  - explorations/precontract-wave-0c-typed-identity-theorem-scope-2026-08-05.md
  - explorations/full-domain-shiab-observed-einstein-receiver-2026-08-05.md
  - lab/active-research/joe-directed/ledger-advancement/la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-constructible-cover-object-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la10-the-cut-vertex-survives-and-is-not-the-second-action-2026-08-15.md
  - lab/process/conditional-physics-ledger-v0.258.json
scripts:
  - tests/channel-swings/joe_directed_ot2_lt_sm3b_ownership_application.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** The computed objects here
> are (i) a **ledger-typing** result about how a terminal row's demand fields
> should be read, (ii) an **exact linear-algebra** reproduction and extension of
> the wave-0C Riemann adapter, and (iii) a **classifier-independence audit** of
> OT-1's own substring policy. Nothing here is a Lagrangian, a spectrum, a
> count, a selection principle, or evidence for or against Weinstein's
> source-native mechanism. Classification:
> **`STRUCTURAL_PLUS_DEFINITIONAL`, `pending_integration`.**

# OT-2 — the predicate was applied, and `LT-SM3b` did not move

## Verdict first, unsoftened

**The row does not move, and the reason is not that the ownership theorem is
hard. The reason is that `LT-SM3b` is not an ownership row at its gate.**

`OWN(Z | S, 𝒲, R)` was applied clause by clause to the object `LT-SM3b`'s own
evidence file actually names — the Riemann adapter. Composite: **`NOT OWNED`,
and no subscript is producible.** But that is the *second* result. The first is
that even a *passing* ownership verdict would not have moved this row, because
`LT-SM3b` is `OVER_DETERMINED / STALE_PREMISE` — terminal — and a terminal
row's gate is its `revival_trigger`, which here asks for **a primary source
fact**, not an action theorem.

| | `LT-SM3b` | `LT-GR1b` |
|---|---|---|
| verdict / reason-kind | `OVER_DETERMINED` / `STALE_PREMISE` | `OVER_DETERMINED` / `GENUINE_FALSIFICATION` |
| `O1` token in `distance` | yes (1 token) | yes |
| `O1` token in `revival_trigger` (**the gate**) | **no** | **yes** — *"an action theorem owning the independent Gauss route"* |
| what the gate asks for | *"a **primary source** or full-domain theorem proving the pure contraction must occupy the constraint-preserving spinor slot"* | an **ownership theorem** |
| is `OWN` the right instrument? | **no, at any budget** | **yes** |

So OT-1's "two reachable rows" is **not a pair**. It is one ownership-gated row
and one source-attribution row that shares a bucket only because a compressed
`distance` string happens to end with the words *"through the action."*

**`A_OWN`'s reachable-now count goes from 2 to 1.**

---

## 0. PREFLIGHT — six specialist lenses, run inline before applying

### Lens P1 — ledger archivist: re-derive `LT-SM3b`'s demand from its own evidence file, and report what moved

The instruction was to read the evidence file, not the summary. Three things
moved, all `[E]`, all substring-certified against the two files.

**(a) The prescribed distance has three conjuncts; the ledger carries two.**
`explorations/precontract-wave-0c-typed-identity-theorem-scope-2026-08-05.md`
§4 prescribes verbatim:

```text
distance: keep the exact gamma-traceless T3 line, separate it from the adjoint
          Shiab, and extend the Riemann adapter through the action
```

The v0.258 row carries `separate source adjoint Shiab from reconstructed spinor
vertex and extend the Riemann adapter through the action`. The first conjunct —
**"keep the exact gamma-traceless T3 line"** — occurs nowhere in the row. So
LA-1's audit note (*"the ledger row transcribes its evidence file's prescribed
disposition verbatim"*) is very nearly right and is off by one conjunct. This
is not a defect in the row: conjunct (a) is *already discharged* inside the
evidence file itself (§1, exact, no convention ambiguity), and so is conjunct
(b) (§2's type table separates the two Shiabs by coefficient bundle and degree).
**The residual demand is exactly conjunct (c).**

**(b) The residual conjunct carries a pairing demand that the ledger row does
not.** The evidence file's own account of what "extend through the action"
requires names, verbatim:

| evidence-file token | where |
|---|---|
| `full action pairing` | §3, in the list of "extra structure" the restriction does not supply |
| `Hodge/Krein owners` | §3, same list |
| `pairing and soldering` | §6, construction handoff step 2 |

**None of these three strings occurs anywhere in the v0.258 row** (`[E]`), and
each occurs exactly once in the evidence file. Control: none of the three
occurs in `LT-GR1b`'s evidence file, so they are demand-specific and not
boilerplate (`[C]`, fires).

**Therefore `LT-SM3b`'s demand set, read from evidence, is at least
`{O1, O4}` — it is not `O1`-alone.** That is the first refutation of the target
claim, and it is visible only at evidence granularity.

**(c) The row is terminal, and both of OT-1's "reachable" rows are terminal.**
Verdict census over the seven `A_OWN` rows (`[E]`):

```text
OVER_DETERMINED  2   LT-GR1b, LT-SM3b     <- OT-1's "reachable now" pair, exactly
DIFFERS          2   LT-GR3, LT-GR6
NEEDS            2   LT-GR1, LT-SM7
SAME             1   LT-SM5
```

The coincidence is exact and it is not a coincidence: §2 explains it.

### Lens P2 — type-checker: the brief's own typing of the row is ill-typed

The task brief types `LT-SM3b` as `NEEDS / STALE_PREMISE`. Against the ledger's
own taxonomy that pair does not exist: `STALE_PREMISE` is listed under
`OVER_DETERMINED` and is **not** listed under `NEEDS` (`[E]`). Under the
taxonomy's `NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN` rule this is **ill-typed,
not false** — the same disposition `O4` gives an unsubscripted pairing. Flagged
because the difference between `NEEDS` and `OVER_DETERMINED` is exactly the
difference between "a demand awaiting discharge" and "an adjudication awaiting
revival," and the whole result below turns on it. Control: `NEEDS /
MISSING_CONSTRUCTION` is well-typed, so the test discriminates (`[C]`, fires).

### Lens P3 — classifier auditor: is OT-1's `O1` evidence policy independent of its input?

**No, and the failure is total on this clause.** OT-1's `O1_PRODUCTION` token
set has nine entries. Hit census over the seven `A_OWN` rows (`[E]`):

| census | count | detail |
|---|---:|---|
| tokens hitting **0** rows | 1 | `ACTION_OWNED` — dead |
| tokens hitting exactly **1** row | 7 | six of them land in a demand-bearing field |
| tokens hitting **≥2** rows | 1 | `RESTRICTED_ACTION` → `LT-GR1`, `LT-GR6` |
| tokens that are **both** discriminating (≥2 rows) **and** demand-bearing | **0** | — |

A substring that hits exactly one row cannot classify; it is a row label with a
receipt stapled to it. `RESTRICTED_ACTION`, the only discriminating token,
lands in **no** demand-bearing field — which is why OT-1 itself marks those two
hits `w`/WEAK. So **every STRONG `O1` hit in OT-1 §4 is a single-row verbatim
lift of that row's own demand string**, and `LT-SM3b`'s is the extreme case:
its entire `O1` classification rests on **one token**, and that token is
`"extend the Riemann adapter through the action"` — the tail of `LT-SM3b`'s
`distance` field, quoted back at it.

This does not make OT-1's §4 partition *wrong*. It makes it a **hand
labelling with a receipt**, carrying zero independent classification content on
`O1`. Control that the audit is not a general smear: OT-1's `O4` token `Hilbert
stress` *does* hit two rows, so a discriminating token is constructible (`[C]`,
fires); and three of OT-1's seven `O4` tokens are dead, so token-set slack is
real and not specific to `O1` (`[C]`, fires).

### Lens P4 — evidence law: grep before claiming novelty

| prior object | owner | relation to OT-2 |
|---|---|---|
| the exact `T3` line, `W − 6C = −6·T3`, the `(1,6)` gamma-trace row, the `(13,1)`/`(156,−2)` responses, trace reversal | wave-0C §1–§3 | **reproduced exactly, not re-derived.** OT-2 adds only the operator form `diag(1−d/2, 1)`, the `d`-sensitivity controls, and `det = −182` |
| `LT-SM3b` is correctly typed `STALE_PREMISE`; the row is terminal, not pending | `LA-1` §383, re-affirmed `LA-6` §4.5 | **carried, not challenged.** OT-2 supplies the *consequence*: a terminal row's gate is `revival_trigger` |
| *"the coupled pair `{LT-GR1b, LT-SM3b}` may be an artifact of both rows being terminal (`OVER_DETERMINED`) and therefore under-described … Not resolved here."* | `LA-6` §5.2, second contrary reading | **now resolved, and confirmed** — independently, on a different classifier. This is the same artifact appearing twice |
| the predicate `OWN`, its five clauses, the `d ≥ 2` invariant-form obstruction, the named datum | `OT-1` §1–§2 | **used as written and not redesigned.** No clause is added, deleted or reweighted |
| `b9_STAT` / the base-duality object no row names | `LA-10`, `OT-1` §5 Q5 item 2 | OT-2 adds `LT-SM3b`'s latent `O4` to the same convergence |

The strings `adapter domain fraction`, `(d+1)/(3(d-1))`, `5096`, and
`arithmetically unsatisfiable` return zero repo-wide hits. Per the
grep-before-novelty rule that is **not** evidence of novelty on its own; the
narrow novelty claim is stated in §6 and it is two numbers and a typing rule.

### Lens P5 — variational geometer: predict `O1`'s verdict before computing it

Write down the adapter's construction steps first, then type them. Wave-0C §3
builds it as: restrict to the algebraic-Riemann spin image → Clifford
contraction `Φ_S` → exact trace reversal → multiply by `−2`. Two of those four
are **named `O1` failure modes verbatim** ("a chosen contraction", "a declared
reduction"); none is a first variation. **Prediction, written before the
arithmetic: `O1 = FAIL`, and it fails structurally rather than contingently.**
The probe confirms it (`[E]`). The prediction is what makes the verdict
interpretable: `LT-SM3b`'s adapter is not an object that *has not yet been*
derived from an action — it is an object built by a route `O1` excludes.

### Lens P6 — honesty auditor: three specific vacuities to guard against

1. **Vacuity by construction.** If `OWN` returned `NOT OWNED` on everything, a
   `NOT OWNED` here would carry no information. Guarded: a synthetic
   fully-owned object returns `OWNED`, a synthetic `O3a`-pass/`O3b`-fail object
   returns `HALF_OWNED`, and flipping `O1` flips the composite — three distinct
   verdicts from the same evaluator (`[C]`, all fire).
2. **Vacuity by threshold coincidence.** §3's extension gap vanishes iff
   `d = 2`; OT-1's nondegenerate invariant form exists iff `d ≤ 1`. These are
   **different predicates** and the temptation to call it a convergence is
   refused: they disagree at `d = 2` exactly, and a planted control asserts the
   disagreement (`[C]`, fires). Agreement for all `d ≥ 3` is not evidence of a
   common mechanism.
3. **Vacuity by unfalsifiable bookkeeping.** The clause verdicts in §2 are
   typed data, so a mutation must be able to break them. Tested: retyping
   `LT-SM3b`'s `O4` to `NOT_TRIGGERED` fails 2 checks; perturbing the adapter
   scalar fails 1; an off-by-one in the Riemann dimension fails 8+.

---

## 1. THE OBJECT — what `Z` actually is

`LT-SM3b`'s *claim* is a source-attribution premise ("the canon spinor
reconstruction is Eric's one written Shiab") and that premise is adjudicated
stale. Applying an ownership predicate to a dead premise would be a category
error, so `Z` is taken from the residual demand conjunct, which names exactly
one object — wave-0C §3's adapter:

> `Shiab_ad | Riemann = −2 · encode · trace_reverse · decode · Φ_S · action`
>
> at the declared **fixed-frame** Riemann-restriction grade.

Reproduced exactly (`[E]`, all `Fraction`):

```text
C  = (1, 0, 1, 0)          pure contraction
W  = (0, 1, 0, 1)          wedge
T3 = C − (1/6)W = (1, −1/6, 1, −1/6)
W − 6C = (−6, 1, −6, 1) = −6·T3            same projective element, exactly
gamma-trace row (1, 6) per block:  T3 ↦ (0,0)      C ↦ (1,1)      W ↦ (6,6)
constraint rank 2 of 4  ⇒  gamma-traceless kernel is exactly 2-dimensional
```

and the Riemann leg, which is where the new arithmetic is:

```text
spinor Ricci path   (13,  1)
adjoint selected    (156, −2)
det[[13,1],[156,−2]] = −182 ≠ 0            no scalar multiple relates them

trace_reverse in dimension d  =  diag(1 − d/2, 1)
   at d = 14:  diag(−6, 1)
   (13, 1) ↦ (−78, 1) ↦ ×(−2) ↦ (156, −2)          EXACT
```

The operator form is the small addition: wave-0C states the numbers, OT-2
states the operator and shows it is **tight in `d` and in the scalar**. Controls
that fire: the identity fails at `d ∈ {4, 10, 13, 15}`; it fails for scalars
`{−3, −1, 2, 6}`; it fails without trace reversal; and it fails if the spinor
scalar coordinate is taken as `d` rather than `d − 1`.

> `|det| = 182 = 2·91 = dim T*Spin₀(7,7)`, the same 182 as OT-1. **Recorded as
> arithmetic, not as a link.** `91 = C(14,2)` appears in both places because
> both are built on `𝔰𝔬(7,7)` at `d = 14`; no mechanism connects them and none
> is claimed.

---

## 2. THE PREDICATE, APPLIED — five clauses on `LT-SM3b`

| clause | verdict | evidence |
|---|---|---|
| **`O1` PRODUCTION** | **FAIL** | The construction contains a **chosen contraction** (`Φ_S`) and a **declared reduction** (restriction to the algebraic-Riemann spin image) — two of `O1`'s four named failure routes, verbatim. **No step is a first variation of any functional.** The evidence file concurs in its own words: *"This makes equality a meaningful question. It does not make it true"*; *"a Riemann-restricted adapter seed, not a full-domain identity."* |
| **`O2` TRIVIALIZATION-INVARIANCE** | **UNREACHED** (not PASS) | The adapter is declared at the **fixed-frame** grade, so `η = w⁻¹δw` never enters and there is no trivialization choice to be invariant under. `O2` acquires content only at wave-0C §6 step 2 ("moving Hodge, pairing and soldering"). Reporting this as PASS would be the error `O2` was written to prevent. |
| **`O3a` reductive leg** | **PASS** | `trace_reverse = diag(1 − d/2, 1)` acts by a scalar on each factor of the `𝔰𝔬(d)`-irreducible (scalar, traceless-Ricci) split — Schur-diagonal, hence equivariant. Clifford contraction and trace reversal are both `𝔰𝔬(d)`-natural. This is the one clause that genuinely passes. |
| **`O3b` translation leg** | **FAIL** | The adapter's *domain* is `R(ℝ^d)`, a proper `𝔰𝔬(d)`-submodule of the curvature fibre `Λ² ⊗ 𝔰𝔬(d)`, of codimension **16 on `X⁴`** and **5096 on `Y¹⁴`** (§3). `V = Ω¹(ad P)` translates a connection by `a`, sending `F ↦ F + d_A a + a∧a`, which does not preserve the first Bianchi condition cutting out `R`. So the adapter's `V`-behaviour is not merely undeclared — **its domain is not `V`-stable.** Wave-0C names this itself, listing *"the Riemann injection/retraction, algebraic and differential Bianchi conditions"* among the extra structure required. |
| **`O4` SUBSCRIPTED PAIRING** | **ILL-TYPED** | Triggered, not by the adapter alone, but by wave-0C §6 step 4's demand that *"the resulting full **variational square** commute"* — identifying two Euler expressions across the two paths requires a pairing. The evidence file names the pairing three times (`full action pairing`, `Hodge/Krein owners`, `pairing and soldering`) and **names no invariance group.** Per `O4`, omitting the subscript is ill-typed, not false. |
| **`O5` RIVAL DISCRIMINATION** | **NOT PRODUCED** (`p = 0`) | No parent produces the adapter by variation, because `O1` fails structurally rather than parent-contingently. `p = 0` is determinate **without adjudication**, so `LT-SM3b` is not parent-entangled in the `LT-GR3` sense. This is `O1` restated across the parent set and carries no independent information. |

### Composite

```text
OWN( Riemann adapter | S_source, 𝒲, R = fixed-frame Riemann restriction )
    =  NOT OWNED
    subscript: NONE PRODUCIBLE
```

**No subscript.** `O4`'s would-be pairing factors, exactly as OT-1 §2 says, into
(a) an `Ad`-invariant nondegenerate fibre form — **available**, the Killing form
of the semisimple `𝔰𝔬(7,7)`, at subscript `𝒢` — and (b) a base duality (the
moving Hodge), which is **unsupplied**. So the verdict cannot even be reported
as `NOT OWNED_𝒢`; the subscript slot is empty because leg (b) has no owner.

**This puts `LT-SM3b` in the same blocked bucket as `LT-GR1` and `LT-GR6`.**
OT-1 §5 Q5 item 2 recorded that those two are blocked at one and the same base
duality — `b9_STAT`'s territory, the object `LA-10` says no row names. **Three
rows now point at it, not two.** That convergence is the one positive result
here.

### Did the row move?

**No, and it is not close.** But the operative reason is upstream of every
clause above:

`LT-SM3b` is `OVER_DETERMINED / STALE_PREMISE`. For a `NEEDS` row, `distance`
*is* the demand. For a terminal row, `distance` is the **evidence file's
transcribed construction handoff** and `revival_trigger` is the **gate**.
`LT-SM3b`'s gate reads:

> *"a **primary source** or full-domain theorem proving the pure contraction
> must occupy the constraint-preserving spinor slot"*

That gate contains **no `O1` token under OT-1's own full token set** (`[E]`).
An ownership theorem cannot supply a fact about what the source wrote. And the
non-source horn is arithmetically closed at the declared convention:

```text
the gate asks:            gamma_trace(pure contraction) = 0
exact arithmetic:         gamma_trace(1, 0) = 1·1 + 6·0 = 1  ≠  0
```

No theorem puts a vector into the kernel of a functional it is not in. The gate
is therefore satisfiable only by (i) a primary-source fact that changes what
"the pure contraction" refers to, or (ii) a full-domain extension that changes
which line is constraint-preserving — **and (ii) is the very object `O1` just
failed on.** The row's revival is circularly gated on the object whose ownership
was at issue. Control: `gamma_trace(T3) = 0`, so the *other* line is
satisfiable and the obstruction is specific, not generic (`[C]`, fires).

### The exact transition, and it is not a discharge

```text
LT-SM3b   verdict / reason-kind      UNCHANGED   OVER_DETERMINED / STALE_PREMISE
          rows_advanced                      0
          channel-internal re-typing:
             OT-1 §4  "PURE_OWNERSHIP, O1 alone, cheapest ownership row"
          →  OT-2     "TERMINAL; gate is source-attribution, not ownership.
                       Residual demand is {O1, O3b, O4}, with O4 at the same
                       unsupplied base-duality datum as LT-GR1 and LT-GR6.
                       NOT reachable by OWN at any budget."
```

**No grant is laundered.** Nothing is converted from conditional to derived.
The one thing carried forward — that the Killing form supplies `O4`'s fibre leg
at subscript `𝒢` — is stated as an *available datum*, never as a discharge, and
the composite verdict explicitly refuses the `𝒢` subscript because the base leg
is missing.

---

## 3. THE EXTENSION GAP — exact, closed form, new

Wave-0C says *"Restriction does not determine a unique full-domain map"* and
does not quantify it. It quantifies exactly.

With `ad P` the frame algebra, the curvature fibre is `Λ²(ℝ^d) ⊗ 𝔰𝔬(d)`, of
dimension `C(d,2)²`, and the algebraic-Riemann subspace has dimension
`d²(d²−1)/12`. The adapter is defined on the second inside the first, so its
**domain fraction** is

```text
   dim R(d)        d²(d²−1)/12          d + 1
 ------------  =  --------------  =  ----------          (exact, [E])
  C(d,2)²          (d(d−1)/2)²         3(d − 1)
```

verified at `d ∈ {2,3,4,5,6,10,14,20}`.

```text
              fibre    Riemann   fraction   unconstrained
  X⁴  (d=4)      36         20      5 / 9              16
  Y¹⁴ (d=14)   8281       3185      5 / 13           5096
```

`8281 = 91²` and `91 = C(14,2) = dim 𝔰𝔬(7,7)`, reproducing OT-1's fibre
dimension (`[R]`). The unconstrained fraction is `(2d−4)/(3(d−1))`, which
**vanishes iff `d = 2`**.

> **The `d = 2` coincidence is refused, not claimed.** OT-1's predicate is
> *"a nondegenerate `Ad(𝒲)`-invariant symmetric form exists iff `d ≤ 1`"*;
> this one is *"the Riemann restriction is the whole fibre iff `d ≤ 2`"*. They
> **disagree at `d = 2`**, and a control asserts the disagreement (`[C]`,
> fires). They agree for every `d ≥ 3`, which is exactly why agreement alone is
> worthless as evidence of a shared mechanism. Two low-dimensional degeneracies,
> two mechanisms.

This number is what makes `O3b`'s failure a measurement rather than an opinion:
on `Y¹⁴` the adapter is silent on **5096 of 8281** fibre directions, and the
`V`-translations move into exactly that silence.

---

## 4. `LT-GR1b` — the other half of OT-1's pair

Applied for completeness, since OT-1 paired them.

| clause | verdict | evidence |
|---|---|---|
| `O1` | **NOT CONSTRUCTED** | The object — *"an independently action-owned pre-Shiab Gauss/II route"* — does not exist. This is **not** `LT-SM3b`'s failure: `LT-SM3b`'s object exists and was built by an excluded route; `LT-GR1b`'s has not been built at all. Different costs, different work. |
| `O2`, `O3a`, `O3b` | **UNREACHED** | no object to test |
| `O4` | **NOT TRIGGERED AT ROW TEXT** — latent | Contracting a Gauss/Codazzi relation down to Einstein–Hilbert requires a base metric contraction, so `O4` is latent. Flagged as a *reading*, not certified; it is not asserted. |
| `O5` | **UNDEFINED UNTIL `O1`** | `p` is not computable without the object |
| composite | **`NOT OWNED`** at an unbuilt object | |

`LT-GR1b` also does not move today. But **its gate names the instrument**:
*"an action theorem owning the independent Gauss route"* sits inside its
`revival_trigger` (`[E]`). So an ownership theorem is the correct tool for
`LT-GR1b` and the wrong tool for `LT-SM3b`, and the two rows are not
interchangeable at any level.

**Corrected reading of OT-1 §4.** The partition `2 + 2 + 1 + 2` survives as a
partition of *demand kinds*. What does not survive is the sentence that follows
it. The "2 reachable now" is **1**: `LT-GR1b`. And `LT-SM3b` should be moved out
of the ownership bucket entirely — its residual demand is real but it is a
*construction* demand inherited from a construction handoff, sitting on a row
whose gate is elsewhere.

---

## 5. POSTFLIGHT — five lenses, run on this artifact

### Lens Q1 — strongest overclaim available here, and it is refused

The available inflation is: **"OT-1 §4 is worthless; the substring evidence
policy is broken and the whole partition should be discarded."** Refused.

What is proved is narrow and it is about **one clause**: the `O1` token set has
zero tokens that both discriminate and land in a demand field. `O4`'s
`Hilbert stress` *does* discriminate, so `LT-GR1`/`LT-GR6`'s "blocked at the
datum" typing is *not* affected by this audit and stands as OT-1 filed it.
`O5`'s `rival action parent` on `LT-GR3` is a single-row lift too, but its
content is a direct quotation of the row's own words about parents and no
classification step intervenes. The partition is a hand labelling with receipts;
hand labellings can be correct, and this one mostly is. **What fails is exactly
one downstream sentence — "cheapest ownership row on the axis" — because that
sentence is a *comparative* claim, and comparative claims are precisely what a
non-discriminating token set cannot support.**

A second available inflation: **"`LT-SM3b` should be closed / retired."**
Refused, and out of scope. Its verdict is not mine to move, no ledger edit is
proposed, and a row whose gate is a primary-source fact is exactly the kind of
row that a later source record can revive. Terminal is not dead.

### Lens Q2 — strongest contrary reading, which I cannot refute

**A reader can deny that `revival_trigger` is the gate for a terminal row.**
The steelman: the ledger schema gives every row a `distance` and a
`revival_trigger`, and nothing in the schema says one supersedes the other by
verdict class. `distance` means "what is missing" for *all* rows; the fact that
`LT-SM3b`'s `distance` was transcribed from a construction handoff is a fact
about how it was written, not about how it should be read. On that reading
`LT-SM3b` genuinely does carry an ownership demand in a demand-bearing field,
OT-1 §4 read it correctly, and my §2 conclusion is a distinction I invented.

I cannot refute this from the schema, and I will not pretend otherwise. What I
can say is that the reading has an uncomfortable consequence: it makes every
adjudicated row's transcribed handoff into a live demand on the current program,
which would inflate the open-work count across the whole ledger by the number of
terminal rows. And it does not touch the *arithmetic* result — `LT-SM3b`'s
revival trigger remains unsatisfiable at fixed convention either way, and
`O1`/`O3b`/`O4` fail either way. **The gate distinction changes the framing;
the clause verdicts survive without it.** But if the distinction is wrong, then
"not an ownership row at all" softens to "an ownership row whose ownership
demand fails at three clauses," which is a weaker and less interesting headline.
**That is the cheapest way to attack this artifact and it should be attacked
first.**

A second contrary reading, weaker but live: `O3b`'s failure here leans on
identifying `ad P` with the frame algebra `𝔰𝔬(d)` so that `Ω²(ad P)` is
`Λ² ⊗ Λ²`. If GU's `ad P` at the relevant stage is *not* the frame algebra, the
codimensions `16` and `5096` are fixture-scoped and the *numbers* go, though the
non-`V`-stability of a Bianchi-cut subspace does not.

### Lens Q3 — weakest seam of this construction

**The seam is `O4 = ILL-TYPED` on `LT-SM3b`, and specifically the step from
"the evidence file says `pairing`" to "the clause is triggered."** `O4`'s
trigger condition is written for a field-type object asserted to be an Euler
expression, or a metric/positivity/norm-square statement. The adapter is
*none* of those — it is a bundle map. I reach `O4` through wave-0C §6 step 4's
demand that the **variational square commute**, which does put two Euler
expressions into the same statement. That inference is a **reading of a
construction handoff**, not a computation, and it is the least-supported
load-bearing step in this artifact. A reader who declines it gets
`O4 = NOT_TRIGGERED`, and then `LT-SM3b` really is `O1`-plus-`O3b`, and the
"three rows point at `b9_STAT`" convergence in §2 drops back to two. **Flagged
rather than buried**, and it is exactly the check the mutation test exercises.

Second seam: `O3a = PASS` is asserted from Schur's lemma on a two-block split
that I did not exhibit as a full `𝔰𝔬(d)`-module decomposition. It is standard
and I believe it, but it is the one clause verdict here with no planted control
of its own.

Third seam, structural: **the census in §0 P3 is over seven rows.** Statements
of the form "zero tokens are discriminating" are cheap on a seven-element set.
Run over all 82 active rows the same token set would certainly discriminate
more. The claim is scoped to OT-1's own denominator, which is the right scope
for auditing OT-1 — but it is a small denominator and that should be said.

### Lens Q4 — the question asked directly: is applying a one-day-old predicate to a row a real discharge, or is it circular?

**Neither, and the honest answer is more useful than either.**

*It is not circular*, and there is a one-bit test for that which it passes: the
predicate's author named `LT-SM3b` "the cheapest ownership row on the axis" and
paired it with `LT-GR1b`. Applying it carefully **broke the pair and removed the
row from the reachable bucket.** A predicate fitted to produce a wanted verdict
does not do that. There is at least one bit of non-circular content, and it
went against the author.

*But it is also not a predicate-driven discharge*, and claiming otherwise would
be the real dishonesty here. **What did the decisive work was not `OWN`.** It
was two pieces of ledger hygiene: (i) reading the evidence file instead of the
row, which surfaced the third conjunct and the pairing demand; and (ii)
noticing that the verdict class `OVER_DETERMINED` changes what `distance`
means. Neither of those is a clause of `OWN`. The predicate then *articulated*
the result — it supplied the vocabulary (`chosen contraction`, `domain not
`V`-stable`, `unsubscripted pairing`) and it forced the `O2`-unreached and
`O5`-`p=0` distinctions that a prose reading would have blurred. That is real
value, and it is the value of a **type system**, not of a theorem.

The sharpest version: **a one-day-old predicate applied to a row by the same
channel that built it is only worth something when it returns an answer the
channel did not want. This one did. That is the whole of its non-circular
content, and it is one bit.** The 128 checks are certification, not
independence; nothing here is independent of OT-1's framing, and a genuinely
independent test would come from someone who did not write `OWN`.

### Lens Q5 — decision usefulness: does this change what to work on?

Yes, and it *removes* work rather than adding it.

1. **`LT-SM3b` should not be attempted as an ownership move.** It was named the
   cheapest and it is unreachable by `OWN` at any budget. Whatever budget was
   earmarked for it is freed.
2. **`LT-GR1b` is the only `A_OWN` row reachable now**, and its `O1` is
   `NOT CONSTRUCTED` — build cost, not re-derivation cost. Reachable-now goes
   `2 → 1`, and the one that survives is the expensive kind.
3. **Three rows, not two, are blocked at the base-duality datum** (`LT-GR1`,
   `LT-GR6`, and now `LT-SM3b`'s latent `O4`). That strengthens OT-1 §5 Q5
   item 2's convergence on the object `LA-10` says no row names.
4. **A ledger-reading rule falls out that is reusable beyond this channel:**
   for a terminal (`OVER_DETERMINED`) row, `distance` is a transcribed handoff
   and `revival_trigger` is the gate; any classifier that treats both as
   demand-bearing will systematically over-count terminal rows as cheap,
   because terminal rows are under-described. `LA-6` §5.2 predicted exactly this
   and left it unresolved; it is now resolved and it fired on the first
   classifier that hit it.

---

## 6. CLAIM CEILING

**May be claimed, exactly and only:**

- `LT-SM3b` is `OVER_DETERMINED / STALE_PREMISE` in v0.258; the pair
  `NEEDS / STALE_PREMISE` does not exist in the ledger's taxonomy.
- Its evidence file prescribes a three-conjunct distance; the ledger row
  carries the last conjunct and drops the first; the strings `full action
  pairing`, `Hodge/Krein owners` and `pairing and soldering` occur in the
  evidence file and in no field of the row.
- Over the seven `A_OWN` rows, OT-1's `O1` token set has one dead token, seven
  single-row tokens and one two-row token, and **zero** tokens that are both
  discriminating and demand-bearing. `LT-SM3b`'s `O1` classification rests on
  one token equal to the tail of its own `distance` field.
- `LT-GR1b`'s `revival_trigger` contains an `O1` token; `LT-SM3b`'s contains
  none.
- The exact adapter arithmetic of §1, including `trace_reverse = diag(1−d/2,1)`,
  the closure at `d = 14` and its failure at the tested alternatives, and
  `det = −182`.
- The adapter domain fraction `(d+1)/(3(d−1))`, equal to `5/9` on `X⁴` and
  `5/13` on `Y¹⁴`, with `16` and `5096` unconstrained fibre directions, under
  the stated identification of `ad P` with the frame algebra.
- `gamma_trace(pure contraction) = 1 ≠ 0` exactly, hence `LT-SM3b`'s revival
  trigger is unsatisfiable at the declared fixed-frame convention.
- The clause verdicts of §2 and §4 **as applications of OT-1's predicate as
  written**, with the composite `NOT OWNED` and no subscript.

**May NOT be claimed, and is not:**

- That `LT-SM3b`'s verdict or reason-kind changes. Zero rows advance; no ledger
  edit is proposed.
- That OT-1's predicate is wrong, or that any clause should be added, removed or
  reweighted. It is used exactly as written.
- That OT-1's `d ≥ 2` invariant-form theorem is challenged. It is not touched.
- That OT-1's §4 partition is wrong. Only the comparative sentence "cheapest
  ownership row on the axis" is refuted, and only because comparative claims
  need discriminating evidence.
- That the `d = 2` agreement between §3's gap and OT-1's pairing threshold is a
  convergence. It is explicitly refused by a control.
- That any GU quantity is, or is not, action-owned.
- Any adjudication between the three action parents. `O5` returns `p = 0` by
  computation, never by preference.
- Novelty for the wave-0C adapter, the `T3` identity, the gamma-trace row, the
  Riemann responses, or the `STALE_PREMISE` typing. The novelty claimed is
  narrow: the closed-form domain fraction, the terminal-row gate rule, and the
  `O1` token-independence census.

**Not laundered:** no grant becomes a derivation. The Killing form is named as
an *available* fibre-leg datum at subscript `𝒢` and is explicitly refused as a
composite subscript because the base leg is unsupplied. `CG-1`'s reduction and
`AUDIT`'s `REDUCTION_EXTERNAL` price are untouched. `SG4` remains the open
decider and nothing here builds it.

---

## 7. REPRODUCE

```bash
cd /path/to/gu-formalization
_local/cas-venv/bin/python \
    tests/channel-swings/joe_directed_ot2_lt_sm3b_ownership_application.py
```

Expected: `CERTIFICATE: 128/128 checks pass; no load-bearing float (swept).`,
exit 0, split `[C] 34  [E] 86  [R] 8`. The probe resolves the ledger and both
evidence files relative to its own location and runs from the repository root.

Failure path (each mutation must break the stated checks and no others):

```text
got = tuple(-2 * x ...)  ->  -3     1 fail   (S5 adapter closure)
return num // 12         ->  + 1    8 fails  (S6 dimensions and closed form)
LT-SM3b O4 ILL_TYPED     ->  NOT_TRIGGERED   2 fails (S7 non-O1-alone typing)
```
