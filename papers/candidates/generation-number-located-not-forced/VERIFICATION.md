# Verification Map: "The Generation Number is Located, Not Forced"

Every quantitative claim in the paper draft ties to a named deterministic test in `tests/` (repo root).
All tests are pure Python (exact integer / rational arithmetic, no RNG, no network); exit 0 = every assert
passed. Last full re-run: **2026-07-13**, all six exit 0.

| Test | Exit (2026-07-13) | What it certifies (and nothing more) |
|---|---|---|
| `tests/W55_path3_A_index.py` | 0 | Branch A (index). Integer Dirac/RS index on closed spin 4-manifolds is `0 mod 3` via `p_1 = 3 sigma` (constrains, does not force); `Hom(Z/3, Z) = 0` kills any torsion-free integer index for the mod-3 count; KO-torsion is all 2-primary (no escape); mod-3k Freed-Melrose and the R/Z reduced-eta / Adams e-invariant (`e_KO(8nu) = 1/3`, order 3) REACH the `Z/3` arena but return a class, not the integer 3. |
| `tests/W56_path3_B_anomaly_inflow.py` | 0 | Branch B (inflow). Nielsen-Ninomiya closed-side zero; wall count = winding number, Z-quantized but value free (w = 1, 2, 3 all realized); bulk level k free in Z; the one forced consistency condition (anomaly-freedom) is 2-primary parity, all residues mod 3 reachable; `Hom(Z/3, Z) = 0` no-go for the standard inflow invariant. |
| `tests/W57_path3_C_cobordism.py` | 0 | Branch C (cobordism). `pi_3^s = Z/24 = Z/8 (+) Z/3` (Toda / Adams, `|im J_3| = den(B_2/4) = 24`); modulus 3 forced (order of the 3-Sylow), value not (Aut(Z/3) = Z/2, no canonical generator); Dai-Freed anomaly is a homomorphism, so N generations scale linearly and the SM per-generation anomaly vanishing makes anomaly cancellation generation-blind; `Hom(Z/3, Z) = 0` (no Z-lift). |
| `tests/W58_path3_D_homotopy_torsion.py` | 0 | Branch D (torsion, the reachable construction). `3 = dim Lambda^2_+(R^4)` two independent ways; `Z/3 subset pi_3^s` three independent ways (Bernoulli denominator, von Staudt-Clausen, Adams alpha-family degree); order-3 action on `R^3` splits fixed axis (1) + rotated pair (2); invariant subspace dims exactly `{0,1,2,3}`; odd invariant ranks exactly `{1,3}`; no order-3 class function separates rank 3 from the trivial sector; promotion `Z/3 -> SO(3)` (irreducibility) is the minimal input that forces 3. |
| `tests/W59_path3_E_nogo.py` | 0 | Branch E (the no-go theorem). Leg 1: `Hom(Z/3, Z) = 0`, `Hom(Z/3, Z/2^k) = 0` (unreachable constructions). Leg 2: class-to-integer gap (a torsion class has no canonical integer value) + the `{1,3}` residual (rank 1 admissible whenever rank 3 is; equivariance, reality, oddness, self-adjointness do not separate them). Steelman encoded: faithfulness/maximality + oddness DOES force 3, and faithfulness is certified NOT first-principles (the sterile axis is consistent and anomaly-free). |
| `tests/W60_path3_wave2_su2plus.py` | 0 | Wave 2 (the SU(2)+ reduction). D1: `Rep(SU(2))` has irreps of every dimension; gauging never forces adjoint matter; Schur forces rank 3 only GIVEN C1 (generation multiplet = the equivariant adjoint bundle `Lambda^2_+`): answer-as-premise. D2: the sterile singlet survives gauging (anomaly-free; mod-3 Dai-Freed arena empty); the rank-1 axis is relocated to an external singlet, not forbidden. Explicit asserts: discrete invariant dims `{0,1,2,3}` vs continuous `{0,3}`; odd SU(2)+ options `{1,3}`; C1 unsupplied; super-IG crack UNESTABLISHED (`super_ig_ties_family_to_spin_connection_PROVEN is False`). |

## Claim-by-claim index

- **Abstract / Result 1 (class-wide no-go):** W55 + W56 + W57 + W58 (each branch's forces-vs-locates verdict) closed into the theorem by W59.
- **Result 2 (forced content: 3-primary, ceiling `3 = dim Lambda^2_+`, count in `{1,3}`):** W57 (modulus), W58 (ceiling + odd ranks), W59 (residual `{1,3}` certified minimal).
- **Result 3 (SU(2)+ reduction; forcing 3 equivalent to C1):** W60 (both derivations, required to agree, agree).
- **"Sterile 1-generation solution is anomaly-free and admissible":** W59 (steelman block) + W60 (D2).
- **"Generation-blind SM Dai-Freed anomaly":** W57 encodes the homomorphism argument; the underlying group computation is CITED prior art (Davighi-Gripaios-Lohitsiri arXiv:1910.11277; Garcia-Etxebarria-Montero arXiv:1808.00009; Wan-Wang arXiv:1910.14668), not certified in-repo.

## Imported premises (dependencies the tests do NOT re-derive)

1. **Oddness of the net-chirality datum** (used to cut `{0,1,2,3}` to `{1,3}`): imported from the prior program leg (H37 / wave16-17). Without it the forced content is the 3-primary + ceiling statement only. Stated in the paper (Section 4 scope note).
2. **`Omega^Spin_5(BG_SM) (x) Z_(3) = 0`** (the empty mod-3 Dai-Freed arena): corollary of published computations (see above), taken as input by W59/W60.
3. **The physics-facing identification** of "the generation count" with the torsion datum in a given framework: reconstruction grade, argued not proven (paper Section 6).

## Reproduce

```
cd tests
python W55_path3_A_index.py && python W56_path3_B_anomaly_inflow.py && \
python W57_path3_C_cobordism.py && python W58_path3_D_homotopy_torsion.py && \
python W59_path3_E_nogo.py && python W60_path3_wave2_su2plus.py
```

Exit 0 on each = all claims above re-certified. No external dependencies beyond the Python standard library.
