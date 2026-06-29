# Located, Not Forced: Two-Primary Blindness and a Three-Primary Boundary Invariant for the Generation Count in a Clifford Rarita-Schwinger Sector

**Draft for external review. This paper does NOT claim three generations. See Sections 1 and 8.**

Version 1.3, 2026-06-29. (v1.1 forcing-slot test; v1.2 the `Hom(Z/3, Z) = 0` sharpening; v1.3 the carrier-mass
capstone -- the gate reduced to one physical term, Section 7.)

---

## Abstract

We study the chirality and generation structure of an explicit real Clifford Rarita-Schwinger sector: the
gamma-traceless rank-3/2 field of a real Clifford module `Cl(p,q)` with `p+q = 14` on a 128-dimensional
spinor, with one generation identified with the `16` of `Spin(10)`. The sector is motivated by, and
reconstructed from, the matter proposal of Geometric Unity (GU); every GU-specific step is marked, and none
of the theorem-grade results depend on GU being correct. We prove two theory-independent impossibility
results and use them to relocate, precisely, the only place a generation count could live.

First, a **2-primary meta-theorem**: every obstruction to a net chiral count in this sector is even or
mod-`2^k` (Kramers, the real/pseudoreal mod-2 Witten index, the cross-chirality Krein signature, the adjoint
index `4k`, Rokhlin mod 16, a spinor 2-smoothness lemma, ghost parity), so the no-go is arithmetically
incapable of imposing an odd-prime congruence and is structurally blind to the 3-primary summand of
`pi_3^s = Z/24 = Z/8 (+) Z/3`. Second, a **machine-verified index-conservation theorem**: the invariant Krein
form on the generation triplet is purely cross-chirality `(+96, -96)`, so every *linear* Krein-isometric
operator conserves the net chiral index at zero (verified across signatures `(9,5)`, `(7,7)`, `(14,0)`), and
the unique symmetry-respecting escape is an **antilinear** (CPT / particle-hole, Altland-Zirnbauer class CII)
re-grading.

The decomposition `pi_3^s = Z/8 (+) Z/3` is the central structural fact. By the Chinese Remainder Theorem the
two summands are disjoint and non-interacting; every obstruction and every chiralizing selector lives in the
2-primary `Z/8` summand, while a homotopy-theoretic count, if it exists, lives only in the odd-torsion `Z/3`
summand. We exhibit a genuine order-3 object in that sector -- the framed-bordism Adams `e`-invariant
`e_R = 1/12` carried by the self-dual `Lambda^2_+` tangential framing on the `RP^3` spine of the metric fiber
-- and we show by explicit computation that it is **tangential but vectorlike and homotopy-fixed**: it
locates the order-3 slot without filling it with a count, and the unique count-producing operator is
frame-trivial and couples to the gauge (2-primary) channel.

We then attempt the single calculation that could decide an integer count on GU's actual 14-manifold and find
it **gated** on an unbuilt object (the stabilized twisted Rarita-Schwinger source action); the only honest
computable generation integer is **one** (GU's own Pati-Salam `Spin(7,7)` chain). A toy of that source action,
built and adversarially tested four ways, does **not** fill the forcing slot -- every integer it produces is
2-primary or one -- which hardens the verdict from conjecture to computation. We therefore do **not**
claim three generations. We claim a no-go that *locates*: it pins the unique CRT-disjoint sector where an odd
count could live, shows that sector genuinely carries an order-3 object, and poses the
`order-3-class -> integer-3` identification as the single named open conjecture (and a candidate category
error). We situate the mechanism against the recent family-puzzle literature and find the
J-homomorphism / Adams-`e` / 2-vs-3-primary move has no precedent. External review of both the core results
and the open bridge is requested.

---

## 1. Introduction

The Standard Model contains three generations of fermions and does not explain the number. A recurring hope
in unification is that the number is fixed by topology. The obstacle, made precise here, is that the natural
index- and anomaly-theoretic invariants one computes in such settings are predominantly **2-primary**:
mod-2 Witten anomalies, mod-16 topological-superconductor classifications, even-valued Dirac indices. A
2-primary invariant cannot, by arithmetic, force an odd count.

This paper turns that obstacle into a positive structural statement, in one explicit sector, and then tests
the strongest possible reading of it by direct computation. Our contributions:

1. **A 2-primary meta-theorem (Section 3).** Every obstruction to a net chiral count in this sector is even
   or mod-`2^k`. [theorem, theory-independent]
2. **A CRT two-arena structure (Section 4).** `pi_3^s = Z/24 = Z/8 (+) Z/3` splits, by the Chinese Remainder
   Theorem, into disjoint summands. Every obstruction *and* every chiralizing selector lives in `Z/8`; a
   homotopy-theoretic count lives only in `Z/3`. The two arenas cannot interact directly; anomaly inflow is
   the sole possible bridge. This is the unifying frame: the no-go is blind to the count not by weakness but
   by arithmetic.
3. **An index-conservation theorem and a necessary antilinear escape (Section 5).** Every linear
   Krein-isometric operator conserves the net chiral index at zero (machine-verified); the unique escape is
   antilinear. We further compute that the antilinear chiralizer is **frame-trivial** (tangent-frame charge
   exactly 0) and therefore couples to the gauge (2-primary) channel -- it supplies chirality but cannot
   reach the 3-primary sector.
4. **A located order-3 carrier (Section 6).** The self-dual `Lambda^2_+` tangential framing on the `RP^3`
   spine carries `e_R = 1/12`, a genuine order-3 class in the `Z/3` summand -- shown by computation to be
   tangential but vectorlike and homotopy-fixed: it locates, it does not fill.
5. **The single decider, and an honest gate (Section 7).** The integer count on GU's actual 14-manifold is
   gated on the unbuilt twisted Rarita-Schwinger source action; the only honest computable integer is one.
   We do not force three.
6. **The open conjecture (Section 8).** `order-3-class -> integer-3` is a theorem of nothing in the present
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

## 3. Theorem 1: the no-go is 2-primary

Call an integer or torsion invariant **2-primary** if it is a power of two, a multiple of one, or a
statement modulo a power of two.

**Theorem 1.** *Every obstruction to a net chiral generation count established in this sector is 2-primary.*

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
odd-prime congruence.** A literature analogue is standard: the 3-primary part of the stable 3-stem is "lost
in the mod-2 Postnikov system."

---

## 4. The CRT two-arena structure

`pi_3^s = Z/24`, with primary decomposition `Z/24 = Z/8 (+) Z/3`. Adams' image-of-`J` theorem gives, in
stem `4s-1`, that `Im J` is cyclic of order `denom(B_{2s}/4s)`; for `s=1` this is `24`, so `Im J_3 = Z/24`
and the Adams `e`-invariant detects it.

**The central structural fact.** By the Chinese Remainder Theorem the splitting `Z/24 = Z/8 (+) Z/3` is into
**disjoint, non-interacting summands**: there is no nonzero homomorphism `Z/8 -> Z/3` or `Z/3 -> Z/8`. By
Theorem 1, every obstruction in the no-go constrains only the `Z/8` (2-primary) summand. We show in Section 5
that every chiralizing *selector* likewise lives in `Z/8`. A homotopy-theoretic generation count, being odd,
can live only in the `Z/3` summand.

**Corollary (the two arenas).** The question "does any obstruction or selector force the count?" is
**arithmetically ill-posed**: obstruction/selector and count inhabit CRT-disjoint summands, so the answer is
no before any geometric input. The no-go's blindness to the count (Theorem 1's corollary) is therefore not a
weakness but a *structural feature*: a no-go that could constrain the odd-torsion summand would be
inconsistent with the CRT splitting. The only object that can bridge the two arenas is anomaly inflow
(Callan-Harvey / Dai-Freed), and Section 7 shows that even the inflow coefficient does not, on present
computation, force three.

This is the unifying frame of the paper. We refer to `Z/8` as the *selector arena* and `Z/3` as the *carrier
arena*. The remaining sections show that the chiralizer lives in the selector arena, the count-carrier lives
in the carrier arena, and they do not meet.

---

## 5. Theorem 2: index conservation and the necessary antilinear escape

**Theorem 2.** *Every linear Krein-isometric operator on the generation triplet conserves the net chiral
index at zero.*

**Proof sketch.** The invariant Krein form is purely cross-chirality `(+96, -96)`; the maximal positive-norm
subspaces of a cross-chirality hyperbolic form are graphs of a chirality-exchanging isometry, forcing an
exact `50/50` chiral split. Machine-verified: net chiral index `~ -2.4e-15` across signatures `(9,5)`,
`(7,7)`, `(14,0)` (`tests/generation-sector/swing_ghost_parity_chiral_selection.py`,
`t1a_kinematic_chirality_kill.py`). QED.

**Corollary (necessary antilinear escape).** No linear / unitary dynamics generates chiral asymmetry in this
sector. By Wigner's dichotomy the unique symmetry-respecting escape is **antilinear** (CPT / particle-hole;
Altland-Zirnbauer class CII), realized by a re-grading `C = J_quat . G` with `C^2 = -I` (Kramers/PHS,
antilinearity defect `~ 85`). Corroborated independently by a Seiberg-Witten moment-map degree argument: a
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

---

## 6. The located order-3 carrier

The order-3 content lives in exactly one place. The self-dual `SU(2)_+ = Lambda^2_+` structure, read as a
**tangential** framing on `RP^3 = L(2;1)` (the deformation-retract spine of the metric fiber
`GL(4,R)/O(3,1)`), has framed-bordism class `+/- 2 in pi_3^s = Z/24` and Adams `e`-invariant

```
e_R = p_1/48 = 1/12   (p_1 = 4, Kirby-Melvin; class 2 in Z/24; 3-primary part nonzero, order 3).
```

The stabilization `pi_3(SO(3)) -> pi_3(SO)` is `x2`, so the stable degree is `p_1/2 = 2`, not the Dynkin
index 4. This is standard topology (Kirby-Melvin; the `e = p_1/48` framed-bordism formula); only the
identification of GU's `Lambda^2_+` twist with this natural tangential framing is reconstruction-grade.

**It locates but does not fill (computed).** The carrier `Lambda^2_+` has net self-dual tangent-frame charge
`33.94` (tangential, `p_1 = 4`) -- it is genuinely on the carrier-arena side -- **but it is vectorlike**
(net chiral 0, Section 2), and `e_R = 1/12` is **homotopy-fixed**: it is a fact about `pi_3^s`, identical for
a universe with one generation or five. So the carrier marks the order-3 slot; it does not co-vary with the
answer and so cannot, by itself, be the thing that counts to three. The negative control confirms the slot is
unique: `RP^3`'s own deck group is `Z/2`, and the charge-`q` Dirac `eta = (2q^2-4q+1)/8` is 2-primary for
every integer `q`, so the order-3 burden sits **only** in the gravitational framing channel `-p_1/24`.

We emphasize the resulting picture, which Sections 5 and 6 establish by computation: the **chiralizer** (the
thing that produces a nonzero net count) is frame-trivial and lives in the selector arena; the **carrier**
(the only order-3 object) is frame-charged and lives in the carrier arena; they are distinct objects bound
only by anomaly inflow.

---

## 7. The single decider, and the honest gate

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
  (`Tr Y = Tr Q = 0`, `16 // 16 = 1`; "2+1 effective"). The spin-1/2 leg is `8*A-hat(K3) = 16`, with
  `A-hat(K3) = 2` the "2" of "2+1". The bulk-topology-forced integers are `{0 (linear net-chiral, vectorlike),
  1 (Pati-Salam), 2 (A-hat(K3))}`; none is 3.
- **The fork lands gauge for the count-producing operator** (`e = 3/8`, denom `8`, 3-part zero), via the
  frame-triviality of Section 5 -- structural and convention-independent.

So under the decision rule fixed in advance, the strong reading dies twice over: the integer is not three
(it is gated, and the only honest one is one), and the fork lands gauge. Controls reproduced exactly:
`ch_2(S_X)[K3] = -5376 = -2^8 . 3 . 7` (the apparent "24" is a disguised `chi(K3)` import via `2chi+3sigma=0`,
rejected; a `chi`-route gives `ch_2 = 0`); `A-hat(K3) = 2`; the charge-`q` `eta` family; Pati-Salam `-> 1`.

**Honestly gated, not fabricated.** Four things remain genuinely gated and are marked as such: (i) the `+8`
RS leg / the literal integer, on the unbuilt source action; (ii) the full analytic Bismut-Cheeger
fibered-boundary reduction theorem for the non-product 9-dim `S^6`-bundle over `RP^3` (the machinery is a
theorem and the even-fiber transparency `A-hat[S^6] = eta(S^6) = 0` is computed, but its application to GU's
actual twisted-RS boundary operator is gated; "the spine is `RP^3`" is not that theorem); (iii) the families
pushforward `pi_! : ch(S)/Y14 -> ch(S_X)/X4`, which is not defined because the fiber `GL(4,R)/O(3,1)` is
non-convex (so `ch_2(S_X)[K3] = -5376` is a bulk characteristic number, not yet the families index);
(iv) `order-3-class -> integer-3` (Section 8). The program has previously caught four fabricated paths to
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
result for the RS-side gate.

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
mass/dynamical level.

---

## 8. What is not claimed: the open conjecture

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
resolved. A toy of that twisted Rarita-Schwinger operator has now been built and tested four ways (Section 7);
it does not fill the forcing slot, and every integer it produces is 2-primary or one -- which strengthens the
conjecture's standing as a candidate category error over the gated-but-derivable alternative (the RS-side gate,
when probed, opens onto the selector arena). Until then the result is a no-go that *locates*, and the evidence
tilts toward one.

---

## 9. Relation to Geometric Unity and to prior art

**Geometric Unity.** The sector is motivated by GU's matter proposal (the 14-dim observerse `Y14 = Met(X^4)`,
the vector-spinor field, the `4+10` split, the `16` of `Spin(10)`, the self-dual base structure). The draft
presents the fermion sector schematically, does not build the matter action, states chirality is only
*effective*, and proposes a "2+1" picture rather than three true generations; Nguyen's critique argues
central technical details are unverifiable from the public material. Our results are therefore a
reconstruction, and where GU's own narrative points (2+1, and the verified `Spin(7,7) -> 1` chain), it tilts
against the strong three-generation reading. We are explicit about this throughout.

**Prior art.** Deriving or constraining the generation number from topology or anomalies has substantial
precedent (Dobrescu-Poppitz; Evans et al.; Kaplan-Sun; Garcia-Etxebarria-Montero's `Z_9` forcing
`N_gen in 3Z`; Juven Wang's 2023 family puzzle via framed/string bordism `Z/24` and `c_- = 24`; Wan-Wang-Yau
2026's 2-power/3-power anomaly decomposition). We claim no novelty for "topology constrains family number."
Our narrow novelty claim: we have not found prior work that (a) identifies the generation/chirality
obstruction package as 2-primary and reads it as a structural blindness via the **CRT two-arena** split of
`pi_3^s`, nor (b) places the candidate count in the 3-primary summand and reads it by the **Adams `e`-invariant
/ image of `J`**. Wang 2023 and Wan-Wang-Yau 2026 are the nearest topological precursors and use neither the
`J`-homomorphism nor the Adams `e`-invariant.

---

## 10. Status of claims

| Claim | Grade |
| --- | --- |
| The no-go is 2-primary (no odd-prime congruence) | theorem (theory-independent) |
| CRT two-arena structure `pi_3^s = Z/8 (+) Z/3`, summands disjoint | theorem |
| Linear Krein-isometric operators conserve the net chiral index | theorem (machine-verified) |
| The unique escape is antilinear (class CII) | corollary (Wigner) + machine-verified |
| The antilinear chiralizer is frame-trivial, couples gauge (selector arena) | computed-confirmed (convention-independent) |
| Tangential `Lambda^2_+` framing carries `e_R = 1/12`, order 3 (carrier arena) | standard-result-applied (Kirby-Melvin); GU identification reconstruction-grade |
| The carrier is vectorlike and homotopy-fixed (locates, does not fill) | computed-confirmed |
| The `J` / Adams-`e` / 2-vs-3-primary mechanism is novel | literature-established |
| The literal generation integer on GU's 14-manifold | GATED on the unbuilt source action |
| The only honest computable generation integer | 1 (Pati-Salam `Spin(7,7)`, computed) |
| `order-3-class -> integer-3` | OPEN; ill-typed as stated (`Hom(Z/3,Z)=0`); an integer needs a relative/rank home (the twisted-RS index) |
| Toy stabilized twisted RS sector fills the forcing slot | NO (computed); reaches <=2 of 3 properties; every integer 2-primary or 1 |
| "2+1" as a single additive count | numerology across disjoint frameworks (computed) |
| Carrier Dirac mass (the gate) | ALLOWED/vectorlike (computed); massive -> decouples to 0, massless -> modulus; neither is 3; forcing 3 needs the frame-trivial selector-side chiral projection |
| GU forces exactly three chiral generations | NOT claimed; evidence tilts toward one |

---

## 11. Conclusion

We have isolated, in an explicit Clifford Rarita-Schwinger sector, a clean structural picture. The
generation/chirality no-go is built from 2-primary statements and is therefore arithmetically incapable of
constraining an odd count; the relevant homotopy group splits, by the Chinese Remainder Theorem, into a
2-primary selector arena and a disjoint odd-torsion carrier arena; every obstruction and every chiralizer
lives in the selector arena, while a homotopy count can live only in the carrier arena. We exhibited the
unique order-3 object in the carrier arena and showed by computation that it is tangential but vectorlike and
homotopy-fixed -- it locates the slot, it does not fill it -- and that the unique count-producing operator is
frame-trivial and couples to the selector arena. The one calculation that could yield an integer on GU's
actual geometry is gated on an unbuilt source action; the only honest computable integer is one.

We submit the 2-primary blindness theorem, the CRT two-arena structure, the index-conservation /
antilinear-escape theorem, and the located order-3 carrier as a referee-proof, GU-independent contribution --
**a no-go that locates** -- and we submit the generation-count reading as a single named open conjecture
(`order-3-class -> integer-3`, a candidate category error) rather than a claim. We do not claim three; the
evidence tilts toward one. We request external review of both the core results and the open bridge.

---

## Appendix: reproducibility

The representation-theoretic decompositions, the Krein signature, the index-conservation check, the
frame-charge / DECOUPLE computation, the boundary `e`-invariant controls, and the single-decider integers are
checked numerically in `tests/` and `tests/generation-sector/`, `tests/source-action/`, `tests/boundary-eta/`,
`tests/decider/` (the last reproduced by an independent from-scratch script, 26/26 checks), and
`tests/forcing-slot/` (the toy RS forcing-slot test, four angles each adversarially re-verified). The homotopy and
`e`-invariant facts are standard (Adams; Kirby-Melvin; Randal-Williams). The campaign's adversarial
deep-research reports and the per-result canon (`canon/two-primary-lemma.md`,
`canon/boundary-eta-of-mu-RESULTS.md`, `canon/three-generations-locate-not-force-CRT-RESULTS.md`,
`canon/single-decider-integer-index-RESULTS.md`, `canon/forcing-slot-toy-rs-RESULTS.md`) are in the
repository.
