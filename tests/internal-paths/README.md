# tests/internal-paths/

Internal-path computational certificates from the 2026-07-03 follow-up attacks.
These scripts turn four named residual questions into runnable checks. They are
target-free and bounded, but they are not claim-status updates. A green run means
the listed certificates reproduce their current internal-path arithmetic and
guards; it does not force a generation count, close the source action wall,
change verdicts, change public posture, or promote canon.

## Running This Family

List the tracked certificates:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/internal-paths --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/internal-paths --timeout 300
```

Run a single certificate directly when reviewing one residual question:

```powershell
python tests\internal-paths\oq_rk1_indh_rank.py
```

## Boundary

The public boundary stays:

- These checks are internal-path witnesses and partial closures, not a verdict
  change for GU or for the generation-count question.
- The source action wall remains open; these scripts name what is gated rather
  than supplying the missing source action.
- The non-compact, APS, and 2-primary conclusions retain the grades stated in
  the corresponding exploration notes.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

| script | role | current shared outcome |
|---|---|---|
| `oq_rk1_indh_rank.py` | Re-runs the OQ-RK1 rank test for `Pi_RS . E_+ . Pi_RS` on the actual Cl(9,5) vector-spinor carrier using an independent gamma realization. | Reports the target-free rank of the effective RS projection and keeps the quaternionic-halving certificate executable. |
| `y14_bundle_index.py` | Splits the true RS/Y14 bundle family-index problem into spin-precondition, bulk, compact-core eta, cross-chirality, and noncompact fiber terms. | The computable pieces are separated from the definite vertical fiber Dirac term, which stays gated on the unbuilt source action. |
| `oc1_oc2_witness.py` | Builds a finite Callias/Jackiw-Rebbi witness for the non-compact signed-readout OC1/OC2 reduction. | Exhibits the Fredholm-at-infinity and quaternionic-symmetry mechanism without proving the genuinely non-compact operator case. |
| `anomaly_sp64.py` | Runs the odd-prime AHSS screen for the Sp-family global anomaly leg and recomputes the conditional local leg. | Shows the global odd-primary part is clean while the 2-primary channel and assumed chiral content remain the decisive gates. |

## Process Gate

`process_gates/internal_paths_readme_inventory_audit.py` keeps this README
synchronized with the tracked direct scripts in this directory and checks that
the internal-path / source-action-gated / not-forced boundary remains visible.
