---
title: "B5 independent reconstruction: finite symbol-class enumeration contract"
status: active_research
doc_type: run-plan-and-receipt
run_id: RUN-20260723-054357-gu-formalization-progress-b5-symbol-contract
parent_run_id: RUN-20260723-054357-repository-work-cycle-nbl-hourly
owner_id: gu-formalization
workflow: repo-progress-run
workflow_revision: sha256:25cb22688e2404b68de1127adbdea940c782335698debddaa665cc73274d9dcc
mode: execute
lane_id: "1"
starting_revision: e089f37a0f9edea43b5a9f8698fd820fdebe53f8
completed_at: 2026-07-23T05:50:33-05:00
claim_status_change: none
canon_change: none
method_refs: []
---

# B5 independent reconstruction: finite symbol-class enumeration contract

## Result

`ENUMERATION-CONTRACT-FROZEN`.

The independent B5 build is now an exact finite representation-theoretic
enumeration problem. This run does **not** claim that the class is already
enumerated, does not select a favorable differential, and does not issue either
`B5-MIDDLE-CONSTRUCTION` or `B5-MIDDLE-OBSTRUCTION-INDEPENDENT`.

The material advance is the completeness gate below: a future symbol list is
admissible only if it exhausts a declared matrix of intertwiner spaces. The
currently named twistor/divergence/Dirac-type symbols are seeds in that matrix,
not evidence that the matrix has no other entries.

## Construction fork and ceiling

This is the independent, conditional construction, not Weinstein's unreleased
native complex. It asks whether an explicitly chosen full finite class contains
an operator-grade recovering action on the `(9,5)`/Rarita-Schwinger carrier.
Every use of the orientation bit `sigma`, the odd-primary datum `tau`, a
families pushforward, a boundary spectral section, or BV-to-boundary data is a
named postulate.

The ceiling is operator-grade conditional recovery. Native uniqueness is
unreachable under the external-sigma result. Failure of the full enumerated
class is a successful obstruction result and must be reported at equal weight.

## Frozen carrier ledger

At symbol grade, retain the typed pieces already established by the B5
campaign:

- `S`, the spinor carrier;
- `R = ker Gamma`, the Rarita-Schwinger carrier;
- the three provenance copies that induce `3E_+ plus 3E_-`; and
- `X`, the 1536-dimensional extra block that must not disappear by notation.

Let `V` be the cotangent/vector symbol slot. For every ordered carrier pair
`(W_i, W_j)` in the frozen ledger, define

```text
m_ij = dim Hom_H(V tensor W_i, W_j),
```

where `H` is the declared observer group at the selected real/Krein fork.
The full first-order principal-symbol class is the direct sum of these finite
Hom spaces, tensored with the explicitly declared provenance-multiplicity
endomorphisms. A class is not complete until every `m_ij` is computed and its
real/Krein compatibility is classified.

## Known generators: admitted as seeds, not a completeness claim

Current owner evidence names four typed generator families:

1. the spin Dirac symbol `c_S(xi): S -> S`;
2. the projected twistor symbol
   `T(xi) = P_kerGamma(xi tensor -): S -> R`;
3. the divergence/gamma-contraction symbol `delta(xi): R -> S`; and
4. the projected RS Dirac-type symbol
   `c_R(xi) = P_kerGamma c(xi) P_kerGamma: R -> R`.

The campaign establishes uniqueness up to scale for the projected twistor and
divergence slots. It does not yet certify the complete `m_ij` matrix over the
selected real/Krein observer group. The mixed super-IG bracket `beta` is a
compatibility constraint on the eventual differential and BV action; it is not
silently counted as another first-order principal-symbol basis vector.

## Enumeration and hostile controls

The next bounded computation must:

1. compute the full multiplicity matrix `m_ij` over the complexified carrier;
2. impose the declared real form and Krein adjoint conditions without changing
   the carrier after seeing the result;
3. expand every provenance-multiplicity coefficient rather than identifying
   the three lines by symmetry fiat;
4. classify every basis vector and allowed coefficient matrix under the
   explicit mirror exchange `J`;
5. send every `J`-even class to the mirror-cohomology obstruction; and
6. send every `J`-breaking survivor to symbol exactness on
   `3E_- plus X`, while preserving all three `E_+` provenance lines.

Planted controls:

- omitting `X` fails completeness;
- identifying the three provenance lines before enumeration fails the target
  ledger;
- counting `beta` as a principal symbol fails typing;
- importing a favorable lower-order term to repair a failed symbol fails the
  predeclared class; and
- calling symbol exactness physical BV cohomology fails the grade boundary.

## Outcome register

- `B5-SYMBOL-CLASS-COMPLETE`: every `m_ij` and real/Krein condition is closed;
- `B5-SYMBOL-MIRROR-OBSTRUCTION`: the full class is mirror-even or otherwise
  forces paired chiral cohomology at symbol grade;
- `B5-SYMBOL-SURVIVORS`: a complete, explicit `J`-breaking survivor list moves
  to symbol exactness;
- `B5-MIDDLE-OBSTRUCTION-INDEPENDENT`: only after the complete class fails all
  allowed routes; and
- `B5-MIDDLE-CONSTRUCTION`: only after global/BV deformation-retract and
  family-superconnection certificates, not at symbol grade.

## Rerank

Lane 1 remains first. Within Lane 1:

1. compute the exact `m_ij` multiplicity matrix and mirror parity under this
   frozen contract;
2. retain `ANOMALY-DESCENT-HARDENING` as the strongest parallel alternative;
3. keep native B5 source recovery parked as a distinct provenance question;
4. do not rerun Q1a, Q2, or the resolved LP/LC fork.

## Validation and receipt

- Current authority, Lane state, portfolio, source/action evidence, B5 scope,
  mirror lemma, and CH-SRC toy were read.
- The preceding material-change Discovery phase closed S2-S5 before Progress.
- No heavy build or test suite ran.
- Lightweight syntax validation is required for the updated YAML and JSON
  control surfaces; `git diff --check` is required before commit.
- Phase result: `progressed`.
- Owner effects: this frozen contract, Lane-state refresh, portfolio advance,
  and NEXT-STEPS handoff.
- Claim/canon/verdict/publication changes: none.
- Method refs/effect: `[]` / `null`.
- Exact wake: the full `m_ij` multiplicity matrix and real/Krein mirror
  classification can be computed under this frozen carrier ledger; a defect in
  the ledger, construction fork, or completeness controls appears; or another
  material owner change lands.
