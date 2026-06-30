---
title: "Observer/Finality GU Measurement Postulate Gate"
date: 2026-06-24
status: exploration/gate
verdict: OPEN_MISSING_GU_MEASUREMENT_POSTULATE
depends_on:
  - explorations/persona-and-dialectic/persona-review-cross-panel-synthesis-2026-06-24.md
  - explorations/time-as-finality-crosswalk/observer-finality-physical-forcing-gate-2026-06-24.md
  - explorations/time-as-finality-crosswalk/observer-finality-pati-salam-chsh-fixture-2026-06-24.md
  - explorations/time-as-finality-crosswalk/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md
  - explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md
  - explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md
  - explorations/time-as-finality-crosswalk/h3-gap2-f2-pati-salam-bipartite-2026-06-23.md
executable:
  - tests/h3_pati_salam_gu_measurement_gate.py
---

# Observer/Finality GU Measurement Postulate Gate

## Verdict

`OPEN_MISSING_GU_MEASUREMENT_POSTULATE`.

This pass does not find a GU-derived Pati-Salam CHSH state or a GU-derived measurement
postulate. The repo supplies the Pati-Salam representation split and executable CHSH
controls. It does not supply the finite GU density matrix `rho_AB`, the extraction map from
zero modes or a two-point function, or the rule selecting admissible noncommuting
Alice/Bob observables.

The strongest violation currently available remains the previous CPT-paired Bell
completion:

```text
rho_ansatz_cpt_color_mixed_su2_phi       CHSH = 2.828427124746
rho_ansatz_cpt_pure_rank8_phi            CHSH = 2.828427124746
```

Both are useful ansatz/control states. Neither is GU-derived. The non-hand-inserted
symmetry-only completion is separable or at least SU(2)-uncorrelated for the existing
fixture settings, and gives no CHSH violation.

## Surfaces Read

Required surfaces:

- `explorations/persona-and-dialectic/persona-review-cross-panel-synthesis-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-physical-forcing-gate-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-pati-salam-chsh-fixture-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md`
- `tests/h3_pati_salam_chsh_correlator.py`
- `tests/h3_pati_salam_chsh_candidate_state.py`

Additional relevant Pati-Salam / generation / H3 surfaces checked:

- `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md`
- `explorations/generation-sector/generation-count-rs-rank-gate-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-clifford-projector-computation-2026-06-24.md`
- `explorations/analytic-index-fredholm/g2-kk-zero-mode-unitarity-2026-06-23.md`
- `explorations/time-as-finality-crosswalk/h3-gap2-gu-universality-2026-06-23.md`
- `explorations/time-as-finality-crosswalk/h3-gap2-f2-pati-salam-bipartite-2026-06-23.md`
- `explorations/time-as-finality-crosswalk/h3-outcome-d-prime-gu-bridge-2026-06-23.md`

## Measurement Postulate / Data Interface GU Would Need

### 1. Zero-Mode Space

Required object:

```text
Z_phys = physical GU zero-mode space after section pullback, gauge constraints,
         and any RS/spin-1/2 decomposition used by the SM sector.

Z_L = P_L Z_phys,     P_L targets V_L = (4,2,1)
Z_R = P_R Z_phys,     P_R targets V_R = (4bar,1,2)
```

The interface must say whether the state is built from:

```text
ker(D_GU) on Y^14
ker(s*(D_GU)) on X^4
a KK zero-mode projection P_ZM
a GU vacuum state omega on local algebras
a GU two-point function / covariance kernel
```

Acceptance rule: provide a basis, projector, covariance, or Green's function with provenance
from GU operator data. Index values or representation dimensions alone are not enough.

Current repo audit: partial. The repo has `S(6,4) -> (4,2,1) + (4bar,1,2)`, right-H/index
language, and reconstruction-grade KK zero-mode projection language. The newer RS
symbol-index gate keeps the analytic zero-mode/index story open. No finite basis or
covariance for the CHSH state is supplied.

### 2. Inner Product

Required object:

```text
<psi,phi>_GU on Z_phys
G_L, G_R finite Gram matrices on Z_L, Z_R after reduction
```

The inner product must be induced from the GU geometry, for example the section-pullback
L2 pairing with the KK renormalization factor if that route is used. If a finite C^8 model
is used, the map from the GU pairing to the standard finite Hermitian pairing must be stated.

Acceptance rule: the finite density matrix and observables must be Hermitian with respect
to this inner product, not just with respect to a convenient Euclidean basis.

Current repo audit: partial. The executable fixture uses the standard finite inner product.
The G2 note discusses an L2/KK normalization factor at reconstruction grade. The repo does
not give the finite GU Gram matrix for the Pati-Salam CHSH reduction.

### 3. Density Matrix Extraction

Required object:

```text
rho_AB in End(H_A tensor H_B),     rho_AB >= 0,     Tr(rho_AB) = 1
H_A = V_L or a GU-derived finite Alice space
H_B = V_R or a GU-derived finite Bob space
```

The extraction map must be explicit. Examples of acceptable future data:

```text
G_LR(x_A,x_B) = <0| psi_L(x_A) psi_R_bar(x_B) |0>
K_AB = finite covariance matrix on V_L tensor V_R
omega(O_A O_B) = Tr(rho_AB (O_A tensor O_B))
rho_AB = normalized finite reduction of omega to A_A tensor A_B
```

Acceptance rule: a Bell state, a maximally entangled C^8 vector, or a CPT-paired equal
Schmidt spectrum cannot be inserted as the extraction map. It must be the output of the
GU zero-mode/two-point calculation.

Current repo audit: missing. The older H3 Pati-Salam note asserts a generalized Bell
vacuum using CPT plus Bisognano-Wichmann/Reeh-Schlieder language, but it does not compute
the finite `rho_AB`, its Schmidt coefficients, or its color/isospin contraction. The newer
state-attempt file correctly demotes that step to ansatz.

### 4. Alice/Bob Factorization

Required object:

```text
H_A tensor H_B
A_A subset End(H_A) tensor I
A_B subset I tensor End(H_B)
[A_A, A_B] = 0 for spacelike separated Alice/Bob regions
```

The Pati-Salam representation gives a direct sum:

```text
S(6,4) = V_L + V_R
```

CHSH needs a two-system tensor product:

```text
H_AB = H_A tensor H_B
```

Acceptance rule: GU must provide the map from the direct-sum field data or local QFT
algebras to the two-observer tensor-product state. The finite proxy
`H_A = V_L`, `H_B = V_R` is a good test harness, not yet a derivation.

Current repo audit: partial. The fixture defines the finite proxy. The repo does not
derive the physical two-observer reduction from GU.

### 5. Admissible Observables

Required object:

```text
A, A' in End(H_A)
B, B' in End(H_B)
A^2 = A'^2 = B^2 = B'^2 = I
A = A*, A' = A'*, B = B*, B' = B'*
provenance = gu-admissible:<measurement-postulate-reference>
```

The measurement postulate must say which operations are physically allowed:

- spectral projectors of Pati-Salam / SM charge operators;
- gauge-rotated isospin components;
- local functions of field operators;
- or another specified GU observer readout algebra.

It must also explain why same-party noncommuting settings are admissible. Diagonal SM
charge projectors alone are generally commuting and do not by themselves force CHSH
violation. The current Pauli `X/Z` operators on SU(2) factors are excellent controls, but
they need GU admissibility before they count as physical settings.

Current repo audit: missing/control-only. The fixture checks the algebra of the control
observables, but no GU measurement postulate selects them.

### 6. Locality and NAC Assumptions

Required assumptions:

```text
[A_x, B_y] = 0 for spacelike separated regions x,y
rho_AB is prepared independently of later choices a,a',b,b'
Alice setting/readout does not depend on Bob future data, and conversely
no postselection on joint outcomes or settings is used to manufacture rho_AB
```

This is the Bell/CHSH locality plus the repo's NAC discipline: local sections are not
anticipatory. The GU argument should connect this to null-cone propagation and section
pullback for the specific measurement algebras.

Current repo audit: conditional. The fixture verifies finite Alice/Bob commutation. The
H3/GU notes argue NAC from null-cone propagation at reconstruction grade, conditional on
the VZ/Fredholm/APS gates. The live CHSH state and observables are still absent.

## Audit Table

| Required item | Repo supplies | Gate status |
|---|---|---|
| Pati-Salam representation spaces | Yes: `V_L=(4,2,1)`, `V_R=(4bar,1,2)` | Sufficient for labels only |
| Zero-mode basis/covariance | No finite GU basis or covariance | Missing |
| Inner product for finite reduction | Standard fixture pairing only; GU L2/KK pairing reconstruction-grade | Partial |
| `rho_AB` extraction | No zero-mode/two-point-to-density-map | Missing |
| Alice/Bob factorization | Finite proxy only; direct sum to tensor-product map not derived | Partial |
| Admissible observables | Pauli controls only | Missing measurement postulate |
| Locality/NAC | Matrix commutation in fixture; GU NAC conditional | Conditional |
| CHSH violation | Bell controls and ansatz states reach `2*sqrt(2)` | Not GU-derived |

## Strongest Non-Hand-Inserted Construction Tried

### Attempt 1: Representation-Only / Symmetry Baseline

Use only the representation data:

```text
H_A = V_L = C^4_color tensor C^2_SU(2)_L
H_B = V_R = C^4_anticolor tensor C^2_SU(2)_R
```

With no two-point function or vacuum covariance, the canonical non-correlating completion is
the tracial state:

```text
rho_sym = I_64 / 64
```

For the existing traceless SU(2) Pauli control observables, this gives:

```text
CHSH = 0
```

More generally, full `G_PS`-invariance constrains density operators on `V_L tensor V_R`
by Schur blocks such as the SU(4) singlet/adjoint split inside `4 tensor 4bar`, but it
does not determine the block weights. It also leaves the SU(2)_L/SU(2)_R factors maximally
mixed unless an additional left-right SU(2) correlation is inserted. This route therefore
does not derive a violation.

Status: not a GU physical state, but the cleanest no-extra-correlation baseline. It is
separable/no-violation for the current fixture settings.

### Attempt 2: CPT-Paired Color-Mixed SU(2) Bell State

The previous state-attempt file gives the strongest plausible violating completion:

```text
rho_mix =
  (1/4) sum_c |c,bar c><c,bar c|_color
        tensor |Phi+><Phi+|_SU(2)
```

This reaches:

```text
CHSH = 2.828427124746
```

But the SU(2) Bell factor is not obtained from a GU zero-mode, propagator, modular
Hamiltonian, or finite reduction map. It is the needed answer inserted into the state.

Status: strong ansatz only.

### Attempt 3: Pure Rank-8 CPT-Paired Bell State

The still stronger completion is:

```text
|Phi_8> = (1/sqrt(8)) sum_{c,q} |c,q>_L tensor |bar c,q>_R
rho_8 = |Phi_8><Phi_8|
```

It also reaches:

```text
CHSH = 2.828427124746
```

This is mathematically the Bell control with Pati-Salam labels and a CPT pairing. It is
not GU-derived unless a GU two-point/state extraction calculation outputs exactly this
Schmidt spectrum and phase convention.

Status: strong ansatz only.

## Executable Gate Added

I added:

```text
tests/h3_pati_salam_gu_measurement_gate.py
```

It checks three things:

1. The measurement interface items above are still partial or missing.
2. Known non-GU candidates are rejected by provenance:
   `symmetry_baseline`, `control`, and `ansatz` roles cannot pass as `gu_derived`.
3. The live GU hook skips by default while `rho_AB` and observables are missing, and fails
   if run with `--require-gu`.

Intended commands:

```bash
python tests/h3_pati_salam_gu_measurement_gate.py
python tests/h3_pati_salam_gu_measurement_gate.py --require-gu
```

Expected current status:

```text
default:      SKIP_MISSING_GU_INPUTS
--require-gu: FAIL, because no GU rho_AB/admissible observables are supplied
```

This is deliberate. A future pass should only make `--require-gu` pass by supplying
`role="gu_derived"` state data and `gu-admissible:` observable provenance.

## Hegelian Steelman / Antithesis / Synthesis

Steelman:

GU has the right structural ingredients for a physical CHSH state. The internal fiber
spinor gives the Pati-Salam split:

```text
S(6,4) -> (4,2,1) + (4bar,1,2)
```

CPT or left-right symmetry plausibly pairs the two 8-dimensional sectors. Relativistic
QFT vacuum structure plausibly produces spacelike entanglement. If GU supplies the actual
two-point function and measurement postulate, the existing finite fixture can immediately
test whether the resulting `rho_AB` violates CHSH.

Antithesis:

Representation labels are not a density matrix. CPT pairing is not a Schmidt spectrum.
Reeh-Schlieder/Bisognano-Wichmann language does not compute the finite Pati-Salam reduced
state. Pauli controls on SU(2) factors are not automatically physical SM/GU measurements.
The statement "all nontrivial SM-charge settings violate CHSH" is too strong: CHSH depends
on the state and on admissible noncommuting local settings.

Synthesis:

Keep the observer/finality theorem and the Pati-Salam fixture, but route every physical
claim through a typed measurement interface:

```text
GU zero-mode/two-point data
  -> finite inner-product space and rho_AB
  -> GU-admissible local observables
  -> locality/NAC check
  -> CHSH computation
```

Controls and ansatz states remain valuable because they verify the plumbing and show the
target is reachable. They do not count as GU evidence.

Closure conditions:

- `GU_DERIVED_STATE_FOUND`: a state with `role="gu_derived"` and provenance from a GU
  zero-mode/two-point calculation, plus `gu-admissible:` observables, passes the live gate
  and gives `CHSH > 2 + epsilon` with locality/NAC intact.
- `SEPARABLE/NO_VIOLATION`: the GU-derived state and all GU-admissible settings stay at
  `CHSH <= 2`.
- `STRONG_ANSATZ_ONLY`: the only violations continue to come from CPT/Bell completions or
  control observables.
- `OPEN_MISSING_GU_MEASUREMENT_POSTULATE`: the finite state extraction or admissible
  observable rule is still missing.

This pass lands in the fourth case.

## Final Assessment

```yaml
pati_salam_representation_split: supplied
finite_chsh_fixture: supplied
control_chsh_value: 2.828427124746
best_ansatz_chsh_value: 2.828427124746
non_hand_inserted_baseline: separable_or_uncorrelated_for_current_settings
gu_zero_mode_basis_or_covariance: missing
gu_density_matrix_extraction: missing
gu_measurement_postulate: missing
locality_nac_for_live_data: conditional
verdict: OPEN_MISSING_GU_MEASUREMENT_POSTULATE
```

Final verdict: `OPEN_MISSING_GU_MEASUREMENT_POSTULATE`
