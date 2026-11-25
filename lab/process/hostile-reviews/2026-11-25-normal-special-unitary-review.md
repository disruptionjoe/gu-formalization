---
title: Normal special-unitary existence independent review
status: process
doc_type: review
created: '2026-11-25'
---

# T2 acceptance and controls

Independent mathematical review accepts the concrete theorem and its proof.
This is internal review, not external-expert or proof-assistant certification.
No scientific matrix status or source/physics verdict is accepted here.

The review checked the actual Clifford double cover of SO0(6,4), rather than
its universal cover. The compact covering character is the sum of the two
rotation parities. S(U3×U2) has windings(1,-1), so its connected lift is
injective; SU(3,2) need not be simply connected. With the negative J fixed,
K/H is S7, not RP7, because the specified Spin cover retains the spinor sign.
The obstruction degree is eight, beyond the X/Y/cover homotopy dimensions.
This proves compatibility with the fixed total Spin, not merely matching w2.

The prescribed-c1 proof retains the full Spin^c lift and integral torsion.
The canonical determinant/half-spin convention was made explicit after review.
The normal determinant is never replaced by the already-trivial spinor one.
The negative c1 need not vanish: the positive factor cancels it.

Both strongest fixed-data countercontrols survive: the lens-space example has
nontrivial torsion determinant with zero real c1; the RP3 phase example has a
Spin discrepancy outside the image of integral H1. The latter concerns an
explicitly prescribed Spin lift and makes no assertion about which lift the
source inherited. Free positive J resolves both, as the theorem promises.

The source bridge remains optional SC-GRP03. Absolute existence neither selects
SU over U nor supplies a preserved connection, physical quotient, observed
chirality or domain. The previous closed-base square criterion is retained;
no claim of its universal solubility, no hypothetical boundary datum, and no
new blanket relative obstruction is introduced.

Root reproduction passed eleven exact finite controls, including the SU4
orbit/stabilizer ranks, paired winding parity, integral torsion cancellation
and nonzero phase Bockstein. Four stronger false alternatives are rejected.
These checks support the written proof; they do not formalize obstruction
theory. No Lean check or T1 kill is claimed.
