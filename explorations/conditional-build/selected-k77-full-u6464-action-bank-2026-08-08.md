---
artifact_type: construction_result
created: 2026-08-08
status: FULL_U6464_POINTWISE_ACTION_BANK_EXACT__LIVE_GRADES_1_2_5__GRADE5_CORRECTS_LOW_GRADE_SUPPORT_AND_OBSERVED_INERTIA
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS__U64_64_TYPE_COMPLEX_PRESENTATION_AND_ACTION_PRODUCTS__SOURCE-SILENT__PREFERRED_SHIAB_GLOBAL_BUNDLE_BFV_DOMAIN__REPO-DERIVES__FULL_REAL_U64_64_POINTWISE_ACTION_BANK
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_full_u6464_action_bank_probe.py
  - tests/channel-swings/selected_k77_full_u6464_action_bank_independent.sage
registry: lab/process/selected-k77-full-u6464-action-bank.json
---

# Selected K77 full pointwise u(64,64) action bank

## Result first

The selected `comm/symi/symi` action covector has now been evaluated exactly
on every one of the 16,384 real directions in the **pointwise** K77
`u(64,64)` comparator.  This closes the coefficient-fibre extension left open
by ledger v0.76; it does not yet globalize that fibre over the actual K77
bundle.

On the preregistered seed background:

```text
real coefficient directions evaluated: 16384
full exterior-row rank:                  14
metric-normal row rank:                  10
union of live coefficient coordinates:  549
live Clifford grades:                    1, 2, 5
grade-union sizes:                       14, 59, 476
raw full-support inertia:                (4, 6, 0)
observed full-support inertia:           (4, 6, 0)
```

All values are real on the exact real-form basis.  Each live grade separately
has full/normal rank `14/10`.  Every grade-1 and grade-2 entry agrees with the
v0.76 direct evaluator, and selected grade-5 entries agree with direct
Clifford differentiation.  A different held-out background again has only
grades `1,2,5` live, rank `14/10`, and a distinct 628-coordinate union.

The result contains a correction that a rank-only check cannot see.  The
v0.76 `Cl1+Cl2` bank already had rank `14/10`, but omitted 476 live grade-5
coordinates.  Adding them changes the **observed** coefficient-image inertia
from `(5,5,0)` to `(4,6,0)`.  The low-grade bank was therefore rank-complete
for this fixture but not geometry-complete.

## Why the full real comparator has dimension 16,384

The exact K77 Clifford algebra is

\[
  Cl(7,7)\cong M_{128}(\mathbb R).
\]

With the pinned bilinear adjoint, the real B-skew Clifford grades
`{1,2,5,6,9,10,13,14}` contribute 8,128 dimensions.  Multiplying the
complementary B-self grades by `i` contributes 8,256 more.  Their real direct
sum has dimension 16,384, the real dimension of `u(64,64)`.  This is the
source-complex comparator.  It is not the K95/right-H
`Sp(32,32;H)` fork and it is not yet a theorem about global sections of an
associated adjoint bundle.

## Layer 0

| phrase | exact object here | not identified with |
| --- | --- | --- |
| full coefficient bank | pointwise action covector on all 16,384 real K77 `u(64,64)` directions | global adjoint-bundle section |
| live grades | exact nonzero support on two fixed backgrounds | a universal all-background selection theorem |
| bank rank | row rank of the action-derived coefficient matrix | coefficient support or inherited geometry |
| full-support pairing | scalar Clifford coefficient form on the complete live image | positive energy or analytic Krein domain |
| complete observation | invertible rational equation-dual fixture | physical global observation section |
| selected Shiab | repo-selected `comm/symi/symi` realization | Weinstein's missing preferred historical Shiab |
| endpoint acceptance | local opposite restrictions preserve the coefficient pairing | global BFV phase space or moment map |

## Exact method

A naive sweep would require 229,376 directional action evaluations.  Instead,
the action derivative is kept symbolically as sparse terms

\[
  c\,L\,\delta a\,R.
\]

Cyclicity of the scalar Clifford trace gives

\[
  \operatorname{Sc}(L\,\delta a\,R)
  =\operatorname{Sc}(R L\,\delta a),
\]

so one exact adjoint expression evaluates the complete real basis.  This is
an algebraic acceleration, not statistical sampling.  The SymPy probe and an
independent Sage implementation reconstruct the Clifford, exterior, Hodge,
Shiab and action calculations separately.

The grade-specific nonzero-entry counts are:

```text
grade 1:  68
grade 2:  98
grade 5: 600
```

The exact full-support Gram determinants are nonzero:

```text
raw:      720675574777908926000373533816344723456 / 129140163
observed: 675990534521630134428443975864366882756479230976 / 20100618201669201
```

The complete observation map remains invertible, retains ranks `14/10`, and
opposite endpoint restrictions preserve the full-support pairing.

## Source return

The source material supplies the `U(64,64)`-type complex presentation and the
commutator/`i`-symmetric algebra-product vocabulary.  The exact real K77
decomposition and the full pointwise action bank are repo derivations.  The
source does not select the preferred Shiab used here or establish global
adjoint-bundle patching, the physical observation section, BFV variables or a
common analytic domain.

```text
SOURCE-CONFIRMS: U(64,64)-type presentation and algebra-product vocabulary
SOURCE-SILENT:   preferred Shiab, global bundle, physical observation, BFV/domain
REPO-DERIVES:    full real pointwise u(64,64) selected-action bank
```

## Seven-axis disposition

- **Layer 0:** pointwise fibre, global bundle, coefficient support, bank rank,
  equation-dual fixture and physical observation section are separated.
- **L1 syntactic:** all real-form grades, action products and exact adjoint
  expressions are explicit.
- **L2 type:** the bank covers the complete pointwise real comparator; the
  K95/right-H fork and global associated bundle remain separate.
- **L3 algebraic:** two independent exact implementations reproduce ranks,
  supports, determinants, inertias and a held-out background.
- **L4 geometric:** the full pointwise coefficient geometry is known.  Atlas
  patching and physical observation overlaps remain open.
- **L5 variational:** every coefficient is derived from the same selected
  action; no fitted current or coefficient selector is introduced.
- **L6 analytic:** no common closed Green/Krein domain, BFV polarization or
  global phase space is claimed.
- **L7 physical:** no vacuum, spectrum, Einstein equation, positivity,
  unitarity or cosmological prediction is promoted.

## Constraint fence and progress

```text
new fitted K/current: 0
new external datum: 0
new coefficients or selectors: 0
new fields: 0
P1/P2/P3 consumed: 0

Ledger v0.77 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: NONE
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed are the full pointwise real-comparator action bank and its complete
support/pairing correction.  Opened is the narrower global
associated-bundle/physical-observation burden.  No verdict, residue,
quotient, datum, canon or public-posture count moves.

Curt remains formally separate inside the Eric lane.  No third lane is
promoted.

## Next gate

Patch the full pointwise covector as a section of the actual K77 adjoint
bundle and prove overlap naturality with the physical observation section.
Only then assemble the global `tau_A0`/BFV moment map and common Green/Krein
domain.  Keep the coupled nonzero-fermion residual and the distinct
`I2B <-> ||II||^2` map separate.
