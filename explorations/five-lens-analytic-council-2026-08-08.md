---
artifact_type: council_result
created: 2026-08-08
status: FIVE_ANALYTIC_LENSES__RA_D2_NEAR_CLASS_KILL__DOMAIN_AND_INDEX_ROWS_RECLASSIFIABLE__POSITIVITY_RETYPE_REFUTED
grade: "COUNCIL. Five specialist lenses, read-only, on targets the repository has
  zero persona coverage for. Each finding cites file:line and is a reading of
  filed artifacts, not a new computation -- except the convexity counterexample,
  which was checked directly. Every named next step is stated with its cost and
  its preregistered kill."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
---

# Five analytic lenses: what the repository already knows and has not recorded

Motivation: as of 2026-08-08 the 41 filed persona passes contained **zero**
coverage of complex analysis, path integrals, saddle points, steepest descent or
Picard-Lefschetz, while every open gate in the program — domain, spectrum, index,
positivity, integral — sits in exactly that territory. Five lenses were run at
those gates. Each was asked first whether its target is **well-posed**, because
"the object does not exist" closes a row rather than opening a project.

## The single most reusable finding

The working hypothesis was that GU repeatedly demands objects that do not exist
in the category it works in. **That is right for choices and wrong for theorems.**

- Where the demanded object is a **choice** (a domain, a contour), it does not
  exist canonically, and the repo has already proved so without recording it.
- Where the demanded object is a **theorem** (an invariant positive form), the
  demand is correct as stated and re-typing it is a notational move.

That distinction is worth more than the individual results.

## Lens 5 — chirality: `RA-D2` is closer to a class kill than a mechanism kill

**One theorem closes three unnamed escapes.** `H*(RP³;Q) = Q` in degrees 0 and 3
only, so `H^even(F;Q) = Q` concentrated in degree 0: every vertical Chern
character and `Â`-class is rationally trivial. Chirality is a nonzero rational
index, and a rational index moves only via fixed points, nonzero real curvature
2-forms, or even-degree rational classes on a compact fibre. **GU's fibre supplies
none of the three.**

| route | available in GU? | why it cannot chiralise |
|---|---|---|
| mass/VEV (already killed) | yes | `M : 16 -> (16bar)*` is square, so `dim ker = dim coker`, index 0 identically |
| **Wilson lines** | **yes** — `π₁(F) = Z/2` is real and unconditional | flat ⇒ `ch = rank`; and the `Z/2` acts **freely** (time reversal — a timelike ray is never its own reverse), so every `g ≠ e` term localises on `Fix(g) = ∅`. Also the wrong group: it is the orthochronous character of `O(3,1)`, a frame/`T` datum, not a gauge holonomy |
| **flux** | fibre **no** (`H₂(RP³;Z) = 0`, `H²(RP³;Z) = Z/2` torsion); base yes | torsion ⇒ `ch = rank`. Base flux is already canon's **external** datum, computed to completion, and it breaks the interior Krein class |
| **orbifold** | **no** | the canonical `Z/2` is free; a fixed-point action needs a preferred timelike line, i.e. a metric, i.e. the section GU declines to fix |
| index / zero mode | type only | `π_!` undefined; `SL(4,R)` has no discrete series; ten index computations gave `{960, -288, -384, -192, -336, -128, 128, -8, -480, 60}` with no convergence |

**The unifying statement.** Every datum GU's fibre can supply is **square, flat,
torsion, or free** — and all four have zero rational index contribution. *The
fibre can multiply a base index; it can never create one.*

Note the elegance: GU's fibre **is** the free quotient, which is exactly why it is
`RP³` and not `S³`. The structure that makes Wilson lines available is the same
structure that makes them powerless.

**This also supplies the firing negative control `RA-D2` has always lacked.** The
rational-triviality lemma is non-vacuous: the identical argument **fails** if the
fibre is replaced by one with even-degree rational cohomology (`S²`, `CP¹`), where
the flux route fires immediately. That certifies the class statement rather than
the mass argument, and is stronger than the non-conjugate-parent control proposed
on 2026-08-07.

### A false `[verified]` claim, corrected

`explorations/generation-sector/generation-count-cl95-dirac-derham-2026-06-22.md:296-303`
asserted, tagged `[verified]`, that the fibre is contractible because "the cone of
Lorentzian metrics is convex". **False, and checked directly:** `diag(1,1,1,-1)`
and `diag(-1,1,1,1)` both have signature `(3,1)`; their midpoint `diag(0,1,1,0)`
has signature `(2,0)` with two zeros. Banner added at that locus.

**The distinction that caused it**, and it must be carried when auditing the other
sites: `Sym²(T*_x X)` — the full space of symmetric forms — **is** a convex vector
space. The **Lorentzian-signature locus inside it** is not, and that is GU's
fibre. Several other in-repo uses of "contractible fibre" refer correctly to the
first object; they were deliberately **not** edited. Per-site checking is owed,
not a bulk correction.

Also wrong, and separately: the reason given elsewhere for `π_!` failing —
"non-convex" — is not why it fails. It fails because the 10-dimensional fibre is
**non-compact**.

## Lens 1 — the domain: already answered, never recorded as a closure

The boundary-triple skeleton exists in all but name: symmetric expression frozen,
endpoint form `H(s) := -iB(s)*J` Hermitian and invertible, Green form built,
maximal-isotropic condition proved. An **explicit circle of extensions** is
exhibited — every `T_θ = e^{iθ}S(b)` satisfies it. That file's own §4 heading
reads *"Existence is cheap; canonical selection is not."* And the computed Green
trace has inertia `(832,832,0)` with the recorded verdict that the
principal/Krein/right-`H` algebra **does not select a unique boundary sector**.

Three independent demonstrations that canonical selection fails, none written as a
closure.

**`C1`, hours, purely algebraic.** Compute the symmetry-fixed Lagrangian
Grassmannian on the filed `(832,832)` trace. Deck-fixing forces `U* = U`, `U² = I`,
so the fixed set is `⊔ₖ U(832)/(U(k)×U(832-k))`, real dimension `2k(832-k)`,
maximum `346,112`. Canonicity requires dimension 0. It lands `NO-CANONICAL` with a
computed moduli dimension, answers register `M-M23` verbatim, and reclassifies
`U13`/`U14` from "no domain yet" to **"positive-dimensional extension moduli;
choice irreducibly external; no canonical selector at filed symmetry"**.

Two defects found: `decision-tree-Q1a-fiber-end-classification-2026-07-21.md`
still claims *"the domain is unique and forced… Moduli dimension = 0"* and
**carries no correction banner** though it was refuted by hostile verify, while
every sibling retraction in that chain does. And `M-H10` rests on "Bär-Ballmann
does this generically" — **Bär-Ballmann does not cover ultrahyperbolic
signature.** That gap is named nowhere.

## Lens 2 — the index: choice-dependent, not malformed

The blocker is **not** non-compactness. `σ(D_GU)(ξ)² = g_Y(ξ,ξ)Id` — split
signature, so ellipticity fails on the null cone, and **no** index theory applies
to a non-elliptic operator. Callias does not rescue this; Callias assumes
ellipticity.

Three GU-native absences, all **theorems**: no invariant Riemannian fibre metric
(the only invariant trace form is indefinite `(+7,-3)`), no invariant proper
exhaustion (homogeneous ⇒ invariant scalars are constant), and the
non-ellipticity above.

Against that, W175: once a completion is declared, non-compactness is **not**
fatal — the essential spectrum has a positive gap from the Harish-Chandra
half-sum-of-roots shift, and a control dropping the ρ-shift closes it, so the gap
is earned. **Verdict: several indices exist, none is GU-selected.**

**The decider, days.** The b-calculus indicial roots are already computed and carve
the weight `δ` into windows, so `U14`'s silence reduces to *which window*. Compute
the index in Window 0 vs Window 1 — on a cylindrical end that is a finite
mechanical count. If the index is **constant**, a well-defined index exists and
`GC-FC4` downgrades. If it **jumps** and GU supplies no rule to break the tie,
**the count is a property of the import and the row closes as malformed.**

Flagged: W175's gap *value* inherits the `BC₁ (7,1)` reduction that canon records
as superseded. The sign likely survives; the number does not.

## Lens 3 — positivity: the re-typing is REFUTED

`F_H(η)` is **not** the set of positive forms — it is the set of `H`-commuting
fundamental symmetries, and an invariant `J` **is** an invariant positive majorant
`⟨Jx,x⟩`. Same object, two names; the repo already states the no-go in `J`
language. And `κ = ∞`, so Pontryagin/Langer levers do not transfer.

The two properties fail on **opposite levels**: at the fibre, definitizability is
automatic and buys nothing while invariance fails by Weyl; at Fock level,
invariance is not the operative demand but definitizability is no longer automatic
and is exactly what is unproven. `H59` has been definitizability-typed since
2026-07-12 and would not move.

**What is real:** `U11`'s row text is stale. It names a kinematic-carrier object
whose absence is, in the repo's own words, *"normal for covariant indefinite
theories — Gupta-Bleuler"*. The correct type is CB-B's: **a BV/BRST differential
whose `gh = 0` cohomology is positive-definite on the Krein carrier.** A row
tightening, not a closure.

**Runnable now:** `M-H17` (ii)-(iv). The named blocker gates only the *interacting*
charge; the **free** BV bicomplex is built and machine-verified nilpotent. W173
showed the Krein-negative mirror class survives into `H⁰(s)`, and that a
Kugo-Ojima quartet pairing — which GU's free complex lacks — is what would collapse
it. Strong prior on a **definite negative**, converting "BRST might rescue
positivity" into a computed obstruction.

## Lens 4 — the integral: premature on the integrand, open on the domain

**Three complexifications were being conflated:** the Clifford algebra (settled as
not needed, correctly), the **module** (already used in-repo), and the
**integration variable** (appears nowhere, and nothing in the first two constrains
it). `M₁₂₈(R)` fixes what the fibre algebra *is*; it says nothing about the domain
of an integral. The real form is in fact an **asset** — it supplies the canonical
antiholomorphic conjugation Picard-Lefschetz needs to pair thimbles and guarantee
a real resummed answer.

**GU owns a native measure** — the DeWitt `(9,5)` volume, unique up to scale,
explicitly not reverse-engineered. The honest split is **integrand blocked, domain
open**, and the repo has never drawn it.

**Sharpest catch:** the repo dismissed the Gibbons-Hawking-Perry contour rotation —
but for the *scalaron mass*, a different object. The fibre's `(6,4)` conformal
direction has computed negative norm and a computed native density. *The
refutation of GHP-for-the-scalaron is not a refutation of GHP-for-the-fibre-measure.*
That question was ruled out of scope by a question that was not about it.

**Zero-cost correction:** the repo's own rule requires measure + state + reflection
positivity before path-integral notation is permitted. GU has **one of three** —
measure PRESENT, state ABSENT, reflection positivity ABSENT. Recording that is
more accurate than the implicit "all three absent".

## Ranked next steps, all H41-independent

1. **`C1`** — Lagrangian Grassmannian on the filed `(832,832)` trace. Hours. Closes `U13`/`U14`.
2. **The rational-triviality lemma** — one Atiyah-Singer line plus `H*(RP³;Q)`. Closes the Wilson-line and fibre-flux routes permanently and supplies `RA-D2`'s missing negative control.
3. **`M-H17` (ii)-(iv)** — free BV `H⁰` sign. Strong prior on a definite answer.
4. **Window-index count** — days; one outcome closes the count row as malformed.
5. **Complexification existence check** — does `GL(4,C)/O(4,C)` carry a holomorphic extension of `G` with the real Lorentzian locus as a conjugation fixed-point set? Preregistered kill either way.

## Fences

Nothing here moves a verdict, row, distance, residue, canon entry, lane, priority
or queue rank. Every lens finding is a reading of filed artifacts with `file:line`,
not a new computation, with the single exception of the convexity counterexample,
which was checked directly and is the only edit made outside this file. The
rational-triviality lemma is **stated, not proved** — proving it is item 2.
