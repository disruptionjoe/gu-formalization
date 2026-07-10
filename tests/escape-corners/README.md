# tests/escape-corners/

Escape-corners campaign certificates for the residual carrier A / carrier B
reading forks after the carrier-bit decision campaign. These scripts, companion
analyses, and checked-in run logs support the escape-corners campaign result;
they are computational, algebraic, and bookkeeping certificates, not claim-status
updates. A green run means the listed checks reproduce the current campaign
arithmetic, source-action / field-space declaration fork, and referee
cross-checks. It does not change canon, verdicts, public posture, paper status,
proof status, or the source action gate.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick -k escape-corners --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick -k escape-corners --timeout 300
```

Run one short leg directly when reviewing a specific claim:

```powershell
python tests\escape-corners\audit_a2_corner_open.py
```

`legb1_graded_ig_algebra.py` is intentionally heavy. Use
`legb1_run_record.log` as the verified run record unless a run packet explicitly
authorizes re-running the heavy certificate under the one-heavy-job rule.

## Boundary

The public boundary stays:

- The campaign outcome is corner-narrowing evidence, not a carrier verdict.
- SG4 remains the source action / field-space declaration decider.
- The carrier-A opening is toy-grade and caveated by the selected sub-slot and
  anchor-scale tests.
- The carrier-B tilt remains evidence-tier and cannot be used as canon movement.
- Story-shopping checks and independent referees are campaign discipline, not
  public posture.
- Do not use these scripts, analyses, or logs to change claim status, canon,
  verdicts, public posture, paper status, proof status, or protected governance
  surfaces.

## Direct Analyses

| file | role | current shared outcome |
|---|---|---|
| `lega1_flipped_chiral_adjudication.py` | Leg A1 flipped-chiral adjudication against the GU source wording. | Keeps the flipped-chiral corner bounded by the source reading rather than closing the carrier fork. |
| `lega1_flipped_chiral_adjudication.md` | Narrative analysis for Leg A1. | Records the source-reading and representation-exact findings for the flipped-chiral corner. |
| `lega2_massless_bookkeeping.py` | Leg A2 massless bookkeeping and spin-3/2 mass-channel checks. | Refutes the filed census while preserving the stronger one-dial tension as an open corner. |
| `lega2_massless_bookkeeping.md` | Narrative analysis for Leg A2. | Records the corrected field-content census and the surviving mass/VEV tension. |
| `legb1_graded_ig_algebra.py` | Leg B1 graded inhomogeneous-gauge algebra certificate. | Verifies the odd extension shape and the carrier-A ghost-subtraction route under caveats. |
| `legb1_graded_ig_algebra.md` | Narrative analysis for Leg B1. | Records the graded-IG construction, caveats, and the open-toward-A reading. |
| `legb2_shadow_restriction.py` | Leg B2 shadow-restriction and deletion-mode bookkeeping. | Separates the toy carrier-A mechanism from self-falsifying whole-column gauging. |
| `legb2_shadow_restriction.md` | Narrative analysis for Leg B2. | Records the surviving shadow-restriction constraints and the SG4 dependence. |

## Corner Audits

| file | role | current shared outcome |
|---|---|---|
| `audit_a2_corner_open.py` | Corner-A2 open-case audit. | Keeps the massless/bookkeeping corner marked open rather than over-closed. |
| `audit_b2_corner_open.py` | Corner-B2 open-case audit. | Keeps the graded-IG door open-toward-A while preserving the caveats. |

## Independent Referees

| file | role | current shared outcome |
|---|---|---|
| `referee_A1_independent.py` | Independent flipped-chiral source and representation check. | Rechecks the A1 source-reading route through a separate path. |
| `referee_legA2_verify.py` | Independent Leg A2 massless bookkeeping verifier. | Rebuilds the corrected census and mass-channel constraint independently. |
| `referee_b1_indep.py` | Independent Leg B1 graded-IG algebra verifier. | Rechecks the forced-shape and ghost-subtraction arithmetic independently. |
| `referee_B2_independent.py` | Independent Leg B2 shadow-restriction verifier. | Rechecks the deletion-mode and carrier-space constraints independently. |

## Run Logs

| file | role | current shared outcome |
|---|---|---|
| `legb1_run_record.log` | Verified heavy B1 run record. | Records the successful long-running B1 certificate output. |
| `legb1_inrepo_run.log` | In-repo rerun note. | Records that a later in-repo rerun was intentionally terminated under the one-heavy-job rule and points back to the verified run record. |

## Process Gate

`process_gates/escape_corners_readme_inventory_audit.py` keeps this README
synchronized with the tracked direct scripts, analyses, and logs in this
directory and checks that the SG4 / no-status-movement boundary remains visible.
