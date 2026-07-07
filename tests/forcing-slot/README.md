# tests/forcing-slot/

Forcing-slot computational certificates for the toy stabilized-source screen.
These scripts are computational certificates, not claim-status updates. A green
run means the listed finite checks reproduce their current forcing-slot
arithmetic and guardrails. It does not derive GU, force the generation count,
change verdicts, change public posture, or supply the missing source action.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k forcing-slot --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k forcing-slot --timeout 300
```

Run a single certificate directly when reviewing one claim:

```powershell
python tests\forcing-slot\rs_frame_index_operator.py
```

## Boundary

The public boundary stays:

- The forcing-slot screen is a toy stabilized-source test surface, not a
  full GU source-action construction.
- A successful check may preserve frame charge, net chirality, or arena
  arithmetic for the tested proxy, but it is not-a-GU-derivation and
  not-a-verdict-change.
- The missing source action and integer-extraction step remain gated.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

| script | role | current shared outcome |
|---|---|---|
| `adv_verify_brst.py` | Independent adversarial recheck of the BRST / Faddeev-Popov forcing-slot claim. | Rebuilds the gauge/ghost checks from scratch and preserves the frame-trivial / vectorlike boundary. |
| `adv_verify_rs_independent.py` | Independent adversarial recheck of the RS frame-index claim. | Distinguishes projector-trace tautology from legitimate net chirality and hunts for disguised `3` or `24` imports. |
| `agw_gravitino_3primary.py` | Exact Alvarez-Gaume-Witten spin-3/2 anomaly coefficient scan. | Tests whether the RS anomaly polynomial reaches the order-3 arena without fitted arithmetic. |
| `brst_fp_stabilization_sector.py` | BRST / Faddeev-Popov stabilization-sector construction on the verified substrate. | Measures frame triviality, ghost subtraction, and vectorlikeness for the RS redundancy sector. |
| `rs_frame_index_operator.py` | RS frame-index operator on the verified Cl(9,5) substrate. | Tests whether frame charge and net chirality appear simultaneously in the untwisted and chiral-16-twisted cases. |
| `rs_index_carrier_arena_scan.py` | Multi-manifold CRT scan for the RS / spin-3/2 index. | Checks whether concrete RS index integers land nontrivially in the Z/3 carrier arena. |
| `rs_net_chiral_decomposition.py` | Forward decomposition of the RS twisted net-chiral integer. | Anchors the `+256` integer and checks whether twist or chirality choices manufacture a factor of 3. |
| `twisted_spin32_index_k3.py` | Exact K3 spin-3/2 index calculation twisted by the chiral 16. | Separates K3 controls from disguised chi input and tests whether the resulting integer is 3-primary or 2-primary. |

## Process Gate

`process_gates/forcing_slot_readme_inventory_audit.py` keeps this README
synchronized with the live direct scripts in this directory and checks that the
toy-model / not-a-GU-derivation / not-a-verdict-change boundary remains visible.
