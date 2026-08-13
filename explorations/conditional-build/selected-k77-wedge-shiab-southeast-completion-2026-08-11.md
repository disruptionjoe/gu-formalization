---
artifact_type: construction_and_composition_result
created: 2026-08-11
ledger_version: "0.173"
result: REAL_K77_WEDGE_SHIAB_SOUTHEAST_FAMILY_PRINCIPAL_SEMISIMPLE__K95_SIGN_REJECTED__TWO_WEIGHTS_AND_REALITY_OPEN
grade: "exact real-K77 flat principal operator family over two finite-field witnesses plus characteristic-zero Clifford identities; source/action selection and global physics open"
canon_verdict_change: none
fork_assumed: none
fork_note: "Real K77 is a labelled conditional comparator; SIGNATURE-AMBIENT and action-parent forks are not settled by this result."
search_space_dim: "four scalar chiral coefficients before semisimplicity; exact two crossed relations leave two weights"
free_object_delta: "zero new fields; two pre-existing family weights remain unselected"
residue_touched:
  - "RA-D4:T2_DISTANCE_ONLY"
  - "RA-F1:T2_DISTANCE_ONLY"
  - "RA-F2:T2_DISTANCE_ONLY"
  - "RA-G2:T2_DISTANCE_ONLY"
  - "LT-SM3:T2_DISTANCE_ONLY"
  - "AC-F1:T2_DISTANCE_ONLY"
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
source_return: SOURCE-CONFIRMS
scripts:
  - tests/channel-swings/selected_k77_wedge_shiab_southeast_completion_probe.py
registry: lab/process/selected-k77-wedge-shiab-southeast-completion.json
---

# Selected real-K77 wedge-Shiab/southeast completion

Status: `CONDITIONAL_CONSTRUCTION_PASSES__SELECTION_REALITY_AND_GLOBAL_DOMAIN_OPEN`

## Plain-English result

The previous rank-128 Jordan obstruction was not a property of every source-admitted fermion operator. It was a property of the source-displayed zero-southeast/contracting-Shiab choice. Replacing the middle block by the source-admitted wedge-Shiab family and turning on the admitted southeast block removes the generalized chains without deleting fields or quotienting observation.

The exact real-`(7,7)` completion has the opposite reciprocal sign from the old quaternionic `(9,5)` completion:

\[
12w_+\ell_- - 11=0,\qquad 12w_-\ell_+ - 11=0.
\]

The old minus sign leaves the full rank-128 defect on K77. The corrected family has invertible time symbol, exact spatial Clifford relations, and a semisimple null characteristic half of rank/nullity `960/960`. Finite Clifford-group averaging supplies a positive common principal symmetrizer in characteristic zero.

This is a real construction gain, not a theory selection. Two chiral weights remain free. With independent barred and unbarred fields the Green time coefficient is nondegenerate, but the operator is not self-adjoint for the current diagonal K77 pairing (adjoint-defect rank `1920`). A compatible reality reduction, global descent/domain, observation, BV cohomology, index and count remain open.

## Layer 0

- changing the Shiab middle symbol is not merely adding a southeast cell;
- semisimple propagation is not coefficient or action selection;
- the `960`-dimensional null characteristic half is not gauge/BV cohomology;
- an independent-dual action is not a K-self-adjoint real action;
- the selected Spin operator, two `U(32,32)` halves, and full `U(64,64)` parent are distinct;
- the K95 right-`H` sign cannot be ported to real K77.

## Exact certificate

The Sage probe constructs the `1920`-dimensional family over `GF(1009)` and `GF(1013)`. Both primes reproduce:

| check | exact value |
|---|---:|
| time-symbol rank | 1920 |
| spatial Jordan ranks | 0, 0, 0 |
| null symbol rank/nullity | 960/960 |
| zero-southeast defect rank | 128 |
| K95 wrong-sign defect rank | 128 |
| independent crossed perturbations | 64, 64; joined 128 |
| Green time rank | 1920 |
| current-pairing adjoint-defect rank | 1920 |
| common symmetrizer rank | 1920 |

The positive characteristic-zero statement is analytic: `H=sum_g g^T g` over the finite Clifford group contains the identity term, so `v^T H v=sum_g ||gv||^2>0` for nonzero `v`.

## Source return and prior art

The 2021 section-9 extraction confirms the wedge-contraction grammar and explicitly admits a nonzero lower-right rival. It does not select this K77 coefficient, its two weights, a reality adjoint, or a common analytic domain. B2C4 is quaternionic K95 prior art and uses the opposite sign. Ledger v0.163 kills every southeast-only repair while leaving Shiab-family changes open; v0.172 then kills the zero-fermion owned-quotient route and promotes operator completion.

Source return: `SOURCE_CONFIRMS_WEDGE_CONTRACTION_GRAMMAR_AND_ADMITS_NONNULL_SOUTHEAST__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_K77_PLUS_11_OVER_12_RELATION_CHIRAL_WEIGHTS_REALITY_REDUCTION_AND_GLOBAL_DOMAIN`.

## Frontier

Closed: exact K77 wedge family; K77/K95 sign separation; rank-128 principal Jordan removal without quotient; semisimple `960/960` characteristic half and positive common principal symmetrizer.

Opened: the corrected operator exposes one sharper combined burden—derive or kill the two chiral weights together with a compatible real/reality adjoint from the selected independent-dual action.

Still open: weight/action ownership; reality adjoint; global descent/Green domain/observation; physical BV cohomology/index/count. P1/P2/P3, residue, quotients, verdicts, canon and public posture do not move.

## Next gate

`DERIVE_OR_KILL_THE_TWO_K77_CHIRAL_WEDGE_WEIGHTS_AND_REALITY_ADJOINT_FROM_THE_SELECTED_INDEPENDENT_DUAL_ACTION__THEN_GLOBAL_DESCENT_GREEN_DOMAIN_AND_OBSERVATION`
