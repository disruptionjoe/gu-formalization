---
title: "Selected-K111 RSAP TT spectral-transport connection and owner gate"
status: superseded_in_part_by_k116
doc_type: exact_moving_background_krein_complex_metric_connection_green_completion_and_action_owner_test
created: "2026-08-15"
registry: lab/process/selected-k111-rsap-tt-spectral-transport-connection-owner-gate.json
probe: tests/channel-swings/selected_k111_rsap_tt_spectral_transport_connection_owner_gate_probe.py
grade: "ON THE GAPPED SIMPLE-SPECTRUM 2D TT BUNDLE, A_C=(1/2)C dC IS THE UNIQUE CONNECTION THAT PRESERVES BOTH K AND C; IT ALSO PRESERVES H=KC, IS FLAT FOR THE ONE-SCALAR FAMILY, AND RESTORES C-COMPATIBLE GREEN PROPAGATION FOR u(x). THE SELECTED CUBIC HESSIAN OWNS ONLY THE VARIABLE MASS BLOCK AND NOT THESE FIRST/ZERO-ORDER CONNECTION TERMS; STATIONARY FULL-ACTION, QUANTUM-DOMAIN AND 98D BFV ATTACHMENT REMAIN OPEN"
target_claim: K110_NEXT_GATE__THE_MOVING_BACKGROUND_DERIVATIVE_COMPLETION_IS_CANONICAL_AND_ALREADY_ACTION_OWNED
target_verdict: CANONICAL_AND_UNIQUE_YES__ACTION_OWNED_NO_AT_THE_SELECTED_CUBIC_TT_TRUNCATION__FULL_ACTION_AND_BFV_PORT_OPEN
canon_verdict_change: none
---

# Selected-K111 RSAP TT spectral-transport connection and owner gate

> **K116 FRAME-CONSISTENCY CORRECTION (2026-08-15):** the abstract theorem
> `A_C=(1/2)C dC` and its compatibility/uniqueness claims survive. Its
> historical concrete `C(u)` came from a mixed-frame pencil. K116 repaired
> that frame mismatch, but its concrete mass-deformed target is itself
> superseded by the K117 differential-order correction below.

> **K117 SYMBOL-ORDER CORRECTION (2026-08-15):** do not use K116 for an
> action-owner comparison. The inherited response moves `K`, and for moving
> `K` the constant-form formula below is not the simultaneous compatibility
> connection. The abstract fixed-form theorem survives; use K117 for scope.

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> Krein, observed-defect and RSAP/BFV operator question. Ordinary Higgs/VEV,
> family-index, net-chirality, anomaly, symmetry-breaking and familiar
> four-dimensional gauge-model conclusions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before importing any such
> comparator.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K110's variable-background obstruction has a canonical mathematical repair.
It is not yet a repair owned by the selected action.

For the moving spectral involution `C(u(x))`, define

```text
A_C = (1/2) C dC.
```

On the gapped simple-spectrum component this connection is exact and unique:

- it makes `C` parallel;
- it preserves the original indefinite/Krein form `K`;
- therefore it preserves the positive fibre metric `H=KC`;
- replacing `Box` by the connection wave operator `Box_A` makes
  `D_A=Box_A+L(u)` commute with `C` and remain formally `H`-symmetric;
- on a globally hyperbolic observed defect, `D_A` remains normally
  hyperbolic and has `C`-compatible advanced/retarded Green operators; and
- because this family depends on one scalar `u`, `A_C` is flat wherever the
  spectral gap remains open.

There is no fitted coefficient and no extra independent function after `u(x)`
is supplied. In that precise sense the moving completion is canonical.

But the selected cubic is

```text
V_3=c theta (q_0+q_m)^2.
```

Its TT Hessian contributes only the zeroth-order block `u(x) vv^T`. It has no
derivatives of the TT fields and therefore supplies none of the first- or
zero-order connection terms in `Box_A-Box`. The free kinetic matrix `K` is
constant in this truncation. So `A_C` is a derived operator covariantization,
not an action-owned term of the currently selected cubic TT Hessian.

This shifts the live question again. We no longer need to invent an arbitrary
moving connection. We need to find—or rule out—the exact `A_C` port in the
complete action linearization, a stationary total-field background, or a
boundary/BFV operator.

## 1. Carrier, forms and owner fence

The carrier is the same real two-field TT bundle as K110:

```text
K=[[alpha,1],[1,0]],
M(u)=M_0+u vv^T,
L(u)=K^-1 M(u),
C(u)=[2L-tr(L)I]/sqrt(Delta),
H(u)=K C(u)>0.
```

The construction is valid on the free-connected component

```text
b+u>0,
alpha^2 b+(alpha-2)^2 u>0.
```

It excludes the exceptional walls `Delta=0`. The selected action owns the
cubic and its pointwise Hessian. It does not derive the background `u(x)`,
prove it stationary, or presently own the transport connection.

## 2. Exact connection identities

Differentiating `C^2=I` gives

```text
C dC+dC C=0.
```

With `A_C=(1/2)C dC`,

```text
dC+[A_C,C]=0.                         (1)
```

Thus `nabla_A C=0`. The `K`-self-adjointness identity

```text
C^T K=K C
```

and its derivative imply

```text
A_C^T K+K A_C=0.                      (2)
```

So `nabla_A K=0`. Equations (1)--(2) give

```text
nabla_A H=nabla_A(KC)=0.              (3)
```

The connection is unique at this grade. If another connection has the same
two properties, its difference `B` obeys

```text
[B,C]=0,
B^T K+K B=0.
```

The simple `+1` and `-1` eigenspaces of `C` are one-dimensional and
`K`-orthogonal. A commuting `B` preserves each line, while a skew operator on
a non-null one-dimensional line is zero. Hence `B=0`.

## 3. Moving Green completion

Use the connection d'Alembertian on the observed globally hyperbolic defect:

```text
D_A=Box_A I+L(u(x)).
```

Because `C` is parallel and `[C,L]=0`,

```text
[C,D_A]=0.
```

Because `H` is parallel and `HL=L^T H`, `D_A` is formally `H`-symmetric.
Changing the connection changes only lower-order terms, so the scalar
Lorentzian principal symbol and normal hyperbolicity remain. The unique Green
operators therefore preserve the two `C` sectors.

For one scalar background, write `A_C=A_u(u)du`. Then

```text
F_A=dA+A wedge A=0:
```

the exterior derivative is proportional to `du wedge du`, and the connection
commutator uses the same single matrix `A_u` in every direction. This is a
flat spectral-transport connection on each gapped component. It can still
have global holonomy if the background domain is not simply connected, but
the present one-interval component has no such local obstruction.

## 4. Exact action-owner failure at the selected truncation

The operator difference is schematically

```text
Box_A-Box
  =2 A^mu partial_mu +(nabla_mu A^mu)+A_mu A^mu.
```

The selected cubic contains no TT-field derivatives. Its second variation in
`(q_0,q_m)` is exactly `u(x)vv^T`, while every Hessian involving
`partial q_0` or `partial q_m` is zero. It therefore cannot generate the
nonzero first-order coefficient `2A^mu` when `du` is nonzero.

This is not a universal action no-go. Other terms in the complete source
action, a coupled scalar/metric field redefinition with its full Jacobian, a
stationary total-field completion, or boundary/BFV data could supply the same
connection. They must be compared coefficientwise to `A_C`; naming an
unspecified “covariant derivative” is not enough.

## 5. Reverse-scaffold disposition

The K110 candidate advances from fixed-background to moving-background Green
grade, conditionally on replacing its operator by the unique spectral
connection completion. The ten-row inventory still has zero full `98D`
entrants because:

```text
moving positive-fibre/Green package on 2D TT bundle:  BUILT CONDITIONALLY
selected cubic action owns its connection terms:      NO
stationary complete-action background:                NO
selected closed positive quantum domain:              NO
typed map into conditional 98D BFV carrier:            NO
```

Keep Variancer's reverse classical RSAP/BFV scaffold. The next exact swing is
an owner-port audit: compute the complete action's first-derivative TT
linearization on a candidate stationary moving background and compare it to
`A_C` coefficientwise, or derive the same connection from a boundary/BFV law.

## Claim ceiling

This is a repository-derived exact theorem on a two-dimensional real
simple-spectrum eigenbundle over a one-scalar gapped background family. It is
not source-confirmed, stationary, action-selected beyond the negative cubic
owner test, a closed quantum domain, positive-energy theorem, physical BFV
cohomology, ambient `Y14` result or `98D` attachment. It proves neither
`H-Q*` nor `H0`.

No ledger, datum, quotient booking, canon, public posture, particle,
phenomenology or GU truth-status claim changes. Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k111_rsap_tt_spectral_transport_connection_owner_gate_probe.py
```
