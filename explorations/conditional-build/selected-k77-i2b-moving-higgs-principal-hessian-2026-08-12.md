---
artifact_type: conditional_build_variational_result
created: 2026-08-12
run_id: RUN-20260812-155230-gu-i2b-moving-higgs-principal-hessian
status: FIRST_GREEN_ZERO_BUT_SECOND_PRINCIPAL_HESSIAN_RANK2__TWO_LIVE_KREIN_RADICAL_DIRECTIONS__DISPLAYED_SHIAB_FAMILY_CANNOT_REPAIR
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B moving-Higgs principal Hessian

## Result

The previous result asked the right first-variation question and drew one
sentence too much from it.  Its vanishing Green coefficient says that the
nonzero background residual contributes no first-variation boundary pairing
on the fixed-`H_q` family.  It does **not** say that the residual-square action
has no kinetic Hessian.

The actual second-variation top-order Gram on the four-real moving-Higgs
tangent is

```text
H^{00} = diag(-8,-8,0,0)
H^{11} = H^{22} = H^{33} = diag(8,8,0,0)
H^{mu nu} = 0 for mu != nu.
```

Thus

\[
H_2(k)=8(-k_0^2+k_1^2+k_2^2+k_3^2)
       \operatorname{diag}(1,1,0,0).
\]

It has rank two for every tested non-null covector and rank zero on the null
cone.  The last two internal directions form the exact radical; the fourth is
the `J`-completed radial direction that also carries the nonzero restricted
potential branch.

This is not a zero-evaluator artifact.  Both radical directions have nonzero
principal responses, each of support two, but those responses are null and
orthogonal to the entire four-real tangent image under the pairing currently
used by `SC-ACT-04`.  The full `196`-real connection bank has exact timelike
principal Gram rank `182`.  The defect therefore lies in the restriction plus
pairing, not in absence of a derivative response.

## Plain English

The current construction gives two of the four proposed Higgs directions an
ordinary wave-like kinetic term.  The other two—including the radial Higgs
amplitude—do respond to derivatives, but the present indefinite pairing
cannot see their response.  So the route is incomplete, not dead.

That distinction matters for the conditional build.  A source-owned bosonic
primalizer `Q_B`, a coupled metric/section/gauge contact block, or a larger
total-residual action parent could pair those live null responses with dual
directions.  This run does not construct any of those repairs.  It establishes
the exact burden they must meet: raise the physical four-real principal symbol
from rank two to rank four without adding an unowned physical datum.

## Layer 0

| phrase | object decided here | kept distinct |
| --- | --- | --- |
| zero Green | first variation paired with the background residual | second-variation kinetic Gram |
| Hessian radical | live derivative responses invisible to the current pairing | zero derivative response |
| current pairing | fixed degree-thirteen Hodge/Clifford-trace comparator | source-owned but unbuilt `Q_B` |
| four-real tangent | selected local moving-Higgs carrier | full `196`-real connection bank |
| principal Hessian | top-order connection-jet block | lower-order terms at a nonzero nonstationary residual |
| fermion dual | independent barred/unbarred action-slot equivalence | bosonic residual primalizer |

The source `C^(32,32)+C^(32,32)` carrier split, the derived
`U(32,32)xU(32,32)` block subgroup, the full `U(64,64)` parent, and the
independent connection fields remain four separately typed objects.  None is
selected by this calculation.

## Selector and first-action controls

All eight displayed `comm/symi` Shiab triples were tested on the same
four-real tangent.  Six have rank two and two have rank zero.  None has rank
four.  Merely changing the displayed Shiab selector therefore cannot repair
the radical.

The source first-action principal quadratic block
`<delta A, Shiab(k wedge delta A)>` is exactly rank zero for all eight triples.
It cannot be silently substituted for the missing second-action kinetic
completion.

## Variational scope

The general stationary factorization

\[
H_2=(D\Upsilon_B)^\vee Q_B(D\Upsilon_B)
\]

was already recorded in v0.82.  The current restricted branch has a nonzero,
Krein-null residual and is not a full stationary background, so lower-order
second-variation terms involving the residual and moving coefficients remain
open.  The theorem here is only the curvature-principal connection-jet block:
that block is the exact Gram above because the residual is affine in those
highest jets.

## Source return

The source owns the bosonic residual square and thereby the typed slot for a
bosonic residual primalizer `Q_B`.  It does not print the exact K77 primalizer,
the four-real Hessian, its rank-two radical, or a repair.

```text
SOURCE-CONFIRMS: bosonic residual-square architecture and Q_B slot.
REPO-CORRECTS: zero first Green does not imply absence of the second principal Hessian.
REPO-DERIVES: exact Lorentz rank-two Hessian and two live pairing-radical directions.
SOURCE-SILENT: exact Q_B, coupled contact completion and radical removal.
```

## Specialist and hostile review

- **Symplectic geometry:** the principal bilinear must be computed before any
  presymplectic/BFV quotient.  Rank two is not a four-real phase space.
- **Analytic/PDE:** the Lorentz factor and null cone are real symbol data, but
  no hyperbolicity, common domain, energy, spectrum or propagator follows from
  this finite block.
- **Variational bicomplex:** first Green and second principal Hessian are
  different variational grades; the former cannot erase the latter.
- **Krein/operator theory:** a live isotropic response is neither zero nor
  positive.  Pairing radical and equation kernel stay distinct.
- **Principal-bundle geometry:** moving metric, section and gauge contact
  terms are outside this frozen calculation and remain legitimate repairs.
- **Source criticism:** the fermionic independent-dual orbit is not the
  bosonic `Q_B` slot.
- **Contrary review:** the rank-182 full-bank control and support-two radical
  responses prevent a vacuous rank-two result.

Hostile verdict:
`RESULT_SURVIVES__V0212_INTERPRETATION_CORRECTED__SCOPED_TO_FIXED_PAIRING_FIXED_GEOMETRY_PRINCIPAL_HESSIAN`.

No ledger verdict, canon surface or public posture moves.

## Progress and next gate

```text
Ledger v0.213 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 3 conditions closed · 1 sharper repair gate opened · 2 remain
```

No field, parameter, selector, quotient or external datum is added.  P1/P2/P3
remain unchanged and unused.

Next type the source-owned bosonic `Q_B`/dual residual pairing and the coupled
moving metric/section/gauge contact or expanded total-residual parent.  Test
whether either makes the four-real principal Hessian nondegenerate.  Do not
attempt a Higgs spectrum until that rank-four gate and observation/gauge
basicness both pass.
