---
artifact_type: construction_result
created: 2026-08-08
status: TEN_METRIC_EQUATIONS_RETAINED__FULL_CONORMAL_BV_ERASURE_REJECTED__SELECTED_K77_EULER_COMPLEX_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS__METRIC_SECTION_RANK10_AND_DIFFEO_ORTHOGONAL_EINSTEIN_TARGET__SOURCE-SILENT__COMPLETE_RECEIVER_AND_SELECTED_K77_BV_COMPLEX
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_metric_section_bianchi_typing_probe.py
  - tests/channel-swings/selected_k77_metric_section_bianchi_typing_independent.sage
registry: lab/process/selected-k77-metric-section-bianchi-typing.json
---

# Selected K77 metric-section and Bianchi/BV typing gate

## Result first

The v0.79 two-horn fork was too coarse.  A BV construction is not an
alternative to retaining the ten metric-section equations.  It is the
rank-four gauge/identity complex **inside** that retained ten-dimensional
sector.

For a local metric section with first jet `J`, the complete field variation is

\[
  \begin{pmatrix}\delta x\\ \delta y\end{pmatrix}
  =
  \underbrace{\begin{pmatrix}I_4&0\\J&I_{10}\end{pmatrix}}_{F}
  \begin{pmatrix}\delta x\\ \delta g\end{pmatrix}.
\]

Ordinary pullback tests only the first four columns.  Its graph-conormal basis

\[
  N=\begin{pmatrix}-J^T\\I_{10}\end{pmatrix}
\]

is killed by ordinary pullback, but the complete equation dual gives

\[
  F^T N=\begin{pmatrix}0\\I_{10}\end{pmatrix}.
\]

Thus the ten equations v0.79 called “conormal” are exactly the ten independent
metric-section Euler coordinates in complete field variables.  Erasing all of
them would erase the gravitational equation carrier the construction is meant
to recover.

The standard linearized Einstein comparator makes the correct BV burden
exact.  For timelike and spacelike noncharacteristic covectors the symbol
complex

\[
  0\longrightarrow V
  \xrightarrow{D_k}\operatorname{Sym}^2 V^*
  \xrightarrow{G_k}\operatorname{Sym}^2 V^*
  \xrightarrow{W_k}V^*\longrightarrow0
\]

has ranks `4,6,4`, satisfies `G_k D_k=0=W_k G_k`, and is exact.  On a null
covector the ranks are `4,4,4`; both middle cohomologies have dimension two.
Explicit plus/cross representatives survive modulo gauge, and their transverse
rotation has characteristic polynomial `lambda^2+4`, so this is a genuine
helicity-`+/-2` comparator rather than a dimension-only reading.

What remains open is load-bearing: construct the selected K77 action's actual
ten-by-ten vertical Euler principal symbol, its rank-four diffeomorphism
differential and four Ward identities, then compare its noncharacteristic
exactness and null cohomology with this Einstein complex.  No identification is
claimed merely because the carriers have the same dimension.

## 1. Layer 0: variations, gauge and identities

| phrase | exact object | disposition |
| --- | --- | --- |
| base motion | `delta x` and induced `J delta x` along the graph | rank four; not an independent metric variation |
| metric-section variation | independent `delta g in Sym^2 T*X` | rank ten and retained by the complete receiver |
| field gauge orbit | principal Lie-derivative image `D_k xi` | rank four for nonzero `k` |
| metric equation | symmetric Euler covector in the dual rank-ten carrier | must not be equated with gauge orbit |
| Bianchi/Ward identity | contraction `W_k E=0` on equation covectors | four identities, not ten vanished equations |
| physical null cohomology | `ker G_k / im D_k` and `ker W_k / im G_k` | dimension two for the comparator |
| selected K77 Euler complex | action-derived vertical operator plus its Ward maps | not yet constructed |

The graph-conormal kernel is therefore a kernel of the **wrong observation
map**, not a proof that its vectors are gauge.  The complete receiver exposes
their correct field-theoretic type.

## 2. Exact complete-receiver retyping

The rational fixture has

```text
rank(base motion)             = 4
rank(metric-section motion)   = 10
rank(F), det(F)               = 14, 1
ordinary pullback times N     = 0
complete equation dual F^T N = [0; I_10]
```

This also retypes the v0.79 augmented-torsion action witness.  It is not merely
a hidden ambient equation: under the complete coordinates it is a nonzero
metric-section Euler covector.  Whether its final selected-action combination
has Einstein/Bianchi form is the next calculation.

## 3. Exact metric comparator

With `h_{mu nu}` symmetric and covector `k`, the comparator uses the standard
principal symbols

\[
  (D_k\xi)_{\mu\nu}=k_\mu\xi_\nu+k_\nu\xi_\mu,
  \qquad
  (W_kE)_\nu=k^\mu E_{\mu\nu},
\]

and the linearized Einstein tensor `G_k`.  Exact rational arithmetic gives:

| `k` | `rank D_k` | `rank G_k` | `rank W_k` | field cohomology | equation cohomology |
| --- | ---: | ---: | ---: | ---: | ---: |
| timelike | 4 | 6 | 4 | 0 | 0 |
| spacelike | 4 | 6 | 4 | 0 | 0 |
| null | 4 | 4 | 4 | 2 | 2 |

The plus/cross null representatives are independently checked against the
gauge image.  Their rotation matrix

\[
  \begin{pmatrix}0&-2\\2&0\end{pmatrix}
\]

has eigenvalues `+/-2i`.  This supplies the representation check that a bare
dimension count would not.

## 4. Symplectic/BV consequence

A legitimate local BV differential may own the rank-four diffeomorphism image,
and its adjoint Ward map may own four identities.  It cannot call the entire
rank-ten metric Euler carrier gauge while retaining an Einstein sector.

The prior contact calculation remains active: compact-support/Dirichlet gauge
is presymplectically horizontal, while unrestricted boundary transformations
carry a live moment map.  Therefore even the rank-four gauge complex needs a
boundary-domain or edge-mode decision before global BFV reduction.

No sixth quotient is booked.  The earlier “source-derived conormal BV quotient”
horn survives only in this narrowed sense: construct the action-derived
diffeomorphism/identity subcomplex inside the retained metric equations.

## 5. Seven-axis disposition

- **Layer 0:** base motion, section variation, field gauge, equation identity,
  and physical cohomology are distinct.
- **L1 source:** source confirms the metric-section/rank-ten and
  diffeomorphism-orthogonal Einstein target, but not the repository receiver or
  selected BV complex.
- **L2 algebra:** the complete dual retypes the conormal ten as pure metric
  Euler coordinates; the Einstein comparator ranks are exact.
- **L3 geometry:** `Sym^2 T*X` is the vertical tangent to the metric section,
  conditional on the admitted Lorentz sector from v0.79.
- **L4 variation:** full-conormal erasure is incompatible with retaining metric
  stationarity; the selected K77 vertical Euler symbol remains open.
- **L5 gauge/BV:** the comparator has a rank-four gauge/identity complex and
  two null helicity classes; the K77 realization is unbuilt.
- **L6 analytic:** global BFV, boundary domain, Green/Krein domain and
  constraint propagation remain open.
- **L7 physical:** the comparator recovers the correct GR symbol architecture,
  not yet the selected GU field equation.

## 6. Exact controls and progress

The composed SymPy route passes `58/58`.  An independent Sage/QQ route passes
`15/15`.  Plants reject ordinary pullback as a metric stationarity test,
complete-receiver erasure of the conormal ten, full-conormal gauge promotion,
and helicity inferred from dimension alone.

```text
new fitted coefficient/selector: 0
new external datum:              0
new scoped quotient:             0
P1/P2/P3 consumed:               0

Ledger v0.80 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: NONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed are the ten-direction physical carrier type, the full-conormal-erasure
rival, and the exact Einstein/Bianchi comparator including null helicity.
Opened is the selected-action vertical Euler/Ward comparison.  The remaining
conditions are that comparison and its global boundary/domain descent.

No verdict, residue, quotient, datum, canon or public posture moves.

## Next gate

`SELECTED_K77_VERTICAL_EULER_DIFFEO_WARD_COMPLEX_AND_EINSTEIN_COHOMOLOGY_COMPARISON`.

Differentiate the selected action with respect to the ten metric-section
variables, including moving Levi-Civita, Shiab/Hodge/frame, observation jets
and augmented torsion.  Construct the actual diffeomorphism generator and Ward
adjoint on that operator.  Only if its noncharacteristic complex is exact and
its null cohomology carries the required helicity classes should the result
advance to boundary BFV and a common Green/Krein domain.
