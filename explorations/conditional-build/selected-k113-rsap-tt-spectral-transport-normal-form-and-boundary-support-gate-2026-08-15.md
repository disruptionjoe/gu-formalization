---
title: "Selected-K113 RSAP TT spectral-transport normal form and boundary-support gate"
status: active_research
doc_type: exact_one_generator_connection_rapidity_zero_transport_locus_boundary_support_and_action_adapter_gate
created: "2026-08-15"
registry: lab/process/selected-k113-rsap-tt-spectral-transport-normal-form-and-boundary-support-gate.json
probe: tests/channel-swings/selected_k113_rsap_tt_spectral_transport_normal_form_and_boundary_support_gate_probe.py
grade: "THE K112 MINIMAL VARIATIONAL CONNECTION REDUCES EXACTLY TO A_C=G dPHI WITH ONE FIXED KREIN-SKEW INVOLUTION G AND CLOSED-FORM PARALLEL TRANSPORT. IT VANISHES IDENTICALLY ON THE GAPPED alpha_II=1 LOCUS, WHICH IS NOT CURRENTLY ACTION-SELECTED. A BOUNDARY-ONLY FUNCTIONAL CANNOT GENERATE THE INTERIOR TRANSPORT COEFFICIENT, ALTHOUGH A BOUNDARY OR COHOMOLOGICAL 2D-TO-98D ATTACHMENT REMAINS OPEN. THE NEXT OWNER TEST IS AN ACTION-NORMALIZATION OR SOURCE-VARIABLE-JACOBIAN MATCH TO THE EXACT TRANSPORT."
target_claim: K112_NEXT_GATE__A_SOURCE_ACTION_OR_BOUNDARY_PACKET_CAN_OWN_THE_MOVING_TT_COMPLETION_WITHOUT_A_MORE_SPECIFIC_COEFFICIENT_OR_ADAPTER_TEST
target_verdict: EXACT_ONE_GENERATOR_ADAPTER_TARGET_BUILT__alpha_II_ONE_ZERO_TRANSPORT_LOCUS_UNSELECTED__BOUNDARY_ONLY_INTERIOR_OWNER_EXCLUDED__BOUNDARY_ATTACHMENT_AND_ACTION_JACOBIAN_REMAIN_OPEN
canon_verdict_change: none
---

# Selected-K113 RSAP TT spectral-transport normal form and boundary-support gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> Krein, observed-defect and RSAP/BFV action-owner question. Ordinary
> Higgs/VEV, family-index, net-chirality, anomaly, symmetry-breaking and
> familiar four-dimensional gauge-model conclusions do not adjudicate it.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K112 proved that the moving TT connection has a minimal local quadratic
variational completion. K113 makes the remaining action search exact.

With `alpha=alpha_II`, define

```text
R(u)=alpha^2 b+(alpha-2)^2 u,
G=[[-1,0],[alpha,1]],
phi(u)=(1/4)log[(b+u)/R(u)].
```

The complete spectral connection is simply

```text
A_C=G dphi.                           (1)
```

There is one fixed matrix direction, one already-determined scalar function
and no connection coefficient to fit. Its parallel transport is explicit:

```text
T(u,u0)=exp[-(phi(u)-phi(u0))G]
       =cosh(dphi) I-sinh(dphi) G.    (2)
```

This gives a precise adapter test. A source/action field map owns the K112
completion only if its moving TT Jacobian induces (2), up to an explicitly
typed constant compatible frame change.

Two further facts narrow the route.

- At `alpha_II=1`, `phi=0`, `C` is constant and `A_C=0` throughout the
  gapped component. No moving connection is needed there. But `alpha_II` is a
  live action coefficient and is not currently selected to one in the fixed
  TT normalization.
- Boundary-only data cannot generate the missing interior first-order Euler
  coefficient. Boundary/BFV data may still select a domain, carry edge modes,
  or provide a non-invariant/cohomological attachment to the `98D` complex.
  Those are different jobs and remain open.

The next swing is therefore an action-normalization/Jacobian audit, not a
generic search for a connection and not a boundary-only repair of the bulk
operator.

## 1. Exact one-generator reduction

Retain the K110--K112 pencil

```text
K=[[alpha,1],[1,0]],
M(u)=[[u,u],[u,b+u]],
L=K^-1 M,
Delta=(b+u)R(u),
C=(2L-tr(L)I)/sqrt(Delta).
```

Direct exact differentiation gives

```text
A_C=(1/2)C dC=g(u)G du,
g(u)=b(alpha-1)/[(b+u)R(u)].          (3)
```

The generator satisfies

```text
G^2=I,
G^T K+K G=0,
tr G=0.                               (4)
```

The coefficient has the partial-fraction identity

```text
g(u)=1/[4(b+u)]-(alpha-2)^2/[4R(u)]
    =dphi/du.                          (5)
```

Equations (3)--(5) prove (1). Flatness is now constructive rather than merely
an integrability statement: (2) gives the unique transport normalized by
`T(u0,u0)=I`.

## 2. Coefficient packet for the K112 action

For `A_mu=gG partial_mu u`, the connection wave operator differs from the
ordinary one by

```text
Box_A-Box
=2gG(partial^mu u)partial_mu
 +G[g Box u+g'(partial u)^2]
 +g^2 I(partial u)^2.                 (6)
```

This is the complete coefficientwise target. A claimed full-action owner must
reproduce all three terms with their relative coefficients, or derive an
equivalent operator through a typed field Jacobian. Matching only a nonzero
first-derivative rank, the word “connection,” or the mass block is not enough.

K112's quadratic action owns (6) by construction at reconstruction grade.
The selected cubic owns none of (6), and the released action has no currently
serialized moving-TT adapter that can be compared to (2).

## 3. The `alpha_II=1` zero-transport locus

At `alpha=1`, on `b+u>0`,

```text
R(u)=b+u,
phi(u)=0,
C=[[1,2],[0,-1]],
dC/du=0,
A_C=0.                                (7)
```

This is not the gap wall `u=-b`. It is a whole gapped coefficient locus on
which the spectral eigenspaces remain fixed while the eigenvalues may move.

The repository records `alpha_II` as an already charged full-`|II|^2`
coefficient and uses only `alpha_II>0` for the present TT majorant. No current
owner fixes it to one in the normalization where the cross kinetic entry is
one and the coupling vector is `v=(1,1)`. A field rescaling that changes those
other recorded structures is not, by itself, a proof of (7).

## 4. Boundary support: owner versus attachment

Let `B` depend only on boundary jets. For every `delta q` compactly supported
in the interior,

```text
delta B=0.
```

Therefore `B` cannot change the interior Euler operator and cannot create the
first term of (6) where `du` has interior support. A boundary BFV charge alone
has the same support limitation.

This closes only **boundary-only ownership of interior transport**. It does
not close:

- a bulk BV action containing the K112 covariant quadratic;
- boundary selection of a closed Green/self-adjoint domain;
- an edge or collar sector with its own bulk-supported coupling;
- a non-invariant boundary or cohomological map from the TT system into the
  balanced `98D` BV-BFV complex.

K112's boundary-compatible Green flux and its open boundary/cohomological
attachment route therefore survive unchanged. The owner and attachment
questions are now explicitly separated.

## 5. Reverse-scaffold disposition

```text
one-generator transport normal form:                 EXACT
closed-form action-variable adapter target:          EXACT
alpha_II=1 zero-transport locus:                      EXACT, UNSELECTED
K112 minimal variational action:                      RETAINED, RECONSTRUCTED
selected/released action coefficientwise owner:       NO CURRENT WITNESS
boundary-only owner of interior transport:            EXCLUDED
boundary/cohomological 2D-to-98D attachment:           OPEN
stationary moving background and closed domain:       OPEN
```

Keep Variancer's reverse classical RSAP/BFV scaffold. The next exact swing is
to trace the ownership and normalization of `alpha_II`, then test any
source-variable-to-TT Jacobian against (2). Only after that should the open
non-invariant/boundary/cohomological `98D` attachment be composed.

## Claim ceiling

This is a repository-derived exact normal form and support theorem on the
observed two-field TT system. It is not source-confirmed, a completed
full-action derivation, a stationary solution, a bulk BV master action, a
closed positive quantum domain, a `98D` attachment or physical cohomology. It
does not prove `alpha_II=1`, `H-Q*` or `H0`.

No ledger, datum, quotient booking, canon, public posture, particle,
phenomenology or GU truth-status claim changes. Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k113_rsap_tt_spectral_transport_normal_form_and_boundary_support_gate_probe.py
```
