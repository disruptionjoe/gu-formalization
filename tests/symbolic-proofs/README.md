# tests/symbolic-proofs/

Symbolic structure-level certificates for the core theorem package. These
scripts check load-bearing algebraic identities over symbolic entries rather
than only over the explicit numeric carrier. They are computational
certificates, not claim-status updates. A green run means the listed symbolic
identities still reproduce their current zero checks; it does not change
verdicts, change public posture, promote canon, or replace a governed Lean,
Coq, or Z3 formalization.

## Running This Family

List the tracked certificates:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/symbolic-proofs --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/symbolic-proofs --timeout 300
```

Run the certificate directly when reviewing the symbolic proof surface:

```powershell
python tests\symbolic-proofs\core_theorems_symbolic_proof.py
```

## Boundary

The public boundary stays:

- These checks are symbolic identity certificates and structure-level proof
  scaffolds, not a verdict change for GU or for the generation-count question.
- The script records the current sandbox boundary: no Lean, Coq, or Z3 proof
  artifact is supplied here.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

| script | role | current shared outcome |
|---|---|---|
| `core_theorems_symbolic_proof.py` | Symbolically checks the cross-chirality Krein-space identities, null-eigenspace transversality, Gamma-odd spectrum pairing, and 2-primary obstruction formulas. | Reproduces the current structure-level zero identities while keeping formalization and verdict boundaries explicit. |

## Process Gate

`process_gates/symbolic_proofs_readme_inventory_audit.py` keeps this README
synchronized with the tracked direct scripts in this directory and checks that
the symbolic / not-a-verdict-change / no-formalization boundary remains visible.
