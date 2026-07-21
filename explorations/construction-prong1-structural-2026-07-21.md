---
title: "Construction swing, PRONG 1 (STRUCTURAL/GEOMETRIC): POSIT S = (P1) three shards are ISOMORPHIC sheaves + (P2) sigma = the CLOSURE ORIENTATION of the shard-cycle. Build the isomorphic-sheaf shard-cycle with sigma inserted at the flip/no-flip realization handle Prong A located; read off what it FORCES. RESULT POSIT-PRODUCTIVE: the posit forces two INDEPENDENT consequences it did not insert that VERIFY banked facts -- (C2) the cycle's symmetry factors as Z/6 = Z/2 x Z/3 as a DIRECT product with the Z/2 = sigma independent of the Z/3 shard-rotation (verifies Q3 sigma_|_tau, and is a concrete instance of Q3's own base-united-but-not-identified escape clause), and (C3) the isomorphic-sheaf descent forces the relative orientation c = sigma_i*sigma_j to be an alpha-even 1-cocycle with vanishing coboundary = 'one globally consistent record arrow' (verifies the banked one-arrow result); plus one forced COMPATIBILITY (C1) the realization map to F is pinned pi_1-nontrivial (Prong A left it free). The null-stratum role (C4) is a SCAFFOLD, not forced (matches UNESTABLISHED). The deliberately-WRONG shard-INTERNAL posit is CAUGHT by the back-gate as an alpha-even contradiction with Q2-FREE/blindness. NO consequence contradicts a banked fact. sigma kept as a POSIT throughout; no derivation claimed."
status: active_research
doc_type: exploration
created: 2026-07-21
mode: CONSTRUCTION/posit-declared
prereg: explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
outcome: POSIT-PRODUCTIVE
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
probe: tests/channel-swings/construction_prong1_structural_probe.py
probe_exit: 0
inputs:
  - explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
  - explorations/three-seam-prongA-class-relative-frame-2026-07-21.md
  - explorations/shard-cycle-prong1-geometry-2026-07-21.md
  - explorations/shard-cycle-prong2-dynamics-gorard-2026-07-21.md
  - explorations/council-committed-constructions-math-2026-07-21.md
  - explorations/council-committed-constructions-extended-2026-07-21.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/decision-tree-Q3-one-anchor-vs-two-2026-07-21.md
---

# Construction Prong 1 -- STRUCTURAL / GEOMETRIC

## 0. Mode and one-line result (read first)

This is **CONSTRUCTION, not derivation.** The premise is that `sigma` is external /
not forced by GU structure -- so "it isn't forced" is **not** a disqualifier here.
I **POSIT** the object, build the coherent surrounding picture, and put the gate at
the **BACK**: does the posited picture FORCE consequences I did **not** insert that
VERIFY against banked facts? `sigma` is kept **labelled as a POSIT** throughout;
nowhere is this a derivation of `sigma`'s value.

> **Outcome: `POSIT-PRODUCTIVE`.** The posit forces **two INDEPENDENT, VERIFIED**
> consequences it did not insert -- the `Z/6 = Z/2 x Z/3` **direct-product**
> factorization with `sigma _|_ tau` (**C2**, verifies Q3) and the isomorphic-sheaf
> **descent cocycle** = "one globally consistent record arrow" (**C3**, verifies the
> banked one-arrow result) -- plus one forced **COMPATIBILITY** (**C1**, the
> realization map `f: S^1_SIO -> F` is pinned `pi_1`-nontrivial, which Prong A had
> left free). The null-stratum role (**C4**) is a **SCAFFOLD**, not forced (matches
> the banked UNESTABLISHED). The deliberately-**WRONG** shard-INTERNAL posit is
> **CAUGHT** by the back-gate as an `alpha`-even contradiction with Q2-FREE. **No
> forced consequence contradicts a banked fact.** Probe **EXIT 0**, deterministic.

## 1. The declared POSIT `S` (never asserted as forced)

- **P1.** The three shards `S`(ubjective) / `I`(ntersubjective) / `O`(bjective) are
  **ISOMORPHIC sheaves** -- three interchangeable copies `F_S ~= F_I ~= F_O` of one
  structure, glued in the cycle `S -> I -> O -> S` by transition isomorphisms
  `phi_SI, phi_IO, phi_OS`.
- **P2.** `sigma` = the **CLOSURE ORIENTATION** of the shard-cycle: the class in the
  deck `Z/2` of the composite monodromy `g = phi_OS . phi_IO . phi_SI in Aut(F_S)`.
  `g = id => sigma = +1` (no-flip closure, `R_noflip`); `g = ` the deck involution
  `=> sigma = -1` (flip closure, `R_flip`). **This is exactly the flip/no-flip
  realization handle Prong A located** (the `K_S / -K_S` isospectral closures): in
  construction mode I **insert** `sigma` there deliberately.

Prong A proved (derivation mode) that GU does **not** force which closure obtains --
that is the premise, restated, not a defect. The construction question is what the
posit, once inserted at that handle, forces **around** it.

## 2. The built picture

The isomorphic-sheaf shard-cycle is a **`Z/2`-twisted 3-object descent datum**: three
isomorphic sheaves cyclically glued, with a `Z/2` monodromy `= sigma`. Read as
geometry, it is a **mapping-torus / local-system** over the type-quotient circle
`S^1_SIO`, with structure group the deck `Z/2` of `{+K_S, -K_S}`. On this one object
sit three pieces of data that the standard (Prong-A) analysis kept separate and that
the posit now organizes:

1. the **closure monodromy** `sigma` -- the holonomy of the loop in the deck group
   (`alpha`-odd, global; **not** readable inside any single shard);
2. the **record-arrow** `Z/2` -- the two cyclic orderings `S->I->O` vs `S->O->I`, a
   **free torsor** (`w1(TS^1) = 0`, Prong A/Prong 1's trivial tangent class): the
   possessable `alpha`-odd **section**, welded to `sigma` by the co-flip (Q2);
3. the **shard-rotation** `Z/3` -- the cyclic relabeling of the three **isomorphic**
   shards (this is what P1 *adds*: without isomorphism the three are distinct labels;
   with it they are a genuine `Z/3` symmetry).

The **seam** (the `O->S` edge) is where the cycle closes and, by P2, where `sigma` is
inserted; when `sigma = -1` the twisted local system has **no global orientation
section**, forcing a branch locus (a wall where the sign is undefined) -- the natural
home of the null-`K_S` stratum. The relation to the **metric fiber** `F ~= RP^3` is a
realization map `f: S^1_SIO -> F` pulling back `w1(L_time)`; the posit constrains `f`
(section 3, C1).

The rest of this document extracts what the picture FORCES, tags each as INDEPENDENT
(forced, not inserted) or RESTATES-POSIT, and VERIFIES each against the banked facts.

## 3. The forced consequences

### C1 -- the realization map is pinned `pi_1`-nontrivial (forced COMPATIBILITY)

**Statement.** The posit (`sigma` = closure orientation, P2) **plus** the banked fact
(`sigma = w1(L_time)`, canonical) force the realization map `f: S^1_SIO -> F` to be
`pi_1`-**nontrivial**: `f^*(w1(L_time)) = sigma_closure` with both classes the
nontrivial generator requires `deg(f) mod 2 = 1`. Degree-0 is inconsistent
(`0 != 1`); degree-1 is forced. [probe **[K]**]

**Independent or restates?** **INDEPENDENT of what I inserted** -- I never mentioned
`f`; the constraint on `f` falls out of gluing my posit to the *external* banked class
`sigma = w1(L_time)`. But it is a **compatibility**, not a new number: a SCAFFOLD.

**Verify.** Prong A's decisive open point was that `f` is a **free `Z/2`** (deg-0 and
deg-1 both exist; GU forces neither), so in derivation mode "cycle-orientation =
`w1(L_time)`" could only be had by *choosing* `f`. In construction mode the posit
**is** that choice, and consistency with the banked class **selects the odd `f`**.
This does **not** contradict Prong A (which said GU doesn't pin `f` -- the *posit*
does). **VERIFIED-consistent; SCAFFOLD** (names the downstream object `f`, not yet
independently falsifiable). Honest reading: the posit does not *derive* the reconcili-
ation Prong A denied; it *supplies the one free bit* (`deg f`) that reconciles the two
readings, and that bit is exactly `sigma` again -- so C1 is largely the posit wearing
a second costume. Its non-trivial residue is only that the reconciliation is now
*forced-once-posited* rather than *free*.

### C2 -- the cycle symmetry is `Z/6 = Z/2 x Z/3`, a DIRECT product, `sigma _|_ tau` (INDEPENDENT, VERIFIED) -- the payoff

**Statement.** P1 (three **isomorphic** shards) forces a genuine order-3 **shard-
rotation** symmetry `R` (`Z/3`). P2 gives the order-2 **closure monodromy** `Q`
(`Z/2 = sigma`). These two commute and generate a group of order exactly 6; because
the deck group `Z/2` is **abelian**, the shard-rotation **fixes the monodromy class**
(cyclic-shifting the three edge-signs leaves their product = the monodromy invariant),
so the extension is **trivial**: `<Q,R> = Z/2 x Z/3 = Z/6`, a **direct product**. In a
direct product, **fixing `sigma` leaves the `Z/3` free and fixing the `Z/3` leaves
`sigma` free.** [probe **[G]**: `|<Q,R>| = 6`, `[Q,R] = 0`, rotation fixes the
monodromy class, `tau`-free-given-`sigma` and `sigma`-free-given-`tau` both hold.]

**Independent or restates?** The **factors** restate the inputs (the `Z/3` is "three
shards"; the `Z/2` is P2). But the **INDEPENDENCE** -- that the two are a *direct*
product, neither forcing the other -- is **INDEPENDENT**: I did **not** insert it. It
follows structurally from *monodromy* (an element of the structure/deck group) being a
different, commuting kind of datum from *permutation* (an automorphism of the diagram),
with the abelian deck making the extension split. **This independence is the payoff.**

**Verify against Q3.** Q3's banked verdict is exactly `sigma _|_ tau`, with the minimal
external ledger `Z/6 = Z/2 x Z/3` (the `Z/2` = `sigma`, the `Z/3` = the generation
trit) as **independent factors**. The construction **reconstructs this precise
factorization from the shard-cycle geometry**, without inserting the independence.
**VERIFIED.**

**The sharp, honest scope of the match.** The construction verifies the **shape**
(independent `Z/2 x Z/3`), not an **object-level identity** `shard-Z/3 = generation-
tau` (that would need the base-uniting map `F <-> S^3` Q3 says is unbuilt at fixture
grade). Moreover the construction realizes `sigma` and the trit on the **same** object
(the shard-cycle), whereas Q3's *evidence* used **different bases** (`F` vs `S^3`).
This is **not** a contradiction of the Q3 verdict -- and it is more than mere
consistency: it is a **concrete instance of Q3's own escape clause**. Q3 (section 4)
warned that a future base-uniting map could revive ONE-ANCHOR, then noted the harder
wall: *"a base-uniting map that leaves the count `sigma`-blind and the DE sign
deck-blind has united the fibers without identifying the data."* The shard-cycle **is**
such a base-uniting realization -- it puts both data on one object -- and the
construction shows they **still come out as a direct product** (`sigma` = monodromy,
`tau` = permutation; fixing one does not fix the other). So the construction
**demonstrates Q3-TWO-INDEPENDENT survives even in the base-united case**, exactly
the wall Q3 named. That is an independent verification of the *robustness* of
`sigma _|_ tau`, not a fresh identification. (It matches Members 1/3's "`sigma` on the
timelike line / spin cover, `tau` on the spacelike triad / `j=1` triplet -- two
orthogonal blocks" build, now realized as monodromy `_|_` permutation on one cycle.)

### C3 -- descent forces "one globally consistent record arrow" (INDEPENDENT, VERIFIED)

**Statement.** P1 (isomorphic sheaves glued in a cycle) forces `sigma` to **be** the
descent (Cech `H^1`) obstruction of the shard-cycle: the three isomorphic shards glue
to one global sheaf **iff** the composite monodromy is trivial, i.e. **iff
`sigma = +1`**; `sigma = -1` is a nontrivial `Z/2`-twisted local system (no global
orientation section). Consequently the **relative** orientation `c_ij = sigma_i *
sigma_j` is an **`alpha`-even 1-cochain** whose coboundary must vanish: on any triangle
of record-regions `c_12 * c_23 * c_31 = +1` **identically** for genuine products, which
**forbids the odd-parity assignments** (4 of the 8 triangle configurations).
[probe **[I]**: cocycle holds for all genuine products; 4 of 8 configs forbidden.]

**Independent or restates?** **INDEPENDENT.** The cocycle/descent condition is a
*consequence of P1's gluing structure*, not something I inserted; the vanishing
coboundary and the forbidden odd-parity set are forced by "three isomorphic sheaves
consistently glued," not by P2.

**Verify.** This is precisely the banked **"one globally consistent record arrow"**
(Prong 3 `F-FALSIFIABLE-CONSISTENT` WEAK; council Members 2/5's cup-product / Cech-`H^1`
descent rule; the "6-of-16-forbidden" prediction on 4 regions, here the triangle
version 4-of-8). It is also the cohomological face of the transferable triple
**objectivity `<=>` causal invariance `<=>` `H^1`(finality sheaf)`= 0`** (Prong 2's
one durable residue; Members 4/5): `sigma = +1 <=> H^1 = 0 <=>` records glue globally.
**VERIFIED-consistent, and directly falsifiable** (an observed odd-parity orientation
defect over a contractible region kills it) -- so C3 is a genuine prediction, not a
scaffold.

### C4 -- the null-stratum seam: forced to be a branch locus, but role/measure NOT forced (SCAFFOLD)

**Statement.** `sigma = -1` (nontrivial closure monodromy) forces the orientation local
system to have a **branch locus** -- a codim-1 wall where the sign is undefined,
Poincare-dual to `w1` -- and the seam is its natural home (`K_S` null `=> sigma`
undefined `=>` no backward-causal edge, resolved by the fresh-token closure, matching
Prong 2's non-causal seam). **But** the identification of that branch locus with the
`q<0` null stratum, and the **~8% measure**, are **NOT forced** by the posit.

**Independent or restates?** The *existence of a branch locus* is INDEPENDENT (forced
by nontrivial monodromy). Its *identity with the null stratum* and the *~8%* are
neither forced nor inserted here -- a **SCAFFOLD**.

**Verify.** This matches the banked status exactly: Prong 1/A found null-stratum
closure **UNESTABLISHED** (isospectral `(+64,-64)` `=>` realization-dependent; the
metric-loop crossing is mid-arc, not at the join; the `q<0` stratum proper is at the
noncompact ends, a distinct locus), and Prong 0 computes the ~8% as a **separate**
measure lemma. The construction **does not force** the coincidence and **does not
contradict** it. **SCAFFOLD; no contradiction.** (Honest: the posit *places* `sigma`
at the seam by P2; it cannot bootstrap the seam into the null stratum -- that remains
the open N2 operator-lift gap.)

## 4. Aggregate back-gate (verify the other way)

| # | consequence | tag | banked check | verdict |
|---|---|---|---|---|
| C1 | realization map `f` pinned `pi_1`-nontrivial | INDEPENDENT (of insert) / SCAFFOLD | Prong A (f free -> posit pins) | VERIFIED-consistent |
| C2 | `Z/6 = Z/2 x Z/3` direct product, `sigma _|_ tau` | **INDEPENDENT** | **Q3 `sigma _|_ tau`** | **VERIFIED** |
| C3 | descent cocycle = one globally consistent arrow | **INDEPENDENT** | one-arrow (Prong 3 / Members 2,5) | **VERIFIED** (falsifiable) |
| C4 | null-stratum branch locus / ~8% role | INDEP. existence / SCAFFOLD identity | UNESTABLISHED (Prong 0/1/A) | SCAFFOLD, no contradiction |

**No forced consequence CONTRADICTS a banked fact.** The two genuinely INDEPENDENT
consequences (C2, C3) both VERIFY banked results the posit did not insert. That is the
construction earning its keep, in the precise sense the prereg's three-tier rule
demands.

## 5. Planted-wrong-posit control -- CAUGHT (back-gate has power)

**PLANT (the prereg's required deliberately-wrong posit):** `sigma` = a shard-INTERNAL
orientation, **readable from inside one shard.**

**Why it must die, and does.** By P1 the three shards are **isomorphic**, so any
shard-internal datum is an **isomorphism-invariant** = **`alpha`-even**. An `alpha`-even
quantity is invariant under the deck flip, so it takes the **identical value in the
`sigma = +` world (anchor `K_S`) and the `sigma = -` world (anchor `-K_S`)** -- it
carries **0 bits** about `sigma`. The correct posit -- the **closure monodromy** -- is
**`alpha`-odd**: the signed anchor differs across the two worlds (`||K_S - (-K_S)|| =
||2K_S|| != 0`), carrying **1 bit** = `sigma`. [probe **[C]**: `I_even = 0` bit,
`I_odd = 1` bit, on the actual 128-dim `K_S`.]

So "`sigma` = shard-internal orientation" **asserts a readable `sigma`**, which
**CONTRADICTS Q2-FREE / the blindness lemma** (`Hom(triv, sign) = 0`, zero inward
channel capacity). The back-gate **REJECTS** it. It **ADMITS** the correct posit
because the closure monodromy is a **global** datum of the loop -- `alpha`-odd,
requiring a full traversal, unreadable inside any single stalk (a stalk kills `H^1`;
the germ sees the torsor, not the class). **The discriminator is exactly
readable-from-inside-one-shard (`alpha`-even, KILLED) vs. global-monodromy-of-the-loop
(`alpha`-odd, admitted)** -- the same axis Prong A/Q2 use, here realized on the
shard-internal-vs-cycle-global split. **The method has discriminating power: it is not
storytelling.** [probe `backgate_has_power = True`.]

## 6. Self-assessment (one line)

**The posit is `POSIT-PRODUCTIVE`:** it forces at least two **INDEPENDENT** consequences
it did not insert -- `sigma _|_ tau` as a `Z/6 = Z/2 x Z/3` direct product (**C2**,
verifies Q3, and demonstrates Q3-independence survives base-uniting) and the descent
"one globally consistent record arrow" (**C3**, verifies the banked one-arrow result,
falsifiable) -- **not** mere restatement; the headline realization-map compatibility
(**C1**) and the null-stratum role (**C4**) remain scaffold, and the
deliberately-wrong shard-internal posit is caught. The honest caveat: the strongest
INDEPENDENT wins (C2, C3) are **relational/orientation** facts about the cycle, not a
new **number** forced from `sigma`; the construction organizes the banked `sigma`/`tau`/
arrow structure into one coherent object and shows it is self-consistent and
discriminating, but it does **not** (and in construction mode must not) derive
`sigma`'s value.

## 7. Boundary

Exploration tier, CONSTRUCTION mode, posit declared. Only this artifact and its probe
(`tests/channel-swings/construction_prong1_structural_probe.py`, foreground,
deterministic two-run-identical, **EXIT 0**, `G=1 I=1 K=1 C=1` ALL PASS) were written.
`sigma` is kept **labelled as a POSIT** throughout; nothing here is promoted to canon
or claimed as a derivation of `sigma`'s value. GU otherwise read-only. No commit, no
push. No edit to any claim / canon / verdict / ledger / LANE-STATE / research-portfolio
/ NEXT-STEPS / prereg / frozen-packet file, or any other agent's artifact. No
claim-status, canon-verdict, or public-posture movement. The planted control was
declared before computation (docstring + section 5). All work is conditional at
exploration grade; nothing here is a GU verdict.
