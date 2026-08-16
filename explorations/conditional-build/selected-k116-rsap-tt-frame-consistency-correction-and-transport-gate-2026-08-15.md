---
title: "Selected-K116 RSAP TT frame-consistency correction and transport gate"
status: active_research
doc_type: exact_coordinate_custody_correction_consistent_tt_spectral_transport_and_successor_gate
created: "2026-08-15"
registry: lab/process/selected-k116-rsap-tt-frame-consistency-correction-and-transport-gate.json
probe: tests/channel-swings/selected_k116_rsap_tt_frame_consistency_correction_and_transport_gate_probe.py
grade: "THE K110--K115 TWO-WALL AND alpha_II=1 ZERO-TRANSPORT PACKET IS SUPERSEDED: IT COMBINED THE RAW (h,v) KINETIC/FREE-MASS MATRICES WITH THE EIGENMODE (q0,qm) INTERACTION HESSIAN. IN A SINGLE CONSISTENT FRAME THE DISCRIMINANT IS b(alpha_II^2 b+4u), THE FREE-CONNECTED POSITIVE COMPONENT HAS ONE WALL alpha_II^2 b+4u=0, AND A_C=H du/(alpha_II^2 b+4u) WITH H^2=I. THE CONNECTION IS NONZERO AT alpha_II=1. THE ABSTRACT SPECTRAL-CONNECTION, VARIATIONAL-COMPLETION, BOUNDARY-SUPPORT, AND LOCAL-FRAME ODE RESULTS SURVIVE AFTER REINSTANTIATION; THE NEXT OWNER TEST MUST USE THIS CORRECTED TARGET."
target_claim: K115_CONCRETE_TT_TRANSPORT_FINGERPRINT_IS_COORDINATE_CONSISTENT_WITH_ITS_ACTION_PROVENANCE
target_verdict: NO__MIXED_RAW_AND_EIGENMODE_FRAMES__CORRECTED_ONE_WALL_NONZERO_ALL_ALPHA_TRANSPORT_PACKET_BUILT
canon_verdict_change: none
---

# Selected-K116 RSAP TT frame-consistency correction and transport gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> coordinate-custody, Krein/Green and action-Hessian question. Ordinary
> Higgs/VEV, family-index, net-chirality, anomaly, symmetry-breaking and
> familiar four-dimensional gauge-model constructions do not adjudicate it.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K110--K115 transported a real algebraic result through the wrong concrete
pencil. The free kinetic and mass matrices were retained in the original
metric/distortion coordinates, while the cubic Hessian was inserted in the
free eigenmode coordinates. Those matrices cannot be combined without a
change-of-basis transformation.

Keeping every matrix in one frame removes the apparent second wall and the
apparent `alpha_II=1` zero-transport locus. The corrected moving spectral
connection is nonzero for every finite `alpha_II`, including one. Therefore
the K115 source/action owner census was aimed at the wrong exact fingerprint.

This is a correction, not a route kill. Four structural results survive:

1. a fixed-background spectral fundamental symmetry can compose with the
   two-field Green system;
2. `A_C=(1/2)C dC` is the unique `K`- and `C`-compatible connection;
3. the minimal covariant quadratic is a valid reconstruction-grade
   variational owner, and boundary-only data cannot generate its interior
   first-order coefficient; and
4. every local frame inducing a one-generator connection is unique up to one
   constant frame.

They must now be instantiated with the corrected pencil below.

## 1. Layer-0 owner packet

```text
carrier:       real two-field observed TT fluctuation
raw frame:     x=(h,v), metric/distortion coordinates
mode frame:    q=(q0,qm), free eigenmode amplitudes, x=Uq
form:          Kx=[[alpha,1],[1,0]], Kq=U^T Kx U
real structure: ordinary real two-component field
grading:       corrected spectral +/- involution C(u)
action owner:  selected free TT pencil plus selected cubic u h^2
target:        repair coordinate custody before any moving-Jacobian census
assumptions:   alpha>0, b>0, one free-connected gapped component
controls:      raw/eigen congruence, alpha=1, u=0, planted mixed-frame pencil
claim ceiling: exact local two-field reconstruction grade
```

The `2D` TT bundle remains distinct from the conditional `98D` balanced
phase/BFV carrier.

## 2. Where the frame mismatch entered

The selected free pencil in the original coordinates `x=(h,v)` is

```text
Kx=[[alpha,1],[1,0]],        M0x=[[0,0],[0,b]].          (1)
```

Its free eigenvectors are the columns of

```text
U=[[1,1],[0,-alpha]],        x=Uq.                       (2)
```

Thus `h=q0+qm`. The selected cubic `u h^2` consequently has Hessian
`u vv^T`, `v=(1,1)`, **in the q frame**. K110--K115 instead combined
`Kx`, `M0x`, and `u vv^T` as if all three lived in one frame.

The two consistent descriptions are

```text
raw x frame:   Kx=[[alpha,1],[1,0]]
               M0x=[[0,0],[0,b]]
               M1x=[[1,0],[0,0]]

mode q frame:  Kq=U^T Kx U=diag(alpha,-alpha)
               M0q=U^T M0x U=diag(0,alpha^2 b)
               M1q=U^T M1x U=[[1,1],[1,1]].             (3)
```

Either triple produces the same dynamics by similarity. The historical
mixed triple does not.

## 3. Corrected spectral packet

In the raw frame,

```text
M(u)=[[u,0],[0,b]],
L(u)=Kx^-1 M(u)=[[0,b],[u,-alpha b]],
Delta=tr(L)^2-4 det(L)=b(alpha^2 b+4u).                 (4)
```

On the free-connected component `alpha^2 b+4u>0`, put

```text
C(u)=1/sqrt(Delta) [[alpha b,2b],[2u,-alpha b]].         (5)
```

Then `C^2=I`, `[C,L]=0`, `C^T Kx=Kx C`, and

```text
sqrt(Delta) Kx C
  =[[alpha^2 b+2u,alpha b],[alpha b,2b]],               (6)
```

which is positive definite for `b>0` on that component. There is one finite
gap wall,

```text
alpha^2 b+4u=0,                                         (7)
```

not the two walls recorded in K110--K115.

## 4. Corrected connection and frame class

Define

```text
H=[[1,0],[-alpha,-1]],          H^2=I,
psi(u)=(1/4)log(alpha^2 b+4u).                          (8)
```

Direct differentiation gives

```text
A_C=(1/2)C dC=H dpsi=H du/(alpha^2 b+4u).               (9)
```

The local moving-frame and parallel-transport classes are therefore

```text
F(u)=F0 exp((psi(u)-psi(u0))H),
T(u,u0)=exp(-(psi(u)-psi(u0))H).                        (10)
```

Here `H^T Kx+Kx H=0`, so the moving factor is `Kx`-orthogonal and has
determinant one. Its reciprocal stretch diverges at the single wall (7), so
the abstract K115 same-frame extension obstruction survives with one wall.

In the mode frame, `U^-1 H U=[[0,1],[1,0]]`; equations (9)--(10) are the same
connection written consistently in eigenmode coordinates.

## 5. The alpha=1 control reverses K113--K115

At `alpha=1`,

```text
A_C=[[1,0],[-1,-1]] du/(b+4u),                          (11)
```

which is nonzero whenever `du` is nonzero. Moreover, splitting the corrected
dynamics into free and interaction pieces gives

```text
[L0,L1]=b H,                                             (12)
```

which has determinant `-b^2` and rank two for every `alpha` when `b!=0`.
There is no commuting or zero-transport coefficient locus to normalize or
select. K114's invariant argument was valid for the mixed triple it was
given; that triple was not the action-owned pencil in any single frame.

## 6. Status correction

| prior result | corrected status |
| --- | --- |
| first perturbative background `C` | concrete two-wall formulas superseded; rebuild from (4)--(7) |
| K110 fixed-background composition | structural composition survives; concrete `C`, component and walls replaced |
| K111 `A_C=(1/2)C dC` | abstract uniqueness/compatibility survives; concrete instantiation replaced by (9) |
| K112 variational completion | structural reconstruction survives with corrected `A_C` |
| K113 one-generator/boundary gate | one-generator and boundary-support results survive; `G,phi`, two walls and alpha=1 locus superseded |
| K114 normalization gate | superseded in full; its target locus was manufactured by the frame mismatch |
| K115 frame classification | abstract ODE classification survives with `H,psi`; concrete fingerprint, two-wall claim and alpha=1 control superseded |

The correction changes no canon, ledger, public posture, particle claim,
phenomenology claim, stationary-background claim, closed-domain claim or BFV
cohomology claim.

## 7. Twenty-lens reassessment and vote

Each lens named its strongest live hypothesis after seeing the frame audit.
`FRAME` means correct provenance first; `SALVAGE` means preserve an abstract
result; `ACTION` means advance only through a literal action derivation; and
`PARK` means do not spend the next swing there.

| # | lens | strongest hypothesis now | vote |
| ---: | --- | --- | --- |
| 1 | Layer-0 semantics | the apparent object identity failed at the coordinate-frame field | FRAME |
| 2 | coordinate geometry | all quadratic forms must move by the same congruence | FRAME |
| 3 | action Hessian | the next admissible owner is the literal full second variation | ACTION |
| 4 | exact linear algebra | the consistent raw and mode pencils are dynamically similar | FRAME |
| 5 | perturbation theory | the historical first-order `C1` must be recomputed | FRAME |
| 6 | Krein operator | a positive spectral involution still exists on one component | SALVAGE |
| 7 | connection geometry | `A_C=(1/2)C dC` survives with corrected `H,psi` | SALVAGE |
| 8 | variational PDE | the minimal covariant quadratic remains a valid reconstruction | SALVAGE |
| 9 | Green hyperbolicity | corrected connection transport preserves the structural Green route | SALVAGE |
| 10 | boundary variational calculus | boundary-only data still cannot own an interior coefficient | SALVAGE |
| 11 | gap-wall analysis | there is one finite wall, so wall work must be retyped | FRAME |
| 12 | source criticism | released source custody does not yet provide the required typed map | ACTION |
| 13 | action ownership | the old zero-owner census is void because it tested the wrong target | ACTION |
| 14 | normalization | there is no alpha-one locus to normalize or select | FRAME |
| 15 | covariance/naturality | basis covariance is the mandatory control for every successor | FRAME |
| 16 | falsification | alpha one is now a planted nonzero-transport control | FRAME |
| 17 | representation/BFV | the `2D`-to-`98D` attachment remains separate and premature | PARK |
| 18 | claim-status discipline | downgrade K110--K115 before building further | FRAME |
| 19 | reverse scaffolding | rebuild backward from corrected `H dpsi` | ACTION |
| 20 | hostile synthesis | derive once from the action, then decide ownership coefficientwise | ACTION |

Vote:

```text
FRAME   9
SALVAGE 5
ACTION  5
PARK    1
```

The highest-vote hypothesis is the frame-custody correction. The highest-
conviction conclusions, including those not winning the vote, are:

- `0.99`: the old two-wall and alpha-one packet is a mixed-frame artifact;
- `0.99`: the corrected packet has one wall and nonzero alpha-one transport;
- `0.97`: the abstract connection, variational, boundary-support and local
  frame-ODE results survive;
- `0.95`: action ownership is reset to open, not negative; the prior census
  tested the wrong fingerprint.

## 8. Reverse scaffold for the next series of swings

Retain Variancer's reverse conditional method. Start with the superposition
hypothesis rather than with a familiar comparator:

> **Superposition hypothesis:** the literal GU source/action moving-background
> TT Hessian, derived entirely in one declared coordinate frame, induces the
> corrected spectral transport `A_C=H dpsi`.

Build backward from the conditions that would make that hypothesis true:

```text
R0 target:       exact corrected H dpsi / exp[-Delta psi H] fingerprint
R1 map owner:    literal source variables -> TT fluctuation map and Jacobian
R2 Hessian:      full second variation, including derivative and mixed terms
R3 comparison:   first- and zero-order coefficients match R0 exactly
R4 background:   action-owned stationary moving background
R5 analysis:     common Green/core/domain data on the one-wall component
R6 attachment:   typed non-invariant/nonlinear/boundary/cohomological 2D->98D map
```

The next swings should therefore be:

1. **K117 — source/action frame custody and literal moving TT Hessian.** Name
   every variable and transform before differentiating; no inferred adapter.
2. **K118 — coefficientwise transport-owner match.** Compare the K117
   first/zero-order operator to (9)--(10), with alpha-one and basis-covariance
   controls.
3. **K119 — conditional branch.** If K118 matches, test stationary-background
   and domain ownership. If it fails, classify the minimal missing action term
   without fitting it.
4. **K120 — attachment only after ownership.** Reopen the `2D`-to-`98D` route
   only after an owner, background and domain survive.

Do not resume the owner census against the historical K115 fingerprint.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k116_rsap_tt_frame_consistency_correction_and_transport_gate_probe.py
```
