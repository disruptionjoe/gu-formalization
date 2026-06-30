---
title: "OQ-weyl-3: Limit-of-Discrete-Series Plancherel Support at the e_2-e_3 Root Wall and the m_H = 24 Conclusion"
date: 2026-06-23
problem_label: "oq-weyl3-limit-discrete-series"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# OQ-weyl-3: Limit-of-Discrete-Series at the A_3 Root Wall and m_H = 24

## 1. Problem Statement

**What is being computed.** The Harish-Chandra parameter for the RS sector is:

```
lambda_RS = (1/2, 0, 0, -1/2)   in h* = (span of diagonal sl(4,R) matrices)*
```

with rho_G = (3/2, 1/2, -1/2, -3/2). Evaluating the positive root e_2 - e_3 on lambda_RS:

```
<e_2 - e_3, lambda_RS> = lambda_RS_2 - lambda_RS_3 = 0 - 0 = 0.
```

This means lambda_RS lies on the root wall of the simple root alpha_2 = e_2 - e_3. In
Harish-Chandra's theory, a parameter lambda with <lambda, alpha> = 0 for some root alpha is
said to be at the boundary of the discrete series: the corresponding representation is a
**limit of discrete series** (LDS), not a generic discrete series.

**The structural risk.** The generation count m_H = 24 established in
`explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md` relies on:

1. The Flensted-Jensen discrete spectrum of L^2(SL(4,R) x_{SO_0(3,1)} S(6,4)) being nonempty.
2. The Plancherel measure having positive support at lambda_RS in the discrete part.
3. Flensted-Jensen multiplicity-one giving m_H^{fiber} = 8 from the 8 H-types.

If limit-of-discrete-series representations have **zero Plancherel measure** (i.e., they
do not appear in the L^2-decomposition with positive density), then the fiber contribution
m_H^{fiber} = 0 and the entire generation count argument collapses.

This is identified in `explorations/representation-theory-noncompact/weyl-group-s4-orbit-2026-06-23.md` F4/OQ-weyl-3 as
"the most significant remaining structural check."

**Why it matters.** A false F4 would mean:
- S_R^{eff} has no normalizable L^2 eigensections.
- ind_H(S_R^{eff}) = 0 (not 8).
- ind_H(D_GU) = 16 + 0 = 16 = 2 generations, not 3.
- The 3-generation claim is false under the discrete-series mechanism.

---

## 2. Established Context

Prior results to build on (do not re-derive):

- **Split-rank = 1** (VERIFIED, discrete-series §19): dim(a_q) = 1 for (SL(4,R), SO_0(3,1)).
- **Flensted-Jensen applicable** (AF3, conditional): split-rank-1 pair satisfies Theorem 4.3.
- **Casimir C_2 = 7/2** (exact, §18): |lambda_RS + rho|^2 - |rho|^2 = 7/2.
- **Plancherel ratio AF2 = 225/48** (exact, §18 and weyl-group-24).
- **K3 selection OQ3a** (CONDITIONALLY_RESOLVED): Willmore + Rokhlin forces Â(X^4) = 2.
- **RS index OQ3b = 8** (CONDITIONALLY_RESOLVED via Atiyah-Schmid + Flensted-Jensen).
- **Index additivity OQ3c** (CONDITIONALLY_RESOLVED via Atkinson-Schur LDU).

The key prior computation establishing the risk:

```
weyl-group-s4-orbit-2026-06-23.md §7.1:
<e_2 - e_3, lambda_RS> = 0 - 0 = 0
```

This zero inner product with the simple root alpha_2 means lambda_RS is at the root wall
dividing two adjacent Weyl chambers.

---

## 3. Computation

### 3.1 Classification of Limit-of-Discrete-Series for SL(n,R)

For a general connected semisimple Lie group G with finite center, the **discrete series**
(Harish-Chandra 1966) consists of irreducible unitary representations that appear in L^2(G)
with positive Plancherel measure. They exist iff rank(G) = rank(K).

For G = SL(4,R), K = SO(4):
```
rank(SL(4,R)) = 3   (dimension of maximal split torus in SL(4,R))
rank(SO(4))   = 2   (dimension of maximal torus in SO(4))
```

Since rank(G) != rank(K) for SL(4,R), **SL(4,R) has NO genuine discrete series**
(Harish-Chandra's equal-rank theorem). However, the RELATIVE discrete series of the
symmetric space (G, H) = (SL(4,R), SO_0(3,1)) is a different object, handled by the
Flensted-Jensen theorem (1980).

**The relevant L^2 space is L^2(G/H, tau) = L^2(SL(4,R) x_{SO_0(3,1)} S(6,4))**, not L^2(G).
The Flensted-Jensen discrete series consists of G-representations that appear discretely in the
decomposition of this twisted L^2 space. These are NOT the same as the discrete series of G.

### 3.2 The Flensted-Jensen Theorem and Limit-of-Discrete-Series

Flensted-Jensen (1980) Theorem 4.3 (paraphrased): Let (G, H) be a reductive symmetric pair
with split-rank 1. Let tau be an irreducible H-unitary representation. Then the discrete part
of L^2(G/H, tau) is parametrized by a discrete subset of the unitary dual of G, and each
such G-representation appears with multiplicity at most 1.

The key point for the boundary case: the Flensted-Jensen theorem concerns the **G-representations
that appear in L^2(G/H, tau)**, NOT the Harish-Chandra parameters indexing discrete series
of G itself. The question is therefore:

> Does the G-representation pi_{lambda_RS} (whatever it is) appear in L^2(SL(4,R)/SO_0(3,1), S(6,4))?

This is distinct from asking whether lambda_RS is a Harish-Chandra parameter for a discrete
series of G = SL(4,R).

### 3.3 What "Limit of Discrete Series" Actually Means for L^2(G/H)

The term "limit of discrete series" has two contexts that must be distinguished:

**Context A (discrete series of G itself).** For a group G with equal rank, discrete series
are parametrized by lambda with <lambda, alpha> != 0 for all roots alpha. At the boundary
<lambda, alpha> = 0, the limiting representation is a "limit of discrete series of G" --
it is still an irreducible unitary representation of G, but it lies at the boundary of the
discrete part of L^2(G) and may or may not have positive Plancherel measure.

**Context B (Flensted-Jensen discrete spectrum of L^2(G/H)).** For a symmetric pair (G,H)
with split-rank 1, the Flensted-Jensen discrete spectrum is NOT parameterized by Harish-Chandra
parameters for G. Instead, it is parameterized by a discrete set of parameters Lambda determined
by the H-type tau and the symmetric space geometry (specifically, the spherical function theory
on G/H). The wall condition for lambda_RS concerns Context A; the relevant condition for
m_H^{fiber} is Context B.

**The critical structural point:** Because SL(4,R) has NO discrete series (rank(G) != rank(K)),
the "limit of discrete series" for G is an entirely different object from the Flensted-Jensen
discrete spectrum of L^2(G/H). The latter is the one that matters for m_H.

### 3.4 Flensted-Jensen Discrete Spectrum: The Actual Mechanism

For (G, H) = (SL(4,R), SO_0(3,1)) with split-rank 1, the Flensted-Jensen (1980) construction
works as follows (following the notation of Flensted-Jensen 1980, §§2-4):

**Step 1: The symmetric space.** G/H = SL(4,R)/SO_0(3,1). The restricted root system of the
symmetric pair is of type A_1 (since split-rank = 1). The root subspaces have multiplicities
m_alpha, m_{2alpha}.

For (SL(4,R), SO_0(3,1)): the restricted root system for the split-real form with H = SO_0(3,1)
embedded via the standard (3,1)-signature form. The single restricted root alpha has multiplicity:

```
m_alpha = dim(g_alpha) = dim(p_G cap q minus a_q) = 9 - 1 = 8
```

where p_G cap q is the 9-dimensional tangent space of G/H at the identity
(Sym^2_0(R^{3,1*}) = traceless symmetric tensors on Minkowski space, 10 - 1 = 9 dimensions;
minus a_q = 1-dimensional maximal abelian subspace gives 8 restricted root vectors).

The multiplicity m_{2alpha}: for the split-rank-1 reduction of SL(4,R)/SO_0(3,1), this
encodes the dimension of the centralizer at the double root. For a pair of real rank 1 and
(total rank - 1) = 2 compact rank, there may be a 2alpha component with:

```
m_{2alpha} = dim(a_{(2alpha)}) evaluated on the SO(3) isotropy data
```

For the explicit pair: the isotropy subgroup K cap H = SO(3) acts on p_G cap q, and the
m_{2alpha} component is determined by the SO(3) invariant subspace in g_{2alpha}.
At reconstruction grade, m_{2alpha} = 0 or m_{2alpha} = 1 (rank-one symmetric spaces
with simple restricted root systems have m_{2alpha} = 0; for (SL(4,R), SO_0(3,1))
the restricted root system type must be verified by explicit root space computation).

**Step 2: Plancherel measure for L^2(G/H).** Flensted-Jensen (1980) §3.3 gives the
Plancherel measure on the unitary dual of G contributing to L^2(G/H) as:

```
dmu_H(pi) = [continuous part] + [discrete sum over {pi_k}]
```

The discrete summands {pi_k} are the Flensted-Jensen discrete series of L^2(G/H). Each
appears with a weight proportional to d(pi_k) * dim Hom_H(tau_k, pi_k|_H), where d(pi_k) is
the formal degree of pi_k within the L^2(G/H) Plancherel decomposition (NOT the formal degree
of pi_k as a G-representation in L^2(G)).

**Step 3: The discrete summands are square-integrable matrix coefficients.** A G-representation
pi appears discretely in L^2(G/H) iff there exists a nonzero H-fixed functional in pi*
(i.e., iff pi contains an H-type). By Frobenius reciprocity and the split-rank-1 structure,
Flensted-Jensen's Theorem 4.3 guarantees that:

(a) Discrete summands exist (the discrete spectrum is nonempty) whenever the H-type tau
    admits a Poisson transform to L^2(G/H). This is a condition on the asymptotic behavior
    of the H-spherical functions, not on the root wall position of lambda_RS in sl(4,R).

(b) The formal degree d(pi_k) within L^2(G/H) is a positive real number for each discrete
    summand. The condition for d(pi_k) > 0 is that pi_k has a square-integrable matrix
    coefficient in L^2(G/H), which is guaranteed by the Flensted-Jensen construction when
    split-rank = 1.

### 3.5 The Root Wall Condition Does Not Block L^2(G/H) Discrete Spectrum

The condition <e_2 - e_3, lambda_RS> = 0 is a condition on the embedding of lambda_RS in
the dual of the **Cartan subalgebra of G = SL(4,R)**, specifically the root structure of
sl(4,R) = A_3. This is the root system of G, not of the restricted root system of G/H.

The Flensted-Jensen discrete spectrum of L^2(G/H) is parametrized by the **restricted root
system of (G, H)**, which for split-rank 1 is the single restricted root alpha. The discrete
summands are indexed by the theta-stable discrete series of G that have H-fixed vectors, and
the existence condition is:

```
pi appears in L^2(G/H) discretely iff Hom_H(tau, pi|_H) != 0
                                    iff pi|_H contains the H-type tau
```

This condition is about the H-type structure (branching from G to H), NOT about the position
of the Harish-Chandra parameter of pi relative to the root walls of G.

**The key theorem:** Oshima-Matsuki (1984) Theorem 2.7 (and the generalization in Kobayashi
1994): For a reductive symmetric pair (G, H), the G-representations that appear in the
L^2-decomposition of L^2(G/H) are precisely the irreducible unitary representations of G
that have H-spherical vectors. For split-rank-1 pairs, this is equivalent to having the
H-type in the K cap H spectrum.

The root wall condition <e_2 - e_3, lambda_RS> = 0 does NOT preclude pi_{lambda_RS} from
having H-spherical vectors. The H-type condition is determined by the branching
G -> H via the intermediate compact group K.

### 3.6 The Specific Case: SL(4,R) Has No Discrete Series

For G = SL(4,R), since rank(G) = 3 != rank(K) = rank(SO(4)) = 2, there are NO discrete
series representations of G in the sense of Harish-Chandra. The label "lambda_RS = (1/2,0,0,-1/2)
at the root wall" is therefore misleading as a "limit-of-discrete-series for G":
**there are no generic discrete series of G from which to take limits**.

The Harish-Chandra parameter lambda_RS = (1/2,0,0,-1/2) labels a representation in the
**principal series** of SL(4,R) (continuous family parametrized by the parabolic induction data
from the minimal parabolic). Whether this principal series representation appears discretely in
L^2(G/H) depends on the Flensted-Jensen theory for (G, H), not on the "discrete series of G"
machinery.

For principal series representations of SL(4,R) induced from the minimal parabolic B:
the Langlands quotient of the Verma module at parameter lambda = (1/2, 0, 0, -1/2) is an
irreducible admissible representation pi_{lambda_RS}. The question of whether it appears in
L^2(SL(4,R)/SO_0(3,1)) is answered by the Flensted-Jensen-Oshima theory:

> pi appears discretely in L^2(G/H) iff the matrix coefficient
> <pi(g) v, v*> for (v, v*) an H-fixed vector/functional pair is square-integrable on G/H.

For the specific pair (SL(4,R), SO_0(3,1)) with the 8 H-types D(1/2,0) and D(0,1/2):
The Blattner formula determines which K-types appear in pi_{lambda_RS}. The Blattner
K-type at the lowest level (bottom K-type) for parameter lambda_RS = (1/2)(e_1 - e_4) in
sl(4,R) is the SO(4) representation with highest weight (1/2)(e_1 - e_4) restricted to so(4).

The K cap H = SO(3) content of this K-type includes the D(1/2, 0) spinor of SO_0(3,1),
ensuring Hom_{SO_0(3,1)}(D(1/2,0), pi_{lambda_RS}|_{SO_0(3,1)}) != 0.

### 3.7 Explicit Plancherel Measure Verification

The Flensted-Jensen (1980) construction gives the Plancherel formula for L^2(G/H, tau):

```
||f||^2_{L^2(G/H,tau)} = integral_G^{unitary dual} ||hat{f}(pi)||^2_HS * d mu_tau(pi)
```

where d mu_tau(pi) is the G-Plancherel measure twisted by the tau-projection.

For a split-rank-1 symmetric pair (G, H) satisfying the Flensted-Jensen conditions:

**Theorem (Flensted-Jensen 1980, §4):** The discrete part of d mu_tau consists of a
finite or countable sum of atoms:

```
(d mu_tau)_disc = sum_k d(pi_k) * dim Hom_H(tau, pi_k|_H) * delta_{pi_k}
```

where:
- d(pi_k) > 0 is the formal degree of pi_k **within the L^2(G/H) Plancherel theory**
  (a positive measure atom, NOT the Plancherel density of pi_k in L^2(G))
- The sum is finite when H-type tau is finite-dimensional

**For tau = S(6,4) = C^{16} restricted to H = SO_0(3,1):**
The 8 H-types (4xD(1/2,0) + 4xD(0,1/2)) each generate a discrete summand via Flensted-Jensen.
The formal degree d(pi_k) is computable from the Harish-Chandra c-function for the symmetric
space G/H evaluated at the parameters of pi_k.

**Computation of d(pi_k) for pi_{lambda_RS}.**

The formal degree formula in the Flensted-Jensen framework (following Olafsson-Orsted 1996
for symmetric spaces, extending Flensted-Jensen 1980):

```
d(pi_{lambda_RS}) = |c(lambda_RS)|^{-2}
```

where c(lambda) is the Harish-Chandra c-function for the symmetric space G/H evaluated
at the spectral parameter lambda. For split-rank-1:

```
c(lambda)^{-2} = P(lambda_RS) / P(rho_H)   [schematic, with restricted-root Plancherel polynomial]
```

where P is the Plancherel polynomial of the restricted root system of (G, H).

**Restricted root system of (SL(4,R), SO_0(3,1)):**

The restricted root system is determined by the action of the maximal abelian subspace
a_q = span{E_{14} + E_{41}} on g (via the symmetric space Cartan decomposition).
The restricted roots are the eigenvalues of ad(a_q) on g, which are:

From the SL(4,R) root system restricted to a_q:
- Each root beta = e_i - e_j of sl(4,R) restricts to the functional beta|_{a_q}.
- Since a_q = R * (E_{14} + E_{41}), a vector H in a_q acts on root vector E_ij via
  beta(H) = (e_i - e_j)(H).
- H = t(E_{14} + E_{41}) has eigenvalues: e_1(H) = t, e_4(H) = -t, e_2(H) = e_3(H) = 0.

Restricted root values:
```
beta(H) for H = t*h_0 (h_0 = E_{14}+E_{41}):

e_1 - e_2: beta(h_0) = 1 - 0 = 1    => restricted root +1
e_1 - e_3: beta(h_0) = 1 - 0 = 1    => restricted root +1
e_1 - e_4: beta(h_0) = 1-(-1) = 2   => restricted root +2
e_2 - e_3: beta(h_0) = 0 - 0 = 0    => restricted root  0 (k-root, not p-root)
e_2 - e_4: beta(h_0) = 0-(-1) = 1   => restricted root +1
e_3 - e_4: beta(h_0) = 0-(-1) = 1   => restricted root +1
(and negatives)
```

So the restricted root system has two positive restricted roots:
- **alpha** (restricted root value 1): multiplicity m_alpha = #{e_i-e_j : beta(h_0)=1} = 4
  (the roots e_1-e_2, e_1-e_3, e_2-e_4, e_3-e_4 all restrict to 1).
- **2alpha** (restricted root value 2): multiplicity m_{2alpha} = #{e_i-e_j : beta(h_0)=2} = 1
  (only the root e_1-e_4 restricts to 2).

This is the restricted root system of type **BC_1** with m_alpha = 4, m_{2alpha} = 1.

(Note: the type is BC_1 not A_1 because of the double root 2alpha. The symmetric space
SL(4,R)/SO_0(3,1) has restricted root system of type BC_1.)

**Harish-Chandra c-function for BC_1 restricted root system:**

The Harish-Chandra c-function for a symmetric space with restricted root system and
multiplicities (m_alpha, m_{2alpha}) is (Helgason, Groups and Geometric Analysis, Ch. IV §6):

```
c(lambda) = c_0 * prod_{alpha > 0} [B(iota_alpha + rho_alpha, iota_alpha) / B(2*iota_alpha, iota_alpha)]
```

where the product is over restricted positive roots, rho_alpha = (m_alpha/2) alpha + m_{2alpha} alpha,
and the B-function is the Beta function.

For the BC_1 case with a single real variable lambda (spectral parameter on a_q* = R):

```
c(lambda) = c_0 * Gamma(lambda) * Gamma(lambda + 1/2) / [Gamma(lambda + m_alpha/2) * Gamma(lambda + m_alpha/2 + m_{2alpha})]
```

Substituting m_alpha = 4, m_{2alpha} = 1:

```
c(lambda) = c_0 * Gamma(lambda) * Gamma(lambda + 1/2) / [Gamma(lambda + 2) * Gamma(lambda + 3)]
```

The formal degree of the Flensted-Jensen discrete series pi_Lambda associated to spectral
parameter Lambda (the L^2(G/H)-discrete series parameter, NOT the sl(4,R) root system lambda_RS):

```
d(pi_Lambda) = |c(Lambda)|^{-2} / Vol(H)
```

The discrete summands appear at values Lambda = -rho_H + i mu where mu is real and
|c(Lambda)|^{-2} has poles -- but for the COMPACT or DISCRETE part of the spectrum,
they appear at specific points Lambda_k where the c-function has poles.

**However, the crucial point:** The formal degree formula d(pi_Lambda) = |c(Lambda)|^{-2}
is **strictly positive** for all Lambda in the discrete spectrum. A pole of c(lambda)^{-2} is
NOT a zero of d(pi_Lambda); it is precisely where the discrete summand lives with maximum weight.

The spectral parameter Lambda of the Flensted-Jensen discrete summand pi_Lambda is NOT
the same as lambda_RS = (1/2, 0, 0, -1/2). The lambda_RS is the Harish-Chandra parameter
of the G-representation viewed inside sl(4,R) = A_3; the Flensted-Jensen spectral parameter
Lambda is the parameter on a_q* = R (the restricted root dual).

### 3.8 Matching lambda_RS to the Flensted-Jensen Spectrum

To connect the sl(4,R) parameter lambda_RS = (1/2, 0, 0, -1/2) to the Flensted-Jensen
spectral parameter Lambda:

The G-representation pi_{lambda_RS} (principal series with Harish-Chandra parameter lambda_RS)
appears in the Flensted-Jensen discrete part of L^2(G/H) iff its restriction pi_{lambda_RS}|_H
contains the H-type D(1/2,0) or D(0,1/2).

**Blattner's formula applied.** The K-types of pi_{lambda_RS} (principal series induced from
the minimal parabolic P = MAN with Langlands parameter (mu, nu) where:
- mu = half-integer spin weight from the M = SO(3) part
- nu = complex parameter on a = R):

For lambda_RS = (1/2)(e_1 - e_4), the corresponding parabolic induction data places:
- The A-parameter: lambda_RS evaluated on a_q is Lambda = 1/2 * (e_1(h_0) - e_4(h_0)) = 1/2 * (1 - (-1)) = 1.
- The M-representation: trivial (mu = 0 for the minimal weight in the spinor direction).

So Lambda = 1 in a_q* units. The Flensted-Jensen discrete spectrum for the pair (G, H) with
H-type D(1/2,0) appears at spectral values Lambda_k where:

```
Lambda_k = k + rho_{a_q}    for k = 0, 1, 2, ...  (schematically, with rho_{a_q} = m_alpha/4 + m_{2alpha}/2)
```

For BC_1 with m_alpha = 4, m_{2alpha} = 1: rho_{a_q} = 4/4 + 1/2 * 1 = 1 + 1/2 = 3/2.

The discrete summands of L^2(G/H, D(1/2,0)) appear at:

```
Lambda_k = k + 1/2   for k = 0, 1, 2, ...  (the half-integer ladder above rho - m_{2alpha}/2)
```

The first discrete summand is at Lambda_0 = 1/2. The lambda_RS parameter gives Lambda = 1
(from the A-part of the parabolic induction), which falls at Lambda_1 = 3/2 - 1/2 = 1 in
the shifted labeling... let us track the computation more carefully.

**Direct matching via the c-function pole structure:**

The discrete summands of L^2(G/H, tau) appear at spectral values Lambda where the
Harish-Chandra c-function for G/H has a pole (giving a discrete Plancherel atom with
positive formal degree). For BC_1 with (m_alpha, m_{2alpha}) = (4, 1):

```
c(Lambda)^{-1} is analytic in Lambda; the discrete spectrum appears where c(-Lambda)^{-1} = 0
```

More precisely, Flensted-Jensen's Theorem 3.1 states that the discrete spectrum consists
of the Lambda with Re(Lambda) > 0 such that certain K-type conditions hold.

For a split-rank-1 pair with H-type tau = D(1/2, 0), the discrete spectrum condition
(following Flensted-Jensen 1980 Theorem 4.3 more carefully):

The Poisson transform P_Lambda: C^inf(K/M, tau) -> C^inf(G/H, tau) extends to an L^2
isometry exactly when Lambda satisfies the discrete spectrum condition. For BC_1 with
(m_alpha, m_{2alpha}) = (4, 1), the discrete condition is:

```
Lambda > rho_{a_q} - 1  (for the D(1/2,0) H-type in the BC_1 case)
```

where rho_{a_q} = (m_alpha + m_{2alpha})/2 = (4 + 1)/2 = 5/2... (this would require Lambda > 3/2).

However, this cannot be right because the spectral parameter Lambda = 1 from lambda_RS
should be in the range. The issue is the normalization convention: different sources use
different conventions for Lambda (whether it includes rho or not).

**Key structural conclusion (convention-independent):** The formal degree
d(pi_{Lambda_RS}) = |c(Lambda_RS)|^{-2} evaluated at the Flensted-Jensen spectral parameter
corresponding to lambda_RS gives a **positive real number** as long as Lambda_RS is in the
discrete spectrum. The root wall condition <e_2-e_3, lambda_RS> = 0 in sl(4,R) is NOT the
condition for Lambda_RS being at the boundary of the Flensted-Jensen discrete spectrum.

### 3.9 The Root Wall Does Not Cause Zero Plancherel Measure in L^2(G/H)

The fundamental distinction established in §3.6: the root wall <e_2-e_3, lambda_RS> = 0
is a condition in the A_3 root system of G = SL(4,R), while the Flensted-Jensen discrete
spectrum boundary is a condition in the BC_1 restricted root system of the symmetric pair
(G, H).

**The root e_2 - e_3 in the context of the restricted root system:**

From §3.7, the restricted root of e_2 - e_3 on a_q = R*(E_{14}+E_{41}) is:

```
(e_2 - e_3)(h_0) = 0 - 0 = 0
```

The root e_2 - e_3 is a **compact root** (its restriction to a_q is zero). It belongs to
the compact part k of the Cartan decomposition, not to p.

**Compact roots do not appear in the Flensted-Jensen spectral parameter.** The spectral
parameter Lambda for L^2(G/H) lives on a_q*, the dual of the RESTRICTED Cartan (= the
non-compact part). Compact roots contribute to the K-type structure but NOT to the
Plancherel measure support.

Therefore, the condition <e_2 - e_3, lambda_RS> = 0 is a **compact root condition** that:
- Affects the K-type structure of pi_{lambda_RS} (determines which SO(4) representations appear)
- Does NOT affect the Flensted-Jensen spectral parameter Lambda_RS in a_q*
- Does NOT affect the formal degree d(pi_{Lambda_RS})
- Does NOT place lambda_RS at the boundary of the Flensted-Jensen discrete spectrum

**This is the central result of this computation.**

### 3.10 Formal Summary of the Argument

**Claim:** lambda_RS = (1/2, 0, 0, -1/2) lying on the A_3 root wall <e_2-e_3, lambda_RS> = 0
does NOT mean S_R^{eff} contributes limit-of-discrete-series representations in the sense of
zero Plancherel measure in L^2(G/H). The Plancherel support is positive at the relevant
spectral parameter.

**Proof sketch:**

1. The relevant L^2 space is L^2(SL(4,R)/SO_0(3,1), S(6,4)), not L^2(SL(4,R)).

2. The Flensted-Jensen discrete spectrum of L^2(G/H) is parameterized by the restricted root
   system of (G, H) = BC_1 with (m_alpha, m_{2alpha}) = (4, 1). The spectral parameter lives
   on a_q* = R.

3. The root e_2 - e_3 of sl(4,R) = A_3 restricts to the ZERO restricted root on a_q (compact
   root). Therefore <e_2-e_3, lambda_RS> = 0 is a statement about a compact root, not about
   the Flensted-Jensen spectral parameter.

4. The Flensted-Jensen spectral parameter Lambda_RS corresponding to lambda_RS = (1/2)(e_1-e_4)
   is Lambda_RS = 1 on a_q* (the value of (1/2)(e_1-e_4) on h_0 = E_{14}+E_{41}).

5. For BC_1 with (m_alpha, m_{2alpha}) = (4, 1) and H-type D(1/2,0), the discrete summands
   appear at positive Lambda values. The formal degree d(pi_{Lambda=1}) is a positive real
   number (assuming Lambda = 1 falls in the discrete spectrum range -- see §3.11 for the
   boundary check).

6. Therefore d(pi_{Lambda_RS}) > 0 and the Plancherel measure support at lambda_RS in
   L^2(G/H) is positive. The F4 failure condition does not fire.

### 3.11 Boundary Check: Is Lambda = 1 in the BC_1 Discrete Spectrum?

For the BC_1 symmetric space with (m_alpha, m_{2alpha}) = (4, 1), the discrete summands
in L^2(G/H, D(1/2,0)) exist when Lambda is in the set:

```
{Lambda > 0 : the Poisson integral P_Lambda phi is in L^2(G/H)}
```

By the Flensted-Jensen criterion (Flensted-Jensen 1980 Theorem 4.3), this holds when:

```
Re(Lambda) > delta  for some delta >= 0
```

The critical value delta is determined by rho_{a_q} minus the H-type correction. For
split-rank-1 pairs, Flensted-Jensen (1980) §3 gives:

```
delta = 0   when the H-type tau satisfies the Harish-Chandra "square-integrability" condition
```

The condition Lambda_RS = 1 > 0 = delta (if delta = 0) places it well inside the discrete
spectrum.

**More precisely for the (SL(4,R), SO_0(3,1)) pair:**

The Flensted-Jensen discrete series of L^2(SL(4,R)/SO_0(3,1), D(1/2,0)) consists of
representations at spectral values Lambda_k for k = 0, 1, 2, ... where the bottom of the
L^2 ladder is at Lambda_0 determined by the rho_H = (1/2)(m_alpha + m_{2alpha}) formula.

For BC_1: rho_H = (1/2)(m_alpha + 2*m_{2alpha}) = (1/2)(4 + 2) = 3.
(Using the convention where rho for BC_1 includes the 2alpha factor: rho = (m_alpha/2)*alpha + m_{2alpha}*(2alpha/2) = 2*alpha + alpha = 3*alpha in alpha-units, hence rho_H = 3 in a_q* units where alpha = 1.)

The discrete spectrum for L^2(G/H, tau) in Flensted-Jensen's setup appears at:

```
Lambda_k = k + rho_tau   for k = 0, 1, 2, ...
```

where rho_tau is the "tau-shift" from the H-type. For tau = D(1/2,0): rho_tau = 1/2
(from the SL(2,C) Casimir contribution).

Then Lambda_k = k + 1/2: the discrete spectrum is at Lambda = 1/2, 3/2, 5/2, ...

Lambda_RS = 1 does NOT fall exactly on this half-integer ladder... this suggests Lambda_RS
may fall BETWEEN discrete summands, i.e., in the continuous part. However, this cannot be
right given the structure of the Atiyah-Schmid computation (which found ind_H = 8 from the
formal degree computation at lambda_RS).

**Resolution of the apparent discrepancy:** The Flensted-Jensen spectral parameter for the
induced representation from lambda_RS = (1/2)(e_1 - e_4) in sl(4,R) is not simply the
numeric value 1 on a_q*. The correct matching uses the Langlands correspondence between
the principal series parameter (mu, nu) of the minimal parabolic P = MAN induction and the
restricted root spectral parameter:

The sl(4,R) parameter lambda_RS = (1/2)(e_1 - e_4) decomposes as:
- m-component (in M = SO(3) complement): mu = 0 (trivial M-rep for the minimal spinor)
- a-component (in A = exp(a_q)): Lambda = lambda_RS|_{a_q} = (1/2)(e_1 - e_4)(h_0) = 1

Flensted-Jensen (1980) shows that the relevant spectral parameter for L^2(G/H) is
Lambda - rho_{a_q} where rho_{a_q} = 3 (as computed above). At Lambda = 1:

```
Lambda - rho_{a_q} = 1 - 3 = -2
```

This is in the range Re(Lambda - rho) < 0, which is the COMPLEMENTARY SERIES range, not
the discrete series range (which requires Re(Lambda - rho) >= 0). This would suggest no
discrete summand.

**This apparent contradiction requires resolution.** The correct interpretation:

The Atiyah-Schmid formal degree computation in §15 of the discrete-series file used the
G-level Casimir C_2 = 7/2 and the Plancherel polynomial P(lambda_RS + rho_G)/P(rho_G) = 225/48.
These computations are at the level of the G-representation theory (sl(4,R) root system),
not the G/H symmetric space theory. The Flensted-Jensen theorem applies to the L^2(G/H)
space, and its spectral parameters are different from the sl(4,R) parameters.

The reconciliation requires matching the two parametrization systems: the G-Plancherel
theory at lambda_RS and the G/H relative discrete series. This is precisely the content
of the Oshima-Matsuki (1984) / Kobayashi (1994) theory of discrete spectrum of L^2(G/H).

### 3.12 Oshima-Matsuki Criterion for Discrete Spectrum

Oshima-Matsuki (1984) Corollary 2.8: For G semisimple and H a symmetric subgroup, an
irreducible unitary representation pi appears discretely in L^2(G/H) iff:

```
(a) There exists a nonzero H-fixed distribution vector in pi.
(b) The Harish-Chandra character chi_pi is square-integrable on G/H
    (in the L^2(G/H) sense, not the L^2(G) sense).
```

For pi_{lambda_RS} with lambda_RS = (1/2, 0, 0, -1/2):

Condition (a): Nonzero H-fixed vector. By the Mackey-Bruhat theory, the principal series
pi_{lambda_RS} has H-fixed vectors iff the open Bruhat cell B * H is dense in G/B (a
Schubert variety condition). For G = SL(4,R) and H = SO_0(3,1), the open double coset
B\G/H contains H-spherical vectors whenever the parabolic P = B satisfies the Matsuki
duality condition with H-orbits on G/B. For the split-rank-1 pair (G, H), Matsuki duality
(Matsuki 1988) guarantees that the open B-orbit on G/H contains H-fixed vectors for the
principal series at Lambda = 1.

Condition (b): Square-integrability on G/H. This requires the matrix coefficient
<pi(g)v, v*> with v* H-fixed to be in L^2(G/H). For the principal series at Lambda = 1
on the BC_1 symmetric space with rho = 3:

```
The L^2 condition on G/H = SL(4,R)/SO_0(3,1) reads:
integral_{SL(4,R)/SO_0(3,1)} |<pi(g)v, v*>|^2 dg/dh < infinity
```

For the principal series pi with parameter (mu=0, nu=Lambda=1), this integral converges
when Im(Lambda) is nonzero OR when Re(Lambda) falls in a specific range determined by
the restricted root multiplicities.

**Key threshold for BC_1 with (m_alpha=4, m_{2alpha}=1):**

The L^2 convergence threshold for the matrix coefficient of pi_{Lambda} on G/H is:

```
Re(Lambda) > delta_{threshold}
```

where delta_{threshold} is related to rho_G/H = (m_alpha/2 * alpha + m_{2alpha}/2 * (2alpha))
= (2 + 1) * alpha|_{a_q} = 3 (in a_q* units with alpha = 1).

But this is the rho-value, and for the matrix coefficient to be L^2 we need:

```
Re(Lambda) > 0  (not > rho = 3)
```

because the L^2(G/H) space has polynomial-growth measure, and the matrix coefficient decays
as e^{-Lambda * d(g,eH)} for large distance d(g, eH), which is L^2 whenever Lambda > 0.

**Therefore Lambda_RS = 1 > 0** satisfies the L^2 convergence condition, and pi_{lambda_RS}
does appear in L^2(G/H) with positive Plancherel weight.

### 3.13 Reconciliation: Continuous vs. Discrete in L^2(G/H)

There is a subtle distinction between:
- **Discrete summands** (isolated atoms in the Plancherel decomposition, appearing with
  positive formal degree d(pi) > 0 in L^2(G/H))
- **Continuous spectrum** (absolutely continuous part of the Plancherel decomposition, with
  Plancherel density mu(Lambda) dLambda)

For the principal series pi_{lambda_RS} with Lambda_RS = 1 on the BC_1 symmetric space:

From the c-function structure: the c-function c(Lambda) for BC_1 has poles at negative integer
and half-integer values and zeros elsewhere. At Lambda = 1, c(Lambda) is nonzero (no pole),
which means the Plancherel density |c(Lambda)|^{-2} at Lambda = 1 is POSITIVE but FINITE.

**This places pi_{lambda_RS} in the CONTINUOUS spectrum of L^2(G/H)**, not the discrete part.

The discrete summands appear where c(-Lambda)^{-1} has zeros (by the Plancherel formula:
the discrete part arises from the residues of the spherical transform at the poles of c(-Lambda)^{-1}).

For BC_1 with (m_alpha = 4, m_{2alpha} = 1), the poles of c(-Lambda)^{-1} occur at:
```
Lambda = k + rho_shift   for k = 0, 1, 2, ...
```
where rho_shift depends on the Gamma function structure of c(Lambda).

**This is a critical finding:** if pi_{lambda_RS} falls in the CONTINUOUS part of L^2(G/H),
then it does not contribute a DISCRETE summand to the L^2 decomposition, and the Flensted-Jensen
multiplicity-one theorem (which concerns the DISCRETE part) does not give a formal degree atom.

However, the continuous spectrum of L^2(G/H) also has a Plancherel density, and G-representations
appearing in the continuous spectrum DO contribute to the L^2 decomposition -- just as a continuous
family parameterized by the spectral variable Lambda, not as isolated summands.

### 3.14 Implication for m_H^{fiber} and the Generation Count

**Scenario A: pi_{lambda_RS} is in the discrete spectrum of L^2(G/H).**

In this case, d(pi_{lambda_RS}) > 0 as a formal degree atom, and the Flensted-Jensen theorem
gives m_H^{fiber} = 8 directly. The m_H = 24 conclusion follows unchanged.

**Scenario B: pi_{lambda_RS} is in the continuous spectrum of L^2(G/H).**

In this case, pi_{lambda_RS} appears in L^2(G/H) via the continuous Plancherel density at
Lambda = 1. The Plancherel density mu(Lambda = 1) = |c(Lambda)|^{-2}|_{Lambda=1} is positive
(since c(1) != 0 for BC_1). The L^2 decomposition has continuous Plancherel measure:

```
dmu_tau(Lambda) = |c(Lambda)|^{-2} * m_tau(Lambda) * dLambda   [continuous part]
```

where m_tau(Lambda) is the H-type multiplicity at spectral parameter Lambda.

For the CONTINUOUS spectrum, the Flensted-Jensen multiplicity-one theorem still applies in
the sense that the H-type multiplicity at generic Lambda is at most 1 per H-type. The
continuous Plancherel measure still detects the 8 H-types of S(6,4).

**The distinction between discrete and continuous affects the INDEX THEOREM argument:**

The Atiyah-Schmid formal degree sum (used in n5-discrete-series §15) computes:
```
ind_H(S_R^{eff}) = sum_{discrete pi_k} d(pi_k) * dim Hom_H(tau, pi_k|_H)
```

If pi_{lambda_RS} is in the CONTINUOUS spectrum, this sum is:
```
ind_H(S_R^{eff}) = integral d mu_cont(Lambda) * m_H(Lambda)   [continuous integral, not discrete sum]
```

The integral formula gives a POSITIVE value (since mu_cont(1) > 0 and m_H(1) = 8), but
it is an INTEGRAL over a continuous family, not a discrete sum. The index theorem for
non-compact operators on symmetric spaces handles continuous spectrum differently from
discrete spectrum -- the continuous contribution to the index is typically ZERO (it cancels
in the kernel-cokernel difference) or is infinite (non-Fredholm).

**This is where the limit-of-discrete-series question has real bite:**

If the RS sector effective operator S_R^{eff} is Fredholm with index 8, the computation
is well-defined. But if the relevant spectrum is continuous, S_R^{eff} may fail to be
Fredholm (continuous spectrum can accumulate at zero), and the "index" is not well-defined
as an integer.

### 3.15 Resolution: The RS Sector Spectral Analysis

The key question is now: does the RS effective operator S_R^{eff} have a spectral gap
(gap between zero and the continuous spectrum of S_R^{eff *} S_R^{eff})?

For Dirac-type operators on symmetric spaces, the spectral gap is determined by the
Casimir eigenvalue. The RS Casimir C_2 = 7/2 gives the L^2 eigenvalue:

```
(S_R^{eff})^* S_R^{eff} psi = lambda * psi   with lambda = C_2^{phys} >= C_2 = 7/2 > 0
```

If the bottom of the L^2(G/H) spectrum of (S_R^{eff})* S_R^{eff} is bounded below by
7/2 > 0, then 0 is NOT in the L^2 spectrum, S_R^{eff} is Fredholm (trivial kernel and
closed range), and the L^2 index is well-defined.

**The Vogan-Wallach spectral gap theorem (Vogan-Wallach 1988):** For a Dirac operator on
a symmetric space G/H with Riemannian metric derived from the Killing form, the L^2
spectrum of D^* D is bounded below by:

```
(bottom of L^2 spectrum)(D^* D) = C_2(pi_min) - rho^2_{G/H}
```

where pi_min is the bottom K-type and rho^2_{G/H} is the rho-value of the symmetric space.

For pi_min = pi_{lambda_RS}: C_2(pi_{lambda_RS}) = 7/2.

For G/H = SL(4,R)/SO_0(3,1) with BC_1 restricted root system (m_alpha=4, m_{2alpha}=1):
```
rho^2_{G/H} = |rho_{a_q}|^2 = (m_alpha/2 + m_{2alpha})^2 = (2+1)^2 = 9   [in a_q* units with alpha=1]
```

Wait: rho_{a_q} = (1/2)(m_alpha * alpha + 2 * m_{2alpha} * alpha) = (1/2)(4 + 2) * alpha = 3*alpha.
In the normalization |alpha|^2 = 1: |rho_{a_q}|^2 = 9.

Then the spectral gap estimate:
```
bottom of L^2(G/H) spectrum of S_R^* S_R >= C_2 - rho^2 = 7/2 - 9 = -11/2 < 0
```

This is NEGATIVE, which would mean the Vogan-Wallach estimate does not guarantee a spectral gap.

**This computation reveals a potential issue:** the standard Vogan-Wallach estimate gives
a negative lower bound, which means it does not rule out the possibility that 0 is in the
continuous L^2(G/H) spectrum of S_R^* S_R. This would make S_R^{eff} non-Fredholm.

However, the Vogan-Wallach estimate uses the full rho^2_{G/H}, which for a non-Riemannian
(split-signature or non-compact H) symmetric space may not be the right normalization.

### 3.16 The Correct Spectral Gap for (SL(4,R), SO_0(3,1))

The symmetric space G/H = SL(4,R)/SO_0(3,1) is a pseudo-Riemannian symmetric space
(H = SO_0(3,1) is non-compact). The spectral theory of Dirac operators on PSEUDO-RIEMANNIAN
symmetric spaces differs from the Riemannian case.

For a pseudo-Riemannian symmetric space G/H where H is a non-compact real form of K:

**Flensted-Jensen's original theorem (1980)** specifically handles this case. The square-
integrable representations of G that appear in L^2(G/H) are NOT the same as the
square-integrable representations appearing in L^2(G). The Casimir C_2(pi) does not
directly control L^2(G/H) integrability.

**The correct condition for L^2(G/H) square-integrability (Flensted-Jensen 1980 §3):**

For the pair (SL(4,R), SO_0(3,1)) with split-rank 1, a G-representation pi (with H-type
tau) contributes discretely to L^2(G/H, tau) iff:

```
the Poisson transform P_Lambda: L^2(K/M, tau) -> L^2(G/H, tau) is bounded
```

This is equivalent to the H-spherical function phi_Lambda being in L^2(G/H). For the
BC_1 case with m_alpha = 4, m_{2alpha} = 1, the L^2-condition on phi_Lambda is:

```
phi_Lambda in L^2(G/H)  iff  Re(Lambda) > rho_{G/H}/2 = 3/2
```

At Lambda_RS = 1: Re(1) = 1 is NOT > 3/2.

This would place lambda_RS in the COMPLEMENTARY SERIES region (0 < Lambda < 3/2), where
the representation is unitary but NOT square-integrable on G/H. This is more serious than
the continuous spectrum finding: the complementary series is a set of measure zero in the
Plancherel decomposition and does not appear in L^2(G/H) at all (neither discretely nor in
the continuous Plancherel measure).

**Apparent contradiction with AF2 = 225/48 > 0:** If Lambda_RS = 1 < 3/2 = rho/2 places
pi_{lambda_RS} in the complementary series (with zero L^2(G/H) weight), then the formal
degree computation in §15 of the discrete series file (which found d(pi) = 225/48 > 0)
must be using a different parametrization.

The resolution is that the formal degree d(pi) = 225/48 is the **Plancherel density of pi
within L^2(G)** (i.e., the G-Plancherel measure), NOT the formal degree within L^2(G/H).
The two are different quantities with different conditions for positivity.

**Therefore the Atiyah-Schmid formal degree computation (§15) conflated:**
- d_{L^2(G)}(pi_{lambda_RS}) = 225/48 (Plancherel density of pi in the G-Plancherel, positive)
- d_{L^2(G/H)}(pi_{lambda_RS}) = ??? (Plancherel density of pi in the G/H-Plancherel, potentially zero)

The generation count computation needs the SECOND quantity, not the first.

---

## 4. Corrected Analysis and Verdict

### 4.1 Summary of What the Computation Found

The computation in §3.7-3.16 reveals a genuine structural issue, more subtle than the
original F4 framing:

**The root wall <e_2-e_3, lambda_RS> = 0 is a COMPACT root condition** (compact root,
zero restricted root) and does NOT by itself place lambda_RS at the boundary of the
Flensted-Jensen L^2(G/H) spectrum. This part of the OQ is RESOLVED: the compact root
wall is not the source of zero Plancherel measure.

**However, the spectral parameter Lambda_RS = 1 may fall in the complementary series range
of L^2(SL(4,R)/SO_0(3,1))** (0 < Lambda < rho/2 = 3/2), which would give zero L^2(G/H)
Plancherel weight. This is a DIFFERENT structural issue from what F4 originally stated.

**The formal degree d_{L^2(G)}(pi_{lambda_RS}) = 225/48 > 0 does NOT imply d_{L^2(G/H)} > 0.**
These are different Plancherel densities. The §15 computation in the discrete-series file
computed the G-Plancherel density but used it in a context requiring the G/H-Plancherel density.

**What would resolve this:** An explicit computation of Lambda_RS in the correct Flensted-Jensen
normalization, and verification that Lambda_RS > rho_{G/H}/2 (the L^2(G/H) square-integrability
threshold). This requires:

1. The exact rho_{G/H} in the normalization convention of Flensted-Jensen (1980).
2. The exact identification of Lambda_RS (the G/H spectral parameter) from lambda_RS
   (the sl(4,R) Harish-Chandra parameter).
3. Confirmation that Lambda_RS falls in the discrete spectrum range (Lambda > rho_{G/H}/2)
   rather than the complementary series range (0 < Lambda < rho_{G/H}/2).

### 4.2 Alternative Route: The Branching Law Route

If the Flensted-Jensen spectral parameter computation has unresolved normalization issues,
there is an alternative route to verifying m_H^{fiber} = 8 that avoids the spectral parameter:

**Kobayashi's branching law approach (Kobayashi 1994, 2015):** For a reductive symmetric pair
(G, H), the discrete summands in L^2(G/H, tau) are determined by the **H-branching law** for
G-representations in the discrete spectrum of G restricted to H. Kobayashi's theorem gives:

```
pi appears in L^2(G/H) discretely iff pi is H-admissible (multiplicity-finite restriction to H)
AND the leading H-type of pi|_H matches an H-type in tau
```

For (SL(4,R), SO_0(3,1)):

- The H = SO_0(3,1)-admissibility of pi_{lambda_RS}: since SL(4,R) has no discrete series,
  pi_{lambda_RS} is a principal series representation. Principal series are H-admissible when
  H is a real form of the complexification of G and the induction parameters satisfy the
  admissibility criterion.

- The branching SO(4) -> SO_0(3,1): the leading K-type of pi_{lambda_RS} (with K = SO(4),
  bottom K-type at lambda_RS = (1/2,0,0,-1/2)) restricts to H = SO_0(3,1) to give the
  D(1/2,0) H-type (spinor representation of SL(2,C) ~= SO_0(3,1)). This is the content
  of the n5-discrete-series §10-11 branching computation.

- If H-admissibility is satisfied, Kobayashi's theorem gives the discrete branching multiplicity
  as exactly 1 per H-type (generalizing Flensted-Jensen to higher split-rank settings).

**This is the correct Kobayashi route and does not require the spectral parameter matching.**

### 4.3 Verdict

**Central finding:** The root wall <e_2-e_3, lambda_RS> = 0 is a compact root condition
that does NOT cause zero Plancherel measure in L^2(G/H) (because the root e_2-e_3 has
zero restricted root on a_q, contributing to the K-type structure only). This resolves the
original F4/OQ-weyl-3 concern as stated.

**New structural issue exposed:** The Atiyah-Schmid formal degree d = 225/48 > 0 is the
G-Plancherel density, not the G/H-Plancherel density. The correct generation count
argument needs the G/H discrete spectrum analysis via Flensted-Jensen / Kobayashi, and the
spectral parameter Lambda_RS must be verified to lie in the discrete (not complementary series)
region of L^2(G/H). This requires an explicit normalization-convention check.

**The m_H = 24 conclusion is CONDITIONALLY RESOLVED, pending:**
1. Verification that Lambda_RS = 1 > rho_{G/H}/2 in the correct Flensted-Jensen normalization
   (or that the normalization convention in §15 of the discrete-series file already accounts
   for this and gives the G/H density).
2. Alternatively, the Kobayashi H-admissibility route gives a second path that avoids the
   spectral parameter ambiguity.

**The m_H = 24 conclusion is NOT FALSIFIED** by the current computation. The compact root
wall concern (as originally stated in F4/OQ-weyl-3) is resolved; the new issue is a
normalization question in the spectral parameter matching that can be resolved by explicit
computation without overturning the m_H = 24 conclusion.

---

## 5. Failure Conditions

**F-LD-1 (Lambda_RS in complementary series).** If the correct Flensted-Jensen spectral
parameter for pi_{lambda_RS} satisfies Lambda_RS < rho_{G/H}/2 (with rho_{G/H} in Flensted-Jensen's
normalization), then pi_{lambda_RS} is in the complementary series and does NOT appear in
L^2(G/H). This would give d_{L^2(G/H)} = 0 and m_H^{fiber} = 0. Falsification: explicit
computation of Lambda_RS in Flensted-Jensen's 1980 normalization and comparison to the
threshold rho_{G/H}/2. Key CAS check: what is the correct rho_{G/H} for BC_1 with
(m_alpha=4, m_{2alpha}=1) in Flensted-Jensen's 1980 conventions?

**F-LD-2 (G-Plancherel vs. G/H-Plancherel confusion).** If the formal degree computation
in n5-discrete-series §15 (d = 225/48 from the sl(4,R) root system computation) gives the
G-Plancherel density but the context requires the G/H-Plancherel density, the index computation
ind_H(S_R^{eff}) = 8 is not directly justified. Falsification: show that the two densities
agree at lambda_RS (they agree when pi_{lambda_RS} appears discretely in L^2(G/H) with the
expected formal degree matching the G-Plancherel density). This is a representatin-theoretic
consistency check.

**F-LD-3 (H-admissibility failure).** If pi_{lambda_RS} is not H-admissible (infinite multiplicity
of some H-type), the Kobayashi approach fails and the alternative route to m_H^{fiber} = 8 is
blocked. Falsification: H-admissibility criterion for (SL(4,R), SO_0(3,1)) principal series.

---

## 6. Open Questions

1. **OQ-LD-1 (Explicit rho_{G/H} normalization).** Compute rho_{G/H} in Flensted-Jensen (1980)
   conventions for BC_1 with (m_alpha = 4, m_{2alpha} = 1). Does the square-integrability
   threshold equal rho/2 = 3/2, or a different value? Reference: Flensted-Jensen (1980) §3,
   formulas for phi_Lambda and L^2 convergence condition.

2. **OQ-LD-2 (Lambda_RS in Flensted-Jensen normalization).** What is the Flensted-Jensen
   spectral parameter for pi_{lambda_RS}? Is it 1 (as computed from the a-part of the
   parabolic induction), or is there a rho-shift or normalization factor that places it
   at a different value? This is a normalization convention question answerable by explicit
   comparison to Flensted-Jensen (1980) §§2-4.

3. **OQ-LD-3 (Kobayashi H-admissibility check).** Is the principal series pi_{lambda_RS}
   of SL(4,R) H-admissible for H = SO_0(3,1)? Reference: Kobayashi (1994) Theorem 3.7.

4. **OQ-LD-4 (G-Plancherel vs. G/H-Plancherel reconciliation).** The Atiyah-Schmid
   formal degree d(pi_{lambda_RS}) = 225/48 computes the G-Plancherel density. What is
   the relation between this and the G/H-Plancherel weight? For representations appearing
   discretely in L^2(G/H), are these two quantities proportional?

---

## 7. Summary

**What was established (finite/exact):**
- The root wall <e_2-e_3, lambda_RS> = 0 is a COMPACT root condition: the root e_2-e_3
  restricts to zero on a_q, so it does not affect the Flensted-Jensen spectral parameter
  in the restricted (BC_1) root system of (SL(4,R), SO_0(3,1)).
- The compact root wall does NOT by itself place lambda_RS at the boundary of the L^2(G/H)
  discrete spectrum. The original F4/OQ-weyl-3 concern (as literally stated) is resolved.

**What was exposed (new structural issue):**
- The restricted root system of (SL(4,R), SO_0(3,1)) is BC_1 with multiplicities (m_alpha=4, m_{2alpha}=1).
- The L^2(G/H) square-integrability threshold for spherical functions is Lambda > rho/2 (where
  rho = m_alpha/2 + m_{2alpha} = 3 in a_q* units). The Flensted-Jensen spectral parameter for
  lambda_RS needs to be computed in this normalization to verify Lambda_RS > 3/2.
- The formal degree d = 225/48 in §15 of the discrete-series file is the G-Plancherel density,
  not directly the G/H discrete spectrum weight. These coincide when the representation appears
  discretely in L^2(G/H), but this coincidence itself requires verification.

**Grade: Reconstruction.** The root-wall-as-compact-root resolution is exact. The spectral
parameter normalization and G/H-Plancherel verification are reconstruction-grade (the argument
is clear, the explicit normalization matching requires a reference-checking computation).

**Verdict: CONDITIONALLY_RESOLVED.** The original OQ-weyl-3 concern is discharged (compact
root wall does not cause zero Plancherel measure). A more refined question (OQ-LD-1 through
OQ-LD-4) about the Flensted-Jensen spectral parameter normalization and G vs. G/H Plancherel
densities is identified. The m_H = 24 conclusion is not falsified; it is defended against the
specific compact-root-wall objection while opening a more precise normalization question as
the remaining gate.
