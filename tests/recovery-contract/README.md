# tests/recovery-contract/

Computational checkpoints for the recovery-certification lane. These scripts test
branch-local recovery contracts without moving claim status, canon verdicts, public
posture, or portfolio state.

## Scripts

- `cosmo_field_type_scalar_truncation_gate.py` - branch-local `NO_GO` for treating
  the theta-background Klein-Gordon object as cosmological perturbation recovery
  under the frozen W203/W229/W230/W236 fingerprint: the branch supplies a theta
  candidate and background evidence, but no physical scalar projector, observable
  map, SVT quadratic action, or closed scalar truncation certificate.
- `cosmo_nogo_history_scope_gate.py` - bounded history-audit and Swing 1 scope
  gate for the cosmology scalar-truncation no-go defense: background and distance
  evidence do not clear the missing physical scalar projector, observable map,
  SVT quadratic action, or closed scalar truncation obstruction.
- `gr_forced_coefficient_residual_test.py` - branch-local `NO_GO` for exact-vacuum GR
  cancellation under the frozen W203/W229/W230/W236 record-current action fingerprint:
  the principled Schwarzschild `Q^TF(B)` residual is nonzero, while the W229
  `Psi=0` source/YM cancellation tensor is zero.
- `gr_nogo_history_scope_gate.py` - bounded history-audit and Swing 1 scope gate
  for the GR no-go defense: prior linear cheap-read clears do not cancel the
  quadratic `Q^TF(B)` obstruction under the W229 record-current vacuum source law.
- `sm_nogo_history_scope_gate.py` - bounded history-audit and Swing 1 scope gate
  for the Standard Model selector no-go defense: prior host, Type II1 selector,
  finite-control, observer-shadow, and W222 relative-arithmetic results do not
  clear the missing target-free complete-sector selector obstruction.
- `sm_selector_screen_gate.py` - branch-local `NO_GO` for complete low-energy
  Standard Model recovery under the frozen action fingerprint: current evidence
  positively hosts a Pati-Salam / Spin(10) branch and W222's relative
  hypercharge/anomaly arithmetic survives, but no target-free selector or
  complete physical observer-sector closure is derived.
