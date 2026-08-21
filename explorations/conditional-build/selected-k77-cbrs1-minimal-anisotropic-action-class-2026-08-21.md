---
artifact_type: conditional_build_result
created: 2026-08-21
status: CBRS1_MINIMAL_ONE_AXIS_CLASS_KILLED_AT_INTRINSIC_METRIC_TRACE__NONPARALLEL_FIRST_JET_SUCCESSOR_LIVE
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_AND_METX_ARGUMENT_GRAMMAR__REPO_DERIVES_CONDITIONAL_CLASS__SOURCE_SILENT_ON_THIS_ANISOTROPIC_BRANCH
registry: lab/process/selected-k77-cbrs1-minimal-anisotropic-action-class.json
probe: tests/channel-swings/selected_k77_cbrs1_minimal_anisotropic_action_class_probe.py
canon_verdict_change: none
---

# Selected K77 CBRS-1 minimal anisotropic action class

## Result first

The smallest target-blind coefficient-anisotropic class allowed by the
selected K77 first action has a new exact nonzero stationary field branch,
but it is **not** a stationary background once `MET(X)` is varied.

Freeze one pinned K77 axis against its thirteen-dimensional complement:

```text
T(a,b) = a e^0 gamma_0 + b sum_(i=1)^13 e^i gamma_i.
```

Direct Clifford evaluation gives

```text
I(a,b) = a^2/2 + 312 a b^2 + 1144 b^3 + 13 b^2/2.
```

Besides zero and the known homogeneous branch `a=b=-1/312`, its exact
anisotropic root is

```text
(a,b)=(-13/96, 1/48).
```

This is not merely critical inside the two-parameter ansatz. The symbolic
Clifford adjoint evaluates all `14 x 16,384 = 229,376` real pointwise
translation directions, and the complete action covector has support zero.
The reduced-curvature packet is nonzero, all fourteen diagonal coefficient
slots are live, and the existing rank-100 Gauss theorem keeps the untraced
full-`II` norm as the action owner.

The held-out test then kills the class. Its on-shell first-action density is

```text
I(-13/96,1/48)=221/55296 != 0.
```

At fixed `varpi`, naturality and CC-01 give the intrinsic metric first
variation

```text
E_g = rho I + (D_g B_Z)^! (E_B-E_T).
```

The frozen class is a constant zero-jet, so the momentum derivative and hence
the source-graph formal adjoint vanish. In canonical symmetric-metric order,
the normalized row is

```text
(-221/27648,0,0,0,221/27648,0,0,221/27648,0,221/27648).
```

It is nonzero. The class therefore closes before full Hessian, global
stabilizer, `mu6`, `J`/Higgs, photon, extra-`U(1)` or gravitational-spectrum
work becomes admissible.

## Frozen class and target blindness

The one-versus-thirteen split was selected before the metric trace was
computed. It is the smallest orbit that breaks the homogeneous coefficient
symmetry without adding a projector, spectral threshold, ledger row, external
datum, potential, normalization or fitted counterterm. The pinned axis is the
existing labelled K77 coefficient axis, not a target-facing Standard Model
selector.

The metric trace was reserved as the held-out output. Neither its support nor
its sign entered the solve for `a` and `b`.

## Typed objects

| object | type here | not promoted to |
| --- | --- | --- |
| `T(a,b)` | constant K77 Clifford-valued one-form zero-jet | spacetime-inhomogeneous open solution |
| `F_bar=(1/3)T wedge T` | nonzero reduced-curvature packet | full source-global curvature solution |
| full-`II` owner | existing rank-100 Gauss restriction of the untraced action norm | arbitrary stationary 100-component `II` orbit |
| complete tangent | pointwise real `u(64,64)` coefficient bank | global associated-bundle/Green domain |
| `E_g` | intrinsic action metric covector with `MET(X)` varied | observed Einstein equation or stress tensor |
| branch | reconstruction-grade conditional action critical point | released source-owned or physical vacuum |

The coefficient anisotropy is not spacetime inhomogeneity. This class is the
minimal coefficient-level interpretation of the CBRS prompt and is killed at
the metric gate. The successor must introduce a genuine nonparallel first jet
and solve its metric source graph on the same carrier.

## Prior-art and correction fence

The August 14 SR-1C--SR-1H chain already closes every then-serialized owned
carrier and the full compatible affine jet fibre over the canonical Zorro
roots. This result does not replay those classes: Joe's August 21 CBRS priority
authorizes explicit new reconstruction-grade classes. The new anisotropic
root is not claimed in the released source.

CC-01 is applied rather than cited decoratively: `MET(X)` is the second action
argument, not background furniture. Fixed-metric criticality therefore cannot
license a background. The HQ and I2B correction rows are out of the decisive
path; no HQ phase, observer adjoint, contact image or gauge-cohomology result
is consumed here.

## Routing notice

This artifact is comparator-adjacent because later CBRS arcs name Standard
Model-facing stabilizer and spectrum roles. The present computation uses none
of those target values. `target_claim: NONE-NOT-A-KILL` is binding: the result
closes one frozen conditional action class, not GU, the ledger rows, or every
future stationary background.

The six/seven-axis substrate-candidate template is exempt: this is a local K77
variational class test, not a proposed substrate route around a chirality,
anomaly or gauge-emergence no-go. Layer-0 typing is supplied above.

## Hostile return

- **Wrong geometry:** the class is coefficient-anisotropic but remains a
  constant zero-jet. It is not called the requested spacetime-nonhomogeneous
  vacuum; its failure instead forces the first-jet successor.
- **Reduced-tangent shortcut:** the two reduced Euler equations are not the
  stationarity certificate. The complete real coefficient covector is.
- **Frozen-metric shortcut:** CC-01 forbids treating `MET(X)` as furniture;
  the held-out metric row is the decisive kill.
- **Full-II overclaim:** the existing action measures the complete rank-100
  Gauss carrier, but this branch does not construct an arbitrary stationary
  100-component `II` tensor.
- **Target leakage:** no Standard Model rank, mass, charge, spectral cut or
  comparator datum selects the class or enters the calculation.

## Reverse-scaffold consequence

CBRS-1 remains active, but its minimal constant coefficient-anisotropic class
is closed. Do not compute or interpret its Hessian or spectrum as if it were a
background, and do not cancel the trace with a fitted constant.

The next materially distinct class is the smallest genuinely nonparallel
one-axis first jet. Freeze its jet support before solving, compute the complete
field equations and the metric source-graph adjoint together, and require any
trace cancellation to arise from the same action-owned carrier. A class-wide
negative is again valid.

No ledger verdict, canon, source ownership, residue, quotient datum or public
posture changes. No physical cohomology, particle assignment, prediction or
confirmation follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1_minimal_anisotropic_action_class_probe.py
```

The exact probe passes `32/32`.
