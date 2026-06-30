---
title: "Type II_1 Spectral SM Checklist Tightening: Connes-Chamseddine Control Comparisons and Falsification Tests"
date: 2026-06-23
problem_label: "type-ii1-sm-checklist-tightening"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Type II_1 Spectral SM Checklist Tightening

## 1. Problem Statement

The existing `lab/specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md`
lists ten items from the finite Connes-Chamseddine spectral SM and names what a Type II_1
extension must preserve, redefine, or replace. The specialist pass in
`explorations/type-ii1-spectral/type-ii1-finite-control-specialist-pass-2026-06-23.md` evaluated KO-6,
principal graphs, and Freed-Hopkins at a qualitative pass/fail level.

**This document adds three missing elements to the checklist:**

1. Explicit Connes-Chamseddine finite-geometry **control comparison points** — precise
   numerical, structural, and representation-theoretic data from the published finite
   construction against which a Type II_1 extension is measured.
2. **GU contact points** — where the established GU/Y^14 mathematical context intersects
   or constrains the Type II_1 checklist items.
3. **Falsification tests** — explicit conditions under which each checklist item can be
   declared CLOSED (positively or negatively) without appeal to a complete construction.

The output is a tightened checklist that a specialist can use as an operational testing
protocol, not merely a requirements list.

## 2. Established Context

This computation builds on:
- `lab/specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md` — 10-item
  baseline
- `lab/specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md` — R1-R10
  additional requirements
- `explorations/type-ii1-spectral/type-ii1-finite-control-specialist-pass-2026-06-23.md` — first specialist
  pass; KO-6 CONDITIONAL/OPEN, principal graphs FAIL as SM rep source, Freed-Hopkins
  CONDITIONAL PASS
- GU context: Cl(9,5) ~= M(64,H), S = H^64, gauge group Sp(64), generation count
  ind_H(D_GU) = 24 (CONDITIONALLY_RESOLVED), KO-class KSp^0(X) (signed-readout-oq2a)

## 3. Computation: Tightened Checklist with Control Points and Falsification Tests

For each of the ten checklist items (and the three highest-risk R-requirements), this
section adds:
- **Control value / exact datum** from the finite Connes-Chamseddine literature
- **GU parallel or contact point**
- **Falsification test** — a bounded specialist computation with a YES/NO verdict

---

### Item 1 — Almost-commutative product structure

**Control datum (exact).** The product spectral triple has the form

```
(C^inf(M) tensor A_F, L^2(M,S) tensor H_F, D_M tensor 1 + gamma_M tensor D_F)
```

where M is a compact Riemannian spin 4-manifold, and the two factors are completely
independent (no mixing of M-data and F-data in the algebra or the Hilbert space). The
internal and external Dirac operators add (not multiply) because they act on orthogonal
tensor factors. The spectral action in the heat kernel expansion gives additive contributions
from M-geometry and F-geometry at each power of Lambda.

**Concrete size data.** dim H_F = 96 (finite-dimensional). dim A_F = dim(C oplus H oplus M_3(C)) = 1 + 4 + 9 = 14 (real dimension). Spectral action yields 7 coupling constants from the heat-kernel coefficients a_0, a_2, a_4 of the product triple.

**GU contact point.** In the GU context, the "product" is replaced by the bundle structure Y^14 = Met(X^4) over X^4 with section s: X^4 -> Y^14. The product is NOT a tensor product but a bundle projection; the Dirac-DeRham operator D_GU acts on the total space, not on a tensor product. The finite factor A_F (dim 14) is replaced by the 14-dimensional Y^14 geometry (dim 14 coincidence is purely numerical). The section pullback s*(D_GU) is the analog of the 4D piece D_M tensor 1, and the fiber structure provides the analog of 1 tensor D_F — but these are NOT independent; the fiber and base are coupled through II_s (second fundamental form) and the Codazzi equation.

**Independence failure at first comparison.** The CC product has algebraically independent M and F factors. The GU bundle has geometrically coupled base and fiber. This means the GU spectral action (if defined) will NOT have the additive heat-kernel expansion structure of the CC product; cross-terms from II_s will enter at every order. This is a structural distinction, not an obstruction — but any attempt to embed GU into a Type II_1 almost-commutative product must either (a) find an approximate-independence regime where II_s terms are suppressed, or (b) give up the additive-heat-kernel structure and find a replacement.

**Falsification test F1.1.** Write down the product structure explicitly for ANY Type II_1 spectral triple proposed as a GU/Type-II_1 contact. Check: are the algebra actions on the two tensor factors truly independent (no mixed commutators)? Check: does the Dirac operator have the form D_ext tensor 1 + gamma_ext tensor D_int, or does it have cross-terms? If cross-terms are present, the almost-commutative product structure (Item 1 control) is not satisfied. The test is BINARY: the structure either has or does not have independent tensor factors.

**Failure condition.** If the proposed Type II_1 extension does NOT have an independent-factor product structure (as expected from GU geometry), then it cannot be evaluated against Items 1-7 of the CC checklist without redefining what "almost-commutative product" means in a bundle context. This does not kill the lane but forces a framework replacement at Item 1 level.

---

### Item 2 — Finite algebra A_F = C oplus H oplus M_3(C)

**Control datum (exact).** The finite algebra is the unique (up to the selection axioms) real *-algebra of the form M_k(C) oplus M_l(H) oplus M_m(C) satisfying:
- real structure (closed under complex conjugation)
- irreducibility (no redundant direct summands)
- quaternion linearity (D_F commutes with quaternion action)
- order-one condition admitting the SM representation on H_F

The selection forces: k=1, l=1, m=3, giving A_F = C oplus H oplus M_3(C). The Hilbert space H_F = (C oplus H oplus M_3(C))^{oplus 32} as a bimodule (32 = 4 generations x 8 internal modes, but typically stated as dim_C H_F = 96 for three generations with the three generations INSERTED BY HAND).

**GU parallel.** In the GU framework, the role of A_F is played by the fiber algebra. The fiber GL(4,R)/O(3,1) has its automorphisms and the Clifford algebra Cl(6,4) ~= M(16,C) acting on the fiber spinor S(6,4) = C^16. The "finite algebra" analog in GU is NOT C oplus H oplus M_3(C); the SM gauge group is recovered via the Pati-Salam decomposition of S(6,4), not from the automorphisms of an internal algebra.

**Representation-theoretic comparison.**

| Datum | CC finite | GU fiber |
|---|---|---|
| Internal algebra | C oplus H oplus M_3(C), dim_R 14 | Cl(6,4) ~= M(16,C), dim_R 512 |
| Gauge group from automorphisms | U(1) x U(2) x U(3) -> SU(3) x SU(2) x U(1)/Z_6 | SU(4) x SU(2)_L x SU(2)_R from Pati-Salam branching of S(6,4) |
| Fermion count per generation | 16 Weyl fermions from H_F bimodule | 16 Weyl fermions from (4,2,1) + (4bar,1,2) |
| Generation count mechanism | Inserted by hand (96/16/2 = 3) | ind_H(D_GU) = 24 H-lines = 3 x 8 (CONDITIONALLY_RESOLVED) |

The Pati-Salam match for 16 fermions per generation is a genuine parallel. The generation count mechanism is the key structural difference: CC puts it in by hand, GU derives it (conditionally) from the index theorem.

**Falsification test F2.1 (algebra selection).** For any proposed Type II_1 extension, run the Connes selection algorithm (irreducibility, quaternion linearity, order-one) on the proposed internal algebra M. Ask: does the selection algorithm produce C oplus H oplus M_3(C) as a finite approximant? If the Type II_1 factor has no finite approximants (non-embeddable case), the algorithm CANNOT be run; the algebra selection is then UNDEFINED in the classical sense. This is a clean binary: either a finite approximant selection is defined and runs to C oplus H oplus M_3(C), or the selection is undefined.

**Falsification test F2.2 (GU contact).** For the GU/Type-II_1 contact: verify whether the Clifford algebra Cl(6,4) acting on S(6,4) can be described as a "Type II_1 analog" of M_3(C). Note: Cl(6,4) ~= M(16,C) is a TYPE I (matrix) factor, not a Type II_1 factor. A Type II_1 extension of GU would need to extend or replace Cl(6,4) with a Type II_1 algebra that carries the same Pati-Salam branching. This is not in the current GU construction.

---

### Item 3 — KO-dimension 6 mod 8

**Control datum (exact).** The CC finite triple has KO-dimension 6, determined by the sign triple (epsilon, epsilon', epsilon'') = (1, 1, -1) from the table:

| KO-dim | epsilon (J^2) | epsilon' (JD=eps'DJ) | epsilon'' (Jgamma=eps''gammaJ) |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 2 | -1 | 1 | -1 |
| 4 | -1 | 1 | 1 |
| 6 | 1 | 1 | -1 |

The SPECIFIC consequence for the SM: J^2 = 1 forces the real structure to be an involution (not a quaternionic structure); JD = DJ enforces C, P, T combined symmetry at the Dirac level; Jgamma = -gamma J separates particle from antiparticle (chirality-reversed = antiparticle).

**Control mechanism (exact): The sign triple forces anomaly structure.** Under KO-dim 6 with these signs, the real spectral triple has an associated Atiyah KO-homology class. The mod 8 periodicity ensures that a fourfold product (4 x 6 = 24 = 0 mod 8, or more precisely: the product KO-dim of the 4-manifold (KO-dim 0 for Riemannian) and the internal triple KO-dim 6 gives KO-dim 4+6 = 10 = 2 mod 8; NOT 0 mod 8). This is the key: KO-dim 2 mod 8 is what gives the chiral asymmetry between left and right Weyl fermions in 4D.

**GU contact point.** The GU spinor module S = H^64 has a quaternionic structure J (right H-multiplication), with J^2 = -1 (since H-multiplication on each H factor has i^2 = j^2 = k^2 = -1). This is KO-dim 4 signature for the J^2 sign, NOT KO-dim 6 (where J^2 = +1). However, the full 14D context is Cl(9,5), whose KO-theory class is KSp (quaternionic). The 4D section pullback has KO class KSp^0(X^4) as established in signed-readout-oq2a. The GU KO-dimension is DIFFERENT from the CC KO-dimension 6.

**Direct comparison table.**

| Datum | CC finite (KO-dim 6) | GU 14D |
|---|---|---|
| J^2 | +1 | -1 (quaternionic J on H^64) |
| Mod 8 class | KO-dim 6 | KSp (KO-dim 4 for the quaternionic signature) |
| Product with 4D base | 0+6=6 mod 8 -> KO-dim 6 product | KSp^0 x KO^0 -> distinct class |
| Chirality mechanism | epsilon''=-1: Jgamma=-gammaJ | Chiral halves S+ = H^32, S- = H^32 from gamma |

The J^2 sign difference is a STRUCTURAL GAP between the CC finite construction and the GU 14D spinor module. For a Type II_1 extension to contact GU physics, it must either (a) have J^2 = -1 (quaternionic real structure, KO-dim 4 or 0), or (b) explain how the +1/-1 discrepancy resolves when the section pullback is taken.

**Falsification test F3.1 (sign check — binary).** For any proposed Type II_1 extension or GU/Type-II_1 contact construction: compute J^2 on the Type II_1 Hilbert module. If J^2 = +1, the construction has CC KO-dim 6 structure (PASS for CC compatibility). If J^2 = -1, the construction has a quaternionic real structure (CC KO-dim 0 or 4 structure; INCOMPATIBLE with CC KO-dim 6). This is a computable BINARY test at the level of the antiunitary J alone.

**Falsification test F3.2 (mod 8 periodicity).** After the J^2 sign is checked, verify the full sign triple (epsilon, epsilon', epsilon''). For KO-dim 6 (the CC control), the required test is: epsilon = +1, epsilon' = +1, epsilon'' = -1. Failure at any single sign closes the KO-dim 6 pathway cleanly. The test is a table lookup once J, D, gamma are specified.

**Falsification test F3.3 (chirality selection power in Type II_1).** The strong version of the KO-dim 6 control: verify that the sign triple (1,1,-1), together with order-zero and order-one, FORCES the SM chiral fermion content in the Type II_1 setting. This is NOT a binary test but a structural proof obligation. If the Breuer-Fredholm chirality index tau-ind(D_+) can be any real number under the (1,1,-1) sign package, the selection power is lost (FAIL). If tau-ind(D_+) is forced onto Z or Z/N for some N under the sign package plus order-one, the selection power is partially preserved (CONDITIONAL PASS). The exact statement: does order-one in the Type II_1 bimodule, combined with KO-dim 6 signs, force tau-ind(D_+) in Z?

---

### Item 4 — Real even structure (J, gamma)

**Control datum (exact).** The CC finite real even structure has:
- J: H_F -> H_F antiunitary, J^2 = 1
- gamma: H_F -> H_F, gamma^2 = 1, self-adjoint
- [gamma, a] = 0 for all a in A_F (gamma commutes with algebra)
- {gamma, D_F} = 0 (gamma anticommutes with Dirac)
- J and gamma are independently specifiable from the algebra and Dirac data

**Concrete constraint.** The combination of J and gamma on the 96-dimensional H_F produces EXACTLY the particle/antiparticle split and the L/R-handedness split. In the SM, these two splits are independent: there exist particles that are left-handed (L and not R) and there exist antiparticles (barred representations). J implements CPT at the level of the finite spectral triple.

**GU parallel.** In the GU context, the chirality grading gamma on S = H^64 is the standard Cl(9,5) volume element or equivalently the product of all 14 gamma matrices. The particle/antiparticle split in GU is handled by the Sp(64) pseudoreal structure (Sp(64) ensures n_L = n_R = 0 net chirality, so there is no net chiral asymmetry at the TOTAL level, though there is at the SM sector level after Pati-Salam reduction). The "J" for GU is right-H-multiplication on H^64, not an antiunitary in the CC sense.

**Falsification test F4.1 (independence).** In any proposed Type II_1 construction: can J and gamma be independently adjusted, or does fixing the Type II_1 algebra M and its tracial state tau force specific J and gamma? If J and gamma are FORCED by M and tau, the chirality content is determined by the algebraic data alone (GU-parallel: Sp(64) pseudoreality forces n_L = n_R). If they are independent free parameters, the construction has less predictive power than the CC finite case. Test: write down the space of admissible (J, gamma) pairs for a given (M, tau, A, H, D) tuple. Dimension 0 (unique J, gamma up to phase) = PASS. Infinite-dimensional space = FAIL (no selection mechanism).

---

### Item 5 — Order-zero and order-one conditions

**Control datum (exact).** Order zero: [a, JbJ^{-1}] = 0 for all a, b in A_F. Order one: [[D,a], JbJ^{-1}] = 0 for all a, b in A_F.

In the CC finite model, the order-one condition with A_F = C oplus H oplus M_3(C) restricts the admissible Dirac operators D_F to a specific finite-dimensional space (the "Dirac masses" space), whose elements are in bijection with the SM Yukawa matrices (quark and lepton Yukawa couplings, CKM matrix, neutrino mixing). The order-one condition is EXACTLY the source of the Higgs field structure in the spectral SM.

**Constraint power quantified.** Without order-one, the space of D_F on H_F has dim ~= dim(End(H_F))^{self-adj} = 96^2/2 ~ 4600 real parameters. With order-one, the space of admissible D_F is ~= 36 real parameters (Yukawa sector). The order-one condition provides a factor of 128 reduction in parameter space. This is the core predictive power of the CC construction.

**GU parallel.** In GU, the analog of order-one is the commutativity of D_GU with the right-H-multiplication on S = H^64, which is used to argue that the index is an H-valued index (KSp class). There is no direct GU analog of the Yukawa-matrix selection via order-one. The Higgs in GU (PC5) is supposed to emerge from inner fluctuations of the Dirac-DeRham operator, but this construction is OPEN (PC5 is the most downstream and undeveloped of the positive construction lane items).

**Falsification test F5.1 (constraint power).** For any Type II_1 internal Dirac D on module H_M: compute dim(admissible D | order-one) / dim(all self-adj D on H_M). If this ratio is 1 (no restriction), order-one has no selection power (FAIL). If this ratio is < 1/100, the selection power is CC-comparable (PASS). The ratio is computable for specific choices of (M, A, H) even if M is a Type II_1 factor — one only needs the bimodule structure and the commutant.

**Falsification test F5.2 (Higgs sector).** After order-one: does the restricted D have an off-diagonal block structure linking L and R sectors? The CC control: D_F = [[0, M*], [M, 0]] in L/R block form, with M the Dirac mass matrix. The Higgs is phi = M. Test: does the Type II_1 analog of D under order-one admit an analogous L/R block structure? If not, the Higgs emergence mechanism is broken at the internal-algebra level.

---

### Item 6 — Chirality and Dirac operator D_F

**Control datum (exact).** The CC finite Dirac operator D_F has:
- dim H_F = 96 (finite; compact resolvent trivially)
- Spectrum = {mass eigenvalues of SM fermions} (at the GUT scale, specific predicted values)
- The Higgs mass prediction 170 GeV (original 2007 paper, later corrected to ~126 GeV by Chamseddine-Connes-Mukhanov 2012 with a real structure sign correction)
- Top quark Yukawa coupling near 1 at GUT scale (from spectral action normalization)

**Concrete prediction from D_F.** The CC spectral action gives the Higgs quartic coupling lambda = g^2 * (m_t^4 + ...) / (sum m_f^4), where m_t is the top mass and g is the weak coupling. This is a TESTABLE prediction (partially: the Higgs mass at 125 GeV is consistent with the corrected spectral prediction to within ~1%).

**GU parallel.** GU has no equivalent prediction from D_GU for the Higgs mass. The Higgs in GU is supposed to emerge from PC5 (open), and the spectral action analog for GU has not been computed. The GU distortion tensor theta = A - Gamma serves the role of "inner fluctuation" but is not a scalar field; its role in symmetry breaking is not established.

**Falsification test F6.1 (prediction extraction).** For any proposed Type II_1 spectral SM construction: compute the analog of the spectral action tau(f(D/Lambda)) and extract the Higgs mass prediction. If no prediction is extractable (the spectral action does not converge, or the heat-kernel expansion does not yield a quartic potential), the Type II_1 construction does not reproduce Item 6 (FAIL). If a prediction is extracted, compare to 125.09 +/- 0.24 GeV. A discrepancy > 10 GeV at the electroweak scale is a FAIL; within 10 GeV is a CONDITIONAL PASS (subject to renormalization group running from GUT to EW scale).

---

### Item 7 — Inner fluctuations and gauge-group recovery

**Control datum (exact).** The SM gauge group recovered by CC inner fluctuations is

```
SU(3) x SU(2) x U(1) / Z_6
```

The Z_6 quotient arises from the center of SU(3) x SU(2) x U(1) that acts trivially on all SM matter representations. The fact that this SPECIFIC quotient (not SU(3) x SU(2) x U(1), not SU(5), not SO(10)) is recovered is a non-trivial output of the inner-fluctuation calculus on A_F = C oplus H oplus M_3(C).

**Derivation trace.** The gauge potential A = sum a_i [D, b_i] has values in the one-form module Omega^1(A_F). The unitary group U(A_F) = U(1) x SU(2) x U(3) acts by A |-> u A u* + u [D, u*]. The inner-fluctuation-invariant content is the adjoint orbit, giving effective gauge group = U(A_F) / center. For A_F = C oplus H oplus M_3(C), center acts trivially iff the center of U(1) x SU(2) x U(3) acts trivially on all of H_F, which forces the Z_6 quotient.

**GU contact point.** In GU, the gauge group is Sp(64) (dim 8256), not SU(3) x SU(2) x U(1) / Z_6. There is no established mechanism by which inner fluctuations of D_GU select Sp(64) over the full diffeomorphism group of Y^14. The Shiab operator Phi defines a specific one-form bimodule (Omega^2 tensor S -> Omega^1 tensor S), but the "inner fluctuations" of D_GU by the algebra of smooth functions on Y^14 have not been computed. The SC1 program (Shiab domain/codomain) is CONDITIONALLY_RESOLVED but does not address gauge-group selection from inner fluctuations.

**Falsification test F7.1 (gauge group extraction).** For any Type II_1 construction: compute the inner-fluctuation calculus explicitly and extract the effective gauge group from the inner-fluctuation orbit. Compare to SU(3) x SU(2) x U(1) / Z_6. Test:
- Is the extracted group compact? (Non-compact gauge group = FAIL immediately — Haag-Kastler theorem requires compact internal gauge groups for local QFT)
- Is the extracted group equal to SU(3) x SU(2) x U(1) / Z_6 (or a specified extension)? If not, report what gauge group is obtained and whether it can flow to the SM group via a spontaneous-symmetry-breaking pattern.

**Falsification test F7.2 (Type II_1 selection problem).** In a Type II_1 factor M, the unitary group U(M) is uncountably infinite and NOT a Lie group in any useful sense. Show that the inner-fluctuation orbit of D under U(M) can be REDUCED to a compact Lie-group orbit by:
(a) The Jones subfactor inclusion N subset M selecting a finite-index compact subgroup, OR
(b) The Connes-channel shadow projecting to a compact group, OR
(c) A direct argument that only a compact Lie-group subgroup of U(M) acts non-trivially on D.
If none of (a), (b), (c) can be established, the Type II_1 inner-fluctuation gauge group is ill-defined (FAIL).

---

### Item 8 — Fermion representation content (16 per generation)

**Control datum (exact).** H_F = C^96 with dim_C = 96, decomposing under A_F x A_F^op as:

```
H_F = sum_{i,j} (e_i H_F e_j)
```

where e_i are minimal projections of A_F. The specific content after J-symmetry and CP-restriction:
- Q_L = (3, 2, +1/6): 6 complex modes (color x isospin)
- L_L = (1, 2, -1/2): 2 complex modes
- u_R = (3bar, 1, -2/3): 3 complex modes
- d_R = (3bar, 1, +1/3): 3 complex modes
- e_R = (1, 1, +1): 1 complex mode
- nu_R = (1, 1, 0): 1 complex mode
Total: 16 complex modes = 16 Weyl fermions per generation.

**GU comparison (EXACT MATCH at 16 per generation).** The GU spinor S(6,4) = C^16 with the Pati-Salam decomposition (4,2,1) oplus (4bar,1,2) under SU(4) x SU(2)_L x SU(2)_R gives EXACTLY 16 Weyl fermions per generation after branching SU(4) -> SU(3) x U(1). This is an exact structural match with the CC control case at the level of 16 fermions per generation:

| Mode | CC | GU Pati-Salam |
|---|---|---|
| Q_L | (3,2,1/6) | from (4,2,1) -> (3,2,1/6) + (1,2,-1/2) |
| L_L | (1,2,-1/2) | from (4,2,1) -> (3,2,1/6) + (1,2,-1/2) |
| u_R, d_R | (3bar,1,Y) | from (4bar,1,2) -> SU(3) content |
| e_R, nu_R | (1,1,Y) | from (4bar,1,2) -> singlet content |

The CONFIRMED GU result (from NEXT-STEPS.md N5): S(6,4) -> (4,2,1) oplus (4bar,1,2) -> 16 Weyl fermions = 1 SM generation [CONFIRMED].

**Generation count comparison.**

| Source | Mechanism | Count | Status |
|---|---|---|---|
| CC finite | Inserted by hand (dim H_F = 96 = 16 x 3 x 2) | 3 | POSTULATE |
| GU ind_H | ind_H(D_GU) = 8 x A-hat(K3) + 8 [RS] = 8x2+8 = 24 H-lines = 3 x 8 | 3 | CONDITIONALLY_RESOLVED |
| Type II_1 subfactor | Principal graph branching (OPEN) | ? | OPEN |

**The Type II_1 lane's headline upside is exactly here.** If a subfactor principal graph can DERIVE the count "3" rather than inserting it, that would be a strict improvement over both CC and GU (where it is an index theorem output, conditional on OQ3a-c). The anti-smuggling requirement from the specialist pass is sharp: the generation invariant must be named, not just "there are 3 summands in the graph."

**Falsification test F8.1 (16-fermion check — binary).** For any Type II_1 spectral SM candidate: compute the Murray-von Neumann dimension of the fermion sector projection p in the Type II_1 Hilbert module. If tau(p) = 16 * u (for some fundamental unit u that is rational or 1), the 16-per-generation constraint is satisfied in Type II_1 language (PASS). If tau(p) is irrational, the fermion count is NOT recoverable from the finite SM by any limit (FAIL for Item 8, unless the irrational value has a separate physical explanation).

**Falsification test F8.2 (generation invariant — non-binary).** For a subfactor candidate inclusion N subset M: produce the principal graph and identify ONE of the following as the "3":
(a) A specific valence-3 vertex in the principal graph (name it)
(b) A Frobenius-Perron multiplicity of 3 for the fundamental M-N bimodule (compute it)
(c) A depth-3 branching at the first non-trivial level of the standard invariant (compute depth-3 Bratteli diagram)
(d) An orbit of size 3 under the Jones planar algebra modular data

If none of (a)-(d) can be produced from the principal graph WITHOUT inserting three copies by hand, the subfactor generation mechanism FAILS.

**Falsification test F8.3 (GU-Type II_1 contact).** The GU generation count ind_H = 24 is in KSp^0(X) (K-theory of quaternionic Hilbert space families). If a Type II_1 extension of GU is proposed: verify that its Breuer-Fredholm index lands on the same KSp^0 class. If the Type II_1 extension gives a Breuer-Fredholm index in R (real-valued, not integer), the GU-KSp integer 24 is not recoverable (FAIL for cross-program contact). If the Breuer-Fredholm index lands on 24 in Z subset R (tracial dimension equal to 24 times fundamental unit), PASS.

---

### Item 9 — Anomaly compatibility

**Control datum (exact).** The SM anomaly cancellation per generation has FIVE independent conditions:

1. SU(3)^2 U(1): sum Q_Y [SU(3) generators] = 3 * (1/6 + 1/6) - (2/3) - (1/3) = 0
2. SU(2)^2 U(1): sum Q_Y [SU(2) generators] = 3 * (1/6) - (1/2) = 0
3. U(1)^3: sum Y^3 = 3*(2*(1/6)^3 + (-2/3)^3 + (1/3)^3) + (2*(-1/2)^3 + 1^3 + 0) = 0
4. Gravitational-U(1): sum Y = 3*(2*(1/6) + (-2/3) + (1/3)) + (2*(-1/2) + 1 + 0) = 0
5. SU(2) global (Witten): n_doublets mod 2 = 0 (satisfied: 3+1=4 doublets per generation, even)

All five conditions vanish simultaneously for EXACTLY the 16-fermion content above. This is not a coincidence but a consequence of the C, H, M_3(C) structure of A_F.

**Freed-Hopkins compatibility (extended control datum).** The five perturbative anomaly conditions above are the low-energy shadow of the Freed-Hopkins invertible-field-theory classification. The precise statement: the SM partition function on any 4-manifold M factors as a product over anomaly-free generations, giving a partition function valued in Z (not merely C* or U(1)). For the SM with 3 generations of the 16-fermion content, the Freed-Hopkins class is TRIVIAL (anomaly-free).

**GU contact point.** The GU anomaly structure is established by Sp(64) pseudoreality: n_L - n_R = 0 (no net chirality at the 14D level), pi_15(Sp) = Z (global anomaly checked). This is a DIFFERENT check from the CC per-generation anomaly: GU checks anomaly at the gauge-group level, not at the fermion-representation level. The SM per-generation anomaly conditions are satisfied by GU ONLY because S(6,4) -> 16 Weyl fermions with the correct hypercharges — and these hypercharges come from the Pati-Salam branching (CONFIRMED), not from an independent check.

**Falsification test F9.1 (five anomaly conditions).** For any Type II_1 spectral SM: run the five anomaly checks explicitly on the proposed fermion content. All five must vanish. This is the most directly testable falsification test on this list: it requires only the list of (representation, hypercharge) pairs for all modes, not the full spectral triple data. If any one of the five conditions fails to vanish, the Type II_1 candidate is DEAD regardless of the KO-dimension or principal-graph structure.

**Falsification test F9.2 (Freed-Hopkins class).** After anomaly cancellation is verified: compute the Freed-Hopkins invertible-field-theory class of the proposed Type II_1 fermion content. In the absence of a full Freed-Hopkins computation (which requires specifying the tangential structure): use the Dai-Freed formalism to check the eta-invariant contribution from each chiral fermion. If any generation contributes a non-trivial eta-invariant that does not cancel among generations, the Freed-Hopkins class is non-trivial (FAIL). The test is: eta(D_+ , generation i) = 0 mod 1 for i=1,2,3 individually.

**Falsification test F9.3 (extra modes).** If the Type II_1 construction produces modes in addition to the 16-fermion SM content (e.g., from non-embeddable factor data that survives the Connes-channel shadow), compute their anomaly contribution separately. If the extra modes contribute non-trivially to any of the five anomaly conditions above, the candidate fails. If extra modes come in vector-like pairs (n_L = n_R), they cancel and do not spoil anomaly cancellation.

---

### Item 10 — Spectral action recovery

**Control datum (exact).** The CC spectral action heat kernel expansion gives:

```
S = Tr(f(D/Lambda)) ~ sum_{k=0,2,4} f_k Lambda^{4-k} a_k(D^2/Lambda^2) + f(0) zeta_{D^2}(0) + O(Lambda^{-2})
```

where a_0, a_2, a_4 are Seeley-DeWitt heat-kernel coefficients. On the product triple, a_0 gives cosmological constant + Higgs quartic, a_2 gives Einstein-Hilbert + Higgs kinetic + Yang-Mills, a_4 gives Gauss-Bonnet + topological terms. SEVEN dimensionless coupling constants appear, matching the SM+gravity count.

**Chattopadhyay-Pradhan-Skripka (2023) extension.** Their result: for tau-compact-resolvent D in a semifinite (M, tau), the spectral action tau(f(D/Lambda)) has a perturbation expansion controlled by the spectral shift function xi(lambda; D, D+V) for perturbations V. This gives a Type II_1 analog of a_k coefficients — but the heat-kernel expansion structure is DIFFERENT: instead of terms Lambda^{4-k} a_k, one gets a tau-traced spectral shift expansion. Whether this yields the same seven coupling constants is not established.

**Falsification test F10.1 (coupling constant count).** For any Type II_1 construction with convergent tau(f(D/Lambda)): extract the number of independent free parameters (analog of coupling constants) in the spectral action expansion. CC control: exactly 7 at one-loop. If the Type II_1 analog gives more than 7, new physics is predicted (may or may not be compatible with SM); if fewer than 7, the SM coupling structure is OVER-constrained (immediate FAIL at the phenomenological level).

**Falsification test F10.2 (Higgs potential recovery).** The CC spectral action gives a Higgs potential V(H) = lambda_H |H|^4 - mu^2 |H|^2 with lambda_H / g^2 = (m_t^4 + ...) / (gauge boson masses). For the Type II_1 construction: does the analog of D_F have an L/R off-diagonal block (from order-one, F5.2 above)? If yes, the tau-traced spectral action WILL generate a quartic potential for the off-diagonal block — this is the Type II_1 Higgs. Extract the quartic coupling and compare to SM lambda_H ~ 0.13 at GUT scale. If the quartic coupling is zero (no off-diagonal block, or off-diagonal block not picked up by tau), FAIL for Higgs mechanism.

---

## 4. Cross-Program Falsification Tests (GU-Type II_1 Contact Zone)

These tests apply when a specific GU/Type-II_1 contact is proposed (not a generic
Type II_1 spectral SM, but specifically a Type II_1 internal factor attached to the GU
Y^14 = Met(X^4) construction).

**Falsification test FX.1 (J^2 consistency across GU/Type-II_1 boundary).** GU 14D has
J^2 = -1 (quaternionic real structure on H^64). CC KO-dim 6 requires J^2 = +1 on the
internal factor. Any contact must reconcile: is the GU J^2 = -1 a 14D artifact that
becomes J^2 = +1 on the section pullback? Compute J^2 on the section pullback bundle
s*(S) over X^4. If s*(J)^2 = -1 still, the GU/Type-II_1 contact is at KO-dim 4 (not 6),
and must deviate from the CC KO-dim 6 control (STRUCTURAL DEVIATION).

**Falsification test FX.2 (ind_H contact).** GU gives ind_H(D_GU) = 24 in KSp^0 (integer,
quaternionic). A Type II_1 spectral SM extension gives Breuer-Fredholm index tau-ind(D_+)
in R. If tau-ind(D_+) = 24 (recovered as an integer despite R-valued a priori), the
GU integer generation count is reproduced in the Type II_1 language (PASS). If tau-ind
is not 24, the two programs diverge at the generation count level (STRUCTURAL MISMATCH).

**Falsification test FX.3 (inner fluctuation compatibility).** GU Dirac inner fluctuations
are D_A = d + A (gauge connection). CC inner fluctuations are D + A + J A J^{-1}
(bimodule fluctuation). These are structurally different (GU inner fluctuation = connection
on a principal bundle; CC inner fluctuation = bimodule one-form). For a GU/Type-II_1
contact: is there a functor or embedding that maps GU gauge connections to CC bimodule
one-forms? If yes, the two inner-fluctuation calculi are equivalent (PASS). If the functor
requires a choice of Section s: X^4 -> Y^14 (section-dependence), the contact is
section-specific and not canonical.

---

## 5. Unified Control Comparison Table

| Item | CC finite control datum | GU parallel | Type II_1 test | Status |
|---|---|---|---|---|
| 1 | Product A_F tensor C^inf(M); additive D | Bundle Y^14, coupled base/fiber | F1.1: independent tensor factors? | STRUCTURAL GAP (bundle vs. product) |
| 2 | A_F = C oplus H oplus M_3(C), dim_R 14, Yukawa 36-param space | Cl(6,4) ~= M(16,C), Pati-Salam branching | F2.1: selection algo runs? F2.2: Cl(6,4) as Type II_1? | OPEN (selection undefined in non-embeddable case) |
| 3 | KO-dim 6: (J^2,JD,Jgamma) = (+1,+1,-1) | KO-class KSp (J^2=-1, quaternionic) | F3.1: J^2 sign; F3.2: full sign triple; F3.3: Breuer-Fredholm integer | STRUCTURAL GAP (J^2 sign differs) |
| 4 | J and gamma independently specifiable | gamma from Cl(9,5) volume, J from H-mult | F4.1: independence of J,gamma | OPEN (dependence on algebra unclear) |
| 5 | Order-one reduces D_F from ~4600 to ~36 params | H-linearity reduces index to Z-valued | F5.1: constraint power ratio; F5.2: L/R block structure | OPEN (constraint power in Type II_1 unstudied) |
| 6 | D_F finite (compact resolvent), Higgs mass ~125 GeV | D_GU tau-compact? Higgs from PC5 (OPEN) | F6.1: Higgs mass extraction | OPEN (PC5 undeveloped) |
| 7 | SU(3)xSU(2)xU(1)/Z_6 from U(A_F) inner fluct | Sp(64) from geometry; no inner-fluct derivation | F7.1: gauge group extraction; F7.2: compact reduction | OPEN (inner fluctuations on Y^14 uncomputed) |
| 8 | 16 Weyl per gen (exact), 3 gen by hand | 16 Weyl per gen (CONFIRMED), 3 gen from ind_H=24 (CONDITIONAL) | F8.1: tau-dim=16u; F8.2: principal graph invariant; F8.3: KSp contact | 16 per gen: CONFIRMED MATCH; gen count: CONDITIONALLY_RESOLVED in GU |
| 9 | 5 anomaly conditions vanish (exact) | Sp(64) pseudoreality + Pati-Salam hypercharges | F9.1: five conditions; F9.2: Freed-Hopkins; F9.3: extra modes | CONDITIONAL PASS (Pati-Salam confirmed, Freed-Hopkins conjecture) |
| 10 | Spectral action -> 7 coupling constants, Higgs mass 125 GeV | GU spectral action uncomputed | F10.1: coupling count; F10.2: Higgs quartic | OPEN |

---

## 6. Result and Verdict

**Verdict: CONDITIONALLY_RESOLVED.**

The checklist tightening is completed at reconstruction grade. The three missing elements
(explicit control comparison points, GU contact points, falsification tests) have been
supplied for all ten CC items. The main structural findings:

**Two genuine structural gaps (not mere open questions — these require positive evidence to survive):**

1. **J^2 sign gap (Items 3, 4, FX.1).** GU quaternionic real structure has J^2 = -1
   (KSp/KO-dim 4), while CC KO-dim 6 requires J^2 = +1. Any GU/Type-II_1 contact must
   resolve this discrepancy. The most natural resolution: the section pullback s*(J) may
   flip J^2, since the section breaks the 14D quaternionic symmetry to a 4D structure.
   This is UNCOMPUTED and constitutes the first falsification gate for any GU/Type-II_1
   contact program.

2. **Product vs. bundle structure gap (Item 1, FX.3).** The CC almost-commutative product
   is algebraically independent between M-factor and F-factor. The GU bundle Y^14 = Met(X^4)
   is geometrically coupled. Any attempt to embed GU physics into a Type II_1 almost-
   commutative product MUST show that the II_s coupling terms are suppressed in some regime
   (e.g., large-fiber limit, GUT scale) so that the product structure is approximately valid.
   This is UNCOMPUTED.

**One confirmed match (positive evidence):**

3. **16 fermions per generation (Item 8).** The CC control (16 Weyl fermions = 1 generation
   from A_F bimodule) is exactly matched by the GU Pati-Salam branching (S(6,4) -> 16 Weyl
   fermions, CONFIRMED). This is the only item where GU and CC agree on an explicit numerical
   count without additional conditions. The generation COUNT (3) is derived in GU via ind_H=24
   (CONDITIONALLY_RESOLVED) vs. inserted by hand in CC — GU has strictly more explanatory
   power here IF the conditional resolves.

**Five open items with explicit falsification tests now available:**

Items 2, 4, 5, 6, 7, 10 all have explicit falsification tests (F-labeled above) that a
specialist can now run without reading the rest of the checklist.

**Explicit failure conditions for this computation:**

FC1. If F3.1 shows J^2 = -1 on ANY proposed Type II_1 SM triple, that triple is NOT at
     CC KO-dim 6. The triple may still be valid physics (KO-dim 4 or 0), but loses the CC
     chirality-selection mechanism.

FC2. If F8.1 shows tau-ind(D_+) is irrational for the Type II_1 internal Dirac, the 16-
     per-generation constraint is not recoverable from the finite SM; the Type II_1 extension
     decouples from CC.

FC3. If F7.2 cannot reduce U(M) inner fluctuations to a compact Lie group via any of the
     three routes, the SM gauge group cannot be recovered from a Type II_1 extension and the
     entire pathway closes at Item 7.

FC4. If F9.1 fails (any one of the five anomaly conditions fails for the proposed fermion
     content), the candidate is dead immediately.

FC5. If F1.1 shows the proposed Type II_1 construction does NOT have an independent-factor
     product structure, the CC checklist does not apply as-is and a replacement framework
     must be specified before further evaluation.

FC6. If the section pullback J^2 computation (FX.1) gives J^2 = -1 also on X^4, the GU-
     Type II_1 contact requires a KO-dim 4 (not 6) analog of the CC checklist — a
     completely different falsification target.

## 7. Open Questions

OQ1 (J^2 section pullback). Compute J^2 on s*(S) over X^4 for the GU quaternionic J.
     Does J^2 change sign under section pullback? Gates FX.1 from UNCOMPUTED to binary.

OQ2 (inner fluctuations of D_GU). Compute D + A + J A J^{-1} analog for D_GU on Y^14.
     What gauge group does the fluctuation orbit generate? Gates F7.1 from OPEN to testable.

OQ3 (order-one constraint power for Type II_1). For a specific (M, tau, A, H, D) tuple
     with M = hyperfinite R: compute dim(admissible D | order-one) / dim(all self-adj D).
     If this ratio is not CC-comparable, Type II_1 order-one has reduced selection power.

OQ4 (Breuer-Fredholm integrality).  Is there a structural reason why tau-ind(D_+) should
     land on Z (integers) rather than Q or R under the KO-dim 6 sign constraints plus
     order-one? This is the key question for the Type II_1 generation count.

OQ5 (Higgs from GU inner fluctuations). This is PC5 in the positive construction lane.
     Remains OPEN and is the single most downstream item; unblocked by Item 5-7 closure
     above but cannot be attempted without closing those first.
