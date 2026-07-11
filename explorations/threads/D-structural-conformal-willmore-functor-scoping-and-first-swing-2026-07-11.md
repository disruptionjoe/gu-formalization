# Thread group D — structural/framing: H-class GU vs conformal gravity, the section functor, the method, the object that must exist

2026-07-11. First swing on thread group D (structural/framing). The one computational leg (D1) is landed as a
reproducible test; D2/D3/D4/D5 are drafted as precisely-stated conjectures + framing, honestly graded, NOT
proofs. Nothing here imports a target number; the one number the test returns (`-4`) is what the computation
gives, sign fixed by the curvature convention.

Companion test: `tests/threads/D_hclass_vs_conformal_gravity.py` (exit 0).

---

## D1 — Is H-class GU literally conformal (Weyl) gravity? — the real swing

### The two objects, stated exactly

- **H-class GU.** The section `s: X^4 -> Y^14 = Met(X^4)`, `s(x) = (x, g_ab(x))`, extremizes the mean-curvature
  functional `E[s] = int |H|^2` (the conformal-Willmore member of the OQ2-A functional freedom). Its EL is the
  curved-ambient Willmore equation
  `Delta^perp H + Q^TF(B) + c_W (R^Y . H)^TF = 0`
  (`willmore_curved_ambient_term.py`, `willmore_oq2a_functional_selection.py`). This is an equation for the
  **immersion** (the section), i.e. for the *extrinsic* geometry of `X^4` sitting inside the space of metrics.
- **Conformal (Weyl) gravity** (Mannheim; intake `mannheim-conformal-gravity-source-action-intake-2026-07-06.md`).
  `S = -alpha_g int C_{mnrs} C^{mnrs}` — the unique conformally invariant pure-metric 4D action — with
  fourth-order **Bach** field equations `B_{mn} = nabla^r nabla^s C_{mrns} + (1/2) R^{rs} C_{mrns} = 0`. This is
  an equation for the *intrinsic* conformal geometry of `X^4` (the Weyl tensor of `g`).

A priori these are different geometric objects: one extrinsic (mean curvature of a map), one intrinsic (Weyl
curvature of a metric). The question is whether their **field equations** coincide, contain one another, or
differ.

### The concrete algebraic check (computed, exit 0)

`tests/threads/D_hclass_vs_conformal_gravity.py`. Linearize both about flat space with `h_ab = g_ab - eta_ab`.

- **Principled linearized mean-curvature vector** (section-6.1 normalized, Hessian-only; slice term subtracted at
  all orders per `ii-s-coordinate-formula` sec 6.1): `H^(1)_ab = eta^{mu nu} d_mu d_nu h_ab = box(h)_ab`. So the
  leading H-class Willmore-EL operator is `Delta^perp H^(1) = box H^(1) = box^2 h_ab` — a **fourth-order**
  operator, matching the harmonic-`H` finding of `willmore_geometric_ii_and_ambient_curvature.py`
  (`box(h)=0` for Schwarzschild is the special case).
- **Linearized Bach** about flat space: the `(1/2)R^{rs}C` term is `O(h^2)`, so `B^(1)_{mn} = d^r d^s C^(1)_{mrns}`,
  computed exactly from the linearized Weyl tensor.

Results (exact sympy, all wave profiles `F` at once via `h_ab = eps_ab F(k.x)`):

1. **On the transverse-traceless (spin-2) sector the two operators are proportional by a single rational scalar,
   for every component:** `box^2 h = (-4) * Bach^(1)` on TT. Equivalently `Bach^(1) = -(1/4) box^2 h^TT`. The
   sign/magnitude `-4` is convention-dependent (Riemann/Weyl/Bach sign convention); what is convention-independent
   is that **one nonzero rational scalar relates the two fourth-order operators across the whole spin-2 sector** —
   they are the *same operator* on the graviton, not merely the same order.
2. **Both are genuinely fourth-order** (carry four derivatives of the profile), i.e. neither is the second-order
   Einstein operator.
3. **Off the spin-2 sector they differ.** On a pure-conformal mode `h_ab = phi eta_ab` the linearized Weyl tensor
   vanishes (conformally flat), so `Bach^(1) = 0`; but the naive `box^2 h = box^2 phi * eta_ab != 0`. This locates
   the difference **precisely in the trace/conformal sector**.

### Verdict (rigorous, honest)

**Special-case / contains, not literal identity.** Concretely:

- **On the spin-2 (graviton) sector the H-class GU section-EL IS the conformal-gravity (Bach) operator** — same
  fourth-order kinetic operator up to one rational constant. So H-class GU is a member of the
  **conformal-Willmore / fourth-order-gravity class**, *not* an Einstein-class (second-order) theory. This is the
  strong, computed part of the identification and it is not accidental: `|H|^2`-Willmore is a conformally invariant
  curvature-squared functional (invariant under conformal change of the *ambient* metric, Blaschke/Willmore), and
  `C^2` is *the* conformally invariant curvature-squared functional of the *intrinsic* metric; both linearize to
  `box^2` on the spin-2 field.
- **It is not a literal identity of theories, for two independent reasons that GU adds:**
  1. **Trace/conformal-sector mismatch.** Bach annihilates the conformal mode; naive `|H|^2` does not. Closing this
     requires the *conformal*-Willmore functional (the `|H|^2 -> |H|^2 - (conformal counterterm)` combination that
     is genuinely conformally invariant, i.e. the Willmore energy proper), which supplies the spin-2 projector and
     kills the trace mode. Whether GU's OQ2-A functional is exactly this conformally-invariant combination is the
     open datum — it is the *same* `c_W`/functional choice already isolated in `willmore_oq2a_functional_selection.py`.
  2. **Extrinsic + fiber richness with no Weyl-gravity analog.** GU's functional is the *extrinsic* Willmore energy
     of the section into `Met(X^4)`; its FULL nonlinear EL carries the `O(M^0)` DeWitt algebraic-slice / ambient
     `R^Y` pieces (`ii-s-coordinate-formula` sec 6.1: "constant sections are not totally geodesic"). Pure `Weyl^2`
     has no analog for these — they are genuine GU content (the curvature of the space of metrics). And GU adds the
     **fiber/gauge (Sp(64)/theta) structure** entirely absent from conformal gravity.

So: **H-class GU reduces to / contains conformal (Weyl) gravity's field equation on the spin-2 graviton sector,
and is a strictly richer theory off it (extrinsic ambient curvature + gauge fiber).** This is exactly the class
membership the Mannheim intake flagged ("GU is not conformal gravity; only class membership of the candidate
source action") — now upgraded from a stated guess to a **computed operator match on the spin-2 sector**.

Grade: **concrete algebraic identity** for the spin-2 operator match (reproducible, exit 0); **structural** for
the full-theory containment statement (the trace-sector closure and the ambient/fiber richness are argued, not
all computed). Honest caveats: (a) the match is linearized about flat space; the nonlinear relation (full Bach vs
full curved-ambient Willmore) is not computed here. (b) The `-4` is convention-bound; only its being a single
nonzero rational is load-bearing. (c) Whether GU's OQ2-A functional is the *conformally invariant* Willmore
combination (needed to also kill the trace mode and make the containment exact on all sectors) is unresolved and
is the same open `c_W` datum.

### Inherited stress (bookkeeping, from the intake docs)

If the identification is taken seriously as "GU's gravity sector is conformal-gravity-class", GU *inherits the
conformal-gravity phenomenology disputes* (`VG-SB-conformal-gravity-critical-line.md`): the lensing-sign
definition dispute (contested, not fired), Yoon's Newtonian-limit standoff, and the Horne/Hobson-Lasenby
frame-independent "no flat rotation curves" objection (stands as of that intake). **Caveat that softens the
inheritance:** those objections attack the *linear potential `gamma r`* used to fit galactic rotation curves
without dark matter — a specific vacuum solution + matter-coupling claim of Mannheim's program, not the Bach
operator itself. GU does not (here) claim the `gamma r` rotation-curve mechanism; the operator-level match does
not import that phenomenology. So the honest inheritance is: GU shares conformal gravity's *fourth-order operator*
(and its ghost/unitarity question — the Bender-Mannheim/Turok-Bateman PT/Krein territory of
`canon/ghost-parity-krein-synthesis.md`), but not automatically its rotation-curve claims.

---

## D2 — The functorial statement (drafted conjecture, NOT proved)

The identifications the arc keeps landing (conjugate SMs → one SM; shared `theta` welding gravity∩dark-energy;
`alpha_W ↔ f_0`) look "lucky" only because they are stated leg-by-leg. The functorial reframing makes them a
single naturality statement. As precisely as is honest:

**The section functor.** Let `Bord_4` (or a suitable site of 4-manifolds `X^4` with the structure GU needs) be
the source. Define
`Sec: X^4  |->  ( Y^14 = Met(X^4),  the fiber bundle P over Y^14,  the space of sections Gamma(s) )`,
a functor to *structured section data*. A GU "physics configuration" over `X^4` is a section `s` together with a
connection `A` on `P`; the GU **field content is the value of `Sec` on `X^4`**.

**Physics = natural transformations.** The claim is that each physical law is a **natural transformation between
functors built from `Sec`**, so that it is defined *uniformly in `X^4`* and its cross-leg agreements are
*naturality squares*, not coincidences:

- **Gravity** = the natural transformation `Willmore-EL: Sec => T^*Sec` (the section EL, a section of the
  cotangent of the section space) whose zero locus is the shape equation.
- **Gauge/source** = the natural transformation `D_A * F_A - theta = 0` relating the connection functor to the
  distortion functor `theta = s^*(...)` (DD1: `s*(theta) = II_s`, `ii-s-coordinate-formula` sec 7).
- **The shared `theta`** is then *forced* to be one object because it is the image of a *single* natural
  transformation `theta: Sec => DistortionFunctor` — gravity's source term and dark energy's dynamical field are
  the **same natural transformation evaluated in two EL contexts**, so their agreement is a naturality square, not
  a fit. This is the functorial content of the "theta = gravity ∩ dark energy" over-determination
  (`source-action-constraint-intersection-2026-07-11.md`).
- **Conjugate SMs → one SM** (`sm_embedding_conjugacy.py`) is naturality of the gauge-group functor: the
  forces-route max-compact and the vacuum-route stabilizer are two natural transformations into the same ambient
  `so(10)` functor; conjugacy in `so(10)` is exactly the statement that they are the *same* natural transformation
  up to the inner-automorphism 2-cell.
- **`alpha_W ↔ f_0`** is naturality of the shape-EL and the DE-EL along the shared `theta` transformation: fixing
  `theta` (a single arrow) fixes both its shape-side weight (`alpha_W`) and its DE-side amplitude (`f_0`).

**Would-be theorem (conjecture, not proved).**
> *There is a functor `Sec` from the site of GU spacetimes to structured section data such that every GU field law
> is a natural transformation between functors built from `Sec`, and the cross-leg identifications
> (single-`theta`, single-SM, `alpha_W`-`f_0` link) are the naturality squares of these transformations. In
> particular the shared `theta` and the shared SM are not coincidences but consequences of there being a single
> arrow in each case.*

Grade: **well-posed conjecture / framing**. What is honestly present: the objects (`Sec`, `Met(X^4)`, `theta` as
`s^*`) and the maps exist in the repo; DD1 already casts `theta` as one natural connection-difference object. What
is NOT done: constructing the site precisely, checking functoriality (morphisms of `X^4` → morphisms of section
data) and the naturality squares. This is a *would-be theorem with its statement*, the D-thread deliverable, not
a proof.

---

## D3 — The method, named and separated from GU

The move that generated every recent result is **not** GU-specific and deserves a standalone name:

**"Constrain-by-the-over-determined-intersection" (COI).** Given several independent sub-claims (legs) that each
depend on a shared unknown object `O` (here: the source action / its sectors), do NOT build `O` freely and score
it against one leg (that p-hacks). Instead, **require every leg to hold simultaneously and take the intersection
of their constraints on the shared sectors of `O`.** Where two or more legs touch the *same* sector, the joint
requirement **over-determines** that sector: the surviving `O` is the intersection, and any agreement found there
is *forced* (each leg is independent physics), not fitted.

Formal skeleton (GU-free):
- Objects: an unknown `O` decomposed into sectors `O = (S_1, ..., S_k)`.
- Legs: independent constraints `L_i(O) = 0`, each depending on a known subset of sectors (a **constraint
  matrix** leg×sector).
- Method: solve the *joint* system `{L_i = 0}`; read off which sectors are pinned by ≥2 legs (over-determined,
  the narrowing) vs 1 leg (a residual scalar) vs 0 legs (free).
- Non-p-hacking guarantee: because the `L_i` are independent measurements/derivations, an intersection point is a
  *consistency* result, not a fit; a genuine tension (empty intersection) is a *disproof*, equally informative.

This is the pattern in `source-action-constraint-intersection-2026-07-11.md` (the leg×sector matrix; `theta`
over-determined by gravity∩DE; the gauge sector fourfold over-determined). Named as a method, COI is portable:
it is the epistemics of any reconstruction where the target object is shared across independent constraints. It is
**separable from GU** — GU is one instance where `O` = the source action; the method would apply to any
under-specified theory whose pieces are each pinned by different phenomenology.

Grade: **method-naming / framing** (a clean statement of an epistemic discipline the repo already practices).

---

## D4 — Orient around the located-not-forced discrete 2-bit prediction

Among all GU outputs, most are continuous (coefficients gated on `c_W`, `f_0`, `alpha_W`). The **one discrete
fact** the structure *locates* is the **RS 2-bit declaration** (the generation-count carrier: an
invariance-selection bit × a phase bit), flagged as "located, not forced" in
`source-action-constraint-intersection-2026-07-11.md` (sector D) and the generation-sector notes.

Why this is the right thing to orient around: a discrete prediction is **falsifiable in a way a fitted continuous
coefficient is not**. A 2-bit output has exactly four possible values; the theory *locates* the datum (says "the
answer lives in this 2-bit space, coupled to the over-determined gauge sector") without yet *forcing* which of the
four. The honest deliverable is therefore:
> **The GU structure predicts that the generation/RS sector is governed by a discrete 2-bit invariant, coupled to
> the (over-determined) gauge sector — a located, finite, falsifiable prediction — with the specific value still
> gated on the RS field-space declaration.**

Orientation consequence: the highest-value next computation is *not* another continuous coefficient — it is
whatever **forces the 2-bit** (or shows it cannot be forced, i.e. is a genuine free choice of the theory). That is
the single place a discrete, checkable number could emerge. Grade: **framing** (identifies the one discrete
falsifiable target; no new computation).

---

## D5 — "Here is the exact object that must exist + everything it implies" (Weyl precedent)

**Framing of the deliverable.** The Weyl precedent: Weyl did not measure the electroweak scale; he wrote down the
*object that must exist* if local phase symmetry is a principle (a connection = the gauge potential) and derived
*everything it implies* (the field strength, the coupling structure) — the physics was in the forced object, not
in a fitted number. The GU deliverable, honestly, should be stated the same way:

> **The exact object that must exist:** a single source action `S_GU` on the field space over `Y^14` whose gravity
> sector is a conformal-Willmore / fourth-order (Bach-class) section-EL (D1, computed on spin-2), whose `theta` is
> one field shared by gravity and dark energy (over-determined, D2/COI), whose gauge sector is the `so(10)`-ambient
> group with max-compact = SM and rank-one vacuum = `G_SM` (conjugacy computed), and whose RS sector carries a
> discrete 2-bit generation invariant (D4).
>
> **Everything it implies (the forced consequences, gated honestly):** on the spin-2 sector gravity is
> fourth-order/conformal-Willmore-class, so GU inherits the fourth-order-gravity ghost/unitarity question (the
> PT/Krein ghost-parity territory) and, if the `gamma r` mechanism were adopted, the conformal-gravity
> phenomenology disputes — but the operator match does not import that mechanism. `alpha_W` and `f_0` collapse to
> one linked datum via the shared `theta`; the gauge sub-block is fixed by the fourfold intersection; the sole
> free continuous datum is `c_W` (= OQ2-A functional choice), and the sole discrete datum is the RS 2-bit.

This reframes the whole arc from "we built something that fits" (a warning sign) to "the independent legs force a
unique object with a short list of residual freedoms, and here is exactly what remains open." The remaining
freedoms are *named and finite*: `{c_W / OQ2-A functional}` (one continuous, which D1 shows is the
conformal-invariance question of the Willmore functional) + `{RS 2-bit}` (one discrete). Grade: **framing**; it
organizes the computed results (D1, conjugacy, `theta`-order-match) into a single "forced object + implications"
statement in the Weyl idiom, without overclaiming a proof.

---

## Grade (thread group D, overall)

- **D1: concrete algebraic computation** (`tests/threads/D_hclass_vs_conformal_gravity.py`, exit 0) for the
  spin-2 operator match `box^2 h = -4 Bach^(1)`, fourth-order, trace-sector difference located — plus a
  **structural** verdict (special-case/contains, richer off spin-2) with honest caveats (linearized only;
  convention-bound constant; conformal-invariance of GU's functional unresolved).
- **D2/D3/D4/D5: structural / framing** — a well-posed functor conjecture with its would-be theorem (D2), a named
  portable method COI (D3), the one discrete falsifiable target (D4), and the Weyl-idiom "object that must exist"
  deliverable (D5). None claim a proof.

No claim/canon movement. No target number imported (the `-4` is computed, not fitted). What was NOT done: the
nonlinear (full) Bach-vs-curved-ambient-Willmore comparison; construction/verification of the `Sec` functor and
its naturality squares; forcing the RS 2-bit. Feeds WI-068 and the North Star (the honest route to the source
action).

## Next step this opens

The sharpest concrete follow-on: **compute whether GU's OQ2-A functional is the conformally-invariant Willmore
combination** — i.e. does the `c_W`/counterterm that OQ2-A must fix coincide with the term that makes `|H|^2`
conformally invariant (and hence annihilates the trace mode, closing the D1 trace-sector gap and upgrading
"contains on spin-2" to "equals on all sectors")? If yes, H-class GU's gravity sector IS conformal gravity's Bach
equation exactly (up to the extrinsic ambient `R^Y` and the fiber), and `c_W` is fixed *by conformal invariance*
rather than left as the last free continuous datum — collapsing the OQ2-A freedom entirely. That is a single,
well-posed, computable question, and D1 has reduced it to exactly that.
