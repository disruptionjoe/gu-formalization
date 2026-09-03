---
title: "Literal-observation gamma-kernel obstruction verification"
status: draft
document_role: draft
operational_state: verified_local
updated_at: "2026-09-02"
---

# Verification

The package-level command is:

~~~sh
python3 papers/drafts/literal-observation-gamma-kernel-obstruction/reproduce_all.py
~~~

It runs the independent theorem certificate twice—baseline and hostile
selftest—then the upstream exact Spin(6,4)/pullback probe, the general Lean
obstruction theorem, the independent corrected-projector probe and its Lean
kernel. A green result establishes the explicit ambient kernel lift, literal
pullback leakage, premise fences and consistency with the banked calculations.

The executable boundary does not construct a source observation intertwiner,
select a corrected projector, define an action or representative-independent
physical quotient, classify the observed leftover, assign a family or
chirality, derive a mass, or make an observable prediction. The independent
certificate uses only the Python standard library and exact rational
arithmetic.
