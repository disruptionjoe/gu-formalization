# tests/generation-sector/

Generation-sector computational certificates. This is a frozen, paper-cited
surface: do not move these scripts and do not rename these scripts casually
because public papers, canon files, and reproduction docs cite these paths
directly.

These files are computational certificates, not claim-status updates. A green
run means the listed finite checks reproduce their current arithmetic and
guardrails. It does not derive the generation count, change verdicts, change
public posture, or bypass the source-action / integer-extraction gates.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick -k generation-sector --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick -k generation-sector --timeout 300
```

Run a single certificate directly when reviewing one claim:

```powershell
python tests\generation-sector\ghost_parity_krein.py
```

## Boundary

The public boundary stays:

- `LOCATE` stands only where a script explicitly supports it.
- `FORCE` is not earned by this directory alone.
- `3` remains gated on source-action and integer-extraction inputs not supplied
  by the current generation-sector finite checks.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

### Shared Bridge

| script | role | current shared outcome |
|---|---|---|
| `gen_sector_bridge.py` | Parent-local bridge for the migrated generation-sector audit tests. | Reproduces the Cl(9,5) representation anchors used by the step chain. |

### Paper-Cited Krein / Chirality Core

| script | role | current shared outcome |
|---|---|---|
| `ghost_parity_krein.py` | Krein signature and ghost-parity substrate. | The triplet sector remains vectorlike in the tested Krein structure. |
| `net_chiral_index_invariant.py` | Finite-dimensional net-chiral-index invariant. | Cross-chirality conservation keeps the current physical subspace index at zero. |
| `t1a_kinematic_chirality_kill.py` | Kinematic falsification test for ghost-parity chiralization. | Ghost parity is not enough to chiralize the triplet kinematically. |
| `swing_ghost_parity_chiral_selection.py` | Combined positivity-versus-chiral-selection swing. | Positivity consistency and chiral selection remain separated. |
| `h1_selfdual_family_kill.py` | Self-dual SU(2)+ family multiplicity test. | A native multiplicity-three object is located, but it is not a net-chiral count. |
| `a1_hypercharge_weighted_index.py` | Hypercharge-weighted index escape-hatch check. | Gauge-charge weighting does not rescue an odd invariant in the tested class. |
| `a2_kr_equivariant_index.py` | KR-equivariant refinement check. | No grading-odd Spin(10)-equivariant element is found in the tested triplet. |
| `a3_gsm_ghost_parity.py` | G_SM-only ghost-parity relaxation check. | The Dirac-form cross-chirality kill survives the relaxed equivariance test. |

### Signature / Selector Checks

| script | role | current shared outcome |
|---|---|---|
| `base_sign_selector_audit.py` | Bounded selector audit for the (9,5) versus (7,7) caveat. | The checked finite proxies do not select the base-sign convention. |
| `signature_77_rerun.py` | Direct (7,7) rerun of representative generation-sector checks. | The tested conclusion does not become a forced count under (7,7). |
| `signature_sweep_fast.py` | Fast signature sweep helper. | Keeps the signature-class arithmetic visible for review. |
| `signature_sweep_leg1.py` | Broader signature sweep over Cl(p,q), p+q=14. | Searches for signature-class routes that would break the multiplicity theorem. |

### Family / External-Base Characterization

| script | role | current shared outcome |
|---|---|---|
| `leg3_external_base_characterization.py` | External-base characterization for the firewall/location leg. | Locates where external base data could carry the count. |
| `leg3_family_embedding_enumeration.py` | SU(2) family embedding enumeration. | The odd family multiplicity is located in the triplet, not forced as a count. |
| `leg4_branching_multiplicity_search.py` | Branching-multiplicity break attempt. | Searches GU-native branching data for a forced generation multiplicity. |

### CONSTRUCT / Step Chain

| script | role | current shared outcome |
|---|---|---|
| `step1_c2_dirac_symbol.py` | C2 escape-symbol audit. | C2 is pinned as a first-order symbol norm in the tested bridge. |
| `step2_boundary_dirac.py` | Candidate boundary Dirac construction. | Builds the boundary operator and names the ellipticity wall. |
| `step3_spectral_section.py` | Spectral-section check for the boundary Dirac. | The tested operator has forced eta-zero symmetry. |
| `step4_mkt_vs_dirac_square.py` | BV/Koszul-Tate Hessian versus Dirac-square bridge. | The square-level bridge reproduces the expected relation. |
| `step5_synthesis.py` | Step-chain synthesis for SPEC 5(iii). | Records the honest negative: C2 lands as norm, not APS index. |
| `step6_grading_break_decision.py` | Grading-break go/no-go decision. | Distinguishes protected eta-zero from admissible breakers. |
| `step7_integer_freeness.py` | Degree-zero integer-freeness check. | Finds no honest scale-invariant integer 3 in the tested bridge data. |
| `step8_grading_flow_character.py` | Character of the revived index under breakers. | The value is connection-dependent, not forced by the representation alone. |
| `step9_selfdual_connection_index.py` | Geometric connection index test. | Metric so(9,5) connections do not force the desired odd count. |
| `step10_parity_gate_quaternionic_wall.py` | Corrected parity-gate check. | Odd is reachable by foreign carriers, so the wall is under-determination. |
| `step11_gu_native_parity_theorem.py` | GU-native parity theorem check. | GU-native Hermitian carriers remain even in the tested H-linear class. |

## Process Gate

`process_gates/generation_sector_readme_inventory_audit.py` keeps this README
synchronized with the live direct scripts in this directory and checks that the
frozen / not-verdict-changing boundary remains visible.
