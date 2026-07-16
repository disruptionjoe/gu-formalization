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
- `gr_forced_coefficient_residual_test.py` - branch-local `NO_GO` for exact-vacuum GR
  cancellation under the frozen W203/W229/W230/W236 record-current action fingerprint:
  the principled Schwarzschild `Q^TF(B)` residual is nonzero, while the W229
  `Psi=0` source/YM cancellation tensor is zero.
- `sm_selector_screen_gate.py` - branch-local `NO_GO` for complete low-energy
  Standard Model recovery under the frozen action fingerprint: current evidence
  positively hosts a Pati-Salam / Spin(10) branch and W222's relative
  hypercharge/anomaly arithmetic survives, but no target-free selector or
  complete physical observer-sector closure is derived.
