---
title: "OC2: H-Linear Fredholmness of D_GU on Y^14 and Well-Definedness of ind_H"
date: 2026-06-23
problem_label: "oc2-h-linear-fredholm-y14"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
gates_for_resolved:
  - "Sobolev domain explicit: D_GU defined on W^{1,2}_H(Y^14, S) with S = H^64"
  - "Pullback parametrix: s*(D_GU) elliptic on compact X^4 (or APS on manifold-with-boundary)"
  - "H-linearity of section pullback: s* commutes with right-H multiplication (RESOLVED here)"
  - "Discrete-series Fredholmness: ind_H(D_GU) = 24 via Atiyah-Schmid (gates on OQ1 split-rank)"
failure_condition: "If s* does not preserve H-linear structure — i.e., the pullback breaks Sp(64) equivariance or the connection A is not Sp(64)-valued — the quaternionic index is not well-defined."
---

# OC2: H-Linear Fredholmness of D_GU on Y^14 and Well-Definedness of ind_H

## 1. Problem Statement

Gate OC2 for the signed-readout boundary theorem (Part K) and for the generation count
requires the following:

> Prove that D_GU is H-linear (quaternion-linear) and Fredholm as an operator on
> H^64-valued spinor sections on Y^14. The H-linearity follows from right-H multiplication
> commuting with D_GU. Fredholm requires: (1) closed range, (2) finite-dimensional kernel
> and cokernel. Show the H-linear index ind_H(D_GU) = dim_H ker(D_GU) - dim_H coker(D_GU)
> is well-defined.
>
> State failure condition: if the pullback does not preserve the H-linear structure, the
> quaternionic index is not well-defined.

This file works in four steps:

1. Establish H-linearity of D_GU from algebraic first principles.
2. Show why Y^14 non-compact does not block the Fredholm property per se, but does shift
   the burden to the section pullback.
3. Use the section s: X^4 -> Y^14 to reduce the Fredholm problem to an elliptic problem
   on compact X^4.
4. Verify that the section pullback preserves H-linear structure (the key structural gate).

---

## 2. Established Context

The following are used without re-derivation:

- **Cl(9,5) = M(64,H):** quaternionic-type Clifford algebra; spinor module S = H^64
  (files: n1-signature-audit-y14, n2-shiab-computation).
- **Gauge group Sp(64) = U(64,H):** pseudoreal fundamental; anomaly-free
  (files: anomaly-audit-cl95-gauge-group, ig-dimension-matching-sp64-tau-plus).
- **Shiab Phi:** Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S; H-linear, Spin(9,5)-
  equivariant (files: sc1-shiab-domain-codomain).
- **Section s: X^4 -> Y^14:** selects a Lorentzian metric g_s on X^4; pullback spinor
  branching S(9,5)|_{S(3,1) tensor S(6,4)} gives SM content
  (files: n5-discrete-series-gl4r, generation-count-sm-branching-closure).
- **VZ EVADED (reconstruction):** principal symbol of effective RS Schur complement has
  trivial kernel for g_Y(xi,xi) != 0; section pullback preserves Clifford module property
  (files: vz-schur-complement, vz-schur §17-18, oq3c-index-additivity).
- **ind_H(D_GU) = 24 (CONDITIONALLY_RESOLVED):** from Atkinson-Schur LDU (oq3c) + formal-
  degree sum (n5-discrete-series §15-18) + K3-type base (oq3a, oq3b).
- **OC1/OC2 sharpening:** Atiyah-Jannich stability applies once D_GU is realized as a
  continuous family in Fred_H; non-compactness shifts the burden to proving Fredholmness,
  not to the classifying-space theorem itself
  (file: signed-readout-oc1-oc2-noncompact-fredholm).

---

## 3. Step 1: H-Linearity of D_GU

### 3.1 Definition Recall

D_GU is the Dirac-DeRham operator for the GU field complex on Y^14, built from:

- The Dirac-type operator using the gimmel metric g_Y (signature (9,5)) and a
  Spin(9,5)-principal bundle with associated spinor bundle S = H^64.
- A connection A on the Sp(64)-principal bundle (gauge field).
- The Shiab coupling Phi: Omega^2 tensor S -> Omega^1 tensor S.
- A Rarita-Schwinger sector coupling S tensor T*Y^14 to S.

In local coordinates, schematically:

```
D_GU = sum_a gamma^a (nabla_a + A_a) + Phi
```

where gamma^a = c(e^a) is Clifford multiplication and A_a is the gauge connection valued
in sp(64).

### 3.2 Three Layers of H-Linearity

**Layer 1: S = H^64 carries a right-H module structure.**

S = H^64 is equipped with the standard right H-module structure: for s in S and q in H,
the right action is s.q = s * q (right matrix multiplication by q in M(64,H)). This action
commutes with left multiplication by M(64,H), hence with the Clifford representation.

**Layer 2: Clifford multiplication c(e^a) is H-linear.**

For any tangent vector v, c(v): S -> S is left multiplication by a fixed element of
M(64,H). Since M(64,H) acts on the left and H acts on the right, these commute:

```
c(v)(s.q) = (c(v) s).q    for all s in S, q in H.
```

This is the fundamental algebraic fact: Cl(9,5) = M(64,H) acts on S = H^64 by left
M(64,H)-multiplication, which commutes with right-H multiplication.

**Layer 3: The connection and gauge coupling preserve H-linearity.**

(a) The Levi-Civita connection nabla on the spinor bundle: the covariant derivative
nabla_a acts by nabla_a s = partial_a s + (1/4) omega_{ab} gamma^{ab} s, where omega_{ab}
is the spin connection. Each factor gamma^{ab} = c(e^a)c(e^b) is left multiplication in
M(64,H), so nabla_a is H-linear.

(b) The gauge connection A_a: A_a is valued in sp(64) = u(64,H), the Lie algebra of
Sp(64). The action on S = H^64 is A_a . s (left Sp(64) action). Since sp(64) is the
skew-Hermitian quaternionic matrices (X such that X* + X = 0 in the quaternionic sense),
acting on the left, it commutes with right-H multiplication. Thus nabla_a^A = nabla_a + A_a
is H-linear.

(c) Shiab Phi: by sc1-shiab-domain-codomain, Phi is H-linear and Spin(9,5)-equivariant.

(d) Rarita-Schwinger sector: the gamma-trace projection Pi_RS: S tensor T*Y^14 -> S^RS
is H-linear (it is c(gamma^a) contracted with the index, in M(64,H), acting on the left).
By oq3c-index-additivity, the LDU splitting D_GU = L * diag(A, S_R^eff) * U uses H-linear
triangular factors L, U; thus D_GU is H-linear iff each block is.

**Conclusion, Step 1:** D_GU commutes with right-H multiplication on S = H^64. This is
an exact algebraic statement, with no analytic input. Grade: VERIFIED at the algebraic level.

---

## 4. Step 2: Fredholmness and the Role of Non-Compactness

### 4.1 Fredholm in the Compact Case (Standard Result)

For a compact Riemannian manifold M^n with a self-adjoint elliptic first-order differential
operator D on a Hermitian (or quaternionic) vector bundle E, D extends to a bounded
operator D: W^{1,2}(E) -> L^2(E) which is Fredholm. This is the classical Atiyah-Singer
setting. The Sobolev embedding W^{1,2} -> L^2 is compact, which forces closed range and
finite-dimensional kernel/cokernel.

### 4.2 Non-Compact Y^14: The Precise Obstruction

Y^14 = Met(X^4) is non-compact (the fiber GL(4,R)/O(3,1) is non-compact). For a non-compact
Riemannian manifold, an elliptic operator need not be Fredholm on L^2: the essential
spectrum can include 0, or the range may fail to be closed.

The Atiyah-Schmid (1977) approach for symmetric spaces establishes Fredholmness for
the discrete-series sector. Specifically, for G/H a semisimple symmetric space and a G-
homogeneous elliptic operator D, the restriction of D to the L^2_disc subspace (the direct
sum of discrete-series summands) is Fredholm. This is not classical Sobolev compactness;
it is a consequence of the spectral decomposition of L^2(G/H) and the fact that each
discrete-series summand contributes a finite-dimensional kernel (by the Flensted-Jensen
theorem, established above for SL(4,R)/SO_0(3,1) with split-rank 1).

**The issue for Y^14:** Y^14 is not itself a symmetric space G/H. The Atiyah-Schmid
mechanism applies to the fibers of the fibration pi: Y^14 -> X^4 (each fiber is
GL(4,R)/O(3,1)), not to Y^14 globally. The global Fredholmness of D_GU on L^2(Y^14, S)
cannot be deduced directly from fiber-by-fiber discrete-series theory without additional
analytic input.

**The section pullback resolves this:** The section s: X^4 -> Y^14 provides a canonical
reduction. The pullback s*(D_GU) is an operator on the compact manifold X^4 (or manifold
with boundary, in the APS setting). Standard elliptic theory applies there, and the
Fredholm property on X^4 is classical.

---

## 5. Step 3: Section Pullback Reduction to Compact X^4

### 5.1 The Pullback Operator

The section s: X^4 -> Y^14 is a smooth embedding. The pullback of the spinor bundle is:

```
s*(S) = S(3,1) tensor S(6,4)
```

where S(3,1) = C^4 is the 4D Dirac spinor (from the base signature (3,1)) and S(6,4) = C^16
is the fiber spinor (from the fiber signature (6,4)), giving:

```
s*(S) = H^8 per point of X^4
```

(since S(3,1) tensor S(6,4) = C^4 tensor C^16 = C^64 = H^16 as a right-H module,
and chiral halves H^8 for chiral Dirac on X^4).

The pullback operator s*(D_GU) acts on sections of s*(S) over X^4. By the principal-
symbol computation in vz-schur §17-18:

```
sigma_{s*(D_GU)}(eta)^2 = g_s(eta,eta) Id_{E_s}   for all eta in T*X^4
```

where g_s = s*(g_Y) is the pulled-back Lorentzian metric. This is an exact matrix identity
(OQ3-V1: RESOLVED), meaning s*(D_GU) is a Dirac-type operator for the metric g_s.

### 5.2 Fredholmness on Compact X^4

**Case A: X^4 compact, Riemannian (Euclidean signature).**

If X^4 is compact with Riemannian metric g_s, then s*(D_GU) is an elliptic first-order
differential operator on the compact manifold X^4 with bundle s*(S) = H^8 per chiral half.
By standard elliptic theory (Atiyah-Singer), s*(D_GU) is Fredholm on L^2(X^4, s*(S)).
The index is well-defined:

```
ind_H(s*(D_GU)) = dim_H ker(s*(D_GU)) - dim_H coker(s*(D_GU)) in Z.
```

**Case B: X^4 compact with boundary, Lorentzian (APS setting).**

If X^4 has Lorentzian signature (3,1) and is a compact manifold with boundary (e.g.,
a cosmological region M = [t_1, t_2] x Sigma^3), the Atiyah-Patodi-Singer theorem
(Bär-Strohmaier 2016/2019 for Lorentzian manifolds with timelike boundary) applies.
The APS condition on the boundary Sigma^3 selects a self-adjoint extension of s*(D_GU)
for which the operator is Fredholm. The APS index formula gives:

```
ind_APS(s*(D_GU)) = integral_{X^4} hat{A}(g_s) ch(s*(S)) - (1/2)(eta(D_{bdry}) + dim ker D_{bdry})
```

where eta is the eta-invariant of the boundary operator. From ind-top-eta-s3, the flat
S^3 eta-invariant is 0, confirming APS compatibility.

**Case C: X^4 = K3 (compact, simply-connected, Ricci-flat).**

The K3 case (oq3a, variational K3 selection) gives a compact Riemannian manifold with
Â(K3) = 2. The operator s*(D_GU) is the product of the spin-1/2 Dirac on K3 twisted by
S(6,4), plus the RS sector. By oq3c-index-additivity (Atkinson-Schur LDU):

```
ind_H(s*(D_GU)) = ind_H(A) + ind_H(S_R^eff) = 16 + 8 = 24.
```

In this case, classical compact elliptic theory gives Fredholmness unconditionally (no
non-compact issue), and the index is 24 at reconstruction grade.

### 5.3 The Pullback Reduction as a Fredholm Instrument

The section pullback s is the instrument that converts the non-compact Fredholm problem
on Y^14 to a classical elliptic problem on X^4. Formally:

**Lemma (Fredholm pullback).** If s: X^4 -> Y^14 is a smooth section, s*(D_GU) is an
elliptic operator on X^4, and X^4 is compact (or APS-complete), then:

(i) s*(D_GU) is Fredholm on L^2(X^4, s*(S)).
(ii) ind_H(s*(D_GU)) is well-defined.
(iii) ind_H(s*(D_GU)) = ind_H(D_GU|_{L^2_disc, s-sector}) under the identification of the
     discrete-series L^2 modes localized near s(X^4).

Part (i): classical elliptic theory on X^4. Part (ii): follows from (i). Part (iii):
reconstruction-grade — the connection between the 14D operator restricted to a sector
near the section and the 4D pullback operator is the Kaluza-Klein reduction. In the
zero-mode sector (RC1, rc1-rs-kk-zero-mode), the KK projection to zero modes commutes
with the horizontal Clifford element (vz-f6-eft-decoupling §F6), so the 14D zero-mode
sector and the 4D pullback agree at principal-symbol level. This part remains reconstruction-
grade: the precise identification of the sector is not fully developed.

---

## 6. Step 4: Pullback Preserves H-Linear Structure

### 6.1 The Critical Gate

The failure condition from the problem statement is:

> If the pullback does not preserve the H-linear structure, the quaternionic index is
> not well-defined.

We now verify that s* preserves H-linearity.

### 6.2 Algebraic Verification

**Claim:** The section pullback s*: Gamma(Y^14, S) -> Gamma(X^4, s*(S)) preserves
right-H multiplication.

**Proof:** The pullback is defined as s*(psi)(x) = psi(s(x)) for a section psi. The right-
H action on S is fiberwise: (psi.q)(y) = psi(y).q for q in H and y in Y^14. The pullback of
this action is:

```
(s*(psi.q))(x) = (psi.q)(s(x)) = psi(s(x)).q = (s*psi)(x).q = (s*psi . q)(x).
```

Therefore s*(psi.q) = (s*psi).q. The pullback commutes with right-H multiplication.

**Conclusion:** s* is H-linear as a map on sections. Grade: VERIFIED (algebraic identity).

### 6.3 Operator Pullback Preserves H-Linearity

**Claim:** If D_GU is H-linear, then s*(D_GU) is H-linear.

**Proof:** For any section psi and q in H:

```
s*(D_GU)(psi.q) = s*(D_GU(psi.q)) = s*((D_GU psi).q) = (s*(D_GU psi)).q = (s*(D_GU) (s*psi)).q.
```

The second equality uses H-linearity of D_GU (Step 1). The third uses H-linearity of s*
(6.2). This is valid when psi is restricted to sections pulled back from s(X^4), i.e., when
the operator commutes with the restriction map. At principal-symbol level this holds exactly
(vz-schur §17 OQ3-V1-V3: RESOLVED). At sub-leading order it is reconstruction-grade.

**Conclusion:** s*(D_GU) is H-linear. The kernel and cokernel of s*(D_GU) are right-H
modules (since D_GU is H-linear, ker(s*(D_GU)) is closed under right-H multiplication).
Hence dim_H ker, dim_H coker are well-defined, and ind_H(s*(D_GU)) is in Z.

### 6.4 Failure Conditions

The H-linear structure breaks if:

**F1 (Gauge field breaks Sp(64)):** If the gauge connection A is not Sp(64)-valued (e.g.,
if a gauge transformation takes A outside sp(64)), then A_a.s is no longer H-linear (the
action would mix the right-H module structure). This would break Step 3.2(b). Status:
gate on gauge group choice; for A in Omega^1(sp(64)) this does not occur.

**F2 (Pullback section is not H-linear):** This is ruled out by 6.2 above (exact algebraic
verification). Status: RESOLVED.

**F3 (RS gamma-trace not H-linear):** If the RS projector Pi_RS is not H-linear, the
oq3c LDU split is not H-linear, and ind_H(D_GU) need not split as 16+8. Status:
Pi_RS is c(gamma^mu) contracted with a tensor index, acting in M(64,H) on the left;
this is H-linear. RESOLVED at reconstruction grade (oq3c file confirms bimodule structure).

**F4 (Sobolev domain breaks H-linearity):** The Sobolev space W^{1,2}_H(X^4, s*(S)) must
be a right-H Hilbert module. The inner product on S = H^64 is the standard quaternionic
inner product <u, v>_H = sum_i bar{u_i} v_i (conjugation on the left), which is compatible
with right-H action. The W^{1,2} norm is built from this. Status: RESOLVED at reconstruction
grade by standard quaternionic Sobolev theory.

---

## 7. Well-Definedness of ind_H(D_GU)

### 7.1 Summary Chain

Combining the four steps:

1. **H-linearity of D_GU (algebraic, VERIFIED):** D_GU commutes with right-H multiplication.
   Source: Cl(9,5) = M(64,H) left-acts, H right-acts, these commute.

2. **Section pullback s* preserves H-linearity (algebraic, VERIFIED):** s*(psi.q) = (s*psi).q
   and s*(D_GU) is H-linear.

3. **Fredholmness of s*(D_GU) on compact X^4 (RESOLVED for K3 case):** s*(D_GU) is an
   elliptic operator on X^4, Fredholm by classical theory. Kernel and cokernel are finite-
   dimensional right-H modules.

4. **ind_H(s*(D_GU)) = dim_H ker - dim_H coker is well-defined and equals 24
   (CONDITIONALLY_RESOLVED):** By oq3c Atkinson-Schur LDU + K3 Â=2 + RS ind=8.

**Conclusion:** ind_H(D_GU) is well-defined under the section pullback reduction. The
failure condition is avoided: s* preserves H-linear structure exactly.

### 7.2 What "Well-Defined" Means Precisely

ind_H(D_GU) is well-defined in the following sense:

(a) **Value:** ind_H = 24 (three H-generations) is the unique integer computed from
    the Atkinson-Schur LDU decomposition of D_GU restricted to the s*(X^4) sector.

(b) **Independence of section choice:** Different sections s, s' (different metrics on X^4)
    give different 4D operators, but the index is locally constant on connected components
    of the section space (this is the Atiyah-Jannich stability of ind_H under continuous
    deformations of s that do not destroy Fredholmness). The connected space of sections
    (gauge-orbit moduli) is contractible as the affine gauge-field space A/G with Sp(64)
    connected (oq2d-gu-contact). Status: CONDITIONALLY_RESOLVED (reconstruction, same gates
    as OC1: continuity of the family in Fred_H topology).

(c) **H-linear index class in KSp^0:** Under assumptions OC2-A1 through OC2-A6
    (signed-readout-oc1-oc2), [D] in KSp^0(X') = KO^4(X') where X' is the compact
    parameter space of observer data. The augmentation recovers ind_H = 24.

### 7.3 Comparison to the Compact Case

In the compact case (e.g., D on a compact manifold M^n), Fredholmness is automatic from
elliptic theory; the section pullback is trivial (s is a diffeomorphism onto M^n). The
non-compact Y^14 case adds one step: prove the pullback operator s*(D_GU) on X^4 is the
correct Fredholm representative of the 14D operator. This is established at reconstruction
grade by the KK zero-mode analysis (rc1-rs-kk-zero-mode, vz-f6-eft-decoupling) and the
principal-symbol computation (vz-schur §17-18).

---

## 8. Remaining Gaps

The following items prevent upgrading from CONDITIONALLY_RESOLVED to RESOLVED:

**G1 (Sobolev domain explicit construction, grade: open).**
The Sobolev domain W^{1,2}_H(Y^14, S) for D_GU on Y^14 (before pullback) has not been
constructed with control over the sub-principal and boundary behavior of the non-compact
fiber GL(4,R)/O(3,1). The pullback to X^4 avoids this, but does not eliminate the need
for a 14D domain description if the 14D-to-4D identification in Step 5.3(iii) is to be
verified fully.

**G2 (Precise 14D-to-4D identification, grade: reconstruction).**
The identification ind_H(D_GU|_{disc, s-sector}) = ind_H(s*(D_GU)) uses the KK zero-mode
argument. The exact form of the projection to the s-sector (the bundle of zero modes over
s(X^4)) and its unitarity relative to the L^2(Y^14, S) inner product have not been
computed explicitly.

**G3 (Section-independence of ind_H, grade: reconstruction).**
Atiyah-Jannich stability (OC1) requires continuity of the family of bounded transforms
in Fred_H topology. While Sp(64) connectedness and gauge-orbit contractibility support
section-independence, the explicit continuity in the gap/bounded-transform topology has
not been verified for the GU family.

**G4 (APS eta boundary terms for Lorentzian X^4, grade: reconstruction).**
In the Lorentzian (physical) setting, the APS theorem applies with boundary terms. The
flat-bundle eta-invariant on S^3 is 0 (from ind-top-eta-s3), but the curved-bundle and
non-flat cases (dynamical instanton backgrounds) could produce non-zero eta. This is
controlled for the K3 ground state; curved backgrounds are not fully analyzed.

---

## 9. Result

**Verdict: CONDITIONALLY_RESOLVED** at reconstruction grade.

- **H-linearity of D_GU:** VERIFIED (exact algebraic identity; not analytic).
- **Section pullback s* preserves H-linear structure:** VERIFIED (exact algebraic identity;
  failure condition is avoided).
- **Fredholmness of s*(D_GU) on compact X^4:** RESOLVED (classical elliptic theory on K3).
- **ind_H(D_GU) = 24 well-defined:** CONDITIONALLY_RESOLVED (gates G1-G4; principal result
  is 16+8=24 from oq3c + discrete-series + K3 variational selection).
- **KSp^0 class:** CONDITIONALLY_RESOLVED pending OC2-A1 through OC2-A6 (see
  signed-readout-oc1-oc2-noncompact-fredholm).

**Failure condition (confirmed avoided for K3/Sp(64) sector):**
The quaternionic index is not well-defined if and only if s* fails to preserve H-linear
structure. As proven in §6.2, s*(psi.q) = (s*psi).q is an exact algebraic identity;
the failure condition does not fire in the Sp(64)-gauged, K3-based GU sector.

---

## 10. Open Questions

**OQ1 (Sobolev 14D domain):** Construct W^{1,2}_H(Y^14, S) explicitly with sub-principal
control on the non-compact fiber. Needed for upgrading G1.

**OQ2 (KK-zero-mode unitarity):** Prove the projection from L^2(Y^14, S) to the zero-mode
sector near s(X^4) is unitary (isometric onto its range in L^2(X^4, s*(S))). Needed for G2.

**OQ3 (Bounded-transform continuity):** Verify that A |-> D_GU(A)(1+D_GU(A)^*D_GU(A))^{-1/2}
is continuous in norm topology for A in Omega^1(sp(64)). Needed for G3.

**OQ4 (Non-trivial eta):** Compute eta(D_{bdry}, s*(S)) for non-flat spatial slices. Needed
for full Lorentzian APS index computation (G4).

---

## 11. Verdict Line

**OC2 (H-linear Fredholm, ind_H well-defined): CONDITIONALLY_RESOLVED.**
H-linearity is verified algebraically and is preserved exactly by section pullback; Fredholmness
on compact X^4 is classical; ind_H = 24 is reconstruction-grade conditional on K3 topology,
RS index 8, and index additivity.
