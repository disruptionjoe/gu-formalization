---
title: "Nikulin order-3 rho: ghost-subtracted A vanishes; geometric gamma-traceless B is nonzero; native Krein-graded identification remains open"
status: staged
doc_type: results
created: 2026-07-10
grade: "COMPUTED / exact (Q(zeta) rational arithmetic; legs 60/1070/183/962 asserts, referees 31/74/108/253 checks, all exit 0, re-run in-repo). Adversarially verified by independent referees using different arithmetic (Q(i*sqrt3) vs Q(zeta)), a lift-free holomorphic-Lefschetz route, and a 24-combination convention sweep. Geometric-benchmark grade: the GU source-action operator identity remains OPEN (SG4 MISSING-CARRIER). Internal tier (caveat (e)). No CANON.md promotion; pauses for Joe."
depends_on:
  - canon/families-e-invariant-order3-monodromy-RESULTS.md
  - explorations/twenty-lens-source-action-build-method-sweep-2026-07-09.md
  - canon/rs-function-space-framework-SPEC.md
  - canon/source-action-family-index-interface-SPEC.md
  - absorbed/gu-source-action/DEAD-ENDS.md
scripts:
  - tests/rs-function-space/order3-rho/leg1_calibration.py
  - tests/rs-function-space/order3-rho/leg2_dirac_rho.py
  - tests/rs-function-space/order3-rho/leg3_rs_rho.py
  - tests/rs-function-space/order3-rho/leg4_arena.py
  - tests/rs-function-space/order3-rho/referee_leg1.py
  - tests/rs-function-space/order3-rho/referee_leg2.py
  - tests/rs-function-space/order3-rho/referee_leg3.py
  - tests/rs-function-space/order3-rho/referee_leg4.py
---

# The order-3 equivariant rho: built, computed, adversarially verified

## Construction scope correction — Joe approved, 2026-11-20

Authority: `joe_direct_chat_2026_11_20_b`; wording correction, with existing
status and grade retained. The Nikulin order-3 **ghost-subtracted** benchmark A
has index -42 and zero rho class. The **geometric gamma-traceless** benchmark B
has index -38 and nonzero classes (0,2,1)/3. The source-native **Krein-graded**
complex remains unidentified at this invariant: retaining ghosts does not
specify their index grading or trace. A/B is a comparison, not an exhaustive
classification of source constructions. Neither residue supplies an integer
family count. Statements below about a binary or sole decider are restricted
to their declared comparison; they do not require building the source action
before testing defined structural subfamilies. Paper and released bytes are
unchanged. See the [approved-scope audit](../explorations/conditional-build/native-complex-order3-fork-2026-11-20.md)
and [follow-up benchmark and map test](../explorations/conditional-build/krein-order3-observation-label-2026-11-20.md).

The gated object named by `families-e-invariant-order3-monodromy-RESULTS.md` -- the fine equivariant
(spectral) rho of an order-3 Nikulin symplectic K3 monodromy -- has now been BUILT and computed
exactly, for both the spin-1/2 Dirac operator and the ghost-subtracted spin-3/2 benchmark A, at
geometric-benchmark grade. Method: 17-agent adversarial campaign (3 design routes -> 1 synthesized
spec -> 4 exact-computation legs -> 8 hostile referees -> completeness critic); every leg survived
refutation (0 killed).

## The construction

`phi` = order-3 Nikulin symplectic automorphism of K3 (6 isolated fixed points; local weights
`(zeta, zeta^{-1})`, `zeta = e^{2 pi i/3}`, forced by `phi* Omega = Omega`). Mapping torus
`T_phi = (K3 x S^1)/(Z/3)` with the product metric (Yau: average the Kahler class; `phi` is an
isometry). Flat characters `alpha_k`, `k = 0,1,2`; `rho_k = eta_{alpha_k} - eta_{alpha_0}` at the
eta level, h reported separately. Here RS means benchmark A, Dirac twisted by `T_C - 1C`, checked against its non-equivariant
gate `ind RS = -42 = 21 sigma/8` (the established AGW/gravitino density; rivals `T_C - 2C` (-44) and
total-space `TM_C - C` (-40) fail this A consistency gate, without being ruled out as different constructions, and are shown failing as negative checks in the scripts).
Spin lift: unique for odd order (`Hom(Z/3, Z/2) = 0`), pinned operationally by
`ind_phi(D) = +2 =` Hodge trace.

## Results (exact; periodic S^1 spin structure -- see convention note)

| operator | eta = rho (k = 0,1,2) | mod-Z class | Z/24 arena N | verdict |
|---|---|---|---|---|
| **Dirac (spin-1/2)** | (0, -2/3, +2/3), h = (2,0,0) | **(0, 1, 2)/3 -- NONZERO** | (0, 16, 8) | **Z3_NONZERO** |
| **A: ghost-subtracted RS** | (0, +2, -2), h_virt = (14,12,12) | **(0, 0, 0)** | (0, 0, 0) | **Z3_ZERO / 2-PRIMARY** |

Historical A-scoped verdict string: `DIRAC_RHO_Z3_NONZERO__RS_RHO_2PRIMARY__LOCATED_NOT_FORCED_SURVIVES_FINE_SPECTRAL_LEVEL`.

**The ghost-subtracted A vanishing is STRUCTURAL.** At every fixed point the RS twist character is
`c = tr(g|T_C K3) - 1 = 2(zeta + zeta^{-1}) - 1 = -3 == 0 mod 3` -- forced by the symplectic weight
structure. Equivalently (referee's independent derivation): `rho_k == -(k/3) * ind_fiber mod Z`, and
`3 | 42` -- the Rokhlin bulk-even mechanism resurfacing at the fine spectral level. Hence **for ANY
order-3 symplectic K3 automorphism the ghost-subtracted A fine rho has zero order-3 class.**
This closes that invariant for A in the stated symplectic class; it does not close B or a
separately specified native Krein complex.

**The Dirac finding is genuinely new for the program.** The spin-1/2 rho carries an honest nonzero
order-3 class `(0,1,2)/3` -- the program's FIRST nonzero mod-3 SPECTRAL number, upgrading "located"
from a boundary-framing datum (`e_R = 1/12`) to a fine spectral invariant on actual K3-family
geometry. Robust across all spin lifts, both circle spin structures, all sign/relabel conventions
(24-combination sweep; only the 1-vs-2 label moves). Still **located, not forced**: nothing ties it
to a generation count, while only the selected A comparator has vanishing class. B is already a nonzero control;
the native generation-arena operator is not identified.

## Verification record

- **Gate ledger (all exact asserts):** Lefschetz forces `(r,s) = (10,12)` (order-2 package `(14,8)`
  REJECTED, `L = 12 != 6`); G-signature `= 2` by fixed-point AND lattice routes; quotient-resolution
  closure (`K3/<phi>` resolves back to K3: sigma and chi bookkeeping); `ind_phi(D) = 2`,
  `ind_phi(RS) = -6` by Atiyah-Bott AND Hodge; non-equivariant `ind D = 2`, `ind RS = -42`; kernel
  multiplicities `(16,12)` unique by exhaustive sweep AND Hodge (`H^{1,1} = 8 + 6 zeta + 6 zeta^2`);
  `sum_k eta_k = 0`; `rho_2 = -rho_1`, all real; Donnelly isotypic averaging == direct spectral
  values EXACTLY (both operators, both k); disk fixed-point route agrees with identical mod-Z
  classes; orbifold-average integrality (2, -18, -4).
- **Hostile referees (2 per leg, 0 refutations):** independent re-derivation in different arithmetic
  (sympy cyclotomics / `Q(i sqrt3)` pairs), a lift-free holomorphic-Lefschetz route, an independent
  CP^2 normalization pin the legs never used, and a 24-combination convention sweep. The identical
  machinery produces the NONZERO Dirac class and the ZERO RS class -- the pipeline is not rigged
  toward either answer.
- **One defect found and corrected (labeling only):** the direct-route values are the PERIODIC
  (non-bounding) S^1 spin-structure package; the originally declared "bounding" structure gives
  Dirac `(0, +4/3, -4/3)`, h = (0,0,0) and RS `(0, -4, +4)` -- differing by exact even integers, so
  the classes, arena image, and verdict are IDENTICAL. The disk route computes the bounding
  structure (which is why it agrees there exactly, implied `ind_g(APS) = 0`). Corrected in the leg-2
  docstring; both value packages recorded here.
- **Firewall (DEAD-ENDS.md) clean, independently audited:** inputs are {6 fixed points (Nikulin),
  symplectic weights, `sigma = -16`, standard Hodge/Betti data, |G| = 3}. No `chi(K3) = 24` input
  (it appears only as a closure TARGET in the quotient-resolution gate), no `/8` manufacture, no
  `A-hat = 3`, no contractible-fiber move. The `3 | 42` mechanism is honest index arithmetic.

## Honest limits (stated, not resolved)

1. **Operator identity (the load-bearing caveat).** The object computed is the ghost-subtracted
   complex: `eta(D tensor T_C) - eta(D)`. **CORRECTION 2026-07-10 (one sentence REFUTED by the -38
   adjudication, `canon/gamma-traceless-38-adjudication-RESULTS.md`):** this item originally said
   "the index and the mod-Z class are stable under the gamma-traceless repackaging." That is FALSE
   as written: the honest geometric gamma-traceless operator is a DIFFERENT published K-class, not a
   repackaging -- its index is `-38 = 19 sigma/8` (Homma-Semmelmann Prop 3.1(i), fetched verbatim)
   and its order-3 rho classes are `(0,2,1)/3` NONZERO. APS-III deformation invariance is untouched;
   it simply does not apply across distinct K-classes. The 2-primary verdict of this file is true
   of, and only of, the ghost-subtracted carrier (`-42 = 21 sigma/8`). The GU source-action operator
   remains UNBUILT (SG4 MISSING-CARRIER); the A/B benchmark fork is ghost-subtract => zero order-3; geometric-complete =>
   nonzero order-3. Native Krein grading and source transfer remain open, outside this binary.
2. **The -38 thread -- ADJUDICATED 2026-07-10.** The fourth convention is not a convention: it is
   the honest geometric gamma-traceless operator (elliptic, published: Homma-Semmelmann / Baer-
   Mazzeo), with `ind Q = -38 = 19 sigma/8` by two independent routes (in-house exact symbol
   block-diagonalization homotopy certificate + published HS eq (11) additivity), equivariant
   multiplier `-1` (not 0 mod 3), and Nikulin rho classes `(0,2,1)/3` NONZERO. Both carriers now
   pass a distinct established published gate (`21 sigma/8` AGW physics vs `19 sigma/8` HS
   mathematics), so the "uniquely selected by the established gate" freeze rationale of item 3 below
   is DEAD; selection authority moved to SG4 (which object the unbuilt GU source action names). Full
   record: `canon/gamma-traceless-38-adjudication-RESULTS.md`,
   `tests/rs-function-space/rho-38-adjudication/`.
3. **Convention freeze requirement.** The entire RS verdict rides the pinned subtraction. The pin is
   operational (canon `-42 = 21 sigma/8` = AGW/Christensen-Duff gravitino density), internally
   coherent, and enforced by a non-equivariant gate in every script -- but it is a program pin, not
   a theorem about "the" RS operator.

## Canon consequences (executed in this commit, correction-note discipline)

- `families-e-invariant-order3-monodromy-RESULTS.md`: (i) lattice ranks corrected `(14,8) -> (10,12)`
  (the original line carried the ORDER-2 Nikulin data; caught by the Lefschetz gate; not load-bearing
  for that file's own verdict); (ii) the BLOCKED_NEEDS_SPEC row annotated: the geometric benchmark IS
  computable and is now computed ("not computable from existing data" was over-conservative); the GU
  caveat stays open.

## What this changes (and what it does not)

- The A comparator has zero order-3 rho; B and Dirac have located nonzero classes.
- None of these computations forces an integer family count. The broader
  located-not-forced conclusion is distinct from universal rho vanishing.
- Source-native Krein grading, the observation map and integer-count transfer
  remain open. Defined benchmark computations do not wait for a source-action build.
- No source/ledger verdict, generation-count credit or public-posture change.
