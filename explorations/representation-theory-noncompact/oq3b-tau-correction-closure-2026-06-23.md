---
title: "OQ3b Tau-Correction Closure: Explicit Formal-Degree Sum Computation"
date: 2026-06-23
problem_label: "oq3b-tau-correction-closure"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
depends_on:
  - explorations/generation-sector/oq3b-rs-index-closed-2026-06-23.md
  - explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md
  - explorations/representation-theory-noncompact/rc1-root-mult-disambiguation-2026-06-23.md
  - explorations/generation-sector/rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md
  - explorations/analytic-index-fredholm/oc1-oc2-aps-closure-2026-06-23.md
gates_to_close:
  - "(1) Lambda_RS^{FJ} = 3/2 lies at a discrete-series pole of the Harish-Chandra c-function"
  - "(2) L^2 eigenspace at Lambda = 3/2 is non-empty with multiplicity 8 in H-lines"
  - "(3) Atiyah-Schmid formal-degree sum = 8"
---

# OQ3b Tau-Correction Closure: Explicit Formal-Degree Sum Computation

## 1. Task and Prior State

The task is to close OQ3b by executing the tau-correction program explicitly:

> Show (1) Lambda_RS^{FJ} = 3/2 sits at a discrete-series pole of the Harish-Chandra c-function;
> (2) the L^2 eigenspace at Lambda = 3/2 is non-empty with multiplicity 8 (H-lines);
> (3) the Atiyah-Schmid formal-degree sum_{pi in disc} d(pi) * m_{S(6,4)}(pi) = 8.

The prior state (oq3b-rs-index-closed-2026-06-23.md, §4):

- OQ1 confirmed split-rank(SL(4,R)/SO_0(3,1)) = 3 under the correct involution sigma_B.
- Scalar Flensted-Jensen / BC1 route ELIMINATED.
- Tau-correction analytic path conditionally survives: if rank_correction(tau_RS) = 2, then
  effective split-rank for L^2(G x_H tau_RS) = 3 - 2 = 1, allowing the FJ theorem to apply
  to the twisted space.
- rc1-rs-kk-zero-mode.md §3.5 executed a tau-shift argument: Lambda_RS + rho_tau(D(1/2,0)) =
  1 + 1/2 = 3/2 = nu_1 (claimed to be the second BC1 discrete pole).

The root-multiplicity disambiguation file (rc1-root-mult-disambiguation-2026-06-23.md) and
the rank-3 rebuild file (rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md) provide
essential corrections that constrain what can be established here.

---

## 2. The Underlying Root System: A3 Not BC1

### 2.1 Correct restricted root system

Under the correct metric-conjugation involution sigma_B (dsigma_B(X) = -J X^T J^{-1},
J = diag(1,1,1,-1)) for the symmetric pair (SL(4,R), SO_0(3,1)):

```
Restricted root system: A3   (rank 3, all multiplicities = 1)
Maximal abelian subspace: a_q = span{H_1, H_2, H_3}   (3-dimensional)
Restricted roots: {e_i - e_j : 1 <= i != j <= 4, restricted to a_q}
                  (all nonzero, giving an A3 system)
```

This is RESOLVED at reconstruction grade (rc1-root-mult-disambiguation-2026-06-23.md).

### 2.2 What this means for the c-function

The Harish-Chandra c-function for a rank-r symmetric space G/H factors over the root system
via the Gindikin-Karpelevich formula:

```
c(lambda)^{-1} = c_0 * prod_{alpha in Sigma^+} 
    [Gamma(i<lambda,alpha>/|alpha|^2 + m_alpha/4 + m_{2alpha}/2)
     / Gamma(i<lambda,alpha>/|alpha|^2 + m_alpha/4)]
```

For the A3 restricted root system with all multiplicities m_alpha = 1, m_{2alpha} = 0
(no double roots in A3):

```
Sigma^+ for A3: {e_1-e_2, e_2-e_3, e_3-e_4, e_1-e_3, e_2-e_4, e_1-e_4}   (6 positive roots)
```

Each factor becomes (m_alpha = 1, m_{2alpha} = 0):

```
Factor for alpha: Gamma(i<lambda,alpha>/|alpha|^2 + 1/4) / Gamma(i<lambda,alpha>/|alpha|^2)
```

The poles of c(lambda)^{-1} (which give the discrete Plancherel atoms) require
Gamma(i<lambda,alpha>/|alpha|^2 + 1/4) to have a pole, i.e.,

```
i<lambda,alpha>/|alpha|^2 + 1/4 = 0, -1, -2, ...
=> i<lambda,alpha>/|alpha|^2 = -1/4, -5/4, -9/4, ...
```

But for spectral parameters in the discrete range (imaginary lambda = i*nu, nu real and
positive), this becomes:

```
<nu,alpha>/|alpha|^2 = -1/4 + n,   n = 0, -1, -2, ...
```

For nu in the dominant positive chamber of a_q^*, we have <nu, alpha> > 0 for all
positive alpha. This means <nu,alpha>/|alpha|^2 > 0, which does NOT satisfy the pole
condition -1/4, -5/4, ... (all negative or zero). The c-function has no poles in
the positive imaginary-nu region for the A3 root system with m_alpha = 1.

**Key conclusion:** For the correct A3 restricted root system of (SL(4,R), SO_0(3,1))
with sigma_B involution, the Harish-Chandra c-function c(lambda)^{-1} for scalar
L^2(G/H) has NO discrete poles in the positive imaginary spectral region. The scalar
Plancherel is absolutely continuous. This confirms the statement in rc1-root-mult-disambiguation:

> "Scalar Plancherel is absolutely continuous (FJ equal-rank 3 = 1 fails, no scalar
> discrete series)."

---

## 3. Gate (1): Does Lambda_RS^{FJ} = 3/2 Lie at a Discrete-Series Pole?

### 3.1 The tau-shift argument and its dependence on BC1

The rc1-rs-kk-zero-mode computation in §3.5 proceeds as follows:

```
Lambda_RS^{FJ} = Lambda_RS + rho_tau(D(1/2,0)) = 1 + 1/2 = 3/2
```

and claims this equals nu_1 = 3/2, the second pole of the BC1 Plancherel measure with
(m_1, m_2) = (7, 1) and rho = 9/2 (from rc3-harish-chandra).

The problem is structural: the BC1 pole ladder nu_n = (2n+1)/2 at n = 0, 1, 2, 3 arises
from the c-function for the (SL(4,R), SO_0(3,1)) pair UNDER THE WRONG INVOLUTION sigma_A.
The rc3-harish-chandra c-function with (m_1, m_2) = (7, 1) is a BC1 c-function, which
requires a rank-1 restricted root system with a double root 2*alpha. Under sigma_B the
correct restricted root system is A3 (rank 3, no double roots), and the rc3 c-function
does not apply to scalar L^2(SL(4,R)/SO_0(3,1)).

**Therefore:**

Gate (1) FAILS as a LITERAL STATEMENT.

Lambda_RS^{FJ} = 3/2 does NOT lie at a discrete-series pole of the Harish-Chandra c-function
for the CORRECT root system A3. The c-function for A3 with m_alpha = 1 has no discrete
poles in the physical spectral region. The BC1 pole at nu_1 = 3/2 is an artifact of the
wrong symmetric-pair involution.

### 3.2 Revised formulation: tau-twisted c-function

The surviving version of the tau-correction argument (oq3b-rs-index-closed §4) is:

> For the TWISTED space L^2(G x_H tau_RS), the Flensted-Jensen theorem may apply with
> an EFFECTIVE split-rank = 3 - rank_correction(tau_RS) = 3 - 2 = 1.

If this effective reduction holds, the relevant c-function is NOT the A3 scalar c-function
but the c-function for the tau-twisted problem, which may have a different pole structure.

The tau-twisted c-function for L^2(G x_H tau_RS) with tau_RS = D(1/2,0) of SO_0(3,1) is
NOT the same as the scalar A3 c-function. It is the matrix-coefficient function:

```
c_tau(lambda) = integral_{N-bar} phi_lambda^tau(n-bar) dn-bar
```

where phi_lambda^tau is the tau-spherical function (generalized zonal spherical function
for the twisted space). For nonunitary tau, this object is analytically more subtle.

**Critical obstruction from rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md, §R1:**

```
tau_RS = D(1/2,0) of SO_0(3,1) is NONUNITARY as an H-representation
(SO_0(3,1) is noncompact; D(1/2,0) is a finite-dimensional nonunitary representation).
```

The Kobayashi-Matsuki-Oshima framework for discrete decomposability of L^2(G x_H tau)
requires the inducing representation tau to be K_H-finite and satisfy a unitarizability
or admissibility condition. For nonunitary tau, the discrete spectrum may be empty
(no square-integrable tau-spherical functions), which is the R1 obstruction.

**Gate (1) status:** CANNOT BE ESTABLISHED in the tau-twisted A3 setting by the methods
available. The BC1 pole at nu_1 = 3/2 is from the wrong root system. The correct tau-twisted
A3 c-function for nonunitary tau_RS is not established to have a pole at any specific value.

---

## 4. Gate (2): L^2 Eigenspace at Lambda = 3/2, Multiplicity 8

### 4.1 Scalar A3 case

For the scalar case (untwisted L^2(G/H) with A3 root system), there is no discrete
spectrum. The eigenspace at any spectral parameter lambda is zero-dimensional in the
discrete sense. Gate (2) FAILS for the scalar case.

### 4.2 Tau-twisted case

For the tau-twisted space L^2(G x_H tau_RS), the existence of a discrete eigenspace
requires either:

(a) The Oshima-Matsuki (1984) condition: the asymptotic cone of tau_RS is compatible
    with the theta-stable parabolic for G/H.

(b) The Kobayashi (1994) discrete decomposability criterion: the restriction of
    some A_q(lambda) (Zuckerman derived functor module) to H is discretely decomposable.

From rs-analytic-rank3-rebuild-or-demotion §R2 and §R3:

> R2 (Oshima-Matsuki A3 classification) fails: the asymptotic cone obstruction is
> nonzero for (SL(4,R), SO_0(3,1)) with A3 root system.

> R3 (b-calculus) fails: the nonunitary alpha_3 character prevents L^2 discrete spectrum.

**Gate (2) status:** CANNOT BE ESTABLISHED by currently available arguments. The nonzero
asymptotic cone obstruction and the nonunitary character of tau_RS block the known routes
to discrete spectrum existence for the twisted space.

### 4.3 The multiplicity-8 argument

Even if a discrete eigenspace existed at Lambda = 3/2 (which is not established), the
multiplicity-8 claim requires:

```
sum_k dim Hom_{SO_0(3,1)}(D(1/2,0), pi_{3/2}|_{SO_0(3,1)}) = 8
```

summed over the 8 H-types 4*D(1/2,0) + 4*D(0,1/2). The Flensted-Jensen multiplicity-one
theorem (FJ Theorem 4.3) would give this if the effective split-rank is 1. But this theorem
applies only when the tau-twisted Flensted-Jensen setup is valid, which requires the tau
to be well-adapted (specifically, to satisfy the FJ rank-condition for the twisted pair).
The rank_correction(tau_RS) = 2 formula attributed to Kobayashi-Oda (2023) has not been
verified for this specific pair and tau.

**Multiplicity-8 conclusion:** The conclusion ind_H = 8 via this route is
reconstruction-grade at best, and the specific gate (Gate 2) cannot be established
from known results.

---

## 5. Gate (3): Atiyah-Schmid Formal-Degree Sum

### 5.1 The sum to compute

The task requires computing:

```
sum_{pi in disc} d(pi) * m_{S(6,4)}(pi) = 8
```

where the sum is over discrete series representations pi of SL(4,R), d(pi) is the
Atiyah-Schmid formal degree, and m_{S(6,4)}(pi) is the multiplicity of S(6,4)|_{SO_0(3,1)}
in pi|_{SO_0(3,1)}.

### 5.2 The discrete series of SL(4,R)

SL(4,R) is a split real form of SL(4,C). For split real semisimple Lie groups, the
discrete series (in the Harish-Chandra sense of square-integrable representations) are
EMPTY unless the split-rank equals the rank of the maximal compact subgroup K.

For SL(4,R): K = SO(4), rank(K) = 2; split-rank of SL(4,R) (rank of A in the Iwasawa
decomposition) = 3. Since split-rank(SL(4,R)) = 3 > rank(SO(4)) = 2, the group SL(4,R)
has NO DISCRETE SERIES REPRESENTATIONS in the L^2(SL(4,R)) sense.

This is a standard fact: Harish-Chandra's theorem (1966) states that G has discrete series
iff rank(G) = rank(K). For SL(4,R), rank(SL(4,R)) = 3 (rank of SL(4)) and rank(SO(4)) = 2.
Since 3 != 2, SL(4,R) has no discrete series.

**The formal-degree sum is an empty sum:**

```
sum_{pi in disc(SL(4,R))} d(pi) * m_{S(6,4)}(pi) = 0   (empty sum)
```

This does not equal 8. Gate (3) FAILS for the discrete series of SL(4,R).

### 5.3 What the AF2 formal degree 225/48 represents

The value d(pi_{lambda_RS}) = 225/48 computed in oq3b-rs-index-8 §5.2 and referenced
in oq3b-rs-index-closed §5 is the G-PLANCHEREL DENSITY of a principal series or
"complementary series" representation of SL(4,R) at the spectral parameter lambda_RS.
It is NOT the formal degree of a discrete series representation (since none exist for
SL(4,R)). The computation uses the A3 Plancherel polynomial P(lambda+rho_G)/P(rho_G),
which gives the density of the continuous Plancherel measure at lambda_RS, not an atom.

The Atiyah-Schmid formula for the L^2-index

```
ind_H(D_GU) = sum_{pi in disc} d(pi) * Hom_H(pi, S^+)
```

applies ONLY to groups G that have discrete series. For SL(4,R) (no discrete series),
this formula does not directly yield an integer from a discrete-series sum. The generation
count must be grounded differently.

### 5.4 The formal-degree computation for the FIBER L^2 space

The relevant discrete-series question for OQ3b is not the discrete series of SL(4,R) in
L^2(SL(4,R)) but the relative discrete series for L^2(SL(4,R)/SO_0(3,1); S(6,4)):
representations pi that appear discretely in the Plancherel decomposition of the QUOTIENT
space L^2(G/H) with coefficient bundle S(6,4).

For this relative discrete series (when it exists), the formal degree atoms carry the
index information. As established in Gates (1) and (2), the existence of these atoms
under the correct A3 root system and with the nonunitary coefficient bundle tau_RS is
not established. Therefore Gate (3) as stated (sum = 8 via Atiyah-Schmid over disc) is
not achievable from the current framework.

**Gate (3) status:** FAILS as a sum over L^2(SL(4,R)) discrete series (that sum is zero).
CANNOT BE ESTABLISHED for the relative discrete series of L^2(G/H; S(6,4)) without
resolving Gates (1) and (2).

---

## 6. What Does Survive: The Three Convergent Paths

Despite the failure of the tau-correction gate to close analytically, the overall claim
ind_H(D_RS) = 8 retains three reconstruction-grade supports (from oq3b-rs-index-closed §7):

**Path 1 (Physical DOF count):**
RS physical degrees of freedom: (4 vector - 1 gamma-trace - 1 gauge) x C^16 = C^32.
Chiral half: C^16. H-dimension: dim_H(C^16) = 8.
No dependence on split-rank or root system.
Grade: reconstruction.

**Path 2 (SM generation count):**
RS sector = 1 SM generation x 8 H-lines/generation = 8.
Derived from S(6,4)|_{SO_0(3,1)} branching (reconstruction grade).
No dependence on split-rank.
Grade: reconstruction.

**Path 3 (APS on compact K3):**
APS index formula on s*(D_RS) restricted to K3-type X^4:
ind_H(D_RS) = hat{A}(K3) * rank_H(S_RS^+) + eta/2 = 2*4 + 0 = 8.
rank_H(S_RS^+) = 4 from physical DOF count; eta = 0 by spectral symmetry on S^3 boundary.
Grade: reconstruction.
(From rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md, Route R4; and oc1-oc2-aps-closure-2026-06-23.md.)

All three paths give 8. No path gives a different number. The tau-correction route (the
FOURTH candidate route) fails on structural grounds at Gates (1), (2), and (3), and is
therefore retired as a live proof strategy.

---

## 7. Why OQ3b Remains CONDITIONALLY_RESOLVED (Not GENUINE_OBSTRUCTION)

The failure of the tau-correction gate does NOT falsify ind_H(D_RS) = 8. It eliminates
one analytic proof strategy while three reconstruction-grade paths remain. The verdict
is CONDITIONALLY_RESOLVED because:

1. Three independent paths (physical DOF, SM generation, APS) all yield 8.
2. No counterargument or computation yields a different value.
3. The analytic obstruction (no discrete series for SL(4,R); asymptotic cone obstruction
   for the twisted space) blocks the proof route but does not assert ind_H = 0 or any
   other contradictory value.

For OQ3b to reach GENUINE_OBSTRUCTION, one of the following would be needed:
- A computation showing ind_H(D_RS) != 8.
- A proof that the physical DOF count is wrong (e.g., more or fewer than 2 physical RS modes).
- A proof that the APS boundary conditions for the constrained RS operator are incompatible.

None of these fire.

---

## 8. Explicit Failure Conditions for the Tau-Correction Route

| Gate | Reason for failure |
|---|---|
| Gate 1: Lambda_RS^{FJ} = 3/2 at a pole | BC1 pole at 3/2 is from wrong involution sigma_A; correct A3 c-function has no discrete poles |
| Gate 1 (twisted): tau-twisted c-function has a pole at 3/2 | Nonunitary tau_RS blocks standard tau-spherical function theory; pole structure unknown |
| Gate 2: L^2 eigenspace exists at 3/2 | Oshima-Matsuki asymptotic cone obstruction nonzero for A3; nonunitary alpha_3 character |
| Gate 3: Atiyah-Schmid sum = 8 | SL(4,R) has no discrete series (rank(G)=3, rank(K)=2); sum is empty = 0 |
| Gate 3 (relative): relative disc series of L^2(G/H) sums to 8 | Conditional on Gates 1 and 2 which both fail |

---

## 9. Updated Failure Conditions for OQ3b

Incorporating the tau-correction route retirement:

| Code | Condition | Status |
|---|---|---|
| OQ3b-F0 | Tau-correction route: discrete-series pole at Lambda_RS^{FJ} = 3/2 | RETIRED (structural failure, not a probabilistic gap) |
| OQ3b-F1 | Tau-correction route: rank_correction(tau_RS) != 2 | RETIRED (route demoted before this can be tested) |
| OQ3b-F2 | APS: RS physical DOF count wrong (not rank_H(S_RS^+) = 4) | OPEN (upgrade target OQ-RK1) |
| OQ3b-F3 | APS: APS boundary conditions for constrained RS operator incompatible | OPEN (upgrade target OQ-RK2) |
| OQ3b-F4 | Physical DOF count: gamma-trace or gauge reduction wrong | OPEN |
| OQ3b-F5 | SM generation count: RS sector != 1 generation | OPEN |
| OQ3b-F6 | Index additivity (OQ3c) fails | CONDITIONALLY_RESOLVED |

---

## 10. N5 Closure Status

The task states: "If the sum equals 8, OQ3b is RESOLVED and N5 closes."

The sum (Gate 3) does NOT equal 8 via the proposed Atiyah-Schmid / Flensted-Jensen route.
N5 does NOT close via this tau-correction mechanism.

N5 remains CONDITIONALLY_RESOLVED at reconstruction grade, with:
- ind_H(D_{1/2}) = 16: CONDITIONALLY_RESOLVED (OQ3a, K3 via hat{A} = 2)
- ind_H(D_RS) = 8: CONDITIONALLY_RESOLVED (three reconstruction-grade paths; tau-correction
  route retired; APS route is primary surviving analytic strategy)
- Additivity: CONDITIONALLY_RESOLVED (OQ3c)
- Total: ind_H(D_GU) = 24: CONDITIONALLY_RESOLVED

The upgrade path to RESOLVED requires OQ-RK1 (first-principles RS rank derivation
without physical DOF count) and OQ-RK2 (APS boundary conditions for RS operator on K3).

---

## 11. References

- `explorations/generation-sector/oq3b-rs-index-closed-2026-06-23.md` — OQ3b post-OQ1 status; three paths; tau-correction gate
- `explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md` — Tau-shift argument Lambda_RS^{FJ} = 3/2 (superseded)
- `explorations/representation-theory-noncompact/rc1-root-mult-disambiguation-2026-06-23.md` — RESOLVED: A3 root system, not BC1
- `explorations/generation-sector/rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md` — R1/R2/R3 demoted; APS (R4) survives
- `explorations/analytic-index-fredholm/oc1-oc2-aps-closure-2026-06-23.md` — APS route for ind_H = 24
- Harish-Chandra (1966) — Discrete series for semisimple Lie groups II. Acta Math. 116:1-111
- Flensted-Jensen (1980) — Discrete Series for Semisimple Symmetric Spaces. Ann. Math. 111:253-311
- Oshima-Matsuki (1984) — A description of discrete series for semisimple symmetric spaces.
  Adv. Stud. Pure Math. 4:331-390
- Kobayashi (1994) — Discrete decomposability of the restriction of A_q(lambda) with respect
  to reductive subgroups and its applications. Invent. Math. 117:181-205
