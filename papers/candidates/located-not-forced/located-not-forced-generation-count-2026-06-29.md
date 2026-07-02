# Located, Not Forced: Two-Primary Obstructions Cannot Force the Fermion Generation Count in a Clifford Rarita-Schwinger Sector

**Draft for external review. This paper does NOT claim three generations.** The theorem-grade results are
independent of Geometric Unity; every GU-specific step is marked motivated or reconstruction-grade. Five
load-bearing caveats hold throughout: **(a)** the torsion-count reading is a *premise, not a result* -- under a
literal integer-index reading the same obstructions would instead *forbid* an odd count outright; **(b)** the
order-3 class cannot literally *be* an integer count, since `Hom(Z/3, Z) = 0` (no homomorphism from a torsion
group to a torsion-free one is nonzero); **(c)** the generation count is *external on present evidence*, not
necessarily external; **(d)** the antilinear non-existence leg is an *open finite adversarial hunt, not a closed
proof*; **(e)** every verification reported here is *internal* -- computations reproduced from scratch and
adversarially reviewed within the same AI-directed process that produced them; no result has yet been
independently replicated or peer-reviewed. See Sections 1 and 9.

*arXiv submission source: [`located-not-forced-generation-count-2026-06-29.tex`](located-not-forced-generation-count-2026-06-29.tex)
(LaTeX; this markdown is the readable working copy). Suggested classification: primary **hep-th**; secondary
**math-ph**, **math.AT**. Keywords: generation number, family puzzle, Rarita-Schwinger, primary decomposition,
index theorem, framed bordism, Adams e-invariant, anomaly inflow, chirality.*

Internal version 2.5.1, 2026-07-02 (repo working copy; the arXiv PDF carries no version number -- arXiv assigns
its own v1, v2, ...). Changelog: v1.1 forcing-slot test; v1.2 the `Hom(Z/3, Z) = 0` sharpening; v1.3 the
carrier-mass capstone; v2.0 the GU-independent class-level structural no-go; v2.1 first hostile-referee
punch-list -- regraded the no-go as a finite adversarial hunt rather than a closed proof, removed the
"necessarily external" and "Standard-Model-shaped" overclaims, fixed the count-forcing vs count-producing
wording, added the torsion-count contingency, upgraded the Theorem 1 and Theorem 2 statements; v2.2
pre-submission punch-list -- keystone normalization attribution and narrowed novelty (conceded the `Z/24` split
and `pi_3^s` use to Wang 2023); v2.3 hardened against a second hostile-referee report -- finite-dimensional
Theorem 2 proof (defuses the Fredholm objection), corrected the `(14,0)` signature to a chirality-detecting
control, added the normalization-conventions paragraph and the order-3 footnote, front-loaded the torsion-count
contingency, restored Wang's full title; post-2.3 -- retitle, and a second hostile-referee pass triaged
(softened "class CII" to "class-CII type", "sole possible bridge" to "natural bridge"; synced the repo prose to
the paper's gated grade); v2.4 pre-submission readiness pass (2026-07-02) -- ported the "2+1 is numerology"
demonstration into the .tex (its Section 10 cross-reference was previously unsupported in the submission
source), added the exact Spin(9,5) Majorana-channel absence (MOVE-4 / SHIAB-05) as a scoped consistency remark
to the carrier-mass capstone in both copies, added three missing status-table rows to the .tex (forcing-slot NO,
2+1 numerology, carrier Dirac mass), synced the .md status table's CRT and novelty rows to the .tex's hedged
v2.2/v2.3 grades (stale stronger wording removed), and added \pdfoutput=1 for arXiv autoTeX; v2.5 final
publication gate (2026-07-02) -- added caveat (e) and a Verification-status paragraph (all verification is
internal-tier: reproduced, not independently replicated; per the project's three-tier vocabulary ratified
2026-07-02), cut the "evidence tilts toward one" prediction-flavored phrasing (per the tracker's F1 warning) and
the "referee-proof" self-description, conceded Theorem 2's classical Krein-space core and the NCG Krein-SM
precedent (novelty now claimed only for the embedding + application), softened the residual "only object that can
bridge" to "natural bridge" in Sections 5 and 7, scoped the abstract's forcing-slot "hardens" sentence to toy
level, added the Furey-Hughes algebraic-lane citation and GU's own "Caveat Emptor" disclaimer of draft eq. 10.10,
and fixed the stale v2.3 header comment in the .tex. See CHANGELOG-v2.5-publication-gate.md; v2.5.1
adversarial-review response (2026-07-02) -- raised Theorem 1's enumeration-conditionality into the abstract and
the theorem statement (completeness of the enumeration is open), added the chain-relativity sentence for the
Pati-Salam "1" (one reduction chain among many), marked every "locates the slot" phrasing as interpretation with
the `Hom(Z/3,Z)=0` flag adjacent, added the Theorem 2 finite-dimensional-kinematics scope sentence (the
function-space extension named as open), retitled the "single decider / honest gate" colloquialisms, and added
the computational pointer for the Spin(9,5) Hom-vanishing remark. See CHANGELOG-v2.5.1-adversarial-review.md.
Publication DEFERRED (2026-07-02) pending WC-ENUM-COMPLETENESS and WC-ANTILINEAR-BOUND (see STAGING-NOTES.md).

---

## Abstract

We study the chirality and generation structure of an explicit real Clifford Rarita-Schwinger sector: the
gamma-traceless rank-3/2 field of a real Clifford module `Cl(p,q)` with `p+q = 14` on a 128-dimensional
spinor, with one generation identified with the `16` of `Spin(10)`. The sector is motivated by, and
reconstructed from, the matter proposal of Geometric Unity (GU); every GU-specific step is marked, and none
of the theorem-grade results depend on GU being correct. We prove two theory-independent structural results
and use them to pin down, precisely, the only place a generation count could live.

First, a **2-primary meta-theorem**: every *enumerated* obstruction to a net chiral count in this sector is even or
mod-`2^k` (Kramers, the real/pseudoreal mod-2 Witten index, the cross-chirality Krein signature, the adjoint
index `4k`, Rokhlin mod 16, a spinor 2-smoothness lemma, ghost parity), so the no-go is arithmetically
incapable of imposing an odd-prime congruence and is structurally blind to the 3-primary summand of
`pi_3^s = Z/24 = Z/8 (+) Z/3`. **This no-go is conditional on the enumerated obstruction list; completeness of
the enumeration is open** -- Theorem 1 is not an impossibility statement over all conceivable obstructions.
Second, a **machine-verified index-conservation theorem**: the invariant Krein
form on the generation triplet is purely cross-chirality `(+96, -96)`, so every *linear* Krein-isometric
operator conserves the net chiral index at zero -- a finite-dimensional fact (the cross-chirality `(96,96)` form
makes every physical subspace chirality-balanced; no Fredholm theory), confirmed in the physical signatures
`(9,5)`, `(7,7)` with Euclidean `(14,0)` as a chirality-detecting control -- and
the unique symmetry-respecting escape is an **antilinear** (CPT / particle-hole, Altland-Zirnbauer class-CII type)
re-grading.

The decomposition `pi_3^s = Z/8 (+) Z/3` is the central structural fact. By the Chinese Remainder Theorem the
two summands are disjoint and non-interacting; every obstruction and every chiralizing selector lives in the
2-primary `Z/8` summand, while a homotopy-theoretic count, if it exists, lives only in the odd-torsion `Z/3`
summand. We exhibit a genuine order-3 object in that sector -- the framed-bordism Adams `e`-invariant
`e_R = 1/12` carried by the self-dual `Lambda^2_+` tangential framing on the `RP^3` spine of the metric fiber
-- and we show by explicit computation that it is **tangential but vectorlike and homotopy-fixed**: it
locates the order-3 slot without filling it with a count ("locates" is an interpretive gloss under the
torsion-count premise of caveat (a), not a further computed quantity; by `Hom(Z/3, Z) = 0` the located class
cannot itself be a count), and the only count-*forcing* operator is
frame-trivial and couples to the gauge (2-primary) channel.

We then attempt the single calculation that could decide an integer count on GU's actual 14-manifold and find
it **gated** on an unbuilt object (the stabilized twisted Rarita-Schwinger source action); the only honest
computable generation integer is **one** (GU's own Pati-Salam `Spin(7,7)` chain). A toy of that source action,
built and adversarially tested four ways, does **not** fill the forcing slot -- every integer it produces is
2-primary or one -- which hardens the RS-side gate verdict from conjecture to computation at toy level (the
actual stabilized action remains unbuilt). Reopened GU-independently, the
obstruction is a **class-level structural no-go** (computed and adversarially verified): no covariant operator
interior to a Clifford-RS sector of this type was found to force an odd chiral count -- frame-triviality is
evadable only into a 2-primary, index-conserving channel, and no frame-non-trivial antilinear loophole survived
an adversarial hunt (an exhaustive non-existence proof is open). On present evidence the generation count is
therefore **external** -- supplied by a net-self-dual chiral background of the general kind that produces
chirality in known chiral theories (chiral gauge couplings, instanton zero-modes, `K3` / Calabi-Yau
compactification). We therefore do **not** claim three generations. We claim a no-go that *locates*: it pins the unique CRT-disjoint sector where an odd
count could live, shows that sector genuinely carries an order-3 object, and poses the
`order-3-class -> integer-3` identification as the single named open conjecture (and a candidate category
error). We situate the mechanism against the recent family-puzzle literature; in a best-effort search we have found no
precedent for the CRT 2-vs-3-primary reading (obstructions in `Z/8`, a count in `Z/3`). External review of both the core results
and the open bridge is requested.

---

## 1. Introduction

The Standard Model contains three generations of fermions and does not explain the number. A recurring hope
in unification is that the number is fixed by topology. The obstacle, made precise here, is that the natural
index- and anomaly-theoretic invariants one computes *in this sector* are predominantly **2-primary**:
mod-2 Witten anomalies, mod-16 topological-superconductor classifications, even-valued Dirac indices. A
2-primary invariant cannot, by arithmetic, force an odd count. (Where the literature *does* obtain an odd
constraint -- Garcia-Etxebarria-Montero's `Z_9 -> N_gen in 3Z` is the sharpest example -- the constraining
anomaly is itself genuinely 3-primary, consistent with the thesis that an odd count requires 3-primary input.)

This paper turns that obstacle into a positive structural statement, in one explicit sector, and then tests
the strongest possible reading of it by direct computation. Our contributions:

1. **A 2-primary meta-theorem (Section 4).** Every *enumerated* obstruction to a net chiral count in this sector
   is even or mod-`2^k` (scoped to the listed classes). The no-go is conditional on the enumerated obstruction
   list; completeness of the enumeration is open. [theorem, theory-independent]
2. **A CRT two-arena structure (Section 5).** `pi_3^s = Z/24 = Z/8 (+) Z/3` splits, by the Chinese Remainder
   Theorem, into disjoint summands. Every obstruction *and* every chiralizing selector lives in `Z/8`; a
   homotopy-theoretic count lives only in `Z/3`. The two arenas cannot interact directly within the group
   structure; anomaly inflow is the natural bridge between them. This is the unifying frame: the no-go is blind to the count not by weakness but
   by arithmetic.
3. **An index-conservation theorem, a necessary antilinear escape, and a class-level structural no-go
   (Section 6).** Every linear Krein-isometric operator conserves the net chiral index at zero (proven directly:
   the cross-chirality `(96,96)` form makes every physical subspace a chirality-balanced graph -- a
   finite-dimensional fact, no Fredholm theory; machine-corroborated); the unique symmetry-respecting escape is
   antilinear.
   Reopened GU-independently: **no covariant operator found -- linear or antilinear -- interior to a Clifford-RS
   sector of this class forces an odd chiral count.** Frame-triviality is evadable, but only into a 2-primary,
   index-conserving channel (a linear `O = L_SD (x) X_L` is net-chiral and frame-active, yet by Theorem 2
   forces no count), and no frame-non-trivial antilinear loophole survived an adversarial hunt (every candidate
   is chirality-reversing, carrier-leaking, or a gauge dressing with `p_1 = 0`; an exhaustive non-existence
   proof is open). On present evidence the generation count is therefore **external**, supplied by a
   net-self-dual chiral background of the general kind that produces chirality in known chiral theories.
   [computed structural no-go, theory-independent; linear leg theorem-grade, antilinear non-existence a finite
   adversarial hunt]
4. **A located order-3 carrier (Section 7).** The self-dual `Lambda^2_+` tangential framing on the `RP^3`
   spine carries `e_R = 1/12`, a genuine order-3 class in the `Z/3` summand -- shown by computation to be
   tangential but vectorlike and homotopy-fixed: it locates, it does not fill ("locates" is an interpretive
   gloss under the torsion-count reading, not an additional computed quantity).
5. **The deciding computation, and the gate (Section 8).** The integer count on GU's actual 14-manifold is
   gated on the unbuilt twisted Rarita-Schwinger source action; the only honest computable integer is one.
   We do not force three.
6. **The open conjecture (Section 9).** `order-3-class -> integer-3` is a theorem of nothing in the present
   literature and is a candidate category error. We state it as the single open bridge and request review.

The robust, theory-independent content is items 1-3 together with the located carrier of item 4. The GU
identification and the generation-count reading are clearly marked reconstruction-grade or open.

---

## 2. The setting

Let `S` be the real spinor module of `Cl(p,q)`, `p+q = 14`, `dim_R S = 128`. The Rarita-Schwinger field is
the gamma-traceless part of `V (x) S`; the constraint cuts `V (x) S` (dimension `14*128 = 1792`) to
`ker(Gamma)`, of dimension `(14-1)*128 = 1664 = 2^7 * 13`. We split `14 = 4 + 10`: a four-dimensional base
`X^4` and a ten-dimensional internal space, with one generation the `16` of `Spin(10)`. The base frame group
is `Spin(4) = SU(2)_+ x SU(2)_-`; the self-dual two-forms `Lambda^2_+` generate `su(2)_+`. Under `su(2)_+`,

```
ker(Gamma) = 640 (singlets) + 832 (doublets) + 192 (triplets),
```

verified numerically (`tests/generation-sector/h1_selfdual_family_kill.py`). The `192`-dimensional `j=1`
sector is the native multiplicity-three structure: a genuine triplet carrying the `16`. The invariant
bilinear is the `so(p,q)`-invariant Krein form `K = eta_V (x) beta_S`; on the triplet it is purely
cross-chirality, signature exactly `(+96, -96)`, so the matter content is vectorlike with net chirality 0.
This is the central tension: the sector is multiplicity-three but vectorlike, and no internal operation
chiralizes it.

---

## 3. Multiplicity versus chirality

The integer 3 plays two arithmetically different roles in this sector, and conflating them is the error the
"located, not forced" reading most guards against. A **multiplicity** is the dimension of a flat family space --
the number of copies of a fixed representation the constrained module carries; it is a representation dimension,
comes with its mirror (copies and anti-copies), and is vectorlike. A **net chiral count** is an index -- the
signed difference (left minus right) of Dirac zero modes; it measures chirality, the property a vectorlike
spectrum lacks. A representation dimension and an operator index are not one number computed two ways. This sector
supplies the first natively and does not supply the second.

**The multiplicity is natively three (verified).** Under the self-dual `su(2)_+` of the 4-base, the
gamma-traceless module decomposes as in Section 2. Written by *multiplicity* rather than dimension,

```
ker(Gamma) = 640 (j=0) + 416 (j=1/2) + 64 (j=1),   640*1 + 416*2 + 64*3 = 1664,
```

i.e. 640 singlets, 416 doublets and 64 triplets, the 64 triplets spanning the 192-dimensional `j=1` sector of
Section 2. On all 192 states the `Spin(10)` Casimir matches the reference `16 / 16bar` value to machine precision
(`tests/generation-sector/h1_selfdual_family_kill.py`). A native multiplicity-three object exists, carried by the
self-dual geometry of any oriented 4-base; the multiplicity dimension 3 is not imported.

**Lemma (spinor 2-smoothness).** *If a family symmetry `SO(m)` acts so that the multiplicity space is a sum of
spinor representations of `SO(m)`, its dimension is a power of two, hence not divisible by 3. An odd multiplicity
can therefore arise only from a non-spinor family representation -- a vector, an adjoint, or a self-dual tensor.*
The Dirac spinor of `SO(m)` has dimension `2^floor(m/2)` and each half-spinor of `SO(2k)` has dimension
`2^(k-1)`; all are powers of two, never divisible by the odd prime 3. The vector (`m`), the adjoint
(`m(m-1)/2`) and self-dual tensors are not so constrained; `Lambda^2_+` of a 4-manifold has dimension 3. QED.

**Three is the canonical odd multiplicity (verified for the commutant of the full `Spin(10)`).** The lemma turns
an open-ended search into a dichotomy: the spinor channels are provably 3-free, so any odd multiplicity must enter
through a non-spinor channel. Inside `Spin(14) ⊃ Spin(10) x Spin(4)` the commutant of `Spin(10)` is
`so(4) = su(2)_+ (+) su(2)_-`, which up to conjugacy has exactly three `su(2)` subalgebras (self-dual,
anti-self-dual, diagonal), and no `su(3)` embeds (by dimension, `dim su(3) = 8 > 6 = dim so(4)`). Enumerating the
16-dimensional multiplicity space under each (`tests/generation-sector/leg3_family_embedding_enumeration.py`),
only the self-dual and anti-self-dual `su(2)` (orientation images of one another) give an odd multiplicity, always
the triplet of dimension 3, never a quintet or higher; the diagonal choice gives an all-even content. So for
family symmetries commuting with the full `Spin(10)` the self-dual route is canonical and the multiplicity it
fixes is three. *This is a statement about a representation dimension, not a net chiral count.* The case of a
family symmetry commuting only with the Standard-Model subgroup `G_SM ⊂ Spin(10)` -- whose larger commutant could
in principle host a horizontal `su(3)` -- is not covered here and is a bounded open computation; the lemma already
constrains it.

**But the triplet is vectorlike, so the native three is not a chiral three.** The native multiplicity three is
vectorlike: as in Section 2, the invariant Krein form `K = eta_V (x) beta_S` on the triplet is purely
cross-chirality with signature `(+96, -96)`, so every physical subspace is chirality-balanced and the net chiral
index is 0 (Theorem 2). The native object is three copies plus three mirrors; turning it into a *net* three is a
separate datum -- an index, or a chiral projection -- that the internal algebra does not fix, that Section 4 shows
is even on every enumerated obstruction, and that Section 6 shows no interior operator supplies. **The multiplicity
three is native; the chiral three is not.** This is the representation-theoretic form of "located, not forced":
the sector locates a genuine three (as a multiplicity) and does not force a three (as a chirality).

---

## 4. Theorem 1: the no-go is 2-primary

Call an integer or torsion invariant **2-primary** if it is a power of two, a multiple of one, or a
statement modulo a power of two.

**Theorem 1 (a no-go conditional on the enumerated obstruction list).** *Among the obstructions to a net chiral
generation count enumerated for this sector (items (1)-(7) in the proof below), none is an odd-prime congruence:
every enumerated obstruction is even or a statement modulo a power of two, and in particular none imposes a mod-3
condition. The no-go is conditional on this enumerated list: completeness of the enumeration is an open question,
and the claim is not an impossibility statement over all conceivable obstructions.*
(The loose "even" reading is near-vacuous -- `96 = 2^5 . 3` is even; the content is the modular statement, that no
enumerated obstruction is a mod-odd-prime condition.)

**Proof (enumeration).** (1) Kramers / quaternionic wall (`J^2 = -1`): a `Z/2` statement. (2) Real /
pseudoreal non-chirality: the mod-2 Witten index, `Z/2`-valued. (3) Cross-chirality Krein signature: the
`(+96, -96)` even split forces net chirality 0. (4) Adjoint Dirac index `2 T(adj) k = 4k`, divisible by 4;
over the full multiplicity bundle `12k` or `24k`, even. (5) Rokhlin: `sign(X) = 0 (mod 16)`, mod `2^4`.
(6) Spinor 2-smoothness: a spinor of `SO(m)` has dimension `2^floor(m/2)`, a power of two; only a non-spinor
(vector / adjoint / self-dual) family representation can be odd-dimensional. (7) Ghost parity: a ghost-parity
resolution of the Krein hyperbolic pairs yields a `50/50` (net 0) physical sector. Every item is even or
mod-`2^k`; there is no odd-prime congruence anywhere in the enumeration. QED.

*Remark.* The integer 3 does appear in the sector -- as a multiplicand (`96 = 2^5 . 3`, `12k`, `24k`,
`|Weyl(D7)|`). Theorem 1 is not "no factor of 3 occurs." It is the sharper statement: **no obstruction is an
odd-prime congruence.** A standard analogue: the 3-primary part of the stable 3-stem is invisible to a mod-2
Postnikov/Adams analysis.

---

## 5. The CRT two-arena structure

`pi_3^s = Z/24`, with primary decomposition `Z/24 = Z/8 (+) Z/3`. Adams' image-of-`J` theorem gives, in
stem `4s-1`, that `Im J` is cyclic of order `denom(B_{2s}/4s)`; for `s=1` this is `24`, so `Im J_3 = Z/24`
and the Adams `e`-invariant detects it.

**The central structural fact.** By the Chinese Remainder Theorem the splitting `Z/24 = Z/8 (+) Z/3` is into
**disjoint, non-interacting summands**: there is no nonzero homomorphism `Z/8 -> Z/3` or `Z/3 -> Z/8`. By
Theorem 1, every obstruction in the no-go constrains only the `Z/8` (2-primary) summand. We show in Section 6
that every chiralizing *selector* likewise lives in `Z/8`. A homotopy-theoretic generation count, being odd,
can live only in the `Z/3` summand.

**Corollary (the two arenas).** *Under the torsion-count reading* -- that a generation count, if it exists,
lives as a 3-primary boundary `e`-invariant in the `Z/3` summand -- the question "does any obstruction or
selector force the count?" is **arithmetically ill-posed**: obstruction/selector and count inhabit CRT-disjoint
summands, so the answer is no before any geometric input. The no-go's blindness to the count (Theorem 1's
corollary) is then not a weakness but a *structural feature*. This premise is load-bearing and
reconstruction-grade: under a literal *integer-index* reading the same obstructions would instead **forbid** an
odd count outright (net index 0 forces count 0), so "located, not forced" presupposes the torsion-count reading
rather than the integer-index one (`canon/two-primary-lemma.md`, Correction 2). The natural bridge between the
two arenas is anomaly inflow (Callan-Harvey / Dai-Freed), and Section 8 shows that even the inflow
coefficient does not, on present computation, force three.

This is the unifying frame of the paper. We refer to `Z/8` as the *selector arena* and `Z/3` as the *carrier
arena*. The remaining sections show that the chiralizer lives in the selector arena, the count-carrier lives
in the carrier arena, and they do not meet.

---

## 6. Theorem 2: index conservation and the necessary antilinear escape

**Theorem 2.** *Every linear Krein-isometric operator on the generation triplet conserves the net chiral
index at zero.*

**Proof (finite-dimensional; the `.tex` carries the full statement and proof).** The cross-chirality `(96,96)`
Krein form makes the chirality eigenspaces `W_+`, `W_-` K-Lagrangian (K-isotropic), with K the pairing between
them. A *physical* subspace is a maximal K-positive-definite subspace `P` (dim 96). Since Lagrangians are K-null
and `P` is positive-definite, `P ∩ W_+ = P ∩ W_- = {0}`, so `P` projects isomorphically onto **both** `W_+` and
`W_-`: `P` is the graph of an isomorphism `W_+ → W_-`, hence chirality-balanced, so the net chiral index
`χ(P) = dim π_+(P) − dim π_-(P) = 0`. A linear K-isometry maps physical subspaces to physical subspaces, so
`χ(UP) = χ(P) = 0`. This is elementary finite-dimensional linear algebra -- no Hilbert space, Fredholm operator,
or spectral flow -- so the "you need a Fredholm index" objection does not apply, and group connectedness plays
no role (`χ` is identically 0, not merely constant). Machine-corroborated
(`tests/generation-sector/net_chiral_index_invariant.py`, building on `ghost_parity_krein.py`,
`t1a_kinematic_chirality_kill.py`): `χ = 0` in the physical indefinite signatures `(9,5)`, `(7,7)`; Euclidean
`(14,0)` is grading-*aligned* (Γ commutes with K), giving `|χ| = 96` as a chirality-detecting control. QED.

**Scope.** Theorem 2 is a statement of finite-dimensional *kinematics* on the 192-dimensional carrier; its
extension to a function-space setting -- sections of the Rarita-Schwinger bundle over a manifold, differential
operators, genuine Fredholm indices and spectral flow -- is a separate, named open problem, not addressed here.

**Corollary (necessary antilinear escape).** No linear / unitary dynamics generates chiral asymmetry in this
sector. By Wigner's dichotomy the unique symmetry-respecting escape is **antilinear** (CPT / particle-hole;
Altland-Zirnbauer class-CII type), realized by a re-grading `C = J_quat . G` with `C^2 = -I` (Kramers/PHS,
the antilinear part of `C` has norm `~ 85` -- i.e. `C` is genuinely antilinear, not a
deviation from the stated `C^2 = -I`). The induced time reversal `T = G C` completes the symmetry triple; the
precise real class (CII versus DIII) depends on whether `J_quat` commutes with `G`, which the argument does not
need to settle -- only that the escape is antilinear with `C^2 = -I`. Corroborated independently by a Seiberg-Witten moment-map degree argument: a
Krein-isometric moment map is degree-2 homogeneous while `ch_2` is degree-0 and connection-independent, so a
source action built from it is orthogonal to the topological index (`canon/source-action-seiberg-witten-RESULTS.md`).

**The antilinear chiralizer is frame-trivial (computed).** The escape operator `C = J_quat . G` is built from
`J_quat = id_14 (x) U` (the quaternionic structure) and the chiral grading -- both internal-fiber
endomorphisms. Its tangent-frame charge is **exactly 0**:
`max ||[J_quat, any tangent-frame so(9,5) rotation]|| = 0.00e+00`, including the `Lambda^2_+` rotation;
`|<J_quat, Lambda^2_+>| = 0`. This is convention-independent (any `id_14 (x) U` is traceless on the frame
factor; verified with a random `U`). Consequently the chiralizer carries no `p_1`, and its reduced boundary
`eta` is the 2-primary gauge type (`(2q^2-4q+1)/8`, here forced to 0 by `C^2 = -I`)
(`canon/boundary-eta-of-mu-RESULTS.md`). **The chiralizer lives in the selector arena `Z/8`.** It supplies
chirality; it cannot reach the carrier arena `Z/3`.

**Frame-triviality is evadable, but no operator forces an odd count: a class-level structural result (computed,
GU-independent).** Reopened without GU restriction, the question is whether *any* operator on a Clifford-RS
carrier of this type -- a real `Cl(p,q)`, `p+q = 14`, gamma-traceless rank-3/2 field, the `j=1` triplet carrying
a purely cross-chirality `(+96, -96)` Krein form -- can be both net-chiral and reach the tangent-frame (`p_1`)
channel where the order-3 carrier lives. The honest answer is a refined no-go
(`canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md`). The clean statement -- "net
chirality and frame charge have orthogonal support, so no operator can be both" -- is in fact **false** on the
carrier: its self-dual `V`-`S` entanglement (`J_3 = id (x) sgen + lvec (x) id`) gives the chirality grading
genuine self-dual spinor content (`||X_L|| = 2.0` on each self-dual frame generator, `~ 0` on anti-self-dual),
so a *linear* covariant operator `O = L_SD (x) X_L` is simultaneously net-chiral (`+16 = 2^4`) and frame-active
(net-self-dual `+2`). These are subspace-restriction / overlap quantities, **not** conserved indices: the full
carrier index stays exactly 0 under `O`, as Theorem 2 requires, so `O` is frame-active and 2-primary but forces
no count. The one genuine loophole Theorem 2 leaves -- a frame-non-trivial *antilinear* (CII) chiralizer -- was
hunted adversarially over candidate families on the `Cl(9,5)` representative and **none was found**: every
candidate is chirality-reversing (net 0), carrier-leaking, or a gauge dressing continuously deformable to the
frame-trivial identity (connected stabilizer, topological `p_1 = 0`, forcing the identical vectorlike `+96`).
The linear leg is theorem-grade (index conservation); the antilinear non-existence is a **finite adversarial
hunt, not a closed proof** (an exhaustive non-existence theorem over the infinite-dimensional antilinear space
is open). **On present evidence, then, no covariant operator interior to a Clifford-RS sector of this class
forces an odd chiral count.** GU's frame-trivial chiralizer is one instance.

**The count is therefore external on present evidence.** Forcing an odd chiral count requires an *external*
net-self-dual chiral background coupled through the index theorem (`int_X A-hat ch`). This is not a contrived
addition: it is of the same general kind by which chirality arises in every known chiral theory -- chiral gauge
couplings, instanton zero-modes, `K3` / Calabi-Yau compactification (examples of the kind, not a derivation of
Standard-Model structure). The result thus relocates the generation count from an internal derivation to
**external (bulk) background data** -- and even that data does not by itself pin three (the
`order-3-class -> integer-3` bridge of Section 9 remains). This is the paper's strongest GU-independent
statement: not a verdict on GU, but a structural no-go for the class, with the count relocated to external
background data.

---

## 7. The located order-3 carrier

The order-3 content lives in exactly one place. The self-dual `SU(2)_+ = Lambda^2_+` structure, read as a
**tangential** framing on `RP^3 = L(2;1)` (the deformation-retract spine of the metric fiber
`GL(4,R)/O(3,1)`), has framed-bordism class `+/- 2 in pi_3^s = Z/24` and Adams `e`-invariant

```
e_R = p_1/48 = 1/12   (p_1 = 4, Kirby-Melvin; class 2 in Z/24; 3-primary part nonzero, order 3).
```

The stabilization `pi_3(SO(3)) -> pi_3(SO)` is `x2`, so the stable degree is `p_1/2 = 2`, not the Dynkin
index 4. This is standard topology assembled from three stated conventions -- the generator of `H^4(BSpin;Z)`
(McLaughlin; Sati-Shim), the `x2` stabilization and framing normalization (Kirby-Melvin), and Adams'
`e_R` normalization; the composite `e_R = (p_1/2)/24` is ours, not a formula quoted verbatim from any one
source (the .tex normalization-conventions paragraph fixes all three). Only the identification of GU's
`Lambda^2_+` twist with this natural tangential framing is reconstruction-grade.

**It locates but does not fill (properties computed; "locates" is interpretation).** The carrier `Lambda^2_+`
has net self-dual tangent-frame charge
`33.94` (tangential, `p_1 = 4`) -- it is genuinely on the carrier-arena side -- **but it is vectorlike**
(net chiral 0, Section 2), and `e_R = 1/12` is **homotopy-fixed**: it is a fact about `pi_3^s`, identical for
a universe with one generation or five. So the carrier marks the order-3 slot; it does not co-vary with the
answer and so cannot, by itself, be the thing that counts to three. The negative control confirms the slot is
unique: `RP^3`'s own deck group is `Z/2`, and the charge-`q` Dirac `eta = (2q^2-4q+1)/8` is 2-primary for
every integer `q`, so the order-3 burden sits **only** in the gravitational framing channel `-p_1/24`.
Throughout, "locates the slot" is an interpretive gloss under the torsion-count premise (Section 5), not an
additional computed quantity: the computed facts are the tangentiality (`p_1 = 4`), the vectorlikeness (net
chiral 0), and the homotopy-fixedness; and by `Hom(Z/3, Z) = 0` (Section 9) the located class cannot itself
*be* an integer count.

We emphasize the resulting picture, which Sections 6 and 7 establish by computation: the **chiralizer** (the
only count-*forcing* operator; a frame-active linear operator can produce a net count but conserves the index
and forces nothing) is frame-trivial and lives in the selector arena; the **carrier** (the only order-3 object)
is frame-charged and lives in the carrier arena; they are distinct objects, with anomaly inflow the natural
bridge between them.

---

## 8. The deciding computation, and the gate

The only computation that could produce an integer count on GU's *actual* geometry, rather than a
homotopy-fixed class identical for any answer, is the net chiral index as the anomaly-inflow coefficient of
the bulk gravitational `-p_1/24` SPT class on the 14-manifold, with the tangential-vs-gauge fork resolved by
the computation. We constructed and ran it (`tests/decider/`, 26/26 checks across four scripts plus an
independent from-scratch re-verification, exit 0, all controls reproduced). The result:

- **The literal net-chiral integer is GATED** on the unbuilt stabilized twisted Rarita-Schwinger / IG source
  action (the `+8` Rarita-Schwinger leg of `ind_H = 8*A-hat(K3) + 8`). Every analytic route to it failed
  (ten Atiyah-Singer routes gave `{960, -288, -384, -192, -336, -128, 128, -8, -480, 60}`, none `= 16`); the
  computation explicitly refused it rather than fabricating a fit.
- **The only honest computable generation integer is one.** GU's verified Pati-Salam
  `Spin(7,7) -> Spin(6) x Spin(4)` chain gives 16 chiral states = exactly one anomaly-free generation
  (`Tr Y = Tr Q = 0`, `16 // 16 = 1`; "2+1 effective"). The `Spin(7,7)` Pati-Salam chain is one reduction
  among many possible symmetry-breaking chains; the integer 1 it yields is chain-relative, not
  chain-independent. The spin-1/2 leg is `8*A-hat(K3) = 16`, with
  `A-hat(K3) = 2` the "2" of "2+1". The bulk-topology-forced integers are `{0 (linear net-chiral, vectorlike),
  1 (Pati-Salam), 2 (A-hat(K3))}`; none is 3.
- **The fork lands gauge for the count-producing operator** (`e = 3/8`, denom `8`, 3-part zero), via the
  frame-triviality of Section 6 -- structural and convention-independent.

So under the decision rule fixed in advance, the strong reading dies twice over: the integer is not three
(it is gated, and the only honest one is one), and the fork lands gauge. Controls reproduced exactly:
`ch_2(S_X)[K3] = -5376 = -2^8 . 3 . 7` (the apparent "24" is a disguised `chi(K3)` import via `2chi+3sigma=0`,
rejected; a `chi`-route gives `ch_2 = 0`); `A-hat(K3) = 2`; the charge-`q` `eta` family; Pati-Salam `-> 1`.

**Gated, not fabricated.** Four things remain genuinely gated and are marked as such: (i) the `+8`
RS leg / the literal integer, on the unbuilt source action; (ii) the full analytic Bismut-Cheeger
fibered-boundary reduction theorem for the non-product 9-dim `S^6`-bundle over `RP^3` (the machinery is a
theorem and the even-fiber transparency `A-hat[S^6] = eta(S^6) = 0` is computed, but its application to GU's
actual twisted-RS boundary operator is gated; "the spine is `RP^3`" is not that theorem); (iii) the families
pushforward `pi_! : ch(S)/Y14 -> ch(S_X)/X4`, which is not defined because the fiber `GL(4,R)/O(3,1)` is
non-convex (so `ch_2(S_X)[K3] = -5376` is a bulk characteristic number, not yet the families index);
(iv) `order-3-class -> integer-3` (Section 9). The program has previously caught four fabricated paths to
three (a disguised `chi`, a reverse-engineered `+8`, a circular rank-4, a fitted holonomy); this computation
adds none, and asserts the absence (`integer_is_3 = False`).

**The forcing-slot test (computed).** Item (i) -- the gate on the unbuilt source action -- has since been
probed directly. We reverse-engineered the necessary conditions ("forcing slot") any source action must meet
to force a count: a term simultaneously (a) tangential (carries `p_1`), (b) net-chiral, and (c)
non-frame-trivial. We then built a toy stabilized twisted Rarita-Schwinger sector four ways (Faddeev-Popov
stabilization; the twisted spin-3/2 AGW index on K3; the RS frame-index operator on the `Cl(9,5)` substrate;
the gravitino anomaly polynomial), each angle adversarially re-verified (`tests/forcing-slot/`,
`canon/forcing-slot-toy-rs-RESULTS.md`). The RS sector reaches at most two of the three properties, never all
three with a 3-primary integer. Every computed integer lands in the selector arena or equals one: `256 = 2^8`
(a tautological projector trace, honest physical-sector index 0), `-672 = -2^5 . 3 . 7`, `-42 == 0 (mod 3)`
(the `Z/3` identity), the HP^2 unit `1`. The gravitino anomaly is not an odd-prime exception: every spin-3/2
coefficient is 2-primary up to von Staudt-Clausen denominators (no factor 3 in any numerator), and the
twisted-by-16 index `16(-42) + 3 ch_2(V)` is `== 0 (mod 3)` for every integer twist. The RS field is the unique
object that is intrinsically non-frame-trivial (its vector index is not `id_14 (x) U`) and chiral under the
16-twist -- but its cross-coupling (mixed gauge-gravitational anomaly inflow) lands 2-primary. The gate, where
it opens at all, opens onto the selector arena. This hardens "located, not forced" from conjecture to computed
result for the RS-side gate at toy level; the actual stabilized action remains unbuilt.

**The "2+1" reading is numerology across frameworks (computed).** The "2+1 effective" picture (the `2` from
`A-hat(K3)`, the `1` from Pati-Salam) is not a single legitimate count. In one common framework (the Â-genus
character-valued index on K3), the spin-1/2 leg gives `2` but the spin-3/2 leg gives `-42 == 0 (mod 3)`, not a
clean `+1`; the `+1` appears only as the twisted-Dirac unit on a different manifold (HP^2). The two summands of
`2+1` live in disjoint frameworks, so their sum is a coincidence, not a derivation. "Located, not forced" thus
holds under both the order-3/triality reading and the additive 2+1 reading.

**The carrier-mass capstone: the gate is one physical term (computed).** The carrier `Lambda^2_+` is vectorlike,
so it has no chiral protection and the entire located-vs-forced question reduces to a single term -- whether the
source action gives it a **Dirac mass** (`canon/carrier-dirac-mass-capstone-RESULTS.md`). The mass is **allowed,
not forbidden**: the Kramers structure `C^2 = -I` is pseudoreal, hence self-conjugate, hence vectorlike, which
*admits* a mass; and the built Seiberg-Witten action *realizes* a vectorlike one (`||M_++|| = ||M_--||`, a
`{+, 0, -}` split, heavy-sector net chiral 0). Both branches give zero, not three: massive, the 96 generation
modes pair with 96 mirror modes and decouple, leaving net chiral index `(n_+ - r) - (n_- - r) = 0` analytically
for every mass; massless, the 192 stay light but net chirality is still 0, a modulus. Forcing a light chiral
count requires a **chiral projection** that breaks the `+96/-96` balance, and no linear Krein-isometric operator
can supply one (index conservation; a linear chiral projector lands on a totally Krein-null, unphysical
subspace). The only operator that breaks the balance is the antilinear chiralizer `C = J_quat . G`, frame-trivial
(tangent-frame charge `0.00`, selector arena) and absent from the tangential `Lambda^2_+` sector where the
order-3 carrier resides. So the gate is now one physical term: **the carrier Dirac mass plus the selector-side
chiral projection GU never built** -- and the carrier resolves either way (massless modulus or massive-decoupled)
to zero net chiral generations absent an operator GU does not provide. Located, not forced, confirmed at the
mass/dynamical level. Consistently, exact `Spin(9,5)` representation theory (computed;
`tests/chase/MOVE-4/move4_spinor_square_forms.py`, with the independent re-check
`tests/chase/MOVE-4/verify/indep_check.py`) gives
`dim Hom_{Spin(9,5)}(S^+ tensor S^+, Lambda^0) = 0`: no invariant same-chirality Majorana scalar-mass bilinear
exists in the equivariant family (the scalar bilinear pairs only `S^+ <-> S^-`), so that mass channel too must be
supplied by an external source-action term. This is a consistency remark about the spinor-square channel, not a
statement about the 192-dimensional carrier's Dirac mass.

---

## 9. What is not claimed: the open conjecture

We do **not** claim three chiral generations. The honest verdict is **located, not forced.** The single open
bridge is

> `order-3-class -> integer-3`.

A nonzero class in `Z/3` detects information *mod 3*; it is not equality to the integer 3, and the
`e`-invariant carrying it (`e_R = 1/12`) is identical for any generation count. APS, Dai-Freed, Callan-Harvey,
and Bismut-Cheeger relate a boundary `eta`/`e`-invariant to indices, determinant lines, anomaly phases, and
cobordism classes -- never directly to an integer family count. So the identification is, in the present
literature, a theorem of nothing, and is a candidate **category error**. This is now algebraically explicit:
there is no canonical class-to-count map at all, since `Hom(Z/3, Z) = 0` (every homomorphism from a torsion
group to a torsion-free group vanishes). An integer count, if one exists, therefore cannot *be* the absolute
torsion class; it can only arise from a **relative, equivariant, or rank** invariant -- integer-valued by
construction yet geometry-dependent -- which is exactly what the unbuilt twisted Rarita-Schwinger index is. The
conjecture is thus better stated as: does that relative index exist on GU's 14-manifold and reduce mod 3 to the
located carrier? To earn "forced," three things must
be built, in one calculation, on GU's actual 14-manifold: a proven fibered-boundary reduction; the explicit
twisted Rarita-Schwinger index operator (the unbuilt source action); and an integer extraction with the fork
resolved. A toy of that twisted Rarita-Schwinger operator has now been built and tested four ways (Section 8);
it does not fill the forcing slot, and every integer it produces is 2-primary or one -- which strengthens the
conjecture's standing as a candidate category error over the gated-but-derivable alternative (the RS-side gate,
when probed, opens onto the selector arena). Until then the result is a no-go that *locates*; no computation
performed in this program yields the integer three.

---

## 10. Relation to Geometric Unity and to prior art

**Geometric Unity.** The sector is motivated by GU's matter proposal (the 14-dim observerse `Y14 = Met(X^4)`,
the vector-spinor field, the `4+10` split, the `16` of `Spin(10)`, the self-dual base structure). The draft
presents the fermion sector schematically, does not build the matter action (the draft's own candidate source
term, its eq. 10.10, is author-disclaimed: "until it is stabilized. Caveat Emptor."), states chirality is only
*effective*, and proposes a "2+1" picture rather than three true generations; the Nguyen-Polya critique argues
central technical details are unverifiable from the public material. Our results are therefore a
reconstruction, and where GU's own narrative points (its 2+1 hedge -- distinct from the computed
`A-hat(K3) + Pati-Salam` 2+1 that Section 8 shows to be numerology across disjoint frameworks; both, however,
point away from a clean internal three -- and the verified `Spin(7,7) -> 1` chain), it tilts against the strong
three-generation reading. We are explicit about this throughout.

**Prior art.** Deriving or constraining the generation number from topology or anomalies has substantial
precedent (Dobrescu-Poppitz 2001; Evans-Ibe-Kehayias-Yanagida 2012; Kaplan-Sun 2012; Garcia-Etxebarria-Montero
2019's `Z_9` anomaly forcing `N_gen in 3Z`; Juven Wang's 2023 family puzzle via framed/string bordism `Z/24`
with `c_- = 24`; and Wan-Wang-Yau 2026 (arXiv:2605.26202), where the group-cohomology subclass `H^5(Z_n,U(1))`
of the 5d spin-bordism anomaly is cancellable by an anomalous `Z_n` 4d TQFT while the beyond-cohomology
Pontryagin `p_1` part is not except at `n=2,3`, isolating `n=3`). Deriving three generations from algebraic
structure is likewise an active lane -- e.g. the division-algebra trialities of Furey-Hughes (arXiv:2409.17948),
where two generations arise as spinors and a third through a Cartan factorization; our Clifford-RS route is
mechanically distinct, but the question is not untouched. We claim no novelty for "topology constrains
family number." (The .tex submission source carries the full verified bibliography.)
Our narrow novelty claim (final wording in the `.tex`): Wang 2023's title arithmetic `24/8 = 3` already pulls
the odd 3-primary factor out of `Z/24` as the family number, and Wan-Wang-Yau 2026 isolate `n=3` via a
cohomology-vs-Pontryagin split, so we claim **no** novelty for the bare 2-vs-3-primary factorization or the use
of `pi_3^s = Z/24`. What we have not found is the **inverse** reading used here -- that the no-go obstructions
and chiralizing selectors live entirely in the 2-primary `Z/8` summand, so the 2-primary no-go is arithmetically
**blind** to any 3-primary count (Wang *forces* `N_gen in 3Z`; we show a no-go *cannot* force it) -- together
with the Clifford-RS embedding. For Theorem 2 itself we claim no novelty beyond its application: its
mathematical core (a maximal definite subspace of a form pairing two complementary Lagrangians is a graph,
hence balanced) is elementary and of a classical Krein-space kind, the vectorlike character of real/pseudoreal
matter is standard representation theory, and indefinite-metric (Krein) formulations of the Standard Model with
an explicit generation space already exist in the noncommutative-geometry literature (the Lorentzian spectral
Standard Model, e.g. arXiv:2010.04960). What we claim is the specific assembly: that theorem, on this carrier,
feeding the two-arena reading.

---

## 11. Status of claims

| Claim | Grade |
| --- | --- |
| The no-go is 2-primary (no odd-prime congruence) | theorem (theory-independent) |
| CRT two-arena reading (`pi_3^s = Z/8 (+) Z/3`, summands disjoint) | decomposition standard; the two-arena structural reading is the contribution, under the torsion-count reading |
| Linear Krein-isometric operators conserve the net chiral index | theorem (machine-verified) |
| The unique escape is antilinear (class-CII type) | corollary (Wigner) + machine-verified |
| The antilinear chiralizer is frame-trivial, couples gauge (selector arena) | computed-confirmed; frame-triviality is evadable only into a 2-primary, index-conserving linear channel |
| No interior operator found forces an odd chiral count; the count is external on present evidence | class-level structural no-go (GU-independent); linear leg theorem-grade (index conservation), antilinear non-existence a finite adversarial hunt (exhaustive proof open) |
| Forcing an odd count requires an external net-self-dual chiral background | computed; a natural ingredient of the general kind that produces chirality in known chiral theories, but an external input; does not by itself pin 3 |
| Tangential `Lambda^2_+` framing carries `e_R = 1/12`, order 3 (carrier arena) | standard-result-applied (Kirby-Melvin); GU identification reconstruction-grade |
| The carrier is vectorlike and homotopy-fixed (locates, does not fill) | computed-confirmed |
| The disjointness-implies-blindness reading (a 2-primary no-go cannot constrain a 3-primary count) is novel; the bare `24 = 8x3` split is not (cf. Wang `24/8=3`) | best-effort literature search; no precedent found (negative result) |
| The literal generation integer on GU's 14-manifold | GATED on the unbuilt source action |
| The only honest computable generation integer | 1 (Pati-Salam `Spin(7,7)`, computed; chain-relative -- one reduction chain among many) |
| `order-3-class -> integer-3` | OPEN; ill-typed as stated (`Hom(Z/3,Z)=0`); an integer needs a relative/rank home (the twisted-RS index) |
| Toy stabilized twisted RS sector fills the forcing slot | NO (computed); reaches <=2 of 3 properties; every integer 2-primary or 1 |
| "2+1" as a single additive count | numerology across disjoint frameworks (computed) |
| Carrier Dirac mass (the gate) | ALLOWED/vectorlike (computed); massive -> decouples to 0, massless -> modulus; neither is 3; forcing 3 needs the frame-trivial selector-side chiral projection |
| GU forces exactly three chiral generations | NOT claimed; no computed quantity in this program equals three |

---

## 12. Conclusion

We have isolated, in an explicit Clifford Rarita-Schwinger sector, a clean structural picture. The
generation/chirality no-go is built from 2-primary statements and is therefore arithmetically incapable of
constraining an odd count; the relevant homotopy group splits, by the Chinese Remainder Theorem, into a
2-primary selector arena and a disjoint odd-torsion carrier arena; every obstruction and every chiralizer
lives in the selector arena, while a homotopy count can live only in the carrier arena. We exhibited the
unique order-3 object in the carrier arena and showed by computation that it is tangential but vectorlike and
homotopy-fixed -- it locates the slot, it does not fill it (an interpretive summary under the torsion-count
premise; `Hom(Z/3, Z) = 0` blocks any literal class-to-count identification) -- and that the only count-*forcing* operator is
frame-trivial and couples to the selector arena. The one calculation that could yield an integer on GU's
actual geometry is gated on an unbuilt source action; the only honest computable integer is one.

We submit the 2-primary blindness theorem, the CRT two-arena structure, the index-conservation /
antilinear-escape theorem, the located order-3 carrier, and -- reopened GU-independently -- the **class-level
structural no-go** that no covariant operator found interior to a Clifford-RS sector of this type forces an odd
chiral count, as a GU-independent contribution: **a no-go that locates, and relocates the count
to external background data.** On present evidence the generation count is external, supplied by a net-self-dual
chiral background of the general kind that produces chirality in known chiral theories (chiral gauge couplings,
instanton zero-modes, `K3` / Calabi-Yau compactification); the `order-3-class -> integer-3` identification of
that external datum remains the single named open conjecture (a candidate category error) rather than a claim.
We do not claim three -- no computed quantity in this program equals three -- and the structural reason the
count is not internal is now computationally established for the whole class (modulo an open exhaustive
non-existence proof on the antilinear side). We request external review of both the core results and the open
bridge.

---

## Appendix: reproducibility

The representation-theoretic decompositions, the Krein signature, the index-conservation check, the
frame-charge / DECOUPLE computation, the boundary `e`-invariant controls, and the decider integers are
checked numerically in `tests/` and `tests/generation-sector/`, `tests/source-action/`, `tests/boundary-eta/`,
`tests/decider/` (the last reproduced by an independent from-scratch script, 26/26 checks),
`tests/forcing-slot/` (the toy RS forcing-slot test), `tests/carrier-mass/` (the Dirac-mass capstone),
`tests/hessian-z3/` (the dynamical test), and `tests/gu-independent/` (the class-level structural law), each
angle adversarially re-verified. The homotopy and
`e`-invariant facts are standard (Adams; Kirby-Melvin; Randal-Williams). The campaign's adversarial
deep-research reports and the per-result canon (`canon/two-primary-lemma.md`,
`canon/boundary-eta-of-mu-RESULTS.md`, `canon/three-generations-locate-not-force-CRT-RESULTS.md`,
`canon/single-decider-integer-index-RESULTS.md`, `canon/forcing-slot-toy-rs-RESULTS.md`,
`canon/carrier-dirac-mass-capstone-RESULTS.md`,
`canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md`) are in the
repository.

**Verification status.** By the project's own three-tier vocabulary, every result in this paper is at most
*internally established*: computed, independently re-derived from scratch, and adversarially reviewed *within
the same AI-directed process that produced it* (reproduced, not replicated). No result here is *externally
established* -- independently replicated, peer-reviewed, or signed off by a named specialist. Because internal
reviewers are spawned by the same process that produced the results, no internal step, however adversarial, can
cross that boundary; the request for external review is a request to cross it.

---

## Appendix: Reproducibility -- the Pati-Salam one-generation verification

The "only honest computable generation integer is one" of Section 8 rests on a self-contained group-theory
verification of GU's Pati-Salam chain, reproduced here for completeness. The script
`lab/active-research/pati_salam_chain_verification.py` (pure `numpy`) builds the `Spin(10)` chiral spinor `16`
from its weights `(+/-1/2)^5` with an even number of minus signs, embeds Pati-Salam by partitioning the rank-5
Cartan as `3 (color + B-L) (+) 2 (T_3L, T_3R)`, and computes hypercharge and electric charge from group theory
alone via

```
Y = T_3R + (B-L)/2,    Q = T_3L + Y,    n = 6Y.
```

Pushing all 16 weights through the branching

```
Spin(7,7) -> Spin(1,3) x Spin(6,4)
          -> Spin(1,3) x Spin(6) x Spin(4)
          ~= SL(2,C) x SU(4) x SU(2) x SU(2)
          -> SL(2,C) x SU(3) x SU(2) x U(1)
```

collapses the `16` to exactly one Standard-Model generation:

| Multiplet (SU3, SU2_L) | n = 6Y | dim | Identification |
| --- | --- | --- | --- |
| (3, 2)     | +1 | 6 | quark doublet Q |
| (3bar, 1)  | +2 | 3 | d^c |
| (3bar, 1)  | -4 | 3 | u^c |
| (1, 2)     | -3 | 2 | lepton doublet L |
| (1, 1)     | +6 | 1 | e^c |
| (1, 1)     |  0 | 1 | nu^c |

totalling `6 + 3 + 3 + 2 + 1 + 1 = 16` states, with `Tr Y = Tr Q = 0` (anomaly-free) and electric charges
`{0, +/-1/3, +/-2/3, +/-1}`. The integer label `n = 6Y` reproduces the GU draft's Section 11.3 table exactly; an
embedding-ambiguity probe confirms that the naive `B-L`-only hypercharge fails, so the standard
`Y = T_3R + (B-L)/2` embedding is forced. An independent explicit-Clifford cross-check
(`lab/active-research/verify_clifford_explicit.py`, with 32x32 gamma matrices satisfying the `SO(10)` Clifford
relations numerically) reproduces the same content and its exact CP conjugate (`n -> -n`, `3 <-> 3bar`).

**Scope: this is a one-generation *structural* verification, not a generation count.** What is verified is that
the `16` of `Spin(10)` carries exactly *one* anomaly-free Standard-Model generation, with the paper's hypercharge
assignments reproduced from first principles -- i.e. internal representation-theoretic consistency of GU's group
theory. It does **not** provide the generation count: it does not establish that nature realizes this breaking
pattern, does not address the effective-chirality or "2+1" claims, and -- being a single generation -- says
nothing about *how many* generations occur. Moreover the `Spin(7,7)` Pati-Salam chain is one reduction among
many possible symmetry-breaking chains; the "1" it yields is chain-relative, not chain-independent. It is the integer "1" of Section 8, and its role in this paper is
precisely that: the only honest computable generation integer, not a derivation of three.
