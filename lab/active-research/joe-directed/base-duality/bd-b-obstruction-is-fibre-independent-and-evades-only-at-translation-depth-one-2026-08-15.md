---
artifact_type: exploration
status: exploration
doc_type: subscript-lattice-decision
created: 2026-08-15
work_item: BD-B
channel: base_duality
route: SWEEP__COMPLETE_SUBSCRIPT_LATTICE_PLUS_EXACT_DICHOTOMY
base_revision: a148ed80
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
ledger_edit: none -- versionless delta, for the canonical owner to disposition
target_claim: "OT-1-2026-08-15-SEC2-SUBSCRIPT-W-ONLY -- OT-1 section 2 and section 5 Lens Q1: `no Ad(W)-invariant nondegenerate symmetric bilinear form on Lie(W) exists for d >= 2` together with its own scope sentence `it shows that ownership carries a mandatory group subscript that cannot be W`, and its named-but-unclosed escape `a pairing that is not symmetric ... my theorem does not touch those`; plus LA-11 section 3's fence that the scope phrase `at a NAMED group subscript` in the proposed LT-GR6b revival_trigger is load-bearing because `fix the subscript to W and the satisfying set IS empty`; plus OT-2's carried datum that `the Killing form supplies O4's fibre leg at subscript G`. All three are INTERNAL CHANNEL claims about repository objects -- not canon claims, not GU physics claims, and not claims about anything Weinstein asserts."
target_claim_verdict: UPHELD_AND_GENERALISED_AT_W__DECIDED_EVERYWHERE_ELSE__ONE_ESCAPE_CLOSED__TWO_TYPING_CORRECTIONS -- OT-1's theorem survives an independent from-scratch re-derivation with no correction; it is generalised to a bound valid at EVERY subscript; the fibre subscript is proved INERT, so the no-go is fibre-subscript-independent; the whole verdict is proved to depend on ONE integer, the translation depth, and the evasion set is exactly `t <= 1`; OT-1's own named antisymmetric escape hatch is CLOSED (the invariant antisymmetric space at subscript W is EMPTY, not merely degenerate); OT-2's fibre-leg typing and OT-1's remainder numbers are corrected for the source's own `Delta1` fibre algebra
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
title: "BD-B: the subscript lattice is DECIDED, and the fibre subscript is INERT. For `w = g |x (Lambda^1 (x) g)` and ANY subalgebra `h`, every `h`-invariant symmetric form obeys `rank B <= dim w - dim(g.V') + dim g` with `V' = h ^ V`; hence a nondegenerate one exists IFF `dim(g.V') <= dim g`, i.e. IFF the TRANSLATION DEPTH `t` is at most 1 -- a criterion that does not mention the fibre subscript at all. Max rank is exactly `min(dim w, (d+2-t) dim g)` and the radical is exactly `max(0, (t-1) dim g)`, collapsing to OT-1's `2 dim g` and `(d-1) dim g` at `t = d`. So the obstruction is a GENERAL NO-GO across the entire fibre column -- `Spin_0(7,7)`, `Spin_0(9,5)`, `Spin(6,4)`, `U(64,64)`, maximal compact `K`, `U(3,2)`, the Standard Model subgroup, a Cartan, and the trivial group all give the SAME verdict at fixed `t` -- and simultaneously a NAMED EVASION ROUTE in the one coordinate that is not the fibre: at `t = 1` an explicit full-rank witness exists at GU's own `d = 4`, and it forces the base form to be CORANK ONE, i.e. a degenerate Carrollian-type base datum with a 3-dimensional structure group on `X^4`, not a metric. Both SIGNATURE-AMBIENT horns are carried and give identical numbers (`dim so(7,7) = dim so(9,5) = 91`, `dim Inv_{Spin(6,4)} = 32`, remainder `273`/`1183`), differing only in Killing signature `(49,42)` vs `(45,46)`. Two corrections are filed: OT-1's antisymmetric escape hatch is closed harder than expected (the invariant antisymmetric space at subscript `W` is EMPTY for `d >= 2`), and the fibre leg OT-2 carries at subscript `G` is typed at the CHIMERIC FRAME algebra `so(7,7)`, whereas the source's own inhomogeneous-gauge-group definition builds on `ad P_H` with `H = U(64,64)`, whose Killing form is DEGENERATE -- there the leg needs the trace form, and the unpaired remainder is at least `49148` on `X^4`, not `273`."
grade: "EXACT integer / fractions.Fraction arithmetic; all Lie brackets built in-file from structure constants and Jacobi-verified, nothing quoted; invariance systems solved as exact nullspaces over Q by sparse integer echelon; every EVASION certified by an explicit exact witness rather than by a bound; every OBSTRUCTION certified by an exact structural bound rather than by sampling; no numpy, no float constructed anywhere, `assert_no_float` sweeps the whole result dict. 131/131 checks, exit 0, via tests/channel-swings/joe_directed_bdb_subscript_lattice.py run from the repository root under _local/cas-venv. Split 95 [E] exact results, 24 [C] controls that must fire, 12 [R] reproductions of OT-1 / OT-2 / LA-11 facts reproduced BEFORE use. FAILURE PATH EXERCISED: fourteen planted false facts (ot1_dim, ot1_threshold, criterion, fibre_indep, contrary, base_natural, so64, inv32, remainder, table, anti, line, source_alg, domain) each drive exit 1 through --selftest. CONTRARY controls included and firing: an explicit t=1 witness of FULL rank 15/15 at d=4, a reductive-algebra t=1 evasion, a line-type translation subscript evasion, iso(2,1), abelian g, trivial V-module, a compact real form giving the identical lattice, and the trivial subscript at the vacuity boundary. NOT: a ledger edit, a verdict change, a physics derivation, a coefficient, a selection principle, an adjudication of SIGNATURE-AMBIENT, an adjudication between action parents, a claim that any GU object exists, or a claim that the ownership theorem is proved."
disposition: SUBSCRIPT_LATTICE_DECIDED__VERDICT_IS_A_FUNCTION_OF_ONE_INTEGER_dim_gVprime__FIBRE_SUBSCRIPT_PROVED_INERT_ON_ALL_THREE_DOMAINS__DOMAIN_FORK_LOCATED_ALPHA_BETA_GAMMA_NOT_ADJUDICATED_BD_A_CREDITED__GENERAL_NO_GO_ACROSS_THE_WHOLE_FIBRE_COLUMN__EVASION_SET_IS_EXACTLY_TRANSLATION_DEPTH_LE_1__EXPLICIT_FULL_RANK_WITNESS_AT_d_EQUALS_4__BASE_FORM_FORCED_CORANK_ONE_STABILIZER_3_ON_X4__NO_GL_OR_SL_NATURAL_BASE_DUALITY_AT_ANY_d__ANTISYMMETRIC_ESCAPE_HATCH_CLOSED_EMPTY_AT_W__BOTH_SIGNATURE_HORNS_IDENTICAL__OT2_FIBRE_LEG_RETYPED_TO_THE_SOURCE_DELTA1_ALGEBRA__REMAINDER_AT_LEAST_49148_ON_X4_THERE__ZERO_ROWS_ADVANCE
rows_touched_structurally: [LT-GR1, LT-GR6, LT-GR6b(proposed), LT-SM8, RA-E1, RA-E3, RA-G2, LT-SM3, AC-F1, AC-G1a]
rows_advanced: 0
rows_escalated: []
free_object_delta: 0
free_object_delta_note: "No new un-owned object is introduced. The `t = 1` evasion datum is a SHARPENING of LA-11's already-proposed leg (b), not an addition: it names the corank and the structure group leg (b) must have if it is to be reached at a subscript that retains any translation invariance at all. It takes nothing off any existing row."
depends_on:
  - lab/active-research/joe-directed/ownership-theorem/ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md
  - lab/active-research/joe-directed/ownership-theorem/ot2-lt-sm3b-is-not-an-ownership-row-and-the-cheapest-pair-is-the-terminal-pair-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md
  - lab/active-research/joe-directed/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/source-claim-register.yaml
  - lab/process/layer0-fork-registry.yaml
  - explorations/signature-fork-is-an-equivariance-defect-2026-08-08.md
  - explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md
scripts:
  - tests/channel-swings/joe_directed_bdb_subscript_lattice.py
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

Classification: `SOURCE_NATIVE_ROUTE`

**Why that classification and not another.** Every object computed here is one
GU declares for itself: the inhomogeneous gauge group `𝒲 = 𝒢 ⋉ Ω¹(ad P)` of the
source's own Definition 5.1, the adjoint bundle of the source's own principal
bundle, the chimeric frame algebra of the source's own signature chain, and the
one-form index on the observed base. No conventional comparator model is
constructed, imported, or compared against anywhere in this file: there is no
Higgs, no family index, no `126`, no anomaly selector, no vector-mass route. The
result is a statement about invariant bilinear forms on a GU-declared Lie
algebra. It is therefore source-native — and, being a **no-go about an internal
repository object**, it is an **internal-target** result and is *not* evidence
for or against anything Weinstein claims. That fence is repeated in §8 and is
not decorative.

---

# BD-B — the whole subscript lattice, decided

## Verdict first, unsoftened

**The obstruction is fibre-subscript-independent, and the only evasion is in a
coordinate that is not the fibre at all.**

OT-1 proved a no-go at one subscript, `𝒲`. LA-11 re-derived it and recorded that
the "NAMED subscript" fence is load-bearing. The natural next question — *is
there some other group under which the certifying pairing does exist?* — has an
exact answer, and it is not "try them one at a time":

> **Theorem (BD-B-1, probe §S2, `[E]`).** Let `𝔤` be a real Lie algebra,
> `V = Λ¹ ⊗ 𝔤` with `d = dim Λ¹`, and `𝔴 = 𝔤 ⋉ V` with `V` abelian. Let
> `𝔥 ⊆ 𝔴` be **any** subalgebra, and put `V' = 𝔥 ∩ V` and `W = 𝔤·V'`. Then
> every `𝔥`-invariant bilinear form `B` on `𝔴` — symmetric **or**
> antisymmetric — satisfies
>
> ```text
>       rank B  ≤  dim 𝔴  −  dim W  +  dim 𝔤 .
> ```
>
> Consequently a **nondegenerate** `𝔥`-invariant form exists only if
> `dim(𝔤·V') ≤ dim 𝔤`. The bound does not mention `π(𝔥) ⊆ 𝔤` — **the fibre
> subscript is inert.**

Two lines of proof, both in §2. For `𝔤` perfect and `V' = T ⊗ 𝔤`, `dim W = t·n`
with `t = dim T` and `n = dim 𝔤`, so the criterion becomes a statement about a
**single integer**:

| translation depth `t` | max rank | radical | verdict |
|---:|---|---|---|
| `0` | `dim 𝔴` | `0` | **EVADED** |
| `1` | `dim 𝔴` | `0` | **EVADED** (witness exhibited) |
| `2 ≤ t ≤ d` | `(d + 2 − t)·n` | `(t − 1)·n` | **OBSTRUCTED** |
| `t = d` | `2n` | `(d − 1)·n` | **OBSTRUCTED** — this row *is* OT-1 |

The bottom row reproduces OT-1 exactly (`max rank = 2 dim 𝔤`, radical
`(d−1) dim 𝔤`) and is now visible as one endpoint of a formula rather than as
an isolated fact.

**So the answer to the brief's fork is: BOTH, and they are on different axes.**

- Down the **fibre column** — `Spin_0(7,7)`, `Spin_0(9,5)`, `Spin(6,4)`,
  `U(64,64)`, the maximal compact `K`, `U(3,2)`, the Standard Model subgroup, a
  Cartan torus, the trivial group — the verdict **never moves**. This is a
  **general no-go**: shopping for a different fibre group cannot help, and the
  fourteen rows LA-11 attaches to the base-duality object are not waiting on a
  better fibre subscript.
- Along the **translation axis** there is a **named evasion route**, and it is
  exactly one step wide: `t ≤ 1`. At `t = 1` an explicit witness of full rank
  `(d+1)·dim 𝔤` exists at GU's own `d = 4`, and it is a **construction target**,
  not a hope.

And the evasion has a price that is itself a sharp result: at `t = 1` the base
form is **forced to be corank one** — a degenerate (Carrollian/Galilean-type)
base datum with a **3-dimensional** structure group on `X⁴`, against `6` for a
Lorentzian metric. A metric on `Λ¹` does **not** work at `t = 1`; it is planted
as a control and it breaks invariance.

**Certificate.** `131/131`, exit 0, split `[C] 24 · [E] 95 · [R] 12`, zero
floats swept, `14/14` planted false facts drive exit 1.

---

## 0. PREFLIGHT — six specialist lenses, run inline before computing

Standing rule: N lenses means N sections written here, never N subagents.

### Lens P1 — programme archivist: is this still the right target after today?

Re-derived, not inherited. Three artifacts landed today on this axis and each
moves the ranking:

| landed today | what it establishes | effect on this target |
|---|---|---|
| **OT-1** | the `O4` no-go at subscript `𝒲`; the named datum factors as (a) fibre form + (b) base duality | **creates** the target: OT-1's own Lens Q1 says *"ownership carries a mandatory group subscript that cannot be `𝒲`"* — which presupposes that some other subscript might work, and does not check |
| **LA-11** | independent from-scratch re-derivation; the trigger fence *"at a **NAMED** group subscript"* is load-bearing because *"fix the subscript to `𝒲` and the satisfying set **is** empty"* | **sharpens** it: LA-11 makes the subscript an explicit free parameter of a proposed ledger row, so the row's satisfiability is *literally* a function of the subscript. Deciding the lattice decides the row's non-emptiness |
| **OT-2** | *"the Killing form supplies `O4`'s fibre leg at subscript `𝒢`"*, carried as an **available datum**, with the composite explicitly refused because leg (b) is unsupplied | **splits** it: OT-2 already occupies one lattice point and reports it as half-supplied. One point is not a lattice |
| **PHI-2** | (phi-reduction channel, committed today) | no bearing: the reduction rank question is upstream of the pairing and does not change which groups can carry it |

**What moved in the ranking, and why.** Before today the obvious next move on
this axis was *build leg (b)* — write the base duality. LA-11 wrote the row for
it and typed it `NEEDS / MISSING_CONSTRUCTION`. That move is now **strictly
worse than deciding the lattice first**, for a reason that is cheap to state and
expensive to discover late: *leg (b) has a different shape at different
subscripts.* §5 shows that at `t = 1` the base form must be **corank one** and
at `t = 0` it may be a metric. Building a Lorentzian metric first and then
discovering it is the wrong object at the only subscript that retains any
translation invariance would be exactly the queue defect
`lab/process/layer0-fork-registry.yaml` was created to surface. So the lattice
moves **ahead** of leg (b), and this artifact is the reordering.

**What did not move.** The ledger is byte-identical at `a148ed80`; nothing here
measures a moved target.

### Lens P2 — Lie theorist (real forms, Killing forms): predict the mechanism

OT-1's proof of the `V–V` vanishing uses `𝔤·V = V`, which for `𝔤` semisimple is
`Λ¹ ⊗ [𝔤,𝔤] = Λ¹ ⊗ 𝔤`. LA-11's Lens P4 already identified that the *module
structure*, not the dimension count, is the killer. **The lens's prediction,
written before computing:** the whole theorem is controlled by the single
subspace `𝔤·(𝔥 ∩ V)`, so shrinking the *fibre* part of the subscript cannot
help — it does not appear in that expression — while shrinking the *translation*
part must help, because it shrinks `V'` directly. §2 confirms this and turns it
into an exact rank bound. The prediction is what makes the result interpretable:
the obstruction was never about which group acts on the fibre.

### Lens P3 — invariant theorist: predict the threshold, and get it wrong

**The lens's prediction, recorded before computing and then REFUTED by the
computation.** I predicted the binding constraint would be the *isotropy* bound:
`V'` totally isotropic forces `dim(𝔤·V') ≤ (dim 𝔴)/2`, giving a centre-fraction
criterion `dim 𝔷(𝔤) ≥ dim 𝔤 ·(d−1)/(2d)` and a threshold `t ≤ (d+1)/2`. **Both
are wrong.** The exact sweep obstructs `gl(2,ℝ)` at `d = 2`, which the isotropy
guess passes; and it obstructs `t = 2` at `d = 3`, which the isotropy guess
passes. The correct bound is the *orthogonality* bound `𝔤·V' ⊆ V^{⊥_B}`, whose
right-hand side has dimension `dim 𝔤` rather than half of `dim 𝔴`, giving
`t ≤ 1` and centre-fraction `(d−1)/d`. The wrong guess is planted as a firing
control (`[C]`, probe §S2) precisely so this file cannot be read as if the
sharper bound had been obvious.

### Lens P4 — evidence law: grep before claiming novelty, and price the prior art

Exact-substring sweeps over `explorations/`, `lab/`, `canon/`:

| string | hits |
|---|---:|
| `translation depth`, `subscript lattice`, `admissible subscript`, `fibre subscript`, `subscript-independent`, `corank-one base`, `perfectness criterion`, `line-type subscript`, `Carrollian` | **0 each** |
| `OWNED_K` | OT-1 + ledger versions |
| `Ad-invariant nondegenerate` | LA-11 only |
| `Killing form is degenerate` | OT-1 only |

**Per the standing rule that is not evidence of novelty.** The substantive
credits are: OT-1 owns the theorem at `𝒲`, the `O3a/O3b` split, the mandatory
subscript, and the `iso(2,1)` control; LA-11 owns the independent re-derivation,
the module-structure control, and the `dim 𝔰𝔬(6,4) = 45` correction; OT-2 owns
the fibre-leg-at-`𝒢` datum and its refusal as a composite; CG-1 owns `Δ1..Δ5`;
`AUDIT-noncompact-compact-reduction-EXTERNAL` owns the price on `K`. The novelty
claimed here is narrow and is stated in §8: the rank bound valid at *every*
subscript, the inertness of the fibre coordinate, the exact `t ≤ 1` dichotomy
with its witness, the corank-one forcing on leg (b), the emptiness of the
antisymmetric invariant space at `𝒲`, and the retyping of the fibre algebra to
the source's own `Δ1` bundle.

### Lens P5 — bilinear-form classifier (Witt/Sylvester): what "nondegenerate" costs

A nondegenerate form on `𝔴` makes `V^{⊥_B}` exactly `dim 𝔤`-dimensional. That is
the whole content of Theorem BD-B-1: the invariance constraint dumps `𝔤·V'` into
`V^{⊥_B}`, and a `dim 𝔤`-dimensional box cannot hold more than `dim 𝔤`
dimensions. Witt's theorem then says the *only* freedom left is how the
hyperbolic pair is arranged, which is why the `t = 1` witness in §4 is forced
into the shape `[[λκ, κ], [κ, 0]] ⊕ (q_U ⊗ κ)` — one hyperbolic block pairing
`𝔤` against `L ⊗ 𝔤`, and an ordinary block on what is left. **The lens's
operational demand:** every EVASION verdict must be certified by an explicit
witness with an exact rank, never by "the bound permits it." §4 obeys this;
every evasion row in the table has a witness.

### Lens P6 — honesty auditor: the four specific vacuities to guard

1. **Vacuity by detector.** A sweep that reports "obstructed" everywhere cannot
   distinguish *no evasion exists* from *my detector never fires*. Guarded by
   eight CONTRARY controls that must fire, including one at GU's own `d = 4`
   with an explicit full-rank witness (`[C]`, §4).
2. **Vacuity by emptiness.** "No nondegenerate element" is trivial if the
   invariant space is empty. Checked nonempty at every symmetric row. The
   antisymmetric rows at `t = d` **are** empty, and that is reported as content
   with its own non-emptiness control at `t ≤ 1` rather than folded into the
   symmetric statement.
3. **Vacuity by convenience.** A subscript lattice can be made to say anything
   by choosing which groups are "admissible." §1 states the criterion first and
   §6 attacks it; the criterion is the load-bearing part of this result and is
   presented as such.
4. **Vacuity by scale.** No `91`-dimensional invariance system is solved here.
   Every GU-scale row is an *integer instantiation of a fixture-free bound*, and
   §6 says so in the same words rather than in a footnote.

---

## 1. THE ADMISSIBILITY CRITERION — stated before the sweep, and load-bearing

Clause `O4` reports `OWNED_H`. `H` is not a free label: it is the group under
which the identification `Lie(𝒲)^* ≅ Lie(𝒲)` is asserted to hold. So the
question "which `H` are admissible" is the question "which identifications does
GU actually own." Three clauses, all required, plus a price column.

> ### `ADM(H)` — admissible subscript
>
> **`ADM-1` — SUPPLY.** `H` is supplied by GU's own declared structure: it is
> the structure group of a declared bundle, a group in a printed reduction
> chain, a declared symmetry of the declared functional, or the stabilizer of a
> datum an existing ledger row already demands.
> *Fails when:* `H` is chosen because it makes the algebra work. That failure is
> the entire reason this clause exists.
>
> **`ADM-2` — ACTION.** `H` acts on `Lie(𝒲) = Ω⁰(ad P) ⊕ Ω¹(ad P)` by a
> **declared** action — `Ad` for subgroups of `𝒲`, or the natural action on the
> one-form index for subgroups of the base structure group — so that
> "`H`-invariant form on `Lie(𝒲)`" is well-posed without inventing anything.
>
> **`ADM-3` — FIBREWISE CLOSURE.** `H` acts pointwise on the fibre (or by base
> transformations on the `Λ¹` index), so OT-1 §2's pointwise-to-integral step
> applies verbatim and the finite-dimensional computation reaches the
> infinite-dimensional statement by the same single step OT-1 used.
>
> **PRICE.** Every admissible `H` additionally carries one of:
> `FREE` (a symmetry of the declared structure), `REDUCTION_EXTERNAL` (a
> declared-but-underived reduction — `AUDIT`'s price), `EXTRA_DATUM` (the
> stabilizer of an object no row supplies), or `VACUOUS` (`H = 1`).

**Why this is the right criterion, argued against the two obvious alternatives.**

*Too narrow:* "`H` must be a symmetry of the action." This excludes the maximal
compact `K`, which the source itself declares as a reduction and which `CG-1`
and `AUDIT` already price. A criterion that cannot even *name* the repository's
existing `OWNED_K` verdict is not a criterion for this repository.

*Too wide:* "`H` may be any subgroup." Then `H = 1` is admissible, every form is
invariant, the obstruction "evades," and the result is worthless. `ADM-1` is
what stops that, and `H = 1` is retained explicitly as the **vacuity boundary
row** so the reader can see where the criterion bites.

**The criterion's real work is the PRICE column.** Every group in the fibre
column is admissible under `ADM-1..3`; what distinguishes them is what you pay.
And the central finding of this artifact is that **the price column is the only
thing that varies down the fibre column** — the mathematics does not vary at
all. That is a stronger and less comfortable statement than "some subscripts
work," and it is the one the computation supports.

---

## 2. THE THEOREM — two lines, valid at every subscript

Let `𝔴 = 𝔤 ⊕ V`, `V = Λ¹ ⊗ 𝔤` abelian, `[X, α⊗a] = α⊗[X,a]`. Let `𝔥 ⊆ 𝔴` be a
subalgebra, `V' = 𝔥 ∩ V`, and let `B` be `𝔥`-invariant:
`B([z,x],y) + B(x,[z,y]) = 0` for all `z ∈ 𝔥` and **all** `x, y ∈ 𝔴`.

**Step 1 (the only step that matters).** Take `z = w ∈ V'`, `x = X ∈ 𝔤`,
`y = v ∈ V`. Then `[w,X] = −X·w ∈ V` and `[w,v] = 0`, so

```text
        B(X·w, v) = 0      for all X ∈ 𝔤, w ∈ V', v ∈ V,
```

i.e. `𝔤·V' ⊆ V^{⊥_B}`. Note `x` and `y` range over all of `𝔴`, so `X` is
**unrestricted** — the fibre part of `𝔥` never enters.

**Step 2.** The rows of `B` indexed by `W := 𝔤·V'` are supported in the `𝔤`
columns only, so they span at most `dim 𝔤` dimensions. Hence

```text
        rank B  ≤  dim 𝔤  +  (dim 𝔴 − dim W).
```

Nondegeneracy needs `rank B = dim 𝔴`, i.e. **`dim W ≤ dim 𝔤`**. ∎

Both steps use only the bracket, never symmetry of `B`, so the bound holds
verbatim for antisymmetric `B` (§4.3).

**Instantiation for `𝔤` perfect.** If `𝔤 = [𝔤,𝔤]` and `V' = T ⊗ 𝔤` with
`t = dim T`, then `W = T ⊗ [𝔤,𝔤] = T ⊗ 𝔤`, `dim W = t·n`, and the criterion is

```text
        nondegenerate   ⟺   t ≤ 1 .
```

**Instantiation at full translations (`t = d`), general `𝔤`.** `dim W = d·dim[𝔤,𝔤]`, so

```text
        nondegenerate at subscript 𝒲   ⟺   d · dim[𝔤,𝔤] ≤ dim 𝔤 ,
```

i.e. the centre must be a `(d−1)/d` fraction of `𝔤`. At `d = 4` that is three
quarters of the algebra. `𝔤` semisimple gives `d ≤ 1` — **OT-1's threshold,
recovered as a corollary.**

### 2.1 OT-1 re-derived from scratch, and it survives without correction

Nothing quoted. `𝔰𝔩(2,ℝ)`, `𝔰𝔩(3,ℝ)`, `𝔰𝔲(2)`, `𝔤𝔩(2,ℝ)` and `𝔦𝔰𝔬(2,1)` are
built from structure constants, Jacobi is verified, `𝔴` is assembled, and the
invariance system is solved as an exact nullspace over `ℚ`.

```text
subscript W,  g = sl(2,R),  n = 3

 d   dim w   dim Inv   V-V block   max rank   nondegenerate?
 0       3         1        --            3        YES
 1       6         2       zero           6        YES
 2       9         3       zero           6        no
 3      12         4       zero           6        no
 4      15         5       zero           6        no
```

Every OT-1/LA-11 claim reproduces: **`dim = d+1`**, **identically zero `V–V`
block**, **max rank exactly `2 dim 𝔤`**, **threshold exactly `d = 2`**, radical
`(d−1)·dim 𝔤`. `𝔰𝔩(3,ℝ)` reproduces `d+1` and `2 dim 𝔤` at `d = 1, 2`, so the
count is not an `𝔰𝔩(2)` accident. **No correction to OT-1's theorem is filed.**

Controls, each firing: `iso(2,1)` (nondegenerate metric exists, Killing rank 3
of 6), abelian `𝔤`, trivial `V`-module, module-structure discrimination, and a
Jacobi mutation that must fail Jacobi.

### 2.2 The exact formulae the theorem produces

For `𝔤` absolutely simple and fibre subscript `𝒢` (probe §S2, `[E]`, verified at
`d = 2,3,4` and `𝔤 = 𝔰𝔩(2,ℝ), 𝔰𝔩(3,ℝ), 𝔰𝔲(2)`):

```text
   max rank         =  min( dim w , (d + 2 - t) · dim g )
   radical          =  max( 0 , (t - 1) · dim g )
   dim Inv          =  1 + d + (d - t)(d - t + 1)/2
```

At `t = d`: `dim Inv = d+1`, max rank `2n`, radical `(d−1)n` — **OT-1 exactly**.
At `t = 0`: `dim Inv = 1 + d + d(d+1)/2`, full rank. The bound is **attained at
every depth**, verified by explicit witnesses at `d = 4` (`[E]`).

---

## 3. THE SWEEP — the complete subscript table, with an exact verdict per row

Columns: `t` is the translation depth; **fibre** is `π(𝔥) ⊆ 𝔤`; **verdict** is
`EVADED` / `OBSTRUCTED` for the composite pairing on `Lie(𝒲)`; **fibre leg** is
whether an `Ad(H₀)`-invariant nondegenerate form on `ad P` exists on its own.

| # | subscript `H` | supply (`ADM-1`) | `t` | fibre leg on `ad P` | **composite verdict** | price |
|---:|---|---|---:|---|---|---|
| 1 | `𝒲 = 𝒢 ⋉ Ω¹(ad P)` | Def. 5.1 / `Δ1` | `d` | available | **OBSTRUCTED** — radical `(d−1)n` | FREE |
| 2 | `𝒢 = Γ(Ad P_H)`, `H = U(64,64)` | Def. 5.1 / `P_H` | `0` | available (trace form; **not** Killing) | **EVADED** | FREE |
| 3 | `Spin_0(7,7)` fibrewise (horn A) | signature chain | `0` | Killing, unique, sig `(49,42)` | **EVADED** | FREE |
| 4 | `Spin_0(9,5)` fibrewise (horn B) | `SIGNATURE-AMBIENT` | `0` | Killing, unique, sig `(45,46)` | **EVADED** | FREE |
| 5 | `Spin(6,4)` internal (**shared by both horns**) | printed chain | `0` | 32-parameter family | **EVADED** | FREE |
| 6 | `Spin(1,3)` base Lorentz | printed chain | `0` | available | **EVADED** | FREE |
| 7 | `K` maximal compact | declared reduction | `0` | 3-parameter family, **positive-definite member exists** | **EVADED** | `REDUCTION_EXTERNAL` |
| 8 | `U(3,2)` / `SU(3,2)` | printed reduction | `0` | available | **EVADED** | `REDUCTION_EXTERNAL` |
| 9 | `SU(3)×SU(2)×U(1)` | printed intersection | `0` | available | **EVADED** | `REDUCTION_EXTERNAL` |
| 10 | Cartan torus of `𝒢` | max-torus of a declared group | `0` | available | **EVADED** | FREE |
| 11 | `𝒢 ⋉ (L ⊗ ad P)` | stabilizer of leg (b) | `1` | available | **EVADED — witness exhibited, §4** | `EXTRA_DATUM` |
| 12 | `Z_𝒢(a₀) ⋉ ⟨α ⊗ a₀⟩` (line type) | stabilizer of a fixed `ad`-valued one-form | `1` | available | **EVADED** | `EXTRA_DATUM` |
| 13 | `𝒢 ⋉ (T ⊗ ad P)`, `2 ≤ t ≤ d−1` | partial translation | `t` | available | **OBSTRUCTED** — radical `(t−1)n` | `EXTRA_DATUM` |
| 14 | `K ⋉ Ω¹(ad P)` | reduction + `Δ1` | `d` | 3-parameter family | **OBSTRUCTED** | `REDUCTION_EXTERNAL` |
| 15 | `Ω¹(ad P)` alone (no fibre group) | normal subgroup of `Δ1` | `d` | n/a | **OBSTRUCTED** | FREE |
| 16 | trivial group `1` | vacuity boundary | `0` | trivially available | **EVADED** (vacuously) | `VACUOUS` |
| 17 | `𝒲 ⋊ Diff(X)` | base naturality | `d` | available | **OBSTRUCTED twice** — by `t` *and* by §5 | FREE |
| 18 | `𝒢 ⋊ Diff(X)` | base naturality | `0` | available | **OBSTRUCTED by the BASE leg** (§5) | FREE |

**Read the table by columns, not rows.** Rows 2–10 and 16 differ in fibre group
by every measure that matters representation-theoretically — split versus
quasi-split real forms, non-compact versus compact, simple versus reductive,
`dim 𝔤` from `3` to `16384` — and the composite verdict is **identical**. Rows
1, 14, 15 differ in fibre group from "all of `𝒢`" to "no fibre group at all" and
the composite verdict is **identical**. The verdict is a function of `t` alone.

### 3.1 Both `SIGNATURE-AMBIENT` horns, carried side by side

The brief's instruction is honored: neither horn is picked.

```text
                          horn A (7,7)      horn B (9,5)
 dim g                          91                91
 Killing signature          (49, 42)          (45, 46)
 maximal compact         Spin(7)xSpin(7)   Spin(9)xSpin(5)
 dim Inv at G                    1                 1
 dim Inv at K                    3                 3
 internal subgroup          Spin(6,4)         Spin(6,4)     <- SHARED
 dim Inv at Spin(6,4)           32                32
 branching                6 + 45 + 40       6 + 45 + 40 = 91
 remainder on X^4  (t=4)       273               273
 remainder on Y^14 (t=14)     1183              1183
```

`dim 𝔰𝔬(7,7) = dim 𝔰𝔬(9,5) = 91` because both are real forms of `𝔰𝔬(14,ℂ)`;
`dim 𝔰𝔬(6,4) = 45` (LA-11's correction, **independently confirmed**). Both horns
branch to the shared internal `𝔰𝔬(6,4)` with a `40`-dimensional mixed block
(`(1,3)+(6,4)` on horn A, `(3,1)+(6,4)` on horn B), giving the identical
isotypic pattern `trivial⊕⁶ ⊕ adjoint ⊕ vector⊕⁴` and hence
`dim Inv = 21 + 1 + 10 = 32` on both. **`SIGNATURE-AMBIENT` is orthogonal to
this result and is not touched by it.**

### 3.2 GU-scale instantiation

```text
so(7,7) on X^4     dim w = 455    t=0,1 -> rank 455, radical 0   (EVADED)
                                  t=2   -> rank 364, radical 91
                                  t=4   -> rank 182, radical 273  (OT-1)
so(7,7) on Y^14    dim w = 1365   t=2   -> rank 1274, radical 91
                                  t=14  -> rank 182, radical 1183 (OT-1)
so(6,4) on X^4     dim w = 225    t=4   -> rank  90, radical 135  (LA-11)
so(6,4) on Y^14    dim w = 675    t=14  -> rank  90, radical 585  (LA-11)
```

---

## 4. THE CONTRARY CONTROL — the evasion is real and is exhibited

A sweep that only ever says "obstructed" cannot distinguish a genuine no-go from
a broken detector. The brief demands a case where the obstruction provably does
**not** hold. Here it is, at GU's own base dimension.

### 4.1 The `t = 1` witness

Subscript `𝔥 = 𝔤 ⋉ (L ⊗ 𝔤)` with `L ⊆ Λ¹` a line, `d = 4`. Choose a covector
`c ∈ (Λ¹)^*` with `c|_L ≠ 0`, a symmetric `q` on `Λ¹` with `rad(q) = L`, and set

```text
   B(X, Y)              =  lambda * kappa(X, Y)              (lambda free)
   B(X, alpha (x) a)    =  c(alpha) * kappa(X, a)
   B(alpha(x)a, beta(x)b) =  q(alpha, beta) * kappa(a, b)
```

In the block order `(𝔤, L⊗𝔤, U⊗𝔤)` with `U` a complement to `L`:

```text
        [ lambda*kappa      kappa        0        ]
        [ kappa             0            0        ]
        [ 0                 0        q_U (x) kappa]
```

Verified `𝔥`-invariant exactly, and of **rank `15/15` at `d = 4`** — full rank,
`= (d+1)·dim 𝔤`. Verified again at a second value of `λ`, so it is a family and
not a point. The same form is verified **not** `𝒲`-invariant, so the control
discriminates rather than merely passing.

Three further contrary controls fire:

- **reductive fibre algebra** `𝔤𝔩(2,ℝ)` at `d = 4`, `t = 1`: **EVADED**, rank
  `20/20`. This is what licenses the `U(64,64)` row of the table rather than
  extrapolating to it.
- **line-type subscript** `Z_𝔤(a₀) ⋉ ⟨α ⊗ a₀⟩` at `d = 4`: `dim(𝔤·V') = 2 ≤ 3`,
  rank `15/15`, **EVADED**. So the evasion set is genuinely larger than the
  single split family — any subscript whose translation content propagates to at
  most `dim 𝔤` dimensions evades.
- **compact real form** `𝔰𝔲(2)` at `d = 4`: max ranks `15, 15, 12, 6` at
  `t = 0,1,2,4` — **identical** to `𝔰𝔩(2,ℝ)`. Definiteness of the fibre form is
  irrelevant to the composite.

### 4.2 The price of the evasion: leg (b) is forced to be corank one

The invariance constraint at `t = 1` forces `q(L, Λ¹) = 0`. So `q` has rank
exactly `d − 1`. **A nondegenerate `q` — an ordinary base metric — is planted as
a control and it breaks invariance.** The datum leg (b) must supply at `t = 1`
is therefore:

> a **line** `L ⊆ Λ¹`, a **covector** `c` transversal to it, and a symmetric
> form `q` of **corank exactly one** with `rad(q) = L` —
> i.e. a degenerate, Carrollian/Galilean-type base structure, **not** a metric.

Its exact stabilizer in `GL(Λ¹)` is computed, not asserted:

```text
                                      X^4        Y^14
   GL(Lambda^1)                        16         196
   metric (t = 0 route)                 6          91
   corank-one datum (t = 1 route)       3          78     = (d-1)(d-2)/2
```

**The `t = 1` route breaks the base structure group harder than a metric does.**
That is a real cost and it is the honest headline of the evasion: the only
subscript that keeps *any* translation invariance buys it by giving up more base
symmetry than a metric would.

### 4.3 OT-1's antisymmetric escape hatch is CLOSED, and closed harder

OT-1 §5 Lens Q1 names an escape it does not touch: *"a pairing that is not
symmetric."* Computed here (`[E]`, probe §S3b). **My prediction was that the
antisymmetric lattice would be identical. It is not — it is strictly stricter.**

```text
 ANTISYMMETRIC invariant forms,  g = sl(2,R),  n = 3

  d   t    dim Inv   max rank   nondegenerate?
  2   0        3          6         no
  2   1        1          6         no
  2   2        0          0         no      <- EMPTY
  3   0        6         12        YES
  3   1        3          6         no
  3   3        0          0         no      <- EMPTY
  4   0       10         12         no
  4   4        0          0         no      <- EMPTY
```

**At subscript `𝒲` the invariant antisymmetric space is EMPTY for `d ≥ 2`** —
not merely degenerate. The symmetric case at least had a `(d+1)`-dimensional
space to fail in; the antisymmetric case has nothing at all. Non-emptiness at
`t ≤ 1` is checked as a control, so the emptiness is content and not a bug.

At GU scale a second, cruder obstruction also applies: `dim 𝔴` is **odd** on
every `𝔰𝔬(∗)` row (`455`, `1365`, `225`, `675`), so no nondegenerate
antisymmetric form exists there at **any** subscript, by parity alone.

---

## 5. THE BASE LEG — there is no natural duality, at any `d`

The `t = 0` evasion (row 3 of the table: subscript `𝒢`) still needs leg (b): a
form `q` on `Λ¹`. Ask whether GU gets one for free from base naturality.

```text
  dim { q symmetric on Lambda^1 : invariant under ... }

              d = 2   d = 3   d = 4   d = 14
   GL(d,R)        0       0       0        0
   SL(d,R)        0       0       0        0
   SO(p,q)        1       1       1        1     <- control, fires
```

`GL(Λ¹)`-invariance forces `2q = 0` immediately; `SL(Λ¹)` (volume-preserving
transformations) kills it too, for every `d ≥ 2`. The discrimination control —
the same machinery run against `𝔰𝔬(1,3)`, `𝔰𝔬(4)`, `𝔰𝔬(3,11)`, `𝔰𝔬(7,7)` —
returns exactly `1` each time, so the window is not a window that never fires.

**Consequence, stated exactly.** Leg (b) is *necessarily* a broken-naturality
datum. There is no diffeomorphism-natural base duality to be found; any leg (b)
reduces the base structure group from `GL(d)` to `O(p,q)` at best, and to the
corank-one stabilizer at `t = 1`. Rows 17 and 18 of the table are therefore
obstructed *for a second, independent reason* — row 18 despite having `t = 0`.
This is exactly why LA-11's proposed row types leg (b) `MISSING_CONSTRUCTION`
and not `MISSING_PROOF`: there is nothing to prove, there is only something to
supply.

---

## 5b. THE DOMAIN FORK — which object this lattice actually decides

**Raised concurrently and independently by `BD-A` (same directory, same day).
It is a real catch, it is verified here from my own structure constants, and it
is credited rather than absorbed.** Three different objects have all been called
"the pairing," and they give three different answers.

```text
                                                  d=1    d=2    d=3    d=4
 (alpha)  symmetric form on the ALGEBRA w = g (+) V
          dim Inv                                   2      3      4      5
          max rank / dim w                        6/6    6/9   6/12   6/15
          nondegenerate?                          YES     no     no     no

 (gamma)  symmetric form on the MODULE V alone
          dim Inv                                   1      3      6     10
          max rank / dim V                        3/3    6/6    9/9  12/12
          nondegenerate?                          YES    YES    YES    YES

 (beta)   pairing V x g -> R  (Lambda^1 (x) ad P -> (ad P)^*)
          max rank                                  3      3      3      3
          left radical = (d-1) dim g                0      3      6      9
```

- **`(α)` is OT-1's theorem and is what §2–§4 of this artifact decide.** It is
  the object clause `O4` names — the identification `Lie(𝒲)^* ≅ Lie(𝒲)`.
- **`(γ)` is what LA-11's proposed `revival_trigger` literally asks for** — *"a
  pairing **on** `Λ¹ ⊗ ad P`."* On `V` the translations act **trivially**
  (`V` is abelian), so `𝒲`-invariance *is* `𝒢`-invariance and a nondegenerate
  member exists at every `d`. BD-A is right, and it is verified here
  independently: `dim Inv = d(d+1)/2` and max rank is full at `d = 1,2,3,4`.
- **`(β)` is OT-1 §2's "named datum" as literally written** — a map
  `Λ¹ ⊗ ad P → (ad P)^*`. A perfect pairing needs `dim V = dim 𝔤`, so it is
  impossible for `d ≥ 2` **at every subscript**, by a pure dimension count.
  This is the "nearly vacuous" horn LA-11's Lens P4 named.

**Two things follow that neither artifact has alone.**

1. **`(α)` and `(β)` agree on the number.** The `(α)` radical and the `(β)`
   left-radical are the *same integer* `(d−1)·dim 𝔤` at every `d` (`[E]`). So
   OT-1's `273` has two independent derivations that coincide — it is not an
   artefact of the algebra-domain reading.
2. **The subscript is inert on all three domains, for three different reasons.**
   On `(α)` because the bound never mentions `π(𝔥)`; on `(γ)` because the
   translations impose no condition at all; on `(β)` because the count is
   dimensional. **The DOMAIN, not the subscript, is what decides.** That is a
   sharper form of this artifact's headline than §3's, and it is the version
   that should be carried forward.

**What this costs my result, stated plainly.** If the operative object for
ownership is `(γ)`, my `t ≤ 1` lattice decides a question nobody is asking, and
the honest content of this file shrinks to §5 (the base leg) plus the `(β)`
dimension count. I do not adjudicate the domain question here — BD-A argues for
`(γ)` from LA-11's trigger text, and OT-1's clause `O4` argues for `(α)` from
its own statement about `Lie(𝒲)^*`. **Both readings are in the repository and
the disagreement is now exactly located**, which is more useful than either
artifact picking a side. What is settled either way: **the fibre subscript is
inert on all three domains**, so the fibre column is closed regardless of how
the domain fork resolves.

**Credit where §5 is concerned.** `BD-C` (same directory, same day) reaches the
base-leg obstruction independently by a different and simpler route — the
scalings `λ·I` sit inside every declared structure group on `X⁴`, and the space
of `λI`-invariant symmetric forms on `ℝ⁴` is zero-dimensional. My §5 computes
the full `GL`/`SL` statement at `d = 2,3,4,14` with an `SO(p,q)` discrimination
control, which subsumes it; but the two were produced concurrently and **§5
should not be read as novel against `BD-C`.**

---

## 6. HOSTILE REVIEW — inline, on my own result

### 6.1 Is the enumeration COMPLETE, and by what criterion?

**It is complete, but not in the way the word suggests, and the difference
matters.** I did not enumerate the subgroups of `𝒲`. That set is not finite and
I did not attempt it. What I enumerated is the **fibres of the verdict map**:

> Theorem BD-B-1 shows the verdict is a function of the single integer
> `m = dim(𝔤·(𝔥 ∩ V))`, which ranges over `{0, …, d·dim 𝔤}`. The verdict is
> `EVADED` for `m ≤ dim 𝔤` and `OBSTRUCTED` for `m > dim 𝔤`. Both classes are
> decided: the second by an exact bound, the first by explicit witnesses.

So every conceivable admissible subgroup lands in a class this artifact has
already decided, whether or not it appears in the table. **That** is the
completeness claim, and it is the strongest one available. The table is an
illustration of the classes, not the proof of coverage.

### 6.2 Four ways this is not complete, stated blunt

1. **Disconnected subscripts are only half-covered.** For `H` with identity
   component `H⁰`, `Inv_H ⊆ Inv_{H⁰}`, so the *necessary* bound (and every
   OBSTRUCTED verdict) survives verbatim — it uses only the Lie algebra. But my
   evasion witnesses are built from `c` and `q` on `Λ¹`, and a component group
   acting nontrivially on `Λ¹` can destroy them. **The EVADED column is
   `connected`-scoped. The OBSTRUCTED column is not.** I did not check a single
   disconnected case and I am not claiming one.

2. **Sufficiency is witness-scoped, not proved in general.** Necessity
   (`dim(𝔤·V') ≤ dim 𝔤`) is proved for *every* subalgebra. Sufficiency is
   certified by explicit witness for `𝔥 = 𝔥₀ ⋉ (T ⊗ 𝔤)` and for the line type.
   A subalgebra whose translation part is neither of these could in principle
   satisfy the bound and still fail. I believe it cannot; I did not prove it.

3. **The GU-scale rows are instantiated arithmetic, not solved systems.** The
   largest invariance system solved exactly is `dim 𝔴 = 40` (`𝔰𝔩(3,ℝ)`, `d = 4`
   grid) with `𝔰𝔩(2,ℝ)`/`𝔰𝔲(2)`/`𝔤𝔩(2,ℝ)` carrying the sweep. Nobody solved a
   `455 × 455` nullspace here. This is legitimate because Theorem BD-B-1's proof
   is two fixture-free lines — but a reader who wants machine-verified `91`s
   will not find them and should not pretend to.

4. **The pointwise-to-integral step is inherited, not re-proved.** OT-1 §2's
   scope paragraph is carried verbatim. If a `𝒢`-invariant pairing exists that
   is not of the form `∫ B_x dvol`, nothing here reaches it. OT-1 flagged this
   as attack vector 3 on itself; it is attack vector 4 on this file too, and it
   is the same hole.

5. **There is a fourth coordinate I did not know about when I started, and it
   dominates the other three: the DOMAIN.** §5b. My completeness argument is
   complete *within* domain `(α)`. Across domains it is not a completeness
   argument at all — it is a location argument, and the location is now exact.
   BD-A found this concurrently and independently; had it not, this file would
   have shipped a complete sweep of one of three possible objects while
   presenting it as the sweep. That is worth recording as a near-miss, not
   smoothing over.

### 6.3 The single cheapest way to kill this artifact

**Delete `O3b`.** OT-1's own Lens Q2 steelman: `Ω¹(ad P)` is not a symmetry to
be equivariant *under*, it is the space the field moves *in*. If that reading is
right, the honest subscript is `𝒢`, `t = 0`, and this entire lattice collapses
to row 3 — everything evades, the no-go evaporates, and the only surviving
content is §5's base-leg result. **I cannot refute this and I will not pretend
to.** What I can say is that my result makes the stakes of that fork sharply
quantitative for the first time: the fork is now worth exactly
`(d−1)·dim 𝔤 = 273` unpaired directions on `X⁴`, and the two horns of it are
`t = d` versus `t = 0`. That is a better-posed fork than it was this morning,
and it should be attacked first.

### 6.4 The second-cheapest attack, and it is aimed at §1

**Attack `ADM-1`.** My table's most consequential row is #2 — the source's own
`𝒢`, on `ad P_H` with `H = U(64,64)`. If a reader argues that the operative
fibre algebra is instead the chimeric `𝔰𝔬(7,7)` (as OT-1 and OT-2 both assume),
then my correction in §7 evaporates and the remainder stays `273`. Both readings
are in the repository. I report the divergence rather than adjudicating it,
because adjudicating it is a Layer-0 typing decision this channel does not own.
The **composite verdict is the same on either reading**, which is why the
divergence changes numbers and not conclusions — but it changes them by two
orders of magnitude, and that should not be buried.

### 6.5 Weakest seam in my own construction

**The `Diff(X)` rows (17, 18).** I model base naturality by `GL(Λ¹)`-invariance
of `q`, which is the linearised, pointwise version. Full `Diff(X)`-naturality is
a statement about natural bundles and I did not formulate it. The pointwise
computation is exact and correct for what it computes; whether it is the right
model of "the pairing should not depend on a choice of base structure" is a
modelling decision I made and am flagging, not proving.

### 6.6 What I checked so a reader does not have to re-attack it

Do **not** attack the invariant-form computations. They carry: four
hypothesis-isolating controls that each fire, a Jacobi mutation control, a
non-vacuity control at every symmetric row, a module-structure discrimination
control, an exact `H¹(𝔤, Λ¹⊗ad) = 0` computation at `d = 2,3,4` (so all
complements to `V` are conjugate and twisted subscripts give no new verdict), an
explicit twisted-complement control confirming it, a compact-real-form control,
a reductive-algebra control, and a recorded refutation of my own preflight
guess. Every evasion is a witness; every obstruction is a bound.

---

## 7. CORRECTIONS FILED

| filed | verdict here |
|---|---|
| **OT-1 §2**, the invariant-form theorem at subscript `𝒲` | **SURVIVES an independent from-scratch re-derivation with no correction.** `dim = d+1`, zero `V–V`, max rank `2 dim 𝔤`, threshold exactly `d = 2`, radical `(d−1) dim 𝔤`: all reproduced exactly. It is now a special case (`t = d`) of a formula valid at every subscript |
| **OT-1 §5 Lens Q1**, *"a second escape I cannot exclude: a pairing that is not symmetric"* | **CLOSED, and closed harder than expected.** At subscript `𝒲` with `d ≥ 2` the invariant **antisymmetric** space is **EMPTY** (dimension `0`), not merely degenerate. At GU scale `dim 𝔴` is odd on every `𝔰𝔬(∗)` row, so parity kills it at every subscript there too |
| **OT-1 §2 / LA-11 §2.1**, `dim 𝔰𝔬(6,4) = 45` not `91` | **CONFIRMED independently.** `dim 𝔰𝔬(7,7) = dim 𝔰𝔬(9,5) = 91`, `dim 𝔰𝔬(6,4) = 45`; remainders `273`/`1183` and `135`/`585` all reproduce |
| **OT-2**, *"the Killing form supplies `O4`'s fibre leg at subscript `𝒢`"* | **TYPING CORRECTION, not a refutation.** That sentence is typed at the **chimeric frame** algebra `𝔰𝔬(7,7)`. The source's own inhomogeneous-gauge-group definition builds `𝒢` and `N = Ω¹(ad P_H)` on `P_H` with `H = U(64,64)`. `𝔲(64,64)` is **reductive, not semisimple**, and its **Killing form is degenerate** (radical = the one-dimensional centre) — verified on the `𝔤𝔩(2,ℝ)` fixture, Killing rank `3` of `4`, trace form rank `4` of `4`. At the source's own `Δ1` algebra the fibre leg needs the **trace form**, not the Killing form. The leg is still available; the *name* of the form is wrong |
| **OT-1's remainder numbers**, `273` / `1183` | **ALGEBRA-SCOPED, and much larger at the source's own algebra.** At `𝔲(64,64)`, `t = d`: the unpaired remainder is **at least `49,148`** on `X⁴` and **at least `212,978`** on `Y¹⁴` (lower bounds — the algebra is not perfect, so the rank bound is not attained; the `𝔰𝔬(∗)` numbers *are* exact). OT-1's Lens Q2 fenced this qualitatively; LA-11 made it quantitative for `𝔰𝔬(6,4)`; this extends it to the algebra the source's own Definition 5.1 names |
| **my own preflight (Lens P3)** | **REFUTED by my own sweep, and planted as a firing control.** The isotropy bound gives `t ≤ (d+1)/2` and centre-fraction `(d−1)/(2d)`; both are too weak. The orthogonality bound gives `t ≤ 1` and `(d−1)/d` |
| **my own prediction on antisymmetry** | **REFUTED.** I expected an identical lattice; the antisymmetric one is strictly stricter |
| **my own scope, corrected by a sibling artifact** | **`BD-A` is right that there is a domain fork and that OT-1's theorem and LA-11's trigger name different objects.** Verified independently here (§5b): on the module `V` alone a nondegenerate `𝒲`-invariant form exists at every `d`. This does not touch Theorem BD-B-1, which is about the algebra; it re-scopes what the theorem is *about*. Credited, not absorbed |

---

## 8. CLAIM CEILING

**May be claimed, exactly and only:**

- **Theorem BD-B-1** as stated in §2: for `𝔴 = 𝔤 ⋉ (Λ¹ ⊗ 𝔤)` and any subalgebra
  `𝔥`, every `𝔥`-invariant bilinear form (symmetric or antisymmetric) obeys
  `rank B ≤ dim 𝔴 − dim(𝔤·(𝔥∩V)) + dim 𝔤`; hence nondegeneracy requires
  `dim(𝔤·(𝔥∩V)) ≤ dim 𝔤`. The bound does not involve `π(𝔥)`.
- The exact formulae `max rank = min(dim 𝔴, (d+2−t)·dim 𝔤)`,
  `radical = max(0, (t−1)·dim 𝔤)`, `dim Inv = 1 + d + (d−t)(d−t+1)/2` for `𝔤`
  absolutely simple at fibre subscript `𝒢`, verified at `d ≤ 4` on three
  algebras.
- **The fibre subscript is inert**: at fixed `t`, max rank and the nondegeneracy
  verdict are the same for `π(𝔥) = 𝔤`, a maximal compact, a Cartan, and the
  trivial group; and the same for split, compact and reductive `𝔤`.
- **The evasion set is exactly `t ≤ 1`**, with explicit full-rank witnesses at
  `d = 4` for a simple, a compact and a reductive fibre algebra, plus a
  line-type subscript.
- At `t = 1` the base form is **forced corank one**, with stabilizer dimension
  `(d−1)(d−2)/2` — `3` on `X⁴`, `78` on `Y¹⁴` — computed, not asserted.
- **No nonzero `GL(Λ¹)`- or `SL(Λ¹)`-invariant symmetric form exists** for
  `d ∈ {2,3,4,14}`, while `SO(p,q)` gives exactly `1`.
- At subscript `𝒲` with `d ≥ 2` the invariant **antisymmetric** space is
  **empty**; and `dim 𝔴` is odd on every `𝔰𝔬(∗)` GU row.
- The re-derivation of OT-1's theorem, the confirmation of LA-11's
  `dim 𝔰𝔬(6,4) = 45`, `dim 𝔰𝔬(7,7) = dim 𝔰𝔬(9,5) = 91`, `dim Inv_{Spin(6,4)} = 32`
  and `dim Inv_K = 3` on **both** horns, and the remainders `273`/`1183`,
  `135`/`585`.
- The corrections in §7.

**May NOT be claimed, and is not:**

- That any GU quantity is, or is not, action-owned. No ownership theorem is
  proved here and none is refuted.
- That an ownership theorem is impossible. The opposite: an entire evasion class
  is exhibited with witnesses.
- That leg (b) has been built. It has not. This artifact **shapes** the
  construction target; it does not perform it.
- Any adjudication of `SIGNATURE-AMBIENT`. Both horns are carried and give
  identical numbers; that is a *robustness* observation, not a settlement, and
  the fork stays open.
- Any adjudication between the Spin-native, two-`U(32,32)`-half and
  full-`U(64,64)` action parents.
- Any adjudication of the Layer-0 typing question in §6.4 (which algebra `Δ1`'s
  `ad P` really is). The divergence is reported; the composite verdict is
  invariant under it.
- Any verdict, reason-kind, priority, canon, `CURRENT-STATE` or public-posture
  movement. **Zero rows advance.**
- **Anything about Weinstein's claims.** This is an internal-target no-go about
  a repository object — the space of invariant bilinear forms on a Lie algebra
  the repository constructed. Weinstein asserts the semidirect product
  (Definition 5.1); he asserts nothing about invariant metrics on it, and this
  result must never be summarised as evidence against him. The `target_claim`
  frontmatter names internal targets for exactly this reason.

**Not laundered:** `CG-1`'s reduction and `AUDIT`'s `REDUCTION_EXTERNAL` price
are carried in the price column and never converted into a derivation. The
`OWNED_K` row evades on the same terms as every other `t = 0` row — the
reduction buys **definiteness of the fibre form**, which is a different question
from nondegeneracy of the composite, and it buys nothing at all on the
composite.

---

## 9. REPRODUCE

```bash
cd /path/to/gu-formalization
_local/cas-venv/bin/python tests/channel-swings/joe_directed_bdb_subscript_lattice.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_bdb_subscript_lattice.py --selftest
```

Expected: `CERTIFICATE: 131/131 checks pass; no load-bearing float (swept).`,
exit 0, split `[C] 24  [E] 95  [R] 12`; and
`FAILURE-PATH SELFTEST: PASS (14/14 planted false facts drove exit 1)`.
The probe is self-contained — it builds every Lie algebra it uses and reads no
repository file.

---

## 10. POSTFLIGHT — six lenses, run on this artifact

### Lens Q1 — the strongest overclaim available here, and it is refused

The available inflation is: **"the base-duality object is impossible; the
fourteen rows LA-11 attached to it are dead."** Refused, on my own numbers.
An entire evasion class exists (`t ≤ 1`), it contains the source's own `𝒢` at
`t = 0`, and it contains a translation-retaining route at `t = 1` with an
explicit witness. What is dead is the *search for a better fibre group* — and
that search was never in anyone's plan; it was the implicit assumption behind
the word "NAMED" in LA-11's trigger. The honest headline is narrower and more
useful: **the trigger's `NAMED subscript` fence is satisfiable, and the set of
satisfying subscripts is now written down exactly.**

The second available inflation is **"OT-1 was too weak."** Also refused. OT-1's
theorem is exactly right at the subscript it addresses and needed no correction;
what it lacked was the observation that its own proof never uses the fibre
group, which is a one-line generalisation nobody had made, including OT-1's
hostile reviewer and LA-11's independent re-derivation.

### Lens Q2 — the strongest contrary construction, which I cannot refute

**A reader can deny that `t` is a free parameter at all.** The steelman: `Δ1`
declares `𝒲` and only `𝒲`; there is no GU object called "translation depth," and
`𝒢 ⋉ (L ⊗ ad P)` is not a group GU has ever named. On that reading rows 11–13
and 16 are inventions, the table has three real rows (`𝒲`, `𝒢`, `𝒦 ⋉ V`), and my
"lattice" is a lattice of my own construction.

I cannot refute this from the declared content. What I can say is that `ADM-1`
was written *before* the sweep precisely to make the objection checkable, and
that row 11's supply justification is not decorative: it is the stabilizer of
the datum LA-11's own proposed `revival_trigger` demands. If leg (b) is ever
built, its stabilizer *becomes* a named subscript whether or not anyone names
it. But the objection is live, and a reader who rejects `ADM-1` should read this
artifact as: *OT-1's obstruction does not depend on the fibre group* — which is
the fibre-column result, and which survives the objection untouched.

### Lens Q3 — the weakest seam

**The seam is sufficiency, and specifically the gap between §2's necessary
condition and §4's witnesses.** I proved `dim(𝔤·V') ≤ dim 𝔤` is *necessary* for
every subalgebra. I proved it *sufficient* only where I built a witness. The
table's EVADED column therefore rests on witnesses for four shapes of subscript
and on an unproved (though I believe true) uniformity for the rest. A reader who
constructs a subalgebra satisfying the bound with no invariant nondegenerate
form has found a real hole. §6.2 item 2 says this in the same words; it is
flagged rather than buried.

Second seam: `H¹(𝔤, Λ¹⊗ad) = 0` is computed at `d = 2,3,4` for `𝔰𝔩(2,ℝ)` only.
Whitehead's lemma makes the general statement standard, but I ran three cases,
not a proof.

### Lens Q4 — what a hostile reader should attack next, in order of yield

1. **Delete `O3b`** (§6.3). Highest yield by a wide margin: it collapses the
   lattice to one row and this artifact becomes a base-leg note.
2. **Reject `ADM-1`** (Lens Q2). Removes the evasion route while leaving the
   fibre-column no-go intact — the most likely *partial* success.
3. **Attack sufficiency** (Lens Q3) by exhibiting a bound-satisfying subalgebra
   with no witness.
4. **Adjudicate the domain fork** (§5b). Higher yield than anything below it
   and lower than `O3b`: deciding whether ownership needs `(α)`, `(β)` or `(γ)`
   decides whether this artifact's §2–§4 are the main result or a footnote. I
   deliberately did not decide it, because deciding it is a Layer-0 typing call
   about clause `O4`'s own wording and this channel does not own that.
5. **Attack the disconnected-subscript gap** (§6.2 item 1) by exhibiting a
   component group that kills a `t = 1` witness. This one I expect to succeed
   and would like someone to run; it would make the evasion route narrower than
   I have drawn it.
6. Do **not** attack the rank bound of §2. It is two lines, it uses only the
   bracket, and it is machine-checked against `131` assertions with `14` planted
   false facts.

### Lens Q5 — decision usefulness: what should actually change

Three specific places.

1. **Stop looking for a better fibre group.** The fibre column is decided and it
   is flat. Any future artifact that proposes to discharge `O4` by moving to
   `Spin(6,4)`, to `K`, to `U(3,2)` or to the Standard Model subgroup is
   proposing a move the mathematics says is inert. That is a real deletion from
   the search space and it is the cheapest thing this artifact does.
2. **LA-11's proposed `LT-GR6b` should carry a corank field.** Its
   `revival_trigger` asks for *"a source-owned global base duality … a density
   together with a nondegenerate `Λ¹` pairing."* At `t = 0` that is right; at
   `t = 1` the pairing is provably **not** nondegenerate — it is corank one. The
   trigger as written silently selects `t = 0` and therefore silently abandons
   all translation invariance. If that is intended it should be said; if it is
   not, the trigger needs a second horn. This is a **wording** observation for
   the canonical owner, not a ledger edit, and no ledger file is touched here.
3. **The `O3b` fork is now priced.** It was a modelling disagreement this
   morning; it is now worth exactly `273` unpaired directions on `X⁴` and `1183`
   on `Y¹⁴` (or `≥ 49,148` / `≥ 212,978` at the source's own `Δ1` algebra). A
   fork with a number attached is a fork that can be scheduled.

### Lens Q6 — reproducibility and drift

Every number in this file is produced by one self-contained probe that reads no
repository file, builds every algebra from structure constants, and re-derives
each borrowed fact before using it. There is therefore no path by which this
artifact can drift from the ledger, from OT-1, or from LA-11 — it depends on
none of them computationally, only argumentatively. The `14` planted false facts
cover every headline claim: the OT-1 reproduction, the threshold, the criterion,
fibre-independence, the contrary control, base naturality, `dim 𝔰𝔬(6,4)`,
`dim Inv = 32`, the remainders, the table partition, the antisymmetric
emptiness, the line subscript, the source-algebra remainder, and the domain
fork. If any of those
sentences is edited without editing the probe, the probe exits 1.
