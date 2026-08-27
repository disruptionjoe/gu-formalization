---
title: "Boundary kappa sign and exceptional-point counterexample"
status: active_research
doc_type: construction_result
created: "2026-08-26"
grade: "EXACT FINITE-DIMENSIONAL PONTRYAGIN COUNTEREXAMPLE; NO GU BOUNDARY OPERATOR"
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
ledger_edit: none
cache: lab/process/boundary-kappa-sign-and-exceptional-point-counterexample.json
scripts:
  - tests/channel-swings/boundary_kappa_sign_and_exceptional_point_counterexample_probe.py
---

# Boundary kappa sign and exceptional-point counterexample

Scope: this result decides only what finite Pontryagin index can imply by
itself. It does not construct GU's boundary triple, Weyl function, generalized
Nevanlinna class, closed extension, physical boundary condition, or physical
exceptional point.

```gu-typed-objects
result: M-M7 boundary-kappa polarity adjudication and M-M24 kappa-only EP-bound counterexample
carrier: real two-dimensional Pontryagin space with fixed J=diag(1,-1); LAYER=toy CHIRALITY=N/A
pairing: indefinite bilinear form x^T J y ON=real-two-dimensional-Pontryagin-space
real_structure: real polynomial J-self-adjoint family
grading: positive versus negative J line
action_owner: N/A; no GU boundary operator constructed
target: logical implication from finite kappa to firewall polarity or parameter-count bound MAP-TYPE=evaluation
```

## Result first

M-M7 and M-M24 are executed at their implication-testing ceiling.

- `M-M7`: finite boundary \(\kappa\) alone has no firewall polarity. The
  owner council's nearest finite-Pontryagin theorem concerns spectral counts
  for one constructed operator; it does not say whether the missing GU
  boundary completion is a firewall or a closure mechanism. That direction
  still requires the actual boundary operator and Weyl function.
- `M-M24`: the proposed statement that fixed finite \(\kappa\) bounds the
  number of exceptional points along a family is false without an independent
  complexity bound.

## Exact fixed-index family

Fix

\[
J=\operatorname{diag}(1,-1),\qquad \kappa=1,
\]

and for any positive integer \(n\) define, on \(-1<t<1\),

\[
A_n(t)=\begin{pmatrix}
2T_n(t)&1\\
-1&-2T_n(t)
\end{pmatrix},
\]

where \(T_n\) is the Chebyshev polynomial. Exact multiplication gives

\[
A_n(t)^T J=J A_n(t),\qquad
A_n(t)^2=(4T_n(t)^2-1)I.
\]

Thus every member is `J`-self-adjoint on the same Pontryagin space of negative
index one. The equation \(4T_n(t)^2-1=0\) has exactly `2n` distinct roots in
`(-1,1)`: \(T_n(t)=1/2\) and \(T_n(t)=-1/2\) each contribute \(n\), and none
is critical because critical values of \(T_n\) are \(\pm1\). At each root,
\(A_n\) is a nonzero rank-one nilpotent. Its two eigenvalues and eigenvectors
coalesce, and the simple discriminant zero gives the local square-root
exceptional-point behavior.

The number of exceptional parameter values is therefore `2n` while
\(\kappa=1\) never changes. Since \(n\) is arbitrary, no bound depending only
on \(\kappa\) can control the number of exceptional points along arbitrary
families. A viable quantitative statement would need additional data such as
polynomial degree, analytic complexity, parameter domain, or a source-owned
boundary family.

## Hostile review and continuation

The counterexample does not contradict finite-index bounds on nonreal
eigenvalues of one fixed operator; it separates that spectral question from
counting defective parameter values across a varying family. It also does not
show that GU has any exceptional point. The missing Weyl/operator construction
is preserved rather than replaced by this toy family.

The exact probe checks `J`-self-adjointness, the square identity, negative
index one, `2n` simple discriminant roots and defectivity for
`n=1,2,3,5,8`. Planted mutations break `J`-self-adjointness, the root count,
defectivity and the false \(\kappa\)-only bound.

No source claim, ledger row, canon verdict, prediction, confirmation, paper,
priority or public posture moves.
