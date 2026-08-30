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
| `GUFormalization/Status.lean` | Claim-status order and dependency monotonicity kernel | `lab/methods/claim-status-consistency.md` |
| `GUFormalization/K3IndexArithmetic.lean` | Symbolic K3/RS index arithmetic used by current audits | `lab/active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md` |
| `GUFormalization/W2Polynomial.lean` | Algebraic `F_2` polynomial identities behind the corrected `w2(Y14)` calculation | `canon/w2-y14-spin-structure.md` |
| `GUFormalization/LocatedNotForcedLegs.lean` | Finite located-not-forced theorem-grade legs: Krein transversality, corrected star-semilinear images with explicit null-image premises and `intersectionDifference = 0`, plus 2-primary identities. This is finite complex Hermitian image-subspace algebra only, not physical-real-form, Fredholm, observed-handedness, or generation-selection content | `canon/core-theorems-symbolic-proof-RESULTS.md`; `explorations/conditional-build/conditional-build-frontier-and-antilinear-null-images-2026-08-22.md` |
| `GUFormalization/LocatedNotForcedFiniteCore.lean` | Finite census encoding and `decide`-checked closure over supplied census data | `papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md` |
| `GUFormalization/ResidualSelection.lean` | Residual-selection finite logic kernels | `papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md` |
| `GUFormalization/GroupActionFixedPoints.lean` | Set-level group-action classification: invariant valuations are equivalent to functions valued in the common fixed-point subtype; on inhabited domains they exist exactly when that subtype is nonempty; empty-fixed-set and fixed-point-free-element no-invariant corollaries follow. No physical action or GU verdict is encoded | `VERIFICATION.md` |
| `GUFormalization/GroupActionFixedPointsAxioms.lean` | Default-target `#print axioms` surface for the complete group-action theorem family | `VERIFICATION.md` |
| `GUFormalization/R4TwoArena.lean` | Two-arena weight-parity, CRT, and 2-primary-blindness proof legs | `canon/two-arena-rep-theory-core-RESULTS.md` |
| `GUFormalization/CoflipCore.lean` | Co-flip finite core (CH-REC P1/P2): (1,1) Krein toy rigidity, zero-import diagonal action, split-costs-one, split parity | `explorations/hardening-h2-lean-coflip-2026-07-19.md` |
| `GUFormalization/CoflipAbstract.lean` | Abstract `(eps,mu)` co-flip sign accounting: zero-import diagonal, exact one-bit split price. The `FiniteSignature` field and the `witnessed` Prop are carried but formally inert — no proof uses them (descoped 2026-08-03) | `explorations/hardening-h1-exhaustiveness-2026-07-19.md`; `explorations/hardening-h4-class-generalization-2026-07-19.md` |
| `GUFormalization/CompactImageObstructions.lean` | Extremal-weight annihilation and explicit square-zero-block kernels; carrier faithfulness and compactness remain outside Lean | `papers/candidates/good-stable-compactification-no-go/REPRODUCE.md` |
| `GUFormalization/CompactImageObstructionsAxioms.lean` | Default-target `#print axioms` surface for the compact-image kernels | `papers/candidates/good-stable-compactification-no-go/REPRODUCE.md` |
| `GUFormalization/FiniteResearchKernels.lean` | Finite achirality-trace, mod-3, and rational phase-boundary kernels | `lab/process/lean-verification-lane-LEDGER.md` |
| `GUFormalization/FiniteResearchKernelsAxioms.lean` | Default-target `#print axioms` surface for the finite research kernels | `lab/process/lean-verification-lane-LEDGER.md` |
| `GUFormalization/PowerMeanReduction.lean` | Finite Cauchy--Schwarz/power-mean kernel, exact 96-cell corollary, and constant-magnitude equality witness; no spectral or physics realization is encoded | `explorations/big-swing-2026-07-07/A1-native-potential-alignment.md`; `explorations/conditional-build/conditional-build-frontier-and-l7-power-mean-2026-08-22.md` |
| `GUFormalization/ChiConjugationTraceParity.lean` | Finite matrix proof that ordinary power traces are even and traces weighted by a conjugation-odd matrix are odd under an involution; no carrier, gauge, vacuum, or physical-orientation realization is encoded | `explorations/big-swing-2026-07-07/A2-native-ring-symmetry-nogo.md`; `explorations/conditional-build/conditional-build-frontier-and-l8-chi-parity-2026-08-22.md` |
| `GUFormalization/InvolutionProjectorKernels.lean` | Abstract inner-involution automorphism and commutator parity, plus complementary linear involution projectors; no carrier, Cartan positivity, maximal-compact, dynamics, spectrum, or physical-sector realization is encoded | `explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md`; `explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md`; `explorations/conditional-build/conditional-build-frontier-and-l9-involution-projectors-2026-08-22.md` |

## Standalone Lean Certificates

| Lean file | Scope | Owner surface |
|---|---|---|
| `GUFormalization/ResidualSelectionAxioms.lean` | Manual, informational `#print axioms` receipt outside the default target; run with `lake env lean` | `lab/process/lean-verification-lane-LEDGER.md` |
| `tests/big-swing/R4_TwoArena.lean` | Compatibility entrypoint importing the default-target R4 module | `canon/two-arena-rep-theory-core-RESULTS.md` |

## Local Commands

After installing Lean/elan:

```powershell
lake exe cache get
lake build
```

The committed `lake-manifest.json` is the dependency lock.  Do not run
`lake update` as a routine reproduction step: the mathlib input tracks
`master`, so an update can advance both the manifest revision and the required
Lean toolchain.  Use it only when intentionally updating and reviewing the pin.

Or use:

```powershell
.\lab\automation\check-lean.ps1 -Update -Cache
```

The process gate `process_gates/lean_certificate_surface_audit.py` derives the
default-target certificate inventory from `GUFormalization.lean`, requires
every library module to be imported or explicitly declared as a manual
non-default certificate, and checks the Lean map, ledger, owner references, and
proof-body placeholder hygiene. It is a routing and governance gate, not a
replacement for `lake build` or targeted standalone Lean checks.
