---
artifact_type: conditional_build_result
created: 2026-08-07
status: FULL_EPSILON_FRAME_EXTENSION_EXACT__UNFRAMED_STABILIZER_BASICNESS_FAILS__SOLDERING_IDENTIFICATION_OPEN
source_return: SOURCE-CONFIRMS__GAUGE_EPSILON_PROMOTED_TO_FIELD_CONTENT_AND_FULL_VARPI_TRANSLATION__SOURCE-SILENT__EPSILON_AS_THE_OBSERVATION_SOLDERING_AND_FOUR_COLUMN_SELECTOR
ledger: lab/process/conditional-physics-ledger-v0.58.json
canon_verdict_change: none
---

# K77 source-graph covariance and quotient basicness

## Result in plain English

The repaired four-column source-`varpi` map can be carried consistently from
patch to patch **if the complete moving K77 frame is retained**. Two
independent exact overlaps and their direct composite agree; the source
endpoint and Spencer maps commute with that transport.

That is not yet the graph object needed by the physical construction. A
physical graph on the unframed quotient must not depend on which equivalent
K77 frame represents the same observed geometry. The fitted map fails this
test. Two horizontal stabilizer rotations produce rank-four defects with 118
nonzero coordinates each. More decisively, a normal rotation that leaves the
observed horizontal four-plane fixed changes all four source lifts, with a
rank-four, 80-coordinate defect.

So the current object is an exact **upstairs framed lift**, not a basic
quotient-level graph morphism. The constructive route remains open, but its
next burden is now narrower: either the action/source must identify Weinstein's
full gauge `epsilon` with a physical observation/soldering selector, or the
four-column map must be replaced by a stabilizer-invariant construction.

## Layer 0

| phrase | object established | object still missing |
| --- | --- | --- |
| covariant graph | an associated family on the full K77 frame bundle | a basic map independent of stabilizer frame choice |
| source `epsilon` | a gauge transformation promoted to field content | the observation/soldering field selecting the physical four-plane |
| three-patch descent | exact principal-frame cocycle transport | descent to the unframed/physical quotient |
| constraint surplus | zero coefficient freedom after the pointwise fit | a quotient-grade surplus after charging any full-frame functional datum |
| symplectic descent | none | a basic Euler/preboundary class on reduced covariant phase space |

This prevents two opposite errors. Frame covariance cannot be sold as physical
descent, and failure of this unframed map cannot be sold as a no-go for every
smaller observation- or soldering-reduced structure group.

## Exact construction

Let `L` be the corrected v0.57 map from the four horizontal graph directions
to `V* tensor so(7,7)`, with supports `57,34,34,34` and rank four. Exact
signed rotations inside equal-sign planes preserve the K77 metric and
orientation. For a stabilizer element `g`, frame-free equivariance would
require

```text
rho(g) L = L sigma(g).
```

It fails:

```text
horizontal rotation (1,2): rank 4, 118 nonzero defect entries
horizontal rotation (2,3): rank 4, 118 nonzero defect entries
normal rotation (4,5):     rank 4,  80 nonzero defect entries
```

The normal rotation is the cleanest witness because it fixes the horizontal
four-plane pointwise while changing the fitted source map.

There is also an invariant-theory cross-check. For the oriented block
stabilizer on `H plus N`, the standard tensor decomposition gives three
canonical maps from `H` to `V* tensor Lambda2(V*)`: horizontal metric
contraction, normal metric contraction and the four-dimensional horizontal
volume contraction. Their flattened span has exact rank three. Adding the
fitted `L` raises the rank to four; the exact linear system has no solution.

The full-frame escape is nevertheless exact. With local frames
`f0=1`, `f1=g01`, `f2=g12 g01`, define

```text
L_i = rho(f_i)L,
s_i = f_i s_0.
```

Then both pairwise overlaps and the direct overlap transport `L_i`, the
four-plane soldering, the Spencer image and the source endpoint exactly. A
planted alternate local frame remains pointwise self-consistent but fails the
declared overlap, proving that local source fitting alone does not establish
descent.

## Constraint surplus

The pointwise coefficient freedom remains zero. Conditional on an already
owned full `epsilon` frame, the framed extension adds no coefficient. But no
positive **quotient** surplus is booked:

```text
CONSTRAINT_SURPLUS =
  UNBOOKABLE_ON_QUOTIENT__FULL_FRAME_FUNCTIONAL_COST_UNRANKED
```

If the full frame is introduced merely to carry the fitted map, it is a new
function-valued selector and must be charged. If it is already an action-owned
physical field, the missing construction is the map identifying it with the
observation soldering and proving the quotient appropriate. P1/P2/P3 do not
supply that map and remain unchanged and unused.

## Source return

The source material explicitly treats `epsilon` as a gauge transformation
promoted to field content and writes the full `(epsilon,varpi)` source
coordinate. It does not identify that `epsilon` with the repo's dynamical
observation/soldering datum, nor state that it selects these four fitted
columns.

```text
SOURCE-CONFIRMS:
  gauge epsilon promoted to field content and the displayed full varpi
  translation.

SOURCE-SILENT:
  epsilon as the observation soldering and as selector of the four-column
  graph map.
```

## Progress and fences

```text
Ledger v0.58 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 1
  - exact full-frame three-patch extension of the corrected K77 map
frontier_conditions_opened: 1
  - quotient basicness / epsilon-soldering ownership
remaining_named_conditions: 3
  - source/action-owned epsilon-to-observation-soldering identification or
    stabilizer-invariant replacement
  - total raw-Upsilon Bianchi/naturality plus null screen
  - survivor-only Euler/preboundary/symplectic and common-domain descent
```

No verdict, residue, quotient count, external datum, canon verdict or public
posture moves. A non-basic source density is not an Euler covector or a class
on reduced covariant phase space.

## Next gate

Run Source and Build together on the new single fork:

1. construct an action-owned map from source gauge `epsilon` to the
   observation/soldering frame and prove that its stabilizer is small enough
   for the four-column map; or
2. construct a replacement in the exact three-dimensional block-invariant
   Hom space and test whether it can still reproduce the four K77 targets.

Only a quotient-basic survivor advances to total raw-`Upsilon`
Bianchi/naturality and Euler/preboundary/symplectic descent. The executable
probe passes `44/44` with a locally fitted, non-descending planted control.
