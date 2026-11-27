---
title: Full-curvature Shiab companions and a nonzero Einstein-response survivor
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Classify the ordinary exterior-symbol companion condition, decide it for the selected displayed Shiab, and test whether that condition itself excludes nonzero Riemann response.
actual_delta: Every algebraic companion pair is a coefficient-linear wedge pair; the selected displayed map has a realizable full-connection-jet obstruction, while an explicit wedge anticommutator has a companion and nonzero Einstein response.
class_covered: Pointwise linear maps from two-forms to degree13 forms with arbitrary finite-dimensional coefficient spaces in dimension14, tested against every ordinary exterior symbol; all algebraic degree3 companions are quantified. The selected and positive examples use the full complex Dirac matrix carrier, with separately stated primary-minus full-unitary reality.
premises:
- lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md
- lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md
- lab/sources/gu-shiab-bianchi-two-connection-target-source-reinspection-2026-08-05.md
- lab/sources/source-claim-register.yaml#SC-OP-02
- lab/sources/source-claim-register.yaml#SC-OP-03
- explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md
- explorations/conditional-build/shiab-graded-derivation-class-2026-11-27.md
source_bridge:
  status: conditional
  reason: The source supplies the operator degrees, possible invariant ingredients and conditional derivation intent, but does not require this universal full-adjoint exterior companion square or identify it with the spinor/somatic cancellation. The positive example is not a source-selected replacement.
kill_condition: A closed full-curvature symbol input with nonclosed selected output excludes every companion in the declared square. A nonzero Einstein-response wedge pair refutes the stronger claim that the square itself forces Riemann silence.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-FULL-CURVATURE-SHIAB-COMPANION
target_claim_verdict: Selected-map companion interpretation excluded; nonzero Einstein-response wedge companions remain possible. No source-necessary exclusion established.
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# Full-curvature companions: obstruction and positive survivor

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Classify the ordinary exterior-symbol companion condition, decide it for the selected displayed Shiab, and test whether that condition itself excludes nonzero Riemann response.
actual_delta: Every algebraic companion pair is a coefficient-linear wedge pair; the selected displayed map has a realizable full-connection-jet obstruction, while an explicit wedge anticommutator has a companion and nonzero Einstein response.
```

## Result first

**The selected displayed Shiab has no companion for the universal full-curvature exterior square. The square nevertheless permits nonzero Einstein response.** The distinction is explicit: every algebraic companion is a wedge map with a coefficient-linear action, and a wedge anticommutator supplies a positive example. It agrees, up to normalization, with the selected map on Riemann curvature while differing on general connection curvature.

The negative result quantifies over every companion, not one candidate. It uses an actual connection jet with vanishing curvature value and nonzero derivative, so moving coefficients and lower-order terms do not repair the held square. The positive result prevents extending that obstruction to every module/wedge interpretation of Shiab. Neither result identifies the source's unpublished spinor construction or an action's full Euler complex.

| State | Scope |
|---|---|
| ESTABLISHED by the written proof | Complete pointwise companion classification; selected-map obstruction; explicit nonzero-Einstein companion pair. Execution and acceptance evidence are recorded separately. |
| RULED OUT | Universal ordinary exterior/Bianchi factorization for the held selected degree-two map on all connection-curvature jets. |
| SURVIVES | Coefficient-linear wedge companions, including the explicit full-unitary real anticommutator under the primary-minus convention. |
| NOT MODELED / UNDETERMINED | Source selection, extra same-order rows, a different outgoing symbol, the full moving two-connection law, action/Euler ownership, physical domains, observed gravity and GU-wide falsification. |

```gu-typed-objects
result: complete algebraic companion class with selected-map obstruction and positive wedge survivor
carrier: Lambda2(Vstar) tensor E to Lambda13(Vstar) tensor Eprime; examples E=Eprime=End_C(S128), full Dirac in dimension14 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: no pairing required for the classification; metric and orientation define example Hodge and Clifford maps ON=ambient_tensors
real_structure: complex classification; primary-minus gamma_i sharp-skew supplies the stated full u(H) examples; K77 and K95 conventions are separately bound
grading: exterior degree only; coefficient matrices have degree0; no source Bose/Fermi grading substitution
action_owner: repository-construction of a structural interpretation test; no action selected or varied
target: ordinary exterior-symbol square between degrees2/3 and13/14 MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Adjoint-valued degree-raising Shiab and spinor-valued degree-lowering Shiab are distinct maps. An exterior companion is not a full graded derivation, a complete Euler identity, or a physical2+1 construction. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Source premise and exact reuse difference

The [Portal transcript](../../lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md) supplies invariant Phi ingredients and product freedom at **01:36:44**, the suite `Omega^i(ad) -> Omega^(d-3+i)(ad)` at **01:37:34–01:39:38**, and spinor0/1-form somatic cancellation at **01:47:01–01:51:50**. The phrase **“if shiab is a derivation”** occurs at **01:48:59**. This is a source hook, not a definition of the full-adjoint square studied below.

The [source reinspection](../../lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md) binds draft pp42–44/Def8.1/eq8.7 and eqs9.2–9.6 to the invariant family, displayed degree-two formula and Euler degrees. SC-OP-02 (`UNCERTAIN`) preserves the missing historical selector in §8.2/p43 footnote10; SC-OP-03 (`ASSERTS`) attributes the displayed Weyl-killing/Ricci-scalar response and allows other Shiabs. Draft §10/eqs10.1–10.9 also contains distinct moving-contraction terms. The source relation `Xi=D Upsilon` is a residual relation, **not** an assertion that `D S2(F)` vanishes off shell. The unreleased2025 two-connection construction does not supply the required equality of carriers and outgoing symbols; see [its source custody](../../lab/sources/gu-two-connection-shifted-superconnection-source-reinspection-2026-08-04.md).

The following owned results have different premises:

* [August5 principal-Bianchi selector](../k77-wave2-principal-bianchi-product-selector-2026-08-05.md): rank91 principal **Riemann spin** jets, coefficient grade2, with a unique nonzero-Einstein survivor among eight fixed product assignments. The witness here uses coefficient grade1 on the full connection carrier.
* [Full graded-derivation theorem](shiab-graded-derivation-class-2026-11-27.md): all-degree associative or graded-Lie Leibniz law. The positive wedge pair below does not satisfy that stronger premise.
* [Full-adjoint/path-moment result](../k77-wave2-full-adjoint-shiab-bianchi-two-connection-target-2026-08-05.md): five-dimensional displayed-map span and pre-Shiab Bianchi syzygy; it leaves the product-sensitive companion open.
* [Degree14 northeast totalization](../k77-wave2-action-owned-degree14-northeast-totalization-2026-08-05.md): particular degree-three candidates and a differently typed raw northeast owner; it does not quantify over every companion in the square below.

The mathematical ingredients are classical exterior algebra. [Stacks Project, Koszul complexes, tag062J](https://stacks.math.columbia.edu/tag/062J) supplies related exterior-algebra/differential context; it is not cited as proving this particular Shiab classification. The proof below is self-contained. No world-novelty claim is made.

## 2. Complete companion classification

Let W be a vector space of dimension n>=3 over R or C, and E,E' arbitrary finite-dimensional coefficient spaces. Fix a linear map

```
S2: Lambda2(W) tensor E -> Lambda^(n-1)(W) tensor E'.
```

The following conditions are equivalent:

1. There is a linear map `S3:Lambda3(W) tensor E -> Lambda^n(W) tensor E'` such that

   `k wedge S2(F) = S3(k wedge F)` for every k,F.

2. `k wedge S2(k wedge a)=0` for every k in W and a in W tensor E.

3. There is a unique tensor `Theta in Lambda^(n-3)(W) tensor Hom(E,E')` such that S2 is **right wedge by Theta**, applying its Hom coefficient to the input coefficient.

In condition3, S3 is uniquely the same right-wedge operation on degree3. No metric, equivariance, matrix multiplication, adjoint or full Leibniz law is assumed. The plus convention in condition1 is fixed here; the odd-degree chain-map convention with a minus has the same class after replacing S3 by -S3.

**Proof.** Choose a nonzero volume. The canonical identification

`Lambda^(n-1)(W) = W* tensor det(W)`

writes S2 as an output vector with components `X^a(F)=(1/2)T^{a|bc}F_bc`, where T is skew in b,c and has Hom(E,E') coefficients. Condition2 is

`k_a k_b T^{a|bc} a_c = 0`.

For each c and input coefficient, polarizing k makes T skew in a,b. Together with its given skewness in b,c, this makes T fully alternating in all three indices. Such tensors are precisely

`Lambda3(W*) tensor det(W) tensor Hom(E,E') = Lambda^(n-3)(W) tensor Hom(E,E')`,

which is condition3. That right-wedge formula immediately gives condition1, and condition1 implies condition2 because k wedge k=0. Finally, the elements k wedge F span Lambda3(W) tensor E, so S3 is unique. The canonical tensor identification also proves uniqueness of Theta.

For n14 the unrestricted parameter space has dimension `364 dim(E) dim(E')`. It is not the two-dimensional family from the full-derivation theorem. Smooth variable coefficients obey this result pointwise; derivatives of those coefficients are a separate condition for a differential chain identity. Classification of all Spin submodules of this large Hom space is unnecessary for the obstruction or positive example.

## 3. The selected full-curvature witness

Use the held displayed product assignment `comm,symi,symi`, with the printed -1/2. Exact formula custody is [`phi_low` and `shiab`](../../tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py):

```
starF = *F
first = Phi1 wedge_comm starF
middle = *[Phi2 wedge_symi starF]
second = *[Phi1 wedge_symi middle]
S2(F) = first - second/2,
Phi1 = sum_i e^i gamma_i,
Phi2 = sum_{i<j} e^i wedge e^j gamma_i gamma_j.
```

Here coefficient products are `comm(X,Y)=XY-YX` and `symi(X,Y)=i(XY+YX)`, separate from the exterior wedge. The native star uses the ordered volume and the product of metric signs on the input blade.

Choose distinct positive orthonormal axes i<j and set

`k=e^i`, `F=e^i wedge e^j tensor gamma_i`.

Only the (i,j) coefficient of Phi2 can meet *F, and

`{gamma_i gamma_j,gamma_i}=0`.

The entire nested term therefore vanishes. In k wedge first, only the j coefficient of Phi1 survives. Consequently

```
k wedge F = 0,
k wedge S2(F) = -2 vol tensor gamma_i gamma_j != 0.
```

For a general signed pair the coefficient is `-2 eta_i eta_j`; choosing positive axes avoids an irrelevant sign change. In the old K77 table axes0 and4 are positive, whereas axis1 is negative. Each native signature table must retain its own labels. A nonzero common normalization or orientation reversal cannot remove the obstruction.

This contradicts condition2 of the classification, so **no algebraic S3 exists**, even without equivariance. There is no need to construct a candidate or run a map census. Under source primary-minus, vectors are sharp-skew and this is a real full-u(H) input. A plus/reversion comparison must change phases coherently with the Phi realization; it cannot silently hold incompatible inputs fixed. Complexification transports the obstruction only after identifying the actual real map with the stated complex extension.

For the coherent algebraic phase comparison `Phi1'=i Phi1`, `Phi2'=-Phi2` and `F'=iF`, the inner term remains zero and the first term changes sign. The witness is then `+2 vol gamma_i gamma_j`, still nonzero. This checks the simultaneous phase change used when self-adjoint vectors are replaced by skew-adjoint i-gamma vectors; it does not by itself identify two different Clifford-sign or real-form realizations.

## 4. Actual connection jet and the precise repair boundary

In a local trivialization use

`A_j=(x^i)^2 gamma_i/2`, with all other A components zero.

At p=0, A=0 and F_A=0, but `partial_i F_A=e^i wedge e^j gamma_i`. This is an actual connection curvature, with `D_A F_A=0` identically. Only one matrix direction occurs, so coefficient commutators vanish directly in this model. For any smooth held S2(x), derivatives of its coefficients multiply F_A(p)=0. An outgoing covariant exterior derivative therefore has the same nonzero value at p as section3.

Thus the obstruction excludes any **zero-preserving factorization solely through the Bianchi residual** `D_A F_A`, including nonlinear or higher-order operations on that residual: its whole jet is zero. Smooth lower-order corrections depending only on A,F and the same fixed backgrounds do not change the difference from the zero connection at p. For an affine nonzero-baseline identity, subtract its value at the zero connection. A smooth nonlinear curvature map whose derivative in F at F=0 equals this S2 has the same linearized obstruction.

This extension fixes the outgoing principal symbol to ordinary exterior multiplication, or an injective re-identification of its output. It does **not** exclude every first-order outgoing operator: a zero symbol or a projection that erases the witness is an immediate counterexample. Extra same-order rows, separately varying field jets, dependence on connection derivative data beyond the curvature, a restricted carrier, a different total grading, or a spinor-module cancellation change the tested identity. No full Euler tuple is asserted to vanish on this germ, and the source's other terms have not been discarded from an authenticated identity.

## 5. Positive wedge companion with Einstein response

In dimension14 let

```
Phi3 = sum_{a<b<c} e^a wedge e^b wedge e^c gamma_a gamma_b gamma_c,
Theta = *Phi3,
Splus2(F) = Theta wedge F + F wedge Theta,
Splus3(G) = G wedge Theta - Theta wedge G.
```

These are ordinary matrix products combined with exterior wedge. Since Theta has odd degree11, wedge associativity gives

`k wedge Splus2(F) = Splus3(k wedge F)`

for every k,F. In the classification, the coefficient action is `X -> Theta_I X+X Theta_I`. Both maps are Spin-equivariant. They are not asserted to be full associative/Lie graded derivations, and the anticommutator does not in general obey the coefficient Leibniz law.

Indeed, the natural all-degree anticommutator wedge suite sends the unit to `2Theta != 0`, whereas an associative derivation kills the unit. For the graded-Lie law, a derivation must preserve the center, but this same image is not graded-central: some coefficient matrix X has `[Theta,X]!=0`. These are separate failures of the stronger derivation premises, not just the associative unit argument reused for Lie brackets.

### 5.1 Exact Riemann restriction

Use the [owned native injection and Einstein output](../../tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py):

```
(I(R))_ij = sum_{d<e} eta_d eta_e R_ijde gamma_d gamma_e,
G14(R) = *[sum_a e^a tensor sum_r eta_r
             (Ric_ar - scal*g_ar/2) gamma_r].
```

Then, for **every algebraic Riemann tensor**,

`Splus2(I(R)) = +2 G14(R)`.

Multiplying the whole operator by i multiplies this coefficient by i. An injection with an additional factor1/2 instead yields G14. These normalization changes must not be confused with a different Einstein ratio or a physical Einstein-equation claim.

**Proof.** In a complex orthonormal frame the output dual coefficient in row a is

`J_a = sum_{b<c,d<e} R_bcde {gamma_abc,gamma_de}`.

Here gamma_abc and gamma_abcde denote antisymmetrized Clifford blades, zero when an index repeats. The Clifford identity is

```
{gamma_abc,gamma_de} = 2 gamma_abcde
 +2[(g_ae*g_bd-g_ad*g_be) gamma_c
    +(g_ad*g_ce-g_ae*g_cd) gamma_b
    +(g_be*g_cd-g_bd*g_ce) gamma_a].
```

The grade5 term contracts the total alternation of R and vanishes by first Bianchi. Replace the ordered-pair sum by one quarter of the unrestricted sum. The six displayed contraction terms contribute Ric, Ric, Ric, Ric, -scal and -scal respectively before the common factor1/2. Therefore

`J_a=2 sum_r Ric_ar gamma_r-scal gamma_a`.

This proves the formula, including Weyl annihilation. It is an orthogonal tensor identity, so complex orthonormal transport proves it in each nondegenerate real signature with coherent Clifford/Hodge conventions. That tensor transport does not identify the K77 and K95 real adjoints.

A sectional positive-plane check makes the sign visible: `I(R)=e^i wedge e^j gamma_i gamma_j` has zero i,j output rows and coefficient `-2 gamma_a` in the other12 diagonal rows, exactly2G14. This is a calibration, not the complete proof.

### 5.2 Primary-minus reality and differential scope

With native `gamma_i^sharp=-gamma_i`, a grade3 Clifford blade is sharp-self. Thus Theta is coefficientwise sharp-self, and the bare anticommutator sends sharp-skew F to sharp-skew output. The top-degree companion has the same coefficient anticommutator after exterior signs are reordered, so it too preserves this real carrier. Full real u(H) need not be associative for these combined operations to close.

Equivalently use the sharp-skew invariant phase iTheta together with the source-style i-Jordan coefficient product: `i{iTheta,F}=-{Theta,F}`. This realizes -Splus2 on the real carrier. Inserting only the outer i while holding bare Theta fixed instead changes the output adjoint type. The phase distinction is substantive; no source selection or new physical contour is inferred. The [primary-adjoint analysis](source-adjoint-spinless-placement-2026-11-26.md) supplies the relevant minus convention; other adjoints require separately coherent comparison data.

For the Levi-Civita spin connection B, the invariant Theta is parallel and `d_B Theta=0`. Graded Leibniz then gives the full fixed-background identity

`d_B(Splus2(F))=Splus3(d_B F)`.

For a general full-U connection, d_A Theta need not vanish. Terms involving that derivative remain, as do moving epsilon and distinct incoming/outgoing connection requirements. The principal companion does not settle a complete two-connection chain or an action-Euler correspondence.

## 6. Decisions, survivors and verification ceiling

The selected map has Riemann restriction -2G14; the negative of the positive wedge map has that same restriction. Yet their full-connection companions differ decisively. Therefore **principal Riemann Bianchi plus Einstein response does not identify the full-curvature map**, and a full-curvature companion does not imply Riemann silence.

Within the inherited K77 displayed grammar and its coherently identified complexification, among the eight individual fixed Phi1/Phi2 assignments with printed -1/2, the inherited complete selector leaves only comm/symi/symi with both principal Riemann Bianchi and nonzero response. That row fails section3. Hence Splus2 cannot be a nonzero scalar multiple of any of those eight full maps. This does not transfer an unexamined product-slot or real-phase convention to K95, and does not classify their five-dimensional linear span or all other invariant Phi choices; no such census is needed or claimed.

Equivalently, **no nonzero scalar multiple of any of the eight fixed individual maps has both the full companion property and nonzero Riemann response**. Full companion implies the prior Riemann-symbol kernel condition, so the inherited selector and the new witness prove this entire discrete-class statement without rerunning its census. Splus2 is an explicit outside-eight survivor; membership in their linear span remains unadjudicated.

The positive map survives this companion test only. If it is inserted into the already-tested fixed-linear/full-U/full-translation first-action architecture with the exact printed Euler correspondence, the [existing endpoint theorem](printed-shiab-endpoint-audit-2026-11-27.md) still applies and excludes every nonzero map there. Its curvature response and companion therefore do not revive that excluded action architecture or supply a new viable action.

The consequence is to stop searching for S3 for the held selected S2 under this universal exterior square. The wedge/module class survives and needs an actual source connection/transport law before a lower-order completion is meaningful. The strongest positive alternative is explicit and inexpensive; it is not installed as Weinstein's missing selector. The source's optional interpretation, missing selector and differently typed spinor construction remain open. Physical2+1, the nonchiral total theory, observed Einstein dynamics, state/domain choices and class-C/GU-wide verdicts do not change.

The two finite lemmas in [ShiabCompanion.lean](../../Lean/GUFormalization/ShiabCompanion.lean) formalize a zero-preserving factorization obstruction and polarization of a diagonal-zero bilinear map into skewness. They do not formalize exterior tensor classification, the full Clifford algebra, signature/reality transport, holonomic geometry or the Einstein identity. The separately owned exact probe calibrates those concrete conventions and mutations; its finite checks are not a replacement for the written universal proof. This report's author ran no tests or Lean compilation. Execution, hashes and independent T1 acceptance are recorded separately.
