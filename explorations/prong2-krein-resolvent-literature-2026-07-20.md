---
title: "Prong-2 literature scout: does established functional-analysis machinery give (or precisely defeat) the product-uniform norm-resolvent boundary-value theorem for the Krein-self-adjoint, type-changing boundary Dirac family? Single best fit = the Krein-space positive-commutator (Mourre) LAP of Georgescu-Gerard-Hafner; the wall is a Krein critical point whose regular-vs-singular status is the one missing ingredient; the PRODUCT-uniformity clause is genuinely novel (no off-the-shelf precedent)"
status: active_research
doc_type: literature_scout
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (Prong 2: Krein-resolvent literature scout)"
inputs:
  - explorations/sector-relative-section-theory-2026-07-20.md
  - explorations/operator-grade-end-2026-07-20.md
  - explorations/n2-end-family-2026-07-20.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# The theorem, as the receipts state it

Object (operator-grade doc, Section 0/2; section-theory doc, Section 7.1):

    N_delta,op = M_op (q_op + i delta)^{-1/2},   M_op = Ku_op D_op

on a discretized non-compact collar. Standing facts from the receipts:

- **Krein-self-adjoint, not Hilbert-self-adjoint.** K_op D_op K_op =
  D_op^dag machine-exact at every resolution; K_S is indefinite
  (signature (64,64)). GEOMETER-VS-PHYSICS-OBJECTS.md: the operator is
  Krein-native; positive-Hilbert machinery must never be assumed.
- **Symbol changes Krein type across a wall.** q_op = P - T runs
  positive (gapped) -> 0 (wall, Jordan nilpotent, M^2 = 0) -> negative
  (cone-crossing, K-null halves). The wall is where the spectral
  datum changes adjoint type (self-adjoint cut -> skew polarization).
- **What is proven (A3):** norm-resolvent mode at z = 2i is delta-Cauchy
  per resolution (rate ~ delta^1.0); sup-norm DIVERGES at the wall
  (ceiling ~ N^1.35); deck-oddness EXACT by pointwise algebra.
- **What is OPEN (the target theorem):** the bound UNIFORM across the
  discretization parameter N and across finite PRODUCTS of the carrier,
  on a z-REGION (not one point z = 2i), with deck-odd limit.

The scout question: does any established framework deliver that uniform
bound (naming its hypotheses), or does the type-change violate a named
hypothesis of each? Every row below is web-sourced; URLs in Section R.

# Section 1. Framework fit table (typed rows, cited)

| # | Framework | Type | One-line verdict |
|---|---|---|---|
| 1 | Definitizable / locally-definitizable operators (Langer, Jonas) | PARTIAL / DEFEATED-AT-WALL | Gives bounded resolvent + spectral function AWAY from critical points; the wall IS a critical point; bound survives iff the critical point is REGULAR, blows up iff SINGULAR. |
| 2 | Krein-space positive-commutator (Mourre) LAP (Georgescu-Gerard-Hafner) | PARTIAL / SINGLE BEST | Weighted resolvent boundary value on a strip, hypotheses explicit; the load-bearing hypothesis (Krein-positive spectral projection on I) is exactly what the wall violates. Delivers the bound on definite-type z-regions. |
| 3 | Klein-Gordon in Krein / definitizable (Langer-Najman-Tretter, Jonas) | PARTIAL (physical instance) | A worked type-change Krein operator: resolvent controlled off a finite critical set. Confirms the shape is handled WHEN definitizable; GU's genuine symbol type-change is not a bounded perturbation of a positive operator. |
| 4 | Boundary triples / Weyl function, indefinite (Derkach-Malamud) | PARTIAL / LOCATOR | Krein resolvent formula converts the bound to invertibility/boundary-values of the Weyl function M(z); does NOT itself supply N- or product-uniformity; type-change = M(z) losing its definite Nevanlinna sign. |
| 5 | Pseudospectra / non-self-adjoint (Trefethen-Embree, Davies, semiclassical) | PARTIAL / DIAGNOSTIC | On the crossed sector M is effectively non-self-adjoint (skew involution); resolvent uniformly bounded OUTSIDE the pseudospectrum, unbounded INSIDE. Gives the z-region; no positive uniform theorem across the wall; pseudospectra behave badly under products. |
| 6 | Parameter-elliptic / Agmon / Boutet de Monvel collar estimates | DEFEATED-BY-TYPE-CHANGE | Parameter-ellipticity gives delta- and often N-uniform resolvent bounds when principal-symbol - z is invertible in a sector; q_op -> 0 at the wall kills invertibility of the leading symbol -> Agmon ray-of-minimal-growth / ellipticity-with-parameter FAILS exactly at the wall. |
| 7 | Norm-resolvent convergence of discretized Dirac (Cornean-Garde-Jensen; Behrndt et al.) | PARTIAL / N-UNIFORMITY | Shows N-uniform norm-resolvent convergence is NOT automatic (fails naive differences dim>=2; needs mass-term fix). The A3 N-uniformity gap is a KNOWN-HARD point, not a routine corollary; existing mesh-uniform machinery assumes a fixed gapped self-adjoint limit. |
| 8 | Melrose-Piazza spectral sections / APS families (eta-form product formula) | IRRELEVANT-FOR-BOUND / DEFEATED | Delivers index-level and eta-form PRODUCT formulas, but requires compact resolvent / gap-uniform boundary family, which the GU end explicitly refuses (n2). Classifies, does not bound; product formula is eta-form, not resolvent-norm. |

# Section 2. Row-by-row, with the exact hypothesis at stake

## 1. Definitizable / locally-definitizable (Langer 1965; Jonas)

An operator A on a Krein space is *definitizable* if it has non-empty
resolvent set and p(A) >= 0 (Krein sense) for some real polynomial p;
its spectral function then has FINITELY MANY critical points, and
outside a neighbourhood of them A behaves spectrally like a Hilbert
self-adjoint operator. The distinguishing feature of the theory is
precisely those critical points; a critical point is *regular* if the
spectral function stays bounded near it, *singular* if it blows up
(Langer, "Spectral functions of definitizable operators"; Curgus-
Gheondea on singular critical points). The key resolvent estimate is
due to P. Jonas.

Mapping to GU: a *spectral point of positive/negative type* is defined
by approximative eigensequences; the points that are of NEITHER type
are the critical points, and for an unbounded operator infinity is
generically a singular critical point (locally-definitizable survey).
The GU **wall** — where the K_S-form of the spectral halves goes null
and M becomes a Jordan nilpotent — is exactly a spectral point where
the Krein type CHANGES, i.e. a critical point. Verdict:

- **APPLIES away from the wall**: on the gapped sub-end (P > 0) the
  spectrum is of definite Krein type, the resolvent boundary value is
  bounded, and N-uniformity is inherited from the definite-type
  functional calculus.
- **DEFEATED-AT-WALL unless regular**: the bound survives across the
  wall iff the wall is a REGULAR critical point (spectral function
  bounded there). The sup-norm ~N^1.35 divergence in the receipts is
  the signature of a SINGULAR critical point in sup-norm; the delta-
  Cauchy norm-resolvent behavior is consistent with regular-in-
  resolvent. Named hypothesis at stake: **regularity of the critical
  point** (and global definitizability itself — GU's imaginary spectrum
  on the K-null timelike sector is not obviously covered by a single
  definitizing polynomial).

## 2. Krein-space positive-commutator / Mourre LAP  — the single best fit

Georgescu, Gerard, Hafner, "Boundary values of resolvents of
selfadjoint operators in Krein spaces," J. Funct. Anal. 265 (2013)
3245-3304 (arXiv:1211.0791). They prove a *limiting absorption
principle in a Krein space* by a POSITIVE COMMUTATOR (Mourre) method,
deliberately AVOIDING definitizability. The conclusion is a weighted
resolvent boundary-value bound

    || <A>^{-s} (H - z)^{-1} <A>^{-s} || < infinity,  s > 1/2,

for z in a strip I +/- i[0, nu], under three hypotheses:
1. H admits a Borel functional calculus on the interval I;
2. the spectral projection 1_I(H) is POSITIVE in the Krein sense on I;
3. a positive commutator estimate Re <u,[H,iA]u> >= c <u,u> holds on
   the range of 1_I(H), for a conjugate operator A.
The flagship application is the abstract Klein-Gordon equation in its
charge (Krein) space — a genuine indefinite-metric operator.

This is the closest existing theorem to the GU target because it is
Krein-native, gives a resolvent BOUNDARY VALUE (delta -> 0), and is
weighted (the natural home for a non-compact collar). The decisive
observation for Prong-1: **hypothesis (2) — 1_I(H) Krein-positive — is
exactly the property the wall destroys.** On the gapped sub-end 1_I is
Krein-positive and the LAP applies; across the wall the projection is
indefinite and the theorem's hypothesis fails by construction. So this
framework simultaneously (a) DELIVERS the bound on the right z-region
and (b) names precisely why the wall is excluded.

## 3. Klein-Gordon in Krein / definitizable (physical worked instance)

Langer, Najman, Tretter (Comm. Math. Phys. 267 (2006); Proc. Edinburgh
Math. Soc. 51 (2008) 711-750) and Jonas study the abstract Klein-Gordon
operator on the charge Krein space: it is DEFINITIZABLE, its spectrum
is real except for finitely many pairs lambda, lambda-bar (imaginary
frequencies = the unstable modes), and at those the resolvent has a
POLE of bounded order. This is the canonical example of a Krein-self-
adjoint operator whose spectral type changes (positive-energy vs non-
positive-energy sectors) and whose resolvent is nonetheless controlled
off a finite critical set. It is a PARTIAL fit: it certifies that
"type-changing Krein operator with a controlled resolvent" is a real,
solved shape — but the KG type-change is a bounded/relatively-compact
perturbation of a positive operator, whereas the GU symbol changes type
at the PRINCIPAL-symbol level across a wall, which definitizability of
the KG kind does not obviously reach.

## 4. Boundary triples / Weyl functions, indefinite (Derkach-Malamud)

The boundary-triple / Weyl-function machinery (Derkach-Malamud; Behrndt-
Hassi-de Snoo, "Boundary Value Problems, Weyl Functions, and Differential
Operators") gives the Krein resolvent formula: the resolvent of an
extension is the resolvent of a reference operator plus a term built
from the Weyl function M(z). It CONVERTS the boundary-value question
into boundary values / invertibility of M(z). Useful to LOCATE the
limit and to organize the collar boundary condition (APS-type), but it
does not by itself supply the N-uniform or product-uniform bound — those
would have to come from uniform control of M(z), which is an added
input. The type-change surfaces as M(z) losing its definite (Nevanlinna
/ definitizable) sign structure at the wall. Type: PARTIAL / locator.

## 5. Pseudospectra / non-self-adjoint resolvent bounds

On the crossed sector the section datum is a K_S-SKEW involution and
the induced pairing is anti-Hermitian (section-theory doc, Section 1,
Krein-analyst lens): the operator there is effectively NON-SELF-ADJOINT.
The relevant theory is pseudospectra (Trefethen-Embree, "Spectra and
Pseudospectra," 2005; Davies). The governing fact: the resolvent norm
is uniformly bounded OUTSIDE the epsilon-pseudospectrum and cannot be
bounded uniformly INSIDE it; semiclassical results (Dencker-Sjostrand-
Zworski; Sjostrand) give uniform resolvent bounds outside the pseudo-
spectrum under ellipticity at infinity, and resolvent norms that blow up
inside. The wall's Jordan nilpotent sits INSIDE the pseudospectrum, so
this framework PREDICTS the sup-norm blow-up and gives the z-region
(stay outside the pseudospectral tongue), but supplies NO positive
uniform theorem across the wall. Critically, pseudospectra are known to
be BADLY behaved under products (the epsilon-pseudospectrum can be far
larger than the neighborhood of the spectrum; Trefethen-Embree) — this
is where the product-uniformity clause has no free ride. Type: PARTIAL /
diagnostic + the source of the product-uniformity difficulty.

## 6. Parameter-elliptic / Agmon / Boutet de Monvel collar estimates

The Agmon / Agranovich-Vishik theory of parameter-elliptic boundary
value problems, and its manifold/collar form in the Boutet de Monvel
calculus (Schulze; Grubb), give resolvent bounds
|| (A - z)^{-1} || <= C/|z| that are UNIFORM in the parameter (and,
discretized, N-uniform) PROVIDED the principal symbol minus z is
invertible for z in a closed sector — Agmon's "ray of minimal growth" /
ellipticity with parameter. This is the framework that would most
directly give the delta- and N-uniformity IF it applied. It does not:
q_op -> 0 at the wall makes the leading (section) symbol M/sqrt(q)
NON-INVERTIBLE at the wall, so the parameter-ellipticity hypothesis
fails exactly there. Type: DEFEATED-BY-TYPE-CHANGE; named hypothesis
violated: **ellipticity with parameter / ray of minimal growth** at the
wall. Off the wall it gives the collar uniformity for free.

## 7. Norm-resolvent convergence of discretized (Dirac) operators

Cornean, Garde, Jensen, "Discrete approximations to Dirac operators and
norm resolvent convergence" (arXiv:2203.07826) show that naive finite-
difference Dirac operators do NOT converge in norm-resolvent sense in
dimension >= 2 (only strong resolvent convergence), and a MASS-TERM
modification is required to restore norm-resolvent convergence; related
mesh-explicit resolvent-difference bounds appear for discretized Fourier
multipliers (arXiv:2010.16215) and delta-shell Dirac (Behrndt et al.,
Math. Nachr. 2025). Bearing on the A3 N-uniformity gap: N-uniform
norm-resolvent convergence of a discretized first-order operator is a
KNOWN-DELICATE point with published positive AND negative results, NOT a
routine corollary — which corroborates the receipts' decision to leave
N-uniformity open. But all this machinery assumes a fixed self-adjoint
limit with a spectral gap; none of it covers a type-changing Krein
symbol. Type: PARTIAL, informs the N-uniformity clause only.

## 8. Melrose-Piazza spectral sections / APS families

Melrose-Piazza spectral sections (and the non-compact-base
generalizations, arXiv:2008.04672; the two-proofs note arXiv:2112.04673)
give a family version of the APS boundary condition and, importantly,
a PRODUCT FORMULA for eta-forms in product situations. But a spectral
section requires a regular self-adjoint operator with COMPACT resolvent
(gap-uniform boundary family), which the GU end explicitly refuses
(n2: "every off-the-shelf spectral-section theorem requires an
invertible — or at least gap-uniform — boundary family; the faithful
GU end REFUSES that hypothesis"). It classifies (index/eta level), it
does not bound resolvent norms, and its product formula is for eta-forms
not for resolvent uniformity. Type: IRRELEVANT-FOR-THE-BOUND / DEFEATED.

# Section 3. (a) Single best framework + hypotheses to verify

**Best fit: the Krein-space positive-commutator (Mourre) LAP of
Georgescu-Gerard-Hafner, J. Funct. Anal. 265 (2013) 3245-3304.** It is
the only surveyed theorem that is Krein-native, produces a weighted
resolvent BOUNDARY VALUE (delta -> 0) on a z-region, and is designed for
non-compact settings. To deploy it for the GU target, verify for our
operator H (take H = D_op or the section generator, on a chosen real
interval I over the GAPPED sub-end):

1. **Krein self-adjointness + Borel functional calculus on I.** We have
   K_op D_op K_op = D_op^dag exactly; confirm a Borel functional
   calculus on I (definitizability on I, or the paper's weaker
   functional-calculus hypothesis). [likely OK on the gapped sub-end]
2. **1_I(H) Krein-positive on I.** TRUE on the gapped sub-end (P > 0),
   FALSE across the wall. This fixes the z-region (Section 3b).
3. **Uniform positive commutator (Mourre) estimate.** Build a conjugate
   operator A — the natural choice is the collar dilation/translation
   generator (roughly s d/ds or d/ds) — with
   Re <u,[H,iA]u> >= c <u,u> on Ran 1_I(H), and crucially with the
   Mourre constant c INDEPENDENT of N and stable across finite products.
   This is the one genuinely new estimate to prove; the discrete
   commutator must be controlled uniformly in the mesh (connect to the
   mesh-uniform machinery of row 7).

If (1)-(3) hold, the weighted resolvent boundary value exists and is
bounded on the strip, delta-uniformly; N- and product-uniformity follow
IF the Mourre constant is N- and product-independent.

# Section 4. (b) z-region guidance for the Prong-1 scope

State for the sibling scope agent, crisply:

**The bound is reachable precisely on the z-region whose spectral
interval is of DEFINITE Krein type** — i.e. z in a strip I +/- i[0, nu]
where 1_I(H) is Krein-positive. Concretely:

- Choose z with Im z >= nu_0 > 0 (bounded off the real axis), AND
- z lying over the DEFINITE-TYPE gap of the GAPPED sub-end symbol
  (P > 0 sector), i.e. bounded AWAY from the images of the walls /
  critical points, AND
- z OUTSIDE the epsilon-pseudospectral tongue that the wall's Jordan
  nilpotent opens on the crossed sector (row 5).

Equivalently: the resolvent set to target is the **definite-type
resolvent set of the sector-restricted operator**, not the full end.
This directly answers the operator-grade doc's own caveat ("z = 2i is a
single resolvent point; a theorem needs the boundary value on a
z-region"): the region is the **Krein-positive-projection strip over the
spacelike sub-end**. Do NOT scope the z-region to sit over the crossing
sector — there the operator is effectively non-self-adjoint and only a
pseudospectral (non-uniform) statement is available.

# Section 5. (c) Product-uniformity verdict

**Genuinely NOVEL.** No surveyed framework delivers resolvent /
boundary-value bounds uniform across finite PRODUCTS of the carrier as a
standard corollary:

- Direct sums are trivial (resolvent norm = max of the summands) — but
  the clause is about genuine products, not sums.
- Kronecker sums have additive spectra, but PSEUDOSPECTRA are not the
  neighborhood-sum and can be much larger than the union (Trefethen-
  Embree) — so a uniform resolvent bound does NOT pass to products for
  non-normal / effectively-non-self-adjoint pieces, which is exactly the
  crossed sector's situation.
- Melrose-Piazza supplies PRODUCT FORMULAS but at the eta-form / index
  level, not resolvent-norm uniformity.
- The Mourre/LAP framework (row 2) has no product clause; a positive
  commutator estimate for a product would have to be established
  separately (tensor products of conjugate operators do not
  automatically inherit the Mourre constant).

Verdict: the product-uniformity clause is the one piece with NO
off-the-shelf precedent — it is the novel content of the theorem, over
and above the (adaptable) single-carrier LAP.

# Section 6. (d) Reachable-vs-new-mathematics — honest call

**Plausibly REACHABLE on the definite-type z-region by adapting the
Krein-Mourre (Georgescu-Gerard-Hafner) machinery — but the wall and the
product clause push the FULL theorem into genuinely-new territory.**

The single missing ingredient (name it precisely):

> **A uniform regularity statement for the wall as a Krein critical
> point** — i.e. a proof that the type-changing wall is a REGULAR (not
> singular) critical point of the K_S spectral function, with the
> regularity UNIFORM in N and stable across finite products; equivalently
> a delta- and N-uniform positive-commutator (Mourre) estimate whose
> constant degrades controllably (not to zero) at the wall.

Why this is the crux: definitizable theory (row 1) makes the entire
boundary-value bound hinge on regular-vs-singular at the critical point;
the sup-norm ~N^1.35 divergence is the signature of a SINGULAR critical
point in sup-norm, while the delta-Cauchy norm-resolvent mode is
consistent with a critical point that is regular IN RESOLVENT NORM though
singular in sup-norm. Deciding that — and doing it uniformly in N and
across products — is not answered by any surveyed theorem:
- If the wall is regular-in-resolvent uniformly: the theorem is
  reachable (Krein-Mourre on the sub-end + a uniform commutator estimate
  + a product argument for the commutator constant).
- If it is singular: the theorem needs genuinely new mathematics — a
  SECTOR-RELATIVE limiting absorption principle with a controlled
  singular critical point at a type-change wall, PLUS a product-
  uniformity clause with no precedent. This is the operator-grade
  version of n2's "no off-the-shelf theorem covers this," now localized
  to one estimate.

Honest posture: the ANALYTIC half (single-carrier, definite-type
z-region, delta-uniform) is adaptable from published Krein-Mourre and
parameter-elliptic machinery; the WALL-CROSSING half and the PRODUCT
half are the new mathematics, and both reduce to the single regularity-
of-the-critical-point ingredient above. Nothing here moves claim status,
canon, scorecard, or posture; this is a literature scope note.

# Section R. Receipts / URLs (every framework claim sourced)

Fetched or search-sourced 2026-07-20 (web):

- Georgescu, Gerard, Hafner, "Boundary values of resolvents of
  selfadjoint operators in Krein spaces," J. Funct. Anal. 265 (2013)
  3245-3304. arXiv:1211.0791 https://arxiv.org/abs/1211.0791 ;
  ScienceDirect https://www.sciencedirect.com/science/article/pii/S0022123613003510 ;
  HAL https://hal.science/hal-00748181v3 . (Hypotheses (1)-(3) and the
  weighted resolvent bound: from the arXiv abstract fetch; PDF body did
  not parse — abstract-level citation, flagged.)
- Follow-up: Georgescu-Gerard-Hafner, "Resolvent and propagation
  estimates for Klein-Gordon equations with non-positive energy,"
  J. Spectral Theory 5 (2015) 113-192. arXiv:1303.4610
  https://arxiv.org/pdf/1303.4610 .
- Langer, "Spectral functions of definitizable operators," Springer LNM
  https://link.springer.com/chapter/10.1007/BFb0069840 ; definitizable-
  operator resolvent estimate (Jonas). Locally-definitizable / sign-type
  survey https://link.springer.com/rwe/10.1007/978-3-0348-0692-3_38-2 .
  Singular critical points: Curgus-Gheondea et al.
  https://cedar.wwu.edu/math_facpubs/8/ .
- Klein-Gordon in Krein/Pontryagin (Langer-Najman-Tretter; Jonas):
  Comm. Math. Phys. 267 (2006)
  https://link.springer.com/article/10.1007/s00220-006-0022-4 ;
  Proc. Edinburgh Math. Soc. 51 (2008) 711-750
  https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/spectral-theory-of-the-kleingordon-equation-in-krein-spaces/C9337ADA741AB5AD97D8500C86484C72 .
- Boundary triples / Weyl functions (Derkach-Malamud; Behrndt-Hassi-
  de Snoo): https://link.springer.com/book/10.1007/978-3-032-02967-6 ;
  Krein-formula chapter
  https://link.springer.com/rwe/10.1007/978-3-0348-0692-3_32-1 .
- Pseudospectra / non-self-adjoint resolvent bounds: Trefethen-Embree,
  "Spectra and Pseudospectra" (2005)
  https://press.princeton.edu/books/hardcover/9780691119465/spectra-and-pseudospectra ;
  Trefethen, "Pseudospectra of linear operators"
  https://people.maths.ox.ac.uk/trefethen/publication/PDF/1997_72.pdf ;
  semiclassical resolvent-outside-pseudospectrum
  https://arxiv.org/pdf/math/0402172 .
- Parameter-elliptic / Agmon / Boutet de Monvel collar resolvents
  (Agranovich-Vishik, Seeley, Schulze, Grubb): conic/collar parameter-
  dependent resolvents https://arxiv.org/pdf/math/0503021 ;
  parameter-dependent pseudodifferential (Toeplitz type)
  https://arxiv.org/pdf/1202.4574 .
- Discretized Dirac norm-resolvent convergence: Cornean-Garde-Jensen,
  arXiv:2203.07826 https://arxiv.org/pdf/2203.07826 ; discretized Fourier
  multipliers arXiv:2010.16215 https://arxiv.org/pdf/2010.16215 ;
  delta-shell Dirac (Behrndt et al., Math. Nachr. 2025)
  https://onlinelibrary.wiley.com/doi/10.1002/mana.70004 .
- Spectral sections (Melrose-Piazza) + non-compact base + eta-form
  product formula: arXiv:2008.04672 https://arxiv.org/abs/2008.04672 ;
  two-proofs note arXiv:2112.04673 https://arxiv.org/abs/2112.04673 .

Gap flagged (no loop-retry per directive): the arXiv:1211.0791 PDF body
did not parse in WebFetch; the three-hypothesis statement and the
weighted-resolvent conclusion are cited at ABSTRACT grade
(arXiv abstract + JFA metadata), not from the theorem statement in the
body. All other framework claims are search- or abstract-sourced as
listed. No computational sanity-check was run (literature scout).

# Boundary

Literature scope note, no probe. Nothing here is a GU claim, canon
verdict, scorecard row, or posture move. It scopes Prong-1: best
framework = Krein-Mourre LAP; z-region = the Krein-positive-projection
strip over the gapped sub-end, off the wall and off the pseudospectral
tongue; product-uniformity = novel; the one missing ingredient = uniform
regularity of the wall as a Krein critical point (N- and product-stable).
No commits, no pushes, no edits to existing files; only this file.
