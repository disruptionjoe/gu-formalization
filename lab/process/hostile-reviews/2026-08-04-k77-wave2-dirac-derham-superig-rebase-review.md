---
title: "Hostile review: K77 Wave-2 Dirac--de Rham and super-IG rebase"
date: 2026-08-04
status: complete
verdict: PASS_WITH_MATERIAL_SCOPE_REPAIRS__GATE_PARTIAL
review_charges:
  - summary_outruns_artifact
  - artifact_defends_superseded_object
  - operator_pde_and_krein_typing
---

# Hostile review

## Verdict

`PASS_WITH_MATERIAL_SCOPE_REPAIRS__GATE_PARTIAL`.

The packet may replace the previous Wave-2 blocker. It may not close Wave 2
or promote the operator to a global GU fermion equation. The exact result is a
source-guided **principal K77 candidate** with a conditional nonchiral action
placement. The remaining gate is the global draft-9.16/Hodge/Krein/
preboundary/domain placement on the same field space as the bosonic action.

## Reviewer 1: where the summary outruns the artifact

**Charge.** Find every sentence which sounds as though the source's complete
operator or three physical generations have been recovered.

**Findings and repairs.**

1. The first draft said “the GU operator.” Repaired to “the strongest
   released-source-guided principal candidate.” The exact source matrix still
   has unresolved `rho(epsilon)`, sign, coefficient, reality, and lower-right
   placement.
2. “Characteristic set is the null cone” is permitted only for the frozen
   symbol. The coordinate formula is built from wedge, metric contraction,
   Clifford contraction, and Hodge identification, hence is Spin-equivariant;
   positive, negative, and nonzero-null covectors form the relevant rank
   orbits. No statement about subprincipal characteristics, evolution, or a
   closed domain is allowed.
3. The prime computation alone would only lower-bound rational rank. The
   packet now pairs its rank-1024 minor with an explicit 896-coordinate kernel,
   fixing null rank exactly. Sage is an independent replay, not the proof's
   only route.
4. Curt's steps 19--23 are kept as a detailed derivation map. The report says
   three **kinematic pieces**, never three chiral generations, and P3 remains
   unused.
5. A cross-paired Krein Hessian is an exact architecture control, not an
   identity to draft equation 9.16. The report now labels it a conditional
   variational completion.

**Disposition:** repaired. The summary no longer outruns the artifact.

## Reviewer 2: where the artifact defends a superseded object

**Charge.** Determine whether the previous demand for a full odd action and
odd Ward/BV identity was a native GU requirement or an imported spacetime-
supersymmetry target.

**Finding.** It was superseded as a Wave-2 exit requirement. In the TOE
conversation at `01:43:43--01:44:14`, the action question is raised and Eric
says it is not what is needed to do GU. Portal 2020 `01:29:47` places products
of spinorial fields in the linear connection sector and explicitly declines
the nonlinear target. These sources call for an algebraic super-extension,
not necessarily an odd action symmetry.

**Repair.** The packet does not claim that odd action/BV is impossible. It
changes the requirement to:

- a globally defined odd module;
- a symmetric bracket into the linear connection sector;
- even equivariance and Jacobi;
- real-pairing/source-group compatibility; and
- associated-bundle/sheaf descent.

An odd Ward/BV identity becomes conditional on a future assertion of odd
action symmetry. It no longer blocks the current even action/Euler program.

**Disposition:** repaired. The lane is no longer defending an orthodox,
source-unasserted object.

## Reviewer 3: operator/PDE/Krein attack

**Charge.** Try to break the actual mathematics rather than the labels.

**Checks.**

1. Restored the omitted trace-removal term
   `-xi_a gamma^b zeta_b` before the admitted run. Ranks were recomputed with
   the full middle symbol.
2. Positive and negative non-null representatives are full rank `1920`.
3. For `xi=e_0+e_7`, `gamma(xi)^2=0` and rank is `64`. The null kernel is
   explicitly parameterized by arbitrary `zeta_0`, `zeta_7=zeta_0`, twelve
   independent `ker gamma(xi)` components, and forced `nu`, giving
   `128+12*64=896`.
4. The second adjacent symbol composition is generically nonzero, so the
   packet correctly refuses to call the released chain a complex.
5. The `d_A/d_A^*` off-diagonal pairing is exact. The middle block is neither
   self- nor skew-adjoint for the frozen `B` pairing. This prevents a hidden
   self-adjointness claim and motivates, but does not source-select, the
   nonchiral cross-pairing.
6. The mixed moment map was tested on actual opposite K77 half-spinors. It is
   nonzero and lies in both stabilizers; same-half input is a zero plant.
7. The conditional `gl(64,R)` result is not equated with the full source
   group. Global descent and the group-level integration remain open.

**Remaining PDE hazards.**

- lower-order curvature and moving-Hodge/Shiab terms;
- a common invariant dense domain and boundary conditions;
- constraint propagation and Green data;
- observation-section leakage;
- selected Lorentz time and positive-majorant/evolution questions; and
- the relation between the 896 null symbol kernel and any physical quotient.

**Disposition:** exact principal result passes; analytic/global promotion is
forbidden.

## Final acceptance boundary

The packet is accepted only with all of the following held:

- Wave 2 remains partial;
- the full odd action/Ward target is rebased, not disproved;
- the exact draft/source operator is still open;
- the cross-paired fermion action is conditional;
- three kinematic pieces do not imply three generations;
- no observation, domain, vacuum, Standard Model recovery, P1/P2/P3 use,
  canon change, lane change, or public-posture change occurs.
