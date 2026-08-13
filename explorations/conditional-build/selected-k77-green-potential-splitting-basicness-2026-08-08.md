---
artifact_type: build_result_and_scope_narrowing
created: 2026-08-08
status: SPLITTING_BASIC_EXACT_AT_COTANGENT_GRADE__CONTACT_AND_PHYSICAL_GAUGE_BASICNESS_OPEN
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 Green-potential splitting/basicness

## Result in plain English

The apparent need for a new vertical B/T connection has narrowed sharply.

The seven owner buckets from v0.66 changed when the field frame changed. That
did **not** mean the complete Green potential changed. It meant the earlier
bookkeeping retained the field-sector term while omitting the compensating
momentum conjugate to the metric-normal coordinate.

For an invertible field-frame change `v=R(n)y`, the complete boundary
one-form is

```text
Theta = p_v^T delta v + pi^T delta n.
```

Its exact cotangent lift is

```text
p_y       = R^T p_v,
pi'_a     = pi_a + p_v^T (partial_a R)y.
```

Then

```text
p_v^T delta v + pi^T delta n
  = p_y^T delta y + (pi')^T delta n
```

coefficientwise. The field and normal/base terms exchange, while the complete
one-form is unchanged. Its field-space exterior derivative is therefore also
unchanged. A nonlinear three-chart calculation verifies the cocycle exactly,
and the actual ten K77 normal generators give ten nonzero compensating normal
momenta. Freezing or deleting those momenta produces the preregistered live
defect.

So a vertical B/T connection is **not required merely to descend through a
pointwise field-frame trivialization**. The next construction is the actual
selected-action presymplectic coefficient current, including any
derivative-dependent Levi-Civita/soldering/observation contact terms. Physical
gauge basicness, polarization, a common domain and BV/BFV remain separate.

## 1. Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| splitting change | pointwise field-frame coordinate change over the metric fibre | derivative-dependent/contact transformation involving spacetime jets |
| complete Green potential | field-space one-form with field and metric-normal cotangent components | field-sector boundary term alone |
| splitting basicness | equality on overlapping coordinate trivializations | horizontality/invariance under physical gauge directions |
| presymplectic current | field-space exterior derivative of the complete local potential | reduced BFV phase space, polarization or charge |
| normal momentum | cotangent chain-rule term already owned by full first variation | new field, coupling or external datum |

This Layer-0 split is load-bearing. A missing field-sector term is a real
defect only if the corresponding normal/base cotangent term is also included.
Conversely, coordinate naturality does not establish gauge reduction.

## 2. Source return

The checked Weinstein material owns the upstairs connection difference and
places the gauge-rotated Levi-Civita connection in the augmented-torsion
reference slot. It does not state a field-space cotangent-lift theorem or a
vertical B/T connection selecting the v0.66 buckets.

```text
SOURCE-SILENT:
  field-space splitting and the cotangent transformation of its Green owner.

REPO-DERIVES:
  exact cotangent-lift naturality, the three-splitting cocycle, and the
  all-ten-K77 normal-momentum correction.
```

The silence is harmless for point-trivialization descent because this is a
coordinate theorem, not a new dynamical axiom. It does not license importing
the gauge-rotated Levi-Civita as a field-space connection.

## 3. Exact nonlinear theorem

The main certificate uses a nonlinear determinant-one frame

```text
R(n0,n1) = [[1,n0,n0*n1],
            [0, 1,n1],
            [0, 0, 1]].
```

The full configuration Jacobian and its cotangent lift are computed
symbolically over rationals. The pulled-back canonical Green one-form equals
the new-coordinate one-form exactly. The complete phase Jacobian preserves
the canonical antisymmetric matrix exactly. Two planted alternatives fail:

- retain only the field momentum and omit the induced normal momentum;
- move the configuration while freezing all conjugate momenta.

A second nonlinear frame is composed with the first. Both the configuration
Jacobians and cotangent momenta satisfy the direct-versus-composed three-chart
cocycle.

## 4. Actual K77 specialization

The exact v0.67 K77 bank supplies ten compensators

```text
A_a = -(1/2) G_Y^-1 (partial_a G_Y).
```

At the preregistered dense rational field and covector, every correction

```text
sigma_a = p^T A_a y
```

is nonzero. The complete `10+14` tangent transition has determinant one and
rank 24; its cotangent lift has rank 48 and preserves the canonical
presymplectic form. Freezing the momentum transform fails exactly.

This uses all ten normal directions rather than the old sampled fixture. The
argument requires nondegeneracy, not positive definiteness; K77 inertia
remains `(7,7)`.

## 5. What moved and what remains

Closed:

- point-field-frame splitting naturality of the complete Green one-form;
- splitting naturality of its field-space exterior derivative;
- the conditional horn requiring a vertical B/T connection merely to repair
  that coordinate change.

Open:

- coefficientwise assembly of the actual selected-action K77 presymplectic
  current;
- derivative-dependent/contact terms from the physical
  Levi-Civita/soldering/observation map;
- contraction and Lie-derivative tests on physical gauge directions;
- polarization, common Krein/Green domain, BV/BFV and charges.

No verdict, residue, quotient, P1/P2/P3, canon or public posture moves.

## 6. Symplectic and hostile review

- **Symplectic geometry:** equality of the complete one-form is the strongest
  local route; its exterior derivative follows functorially.
- **Differential geometry:** a cotangent lift removes coordinate dependence
  without selecting a connection. Contact transformations remain separately
  typed.
- **Variational PDE:** the normal/base momentum is part of the full first
  variation and cannot be dropped from the Green boundary owner.
- **Krein/operator theory:** no positivity, self-adjoint domain or energy
  conclusion is used.
- **Source criticism:** Weinstein's Levi-Civita statement is retained at its
  published locus and not promoted into the missing field-space object.

Both standing hostile charges fire:

1. **Summary outruns artifact:** “the Green potential is physically basic” is
   rejected. Only point-trivialization naturality is proved.
2. **Artifact defends a superseded object:** the partial seven-bucket
   potential is not repaired; it is replaced by the complete cotangent one-form.

## 7. Progress meter

```text
Ledger v0.68 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Next:

`SELECTED_ACTION_K77_PRESYMPLECTIC_COEFFICIENT_ASSEMBLY_WITH_CONTACT_TERMS__THEN_PHYSICAL_GAUGE_BASICNESS_POLARIZATION_COMMON_DOMAIN`.

Main probe: `38/38 PASS`. Independent Sage/QQ: `PASS`.
