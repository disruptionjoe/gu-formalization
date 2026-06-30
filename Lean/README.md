# Lean Certificates

This directory contains the repo's first Lean 4 + mathlib robustness layer.

The boundary is deliberately narrow:

- Lean checks finite mathematical kernels.
- Markdown owns interpretation, source provenance, and physics scope.
- Python audits continue to parse repo artifacts and enforce process gates.

Certified files should not contain `sorry` when cited by canon or active-research
documents.

## Current Certificates

| Lean file | Scope | Owner surface |
|---|---|---|
| `GUFormalization/Status.lean` | Claim-status order and dependency monotonicity kernel | `lab/process/runbooks/claim-status-consistency-quality-workflow.md` |
| `GUFormalization/K3IndexArithmetic.lean` | Symbolic K3/RS index arithmetic used by current audits | `lab/active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md` |
| `GUFormalization/W2Polynomial.lean` | Algebraic `F_2` polynomial identities behind the corrected `w2(Y14)` calculation | `canon/w2-y14-spin-structure.md` |

## Local Commands

After installing Lean/elan:

```powershell
lake update
lake exe cache get
lake build
```

Or use:

```powershell
.\automation\check-lean.ps1 -Update -Cache
```

The current shell used for the initial scaffold did not have `lean`, `lake`, or
`elan` installed, so the first pass was source-level plus Python surface-audit
verification.
