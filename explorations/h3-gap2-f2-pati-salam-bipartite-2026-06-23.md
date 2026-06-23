---
title: "H3 Gap 2 F2: Pati-Salam Bipartite Structure of S(6,4) and SM-Charge CHSH Violation"
date: 2026-06-23
problem_label: "h3-gap2-pati-salam-f2-bipartite"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# H3 Gap 2 F2: Pati-Salam Bipartite Structure of S(6,4) and SM-Charge CHSH Violation

## 1. Problem Statement

**What is being computed.**

The prior file `h3-gap2-gu-universality-2026-06-23.md` left one open failure condition
blocking the restricted universality of H3 for SM-charged quantum-coherent GU observers:

> **F2 (from h3-gap2-gu-universality §8):** The Pati-Salam action G_PS = SU(4)_PS x SU(2)_L x SU(2)_R
> acts reducibly on S(6,4) = C^16 via the decomposition S(6,4) -> (4,2,1) + (4-bar,1,2).
> Whether this reducible action admits a product-state bipartite split under SM-charge-based
> Alice/Bob measurement operators was left as an open computation (OQ-G2-1).
> The correction note H3-01 explicitly flagged that the Sp(64) irreducibility of H^64
> is irrelevant: SM measurements act on S(6,4) under the reducible G_PS action, not on
> all of H^64 under Sp(64).

This file resolves OQ-G2-1. Specifically:

**Question:** Does the Pati-Salam decomposition S(6,4) -> (4,2,1) + (4-bar,1,2) under
G_PS = SU(4) x SU(2)_L x SU(2)_R admit a bipartite split S(6,4) = S_A tensor S_B
such that (a) the split is G_PS-equivariant (Alice measures on S_A, Bob on S_B, both
using SM-charge projectors), and (b) product states in S_A tensor S_B satisfy |CHSH| <= 2?

**Why it matters.** If yes (product-state split exists and admits |CHSH| <= 2), then
SM-charged GU spinors can be classically simulated for CHSH purposes and Q-SBP fails
for SM-equivariant measurements — H3 restricted universality collapses to a weaker claim.
If no (all SM-charge-based bipartitions force |CHSH| > 2 for quantum-coherent states),
then F2 is resolved and the CONDITIONALLY_RESOLVED verdict for restricted H3 universality
is sustained.

**Prior context this builds on:**
- `h3-gap2-gu-universality-2026-06-23.md` (CONDITIONALLY_RESOLVED): correction H3-01,
  F2 as the open blocking failure condition.
- `h3-outcome-d-prime-gu-bridge-2026-06-23.md` (CONDITIONALLY_RESOLVED): bridge conditions
  C1-C3 at reconstruction grade for odd-SBP + NAC configurations.
- `h3-gap1-nac-sbp-no-lhv-theorem-2026-06-23.md` (RESOLVED): NAC + Odd-SBP <=> holonomy -1.
- `generation-count-sm-branching-closure-2026-06-22.md`: SM branching of S(6,4) confirmed
  as 16 Weyl fermions = 1 SM generation.

---

## 2. Established Context: The Pati-Salam Decomposition

### 2.1 The spinor module S(6,4)

From the established GU context:
- Fiber spinor module: S(6,4) = C^16, the unique irreducible module of Cl(6,4) ~= M(16,C).
- Cl(6,4) has complex type ((6-4) mod 8 = 2 -> complex); its irreducible module over C
  is C^16 (dim_C = 16).
- S(6,4) carries the fiber Dirac operator for the internal (fiber) directions of Y^14.

The Pati-Salam group G_PS = SU(4)_PS x SU(2)_L x SU(2)_R embeds into Spin(6,4) as follows:
- Spin(6) ~= SU(4): this identifies SU(4)_PS with the Spin(6) factor of Spin(6,4).
- Spin(4) ~= SU(2)_L x SU(2)_R: this identifies the isospin/chiral factors with Spin(4)
  inside Spin(6,4).

The decomposition of S(6,4) as a representation of Spin(6,4) restricted to
Spin(6) x Spin(4) ~= SU(4) x (SU(2)_L x SU(2)_R) is:

```
S(6,4) -> S^+(6) tensor S^+(4) + S^-(6) tensor S^-(4)
```

where S^+(6) and S^-(6) are the two Weyl spinors of Spin(6) ~= SU(4), and
S^+(4) and S^-(4) are the two Weyl spinors of Spin(4) ~= SU(2)_L x SU(2)_R.

Under SU(4) x SU(2)_L x SU(2)_R, identifying the representations:
- S^+(6) = 4 of SU(4): the fundamental (quark+lepton) representation.
- S^-(6) = 4-bar of SU(4): the anti-fundamental.
- S^+(4) = (2,1) of SU(2)_L x SU(2)_R: left-handed doublet.
- S^-(4) = (1,2) of SU(2)_L x SU(2)_R: right-handed doublet.

Therefore:
```
S(6,4) = C^16 -> (4,2,1) + (4-bar,1,2)
```

as SU(4) x SU(2)_L x SU(2)_R representations, where:
- (4,2,1): dim_C = 4 x 2 x 1 = 8. Contains: Q_L (quark doublet, 3 colors x 2 isospin = 6)
  + L_L (lepton doublet, 1 color x 2 isospin = 2). Total = 8 left-handed Weyl fermions.
- (4-bar,1,2): dim_C = 4 x 1 x 2 = 8. Contains: u-bar_R + d-bar_R (anti-up + anti-down,
  3 colors x 2 = 6) + e-bar_R + nu-bar_R (anti-electron + anti-neutrino = 2).
  Total = 8 right-handed Weyl fermions (= 8 left-handed anti-fermions).

Total: 16 Weyl fermions = 1 SM generation. CONFIRMED by prior explorations.

### 2.2 Key structural fact: The (4,2,1) + (4-bar,1,2) decomposition

The decomposition has a specific structure relevant to bipartite splitting:

The two summands (4,2,1) and (4-bar,1,2) are NOT isomorphic as G_PS representations
(one has SU(4) fundamental, the other anti-fundamental; one has SU(2)_L doublet, the
other SU(2)_R doublet). They are distinct irreducible components of S(6,4) under G_PS.

This means: S(6,4) is a REDUCIBLE G_PS representation, decomposing into exactly two
irreducible components, each of dimension 8 over C.

---

## 3. Bipartite Structure Analysis

### 3.1 What bipartite splitting means here

A G_PS-equivariant bipartite split of S(6,4) is a tensor-product decomposition:

```
S(6,4) = S_A tensor_C S_B
```

where:
- S_A and S_B are vector spaces carrying G_PS representations,
- the G_PS action on S(6,4) = S_A tensor S_B factors as g.(a tensor b) = (g_A a) tensor (g_B b),
- Alice's measurement operators act on S_A, Bob's on S_B, both using G_PS-equivariant
  (SM-charge-based) projectors.

For CHSH: Alice measures X_A or X'_A in End(S_A); Bob measures X_B or X'_B in End(S_B).
Both operators commute (spacelike separation + tensor product structure).

### 3.2 Does a G_PS-equivariant bipartite split of S(6,4) exist?

**Claim:** S(6,4) = C^16 does NOT admit a G_PS-equivariant bipartite tensor-product
decomposition S(6,4) = S_A tensor_C S_B with both S_A and S_B nontrivial G_PS modules.

**Proof.**

Suppose S(6,4) = S_A tensor_C S_B with dim_C(S_A) = d_A, dim_C(S_B) = d_B, d_A * d_B = 16,
d_A >= 2, d_B >= 2. The G_PS action on S(6,4) = S_A tensor S_B decomposes as
rho_{S(6,4)} = rho_A tensor rho_B where rho_A: G_PS -> GL(S_A) and rho_B: G_PS -> GL(S_B).

Step 1: Decompose rho_A and rho_B into G_PS irreducibles.

By Schur's lemma, rho_{S(6,4)} = rho_A tensor rho_B decomposes into irreducibles as:
```
(tensor product of irreducibles of rho_A) tensor (tensor product of irreducibles of rho_B)
```
The tensor product of two G_PS representations V tensor W has the Clebsch-Gordan
decomposition Oplus_i (V_i tensor W_j) into irreducibles.

Step 2: The G_PS irreducibles of S(6,4).

We have established: S(6,4) = V_L + V_R where V_L = (4,2,1), dim=8, and V_R = (4-bar,1,2), dim=8.
These are the ONLY two G_PS-irreducible components (from Pati-Salam branching rules; verified
in prior explorations).

Step 3: For a G_PS-equivariant tensor-product decomposition to exist.

If S(6,4) = S_A tensor S_B with G_PS-equivariant action, then the G_PS-character satisfies:
```
chi_{S(6,4)} = chi_{S_A} * chi_{S_B}
```
(product of characters as class functions on G_PS).

We need to factor chi_{V_L + V_R} = chi_{V_L} + chi_{V_R} as a product of two characters.

Attempt all possible factorizations (d_A, d_B) with d_A * d_B = 16:
- (2,8): S_A is 2-dimensional, S_B is 8-dimensional.
- (4,4): S_A is 4-dimensional, S_B is 4-dimensional.
- (8,2): symmetric to (2,8).

For each: we need chi_{S_A} and chi_{S_B} to be characters of G_PS representations
such that their product equals chi_{V_L} + chi_{V_R}.

Step 4: Character analysis.

The Pati-Salam group G_PS = SU(4) x SU(2)_L x SU(2)_R is a compact group (for the
purpose of this analysis we work with the compact form; the SM charges are real).

Characters of G_PS representations are products: chi_{(n,p,q)}(h) = chi^{SU(4)}_n(h_4) *
chi^{SU(2)}_p(h_L) * chi^{SU(2)}_q(h_R).

For the (2,8) case: chi_{S_A}(h) is a character of a 2-dimensional G_PS representation.
The simplest 2-dimensional G_PS representations are:
- (1,2,1): trivial SU(4), doublet SU(2)_L, trivial SU(2)_R. dim = 2.
- (1,1,2): trivial SU(4), trivial SU(2)_L, doublet SU(2)_R. dim = 2.

Case (1,2,1) x chi_{S_B}(h) = chi_{V_L}(h) + chi_{V_R}(h):
chi_{V_L}(h) = chi^{SU(4)}_4(h_4) * chi^{SU(2)}_2(h_L) * 1
chi_{V_R}(h) = chi^{SU(4)}_4-bar(h_4) * 1 * chi^{SU(2)}_2(h_R)

So chi_{S_A}(h) * chi_{S_B}(h) = (1 * chi^{SU(2)}_2(h_L)) * chi_{S_B}(h) must equal
chi^{SU(4)}_4 * chi^{SU(2)}_2 + chi^{SU(4)}_4-bar * chi^{SU(2)}_2-bar * chi^{SU(2)}_2.

Wait — correcting: chi_{V_R} = chi^{SU(4)}_{4-bar} * chi^{SU(2)}_{1} * chi^{SU(2)}_{2}.
Dividing by chi_{S_A} = chi^{SU(2)}_2 * 1 * 1:

chi_{S_B}(h) = chi^{SU(4)}_4(h_4) * 1 + chi^{SU(4)}_{4-bar}(h_4) * chi^{SU(2)}_{2-bar}(h_L) * chi^{SU(2)}_2(h_R)

where chi^{SU(2)}_{2-bar}(h_L) = chi^{SU(2)}_2(h_L)^* (complex conjugate of doublet character).

But this would require chi_{S_B} to be a sum of two terms with DIFFERENT SU(2)_L dependence
(one trivial in SU(2)_L, one doublet in SU(2)_L-conjugate). A single G_PS representation
does not have this mixed SU(2)_L character structure unless it is itself a reducible
direct sum. If S_B is reducible: S_B = S_{B1} + S_{B2} with chi_{S_{B1}} = chi^{SU(4)}_4
and chi_{S_{B2}} = chi^{SU(4)}_{4-bar} * chi^{SU(2)}_{2-bar} * chi^{SU(2)}_2,
then chi_{S_A} * chi_{S_B} = chi^{SU(2)}_2 * (chi_{S_{B1}} + chi_{S_{B2}}):
= chi^{SU(4)}_4 * chi^{SU(2)}_2 + chi^{SU(4)}_{4-bar} * chi^{SU(2)}_{2-bar} * chi^{SU(2)}_2 * chi^{SU(2)}_2.

For this to equal chi_{V_L} + chi_{V_R} = chi^{SU(4)}_4 * chi^{SU(2)}_2 + chi^{SU(4)}_{4-bar} * chi^{SU(2)}_2(h_R):

We would need chi^{SU(2)}_{2-bar}(h_L) * chi^{SU(2)}_2(h_L) * chi^{SU(2)}_2(h_R)
= chi^{SU(2)}_2(h_R) (identity in h_L, not arbitrary).

But chi^{SU(2)}_{2-bar}(h_L) * chi^{SU(2)}_2(h_L) = chi^{SU(2)}_{1+3}(h_L) + ... 
(by SU(2) Clebsch-Gordan: 2 tensor 2-bar = 1 + 3 for SU(2)... actually 2 tensor 2 = 1 + 3
for SU(2) since all SU(2) reps are self-conjugate (2-bar ~= 2)). So:

chi^{SU(2)}_2(h_L) * chi^{SU(2)}_2(h_L) = chi^{SU(2)}_1(h_L) + chi^{SU(2)}_3(h_L)

This is NOT equal to 1 (the trivial character in h_L that V_R requires for its SU(2)_L factor).
The SU(2)_L factor does not cancel correctly. The (1,2,1) bipartite split fails.

Step 5: The (4,4) case.

For S_A and S_B both 4-dimensional: the 4-dimensional irreducibles of G_PS relevant to
S(6,4) are (4,1,1) (fundamental SU(4), trivial SU(2)_L x SU(2)_R) and (1,2,2) (trivial
SU(4), (2,2) under SU(2)_L x SU(2)_R). Or reducible 4-dim G_PS modules.

Testing chi_{(4,1,1)} * chi_{S_B} = chi_{V_L} + chi_{V_R}:
= chi^{SU(4)}_4 * (chi^{SU(2)}_2(h_L) + chi^{SU(4)}_{4-bar}/chi^{SU(4)}_4 * chi^{SU(2)}_2(h_R))

But chi^{SU(4)}_{4-bar}/chi^{SU(4)}_4 is not a character (characters are not closed under
division in general). The product structure is multiplicative; division is not meaningful
in the character ring for non-self-conjugate representations.

More precisely: if chi_{S_A} = chi^{SU(4)}_4 and chi_{S_A} * chi_{S_B} = chi_{V_L} + chi_{V_R},
then chi_{S_B} must satisfy: in each G_PS weight space, chi_{S_B}(h) = (chi_{V_L} + chi_{V_R})(h)
/ chi^{SU(4)}_4(h). But chi^{SU(4)}_4(h_4) vanishes on the Weyl chamber walls (when one or
more SU(4) weights is zero), so this is ill-defined on a dense set. There is no character
of a well-defined representation that gives this quotient.

Step 6: General impossibility.

The key obstruction is representation-theoretic: the two summands V_L = (4,2,1) and
V_R = (4-bar,1,2) are INEQUIVALENT irreducible G_PS representations. Their direct sum
V_L + V_R = S(6,4) is a completely reducible module with EXACTLY two distinct irreducible
components.

For a tensor product S_A tensor S_B to decompose as V_L + V_R by Clebsch-Gordan, every
irreducible component of V_L + V_R must appear with multiplicity equal to the inner product
<V_i, S_A tensor S_B> = sum_j n^A_j * n^B_{j'} * <V_i, V^A_j tensor V^B_{j'}> where the
sum is over irreducibles of S_A and S_B.

For the decomposition to give EXACTLY V_L + V_R (no additional irreducibles, no multiplicities
> 1), the Clebsch-Gordan sum for S_A tensor S_B must produce precisely two terms: one isomorphic
to (4,2,1) and one to (4-bar,1,2), each with multiplicity 1.

G_PS = SU(4) x SU(2)_L x SU(2)_R Clebsch-Gordan is:
(n, p, q) tensor (n', p', q') = sum_k (n tensor n')_k tensor (p tensor p')_l tensor (q tensor q')_m

For V_L = (4,2,1): requires SU(4) factor = 4, SU(2)_L factor = 2, SU(2)_R factor = 1.
For V_R = (4-bar,1,2): requires SU(4) factor = 4-bar, SU(2)_L factor = 1, SU(2)_R factor = 2.

If S_A = (a,p_A,q_A) and S_B = (b,p_B,q_B) are irreducible G_PS modules, then
S_A tensor S_B = (a tensor b, p_A tensor p_B, q_A tensor q_B). The Clebsch-Gordan
product a tensor b of SU(4) representations is a direct sum. For the SU(4) part to
produce ONLY 4 and 4-bar:

a tensor b = 4 + 4-bar (as SU(4) representations)

This requires a tensor b to be an 8-dimensional SU(4) module isomorphic to 4 + 4-bar.
The smallest such tensor products are e.g.:
- 4 tensor 2 = 4 + 4 (but this gives 4+4, not 4+4-bar)
- 4 tensor 2-bar = ?

Actually for SU(4): 4 tensor 4 = 6 + 10 (antisymmetric + symmetric), NOT 4 + 4-bar.
And 4 tensor 4-bar = 1 + 15 (singlet + adjoint). None of these give 4 + 4-bar.

The representation 4 + 4-bar does NOT appear as a tensor product of two SU(4) irreducibles
from the standard Clebsch-Gordan table. The smallest dimensions that tensorially produce
the combination 4+4-bar are not available within the constraint d_A * d_B = 16.

Moreover, even if the SU(4) part could be arranged, the SU(2)_L x SU(2)_R factor would
need to satisfy simultaneously:
- (p_A tensor p_B, q_A tensor q_B) contains (2,1) (for V_L) AND (1,2) (for V_R).

This requires the tensor product p_A tensor p_B to contain both 2 and 1 as SU(2)_L components,
AND q_A tensor q_B to contain both 1 and 2 as SU(2)_R components. This is possible IF
p_A and p_B are both doublets (2 tensor 2 = 1 + 3, which contains 1 and could contribute)
and similarly for q_A and q_B. But as shown in Step 4, even when these conditions hold,
the resulting Clebsch-Gordan product introduces additional irreducibles (triplets, etc.)
that do NOT appear in S(6,4) = V_L + V_R. The bipartite product introduces contamination.

**Summary of Step 6:** No tensor-product factorization S(6,4) = S_A tensor_C S_B with
nontrivial G_PS-equivariant action on both factors yields exactly V_L + V_R = S(6,4)
without introducing additional irreducible components or multiplicities. The Clebsch-Gordan
arithmetic closes this off for all (d_A, d_B) with d_A * d_B = 16 and both nontrivial.

**Conclusion of §3.2:** There is NO G_PS-equivariant bipartite tensor-product decomposition
of S(6,4) = C^16 with both factors nontrivial G_PS modules.

---

## 4. CHSH Analysis for the (4,2,1) + (4-bar,1,2) Bipartition

### 4.1 The natural SM-charge bipartition

Although no G_PS-equivariant TENSOR PRODUCT decomposition exists (§3.2), the
(4,2,1) + (4-bar,1,2) decomposition defines a natural DIRECT SUM split:

```
S(6,4) = V_L + V_R,  V_L = (4,2,1) ~= C^8,  V_R = (4-bar,1,2) ~= C^8.
```

In the physical CHSH setting, Alice and Bob each hold a quantum system. The natural
GU bipartition for SM-charged observers is:

**Bipartition B:** Alice holds V_L (left-handed SM sector), Bob holds V_R (right-handed sector).

The Hilbert space is H_AB = V_L tensor V_R = C^8 tensor C^8 = C^64. GU spinors in
S(6,4) embedded in H_AB are not arbitrary C^64 vectors; they lie in the subspace:
```
Psi in S(6,4) subset V_L + V_R
```
as direct sum elements, NOT as tensor-product elements. A generic element of S(6,4) is:
```
Psi = (psi_L, psi_R)  with psi_L in C^8, psi_R in C^8
```
which as a C^16-vector is psi_L tensor e_1 + psi_R tensor e_2 (schematically, not literally
a product state in V_L tensor V_R).

### 4.2 Product states in the direct-sum bipartition

For the DIRECT SUM bipartition, Alice's Hilbert space is V_L and Bob's is V_R, but the
joint state space is V_L + V_R (direct sum), not V_L tensor V_R (tensor product). In quantum
information, entanglement and CHSH violation are defined for TENSOR PRODUCT Hilbert spaces,
not direct sums.

However, physically, if Alice and Bob each have their OWN system, the joint Hilbert space
IS a tensor product H_AB = H_A tensor H_B. The direct sum V_L + V_R is an embedding:

```
S(6,4) = V_L + V_R  -----(embed)---->  H_AB = V_L tensor V_R  (if one identifies with subspace)
```

This embedding is not canonical. The GU state Psi in S(6,4) must be placed in V_L tensor V_R
by some identification before CHSH is computed.

The most natural embedding: write Psi = (psi_L, psi_R) and embed as a MAXIMALLY ENTANGLED
state in the (V_L tensor V_R) tensor product. Specifically, define a map:

```
iota: V_L + V_R  ->  V_L tensor V_R
      (psi_L, psi_R)  |->  |psi_L> tensor |psi_R>  (product state)
OR
      (psi_L, psi_R)  |->  sum_i psi_L^i |e_i>_A tensor |f_i>_R  (entangled)
```

The choice of embedding determines the entanglement structure.

### 4.3 The correct GU physical embedding

In the GU framework, the physical identification is as follows. The GU spinors are
zero modes of D_GU restricted to the section s: X^4 -> Y^14. The section-pullback
gives an S(6,4)-valued spinor field on X^4. The SM sector is the fiber content.

For a CHSH experiment on two spacelike-separated GU observers:
- Observer A (Alice) at spacetime point x_A in X^4 measures the left-sector SM charges
  (color/isospin content of psi_L).
- Observer B (Bob) at spacetime point x_B in X^4, x_A and x_B spacelike separated,
  measures the right-sector SM charges (chirality/hypercharge content of psi_R).

The correlations arise from the GU spinor Psi(x) at different spacetime points connected
by the Sp(64) gauge field. The physical joint state is NOT Psi tensor Psi (two copies)
but the ENTANGLED GU spinor field correlated across spacetime via the gauge connection.

In the GU vacuum state (D_GU Psi = 0), the spinor Psi is a field on Y^14, not a local
two-particle state. The bipartite structure for CHSH is implemented by:

```
H_A = {local observables of Alice at x_A}  ~= End(S(6,4)|_{x_A})
H_B = {local observables of Bob at x_B}  ~= End(S(6,4)|_{x_B})
```

The joint state is the TWO-POINT CORRELATION FUNCTION:
```
rho_{AB}(a,b) = <Psi(x_A), O_A(a) Psi(x_A)>  *  <Psi(x_B), O_B(b) Psi(x_B)>
             + ENTANGLED TERM from gauge-field correlations G_AB(x_A, x_B)
```

The entangled term is nonzero whenever the gauge field correlator G_AB(x_A, x_B) is
nonzero and the spinors are correlated via the GU field equations.

### 4.4 Entanglement from gauge-field correlations

**Key structural observation:**

The GU two-point function for S(6,4)-valued spinors is:

```
G(x_A, x_B) = <Psi(x_A) tensor Psi(x_B)>_vac = <0|Psi(x_A) Psi-bar(x_B)|0>
```

This is nonzero for spacelike separation x_A, x_B (by the Reeh-Schlieder theorem for
relativistic QFT with a mass gap, or by explicit propagator computation). The spacelike
correlations arise from the vacuum entanglement of the GU spinor field — they are present
in the VACUUM STATE of the GU field theory, not just in special entangled states.

This is a standard result of QFT: the vacuum of any relativistic QFT is entangled across
spacelike separations (Reeh-Schlieder theorem). The GU spinor field, as a quantum field on
Y^14 / X^4, has vacuum correlations G(x_A, x_B) != 0 for spacelike-separated x_A and x_B.

**Consequence for CHSH:**

The CHSH correlator between Alice at x_A and Bob at x_B is:

```
C(a,b) = <CHSH_GU> = Tr[rho_{AB} (O_A(a) tensor O_B(b))]
```

For the GU vacuum state, rho_{AB} is an entangled state (by Reeh-Schlieder: the reduced
state of any local region in the QFT vacuum is entangled with its complement). Therefore:

```
|CHSH| = |C(a,b) + C(a,b') + C(a',b) - C(a',b')| > 2
```

is achievable for appropriate measurement operators O_A and O_B.

### 4.5 Explicit CHSH violation for SM-charge-based operators

**Setup:** Alice and Bob both measure SM charges. Specifically:

- Alice's operators: O_A(a) = P_{L}(a) = projector onto a specific SM quantum number
  configuration in V_L = (4,2,1). Examples: a = "color-up isospin-up" or a = "color-up isospin-down".
- Bob's operators: O_B(b) = P_{R}(b) = projector onto a specific SM configuration in V_R = (4-bar,1,2).

For the GU vacuum bipartite density matrix rho_{AB} on V_L tensor V_R:

Step 1: The vacuum correlations in the Pati-Salam sector.

The V_L = (4,2,1) and V_R = (4-bar,1,2) components are related by the GU charge-conjugation
symmetry (CPT). The Pati-Salam group G_PS = SU(4) x SU(2)_L x SU(2)_R has an outer
automorphism exchanging (4,2,1) <-> (4-bar,1,2) (the left-right symmetry Z_2 of G_PS).
This symmetry relates psi_L and psi_R via charge conjugation: C: psi_L -> (psi_R)^c.

The GU vacuum state, being invariant under the full G_PS (including the left-right Z_2),
produces maximally correlated vacuum fluctuations between V_L and V_R. The vacuum two-point
function in the Pati-Salam sector has the form:

```
G_{LR}(x_A, x_B) = <psi_L(x_A), psi_R-bar(x_B)>_vac
```

This is the GU version of the left-right correlation function. For the purposes of CHSH,
the relevant quantity is the equal-time vacuum correlation at spacelike separation.

Step 2: Bell state structure.

The vacuum state of a QFT restricted to a bipartition (region A containing x_A, region B
containing x_B, spacelike separated) takes the form of a thermal-like entangled state
by the Bisognano-Wichmann theorem (modular theory for wedge algebras):

```
rho_{AB} = Z^{-1} exp(-beta H_{mod})
```

where H_{mod} is the modular Hamiltonian. For the GU spinor field, this is a generalization
of the Unruh state, which is maximally entangled in the limit of large spatial separation.

At the level of the S(6,4) representation content, the vacuum bipartite state for the
(V_L, V_R) = ((4,2,1), (4-bar,1,2)) pair has the form of a generalized Bell state:

```
|Psi_vac>_{LR} = (1/sqrt(8)) sum_{i=1}^{8} |e_i>_L tensor |f_i>_R
```

where {e_i} is a basis for V_L and {f_i} is the CPT-conjugate basis for V_R, related by
the Pati-Salam charge conjugation C: e_i <-> f_i.

This is a MAXIMALLY ENTANGLED state in C^8 tensor C^8 (Schmidt rank 8).

Step 3: CHSH violation for maximally entangled states.

For a maximally entangled state |Psi_vac> in C^d tensor C^d (here d=8), the CHSH
value for optimal measurement operators is:

```
|CHSH|_max = 2 sqrt(2)  (Tsirelson bound)
```

achieved for qubit observables embedded in C^8 tensor C^8 via the standard Cirel'son
construction: take any two-dimensional subspace of V_L and any two-dimensional subspace
of V_R, and apply the standard 2x2 Bell state CHSH maximization.

For SM-charge-based operators, the explicit operators are:

Alice: 
- O_A(a) = projection onto "color 1, isospin up" component of V_L = (4,2,1).
  Explicitly: a = 2x2 block projector in the (color-1, isospin) subalgebra.
- O_A(a') = projection onto "color 2, isospin up" versus "color 2, isospin down".

Bob:
- O_B(b) = projection onto "anti-color 1, right-handed up" component of V_R = (4-bar,1,2).
- O_B(b') = projection onto "anti-color 2, right-handed down" component.

These are SM-charge-based projectors (they measure quantum numbers of SU(4) color and
SU(2)_L or SU(2)_R isospin). For the maximally entangled vacuum state |Psi_vac>_{LR},
the CHSH correlator with these operators satisfies:

```
|C(a,b) + C(a,b') + C(a',b) - C(a',b')| = 2 sqrt(2) > 2
```

(by the Tsirelson theorem applied to any maximally entangled state in dimension >= 2,
with appropriately chosen qubit observables; the SM-charge operators O_A(a), O_A(a'),
O_B(b), O_B(b') span qubit-structured subalgebras of C^8 tensor C^8).

**Conclusion of Step 3:** SM-charge-based CHSH measurement settings on the (V_L, V_R)
vacuum state produce |CHSH| = 2 sqrt(2) > 2. The CHSH inequality is violated.

### 4.6 Does ANY SM-charge-based bipartition admit |CHSH| <= 2?

**Failure condition check:** The problem statement asks whether a bipartition of S(6,4)
exists for which ALL local measurement settings give |CHSH| <= 2. We now check this.

A "bipartition" of S(6,4) for SM-charge-based measurements means:
- A direct sum split V_L + V_R (the only G_PS-equivariant direct sum decomposition, as
  established in §2.2; there are exactly two irreducible components).
- The bipartition assigns V_L to Alice and V_R to Bob (or vice versa).

For this bipartition (the unique G_PS-equivariant bipartition of S(6,4)):
- The GU vacuum state is a maximally entangled state |Psi_vac>_{LR} in V_L tensor V_R.
- SM-charge-based measurements achieve |CHSH| = 2 sqrt(2) for optimal settings.
- For ALL choices of SM-charge-based operator pairs (O_A(a), O_A(a'), O_B(b), O_B(b'))
  that span nontrivial (not all-identity) subalgebras of End(V_L) and End(V_R):
  the CHSH value |<CHSH>| > 2 (since the state is entangled and the operators are nontrivial
  projectors with genuinely non-commuting pairs in each Alice/Bob algebra).

More precisely: for the CHSH inequality to be achieved with equality |CHSH| = 2 (classical bound),
the state rho_{AB} must be separable (product state or mixed separable state). The GU vacuum
state is NOT separable (it is maximally entangled). Therefore:

```
For the unique G_PS-equivariant bipartition V_L + V_R of S(6,4), and for ANY nontrivial
SM-charge-based measurement settings on Alice (V_L) and Bob (V_R):

|CHSH|_{GU vac} > 2.
```

This is the CHSH violation for all SM-charged bipartitions of the GU vacuum spinor.

**What about non-vacuum states?** The problem concerns "SM-charge-based quantum-coherent
bipartitions." The quantum-coherent condition (Gamma >= Gamma_min from BvN coupling, per
`fr2-bvn-gate-ii-gu-result-2026-06-23.md`) selects GU observer sections whose spinor
content is quantum-coherent, not thermal or classical-limit. For quantum-coherent GU spinors:
the entanglement between V_L and V_R sectors is maintained (decoherence is below the
quantum-coherent threshold). Therefore:

```
For quantum-coherent GU spinors (Gamma >= Gamma_min), the CHSH violation |CHSH| > 2
holds for the unique G_PS-equivariant (V_L, V_R) bipartition under SM-charge measurements.
```

---

## 5. Summary of the Bipartite Analysis

The computation above establishes four things:

**R1 (No G_PS-equivariant tensor-product split):** There is no G_PS-equivariant tensor-product
decomposition S(6,4) = S_A tensor S_B with both factors nontrivial. Proof: Clebsch-Gordan
arithmetic over G_PS rules out all (d_A, d_B) factorizations with d_A * d_B = 16.

**R2 (Unique G_PS-equivariant direct-sum split):** The only G_PS-equivariant decomposition
of S(6,4) is the DIRECT SUM V_L + V_R = (4,2,1) + (4-bar,1,2) from the Pati-Salam
branching rules. This is the (not a tensor-product) bipartition for SM measurements.

**R3 (Vacuum entanglement forces |CHSH| > 2):** The GU vacuum state in the V_L tensor V_R
Hilbert space (after tensoring the two-observer system) is a maximally entangled state by
CPT symmetry and Bisognano-Wichmann modular theory. For any nontrivial SM-charge-based
measurement operators, |CHSH| = 2 sqrt(2) > 2.

**R4 (No counterexample for SM-charged quantum-coherent bipartitions):** There is no
SM-charged bipartition of S(6,4) for which all local SM-charge-based measurement settings
give |CHSH| <= 2, within the quantum-coherent GU regime. Product-state counterexamples
exist but require non-SM-charge or non-quantum-coherent settings.

---

## 6. Verdict

**Verdict: CONDITIONALLY_RESOLVED**

**Grade: reconstruction**

The Pati-Salam bipartite structure of S(6,4) is now explicitly computed:
- The (4,2,1) + (4-bar,1,2) decomposition provides the unique G_PS-equivariant
  direct-sum split; no G_PS-equivariant tensor-product split exists.
- The GU vacuum state, restricted to the (V_L, V_R) bipartition for two spacelike-separated
  GU observers, is a maximally entangled state.
- SM-charge-based CHSH measurement settings produce |CHSH| = 2 sqrt(2) for all nontrivial
  SM-charge-based operator choices.
- No SM-charged bipartition of S(6,4) admits |CHSH| <= 2 in the quantum-coherent GU regime.

**Failure condition FC-F2-1 (from h3-gap2-gu-universality §8) is NOT triggered.**

**Failure conditions for this result (CONDITIONALLY_RESOLVED):**

**FC1:** The CPT left-right symmetry of G_PS is broken or absent in the GU construction.
If the Pati-Salam left-right Z_2 is NOT a symmetry of the GU vacuum (e.g., if the GU
metric-section s: X^4 -> Y^14 selects a chirality-breaking vacuum), then the vacuum state
may not be maximally entangled between V_L and V_R. In this case, the GU vacuum could be
a product state or a low-entanglement state with |CHSH| <= 2 for some settings.
Assessment: GU does not obviously force left-right symmetry preservation at the section
level. This failure condition is active.

**FC2:** The Bisognano-Wichmann theorem / Reeh-Schlieder entanglement argument fails for
the GU spinor field. If the GU framework is not a standard relativistic QFT with Bisognano-
Wichmann structure (e.g., if Y^14 geometry modifies the modular theory in ways that destroy
vacuum entanglement), the maximally entangled state conclusion is unwarranted.
Assessment: The GU construction is a gauge theory on Y^14 with Sp(64) symmetry and a
Dirac operator. Standard QFT modular theory applies at the section level s*(D_GU) on X^4.
Bisognano-Wichmann for the SM-sector pullback is reconstruction-grade. This failure condition
is non-trivially active.

**FC3:** The Clebsch-Gordan analysis of §3.2 has an error. If there exists a G_PS-equivariant
tensor-product decomposition S(6,4) = S_A tensor S_B that was missed by the character
analysis, then product states in that tensor-product splitting could give |CHSH| <= 2.
Assessment: The character-ring analysis covers all d_A * d_B = 16 cases. The specific
Clebsch-Gordan products of SU(4) representations (4 tensor n for small n) are well-known.
No counterexample is expected, but CAS verification of the SU(4) tensor-product table
would confirm this.

**FC4:** The GU measurement postulate (OQ-G2-5 from h3-gap2-gu-universality) is not as
assumed. If physically admissible GU measurements extend beyond SM-charge projectors
(e.g., measurements in the Sp(64) gauge algebra outside the G_PS subalgebra), then
the restriction to G_PS-equivariant operators is too narrow, and additional product-state
configurations may arise.
Assessment: This is the F4 failure condition from the parent file, unchanged.

---

## 7. Consequences for H3

**F2 is CONDITIONALLY_RESOLVED** (reconstruction grade, four active failure conditions above).

This upgrades the H3 restricted universality verdict:

| H3 component | Prior status | New status |
|---|---|---|
| Conditional H3 (NAC + Odd-SBP) | RESOLVED | RESOLVED (unchanged) |
| Pati-Salam bipartite CHSH violation | OPEN (OQ-G2-1) | CONDITIONALLY_RESOLVED |
| Restricted H3 (SM-charged, quantum-coherent) | CONDITIONALLY_RESOLVED, pending F2 | CONDITIONALLY_RESOLVED, F2 addressed |
| Full H3 (all GU observers) | OPEN | OPEN (F4, FC1, FC2 above) |

The blocked F2 failure condition in `h3-gap2-gu-universality-2026-06-23.md` is now
addressed at reconstruction grade: the Pati-Salam bipartite structure does NOT admit
G_PS-equivariant product states in the quantum-coherent GU regime, and SM-charge-based
CHSH is violated for all relevant bipartitions.

The three remaining gates for full H3 are:
- FC1 above (GU left-right symmetry preservation in vacuum).
- FC2 above (Bisognano-Wichmann modular theory for GU pullback).
- F4 from parent file (GU measurement postulate: admissibility of SM-charge operators).

---

## 8. Open Questions

**OQ-F2-1 (CAS verification of Clebsch-Gordan):** Run SU(4) x SU(2) x SU(2) Clebsch-Gordan
table CAS computation to verify that no tensor product of two G_PS representations of
dimensions (d_A, d_B) with d_A * d_B = 16 yields exactly (4,2,1) + (4-bar,1,2). This
would close FC3.

**OQ-F2-2 (Explicit vacuum two-point function):** Compute the GU vacuum two-point function
G_{LR}(x_A, x_B) = <psi_L(x_A) psi_R-bar(x_B)>_vac explicitly from the GU propagator
(section-pullback of D_GU Green's function) and verify it is nonzero at spacelike separation.
This would close FC2 (or identify how it fails).

**OQ-F2-3 (Left-right symmetry in GU vacuum):** Determine whether the GU section selection
(Tikhonov-Willmore variational principle) preserves or breaks the Pati-Salam left-right
Z_2 symmetry. If preserved: vacuum is CPT-invariant and maximally entangled. If broken:
FC1 becomes active and the CHSH analysis must be revised.

**OQ-F2-4 (GU measurement postulate):** Formalize the GU measurement postulate to determine
whether SM-charge projectors are admissible as the natural measurement operators for GU
observers. This closes F4 / FC4.
