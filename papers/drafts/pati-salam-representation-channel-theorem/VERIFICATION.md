---
title: "Pati-Salam representation-channel theorem verification"
status: draft
document_role: draft
operational_state: verified_local
updated_at: "2026-09-02"
---

# Verification

The package-level command is:

~~~sh
python3 papers/drafts/pati-salam-representation-channel-theorem/reproduce_all.py
~~~

It runs the independent composition certificate twice—baseline and hostile
selftest—then the upstream exact weight-character probe and the existing Lean
intersection kernel. A green result establishes the finite D5 support
intersections, held Pati-Salam singlet filter, paired-real and source-typing
fences, and consistency with the banked calculations.

The executable boundary does not construct Clebsch coefficients, a source
action term, form-leg contraction, family covector, stationary background,
physical operator, observation quotient, mass, scale, threshold or prediction.
The independent certificate uses only the Python standard library; the
upstream probe uses the repository's existing exact character engine.
