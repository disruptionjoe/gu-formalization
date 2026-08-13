---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
run_id: RUN-20260812-043842-gu-trace-hq-connection-internal-chain
status: SPLIT_SPIN_TRACE_HQ_COMPATIBILITY_CONSTRUCTED__FROZEN_Q_PATI_SALAM_AND_EXISTING_VPSB_COMPOSITION_FAILS__MOVING_FULL_UNITARY_AND_DISTINCT_VARPI_BLOCK_OPEN
target_claim: NONE-NOT-A-KILL
ledger: lab/process/conditional-physics-ledger-v0.195.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 trace-Hq connection and internal-chain gate

## Result in plain English

The trace-owned Hermitian form now has an exact compatible connection at the
K77 split-spin layer, but the compatibility condition is not free.  For a
fixed trace direction, it keeps

```text
Spin(1,3) x Spin(6,3)        dimension 6 + 36 = 42
```

inside `Spin(1,3) x Spin(6,4)`.  The nine removed normal connection
components are exactly the directions that move the trace line.  They are not
lost information: `D H_q` reconstructs all nine of them exactly.

That answers the connection question conditionally and exposes a decisive
representation fork.  Freezing q loses the full Pati-Salam maximal compact
`Spin(6)xSpin(4)` and leaves `Spin(6)xSpin(3)`.  The latter contains an
abstract `su(3)+su(2)+u(1)` algebra, but that is not enough.  Its naive
restriction sends both Pati-Salam chiral doublets to doublets of the same
diagonal `SU(2)`, and its exact intersection with the repository's independent
rank-one `(4,1,2)` Pati-Salam breaking vector has dimension `9`, not the
Standard Model's `12`.

So trace q cannot secretly do two jobs.  It supplies the Hermitian form with
zero datum cost, but it is not the existing Standard-Model breaking vector and
its nine-component connection defect is not a Higgs doublet.  The viable route
is now sharper: retain the moving `H_q` / full-unitary parent while constructing
the distinct action-owned `varpi` cell and the source's Pati-Salam--`U(3,2)`
intersection.  Only that composition can be tested for the observed scalar
doublet, Yukawa placement and symmetry-breaking surplus.

## Layer 0 and pre-wave

No signature horn or action parent was selected.

| phrase | object tested here | not identified with it |
|---|---|---|
| moving `H_q` | natural Hermitian-form family transported with `q_g` | one frozen matrix in every frame |
| `D H_q=0` | connection compatibility with the trace reduction | action selection of that connection |
| fixed-q stabilizer | `Spin(1,3)xSpin(6,3)` at the split-spin layer | full `U(64,64)` or two `U(32,32)` parents |
| Pati-Salam | maximal compact `Spin(6)xSpin(4)` of the full normal `Spin(6,4)` | mere containment of a 12-dimensional algebra |
| `v_PSB` | independent rank-one vector in `(4,1,2)` whose stabilizer is the SM | trace q in the normal vector `(1,2,2)` |
| connection defect | nine directions reconstructed from `D H_q` | a four-real-component Higgs doublet |
| Higgs-like cell | source-assigned component of the ad-valued one-form `varpi` | trace q or its stabilizer by naming |

The finite connection and branching calculation is decided wholesale.  The
full source connection, `U(3,2)` intersection, nonlinear action vacuum,
observed scalar block, Euler/BV equations and analytic domain are outside it.

## Exact connection theorem

Let `Q=gamma(q_g)` and `H_q=i B Q`, with spin generators `X` that are
`B`-skew.  Then

```text
X^dag H_q + H_q X = 0    iff    [X,Q] = 0.
```

All six base Lorentz generators commute with `Q`.  In the normal algebra,
`36/45` generators commute and the remaining nine are exactly
`q wedge q-perp`.  Hence

```text
ker(D H_q on the split-spin algebra)
  = spin(1,3) + spin(6,3),             dimension 42,

rank(D H_q) = 9.
```

For the broken part `X_perp`, the defect is lossless:

```text
X_perp = -(1/2) [X,Q] Q.
```

Thus `D H_q=0` is a valid construction of a reduced compatible connection,
while general split-spin connections decompose into the compatible connection
plus a canonical nine-component reduction-breaking tensor.  The preceding
action Hessian is nondegenerate on its already-tested moving-structure
breaking banks, so the current action does not yet force this tensor to zero.

## Internal-chain result

For negative normal q,

```text
Stab_normal(q) = Spin(6,3),
maximal compact = Spin(6) x Spin(3),    dimension 15 + 3 = 18.
```

The full source Pati-Salam compact is

```text
Spin(6) x Spin(4),                     dimension 15 + 6 = 21.
```

Fixing q breaks three compact and six noncompact normal generators.  The
residual compact algebra does abstractly contain
`su(3)+u(1)+su(2)`, but representation recovery fails under the naive
identification:

```text
(4,2,1) + (4bar,1,2)
       -> (4,2_diag) + (4bar,2_diag).
```

Both halves become doublets of the same diagonal `SU(2)`; the Standard Model
right-handed conjugates are weak singlets.  More decisively, exact real linear
algebra inside `su(4)+su(2)_L+su(2)_R` gives

```text
dim Stab(v_PSB)             = 12,
dim Stab(q)                 = 18,
dim (Stab(v_PSB) ∩ Stab(q)) = 9.
```

The two known reductions therefore cannot simply be imposed simultaneously
and called the Standard Model.  This does not refute source claim `SC-GRP-03`:
that claim uses the intersection of the full Pati-Salam and complex `U(3,2)`
reductions.  It means the exact `U(3,2)`-relative placement is now the required
next object rather than an optional embellishment.

## Higgs and datum accounting

The nine broken directions split under the residual compact group as real
`6+3`, not as a four-real-component scalar doublet.  Normalized q also lacks a
free radial amplitude.  Source claims `SC-FER-03`, `SC-GEO-58` and
`SC-META-57` instead place Higgs-like behavior in a component of the
ad-valued one-form `varpi` and deny a separate fundamental Higgs.  The result
therefore strengthens, rather than relaxes, the Layer-0 fence: q supplies the
Hermitian reduction; another action-owned `varpi` cell must carry the observed
scalar physics.

No continuous, functional or discrete datum is added.  P1/P2/P3 remain
unchanged.  No quotient, verdict, canon or public posture moves.

## Adaptive specialist and hostile review

- **Layer-0/prior art — actual math, very high:** found the source's already-
  printed `Spin(6,3)xSpin(0,1)` stage and the independent `(4,1,2)` `v_PSB`.
- **Principal-bundle geometry — actual math, very high:** types `D H_q=0` as
  a reduction-compatible connection, not an action-selected vacuum.
- **Clifford/Krein — actual math, very high:** proves compatibility iff
  `[X,Q]=0` and reconstructs the rank-nine defect.
- **Representation theory — actual math, very high:** distinguishes abstract
  SM algebra containment from the incorrect diagonal-`SU(2)` fermion branch.
- **Symplectic/variational — actual math, high:** prevents q from acquiring a
  fictitious independent field equation or Higgs identity.
- **Analytic — actual math, high:** no positivity or domain follows from this
  finite reduction.
- **Contrary path — actual math, high:** the moving `H_q` family and full
  source-sized unitary connection remain viable and now lead the route.

The exact probe passes `56/56` new checks plus the predecessor's `50/50`, with
five firing controls.  Six ledger rows move only in distance/evidence.
Coverage `82/82`, verdicts `32/19/26/5`, residue `84`, at least `19`
function-valued slots, nine forks and five quotients remain unchanged.

## Next gate

```text
CONSTRUCT_THE_EXACT_SOURCE_U3_2_INTERSECTION_RELATIVE_TO_THE_MOVING_TRACE_HQ
FAMILY__TEST_WHETHER_IT_PRESERVES_THE_EXISTING_12_DIMENSIONAL_SM_STABILIZER_AND
THE_16_STATE_HYPERCHARGE_BRANCH__THEN_DECOMPOSE_THE_FULL_OR_TWO_HALF_VARPI
CONNECTION_AND_REQUIRE_A_DISTINCT_ACTION_OWNED_OBSERVED_SCALAR_DOUBLET_WITH
KINETIC_POTENTIAL_YUKAWA_AND_POSITIVE_CONSTRAINT_SURPLUS.
```

The alternative if the `U(3,2)` placement cannot close is to keep `H_q`
moving under the full `U(64,64)` connection and treat fixed-q compatibility as
an adapted-frame description rather than the physical gauge stabilizer.
