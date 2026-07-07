# tests/source-action/

Source-action computational certificates for the Seiberg-Witten / moment-map
construction surface. This is a frozen, paper-adjacent test family: do not move
or rename these scripts casually because the public reproduction map and
source-action wall references depend on these paths.

These files are computational certificates and stress tests, not claim-status
updates. A green run means the listed finite checks reproduce their current
source-action arithmetic and guardrails. It does not derive the generation
count, change verdicts, change public posture, or bypass the source action /
integer-extraction gates.

## Running This Family

List the tracked certificates:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/source-action --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/source-action --timeout 300
```

Run a single certificate directly when reviewing one claim:

```powershell
python tests\source-action\foundation_moment_map.py
```

## Boundary

The public boundary stays:

- This directory maps and runs the current source-action construction checks.
- It does not close the source-action wall by itself.
- It does not supply a GU-forced generation count or an integer-extraction
  verdict.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

### Moment-Map Construction

| script | role | review note |
|---|---|---|
| `foundation_moment_map.py` | Checks the SU(2)+-equivariant quadratic moment-map substrate. | Keeps the basic moment-map existence and equivariance questions executable. |
| `sw_moment_map_cl95.py` | Tests the Cl(9,5) Seiberg-Witten moment-map angle. | Keeps the local monopole-equation construction visible as a finite certificate. |
| `moment_map_noether_closure.py` | Checks Noether-closure premises for the moment-map sector. | Separates finite substrate checks from base-manifold Noether identities. |
| `full_lambda2_doubling_check.py` | Tests the full Lambda^2 doubling after the self-dual-only route is challenged. | Keeps the self-dual and anti-self-dual legs reviewable together. |

### Discharge And Consistency Gates

| script | role | review note |
|---|---|---|
| `verify_A_dark_energy.py` | Verifies the finite substrate part of the dark-energy / Noether-II discharge. | Leaves base differential identities at their stated grade. |
| `verify_B_middle_map.py` | Checks middle-map closure and selection on the Seiberg-Witten shell. | Reports whether on-shell restriction reduces the obstruction rather than assuming it. |
| `seesaw_majorana_mu_block.py` | Tests whether the moment map supplies a chirality-preserving Majorana block. | Distinguishes a usable seesaw block from vectorlike or non-forcing behavior. |
| `verify_C_seesaw.py` | Assembles the folded seesaw operator and reads its eigenvalue structure. | Tests hierarchy behavior directly instead of inferring it from block norms. |
| `verify_D_consistency.py` | Runs the D-gate consistency checks for the doubled source action. | Keeps Krein compatibility, scale/integer mismatch, and Velo-Zwanziger proxy limits explicit. |

### Adversarial Stress Checks

| script | role | review note |
|---|---|---|
| `sw_bv_master_equation_c2.py` | Tests whether the SW-sourced compensator closes the BV/BRST C2 obstruction. | Preserves the anti-trap that RS coupling must not be silently decoupled. |
| `synth_B1_onshell_leakage.py` | Measures on-shell leakage for the SW j=1 carrier. | Keeps the B1 obstruction comparison executable as a finite stress check. |

## Process Gate

`process_gates/source_action_readme_inventory_audit.py` keeps this README
synchronized with the tracked direct scripts in this directory and checks that
the frozen / source-action-wall / not-a-verdict-change boundary remains visible.
