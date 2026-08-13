---
artifact_type: construction_result
created: 2026-08-06
status: TWO_CONNECTION_PRINCIPAL_DESCENT_EXACT__PHYSICAL_LC_KERNEL_PRESERVED__LOWER_ORDER_WARD_BV_PREBOUNDARY_OPEN
source_return: SOURCE-CONFIRMS
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_cubic_two_connection_principal_ward_descent_probe.py
  - tests/channel-swings/selected_cubic_two_connection_principal_ward_descent_independent.sage
registry: lab/process/selected-cubic-two-connection-principal-ward-descent.json
---

# Selected-cubic two-connection principal Ward descent

## Result first

The rank-five obstruction from the preceding swing was real for one connection
in isolation, but it was not typed on GU's full source object. Augmented
torsion uses two connections through

\[
 T=A-B.
 \tag{1}
\]

On the complete `24+24` Levi-Civita carrier, the tangent map

\[
 W(\delta A,\delta B)=\delta A-\delta B
 \tag{2}
\]

has rank 24 and kernel exactly equal to the 24-dimensional diagonal. Therefore
the simultaneous inhomogeneous principal connection-gauge motion
`(D chi,D chi)` is in the radical. The old six-dimensional isolated gauge
block has rank five; the two-connection diagonal gauge block has rank zero.

The cancellation does not erase the physical Levi-Civita response. On the
same exact shells,

\[
 D^3I_T[\Phi_1,L_p(h_0),L_q(h_m)]
 =\frac{14}{3}(p\!\cdot\!q)(h_0\!:\!h_m)
 \tag{3}
\]

survives unchanged. Equation (2) is not a counterterm fit: diagonal
annihilation plus endpoint normalization uniquely fixes `(1,-1)`, exactly the
source-owned connection difference.

The disposition is
`PRINCIPAL_DESCENT_EXACT__LOWER_ORDER_WARD_BV_PREBOUNDARY_OPEN`. At nonzero
background `T`, the lower-order homogeneous orbit `[T,chi]`, moving primitive
owners, nonlinear Ward/BV identity and preboundary class remain unbuilt. No Q1
pole, transition, fifth quotient, physical particle or cosmological claim is
made.

## Plain English

We had found a gauge problem in the new gravity interaction. The problem came
from checking how one connection moved. Eric's construction actually uses the
difference between two connections. Gauge transformations move both
connections together, so their shared motion cancels in the difference while
the physical relative motion remains.

That is genuine progress: the first and cheapest gauge obstruction is gone
without adding a knob. It is not the end of the gauge problem. Once the
background connection difference is nonzero, gauge transformations also
rotate that difference, and the Shiab, pairing, observation map and boundary
terms move too. Those pieces now form the next exact construction gate.

## 1. Layer 0

| phrase | object computed here | not identified with |
| --- | --- | --- |
| augmented torsion | source-owned difference of two connections `A-B` | either connection alone |
| principal gauge motion | shared affine derivative `(D chi,D chi)` | lower-order homogeneous orbit `[T,chi]` |
| principal descent | radical test after the tangent difference map | full nonlinear Ward/BV or BFV reduction |
| physical LC response | anti-diagonal/relative connection response | gauge-diagonal carrier |
| normalized difference | unique `(1,-1)` in the stated two-coefficient family | fitted cancellation term |

The v0.21 rank-five result and the present rank-zero result concern different
objects. Both computations remain valid in their stated scopes.

## 2. Source locus and disposition

The source material types augmented torsion as a difference of two connections
and places the gauge-rotated Levi-Civita connection in the contorsion slot. The
existing reconstruction already writes `T=A-B`. The scoped source return is
therefore `SOURCE-CONFIRMS` for the bi-connection owner and difference form.

The source does not publish the exact rank calculation, equation (3), a
lower-order compensator, a nonlinear Ward identity or a BFV/preboundary
quotient. Those are construction results or open burdens, not quotations.

## 3. Divergent preassessment

| lens | demand | disposition |
| --- | --- | --- |
| differential geometry | vary the source-owned pair of connections, not one representative | enforced by (1)-(2) |
| affine gauge geometry | separate the inhomogeneous diagonal derivative from the homogeneous adjoint orbit | principal part closed; lower order open |
| representation theory | test the complete `24+24` carrier and kernel equality | rank 24, kernel diagonal 24 |
| variational PDE | preserve the physical shell kernel while quotienting gauge motion | equation (3) survives |
| exact computation | reproduce by independent rational and Sage routes | passed |
| symplectic/BV | forbid promotion from principal radical to reduced phase space | enforced |
| source criticism | confirm only the owner and difference, not the derived coefficient | enforced |
| constraint accounting | price any compensator or fit | zero new fields, coefficients, selectors or datum |
| epistemic breadth | test whether the prior fence defended a mistyped object | yes; scope corrected, provenance preserved |
| program management | move only rows whose distance changed | five distance-only migrations |

Preregistered endpoints were: diagonal survives; diagonal cancels but physical
carrier also dies; diagonal cancels and physical carrier survives; or source
typing is ambiguous. The third endpoint occurred.

## 4. Exact difference-map theorem

On `C direct-sum C`, with `dim C=24`, the matrix of `W` is `[I -I]`. Hence

```text
rank W = 24
dim ker W = 24
ker W = {(x,x): x in C}
rank W on {(x,-x)} = 24.
```

For `W_(alpha,beta)(a,b)=alpha a+beta b`, diagonal annihilation gives
`alpha+beta=0`. Normalization at the first connection gives `alpha=1` and
therefore uniquely `beta=-1`. Two conditions fix two coefficients, leaving
zero fitted freedom.

## 5. Exact shell and gauge results

For rational mass pairs `(3,1)`, `(5,3)`, `(7,1)` and `(11,5)`, the physical
plus-plus and cross-cross kernels reproduce (3); plus-cross remains zero. The
one-connection gauge block reproduces rank five at every pair. Pulling both
gauge entries through `(D chi,D chi)` and then through `W` makes the entire
`6 x 6` block zero, with gauge directions in the two-sided radical.

The samples check one symbolic identity and do not manufacture independent
phenomenological constraints.

## 6. Symplectic and Ward boundary

The source-owned difference now has the correct principal presymplectic
radical: diagonal affine gauge directions are killed. That is necessary, not
sufficient, for a reduced covariant Hamiltonian class. At nonzero
`T=t Phi1`, the homogeneous orbit `[T,chi]` is generally nonzero. The moving
Shiab, Hodge/DeWitt/Krein primalization, observation map, direct action owners
and preboundary current must join it in one Ward/BV identity.

Accordingly the existing connection-gauge quotient is corrected, not counted
again. A fifth quotient would require the complete reduced class.

## 7. Seven-axis audit

| axis | result |
| --- | --- |
| Layer 0 | one connection, connection difference, principal motion and full quotient separated |
| L1 typing | `W:C direct-sum C -> C` is the tangent of the source-owned difference |
| L2 covariance | diagonal affine connection motion cancels; homogeneous adjoint covariance open |
| L3 carrier | complete rank/kernel theorem on `24+24`; gauge block `6 x 6` |
| L4 variation | exact selected-action pullback preserves the LC mixed TT kernel |
| L5 quotient | principal diagonal descent exact; nonlinear BV/preboundary reduction open |
| L6 domain | finite exact shell only; common Green/operator domain open |
| L7 physics | no pole, transition, particle, positivity or cosmological prediction claimed |

## 8. Constraint-surplus and datum accounting

```text
new fields: 0
new coefficients: 0
new selectors: 0
P1/P2/P3 consumed: 0
new real-form identifications: 0
```

## 9. Ledger movement and next gate

`LT-GR1`, `LT-GR2b`, `LT-GR5`, `LT-GR6` and `LT-SM8` receive
distance-only migrations. Verdicts, reason kinds, residue and quotient count
do not move. `LT-GR3` remains open.

Next assemble the lower-order homogeneous adjoint orbit, moving
Shiab/Hodge/DeWitt/Krein pairing/observation Ward terms, direct
curvature/full-`II`/defect `D3`, and preboundary current. Only the complete
reduced class may advance to Q1.
