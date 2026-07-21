---
title: "Prong 1 (GEOMETRY, make-or-break): sigma is a canonical Z/2 orientation class -- of the ARROW-OF-TIME LINE BUNDLE over F~RP^3, NOT of the shard 1-cycle; the model's 'Z/2 = the two orientations of a circle' slogan is FALSIFIED (circles are orientable, orientation class 0); the canonical congruence loop DOES transit the null cone at the light-cone quarter-turns but the crossing is not topologically forced (K_S,-K_S isospectral (64,64)) and is mid-arc not at the join, so 'necessarily closes through the null stratum' is unestablished. Verdict G-PARTIAL."
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-oriented-shard-cycle-swing-2026-07-21.md
inputs:
  - explorations/prereg-oriented-shard-cycle-swing-2026-07-21.md
  - explorations/blockbuster-p3-one-bit-dossier-v2-2026-07-19.md
  - explorations/source-packet-coflip-holonomy-freeze-2026-07-20.md
  - explorations/oracle-relative-prong0-measure-lemma-2026-07-21.md
  - canon/source-action-seiberg-witten-construction.md
  - tests/channel-swings/sig_b5_habitat_probe.py (the canonical generator loop, reused verbatim)
probe: tests/channel-swings/shard_cycle_prong1_geometry_probe.py (foreground, deterministic two-run-identical, EXIT 0; 12 [E] + 2 [F] = 14 ALL PASS)
outcome: G-PARTIAL
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
---

# Prong 1 -- GEOMETRY: is sigma the orientation class of a canonical 1-cycle?

Adversarial truth-test, MAXIMUM skepticism. This is the make-or-break prong: a
"constructed" result would be a real find, so it gets zero benefit of the doubt,
and the numerology gate is armed -- if the object cannot be CONSTRUCTED from
canonical GU structure, it is dropped. Three clean fits died on hostile verify
this session for planting a convenient object; this run plants nothing and reports
the one FAIL the first pass produced (Sec. 4) rather than tuning it away.

## 0. Verdict up front

> **`G-PARTIAL`.** A canonical nontrivial Z/2 holonomy exists and IS an
> orientation class -- but of the **arrow-of-time LINE BUNDLE** over the metric
> fiber, **not** of the shard 1-cycle qua circle. Precisely:
>
> 1. **pi_1(F) = Z/2, canonically.** `F = GL(4,R)/O(3,1)` deformation-retracts
>    onto `RP^3` (the signature-(3,1) involutions `I - 2P`, = the timelike lines).
>    `pi_1(RP^3) = Z/2`. The generator loop has double-cover monodromy `-1`, its
>    square closes. [computed; matches the frozen packet]
> 2. **sigma = w_1(L_time), a genuine orientation class -- of the time bundle.**
>    The co-flip holonomy equals the first Stiefel-Whitney class of the
>    **tautological timelike-line bundle** `L_time` over `F~RP^3` (the arrow of
>    time = the `-1` eigenline of the metric-involution). `w_1(L_time) != 0`
>    (Moebius): a section flips sign around the loop -- this IS the co-flip. So
>    "sigma is an orientation class" is **true** -- it is the obstruction to
>    globally choosing a time direction around the canonical loop.
> 3. **But sigma is NOT the orientation of the shard CIRCLE.** A circle is
>    **orientable** (`w_1(T S^1) = 0`); its "two orientations" form a
>    **trivial-class Z/2 torsor**, which cannot equal a nontrivial holonomy. The
>    model's slogan "**Z/2 = the two orientations of S^1**" is **FALSIFIED**. The
>    real source of the "2" is the **non-orientability of `L_time`** / the
>    **SPIN double cover `S^3 -> RP^3`** (the belt-trick class), not the two
>    directions of a circle.
> 4. **Null-stratum closure: partially consonant, not as stated.** The canonical
>    **congruence** realization of the loop DOES transit the null cone -- the
>    transported `K_S(t)` is exactly singular at the light-cone quarter-turns
>    `t = 1/4, 3/4` (a `+` leg goes eta-null), the same `q=0` wall Prong 0 names.
>    BUT (a) `K_S` and `-K_S` are **isospectral** (`(+64,-64)`), so the crossing
>    is **not topologically forced** -- an invertible connecting path exists and
>    a different realization avoids null; and (b) the transit is **mid-arc**, not
>    at the **join** (`t=0=1`, where `K_S(1) = -K_S` is nondegenerate). The
>    model says the cycle "closes THROUGH the null stratum" (null AT the join);
>    that placement is **not matched**. So "**necessarily** closes through the
>    null stratum" is **unestablished** and reduces to Prong 0's open N2 gap.
>
> The make-or-break claim (**sigma = orientation of a canonical observerse
> 1-cycle**) is therefore **not** constructed as stated: sigma orients a
> canonical LINE BUNDLE, not the cycle. A real, computed, canonical object
> survives (sigma = `w_1(L_time)` = the spin/belt-trick class), which is why this
> is PARTIAL and not NUMEROLOGY -- but the specific "circle-orientation" mechanism
> and the "closes through the null stratum" geometry are falsified/unestablished.

## 1. pi_1(F) for F = GL(4,R)/O(3,1) -- the computation

`F` is the space of nondegenerate symmetric bilinear forms of signature `(3,1)`
on `R^4` (`GL(4,R)` acts by congruence `g -> A^T g A`; the stabilizer of the
standard form is `O(3,1)`). This is the program-native metric fiber of
`Y14 = Met(X^4)` (per `GEOMETER-VS-PHYSICS-OBJECTS`), not a standard-physics
substitute.

**Retraction onto RP^3.** Any signature-`(3,1)` form spectrally retracts onto the
reflection `I - 2P_L`, `P_L` the orthogonal projector onto its `1`-dim negative
(timelike) eigenline `L`. Such reflections are exactly `{signature-(3,1)
involutions}`, parametrized by the timelike **line** `L in RP^3`. So

> `F = GL(4,R)/O(3,1) ~ RP^3`, hence `pi_1(F) = pi_1(RP^3) = Z/2`.

The straight-line homotopy `g -> I - 2P_L` keeps signature `(3,1)` (probe/packet
sampled), so it is a genuine deformation retraction. **This is a fully canonical
computation** -- it uses only `GL(4,R)`, the `(3,1)` signature, and Sylvester's
law. The covering-space step `pi_1(RP^3) = Z/2` (given the simply-connected double
cover `S^3`) is typed IMPORTED-standard, matching the frozen packet's own typing.

**The generator loop.** The canonical generator (reused verbatim from the habitat
probe) is the loop of timelike lines `v(t) = (sin pi t, 0, 0, cos pi t)`,
`t in [0,1]`. Its continuous lift to `S^3` returns **anti-periodic**
(`<v(1),v(0)> = -1`: monodromy `-1`); the squared loop closes (`+1`). Order
exactly `2`. [probe Part A]

**Cross-check against the group homotopy the prereg asked for.** `GL(4,R)` has two
components; `GL^+(4,R) ~ SO(4)`, `pi_1 = Z/2`. `O(3,1)` has four components; its
identity component `SO^+(3,1) ~ SO(3)` (maximal compact), `pi_1 = Z/2`. The
homotopy quotient is governed by the maximal-compact pair `O(4)/(O(3)xO(1)) =
Gr(3,4) = RP^3` -- identical to the retraction result. The `Z/2` is real and
canonical, from every route.

## 2. Orientation-class analysis -- the crux, and the pigeonhole trap

The prereg's technical target for a WIN: sigma = "the orientation double-cover
class of a canonical bundle over a canonical cycle / a first-Stiefel-Whitney-type
class." The trap that MUST be avoided: `H^1(RP^3; Z/2) = Z/2` has **exactly one**
nonzero element, so **any** nontrivial Z/2 monodromy over `F` -- sigma, `w_1` of
the tautological bundle, `w_1` of anything non-orientable -- is **automatically**
the same class, by pigeonhole, with **zero content**. A test that only checks
"do the classes agree in `H^1`" has no power (it is exactly the planted control,
Sec. 5). The test must separate distinct Z/2 DATA on the loop:

- **(i) `w_1(T S^1)` -- the orientation of the CYCLE ITSELF** (the "two
  orientations of a circle"). A circle is **orientable**: the loop's tangent
  frame `dg/dt` is smooth and periodic, returning to ITSELF (`<T(1),T(0)>_F =
  +1.0000`, probe Part B). So `w_1(T S^1) = 0`. The two orientations are a
  **trivial-class torsor** -- a choice, not a class.
- **(ii) `w_1(L_time)` -- the tautological TIMELIKE-LINE bundle.** The arrow of
  time = the `-1` eigenline. Its continuous unit section flips sign around the
  loop (`<v(1),v(0)> = -1.0000`, probe Part B): the **Moebius** bundle,
  `w_1(L_time) = 1 != 0`. This non-orientability -- you cannot consistently orient
  time around the loop -- **IS the co-flip**.
- **(iii) sigma -- the loop-transport of the actual `K_S = e_0...e_8`.** The mixed
  `(0,9)`-plane loop sends `K_S -> -K_S` (`|K_trans + K_S| = 1.2e-16`, probe
  Part B): nontrivial, `= 1`.

**The discriminator (probe Part B, decisive):**

> `sigma = w_1(L_time) = 1  !=  0 = w_1(T S^1)`.

sigma is the orientation class of the **arrow-of-time line bundle**, NOT the
orientation of the shard circle. The two Z/2 data are **different on the same
loop** -- so the identification is NOT the vacuous pigeonhole, and the model's
slogan "`Z/2` = the two orientations of `S^1`" is **falsified**: the circle's own
orientation class is `0`, and `0 != sigma`.

**The honest positive residue.** `w_1` of any line bundle IS "the orientation
class of that bundle." sigma = `w_1(L_time)` is a genuine, canonical orientation
class -- of `L_time` (time direction), obstructing a global arrow of time around
the loop. This is real and computed. What the geometry **cannot** do, because
`H^1(RP^3;Z/2) = Z/2` is one-dimensional, is single sigma out from "any nontrivial
Z/2" at the class level; the SEMANTIC content (this class = the co-flip = time
orientation) is carried by the physics (the frozen packet), not by a finer
cohomological computation. That is exactly why this is PARTIAL, not CONSTRUCTED.

## 3. The double cover is the SPIN cover, not an orientation cover

sigma's `-1` monodromy corresponds to the double cover `v ~ -v : S^3 -> RP^3`
(the lift runs from `v(0)` to `-v(0)` INSIDE the cover; probe Part C, residual
`1.2e-16`). This cover is **connected** (`S^3` simply connected).

> An **orientation** double cover of an **orientable** manifold is **disconnected**
> (two copies). `RP^3` is orientable (`RP^n` orientable iff `n` odd; probe
> confirms `det(B_t) = +1` around the loop, so `w_1(T RP^3) = 0`). Hence sigma's
> cover is **NOT an orientation double cover** -- it is the **SPIN cover**
> `SU(2) -> SO(3)` (`RP^3 ~ SO(3)`), the belt-trick / 2pi-vs-4pi class.

This is the sharpest statement of what the "2" is: the non-orientability of a
canonical **line** bundle (`L_time`), equivalently the spin double cover -- a
`w_1`-of-a-bundle / spin datum, **not** the orientation of the base 1-manifold
(which is zero). The model reached for the right *kind* of object (a Z/2 that is
"which of two" with an externally-set value -- and the two lifts to the spin cover
/ the two orientations of `L_time` ARE such a torsor) but named the wrong carrier
(the circle's own two directions).

## 4. Null-stratum closure -- the FAIL the first pass produced, reported straight

The first probe pass asserted "the loop avoids null-`K_S`" and **FAILED**. The
computation refuted the assertion; it is reported, not tuned away.

- **The metric never degenerates.** Signature `(9,5)` is constant along the loop
  (Sylvester). The base metric is fine everywhere. [probe Part D, D3]
- **But the transported Krein form DOES go null -- mid-arc.** Along the canonical
  **congruence** loop (`g_t = A_t^T eta A_t`, the packet's own realization), the
  transported `K_S(t) = kprod(A_t^{-1})` is **exactly singular** at
  `t = 1/4, 3/4` (`sigma_min ~ 4e-18`), precisely where the moving `+` leg
  `f_0(t) = cos(pi t) e_0 - sin(pi t) e_9` becomes **eta-null** (Clifford square
  `eta(f_0,f_0) = cos(2 pi t) = 0`). This is a **light-cone crossing** -- the
  same `q = P - T = 0` wall Prong 0 names (spacelike<->timelike exchange). So the
  co-flip loop, as canonically realized, **does transit null-`K_S`**. [probe D1]
- **Two reasons this does not vindicate the model as stated:**
  1. **Not forced.** `K_S = e_0...e_8` has signature `(+64,-64)`; so does `-K_S`.
     They are **isospectral**, hence connectable by an invertible (conjugation)
     path -- a null-crossing is **not topological**. Whether a loop crosses null
     is **realization-dependent**. [probe D0]
  2. **Wrong locus.** The transit is at the **quarter-turns**, not at the
     **join**. At `t=0` (`K_S`), `t=1/2`, `t=1` (`-K_S`) the form is invertible
     (`sigma_min = 1`). The model says the cycle "closes THROUGH the null stratum"
     (null AT the join, where sigma is undefined and the backward-causal edge is
     erased). The join is **nondegenerate**. [probe D2]
- **The q<0 stratum proper is elsewhere.** Prong 0's `q<0` stratum (`~8%` of
  genuine ends) lives at the **noncompact flat-geodesic ends** (`||g_s|| ->
  infinity`), retracted away onto compact `RP^3`; the loop stays bounded
  (`<= 2.00`). The loop's mid-arc light-cone transit and the end-stratum are
  **distinct loci**; the model's identification of the join with Prong 0's ends
  is not established. [probe D4]

**Net null-stratum finding:** the canonical congruence realization crosses the
null cone (mildly consonant with the model's picture), but the crossing is not
forced (isospectral) and is mis-placed relative to the model's claim (mid-arc, not
the join). "Necessarily closes through the null stratum at the join" is
**unestablished**, and its truth reduces to the still-open N2 operator-lift /
`P=0`-stratum question Prong 0 named. This is the PARTIAL's second horn.

## 5. Planted control -- REJECTED, with the power demonstrated

**Plant:** "any Z/2 bit is the orientation of SOME circle." If true, sigma (a
nontrivial Z/2) would BE the orientation class of the cycle, i.e. predict
`w_1(T S^1) = sigma = 1`.

**Rejection (probe Part E):** the computed circle-orientation class is
`w_1(T S^1) = 0` while sigma `= 1`. A circle is **orientable**, so **no**
nontrivial Z/2 is its orientation class; the plant conflates a **trivial-class
torsor** (the two directions of an orientable circle) with a **nontrivial
holonomy** (`w_1` of a twisted line bundle). REJECTED.

**Power (probe Part E):** the test returns **different** Z/2 for the two objects
on the **same** loop -- `0` for the tangent (`w_1(T S^1)`), `1` for the
tautological bundle (`w_1(L_time)`). So it CAN tell "sigma orients the cycle" from
"sigma orients a canonical line bundle over the cycle." A method that only checked
class-agreement in `H^1(RP^3;Z/2) = Z/2` would return the same for both (pigeonhole)
and could not reject the plant. This test has power **because** it computes the
distinguished class `w_1(T S^1)` of a NAMED object and finds it `0`.

This is exactly the discipline the prereg demanded: the cycle must be canonical and
its orientation class **computed, not asserted** -- and when computed, the cycle's
own orientation class is `0`, killing the "circle orientation" reading while
leaving the line-bundle reading standing.

## 6. Verdict and what it does to the model

- **Outcome: `G-PARTIAL`.**
- **What is CONSTRUCTED (keep):** `pi_1(F) = Z/2` canonically (`F ~ RP^3`); sigma
  = `w_1` of the canonical tautological **timelike/arrow-of-time line bundle**
  `L_time` = the **spin/belt-trick class** of `pi_1(RP^3)`. sigma IS an orientation
  class -- of `L_time` -- and its non-orientability IS the co-flip (obstruction to
  a global time arrow around the loop). Canonical, computed, program-native.
- **What is FALSIFIED (do not ship):** "**sigma = the orientation of the shard
  circle**" / "**Z/2 = the two orientations of `S^1`**." A circle is orientable
  (`w_1(T S^1) = 0`); its orientation is a trivial-class torsor and cannot equal a
  nontrivial holonomy. The "2" is the non-orientability of a canonical line bundle
  / the spin cover `S^3 -> RP^3`, not the two directions of a circle.
- **What is UNESTABLISHED (the second PARTIAL horn):** "**the cycle necessarily
  closes through the null stratum.**" The canonical congruence realization DOES
  transit the null cone, but mid-arc (not at the join) and not forced (`K_S,-K_S`
  isospectral `(64,64)`); the q<0 stratum proper is at the noncompact ends
  (Prong 0), a distinct locus. Truth reduces to the open N2 operator-lift gap.
- **Consequence for the swing (per prereg synthesis):** Prong 1 was the
  make-or-break. The geometric story is **not** numerology (a real canonical
  orientation class survives), but it is **not** the claimed circle-orientation
  either -- sigma orients the arrow-of-time LINE BUNDLE, not the shard cycle. So
  the "why the bit is Z/2 = two orientations of a circle" explanation is retired;
  the honest replacement is "the bit is Z/2 = the spin/`w_1` class of the metric
  fiber's timelike line bundle," which was already the frozen packet's content and
  is **not** a new geometric mechanism. Prongs 2-3 therefore stand or fall on
  their own; they cannot inherit a geometric grounding from here.

## 7. Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/shard_cycle_prong1_geometry_probe.py`, foreground,
deterministic two-run-identical, **EXIT 0**, 12 [E] + 2 [F] = 14 ALL PASS) were
written. GU otherwise read-only. No commit, no push. No edit to LANE-STATE,
research-portfolio, NEXT-STEPS, the prereg, the frozen packet, Prong 0, the
one-bit dossier, any claim/canon/verdict/ledger file, or any other agent's
artifact. No claim-status, canon-verdict, or public-posture movement; the
externality of the bit's VALUE is untouched (Kramers blindness unaffected). Kill
conditions were declared before computation (prereg + the planted control run in
the probe before GU's case). The first pass produced one FAIL (Sec. 4); it was
reported and the assertion corrected to the computed truth, not tuned to pass. All
work is conditional at exploration grade; nothing here is a GU verdict.
