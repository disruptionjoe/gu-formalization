---
title: Six-spinor grading — internal mathematical and hostile source review
status: process
doc_type: review
created: '2026-11-24'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: F16-K95-SPECTRAL-R6-BN0-GRADED-EXTENSION
target_claim_verdict: EXCLUDED_IN_DECLARED_RECONSTRUCTION
canon_verdict_change: none
---

# Review disposition

**Accepted at internal T1 in the preregistered F16-K95-spectral/R6-Bn0
realization.** Two mathematical specialists and a separate hostile
source/domain specialist reviewed the proof, followed by root's serialized
exact and Lean checks. These are simulated specialist agents, not independent
human experts or external certification. Base `d1cc9825ef3aaf18f7bf5c515a9e3b8302c53a0b`.

## Independent mathematics

`wave_global_reduction` independently derived the complete receiver symbol
in `(b,sigma=tau-Gamma_H b,nu)`. The perpendicular horizontal principal
block forces the entire sigma residual row to vanish, then the scalar row,
even for arbitrary spinor endomorphism blocks. No diagonal or scalar ansatz
for the competing observed grade is used. Parallelism of the unique grade
under the held split connection closes the derivative-of-grade alternative.

`krein_index_review` independently rederived that proof and both torsion
coordinate witnesses. The allowed raw input is `b=J_H psi,sigma=nu=0`, with
original total trace `tau=4psi`; it is not a falsely gamma-traceless input.
Selfadjoint shape operators give `F(J_H psi)=c_N(H_mean)psi`, with
`H_mean^2=-1`. The sigma and original tau coefficients differ because the
latter includes Gamma_H of the b-row output. The full defect has rank **at
least128**; only the restricted spinor witness is rank128. The surjective
quotient identity excludes hidden-grade and kernel-preserving-shear repairs
of this same observed operator without an exhaustive commutant calculation.

Both accepted the conditional Lean core: residual-row annihilation,
receiver uniqueness, oddness descent and injectivity from the supplied
square laws and nonzero coefficient. The native geometry and connection
identities are explicit mathematical premises, not fully Lean-formalized.

## Hostile source and observation review

`wave_observation_domain` checked SC-OP-04/05, SC-CHI-01/04/51/52,
SC-META-56, the actual full observation and source independence of bars.
The result tests the existing zero-SE, natural two-channel reconstruction
with B_n=0, coherent normal jets, density repair and retained exterior
torsion. It does not establish that same-field/equation oddness is a source
obligation. Source effective chirality and 2+1 labels, nonzero-SE rivals,
barred currents, global domains and class-C nonemptiness remain open.
K95's skew-sharp grade law is retained; no positive-metric substitution or
K77 transfer is made. The rank1664 RS carrier is not substituted for raw E1920.

Two integration corrections were applied: the exact probe filename now
matches its owner path; SC-META-56's odd-group/action demand is explicitly
distinct from the fermion-chirality anticommutator used here.

## Held constant-W follow-through

The reviewers requested the already-owned constant chiral wrapper be checked
before scheduling broader work. Root recorded this bounded corollary in the
scope document before calculation. Mathematical and hostile source reviews
accepted `F_o=diag(W,Wbar,I)`, `L_o=diag(I,I,W)` and crossed contraction
`Gamma W=Wbar Gamma`. Principal uniqueness is reproved directly with the
invertible perpendicular block multiplied by Wbar; it is not inferred from
arbitrary left/right equivalence. Parallel W and the forced grade commute,
so the defect transports exactly. Transporting the input by W inverse
preserves the original nonzero trace witness. The held wrapper is excluded
as a repair; variable wrappers and distinct field/equation transformations
remain outside. No physical-necessity bridge is supplied by this corollary.

## Verification and continuation

Root ran all40 exact rational Clifford controls and compiled
`Lean/GUFormalization/SixSpinorGrading.lean` successfully, with no sorry.
The probe checks native signatures, full principal coefficients, wrong-sign
controls, torsion, both coordinate witnesses/inverses, omitted-torsion false
survival, and actual W observation/defect transport. Generic coefficient
scope and arbitrary endomorphism uniqueness belong to the written proof;
the rational control point is not a fitted or selected action.

The unchanged operator is excluded at this named grading-realization scope.
The next packet step classifies admitted metric normal-connection extensions
while preserving the complete observation, principal and exterior equations.
Neither a fitted connection nor the gated source operator is authorized.
The localization audit found neither promotion premise established and
records that the original brief relied on the withdrawn W175 native gap.

[Proof and exact scope](../../../explorations/conditional-build/six-spinor-grading-compatibility-2026-11-24.md),
[machine receipt](../six-spinor-grading-compatibility.json),
[Lean core](../../../Lean/GUFormalization/SixSpinorGrading.lean).
