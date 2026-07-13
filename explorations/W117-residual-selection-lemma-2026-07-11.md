# W117: The Residual-Selection Lemma -- one kernel-checked core for two instances

**Swing, submit-track cross-repo artifact.** Status: LEMMA-PROVEN-KERNEL.

## What this is

ONE Lean lemma, stated once at the shared level of generality, from which BOTH
machine-checked instances derive as corollaries:

1. **GU instance** -- the observer-value-selection theorem
   (`papers/candidates/observer-value-selection-theorem/observer-value-selection-theorem-2026-07-11.md`):
   Lawvere no-closure (I-a) and no-invariant-valuation (I-b) for a two-element
   admissibility grading with the fixpoint-free swap involution. Previously
   confirmed only on finite models (W70, W73, W75, W99); now kernel-checked in
   full generality.
2. **TI instance** -- temporal-issuance's semantic-tier diagonal
   (`temporal-issuance/formal/lean/OnlineIssuance/Comparator.lean`, T5
   `diagSem_escapes`): no countable total Nat-indexed Boolean family internally
   indexes its own extensional diagonal.

The shared core is Lawvere's fixed-point theorem in Yanofsky's elementary form,
phrased pointwise (funext-free, matching TI's own discipline).

## The shared lemma (Lean: `Lean/GUFormalization/ResidualSelection.lean`)

Over types `A B : Type`, with `alpha : B -> B` fixpoint-free
(`forall b, alpha b != b`):

- **`residual_escapes`** (escape leg): for ANY `T : A -> A -> B` and ANY code
  `a0`, the row `T a0` does not pointwise equal the residual diagonal
  `fun a => alpha (T a a)`. Proof: one line -- evaluate at `a0`, contradict
  fixpoint-freeness.
- **`lawvere_fixed_point`** (Lemma L, positive form): a weakly point-surjective
  `T` forces every `alpha : B -> B` to have a fixed point.
- **`no_closure`** (no-closure leg): fixpoint-free `alpha` forbids any weakly
  point-surjective `T`.
- **`no_invariant_valuation`** (residual corollary; the fixed-point-count leg,
  Lemma C): for inhabited `A`, no valuation `p : A -> B` satisfies
  `forall x, alpha (p x) = p x`. Every committed valuation breaks the grading
  symmetry.

Axiom audit: `#print axioms` reports **no axioms** for all seven theorems --
not even `propext` or `Classical.choice`. The proofs are pure kernel-level
intuitionistic Lean.

## Corollary GU (derived, actual)

Instantiate `B = Bool`, `alpha = not` (fixpoint-freeness `(!b) != b` is
kernel-decided by `decide`):

- `gu_residual_not_row` -- the paper's (I-a) concrete residual form: the
  diagonal valuation `d = alpha . T . Delta` is not a row of any `T`.
- `gu_no_closure` -- (I-a): no weakly point-surjective `T : A x A -> Bool`.
- `gu_no_invariant_valuation` -- (I-b): for inhabited `A`, no total valuation
  is alpha-invariant.

These ARE the paper's theorem statements (Parts I-a and I-b), at full
generality over any arena type `A`, not the finite-model confirmations of
W70/W75. Part II (the arena/value partition) is group-theoretic framing on top
of (I-b) and is not separately formalized; its load-bearing mathematical
content IS (I-b), which is now kernel-checked.

## Corollary TI (derived, shape-level -- stated honestly)

`ti_diagSem_escapes` re-derives, from the shared lemma at `A = Nat`,
`B = Bool`, `alpha = not`, a statement whose definitions (`SemFamily`,
`InternallyIndexed`, `diagSem`) are declared with bodies definitionally
IDENTICAL to TI's and whose statement is identical to TI's kernel-checked T5
`diagSem_escapes`.

**What is and is not derived:**

- DERIVED (actual shape): TI's semantic-tier escape theorem, token-for-token
  the same statement over locally redeclared but definitionally identical
  types. TI is a separate Lake project; a true import would require TI
  published as a Lake dependency (or a shared upstream package). Until then
  the correspondence is shape-level by reproduction, and we say so.
- NOT derived: TI's string-tier `diagName_not_mem`
  (`OnlineIssuance/Diagonal.lean`) -- the padded character-level list Cantor.
  Its statement (list non-membership with length bookkeeping over
  `List String`) is a finite-tier relative of the diagonal, not a literal
  instance of the shared lemma; deriving it would need a finite-index bridge
  (rows indexed by list position, escape by disagreement-or-length), which is
  extra machinery, not a corollary. Likewise `issue_lc_all_derived` bundles
  the diagonal with TI's admissibility/witness apparatus (G2), which is TI
  domain content, not shared structure.
- TI's own honest caveats carry over: modeling faithfulness is internal to
  TI's fixture (its E-series notes), and `diagSem_escapes` is
  DERIVED-MODEL-RELATIVE in TI's vocabulary (total families, not c.e.
  generation; no programs, no s-m-n). Nothing here upgrades those caveats.

## Build and verification status

- **Lean: kernel-checked.** `lake build GUFormalization.ResidualSelection`
  succeeds (Lean 4.32.0-rc1, the repo's existing scaffold); the module is
  imported from `Lean/GUFormalization.lean` and the full default target
  builds. Build run as the single Lean build on the machine (serialized per
  workspace rule; this repo's `lake` version rejects an explicit `-j1` flag,
  so serialization was enforced by running exactly one build at a time). No
  Mathlib import in the new module: core Lean 4 only. Axiom-free per
  `#print axioms`.
- **Python finite-model confirmation:** `tests/W117_residual_selection.py`,
  exit 0. Exhaustive over all `T` for `|A| in {1,2,3}` with `B = {0,1}`,
  swap; a 4-element `B` with a two-2-cycle involution (the lemma is not
  Bool-specific); identity-alpha controls confirming fixpoint-freeness is
  load-bearing (the no-gos dissolve); and the TI shape exhaustively over all
  `2^(n^2)` truncated families for `n in {1,2,3}`.

## What this does for the paper

The observer-value-selection paper (novelty grade (b), novel packaging)
previously had machine-checked *finite confirmations* only. It now has:

1. Its Lemmas L and C and results (I-a)/(I-b) **kernel-checked at full
   generality**, axiom-free.
2. A **second kernel-checked instance at a different layer**: the same lemma
   that forbids an alpha-invariant physics-selection valuation also produces
   the issuance-space escape of temporal-issuance's diagonal suite. Two
   layers (physics-selection and issuance), one proof core, one kernel.
   This partially defuses the same-designer confound: the two instances'
   agreement is enforced by the proof kernel, not by the author's intent --
   though the CHOICE of both modelings remains same-designer (the confound
   is defused at the derivation step, not at the modeling step).

## Adversary answers (self-critical)

- *"The TI corollary is a shape-reproduction, not TI's actual theorem."*
  Correct, and stated above exactly: the derived statement is
  token-identical to TI's T5 over definitionally identical redeclared types;
  it is not an import of TI's declarations, and TI's string-tier and
  issuance-bundle theorems are not derived. The upgrade claim is scoped to
  the semantic tier.
- *"The shared lemma is just Cantor."* Yes -- with `B = Bool` and
  `alpha = not` it is literally Cantor, and the paper already concedes
  (b)-grade novelty (Lawvere 1969 / Yanofsky 2003). The artifact's value is
  the TWO-INSTANCE kernel anchor -- one checked lemma discharging both
  layers -- not lemma novelty.

## Files

- `Lean/GUFormalization/ResidualSelection.lean` -- the lemma + both
  corollaries (kernel-checked, axiom-free).
- `Lean/GUFormalization.lean` -- import added.
- `tests/W117_residual_selection.py` -- finite-model verification (exit 0).
- Read-only sources: `temporal-issuance/formal/lean/OnlineIssuance/
  {Comparator,Diagonal,Core,Admissibility}.lean`;
  `papers/candidates/observer-value-selection-theorem/
  observer-value-selection-theorem-2026-07-11.md`; tests W70/W73/W75/W99.

**Verdict: LEMMA-PROVEN-KERNEL** (Lean builds; both corollaries derive; the
TI corollary is semantic-tier shape-level as disclosed; Python check green,
exit 0). No canon or claim-status changes; claim_status_change: none.
