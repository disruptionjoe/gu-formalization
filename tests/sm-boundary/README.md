# tests/sm-boundary

Computational certificates for `LANE-SM-BOUNDARY`, the "SM as boundary / cobordism condition" lane. These scripts do not derive the generation count and do not change any canon, claim status, verdicts, or public posture. They test whether simple SM-shaped boundary constraints pin or constrain the external chiral background.

Boundary: this family is a local anomaly / inflow toy only. A green result says local anomaly cancellation gives a 2-primary parity constraint and no mod-3 selector for the external count. It is not a generation-count derivation.

Run from the repository root:

```bash
python tests/sm-boundary/anomaly_inflow_toy.py
python tests/sm-boundary/verify/anomaly_inflow_algebraic_indep_check.py
```

## Certificates

- `anomaly_inflow_toy.py` combines a 2D flux-Dirac lattice check with a bounded anomaly-free boundary-multiplet census. It reads off that local U(1) anomaly cancellation gives a parity constraint on the external count but no mod-3 selector.
- `verify/anomaly_inflow_algebraic_indep_check.py` re-checks the same boundary-anomaly conclusion with pure integer algebra and an independent constructive family, without importing the lattice implementation.
