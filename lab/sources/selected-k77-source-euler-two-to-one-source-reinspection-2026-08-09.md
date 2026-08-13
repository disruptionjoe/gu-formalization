---
artifact_type: source_reinspection
created: 2026-08-09
status: SOURCE_CORRECTS_INDEPENDENT_B_VARIATION__CONFIRMS_TWO_TO_ONE_BAR__SILENT_GLOBAL_COMPLETION
source_return: SOURCE-CORRECTS
---

# Source reinspection: which variations belong to the first action?

## Decisive return

The source field space corrects the v0.108 freedom count. Weinstein's first
bosonic action is displayed on `(epsilon,varpi,g)`, not on independent
coordinates `(B,T,g)`. The reference connection

```text
B_omega = nabla_0 + epsilon^-1 d_0 epsilon
```

is derived from `epsilon`, and

```text
T_omega = varpi - B_omega.
```

The displayed translation varies `varpi` while holding `epsilon` fixed. It
therefore varies `T` at fixed `B`; it does not authorize an arbitrary variation
of `B` while holding `T` fixed. The v0.108 equation `2b+t=0` came from precisely
that latter direction. It is a useful reconstruction condition selecting one
representative, but it is not a source-field Euler equation.

## Primary/source loci already held locally

- `lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md`: the action
  domain, `T_omega`, and the displayed `varpi` translation
  `I_1^B(epsilon,varpi+s alpha)`;
- `lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md`:
  epsilon variation gives `delta B=D_B eta`, `delta T=-D_B eta`, together with
  the moving-Shiab response;
- `lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md`:
  Weinstein's magnitude claim is the reduction of two problems to one, not a
  first-principles value.

## Correct source-coordinate consequence

At the selected scalar-jet point define invariant coefficients

```text
F_B        = f (Phi1 wedge Phi1)
D_B T      = u (Phi1 wedge Phi1)
T          = t Phi1.
```

The displayed translation residual and the already-derived metric-volume
trace give two independent equations:

```text
312(f+u+t^2)+t = 0,
624(f+u/2+t^2/3)+t = 0.
```

They imply

```text
f=t^2/3,
u=-t/312-4t^2/3,
```

leaving one common amplitude. The source does not select that amplitude.
The v0.108 rational point is one member of this family, not a unique source
vacuum.

## Source silence

The released source does not supply the invariant scalar ansatz, the rational
coefficients, a nonconstant `Y14` atlas, an open-neighborhood solution of the
epsilon prolongation `Xi=D_omega Upsilon`, a physical magnitude-selection
mechanism, radiative screening, or a cosmological solution.

Source return:
`SOURCE_CORRECTS_INDEPENDENT_B_EULER_AS_NON_SOURCE_VARIATION__SOURCE_CONFIRMS_TRANSLATION_UPSILON_AND_EPSILON_CHAIN__REPO_DERIVES_LOCAL_TWO_TO_ONE_FAMILY__SOURCE_SILENT_GLOBAL_PROLONGATION_AND_AMPLITUDE_SELECTION`.
