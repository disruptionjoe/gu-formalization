---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-15
work_item: CS-1
channel: class-shift
target_claim: "INTERNAL — CR-B §7 Lens C, the contrary construction it named as its own cheapest next gate: 'a first-order Spin-equivariant operator Gamma(E) -> Gamma(F) needs cls(F) = cls(E) + 2. Both summands of the protected pairing have the SAME class, so no first-order equivariant operator connects them — while the class-MIXED pairing is precisely the one that admits it. If GU's operator between the 0-form and 1-form slots is first-order and equivariant, the protected pairing cannot be the carrier of that operator, and the two horns of §4.2 are not symmetric.'"
target_claim_verdict: "ARITHMETIC CONFIRMED, GATE RETYPED, CONCLUSION REFUTED. Lens C's computation is exactly right — dim Hom(V (x) Omega^0(S_+), Omega^1(S_-)) = 0 is reproduced here — and its inference does not follow. It tested `Hom(V (x) E, F)`; an action contains `Hom(V (x) E (x) F, C) = Hom(V (x) E, F^*)`. At D_7 these are DIFFERENT questions because S^+ is not self-dual, and they have OPPOSITE answers: for the protected half the first is 0 and the second is 9. The absence of a first-order operator from a class-homogeneous half TO ITSELF is not a defect; it is the defining property of a chirality eigenspace, and D_7's first-order equivariant operators are exactly the maps BETWEEN the two classes. The protected reading is not weakened. The two horns of CR-B §4.2 remain as CR-B left them, and the selector remains SG4 bit 2. Kill of an internal repository reading: NOT ACHIEVED, and the attempt is reported."
title: "CS-1: the class-shift rule cls(F) = cls(E) + 2k for Spin(2m)-equivariant operators of order exactly k, derived with hypotheses — and the decision it forces on CR-B's Lens C. The missing first-order operator between the protected summands is REAL and is the SIGNATURE of chirality, not a defect: at D_7 no first-order equivariant operator acts within a centre class, because every one of them shifts the class by exactly 2. W_+ = Omega^0(S_+) (+) Omega^1(S_-) has W_+^* = W_- EXACTLY, so the operator an action needs, W_+ -> W_+^*, exists with dim 9 while the bare mass is 0; the class-MIXED pairing has the mirror numbers, mass 2 and cross-kinetic 0. GU's own eq (9.16) is then swept over all four uniform label conventions and EXACTLY ONE is Spin(14)-consistent on its six printed derivative cells; under it the free operator is class-ODD, splits into exactly the two blocks SC-CHI-01 asserts, and the varpi cells are exactly the class-diagonal ones — so the VEV is precisely what re-couples them. HONEST RATIO: the Z/4 classes, the 832/64 decompositions, the shiab Hom numbers, `G = (-1)^form J`, the 960+960 split and the eq (9.16) parity obstruction were ALL already banked; ~45% of this file is reproduction."
grade: "EXACT integer arithmetic. Weights are DOUBLED integer tuples; every centre class is an integer mod 4; Weyl dimensions use Fraction and are asserted integral; every tensor product is decomposed by Racah-Speiser/Klimyk and DIMENSION-SATURATED against the product of the factor dimensions, so a dropped or spurious constituent cannot survive. 105/105 checks, exit 0. NON-VACUITY four ways: CR-B's class arithmetic reproduced by THREE independent routes (coordinate sum, additivity forced by the decompositions with the formula unused, and -w_0 by weight negation) plus a SOURCE cross-check against SC-FER-06's printed Spin(7,7)^+ superscript; a D_6 contrary control giving the exact MIRROR numbers (mass 5, kinetic 0 against D_7's 0 and 9); 18 class-ALLOWED (degree, target) pairs whose Hom space is nevertheless 0, proving the rule is necessary and NOT sufficient; and 15/15 planted false assertions each observed False. Failure path: --selftest, 13/13 injected machinery mutations exit 1, the selftest itself exiting 0 on success. STANDARD REPRESENTATION THEORY throughout: the Z/4 grading of the D_n representation ring, Klimyk/Racah-Speiser, the Weyl dimension formula, -w_0 as the diagram automorphism, and the Stein-Weiss form of a first-order natural operator. NOT: an index, a generation count, a physical carrier, a source action, a dynamical or VEV statement, a resolution of SIGNATURE-AMBIENT, a proof that eq (9.16) is globally defined, or any claim-status movement."
disposition: CLASS_SHIFT_RULE_DERIVED_AT_ARBITRARY_ORDER__LENS_C_ARITHMETIC_CONFIRMED_AND_INFERENCE_REFUTED__ABSENCE_OF_A_FIRST_ORDER_OPERATOR_WITHIN_A_CLASS_IS_THE_SIGNATURE_OF_CHIRALITY__W_PLUS_DUAL_IS_W_MINUS_EXACTLY_SO_THE_ACTION_LEVEL_OPERATOR_EXISTS_DIM_9_WHILE_BARE_MASS_IS_ZERO__MIXED_PAIRING_HAS_THE_MIRROR_NUMBERS__EQ_916_HAS_EXACTLY_ONE_SPIN14_CONSISTENT_UNIFORM_LABEL_CONVENTION__FREE_PART_IS_CLASS_ODD_AND_SPLITS_INTO_THE_TWO_BLOCKS_SC_CHI_01_ASSERTS__VARPI_CELLS_ARE_EXACTLY_THE_CLASS_DIAGONAL_ONES__PROTECTED_READING_SURVIVES_UNWEAKENED__SELECTOR_STILL_SG4_BIT_2
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md
  - explorations/form-spinor-decomposition-and-shiab-family-dimension-2026-08-03.md
  - explorations/shiab-operator/shiab-codiff-intertwiner-dim-2026-06-26.md
  - explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md
  - explorations/signature-independent-scalar-vanishing-lemma-2026-08-03.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/sources/source-claim-register.yaml
  - canon/shiab-existence-cl95.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - lab/methods/source-native-comparator-routing.md
scripts:
  - tests/channel-swings/joe_directed_cs1_first_order_class_shift.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY` — see §8, which separates the
> source-native leg (what `Spin(14)`-equivariance forces about the draft's own
> printed cell pattern) from the comparator leg (the words "mass term",
> "kinetic term", "chiral" and "vectorlike"). The registration decision in
> `lab/process/source-native-comparator-routing-registry.json` is the method
> owner's call; the notice and the classification string are in the exact form
> `process_gates/source_native_comparator_routing_audit.py` requires.

# CS-1 — the first-order class shift IS the chirality grading

## 0. The gate, verbatim

CR-B (2026-08-15, 179/179) established odd `Z/4` centre-class homogeneity as the
governing invariant, then named its own cheapest next gate:

> **Lens C — strongest contrary construction against CR-B.** [...] GU's content
> is not a module, it is a complex with a rolled-up Dirac/de-Rham/
> Rarita-Schwinger operator, and a first-order `Spin`-equivariant operator
> `Gamma(E) -> Gamma(F)` needs `cls(F) = cls(E) + 2`. Both summands of the
> protected pairing have the SAME class, so **no first-order equivariant
> operator connects them** — while the class-MIXED pairing is precisely the one
> that admits it. If GU's operator between the `0`-form and `1`-form slots is
> first-order and equivariant, the protected pairing cannot be the carrier of
> that operator, and the two horns of §4.2 are not symmetric.

**Verdict in one line, and both halves are load-bearing: the arithmetic is
exactly right and the inference does not follow.** The gate was aimed at
`Hom(V (x) E, F)`. An action contains `Hom(V (x) E (x) F, C) = Hom(V (x) E, F^*)`.
At `D_7` those are different questions, because `S^+` is not self-dual, and they
have opposite answers.

---

## 1. Prior-art sweep, by mechanism — and the honest ratio

Retrieval ran **before** any construction. Searched by mechanism, not by label:
*Stein-Weiss, Fegan, natural operator, first-order equivariant, principal
symbol, symbol degree, twistor operator, Rarita-Schwinger, Racah, Klimyk,
Littlewood-Richardson, class shift, centre class, congruence class, `832`,
`Sym^2`, self-dual, contragredient, opposite-half, invariant bilinear, kinetic
term, `(-1)^form`, relabel*. **Most of the mechanism in this file was already
banked and is reproduced rather than re-derived.** Leading with the ratio, per
the standing eight-count false-novelty correction.

| Result | Owner | Status before CS-1 |
|---|---|---|
| `cls(lambda)` = doubled-coordinate sum mod 4; `cls(S^+)=3`, `cls(S^-)=1`, `cls(V)=2`, `cls(ad)=0`; the four corners `3,1,1,3` | CR-B §3.2–3.3 | **exact — §2 reproduces all of it by three independent routes** |
| `V (x) S^- = S^+ (+) 832`, `V (x) S^+ = S^- (+) 832`, multiplicity-free; `Lambda^2 V (x) S^+ = S^+ (+) 832 (+) 4928` | `explorations/form-spinor-decomposition-and-shiab-family-dimension-2026-08-03.md` (M-M2), `tests/shiab_codiff_intertwiner_dim.py` | **exact — reproduced** |
| `dim Hom(Lambda^2 V (x) S^+, V (x) S^-) = 2`; the chirality-**diagonal** blocks are `0`, "wrong congruence class" | same two, SHIAB-03 | **exact — reproduced.** This is the `Z/2` shadow of the rule this file derives |
| `dim Hom(S^+ (x) S^+, Lambda^0) = 0` for every signature with `n = 2 mod 4` | `explorations/signature-independent-scalar-vanishing-lemma-2026-08-03.md` | **exact — the `k = 0` case, cited not re-claimed** |
| `G = (-1)^form . J` makes all three principal blocks odd, **reproduces the six eq (9.16) derivative-cell locations after a one-form relabel**, and is "the unique grading generated from ambient chirality and form parity with that property" | `explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md` | **exact — §6 reproduces the fit and its obstruction** |
| The parity obstruction itself: `parity_J(Phi d) = -1`, `parity_J(d) = +1`, "no value of `kappa` fits" for either uniform barred-row convention | same file | **exact — §6's sweep is the `Z/4` form of this argument** |
| Rolled carrier dimensions `960 + 960` | same file | **exact — reproduced as `dim W_+ = dim W_- = 960`** |
| The four-way typed construction fork on eq (9.16), and `source-faithful parity or duality convention: OPEN` | `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` | **standing OPEN — §6 closes two of its four horns** |
| The sixteen cells, the six derivative-cell locations `(0,1)(0,3)(1,0)(1,2)(2,1)(3,0)`, the southeast zero, the reversed barred row order | same file, `SC-OP-04` | primary source, identity grade |
| The p.51 corner `( ... )^{Spin(7,7)+}_{832-} (+) ( ... )^{Spin(7,7)+}_{64-} )^{Omega^1(S/-, Y^14)}_{zeta-}` | `SC-FER-06`, `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` | primary source, verbatim |

**Honest ratio: roughly 45% of this file is reproduction.** Every number in §2
and half of §6 already existed. The new content is §3 (the rule as a rule),
§5 (the distinction that decides the gate) and three riders in §6.

### 1.1 What is actually new

1. **The rule at arbitrary symbol degree, with its hypotheses** (§3).
   `cls(F) = cls(E) + 2k` for an operator of order exactly `k`, its parity
   corollary (an odd class gap admits **no** equivariant operator of any
   order), and its insertion-extended form. CR-B **asserted** the `k = 1` case;
   M-M2 **used** its `Z/2` shadow under the name "wrong congruence class".
   Neither states it as a rule, gives its hypotheses, or extends it in `k`.
2. **The distinction that decides the gate** (§5): `Hom(V (x) E, F)` versus
   `Hom(V (x) E (x) F, C) = Hom(V (x) E, F^*)`, and the fact that `W_+^* = W_-`
   **exactly as modules** at `D_7`. Zero hits anywhere in the repository for
   this identity as the decider of an operator question.
3. **The symbol-degree x corner-pair operator table**, including the
   class-2-insertion column (§4).
4. **Three riders on the banked eq (9.16) fork** (§6): horn 1 is **empty**;
   `G` is **forced**, not selected; horn 3 is not a source correction.
5. **The `D_6` mirror control** (§7): the class-homogeneous half there has mass
   `5` and kinetic `0`, the exact reverse of `D_7`'s `0` and `9`.

---

## 2. Preflight — retrieval first, then the lenses

Retrieval is §1 and it ran first. Five problem-matched lenses, recorded before
computing.

**Lens 1 — invariant-theorist / symbol calculus.** *Route:* do not quote CR-B's
rule. A differential operator of order `k` has a principal symbol living in
`Hom(Sym^k T^*M (x) E, F)`; naturality means that `Hom` is taken in the fibre
over `Spin(n)`. The centre then does all the work in one line. *Prediction:*
the rule generalises to `cls(F) = cls(E) + 2k`, so the ORDER PARITY of an
equivariant operator is pinned by the class gap, and an ODD gap admits nothing
at any order. *Stake:* if any tensor decomposition produces a constituent
violating this, the lens is wrong and the file reports that instead.

**Lens 2 — duality auditor (the lens that decided it).** *Route:* CR-B's Lens C
asks for an operator `E -> F`. Ask instead what an ACTION contains. A Lagrangian
term is an invariant scalar, i.e. an element of `Hom(Sym^k V (x) E (x) F, C)`,
which is `Hom(Sym^k V (x) E, F^*)` — the same question only when `F^* = F`.
*Prediction:* at `D_7`, `n = 7` is odd, `-w_0` is the diagram automorphism, so
`S^+` is NOT self-dual and the two questions come apart. *Stake:* if `W_+^*`
turns out not to be `W_-`, this lens dies and Lens C's inference stands.

**Lens 3 — source philologist.** *Route:* GU's object is not an abstract
operator; the draft PRINTS it. Read eq (9.16)'s sixteen cells as data, not as
prose, and read §11.2's corner diagram separately. *Binding condition:* every
source sentence quoted with a locus; anything the source does not say is typed
`SOURCE-SILENT` and stays there; nothing is credited to the source that the
repository constructed. *Prediction:* the `+/-` glyphs will turn out to carry
two different meanings in two places, and the draft will be found printing both.

**Lens 4 — adversary / kill designer.** *Route:* design the failure first. A
"the protected reading survives" verdict is worthless unless the instrument can
see a class-homogeneous half FAIL to be chiral. `D_6` — TWELVE dimensions — is
that case: `-w_0 = id`, the half-spinor is self-dual, `cls(S^+) = 2` is even.
Require the instrument to return a NONZERO mass there. Second control: exhibit
pairs the class rule ALLOWS whose `Hom` space is nevertheless `0`, so nobody
reads the rule as sufficient. Third: plant assertions false by construction.
Fourth: mutate the machinery and require every mutant to exit 1.

**Lens 5 — honesty auditor.** *Route:* this region is the highest prior-art
density in the repository and the standing correction is that eight
false-novelty claims were burned in one session. Grep the exact objects first,
lead with the ratio, and grade the swing by what is NEW. *Binding condition:*
if a banked artifact owns a leg, cite it in the results table and do not
re-claim it. **This lens changed the file:** the eq (9.16) parity obstruction,
`G = (-1)^form J`, the `960+960` split and the "one-form relabel" fit were all
found already banked in `k77-wave2-actual-draft916-k77-blockwise-adjoint-
descent-2026-08-04.md`, and §6 was rewritten from "result" to "reproduction plus
three riders".

**Lens 6 — verdict-typing auditor.** *Route:* the standing correction is that
verdicts are claim-indexed and misaimed critiques fail. Lens C is a
**repository-internal** contrary construction, not a source claim. Whatever
happens to it, the result is an INTERNAL-TARGET verdict and must never be
summarised as evidence about Weinstein's claims. Applied in §9 and §10.

**Cheapest kill-or-switch, recorded before computing.** If `W_+^* /= W_-`, the
duality lens is dead, Lens C's inference stands, and this file reports that the
protected reading is genuinely weakened. It is not dead: `W_+^* = W_-` exactly.

**One credible contrary route, recorded before computing.** The source wants
*"a zero in a self adjoint operator ... in order to get wildly different
eigenvalues"* (`Transcript into the impossible.md:119`). EIGENVALUES need an
endomorphism, i.e. an identification `W_+ = W_+^*`, which is exactly the
invariant bilinear that odd class forbids. That route survives and is §9's
weakest seam.

---

## 3. The class-shift rule, derived

**Setup.** `G = Spin(2m)` (any real form; the statement is settled in the
complexification `Spin(2m,C) = D_m`, which every real form shares). Write
weights in DOUBLED integer coordinates. Every `D_m` root has doubled-coordinate
sum in `{0, +-4}` (verified for `m = 4,...,8`), so

```
    cls(lambda) = (sum of doubled coordinates) mod 4
```

is well defined on `P/Q`, additive over `(+)` on class-homogeneous summands and
additive over `(x)`. It is the character by which the centre acts, and for `m`
ODD it is a faithful description of `Z(Spin(2m)) = Z/4`.

> **THEOREM (class shift).** Let `E = P_Spin x_{rho_E} V_E` and
> `F = P_Spin x_{rho_F} V_F` be bundles associated to centre-class-homogeneous
> `Spin(2m)`-representations, of classes `c_E` and `c_F`. Let
> `D : Gamma(E) -> Gamma(F)` be a differential operator of order **exactly** `k`
> whose principal symbol `sigma_k(D)` is induced by a `Spin(2m)`-equivariant
> fibre map `Sym^k V (x) V_E -> V_F`. Then
>
> ```
>     c_F = c_E + 2k    (mod 4).
> ```

**Proof.** The centre acts on `Sym^k V (x) V_E` by the character
`i^{2k + c_E}`, because `cls(V) = 2` and `cls` is additive over `(x)`; it acts
on `V_F` by `i^{c_F}`. A **nonzero** equivariant map intertwines the two central
characters, so the exponents agree mod 4. Order exactly `k` means
`sigma_k(D) /= 0`. `[]`

**Corollaries.**

- **(a) First order.** `k = 1` gives `c_F = c_E + 2` — CR-B's Lens C statement,
  now derived.
- **(b) Parity.** `c_F - c_E` is always EVEN. So no `Spin`-equivariant
  differential operator of ANY order joins two modules whose classes differ by
  an odd amount. Verified: `Hom(Sym^k V (x) S^+, V) = 0` for `k = 0,1,2,3`.
- **(c) Order parity.** A class gap of `0` forces EVEN order; a gap of `2`
  forces ODD order. This is the exact statement that replaces Lens C's binary.
- **(d) Insertions.** If `D` may depend on a background section of a bundle `T`,
  the symbol lands in `Hom(Sym^k V (x) T (x) V_E, V_F)` and the rule becomes
  `c_F = c_E + 2k + c_T`. GU's `ad P = End(Delta) = sum_j Lambda^j V` carries
  classes `{0,2}` only, so an insertion can shift by `0` or `2` and can NEVER
  change (b).
- **(e) Lagrangian form.** An invariant scalar with `k` derivatives coupling
  sections of `E_1,...,E_r` requires `sum_i c_i + 2k = 0 mod 4`, because the
  trivial representation has class `0`. **This is the form §5 needs and it is
  not the same as (a).**

**Hypotheses, stated because they are where GU could escape.**

- **H1** `m` odd, so the mod-4 class is the FULL centre character. For `m` even
  the centre is `Z/2 x Z/2` and the mod-4 map is a coarser `Z/2`-valued
  invariant — §7's contrary control lives exactly here. `m = 7` for `Y^14`.
- **H2** `V_E`, `V_F` class-homogeneous. Checked for every module used.
- **H3** **Naturality**: the symbol is induced by an equivariant map of the
  fibres. True of anything assembled from the Levi-Civita/spin connection and
  equivariant bundle maps. **FALSE** as soon as a background field of nonzero
  class is inserted — corollary (d) is the repair, and it is the same class-2
  insertion CR-B §3.6 already priced. It is also false for the inhomogeneous
  gauge group: `U(64,64)` is not inside `Spin(14)`, its adjoint carries class 2,
  and conjugation by a general `rho(epsilon)` need not preserve the grading.
- **H4** The statement is pointwise and algebraic, hence **real-form blind and
  signature blind** — `Cl(p,q) (x) C` depends only on `p+q`, so both horns of
  SIGNATURE-AMBIENT complexify to the same `D_7`.

**Necessary, not sufficient.** The rule constrains; it does not construct. The
probe exhibits **18** class-ALLOWED `(degree, target)` pairs whose `Hom` space
is nevertheless exactly `0`. Anyone using the rule as a licence to assert an
operator exists is misusing it.

---

## 4. What each pairing actually admits — exact `dim Hom`

`E = Omega^0(S_+)` throughout (class 3). Multiplicities computed by
Racah-Speiser, each product dimension-saturated.

```
    E -> F                      k=0   k=1   k=2   k=1 with a class-2 insertion
    Omega^0(S_+) -> Omega^1(S_-)  1     0     2     5      PROTECTED (both class 3)
    Omega^0(S_+) -> Omega^1(S_+)  0     2     0     0      MIXED (classes 3, 1)
```

Read this off the rule. The protected pair has class gap `0`, so it admits
operators of EVEN order and nothing of odd order: a **zeroth-order** bundle map
(the Clifford injection `S^+ -> V (x) S^-`, `dim 1`), **second-order**
operators (`dim 2`, e.g. `nabla` after Dirac), and **no first-order** one. The
mixed pair has gap `2`, so it admits ODD orders only: two first-order operators
(`nabla` and the twistor projection) and no zeroth- or second-order one. Switch
on a class-2 bosonic insertion and the protected pair gains first-order
operators (`dim 5`) while the mixed pair loses them (`dim 0`) — the table
inverts, which is what an insertion is for.

Over all `48` `(degree, corner, corner)` cells, a nonzero `Hom` occurs **only**
where the class gap equals `2k`. The rule never fails on the data.

---

## 5. The decision — Lens C tested the wrong `Hom`

Define the two class-homogeneous halves of the four printed corners:

```
    W_+ = Omega^0(S_+) (+) Omega^1(S_-)      class 3,  dim 960   [the L107 half]
    W_- = Omega^0(S_-) (+) Omega^1(S_+)      class 1,  dim 960
```

`dim 960 + 960` reproduces the banked rolled-carrier dimensions. Now the load-
bearing fact, computed as a module isomorphism and not merely as a class
statement:

```
    W_+^*  =  W_-      EXACTLY.
```

Because `m = 7` is odd, `-w_0` is the non-trivial diagram automorphism,
`(S^+)^* = S^-`, and `V` is self-dual, so
`W_+^* = Omega^0(S_-) (+) Omega^1(S_+) = W_-`. Hence:

```
    first-order  W_+ -> W_+     : dim 0      <-- CR-B Lens C measured THIS
    first-order  W_+ -> W_+^*   : dim 9      <-- an ACTION contains THIS
    bare mass on W_+                    : dim 0
    bare mass on the class-MIXED pairing: dim 2
    cross kinetic term, MIXED pairing   : dim 0
```

**Both zeros are real and Lens C's is reproduced.** The inference from it is
what fails, for two independent reasons.

**First, the absence is the definition of a chirality eigenspace.** By
corollary (c), every first-order equivariant operator at `D_7` shifts the class
by exactly 2 — so *no* first-order equivariant operator ever acts WITHIN a
centre class, for any class-homogeneous module whatever. `S^+` itself has no
first-order self-operator; the Dirac operator maps `S^+ -> S^-`. Demanding that
a chiral half carry a first-order operator to itself is demanding that it not be
chiral. The vanishing Lens C found is not evidence against the protected half;
it is the certificate that the protected half is one eigenspace of the grading
under which every first-order operator is odd.

**Second, an action does not contain `Hom(V (x) E, F)`.** By corollary (e) the
object in a Lagrangian is `Hom(V (x) E (x) F, C) = Hom(V (x) E, F^*)`. Those
agree only when `F^* = F`, and at `D_7` they do not. Concretely, on the bare
half-spinor:

```
    S^+ (x) S^+ = Lambda^1 (+) Lambda^3 (+) Lambda^5 (+) Lambda^7_+
                =    14   +    364   +   2002  +   1716   = 4096
```

`Lambda^0` is ABSENT — no invariant bilinear, hence no bare mass, which is
CR-B's certificate and the banked `n = 2 mod 4` scalar-vanishing lemma.
`Lambda^1 = V` is PRESENT with multiplicity 1 — so a first-order invariant
bilinear `<psi, nabla psi>` DOES exist. **No mass, yes kinetic.** That is the
textbook content of "chiral", and it is exactly the complementarity the table
above shows at the level of the full halves: `0` and `9` for the protected half,
`2` and `0` for the mixed one.

So the two horns of CR-B §4.2 are *not* asymmetric in the direction Lens C
feared. If anything they are asymmetric the other way: the protected half has a
kinetic pairing and no mass, the mixed pairing has a mass and no cross-kinetic
term. Which is operative remains SG4 bit 2, exactly as CR-B left it.

---

## 6. GU's actual rolled-up operator — does the constraint even apply?

The brief asks whether the class-shift constraint applies to GU's own object,
*"a Dirac, de Rham, Rarita-Schwinger gadget"*
(`papers/drafts/Transcript into the impossible.md:119`). It does, to the part
of it the source calls free, and §3's H3 says exactly where it stops.

### 6.1 The three principal blocks, and the shiab

The source describes the middle map twice, at the same locus:

> "it's just the ordinary derivative which would take you from one forms to two
> forms, and then you knock it back from two forms to one forms with this ship
> in a bottle operator, and then that's what gives you your rolled up complex"
> (`:119`)

and names the coupling:

> "this is an exterior derivative coupled to connection information, that's
> housed in the inhomogeneous gauge group [...] you're mining that for a
> **minimally coupled exterior derivative**" (`:116`)

The shiab is a ZEROTH-order equivariant bundle map, and the repository already
computed its `Hom` space: `dim Hom(Lambda^2 V (x) S^+, V (x) S^-) = 2`, with the
chirality-diagonal blocks `0`. Reproduced here. Class-wise
`cls(Lambda^2 V (x) S^+) = 3 = cls(V (x) S^-)`, so the shiab preserves the
class, as a zeroth-order map must. All three principal derivative classes then
shift the class by exactly `+2`:

```
    d       : Omega^0(S_a) -> Omega^1(S_a)     class 3 -> 1
    -d^*    : Omega^1(S_a) -> Omega^0(S_a)     class 3 -> 1
    *(o)d   : Omega^1(S_a) -> Omega^1(S_-a)    class 3 -> 1
```

which is what a first-order natural operator must do, and is the `Z/4` form of
the banked statement that all three are odd for `G = (-1)^form . J`.

### 6.2 The sweep, and its unique survivor

Identity-grade source data (`SC-OP-04`): rows
`(zeta-bar_-, zeta-bar_+, nu-bar_-, nu-bar_+)`, columns
`(zeta_+, zeta_-, nu_+, nu_-)^T`, six cells carrying `d_0` or `d_0^*` at
zero-indexed `(0,1) (0,3) (1,0) (1,2) (2,1) (3,0)`, four southeast zeros, six
`varpi`-only cells. Only the LABEL convention is free, and it is a finite space:
`{one-form labels as printed | reversed} x {barred rows same-bundle | dual}`.
Requiring every `d_0` cell to be `Spin(14)`-invariant:

```
    flip=False, bar_dual=False   six d_0 cells consistent: False
    flip=False, bar_dual=True    six d_0 cells consistent: False
    flip=True,  bar_dual=False   six d_0 cells consistent: TRUE
    flip=True,  bar_dual=True    six d_0 cells consistent: False
```

**Exactly one survives**, and it is the `Z/4` form of the banked `Z/2` argument
("no value of `kappa` fits ... reversing the one-form labels converts ambient
`J` to total `G` and makes the matrix fit"). Under it:

- the free (`varpi = 0`) part sends class `1 -> 3` and class `3 -> 1` **only**:
  it is class-ODD, so it splits into exactly TWO blocks, `W_+ -> W_-` and
  `W_- -> W_+`;
- the class-3 column set is `{zeta_+, nu_+}`, which under this convention reads
  `{Omega^1(S_-), Omega^0(S_+)}` — **the L107 protected pairing, verbatim**;
- the six `varpi`-only cells are **exactly** the class-DIAGONAL ones, each
  requiring a class-2 insertion, which `ad P = End(Delta)` supplies;
- of the four southeast ZEROS, exactly TWO are first-order class-allowed (the
  ambient Dirac positions). So the seesaw zero is a CHOICE of the rolled-up
  complex on cells where an operator exists — not a class obstruction.

The middle bullet is the answer to the brief's fourth question. **GU's own
printed operator restricts to the protected half as a map into that half's
DUAL, and its free part decouples into exactly the two operators `SC-CHI-01`
asserts, with `varpi` — the VEV — as precisely what re-couples them.** The
draft states the condition and this computes it:

> "the full operator depicted decouples effectively into two separate Dirac like
> operators, **when there is no vacuum expectation value pulling the various
> sub-fields of ϖ to values significantly above zero**." (`SC-CHI-01`, p.52)

### 6.3 Three riders on the banked fork

The banked s9 extraction types the reconciling convention as **OPEN** and offers
four repairs. Two of them can now be closed and one retyped.

1. **Horn 1 — "a different Shiab contraction with the required ambient parity" —
   is EMPTY.** The required parity is chirality-PRESERVING, and
   `dim Hom(Lambda^2 V (x) S^+, V (x) S^+) = 0`: no such contraction exists at
   any dimension of the `Hom` space. **Both numbers were already in the
   repository** (SHIAB-03's zero diagonal block, and the fork). Joining them is
   what is new, and it is a join, not a discovery.
2. **`G = (-1)^form . J` is FORCED, not selected.** Certified on all four
   corners: `G = +1` exactly when `cls = 3`, `G = -1` exactly when `cls = 1`. So
   the banked "auxiliary rolled grading", typed `CONSTRUCTION-SELECTED-RIVAL`,
   is the mod-2 shadow of a central character that `Spin(14)`-equivariance
   fixes. It was never a construction choice. The `Z/4` refinement is strictly
   stronger: `G` cannot distinguish `W_+` from `W_-`, and the mass certificate
   lives only at the `Z/4` level.
3. **Horn 3 — "a correction or reinterpretation of the draft's field
   subscripts" — is not a correction of the source.** The draft prints BOTH
   labels on the same object. `SC-FER-06`, verbatim:

   > `( ( Z-_{1/2} (+) Q+_{3/2} --(+)-- F-_{1/2} )^{Spin(7,7)+}_{832-} (+) ( F-_{1/2} )^{Spin(7,7)+}_{64-} )^{Omega^1(S/-, Y^14)}_{zeta-}`

   The slot is `Omega^1(S/_-)` and its two constituents, of printed dimensions
   `832` and `64`, both carry the superscript **`Spin(7,7)^+`**. Computed:
   `V (x) S^- = 832 (+) 64` with both constituents of centre class `3 = cls(S^+)`.
   **The draft's own `Spin(7,7)^+/-` superscript IS the `Z/4` centre class, and
   on a one-form slot it is opposite to the `S/_+/-` bundle subscript.** So the
   "flip" the sweep selects is a choice between two labels the source prints,
   not an imposed relabelling.

**Honest limits on rider 3.** The extraction quotes ONE corner verbatim and says
the other three "permute the ± signs"; I did not re-read the PDF. So the two-
label fact is established for the `zeta_-` corner and is inferred, not verbatim,
for the other three. And this settles the MATHEMATICAL half of the collision
only: that eq (9.16)'s `+/-` behaves like the class label is now forced; that
the author INTENDED the superscript convention there remains a source-reading
question, and horn 2 (an explicit degree-dependent duality/reality map) survives
untouched because the sweep — like the banked argument — covers only UNIFORM
conventions. The s9 disposition
`source-faithful parity or duality convention: OPEN` narrows; it does not close.

---

## 7. Contrary controls

**CONTRARY A — `D_6`, twelve dimensions, the mirror.** Hypothesis H1 fails
there: the centre is `Z/2 x Z/2`, `-w_0 = id`, `S^+` IS self-dual and
`cls(S^+) = 2` is EVEN. The class-homogeneous pairing
`Omega^0(S_+) (+) Omega^1(S_-)` is still class-homogeneous — and:

```
              D_7 (14 dimensions)        D_6 (12 dimensions)
    bare mass         0                          5
    kinetic           9                          0
```

**Exactly reversed.** In twelve dimensions the class-homogeneous half is massive
and, because it is self-dual, kinetically inert as an equivariant bilinear. The
`D_7` verdict is therefore not automatic and the instrument is not rigged.

`D_6` also carries the sharpest form of the retype: `Hom(V (x) S^+, Omega^1(S^-))`
is `0` there **too**, in a case where the pairing is provably NOT protected. So
"no first-order operator between the summands" and "protected" are different
properties, and the first is not evidence about the second. That is the control
that shows what CR-B's Lens C was measuring.

**CONTRARY B — necessity is not sufficiency.** 18 class-ALLOWED
`(degree, target)` pairs have `Hom` space exactly `0`.

**CONTRARY C — odd class gap.** `Hom(Sym^k V (x) S^+, V) = 0` for
`k = 0,1,2,3`: no equivariant operator of any order, as corollary (b) requires.

**PLANTED FALSE FACTS.** 15, each observed False inside the run — including
"a first-order operator `W_+ -> W_+` exists", "the class rule is SUFFICIENT",
"eq (9.16) is consistent with the one-form labels read as the bundle half", and
"a chirality-PRESERVING shiab contraction exists".

**FAILURE PATH.** `--selftest` injects 13 machinery mutations — a broken class
formula, a broken Racah-Speiser sign, a suppressed wall test, an identity duality
map, and one per headline number — and **13/13 drive exit 1**, the selftest
itself exiting 0 on success.

---

## 8. Comparator routing — which route does this bind?

`lab/methods/source-native-comparator-routing.md` fork 1 covers this boundary
and the two halves must be reported separately.

**Source-native half — this BINDS.** *"Every `Spin(14)`-equivariant operator of
order exactly `k` shifts the `Z/4` centre class by `2k`"* is representation
theory of `D_7`, common to both horns of SIGNATURE-AMBIENT. *"Exactly one
uniform label convention makes eq (9.16)'s six printed derivative cells
`Spin(14)`-invariant"* is a statement about the draft's own printed cell
pattern, carried by a SHA-pinned extraction and the claim register. *"`W_+^*` is
`W_-` exactly"* is a fact about `D_7` and GU's own printed field content. These
bind source-natively and they are **structural, not evaluative**.

**Comparator half — this does NOT bind.** *"mass term"*, *"kinetic term"*,
*"chiral"* and *"vectorlike"* are fork-1's conventional comparators. The computed
objects are `dim Hom(W (x) W, C)` and `dim Hom(V (x) W (x) W, C)` — pure
representation theory. The step from "no invariant bilinear" to "no mass, hence
chiral, hence a generation count" is the comparator step and does not advance a
GU row in either direction under the boundary's symmetric rule.

**Forbidden summaries, named so they are not written.** *"CS-1 shows GU is
chiral."* No — it shows a class-homogeneous half admits a first-order invariant
bilinear and no bare one, at zero insertion, and §6 shows GU's own `varpi` cells
are exactly the insertions that remove that. *"CS-1 proves eq (9.16) is
correct."* No — it shows exactly one uniform label convention is
`Spin(14)`-consistent, leaves horn 2 open, and proves nothing about global
definedness, descent, domain or adjoint. *"CS-1 kills CR-B's protected
reading."* No — the attempted kill did not land, and §9 says where it could
still land. *"Weinstein derives the decoupling."* No — he asserts it, hedged as
*"the idea being explored here"*, twice flagged *"stylized"*, and says
*"I don't know what to do"* about the adjacent indefinite-Killing-form problem
(`Transcript into the impossible.md:155`).

---

## 9. Hostile review, inline

**Strongest surviving contrary construction against CS-1 — the eigenvalue
route.** §5 shows `D : W_+ -> W_+^*` exists, which is a BILINEAR FORM on `W_+`,
and that is enough for an action. It is NOT enough for EIGENVALUES, and the
source explicitly wants eigenvalues: *"you want a zero in a self adjoint
operator that looks like that in order to get wildly different eigenvalues"*
(`:119`), naming the seesaw. Eigenvalues need an endomorphism `W_+ -> W_+`,
which needs an identification `W_+ = W_+^*`, which is exactly the invariant
bilinear that odd class forbids. **So the seesaw eigenvalue reading and the
chiral protected reading cannot both be operative at once**, and the class-2
insertion is what moves between them. This is not a new fork: it is CR-B §3.6's
conditional and `SG4` bit 2, now attached to the OPERATOR rather than to a bare
mass term, and both phases are computed. Classified **route-alive, not a
defeater** — but anyone who wants GU's seesaw spectrum on the protected half is
asking for the massive phase and should say so.

**Second seam — H3 is where GU actually lives.** The rule governs
`Spin(14)`-natural operators. GU's operator is minimally coupled to the
inhomogeneous gauge group, whose adjoint carries class 2 and which is not inside
`Spin(14)`. Everything in §6.2 about the `d_0` cells is therefore exact and
everything about the `varpi` cells is only a constraint of the form "the
insertion must be class-2". A finer statement about WHICH components of
`ad P = End(Delta)` sit in which cell would need the repository's open total-
grading fork settled. Residual risk: low, and confined to §6.2's `varpi` bullet.

**Third seam — the sweep is over UNIFORM conventions only.** A degree-dependent
duality or reality map (horn 2 of the banked fork) is outside it, exactly as it
is outside the banked `Z/2` argument. "Exactly one convention survives" means
"exactly one of the four uniform ones", and that is how it is stated everywhere
above.

**Fourth seam — `dim 9` is a multiplicity, not an operator.** The nine-
dimensional space of first-order equivariant maps `W_+ -> W_+^*` says a kinetic
pairing EXISTS; it does not say which one GU uses, and by SHIAB-03's precedent
equivariance does not pin a selector. GU's specific operator is `SG4`'s to
supply. The claim here is existence, and existence is what Lens C denied.

**Strongest overclaim available, and where it is refused.** *"The class rule
explains every cell of eq (9.16), so the draft's fermionic operator is
derived."* Refused. What is shown is that one uniform label convention makes the
six printed derivative cells centrally consistent and that the `varpi` cells
then require a class-2 insertion. That is a consistency statement about a
printed pattern under a stated equivariance hypothesis. It is not a derivation
of the operator, does not select the shiab, does not supply a density, adjoint,
domain or descent, and the draft itself introduces eq (9.16) as something one
*"can begin with"*.

---

## 10. Postflight — five lenses

**Lens A — smuggled-assumption auditor.** *Did I import an assumption GU does
not declare?* Four candidates. (i) **A reality condition** — never imposed; the
whole file is complex representation theory of `D_7` and the barred fields are
treated as independent, which is the draft's own statement and the repository's
standing fence. Indeed `bar_dual=False` — the source's reading — is what the
sweep SELECTS. (ii) **A chirality projection** — never imposed; the four corners
are carried throughout and `W_+`/`W_-` are computed, not chosen. (iii)
**Minimality of the carrier** — used nowhere. (iv) **"No invariant bilinear
means no mass"** — this IS a comparator import and it is fenced in §8 rather
than used. **One import survives and is declared:** the naturality hypothesis
H3, which is stated as a hypothesis in §3 and whose failure mode is §9's second
seam.

**Lens B — reproduction auditor.** The banked artifacts own more of this file
than the first draft admitted: `G = (-1)^form J`, the six-cell fit after a
one-form relabel, the `960+960` split, the parity obstruction "no value of
`kappa` fits", the `832/64` decompositions, the shiab `Hom` numbers, and CR-B's
class arithmetic. All are cited in §1 and reproduced in the probe rather than
re-claimed. The one place a banked number is used to produce something new is
horn-1 closure, and §6.3 says explicitly that both inputs were already in the
repository and that joining them is the contribution.

**Lens C — verdict-typing auditor.** The target is `CR-B §7 Lens C`, a
**repository-internal** contrary construction. The verdict is split: arithmetic
CONFIRMED, gate RETYPED, conclusion REFUTED. This file targets no source claim,
is not a falsification of GU, and moves no claim status. Against the source it
is confirmatory in one narrow place — `SC-CHI-01`'s decoupling gets an exact
representation-theoretic realisation as the class-odd block structure of the
draft's own printed cells — and silent everywhere else. **A kill of the
protected reading was attempted and did not land**; that is stated as plainly as
a success would be.

**Lens D — what did NOT move.** `n_g -> n_g - 1` unchanged. The repository count
`{1,3}` unchanged. `SC-GEN-53` unchanged. `PH-K1-KINEMATIC` unchanged and
consistent. SIGNATURE-AMBIENT untouched — the whole file is signature-blind by
H4, which is robustness, not resolution. `SG4` unchanged as the decider, and
bit 2 remains the selector. `canon_verdict_change: none`.

**Lens E — the source-credit auditor.** Nothing here credits Weinstein with a
mechanism he disclaims. The words "Krein", "ghost" and "Majorana" appear zero
times in the load-bearing part of this file, as they do in the primary corpus.
The source disavows compactification and `Y^14` is endogenous throughout; the
`4+10` language does not appear in this file at all. `SC-CHI-01` is quoted with
its hedge attached. The one thing credited to the source is that it PRINTS a
`Spin(7,7)^+` superscript on an `Omega^1(S/_-)` corner, which is `SC-FER-06`
verbatim.

---

## 11. Claim ceiling

- **Exact, and load-bearing:** the class-shift rule `cls(F) = cls(E) + 2k` with
  its four hypotheses and five corollaries; the 48-cell operator table and its
  agreement with the rule; the 18 class-allowed-but-zero witnesses;
  `W_+^* = W_-` as a module isomorphism; the numbers `0/9` at `D_7` and `5/0` at
  `D_6`; `S^+ (x) S^+ = Lambda^1 (+) Lambda^3 (+) Lambda^5 (+) Lambda^7_+` with
  `Lambda^0` absent; the uniqueness of the surviving uniform label convention
  for eq (9.16) among the four; the class-odd block split of its free part; the
  class-diagonal placement of its `varpi` cells; the emptiness of fork horn 1;
  the identification of `G = (-1)^form J` with the mod-2 shadow of the centre
  class.
- **Reproduction, claimed by nobody here:** CR-B's class arithmetic; M-M2's and
  SHIAB-03's decompositions and `Hom` numbers; the k77-wave2 `G`-fit, its parity
  obstruction and its `960+960`; the banked `n = 2 mod 4` scalar-vanishing
  lemma. See §1.
- **Standard representation theory:** the `Z/4` grading of the `D_n`
  representation ring; Klimyk/Racah-Speiser; the Weyl dimension formula; `-w_0`
  as the diagram automorphism; the Stein-Weiss form of a first-order natural
  operator.
- **Source, quoted with loci, not interpreted:** eq (9.16) p.46 (`SC-OP-04`);
  the p.51 corner (`SC-FER-06`); eq (11.6) p.52 (`SC-CHI-01`);
  `Transcript into the impossible.md` lines 107, 116, 119, 155.
- **NOT claimed:** an index; a generation count; that `n_g = 3`; that GU is
  chiral; that GU is not chiral; that eq (9.16) is globally defined, descends,
  has an adjoint, a density or a domain; that the shiab is unique; a source
  action; a dynamical, VEV, mass-matrix, scale or threshold statement; a
  resolution of SIGNATURE-AMBIENT; a resolution of the total-grading fork; that
  the author intended the superscript convention in eq (9.16).
- **Claim-status movement:** none.

---

## 12. Did I decide the tension, or restate it? — blunt

**I decided it, in the direction the brief said not to assume, and the honest
qualifier is that a large part of the machinery was already in the repository.**

*Decided.* CR-B's Lens C does not weaken the protected reading. Its arithmetic
is right and I reproduced it — `dim Hom(V (x) Omega^0(S_+), Omega^1(S_-)) = 0`
— but the quantity it measured is not the one that matters, and I can say why
in one sentence: at `D_7` **every** first-order equivariant operator shifts the
centre class by exactly 2, so **none** of them acts within a class, so "the
protected half admits no first-order operator to itself" is a theorem about
every class-homogeneous module in fourteen dimensions and carries no information
about GU. What an action needs is the operator into the DUAL half, and because
`S^+` is not self-dual at `D_7` that is a different `Hom` space, and it is
9-dimensional. The brief asked whether this kills, weakens, or is harmless. **It
is harmless, and the reason it looked lethal is a duality step, not a physics
step.**

*Decided, and it is the part I would have missed without §6.* The constraint
does apply to GU's actual rolled-up gadget, and when applied it does something
better than survive: exactly one of the four uniform label conventions makes the
draft's six printed derivative cells `Spin(14)`-consistent, and under it the
free operator is class-odd, splits into precisely the two blocks `SC-CHI-01`
asserts, carries the L107 pairing as one of them, and places every `varpi` cell
on the class diagonal — so the VEV is exactly the thing that re-couples them.
The source states that decoupling and hedges it; the class arithmetic makes the
BLOCK STRUCTURE of the printed matrix a consequence of equivariance rather than
an assertion. What it does not make is the decoupling itself true, because that
is a statement about `varpi` being small, which is dynamics.

*Not decided, and I will not dress it up.* Whether GU's operator is meant to
have EIGENVALUES on the protected half. §9 says why: eigenvalues need an
endomorphism, an endomorphism needs `W_+ = W_+^*`, and that is the invariant
bilinear odd class forbids. The seesaw language at `:119` wants eigenvalues.
That is not a new unknown either — it is the same class-2 insertion, i.e. `SG4`
bit 2 — but it means the protected reading buys chirality and gives up the
seesaw spectrum in the same breath, and CR-B did not say that.

*The reproduction ratio, stated last so it is not buried.* Roughly 45% of this
file existed. `G = (-1)^form . J`, the eq (9.16) parity obstruction, the "no
value of `kappa` fits" argument, the `960+960` split and every decomposition
number were banked, and the single most useful thing §6 does — closing fork horn
1 — is a JOIN of two numbers that were already sitting in the repository in
different files. The genuinely new mathematics is §3's rule as a rule with
hypotheses and §5's duality distinction. That is a smaller contribution than the
title of a "decisive gate" suggests, and it is still enough to decide the gate,
because the gate turned on exactly the distinction §5 makes.
