---
title: "VZ F6: 4D EFT Decoupling — KK Mass Scale, Codazzi-Corrected RS/Spin-1/2 Mixing Gap, and Loop Suppression of B/C Blocks"
date: 2026-06-23
problem_label: "vz-4d-eft"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# VZ F6: 4D EFT Decoupling of the RS Sector

## 1. Problem Statement

**What is being computed.** The principal-symbol VZ evasion is CONDITIONALLY_RESOLVED at 4D (constant-coefficient gauge; vz-schur-complement
§18, OQ3-V1/V2/V3 resolved). The F5 curvature-protection check is CONDITIONALLY_RESOLVED
(vz-f5-curvature-check). The remaining open question labeled F6 in the tracking table asks:

> Does a KK-type mass scale M_KK separate the RS sector into an approximately standalone
> 4D field at low energies, and if so, does the resulting EFT RS field re-acquire VZ vulnerability?

The preliminary analysis in vz-schur-complement §19 established the structural EFT argument
at reconstruction grade. This file deepens it along three axes:

1. **KK mass gap estimation via the section-pullback Codazzi correction.** The Codazzi equation
   derived in codazzi-sp64-2026-06-23.md governs the normal-bundle curvature; its spectrum
   determines M_KK. We use the Codazzi correction to estimate the RS/spin-1/2 mixing gap.

2. **B/C block structure at zero-mode level.** The off-diagonal coupling blocks B (spin-1/2
   to RS) and C (RS to spin-1/2) in the Schur complement were identified as O(1) algebraic
   maps in §19.4. Here we verify this claim with explicit Clifford-block matrices and assess
   whether any mechanism could suppress these blocks below M_KK.

3. **Loop corrections to B/C blocks.** The question whether quantum loop corrections at
   one loop (or higher) can effectively decouple the RS and spin-1/2 sectors below M_KK
   is assessed structurally. A suppression would open a window for VZ vulnerability in
   the EFT; an absence confirms the evasion is UV-robust.

**Why F6 matters.** VZ fires for standalone RS fields with non-trivial gauge coupling. The
entire VZ evasion argument rests on the non-standalone character of the RS sector: it is
the Leibniz cross-term in D_GU, permanently coupled to the spin-1/2 sector. If the B/C
coupling is suppressed at any energy scale, the RS sector would effectively decouple and
VZ would re-apply. This file proves the coupling is kinematic (not dynamical), making
decoupling impossible by structure.

---

## 2. Established Context

**Prior results this builds on:**

- `vz-schur-complement-2026-06-23.md` §8: Schur complement `S_R = A - B E^{-1} C` has
  `ker = 0` for all `g_Y(xi,xi) != 0`. VZ evasion at 14D: EVADED (reconstruction).

- `vz-schur-complement-2026-06-23.md` §18: 4D section-pullback preserves Clifford module
  identity. `ker S_{R_s}^{4D}(eta) = 0` for all `g_s(eta,eta) != 0`. VZ evasion at 4D:
  VERIFIED (OQ3-V1/V2/V3 resolved).

- `vz-schur-complement-2026-06-23.md` §19: F6 preliminary analysis. KK zero mode projector
  commutes with horizontal Clifford element. B/C blocks are O(1) in zero-mode sector.
  Structural conclusion: no standalone RS EFT arises. Status: CONDITIONALLY_RESOLVED.

- `vz-f5-curvature-check-2026-06-23.md`: All curvature sources (Weyl, Riemann, F_A, II_s,
  H^{(i)}) are zero-order in Psi after 4D pullback. VZ evasion is curvature-robust.
  Status: CONDITIONALLY_RESOLVED.

- `vz-oq1-sr-squared-identity-2026-06-23.md`: `S_R^2 != xi^2 Id_R` (explicit: the B
  E^{-2} C correction is nonzero, coefficient `(2842 chi - 98 mu)/7 xi^2` in 14D).
  The RS sector is not a sub-Clifford-module. This is the evasion mechanism.

- `codazzi-sp64-2026-06-23.md`: Full Codazzi equation for Sp(64) derived:
  `[D_{a0}, D_{a0}](j_s theta) = j_s(R^{Y^14,perp}) + F^Psi_{j_s} - [F_{a0}, j_s theta]`.
  Normal-bundle curvature `R^{Y^14,perp}` governs the normal-direction spectrum.

- `ii-s-moving-frames-2026-06-23.md`: Gimmel Christoffel symbols explicit. Normal-direction
  fiber metric V = trace-reversed Frobenius metric on `Sym^2 T*X^4`.

- `n5-discrete-series-gl4r-2026-06-23.md`: Generation count `ind_H(D_GU) = 24` from
  `8*Â(X^4) + 8 = 8*2 + 8` (K3-type + RS sector). KK zero mode existence gates on
  discrete-series condition (CONDITIONALLY_RESOLVED).

**Physical setup.** After section pullback `s: X^4 -> Y^{14}`, the 14-dimensional
bulk is compactified. The 10 normal directions `N_s = Sym^2 T*X^4` (signature (6,4))
carry the KK tower. The KK mass gap is:

```
M_KK ~ 1/R_N
```

where `R_N` is the characteristic size of the normal fiber. From the gimmel geometry,
`R_N` is set by the scale of curvature of `g_Y` in the fiber directions.

---

## 3. KK Mass Gap from the Codazzi Correction

### 3.1 Normal-Direction Spectrum

The Codazzi equation for the Sp(64) bundle (codazzi-sp64) gives the curvature of the
normal connection:

```
[D_{perp}, D_{perp}](j_s theta) = R^{Y^14, perp} + F^Psi_{j_s} - [F_{a0}, j_s theta]
```

The normal-direction Laplacian acting on sections of `E_s = s*E -> X^4` is:

```
Delta_N = - sum_{i=1}^{10} (D_{n_i})^2
```

where `{n_i}` is a frame for the normal bundle `N_s` at the section. The eigenvalues of
`Delta_N` determine the KK mass spectrum.

**The normal-bundle metric.** From ii-s-moving-frames, the fiber metric on `Sym^2 T*X^4`
is the trace-reversed Frobenius metric V:

```
V(h, k) = (1/2)[g_s(h, k) - (1/4) tr(h) tr(k)]   for h, k in Sym^2 T*X^4
```

(Signature (6,4): 6 positive modes from traceless symmetric 2-tensors of mixed + signature,
4 negative from timelike-containing modes.)

**KK mass gap from normal Lichnerowicz spectrum.** The operator `Delta_N` restricted to
the fiber `GL(4,R)/O(3,1)` over a point `x in X^4` is the Laplacian on the fiber
`F_x = GL(4,R)/O(3,1)`. In the compact approximation (treating the fiber as a compact
homogeneous space), the first eigenvalue of `Delta_N` sets M_KK.

**Fiber geometry.** The fiber homotopy type is `F_x ~= RP^3 ~= SO(3)` (from N5/N6 analysis:
polar decomposition gives `GL(4,R)/O(3,1) ~= RP^3` via `O(4)/(O(3) x O(1)) = S^3/Z_2`).
The normal-direction fiber is 10-dimensional (not 3-dimensional), because the full fiber
is `Sym^2 T*R^{3,1} / R^+` (trace directions quotiented out).

For the fiber `F_x`, the relevant normal-direction operator is the Laplacian on
`Sym^2_0(R^{3,1})` (traceless symmetric 2-tensors, the 9-dimensional fiber of `Y^{14}`
after modding out the scale). With the Frobenius metric and trace-reversal:

**Claim.** The lowest eigenvalue of the normal Laplacian `Delta_N` on the 10-dimensional
fiber at a smooth section `s: X^4 -> Y^{14}` is:

```
lambda_{N,min} ~ 1/R_s^2
```

where `R_s` is the curvature radius of `g_s` (the characteristic scale of the 4D metric).
This follows because the Frobenius metric on `Sym^2 T*X^4` is controlled by `g_s` (the
fiber metric is bilinear in the base metric components).

**KK mass gap estimate:**

```
M_KK ~ 1/R_s
```

This is the Planck-scale (or curvature-scale) KK mass gap: the normal modes of the fiber
become heavy at the scale of curvature of the physical metric `g_s`. On cosmological scales
(`R_s ~ H^{-1} = t_obs`), this gives `M_KK ~ H = 1/t_obs`, coinciding with the Hubble
scale. On particle physics scales (where `g_s ~ eta_{mu nu}`, Minkowski), the fiber
is approximately flat and `M_KK -> infinity` (no finite KK gap in the flat limit).

**Consistency check with CPA-1.** The Tikhonov scale `Lambda_GU ~ epsilon^2/t_obs^2`
(cpa1-tobs) sets the section-selection regularization. At this scale, the section
curvature is controlled. The KK gap `M_KK ~ 1/R_s ~ 1/t_obs` is consistent:
`M_KK^2 ~ lambda_max^2 = 1/t_obs^2`, matching the Tikhonov scale up to an `epsilon^2` factor.

**Codazzi correction to M_KK.** The Codazzi equation gives the curvature of the normal
connection. Its contribution shifts the normal Laplacian eigenvalues by:

```
Delta lambda_N = [R^{Y^14,perp}]|_{fiber} + [F^Psi_{j_s}]|_{fiber}
```

From vz-f5 and codazzi-sp64: these contributions are zero-order (they shift eigenvalues
but do not change the order of the operator). The leading eigenvalue remains `~ 1/R_s^2`.

The Codazzi correction therefore does NOT lower M_KK to zero. It is a subleading correction
that shifts the KK gap by O(curvature/M_KK^2) relative corrections.

### 3.2 RS/Spin-1/2 Mass Splitting

**Mass spectrum separation.** The RS and spin-1/2 sectors have different KK mass spectra
because they have different D_GU block structures:

- **Spin-1/2 zero modes:** The spin-1/2 sector of D_GU is the block `E` (non-RS sector).
  Its zero-mode mass comes from the zero-order piece of `E` at zero momentum `eta = 0`.
  From §3.2 of vz-schur-complement, `E` has a scalar sub-block and a gamma-trace sub-block.

- **RS zero modes:** The RS sector block `A` has zero-mode mass from the RS constraint
  projection. From §19.6 of vz-schur-complement, the RS zero-mode mass `m_RS` is a
  zero-order operator in `D_GU^{4D}`.

**The mixing gap.** The RS/spin-1/2 mixing gap `delta_m` is the difference between the
lowest RS mass and the lowest spin-1/2 mass in the 4D KK spectrum. From the block
structure of D_GU:

```
A(eta=0) = P_R [D_GU^{(0)}] P_R     (RS zero-mode mass operator)
E(eta=0) = P_Q [D_GU^{(0)}] P_Q     (spin-1/2 zero-mode mass operator)
```

where `D_GU^{(0)}` is the zero-order (mass) part of the full operator.

**Codazzi correction to the mixing gap.** The Codazzi equation for Sp(64) gives an
explicit correction to the effective RS mass from the normal-bundle curvature:

```
D_GU^{(0),RS} = [D_GU^{(0)}]_{RS-RS} + [F^{perp}_{j_s} correction]_{RS-RS}
```

From codazzi-sp64: `[D_{a0}, D_{a0}](j_s theta) = j_s(R^{Y^14,perp}) + ...`. The
`R^{Y^14,perp}` term contributes an additive correction to the RS mass at O(curvature).
Explicitly, in the notation of codazzi-sp64:

```
Delta m_RS = [j_s(R^{Y^14,perp})]_{RS-RS projection}
           = P_R [c(n_i) c(n_j) R^{perp}_{ij}] P_R
```

where `R^{perp}_{ij}` are the normal-bundle curvature 2-form components. This is an
SO(1,3)-invariant zero-order operator.

**Estimate.** The normal-bundle curvature `R^{Y^14,perp} ~ 1/R_s^2` (from the Gauss
formula: normal curvature is bounded by the ambient curvature `R^{Y^14}`). Therefore:

```
Delta m_RS ~ 1/R_s^2 ~ M_KK^2
```

The Codazzi correction to the RS mass is of the same order as M_KK. This means the
RS zero-mode mass is generically of order M_KK, not parametrically lighter.

**Consequence for decoupling.** The RS zero-mode mass `m_RS ~ M_KK` means:
- Below `M_KK`: both the RS and spin-1/2 KK towers are integrated out simultaneously.
  There is no window in which only spin-1/2 modes propagate and RS modes are absent.
- The mixing gap `delta_m = |m_RS - m_{1/2}|` is at most O(M_KK). It does not separate
  the sectors at energies `E << M_KK` because both sectors become non-propagating at
  the same scale.

**An exception: KK zero modes with m = 0.** If the 4D theory has massless RS zero modes
(`m_RS = 0`) and massive spin-1/2 zero modes (`m_{1/2} ~ m_{SM}`), the RS sector would
be the lightest. But massless RS fields in 4D would be Goldstino-type particles (requiring
a broken SUSY). In GU there is no broken global SUSY at the fundamental level (the gauge
group is Sp(64), not a supergroup). So massless RS zero modes are not expected generically.

The existence of RS zero modes is gated on the discrete-series condition (CONDITIONALLY_RESOLVED,
n5-discrete-series-gl4r §12-19): the formal degree computation gives `ind_H(S_R^{eff}) = 8`,
meaning the RS sector has exactly 8 H-lines' worth of L^2 zero modes on the non-compact fiber.
These are zero modes of `S_R^{eff}` (the effective RS operator on `GL(4,R)/O(3,1)`), not of
the 4D massive theory.

---

## 4. B/C Coupling Block Structure: Explicit Assessment

### 4.1 Tree-Level B/C Blocks

At tree level (classical), the B and C blocks in the Schur complement are:

```
B(eta): Q_s^{(0)} -> R_s^{(0)}    (spin-1/2 / scalar -> RS)
C(eta): R_s^{(0)} -> Q_s^{(0)}    (RS -> spin-1/2 / scalar)
```

From §3 and §19.4 of vz-schur-complement, these are determined by:

```
B(eta)_{AR} = (P_R sigma_D(eta) P_Q)_{A}
C(eta)_{RA} = (P_Q sigma_D(eta) P_R)_{A}
```

where `sigma_D(eta)` is the principal symbol of `D_GU^{4D}` at covector `eta in T*X^4`.

**Explicit form of B and C at 4D.** From the block computation in §3 of vz-schur-complement
(here specialized to 4D horizontal covectors `eta in H* = T*X^4`):

For an RS input `psi_R` with `chi = g_s(eta, psi_R)`:

```
C(eta) psi_R:
  scalar component = chi                                  [from (C1)]
  4D gamma-trace component = gamma_s(eta) chi - 2 chi    [from (C2), with 14 -> 4]
```

For the 4D case, the gamma-trace contraction factor changes from 14 to 4:
`gamma^a gamma(eta) gamma_a = (2-4) gamma(eta) = -2 gamma(eta)` in 4D.

So `Gamma^{4D}(F_eta psi_R) = gamma_s(eta) chi - 2 chi` (4D version with factor `(13/7)` replaced
by the 4D equivalent `(2-4/4 + 1) * chi` -- more precisely, using the 4D contraction identity
`{gamma^a, gamma(eta)} = 2 eta^a` in 4D with `n = 4`:

```
Gamma^{4D}(F_eta psi_R) = gamma_s(eta) chi + (2-2) chi = gamma_s(eta) chi       [4D version]
```

(The coefficient changes from 14D's `(2 - 2) = 0` -- wait, let me be careful. In n dimensions:
`gamma^A gamma(xi) psi_{R,A} = (2 xi^A - gamma(xi) gamma^A) psi_{R,A} = 2 chi - gamma(xi) * 0 = 2 chi`
using `Gamma^n(psi_R) = 0`. This is dimension-independent. So `Gamma^{4D}(F_eta psi_R) = gamma_s(eta) chi - 2 chi` in 4D as well, matching the 14D formula (C2).)

The C block maps `psi_R` to `(chi, gamma_s(eta) chi - 2 chi)` which is generically nonzero whenever
`chi = g_s(eta, psi_R) != 0`.

**When does chi vanish?** `chi = g_s(eta, psi_R) = eta^a psi_{R,a}` (contraction of the 4D
covector `eta` with the spin-vector index of `psi_R`). This vanishes when:

1. `eta = 0` (zero momentum, trivially), or
2. `psi_R` is `g_s`-orthogonal to `eta` for all 4D components.

Condition 2 requires `eta^a psi_{R,a} = 0` for all components `a`. For a nonzero covector `eta`,
this imposes a linear constraint on `psi_R`. The RS constraint `Gamma^{4D}(psi_R) = gamma^a psi_{R,a} = 0`
is a different linear constraint. Generically, the subspace `{psi_R : chi = 0}` within `R_s^{(0)}`
is proper (not the whole RS sector).

**Conclusion: C is generically nonzero.** For generic non-null `eta` and generic `psi_R in R_s^{(0)}`,
`chi = g_s(eta, psi_R)` is nonzero, and `C(eta) psi_R != 0`. The B block is the transpose of C
(up to Clifford-adjoint), so it is also generically nonzero.

**The B and C blocks are kinematic.** They depend only on:
- The Clifford algebra structure of `Cl(9,5)` pulled back to `T*X^4`
- The RS projection `P_R = (Id - (1/4) gamma_a Gamma^{4D, adj})` (4D version)
- The covector `eta`

They do NOT depend on:
- The gauge coupling of Sp(64)
- The Sp(64) connection `A` (enters only zero-order)
- The second fundamental form II_s (enters only zero-order)
- Any dynamical coupling constant

This is the central structural fact: the RS/spin-1/2 coupling is kinematic, built into the
Clifford module structure, not a dynamical parameter that can be tuned to zero.

### 4.2 KK Mode Restriction of B/C

When we restrict to KK zero modes (the EFT truncation), the zero-mode versions of B and C are:

```
B^{(0)}(eta) = P_{(0)} B(eta) P_{(0)}: Q_s^{(0)} -> R_s^{(0)}
C^{(0)}(eta) = P_{(0)} C(eta) P_{(0)}: R_s^{(0)} -> Q_s^{(0)}
```

The KK mode projector `P_{(0)}` acts on the fiber (normal-direction) quantum numbers, not on
the 4D spacetime or Clifford-algebra structure. Since B and C are purely algebraic (Clifford
matrices acting on `S = H^{64}` and the spinor-vector structure), and the KK projector acts
on the fiber quantum numbers:

```
P_{(0)} [c_s(eta)] = c_s(eta) P_{(0)}     [commutativity, §19.3]
```

Therefore:

```
B^{(0)}(eta) = B(eta)|_{zero modes},   C^{(0)}(eta) = C(eta)|_{zero modes}
```

These are the same algebraic matrices B and C, just evaluated on the zero-mode subspace. Their
rank is generically the same as the full B and C (no reduction in the fiber-direction projection
can kill the 4D Clifford-algebra structure). Hence:

```
B^{(0)} = O(|eta|),    C^{(0)} = O(|eta|)    (linear in eta, O(1) coefficients)
```

The coupling is not suppressed below M_KK. The KK truncation does not decouple the sectors.

---

## 5. Loop Corrections to B/C Blocks

### 5.1 What Loop Corrections Could Do

A one-loop correction to the B/C blocks would take the schematic form:

```
B^{1-loop}(eta) = integral_k B(k) E^{-1}(k) C(k+eta) [propagator kernel]
```

where the loop momentum `k` is integrated over all scales. The question is whether such
corrections can suppress `B^{(0)}` below the KK scale `M_KK`.

### 5.2 Structural Argument: Kinematic Coupling Cannot Be Loop-Corrected to Zero

The B and C blocks are **not** conventional dynamical coupling constants. They are components
of the principal symbol `sigma_D(eta)` of a differential operator. Principal symbols are
determined by the kinematic structure (derivative order and Clifford module), not by dynamics.

**The Clifford algebra identity is exact.** The principal symbol satisfies:

```
sigma_D(eta)^2 = g_s(eta, eta) Id_{E_s}    [exact, from OQ3-V1]
```

This identity holds at all loop orders, because it is a consequence of the Clifford algebra
structure of `Cl(9,5)`, which is a fixed algebraic fact. The loop-corrected operator
`D_GU^{1-loop}` still acts on sections of a Cl(9,5)-module, so its principal symbol
satisfies the same Clifford identity.

**Implication for B and C.** The full Schur block structure at any loop order is:

```
sigma_{D^{n-loop}}(eta) = [A^{(n)}(eta)  B^{(n)}(eta)]
                          [C^{(n)}(eta)  E^{(n)}(eta)]
```

The Clifford identity forces `sigma^2 = xi^2 Id`. As computed in vz-oq1 (S_R^2 clarification):
the cross-term `B E^{-2} C` is explicitly nonzero at tree level (coefficient `(2842 chi - 98 mu)/7 xi^2`
in 14D). Loop corrections to this cross-term would be computable as functional-determinant
corrections, but they cannot kill the cross-term algebraically, because the algebraic identity
`A S_R = xi^2 Id_R` (from block-square (II)-(III)) must hold at each loop order by consistency
of the Clifford module structure.

In other words: if `B^{(n)} = 0` identically at some loop order n, then `A^{(n)} S_R^{(n)} = xi^2 Id_R`
would force `A^{(n)}` to left-invert `S_R^{(n)}`. But then `S_R^{(n)}` would be a Clifford element
itself (since its left inverse is A, a Clifford element), and from OQ1 we know this requires
`B E^{-2} C = 0`. A non-trivial loop correction that sends `B -> 0` would need to cancel
a purely algebraic (Clifford-algebra-determined) quantity, which is impossible: algebraic
relations between Clifford matrix components cannot be altered by quantum corrections in
a fixed representation.

### 5.3 More Precise Statement: Renormalization Group and the Clifford Algebra

In any quantum field theory built on a Clifford module, the renormalization group (RG) flow
of coupling constants can shift the *dynamical* couplings (gauge coupling, mass parameters,
Yukawa couplings). It cannot shift the *kinematic* structure (the Clifford algebra itself).

In the GU context:
- The Sp(64) coupling `g_{Sp}` runs under RG flow.
- The Clifford algebra `Cl(9,5)` does not run under RG flow. It is determined by the
  geometry of Y^{14} = Met(X^4), which is not a dynamical field in the conventional QFT sense.
- The B/C blocks are Clifford-algebra components, not gauge-coupling-dependent coefficients.
  They are not renormalized by loop corrections to the Sp(64) gauge coupling.

**Formal statement.** Let `Z_{RS}` and `Z_{1/2}` be the wave-function renormalization
factors for the RS and spin-1/2 sectors. Under renormalization, the operator `D_GU` is
rescaled as:

```
D_GU^{ren} = Z_{RS}^{1/2} P_R D_GU P_R Z_{RS}^{1/2} + Z_{1/2}^{1/2} P_Q D_GU P_Q Z_{1/2}^{1/2}
             + Z_{mix}^{1/2} (P_R D_GU P_Q + P_Q D_GU P_R) Z_{mix}^{1/2}
```

The mixing renormalization `Z_{mix}` governs the B and C blocks. In general, `Z_{mix} != 0`
because the RS and spin-1/2 sectors are not separately conserved: there is no symmetry in the
14D GU theory that forbids RS-spin-1/2 mixing (it is required by the Clifford module structure).

**Symmetry argument for non-zero mixing.** If there were a symmetry `G_{sep}` that
separately rotated the RS and spin-1/2 sectors (a "fermion-number conservation" for each
separately), then `Z_{mix} = 0` by Ward identity. But in GU:
- The RS sector is not a globally charged sector (it carries the same SM charges as the
  spin-1/2 sector via `S(6,4)`).
- The distinction between RS and spin-1/2 is the Lorentz spin (spin-3/2 vs spin-1/2).
  Lorentz symmetry is NOT broken by the quantum corrections in D_GU (the theory is
  Lorentz-covariant).
- But Lorentz covariance does NOT forbid RS-spin-1/2 mixing: the B/C blocks are
  Lorentz-covariant (they transform as spinor-vector operators under SO(1,3)).

**Conclusion:** No symmetry forbids `Z_{mix} != 0`. Loop corrections renormalize B and C
but cannot send them to zero without violating the Clifford algebra identity. The
mixing remains O(1) at all loop orders.

### 5.4 Explicit One-Loop Estimate

For concreteness, consider a one-loop correction to the RS/spin-1/2 mixing propagator in
the EFT below M_KK. The loop involves:
- An internal RS propagator: `G_R(k) = S_R^{EFT}(k)^{-1}`
- An internal spin-1/2 propagator: `G_{1/2}(k) = E^{EFT}(k)^{-1}`
- Vertex insertions from the B/C blocks

The one-loop correction to the B block is schematically:

```
delta B^{1-loop}(eta) ~ int_{|k| < M_KK} B(k) G_{1/2}(k) E(k) G_R(k+eta) dk^4
                      ~ B_{kin} * (loop integral) * B_{kin}
```

where `B_{kin} = O(|eta|)` is the kinematic B block.

For `|eta| << m_{1/2}` (deep IR):

```
G_{1/2}(k) ~ 1/m_{1/2}    (massive spin-1/2 propagator at zero momentum)
G_R(k) ~ 1/m_RS           (massive RS propagator at zero momentum)
```

The loop integral `int_{|k| < M_KK} dk^4 / (m_{1/2} m_RS)` is power-law divergent (UV) and
suppressed by `1/(m_{1/2} m_RS)` in the IR. With a KK cutoff at M_KK:

```
delta B^{1-loop}(eta) ~ B_{kin} * (M_KK^4 / m_{1/2} m_RS) * B_{kin}
```

For `m_{1/2} ~ m_RS ~ M_KK` (generic from §3.2):

```
delta B^{1-loop}(eta) ~ B_{kin}^2 * M_KK^2 = O(eta^2 / M_KK^2) * M_KK^2 = O(eta^2)
```

This is a **quadratic correction** in `eta` to the **linear** tree-level B block. It is
subleading (does not modify the principal symbol) and does not suppress B.

For `m_{1/2} << M_KK` (if spin-1/2 is light, near the SM scale):

```
delta B^{1-loop}(eta) ~ B_{kin}^2 * M_KK^4 / (m_{1/2} M_KK) = O(eta^2 M_KK / m_{1/2})
```

This is a loop-enhanced correction, but it is **still subleading to the principal symbol**
(it is O(eta^2), while the tree-level B is O(eta)). The principal symbol dominates for
large `|eta|`, and no loop correction can cancel the O(eta) kinematic coupling.

**Summary of loop corrections:**
- Loop corrections to B/C are O(eta^2) or higher, subleading to the tree-level O(eta) blocks.
- They cannot send B/C to zero without violating the Clifford algebra identity.
- The kinematic (principal-symbol) RS/spin-1/2 coupling is loop-stable.
- The Sp(64) coupling `g_{Sp}` runs, but the B/C blocks are Clifford-algebra-determined,
  not coupling-dependent; they do not run with `g_{Sp}`.

---

## 6. Result: F6 EFT Decoupling Verdict

### 6.1 Summary of Findings

| Question | Answer | Grade |
|---|---|---|
| Does M_KK separate RS from spin-1/2 sectors? | No (both at ~M_KK scale generically) | Reconstruction |
| Does KK zero mode projector preserve Clifford identity? | Yes (commutes with horizontal Clifford element) | Verified (§19.3) |
| Are B/C blocks O(1) at zero-mode level? | Yes (kinematic, Clifford-algebra-determined) | Reconstruction |
| Does any energy limit suppress B/C to zero? | No (algebraic identity prevents this) | Reconstruction |
| Are loop corrections to B/C suppressed below M_KK? | Yes (O(eta^2), subleading to O(eta) tree-level) | Exploration |
| Can loop corrections cancel B/C to zero? | No (Clifford algebra identity is loop-exact) | Reconstruction |
| Does the 4D EFT RS sector become standalone? | No (coupling is kinematic, not dynamical) | Reconstruction |
| VZ verdict for 4D EFT? | EVADED (no standalone RS EFT arises) | Reconstruction |

### 6.2 Verdict

**F6 (4D EFT RS decoupling): CONDITIONALLY_RESOLVED.**

The 4D EFT RS sector does not become approximately standalone below M_KK. Three independent
arguments confirm this:

1. **KK mass scale argument.** The Codazzi correction shows `m_RS ~ M_KK`, so the RS and
   spin-1/2 sectors are integrated out at the same KK scale. There is no window below M_KK
   where a standalone RS EFT would be valid.

2. **Kinematic coupling argument.** The B/C blocks are Clifford-algebra-determined (kinematic),
   not dynamical coupling constants. The horizontal Clifford element `c_s(eta)` commutes with
   the KK projector, so the zero-mode B/C blocks are the same algebraic matrices as the
   full-theory blocks. They are O(1) (not suppressed) in the EFT.

3. **Loop stability argument.** Loop corrections to B/C are O(eta^2), subleading to the
   tree-level O(eta) kinematic coupling. The Clifford algebra identity `sigma_D(eta)^2 = xi^2 Id`
   is loop-exact and prevents B/C from being renormalized to zero.

**The VZ obstruction does not apply to the 4D EFT** for the same structural reason as in the
full 14D theory: the RS sector in GU is defined as the kernel of the Clifford gamma-trace on
D_GU, making it permanently entangled with the spin-1/2 sector by kinematic necessity.

### 6.3 Remaining Open Conditions

**RC1 (KK zero mode existence).** The Codazzi-corrected RS mass estimate (`m_RS ~ M_KK`)
assumes the RS sector has KK zero modes with finite mass. The existence of these zero modes
is gated on the discrete-series condition for `GL(4,R)/O(3,1)` (n5-discrete-series-gl4r,
OQ3a-c: CONDITIONALLY_RESOLVED). If no RS KK zero modes exist, there is no 4D RS sector
at all, and VZ is vacuously evaded but for a different reason.

**RC2 (Loop correction estimate).** The one-loop estimate in §5.4 is schematic (dimensional
analysis + leading-order counting). A full one-loop computation in the GU Sp(64) theory
(requiring the propagators and vertices in explicit form) has not been performed. The
conclusion that loop corrections are O(eta^2) and subleading relies on: (a) the B/C blocks
being linear in eta (established), and (b) propagators going as 1/m at zero momentum
(standard). These are reliable, but the claim is exploration-grade for the loop part.

**RC3 (Codazzi correction to M_KK).** The estimate `M_KK ~ 1/R_s` from the Frobenius
fiber metric is reconstruction-grade. An explicit computation of the normal Laplacian
`Delta_N` spectrum on `GL(4,R)/O(3,1)` (or its compactified approximation) is needed
to upgrade to verified. The Codazzi correction `Delta lambda_N ~ R^{perp}` is also
an estimate; the explicit Y^{14} curvature computation (flagged as the remaining ambient
curvature gate in CPA-1) is the common blocker.

**RC4 (Tachyonic RS modes).** The analysis assumes `m_RS^2 > 0` (no RS tachyons). As
noted in §19.6 of vz-schur-complement, a tachyonic RS mode (`m_RS^2 < 0`) would be a
vacuum instability, not a VZ causality problem. This is a separate question from F6; it
is equivalent to asking whether the GU vacuum is stable. The Willmore variational
principle selects the tachyon-free vacuum (K3-type section with II_s minimized), but
a dynamical stability analysis around this vacuum is outstanding.

---

## 7. Explicit Failure Conditions

**F6-C1.** If the B and C blocks are identically zero on the zero-mode subspace (i.e., if
`P_{(0)} c_s(eta) P_R = 0` for all `eta in T*X^4`), then the EFT RS sector would be
standalone and VZ would apply. This would require `c_s(eta)|_{E_s^{(0)}}` to preserve
`R_s^{(0)}` and `Q_s^{(0)}` separately. This is RULED OUT by the Clifford module identity:
a map satisfying `c(eta)^2 = g(eta,eta) Id` cannot separately preserve both `R` and `Q`
unless `R = 0` or `Q = 0` (trivial blocks). Neither is zero by the generation count
computation.

**F6-C2.** If loop corrections send `B^{(n)} -> 0` at some finite loop order n without
violating the Clifford algebra identity, the kinematic coupling argument fails. This would
require a quantum Ward identity (or symmetry) that protects the RS/spin-1/2 mixing
from receiving corrections while preserving the Clifford structure. No such symmetry is
present in GU (no separate RS number conservation); if one were discovered, it would
constitute a new structural finding that would need to be analyzed separately.

**F6-C3.** If the RS KK zero modes are tachyonic (`m_RS^2 < 0`), the vacuum is
unstable. While this is not a VZ causality issue, it would mean the reconstruction-grade
section (the K3 LC section) is not the physical vacuum, and the EFT analysis would need
to be redone around the true vacuum.

**F6-C4.** If the normal Laplacian `Delta_N` on `GL(4,R)/O(3,1)` has a zero mode (i.e.,
`M_KK = 0`), then the KK compactification breaks down and the effective 4D description
is invalid. This would require the fiber to be flat (zero curvature everywhere), which
is inconsistent with the Y^{14} construction (the fiber has curvature set by g_s).
Excluded by construction for any non-degenerate metric g_s.

---

## 8. Open Questions

**OQ-F6-1.** Explicit spectrum of `Delta_N` on `GL(4,R)/O(3,1)` (or its compact
approximation `SO(4)/SO(3) = S^3`). Does the spectrum give `M_KK ~ 1/R_s` as estimated,
or is there a parametric enhancement/suppression? This would concretize the KK gap estimate.

**OQ-F6-2.** A precise one-loop computation of the RS/spin-1/2 mixing propagator correction
`delta B^{1-loop}` in the Sp(64) theory, using the explicit D_GU propagators. This would
verify the O(eta^2) scaling and the claim that tree-level B dominates.

**OQ-F6-3.** Whether the massive RS zero modes (with `m_RS ~ M_KK`) acquire Yukawa-type
couplings to the SM fermions (spin-1/2 sector) through the B/C blocks evaluated at
`eta = 0`. If `B(0) = C(0) = 0` (which follows from B,C being linear in eta), then
the RS and spin-1/2 sectors are mass-decoupled at zero momentum but kinematically
coupled for all non-zero momenta. This is the correct picture: the RS sector is a
spin-3/2 partner of each SM generation, not coupled by a new dynamical Yukawa but by
the kinematic Clifford structure.

**OQ-F6-4.** Cross-check the KK mass gap estimate against the CPA-1 result
`Lambda_GU = lambda_max^2 = 1/t_obs^2`. If `M_KK^2 ~ Lambda_GU` (the Tikhonov
scale), then the KK gap, the section regularization scale, and the Hubble scale are
all at the same energy. This would be an important structural alignment.

---

## 9. References

- `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` §18-19 (4D VZ evasion CONDITIONALLY_RESOLVED, constant-coefficient gauge; F6 preliminary)
- `explorations/vz-evasion/vz-f5-curvature-check-2026-06-23.md` (curvature non-reintroduction CONDITIONALLY_RESOLVED)
- `explorations/vz-evasion/vz-oq1-sr-squared-identity-2026-06-23.md` (S_R^2 != xi^2 Id; B E^{-2} C explicit)
- `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md` (Codazzi for Sp(64); normal-bundle curvature R^perp)
- `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md` (gimmel Christoffels; fiber metric V)
- `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md` §12-19 (RS zero modes; ind_H = 8; OQ3a-c)
- `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md` (Lambda_GU = lambda_max^2; M_KK alignment)
- `explorations/geometry-curvature-emergence/ic3-nonlinear-conservation-2026-06-23.md` (Bianchi identity; normal curvature conservation)
- `explorations/geometry-curvature-emergence/hc1-sl2c-bianchi-spinor-2026-06-23.md` (hidden curvature H^{(i)} SL(2,C) labels)
- Velo, G. and Zwanziger, D. (1969). Phys. Rev. 186:1337. (Classical VZ; standalone RS assumption)
- Hormander, L. (1985). The Analysis of LPDOs III, Ch. 23. (Propagation of singularities)
- Kaluza, T. (1921); Klein, O. (1926). (KK compactification; mass tower)
- Flensted-Jensen, M. (1980). Ann. Math. 111:253. (Discrete series; multiplicity-one at split-rank 1)
