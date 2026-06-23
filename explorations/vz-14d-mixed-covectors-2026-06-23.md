---
title: "VZ Evasion for Mixed 14D Covectors: Synthesis and Verdict"
date: 2026-06-23
problem_label: "vz-14d-mixed"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
vz_evasion_status: CONDITIONALLY_EVADED
proof_grade: reconstruction
correction: "2026-06-23 VZ-01: vz_evasion_status downgraded from EVADED to CONDITIONALLY_EVADED. The Schur complement proof in §4 uses E^{-1} whose existence it does not independently establish. The det(M)=det(E)*det(S_R) identity requires E invertible as a precondition and cannot be used to prove E invertible without circularity. E(xi) invertibility must be proved directly from the Clifford algebra for all xi with g_Y(xi,xi) != 0."
vz01_closure: "2026-06-23: direct Clifford algebra argument provided in explorations/vz-e-block-direct-clifford-2026-06-23.md (reconstruction grade); upgrade to EVADED requires verification outside the session loop. The proof uses the 2x2 block form and gamma(xi)^2=xi2 Id in Cl(9,5)=M(64,H), but does not exhibit a fully explicit matrix computation or reference a verified theorem. A circularity flag resolved by a same-session reconstruction-grade file is methodologically unsound; status remains CONDITIONALLY_EVADED pending external verification."
---

# VZ Evasion for Mixed 14D Covectors: Synthesis and Verdict

## 1. Problem Statement

For a general 14D covector `xi = xi_H + xi_V` where

```
xi_H in H* (signature (3,1), horizontal / 4D spacetime directions)
xi_V in N* (signature (6,4), vertical / fiber directions)
xi = xi_H + xi_V,   xi2 := g_Y(xi, xi) = g_H(xi_H,xi_H) + g_N(xi_V,xi_V)
```

does the Rarita-Schwinger (RS) sector of the GU principal symbol decouple from the
non-RS sector? Specifically:

1. Does the effective RS principal symbol `D_RS_eff(xi) = S_R(xi) = A(xi) - B(xi) E(xi)^{-1} C(xi)` have trivial kernel for all `xi2 != 0`?
2. Does VZ evasion hold for the full 14D covector `xi = xi_H + xi_V`?
3. What is the correct statement of VZ evasion (is `S_R^2 = xi2 Id` or a weaker identity)?

This file synthesizes the results of the full VZ exploration chain completed 2026-06-23.

---

## 2. Geometry and Setup

**Geometry:** `Y^14 = Met(X^4)`, signature `(9,5)`, fiber `GL(4,R)/O(3,1)`.

At a section `s: X^4 -> Y^14`, the cotangent space splits:

```
T*Y|_s = H* direct-sum N*
dim H* = 4 (sig (3,1), horizontal)   dim N* = 10 (sig (6,4), vertical)
g_Y(xi_H, xi_N) = 0    (block-diagonal metric in product coordinates)
```

**Clifford algebra:** `Cl(9,5) ~= M(64,H)`, spinor module `S = H^{64}`, `dim_R S = 256`.

The Clifford identity:

```
c(xi)^2 = g_Y(xi, xi) * Id_S = xi2 * Id_S    for all xi in T*Y^14.   (Cl)
```

**RS sector:** The 14D Rarita-Schwinger sector is

```
R^{14D} = ker Gamma^{14D},   Gamma^{14D}(psi) = gamma^A psi_A   (sum over all 14 frame directions).
dim_R R^{14D} = 13 * 256 = 3328.
```

**Operator:** `D_GU` is a Dirac-type operator on

```
E = (Omega^0(Y^14) tensor S^+) direct-sum (Omega^1(Y^14) tensor S^-)
```

with principal symbol `sigma_{D_GU}(xi) = M(xi): E -> E` satisfying `M(xi)^2 = xi2 * Id_E` (from (Cl)).

---

## 3. Block Structure at a Mixed Covector

At `xi = xi_H + xi_V` with both parts nonzero, decompose `E = R^{14D} direct-sum Q` where
`Q = E_0 direct-sum Q^{14D}` (scalar spinors and gamma-trace one-forms). The principal
symbol has block form:

```
M(xi) = [ A(xi)  B(xi) ]    with  M(xi)^2 = xi2 Id_E.
         [ C(xi)  E(xi) ]
```

The four block-square identities follow from `M^2 = xi2 Id`:

```
(I)   A^2 + BC = xi2 Id_R
(II)  AB + BE  = 0
(III) CA + EC  = 0
(IV)  CB + E^2 = xi2 Id_Q
```

**Explicit computation of C block (§3.1 of vz-schur-complement-2026-06-23.md).**

For `psi_R in R^{14D}` (gamma-trace-free), let `chi = g_Y(xi, psi_R)`. Then:

```
C psi_R = (chi, (gamma(xi) - 2) chi)   in Q_0 direct-sum Q_T.
```

The C block is nonzero for generic `xi` and generic `psi_R`. This confirms the RS sector
is coupled to the non-RS sector by the off-diagonal block C.

**Mixed covector structure.** For `xi = xi_H + xi_V`:

```
chi = g_Y(xi, psi_R) = g_H(xi_H, psi_{R,H}) + g_V(xi_V, psi_{R,V})
```

This has contributions from both horizontal and vertical components of `psi_R`. The mixing is
not eliminated by restricting to horizontal or vertical covectors separately -- the full 14D
coupling is generically nonzero for mixed covectors.

---

## 4. Main Theorem: VZ Evasion for All Non-Null 14D Covectors

**Theorem (reconstruction grade).** For all `xi in T*Y^{14}` with `g_Y(xi, xi) != 0`:

```
ker S_R^{14D}(xi) = 0.
```

Equivalently, the 14D effective RS principal symbol `D_RS_eff(xi) = S_R(xi)` has trivial kernel
for all non-null 14D covectors, including mixed covectors `xi = xi_H + xi_V`.

**Proof.** The argument is structural and relies only on the Clifford module identity (Cl).

Step 1. Suppose `S_R(xi) psi_R = 0` for some `psi_R in R^{14D}`.

Step 2. By definition of the Schur complement:

```
M(xi) (psi_R, -E^{-1} C psi_R) = (A psi_R - B E^{-1} C psi_R, C psi_R - C psi_R)
                                 = (S_R psi_R, 0) = (0, 0).
```

Step 3. Apply `M(xi)` to the zero vector:

```
0 = M(xi)(0, 0) = M(xi)^2 (psi_R, -E^{-1} C psi_R) = xi2 (psi_R, -E^{-1} C psi_R).
```

Step 4. Since `xi2 != 0`:

```
(psi_R, -E^{-1} C psi_R) = 0   =>   psi_R = 0.
```

This uses the Clifford module identity `M(xi)^2 = xi2 Id_E` in Step 3. The conclusion
`psi_R = 0` is forced for any non-null covector, including mixed covectors. QED.

**Remark.** The proof applies verbatim to mixed covectors because (Cl) holds for all
`xi in T*Y^{14}` and the block decomposition is valid globally on `E`. No restriction
to horizontal or vertical covectors is needed.

**Invertibility of E — PRECONDITION FAILURE (VZ-01, 2026-06-23).**

The proof uses `E^{-1}` in Step 2 without first establishing that `E(xi)` is invertible.
The block determinant identity `det(M) = det(E) * det(S_R)` holds ONLY when `E` is
invertible and `S_R` is the Schur complement. It cannot be inverted to conclude `E` is
invertible: the identity is a consequence of `E` being invertible, not a proof of it.

The attempt to use `det(M)^2 = xi2^{dim E} != 0` (from (Cl)) to conclude `det(E) != 0` is
circular: that factorisation requires `E` invertible as a precondition. If `E(xi)` has a
null vector for some `xi` with `xi2 != 0` (e.g., for covectors with nontrivial fiber
components near a null-fiber direction), the entire Schur complement construction fails
before Step 2, and Steps 3-4 do not apply.

**What is needed to close the gap.** A direct proof — from the Clifford algebra of `Cl(9,5)`
acting on `Q = E_0 + Q^{14D}` — that `E(xi)` has trivial kernel for all `xi` with
`g_Y(xi,xi) != 0`. This requires an explicit computation of the Q-block Clifford action,
not a determinant identity. Until this is supplied, the proof in Steps 1-4 is valid only
CONDITIONALLY on E-invertibility, and the verdict is `CONDITIONALLY_EVADED`, not `EVADED`.

**Consequence for the verdict.** VZ evasion at the 14D mixed-covector level is demoted from
`EVADED` to `CONDITIONALLY_EVADED`. The 4D section-pullback result (OQ3-V1/V2/V3, VERIFIED)
and the structural Clifford module non-decoupling argument are unaffected; those arguments
do not rely on Schur complement block-inversion in Q.

---

## 5. Exact vs Approximate Matrix Identity

**OQ1 resolution (from vz-oq1-sr-squared-identity-2026-06-23.md).**

The stronger identity `S_R^2 = xi2 Id_{RS}` does NOT hold as an exact matrix identity.

From the block-square calculation:

```
S_R^2 = xi2 Id_R + xi2 B E^{-2} C.
```

Explicit computation of `B E^{-2} C psi_R` for 14D (using the 14D E-matrix
`E = gamma(xi) * [[0, 1/14], [1, 13/7]]` and corrected B-block formula) gives:

```
(B E^{-2} C psi_R)_A = (1/7 xi2) xi_A [2842 chi - 98 mu] + (1/xi2) gamma_A [-(203/7) mu + xi2 chi]
```

where `chi = g_Y(xi, psi_R)` and `mu = gamma(xi) chi`. This is manifestly nonzero for
generic `xi2` and generic `chi`.

> **[RECONSTRUCTION GRADE — OQ-RS-1 PENDING]** The numerical coefficients `2842`, `98`,
> and `203/7` in the formula above are sourced from a reconstruction-grade computation in
> `vz-oq1-sr-squared-identity-2026-06-23.md`, which has not yet been committed to the repo
> and cannot currently be independently verified. No in-line derivation trace is present in
> this file. These coefficients must be treated as unverified pending CAS confirmation under
> OQ-RS-1 (see §8). The conclusion that `B E^{-2} C != 0` is expected to survive CAS
> verification (the nonvanishing is structural for generic xi), but the explicit coefficient
> values should not be cited as authoritative until CAS verification is complete.

**Correct statement.** The exact matrix identity that holds is:

```
A S_R = S_R A = xi2 Id_R    (exact, from block-square identities (I) and (II)/(III))
```

This is a consequence of `A^2 + BC = xi2 Id` and `AB = -BE`. It shows that A is a
left/right inverse of S_R up to the scalar `xi2`, and the full-symbol A-block entangles
S_R essentially with the non-RS sector. The RS sub-bundle is NOT a sub-Clifford-module
(Clifford multiplication `c(xi)` does not preserve `ker Gamma^{14D}`), which is precisely
why VZ evasion holds: the RS sector cannot propagate as a standalone field.

---

## 6. Physical Interpretation: Why VZ Is Evaded

The VZ theorem (Velo-Zwanziger 1969) assumes:

- **H1.** The RS field is described by a standalone RS Lagrangian.
- **H2.** The RS field is minimally coupled to a nontrivial gauge background.
- **H3.** No guardian symmetry protects causality.

The GU construction violates H1: the RS sector is the kernel of the full 14D gamma trace
applied to the Clifford module bundle E for D_GU. It is not a standalone field -- it is
a direct summand of the Clifford module bundle, permanently coupled to the spin-1/2 sector
via off-diagonal blocks B and C.

The Schur complement operation (integrating out the spin-1/2 Q sector) gives the effective
RS propagator `S_R(xi)`. The theorem in §4 establishes that `S_R(xi)` has trivial kernel
for all non-null `xi`, which is equivalent to: the characteristic cone of the effective RS
symbol is contained in the null cone `{xi : g_Y(xi,xi) = 0}`. No spacelike characteristics
exist. VZ acausality cannot arise.

**Mechanism:** The VZ evasion is not due to a guardian symmetry (H3 might hold) but to
Clifford module non-decoupling. The Clifford identity (Cl) propagates through the Schur
complement to guarantee causal characteristics, because the entanglement with the spin-1/2
sector (via B and C) cannot be removed at any energy scale -- the coupling is kinematic
(determined by the Clifford algebra), not dynamical.

---

## 7. Full Chain of VZ Results

| Item | Verdict | File |
|---|---|---|
| Horizontal covectors `xi_H`: `ker S_R = 0` | CONFIRMED (explicit) | vz1-schur-complement-symbol (prior) |
| Vertical one-forms: no change to horizontal Schur | CONFIRMED (structural) | vz1-schur-vertical-extension (prior) |
| Full 14D mixed covectors `xi = xi_H + xi_V`: `ker S_R^{14D}(xi) = 0` | CONDITIONALLY_EVADED (reconstruction) — proof assumes E invertible; E invertibility not independently proved | vz-schur-complement-2026-06-23.md §8 |
| E block invertible for `xi2 != 0` | CONDITIONALLY_RESOLVED — direct Clifford argument provided (reconstruction grade, same-session file); explicit E^{-1} not fully verified; upgrade to RESOLVED requires external verification of vz-e-block-direct-clifford-2026-06-23.md | vz-e-block-direct-clifford-2026-06-23.md |
| `S_R^2 = xi2 Id` as exact matrix identity | FALSE (explicit `B E^{-2} C != 0`) | vz-oq1-sr-squared-identity-2026-06-23.md |
| Correct identity: `A S_R = xi2 Id_R` | TRUE (exact, block-square) | vz-oq1-sr-squared-identity-2026-06-23.md |
| Lower-order curvature (14D): zero-order, no new characteristics | CONDITIONALLY_RESOLVED | vz-oq2-lower-order-curvature-2026-06-23.md |
| Subprincipal symbol: no sub-characteristics | CONDITIONALLY_RESOLVED | vz-subprincipal-symbol-rs-2026-06-23.md |
| OQ3-V1: no anomalous normal terms in `s*(sigma)` | RESOLVED | vz-schur-complement-2026-06-23.md §18.1 |
| OQ3-V2: 4D E-block invertible (`det = -1/4`) | RESOLVED | vz-schur-complement-2026-06-23.md §18.2 |
| OQ3-V3: `R_s = ker Gamma^{4D}` identification | RESOLVED | vz-schur-complement-2026-06-23.md §18.3 |
| 4D section-pullback VZ evasion | VERIFIED | vz-schur-complement-2026-06-23.md §17-18 |
| F5: 4D curvature non-reintroduction | CONDITIONALLY_RESOLVED | vz-f5-curvature-check-2026-06-23.md |
| F6: 4D EFT decoupling (B/C kinematic, loop-exact) | CONDITIONALLY_RESOLVED | vz-f6-eft-decoupling-2026-06-23.md |

**Overall VZ verdict: CONDITIONALLY_EVADED (reconstruction grade) with 4D evasion VERIFIED.**

The E(xi) invertibility precondition has a direct Clifford algebra argument in
`explorations/vz-e-block-direct-clifford-2026-06-23.md` (2026-06-23, reconstruction grade),
but this file was produced in the same session loop as the circularity flag (VZ-01) and has
not been externally verified. A same-session reconstruction-grade file does not constitute
independent closure of a circularity. Status remains CONDITIONALLY_EVADED until external
verification of the E-block proof. The 4D section-pullback result (OQ3-V1/V2/V3) is
unaffected and remains VERIFIED.

---

## 8. Remaining Open Questions

**OQ-RS-1 (Clifford trace CAS).** Verify `Tr_S(c(u) c(v)) = 256 g_Y(u,v)` explicitly
in the M(64,H) representation via CAS computation. This underpins the E-matrix formula
and the B-block derivation. Also covers CAS verification of the explicit coefficients
`2842`, `98`, `203/7` appearing in the `B E^{-2} C` formula in §5 (sourced from
`vz-oq1-sr-squared-identity-2026-06-23.md`, not yet in repo; see reconstruction-grade
warning in §5). Status: CONDITIONALLY_RESOLVED (reconstruction; three methods) — explicit
coefficients remain UNVERIFIED pending CAS.

**OQ-RS-2 (Loop corrections).** Are the off-diagonal B/C coupling blocks modified at
one loop? Structural argument (vz-f6): B/C are kinematic (Clifford-algebra-determined)
and the Clifford identity `sigma_D^2 = xi2 Id` is loop-exact. One-loop CAS computation
of the B/C blocks has not been performed.

**OQ-RS-3 (GU-Vasiliev comparison).** Does the GU RS embedding strategy (Leibniz
cross-term as RS definition) provide a new class of consistent higher-spin theories,
distinct from Vasiliev's higher-spin gravity? This is P53-NOVEL; remains open.

**OQ-RS-4 (Noncompact bounded-transform).** Full Fredholmness on noncompact `Y^14`
requires b-calculus or scattering parametrix construction. Blocked on: bounded-transform
continuity for GU operators in `Fred_H` (H-linear Fredholm spaces). Status: G3 gap from
OC2.

---

## 9. Verdict

**Verdict: CONDITIONALLY_RESOLVED** (supersedes earlier OPEN status for mixed covectors).

**VZ evasion status: CONDITIONALLY_EVADED** (CR-04 correction 2026-06-23: premature upgrade to EVADED reverted).

The E(xi) invertibility precondition has a direct Clifford algebra argument in
`explorations/vz-e-block-direct-clifford-2026-06-23.md`, but that file was produced in the
same session loop as the VZ-01 circularity flag and constitutes reconstruction-grade work
without external verification. Methodological requirement: a circularity flag cannot be
closed by a same-session reconstruction-grade reconstruction. The `det(M) = det(E)*det(S_R)`
circular step in the original §4 proof has a proposed replacement (direct kernel argument:
E(xi)(phi, j(s)) = 0 implies gamma(xi)^2 s = xi2 s = 0 implies s = 0 for xi2 != 0), and
an explicit inverse E^{-1} = [[-(26/xi2)G,(14/xi2)G],[(14/xi2)G,0]] is proposed, but
neither has been externally verified. Status remains CONDITIONALLY_EVADED.

**Open precondition.** For all `xi in T*Y^{14}` with `g_Y(xi,xi) != 0`, the operator
`E(xi): Q -> Q` has trivial kernel. CONDITIONALLY_RESOLVED (reconstruction grade, same-session
argument in `explorations/vz-e-block-direct-clifford-2026-06-23.md`); upgrade to RESOLVED
requires: (FC1) independent external verification of the 2x2 block kernel argument; (FC2)
explicit CAS computation confirming the E^{-1} formula; (FC3) confirmation that the
failure locus is exactly the null cone and no non-null xi produces a zero eigenvalue of E.

The 4D section-pullback result (OQ3-V1/V2/V3, VERIFIED) is unaffected.

**Evasion mechanism (structurally intact).** Clifford module non-decoupling: the RS sub-bundle
is not a sub-Clifford-module of E, so the RS sector is essentially entangled with the spin-1/2
sector, preventing standalone RS propagation. The identity `A S_R = xi2 Id_R` (exact) encodes
this entanglement.

---

## 10. References

- `explorations/vz-schur-complement-2026-06-23.md` (main Schur computation; §8 kernel argument; §17-18 4D pullback; OQ3-V1/V2/V3 RESOLVED; verdict: CONDITIONALLY_EVADED — see VZ-01 correction in this file §4 and §9)
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md` (OQ1 resolved: `S_R^2 != xi2 Id`; `A S_R = xi2 Id` is correct; `B E^{-2} C != 0` explicit)
- `explorations/vz-oq2-lower-order-curvature-2026-06-23.md` (OQ2: curvature terms zero-order; CONDITIONALLY_RESOLVED)
- `explorations/vz-subprincipal-symbol-rs-2026-06-23.md` (OQ2-b subprincipal: no sub-characteristics; CONDITIONALLY_RESOLVED)
- `explorations/vz-f5-curvature-check-2026-06-23.md` (F5: 4D curvature non-reintroduction; CONDITIONALLY_RESOLVED)
- `explorations/vz-f6-eft-decoupling-2026-06-23.md` (F6: EFT decoupling; CONDITIONALLY_RESOLVED)
- Velo and Zwanziger (1969), Phys. Rev. 186:1337
- Lawson-Michelsohn, _Spin Geometry_, Ch. II §6 (Clifford module structure)
- Hormander, _The Analysis of Linear Partial Differential Operators_, Vol. III, §23.2 (propagation of singularities)
