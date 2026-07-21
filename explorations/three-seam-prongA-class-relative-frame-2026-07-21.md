---
title: "Three-seam swing, Prong A (CLASS-RELATIVE CIRCLE FRAME): is sigma the ORIENTATION of the shard-cycle under a GU-native deck/Krein structure group? VERDICT A-NUMEROLOGY. reading-A (sigma = w1(L_time)) is canonical and forced; the BARE shard-cycle (type-quotient of the record helix) carries only the TRIVIAL tangent orientation (a torsor = the record-arrow choice, w1(TS^1)=0). Every reading-B construction (twisted coequalizer / deck-site H^1 / incidence-parity / consensus coequalizer) obtains sigma = cycle-orientation ONLY by decorating the cycle with a sign(K_S)-valued band the type-quotient does not carry; that band is not GU-forced (no functor transports K_S; Prong 2), its value is realization-dependent (K_S,-K_S isospectral; Prong 1 D0), and the fresh-token seam sign IS the inserted free coin sigma -- so 'cycle-orientation = sigma' is a tautology of insertion, not a derivation. reading-B is numerology; reading-A stands alone."
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-three-seam-swing-2026-07-21.md
outcome: A-NUMEROLOGY
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
kill_conditions_declared_before_computation: true
probe: tests/channel-swings/three_seam_prongA_class_relative_frame_probe.py
probe_exit: 0
inputs:
  - explorations/prereg-three-seam-swing-2026-07-21.md
  - explorations/shard-cycle-prong1-geometry-2026-07-21.md
  - explorations/shard-cycle-prong2-dynamics-gorard-2026-07-21.md
  - explorations/council-committed-constructions-extended-2026-07-21.md
  - explorations/council-committed-constructions-math-2026-07-21.md
  - canon/source-action-seiberg-witten-construction.md
  - tests/channel-swings/council_committed_w1_Ltime_probe.py (backbone reused)
  - tests/channel-swings/shard_cycle_prong1_geometry_probe.py (K_S transport reused)
---

# Prong A -- CLASS-RELATIVE CIRCLE FRAME

Adversarial truth-test, MAXIMUM skepticism, numerology gate ARMED. A construction
here would resolve the #1 contested seam, so it gets zero benefit of the doubt.
Three clean fits died on hostile verify this session for planting a convenient
object; this run plants nothing it does not then reject, and reports the outcome
the discipline forces rather than the outcome that would be a "find."

## 0. Verdict up front

> **`A-NUMEROLOGY`.** There is **no canonical, GU-native structure group under
> which sigma is the ORIENTATION of the shard-cycle.** reading-A
> (`sigma = w1(L_time)`, the arrow-of-time Moebius line bundle over `F ~ RP^3`)
> is canonical and **forced** -- the `pi_1(F)` generator loop transports the
> actual 128-dim `K_S -> -K_S` (residual `1.2e-16`). The **bare** shard-cycle
> (the type-quotient `S->I->O->S` of the record helix) carries only the
> **trivial** tangent orientation: `w1(TS^1) = 0`, and its "two orientations"
> (the record-arrow direction) are a free `Z/2` **torsor** -- a choice, not a
> nontrivial holonomy, so they **cannot** equal sigma. Every reading-B
> construction -- MTH-CAT's twisted coequalizer, MTH-SHEAF's
> `H^1(S^1_SIO; or_deck)` over a deck-site, EXT-HYPER's incidence-parity class,
> EXT-INTER's consensus coequalizer -- obtains "sigma = cycle-orientation"
> **only by decorating the cycle with a `sign(K_S)`-valued band/site/twist.**
> That decoration is not forced by GU: (i) the type-quotient does not carry
> `sign(K_S)` -- **no functor transports it** (Prong 2); (ii) even granting the
> band, its accumulation around the cycle is **realization-dependent** because
> `K_S` and `-K_S` are **isospectral** `(+64,-64)` (Prong 1 D0), so the `O->S`
> closure admits BOTH a flip path (`w1=1`) and a no-flip path (`w1=0`); and
> (iii) the type-quotient seam **mints a fresh token**, whose sign IS the free
> external coin sigma -- so "cycle-orientation = sigma" is a **tautology of
> insertion, not a derivation.** The "iso of `Z/2`'s" between cycle-orientation
> and `w1(L_time)` is the **pigeonhole identity** (`Z/2` has one nonzero element),
> which Prong 1 already showed is a powerless test. **reading-B is numerology;
> reading-A stands alone.**

This is **not** A-DISTINCT: A-DISTINCT would need a *canonical nontrivial*
cycle-orientation that differs from `w1(L_time)`. The only `Z/2`'s canonically
attached to the bare cycle are the **trivial** tangent class and the **trivial**-
class record-arrow torsor. There is no second canonical nontrivial datum to be
"distinct." So the fork lands on numerology, not distinctness.

## 1. The two readings, made precise as cohomology of two different loops

- **reading-A (solid).** `sigma = w1(L_time) in H^1(F ~ RP^3; Z/2) = Z/2`. The
  loop is the `pi_1(F)` generator -- a loop of **timelike lines in the METRIC
  FIBER** `F = GL(4,R)/O(3,1)`. Going around it once, the tautological
  time-line's section flips: `K_S -> -K_S`. **Forced** by canonical structure:
  the deck involution `U` (`rot(0,9,pi)`, `U K_S U^{-1} = -K_S`) is a fixed
  algebraic object (source-action canon), and `w1(L_time) != 0` is its monodromy.
  Probe [A]: `deckA_residual = 1.2e-16`, `U^2` closes (`2.4e-16`).

- **reading-B (the open one, tested here).** `sigma = ` the orientation of the
  **shard-cycle** `S^1_SIO` -- the type-quotient of the record helix (Prong 2:
  the acyclic issuance helix winds forward forever; forgetting the winding number
  sends it onto the oriented 3-cycle `S->I->O->S`). The loop is in the **issuance
  TYPE space**, a different object from the metric fiber.

For reading-A and reading-B to be **one** `Z/2` in two structure-classes, GU must
supply a **canonical map** `f: S^1_SIO -> F` whose induced
`f^* : H^1(F;Z/2) -> H^1(S^1_SIO;Z/2)` sends `sigma` to the generator (i.e. `f`
is `pi_1`-nontrivial), **and** the whole thing must be forced, not chosen. The
rest of this doc computes each link and finds every one un-forced.

## 2. The candidate GU-native frame, built explicitly

The council's live reading-B constructions (math Members 2/4/5, extended
Members 3/4) all instantiate the **same** frame in different languages:

| construction | native structure group | the cycle-orientation object |
|---|---|---|
| MTH-CAT (category theorist) | a `Z/2`-twist of the identity functor, **band = `sign(K_S)`** | global element of the twist torsor over the colimit of `S/I/O` |
| MTH-SHEAF (sheaf/cohomology) | Grothendieck topology whose **covers are refined by `sign(K_S)`-transitions** | `H^1(S^1_SIO; or_deck) = Z/2` |
| EXT-HYPER (hypergraph) | incidence line bundle with **`sign(K_S)` incidence parity** | `w1` of the incidence bundle on the cycle-space class `z in ker(partial)` |
| EXT-INTER (intersubjectivity) | consensus coequalizer with **`sign(K_S)` circulation** | orientation of the coequalizer cycle |

Stripped of language, the frame is: **equip `S^1_SIO` with the real line bundle
`L_deck` whose transition cocycle is `sign(K_S)`,** and read `w1(L_deck) in
H^1(S^1_SIO; Z/2) = Z/2`. `w1(L_deck)` is the generator **iff** `sign(K_S)`
accumulates to `-1` around one `S->I->O->S` traversal. This is the single number
the whole reading-B program reduces to, and it is exactly the decisive
computation the prereg demands.

The class-relative principle Joe correctly flagged is granted in full: **`w1`
depends on the chosen structure group**, and over `S^1` there genuinely DO exist
nontrivial real line bundles (the Moebius band, `w1 != 0`) -- the standard
`w1(TS^1) = 0` is only the *tangent* structure group. So the question is never
"does a nontrivial line bundle over the cycle exist" (it does); it is **"does GU
CANONICALLY force the nontrivial one, with band `= sign(K_S)`, as *the
orientation of the cycle*?"** Sections 3-6 answer: no, at four independent links.

## 3. Link 1 -- the bare cycle's own orientation is TRIVIAL (probe [B])

"The orientation of a circle" denotes `w1` of the circle's **own tangent
bundle**. The type-quotient `C_3 = (S->I->O->S)` is an orientable circle: its
cyclic-successor direction is a globally consistent nonvanishing field that
returns to itself, so `w1(TS^1) = 0`. Its two cyclic orderings
`{S->I->O, S->O->I}` -- which is the **record-arrow direction** -- form a **free
`Z/2` torsor** (two elements, no canonical basepoint): a *choice*, a *section*,
**trivial class**. A torsor (no obstruction) can never equal sigma (a nontrivial
holonomy, `w1(L_time) != 0`). This is Prong 1's discriminator, now realized on
the *cycle* object rather than the metric loop: **the record-arrow torsor is the
possessable alpha-odd section; sigma is the unreadable alpha-even obstruction --
they are the two different `Z/2` data the model's slogan conflates.**

So the literal reading-B ("sigma = the orientation of the shard circle") is
**dead** for the same reason Prong 1 killed the slogan: orientable circle,
trivial class. To survive, reading-B must mean `w1` of some *other* bundle
`L_deck` over the cycle -- which is §4-§6.

## 4. Link 2 -- the deck band is NOT a function of the shard-type (probe [C])

`L_deck`'s transition data is `sign(K_S)`. But the type-quotient **forgets
everything but the type.** Two record helices with the **same** type-sequence and
**different** `sign(K_S)` patterns produce the **identical** type-quotient
(probe [C]: `helix1` ksign `+,+,+,...` and `helix2` ksign `+,-,+,-,...` both give
the edge set `{S->I, I->O, O->S}`). Therefore **`sign(K_S)` is not a function of
the shard-type** -- it is EXTRA structure laid onto the cycle, not read off it.
This is Prong 2's finding made exact: the rewriting/type apparatus is
combinatorial and **no functor transports `sign(K_S)`** (nor `GL(4,R)/O(3,1)`,
nor `q`, nor the null stratum) onto the quotient. To put the band on the cycle
you must **import** it. Importing the answer is the numerology gate's trip-wire.

## 5. Link 3 -- the accumulation is REALIZATION-DEPENDENT, and self-inserted (probe [D])

Grant the import anyway and ask: does `sign(K_S)` accumulate to `-1` around the
cycle? This reduces to "does the `O->S` closure apply the deck flip `U`?" GU does
**not** force it, on two counts:

1. **Isospectral, so not forced (Prong 1 D0, verified here on the actual `K_S`).**
   `K_S` and `-K_S` are isospectral `(+64,-64)`. The seam therefore admits BOTH:
   - **`R_flip`**: apply `U` once (`K_S -> -K_S`, residual `1.2e-16`) -> cycle
     product `-1` -> `w1(L_deck) = 1`.
   - **`R_noflip`**: apply an invertible isospectral loop `U^2` that returns
     `K_S` (residual `2.4e-16`) -> cycle product `+1` -> `w1(L_deck) = 0`.
   Both are genuine closures on the real 128-dim `K_S`; GU pins **neither**. A
   canonical class cannot be realization-dependent -- and this one splits
   (`deck_class_realization_dependent = True`).

2. **The fresh-token seam sign IS the inserted coin (Prong 2).** The `O->S`
   closure mints a **fresh token**; a fresh token samples a fresh `K_S` with its
   own sign, which is the **free external coin sigma** (Q2-FREE: the first person
   hosts sigma and forces its externality but cannot supply its value). So the
   seam sign is sigma **by insertion**. "Cycle-orientation = sigma" then holds
   trivially -- because you placed sigma at the seam by hand
   (`cycle_orientation_is_inserted_sigma = True`). That is circular: sigma out
   because sigma in.

## 6. Link 4 -- the realization map to `w1(L_time)` is a FREE `Z/2` (probe [E])

The prereg's decisive check: exhibit the realization map (native cycle-orientation)
`-> ` (standard `w1(L_time)`) and test whether it is an **iso of `Z/2`'s**.

A map `f: S^1_SIO -> F` induces `f^* : H^1(F;Z/2) -> H^1(S^1_SIO;Z/2)`, and
`f^*(sigma)` is the generator **iff** `f` is `pi_1`-nontrivial. GU provides no
canonical `f`: the issuance/type dynamics (Prong 2) carries no metric-fiber data,
and the metric-fiber loop (Prong 1) is a separate object. A **degree-0** (constant)
`f` gives `f^*(sigma) = 0`; a **degree-1** (wrap-once) `f` gives the generator
(probe [E]: `fstar_sigma_deg0 = 0`, `fstar_sigma_deg1 = 1`). Both maps exist; GU
forces neither. So `f^*(sigma)` is a **free `Z/2`**, and there is **no canonical
iso** to exhibit. The "reconciliation" is available only if you *choose* `f`
`pi_1`-nontrivial -- i.e. plant the answer.

**Net:** reading-B is not "reading-A relocated by a canonical map" (which would
reconcile). It is "reading-A relocated by a **chosen** map," and the choice is
exactly the planted `Z/2`. The apparent `sigma = w1(L_deck) = w1(L_time)` is the
**pigeonhole identity** `Z/2 = Z/2` with the connecting map hand-picked --
precisely the powerless test Prong 1 named.

## 7. The planted control -- REJECTED, with power demonstrated (probe [F])

- **PLANT-1** (the prereg's required plant): *"any quotient/coequalizer carries
  sigma as its orientation."* If true, the bare cycle's orientation would be
  sigma, predicting `w1(TS^1) = 1`. Computed `w1(TS^1) = 0` (§3). **REJECTED.**

- **PLANT-2** (the sharper, construction-level plant): *"decorate the cycle with
  a `sign(K_S)` band/site/twist and read `w1`."* This is what MTH-CAT / MTH-SHEAF
  / EXT-HYPER / EXT-INTER actually do. It returns `w1 = 1` for `R_flip` and
  `w1 = 0` for `R_noflip`, both valid GU closures -> the decorated class is **not
  GU-determined** -> **REJECTED as non-canonical.** (Strip the decoration and you
  are back to the trivial tangent class of §3.)

- **POWER.** The method returns a **single forced value** (`-1`, every
  realization) for the reading-A metric-fiber loop -- because there `U` genuinely
  IS the monodromy of `L_time` -- but a **realization-split value** (`+1` or `-1`)
  for the shard-cycle. A pigeonhole method that only noted "both are `Z/2`, so
  identify them" would return "same" and could never reject the plant. This
  method distinguishes **forced** (reading-A) from **imported** (reading-B), so it
  has power. `method_has_power = True`.

## 8. What survives, and why the seam-through-null hope also fails

The strongest steelman for A-RECONCILED is: *"the cycle closes at the null-`K_S`
seam (Prong 2), and crossing null-`K_S` flips `sign(K_S)` (the definite sign is
undefined at `K_S = 0` and emerges as `-K_S`), so the cycle intrinsically applies
the deck flip -- no import needed."* It fails on **three banked results**, any one
sufficient:

- **Not forced (Prong 1 D0):** `K_S, -K_S` isospectral -> an invertible path
  connects them without going null -> "closes THROUGH null" is realization-
  dependent, exactly §5.1.
- **No transport at the seam (Prong 2):** the seam mints a fresh token; it does
  not transport `K_S` at all -> nothing to flip; the sign is re-sampled (the free
  coin), exactly §5.2.
- **Locus mismatch (Prong 1 D2/D4):** even the metric loop's null crossing is
  **mid-arc** (`t = 1/4, 3/4`), not at the join; and the `q<0` stratum proper is
  at the noncompact ends, a **distinct locus** from the compact cycle. So "null AT
  the join" is unmatched.

**What genuinely survives is exactly reading-A:** `sigma = w1(L_time)`, the Moebius
class of the arrow-of-time line bundle = the spin/belt-trick class of
`pi_1(F ~ RP^3)`. It IS an orientation class -- of a canonical **line bundle**,
obstructing a global time-arrow -- and it is canonical, forced, computed. It is
just **not** the orientation of the shard cycle, in any GU-forced structure group.

## 9. Verdict and consequence for the swing

- **Outcome: `A-NUMEROLOGY`.** No canonical GU-native frame carries sigma as a
  cycle-orientation. reading-A stands alone.
- **Is `sigma = cycle-orientation = w1(L_time)`?** **No.** `sigma = w1(L_time)`
  (canonical). `cycle-orientation` is either the **trivial** tangent torsor (the
  record-arrow choice, §3) or an **imported, realization-dependent, self-inserted**
  band (§4-§6). The equality holds only by planting the connecting map (§7), which
  the method rejects with demonstrated power.
- **Consequence (per prereg synthesis).** Prong A was the #1 contested seam. It
  does **not** dissolve into A-RECONCILED: the "class-relative" move is legitimate
  in general (orientability is structure-group-relative) but does **not** rescue
  reading-B here, because GU does not canonically pick out the nontrivial band or
  the `pi_1`-nontrivial realization map. The honest standing story is unchanged:
  **the bit is `Z/2 = w1(L_time)` = the spin class of the metric fiber's timelike
  line bundle** -- already the frozen packet's content -- and the
  "sigma = orientation of a first-person/consensus/quotient circle" reading is
  **retired as numerology**, not banked as a second face of the same object. The
  council's Members 2/4/5/EXT constructions that leaned on it are, at this seam,
  **planting a convenient object**; their *other* legs (the confluence <-> H^1
  triple, the generation counting, the descent/cocycle relative-orientation rule)
  are untouched by this verdict.

## 10. Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/three_seam_prongA_class_relative_frame_probe.py`,
foreground, deterministic two-run-identical, **EXIT 0**, `A=1 B=1 C=1 D=1 E=1
F=3`, ALL PASS) were written. GU otherwise read-only. No commit, no push. No edit
to LANE-STATE, research-portfolio, NEXT-STEPS, the prereg, the frozen packet,
Prong 0/1/2, the council docs, any claim/canon/verdict/ledger file, or any other
agent's artifact. No claim-status, canon-verdict, or public-posture movement. Kill
conditions were declared before computation (docstring + the CONTROLS block; the
plants run in the probe as PLANT-1/PLANT-2). All work is conditional at exploration
grade; nothing here is a GU verdict.
