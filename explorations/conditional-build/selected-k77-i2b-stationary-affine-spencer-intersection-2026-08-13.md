---
artifact_type: construction_correction
created: 2026-08-13
status: RANK56_RETYPED_AS_FORMAL_JET_SELECTION__NONEMPTY_ENDPOINT_INTERSECTION__SECOND_PROLONGATION_CRITERION_PASSES
source_return: SOURCE_CONFIRMS_PRINTED_ENDPOINT_AND_CONNECTION_GRAMMAR__SOURCE_SILENT_AFFINE_SPENCER_INTERSECTION
ledger_change: none
target_claim: NONE-NOT-A-KILL
scripts:
  - tests/channel-swings/selected_k77_i2b_stationary_affine_spencer_intersection_probe.py
---

# Selected K77 I2B stationary-affine Spencer intersection

## Result first

The corrected rank-56 frozen term is a real compatibility condition, but it
is **not** a nonexistence theorem for stationary formal jets. The previous
wave asked whether one constant lower-order operator `C0` makes the
divergence identity hold on every field. It correctly answered no. This wave
asks the different PDE question: does the stationary affine two-jet fibre
intersect the kernel of the next compatibility map? It answers yes, exactly.

On Weinstein's printed endpoint residual, retaining the repository's
conditional fixed-`H_q` pairing:

```text
old 14-support stationary witness:       misses 2 compatibility cells

restricted (00)+(01) two-jet space:      392 variables
stationarity rank:                        196
compatibility rank on this ansatz:         28
joint rank / augmented rank:              224 / 224
compatible affine-fibre dimension:        168
new exact witness support:                 16
witness denominators:                      1,4,7

complete ten-block two-jet space:         1960 variables
stationarity rank:                         196
compatibility rank:                         56
joint rank / augmented rank:              252 / 252
compatible affine-fibre dimension:       1708
```

Thus even the old restricted ansatz contains an exact rational two-jet that
cancels all 196 endpoint Euler cells and all 56 next compatibility rows. The
original sparse witness was stationary but did not have this stronger
property; its failure is a useful firing control.

The full second prolonged principal symbol was also assembled, not inferred
from the candidate rows. Its receiver is

```text
Sym^2(T*X) tensor E_196,  dimension 10*196 = 1960,
```

and its image has rank `1904` at two independent good primes with an identical
35-step rank profile. The 56 differentiated divergence rows are independent
over `QQ`, annihilate every prolongation column exactly, and exhaust the
cokernel because `1904+56=1960`. The compatible endpoint witness therefore
meets the complete frozen second-prolongation solvability criterion.

## What this corrects

The previous result remains true as written at operator grade:

```text
no constant C0 makes C(D)(H2(D)+H0)=0 identically.
```

What does not follow is:

```text
there is no stationary jet on which the next compatibility condition holds.
```

For a PDE with lower-order terms, a principal-symbol compatibility row can
become an equation restricting lower jets. Requiring the corresponding
coefficient to vanish on the entire field space is stronger than requiring
it on a solution jet. The exact pullback

```text
{stationary endpoint two-jets} x_{J^2} ker(K_H0)
```

is nonempty, of dimension 168 in the restricted ansatz and 1708 in the full
two-jet space. The rank 56 is therefore best typed here as formal-jet
selection—not a local frozen obstruction to existence.

## Second-prolongation derivation

The first Spencer result found the complete cokernel

```text
C_a(E) = sum_lambda d_lambda E_(lambda,a),  a=0,...,13.
```

Differentiating it by `d_beta` gives 56 rows

```text
C_(beta,a)(E) = sum_lambda d_beta d_lambda E_(lambda,a).
```

The exact second prolonged symbol maps fourth field jets to second equation
jets. It has 6,860 source columns (`dim Sym^4(R^4)=35`, times 196 fields) and
1,960 receiver rows. Direct modular elimination gives rank 1,904 twice. The
56 rows above have rational rank 56 and annihilate all 6,860 columns over
`QQ`, so they are the full cokernel. Applying their lower-order right-hand
side to the constructed compatible two-jet gives zero exactly; a fourth jet
therefore exists in the frozen linear system.

This is stronger than merely testing a guessed subset of relations. It is
still not Cartan involutivity or nonlinear existence.

## Layer 0 and structure fingerprint

| field | inherited value | still open |
| --- | --- | --- |
| carrier | 196-real selected connection field/equation bank | physical carrier/projector |
| pairing | repository fixed-`H_q` comparator | source `Q_B` |
| real structure | selected real K77 | another action-owned real form |
| grading | symmetric observed connection two-jets | full unitary/odd parent |
| signature | conditional `(7,7)` fixture | no settlement made here |
| embedding | selected K77 | full `U(64,64)` or block-preserving parent |
| variation | frozen linear endpoint Hessian | complete moving nonlinear Euler/BV |
| globalization | one formal jet and one further prolongation | analytic germ, atlas descent, global domain |

The source carrier `C^(32,32)+C^(32,32)`, the block-preserving unitary parent,
full `U(64,64)` and this 196-real K77 connection bank remain distinct.

## Specialist review

- **Spencer/EDS:** the correct object is the pullback of the equation fibre
  and compatibility kernel. That pullback is nonempty; the 56 rows are the
  full second-prolongation cokernel.
- **Variational bicomplex:** an off-shell differential identity and an
  on-shell compatibility restriction are different. This wave proves the
  latter only.
- **Category/functoriality:** the pullback is the typed composition; matching
  ranks of unrelated maps is not.
- **Principal-bundle geometry:** no field-to-frame adapter or new connection
  is introduced. Existing connection-jet freedom absorbs the condition.
- **Hyperbolic/analytic:** a compatible formal fourth jet supplies neither a
  Cauchy theorem nor convergence of a formal series.
- **Krein:** no positivity follows from the ranks or rational witness.
- **Symplectic:** no preboundary reduction, BFV phase space or quotient follows.
- **Contrary:** the original stationary witness fails two cells, proving that
  the compatibility map is live rather than vacuous.

## Source return and accounting

The source confirms the printed endpoint and connection/covariant-derivative
grammar. It does not print the fixed-`H_q` pairing as `Q_B`, the affine
intersection, the 1,904 rank, or any nonlinear integrability theorem.

```text
SOURCE-CONFIRMS: printed endpoint and connection grammar
REPO-DERIVES:    exact affine intersection and second prolonged cokernel
SOURCE-SILENT:   nonlinear formal integrability, analytic/global existence
```

No field, coefficient, selector, quotient, external datum, P1/P2/P3 use,
ledger row, residue count, canon verdict or public posture changes. The
168/1708 dimensions are spaces of formal solution jets, not theory inputs.

## Next gate

Do not search for a constant adapter merely because the universal identity
fails. Next test the higher nonlinear/moving-coefficient prolongation and its
Cartan/Spencer involutivity, including the action-owned coefficient motions
that are actually present. Only after formal integrability survives should
the program attempt analytic local existence and global observation/domain
descent. Source `Q_B`, physical BV tangent reduction and preboundary/BFV
remain separate.
