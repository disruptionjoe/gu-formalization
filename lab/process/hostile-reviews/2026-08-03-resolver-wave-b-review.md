---
artifact_type: hostile-review
created: 2026-08-03
status: complete
subject: Resolver Wave B
verdict: PASS_AFTER_REPAIRS
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Hostile review — Resolver Wave B

## Final verdict

**PASS AFTER REPAIRS.** Three disjoint read-only reviewers covered the RS
principal symbol, compact representation/Krein chain, and the two-sided
summary/stale-object failure modes. The repaired packet reruns green:

- Q3 exact coefficient certificate: `584/584`;
- DQ3 exact constrained-neutrality certificate: `103/103`;
- DQ1 dependency-free Weyl/arithmetic certificate: `21/21`;
- independent Sage 10.9 character certificate: `12/12`;
- combined direct assertions: `720/720`;
- Resolver Wave A/B scope gates, process-gate inventory,
  generation-sector inventory, certificate-shape gate, JSON parse, Python
  compilation, and `git diff --check`: PASS.

## Blocking findings repaired

### Q3 symbol/type review

1. Replaced the ill-typed chiral “commutator” with
   `Delta_h^±=sigma_R^±P_h^±-P_h^∓sigma_R^±` and the intrinsic quotient
   leakage `H^± -> R^∓/H^∓`.
2. Made chirality reversal explicit: `H^-=X(S^+)`, `H^+=X(S^-)`.
3. Relabelled ranks as theorem-inferred from the exact `2e_b` witness and
   invertibility, rather than pretending the coefficient script called a
   rank routine.
4. Passed explicit `(9,5)` and `(7,7)` sign vectors and checked the
   nondegenerate-Clifford/even-dimensional premises.
5. Preserved the exact kill scope: sole-leading-II / invariant raw block only;
   coupled, compressed, physical-quotient, ellipticity, and domain routes stay
   open.

An independent explicit Cl(9,5) replay by the hostile reviewer found leakage
rank 128 for all 14 coordinate directions and rank 64 on both chiral halves.
It corroborates but is not folded into the exact assertion count.

### DQ3 Krein/adjoint review

1. Replaced the raw seven-word by the phased Hermitian involution
   `beta_7=i e_0...e_6`; the nine-word needs no phase.
2. Added every exact `e_a^dagger beta=beta e_a` identity, so
   `Gamma-sharp` is proved to be the metric/Krein adjoint.
3. Derived the B-orthogonal splitting from the adjoint identity together with
   `Gamma Gamma-sharp=14I` before inferring nondegeneracy and inertia
   `(832,832)`.

### DQ1 representation/summary review

1. Removed the optional `python-flint` import from the ordinary certificate.
2. Added a separate Sage character-ring route verifying actual B4/B2 tensor
   decompositions, without adding Sage to the base Python harness.
3. Split executable exact branching from the named standard compact-Clifford
   reality inputs.
4. Added the missing analytic Schur chain: central quotient, real/quaternionic
   types, K-invariant nondegenerate cross-pairing, multiplicity-one distinct
   types, and hyperbolic `(1,1)` multiplicity forms.
5. Fenced Weyl isotropic halves from positive/negative Krein sign spaces and
   graded residual dimension 12 conditionally at the precise carrier/group
   scope.

### Meta/stale-object review

1. Propagated `P_hinge` versus external P3 back into the Wave-A handoff.
2. Added register Revision 4 so the next named gate is no longer stale.
3. Rebased Wave C: a 126 occurrence can show representation-channel
   availability only—not coupling, mediation, mass, or A/B adjudication—and
   the bilinear→Krein→reality→VEV→induced-4D-mass checklist remains mandatory.

## Standing boundary

This review licenses the pre-deposit finite-kinematic results only. It moves no
claim, canon result, bar(b), H59, generation count, public posture, external
datum, or lane status. P1/P2/P3 remain unchanged and unused.
