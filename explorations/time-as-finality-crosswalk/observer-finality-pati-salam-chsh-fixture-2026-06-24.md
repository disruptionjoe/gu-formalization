---
title: "Observer/Finality Pati-Salam CHSH Fixture"
date: 2026-06-24
status: executable-control
verdict: EXECUTABLE_CONTROLS_PASS_GU_PENDING
---

# Observer/Finality Pati-Salam CHSH Fixture

## Verdict

The finite-dimensional Pati-Salam proxy CHSH fixture now exists as an executable Python
script:

`tests/h3_pati_salam_chsh_correlator.py`

It verifies the control calculation:

- a maximally entangled Alice/Bob control reaches `CHSH = 2*sqrt(2)`;
- a product control gives `CHSH = sqrt(2) <= 2`;
- the control density matrices are Hermitian, positive semidefinite, and trace one;
- the control observables are Hermitian `+/-1` operators;
- Alice-side and Bob-side observables commute as a valid local CHSH split.

The GU-derived state is not supplied. The fixture marks the GU branch
`PENDING_GU_INPUT` by default, and it can be made to fail explicitly with
`--require-gu`. This is intentional: a hand-inserted Bell state is a control, not a GU
proof.

## Fixture Construction

The executable model uses the finite proxy

```text
H_A = C^4_color tensor C^2_SU(2)_L
H_B = C^4_anticolor tensor C^2_SU(2)_R
H_AB = H_A tensor H_B
dim(H_AB) = 64
```

This follows the Pati-Salam split only as a controlled toy version of
`(4,2,1)` versus `(4-bar,1,2)`. The color/anticolor factors are spectators in the
control calculation. The CHSH observables act on the `SU(2)_L` and `SU(2)_R` qubit
factors:

```text
A  = Z_L
A' = X_L
B  = (Z_R + X_R) / sqrt(2)
B' = (Z_R - X_R) / sqrt(2)
```

Each observable is embedded into the full 64-dimensional space with identities on the
other factors.

## Executed Controls

Command:

```bash
python tests/h3_pati_salam_chsh_correlator.py
```

Observed control values:

| state | E(a,b) | E(a,b') | E(a',b) | E(a',b') | CHSH |
|---|---:|---:|---:|---:|---:|
| `rho_control_phi_8` | `0.707106781187` | `0.707106781187` | `0.707106781187` | `-0.707106781187` | `2.828427124746` |
| `rho_control_product_00` | `0.707106781187` | `0.707106781187` | `0.000000000000` | `0.000000000000` | `1.414213562373` |

The first row is the expected Tsirelson control. The second row is the separable control
and stays inside the Bell bound.

## GU Gate Interface

The script exposes two explicit future-work hooks:

```python
def supply_gu_derived_rho_ab() -> DensityCandidate:
    ...

def supply_gu_admissible_observables() -> CHSHObservables:
    ...
```

Both currently raise `PendingGUInput`. A future successful GU pass must supply:

- a density matrix with `role="gu_derived"`;
- provenance beginning with `gu-derived:`;
- a Hermitian, positive semidefinite, trace-one `rho_AB`;
- CHSH observables with provenance beginning with `gu-admissible:`;
- Hermitian `+/-1` observable checks and Alice/Bob local commutation;
- `CHSH > 2 + 1e-6`.

The guardrail is also explicit: `evaluate_gu_candidate(...)` rejects a candidate that
matches the maximally entangled control state or the product control state. Therefore the
fixture cannot be closed by copying the Bell control into the GU slot.

## What This Proves

This proves that the next-gate calculation has executable finite-dimensional plumbing:

- the CHSH sign convention and observables are implemented correctly;
- the maximally entangled and product controls separate the quantum and separable cases;
- the Pati-Salam-inspired Alice/Bob factor split is concrete enough to evaluate
  correlators;
- future GU data has a clearly named insertion point and validation path.

It also proves that the fixture is adversarial against the obvious false positive:
declaring the control Bell state to be the GU result.

## What This Does Not Prove

This does not prove that GU forces a CHSH violation.

Missing ingredients remain:

- a GU-derived `rho_AB` from zero modes, a two-point function, or another auditable GU
  construction;
- a GU measurement postulate selecting the admissible Pati-Salam observables;
- proof that the selected observables are the right physical `SU(2)_L/SU(2)_R` or
  SM-sector measurements rather than convenient Pauli controls;
- proof that NAC/locality and the observer-finality odd-SBP input are physically forced
  by the GU construction;
- a derived value `CHSH > 2`, rather than a value obtained by choosing a known Bell state.

So the status is:

```yaml
fixture_status: EXECUTABLE
controls: PASS
gu_state: PENDING
gu_observables: PENDING
physical_forcing: NOT_ESTABLISHED
verdict: EXECUTABLE_CONTROLS_PASS_GU_PENDING
```

## Next Gate

The next worker should not add more control states as proof. The required move is to
derive or import an auditable GU `rho_AB` and an auditable set of GU-admissible
observables, then run the same `evaluate_gu_candidate(...)` gate. If that state is
separable or if all admissible settings stay at `CHSH <= 2`, the observer/finality CHSH
claim remains conditional rather than physically forced.
