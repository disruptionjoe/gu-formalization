---
artifact_type: conditional_build_correction
created: 2026-08-07
status: GCR_WRONG_CLIFFORD_GRADE_AND_DIRECT_INPUT_TYPE__ODD_TORSION_TRANSLATION_CURVATURE_OR_SOLDERING_OWNER_REQUIRED
source_return: SOURCE-CONFIRMS__GAUSS_COMPATIBLE_TWO_CONNECTION_ARENA__SOURCE_SILENT__K77_GCR_TO_ODD_CURVATURE_OWNER_MAP
ledger: lab/process/conditional-physics-ledger-v0.49.json
canon_verdict_change: none
---

# Selected second-layer GCR exterior-degree owner retype

## Result in plain English

The `117` coefficients isolated in v0.48 are **not directly
Gauss--Codazzi--Ricci curvature**. In fact, neither are the other `28`
coefficients, in the literal carrier used by that calculation.

The reason is a Layer-0 type distinction. Ordinary Levi-Civita/GCR curvature
is a bivector-valued two-form: in the Clifford model it is `Cl2`-valued. The
four v0.48 inverse-Shiab packets are vector-valued two-forms: they are
`Cl1`-valued. On the selected `comm/symi/symi` Shiab, that difference is
decisive:

```text
all Cl2-valued curvature inputs: 91 x 91 = 8,281 basis columns
their selected-Shiab output grades: Cl1 and Cl5 only
their output in the required Cl2 target: exactly zero

v0.48 Cl1-valued inputs: 91 x 14 = 1,274 dimensions
their selected-Shiab Cl2 map: exact rank-1,274 isomorphism
required inverse support: 145 = 28 + 117
```

So the previous mathematical split remains exact, but its owner must be
retyped. It is an odd/vector-valued curvature packet--the type occupied by
torsion or translational curvature in Cartan language--not direct
Levi-Civita GCR curvature. Weinstein's gauge-rotated Levi-Civita prescription
still tells us which two-connection geometry to use; it does not turn an even
curvature bivector into this odd packet.

The cheapest repair also fails. Contracting a `Cl2` curvature value with the
same non-null `q` produces only vectors perpendicular to `q`. Every one of the
four required packets has exactly seven nonzero `q`-direction Clifford
components. A single `gamma(q)`/contraction adapter therefore cannot supply
the packet. The next build must construct either the source-native odd
augmented-torsion/translational-curvature block or a richer moving
epsilon/soldering map.

## Layer 0

| phrase | object tested | object kept distinct |
| --- | --- | --- |
| GCR curvature | `Lambda2 T*Y tensor Cl2`, with an antisymmetric curvature-value pair | v0.48's `Lambda2 T*Y tensor Cl1` inverse packet |
| HN/NN | type of the exterior two-form pair in v0.48 | tangent/normal type of the curvature-value indices in Gauss, Codazzi or Ricci |
| pair exchange | Riemann symmetry exchanging two antisymmetric pairs | an operation available after the value pair has been reduced to one vector index |
| odd packet | vector-valued two-form, torsion/translation-curvature **type** | a source-derived identification with GU augmented torsion |
| q adapter | contraction of a bivector with one fixed non-null covector | a moving, equivariant epsilon/soldering construction |
| old GCR files | `(9,5)` tensor reconstruction on the frame bundle | the current K77 selected Clifford carrier |

This is the precise sense in which controls can pass while the question is
wrong. v0.48 correctly computed a Koszul split of the packet it named. Layer 0
now shows that “GCR” denoted the wrong value grade for that packet.

## Exact calculation

The selected Shiab contains Clifford multiplication by odd total parity. It
therefore flips Clifford parity. The probe does not rely only on that abstract
observation: it evaluates every one of the `91 x 91 = 8,281` basis elements of
the complete `Cl2`-valued curvature carrier. Every column is nonzero, every
output lies in grades one or five, and the number of grade-two target entries
is exactly zero.

The four required correction targets are nonzero and entirely grade two. The
complete `Cl1 -> Cl2` map used by v0.47/v0.48 remains the exact rank-1,274
isomorphism already certified. Thus the direct image intersection is zero by
grade, not by a numerical accident or an incomplete sample.

The exterior-slot audit reaches the same warning from another direction. All
145 inverse coefficients use `HN` or `NN` exterior pairs; none uses a direct
`HH` pulled-back curvature pair. Riemann pair symmetry can rewrite some GCR
components with mixed exterior inputs, but only while a second antisymmetric
value pair is still present. The current `Cl1` value has no such pair. HN/NN
labels therefore cannot be promoted to Codazzi/Ricci names.

Finally, for non-null `q`,

```text
i_q : Lambda2 V -> q-perp
```

has rank thirteen and cannot produce the `q` direction. The four exact inverse
packets each contain seven nonzero Clifford-`q` entries. The grade-one part of
`gamma(q)F` is the same contraction, while its other part is grade three, so
the one-vector repair is excluded exactly.

## What survives from the older GCR work

The older files remain useful geometry, not a current owner certificate.

- `H21-theta-equals-II` proves the graph Gauss identity in the canonical
  ambient Levi-Civita gauge, but explicitly leaves the
  `SO(9,5) -> Sp(64)` spin-lift/bundle identification unbuilt.
- `pc2-gauss-y14-curvature` writes Gauss, Codazzi and Ricci components for the
  `(9,5)` gimmel reconstruction and retains the full Riemann value pair.
- the current lane has settled on K77 and the selected residual calculation
  has already restricted to a `Cl1` source bank.

Porting those formulas therefore requires a new typed map; their familiar
names do not fill it in.

## Source return

```text
SOURCE-CONFIRMS:
  the gauge-rotated Levi-Civita/two-connection arena and a Gauss-compatible
  connection locus.

SOURCE-SILENT:
  the K77 map from even Levi-Civita/GCR curvature into the required odd
  curvature packet, and the exact 145 packet coefficients.
```

Curt's source record separately says ordinary torsion is a vector-valued
two-form. That supports the type analogy only. It does not establish that the
v0.48 packet is GU's augmented torsion, which the source types as a difference
of connections rather than as this two-form.

## Specialist and hostile review

- **Differential geometry:** direct GCR ownership fails at the curvature-value
  grade. Pair exchange cannot be used after deleting the second antisymmetric
  pair.
- **Representation theory:** the `Cl2 -> odd` parity calculation exhausts all
  8,281 basis columns; no dimension-only inference is used.
- **Variational PDE/hyperbolic equations:** the result retypes the principal
  source carrier. It is not the nonlinear covariant Bianchi identity or a
  characteristic-domain result.
- **Symplectic geometry:** no Euler covector, presymplectic current,
  characteristic quotient or BFV phase space follows from the grade fence.
- **Krein/operator theory:** the finite exact carrier result says nothing
  about positivity, self-adjointness or a common closed domain.
- **Source criticism:** the source selects the arena but is silent on the
  degree-changing map and coefficients.
- **Repo archaeology:** the old GCR files were found and used to locate the
  missing bundle/grade map; their `(9,5)` tensor result was not silently ported.

Both two-sided hostile charges fire. The summary must not rename a
vector-valued packet “GCR,” and the lane must not keep hardening that owner
merely because the Koszul calculation itself was exact.

## Progress and fences

```text
Ledger v0.49 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - direct Levi-Civita/GCR Cl2 owner excluded for the required Cl2 target
  - all 8,281 selected Cl2 source columns grade-classified exactly
  - the single-q contraction/gamma adapter excluded
frontier_conditions_opened: 1
  - source-native odd augmented-torsion/translation-curvature or richer
    epsilon/soldering owner map
remaining_named_conditions: 5
  - source-native odd owner map and coefficientwise packet match
  - null characteristic screen and continuation
  - total nonlinear Bianchi and raw-Upsilon naturality
  - scalar and massless physical constraint quotient
  - coupled fermion Hessian and common domain
```

No Euler equation, scalar pole, cosmological magnitude, fifth quotient,
external datum, canon verdict or public posture changes. P1/P2/P3 remain
unused. Curt remains formally separate and no third lane is promoted.

## Next gate

Construct the source-native odd/vector-valued curvature block generated by the
full augmented-torsion/two-connection geometry, or construct a richer moving
epsilon/soldering map from the even GCR block into that odd carrier. Compare it
coefficientwise with all 145 exact inverse-Shiab coefficients. Only after that
match may the completed packet be tested against total covariant Bianchi and
raw-`Upsilon` naturality. Keep the null screen separate.

The executable probe passes `41/41`, including the exhaustive 8,281-column
grade audit and planted failures against GCR relabelling, `(9,5)` transfer,
single-`q` repair, BV/BFV inflation and datum substitution.
