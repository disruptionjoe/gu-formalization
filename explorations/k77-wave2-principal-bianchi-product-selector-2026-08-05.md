---
title: "K77 Wave 2: principal-Bianchi product selector and curvature comparison square"
date: 2026-08-05
status: complete
verdict: "CONDITIONAL_SELECTOR_RESOLVED_INSIDE_DISPLAYED_EIGHT_ROW_GRAMMAR__CURVATURE_COMPARISON_BUILT__FULL_CHAIN_AND_EULER_FUNCTOR_OPEN"
grade: "EXACT finite-dimensional principal-symbol theorem plus source-graded reconstruction; not source attribution, global chain closure, full Shiab uniqueness, observed gravity, or physics"
fork: SIGNATURE_AMBIENT_7_7
---

# K77 Wave 2 principal-Bianchi product selector

## Plain-English result

We found a condition that actually distinguishes the eight product choices in
Weinstein's written Shiab formula.

At the leading-derivative level, the Bianchi identity says a legitimate metric
curvature jet has a particular closed form. Four of the eight product choices
carry every such curvature jet to another closed object. Three of those four,
however, do so only because they erase the entire Riemann-curvature sector.
Exactly one choice both obeys Bianchi and retains gravity:

```text
first product: commutator
inner nested product: i times anticommutator
outer nested product: i times anticommutator
```

That same row, in a separately assembled curvature calculation, equals `-2` times the fourteen-dimensional
Einstein contraction on the scalar and traceless-Ricci pieces and kills the
Weyl piece. The Einstein calculation corroborates the selector; it is not
counted as an independent surplus constraint because contracted Bianchi and
the Einstein trace ratio are mathematically linked.

This is the strongest selector result in the K77 construction so far. Its
boundary matters: it chooses among the **eight fixed product assignments in
the displayed formula**. It does not prove that no other Shiab formula exists.

## 1. What the source supplied, and what it did not

The Portal transcript says:

- the invariant forms supply a family of degree-changing Shiab operators;
- the rolled cancellation works “if shiab is a derivation”;
- curvature followed by Shiab is meant to be the common obstruction.

The 2021 draft fixes the `Phi1/Phi2` degree-two formula, its relative
coefficient `-1/2`, and the commutator/`i`-anticommutator coefficient products.
It also says a historical highest-weight/Bianchi calculation selected a
preferred operator, while explicitly acknowledging that the calculation
cannot be located.

The source does **not** define the executable derivation/Bianchi criterion or
label the three product nodes. This artifact therefore reconstructs a
necessary principal-symbol condition and grades it as a reconstruction. See
`lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md`.

## 2. Layer 0

The following objects remain separate:

| phrase | object used here | object not claimed |
| --- | --- | --- |
| derivation | principal-symbol kernel transport on the displayed degree-two map | a fully defined degree-11 graded derivation on every form degree |
| Bianchi | differential second-Bianchi symbol on algebraic Riemann curvature | algebraic first Bianchi alone, `Xi=D Upsilon`, Noether/BV, or a global covariant complex |
| curvature | spin injection of the algebraic Riemann module | arbitrary `Omega2(ad)` coefficient data |
| selection | one row among eight fixed coefficient-product assignments | uniqueness among every invariant-tensor Shiab |
| Einstein | ambient fourteen-dimensional Ricci-minus-half-trace map | pulled-back four-dimensional Einstein equations |
| comparison | curvature component of a two-connection/path-average square | the complete fermion-complex-to-bosonic-Euler functor |

Layer 0 passes with these fences. Removing any one of them changes the theorem.

## 3. The complete principal-Bianchi carrier

Fix a nonzero principal covector `k`. A curvature tensor satisfying the
algebraic Riemann symmetries and the differential-Bianchi principal symbol has
the form

\[
 R_{ijab}
 =k_i k_a S_{jb}-k_i k_b S_{ja}
  -k_j k_a S_{ib}+k_j k_b S_{ia}, \tag{1}
\]

for a symmetric tensor `S`, modulo the kernel of this presentation. In an
adapted basis the only independent entries are `R_(0p0q)=S_(pq)`, so the
carrier has dimension

\[
 \dim \operatorname{Sym}^2(\mathbb R^{13})=91. \tag{2}
\]

The exact probe constructs the spin injection of (1) and independently finds
rank 91 for positive, negative and null representatives of the three nonzero
`Spin(7,7)` covector orbits. Every generated jet satisfies

\[
 k\wedge F=0. \tag{3}
\]

Thus the test is complete on the principal Riemann/Bianchi carrier, rather
than a representative-jet heuristic.

## 4. Product-sensitive condition

For each of the eight fixed product assignments `p`, impose

\[
 k\wedge \mathscr S_p(F)=0
 \quad\text{for every }F\text{ in the rank-91 carrier}. \tag{4}
\]

The exact result is:

| product assignment `(first, inner, outer)` | principal Bianchi | Riemann response | disposition |
| --- | --- | --- | --- |
| `comm,comm,comm` | fail | nonzero | reject |
| `comm,comm,symi` | fail | nonzero | reject |
| `comm,symi,comm` | fail | nonzero | reject |
| `comm,symi,symi` | pass | nonzero | **unique displayed survivor** |
| `symi,comm,comm` | pass | zero | reject as vacuous |
| `symi,comm,symi` | pass | zero | reject as vacuous |
| `symi,symi,comm` | pass | zero | reject as vacuous |
| `symi,symi,symi` | fail | scalar-only | reject |

The Bianchi defect has rank one on the predecessor's five-dimensional full
displayed-map span. Therefore Bianchi alone leaves a four-dimensional
continuous kernel; it is not a continuous uniqueness theorem. The unique
statement is discrete and exact:

> Among the eight fixed displayed product assignments, exactly one is both
> principal-Bianchi compatible and nonzero on algebraic Riemann curvature.

## 5. Independent Einstein check

Let `I(R)` be the spin-curvature injection and `G14(R)` the natural degree-13
image of

\[
 \operatorname{Ric}(R)-\frac12\operatorname{scal}(R)g.
\]

For the selected row the exact calculation gives

\[
 \mathscr S_{\rm comm,symi,symi}(I(R))=-2G_{14}(R) \tag{5}
\]

on both the scalar and traceless-Ricci irreducible pieces, and gives zero on a
nonzero Ricci-free Weyl fixture. The algebraic Riemann decomposition
`1 + 104 + 3080` and the earlier target-multiplicity calculation then identify
this as the complete Riemann restriction at the declared representation
grade. No Standard Model, four-dimensional gravity, external datum or
phenomenological target was used to obtain the row.

No positive constraint-surplus number is claimed: Bianchi and the Einstein
ratio are not independent rows in the natural Ricci/scalar map space. The
information gain is instead the exact discrete elimination—one nonvacuous row
survives out of eight with zero fitted coefficients.

## 6. Moving epsilon

The predecessor proved

\[
 \delta\Phi_i=[\Phi_i,\chi]
\]

and exact invertible conjugation transport of the displayed maps. Simultaneous
conjugation commutes with the zero/nonzero kernel condition, so moving
`epsilon` transports the selected row but supplies no additional selector.
This closes the moving-`Phi/epsilon` part of the named product subgate at
principal-symbol grade.

## 7. Two-connection comparison square

The shifted two-connection construction supplies

\[
 \Delta F=D_BT+T^2.
\]

Its curvature projection is

\[
 F_B+\frac12\Delta F-\frac16T^2
 =F_B+\frac12D_BT+\frac13T^2=\bar F. \tag{6}
\]

Equation (6) gives a commuting linear square before Shiab. Postcomposing both
paths with the selected linear Shiab gives the same curvature contribution to
the degree-13 Euler row. This is now a typed comparison square, not merely a
mnemonic.

It is not the full requested functor. The square does not yet include:

- the augmented-torsion Euler terms;
- moving `epsilon` and section/density/Hodge owners in the same diagram;
- matter and the degree-14 redundant row;
- Green/Noether/BV data;
- the unreleased fermion rolled complex as a defined source object.

## 8. Seven-axis disposition

| layer | result |
| --- | --- |
| Layer 0 | passes with the nine distinctions above |
| L1 substrate | unchanged smooth K77 Observerse construction |
| L2 observer | fixed ambient principal-symbol frame; no observation-map physics claim |
| L3 pairing | exact exterior/Hodge/Clifford coefficient products; no new pairing datum |
| L4 causal order | formal principal symbol only; no hyperbolic domain claim |
| L5 emergence | unchanged |
| L6 coordination loop | moving epsilon transports but does not select |
| L7 positivity | untouched; no Hilbert/Krein physical-domain claim |

## 9. Verdict and next gate

```text
DISPLAYED_EIGHT_ROW_PRODUCT_SELECTOR:
  CONDITIONALLY_RESOLVED at complete Riemann principal-symbol grade

SELECTED_ROW:
  comm / symi / symi

FULL_SOURCE_NATURAL_SHIAB_UNIQUENESS:
  OPEN

TWO_CONNECTION_CURVATURE_COMPARISON:
  BUILT

FULL_TWO_CONNECTION_TO_EULER_COMPARISON_FUNCTOR:
  OPEN
```

The next named build is:

```text
K77_EDDY_COMPLETED_AUGMENTED_TORSION_CHAIN_MAP_AND_FULL_EULER_COMPARISON_FUNCTOR
```

It must test the selected row on the full eddy-completed, generally
non-Riemann curvature packet and assemble the missing torsion/epsilon/Euler
owners in one diagram. P1/P2/P3 remain unchanged and unused; Curt stays
formally separate; Wave 3 and all physics rows remain closed.

## Reproducibility

- Main exact probe:
  `tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py`
- Independent Sage reconstruction:
  `tests/channel-swings/k77_wave2_principal_bianchi_product_selector_independent.sage`
