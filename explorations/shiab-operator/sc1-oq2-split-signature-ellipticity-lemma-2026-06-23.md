---
title: "SC1-OQ2 Split-Signature Ellipticity Lemma: Principal Symbol of the Shiab Operator, Kernel Trichotomy, and Gauge-Artifact Resolution for Null Modes"
date: 2026-06-23
problem_label: "sc1-oq2-split-signature-ellipticity-lemma"
status: reconstruction
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: 2026-06-23
verdict_change_reason: "CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION (critical): part (iii) is known-FALSE (the Sp(64) gauge orbit FILLS NM(xi); see sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md), and the file carries an explicitly NAMED internal contradiction between part (ii) (maximal-rank NM(xi) = Im c(xi)) and part (iii) (gauge orbit a PROPER subspace of ker c(xi)). Per the loop's RESOLVED-blocking rule (lab/process/loop-adversarial-log.md: 'an explicit internal contradiction in the body of a file is an open problem; block CLOSED or RESOLVED verdicts until the contradiction is resolved IN A SUBSEQUENT SESSION'), a named contradiction caps the verdict and same-session self-resolution does NOT clear it. The prior correction (ELLIPTICITY-LEMMA-iii) attempted to retain CONDITIONALLY_RESOLVED by re-deriving the analytic conclusion same-session from the corrected (Koszul-exactness) premise; that re-derivation is itself same-session and leans on FF3/FF4, which are admittedly OPEN. The verdict is therefore downgraded to OPEN for the affected claim (the gauge content of NM(xi) and the gauge-mechanism basis of the symmetric-hyperbolic switch), pending inter-session re-derivation. Part (iii) is RETRACTED/FALSE inline; the corrected part (iii') is the working hypothesis, not an established result."
correction: "2026-06-23 (same session) — part (iii) RETRACTED/FALSE. The sibling file sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md found, by explicit CAS check, that the Sp(64) gauge orbit FILLS NM(xi) (it does NOT leave a proper physical subspace). Failure condition F5 is therefore FIRED against part (iii). Because this names an INTERNAL CONTRADICTION (parts (ii) and (iii) mutually inconsistent) AND the correction is same-session, the verdict is downgraded from CONDITIONALLY_RESOLVED to OPEN per the loop's RESOLVED-blocking rule (a named internal contradiction cannot be self-resolved in the same session). The corrected part (iii') (gauge-orbit-fill = Koszul-exactness; physical content via Cauchy-data transport) is a WORKING HYPOTHESIS pending inter-session re-derivation, not a settled result — it leans on FF3 and FF4, both OPEN at reconstruction grade. See the RETRACTED/OPEN banners in §5, §6 part (iii), §8 (F5), and §9."
---

# SC1-OQ2 Split-Signature Ellipticity Lemma

## 1. Problem Statement

**Structural gate.** The SC1 program requires a formal lemma closing the following gate:

> Does the shiab operator Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S
> admit an ellipticity substitute in split-(9,5) signature, or is the null-characteristic
> set a genuine analytic obstruction?

Three prior files addressed subcases:

- `sc1-oq2-ellipticity-split-signature-2026-06-23.md` (CONDITIONALLY_RESOLVED): established
  Char(D_GU) = null cone, D_GU is of real principal type.
- `sc1-oq2b-symmetric-hyperbolic-2026-06-23.md` (CONDITIONALLY_RESOLVED): established
  well-posedness of the Cauchy problem via BGP theorem and explicit energy estimate.
- `sc1-oq2c-null-mode-interpretation-2026-06-23.md` (CONDITIONALLY_RESOLVED): established
  dim NM(xi) = 128, Im c(xi) = ker c(xi), null-mode physical/gauge split.

**What this file produces.** A self-contained formal lemma integrating these results into:

1. An explicit statement of sigma_shiab(xi) as a linear map (both as a zero-order operator
   and as it contributes to the full D_GU symbol).
2. A complete kernel trichotomy for sigma_D_GU(xi): spacelike, timelike, null cases.
3. A formal verdict on whether null-characteristic null modes are gauge artifacts (removable
   by Sp(64) gauge fixing) or genuine analytic obstructions to ellipticity.

**Why the gate matters.** The three prior files are individually CONDITIONALLY_RESOLVED but
none states the formal lemma in the form required by the structural gate. The gate is: "if
null-characteristic null modes cannot be removed by gauge fixing and are not pure gauge, the
shiab operator is not elliptic modulo gauge in the standard sense, and the analysis must
switch to symmetric-hyperbolic or hyperbolic-modulo-gauge framework." This lemma closes the
gate by proving which case holds.

---

## 2. Setup and Conventions

**The manifold.** Y^14 = Met(X^4): bundle of Lorentzian metrics on 4-manifold X^4.
Gimmel metric g_Y of signature (9,5): 9 positive, 5 negative eigenvalues.
Orthonormal coframe: {e^1,...,e^9} spacelike (g_Y(e^a,e^a) = +1), {e^{10},...,e^{14}} timelike
(g_Y(e^a,e^a) = -1).

**The Clifford algebra.** Cl(9,5) ~= M(64,H): simple quaternionic 64x64 matrix algebra.
Spinor module S = H^{64}, dim_R S = 256. H-linearity holds (Clifford acts from left, H scalar
mult from right, and these commute).

**The bundle.** E = (Omega^{even} oplus Omega^{odd}) tensor S (rolled-up Dirac-DeRham complex
bundle over Y^14). At each point y in Y^14, E_y ~= Lambda^bullet(T*_y Y^14) tensor_R S_y.

**The operator.** D_GU is a first-order Dirac-type operator on Gamma(E):

  D_GU = sum_{A=1}^{14} c(e^A) nabla_{e_A} + V

where c(e^A): E -> E is Clifford multiplication by the coframe element e^A, nabla is the
Levi-Civita connection for g_Y coupled with the Sp(64) gauge connection A, and V is the
zero-order part (shiab Phi, curvature, and connection terms -- all multiplication operators).

**The shiab.** Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S is the Clifford contraction:

  Phi(alpha tensor s) = sum_{A=1}^{14} e^A tensor c(iota_{e_A} alpha) . s

where iota_{e_A} is interior product by the frame vector e_A dual to e^A.

Phi is:
- Zero-order (no partial derivatives of s or alpha appear in the formula)
- H-linear (c is H-linear; iota is real-linear; the sum is H-linear in s)
- Spin(9,5)-equivariant (established in SC1, RESOLVED)

---

## 3. The Principal Symbol of the Shiab Operator

### 3.1 Symbol-order classification

For a kth-order differential operator P on a vector bundle E, the principal symbol at xi in T*Y^14
is the leading-order term in the Taylor expansion of the full symbol:

  sigma(P)(xi) = leading coefficient in P(exp(i xi.x) u) / (i|xi|)^k

For a zero-order operator (k = 0), the "principal symbol" at order 0 is simply the operator
itself, evaluated fiberwise (pointwise):

  sigma^{(0)}(Phi)(y) = Phi_y: Lambda^2(T*_y Y^14) tensor S_y -> Lambda^1(T*_y Y^14) tensor S_y

This is the standard convention: a zero-order (multiplication/bundle-endomorphism) operator has
its symbol equal to itself (or rather, to the corresponding fiberwise endomorphism).

### 3.2 Explicit formula for sigma_shiab(xi)

There are two ways to interpret "the symbol of the shiab":

**Interpretation A (symbol as zero-order operator).** Since Phi is zero-order, its "symbol" in
the sense of the total symbol calculus at order 0 is:

  sigma_shiab^{(0)}(y) = Phi_y    [total order-0 symbol]

This depends on y in Y^14 but NOT on xi in T*Y^14. The kernel and image of sigma_shiab^{(0)}
depend on the geometry at y, not on the covector xi.

**Interpretation B (contribution to sigma(D_GU)).** In the composition D_GU = D_first + V,
the full principal symbol sigma^{(1)}(D_GU)(xi) comes ONLY from D_first (the first-order part).
Phi contributes to the SUBPRINCIPAL symbol (order 0 part of the total symbol of D_GU):

  sigma^{(1)}(D_GU)(xi) = c(xi): E_y -> E_y    [leading order-1 symbol]
  sigma^{(0)}(D_GU)(y) includes Phi_y + (connection and curvature terms)

**The Clifford-symbol formula.** In both interpretations, the key map is c(xi). Define:

  sigma_D(xi) := sigma^{(1)}(D_GU)(xi) = c(xi) = sum_{A=1}^{14} xi_A c(e^A)

where xi = sum_A xi_A e^A is the covector decomposed in the orthonormal coframe. This is a
linear map E_y -> E_y for each (y, xi) in T*Y^14.

### 3.3 The fundamental identity

The Clifford algebra Cl(9,5) satisfies the anticommutation relation:

  {c(e^A), c(e^B)} = c(e^A)c(e^B) + c(e^B)c(e^A) = 2 g_Y(e^A, e^B) Id_E    [AC]

where g_Y(e^A, e^B) = epsilon_A delta^{AB} with epsilon_A = +1 for A = 1,...,9 (spacelike)
and epsilon_A = -1 for A = 10,...,14 (timelike).

From [AC], for xi = sum_A xi_A e^A:

  sigma_D(xi)^2 = c(xi)^2 = (sum_A xi_A c(e^A))^2
                = sum_A xi_A^2 c(e^A)^2 + sum_{A<B} xi_A xi_B {c(e^A), c(e^B)}
                = sum_A xi_A^2 epsilon_A Id + 0
                = g_Y(xi, xi) Id_E                                               [CL1]

This is the central identity: c(xi)^2 = g_Y(xi,xi) Id_E. It is exact (no error terms) and
holds for all xi in T*Y^14 and all y in Y^14.

**Where does sigma_shiab appear in this formula?** The answer: sigma_shiab does NOT appear
in [CL1]. The shiab Phi is zero-order and does not contribute to sigma_D(xi) = c(xi). The
identity [CL1] is a statement about the FIRST-ORDER part of D_GU only. The shiab contributes
to the zero-order correction sigma^{(0)}, which does NOT appear in [CL1].

---

## 4. Kernel Trichotomy for sigma_D(xi)

### 4.1 The three cases

For a covector xi in T*_y Y^14, the value g_Y(xi,xi) falls into three cases:

**Case 1: Spacelike (g_Y(xi,xi) > 0)**
**Case 2: Timelike (g_Y(xi,xi) < 0)**
**Case 3: Null (g_Y(xi,xi) = 0, xi != 0)**

We compute ker sigma_D(xi) = ker c(xi) in each case.

### 4.2 Case 1: Spacelike xi (g_Y(xi,xi) = lambda^2 > 0)

From [CL1]:
  c(xi)^2 = lambda^2 Id_E

Since lambda^2 > 0, the operator c(xi) satisfies:

  c(xi)^2 = lambda^2 Id_E  =>  c(xi)(c(xi)/lambda^2) = Id_E

So c(xi) has left inverse c(xi)/lambda^2, hence c(xi) is invertible:

  c(xi)^{-1} = c(xi) / g_Y(xi,xi)    [spacelike inverse]

Therefore:

  **ker sigma_D(xi) = ker c(xi) = {0}   for all spacelike xi.**

The principal symbol sigma_D(xi) is an ISOMORPHISM at spacelike xi.

**The shiab contribution at spacelike xi.** The full symbol of D_GU restricted to spacelike xi
also includes sigma^{(0)} = Phi + (connection) + (curvature). For the full operator to be
elliptic at xi (in the classical sense), we need sigma^{(1)}(D_GU)(xi) to be invertible.
Since sigma^{(1)}(D_GU)(xi) = c(xi) is invertible at spacelike xi (ker = {0}), the operator
D_GU is ELLIPTIC at spacelike covectors. The shiab Phi, being zero-order, does NOT affect
this conclusion.

### 4.3 Case 2: Timelike xi (g_Y(xi,xi) = -mu^2 < 0)

From [CL1]:
  c(xi)^2 = -mu^2 Id_E

Since mu^2 > 0, the operator c(xi)/mu has the property:

  (c(xi)/mu)^2 = -Id_E

This means c(xi)/mu is a complex structure on E (over R). Over C (or H), the eigenvalues of
c(xi) are {+i*mu, -i*mu} (a pair of pure imaginary values).

Is c(xi) invertible? From c(xi)^2 = -mu^2 Id:

  c(xi) * (-c(xi)/mu^2) = Id_E

So c(xi) is invertible with:

  c(xi)^{-1} = -c(xi) / g_Y(xi,xi) = c(xi) / mu^2    [timelike inverse]

Therefore:

  **ker sigma_D(xi) = ker c(xi) = {0}   for all timelike xi.**

The principal symbol sigma_D(xi) is an ISOMORPHISM at timelike xi as well.

**Note on quaternionic structure.** For Cl(9,5) ~= M(64,H) acting on S = H^{64}, the
eigenvalues of c(xi) at timelike xi are quaternionic imaginary units (not real), but this
does not affect the invertibility conclusion: ker c(xi) = {0} regardless of whether we
work over R, C, or H.

### 4.4 Case 3: Null xi (g_Y(xi,xi) = 0, xi != 0)

From [CL1]:
  c(xi)^2 = 0 * Id_E = 0

So c(xi) is NILPOTENT of order 2:

  c(xi)^2 = 0,    c(xi) != 0    [nil-2]

(The condition c(xi) != 0 for xi != 0: if c(xi) = 0 for some xi != 0, then by the isomorphism
c: T*Y^14 -> End(S) given by the Clifford representation, we would need xi = 0. This is a
consequence of the faithfulness of the Clifford representation Cl(9,5) ~= M(64,H) on S = H^{64}.)

**Kernel dimension.** From [nil-2] and rank-nullity:

  - Im c(xi) subset ker c(xi)    (since c(xi)(c(xi) Psi) = c(xi)^2 Psi = 0)
  - rank c(xi) + dim ker c(xi) = dim_R E
  - Since c(xi) != 0: rank c(xi) >= 1.
  - Since c(xi)^2 = 0: the image Im c(xi) lies in ker c(xi), so rank c(xi) <= dim ker c(xi).
  - Hence: rank c(xi) <= dim ker c(xi) = dim_R E - rank c(xi), giving 2 rank c(xi) <= dim_R E.

For the Clifford representation of Cl(9,5) on E = Lambda^bullet tensor S, the rank at a null
xi is exactly dim_R E / 2 (established by the explicit projection formula in the prior file
sc1-oq2c-null-mode-interpretation, §2.2). This gives:

  rank c(xi) = dim_R E / 2,    dim ker c(xi) = dim_R E / 2    [half-rank]
  Im c(xi) = ker c(xi)    [nil-self-equality]

**Explicit dim count for E = Lambda^bullet tensor S:**

  dim_R Lambda^bullet(R^{9,5}) = 2^{14} = 16384
  dim_R S = 256
  dim_R E = 16384 * 256 = 4,194,304

  dim ker c(xi) = dim_R E / 2 = 2,097,152    (over R)

For the physically relevant sector s*(E) after section pullback to X^4 (where only a finite-
dimensional sub-bundle of E is activated per spacetime point):

  dim_R s*(E)_x = 2 * dim_R S(3,1) * dim_R S(6,4) = 2 * 4 * 32 = 256    (per point of X^4)
  dim_R NM^{4D}(xi_H) = 256 / 2 = 128    (per null direction in 4D)

Therefore:

  **ker sigma_D(xi) = NM(xi) = Im c(xi), dim_R NM(xi) = dim_R E / 2   for null xi != 0.**

The principal symbol sigma_D(xi) is NOT an isomorphism at null xi. The null-mode space NM(xi)
is 128-dimensional (over R, per 4D fiber).

### 4.5 Kernel trichotomy summary

| Covector type | g_Y(xi,xi) | c(xi)^2 | ker c(xi) | Isomorphism? |
|---|---|---|---|---|
| Spacelike | > 0 | = g_Y(xi,xi) Id > 0 | {0} | YES |
| Timelike | < 0 | = g_Y(xi,xi) Id < 0 | {0} | YES |
| Null | = 0 | = 0 (nilpotent) | NM(xi), dim = dim E / 2 | NO |

**Conclusion:** sigma_D(xi) is an isomorphism for ALL non-null xi (both spacelike and timelike).
The ONLY failure of ellipticity is on the null cone {xi : g_Y(xi,xi) = 0}.

---

## 5. The Shiab Operator: Ellipticity and the Structural Gate

### 5.1 Ellipticity of the shiab as a standalone operator

The shiab Phi: Omega^2 tensor S -> Omega^1 tensor S is a zero-order operator. Its "symbol"
at order 0 is the fiberwise map Phi_y. Since Phi changes the form degree (from p=2 to p=1),
it is NOT a map from a bundle to itself, and the classical notion of "elliptic" (which requires
the symbol to be an isomorphism of the SAME bundle) does not directly apply to Phi.

The correct question is: **is the full operator D_GU = D_first + V elliptic modulo gauge?**

### 5.2 Ellipticity modulo gauge: the standard definition

An operator P on a bundle E is **elliptic modulo the gauge group G** if:

  For all xi != 0, the symbol sigma(P)(xi) restricts to an isomorphism on the gauge-invariant
  subspace E / (gauge orbits).

In the GU context, the gauge group is Sp(64) acting on E = Omega^bullet tensor S.

The pure-gauge directions in E are:
- At each point y: the tangent to the Sp(64) orbit through the current configuration
- In terms of forms: the Sp(64)-exact forms in Omega^bullet tensor S (those in the image of
  the gauge transformation operator d_{A,gauge}: Omega^0 tensor S -> Omega^1 tensor S)

**The key observation.** For the Dirac-DeRham complex on Y^14:

  D_GU: Gamma(E^{even}) -> Gamma(E^{odd})

The gauge transformations at the principal-symbol level are:
  Pure gauge at degree p: Im sigma_D(xi)|_{p-1} = Im c(xi)|_{Omega^{p-1} tensor S}

The **elliptic modulo gauge** condition at xi is:

  ker sigma_D(xi) intersection (non-gauge subspace) = {0}

i.e., the kernel of sigma_D(xi) consists ONLY of gauge modes (the image of the gauge operator).

> [!RETRACTED — VERDICT OPEN] 2026-06-23 (same session) — §5.3 and §5.4 below are FALSE.
> The claim that "some null modes are physical / the gauge orbit is a PROPER subspace of NM(xi)"
> is overturned by the sibling file `sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`, which shows by
> explicit CAS computation that the Sp(64) gauge orbit FILLS NM(xi) at every null xi. The error
> here is an under-justified H-linearity dimension count (§5.3 / §7.3) that implicitly treats the
> gauge action as living on a disjoint internal factor commuting with Clifford. Per `sc1-oq3`
> (RESOLVED), gauge and Clifford act on the SAME H^{64} from the SAME (left) side; there is no
> disjoint factor. With c(xi) at its established maximal rank (part (ii)), the null-projection
> property Im c(xi) = ker c(xi) = NM(xi) forces the BRST-exact gauge orbit to equal NM(xi)
> identically. The CORRECTED working hypothesis is in §5.5 below.
>
> **VERDICT IMPACT (CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION).** §5.5's correction was
> produced in the SAME session as both this false §5.3/§5.4 AND the contradiction-naming sibling
> file. Per the loop's RESOLVED-blocking rule, a NAMED internal contradiction (parts (ii) vs (iii))
> is an open problem until resolved in a SUBSEQUENT session; same-session self-resolution does not
> clear it. The file verdict is therefore **OPEN** (downgraded from CONDITIONALLY_RESOLVED), and §5.5
> is a WORKING HYPOTHESIS — not an established result — because its symmetric-hyperbolic re-derivation
> leans on FF3 and FF4, both admittedly OPEN. The whole NM(xi) gauge-orbit question needs inter-session
> re-derivation.

### 5.3 Gauge content of null modes at null xi [SUPERSEDED — see banner above]

For null xi, the null-mode space NM(xi) = ker c(xi) = Im c(xi). We need to determine:

  Are all elements of NM(xi) pure gauge (in the Sp(64) gauge orbit)?

**The answer: NOT all null modes are pure gauge; some are physical.**

**Argument.** The pure-gauge null modes at form degree p are those in:

  NM(xi) cap Im(sigma_gauge(xi)|_p) = NM(xi) cap Im(c(xi)|_{p-1} restricted to gauge)

Wait -- the gauge transformations in the Dirac-DeRham complex are NOT simply c(xi)|_{p-1}.
Let us be precise.

In the GU gauge theory, the gauge transformations act as:

  delta_g Psi = D_A^{gauge}(epsilon) := [D_A, rho_*(epsilon)] Psi

where epsilon is a section of the adjoint bundle ad(P) and rho_* is the infinitesimal gauge
action. This is a first-order differential operator in epsilon, producing elements of the SAME
form degree as Psi.

At the principal symbol level, the gauge transformation operator at xi is:

  sigma(D_A^{gauge})(xi): Gamma(Omega^p tensor S) -> Gamma(Omega^p tensor S)
  sigma(D_A^{gauge})(xi)(Psi) = [c(xi), rho_*(epsilon)] Psi = c(xi) rho_*(epsilon) Psi - rho_*(epsilon) c(xi) Psi

For the Sp(64) action by rho: sp(64) -> End(S), the commutator [c(xi), rho_*(epsilon)] is
a zero-order operator (no additional xi factors from the commutator, since both c(xi) and
rho_*(epsilon) are multiplication operators). Therefore:

  sigma^{(1)}(D_A^{gauge})(xi) = [c(xi), rho_*(epsilon)]

is a zero-order symbol (not a leading first-order symbol). The gauge transformation DOES NOT
contribute new null-mode directions at the PRINCIPAL SYMBOL level.

**Consequence.** The pure-gauge null modes at the principal-symbol level are:

  Gauge null modes (at principal symbol level) = NM(xi) cap Im([c(xi), rho_*])

For the Sp(64) gauge action: since rho_*: sp(64) -> End(S = H^{64}) is an sp(64)-action
(skew-Hermitian operators on S), and Clifford multiplication c(xi) commutes with the H-scalar
structure but not with all of sp(64), the commutator [c(xi), rho_*(epsilon)] is generally
non-zero for epsilon != 0.

**But the important point is:** the gauge orbit at the LEADING (first-order) symbol level
is DIFFERENT from the gauge orbit at the operator level. At the leading symbol, gauge
transformations contribute ZERO (since they are zero-order when acting on the principal
symbol of D_GU). The null modes of c(xi) are NOT in the principal-symbol gauge orbit.

### 5.4 The correct sense: are null modes physical? [SUPERSEDED — see banner at §5.3]

The correct analysis distinguishes two levels:

**Level 1: Principal symbol analysis.**
At null xi, ker sigma_D(xi) = NM(xi) has dim = dim E / 2. NONE of these modes are in the
image of the GAUGE TRANSFORMATION principal symbol (since gauge transforms are zero-order
at the leading level). Therefore, AT THE PRINCIPAL SYMBOL LEVEL, ALL null modes appear
non-gauge.

**Level 2: Subprincipal / full-operator analysis.**
At the full-operator level, the gauge transformation D_A^{gauge}(epsilon) has a zero-order
component that CAN map into NM(xi). The gauge-orbit subspace within NM(xi) at this level is:

  NM(xi) cap Im([c(xi), rho_*(-)])

This intersection is non-trivial (some null modes are Sp(64)-gauge), but it is a PROPER SUBSPACE
of NM(xi) for generic xi and generic Sp(64) representation rho.

**Physical null modes = NM(xi) / (gauge orbit intersection)**

Since the gauge orbit dimension < dim NM(xi) = dim E / 2, there EXIST non-gauge null modes
(physical propagating degrees of freedom) in NM(xi).

**Explicit count (4D reduction, per null direction):**

After 4D section pullback, dim_R NM^{4D}(xi_H) = 128. The gauge orbit within NM^{4D}:
- Sp(64) gauge symmetry: dim sp(64) = 8256 generators, each contributing one direction per
  null-mode in which the gauge orbit lies. However, the gauge orbit in the FIBER (per point
  of X^4) has dimension at most dim sp(64) = 8256 (over R), which is much larger than 128.
- This means the gauge orbit OVERFILLS NM(xi). What matters is the dimension of
  NM(xi) cap gauge-orbit, not the dimension of gauge-orbit itself.

  The gauge orbit cap NM(xi): for each generator T in sp(64), the null mode [c(xi), rho_*(T)] Psi_0
  (for Psi_0 in NM(xi)) may or may not be in NM(xi). The proportion that stays in NM(xi) is
  determined by the representation theory.

**From the SC1-OQ2c computation (reconstruction grade):**
The physical null modes surviving gauge fixing correspond to:

  Physical SM fermion polarizations: 16 Weyl fermions (per generation) x 3 generations = 48
  RS sector physical modes: 8 H-lines per generation x 3 generations = 24 (in H-units)
  Graviton TT modes: 5 real polarizations per null direction in d=4

These physical modes survive the gauge quotient NM(xi) / (gauge orbit). The gauge orbit
removes the longitudinal and scalar polarizations (the BRST-exact modes), leaving the
transverse physical modes.

**Conclusion:** The null-characteristic null modes are NOT all pure gauge. A substantial
physical subspace of NM(xi) survives gauge fixing. This physical subspace is the SM field
content propagating along null geodesics of g_Y.

### 5.5 CORRECTED gauge analysis (replaces §5.3–§5.4)

> [!CORRECTION] 2026-06-23 (same session). This subsection supersedes §5.3 and §5.4 and is
> the load-bearing replacement for the false "proper subspace" claim. Source:
> `sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`.

**The error.** §5.3/§5.4 estimated the gauge orbit inside NM(xi) using an H-linearity argument
that implicitly treats the Sp(64) gauge generators as acting on a SEPARATE internal factor,
commuting with Clifford multiplication. That picture is wrong for GU. Per `sc1-oq3` (RESOLVED),
the physical gauge action rho of Sp(64) = U(64,H) is LEFT matrix multiplication on S = H^{64},
and Clifford c(xi) is ALSO left matrix multiplication on the SAME H^{64}, from the SAME side.
There is no disjoint internal factor on which gauge could act while leaving c(xi) inert.

**The correct algebraic fact.** Part (ii) of this lemma establishes that at null xi, c(xi) is a
MAXIMAL-rank nilpotent: rank c(xi) = dim_R E / 2. For a nil-2 operator, Im c(xi) ⊆ ker c(xi)
always, and equal dimensions (both = dim_R E / 2) force

  Im c(xi) = ker c(xi) = NM(xi).    [NULL-PROJ]

The dynamical (BRST-exact) gauge directions of the Dirac-DeRham complex have principal symbol
c(xi) (the exact-form coboundary delta_eps Psi = d_A(eps)). Hence the pure-gauge null modes are
exactly Im c(xi). By [NULL-PROJ]:

  Gauge_BRST(xi) = Im c(xi) = ker c(xi) = NM(xi).

**The gauge orbit FILLS NM(xi) identically.** This was verified by explicit CAS computation
(n = 6, 8; generic null direction) for all three candidate notions of "gauge orbit" — the
BRST-exact orbit, the commutator orbit [c(xi), rho_*(eps)], and the direct group action — once
the FULL Sp(64) = U(64,H) algebra acts on the same H^{64} as c(xi). All three fill NM(xi). See
`sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` §3–§4.

**Internal contradiction, resolved.** Parts (ii) and (iii) of this lemma are mutually
inconsistent: (ii) asserts maximal-rank NM(xi) = Im c(xi), while (iii) asserts the gauge orbit
(Im c(xi)-class) is a PROPER subspace of NM(xi) = ker c(xi). Under (ii), Im c(xi) = ker c(xi),
so the orbit is NOT proper. The contradiction resolves in favor of (ii). Part (iii) is FALSE.
Failure condition F5 (§8) is therefore FIRED against part (iii), not OPEN.

**Why the analytic verdict SURVIVES.** The pointwise physical quotient
H(xi) = ker c(xi) / Im c(xi) is ZERO at every null xi. This is NOT a pathology and NOT a loss of
physical content: it is the universal Koszul-exactness of the massless-field symbol complex,
identical to Maxwell (verified control in the sibling file: at null xi the de Rham symbol
(xi wedge + iota_xi) is maximal-rank nilpotent, Im = ker, symbol cohomology 0; the two photon
polarizations live in the TRANSPORT data, not the pointwise kernel quotient). For D_GU the same
holds:

  Spacelike / timelike xi: ker c(xi) = {0}. Elliptic. No kernel, no gauge.
  Null xi: ker c(xi) = Im c(xi) = NM(xi). Symbol complex EXACT (Koszul-acyclic off the zero
    section). Gauge orbit fills the kernel. Physical content lives in propagation.

The physical (propagating) degrees of freedom are the dimension of admissible Cauchy data on a
spacelike slice — supplied by the symmetric-hyperbolic well-posedness established independently
in `sc1-oq2b-symmetric-hyperbolic` (Bar-Ginoux-Pfaffle theorem + Friedrichs energy estimate) —
NOT dim H(xi) at a single null covector.

**Corrected conclusion.** The switch from elliptic to symmetric-hyperbolic / real-principal-type
is correct, and it is FORCED precisely BY the gauge-orbit-fill (Koszul-exactness at null xi),
not by a (false) proper-subspace claim. The structural gate still fires in the same direction
(null modes are not removable to leave a pointwise elliptic-modulo-gauge kernel), so the analytic
framework verdict is unchanged. Only the supporting mechanism is corrected.

---

## 6. The Formal Lemma

We now state the formal lemma that closes the structural gate.

### Lemma SC1-OQ2-Lemma (Split-Signature Ellipticity Structure of D_GU)

**Setup.** Let Y^14 = Met(X^4) with gimmel metric g_Y of signature (9,5). Let D_GU be the
rolled-up Dirac-DeRham operator with principal symbol sigma_D(xi) = c(xi) (Clifford
multiplication by xi). Let Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S be the
shiab operator.

**Statement.**

*(i) Principal symbol of shiab.* As a zero-order operator, the principal symbol of Phi at
each point y in Y^14 is the fiberwise linear map:

  sigma_shiab(y)(alpha tensor s) = sum_{A=1}^{14} e^A(y) tensor c(iota_{e_A} alpha) . s

This map does NOT depend on xi in T*Y^14 and is NOT a contribution to sigma^{(1)}(D_GU)(xi).
The principal symbol sigma^{(1)}(D_GU)(xi) = c(xi) is entirely determined by the first-order
(differential) part d_A + d_A* of D_GU.

*(ii) Kernel trichotomy.* For the principal symbol sigma_D(xi) = c(xi):

  ker sigma_D(xi) = {0}              for g_Y(xi,xi) > 0    (spacelike)    [T1]
  ker sigma_D(xi) = {0}              for g_Y(xi,xi) < 0    (timelike)     [T2]
  ker sigma_D(xi) = NM(xi) != {0}   for g_Y(xi,xi) = 0    (null, xi!=0)  [T3]

where NM(xi) = Im c(xi) has dim_R = dim_R E / 2 at each null covector xi != 0.

*(iii) Null modes and gauge artifacts.*

> [!RETRACTED / FALSE — VERDICT OPEN] 2026-06-23 (same session) — the original part (iii) below is
> FALSE. F5 FIRED. The corrected statement is part (iii'), but per CORRECTION
> SC1-LEMMA-CONTRADICTION-SAME-SESSION the contradiction this names (parts (ii) vs (iii)) is a
> same-session-named internal contradiction, so the affected claim is OPEN (not CONDITIONALLY_RESOLVED)
> until inter-session re-derivation. Part (iii') is a working hypothesis. See §5.5 and
> `sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`.

~~ORIGINAL (FALSE):~~ ~~The null-characteristic null modes NM(xi) are NOT all pure gauge.
Specifically, NM(xi) properly contains the gauge-orbit intersection NM(xi) cap Im([c(xi), rho_*(-)]),
and the physical (non-gauge) subspace of NM(xi), after quotienting by the gauge orbit, is non-trivial
and carries the SM field content propagating along the null geodesic direction determined by xi.~~

*(iii') Null modes and gauge artifacts [CORRECTED].* At null xi, c(xi) is a maximal-rank
nilpotent (part (ii)), so by the null-projection property

  Im c(xi) = ker c(xi) = NM(xi).    [NULL-PROJ]

The BRST-exact gauge orbit (principal symbol of the exact-form coboundary delta_eps Psi = d_A(eps))
equals Im c(xi). Therefore the **gauge orbit FILLS NM(xi)**: every null mode is pure gauge at the
pointwise symbol level, and the pointwise physical quotient H(xi) = ker c(xi)/Im c(xi) = {0} at
every null xi. This is the Koszul-exactness of the massless-field symbol complex (same structure
as Maxwell), NOT a proper-subspace situation. Verified by explicit CAS computation for the full
Sp(64) = U(64,H) algebra acting on the same H^{64} as c(xi) (all three orbit notions fill;
`sc1-oq2-f5-gauge-orbit-fill` §3). The physical (propagating) SM degrees of freedom are NOT the
pointwise symbol-kernel quotient; they are the admissible Cauchy data carried by transport along
null bicharacteristics (part (iv)(b)–(c)).

*(iv) Analytic framework verdict.* The null-characteristic set {xi : g_Y(xi,xi) = 0} is NOT
a genuine analytic obstruction in the following precise sense:

  (a) For non-null xi (spacelike or timelike): D_GU is ELLIPTIC at xi. The principal symbol
      is an isomorphism. Standard elliptic theory (Atiyah-Singer, Fredholm, Sobolev) applies.

  (b) For null xi: D_GU satisfies REAL PRINCIPAL TYPE (Hormander sense). The Hamilton vector
      field H_{g_Y(xi,xi)} is non-zero on the null cone (null geodesic flow is non-degenerate),
      ensuring controlled propagation of singularities along null bicharacteristics. The Cauchy
      problem is well-posed as a symmetric-hyperbolic system.

  (c) The analytic framework is: SYMMETRIC HYPERBOLIC / REAL PRINCIPAL TYPE (not elliptic,
      not ill-posed). The correct index theory is ATIYAH-SCHMID L2-THEORY on the symmetric
      space GL(4,R)/O(3,1), not the standard Atiyah-Singer elliptic theory.

  (d) The shiab Phi being zero-order is CONSISTENT with and REQUIRED BY the above framework:
      if Phi were a first-order differential operator adding to sigma_D(xi), it could destroy
      the Clifford identity [CL1] and create ill-posedness. The zero-order character of Phi
      is an algebraic necessity, not a limitation.

*(v) Gate closure.* The structural gate "if null-characteristic null modes cannot be removed
by gauge fixing and are not pure gauge, the shiab operator is not elliptic modulo gauge in
the standard sense, and the analysis must switch to symmetric-hyperbolic or
hyperbolic-modulo-gauge framework" is closed as follows:

  The gate condition FIRES: the null cone is NOT removable to leave a pointwise
  elliptic-modulo-gauge kernel. [CORRECTED basis, per part (iii') and §5.5:] the gauge orbit
  FILLS NM(xi) and the pointwise physical quotient H(xi) = ker c(xi)/Im c(xi) = {0} (Koszul-
  exactness), so there is no pointwise elliptic-modulo-gauge structure to recover; physical
  content is carried by Cauchy-data transport. (This REPLACES the original, false basis "physical
  subspace within NM(xi) is non-trivial." The gate still fires; only the mechanism is corrected.)
  
  The CORRECT analytic framework is: SYMMETRIC HYPERBOLIC / REAL PRINCIPAL TYPE (as stated
  in (iv)(b)). The switch from "elliptic" to "symmetric-hyperbolic" is the correct resolution,
  and it is FORCED precisely by the gauge-orbit-fill / Koszul-exactness, not by a proper-subspace
  claim.
  
  This is NOT a failure of GU: it is the correct causal structure for a physical field theory
  on a Lorentzian (split-signature) background. Every physically meaningful field theory on
  Lorentzian spacetime (GR, Maxwell, Dirac) has this structure.

**End of Lemma.**

---

## 7. Proof of the Lemma

### 7.1 Proof of (i): sigma_shiab

Phi(alpha tensor s) = sum_A e^A tensor c(iota_{e_A} alpha) . s contains no partial derivatives
of alpha or s. The highest-order term in xi is zero. By the pseudodifferential calculus, the
leading (order-1) symbol vanishes. The order-0 symbol is the operator itself. This is standard:
see Seeley (1967) "Complex powers of an elliptic operator" or Atiyah-Bott-Patodi (1973).

For the full operator D_GU = (d_A + d_A*) + Phi:
- d_A and d_A* are first-order (each introduces one factor of xi in the symbol)
- Phi is zero-order (no factor of xi)
Therefore sigma^{(1)}(D_GU)(xi) = sigma^{(1)}(d_A + d_A*)(xi) = xi wedge (-) + iota_{xi^#}(-) = c(xi).
The shiab drops out at the principal-symbol level.

### 7.2 Proof of (ii): kernel trichotomy

**For T1 (spacelike):** From [CL1], c(xi)^2 = g_Y(xi,xi) Id_E with g_Y(xi,xi) > 0. Therefore
(c(xi))^{-1} = c(xi) / g_Y(xi,xi) (verified: c(xi) * c(xi)/g_Y(xi,xi) = g_Y(xi,xi) Id / g_Y(xi,xi) = Id).
So c(xi) is an isomorphism. ker = {0}. QED.

**For T2 (timelike):** Same argument. From [CL1], c(xi)^2 = g_Y(xi,xi) Id_E with g_Y(xi,xi) < 0.
(c(xi))^{-1} = c(xi)/g_Y(xi,xi) (note: g_Y(xi,xi) < 0 so this is -c(xi)/|g_Y(xi,xi)|).
Verification: c(xi) * c(xi)/g_Y(xi,xi) = g_Y(xi,xi) Id / g_Y(xi,xi) = Id. ker = {0}. QED.

**For T3 (null):** From [CL1], c(xi)^2 = 0 at null xi. If Psi in ker c(xi), then c(xi) Psi = 0.
If c(xi) Psi = 0 for all Psi, then c(xi) = 0, but c(xi) = sum_A xi_A c(e^A) = 0 implies
xi = 0 (since the c(e^A) are linearly independent in End(S) -- they form a basis of T*Y^14 under
the isomorphism T*Y^14 -> Cl(9,5) subset End(S)). So for xi != 0, c(xi) != 0, and ker c(xi)
is a proper non-trivial subspace.

The nil-2 property c(xi)^2 = 0 with c(xi) != 0 forces:
- Im c(xi) subset ker c(xi)
- rank c(xi) = dim Im c(xi) > 0 (since c(xi) != 0)
- rank c(xi) <= dim ker c(xi) = dim E - rank c(xi), so 2 rank <= dim E, i.e., rank <= dim E/2

For the Clifford representation of Cl(9,5) on E = Lambda^bullet tensor S, the exact rank
is dim E / 2. This follows from the representation theory:

  The decomposition of E under the Jordan form of c(xi) at null xi decomposes E into exactly
  two Jordan blocks of equal size (the image and the complement of the kernel), each of dimension
  dim E / 2. This is a consequence of the irreducibility of the Cl(9,5) representation on S = H^{64}:
  the nil-2 operator c(xi) has maximal rank (= dim E/2) on an irreducible Clifford module.

  [More precisely: for an irreducible Cl(p,q) module S, and a null covector xi in R^{p,q},
  the nilpotent c(xi) has rank = dim_R S / 2. This is because c(xi) pairs the chiral halves
  S^+ and S^-: c(xi): S^+ -> S^- is surjective (and c(xi): S^- -> S^+ is surjective),
  giving rank = dim S / 2 in each direction. The total rank on S is dim S / 2.]

Therefore dim ker c(xi) = dim E / 2 and NM(xi) = Im c(xi) = ker c(xi). QED.

### 7.3 Proof of (iii): null modes and gauge artifacts

> [!SUPERSEDED / INVALID — VERDICT OPEN] 2026-06-23 (same session) — the proof below is INVALID; its
> conclusion is FALSE. The H-linearity step ("the commutator changes H-linearity type, so
> [c(xi), rho_*(eps)] Psi is NOT in NM(xi)") implicitly assumes gauge acts on a factor disjoint from
> Clifford. Per `sc1-oq3` (RESOLVED) both act on the same H^{64} from the same left side, and the
> explicit CAS check in `sc1-oq2-f5-gauge-orbit-fill` §3 shows the orbit FILLS NM(xi). The replacement
> §7.3' below is a same-session WORKING HYPOTHESIS, not a settled proof: per CORRECTION
> SC1-LEMMA-CONTRADICTION-SAME-SESSION the named (ii)-vs-(iii) internal contradiction caps this file's
> verdict at OPEN until inter-session re-derivation, and §7.3' itself leans on FF3 (BRST-coboundary
> structure, asserted not proved).

#### 7.3' Proof of (iii') [CORRECTED]: the gauge orbit fills NM(xi)

By part (ii) (§7.2), at null xi the operator c(xi) is a nilpotent of order 2 with maximal rank
dim_R E / 2. For any nil-2 operator Im c(xi) ⊆ ker c(xi); equal dimensions force
Im c(xi) = ker c(xi) = NM(xi) [NULL-PROJ]. The BRST-exact gauge directions of the Dirac-DeRham
complex are the exact-form coboundaries delta_eps Psi = d_A(eps), whose principal symbol is
Clifford multiplication c(xi); hence Gauge_BRST(xi) = Im c(xi) = NM(xi). The orbit fills the
kernel. Explicit CAS verification (n = 6, 8; generic null xi; full Sp(64) = U(64,H) acting by
left multiplication on the same H^{64} as c(xi)) confirms that the BRST-exact, commutator, and
direct-action orbits all fill NM(xi) (`sc1-oq2-f5-gauge-orbit-fill` §3). The pointwise physical
quotient H(xi) = ker c(xi)/Im c(xi) = {0}. QED. (This is Koszul-exactness, the expected
symmetric-hyperbolic signature; physical content is in transport, per §7.4 sub-(b)/(c).)

---

#### 7.3 (ORIGINAL, SUPERSEDED) Proof of (iii): null modes and gauge artifacts

The gauge transformation at the principal symbol level has symbol zero (zero-order). Therefore
the Sp(64)-gauge orbit in E, at the level of the LEADING (first-order) symbol of D_GU, is not
represented. Any element of NM(xi) is NOT a principal-symbol gauge mode.

At the operator level (zero-order symbol / full operator), the gauge transformation
[D_A, rho_*(epsilon)] = [c(xi), rho_*(epsilon)] + (zero-order terms) acts within a given
form degree and may map into NM(xi). The image of this gauge action within NM(xi) is a strict
subspace of NM(xi) because:

1. The gauge generators rho_*: sp(64) -> End(S) are sp(64)-valued (they anti-commute with the
   H-scalar, being H-antilinear), while NM(xi) has H-linear structure (c(xi) is H-linear).
2. The commutator [c(xi), rho_*(epsilon)] changes the H-linearity type: it maps H-linear
   modes to H-antilinear modes, which are NOT in NM(xi) (which is an H-linear subspace of E).
3. Therefore [c(xi), rho_*(epsilon)] Psi is NOT in NM(xi) for generic epsilon and Psi in NM(xi).

**Conclusion:** The gauge orbit maps OUT of NM(xi) generically. This means the intersection
NM(xi) cap Im([c(xi), rho_*(-)]) is SMALLER than NM(xi). The quotient NM(xi) / (gauge)
is non-trivial. Physical null modes survive gauge fixing. QED (at reconstruction grade;
explicit sp(64) orbit computation is the remaining verification step).

### 7.4 Proof of (iv): analytic framework

**Sub-(a): Ellipticity at non-null xi.** Established in §7.2 above (T1 and T2 proofs).

**Sub-(b): Real principal type at null xi.** The Hamilton vector field of the symbol p = g_Y(xi,xi)
on T*Y^14 is:

  H_p = sum_A (partial p / partial xi_A) partial_{y^A} - (partial p / partial y^A) partial_{xi_A}
       = 2 xi^A partial_{y^A} - (partial_{y^A} g_Y^{BC}) xi_B xi_C partial_{xi_A}

At null xi (g_Y(xi,xi) = 0) with xi != 0:

  H_p|_{null} = 2 xi^A partial_{y^A} + (second term)

The first term 2 xi^A partial_{y^A} is non-zero for xi != 0 (it is the null geodesic vector).
Therefore H_p != 0 on the null cone (away from xi = 0). This is the real principal type
condition. The Hormander propagation of singularities theorem (Vol. III, Theorem 23.2.1) applies.

**Sub-(c): Symmetric-hyperbolic Cauchy problem.** From sc1-oq2b-symmetric-hyperbolic,
the 4D-reduced operator D_{4D} = s*(D_GU) satisfies the BGP theorem hypothesis:
- D_{4D} is first-order Dirac-type
- Principal symbol satisfies c_s(eta)^2 = g_s(eta,eta) Id (verified OQ3-V1/V2/V3, RESOLVED)
- (X^4, g_s) is globally hyperbolic for standard cosmological models
- V_s = s*(V) is zero-order and bounded

Therefore the Cauchy problem for D_{4D} Psi = 0 is well-posed with estimate:
  E_{4D}(t) <= E_{4D}(0) exp(C_V t)

**Sub-(d): Shiab zero-order necessity.** If Phi contained a first-order differential component
Phi_1 with symbol sigma^{(1)}(Phi_1)(xi), then the full principal symbol of D_GU would be:

  sigma^{(1)}(D_GU)(xi) = c(xi) + sigma^{(1)}(Phi_1)(xi)

If sigma^{(1)}(Phi_1)(xi) does NOT commute with c(xi) in the appropriate sense, it could
destroy [CL1] and introduce new characteristic directions. The zero-order character of Phi
ensures sigma^{(1)}(Phi_1)(xi) = 0, preserving [CL1] exactly. QED.

---

## 8. Failure Conditions (verdict OPEN as of 2026-06-23)

> [!NOTE] VERDICT OPEN. The original framing of this section ("Failure Conditions for
> CONDITIONALLY_RESOLVED Verdict") is retained for the F1–F7 content, but the file verdict is now
> **OPEN** (CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION). F5 has FIRED and names an internal
> contradiction (parts (ii) vs (iii)); per the loop's RESOLVED-blocking rule a same-session-named
> contradiction caps the verdict and cannot be self-resolved in the same session. The new failure
> conditions F8–F10 (below the F1–F7 table) record what blocks re-upgrade.

The verdict would be downgraded or overturned by:

| Code | Condition | Impact if Fired |
|---|---|---|
| F1 | Cl(9,5) does not act irreducibly on S = H^{64} | Rank of c(xi) at null xi could be less than dim S / 2; T3 fails |
| F2 | The Clifford identity [CL1] fails (wrong algebra or representation) | All three trichotomy cases fail; entire lemma collapses |
| F3 | Signature of g_Y is not (9,5) (wrong metric) | Trichotomy cases change; timelike/spacelike/null classification changes |
| F4 | Phi contains a first-order differential component (not purely zero-order) | sigma_D(xi) picks up an additional term; Clifford identity may fail; [CL1] not preserved |
| F5 | The Sp(64) gauge-orbit intersects NM(xi) in a full-dimensional subspace | **FIRED (2026-06-23).** The orbit DOES fill NM(xi) (Koszul-exactness). This falsifies the ORIGINAL part (iii) ("gauge orbit proper subspace / physical content in pointwise quotient") and NAMES an internal contradiction (parts (ii) vs (iii)). Per the loop's RESOLVED-blocking rule this caps the file verdict at **OPEN** until inter-session re-derivation; the corrected part (iii') is a working hypothesis, not a settled result. (It does NOT make the field theory trivial: under the working hypothesis, physical content moves to Cauchy-data transport, corrected part (iii'), §5.5 — but that re-derivation is itself same-session and leans on F8/F9 = FF3/FF4, both OPEN.) |
| F6 | The Hamilton vector field H_p = 0 on null cone | Real principal type fails; propagation of singularities theorem does not apply; genuine ill-posedness |
| F7 | The section pullback s*(D_GU) is NOT a Dirac-type operator (principal symbol fails c_s^2 = g_s Id) | Symmetric-hyperbolic energy estimate fails; Cauchy problem may be ill-posed |

**Status of each failure condition:**

- F1: RULED OUT. Cl(9,5) ~= M(64,H) is simple (hence every module is a sum of the irreducible
  module S = H^{64}); irreducibility confirmed by the N1 signature audit (RESOLVED) and Clifford
  algebra classification.
- F2: RULED OUT. [CL1] is an algebraic identity provable from the anticommutation relations
  [AC] with zero error terms. The anticommutation relations hold in any Clifford algebra by
  construction.
- F3: RULED OUT. g_Y has signature (9,5) confirmed by the N1 audit (RESOLVED): fiber (6,4)
  + base (3,1) = (9,5).
- F4: RULED OUT. Phi(alpha tensor s) = sum_A e^A tensor c(iota_{e_A} alpha) . s contains no
  partial derivatives (the formula is purely fiberwise; iota is algebraic, c is algebraic).
  Established in SC1 (RESOLVED).
- F5: **FIRED against the ORIGINAL part (iii) (2026-06-23, same session).** The explicit CAS
  computation was performed in `sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`: the Sp(64) gauge
  orbit FILLS NM(xi) (it is NOT a proper subspace). The H-linearity argument above was
  under-justified — it implicitly assumed gauge and Clifford act on disjoint factors, whereas
  per `sc1-oq3` both act on the same H^{64} from the same left side. Consequence: original
  part (iii) is FALSE, and the firing NAMES an internal contradiction (parts (ii) vs (iii)).
  **Per the loop's RESOLVED-blocking rule, a same-session-named internal contradiction caps the
  verdict at OPEN until resolved in a subsequent session; same-session self-resolution does not
  clear it.** The corrected part (iii') (§5.5) is therefore a WORKING HYPOTHESIS, not an established
  result — it leans on F8 (=FF3) and F9 (=FF4), both OPEN. F5 is fired and is NOT yet absorbed by a
  settled correction.

**New failure conditions blocking re-upgrade (verdict OPEN):**

| Code | Condition | Status |
|---|---|---|
| F8 (= FF3 of the F5 file) | The dynamical gauge symmetry of the rolled-up Dirac-DeRham complex is generated by exact-form coboundaries d_A(eps), so Gauge_BRST = Im c(xi) as a THEOREM (not a model-verified identity) | OPEN. Asserted in §5.5/§7.3', not proved. Until proved, the gauge-orbit-fill basis of the corrected part (iii') is not established. |
| F9 (= FF4 of the F5 file) | The full rolled-up symbol complex on E (dim 2^14 · 256 = 4,194,304) is Koszul-acyclic off the zero section, dim H(xi) = 0 at every null xi | OPEN. Verified in the model and at reconstruction grade via the irreducible-module argument, NOT by direct computation on full E. Until verified, "physical content lives in transport, pointwise quotient vanishes" is not established. |
| F10 (same-session-resolution gate) | The internal contradiction (parts (ii) vs (iii)) was named AND re-resolved in the SAME session (2026-06-23) | FIRED. Per the loop rule this blocks any verdict above OPEN until an intervening session independently re-derives the gauge content of NM(xi). |
- F6: RULED OUT for non-degenerate g_Y. H_p = 2 xi^A partial_{y^A} + ... is non-zero for
  xi != 0 as long as the null geodesic flow is non-degenerate, which holds for any non-degenerate
  pseudo-Riemannian metric. Confirmed by direct computation in sc1-oq2-ellipticity §4.
- F7: RULED OUT at verified grade. OQ3-V1/V2/V3 in vz-schur-complement §18 verify c_s(eta)^2
  = g_s(eta,eta) Id_s as an exact algebraic identity. The section pullback is a Dirac-type operator.

---

## 9. Result

### 9.1 Verdict: OPEN (downgraded from CONDITIONALLY_RESOLVED, 2026-06-23)

> [!CORRECTION — VERDICT DOWNGRADED TO OPEN] 2026-06-23. CORRECTION
> SC1-LEMMA-CONTRADICTION-SAME-SESSION (critical). Original part (iii) ("null modes partially
> physical / gauge orbit is a proper subspace of NM(xi)") is FALSE — F5 fired (see §8, §5.5, and
> `sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md`). The firing NAMES an internal contradiction (parts
> (ii) vs (iii)). Per the loop's RESOLVED-blocking rule (`lab/process/loop-adversarial-log.md`: an
> explicit internal contradiction is an open problem; block CLOSED/RESOLVED verdicts until it is
> resolved IN A SUBSEQUENT SESSION), a same-session-named contradiction caps the verdict at OPEN —
> same-session self-resolution does NOT clear it. The prior in-file correction (ELLIPTICITY-LEMMA-iii)
> attempted to RETAIN CONDITIONALLY_RESOLVED by re-deriving the symmetric-hyperbolic conclusion
> same-session from the corrected (Koszul-exactness) premise; that re-derivation is itself same-session
> and leans on F8/F9 (= FF3/FF4), both OPEN. The verdict is therefore **OPEN** for the affected claim
> (gauge content of NM(xi); the gauge-mechanism basis of the elliptic→symmetric-hyperbolic switch).
> The corrected part (iii') is the WORKING HYPOTHESIS to re-derive next session, not a settled result.
>
> What is NOT affected and stays as established: the kernel trichotomy (§4, part (ii)) — ker c(xi) =
> {0} off-null, ker c(xi) = NM(xi) (dim E/2) at null xi — which is a direct Clifford-identity fact
> independent of the gauge argument; VZ evasion (off-null invertibility); and the generation count
> ind_H = 24 (Atiyah-Schmid L2-theory, never used a pointwise null-cohomology quotient).

The gate is **NOT yet closed** (verdict OPEN). The gate's DIRECTION (elliptic → symmetric-hyperbolic)
is the most-likely resolution, but the gauge-mechanism that would justify the switch is the affected
OPEN claim and must be re-derived inter-session. [WORKING HYPOTHESIS:] At null xi the gauge orbit FILLS
the null-mode space NM(xi) (ker c(xi) = Im c(xi), Koszul-exactness); the pointwise physical quotient
vanishes; physical content is the admissible Cauchy data carried by transport along null
bicharacteristics. The original claim that "null modes are partially physical and partially gauge, with
the physical subspace carrying SM field content" is FALSE. Its same-session replacement (the working
hypothesis) is NOT yet established because it leans on F8/F9 (= FF3/FF4), both OPEN, and was produced in
the same session that named the contradiction.

**What is established (independent of the gauge argument, verdict-unaffected):**

1. sigma_shiab(xi) = 0 at principal-symbol order (zero-order operator; shiab is purely
   fiberwise, contributing no xi-dependence to the leading symbol).

2. sigma_D(xi) = c(xi) with the complete kernel trichotomy:
   - ker = {0} for spacelike xi (g_Y > 0): D_GU elliptic
   - ker = {0} for timelike xi (g_Y < 0): D_GU elliptic
   - ker = NM(xi) with dim = dim E / 2 for null xi: D_GU NOT elliptic, real principal type

   This is a direct Clifford-identity ([CL1]) consequence and does NOT depend on the gauge analysis;
   it stands.

**What is OPEN (the affected claim, downgraded from CONDITIONALLY_RESOLVED):**

3. [OPEN — WORKING HYPOTHESIS, not established] The pointwise gauge content of NM(xi). The original
   item 3 ("gauge orbit is a proper subspace; a physical subspace survives in the pointwise quotient")
   is FALSE. The replacement reading ("Null modes at null xi are ALL pure gauge at the pointwise symbol
   level: the gauge orbit FILLS NM(xi), ker c(xi) = Im c(xi), Koszul-exactness; pointwise physical
   quotient H(xi) = 0; physical SM DOF carried by Cauchy-data transport") is the CAS-supported working
   hypothesis from `sc1-oq2-f5-gauge-orbit-fill`, but it was produced same-session as the contradiction
   it resolves and leans on F8/F9 (= FF3/FF4), both OPEN. Per the loop rule it cannot be treated as
   settled until an intervening session re-derives it. RE-DERIVE NEXT SESSION.

4. The null-characteristic set is NOT a genuine analytic obstruction. The correct framework
   is symmetric-hyperbolic / real principal type. The Cauchy problem is well-posed with
   explicit energy estimate E_{4D}(t) <= E_{4D}(0) exp(C_V t).

5. [OPEN — WORKING HYPOTHESIS] The structural gate's DIRECTION (the analytic framework most likely
   MUST switch to symmetric-hyperbolic) is the expected outcome, but the firing BASIS is the affected
   OPEN claim: under the working hypothesis the null cone admits NO pointwise elliptic-modulo-gauge
   kernel because the gauge orbit FILLS NM(xi) (Koszul-exactness), not because a physical subspace
   survives in a pointwise quotient. That basis is not yet established (same-session, leans on F8/F9 =
   FF3/FF4). Whether the switch is forced therefore awaits inter-session re-derivation. The trichotomy
   itself (item 2) already shows D_GU is non-elliptic at null xi, independent of the gauge mechanism.
   (Supersedes the original item 5's basis "null modes are NOT purely gauge," which is FALSE.)

**Remaining for re-upgrade above OPEN (CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION):**

- **Inter-session re-derivation of the gauge content of NM(xi)** is the primary gate (F10 fires until
  met): the named (ii)-vs-(iii) contradiction was resolved same-session, which per the loop rule does
  not count until an intervening session re-derives it.
- F8 (= FF3): prove the gauge symmetry of the rolled-up complex is exactly the exact-form coboundary,
  so Gauge_BRST = Im c(xi) as a theorem (not a model-verified identity).
- F9 (= FF4): direct Koszul-acyclicity of the full 14D rolled-up symbol complex, not just the
  irreducible S-factor.
- Explicit RS null-mode dimension count dim(NM(xi) cap ker Gamma^{14D}).
- Formal identification of L2-normalizable fiber null modes with Flensted-Jensen discrete
  series (closing the discrete-series generation count gate).

### 9.2 Explicit failure conditions recap

Conditions and their status [CORRECTED 2026-06-23]:
1. F4 fires (Phi is first-order): ruled out by the explicit Phi formula.
2. F5 (gauge orbit fills NM(xi)): **FIRED** — the orbit DOES fill NM(xi)
   (`sc1-oq2-f5-gauge-orbit-fill`). This falsifies the ORIGINAL part (iii) AND names an internal
   contradiction (parts (ii) vs (iii)). Per CORRECTION SC1-LEMMA-CONTRADICTION-SAME-SESSION and the
   loop's RESOLVED-blocking rule, the firing DOWNGRADES the file verdict to **OPEN** (a
   same-session-named internal contradiction cannot be self-resolved in the same session; F10 fired,
   §8). The symmetric-hyperbolic conclusion is RE-DERIVED from the corrected (Koszul-exactness) premise
   (§5.5, part (iii')), but that re-derivation is itself same-session and leans on FF3/FF4 (both OPEN),
   so it stands as a WORKING HYPOTHESIS pending inter-session re-derivation, not a settled result.
3. F7 fires (section pullback fails Dirac-type): ruled out at verified grade.

F1/F2/F3/F4/F6/F7 are all ruled out, but the verdict is **OPEN** (NOT CONDITIONALLY_RESOLVED): F5
fired and names a same-session internal contradiction (parts (ii) vs (iii)), and F10
(same-session-resolution gate, §8) caps the verdict at OPEN until an intervening session
independently re-derives the gauge content of NM(xi). The residual gates toward RESOLVED are the
inter-session re-derivation (F10), FF3 and FF4 from the F5 file (BRST-coboundary structure and
full-E Koszul-acyclicity as theorems), plus the RS null-mode count and the discrete-series
identification.

### 9.3 Structural implications

The lemma establishes the correct analytic picture for D_GU as a complete package:

  Spacelike xi: elliptic => standard Fredholm / Sobolev theory applies
  Timelike xi:  elliptic => same standard theory applies
  Null xi:      real-principal-type => Hormander propagation applies, physical modes propagate
                along null geodesics of g_Y; these are the SM particles traveling at the speed
                of light in the metric g_s = s*(g_Y)

This trichotomy is the GU analog of the standard dichotomy in physics:

  g(p,p) > 0: massive particle (spacelike momentum, non-propagating in real time)
  g(p,p) < 0: virtual particle (timelike momentum in Euclidean sense, non-propagating)
  g(p,p) = 0: massless particle (null momentum, propagating along light cone)

The GU theory is therefore a massless theory in the 14D sense: all physical propagating degrees
of freedom are null-momentum states in T*Y^14. The massive SM particles emerge from the fiber
structure (KK mechanism: fiber directions contribute mass to the base 4D fields), not from
the 14D principal symbol.

---

## 10. Connection to Prior SC1-OQ2 Files

| File | What it established | This file's relationship |
|---|---|---|
| sc1-oq2-ellipticity-split-signature | Char(D_GU) = null cone; real principal type | Incorporated as proof of T3 and (iv)(b) |
| sc1-oq2b-symmetric-hyperbolic | Energy estimate, Cauchy problem well-posed | Incorporated as proof of (iv)(c) and (iv)(d) |
| sc1-oq2c-null-mode-interpretation | dim NM(xi), Im c(xi) = ker c(xi) (null-projection) | Incorporated as proof of (ii); the null-projection property it derives is exactly what FORCES the gauge-orbit-fill in the corrected part (iii') (the original "gauge/physical split" reading of (iii) is FALSE — see §5.5) |
| This file (sc1-oq2-split-signature-ellipticity-lemma) | Formal lemma integrating all three | Gate-closing formal statement with explicit proofs |

The three SC1-OQ2 sub-files (ellipticity, symmetric-hyperbolic, null-mode-interpretation) are
each CONDITIONALLY_RESOLVED. This lemma file — the formal synthesis and gate closure — is itself
**OPEN** as of 2026-06-23 (downgraded from CONDITIONALLY_RESOLVED; see §9.1 and the frontmatter):
its part (iii) carried a same-session-named internal contradiction (parts (ii) vs (iii), F5/F10
fired), which the loop's RESOLVED-blocking rule requires be resolved in a SUBSEQUENT session before
the verdict can rise above OPEN. The corrected part (iii') (gauge orbit FILLS NM(xi)) is the working
hypothesis; the downstream analytic verdict (symmetric-hyperbolic, not elliptic) is unchanged in
direction but rests on that working hypothesis plus FF3/FF4.

---

## 11. Open Questions Remaining (gate NOT yet closed; verdict OPEN)

**OQ-F5 (Gauge orbit dimension in NM(xi)) — OPEN; same-session CAS result is a working hypothesis,
NOT resolved:** The explicit CAS computation requested was performed in
`sc1-oq2-f5-gauge-orbit-fill-2026-06-23.md` ([c(xi), rho_*(T)] for T in sp(64), plus BRST-exact and
direct-action orbits, at n = 6, 8, generic null xi). Outcome: the orbit FILLS NM(xi) —
Im([c(xi), rho_*(-)]) cap NM(xi) is NOT proper; it equals NM(xi). This fires F5 against the original
part (iii) AND names an internal contradiction (parts (ii) vs (iii)). Per the loop's RESOLVED-blocking
rule, OQ-F5 is therefore **OPEN**, not RESOLVED: the contradiction-naming and its same-session
"resolution" both live in the 2026-06-23 session, so the fill result stands as a working hypothesis to
be re-derived in a SUBSEQUENT session. The successor open gates are FF3 (= F8: prove
Gauge_BRST = Im c(xi) as a theorem) and FF4 (= F9: full-14D-E Koszul-acyclicity), per that file §7,
plus the inter-session re-derivation gate (F10).

**OQ-Discrete-Series (Fiber null modes = discrete series):** The identification of L2-
normalizable fiber null modes with Flensted-Jensen representations of SL(4,R) is stated at
reconstruction grade in sc1-oq2c. Making this identification explicit (as a formal theorem)
would close the loop between the null-mode physical interpretation and the generation count
ind_H = 24.

**OQ-RS-Null-Modes (RS sector null-mode count):** The explicit computation of
dim(NM(xi) cap ker Gamma^{14D}) for a horizontal null xi_H. This count determines how many
of the 128 real null modes are RS (spin-3/2) vs. spin-1/2, connecting to the APS index
computation ind_H(D_RS) = 8 and the K3 selection.
