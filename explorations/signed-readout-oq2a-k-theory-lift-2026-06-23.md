---
title: "K-Theory Lift of Signed-Readout Integer-Index Recovery: Atiyah-Janich Theorem for the Family {R(x)}"
date: 2026-06-23
problem_label: "signed-readout-oq2a-k-theory-lift"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# K-Theory Lift of Signed-Readout Integer-Index Recovery

## 1. Problem Statement

The OQ2 result (`signed-readout-oq2-integer-index-2026-06-23.md`) established:

- **Z-grading theorem:** w: X -> Z forces R: E -> Z (integer readout).
- **Topological protection theorem:** connected deformation space T + continuity forces
  R_{phi(t)}(e_max) constant on connected components of T.
- **Integer-Index Recovery theorem:** combining both gives a Z-valued, deformation-
  invariant index Ind(G_R, C) = Ind^+ - Ind^- for each connected component C of T.

OQ2 identified the remaining lift as OQ2-A:

> "Can the PN/Jordan framework produce invariants in K^0(T) (the K-theory of the
> deformation space) rather than just Z? This would be the abstract generalization of
> the Atiyah-Singer index family theorem."

The specific formulation of this problem is:

**OQ2-A:** Given the family of operators {R(x)} parametrized by observer states x in a
compact space X (the "observer state space"), does the integer-index Ind(G_R, x) lift
from a locally-constant Z-valued function on X to a class in K^0(X) or KO^0(X)?

More precisely, there are three sub-questions:

1. **Family formulation:** What is the family of Fredholm operators {R(x)}_{x in X}?
2. **Atiyah-Janich statement:** How does the Atiyah-Janich theorem apply to this family?
3. **K^0 vs KO^0:** Does the class land in K^0(X) (complex K-theory) or KO^0(X) (real
   K-theory), given the quaternionic structure of S = H^{64} in GU?

The answer determines whether the signed-readout framework produces a richer invariant
than just the integer count -- whether it classifies observer-dependent families of
indices in K-theory.

---

## 2. Established Context

Prior results this builds on:

- **OQ2 (CONDITIONALLY_RESOLVED):** Integer-index recovery via Z-grading + topological
  protection. PN/Jordan split gives Ind = Ind^+ - Ind^- in Z. GW axial charge
  Q_A = n_+ - n_- worked out explicitly. GU ind_H(D_GU) = 24 fits as monotone case.
  File: `signed-readout-oq2-integer-index-2026-06-23.md`.

- **Atiyah-Janich theorem (classical):** The space of Fredholm operators on a Hilbert
  space H, denoted Fred(H), represents K^0 in the sense:
  [X, Fred(H)] = K^0(X)
  for any compact Hausdorff space X, where [X, Fred(H)] is the set of homotopy classes
  of continuous maps X -> Fred(H). The index map ind: Fred(H) -> Z is the component
  map of the classifying space.

- **GU discrete-series ind_H(D_GU) = 24** (n5-discrete-series-gl4r §§12-19,
  CONDITIONALLY_RESOLVED): ind_H is computed via Atiyah-Schmid formal-degree sum;
  all multiplicities are non-negative integers; S = H^{64} has quaternionic structure.

- **VZ evasion (EVADED):** D_GU is a Dirac-type operator on Y^14 (non-compact, split-
  signature (9,5)); Fredholm on L^2 spaces by the discrete-series mechanism.

- **Sp(64) gauge group:** pseudoreal structure J: S -> S with J^2 = -1; S = H^{64} is
  a quaternionic Hilbert space.

- **OQ1 split-rank = 1 (VERIFIED):** Flensted-Jensen criterion met for
  SL(4,R)/SO_0(3,1).

---

## 3. The Family of Fredholm Operators {R(x)}

### 3.1 What x Parametrizes

In the signed-readout framework, an observer state x encodes:
- A section s_x: X^4 -> Y^14 (a choice of Lorentzian metric g_x on X^4),
- A gauge field A_x on the Sp(64) bundle P over Y^14,
- The resulting GU Dirac operator D_x = D_{A_x} on S = H^{64}.

The "observer state space" X is the space of GU data (section + gauge field) modulo
gauge equivalence:

```
X = { (s, A) : s in Gamma(Y^14 -> X^4), A in A(P) } / Gauge(P)
```

This is an infinite-dimensional space in general. For the K-theory lift we need X to
be compact, so we work with appropriate completions or finite-dimensional approximations.

**Key constraint:** For the signed-readout OQ2-A lift, the relevant space is the
connected component of the gauge-field moduli:

```
X = M^{GU}_0 = { A in A(P) : D_A has discrete L^2 spectrum on Y^14 } / Gauge(P)
```

This is the space where the Atiyah-Schmid discrete-series mechanism applies (the
operator D_A is Fredholm in the L^2-discrete-series sense).

### 3.2 The Operator Family

For each x in X = M^{GU}_0, define:

```
R(x) = D_x: dom(D_x) subset L^2(S) -> L^2(S)
```

This is a family of closed, densely defined operators on the quaternionic Hilbert space
L^2(Y^14, S) = L^2(Y^14, H^{64}).

**Fredholm property:** R(x) is Fredholm in the generalized (L^2-discrete-series) sense:
the kernel ker(R(x)) is finite-dimensional (by the Atiyah-Schmid theorem) and lies in
the discrete-series part of L^2.

More precisely, using the Plancherel decomposition:

```
L^2(Y^14, S) = integral_{SL(4,R)-hat} H_pi tensor Hom(S, V_pi) d mu(pi)
```

the operator D_x acts on each fiber H_pi x Hom(S, V_pi) with principal symbol c(xi).
The discrete-series contribution is:

```
L^2_disc(Y^14, S) = direct sum_{pi in disc(SL(4,R))} H_pi tensor Hom_K(tau, pi|_K)
```

and on this summand D_x is Fredholm with:

```
ind_H(D_x) = sum_{pi in disc} d(pi) * dim Hom_K(tau, pi|_K)
```

which equals 24 for the GU case (from the discrete-series computation).

### 3.3 The Record-Graph Readout as an Index Function

From the OQ2 framework: the integer-index recovery produces:

```
Ind(G_R, C) = R_{phi(t)}(e_max)  for t in connected component C of X
```

In the GU context:
- e_max = "all evidence accumulated from Y^14" (the full finalized evidence element),
- phi(x)(v) = d(pi_v) * dim Hom_K(tau_v, pi_v|_K) for discrete-series mode v at
  observer state x,
- Ind(x) = sum_v phi(x)(v) = ind_H(D_x).

The map x |-> Ind(x) = ind_H(D_x) is a locally constant Z-valued function on X (by
Atiyah-Janich stability). The K-theory lift asks: is there more structure than just a
Z-valued function?

---

## 4. The Atiyah-Janich Theorem for the Family {R(x)}

### 4.1 Classical Atiyah-Janich

The Atiyah-Janich theorem (Atiyah 1967, Janich 1965) states:

**Theorem (Atiyah-Janich):** Let H be a separable infinite-dimensional complex Hilbert
space. The space of Fredholm operators Fred(H) with the operator-norm topology is a
classifying space for complex K-theory:

```
pi_0(Fred(H)) = Z
[X, Fred(H)] = K^0(X)   for compact Hausdorff X
```

The index map ind: Fred(H) -> Z gives the component (hence pi_0 = Z). The full
K-theory class [f] in K^0(X) for f: X -> Fred(H) is the "index bundle" or "virtual
kernel bundle":

```
ind(f) = [ker f] - [coker f]  in K^0(X)
```

This is a class in the Grothendieck group K^0(X) = K(Vect_C(X)), the virtual complex
vector bundles on X.

### 4.2 Adaptation to the Signed-Readout Setting

**Setup:**
- Observer state space X (compact, Hausdorff -- see §4.4 for the compactification).
- Family R: X -> Fred(L^2(Y^14, S)) by x |-> D_x (the GU Dirac operator at state x).

**The Atiyah-Janich theorem applied to this family gives:**

```
ind(R) = [ker R] - [coker R]  in K^0(X)
```

where:
- [ker R] is the class of the "kernel bundle" (not an honest bundle in general, but a
  virtual bundle via stabilization),
- [coker R] is the class of the "cokernel bundle."

**Z-valued component:** The component of [ker R] - [coker R] in K^0(X) at the base
point x_0 maps to:

```
rank(ind(R)) at x_0 = ind_H(D_{x_0}) = 24  in Z = K^0(pt)
```

via the augmentation map eps: K^0(X) -> K^0(pt) = Z.

### 4.3 The Signed-Readout Connection

The PN/Jordan split in OQ2 gives:

```
Ind(G_R, x) = Ind^+(x) - Ind^-(x) = dim_H ker D_x - dim_H coker D_x
```

This is exactly the rank of the Atiyah-Janich class ind(R) at x:

```
rank[ind(R)](x) = rk[ker R] - rk[coker R] at x
```

The K-theory class ind(R) in K^0(X) is the **lifted** version of this Z-valued function.
The lifting from Z-function to K^0(X)-class is:

- If ker D_x has constant dimension for all x in X: ind(R) = [ker R] - [coker R] in
  K^0(X) is an honest virtual bundle.
- If ker D_x jumps: ind(R) is computed via the stabilization K^0(X) = [X, BU x Z]
  (in the complex case).

**Theorem (OQ2-A, K-theory lift, complex case).** Let X be a compact Hausdorff
observer state space and R: X -> Fred(L^2(Y^14, S_C)) be the continuous family of
complexified GU Dirac operators, where S_C = S tensor_H C is the complexification.
Then:

```
ind(R) in K^0(X)
```

is a well-defined class, whose reduction to K^0(pt) = Z under the map induced by any
x_0 in X is the signed-readout integer Ind(x_0) = Ind^+(x_0) - Ind^-(x_0).

**Proof.** Standard: the map R: X -> Fred(H_C) is continuous (by construction of D_x
from smooth gauge-field data, and continuity of the principal symbol). By Atiyah-Janich,
this continuous map represents a class [R] in [X, Fred(H_C)] = K^0(X). The class
ind([R]) = [ker R] - [coker R] (as a virtual bundle) is the index class. Augmenting
at any x gives ind_H(D_x) times (the rank of a complex line is 2 over R; but in H-
dimension, see §5). QED.

### 4.4 Compactification of the Observer State Space

The observer state space M^{GU}_0 is in general non-compact. To apply Atiyah-Janich,
we need X to be compact. Three options:

**(Option A) Section-energy compactification.** The GU variational principle E[s] =
integral |II_s|^2 selects a finite-energy component of section space. The Willmore
critical-point locus (Willmore sections on S^4 with K3-type X^4) is compact modulo
gauge (by the GU-analog of Uhlenbeck compactness for Yang-Mills). This gives a compact
moduli space X = M^{GU}_{Willmore}.

**(Option B) Topological-sector compactification.** Fix a topological sector (a class
in H^4(Y^14, Z) or the relevant cohomology group) and take X = M^{GU}_{top}(k) to be
the moduli within that sector. Under appropriate energy bounds, this is compact by
the GU analog of Donaldson compactness.

**(Option C) One-point compactification.** Take X = M^{GU}_0^+ (one-point
compactification), and define R(infty) = some fixed Fredholm operator. This gives a
class in K^0(X^+) = K-tilde^0(X^+) oplus Z, the reduced K-theory of the
one-point compactification.

For the statement of OQ2-A, Option C is the most abstract and avoids Uhlenbeck-type
compactness. We use X = X^+ below.

---

## 5. K^0(X) vs KO^0(X): The Quaternionic Structure

### 5.1 The Quaternionic Hilbert Space L^2(Y^14, S)

The spinor module S = H^{64} is a quaternionic Hilbert space. The GU Dirac operator
D_x is H-linear (commutes with right-H multiplication), as established in the discrete-
series computation (n5-discrete-series §12):

```
D_x (psi * q) = (D_x psi) * q    for all q in H
```

This means D_x is a Fredholm operator on the quaternionic Hilbert space H_H =
L^2(Y^14, H^{64}).

### 5.2 KSp-Theory for Quaternionic Hilbert Spaces

For a family of self-adjoint Fredholm operators on a quaternionic Hilbert space, the
appropriate K-theory is KSp (symplectic K-theory), which classifies families of
Fredholm operators on H-modules:

```
[X, Fred_H(H_H)] = KSp^0(X)
```

where Fred_H(H_H) is the space of H-linear Fredholm operators on the quaternionic
Hilbert space H_H.

**Bott periodicity for KSp:** KSp satisfies 8-fold Bott periodicity (real K-theory
with structure group Sp). In terms of KO:

```
KSp^0(X) = KO^4(X)    (by Bott periodicity shift)
```

since the symplectic group Sp corresponds to the 4th step in the Bott periodicity cycle.

**For H-linear Fredholm operators:**

```
ind_H: Fred_H(H_H) -> Z    (quaternionic index, counting H-lines in kernel - cokernel)
[X, Fred_H(H_H)] = KSp^0(X) = KO^4(X)
```

### 5.3 The K-Theory Class for {D_x}

**Theorem (OQ2-A verdict, quaternionic case).** The family {D_x}_{x in X} of H-linear
GU Dirac operators defines a class:

```
[{D_x}] in KSp^0(X) = KO^4(X)
```

via the Atiyah-Janich theorem for quaternionic Hilbert spaces. The augmentation map
sends this class to:

```
eps: KSp^0(X) -> KSp^0(pt) = Z
[{D_x}] |-> ind_H(D_{x_0}) = 24    for any x_0 in X
```

(The KSp^0(pt) = Z identification holds because dim_H(H^n) = n is integer-valued; the
quaternionic Grothendieck group of a point is Z.)

**Proof.** The map X -> Fred_H(H_H) by x |-> D_x is continuous (by the same argument
as the complex case: smooth gauge-field dependence of the operator). The Atiyah-Janich
theorem for quaternionic Hilbert spaces (the H-analog of the complex Atiyah-Janich
theorem; see Atiyah 1966 "K-theory and reality") gives [X, Fred_H(H_H)] = KSp^0(X).
The augmentation to a point sends the class to ind_H(D_{x_0}) = 24 (from the
discrete-series computation). QED.

### 5.4 Comparison: K^0(X) vs KO^0(X) vs KSp^0(X)

The three versions:

| Framework | Operator type | K-theory | Index group | GU context |
|---|---|---|---|---|
| Complex | C-linear Fredholm on H_C | K^0(X) | Z | D_x after complexification |
| Real | R-linear skew-adjoint Fredholm on H_R | KO^0(X) | Z | Not the natural setting |
| Quaternionic | H-linear Fredholm on H_H | KSp^0(X) = KO^4(X) | Z | **The correct GU setting** |

**Answer to OQ2-A:** The Z-grading integer-index class lifts to KSp^0(X) = KO^4(X),
not to K^0(X) or KO^0(X). The quaternionic structure of S = H^{64} (and H-linearity
of D_x) selects KSp, which equals KO^4 by Bott periodicity.

---

## 6. The PN/Jordan Split in K-Theory

### 6.1 The Abstract Statement

The OQ2 PN/Jordan split R = R_+ - R_- in Z lifts to K-theory as follows.

In the K-theory setting, the index class is:

```
ind({D_x}) = [ker D_x] - [coker D_x]  in KSp^0(X)
```

This is a virtual quaternionic bundle on X (an element of the Grothendieck group of
quaternionic vector bundles on X).

The PN/Jordan split corresponds to:

```
R_+^K = [ker D_x]   in KSp^0_+(X)   (the "positive part" = kernel bundle)
R_-^K = [coker D_x] in KSp^0_+(X)   (the "negative part" = cokernel bundle)
ind = R_+^K - R_-^K  in KSp^0(X)
```

where KSp^0_+(X) is the submonoid of virtual quaternionic bundles of non-negative rank.

**This is the K-theory lift of the PN/Jordan split:**

| OQ2 level | OQ2-A level (K-theory lift) |
|---|---|
| w_+(x) in N_0 | [ker D_x] in KSp^0_+(X) (quaternionic vector bundle) |
| w_-(x) in N_0 | [coker D_x] in KSp^0_+(X) (quaternionic vector bundle) |
| Ind^+ - Ind^- in Z | [ker D_x] - [coker D_x] in KSp^0(X) |
| Ind constant on C | ind class constant in each KSp^0 component |

The PN/Jordan split "Ind^+ = R_+(e_max) in N_0" lifts to a genuine quaternionic bundle
(not just a rank), and the deformation invariant is the K-class, not just an integer.

### 6.2 The GU Generation Count in K-Theory

In the GU case:
- All discrete-series contributions have phi(v)(x) in N_0 (R_- = 0 from OQ2 §9).
- The GU generation count is the MONOTONE case: all weights nonneg, Ind = Ind^+ = 24.

At the K-theory level, this means:
- [coker D_x] = 0 (trivial cokernel bundle, since D_x is injective in the relevant
  discrete-series sector by construction -- the cokernel is the kernel of D_x^*).
- [ker D_x] is a quaternionic vector bundle of H-rank 24 on X.

The K-theory class is:

```
ind({D_x}) = [ker D_x] - 0 = [ker D_x]  in KSp^0(X)
```

This is an actual quaternionic bundle (not just a virtual one), of H-rank 24.

**Physical meaning:** The kernel bundle [ker D_x] is the "generation bundle" -- its
fiber at x is the space of L^2 zero modes of D_{x} on Y^14. As x varies over the
observer state space X, these zero modes form a quaternionic vector bundle of rank 24
(3 generations x 8 H-lines/generation). The K-theory class [ker D_x] classifies how
this bundle twists over the observer state space.

If [ker D_x] is a trivial bundle (X-independent zero modes), then [{D_x}] = 24 [H] in
KSp^0(X) = KSp^0(pt) x K-tilde^0(X), and there is no additional K-theory information.
If [ker D_x] is non-trivial (the zero modes twist as x varies), then [{D_x}] contains
information beyond the integer 24.

---

## 7. The Atiyah-Janich Theorem Statement for the GU Family

### 7.1 Precise Statement

**Theorem (Atiyah-Janich for GU, OQ2-A).** Let X be a compact Hausdorff observer
state space (see §4.4 for the compactification). Let

```
R: X -> Fred_H(L^2(Y^14, H^64))
```

be the continuous family of H-linear GU Dirac operators x |-> D_x. Then:

**(a) K-theory class.** There is a well-defined class

```
[D] = ind(R) = [ker R] - [coker R]  in KSp^0(X) = KO^4(X)
```

given by the Atiyah-Janich map K^0_sp: [X, Fred_H(H_H)] -> KSp^0(X).

**(b) Integer reduction.** The augmentation eps: KSp^0(X) -> Z sends [D] to ind_H(D_{x_0})
for any base point x_0 in X. In the GU case this equals 24 (3 generations).

**(c) PN/Jordan correspondence.** The PN/Jordan split of the signed-readout theorem
corresponds to the Grothendieck decomposition:

```
[D] = [ker D] - [coker D]  in KSp^0(X) = KSp^0_+(X) / (bundle isomorphism)
```

The positive part [ker D] is the generation bundle (H-rank 24); the negative part
[coker D] = 0 in the GU monotone case.

**(d) Stability.** [D] is constant on connected components of [X, Fred_H(H_H)]; in
particular it is invariant under compact perturbations of D_x that do not change the
essential spectrum.

**(e) K-theory vs Z.** The class [D] in KSp^0(X) contains MORE information than the
integer ind_H(D_{x_0}) = 24 when X is not a point: the difference is the reduced
K-theory K-tilde-Sp^0(X), which classifies the non-trivial twisting of the generation
bundle over observer state space.

### 7.2 The K^0 vs KO^4 Identification

The identification KSp^0(X) = KO^4(X) comes from Bott periodicity. For a finite CW
complex X:

```
KO^n(X) has period 8 in n
KO^0(X) = real K-theory (structure group O)
KO^4(X) = symplectic K-theory (structure group Sp) = KSp^0(X)
```

The Bott periodicity sequence gives KO^4 = KSp^0 as the 4th step. For X = pt:

```
KO^0(pt) = Z, KO^1(pt) = Z/2, KO^2(pt) = Z/2, KO^3(pt) = 0,
KO^4(pt) = Z, KO^5(pt) = 0,   KO^6(pt) = 0,   KO^7(pt) = 0.
```

So KSp^0(pt) = KO^4(pt) = Z, consistent with ind_H counting H-lines (integer-valued).

The choice KSp^0(X) = KO^4(X) rather than K^0(X) (complex) or KO^0(X) (real) is
dictated by the quaternionic structure of S = H^{64}. This is the first firm answer to
the "K^0 or KO^0" question in OQ2-A: **neither -- the correct answer is KO^4 = KSp^0.**

---

## 8. Application to the Signed-Readout Framework

### 8.1 The Lifted Signed-Readout Theorem

The OQ2 signed-readout framework (integer-index recovery) lifts as follows.

**OQ2 level (Z-valued invariant):**
```
Ind(G_R, C) = Ind^+ - Ind^- in Z
```
a locally-constant integer function on connected components of X.

**OQ2-A level (KSp^0(X)-valued invariant):**
```
Ind_{KSp}(G_R, X) = [ker R] - [coker R] in KSp^0(X)
```
a virtual quaternionic bundle on X.

The OQ2-A class contains OQ2 as a shadow:

```
eps(Ind_{KSp}) = Ind in Z = KSp^0(pt)
```

When X is connected:

```
Ind_{KSp} in KSp^0(X) = Z oplus K-tilde-Sp^0(X)
```

and the OQ2 integer is the Z-component; the K-tilde-Sp^0(X) component is new
information from the K-theory lift.

### 8.2 When is the Lift Trivial?

The lift from Z to KSp^0(X) is trivial (carries no additional information) when:

```
K-tilde-Sp^0(X) = 0
```

This happens for example when X is contractible (homotopy type of a point). In the
GU case, if the moduli space M^{GU}_0 is contractible (as would follow from a unique
GU vacuum on K3-type X^4 up to gauge), the lift is trivial and the K-theory class is
just the integer 24 sitting in Z = KSp^0(pt).

When the lift is non-trivial (K-tilde-Sp^0(X) != 0), the generation bundle [ker D_x]
twists over the observer state space, encoding additional topological information about
how the zero modes transform as the observer changes state.

### 8.3 Physical Interpretation of the K-Class

The K-theory class [ker D_x] in KSp^0(X) is a quaternionic vector bundle of H-rank 24
over the observer state space X. Its fibers at different x in X are:

```
fiber at x = ker D_x|_{L^2_disc}  (the discrete-series zero modes of D_x)
             = 24-dimensional H-vector space (3 generations x 8 H-lines)
```

As x varies (observer changes gauge field / section), the zero modes can mix. The
K-theory class records whether this mixing is topologically non-trivial (i.e., whether
the bundle [ker D_x] is a non-trivial quaternionic bundle over X).

Physical cases:
- **Trivial class:** All observers see the same 24 zero modes (same generation structure
  regardless of gauge field choice). This is the case if the gauge field space is
  contractible (single topological sector).
- **Non-trivial class:** The generation structure (which H-lines are in the kernel)
  rotates as the observer changes state. This would manifest as an observer-dependent
  generation mixing -- a potentially observable effect.

The non-trivial classes are classified by K-tilde-Sp^0(X), which for X = S^n gives:

```
K-tilde-Sp^0(S^n) = KO^4(S^n):
n=0: Z, n=1: 0, n=2: 0, n=3: Z, n=4: Z, n=5: Z/2, n=6: Z/2, n=7: 0
```

(from the exact sequence of Bott periodicity).

---

## 9. The Z-Grading / PN-Split Result in KSp^0(X)

### 9.1 Does the Z-Grading Lift?

In OQ2, the Z-grading theorem says: w: X_generators -> Z forces Ind in Z.

In OQ2-A: the weight function w(x)(v) = d(pi_v) * dim Hom (from OQ2 §9) is N_0-valued
(positive integers). The "Z-grading" at the K-theory level is the condition that the
weight function takes values in N_0 = KSp^0_+(pt), i.e., represents genuine (non-
virtual) quaternionic vector bundles.

**Answer:** Yes, the Z-grading lifts. Since all GU discrete-series multiplicities are
in N_0, the index class lies in:

```
ind({D_x}) = [ker D_x] in KSp^0_+(X) subset KSp^0(X)
```

(the class of an actual quaternionic bundle, not a virtual bundle). This is the lift
of "Ind^+ - 0 = Ind^+" to the K-theory level.

### 9.2 Does the PN-Split Lift?

In OQ2, the PN/Jordan split R = R_+ - R_- in Z lifts to:

```
ind = [ker D] - [coker D]  in KSp^0(X)
```

Each summand is an element of the positive part KSp^0_+(X).

For the GU monotone case (R_- = 0, [coker D] = 0):

```
ind = [ker D]  in KSp^0_+(X)  (an actual quaternionic bundle of H-rank 24)
```

For a non-monotone case (like the GW axial charge, with both ker and coker non-trivial):

```
ind = [ker D] - [coker D]  in KSp^0(X)  (a virtual quaternionic bundle)
```

The PN-split in Z (Ind = Ind^+ - Ind^-) corresponds to the Grothendieck split in K-theory
(ind = [ker D] - [coker D]). This is the "K-theory lift of the PN/Jordan decomposition."

### 9.3 Summary: The Lifting Diagram

```
OQ1 (record-graph)            OQ2 (Z-grading)          OQ2-A (K-theory lift)
-----------------------        -----------------        ----------------------
G_R = (V, E_causal, lambda)    w: X -> Z                w: X -> N_0
R = sum lambda(v)              Ind = sum w(v) in Z      ind = [ker D] in KSp^0(X)
PN split: Ind = Ind+ - Ind-    Ind = Ind+ - Ind- in Z   ind = [ker D] - [coker D] in KSp^0
protected by Atiyah-Janich Z   protected by pi_0(Fred)   protected by [X, Fred_H] = KSp^0
```

---

## 10. Explicit Failure Conditions

The following conditions would falsify or downgrade the OQ2-A result:

**F1: D_x is not H-linear for all x in observer state space.**
If the Dirac operator D_x is not H-linear (e.g., if the gauge connection breaks the
quaternionic structure of S = H^{64}), then the correct K-theory is K^0 (complex) or
KO^0 (real), not KSp^0. Falsification: exhibit a gauge field A_x such that D_x does not
commute with right-H multiplication. (This would require A_x to break the Sp(64)
structure group to a subgroup not respecting the H-module structure.)

**F2: Fred_H(L^2(Y^14, H^64)) does not classify KSp^0.**
The H-analog of Atiyah-Janich requires that Fred_H(H_H) (Fredholm operators on a
quaternionic Hilbert space) classifies KSp^0. This holds for compact complex H but
may need care for the non-compact L^2(Y^14, H^64) (infinite-dimensional, non-compact
base Y^14). Falsification: show that Fred_H of the relevant L^2 space does not satisfy
[X, Fred_H] = KSp^0(X) for compact X.

**F3: The observer state space X is not compact (or not compactifiable).**
The Atiyah-Janich theorem requires X to be compact Hausdorff. If the GU moduli
M^{GU}_0 has no natural compactification preserving the Fredholm family property
(analogous to the failure of Uhlenbeck compactness for non-self-dual Yang-Mills), then
the K-theory class is not well-defined globally. Falsification: exhibit a sequence of
gauge fields A_n in M^{GU}_0 with no convergent subsequence (even after gauge
transformation and passage to an appropriate topology).

**F4: The kernel bundle [ker D_x] is not locally constant in H-rank.**
If ind_H(D_x) jumps as x varies within a connected component of X (due to non-
Fredholmness of D_x for some x), the K-theory class is not well-defined as a virtual
bundle. Falsification: exhibit x in M^{GU}_0 where D_x is not Fredholm in the L^2-
discrete-series sense (the essential spectrum of the fiber Dirac operator touches zero).

**F5: K-tilde-Sp^0(X) is trivial for the physical X.**
If the moduli space X = M^{GU}_0^+ has K-tilde-Sp^0(X) = 0, the K-theory lift
contains no additional information beyond the Z-valued integer count. This would make
OQ2-A formally true (the lift exists) but physically vacuous. Confirmation (rather than
falsification): a positive computation of K-tilde-Sp^0(X) for the GU moduli space.

**F6: Bott periodicity identification KSp^0 = KO^4 breaks for the relevant spaces.**
The identification KSp^0(X) = KO^4(X) holds for finite CW complexes by Bott periodicity.
If X is an infinite-dimensional space (the full gauge field space, not a finite-
dimensional moduli), the identification may require care (use of Kuiper's theorem for
contractibility of U(H_H), or an appropriate direct-limit construction). Falsification:
exhibit an infinite-dimensional X for which [X, Fred_H] != KO^4(X).

---

## 11. Verdict and Open Questions

### 11.1 Verdict

**Verdict: CONDITIONALLY_RESOLVED at reconstruction grade.**

**What was established:**

1. **Atiyah-Janich for quaternionic Hilbert spaces (reconstruction):** The family
   {D_x}_{x in X} of H-linear GU Dirac operators defines a class

   ```
   ind({D_x}) = [ker D_x] - [coker D_x]  in KSp^0(X) = KO^4(X)
   ```

   via the quaternionic Atiyah-Janich theorem [X, Fred_H(H_H)] = KSp^0(X).

2. **Correct K-theory: KSp^0 = KO^4, not K^0 or KO^0 (reconstruction).** The
   quaternionic structure of S = H^{64} and H-linearity of D_x select KSp^0 over
   the complex or real alternatives. The Bott periodicity identification KSp^0 = KO^4
   places the generation-count index at the 4th step of KO-theory.

3. **PN/Jordan lift to KSp^0 (reconstruction):** The OQ2 PN/Jordan decomposition
   Ind = Ind^+ - Ind^- in Z lifts to ind = [ker D] - [coker D] in KSp^0(X). The
   GU monotone case (R_- = 0) gives [ker D] as an actual quaternionic bundle of H-
   rank 24 (the "generation bundle" over observer state space).

4. **Integer reduction (reconstruction):** The augmentation eps: KSp^0(X) -> Z gives
   eps(ind) = 24 for the GU family, recovering the generation count as the rank of the
   K-theory class. OQ2's integer index is the shadow of the K-class at a point.

5. **GU generation bundle (reconstruction, tentative):** The kernel bundle [ker D_x]
   is a quaternionic bundle of H-rank 24 over the GU moduli; its topological complexity
   is classified by K-tilde-Sp^0(X), which is the new information in the lift beyond
   the integer count.

**Grade:** Reconstruction. The formal argument is complete at the level of citing the
relevant theorems (Atiyah-Janich for quaternionic Hilbert spaces, Bott periodicity,
Grothendieck group construction). The gaps are: (a) verification that Fred_H(L^2(Y^14,
H^64)) classifies KSp^0 in the non-compact-base setting; (b) compactification of the
GU moduli; (c) explicit computation of K-tilde-Sp^0(X) for the physical X.

### 11.2 Open Questions

**OQ2-A-i (KSp^0 for non-compact base):** Does the Atiyah-Janich classifying theorem
for Fred_H extend from compact manifold bases to the non-compact Y^14 base? The
standard Atiyah-Janich proof uses the compact base of the Hilbert space (compactness
of the index bundle over X), not of the base manifold. But L^2(Y^14, H^64) with non-
compact Y^14 introduces subtleties in the L^2 Fredholm theory. Expected answer: yes,
via the discrete-series L^2 space L^2_disc (which is a direct sum of finite-multiplicity
summands, hence behaves like a countable direct sum of finite-dimensional spaces).

**OQ2-A-ii (Non-trivial generation bundle):** Is the generation bundle [ker D_x] a
non-trivial quaternionic bundle over the GU moduli space? Equivalently, is
K-tilde-Sp^0(M^{GU}_0) non-zero? This would require computing the topology of the
gauge field moduli (an analogue of the Donaldson-Thomas theory for the GU Yang-Mills
functional on Y^14). This is a deep open problem, analogous to the instanton moduli
in 4D Yang-Mills.

**OQ2-A-iii (KO^4 interpretation of the physical GU 4D theory):** The KO^4
identification points to the 4th Bott period. In the physical 4D theory (after section
pullback X^4 -> Y^14), KO^4(X^4) = KO^4 of the spacetime. For X^4 = R x K3:

```
KO^4(R x K3) = KO^4(K3) = ?
```

This is a computation in the KO-theory of K3 surfaces, which is known in principle
but not computed here. The answer would give the number of inequivalent generation
bundles on the K3-type GU background.

**OQ2-D (updated):** The original OQ2-D asked for (a) an explicit record-graph G_R^{GU}
and (b) connectivity of T^{GU}. The K-theory lift adds: (c) computation of
K-tilde-Sp^0(T^{GU}) to determine whether the generation bundle is trivial or twisted.

---

## 12. Connection to Prior Results

**Connection to OQ2:** The OQ2 integer-index recovery is the KSp^0(pt) shadow of the
OQ2-A KSp^0(X) class. Both are CONDITIONALLY_RESOLVED; OQ2-A provides strictly more
structure.

**Connection to discrete-series ind_H = 24:** The 24 is eps(ind({D_x})) for any base
point x -- the augmentation to a point. The K-theory class ind({D_x}) in KSp^0(X)
is the "family version" of this number, valid for all x simultaneously.

**Connection to VZ evasion:** VZ evasion requires D_x to be a well-posed Fredholm
operator for all x in X. The Fredholm property of D_x is prerequisite for the Atiyah-
Janich theorem to apply. VZ evasion (EVADED, reconstruction) is therefore a necessary
condition for OQ2-A; the implication runs: VZ evasion => D_x Fredholm => Atiyah-Janich
applies => OQ2-A K-theory class exists.

**Connection to OQ3b-c (discrete-series):** The H-linearity established for OQ3b (the
RS block index = 8 being H-linear) is the same H-linearity that forces D_x into
Fred_H, hence into the KSp^0 classification. The two results are consistent and
mutually reinforcing.

**Connection to Sp(64) anomaly cancellation:** Sp(64) is anomaly-free (n_L - n_R = 0,
pseudoreal; pi_{15}(Sp) = Z, no global anomaly). The KSp^0 classification is
consistent with Sp(64) structure: symplectic K-theory (KSp) is the natural home for
families of operators with symplectic (pseudoreal) symmetry, matching Sp(64) exactly.
The anomaly cancellation can be re-read as: the KSp^0 class of the trivial (constant)
family is zero (no anomaly), and the non-trivial classes are the anomaly-free
representations.
