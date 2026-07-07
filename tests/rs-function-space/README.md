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
python tests/rs-function-space/verify/rs_boundary_eta_indep_check.py
python tests/rs-function-space/verify/family_generation_arena_indep_check.py
```

## Honest Scope

- Computed certificates: RS index arithmetic, product-family sanity checks, full RS boundary eta parity,
  and currently honest family/characteristic numbers.
- Independent verification: boundary eta parity and generation-arena arithmetic have separate re-checks
  under `verify/`.
- Analytic boundary: the actual GU source action, GU K3-fibered family symbol, `ch2`/eta correction, and
  H-line normalization remain open. This directory records the boundary; it does not close the crux.
