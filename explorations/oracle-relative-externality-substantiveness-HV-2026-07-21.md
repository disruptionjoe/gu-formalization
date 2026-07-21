---
title: "HOSTILE VERIFY of the Prong III externality capstone: is 'the observer forces sigma's externality but cannot SUPPLY its value' a genuine THEOREM (= no_invariant_valuation for the fixpoint-free K_S flip), or a trivial retreat? VERDICT HV-BRIDGE-GAP. The Lean theorem no_invariant_valuation is REAL but its content is a CODOMAIN tautology (no map into {+K_S,-K_S} has an alpha-FIXED output; true of any fixpoint-free Z/2, GU-free); it is NOT literally the physics claim. The physics claim ('no internal/first-person observable can supply sigma') is carried by a DIFFERENT statement -- the DOMAIN-side alpha-even/Schur identical-rows result (prong I zero-capacity) -- which no_invariant_valuation does not prove. The connector is a NAMED BRIDGE LEMMA: 'the internal first-person observable algebra = the alpha-EVEN class (so any internal sigma-supplier is an alpha-invariant valuation).' That bridge is separately established only at EXPLORATION grade (W211 five-method Godel-independence + prong I Schur, itself HV-flagged), NOT at the Lean/canon grade the capstone's phrasing implies. Capstone does NOT collapse (real, GU-specific, multiply-established content survives) but must be RESTATED: cannot-supply is theorem-grade CONDITIONAL on the internal=alpha-even bridge; no_invariant_valuation formalizes only the trivial codomain tail. Attacks 1 (triviality) and 2 (bridge) LAND as one; attacks 3 (fixpoint-freeness) and 4 (valuation-vs-reading) do NOT independently land but CONFIRM the diagnosis (the hypothesis is real but near-trivial for a 2-element object; InvariantValuation is codomain-invariant-labeling, not reading)."
status: active_research
doc_type: exploration
created: 2026-07-21
verifies: "the Prong III externality theorem (explorations/oracle-relative-prongIII-exhaustiveness-theorem-2026-07-21.md, outcome III-THEOREM for the externality claim proper; its Section 6 hostile-verification flag)"
inputs:
  - explorations/oracle-relative-prongIII-exhaustiveness-theorem-2026-07-21.md
  - explorations/oracle-relative-prongI-info-exact-2026-07-21.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/decision-tree-Q2-defense-attorney-2026-07-21.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - "READ-ONLY temporal-issuance: formal/lean/OnlineIssuance/BoundaryInvolution.lean, BoundaryParent.lean"
runnable:
  - tests/channel-swings/externality_substantiveness_HV_probe.py
outcome: HV-BRIDGE-GAP
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Hostile verify: is the externality "theorem" substantive, or a trivial retreat?

Refute, don't confirm. The claim under test is the Prong III capstone's headline
(its Section 5 "III-THEOREM for the externality claim proper"):

> "The observer forces sigma's externality but cannot SUPPLY its value" is a
> genuine THEOREM = `no_invariant_valuation` for the fixpoint-free K_S flip -- a
> promotion from strong-lean to theorem/Lean grade, NOT a trivial retreat.

My single job: decide SUBSTANTIVE vs vacuous/trivial-dressed-as-result. Default
skeptical; two earlier session wins died on verification.

**Verdict up front: HV-BRIDGE-GAP.** The Lean theorem is real but it is NOT
literally the physics claim. `no_invariant_valuation` proves a CODOMAIN
tautology; the physics ("no internal observable supplies sigma") is a DIFFERENT,
DOMAIN-side statement (Schur / prong-I zero-capacity) that the Lean theorem does
not touch. The connector is a named bridge lemma (internal = alpha-even),
separately established only at EXPLORATION grade. The capstone does not collapse,
but its attribution over-reaches and it must be restated.

Receipt: `tests/channel-swings/externality_substantiveness_HV_probe.py` --
deterministic (exhaustive enumeration, no RNG, no network), foreground, **exit
0**, double-run **byte-identical**, HEADLINE
`5 [E] + 2 [F] = 7 :: no_invariant_valuation is CODOMAIN-trivial ... BRIDGE-GAP CONFIRMED`.

---

## 0. The exact object, read off the Lean source

`BoundaryInvolution.lean` (READ-ONLY temporal-issuance):

```
def InvariantValuation {A B : Type _} (alpha : B -> B) (v : A -> B) : Prop :=
  forall a, alpha (v a) = v a

theorem no_invariant_valuation {A B : Type _} {alpha : B -> B}
    (hff : FixpointFree alpha) (a0 : A) :
    not (exists v : A -> B, InvariantValuation alpha v) := by
  intro h; obtain <v, hv> := h; exact hff (v a0) (hv a0)
```

Read the definition literally. `alpha : B -> B` acts on the **codomain** (the
label object). `InvariantValuation alpha v` says **every output value `v a` is
alpha-FIXED**. There is NO action of `alpha` on the domain `A` anywhere in the
definition. So `no_invariant_valuation` is a statement purely about `B`: *a
fixpoint-free involution on the labels admits no map whose outputs are fixed
labels* -- because a fixed output would be a fixed label, and there are none.
Its own docstring concedes it: "Trivial, but it is the exact content the parent's
conclusion (b) rides on."

This single reading is the whole finding. Everything below is its consequences.

---

## Attack 1 -- TRIVIALITY / vacuity: does the theorem say anything GU-specific?

**Result: LANDS (as the surface of Attack 2).**

`no_invariant_valuation` carries **zero** GU-specific content. It is true of ANY
fixpoint-free involution on any 2+-element set -- a coin's `not`, negation on `Z`,
the swap on `{apple, pear}`. The Lean file proves it generically and instantiates
it on `Bool`/`not` (`bool_no_invariant_valuation`) with no physics in sight.
Probe F2: dissolve fixpoint-freeness (`alpha = id`) and 4 invariant valuations
reappear -- so the theorem's *entire* content is fixpoint-freeness, nothing more.
It would be "equally true of a coin flip in any theory," exactly the attack's
phrasing.

Where, then, is the GU content? It is NOT in the theorem. It is split between:
(i) the **hypothesis** -- "the K_S-flip is a fixpoint-free involution on
`{+K_S,-K_S}`" (real, but see Attack 3: near-trivial for a 2-element object); and
(ii) the **interpretation of the conclusion** -- "no alpha-invariant valuation"
= "the observer cannot internally supply sigma." (ii) is the substance, and (ii)
is precisely the bridge of Attack 2. So triviality is not fatal *by itself* -- it
is fatal only insofar as the content that would redeem it (the bridge) is
unproven at the claimed grade. Attack 1 is the surface; Attack 2 is the diagnosis.

---

## Attack 2 -- THE BRIDGE GAP: is the Lean theorem literally the physics claim?

**Result: LANDS. This is the verdict.**

Two statements are in play:

- **(Lean, codomain)** no `v : A -> B` has alpha-FIXED output.
- **(physics, domain)** no INTERNAL / first-person physical observable can
  determine sigma (the Krein orientation / DE sign).

Are they the same? **No.** Trace the actions:

1. A genuine **sigma-reader** is a map that OUTPUTS the actual orientation. Under
   the state-flip it co-varies: `v(act a) = flip(v a)`. That is
   **alpha-EQUIVARIANT**, NOT alpha-invariant. Its outputs are the two DISTINCT
   labels -- never fixed. So a correct reader is exactly the kind of map
   `no_invariant_valuation` says nothing about. Probe E2/E3: `sigma` itself reads
   the bit, is equivariant, and is NOT an invariant valuation -- it is a reader
   the codomain theorem **misses**.

2. What actually forbids an internal reader is a **domain-side** fact: the
   internal observable is **alpha-EVEN** (`f(act a) = f(a)`), so `f(p_+) =
   f(act p_-) = f(p_-)` -- IDENTICAL rows on the sigma-orbit, hence zero
   resolution of sigma. Probe E4: among alpha-even maps, ZERO read sigma. This is
   `Hom(triv,sign)=0` (Schur) -- **prong I's zero-capacity theorem** -- and it is
   a DIFFERENT computation from `no_invariant_valuation`. Probe F1: drop the
   alpha-even premise and a reader (`sigma`) reappears -- so the block is
   **bridge-borne**, not theorem-borne.

So the physics claim decomposes as:

- (B1) internal reader = alpha-EVEN (domain). **[substantive GU/rep-theory fact;
  NOT the Lean theorem]**
- (B2) an alpha-even map cannot resolve the alpha-odd sigma (identical rows /
  Schur). **[theorem-grade -- but this is prong I, NOT `no_invariant_valuation`]**
- (B3) equivalently: an internal map forced to co-vary with sigma would need an
  alpha-FIXED label; none exists. **[here, and ONLY here, `no_invariant_valuation`
  applies -- as the trivial final tail]**

`no_invariant_valuation` is step (B3): the last, trivial line. The load-bearing
content is (B1)+(B2), which lives in W211 and prong I, not in the Lean file.

**The named bridge lemma** (what must be proved to make the Lean theorem the
physics claim):

> **BRIDGE LEMMA.** The first-person / internal observable algebra is exactly the
> alpha-even (domain-invariant) class; equivalently, every physical internal
> sigma-supplier factors as an alpha-invariant valuation. (So that an internal
> map co-varying with sigma would require an alpha-fixed label, whence
> `no_invariant_valuation` bites.)

Prong III asserts this bridge in passing -- Section 6.4: "an alpha-invariant
valuation IS an internal, orientation-free commitment to a definite label." The
word "internal" is the entire bridge, asserted, not proved *in the theorem*. Its
real support is the identification "internal = alpha-even," which is:

- prong I Section 0 ("the diagonal-boundary result that excluded-reading =
  alpha-equivariant class" + "W211's five-method finding that every internal
  sense of compute-inside-GU lands in the alpha-even part"), and
- W211 (five methods: counterfactual-invariance, BRST, Lawvere, topos, Helmholtz,
  all converging on internal = alpha-even and the sign Godel-INDEPENDENT).

That support is genuine and multiply-argued -- the best-established part of the
whole edifice -- but it is **exploration grade**: W211 is explicitly
LOCATED-NOT-FORCED, Joe-gated, NOT canon; prong I's Schur zero-capacity is itself
"flagged for hostile verify," not yet banked. So the bridge is *separately
established at exploration grade*, NOT at the "operator/Lean grade" the capstone's
phrasing ("ALREADY Lean-proved", "theorem at operator/Lean grade") implies.

**Does prong III's Section 6 pre-answer defeat this?** No. Its Section 6.1
answer addresses a *different* triviality worry -- "is the fixpoint-freeness
hypothesis gated on the open resolvent theorem?" -- and correctly answers no
(deck-oddness `U_h K_S U_h^{-1} = -K_S` is machine-exact, ungated). I concede
that (Attack 3). But that defends the HYPOTHESIS; it does not close the gap
between the codomain conclusion and the physics claim. Section 6.4 merely
*asserts* the bridge ("an alpha-invariant valuation IS an internal commitment")
rather than establishing internal = alpha-even. The bridge attack survives all
four of Section 6's pre-answers -- which is exactly what a hostile pass is for.

---

## Attack 3 -- FIXPOINT-FREENESS: real GU fact, or vacuous / trivial-by-construction?

**Result: does NOT land (the hypothesis is real) -- but it CONFIRMS Attack 1/2.**

Could the K_S-flip secretly have a fixed point (theorem vacuously inapplicable)?
No: a fixed point means `K_S = -K_S`, i.e. `K_S = 0`, excluded (nondegenerate
Krein form). On `{+K_S,-K_S}` the flip swaps two distinct labels; fixpoint-free
is manifest. Is it trivially true by construction (content-free)? The physical
identity `U_h K_S U_h^{-1} = -K_S` (deck-oddness, defect ~1e-12) is a genuine
computed fact about the specific `U_h`, not a tautology -- so the hypothesis IS
real GU content. Attack 3 fails to kill.

But note what this concession is worth: it establishes only that the *flip is a
physically realized symmetry*. For `no_invariant_valuation` itself you need much
less -- merely "two distinct labels swapped," which is near-trivial. The
deck-oddness identity's real job is to certify that the internal observer
*respects* this flip (feeding the BRIDGE, B1), not to power the Lean theorem. So
Attack 3 relocates the GU content into the bridge, sharpening Attacks 1-2 rather
than rescuing the capstone's attribution.

---

## Attack 4 -- "valuation" vs "reading": does InvariantValuation capture "reads the bit"?

**Result: does NOT independently land -- but CONFIRMS the bridge diagnosis.**

`InvariantValuation alpha v := forall a, alpha (v a) = v a` captures
"commits to an alpha-INVARIANT label," a codomain-fixed-point notion. It is a
DIFFERENT and weaker/other notion than "reads sigma" (which is domain
equivariance). It was chosen because it yields the one-line proof, not because it
is the reading notion. Under the most charitable framing -- "an alpha-symmetric
(internal) agent's committed label must be alpha-invariant, and none exists" --
`InvariantValuation` becomes apt, but ONLY after importing "the agent is
alpha-symmetric" = the bridge premise again. So Attack 4 does not open a new
front; it confirms that `InvariantValuation` reaches "reading" only across the
same internal=alpha-even bridge.

---

## Probe summary

`tests/channel-swings/externality_substantiveness_HV_probe.py` (exit 0,
deterministic, byte-identical double-run):

| id | check | result |
|----|-------|--------|
| E1 | `no_invariant_valuation` true: 0 alpha-invariant valuations (codomain) | PASS |
| E2 | `sigma` READS the bit (distinguishes +K_S / -K_S) | PASS |
| E3 | `sigma` is alpha-EQUIVARIANT (a reader), NOT an invariant valuation | PASS |
| E4 | codomain theorem is SILENT about equivariant readers (>=1 missed) | PASS |
| E5 | under the alpha-EVEN bridge: 0 internal readers of sigma (Schur) | PASS |
| F1 | dissolve the alpha-even bridge => a reader reappears (block is bridge-borne) | FIRE |
| F2 | dissolve fixpoint-freeness (`alpha=id`) => 4 invariant valuations reappear (content = fpf only) | FIRE |

The probe is a faithful finite model of the grade-independent structural facts:
the codomain theorem's blindness to equivariant readers (E2-E4), the domain-even
Schur block that actually carries the physics (E5), and the two teeth showing the
substance is bridge-borne and the theorem's content is fixpoint-freeness alone
(F1-F2).

---

## Verdict

**HV-BRIDGE-GAP.** The Lean theorem `no_invariant_valuation` is real and its GU
hypothesis (fixpoint-free K_S-flip) is real, but the theorem is a CODOMAIN
tautology that is **not literally the physics claim**. "The observer cannot
supply sigma's value" is carried by a DIFFERENT statement -- the domain-side
alpha-even / Schur zero-capacity result (prong I) -- connected to the Lean
theorem only through an unstated-at-theorem-grade **bridge lemma**.

**Does the capstone stand as stated?** No -- not as "cannot-supply IS the theorem
`no_invariant_valuation`, at operator/Lean grade." That attribution folds an
exploration-grade structural identification (internal = alpha-even) into a
trivially-true Lean line and thereby overstates the grade. The capstone does NOT
collapse: there is real, GU-specific, multiply-established content that the
internal observer cannot supply sigma. It must be **restated**:

> The "cannot-supply the value" claim is theorem-grade **conditional on the
> bridge lemma** [the internal first-person observable algebra = the alpha-even
> class]. Its substantive carrier is prong I's Schur zero-capacity theorem
> (`Hom(triv,sign)=0` => identical channel rows => `I(sigma;internal)=0`) together
> with W211's five-method internal=alpha-even / Godel-independence. The Lean
> `no_invariant_valuation` formalizes only the trivial codomain tail (no
> alpha-fixed label) and does NOT by itself bridge to physical readers. The bridge
> is established at EXPLORATION grade (W211 five-method + prong I Schur, itself
> HV-flagged), not at Lean/canon grade.

**The exact bridge lemma (named open at Lean/operator grade):**

> **BRIDGE LEMMA.** Every physical first-person / internal sigma-supplier is an
> alpha-invariant valuation -- equivalently, the internal observable algebra is
> exactly the domain-alpha-even class, so any internal map co-varying with sigma
> (an equivariant reader) would require an alpha-fixed label and hence cannot
> exist. This is what connects `no_invariant_valuation` (codomain: no alpha-fixed
> label) to the physics ("no internal observable reads/supplies sigma"). Support:
> prong I (Schur, theorem-grade linear algebra, HV-flagged) + W211 (five-method,
> exploration grade). NOT proved in the Lean files (`InvariantValuation` never
> references a domain action).

**Attack scorecard.** Attack 1 (triviality) LANDS as the surface of Attack 2.
Attack 2 (bridge) LANDS -- the verdict. Attack 3 (fixpoint-freeness) does NOT land
(hypothesis is real) but confirms the GU content sits in the bridge, not the
theorem. Attack 4 (valuation vs reading) does NOT independently land but confirms
`InvariantValuation` reaches "reading" only across the same bridge.

**Net for the session headline.** The externality result is not vacuous and not a
retreat to nothing -- but it is also not the clean "already Lean-proved theorem"
the capstone advertises. It is: a trivial Lean shadow (`no_invariant_valuation`)
+ a real but exploration-grade bridge (internal = alpha-even, from W211/prong-I) +
the genuine theorem-grade carrier (prong I Schur zero-capacity, still
HV-flagged). Bank it as "theorem-grade conditional on the internal=alpha-even
bridge," and promote the bridge lemma to a named, separately-verified target
before any canon/grade claim rides on the word "theorem."

---

## Boundary

Exploration tier. One new artifact + one foreground probe
(`tests/channel-swings/externality_substantiveness_HV_probe.py`, exit 0,
deterministic, double-run byte-identical, pure-python exhaustive enumeration, no
RNG, no network). This document VERIFIES a claim and moves nothing: no edits to
LANE-STATE, research-portfolio, NEXT-STEPS, any decision-tree, any
claim/canon/verdict/ledger/portfolio file, the Prong III/Prong I/Q2 artifacts, or
any other agent's work. GU and the cross-repos (temporal-issuance) touched
READ-ONLY. No commit/push, no external actions. `claim_status_change: none`,
`canon_verdict_change: none`, `public_posture_change: none`. The externality of
sigma remains the program's closed premise (p2c-owned per the tri-repo
signed-graph); this pass judges only whether the "cannot-supply" half is the
theorem the capstone claims it is, and finds it is theorem-grade only across a
named, exploration-grade bridge.
