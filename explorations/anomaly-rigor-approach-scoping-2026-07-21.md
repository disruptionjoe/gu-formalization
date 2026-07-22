---
title: "SCOPING the approach to making sigma's anomaly-protection rigorous -- the exact Omega^{Pin+}_14 computation the T1 shot (pin14-anomaly-number) left BLOCKED. Four personas reason INLINE in one worker (stable-homotopy/Adams-SS computationalist; bordism/Anderson-Brown-Peterson specialist; computational-algebra/formal-verification engineer; anomaly/physics theorist), then synthesize. This is a SCOPE-THE-APPROACH swing, NOT the computation: no probe run, no full resolution built. DECISIVE REFRAME (physics persona): the full group ORDER |Omega^{Pin+}_14| is NEITHER necessary NOR sufficient to settle ANOMALY-TRIVIAL. What excludes ANOMALY-TRIVIAL is a SINGLE invariant: one homomorphism phi: Omega^{Pin+}_14 -> Q/Z that is NONZERO on sigma's representative. This yields a cheapest-first LADDER: (rung 1, cheapest, ~T2-light) test whether a w1-monomial Stiefel-Whitney number of the observerse survives the forgetful map Omega^{Pin+}_14 -> Omega^O_14 -- if any is nonzero, sigma != 0 is proved WITHOUT the group order and WITHOUT the deck, ANOMALY-TRIVIAL excluded; (rung 2, if rung 1 vanishes into the Pin+ torsion kernel) build the group via the three named blockers AND evaluate the Pin+ eta-invariant on sigma's geometry -- the latter is T2-entangled and is the genuine residual hardness. BLOCKER TRACTABILITY: (1) h0-tower truncation lengths = a minimal A(1)-resolution of N through internal degree ~22 -- TRACTABLE NOW, bounded deterministic F_2 engine build (~400-700 lines extending the existing pin14 engine, cross-validated against Bruner's ext); (2) MSpin ABP corrections -- the summand list (ko, Sigma^8 ko<2>, Sigma^10 ko, Sigma^12 ko<2>) is PINNED by published ABP structure, their contributions are the SAME engine at cheaper stems 6/4/2, TRACTABLE with a literature-fidelity flag; (3) Adams d2/d3 + hidden 2-extensions -- mostly SUBSUMED into reading the h0-towers off the resolution (one v1-tower strongly constrains differentials), the one judgment-heavy residual, cross-checkable against Bruner-Greenlees ko^(RP-Thom) tables. THE CLASS GATE (T2) is the true blocker: which class sigma is needs the deck action, which the operator-grade swing found sigma-CIRCULAR -- so the exact class-assignment is NOT tractable from committed structure; the rung-1 SW route is the only sigma-free shot at class-nonvanishing and it may be too weak to see the torsion. HONEST BOTTOM LINE: the three 'blockers' compute the GROUP (tractable, well-posed, bounded) but the group is not the deliverable; the deliverable is sigma's-class-nonzero, whose cheap route (rung 1) is worth a dedicated pass NOW and whose fallback (rung 2 eta) stays T2-gated."
status: active_research
doc_type: exploration
created: 2026-07-21
outcome: "SCOPED (approach + minimum-sufficient computation identified). Recommended: run the cheapest-first ladder -- rung 1 (w1-SW-number survival under Omega^{Pin+}_14 -> Omega^O_14) is a bounded, largely T2-light pass that could settle ANOMALY-TRIVIAL now; the full |Omega^{Pin+}_14| order is a well-posed bounded engine build but is neither necessary nor sufficient; the class-assignment (rung-2 eta) stays T2-gated."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
directed_by: "Joe direct chat, 2026-07-21 (SCOPE the anomaly-rigor approach; 4 personas inline in one worker; scoping only -- no full computation, no commit/push)"
inputs:
  - explorations/pin14-anomaly-number-2026-07-21.md
  - tests/channel-swings/pin14_anomaly_number_probe.py
  - explorations/operator-grade-anomaly-banking-2026-07-21.md
  - explorations/pin-bordism-cardinality-2026-07-21.md
  - explorations/anomaly-inflow-swing-2026-07-21.md
  - tests/big-swing/fb_f2_adams_einvariant_obstruction.py
probe: NONE -- scoping pass only. No probe was run; no resolution engine was built. Everything below is design/estimation, not a certified computation.
---

# SCOPING the anomaly-rigor approach -- the exact Omega^{Pin+}_14 computation, scoped

> **CORRECTION (2026-07-22).** The ambient group computation proposed below is no longer a live task:
> Kirby--Taylor's direct table gives `Omega^{Pin+}_14 ~= Z/2` exactly.  The scoping's more important
> separation survives: knowing the group is neither sufficient nor a construction of the proposed GU class.
> That class still requires the missing operator/domain/line map.  See
> `explorations/pin14-smith-route-audit-2026-07-22.md` and
> `explorations/operator-to-anomaly-closure-campaign-2026-07-22.md`.

Four personas reason INLINE in this one worker (each in-character and independent,
then a synthesis; NEVER one agent per persona -- Joe's standing rule). This is a
**scope-the-approach** swing: it designs the best route to the number the T1 shot
(`pin14-anomaly-number`) left BLOCKED and identifies the MINIMUM computation that
rigorously excludes ANOMALY-TRIVIAL. It does **not** run the computation, build the
resolution engine, or bank any order. Nothing is promoted; the receptacle
`Omega^{Pin+}_14`, the proposal-grade anomaly-inflow identification, and the
`LC-SELECTOR` / `CARDINALITY-1 + PROTECTED` verdicts are **consumed, not moved**.

## 0. The state handed to the team (from the T1 shot)

`pin14-anomaly-number` genuinely reconstructed the *instrument*: the ABP reduction
`MTPin+ = MSpin ^ T`, `T = (RP^inf)^{3L-3}`; the leading ko-Adams
`E_2 = Ext_{A(1)}(N, F_2)` with `N = ~H^*(T)` built from the DERIVED action
`Sq^j x_i = C(i+3,j) x_{i+j}` and machine-verified a valid A(1)-module; both Margolis
homologies (`H(N;Q_0)=0`, `H(N;Q_1)=F_2 @ deg 1` => exactly ONE `v_1`-tower); and the
indecomposable generators at degrees `0,4,8,12`, **none at stem 14**. The NUMBER stayed
BLOCKED at three named sub-steps, and `sigma`'s specific 14-class stayed T2-gated:

- **(1)** the `h_0`-tower TRUNCATION LENGTHS at stem 14 (a verified minimal
  A(1)-resolution / the Bruner-Greenlees `ko ^ (RP^inf Thom)` values);
- **(2)** the MSpin ABP CORRECTION modules `Sigma^8 ko<2>`, `Sigma^10 ko`,
  `Sigma^12 ko<2>` smashed with `T`, at total degree 14;
- **(3)** the Adams `d_2`/`d_3` DIFFERENTIALS + hidden 2-extensions.
- **the class gate:** `sigma`'s SPECIFIC 14-class assignment (T2-gated -- needs the deck
  structure, which the operator-grade swing found `sigma`-CIRCULAR at operator grade).

What is REUSABLE from the T1 probe (`tests/channel-swings/pin14_anomaly_number_probe.py`):
the exact `F_2` rank/kernel engine (`f2_rank`), the graded A(1)-module class `Mod`
(`apply`/`compose`/`homology`/`indecomposables`), the derived `Sq` action on `N`, and the
Margolis validation on `F_2`/`A(0)` controls. What is MISSING: the *resolution loop*
(kernel-as-module + minimal-generator extraction + next differential), the `h_0`/`h_1`
Ext-multiplication bookkeeping, the ABP correction modules, and the differential/extension
analysis.

---

## Persona (i) -- Stable-homotopy / Adams-SS computationalist

**The route to the verified minimal A(1)-resolution of `N` through stem 14.**

`A(1)` is the 8-dimensional sub-Hopf-algebra `<Sq^1, Sq^2>` of the Steenrod algebra.
Computing `Ext_{A(1)}(N, F_2)` through stem 14 is a **finite, deterministic `F_2`
linear-algebra problem** -- there is no analytic difficulty, only bookkeeping. The
algorithm (standard minimal free resolution over a graded connected algebra):

1. Free cover `F_0 = A(1) (x) V_0 -> N`, `V_0 =` the indecomposables of `N`
   (the T1 probe already computes these: bottoms at `0,4,8,12`).
2. `K_0 = ker(F_0 -> N)`; find its minimal generators degree-by-degree
   (`= dim (K_0 / A(1)_+ K_0)_d`), giving `F_1 = A(1) (x) V_1 -> K_0`; the composite
   `F_1 -> F_0` is `d_1`.
3. Iterate: `K_s = ker(F_s -> F_{s-1})`, minimal generators `V_{s+1}`, next differential.
   Stop when `stem(V_s) > 14` for all future `s` (bounded: with one `v_1`-tower the
   Adams filtration at stem 14 is capped near `s ~ 7`, so `s <= ~8` and internal degree
   `<= ~22` suffice).

The `h_0`-tower TRUNCATION LENGTHS (blocker 1) fall straight out: `h_0 = [Sq^1] in
Ext^{1,1}`, and a length-`k` `h_0`-tower over a stem-14 class is exactly a `Z/2^k`
summand. So the resolution *is* the truncation data -- I do not need a separate
"BG table lookup"; the resolution reproduces the BG `nu` truncation function from first
principles (that is precisely what upgrades "recite the number" to "compute it").

**Reusable vs build.** REUSABLE: Bruner's `ext` C software is the canonical, decades-hardened
minimal-resolution engine for sub-Hopf-algebras of `A` (including `A(1)`) and is the natural
external authority; Sage's `SteenrodAlgebra`/`FPModule` (the Bruner-Rognes-Sage `sage.modules.fp_over_steenrod`)
can compute `Ext` over `A(1)` for finitely-presented modules and is scriptable; `steenroder`
(pure-Python) computes minimal resolutions over the full `A` (heavier than needed). MUST BE
BUILT (or adapted): the *encoding of `N`* -- `N = ~H^*((RP^inf)^{3L-3})` with the derived
`(1+a)^3`-twisted action -- as input to whichever engine, and, if we want the in-repo
deterministic artifact the house discipline prefers, a **pure-Python A(1)-resolution loop**
bolted onto the existing `Mod`/`f2_rank` engine (kernel-of-a-map-as-a-module is the one new
primitive; everything else the T1 probe already has).

**Controls that MUST pass (or discard):** the engine must reproduce `Ext_{A(1)}(F_2,F_2)` =
the ko lightning-flash chart (`h_0,h_1`, `(8,4)`-periodicity `v_1^4`); `Ext_{A(1)}(A(1)) =
F_2` (free is acyclic); and the anchors -- the same `N`-machine restricted to the
`RP^4 <-> Z/16` base must return a length-4 `h_0`-tower at stem 4 (the ABK order). If the
engine does not return `Z/16` at the `n=4` anchor, it is broken.

**Verdict (i):** blocker 1 is **TRACTABLE NOW**. It is a bounded, well-posed, deterministic
resolution -- the single most attackable of the three. Recommended: build the pure-Python
loop for the in-repo reproducible artifact AND cross-validate against Bruner `ext` for
independent authority. Estimated engine: ~400-700 lines on top of the existing probe.

---

## Persona (ii) -- Bordism / Anderson-Brown-Peterson specialist

**The MSpin correction modules and whether published ABP structure pins them.**

The splitting `MSpin_(2) = ko v Sigma^8 ko<2> v Sigma^10 ko v Sigma^12 ko<2> v ...`
is **Anderson-Brown-Peterson (1967), published and standard** -- the summand *list*
through degree 14 is pinned by the literature, not something we must rediscover. What is
NOT handed to us for free is each summand's **contribution to `Omega^{Pin+}_14 =
pi_14(MSpin ^ T)`**:

    pi_14( ko ^ T )            <- the leading term (blocker 1)
    pi_14( Sigma^8 ko<2> ^ T ) = pi_6 ( ko<2> ^ T )
    pi_14( Sigma^10 ko ^ T )   = pi_4 ( ko    ^ T )
    pi_14( Sigma^12 ko<2> ^ T ) = pi_2 ( ko<2> ^ T )

Two things I want to stress. First, the corrections are the **SAME engine at CHEAPER
stems** (6, 4, 2) -- they are strictly smaller computations than the leading term, so once
blocker 1's engine exists, blocker 2 is nearly free. `ko<2>` (the 2-connected cover) differs
from `ko` only by its bottom-cell structure: `H^*(ko<2>)` as an `A(1)`-module is
`A(1)//A(0) = A(1)/A(1)Sq^1` shifted, so it is *another finitely-presented A(1)-module* the
same resolution loop handles; smashing with `T` = tensoring the `A(1)`-module with `N` and
resolving. Second, the honest flags:

- **Literature-fidelity risk.** The precise summand at total degree 14 must be got exactly
  right (is the top correction `Sigma^12 ko<2>`, and is there a `Sigma^14`-summand touching
  `pi_0`?). A one-summand slip corrupts the group. This is a *read-the-ABP-paper-carefully*
  step, not a compute step -- so it is "pinned by published structure" **provided the
  transcription is verified against a second source** (Kirby-Taylor for Pin, or the
  Kapustin-Thorngren-Turzillo-Wang `1406.7329` Pin+ tables as an end-to-end control).
- **Assembly is not additive-trivial.** The four summand contributions are the associated
  graded; reassembling them into the actual abelian group is blocker 3's extension problem
  (below). Through degree 7 `MSpin = ko` so the leading term is exact; at `n=14` the
  corrections are genuinely present and must be added -- this is why `n=14` is strictly
  harder than the `n<=7` controls the prior probes certified.

An **alternative to the ABP-summand route** worth naming: work directly over the full
Steenrod algebra `A` with `H^*(MTPin+)` as an `A`-module (the "one big Adams SS" instead of
the ko-summand decomposition). This avoids the summand-transcription risk but is a much
larger `Ext` computation (over `A`, not `A(1)`) and loses the clean `v_1`-tower reading. I do
**not** recommend it -- the ABP-summand route is the standard tractable one and the T1 probe
already committed to it.

**Verdict (ii):** blocker 2 is **TRACTABLE** and *cheaper than blocker 1* once the engine
exists; the summand list is **pinned by published ABP structure**; the only genuine risk is
literature-transcription fidelity, mitigated by cross-checking against a second Pin+ table.

---

## Persona (iii) -- Computational-algebra / formal-verification engineer

**Can the resolution be machine-checked and reproducible, and at what build cost?**

Yes -- cleanly, and this is the discipline's strong suit. A minimal free resolution over
`A(1)` is a chain of `F_2` matrices `... -> F_2 -> F_1 -> F_0 -> N`. Everything is exact `F_2`
arithmetic: **no floating point, deterministic, byte-identical reruns** (the house standard the
existing probes already meet). The verification battery writes itself:

- **`d^2 = 0`** at every stage (composites of consecutive differentials vanish).
- **Minimality:** every differential has entries in the augmentation ideal `A(1)_+`
  (no unit/`degree-0` entries) -- this is what makes the resolution *minimal* and the
  `Ext` groups read directly off the generator counts `dim V_s`.
- **Exactness in range:** rank-nullity degree-by-degree (`im d_{s+1} = ker d_s`), the
  check the existing `f2_rank` already supports.
- **Control reproduction (KILL conditions):** `Ext_{A(1)}(F_2)` = the ko chart;
  `Ext_{A(1)}(A(1))` free-acyclic; the `RP^4 -> Z/16` anchor returns a length-4 `h_0`-tower.
- **Double-run byte-identical + fixed seed** (the repo convention), and an **independent
  authority cross-check**: encode `N` for Bruner's `ext` and confirm the same Betti table.
  Two engines (pure-Python in-repo + Bruner external) agreeing is the strongest reproducibility
  guarantee available and matches the "hostile-verify" posture.

**Tooling options, ranked for this repo.** (a) **Pure-Python on the existing engine** -- best
fit for the in-repo deterministic artifact; the only new primitive is "kernel of an
`A(1)`-map as an `A(1)`-module" (present the kernel `F_2`-basis, then close under `Sq^1,Sq^2`
and find minimal generators). Reuses `Mod`, `f2_rank`, the derived action. (b) **Bruner `ext`
(C)** -- authoritative, but old Unix C: compiling and encoding `N` as a `.def` module file is
fiddly and is an *external* dependency (flag: this is a build-environment cost, not a math
cost). (c) **Sage `fp_over_steenrod`** -- scriptable `Ext_{A(1)}`, good as a *second*
cross-check if Sage is available; heavier dependency. (d) **`steenroder`** -- pure-Python but
resolves over the full `A`; overkill.

**Build-cost estimate.** The pure-Python A(1)-resolution engine: **~400-700 lines** extending
the existing ~430-line probe (the resolution loop + `h_0`/`h_1` bookkeeping + control battery).
The ABP corrections (persona ii): **+~150-250 lines** (the `ko<2>` module + smash + three
cheaper resolutions). Cross-validation against Bruner `ext`: **hours-to-a-day of environment
work**, not code. Total: a **single dedicated engine-build pass**, foreground-feasible over one
focused session -- the same shape as the existing big-swing probes, materially larger than a
channel-swing probe.

**Verdict (iii):** **fully machine-checkable and reproducible**, deterministic, with a
two-engine cross-check available. Build cost is bounded and known: one dedicated engine pass,
~600-950 lines total in-repo plus optional external cross-validation. No formal-methods
blocker.

---

## Persona (iv) -- Anomaly / physics theorist (the decisive reframe)

**Do we actually need the full exact `|Omega^{Pin+}_14|` order -- or only "is `sigma`'s
14-class NONZERO (and its 2-adic order)"?**

This is the load-bearing question, and the answer changes the whole cost structure.
**ANOMALY-TRIVIAL means `sigma`'s class in `Omega^{Pin+}_14` is ZERO** (the reflection
symmetry is non-anomalous; the `{q=0}` wall could be trivially gapped/excised). To *exclude*
it we need `sigma != 0` in the receptacle. And the sharp fact is:

> The full group ORDER `|Omega^{Pin+}_14|` is **NEITHER necessary NOR sufficient** to settle
> ANOMALY-TRIVIAL. A nonzero group can still have `sigma = 0` inside it (the T1/cardinality
> docs already say the group being nonzero only makes trivial "disfavored," not excluded).
> What excludes ANOMALY-TRIVIAL is a **single homomorphism** `phi: Omega^{Pin+}_14 -> Q/Z`
> (a Pin+ bordism invariant) with `phi(sigma-representative) != 0`. **One nonzero invariant
> on the class settles it -- the whole group is unnecessary.**

This gives a **cheapest-first ladder**:

**Rung 1 (cheapest, largely T2-LIGHT) -- the forgetful map to unoriented bordism.**
Consider `f: Omega^{Pin+}_14 -> Omega^O_14`. If `x in Omega^{Pin+}_14` has `f(x) != 0`, then
`x != 0`. And `Omega^O_*` is *completely* detected by Stiefel-Whitney numbers (Thom). So:
**evaluate the `w_1`-monomial SW numbers of `sigma`'s carrier** (`sigma = w_1(L_time)`
committed; the observerse is 14-dim). If **any** `w_1(L)`-monomial SW number (e.g.
`w_1(L)^14`, or `w_1(L)^a w_i(TM)^...` of total degree 14) is nonzero, then `sigma`'s class
survives the forgetful map, is nonzero in `Omega^{Pin+}_14`, and **ANOMALY-TRIVIAL is excluded
-- without the group order and without the operator-grade deck action.** This uses only
committed structure (`sigma = w_1`, the observerse SW numbers) and is a **few-line
computation** -- the T1 probe already computes `w_1(L)^n[RP^n] = 1` for the generators;
extending to the observerse's 14-dim SW numbers is the same machinery.
- **The honest caveat (why this may fail):** SW numbers factor through `Omega^O`, and Pin+
  *torsion* can lie in `ker f` (invisible to SW). The `Z/16` at `n=4` is an ABK eta-invariant,
  NOT a SW number -- so if `sigma`'s 14-class is pure Pin+ torsion in `ker f`, rung 1 returns
  zero and proves nothing. Rung 1 is a **cheap shot that may miss**; it is decisive only if it
  fires.

**Rung 2 (if rung 1 vanishes) -- the Pin+ eta-invariant on `sigma`'s geometry.** The complete
detector of the torsion is the dim-14 Pin+ eta-invariant (the ABK/`Z/16`-analog one dimension
family up). Evaluating it needs (a) the group structure -- so that we know which eta-invariant
is the primitive detector and its modulus (this is exactly blockers 1-3, the group build) -- and
(b) `sigma`'s **representing geometry with its deck structure**. Step (b) is the T2 object, and
the operator-grade swing found it `sigma`-CIRCULAR at operator grade. So **rung 2 is
T2-GATED**: the eta route cannot be evaluated from committed structure alone.

**The minimum sufficient computation, stated exactly.** Not the group order. It is:
**a single Pin+ bordism invariant nonzero on `sigma`'s class.** Try it cheapest-first:
rung 1 (a `w_1`-SW-number survival check -- bounded, T2-light, could settle it NOW) before
rung 2 (the group build + eta on the T2 geometry -- larger, and class-assignment stays
T2-gated).

**Verdict (iv):** the decisive reframe is that **the three named "blockers" compute the GROUP,
but the group is not the deliverable.** The deliverable is `sigma`-class-nonzero. Its cheap
route (rung 1) is worth a dedicated pass immediately; its fallback (rung 2) inherits the T2
circularity. So the physics answer to "full order or just class-nonzero?" is: **just
class-nonzero -- and even that has a T2-free first attempt worth trying before the full machine.**

---

## SYNTHESIS -- the BEST plan

### The four lenses converge on a two-track plan

The computationalist, the ABP specialist, and the verification engineer agree that the
**group build (blockers 1-3) is tractable now**: a bounded, deterministic, machine-checkable
minimal-A(1)-resolution engine, cheaper corrections, and a differential/extension step that is
mostly subsumed by the `h_0`-tower reading. The physics theorist supplies the reframe that
**re-orders the work**: the group build is *sufficient-but-not-necessary* for the actual goal,
and there is a cheaper first shot at the goal.

**Recommended BEST plan -- cheapest-first, two tracks:**

- **Track A (do FIRST -- the minimum-sufficient shot):** the **rung-1 `w_1`-SW-number
  survival check**. Evaluate the `w_1(L_time)`-monomial Stiefel-Whitney numbers of the
  observerse (total degree 14) and test whether any is nonzero, i.e. whether `sigma`'s class
  survives `Omega^{Pin+}_14 -> Omega^O_14`. This is bounded, largely T2-light (uses committed
  `sigma = w_1` + the observerse characteristic numbers), reuses the existing probe machinery,
  and **if it fires, ANOMALY-TRIVIAL is rigorously excluded with no group order and no deck
  action.** ~a focused channel-swing-sized pass. HIGH VALUE / LOW COST -- run it before
  anything else.

- **Track B (the full instrument, if Track A vanishes or if the group order is wanted for its
  own sake):** the **minimal-A(1)-resolution engine build** resolving blockers 1-3:
  1. Blocker 1: build the pure-Python A(1)-resolution loop on the existing engine; read the
     `h_0`-tower truncation lengths at stem 14; controls = ko chart + `RP^4 -> Z/16` anchor;
     cross-validate against Bruner `ext`.
  2. Blocker 2: add the ABP corrections (`ko<2>` module + smash with `N`; resolutions at
     stems 6,4,2); transcribe the ABP summand list carefully and cross-check against a second
     Pin+ table (Kirby-Taylor / KTTW `1406.7329`).
  3. Blocker 3: read differentials/extensions off the single `v_1`-tower (`h_0`-towers give the
     `Z/2^k` extensions); the one judgment-heavy residual, cross-checked against the
     Bruner-Greenlees `ko ^ (RP-Thom)` values.
  This delivers the **exact `|Omega^{Pin+}_14|` group order** as a genuine, reproducible,
  two-engine-verified computation (not a recitation). The published value then serves as a
  **post-hoc engine control** (like the `Z/8`, `Z/16` anchors), NEVER as the deliverable.

- **The class gate (T2) -- the true residual, on BOTH tracks' far side:** pinning *which*
  element `sigma` is (needed for rung 2's eta evaluation, and for the exact 2-adic order of
  `sigma`'s class) requires the deck action, which is `sigma`-CIRCULAR at operator grade
  (operator-grade swing T2). **This is genuinely blocked and is NOT a computation the engine
  can supply** -- it needs the external operator-grade deck input, or Track A's SW route to
  sidestep it. Flag it honestly: the group order (Track B) can be banked; `sigma`'s *exact
  class* cannot, until T2 is broken non-circularly.

### Per-blocker + class-gate summary

| piece | best approach | minimum sufficient? | tooling | rough effort | tractable now? |
|---|---|---|---|---|---|
| **(1) `h_0`-tower truncation lengths** | pure-Python minimal A(1)-resolution of `N` through int. deg ~22; read `h_0`-towers at stem 14; cross-validate vs Bruner `ext` | needed only for Track B (group order); NOT needed if Track A fires | existing `f2_rank`/`Mod` engine + new resolution loop; Bruner `ext`; Sage `fp_over_steenrod` (2nd check) | ~400-700 lines | **YES** -- bounded, deterministic |
| **(2) MSpin ABP corrections** | same engine at stems 6,4,2 on `ko<2>`/`ko` smashed with `N`; transcribe ABP list, cross-check vs 2nd Pin+ table | needed only for Track B | same engine; ABP 1967 + KTTW `1406.7329` for fidelity | ~+150-250 lines | **YES** -- cheaper than (1); flag: literature-transcription fidelity |
| **(3) Adams `d_2`/`d_3` + hidden 2-extensions** | read off the single `v_1`-tower `h_0`-structure; cross-check vs Bruner-Greenlees `ko^RP` | needed only for Track B | same engine + BG tables as control | small (mostly subsumed) | **MOSTLY** -- one judgment-heavy residual; the exotic-differential risk |
| **class gate (T2): `sigma`'s specific class** | (Track A) `w_1`-SW-number survival under forgetful map -- `sigma`-free; else (Track B) Pin+ eta on the deck geometry | **THIS is the deliverable** -- and rung-1 is the minimum-sufficient shot at it | committed `sigma=w_1` + observerse SW numbers (Track A); eta-invariant machinery (Track B) | Track A: small pass; Track B eta: large + T2 | **Track A: largely YES** (worth a pass now). **Track B eta: NO** -- `sigma`-circular (needs external operator-grade deck input) |

### The MINIMUM sufficient computation to settle ANOMALY-TRIVIAL (the headline)

**Not the full order.** The minimum is **a single Pin+ bordism invariant nonzero on
`sigma`'s class.** Concretely, run **Track A first**: test whether a `w_1(L_time)`-monomial
Stiefel-Whitney number of the observerse survives `Omega^{Pin+}_14 -> Omega^O_14`. If any is
nonzero, `sigma != 0`, **ANOMALY-TRIVIAL is excluded** -- with no group order and no deck
action. This is bounded, largely T2-light, and reuses existing machinery. Only if Track A
vanishes into the Pin+-torsion kernel do you need Track B (the full group build) *and* the
Pin+ eta-invariant on `sigma`'s deck geometry -- and that eta step stays **T2-gated**
(`sigma`-circular).

### Honest hardness flags (where it is genuinely hard / blocked)

1. **The class gate is the real blocker, not the three named ones.** Blockers 1-3 are
   tractable engineering (they compute the GROUP). The group is neither necessary nor
   sufficient for ANOMALY-TRIVIAL. The genuinely hard/blocked piece is `sigma`'s *class*: the
   eta route to it is `sigma`-CIRCULAR (operator-grade T2). Track A is the only `sigma`-free
   shot, and it **may be too weak** (SW numbers miss Pin+ torsion). If Track A vanishes, the
   rigorous exclusion of ANOMALY-TRIVIAL **cannot be completed from committed structure** --
   it waits on breaking T2 non-circularly. State this plainly; do not let the tractable group
   build masquerade as settling the anomaly.
2. **Literature-transcription fidelity (blocker 2).** The ABP summand list through deg 14 must
   be exact; a one-summand slip corrupts the group. Mitigation: cross-check two Pin+ sources.
   This is a fidelity risk, not a math obstruction.
3. **The exotic-differential residual (blocker 3).** A single `v_1`-tower strongly constrains
   the Adams differentials, but a hidden `d_2` or a hidden 2-extension the pure `E_2` does not
   settle would need a secondary argument (a comparison map, or the BG `ko^RP` tables as an
   external check). Low-probability but real; flag it rather than assume collapse.
4. **Bruner `ext` is an environment cost.** The authoritative external cross-check is old Unix
   C; compiling it and encoding `N` is fiddly build-environment work (not math). The in-repo
   pure-Python engine is the primary deliverable; Bruner `ext`/Sage are the optional second
   opinion.

## Boundary

Exploration tier, **scoping only**. Only ONE new file was written -- this document.
**No probe was run; no resolution engine was built; no order was computed or banked.**
Everything above is design and estimation. GU otherwise read-only. **No commit, no push**
(the coordinator commits with explicit paths). No edit to LANE-STATE, research-portfolio,
NEXT-STEPS, canon, PP1/PP2/PP3, the anomaly-inflow swing, `pin-bordism-cardinality`,
`operator-grade-anomaly-banking`, `pin14-anomaly-number`, the LP-LC receipt, or any other
agent's artifact, or any claim/canon/verdict/ledger/portfolio file. No claim-status,
canon-verdict, paper-status, or public-posture change; the externality of `sigma`/`tau`, the
receptacle `Omega^{Pin+}_14`, the verdicts `LC-SELECTOR` and `CARDINALITY-1 + PROTECTED`
(proposal), and the proposal-grade anomaly-inflow identification are **consumed, not moved or
promoted**. The published `Omega^{Pin+}_14` value is named only as a *post-hoc engine control*
for a future Track B, never as a deliverable (reciting it as computed remains the forbidden
over-claim the T1 shot declined). Nothing routes externally (Joe alone publishes).

**Contribution.** Scopes the best approach to the T1-BLOCKED `Omega^{Pin+}_14` computation via
four inline personas, and delivers the decisive reframe: the three named blockers compute the
GROUP (tractable now -- a bounded, deterministic, two-engine-verifiable minimal-A(1)-resolution
build, ~600-950 lines in-repo), but the group is **neither necessary nor sufficient** to settle
ANOMALY-TRIVIAL. The minimum-sufficient computation is a **single Pin+ bordism invariant nonzero
on `sigma`'s class**, attacked cheapest-first: **Track A** (a `w_1`-SW-number survival check
under the forgetful map to `Omega^O_14`) is a bounded, largely T2-light pass that could exclude
ANOMALY-TRIVIAL **now**, if it fires; **Track B** (the full group build + Pin+ eta) is the
fallback, and its eta/class-assignment step stays **T2-gated** (`sigma`-circular). The honest
residual: the class gate, not the three named blockers, is the true hardness -- and Track A is
the only `sigma`-free shot at it.
