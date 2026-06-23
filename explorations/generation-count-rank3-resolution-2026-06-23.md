---
title: "Generation Count: Rank-3 Resolution via Tau-Twisted RS and K3 Gate"
date: 2026-06-23
problem_label: "generation-count-rank3-resolution"
status: synthesis
verdict: OPEN
verdict_detail: "Generation count 3 vs 4 undetermined — gated on OQ-RK1 (CAS matrix computation of rank_H(S_RS^+) in M(64,H)). Candidate A (rank_H=4, 3 generations) and Candidate B (rank_H=8, 4 generations) are equistatus: neither is eliminated. Discrete-series analytic route fully closed as FAILED; K3 gate RESOLVED; OQ-RK1 required before any candidate is selected as baseline."
owned_by: "Task 2026-06-23"
depends_on:
  - explorations/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md
  - explorations/tau-correction-oshima-matsuki-rs-2026-06-23.md
  - explorations/split-rank-reconciliation-audit-2026-06-23.md
  - explorations/oq3a-t4-vs-k3-disambiguation-2026-06-23.md
  - explorations/ic4-source-free-k3-gate-2026-06-23.md
  - explorations/rc1-discrete-series-verification-pack-2026-06-23.md
---

# Generation Count: Rank-3 Resolution via Tau-Twisted RS and K3 Gate

## One-Sentence Result

The standard discrete-series analytic route to `ind_H(D_GU) = 24` is fully closed as
FAILED on structural grounds (SL(4,R) has no discrete series at all; the tau-twisted rescue
also fails on four independent criteria); however the generation count is **OPEN** at
either 3 or 4 generations via the APS/K3 route, pending OQ-RK1. Candidate A (rank_H(S_RS^+)=4)
gives 3 generations; Candidate B (rank_H(S_RS^+)=8) gives 4 generations. Both are live
and neither is eliminated. The APS/K3 route is independent of all failed discrete-series
machinery but cannot resolve the generation count without the M(64,H) CAS computation.

---

## Verdict Summary

| Route | Verdict | Reason |
|---|---|---|
| Rank-1 BC1 / scalar FJ | **SUPERSEDED / FAILED** | Split-rank is 3 (A3), not 1; equal-rank condition 3=1 fails |
| Rank-3 A3 Harish-Chandra direct | **FAILED** | SL(4,R) has NO discrete series (rank(G)=3, rank(K)=2; rank mismatch) |
| Tau-twisted L^2(G x_H tau_RS) | **FAILS AS STATED** | 4 independent failures (see below) |
| K3 gate / APS | **CONDITIONALLY_RESOLVED** | K3 unique Ricci-flat A-hat=2; APS formula applies; generation count depends on rank_H(S_RS^+); OQ-RK1 required |
| Generation count = 3 (Candidate A) | **OPEN — equistatus with B** | rank_H(S_RS^+)=4 => ind_H=24 => 3 generations; requires OQ-RK1 to confirm |
| Generation count = 4 (Candidate B) | **OPEN — equistatus with A** | rank_H(S_RS^+)=8 => ind_H=32 => 4 generations; requires OQ-RK1 to exclude |

---

## Part A: Rank-3 Route — Direct Harish-Chandra Computation

### Setup

The symmetric pair is:

```
G = SL(4,R),   H = SO_0(3,1),   sigma_B(X) = -J X^T J^{-1},   J = diag(1,1,1,-1)
K = SO(4),     K cap H = SO(3)
```

The corrected split-rank computation (oq1-split-rank-verification, rc1-discrete-series-
verification-pack, split-rank-reconciliation-audit) gives:

```
p_G cap q_B = span{H_1, H_2, H_3, S_12, S_13, S_23}   (dim = 6)
a_q = span{H_1, H_2, H_3}   (maximal abelian in p_G cap q_B)
split-rank(SL(4,R)/SO_0(3,1)) = dim(a_q) = 3
Restricted root system: A3   (rank 3, all multiplicities = 1)
rank(K/(K cap H)) = rank(SO(4)/SO(3)) = rank(S^3) = 1
```

### Harish-Chandra Discrete Series Criterion for G

The Harish-Chandra criterion: a connected semisimple Lie group G has discrete series
representations if and only if rank(G) = rank(K).

**Rank convention (disambiguation):** Throughout this criterion, rank(G) and rank(K) denote
the dimension of a maximal torus of the respective compact forms — equivalently, the rank of
the root system of the complexified Lie algebra. This is the compact-form Cartan rank, NOT
the split rank of the symmetric space G/H used elsewhere in this document.

For G = SL(4,R):

```
rank(G) = rank(sl(4,R)) = 3   (root system A3, compact form SU(4), dim maximal torus = 3)
rank(K) = rank(so(4))   = 2   (root system A1 x A1 (equivalently B2/D2), SO(4) = (SU(2)xSU(2))/Z2,
                                dim maximal torus = 2)
3 != 2
```

Note: rank(SO(4)) = 2 is correct. SO(4) = (SU(2) x SU(2))/Z2 has a maximal torus of
dimension 2 (one U(1) from each SU(2) factor), giving root system A1 x A1. This compact-form
rank is distinct from the split rank dim(a_q) = 3 computed in the symmetric space setup above.

**Conclusion: SL(4,R) has NO discrete series representations whatsoever.**

This is a theorem-grade obstruction. The Atiyah-Schmid formal-degree sum over the discrete
series of SL(4,R) is an EMPTY SUM. The entire analytic chain:

```
Atiyah-Schmid sum -> formal degree d(pi) -> ind_H(S_R^{eff}) = 8
```

fails at the first step because there are no summands.

### What The Rank-3 Route Buys

The A3 restricted root system does supply a complete Plancherel decomposition for the
CONTINUOUS spectrum of L^2(SL(4,R)/SO_0(3,1)):

```
L^2(SL(4,R)/SO_0(3,1)) = integral_{a_q^*/W} pi_lambda d mu(lambda)   (Plancherel)
```

This is absolutely continuous; there is no discrete component. The Plancherel measure is:

```
d mu(lambda) = |c(lambda)|^{-2} d lambda
```

where c(lambda) is the A3 Harish-Chandra c-function. For A3 with all multiplicities = 1,
the c-function has no poles in the positive imaginary spectral region. The earlier BC1
poles at nu_n = (2n+1)/2 belonged to the WRONG involution sigma_A, not sigma_B.

### Implication for the Generation Count Formula

The formula `ind_H(D_GU) = 8*A-hat(X^4) + 8` cannot be derived from the RS analytic
discrete-series route for (SL(4,R), SO_0(3,1)). The 8 in `8 [RS sector]` requires either:

(A) A non-compact analytic proof via a different framework (nonunitary bundle theory,
    b-calculus, hyperfunction boundary values) — all currently OPEN with obstructions.
(B) The physical DOF count: RS modes = (4-1-1) x C^16 = C^32; chiral half = C^16;
    dim_H = 8. Reconstruction grade, no dependence on discrete series.
(C) APS on compact K3: ind_H(D_RS) = A-hat(K3) * rank_H(S_RS^+) + eta/2.
    This is the surviving analytic route (see Part C). The value rank_H(S_RS^+) is
    OPEN (GEN-01): Candidate A gives 2*4+0=8 (3 generations); Candidate B gives
    2*8+0=16 (4 generations). OQ-RK1 required to resolve.

---

## Part B: Tau-Twisted Route — Four Independent Failures

The tau-twisted rescue route proposes:

```
L^2(SL(4,R) x_{SO_0(3,1)} tau_RS),   tau_RS = 4D(1/2,0) + 4D(0,1/2)
```

with a claimed "rank correction" rank_correction(tau_RS) = 2 reducing effective split-rank
from 3 to 1 to restore the Flensted-Jensen equal-rank gate.

All four required conditions fail independently.

### Failure F1: Nonunitary Coefficient

The Lorentz summands D(1/2,0) and D(0,1/2) are nontrivial finite-dimensional
representations of the noncompact group SO_0(3,1). A noncompact semisimple group admits no
nontrivial finite-dimensional unitary representations. Therefore:

```
tau_RS is NOT a unitary representation of H = SO_0(3,1)
L^2(G x_H tau_RS) is NOT a standard Hilbert induced representation
Oshima-Matsuki / FJ Hilbert discrete spectrum: not directly applicable
```

Any Plancherel or Fredholm language for this object requires a nonunitary or indefinite
analytic framework that is NOT the standard Hilbert L^2 theory.

### Failure F2: Scalar Equal-Rank Condition

The Flensted-Jensen criterion for scalar discrete series is:

```
Disc(G/H) nonempty iff rank(G/H) = rank(K/(K cap H))
```

For the actual pair: `rank(G/H) = 3`, `rank(K/(K cap H)) = 1`. Criterion FAILS: 3 != 1.

The claimed rank_correction formula `split-rank_tau = split-rank(G/H) - rank_correction(tau)`
is an UNVERIFIED assertion. No inspected theorem (Flensted-Jensen 1980, Oshima-Matsuki 1984,
Kobayashi 1994, Kobayashi-Oshima arXiv:1202.5743) supports subtracting a finite-dimensional
coefficient representation from the geometric split-rank of the symmetric space.

The split-rank is an invariant of the triple (G, H, sigma), not of a fiber coefficient.
Coefficients can change which infinitesimal characters or boundary values are tested; they
cannot reduce dim(a_q).

### Failure F3: Kobayashi-Oshima Discrete-Decomposability Classification

For a Kobayashi-style proof that L^2(G x_H tau_RS) has a discrete component, one needs
an infinite-dimensional irreducible (g,K)-module X that is discretely decomposable as an
(h, K cap H)-module.

The Kobayashi-Oshima classification (arXiv:1202.5743) lists the symmetric pairs (g,h) for
which such an X exists. For g = sl(4,R) = sl(2n,R) with n=2, the admissible symmetric
subpairs are:

```
sl(n,C) + u(1)    (real dimension 7 for n=2)
sp(n,R)           (real dimension 6 for n=2)
```

The pair so(3,1) inside sl(4,R) has real dimension 6, but so(3,1) ~= sl(2,C)_R is not
sp(2,R) (the latter is the real symplectic algebra, not the complex linear algebra). The
pair (sl(4,R), so(3,1)) does NOT appear in the Kobayashi-Oshima classification.

Therefore: there is NO infinite-dimensional irreducible (sl(4,R),K)-module that is
discretely decomposable as an (so(3,1),K')-module.

### Failure F4: Asymptotic Cone Obstruction

The Kobayashi admissibility test at the compact K-level:

```
X is K'-admissible iff AS_K(X) cap C_K(K') = {0}
K = Spin(4) = SU(2)_L x SU(2)_R
K' = Spin(3) = SU(2)_diag
C_K(K') = R_{>=0} (1,1)   (moment cone of K/K' = S^3)
```

For the RS coefficient, the branching K -> K' analysis shows:

```
(j_L, j_R)|_{diag SU(2)} contains 1/2 iff |j_L - j_R| <= 1/2 <= j_L + j_R
```

The infinite families (n+1/2, n) and (n, n+1/2) all contribute and their normalized
highest weights tend to the diagonal ray R_{>=0}(1,1) = C_K(K'). Therefore:

```
AS_K(Ind_{K'}^K tau_RS) cap C_K(K') contains R_{>=0}(1,1)   (NONZERO)
```

The Kobayashi vanishing condition FAILS. Finite-dimensional twisting does not erase an
asymptotic ray.

### Summary: Tau Route Status

```
F1 Nonunitary coefficient Hilbert space:     FAILS (fires)
F2 Scalar equal-rank condition:              FAILS (fires; 3 != 1)
F3 Kobayashi-Oshima classification:          FAILS (pair excluded)
F4 Asymptotic cone obstruction:              FAILS (fires; nonzero cone intersection)
```

The formula `rank_correction(tau_RS) = 2` is **FALSIFIED** as an analytic gate.
Do not use it. The tau-twisted route to `ind_H(RS) = 8` via discrete Plancherel atoms
is not established.

---

## Part C: K3 Gate — APS Route and Generation Count

The failure of discrete-series routes does NOT close the generation count. The K3 gate and
APS mechanism provide an independent path.

### C1: K3 vs T^4 Disambiguation (RESOLVED)

Both K3 and T^4 are compact Ricci-flat 4-manifolds. Both achieve E[s_LC] = 0 via the
tautological LC section. The Willmore principle alone does not distinguish them.

The A-hat genus is the discriminant:

```
A-hat(K3) = -sigma(K3)/8 = -(-16)/8 = 2   (exact: Hirzebruch, three independent routes)
A-hat(T^4) = -sigma(T^4)/8 = 0             (exact: flat metric, sigma = 0)
```

Applying the 2+1 split formula `ind_H(D_GU) = 8*A-hat(X^4) + 8`:

```
T^4:  8*0 + 8 = 8 = 1 SM generation   (WRONG)
K3:   8*2 + 8 = 24 = 3 SM generations (CORRECT)
```

T^4 is ruled out by the generation count discriminant (C2), not by Willmore (C1). The
failure condition "another Ricci-flat 4-manifold with A-hat = 2" does NOT fire:

Among compact simply-connected smooth Ricci-flat 4-manifolds (Berger holonomy + Yau + 
Donaldson + Freedman):

```
A-hat = 0:  T^4 (and orbifolds T^4/Gamma)
A-hat = 2:  K3 ONLY
```

No other simply-connected compact smooth Ricci-flat 4-manifold exists with A-hat = 2.
Exotic K3 is excluded (no Ricci-flat metric exists by Seiberg-Witten/Taubes 1994).

**K3 is the unique fiber topology satisfying both:**
- Willmore minimizer (Ricci-flat, achieves E[s_LC] = 0)
- Correct generation count (A-hat = 2, ind_H = 24)

OQ3a is **RESOLVED** (oq3a-t4-vs-k3-disambiguation).

### C2: APS Route for ind_H(D_RS) = 8

The non-compact analytic route is demoted (see Part A, Part B). The APS route on compact
K3 provides the surviving analytic strategy.

The APS index formula on compact K3 with boundary S^3:

```
ind_H(D_RS) = A-hat(K3) * rank_H(S_RS^+) + eta(A_RS)/2
```

Input values:

```
rank_H(S_RS^+) = ?    (OPEN — factor-of-2 ambiguity; see GEN-01 analysis below)
eta(A_RS) = 0          (spectral symmetry of round S^3 under orientation-reversing isometry;
                        verified: oq-rk2)
A-hat(K3) = 2          (exact: topological invariant)
```

#### GEN-01: rank_H(S_RS^+) factor-of-2 ambiguity (CRITICAL)

**Issue (flagged 2026-06-23):** The prior entry `rank_H(S_RS^+) = 4` was derived from a
physical DOF count with three halvings whose final step is unjustified:

```
Step 1: RS modes in 4D = (4 vector components - 1 gamma-trace constraint - 1 gauge d.o.f.)
        = 2 transverse d.o.f.   [transverse DOF halving]
Step 2: Tensor with fiber S(6,4) = C^16:  2 x C^16 = C^32 physical RS modes
Step 3: Chiral projection (chirality operator omega; (omega)^2 = +1 in Cl(9,5)):
        chiral half = C^16   [chiral halving]
Step 4: "half of chiral = 4 H-lines"  [UNJUSTIFIED]
```

Step 4 is the error: `C^16` as a right-H-module via the Cl(9,5) = M(64,H) structure has
`dim_H(C^16) = 8`, not 4, because each complex dimension is half a quaternionic dimension
(`dim_H = dim_C / 2`). The step "half of chiral = 4" invokes a second unspecified chirality
split on top of Step 3. This split is not derived; it is asserted.

**Two candidate values and their consequences:**

```
Candidate A: rank_H(S_RS^+) = 4  (a second chirality split Pi_+ further halves C^16)
  => ind_H(D_RS) = 2 * 4 + 0 = 8
  => ind_H(D_GU) = 16 + 8 = 24 => 3 generations

Candidate B: rank_H(S_RS^+) = 8  (no second split; dim_H(C^16) = 8 is correct H-rank)
  => ind_H(D_RS) = 2 * 8 + 0 = 16
  => ind_H(D_GU) = 16 + 16 = 32 => 4 generations
```

Candidate A requires justification that a second chirality projector Pi_+ acts on the
chiral C^16 sub-bundle and that this projector is (a) well-defined, (b) H-linear, and
(c) reduces the H-rank by exactly 2. This must be derived from Cl(9,5) = M(64,H)
representation theory, not from the physical-DOF heuristic.

The correct derivation path (required for OQ-RK1):

1. In Cl(9,5) = M(64,H), the full spinor module is S = H^64 with dim_H = 64.
2. The chirality operator omega (product of all 14 basis gamma matrices) satisfies
   omega^2 = +1 in Cl(9,5) (confirmed independently). The chiral projector gives
   S^+ = H^32 with dim_H(S^+) = 32.
3. The RS sector is defined by the gamma-trace constraint Gamma^mu psi_mu = 0 inside
   Omega^1(Y^14) tensor S. The physical RS sub-bundle S_RS^+ c S^+ must be specified as
   the kernel of a specific H-linear projector Pi_RS acting on S^+ (or on the
   tensor product Omega^1 tensor S^+).
4. rank_H(S_RS^+) = dim_H(ker Pi_RS|_{S^+}) requires the explicit matrix computation
   of Pi_RS in M(64,H). This is OQ-RK1; it has not been performed.

**Current status of rank_H(S_RS^+):** UNRESOLVED pending OQ-RK1 (CAS matrix computation
of Pi_RS in M(64,H)). The value 4 is a heuristic reconstruction-grade guess, not a
derived result. Both candidates A and B remain open.

**Consequence for the APS computation:**

```
If rank_H(S_RS^+) = 4:  ind_H(D_RS) = 2 * 4 + 0 = 8   (3 generations)
If rank_H(S_RS^+) = 8:  ind_H(D_RS) = 2 * 8 + 0 = 16  (4 generations)
```

This note is OPEN: Candidate A (3 generations) and Candidate B (4 generations) are
equistatus. Selecting Candidate A as a baseline overstates the state of knowledge while
Candidate B remains live and undismissed. OQ-RK1 is required to resolve the ambiguity
before any generation count is designated as the baseline.

This route bypasses the non-compact obstruction entirely. It does not use discrete series
of SL(4,R), BC1 root multiplicities, or the tau-correction formula.

### C3: Full Generation Count (OPEN — Candidates A and B equistatus)

From OQ3c (cross-term cancellation, RESOLVED):

```
ind_H(D_GU) = ind_H(D_{spin-1/2}) + ind_H(D_RS)
```

Cross-terms contribute zero by the Clifford identity `c(xi)^2 = g_Y(xi,xi) Id` and the
H-linear Atkinson-Schur LDU theorem.

Substituting (under Candidate A: rank_H(S_RS^+) = 4; see GEN-01 for Candidate B):

```
ind_H(D_{spin-1/2}) = 8 * A-hat(K3) = 8 * 2 = 16   (Atiyah-Singer on K3, exact)
ind_H(D_RS)         = 8                              (APS route, Candidate A; gate: OQ-RK1)
ind_H(D_GU)         = 16 + 8 = 24
generations         = 24 / 8 = 3

Under Candidate B (rank_H(S_RS^+) = 8):
ind_H(D_RS)  = 16
ind_H(D_GU)  = 16 + 16 = 32
generations  = 32 / 8 = 4
```

---

## Dependency Map: What Is Settled, What Is Open

### Settled (at reconstruction grade or better)

- split-rank(SL(4,R)/SO_0(3,1)) = 3 (A3 root system) — **RESOLVED** (explicit matrix computation)
- SL(4,R) has no discrete series (rank(G) != rank(K), compact-form Cartan ranks: 3 != 2) — **THEOREM GRADE** (Harish-Chandra)
- tau-twisted route fails (four independent criteria) — **FALSIFIED**
- rank_correction(tau_RS) = 2 — **FALSIFIED / DO NOT USE**
- A-hat(K3) = 2 — **EXACT** (topological invariant; Hirzebruch + Atiyah-Singer + Chern-Weil)
- A-hat(T^4) = 0 — **EXACT** (three independent routes)
- T^4 gives 1 generation (A-hat = 0 => ind_H = 8) — **EXACT conditional on the split formula**
- K3 unique in A-hat = 2 Ricci-flat class — **THEOREM GRADE** (Berger + Yau + Donaldson + Freedman)
- OQ3a T^4 vs K3 disambiguation — **RESOLVED**
- OQ3c cross-term cancellation — **RESOLVED** (Clifford identity + Atkinson-Schur LDU)
- eta(A_RS on S^3) = 0 — **CONDITIONALLY_RESOLVED** (spectral symmetry argument)

### Open — Candidates Equistatus (blocking for generation count conclusion)

- **GEN-01 / OQ-RK1 (CRITICAL): rank_H(S_RS^+) undetermined** — 3 vs 4 generations cannot
  be settled until OQ-RK1 resolves rank_H(S_RS^+) via M(64,H) CAS computation.
  - Candidate A: rank_H(S_RS^+) = 4 => ind_H(D_RS) = 8 => ind_H(D_GU) = 24 => 3 generations
  - Candidate B: rank_H(S_RS^+) = 8 => ind_H(D_RS) = 16 => ind_H(D_GU) = 32 => 4 generations
  - Both candidates are **equistatus**: neither is derived, neither is eliminated.

### Conditionally Resolved (reconstruction grade, generation-count-independent)

- ind_H(D_{spin-1/2}) = 16 — **CONDITIONALLY_RESOLVED**
  (gates: compact K3 Fredholm completion, parametrix for D_{spin-1/2})
- K3 unique Ricci-flat A-hat=2 fiber — **THEOREM GRADE** (Berger+Yau+Donaldson+Freedman)
- APS index formula applicable on K3 with boundary S^3 — **CONDITIONALLY_RESOLVED**
  (gates: OQ-RK2 APS boundary conditions, FC3/FC4 M(64,H) checks)

### Open (blocking for generation count conclusion)

- **OQ-RK1 (CRITICAL): rank_H(S_RS^+) from M(64,H) CAS computation** — determines whether
  generation count is 3 (Candidate A, rank = 4) or 4 (Candidate B, rank = 8). Requires
  explicit matrix computation of the RS gamma-trace projector Pi_RS in Cl(9,5) = M(64,H).
  The physical DOF heuristic giving rank = 4 contains an unjustified third halving (GEN-01).

### Open (analytic, non-blocking for reconstruction-grade conclusion)

- Non-compact analytic proof of ind_H(D_RS) = 8 (blocked: SL(4,R) has no discrete series;
  nonunitary tau_RS blocks Hilbert L^2 route; Kobayashi-Oshima classification excludes pair)
- b-calculus / scattering parametrix for full non-compact Y^14 (OC2 partial)
- ch_2(S(6,4))[K3] = 0 (flat-bundle approximation explicit check)
- FC3: explicit M(64,H) check that Pi_RS commutes with sigma
- FC4: analytic proof of rank_H(E_RS^{eff}) from first principles beyond physical DOF count

---

## What Changed in This Resolution Pass

Prior state (before 2026-06-23 passes):

```
Generation count = 3: CONDITIONAL on tau-twisted discrete-series
Rank-1 BC1 chain: claimed as primary route (WRONG involution)
K3 gate: Â=2 target confirmed; T^4 disambiguation: open
```

Current state (after this pass):

```
Generation count: OPEN — 3 or 4 generations, gated on OQ-RK1
  Candidate A (rank_H=4): 3 generations — OPEN, equistatus
  Candidate B (rank_H=8): 4 generations — OPEN, equistatus
Rank-1 BC1 chain: SUPERSEDED (wrong involution sigma_A, not sigma_B)
Rank-3 A3 direct: FAILED (SL(4,R) has no discrete series)
Tau-twisted route: FAILS AS STATED (4 independent failures)
K3 gate: RESOLVED (T^4 ruled out; K3 unique; A-hat discriminant exact)
Primary analytic strategy: APS on compact K3, not discrete-series on non-compact G/H
```

The generation count argument has shifted from a non-compact representation-theoretic
derivation to a compact index-theory derivation. The proof architecture is cleaner and
the obstruction structure is fully understood, but the generation count (3 or 4) remains
undetermined pending OQ-RK1.

---

## Primary Remaining Gate

The single most important remaining open item is **OQ-RK1** (which supersedes the prior
framing of OQ3b as the gate):

```
OQ-RK1: Determine rank_H(S_RS^+) from first principles via M(64,H) CAS computation.
         Specifically: compute dim_H(ker Pi_RS|_{S^+}) where Pi_RS is the H-linear
         gamma-trace projector in the explicit M(64,H) matrix representation of Cl(9,5).
         Result determines generation count: rank 4 => 3 generations; rank 8 => 4 generations.
```

OQ-RK1 is BLOCKING: the generation count (3 or 4) cannot be determined without it.
It must precede OQ3b (analytic Fredholm completion) because OQ3b's target index value
depends on rank_H(S_RS^+).

Full upgrade from OPEN to RESOLVED requires:
1. OQ-RK1: CAS matrix computation of Pi_RS in M(64,H); determine rank_H(S_RS^+)
2. OQ-RK2: full APS boundary analysis for the constrained RS operator on K3
3. FC3: explicit CAS check that Pi_RS commutes with sigma in M(64,H) representation
4. FC4: analytic proof of rank_H beyond DOF count, consistent with OQ-RK1 result

Once OQ-RK1 resolves the rank ambiguity and OQ-RK2 and FC3 are verified, the generation
count upgrades from CONDITIONALLY_RESOLVED to RESOLVED (at whatever value rank_H selects).

---

## Failure Conditions For This Note

**FC1: Another compact simply-connected Ricci-flat 4-manifold with A-hat = 2.**
Assessment: DOES NOT FIRE. Berger + Yau + Donaldson + Freedman classify all such
manifolds; K3 is the unique A-hat = 2 representative.

**FC2: APS index formula gives ind_H(D_RS) != 8.**
Assessment: Candidate B (rank_H(S_RS^+)=8) already gives ind_H(D_RS)=16, not 8. FC2
FIRES under Candidate B. eta(A_RS) = 0 is confirmed at reconstruction grade (spectral
symmetry of round S^3). rank_H(S_RS^+) is UNRESOLVED (GEN-01 factor-of-2 ambiguity);
OQ-RK1 determines which candidate is correct. Gate: OQ-RK1 and OQ-RK2.

**FC5: rank_H(S_RS^+) = 8 rather than 4 (GEN-01 — CRITICAL, OPEN).**
Assessment: If no second chirality projector Pi_+ acts on the chiral C^16 sub-bundle,
then dim_H(C^16) = 8 and rank_H(S_RS^+) = 8. This gives ind_H(D_RS) = 16 and
ind_H(D_GU) = 32 = 4 generations. FIRES if OQ-RK1 confirms Candidate B. The 3-generation
conclusion depends on excluding this case. OQ-RK1 (CAS matrix computation of Pi_RS in
M(64,H)) is the required gate.

**FC3: ch_2(S(6,4))[K3] != 0 changes the required A-hat value.**
Assessment: The T^4 vs K3 disambiguation is robust (any positive A-hat value required
selects K3 over T^4). Only an exact cancellation or reduction to A-hat < 2 would threaten
the selection. No mechanism for this is identified.

**FC4: H-linear Atkinson-Schur LDU fails.**
Assessment: Would require Pi_RS not H-linear, impossible given Cl(9,5) ~= M(64,H).
DOES NOT FIRE at algebraic level; analytical completion on non-compact Y^14 is outstanding
(OC2 gates).
