---
title: "Sigma/dark-energy sign-nonselection verification"
status: draft
document_role: draft
operational_state: verified_local
updated_at: "2026-09-02"
---

# Verification

The package-level command is:

```sh
python3 papers/drafts/sigma-dark-energy-sign-nonselection/reproduce_all.py
```

It runs the independent composition certificate twice—baseline and hostile
selftest—then the upstream Q2-FREE, W211, W219 and CC-1 certificates. A green
result establishes the finite two-orientation logic, the correction boundary,
the exact CC-1 countermodels and consistency with the frozen source packets.

The executable boundary does not construct the physical sigma-to-Lambda
bridge. It does not verify an interacting vacuum, physical state, observable
algebra, cosmological likelihood, dark-energy equation of state or source-
native prediction. The integrated certificate uses only the Python standard
library; the upstream controls use the repository's existing dependencies.
