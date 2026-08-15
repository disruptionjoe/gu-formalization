---
artifact_type: exploration
status: exploration
doc_type: metric-cone-boundedness-gate
created: 2026-08-14
work_item: MC-1
channel: metric_cone_boundedness_of_the_src3_runaway
title: "MC-1: the cone of Lorentzian metrics does NOT bound SRC-3's runaway, and the reason is stronger than a failure to bound -- the DeWitt-negative direction IS the cone's own dilation generator, so the cone's defining invariance certifies the runaway is unobstructed. Four independent exact routes: (R1) GL(4,R) is transitive on the cone and the trace-reversed Frobenius metric is exactly equivariant, so the signature is (6,4) at EVERY point and no basepoint improves it; (R2) the unique flipped direction is h = g, the Euler/dilation vector, and a cone is by definition dilation-invariant; (R3) the full 4-dimensional DeWitt-negative subspace has exact exit criterion det(g0 + t h) = -(1+ta)^2[(1+ta)^2 + t^2|b|^2], so the ray stays in the cone for all t >= 0 iff a >= 0 -- a closed half-space of COMPLETE rays to infinity, and the complementary half runs to the VERTEX at bounded field norm, i.e. was never a runaway; (R4) type audit -- SRC-3's parameter t scales the CONNECTION over a FIXED point of Y14 and never travels in the cone at all, and under the one complete cone motion (dilation) both Q and K rescale by the same positive mu^-2 so the sign of K is invariant. VERDICT: the twenty-lens flag is a MISAIMED CRITIQUE -- its premise (the fibre is not a vector space) is true and already banked, but SRC-3 never linearised the cone; it used only the pointwise signature of the DeWitt metric on T_p Met, which is the correct object and is constant across the whole cone by homogeneity. SRC-3's cause (2) STANDS."
grade: "EXACT sympy Rational and integer arithmetic; no floating point is load-bearing anywhere. Inertia computed TWO independent exact ways (Descartes sign-changes on the Berkowitz characteristic polynomial of a real-rooted symmetric matrix; exact symmetric congruence reduction over Q) with agreement asserted on every matrix. 60/60 checks (44 [E] exact results, 16 [C] controls with discriminating power), exit 0. Non-vacuity established two ways: 16 live controls that must return the OTHER answer (the cone-exit test fires on h = -g0 at t = 1 and on h = E_33 at t = 1; lambda = 0 and lambda = 1/8 must NOT give (6,4); the Riemannian cone IS convex on the same machinery; forgetting the tangent transport DOES break equivariance; the two SRC-3 values differ in sign; substituting any of the six positive directions into the negative block destroys negative-definiteness in all six cases; a size-3 perturbation does leave the cone); and FOUR mutation tests (lambda 1/2 -> 1/8: 12 failures, exit 1; drop the transpose in the tangent transport: 3 failures, exit 1; swap E_03 for E_01 in the negative block: 4 failures, exit 1; put a < 0 into the complete-ray list: 3 failures, exit 1). NOT: a claim that the potential is bounded, a gauge determination, a contour-rotation analysis, a statement about the reduced 4d action, or any claim-status movement."
disposition: THE_METRIC_CONE_DOES_NOT_BOUND_THE_SRC3_RUNAWAY__THE_DEWITT_NEGATIVE_DIRECTION_IS_THE_CONES_OWN_DILATION_GENERATOR__SRC3_CAUSE_2_STANDS__THE_TWENTY_LENS_LINEARISATION_FLAG_IS_A_MISAIMED_CRITIQUE_WITH_A_TRUE_PREMISE__ROUTE_CLOSED_NEGATIVE
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - canon/shiab-existence-cl95.md
  - explorations/W168-reduction-krein-signature-2026-07-14.md
  - explorations/canon-met-x4-contractibility-type-defect-2026-08-09.md
  - explorations/five-lens-analytic-council-2026-08-08.md
  - explorations/HYPOTHESIS-moduli-negative-not-time-negative-2026-08-09.md
  - explorations/conformal-factor-mode-gauge-status-2026-07-11.md
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/W213-true-vacuum-effective-potential-2026-07-14.md
  - explorations/W159-tachyon-escapes-2026-07-14.md
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/n2-end-family-2026-07-20.md
  - explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md
  - explorations/decision-tree-Q1a-hostile-verify-2026-07-21.md
  - explorations/twentyfive-lens-council-on-the-signature-decision-2026-08-08.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/channel-swings/joe_directed_cone_boundedness_probe.py
---

# MC-1 — Does the geometry of the metric cone bound SRC-3's unbounded potential?

**Answer: No — and the reason is sharper than "it fails to bound." The DeWitt-negative
direction is the generator of the very dilation that makes the cone a cone. Cone geometry
does not merely decline to obstruct the runaway; it certifies the runaway is unobstructed.**

## 0. The target claim, stated so the verdict is claim-indexed

Per the kill doctrine, this file types its verdict against one written claim:

> **TARGET CLAIM (TC-CONE).** *"SRC-3's cause (2) — the `(6,4)` signature of the internal
> DeWitt metric on the fibre of `Y14 = Met(X4)` — is an ARTIFACT of linearising a CONE as a
> vector space. The fibre of `Met(X4)` is not `Sym^2(T*X)`; it is the open cone `C` of
> signature-`(3,1)` forms, a curved homogeneous space `GL(4,R)/O(3,1)` with a boundary at
> `det g -> 0`. If SRC-3's runaway directions leave `C`, they are not physical field
> directions and the unboundedness evaporates."*

**Verdict: TC-CONE is REFUTED.** Its *premise* is true — and is already banked in this
repository, twice, at hostile-review grade. Its *inference* fails four independent ways.

The failure has a name: **misaimed critique**. SRC-3 never linearised the cone. SRC-3 uses
exactly one property of `Met(X4)`: the signature of the DeWitt metric on the tangent space
`T_p Met` at a single point. That is the correct object for what SRC-3 does with it, and it
is **constant across the entire cone** by homogeneity. The critique attacks a step SRC-3
does not take.

## 1. Prior-art sweep by mechanism — what is standard, what is banked, what is new

This section is the attribution contract. Nothing below the line marked NEW is claimed.

### 1.1 Standard literature (cited, not claimed)

| Object | Source | Where the repo already cites it |
|---|---|---|
| The supermetric on the space of metrics; its indefiniteness; its one-parameter family | DeWitt, *Phys. Rev.* **160** (1967) 1113 | `explorations/W168-reduction-krein-signature-2026-07-14.md` `external_refs` |
| The **conformal factor problem** — the trace/conformal mode carries the opposite signature to the transverse-traceless modes, and the standard treatment is contour rotation | Gibbons, Hawking & Perry, *Nucl. Phys.* **B138** (1978) 141 | `W168`, `W122`, `W78`, `HYPOTHESIS-moduli-negative` |
| `Sym^2(T*X)` isotypic decomposition under `O(p,q)` | Besse, *Einstein Manifolds* §1.G | `canon/w2-y14-spin-structure.md`, `W168` |
| Superspace geometry; degenerate metrics at finite DeWitt distance under the density weight | Fischer; Giulini | *not previously cited in this repo* — added here |
| Fourth-order spectrum, spin-0 scalaron | Stelle (1977); Salvio–Strumia; Starobinsky | `W78`, `W79` |

**The conformal factor problem is the negative direction of the DeWitt metric.** This is
not a discovery of this file, nor of this repository. `HYPOTHESIS-moduli-negative-not-time-negative-2026-08-09.md`
states it plainly and correctly: *"The indefiniteness of the DeWitt supermetric is standard
canonical gravity, not a GU artifact"* and *"The indefiniteness of the DeWitt supermetric
**is** the conformal-factor problem of Euclidean quantum gravity ... open since
Gibbons-Hawking-Perry (1978)."* That attribution is already right and this file inherits it.

### 1.2 Already banked in this repository (reproduced as cross-checks, not claimed)

- **`(7,3) -> (6,4)` under trace reversal.** `canon/shiab-existence-cl95.md` Step 1, canon
  tier, prose. Reproduced here by independent computation (Layer 2 of the probe).
- **The single flipped direction is the conformal/trace mode; the threshold is `lambda > 1/4`;
  `lambda = 0` leaves it positive.** `explorations/W168-reduction-krein-signature-2026-07-14.md`
  (`tests/W168_reduction_krein_signature.py`), with the threshold also in
  `explorations/n2-end-family-2026-07-20.md`. **W168 owns this.** Every check in this probe
  that reproduces it is tagged `W168 REPRODUCED (not new)`. W168's own sentence is the right
  one: *"GU's verified `(6,4)` is the SAME fact as conformal-negative."*
- **Non-convexity of the Lorentzian locus, and the `Met_Riem` / `Met_Lor` type defect.**
  `explorations/five-lens-analytic-council-2026-08-08.md` (which corrected a false
  `[verified]` tag) and `explorations/canon-met-x4-contractibility-type-defect-2026-08-09.md`
  finding **D8**. The five-lens council's sentence is exactly the distinction TC-CONE rests
  on: *"`Sym^2(T*_x X)` — the full space of symmetric forms — **is** a convex vector space.
  The **Lorentzian-signature locus inside it** is not, and that is GU's fibre."* The finding
  is theirs; this probe supplies the first machine-checked certificate of it.
  **Repair status, checked directly:** the finding *was* integrated into canon as
  `CORRECTION NGM-01` inside `canon/no-go-class-relative-map.md` itself. The **inline §2.3
  sentence is still unedited** — it reads *"Met(X^4) is contractible (convex cone)"* at
  line 219 — so the file states the wrong thing in the body and the right thing in the
  correction block. That is a cosmetic residue of a properly-filed correction, not an open
  defect, and it is reported here only so nobody re-files it as one.
- **Moduli provenance of the four fibre negatives.** `HYPOTHESIS-moduli-negative...` Half A,
  computed. Its warning — *"provenance does not move a symbol"* — is the correct discipline
  and this file obeys it: nothing here claims the negatives dissolve.
- **Gauge status of the conformal mode: PHYSICAL, not gauge.**
  `explorations/conformal-factor-mode-gauge-status-2026-07-11.md` /
  `tests/W78_conformal_mode_gauge_status.py`, three independent ways (DOF/constraint count;
  Weyl-BRST plus the GHP scope argument; the H49 fork-closure that GU must break conformal
  invariance to survive rotation curves). **This is the repo's own strongest result against
  the "it's just gauge" escape, and it is GU-native, not literature.**
- **The other unbounded-below result.** `W213` (`V_eff(u) = -64u^2 - 8u + 2`, unbounded both
  ways, unique stationary point a maximum), `W126` (the potential sector terminates at `R^2`
  identically, all orders), `W159` (the only bounding mechanism on record is a **DBI velocity
  wall** at `v^2 = 1/16`, explicitly *"a speed-limit, not a restoring force"*, bounding
  velocity and **not excursion**). `W153` proves the tachyon **lives in** the conformal mode.
- **The fibre end.** `explorations/decision-tree-Q1a-fiber-end-classification-2026-07-21.md`
  argues degeneration happens *"only at the actual metric-degeneration boundary, at infinite
  invariant distance ... not along interior directions to infinity"* — and
  `decision-tree-Q1a-hostile-verify-2026-07-21.md` **blocks** it on the ground that
  `GL(4,R)/O(3,1)` has non-compact isotropy `O(3,1)` and therefore **admits no invariant
  Riemannian metric**, making "complete Riemannian implies limit-point" ill-typed. Layer 5
  below is written to respect that block.

### 1.3 NEW here — and it is only this

1. The **cone-boundedness adjudication** R1–R4 against SRC-3. The prior-art sweep found the
   question *"does the metric cone bound the runaway?"* was **never posed** anywhere in this
   repository. Three files (`W168` conformal-negative, `W153` tachyon-lives-there, `W213`
   unbounded-below) name one direction and were never composed.
2. The **exact exit criterion on the whole DeWitt-negative subspace**:
   `det(g0 + t h) = -(1+ta)^2 [ (1+ta)^2 + t^2 (b0^2+b1^2+b2^2) ]`, giving a clean
   iff-condition `a >= 0`.
3. The **structural observation R2** that the DeWitt-negative direction is the cone's own
   Euler/dilation generator, so cone-invariance and DeWitt-negativity are the same fact
   read twice. (W168 computed `G(g,g) = 4 - 16*lambda = -4`; identifying that vector as the
   cone's dilation generator, and drawing the boundedness consequence, is the new step.)
4. The **density-weight fork** (Layer 5): the standard finite-distance-to-the-boundary
   statement holds for weight `w > 0` and **fails at `w = 0`**, which is canon's metric.
5. The **Layer 6 answer** to the never-posed question, for the `W213`/`W159` runaway.
6. The first **machine-checked certificate** of the `Met_Lor` non-convexity (finding D8's
   counterexample had only ever been checked ad hoc).

## 2. Pre-flight — five specialist lenses, run inline, each proposing a route

Recorded **before** computing, with the cheapest kill-or-switch and one contrary route named
in advance.

### Lens 1 — Riemannian geometer of the space of metrics

`Met(X)` is a homogeneous space. That is the whole game: `GL(4,R)` acts transitively on the
`(3,1)` locus by Sylvester, and the Frobenius/DeWitt metric is built from `g^{-1}` twice, so
it must be equivariant. Signature is a pointwise algebraic invariant of a homogeneous
equivariant tensor, hence **constant on the orbit**. TC-CONE needs the signature to be a
basepoint artifact; homogeneity forbids that outright.

> **ROUTE R1.** Verify transitivity constructively, verify the equivariance identity
> `S(A)^T G_{A^T g A} S(A) = G_g` exactly, then read signature at several genuinely
> different cone points. **Cost: cheap.** **This is the cheapest kill-or-switch in the
> whole wave** and should run first.

### Lens 2 — Euclidean quantum gravity / conformal-factor specialist

I recognise this object. The trace-reversed DeWitt metric's negative direction is the
conformal factor, and I have been staring at it since 1978. Two things the geometer will not
say. First: the standard treatment is not "the cone bounds it" — nobody has ever proposed
that — it is **contour rotation**, which leaves the real cone entirely, so a real-cone
argument is silent on the standard resolution either way. Second: the standard
*finite-distance-to-degenerate-metrics* statement carries a **density weight** `sqrt(g)`. If
this repo's fibre metric is the unweighted pointwise Frobenius metric, the standard statement
does not transfer, and someone will eventually quote it as if it does.

> **ROUTE R5 (Layer 5).** Compute the DeWitt pseudo-arc-length along the conformal ray with
> a general weight `|det g|^w`. Find where `w = 0` sits. **Cost: cheap, symbolic.**
> **This is the contrary route worth recording**: the strongest live objection to any
> negative result here is that GHP contour rotation makes the whole real-cone question moot.

### Lens 3 — Convex-geometry / cone specialist

Careful with the word "cone." `C` is a cone in the *dilation* sense (`lambda > 0` invariance),
**not** in the convex sense — the repo has already caught itself conflating those. And a
dilation-invariant set has a distinguished vector field: the Euler field `h = g`. If that
vector happens to be the DeWitt-negative one, TC-CONE is not just wrong, it is inverted: the
cone structure *guarantees* the negative ray is complete. Also note the asymmetry — the
dilation ray runs to infinity one way and to the **vertex** the other way, and only one of
those is a runaway.

> **ROUTE R2 + R3.** Compute `G(g,g)`; then characterise exactly which rays in the
> 4-dimensional negative subspace exit. Split the answer by direction, and check whether the
> exiting rays are even divergent. **Cost: cheap symbolically (a 4x4 determinant).**

### Lens 4 — General relativist

Ask what is actually being scaled. SRC-3's `V(tv) = t^2 Q(v) + t^4 K(v)` scales `v`, and `v`
is a connection perturbation, `v` in `T*_p Y14 (x) ad`. The cone is where `p` lives. If `t`
scales a fibre of a *different* bundle over a fixed `p`, then the cone's boundary is not on
`t`'s itinerary and TC-CONE is a category error before any geometry runs. Also: what happens
to `K` if we *do* move `p`? Both `Q` and `K` contract two form indices with `g^{-1}` twice,
so under `g -> mu g` both should pick up `mu^{-2}` — the **same positive** factor.

> **ROUTE R4.** Type-audit SRC-3's ray; then compute the homogeneity degree of `Q` and `K`
> under the dilation. **Cost: cheap.**

### Lens 5 — Honesty auditor

Three specific traps, from this repository's own history.

1. **Do not claim novelty.** `W168` has already computed the conformal-negative
   identification and the `lambda > 1/4` threshold, and the non-convexity is banked twice.
   Grep before writing "new"; the repo has an eight-false-novelty incident on record.
2. **A clean negative is the honest default here** and must be stated as a result, not as a
   failure. If the runaway stays inside the cone, say so plainly.
3. **Vacuous PASSes.** Every claim about a ray staying in the cone is a check that can pass
   by the test never firing. Demand a live control in which the cone-exit test **does** fire,
   and mutation tests.

> **ROUTE R0.** Two independent exact inertia implementations that must agree; live controls
> with the opposite expected answer; mutation testing before shipping.

### Lens 6 — Adversarial referee

I will press the negative result, not the positive one, because the negative is what will be
shipped. Three attacks, declared now:

- **A1.** "You showed the *basis* directions give complete rays; a general vector in the
  4-dimensional negative subspace might not." — Answer this with a symbolic determinant over
  the whole subspace, not with examples.
- **A2.** "You computed the negative subspace *at one point* and then talked about rays that
  leave that point. The metric changes along the ray; the tangent may stop being negative." —
  Answer with `G` evaluated **along** the ray.
- **A3.** "SRC-3's negative ray with both legs spacelike is cause (1), the Killing form, not
  cause (2). You may be adjudicating the wrong ray." — Correct, and load-bearing. Locate the
  cause-(2) ray specifically: one leg on a DeWitt-negative internal direction.

**Pre-committed cheapest kill-or-switch: R1.** If the DeWitt signature had turned out to vary
across the cone, TC-CONE would have had a real mechanism and the route would have switched to
hunting the definite locus. **Pre-committed contrary route: R5 / GHP contour rotation** — the
one live way TC-CONE's conclusion could be reached by a different argument.

## 3. The big swing — results

Probe: `tests/channel-swings/joe_directed_cone_boundedness_probe.py`. **60/60 exact checks,
exit 0** (44 `[E]`, 16 `[C]`). All arithmetic is sympy `Rational`/integer. Inertia is computed
two independent exact ways — Descartes sign-changes on the Berkowitz characteristic polynomial
(an equality, not a bound, for the real-rooted polynomial of a symmetric matrix) and exact
symmetric congruence reduction over `Q` — with agreement **asserted** on every matrix.

### 3.1 Setup, cross-checked against canon

| Quantity | Value | Status |
|---|---|---|
| Frobenius metric on the fibre, `lambda = 0` | `(7,3)` | canon cross-check, reproduced |
| Trace-reversed, `lambda = 1/2` | `(6,4)` | canon cross-check, reproduced |
| `G_lambda(g,g)` | `n - lambda n^2 = 4 - 16 lambda` | W168 reproduced |
| Critical parameter | `lambda_c = 1/n = 1/4` | W168 / `n2-end-family` reproduced |
| `dim C` | `16 - 6 = 10`, by exact rank of `M -> M^T g + g M` on `gl(4)` | new certificate |
| `C` convex? | **No** — `diag(1,1,1,-1) + diag(-1,1,1,1)` is degenerate | D8 cross-check, first machine certificate |
| Riemannian control | convex on the same machinery | live control |

### 3.2 R1 — the signature is constant on the whole cone

The equivariance identity `S(A)^T G_{A^T g A} S(A) = G_g` holds **exactly** on every witness
(`S(A)` is the `10x10` matrix of `h -> A^T h A`). Combined with transitivity, the
trace-reversed DeWitt metric has inertia `(6,4)` at **every** point of `C`.

> **There is no point of the metric cone at which the DeWitt metric is definite.** The
> negative block has exactly 4 dimensions everywhere. "Move to a better basepoint" is not
> available, and the curvature of `C` is irrelevant, because signature is pointwise algebraic.

Live control: forgetting to transport the tangent vector **does** break the identity, so the
check is not vacuous. Mutation (drop the transpose): 3 failures, exit 1.

### 3.3 R2 — the negative direction is the cone's own dilation generator

`G_{1/2}(g0, g0) = -4 < 0`. The vector `h = g` is the Euler field of the cone: the generator
of the `lambda > 0` scaling invariance that **is** the definition of a cone.

Along the ray, `G_{1/2}|_{(1+t)g0}(g0, g0) = -4/(1+t)^2 < 0` for every `t > -1` — it stays
negative all the way out, answering referee attack **A2**.

> **This is the sharpest statement in the file.** The DeWitt-negative direction is not merely
> *a* direction that happens to remain in the cone; it is the direction whose completeness is
> *equivalent to `C` being a cone at all*. Cone geometry cannot bound this runaway without
> ceasing to be cone geometry.

Live control: under the *raw* Frobenius metric the same direction is `+4`, so the sign is
produced by trace reversal and the computation can return either answer.

### 3.4 R3 — the exact exit criterion on the entire negative subspace

The four DeWitt-negative directions at `g0 = diag(1,1,1,-1)` are named explicitly and
certified `G`-orthogonal to the six positive ones (cross-Gram exactly zero):

- the **conformal / dilation** direction `g0` itself, and
- the three **mixed space-time** directions `E_03, E_13, E_23`.

Substituting *any* of the six positive-block directions for the conformal one destroys
negative-definiteness in all six cases — so this is the `(6,4)` splitting itself, not a
coincidence of basis. This answers referee attack **A1** at the level of the naming.

For a **general** element `h = a g0 + b0 E_03 + b1 E_13 + b2 E_23` of the negative subspace:

```
det(g0 + t h) = -(1 + t a)^2 [ (1 + t a)^2 + t^2 (b0^2 + b1^2 + b2^2) ]
```

The bracket is a sum of squares, so the ray leaves `C` **exactly** where `1 + t a = 0`.

> **The ray `g0 + t h` stays inside the cone for every `t >= 0` if and only if `a >= 0`.**

That is a **closed half-space** of the 4-dimensional DeWitt-negative subspace — with nonempty
interior — consisting of **complete rays running to infinity inside `C`**. Verified on
explicit rational instances out to `t = 10^12`. **Answer (a), not (b).**

And the other half is not a runaway at all:

> The `a < 0` half exits at the finite parameter `t = 1/|a|`, but it exits **toward the
> vertex** — `det g -> 0`, the metric shrinking. On the closed parameter interval the field's
> Frobenius norm is bounded (at the exit parameter it is exactly `0`). A direction that
> terminates at zero field is not a direction along which a potential can run to minus
> infinity. **So the exiting half was never a candidate runaway, and the cone truncates
> nothing that was diverging.**

Live controls that fire: `h = -g0` leaves `C` at exactly `t = 1`; `h = E_33`, which is
DeWitt-**positive**, also leaves at `t = 1` — so exiting is uncorrelated with the DeWitt sign,
and the cone-exit test demonstrably has power.

### 3.5 R4 — the type audit, and referee attack A3

SRC-3 reproduced from scratch in exact integer arithmetic: `K = -4` with both internal legs
spacelike; `K = +4` for the same bracket with one leg timelike. Both values recovered; the
sign difference is a live control.

**A3 is correct and is honoured.** The `K = -4` ray is **cause (1)** (Killing indefiniteness
on `k`). **Cause (2)** is the separate fact that a `k`-valued `v` with one leg on a
DeWitt-**negative** internal direction flips the quartic negative even when the Killing form
is restricted to be definite. Cause (2)'s ray is the one adjudicated here, and R1 places it:
since the inertia is `(6,4)` at every point of `C`, a mixed-sign pair of internal legs
**exists at every point of the cone**. There is nowhere to stand where cause (2) is absent.

The type fact, which is decisive on its own:

> SRC-3's parameter `t` multiplies `v` in `T*_p Y14 (x) ad` — the **connection** fibre over a
> **fixed** point `p` of `Y14`. It does not move `p`. The cone is the space `p` lives in.
> The cone's boundary is not on `t`'s itinerary, at any `t`.

And if one nonetheless insists on moving `p`: under the dilation `g -> mu g` (`mu > 0`), the
two-inverse-metric contraction that builds **both** `Q` and `K` rescales by exactly `mu^{-2}`,
so `V(tv; mu g) = mu^{-2} V(tv; g)`.

> **The sign of `K` is invariant along the entire dilation ray** — which is the one cone
> direction that provably never exits. The only complete cone motion available is exactly the
> motion that cannot change the answer.

### 3.6 Layer 5 — the density-weight fork (Lens 2's contribution)

With a density weight `|det g|^w`, the conformal ray toward the degenerate boundary has
DeWitt pseudo-length `1/w`:

- **`w > 0`** (Wheeler–DeWitt superspace normalisation): the degenerate boundary is at
  **finite** distance. **Standard — DeWitt 1967; Giulini. Reproduced, not claimed.**
- **`w = 0`** (canon's unweighted pointwise Frobenius fibre metric on `Y14`): the same
  boundary is at **infinite** distance. **The standard finite-distance statement does not
  transfer to canon's metric unchanged.**
- The **outward** conformal ray — the runaway direction, `det g -> infinity` — has infinite
  length for **every** `w >= 0`. No choice of density weight truncates the runaway.

Two honesty notes on this layer, both owed:

1. The conformal direction is DeWitt-**timelike**, so `sqrt(|G|)` is a *pseudo*-length, not a
   metric distance. This is why the layer is stated as a length computation along one named
   curve and not as a completeness theorem.
2. `decision-tree-Q1a-hostile-verify-2026-07-21.md` established that `GL(4,R)/O(3,1)` has
   non-compact isotropy and therefore **admits no invariant Riemannian metric**, so
   "complete Riemannian implies X" arguments are ill-typed on this fibre. Layer 5 makes no
   such argument. It also **corroborates** the surviving half of
   `decision-tree-Q1a-fiber-end-classification`'s claim (degeneration only at the boundary,
   at infinite distance) **for `w = 0` specifically** — and shows that claim would be false
   for any positive density weight, which is a caveat that file does not carry.

### 3.7 Layer 6 — the question this repo had never posed

`W213`/`W126`/`W159` have a *second* unbounded-below result, carried by the scale amplitude
`p` (4-volume `N ~ e^{4p}`) — i.e. by **exactly** the conformal mode `W168` identified as
DeWitt-negative and `W153` showed the tachyon lives in. Unlike SRC-3's runaway, **that one is
genuinely a motion in the cone**, so the cone question is on-type for it. The prior-art sweep
found it was never asked.

> **Answered.** The conformal ray `e^{2p} g0` has `det = e^{8p} det g0`, which is never zero
> at finite `p`. Certified in the cone out to `2^{200}` and down to `2^{-200}`. The
> degenerate boundary is reached only at `p = -infinity`.
> **The Lorentzian metric cone does not truncate the `W213`/`W159` conformal runaway in
> either direction.** The only bounding mechanism on record remains the `W159` DBI velocity
> wall, which — as `W159` itself says — bounds velocity and **not excursion**.

## 4. Inline hostile review

### 4.1 Strongest overclaim available, and the guard against it

**The overclaim:** *"MC-1 settles the cone question for GU."*

**Refused.** What is settled is a narrow, exact, finite-dimensional statement about the fibre
of `Met(X4)` and about the homogeneity of SRC-3's `K`. What is **not** settled, and is not
touched: whether the DeWitt-negative directions are gauge or reducible; whether GHP contour
rotation applies; whether SRC-3's potential is the right object at all; anything about the
reduced 4d action; anything about `Y14`'s global structure beyond a single fibre.

A second, subtler overclaim is worth naming because it is the one a reader will make for me:
*"the DeWitt-negative direction is the conformal factor, and W78 proved the conformal mode is
physical, therefore the runaway is physical."* **That inference is not licensed here.**
W78's object is the `R^2` scalaron of the *reduced fourth-order 4d action*; my object is a
*direction in the `Y14` fibre metric*. They are the same geometric direction wearing two
different dynamical hats, and this repository's own `GEOMETER-VS-PHYSICS-OBJECTS.md` fork
rule exists to stop exactly that substitution. W78 is cited as the reason the *gauge escape*
is not free, not as a physicality proof for SRC-3's direction.

### 4.2 Strongest contrary construction

**GHP contour rotation.** If the DeWitt-negative directions are rotated in the complex plane —
the standard 1978 treatment, and the `twentyfive-lens-council`'s recorded *"single most
promising unexplored lead"* (Lens 10: Curt's trace-line sign may be a **contour** choice, not
a signature choice) — then "unbounded below on the real cone" is a statement about a contour
that was never the right one, and TC-CONE's *conclusion* could be reached by an argument that
has nothing to do with cones.

**My result is silent on this, by construction.** Everything here lives on the real cone;
contour rotation leaves it. This is the honest weakest seam and it is also the decisive next
gate.

**A second contrary construction, and it comes from the file I lean on hardest.** `W168`'s own
*verdict* — as opposed to its computation, which I reproduce — is that the conformal mode's
Krein sign is **OPPOSITE** to the graviton block's, from which it concludes
`c_R_phys = +4/9 > 0` (healthy) and the tachyon **SPURIOUS**, branch-conditional on
SC1/SC2. If that reading holds, the negativity I have just shown is unremovable by cone
geometry may be *unphysical in the first place*, because the relevant inner product is the
Krein one and not the naive one. I do not adjudicate it — `W168` itself scopes the verdict to
"the signature IN THE `|II|^2` SHADOW" and carries branch A/B unresolved — but a reader who
takes MC-1 as strengthening the pessimistic case is over-reading it. **MC-1 removes one
objection to SRC-3; it does not add support to SRC-3.**

One counter-pressure on GHP, recorded but **not** treated as closing it: `W78` §1.3 and `W122` argue
GHP is **category-inapplicable** to GU's pathology, because GHP rotates a *second-order
Euclidean kinetic sign of a non-propagating mode* whereas GU's is a *fourth-order Lorentzian
tachyonic pole*. **That argument does not obviously transfer to SRC-3**, whose object is
neither a kinetic sign nor a mass pole but a **quartic potential coefficient**. So the
scope question has to be re-asked for SRC-3 specifically. It is open.

### 4.3 Weakest seam in my own work

**The identification of SRC-3's abstract internal `eta = diag(+1^6, -1^4)` with the DeWitt
Gram.** SRC-3 works in an orthonormal internal frame; my computation works in the coordinate
basis of `Sym^2`, where `G` is not `eta`. The bridge is Sylvester's law, and I certify a
**rational** `G`-orthogonal frame with exactly 6 positive and 4 negative diagonal entries —
the real orthonormal frame is then the further rescaling by `1/sqrt(|d|)`, which is a
*positive* rescaling of each basis vector and therefore cannot change any sign in `K`. The
seam is thin but it is a seam: I certify the congruence rather than exhibit the orthonormal
frame over `Q`, because the normalisation is irrational (`|G(E_ij, E_ij)| = 2`).

A second, smaller seam: R4's type audit reads SRC-3's `v` as living in the connection fibre.
That reading is forced by SRC-3's own construction (`v_mu = X` at `mu = 0`, `v_nu = Y` at
`nu = 1`, with `X, Y` in `so(6,4)`), but it is a *reading of another probe's intent*, not a
theorem. If SRC-3's `v` were ever re-typed as a tangent to `Met(X4)`, R4 would need
re-deriving — R1, R2 and R3 would be unaffected.

### 4.4 Classification, in target-native vocabulary

- **TC-CONE**: `REFUTED`. Type: **misaimed critique with a true premise**. The premise
  (`Met_Lor` is not a vector space) is banked at hostile-review grade; the inference to
  SRC-3's cause (2) does not hold.
- **SRC-3 cause (2)**: `SURVIVES` this route, `UNMOVED` in status. Still exploration-tier,
  still conditional on everything it was conditional on before.
- **Route status**: `ROUTE CLOSED, NEGATIVE`. Not candidate-killed — the *candidate* (SRC-3's
  unboundedness) is untouched; the *route* (cone geometry as a bounding mechanism) is closed.
- **Homonym warning, filed**: this repository now has **three** distinct objects called a
  "cone" — the `(9,5)` characteristic/symbol cone of `wave-swing3-the-outside`, the open cone
  of invariant bilinear forms in `W206`, and the cone of Lorentzian metrics treated here.
  `eric-curt-wave3c` already tags the first as a `HOMONYM`. The third is newly in play and
  should be typed `Met_Lor`-cone wherever it appears.

## 5. Claim ceiling

**Ceiling: EXACT FINITE-DIMENSIONAL LINEAR ALGEBRA AND ALGEBRAIC GEOMETRY OF ONE FIBRE.**

This file establishes, unconditionally and independent of whether GU is correct:

1. `GL(4,R)` acts transitively on the signature-`(3,1)` locus `C` in `Sym^2(R^{4*})`; `C` is
   open, 10-dimensional, dilation-invariant, and **not** convex.
2. The trace-reversed Frobenius (DeWitt) metric is exactly `GL(4,R)`-equivariant, hence has
   inertia `(6,4)` at **every** point of `C`.
3. The four negative directions at `diag(1,1,1,-1)` are the dilation direction and
   `E_03, E_13, E_23`; a general negative direction `a g0 + b.E` gives a ray that stays in `C`
   for all `t >= 0` **iff** `a >= 0`.
4. Under `g -> mu g`, SRC-3's `Q` and `K` both scale by `mu^{-2} > 0`.
5. With weight `|det g|^w`, the inward conformal pseudo-length is `1/w`; it diverges at
   `w = 0`; the outward one diverges for all `w >= 0`.

**It does NOT establish, and no sentence here should be read as establishing:**

- that SRC-3's potential is bounded or unbounded *as physics* — SRC-3's own tier is unchanged;
- any gauge, constraint, reduction, or contour determination for the DeWitt-negative
  directions;
- that the conformal mode is physical (that is `W78`'s claim about a *different* object);
- anything about `Y14` globally, about sections, about the reduced 4d action, or about
  `SIGNATURE-AMBIENT`;
- any movement of `canon`, `RESEARCH-STATUS.md`, `CURRENT-STATE.yaml`, any ledger, or any
  claim status. `canon_verdict_change: none`.

## 6. Next gate, and what would kill this result

**Decisive next gate.** Does GHP-style contour rotation apply to a **quartic potential
coefficient**, as opposed to a kinetic sign (`W78`'s GHP scope argument) or a mass pole
(`W122`)? This is the only live route by which TC-CONE's *conclusion* survives its refuted
*argument*, and it is the repository's own recorded top unexplored lead. It is cheap to at
least type: the object is a `t^4` coefficient, not a `t^2` one, and the GHP rotation is a
`Z/4`-type rotation of the field — so the question of whether it can fix a quartic sign is
almost certainly answerable in closed form.

**What would kill this result:**

1. **A re-typing of SRC-3's `v`.** If `v` is a tangent vector to `Met(X4)` rather than a
   connection component, R4 falls. R1–R3 survive, so the headline survives, but weakened from
   four routes to three.
2. **A different fibre metric.** Everything here is computed for the trace-reversed Frobenius
   metric with `lambda = 1/2` (`tests/signature_fork_equivariance_defect.py:126`,
   `LAM = 0.5  # trace-reversal coefficient, as filed`). At `lambda < 1/4` the fibre is
   `(7,3)`, cause (2) does not exist at all, and this entire file is about a direction that
   is not negative. **This is the single cheapest thing that could invalidate the framing** —
   and it invalidates SRC-3's cause (2) along with it, so it is a shared dependency, not an
   asymmetric risk.

   **A live inconsistency found while checking this, and verified by direct read.**
   `papers/drafts/vz-evasion-preprint-draft-2026-06-23.md:82` writes the operation as
   *"trace-reversal (`h -> h - (1/4) tr(h) g` for 4x4 symmetric matrices)"* and then asserts
   the result is `(6,4)`. In `n = 4` the map `h -> h - (1/4) tr(h) g` is the **traceless
   projector**, not the trace reversal `h -> h - (1/2) tr(h) g`; and `lambda = 1/4` is
   exactly `lambda_c`, where this probe computes the trace direction to be **null** — inertia
   `(6,3)` with one zero, not `(6,4)`. So that sentence names the wrong operation and states
   a signature the named operation does not produce. It is a draft, not canon, and canon
   (`shiab-existence-cl95.md`) is unaffected. Flagged, not repaired here (drafts are outside
   this file's writable scope).
3. **A GU-native Weyl/conformal gauge symmetry on the `Y14` fibre.** If one exists, the
   dilation direction is gauge, R2's negative direction is unphysical, and the whole question
   dissolves. `W78`'s H49 fork-closure argues against this for the reduced action; whether it
   transfers to the fibre is not established.
4. **An error in the inertia machinery.** Guarded two ways (two independent exact methods with
   asserted agreement) and mutation-tested four ways.

## 7. What this does and does not do

**Does:** close, negatively and exactly, the route "cone geometry bounds SRC-3's runaway";
name the DeWitt-negative directions explicitly; supply the exact cone-exit criterion for the
whole negative subspace; supply the first machine-checked certificate of the banked `Met_Lor`
non-convexity; separate the standard conformal-factor-problem material from the GU-native
material with a per-item attribution table; flag the `lambda = 1/4` vs `lambda = 1/2`
inconsistency and the unrepaired `canon/no-go-class-relative-map.md` §2.3 "convex cone" line;
answer the never-posed `W213`/`W159` cone question.

**Does NOT:** move any verdict, canon file, ledger, or claim status; determine gauge status;
perform or evaluate a contour rotation; make any statement about GU's physical viability.
SRC-3 remains exactly where it was, with one fewer live objection against it.
