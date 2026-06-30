---
title: "Direct Clifford Algebra Proof of E(xi) Invertibility on Q=E_0+Q^{14D} via Cl(9,5)=M(64,H)"
date: 2026-06-23
problem_label: "vz-e-block-direct-clifford-invertibility"
status: reconstruction
verdict: RESOLVED
vz_evasion_upgrade: "CONDITIONALLY_EVADED -> EVADED (pending this file)"
---

# Direct Clifford Algebra Proof of E(xi) Invertibility on Q

## 1. Problem Statement

The VZ mixed-14D synthesis (`vz-14d-mixed-covectors-2026-06-23.md`) established:

- The kernel argument for `ker S_R^{14D}(xi) = 0` uses `E(xi)^{-1}` in Step 2.
- The circularity flag (VZ-01, 2026-06-23): `det(M) = det(E) * det(S_R)` is a consequence
  of E being invertible, not a proof of it.
- Open precondition: prove directly, from the Clifford algebra of `Cl(9,5)` acting on
  `Q = E_0 + Q^{14D}`, that `E(xi)` has trivial kernel for all `xi` with `g_Y(xi,xi) != 0`.

The failure condition is: exhibit a nonzero `psi in Q` such that `E(xi) psi = 0` for some
lightlike `xi` (i.e., `g_Y(xi,xi) = 0`). Note: the claim is only for `g_Y(xi,xi) != 0`; on
the null cone the result is not claimed.

This file provides the direct proof, upgrading the verdict from CONDITIONALLY_EVADED to EVADED.

---

## 2. Setup: The Q Sector and E Block

### 2.1 The Block Decomposition

The GU Dirac operator bundle decomposes as

```
E = R^{14D}  direct-sum  Q
```

where:
- `R^{14D} = ker Gamma^{14D}` is the 14D RS subspace (gamma-trace-free one-form spinors),
  dim_R = 13 * 256 = 3328.
- `Q = E_0 + Q^{14D}` is the complementary sector.

More precisely, `E` is the full Clifford module bundle on which `sigma_D(xi)` acts. In the
GU construction `E = Omega^0(Y^14) tensor S^+ + Omega^1(Y^14) tensor S^-` (chiral halves),
but for the principal symbol computation what matters is the Clifford module structure.

At any point on Y^14, the fiber is

```
E|_y = S^+  direct-sum  (T*Y^14 tensor_R S^-)
```

where `S = H^64`, `S^pm` are the chiral halves `S^pm = H^32`, and
`T*Y^14 tensor_R S^- = R^{14} tensor_R H^32` has dim_R = 14 * 128 = 1792 + 128 = 1920 total.

The **Q sector** (non-RS in the one-form factor) is the complement to the gamma-trace-free part:

```
Q  =  S^+  direct-sum  P_T (T*Y^14 tensor S^-)
```

where `P_T = Id - P_R` and `P_R` is the orthogonal projector onto the RS subspace
`ker Gamma^{14D}` inside the one-form factor. Concretely:

```
P_R alpha_A = alpha_A - (1/14) gamma_A gamma^B alpha_B    (RS projector, 14D)
P_T alpha_A = (1/14) gamma_A gamma^B alpha_B              (gamma-trace projector)
```

So `Q^{14D} = Im(P_T)` consists of sections of the form `(1/14) gamma_A s` for `s in S^-`
(the gamma-trace sector), and `E_0 = S^+` is the scalar spinor sector.

### 2.2 Explicit Description of E(xi)

The E block is the restriction and projection of the principal symbol `M(xi)` to the Q sector:

```
E(xi) = P_Q sigma_D(xi) P_Q |_{Q -> Q}
```

For a general 14D covector `xi` with components `xi_A` (A = 0,...,13), the principal symbol
on the Clifford module acts as

```
sigma_D(xi)(psi) = c(xi) psi = xi_A gamma^A psi     (scalar sector input -> one-form sector output)
sigma_D(xi)(alpha)_B = g_Y(xi, alpha) s_{part} + (F_xi alpha)_B    (one-form sector input)
```

More precisely, using the explicit GU formula from `vz-schur-complement-2026-06-23.md` §2:

```
(F_xi psi_R)_A = xi_A (gamma^B psi_{R,B}) - gamma(xi) psi_{R,A}
```

where `gamma(xi) = xi_A gamma^A` is the full 14D Clifford element.

For Q-inputs, the E block maps:

**Scalar input `phi in S^+ = E_0`:**
```
E(xi): phi  |->  P_Q (sigma_D(xi) phi)
       phi in S^+  |->  (something in Q = S^+ + Im P_T)
```

The principal symbol takes a scalar spinor `phi` to a one-form spinor:
```
sigma_D(xi) phi |_{one-form} = xi tensor phi,   i.e., (xi tensor phi)_A = xi_A phi.
```

Its gamma-trace: `gamma^A (xi_A phi) = gamma(xi) phi`.

The P_T projection: `P_T (xi tensor phi)_A = (1/14) gamma_A gamma^B (xi_B phi) = (1/14) gamma_A gamma(xi) phi`.

So: `E(xi) phi = (1/14) gamma_A gamma(xi) phi in Im P_T`.

The scalar-to-scalar component is zero (scalar output would require `sigma_D(xi)` to map
scalars to scalars, but Dirac-type operators shift degree by one).

**Gamma-trace input `(1/14) gamma_A s in Im P_T`, `s in S^-`:**

The principal symbol acts:
```
sigma_D(xi)((1/14) gamma_B s)
  (scalar part) = g_Y(xi, (1/14) gamma s) = (1/14) xi^A gamma_A s = (1/14) gamma(xi) s  in S^+
  (one-form part) = F_xi((1/14) gamma_B s)
```

Computing the one-form part:
```
(F_xi j(s))_A where j(s)_B = (1/14) gamma_B s
  = xi_A gamma^B j(s)_B - gamma(xi) j(s)_A
  = xi_A gamma^B (1/14) gamma_B s - gamma(xi) (1/14) gamma_A s
  = xi_A (14/14) s - (1/14) gamma(xi) gamma_A s
  = xi_A s - (1/14) gamma(xi) gamma_A s.
```

Its gamma-trace (computed in `vz-schur-complement-2026-06-23.md` §3.3):
```
Gamma^{14D}(F_xi j(s)) = (13/7) gamma(xi) s.
```

So P_T projects to:
```
P_T(F_xi j(s))_A = (1/14) gamma_A (13/7) gamma(xi) s = (13/98) gamma_A gamma(xi) s.
```

**Summary of E(xi) as a 2x2 matrix on Q = E_0 direct-sum Im P_T:**

With basis elements `phi in E_0 = S^+` and `j(s) = (1/14) gamma s in Im P_T, s in S^-`:

```
E(xi): [phi ]  |->  [    0              (1/14) gamma(xi) s   ]
       [j(s)]       [(1/14) gamma(xi) phi  (13/98) gamma_A gamma(xi) s]
```

Writing more compactly with `G := gamma(xi): S -> S` (the Clifford element):

```
E(xi) = [ 0        (1/14) G ]      acting on   E_0 direct-sum Im P_T
        [ (1/14) G  (13/98) G ]
```

where the (1,2) entry maps `s in S^-` to `(1/14) G s in S^+` and the (2,1) entry maps
`phi in S^+` to `(1/14) G phi in Im P_T` (specifically `(1/14) gamma_A G phi`).

---

## 3. Main Theorem: E(xi) is Invertible for g_Y(xi,xi) != 0

### 3.1 Direct Clifford Algebra Proof

**Theorem.** For all `xi in T*Y^{14}` with `xi2 := g_Y(xi,xi) != 0`, the operator
`E(xi): Q -> Q` has trivial kernel.

**Proof.**

Let `(phi, j(s)) in Q = E_0 direct-sum Im P_T` satisfy `E(xi)(phi, j(s)) = 0`.

From the E-matrix above, the two equations are:

```
(Row 1, E_0 output):     (1/14) G s  =  0                     (E1)
(Row 2, Im P_T output):  (1/14) G phi + (13/98) G P_T s = 0  (E2)
```

where we use `G = gamma(xi)` and identify `j(s) = (1/14) gamma_A s` so `s` parametrizes
the Im P_T input.

**Step 1: From (E1).**

```
(1/14) G s = 0   =>   G s = 0   =>   gamma(xi) s = 0.
```

**Step 2: Apply G to (E1) — the key Clifford step.**

```
G^2 s = G (G s) = G (0) = 0.
```

But `G^2 = gamma(xi)^2 = g_Y(xi,xi) Id_S = xi2 Id_S` (Clifford identity in Cl(9,5)).

Therefore:
```
xi2 s = 0.
```

Since `xi2 != 0`:
```
s = 0.
```

**Step 3: From (E2) with s = 0.**

```
(1/14) G phi = 0   =>   G phi = 0.
```

**Step 4: Apply G.**

```
G^2 phi = xi2 phi = G(0) = 0   =>   xi2 phi = 0.
```

Since `xi2 != 0`:
```
phi = 0.
```

**Conclusion.** `(phi, j(s)) = (0, 0)`. So `ker E(xi) = {0}`.  QED.

---

### 3.2 Why This is a Direct Clifford Proof (Not Circular)

The proof uses only:

1. The explicit formula for `E(xi)` derived from the Clifford module structure of `sigma_D`.
2. The fundamental identity `gamma(xi)^2 = g_Y(xi,xi) Id_S` in `Cl(9,5)`.
3. Elementary linear algebra over `H` (since `S = H^64`).

At no point is E-invertibility assumed; it is derived from the eigenvalue structure of `G = gamma(xi)`.
At no point is the `det(M) = det(E)*det(S_R)` factorization invoked. The argument is purely
from the algebraic structure of Clifford multiplication on the Q sector.

---

## 4. Explicit E^{-1} Formula

Since `E(xi)` is invertible for `xi2 != 0`, we can compute `E(xi)^{-1}` explicitly.

From the E-matrix (in block form on `E_0 direct-sum Im P_T`):

```
E(xi) = [ 0         (1/14) G ]
        [ (1/14) G  (13/98) G ]
```

To invert this 2x2 block matrix over the quaternionic scalars (each entry is a map `S^pm -> S^pm`
given by Clifford multiplication, which is invertible when `xi2 != 0`):

Using Schur complement of the (1,1) block (which is 0, so we use the (2,2) block's Schur):

Actually, use row/column operations. From `E(xi) = [[0, A],[A, B]]` where
`A = (1/14) G` and `B = (13/98) G`, note that `A` is invertible with `A^{-1} = 14 G^{-1}`.

Here `G^{-1} = xi2^{-1} G` (since `G^2 = xi2 Id => G * (G/xi2) = Id`).

So `A^{-1} = 14 G^{-1} = (14/xi2) G`.

Schur complement of the top-left block (taking Schur from below):
```
S_{11} = 0 - A * B^{-1} * A = - A B^{-1} A.
```

`B^{-1} = (98/13) G^{-1} = (98/(13 xi2)) G`.

`A B^{-1} A = (1/14) G * (98/(13 xi2)) G * (1/14) G = (98/(13 * 196 * xi2)) G^3 = (98/(13 * 196 * xi2)) * xi2 * G = (1/(2 * 13)) G / 1 = (1/26) G`.

Wait let me redo: `G^3 = G * G^2 = G * xi2 Id = xi2 G`.

`A B^{-1} A = (1/14) G * (98/(13 xi2)) G * (1/14) G`
`= (98/(14 * 13 * 14 * xi2)) G * G * G`
`= (98/(2548 xi2)) * xi2 * G`
`= (98/2548) G`
`= (1/26) G`.

So Schur complement `S_{11} = 0 - (1/26) G = -(1/26) G`.

The block matrix inverse formula for `[[0, A],[A, B]]`:

Using the identity for 2x2 block matrices with invertible off-diagonal:
Let M = [[0, A],[C, B]] with A, C invertible. Then

```
M^{-1} = [[-C^{-1} B A^{-1}, C^{-1}],
           [A^{-1},           -A^{-1} 0 C^{-1}]] ... 
```

Actually, let's use direct computation. We want `X = [[X_{11}, X_{12}],[X_{21}, X_{22}]]` such that `E X = Id`.

```
E X = [[0, A],[A, B]] [[X_{11}, X_{12}],[X_{21}, X_{22}]] = Id
```

Equations:
```
A X_{21} = Id           (from row 1, col 1)  =>  X_{21} = A^{-1} = (14/xi2) G
A X_{22} = 0            (from row 1, col 2)  =>  X_{22} = 0
A X_{11} + B X_{21} = 0 (from row 2, col 1)  =>  X_{11} = -A^{-1} B X_{21} = -A^{-1} B A^{-1}
A X_{12} + B X_{22} = Id (from row 2, col 2) =>  X_{12} = A^{-1} = (14/xi2) G
```

Now compute `X_{11} = -A^{-1} B A^{-1}`:

```
A^{-1} B = (14/xi2) G * (13/98) G = (14 * 13)/(98 xi2) G^2 = (14*13)/(98) Id = (182/98) Id = (13/7) Id.
```

So `X_{11} = -(13/7) A^{-1} = -(13/7)(14/xi2) G = -(26/xi2) G`.

**Explicit E^{-1}:**

```
E(xi)^{-1} = [-(26/xi2) G    (14/xi2) G ]
              [(14/xi2) G       0        ]
```

where `G = gamma(xi)`, `xi2 = g_Y(xi,xi) != 0`.

**Verification:** E E^{-1} at position (1,1):
`0 * (-(26/xi2) G) + A * (14/xi2) G = (1/14) G * (14/xi2) G = (1/xi2) G^2 = (1/xi2) xi2 Id = Id`. Check.

At position (1,2):
`0 * (14/xi2) G + A * 0 = 0`. Check.

At position (2,1):
`A * (-(26/xi2) G) + B * (14/xi2) G = (1/14)(-(26/xi2)) G^2 + (13/98)(14/xi2) G^2`
`= (-(26)/(14 xi2)) xi2 + (13*14)/(98 xi2) xi2`
`= -26/14 + 182/98`
`= -13/7 + 13/7 = 0`. Check.

At position (2,2):
`A * (14/xi2) G + B * 0 = (1/14)(14/xi2) G^2 = (1/xi2) xi2 Id = Id`. Check.

The explicit formula is consistent.

---

## 5. Structural Analysis: Where Does the E Block Act?

### 5.1 Cl(9,5) = M(64,H) Structure

The proof in §3 used only `gamma(xi)^2 = xi2 Id`. This is an identity in `Cl(9,5)`,
where `Cl(9,5) ~= M(64,H)` (quaternionic 64x64 matrices). The spinor module is
`S = H^{64}`, the unique irreducible representation of `Cl(9,5)`.

The element `gamma(xi) = xi_A gamma^A in Cl(9,5)` is a degree-1 Clifford element.
In the representation `Cl(9,5) ~= M(64,H)`, it acts as a 64x64 quaternionic matrix.

The identity `gamma(xi)^2 = g_Y(xi,xi) Id_{64}` is the defining relation of the Clifford
algebra: `{gamma^A, gamma^B} = 2 g_Y^{AB} Id`. It is exact in any faithful representation,
including `M(64,H)`.

**Key consequence.** For any `xi` with `xi2 != 0`:

```
gamma(xi) has eigenvalues pm sqrt(xi2)   (over H, with appropriate meaning).
```

More precisely: `gamma(xi)^2 = xi2 Id` means `gamma(xi) satisfies X^2 - xi2 = 0`,
so `gamma(xi)` is a square root of the scalar `xi2 * Id`. In `M(64,H)` with `xi2 != 0`,
this polynomial has no zero eigenvalues: the minimal polynomial divides `X^2 - xi2`,
which has roots `pm sqrt(xi2)` (both nonzero for `xi2 != 0`). Therefore `gamma(xi) in
GL(64, H)` for `xi2 != 0`.

This is precisely what makes Step 2 of the proof work: `G s = 0 => G^2 s = xi2 s = 0 => s = 0`.

### 5.2 Signature-Independence

The proof works for any signature of the ambient metric `g_Y`. The key is `xi2 != 0`,
not the sign of `xi2`. In signature (9,5):

- For spacelike covectors (g_Y(xi,xi) > 0): `xi2 > 0`, `G` invertible.
- For timelike covectors (g_Y(xi,xi) < 0): `xi2 < 0`, `G` invertible.
- For null covectors (g_Y(xi,xi) = 0): `xi2 = 0`, `G` is nilpotent (`G^2 = 0`), NOT invertible.

The null case is the failure locus: E(xi) is NOT invertible for null xi.

### 5.3 Surjectivity

Since E(xi) is a finite-dimensional linear map (over H, finite-dimensional quaternionic
vector spaces) with trivial kernel, it is automatically bijective (since domain and codomain
have the same H-dimension). Therefore `E(xi)` is an H-linear isomorphism of `Q` for
all `xi` with `xi2 != 0`.

---

## 6. The Failure Locus and Its Physical Interpretation

**Failure locus.** The E block E(xi) is NOT invertible precisely when `xi2 = g_Y(xi,xi) = 0`,
i.e., on the null cone of the ambient metric `g_Y`.

**Why E fails at null xi.** For a null covector `xi` with `gamma(xi)^2 = 0`, the Clifford
element `gamma(xi)` is nilpotent (of order 2). The E matrix becomes:

```
E(xi)_{null} = [ 0        (1/14) G ]    with G^2 = 0.
               [ (1/14) G  (13/98) G ]
```

The kernel: `(1/14) G s = 0` gives `G s = 0`, which has nontrivial solutions when `G`
is nilpotent. Specifically, in `Cl(9,5) ~= M(64,H)`, for any null covector `xi`,
`gamma(xi)` is a nilpotent element and `ker gamma(xi) != 0` (it is a 32-dimensional
H-subspace of S = H^{64}, since `G^2 = 0` implies `Im G subset ker G` and by dimension
counting `dim_H Im G = dim_H ker G = 32` for a generic null G in M(64,H)).

Any `s in ker gamma(xi)` (with `s != 0`) gives `(phi, j(s)) = (0, j(s)) in ker E(xi)`.

**Physical interpretation of the null locus.** The null cone `{xi : g_Y(xi,xi) = 0}` in
`T*Y^14` corresponds to the characteristics of the GU Dirac operator: these are the
directions in which `sigma_D(xi)` fails to be an isomorphism. This is completely expected
and correct:

1. The GU Dirac operator `D_GU` is a hyperbolic-type operator. Its characteristic cone is
   exactly the null cone of the ambient metric. At null characteristics, the principal symbol
   `M(xi)` has a nontrivial kernel (this is what makes `D_GU` a wave operator rather than
   an elliptic operator).

2. E(xi) failing at null xi is part of this expected behavior. It signals that the null
   characteristics of `D_GU` are correctly null-cone-governed, not a defect.

3. VZ evasion requires that the effective RS propagator `S_R(xi)` has no spacelike
   characteristics (no null vector with `xi2 > 0`). The theorem in §3 proves exactly this:
   for all `xi` with `xi2 != 0` (including all spacelike and timelike xi), `ker E(xi) = 0`,
   and therefore the Schur complement argument in `vz-14d-mixed-covectors-2026-06-23.md`
   §4 is valid, and `ker S_R^{14D}(xi) = 0`.

4. The null locus `xi2 = 0` is not a VZ failure locus: VZ acausality would require spacelike
   characteristics (`xi2 > 0`, lightcone coordinates). Null characteristics are the CORRECT
   behavior for a causal wave operator.

**Failure condition from the problem statement.** The task asked us to exhibit or rule out
a nonzero `psi in Q` with `E(xi) psi = 0` for some lightlike `xi`. We have shown:

- For lightlike xi (xi2 = 0): such `psi` EXIST (any `psi = (0, j(s))` with `s in ker gamma(xi)`).
- But lightlike xi are NOT in the VZ failure locus: the Schur complement argument for VZ
  evasion only requires E invertible at non-null xi. The Schur complement argument is invoked
  for the VZ principal symbol at `xi2 != 0`.

So the failure condition is correctly scoped: E fails exactly at the null cone, which is
not a VZ problem but rather the expected hyperbolic characteristic behavior.

---

## 7. Completing the VZ Evasion Proof

With E(xi) invertibility established for all `xi2 != 0`, the Schur complement argument
in `vz-14d-mixed-covectors-2026-06-23.md` §4 is now valid without any circular step.

**Corrected proof of `ker S_R^{14D}(xi) = 0` for `xi2 != 0`.**

**Step 1.** Suppose `S_R(xi) psi_R = 0` for some `psi_R in R^{14D}`.

**Step 2.** Since `xi2 != 0`, E(xi) is invertible (proved in §3 above). Define
`v = -E(xi)^{-1} C(xi) psi_R`. Then:

```
M(xi)(psi_R, v) = (A psi_R + B v, C psi_R + E v)
                = (A psi_R - B E^{-1} C psi_R, C psi_R - E E^{-1} C psi_R)
                = (S_R psi_R, 0)
                = (0, 0).
```

**Step 3.** Apply `M(xi)` to (psi_R, v):

```
0 = M(xi)(0) = M(xi)^2 (psi_R, v) = xi2 (psi_R, v).
```

**Step 4.** Since `xi2 != 0`: `(psi_R, v) = 0`, hence `psi_R = 0`. QED.

This is a complete proof at reconstruction grade, with no circular steps.

---

## 8. Verdict Upgrade: EVADED

**Verdict for `vz-14d-mixed-covectors`:** CONDITIONALLY_EVADED -> **EVADED**

The single remaining precondition (E(xi) invertibility for xi2 != 0) is now directly proved
from the Clifford algebra of Cl(9,5) acting on Q = E_0 + Q^{14D}.

**Summary of what is now established (reconstruction grade):**

| Statement | Status |
|---|---|
| E(xi) invertible for xi2 != 0 | RESOLVED (§3, direct Clifford) |
| E(xi) fails for xi2 = 0 (null cone) | RESOLVED (§6, explicit kernel) |
| ker S_R^{14D}(xi) = 0 for all xi2 != 0 | RESOLVED (§7, corrected Schur proof) |
| VZ evasion: no spacelike RS characteristics in 14D | EVADED (reconstruction grade) |
| Failure locus: null cone only | RESOLVED — expected hyperbolic behavior |
| Null locus is not a VZ failure | RESOLVED — VZ requires spacelike characteristics |

**Explicit E^{-1} formula** (from §4):

```
E(xi)^{-1} = [-(26/xi2) gamma(xi)    (14/xi2) gamma(xi) ]
              [(14/xi2) gamma(xi)        0                ]
```

This is a clean closed-form inverse, confirming the invertibility constructively.

---

## 9. Remaining Open Questions

The upgrade to EVADED is for the **principal symbol** level. The following remain open at
the level of the full operator:

**OQ-RS-2 (loop corrections).** Are B/C blocks modified at one loop? Structural argument
(vz-f6) says the Clifford identity `sigma_D^2 = xi2 Id` is loop-exact because it follows
from the graded algebra structure. The explicit E^{-1} formula in §4 is also loop-exact
(it is an algebraic identity in the principal symbol, not a perturbative expansion). CAS
one-loop computation not yet performed.

**OQ-RS-3 (GU-Vasiliev comparison).** The Leibniz RS embedding strategy may give a new
class of consistent higher-spin theories; comparison with Vasiliev not yet completed.

**OQ-RS-4 (Noncompact Fredholmness).** Full Fredholmness on noncompact Y^14 requires
b-calculus; blocked on G3 (bounded-transform continuity in Fred_H).

**OQ-CAS-E.** CAS verification of the E^{-1} formula: explicit 64x64 quaternionic matrix
computation of `gamma(xi)` for representative xi (e.g., xi = e^0 + e^9 with sig (3,1)+(6,4)
and xi2 = -1 + 1 = 0 at null, or xi = e^0 alone with xi2 = -1 != 0). Should confirm
`ker gamma(xi) = 0` for timelike xi and `ker gamma(xi) != 0` for null xi.

---

## 10. Explicit Failure Check (Problem Statement)

The problem statement asked: exhibit a nonzero psi in Q such that E(xi) psi = 0 for some
lightlike xi.

**Answer:** Such psi exists precisely on the null cone. Take any null covector `xi` with
`xi2 = g_Y(xi,xi) = 0`. Then `G = gamma(xi)` satisfies `G^2 = 0`. The kernel of G in
`S = H^64` is a 32-dimensional H-subspace (by nilpotency and rank-nullity in `M(64,H)`).
Take any `s in ker G`, `s != 0`. Set `psi = (0, j(s)) in E_0 direct-sum Im P_T = Q`.
Then:

```
E(xi)(0, j(s)) = [(1/14) G s, (13/98) G j(s)]
               = [(1/14) * 0, (13/98) * 0]
               = (0, 0).
```

So `psi = (0, j(s)) != 0` satisfies `E(xi) psi = 0` for null xi.

**But this does not obstruct VZ evasion.** The Schur complement for VZ is used at `xi2 != 0`.
For null xi, the entire operator M(xi) has a nontrivial kernel (since `M(xi)^2 = 0`);
this is the expected behavior for a hyperbolic wave operator and is not an acausality.

---

## 11. Explicit Failure Conditions (for EVADED status)

The EVADED verdict would be falsified by:

**F1.** The Q-block sector being larger than `E_0 direct-sum Im P_T`. If the Q decomposition
is different from what is computed here (e.g., if the GU operator includes additional
sector couplings beyond the standard Clifford module structure), the E matrix could have
additional rows/columns.

**F2.** The E-matrix formula `E = [[0, (1/14)G],[(1/14)G,(13/98)G]]` being incorrect.
This would require the Clifford multiplication formula `gamma^A gamma(xi) gamma_A = -12 gamma(xi)`
(which holds in 14D from `{gamma^A,gamma^B}=2g^{AB}Id`) to fail. This is an algebraic identity
in Cl(9,5) and cannot fail.

**F3.** An additional non-Clifford term in `sigma_D(xi)`. If the GU Dirac operator has
a non-standard principal symbol (e.g., from a non-minimal coupling that modifies the leading
order symbol), the Clifford identity would not apply.

**F4.** The Q-sector having elements outside `E_0 direct-sum Im P_T` that are in the kernel
of the projection `P_Q`. If the RS projector P_R is defined differently in the full GU
construction (e.g., using a covariant projector that mixes horizontal and vertical components),
the Q-block could be larger.

---

## 12. References

- `explorations/vz-evasion/vz-14d-mixed-covectors-2026-06-23.md` (parent synthesis; VZ-01 correction; CONDITIONALLY_EVADED verdict being upgraded)
- `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` (E-block derivation §3.3; 4D CONDITIONALLY_RESOLVED, constant-coefficient gauge; OQ3-V1 CONDITIONALLY_RESOLVED, V2/V3 RESOLVED)
- `explorations/vz-evasion/vz-oq1-sr-squared-identity-2026-06-23.md` (S_R^2 != xi2 Id; A S_R = xi2 Id)
- Lawson-Michelsohn, _Spin Geometry_, Ch. I §1-2 (Clifford algebra, `gamma(xi)^2 = g(xi,xi) Id`)
- Atiyah-Bott-Shapiro, _Clifford Modules_ (1964) (Cl(9,5) = M(64,H) classification)
- Velo-Zwanziger (1969), Phys. Rev. 186:1337 (H1-H3 hypotheses for VZ theorem)
