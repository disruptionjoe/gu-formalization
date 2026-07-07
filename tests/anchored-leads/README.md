# tests/anchored-leads/

Anchored-lead candidate screens for routes that could appear to move the
generation-count problem from a located slot toward a forcing mechanism. These
scripts are computational or exact-arithmetic screens, not claim-status updates.
A green run keeps the candidate-screen evidence reproducible; it does not force
the generation count, change verdicts, change public posture, promote canon, or
bypass the source action gate.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick --tracked-only --list -k tests/anchored-leads
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/anchored-leads --timeout 300
```

Run a single screen directly when reviewing one lead:

```powershell
python tests\anchored-leads\jones_index_arena_indep_check.py
```

## Boundary

The public boundary stays:

- These scripts screen anchored leads; they do not establish a GU derivation.
- A located arithmetic or symmetry slot is not forced into a generation count.
- Candidate routes that survive a local check remain gated on missing structure
  such as the source action, pinned geometry, or external graph/symmetry data.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Candidate Screens

| script | role | current shared outcome |
|---|---|---|
| `jones_index_arena_indep_check.py` | Independent finite-type recheck for the Jones-index anchored lead. | GU-native finite Clifford and frame-split screens stay 2-primary; index `3` requires extra `A_5` graph structure. |
| `jones_subfactor_index_m64h.py` | Direct Jones/subfactor substrate screen on `Cl(9,5) = M(64,H)`. | Natural GU inclusions are type-I finite and produce power-of-two or graph-norm indices, not a forced generation count. |
| `km_n3_phase_and_reality_structure.py` | Kobayashi-Maskawa phase-count and reality-structure screen. | `n >= 3` is selector/cardinal arithmetic, while a forced real or quaternionic reality structure removes the CP phase. |
| `sm_z6_quotient_bridge.py` | SM global-form `Z_6 = Z/2 x Z/3` bridge test on the verified substrate. | The SM diagonal quotient remains gauge/internal and frame-trivial; it restates the CRT firewall rather than bridging it. |
| `spin8_triality_lefschetz.py` | Spin(8) triality / equivariant Lefschetz integer screen. | Internal triality has zero tangent-frame charge, and its Lefschetz integer is deformation-invariant, so it can relocate but not force. |
| `thooft_anomaly_matching_lever.py` | 't Hooft anomaly matching as a locate-to-force lever. | Matching is homogeneous in generation count; continuous anomalies vanish per generation and any discrete residue remains mod-3/gated. |
| `tmf_elliptic_genus_covary_screen.py` | tmf / elliptic-genus co-variation screen. | Co-varying elliptic-genus data is free-part/integer-valued, while degree-3 tmf torsion re-describes the homotopy-fixed carrier. |

## Process Gate

`process_gates/anchored_leads_readme_inventory_audit.py` keeps this README
synchronized with the live direct scripts in this directory and checks that the
candidate-screen / located-not-forced / source-action-gated boundary remains
visible.
