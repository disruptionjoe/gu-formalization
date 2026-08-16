---
title: "Selected-K115 RSAP TT moving-Jacobian classification and gap-wall gate"
status: superseded_in_part_by_k116
doc_type: exact_local_moving_frame_classification_owner_fingerprint_and_gap_wall_obstruction
created: "2026-08-15"
registry: lab/process/selected-k115-rsap-tt-moving-jacobian-classification-and-gap-wall-gate.json
probe: tests/channel-swings/selected_k115_rsap_tt_moving_jacobian_classification_and_gap_wall_gate_probe.py
grade: "EVERY LOCAL INVERTIBLE MOVING-TT FRAME THAT INDUCES THE K113 CONNECTION IS, UP TO ONE CONSTANT FRAME, exp((phi-phi0)G). ITS MOVING PART IS K-ORTHOGONAL, UNIT-DETERMINANT, HAS FIXED G-EIGENLINES AND EXACT RECIPROCAL STRETCH. FOR GENERIC alpha_II!=1 THAT STRETCH DIVERGES AT EITHER SIMPLE SPECTRAL GAP WALL, SO NO BOUNDED INVERTIBLE SAME-FRAME EXTENSION CROSSES THE WALL. THE CURRENT SERIALIZED SOURCE/ACTION CUSTODY SUPPLIES NO TYPED TT MAP WITH THIS FINGERPRINT; K112/K113 REMAIN RECONSTRUCTION GRADE."
target_claim: K114_NEXT_GATE__A_CURRENT_SOURCE_OR_ACTION_MOVING_TT_JACOBIAN_MAY_OWN_THE_GENERIC_ALPHA_K113_TRANSPORT
target_verdict: EXACT_LOCAL_JACOBIAN_CLASS_AND_OWNER_FINGERPRINT_BUILT__CURRENT_SERIALIZED_OWNER_CENSUS_EMPTY__NEW_TYPED_SOURCE_ACTION_MAP_REQUIRED
canon_verdict_change: none
---

# Selected-K115 RSAP TT moving-Jacobian classification and gap-wall gate

> **K116 FRAME-CONSISTENCY CORRECTION (2026-08-15):** the abstract local
> moving-frame ODE classification survives, but this concrete fingerprint is
> superseded because it inherited a mixed-frame pencil. Replace `G,phi`, the
> two walls and the `alpha=1` control by K116's
> `H=[[1,0],[-alpha,-1]]`, `psi=(1/4)log(alpha^2 b+4u)`, and single wall
> `alpha^2 b+4u=0`. The corrected connection is nonzero at `alpha=1`.

> **K117 SYMBOL-ORDER CORRECTION (2026-08-15):** K116's concrete fingerprint
> is also superseded as an action target because the inherited `d z E_hh`
> response is kinetic, not zero order. Retain only the abstract local-frame
> ODE classification. A new fingerprint requires the full moving `D3I` owner.

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> Krein/Green moving-frame and action-owner question. Ordinary Higgs/VEV,
> family-index, chirality, anomaly and symmetry-breaking constructions do not
> adjudicate it. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K113 supplied one exact parallel transport. K115 proves it is not merely one
choice among many local adapters. On any connected gapped interval, every
invertible moving frame whose Maurer--Cartan form is the K113 connection is

```text
F(u)=F0 exp((phi(u)-phi(u0))G),                    (1)
```

where `F0` is one constant invertible frame. The parallel transport is the
inverse moving factor,

```text
T(u,u0)=exp(-(phi(u)-phi(u0))G).                   (2)
```

Thus the owner search now has an exact fingerprint. The moving factor has
determinant one, preserves the Krein form, retains the two fixed `G`
eigenlines, and stretches them reciprocally by `exp(+Delta phi)` and
`exp(-Delta phi)`. No additional function can be fitted.

For generic `alpha_II!=1`, `|Delta phi|` diverges at either simple wall of the
gapped component. One reciprocal stretch therefore diverges while the other
collapses. The local adapter cannot extend through such a wall as a bounded
invertible map in the same frame. This does not forbid patched frames,
singular variables, a degenerate spectral theory, or new action data.

The current custody still has no owner. The absorbed source does not name the
reconstructed `alpha_II` coefficient or a two-field TT adapter; the unified
packet introduces `alpha_II` as a reconstructed local action coefficient, and
the action census charges it as `U7`. The selected cubic supplies only the
zeroth-order moving mass block. A mathematical frame satisfying (1) is
therefore an exact reconstruction target, not evidence that the source or
released action contains it.

## 1. Layer-0 owner packet

```text
carrier:       real two-field observed TT fluctuation
form:          K(alpha)=[[alpha,1],[1,0]], signature (1,1)
real structure: ordinary real two-component field
grading:       K113 moving spectral +/- involution C(u)
candidate owner: typed source/action field map with invertible TT Jacobian
target:        classify every local Jacobian inducing A_C and test ownership
assumptions:   b!=0; one connected simple-spectrum component; C1 field map
claim ceiling: exact local two-field and componentwise wall grade
```

The `2D` TT bundle remains distinct from the conditional `98D` balanced
phase/BFV carrier.

## 2. Complete local Jacobian class

K113 gives

```text
G=[[-1,0],[alpha,1]],          G^2=I,
phi=(1/4)log((b+u)/R),         R=alpha^2 b+(alpha-2)^2 u,
A_C=G dphi.                                              (3)
```

For a moving frame `F`, use the explicit convention

```text
F^-1 dF=A_C.                                             (4)
```

Since `G` is constant, (4) integrates directly to (1). Conversely,
differentiating (1) gives (4). If `F1` and `F2` solve (4), then
`d(F1 F2^-1)=0`; they differ by one constant left frame. This proves
completeness, not only existence.

A parallel section solves `dT+A_C T=0`, which fixes the opposite sign and
gives (2). This resolves the only convention ambiguity: moving-frame
Jacobian and parallel transport are inverses.

## 3. Invariant fingerprint

Because `tr(G)=0`, `det(G)=-1`, and `G^T K+KG=0`, the moving factor obeys

```text
det exp(Delta phi G)=1,
exp(Delta phi G)^T K exp(Delta phi G)=K.                (5)
```

Its two eigenvalues are `exp(Delta phi)` and `exp(-Delta phi)`. Hence

```text
exp(2 Delta phi)
  = sqrt(((b+u) R(u0))/(R(u)(b+u0))).                   (6)
```

Any exact source/action adapter must therefore reproduce, up to a constant
frame:

1. the two fixed `G` eigenlines;
2. reciprocal determinant-one motion;
3. the exact cross-ratio (6); and
4. no additional functional coefficient.

Matching only a nonzero connection, a determinant, or a generic residual
Jacobian is insufficient.

## 4. Gap-wall gate

The two walls are

```text
b+u=0,                  R(u)=0.                         (7)
```

At a simple numerator wall with the other factor nonzero, `phi -> -infinity`.
At a simple `R` wall with `b+u` nonzero, `phi -> +infinity`. Equation (6) then
forces one eigenvalue ratio to zero or infinity. Multiplication by a fixed
invertible `F0` cannot make both the frame and its inverse bounded. Therefore
there is no bounded invertible same-frame extension through either generic
wall.

At `alpha=1`, the control is exact: `R=b+u`, `phi=0`, and the moving factor is
constant. K114 already proved this commuting locus is invariant but
action-unselected.

## 5. Serialized owner census

```text
K115 local adapter class:                    COMPLETE
new functional freedom:                     ZERO
absorbed source alpha_II / TT adapter:       NOT SERIALIZED
unified packet alpha_II status:              RECONSTRUCTED COEFFICIENT
action-census status:                        U7 CHARGED
selected cubic derivative TT Jacobian:       ABSENT
current matching source/action owner count:  ZERO
```

This census is deliberately current-custody scoped. New source material, a
fully typed common-field map, or a complete action linearization can reopen
it immediately by meeting (1)--(6).

## 6. Reverse-scaffold disposition and hostile ceilings

Retain the K112 minimal covariant TT quadratic and K113 transport at
reconstruction grade. K115 narrows the next owner evidence to one exact
class, and exposes the component boundary where a global theory must add
patching or new data. It does not construct a stationary background, global
bulk action, closed positive domain, boundary/BFV attachment, `98D` physical
complex, or cohomology.

The invariant linear `2D`-to-`98D` route remains closed by K107; non-invariant,
nonlinear, boundary, nonlocal, and cohomological maps remain open. No ledger,
datum, quotient booking, canon, public posture, particle, phenomenology or GU
truth-status claim changes.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k115_rsap_tt_moving_jacobian_classification_and_gap_wall_gate_probe.py
```
