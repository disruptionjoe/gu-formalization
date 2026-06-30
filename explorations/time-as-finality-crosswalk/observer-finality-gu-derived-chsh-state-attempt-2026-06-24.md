---
title: "Observer/Finality GU-Derived CHSH State Attempt"
date: 2026-06-24
status: exploration/candidate-audit
verdict: STRONG_ANSATZ_ONLY
---

# Observer/Finality GU-Derived CHSH State Attempt

## Verdict

`STRONG_ANSATZ_ONLY`.

I did not find a GU-derived `rho_AB` in the current repo data. I did construct the
strongest honest finite candidate I can justify from the available Pati-Salam
representation data plus explicit extra assumptions:

```text
H_A = V_L = C^4_color tensor C^2_SU(2)_L
H_B = V_R = C^4_anticolor tensor C^2_SU(2)_R
V_L = (4,2,1),  V_R = (4-bar,1,2)
```

The best conservative candidate is a CPT-paired color-mixed state with Bell
correlations only in the SU(2) factor:

```text
rho_mix =
  (1/4) sum_{c=1}^4 |c,bar c><c,bar c|_color
        tensor |Phi+><Phi+|_SU(2)

|Phi+>_SU(2) = (|0_L 0_R> + |1_L 1_R>) / sqrt(2)
```

With the existing control observables, this candidate gives:

```text
CHSH = 2.828427124746 = 2*sqrt(2)
```

I also audited the stronger pure rank-8 CPT-paired Bell ansatz:

```text
|Phi_8> = (1/sqrt(8)) sum_{c=1}^4 sum_{q=0}^1 |c,q>_L tensor |bar c,q>_R
rho_8 = |Phi_8><Phi_8|
```

It gives the same CHSH value:

```text
CHSH = 2.828427124746 = 2*sqrt(2)
```

Both are valid density matrices and strong CHSH candidates. Neither is GU-derived. The
color-mixed state uses less unlicensed structure than the pure rank-8 Bell state, because
it does not assume coherent color superposition. But it still inserts the left/right SU(2)
Bell correlation by hand.

## What The Repo Data Actually Supplies

The current repo supplies the following usable ingredients:

1. Pati-Salam representation content:

```text
S(6,4) -> (4,2,1) + (4-bar,1,2)
```

This fixes the available left/right representation spaces and their dimensions.

2. A natural left/right direct-sum split:

```text
S(6,4) = V_L + V_R
```

This is not itself an Alice/Bob tensor-product state. CHSH needs a two-observer Hilbert
space `H_A tensor H_B`, so an additional physical construction is required to turn this
direct-sum representation data into `rho_AB`.

3. A plausible CPT/left-right pairing:

```text
C: V_L -> V_R
```

This can pair basis labels `(color, SU(2)_L)` with `(anticolor, SU(2)_R)`. It does not
fix amplitudes, phases, purity, color coherence, or entanglement strength.

4. Generic vacuum-entanglement language in the prior Pati-Salam note.

The earlier file invokes Reeh-Schlieder/Bisognano-Wichmann style vacuum entanglement and
then specializes to a maximally entangled finite state. That is a plausible physics
motivation, but it is not yet a GU computation of the reduced finite density matrix.

5. Executable control plumbing.

`tests/h3_pati_salam_chsh_correlator.py` correctly evaluates density matrices and CHSH
observables on the finite proxy. It intentionally marks the GU state as pending.

## Candidate Construction

### Candidate A: Color-Mixed CPT/SU(2) Bell Ansatz

Definition:

```text
rho_A =
  (1/4) sum_c |c,bar c><c,bar c| tensor |Phi+><Phi+|
```

Motivation:

- Pati-Salam gives `C^4_color tensor C^2_SU(2)_L` and
  `C^4_anticolor tensor C^2_SU(2)_R`.
- CPT can pair `c` with `bar c`.
- Color neutrality suggests not privileging one color.
- Refusing unproved coherent color superposition suggests a classical mixture over color.
- A left/right SU(2) Bell factor is the minimal inserted quantum correlation that can
  realize the CHSH obstruction.

Audit:

- Valid density matrix: Hermitian, positive semidefinite, trace one.
- CHSH with current Pauli-type fixture settings: `2.828427124746`.
- Provenance: ansatz.
- Not GU-derived, because no GU zero-mode, propagator, covariance, modular Hamiltonian,
  or finite reduction map produces the SU(2) Bell factor.

This is the strongest conservative candidate I found.

### Candidate B: Pure Rank-8 CPT-Paired Bell Ansatz

Definition:

```text
rho_B = |Phi_8><Phi_8|
|Phi_8> = (1/sqrt(8)) sum_{c,q} |c,q>_L tensor |bar c,q>_R
```

Motivation:

- This is what the prior Pati-Salam note effectively assumes when it says the vacuum
  state has generalized Bell form.
- It is compatible with a CPT-paired basis and maximal finite left/right entanglement.

Audit:

- Valid density matrix: Hermitian, positive semidefinite, trace one.
- CHSH with current Pauli-type fixture settings: `2.828427124746`.
- Provenance: ansatz.
- It is mathematically the same Bell-style object as the control state, now relabelled
  with Pati-Salam/CPT motivation. That relabelling is not a derivation.

This state should remain a control/ansatz until the GU two-point calculation produces it.

## Harsh Provenance Audit

The repo does not yet contain enough data to upgrade either candidate to
`GU_DERIVED_STATE_FOUND`.

Representation theory fixes labels, not a density matrix. The branching
`(4,2,1) + (4-bar,1,2)` tells us what the local fibers are. It does not specify a state
on `V_L tensor V_R`.

CPT pairing fixes at most an antiunitary identification. It does not imply equal Schmidt
coefficients, maximal entanglement, a pure state, or a color-mixed block form.

Color neutrality is not enough. It may motivate averaging over color, but it does not
choose between classical color mixture, coherent color singlet, color-decohered Bell
blocks, or a separable color/isospin state.

Bisognano-Wichmann/Reeh-Schlieder reasoning is too coarse here. Those theorems can support
vacuum entanglement in suitable QFT settings, but they do not by themselves give the finite
Pati-Salam reduced density matrix, its Schmidt spectrum, or the exact `2*sqrt(2)` CHSH
value for these finite observables. The prior note's jump from generic vacuum entanglement
to a maximally entangled `C^8 tensor C^8` Bell state is an ansatz step.

The GU measurement postulate is still absent. The current operators are good Pauli-type
controls on the `SU(2)_L/SU(2)_R` factors, but the repo has not proved that these exact
noncommuting `+/-1` operators are the physically admissible GU/SM-charge measurements.
SM-charge projectors alone are often commuting; a CHSH violation requires suitable
noncommuting local settings.

Also, the claim that every nontrivial SM-charge setting violates CHSH is too strong as a
state-independent statement. Even for an entangled state, CHSH violation depends on the
state and on chosen local noncommuting observables. The executable fixture demonstrates
one optimal setting, not all settings.

## Executable Audit Added

I added:

```text
tests/h3_pati_salam_chsh_candidate_state.py
```

It imports the existing control fixture and audits two candidates:

| candidate | state type | CHSH | GU-derived gate |
|---|---:|---:|---|
| `rho_ansatz_cpt_color_mixed_su2_phi` | color-mixed SU(2) Bell ansatz | `2.828427124746` | rejected |
| `rho_ansatz_cpt_pure_rank8_phi` | pure rank-8 Bell ansatz | `2.828427124746` | rejected |

The rejection is intentional:

```text
GU gate requires role='gu_derived', got 'ansatz'
```

This prevents a control/ansatz Bell state from being silently promoted to GU evidence.

## Data Needed To Upgrade

To upgrade from `STRONG_ANSATZ_ONLY` to `GU_DERIVED_STATE_FOUND`, the repo needs all of
the following:

1. Explicit GU zero-mode or two-point data.

One of:

```text
P_ZM, basis of ker(D_GU) after section pullback
G_LR(x_A,x_B) = <0| psi_L(x_A) psi_R_bar(x_B) |0>
K_AB = finite covariance kernel on V_L tensor V_R
```

This data must determine the finite `rho_AB`, not merely motivate entanglement.

2. A finite reduction map.

A specified map from the field-theoretic/local-algebra state to:

```text
rho_AB in End(V_L tensor V_R)
```

including normalization, trace, positivity, and how color/isospin indices are contracted.

3. CPT/left-right symmetry status of the selected GU vacuum or section.

The repo must determine whether the physical section preserves the left/right `Z_2` or
breaks it. If broken, the Bell-pair ansatz may be wrong.

4. The Schmidt/correlation spectrum.

The derived state must say whether the left/right pairing is:

```text
pure maximally entangled,
color-mixed with SU(2) Bell blocks,
partially entangled,
separable,
thermal/modular,
or something else.
```

5. A GU measurement postulate.

The CHSH observables must be identified as GU-admissible self-adjoint `+/-1` operators:

```text
A, A' in End(V_L)
B, B' in End(V_R)
```

with local Alice/Bob commutation and noncommuting same-party settings justified physically.

6. A derived CHSH computation.

After the above, run the same finite gate:

```text
Tr(rho_AB (A tensor B + A tensor B' + A' tensor B - A' tensor B')) > 2
```

or else record the failure if the derived state/settings stay at `<= 2`.

## Final Assessment

The current repo supports a strong candidate state and a clean executable audit, but not a
GU-derived state. The strongest honest result is:

```yaml
candidate_state_found: true
candidate_chsh: 2.828427124746
candidate_status: ansatz
gu_zero_mode_or_two_point_source: missing
gu_measurement_postulate: missing
verdict: STRONG_ANSATZ_ONLY
```

