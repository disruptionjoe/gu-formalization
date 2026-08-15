---
artifact_type: exploration
status: exploration
doc_type: source-typing-and-structural-scope-gate
created: 2026-08-14
work_item: CG-1
channel: coset_versus_gauge
title: "CG-1: GU's 24-dimensional `p` is a DECLARED COSET sector, not a gauge sector. The source's own construction step -- UCSD [00:46:40] 'reduce maximal compact subgroups along the fibers' -- makes K = Spin(6)xSpin(4) the structure group, and `p` the fibre of the reduction. `p` is not a subalgebra, so 'gauge exactly p' is not an available reading at all. The same reduction supplies a K-invariant POSITIVE-DEFINITE form on BOTH the adjoint 45 and the internal 10, which removes all three causes of SRC-3's unboundedness by completion of square. The price is exactly the one AUDIT-noncompact-compact-reduction-EXTERNAL priced: the positivity is K-invariant only, and the reduction is DECLARED but not DERIVED."
grade: "EXACT integer and mod-p linear algebra on so(6,4), 50/50, exit 0, with PV-2's Killing signature, CC-1's uniqueness and SRC-3's published ray all re-run as live controls, and two mutation tests confirming the gates have failure paths. NOT: a derivation of the reduction, a Lagrangian for GU, a claim that GU uses the post-reduction pairing, a quantization or ghost-removal argument, a novelty claim for the Cartan-involution mathematics (VG-V2 prior art), or any claim-status movement."
disposition: P_IS_A_DECLARED_COSET_FIBRE_NOT_A_GAUGE_SECTOR__GAUGE_READING_STRUCTURALLY_UNAVAILABLE_FOR_P_ALONE__SRC3_RE_TYPED_NOT_KILLED__REDUCTION_DECLARED_BUT_NOT_DERIVED__DYNAMICAL_VS_BACKGROUND_COSET_UNDECIDED_BY_DECLARED_CONTENT
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md
  - lab/active-research/joe-directed/cosmological-constant-sign/cc1-killing-signature-cannot-sign-lambda-2026-08-14.md
  - explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - lab/active-research/source-residual-cohomology/sr0-operator-owner-rebase-2026-08-14.md
  - canon/shiab-existence-cl95.md
scripts:
  - tests/channel-swings/joe_directed_coset_versus_gauge_probe.py
---

# CG-1 — `p` is a declared coset sector, and GU's equation is Yang-Mills-LIKE

## Result first

Two results, one source-side and one structure-side.

> **(a) TYPED.** GU's bosonic equation differs from Yang-Mills at five typed
> slots, and it already fails to be Yang-Mills at the first two — the symmetry
> group and the field type — before any question about the action arises. The
> typing is `GU-YM-Δ1..Δ5` below.
>
> **(b) STRUCTURAL.** The 24 directions of `p` are the fibre of a declared
> REDUCTION OF STRUCTURE GROUP, not gauge directions. `p` is not a subalgebra,
> so "gauge exactly `p`" is not an available reading; the only gauge readings
> are "all of `so(6,4)`" or "`k` only", and the source declares the latter in
> three separate places. Under the declared reading `p` carries no wrong-sign
> kinetic term, because the same reduction supplies a positive-definite
> K-invariant form on both the adjoint 45 and the internal 10.

The price is real and is not new: the positivity is `K`-invariant only, never
`G`-invariant, and the reduction is **declared but not derived**. That is
exactly the boundary `AUDIT-noncompact-compact-reduction-EXTERNAL` priced at
`REDUCTION_EXTERNAL` six weeks ago. Nothing here overturns that audit.

---

## Preflight — six lenses, recorded before computing

Each lens proposed a route; the cheapest kill-or-switch and one contrary route
were fixed before any arithmetic was run.

**L1, gauge-theory / fibre-bundle specialist.** A gauge sector is the Lie
algebra of the structure group; a coset sector is the fibre of a reduction of
that group. Route: find whether the source declares a *reduction*. Kill: if the
source declares the gauge group to be `Spin(6,4)` with a curvature norm over
all 45, `p` is gauged and the ghost reading stands.

**L2, symmetric-space geometer.** Route: verify the symmetric-pair axioms
exactly, then check the SIGN of the Killing form on `p`. For `G/K` to be
Riemannian of non-compact type one needs `B|_p` POSITIVE definite — which is
precisely what PV-2 already computed. Prediction: the "wrong sign" is the
*required* sign for a coset. Kill: if `[p,p]` were not inside `k`, there is no
symmetric-space reading at all.

**L3, nonlinear-sigma-model specialist.** In a coset construction the sector's
kinetic term is the pullback of the `G`-invariant metric on `G/K`, whose target
metric is `B|_p`. Route: check that metric's definiteness rather than assume
it; a pseudo-Riemannian `G/K` would bring the ghosts straight back.

**L4, BRST / constraint specialist.** If `p` is gauged, 24 wrong-sign
directions must be removed by cohomology (`W173`'s territory). If `p` is coset,
there is nothing to remove. Decisive discriminator: does `p` CLOSE under
bracket? A gauge sector must. Kill: `p` not a subalgebra ⟹ the gauge reading
cannot be localised on `p`.

**L5, source-fidelity reader.** Route: collect every verbatim sentence in which
the source names the group. Kill: if the source anywhere says the gauge group
is the non-compact real form, the coset reading dies.

**L6, honesty auditor.** Guard against a vacuous repair. Positive-definiteness
makes any norm-square non-negative *trivially*; the non-vacuous content must be
(i) that the positive form is invariant under the REDUCED group and NOT under
the full one, two-sided; (ii) that the invariant-form space genuinely GROWS
under reduction; (iii) that the repair also reaches SRC-3's independent
internal-metric cause; and (iv) that PV-2 and SRC-3 are read at their
REGISTERED claims, not at any downstream gloss of them.

**Cheapest kill-or-switch (declared first).** Compute whether the
Ad(K)-invariant symmetric form space on `so(6,4)` contains a positive-definite
element, given CC-1's result that the Ad(G)-invariant space is 1-dimensional
and indefinite. If it does not, the route dies in one nullspace computation and
SRC-3 stands untouched.

**One contrary route (declared first).** UCSD [00:46:02] / `TII` L158: *"Then
the Lorentz group is the gauge group."* The Lorentz group is NON-compact. If GU
genuinely gauges non-compact groups, Reading A is live and the coset reading is
not GU's posture. Disposition after the swing: recorded below as the strongest
contrary construction, and it is **not** the same construction.

---

## Prior art, attributed — what is NOT re-claimed here

| object | owner | disposition here |
|---|---|---|
| `so(6,4) = k(21) ⊕ p(24)`, Killing negative on `k`, positive on `p`, `k` a subalgebra, `[p,p] ⊆ k`, SM's 12 inside `k` | **PV-2** | re-run as a live control; re-typed, not re-derived |
| Ad(G)-invariant bilinear form space of `so(6,4)` has dimension exactly one | **CC-1** | cited; independently re-verified as a control |
| the source's Mexican-hat potential is unbounded below on an explicit ray, from an ad-pairing cause and an internal-metric cause | **SRC-3** | published ray re-run exactly (`-4`, `+4`); re-typed, not refuted |
| `B_θ(X,Y) = -B(X, θY)` is positive definite; `θ`-even part is the maximal compact; "Weinstein's punchline is the Gupta-Bleuler move" | **VG-V2** (`explorations/big-swing-2026-07-06/`) | **prior art. Computed there on `so(9,5)` and on a θ-stable `so(6,4)` sub-block. This gate runs it on the NATIVE vertical `so(6,4)` as an instance, and claims no novelty for the mathematics.** |
| "take the maximal compact" is EXTERNAL, not GU-forced; Weyl unitarian trick; logically DG-A3 re-imposed | **AUDIT-noncompact-compact-reduction-EXTERNAL** (2026-07-04) | **the strongest adversary to this route. Engaged head-on below; not contradicted.** |
| GU's second Euler equation `E2 = 0` is NOT ordinary Yang-Mills `D_A^*F_A = 0`; the implication fails both ways | **SR-0** (superposition lane property) | **read-only. Owns the OPERATOR-level non-identity. This gate contributes the SOURCE-level typing and the structural typing, which are disjoint from it.** |
| the bare Shiab-curvature is not exact without a quadratic "eddy"/Chern-Simons completion | source pack `weinstein-gu-primary-source-pack-2026-07-30.md` L185, L404 | cited as an open completion; not modelled |
| `WG-B06` (`O 01:34:49`, AUTHOR-STATED self-correction): "The relevant map is a contraction, not a projection" | `lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md` L114 | Layer-0 constraint, respected in Δ3 |
| `WG-SH3`: "Shiab" is not spoken in that episode; manuscript vocabulary only | same, L117 | respected — the name is not attributed to the TOE episode |
| Shiab existence only: at least one natural real-linear equivariant Clifford-contraction map; no injectivity, uniqueness, source-forced selector, anomaly cancellation or generation count | `canon/shiab-existence-cl95.md`, CORRECTION SHIAB-01 | respected |

**Mechanism sweep.** A full-repo sweep by mechanism (coset, symmetric space,
Cartan decomposition, Cartan involution, maximal compact, Iwasawa, polar
decomposition, Goldstone, inhomogeneous gauge group, semidirect product,
non-compact gauge, ghost, wrong-sign, indefinite metric, Killing form,
Yang-Mills-like) found the coset/Cartan machinery **densely covered** and the
naming question **nearly untouched**. The strings `nonlinear sigma model`,
`Nambu-Goldstone` and `pion` return zero genuine hits — but per the
grep-before-novelty rule that is **not** evidence of novelty: the *mechanism*
is fully present in this repo under `Cartan involution`, `maximal compact` and
`coset`. No novelty is claimed for it.

The one prior statement that anticipates this gate's conclusion is a single
undeveloped line in a perspective-pass lens file,
`lab/process/perspective-passes/01-foundational-math-lenses/08-higher-dim-kk.md`
L30: *"an Einstein-Hilbert-like action on the 14D total space would, on
dimensional reduction, give 4D gravity plus a sigma-model of metric-valued
fields, NOT Yang-Mills for SU(3) x SU(2) x U(1)."* It is credited here as the
earliest repo statement of the reading and it is not developed anywhere.

---

## Part (a) — SOURCE: the typed statement `GU-YM-Δ`

Locators are given twice: `TII` = `papers/drafts/Transcript into the impossible.md`
(line number), `UCSD` = `lab/literature/weinstein-ucsd-2025-04-transcript.md`
(line number), plus the transcript timestamp. Both transcripts are automated
and lightly garbled; every quotation below was read in surrounding context.

> ### `GU-YM-Δ1` — SYMMETRY TYPE: the symmetry group is not reductive
>
> Yang-Mills' symmetry is the gauge group `𝒢 = Γ(Ad P)` acting on the AFFINE
> space `𝒜 = A_ℵ + Ω¹(ad P)`. GU's symmetry is the **inhomogeneous gauge
> group** `𝒲 = 𝒢 ⋉ Ω¹(ad P)` — the semidirect product of `𝒢` with its own
> model vector space.
>
> *"the claim is that what we're going to be doing is taking a **semi direct
> product**. So if you are familiar with the Poincare group, think about the
> group of gauge transformations as what the Lorentz group always wanted to be,
> and the space of add valued one forms or gauge potentials being the natural,
> linear space upon which an affine space of connections is modeled. So that'll
> be playing the role of the four momenta."* — `TII` L20 / `UCSD` L32,
> [00:03:06]
>
> **Type delta.** YM's symmetry group is reductive with no nontrivial abelian
> normal subgroup. GU's is a Poincaré-type non-reductive semidirect product
> with `Ω¹(ad P)` as an abelian normal subgroup. Registered as `SC-GRP-05`
> (`lab/sources/source-claim-register.yaml`).

> ### `GU-YM-Δ2` — FIELD TYPE: the field is a group element, not a connection
>
> YM's field is a POINT of `𝒜`: one connection. GU's field is a POINT of `𝒲`:
> one group element, which resolves into an ORDERED PAIR of connections — the
> gauge-transform of the distinguished `A_ℵ`, and the translate of `A_ℵ` — and
> the physically-used object is their **difference**, which is gauge-equivariant
> where each inhomogeneous term separately is not.
>
> *"if I have an element of the inhomogeneous gauge group, I have two
> subelements that can both push that one connection into different places, and
> then I can take a difference. And by the magic of the inhomogeneous gauge
> group, both of those connections are gonna transform properly as well as
> their difference is going to be perfectly gauge equivariant."* — `TII` L65 /
> `UCSD` L77, [00:18:03]
>
> *"Anytime you have a disease, you should either try to get rid of the disease
> and go for zero or to find an even number of diseases so you can have a
> Mexican standoff."* — same locator.
>
> **Type delta.** YM's field is a section of an affine bundle whose curvature is
> a degree-2 object. GU's is a section of a group bundle whose primary
> observable is a DIFFERENCE OF TWO CONNECTIONS — a tensorial degree-1 object.
> The configuration space is a **double coset**, `τ⁺(𝒢)\𝒲/τ⁺(𝒢) ≃ 𝒜/𝒢`
> (`TII` L80 / `UCSD` L92, [00:23:02]; registered `SC-GEO-54`).

> ### `GU-YM-Δ3` — ROLE TYPE: the ad-valued 1-form is the cosmological term
>
> In YM, ad-valued 1-forms occupy the gauge-potential slot: degree-1 objects
> differentiated into a degree-2 curvature. In GU an ad-valued 1-form ALSO
> occupies the slot that `Λ·g_{μν}` occupies in the Einstein equation.
>
> *"my claim is is that this is going to end up as the formula for dark energy,
> what currently is lambda times g mu nu. ... this is actually a pi, which we
> don't use all that much, which is an add valued one form or a gauge
> potential."* — `TII` L17 / `UCSD` L29, [00:02:05]
>
> *"this whole thing is gonna live in add valued one forms, and it's gonna
> replace the cosmological constant times the metric."* — `TII` L20 / `UCSD`
> L32, [00:03:06]
>
> **Type delta.** A degree/role reassignment with no YM counterpart: the object
> that would be "the potential" is instead "the cosmological term", and its
> divergence-freedom comes from EQUIVARIANCE rather than from covariant
> constancy of the metric (`TII` L80, [00:23:02]: *"equivariance is what leads
> to divergence free"*). Consistent with banked **MV-2**: GU's inhomogeneous
> translations are ad-valued ONE-forms, so they shift degree-1 objects. The
> underlying Einstein move is a CONTRACTION, not a projection (`TII` L53,
> [00:13:44]: *"he used a contraction"*), matching Layer-0 constraint `WG-B06`.

> ### `GU-YM-Δ4` — POTENTIAL TYPE: the quartic is derived, not postulated
>
> YM+Higgs carries TWO independent terms: `‖F‖²`, and a separately-postulated
> `V(φ) = μ²|φ|² + λ|φ|⁴` with two free parameters. GU carries ONE term, the
> norm-square of a single curvature expanded about a NON-FLAT background, whose
> quartic and quadratic both fall out, with the quadratic's sign inherited from
> the background curvature.
>
> *"there's no Higgs. The Higgs is an illusion. If you look at the Yang Mills
> sector of the standard model versus the Higgs, it's almost exactly the same.
> They both have a Klein Gordon kinetic term. They both have a quartic term. You
> have that a wedge a in the perturbative expansion of a curvature tensor. So
> when you take its norm square, you get a quartic."* — `TII` L146 / `UCSD`
> L158, [00:42:42]
>
> *"If you take the norm square, you also get a term that looks like the
> unperturbed curvature, interproducted with a wedge a, which is a quadratic. So
> if your curvature is negative, now you start to get a Mexican hat potential.
> Minimal coupling and Yukawa coupling are the same thing. The only thing that's
> really different is the spin."* — `TII` L149 / `UCSD` L161, [00:43:04]
>
> **Type delta.** YM's Higgs potential is an INPUT; GU's is an OUTPUT of one
> background field. This is the claim **SRC-1/SRC-2/SRC-3** analysed, and it is
> the only Δ on which the repo has already computed.

> ### `GU-YM-Δ5` — STRUCTURE-GROUP TYPE: the internal group is an OUTPUT
>
> YM's structure group is chosen — *"you have complete content freedom. You can
> dial in s u three cross s u two cross u one"* (`TII` L53 / `UCSD` L65,
> [00:13:44]). GU's is forced as the MAXIMAL COMPACT SUBGROUP of a non-compact
> real form, and the reduction is a declared construction step.
>
> *"Standard model answers the question, what is the maximal compact subgroup of
> s u three comma two? And that's s u three cross s u two cross u one. ... It's
> spin six cross spin four, and it's the maximal compact subgroup of spin six
> comma spin four."* — `TII` L152 / `UCSD` L164, [00:43:47]
>
> *"we wasted the seventies work because we wanted to avoid indefinite signature
> on the killing form, and I don't know what to do because we're in a maximally
> compact subgroup. We're shielded experimentally from understanding how nature
> handles the, indeterminacy of the killing form. **But this is the right chain.
> Spin six four, spin three comma two, s u three cross s u two cross u one**"* —
> `TII` L155, [00:45:00]
>
> *"I have a four manifold passed to its bundle of metrics. Take the Frobenius
> metric, reverse the trace, **reduce maximal compact subgroups along the
> fibers**, pull back Weyl spinors, and you have one grand unified generation"*
> — `TII` L161 / `UCSD` L173, [00:46:40]
>
> **Type delta.** In YM the internal group is DATA. In GU it is the OUTPUT of a
> Cartan-involution reduction, and the source explicitly flags the residual
> indefiniteness as an OPEN item in its own voice ("I don't know what to do").

### The naming verdict

**GU's bosonic equation is Yang-Mills-LIKE and is not Yang-Mills.** It fails to
be Yang-Mills already at `Δ1` and `Δ2` — the symmetry group is not of YM's type
and the field is not of YM's type — before the action is even written. It is
Yang-Mills-SHAPED only at `Δ4`, where a curvature norm-square appears. The
source itself uses Yang-Mills as a comparison ROW, not an identification:
*"you have an action, in this case, Yang Mills plus Dirac plus Higgs. In g u,
there's a first order theory and then a second order theory that's built from
the first order theory. ... think double copy"* (`TII` L26 / `UCSD` L38,
[00:05:43]).

This is the source-side counterpart of **SR-0**, which reached the same
conclusion independently from the operator side and which owns that result.

### Source-fidelity defect found

The two transcripts DIFFER at the load-bearing [00:45:00] passage. The copy
marked `doc_type: primary_source`,
`lab/literature/weinstein-ucsd-2025-04-transcript.md` L167, **omits the
sentence** *"But this is the right chain. Spin six four, spin three comma two,
s u three cross s u two cross u one"* which is present in
`papers/drafts/Transcript into the impossible.md` L155. The omission flips the
local reading from concession-only to concession-plus-affirmative-endorsement
of the max-compact chain. `AUDIT-noncompact-compact-reduction-EXTERNAL` quotes
only the concession clauses, consistent with having used the lossy copy. This
is a source-hygiene finding, not a refutation of that audit.

---

## Part (b) — STRUCTURE: gauged or coset?

### The three readings, and which the declared content excludes

| reading | gauge algebra | what `p` is | kinetic term on `p` |
|---|---|---|---|
| **A — GAUGE** | all of `so(6,4)` | 24 gauge directions of a non-compact group | wrong-sign under the unique Ad(G)-invariant form ⟹ ghost-like |
| **B — DYNAMICAL COSET** | `k` only | Goldstone-type field valued in `G/K` | pullback of the `G`-invariant metric on `G/K`; POSITIVE definite |
| **C — BACKGROUND REDUCTION** | `k` only | a gauge-fixing / background section | none: `p` carries no propagating mode |

**Reading A is excluded by the declared content**, on two independent grounds.

1. *Structural.* `p` is **not a subalgebra** — exhibited explicitly, not
   asserted: an explicit pair in `p` brackets to a nonzero element whose
   `p`-component vanishes and whose `k`-component does not, and no pair in `p`
   brackets to a nonzero element of `p`. So there is no reading in which `p`
   alone is gauged. The only gauge readings available are "all of `so(6,4)`" or
   "`k` only".
2. *Declared.* The source names the maximal compact as the physical group three
   times (`Δ5` locators) and declares the reduction as a construction step
   ([00:46:40]). It never declares `Spin(6,4)` as the gauge group of a
   curvature norm over all 45 directions.

**Readings B and C are both consistent with the declared content, and the
source does not pick between them.** It never states whether the reduction
section is dynamical. But **B and C agree on everything this route needs**: in
neither does `p` carry a wrong-sign kinetic term.

### The sign that looked like a pathology is the required positivity

This is the cleanest statement of the result.

> The same exact number — **the Killing form is POSITIVE on all 24 directions
> of `p`** (PV-2) — is a pathology under Reading A and is the DEFINING
> POSITIVITY CONDITION under Reading B. `B|_p > 0` is exactly the criterion
> that `G/K = SO(6,4)/(SO(6)×SO(4))` is a Riemannian symmetric space of
> non-compact type, whose invariant metric is the target metric of a coset
> field. And `B|_k < 0` is exactly the standard, healthy condition for a
> COMPACT gauge algebra, where Yang-Mills uses `-B`.
>
> One form, two roles, both signs correct. That combination is `B_θ`.

Certified exactly, on the native vertical `so(6,4)`:

- `θ(X) = -X^T` is an involutive Lie algebra AUTOMORPHISM (checked on all 990
  basis pairs), with `k` its `+1` eigenspace and `p` its `-1` eigenspace;
- `so(6,4)` is transpose-closed, the algebraic hypothesis behind the global
  Cartan decomposition `G = K·exp(p)` with contractible fibre `exp(p) ≅ R²⁴`
  (Helgason Thm VI.1.1 — **cited from literature, not proved here**);
- `k ⊥ p` under the Killing form, and Killing-NULL nonzero elements of
  `so(6,4)` exist;
- `B_θ(X,Y) = -B(X, θY) = tr(X Yᵀ)` has Gram matrix **exactly `2·I₄₅`** in this
  basis, hence is symmetric and positive definite;
- `B_θ` is **Ad(K)-invariant for all 21 generators of `k`** and **NOT
  Ad(G)-invariant** — an explicit generator of `p` gives a nonzero residual.
  This is the price, stated two-sided.

Because the reduction has contractible fibres, it always exists on a
paracompact base and is unique up to homotopy: it carries no topological
information. Reading C therefore adds no degrees of freedom at all, and Reading
B adds 24 positive-metric scalars.

### The internal 10 — SRC-3's "geometric, not a choice" cause

SRC-3 graded its second cause unrepairable because the `(6,4)` DeWitt signature
is intrinsic to `Y14 = Met(X⁴)`. It **is** intrinsic. But the SAME declared
reduction supplies a companion on the internal 10 as well, and SRC-3 did not
consider that:

- every generator of `k` is ANTISYMMETRIC as a 10×10 matrix, so `η₊ = I₁₀` is
  **K-invariant**; an explicit generator of `p` shows `η₊` is **not**
  G-invariant;
- exact two-sided sandwich (explicit rational witnesses for the lower bound,
  mod-`p` rank for the upper bound): the space of invariant symmetric forms on
  the internal 10 has dimension **exactly 1 under `G`** (only `η`, indefinite)
  and **exactly 2 under `K`** (containing the positive-definite `η₊`).

The same enlargement happens on the adjoint: **exactly 1** Ad(G)-invariant form
(CC-1) against **at least 4** Ad(K)-invariant forms, exhibited as `B_θ`
restricted to the `so(6)`, `su(2)_L`, `su(2)_R` and `p` blocks. (The lower
bound is certified; the exact dimension is not needed and is not claimed.)

### What this does to SRC-3 — claim-indexed, and it is a RE-TYPING, not a kill

**SRC-3's target claim** is: *"K is not positive. An explicit `k`-valued ray
gives `K = -4 < 0`, so `V(tv) → -∞` regardless of `Q`. The potential is
unbounded below,"* stated **conditional** on *"the norm-square uses the
Ad-invariant pairing on `ad` and the DeWitt metric on internal form indices"*,
with SRC-3 itself noting *"SG4 leaves the actual quadratic form undeclared."*

The arithmetic is exact and is reproduced here as a live control: `-4` on the
spacelike ray, `+4` with one timelike internal leg. **SRC-3 is not wrong.** But
its stated CONDITION is a pre-reduction condition, and the source declares a
reduction. Under the post-reduction pairing `(B_θ, η₊)`:

| SRC-3 cause | status under `(B_θ, η₊)` |
|---|---|
| 1. indefinite ad pairing (the unique Ad(G)-invariant form) | **removed** — the published `-4` ray becomes `+4`; SRC-3 itself already granted this for `k` on its branch B |
| 2. internal DeWitt `(6,4)`, graded "geometric, not a choice" | **removed** — `η₊` is K-invariant and positive; the timelike leg no longer flips a sign. **New here; VG-V2 treated the adjoint only.** |
| 3. Killing-NULL non-abelian brackets (a cause SRC-3 did not name) | **removed** — see below |

**A third cause, found and then closed.** SRC-3's flat-direction paragraph used
630 ABELIAN generator pairs. On an abelian pair `[X,Y] = 0`, so `a∧a = 0`, so
the quadratic `Q = 2⟨F₀, a∧a⟩` vanishes **together with** the quartic under any
pairing: those directions are flat, not runaways, and SRC-3's clause *"on any
such direction with `Q < 0`"* is never satisfied on them. The genuine third
cause is different and this gate exhibits it: **NON-abelian Killing-NULL
brackets exist** — an explicit ray with `[X,Y] ≠ 0` on which the Killing
quartic vanishes while `Q` need not, because an indefinite form has null
vectors. Under `B_θ` that same ray has a strictly positive quartic, and over
the full basis sweep the quartic vanishes **exactly** on the vanishing
brackets and on no others.

**The whole obstruction is Cauchy-Schwarz.** With any positive-definite
pairing,

```text
V(a) = 2<F_0, a^a> + ||a^a||^2 = ||a^a + F_0||^2 - ||F_0||^2  >=  -||F_0||^2,
```

a completion of square, bounded below globally with the bound saturated iff
`a∧a = -F₀`. The probe verifies Cauchy-Schwarz holds everywhere in the sweep
under `B_θ` and **FAILS somewhere in the same sweep under the Killing form**.
SRC-3's unboundedness is precisely the absence of Cauchy-Schwarz for an
indefinite form — nothing more and nothing less.

**Re-typed SRC-3.** *The source's Mexican-hat potential is unbounded below iff
the norm-square is taken with the PRE-reduction G-invariant forms. It is
bounded below by `-‖F₀‖²` under the POST-reduction K-invariant forms. The
source declares the reduction; it does not declare which pairing enters the
norm-square.*

### What this does to PV-2 — nothing, and the ghost gloss was never PV-2's claim

PV-2's registered claims — the Cartan decomposition, the Killing signature on
each summand, the SM's 12 inside `k`, the nine non-SM compact survivors, and
"observation cannot close PV-1's gap" — are pure Lie algebra and **survive
intact**; they are re-run here as controls.

PV-2 does **not** claim `p` is a ghost sector. Under its own heading *"What
this does NOT establish"* it says: *"The `p` directions are shown to carry the
opposite Killing signature, **not** to be successfully removed. Wrong-sign
kinetic terms make them ghost-like, ... but whether a wrong-sign sector is
consistently removed is a quantization question about the physical state space,
not a group-theoretic one, and **this artifact does not decide it**."*
PV-2's operative model is already the reduction — *"Observation removes only
the 24 non-compact directions of `p`."*

So the reading that treats `p` as a wrong-sign GAUGE sector is a downstream
gloss, not PV-2's claim, and this gate supplies the structural justification
for exactly the thing PV-2 declined to decide. **PV-3 as PV-2 framed it — "is
the wrong-sign `p` sector consistently removable at all" — is the wrong next
question under the declared reading, because there is no wrong-sign `p` sector
to remove.** `W173`/`W132` remain the owners of the fermionic Krein problem,
which is a different object and is untouched here.

---

## Inline hostile review

**Strongest overclaim available, and rejected.** "SRC-3 is dead and the
potential is bounded below." False. What is established is a CONDITIONAL: the
potential is bounded below *under the post-reduction pairing*. GU declares no
Lagrangian, so which pairing enters the norm-square is undeclared — SRC-3 said
so itself, and this gate does not settle it. Claiming the repair is claiming
knowledge of an object (`SG4`) that does not exist.

**Strongest contrary construction: `AUDIT-noncompact-compact-reduction-EXTERNAL`
(2026-07-04), verdict `REDUCTION_EXTERNAL`.** By the Weyl unitarian trick, a
finite-dimensional module carries an invariant positive-definite form **iff**
the acting group is compact; GU's internal group is non-compact, so **no
GU-native positive form exists** and the positivity selecting `K` is imported —
logically identical to re-imposing Distler-Garibaldi assumption DG-A3, which GU
deliberately dropped. That audit is rigorous and this gate does **not**
contradict it. Every positivity statement here is explicitly `K`-invariant and
explicitly **not** `G`-invariant, and the probe certifies the failure of
`G`-invariance two-sided rather than hiding it. The two results compose as:

> The reduction is **declared** by the source (UCSD [00:46:40]) and **not
> derived** by GU-native structure (AUDIT). `p` is therefore a
> *declared-coset* sector whose declaration is an external input.

The audit asked FORCED-vs-EXTERNAL; this gate asks GAUGED-vs-COSET. Those are
different questions and the audit's answer does not settle this one — but it
does cap how strongly this one can be stated, and it has been allowed to.

**Second contrary construction, the one recorded at preflight.** `TII` L158 /
`UCSD` L170, [00:46:02]: *"Feed it the space of connections. Then the Lorentz
group is the gauge group."* The Lorentz group is non-compact, so the source
does contemplate a non-compact gauge group somewhere. **Disposition:** that
passage is about the inhomogeneous gauge group acting on the space of
connections as the affine space fed to a Salam-Strathdee superalgebra — a
different construction from the `Y14` fibre reduction, and there the "gauge
group" is `𝒢` itself in the `Δ1` sense, not `Spin(6,4)` acting on the vertical
10. It does not restore Reading A for the vertical sector. But it is a genuine
tension in the source and it is recorded, not dismissed.

**Weakest seam.** The Reading-B / Reading-C ambiguity. This gate cannot say
whether the 24 coset directions are DYNAMICAL scalars or a non-dynamical
background choice, because the source declares no Lagrangian for the reduction
section. Everything about ghost-freedom survives that ambiguity, but the
PHYSICAL CONTENT of `p` does not: B predicts 24 new positive-metric scalars,
C predicts nothing. Anyone quoting this artifact for a spectrum claim is
quoting it beyond its ceiling.

**Self-audit of this gate's own probe.** Three defects were found and fixed
before the result was recorded: a floating-point `np.linalg.matrix_rank` used
for a load-bearing independence claim (replaced with exact mod-`p` rank),
hardcoded metric factors that would have made two gate checks unfalsifiable
(now read from the metric matrices), and an unreachable dead branch. Two
mutation tests were then run: setting `η₊ := η` (killing the internal
reduction) fails 4 checks and exits nonzero; replacing `B_θ` by the Killing
form fails 11 checks and exits nonzero. The gates have failure paths.

---

## Claim ceiling

This artifact establishes, at EXACT grade:

1. `p` is not a subalgebra, so no reading gauges `p` alone;
2. `(so(6,4), k)` is a symmetric pair with `θ(X) = -Xᵀ`, `k` compact, `B|_p > 0`
   — the criterion for `G/K` Riemannian of non-compact type;
3. reduction to `K` strictly enlarges the invariant-form space, `1 → ≥4` on the
   adjoint and `1 → 2` on the internal 10, in both cases adding a
   positive-definite element;
4. under the post-reduction pairing, all three causes of SRC-3's unboundedness
   vanish by completion of square, and one of those three causes is identified
   here for the first time;
5. the source declares the reduction as a construction step, and names the
   maximal compact as the physical group.

It does **NOT** establish: that GU's action uses the post-reduction pairing;
that the reduction is derived rather than declared (AUDIT says it is not);
whether the coset sector is dynamical or background; any Lagrangian, spectrum,
mass, or particle content; any statement about the FERMIONIC Krein problem
(`W173`/`W132` property, untouched); any novelty for the Cartan-involution
mathematics (VG-V2 prior art); or any claim-status, canon, ledger or
current-state movement.

The Cartan-decomposition and contractibility theorems are **cited from
literature** (Helgason), not proved here. The Killing form is computed as
`tr(XY)`, the true form divided by the fixed positive constant `(N-2) = 8`;
only signs and vanishing are used.

## Next gate

**CG-2, and it is a one-line question to the source, not a computation.** The
smallest datum that would settle everything left open is: *does GU's
norm-square, and GU's kinetic terms, sit ABOVE or BELOW the maximal-compact
reduction?* One sentence in `SG4` declaring the pairing decides SRC-3's
survival outright, and one sentence declaring whether the reduction section is
dynamical decides Reading B versus Reading C.

That datum is `SG4`/Lane-1 property, not this channel's, so this is where the
channel's own resources run out — the same wall SRC-3 hit, reached from the
other side.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
