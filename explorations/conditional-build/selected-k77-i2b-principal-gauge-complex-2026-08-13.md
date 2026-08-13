---
artifact_type: construction_result
created: 2026-08-13
status: NONNULL_PRINCIPAL_GAUGE_COMPLEX_EXACT__RAW_NULL_COHOMOLOGY_168__FULL_WARD_AND_PHYSICAL_CARRIER_OPEN
run_id: RUN-20260813-104500-gu-i2b-principal-gauge-complex
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: SC-ACT-04
source_return: SOURCE_CONFIRMS_I2B_CONNECTION_AND_GAUGE_GRAMMAR__SOURCE_SILENT_EXACT_PRINCIPAL_COMPLEX_WARD_TOTALIZATION_AND_PHYSICAL_CARRIER_REDUCTION
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
fork_assumed: none
search_space_dim: "exact 14 -> 196 -> 196 -> 14 principal complex; cubic polynomial syzygy plus non-null and null orbit representatives decided wholesale"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
---

# Selected K77 I2B principal gauge complex

> **CORRECTION `I2B-PRINCIPAL-GAUGE-20260813`.** The exact polynomial
> syzygy and every reported rank survive, but the `14 -> 196` map is not the
> already-built source gauge map. Its domain is `Cl1` and it is the
> exact-form principal map `xi -> k tensor xi`; the source adjoint gauge map
> has domain `Cl2`, shape `196 x 91`, and projected rank `25`. The target
> annihilates that actual source gauge image while retaining the `(8/3)k`
> contraction with the exact-form map. Therefore the ordinary-gauge,
> lower-order Ward-obligation, and gauge-cohomology readings below are
> retracted. Read the `168/168` only as raw principal-symbol quotient
> dimensions. See
> `selected-k77-i2b-principal-degeneracy-retype-2026-08-13.md`.

## Result in plain English

The fourteen directions found in the previous two waves are not an arbitrary
new constraint space. Off the light cone, they are exactly the ordinary
connection-gauge directions. The principal Hessian sits in the complex

```text
gauge parameter 14 -> connection field 196 -> Euler equations 196
                   -> Ward identities 14,
```

and that complex is exact for both timelike and spacelike covectors.

On a null covector, the Hessian rank drops from `182` to `14`. After removing
the fourteen ordinary gauge directions, the raw field and equation symbol
cohomologies each have dimension `168`. The exact linearized Einstein
comparator has dimension `2` on each side. This is not a claim of 168 physical
particles. It is a quantitative burden on the missing physical carrier,
projector, coupled fields, or further BV reduction: they must remove or
reinterpret 166 null classes before this connection complex can reproduce the
Einstein propagating sector.

## Exact certificate

Let `G(k) xi = k tensor xi` be the ordinary connection-gauge symbol and `H(k)`
the selected I2B principal Hessian. The probe proves all twenty cubic
coefficients of

```text
H(k) G(k) = 0
```

vanish exactly. Since every Hessian block is symmetric, the dual identity
`G(k)^T H(k)=0` follows too.

```text
                         timelike   spacelike   null
rank G(k)                   14          14        14
rank H(k)                  182         182        14
field-symbol H^0             0           0       168
equation-symbol H^1          0           0       168

Einstein null H^0/H^1                              2/2
raw excess per side                                166
```

This also corrects the interpretation of arbitrary holonomic jets. The
combined `B00/B01` pointwise jet map is full rank `196`, but a rank-one Fourier
jet `k_mu k_nu a` is constrained by the gauge complex. Pointwise jet
surjectivity is therefore not mode-by-mode hyperbolicity or propagation.

## Lower-order Ward obligation

The isolated fourteen-cell target is not annihilated by the ordinary gauge
generator. Its contraction is exactly

```text
target^T G(k) = (8/3) (k_0,k_1,k_2,k_3,0,...,0).
```

This is **not yet a full Noether failure**. Differentiating an off-shell
Noether identity includes lower-order connection commutators and variations
of every moving field and reduction. The result says those omitted terms have
a precise obligation: they must totalize and cancel this `8/3` covector. If
the complete source action cannot do so, the selected background/ansatz is not
an admissible stationary branch.

## Hostile-review boundary

The review returns
`SCOPED_THEOREM__PRINCIPAL_GAUGE_COMPLEX_AND_RAW_NULL_BURDEN`. It rejects:

- calling the 168 classes particles or physical polarizations;
- transferring the Einstein `2` directly into the raw connection carrier;
- treating arbitrary second jets as a Fourier-mode solution;
- calling the isolated target contraction a complete Noether violation;
- inferring a domain, propagation theorem, presymplectic quotient, or BV phase
  space from symbol exactness.

## Source return and ledger disposition

The source supports the connection, gauge and I2B action grammar, but does not
print this exact principal complex, its null cohomology, the physical reduction
from 168 to the observed sector, or the required lower-order Ward
totalization. These are repository-derived obligations.

No ledger migration is booked. The current rows already name the physical
carrier, action-owner and observation/BV gaps; this theorem makes their
distance quantitative without changing verdict, residue, tightness, quotient
count, datum, canon or public posture.

## Next gate

Compute the complete linearized Ward identity for the actual selected source
action and moving background, including:

- the connection commutator/lower-order terms;
- moving `H_q`, reference connection, metric/section, Hodge/Shiab and
  observation responses;
- any source-owned coupled fermion/current contribution;
- the exact `8/3` target contraction as the firing obligation.

If it closes, induce the complex on the action-owned physical carrier and
recompute the null cohomology against the Einstein `2`. If it fails, the
selected background/ansatz—not merely a symbol—is ruled out at the tested
grade.
