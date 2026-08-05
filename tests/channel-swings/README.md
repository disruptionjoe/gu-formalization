# Pre-contract wave probes

This local index records the three pre-contract probes added on 2026-08-05.
The repository-wide family inventory remains in `tests/README.md`.

- `precontract_wave_0b_trace_reversal_robustness_probe.py` rejects the inherited
  three-trace switch as ill-typed, retains the ambient selector kill, and proves
  by exact `26` versus `6` response ratios that naive restriction is not the
  observed Einstein receiver.
- `conditional_physics_ledger_v01_probe.py` enumerates all 86 source rows into
  78 canonical targets plus eight aliases, validates every information-bearing
  row field, recomputes the meter/residue and tests the new-kind and independent
  escalation rules.
- `precontract_wave_0c_typed_identity_theorem_scope_probe.py` proves the narrow
  projective spinor-line identity, separates it from the written adjoint Shiab,
  constructs the exact Riemann trace-reversal adapter and plants counterexamples
  against full-domain and scale-theorem overreach.

Run the SymPy-bearing probes with `uv run --with sympy==1.14.0 python <path>`;
the ledger probe uses the standard Python interpreter.
