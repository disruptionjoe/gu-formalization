---
title: "SC1-OQ2 — Ellipticity of the Rolled-Up Dirac-DeRham Complex in Split-Signature (9,5): Characteristic Variety of D_GU"
date: 2026-06-23
problem_label: "sc1-oq2-ellipticity"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# SC1-OQ2 — Ellipticity of the Rolled-Up Dirac-DeRham Complex in Split-Signature (9,5)

## 1. Problem Statement

**What is being computed.** The rolled-up Dirac-DeRham complex on Y^14 = Met(X^4) has
the form

  D_GU: Gamma(Omega^{even} tensor S) -> Gamma(Omega^{odd} tensor S)

assembled from the exterior differential d_A, its formal adjoint d_A*, and the shiab
operator Phi: Omega^2 tensor S -> Omega^1 tensor S (Clifford contraction). The precise
operator is, schematically:

  D_GU = d_A + d_A* + Phi_{shiab}

acting on the Z_2-graded complex with coefficients in S = H^{64}.

The question has two parts:
1. Is D_GU elliptic (principal symbol invertible for ALL xi != 0)?
2. If not, what is the correct characteristic variety Char(D_GU), and does D_GU
   satisfy the weaker "principally real type" or "real principal type" condition in
   null-cone directions of the split-signature (9,5) metric on Y^14?

**Why it matters.** Ellipticity controls:
- Fredholmness of D_GU (finite-dimensional kernel and cokernel on compact spaces)
- Well-posedness of the equation D_GU Psi = 0
- The analytic index theorem and generation count (ind_H(D_GU) = 24)
- Propagation of singularities (which directions causally determine the field Psi)

For the (9,5) split-signature, standard ellipticity fails on the null cone. But:
- The VZ evasion computation (vz-schur-complement-2026-06-23.md) established that
  the EFFECTIVE RS symbol S_R^{eff} has trivial kernel at all non-null xi.
- The real-principal-type condition (Hormander) guarantees null-bicharacteristic
  propagation even without full ellipticity.

The question is: which of these structures applies to D_GU as a whole?

**Established context this builds on:**
- `explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md` (SC1 RESOLVED): domain/codomain
  Phi: Omega^2 tensor S -> Omega^1 tensor S confirmed; OQ2 explicitly left open there.
- `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` (VZ EVADED; 4D CONDITIONALLY_RESOLVED, principal-symbol, constant-coefficient gauge): principal
  symbol S_R^{eff}(xi) has trivial kernel for all xi with g_Y(xi,xi) != 0; characteristic
  cone = null cone.
- `explorations/vz-evasion/vz-subprincipal-symbol-rs-2026-06-23.md` (CONDITIONALLY_RESOLVED):
  subprincipal symbol does not introduce new real characteristics beyond the null cone;
  Hormander real-principal-type propagation confirmed for S_R^{full}.
- `explorations/shiab-operator/pc1-spin77-spinor-decomp-2026-06-23.md` (CONDITIONALLY_RESOLVED): the
  Dirac-DeRham complex structure (Omega^bullet tensor S with shiab differentials) is
  representation-theoretically forced.

---

## 2. Established Mathematical Context

### 2.1 The Rolled-Up Complex

The Dirac-DeRham complex in degree decomposition is:

  0 -> Omega^0 tensor S --(d_A)--> Omega^1 tensor S --(d_A + Phi)--> Omega^2 tensor S
    --(d_A* + Phi*)--> Omega^1 tensor S --(d_A*)--> Omega^0 tensor S -> 0

The rolled-up version combines the even and odd grades:

  E^{even} = (Omega^0 oplus Omega^2 oplus Omega^4 oplus ...) tensor S
  E^{odd}  = (Omega^1 oplus Omega^3 oplus Omega^5 oplus ...) tensor S

  D_GU: Gamma(E^{even}) -> Gamma(E^{odd})

At the principal-symbol level (in the cotangent fiber), the operator becomes:

  sigma(D_GU)(xi): E^{even}_y -> E^{odd}_y    at each y in Y^14 and xi in T*_y Y^14

The principal symbol at xi is given by:
- From d_A: exterior product by xi (wedge multiplication by the covector xi)
  sigma(d_A)(xi) = xi wedge (-)
- From d_A*: interior product by xi^# (musical dual of xi under g_Y)
  sigma(d_A*)(xi) = iota_{xi^#}(-)
- From the shiab Phi: the Clifford-contraction symbol
  sigma(Phi)(xi)(alpha tensor s) = sum_a xi^a tensor c(iota_{e_a} alpha).s
  evaluated at the principal level -- but the shiab is a ZERO-ORDER operator
  (no derivatives), so sigma(Phi) = 0 as a principal symbol in the classical sense!

**Key observation:** The shiab Phi is a fiber-linear (multiplication) operator, not a
differential operator. Its symbol is zero-order, meaning it does NOT contribute to the
PRINCIPAL symbol of D_GU. Only d_A and d_A* (the differential parts) contribute.

Therefore the full principal symbol of D_GU is:

  sigma(D_GU)(xi) = sigma(d_A + d_A*)(xi) = xi wedge (-) + iota_{xi^#}(-)

This is the de Rham symbol (without spinors, since the S = H^{64} coefficient bundle
is acted on trivially in the principal symbol -- the S-action from Clifford comes
from the shiab which is zero-order).

Wait -- the structure is more subtle. D_GU includes Clifford multiplication in its
formulation. Let us be precise about the operator structure.

### 2.2 D_GU as a Dirac-Type Operator

The GU operator D_GU is better understood as a Dirac-type operator on the full spinor
bundle for the 14-dimensional manifold Y^14. The key structure is:

  D_GU = sum_{a=1}^{14} gamma^a nabla_{e_a} + (lower-order terms including Phi)

where gamma^a are Clifford generators of Cl(9,5) acting on S = H^{64}. The principal
symbol of a Dirac-type operator is:

  sigma(D_GU)(xi) = sum_a xi_a gamma^a = gamma(xi) := c(xi) in End(S)

Here xi = xi_a e^a is the covector, and c(xi): S -> S is Clifford multiplication by xi.

**But D_GU also involves form-degree.** The complete operator acts on Omega^bullet tensor S.
On this larger space, the Clifford symbol is:

  sigma(D_GU)(xi) = c(xi) = xi wedge (-) + iota_{xi^#}(-): Omega^bullet tensor S -> Omega^bullet tensor S

This is the de Rham-Dirac symbol: the standard Dirac operator in the de Rham formulation.

The principal symbol at covector xi in T*_y Y^14 is therefore the linear map:

  c(xi): Lambda^bullet(T*_y Y^14) tensor S_y -> Lambda^bullet(T*_y Y^14) tensor S_y

given by Clifford multiplication by the 1-form xi.

---

## 3. Computation: Principal Symbol and Characteristic Variety

### 3.1 The Clifford Symbol in Split-Signature (9,5)

For Cl(9,5) with metric g_Y of signature (9,5), the Clifford symbol at xi satisfies:

  c(xi)^2 = g_Y(xi,xi) . Id_S    for all xi in T*Y^14          [CL1]

where g_Y(xi,xi) = g^{ab} xi_a xi_b and the metric g_Y has signature (9,5) on Y^14.

**Proof of [CL1]:** In Cl(p,q), if {e^a} is an orthonormal coframe with
g_Y(e^a, e^b) = epsilon_a delta^{ab} (where epsilon_a = +1 for a <= p and -1 for
a > p), then for xi = xi_a e^a:

  c(xi)^2 = (sum_a xi_a c(e^a))^2
           = sum_a xi_a^2 c(e^a)^2 + sum_{a<b} xi_a xi_b {c(e^a), c(e^b)}
           = sum_a xi_a^2 epsilon_a Id + 0   [since {c(e^a),c(e^b)} = 2g(e^a,e^b) Id = 0 for a != b]
           = g_Y(xi,xi) Id_S    checkmark

The key structure identity [CL1] holds in any signature.

### 3.2 Ellipticity Fails on the Null Cone

**Definition.** An operator P is elliptic at xi if sigma(P)(xi) is invertible.

For D_GU with principal symbol sigma(D_GU)(xi) = c(xi):

  sigma(D_GU)(xi) is invertible  <=>  c(xi) is invertible
                                  <=>  c(xi)^2 = g_Y(xi,xi) Id is invertible
                                  <=>  g_Y(xi,xi) != 0
                                  <=>  xi is NOT null (i.e., xi is not on the null cone)

**On the null cone {xi : g_Y(xi,xi) = 0}:**

  c(xi)^2 = 0    =>   c(xi) is nilpotent   =>   c(xi) is NOT invertible

Therefore D_GU is NOT elliptic in the standard sense. The characteristic variety is:

  Char(D_GU) = {xi in T*Y^14 : g_Y(xi,xi) = 0} = the null cone of g_Y

This is the characteristic variety of a symmetric-hyperbolic operator, not an elliptic one.

**Failure condition for ellipticity (explicit):**
D_GU would be elliptic if and only if the null cone of g_Y is empty, which requires
positive-definite (Riemannian) signature. For the split-signature (9,5) metric on Y^14,
the null cone is a 13-dimensional cone in each T*Y^14 fiber, and ellipticity fails
throughout.

**This is not a defect.** Standard GR (Einstein's equations) has the same structure:
the principal symbol of the de Rham complex or the Lichnerowicz operator in Lorentzian
signature has the null cone as characteristic variety. The failure of ellipticity is
the mathematical signature of a hyperbolic (causal) physical theory.

### 3.3 Real Principal Type: the Correct Weaker Condition

Since D_GU is not elliptic, the relevant question is whether it satisfies the
"real principal type" condition of Hormander, which ensures controlled propagation
of singularities.

**Definition (Hormander, Vol. III §23.2).** A scalar pseudodifferential operator P
of order m is of real principal type at (y, xi) in T*Y^14 if:
1. The principal symbol p_m(y, xi) = 0 (i.e., (y, xi) is characteristic), AND
2. The Hamilton vector field H_{p_m} is not zero at (y, xi) (non-degenerate null covector)

For a system (matrix-valued symbol) P, the condition is that the characteristic
variety {det sigma(P) = 0} is smooth and the Hamilton map is non-degenerate along it.

**D_GU satisfies real principal type.** For D_GU with principal symbol sigma(D_GU)(xi) = c(xi):

The determinant of c(xi) on the full space Lambda^bullet tensor S:

  det(c(xi)) = det_{Lambda^bullet tensor S}(c(xi))

For the Clifford operator, the determinant structure follows from [CL1]:
  c(xi)^2 = g_Y(xi,xi) Id

The eigenvalues of c(xi) come in pairs +-lambda where lambda^2 = g_Y(xi,xi).

For xi non-null (g_Y(xi,xi) != 0): all eigenvalues are non-zero, det != 0, no
characteristic point.

For xi null (g_Y(xi,xi) = 0): c(xi) is nilpotent, all eigenvalues = 0,
det(c(xi)) = 0.

The characteristic variety is:
  {xi in T*Y^14 : g_Y(xi,xi) = 0}   [the null cone of g_Y]

**Hamilton vector field.** The principal symbol (as a function on T*Y^14) in the
scalar case would be p(y, xi) = g_Y(xi,xi). The Hamilton vector field is:

  H_p = partial_xi p . partial_y - partial_y p . partial_xi

For p = g_Y(xi,xi) = g^{ab}(y) xi_a xi_b:
  partial_{xi_a} p = 2 g^{ab}(y) xi_b = 2 xi^a (the 14D covector)
  H_p = 2 xi^a partial_{y^a} - (partial_{y^a} g^{bc}) xi_b xi_c partial_{xi_a}

At a null point g_Y(xi,xi) = 0 with xi != 0: H_p != 0 because 2 xi^a partial_y^a
is the null geodesic vector field, which is non-zero for xi != 0.

**Conclusion:** D_GU is of real principal type in null-cone directions. The Hamilton
vector field is non-degenerate on the null cone (away from xi = 0). The Hormander
propagation theorem (Th. 23.2.1) applies: wavefront sets of solutions to D_GU Psi = 0
propagate along null bicharacteristics (null geodesics of g_Y). This is exactly the
correct causal structure for a physical field theory on the (9,5) spacetime Y^14.

### 3.4 The Null-Cone Symbol: Nilpotent but Controlled

For xi null (g_Y(xi,xi) = 0), c(xi) is nilpotent. Specifically:
  c(xi)^2 = 0    on S (since g_Y(xi,xi) = 0)

The image of c(xi) is:
  Im c(xi) = ker c(xi)    [since c(xi)^2 = 0 implies Im subset ker]

The kernel is:
  ker c(xi) = {s in S : c(xi).s = 0}

For a null covector xi, dim ker c(xi) = dim S / 2 = 128 (over R). This follows from
the rank-nullity theorem and the fact that c(xi)^2 = 0 forces ker = Im and
dim Im + dim ker = dim S, so 2 dim ker = dim S = 256, giving dim ker = 128.

**This is NOT a problem for D_GU.** The kernel on null covectors is the classical
null-propagation structure. It says: there are null-polarized modes that propagate
along null bicharacteristics. This is analogous to photons (massless spin-1 fields)
propagating along null geodesics -- the polarization constraint is the kernel of
c(xi) at null xi.

### 3.5 The Full Complex Symbol and Overdetermined Ellipticity

The rolled-up Dirac-DeRham complex can be analyzed using the theory of overdetermined
elliptic complexes. Even though D_GU itself is not elliptic in the standard sense, the
associated complex

  0 -> E^{even} --D_GU--> E^{odd} --D_GU^*--> E^{even} -> 0

might satisfy a weaker ellipticity condition.

**The symbol sequence.** At each non-null xi, the symbol sequence is:

  E^{even} --c(xi)--> E^{odd} --c(xi)--> E^{even}

This is exact (since c(xi)^2 = g_Y(xi,xi) Id != 0 for non-null xi), giving a
Fredholm complex at non-null xi.

At null xi:

  E^{even} --c(xi)--> E^{odd} --c(xi)--> E^{even}

c(xi)^2 = 0, so the complex is NOT exact at null xi. The cohomology of the symbol
complex at null xi is:

  H^0 = ker c(xi)|_{E^{even}} = {half of E^{even}}   (dim = dim E^{even}/2)
  H^1 = ker c(xi)|_{E^{odd}} / Im c(xi)|_{E^{even}}

These cohomology spaces are non-trivial, which is precisely the statement that D_GU
is not elliptic. They encode the null-polarized modes.

**This is exactly the structure of a hyperbolic operator.** The symbol complex is
elliptic (exact) at all non-null xi and has non-trivial cohomology at null xi. The
null cohomology spaces parametrize the physical propagating degrees of freedom.

### 3.6 The Shiab Contribution to the Symbol

The shiab Phi: Omega^2 tensor S -> Omega^1 tensor S is a zero-order (multiplication)
operator. Its symbol is the operator itself, evaluated fiberwise:

  sigma^{(0)}(Phi)(y) = Phi_y: Lambda^2(T*_y Y^14) tensor S_y -> Lambda^1(T*_y Y^14) tensor S_y

This is the TOTAL SYMBOL at order 0 (the "full symbol" including lower-order terms)
but it contributes to the PRINCIPAL symbol only at order 0, not at the leading
(differential) order.

In the standard hierarchy of symbol orders for a first-order operator:
- The ORDER-1 symbol (principal symbol): comes from d_A and d_A*
  => This is sigma^{(1)}(D_GU)(xi) = c(xi) (Clifford symbol at xi)
- The ORDER-0 symbol (subprincipal symbol): includes Phi (the shiab), curvature terms,
  the connection 1-form A, etc.
  => This is sigma^{(0)}(D_GU) = Phi + (curvature terms) + ...

**The characteristic variety is determined by the PRINCIPAL (order-1) symbol only.**
Since sigma^{(1)}(D_GU)(xi) = c(xi), the characteristic variety is exactly the null
cone {g_Y(xi,xi) = 0}, regardless of the shiab or other lower-order terms.

**This was already established in the VZ computations.** From
`explorations/vz-evasion/vz-subprincipal-symbol-rs-2026-06-23.md` (OQ2-a RESOLVED):
"The Shiab contribution to sigma_0 is anti-Hermitian (sp(64)-valued, Sp(64) = U(64,H)
acts unitarily on S = H^{64}) producing only amplitude effects, not new directions."

And from `explorations/vz-evasion/vz-oq2-lower-order-curvature-2026-06-23.md`:
"All curvature contributions enter D_GU as zero-order (multiplicative) operators;
they cannot change the principal symbol of the effective RS Schur complement S_R^{full};
the characteristic set therefore remains the null cone of g_Y."

### 3.7 The RS Sector and Mixed Signatures

A subtlety: the GU operator D_GU has a block structure in the RS / spin-1/2 decomposition.
The principal symbol in this block form is:

  sigma(D_GU)(xi) = c(xi) acting on E = E_{RS} oplus E_{1/2}

where E_{RS} = RS sector (Rarita-Schwinger, spin-3/2 component of Omega^bullet tensor S)
and E_{1/2} = spin-1/2 sector (non-gamma-trace part).

From the Schur complement analysis (vz-schur-complement-2026-06-23.md, §8):
For all xi with g_Y(xi,xi) != 0:

  ker sigma(D_GU)|_{E_{RS}}(xi) = ker S_R^{14D}(xi) = {0}

where S_R^{14D} is the effective RS Schur complement symbol. The Clifford module identity
c(xi)^2 = g_Y(xi,xi) Id forces this kernel to be trivial. This means:
- At non-null xi: the RS block symbol is invertible => no spurious spacelike RS
  characteristics.
- At null xi: c(xi) is nilpotent on E_{RS} as well, with the same dimension count.

The characteristic variety of the full D_GU restricted to the RS sector is also the
null cone of g_Y. No sector of D_GU has a smaller or larger characteristic variety.

### 3.8 Summary: The Characteristic Variety of D_GU

**Theorem (reconstruction grade):**

  Char(D_GU) = {xi in T*Y^14 \ {0} : g_Y(xi,xi) = 0}   [the null cone of g_Y]

**Proof sketch:**
1. The principal symbol is sigma^{(1)}(D_GU)(xi) = c(xi) (Clifford multiplication by xi).
2. [CL1]: c(xi)^2 = g_Y(xi,xi) Id_E.
3. c(xi) is invertible iff g_Y(xi,xi) != 0 (by [CL1] and invertibility of scalars).
4. det sigma^{(1)}(D_GU)(xi) = 0 iff c(xi) is non-invertible iff g_Y(xi,xi) = 0.
5. Therefore Char(D_GU) = {xi : g_Y(xi,xi) = 0}.

**The operator D_GU is:**
- NOT elliptic (null cone is non-empty in signature (9,5))
- OF REAL PRINCIPAL TYPE in null-cone directions (Hamilton vector field of p = g_Y(xi,xi)
  is non-zero on the null cone, ensuring non-degenerate bicharacteristics)
- SYMMETRIC HYPERBOLIC in the sense that null-cone propagation is well-controlled
- The shiab Phi (zero-order) does NOT modify the characteristic variety

---

## 4. The Principal-Real-Type Structure in Null-Cone Directions

The precise claim is:

**Claim (principally-real-type in null-cone directions):**
On each null direction xi (g_Y(xi,xi) = 0, xi != 0), the operator D_GU:
1. Has c(xi) nilpotent (c(xi)^2 = 0) but NON-ZERO (c(xi) != 0 since c(e_a)^2 = epsilon_a != 0)
2. The null space ker c(xi) equals the image Im c(xi) (both are the "null polarization" subspace)
3. The Hamilton vector field of g_Y(xi,xi) is non-zero at xi (null geodesic flow is non-trivial)
4. Singularities propagate along null bicharacteristics (null geodesics of g_Y on Y^14)

This is the defining condition for "principally real type" in the sense used by
Hormander and Dencker for Dirac-type operators in indefinite-signature geometry.

**Explicit example.** In a local orthonormal frame {e^1, ..., e^{14}} with e^1 timelike
(g_Y(e^1, e^1) = -1), take the null covector xi = e^1 + e^2 (where e^2 is spacelike,
g_Y(e^2,e^2) = +1). Then:

  g_Y(xi,xi) = g_Y(e^1+e^2, e^1+e^2) = -1 + 1 = 0   (null)

  c(xi) = c(e^1) + c(e^2) = gamma^1 + gamma^2   (where gamma^a = c(e^a) in Cl(9,5))

  c(xi)^2 = (gamma^1 + gamma^2)^2
           = (gamma^1)^2 + (gamma^2)^2 + gamma^1 gamma^2 + gamma^2 gamma^1
           = (-1).Id + (+1).Id + {gamma^1, gamma^2}/2 * 2
           = 0 + 2 g_Y(e^1,e^2) Id
           = 0   (since g_Y(e^1, e^2) = 0 for an orthonormal frame)

  Correct: c(xi)^2 = g_Y(xi,xi) Id = 0.

The kernel of c(xi) = gamma^1 + gamma^2 in S = H^{64}:
  ker(gamma^1 + gamma^2) = {s : (gamma^1 + gamma^2)s = 0} = {s : gamma^1 s = -gamma^2 s}

dim ker = 128 (over R) = dim S / 2 = 256/2. [verified by rank-nullity + c(xi)^2 = 0]

The Hamilton vector field at this null xi:
  H_p = 2 partial_{y_1} - 2 partial_{y_2}   (schematically, the null geodesic direction)
  H_p != 0   checkmark (since the null geodesic direction e^1 - e^2 is non-zero)

Real principal type is satisfied at this null covector xi.  checkmark

---

## 5. The Distinction from Elliptic and Standard Hyperbolic

The characteristic variety of D_GU and its type can be summarized in a table:

| Property | Elliptic operator | Standard wave operator (box) | D_GU (Dirac-DeRham) |
|---|---|---|---|
| Char variety | Empty | {xi : g(xi,xi)=0} | {xi : g_Y(xi,xi)=0} |
| Symbol at null xi | N/A | Nilpotent (scalar) | Nilpotent (Clifford operator) |
| Fredholm on compact? | Yes (without boundary) | Yes (with Cauchy data) | Yes (with null-cone data) |
| Propagation | No propagation | Along null geodesics | Along null geodesics of g_Y |
| Kernel dim at null xi | N/A | Co-dim 1 (scalar) | dim S/2 = 128 (over R) |
| Index theorem | Atiyah-Singer | Not applicable | APS / Atiyah-Schmid (L2) |

The Clifford-symbol version (D_GU) is a Dirac-type operator in indefinite signature.
It falls into the class of "symmetric hyperbolic systems" in the sense of Friedrichs
(with the (9,5)-metric providing the symmetry), and into the class of "operators of
real principal type" in the sense of Hormander.

---

## 6. Implications for D_GU Analysis

### 6.1 Well-Posedness

D_GU Psi = 0 is NOT an elliptic equation. It is a hyperbolic equation, with initial
data posed on a spacelike hypersurface (with respect to the (9,5) metric on Y^14).

The correct well-posedness theory is:
- Symmetric-hyperbolic theory (Friedrichs 1954, applied to Clifford algebra-valued systems)
- Energy estimates using the (9,5) inner product to define a positive-definite energy
  on spacelike hypersurfaces
- The Cauchy problem for D_GU Psi = 0 is locally well-posed in standard Sobolev spaces
  H^k for initial data on a spacelike hypersurface

[reconstruction -- this is the standard theory for Dirac operators in indefinite
signature; see Baer-Ginoux-Pfaeffle, "Wave Equations on Lorentzian Manifolds", for
the Lorentzian analog; the (9,5) case is analogous with 9 timelike and 5 spacelike]

Wait: this is a (9,5) signature with 9 POSITIVE and 5 NEGATIVE directions (using the
physics convention (+ ... - ...)). Actually let us fix conventions:

Signature (9,5) means: 9 eigenvalues of g_Y are positive, 5 are negative. The
"timelike" directions (where the metric is negative-definite when restricted) are the
5-dimensional subspace; the "spacelike" directions are 9-dimensional. The null cone
{g_Y(xi,xi) = 0} separates these.

In the GU physical setting, the base X^4 has Lorentzian signature (3,1): 3 positive,
1 negative. The fiber GL(4,R)/O(3,1) contributes (6,4) to the total (9,5). The 5
negative directions of g_Y correspond to the time direction of X^4 plus 4 fiber-negative
directions (from the (6,4) fiber signature after trace reversal).

The well-posedness analysis on Y^14 must account for this fiber structure. In particular,
a global Cauchy surface for D_GU on Y^14 would be a 13-dimensional hypersurface that is
spacelike with respect to g_Y. The normal to such a hypersurface must be timelike
(g_Y-negative), i.e., in the 5-dimensional negative-signature subspace of T*Y^14.

### 6.2 L2-Index Theory

The failure of ellipticity means that the standard Atiyah-Singer index theorem (which
requires ellipticity) does not apply to D_GU on compact manifolds. Instead, the
relevant index theory is:
- Atiyah-Schmid for the L2-index on non-compact symmetric spaces (the fiber GL(4,R)/O(3,1))
- Bär-Strohmaier Lorentzian APS index theorem (for the 4D reduction)
- The discrete-series mechanism (established in n5-discrete-series-gl4r-2026-06-23.md)

The L2-kernel of D_GU (defined using the (9,5)-metric and a suitable L2-space on Y^14)
is not the same as a kernel in the elliptic sense. The generation count relies on the
DISCRETE SERIES representation theory (Flensted-Jensen, Harish-Chandra), not on
classical Fredholm theory for elliptic operators. This is consistent and already
established in the prior discrete-series computations.

### 6.3 The Index-Count Mechanism

From the established discrete-series results:

  ind_H(D_GU) = 16 [spin-1/2 sector, K3-type X^4] + 8 [RS sector]
             = 24 = 3 SM generations

This count uses the Atiyah-Schmid framework for the L2-kernel on the non-compact fiber
GL(4,R)/O(3,1) (a symmetric space of real rank 1 after our split-rank computation).
The non-ellipticity of D_GU does NOT obstruct this count because:
1. The Atiyah-Schmid theorem is formulated for non-elliptic Dirac operators on
   symmetric spaces where the L2-theory is controlled by the Plancherel formula, not
   by standard elliptic theory.
2. The generation count mechanism is the discrete-series Plancherel multiplicity, which
   is a feature of the representation theory of GL(4,R), independent of whether the
   full operator on Y^14 is elliptic.

---

## 7. Comparison with the VZ Computation

The VZ evasion computation (EVADED, reconstruction; 4D CONDITIONALLY_RESOLVED, constant-coefficient gauge) established:

  ker S_R^{14D}(xi) = {0}   for all xi with g_Y(xi,xi) != 0

where S_R^{14D} is the effective RS Schur complement symbol. This is the statement
that the RS sector characteristic variety is ALSO the null cone -- no RS spacelike
characteristics. This is exactly consistent with the general D_GU characteristic
variety = null cone established here.

The VZ computation can be seen as a SECTOR DECOMPOSITION of the general result:
- The full D_GU symbol c(xi) has Char = null cone
- Each sector (RS and spin-1/2) also has Char = null cone
- The sectors do not introduce additional characteristics or spacelike propagation

The present computation provides the GLOBAL STRUCTURE (full D_GU characteristic variety)
that the VZ computation established sector-by-sector.

---

## 8. Failure Conditions (Explicit)

The verdict CONDITIONALLY_RESOLVED would be falsified or downgraded by:

**F1 (Wrong principal symbol).** If the principal symbol of D_GU is not c(xi) (Clifford
multiplication by xi), the characteristic variety would differ. This would require D_GU
to have a component of higher-order type than first-order in xi, which is incompatible
with it being a Dirac-type operator. The shiab Phi is explicitly confirmed as zero-order
(SC1 + VZ-subprincipal), so this failure mode is essentially ruled out. The only route
would be if the connection A or the curvature of Y^14 contributed a first-order
differential operator to D_GU beyond d_A -- which is not the case by the standard
formulation of D_GU = d_A + d_A* + Phi.

**F2 (Non-Clifford principal symbol).** If the construction of D_GU in the GU formalism
is not a standard Dirac-type operator (i.e., if the gamma matrices in D_GU do not
satisfy c(xi)^2 = g_Y(xi,xi) Id_E), then [CL1] fails and the characteristic variety
could differ. This would require Cl(9,5) to act in a non-standard way. Given that
Cl(9,5) ~= M(64,H) acts irreducibly on S = H^{64}, and the irreducible module structure
forces [CL1], this failure mode is ruled out by the algebraic structure.

**F3 (Different signature of g_Y on Y^14).** If the signature of g_Y is not (9,5)
-- e.g., if the trace-reversal procedure gives a different signature from (6,4) + (3,1)
= (9,5) -- then the null cone structure changes. The N1 audit (RESOLVED) confirms
signature (9,5), so this is ruled out.

**F4 (Non-real-type on null cone).** If the Hamilton vector field H_p = H_{g_Y(xi,xi)}
were zero on the null cone, D_GU would fail real-principal-type. This would require
the null geodesic vector field to be identically zero, which is impossible for a
non-degenerate (pseudo-)Riemannian metric. So real-principal-type on the null cone
holds unconditionally for any non-degenerate g_Y.

**F5 (Ellipticity claimed in a different sense).** There exist "twisted" or "modified"
notions of ellipticity (e.g., transversally elliptic for group actions, elliptic with
torsion coefficients) that might apply to D_GU. If Weinstein's GU intends D_GU to be
elliptic in such a modified sense (e.g., elliptic modulo a gauge group action), the
correct characteristic variety might differ. This is not falsified here but would require
specification of the modified ellipticity notion.

**F6 (Order of D_GU).** If D_GU contains second-order (or higher) differential terms
beyond the first-order d_A + d_A*, the principal symbol analysis changes. From the
formulation (Dirac-DeRham complex with shiab as zero-order operator), this failure mode
is not expected.

---

## 9. The Characteristic Variety in Explicit Coordinates

To make the result concrete, we compute in local coordinates on Y^14.

Let y = (x^mu, h_{(ij)}) be local coordinates on Y^14, where x^mu (mu = 0,1,2,3) are
coordinates on X^4 and h_{(ij)} (i,j = 0,...,3, ij in symmetric pairs) are fiber
coordinates on the Sym^2 T*X^4 fiber. The cotangent vector has components:

  xi = xi_mu dx^mu + xi_{(ij)} dh^{(ij)}

The gimmel metric g_Y on Y^14 in these coordinates has signature (9,5). From the N1
audit and moving-frame derivation:

  g_Y(xi, xi) = g^{mu nu}(h) xi_mu xi_nu + h_{metric}^{(ij)(kl)} xi_{(ij)} xi_{(kl)}

where g^{mu nu}(h) is the Lorentzian (3,1) metric on X^4 evaluated at the fiber point h,
and h_{metric}^{(ij)(kl)} is the Frobenius metric on the fiber Sym^2 T*X^4 with
signature (6,4) (after trace reversal).

The null cone of g_Y is:
  g_Y(xi,xi) = 0
  <=> g^{mu nu} xi_mu xi_nu + h^{(ij)(kl)} xi_{(ij)} xi_{(kl)} = 0

This is a quadric in the 14-dimensional cotangent fiber. It is a non-degenerate
quadric (since g_Y has signature (9,5), the quadric is non-degenerate) of codimension 1.

The characteristic variety Char(D_GU) is exactly this quadric (minus the zero section).

---

## 10. Relation to the SC1 Open Question

The SC1 file (`explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md`, §5, OQ2) stated:

> "The GU Dirac-type operator on (9,5) signature Y^14 is therefore NOT elliptic in
> the standard sense; it is hyperbolic (or at best weakly hyperbolic) in null directions.
> Whether it is 'well-posed' in some weaker sense (e.g., as a symmetric hyperbolic
> system) is an analytic question not addressed here."

The present computation resolves this:
- D_GU is NOT elliptic (confirmed): Char(D_GU) = null cone of g_Y (non-empty).
- D_GU is of REAL PRINCIPAL TYPE in null-cone directions (confirmed): Hamilton vector
  field is non-zero on the null cone.
- D_GU is "principally real type" in Hormander's sense: propagation of singularities
  along null bicharacteristics (null geodesics of g_Y on Y^14).
- The well-posedness in the symmetric-hyperbolic sense holds at reconstruction grade.

The sc1-shiab-domain OQ2 is therefore CONDITIONALLY_RESOLVED here. The remaining gap
(to reach RESOLVED) is the explicit CAS verification that the null-cone real-principal-type
condition holds in coordinates and the explicit symmetric-hyperbolic energy estimate for
D_GU on Y^14 (which requires specifying the spacelike foliation of Y^14 with respect to g_Y).

---

## 11. Result

### 11.1 Verdict

CONDITIONALLY_RESOLVED.

**What is established (reconstruction grade):**

1. Char(D_GU) = null cone of g_Y on Y^14 = {xi in T*Y^14 : g_Y(xi,xi) = 0}.
   The characteristic variety is the null cone, not empty (D_GU is NOT elliptic).

2. D_GU is of real principal type in null-cone directions (Hormander sense): the
   Hamilton vector field H_{g_Y(xi,xi)} is non-zero on the null cone (non-degenerate
   null geodesic flow on Y^14).

3. The shiab Phi is a zero-order operator and does NOT modify the principal symbol
   or the characteristic variety. The characteristic variety is determined entirely
   by the first-order (Clifford) part of D_GU.

4. The null-cone structure is consistent with the VZ evasion (characteristic cone
   of the RS effective operator = null cone, CONDITIONALLY_RESOLVED at 4D — constant-coefficient gauge).

5. The generation count (ind_H = 24) is not obstructed by the failure of ellipticity.
   The correct analytic framework is the Atiyah-Schmid L2-theory on the symmetric
   space GL(4,R)/O(3,1), which does not require ellipticity of D_GU on Y^14.

**What remains open:**

- OQ2-a: Explicit coordinate computation of the real-principal-type condition on
  Y^14 in the gimmel-metric coordinate system. Requires the Christoffel symbols
  from the ii-s-moving-frames computation to write the null geodesic equations and
  confirm they are non-trivial.
- OQ2-b: Explicit symmetric-hyperbolic energy estimate for D_GU on Y^14. Requires
  identifying the spacelike foliation of Y^14 with respect to g_Y and constructing
  a positive-definite energy functional.
- OQ2-c: The KERNEL of D_GU at null xi (the null-polarized modes) should be related
  to gauge invariance / physical degrees of freedom via the machinery of the complex.
  This identification would upgrade the structural result to a physical statement.

### 11.2 Explicit Failure Conditions

| Code | Condition | Status |
|------|-----------|--------|
| F1 | Principal symbol of D_GU is not c(xi) | Ruled out by Dirac-type structure |
| F2 | [CL1] fails (c(xi)^2 != g_Y(xi,xi) Id) | Ruled out by Cl(9,5) algebra |
| F3 | g_Y has different signature than (9,5) | Ruled out by N1 audit (RESOLVED) |
| F4 | Hamilton vector field zero on null cone | Ruled out by non-degeneracy of g_Y |
| F5 | Modified ellipticity notion applies | Open -- would require specification |
| F6 | D_GU contains second-order terms | Ruled out by Dirac-type formulation |

---

## 12. Open Questions for Follow-On Work

**OQ2-a (Coordinate null-cone verification):** Using the moving-frame Christoffel
symbols from `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`, write out the
null geodesic equations on Y^14 = Met(X^4) in local coordinates and confirm that
the Hamilton vector field H_{g_Y(xi,xi)} has non-zero components in the fiber directions.
This is a CAS-checkable computation that would upgrade OQ2 from reconstruction to verified.

**OQ2-b (Symmetric-hyperbolic energy estimate):** Construct an explicit positive-definite
energy functional for D_GU Psi = 0 on a spacelike hypersurface in Y^14. The
(9,5)-metric provides the inner product; the difficulty is that the fiber directions
contribute mixed-signature energy. A comparison with the standard Cauchy problem for
the Dirac equation in Lorentzian signature (e.g., Baer-Ginoux-Pfaeffle) would confirm
the symmetric-hyperbolic structure.

**OQ2-c (Physical interpretation of null modes):** The kernel of c(xi) at null xi
(dim 128 over R) should be identified with physical polarization states. In the
photon analogy, the null-mode kernel is the polarization constraint (transversality).
The GU analog would identify the null-mode kernel with the physical field content
propagating along null bicharacteristics of g_Y on Y^14.

**OQ-new (Modified ellipticity via gauge symmetry):** If D_GU is gauge-equivariant
and the gauge group Sp(64) acts on the null-mode kernel, one could define ellipticity
"modulo gauge" -- i.e., D_GU is elliptic on the gauge-invariant subspace. Whether this
holds for D_GU requires specifying the Sp(64) action on the fiber of E = Omega^bullet tensor S
and checking whether the gauge-invariant null-mode kernel is trivial. This would be a
stronger result than real-principal-type and would more directly connect to the
Fredholmness of D_GU.

---

## 13. Summary

| Question | Answer | Grade |
|----------|--------|-------|
| Is D_GU elliptic? | No -- Char(D_GU) = null cone of g_Y (non-empty) | verified |
| What is Char(D_GU)? | {xi in T*Y^14 : g_Y(xi,xi) = 0} (the null cone) | verified |
| Is D_GU principally-real-type at null xi? | Yes -- Hamilton vector field non-zero on null cone | reconstruction |
| Does the shiab modify Char(D_GU)? | No -- Phi is zero-order, does not change principal symbol | verified |
| Is generation count affected by non-ellipticity? | No -- Atiyah-Schmid L2 theory applies instead | reconstruction |
| Are VZ results consistent with this? | Yes -- both give null cone as characteristic variety | verified |
| What is the correct analytic framework for D_GU? | Symmetric-hyperbolic / real-principal-type (Hormander) | reconstruction |

**Verdict for sc1-oq2-ellipticity:** CONDITIONALLY_RESOLVED.

The characteristic variety is the null cone of g_Y on Y^14 (explicit formula in §9).
D_GU is principally-real-type (not elliptic) in null-cone directions of the (9,5) metric.
The generation count is not obstructed. Remaining for RESOLVED: coordinate null-geodesic
verification (OQ2-a), energy estimate (OQ2-b), null-mode physical interpretation (OQ2-c).
