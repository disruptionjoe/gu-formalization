# CPTt triality native-action gate

Date: 2026-07-15

Repository revision at intake: `78e0822`

Tier: exploration

Overall result: `UNDERDEFINED`

Scoped result for the current typed 2+1 construction: `NO_GO`

## Question

Does the finite triality construction in A. Garrett Lisi, *C, P, T, and
Triality*, arXiv:2407.02497v2, supply a missing native GU family symmetry, a
generation-count derivation, or a physical Standard Model recovery step?

The adversarial gate asks for more than a matching order-three matrix. A
survivor must act on one GU-derived physical fermion carrier, preserve its field
types and charges, preserve the action, descend through the constraints to the
positive physical quotient, and not begin by naming three generations.

## What the cited paper establishes

The paper extends `C`, `P`, and `T` by an order-three quaternionic operation
`t`. It builds a finite group described as the central product of the binary
tetrahedral group and `D4`, of order 96, acting projectively on a 24-cell made
from three Dirac-generation cubes. The construction organizes three supplied
Dirac generations. It does not derive why the number of generations is three.

This quaternionic `t` is not the same construction as Spin(8) Dynkin triality.
It is structurally close to the cyclic action on
`Lambda^2_+(R^4) ~= su(2)_+ ~= Im(H)`. Therefore GU's older Spin(8)-triality
commutant obstruction is not, by itself, a refutation of this paper's `t`.

The paper also states that one generated creation-conjugation operation maps
positive-energy annihilation states to nonphysical negative-energy states and
is not a symmetry of nature. The order-96 closure is consequently a kinematic
organization, not already a positive-Hilbert-space symmetry.

## Exact quick check

`tests/cptt/cptt_triality_gate.py` uses exact rational arithmetic to obtain:

| Check | Result | Meaning |
|---|---|---|
| `2T` Hurwitz units | `PASS`, 24 elements | Finite positive control |
| `(2T x D4)/Z2` | `PASS`, 96 classes and center order 2 | Abstract group-order and center control |
| Quaternion sign | `PASS` | Equation 6.2's negative unit has raw order 3; the positive unit printed later has raw order 6 but projective/adjoint order 3 |
| Quaternion adjoint | `PASS` | `Ad_t` cycles `i -> j -> k -> i` exactly |
| Three-cycle character | `PASS`, dimension 3 and trace 0 | Same real `C3` representation type as the native GU self-dual triplet |
| Repeated-copy equivariance | `PASS` | Negative control: manually copying one operator three times always manufactures a commuting cycle |
| Split third operator | `PASS`, cycle fails | The control has teeth when the third sector differs |
| GU typed 2+1 Lorentz gate | `NO_GO` | Spin-1/2 Casimir `3/4` differs from spin-3/2 Casimir `15/4`, so every Lorentz intertwiner between them is zero |
| Full GU physical CPTt | `UNDERDEFINED` | No derived family-frame identification, interacting equivariance, or positive-quotient lift exists |

The finite positive control reproduces the abstract central-product order and
the 24 Hurwitz vertices. It does not reproduce or certify every matrix and
uniqueness claim in the paper.

## GU comparison

GU has two different appearances of three that must not be conflated.

First, the native self-dual carrier in
`explorations/wave15/H38-z3-chiral-selector-2026-07-11.md` has dimension
`192 = 3 x 64` and admits an order-three element with three 64-dimensional
eigenspaces. This is a real kinematic match to the paper's quaternionic
three-cycle. Existing GU work also shows that the triplet is vectorlike, that a
particular `Z/3` subgroup is not selected by the frozen data, and that the
family interpretation of a frame rotation has not been derived. The honest
classification is `KINEMATICALLY_HOSTED`, not `NATIVE_FORCED`.

Second, GU's separate 2+1 construction uses two spin-1/2 sectors and one
Rarita-Schwinger or vector-spinor sector. These have different Lorentz
Casimirs, form degree, projectors, and kinetic-operator types. An invertible
Lorentz-equivariant order-three map cannot cycle the three. This is a scoped
`NO_GO` for adding Lisi-style triality to that current typed construction. It is
not a no-go for all future same-type three-family constructions.

## Physical obligations that remain

A physical survivor would still need:

1. native `C`, `P`, `T`, and `t` operators on the same derived GU carrier;
2. preservation of the CAR algebra and positive-energy subspace;
3. preservation of the Krein metric and descent to BRST cohomology and the
   positive physical quotient;
4. equivariance of kinetic, gauge, Higgs, and Yukawa terms;
5. anomaly checks appropriate to whether the discrete operation is global,
   gauged, or a redundancy;
6. derived symmetry breaking and at least one observable consequence.

The current source-action and physical-QFT gaps stop the check before these
obligations can be discharged.

## Consequence

This paper is useful prior art and a useful representation-level comparator.
It does not reopen generation-count forcing, repair the flavor-rank no-go,
recover the Standard Model, supply the physical Hilbert space, or create a GU
prediction.

On the next substantive hardening pass for the located-not-forced paper, this
reference should be included in the prior-art comparison with the precise
statement that it organizes three supplied Dirac generations using a finite
extension of CPT. That is a draft-factory hardening signal, not a request to
promote or publish anything.

No new technical lane is warranted. The result belongs as a bounded subcheck
inside the existing Standard Model recovery work, and the recovery contract
remains higher priority.
