# tests/carrier-mass/

Carrier-mass computational certificates for the vectorlike triplet carrier. These
scripts are computational certificates, not claim-status updates. A green run
means the listed finite checks reproduce their current carrier-mass arithmetic
and honesty boundary; it does not change verdicts, public posture, canon, paper
status, or the source action gate.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick -k carrier-mass --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick -k carrier-mass --timeout 300
```

Run a single certificate directly when reviewing one claim:

```powershell
python tests\carrier-mass\carrier_dirac_mass_allowed_or_forbidden.py
```

## Boundary

The public boundary stays:

- The carrier remains vectorlike in these checks.
- A mass term decouples the tested light sector to zero, not three.
- A forced light chiral count remains action-gated on the missing source action
  and chiral projection input.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates And Output

| file | role | current shared outcome |
|---|---|---|
| `carrier_dirac_mass_allowed_or_forbidden.py` | Tests whether GU-native symmetries forbid or admit a carrier Dirac mass. | No tested GU-native symmetry supplies a forced chiral protection of three. |
| `decoupling_to_zero_not_three.py` | Sweeps massive and massless carrier cases for light-sector net chirality. | Massive cases decouple to net zero; massless case stays vectorlike. |
| `verify_decoupling_independent.py` | Independent adversarial recheck of the decoupling sweep. | Reconfirms vectorlike index conservation and no net-three light sector. |
| `chiral_projection_requirement.py` | Computes what a chiral projection would need to supply. | The required selector-side chiralizer is frame-trivial and not the tangential order-3 carrier. |
| `sw_action_carrier_mass.py` | Tests the built Seiberg-Witten proxy mass structure on the carrier. | The proxy realizes nonzero, vectorlike carrier mass structure; the actual value remains action-gated. |
| `verify_sw_carrier_mass_independent.py` | Independent recheck of the Seiberg-Witten proxy mass claims. | Rechecks vectorlike grading, nonzero proxy mass scans, and the chiralizer split. |
| `decoupling_results.json` | Recorded output from the decoupling sweep. | Documents the current vectorlike, zero-not-three sweep result for review. |

## Process Gate

`process_gates/carrier_mass_readme_inventory_audit.py` keeps this README
synchronized with the live direct scripts and JSON output in this directory and
checks that the not-forced / action-gated boundary remains visible.
