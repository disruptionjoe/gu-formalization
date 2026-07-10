# RS function-space certificate family

Executable certificates for the RS function-space family-index and boundary-eta scaffolds connected to
`canon/rs-function-space-framework-SPEC.md`.

These scripts do not derive a GU source action, do not prove that GU forces three generations, and do
not change any claim status, verdicts, or public posture. They keep the open crux explicit: the current
family-index and boundary-eta data remain 2-primary unless a future GU source action supplies a
target-import-free higher family term.

## Result Boundary

The recorded boundary is an open-crux / no-target-import boundary. The existing RS function-space
checks show that current bulk, family, and boundary data do not source an order-3 generation count by
themselves. The forbidden `chi(K3) / 8 = 3` shortcut is treated only as a control, not as evidence.

## Scripts

| script | role |
|---|---|
| `rs_index_harness.py` | Reusable exact-arithmetic RS index harness for spin 4-manifold checks and the bulk 2-primary boundary. |
| `k3_family_pushforward_scaffold.py` | K3 family-index scaffold separating the computed product-family sanity check from the unbuilt higher family term. |
| `rs_boundary_eta_l21.py` | Full RS boundary eta check on `RP^3 = L(2;1)`, showing the sector's own boundary channel remains 2-primary. |
| `family_generation_arena_probe.py` | Generation-arena probe showing the currently honest family/characteristic numbers remain in the 2-primary arena. |
| `families_e_invariant_order3_monodromy.py` | Exact Z/24 and Z/3 families e-invariant probe for order-3 K3 monodromy, preserving the located-not-forced / source-action-gated boundary. |
| `order3-rho/leg1_calibration.py` | Calibration leg for the order-3 equivariant rho build: lattice, G-signature, quotient-resolution, and RS convention gates. |
| `order3-rho/leg2_dirac_rho.py` | Exact Dirac rho computation for the order-3 Nikulin monodromy mapping torus. |
| `order3-rho/leg3_rs_rho.py` | Exact Rarita-Schwinger rho computation under the canon-pinned RS convention. |
| `order3-rho/leg4_arena.py` | Arena and firewall audit mapping the order-3 rho values into the Z/24 and Z/3 readout. |
| `order3-rho/referee_leg1.py` | Independent hostile-referee recheck of the calibration leg with exact cyclotomic arithmetic. |
| `order3-rho/referee_leg2.py` | Independent hostile-referee recheck of the Dirac rho leg across spin and character conventions. |
| `order3-rho/referee_leg3.py` | Independent hostile-referee recheck of the RS rho leg and rival convention gates. |
| `order3-rho/referee_leg4.py` | Independent hostile-referee recheck of the arena/firewall reading. |
| `rho-38-adjudication/legA_symbol_homotopy.py` | Symbol-level adjudication of the pinned `-42` versus geometric `-38` RS conventions: ellipticity, additivity, and equivariance gates. |
| `rho-38-adjudication/legB_index_bookkeeping.py` | Exact K3 index bookkeeping for the ghost-subtracted and geometric gamma-traceless RS conventions. |
| `rho-38-adjudication/legC_equivariant_rho.py` | Equivariant rho computation for the geometric gamma-traceless RS operator, compared against the pinned convention. |
| `rho-38-adjudication/legD_identification.py` | Identification ledger for where the order-3 class lives in the RS convention fork and what remains blocked. |
| `rho-38-adjudication/referee_legA.py` | Independent hostile-referee recheck of the symbol homotopy and equivariance leg with different Clifford machinery. |
| `rho-38-adjudication/referee_legB.py` | Independent hostile-referee recheck of the index bookkeeping leg via Dolbeault/Hodge and Lefschetz routes. |
| `rho-38-adjudication/referee_legC.py` | Independent hostile-referee recheck of the geometric RS equivariant rho leg with different exact-arithmetic machinery. |
| `rho-38-adjudication/referee_legD.py` | Independent hostile-referee recheck of the identification leg, including kernel phases and class-law controls. |
| `verify/rs_boundary_eta_indep_check.py` | Independent re-check of the RS boundary eta result using rotated frame bases and a fiber similarity. |
| `verify/family_generation_arena_indep_check.py` | Independent re-derivation of the family generation-arena arithmetic without importing the main probe. |

## Running

From the repo root, run the central harness:

```powershell
python scripts/reproduce_all.py --quick -k rs-function-space
```

For targeted review, run the direct and independent checks:

```powershell
python tests/rs-function-space/rs_index_harness.py
python tests/rs-function-space/k3_family_pushforward_scaffold.py
python tests/rs-function-space/rs_boundary_eta_l21.py
python tests/rs-function-space/family_generation_arena_probe.py
python tests/rs-function-space/families_e_invariant_order3_monodromy.py
python tests/rs-function-space/order3-rho/leg1_calibration.py
python tests/rs-function-space/order3-rho/leg2_dirac_rho.py
python tests/rs-function-space/order3-rho/leg3_rs_rho.py
python tests/rs-function-space/order3-rho/leg4_arena.py
python tests/rs-function-space/order3-rho/referee_leg1.py
python tests/rs-function-space/order3-rho/referee_leg2.py
python tests/rs-function-space/order3-rho/referee_leg3.py
python tests/rs-function-space/order3-rho/referee_leg4.py
python tests/rs-function-space/rho-38-adjudication/legA_symbol_homotopy.py
python tests/rs-function-space/rho-38-adjudication/legB_index_bookkeeping.py
python tests/rs-function-space/rho-38-adjudication/legC_equivariant_rho.py
python tests/rs-function-space/rho-38-adjudication/legD_identification.py
python tests/rs-function-space/rho-38-adjudication/referee_legA.py
python tests/rs-function-space/rho-38-adjudication/referee_legB.py
python tests/rs-function-space/rho-38-adjudication/referee_legC.py
python tests/rs-function-space/rho-38-adjudication/referee_legD.py
python tests/rs-function-space/verify/rs_boundary_eta_indep_check.py
python tests/rs-function-space/verify/family_generation_arena_indep_check.py
```

## Honest Scope

- Computed certificates: RS index arithmetic, product-family sanity checks, full RS boundary eta parity,
  currently honest family/characteristic numbers, the order-3 monodromy families e-invariant probe, and the
  order-3 equivariant rho build plus the geometric `-38` RS adjudication suite with independent referee legs.
- Independent verification: boundary eta parity and generation-arena arithmetic have separate re-checks
  under `verify/`; the order-3 rho build has leg-local hostile-referee checks under `order3-rho/`, and
  the geometric `-38` adjudication has leg-local hostile-referee checks under `rho-38-adjudication/`.
- Analytic boundary: the actual GU source action, GU K3-fibered family symbol, `ch2`/eta correction, and
  H-line normalization remain open. This directory records the boundary; it does not close the crux.
