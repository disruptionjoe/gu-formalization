---
artifact_type: exploration
label: "Resolver Wave C rebased: Q5 + Q6 + M-H7"
created: 2026-08-03
status: exploration
posture: adversarial; Layer-0-first; exact representation theory and topology; pre-deposit
title: "A conditional dualized 126 factor exists; its physical pairing, native carrier, and dim-13 class do not yet"
grade: "EXACT compact-complex representation/channel and coefficient-group results; GU-native carrier, link realization, action, VEV, mass, and integer datum remain reconstruction/open"
canon_verdict_change: none
route_disposition: REBASE
hostile_review_status: PASS_AFTER_REPAIRS
depends_on:
  - lab/specifications/six-axis/six-axis-template.md
  - explorations/cycle-gates-and-audits/resolver-wave-b-disposition-2026-08-03.md
  - explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md
  - explorations/signature-independent-scalar-vanishing-lemma-2026-08-03.md
  - canon/boundary-einvariant-and-the-tangential-fork.md
  - explorations/W192-explicit-carrier-kernel-spectral-gate-2026-07-14.md
  - explorations/W194-w192-reciprocal-packet-intake-gate-2026-07-14.md
scripts:
  - tests/generation-sector/q5_spin10_vector_spinor_product.py
  - tests/generation-sector/q5_spin10_vector_spinor_product_sage.py
  - tests/generation-sector/q6_lambda5_spin10_pati_salam.py
  - tests/located-not-forced/mh7_dim13_restatement.py
---

# Resolver Wave C rebased

## Outcome first

Wave C finds a conditional shared internal representation factor, but it is
several typing arrows earlier than the council summary implied.

1. The bare same-label product `16+ tensor 144+` contains **no 126**. If one
   chooses a complex-linear internal operator `16+ -> 144+`, its correctly
   dualized Spin(10) factor
   `Hom(16+,144+) = (16+)* tensor 144+ = 16- tensor 144+` contains one `126+`.
   That same type occurs in `16+ tensor 16+`. The physical pairing could instead
   be Krein/C-real and is unbuilt, as are its Spin(4), full-20, one-form, and
   `ad(P)` factors. This is a conditional shared internal type, not an activated
   mediator.
2. The base-degree-zero term of `Lambda^5(V4 plus V10)` is the internal 252,
   which complexifies as `126+ plus 126-`. Under Pati--Salam, the right-neutrino
   bilinear lies in `(10bar,1,3)` and contracts with a dual `(10,1,3)` field.
   The complex bilinear channel passes; the native ad-valued-one-form carrier,
   complete Krein/C-reality placement, VEV, and induced 4D mass do not.
3. The abstract framed coefficient group in degree 13 is exactly
   `Omega^fr_13 = pi^S_13 = Z/3`, with `Im J_13=0` and `Omega^Spin_13=0`.
   But GU has not built a closed globally stably framed end link or a nonzero
   Pontryagin--Thom class. Worse for the easy story, the external-product class
   with its product stable framing is zero under the stated closed/framed-X
   assumptions. Any nonzero class needs global twisting, clutching,
   transgression, or a non-product framing.

The route disposition is **REBASE**, not stop. A raw real `Lambda^5` Clifford
element is K-self-adjoint while an `Sp` connection generator must be
K-anti-self-adjoint, so the shortcut `Lambda^5 subset ad(P)` is obstructed.
The next source-action gate must first derive the physical pairing object and
then classify admissible phased/reality-completed or contracted effective
placements of schematic type

```text
Omega^1(Y, ad P)  --->  Lambda^5 V10
```

with right-H, Krein, C/reality, observer, and source-Euler checks. The dim-13
external-datum route proceeds independently only after the actual end link,
stable framing, and Pontryagin--Thom class are constructed. P1/P2/P3 remain
unchanged and unused.

## 0. Layer-0 object table

| shared word | exact objects | ruling |
|---|---|---|
| `16 tensor 144` | bare same-label tensor `F+ tensor T+`; crossed tensor `F- tensor T+`; complex-linear internal operator factor `Hom(F+,T+)=F+* tensor T+`; unbuilt Krein/C-real bilinear | the Hom answer is conditional on complex-linearity and omits Spin(4), full-20, one-form, and `ad(P)` typing |
| `126 channel` | a bilinear representation type `126+`; the dual field type `126-`; the two complex Hodge eigenspaces of one real 252 | occurrence is not selection, coefficient, field, VEV, or mass |
| `scalar` | base exterior degree zero; trivial representation of connected `Spin(1,3)`; parity-even `O(1,3)` scalar | the internal 252 is degree zero; the base-top-form 10 is also a connected-Lorentz singlet but a pseudoscalar |
| `seesaw` | Weinstein's prospective rolled-operator matrix shape; a right-neutrino Majorana block; the complete light-heavy mass mechanism | source shape is not the Lambda5/126 carrier and neither is a complete mass matrix |
| `13` | `1664/128` RS multiplicity; dimension of the proposed Y14 end link; stable-stem degree 13 | numerical equality supplies no map among the three |
| `link` | global `S^6`-bundle over `P(TX)`; fixed-x `S^6`-bundle over the RP3 spine; noncanonical `RP3 x S6` model | the product is not the global link and cannot carry the desired product class |
| external `P3` | integer-valued realized chiral-index/count datum | no torsion group or representation multiplicity here constructs it |

No new seven-axis candidate is admitted. This wave stays inside the current
smooth/Krein construction and resolves only the typed local gates above.

## 1. Specialist pre-assessment and preregistration

Three disjoint read-only specialists were used before construction:

- a D5 representation theorist required all four chiral products and the
  dualized-Hom correction;
- a Pati--Salam/Krein mass specialist required bidegree tags, bilinear/field
  duality, real-form Hodge typing, and the full five-stage physical burden;
- a stable-homotopy/end-topology specialist required the true bundle link,
  the three-13 fence, and a product-model vanishing control.

The preregistered terminal rules were:

- no 126 in either dualized Hom kills the shared compact channel;
- a 126 only in the Hom, but not the bare product, rebases rather than falsifies
  the mediator idea;
- absence of `(10,1,3)` support kills the right-neutrino field channel;
- support without `Omega^1(Y,ad P)` placement returns `REBASE-CARRIER`;
- a literal-product or unframed link cannot be read in `pi^S_13`;
- order-three torsion may not be called integer generation count three.

## 2. Q5: the exact four-product dictionary

Use Bourbaki D5 labels

```text
F+=[0,0,0,0,1],  F-=[0,0,0,1,0],
T+=[1,0,0,0,1],  T-=[1,0,0,1,0].
```

The exact decompositions are

```text
F+ x T+ = 45 + 54 + 210 + 945 + 1050+,
F- x T- = 45 + 54 + 210 + 945 + 1050-,
F+ x T- = 10 + 120 + 126- + 320 + 1728,
F- x T+ = 10 + 120 + 126+ + 320 + 1728.
```

Every multiplicity is one and both dimension rows close at

```text
45+54+210+945+1050 = 2304 = 16*144,
10+120+126+320+1728 = 2304.
```

The analytic certificate derives these from
`T+=10 tensor F+ - F-`, `T-=10 tensor F- - F+` and lower representation-ring
identities. The separate Sage 10.9 certificate computes the actual D5 Weyl
characters.

The Layer-0 correction resolves the complex-linear internal fork:

```text
Hom(F+,T+) = F+* tensor T+ = F- tensor T+,
```

so `126+` occurs once in this conditional operator-factor space and once in
`F+ tensor F+`. A field contracting that complex bilinear has dual type
`126-`; silently calling both simply "the 126" loses a necessary arrow. This
does not establish that the physical Krein/C-real pairing uses this Hom. The
existing B5 first-order
`F+ <-> T+` symbol is the `10` channel, not a selected 126. Q5 therefore
establishes a candidate higher/lower-order channel only.

**Q5 disposition:**
`CONDITIONAL_COMPLEX_LINEAR_HOM_126_AVAILABLE_PHYSICAL_PAIRING_OPEN`.

## 3. Q6: Lambda5, Pati--Salam, and the five-stage burden

The bidegree-tagged exterior split is

```text
Lambda^5(V4+V10)
 = sum_(a=0)^4 Lambda^a(V4) tensor Lambda^(5-a)(V10)
```

with dimensions

```text
252 + 840 + 720 + 180 + 10 = 2002 = C(14,5).
```

The `a=0` term is the internal 252. Under complex Spin(10),

```text
Lambda^5(V10)_C = 126+ + 126-.
```

The `a=4` term is another trivial representation under connected Spin(4), so
"the only Lorentz singlet is 252" is false without the essential
base-degree/parity qualifier. It is a top-form pseudoscalar 10.

Starting from

```text
16+ = (4,2,1) + (4bar,1,2),
Sym^2(16+) = 10 + 126+,
```

the certificate derives

```text
126+ = (6,1,1) + (10,3,1) + (10bar,1,3) + (15,2,2),
126- = (6,1,1) + (10bar,3,1) + (10,1,3) + (15,2,2).
```

Thus the symmetric `nu^c nu^c` bilinear lies in `(10bar,1,3)` and a dual
`(10,1,3)` field can contract it with singlet multiplicity one. The Sage
dictionary independently checks `Sym^2(16+)=10+126+`,
`Lambda^2(16+)=120`, `Lambda^5(10)=126++126-`, and
`Lambda^2(S14+)=V14+Lambda^5(V14)`.

Two native refinements survive the computation:

- On real internal signature `(6,4)`, `star^2=(-1)^(25+4)=-1` on 5-forms.
  The real object is one 252-dimensional carrier with complex structure; the
  126 halves are exchanged by conjugation, not two independent real fields.
- A real degree-five Clifford word is raw K-self-adjoint by reversal parity,
  while an `Sp` connection generator is K-anti-self-adjoint (the W192/W194
  carrier gate). Thus raw `Lambda^5 subset ad(P)` is obstructed. The individual
  complex 126 half is not by itself a real K-self-adjoint field because
  conjugation exchanges the halves. A phase/reality completion, or a covector
  contraction whose actual `ad(P)` generator has even grade four or six, is
  still open. `K c(Phi5)` preserving 14D chirality is only a raw bilinear-parity
  observation, not native connection placement.

The five stages now stand:

| stage | status |
|---|---|
| complex bilinear/PS representation support | PASS |
| GU-native Krein/full-carrier pairing | OPEN: raw odd-grade shortcut has wrong connection adjoint class |
| real/C-reality completion | PARTIAL: real 252 and conjugate halves only |
| nonzero source-owned VEV | OPEN |
| induced 4D mass/seesaw operator | OPEN |

The central missing type is prior to the VEV. GU's boson is an ad-valued
one-form. `Lambda^5 V10` sitting in `End(S)` neither constructs the extra
one-form leg nor lands in the correct K-anti adjoint class. If `Phi5` is simply
posited instead, it is a new field/spurion and must be counted in the
constraint-surplus audit. Wave D must classify admissible phase/reality
completions and covector-plus-even-generator contractions rather than use the
raw inclusion shortcut.

**Q6 disposition:**
`COMPLEX_CHANNEL_PASS_RAW_LAMBDA5_CONNECTION_SHORTCUT_OBSTRUCTED`.

## 4. M-H7: what dimension 13 really supplies

The coefficient facts are exact:

```text
Omega^fr_13 = pi^S_13 = Z/3,
Im J_13 = 0,
Omega^Spin_13 = 0.
```

The stable-stem value is independently recorded in the published
Isaksen--Wang--Xu table; the J statement follows from Bott periodicity
`pi_13(SO)=pi_5(SO)=0`; the Spin value is the existing ABP coefficient result.
Consequently the framed-to-Spin forgetful map is zero, and every additive map
between a finite 2-primary obstruction group and the framed Z/3 is zero. This
is the honest meaning of the firewall sentence at coefficient-group grade.
It does not constrain nonlinear, mixed, equivariant, or source-action-defined
bridges.

The geometry is only partly built. After choosing an auxiliary Riemannian
reduction/Mostow-tubular model, the panel proposes at fixed x a normal bundle
`nu_x = R plus Sym^2 Q*` over the metric-fibre RP3 spine. Before its sphere
bundle may be called noncanonically `RP3 x S6`, one must prove the stated
normal-bundle identification, `w1=w2=w3=0`, and the relevant rank-at-least-four
classification. The inherited global candidate radial-boundary model is

```text
S6 ---> L13=S(nu) ---> P(TX),
```

where `dim P(TX)=7`. It is not yet a GU end link. Compactness additionally
requires compact X or a controlled compactification of its ends; global
transition data, stable framing, and the actual end compactification are
unproved. The product model cannot be promoted: if X is closed and stably
framed and the total framing is the external-product stable framing,

```text
[X4 x RP3 x S6] = 0 in Omega^fr_13
```

because `pi^S_4=0`; independently the selected 3-primary component of the
framed RP3 class times the 2-primary S6 class is zero. A nonzero degree-13 class
would therefore have to be generated by global twisting, clutching,
transgression, or a non-product framing, not inherited from that
external-product framing.

The degree-13 class `alpha1 beta1` has Adams--Novikov filtration three, so its
ordinary e-invariant is zero; `Im J_13=0` is compatible shorthand, not the full
detector argument. The ordinary f-invariant is also not a direct detector of
this odd-stem, filtration-three class. The construction burden is now four
explicit gates:

1. a closed compact end link;
2. a global stable framing;
3. a nonzero Pontryagin--Thom class in `pi^S_13`;
4. a typed, necessarily non-additive dictionary to integer-valued P3.

This candidate does not supersede the existing `pi^S_3` spine/J route. No
family pushforward, suspension, or other map relating the degree-three and
degree-thirteen routes has been built.

**M-H7 disposition:**
`ABSTRACT_DEGREE13_FRAMED_COEFFICIENT_GROUP_EXACT_RECEIVING_OBJECT_OPEN`.

## 5. Primary-source collision

The Weinstein sources do not supply a hidden 126 solution.

| source passage | disposition | effect |
|---|---|---|
| TOE transcript `02:42:28-02:43:30` | `SOURCE-CONFIRMS` a prospective rolled-complex/seesaw shape | it does not provide a completed mass mechanism |
| TOE transcript `02:52:38-02:54:14` | `SOURCE-CONFIRMS` separately named 16 and 144 sectors and explicitly leaves their mass unknown | Q5 tests a reconstruction-motivated relation; the source does not assert `Hom(16,144)` or a 126 |
| `papers/drafts/Transcript into the impossible.md` `00:35:30-00:36:13` | `SOURCE-CONFIRMS` a zero in a self-adjoint rolled operator linked to separated neutrino eigenvalues | it still does not identify Lambda5, a 126 field, or a VEV |
| the named passages/source pack above | `SOURCE-SILENT` on the exact Lambda5/126 connection carrier | the branching dictionary is reconstruction, not author attribution |

This makes the result source-compatible and properly weaker than a physical
mass claim.

## 6. Exact evidence and controls

The direct Wave C packet currently passes **119 exact/boundary assertions plus
7 planted failures = 126**:

- Q5 analytic representation ring: 45 exact/boundary + 1 planted;
- Q5/Q6 Sage Weyl characters: 27 exact + 1 planted;
- Q6 Lambda5/Pati--Salam/Krein typing: 27 exact/boundary + 3 planted;
- M-H7 dimension-13 accounting: 20 exact/boundary + 2 planted.

The planted failures reject same-label 126 occurrence, a chirality-mismatched
Sage identity, the 252-only Lorentz-singlet claim, a nondual `10bar x 10bar`
contraction, occurrence-to-mass promotion, identification of the two
thirteens, and a product-model generator.

## 7. Construction consequence

The next highest-information swing is
`RESOLVER-WAVE-D-NATIVE-126-CONNECTION-PLACEMENT`:

1. derive whether the physical pairing is complex-linear Hom,
   sesquilinear/Krein, or C-real, including Spin(4) and full-20 provenance;
2. construct every natural candidate from the actual connection carrier, for
   example a typed contraction of the one-form leg with Clifford degree four
   or six into an effective internal degree-five kernel, and classify
   phase/reality completions; explicitly reject raw `Lambda^5 subset ad(P)`;
3. classify the candidate space and compute constraint surplus before choosing;
4. test full-20 provenance, observer descent, right-H, Krein adjoint, C/reality,
   and whether the map is source-owned rather than an inserted Phi5;
5. only after that, vary the source action for a stable SM-neutral
   `(10,1,3)` value and compute the induced 4D block.

An external-datum opportunity remains conditional: the 126 contains left and
right triplet sectors, so one may test whether the existing P1 orientation
holonomy really acts as their exchange and selects the right component. Equal
Z/2 type is not evidence; the base map and equality of holonomy/w1 must be
constructed. This candidate does not spend P1 now.

In parallel, M-H7's successor is the candidate global radial-boundary,
normal-bundle, framing, and clutching computation, not another coefficient-table
pass. It must beat the external-product-framing zero control before a boundary
datum is discussed.

## 8. Boundaries

- No native Lambda5 bosonic connection component is constructed.
- No nonzero Yukawa/Majorana coefficient, VEV, scale, mass hierarchy, or seesaw
  matrix is derived.
- No physical quotient, BV complex, domain, or observer pushdown is built.
- No nonzero framed class on the actual Y14 end is exhibited.
- No order-three torsion is converted into integer P3 or a generation count.
- P1/P2/P3 remain unchanged and unused.
- No claim, canon, bar, H59, public posture, count, lane, Eric/Curt separation,
  or third-lane status moves.
