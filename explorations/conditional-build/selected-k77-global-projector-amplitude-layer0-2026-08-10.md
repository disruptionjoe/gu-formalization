---
artifact_type: construction_composition_and_layer0_correction
created: 2026-08-10
status: GLOBAL_PROJECTOR_SCREENS_SHIFTS__DOES_NOT_SELECT_NONZERO_VEV_AMPLITUDE
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_SILENT_NORMALIZED_FUNCTIONAL_AND_AMPLITUDE_VALUE
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 global-projector / VEV-amplitude Layer-0 gate

## Result in plain English

The repository already had the first proposed global mechanism. Given a
normalized functional `ell`, it forms the constant-mode projector
`Pi0=1 tensor ell` and `Q=1-Pi0`. That construction really does screen an
independent constant shift of the source.

It does **not** choose the nonzero VEV amplitude left by ledger v0.142.
Composed with the exact family, `ell` merely reads the amplitude, while `Q`
annihilates every constant member. Requiring the physical VEV field itself to
lie in `im Q` forces the amplitude to zero. Requiring `ell(T)=c` selects the
amplitude, but selects exactly the supplied scalar `c`.

Thus screening and amplitude selection are separate construction burdens.
The next gate is not another projector. It is an action-owned,
amplitude-dependent global solvability/spectral condition—or an explicitly
typed external value—with the common domain built first. The existing
projector remains a valid conditional screening horn after its domain/measure
owner is supplied.

## Layer 0

| operation | what it accomplishes | what it does not accomplish |
|---|---|---|
| `Q rho` | removes independent constant source shifts | choose a nonzero VEV |
| `ell(T)` | reads the constant amplitude | provide its value |
| `T in im Q` | removes the constant mode, forcing `T=0` | retain dark-energy VEV |
| `ell(T)=c` | fixes `T=c` | derive `c` |
| Fredholm compatibility of `L R=Q rho` | guarantees the projected source is orthogonal to the constant kernel | add an equation depending on `T` |

The source explicitly does not publish `ell`, a zero-mode projector, a compact
domain, measure, observer window or amplitude value. These remain repository
constructions or external data, not Weinstein-derived objects.

## Exact composition

The local source family remains

```text
f=t^2/3,
u=-t/312-4t^2/3,
```

with rank-two source Jacobian and one-dimensional tangent. On the finite
transitive predecessor model,

```text
Pi0=(1/4)11^T,
Q=I-Pi0,
ell=(1/4)1^T.
```

For constant family fields `t1`, `f(t)1`, and `u(t)1`, `Q` sends all three to
zero, while `ell(t1)=t`. For any source `rho` and constant shift `delta`,

```text
(I+L)^(-1) Q (rho+delta 1) = (I+L)^(-1) Q rho.
```

The Fredholm compatibility condition `1^T Q rho=0` is an identity independent
of `t`; it cannot raise the family Jacobian rank. A planted global operator
`L+(t-5/17)Pi0` has determinant `16(t-5/17)` and does select `t=5/17`, proving
that the harness would detect a genuinely amplitude-dependent global gate.

## Efficient specialist review

- **Global analysis:** the existing projector closes source-shift
  compatibility, not amplitude selection. A selector must make the global
  operator or boundary condition depend on `t` nontrivially.
- **Variational bicomplex:** `ell(T)=c` is a third equation only after `c` and
  the functional owner are supplied; neither may hide in notation.
- **Symplectic/BV--BFV:** local branch symplectomorphism remains blind. A
  coupled global boundary charge may select only if it produces a new
  amplitude-dependent condition.
- **Krein/operator theory:** determinant, self-adjoint extension or stability
  can be tested only after one common closed domain exists.
- **Principal-bundle geometry:** a normalized `ell` must descend with the
  observation/domain data; the finite average is not automatically covariant.
- **Index theory:** removing a zero mode is not selecting its continuous
  value. Index jumps may choose sectors but need not choose scale.
- **Cosmology/EFT:** screening a vacuum shift is valuable even if the VEV
  magnitude remains external; the two claims must not be merged.
- **Constraint accounting:** `ell(T)=c` consumes the supplied scalar `c` unless
  another action-owned equation fixes it with positive surplus.

## Disposition and next gate

Verdict:

```text
GLOBAL_PROJECTOR_SCREENS_SHIFTS
GLOBAL_PROJECTOR_DOES_NOT_SELECT_NONZERO_VEV_AMPLITUDE
NORMALIZED_FUNCTIONAL_AND_VALUE_REMAIN_SEPARATE OWNERS
```

Next:

1. build the common global Green/Krein and bulk--boundary BV--BFV domain;
2. derive an action-owned amplitude-dependent solvability, determinant,
   boundary-charge or stability condition on that domain;
3. retain the explicit external-value horn and count its constraint surplus;
4. only after selection test observation Hilbert stress, vacuum-shift response
   and cosmology.

No canon verdict or public posture changes. P1/P2/P3 remain unassigned.
