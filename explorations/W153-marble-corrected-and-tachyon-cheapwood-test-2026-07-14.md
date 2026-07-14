---
artifact_type: exploration
status: exploration (W153; coherence-first then kill; five personas inline, one worker, no sub-agents; deterministic test with positive controls)
created: 2026-07-14
wave: W153
label: W153
supersedes_framing_of: explorations/W152-marble-and-wood-source-fix-2026-07-14.md
title: "W153 -- marble corrected and the coherence-first tachyon-as-cheap-wood test. CORRECTS the W152 three-term scorecard under Joe's GU-native reading: in G_munu + Lambda g_munu = (8 pi G / c^4) T_munu the CHEAP WOOD is the METRIC g_munu (imposed by hand; the thing GU exists to DERIVE, Y14 = the bundle of all metrics) and Lambda (the unexplained blunder constant); T_munu is KEPT (in the substrate inversion the RECORDS ARE THE MATTER, held in Y14) and G is KEPT (the coupling). Then BUILDS and TESTS Joe's coherence hypothesis that the R^2 tachyon (route alpha, |II|^2 on the imposed metric) DISSOLVES when the metric is record-derived. Verdict: the hypothesis FAILS, and is understood from within the complete picture -- the tachyon is GENUINE and SURVIVES a record-derived metric, because the R^2 coefficient a2 = -1/9 is an intrinsic property of the |II|^2 FUNCTIONAL, invariant under how the metric is sourced, and it LIVES IN the conformal factor = the BLMS record-count leg; record-derivation LOCATES the tachyon, it does not remove it. Pure Einstein is recovered only by re-sourcing the DYNAMICS (|II|^2 -> Jacobson record-thermodynamics), an equilibrium/leading-order truncation, not by re-sourcing the metric."
hypothesis: "Coherence-first: BUILD the larger story that fits before killing. Story 1 (JOB 1): under GU's ontology inversion the metric g_munu and Lambda are the cheap wood (derived shadows), T_munu and G are kept (records = matter). Story 2 (JOB 2): the route-alpha R^2 tachyon is an ARTIFACT of evaluating GU's |II|^2 on the imposed (cheap-wood) metric, and dissolves to pure Einstein once the metric is RECORD-DERIVED (Malament conformal + BLMS record-count factor)."
grade: "exploration / conditional register throughout. Every 'GU does X' reads 'under the declared conditional structure, X'. COMPUTED (deterministic, tests/W153_marble_corrected_and_tachyon_cheapwood_test.py, 9/9 exit 0): the W126 MSS interpolant W(u) = -64 u^2 - 8 u + 2 -> F(R) = 2 + R/3 - R^2/9 (a0=2, a1=+1/3, a2=-1/9, a2/a1=-1/3) as a POSITIVE CONTROL; the SCALE-MODE INVARIANCE of a1, a2 under the conformal factor p (the JOB-2 load-bearing check: re-sourcing the metric scale = the record-count leg does not move the tachyon); Malament order->[g]-only under monotone null reparam and BLMS count->volume on a toy 1+1 causal diamond (the record-derived-metric positive control). CITED (not re-derived): W126/W130 (the induced |II|^2 action, a1=1/3, a2=-1/9, c_W=+2, c_R=-4/9, the 3:2:1 split), W122/W123 (the native tachyon, f_0^2<0), W128 (AS/Reuter branch permits the healthy scalaron), W130 (native tree point off the AF branch), W145-W147 (everpresent-Lambda, sqrt(N_4)=S_dS relabel, C-operator sign pin), W151 (the two-route alpha/beta result), W152 (the prior scorecard, framing corrected here append-only), papers/drafts/Transcript into the impossible.md (DATA). No canon / RESEARCH-STATUS / claim-status / verdict / posture change; H41 unbuilt; H59 OPEN; E2 AF-vs-AS fork CARRIED."
construction: "program-native where the objects are GU's (Y14 = Met(X4), the induced |II|^2 action, the gimmel (9,5) cone, the C-operator); standard-field where the machinery binds any construction (Malament 1977, BLMS 1987, Jacobson 1995, the contracted Bianchi identity). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md. The Malament/BLMS/Jacobson chain is PORTED and labelled; the everpresent-Lambda mechanism is PORTED (Sorkin/ADGS)."
depends_on:
  - papers/drafts/Transcript into the impossible.md
  - explorations/W152-marble-and-wood-source-fix-2026-07-14.md
  - explorations/W151-gr-and-c-emergence-from-records-2026-07-14.md
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W128-reuter-branch-scalaron-native-2026-07-14.md
  - explorations/W122-spin0-gauge-vs-physical-auxfield-2026-07-13.md
  - explorations/W145-substrate-sweep-mathematics-2026-07-14.md
  - explorations/W146-substrate-sweep-theoretical-physics-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W153_marble_corrected_and_tachyon_cheapwood_test.py
external_refs:
  - "Malament, J. Math. Phys. 18 (1977) 1399 -- causal order determines the conformal metric, topology, differentiable structure (not the conformal factor)"
  - "Bombelli, Lee, Meyer, Sorkin, PRL 59 (1987) 521 -- causal sets; order + number = geometry"
  - "Jacobson, PRL 75 (1995) 1260 -- Einstein equations as an equation of state, delta Q = T delta S"
  - "Eling, Guedens, Jacobson, PRL 96 (2006) 121301 -- f(R) needs a non-equilibrium entropy-production term"
  - "Stelle, PRD 16 (1977) 953 -- fourth-order gravity spectrum"
---

# W153 -- Marble corrected, and the coherence-first tachyon-as-cheap-wood test

## 0. Why this note exists (append-only correction of W152's framing)

W152 graded Einstein's three terms exactly as Weinstein's talk does at the level of the field-equation
TERMS: the Einstein tensor `G_munu` is the fine marble (kept), and `Lambda g_munu` plus `T_munu` are
the cheap wood (replace). That reading is faithful to the transcript at the term level
(`papers/drafts/Transcript into the impossible.md`, 00:41-ish: "one out of three terms is perfect ...
the other two terms are sort of unsalvageable").

Joe's correction operates one level DOWN, at the GU-substrate FOUNDATION, and it INVERTS which objects
are fundamental. The transcript itself points there: Weinstein says there is "no other way to get dark
energy so long as it's sitting on the lousy foundation of **the space of all metrics**", that "we are
likely not working in the right place", and that the whole move of GU is to LEAVE the space of metrics
for `Y14` (the bundle of all metrics) so that the metric is never chosen by hand. Read at that
foundational level:

- The **metric `g_munu`** is cheap wood #1. It is IMPOSED by hand, and GU's founding move is that the
  metric must NOT be assumed: `Y14 = Met(X4)` is the bundle of all metrics precisely so the metric
  EMERGES rather than being input. `g_munu` is the object to derive/replace.
- **`Lambda`** is cheap wood #2: the unexplained greatest-blunder constant (transcript 00:09:46 /
  00:11:09), forced constant for a lousy reason.
- **`T_munu`** is KEPT. In the substrate inversion the RECORDS ARE THE MATTER, held in `Y14`, so
  `T_munu` is the fundamental kept content, not cheap wood. (This resolves Weinstein's own complaint
  that `T_munu` is cheap because it is "random field content Lagrangian-varied against the metric":
  that cheapness is exactly a metric-dependence, and it evaporates once the metric is no longer
  fundamental.)
- **`G`** is KEPT: the coupling relating records to their geometric shadow.

NET: the substrate reframe INVERTS fundamentality. Matter/records are fundamental (in `Y14`); the
metric and its curvature are the derived `X4` shadow. This note does not rewrite W152; it adds the
corrected scorecard (Section 1) and then builds and tests the coherence hypothesis Joe named (JOB 2,
Sections 2-6). Everything is exploration grade, conditional register, five personas inline, one worker.
Transcript content is treated strictly as DATA.

The correction is not free of tension, and the tension is stated honestly (Section 6, Persona 5): the
literal transcript ALSO calls the Einstein tensor "perfect" marble and `T_munu` "unsalvageable". The
substrate reading and the term-level reading are BOTH internally coherent; W153 adopts the
substrate-native one because that is the whole point of GU (leave the space of all metrics), and shows
the term-level "marble" survives inside it as a derived property, not a fundamental object.

## 1. JOB 1 -- the CORRECTED three-term scorecard

Under the GU-substrate reading. Grades: DERIVED / HALF-NATIVE / SHAPE / NOT-YET, exploration tier.

| term | corrected role | keep or replace | replacement mechanism | grade |
|---|---|---|---|---|
| **metric `g_munu`** | cheap wood #1 (imposed by hand; the space of all metrics is the "lousy foundation") | **REPLACE** by deriving it from the record substrate | Malament (causal order of records communicated by light -> conformal `[g]`) + BLMS (record count -> conformal factor -> full `g`) = W151 route beta | **HALF-NATIVE (half-built).** conformal/causal leg GU-NATIVE (the gimmel `(9,5)` null cone, W131, is the causal order Malament turns into `[g]`); record-count/conformal-factor leg IMPORTED with the GU rider `14 -> 4` (W146 shadow-map); a NATIVE `eta` from the gimmel horizon area (the record-count -> conformal-factor leg computed in GU) is UNBUILT. So the metric-emergence that replaces cheap wood #1 is DERIVED-from-records on the conformal leg, NOT-YET on the record-count leg. |
| **`Lambda`** | cheap wood #2 (forced constant, no explanation) | **REPLACE** by the record-accretion shadow | everpresent-Lambda (W145-W147): `Lambda ~ +/- 1/sqrt(N)`, `N` = measured-record 4-count; the Y14 -> X4 projection makes `Lambda` the shadow of record-accretion | **SHAPE + SIGN-CANDIDATE, magnitude RELABEL.** rise-and-fall shape achieved; MAGNITUDE is a de Sitter relabel (`sqrt(N_4) = S_dS`, W138 G5 bites); the SIGN is GU-pinned positive by C-operator positivity (a GU-specific falsifiable hook a bare sprinkle lacks) but that prediction is UNBUILT; the normalization `phi = 1/(3 Omega_L)^2` is a fit, its derivation from the `(9,5)` DeWitt-fiber measure UNBUILT. |
| **`T_munu`** | KEPT -- fundamental record/matter content | **KEEP** (NOT the thing to replace) | "the records ARE the matter, held in Y14" (W148 substrate core); the source action maps the kept Y14 record content to its stress-energy shadow | **KEPT; identification CONSISTENT, matter-sector map OPEN.** This CORRECTS W152's "T_munu NOT-YET / replace-intended / essentially untouched" -- under the inversion that is a category error: `T_munu` being the fundamental record content is a FEATURE, not a defect. The identification `T_munu` = X4 shadow of the Y14 record content is consistent at the ontology level (spinors pulled back from `Met(X4)` give the standard-model fermion content natively -- transcript 00:107, 00:161). The SPECIFIC matter-sector map (RS/fermion Yukawa hierarchy) is the same open H41/source-action object: W136's dimensional no-go shows the issuance datum cannot feed the dimensionless Yukawa data (only the Majorana channel is dimensionally reachable, OOM tier). Correctly framed now as "derive the matter shadow FROM the kept record content", not "replace cheap-wood `T_munu`". |
| **`G`** | KEPT -- coupling records to geometric shadow | **KEEP** | Newton's constant is the record-to-shadow coupling; in route beta it is DEFINED by the horizon entropy density `eta` | **KEPT, unproblematic** (its value is a normalization, not a substrate prediction, exactly as `c = 1` is convention in W151). |

**The marble, relocated (do not skip).** W152 kept the Einstein tensor `G_munu` as independent marble.
Under the inversion `G_munu` is the curvature of the RECORD-DERIVED metric -- not a fundamental input.
Its divergence-freedom `nabla_mu G^{mu nu} = 0` (the contracted Bianchi identity) is a geometric
identity for ANY metric, so the marble PROPERTY (genuine divergence-freedom) transfers intact to the
record-derived metric, and in route beta (Jacobson) it is genuinely DERIVED as the record-thermodynamic
equation of state. So the marble is kept as a property and now derived as an object -- it sits ON the
replaced cheap-wood foundation rather than being fundamental beside it. This is the coherent reconciliation
of "the Einstein tensor is perfect" (transcript, term level) with "the metric is the lousy foundation"
(transcript, foundation level).

## 2. JOB 2 -- the coherence-first construction, stated at full strength

W151 found two routes to emergent Einstein gravity:

- **route alpha** -- GU's induced `|II|^2` action computed ON a metric section of `Y14 = Met(X4)`,
  reducing on the scalar slice to `F(R) = 2 + R/3 - R^2/9`: Einstein (`a1 = +1/3`) PLUS a tachyonic
  `R^2` sector (`a2 = -1/9`), the native scalaron (W126/W130, exact, all orders in the conformal
  factor).
- **route beta** -- Malament conformal + BLMS record-count factor + Jacobson equation-of-state on the
  measurement-gated horizon: PURE EINSTEIN, no `R^2`, no tachyon.

Joe's coherence hypothesis: route alpha uses the CHEAP-WOOD imposed metric, so the `R^2` tachyon may be
an ARTIFACT of treating the imposed metric as fundamental, and it should DISSOLVE when the metric is
record-derived. We build this hypothesis and test it at full strength. Five personas inline.

## 3. Persona 1 -- GR/geometry theorist: is the Einstein tensor genuine once the metric is record-derived?

Yes, and this is the load-bearing coherence WIN of JOB 1 rather than a debit. Malament gives the
conformal class `[g]`; BLMS gives the conformal factor from the record count; together they yield a
FULL, generic Lorentzian metric `g`. The Einstein tensor `G_munu` of that record-derived metric is a
genuine tensor with `nabla_mu G^{mu nu} = 0` automatically (PC-level fact, geometric identity). So the
"marble" is intact on the record-derived metric.

But note precisely what record-derivation produces: a GENERIC metric, not a metric confined to some
special submanifold of `Met(X4)` on which the second fundamental form of the section would vanish.
Malament fixes 9 of the 10 local metric components (the conformal class), BLMS supplies the 10th (the
scale). There is no constraint here that would zero `|II|`. So whatever `|II|^2` does to an imposed
generic metric, it does identically to a record-derived generic metric. This is the first localisation:
the metric's ORIGIN (imposed vs record-derived) does not restrict the metric to an `|II|`-flat locus.

## 4. Persona 2 -- GU-structure specialist: is `|II|^2` intrinsically a functional of the imposed metric?

**Where the `R^2` sector comes from, exactly (W126/W130).** `|II|^2` is the squared norm of the second
fundamental form of the GRAPH of the metric-section in `Y14 = Met(X4)`. Pointwise it depends only on the
2-jet `(p ; v ; s)` of the section. On the potential slice (`v = dphi = 0`, general `s`), W126 proved by
two independent routes and all orders in the conformal factor `p`:

1. **scale collapse:** `|II|^2` depends on `(p, s)` ONLY through the scale-covariant variable
   `sigma = e^{-2p} s`. Every power of the conformal factor cancels.
2. **degree termination:** `W(sigma)` is EXACTLY a degree-2 polynomial; `c_3 = c_4 = ... = 0` identically.
3. **slice reduction:** with the pinned curvature map `R = -24 u` (`u` the slice curvature variable),
   `F(R) = 2 + R/3 - R^2/9`. The `R^2` sector is the QUADRATIC-in-`sigma` (bending / Willmore) piece of
   the second-fundamental-form norm. `a2 = -1/9`.

So the `R^2` originates in the quadratic-in-second-fundamental-form (bending-energy) term of `|II|^2`,
and its coefficient is a FIXED PROPERTY of the functional's form -- exact, all orders in `p`. Test T1
makes this concrete: at every conformal scale `p in {-2,-1,0,1,2}` the re-expressed `F(R)` has
`a1 = +1/3, a2 = -1/9` identically. The conformal factor `p` is exactly the mode the BLMS record-count /
volume leg sets. So:

> **The induced `R^2` coefficient is INVARIANT under the record-count / scale mode.** Re-sourcing the
> metric's scale (the BLMS leg that makes the metric "record-derived" rather than "imposed") does not
> move `a2` at all. Worse for the dissolution hypothesis and better for coherence: the tachyonic
> scalaron IS the conformal / scale mode, i.e. the BLMS record-count mode. Record-derivation LOCATES the
> tachyon inside the record-count leg; it does not remove it.

**Engaging W151's "GU's geometry does not permit the truncation to pure Einstein", at full strength.**
This claim is CORRECT and it is about the intrinsic form of `|II|^2`, not an artifact of the imposed
metric. W126 proves `a2 = -1/9` EXACTLY, all orders in `p`, two routes, family-wide in the wave-35
`alpha|II|^2 + beta|H|^2` shape freedom. The claim would be an "imposed-metric artifact" only if `|II|^2`
evaluated on a record-derived metric gave a different `a2`; T1 shows it gives the SAME `a2`. So the
assertion is a genuine obstruction of the FUNCTIONAL, robust to metric re-sourcing. It is NOT removed by
replacing cheap wood #1.

## 5. Persona 3 -- emergent-gravity theorist: why does route beta give pure Einstein, then?

Because route beta changes the DYNAMICS, not the metric. Jacobson's derivation uses area-entropy
`S = eta A` and the Clausius relation on a local horizon; the Raychaudhuri area change is LINEAR in
`R_ab`, so the equation of state yields `G_ab + Lambda g_ab` with NO `R^2` (W151 test J: `a2_beta = 0`).
Getting `f(R)` out of the equation of state requires a curvature-dependent Wald entropy and an internal
entropy-PRODUCTION term -- it becomes NON-equilibrium (Eling-Guedens-Jacobson 2006). So route beta is an
EQUILIBRIUM / leading-order (area-entropy) statement, structurally blind to higher-derivative structure.

This is the order-of-approximation gap W151 named, and it is the actual reason the two routes differ:

- route alpha = the EXACT induced functional `|II|^2` (carries `R^2`);
- route beta = its EQUILIBRIUM / leading-order thermodynamic face (pure Einstein).

The metric ORIGIN (imposed vs record-derived) is ORTHOGONAL to the DYNAMICS choice (`|II|^2`
extremisation vs Jacobson equilibrium). Both routes can use either metric. Joe's hypothesis conflated
"re-source the metric" with "re-source the law". Re-sourcing the metric leaves `a2 = -1/9` (T1);
re-sourcing the LAW (from `|II|^2` to record-thermodynamics) is what produces pure Einstein -- and that
is a truncation to leading order, not a consequence of the metric being record-derived.

**The one genuinely open sub-leg (NOT-YET).** Whether route beta is LITERALLY the leading-order face of
route alpha -- i.e. whether `|II|^2`-extremisation reduces to the Jacobson area-entropy law at
equilibrium -- is CONJECTURED (W151's "order-of-approximation departure") but NOT PROVED. If the two are
the SAME theory at two orders, the tachyon is real subleading structure invisible at equilibrium. If they
are DIFFERENT theories, then a GU whose true law is record-thermodynamic (metric = shadow, its dynamics =
record equilibrium) would be genuinely tachyon-free, and `|II|^2` would simply be the wrong fundamental
action. GU as currently stated asserts `|II|^2` (the observerse action); on GU-as-stated the tachyon is
real. The dissolution would require REPLACING GU's action, not just its metric.

## 6. Persona 4 -- tachyon specialist, and Persona 5 -- adversarial skeptic

**Persona 4 (what survives a record-derived metric).** The tachyon (`m_0^2 = gamma/(6 f_0^2) < 0` on the
AF trajectory, `f_0^2 < 0`, W122; hardened by W126 no-rescue; native operator `f_0^2 = -3/8`, `f_2^2 =
-1/4`, W130) is fed by `a2 = -1/9`, which T1 shows is record-count-invariant. So it survives a
record-derived metric. The ONE live escape that is NOT about metric origin is the E2 AF-vs-AS fork: W130
found GU's native tree point lies OFF the AF branch, and W128 showed the AS/Reuter branch PERMITS a
healthy (non-tachyonic) scalaron as a free relevant IR boundary condition. That escape is real, standing,
and orthogonal to Joe's metric-origin hypothesis -- record-derivation neither opens nor closes it.

**Persona 5 (steelman the two coherence-breakers, at full strength).**

- *"THE TACHYON IS REAL REGARDLESS OF METRIC ORIGIN."* This is what the computation supports. `a2 = -1/9`
  is exact, all orders in `p`, two routes (W126), record-count-invariant (T1); W123 pinned the sign
  native-robust; W126 closed the beyond-4th-order and loop-`R^3` rescues; W130 confirmed at operator
  level. The tachyon does not care how the metric was sourced. VERDICT UPHELD: on GU-as-stated (`|II|^2`
  the action), GENUINE, survives the record-derived metric.

- *"THE METRIC IS NOT CHEAP WOOD BECAUSE `G_munu` IS BUILT FROM IT."* The steelman: you cannot demote the
  metric to cheap wood while keeping the Einstein tensor as marble, since `G` is a functional of `g`.
  Answer (Persona 1 / Section 1 marble-relocation): under the inversion `G_munu` is NOT independently
  marble; it is the derived curvature of the record-derived metric, and its divergence-freedom (the
  marble property) is a geometric identity that transfers to any metric and is genuinely DERIVED in route
  beta. So the objection dissolves: the metric is cheap wood #1 (the foundation), and the Einstein
  tensor's good property rides on top of the replaced foundation. The transcript supports both halves
  ("the term is perfect" AND "the space of all metrics is the lousy foundation"); the substrate reading
  reconciles them.

- *Honest residual the skeptic keeps.* The claim "route beta is the leading-order face of route alpha" is
  unproved (Section 5 NOT-YET). Until it is proved, one cannot assert the tachyon is "merely subleading";
  one can only assert it is real IF `|II|^2` is the law. And the substrate reading of `T_munu` (Section 1)
  is an ontology identification, not a computed matter-sector map (H41 open, Yukawa no-go standing).

## 7. Verdicts (the brief's return fields)

**Corrected three-term scorecard:** metric `g_munu` = cheap wood #1, REPLACE via records
(Malament+BLMS = route beta), grade HALF-NATIVE (conformal leg native, record-count leg NOT-YET);
`Lambda` = cheap wood #2, REPLACE via everpresent record-accretion shadow, grade SHAPE + sign-candidate,
magnitude a dS relabel; `T_munu` = KEPT (records are the matter), identification CONSISTENT, matter-sector
map OPEN (corrects W152's replace-intended framing); `G` = KEPT (coupling). Marble (Einstein-tensor
divergence-freedom) relocated: kept as a property, derived as an object, riding on the replaced metric.

**Tachyon-as-cheap-wood verdict:** **GENUINE -- SURVIVES-RECORD-DERIVED-METRIC.** Evidence: (1) the
induced `R^2` coefficient `a2 = -1/9` is an intrinsic property of the `|II|^2` FUNCTIONAL, exact and all
orders in the conformal factor (W126), and INVARIANT under the record-count / scale mode (test T1,
`a1 = +1/3, a2 = -1/9` at every `p`); (2) a record-derived metric (Malament `[g]` + BLMS factor) is a
generic metric, not confined to an `|II|`-flat locus (Persona 1); (3) the tachyonic scalaron LIVES IN the
conformal factor = the BLMS record-count leg, so record-derivation LOCATES the tachyon rather than
removing it. With one NOT-YET rider: whether route beta (pure Einstein) is literally the leading-order
face of route alpha (`|II|^2`) is conjectured but unproved -- so "the tachyon is merely subleading" is
NOT-YET-DECIDABLE, while "the tachyon is real if `|II|^2` is GU's law" is upheld.

**R^2 localisation and its survival:** originates in the quadratic-in-second-fundamental-form (bending /
Willmore) term of `|II|^2`, carried by the conformal / scale mode; survives a record-derived metric
because the coefficient is scale-mode-invariant (T1). It is removed ONLY by replacing the DYNAMICS
(`|II|^2` -> Jacobson equilibrium), which is an order-of-approximation truncation, not a metric-origin
effect.

**The coherent picture (what the honest test yields).** Joe's dissolution hypothesis, built at full
strength, FAILS -- and is understood from within the complete picture. The tachyon is not a cheap-wood
artifact of the imposed metric; it is a real feature of GU's induced action that record-derivation merely
relocates into the record-count leg. Route beta gives pure Einstein because it is the leading-order
thermodynamic (equilibrium) face, blind to higher-derivative structure -- exactly W151's
order-of-approximation gap. So the two routes are best read as ONE theory at two orders, with the tachyon
as its exact-order content; and the genuine remaining escape (whether the exact tachyon is fatal or fork-
relieved) is the E2 AF-vs-AS branch question (W128/W130), which record-derivation does not touch.

**W151's "geometry does not permit the truncation to pure Einstein":** engaged directly and UPHELD as a
statement about the intrinsic `|II|^2` functional (W126 exact), NOT an artifact of the imposed metric
(T1). It is a genuine obstruction of the FUNCTIONAL. The only way past it is to demote `|II|^2` from GU's
law to a diagnostic, handing the dynamics to record-thermodynamics -- which yields pure Einstein at
equilibrium but abandons the very action GU asserts.

## 8. Tests, exit codes, files

- `tests/W153_marble_corrected_and_tachyon_cheapwood_test.py` -- 9 checks, exit 0. PC1: W126 interpolant
  `W(u) = -64 u^2 - 8 u + 2` -> `F(R) = 2 + R/3 - R^2/9`, `a0=2, a1=+1/3, a2=-1/9, a2/a1=-1/3` (positive
  control, regression pin). T1: scale-mode invariance of `a1, a2` under the conformal factor
  `p in {-2,-1,0,1,2}` (the JOB-2 load-bearing check). PC2: Malament order->`[g]`-only under monotone
  null reparam (`u->u^3, v->(e^v-1)/(e-1)`, exact relation-matrix equality on 40736 relations) + BLMS
  count->volume on a 1+1 causal diamond (4-sigma Poisson).

## 9. Honest limits

- Exploration grade / conditional register throughout. Nothing asserts GU, that the DESI wiggle is real,
  that any decomposition is physical, or that the substrate reading is true.
- The Malament/BLMS/Jacobson chain and the everpresent-Lambda mechanism are PORTED (labelled). The `R^2`
  origin, `a1/a2`, and the AF/AS data are CITED from W126/W130/W122/W128, regression-pinned here on the
  `a1/a2` values, not re-derived from the full `|II|^2` machinery.
- The load-bearing NOT-YET: whether route beta is the exact leading-order face of route alpha is
  conjectured, not proved; the `T_munu` = record-content identification is ontological, with the
  matter-sector (Yukawa) map open (H41, W136 no-go). The everpresent sign pin and `phi` normalization are
  named targets, unbuilt.
- No canon / RESEARCH-STATUS / claim-status / verdict / posture change; no spec FIT row moves; H41
  unbuilt; H59 OPEN; the E2 AF-vs-AS fork CARRIED. Tri-repo gating honored: record/finality/time
  semantics belong to temporal-issuance + time-as-finality; capability MEASURE is TaF's; GU owns the
  emergent-metric math only; no cross-repo identity asserted.

*Filed 2026-07-14 by Team MARBLE-2 (W153). Coherence-first then kill. Five personas inline in one worker
(GR/geometry theorist; GU-structure specialist; emergent-gravity theorist; tachyon specialist;
adversarial skeptic); no sub-agents. Reproducible:
`python -u tests/W153_marble_corrected_and_tachyon_cheapwood_test.py` (9/9, exit 0). Exploration grade;
conditional register; zero em dashes in paper-facing text; no canon movement.*
