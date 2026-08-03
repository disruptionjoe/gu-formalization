# Verification receipt

Date: 2026-08-03  
Scope: the manuscript and paper-specific evidence only

## Environment

| component | recorded version |
|---|---|
| Lean | 4.32.0-rc1, commit `b4812ae53eea93439ad5dce5a5c26591c31cb697` |
| Lake | 5.0.0-src+b4812ae |
| SageMath | 10.9, release 2026-05-04 |
| Python | 3.14.6 |
| uv | 0.11.24 |
| Hypothesis | 6.163.0, locked in `evidence/uv.lock` |

## Results

### SageMath exact quaternion certificate

Result: **PASS**

```text
PASS exact SageMath certificate: 2721 checks
decomposition: 8256 = 2080 + 4096 + 2080
arithmetic: rational quaternions; no floating point or tolerances
```

The count includes exact checks of the isotropic basis change and the
upper/diagonal/lower transformed grading blocks.

### Exact property-based certificate

Result: **PASS**

```text
PASS exact property certificate: 400 generated examples plus deterministic controls
arithmetic: integer quaternions; no floating point or tolerances
planted mutants rejected: wrong X_+ sign; noncommuting-is-not-purely-odd
```

### Lean paper kernel

Result: **PASS**

The paper-specific module and axiom-receipt module compile under the pinned
toolchain. The axiom receipt reports:

```text
conjugation_fixed_iff_commutes: [propext]
shifted_eigenvector: [propext, Quot.sound]
extremal_annihilation: [propext, Quot.sound]
xPlus_comp_zero: [propext]
xMinus_comp_zero: [propext]
xPlus_square_zero: [propext]
xMinus_square_zero: [propext]
```

These are standard Lean foundational axioms. There are no project-specific
axioms, `sorry` declarations, or admitted paper-facing results.

## Evidence boundary

This receipt does not certify the whole repository. It does not claim that
Proposition 1, Haar averaging, the full real-reductive theorem, quaternionic
Lie-group membership, or any physical interpretation is formalized in Lean.
It certifies only the exact commands and named files in `REPRODUCE.md`.

### Frozen-file checksums

Result: **PASS**

`evidence/checksums.sha256` freezes every paper-facing source and verification
artifact except the checksum manifest itself. An archival package must include
this complete tree; a manuscript-only copy does not expose the computational
evidence to its reader.
