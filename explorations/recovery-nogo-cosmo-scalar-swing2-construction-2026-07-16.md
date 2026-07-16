---
title: "Recovery no-go cosmology scalar Swing 2 construction attempt"
status: exploration
doc_type: recovery_no_go_defense
created: 2026-07-16
run_id: GUH-20260716T190718Z-cosmo-swing2
target: RECOVERY-NOGO-COSMO-SCALAR
test: tests/recovery-contract/cosmo_nogo_swing2_construction_gate.py
register: lab/process/recovery-no-go-defense-register.json
---

# Recovery no-go cosmology scalar Swing 2 construction attempt

Operational result: `NO_SURVIVOR` for Swing 2 of
`RECOVERY-NOGO-COSMO-SCALAR`.

This is not a cosmology verdict, dark-energy verdict, claim-status move, canon
move, public-posture move, or paper action. It only records that the named
alternate construction classes do not currently supply a source-owned physical
scalar and closed perturbation truncation for the frozen W203/W229/W230/W236
record-current branch.

## Decision question

Can a genuinely different construction avoid the Swing 1 obstruction by
deriving a physical scalar object from GU-side data rather than treating the
current homogeneous `s*(theta)` amplitude as the physical perturbation variable?

Answer: no survivor was found in the predeclared construction space.

## Construction fork

Source side: the GU-native W203/W229/W230/W236 record-current/source-action
fingerprint. Comparator side: standard cosmological scalar-vector-tensor
language, used only as the benchmark vocabulary for perturbation recovery.

A valid Swing 2 escape must derive at least:

1. a physical scalar projector or scalar object;
2. a gauge-invariant observable map;
3. a block-diagonal SVT quadratic action or equivalent closed truncation;
4. residue accounting for vector, tensor, connection, gauge, boundary, and
   non-scalar source terms; and
5. a first falsification test fixed before target-data or standard-SVT import.

## Attempted constructions

| construction | axis delta | result | first falsification test |
|---|---|---|---|
| Gauge-invariant or constrained composite scalar from frozen GU fields | Replace the raw homogeneous `s*(theta)` amplitude with a GU-derived scalar composite or constrained gauge-invariant. | `NO_SURVIVOR`: prior packets name the needed `scalar_theta_mode`, `Z_theta`, `C_Rtheta`, and `xi_eff`, but none is emitted by the frozen fingerprint. No projector, observable map, or quadratic action is currently source-owned. | A future composite must output a scalar mode and positive kinetic normalization before any DESI, CMB, or SVT-target comparison; it fails if the object is chosen because it has the desired scalar equation. |
| Mixed-sector scalar induced by already-present GU sectors | Let the scalar arise from mixing among theta, normal-flux, source-current, or connection sectors rather than from `s*(theta)` alone. | `NO_SURVIVOR`: the existing records leave source, gauge, boundary, vector, tensor, and connection residues open. A mixed-sector scalar without residue discharge is not a closed scalar truncation. | The mixed quadratic action must block-diagonalize with an independently named scalar block and all non-scalar residues accounted for; it fails if vector/tensor/connection residues feed the scalar equation at the same order. |
| Boundary-conditioned scalar channel under explicit adapter assumption | Add a typed boundary/firewall adapter assumption and ask whether it supplies the scalar channel. | `NO_SURVIVOR`: no frozen adapter packet supplies the scalar projector, physical observable, boundary data, or state-preserving perturbation dynamics. This remains an assumption-capped possible future construction. | A returned adapter must provide provenance, branch conditions, scalar projection, boundary data, and a gauge-invariant observable; it fails if it merely selects the desired scalar mode as boundary data. |
| Standard cosmological SVT variables | Use ordinary cosmological perturbation variables as the scalar sector. | `INVALID_ESCAPE`: these variables define the comparator benchmark. Importing them as GU dynamics or as the missing projector would assume the target theory. | Reject any candidate whose scalar equation is the standard SVT equation unless the GU source action independently derives the projector and truncation first. |

## Result

Swing 2 returns `NO_SURVIVOR`.

The obstruction is not merely a naming issue. The alternate constructions remain
eligible future construction classes only after they produce source-side scalar
data, not before. At the current grade:

- the constrained-composite route lacks an emitted scalar object and
  normalization;
- the mixed-sector route lacks a block-diagonal quadratic action and residue
  discharge;
- the boundary-conditioned route lacks a frozen adapter return; and
- the standard-SVT route is a comparator, not a lawful GU escape.

The original branch-local no-go is preserved at its scope. Swing 3 should now
adjudicate whether this no-survivor result supports a bounded stop decision or
whether the construction space needs one more finite source-owned test.

## Status boundary

No `RESEARCH-STATUS.md`, `CANON.md`, `NEXT-STEPS.md` top block,
`lab/process/research-portfolio.json`, claim ledger, paper, license, Lean,
absorbed source, public-posture, verdict, or cross-repo surface moved.

Paper seed proposal: none.
