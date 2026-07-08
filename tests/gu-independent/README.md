# GU-independent certificate family

Executable certificates for the GU-independent frame-triviality / structural-law result:
`canon/frame-triviality-structural-or-evadable-GU-independent-RESULTS.md`.

These scripts do not prove three generations, derive a GU source action, or change
any claim status, verdicts, or public posture. They test the class-level structural no-go:
whether an operator internal to the Clifford-Rarita-Schwinger carrier can force an odd
chiral count, versus requiring an external index / anomaly-inflow input.

## Result Boundary

The recorded result is a refined no-go: frame-active linear chirality coupling exists on
the carrier and produces 2-primary counts, but it is not an index-forcing antilinear
escape. The surviving boundary is that an odd/order-3 count is not forced by an internal
linear or antilinear carrier operator in this class.

## Scripts

| script | role |
|---|---|
| `structural_frame_triviality_metatheorem.py` | Construct-side meta-theorem test over the Clifford-RS carrier, including frame-charge and selected-half counts. |
| `adversarial_frame_chir_orthogonality_probe.py` | Independent probe that refutes the overly-clean trace-orthogonality claim by detecting self-dual carrier entanglement. |
| `decisive_escape_vs_forcing.py` | Separates the frame-active linear escape from the actual forcing notion and factors the resulting counts. |
| `adv_verify_escape_class_check.py` | Adversarial check that the frame-active linear escape is not a Krein-isometric or antilinear index escape. |
| `frame_active_antilinear_chiralizer_hunt.py` | Constructive hunt for a frame-non-trivial antilinear chiralizer. |
| `adversarial_gauge_artifact_check.py` | Checks whether the best antilinear candidate is only a connected gauge dressing of the baseline. |
| `verify_structural_crux_independent.py` | From-scratch recomputation of the load-bearing connectedness/carrier-preservation mechanism. |
| `nongu_source_action_chiral_count.py` | Non-GU source-action attempt that tests frame-charged gradings and explicit source-action-style operators. |
| `adv_verify_escape_hunt.py` | Adversarial search over genuine carrier involutions and conjugation gradings for a missed escape. |
| `minimal_forcing_ingredient.py` | Computes the operator-side obstruction and identifies the external index/anomaly-inflow ingredient boundary. |
| `escape_search_chirality_odd_frame.py` | Broad chirality-odd frame-coupled search; retained as a heavy exploratory probe, not a load-bearing certificate. |

## Running

From the repo root, run the central harness:

```powershell
python scripts/reproduce_all.py --quick -k gu-independent
```

For targeted review, run the load-bearing scripts directly:

```powershell
python tests/gu-independent/adversarial_frame_chir_orthogonality_probe.py
python tests/gu-independent/decisive_escape_vs_forcing.py
python tests/gu-independent/adv_verify_escape_class_check.py
python tests/gu-independent/adversarial_gauge_artifact_check.py
python tests/gu-independent/verify_structural_crux_independent.py
python tests/gu-independent/minimal_forcing_ingredient.py
```

`adv_verify_escape_hunt.py` and `escape_search_chirality_odd_frame.py` are intentionally
heavier than the rest. Use them when re-auditing the broad search surface rather than
for short smoke checks.

## Honest Scope

- Computed certificates: carrier dimensions, frame charges, traces, selected-half counts,
  candidate leakage/isometry checks, and the decisive escape-vs-forcing probes.
- Adversarially verified corrections: the naive full-space orthogonality argument is too
  strong on the projected carrier; the frame-active linear channel exists but remains
  2-primary and non-forcing.
- Analytic boundary: the external index/anomaly-inflow route is identified as the natural
  remaining ingredient, but this directory does not build that source action or pin the
  value three.

`process_gates/gu_independent_readme_inventory_audit.py` keeps this README
synchronized with the tracked direct scripts and the no-status-movement boundary.
