# Generation Multiplicity versus Chirality: A Two-Primary No-Go and a Three-Primary Boundary Class in a Clifford Rarita-Schwinger Sector

**Draft for external review. Not a claim of three generations. See Section 8.**

Version 0.1, 2026-06-28.

---

## Abstract

We study the chirality and generation structure of an explicit real Clifford Rarita-Schwinger
sector: the rank-(3/2) field of a real Clifford module `Cl(p,q)` with `p + q = 14` acting on a
128-dimensional spinor, with the internal generation content carried by the **16** of `Spin(10)`. (The
sector is motivated by, and reconstructed from, the matter proposal of Geometric Unity; nothing in the
core results depends on that motivation, and we mark every GU-specific step.) We prove a structural
meta-theorem: **every obstruction to a net chiral generation count in this sector is 2-primary** -- each
is a statement modulo a power of two, or a power-of-two-valued index. Consequently the no-go is
**structurally blind to the 3-primary (odd-torsion) part** of any invariant in which a homotopy-theoretic
generation count could live. The natural such invariant is the framed-bordism / Adams `e`-invariant group
`pi_3^s = Z/24 = Z/8 (+) Z/3`, with `|Im J_3| = 24` (Adams). We then exhibit a concrete odd-torsion class
in exactly the blind sector: the self-dual `SU(2)_+ = Lambda^2_+` structure of the four-dimensional base,
read as a **tangential** framing on the `RP^3 = L(2;1)` spine of the metric fiber, has Adams `e`-invariant
`e_R = +/- 1/12` (class `+/- 2 in Z/24`), with **nonzero 3-primary part** -- established by Kirby-Melvin's
computation of the natural framing on `L(2;1)` together with the standard framed-bordism formula
`e = +/- p_1/48`. We do **not** claim this proves three chiral generations. We state precisely the bridge
that such a claim would require -- a fibered-boundary index reduction, an explicit Rarita-Schwinger index
operator, and an argument from an order-3 class to the integer 3 -- and we pose the generation count as an
open question. To our knowledge the mechanism (a generation/family invariant carried by the `J`-homomorphism
and the Adams `e`-invariant, with the no-go recast as a 2-primary blindness) has no prior art; we situate
it against the nearest precedents.

---

## 1. Introduction

The number of fermion generations is not explained by the Standard Model. A recurring hope in
unification programs is that it is fixed by topology. Many such mechanisms exist (Section 7), but a
persistent obstacle is that the natural index-theoretic and anomaly-theoretic invariants that one computes
in these settings are predominantly **2-primary**: mod-2 Witten anomalies, mod-16 topological-superconductor
classifications, even-valued Dirac indices. A 2-primary invariant cannot, by arithmetic, force an odd count.

This paper makes that obstacle precise, and turns it into a positive structural statement, in one explicit
sector. Our contributions are:

1. **A 2-primary meta-theorem (Section 3).** In a real Clifford Rarita-Schwinger sector, every obstruction
   to a net chiral generation count -- Kramers, real/pseudoreal mod-2 index, the cross-chirality Krein
   signature, the adjoint Dirac index, Rokhlin, a spinor 2-smoothness lemma, the ghost-parity no-go -- is a
   power-of-two or mod-`2^k` statement. We give the enumeration and the proof.

2. **A blindness corollary (Section 3.2).** Such a no-go constrains only the 2-primary part of any abelian
   invariant; it places no condition on odd torsion. If a homotopy-theoretic generation count exists, it
   lives in the 3-primary summand the no-go cannot reach.

3. **The homotopy receptacle (Section 4).** The natural home is `pi_3^s = Z/24 = Z/8 (+) Z/3`, with the
   image of `J` of order `24 = denom(B_2/4)` (Adams) and the Adams `e`-invariant detecting it.

4. **A concrete 3-primary boundary class (Sections 5-6).** The GU-native self-dual `Lambda^2_+` structure,
   read tangentially, gives `e_R = +/- 1/12` on the `RP^3` spine -- nonzero 3-primary part -- by
   Kirby-Melvin plus the standard framed-bordism formula.

5. **An honest statement of the open bridge (Section 8).** We do not claim the generation count is 3, and
   we name exactly what would be needed to claim it.

The robust, theory-independent content is items 1-3 together with the `e`-invariant computation of item 4.
The identification of the GU twist with the natural tangential framing, and the reading of the 3-primary
class as a generation count, are clearly-marked reconstruction-grade or open.

---

## 2. The setting

Let `S` be the real spinor module of a real Clifford algebra `Cl(p,q)` with `p + q = 14`, `dim_R S = 128`.
The Rarita-Schwinger (rank-3/2) field is the gamma-traceless part of `V (x) S`, where `V` is the
14-dimensional vector module; the gamma-trace constraint cuts `V (x) S` (dimension `14 * 128 = 1792`) down
to `ker(Gamma)`, of dimension `(14 - 1) * 128 = 1664 = 2^7 * 13`.

We split the 14 directions as `4 + 10`: a four-dimensional base `X^4` and a ten-dimensional internal space,
with one generation identified with the `16` of `Spin(10)`. The frame group of the base is
`Spin(4) = SU(2)_+ x SU(2)_-`; the self-dual two-forms `Lambda^2_+` generate `su(2)_+`. Under `su(2)_+`,

```
ker(Gamma) = 640 (singlets) + 416 (doublets) + 64 (triplets),
```

a decomposition we verify numerically (`tests/generation-sector/h1_selfdual_family_kill.py`). The 64
triplets are the only odd-multiplicity piece, and they carry the pure `16`. This is the native
**multiplicity-three** structure of the sector: a genuine triplet under the self-dual frame `su(2)_+`.

The relevant invariant bilinear form is the `so(p,q)`-invariant Krein form `K = eta_V (x) beta_S`. On the
triplet it is purely cross-chirality, of signature exactly `(+96, -96)`; the matter content it pairs is
therefore vectorlike, with net chirality `0`. This is the central tension the paper resolves structurally:
the sector is multiplicity-three but vectorlike, and no internal operation chiralizes it.

---

## 3. The 2-primary lemma

### 3.1 Statement and proof

Call an integer or torsion invariant **2-primary** if it is a power of two, a multiple of one, or a
statement modulo a power of two (equivalently, it lives in or constrains only the 2-primary part of an
abelian group).

**Lemma.** *Every obstruction to a net chiral generation count established in this sector is 2-primary.*

**Proof (enumeration).**

1. **Kramers wall (`J^2 = -1`).** A quaternionic structure forces complex dimensions even: "the complex
   dimension of a quaternionic representation is even" is a `Z/2` statement.

2. **Real / pseudoreal non-chirality.** A real or pseudoreal representation has vanishing mod-2 Witten
   index; the relevant index is `Z/2`-valued.

3. **Cross-chirality Krein signature.** The `so(p,q)`-invariant form on the triplet is purely
   cross-chirality, signature `(+96, -96)`; the even split forces net chirality `0`.

4. **Adjoint Dirac index.** Gauging the real self-dual adjoint by a charge-`k` instanton gives Dirac index
   `2 T(adjoint) k = 4k`; over the full 16-dimensional multiplicity bundle, `12k` or `24k`. Even in every
   case.

5. **Rokhlin.** The untwisted gravitational contribution involves `sign(X) = 0 (mod 16)`, a statement mod
   `2^4`.

6. **Spinor 2-smoothness.** A family entering as a spinor of `SO(m)` has dimension `2^floor(m/2)`, a power
   of two; the only route to odd multiplicity is a non-spinor (vector / adjoint / self-dual) family
   representation.

7. **Ghost-parity no-go.** A ghost-parity resolution of the Krein hyperbolic pairs yields a physical sector
   exactly `50/50` in chirality (net `0`); the only chiralizing alternative is a non-Dirac invariant form.

Every item is a power-of-two or mod-`2^k` statement. There is no odd-prime **modular** (congruence)
obstruction anywhere in the enumeration. QED.

*Remark (a needed correction to a tempting overstatement).* The integer 3 does appear in the sector -- as a
**multiplicand**, in dimensions like `96 = 2^5 * 3` and indices `12k`, `24k`, and in `|Weyl(D7)|`. The
lemma is **not** "no factor of 3 occurs." It is the sharper and true statement: **no obstruction is an
odd-prime congruence.** Every constraint is even-valued or mod-`2^k`; none is a `mod 3` condition.

### 3.2 The blindness corollary

**Corollary.** *The no-go places no condition on the 3-primary part of an abelian invariant in which the
generation count could live.*

**Proof.** A mod-`2^k` or power-of-two statement constrains only the 2-primary summand of an abelian group;
by the Chinese Remainder Theorem the odd-torsion summand is a direct complement on which every such map is
determined by the 2-part alone. The count `3` is odd. If it is a homotopy-theoretic invariant, its natural
home is `pi_3^s = Z/24 = Z/8 (+) Z/3`; the no-go lives in the `Z/8` summand and says nothing about `Z/3`,
because `3` is coprime to `2`. QED.

**Two honest qualifications.** (i) For the two **integer-valued** items -- the exact adjoint index `4k` and
the exact net chirality `0` -- the integer Atiyah-Singer index pins every prime, so under a literal
integer-index reading `net = 0` would *forbid* `3`. The "blindness to 3" is purchased by relocating the
count to the **torsion** boundary `e`-invariant in `pi_3^s`. The mod-2 **lemma** (every obstruction is even
/ mod-`2^k`) is unconditional; the **corollary** ("the no-go cannot see the count") holds under the
torsion-count reading, which is a premise, not a theorem of the sector. (ii) The 3-primary part of `pi_3^s`
being invisible to mod-2 data is independently standard: it is "lost in the mod-2 Postnikov system." The
slogan is mathematically natural, not rhetorical.

---

## 4. The homotopy receptacle

We recall the standard facts (theorem-grade). The stable 3-stem is `pi_3^s = Z/24`, with primary
decomposition `Z/8 (+) Z/3`. Adams' image-of-`J` theorem gives, in stem `4s - 1`, that `Im J` is cyclic of
order the denominator of `B_{2s}/4s`; for `s = 1` this denominator is `24`, so `Im J_3 = Z/24` and the
whole 3-stem is, in degree three, exhausted by the image of `J`. The Adams `e`-invariant
`e_R: pi_3^s -> Q/Z` was introduced precisely to detect image-of-`J` classes.

One sharpening, important for honesty: **Adams' theorem gives total order 24, not order 3.** That the
physically relevant class lands in the `Z/3` summand requires the additional input that the `Z/8` part is
killed or invisible -- which is exactly the content of the 2-primary lemma (Section 3). The route
"Adams `=>` 24 `=>` therefore 3" is not valid by itself; it is valid only when paired with the 2-primary
blindness, and even then it yields "the 2-primary obstructions do not constrain the `Z/3`," not "the count
equals 3." We are careful not to conflate these.

---

## 5. The tangential `e`-invariant: statement

The self-dual structure `SU(2)_+ = Lambda^2_+` defines a charge-1 twist on the base. Read as a modification
of the **stable tangent framing** (the *tangential* reading; see Section 6 for the alternative), this twist
defines a framed-bordism class, and the invariant lands in `pi_3^s`.

**Computation.** The natural framing on `RP^3 = L(2;1)` coming from the charge-1 self-dual twist has
framed-bordism class `+/- 2 in pi_3^s = Z/24`, hence

```
e_R(RP^3, self-dual tangential framing) = +/- 1/12  in Q/Z,
```

with **nonzero 3-primary part** (`+/- 2` is nonzero mod 3; equivalently `1/12` retains a factor of 3 in its
denominator).

**Published support.** Two standard ingredients combine to give this. First, Kirby-Melvin compute the
natural fiber-preserving framing on `L(2;1) = RP^3` as the Euler-2 circle bundle over `S^2`: the relative
Pontryagin number of the disk-bundle filling is `p_1 = n + chi(S^2)^2/n = 2 + 4/2 = 4`, and the Hirzebruch
defect is `h = p_1 - 3 sign = 4 - 3 = 1`; they identify the quotient framing with the right-handed Lie
framing. Second, the standard framed-bordism formula (Randal-Williams) represents the class of a framed
3-manifold `M` by `-(1/48) <p_1(W,M), [W,M]>` for a Spin filling `W`, so `p_1 = 4` gives `+/- 1/12`. The
two are consistent: `h = 1` and `p_1 = 4` coexist because the Euler-2 disk bundle has signature `+1`.

**Why `p_1/2`, not the Dynkin index.** The clutching map of the charge-1 `SU(2)` twist generates
`pi_3(SU(2)) = Z`; via the double cover `SU(2) -> SO(3)` it generates `pi_3(SO(3))`. The stabilization
`pi_3(SO(3)) -> pi_3(SO)` is multiplication by `2` (`rho -> 2 sigma`, Kirby-Melvin), so the stable degree
seen by `J` is `p_1/2 = 2`, **not** the Dynkin index `4`. Normalizing on the right-handed Lie framing of
`S^3` (`p_1 = 2`, giving the generator `+/- 1/24`), the doubled class is `+/- 2/24 = +/- 1/12`. This is an
independent derivation matching the Kirby-Melvin route.

The topology here is standard. The single reconstruction-dependent step is the identification of the GU
`Lambda^2_+` twist with this natural `SO(3)`-valued tangential framing (Section 6).

---

## 6. The tangential fork, and why the gauge branch differs

There are two ways the self-dual `Lambda^2_+` structure can enter, and they land in different receptacles.

- **Tangential.** The twist modifies the stable tangent framing. The invariant is a framed-bordism class in
  `pi_3^s`, governed by the relative Pontryagin number of a filling. This gives `+/- 2 in Z/24`,
  `e_R = +/- 1/12`, with nonzero 3-primary part (Section 5).

- **Gauge.** The twist is a coefficient bundle for a twisted Dirac operator in the adjoint. The eta-reduced
  spectral-asymmetry value is `+/- 3/8`, of order dividing `8`: **no** 3-primary part.

These are not in conflict; they are different computations in different groups. The 3-primary part survives
on the tangential branch and vanishes on the gauge branch, exactly as the arithmetic of `1/12` versus `3/8`
predicts. Which branch is physically correct is a question internal to the matter-sector reconstruction;
the public GU draft's use of the Levi-Civita connection and the vector-spinor index split (Section 7) is
suggestive of the tangential reading, and three independent first-principles derivations resolve it
tangential at reconstruction grade, but this remains the load-bearing reconstruction-dependent choice. We
record both branches and do not hide the dependence.

*A scope correction.* The `RP^3` here is the deformation-retract **spine** of the metric fiber, not the
literal link of the noncompact end (which is 13-dimensional, a 9-dimensional `S^6`-bundle over `RP^3`).
The end-and-twist apparatus should be stated on a framed-bordism / `J`-homomorphism footing, and the
reduction from the 13-dimensional boundary to the `RP^3` spine is itself one of the open bridges
(Section 8). The `Z/3` cannot enter "for free" from the manifold: there is no `Z_3` anywhere in the metric
fiber, so every 3-divisible lens space and order-3 geometric route is foreclosed. The 3-primary class is
genuinely carried by the framing, or it is not present at all.

---

## 7. Relation to Geometric Unity, and to prior art

**Geometric Unity.** The sector is motivated by GU's matter proposal: the 14-dimensional observerse, the
vector-spinor (rank-3/2) field, the `4 + 10` split, the `16` of `Spin(10)`, and the self-dual structure of
the base. The tangential reading is consistent with several anchored features of the public draft -- the
vector-spinor matter field, the `TX (+) N` split of the Rarita-Schwinger index, the Levi-Civita connection
on the relevant sector, and the placement of gauge groups in the vertical sector. But the draft presents the
fermion sector schematically; it does not build the matter action; it states that chirality is only
*effective* and proposes a "2 + 1" picture (two true generations plus an effective imposter), not three true
generations; and Nguyen's published critique argues central technical details are not verifiable from the
public material. Our results are therefore a **reconstruction**, not a reading-off of GU, and where GU's own
narrative points (2 + 1), it points slightly against the strong "three generations" reading. We are explicit
about this throughout.

**Prior art.** Deriving or constraining the generation number from topology or anomalies has substantial
precedent, and we claim no novelty for that broad pitch:

- Dobrescu-Poppitz (2001): three generations from 6d global anomaly cancellation.
- Evans-Ibe-Kehayias-Yanagida (2011): three generations from a discrete `R`-symmetry anomaly.
- Kaplan-Sun (2012): three generations as surface modes of a 5d topological-insulator-like theory.
- Garcia-Etxebarria-Montero (2019): a `Z_9` anomaly forcing the generation number into `3Z`, alongside a
  mod-16 constraint on the 16 fermions per generation -- the clearest published case of odd-primary and
  2-primary constraints touching the family puzzle together.
- Juven Wang (2023): the family puzzle via framed/string bordism `Z/24` and `c_- = 24` -- the closest broad
  topological overlap. It does **not** use the Adams `e`-invariant, the `J`-homomorphism, or a
  2-vs-3-primary blindness as the mechanism.
- Wan-Wang-Yau (2026): decomposition of a family-number anomaly index into a 2-power piece and a 3-power
  piece, trivialized by `Z_4` and `Z_3` extensions -- the nearest published 2-vs-3-primary analogue. But the
  objects are discrete gauge-anomaly classes and symmetry extensions, not the `J`-image / `e`-invariant
  decomposition of `pi_3^s`.

**Our novelty claim, stated narrowly.** Recent work has connected family number to `Z/24`-valued
framed/string bordism, and has separately decomposed family-anomaly indices into 2-power and 3-power
sectors. We have not found prior work that (a) identifies the relevant generation/chirality obstruction
package as 2-primary and reads that as a structural **blindness** to an odd count, nor (b) places the
candidate count in the 3-primary summand of `pi_3^s` and reads it by the **Adams `e`-invariant / image of
`J`**. The mechanism is, to our knowledge, new. We cite Wang 2023 and Wan-Wang-Yau 2026 as the nearest
topological precursors and distinguish them on exactly this mechanism, rather than claiming they are
unrelated.

---

## 8. What is not claimed: the open bridge

We do **not** claim this proves three chiral generations. There is no standard theorem identifying a
boundary `e`-invariant with a net chiral generation count: APS, Dai-Freed, Callan-Harvey, and Bismut-Cheeger
relate boundary `eta` / `e` data to indices, determinant lines, anomaly phases, and cobordism classes, never
directly to an integer family count. Three explicit, currently-unbuilt steps stand between our 3-primary
class and the statement "the count is 3":

1. **A fibered-boundary index reduction.** APS on the 14-manifold applies to a 13-dimensional boundary
   operator. To replace that contribution by a scalar `e`-invariant on the `RP^3` spine requires a proven
   Bismut-Cheeger / adiabatic-limit / fibered-boundary reduction in which `RP^3` appears as the relevant
   fiber, not the assertion "the spine is `RP^3`."

2. **The Rarita-Schwinger index operator.** GU's matter sector is a reconstructed spin-3/2 sector; the
   physical RS index is a twisted Dirac index with a spin-1/2 ghost subtraction. One must write down the
   specific projected/twisted operator whose index equals the number of surviving `16`s of `Spin(10)`. This
   operator is not in the public draft.

3. **From an order-3 class to the integer 3.** A nonzero element of `Z/3` is information *modulo 3*, not the
   integer 3. Turning it into a count of exactly three uses the native multiplicity-three triplet (Section 2)
   plus a proof that only one copy of that triplet contributes chirally. Absent that, "the class has order 3"
   is not "there are 3 generations."

The honest statement is therefore: **there is a 3-primary topological/anomaly datum in a sector the
2-primary no-go cannot see, carried by a standard, published-referenced `e`-invariant computation; whether
that datum is the generation count is an open question with a precisely named bridge.** We pose the bridge,
and we request external review of both the core results and the bridge.

---

## 9. Status of claims

| Claim | Grade |
| --- | --- |
| The sector's no-go obstructions are all 2-primary (no odd-prime congruence) | Theorem (theory-independent) |
| The no-go is blind to the 3-primary part of a torsion-valued count | Corollary; contingent on the torsion-count reading |
| `pi_3^s = Z/24 = Z/8 (+) Z/3`, `|Im J_3| = 24`, `e` detects `Im J` | Theorem (Adams) |
| Self-dual tangential framing on `RP^3` has `e_R = 1/12`, 3-primary nonzero | Standard-result-applied (Kirby-Melvin, Randal-Williams) |
| Identification of the GU `Lambda^2_+` twist with that natural framing | Reconstruction-dependent |
| The `J` / Adams-`e` / 2-vs-3-primary mechanism is novel | Established by literature sweep (cf. Wang 2023, Wan-Wang-Yau 2026) |
| The 3-primary class is the net generation count = 3 | Open; not established (Section 8, bridges 1-3) |
| GU forces exactly three chiral generations | Not a theorem of the public draft; GU's own narrative reads "2 + 1" |

---

## 10. Conclusion

We have isolated, in an explicit Clifford Rarita-Schwinger sector, a clean structural fact: the entire
generation/chirality no-go is built from 2-primary statements and is therefore arithmetically incapable of
constraining an odd generation count. We have located the only place such a count could live -- the
3-primary summand of `pi_3^s`, read by the Adams `e`-invariant -- and we have exhibited a concrete nonzero
class there, `e_R = 1/12`, coming from the sector's native self-dual structure read tangentially, with
published support for the computation. We have been explicit that this does not establish three generations,
and we have named the exact bridge that would. The 2-primary blindness and the `J` / `e`-invariant mechanism
appear to be new. We submit the core as a theorem-grade contribution and the generation-count reading as a
motivated open conjecture, and we request external review.

---

## Appendix: reproducibility

The representation-theoretic decompositions (the `640 + 416 + 64` split of `ker(Gamma)` under `su(2)_+`, the
`(+96, -96)` Krein signature, the `12k`/`24k` indices, the self-dual family enumeration) are checked
numerically in `tests/generation-sector/` (`h1_selfdual_family_kill.py`, `t1a_kinematic_chirality_kill.py`,
`ghost_parity_krein.py`, `swing_ghost_parity_chiral_selection.py`, `a1_hypercharge_weighted_index.py`,
`a2_kr_equivariant_index.py`, `a3_gsm_ghost_parity.py`, `leg3_family_embedding_enumeration.py`). The
homotopy and `e`-invariant facts are standard (Adams; Kirby-Melvin; Randal-Williams). The supporting
adversarial deep-research reports are in `deep-research/`.
