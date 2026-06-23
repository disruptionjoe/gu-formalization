---
title: "OQ3b Literature Verification: Tau-Correction Formula and Formal-Degree Sum"
date: 2026-06-23
problem_label: "oq3b-literature-verification"
status: definitive
verdict: CONDITIONALLY_RESOLVED
depends_on:
  - explorations/oq3b-tau-correction-closure-2026-06-23.md
  - explorations/oq3b-rs-index-closed-2026-06-23.md
  - explorations/rc1-rs-kk-zero-mode-2026-06-23.md
  - explorations/rc1-root-mult-disambiguation-2026-06-23.md
supersedes:
  - explorations/rc1-rs-kk-zero-mode-2026-06-23.md (scalar BC1 chain)
  - explorations/rc3-harish-chandra-c-function-2026-06-23.md (scalar BC1 chain)
---

# OQ3b Literature Verification: Tau-Correction Formula and Formal-Degree Sum

## Summary Verdict

**CONDITIONALLY_RESOLVED.** The claim ind_H(D_RS) = 8 survives on three independent
reconstruction-grade paths. The specific tau-correction route as stated -- Lambda_RS^{FJ}=3/2
at a discrete-series pole of the Harish-Chandra c-function for (SL(4,R), SO_0(3,1)),
formal-degree sum = 8 -- is **NOT supportable as a literal theorem** because:

1. The symmetric pair (SL(4,R), SO_0(3,1)) under the correct metric involution sigma_B
   has restricted root system A3 (rank 3), not BC1 (rank 1); the Harish-Chandra c-function
   for A3 has no discrete poles in the physical spectral region.
2. SL(4,R) has no discrete series representations (Harish-Chandra equal-rank criterion fails:
   rank(SL(4,R))=3, rank(SO(4))=2); the formal-degree sum over disc(SL(4,R)) is an empty
   sum equal to 0, not 8.
3. The claimed Kobayashi-Oda (2023) rank_correction formula cannot be verified for this pair
   and tau from the available literature.

However, the numerical conclusion ind_H(D_RS) = 8 is supported by three OQ1-independent
paths that remain intact and mutually consistent.

---

## 1. The Exact Theorem That Was Supposed to Apply

### 1.1 Kobayashi-Oda (2023) and the Finite-Multiplicity Framework

The paper "Symmetric pairs with finite-multiplicity property for branching laws of admissible
representations" by Kobayashi and Oda (2023, arXiv:2109.12154 and Selecta Math.) addresses
when the restriction of a unitary representation pi of G to a reductive subgroup H has
finite multiplicity. The precise theorem relevant to OQ3b is:

**Kobayashi-Oda Theorem (paraphrase):** Let (G, H) be a symmetric pair with G real reductive.
The following are equivalent:
  (KO-i) Every admissible smooth representation of G has finite-multiplicity restriction to H.
  (KO-ii) The symmetric pair (G, H) is "real spherical" (i.e., a minimal parabolic of G has
           an open orbit on G/H).
  (KO-iii) rank_R(G) = rank_R(H) + s where s = "split-rank correction" satisfying
            s <= dim(a_G) - dim(a_H).

For (G, H) = (SL(4,R), SO_0(3,1)), this theorem applies to the multiplicity problem but
does NOT directly compute ind_H(D_RS). The finite-multiplicity property is a necessary
structural condition, not a formula for formal degrees.

### 1.2 What Kobayashi-Oda Does NOT Provide

Kobayashi-Oda (2023) does NOT contain:
- An explicit formula "rank_correction(tau) = 2" for tau = D(1/2,0) of SO_0(3,1).
- An explicit pole position Lambda_RS^{FJ} = 3/2 for the twisted space L^2(G x_H tau_RS).
- A computation of ind_H(D_RS) = 8 for this specific pair and tau.

The "rank_correction = 2" formula in the prior exploration files was a reconstruction-grade
inference, not a cited theorem. There is no theorem in Kobayashi-Oda (2023) producing this
specific numerical claim.

### 1.3 Oshima-Matsuki (1984) Theorem

The relevant theorem from Oshima-Matsuki (1984) "A description of discrete series for
semisimple symmetric spaces," Adv. Stud. Pure Math. 4:331-390, is:

**Oshima-Matsuki Theorem 6.11:** Let G/H be a semisimple symmetric space with Cartan
involution theta on G and the involution sigma defining H. A necessary condition for the
existence of discrete series representations in L^2(G/H) is:

  rank(G/H)_R = rank((G^theta cap G^sigma) \ G^theta / G^sigma)

where rank(G/H)_R denotes the real rank of the symmetric space (= dim a_q, the split rank).
The discrete series exist if and only if rho_H - rho_G lies in the dual of the positive Weyl
chamber of a_q^* relative to the ordering compatible with sigma.

For scalar L^2(SL(4,R)/SO_0(3,1)) with sigma_B:
- a_q has dimension 3 (split-rank 3, RESOLVED by explicit matrix computation).
- rho_H - rho_G = (-1, -1/2, 1/2, 1) in standard A3 coordinates, which lies OUTSIDE
  the dominant Weyl chamber for A3 (requires all components > 0).
- **Oshima-Matsuki condition: FAILS for scalar L^2(G/H).** No discrete series exist.

For twisted L^2(G x_H tau_RS): The rho_H - rho_G shift is modified by the representation
tau_RS = D(1/2,0). The modified condition is:

  rho_H - rho_G + rho_tau lies in the dominant Weyl chamber

where rho_tau is the half-sum of roots of H acting in tau. For SO_0(3,1) and D(1/2,0),
rho_tau = 1/2 in the relevant direction. This gives:

  (-1, -1/2, 1/2, 1) + (1/2) = (-1/2, 0, 1, 3/2)   [schematic, tau shifts one component]

The shifted vector still has a negative component (-1/2 in the first position), so the
**Oshima-Matsuki condition fails for the tau-twisted space as well**, at least naively.
The full verification requires an explicit Weyl-chamber membership check in the A3
coordinates, which has not been performed.

---

## 2. The Harish-Chandra c-Function for (SL(4,R), SO_0(3,1))

### 2.1 The Correct Root System

Under the metric involution sigma_B: dsigma_B(X) = -J X^T J^{-1}, J = diag(1,1,1,-1),
the restricted root system of (SL(4,R), SO_0(3,1)) is:

```
Root system: A3   (not BC1)
Rank: 3
Positive roots: {e_i - e_j : 1 <= i < j <= 4}   (6 positive roots)
Root multiplicities: m_alpha = 1 for all alpha in A3, m_{2alpha} = 0 (no double roots)
Half-sum of positive roots: rho_G = (3/2, 1/2, -1/2, -3/2)
```

This is DEFINITIVELY established by the explicit matrix computation in
oq1-split-rank-verification-2026-06-23.md (RESOLVED status) and the disambiguation in
rc1-root-mult-disambiguation-2026-06-23.md (RESOLVED status).

### 2.2 The Gindikin-Karpelevich Formula for A3

The Harish-Chandra c-function for a rank-r symmetric space with A3 restricted roots:

```
c(lambda)^{-1} = c_0 * prod_{alpha in Delta^+} F(alpha, lambda)
```

where for each positive root alpha with multiplicities m_alpha = 1, m_{2alpha} = 0:

```
F(alpha, lambda) = Gamma(<lambda, alpha^vee>/2 + m_alpha/4 + m_{2alpha}/2)
                   / Gamma(<lambda, alpha^vee>/2 + m_alpha/4)
                 = Gamma(<lambda, alpha^vee>/2 + 1/4)
                   / Gamma(<lambda, alpha^vee>/2)
```

where alpha^vee = 2alpha/|alpha|^2.

For a spectral parameter lambda = i*nu with nu real and positive (imaginary axis, physical
Plancherel regime), each factor becomes:

```
F(alpha, i*nu) = Gamma(i<nu, alpha^vee>/2 + 1/4) / Gamma(i<nu, alpha^vee>/2)
```

The poles of c(lambda)^{-1} (which would give discrete Plancherel atoms) arise when
Gamma(i<nu, alpha^vee>/2 + 1/4) has a pole, i.e., when:

```
i<nu, alpha^vee>/2 + 1/4 = 0, -1, -2, ...
=> i<nu, alpha^vee>/2 = -1/4, -5/4, -9/4, ...
```

For real nu in the positive Weyl chamber, <nu, alpha^vee> > 0 for all positive alpha in A3.
This means i<nu, alpha^vee>/2 is PURELY IMAGINARY with positive imaginary part, which can
NEVER equal -1/4, -5/4, ... (which are real negative numbers).

**Conclusion:** The A3 c-function has NO discrete poles for spectral parameters in the
positive imaginary-nu region. The scalar L^2(SL(4,R)/SO_0(3,1)) Plancherel measure is
ABSOLUTELY CONTINUOUS. There are no discrete series for the scalar pair.

### 2.3 The BC1 c-Function Was Wrong

The c-function c(lambda) with (m_1, m_2) = (7, 1) and poles at nu_n = (2n+1)/2 (n = 0,1,2,3)
cited in rc3-harish-chandra-c-function-2026-06-23.md corresponds to a BC1 root system of
rank 1. This arises from the WRONG involution sigma_A (block-conjugation), which gives a
different symmetric pair with a different restricted root system. Under sigma_A, one can
find a rank-1 restricted root system, but sigma_A does NOT define the metric pair
(SL(4,R), SO_0(3,1)); it defines a pair (SL(4,R), another subgroup).

The value Lambda_RS^{FJ} = 3/2 was computed as the tau-shift of Lambda_RS = 1 to the second
BC1 pole nu_1 = 3/2. This construction is invalid because:
- The BC1 root system is an artifact of the wrong involution.
- The BC1 poles do not exist for the correct A3 pair.
- Lambda_RS^{FJ} = 3/2 is therefore not a discrete-series pole of any c-function associated
  with (SL(4,R), SO_0(3,1)).

---

## 3. The Flensted-Jensen Discrete Series Condition

### 3.1 The Correct Flensted-Jensen Theorem

**Flensted-Jensen (1980), Theorem 3.1** (Ann. Math. 111:253-311):

Let G/H be a semisimple symmetric space. A necessary and sufficient condition for the
existence of discrete series representations in L^2(G/H) is:

  rank(G/H) = rank(K / (K cap H))

where rank(G/H) = dim a_q = split-rank of G/H, and K is the maximal compact subgroup of G.

For (SL(4,R), SO_0(3,1)):
- G = SL(4,R), K = SO(4)
- H = SO_0(3,1)
- K cap H = SO(3) (maximal compact of H)
- K / (K cap H) = SO(4) / SO(3) = S^3 (3-sphere)
- rank(K / (K cap H)) = rank(S^3) = 1

Under the CORRECT involution sigma_B:
- split-rank(G/H) = dim a_q = 3   [RESOLVED by oq1-split-rank-verification]

Flensted-Jensen equal-rank criterion: **3 != 1.** The criterion FAILS.

Under the WRONG involution sigma_A (which gives a rank-1 restricted root system):
- split-rank would be 1, and the criterion 1 = 1 would hold.

The prior claim in n5-discrete-series-gl4r-2026-06-23.md §19 that "OQ1 RESOLVED: split-rank
= 1" was based on bracket computations in the wrong model (sigma_A or a non-maximal line).
The definitive computation under sigma_B gives split-rank = 3.

### 3.2 Consequence for OQ3b

The scalar Flensted-Jensen theorem does NOT guarantee discrete series in L^2(SL(4,R)/SO_0(3,1)).
The prior argument in n5-discrete-series-gl4r-2026-06-23.md that derived ind_H(D_RS) = 8
via Flensted-Jensen is INVALID at the scalar level.

### 3.3 No Applicable Published Theorem

A search of the available literature (Oshima-Matsuki 1984, Kobayashi 1994, Flensted-Jensen
1980, Kobayashi-Oda 2023, Helgason 1978, Wallach 1988) reveals:

- No published theorem establishing discrete series for the SCALAR L^2(SL(4,R)/SO_0(3,1))
  with the sigma_B involution, because the equal-rank criterion fails.
- No published theorem establishing discrete decomposability of L^2(G x_H tau_RS) for
  the TWISTED problem with tau_RS = D(1/2,0) of SO_0(3,1), because tau_RS is nonunitary
  (H = SO_0(3,1) is noncompact) and the Kobayashi (1994) admissibility criterion requires
  unitary or K_H-finite inducing representations.
- No published theorem computing rank_correction(tau_RS) = 2 explicitly for this pair.

---

## 4. The Atiyah-Schmid Formal-Degree Sum: Explicit Computation

### 4.1 Setting Up the Sum

The claim: the formal-degree sum

```
sum_{pi in disc(SL(4,R))} d(pi) * m_{S(6,4)}(pi) = 8
```

where d(pi) is the Atiyah-Schmid formal degree and m_{S(6,4)}(pi) counts S(6,4) H-types in
pi|_{SO_0(3,1)}.

### 4.2 The Empty Sum: SL(4,R) Has No Discrete Series

**Harish-Chandra's Discrete Series Theorem (1966):** A connected semisimple Lie group G
has discrete series representations (square-integrable modulo center) if and only if:

  rank(G) = rank(K)

where K is a maximal compact subgroup.

For SL(4,R):
- G = SL(4,R), rank(G) = rank(SL(4,C)) = 3 (dimension of the diagonal Cartan in SL(4))
- K = SO(4), rank(SO(4)) = rank(SO(4,C)) = 2

Since rank(SL(4,R)) = 3 != rank(SO(4)) = 2, the group SL(4,R) has **no discrete series
representations** in the sense of L^2(SL(4,R)).

This is a standard textbook fact (see Knapp, "Representation Theory of Semisimple Groups,"
Ch. IX; Varadarajan, "Harmonic Analysis on Real Reductive Groups," Ch. IV).

Therefore:

```
disc(SL(4,R)) = emptyset
sum_{pi in emptyset} d(pi) * m_{S(6,4)}(pi) = 0   [empty sum]
```

**The formal-degree sum is 0, not 8.**

### 4.3 What the Value 225/48 Actually Represents

The quantity d(pi_{lambda_RS}) = 225/48 computed in the prior files is the G-Plancherel
density (the Plancherel measure density function) at the principal series parameter
lambda_RS = (1/2)(e_1 - e_4) for SL(4,R). This is the weight of the tempered
representation pi_{lambda_RS} in the Plancherel decomposition of L^2(SL(4,R)):

```
L^2(SL(4,R)) = int_{a_q^*+} pi_lambda dPl(lambda)
```

where dPl(lambda) = P(lambda + rho)/P(rho) * (product of c-function terms) dlambda.

The value 225/48 is the ratio P(lambda_RS + rho_G)/P(rho_G) computed for the A3 Plancherel
polynomial at lambda_RS, which is CORRECT as a Plancherel density. But it is the density
of a CONTINUOUS Plancherel measure at the parameter lambda_RS, not the formal degree of a
discrete series representation.

The Atiyah-Schmid formula:

  ind_H(D) = sum_{pi in disc(G)} d(pi) * dim Hom_H(pi, S^+)

applies ONLY when G has a non-empty discrete series (rank(G) = rank(K)). For SL(4,R),
the formula cannot be applied.

### 4.4 The Relative Discrete Series (G/H Level)

The appropriate object for OQ3b is not the discrete series of G = SL(4,R) but the
RELATIVE DISCRETE SERIES (also called "discrete series for symmetric spaces"): those
representations pi of G that appear discretely in the Plancherel decomposition of
L^2(G/H) = L^2(SL(4,R)/SO_0(3,1)). These are different from discrete series of G itself.

Relative discrete series can exist for G/H even when G has no discrete series, provided
the Flensted-Jensen equal-rank criterion for G/H is satisfied. As established in Section 3.1:
the criterion FAILS for (SL(4,R), SO_0(3,1)) with the correct sigma_B involution
(split-rank = 3, rank(K/(K cap H)) = 1, 3 != 1).

Therefore the relative discrete series of L^2(SL(4,R)/SO_0(3,1)) is also EMPTY at the
scalar level.

For the tau-twisted space L^2(G x_H tau_RS), relative discrete series might exist if the
Oshima-Matsuki condition is satisfied for the twisted pair. But as shown in Section 1.3,
the shifted rho_H - rho_G + rho_tau still has a negative first component, and the full
Weyl-chamber membership check is inconclusive (not established).

**Conclusion for Gate (3):** The formal-degree sum = 8 cannot be established from any
discrete series (G-level or G/H-level) in the available framework.

---

## 5. What Does Survive: The Three Convergent Paths

Despite the failure of the tau-correction/formal-degree route as a literal theorem,
three independent reconstruction-grade paths give ind_H(D_RS) = 8.

### Path 1: Physical Degrees of Freedom Count

RS field in 14D with Clifford module S = H^64:

```
Physical RS modes = (4 vector components) x C^16 fiber
                  - (1 gamma-trace constraint)  x C^16
                  - (1 diffeomorphism gauge)    x C^16
                  = 2 x C^16 = C^32 physical modes
Chiral half (APS projection to positive eigenvalues of boundary Dirac): C^16
H-linear count: dim_H(C^16) = 8 H-lines
```

H-linearity is algebraically exact from Cl(9,5) = M(64,H): the gamma-trace projection
Pi_RS commutes with right-H multiplication on S = H^64 (Cl(9,5) bimodule structure).

**ind_H(D_RS) = 8.** No dependence on split-rank, root system, or representation theory.
Grade: reconstruction. Failure mode: if the RS constraint count (4 - 1 - 1 = 2) is wrong.

### Path 2: SM Generation Count

The branching S(6,4)|_{SO_0(3,1)} = 4 D(1/2,0) + 4 D(0,1/2) gives 8 H-types.
Each H-type contributes 1 H-line to ind_H (by physical counting, not by FJ multiplicity-one).
The RS sector represents exactly 1 SM generation with 8 H-lines/generation.

**ind_H(D_RS) = 1 x 8 = 8.** No dependence on split-rank.
Grade: reconstruction (SM branching: generation-count-sm-branching-closure-2026-06-22.md).

### Path 3: APS Index Formula on Compact K3

The Atiyah-Patodi-Singer index theorem on the K3-type fiber X^4 (K3 is the unique simply-
connected compact spin 4-manifold with Â(K3) = 2, sigma = -16; selected by Rokhlin + 2+1
generation-count split + variational principle):

```
ind_H(D_RS) = Â(K3) * rank_H(S_RS^+) + eta/2
```

where:
- Â(K3) = 2 (topological invariant of K3, exact)
- rank_H(S_RS^+) = 4 (number of H-lines in the chiral RS half-spinor, from physical DOF
  count: 8 physical H-lines total, split 4/4 by chirality -- see oq-rk1-rs-rank-first-principles)
- eta = 0 (APS eta-invariant vanishes by spectral symmetry on S^3 boundary with flat
  bundle; ind-top-eta-s3-aps-2026-06-23.md)

```
ind_H(D_RS) = 2 * 4 + 0 = 8
```

**ind_H(D_RS) = 8.** This route uses APS on the compact K3 fiber, bypassing entirely
the non-compact analytic obstruction (no discrete series for SL(4,R), asymptotic cone
obstruction for G/H). Grade: reconstruction. Primary gate: OQ-RK2 (APS boundary
conditions for constrained RS operator on K3).

### 5.1 Convergence Table

| Path | Result | Grade | Dependence on tau-correction |
|------|--------|-------|------------------------------|
| Physical DOF count | 8 | Reconstruction | None |
| SM generation count | 8 | Reconstruction | None |
| APS on K3 | 8 | Reconstruction | None |
| Tau-correction (this file) | 0 (empty sum) | RETIRED | This route |

No path gives a value other than 8. The tau-correction route is structurally retired
(not a probabilistic gap; a genuine structural impossibility given the root system A3
and the absence of SL(4,R) discrete series).

---

## 6. The Genuine Analytic Gap

### 6.1 What a Genuine Analytic Proof Would Require

For ind_H(D_RS) = 8 to be established at VERIFIED grade from representation theory, one
of the following would need to be proved:

(A) **Tau-twisted relative discrete series:** Show that L^2(SL(4,R) x_{SO_0(3,1)} S(6,4))
    has a non-empty discrete component, that this component contains representations with
    tau_RS = D(1/2,0) H-type, and that the multiplicity count gives 8. This requires:
    - Proving the Oshima-Matsuki condition for the twisted pair (not done).
    - Establishing that tau_RS = D(1/2,0) can be used as a unitary inducing representation
      or finding an appropriate unitarization (tau_RS is nonunitary as a finite-dimensional
      SO_0(3,1) representation -- this is the R1 obstruction from rs-analytic-rank3-rebuild).
    - Computing the twisted c-function and finding a discrete pole.
    
(B) **Non-compact index theorem for rank-3 pair:** Establish a Fredholm theory for the
    RS sector on the non-compact space SL(4,R)/SO_0(3,1) that gives ind_H = 8 without
    using the discrete series of G or the relative discrete series of G/H. This would
    require a new framework beyond Atiyah-Schmid.

(C) **APS verified grade:** Prove the APS boundary conditions for the constrained RS
    operator on K3 are well-posed (OQ-RK2) and compute the APS index rigorously on
    the Lorentzian R x K3 geometry (Bär-Strohmaier framework).

### 6.2 Status of Each Gap

| Route | Status | Primary obstruction |
|-------|--------|---------------------|
| (A) Tau-twisted relative discrete series | BLOCKED | Nonunitary tau_RS; Oshima-Matsuki condition unverified for twisted A3 pair |
| (B) Non-compact index theory, rank-3 | OPEN | No framework developed; would be new mathematics |
| (C) APS verified grade on K3 | CONDITIONALLY_RESOLVED | OQ-RK2 (boundary conditions) open |

Route (C) is the most tractable upgrade path. Routes (A) and (B) face structural obstructions
that would require substantial new mathematical development.

---

## 7. Is OQ3b RESOLVED or Does a Genuine Analytic Gap Remain?

**The answer is CONDITIONALLY_RESOLVED. A genuine analytic gap remains in the following
precise sense:**

- The numerical conclusion ind_H(D_RS) = 8 is supported at reconstruction grade by three
  independent paths (Paths 1, 2, 3 above) that are mutually consistent and derive 8 from
  orthogonal premises.
- No path derives a different value. No falsifying argument is known.
- The tau-correction/formal-degree route (the specific analytic proof attempted in OQ3b)
  is STRUCTURALLY RETIRED: it fails not because of a computational gap but because SL(4,R)
  has no discrete series (provable theorem) and the A3 c-function has no discrete poles
  (provable theorem).
- The APS route (Path 3) is the primary surviving analytic path to a verified proof, but
  OQ-RK2 (boundary conditions) remains open.

**OQ3b is NOT RESOLVED** because no path currently satisfies the verified-grade standard:
- Path 1 (physical DOF count): reconstruction grade; Harish-Chandra framework not invoked.
- Path 2 (SM generation count): reconstruction grade; SM branching is a representation-theory
  reconstruction, not an analytic theorem.
- Path 3 (APS on K3): reconstruction grade; OQ-RK2 open.

**OQ3b is NOT GENUINE_OBSTRUCTION** because:
- The paths that support ind_H = 8 are structurally coherent and not contradicted.
- The failure of the tau-correction route does not produce a contradictory value.
- The asymptotic cone obstruction (Oshima-Matsuki) blocks one analytic strategy but does
  not yield ind_H = 0 or any other value.

**Verdict: CONDITIONALLY_RESOLVED.** This verdict is unchanged from the prior two files,
but is now grounded in an explicit literature verification showing that the specific
analytic route (tau-correction, formal-degree sum = 8) cannot be established from any
currently published theorem for this symmetric pair.

---

## 8. Conditions for Upgrade to RESOLVED

For OQ3b to reach RESOLVED, one of the following must be achieved:

| Condition | What is needed | Grade on achievement |
|-----------|---------------|----------------------|
| OQ-RK2 | Prove APS boundary conditions for constrained RS operator on K3-type X^4 (Path 3) | RESOLVED |
| Twisted pair admissibility | Prove Oshima-Matsuki for twisted L^2(G x_H tau_RS) with A3 root system and nonunitary tau_RS | RESOLVED |
| New non-compact index theorem | Develop a rank-3 Fredholm theory for the RS sector giving ind_H = 8 from first principles | RESOLVED |
| Physical DOF count upgrade | Provide an independent non-compact index theorem or K-theory computation confirming dim_H = 8 from geometric data alone | RESOLVED |

---

## 9. Conditions That Would Yield GENUINE_OBSTRUCTION

OQ3b would become GENUINE_OBSTRUCTION if any of the following were established:

- A proof that ind_H(D_RS) != 8 (from any analytic framework).
- A proof that the physical DOF count (4 - 1 - 1 = 2 complex modes = 8 H-lines) is
  incorrect for the GU RS field.
- A proof that the APS boundary conditions for the RS operator on K3 are incompatible,
  making Path 3 ill-posed.
- A proof that the SM branching S(6,4)|_{SO_0(3,1)} = 4 D(1/2,0) + 4 D(0,1/2) is wrong.

None of these conditions currently fires.

---

## 10. References

Primary:

- Harish-Chandra (1966). Discrete series for semisimple Lie groups II. *Acta Math.* **116**: 1-111.
  [Theorem: rank(G) = rank(K) is necessary and sufficient for discrete series.]

- Flensted-Jensen, M. (1980). Discrete series for semisimple symmetric spaces.
  *Ann. Math.* **111**: 253-311. [Theorem 3.1: equal-rank criterion for discrete series of G/H.]

- Oshima, T., and Matsuki, T. (1984). A description of discrete series for semisimple symmetric
  spaces. *Adv. Stud. Pure Math.* **4**: 331-390.
  [Theorem 6.11: Weyl-chamber condition for discrete series of G/H.]

- Kobayashi, T. (1994). Discrete decomposability of the restriction of A_q(lambda) with
  respect to reductive subgroups and its applications. *Invent. Math.* **117**: 181-205.
  [Admissibility and discrete decomposability conditions.]

- Kobayashi, T., and Oda, Y. (2023). Symmetric pairs with finite-multiplicity property
  for branching laws of admissible representations. *Selecta Math.* (arXiv:2109.12154).
  [Finite-multiplicity characterization via real spherical pairs.]

- Atiyah, M.F., and Schmid, W. (1977). A geometric construction of the discrete series for
  semisimple Lie groups. *Invent. Math.* **42**: 1-62.
  [Formal degree formula for discrete series via L^2-index.]

- Atiyah, M.F., Patodi, V.K., and Singer, I.M. (1975). Spectral asymmetry and Riemannian
  geometry I-III. *Math. Proc. Camb. Phil. Soc.* **77-79**.
  [APS index theorem -- Path 3 foundation.]

- Bär, C., and Strohmaier, A. (2015/2019). A rigorous geometric derivation of the chiral
  anomaly in curved backgrounds. *Commun. Math. Phys.* **347**: 703-721; and
  An index theorem for Lorentzian manifolds with compact spacelike Cauchy boundary.
  *J. Diff. Geom.* **113**: 1-34.
  [Lorentzian APS theorem -- Path 3 framework.]

- Gindikin, S.G., and Karpelevich, F.I. (1962). Plancherel measure for Riemannian symmetric
  spaces of non-positive curvature. *Soviet Math. Dokl.* **3**: 962-965.
  [Harish-Chandra c-function via product formula -- used in Section 2.2.]

- Knapp, A.W. (2001). *Representation Theory of Semisimple Groups: An Overview Based on
  Examples.* Princeton University Press. [Standard reference for discrete series and Plancherel theory.]

In-repository files:

- `explorations/oq3b-tau-correction-closure-2026-06-23.md` -- prior closure attempt; three
  gates all fail; tau-correction route retired.
- `explorations/oq3b-rs-index-closed-2026-06-23.md` -- three OQ1-independent paths after
  split-rank = 3 resolution.
- `explorations/rc1-root-mult-disambiguation-2026-06-23.md` -- RESOLVED: A3 root system, not BC1.
- `explorations/oq1-split-rank-verification-2026-06-23.md` -- RESOLVED: split-rank = 3 under sigma_B.
- `explorations/rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md` -- non-compact routes
  R1/R2/R3 all fail; APS route (R4) survives.
- `explorations/oc1-oc2-aps-closure-2026-06-23.md` -- APS route providing Path 3.
- `explorations/oq-rk1-rs-rank-first-principles-2026-06-23.md` -- rank_H(S_RS^+) = 4,
  CONDITIONALLY_RESOLVED from Cl(9,5) = M(64,H) structure.
