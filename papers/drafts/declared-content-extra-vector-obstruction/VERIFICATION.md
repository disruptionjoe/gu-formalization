---
title: "Declared-content extra-vector verification"
status: draft
document_role: draft
operational_state: verified_local
updated_at: "2026-09-02"
---

# Verification

The package-level command is:

```sh
python3 papers/drafts/declared-content-extra-vector-obstruction/reproduce_all.py
```

It runs the new independent composition certificate twice—baseline and hostile
selftest—then the four upstream PV-1, PV-2, MV-1 and MV-2 certificates. A green
result establishes exact arithmetic and consistency with those frozen packets.

The executable boundary is finite representation, root, dimension and anomaly
arithmetic. It does not verify a source-owned action, kinetic operator,
propagator, coupling, detector, cosmology or experimental constraint.

The integrated certificate uses only the Python standard library. PV-2 and the
non-load-bearing MV-1 empirical control use the repository dependencies in
`requirements.txt` (`numpy` and `sympy`); the capsule uses `_local/cas-venv`
when the launching interpreter lacks SymPy.
