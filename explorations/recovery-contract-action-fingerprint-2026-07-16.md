---
title: "Recovery contract action fingerprint"
status: exploration
doc_type: recovery_contract_checkpoint
created: 2026-07-16
run_id: GUH-20260716T061100Z-action-fingerprint
fingerprint: lab/process/recovery-contract-action-fingerprint-2026-07-16.json
gate: process_gates/recovery_contract_action_fingerprint_audit.py
---

# Recovery contract action fingerprint

Operational result: `CONDITIONAL`.

The W203/W229/W230/W236 family can be stated as one branch-local testing object, but only with its
posit and residues visible. The object is the record-current induced-YM branch-3 action:

```text
W203 ultralocal record-current bridge
-> W229 nonlocal induced-YM / Z_U completion
-> W230 W154 / c_kin = 0 posit boundary
-> W236 imported-Schwarzschild theta-sector clearance under that boundary
```

This is enough to support branch-local recovery tests that explicitly consume this action, source law,
variation space, and free-quantity ledger. It is not a primary theory freeze. The sector combination
remains `UNDERDEFINED` outside this branch until later tests prove that quantum, Standard Model,
gravity, cosmology, and any prediction claim consume the same fingerprint without retuning.
Short form: sector combination remains `UNDERDEFINED` for recovery-grade claims.

No claim status, canon verdict, public posture, paper surface, or portfolio surface changed.

## Construction Fork

The construction side used here is GU-native for the load-bearing objects: `Y14 = Met(X4)`, the
DeWitt/gimmel metric-on-metrics, the Krein `eta` pairing, the record current `J[Psi]`, and the
connection-distortion/source-action family. The standard-field side is used only as machinery or
comparator: Legendre elimination, screened-Poisson Green's functions, and imported Schwarzschild.

The fingerprint uses the record-current construction for `theta`. The alternative bare geometric
distortion, independent of `Psi`, is not varied inside this branch. That is exactly the W154 /
`c_kin = 0` posit boundary: W230 shows that `theta = J[Psi]` is a necessary named assumption, not a
symmetry theorem.

## Fingerprint

| component | branch-local statement | boundary |
|---|---|---|
| action family | `Re<Psi, K_S c(A) Psi> + (1/(2 kappa))<theta, eta theta> - <theta,J[Psi]>`, plus W229's first-order `P_IG` parent and induced gradient sector `-(Z_U/2)<D_A U,D_A U>` | Not a source-closed primary theory; one action branch only. |
| source law | `(-Z_U D_A*D_A + c_theta eta) theta = J[Psi]`, with `c_theta = 1/kappa` | Conditional on the W154 / `c_kin = 0` posit. |
| variation space | Vary `P_IG`, `theta/U`, and `A` inside the record-sourced induced-YM branch | Do not add a bare `theta`, a fundamental `c_kin > 0` branch, or sector-specific retuning. |
| forced pieces | `eta` kernel shape, source coupling once W154 is granted, differential part `D_A`, and `Psi=0 => J=0` | Forced in shape, not full native normalization. |
| free or unbuilt pieces | `kappa`, `Z_U`, eta-from-gimmel-area bridge, K_IG algebraic residue, interacting C-operator sign condition | Must be carried into every downstream test. |
| allowed reductions | W229 reduces to W203 for `Z_U -> 0` or zero-mode source; W236 gives `J=0`, `theta=0`, `E_s^theta=0` on imported Schwarzschild vacuum | These are branch-local reductions, not exact GR recovery. |

## Result

The action/source/variation conflict does not block branch-local tests. The correct status is
`CONDITIONAL`, not `UNDERDEFINED`: one coherent testing object can be named.

The conflict still blocks recovery-grade sector combination. The open boundaries are:

- `PRIMARY-ACTION-VARIANTS`: one operator spine and several action/IG branches remain broader than this
  fingerprint.
- `W154_SOURCE_IDENTIFICATION`: `theta = J[Psi]` is a named posit, not derived by symmetry.
- `ULTRALOCAL_VS_NONLOCAL_STIFFNESS`: W203 is the ultralocal limit, W229 is the induced nonlocal
  completion, and fundamental `c_kin > 0` is a different construction.
- `IMPORTED_GRAVITY_EVIDENCE`: W236 clears the imported-metric theta row only under the branch posit.
- `SECTOR_COMBINATION`: no downstream sector may combine evidence until it uses the same fingerprint and
  free-quantity ledger.

## Validation Role

`process_gates/recovery_contract_action_fingerprint_audit.py` checks that the fingerprint:

- remains process-grade only;
- names exactly the W203/W229/W230/W236 source family;
- preserves the W154 / `c_kin = 0` boundary;
- separates forced, free, imported, and forbidden quantities;
- limits W203 and W236 reductions to branch-local use; and
- does not leak local home paths.

The gate is a process and overclaim boundary check. It does not validate GU physics.

## Next recovery work

Use this fingerprint as the branch-local input to the next `RECOVERY-CONTRACT` or
`GR-DYNAMICAL-BENCHMARKS` swing: preregister the forced-coefficient `O(M^2)` Schwarzschild/Kerr
cancellation or failure test. The next test should name whether it uses the W203 ultralocal limit or the
W229 nonlocal equation, carry `{kappa, Z_U}` as unfixed native normalizations, and stop if it needs to
change the action, source law, variation space, or free-quantity ledger after inspecting the sector target.

Priority signal: none for Joe; daily steward can consume this as advisory evidence inside the existing
protected primary lane.

Paper seed proposal: none.
