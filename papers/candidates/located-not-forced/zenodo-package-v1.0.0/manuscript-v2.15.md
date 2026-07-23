# Located, Not Forced: A Scoped Two-Primary Audit of a Clifford Rarita-Schwinger Generation Carrier

**Public preprint draft. This paper does NOT claim three generations.** The conditional mathematical
results do not require Geometric Unity to be physically correct, but the choice of carrier and its proposed
physical interpretation are GU-motivated; every GU-specific step is marked motivated or reconstruction-grade. Six
load-bearing caveats hold throughout: **(a)** the torsion-count reading is a *premise, not a result* -- under a
literal integer-index reading the same obstructions would instead *forbid* an odd count outright; **(b)** the
projected order-3 component cannot literally *be* an integer count, since `Hom(Z/3, Z) = 0` (no homomorphism from a torsion
group to a torsion-free one is nonzero); **(c)** the exact theorem domain `C_fin` is the encoded
fifteen-generator finite type; transfer to the broader semantic invariant class `C_inv` is computed for
C1--C5 but remains conditional for the named characteristic/analytic remainder; non-equivariant operators,
external backgrounds, and the
true-`Y14` source-action pushforward remain open, so externality is not proved; **(d)** Theorem 2 is a finite
Krein intersection-nullity theorem, not a physical handedness count, Hilbert-space positivity claim, or
Fredholm index. At canon grade, faithful stand-ins discharge the conditional APS/end/gap/family terms;
transfer to the true Rarita-Schwinger `Y14` bundle remains open; **(e)** the compact/complexified
`192`, `(96,96)`, and `(2,2,2,2,0)` packet is not silently identified with a physical Lorentzian real-form
packet: one Lorentzian Hodge half is `192`-dimensional but Krein-null and is exchanged by physical
conjugation, while the computed conjugation-stable closure is `384`-dimensional with signature
`(192,192)`; **(f)** every verification reported here is *internal* -- computations reproduced from scratch and
adversarially reviewed within the same AI-directed process that produced them; no result has yet been
externally replicated or peer-reviewed. External review is welcome but is not a prerequisite for public
Zenodo deposit; it is required before describing the work as externally validated. See Sections 1 and 9.

*Canonical release source: this Markdown file. The adjacent
[`located-not-forced-generation-count-2026-06-29.tex`](located-not-forced-generation-count-2026-06-29.tex)
is mechanically generated from it for the v2.15 release and must remain semantically aligned.*
Suggested classification: primary **hep-th**; secondary
**math-ph**, **math.AT**. Keywords: generation number, family puzzle, Rarita-Schwinger, primary decomposition,
index theorem, framed bordism, Adams e-invariant, anomaly inflow, chirality.*

Internal version 2.15, 2026-07-23. This hardening pass separates `C_fin` from
`C_inv`, retypes the Lean theorem by codomain, formalizes the finite complex
Krein lemma, audits the physical Lorentzian real-form transfer, fixes the full
framing convention chain, and replaces the historical claim map with a
machine-validated current ledger. Detailed history is retained in the
adjacent changelog and review files rather than in the manuscript.

---

## Abstract

We study the chirality and generation structure of an explicit Clifford Rarita-Schwinger sector: the
gamma-traceless rank-3/2 field built in a 128-dimensional **complex** Dirac-spinor model of
`Cl(p,q)`, `p+q = 14`, with one Standard-Model family carried by the `16` of `Spin(10)`. For the physical
`Cl(9,5) = M(64,H)` real form, the irreducible real module is `H^64` (real dimension 256); the
128-by-128 complex matrices used here are its complex realization, and all unqualified carrier dimensions
below are complex dimensions. The sector is motivated by, and
reconstructed from, the matter proposal of Geometric Unity (GU); every GU-specific step is marked, and none
of the conditional finite-dimensional deductions depends on GU being physically correct.

We prove a codomain-separated **two-primary finite-census theorem** for `C_fin`, the explicitly encoded
fifteen-generator finite type: finite torsion constraints are 2-primary; integer equality/divisibility rows,
representation dimensions, and diagnostics remain in distinct codomains; and no constructor supplies a
mod-3 congruence or selects a particular odd integer. A computed C1--C5 lift relates this finite type to the
broader semantic invariant class `C_inv`, but the unrestricted characteristic/analytic lift remains open.
Listed first-step departures are controls, not an exhaustive classification beyond `C_fin`. We also prove a
finite **Krein intersection theorem** on the compact/complexified `(96,96)` packet: a maximal positive subspace
intersects each chiral Lagrangian trivially. This does not count the physical left-minus-right handedness of
its vectors and is not a Fredholm index. The physical-signature audit keeps one Lorentzian Hodge half at
complex dimension `192`, but finds that it is Krein-null and exchanged by physical conjugation; its
conjugation-stable closure has complex dimension `384` and signature `(192,192)`.

The standard decomposition `pi_3^s = Z/24 = Z/8 (+) Z/3` separates torsion data already mapped into those
summands. It does not move the paper's integer-valued constraints into `Z/8` or an integer generation count
into `Z/3`; those maps are absent. We exhibit a framed class with a nonzero 3-primary component -- the framed-bordism
Adams `e`-invariant `e_R = 1/12` carried by the self-dual `Lambda^2_+` tangential framing on the `RP^3` spine
of the metric fiber. The full class `2 in Z/24` and `e_R = 1/12 in Q/Z` have order 12; only the projected
`Z/3` component has order 3
-- and we show by explicit computation that it is **tangential but vectorlike and homotopy-fixed**: it
locates the 3-primary slot without filling it with a count ("locates" is an interpretive gloss under the
torsion-count premise of caveat (a), not a further computed quantity; by `Hom(Z/3, Z) = 0` the located class
cannot itself be a count).

We then attempt a direct candidate calculation for an integer count on GU's actual 14-manifold and find
it **gated** on an unbuilt object (the stabilized twisted Rarita-Schwinger source action). A reconstructed
Pati-Salam `Spin(7,7)` branch verifies that one `Spin(10)` `16` contains one Standard-Model family; this is a
family-unit normalization, not an observable that counts how many such families occur. A toy of the missing source action,
built and adversarially tested four ways, does **not** fill the forcing slot -- every tested integer is even
or one -- but this remains bounded negative evidence. None of the `C_fin` constructions or listed
controls supplies a typed integer generation count. We do not infer that the count is necessarily external,
because non-equivariant operators and the true Rarita-Schwinger `Y14` source-action pushforward remain open.
We therefore do **not** claim three generations.
We claim a scoped non-derivation that *locates*: after an explicit map into `Z/24`, a 2-primary image cannot
determine the separate `Z/3` component; the exhibited framed class has a nonzero 3-primary projection. We pose the
`3-primary torsion component -> integer 3` identification as the single named open conjecture (and a candidate
category error). Primary decomposition and positive uses of its 3-primary content are prior art. The
search-bounded candidate delta is only the carrier-specific inverse assembly: the explicit compact/complexified
cross-chirality
Clifford-RS carrier, a scoped 2-primary sector-interior result, and the inference that those data cannot
determine the separate 3-primary torsion component. External review of both the core results and the open
bridge is invited as an optional later validation stage.

---

## 1. Introduction

The Standard Model contains three generations of fermions and does not explain the number. A recurring hope
in unification is that the number is fixed by topology. The obstacle, made precise here, is that the natural
index- and anomaly-theoretic invariants one computes *in this sector* are predominantly **2-primary**:
mod-2 Witten anomalies, mod-16 topological-superconductor classifications, even-valued Dirac indices. A
2-primary torsion invariant cannot select a 3-primary class through the group structure alone; an
integer-valued zero or evenness constraint can instead forbid an odd count. (Where the literature *does* obtain an odd
constraint -- Garcia-Etxebarria-Montero's `Z_9 -> N_gen in 3Z` is the sharpest example -- the constraining
anomaly is itself genuinely 3-primary, consistent with the thesis that an odd count requires 3-primary input.)

This paper turns that obstacle into a positive structural statement, in one explicit sector, and then tests
the strongest possible reading of it by direct computation. Our contributions:

1. **A codomain-separated 2-primary finite-census theorem (Section 4).** No item in the exact `C_fin` type
   supplies an odd-prime congruence or selects a particular odd integer. Finite torsion rows are 2-primary;
   integer rows remain `Z`-valued parity/divisibility constraints; dimensions and diagnostics remain
   separately typed. The C1--C5 lift toward `C_inv` is computed, while the broader lift and listed outside
   controls are not an exhaustive classification.
2. **A CRT two-arena structure (Section 5).** `pi_3^s = Z/24 = Z/8 (+) Z/3` splits, by the Chinese Remainder
   Theorem, into disjoint summands. If an explicit map places a finite sector constraint in `Z/8`, that image
   cannot determine the separate `Z/3` component. No such statement is made for the `Z`-valued rows or an
   integer generation count.
3. **A finite Krein intersection theorem and bounded operator audit (Section 6).** Every strictly K-positive
   subspace intersects each chiral Lagrangian trivially, and linear K-isometries preserve that nullity. This is
   not a physical handedness count. The same intersection statement holds for a delimited class of antilinear
   K-null re-gradings. No `C_fin` construction supplies the missing integer generation operator;
   unrestricted and true-`Y14` constructions remain open.
4. **A located 3-primary carrier (Section 7).** The self-dual `Lambda^2_+` tangential framing on the `RP^3`
   spine carries `e_R = 1/12`. The full class has order 12, while its projected `Z/3` component is nonzero and
   has order 3. It is shown by computation to be tangential but vectorlike and homotopy-fixed: it locates, it
   does not fill ("locates" is an interpretive gloss under the torsion-count reading, not an additional
   computed quantity).
5. **The deciding computation, and the gate (Section 8).** The integer count on GU's actual 14-manifold is
   gated on the unbuilt twisted Rarita-Schwinger source action. The explicit Pati-Salam branch normalizes one
   `Spin(10)` `16` to one Standard-Model family but does not count the number of copies.
   We do not force three.
6. **The open conjecture (Section 9).** `3-primary torsion component -> integer 3` is a theorem of nothing in the present
   literature and is a candidate category error. We state it as the single open bridge and invite review.

The robust content is conditional mathematics about an explicitly specified carrier: the codomain audit,
finite intersection theorem, standard CRT decomposition, and framed-class calculation. The selection of
that carrier, its GU identification, and the generation-count reading are clearly marked motivated,
reconstruction-grade, or open.

---

## 2. The setting

For the computational model, let `S_C` be the 128-dimensional complex Dirac-spinor realization of
`Cl(p,q)`, `p+q = 14`. In the physical `(9,5)` real form this is the complex realization of
`S_R = H^64`, `dim_R S_R = 256`; it is not a 128-dimensional real Clifford module. The
Rarita-Schwinger carrier is the gamma-traceless part of `V_C (x) S_C`; the constraint cuts
`V_C (x) S_C` (complex dimension `14*128 = 1792`) to `ker(Gamma)`, of complex dimension
`(14-1)*128 = 1664 = 2^7 * 13`.

We split `14 = 4 + 10`: a four-dimensional base `X^4` and a ten-dimensional internal space, with one
Standard-Model family carried by the `16` of `Spin(10)`. The explicit compact calculation uses
`Spin(4) = SU(2)_+ x SU(2)_-`; its self-dual two-forms `Lambda^2_+` generate `su(2)_+`. For a Lorentzian
`(3,1)` base, `*^2 = -1` on real two-forms, so the self-dual/anti-self-dual rank-three splitting exists only
after complexification (or after a stated Wick rotation/maximal-compact reduction). The paper uses that
complexified/compact representation calculation; transfer of the proposed family interpretation to the
physical Lorentzian bundle is reconstruction-grade, not silently identified with the Euclidean statement.
Under the compact `su(2)_+` calculation,

```
ker(Gamma) = 640 (singlets) + 832 (doublets) + 192 (triplets),
```

verified numerically (`tests/generation-sector/h1_selfdual_family_kill.py`). The complex
`192`-dimensional `j=1` sector is the multiplicity-three structure in this computational model. More precisely, its
two total-chirality blocks have the form `(3,2,16)` and `(3,2,16bar)`, each of complex dimension 96. The relevant
invariant Hermitian form is the `so(p,q)`-invariant Krein form `K = eta_V (x) beta_S`; on the triplet it is purely
cross-total-chirality, Hermitian signature exactly `(+96, -96)` in the compact baseline. This is an indefinite
Krein statement, not a physical
left-minus-right state count. The sector is multiplicity-three, while a typed physical chirality operator or
index remains separate and unbuilt.

**Physical-real-form discriminator.** Direct construction with the
`(3,1)+(6,4)` split preserves the complex dimension `192` and the `96+96`
total-chirality branching for either Hodge-star half, but each half is
Krein-null and physical quaternionic conjugation exchanges the two halves.
Their conjugation-stable closure has complex dimension `384` and Krein
signature `(+192,-192)`. Physical conjugation preserves total
14-dimensional chirality while swapping base and internal chirality
separately. Thus the compact packet is the exact premise of the finite
theorems below; selection of a physical carrier on the true `Y14` bundle
remains reconstruction-grade.

---

## 3. Multiplicity versus chirality

The integer 3 plays two arithmetically different roles in this sector, and conflating them is the error the
"located, not forced" reading most guards against. A **multiplicity** is the dimension of a flat family space --
the number of copies of a fixed representation the constrained module carries; it is a representation dimension,
comes with its mirror (copies and anti-copies), and is vectorlike. A **net chiral count** is an index -- the
signed difference (left minus right) of Dirac zero modes; it measures chirality, the property a vectorlike
spectrum lacks. A representation dimension and an operator index are not one number computed two ways. This sector
supplies the first natively and does not supply the second.

**The multiplicity is three in the compact/complexified carrier calculation (verified).** Under the
self-dual `su(2)_+` used in Section 2, the
gamma-traceless module decomposes as in Section 2. Written by *multiplicity* rather than dimension,

```
ker(Gamma) = 640 (j=0) + 416 (j=1/2) + 64 (j=1),   640*1 + 416*2 + 64*3 = 1664,
```

i.e. 640 singlets, 416 doublets and 64 triplets, the 64 triplets spanning the complex
192-dimensional `j=1` sector of Section 2. On all 192 complex states the `Spin(10)` Casimir matches the
reference `16 / 16bar` value to machine precision
(`tests/generation-sector/h1_selfdual_family_kill.py`). A multiplicity-three object therefore exists in the
specified carrier calculation; the representation dimension 3 is not inserted as a target. Its transfer from
the compact/complexified self-dual calculation to the physical Lorentzian GU bundle has the
reconstruction-grade scope stated in Section 2.

**Lemma (irreducible spinor dimensions are 2-primary).** *A single irreducible complex Dirac or half-spinor
representation of `Spin(m)` has power-of-two dimension and hence no factor of 3. Consequently, any factor of
3 in a family multiplicity cannot come from the dimension of one such irreducible spinor; it must come from
the number of spinor copies or from a non-spinor family representation.*
The complex Dirac spinor has dimension `2^floor(m/2)` and each complex half-spinor of `Spin(2k)` has
dimension `2^(k-1)`; all are powers of two. Dimensions of direct sums add, so the original stronger wording
for an arbitrary “sum of spinors” would be false (three copies already supply a factor of 3). The vector,
adjoint, and self-dual tensor dimensions are not power-of-two constrained; in the compact four-dimensional
calculation, `Lambda^2_+` has complex dimension 3. QED.

**Three is the canonical odd multiplicity (verified for the commutant of the full `Spin(10)`).** The lemma turns
an open-ended search into a narrower audit: an irreducible spinor dimension is 3-free, so any factor of 3
must enter through copy multiplicity or a non-spinor channel. Inside the compact branching
`Spin(14) ⊃ Spin(10) x Spin(4)` the commutant of `Spin(10)` is
`so(4) = su(2)_+ (+) su(2)_-`, which up to conjugacy has exactly three `su(2)` subalgebras (self-dual,
anti-self-dual, diagonal), and no `su(3)` embeds (by dimension, `dim su(3) = 8 > 6 = dim so(4)`). Enumerating the
16-dimensional multiplicity space under each (`tests/generation-sector/leg3_family_embedding_enumeration.py`),
only the self-dual and anti-self-dual `su(2)` (orientation images of one another) give an odd multiplicity, always
the triplet of dimension 3, never a quintet or higher; the diagonal choice gives an all-even content. So for
family symmetries commuting with the full `Spin(10)` the self-dual route is the unique odd-dimensional route
in that enumerated commutant, and the odd irrep it contains is a triplet. *This is a statement about a
representation dimension in the stated compact branching, not a net chiral count or a Lorentzian transfer
theorem.* The case of a
family symmetry commuting only with the Standard-Model subgroup `G_SM ⊂ Spin(10)` -- whose larger commutant could
in principle host a horizontal `su(3)` -- is not covered here and is a bounded open computation; the lemma already
constrains the irreducible-dimension part of that search.

**But the triplet does not by itself supply a chiral count.** The invariant Krein form
`K = eta_V (x) beta_S` on the compact/complexified triplet is purely cross-total-chirality with signature
`(+96, -96)`. Theorem 2 proves
only a finite Krein-side intersection nullity: a maximal K-positive subspace contains no nonzero vector lying
wholly in either chiral Lagrangian. It does not count the handedness of the 96 physical vectors, because a
generic graph vector has components in both chiral spaces. Turning the specified multiplicity three into a net
physical three therefore requires a separately typed grading-invariant subspace, graded trace, or Fredholm/index
construction, none of which is supplied by this finite carrier argument. **The multiplicity-three irrep is
present in the specified compact/complexified carrier; a physical Lorentzian chiral count is not derived
here.**

---

## 4. Theorem 1: a codomain-separated 2-primary finite census

A finite torsion invariant is **2-primary** when it is annihilated by a power of two. An integer-valued
constraint is called **2-adic/parity-valued** here only when its content is divisibility by a power of two.
These are different codomains: a `Z`-valued equality or index is not an element of `Z/8` unless an explicit
reduction or torsion-valued map is supplied.

**Theorem 1 (complete for `C_fin`).** *Let `C_fin` be the fifteen-constructor finite type encoded in
`Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`, together with finite product, gcd, and lcm expressions
over its torsion-valued atoms. Its finite-torsion rows have moduli `2`, `2`, and `16` and remain 2-primary
under those operations. Its integer equality and divisibility rows remain `Z`-valued; its representation
dimensions and rank diagnostics remain in their own codomains. No constructor has the codomain of a selected
generation integer, and no encoded finite-torsion modulus has an odd-prime divisor. In particular, `C_fin`
supplies neither a mod-3 congruence nor a particular odd integer.*

The broader semantic class `C_inv` denotes all linear or antilinear structures on the fixed carrier that are
equivariant under the stated split symmetry and use only sector-internal data. The compact carrier computation
provides a bounded C1--C5 lift into `C_fin`; C6 is certified only as the seven named characteristic/arithmetic
rows, not as a classification of every possible sector characteristic construction. Completeness over
unrestricted `C_inv`, the physical Lorentzian bundle, external backgrounds, added gauge twists, and the
function-space/Fredholm setting remains open. Listed gauge-twist, boundary/`eta`, composition, and
dressed-pairing departures are controls rather than a classification; odd primes appear after importing
outside data (`54 -> 3`, `120 -> 7`, `126 -> 5.7`).
(The loose "even" reading is near-vacuous -- `96 = 2^5 . 3` is even; the content is the modular statement, that no
enumerated obstruction is a mod-odd-prime condition.)

| Boundary | Exact `C_fin` theorem domain | Conditional `C_inv` target | Outside both |
|---|---|---|---|
| Carrier | Fifteen encoded generators over the compact/complexified carrier packet | All invariant structures on that fixed carrier, subject to a proved/computed lift | Added fields, representations, spurions, or a different physical carrier |
| Maps | Encoded linear, bilinear, sesquilinear, antilinear, and named characteristic rows | All linear or antilinear maps equivariant under the stated split symmetry | Non-equivariant maps or an added global/discrete symmetry such as `Z/9` |
| Data | Three finite-torsion rows, one integer-equality row, one integer-divisibility row, one representation-dimension row, and one diagnostic row | Other sector-internal invariant data, if normalized to the finite constructors | External backgrounds, non-sector gauge twists, or background expectation values |
| Analytic setting | Finite carrier arithmetic only | Finite invariant carrier theory | Section-space, Fredholm, APS/family-index, and true-`Y14` source-action data |

Here **outside** means outside the theorem's quantified class, not impossible or physically inadmissible. The
extension engine tests several first-step departures from `C_fin` as adversarial controls; odd-primary factors appear
only after importing data on the OUT side of this boundary.

**Completeness certificate and proof boundary.** “Complete” means complete for the finite generator type
`C_fin`, not complete for every map satisfying the semantic `C_inv` prose by definition alone. The
exact/computed compact-carrier scripts
`tests/enum-completeness/enum_class_c_generators.py` and
`tests/enum-completeness/verify/indep_check.py` supply the two-block Schur-matching packet
`2/2/2/2/0`; `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean` proves exhaustiveness, row assignment,
and product/gcd/lcm closure only for genuinely torsion-valued atoms. It types integer equality/divisibility,
representation dimensions, and diagnostics separately, and its CRT projection API accepts only an explicit
torsion-valued map into `Z/24`. Lean does not reconstruct the matrices or prove physical carrier faithfulness.
The bounded lift and its open exits are recorded in
`review/V15-2-cfin-cinv-lifting-audit-2026-07-23.md`.

**Proof (enumeration and codomain audit, conditional on that certificate).** (1) Kramers / quaternionic wall (`J^2 = -1`): a `Z/2` statement.
(2) Real / pseudoreal non-chirality: the mod-2 Witten index, `Z/2`-valued. (3) Cross-chirality Krein
signature: the finite intersection-index nullity of Theorem 2, a `Z`-valued equality rather than a torsion
class or physical handedness count. (4) Adjoint Dirac indices `4k`, `12k`, and `24k`: `Z`-valued divisibility
statements, not elements of `Z/8`. (5) Rokhlin: `sign(X) = 0 (mod 16)`, mod `2^4`.
(6) Irreducible spinor dimension: a single complex irreducible Dirac or half-spinor has power-of-two
dimension; a factor of 3 must therefore enter through copy multiplicity or a non-spinor representation.
(7) Ghost parity: a ghost-parity
resolution of the Krein hyperbolic pairs yields a tested `50/50` rank diagnostic. No item supplies a mod-3
congruence or selects the integer three. The integer rows can forbid an odd value under a literal
integer-index reading; they cannot be moved into `Z/8` without an additional map. QED.

*Remark.* The integer 3 does appear in the sector -- as a multiplicand (`96 = 2^5 . 3`, `12k`, `24k`,
`|Weyl(D7)|`). Theorem 1 is not "no factor of 3 occurs." It says only that no encoded constraint supplies an
odd-prime congruence or selects a specific odd integer, with `Z`-valued and torsion rows kept separate.

*Remark (finite equivariant backstop, 2026-07-03, exploration-grade).* For the tested
`so(4) (+) so(10)`-equivariant finite carrier, full chirality is central in the even Clifford algebra. By
Schur, each irreducible summand sits wholly in one chirality, and the tested count lattice is
`{ sum_R d_R (k_R - l_R) }`. Every appearing irreducible in this decomposition has even dimension, so this
specific equivariant lattice is even. This corroborates the compact `C_fin` census; it does not classify
non-equivariant operators, alternative physical state spaces, or function-space/source-action constructions
(`explorations/big-swing-2026-07-03/R1-rs-operator-residual-and-odd-count-nogo.md`,
`tests/big-swing/R1_kill_odd_index_isotypic.py`, exit 0).

---

## 5. The CRT two-arena structure

`pi_3^s = Z/24`, with primary decomposition `Z/24 = Z/8 (+) Z/3`. Adams' image-of-`J` theorem gives, in
stem `4s-1`, that `Im J` is cyclic of order `denom(B_{2s}/4s)`; for `s=1` this is `24`, so `Im J_3 = Z/24`
and the Adams `e`-invariant detects it.

**The central structural fact and its limit.** By the Chinese Remainder Theorem the splitting
`Z/24 = Z/8 (+) Z/3` is into disjoint summands: there is no nonzero homomorphism `Z/8 -> Z/3` or
`Z/3 -> Z/8` (`canon/two-arena-rep-theory-core-RESULTS.md`). This applies to torsion-valued data already
mapped into `Z/24`. It does not place the `Z`-valued equality/index rows of Theorem 1 into `Z/8`, and it does
not place an integer generation count into `Z/3`. Both transfers require additional maps not constructed here.

**Corollary (conditional torsion statement).** If an explicit map sends a sector constraint into the `Z/8`
summand of `Z/24`, then that image cannot determine the separate `Z/3` component through the group structure
alone. This is a statement about mapped torsion data, not an integer generation count.

Under a literal integer-index reading, a zero or evenness constraint may instead forbid an odd count. Thus the
program-native torsion reading and physics-default integer reading fork; neither transfers to the other.
`Hom(Z/3,Z)=0` blocks a direct class-to-count map. “Selector arena” and “carrier arena” are retained only as
mnemonics for the two torsion summands, not as types assigned to every obstruction or to the generation count.

---

## 6. Theorem 2: a finite Krein intersection invariant

For a strictly K-positive complex subspace `P`, define the finite
**intersection difference**
`Delta_cap(P) = dim_C(P intersect W_+) - dim_C(P intersect W_-)`.

**Theorem 2.** *For a finite-dimensional complex vector space with a nondegenerate Hermitian form K, every
strictly K-positive subspace has `Delta_cap(P)=0` relative to two totally K-isotropic subspaces `W_+` and
`W_-`; a complex-linear K-isometry preserves this nullity after transporting all three subspaces.*

**Proof.** If a nonzero vector lay in both `P` and either totally K-isotropic subspace, its Hermitian
quadratic value would be simultaneously strictly positive and zero, a contradiction. Hence both intersections
are trivial and their complex dimensions have difference zero. A complex-linear K-isometry transports strict
positivity and total isotropy. QED.

**Scope.** This is finite-dimensional Krein linear algebra. It does not prove a physical chiral state count,
a graded trace, spectral flow, or a Fredholm index. At canon grade, faithful stand-ins discharge the
APS/end/gap/family terms for a separately stated conditional section-setting model; transfer to the true
Rarita-Schwinger `Y14` bundle/source-action pushforward remains open.

The abstract intersection implication is Lean-checked in
`Lean/GUFormalization/LocatedNotForcedLegs.lean` directly over a complex sesquilinear Hermitian form and is
conditional on supplied positivity, isotropy, nondegeneracy, and finite-dimensionality premises. Lean does
not construct the compact `192`-dimensional carrier or certify those premises; the numerical scripts test
them. Existing numerical scripts also report equal projection-image
ranks on graph subspaces. That is a
separate balance diagnostic, not a count of 96 left states minus 96 right states.
The numerical signature cross-check reproduces the same-chirality block nullity and zero projection-rank
difference in `(9,5)` and `(7,7)`; a grading-aligned Euclidean `(14,0)` control gives projection-rank difference
`96`. These are diagnostics and controls, not physical handedness indices.

**Physical-signature boundary.** The compact/complexified `192`-space supplies
the `(96,96)` theorem instance above. On one physical Lorentzian Hodge half,
the computed Krein restriction is zero, so that object does not instantiate
the same premise packet. The conjugation-stable `384`-space has signature
`(192,192)` and could instantiate the abstract theorem only after the relevant
grading and physical subspace are typed. No such true-`Y14` selection is
claimed here.

**Antilinear audit boundary.** The finite theorem does not invoke Wigner's Hilbert-space ray theorem or make
antilinearity a unique physical escape. For a separately delimited class of antilinear re-gradings whose
**images of the original chiral subspaces** are K-null, the same intersection index relative to those images
remains zero. This avoids treating complex eigenspaces of an antilinear map as ordinary linear eigenspaces.
The result is still Krein-side nullity, not a
physical handedness count.

**A GU-motivated re-grading candidate is frame-trivial (computed).** The operator `C = J_quat . G` is built from
`J_quat = id_14 (x) U` (the quaternionic structure) and the chiral grading -- both internal-fiber
endomorphisms. Its tangent-frame charge is **exactly 0**:
`max ||[J_quat, any tangent-frame so(9,5) rotation]|| = 0.00e+00`, including the `Lambda^2_+` rotation;
`|<J_quat, Lambda^2_+>| = 0`. The structural reason is that `id_14 (x) U` acts trivially on the frame
factor, so its commutator with frame rotations vanishes; the random-`U` run is only a numerical control, not
the proof of convention independence. Consequently this candidate carries no frame `p_1` in this construction,
and its reduced boundary
`eta` is the 2-primary gauge type (`(2q^2-4q+1)/8`, here forced to 0 by `C^2 = -I`). The calculation supplies no
integer generation count. The denominator-eight diagnostic does not by itself define a map from this operator
to the `Z/8` summand of `Z/24`.

**Bounded operator audit.** The `C_fin` and first-step-control calculations found no operator that constructs
an integer generation count. A frame-active linear overlap `O = L_SD (x) X_L` exists, so the stronger claim
that frame charge and chirality support are orthogonal is false. Its reported `+16` and `+2` are
subspace-restriction/overlap diagnostics, not a conserved physical chiral index. This audit is complete only
for the encoded compact equivariant packet and the listed controls; it does not quantify over unrestricted,
non-equivariant, or function-space constructions.

For antilinear re-gradings whose images of `W_+` and `W_-` are K-null, the delimited calculation proves the
same intersection nullity as Theorem 2. Frame-nontrivial antilinear swap operators exist once symmetry is
dropped; the theorem says only that those K-null image subspaces have zero intersection index. It does not identify that
index with a physical handedness count and does not close K-definite, unrestricted, or true-`Y14`
source-action constructions.

**What remains open.** External chiral backgrounds are one standard way to produce an integer index: a 2D
magnetic-flux Wilson-Dirac model realizes net chiral index = flux number
(`canon/external-topological-index-flux-RESULTS.md`). The present finite `C_fin` audit does not prove that
external data are necessary, because it does not cover non-equivariant operators or the true
Rarita-Schwinger `Y14` bundle/source action. The supported conclusion is narrower: none of the encoded
sector-interior constructions supplies a typed integer generation count, and the missing map/operator is
named rather than inferred away.

---

## 7. An exhibited 3-primary carrier

The paper exhibits 3-primary content in the following place; it does not prove uniqueness over untested
channels. Under the reconstruction that reads the self-dual `SU(2)_+ = Lambda^2_+` structure as a
**tangential** framing on `RP^3 = L(2;1)` (the deformation-retract spine of the metric fiber
`GL(4,R)/O(3,1)`), the resulting framed classes are `+2` and `-2=22` in
`pi_3^s = Z/24`, with Adams `e`-invariants

```
e_R = +/- p_1/48 = +/- 1/12   (p_1 = +/- 4; each full class has order 12).
```

Their exact CRT coordinates are `2 -> (2 mod 8, 2 mod 3)` and
`22 -> (6 mod 8, 1 mod 3)`. The embedded 3-primary representatives are
respectively `8` and `16` in `Z/24`, each of order 3. Thus the sign convention
changes the representative but not nonvanishing or order.

The stabilization `pi_3(SO(3)) -> pi_3(SO)` is `x2`, so the stable degree is `p_1/2 = 2`, not the Dynkin
index 4. This is standard topology assembled from three stated conventions -- the generator of `H^4(BSpin;Z)`
(McLaughlin; Sati-Shim), the `x2` stabilization and framing normalization (Kirby-Melvin), and Adams'
`e_R` normalization; the composite `e_R = (p_1/2)/24` is ours, not a formula quoted verbatim from any one
source. Only the identification of GU's
`Lambda^2_+` twist with this natural tangential framing is reconstruction-grade.
The exact internal sensitivity audit enumerates all orientation/generator/Adams sign combinations and the
common factor-of-two alternatives. No viable convention for the same framed cycle erases the 3-primary
projection. A gauge/coefficient reading or a genuinely different stable framing can erase it, but either
changes the load-bearing GU-to-natural-framing premise. External specialist review remains a useful optional
validation target rather than a gate on Zenodo publication.

**It locates but does not fill (properties computed; "locates" is interpretation).** The carrier `Lambda^2_+`
is tangential in the stated framing reconstruction (`p_1 = 4`) and is vectorlike in the tested finite
representation. We omit the basis- and normalization-dependent numerical overlap previously called a
“frame charge”; it is not a topological invariant and adds no evidence beyond the stated framing
calculation. Meanwhile `e_R = 1/12` is **homotopy-fixed**: it is a fact about `pi_3^s`, identical for
a universe with one generation or five. So the carrier marks the 3-primary slot; it does not co-vary with the
answer and so cannot, by itself, be the thing that counts to three. A negative control shows that the tested
`RP^3` deck/gauge channel does not supply a 3-primary component: its deck group is `Z/2`, and the charge-`q`
Dirac `eta = (2q^2-4q+1)/8` is 2-primary for every integer `q`. This does not prove uniqueness among untested
channels.
Throughout, "locates the slot" is an interpretive gloss under the torsion-count premise (Section 5), not an
additional computed quantity: the computed facts are the tangentiality (`p_1 = 4`), finite-model
vectorlikeness/balance diagnostics, and homotopy-fixedness; and by `Hom(Z/3, Z) = 0` (Section 9) the located class cannot itself
*be* an integer count.

The computed picture is therefore limited but useful: the frame-trivial re-grading candidate and the
frame-charged class are distinct objects, and the latter has a nonzero 3-primary projection. Neither object is
a typed integer generation count, and no direct class-to-count map exists.

---

## 8. The deciding computation, and the gate

A direct candidate computation that could produce an integer count on GU's *actual* geometry, rather than a
homotopy-fixed class identical for any answer, is the net chiral index as the anomaly-inflow coefficient of
the bulk gravitational `-p_1/24` SPT class on the 14-manifold, with the tangential-vs-gauge fork resolved by
the computation. We constructed and ran a gate audit of the available finite, characteristic-class, and
toy-model inputs (`tests/decider/`, 26/26 checks across four scripts plus an independent from-scratch
re-verification, exit 0, all controls reproduced). We did **not** construct the actual global operator whose
index would answer the question. The gate audit found:

- **The literal net-chiral integer is GATED** on the unbuilt stabilized twisted Rarita-Schwinger / IG source
  action (the `+8` Rarita-Schwinger leg of `ind_H = 8*A-hat(K3) + 8`). Every analytic route to it failed
  (ten Atiyah-Singer routes gave `{960, -288, -384, -192, -336, -128, 128, -8, -480, 60}`, none `= 16`); the
  computation explicitly refused it rather than fabricating a fit.
- **The explicit family-unit normalization is one, not a generation-count observable.** A reconstructed
  Pati-Salam `Spin(7,7) -> Spin(6) x Spin(4)` branch decomposes one `Spin(10)` `16` into exactly one
  Standard-Model family and verifies the listed linear traces `Tr Y = Tr Q = 0`
  (`16 // 16 = 1`; "2+1 effective"). Full Standard-Model anomaly cancellation is standard for the
  `16`, but the paper harness directly checks only these displayed trace and charge identities. The branch is
  one reduction among many possible symmetry-breaking chains, and `16 // 16 = 1` normalizes a family unit; it
  does not determine how many copies nature or the source action supplies. The spin-1/2 leg is
  `8*A-hat(K3) = 16`, with `A-hat(K3) = 2` the "2" of "2+1". The tested outputs include
  `{0 (linear net-chiral, vectorlike), 1 (Pati-Salam family-unit normalization), 2 (A-hat(K3))}`; none is a
  derived generation count of 3.
- **The tested re-grading candidate has a denominator-eight boundary diagnostic** (`e = 3/8`, 3-part zero)
  and is frame-trivial. This does not define an integer count or a canonical map into the `Z/8` summand.

Under the decision rule fixed in advance, the strong reading fails: the sought integer is gated, while the
explicit Pati-Salam calculation only normalizes a single `16` as one family. Controls reproduced exactly:
`ch_2(S_X)[K3] = -5376 = -2^8 . 3 . 7` (the apparent "24" is a disguised `chi(K3)` import via `2chi+3sigma=0`,
rejected; a `chi`-route gives `ch_2 = 0`); `A-hat(K3) = 2`; the charge-`q` `eta` family; Pati-Salam `-> 1`.

**Gated, not fabricated.** Four things remain genuinely gated and are marked as such: (i) the `+8`
RS leg / the literal integer, on the unbuilt source action; (ii) the full analytic Bismut-Cheeger
fibered-boundary reduction theorem for the non-product 9-dim `S^6`-bundle over `RP^3` (the machinery is a
theorem and the even-fiber transparency `A-hat[S^6] = eta(S^6) = 0` is computed, but its application to GU's
actual twisted-RS boundary operator is gated; "the spine is `RP^3`" is not that theorem); (iii) the families
pushforward `pi_! : ch(S)/Y14 -> ch(S_X)/X4`, which is not defined because the fiber `GL(4,R)/O(3,1)` is
non-convex (so `ch_2(S_X)[K3] = -5376` is a bulk characteristic number, not yet the families index);
(iv) `3-primary torsion component -> integer 3` (Section 9). The program has previously caught four fabricated paths to
three (a disguised `chi`, a reverse-engineered `+8`, a circular rank-4, a fitted holonomy); this computation
adds none, and asserts the absence (`integer_is_3 = False`).

**The forcing-slot test (computed).** Item (i) -- the gate on the unbuilt source action -- has since been
probed directly. We reverse-engineered the necessary conditions ("forcing slot") any source action must meet
to force a count: a term simultaneously (a) tangential (carries `p_1`), (b) net-chiral, and (c)
non-frame-trivial. We then built a toy stabilized twisted Rarita-Schwinger sector four ways (Faddeev-Popov
stabilization; the twisted spin-3/2 AGW index on K3; the RS frame-index operator on the `Cl(9,5)` substrate;
the gravitino anomaly polynomial), each angle adversarially re-verified (`tests/forcing-slot/`,
`canon/forcing-slot-toy-rs-RESULTS.md`). The RS sector reaches at most two of the three properties, never all
three with a derived generation-count integer. The tested integers are even or equal one: `256 = 2^8`
(a tautological projector trace, with physical-sector index 0), `-672 = -2^5 . 3 . 7`, `-42 == 0 (mod 3)`
(the `Z/3` identity), the HP^2 unit `1`. In the exact anomaly-polynomial expansion actually tested
(Pontryagin degree through `p_4`, i.e. differential-form degree 16), no spin-3/2 coefficient has a factor of
3 in its reduced numerator; factors of 3 occur in the genus denominators. This is a finite-degree
calculation, not a theorem about every coefficient in all dimensions. In the four-dimensional K3 case, the
twisted-by-16 index `16(-42) + 3 ch_2(V)` is `== 0 (mod 3)` for every integer twist. These are four bounded
negative tests, not a classification of source actions. Their integer outputs do not acquire a `Z/8` type
merely because some are even. The actual stabilized action remains unbuilt.

**The "2+1" reading is numerology across frameworks (computed).** The "2+1 effective" picture (the `2` from
`A-hat(K3)`, the `1` from Pati-Salam) is not a single legitimate count. In one common framework (the Â-genus
character-valued index on K3), the spin-1/2 leg gives `2` but the spin-3/2 leg gives `-42 == 0 (mod 3)`, not a
clean `+1`; the `+1` appears only as the twisted-Dirac unit on a different manifold (HP^2). The two summands of
`2+1` live in disjoint frameworks, so their sum is a coincidence, not a derivation. "Located, not forced" thus
holds under both the order-3/triality reading and the additive 2+1 reading.

**Carrier-mass test (computed).** In the tested finite model the carrier `Lambda^2_+` is vectorlike, so the
source action's possible **Dirac mass** is a relevant unresolved term
(`canon/carrier-dirac-mass-capstone-RESULTS.md`). The mass is **allowed,
not forbidden**: the Kramers structure `C^2 = -I` is pseudoreal, hence self-conjugate, hence vectorlike, which
*admits* a mass; and the built Seiberg-Witten action *realizes* a vectorlike one (`||M_++|| = ||M_--||`, a
`{+, 0, -}` split, heavy-sector net chiral 0). Both branches give zero, not three: massive, the 96 generation
modes pair with 96 mirror modes and decouple, leaving net chiral index `(n_+ - r) - (n_- - r) = 0` analytically
for every mass; massless, the 192 stay light but the tested balance remains zero. A light chiral count would
require a separately typed projection/index construction that breaks this balance. The finite Krein theorem
does not prove that no such physical or function-space construction exists. Consistently, exact `Spin(9,5)`
representation theory (computed by decomposing `S^+ (x) S^+` over the explicit
`Cl(9,5) = M(64,H)` gamma matrices into the Clifford form-degree basis `End(S) = (+)_k Lambda^k` and solving for
the `Spin(9,5)`-invariant bilinear space by trace-orthonormal projection onto antisymmetrized Clifford words
(checksum `sum_k mult = 128^2 = 16384`); `tests/chase/MOVE-4/move4_spinor_square_forms.py`, with the independent
re-check `tests/chase/MOVE-4/verify/indep_check.py`) gives
`dim Hom_{Spin(9,5)}(S^+ tensor S^+, Lambda^0) = 0`: no invariant same-chirality Majorana scalar-mass bilinear
exists in the equivariant family (the scalar bilinear pairs only `S^+ <-> S^-`), so that mass channel is absent
from the tested equivariant family. This is a consistency remark about the spinor-square channel, not a
statement about the 192-dimensional carrier's Dirac mass. (This Hom-vanishing is now canon as fact (A) of the
two-arena rep-theory core, `canon/two-arena-rep-theory-core-RESULTS.md`, re-run exit 0 on 2026-07-03.)

---

## 9. What is not claimed: the open conjecture

We do **not** claim three chiral generations. The supported verdict is **located, not forced.** The single open
bridge is

> `3-primary torsion component -> integer 3`.

A nonzero class in `Z/3` detects information *mod 3*; it is not equality to the integer 3, and the
`e`-invariant carrying it (`e_R = 1/12`) is identical for any generation count. APS, Dai-Freed, Callan-Harvey,
and Bismut-Cheeger relate boundary invariants to indices, determinant lines, anomaly phases, and cobordism
classes, not directly to an integer family count. A direct class-to-count homomorphism is impossible because
`Hom(Z/3, Z) = 0`; likewise `Hom(Z/24, Z) = 0`.

An integer count, if one exists, therefore needs a separately constructed integer-valued invariant—such as a
relative, equivariant, rank, or Fredholm index—plus an explicit relation between its mod-3 reduction and the
located torsion component. On GU's actual 14-manifold that would require, at minimum, a proved
fibered-boundary reduction, an explicit stabilized twisted Rarita-Schwinger operator/source action, and a
well-typed integer extraction. Those objects are not presently built.

The computations on the `RP^3 = L(2;1)` spine and their `L(3;1)` controls are evidence about specific
constructions, not an exhaustion theorem. Likewise, the `C_fin` census and the finite Krein theorem do not
exclude non-equivariant operators, K-definite constructions, or the true-`Y14` family pushforward. The open
question is therefore narrow but genuine: can a geometry-dependent integer index be constructed on the actual
bundle, and can its mod-3 reduction be proved to match the exhibited torsion component? Until then, no
computation in this program yields the integer three.

---

## 10. Relation to Geometric Unity and to prior art

**Geometric Unity.** The sector is motivated by GU's matter proposal (the 14-dimensional observer space
`Y14 = Met(X^4)`,
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
with `c_- = 24`; and Wan-Wang-Yau 2026 v2 (arXiv:2605.26202v2), which explicitly separates 2- and 3-primary
anomaly data and combines the corresponding extensions by CRT. Its conditional minimal
`N = N_c = N_f = 3` conclusion also uses the generalized Standard Model without sterile `nu_R`, minimal
cyclic extensions, the `SU(2)` oddness condition, color-center matching, and fermionic baryons. Deriving three generations from algebraic
structure is likewise an active lane -- e.g. the division-algebra trialities of Furey-Hughes (arXiv:2409.17948),
where two generations arise as spinors and a third through a Cartan factorization; our Clifford-RS route is
mechanically distinct, but the question is not untouched. We claim no novelty for "topology constrains
family number." Section 14 makes this canonical Markdown bibliographically self-contained.
Our narrow novelty claim (the canonical source and release TeX use the same scope): Wang 2023's title
arithmetic `24/8 = 3` already pulls
the odd 3-primary factor out of `Z/24` as the family number, and Wan-Wang-Yau 2026 v2 explicitly separates the
2- and 3-primary parts and uses CRT. We therefore claim **no** novelty for the bare factorization, primary
decomposition, CRT step, or use of `pi_3^s = Z/24`. To the best of the bounded primary-source search recorded
in `PRIOR-ART-DELTA.md`, no located source combines the explicit cross-chirality Clifford-RS carrier, a scoped
sector-interior 2-primary obstruction/selector result, and the inverse conclusion that those data are blind
to a separate 3-primary torsion component. The candidate delta is only this carrier-specific inverse assembly;
it is not proof of publication novelty, and the inverse step may be elementary once the premises are granted.
For Theorem 2 itself we claim no novelty beyond its application: its
mathematical core (a maximal definite subspace of a form pairing two complementary Lagrangians is a graph,
hence balanced) is elementary and of a classical Krein-space kind, the vectorlike character of real/pseudoreal
matter is standard representation theory, and indefinite-metric (Krein) formulations of the Standard Model with
an explicit generation space already exist in the noncommutative-geometry literature (the Lorentzian spectral
Standard Model, e.g. arXiv:2010.04960). What we claim is the specific assembly: that theorem, on this carrier,
feeding the two-arena reading.

---

## 11. Status of claims

| ID | Claim | Grade |
| --- | --- | --- |
| LNF-CL-001 | `Cl(9,5)` carrier type | `H^64` has real dimension 256; computations use its 128-dimensional complex realization, and unqualified carrier dimensions are complex |
| LNF-CL-002 | Compact/complexified `su(2)_+` triplet | compact complex `192=96+96` calculation verified; a physical Lorentzian half is also dimension 192 but K-null and conjugation-exchanged, while the computed stable closure is `384` with signature `(192,192)` |
| LNF-CL-003 | `C_fin` constraints do not supply an odd-prime congruence or select an odd integer | Lean-verified for the exact encoded finite type; compact C1--C5 carrier lift computed; unrestricted `C_inv`, C6 classification, and physical transfer remain open |
| LNF-CL-004 | CRT decomposition `pi_3^s = Z/8 (+) Z/3` | standard; disjointness applies only after an explicit torsion-valued map into `Z/24` |
| LNF-CL-005 | Finite Krein intersection difference vanishes | finite complex Hermitian theorem, Lean-checked from supplied premises; compact carrier instance computed; not a physical handedness count or Fredholm index |
| LNF-CL-006 | Antilinear K-null image subspaces retain zero intersection index | delimited theorem; avoids ordinary-eigenspace language for antilinear maps; no Wigner-based uniqueness claim and no transfer to K-definite or unrestricted constructions |
| LNF-CL-007 | Tangential `Lambda^2_+` framing carries `e_R = 1/12` | sign-complete convention audit gives `+/-1/12`; full classes have order 12 and projected 3-primary components order 3; exact GU framing identification reconstruction-grade |
| LNF-CL-008 | The framed class is homotopy-fixed and does not define an integer count | computed/standard-result-applied; `Hom(Z/3,Z)=0` blocks a direct class-to-count homomorphism |
| LNF-CL-009 | Toy source-action constructions supply the missing integer count | NO in four tested constructions; bounded negative evidence, not a universal theorem |
| LNF-CL-010 | Carrier Dirac mass | allowed/vectorlike in the tested model; neither massive nor massless branch derives three |
| LNF-CL-011 | Carrier-specific inverse assembly | search-bounded candidate delta only; primary decomposition and CRT are prior art (Wang; Wan-Wang-Yau v2) |
| LNF-CL-012 | The literal generation integer on GU's 14-manifold | gated on the unbuilt true-`Y14` source action/pushforward |
| LNF-CL-013 | Pati-Salam `16 // 16 = 1` | verified family-unit normalization in a reconstructed `Spin(7,7)` branch; not a generation-count observable |
| LNF-CL-014 | `3-primary torsion component -> integer 3` | open and ill-typed as a homomorphism; needs a separately constructed integer/rank/index home |
| LNF-CL-015 | Necessity of external backgrounds | not proved; a flux-index model is a positive control, while non-equivariant and true-`Y14` routes remain open |
| LNF-CL-016 | GU forces exactly three chiral generations | not claimed; no computed quantity in this program equals three |

---

## 12. Conclusion

The release-surviving result is narrower than the original structural reading. In exact `C_fin`, finite
torsion constraints are 2-primary, integer constraints remain equality/divisibility statements, and
dimensions and diagnostics remain separately typed; none supplies a mod-3 congruence or selects the integer
three. The C1--C5 lift toward semantic `C_inv` is computed only on the compact carrier, and the unrestricted
lift remains open. The CRT decomposition separates
torsion data only after a map into `Z/24` is supplied. It does not convert a `Z`-valued index into `Z/8` or a
generation count into `Z/3`.

The finite complex Krein theorem proves zero intersection difference from positivity and isotropy, not a
physical left-minus-right state count. Its `(96,96)` instance belongs to the compact/complexified packet;
the computed physical Lorentzian half is K-null and its conjugation-stable closure is `(192,192)`. The framed
classes `+/-2 in Z/24` have order 12 and nonzero order-3 projections; they are tangential, homotopy-fixed, and
not integer counts. The true Rarita-Schwinger `Y14` source-action pushforward,
non-equivariant constructions, and a typed integer index remain open.

Thus “located, not forced” means only that a 3-primary torsion component is exhibited while no tested
construction supplies the missing integer bridge. We do not claim three generations, a universal no-go, or
that external backgrounds are necessary. Zenodo publication records this internally established result;
external review of the scoped theorems and open typing bridge is welcome as an optional later validation stage.

---

## 13. Data and code availability

The canonical release source, claim ledger, review packets, Python evidence,
and Lean certificates are in the public repository:
[disruptionjoe/gu-formalization](https://github.com/disruptionjoe/gu-formalization).
`REVIEWER.md` gives the pinned-checkout and copy-paste reproduction route.
`CLAIM-AND-PREMISE-LEDGER.json` is the current claim authority;
`LOAD-BEARING-NUMBERS.json` maps all 31 release-harness results to source and
evidence. The historical July 14 claim map remains archived in `review/` but
is not the current release surface.

The adjacent TeX, PDF, and Zenodo package are downstream release artifacts
generated from this v2.15 Markdown. Their integrity manifest and verification
receipt bind the deposited files to the stated source commit. The DOI and
publication date remain unset until Zenodo assigns and records them.

---

## 14. References

1. J. F. Adams, “On the groups J(X). IV,” *Topology* **5** (1966), 21–71,
   [DOI:10.1016/0040-9383(66)90004-8](https://doi.org/10.1016/0040-9383(66)90004-8);
   correction, *Topology* **7** (1968), 331,
   [DOI:10.1016/0040-9383(68)90010-4](https://doi.org/10.1016/0040-9383(68)90010-4).
2. A. Altland and M. R. Zirnbauer, “Nonstandard symmetry classes in
   mesoscopic normal-superconducting hybrid structures,” *Physical Review B*
   **55** (1997), 1142–1161, [arXiv:cond-mat/9602137](https://arxiv.org/abs/cond-mat/9602137).
3. L. Alvarez-Gaumé and E. Witten, “Gravitational anomalies,” *Nuclear
   Physics B* **234** (1984), 269–330; erratum **244** (1984), 421.
4. J.-M. Bismut and J. Cheeger, “η-invariants and their adiabatic limits,”
   *Journal of the American Mathematical Society* **2** (1989), 33–70.
5. F. Besnard and C. Brouder, “Noncommutative geometry, the Lorentzian
   Standard Model, and its B−L extension,” *Physical Review D* **103** (2021),
   035003, [arXiv:2010.04960](https://arxiv.org/abs/2010.04960),
   [DOI:10.1103/PhysRevD.103.035003](https://doi.org/10.1103/PhysRevD.103.035003).
6. C. G. Callan Jr. and J. A. Harvey, “Anomalies and fermion zero modes on
   strings and domain walls,” *Nuclear Physics B* **250** (1985), 427–436.
7. X. Dai and D. S. Freed, “η-invariants and determinant lines,” *Journal of
   Mathematical Physics* **35** (1994), 5155–5194,
   [arXiv:hep-th/9405012](https://arxiv.org/abs/hep-th/9405012),
   [DOI:10.1063/1.530747](https://doi.org/10.1063/1.530747); erratum **42**
   (2001), 2343–2344.
8. B. A. Dobrescu and E. Poppitz, “Number of fermion generations derived from
   anomaly cancellation,” *Physical Review Letters* **87** (2001), 031801,
   [arXiv:hep-ph/0102010](https://arxiv.org/abs/hep-ph/0102010).
9. J. L. Evans, M. Ibe, J. Kehayias, and T. T. Yanagida, “Non-anomalous
   discrete R-symmetry decrees three generations,” *Physical Review Letters*
   **109** (2012), 181801, [arXiv:1111.2481](https://arxiv.org/abs/1111.2481).
10. N. Furey and M. J. Hughes, “Three generations and a trio of trialities,”
    *Physics Letters B* (2025), 139473,
    [arXiv:2409.17948](https://arxiv.org/abs/2409.17948),
    [DOI:10.1016/j.physletb.2025.139473](https://doi.org/10.1016/j.physletb.2025.139473).
11. I. García-Etxebarria and M. Montero, “Dai-Freed anomalies in particle
    physics,” *JHEP* **08** (2019), 003,
    [arXiv:1808.00009](https://arxiv.org/abs/1808.00009).
12. D. B. Kaplan and S. Sun, “Spacetime as a topological insulator: mechanism
    for the origin of the fermion generations,” *Physical Review Letters*
    **108** (2012), 181807, [arXiv:1112.0302](https://arxiv.org/abs/1112.0302).
13. R. Kirby and P. Melvin, “Canonical framings for 3-manifolds,” *Turkish
    Journal of Mathematics* **23** (1999), 89–115,
    [arXiv:math/9903056](https://arxiv.org/abs/math/9903056).
14. D. A. McLaughlin, “Orientation and string structures on loop space,”
    *Pacific Journal of Mathematics* **155** (1992), 143–156.
15. T. Nguyen and T. Polya, “A response to Geometric Unity,” self-published
    manuscript (23 February 2021),
    [author-hosted PDF](https://files.timothynguyen.org/geometric_unity.pdf).
16. V. A. Rokhlin, “New results in the theory of four-dimensional manifolds,”
    *Doklady Akademii Nauk SSSR* **84** (1952), 221–224.
17. H. Sati and H.-b. Shim, “String structures associated to indefinite Lie
    groups,” *Journal of Geometry and Physics* **140** (2019), 246–264,
    [arXiv:1504.02088](https://arxiv.org/abs/1504.02088),
    [DOI:10.1016/j.geomphys.2019.02.002](https://doi.org/10.1016/j.geomphys.2019.02.002).
18. K. G. C. von Staudt, “Beweis eines Lehrsatzes, die Bernoullischen Zahlen
    betreffend,” *Journal für die reine und angewandte Mathematik* **21**
    (1840), 372–374; T. Clausen, *Astronomische Nachrichten* **17** (1840),
    351–352.
19. Z. Wan, J. Wang, and S.-T. Yau, “Fermion Families and Pontryagin Class:
    Topological Field Theory via Colour Symmetry Extension,”
    [arXiv:2605.26202v2](https://arxiv.org/abs/2605.26202) (2026).
20. J. Wang, “Family Puzzle, Framing Topology, c−=24 and 3(E8)1 Conformal
    Field Theories: 48/16 = 45/15 = 24/8 = 3,”
    [arXiv:2312.14928](https://arxiv.org/abs/2312.14928) (2023).
21. E. Weinstein, “Geometric Unity (author's working draft),” self-published
    manuscript (1 April 2021), [geometricunity.org](https://geometricunity.org/).
22. E. P. Wigner, *Group Theory and Its Application to the Quantum Mechanics
    of Atomic Spectra*, Academic Press, New York (1959), translated from the
    1931 German edition.

---

## Appendix: reproducibility

A single self-contained script, `papers/candidates/located-not-forced/reproduce_all.py`, recomputes the 31
enumerated numerical and symbolic checks in the release manifest from a clean checkout and checks each against
its stated value (exit 0 iff all 31 checks match; every check ships a discriminating control that must fail on
a scrambled input); see `REVIEWER.md`.

The representation-theoretic decompositions, compact Krein signature, finite
intersection-difference checks, framing convention/sensitivity controls, and decider integers are
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
`canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md`,
`canon/core-theorems-symbolic-proof-RESULTS.md`, `canon/external-by-structure-synthesis-RESULTS.md`,
`canon/external-topological-index-flux-RESULTS.md`, `canon/rs-function-space-framework-SPEC.md`) are in the
repository. The v2.9 symbolic and external-index checks run in `tests/symbolic-proofs/` and
`tests/function-space-ext/` (with an independent re-verification under `tests/function-space-ext/verify/`).
The v2.15 physical-signature discriminator is
`tests/lorentzian-transfer/physical_signature_transfer_audit.py`; the exact
framing sensitivity check is
`tests/boundary-eta/v15_framing_convention_sensitivity.py`; and the targeted
Lean entrypoints are under `tests/located-not-forced/`.

**Verification status.** By the project's own three-tier vocabulary, every result in this paper is at most
*internally established*: computed, independently re-derived from scratch, and adversarially reviewed *within
the same AI-directed process that produced it* (reproduced, not replicated). No result here is *externally
established* -- independently replicated, peer-reviewed, or signed off by a named specialist. Because internal
reviewers are spawned by the same process that produced the results, no internal step, however adversarial, can
cross that boundary. Zenodo publication does not claim to cross it. Optional
later external review is the route to an external-validation grade.

---

## Appendix: Reproducibility -- the Pati-Salam one-generation verification

The Pati-Salam family-unit normalization used in Section 8 rests on a self-contained group-theory
verification of a reconstructed GU-motivated branch, reproduced here for completeness. The script
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

totalling `6 + 3 + 3 + 2 + 1 + 1 = 16` states, with the directly checked linear traces
`Tr Y = Tr Q = 0` and electric charges
`{0, +/-1/3, +/-2/3, +/-1}`. The integer label `n = 6Y` reproduces the GU draft's Section 11.3 table exactly; an
embedding-ambiguity probe confirms that the naive `B-L`-only hypercharge fails, so the standard
`Y = T_3R + (B-L)/2` embedding is forced. An independent explicit-Clifford cross-check
(`lab/active-research/verify_clifford_explicit.py`, with 32x32 gamma matrices satisfying the `SO(10)` Clifford
relations numerically) reproduces the same content and its exact CP conjugate (`n -> -n`, `3 <-> 3bar`).

**Scope:** this is a one-family *structural* verification, not a generation count. What is verified is that
the `16` of `Spin(10)` carries exactly *one* Standard-Model family, with the paper's hypercharge
assignments and displayed linear trace checks reproduced from first principles -- i.e. internal
representation-theoretic consistency of the reconstructed branch. It does **not** provide the generation
count: it does not establish that nature realizes this breaking
pattern, does not address the effective-chirality or "2+1" claims, and -- being a single generation -- says
nothing about *how many* generations occur. Moreover the `Spin(7,7)` Pati-Salam chain is one reduction among
many possible symmetry-breaking chains; the "1" it yields is chain-relative, not chain-independent. It is
the arithmetic normalization `16 // 16 = 1` of Section 8, and its role in this paper is
precisely that: a normalization of one `16` as one family, not a derivation of how many families occur.
