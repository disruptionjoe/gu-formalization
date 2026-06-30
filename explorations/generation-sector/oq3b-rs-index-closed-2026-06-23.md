---
title: "OQ3b Closure: RS Sector H-Linear Index = 8 (Post-OQ1 Resolution)"
date: 2026-06-23
problem_label: "oq3b-rs-index-closed"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
depends_on:
  - explorations/generation-sector/oq3b-rs-index-8-2026-06-23.md
  - explorations/representation-theory-noncompact/oq1-split-rank-verification-2026-06-23.md
  - explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md
supersedes: oq3b-rs-index-8-2026-06-23.md (partial — this file closes the OQ1 gate only)
---

# OQ3b Closure: ind_H(D_RS) = 8 After OQ1 Resolution

## 1. What OQ1 Actually Resolved

The prompt states that OQ1 (split-rank = 1) is now RESOLVED, expecting this to close OQ3b.
The explicit matrix computation in `oq1-split-rank-verification-2026-06-23.md` did resolve
OQ1 definitively — but the resolution is:

```
split-rank(SL(4,R) / SO_0(3,1)) = 3   [NOT 1].
```

The key findings from that file:

- The correct symmetric-pair involution for (SL(4,R), SO_0(3,1)) is sigma_B with
  dsigma_B(X) = -J X^T J^{-1}, J = diag(1,1,1,-1).

- Under sigma_B: p_G cap q_B is 6-dimensional with basis
  {H_1, H_2, H_3, S_{12}, S_{13}, S_{23}}.
  Maximal abelian subspace a_q = span{H_1, H_2, H_3} (3-dimensional).
  Brackets [H_i, S_{jk}] land in k = so(4), not in p_G cap q_B.

- The earlier "split-rank = 1" result in n5-discrete-series §19 used sigma_A (the
  block-conjugation involution), which is the correct involution for a DIFFERENT
  symmetric pair, not for (SL(4,R), SO_0(3,1)).

- Flensted-Jensen equal-rank criterion: split-rank = 3 vs rank(SO(4)/SO(3)) = 1.
  3 != 1. Criterion FAILS for scalar L^2(SL(4,R)/SO_0(3,1)).

This means the prior OQ3b argument via scalar BC1 / Flensted-Jensen does not survive.
OQ1 resolves the split-rank question definitively, but in the direction that REMOVES the
previously claimed FJ guarantee, not confirms it.

---

## 2. What Sub-Conditions of OQ3b Depend on OQ1

OQ3b has three routes to ind_H(D_RS) = 8:

**Route A (Physical DOF count):**
- Input: RS field in 14D has (4 - 1 gamma-trace - 1 gauge) x C^16 = C^32 physical modes.
  Chiral half = C^16. dim_H(C^16) = 8.
- Dependence on OQ1: NONE. This route is independent of split-rank.
- Status after OQ1 resolution: UNCHANGED, reconstruction grade.

**Route B (Atiyah-Schmid / Flensted-Jensen formal-degree sum):**
- Prior version: Relied on split-rank = 1 for scalar L^2(G/H) to invoke FJ Theorem 3.1.
  This FAILS after OQ1 is resolved to split-rank = 3.
- Surviving version (tau-correction, from oq3b-rs-index-8 §4.2): The claim is that
  the EFFECTIVE split-rank of the TWISTED space L^2(G x_H tau_RS) is reduced from 3 to 1
  by the RS H-type tau = 4*D(1/2,0) + 4*D(0,1/2), via rank_correction(tau) = 2.
  This tau-correction formula has NOT been verified from a primary reference
  (Kobayashi-Oda or Oshima). It remains reconstruction grade.
- Status after OQ1 resolution: Prior scalar FJ route CLOSED. Tau-correction route
  CONDITIONALLY SURVIVES at reconstruction grade. Gate = explicit tau-correction formula.

**Route C (Physical generation count consistency):**
- Input: RS sector = 1 SM generation x 8 H-lines/generation = 8.
- Dependence on OQ1: NONE. This route uses SM quantum number counting, not split-rank.
- Status after OQ1 resolution: UNCHANGED, reconstruction grade.

---

## 3. Checking All OQ3b Sub-Conditions

| Sub-condition | Prior basis | Status after OQ1=3 |
|---|---|---|
| Scalar FJ discrete series exist for L^2(G/H) | split-rank=1 via FJ Th 3.1 | FAILS: 3!=1 |
| Tau-twisted FJ: L^2(G x_H tau_RS) has discrete series | Tau-correction rank=3->1 | CONDITIONALLY_RESOLVED: formula unverified |
| Oshima-Matsuki condition for twisted pair | rho_H - rho_G cone check | OPEN: not verified for this pair |
| Physical RS DOF = C^32, chiral half C^16, dim_H=8 | 4D RS constraint count | UNAFFECTED by OQ1 |
| S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2), 8 H-types | Branching computation | UNAFFECTED by OQ1 |
| Flensted-Jensen multiplicity-one per H-type | FJ Th 4.3 for effective split-rank=1 | CONDITIONAL on tau-correction |
| AF2 = 225/48 exact at lambda_RS | A3 root system computation | UNAFFECTED by OQ1 |
| RS sector = 1 SM generation = 8 H-lines | SM branching (COND_RESOLVED) | UNAFFECTED by OQ1 |

**Gate analysis:** OQ1 resolution eliminates one sub-condition (scalar FJ guarantee) and
leaves two paths intact that do not depend on scalar FJ at all (Routes A and C). The
scalar BC1 chain from rc1-rs-kk-zero-mode (tau-shift to nu_1 = 3/2 on BC1 Plancherel
poles) is superseded because the root system for the correct sigma_B metric pair is A3
(rank 3), not BC1 (rank 1). The BC1 c-function poles and the tau-shift to 3/2 were
derived under the wrong involution assumption and do not carry forward.

The ONLY analytic route that survives for ind_H(D_RS) = 8 from representation theory
is the tau-correction mechanism, which is reconstruction grade and has one unverified gate.

---

## 4. The Tau-Correction Gate (Primary Analytic Obstruction)

From oq3b-rs-index-8 §4.2, the argument requires:

```
rank_correction(tau_RS) = 2
```

where tau_RS = D(1/2,0) + D(0,1/2) of SO_0(3,1), so that:

```
effective split-rank = split-rank(G/H) - rank_correction(tau_RS) = 3 - 2 = 1.
```

If this formula is correct, the Flensted-Jensen theorem applies to the TWISTED space
L^2(G x_H tau_RS) (not the scalar L^2(G/H)), and the discrete series argument for
ind_H = 8 proceeds via the 8 independent H-types.

The formula rank_correction = 2 is attributed to Oshima (2011) / Kobayashi-Oda (2023)
but has not been explicitly verified for the pair (SL(4,R), SO_0(3,1)) with tau = D(1/2,0).
This is OQ3b-OQ1 (tau-correction CAS verification) from the parent file.

**Failure condition OQ3b-F1 (carried forward):**
If rank_correction(tau_RS) != 2, the effective split-rank is not 1, the FJ condition
for the twisted space may not hold, and the analytic route to ind_H = 8 fails.
The claim would then rest on Routes A and C only (physical DOF count + SM generation count),
both at reconstruction grade.

---

## 5. The Formal-Degree Mechanism (A3 vs BC1)

With split-rank = 3 and root system A3 (not BC1), the AF2 formal-degree computation
requires the full A3 Plancherel polynomial, not the 1-dimensional BC1 c-function.

From oq3b-rs-index-8 §5.2, the Harish-Chandra parameter lambda_RS = (1/2)(e_1-e_4) is
a principal series parameter for SL(4,R) with A3 root system. The AF2 value 225/48 was
computed from the A3 root system:

```
d(pi_{lambda_RS}) = P(lambda_RS + rho_G) / P(rho_G) = 225/48   [A3 root system, EXACT]
```

This computation is independent of whether the scalar split-rank is 1 or 3. It is a
statement about the G-Plancherel density of the representation pi_{lambda_RS}, which
is a G-level (not G/H-level) computation. The A3 formal degree 225/48 therefore
SURVIVES the OQ1 correction.

What does NOT survive is the claim that this G-Plancherel density is proportional to a
discrete atom in G/H. That requires either scalar FJ (fails, split-rank 3) or the
tau-correction (reconstruction grade).

---

## 6. The Oshima-Matsuki Condition

For the pair (SL(4,R), SO_0(3,1)) with sigma_B involution and split-rank 3, the
Oshima-Matsuki (1984) Theorem 6.11 gives a necessary condition for discrete spectrum
existence. From oq3b-rs-index-8 §3.2:

```
rho_H - rho_G projected on a_q_B = (-1, -1/2, 1/2, 1).
```

This is NOT in any dominant Weyl chamber for A3, suggesting the standard Oshima-Matsuki
condition for the UNTWISTED L^2(G/H) is not satisfied.

For the TWISTED L^2(G x_H tau_RS), the condition is modified by the tau representation.
The effective rho shift changes the projection and may place the twisted pair in the
required cone. This is the content of OQ3b-OQ2 (Oshima-Matsuki for twisted space)
from the parent file — open.

---

## 7. Three-Path Summary After OQ1

**Path 1 (Physical DOF count — most robust):**

RS physical degrees of freedom: (4 vector components - 1 gamma-trace - 1 gauge) x C^16 = C^32.
Chiral half: C^16. H-dimension: dim_H(C^16) = 8.
H-linearity of projection: exact from Cl(9,5) = M(64,H) bimodule structure.

ind_H(D_RS) = 8.

Grade: reconstruction. Failure condition (OQ3b-F3/F4): RS constraint count wrong, or
gamma-trace not H-linear.

This path does NOT depend on OQ1 in any way. It uses only the structure of the RS field
in 14D and the H-module structure of S = H^64.

**Path 2 (Tau-corrected Atiyah-Schmid):**

Effective split-rank for L^2(G x_H tau_RS) = 3 - 2 = 1 (tau-correction, unverified).
Hom multiplicity: 4*1 + 4*1 = 8 per FJ Th 4.3 (for effective split-rank 1).
AF2 = 225/48 (A3 root system, exact, survives OQ1).

ind_H(D_RS) = 8.

Grade: reconstruction. Gate: tau-correction formula rank_correction = 2. This path
WAS the primary analytic route before OQ1; it now requires verification of the
tau-correction formula.

**Path 3 (SM generation count):**

RS sector = 1 SM generation x 8 H-lines/generation = 8.
SM branching verified in generation-count-sm-branching-closure-2026-06-22.md.

ind_H(D_RS) = 8.

Grade: reconstruction (depends on SM branching being correct). Failure condition (OQ3b-F6):
RS sector does not contain exactly 1 SM generation.

**Convergence:** All three paths continue to give 8 after OQ1 resolution. No path gives
a different number. The scalar FJ argument (which was the prior "primary" route) is
eliminated, but two robust routes remain that never depended on split-rank.

---

## 8. Why OQ3b Does Not Upgrade to RESOLVED

The task prompt anticipates that OQ1 being "RESOLVED" would close OQ3b. This was
predicated on the expectation that OQ1 would confirm split-rank = 1. Instead, OQ1
confirmed split-rank = 3, which removes the scalar Flensted-Jensen guarantee.

For OQ3b to reach RESOLVED, one of the following must be established:

(a) The tau-correction formula rank_correction(tau_RS) = 2 is verified from a primary
    reference, and the Flensted-Jensen theorem for the twisted space L^2(G x_H tau_RS)
    is confirmed to apply with effective split-rank = 1.

(b) The Oshima-Matsuki condition for the twisted pair is verified, showing the discrete
    spectrum of L^2(G x_H tau_RS) is nonempty.

(c) Path 1 (physical DOF count) is upgraded to verified grade by an independent
    non-compact index theorem (OC1) or a K-theory computation (OQ3b-OQ4).

Currently, none of (a)-(c) are satisfied. The obstruction is real but the claim is not
falsified: three independent reconstruction-grade paths agree on ind_H = 8, and no
counterargument or contradictory computation has been found.

**Verdict: CONDITIONALLY_RESOLVED.**

OQ3b is conditionally resolved at reconstruction grade via three convergent paths. The
primary analytic gate is the tau-correction formula (OQ3b-OQ1). The claim is not an
analytic theorem until one path reaches verified grade.

---

## 9. Explicit Failure Conditions (Complete List)

Carried forward from oq3b-rs-index-8 §8, with OQ1-updated status:

| Code | Condition | OQ1 Impact |
|---|---|---|
| OQ3b-F1 | Tau-correction rank_correction(tau_RS) != 2 | Primary gate; OQ1 makes this the only analytic path |
| OQ3b-F2 | Oshima-Matsuki rules out twisted discrete spectrum | Open; independent of OQ1 |
| OQ3b-F3 | RS physical DOF count wrong (not 2 x C^16 = C^32) | Open; independent of OQ1 |
| OQ3b-F4 | H-linearity of gamma-trace fails | Open; would falsify Cl(9,5)=M(64,H) |
| OQ3b-F5 | Index additivity (OQ3c) fails | Open; separate gate |
| OQ3b-F6 | SM generation count for RS sector wrong | Open; independent of OQ1 |
| ~~OQ3b-SCALAR~~ | Scalar FJ guarantee via split-rank=1 | ELIMINATED by OQ1=3 |

OQ1 resolution adds one new failure confirmation (scalar FJ eliminated) and one new
gate (tau-correction now the primary analytic path). No failure conditions are FIRED
against ind_H = 8; the claim survives at reconstruction grade.

---

## 10. Relationship to Generation Count

The generation count ind_H(D_GU) = 24 = 3 SM generations requires:

```
ind_H(D_GU) = ind_H(D_{1/2}) + ind_H(D_RS) = 16 + 8 = 24.
```

With OQ3b CONDITIONALLY_RESOLVED at reconstruction grade, the generation count remains
CONDITIONALLY_RESOLVED. The remaining gates are:

| Gate | Status | Primary blocker |
|---|---|---|
| ind_H(D_RS) = 8 | CONDITIONALLY_RESOLVED (this file) | Tau-correction rank formula |
| ind_H(D_{1/2}) = 16 | CONDITIONALLY_RESOLVED (OQ3a) | K3 variational selection |
| Index additivity | CONDITIONALLY_RESOLVED (OQ3c) | Fredholm decomposition |
| ind_H(D_GU) = 24 | CONDITIONALLY_RESOLVED | OQ3a + OQ3b + OQ3c |

The primary structural advance from this closure pass: the prior "BC1 scalar chain" is
retired, the physical DOF count (Route A) is confirmed as the most OQ1-independent path,
and the tau-correction mechanism is identified as the correct analytic framework to pursue
if an analytic verification is required.

---

## 11. References

- `explorations/representation-theory-noncompact/oq1-split-rank-verification-2026-06-23.md` — RESOLVED: split-rank = 3
- `explorations/generation-sector/oq3b-rs-index-8-2026-06-23.md` — Parent file, tau-correction mechanism
- `explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md` — BC1 chain (superseded for scalar pair)
- `explorations/representation-theory-noncompact/rc1-discrete-series-verification-pack-2026-06-23.md` — FAILS_AS_STATED note
- `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md` — SM branching
- Flensted-Jensen (1980) Ann. Math. 111:253-311
- Oshima-Matsuki (1984) Adv. Stud. Pure Math. 4:331-390
- Kobayashi (1994) Invent. Math. 117:181-205
