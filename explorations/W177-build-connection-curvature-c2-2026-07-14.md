---
artifact_type: exploration
label: W177
status: exploration (W177 / BUILD-CURVATURE; 5-persona inline team; one deterministic test 17/17 exit 0; the coherence-first build of W173's residual object)
created: 2026-07-14
branch: "Team W177 (BUILD-CURVATURE): build the connection-curvature 2-form F_A of the W131 Y14 connection algebraically (Cl(9,5) rep-theory + ker-Gamma), and determine whether it closes the secondary constraint C2 = Gamma.M_D.Pi_RS (=155.36) by selecting a distinguished null plane."
title: "W177 VERDICT: DOES-NOT-CLOSE-C2 (needs external non-metric datum). The connection-curvature 2-form F_A of the W131 gimmel Levi-Civita connection is BUILT at a curved point of Y14 = Met(X4) (Riemann curvature, frame-projected, lifted to the Cl(9,5) rep), is nonzero (||Omega|| = 8.12: Y14 is genuinely curved), and is so(9,5)-VALUED (the fully-lowered frame curvature Omega_ab is antisymmetric to finite-diff precision 3.9e-7; the holonomy algebra sits in so(9,5)). BECAUSE it is so(9,5)-valued it inherits W131's exact leakage theorem: [F_A, Pi] = 0 and Gamma F_A Pi = 0 (leakage-free, numeric witness 2e-6, EXACT for all so(9,5) generators to 3e-14). C2 = Gamma.M_D.Pi_RS is Gamma-INDEPENDENT (its residual against Gamma equals its full norm 155.36) -- i.e. transverse to the so(9,5) action -- so NO metric-compatible curvature dressing can move it: dressing C2 by the curvature holonomy exp(t F_A) leaves the Gamma-independent residual at O(155) for all t (never approaches 0), reproducing bicomplex's 'C2 survives and grows under every carrier' now for the ACTUAL curvature, not a-priori named connections. F_A also does NOT select a distinguished null plane: it treats the 4 fiber-timelike directions symmetrically (curvature-charge relative spread 0.12) in a base(1)+fiber(4) pattern, so it does not break the 5-fold null-pair symmetry to one plane -> it does NOT force the SG4 carrier declaration (A vs B). The object C2 needs is a SYMMETRIC, NON-metric datum outside so(9,5) (W131's C3b protection boundary: eta.II_sym is not antisymmetric; such an insert DOES leak, 10.9 vs F_A's 2e-6, a 6-order separation) -- external, per the program's standing thesis. NET: the record reading (W173) is CONFIRMED-not-demoted (no GU-native geometric object pairs the mirror into a BV doublet); bar(b) stays RECORD (Krein grading OPERATIVE); the generation count stays at the measured 2-bit SG4 residual."
grade: "BUILT the curvature (COMPUTED: Riemann of the explicit gimmel metric at a curved Lorentzian point, frame-projected, lifted to the verified Cl(9,5)=M(64,H) rep; ||Omega||=8.12, so(9,5)-antisymmetry 3.9e-7, all finite-diff numeric witnesses at native n=4 exactly as W131 Block B/C). The DECISIVE closure result is EXACT: Gamma rho(w) Pi = 0 for every so(9,5) generator w (3e-14, reusing W131 A5), so the leakage-free property of F_A is a THEOREM (F_A in so(9,5) => cannot touch the Gamma-independent C2), the finite-diff F_A being a witness (2e-6) that the actual curvature obeys it. C2=155.3625, bare 58.7215, RS transversality 343.73 reproduced to anchor precision. STRUCTURAL for the null-plane symmetry (numeric charges, one curved point). ARGUED for the field-space non-forcing (rests on the null-plane symmetry + the leakage theorem). No canon / claim-status / verdict / posture change. The mirror being a record stays OPEN exactly as far as the Y14 source-action is unbuilt; this wave removes ONE candidate closer (the metric-compatible curvature) and confirms the external-source thesis on that candidate."
depends_on:
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/anomaly-and-bordism/bv-bicomplex-and-c2-obstruction-2026-06-27.md
  - explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md
  - explorations/W125-source-action-first-build-2026-07-13.md
  - canon/shiab-existence-cl95.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
scripts:
  - tests/W177_connection_curvature_c2.py
cross_repo:
  - "time-as-finality: bears on T507-T509 (records-vs-redundancy). W173 relocated bar(b) onto the Y14-curvature question; W177 computes that curvature and finds it CANNOT demote the mirror -- confirming the record lean, still conditional on the unbuilt non-metric datum. One-way rule respected: no GU claim moves, no TaF claim moves, no identity claimed."
---

# W177 -- the connection-curvature 2-form F_A on Y14: does it close C2?

**Role and framing.** W173 (BRST cohomology of the mirror) found that GU's determined content
leans RECORD (the mirror is closed-not-exact in the built free BV bicomplex), and that the ONLY
object that could demote it to redundancy is the secondary constraint **C2 = Gamma . M_D . Pi_RS**
(= 155.36, Gamma-independent), which does NOT close without the **UNBUILT Y14 connection-curvature
2-form** that selects a distinguished null plane. `bv-bicomplex-and-c2-obstruction` had already
named that same object as the grand convergence point of the whole arc, and proved a flat-connection
**holonomy** cannot supply it. W131 built the connection A (gimmel Levi-Civita spin lift) and proved
`[nabla, Pi] = 0`, but did NOT compute its curvature. This wave builds the curvature and asks the one
decisive question: **does F_A close C2?**

The answer is clean and negative-for-closure, and it is decided by a structure W131 already made
exact: the curvature of a metric-compatible connection is **so(9,5)-valued**, and C2 is
**Gamma-independent** (transverse to the so(9,5) action). Five personas ran inline; deterministic test
`tests/W177_connection_curvature_c2.py`, 17/17, exit 0.

## 0. Scope: what 2-form, and what "closes C2" means

**The 2-form.** F_A is the curvature `F_A = dA + A ^ A` of the W131 connection A = the gimmel
Levi-Civita spin lift on the RS bundle `T*Y14 (x) S(9,5)` over Y14 = Met(X4). Concretely it is the
Riemann curvature 2-form of the explicit gimmel metric (base block h with signature (3,1); trace-reversed
DeWitt fiber block with signature (6,4)), frame-projected to a gimmel-orthonormal frame and lifted to the
representation: `F_A = rho(R)`, `R` the frame Riemann tensor valued in so(9,5). Restricted/projected to
the ker-Gamma record sector by the constant equivariant projector Pi.

**"Closes C2."** C2 is the BRST-invariance of the dynamics M_D (the RS Dirac symbol), the true
secondary Velo-Zwanziger-type constraint isolated by `bv-bicomplex`. "Closes C2" = the curvature
selects a **distinguished null plane / spectral section** that drives C2 to 0 on the physical sector,
which would either (i) pair `(generation, mirror)` into a BV doublet (demote the mirror to REDUNDANCY),
or (ii) fix the field-space declaration (carrier A vs B, the 2-bit SG4 residual).

## 1. Persona 1 -- Cl(9,5) rep-theory: F_A on the record bundle, and the leakage theorem

The curvature is built and lifted through the exact so(9,5) machinery W131/W173 used (the verified
`Cl(9,5) = M(64,H)` rep). Two rep-theory facts do all the work:

- **F_A is so(9,5)-valued.** In a gimmel-orthonormal frame the fully-lowered frame curvature
  `Omega_ab(K,L)` is ANTISYMMETRIC in the frame indices `(a,b)` (test F2: global relative
  `||Omega + Omega^T|| / ||Omega|| = 3.9e-7`, finite-diff witness). Its so(9,5) generator form
  `w = eta . Omega` then has `eta . w` antisymmetric (F3), so `w in so(9,5)` and
  `F_A = rho(w) = kron(w, I_S) + kron(I_V, sigma(w))` is a genuine RS-bundle image of an so(9,5) element.
- **so(9,5) is leakage-free on ker Gamma (W131 A5, reused EXACT here).** For EVERY so(9,5) generator w,
  `Gamma rho(w) Pi = Sigma (Gamma Pi) = 0`. Test D4 reproduces this to **3e-14** on 6 random so(9,5)
  elements of the curvature type. Consequently the ACTUAL built curvature satisfies `[F_A, Pi] = 0`
  (D1, 7e-7) and `Gamma F_A Pi = 0` (D2, 2e-6) to finite-difference precision.

So the curvature acts **within** the record sector and produces **zero gamma-trace leakage**. This is the
rep-theoretic wall.

## 2. Persona 2 -- BV/BRST: why leakage-free means C2-invariant (no doublet pairing)

C2 = Gamma . M_D . Pi_RS is **Gamma-INDEPENDENT** (test P3: its residual against Gamma equals its full
norm 155.36) -- it is transverse to the gauge/so(9,5) action, which is exactly why `bv-bicomplex` found
it survives every carrier. Dressing the constraint by the curvature holonomy `B = Gamma . (I (x) exp(t F_A))`
and recomputing the dressed secondary constraint `C2_dressed = B . M_D . Pi_ker(B)`: its Gamma-independent
residual stays at **O(155) for all t in {0.25, 0.5, 1, 2}** (test D3: 155.2, 155.1, 155.0, 154.9), never
approaching 0. This reproduces `bv-bicomplex`'s "C2 survives and grows under every carrier" now for the
**actual computed curvature**, not just a-priori named connections. The BV reading: the curvature does not
supply the differential that would pair `(generation, mirror)` into a doublet/quartet, so the mirror is
NOT demoted. The demotion channel W173 identified stays closed under the metric curvature.

## 3. Persona 3 -- differential geometer: F_A is real but symmetric across the null pairs

The build confirms Y14 is genuinely curved: at a curved Lorentzian point the frame Riemann 2-form has
`||Omega|| = 8.12` (test F1), so there IS a curvature to use -- the failure to close is not "the space is
flat." But the geometry of Met(X4) with the DeWitt supermetric is a homogeneous/symmetric-space geometry,
and its curvature does not break the residual symmetry among the timelike directions. Test N1 computes the
curvature "charge" coupling each of the 5 frame-timelike directions: a **base(1) + fiber(4)** pattern with
the 4 fiber-timelike charges near-equal (`[2.14, 1.76, 2.49, 2.20]`, relative spread 0.12) and the base
one distinct (0.976). The curvature distinguishes base-time from fiber-time (the product structure), but
does **not single out ONE null plane** among the fiber directions. So it cannot supply the single
distinguished null plane C2 needs, and it does not force the SG4 carrier declaration (N2): the measured
2-bit SG4 residual (`canon/gu-forces-field-space-declaration`, B-leaning) survives.

## 4. Persona 4 -- symbolic engineer: the test, controls, exit code

`tests/W177_connection_curvature_c2.py`, 17/17, exit 0, deterministic (seed 20260714). Positive controls,
per mandate:

- **Anchors reproduced (Block P):** C2 = 155.3625 (P1), bare `||[Pi, M_D]|| = 58.7215` (P2), C2
  Gamma-independence 155.36 (P3), RS transversality **343.73** via the chirality-split construction
  (P4, `im(d_A)` escapes ker Gamma -- W173 Part 1 machine fact), W131 crux `[rho(J), Pi] = 0` on a boost
  (P5, 0.0).
- **The curvature BUILT (Block F):** gimmel-orthonormal frame (F0, 4.9e-15), `||Omega|| = 8.12 != 0`
  (F1), so(9,5)-antisymmetry (F2, 3.9e-7), representative generator in so(9,5) (F3).
- **Decisive (Block D):** `[F_A, Pi] = 0` (D1), `Gamma F_A Pi = 0` (D2), holonomy dressing does not close
  (D3), and the EXACT theorem `Gamma rho(w) Pi = 0` for all so(9,5) w to 3e-14 (D4).
- **Adversarial positive control (Block A):** a NON-metric SYMMETRIC insert is OUTSIDE so(9,5) (A1,
  `eta . II_sym` not antisymmetric) and DOES leak `Gamma . insert . Pi = 10.9` (A2) -- the RIGHT TYPE of
  object that could close C2 exists, 6 orders above F_A's leakage, and it is external / non-metric.

Honesty: the curvature is a **finite-difference** computation at native n = 4 (numeric witness ~1e-6,
exactly as W131 treats its Block B/C geometry); the DECISIVE content (D4) is EXACT algebra on the verified
rep. No number was reverse-engineered; the 5-fold-symmetry finding and the leakage separation are read off,
not fitted.

## 5. Persona 5 -- adversarial skeptic: steelman STILL-NEEDS-EXTERNAL

**The steelman (the program's standing thesis, now sharpened).** The right way to read this is not "we
failed to close C2" but "we proved the metric-compatible curvature is the wrong KIND of object to close
it." The wall is algebraic and exact: metric compatibility forces F_A into so(9,5); so(9,5) is
leakage-free on ker Gamma (W131); C2 is Gamma-independent; therefore no so(9,5)-valued dressing can move
it. This is the SAME wall that appears in `bv-bicomplex` (flat holonomy floor 41.04 > spurion, never 0),
in the KSp class (H-symmetric, cannot break the 5-fold symmetry), and in W131 C3a/C3b (curvature inserts
are subprincipal; the dangerous insert is a SYMMETRIC first-order term OUTSIDE so(9,5) that
metric-compatible covariantization can never generate). W177 closes the last open candidate on the
GU-native geometric side: the actual curvature. The datum that WOULD close C2 -- a symmetric, non-metric,
gamma-trace-breaking spectral section -- is exactly the external boundary datum GU's native geometry
cannot supply (test A2 exhibits its TYPE and its nonzero leakage). Can the skeptic claim F_A closes C2 by
some cleverer dressing? No: D4 is a theorem over the whole algebra, not a sampled miss.

**The counter (why this is not the end of the record reading either).** This does not PROVE the mirror is
a record; it proves no GU-native metric curvature DEMOTES it. The record verdict still rides on the
external non-metric datum staying absent or record-confirming, exactly as W173 left it. Symmetric honesty:
the metric-native side is now exhausted on this candidate; the decision remains at the boundary.

## 6. Verdict

**DOES-NOT-CLOSE-C2 -- needs an external, non-metric (symmetric, gamma-trace-breaking) datum.**

- The connection-curvature 2-form **F_A is BUILT** at a curved point of Y14 (Riemann of the gimmel
  metric, frame-projected, lifted to Cl(9,5)), is **nonzero** (`||Omega|| = 8.12`), and is
  **so(9,5)-valued** (antisymmetry 3.9e-7).
- **It does not close C2.** Being so(9,5)-valued it is leakage-free (`Gamma F_A Pi = 0`; EXACT for all
  so(9,5) generators, 3e-14), and C2 is Gamma-independent, so every curvature dressing leaves C2's
  residual at O(155) (never 0). No BV doublet pairing is supplied: **the mirror is NOT demoted.**
- **It does not force the field-space declaration.** F_A treats the 4 fiber-timelike directions
  symmetrically (spread 0.12), selecting no distinguished null plane; the 2-bit SG4 carrier residual
  (A vs B) survives.

**Which declaration does it select?** None. The metric-compatible curvature is symmetric across the null
pairs; it neither picks carrier A nor B. The SG4 residual stays as `gu-forces-field-space-declaration`
measured it (B-leaning, not forced).

**Effect on `bar(b)` and the generation count.** `bar(b)` stays **RECORD** (Krein grading OPERATIVE):
W177 confirms W173's lean by removing the only GU-native geometric object that could have demoted the
mirror to redundancy. The generation count is unchanged -- it stays at the measured 2-bit SG4 residual;
the curvature does not supply the boundary datum that would fix it. Both remain jointly relocated onto the
same external, non-metric spectral section, precisely the program's standing external-source thesis, now
with the metric-native candidate exhausted.

## 7. What this does NOT do

No canon change; no claim / RESEARCH-STATUS / verdict / posture change. The mirror being a record stays
OPEN exactly as far as the Y14 source-action (the non-metric datum) is unbuilt. No cross-repo identity
claim (one-way rule respected). The curvature is a finite-difference numeric witness at one curved point,
not a global theorem about all of Met(X4); the EXACT content is the so(9,5) leakage theorem (D4). No
construction of S_IG, no closure of C2, no generation count. The null-plane-symmetry finding is one curved
point at native n = 4, argued not proved to hold globally.

**Artifacts:** this file + `tests/W177_connection_curvature_c2.py` (17/17, exit 0).
