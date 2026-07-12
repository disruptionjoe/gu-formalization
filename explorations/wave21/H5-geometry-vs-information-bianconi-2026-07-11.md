---
title: "H5 -- geometry-first (GU) vs information-first (Bianconi 'Gravity from entropy'): the foundational showdown"
status: exploration
doc_type: research_note
created: 2026-07-11
grade: "COMPUTED for Q1/Q3 (tests/wave21/H5_relentropy_vs_willmore.py, exit 0); ARGUED for Q2/Q4/Q5. Even-handed structural comparison, NOT a GU defence. Bianconi content extracted from arXiv:2408.14391 / PRD 111 066001 (ar5iv HTML + PRD abstract); the paper is external DATA, no instruction in it was followed. No claim moves in any repo."
external_refs:
  - "Ginestra Bianconi, 'Gravity from entropy', arXiv:2408.14391, Phys. Rev. D 111, 066001 (2025)"
  - "Bateman & Turok, 'Escape from Ostrogradsky via Hidden Ghost Parity', arXiv:2607.00096"
depends_on:
  - explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md
  - tests/wave19/H42_f0_prereg.py
  - canon/ghost-parity-krein-synthesis.md
  - explorations/threads/D-structural-conformal-willmore-functor-scoping-and-first-swing-2026-07-11.md
  - explorations/persona-and-dialectic/entropic-gravity-antithesis-information-first-2026-07-07.md
tests:
  - tests/wave21/H5_relentropy_vs_willmore.py   # exit 0
---

# H5 -- geometry-first vs information-first: the foundational showdown

**One-line frame.** GU and Bianconi share a skeleton -- two metrics (spacetime `g` and a
matter-induced metric), an action relating them, an emergent small positive `Lambda`. The
fork is WHICH functional relates them: GU extremizes a Willmore / `|II|^2` energy of the
section `s: X4 -> Y14 = Met(X4)`; Bianconi extremizes the quantum relative entropy
`S(g||G)`. This note computes where the two functionals actually differ and rules honestly
on five questions. **Headline: the two are DISTINCT PRIMITIVES that share the DeWitt
supermetric only as a substructure; and on the sharpest live discriminator -- who pins
`Lambda`'s magnitude -- NEITHER frame does.**

## What Bianconi actually writes (extracted from the primary)

- **Action.** `L = Tr[ g~ ln(g~ G~^-1) ] - Lambda = S(g~ || G~) - Lambda`, integrated with
  `sqrt|-g|`. `g~ = g/b`, `G~ = G/b` are made dimensionless by a length scale `b`;
  `S(g~||G~) = Tr[ g~(ln g~ - ln G~) ]` is the (Umegaki) quantum relative entropy. (Eqs. 34-36.)
- **Matter-induced metric.** `G~ = g~ + alpha( D|Phi><Phi|D + (m^2+R)|Phi><Phi| ) - beta*Ricci`,
  where `|Phi> = phi (+) omega_mu dx^mu` is the topological bosonic (Dirac-Kahler) field
  (paper restricts to the 0-form + 1-form sector), `D` the Dirac operator, `R` the Ricci
  scalar, and `alpha, beta > 0` couplings. (Eq. 32.)
- **Emergent `Lambda`.** In the weak-coupling limit (`alpha, beta << 1`) the Lagrangian
  reduces to the **dressed Einstein-Hilbert form** `2*beta(R - 2 Lambda') - alpha(|grad phi|^2 +
  ...) - alpha(m^2+R)(|phi|^2 + ...)` with `Lambda' = Lambda/(4 beta)`. (Eq. 39.)
- **Order / ghosts.** Field equations (Eq. 45) are second-order in the weak-coupling limit;
  the paper defers the full modified-equation and stability/ghost analysis to future work
  ("beyond the scope of this paper"). No Ostrogradsky/ghost discussion appears.

Note the tension between the **press-release claim** ("emergent small positive cosmological
constant only dependent on the G-field") and the **equations**: `Lambda` enters Eq. 35 as a
subtracted constant and reappears as `Lambda' = Lambda/(4 beta)`. This matters for Q2.

---

## Q1 -- The two functionals: same object, a limit, or distinct primitives? **[COMPUTED]**

`tests/wave21/H5_relentropy_vs_willmore.py` (exit 0) settles this by direct linear algebra.

- **(A) The relative-entropy Hessian is the Kubo-Mori / Fisher metric.** The 2nd-order Taylor
  coefficient of `t -> S(g || g+tD)` equals `KM(D,D) = \int_0^inf Tr[ D (g+sI)^-1 D (g+sI)^-1 ] ds`
  (verified to rel err `1.8e-7` against the exact matrix-log). So `S(g||G)` is, at second
  order, an **ULTRALOCAL quadratic form in the ALGEBRAIC displacement `D = G - g`** -- zero
  derivatives of `D`.
- **(B) It is a DeWitt-family member.** Commuting, `KM(D,D) = Tr[ D g^-1 D ]` exactly -- a
  g-weighted quadratic form on `Sym^2 T*X` with a **single** inverse-metric weight.
- **(D) But NOT GU's supermetric.** GU's gimmel/DeWitt fiber supermetric (ii-s-coordinate-formula
  sec.1) is `V_g(D,D) = Tr[ g^-1 D g^-1 D ] - 1/2 (Tr[g^-1 D])^2` -- a **double** inverse weight
  (`g^-2`). Numerically `V_g / (1/2 KM) = 1.16 != 1`; in the diagonal case the weights are
  `sum d^2/lambda` (RE) vs `sum d^2/lambda^2` (gimmel). Same FAMILY, different MEMBER.
- **(E) And |II|^2 is a different derivative order entirely.** GU's ACTION is `|II_s|^2`,
  quadratic in the second fundamental form `B ~ Hessian(g) ~ d^2 g` (order 4 in the action;
  the linearized H-class operator is `box^2 h = -4 Bach`, thread D). An ultralocal form in `D`
  and a Hessian-squared functional in `g` cannot be Taylor limits of one another.

**Verdict Q1: DISTINCT PRIMITIVES.** They are not the same object and neither is a
small-coupling limit of the other. What they SHARE is the **DeWitt supermetric on `Met(X4)`**,
appearing at two DIFFERENT LEVELS: for Bianconi it is (a member of the family that is) the
ACTION's own second-order form; for GU it is the AMBIENT FIBER metric `V_h` of `Y14`, on top of
which a Willmore energy is extremized. This is the precise, computed sense in which the two
frames "touch without coinciding." Honest even-handed note: the fact that the information-first
action's Hessian lands *inside the DeWitt family that GU independently uses for its fiber* is a
genuine structural rhyme -- but it is a rhyme at different levels, not an identity, and (per the
2026-07-07 dialectic) reading it as a deeper unity is manufactured-convergence-prone.

## Q2 -- Emergent `Lambda` and the amplitude-determinacy asymmetry **[ARGUED, from the primary]**

This is the sharpest live discriminator, so it gets the most honest reading.

- **GU (Wave 19, H42).** GU leaves the emergent-`Lambda` AMPLITUDE FREE: `f0 =
  rho_theta(0)/rho_Lambda(0)` is set by two named UNBUILT inputs -- `B_i` (theta
  initial/vacuum amplitude; Willmore selects the critical section, not the perturbation
  amplitude) and `mu_DW` (the DeWitt overall dimensionful scale; geometry fixes ratios, not the
  overall scale). GU fixes the `w(z)` SHAPE (`M^2 = 8 H0^2`) but not the amplitude.
- **Bianconi.** Reading the EQUATIONS (not the press release): `Lambda` enters the action as a
  **subtracted constant** (Eq. 35) and appears as `Lambda' = Lambda/(4 beta)` (Eq. 39). The
  G-field equation (Eq. 43) determines the MATTER field `|Phi>`, and the "emergent" `Lambda`
  term is dressed by the couplings `alpha, beta` and the bare `Lambda`. The paper makes **no
  magnitude prediction** and explicitly argues only the weak-coupling regime. The abstract's
  "only dependent on the G-field" is the claim that the `Lambda` term is packaged WITH the
  relative-entropy/G-field structure and is naturally small and positive at weak coupling -- NOT
  that its magnitude is derived.

**Verdict Q2: NEITHER FRAME PINS `Lambda`'s MAGNITUDE.** The hoped-for asymmetry (Bianconi
determines `Lambda`, GU does not) does NOT hold at the level either can currently compute. Both
leave the amplitude to unfixed inputs: GU to `{B_i, mu_DW}`, Bianconi to `{Lambda, beta}`. Where
Bianconi is genuinely CLEANER: the **sign/positivity** of `Lambda` is structurally natural from
the entropic action (relative entropy `>= 0`, and the small-positive `Lambda'` drops out of the
weak-coupling reduction), whereas GU's `Lambda` SIGN is set by the still-open `|H|^2`-vs-`|II|^2`
functional binary (thread B: `|H|^2 = -1` wrong-sign vs `|II|^2 = +2`). So on `Lambda`: **tie on
magnitude (both free); edge to Bianconi on sign-naturalness.** This retires the strongest
pro-information-first hypothesis of the H5 brief.

## Q3 -- Order and ghosts **[COMPUTED origin; ARGUED cost/benefit]**

- **Confirmed from the primary:** Bianconi is 2nd-order (weak coupling), no ghost analysis
  offered. GU's H-class Willmore is Bach-class / 4th-order on the TT graviton
  (`box^2 h = -4 Bach`, thread D, exact sympy), Krein-clearing its ghost via Bateman-Turok
  hidden ghost parity (arXiv:2607.00096).
- **Computed origin of the order gap (test check C):** the LINEAR term of `S(g||G)` is `-Tr[D]`.
  Because Bianconi's `G` carries the Ricci scalar `R` INSIDE it (`- beta*Ricci`, and `(m^2+R)`),
  this linear term delivers Einstein-Hilbert `~2*beta*R` at LINEAR order in the displacement -- a
  term linear in `R` gives a 2nd-order Euler-Lagrange equation. `|II|^2` has NO linear term (it
  is intrinsically quadratic in the Hessian `B`), so its EL is 4th-order. The 2nd-vs-4th split is
  thus a computed consequence of WHERE curvature enters: linearly-inside-`G` (Bianconi) vs
  squared-Hessian (GU).
- **Is 4th-order a pure cost?** No -- it BUYS the conformal/Weyl sector. GU's Bach operator is
  the conformal-gravity operator on spin-2; the `|II|^2 = |H|^2 - R^X` Gauss identity means the
  Willmore functional carries the Weyl-sector dynamics that a 2nd-order entropic action, whose
  graviton kinetic term is just `2*beta*R` (Einstein, no Weyl), CANNOT reproduce. Bianconi's
  gravity is Einstein + matter dressing; it has no independent conformal graviton sector.

**Verdict Q3: Bianconi is genuinely cleaner on order/ghosts (2nd-order, ghost-free by
construction, no Krein apparatus needed).** That is a real cost for GU -- BUT the 4th-order
structure is not gratuitous: it is exactly the conformal/Weyl sector, absent in the entropic
frame. The trade is "2nd-order simplicity + ghost-freedom" (Bianconi) vs "a conformal graviton
sector at the price of a 4th-order operator and a Krein-space ghost-clearing" (GU). Which is a
virtue depends on whether the Weyl sector is physically wanted -- an open empirical question, not
a settled point for either side.

## Q4 -- Matter representation **[ARGUED]**

- **Bianconi:** Dirac-Kahler matter `|Phi> = phi (+) omega_mu dx^mu (+) ...` -- inhomogeneous
  differential forms (0-form + 1-form, with the 2-form sector available), acted on by the Dirac
  operator `D = d + delta`. The forms are the matter; `G` is built bilinearly from them.
- **GU:** Clifford/spinor matter on the `(9,5)` Krein space `V (x) S`, `Cl(p,q)` with `q>0`
  timelike directions; the derived generation `Z/3` lives on `Lambda^2_+` (self-dual 2-forms,
  dim 3) as the `SU(2)_+` triplet multiplicity.
- **Correspondence?** There IS a formal contact point: Dirac-Kahler theory is the statement
  `Cl(T*X) ~= Lambda^* T*X` -- Clifford multiplication on spinors is isomorphic to the exterior
  algebra of forms, and Dirac-Kahler fermions are known to carry a "flavour" multiplicity equal
  to the number of spinor columns (`2^{n/2}` in `n` dims; the well-known Dirac-Kahler
  degeneracy). So both frames' matter lives in `Lambda^* T*X` and both extract a MULTIPLICITY from
  its 2-form content. But the resemblance is superficial in the load-bearing detail: **Bianconi's
  2-form is a bosonic matter field (part of `|Phi>`), whereas GU's `Lambda^2_+` triplet is a
  SPINOR generation index carrying `Spin(10)` `16`s.** GU's `3` is the self-dual `SU(2)_+`
  multiplicity of a 4-base (a geometric index); Bianconi's form degeneracy is the flat
  Dirac-Kahler flavour count. They are not the same `3`, and Bianconi neither derives nor targets
  three chiral generations.

**Verdict Q4: fundamentally different matter contents that share only the ambient exterior
algebra.** Both live in `Lambda^* T*X`; both have a 2-form sector. But bosonic-form-matter
(Bianconi) vs spinor-generation-index-on-`Lambda^2_+` (GU) are not in correspondence, and only GU
makes a generation-count claim. No cash for either side here.

## Q5 -- The decider **[ARGUED]**

Is there a concrete observable or internal-consistency test that decides geometry-first vs
information-first, not by taste?

1. **`Lambda` magnitude:** NOT a decider now -- both frames leave it free (Q2). Ruled out.
2. **The conformal/Weyl graviton sector (the sharpest internal-consistency decider).** GU
   carries an independent 4th-order Weyl sector (Bach); Bianconi's weak-coupling gravity is
   strictly Einstein (`2*beta*R`) with no independent conformal graviton. These are DISTINCT
   theories of the spin-2 field: they differ in the graviton propagator (`1/p^2` for Einstein vs
   the `1/p^4`-modified Bach propagator with its extra pole). Any probe sensitive to the
   graviton's high-momentum behaviour or to a massive spin-2 ghost/partner -- gravitational-wave
   dispersion at high frequency, the short-distance modification of the Newtonian potential
   (Stelle's Yukawa correction), or the lensing-sign disputes known for conformal gravity --
   discriminates them. This is a genuine physical fork, not a re-description.
3. **Order + ghost content as an internal decider.** If the correct theory of gravity is exactly
   2nd-order and ghost-free, Bianconi's frame is favoured and GU pays for the Weyl sector it must
   Krein-clear; if a conformal graviton sector is physically required, GU's `|II|^2` supplies it
   natively and the entropic action cannot. This is decidable in principle by the same
   spin-2-sector observables.

**Verdict Q5: yes, there is a decider, and it is the SPIN-2 SECTOR, not `Lambda`.** GU predicts an
independent 4th-order conformal/Weyl graviton (Bach), Bianconi predicts pure 2nd-order Einstein
gravity dressed by matter. They are empirically distinguishable at the level of the graviton
propagator (short-distance potential / high-frequency GW dispersion / conformal-lensing signs).
At the level of the emergent-`Lambda` amplitude that both currently compute, they are
empirically EQUIVALENT (both free) -- so anyone hoping `Lambda` decides it will be disappointed.

---

## Side-by-side table

| Axis | GU (geometry-first) | Bianconi (information-first) | grade |
|---|---|---|---|
| Functional relating the two metrics | `|II_s|^2` / Willmore energy of section `s: X4 -> Met(X4)` | quantum relative entropy `S(g~||G~) = Tr[g~(ln g~ - ln G~)]` | COMPUTED |
| 2nd-order form | Hessian-squared (order 4 in `g`); ambient fiber is DeWitt `V_h` (double `g^-1`) | Kubo-Mori/Fisher ultralocal supermetric in `D=G-g` (single `g^-1`) | COMPUTED |
| Same object? | NO -- distinct primitives; share DeWitt FAMILY at different LEVELS | (as left) | COMPUTED |
| Induced metric built from | distortion `theta = II_s` of the section (`s*theta = II_s`) | `G~ = g~ + alpha(D\|Phi><Phi\|D + (m^2+R)\|Phi><Phi\|) - beta*Ricci` | ARGUED/primary |
| Emergent `Lambda` -- SIGN | set by open `\|H\|^2`-vs-`\|II\|^2` binary (thread B) | naturally small + positive (weak-coupling reduction) | ARGUED |
| Emergent `Lambda` -- MAGNITUDE | FREE: `f0` needs `{B_i, mu_DW}` (unbuilt source action) | FREE: `Lambda' = Lambda/(4 beta)`, bare input, no number | ARGUED/primary |
| Order + ghost | 4th-order (Bach/Stelle); ghost Krein-cleared (Bateman-Turok) | 2nd-order (weak coupling); ghost-free by construction; not analyzed | COMPUTED origin |
| Order buys | the conformal/Weyl graviton sector (`\|II\|^2 = \|H\|^2 - R^X`) | nothing extra -- Einstein graviton only | ARGUED |
| Matter rep | Clifford spinors on `(9,5)` Krein; gen `Z/3` on `Lambda^2_+` | Dirac-Kahler forms `phi (+) omega (+) ...`; bosonic | ARGUED |
| The decider | the spin-2 sector (Bach 4th-order vs Einstein 2nd-order graviton propagator) | (same fork) | ARGUED |

## Where each frame wins (even-handed)

- **Bianconi wins:** order + ghosts (2nd-order, ghost-free, no Krein apparatus needed);
  sign-naturalness of `Lambda` (positivity is structural to relative entropy); economy (one scalar
  functional, matter and `Lambda` in one action); it is a COMPLETE, published, self-contained
  action -- GU's source action is still UNBUILT. On raw "is there a written-down dynamics," Bianconi
  is ahead of GU today.
- **GU wins:** it carries a genuine conformal/Weyl graviton sector the entropic action cannot
  reproduce; it makes a matter-content and generation-count claim (`Z/3` on `Lambda^2_+`) that
  Bianconi does not attempt; its `Lambda` is at least tied to two NAMED geometric inputs
  (`B_i, mu_DW`) rather than a single bare constant.
- **Tie / no-cash:** the `Lambda` MAGNITUDE (both free); the DeWitt-supermetric rhyme (real but
  cross-level, manufactured-convergence-prone per the 2026-07-07 dialectic); the matter `Lambda^*`
  ambient (shared algebra, different content).

## RE-RANK signal

**The H5 discriminator sharpened, and it MOVED off `Lambda`.** Going in, the hoped-for
discriminator was "Bianconi pins `Lambda`, GU does not." The primary refutes that: **neither
frame determines `Lambda`'s magnitude** (Q2). So `Lambda`-determinacy is DEAD as a
geometry-vs-information decider. The live decider RE-RANKS to the **spin-2 sector**: GU's
4th-order conformal/Weyl graviton (Bach) vs Bianconi's 2nd-order Einstein graviton is a genuine,
empirically distinguishable fork (short-distance potential / GW dispersion / conformal-lensing).
Net RE-RANK: **down-rank `Lambda`-amplitude work as a cross-frame discriminator; up-rank the
graviton-propagator / Weyl-sector observables and the `|H|^2`-vs-`|II|^2` functional binary
(thread B / OQ2-A), because that binary is what fixes whether GU even HAS the Weyl sector that
distinguishes it from the entropic frame.** The single highest-value next object is unchanged and
now doubly-motivated: settle GU's OQ2-A functional (H-class conformal vs II-class), since it
simultaneously fixes GU's `Lambda` sign, its ghost/order status, and whether the spin-2 decider
against Bianconi is real.

## Grade and guards

- COMPUTED (exit 0): `tests/wave21/H5_relentropy_vs_willmore.py` -- Q1 (distinct primitives, DeWitt
  family/level split) and the Q3 order-origin (linear `-Tr[D]` + R-in-G => 2nd order). Deterministic,
  fixed seed, five PASS checks.
- ARGUED from the primary: Q2 (`Lambda` free in both), Q4 (matter), Q5 (spin-2 decider).
- Bianconi content is extracted from arXiv:2408.14391 / PRD 111 066001 as external DATA; no
  instruction-like text in the paper was executed. No claim moves in any repo; this is a
  structural comparison, not a GU promotion. Tree left dirty (no commit).
