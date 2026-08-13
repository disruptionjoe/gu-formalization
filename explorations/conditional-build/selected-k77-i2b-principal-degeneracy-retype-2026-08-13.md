---
artifact_type: correction_result
created: 2026-08-13
status: PRINCIPAL_DIFFERENTIAL_COMPLEX_EXACT__GAUGE_NOETHER_INTERPRETATION_RETRACTED
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_TILTED_GRAPH_INDEPENDENT_VARPI_AND_ADJOINT_GAUGE_GRAMMAR__SOURCE_SILENT_CL1_EXACT_FORM_GAUGE_SYMMETRY
canon_verdict_change: none
fork_assumed: none
search_space_dim: "two exact linear maps into the same 196-real bank: 196x14 Cl1 exact-form and 196x91 Cl2 adjoint source gauge; decided wholesale"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
---

# Selected K77 I2B principal-degeneracy retype

## Result in plain English

The previous wave found a real and useful mathematical structure, but gave it
the wrong physical name.

The exact `14 -> 196` map is the differential map

```text
Cl1-valued scalar xi  ->  k tensor xi.
```

It generates the complete non-null kernel of the principal Hessian. But the
source's already-built infinitesimal gauge action is a different map:

```text
Cl2 Spin parameter zeta  ->  [T,zeta]
R^91                     ->  R^196,
```

whose selected image has rank `25`. Different domains, transformation laws
and ranks mean there is no invertible adapter identifying them. The
predecessor's exact polynomial identity was sound; calling it ordinary gauge
was not.

## The decisive Ward comparison

On the same fourteen-cell Euler target, the two maps behave oppositely:

```text
target^T G_source = 0,
target^T K_exact-form(k) = (8/3) k.
```

Thus the source Ward identity already annihilates the target at this selected
grade. The nonzero `(8/3)k` contraction is with a map that has not been derived
as a source symmetry. It creates no lower-order Ward-cancellation obligation.
Lower-order terms are permitted to lift that accidental principal degeneracy,
just as a zero-order term can lift a kinetic operator's principal kernel,
without violating source gauge covariance.

## What survives and what is retracted

Survives exactly:

- every coefficient of the principal syzygy `H(k)K(k)=0`;
- non-null ranks `rank K=14`, `rank H=182` and exactness of the raw
  differential complex;
- the null rank jump `rank H=14`;
- raw null quotient dimensions `168/168`;
- the timelike/mixed holonomic image and constraint-quotient results.

Retracted:

- identification of `K(k)` with ordinary connection gauge;
- the claim that `(8/3)k` must be canceled by a lower-order Ward identity;
- the labels "field/equation gauge cohomology" for `168/168`;
- the exact `166` difference from Einstein as a required physical reduction
  count. Einstein `2/2` remains a comparator, but the two quotients are not yet
  taken by the same action-owned gauge complex.

## Hostile review

The predecessor summary outran its artifact by naming a kernel from its shape
rather than comparing it to the already-filed source map. Rigor then defended
the mistyped object by demanding a Ward cancellation for a direction that was
never shown to be gauge. The correction is narrower than rejecting the
principal theorem: it preserves all exact algebra and retracts only the
physical disposition.

No source claim is killed. `SC-ACT-04` owns the residual-square grammar, while
the source remains silent on a `Cl1`-valued zero-form gauge symmetry for this
selected bank.

## Accounting

No ledger migration is needed. The affected rows already require the complete
action, physical carrier and BV/analytic reduction. No residue, quotient,
datum, canon verdict or public posture moves. Correction
`I2B-PRINCIPAL-GAUGE-20260813` is registered so future agents do not replay
the name error.

## Verification

`selected_k77_i2b_principal_degeneracy_retype_probe.py` passes `48/48` under
the pinned SymPy/NumPy environment. It replays both exact constructions,
checks their carrier/domain/rank fingerprints, verifies both target
contractions, and reruns the principal syzygy on timelike, spacelike and null
representatives.

## Next gate

Assemble the complete lower-order Hessian/characteristic complex and determine
which part of the principal exact-form kernel survives. Then induce the actual
source rank-25 adjoint gauge/BV distribution on the action-owned physical
carrier and recompute the null quotient. Keep the independently varied
`varpi/T` Euler equation, nonlinear Bianchi/atlas realization, observation
contact, preboundary class and analytic domain separate.
