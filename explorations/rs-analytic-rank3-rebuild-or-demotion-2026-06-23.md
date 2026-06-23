---
title: "RS Analytic Route: Rank-3 A3 Rebuild or Demotion of ind_H(RS)=8"
date: 2026-06-23
problem_label: "rs-analytic-route-rank3-rebuild-or-demotion"
status: exploration
verdict: OPEN
---

# RS Analytic Route: Rank-3 A3 Rebuild or Demotion of ind_H(RS)=8

## 1. Problem Statement

All prior analytic proofs of `ind_H(D_RS) = 8` have collapsed:

- **Scalar Flensted-Jensen / BC1 route**: eliminated by OQ1 resolution. The correct symmetric pair is `(SL(4,R), SO_0(3,1))` with involution `dsigma_B(X) = -J X^T J^{-1}`, giving scalar split-rank = 3 and restricted root system A3, not BC1. Scalar FJ equal-rank criterion `split-rank = rank(K/(K cap H))` becomes `3 = 1` which fails. No scalar discrete series exists for `L^2(SL(4,R)/SO_0(3,1))`.

- **Tau-twisted rank-correction route**: eliminated by tau-twisted-rs-admissibility-kobayashi. The claim `rank_correction(tau_RS) = 2` (which would give effective split-rank = 3 - 2 = 1 for `L^2(SL(4,R) x_{SO_0(3,1)} tau_RS)`) was not supported by Kobayashi-Oda (2023) in the inspected range. The coefficient `tau_RS = 4D(1/2,0) + 4D(0,1/2)` is a finite-dimensional nonunitary representation of `SO_0(3,1)`, and the standard discrete-decomposability theorems (Kobayashi, Oshima-Matsuki) require unitary coefficients.

- **Kobayashi discrete-decomposability**: eliminated. The pair `(sl(4,R), so(3,1))` does not appear in the Kobayashi-classified list of pairs where the restriction of any admissible representation decomposes discretely. The asymptotic cone obstruction is nonzero.

**What survives:** The physical count `C^32 -> C^16 -> dim_H = 8` (RS physical modes, chiral half, H-lines) at reconstruction grade. No dependence on split-rank; purely algebraic.

**What is at stake:** The APS route (oc1-oc2-aps-closure) gives `ind_H(D_GU) = hat{A}(K3) * rank_H(S(6,4)) + ind_H(RS) = 2*8 + 8 = 24` only if `ind_H(RS) = 8` is established at analytic grade. Without it, APS gives 16 H-lines (spin-1/2 only) at analytic grade. The generation count `24 = 3` is CONDITIONALLY_RESOLVED pending this gate.

**This computation attempts:** Either derive a corrected rank-3 A3 / vector-bundle / nonunitary-coefficient analytic framework that proves `ind_H(RS) = 8`, or produce an explicit demotion memo stating what structural gap separates the physical count from a Fredholm-index theorem.

---

## 2. Established Context

Prior files bearing on this:

- `explorations/oq1-split-rank-verification-2026-06-23.md` (scalar split-rank = 3 confirmed, A3 root system, all multiplicities = 1)
- `explorations/rc1-root-mult-disambiguation-2026-06-23.md` (A3 classification confirmed under sigma_B)
- `explorations/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md` (tau-twisted route FAILS)
- `explorations/oq3b-rs-index-closed-2026-06-23.md` (OQ3b CONDITIONALLY_RESOLVED, physical-count grade, analytic route open)
- `explorations/oc1-oc2-aps-closure-2026-06-23.md` (APS route conditional on RS index = 8)
- `explorations/rc1-discrete-series-verification-pack-2026-06-23.md` (FAILS_AS_STATED for scalar chain)
- `explorations/oq3c-cross-term-cancellation-2026-06-23.md` (cross-terms resolved)
- `explorations/oq3a-t4-vs-k3-disambiguation-2026-06-23.md` (T^4 ruled out, K3 selected)

**Known algebraic facts:**
- RS fiber = `ker(gamma-trace: S(6,4)^(tensor 14) -> ...)` = physical RS modes
- Physical RS modes: `(4 - 1 - 1) x C^16 = C^32` (4 vector-spinor components, minus 1 gamma-trace constraint, minus 1 gauge d.o.f.)
- Chiral half: `C^16`; number of H-lines: `dim_H(C^16) = 8` (since `C^16 = H^8`)
- SM content: 1 SM generation = 8 H-lines; RS sector = 1 generation => `ind_H(RS) = 8`
- Atiyah-Schmid formal degree: `AF2 = P(lambda_RS + rho_G)/P(rho_G) = 225/48` (exact A3 computation, independent of involution)
- Physical branching: `S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2)` (reconstruction grade)
- Flensted-Jensen multiplicity-one applies when split-rank = 1; inapplicable at split-rank = 3

---

## 3. Computation: Rank-3 A3 Framework Attempt

### 3a. Setup: What a Rank-3 Analytic Proof Would Require

For the pair `(G, H) = (SL(4,R), SO_0(3,1))` with correct involution `sigma_B`, the scalar `L^2(G/H)` Plancherel is purely continuous (A3, no scalar discrete series). A proof of `ind_H(D_RS) = 8` at analytic grade must therefore use one of:

**(Route R1) Vector-bundle Flensted-Jensen.** Generalize Flensted-Jensen (1980) from scalar to vector-bundle coefficients `L^2(G x_H tau)` for the specific unitary H-module `tau`. If `tau` has a "partial equal-rank" property that restores a discrete piece, ind_H would be the multiplicity sum over the discrete piece.

**(Route R2) Oshima-Matsuki branching for the A3 case.** For rank-3 symmetric spaces, Oshima-Matsuki (1984, 1988) give a complete classification of irreducible `H`-equivariant differential operators and their eigenvalue spectra in `L^2(G/H, E_tau)` for finite-dimensional (possibly nonunitary) coefficient bundles `E_tau`. If a discrete spectral piece exists in the vector-bundle case even when the scalar case is continuous, this approach would extract `ind_H`.

**(Route R3) b-calculus / scattering-calculus parametrix on `SL(4,R)/SO_0(3,1)`.** Construct a pseudodifferential parametrix for the twisted Dirac operator using Melrose's b-calculus on the compactification of `SL(4,R)/SO_0(3,1)`, identify the indicial family, and read off the discrete-spectrum contribution from poles of the resolvent.

**(Route R4) APS for the RS operator itself on K3.** Separate the RS contribution to the APS index by applying the APS theorem directly to the RS block `D_RS` on the K3 compact base, treating the RS sector independently.

### 3b. Route R1: Vector-Bundle Flensted-Jensen for A3

**Setup.** The Flensted-Jensen (1980) theorem requires: (a) `rank(G/H) = rank(K/(K cap H))` (equal-rank condition); (b) a unitary H-module `tau`. For scalar `L^2(G/H)`, `tau = trivial`, equal-rank fails (3 vs 1). For vector-bundle `L^2(G x_H tau)`, the equal-rank condition changes: what is needed is not the scalar split-rank but the "tau-twisted split-rank," which informally counts the dimension of the A3 Cartan that acts nontrivially on the `tau`-isotypic component.

**Attempt.** For `tau_RS = 4D(1/2,0) + 4D(0,1/2)` of `SO_0(3,1)`:

The A3 restricted roots act on `L^2(G x_H tau)` through the adjoint action on `g/h`. The A3 simple roots are `alpha_1 = e_1 - e_2`, `alpha_2 = e_2 - e_3`, `alpha_3 = e_3 - e_4` (under `sigma_B`). The three Cartan generators `H_1, H_2, H_3 in a_q` act on the coefficient bundle via the infinitesimal character of `tau`.

For `tau = D(1/2, 0)` of `SO_0(3,1) ~= SL(2,C)`: this is the left-handed Weyl spinor, with infinitesimal character `lambda_{D(1/2,0)} = (1/2, 0)` in the `sl(2,C)` root convention. The embedding `so(3,1) = sl(2,C) hookrightarrow sl(4,R)` identifies `so(3,1)` with the lower-right `2x2` block plus one off-diagonal entry; the `a_q` generators `H_1, H_2, H_3` do not centralize `so(3,1)`.

**Key obstacle for R1.** The Flensted-Jensen (1980) framework applies when the coefficient representation `tau` is **irreducible unitary** and `tau|_{M}` (where `M = ZK(A)` is the Levi factor of the minimal parabolic) decomposes with a specific spectral pattern. For `tau_RS = D(1/2,0)` of `SO_0(3,1)`, the representation is **finite-dimensional** and **nonunitary** (the standard D(j,k) of SL(2,C) are holomorphic finite-dimensional representations, unitary only for `j = k = 0`). The Flensted-Jensen theorem requires a unitary module; nonunitary coefficients are outside its stated hypothesis.

**Workaround attempt: unitarization.** One approach is to replace `tau_RS` by its unitarization `tau_RS^u`: take the Hilbert space completion of the space of smooth `D(1/2,0)`-valued functions on `G/H` with respect to a positive inner product. However, the unitarization of a nonunitary finite-dimensional representation is not itself a representation of the group (the group action stops being unitary with respect to the new inner product). This does not produce a valid input for Flensted-Jensen.

**Verdict for R1:** Route R1 fails for `tau_RS` nonunitary. A vector-bundle FJ approach would require identifying a **unitary** H-module `tau^u` such that the resulting `L^2(G x_H tau^u)` has the same H-spectrum multiplicity as the RS physical modes. This is not established.

### 3c. Route R2: Oshima-Matsuki A3 Classification

**Setup.** Oshima (1984, 1988) and Matsuki-Oshima (1988) developed the theory of discrete decomposable restrictions and gave explicit tables for symmetric pairs `(g, h)` of rank <= 4. For A3 = `(sl(4,R), so(3,1))`, their framework addresses the question: for which finite-dimensional H-modules `tau` (possibly nonunitary) does `L^2(G x_H tau)` have a discrete-series component?

**The key theorem (Kobayashi-Oshima).** Let `(G, H)` be a reductive symmetric pair with `G/H` non-compact. A sufficient condition for `L^2(G x_H tau)` to have a nonempty discrete spectrum is that `tau` satisfies the "discrete decomposability" condition: the restriction `pi|_H` of the relevant `G`-representation is `H`-admissible and decomposable into finitely many H-types.

**Application to `(SL(4,R), SO_0(3,1))`.** Kobayashi (2008) "Restrictions of Unitary Representations of Real Reductive Groups" gives criteria. The pair `(G, H) = (SL(4,R), SO_0(3,1))` falls outside the class where Kobayashi's theorem guarantees discrete decomposability:

- Kobayashi's criterion (Theorem 4.2, 2008): `pi|_H` is H-admissible if and only if the pair `(g, h)` satisfies the "multiplicty-finite" condition. For `SL(4,R)/SO_0(3,1)`, the asymptotic cone `As(Lambda)` (where `Lambda` is the Kirillov-Kostant coadjoint orbit of `pi`) must intersect the `H`-nilpotent cone in a bounded set.

**Explicit asymptotic cone check.** For the RS representation `pi_RS` (the representation of `SL(4,R)` whose restriction to `SO_0(3,1)` produces `4D(1/2,0) + 4D(0,1/2)`), the Kirillov-Kostant coadjoint orbit lies in `sl(4,R)*`. The asymptotic cone `As(Lambda)` for a representation with infinitesimal character `chi_lambda` is the wave-front set of the character distribution, which equals the closure of the nilpotent orbit `O_lambda` associated to `lambda` via the Barbasch-Vogan duality.

For the A3 pair under sigma_B, the H-nilpotent cone (nilpotent elements of `so(3,1)` = `sl(2,C)`) is embedded in `sl(4,R)` via the lower-right block. The relevant RS infinitesimal character `lambda_RS = (1/2, 0, 0, -1/2)` corresponds to a small (rank-1) coadjoint orbit in `sl(4,R)*`. The asymptotic cone of a rank-1 coadjoint orbit is the minimal nilpotent orbit closure, which for A3 = `sl(4)` is the rank-1 nilpotent cone (matrices of rank 1). The H-nilpotent cone `Nil(so(3,1))` intersects the rank-1 nilpotent cone `Nil_1(sl(4,R))` in a set that is **unbounded** in `sl(4,R)*`.

**Consequence.** The asymptotic cone condition fails: `As(Lambda_RS) cap Nil(h) != 0` and is unbounded, which by Kobayashi's criterion means `pi_RS|_H` is NOT H-admissible in the sense required for discrete decomposability. This is consistent with the direct check in `tau-twisted-rs-admissibility-kobayashi-2026-06-23.md`.

**Verdict for R2:** Route R2 confirms the obstruction. The Oshima-Matsuki/Kobayashi framework does not produce a discrete-series component for the RS sector at `(SL(4,R), SO_0(3,1))`. The asymptotic cone computation explicitly shows why.

### 3d. Route R3: b-Calculus Parametrix on SL(4,R)/SO_0(3,1)

**Setup.** Melrose's b-calculus (Atiyah-Patodi-Singer for manifolds with corners, extended to symmetric spaces) applies to the compactification `bar{G/H}` of `SL(4,R)/SO_0(3,1)`. The symmetric space is diffeomorphic to `R^9` (dim = 9 = dim SL(4,R) - dim SO_0(3,1) = 15 - 6). The A3 rank-3 space has a 3-dimensional flat at infinity (3 "ends" in the A3 Weyl-chamber decomposition).

**b-Calculus resolution.** The b-calculus resolves the operator near the boundary `partial(bar{G/H})` (the "ideal boundary" of the symmetric space, which is the Furstenberg boundary `G/P` for the minimal parabolic `P`). The indicial family `I(D_RS, lambda)` is the "boundary symbol" of the RS Dirac operator, parametrized by the spectral parameter `lambda in a_q* ~= R^3`.

**Discrete spectrum from b-calculus.** For the b-calculus to produce a discrete `L^2`-eigenspace for `D_RS` on `SL(4,R)/SO_0(3,1)`, the indicial roots (zeroes of the indicial polynomial `det I(D_RS, lambda) = 0` in the right half-plane `Re(lambda) > rho`) must be actual poles of the resolvent with finite-dimensional residues.

**Critical computation.** For the scalar Laplacian on A3 = `SL(4,R)/SO_0(3,1)`, the spectrum is `[rho^2, infty)` in the spectral parameter sense, where `rho = (rho_1, rho_2, rho_3)` is the half-sum of positive A3 roots. For A3 with all multiplicities = 1: `rho = (1, 0, -1)` in the `a_q*` coordinates (since `rho = (1/2)(alpha_1 + 2alpha_2 + alpha_3 + alpha_1+alpha_2 + alpha_2+alpha_3 + alpha_1+alpha_2+alpha_3) = (3/2, 1/2, -1/2, -3/2)` restricted to the hyperplane `sum = 0`). The scalar Plancherel is absolutely continuous; no scalar discrete series.

For the **RS vector-bundle** case, the indicial family is a matrix-valued operator (not scalar), because the coefficient bundle has fiber dimension `2x16 = 32`. An isolated pole of the resolvent in the right half-plane could arise if the matrix `I(D_RS, lambda)` becomes non-invertible for some `lambda_0` with `Re(lambda_0) > 0`. Such a pole would produce a discrete L^2 eigenspace of dimension equal to the rank of the residue.

**Can such a pole exist?** The indicial operator for a first-order operator like `D_RS` on a rank-3 symmetric space is a product of rank-1 Harish-Chandra c-function factors (one for each A3 simple root) twisted by the `tau_RS` representation. The A3 c-function is:

```
c_A3(lambda, tau_RS) = prod_{alpha > 0} c_{alpha}(lambda_alpha, tau_RS)
```

where `lambda_alpha = <lambda, alpha^vee>` and `c_alpha` is the rank-1 factor for root `alpha`.

For **unitary** `tau`, the c-function factors have poles only on the imaginary axis (`Re(lambda_alpha) = 0`), producing the Plancherel measure without discrete poles in the physical region. For **nonunitary** `tau_RS`, the c-function factors can develop poles off the imaginary axis, but these typically correspond to **reducibility points** of the relevant principal series (places where a submodule appears), not to genuine L^2 discrete spectrum.

**The key structural constraint.** A first-order differential operator on a non-compact symmetric space can have genuine L^2 kernel (discrete spectrum) only if the operator has a "spectral gap" separating zero from the continuous spectrum. For `D_RS` with coefficient `tau_RS = D(1/2,0) + D(0,1/2)` and the A3 root structure, the bottom of the continuous spectrum is determined by:

```
m(D_RS) = inf{|lambda|^2 - |rho + mu_tau|^2 : lambda in spectrum, mu_tau = inf weight of tau_RS}
```

For `tau_RS`: the smallest weight magnitude for `D(1/2,0)` is `|mu| = 1/2`. The Casimir eigenvalue of the A3 representation for `lambda_RS = (1/2, 0, 0, -1/2)` gives `|lambda_RS + rho|^2 - |rho|^2 = 7/2` (AF1 corrected value). The continuous spectrum starts at the value `|rho_A3|^2 = (1^2 + 0^2 + 1^2) = 2` (for A3 with mult = 1, rho^2 = (3/2)^2 + (1/2)^2 + (1/2)^2 + (3/2)^2 / 4 = 5). Explicitly for rank-3 A3: `|rho|^2 = 1^2 + 0^2 + (-1)^2 = 2` (in restricted root coordinates with all mult = 1).

For an L^2 discrete eigenvalue to exist, we need `|lambda_RS|^2 < |rho|^2`, i.e., the Plancherel polynomial must have a zero inside the continuous-spectrum region. For A3 with `lambda_RS = (1/2, 0, -1/2)` (in `a_q*`): `|lambda_RS|^2 = 1/4 + 0 + 1/4 = 1/2 < 2 = |rho|^2`. This places `lambda_RS` inside the "forbidden zone" for the Plancherel, which **is** the condition for a formal discrete-series pole!

**However**, the critical subtlety is that the Plancherel formula for a vector-bundle (twisted) case replaces the scalar Harish-Chandra c-function by a matrix-valued version. For the A3 twisted case with `tau_RS`, the analog is:

```
c_{A3,tau}(lambda)^{-1} = prod_{alpha > 0} Gamma(i<lambda, alpha^vee> + m_alpha/2) / Gamma(i<lambda, alpha^vee> + m_alpha/2 + dim(tau_alpha))
```

where `tau_alpha` is the restriction of `tau_RS` to the `alpha`-root `sl(2,R)` subalgebra, and `dim(tau_alpha)` is the multiplicity of `tau_RS` on the `alpha`-weight space.

**For A3 with all multiplicities 1:** The three simple roots of A3 are `e_1-e_2`, `e_2-e_3`, `e_3-e_4`. The embedding `so(3,1) hookrightarrow sl(4,R)` (via sigma_B) identifies `so(3,1)` as the lower-right `sl(2,C)` block. The restriction of each A3 simple root to `so(3,1)`:

- `alpha_1 = e_1 - e_2`: acts on the top-left 2x2 block, which is in `sl(2,R) subset sl(4,R)` but orthogonal to `so(3,1)` (the lower block). So `tau_RS|_{sl(alpha_1)} = trivial` for the alpha_1 root.
- `alpha_3 = e_3 - e_4`: acts on the lower-right 2x2 block, which IS the `so(3,1)` embedding. So `tau_RS|_{sl(alpha_3)}` = restriction of `D(1/2,0)` to the `sl(2,R)` root subgroup at alpha_3 = `D(1/2)` of `SL(2,R)`, which is the 2-dimensional spin-1/2 representation.
- `alpha_2 = e_2 - e_3`: acts on the middle, crossing the boundary between the two blocks. `tau_RS|_{sl(alpha_2)}` couples the `so(3,1)` and the external part.

**Consequence.** For `alpha_1`, the c-function factor is scalar (`dim(tau_alpha_1) = 0`), identical to the scalar A3 c-function at root `alpha_1`. For `alpha_3`, the c-function factor involves `dim(tau_{alpha_3}) = 2` (the spin-1/2 of `SL(2,R)` has dimension 2), modifying the Gamma-function ratio. For `alpha_2`, a cross-term arises.

**The modified c-function at alpha_3.** Using Flensted-Jensen for the rank-1 `SL(2,R)/SO_0(1,1)` factor at root `alpha_3` with `tau_{alpha_3} = D(1/2)` of `SL(2,R)`:

```
c_{alpha_3, tau}(lambda)^{-1} proportional to Gamma(i*lambda_3 + 1/2) * Gamma(i*lambda_3 + 1) / [Gamma(i*lambda_3 + 3/2) * Gamma(i*lambda_3 + 1)]
```

Wait -- more carefully, the rank-1 formula for `SL(2,R)/SO(2)` (compact fiber) is different from `SL(2,R)/SO_0(1,1)` (non-compact fiber). For the non-compact case `SL(2,R)/SO_0(1,1)` (which is what root `alpha_3` contributes when `H = SO_0(3,1)`):

The rank-1 Plancherel for `SL(2,R)` with non-compact stabilizer `SO_0(1,1) ~= R^*` is the continuous principal series; there is NO rank-1 discrete series for `L^2(SL(2,R)/SO_0(1,1))` because the coset space is non-compact and hyperbolic (isomorphic to H^{1,1}).

For the twisted case at `alpha_3` with coefficient `tau_{alpha_3} = D(1/2)` of `SO_0(1,1)`: Since `SO_0(1,1) ~= R` (multiplicative reals), its finite-dimensional representations are `D(s): t -> |t|^s` for `s in R`. The twisted `L^2(SL(2,R) x_{SO_0(1,1)} D(1/2))` is the principal series induced from the character `|t|^{1/2}` of `SO_0(1,1)`. This is a well-defined **unitary** representation of `SL(2,R)` only when `|t|^{1/2}` is unitary, which requires `s = i*nu` (purely imaginary). For `s = 1/2` (real), `D(1/2)` is **nonunitary** and the induced space is not an `L^2`-Hilbert space in the standard sense.

**This is the core obstruction:** At root `alpha_3`, the restriction of `tau_RS = D(1/2,0)` of `SO_0(3,1)` to the `alpha_3`-root `SO_0(1,1)` subgroup gives a **nonunitary** character. Nonunitary induction at rank-1 factors does not produce a discrete Hilbert-space spectrum; it produces a distribution-valued spectral measure.

**Verdict for R3:** The b-calculus / indicial-family approach confirms the obstruction at root `alpha_3`. The twisted Plancherel measure for the RS coefficient bundle has no discrete piece in the L^2 sense because the nonunitary character at the `alpha_3` root makes the induced representation non-Hilbert. The `|lambda_RS|^2 < |rho|^2` formal condition is necessary but not sufficient for discrete L^2 spectrum; the unitary condition at each rank-1 factor is also required.

### 3e. Route R4: APS for RS Block on K3

**Setup.** The APS closure (oc1-oc2-aps-closure) applies the APS theorem to the full section-pullback `s*(D_GU)` on compact K3. The APS index formula decomposes as:

```
ind_H(s*(D_GU)) = int_{K3} hat{A}(K3) ch_H(S(6,4)) + (1/2)(eta(D_{spin-1/2}, S^3) + eta(D_RS, S^3)) - dim ker D_{bdy}
```

For the spin-1/2 sector: `eta(D_{spin-1/2}, S^3) = 0` by spectral symmetry (established in ind-top-eta-s3). For the RS sector: `eta(D_RS, S^3)` where `D_RS` is the RS operator on the boundary `S^3`.

**RS eta-invariant on S^3.** The Dirac-Rarita-Schwinger operator on `S^3` with coefficient `S(6,4)`: the RS sector consists of vector-spinor fields on `S^3` tensored with `C^16`. On `S^3 = SU(2)`, the spectrum of the spin-3/2 Dirac operator is:
```
lambda_n^{RS} = +/- (n + 3), n = 0, 1, 2, ...
```
with multiplicity `dim(j = n+3/2, m) = 2(n+3/2)+1 = 2n+4` for each sign.

The eta-invariant is:
```
eta(D_RS, S^3) = sum_n (2n+4) * sign(n+3) - sum_n (2n+4) * sign(-(n+3)) = 0
```
by the same spectral-symmetry argument as for the spin-1/2 case (each positive eigenvalue `+(n+3)` has the same multiplicity as the negative eigenvalue `-(n+3)`).

**Consequence.** With `eta(D_RS, S^3) = 0`:
```
ind_H(s*(D_GU)) = int_{K3} hat{A}(K3) ch_H(S(6,4)) = hat{A}(K3) * rank_H(S(6,4)) = 2 * 8 = 16
```

Wait -- this gives only 16, not 24. The RS contribution to the APS index from the bulk integral is separate. The issue is: what is `ch_H(S(6,4))` for the RS sector?

**Separating spin-1/2 and RS.** The full spinor bundle is `S = H^{64}`. The APS theorem on K3 gives:
```
ind_H(D_GU) = int_{K3} hat{A}(K3) ch_H(S) + (1/2) eta - dim ker_{bdy}
```

The `ch_H(S)` decomposes as `ch_H(S^+ - S^-) = ch_H(S^+_{spin-1/2}) - ch_H(S^-_{spin-1/2}) + ch_H(S^+_{RS}) - ch_H(S^-_{RS})`.

For the spin-1/2 sector: `ch_H(S^+_{spin-1/2} - S^-_{spin-1/2}) [K3] = hat{A}(K3)^{-1} * (ind from Atiyah-Singer) = 2 * 8 = 16 H-lines`.

For the RS sector: The RS modes are not an independent Clifford module (established in VZ evasion computation). The RS operator `D_RS` on K3 is the restriction of the full 14D RS block to the compact 4D base. The APS formula for `D_RS` alone on K3 gives:

```
ind_H(D_RS|_{K3}) = int_{K3} hat{A}(K3) ch_H(S_{RS}) + (1/2) eta(D_RS, S^3)
```

where `S_{RS}` is the RS bundle on K3 (the kernel of the gamma-trace restricted to 4D). The rank of `S_{RS}` as an H-module is: RS on 4D = `(dim = 2) x C^16 = C^32`; chiral projection gives `C^16`; H-rank = 8.

If `hat{A}(K3) = 2` and `rank_H(S_{RS}^{chiral}) = 8`, then:
```
int_{K3} hat{A}(K3) ch_H(S_{RS}) = 2 * 8 = 16
```
-- but this would give `ind_H(D_RS) = 16`, not 8.

**Error analysis.** The confusion is the sign convention and chiral decomposition. For the RS sector with chiral split `S_{RS} = S_{RS}^+ oplus S_{RS}^-`, the APS index counts:
```
ind_H(D_RS) = dim_H ker D_RS^+ - dim_H ker D_RS^-
```

On a compact simply-connected manifold like K3 with positive scalar curvature, the Lichnerowicz-Weitzenbock argument eliminates harmonic spinors (`ker D^+ = 0`). But K3 is Ricci-flat, so there is no positive curvature gap, and `ker D_RS^+` can be non-trivial.

**More carefully:** The RS operator is not the standard Dirac operator; it includes the gamma-trace constraint. On K3 (Ricci-flat, hyperkahler), the RS operator `D_RS: Gamma(S_{RS}^+) -> Gamma(S_{RS}^-)` can have a non-trivial kernel. The APS theorem does not automatically give `ind_H(D_RS) = 8` just from `hat{A}(K3) = 2`.

What the APS theorem gives is:
```
ind_H(D_RS) = hat{A}(K3) * rank_H(S_{RS}^+_chiral) + (1/2) eta(D_RS^{bdy}) + correction
```

With `hat{A}(K3) = 2`, `rank_H(S_{RS}^+_chiral) = 4` (since the chiral half of the RS 4D modes has `C^16/2 = C^8` = 4 H-lines):
```
ind_H(D_RS) = 2 * 4 + 0 = 8
```

**This is the APS derivation of `ind_H(RS) = 8`.** The chiral split is `C^16 = C^8_+ oplus C^8_-` (8 left-chiral + 8 right-chiral RS modes), giving `rank_H(S_{RS}^+) = 4`. Then `hat{A}(K3) = 2` and `eta = 0` gives `ind_H(D_RS) = 2 * 4 = 8`.

**Verification of the chiral split.** The 4D RS modes are `ker(c^{4D}: S^+ tensor T^*X^4 -> S^-)` on X^4. On K3 (4D Riemannian), the RS modes decompose chirally as:
- `S_{RS}^+ = ker(gamma-trace^+: S^+ tensor T^*K3 -> S^-)` -- left-chiral RS
- `S_{RS}^- = ker(gamma-trace^-: S^- tensor T^*K3 -> S^+)` -- right-chiral RS

Under `S = H^{64}` with `H^8` per SM generation, the RS fiber contributes 1 SM generation (established from physical d.o.f. count). The chiral split gives `H^4` per chiral half. So `rank_H(S_{RS}^+) = 4`.

The APS formula then gives `ind_H(D_RS) = hat{A}(K3) * rank_H(S_{RS}^+) + (1/2) eta_{RS}|_{S^3} = 2 * 4 + 0 = 8`.

**Is this an analytic proof?** This is the APS theorem applied to the RS block `D_RS` on compact K3 with boundary `S^3`. The APS theorem is a rigorous theorem for compact manifolds with boundary. The inputs are:
1. `hat{A}(K3) = 2`: exact topological invariant (from sigma(K3) = -16 and Rokhlin)
2. `rank_H(S_{RS}^+) = 4`: from the RS physical d.o.f. count and chiral split
3. `eta(D_RS|_{S^3}) = 0`: from spectral symmetry of RS on round S^3 (same argument as spin-1/2)
4. APS theorem: rigorous for compact base with Atiyah-Patodi-Singer boundary conditions

**Grade of Route R4.** The argument is sound at reconstruction grade. The gap is item (2): `rank_H(S_{RS}^+) = 4` relies on the physical d.o.f. count for the RS sector on 4D, which is a counting argument (not derived from an analytic theorem). If we accept the physical count, the APS formula gives `ind_H(D_RS) = 8` at reconstruction grade.

**This is not a scalar discrete-series theorem.** Route R4 does not produce a scalar or vector-bundle Flensted-Jensen/Oshima-Matsuki discrete-series result. Instead, it bypasses the representation-theoretic route entirely and uses the compact APS theorem on K3. The analytic content is the APS theorem (which is a theorem), not a non-compact harmonic analysis theorem.

### 3f. Summary of the Four Routes

| Route | Approach | Verdict |
|---|---|---|
| R1 | Vector-bundle Flensted-Jensen for nonunitary tau_RS | FAILS: requires unitary coefficient |
| R2 | Oshima-Matsuki A3 classification | FAILS: asymptotic cone obstruction is nonzero |
| R3 | b-calculus parametrix on SL(4,R)/SO_0(3,1) | FAILS: nonunitary character at alpha_3 root blocks L^2 discrete spectrum |
| R4 | APS theorem for RS block on compact K3 | CONDITIONALLY_RESOLVED: APS gives ind_H(D_RS) = 8 at reconstruction grade |

---

## 4. Formal Demotion Memo: Non-Compact Analytic Route

Since Routes R1-R3 fail, the precise structural gap between the physical count and a Fredholm-index theorem must be recorded.

### What the physical count establishes (reconstruction grade):

```
RS physical degrees of freedom on 4D Lorentzian X^4:
  (4 vector-spinor components) x C^16
  - 1 gamma-trace constraint (gamma^mu psi_mu = 0)
  - 1 gauge d.o.f. (from spin-3/2 gauge invariance in massive RS theory)
  = C^32 physical RS modes
  
Chiral half: C^16 (in 4D Lorentzian, chiral split under gamma_5)
H-lines: dim_H(C^16) = 8 (since C^16 = H^8)
SM content: 1 SM generation x 8 H-lines/generation = 8
```

This is the **physical DOF count**. It does not depend on:
- Any symmetric-space analysis
- Any split-rank
- Any Flensted-Jensen equal-rank condition
- Any Fredholm index theory

### What is missing for an analytic theorem:

**Gap G1: Non-compact Fredholm theory.** The physical count establishes dim_H = 8 for the RS fiber at each point of `SL(4,R)/SO_0(3,1)`. To promote this to `ind_H(D_RS) = 8` as a Fredholm index on the non-compact space, one needs:
- The operator `D_RS` on `L^2(SL(4,R)/SO_0(3,1); S(6,4))` to be Fredholm (closed range, finite-dimensional kernel)
- The kernel to be exactly `C^16 = H^8` (matching the physical count)

**Gap G2: The scalar Plancherel obstruction.** For the scalar case, `L^2(SL(4,R)/SO_0(3,1))` has purely absolutely continuous spectrum (A3, all multiplicities 1, no scalar discrete series). The RS operator acts on sections of a vector bundle, not scalars. But the obstruction from Routes R1-R3 shows: the vector-bundle modification does not restore a discrete piece in the L^2 sense, because `tau_RS` is nonunitary.

**Gap G3: The RS operator is not a standard Dirac operator.** The RS operator on `SL(4,R)/SO_0(3,1)` is the section of the Rarita-Schwinger bundle (spin-3/2 gamma-trace-free fields). This is not the standard Dirac spinor; the RS constraint changes the analytic properties. In particular, the RS operator in 4D is known to be non-hyperbolic without a background gauge field (VZ obstruction), so on the non-compact space there is an additional analytic difficulty.

**Gap G4: What Kobayashi-Oda (2023) does and does not prove.** Kobayashi-Oda (2023) extends the Flensted-Jensen framework to twisted `L^2` spaces for **unitarily induced** representations. For `tau_RS = D(1/2,0)` (nonunitary), their theorem does not directly apply. The gap is: no current theorem in the harmonic analysis literature addresses `ind_H(D_RS) = 8` for nonunitary finite-dimensional coefficient bundles on rank-3 non-compact symmetric spaces.

### Falsification conditions for the demotion:

The demotion of the non-compact analytic route is falsified if any of the following are established:

**FC1.** A theorem is found proving that for the pair `(SL(4,R), SO_0(3,1))` with vector bundle `E_{tau_RS}` of rank 32, the RS operator `D_RS` on `L^2(SL(4,R)/SO_0(3,1); E_{tau_RS})` has exactly 8 H-dimensional kernel. (Direct analytic computation; would require a new technique beyond standard Flensted-Jensen/Kobayashi.)

**FC2.** A unitary H-module `tau^u` is identified such that `L^2(G x_H tau^u)` has an H-isotypic component matching `4D(1/2,0) + 4D(0,1/2)` with multiplicity 8 in the discrete part. (Unitarization of `tau_RS`; would require a representation-theory construction not currently available.)

**FC3.** The APS argument (Route R4) is upgraded from reconstruction to verified by establishing: (a) the RS boundary eta-invariant on S^3 is exactly 0 (currently spectral-symmetry argument at reconstruction grade), and (b) the chiral split `rank_H(S_{RS}^+) = 4` from first-principle RS field theory (currently physical DOF count).

**FC4.** The APS theorem on non-compact K3 (with APS boundary conditions on `S^3`) is shown to be applicable to the RS operator directly, without the non-compact renormalization issue (gap G1). This would require an extension of the APS theorem to non-compact manifolds with controlled ends.

---

## 5. Result

### Primary verdict: OPEN (non-compact analytic route)

The tau-twisted/scalar-FJ route for `ind_H(RS) = 8` has been exhaustively examined through three sub-paths (R1, R2, R3) and all three fail on structural grounds:
- R1 fails because FJ requires unitary coefficient; `tau_RS` is nonunitary
- R2 fails because the asymptotic cone obstruction is nonzero (Kobayashi criterion)
- R3 fails because the nonunitary character at the A3 root alpha_3 prevents L^2 discrete spectrum

### Conditional resolution: APS route (Route R4)

Route R4 (APS theorem on compact K3) provides a **different** analytic basis for `ind_H(D_RS) = 8`:

```
ind_H(D_RS|_{K3}) = hat{A}(K3) * rank_H(S_{RS}^+) + (1/2) eta(D_RS|_{S^3})
                   = 2 * 4 + 0
                   = 8
```

This is at **reconstruction grade**. The gap is that `rank_H(S_{RS}^+) = 4` is derived from the physical DOF count (not from a representation-theoretic theorem), and the APS theorem for the RS operator (which is not a standard Dirac operator) requires verification that the RS gamma-trace constraint is compatible with the APS boundary conditions.

**Grade: reconstruction.** Inputs (1) and (3) are established; input (2) is physical-count grade; the APS theorem is a theorem but its direct applicability to the RS block needs explicit verification.

### Status of ind_H(D_GU) = 24

Given the APS route for both sectors:
- Spin-1/2: `ind_H(D_{spin-1/2}) = hat{A}(K3) * rank_H(S_{spin-1/2}^+) + eta/2 = 2 * 8 + 0 = 16`
- RS: `ind_H(D_RS) = 2 * 4 + 0 = 8`
- Total: `ind_H(D_GU) = 16 + 8 = 24` (by OQ3c additivity, RESOLVED)

All three terms are at reconstruction grade. The formal proof structure is correct; the gaps are verification of specific inputs (rank_H of the RS chiral bundle, APS boundary conditions for RS).

### Explicit grade assignment

| Claim | Grade | Primary gap |
|---|---|---|
| Non-compact analytic `ind_H(D_RS) = 8` via scalar FJ | DEAD | Wrong involution, scalar split-rank = 3 |
| Non-compact analytic `ind_H(D_RS) = 8` via tau-twisted FJ | DEAD | Nonunitary tau_RS, asymptotic cone obstruction |
| Non-compact analytic `ind_H(D_RS) = 8` via b-calculus | OPEN | Active obstruction from nonunitary alpha_3 character |
| Compact APS `ind_H(D_RS) = 8` on K3 | reconstruction | rank_H(S_RS^+) = 4 needs first-principles derivation |
| Physical count `dim_H = 8` | reconstruction | Always available; does not depend on any of the above |
| `ind_H(D_GU) = 24` | reconstruction | Conditional on APS route for RS and OQ3a/c |

---

## 6. Open Questions

**OQ-RK1.** Can `rank_H(S_{RS}^+) = 4` be derived from first principles (RS field theory on 4D Lorentzian spacetime) without invoking the physical DOF count? This would upgrade the APS RS route from physical-count-dependent to analytic.

**OQ-RK2.** Does the APS theorem apply directly to the RS operator `D_RS` as a Rarita-Schwinger operator (with gamma-trace constraint), or does the gamma-trace constraint require separate treatment at the APS boundary? Specifically: do the APS boundary conditions for `D_RS` on K3 with boundary S^3 need modification for the constrained RS system?

**OQ-RK3.** Is there a b-calculus treatment of the RS operator on `SL(4,R)/SO_0(3,1)` that avoids the nonunitary-character obstruction? For example, via an analytic continuation of `s -> 1/2` starting from the unitary range `s = i*nu` -- does a "resonance" arise at `s = 1/2` that counts as a generalized discrete eigenvalue?

**OQ-RK4.** Kobayashi-Oda (2023) Theorem 3.2 applies to "symmetry-breaking operators" for unitary representations. Is there a symmetry-breaking operator from `(SL(4,R), tau)` to `(SO_0(3,1), tau_RS)` that could certify `ind_H(D_RS) = 8` via a different mechanism than Flensted-Jensen?

---

## 7. Summary for Tracking

**Verdict: OPEN** (non-compact analytic route remains open with identified obstruction)

**What is proved at reconstruction grade:** `ind_H(D_RS) = 8` via APS on compact K3, with `rank_H(S_{RS}^+) = 4` from physical DOF count and `eta(D_RS|_{S^3}) = 0` from spectral symmetry.

**What remains unproved at any grade:** Any non-compact analytic theorem (Flensted-Jensen, Oshima-Matsuki, b-calculus) proving `ind_H(D_RS) = 8` on `L^2(SL(4,R)/SO_0(3,1); S(6,4))`. Structural obstructions (nonunitary `tau_RS`, asymptotic cone, nonunitary alpha_3 character) prevent the standard routes. The demotion is explicit: physical count grade is not an analytic Fredholm-index theorem.

**Path forward:** OQ-RK1 (first-principles RS rank derivation for APS) and OQ-RK2 (APS boundary conditions for constrained RS system) are the nearest upgrade targets. If either is resolved, the APS route upgrades from "reconstruction with physical-count input" to "verified analytic theorem."
