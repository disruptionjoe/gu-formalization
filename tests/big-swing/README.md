# tests/big-swing/

Big-swing certificates for adversarial research packets that attack the generation-count, boundary,
framed-bordism, mirror-sector, and capability-wall leads. These files are computational or Lean
certificates paired with exploration notes, not claim-status updates. A green run keeps the packet
reproducible; it does not derive GU, force the generation count, change verdicts, change public
posture, or supply the missing source action.

## Running This Family

List the Python certificates discovered by the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only --list -k tests/big-swing
```

Run the Python certificates through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/big-swing --timeout 300
```

Run a single certificate directly when reviewing one packet:

```powershell
python tests\big-swing\rs_s4_base_forcing_bismut_cheeger.py
```

The Lean certificate is checked separately with the provisioned Lean toolchain:

```powershell
lake env lean tests\big-swing\R4_TwoArena.lean
```

## Boundary

The public boundary stays:

- These files are big-swing exploration certificates and packet checks; they do not establish a GU
  derivation or move claim status.
- A located carrier, arithmetic slot, mirror sector, framed-bordism lead, or capability-wall contact
  is not a forced generation count.
- Surviving candidates remain gated on named missing structure such as the source action, a proven
  boundary reduction, pinned external data, or an independently checked formalization.
- Do not use these scripts to change canon, claim status, verdicts, public posture, paper status, or
  protected governance surfaces. This family is a not-a-verdict-change reproducibility map.

## Direct Certificate Files

| script | packet | role |
|---|---|---|
| `as_a1_native_potential_alignment.py` | alignment phase | Native-potential alignment screen for the phase-not-tuning packet. |
| `as_a1b_reduced_phase_confirm.py` | alignment phase | Reduced-phase confirmation check for the alignment packet. |
| `as_a2b_native_ring_symmetry_nogo.py` | alignment phase | Native ring-symmetry no-go check. |
| `as_a3_orientation_z2.py` | alignment phase | Orientation / Z2 branch screen. |
| `as_a4_basin_stability.py` | alignment phase | Basin-stability check for the alignment packet. |
| `c07_kramers_regression.py` | C-07 wall | Regression guard for the quaternionic Kramers parity wall. |
| `cg_r1_pu_pt_vs_ghost_parity.py` | conformal / ghost | PU/PT versus ghost-parity carrier screen. |
| `cg_r3_pt_phase_gu_cores.py` | conformal / ghost | PT-phase screen on GU core objects. |
| `cg_r4_conformal_fiber_obstruction.py` | conformal / ghost | Conformal-fiber obstruction check. |
| `fb_f1_twisted_operator_build.py` | framed bordism | Twisted-operator build attempt for the framed-bordism packet. |
| `fb_f2_adams_einvariant_obstruction.py` | framed bordism | Adams e-invariant obstruction check. |
| `fb_f3_crt_split_on_carrier.py` | framed bordism | CRT split screen on the carrier. |
| `fb_f4_imageofJ_fractional_and_imports.py` | framed bordism | Image-of-J fractional/import boundary check. |
| `mp_m1_mirror_quantum_numbers.py` | mirror predictions | Mirror-sector quantum-number screen. |
| `mp_m2_dark_vs_visible.py` | mirror predictions | Dark-versus-visible sector distinction check. |
| `mp_m3_count_and_anomaly.py` | mirror predictions | Count/anomaly consistency screen. |
| `mp_m4_mass_texture_sign_bit.py` | mirror predictions | Mass-texture sign-bit screen. |
| `R1_actual_rs_operator_residual.py` | 2026-07-03 big swing | Actual RS-operator residual check. |
| `R1_kill_odd_index_isotypic.py` | 2026-07-03 big swing | Odd-index isotypic route kill check. |
| `R2_lens_dai_freed_eta.py` | 2026-07-03 big swing | Lens-space Dai-Freed eta check. |
| `R2_spin_bordism_mod3.py` | 2026-07-03 big swing | Spin-bordism mod-3 arena check. |
| `R3_signed_readout_certificate.py` | 2026-07-03 big swing | Signed-readout certificate. |
| `R4_crt_two_arena.py` | 2026-07-03 big swing | CRT two-arena Python certificate. |
| `R4_spin95_hom_vanishing.py` | 2026-07-03 big swing | Spin(9,5) Hom-vanishing certificate. |
| `R4_TwoArena.lean` | 2026-07-03 big swing | Lean certificate for the two-arena packet. |
| `R5_chiral_tie_nogo.py` | 2026-07-03 big swing | Chiral-tie no-go check. |
| `R5_crosscheck_bilinear.py` | 2026-07-03 big swing | Bilinear cross-check for the R5 packet. |
| `R5_theta_signed_readout.py` | 2026-07-03 big swing | Theta signed-readout check. |
| `rs_s1_relative_index_construct.py` | RS index gated | Relative-index construction attempt. |
| `rs_s2_relative_index_nogo.py` | RS index gated | Relative-index no-go check. |
| `rs_s3_double_duty_base_selection.py` | RS index gated | Double-duty base-selection check. |
| `rs_s4_base_forcing_bismut_cheeger.py` | RS index gated | Bismut-Cheeger base-forcing gate. |
| `t12p_mirror_capability_wall.py` | capability wall | T12 prime mirror capability-wall certificate. |
| `vg_sa_mannheim_source_arithmetic.py` | verification gates | Mannheim source-arithmetic check. |
| `vg_sd_math_flag_clearance.py` | verification gates | Math-flag clearance guard for public posture. |
| `vg_v1_condensate_parity_scan.py` | verification gates | Condensate parity scan. |
| `vg_v2_fourth_seat_gauge_indefiniteness.py` | verification gates | Fourth-seat gauge-indefiniteness screen. |
| `vg_v3_j_commutant_conformal_native.py` | verification gates | J-commutant conformal-native screen. |
| `vg_v4_quantize_break_commuting_square.py` | verification gates | Quantized commuting-square break attempt. |
| `vg_v5_breaking_coset_topology.py` | verification gates | Breaking-coset topology screen. |
| `vg_v6_conformal_constrained_scatter.py` | verification gates | Conformal constrained-scatter check. |
| `vg_v7_cp2_equivariant_payoff.py` | verification gates | CP2 equivariant-payoff check. |
| `vg_v8_t5_map_attempt.py` | verification gates | T5 map-attempt check. |
| `sg1_signature_carrier_parity_77.py` | sequential-goals 2026-07-09 | Both-signature control: C-07 quaternionic-parity no-go on (9,5) vs (7,7)=M(128,R). |
| `sg2_price_sigma_mod3_import.py` | sequential-goals 2026-07-09 | Prices the 3\|sigma external import (Rokhlin lattice + realizability). |
| `sg3_s2_mod3_tautology_audit.py` | sequential-goals 2026-07-09 | Audits S2's mod-3 tautology; derives the residue + supplies a discriminating test. |
| `sg4_source_action_candidate_classifier.py` | sequential-goals 2026-07-09 | Boundary-supply-ledger candidate packet + executable taxonomy classifier. |
| `sg5_import_channel_independence.py` | sequential-goals 2026-07-09 | Three disjoint homes for the prime 3; import-channel independence. |

## Process Gate

`process_gates/big_swing_readme_inventory_audit.py` keeps this README synchronized with
the live direct certificate files in this directory and checks that the exploration /
not-a-verdict-change / source-action-gated boundary remains visible.
