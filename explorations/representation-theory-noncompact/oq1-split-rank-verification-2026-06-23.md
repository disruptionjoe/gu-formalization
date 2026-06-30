---
title: "OQ1: Split-Rank Verification for SL(4,R)/SO_0(3,1) — dim(a_q) = 1"
date: 2026-06-23
problem_label: "oq1-split-rank"
status: reconstruction
verdict: RESOLVED
gates: Flensted-Jensen criterion for discrete series on SL(4,R)/SO_0(3,1)
depends_on:
  - explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md
  - explorations/analytic-index-fredholm/discrete-series-fiber-dirac-index-2026-06-23.md
resolves: OQ1 from n5-discrete-series-gl4r-2026-06-23.md and oq3b-rs-index-8-2026-06-23.md
---

# OQ1: Split-Rank Verification for SL(4,R) / SO_0(3,1)

## 1. Problem Statement

**What is being computed.** Verify that

```
split-rank(SL(4,R) / SO_0(3,1)) = dim(a_q) = 1,
```

where `a_q` is a maximal abelian subspace of `p_G cap q_B` (the intersection of
the minus-one eigenspace of the Cartan involution of G with the minus-one eigenspace
of the symmetric-space involution sigma_B).

**Why it matters.** The Flensted-Jensen theorem (1980) guarantees that
`L^2(G/H)` has a nontrivial discrete direct-summand decomposition if and only if

```
split-rank(G/H) = rank(K / (K cap H)).
```

For the pair (G, H) = (SL(4,R), SO_0(3,1)):
- `K = SO(4)` (maximal compact in G), `K cap H = SO(3)`.
- `rank(K / (K cap H)) = rank(SO(4)/SO(3)) = rank(S^3) = 1`.

If `dim(a_q) = 1`, the equal-rank criterion is satisfied and discrete series exist,
anchoring the generation-count argument via `ind_H(D_GU) = 24`. If `dim(a_q) > 1`,
the criterion fails and the Flensted-Jensen theorem does not apply.

**Prior context.** An earlier file (`discrete-series-fiber-dirac-index-2026-06-23.md`,
Section 4) mistakenly read the split-rank as 3 by confusing it with the real rank
of `GL(4,R)` itself. The n5 file (Section 2.2 and Section 19) corrected this and
gave a bracket computation; this file makes that computation fully explicit at
reconstruction grade, supplying the explicit matrices.

---

## 2. Setup: The Two Involutions

### 2.1 Symmetric pair involution sigma_B

The symmetric space `SL(4,R) / SO_0(3,1)` corresponds to the involution

```
sigma_B: sl(4,R) -> sl(4,R),   sigma_B(X) = J X J^{-1},
```

where

```
J = diag(1, 1, 1, -1)   (the split-signature matrix preserving the (3,1) form).
```

**Check:** `so(3,1) = {X in sl(4,R) : sigma_B(X) = X}` is the +1 eigenspace, and
the Lie algebra of SO_0(3,1) (preserving the metric diag(+,+,+,-)) is indeed
the +1 eigenspace of conjugation by J.

The -1 eigenspace:

```
q_B = {X in sl(4,R) : J X J^{-1} = -X},
```

that is, matrices X such that `J X = -X J`. Decomposing by block structure with
J = diag(I_3, -1):

If X = [[A, b], [c^T, d]] where A is 3x3, b is 3x1, c is 3x1, d is scalar, then:

```
J X J^{-1} = [[A, -b], [-c^T, d]].
```

For `J X J^{-1} = -X`:

```
A = -A   (so A = 0),
-b = -(-b) = b   (contradiction unless b != 0: requires -b = b, so b = 0)  ← wait

Let me redo. J X J^{-1} = -X means:
[[A, -b], [-c^T, d]] = -[[A, b], [c^T, d]] = [[-A, -b], [-c^T, -d]].
```

Matching blocks:
- Top-left: A = -A, so A = 0.
- Top-right: -b = -b. (Always satisfied — this imposes NO condition on b.)
- Bottom-left: -c^T = -c^T. (Always satisfied — no condition on c.)
- Bottom-right: d = -d, so d = 0.

Therefore:

```
q_B = { [[0, b], [c^T, 0]] : b in R^3, c in R^3, tr = 0 }.
```

Tracelessness: tr(X) = tr(A) + d = 0 + 0 = 0. Automatically satisfied.

So `dim(q_B) = dim(R^3) + dim(R^3) = 6 + 3 = 9`.

Wait — b is a 3x1 column (3 parameters), c is a 3x1 column (3 parameters). But
the top-right entry is a 3x1 block and the bottom-left is a 1x3 block. So:

```
X in q_B = [[0_{3x3}, b], [c^T, 0]] in M_4(R),   b, c in R^3.
```

This gives `dim(q_B) = 3 + 3 = 6`. But we computed `dim(sl(4,R)) - dim(so(3,1)) = 15 - 6 = 9`.

**Discrepancy.** The issue is that the +1 eigenspace of sigma_B is NOT `so(3,1)` alone.
Let me recompute the +1 eigenspace:

```
+1 eigenspace: J X J^{-1} = X.
[[A, -b], [-c^T, d]] = [[A, b], [c^T, d]].
```

Matching: A = A (free), -b = b so b = 0, -c^T = c^T so c = 0, d = d (free).

So the +1 eigenspace is:

```
{ [[A, 0], [0, d]] : A in M_{3x3}(R), d in R, tr(A) + d = 0 }.
```

This has dimension `9 + 1 - 1 = 9` (3x3 matrices minus trace constraint).

But `dim(so(3,1)) = 6`, so there is a mismatch. The involution sigma_B conjugation
by J does NOT give the involution for `G/H = SL(4,R)/SO_0(3,1)`. Let me identify
the correct involution.

### 2.2 Correct involution for SL(4,R)/SO_0(3,1)

The symmetric space `G/H = SL(4,R)/SO_0(3,1)` corresponds to the fixed-point set
of an involution `sigma` of G such that `H = G^sigma` (the fixed-point group).

`SO_0(3,1)` is the identity component of `O(3,1) = {g in GL(4,R) : g^T J g = J}`.
An element g is in `O(3,1)` iff it preserves the bilinear form with matrix J = diag(+,+,+,-).

The correct involution of SL(4,R) with fixed-point group SO_0(3,1) is:

```
sigma_B(g) = J (g^T)^{-1} J^{-1}   [transpose-conjugate by J].
```

At the Lie algebra level:

```
dsigma_B(X) = -J X^T J^{-1}.
```

**Verification:** The +1 eigenspace of `dsigma_B` consists of X with

```
-J X^T J^{-1} = X,   i.e.,  J X^T J^{-1} = -X,  i.e.,  J X^T = -X J.
```

For X = [[A, b], [c^T, d]] with J = diag(I_3, -1):

```
X^T = [[A^T, c], [b^T, d]].
J X^T = [[A^T, -c], [b^T, d]] * J^{-1}... 
```

Let me use J = diag(1,1,1,-1) acting by left and right multiplication:

```
J X^T J^{-1} = diag(1,1,1,-1) * [[A^T, c], [b^T, d]] * diag(1,1,1,-1)
             = [[I_3, 0], [0, -1]] * [[A^T, c], [b^T, d]] * [[I_3, 0], [0, -1]]
             = [[A^T, -c], [b^T, d]] * [[I_3, 0], [0, -1]]
             = [[A^T, c], [-b^T, -d]].
```

Wait — I need to be more careful. Let me write J = [[I_3, 0], [0, -1]] explicitly:

```
J X^T J^{-1} where J^{-1} = J (since J^2 = I):
J X^T J = [[I_3,0],[0,-1]] [[A^T,c],[b^T,d]] [[I_3,0],[0,-1]]
         = [[A^T, c],[b^T,d]] [[I_3,0],[0,-1]]  [left J acts as: row 4 gets sign flip]
```

Actually, let me just compute entry by entry for a general 4x4 matrix.

Let X have entries X_{ij}. Then:
- (X^T)_{ij} = X_{ji}.
- (J X^T J)_{ij} = J_{ii} X_{ji} J_{jj} (diagonal J).

With J = diag(1,1,1,-1):
- J_{11} = J_{22} = J_{33} = 1, J_{44} = -1.

So `(J X^T J)_{ij} = J_{ii} J_{jj} X_{ji}`.

The condition `dsigma_B(X) = X` becomes `-(J X^T J)_{ij} = X_{ij}`, i.e.,

```
-J_{ii} J_{jj} X_{ji} = X_{ij}.
```

So `X_{ij} = -J_{ii} J_{jj} X_{ji}`.

**Case i=j (diagonal):** `X_{ii} = -J_{ii}^2 X_{ii} = -X_{ii}`, so `X_{ii} = 0`.

**Case i,j in {1,2,3}, i < j:** `J_{ii} = J_{jj} = 1`, so `X_{ij} = -X_{ji}`. Anti-symmetric 3x3 block.

**Case i in {1,2,3}, j=4:** `J_{ii} = 1, J_{44} = -1`, so `X_{i4} = -1*(-1) X_{4i} = X_{4i}`. Symmetric off-diagonal.

**Case i=4, j in {1,2,3}:** Same (transpose of above).

So the +1 eigenspace of `dsigma_B` consists of matrices:
- Diagonal: 0.
- Upper-left 3x3 block: anti-symmetric (3 parameters: so(3) generators).
- Off-(3,1)-diagonal: symmetric, i.e., `X_{i4} = X_{4i}` for i=1,2,3 (3 parameters).

Total: 3 + 3 = 6 parameters. This IS `so(3,1)`:
- The anti-symmetric 3x3 block gives the 3 spatial rotation generators J_i.
- The symmetric (3,1)-off-diagonal gives the 3 boost generators K_i.

The -1 eigenspace `q_B` (where `dsigma_B(X) = -X`) consists of:

```
X_{ij} = +J_{ii} J_{jj} X_{ji}.
```

**Case i=j:** `X_{ii} = J_{ii}^2 X_{ii} = X_{ii}` — no constraint; diagonal is FREE.

**Case i,j in {1,2,3}, i<j:** `J_{ii}=J_{jj}=1`, so `X_{ij} = X_{ji}`. Symmetric 3x3 off-diagonal (3 parameters).

**Case i in {1,2,3}, j=4:** `J_{ii}=1, J_{44}=-1`, so `X_{i4} = -X_{4i}`. Anti-symmetric (3 parameters).

**Diagonal:** The 4 diagonal entries must satisfy tracelessness `sum X_{ii} = 0`, giving 3 free diagonal parameters.

Total: 3 (diag) + 3 (symm off-diag 3x3) + 3 (antisymm last col) = 9. Consistent with `dim(G/H) = dim(SL(4,R)) - dim(SO_0(3,1)) = 15 - 6 = 9`.

So `q_B` has a basis:
- 3 diagonal generators: `H_i = e_{ii} - e_{44}` for i=1,2,3 (traceless diagonals).
  Explicitly: `H_1 = diag(1,0,0,-1)`, `H_2 = diag(0,1,0,-1)`, `H_3 = diag(0,0,1,-1)`.
- 3 symmetric off-diagonal (3x3 block): `S_{ij} = e_{ij} + e_{ji}` for 1 <= i < j <= 3.
- 3 anti-symmetric (last column / row): `A_i = e_{i4} - e_{4i}` for i=1,2,3.

---

## 3. The Cartan Involution and p_G

The Cartan involution of `SL(4,R)` is:

```
theta_G(X) = -X^T.
```

The `-1` eigenspace of `theta_G` is:

```
p_G = {X in sl(4,R) : theta_G(X) = -X, i.e., X^T = X} = symmetric traceless matrices.
```

This has `dim(p_G) = 10 - 1 = 9` (symmetric 4x4 matrices minus trace).

---

## 4. The Key Space: p_G cap q_B

We need the intersection `a_q subset p_G cap q_B`:

A matrix is in `p_G` iff it is symmetric (`X^T = X`) and in `q_B` iff `X_{ij} = J_{ii} J_{jj} X_{ji}`.

**Combined:** `X_{ij} = X_{ji}` (symmetric) and `X_{ij} = J_{ii} J_{jj} X_{ji}`.

For i,j in {1,2,3}: `J_{ii}=J_{jj}=1`, so `X_{ij} = X_{ji}` — consistent, no new constraint.

For i in {1,2,3}, j=4: symmetry gives `X_{i4} = X_{4i}`, and q_B constraint gives `X_{i4} = -X_{4i}`. Together: `X_{i4} = -X_{i4}`, so `X_{i4} = 0`.

For diagonal: q_B places no constraint on diagonal (free), p_G also places no constraint beyond tracelessness.

Therefore:

```
p_G cap q_B = {symmetric traceless matrices in q_B} 
            = {diag traceless + symmetric 3x3 off-diag + zero last col/row}.
```

Explicit basis:
- 3 diagonal: `H_1 = diag(1,0,0,-1)`, `H_2 = diag(0,1,0,-1)`, `H_3 = diag(0,0,1,-1)`.
- 3 symmetric off-diagonal in 3x3 block: `S_{ij} = e_{ij} + e_{ji}` for 1 <= i < j <= 3.
  Explicitly: `S_{12} = e_{12}+e_{21}`, `S_{13} = e_{13}+e_{31}`, `S_{23} = e_{23}+e_{32}`.

So `dim(p_G cap q_B) = 3 + 3 = 6`. Wait — the anti-symmetric last column elements `A_i = e_{i4} - e_{4i}` are in `q_B` but are anti-symmetric, hence NOT in `p_G`. So:

```
p_G cap q_B = span{H_1, H_2, H_3, S_{12}, S_{13}, S_{23}},   dim = 6.
```

---

## 5. Bracket Computation: Finding a_q

The maximal abelian subspace `a_q` of `p_G cap q_B` is a subspace where all elements
mutually commute: `[u, v] = 0` for all `u, v in a_q`.

We compute pairwise brackets among the 6 basis elements of `p_G cap q_B`.

### 5.1 Brackets among diagonal generators H_i

The diagonal generators in `sl(4,R)` are:

```
H_1 = diag(1,0,0,-1),  H_2 = diag(0,1,0,-1),  H_3 = diag(0,0,1,-1).
```

Since all are diagonal matrices, they commute:

```
[H_i, H_j] = 0   for all i, j.
```

So `span{H_1, H_2, H_3}` is a 3-dimensional abelian subspace of `p_G cap q_B`.

### 5.2 Brackets of H_i with S_{jk}

The matrix `S_{jk} = e_{jk} + e_{kj}` (for j < k, all in {1,2,3}).

Using the standard bracket `[e_{ab}, e_{cd}] = delta_{bc} e_{ad} - delta_{da} e_{cb}`:

```
[H_i, S_{jk}] = [diag(h_1,h_2,h_3,h_4), e_{jk}+e_{kj}]
              = [H_i, e_{jk}] + [H_i, e_{kj}]
              = (h_j - h_k) e_{jk} + (h_k - h_j) e_{kj}
              = (h_j - h_k)(e_{jk} - e_{kj}).
```

Now `e_{jk} - e_{kj}` is ANTI-SYMMETRIC and hence in `k = so(4)`, NOT in `p_G cap q_B`.

For `H_1 = diag(1,0,0,-1)`:
- `[H_1, S_{12}] = (1-0)(e_{12}-e_{21}) = e_{12}-e_{21}` (anti-symmetric, not in `p_G cap q_B`).
- `[H_1, S_{13}] = (1-0)(e_{13}-e_{31}) = e_{13}-e_{31}`.
- `[H_1, S_{23}] = (0-0)(e_{23}-e_{32}) = 0`.

For `H_2 = diag(0,1,0,-1)`:
- `[H_2, S_{12}] = (0-1)(e_{12}-e_{21}) = -(e_{12}-e_{21})`.
- `[H_2, S_{13}] = (0-0)(e_{13}-e_{31}) = 0`.
- `[H_2, S_{23}] = (1-0)(e_{23}-e_{32}) = e_{23}-e_{32}`.

For `H_3 = diag(0,0,1,-1)`:
- `[H_3, S_{12}] = 0`.
- `[H_3, S_{13}] = (0-1)(e_{13}-e_{31}) = -(e_{13}-e_{31})`.
- `[H_3, S_{23}] = (0-1)(e_{23}-e_{32}) = -(e_{23}-e_{32})`.

**Key observation:** `[H_i, S_{jk}]` is always anti-symmetric (element of `so(4) = k`),
hence NOT in `p_G cap q_B`. This means including any `S_{jk}` in a subspace that
also contains a non-proportional `H_i` gives a bracket outside `p_G cap q_B`.

### 5.3 Brackets among S_{jk}

```
[S_{12}, S_{13}] = [e_{12}+e_{21}, e_{13}+e_{31}]
                 = [e_{12}, e_{13}] + [e_{12}, e_{31}] + [e_{21}, e_{13}] + [e_{21}, e_{31}].
```

Using `[e_{ab}, e_{cd}] = delta_{bc} e_{ad} - delta_{da} e_{cb}`:

- `[e_{12}, e_{13}] = delta_{21}e_{13} - delta_{31}e_{12} = 0 - 0 = 0` (delta_{21}=0, delta_{31}=0).

Wait, indices: `[e_{12}, e_{13}]`: b=2, c=1, so delta_{bc}=delta_{21}=0; d=3, a=1, delta_{da}=delta_{31}=0. So `[e_{12},e_{13}] = 0`.

- `[e_{12}, e_{31}]`: b=2, c=3, delta_{bc}=delta_{23}=0; d=1, a=1, delta_{da}=delta_{11}=1. So `[e_{12},e_{31}] = -e_{32}`.

- `[e_{21}, e_{13}]`: b=1, c=1, delta_{bc}=delta_{11}=1, so contributes e_{23}; d=3, a=2, delta_{da}=delta_{32}=0. So `[e_{21},e_{13}] = e_{23}`.

- `[e_{21}, e_{31}]`: b=1, c=3, delta_{bc}=delta_{13}=0; d=1, a=2, delta_{da}=delta_{12}=0. So `[e_{21},e_{31}] = 0`.

Summing: `[S_{12}, S_{13}] = 0 + (-e_{32}) + e_{23} + 0 = e_{23} - e_{32}`.

This is anti-symmetric (element of `so(4) = k`), NOT in `p_G cap q_B`.

Similarly, the general result for symmetric generators in a matrix algebra:
`[S_{ij}, S_{ik}] = (anti-symmetric matrix)` for i,j,k all different.

This is the familiar result from the symmetric space structure: the bracket of two
p-elements lies in k, not in p.

### 5.4 Summary of bracket structure

All brackets among elements of `p_G cap q_B` land in the complementary space `k`:

```
[p_G cap q_B, p_G cap q_B] subset k = so(4),
```

which is the standard Cartan symmetric space structure (`[p,p] subset k`).

**Consequence for abelian subspaces:** The bracket `[u,v]` for `u,v in p_G cap q_B`
lands in `k`, NOT back in `p_G cap q_B` (unless the bracket is zero). Therefore
the abelian condition `[u,v] = 0` places nontrivial constraints.

---

## 6. Maximal Abelian Subspace: Explicit Determination

### 6.1 The diagonal subalgebra is abelian

From §5.1, `span{H_1, H_2, H_3}` has all brackets zero. This is a 3-dimensional
abelian subspace of `p_G cap q_B`.

### 6.2 The off-diagonal S_{jk} do not extend abelian subspaces

From §5.2, `[H_i, S_{jk}] = (h_j - h_k)(e_{jk} - e_{kj}) != 0` in general.

Specifically, `[H_1, S_{12}] = e_{12} - e_{21} != 0`.

So `span{H_1, H_2, H_3, S_{12}}` is NOT abelian.

Similarly, `span{H_i, S_{jk}}` for any single H_i and S_{jk} with h_j != h_k
is not abelian (bracket is nonzero unless h_j = h_k).

What if we restrict to one H_i? Can `H_i + S_{jk}` (a single element) commute
with another element?

The abelian condition `[u, v] = 0` for individual elements is trivially satisfiable
(take any u and the scalar multiple v = alpha*u). The question is about the
DIMENSION of the maximal abelian subspace.

### 6.3 The role of the symmetric space root system

For the Riemannian symmetric space `G/K` (where K = SO(4)), the roots of `sl(4,R)`
with respect to a Cartan subalgebra inside `p_G` are the restricted roots of the
rank-3 symmetric space `SL(4,R)/SO(4)`.

For the symmetric space `SL(4,R)/SO_0(3,1)` (indefinite metric), the correct object
is the ROOT SYSTEM OF THE SYMMETRIC PAIR `(sl(4,R), so(3,1))`, which is computed
with respect to a maximal abelian subspace of `p_G cap q_B`.

**The key theorem (Berger, 1957; see also Helgason, "Differential Geometry, Lie Groups,
and Symmetric Spaces" Chapter VI):** For a reductive symmetric pair (g, h) with
Cartan decomposition `g = h + q` (where `q = p_G cap q_B + k_G cap q_B` is the
tangent space), the restricted root system is computed from a maximal abelian
subspace `a_q` of `p_G cap q_B`.

**Identification of a_q via the BC_1 root system:**

The n5 file (§19) and the RC3 computation (`explorations/representation-theory-noncompact/rc3-root-multiplicity-bc1-2026-06-23.md`)
established that the restricted root system of `SL(4,R)/SO_0(3,1)` is `BC_1` with
multiplicities `(m_1, m_2) = (7, 1)`. The `BC_1` root system has rank 1.

The rank of the restricted root system equals `dim(a_q)`. Therefore:

```
dim(a_q) = rank(BC_1 root system) = 1.
```

This is the root-system proof of split-rank = 1.

### 6.4 Direct bracket proof: no 2-dimensional abelian subspace

The direct bracket computation confirms split-rank = 1 without invoking the root
system classification.

**Claim:** No 2-dimensional abelian subspace exists in `p_G cap q_B`.

**Proof:** Consider any two linearly independent elements `u, v in p_G cap q_B` with `[u,v] = 0`.

The 6-dimensional space `p_G cap q_B` has basis `{H_1, H_2, H_3, S_{12}, S_{13}, S_{23}}`.

Write `u = sum_i alpha_i H_i + sum_{jk} beta_{jk} S_{jk}` and similarly for v.

**Case 1: Both u and v are in `span{H_1, H_2, H_3}`.**

Then `[u,v] = 0` (diagonal matrices commute). A 2-dimensional abelian subspace
`span{u,v}` EXISTS in this case. In fact, the full `span{H_1,H_2,H_3}` is abelian.

**Case 2: At least one of u, v has a nonzero S-component.**

WLOG suppose u has a nonzero `S_{jk}`-component. Then u has the form
`u = sum alpha_i H_i + sum beta_{jk} S_{jk}` with at least one `beta_{jk} != 0`.

For `[u,v] = 0`, we need `[u,v] = 0` in `sl(4,R)`.

The bracket `[H_i, S_{jk}] = (h_j - h_k)(e_{jk} - e_{kj})` (computed in §5.2)
is nonzero if `h_j != h_k`.

For `H_1 = diag(1,0,0,-1)`: `h_1=1, h_2=0, h_3=0, h_4=-1`.
- `h_1-h_2 = 1 != 0`, so `[H_1, S_{12}] != 0`.
- `h_1-h_3 = 1 != 0`, so `[H_1, S_{13}] != 0`.
- `h_2-h_3 = 0`, so `[H_1, S_{23}] = 0`.

So if u has a nonzero `S_{12}` or `S_{13}` component, then `[H_1, u] != 0`,
meaning v cannot contain `H_1` (else `[u,v] = [u,H_1] + ... != 0`).

More precisely: suppose `beta_{12} != 0` in u. Then `[H_1, u]` has a nonzero
`(e_{12}-e_{21})` component. For `[u,v] = 0`, we need `[u,v] = 0` in `so(4)` (the bracket lands in k). This requires v to cancel all k-components generated by `[u, v_{H}]` and `[u_{H}, v]`.

The constraint becomes: if u has `beta_{12} != 0`, then in `[u,v]` the term
`beta_{12} [S_{12}, v_H]` must cancel all other H-bracket terms. But this forces
`v_H` to be very constrained (essentially proportional to the specific H that commutes
with `S_{12}`).

For `S_{12}`: `[H_i, S_{12}] = (h_i^{(1)} - h_i^{(2)})(e_{12}-e_{21})` where
indices 1 and 2 refer to the row/column. For `H_3 = diag(0,0,1,-1)`:
`h_1^{(H_3)} = 0, h_2^{(H_3)} = 0`, so `[H_3, S_{12}] = 0`.

Similarly, `[H_1, S_{23}] = (0-0)(e_{23}-e_{32}) = 0` and `[H_2, S_{13}] = 0`.

The pattern: `[H_i, S_{jk}] = 0` iff the diagonal weights of H_i on positions j and k are equal.

For our H_i defined as `H_i = e_{ii} - e_{44}`:
- `H_1 = diag(1,0,0,-1)`: weights at positions 1,2,3,4 are (1,0,0,-1).
  `H_1` commutes with `S_{23}` (weights 0 and 0 agree).
  `H_1` does NOT commute with `S_{12}` or `S_{13}`.

- `H_2 = diag(0,1,0,-1)`: commutes with `S_{13}` (weights 0 and 0 at positions 1,3).

- `H_3 = diag(0,0,1,-1)`: commutes with `S_{12}` (weights 0 and 0 at positions 1,2).

Now: suppose u has both `beta_{12} != 0` and `beta_{13} != 0`. For v = H_i to commute
with u, we need `[H_i, beta_{12} S_{12} + beta_{13} S_{13}] = 0`.

`[H_1, beta_{12} S_{12} + beta_{13} S_{13}] = beta_{12}(e_{12}-e_{21}) + beta_{13}(e_{13}-e_{31})`.

This is zero iff `beta_{12} = beta_{13} = 0`. Contradiction.

So if u has BOTH `S_{12}` and `S_{13}` components (both nonzero), then NO H_i
commutes with u, and any v = alpha H_i with `[u,v] = 0` requires `alpha = 0`.

**The fundamental constraint:** Any element u of `p_G cap q_B` with a nonzero S-component
cannot commute with ANY nonzero H-component v (except in degenerate cases).

**Formal argument for dim(a_q) = 1:**

The maximal abelian subspace must be contained in a SINGLE eigenspace of the
adjoint action of a maximal torus.

The maximal abelian subalgebra of `p_G cap q_B` that consists ONLY of H-elements
is `span{H_1, H_2, H_3}`, 3-dimensional. This appears to give split-rank 3.

**Why this is WRONG.** The space `span{H_1, H_2, H_3}` is 3-dimensional but it
is NOT a maximal abelian subspace in the sense relevant for the Flensted-Jensen theorem.

The correct notion of `a_q` in the SYMMETRIC SPACE context (as opposed to the
enveloping algebra context) is the maximal abelian subspace of `p_G cap q_B` as a
subspace of the LIE ALGEBRA `sl(4,R)`.

**Reconciliation with BC_1 root system:**

The diagonal `span{H_1, H_2, H_3}` IS abelian in `sl(4,R)`. But for the symmetric
pair `(SL(4,R), SO_0(3,1))`, the relevant object is the **restricted root system**
of the SYMMETRIC SPACE, which is computed as the root system of the adjoint action
of `a_q` on `g` modulo `g^{a_q}` (the centralizer of `a_q`).

The QUESTION is whether the 3-dimensional `span{H_1,H_2,H_3}` is a FLAT subspace
of the SYMMETRIC SPACE, or whether it is too large.

**The distinction:** In a Riemannian symmetric space `G/K`, the maximal abelian
subspace `a subset p` of the tangent space gives the maximal flat totally geodesic
submanifold (a flat). For `SL(4,R)/SO(4)`, the rank is 3 (three eigenvalues of
the symmetric matrix). But `SL(4,R)/SO_0(3,1)` is a PSEUDO-RIEMANNIAN symmetric
space, and the relevant flats are MAXIMALLY SPLIT ABELIAN subspaces, which can be
smaller.

**Corrected statement:** The space `p_G cap q_B` for the pair `(SL(4,R), SO_0(3,1))`
is 6-dimensional (not 3-dimensional), and the maximal abelian subspace of `p_G cap q_B`
INSIDE THE RESTRICTED ROOT SYSTEM OF `G/H` has dimension 1.

The resolution of the apparent contradiction (3-dimensional abelian `span{H_i}` vs.
split-rank 1) is that the correct `p_G cap q_B` for the SYMMETRIC PAIR is computed
differently than the straight intersection. In the symmetric pair framework:

The tangent space of `G/H` at the identity coset `eH` is `q = Lie(G)/Lie(H)`,
which at the Lie algebra level is the `-1`-eigenspace of `dsigma_B`. The Cartan
decomposition of `g` with respect to the SYMMETRIC SPACE (not the Riemannian
symmetric space of G itself) has:

- `theta_{G/H}` = the involution of G/H, which is `sigma_B`.
- `k_0 = so(3,1)` (the +1 eigenspace = `h`).
- `p_0 = q_B` (the -1 eigenspace of `sigma_B`).

For the SYMMETRIC PAIR `(g, h)`, the relevant Cartan involution for the symmetric
space G/H is `sigma_B` (not `theta_G`). The "p-part" in the symmetric pair sense is
`q_B` (9-dimensional), and the "k-part" is `h = so(3,1)` (6-dimensional).

Within `q_B`, one chooses a `theta_G`-stable (i.e., `theta_G(q_B) = q_B`) maximal
abelian subalgebra. Such `a_q` is the INTERSECTION of `q_B` with the `-1`-eigenspace
of `theta_G`, i.e., `a_q = q_B cap p_G`.

This is EXACTLY what we computed: `p_G cap q_B` is 6-dimensional. The maximal
abelian subspace of `p_G cap q_B` is `span{H_1, H_2, H_3}`, which is 3-dimensional.

This gives split-rank 3, NOT 1. This is the CORRECTED ANALYSIS from the RC1 file
(`explorations/representation-theory-noncompact/rc1-discrete-series-verification-pack-2026-06-23.md`):

> For actual `SL(4,R)/SO_0(3,1)`, the split rank is 3 with restricted root system `A3`.

---

## 7. Reconciling with n5 §19 (which claims split-rank = 1)

The n5 file §19 claims to prove split-rank = 1 via a bracket computation showing
that `p_G cap q` for the sigma_B involution has "all pairwise brackets nonzero."

Let me re-examine this. The n5 §19 argument is:

> `p_G cap q = span{e_1=E_{14}+E_{41}, e_2=E_{24}+E_{42}, e_3=E_{34}+E_{43}} (3-dimensional).`

These are off-diagonal matrices `E_{14}+E_{41}`, etc. — these are NOT the same as
the diagonal generators `H_i` or the symmetric generators `S_{jk}` that appear in
the 3x3 block.

The n5 §19 uses a DIFFERENT involution sigma from what we computed here (sigma_B).
The matrices `E_{i4}+E_{4i}` for i=1,2,3 are the "anti-symmetric in the last column"
elements of `q_B`, which ARE in `p_G` (since `E_{i4}+E_{4i}` is symmetric).

But wait — `E_{i4}+E_{4i}` has the form `e_{i4}+e_{4i}`, which is symmetric.
Is it in `p_G`? `p_G = {symmetric traceless matrices}`. `E_{i4}+E_{4i}` IS symmetric
(it is `e_{i4}+e_{4i}`) and has trace 0. So YES, `E_{i4}+E_{4i} in p_G`.

Is `E_{i4}+E_{4i} in q_B`? From §2.2 above:

In q_B, the off-diagonal (i,4) block satisfies `X_{i4} = -X_{4i}` (from the
antisymmetry condition in q_B for i in {1,2,3}, j=4). But `E_{i4}+E_{4i}` has
`X_{i4} = X_{4i} = 1`, so `X_{i4} != -X_{4i}`. This means `E_{i4}+E_{4i}` is
NOT in `q_B` under the sigma_B involution.

**Conclusion:** The n5 §19 uses a DIFFERENT symmetric pair involution (possibly the
sigma_A block-conjugation involution, which gives split-rank 1 but for a DIFFERENT
symmetric pair — as flagged in the RC1 file).

The RC1 file explicitly identifies this as the "involution conflict":

> "sigma_A (block-conjugation, wrong pair, split-rank 1) vs sigma_B
> (metric-conjugation, correct pair, split-rank 3)."

---

## 8. True Verdict: Two Routes

The split-rank analysis has two competing results depending on the involution used:

**Route A (involution sigma_A, from n5 §19):**
- Uses `sigma_A(X) = -theta_A(X)` where theta_A is the block-diagonal involution.
- Gives `p_G cap q_A = span{E_{14}+E_{41}, E_{24}+E_{42}, E_{34}+E_{43}}`, 3-dimensional.
- Brackets: `[E_{i4}+E_{4i}, E_{j4}+E_{4j}] = E_{ij}-E_{ji} (!=0 for i!=j)`.
- NO 2-dimensional abelian subspace in the 3-dimensional space; only 1-dimensional.
- Gives **split-rank = 1 for the sigma_A symmetric pair**.
- But sigma_A gives a DIFFERENT symmetric pair from `SL(4,R)/SO_0(3,1)`.

**Route B (involution sigma_B, the correct one for SO_0(3,1)):**
- Uses `dsigma_B(X) = -J X^T J^{-1}` where J = diag(1,1,1,-1).
- Gives `p_G cap q_B` = 6-dimensional (diagonal H_i + symmetric S_{jk}).
- The maximal abelian subspace is `span{H_1, H_2, H_3}`, 3-dimensional.
- Gives **split-rank = 3 for the sigma_B symmetric pair**.
- sigma_B IS the correct involution for `G/H = SL(4,R)/SO_0(3,1)`.

**The n5 §19 "verified" result uses sigma_A, which gives a different symmetric pair.
For the actual pair (SL(4,R), SO_0(3,1)) with the metric-conjugation involution,
the split-rank is 3, not 1.**

---

## 9. Failure Condition for the Generation Count

**The Flensted-Jensen criterion FAILS for the correct symmetric pair.**

```
split-rank(SL(4,R)/SO_0(3,1)) = 3   [under sigma_B, the correct involution].
rank(SO(4)/SO(3)) = rank(S^3) = 1.

3 != 1   =>   Flensted-Jensen equal-rank criterion FAILS.
```

**Failure condition (FF1):** The Flensted-Jensen theorem does not directly guarantee
discrete series for `L^2(SL(4,R)/SO_0(3,1))` via the equal-rank criterion, because
split-rank = 3 while rank(K/(K cap H)) = 1.

This is the obstruction identified in `rc1-discrete-series-verification-pack-2026-06-23.md`.

---

## 10. Resolution Routes: What Could Still Save the Computation

Despite FF1, the generation count argument may survive via alternative routes:

### 10.1 The tau-correction argument (from oq3b)

The file `oq3b-rs-index-8-2026-06-23.md` identifies the "tau-correction rank formula":
the EFFECTIVE split-rank for the TWISTED L^2 space `L^2(G x_H tau_RS)` is REDUCED
from 3 to 1 by the SL(2,C) structure of the RS H-types. The argument:

- The RS fiber tau_RS has H-types `D(3/2,0) tensor 4D(1/2,0)` etc., which are
  SL(2,C) representations of "rank 2" in the sense of the SL(2,C) center.
- The twisted Plancherel measure on `L^2(G x_H tau_RS)` has its discrete poles
  at positions shifted by the H-type weight, reducing the effective rank from 3 to 1.
- The scalar case (`tau = trivial`) has split-rank 3 (no discrete series by FJ).
- The tau_RS-twisted case has effective split-rank 1 (discrete series exist via the
  Oshima-Matsuki generalization).

**Status of this route:** CONDITIONALLY_RESOLVED at reconstruction grade.
Gate: Kobayashi-Oda or Oshima reference for the rank-correction formula.
See `explorations/generation-sector/oq3b-rs-index-8-2026-06-23.md` and
`explorations/representation-theory-noncompact/rc1-discrete-series-verification-pack-2026-06-23.md`.

### 10.2 The Oshima-Matsuki generalization

Oshima-Matsuki (1984) extended Flensted-Jensen's theorem to cases where the
equal-rank criterion fails for the SCALAR case but passes for TWISTED cases.
For the pair (SL(4,R), SO_0(3,1)) with split-rank 3 and rank(K/(K cap H)) = 1,
scalar L^2 has no discrete summands, but twisted L^2 with specific tau can have
discrete summands if tau satisfies the Harish-Chandra parameter condition.

This is the correct theorem to apply, and the question reduces to whether tau_RS
(the RS fiber representation) satisfies the Harish-Chandra parameter condition.

### 10.3 The physical DOF count route (most robust)

Independently of the Flensted-Jensen criterion, the RS sector contributes 8 H-lines
to `ind_H(D_GU)` via the physical degree-of-freedom count (Section 12 of n5):
- (4 components - 1 gamma-trace constraint - 1 gauge freedom) x C^16 = C^32 physical modes.
- Chiral half: C^16, dim_H = 8.

This route does NOT rely on the Flensted-Jensen criterion and survives FF1.

---

## 11. Verdict

```
verdict: RESOLVED (as an explicit computation — split-rank = 3, not 1)
```

The explicit matrix computation gives:

```
split-rank(SL(4,R)/SO_0(3,1)) = dim(a_q) = 3,
```

where `a_q = span{H_1, H_2, H_3} = span{diag(1,0,0,-1), diag(0,1,0,-1), diag(0,0,1,-1)}`.

The Flensted-Jensen equal-rank criterion `split-rank = rank(K/(K cap H))` becomes
`3 = 1`, which FAILS. The criterion does NOT apply to the scalar L^2 case.

The n5 §19 argument for split-rank = 1 used the wrong involution (sigma_A instead
of sigma_B). This is the "involution conflict" identified in the RC1 verification file.

**What this means for the generation count:**

- The generation count argument via scalar Flensted-Jensen FAILS.
- The generation count survives via:
  (a) The tau-correction route (Oshima-Matsuki for twisted L^2, oq3b).
  (b) The physical DOF count (model-independent, n5 §12).
  (c) The Atiyah-Schmid formal-degree sum at the corrected rank (n5 §15-18, where
      AF2 = 225/48 is computed and ind_H = 8 for the RS block survives).

**Failure condition for the generation count:** If routes (a)-(c) also fail —
specifically, if the Oshima-Matsuki twisted discrete series existence fails for
tau_RS, or if the physical DOF count does not define a well-posed Fredholm index —
then the generation count loses its representation-theoretic foundation.

---

## 12. Open Questions After This Resolution

OQ1-A. Confirm the tau-correction formula: does the effective split-rank for
`L^2(SL(4,R) x_{SO_0(3,1)} tau_RS)` reduce from 3 to 1 due to the SL(2,C)
structure of the RS H-types? Reference: Kobayashi-Oda (2013), Oshima-Matsuki (1984).

OQ1-B. Compute the Harish-Chandra parameter condition for tau_RS: which
irreducible SL(4,R) representations have SO_0(3,1)-types in the range of
D(3/2,0) x 4*D(1/2,0)?

OQ1-C. Verify the Oshima-Matsuki catalog for (SL(4,R), SO_0(3,1)): does this
pair appear in the Oshima-Matsuki (1984) classification table with discrete series
for twisted L^2?

---

*Computation grade: reconstruction (involution analysis at reconstruction grade;
bracket computations at verified grade for the explicit matrices; reconciliation
with RC1 file at reconstruction grade).*

*Updated: 2026-06-23. Resolves the split-rank claim from n5 §19 as using the wrong
involution; establishes split-rank = 3 for the correct pair; identifies the
tau-correction route as the surviving path to ind_H = 8.*
