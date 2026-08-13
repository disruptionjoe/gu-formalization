---
artifact_type: conditional_build_result
created: 2026-08-07
status: SELECTED_SHIAB_ISOMORPHISM__SPLIT_PREIMAGES_NOT_PRINCIPAL_BIANCHI__TOTAL_GCR_COMPLETION_REQUIRED
source_return: SOURCE-CONFIRMS__RAW_UPSILON_EQUIVARIANCE_INTENT__SOURCE-SILENT__GAUSS_CODAZZI_RICCI_SPLIT_COEFFICIENTS_AND_BACKGROUND_COMPLETION
ledger: lab/process/conditional-physics-ledger-v0.47.json
canon_verdict_change: none
---

# Selected second-layer Shiab inverse and Bianchi completion

## Result in plain English

The four corrections found in v0.46 fit perfectly inside the selected
curvature carrier, and in fact they fit there **uniquely**. But none of those
four unique objects can, by itself, be the first derivative of a connection
curvature along any nonzero fourteen-dimensional wave direction.

That is not a no-go for the completed GU geometry. It says the attempted
identification was one layer too early. The conditional full-`II`/Gauss term
and its compensating term are split pieces of one total curvature response.
A split piece need not obey differential Bianchi alone; Gauss, Codazzi, Ricci,
connection, Hodge, Shiab and graph motion must be assembled before testing the
total. The next Build therefore constructs that complete packet rather than
calling the inverse carrier representative `j1(L_xi A)`.

```text
full selected Hodge-Shiab map: 1274 x 1274, exact rank 1274
unique correction supports:   58, 29, 29, 29
q-wedge ranks:                 14, 14, 14, 14
common q-wedge rank:           14
nonzero common q:              none
```

No external datum can fix this: the missing information is an action- and
geometry-owned derivative, not a free sign, count or parameter.

## Layer 0

| phrase | object tested | object kept distinct |
| --- | --- | --- |
| curvature carrier | `Lambda^2 T*Y tensor Cl_1` before the selected Hodge-Shiab | a connection-curvature first jet |
| conditional Gauss response | full-`II` contribution to the selected raw residual | total Gauss-Codazzi-Ricci curvature packet |
| differential Bianchi | flat/principal-symbol condition `q wedge F=0` | nonlinear covariant Bianchi with background commutators and lower terms |
| unique preimage | inverse under the selected `comm/symi/symi` map | source ownership of that preimage |
| zero total pure-gauge response | exact cancellation of complementary split pieces | Einstein recovery, physical quotient or spectrum |

The control that matters is not another rank comparison at the residual
output. A lawful first-prolonged curvature must lie in the image of
`a -> q wedge a`, hence must satisfy `q wedge F=0`. Carrier containment alone
does not impose that integrability condition.

## Source return

The source displays the raw bosonic residual and states the equivariance
intent. It does not print this selected product as Weinstein's preferred
historical selector, the required Gauss-Codazzi-Ricci coefficient split, or a
background connection at which the full nonlinear Bianchi terms can be
assembled.

```text
SOURCE-CONFIRMS:
  raw Upsilon and the demand that its completed construction transform
  equivariantly.

SOURCE-SILENT:
  the selected split coefficients, their Gauss-Codazzi-Ricci completion and
  the background/lower-order terms needed for nonlinear covariant Bianchi.
```

This is a source return, not source deference: the exact test decides that the
repo's split carrier representative is not itself a principal connection jet.

## Exact construction

Let

\[
 S:\Lambda^2T^*Y\otimes \mathrm{Cl}_1
   \longrightarrow T^*Y\otimes \mathrm{Cl}_2
\]

be the previously selected `comm/symi/symi` Shiab followed by the Hodge
primalization. Both source and target have dimension
`91 x 14 = 1,274`. The probe constructs all 1,274 columns and proves

\[
 \operatorname{rank}S=1274.
\]

Thus every selected residual column has at most one curvature preimage. The
rank-1,190 mixed-normal bank already contains all four v0.46 correction
columns. Exact elimination gives unique real-rational preimages with support
sizes `58, 29, 29, 29`, and coefficientwise reconstruction returns the four
targets exactly. Full-map injectivity proves that no tangential or other
kernel addition can replace them with alternate representatives.

For each Cl1-valued two-form `F_alpha`, the probe constructs the exact linear
map

\[
 B_{F_\alpha}:q\longmapsto q\wedge F_\alpha.
\]

The time-column matrix has shape `624 x 14`; each spatial matrix has shape
`336 x 14`. All four have rank fourteen and empty nullspace. Their stacked
`1,632 x 14` system also has rank fourteen. Therefore there is no nonzero
principal covector—shared or individual—for which any correction is closed.

This excludes the narrow identification

```text
unique inverse-Shiab correction = j1(L_xi A) curvature by itself.
```

It does not exclude a total completion. The inverse of the positive
conditional Gauss response is the exact negative of the correction preimage;
their sum is zero and hence principal-Bianchi closed for every `q`. This
zero-sum calculation is only the nonvacuous control showing why split
nonclosure cannot be promoted to a full-curvature no-go. It does not derive
the source-native Gauss-Codazzi-Ricci decomposition.

## Specialist and hostile review

- **Differential geometry:** the principal-Bianchi failure is decisive for a
  standalone connection-curvature jet; Gauss, Codazzi and Ricci pieces must be
  tested as a total.
- **Representation theory:** the full selected map, not only the mixed bank,
  is an isomorphism, so no hidden kernel can repair closure.
- **Variational PDE:** a lawful first prolongation requires a nonzero common
  characteristic covector; every exact wedge matrix has full column rank.
- **Symplectic geometry:** Bianchi integrability precedes the covariant
  presymplectic current. Neither this test nor split cancellation constructs a
  Green-Lagrangian boundary condition, BV quotient or BFV phase space.
- **Krein/operator theory:** the result is an exact finite algebraic
  integrability statement. Positivity, Krein self-adjointness and the common
  closed domain remain open.
- **Source criticism:** raw equivariance intent is source-confirmed; the
  selected coefficients and completion are source-silent.
- **Repo archaeology:** composing v0.39's full selected map, v0.46's carrier
  containment and the August 5 principal-Bianchi test produced the result;
  no new datum or carrier was needed.

Both two-sided hostile charges fire. A summary may not turn split nonclosure
into a completed-theory no-go. Conversely, the lane must stop defending the
superseded identification of an arbitrary inverse-carrier vector with a
connection first jet.

## Progress and fences

```text
Ledger v0.47 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - the full selected Hodge-Shiab map is an exact isomorphism
  - all four inverse correction representatives are unique
  - the standalone split-jet identification fails principal Bianchi
frontier_conditions_opened: 1
  - complete source-native Gauss-Codazzi-Ricci/background decomposition
remaining_named_conditions: 4
  - total GCR curvature packet and raw-Upsilon naturality
  - optional action-owned background subtraction
  - scalar and massless constraint quotient
  - coupled fermion Hessian and common domain
```

No scalar pole, cosmological magnitude, physics equation, fifth quotient,
external datum, canon verdict or public posture changes. P1/P2/P3 remain
unused. Curt remains formally separate and no third lane is promoted.

## Next gate

Construct the source-native total connection curvature under the moving graph:
the Gauss, Codazzi and Ricci blocks, `j1(L_xi A)`, gauge-rotated Levi-Civita,
moving Hodge/Shiab and any explicitly owned background/lower-order terms.
Only then test coefficientwise total raw-`Upsilon` naturality and differential
Bianchi. Do not identify another split inverse with the connection jet, and do
not reintroduce a background subtraction without an action/counterterm owner.

The executable probe passes `50/50`, including planted failures against
carrier/jet equivocation, invertibility/closure equivocation, split-to-total
overclaim, physics promotion, datum substitution and source attribution.
