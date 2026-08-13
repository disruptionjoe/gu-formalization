---
artifact_type: construction_and_scope_result
created: 2026-08-10
status: LOCAL_FIRST_ORDER_BOSONIC_MOVING_REDUCTION_CONSISTENT_TRUNCATION_CANDIDATE__NOT_FERMION_SELECTOR__INDUCED_FERMION_OPERATOR_REQUIRED
ledger_rows: [RA-D2, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1, LT-GR1, LT-GR2b, LT-GR3]
canon_verdict_change: none
---

# Selected K77 action-owned reduction and carrier typing

## Result in plain English

The current moving reduction is a legitimate **local first-order bosonic
consistent-truncation candidate**, but it is not yet a nonlinear/global
subtheory or a selector for the proposed `192`-dimensional fermion carrier.

Three existing exact results compose decisively:

1. the transported rank-`8128` connection projector and its rank-`8256`
   complement both survive the first-order Euler operator;
2. both the Spin and full-`U(64,64)` parent tangents retain the same stationary
   branches; and
3. ordinary observation does not select between them.

That is the definition of an admissible consistent truncation, not a dynamical
choice of one truncation. Exact projector variation confirms the distinction.
For `P_epsilon u=u`, allowed variations obey

```text
(1-P_epsilon) delta u = (delta P_epsilon) u,
P_epsilon (delta P_epsilon) P_epsilon = 0.
```

The moving-projector term transports the subbundle; it does not generate an
equation that creates or prefers it. A multiplier could enforce the constraint
and a penalty could prefer it, but either would be a new action object.

Most importantly, the two candidate selectors act on different spaces.
`P_epsilon` acts on connection coefficients (`8128+8256=16384`). The disputed
`640+832+192=1664` split lives in gamma-traceless spinor-valued one-forms.
Likewise, `D_varpi chi_epsilon=0` makes a connection preserve the two Weyl
halves; an exact counterexample shows that such a connection can freely mix a
proper subspace inside either half. Weyl compatibility therefore does not
select the `j=1` triplet.

## Layer 0

| phrase | object here | not the same object |
|---|---|---|
| moving Spin projector | real-form/adjoint parity projector on bosonic connection coefficients | fermion-generation projector |
| `D_varpi chi=0` | compatibility with a moving two-Weyl-half reduction | preservation of the `j=1` triplet inside `ker Gamma` |
| Euler sector closure | consistent truncation | unique vacuum or action preference |
| fixed `W` theorem | theorem conditional on a supplied fermion subspace | derivation of that subspace |
| induced fermion operator | representation of the selected connection/action on the common K77 RS bundle | an already-built map |

The relevant physical test is not yet “apply `P_epsilon` to five fermion
subspaces.” It is first to construct the common K77 fermion bundle and the
action-derived odd operator or BV differential, then test whether its kernel,
cohomology or spectral projector distinguishes the proposed `W` from its
mirror, planted random `192`s, `640`, and `832`.

## Exact variational result

For a projector family `P(t)^2=P(t)`, differentiation gives

```text
P dP P = 0,
(1-P)dP(1-P)=0.
```

Thus the shape derivative is off-diagonal. On a field constrained by `u=Pu`,
the tangent equation is `Q delta u=dP u`, not `Q delta u=0`. The exact rational
model verifies this identity and plants the frozen-projector failure.

When the Euler operator commutes with `P`, both `P` and `Q` are invariant. The
complement Euler equation vanishes on the `P` subtheory, so the restriction is
consistent. But the complementary theory is consistent as well. The reduced
variation supplies `P^*E=0`; it does not supply the missing constraint as an
Euler equation. This is exactly compatible with the repo's full-parent result:
both parent tangents are stationary and `parent_selected=false`.

## Source return

The source owns the full `U(64,64)` principal arena, two Weyl halves,
connection-valued `varpi`, moving `epsilon`, and associated fermion grammar.
The checked material does not print a finite physical `192` projector or an
action-derived map from the bosonic coefficient reduction to the RS
`640/832/192` decomposition.

```text
SOURCE-CONFIRMS: full P_H, moving connection/reduction grammar and associated fermions
SOURCE-SILENT: finite physical carrier projector and induced odd selection operator
REPO-DERIVES: exact consistent-truncation/selector separation
```

## Efficient specialist preassessment

- **Layer-0 semantics — ACTUAL MATH, very high.** The two decompositions have
  different ambient spaces and dimensions. No label can substitute for an
  intertwiner.
- **Prior art — ACTUAL MATH, very high.** v0.130 gives two-sector closure and
  v0.112 gives stationarity on both parents; replaying the expensive evaluator
  would add no information.
- **Principal-bundle geometry — ACTUAL MATH, high.** `D_varpi chi=0` is a
  reduction-of-structure-group compatibility equation, not an isotypic
  projector inside an associated RS bundle.
- **Representation/Clifford — ACTUAL MATH, high.** A block connection can mix
  every proper subspace within a Weyl block; the exact four-dimensional model
  provides a counterexample.
- **Variational bicomplex — ACTUAL MATH, very high.** Constrained and
  unrestricted variations produce different Euler systems; a constraint is
  not generated by restricting the field space.
- **Symplectic/BV — ACTUAL MATH, high.** A configuration subbundle is not yet a
  characteristic quotient or physical cohomology.
- **Operator/PDE/Krein — ACTUAL MATH, high.** Finite closure supplies no
  fundamental symmetry, Fredholm domain, positivity or propagation theorem.
- **Source criticism — ACTUAL MATH, high.** The source supports the grammar but
  is silent on the finite selector.

## Accounting and next gate

No scientific verdict, residue, quotient, datum, P1/P2/P3 or public posture
moves. Nine ledger rows migrate in distance/scope only.

```text
headline_delta: none
conditions_closed: 2
  - the current bosonic moving reduction is typed as a consistent truncation
  - direct use of that projector as the 192/640/832 discriminator is rejected
conditions_opened: 1
  - construct the induced K77 fermion operator/BV differential on one common RS carrier
remaining_named_conditions: 3
```

The Build queue now has two serial gates:

1. finish the bosonic action-parent question by deciding whether a source term,
   multiplier-free constraint, or global/BV condition uniquely owns the moving
   reduction; and
2. construct the induced K77 fermion operator on `ker Gamma`, then run the
   five-way carrier discrimination and physical-cohomology test.

Evidence: exact composition probe `28/28 PASS` (final count verified by its
receipt). No random sampling and no complexified signature decision are used.
