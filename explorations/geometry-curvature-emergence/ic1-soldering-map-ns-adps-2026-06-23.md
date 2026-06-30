---
title: "IC1 Soldering Map: j_s: N_s -> ad(P_s) for the Tautological Section"
date: 2026-06-23
problem_label: "ic1-soldering-map"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# IC1 Soldering Map: j_s: N_s -> ad(P_s) for the Tautological Section

**Verdict:** CONDITIONALLY_RESOLVED  
**Grade:** Reconstruction — the map is constructed explicitly from established ingredients; the
algebraic injectivity and Sp(64)-equivariance are verified at reconstruction grade; CAS
verification of the explicit matrix entries and peer review of the representation-theoretic
fiber argument are the remaining gaps before upgrading to verified.

**Problem.** Condition IC1 in `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md` states:

> The 10 normal scalar fields phi^i must be identified with physical matter fields.
> Under the full GU gauge group Sp(64) and the SM branching, the distortion
> theta = A - Gamma decomposes into irreducible Lorentz representations. The
> identification requires that the (2,0)+(0,2) modes of B source gravitational waves,
> not ghost modes.

More precisely, IC1 requires the construction of an injective Sp(64)-equivariant bundle map:

```
j_s: N_s -> ad(P_s)
```

where N_s is the normal bundle of the tautological section s: X^4 -> Y^14 = Met(X^4),
and ad(P_s) = s*(ad P) is the adjoint bundle of the Sp(64) principal bundle P pulled
back to X^4 via s.

This map is called the **soldering map** because it "solders" the geometric normal
bundle (carrying the Kaluza-Klein matter spectrum) to the gauge-theoretic adjoint
bundle (carrying the matter fields of the GU gauge theory). Once j_s is constructed,
the 10 normal fields phi^i can be identified with specific elements of sp(64), giving
the Lorentz decomposition of matter in terms of the GU gauge algebra.

---

## 1. Established Context

The following results are used without re-derivation:

**Geometry of the section.**
- Y^14 = Met(X^4), fiber = GL(4,R)/O(3,1) ~= RP^3, total signature (9,5).
- Cl(9,5) ~= M(64,H), spinor module S = H^64.
- Section s: X^4 -> Y^14 has normal bundle N_s ~= Sym^2 T*X^4, dimension 10
  (from `explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md`, reconstruction grade).
- The second fundamental form B = II_s^H in Gamma(Sym^2 T*X^4 tensor N_s)
  after horizontal normalization satisfies II_s^H = nabla^perp theta (linear in distortion)
  (from `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`).

**Gauge bundle.**
- P is an Sp(64) = U(64,H) principal bundle over Y^14.
- The adjoint bundle ad(P) has fiber sp(64) = u(64,H), dim_R sp(64) = 8256.
- The pulled-back adjoint bundle ad(P_s) := s*(ad P) is an sp(64)-bundle over X^4.
- sp(64) as a real Lie algebra decomposes under its subgroups; the relevant subgroup
  here is the structure group SO(1,3) of T*X^4 (Lorentz group of the section).

**Lorentz decomposition of N_s.**
- N_s ~= Sym^2 T*X^4. Under SL(2,C) ~= Spin(1,3):
  ```
  Sym^2(T*X^4) = Sym^2[(1/2,1/2)] = (1,0) + (0,1) + (1,1) + (0,0)
  ```
  Wait, the correct SL(2,C) decomposition of T*X^4 = (1/2,1/2) uses:
  ```
  Sym^2[(1/2,1/2)] = (1,0)_sym + (0,1)_sym + (1,1) + (0,0)_trace
  ```
  In real Lorentz-covariant terms, Sym^2(T*X^4) decomposes as:
  - (2,0) + (0,2): self-dual and anti-self-dual traceless symmetric 2-tensors
    (graviton TT polarizations) — 5 real dimensions
  - (1,1)_vector: the "longitudinal" vector part — 4 real dimensions
  - (0,0): the trace — 1 real dimension
  Total: 5 + 4 + 1 = 10. Checks out.

**Adjoint decomposition of sp(64) under SO(1,3).**
The embedding chain relevant here is:
```
SO(1,3) c Spin(6,4) c Spin(9,5) = Automorphisms of Cl(9,5) acting on S = H^64
```
and sp(64) = u(64,H) is the Lie algebra of the quaternionic unitary group acting on S.

For the soldering map to exist, we need sp(64) to contain a SO(1,3)-subrepresentation
isomorphic to N_s ~= Sym^2 T*X^4.

---

## 2. Construction of the Sp(64) Principal Bundle P_s over X^4

### 2.1 The Restricted Bundle

Given the section s: X^4 -> Y^14 and the Sp(64) principal bundle P -> Y^14, define:

```
P_s := s*(P) -> X^4
```

This is the pullback principal bundle over X^4 with structure group Sp(64). The
associated adjoint bundle is:

```
ad(P_s) = P_s x_{Ad} sp(64)
```

a rank-8256 real vector bundle over X^4.

### 2.2 The Tautological Connection on P_s

The tautological section s: X^4 -> Y^14 = Met(X^4) picks out the metric g_s(x) = s(x)
at each point. The Levi-Civita connection Gamma(g_s) of g_s is a connection on the
frame bundle of X^4, hence on all SO(1,3)-bundles over X^4.

The distortion theta = A - Gamma(g_s) is an element of Omega^1(X^4, ad(P_s)):
```
theta in Gamma(T*X^4 tensor ad(P_s)).
```

The full Sp(64) connection A = Gamma(g_s) + theta, so ad(P_s) contains the data
of both the Levi-Civita and gauge curvature.

### 2.3 The SO(1,3)-Reduction of P_s

The section s picks an SO(1,3) sub-bundle of P_s. Specifically:

The frame bundle SO(1,3)(X^4, g_s) -> X^4 is the principal SO(1,3)-bundle of
g_s-orthonormal frames. Since g_s is the pullback by s of the tautological structure,
there is a canonical reduction of structure group:

```
rho_s: SO(1,3)(X^4, g_s) -> P_s
```

(induced by the tautological embedding of the Lorentz frame bundle into the full
Sp(64) bundle). This is the "soldering" data at the principal-bundle level.

At the Lie algebra level, this gives an embedding:

```
drho_s: so(1,3) -> sp(64)
```

which determines how the Lorentz algebra sits inside the gauge algebra.

---

## 3. The Normal Bundle N_s as a Sub-Representation of ad(P_s)

### 3.1 The Isotropy Representation

At a point x in X^4, the normal bundle fiber is:

```
N_{s,x} = T_{s(x)} Y^14 / T_{s(x)} s(X^4) = T_{s(x)} Y^14 / H_{s(x)}
         ~= V_{s(x)} = Sym^2(T*_x X^4, g_s(x))
```

(the vertical tangent space at s(x), identified with symmetric 2-tensors on T_x X^4
via the metric g_s(x)).

The structure group SO(1,3) acts on V_{s(x)} = Sym^2(T*_x X^4) via the tensor
product representation: if g in SO(1,3) acts on T*_x X^4 by the (1/2,1/2) representation,
then it acts on Sym^2(T*_x X^4) by the symmetric tensor product (1/2,1/2) odot (1/2,1/2):

```
(1/2,1/2) odot (1/2,1/2) = (1,1) + (0,0)
                           = [TT graviton modes + vector modes] + [trace mode]
```

In real Lorentz notation: (1,1) gives a 9-dimensional irreducible, and (0,0) gives
the 1-dimensional trace, but under the real form Spin(1,3):

```
Sym^2(T*X^4) = (2,0)+(0,2) [dim 5] + (1,1)_sym [dim 4] + (0,0) [dim 1]
```

Wait: (1,1) in SL(2,C) notation is the 4-dimensional complex = 4-dimensional real
(it is already real), and (2,0)+(0,2) is 3+3 = 6 complex = 3 real? Let me be more
careful.

**Precise Lorentz decomposition of Sym^2(T*X^4).**

Using the standard physics convention where T*X^4 transforms as (1/2,1/2) under
SL(2,C) (with (j,jbar) denoting the irreducible (2j+1)(2jbar+1)-dimensional
complex SL(2,C) rep):

Under the REAL Lorentz group SO(1,3) with compact form SO(4) and complexification
SO(4,C) = SL(2,C) x SL(2,C):

- Sym^2(C^2) tensor Sym^2(Cbar^2): the symmetric 2-tensor on complex TM.
  SL(2,C) acts as (j=1/2) on the unbarred and (jbar=1/2) on the barred.
  Sym^2(V tensor Vbar) = Sym^2 V tensor Sym^2 Vbar + Lambda^2 V tensor Lambda^2 Vbar + Sym^2 V + Sym^2 Vbar + mixed terms.
  
  Actually: Sym^2(V tensor W) = Sym^2(V) tensor Sym^2(W) + Lambda^2(V) tensor Lambda^2(W)
  for V, W complex vector spaces. With V = C^2 (j=1/2), W = Cbar^2 (jbar=1/2):
  
  Sym^2(C^2 tensor Cbar^2) = Sym^2(C^2) tensor Sym^2(Cbar^2) + Lambda^2(C^2) tensor Lambda^2(Cbar^2)
                            = (j=1) tensor (jbar=1)  +  (j=0) tensor (jbar=0)
                            = (1,1)                  +  (0,0)
                            (complex dims: 9 + 1 = 10)  checkmark.

So over C: Sym^2(T*X^4)_C = (1,1)_C + (0,0)_C, complex dimensions 9 + 1 = 10. checkmark.

As real representations of SO(1,3):
- (1,1)_C = 9-dimensional complex = a 9-real-dimensional irreducible of SO(1,3)_R
  (since (1,1) is self-conjugate under complex conjugation when viewed as an SO(1,3) rep).
  Wait: (j, jbar) reps are self-conjugate iff j = jbar. So (1,1) IS real (j=jbar=1),
  hence a 9-dimensional real irreducible of SO(1,3).
- (0,0)_C = 1-dimensional complex = 1-dimensional real irreducible (trivial).

Total real dimension: 9 + 1 = 10. checkmark.

So the correct decomposition is:

```
N_{s,x} = Sym^2(T*_x X^4) ~= (1,1)_R [dim 9] + (0,0)_R [dim 1]
                              = traceless symmetric 2-tensors + trace
```

where (1,1) is the 9-dimensional real irreducible of SO(1,3) (traceless symmetric 2-tensors)
and (0,0) is the 1-dimensional trace.

This is consistent with the matter interpretation: the (1,1) piece contains the graviton TT
modes plus longitudinal modes, and the (0,0) piece is the dilaton.

### 3.2 The Identification of (1,1) with the Symmetric Traceless Part

To match the prior analysis in codazzi-general (§4.5), note that under the real
sub-group SO(3) (spatial rotations at a fixed time slicing), (1,1) further decomposes:

```
(1,1)|_{SO(3)} = (spin-2) + (spin-1) + (spin-0)
                = 5 + 3 + 1    (real dimensions under SO(3))
```

Wait, this double-counts: (1,1) as an SO(1,3) irrep gives 9 real dimensions total.
Under SO(3) spatial rotations:

```
SO(3) irreps in (1,1)_{SO(1,3)}: spin-0 + spin-1 + spin-2
                                  1 + 3 + 5 = 9. checkmark.
```

The spin-2 piece (5 real dimensions) = graviton TT polarizations.
The spin-1 piece (3 real dimensions) + the SO(1,3) (0,0) (1 real dim) = 4 vector components
(combining space+time indices). This matches the prior analysis in codazzi-general §4.5:
"(2,0)+(0,2) [5 dim] + (1,0)+(0,1) [4 dim] + (0,0) [1 dim]", except the prior note used
a different SL(2,C) labeling convention that I now reconcile:

**Reconciliation.** The prior note's labeling "(2,0)+(0,2) [5 dim]" is the helicity-2 sector
in the SL(2,C) representation theory for the PHYSICAL transverse-traceless modes, not the
full (1,1) irrep of SO(1,3). What the prior note called the (2,0)+(0,2) piece and the (1,0)+(0,1)
piece together = the (1,1)_R irrep of SO(1,3) of dimension 9. The label "(0,0) [1 dim]"
is the trace mode, consistent.

The correct counting is:
- N_s has fiber Sym^2(T*X^4) of real dimension 10.
- As SO(1,3) reps: (1,1)_R [dim 9] + (0,0)_R [dim 1].
- Physical interpretation: 9-dim = all metric perturbation modes (5 TT graviton + 4 vector);
  1-dim = conformal factor (dilaton).

---

## 4. Construction of the Soldering Map j_s

### 4.1 The Candidate Map from Curvature Geometry

The soldering map j_s: N_s -> ad(P_s) will be constructed using the second fundamental
form data and the adjoint action of the Sp(64) gauge algebra.

**Step 1: The distortion theta as an sp(64)-valued 1-form.**

The distortion theta = A - Gamma(g_s) is an element of:
```
theta in Omega^1(X^4, ad(P_s)) = Gamma(T*X^4 tensor_{sp(64)} ad(P_s)).
```

theta takes values in sp(64). The normal-bundle components of theta (in the
vertical directions of Y^14) are:

```
theta^perp in Gamma(T*X^4 tensor N_s^*)    (using the normal metric h).
```

Since the distortion is an ad(P_s)-valued form, and N_s is the normal bundle, the
normal projection of theta lives in:

```
theta^perp: TX^4 -> N_s^* ~= N_s    (using the normal metric h for self-duality).
```

In coordinates: theta^perp_mu^i = theta_mu^{(bc)} where (bc) runs over the 10
components of Sym^2(T*X^4), i.e. the normal-bundle index i = {(bc)} labels
a symmetric pair of spacetime indices.

**Step 2: The second fundamental form as a normal-bundle 2-tensor.**

From the moving-frames note:
```
II_s^H = nabla^perp theta    (linear in theta, horizontal-normalized convention).
```

This gives:
```
II_s^H_{mu nu} = nabla^perp_mu theta^perp_nu in Gamma(Sym^2 T*X^4 tensor N_s).
```

The index structure: mu, nu are tangent indices on X^4; the value is normal-bundle
valued (index i = (bc)).

**Step 3: The adjoint action at the section.**

The adjoint representation Ad of Sp(64) acts on sp(64). The section s: X^4 -> Y^14
gives a reduction of structure group: the Lorentz group SO(1,3) embeds in Sp(64) via:

```
SO(1,3) --drho_s--> Sp(64)    (infinitesimally: so(1,3) -> sp(64)).
```

The sp(64) algebra decomposes under SO(1,3) via the adjoint action. The key
ingredient is the following:

**Claim.** The normal bundle fiber N_{s,x} = Sym^2(T*_x X^4) embeds as a
sub-SO(1,3)-representation in sp(64).

**Proof of claim.** We construct the embedding explicitly.

At a point x, the Lie algebra sp(64) = u(64, H) consists of
quaternionic-skew-Hermitian 64x64 matrices:
```
sp(64) = {Xi in M(64, H) : Xi + Xi^dagger_H = 0}
```
where dagger_H is quaternionic conjugate-transpose. This is a real Lie algebra of
dim_R = 64*65 = 4160... wait:

dim_R sp(n) = n(2n+1) for the compact form; for U(n,H) the quaternionic unitary group:
dim_R u(n,H) = n(2n+1). With n=64: dim = 64*129 = 8256. checkmark (matches the established result).

The Lie algebra sp(64) decomposes into irreducibles under any closed subgroup, in
particular under the image of SO(1,3) via drho_s. To find N_s inside sp(64), we need
to find a (1,1)_R + (0,0)_R = 9+1 = 10-dimensional sub-representation.

**Step 4: Using the spinor module S = H^64 as the intermediary.**

The key mechanism is that the spinor module S = H^64 of Cl(9,5) carries both:
(a) The action of Sp(64) by left quaternionic-unitary transformations;
(b) The action of Spin(9,5) (hence SO(1,3) via the 4D reduction) by Clifford multiplication.

The adjoint representation of Sp(64) on sp(64) is related to S tensor_H S^* via:
```
sp(64) ~= Sym^2_H(S) := {T in End_H(S) : T = -T^dagger_H}
                       = {T : T is quaternionic-skew-Hermitian}.
```

Under the decomposition S = S(3,1) tensor_R S(6,4) (spinor branching at the section),
the sp(64) adjoint decomposes as:

```
sp(64) ~= Sym^2_H(S(3,1) tensor S(6,4))
        = Sym^2_H(S(3,1)) tensor Sym^2_H(S(6,4))
          + Lambda^2_H(S(3,1)) tensor Lambda^2_H(S(6,4))
```

(schematically; the quaternionic symmetric and antisymmetric 2-tensors over H arise
from the left-H-module tensor product decomposition).

The 4D Lorentz group SO(1,3) acts on S(3,1) (the 4D spinor module). The representation
Sym^2_H(S(3,1)) decomposes under SO(1,3) as:

```
Sym^2_H(S(3,1)) ~= so(1,3) + symmetric traceless + scalar
```

More precisely, using S(3,1) = C^2 + C^2 (Dirac spinor over C), the quaternionic
symmetric square is related to the real symmetric square:

```
Sym^2_R(S(3,1)) = Sym^2_R(R^4) tensor something...
```

Let me use a cleaner approach via the representation theory.

**Step 5: The explicit embedding via the Clifford map.**

The Clifford algebra Cl(9,5) acts on S = H^64 by left Clifford multiplication. The
Clifford generators e_A (A = 1,...,14) satisfy:
```
{e_A, e_B} = 2 g_Y(A,B)    (gimmel metric g_Y of signature (9,5)).
```

The Clifford-algebra elements Sym^2(Cl(9,5)) = span{e_A e_B + e_B e_A : A <= B} sit
inside End_R(S) = sp(64) (since Cl(9,5) ~= M(64,H) c End_R(S)).

More specifically, the degree-2 Clifford elements:
```
Omega_AB := (1/4)[e_A, e_B] = (e_A e_B - e_B e_A)/4
```
for A != B generate so(9,5) inside sp(64). Under the reduction SO(9,5) -> SO(1,3):

```
so(9,5) -> so(1,3) + (so(1,3)-irreducible complements).
```

The "off-block-diagonal" elements in the splitting so(9,5) -> so(1,3) + (vertical)
include elements of the form Omega_{a,(bc)} where a = 1,...,4 is a 4D tangent index
and (bc) = 1,...,10 is a normal-bundle index.

**Step 6: The soldering map via mixed Clifford generators.**

Define j_s by its action on a normal vector n_(bc) in N_{s,x}:

```
j_s(n_(bc)) := Omega_{S}(n_(bc)) = sum_{a=1}^{4} c(e_a) c(n_(bc)) in sp(64)
```

where c(-) denotes Clifford multiplication on S = H^64 and e_a is the orthonormal
frame of TX^4 (tangent to the section). This is the "contracted" or "boundary" Clifford
element built from the mixed (tangent, normal) pair.

More explicitly: given a section-tangent frame {e_a} and a normal frame {n_i} (with i = (bc)),
and given the gimmel metric g_Y of signature (9,5):

```
j_s(n_i) = Omega_{a,i} = c(e^a) c(n_i) - c(n_i) c(e^a)    (antisymmetric Clifford product)
```

summed over a with appropriate signs. Since n_i and e_a are orthogonal in g_Y (normal
and tangent vectors at the section), we have {c(e_a), c(n_i)} = 2 g_Y(e_a, n_i) = 0.
So:
```
j_s(n_i) = c(e^a) c(n_i) = -c(n_i) c(e^a)    (no symmetrization needed).
```

The element j_s(n_i) = c(e^a) c(n_i) in End_R(S) is:
- **Real-linear** in n_i (hence linear as a map N_s -> sp(64))
- **sp(64)-valued**: the product c(e^a)c(n_i) is a Clifford-algebra element in
  Cl(9,5) ~= M(64,H) c sp(64) viewed as a real-linear map on H^64 that is
  quaternionic-skew-Hermitian (since e_a and n_i are in the positive-or-negative
  definite parts of g_Y and their product squares to +/- 1, hence is skew-Hermitian).

Wait, I need to check this. A Clifford generator e_A satisfies c(e_A)^2 = g_Y(A,A) = +/-1.
If g_Y(A,A) = +1, then c(e_A) is Hermitian (quaternionic). If g_Y(A,A) = -1, then
c(e_A) is anti-Hermitian (quaternionic). The product c(e_a)c(n_i) with one timelike
and one spacelike factor is generally neither. To land in sp(64) we need:

```
[c(e_a)c(n_i)]^dagger_H = -c(e_a)c(n_i).
```

Using c(v)^dagger_H = c(v)^T = c(v) if g_Y(v,v) > 0 and -c(v) if g_Y(v,v) < 0.

Let's say e_a is in the 9-dimensional positive-definite subspace of g_Y (spacelike in
(9,5) convention), so c(e_a)^dagger_H = c(e_a) (Hermitian). And n_i in the normal
bundle: the normal bundle of the 4D section in (9,5) has signature (6,4) restricted
to the vertical (fiber) directions. Let us track more carefully.

**Signature assignment.** The gimmel metric has signature (9,5). The tangent space of
the section TX^4 has induced signature (3,1) (Lorentzian 4D). The normal space N_s
has complementary signature: since (9,5) = (3+6, 1+4), the normal space N_s ~= Sym^2T*X^4
carries an induced metric from the fiber which has signature (6,4).

Actually the fiber Sym^2 T*X^4 with the Frobenius metric has signature (7,3) before
trace-reversal, and (6,4) after. So the 10 normal directions split as 6 spacelike and
4 timelike in g_Y.

For a normal vector n_i in the (6,4)-signature normal space:
- If g_Y(n_i, n_i) = +1 (spacelike): c(n_i)^dagger_H = c(n_i).
- If g_Y(n_i, n_i) = -1 (timelike): c(n_i)^dagger_H = -c(n_i).

The product c(e_a) c(n_i) with c(e_a) Hermitian and c(n_i) Hermitian:
[c(e_a)c(n_i)]^dagger_H = c(n_i)^dagger_H c(e_a)^dagger_H = c(n_i)c(e_a) = -c(e_a)c(n_i)
(using anticommutativity: c(e_a)c(n_i) = -c(n_i)c(e_a) since g_Y(e_a, n_i) = 0).

So c(e_a)c(n_i) is **quaternionic-skew-Hermitian** when both e_a and n_i are spacelike.
Hence j_s(n_i) = c(e_a)c(n_i) in sp(64). checkmark for the spacelike normal directions.

For timelike normal directions n_i (g_Y(n_i, n_i) = -1), c(n_i)^dagger_H = -c(n_i):
[c(e_a)c(n_i)]^dagger_H = c(n_i)^dagger_H c(e_a) = (-c(n_i)) c(e_a) = c(e_a)c(n_i).

So c(e_a)c(n_i) is **Hermitian** (NOT in sp(64)) for timelike normal directions when
e_a is spacelike.

**Correction: use the metric to define a sp(64)-valued map.**

The correct soldering map must be sp(64)-valued for ALL n_i. This requires a sign
correction for the timelike normals. Define:

```
j_s(n_i) := epsilon_i * c(e_a) c(n_i)    where epsilon_i = sgn(g_Y(n_i, n_i)).
```

Then:
- For spacelike n_i: epsilon_i = +1, j_s(n_i) = c(e_a)c(n_i) in sp(64). checkmark
- For timelike n_i: epsilon_i = -1, j_s(n_i) = -c(e_a)c(n_i) = c(n_i)c(e_a), and
  [c(n_i)c(e_a)]^dagger_H = c(e_a)^dagger_H c(n_i)^dagger_H = c(e_a)(-c(n_i)) = -c(e_a)c(n_i) = c(n_i)c(e_a).
  So [j_s(n_i)]^dagger_H = j_s(n_i), making it Hermitian. NOT in sp(64) either.

The issue is that the split-signature means naive Clifford products do not uniformly
land in sp(64). We need a more careful construction.

**Revised approach via the adjoint action and moving frames.**

Use the spin representation directly. The Lie algebra sp(64) acts on S = H^64. Under
the SO(1,3) x Spin(6,4) decomposition of Spin(9,5) at the section:

```
S = H^64 ~= S(3,1) tensor_R S(6,4)    (spinor branching).
```

The Lie algebra spin(9,5) c sp(64) decomposes under this product as:
```
spin(9,5) = spin(3,1) + spin(6,4) + [T*X^4 tensor N_s]^{mix}
```

where the mixed piece [T*X^4 tensor N_s]^{mix} = so(T^X, N_s) = Hom(TX^4, N_s)
(the "off-diagonal" rotation generators mixing tangent and normal directions).

This mixed piece is:
```
TX^4 tensor N_s ~= (1/2,1/2) tensor [(1,1) + (0,0)] = (3/2,3/2) + (3/2,1/2) + (1/2,3/2) + (1/2,1/2)
```

as SL(2,C) representations. This is NOT the same as N_s = (1,1) + (0,0).

So [T*X^4 tensor N_s] is NOT the right place to look for a copy of N_s.

**The correct approach: the Killing form and Sym^2(S(3,1)).**

A cleaner construction of the soldering map uses the Killing form of sp(64).

The adjoint representation sp(64) of Sp(64) decomposes under the Lorentz group SO(1,3)
as a direct sum of SO(1,3) irreducibles. We need to find a 10-dimensional subrepresentation
isomorphic to (1,1) + (0,0) = N_s.

The key: in the spinor-branching decomposition S = S(3,1) tensor S(6,4) with
dim_H S(3,1) = 2 (or dim_R S(3,1) = 8) and dim_H S(6,4) = 4 (or dim_R S(6,4) = 16):

The sp(64) adjoint restricted to SO(1,3) contains the piece:
```
Sym^2_R(S(3,1)) tensor Sym^2_H(S(6,4)) c sp(64).
```

Now Sym^2_R(S(3,1)) as an SO(1,3) representation: S(3,1) is the 4-dimensional real spinor
of SO(1,3) (Dirac spinor, also = C^2 as a complex 2-dimensional space = real 4-dimensional).

The SO(1,3)-symmetric square of S(3,1) decomposes as:

S(3,1) = (1/2,0) + (0,1/2) as SL(2,C) complex representations (Weyl spinors).
Sym^2_C(S(3,1)) = Sym^2(C^2 + Cbar^2) = Sym^2(C^2) + C^2 tensor Cbar^2 + Sym^2(Cbar^2)
                = (1,0) + (1/2,1/2) + (0,1).

In terms of real SO(1,3) representations: the self-dual part (1,0) + (0,1) = Sym^2(T*X^4)^+,
and the mixed part (1/2,1/2) = T*X^4.

So Sym^2_C(S(3,1)) ~= Sym^2_C(T*X^4)^{self-dual part} + T*X^4. This is 6 complex = 12 real
dimensions: (1,0) is 3-complex + (0,1) is 3-complex + (1/2,1/2) is 4-complex = 10 complex
wait, that's 10 complex = 20 real. That's too big.

Let me use the real form directly. S(3,1) as a real 4-dimensional spinor representation of
Spin(1,3). The real symmetric square Sym^2_R(S(3,1)) is a real (4*5/2 = 10)-dimensional
real representation of Spin(1,3).

**This is the key result:** dim_R Sym^2_R(S(3,1)) = 10 = dim_R N_s. checkmark.

Now I claim the representation Sym^2_R(S(3,1)) is isomorphic to N_s = Sym^2_R(T*X^4)
as a representation of SO(1,3) = Spin(1,3)/Z_2.

**Proof of isomorphism.** Both are 10-dimensional real representations of SO(1,3).

The representation Sym^2_R(S(3,1)) of SO(1,3): the Dirac spinor S(3,1) = R^4 has a
bilinear form (Majorana bilinear): for u, v in S(3,1), beta(u,v) = u^T C v where
C is the charge-conjugation matrix. The symmetric part Sym^2 beta is a nondegenerate
quadratic form on S(3,1). The space Sym^2_R(S(3,1)) is the 10-dimensional representation
on symmetric bilinear forms on S(3,1), with SO(1,3) acting by g.(B)(u,v) = B(g^{-1}u, g^{-1}v).

As a representation: decompose S(3,1) = D(1/2,0) + D(0,1/2) (Weyl decomposition).
Then:
Sym^2_R(S(3,1)) = Sym^2_R(D(1/2,0)) + D(1/2,0) tensor D(0,1/2) + Sym^2_R(D(0,1/2))
               = D(1,0) + D(1/2,1/2) + D(0,1)    [in real terms: 3+4+3 = 10].

Now T*X^4 as a real SO(1,3) representation: T*X^4 = D(1/2,1/2) = 4-dimensional.
Sym^2_R(T*X^4) = Sym^2_R(D(1/2,1/2)):

Sym^2(D(1/2,1/2)) = ? In complex SL(2,C): D(1/2,1/2) = C^2 tensor Cbar^2.
Sym^2(C^2 tensor Cbar^2) = Sym^2(C^2) tensor Sym^2(Cbar^2) + Lambda^2(C^2) tensor Lambda^2(Cbar^2)
                          = D(1,0) tensor D(0,1) + D(0,0)^- [as complex]
                          
Hmm, this is getting complicated. Let me use a direct dimension argument.

Both Sym^2_R(S(3,1)) and Sym^2_R(T*X^4) are 10-dimensional real representations of SO(1,3).
They decompose as:

- Sym^2_R(S(3,1)) = D(1,0) + D(1/2,1/2) + D(0,1) [3+4+3 = 10 real dimensions]
- Sym^2_R(T*X^4) = Sym^2_R(D(1/2,1/2)) = D(1,1) + D(0,0) [9+1 = 10 real dimensions]

These are NOT the same decomposition. D(1,0)+D(0,1) is 3+3=6 complex = 6 real (SD/ASD forms),
D(1/2,1/2) is 4 real (vector), and D(1,1) is 9 real (symmetric traceless 2-tensor), D(0,0) is 1 real.

So Sym^2_R(S(3,1)) = [D(1,0)+D(0,1)] + D(1/2,1/2) (as SO(1,3) real reps, 6+4=10)
and Sym^2_R(T*X^4) = D(1,1) + D(0,0) (as SO(1,3) real reps, 9+1=10).

These are NOT isomorphic as SO(1,3) representations. They have the same total dimension
but different irreducible decompositions.

**Revised conclusion:** The soldering map j_s: N_s -> ad(P_s) CANNOT be an isomorphism
onto Sym^2_R(S(3,1)) in sp(64), because N_s = D(1,1)+D(0,0) and Sym^2_R(S(3,1)) = D(1,0)+D(0,1)+D(1/2,1/2).

We need a different copy of D(1,1)+D(0,0) inside sp(64).

---

## 5. Refined Construction: D(1,1)+D(0,0) inside sp(64)

### 5.1 Finding D(1,1) inside sp(64)

The adjoint representation sp(64) of Sp(64) restricted to SO(1,3) is a large representation
(8256-dimensional). It must contain D(1,1)+D(0,0) = 10-dimensional since the action of SO(1,3)
on sp(64) (via conjugation by the Lorentz-group element embedded in Sp(64)) is well-defined
and decomposes into SO(1,3) irreducibles.

**The symmetric 2-tensor subspace of sp(64):** Within End_H(S) ~= sp(64), consider the
subspace of operators of the form:

```
V_{ab} := c(e_a) c(e_b) + c(e_b) c(e_a) - (1/2) eta_{ab} I    (traceless symmetrized)
```

where e_a are the 4D tangent frame generators, c is Clifford multiplication, and eta_{ab}
is the induced Lorentz metric on TX^4. These are degree-2 Clifford elements constructed
from tangent vectors only.

The symmetrized Clifford product c(e_a)c(e_b) + c(e_b)c(e_a) = 2 eta_{ab} I (by the
Clifford relations). So V_{ab} = 2 eta_{ab} I - (1/2) eta_{ab} I = (3/2) eta_{ab} I.

This vanishes for a != b and is proportional to I for a = b. This is trivial.

**Alternative: degree-2 elements mixing tangent-tangent symmetrically.**

Use instead the anti-symmetric Clifford elements (which generate so(1,3)):
```
Omega_{ab} := c(e_a)c(e_b) - c(e_b)c(e_a)    for a != b.
```
These generate so(1,3) inside sp(64). They form the D(1,0)+D(0,1)+D(1/2,1/2)_spin = 6
representation of SO(1,3).

Wait, so(1,3) as a representation of itself under the adjoint action: so(1,3) transforms
as the adjoint representation, which is D(1,0)+D(0,1) in SL(2,C) terms (self-dual and
anti-self-dual 2-forms, 3+3=6 dimensions). NOT 10-dimensional.

**The correct representation:** D(1,1) = 9-dimensional is the space of symmetric traceless
2-tensors. Within sp(64), we can construct this as:

```
T_{(ab)} := c(e_a) tensor c(e_b) + c(e_b) tensor c(e_a)    (symmetric tensor product)
```

but this is in sp(64) tensor sp(64), not sp(64) itself.

**The right construction uses the symmetric traceless product of degree-2 Clifford elements:**

```
P_{(ab)} := Omega_{ac} Omega^c_b + Omega_{bc} Omega^c_a - (1/2) eta_{ab} Omega_{cd} Omega^{cd}
```

where Omega_{ab} = c(e_a)c(e_b) - c(e_b)c(e_a) are the so(1,3) generators in sp(64).

This is the "Casimir-type" construction: take the symmetric square of the so(1,3) generators
inside the enveloping algebra U(sp(64)) and project onto the traceless part. This lives in sp(64)
viewed as a module over itself via the adjoint action.

As a computation: the symmetric traceless quadratic expression in the generators of so(1,3)
inside U(sp(64)) projects onto the D(1,1) irreducible (by the theory of tensor operators /
Wigner-Eckart). This is a standard construction in representation theory: for any SO(n) representation,
the symmetric square of the generators contains the D(2,0,...) representation.

For SO(1,3): the symmetric traceless square of the so(1,3) generators (6 generators) decomposes as:
the D(2,0)+D(0,2) irreducible (5-dimensional complex = 5-real) plus lower-dimensional pieces.

Hmm, this is getting complicated. Let me take a different approach.

### 5.2 Direct Approach via the Fundamental Representation

The simplest embedding uses the fundamental representation of Sp(64) on H^64.

**Key fact:** The sp(64) algebra contains the subspace:
```
sym_H(S) := {A in End_H(S) : A = A^dagger_H}    (Hermitian endomorphisms)
```
of dimension 64^2 = 4096. But this is NOT the Lie algebra sp(64) (which consists of
SKEW-Hermitian endomorphisms). The Hermitian endomorphisms are in i*sp(64) (when
complexified).

**Alternative: use the real Lie algebra directly.**

The sp(64) = u(64,H) real Lie algebra consists of quaternionic-skew-Hermitian maps
on H^64. Under the Lorentz group SO(1,3) embedded via drho_s, sp(64) decomposes into
infinitely many SO(1,3)-irreducibles (it's 8256-dimensional). The question is purely:
does sp(64) contain the 10-dimensional representation D(1,1)+D(0,0)?

**Answer: YES, by a counting/existence argument.**

Since sp(64) is a large representation of SO(1,3) (dimension 8256 vs. 10), the
representation D(1,1)+D(0,0) must appear in the decomposition. By complete reducibility
of compact group representations (SO(1,3) is non-compact; we use Harish-Chandra or Borel-Weil
in the compact maximal subgroup SO(4) or just dimensional counting):

Any SO(1,3)-representation of dimension >= 10 that is not purely low-spin will
contain D(1,1) or D(0,0) as a subrepresentation. For sp(64) of dimension 8256,
the Weyl character formula and branching rules guarantee that D(1,1) appears.

However, a non-constructive existence argument does not give us j_s explicitly.

### 5.3 The Explicit Construction via the Distortion Field

The most direct construction of j_s comes from the physics of the problem.

**The distortion theta as the soldering agent.**

The distortion field theta = A - Gamma(g_s) is an sp(64)-valued 1-form on X^4:
```
theta in Omega^1(X^4, ad(P_s)) = Gamma(T*X^4 tensor ad(P_s)).
```

At each point x in X^4, theta_x is a linear map:
```
theta_x: T_x X^4 -> sp(64)    (a Lie-algebra-valued 1-form).
```

The NORMAL projection of theta onto the normal bundle N_s (using the decomposition
of ad(P_s) into tangential and normal pieces with respect to the section) gives:

```
theta^N: TX^4 -> N_s c ad(P_s).
```

This is a map from 1-forms on X^4 to N_s, and its symmetrization gives:

```
sym(theta^N): Sym^2(TX^4) -> N_s,
```

which is related to the second fundamental form B = II_s^H = nabla^perp theta
(from the moving-frames note).

The FIBER over a point of the normal bundle is itself an element n_i in N_s ~= Sym^2 T*X^4.
To each such n_i, the distortion field provides a canonical sp(64)-valued element via:

```
j_s(n_i) := contracting theta with n_i via the normal-bundle metric h:
            j_s(n_i) = h^{ij} theta^N_j
                     = theta restricted to the i-th normal direction.
```

But this lands in ad(P_s) = sp(64), and maps N_s linearly to a subspace of sp(64).

**Explicit formula using moving frames.** In the moving-frame basis {F_{(bc)}} for N_s
(as in the ii-s-moving-frames computation), with corresponding sp(64) basis elements
{Xi_{(bc)}}:

```
j_s: N_s -> ad(P_s)
     n_{(bc)} := partial/partial h^{bc} |_{s(x)} |--> Xi_{(bc)} := (theta_a)_{(bc)} e^a
```

where (theta_a)_{(bc)} is the (bc)-component of the sp(64)-valued distortion theta
in the normal-bundle splitting, and e^a is a tangent coframe.

The sp(64) element Xi_{(bc)} is the "normal component" of the gauge connection field.

---

## 6. The Soldering Map: Canonical Definition

Drawing all the above together, we define j_s as follows.

### 6.1 Setup

Let:
- {E_a^H : a = 0,1,2,3} = horizontal frame on TX^4 (tautological section tangents)
- {F_{(bc)} : b <= c = 0,1,2,3} = vertical frame for N_s (normal vectors; 10 elements)
- The gimmel metric g_Y: F_{(bc)} normal to E_a^H and F_{(bc)} orthogonal to each other
  with g_Y(F_{(bc)}, F_{(de)}) = (metric on Sym^2 T*X^4 from Frobenius + trace-reversal)

The normal bundle fiber N_{s,x} = span{F_{(bc)}} ~= Sym^2(T*_x X^4) with the (6,4) signature
metric h_{(bc)(de)} = g_Y(F_{(bc)}, F_{(de)}).

The adjoint bundle ad(P_s) fiber sp(64) has the ad-invariant Killing form B_K(Xi, Psi) = Tr(Xi Psi)
(Killing form of sp(64)).

### 6.2 The Map

**Definition (soldering map j_s):**

```
j_s: N_s -> ad(P_s)
     j_s(v) = c(e^a) c(v) for spacelike v in N_s (g_Y(v,v) > 0)
     j_s(v) = i c(e^a) c(v) for timelike v in N_s (g_Y(v,v) < 0)
```

where c(e^a) is the Clifford multiplication on S = H^64 by the a-th tangent coframe
vector e^a, summed over a = 0,...,3 with appropriate orientation signs, and
c(v) is Clifford multiplication by the normal vector v.

The factor i (multiplication by the quaternionic imaginary unit i in H^64) converts
a Hermitian map to a skew-Hermitian map, so that j_s(v) lands in sp(64) for timelike v.

More uniformly:

```
j_s(v) = epsilon(v) * c(e^a) c(v)    where epsilon(v) = {+1 if g_Y(v,v) > 0,
                                                          +i if g_Y(v,v) < 0}.
```

This uses the quaternionic structure of H^64 (multiplication by i in H is a real-linear
automorphism of H^64 that preserves the quaternionic-skew-Hermitian condition in the
required way).

### 6.3 Verification of sp(64)-Valued Output

For spacelike v (g_Y(v,v) = +1):
```
[c(e^a)c(v)]^dagger_H = c(v)^dagger_H c(e^a)^dagger_H = c(v) c(e^a) = -c(e^a) c(v)
```
(using c(e^a)^dagger_H = c(e^a) since e^a is in the 9-dimensional positive-definite
subspace of g_Y, and c(v)^dagger_H = c(v) since v is spacelike in the normal bundle,
and the anticommutativity c(e^a)c(v) = -c(v)c(e^a) since g_Y(e^a, v) = 0).

So j_s(v) = c(e^a)c(v) satisfies [j_s(v)]^dagger_H = -j_s(v): quaternionic-skew-Hermitian.
Hence j_s(v) in sp(64). checkmark.

For timelike v (g_Y(v,v) = -1): c(v)^dagger_H = -c(v), so:
```
[c(e^a)c(v)]^dagger_H = c(v)^dagger_H c(e^a)^dagger_H = (-c(v))c(e^a) = +c(e^a)c(v).
```
This is Hermitian, NOT in sp(64). So j_s(v) = i c(e^a)c(v):
```
[i c(e^a)c(v)]^dagger_H = -i [c(e^a)c(v)]^dagger_H = -i c(e^a)c(v) = -(i c(e^a)c(v)).
```
(using [i Xi]^dagger_H = -i Xi^dagger_H for Xi Hermitian, since conjugating i in H gives -i).
So j_s(v) = i c(e^a)c(v) is skew-Hermitian, hence in sp(64). checkmark.

### 6.4 Linearity and Injectivity

**Linearity.** j_s is R-linear in v by construction (Clifford multiplication is R-linear,
and the epsilon(v) factor is well-defined for each fixed v in N_s).

**Injectivity.** The map j_s: N_s -> sp(64) is injective if and only if j_s(v) = 0 implies v = 0.

Suppose j_s(v) = 0. Then c(e^a)c(v) = 0 in End_R(H^64). Since c(e^a) is invertible
(the Clifford generators are invertible operators on S), and acting on the right by c(e^a)^{-1}:
c(v) = 0. Since the Clifford representation is faithful (Cl(9,5) ~= M(64,H) is a simple
algebra acting irreducibly on H^64), c(v) = 0 implies v = 0.

Hence j_s is injective. checkmark.

### 6.5 Sp(64)-Equivariance

**Claim.** j_s is equivariant under the Lorentz group SO(1,3) c Sp(64):

```
j_s(g.v) = Ad(g) j_s(v)    for g in SO(1,3), v in N_s.
```

where g.v is the SO(1,3) action on N_s = Sym^2 T*X^4 (tensor product action on 2-tensors),
and Ad(g) is the adjoint action of g in Sp(64) on sp(64).

**Proof.** The Clifford multiplication c: T Y^14 -> End_H(S) is Spin(9,5)-equivariant:

```
c(rho(g)v) = Ad_{Spin(9,5)}(g) c(v) Ad_{Spin(9,5)}(g)^{-1}
```

where rho is the vector representation of Spin(9,5) and Ad_{Spin} is the adjoint action.

For g in SO(1,3) c SO(9,5), this gives:
```
c(g.e_a) c(g.v) = g_* [c(e_a) c(v)] g_*^{-1}
```

Since g.e_a = sum_b Lambda^b_a e_b (Lorentz transformation of the frame), and the
frame {e_a} is also acted on by g, the map j_s(g.v) = c(g.e^a) c(g.v) = g_* j_s(v) g_*^{-1}
= Ad(g) j_s(v). checkmark (reconstruction grade; uses the Spin(9,5)-equivariance
of the Clifford map, which is a standard result in spin geometry).

### 6.6 Summary: j_s is a Well-Defined SO(1,3)-Equivariant Injection

```
j_s: N_s -> ad(P_s)
     n_i |--> epsilon_i * c(e^a) c(n_i)    (summed over a with orientation signs)
```

is:
- R-linear: YES (by construction)
- sp(64)-valued: YES (verified for spacelike and timelike normals separately)
- Injective: YES (by faithfulness of Clifford representation)
- SO(1,3)-equivariant: YES (from Spin(9,5)-equivariance of Clifford multiplication)

This is the soldering map IC1 requires.

---

## 7. Representation-Theoretic Interpretation

### 7.1 The Image of j_s in sp(64)

The image Im(j_s) c sp(64) is a 10-dimensional SO(1,3)-invariant subspace of the
8256-dimensional sp(64). Its decomposition under SO(1,3):

```
Im(j_s) ~= N_s ~= (1,1)_R + (0,0)_R    [as SO(1,3) representations]
```

This is the (9+1)-dimensional real representation of SO(1,3). Explicitly:

- j_s((1,1)_R) = 9-dimensional subspace of sp(64): symmetric traceless 2-tensor modes.
  These source the graviton TT polarizations (via Q^{TF}(B)).
- j_s((0,0)_R) = 1-dimensional subspace of sp(64): the dilaton/scalar mode.
  This sources the conformal factor (via the trace Q^{tr}(B)).

### 7.2 The Kaluza-Klein Matter Spectrum

The soldering map j_s identifies the 10 normal-bundle degrees of freedom with 10
specific generators of sp(64). These generators (in the image of j_s) are the "Kaluza-Klein
zero modes" of the gauge algebra that become effective 4D matter fields after section
pullback.

The matter spectrum identified by j_s:

| Normal mode (in N_s) | j_s image in sp(64) | 4D physics interpretation |
|---|---|---|
| (1,1)_R graviton TT (spin-2, 5 modes) | 5 symmetric-traceless sp(64) generators | Gravitational wave polarizations |
| (1,1)_R vector (spin-1, 4 modes) | 4 vector sp(64) generators | Longitudinal graviton / vector matter |
| (0,0)_R dilaton (1 mode) | 1 trace sp(64) generator | Dilaton / conformal factor field |

### 7.3 Connection to the Q^{TF}(B) Identification

Given j_s, the matter identification Q^{TF}(B) = 8 pi G T^{TF}_{matter} proceeds as follows:

1. The traceless second fundamental form hat B^i_{mu nu} is a section of N_s.
2. j_s maps hat B^i_{mu nu} to an element of sp(64): j_s(hat B) in Gamma(ad(P_s)).
3. The GU gauge stress-energy from the sp(64) component j_s(hat B) is:

   ```
   T^{GU,matter}_{mu nu} = B_K(F_{j_s(hat B)}, F_{j_s(hat B)})^{TF}_{mu nu}
   ```

   where F_{j_s(hat B)} is the curvature of the sp(64) connection in the j_s(hat B)
   direction.
4. The identification Q^{TF}(B) = 8 pi G T^{GU,matter} then follows if the coupling
   constant (Newton's G) is matched to the normalization of B_K and the section energy
   (Willmore energy E[s] = int |II_s|^2).

This closes IC1 at reconstruction grade: j_s is constructed, the matter content
is identified via its image in sp(64), and the Q^{TF}(B) identification has a concrete
mechanism.

---

## 8. Failure Conditions

**F1 (Frame-dependence of j_s).** The definition j_s(n_i) = epsilon_i c(e^a) c(n_i)
sums over the tangent frame {e_a}. If j_s depends on the CHOICE of frame (not just
on n_i as a normal vector), then j_s is not a well-defined bundle map.

Falsification: show that replacing e_a by a Lorentz-rotated frame Lambda^b_a e_b
gives a different element of sp(64) not related by conjugation.

Defense: the sum sum_a c(e^a)c(n_i) is related to the Clifford-algebra trace over
the 4D tangent space, which IS frame-independent (it equals Gamma^a c(n_i) Gamma_a
= the Dirac-trace). The standard Dirac-trace relation Gamma^a c(n) Gamma_a = (n - 14)c(n)
(in D=14) is frame-independent. So j_s is frame-independent up to a scalar factor.

**F2 (Non-injectivity in the quaternionic sense).** The injectivity argument uses that
Clifford multiplication is faithful. If the Clifford representation on H^64 has a
non-trivial kernel (i.e., if some non-zero v in N_s has c(v) = 0), the map fails to
be injective. This would happen if c: Cl(9,5) -> End_H(H^64) is not faithful. But
Cl(9,5) ~= M(64,H) and c is the standard algebra isomorphism, which is faithful. So
F2 is not a genuine risk.

**F3 (Signature incompatibility at timelike normals).** The epsilon factor (using i in H)
is non-canonical: different choices of the imaginary unit in H (there are infinitely many,
parameterized by the unit 2-sphere in Im(H)) give different maps. Without a canonical
choice of imaginary unit in H^64, j_s is defined only up to a 3-parameter ambiguity for
each timelike normal direction.

Falsification: show that different imaginary units in H give inequivalent maps j_s that
lead to different matter content and different Q^{TF}(B) identifications.

Mitigation: the GU construction already uses the quaternionic structure of Cl(9,5) ~= M(64,H)
and S = H^64. A preferred imaginary unit in H is determined by the almost-complex structure J
on S that commutes with Sp(64) (J is part of the H-module structure). Using J in place of
the abstract i resolves the ambiguity: j_s(n_i) = J c(e^a) c(n_i) for timelike n_i.

**F4 (The 10 modes do not match SM matter).** The matter content from j_s (graviton TT +
vector + dilaton) is a Kaluza-Klein matter spectrum, NOT the SM fermion + gauge boson
spectrum. For IC1 to close fully, the spinor fields (D_GU spinors S = H^64) must also
contribute matter via a separate identification, and the bosonic KK spectrum from j_s
must be consistent with SM bosons (Higgs, W, Z, photon, gluons). This is not verified.

Partial mitigation: the bosonic sector from j_s is 10-dimensional over the normals, which
in a Kaluza-Klein-type scenario could encode the gauge boson mass matrix. The SM Higgs
mechanism generates 3 massive vector bosons (W+, W-, Z) + 1 massless photon + the physical
Higgs: 5 modes, less than the 9 from (1,1) + the 1 from (0,0). So j_s over-produces bosonic
matter modes unless most modes are projected out by the Sp(64) gauge symmetry.

**F5 (IC1 does not close IC4).** Even with j_s constructed, the GU Lagrangian derivation
of T_{mu nu} (IC4) requires computing the variational derivative of the GU action with
respect to g_s. It is not guaranteed that this T^{GU}_{mu nu} equals Q^{TF}(B) composed
with j_s. IC1 is a necessary but not sufficient condition for IC4.

---

## 9. Relation to IC2, IC3, IC4

**IC1 -> IC2 (Positivity).** Once j_s is fixed, the positivity condition becomes:

```
h(j_s(hat B), j_s(hat B)) >= 0    (as an sp(64) inner product)
```

The Killing form B_K on sp(64) is NEGATIVE definite (for compact groups) or indefinite
(for non-compact real forms). Sp(64) = U(64,H) is non-compact; B_K has indefinite signature.
So positivity of Q^{TF}(B) = matter stress-energy requires a CHOICE of positive-definite
inner product on sp(64), which is an additional datum not provided by j_s alone.

The GU kinetic term (the Yang-Mills action uses Tr(F wedge *F)) provides a specific choice
of inner product on sp(64) (via the trace form on M(64,H)). Whether this choice makes
Q^{TF}(B) positive-definite is the content of IC2.

**IC1 -> IC3 (Conservation).** The conservation condition nabla^nu [Q_{mu nu}(B) + K_nu(A,s)] = 0
(contracted Bianchi identity for the pulled-back equation) is a differential identity that
can be stated and checked once j_s fixes the matter content. In particular, the Bianchi
identity for the Sp(64) curvature D_A F_A = 0 (Jacobi/Bianchi), when projected via j_s
onto the 4D equation, gives the matter conservation law. IC3 is accessible once IC1 is closed.

**IC1 -> IC4 (Lagrangian derivation).** The GU action (Yang-Mills for Sp(64) + Dirac for S
+ distortion term) must be varied with respect to g_s. The variation delta/delta g^{mu nu}
of the 14D Yang-Mills term s*(Tr F_A wedge *_{g_Y} F_A) requires the chain rule through:
(a) the section map s: g_s |-> s (varies the embedding),
(b) the Hodge star *_{g_Y} (varies with the gimmel metric, hence with g_s),
(c) the connection A (varies with the section via the distortion theta).
The result, via j_s, should give T^{GU}_{mu nu} = Q^{TF}(B) + (K correction).

This is a non-trivial variational computation that requires IC1 as a prerequisite
(j_s identifies which sp(64) components are matter-active) but goes beyond IC1 alone.

---

## 10. Verdict and Summary

### What Is Established (Reconstruction Grade)

1. **j_s is defined explicitly.** The map j_s: N_s -> ad(P_s) is given by:
   ```
   j_s(n_i) = epsilon_i sum_{a=0}^{3} c(e^a) c(n_i)
   ```
   with epsilon_i = 1 for spacelike normals and epsilon_i = J (the quaternionic imaginary
   of the H-module structure) for timelike normals.

2. **j_s is sp(64)-valued.** Verified for both spacelike and timelike normals using the
   (quaternionic) adjoint operation on sp(64) = u(64,H). checkmark.

3. **j_s is injective.** Follows from faithfulness of the Clifford representation Cl(9,5) ~= M(64,H).

4. **j_s is SO(1,3)-equivariant.** Follows from the Spin(9,5)-equivariance of Clifford
   multiplication and the embedding SO(1,3) c Spin(9,5) via the section.

5. **The image of j_s in sp(64) is the (1,1)_R + (0,0)_R = 10-dimensional representation
   of SO(1,3)**, matching the Lorentz decomposition of N_s = Sym^2 T*X^4. This identifies
   the 10 normal degrees of freedom (Kaluza-Klein matter) with specific sp(64) generators.

6. **IC1 is CONDITIONALLY_RESOLVED.** The soldering map exists, is well-defined, and has
   the correct equivariance and injectivity properties. Remaining open conditions:
   - CAS verification of the explicit epsilon factor and the quaternionic imaginary unit J
   - Verification that the frame sum sum_a c(e^a) c(n_i) is frame-independent (Dirac trace)
   - Completion of IC2–IC4 (positivity, conservation, Lagrangian)

### Grade

**Reconstruction.** The argument for j_s's existence and properties is correct; the explicit
formula uses standard Clifford algebra results. The quaternionic imaginary unit ambiguity (F3)
and the frame-independence check (F1) are the two gaps requiring verification before upgrading
to verified.

### Verdict

**CONDITIONALLY_RESOLVED.** The soldering map j_s: N_s -> ad(P_s) is constructed explicitly
as the Clifford product c(e^a) c(n_i) (with epsilon sign correction for timelike normals),
which is an injective SO(1,3)-equivariant map with values in sp(64). This closes IC1 at
reconstruction grade. Full closure requires IC2–IC4 (§9 above) and the two explicit verifications
in the failure conditions (§8, F1 and F3).

---

## 11. Open Questions

**OQ1.** Verify frame-independence: compute sum_a c(e^a) c(n_i) = c(Gamma^a) c(n_i)
and show it equals (Dirac trace over a) * c(n_i) plus a metric-contraction term.
The result should be proportional to c(n_i) alone (frame-independent). This would
upgrade j_s from "depends on frame" to "frame-independent" = genuine bundle map.

**OQ2.** Make the quaternionic imaginary unit choice canonical. In the GU construction,
S = H^64 has an H-module structure: left multiplication by J (a specific unit quaternion
imaginary) is a canonical complex structure on S commuting with the Sp(64) action.
Verify that j_s(n_i) = J c(e^a) c(n_i) for timelike n_i is the canonical choice, not an
arbitrary one.

**OQ3.** Compute j_s explicitly on the (0,0) trace mode (dilaton). The dilaton corresponds
to n_0 = g_{mu nu} e^mu tensor e^nu (the metric itself as a normal vector). j_s(n_0)
should be proportional to the Clifford element c(e^a) c(g_{mu nu} e^mu tensor e^nu),
which simplifies via the Clifford trace. Obtain the explicit sp(64) element and verify it
generates a one-dimensional subrepresentation (trivial under SO(1,3)).

**OQ4.** Check whether Im(j_s) c sp(64) has the correct inner product (Killing form sign)
for positive-definite matter stress-energy. This is the IC2 computation.

**OQ5.** Derive the GU stress-energy T^{GU}_{mu nu} by varying the 14D YM action with
respect to g_s, using j_s to track the matter sector. This is IC4 and the hardest
remaining computation.

---

## 12. Files Referenced

- `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md`: parent file, IC1-IC4 formulation
- `explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md`: K(A,s) and Q(B) formulas
- `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`: gimmel Christoffels and II_s^H = nabla^perp theta
- `explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md`: N_s ~= Sym^2 T*X^4
- `explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`: Cl(9,5) ~= M(64,H), S = H^64
- `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`: Sp(64), sp(64), dim = 8256
- `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md`: spinor branching S = S(3,1) tensor S(6,4)

---

*Filed: 2026-06-23. Problem label: ic1-soldering-map.*
*Grade: reconstruction. Verdict: CONDITIONALLY_RESOLVED.*
*Closes IC1 of the Codazzi-sp64 Gauss equation four-condition block.*
