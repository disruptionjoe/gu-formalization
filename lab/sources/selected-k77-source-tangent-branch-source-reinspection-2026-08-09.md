---
artifact_type: source_reinspection
created: 2026-08-09
status: SOURCE_CONFIRMS_SOURCE_COORDINATES_AND_XI_REDUNDANCY__SILENT_BRANCH_STATIONARITY_AND_COMPLETENESS
source_return: SOURCE-CONFIRMS
---

# Source reinspection: source coordinates versus reconstruction coordinates

## Return

The primary source fixes the first-action field locus strongly enough to decide
which derivatives count as its Euler equations:

```text
I_1^B : G x MET(X) -> R,
T_omega = varpi - epsilon^-1 d_0 epsilon,
delta_varpi I_1^B = <alpha,Upsilon_omega>,
Xi_omega = D_omega Upsilon_omega.
```

Thus the source variables are `(g,varpi,epsilon)`.  `B` is derived from
`epsilon`, and a primitive epsilon variation moves `B` and `T` oppositely.
The source explicitly calls `Xi` redundant when `Upsilon=0`.  It does not
license an arbitrary independent `B` variation while holding `T` fixed.

## Layer 0

| object | source status | consequence |
| --- | --- | --- |
| `delta_varpi` | explicit | tests the `T`/translation Euler residual |
| primitive `delta_epsilon` | explicit field coordinate; detailed selected-action completion repo-derived | combines opposite `B/T` motion and moving Shiab |
| metric variation | explicit through `MET(X)` | must move the gimmel/Hodge/Phi packet and the derived connection |
| independent `delta B` at fixed `T` | not a source coordinate | diagnostic reconstruction equation only |
| `Xi=D Upsilon` | explicit and redundant on `Upsilon=0` | no independent amplitude equation |

The inspected source does not mention the two `QQ(sqrt(3))` branches, prove
their source-tangent stationarity, select their amplitude, choose the selected
Spin-native action parent over two `U(32,32)` halves or full `U(64,64)`, or
declare a complete tangent/Hessian/BV domain.

Source return:
`SOURCE_CONFIRMS_G_VARPI_EPSILON_TWO_CONNECTION_AND_XI_REDUNDANCY__SOURCE_SILENT_ALGEBRAIC_BRANCH_SOURCE_TANGENT_STATIONARITY_AND_TANGENT_COMPLETENESS`.
