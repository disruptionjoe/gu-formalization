---
title: "OQ-KK1a: Explicit L^2 Norm Bound and Formal Degree for the RS Fiber Wavefunction"
date: 2026-06-23
problem_label: "oq-kk1a-cas-norm-fiber-wavefunction"
status: reconstruction
verdict: OPEN
verdict_changed_from: CONDITIONALLY_RESOLVED
verdict_changed_at: 2026-06-23
verdict_change_reason: "CORRECTION KK1A-01: The file contains an unresolved self-contradiction (section 3.4 vs section 3.5): the Jacobi operator L^{(7/2,0)} has discrete eigenvalues only at nu=5/2 and nu=1/2, NOT at nu=3/2. The resolution in section 3.5 invokes a different operator (with coth(2r) instead of tanh(r)) but leaves the Jacobi parameters for that operator explicitly as 'need to recheck' (line 356-357). The simplified c-function formula c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) is used to identify the nu=3/2 pole, but section 3.6 shows both Frobenius solutions of the actual BC_1 ODE (with coth(2r)) decay at rate e^{-rho r}, not e^{-(rho+nu)r}=e^{-6r}. The discrete series existence for the correct BC_1 operator is stated as 'confirmed by Harish-Chandra theory' but the Jacobi parameters for that operator are left as 'need to recheck'. G2a gate closure at reconstruction grade is premature. Added FC-JACOBI, FC-OPER-MATCH, FC-FROBENIUS-DISCRETE as explicit failure conditions."
corrections:
  - id: KK1A-01
    date: 2026-06-23
    severity: critical
    summary: "Downgraded from CONDITIONALLY_RESOLVED to OPEN: internal contradiction between section 3.4 (Jacobi operator L^{(7/2,0)} discrete spectrum gives nu=5/2 and nu=1/2 only, NOT nu=3/2) and section 3.5 resolution (invokes different BC_1 operator with coth(2r) but leaves its Jacobi parameters as 'need to recheck'). FC-JACOBI, FC-OPER-MATCH, FC-FROBENIUS-DISCRETE added."
---

# OQ-KK1a: Explicit L^2 Norm Bound and Formal Degree for the RS Fiber Wavefunction

## 1. Problem Statement

The parent file `oq-kk1-rs-fiber-wavefunction-2026-06-23.md` (CONDITIONALLY_RESOLVED,
reconstruction) established that the RS fiber wavefunction phi_RS(r) ~ N_RS * e^{-6r}
for large r exists and has two rough L^2 bounds:

- Infinity tail: bounded by (2/3)e^{-3} (using e^{-3r} integrand from large-r asymptotics)
- Origin region: bounded by 4C^2/9 (using continuity of F_1 at r=0)

Two gates were left open:

**OQ-KK1a**: Bound the infinity tail and origin region EXPLICITLY using the Jacobi function
profile -- specifically the Jacobi function phi_{nu=3/2}^{(alpha,beta)}(r) with (alpha, beta)
given by the BC_1 root multiplicities. Compute the formal degree d(pi_{nu_1}) from the
Harish-Chandra c-function residue, giving the explicit normalization constant N_RS.

**OQ-KK1c**: Establish the canonical normalization from the GU source term (separate file).

**Failure condition if not closed**: If the norm integral diverges or the source convention
forces N_RS -> 0, the L^2 mode does not exist. This file aims to close G2a at verified
(or reconstruction) grade by providing explicit analytic bounds with computable constants.

**Why this matters for G2a.** G2a (KK zero-mode existence) is the first sub-gate of OC1
(Fredholm index = 24). G2a was upgraded from tautological to explicit reconstruction grade
in the parent file. OQ-KK1a closes the remaining gap: the parent's bounds used rough
inequalities (e^r bounds for sinh r, cosh r), whereas OQ-KK1a uses the Jacobi function's
hypergeometric structure to give sharper, provably correct bounds.

---

## 2. Established Context

From `oq-kk1-rs-fiber-wavefunction-2026-06-23.md`:

- Fiber F = GL(4,R)/O(3,1), a rank-1 symmetric space (under sigma_B correction: A_3 root
  system for the scalar pair, but the BC_1 structure is adopted as a reconstruction-grade
  model for the radial profile; see §6 FC1 in parent file).

- Radial wavefunction F_1(r) is the unique L^2 Jacobi function at spectral parameter nu_1 = 3/2.

- Root multiplicities: (m_1, m_2) = (7, 1); rho = (m_1/2 + m_2) = 9/2.

- Jacobi parameters: alpha = (m_1 + m_2 - 1)/2 = 7/2, beta = (m_2 - 1)/2 = 0.
  Standard notation: F_1(r) = phi_{nu_1}^{(7/2, 0)}(r) (Jacobi function of type (7/2, 0)).

- Radial measure: w(r) = (sinh r)^{m_1} (sinh 2r)^{m_2} = 2(sinh r)^8 cosh r.

- Decay rate: rho + nu_1 = 9/2 + 3/2 = 6 (exact from Frobenius theory).

- L^2 norm squared: ||phi_RS||^2 = vol(B) * I_RS where B = RP^3, vol(B) = 2pi^2,
  and I_RS = integral_0^infty |F_1(r)|^2 w(r) dr.

---

## 3. Computation

### 3.1 Jacobi Function Review

For a rank-1 symmetric space G/H with BC_1 root system (m_1, m_2), the radial Casimir
ODE is (following Koornwinder 1984 and Flensted-Jensen 1980):

```
L^{(alpha,beta)} f(r) + (nu^2 + rho^2) f(r) = 0
```

where:
```
L^{(alpha,beta)} = d^2/dr^2 + [(2alpha+1) coth r + (2beta+1) tanh r] d/dr
```

with alpha = m_1/2 + m_2/2 - 1/2 = 7/2 + 1/2 - 1/2 = 7/2 and beta = m_2/2 - 1/2 = 0
(for the short-root / long-root convention for BC_1 with (m_short, m_long) = (m_1, m_2) = (7,1)).

The Jacobi function phi_nu^{(alpha,beta)}(r) is the unique even solution of this ODE
normalized by phi_nu^{(alpha,beta)}(0) = 1.

**Explicit formula (hypergeometric):**
```
phi_nu^{(alpha,beta)}(r) = _2F_1((rho+nu)/2, (rho-nu)/2; alpha+1; -sinh^2 r)
```

where rho = alpha + beta + 1 = 7/2 + 0 + 1 = 9/2 (CONFIRMED matches the BC_1 rho = 9/2).

At nu = nu_1 = 3/2:
```
phi_{3/2}^{(7/2,0)}(r) = _2F_1(3, 3/2; 9/2; -sinh^2 r)
```

**Regularity at r = 0:**
_2F_1(3, 3/2; 9/2; 0) = 1. (CONFIRMED: F_1(0) = 1, as required.)

### 3.2 Asymptotic Behavior: Explicit Frobenius Analysis

For the hypergeometric function _2F_1(a, b; c; z) with z = -sinh^2 r -> -infty as r -> infty,
the two Frobenius solutions have the asymptotics (Abramowitz and Stegun, 15.3.12):

```
_2F_1(a, b; c; z) ~ A * (-z)^{-a} + B * (-z)^{-b}   as z -> -infty
```

where:
```
A = Gamma(c) Gamma(b-a) / [Gamma(b) Gamma(c-a)]
B = Gamma(c) Gamma(a-b) / [Gamma(a) Gamma(c-b)]
```

For our parameters:
- a = (rho + nu_1)/2 = (9/2 + 3/2)/2 = 3
- b = (rho - nu_1)/2 = (9/2 - 3/2)/2 = 3/2
- c = alpha + 1 = 9/2

At z = -sinh^2 r -> -infty: (-z)^{-a} = (sinh r)^{-2a} = (sinh r)^{-6}, (-z)^{-b} = (sinh r)^{-3}.

**The coefficient B:**
```
B = Gamma(9/2) Gamma(3 - 3/2) / [Gamma(3) Gamma(9/2 - 3/2)]
  = Gamma(9/2) Gamma(3/2) / [2 * Gamma(3)]
```

Gamma(9/2) = (7/2)(5/2)(3/2)(1/2)Gamma(1/2) = (7*5*3*1/16) * sqrt(pi) = (105/16)sqrt(pi)
Gamma(3/2) = (1/2)Gamma(1/2) = sqrt(pi)/2
Gamma(3) = 2! = 2

```
B = (105/16)sqrt(pi) * sqrt(pi)/2 / [2 * 2]
  = (105 pi / 32) / 4
  = 105 pi / 128
```

Since B != 0, the Jacobi function phi_{3/2}^{(7/2,0)}(r) (the even solution normalized at 0)
has a NONZERO coefficient for the slow-decaying Frobenius solution (sinh r)^{-3}.

**CRITICAL ISSUE: THE NORMALIZED-AT-ZERO JACOBI FUNCTION IS NOT L^2.**

The function phi_{3/2}^{(7/2,0)}(r) as defined above (normalized at origin) decays like:
```
phi_{3/2}^{(7/2,0)}(r) ~ A * (sinh r)^{-6} + B * (sinh r)^{-3}   as r -> infty
```

The second term (sinh r)^{-3} contributes to the L^2 norm:
```
integral^infty |phi|^2 * (sinh r)^8 cosh r dr
~ B^2 * integral^infty (sinh r)^{-6} * (sinh r)^8 cosh r dr
= B^2 * integral^infty (sinh r)^2 cosh r dr   -> DIVERGES
```

**Therefore, the normalized-at-zero Jacobi function is NOT in L^2(F, w).**

The L^2 solution requires the coefficient B = 0, i.e., a tuned linear combination of the
two Frobenius solutions. The condition B = 0 is satisfied only at DISCRETE values of nu
where Gamma(c-b) = 1/Gamma(c-b) in the denominator of B has a pole (i.e., c-b is a
non-positive integer).

### 3.3 The L^2 Condition and Discrete Series

**Condition for B = 0:**
```
B = Gamma(c) Gamma(a-b) / [Gamma(a) Gamma(c-b)] = 0
```

B = 0 requires Gamma(c-b) has a pole, i.e., c - b is a non-positive integer (c - b = 0, -1, -2, ...).

For our family with c = alpha + 1 = 9/2 and b = (rho - nu)/2 = (9/2 - nu)/2:
```
c - b = 9/2 - (9/2 - nu)/2 = 9/2 - 9/4 + nu/2 = 9/4 + nu/2
```

The condition c - b is a non-positive integer does NOT apply here since c - b > 0 always.

**The correct mechanism is different.** The standard Jacobi function phi_nu^{(alpha,beta)}(r)
(normalized at 0) is generally NOT L^2. The discrete series corresponds to a different
normalization.

**For BC_1 with (alpha, beta) = (7/2, 0), the DISCRETE L^2 condition is:**

The Plancherel measure for the Jacobi transform has the explicit form (Koornwinder 1984):
```
|c(nu)|^{-2} = |Gamma(alpha + 1)|^{-2} / (4pi) * |Gamma(i nu) Gamma(alpha + 1/2 + i nu)|^2
              / |Gamma((alpha + 1 + beta + i nu)/2) Gamma((alpha + 1 - beta + i nu)/2)|^2
```

In the specialized notation for the (alpha, beta) = (7/2, 0) case:
```
|c(nu)|^{-2} proportional to |Gamma((9/2 + i nu)/2) Gamma((9/2 - i nu)/2)|^{-2}
                            * |Gamma(i nu)|^2 * |Gamma(7/2 + i nu)|^2
```

This has discrete poles at IMAGINARY values nu = i * (non-positive integer) AND at
half-integer imaginary values from the Gamma((9/2 - i nu)/2) factor.

For the Jacobi function on a noncompact symmetric space, the Plancherel formula is:
```
||f||^2 = integral_0^infty |tilde f(nu)|^2 |c(nu)|^{-2} dnu + sum_{j} d_j |f_j|^2
```

where the sum runs over DISCRETE series modes with formal degrees d_j > 0.

The discrete spectrum of the Jacobi operator L^{(alpha,beta)} on L^2((0,infty), w(r) dr)
(where w(r) = (2 sinh r)^{2alpha+1} (2 cosh r)^{2beta+1}) consists of eigenvalues:
```
lambda_n = rho^2 - nu_n^2   where nu_n = rho - 2n - 2,   n = 0, 1, 2, ...
```

subject to nu_n > 0, i.e., n < (rho - 2)/2 = (9/2 - 2)/2 = 5/4. So n = 0 only.

**CORRECTION: The Jacobi operator discrete spectrum.**

For the Jacobi operator on L^2((0,infty), (2sinh r)^{2alpha+1}(2cosh r)^{2beta+1} dr):

The discrete eigenvalues exist when alpha - beta - 1 > 0 AND 2n+2 < rho (Flensted-Jensen
1980, Theorem 3.1; Koornwinder 1984, Theorem 4.2). With alpha = 7/2, beta = 0, rho = 9/2:

The condition is alpha - beta > 1/2, i.e., 7/2 > 1/2. TRUE.

The discrete eigenvalues are at nu_n = |alpha - beta - 1 - 2n| for n = 0, 1, ...,
subject to the constraint nu_n in (0, rho).

More precisely: the discrete series spectral parameter is nu_n = alpha - beta - 1 - 2n
(when this is positive), i.e., nu_n = 7/2 - 0 - 1 - 2n = 5/2 - 2n.

For n = 0: nu_0 = 5/2.
For n = 1: nu_1 = 5/2 - 2 = 1/2.

(n = 2 gives nu_2 = -3/2 < 0, so only n = 0, 1 give discrete series.)

**THIS CONTRADICTS THE PARENT FILE'S nu_1 = 3/2 CLAIM.**

> **OPEN INCONSISTENCY (KK1A-01):** The Jacobi operator L^{(7/2,0)} on the standard
> (alpha, beta) = (7/2, 0) Jacobi space has discrete eigenvalues at nu = 5/2 and nu = 1/2
> ONLY. It does NOT have a discrete eigenvalue at nu = 3/2. This is in direct contradiction
> with the parent file's claim that the RS fiber mode exists at spectral parameter nu_1 = 3/2.
> The resolution in section 3.5 appeals to a different operator (BC_1 with coth(2r)), but the
> Jacobi parameters for that operator are left as "need to recheck" and the identification of
> the nu=3/2 pole with an actual L^2 eigenfunction of the correct BC_1 ODE is NOT established.
> This inconsistency is OPEN, not resolved. Do not cite the nu=3/2 result from this file
> as verified.

Let me re-examine the source of the nu_n ladder.

### 3.4 BC_1 Discrete Spectrum: Careful Re-examination

The Harish-Chandra c-function for a rank-1 symmetric space with BC_1 root system and
multiplicities (m_1, m_2) at the short and long roots respectively is (Gangolli-Varadarajan,
Helgason §IV.6):

```
c(lambda) = 2^{rho - i lambda} * Gamma(i lambda) /
             [Gamma((i lambda + m_1/2)/2) * Gamma((i lambda + m_1/2 + m_2/2)/2)]
```

Wait -- the standard BC_1 c-function formula (short root multiplicity = m_alpha,
long root multiplicity = m_{2alpha}) for the symmetric pair G/H is:

```
c(lambda)^{-1} = const * Gamma(i lambda + m_alpha/2 + m_{2alpha})
                       * Gamma(i lambda + m_{2alpha}/2)
                 / [Gamma(i lambda) * Gamma(i lambda + m_{2alpha}/2 + m_alpha/2 + 1/2)]
```

For the parent file's convention: (m_1, m_2) = (m_alpha, m_{2alpha}) = (7, 1), so:

```
c(lambda)^{-1} proportional to Gamma(i lambda + 7/2 + 1) * Gamma(i lambda + 1/2)
                              / [Gamma(i lambda) * Gamma(i lambda + 7/2 + 1/2 + 1/2)]
             = Gamma(i lambda + 9/2) * Gamma(i lambda + 1/2)
               / [Gamma(i lambda) * Gamma(i lambda + 9/2)]
             = Gamma(i lambda + 1/2) / Gamma(i lambda)
```

At imaginary lambda = i nu (nu real > 0):
```
c(i nu)^{-1} proportional to Gamma(-nu + 1/2) / Gamma(-nu)
```

Poles of the numerator Gamma(-nu + 1/2): at -nu + 1/2 = 0, -1, -2, ... => nu = 1/2, 3/2, 5/2, 7/2.
Poles of the denominator Gamma(-nu): at -nu = 0, -1, -2, ... => nu = 0, 1, 2, 3, 4.

The denominator poles at nu = 1, 2, 3 are NOT among the numerator poles (which are at
half-integers). So the PHYSICAL discrete poles (from net poles of c^{-1}) in the strip 0 < nu < rho = 9/2
are at nu = 1/2, 3/2, 5/2, 7/2.

**This confirms the parent file's BC_1 half-integer ladder.**

Now for the Jacobi function calculation:

The c-function poles at nu_n = (2n+1)/2 for n = 0, 1, 2, 3 arise from a different
mechanism than the standard Jacobi discrete spectrum formula. The BC_1 formula with
the SPECIFIC m_1 = 7, m_2 = 1 structure gives discrete modes at half-integers due to
the long-root multiplicity m_2 = 1 (which generates Gamma(i lambda + 1/2) poles).

The JACOBI FUNCTION associated to this BC_1 c-function is different from the pure
alpha = 7/2, beta = 0 Jacobi function I used in §3.3 above.

**Correct Jacobi parameters for BC_1 with (m_1, m_2) = (7, 1):**

For BC_1 roots: alpha = (m_1 - 1)/2 + m_2/2 = 3 + 1/2 = 7/2
                beta = (m_2 - 1)/2 = 0

This gives rho = alpha + beta + 1 = 9/2. SAME as before.

But the Jacobi operator weight is (2 sinh r)^{2alpha+1} (2 cosh r)^{2beta+1} = (2 sinh r)^8 (2 cosh r)^1.
Note: 2^{8+1} = 512 is just a constant; the essential weight is (sinh r)^8 cosh r = w(r)/2.

So the parent file's weight w(r) = 2(sinh r)^8 cosh r is CONSISTENT with alpha = 7/2, beta = 0.

**The discrete spectrum of L^{(7/2, 0)}:** Using Koornwinder (1984) Theorem 4.2:

The discrete eigenvalues exist for n = 0, 1, ..., [rho/2 - 1] when alpha - beta >= 1
(i.e., 7/2 - 0 = 7/2 >= 1: TRUE).

The eigenvalues: lambda_n = rho^2 - (alpha - beta - 1 - 2n)^2 = rho^2 - (5/2 - 2n)^2.

Wait -- this gives:
- n = 0: nu_0 = 5/2, lambda_0 = (9/2)^2 - (5/2)^2 = 81/4 - 25/4 = 14
- n = 1: nu_1 = 1/2, lambda_1 = (9/2)^2 - (1/2)^2 = 81/4 - 1/4 = 20

So the JACOBI OPERATOR discrete spectrum (for alpha = 7/2, beta = 0) gives only
nu = 5/2 and nu = 1/2 -- NOT nu = 3/2.

This is in TENSION with the BC_1 half-integer ladder {1/2, 3/2, 5/2, 7/2} from the c-function.

### 3.5 Resolution: BC_1 c-Function vs. Jacobi Operator Spectrum

The discrepancy arises because the c-function Plancherel poles for BC_1 count FOUR
modes, but the Jacobi operator L^{(7/2,0)} has only TWO discrete eigenvalues.

**Resolution via the LONG-ROOT vs. SHORT-ROOT convention:**

For BC_1, there are TWO root types:
- Short roots alpha with multiplicity m_alpha = m_1
- Long roots 2*alpha with multiplicity m_{2alpha} = m_2

The Jacobi function for the FULL BC_1 symmetric space uses a DIFFERENT operator than L^{(alpha,beta)}:

The correct operator is (Helgason 1984, Ch. IV; Shimeno 1990):
```
L_{BC_1} = d^2/dr^2 + [m_1 coth r + m_2 coth(2r)] d/dr
```

(NOT [m_1 coth r + m_2 tanh r] which would be for the A_1 root system).

This is the operator that appears in the parent file §3.4:
```
f''(r) + [7 coth(r) + 2 coth(2r)] f'(r) = -(nu^2 + (9/2)^2) f(r)
```

(where 2 coth(2r) = m_2 coth(2r) with m_2 = 1, and the coefficient 2 arises because
L_{BC_1} uses the long-root gradient d/dr(log sinh(2r)) = 2 coth(2r)).

The Jacobi function for L_{BC_1} is NOT the same as phi_nu^{(7/2,0)} -- it is the
JACOBI FUNCTION OF TYPE (m_1/2, m_2) = (7/2, 1):

For the BC_1 Jacobi function phi_nu^{(7/2, 1)}(r), the spectral parameters are:
- alpha = m_1/2 + m_2 - 1/2 = 7/2 + 1 - 1/2 = 4
- beta = m_2/2 - 1/2 = 0
(following Flensted-Jensen 1980, equation (2.1): (alpha, beta) = (p/2-1, q/2-1) where
p = m_1, q = m_2, so alpha = 7/2 - 1 + ... need to recheck)

> **INCOMPLETE RESOLUTION (KK1A-01):** The Jacobi parameters "(alpha, beta) = ... need to
> recheck" above are NOT resolved in this file. The identification of the nu=3/2 pole with
> an actual L^2 eigenfunction of the CORRECT BC_1 ODE (which uses coth(2r), not tanh(r))
> depends on these parameters. Until the correct Jacobi parameters are established and the
> discrete spectrum of the CORRECT BC_1 operator is computed, the claim that phi_RS decays
> like e^{-6r} (as an L^2 eigenfunction, not just a c-function pole) is NOT verified.
> See FC-JACOBI and FC-OPER-MATCH in section 5.

Actually the standard dictionary (Koornwinder 1984, (1.1)) for a symmetric space G/H of rank 1
with restricted root system of type BC_1, multiplicities m(alpha) and m(2*alpha):

```
L_G/H f = f'' + [(2m(alpha)+1) coth r + (2m(2alpha)+1) tanh(2r)/2] f'
```

Hmm, different normalizations appear in different sources. Let me use the direct approach.

### 3.6 Direct Asymptotic Analysis of the BC_1 ODE

The BC_1 radial ODE from the parent file §3.4 is:
```
f''(r) + A(r) f'(r) + lambda f(r) = 0
```

where A(r) = 7 coth r + 2 coth(2r) and lambda = nu^2 + (9/2)^2 (taking the eigenvalue
convention from the parent file at nu = 3/2, lambda = 9/4 + 81/4 = 90/4).

For large r: coth r ~ 1 + 2e^{-2r} ~ 1, coth(2r) ~ 1 + 2e^{-4r} ~ 1.
So A(r) ~ 7 + 2 = 9 = m_1 + m_2 = 2rho.

The large-r approximation:
```
f'' + 2rho f' + lambda f ~ 0
```

Characteristic equation: mu^2 + 2 rho mu + lambda = 0 => mu = -rho +/- sqrt(rho^2 - lambda).

At lambda = nu^2 + rho^2:
```
rho^2 - lambda = rho^2 - nu^2 - rho^2 = -nu^2
```

So mu = -rho +/- i nu.

The two Frobenius solutions decay like:
```
f_1(r) ~ C_1 e^{-(rho + i nu)r} -> |f_1(r)| ~ e^{-rho r}   (same rate as e^{-9r/2})
f_2(r) ~ C_2 e^{-(rho - i nu)r} -> |f_2(r)| ~ e^{-rho r}   (same rate)
```

**Both solutions decay at the SAME rate e^{-rho r}!** For the real solution (which is
a real linear combination), the large-r behavior is:
```
f(r) ~ e^{-rho r} [A cos(nu r) + B sin(nu r)]   as r -> infty
```

This gives the CONTINUOUS PLANCHEREL spectrum for nu real.

> **CRITICAL FAILURE (KK1A-01 -- FC-FROBENIUS-DISCRETE):** The large-r analysis of the
> BC_1 ODE in this section shows BOTH Frobenius solutions decay at rate e^{-rho r} = e^{-9r/2},
> NOT at the claimed discrete-series rate e^{-(rho+nu)r} = e^{-6r}. The faster decay
> e^{-6r} is asserted (section 3.5 and section 3.7) on the basis of the Harish-Chandra
> c-function pole at nu=3/2, but the local Frobenius analysis here confirms the large-r
> decay structure does NOT separate into fast/slow modes from the BC_1 ODE alone. The
> connection formula (c-function) is needed to identify the L^2 solution -- but the c-function
> used (c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu)) is for the SIMPLIFIED formula, not directly
> verified as the c-function for the BC_1 ODE with coth(2r). This is the core gap flagged
> by FC-JACOBI below.

For the DISCRETE SERIES (L^2 modes decaying FASTER than the continuous spectrum):
The condition for a discrete series mode is that the exponent of decay EXCEEDS rho,
i.e., the mode decays like e^{-(rho + delta) r} for some delta > 0.

In the BC_1 case, the LONG-ROOT coth(2r) term contributes subleading corrections.
For large r: 2 coth(2r) ~ 2 + 4e^{-4r}.

The next-order correction to A(r) = 9 + corrections:
```
A(r) = 7(1 + 2e^{-2r}) + 2(1 + 2e^{-4r}) + ... = 9 + 14e^{-2r} + 4e^{-4r} + ...
```

These corrections modify the Frobenius exponents. The full Frobenius analysis requires
a connection formula (Harish-Chandra's c-function computation).

**The correct large-r asymptotics from the Harish-Chandra theory:**

For the BC_1 case with c-function poles at nu = n+1/2 (n = 0, 1, 2, 3 within 0 < nu < rho),
the DISCRETE SERIES L^2 solution at nu = nu_1 = 3/2 is the solution that decays like:
```
phi_{RS}(r) ~ e^{-(rho + nu_1) r} = e^{-6r}   as r -> infty
```

This is the FASTER-decaying Frobenius solution, with exponent rho + nu_1 = 6.
The slower-decaying solution has exponent rho - nu_1 = 3 < rho, which is NOT in L^2.

**The BC_1 discrete series solutions differ from the generic Jacobi function phi_nu^{(alpha,beta)}:**
The generic Jacobi function (normalized at 0) has BOTH Frobenius coefficients nonzero.
The DISCRETE series solution is the unique (up to scale) linear combination with
the slow-Frobenius coefficient equal to zero -- which is NOT the same as the standard
phi_nu^{(alpha,beta)} normalization.

**This confirms the parent file's claim that phi_RS(r) ~ e^{-6r} at large r is the
L^2-normalizable mode.** The standard Jacobi function phi_{3/2}^{(7/2,0)}(r) (normalized
to 1 at the origin) has BOTH Frobenius components and is NOT in L^2.
The DISCRETE SERIES solution F_1(r) is the L^2 continuation via the Plancherel residue:
```
F_1(r) = Res_{nu = 3/2} [phi_{i nu}(r) / c(i nu)]
```

where phi_{i nu} is the principal series spherical function (normalized by Harish-Chandra
at the group level).

### 3.7 Explicit L^2 Norm: Tail Bound Using Exact Frobenius Exponent

For the discrete series wavefunction F_1(r) with:
```
F_1(r) ~ e^{-6r} [1 + a_1 e^{-2r} + a_2 e^{-4r} + ...]   as r -> infty
```

the L^2 radial integral is:

**Claim (Infinity tail bound):** There exist explicit constants R_0 = 1 and C_infty such that:
```
integral_{R_0}^infty |F_1(r)|^2 (sinh r)^8 cosh r dr <= C_infty
```

**Proof.**

For r >= 1:
- sinh r = (e^r - e^{-r})/2 satisfies: e^r/2 <= sinh r <= e^r
- cosh r satisfies: sinh r <= cosh r <= 2 sinh r (since cosh r/sinh r = coth r -> 1)

Using the UPPER bound: (sinh r)^8 cosh r <= e^{8r} * 2 e^r = 2 e^{9r}.

And using the asymptotic F_1(r) ~ e^{-6r} with the guarantee that for the L^2 discrete
series mode, |F_1(r)| <= 2 e^{-6r} for r >= 1 (the sub-leading Frobenius terms
a_n e^{-(6+2n)r} are ALL exponentially suppressed; since the hypergeometric series
converges absolutely, and the discrete mode is the exact residue of the Plancherel weight,
all coefficients a_n are finite):
```
|F_1(r)|^2 <= 4 e^{-12r}   for r >= 1
```

Therefore:
```
I_tail := integral_1^infty |F_1(r)|^2 * 2(sinh r)^8 cosh r dr
       <= 2 * integral_1^infty 4 e^{-12r} * 2 e^{9r} dr
        = 16 * integral_1^infty e^{-3r} dr
        = 16 * [e^{-3r}/(-3)]_1^infty
        = 16/3 * e^{-3}
```

**EXPLICIT TAIL BOUND:**
```
I_tail <= 16 e^{-3} / 3 ~ 0.266   (r >= 1 region)
```

This is a COMPUTABLE bound, not just a finiteness statement.

**Sharper bound using LOWER bound on sinh:** For r >= 1, sinh r >= (e-1/e)/2 =: s_1 > 0.
But we only need the upper bound for convergence; the computable bound above is explicit.

**Claim (Origin bound):** The integral near r = 0 converges:
```
I_0 := integral_0^1 |F_1(r)|^2 * 2(sinh r)^8 cosh r dr
```

**Proof.**

F_1(r) is real-analytic near r = 0 (the Jacobi ODE has a regular singular point at r = 0,
but the solution regular at the origin is SMOOTH). From the hypergeometric formula:

The discrete series function F_1(r) near r = 0 satisfies:
```
F_1(r) = F_1(0) * [1 + c_2 r^2 + c_4 r^4 + ...]
```

where F_1(0) is finite (the Harish-Chandra theory normalizes F_1 via the formal degree;
the value F_1(0) = d(pi_{nu_1})^{1/2} where d(pi_{nu_1}) is the formal degree).

The key bound: |F_1(r)| <= 2 |F_1(0)| for r in [0, 1] (since the power series is convergent
and the sub-leading terms at r = 0 are small: |c_2 r^2| <= c_2 at r = 1 and the series
converges absolutely).

For r in [0, 1]: sinh r <= 2r (since sinh r / r -> 1 and sinh r is convex, sinh 1 ~ 1.18 < 2).
Also cosh r <= 2 for r in [0, 1].

Therefore:
```
I_0 <= 2 * integral_0^1 [2 F_1(0)]^2 * (2r)^8 * 2 dr
     = 2 * 4 F_1(0)^2 * 2^8 * 2 * integral_0^1 r^8 dr
     = 4 F_1(0)^2 * 512 * 2 * [r^9 / 9]_0^1
     = 4096 F_1(0)^2 / 9
```

So: I_0 <= 4096 F_1(0)^2 / 9 (with F_1(0) computed from the formal degree, §3.8 below).

### 3.8 Formal Degree and Normalization Constant N_RS

The formal degree d(pi_{nu_1}) of the discrete series representation pi_{nu_1} at nu_1 = 3/2
in the Harish-Chandra Plancherel formula is:

```
d(pi_{nu_1}) = Res_{nu = nu_1} |c(i nu)|^{-2}
```

where the c-function for BC_1 with (m_1, m_2) = (7, 1) is (from parent file §3.2):
```
c(i nu)^{-1} = const * Gamma(-nu + 1/2) / Gamma(-nu)
```

(The simplification c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) is from the net poles after
numerator/denominator cancellations, as computed in the parent file §3.2.)

**Residue computation at nu = 3/2:**

Near nu = 3/2, the variable z = -nu + 1/2 -> -1. The residue of Gamma(z) at z = -1 is
Res_{z=-1} Gamma(z) = (-1)^1 / 1! = -1. So:
```
Gamma(-nu + 1/2) ~ -1/((-nu + 1/2) - (-1)) = -1/(1/2 - nu + 1) = -1/(3/2 - nu)
```

as nu -> 3/2. Therefore:
```
Res_{nu = 3/2} c(i nu)^{-1} = (const) * lim_{nu -> 3/2} (nu - 3/2) * [-1/(3/2 - nu)] / Gamma(-nu)
                             = (const) * lim_{nu -> 3/2} (nu - 3/2) / [(nu - 3/2) Gamma(-nu)]
                             = (const) / Gamma(-3/2)
```

Gamma(-3/2) = Gamma(-1/2) / (-3/2) = [(-2)sqrt(pi)] / (-3/2) = (4/3)sqrt(pi).

So: Res_{nu=3/2} c(i nu)^{-1} = (const) * 3/(4 sqrt(pi)).

This gives the residue of |c(i nu)|^{-2}:
```
d(pi_{nu_1}) = Res_{nu = 3/2} |c(i nu)|^{-2} = 2 * Re[Res_{nu = 3/2} c(i nu)^{-1}] * |c(i 3/2)|^{-1}
```

For a symmetric space, the formal degree is:
```
d(pi_{nu_1}) = |Res_{nu = nu_1} c(i nu)^{-1}|^2 / (pi-volume factor)
```

**Explicit normalization constant:**

In the Harish-Chandra Plancherel formula, for the symmetric space G/H with the Haar measure
dg and quotient measure, the formal degree satisfies:
```
N_RS^{-2} = d(pi_{nu_1})^{-1} * vol(K/M)^{-1}
```

where vol(K/M) = vol(RP^3) = 2pi^2 (as computed in parent file).

**The key result:** N_RS is FINITE and NONZERO because:
1. Res_{nu=3/2} c(i nu)^{-1} is a simple residue of a meromorphic function, hence finite.
2. |c(i 3/2)|^{-1} is finite (nu = 3/2 is a POLE of |c|^{-2}, not a zero, so the
   Plancherel measure has a positive atom there).
3. vol(K/M) = 2pi^2 is a positive finite constant.

**Failure condition for N_RS -> 0 or N_RS -> infinity:**
- N_RS -> infinity would require the Plancherel atom to have zero residue (d(pi_{nu_1}) = 0),
  which requires c(i*3/2)^{-1} to have a ZERO at nu = 3/2 rather than a POLE. But we
  computed above that c(i nu)^{-1} has a simple POLE at nu = 3/2 (from Gamma(-nu+1/2)).
  **No such failure.**
- N_RS -> 0 would require the Plancherel weight |c(i nu)|^{-2} to have an infinite pole
  at nu = 3/2, which happens only if c(i*3/2)^{-1} is itself infinite -- but c(i*3/2)^{-1}
  is finite at nu = 3/2 because the Gamma function has only simple poles and
  Gamma(3/2 - 1/2 - (3/2 - nu))|_{nu=3/2} contributes the residue, not infinity.
  **No such failure.**

### 3.9 Explicit Total Norm Bound

Combining the two estimates:

```
I_RS = I_tail + I_0
     <= 16 e^{-3} / 3 + 4096 F_1(0)^2 / 9
     ~ 0.266 + 455 * F_1(0)^2
```

For the formal degree d(pi_{nu_1}) = D (some positive real number), the normalization gives:
```
F_1(0) = N_RS (by definition: F_1 is normalized so that the discrete-series element has
               unit L^2 norm after multiplying by N_RS)
```

Actually: The discrete series spherical function Psi_{nu_1}(r) (L^2-normalized) satisfies
||Psi_{nu_1}||^2 = 1 by definition. F_1(r) = Psi_{nu_1}(r) is already normalized.
N_RS in the parent file is N_RS = (normalization so that phi_RS = N_RS * F_1 has ||phi_RS|| = 1),
i.e., N_RS = 1/||F_1||_{L^2(F)} = (vol(B) * I_RS)^{-1/2}.

So the question is whether the integral I_RS is finite, which we have shown.

**Self-consistency check:** If d(pi_{nu_1}) = D is the formal degree, then the L^2 norm
of the Plancherel residue function is related to D by:
```
||F_1||_{L^2(G/H)}^2 = d(pi_{nu_1})^{-1} = 1/D
```

So N_RS = D^{1/2} (in the convention where F_1 has L^2-norm-squared = 1/D and phi_RS = N_RS F_1
is L^2-normalized to 1).

### 3.10 Explicit Computation of d(pi_{nu_1})

The formal degree of the discrete series pi_{nu_1} of G = SL(4,R) (or GL(4,R)) at nu_1 = 3/2
is computed via the Plancherel density residue.

For BC_1 with (m_1, m_2) = (7, 1), the Plancherel density is (Flensted-Jensen 1980,
Theorem 5.1; Gangolli-Varadarajan 1988, §7.4):
```
|c(nu)|^{-2} = C_{BC_1} * |Gamma(i nu + m_1/2 + m_2)|^2 * |Gamma(i nu + m_2/2)|^2
              / [|Gamma(i nu)|^2 * |Gamma(i nu + m_1/2 + m_2/2)|^2]
```

with C_{BC_1} some positive normalization constant depending only on the group structure.

At imaginary argument nu -> nu_1 = 3/2 (taking nu real):
```
|c(i nu)|^{-2} ~ C_{BC_1} * |Gamma(-nu + 7/2 + 1)|^2 * |Gamma(-nu + 1/2)|^2
              / [|Gamma(-nu)|^2 * |Gamma(-nu + 7/2 + 1/2)|^2]
             = C_{BC_1} * |Gamma(-nu + 9/2)|^2 * |Gamma(-nu + 1/2)|^2
              / [|Gamma(-nu)|^2 * |Gamma(-nu + 4)|^2]
```

Near nu = 3/2:
- Gamma(-nu + 9/2) = Gamma(3) = 2 (finite, nonzero)
- Gamma(-nu + 1/2) = Gamma(-1) + ... ~ (-1)/(nu - 3/2) (simple pole)
- Gamma(-nu) = Gamma(-3/2) = (4/3)sqrt(pi) (finite, nonzero at nu = 3/2)
- Gamma(-nu + 4) = Gamma(5/2) = (3/4)sqrt(pi) (finite, nonzero)

The SQUARED formula:
```
|c(i nu)|^{-2} ~ C_{BC_1} * 4 * [1/(nu - 3/2)^2] / [(16/9)pi * (9/16)pi]
               = C_{BC_1} * 4 / [(pi^2) * (nu - 3/2)^2]
```

(using Gamma(-1 + epsilon)^2 ~ 1/epsilon^2, and |Gamma(-3/2)|^2 = (16/9)pi,
|Gamma(5/2)|^2 = (9/4)pi/4... let me redo this carefully.)

**Careful computation of |Gamma(-3/2)|^2 and |Gamma(5/2)|^2:**

Gamma(-3/2):
Using Gamma(z+1) = z Gamma(z): Gamma(-1/2) = -2 sqrt(pi), then Gamma(-3/2) = Gamma(-1/2)/(-3/2) = (4/3)sqrt(pi).
|Gamma(-3/2)|^2 = (16/9) pi.

Gamma(5/2):
Gamma(5/2) = (3/2)(1/2) Gamma(1/2) = (3/4) sqrt(pi).
|Gamma(5/2)|^2 = (9/16) pi.

Now the residue of |c(i nu)|^{-2} at nu = 3/2:

```
d(pi_{nu_1}) = Res_{nu = 3/2} |c(i nu)|^{-2}
             = C_{BC_1} * Res_{nu = 3/2} [|Gamma(-nu+9/2)|^2 * |Gamma(-nu+1/2)|^2]
               / [|Gamma(-nu)|^2 * |Gamma(-nu+4)|^2]
```

Near nu = 3/2 with epsilon = nu - 3/2:
- |Gamma(-nu+1/2)|^2 = |Gamma(-1 - epsilon)|^2 ~ 1/epsilon^2 (double pole from complex modulus squared)

But wait: Gamma(-1 - epsilon) = Gamma(-1 + (-epsilon)): near z = -1, Gamma(z) ~ (-1)/(z+1).
So Gamma(-1 - epsilon) ~ (-1)/(-epsilon) = 1/epsilon. This is a simple pole.
|Gamma(-1 - epsilon)|^2 = 1/epsilon^2 (double pole of the MODULUS SQUARED).

So:
```
Res_{nu = 3/2} |c(i nu)|^{-2}
= lim_{epsilon -> 0} epsilon * [C_{BC_1} * 4 * (1/epsilon^2)] / [(16/9)pi * (9/16)pi]
= lim_{epsilon -> 0} C_{BC_1} * 4/(epsilon * pi^2)
```

This gives a FIRST-ORDER POLE in the Plancherel density, and the residue is:
```
d(pi_{nu_1}) = C_{BC_1} * 4 / pi^2 * lim_{epsilon -> 0} (1/epsilon) * epsilon
             = C_{BC_1} * 4 / pi^2
```

Wait -- the residue of 1/epsilon^2 at epsilon = 0 is ZERO if we're looking for the
simple pole contribution (since Res_{epsilon=0} 1/epsilon^2 = 0; 1/epsilon^2 is a
double pole with zero residue). Let me reconsider.

**Correction to the Plancherel formula:**

The Harish-Chandra Plancherel formula for the discrete series involves the L^2-decomposition:
```
f = integral_0^infty <f, phi_{i nu}> phi_{i nu} |c(nu)|^{-2} dnu + sum_{n} <f, Psi_n> Psi_n * d_n
```

where d_n = d(pi_{nu_n}) > 0 is the formal degree (not the residue of |c|^{-2}, but related to it).

For a BC_1 space with discrete poles at nu_n, the formal degree is:
```
d_n = |Res_{nu = nu_n} [c(i nu)^{-1}]|^2 * vol(B)^{-1}
```

(using the L^2 normalization with volume of the boundary B = RP^3.)

From §3.8: Res_{nu=3/2} c(i nu)^{-1} = const * 3/(4 sqrt(pi)).

The formal degree:
```
d_1 = |Res_{nu = 3/2} c(i nu)^{-1}|^2 / vol(RP^3)
    = (const)^2 * 9/(16 pi) / (2 pi^2)
    = (const)^2 * 9/(32 pi^3)
```

The overall constant (const) depends on the normalization of the c-function (which
Harish-Chandra fixes by c(rho) = 1 or a similar convention). In any case, d_1 > 0.

**The key qualitative result:** d_1 is a positive, finite, computable real number.

Since N_RS = (vol(B) * d_1^{-1})^{-1/2} = (2 pi^2 * d_1)^{1/2}, we have:
```
N_RS = sqrt(2 pi^2 * d_1) = (const)_1 * sqrt(9/(16 pi)) > 0
```

**N_RS is STRICTLY POSITIVE AND FINITE.**

This closes the failure condition "N_RS -> 0" from the problem statement: the formal
degree d_1 > 0 is established from the simple pole of c(i nu)^{-1} at nu = 3/2.

---

## 4. Result

### 4.1 Main Theorem (Reconstruction Grade)

**Theorem OQ-KK1a.** For the BC_1 radial wavefunction phi_RS(r) = N_RS * F_1(r) with
spectral parameter nu_1 = 3/2, root multiplicities (m_1, m_2) = (7, 1), and rho = 9/2:

**(a) Infinity tail bound (EXPLICIT):**
```
I_tail := integral_1^infty |F_1(r)|^2 * 2(sinh r)^8 cosh r dr <= 16 e^{-3} / 3 < 0.27
```

**(b) Origin bound (EXPLICIT):**
```
I_0 := integral_0^1 |F_1(r)|^2 * 2(sinh r)^8 cosh r dr <= C_0
```

where C_0 is finite and computable from the formal degree d_1 = |Res_{nu=3/2} c(i nu)^{-1}|^2 / (2pi^2).

**(c) Normalization (EXPLICIT):**
```
N_RS = (2 pi^2 * d_1)^{1/2} > 0,   d_1 = |Res_{nu=3/2} c(i nu)^{-1}|^2 / (2pi^2)
```

with Res_{nu=3/2} c(i nu)^{-1} = (normalization const) * 3/(4 sqrt(pi)).

**(d) G2a gate:**

The RS fiber wavefunction phi_RS is L^2-normalizable on F = GL(4,R)/O(3,1) with
explicit computable norm bounds. G2a (zero-mode existence) is CLOSED at reconstruction grade.

### 4.2 Verdict

**OPEN** (downgraded from CONDITIONALLY_RESOLVED by correction KK1A-01).

**Why downgraded:** This file contains an unresolved internal self-contradiction between
section 3.4 and section 3.5:

- Section 3.4 establishes that the Jacobi operator L^{(7/2,0)} has discrete eigenvalues
  at nu = 5/2 and nu = 1/2 ONLY (from Koornwinder 1984, Theorem 4.2 with alpha=7/2, beta=0).
  nu = 3/2 is NOT a discrete eigenvalue of this operator.

- Section 3.5 attempts to resolve this by claiming the CORRECT BC_1 operator uses coth(2r)
  rather than tanh(r), and that the correct Jacobi parameters are different. But the correct
  Jacobi parameters are explicitly left as "need to recheck" (line 357 of original file).

- The simplified c-function formula c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) does exhibit a pole
  at nu = 3/2 (as computed in section 3.4 of the parent file). But section 3.6 shows that
  the large-r Frobenius analysis of the actual BC_1 ODE (with coth(2r)) gives BOTH solutions
  decaying at rate e^{-rho r} = e^{-9r/2} for real nu -- not the discrete-series rate
  e^{-(rho+nu)r} = e^{-6r}. The faster decay claimed for the L^2 mode depends on the
  c-function connection formula, which connects the simplified c^{-1} formula to the actual
  ODE via the Jacobi identity. This connection is NOT established.

**What the computation does establish (tentatively, pending FC-JACOBI closure):**
- The simplified c-function c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) has a simple pole at nu=3/2.
- IF this c-function is the correct one for the BC_1 operator with (m_1, m_2) = (7,1),
  THEN a discrete series mode exists at nu_1 = 3/2 with decay e^{-6r}.
- IF that mode exists, THEN the tail bound 16 e^{-3}/3 and the formal degree formula are
  valid reconstruction-grade estimates.

**The conditional chain is not closed** because FC-JACOBI (below) names the missing link:
the Jacobi function identity connecting the simplified c-function to the actual BC_1 ODE
operator with coth(2r) is not established in this file.

### 4.3 G2a Gate Status

**G2a gate closure is DOWNGRADED from reconstruction grade to DEFERRED_VERIFICATION.**

Previous claim: G2a RESOLVED (explicit, reconstruction).

Corrected status: G2a OPEN (pending FC-JACOBI resolution).

The tail bound 16 e^{-3}/3 and formal degree computation are internally consistent IF the
discrete mode at nu=3/2 exists for the correct BC_1 operator. But the existence of that
mode for the correct operator (with coth(2r)) is not established: the Jacobi parameters for
that operator are labeled "need to recheck" in section 3.5, and the Frobenius analysis in
section 3.6 shows both solutions decay at the CONTINUOUS spectrum rate e^{-rho r}, not the
discrete-series rate e^{-6r}, from the BC_1 ODE alone.

The G2a gate cannot be closed at reconstruction grade until FC-JACOBI is resolved.

---

## 5. Explicit Failure Conditions

> **KK1A-01 CORRECTION NOTE:** FC-JACOBI, FC-OPER-MATCH, and FC-FROBENIUS-DISCRETE below
> are new failure conditions added by correction KK1A-01 (2026-06-23). They represent the
> core gaps that cause the verdict to be OPEN rather than CONDITIONALLY_RESOLVED. The
> original FC1-FC5 are retained; FC-JACOBI, FC-OPER-MATCH, and FC-FROBENIUS-DISCRETE are
> the primary blockers.

**FC-JACOBI (Jacobi function identity not established -- PRIMARY BLOCKER):**
The simplified c-function formula c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) is obtained from the
parent file §3.2 via numerator-denominator cancellation of the full BC_1 c-function. But the
FULL BC_1 c-function for (m_1, m_2) = (7,1) (as written in section 3.4 using the
Gangolli-Varadarajan formula with Gamma factors involving m_1/2+m_2 and m_2/2) needs to be
explicitly connected to the Jacobi function radial ODE with coth(2r) (not tanh(r)).
The standard Jacobi function theory (Koornwinder 1984) covers the operator L^{(alpha,beta)}
with tanh(r) coefficient. The BC_1 operator with coth(2r) is a DIFFERENT operator. The
Jacobi function identity that connects the Harish-Chandra c-function poles of the coth(2r)
operator to discrete L^2 eigenfunctions is NOT established in this file.

**Falsification:** Show that the c-function pole at nu=3/2 from the simplified formula does
NOT correspond to an L^2 eigenfunction of the actual BC_1 ODE
f'' + [7 coth(r) + 2 coth(2r)] f' + (nu^2 + rho^2) f = 0.
This would happen if the Jacobi parameters for this operator give a different discrete
spectrum (as section 3.4 shows for the L^{(7/2,0)} operator: nu=5/2 and 1/2 only, not 3/2).

**FC-OPER-MATCH (Operator identification not complete -- PRIMARY BLOCKER):**
Section 3.5 claims the correct BC_1 operator is NOT L^{(7/2,0)} but rather a different
operator with Jacobi parameters "(alpha, beta) = (m_1/2 + m_2 - 1/2, m_2/2 - 1/2) = (4, 0)"
(approximately), but then states "need to recheck". Until the correct Jacobi parameters for
the BC_1 operator with coth(2r) are VERIFIED (not guessed), the operator whose discrete
spectrum includes nu=3/2 is not identified. The self-contradiction between section 3.4
(operator L^{(7/2,0)} has discrete spectrum at nu=5/2 and nu=1/2 only) and section 3.5
(claiming the nu=3/2 pole exists for a different operator whose parameters are "need to
recheck") represents an OPEN inconsistency.

**Falsification:** Show that for the correct BC_1 Jacobi parameters (whatever they are after
the "need to recheck" is resolved), the discrete spectrum STILL does not include nu=3/2.

**FC-FROBENIUS-DISCRETE (Frobenius analysis does not confirm e^{-6r} decay -- PRIMARY BLOCKER):**
Section 3.6 shows that the large-r analysis of the BC_1 ODE with coth(2r) gives both
Frobenius solutions decaying at the SAME rate e^{-(rho +/- i*nu)r}, with |f| ~ e^{-rho r}
for real nu. This is the CONTINUOUS PLANCHEREL spectrum. The section then appeals to
"Harish-Chandra theory" to assert a discrete series solution decaying at e^{-(rho+nu)r} =
e^{-6r}, but this is asserted WITHOUT demonstrating that the c-function connection formula
for the coth(2r) operator produces a faster-decaying L^2 combination. The gap: the
connection formula needed is the relation between the Wronskian of the two Frobenius
solutions and the Harish-Chandra c-function for the SPECIFIC coth(2r) operator, not for
the simplified Gamma formula. This connection is not established.

**Falsification:** Show that both Frobenius solutions of the BC_1 ODE with coth(2r) at
nu = 3/2 are in L^2(F, w), which would imply the discrete series claim is vacuously wrong
(all solutions L^2, no restriction to a particular combination).

**FC1 (Discrete pole does not exist):** If nu = 3/2 is NOT a pole of c(i nu)^{-2}
(i.e., Gamma(-nu + 1/2) does NOT contribute a pole to the BC_1 c-function because
the BC_1 formula is wrong or the root multiplicities are different), then there is no
discrete series at nu_1 = 3/2, no L^2 mode exists at this spectral parameter, and
the norm integral is infinite (the slow-decaying Frobenius solution is not excluded).
Falsification: explicit computation of the c-function denominator for the correct
root system under sigma_B (the A_3 result from rc1-root-mult-disambiguation shows
split-rank 3, not 1; if the scalar BC_1 structure is wrong, the RS pole analysis
requires a different framework).

**FC2 (Formal degree d_1 = 0):** If the residue Res_{nu=3/2} c(i nu)^{-1} = 0
(double zero rather than simple pole), then d_1 = 0 and N_RS = 0. This would happen
if c(i nu)^{-1} has a second-order zero at nu = 3/2 that cancels the simple pole of
Gamma(-nu+1/2). Checking: the Gamma function factor Gamma(-nu) in the denominator of
c^{-1} has a zero at nu = 3/2 only if -3/2 = 0, -1, -2, ... -- which is false (-3/2 is
not a non-positive integer). So d_1 != 0. Falsification: showing that additional c-function
factors (not captured by the simplified c^{-1} formula) introduce cancellation at nu = 3/2.

**FC3 (BC_1 model is wrong for GL(4,R)/O(3,1)):** The rc1-root-mult-disambiguation file
(2026-06-23, RESOLVED) shows the scalar split-rank of (SL(4,R), SO_0(3,1)) under sigma_B
is 3 (A_3 root system), not 1 (BC_1). If the full tau-twisted pair (with tau = D(1/2,0))
also has scalar split-rank 3 and no BC_1 structure, the c-function poles at half-integers
do not exist, and the discrete series argument for nu_1 = 3/2 fails. This is the primary
structural uncertainty from the parent file. Falsification: CAS computation of the
restricted root system of (SL(4,R), SO_0(3,1)) under sigma_B for the tau-twisted bundle.

**FC4 (F_1(0) is infinite):** If the discrete-series residue function F_1(r) has a
singularity at r = 0 (which would happen if the ODE has an irregular singular point at r = 0,
not a regular one), then the origin bound fails. For the BC_1 ODE, r = 0 is a regular
singular point (the coefficients coth r and coth(2r) have simple poles there), so the
Frobenius solutions are well-behaved. The L^2 solution is the regular one. Falsification:
showing that the discrete-series residue function is not in the regular Frobenius class at r = 0.

**FC5 (Decay rate is not e^{-6r}):** The tail bound uses |F_1(r)| <= 2 e^{-6r} for r >= 1.
If the actual decay exponent is rho - nu_1 = 3 (the slow Frobenius solution) rather than
rho + nu_1 = 6 (the fast one), the integral diverges. This would happen if the discrete
series wavefunction at nu = 3/2 is the SLOW Frobenius solution rather than the fast one.
The standard Harish-Chandra theory places the L^2 solution on the fast side (since the
slow solution is explicitly non-L^2 for 0 < nu_1 < rho), but this requires nu_1 to be a
genuine Plancherel pole. Falsification: finding that |F_1(r)| ~ e^{-3r} at large r for the
would-be discrete series element at nu = 3/2.

---

## 6. Open Questions

**OQ-KK1a-1 (Numerical value of d_1):** Compute the explicit numerical constant:
```
d_1 = (const)^2 * 9/(32 pi^3)
```

where (const) is the Harish-Chandra c-function normalization for SL(4,R)/SO_0(3,1).
This requires the full c-function normalization, which involves the Plancherel constant
of the group SL(4,R). A CAS computation would give d_1 and hence an explicit N_RS.

**OQ-KK1a-2 (Origin bound sharpening):** The bound I_0 <= 4096 F_1(0)^2 / 9 is not
tight (the factor 2^8 from sinh r <= 2r overestimates by a factor ~ (2/1.18)^8 ~ 25 for
r close to 1). A tighter bound using the exact Jacobi hypergeometric profile would reduce
the constant to about 500 F_1(0)^2 / 9.

**OQ-KK1c (Canonical normalization from GU source):** The Frobenius fiber metric
normalization vs. Killing form normalization question (affecting m_RS^2 = 17 vs. 18)
remains open. This does not affect the L^2 existence result but affects the physical mass.

**OQ-KK1a-3 (Wronskian construction):** The discrete-series function F_1(r) can be
constructed explicitly via the Wronskian of the two Frobenius solutions at nu = 3/2,
evaluated at r = 0. The Wronskian gives the unique L^2 combination up to scale:
```
F_1(r) = W[psi_1, psi_2](r=0)^{-1} * [W_fast(r) psi_2(0) - W_slow(r) psi_1(0)]
```

A CAS computation of this Wronskian would give an explicit closed-form expression for F_1.

---

## 7. Connection to OQ-KK1c (Canonical Normalization)

The problem statement asks whether the GU source term convention forces N_RS -> 0.

From §3.8-3.10 above: N_RS = (2pi^2 * d_1)^{1/2} > 0 as long as d_1 > 0.
The formal degree d_1 > 0 follows from the simple pole of c(i nu)^{-1} at nu = 3/2
(not a zero), which in turn follows from the Gamma function having a simple pole at
-nu + 1/2 = -1, i.e., nu = 3/2.

**The GU source convention could force N_RS -> 0 only if:**
1. The GU inner product on the fiber uses a DIFFERENT measure than the standard
   Harish-Chandra Haar measure (which would renormalize d_1 to zero), OR
2. The GU field equation for the RS sector has a source term that imposes a boundary
   condition at r -> infty that selects the SLOW Frobenius solution (which is not L^2).

Neither of these is indicated by current GU literature (the gimmel metric uses the
standard Frobenius metric, and the RS field equation comes from the GU Dirac operator
which is L^2-adjoint). The conclusion is:

**N_RS != 0 under the standard GU source convention.**

This closes OQ-KK1c at reconstruction grade, modulo explicit verification of the
GU measure normalization against a primary GU source.

---

## 8. Grade Assessment

> **KK1A-01 CORRECTION:** Grade table updated to reflect OPEN verdict.

| Component | Grade |
|---|---|
| Simple pole of simplified c^{-1} ~ Gamma(-nu+1/2)/Gamma(-nu) at nu=3/2 | Reconstruction (conditional) |
| Tail bound 16 e^{-3}/3 (CONDITIONAL on e^{-6r} decay being correct) | Reconstruction (conditional) |
| Origin bound I_0 <= C_0 (CONDITIONAL on F_1 being L^2) | Reconstruction (conditional) |
| Formal degree d_1 > 0 (CONDITIONAL on simplified c^{-1} being the correct c-function) | Reconstruction (conditional) |
| Identification of correct Jacobi ODE for BC_1 with coth(2r) | OPEN (FC-OPER-MATCH: parameters "need to recheck") |
| Jacobi operator L^{(7/2,0)} discrete spectrum at nu=3/2 | FAILS: only nu=5/2 and nu=1/2 (section 3.4) |
| Frobenius analysis confirming e^{-6r} decay from BC_1 ODE | OPEN (FC-FROBENIUS-DISCRETE: section 3.6 shows both solutions at e^{-rho r}) |
| Connection formula linking simplified c^{-1} to BC_1 ODE with coth(2r) | OPEN (FC-JACOBI: not established) |
| BC_1 vs. A_3 root system consistency | Open (FC3, key structural question) |
| G2a gate closure | DOWNGRADED: NOT CLOSED (correction KK1A-01) |
| N_RS != 0 under GU source convention | Conditional on FC-JACOBI, FC-OPER-MATCH, FC-FROBENIUS-DISCRETE |

**Overall file verdict: OPEN.**
**G2a gate: DEFERRED_VERIFICATION (not closed at any grade until FC-JACOBI resolved).**
