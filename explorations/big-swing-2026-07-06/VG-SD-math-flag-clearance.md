---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing VG-SD (source route, supports V3/V5): five from-memory mathematical flags in the federation docs are now CHECKED MATHEMATICS -- (1) orthogonal J on R^(p,q) iff p,q both even: literature located (Davidov-Mushkarov arXiv:math/0607030 Sec.2, J(W) = O(2p,2q)/U(p,q)) + two-line proof + machine mechanism check (complex signature (3,2) doubles to (6,4); (7,3) scan floor 4.000000 matches V3's independent 40-start floor); (2) positive lines in C^(3,2) retract to CP^2: Wolf-1969 base-cycle + Mostow-fibration lineage located + Mostow dimension bookkeeping measured (24/16/12/8 -> orbit dims 8 and 4); (3) c(T CP^n) = (1+h)^(n+1): Hartshorne II.8.13 located, symbolic check with failing control; (4) su(2,2) = so(4,2): Spin+(2,4) = SU(2,2) located (Wikipedia exceptional isomorphisms) AND the explicit isomorphism CONSTRUCTED on Lambda^2 C^4 (real structure S Sbar = +I/6, Q|V_R signature (4,2), rank 15, bracket residual 1e-16; su(3,1) control comes out QUATERNIONIC, S Sbar = -I/6); (5) Cartan involution existence/uniqueness/B_theta-positivity/maximal-compact: Knapp PSPM 61 Thm 4.2 + Corollary (a)(b) = [K3 Thm 6.16, Sec VI.2] + [K3 Thm 6.31], quotes extracted from the PDF, verified numerically on su(2,2) with a failing non-Cartan control. HONEST OUTCOME: all five SETTLED; one small CORRECTION to the persona doc (the compatible-J family is O(6,4)/U(3,2) with FOUR components; SO(6,4)/U(3,2) is only its two orientation-compatible components); remaining unverified residue is named (Mostow 1955 theorem number, so*(6) = su(3,1) label, Milnor-Stasheff theorem number)."
grade: "exploration / all five items SETTLED (literature reference located AND mechanism machine-verified with failing controls); overall THEOREM-grade for the five mathematical statements themselves; the route makes NO physics claim. Source route: does not touch the 1792-dim carrier, so carrier anchors are not reproduced here (owned by vg_v1/vg_v3/vg_v5). Target-import guard at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, or divided by -- every printed 3 below is a measured eigenvalue count (complex signature (3,2)) or the binomial coefficient forced by the n+1 = 3 summands of the CP^2 Euler sequence."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - explorations/big-swing-2026-07-06/VG-V3-j-commutant-conformal-native.md
  - explorations/big-swing-2026-07-06/VG-V5-breaking-coset-topology.md
  - canon/h2-base-index-chirality.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
scripts:
  - tests/big-swing/vg_sd_math_flag_clearance.py
---

# VG-SD: mathematical flag clearance — five from-memory claims converted to checked mathematics

**Route class:** source intake (web) + first-principles argument + machine verification. Supports
V3 (J-commutant / even-parity theorem) and V5 (coset topology). This route makes **no physics
claim** and touches **no carrier**: the Cl(9,5) anchors (triplet (+96,−96,0), beta_S residual,
rank(Gamma) = 128 / ker = 1664) are owned and reproduced by the carrier routes (vg_v1, vg_v3,
vg_v5), not here. A separate big-swing workflow (R1 PT-vs-ghost-parity, R2 chirality wall, R3
PT-phase of GU cores, R4 conformal fiber obstruction) is running; its outcomes are neither cited
nor used — gates only.

**Script:** `python tests/big-swing/vg_sd_math_flag_clearance.py` → exit 0, 30 checks PASS,
including five controls that show the checks can fail. Every number cited below is printed by it.

**The five flags** (locations in the federation docs):

| # | Claim | Where flagged from-memory |
|---|-------|---------------------------|
| 1 | orthogonal complex structure on R^{p,q} iff p, q both even | persona doc §3.2 line 125; V3 cleared the proof, reference was still missing |
| 2 | positive-line domain in C^{p,q} deformation-retracts to CP^{p-1} | persona doc §3.2 line 138 ("from memory"); V5 built the retraction, lineage was still missing |
| 3 | c(T CP^n) = (1+h)^{n+1}, hence c1 = (n+1)h, chi = n+1 | persona doc line 141 ("flagged numerology until derived"); V5 derived it, citation was still missing |
| 4 | su(2,2) = so(4,2) (exceptional isomorphism) | persona doc line 118 ("theorem" asserted from memory); V3 line 128 ("the abstract iso ... is standard — from memory") |
| 5 | Cartan involution basics (existence, uniqueness up to conjugation, B_theta > 0, even part = maximal compact) | underwrites every "maximal compact of the chain" statement in persona §3.2 (Pati-Salam / SM punchlines) |

---

## 1. Orthogonal complex structures on R^{p,q} exist iff p, q both even — SETTLED

**Literature (located, exact quote).** Davidov–Mushkarov, *Twistorial construction of generalized
Kähler manifolds*, arXiv:math/0607030, Section 2:

> "Suppose that dim W = 2m and g is of signature (2p, 2q), p + q = m. Denote by J(W) the set of
> all complex structures on W compatible with the metric g. The group O(g) of orthogonal
> transformations of W acts transitively on J(W) by conjugation and J(W) can be identified with
> the homogeneous space O(2p, 2q)/U(p, q). In particular, dim J(W) = m² − m. The group
> O(2p, 2q) has four connected components, while U(p, q) is connected, therefore J(W) has four
> components."

This is the standard pseudo-Kähler statement: compatible complex structures exist precisely on
even-even signatures and form the homogeneous family O(2p,2q)/U(p,q). The quote carries the
existence direction and the family structure; the necessity direction ("only if") is the two-line
proof below (also proved and constructively verified in VG-V3, whose flag this clears).

**Two-line proof (necessity).** If J is g-orthogonal (JᵀgJ = g) and J² = −I, then
h(x,y) := g(x,y) + i·g(x,Jy) is a Hermitian form on the complex vector space (V,J) with
g = Re h. Diagonalizing h over C with complex signature (r,s) gives real signature
(2r, 2s) — J pairs eigen-directions within each definiteness class, so both parts are even. ∎

**Machine check (mechanism, not just endpoint).** On R^{6,4}: exact block J (residuals 0.0e+00);
a generic O(6,4)-conjugate J (residuals 1.2e−15 / 1.4e−15); the Hermitian form h built from that
generic J is Hermitian to 1.3e−15 and has **measured complex signature (3,2)** — doubling to
(6,4) exactly as the proof mechanism says. Obstruction side: minimizing
‖J²+I‖² + ‖JᵀgJ−g‖² over all real 10×10 matrices reaches **6.1e−14 on (6,4)** and floors at
**4.000000 on (7,3)** (15 L-BFGS starts) — independently matching VG-V3's 40-start floor 4.000.

**Correction to the persona doc (small, checked).** Persona §3.2 line 128 says "compatible J's
form the family SO(6,4)/U(3,2)". Per the located reference, the full family is
**O(6,4)/U(3,2) with four components**; SO(6,4)/U(3,2) is the union of only the **two**
orientation-compatible components (the paper: "The set J±(W) has the homogeneous representation
SO(2p,2q)/U(p,q) and, thus, is the union of two components of J(W)"). Nothing downstream leaned
on the component count, but the family name should be O/U, or SO/U with an orientation fixed.

## 2. Positive lines in C^{p,q} deformation-retract to CP^{p-1} — SETTLED

**Literature lineage (located).** This is the flag-domain base-cycle picture:

- **Wolf**, *The action of a real semisimple group on a complex flag manifold, I*, Bull. AMS
  75(6), 1969, 1121–1237: a real form G0 has finitely many orbits on a complex flag manifold,
  hence open orbits (flag domains); **every open G0-orbit contains a unique orbit of a maximal
  compact subgroup K0 that is a complex submanifold** — the base cycle. (Statement as quoted in
  the Fels–Huckleberry–Wolf lineage below.)
- **Fels–Huckleberry–Wolf**, *Cycle Spaces of Flag Domains: A Complex Geometric Viewpoint*,
  Birkhäuser 2006 (survey arXiv:math/0210445); Hong–Huckleberry, *Normal bundles of cycles in
  flag domains* (arXiv:1807.07311): "Every open G0-orbit D contains a unique orbit C0 of a
  maximal compact subgroup K0, which is a complex submanifold."
- **Mostow**, *On covariant fiberings of Klein spaces*, Amer. J. Math. 77 (1955): the Mostow
  fibration — G0/L0 is K0-equivariantly a bundle over K0/(K0∩L0) with contractible (Euclidean)
  fiber when K0∩L0 is maximal compact in L0, hence deformation-retracts onto the K0-orbit.
  (Paper identity verified against the flag-domain literature that uses it by name; the exact
  theorem number inside the 1955 paper is **not** verified — honest caveat below.)
- Contextual lineage: these domains are the open-orbit setting of Griffiths–Schmid, *Locally
  homogeneous complex manifolds*, Acta Math. 123 (1969) (lineage-level citation; not fetched).

For D = {positive lines in C^{p,q}}: G0 = SU(p,q), the stabilizer of a positive line is
L0 = S(U(1)×U(p−1,q)) (reductive — the line is definite, so no unipotent radical), K0 = S(U(p)×U(q)),
K0∩L0 = S(U(1)×U(p−1)×U(q)) is maximal compact in L0, and the base cycle is
K0·[e1] = P(C^p) = **CP^{p-1}**. Mostow then gives the deformation retraction D → CP^{p-1}.

**Machine check (all dims measured as nullspace dimensions, C^{3,2} case).**
dim su(3,2) = **24** (defining residual 1.1e−15); stabilizer of [e1] = **16**, so the orbit is
**open** (dim 8 = dim_R CP⁴); dim k0 = **12**; stabilizer in k0 = **8**, so the K0-orbit has
dim **4 = dim_R CP²**; the theta-fixed part of L0 has dim **8** — equal to k0 ∩ l0, confirming
the Mostow hypothesis (K0∩L0 maximal compact in L0). The direct retraction
r_t(v) = (v₊, (1−t)v₋) (VG-V5's construction, re-verified lighter here): over 400 random
positive lines × 21 t-steps, min ⟨r_t v, r_t v⟩ = **0.037284 > 0** (domain preserved), r_t = id
on CP² exactly, and the mirror control (retracting toward the negative block) exits the domain
in **400/400** cases — the check can fail.

## 3. c(T CP^n) = (1+h)^{n+1} via the Euler sequence — SETTLED

**Literature (located).** The Euler sequence 0 → O → O(1)^{⊕(n+1)} → T CP^n → 0 (dual form
0 → Ω¹ → O(−1)^{⊕(n+1)} → O → 0): **Hartshorne, *Algebraic Geometry*, GTM 52, Theorem II.8.13**
(citation confirmed via the Wikipedia "Euler sequence" article, which cites exactly that theorem).
The Chern-class consequence by Whitney product: c(T CP^n) = (1+h)^{n+1} mod h^{n+1} — also
standard in Milnor–Stasheff, *Characteristic Classes*, §14 (the formula is confirmed by multiple
sources; the precise theorem number 14.10 is from memory, unverified — caveat below).

**Machine check (symbolic, sympy).** For n = 1..4: c1 = (n+1)h and chi = ⟨c_n,[CP^n]⟩ = n+1,
printed: (2,2), (3,3), (4,4), (5,5). CP² specifics used by V5: ⟨c1²⟩ = **9**, ⟨c2⟩ = chi = **3**,
p1 = c1² − 2c2 = **3** = 3σ with σ(CP²) = +1 (Hirzebruch). Control: dropping the trivial summand
((1+h)² instead of (1+h)³) gives "chi(CP²)" = **1 ≠ 3** — the check can fail. Provenance of every
3 here: the binomial coefficient of a sequence with n+1 = 3 summands, n = 2 forced by the
measured Hermitian signature (3,2) of item 1 / V5 — never inserted.

## 4. su(2,2) = so(4,2) — SETTLED, and now CONSTRUCTED, not just cited

**Literature (located).** Wikipedia, *Exceptional isomorphism* (spin-group table):
**Spin⁺(2,4) ≅ SU(2,2)** (with Spin(6) ≅ SU(4), Spin⁺(3,3) ≅ SL(4,R), Spin⁺(1,5) ≅ SL(2,H) as
the neighboring A3 = D3 real forms). Group-level bookkeeping for downstream users: SU(2,2) is
the **2:1 cover of SO⁺(4,2)** with kernel {±1}; the effective conformal group of compactified
Minkowski space is SU(2,2)/Z₄ ≅ PSO⁺(4,2) (the Z₄ is the center {i^k I}). The persona doc's
"SU(2,2) = Spin(4,2)" (line 119) is **correct** at this level; loose statements in the wider
literature of the form "SO(4,2) = SU(2,2)/Z₄" refer to the projective/effective group.

**Explicit isomorphism (this route's construction — clears V3's from-memory flag).** On
Λ²C⁴ ≅ C⁶ with action ρ(X)A = XA + AXᵀ and the Λ⁴ (Levi-Civita) symmetric pairing Q:

| step | measured |
|------|----------|
| ρ is a Lie-algebra homomorphism | bracket residual 1.1e−16 |
| Q symmetric, ρ(su(2,2))-invariant | invariance residual 3.3e−15 |
| antilinear commutant {S : S ρ̄ = ρ S} | complex dimension **1** (irreducible, self-conjugate) |
| S S̄ = λI | λ = **+1/6** (residual 1.6e−16) → **REAL** structure σ, σ² = +1 |
| fixed space V_R = Fix(σ) | dim_R = **6**; ρ-invariant |
| Q restricted to V_R | real up to phase (im residual 3.6e−15), signature **(4,2)** |
| ρ|V_R | real (3.2e−15), preserves Q|V_R (1.1e−15), injective: rank **15/15** |

Injective homomorphism su(2,2) → so(4,2) between 15-dimensional algebras ⇒ **isomorphism**.
Cross-checks: Killing signature of su(2,2) = **(8,7)** (matches V3's printed (8,7); so(4,2) has
k = so(4)⊕so(2), dim 7). **Control:** the identical construction on su(3,1) returns
S S̄ = **−1/6 · I** — a **quaternionic** structure, no real 6-dim form-preserving subspace, so
su(3,1) is *not* an so(p,q) (it pairs with so*(6) — that name from memory) — the real-structure
test can fail and distinguishes real forms.

## 5. Cartan involution basics — SETTLED

**Literature (located, quotes extracted from the PDF).** Knapp, *Structure Theory of Semisimple
Lie Groups* (in Proc. Sympos. Pure Math. 61, 1997; www.math.stonybrook.edu/~aknapp/pdf-files/1-27.pdf),
Section 4, with pointers into [K3] = *Lie Groups Beyond an Introduction*:

> "An involution θ of g0 ... such that the symmetric bilinear form Bθ(X,Y) = −B(X,θY) is
> positive definite is called a Cartan involution of g0."

> "Theorem 4.2. Let θ be a Cartan involution of g0, and let σ be any involution. Then there
> exists φ in Int g0 such that φθφ⁻¹ commutes with σ. Reference. [K3, Theorem 6.16].
> Corollary. (a) g0 has a Cartan involution. (b) Any two Cartan involutions of g0 are conjugate
> via Int g0." — **existence + uniqueness up to (inner) conjugation.**

> "Theorem 4.3. ... (b) the subgroup of G fixed by Θ is K ... (c) the mapping K × p0 → G given
> by (k,X) → k exp X is a diffeomorphism onto ... (g) when Z is finite, K is a maximal compact
> subgroup of G. Reference. [K3, Theorem 6.31]." — **even part = maximal compact** (with the
> honest finite-center hypothesis attached, which the docs' matrix groups satisfy).

Also extracted: B is negative on k0, positive on p0, B(k0,p0) = 0 — the decomposition facts the
federation docs use when reading off maximal compacts of the chain (S(U(3)×U(2)) for SU(3,2),
(Spin(6)×Spin(4))/Z₂ for Spin(6,4)).

**Machine check on su(2,2).** θ(X) = −X†: involution (θ²−id residual 1.0e−15), automorphism
(residual 0.0e+00); B_θ = −B(X,θY) has **min eigenvalue 8.000000 > 0** — positive definite;
k = Fix(θ) has dim **7** = dim s(u(2)⊕u(2)) with B|k max eigenvalue **−8.000000 < 0** (compact).
**Control:** σ = Ad(diag(1,−1,1,1)) is an involutive automorphism but B_σ has min eigenvalue
**−8.0 < 0** — not Cartan; the positivity check can fail.

---

## Verdict table

| # | Item | Reference status | Mechanism status | Grade |
|---|------|------------------|------------------|-------|
| 1 | even-even theorem | located, quoted (O(2p,2q)/U(p,q)) | proof + verified, floors 6e−14 vs 4.000 | **SETTLED** |
| 2 | positive-line retraction | lineage located (Wolf 69 / Mostow 55 / FHW 06) | explicit retraction + Mostow bookkeeping verified | **SETTLED** |
| 3 | c(T CP^n) = (1+h)^{n+1} | located (Hartshorne II.8.13) | symbolic + failing control | **SETTLED** |
| 4 | su(2,2) = so(4,2) | located (Spin⁺(2,4) ≅ SU(2,2)) | **explicit iso constructed**; quaternionic control | **SETTLED** |
| 5 | Cartan involution basics | located, quoted (Knapp PSPM 61 / K3 6.16, VI.2, 6.31) | verified on su(2,2) + failing control | **SETTLED** |

**Corrections fed back to the federation docs:** one — persona §3.2's "family SO(6,4)/U(3,2)"
should read O(6,4)/U(3,2) (four components; SO/U is its two orientation-compatible components).
No claim was overturned: all five from-memory statements were **true as stated**.

**Honest residue (still unverified):** (i) the exact theorem number inside Mostow 1955 (paper
identity and downstream usage verified, internal numbering not); (ii) "Milnor–Stasheff Theorem
14.10" as the precise locator for item 3 (the formula itself is multiply confirmed; Hartshorne
II.8.13 is the verified citation); (iii) the label so*(6) ≅ su(3,1) for the quaternionic control
(the measured content — S S̄ = −I/6, hence not so(p,q) — does not depend on the name);
(iv) Griffiths–Schmid 1969 cited as lineage only, not fetched. None of these carries any load in
V3/V5: the load-bearing statements are items 1–5 themselves, now referenced and machine-verified.

**What this buys the federation:** V3's even-parity theorem and su(2,2)~so(4,2) chain, and V5's
D ≃ CP² retraction and c1 = 3h derivation, no longer rest on any from-memory mathematics. The
"conformal is what survives at the vacuum" geometric chain (persona §3.2) is now fully referenced
mathematics at every link that was flagged; whether it is GU-*native* remains exactly where V3
left it (refuted at the fiber level — the chain requires breaking GU's trace split and isotropy).
