# tests/hessian-z3/

Hessian/Z3 carrier-occupancy computational certificates. These scripts are
finite proxy checks, not claim-status updates. A green run means the listed
certificates reproduce their current Hessian, occupancy, torsion, and mechanism
arithmetic; it does not derive a generation count, force three, change verdicts,
change public posture, or bypass the source action gate.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick -k hessian-z3 --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick -k hessian-z3 --timeout 300
```

Run a single certificate directly when reviewing one claim:

```powershell
python tests\hessian-z3\carrier_occupancy_hessian.py
```

## Boundary

The public boundary stays:

- These checks use finite proxy substrates for the action quadratic part.
- The vectorlike carrier-occupancy direction is tested as a flat/null direction,
  not as an independently forced generation count.
- The source action and integer-extraction inputs remain action-gated and are not
  supplied by this directory alone.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

### Core Occupancy And Proxy Checks

| script | role | current shared outcome |
|---|---|---|
| `carrier_occupancy_hessian.py` | Computes the carrier-occupancy Hessian Rayleigh quotient on the vectorlike Cl(9,5) carrier proxy. | The balanced occupancy direction is numerically flat/null while purely chiral occupations are curved. |
| `offdiag_meanfield_coupling.py` | Computes selector-to-carrier off-diagonal mean-field coupling across proxy quadratic forms. | The tested off-diagonal coupling remains decoupled in the current finite proxy setup. |
| `cross_proxy_carrier_hessian.py` | Compares carrier-direction diagonal and off-diagonal Hessian readouts across Krein, Seiberg-Witten, and boundary-eta proxies. | The vectorlike zero survives the tested proxy sweep while the full source action remains unbuilt. |
| `criticality_torsion_lambda_epsilon.py` | Perturbs the carrier/selector setup by torsion-like epsilon deformations and tracks the Hessian readout slope. | The current GU-structured torsion test keeps the net readout protected at first order. |

### Adversarial Rechecks

| script | role | current shared outcome |
|---|---|---|
| `adversarial_recheck_occupancy.py` | Re-derives the occupancy-reflection claims and stress-tests the null-direction interpretation. | Occupancy flatness is distinguished from a kernel zero mode and remains gated on the proxy action form. |
| `adversarial_verify_eigenvalue.py` | Checks whether the reported eigenvalue-zero is a real null direction or a hidden zero eigenvalue across proxies. | The checked zero is a vectorlike cancellation/null-direction reading, not a literal kernel claim. |
| `adv_refute_flatdir_curvature.py` | Tracks the actual occupancy direction under curvature/torsion variation rather than averaging the whole spectrum. | The script separates trace-mean artifacts from movement of the tested flat direction. |

### Mechanism And Robustness

| script | role | current shared outcome |
|---|---|---|
| `mechanism_offdiagonal_check.py` | Decomposes the torsion action into generation/mirror blocks and checks the decisive block trace. | GU-structured torsion is block-diagonal and traceless on the tested carrier split; generic torsion moves the mean. |
| `robustness_and_mechanism.py` | Sweeps structured and generic torsion seeds to test robustness of the protected-slope reading. | The structured case stays protected across the tested seeds while generic deformations are critical. |

## Process Gate

`process_gates/hessian_z3_readme_inventory_audit.py` keeps this README
synchronized with the live direct scripts in this directory and checks that the
proxy / action-gated / not forced boundary remains visible.
