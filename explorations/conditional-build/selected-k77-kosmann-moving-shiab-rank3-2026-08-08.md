# Selected K77 Kosmann moving-Shiab rank-three gate

Status: exact internal Ward closure; physical diffeomorphism Frechet/Green gate open. No canon, verdict, datum, quotient, or public-posture change.

## Plain-English result

The previous wave correctly found a three-direction obstruction, but it compared the spacelike and null labels with a response operator still frozen at the timelike covector. Recomputing with the operator matched to each covector preserves rank three while changing those coefficient packets.

The explicit motion of the Shiab coefficients also has rank three, but it is not the negative of the previous packet. Equal rank is not cancellation. The cancellation occurs only after assembling the whole lower-order bivector gauge tangent:

\[
\delta A=q\eta+[T,\eta],\qquad \delta F=[F,\eta],
\]

together with the differentiated moving `Phi_i`/Shiab coefficients. That complete response sends the raw `Upsilon` variation to zero coefficientwise in timelike, spacelike, and null cases, with no fitted parameter.

This closes the internal homogeneous bivector Ward orbit. It does **not** yet close the physical spacetime diffeomorphism: Lie transport, density, Hodge, observation, lower-order metric terms, and the distinction between dependent Kosmann transport and a primitive epsilon Euler row remain to be constructed.

## Exact outputs

| class | matched-q supports | v0.86 frozen-q0 supports | rank before | rank after full lower-order completion |
|---|---:|---:|---:|---:|
| timelike | `(0,1,1,1)` | `(0,1,1,1)` | 3 | 0 |
| spacelike | `(1,0,1,1)` | `(13,0,2,2)` | 3 | 0 |
| null | `(2,5,5,2)` | `(14,7,7,14)` | 3 | 0 |

The opposite lower-order sign fails. The grade-one gamma-soldering proposal is unused. P1/P2/P3 remain unused.

## Layer 0

- Moving Shiab alone is not the complete connection/curvature gauge tangent.
- An internal H-valued bivector gauge orbit is not automatically the physical spacetime diffeomorphism orbit.
- Dependent Kosmann frame transport is not automatically a primitive epsilon Euler equation.
- A Ward identity is not yet a reduced symplectic class, BFV phase space, Green operator, or quantum measure.

## Source return

`SOURCE-CONFIRMS` the moving conjugated `Phi_i(epsilon)` grammar and primitive epsilon variation. `SOURCE-SILENT` on the missing physical diffeomorphism soldering and analytic/domain completion.

## Next gate

Construct the covector-matched physical diffeomorphism Lie/density/Hodge/observation and lower-order metric packet, prove the full Frechet identity `J R=0`, then derive `K*`, the formal adjoint and Green concomitant before stationary Gram, Einstein, symplectic or BFV claims.

## Reproducibility

- Python exact probe: `tests/channel-swings/selected_k77_kosmann_moving_shiab_rank3_probe.py`
- Independent Sage certificate: `tests/channel-swings/selected_k77_kosmann_moving_shiab_rank3_independent.sage`
- Typed registry: `lab/process/selected-k77-kosmann-moving-shiab-rank3.json`
