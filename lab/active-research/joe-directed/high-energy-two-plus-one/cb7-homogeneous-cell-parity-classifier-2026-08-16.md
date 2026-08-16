---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_parity_classifier
created: 2026-08-16
work_item: CB-7A
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-7A: no summand-blind half/degree primalizer makes the four displayed d0 plus H210 cells homogeneous"
grade: "EXACT FINITE F2 CLASSIFIER plus general same-cell parity proof for homogeneous source-half primalizers. CONDITIONAL on H210 and on the source-faithful section-11.2 ambient-half labels. Grading-mixing automorphisms and enlarged full-Dirac codomains are different operator grammars and are not enumerated. No action, selector, graph/background, family row, reduction, quotient, external datum, mass, spectrum, or physical adjoint is constructed."
disposition: SUMMAND_BLIND_NO_GO__SAME_HALF_TYPES_D0_ONLY__OPPOSITE_HALF_TYPES_H210_ONLY__PRODUCT_GRADING_DIAGNOSES_NOT_REPAIRS__TWO_ABSTRACT_MINIMAL_ODD_ADAPTER_CLASSES
canon_verdict_change: none
steering_effect: "Carry forward the exact homogeneous-summand-blind no-go. The two odd-adapter classes are parity candidates only; source-module and differential covariance must be adjudicated separately. A changed source-label, grading-mixing, or enlarged-target grammar is a different construction. Do not import the W/mirror trace-q kill without an H210-specific carrier calculation."
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/source-claim-register.yaml
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb6-h210-equation916-observed-composition-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb6-wave-h210-correlated-lift-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb6-h210-correlated-lift-review.md
  - explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md
  - explorations/conditional-build/selected-k77-degree-duality-pair-graph-gate-2026-08-10.md
scripts:
  - tests/channel-swings/joe_directed_cb7_homogeneous_cell_parity_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — source-native conditional build.** This artifact
> concerns Weinstein's equation-(9.16) candidate grammar, section-11.2
> ambient-half labels, equation-(11.6) Z/internal-`144` partner sector,
> equation-(12.22) F/imposter referent, `2+1`, and emergent chirality.
> Ordinary family indices, net-chirality arguments, scalar-Higgs/VEV models,
> conventional `SO(10)` mass mechanisms, and familiar low-energy particle
> models are irrelevant comparators without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md`.
>
> Horn `H210` is assumed. Constructing or deriving an action, selector,
> observer graph/background, family row, moving PS reduction, physical
> quotient, external datum, mass, scale, threshold, spectrum, or observable
> is outside this channel. Bars remain independent fields; stars are not
> promoted to a common-domain adjoint.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-7A — homogeneous-cell half/parity classifier

## Outcome first

The four full equation-(9.16) cells cannot be made homogeneous by any
invertible **summand-blind** row/column primalizer that depends on form degree,
source half, row slot, column slot, or the cell itself.

The reason is local to one cell. After any common row and column retyping, the
derivative and H210 summands inherit the same primalizer factors, but their
ambient-half parities remain opposite:

```text
o(d0)=o(d0*)=0,                 ambient-half preserving,
o(varpi_H210)=o(bar-varpi*)=1,  ambient-half flipping.
```

Thus exactly one summand types in each cell and the other misses. The exact
finite classifiers give:

```text
degree-sensitive r0,r1,c0,c1 conventions:       16 conventions,
source-slot-sensitive invertible conventions:  256 conventions,
for every convention:                            4/8 term incidences type,
                                                   0/4 full cells are homogeneous.
```

The familiar extremes expose the collision directly:

| density-dual convention | derivative incidences | H210 incidences | homogeneous full cells |
|---|---:|---:|---:|
| same-half | `4/4` | `0/4` | `0/4` |
| opposite-half | `0/4` | `4/4` | `0/4` |

This is a conditional no-go for the present source labels and K77 operator
grammar. It is not a rejection of equation (9.16), H210, GU, or a different
Shiab/operator-family member.

## 1. Reverse scaffold and source cells

Start from the superposition hypothesis:

```text
the derivative and H210 zero-order term printed in each relevant equation-
(9.16) cell have one homogeneous typed realization.
```

The source fixes the row and column orders:

```text
rows:    (bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus),
columns: (zeta-plus, zeta-minus, nu-plus, nu-minus).
```

Section 11.2 fixes `zeta+/-` and `nu+/-` as ambient half-spinor labels. The
four cells to satisfy simultaneously are:

| role | cell | displayed entry | source input | same-half derivative target | opposite-half H210 target |
|---|---:|---|---|---|---|
| A forward | `(1,2)` | `d0 + varpi_-+` | `nu+ in Omega0(S+)` | `zeta+ in Omega1(S+)` | `zeta- in Omega1(S-)` |
| B forward | `(0,3)` | `d0 + varpi_+-` | `nu- in Omega0(S-)` | `zeta- in Omega1(S-)` | `zeta+ in Omega1(S+)` |
| A reverse-shaped | `(2,1)` | `-d0* - bar(varpi_+-)*` | `zeta- in Omega1(S-)` | `nu- in Omega0(S-)` | `nu+ in Omega0(S+)` |
| B reverse-shaped | `(3,0)` | `-d0* - bar(varpi_-+)*` | `zeta+ in Omega1(S+)` | `nu+ in Omega0(S+)` | `nu- in Omega0(S-)` |

The reverse-shaped entries are classified by their displayed source typing.
They are not declared formal adjoints. Both ambient halves and both directions
are retained.

## 2. Exact F2 theorem

Write half labels and flips additively in `F2`. For a cell with row slot `i`,
column slot `j`, row half label `h_i`, column half label `h_j`, row-primalizer
flip `r_i`, column-primalizer flip `c_j`, and operator parity `o`, typing asks

```text
h_i + r_i = h_j + c_j + o.                 (T)
```

In each of the four displayed cells `h_i=h_j`. More importantly, even if that
equality were absent, the derivative and H210 terms share the same `i,j` and
therefore the same left side and common primalizer factors. Their two
instances of (T) are

```text
h_i + r_i = h_j + c_j + 0,                 derivative,
h_i + r_i = h_j + c_j + 1.                 H210.
```

Adding the equations gives `0=1`. This proves the same-cell no-go without a
restriction to a particular degree twist. It covers:

- same-half and opposite-half density duals;
- row-only, column-only, and joint row/column primalizers;
- primalizers depending on zero- versus one-form degree;
- invertible half flips depending separately on the source half or field slot;
- arbitrary cell-dependent but summand-blind retypings.

Because the two operator parities exhaust `F2`, every convention types exactly
one of the two terms in every cell. This proves the exact `4/8` and `0/4`
counts, not merely an upper bound.

Noninvertible maps that collapse `S+` and `S-` can hide the contradiction only
by deleting the source half distinction. They are outside the source-faithful
classifier and are retained as an adverse semantic control.

## 3. Degree and product-grading audit

Both forward terms shift `Omega0 -> Omega1`; both reverse-shaped terms shift
`Omega1 -> Omega0`. Form degree alone therefore assigns the same degree parity
to the two summands and is blind to their different target bundles. It cannot
repair the half mismatch.

For the product grading

```text
G = form-degree + ambient-half mod 2,
```

the wording must be more precise. Product grading is **not** blind. On either
direction, the form parity changes once, so

```text
Delta G(d0)    = 1,
Delta G(H210)  = 0.
```

It diagnoses that the two summands have opposite product parity. It does not
make them homogeneous. A grading that ignores ambient half can call both
summands degree-odd, but then it has discarded the identity-grade source
half target and does not type their sum as a map to one `S+` or `S-` bundle.

## 4. Minimal abstract escape classes

A genuine repair must change the **relative** parity of the two summands. Add
operator-class adapter bits `a_d,a_H in F2` before applying a common
primalizer. Homogeneity requires

```text
0 + a_d = 1 + a_H,
```

so `a_d+a_H=1`. The two minimum-Hamming-weight classes are:

| abstract branch | duality placement | relative-parity repair |
|---|---|---|
| `H210-ODD-ADAPTER` | same-half | apply one additional odd adapter to every H210 forward and reverse-shaped term |
| `D0-ODD-ADAPTER` | opposite-half | apply one additional odd adapter to every derivative forward and reverse-shaped term |

One operator-class-wide bit covers all four cells algebraically. This does not
construct the corresponding bundle map, prove its naturality, preserve the
H210 Z/RS/PS port, or establish forward/reverse coherence. Those are separate
gates. In particular, this parity certificate does not decide whether an
H210-side odd adapter still lands in the source-required `144` versus
`144bar` module after same-half primalization. Module coherence can kill an
algebraically surviving parity class and must be adjudicated separately. If
no such map exists, the remaining escape is to change the source
label/operator grammar—for example, enlarge a cell target to both halves or
replace one displayed operator class. That is explicitly a different
construction, not a silent reinterpretation.

## 5. Prior-art and novelty fence

The 2026-08-04 source-sign reconciliation solved a different SAT problem:
three principal classes in distinct cells admit two global-sign-related
degree-sensitive row/column assignments, but their realization requires an
odd `q`-type intertwiner. Those assignments cannot solve the present
same-cell collision because the common row/column factors cancel between the
two summands.

The v0.140 trace-`q`/Pin computation then killed its canonical realization on
the proposed `W + mirror` graph carrier: the upper joined rank was `256`.
That is a carrier-scoped negative result. It is not automatically a no-go for
an H210-specific adapter on the present Z/internal-`144` port. Conversely,
CB-7A does not reopen the retired W/mirror graph campaign.

Twistors remain controls only: the four-dimensional gamma-trace projector and
`Pi_4 != Pi_14` do not change the upstream relative half parity. The downstream
CB-6 `kappa_J` also cannot repair it and must never be inserted into `varpi`.

## 6. Multi-lens audit

1. **F2/SAT completeness:** the 16 degree conventions and all 256 invertible
   source-slot conventions are exhausted; the local proof covers even
   cell-dependent summand-blind flips.
2. **Source fidelity:** equation-(9.16) order and section-11.2 ambient labels
   stay fixed; the displayed candidate is not promoted to a unique operator.
3. **Bundle typing:** an `S+` target and an `S-` target are not addable merely
   because their form degrees agree.
4. **Both halves:** A/B forward and reverse-shaped conjugate cells have the
   same fingerprint; no luminous half is selected.
5. **Reverse coherence:** stars and bars are preserved as source syntax, not
   used to infer a reality map or common-domain adjoint.
6. **Adversarial controls:** silent one-form relabeling, half collapse,
   deletion of reverse cells, bar-as-adjoint promotion, and upstream kappa are
   rejected.
7. **Prior-art novelty:** the result is a same-cell superposition theorem, not
   another W/mirror graph or three-principal-class SAT campaign.
8. **Conditional-build scope:** H210 is assumed and no action, external datum,
   graph, family row, reduction, quotient, mass, or spectrum is sought.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb7_homogeneous_cell_parity_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb7_homogeneous_cell_parity_probe.py --selftest
```

The probe checks source order, all four displayed cells, both halves, both
directions, the 16 and 256 convention families, the general same-cell proof,
same/opposite extremes, degree/product grading, the two minimum abstract
adapter classes, prior-art scope, and semantic mutations.

## Strict claim ceiling

CB-7A proves that no invertible summand-blind half/form-degree primalizer makes
the four displayed derivative-plus-H210 cells homogeneous while retaining the
source's ambient-half labels. It identifies two abstract minimum parity-repair
classes but constructs neither. It does not reject the source candidate,
derive an action or external datum, select an operator, graph, family row,
reduction, quotient, reality condition, domain, mass, scale, spectrum,
observable, or phenomenology. F/imposter, `M_3`, and Z/internal-`144` remain
distinct, the parent carrier remains non-chiral, and both conjugate halves
remain present.
