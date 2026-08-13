---
artifact_type: construction_result
created: 2026-08-12
run_id: RUN-20260812-110014-gu-i2b-full-unitary-image-covariance
lane: 1
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_claims: [SC-GRP-01, SC-GRP-02, SC-ACT-02, SC-ACT-04]
source_return: SOURCE_CONFIRMS_FULL_U64_64_PARENT_TWO_WEYL_HALVES_AND_RESIDUAL_SQUARE__REPO_CORRECTS_V0202_POINTWISE_COMPLEMENT_FENCE__SOURCE_SILENT_ON_SELECTED_SHIAB_GLOBAL_CONNECTION_AND_MOVING_HQ_DERIVATIVES
verdict: FULL_POINTWISE_U64_64_AND_BLOCK_U32_32_DIRECT_SHIAB_CANCELLATION_KILLED__MOVING_DERIVATIVE_GLOBAL_AND_ALTERNATE_SELECTOR_ROUTES_OPEN
target_claim: NONE-NOT-A-KILL
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
fork_assumed: none
search_space_dim: 16384
free_object_delta: 0
residue_touched:
  - "RA-E1:T2_DISTANCE_ONLY"
  - "RA-E3:T2_DISTANCE_ONLY"
  - "LT-SM6:T2_DISTANCE_ONLY"
---

# Selected K77 I2B full-unitary image and covariance gate

## Outcome

Ledger v0.202 drew one fence too conservatively.  Its `99,463`-column bank was
described as a finite fixed-`H_q` Clifford bank distinct from the pointwise
source-full `U(64,64)` algebra.  Exact prior art and a new composition theorem
show that, for the pointwise image question, there is no missing complement.

The phase-completed real Clifford basis is exactly all of

```text
u(H_q) = u(64,64),  dim_R = 16,384.
```

The v0.202 grades `0,2,4` bank is the complete part of that full algebra able
to reach the Clifford-grade-one displasion target through the selected Shiab.
The target is outside its image.  Therefore direct pointwise cancellation is
excluded not only for a finite sub-bank, but for the full `u(64,64)` parent
and hence for its block `u(32,32)+u(32,32)` subgroup.

This is still a route kill, not a theory kill.  A global principal connection,
derivatives of the moving Hermitian form, Bianchi descent, an alternate
source-typed Shiab and the physical quotient remain open.

## Layer 0

These objects are kept separate:

1. the pointwise Lie algebra `u(H_q)`;
2. a global `U(64,64)` principal connection and its curvature;
3. the block `U(32,32)xU(32,32)` subgroup preserving the Weyl halves;
4. two independent connection fields in the inhomogeneous construction;
5. pointwise co-moving conjugation of `H_q`;
6. derivative terms produced when `H_q`, Hodge or Shiab moves;
7. selected-Shiab image membership versus a Bianchi-compatible curvature.

The theorem identifies item 1 with the complete pointwise source-full algebra.
It does not identify items 1 and 2, collapse items 3 and 4, or compute item 6.

## Exact result 1: full pointwise real form

Prior exact work establishes

```text
Cl(7,7) = M_128(R).
```

For every one of the `2^14=16,384` real Clifford blades `X`, exactly one of
`X` or `iX` satisfies

```text
X^dagger H_q + H_q X = 0.
```

The phase count is

```text
8,256 real-phase blades + 8,128 imaginary-phase blades = 16,384.
```

Because the real Clifford blades form a basis of `M_128(R)`, multiplying
individual basis elements by `i` preserves real-linear independence.  The
resulting `16,384` independent `H_q`-skew directions have exactly the real
dimension of `u(64,64)`.  They therefore form its complete pointwise basis.

As a firing control, the combinatorial adjoint rule reproduces all `1,093`
phases that v0.202 independently classified by explicit `128x128` matrices.

## Exact result 2: complete target-relevant image

The selected Shiab multiplies the input Clifford coefficient by one generator
in one summand and three in the other.  It flips parity and changes grade by at
most three.  A grade-one output can therefore receive contributions only from
even input grades `0`, `2`, and `4`:

```text
C(14,0)+C(14,2)+C(14,4) = 1,093.
```

Thus v0.202's enumeration of every form-two slot times every allowed real-form
phase,

```text
91 * 1,093 = 99,463 columns,
```

is complete for the grade-one projection of the entire pointwise
`u(64,64)` algebra.  Its exact image has rank `364`; adjoining the q13
displasion target raises the rank to `365`.

Since `u(32,32)+u(32,32)` is a subalgebra of `u(64,64)`, it cannot supply a
target absent from the full parent's selected-Shiab image.  This does not say
the full group and block product are the same object.

## Exact result 3: held-out co-moving representative

The complete rank computation was repeated after moving the trace direction
from q13 to q12 and moving the target with it.  The result is identical:

```text
allowed relevant phases: 364 real + 729 imaginary
source columns:           99,463
grade-one image rank:     364
rank with moved target:   365
```

This kills the concern that the exclusion was an accidental property of the
original q13 frame.  Pointwise Spin conjugation transports `H_q`, the unitary
algebra, selected Shiab and target together, so image membership is invariant
under that co-moving action.  Derivatives of the moving objects are not
pointwise conjugations and remain uncomputed.

## Correction to v0.202

v0.202 remains immutable.  Its exact rank result was correct; only its scope
fence was too weak.  Replace the sentence

```text
the full source-unitary complement remains unconstructed
```

by the typed statement

```text
there is no missing pointwise u(64,64) complement; the remaining completion
is global/derivative, not an additional coefficient-fibre direction.
```

The two `U(32,32)` halves remain a distinct block presentation, but they are
not a larger pointwise supplier than their full parent.

## Constraint accounting

- New fields: `0`.
- New parameters: `0`.
- New data: `0`.
- New selectors: `0`.
- P1/P2/P3: unchanged and unused.
- Pointwise full-unitary complement: closed as nonexistent.
- Moving-form derivative and global-connection completion: open.

## What died and what survived

**Died:**

- direct pointwise selected-Shiab cancellation by any `u(64,64)` curvature
  coefficient at fixed/co-moving `H_q`;
- the block `u(32,32)+u(32,32)` subgroup as a revival of that direct route;
- the claim that v0.202 omitted pointwise full-unitary coefficient directions
  relevant to the grade-one target.

**Survived:**

- moving-`H_q` derivatives of Hodge/Shiab and the connection compatibility
  equation;
- global curvature realization, Bianchi identities and atlas descent;
- a different source-typed Shiab or adjoint-Shiab channel;
- the full second-action Euler/preboundary calculation;
- physical reduction, Higgs spectrum, Yukawa placement, BV and domain.

## Next gate

Differentiate the moving `H_q`, Hodge and selected Shiab in the source-full
connection geometry and insert those terms into both the first-shell residual
and the second-action Euler map.  Do not search another pointwise full-unitary
coefficient bank: that space is now exhausted.
