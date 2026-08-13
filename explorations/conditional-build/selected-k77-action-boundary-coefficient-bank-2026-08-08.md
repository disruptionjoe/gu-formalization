---
artifact_type: construction_result
created: 2026-08-08
status: ACTION_ACTIVE_CL1_CL2_TEN_NORMAL_BANK_EXACT__COMPLETE_OBSERVATION_LOSSLESS__LOCAL_ENDPOINT_DRESSING_ACCEPTS_ACTION_COVECTOR
source_return: SOURCE-CONFIRMS__NONQUADRATIC_ACTION_T_CHAIN__SOURCE-SILENT__PREFERRED_SHIAB_BFV_AND_FULL_U64_64_EXTENSION__REPO-DERIVES__SELECTED_COMM_SYMI_SYMI_CL1_CL2_ACTION_BANK
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_action_boundary_coefficient_bank_probe.py
  - tests/channel-swings/selected_k77_action_boundary_coefficient_bank_independent.sage
registry: lab/process/selected-k77-action-boundary-coefficient-bank.json
---

# Selected K77 action boundary coefficient bank

## Result first

The missing local owner from v0.75 now exists on the admitted low-grade K77
action tangent.  Exact differentiation of the same selected
`comm/symi/symi` action gives the coefficient covector

\[
  E_B-E_T
\]

in every one-form direction with a real `Cl1 + Cl2` coefficient.  On the
predeclared deterministic background, its fourteen exterior rows have rank
fourteen.  The ten metric-fibre normal rows are all nonzero and have rank ten,
with support fingerprint

```text
13, 14, 12, 16, 13, 16, 13, 12, 5, 8.
```

This is not a fitted current or a free `K`.  Both analytic Euler derivatives
were checked against exact five-point differentiation of the same action, and
an independent Sage reconstruction reproduced the complete bank, ranks,
supports, action fingerprints and Gram determinants.

The complete `4+10` observation equation dual is an invertible triangular
map with a written inverse.  It preserves the full rank-fourteen bank and a
rank-ten observed normal bank.  Naive tangential pullback retains only four
rows and therefore still fails.  On the program-native scalar Clifford
coefficient form, the raw and observed ten-dimensional images are
nondegenerate with exact inertias

```text
raw normal image:      (4 positive, 6 negative, 0 null)
observed normal image: (5 positive, 5 negative, 0 null).
```

The two endpoint restrictions take opposite Green orientations and each
retains rank ten.  Therefore the already-exact two-copy endpoint dressing can
accept the selected action covector locally.  This closes the arbitrary-`K`
gap without inventing another edge field or external datum.

## What this does not prove

The firing point proves that a rank-ten minor is not the zero polynomial on
the selected low-grade action family; it is not a selected vacuum, a field
equation solution or a theorem at every background.  The coefficient tangent
is the 105-dimensional real `Cl1 + Cl2` sector, not the full `U(64,64)`
coefficient algebra.  The scalar Clifford form tested here is the exact
program-native low-grade coefficient pairing; identifying it with the full
physical Krein domain is still open.

Likewise, the written rational observation graph proves the complete-germ
receiver is lossless and exposes why pullback alone fails.  It does not
construct the global physical observation section.  Opposite endpoint copies
and the v0.74 local `40/40` quotient are not a global `tau_A0` overlap theorem,
a BFV charge algebra, a polarization or a common analytic domain.

## Layer 0

| phrase | exact object here | not identified with |
| --- | --- | --- |
| selected action | source-shaped first-order action with repo-selected `comm/symi/symi` Shiab channel | Weinstein's missing preferred historical Shiab |
| coefficient bank | exact directional `E_B-E_T` on `Omega1 x (Cl1+Cl2)` | arbitrary fitted current or full `U(64,64)` coefficient algebra |
| ten normals | rows 4 through 13 in the fixed `4+10` exterior split | ten arbitrary coefficient directions |
| complete observation | invertible equation-dual graph on all `4+10` rows | tangential pullback or global section theorem |
| inherited pairing | scalar Clifford-product form restricted to the action image | positive Hilbert metric or full physical Krein domain |
| endpoint acceptance | two independent local restrictions with opposite Green signs | diagonal endpoint identification or global BFV phase space |

## Exact action and derivative control

At the deterministic real fixture the selected cubic and quadratic pairings
are respectively

```text
<T,S(P)> = 176
<T,*T>   = -24.
```

The action is

\[
 I(B,T)=\langle T,S(P(B,T))\rangle+
         \tfrac12\langle T,*T\rangle,
\]

where

\[
 P=B\wedge B+\tfrac12(B\wedge T+T\wedge B)+\tfrac13T\wedge T.
\]

Dense held-out `B` and `T` directions agree exactly between the analytic
Euler formula and finite differentiation.  Deleting the quadratic `T`
derivative fires a planted failure.  Deleting one normal receiver row drops
rank to nine; diagonalizing the two endpoints loses one endpoint coordinate;
and replacing complete observation by tangential pullback loses the normal
receiver.

## Source return

The primary-source pack fixes the nonlinear first-order action family and the
two-connection distortion `T`.  It does not select BFV variables, print the
preferred historical Shiab, or establish the full coefficient/global
extension used downstream.

```text
SOURCE-CONFIRMS: nonlinear action and T chain
SOURCE-SILENT:   preferred Shiab, BFV and full U(64,64)/global extension
REPO-DERIVES:    comm/symi/symi Cl1+Cl2 action bank and local endpoint acceptance
```

## Seven-axis disposition

- **Layer 0:** action covector, normal rows, observation dual, coefficient
  pairing, endpoint restrictions and BFV phase space are separated.
- **L1 syntactic:** the selected action, Euler directions, coefficient basis,
  observation matrix and endpoint signs are explicit.
- **L2 type:** all ten normal rows live in the dual of the same 105-dimensional
  low-grade action tangent; no fitted receiver is used.
- **L3 algebraic:** ranks, supports, determinants, inertias, inverse transport,
  derivative controls and planted failures pass exactly and independently.
- **L4 geometric:** a local fixed split and a complete graph receiver pass;
  full bundle overlap and actual global observation remain open.
- **L5 variational:** `E_B-E_T` is derived from the same selected action and
  may be inserted into the existing local endpoint cotangent dressing.
- **L6 analytic:** no common closed Krein/Green domain, polarization or global
  BFV phase space is claimed.
- **L7 physical:** no vacuum, Einstein equation, spectrum, positivity,
  unitarity or cosmological prediction is promoted.

## Constraint fence and progress

```text
new fitted K/current: 0
new external datum: 0
new coefficients or selectors: 0
new fields: 0
P1/P2/P3 consumed: 0

Ledger v0.76 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: NONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed are the selected low-grade all-ten bank, its lossless complete
observation transport, and its nondegenerate oriented local endpoint
acceptance.  Opened is the honest full-coefficient/globalization burden.  No
verdict, residue, quotient, datum, canon or public-posture count moves.

Curt remains formally separate inside the Eric lane.  No third lane is
promoted.

## Next gate

Extend the selected action bank from the admitted `Cl1 + Cl2` tangent to the
actual full coefficient/bundle carrier, prove overlap naturality with the
physical observation section, and then assemble the global `tau_A0`/BFV
moment map and common Green/Krein domain.  Keep the coupled nonzero-fermion
residual and the distinct `I2B <-> ||II||^2` map separate.

