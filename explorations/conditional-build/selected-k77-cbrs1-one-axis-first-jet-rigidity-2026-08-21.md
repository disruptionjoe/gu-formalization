---
title: "Selected-K77 CBRS-1 one-axis first-jet rigidity through transverse grades zero and one"
status: active_research
doc_type: exact_class_obstruction
created: "2026-08-21"
registry: lab/process/selected-k77-cbrs1-one-axis-first-jet-rigidity.json
probe: tests/channel-swings/selected_k77_cbrs1_one_axis_first_jet_rigidity_probe.py
grade: "EXACT NESTED A/B PLUS REPRESENTATIVE GRADE-ZERO/ONE DERIVATIVE-MODULE CLASS KILL; NOT A FULL CLIFFORD FIRST-JET THEOREM"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_AND_METX_ARGUMENT_GRAMMAR__REPO_DERIVES_AND_KILLS_THIS_REDUCED_JET_CLASS__SOURCE_SILENT_ON_THE_CLASS
canon_verdict_change: none
---

# Selected-K77 CBRS-1 one-axis first-jet rigidity through grades zero and one

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1B/C1 frozen one-axis a/b plus lowest transverse grade-zero/one first-jet rigidity and metric-trace class kill
carrier: Omega1_base_tensor_span{d_a,d_b,i1,gamma1_offdiag} at the K77 anisotropic point LAYER=ambient CHIRALITY=N/A
pairing: K77 Clifford scalar-density pairing ON=Omega1_Cl77
real_structure: K77 real u(64,64) comparator
grading: exterior degree and Clifford parity
action_owner: repository-construction
target: stationary-scheme tangent and intrinsic metric covector MAP-TYPE=evaluation
```

## Result first

The smallest derivative-bearing successor to CBRS-1A does not contain a
genuinely nonparallel on-shell first jet.

Keep the already frozen one-versus-thirteen Clifford support, but allow its
two coefficients to vary along one labelled base coordinate `s`:

```text
T(s) = a(s) e^0 gamma_0 + b(s) sum_(i=1)^13 e^i gamma_i.
B(s)=0,  partial_s B=0.
```

The zero connection value and jet are inherited parts of the CBRS-1A frozen
class, not conclusions about every canonical `B_Z` branch.

The selected action remains

```text
I(a,b) = a^2/2 + 312 a b^2 + 1144 b^3 + 13 b^2/2.
```

At the exact anisotropic point `(a,b)=(-13/96,1/48)`, the first prolongation
of the field equations is

```text
[ 1    13  ] [a'] = [0]
[13  143/2] [b']   [0].
```

The determinant is `-195/2`, so the only on-shell first jet in this frozen
derivative module is

```text
a'=b'=0.
```

This is not just a reduced-equation shortcut. Exact differentiation of the
complete `14 x 16,384 = 229,376`-direction symbolic action covector gives two
fourteen-cell derivative columns. Their restriction to the frozen `a/b`
tangent is exactly the matrix above and has rank two. A nonzero planted jet
fires the complete covector, while a deliberately singular Hessian plant
retains its expected nonzero tangent.

The predeclared transverse fallback then closes the two lowest Clifford
grades. Add `c(s) i1` in the pinned form slot (the real-form grade-zero basis)
and the lexicographically first off-diagonal grade-one cell
`d(s) gamma_1` in that same slot. The nested prolonged matrix is

```text
[ 1    13     0     0  ]
[13  143/2    0     0  ]
[ 0     0    -1     0  ]
[ 0     0     0   -1/3 ].
```

It has determinant `-65/2` and rank four, so the nested carrier forces
`a'=b'=c'=d'=0`. The scalar and off-diagonal-vector derivative columns have
exact supports one and two; independent planted jets fire both. This closes
the lowest transverse grades without claiming a full Clifford Hessian.

Because field stationarity forces every admitted nested jet to zero, the fixed-`varpi`
source momentum derivative and its metric-graph formal adjoint are zero on
the whole class. The held-out density remains `221/55296`, leaving the same
nonzero four-cell intrinsic `MET(X)` row as CBRS-1A. The class therefore closes
before full Hessian, stabilizer, `mu6`, `J`/Higgs, photon, extra-`U(1)`, or
gravitational-spectrum work is admissible.

## What “first jet” means here

A written affine function is not automatically an on-shell formal jet. A
formal first jet of a solution must satisfy the first prolongation of every
field equation. The invertible Hessian proves that the anisotropic stationary
point is isolated inside this two-coefficient orbit, so a curve of stationary
points cannot leave it to first order.

The same reduced stationary scheme contains exactly three rational points:

| point | Hessian determinant |
| --- | ---: |
| `(0,0)` | `13` |
| `(-1/312,-1/312)` | `-15` |
| `(-13/96,1/48)` | `-195/2` |

All three are nonsingular. Thus no reduced one-axis profile can move through
any of them while remaining pointwise stationary. The complete-covector
cross-check is executed at the new anisotropic point, which is the only CBRS-1A
branch at issue.

## Held-out metric return

CC-01 is binding: `MET(X)` is an action argument, not background furniture.
For the frozen carrier, the intrinsic fixed-`varpi` first variation is

```text
E_g = rho I + (D_g B_Z)^! (E_B-E_T).
```

The only on-shell jet in the nested `a/b` plus grade-zero/one carrier is zero,
so the second term has no derivative source in this module. The normalized
metric row remains

```text
(-221/27648,0,0,0,221/27648,0,0,221/27648,0,221/27648),
```

and is nonzero. No counterterm, target-facing coefficient, or individual
ledger row was used to select the carrier or adjudicate the trace.

## Prior-art and scope fence

The August 14 SR-1D parity and cokernel results exhaust first- and second-jet
freedom over a different canonical point carrier,
`T=t Phi1` with its fixed `B_Z` branch. They do not decide the new anisotropic
point. This result does not replay them: it computes the tangent scheme and
complete covector derivative of the CBRS-1A orbit itself.

The class kill is exactly this nested carrier:

```text
one labelled base axis
times
the frozen two-coefficient a/b derivative module plus one target-blind
grade-zero scalar and one off-diagonal grade-one representative
at
(a,b)=(-13/96,1/48).
```

It is not a theorem over arbitrary Clifford-valued first jets, grade-two and
higher coefficient modules, distinct point carriers, alternative
source-derived Zorro reconstructions, or source-global
solutions. In particular, the full Clifford coefficient space can have
transverse Hessian directions invisible to the reduced `a/b` block.

## Hostile return

- **Strongest overclaim:** invertibility of the reduced Hessian does not prove
  invertibility of the full `229,376`-direction Hessian. The probe checks the
  complete covector only on the declared two-dimensional derivative module.
- **Strongest contrary route:** grade two is the first untested transverse
  grade. It is connection-algebra-valued, so its `T` motion cannot be tested
  honestly without moving the connection/gauge owner on the same carrier. A
  transverse zero mode could create a genuine first jet and a nonzero
  source-graph return.
- **Weakest propagation seam:** the metric graph zero follows because the
  frozen class has no nonzero on-shell field jet; it is not a universal
  factorization theorem for every K77 connection graph.
- **Source ceiling:** the action and `MET(X)` grammar are source-aligned; this
  carrier, exact tangent calculation, and class disposition are repository
  reconstruction results.

## Reverse-scaffold consequence

CBRS-1A through CBRS-1C1 now close the constant orbit, its full `a/b` tangent,
and the two lowest representative transverse Clifford grades. Do not spend a
second jet, Hessian, stabilizer, or spectrum calculation on those carriers.

The next materially distinct class is `CBRS-1D`: freeze one labelled base axis
and the smallest grade-two connection-algebra direction transverse to the
closed carriers. Move `T` and the connection/gauge owner together, then
compute the complete field-covector derivative, primitive-epsilon equation,
and intrinsic metric source graph before allowing second jets. If every
target-blind transverse direction is rigid or retains the metric trace, a
class-wide negative is again valid.

No ledger verdict, source ownership, canon, residue, quotient datum, or public
posture changes. No physical vacuum, particle assignment, cohomology,
prediction, or confirmation follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1_one_axis_first_jet_rigidity_probe.py
```

The exact probe passes `41/41`.
