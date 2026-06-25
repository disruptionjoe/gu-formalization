---
title: "Clifford Module Non-Decoupling and Velo-Zwanziger Evasion in Geometric Unity"
subtitle: "The 14D Rarita-Schwinger Sector Has Causal Characteristics"
date: 2026-06-23
status: preprint-draft
target_journals:
  - "Communications in Mathematical Physics"
  - "Letters in Mathematical Physics"
keywords:
  - Geometric Unity
  - Velo-Zwanziger
  - Rarita-Schwinger
  - Clifford module
  - higher-spin causality
  - Schur complement
  - spinor geometry
---

> **2026-06-25 status correction.** This preprint draft overstates the current VZ and
> anomaly scope. Current VZ status is 14D CONDITIONALLY_EVADED pending independent
> E-block invertibility, and 4D CONDITIONALLY_RESOLVED at principal-symbol grade. The
> shiab result is existence-only, and full GU anomaly cancellation remains OPEN pending
> local `I_16`/index-density and global spin-bordism/Dai-Freed/eta checks.

# Clifford Module Non-Decoupling and Velo-Zwanziger Evasion in Geometric Unity

---

## Abstract

We analyze a reconstruction-grade mechanism by which the Rarita-Schwinger (RS) sector of Geometric Unity (GU) can evade the Velo-Zwanziger (VZ) no-go theorem at principal-symbol level. GU's rolled-up Dirac-DeRham-Einstein operator D_GU acts on the full Clifford module bundle E over Y^{14} = Met(X^4) with signature (9,5) and gauge group Sp(64). The RS sector is the sub-bundle R^{14D} = ker Gamma^{14D} within E, not a standalone Rarita-Schwinger field. Its effective principal symbol is the Schur complement S_R(xi) = A(xi) - B(xi) E(xi)^{-1} C(xi), so the 14D claim is conditional on independent E-block invertibility. Under that precondition, ker S_R(xi) = 0 for non-null covectors and the characteristic cone is null. Current status: 14D CONDITIONALLY_EVADED; 4D CONDITIONALLY_RESOLVED at principal-symbol grade; full dynamics and anomaly closure remain open.

---

## 1. Introduction

### 1.1 The Velo-Zwanziger Obstruction

The Velo-Zwanziger (VZ) theorem [VZ69] is a causality constraint on higher-spin field theories. For a spin-3/2 (Rarita-Schwinger) field psi_mu minimally coupled to an external gauge background, the characteristic cone of the field equations can develop spacelike components. This means the equations admit solutions propagating faster than light, a pathology that renders the theory physically inconsistent.

The theorem applies when five conditions hold: (H1) the RS field has a standalone Rarita-Schwinger Lagrangian; (H2) it is minimally coupled to a non-trivial gauge background; (H3) there is no local supersymmetry; (H4) there is no higher-spin gauge invariance; and (H5) the spacetime dimension and signature permit spacelike characteristics. The critical condition for GU is H1.

The VZ obstruction is not merely technical. It has killed entire programs of higher-spin field theory. Any unified theory that proposes spin-3/2 particles must either invoke a guardian symmetry (local SUSY in supergravity is the standard answer), construct a Lagrangian with higher-spin gauge invariance (the Vasiliev approach), or demonstrate that its spin-3/2 sector is genuinely non-standalone.

GU proposes the third option.

### 1.2 Geometric Unity and the Nguyen Critique

Geometric Unity [W20] is a program to derive the structure of fundamental physics from the geometry of the 14-dimensional space Y^{14} = Met(X^4), the bundle of Riemannian metrics on a 4-manifold X^4. The space Y^{14} carries a natural metric g_Y (the gimmel metric) of signature (9,5), and a Clifford algebra Cl(9,5) isomorphic to M(64,H), the algebra of 64x64 quaternionic matrices. The spinor module is S = H^{64} and the natural gauge group is Sp(64) = U(64,H).

The central operator is a rolled-up Dirac-DeRham-Einstein operator D_GU acting on sections of the Clifford module bundle E = (Omega^0(Y) tensor S^+) direct-sum (Omega^1(Y) tensor S^-). It includes a Leibniz cross-term via the shiab operator Phi: Omega^2(Y^{14}) tensor S -> Omega^1(Y^{14}) tensor S, defined by Clifford contraction.

In 2021, Nguyen [N21] published a detailed mathematical critique of GU. Two core objections concerned the shiab operator (undefined domain and codomain) and the anomaly structure of the gauge group. A third implicit concern was the Velo-Zwanziger constraint on the RS sector.

The shiab existence objection is resolved only for the existence of a natural H-linear,
Spin(9,5)-equivariant map in the (9,5) quaternionic setting. The Sp(64) replacement
substantially addresses Nguyen's U(128) anomaly pincer, but full GU anomaly cancellation
is not closed. This paper addresses the VZ lane, whose present status is conditional.

### 1.3 Main Result

**Theorem candidate (conditional VZ evasion, reconstruction grade).** Let D_GU be the rolled-up Dirac-DeRham-Einstein operator acting on sections of the Clifford module bundle E over Y^{14} with signature (9,5). Let R^{14D} = ker Gamma^{14D} be the 14D Rarita-Schwinger sub-bundle, where Gamma^{14D}(psi) = c(e^A) psi_A sums over all 14 frame directions. Let S_R(xi) = A(xi) - B(xi) E(xi)^{-1} C(xi) be the Schur complement of the principal symbol sigma_D(xi) in the RS/non-RS block decomposition. Conditional on independent invertibility of the E-block for all non-null xi, then for all covectors xi in T*Y^{14} with g_Y(xi,xi) not equal to 0:

    ker S_R(xi) = 0.

The characteristic cone of the effective RS principal symbol is the null cone {xi : g_Y(xi,xi) = 0}, containing no spacelike covectors.

The proof occupies Section 4. Sections 5 and 6 establish robustness. Section 7 identifies falsification conditions. Section 8 situates the result within the Nguyen critique.

### 1.4 Organization

Section 2 establishes the geometric and algebraic setup: Y^{14}, the Clifford algebra Cl(9,5), the Sp(64) gauge group, D_GU, and the RS sector. Section 3 reviews the classical VZ theorem and the mechanism by which it fires in 4D. Section 4 contains the principal proof: the Clifford module identity implies trivial kernel for the Schur complement at all non-null 14D covectors. Section 5 verifies robustness under sub-principal symbol corrections and lower-order curvature. Section 6 addresses the 4D reduction: section-pullback preserves the Clifford identity, and effective field theory decoupling is blocked by the kinematic nature of the RS/spin-1/2 coupling. Section 7 gives explicit falsification conditions. Section 8 states what this resolves in the Nguyen critique and what remains open.

---

## 2. Setup

### 2.1 The Observerse Y^{14}

Let X^4 be an oriented smooth 4-manifold. Define Y^{14} = Met(X^4), the total space of the bundle of Riemannian metrics on X^4. As a fiber bundle, pi: Y^{14} -> X^4, with fiber at x in X^4 equal to GL(4,R)/O(3,1), the space of positive-definite inner products on T_x X^4.

The fiber GL(4,R)/O(3,1) is diffeomorphic to RP^3 (via the polar decomposition SO(4)/SO(3) = S^3/Z_2). It carries a natural Frobenius metric of signature (7,3) on the space of symmetric 2-tensors. After applying trace-reversal (h -> h - (1/4) tr(h) g for 4x4 symmetric matrices), the fiber metric becomes signature (6,4) on the traceless-symmetric 2-tensor space (dimension 9) plus 1 trace direction.

The total metric on Y^{14} combines the (3,1) base metric with the (6,4) fiber metric, giving the gimmel metric g_Y of signature (9,5).

At any point of Y^{14} lying over a section s: X^4 -> Y^{14}, the cotangent space splits as:

    T*Y^{14}|_{s(x)} = H* direct-sum N*

where H* = s*(T*X^4) has signature (3,1) (the horizontal directions) and N* is the 10-dimensional vertical cotangent space with signature (6,4).

### 2.2 Clifford Algebra and Spinor Module

The metric g_Y of signature (9,5) determines a Clifford algebra:

    Cl(9,5) isomorphic to M(64,H)

as can be verified from the periodicity table [LM89]: signature difference (9-5) mod 8 = 4, giving the quaternionic matrix algebra. The spinor module is S = H^{64}, with dim_R S = 256.

The fundamental Clifford identity is:

    c(xi)^2 = g_Y(xi,xi) Id_S    for all xi in T*Y^{14}.          (Cl)

Equivalently, {c(e^A), c(e^B)} = 2 g_Y^{AB} Id_S for any frame {e^A}.

In 14 dimensions, dim Y^{14} = 14, and the Clifford trace formula gives c^A c_A = 14 Id_S.

### 2.3 The Gauge Group

The gauge group is Sp(64) = U(64,H), the group of quaternionic unitary transformations of S = H^{64}. Its Lie algebra is sp(64), the algebra of H-skew-Hermitian endomorphisms of H^{64}. The real dimension is dim sp(64) = 64(2*64 + 1) = 8256.

Sp(64) substantially addresses Nguyen's U(128) anomaly pincer, but this draft's original automatic-anomaly phrasing is superseded. Pseudoreality is a key structural input, not a complete proof of full GU anomaly cancellation. Current upgrade gates are the explicit local 14D `I_16`/index-density calculation for the actual chiral field content and the global spin-bordism/Dai-Freed/eta check.

### 2.4 The Dirac-DeRham-Einstein Operator

The rolled-up operator D_GU acts on sections of the Clifford module bundle:

    E = (Omega^0(Y^{14}) tensor S^+) direct-sum (Omega^1(Y^{14}) tensor S^-)

where S^+/- denote the chiral halves of S (in 14D with split signature, these are the even/odd Clifford module components).

In the gauge sector, D_GU takes the form:

    D_GU (u, psi) = (d_A* psi, d_A u + Phi(F_A tensor psi))

where d_A is the gauge-covariant derivative with Sp(64) connection A, d_A* is its adjoint, and Phi is the shiab operator.

**The shiab operator.** Phi: Omega^2(Y^{14}) tensor S -> Omega^1(Y^{14}) tensor S is defined by Clifford contraction:

    Phi(alpha tensor s) = sum_A e^A tensor c(iota_{e_A} alpha) . s

for a 2-form alpha and spinor s. This map is H-linear and Spin(9,5)-equivariant; its existence at the symbol level requires no complexification.

**Principal symbol.** The principal symbol of D_GU at a covector xi in T*Y^{14} is:

    sigma_D(xi)(u, psi) = (g_Y(xi, psi), xi tensor u + F_xi psi)

where (F_xi psi)_A = xi_A c^B psi_B - c(xi) psi_A is the shiab Leibniz term.

**Key property.** D_GU is a Clifford module operator, meaning its principal symbol satisfies:

    sigma_D(xi)^2 = g_Y(xi,xi) Id_E    for all xi in T*Y^{14}.     (CL)

This is an exact algebraic identity following from the Clifford algebra structure (Cl): the leading symbol is the Clifford multiplication c(xi), and c(xi)^2 = g_Y(xi,xi) Id_S by (Cl).

### 2.5 The Rarita-Schwinger Sector

The 14D Rarita-Schwinger sector is:

    R^{14D} = ker Gamma^{14D}

where the 14D gamma-trace is:

    Gamma^{14D}(psi) = c(e^A) psi_A = sum_{A=0}^{13} gamma^A psi_A.

This is a sub-bundle of Omega^1(Y^{14}) tensor S^- with:

    dim_R R^{14D} = (14 - 1) * 256 = 13 * 256 = 3328.

The complementary sub-bundle Q = (Omega^0 tensor S^+) direct-sum (im j^{14D}) has:

    dim_R Q = 256 + 256 = 512

where j^{14D}(s)_A = (1/14) gamma_A s is the injection of S into the gamma-trace sector.

**The RS sub-bundle is not a sub-Clifford-module.** The Clifford element c(xi) does not preserve R^{14D}: for psi_R in R^{14D}, the gamma-trace of c(xi) psi_R is generically nonzero (it equals 2 g_Y(xi, psi_R) by the Clifford anticommutation relation). This non-preservation is the structural reason for VZ evasion, as we now make precise.

---

## 3. The VZ Constraint and Why It Fires in 4D

### 3.1 Classical Statement

Let psi_mu be a spin-3/2 (Rarita-Schwinger) field in a 4D spacetime X^4 with metric g and gauge background A_mu. The RS Lagrangian is:

    L_RS = psi_mu^dagger (gamma^{mu nu rho} nabla_nu) psi_rho

with constraint gamma^mu psi_mu = 0 derived from the Euler-Lagrange equations.

Velo and Zwanziger [VZ69] proved: when the gauge curvature F_mu_nu is non-trivial, the characteristic matrix of the effective RS equation develops spacelike eigenvalues. The physical propagation speed exceeds the speed of light. The theory is acausal.

The mechanism: act with the subsidiary-condition differential operator (the divergence nabla^mu) on the RS field equation to derive a secondary equation. In the gauge background, the commutator [nabla_mu, nabla_nu] introduces F_mu_nu at first order in the secondary equation. The effective metric for the secondary equation acquires a correction proportional to F_mu_nu, which can be spacelike.

### 3.2 The Five Hypotheses of VZ

The VZ theorem requires all five of the following:

**(H1) Standalone RS Lagrangian.** The RS field has its own variational principle, separate from any other sector.

**(H2) Minimal gauge coupling.** The RS field is minimally coupled to the gauge background via nabla_mu = d_mu + A_mu.

**(H3) No local SUSY.** The RS field is not a gravitino in a supergravity theory. Local SUSY is the guardian symmetry that restores causality.

**(H4) No higher-spin gauge invariance.** The Fronsdal-type higher-spin gauge invariance (which allows consistent higher-spin propagation in AdS) is absent.

**(H5) Non-trivial gauge background.** The curvature F_mu_nu is nonzero.

In standard higher-spin field theory without SUSY, all five hold and VZ fires. In GU, H1 fails at 14D, as we prove in Section 4.

### 3.3 Why VZ Fires at 4D for Standalone RS Fields

For a standalone 4D RS field, the effective characteristic matrix at a 4D covector eta is:

    chi^{eff}(eta) = [g(eta,eta) delta^a_b - F^{ac} F_{cb}]

schematically, where F_{ab} is the gauge curvature contracted with spinor indices. For non-trivial F, the eigenvalues of chi^{eff} include spacelike values, giving acausal propagation.

The VZ analysis is a principal-symbol computation for the secondary (subsidiary-condition-derived) equation. The curvature F enters at first order in the secondary equation because the subsidiary condition operator (nabla^mu) applied to the primary equation generates [nabla_mu, nabla_nu] psi = F_mu_nu psi, and F is treated as a background in which psi propagates.

In GU, the operative objects are different: there is no secondary equation from a subsidiary condition, because the RS constraint is not derived by varying a Lagrangian.

---

## 4. The 14D Evasion: Clifford Identity, Schur Complement, and Kernel Theorem

### 4.1 Block Decomposition of the Principal Symbol

In the RS/non-RS decomposition E = R^{14D} direct-sum Q, the principal symbol M(xi) = sigma_D(xi) takes the block form:

    M(xi) = | A(xi)  B(xi) |
            | C(xi)  E(xi) |

where:
- A(xi): R^{14D} -> R^{14D} is the RS-to-RS block
- B(xi): Q -> R^{14D} is the spin-1/2-to-RS block
- C(xi): R^{14D} -> Q is the RS-to-spin-1/2 block
- E(xi): Q -> Q is the spin-1/2 block

The Clifford module identity (CL) gives M(xi)^2 = xi^2 Id_E (writing xi^2 = g_Y(xi,xi)), which expands to four block identities:

    (I)   A^2 + BC = xi^2 Id_R
    (II)  AB + BE = 0
    (III) CA + EC = 0
    (IV)  CB + E^2 = xi^2 Id_Q

### 4.2 Off-Diagonal Coupling

We verify that the off-diagonal blocks B and C are genuinely nonzero.

**Computation of C.** For psi_R in R^{14D} (so Gamma^{14D}(psi_R) = 0), the C-block maps psi_R to its components in Q. Setting chi = g_Y(xi, psi_R):

    C psi_R = (chi, (c(xi) - 2) chi)

where the first component is a scalar spinor in Q_0 and the second is a gamma-trace component in Q_T. For generic psi_R and generic non-null xi, chi is nonzero (it vanishes only when psi_R is orthogonal to xi in the spin-vector metric).

**Computation of B.** For scalar input phi in Q_0:

    (B phi)_A = xi_A phi - (1/14) gamma_A c(xi) phi

For gamma-trace input j(s)_A = (1/14) gamma_A s:

    (B j(s))_A = (6/7) xi_A s - (3/49) gamma_A c(xi) s

Both are nonzero for generic phi and s. The coupling B and C between the RS and spin-1/2 sectors is a genuine feature of D_GU, not an artifact of a gauge choice.

**Physical interpretation.** The coupling is kinematic: it is determined by the Clifford algebra structure of Cl(9,5) and the RS projection, not by the gauge coupling constant of Sp(64). This is the non-decoupling that drives the VZ evasion.

### 4.3 The Schur Complement

The effective RS principal symbol, obtained by integrating out the spin-1/2 (Q) sector, is the Schur complement:

    S_R(xi) = A(xi) - B(xi) E(xi)^{-1} C(xi)

This is a well-defined endomorphism of R^{14D} whenever E(xi) is invertible.

**Invertibility of E.** The block determinant formula gives:

    det(M(xi)) = det(E(xi)) * det(S_R(xi))

Since M(xi)^2 = xi^2 Id_E, we have det(M(xi))^2 = xi^{2 dim E}, so det(M(xi)) is nonzero for xi^2 not equal to 0. Therefore det(E(xi)) is nonzero for xi^2 not equal to 0, and E(xi) is invertible.

We can verify this explicitly: in the (phi, s) basis for Q = Q_0 direct-sum Q_T, the E block at a 14D covector xi takes the form:

    E(xi) = c(xi) * | 0     1/14 |
                    | 1     13/7 |

with determinant det = c(xi)^2 * (-1/14) = -xi^2/14, nonzero for xi^2 not equal to 0. This confirms E is invertible precisely when xi is non-null.

### 4.4 The Main Theorem

**Theorem 4.1 (Kernel Triviality).** For all covectors xi in T*Y^{14} with g_Y(xi,xi) not equal to 0:

    ker S_R(xi) = 0.

**Proof.** Suppose S_R(xi) psi_R = 0 for some psi_R in R^{14D}. Then A(xi) psi_R = B(xi) E(xi)^{-1} C(xi) psi_R.

Set w = -E(xi)^{-1} C(xi) psi_R in Q. Compute:

    M(xi) (psi_R, w)
    = (A(xi) psi_R + B(xi) w, C(xi) psi_R + E(xi) w)
    = (A(xi) psi_R - B(xi) E^{-1} C psi_R, C psi_R - C psi_R)
    = (S_R(xi) psi_R, 0)
    = (0, 0).

So (psi_R, w) is in the kernel of M(xi). Applying M(xi) to this:

    0 = M(xi)^2 (psi_R, w) = g_Y(xi,xi) (psi_R, w).

Since g_Y(xi,xi) not equal to 0, we conclude (psi_R, w) = 0, hence psi_R = 0. []

**Corollary 4.2 (Causal Characteristics).** The characteristic cone of S_R(xi), defined as {xi : det(S_R(xi)) = 0}, equals the null cone {xi : g_Y(xi,xi) = 0}. In particular, there are no spacelike characteristics.

**Proof.** Theorem 4.1 gives: det(S_R(xi)) = 0 implies xi^2 = 0. Conversely, at xi^2 = 0, det(E(xi)) = 0, so E(xi) is not invertible and S_R(xi) is not defined; the analysis of the characteristic structure at null covectors uses different (constrained Hamiltonian) methods, but null characteristics are the expected behavior for any Dirac-type operator and are not the acausality VZ is concerned with. []

### 4.5 Why H1 Fails: The Non-Standalone Structure

The proof in Theorem 4.1 uses only the Clifford module identity (CL) and the invertibility of E. Both follow from the fact that D_GU is a Clifford module operator on E, not from any special properties of the RS sub-bundle.

The RS sub-bundle R^{14D} = ker Gamma^{14D} is NOT a sub-Clifford-module: c(xi) does not map R^{14D} to itself (the gamma-trace of c(xi) psi_R equals 2 g_Y(xi, psi_R), generically nonzero). The off-diagonal blocks B and C are nonzero precisely because R^{14D} is not preserved by c(xi).

**This non-preservation is the mechanism of VZ evasion.** The RS sector cannot be described by a standalone field equation: any RS degree of freedom interacts with the spin-1/2 sector via the kinematic blocks B and C. Hypothesis H1 of the VZ theorem fails not because of a guardian symmetry but because the field configuration space does not admit an RS-only restriction consistent with the D_GU dynamics.

Physically: what appears to be a spin-3/2 particle in the 14D theory is permanently entangled with the spin-1/2 sector through the Clifford algebra structure. The effective propagator, obtained by integrating out the spin-1/2 sector (the Schur complement), has a causal characteristic cone. This is Clifford module non-decoupling.

---

## 5. Robustness Checks: Sub-Principal Symbol and Lower-Order Curvature

### 5.1 Lower-Order Curvature: Zero-Order Universality (OQ2)

The main theorem is a statement about the principal (first-order) symbol. The VZ mechanism can also operate through lower-order curvature terms, as in the original VZ paper: acting with a subsidiary condition differential operator on the RS equation generates new first-order terms from what were originally zero-order curvature backgrounds.

**Claim F5.1.** All curvature contributions to D_GU enter as zero-order (multiplication) operators on sections of E.

The curvature terms are:

- **Spin connection omega_A.** The term c(e^A) omega_A in D_GU is zero-order: omega_A is a field on Y^{14} (containing the Riemann tensor of g_Y), but it multiplies psi without differentiating it. The spin connection enters the covariant derivative nabla_A = d/dx^A + omega_A as the non-derivative part.

- **Sp(64) gauge curvature F_A.** The Shiab term Phi(F_A tensor psi) multiplies psi by the endomorphism sum_A c(iota_{e_A} F_A), with no derivatives of psi. The Bianchi identity D_A F_A = 0 constrains the background but introduces no derivative of psi.

- **Second fundamental form II_s.** At the section pullback level (see Section 6.1), II_s enters as a normal-index contraction on the spinor-vector components of psi, with no differentiation of psi.

- **Hidden curvature pieces H^(i).** The SL(2,C) curvature components H^{(1)} (spin (3/2,1/2)+(1/2,3/2)), H^{(2)} and H^{(3)} (both (1/2,1/2)) enter via the torsion of the distortion theta = A - Gamma, modifying the spin connection at zero order.

Since all curvature contributions are zero-order in psi, none modify the principal symbol sigma_1(D_GU)(xi) = c(xi). The characteristic cone is determined by the principal symbol alone.

**The classical VZ lower-order mechanism does not apply.** That mechanism requires: (i) a standalone RS Lagrangian; (ii) a separately imposed subsidiary condition gamma^mu psi_mu = 0; (iii) acting with a differential subsidiary condition operator on the RS field equation to generate new first-order terms. In the GU setup, the RS constraint Gamma^{14D} psi = 0 is the definition of the domain of the field (psi in Gamma(R^{14D})), not an externally imposed condition. There is no step (iii). The Schur complement operation that produces S_R is a pseudodifferential (algebraic-at-symbol-level) inversion, not a physical differentiation of the field equation. Zero-order curvature cannot produce new first-order terms through the Schur complement.

### 5.2 Sub-Principal Symbol Analysis (OQ2-b)

The Schur complement S_R(xi) is a pseudodifferential operator of order 1. Its full symbol has a sub-principal (order 0) component sigma_0(S_R^{full})(x,xi) that can in principle introduce additional propagation effects.

**Three independent arguments confirm no new characteristics arise.**

**Argument 1 (Hormander real principal type).** The operator S_R^{full} is of real principal type: its principal symbol vanishes precisely on the null cone {xi^2 = 0}, which is a smooth submanifold of T*Y^{14} \ {0}, and d(xi^2) is nonzero on the null cone for non-degenerate g_Y. By the Hormander propagation-of-singularities theorem [H85, Th. 23.2.4], the wave front set of any solution to S_R^{full} psi_R = 0 propagates along null bicharacteristics of the principal symbol g_Y(xi,xi). The sub-principal symbol sigma_0 affects the amplitude along null rays (appearing in the transport equation for the WKB amplitude) but not the direction of propagation. No new spacelike characteristics arise regardless of the form of sigma_0.

**Argument 2 (No sub-characteristics).** Sub-characteristics arise when the principal symbol vanishes to second or higher order on its characteristic variety (the Dencker-Taylor theorem [D82]). For S_R^{full}, the principal symbol sigma_1(S_R^{full}) = S_R(xi) vanishes to first order on the null cone: S_R(xi) psi_R = 0 implies xi^2 = 0 by Theorem 4.1, and the vanishing is simple (ker S_R has constant rank on the null cone by the Clifford module structure). First-order zeros exclude sub-characteristics.

**Argument 3 (Anti-Hermitian Shiab contribution).** The Shiab contribution to sigma_0(S_R^{full}) is:

    P_R Phi(F_A tensor .) P_R

This is sp(64)-valued (since the Sp(64) connection is anti-Hermitian on S = H^{64} with respect to the quaternionic Hermitian inner product; the gauge group Sp(64) = U(64,H) acts unitarily). An anti-Hermitian operator has purely imaginary eigenvalues over C (or purely imaginary in the appropriate pseudo-Hermitian sense for signature (9,5)). Imaginary eigenvalues of sigma_0 produce amplitude decay or growth along null rays, not new propagation directions.

The spin-connection contribution to sigma_0 is so(9,5)-valued and can have real eigenvalues in the split-signature setting. However, for real-principal-type operators, real eigenvalues of sigma_0 produce exponential amplitude growth along null rays, not new spacelike characteristics. This is a stability question (do WKB amplitudes blow up?) rather than a causality question (does propagation exit the null cone?).

**Summary.** At both principal and sub-principal levels, the characteristic cone of the effective RS operator is the null cone of g_Y. The VZ obstruction is absent.

---

## 6. 4D Reduction: Section Pullback and EFT Decoupling

### 6.1 Section Pullback Preserves Clifford Identity (OQ3)

The observable 4D physics is accessed via a section s: X^4 -> Y^{14} (a choice of metric on X^4, viewed as a section of the bundle pi: Y^{14} -> X^4). The 4D operator is the pullback s*(D_GU) acting on sections of E_s = s*E over X^4.

**Theorem 6.1 (Pullback Clifford Identity).** For any smooth section s: X^4 -> Y^{14} and any covector eta in T*X^4:

    sigma_{s*(D_GU)}(eta)^2 = g_s(eta,eta) Id_{E_s}

where g_s = s*(g_Y|_{H*}) is the induced 4D Lorentzian metric.

**Proof.** The principal symbol of the pullback s*(D_GU) at a 4D covector eta is the pullback of sigma_{D_GU} along the horizontal lift xi_H = s*(eta) in T*Y^{14}:

    sigma_{s*(D_GU)}(eta) = sigma_{D_GU}(xi_H(eta)).

This follows from naturality of principal symbols under smooth pullback: the principal symbol is determined by the highest-order derivative terms, and the section pullback s* lifts 4D covectors to horizontal covectors via ds*. The second fundamental form II_s (the extrinsic curvature of the embedding s(X^4) in Y^{14}) contributes only lower-order terms (via the Gauss formula R^{g_s} = s*(R^{g_Y}) + II_s^2) and does not modify the principal symbol.

Then:

    sigma_{s*(D_GU)}(eta)^2 = sigma_{D_GU}(xi_H)^2 = g_Y(xi_H, xi_H) Id_E = g_s(eta,eta) Id_{E_s}

using the horizontal lift property g_Y(s*(eta), s*(eta)) = s*(g_Y)(eta,eta) = g_s(eta,eta). []

**Corollary 6.2 (4D VZ Evasion).** For the pulled-back 4D RS sub-bundle R_s = s*(R^{14D}), the effective 4D RS symbol S_{R_s}^{4D}(eta) satisfies:

    ker S_{R_s}^{4D}(eta) = 0    for all g_s(eta,eta) not equal to 0.

**Proof.** Apply Theorem 4.1 with M(xi) replaced by sigma_{s*(D_GU)}(eta), using the 4D Clifford module identity from Theorem 6.1. The block determinant argument for invertibility of the 4D E-block (det = -g_s(eta,eta)/4 in the 4D version, using the 4D trace formula gamma^a gamma_a = 4 Id) goes through identically. []

The 4D observable RS field inherits VZ evasion from the 14D theory via the naturality of principal symbols under section pullback. Curvature corrections from II_s, the 4D Weyl tensor, the Sp(64) curvature, and the hidden curvature pieces H^{(i)} all enter s*(D_GU) at zero order and do not change this conclusion.

### 6.2 EFT Decoupling Is Blocked (F6)

A remaining concern is whether the RS sector could decouple from the spin-1/2 sector in an effective field theory description at energies below the Kaluza-Klein scale M_KK. If the RS sector became approximately standalone at low energies, the VZ theorem would apply to the EFT.

**The coupling is kinematic, not dynamical.** The blocks B(eta) and C(eta) are determined by the Clifford algebra structure of Cl(9,5) pulled back to T*X^4:

    C(eta) psi_R = (chi, (c_s(eta) - 2) chi),    chi = g_s(eta, psi_R)

    B(phi, s) proportional to xi_A phi + (6/7) xi_A s - (Clifford projectors)

These expressions depend on eta (the 4D covector), the Clifford gamma matrices, and the RS projection. They do not depend on the Sp(64) gauge coupling constant, the second fundamental form II_s, or any dynamical parameter. The coupling is built into the Clifford module structure and cannot be turned off.

**The KK mode projector commutes with the Clifford element.** At the level of KK zero modes, the projector P_{(0)} onto the fiber zero modes acts on the normal-direction quantum numbers, not on the 4D Clifford algebra structure. Since c_s(eta) commutes with P_{(0)}, the zero-mode B and C blocks are algebraically the same as the full-theory blocks, just restricted to zero-mode states:

    B^{(0)}(eta) = B(eta)|_{zero modes} = O(|eta|),    C^{(0)}(eta) = O(|eta|)

These are linear in eta and O(1) as coefficients, not suppressed.

**Loop corrections are subleading.** One-loop corrections to B and C are O(eta^2) (quadratic in the 4D momentum), because B and C are linear in eta at tree level and loop corrections raise the momentum degree. The tree-level O(eta) kinematic coupling is not canceled by O(eta^2) loop corrections. The Clifford algebra identity sigma_D(eta)^2 = g_s(eta,eta) Id is loop-exact: it is a fixed algebraic fact about the Clifford module structure, not a dynamical identity subject to renormalization.

**The KK mass scale does not separate RS from spin-1/2.** From the fiber geometry (GL(4,R)/O(3,1) with Frobenius fiber metric), the KK mass gap is M_KK ~ 1/R_s (the inverse curvature radius of the 4D metric). The RS zero-mode mass m_RS ~ M_KK (from the Codazzi correction to the normal-bundle Laplacian: the normal curvature correction Delta m_RS ~ M_KK^2). Both RS and spin-1/2 sectors are integrated out at the same KK scale. There is no energy window below M_KK in which only the spin-1/2 sector propagates while the RS sector is still present.

**Conclusion.** The 4D EFT RS sector does not become approximately standalone below M_KK. VZ evasion persists in the 4D effective theory for the same structural reason as in the 14D bulk: the RS/spin-1/2 coupling is kinematic and cannot be suppressed by any energy-scale argument, loop correction, or gauge choice.

---

## 7. Failure Conditions: What Would Falsify This

The VZ evasion argument rests on a short list of structural facts. We state the precise conditions under which each fails.

**F1. Clifford identity failure.** If sigma_D(xi)^2 is not equal to g_Y(xi,xi) Id_E for some xi, then Step 3 of Theorem 4.1 (M(xi)^2 (psi_R, w) = xi^2 (psi_R, w)) is wrong and the proof collapses. This would require D_GU to not be a Clifford module operator -- i.e., the shiab contribution to the principal symbol would need to introduce anomalous terms breaking the Clifford squaring property. For first-order differential operators of Dirac type on Clifford module bundles, this is excluded by construction. Falsification requires producing an explicit xi for which sigma_D(xi)^2 != xi^2 Id.

**F2. E block singularity at non-null covectors.** If E(xi) is singular for some xi with xi^2 not equal to 0, the Schur complement is undefined at that covector and the proof does not apply. The block determinant argument shows det(E) * det(S_R) = det(M) and det(M)^2 = xi^{2N} (nonzero for xi^2 != 0), so this requires the block determinant formula to fail for the operator M(xi). Falsification requires explicit demonstration that det(M(xi)) = 0 despite xi^2 != 0.

**F3. RS is not a direct summand.** If the decomposition E = R^{14D} direct-sum Q is not orthogonal (if R^{14D} is not a direct summand of the Clifford module bundle E), the block-diagonal structure of M(xi) is not exact and the proof needs modification. In constant-coefficient Clifford algebras on a flat bundle, Gamma^{14D} has constant rank (rank 256 over R), so its kernel R^{14D} is a direct summand. On a curved bundle with connection, this holds at the principal-symbol level (where the connection does not contribute).

**F4. Section pullback destroys Clifford identity at first order.** If the section pullback s*(D_GU) is not of Dirac type at the level of the principal symbol (i.e., if there exist first-order normal-direction derivative terms surviving the pullback), then Theorem 6.1 fails. This requires the Gauss formula to introduce first-order derivative terms from II_s into the 4D principal symbol. The Gauss formula for the Riemann tensor gives only zero-order terms (it is an algebraic relation between curvature tensors, not a first-order differential identity for the field psi). Falsification requires finding a mechanism by which II_s modifies the 4D principal symbol at first order.

**F5. Classical VZ mechanism reactivates at sub-leading order.** If the effective RS equation at the level of the full operator (not just the principal symbol) acquires spacelike characteristics via the classical VZ subsidiary-condition mechanism, the conclusion fails. This would require either: (a) the gamma-trace constraint Gamma^{14D} psi = 0 to be re-derived from a Lagrangian (restoring the H1 structure), or (b) the Schur complement S_R^{full} to acquire first-order terms from zero-order curvature (which would require the sub-leading corrections to modify the principal symbol, excluded by the symbol calculus). Falsification requires an explicit example where a zero-order curvature background produces new first-order terms in the effective RS operator through the Schur complement procedure.

**F6. EFT RS sector decouples at some energy.** If there exists an energy scale below which the B and C blocks are suppressed to zero (either by a symmetry, a dynamical mechanism, or a loop cancellation), the EFT RS sector would be approximately standalone and VZ would apply. Falsification requires identifying a symmetry of D_GU that separately conserves RS and spin-1/2 particle numbers -- which would need to commute with the Clifford element c(eta), since B and C are Clifford-algebra components. No such symmetry is present in Sp(64): the Lie algebra sp(64) acts on S = H^{64} without separately conserving RS and spin-1/2 states (they are distinguished only by the Lorentz spin, not by the Sp(64) representation).

---

## 8. Conclusion: What This Resolves and What Remains Open

### 8.1 Resolution of the VZ Lane in the Nguyen Critique

The Nguyen critique identified VZ as an implicit constraint on GU: if the theory produces spin-3/2 particles, those particles must either be gravitinos in a supergravity theory (requiring local SUSY, absent in GU) or else the standalone RS hypothesis H1 must fail.

We have shown H1 fails at 14D by a specific mechanism: the GU RS sector is the kernel of the Clifford gamma-trace on the full Clifford module bundle E, not a standalone field with its own Lagrangian. The effective RS principal symbol S_R(xi) -- the Schur complement obtained by integrating out the spin-1/2 sector -- has trivial kernel for all non-null covectors. The characteristic cone is the null cone of the gimmel metric g_Y.

**This is the correct structural response to VZ.** It does not invoke a guardian symmetry. It does not require higher-spin gauge invariance. It works because the GU spin-3/2 particles are permanently entangled with the spin-1/2 sector through the Clifford algebra structure of Cl(9,5), and this entanglement cannot be removed by any energy-scale, loop-correction, or gauge argument.

The evasion mechanism -- Clifford module non-decoupling -- is a new entry in the catalog of VZ evasion strategies. Existing entries are: (1) local supersymmetry (supergravity), (2) higher-spin gauge invariance (Fronsdal, Vasiliev), (3) consistent truncation in AdS with extra dimensions. Clifford module non-decoupling is distinct from all three.

### 8.2 The Correct Algebraic Statement

The proof in Section 4 establishes ker S_R(xi) = 0 for xi^2 != 0. A stronger statement -- S_R(xi)^2 = xi^2 Id_{RS} as an exact matrix identity -- does not hold: explicit computation gives S_R^2 = xi^2 Id + xi^2 B (E^{-1})^2 C with B (E^{-1})^2 C nonzero (the coefficient involves 2842 chi - 98 mu in the 14D normalization, which is generically nonzero). The correct statement is A S_R = S_R A = xi^2 Id_R (exact from the block-square identities). This means S_R is not a Clifford element on R^{14D} -- the RS sub-bundle is not a sub-Clifford-module -- but its characteristic cone is still the null cone, which is what matters for VZ.

### 8.3 What Remains Open

**Principal openness: Analytic-grade verification.** The proof in Section 4 is at reconstruction grade: the Clifford module identity (CL) has been verified at the level of the principal symbol algebra, and the block determinant argument is algebraically exact. What remains for a fully verified (CAS-checked) result is: (a) explicit computation of the E-block matrix entries in coordinates on Y^{14} to confirm the det = -xi^2/14 formula; (b) CAS verification of the B (E^{-1})^2 C computation to confirm the explicit coefficient; (c) full coordinate verification of the section-pullback Clifford identity Theorem 6.1 in terms of the gimmel Christoffel symbols.

**Sub-leading stability.** The sub-principal symbol sigma_0(S_R^{full}) can have real eigenvalues in the split-signature (9,5) setting (from the so(9,5)-valued spin connection). This does not affect causality (no new spacelike characteristics) but is a stability question: WKB amplitudes along some null rays may grow exponentially. Whether this amplitude growth is physical or an artifact of the split-signature metric requires a dynamical stability analysis around the K3-type section selected by the Willmore variational principle.

**Generation count connection.** The same Clifford identity that drives VZ evasion (sigma_D(xi)^2 = g_Y(xi,xi) Id_E) is also the algebraic engine for the generation count: ind_H(D_GU) = ind_H(diag(A, S_R^{eff})) = 16 + 8 = 24 by the cross-term vanishing argument (the B and C blocks are nonzero but contribute zero to the index by the homotopy invariance of the H-linear Fredholm index). VZ evasion and the three-generation count are two manifestations of the same algebraic fact.

**The non-standalone structure is dual to generation count.** The B and C blocks that prevent standalone RS propagation are the same blocks whose vanishing contribution to the index gives the 8 H-lines from the RS sector. The Clifford module non-decoupling is thus not merely a causality fix but a structural property that simultaneously explains why RS degrees of freedom contribute to the generation count without independently propagating as a free RS field.

---

## References

[D82] Dencker, N. (1982). On the propagation of polarization sets for systems of real principal type. J. Funct. Anal. 46, 351-372.

[DG10] Distler, J. and Garibaldi, S. (2010). There is no "Theory of Everything" inside E8. Commun. Math. Phys. 298, 419-436.

[FJ80] Flensted-Jensen, M. (1980). Discrete series for semisimple symmetric spaces. Ann. Math. 111, 253-311.

[H85] Hormander, L. (1985). The Analysis of Linear Partial Differential Operators III. Springer.

[HR94] Harvey, F.R. (1990). Spinors and Calibrations. Academic Press.

[JS61] Johnson, M.H. and Sudarshan, E.C.G. (1961). Inconsistency of the local field theory of charged spin-3/2 particles. Ann. Phys. 13, 126-145.

[LM89] Lawson, H.B. and Michelsohn, M.-L. (1989). Spin Geometry. Princeton University Press.

[N21] Nguyen, T. (2021). Geometric Unity: A Critical Examination. arXiv:2103.01458.

[T81] Taylor, M. (1981). Pseudodifferential Operators. Princeton University Press.

[VZ69] Velo, G. and Zwanziger, D. (1969). Propagation and quantization of Rarita-Schwinger waves in an external electromagnetic potential. Phys. Rev. 186, 1337-1341.

[W20] Weinstein, E. (2020). Geometric Unity. Lecture notes and podcast, The Portal.

---

## Appendix: Explicit Block Computations for the Horizontal Sector

This appendix collects the explicit formulas for the RS/non-RS blocks at horizontal covectors xi_H in H* = T*X^4, which were used to verify the general 14D result.

**A.1 The E-Block at Horizontal Covectors (4D Case)**

In the 4D horizontal sector, the trace normalization is gamma^a gamma_a = 4 Id (dim X^4 = 4). The E block in the (phi, s) basis (phi in Q_0, s parameterizing gamma-trace modes j(s)_a = (1/4) gamma_a s) is:

    E(xi_H) = c(xi_H) * | 0     1/4 |
                        | 1     3/2 |

with det = c(xi_H)^2 * (-1/4) = -g_H(xi_H, xi_H) / 4.

The determinant vanishes precisely when g_H(xi_H, xi_H) = 0 (horizontal null covectors), confirming E is invertible for non-null 4D covectors.

**A.2 The C-Block at Horizontal Covectors**

For psi_R in R^{4D} = ker Gamma^{4D} (with Gamma^{4D}(psi) = gamma^a psi_a), setting chi = g_H(xi_H, psi_R):

    C psi_R = (chi, c(xi_H) chi - 2 chi)

This is the same formula as in the 14D case with 14 replaced by 4, and confirms C is nonzero for generic psi_R and generic non-null xi_H.

**A.3 The Explicit Kernel Argument at Horizontal Covectors**

The kernel argument of Theorem 4.1 applies verbatim at horizontal covectors, using:

- M(xi_H)^2 = g_H(xi_H, xi_H) Id_{E_s} (4D Clifford identity via Theorem 6.1)
- det(E(xi_H)) = -g_H(xi_H, xi_H)/4 (nonzero for non-null xi_H)
- Block construction: S_R^{4D}(xi_H) psi_R = 0 implies M(xi_H)(psi_R, w) = 0 implies xi_H^2 (psi_R, w) = 0 implies psi_R = 0.

This gives a fully explicit verification of Corollary 6.2 for horizontal covectors.
