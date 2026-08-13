---
title: "Selected K77 primitive-epsilon common residual bank"
status: conditional_build
doc_type: exploration
created: "2026-08-08"
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
canon_verdict_change: none
---

# Selected K77 primitive-epsilon common residual bank

## Result

The source-owned primitive `epsilon` field can now be placed on the same
principal residual-coordinate bank as the metric and independent connection.
On the conditionally selected Spin-native K77 action parent, its infinitesimal
field `eta` has all `91` bivector directions of `spin(7,7)`. At fixed
independent `varpi`, its principal response is

```text
delta_epsilon T = -q eta,
delta_epsilon F_varpi = 0.
```

Appending those directions to the ten metric and twenty-four connection
variables gives a `125`-field principal tangent. Its exact raw ranks are
`110/110/110` for timelike, spacelike and null covectors. The induced
stationary norm-square Gram ranks and inertias are

| stratum | raw rank | Gram rank | inertia (+,-,0) | doubled quotient |
|---|---:|---:|---:|---:|
| timelike | 110 | 110 | (58,52,15) | 220 |
| spacelike | 110 | 110 | (53,57,15) | 220 |
| null | 110 | 16 | (10,6,109) | 32 |

The primitive epsilon image has rank `91`. The metric bank contributes six
additional transverse directions rather than lying inside epsilon, and the
curvature part of the connection contributes thirteen more. Fifteen field
directions are in the raw kernel on every causal stratum. At a null covector,
another `94` directions in the raw image become isotropic for `K_loc`.

This closes the missing **principal** primitive-epsilon bank on the selected
Spin-native horn. It does not close the full action. The available normalized
first-action Schur symbol acts on only `34` fields; it cannot be added to this
`125`-field second-action symbol. The lower-order moving-Shiab response
`delta Phi_i=[Phi_i,eta]` is source-owned but still not serialized on the
common coefficient bank. Those are the next two construction obligations.

## Layer 0

| phrase | exact object | disposition |
|---|---|---|
| primitive source epsilon | independent H-valued action field; selected tangent `spin(7,7)` | principal 91-column bank exact |
| physical epsilon/Kosmann orbit | four dependent diffeomorphism columns | already exact; not substituted here |
| gamma-soldered epsilon | source-silent grade-one four-column construction | separate conditional comparator |
| `Xi=D_omega Upsilon` | exterior-covariant redundant equation | not `D_epsilon Upsilon` |
| principal epsilon response | derivative term `-q eta` in augmented torsion | exact here |
| complete epsilon Frechet response | principal response plus moving Shiab and other lower-order coefficients | open |
| selected Spin-native action | grade-1+2+5 action parent, with 91 epsilon directions | conditional horn used here |
| two `U(32,32)` halves | Weyl-half product comparator | retained separately |
| full `U(64,64)` | expanded unitary comparator | retained separately |

This corrects the queue without rewriting history: the primitive epsilon row,
Euler chain and compact Green owner already existed. What was missing was its
serialization on the actual K77 residual bank.

## What the exact ranks mean

The non-null result is strong but local: `K_loc` is nondegenerate when
restricted to the 110-dimensional raw image. The fifteen null field directions
therefore come from redundancy in the principal field-to-residual map, not
additional Krein isotropy.

The null stratum is radically different. The raw rank remains 110, but the
Gram rank falls to 16. Thus `94` live residual-image directions are isotropic.
The old partial null quotient dimension `28` becomes `32`, while the non-null
diagnostic grows from `44` to `220`. No fixed-rank boundary bundle can be
inferred across the null cone.

These doubled dimensions remain unbooked diagnostics. A quotient by the
computed radical is not yet a gauge/BV quotient, an edge phase space, a
maximal domain or a physical state space.

## First-action and action-parent obstruction

The next action-layer composition is now blocked for a concrete reason rather
than a vague missing-object label:

```text
available first-action source tangent = 34 fields
epsilon-complete second-action tangent = 125 fields
```

The old first-action symbol must be rederived on the same selected stationary
background with the primitive epsilon directions and their lower-order
moving-Shiab coefficients. Padding it with zeros would assume that epsilon is
pure gauge before the action-derived BV differential exists.

This wave also does not decide the larger action parent. The source's frame
group can be read as the full `U(64,64)` extension, while Curt's exposition
also presents two `U(32,32)` Weyl halves. The selected Spin-native 91-column
bank is exact on its declared horn; it is not evidence that the expanded
parents reduce to it.

## Specialist and hostile return

- **Variational bicomplex/PDE:** the complete stationary Hessian requires the
  same field tangent and background in both action layers. The 34-versus-125
  mismatch forbids direct addition.
- **Symplectic geometry:** the `220/220/32` doubled radical quotients are not
  BFV phase spaces until an action-derived trace soldering/Legendre map and
  characteristic differential exist.
- **Krein/operator:** exact inertia closes the finite coefficient question,
  not the field Riesz, tangential operator, collar or maximal domain.
- **Microlocal:** the 94-dimensional null isotropic excess makes a stratified
  characteristic treatment mandatory.
- **Real Clifford:** all decisive ranks are exact over the real K77 carrier;
  complexification was not used for signature-sensitive data.
- **Complex/path-integral:** no contour, measure, determinant or reflection
  positivity is selected.
- **Source:** `SOURCE-CONFIRMS` primitive epsilon and moving-Shiab grammar;
  `SOURCE-SILENT` on this K77 bank, action-parent selection and shared
  first-action symbol.
- **Accounting:** no new field, coefficient, quotient, external datum or
  parameter is introduced. P1/P2/P3 remain unused.

The hostile review keeps the conclusion principal and horn-scoped. It rejects
calling this the full nonlinear `D_epsilon Upsilon`, rejects zero-padding the
first action, and rejects promotion of a finite radical quotient to BFV.

## Progress and next gate

Ledger v0.105 remains `82/82`, with verdict counts `32/19/26/5`, residue
`84..86`, nine forks and five booked scoped quotients. Four conditions close:
the selected primitive epsilon principal bank, its overlap decomposition, its
causal Gram strata and the exact 34-versus-125 first-action mismatch. One
condition opens explicitly: full lower-order epsilon plus the enlarged
first-action stationary bank.

Next build the lower-order moving-Shiab epsilon columns and recompute the
first-action Hessian on the same 125-field stationary fixture. Then derive the
action-owned BV differential/characteristic quotient before attempting edge
trace soldering, a tangential/collar maximal domain and odd BFV/BRST/CME.
Expanded action parents and the charged boundary horn remain separate.

## Receipts

- Primary exact route:
  `tests/channel-swings/selected_k77_primitive_epsilon_common_bank_probe.py`
  — `52/52 PASS`.
- Independent Sage/FLINT route:
  `tests/channel-swings/selected_k77_primitive_epsilon_common_bank_independent.sage`
  — `31/31 PASS`.
- Hostile review:
  `lab/process/hostile-reviews/2026-08-08-selected-k77-primitive-epsilon-common-bank-review.md`.
