---
title: "Hardening prompts for deep research (generation-sector / firewall result)"
status: tooling
doc_type: prompt_set
created: 2026-06-28
note: "Each prompt = the SHARED BACKGROUND block + the specific ask. Paste the background, then the ask. The three CRITICAL prompts are 1, 2, 6."
---

# Hardening prompts for deep research

Eight deep-research prompts to harden the result, ordered by leverage. Each is meant to be run independently:
paste the **SHARED BACKGROUND** block below, then the specific **PROMPT** ask. Prompts **1, 2, and 6** are
the critical three (the others harden positioning and the reconstruction bridge).

---

## SHARED BACKGROUND (prepend this to any prompt below)

```
I have a research result I want to harden. Work from first principles, attack my framing where it is weak,
and grade everything honestly (theorem / standard-result-applied / reconstruction-dependent / speculative).

Setting: a machine-checked reconstruction of the matter sector of Geometric Unity (GU, Eric Weinstein)
realizes its Rarita-Schwinger (spin-3/2) sector as a real Clifford algebra Cl(p,q), p+q=14, on a 128-dim
spinor module; one Standard-Model generation is the 16 of Spin(10). Established facts:

- The generation sits in a self-dual su(2)_+ TRIPLET: the rank-3 bundle Lambda^2_+ of self-dual 2-forms of
  the 4-dimensional spacetime base X^4, which generates su(2)_+, one factor of so(4) = su(2)_+ (+) su(2)_-,
  the SO(4) frame rotations of X^4 (Spin(4) = SU(2)_+ x SU(2)_-).
- The triplet is VECTORLIKE: the natural so(p,q)-invariant inner product is indefinite (a Krein form),
  purely cross-chirality, so every positive-norm subspace is 50/50 left/right, net chirality 0.
- Every internal obstruction is 2-PRIMARY (a power-of-2 / mod-2^k statement): the quaternionic Kramers wall
  J^2 = -1; Rokhlin's theorem sign(X) = 0 mod 16; real/pseudoreal representations give an even/mod-2 index;
  the adjoint Dirac index 2T(adj)k = 4k; the (+96,-96) cross-chirality Krein signature; a spinor
  2-smoothness lemma (spinor-family multiplicities are powers of two). So the internal "no-go" (no net
  chiral count) is structurally a 2-primary statement, and is provably blind to odd torsion (3 coprime to 2).
- pi_3^s (third stable homotopy group of spheres) = Z/24 = Z/8 (+) Z/3; the J-homomorphism gives
  |Im J_3| = denominator of B_2/4 = 24 (Adams); the 3-primary part is Z/3. The Adams e-invariant (the
  homotopy avatar of the APS eta/rho invariant) detects it.
- GU's 14-dim observerse Y^14 has a non-compact end whose link is the lens space RP^3 = S^3/Z_2 = L(2;1),
  carrying a charge-1 self-dual su(2)_+ twist. A careful computation (three independent derivations) found:
  the boundary e-invariant of this twist has a nonzero 3-primary part IFF Lambda^2_+ enters as a TANGENTIAL
  framing (part of the SO(4) frame/spin structure, feeding the gravitational framing channel -p_1/24, whose
  denominator 24 carries the von Staudt-Clausen 3), giving e_R = 1/12 (class 2 in Z/24, 3-primary part order
  3, nonzero). If instead it enters as a gauge coefficient, the boundary reduced eta = +/-3/8 (3-primary
  part 0). Three independent first-principles analyses (one citing the GU draft directly) resolved the fork
  TANGENTIAL at reconstruction grade.
- Current claim: GU, read tangentially, forces generation count 3 at the boundary via Adams' theorem, in
  exactly the sector the 2-primary no-go is structurally blind to. This is RECONSTRUCTION-GRADE, not a
  theorem of the published GU draft (the explicit matter action is unbuilt; Timothy Nguyen's complexification
  critique of GU stands).
```

---

## PROMPT 1 (CRITICAL) -- the identification: does a boundary e-invariant equal the generation count?

```
THE QUESTION. Is there an established mechanism by which a boundary e-invariant (reduced APS eta / Adams
e-invariant) of a spin manifold-with-boundary EQUALS the net chiral fermion (generation) count, modulo the
bulk? Specifically: on the non-compact observerse Y^14 (a manifold with the RP^3 end), does the
Atiyah-Patodi-Singer index theorem give

    net chiral generation count = (bulk Atiyah-Singer integral) - (boundary reduced eta),

so that the bulk carries the 2-primary (even) part and the boundary eta carries the odd-primary part of the
count? Survey the literature that would establish or refute this: Atiyah-Patodi-Singer I/II/III (the eta
boundary term); Callan-Harvey anomaly inflow (chiral fermions localized at a boundary/defect counted by
inflow); the eta-invariant as a boundary fermion number / global anomaly (Witten, and the recent
Dai-Freed / cobordism-anomaly literature); the Bismut-Cheeger families eta. Determine: under what
hypotheses is "the boundary e-invariant equals the net chiral count modulo the even bulk" a standard,
correct statement, and does its 3-primary part genuinely equal the net count's 3-primary part?

DELIVERABLE. Whether the identification holds rigorously and under exactly what hypotheses; whether the
chain "there is a 3-primary boundary invariant => the net generation count is 3" is sound, or whether the
honest statement is weaker ("there is a 3 in the topology, not necessarily the generation number"); the
precise mechanism if it holds, and the precise gap if it does not. This is the single most load-bearing
question between "the generation count is 3" and a footnote; do not be charitable, attack it.
```

---

## PROMPT 2 (CRITICAL) -- the tangential branch, derived rigorously

```
THE QUESTION. Independently derive (or find a published reference for) the Adams e-invariant / reduced
framing defect of RP^3 = L(2;1) carrying the framing induced by the self-dual SU(2)_+ = Lambda^2_+
structure at charge 1, treated as a TANGENTIAL framing (a modification of the SO(4) frame / spin structure),
NOT as a gauge-coefficient bundle. Confirm or correct e_R = +/- 1/12 (class 2 in Z/24). The claimed chain:
the adjoint of a charge-1 SU(2) bundle has p_1(ad) = -4 c_2 = -4, so |p_1/2| = 2 (the STABLE framing degree
the J-homomorphism sees -- since SU(2) = Spin(3) -> SO(3) is an iso on pi_3 but SO(3) -> SO stabilizes by
x2 -- NOT the Dynkin index 4); Adams' e(generator) = 1/24; so e_R = 2/24 = 1/12, and the von Staudt-Clausen
3 in the denominator 24 survives, giving a nonzero 3-primary part. Contrast carefully with the GAUGE-
coefficient computation via Gilkey's lens-space eta formula, which gives reduced eta = +/-3/8 (Tr Ad(-1) = 3
because the SU(2) center acts trivially in the adjoint; 3-primary part 0).

DELIVERABLE. An independent rigorous derivation of the tangential-branch e-invariant (the leg that LANDS
the result), confirming or correcting 1/12 and its 3-primary part; any published reference computing the
e-invariant of a self-dual-framed RP^3 or the equivalent framed-bordism class; and an honest statement of
which steps are standard versus reconstructed. The tangential branch delivers the conclusion, so it must be
airtight; the gauge branch (3/8) is already cleanly settled by Gilkey, so focus the rigor on the tangential
branch and on whether the framing defect honestly carries the von Staudt-Clausen 3 to the boundary.
```

---

## PROMPT 3 -- audit that every obstruction is genuinely 2-primary

```
THE QUESTION. Audit, rigorously, whether EVERY obstruction in the generation-sector no-go is genuinely
2-primary (a power of two, a multiple of a power of two, or a statement modulo 2^k) with NO hidden odd-prime
(3, 5, ...) content. Check one by one: (i) the quaternionic Kramers wall J^2 = -1 (a Z/2 statement); (ii)
Rokhlin's theorem sign(X) = 0 mod 16; (iii) "a real or pseudoreal representation gives a non-chiral / even
(mod-2) index"; (iv) the adjoint Dirac index 2T(adj)k = 4k and the full-bundle indices 12k, 24k; (v) the
cross-chirality Krein signature (+96, -96); (vi) the spinor 2-smoothness lemma (spinor-family multiplicities
are powers of two). For each, confirm it is 2-primary or expose any odd-torsion content. Also check whether
any two obstructions COMBINE to produce odd content.

DELIVERABLE. A per-item verdict confirming the meta-lemma "every obstruction is 2-primary" without
exception, or identifying any exception (which would weaken the central claim that the no-go is structurally
blind to the 3-primary generation count). This lemma is the GU-independent spine of the result, so it must
hold without exception.
```

---

## PROMPT 4 -- is the link of GU's non-compact end actually RP^3?

```
THE QUESTION. In Geometric Unity, what is the link of the non-compact end of the observerse Y^14 = Met(X^4)
(the bundle of metrics over the 4-base), or whichever end carries the matter boundary data? Is it the lens
space RP^3 = S^3/Z_2 = L(2;1)? GU's signature is p - q = 4, which points at the metric-fiber homogeneous
space GL(4,R)/O(3,1), whose maximal-compact / link structure is the relevant geometry. Confirm or correct:
(a) is the relevant boundary link RP^3 = L(2;1), or a different lens space / manifold; (b) is the charge-1
self-dual SU(2)_+ twist the canonical boundary data. This matters because the boundary e-invariant is highly
sensitive to the manifold: L(2;1) gives a 2-primary +/-1/8 bare value, but L(3;1) gives -1/3 (3-divisible),
so a different end could change the 3-primary conclusion entirely.

DELIVERABLE. The best available identification of the geometry of GU's non-compact end and its link, with an
honest grade (theorem of the draft / reconstruction / open), and an explicit statement of how the result
would change if the link is NOT RP^3.
```

---

## PROMPT 5 -- explicit GU text on the matter-Lambda^2_+ coupling

```
THE QUESTION. In the Geometric Unity April 2021 draft (and any community reconstructions), is there explicit
text pinning HOW the matter Dirac / Rarita-Schwinger operator couples to the self-dual two-forms Lambda^2_+
of the 4-base: as a TANGENTIAL framing (the Levi-Civita spin connection acting on the Rarita-Schwinger
1-form / vector index) or as a GAUGE COEFFICIENT (an independent internal bundle twisting the matter
operator)? Known anchors: GU introduces the fermion zeta as a spinor-valued 1-form (zeta in Omega^1(Y, S)),
with the horizontal piece U the spacetime tangent directions and the vertical piece V the normal bundle
N_gamma; it locates the Standard-Model / Pati-Salam gauge groups in reductions of the vertical 10-sector
(Spin(6,4) -> Spin(6) x Spin(4)), keeping the horizontal Spin(1,3) distinct. Three independent analyses
inferred TANGENTIAL from this, but it is reconstruction-grade.

DELIVERABLE. The most explicit statement available in GU's own writing (or a credible community
reconstruction) on the matter-Lambda^2_+ coupling; whether it upgrades "tangential" from reconstruction-
grade-favored toward established; and an honest grade. If the published draft genuinely does not pin the
coupling, say so plainly.
```

---

## PROMPT 6 (CRITICAL) -- novelty / prior art

```
THE QUESTION. Has anyone connected the NUMBER OF STANDARD-MODEL FERMION GENERATIONS to the third stable
homotopy group of spheres pi_3^s = Z/24, to the J-homomorphism, to the Adams e-invariant, or to a 2-primary
versus 3-primary (Z/8 vs Z/3) decomposition of a topological invariant? Has anyone framed a generation /
chirality no-go as a 2-primary (mod-2) statement that is structurally blind to a 3-primary count? Separately
and importantly, DISAMBIGUATE from the large and growing literature where the integer 24 appears in flavor /
generation models -- modular flavor symmetry (Gamma-modular forms and their levels), the 24 in K3 / string
compactifications, the bosonic-string transverse 24 -- and determine whether any of it actually uses the
homotopy / e-invariant / 2-vs-3-primary mechanism we use, or whether those 24s coincide numerically but
differ mechanistically.

DELIVERABLE. The closest prior art (if any), with citations; an honest assessment of whether the reframe
"the generation no-go is 2-primary and the count is a 3-primary boundary e-invariant" is genuinely new; and,
if there is overlap, exactly where, so it can be cited and disambiguated. Novelty is the entire value
proposition for publication; be thorough and do not flatter the result.
```

---

## PROMPT 7 -- precedent for "number of generations as a topological invariant"

```
THE QUESTION. Survey the precedent for the NUMBER OF FERMION GENERATIONS being a TOPOLOGICAL / INDEX
invariant rather than a free parameter. Cover: the Atiyah-Singer index theorem counting net generations in
Calabi-Yau / heterotic string compactifications (the (1/2)|chi(CY)| and Hodge-number (h^{2,1}, h^{1,1})
generation formulas); chi(K3) = 24 and chi/24-type relations; anomaly inflow counting chiral fermions
localized at boundaries / defects; intersecting-brane and F-theory generation counts as intersection
numbers; and any explicit "three generations from topology" constructions and their successes / failures.
Then position our claim (generation count = the 3-primary part of a boundary e-invariant on RP^3, forced by
Adams' theorem) relative to this landscape: is it a member of this tradition, a novel variant, or
orthogonal?

DELIVERABLE. The precedent landscape with citations; the closest analogues to our boundary-e-invariant
mechanism; and an honest assessment of whether "generations as a topological invariant" legitimizes our
claim (places it in a respectable tradition) or whether ours is unusual and needs extra defense.
```

---

## PROMPT 8 -- is the Distler-Garibaldi scope-exit airtight?

```
THE QUESTION. Is Geometric Unity's exit from the Distler-Garibaldi no-go ("There is no Theory of Everything
inside E8", Comm. Math. Phys. 298 (2010) 419) airtight? GU's claimed scope-exit: its gauge group is Sp(64)
(or the Spin(7,7)-derived structure), not a real form of E8; the 4d Lorentz group does not embed inside the
internal gauge factor; chirality is realized as an OPERATOR INDEX (the index of a Clifford-module Dirac
operator), not as the complexity / reality type of a representation V_{2,1}; and the matter is geometric
bundle data on the non-compact Y^14 = Met(X^4). Distler-Garibaldi assume a single finite-dimensional real
form of E8 with an SL(2,C) x G centralizer and V_{2,1} a complex G-representation. Determine: is GU genuinely
OUTSIDE the Distler-Garibaldi hypothesis class (so the theorem is inapplicable, not violated), and is that
scope-exit complete and correct? What do Jacques Distler, Skip Garibaldi, Timothy Nguyen, and the broader
GU-critique community say about whether GU evades or falls to Distler-Garibaldi?

DELIVERABLE. Whether the scope-exit is airtight (with any holes named); the precise Distler-Garibaldi
assumptions GU violates and whether violating them genuinely removes GU from the theorem's scope (versus
merely contradicting it within scope); and the documented community view. Distler-Garibaldi is the
stress-case no-go a referee will invoke first, so this must be solid.
```
