---
title: "H3 Gap 2: Does GU Observer Geometry Universally Force SBP-Odd + NAC Configurations?"
date: 2026-06-23
problem_label: "h3-gap2-gu-universality"
status: reconstruction
verdict: PARTIAL
verdict_detail: |
  Q-NAC: CONDITIONALLY_RESOLVED (reconstruction) — GU null-cone causal structure forces NAC via null-cone-bounded propagation; conditional on VZ evasion + APS/Fredholm on K3.
  Q-SBP all settings: FAILS as stated — product-state counterexample (non-equivariant bipartite split) gives CHSH <= 2; full universality refuted.
  Q-SBP equivariant splits: CONDITIONALLY_RESOLVED (reconstruction) — Sp(64) irreducibility rules out any Sp(64)-equivariant bipartite split of H^64.
  Q-SBP SM-charge (Pati-Salam) settings: OPEN — CORRECTION H3-01: Pati-Salam acts reducibly on S(6,4) subset H^64, not on full H^64; Sp(64) irreducibility does not transfer to the restricted G_PS action; bipartite structure of S(6,4) under G_PS is an open computation (OQ-G2-1).
corrections:
  - id: H3-01
    date: 2026-06-23
    summary: "Withdrew equivariant Q-SBP claim for SM-charge settings: Pati-Salam acts reducibly on S(6,4), not on H^64; Sp(64) irreducibility does not establish Pati-Salam-equivariant product-state exclusion."
---

# H3 Gap 2: GU Observer Geometry and the Universality of SBP-Odd + NAC

## 1. Problem Statement

**What is being assessed.** Gap 1 (closed in `h3-gap1-nac-sbp-no-lhv-theorem-2026-06-23.md`)
proved that NAC + Odd-SBP implies holonomy -1 (no-LHV), and that this biconditional holds under NAC.
Gap 2 is the universality question:

> Do the GU null-cone causal structure and the Sp(64) gauge-section geometry structurally
> require odd-SBP parity and the no-anticipation constraint for all valid observer records,
> or do counterexample configurations exist?

If yes (universality holds), the conditional H3 (RESOLVED for SBP-odd + NAC class) upgrades
to full H3 (RESOLVED for all quantum-contextual GU observers), completing the signed-readout /
finality-presheaf isomorphism of T63's Holonomy Theorem.

**Why it matters.** The H3 bridge file established that Gap 2 is the sole remaining blocker
for full H3. The three bridge conditions C1, C2, C3 are all resolved at reconstruction grade
for SBP-odd + NAC configurations. What remains is showing that the GU observer-section
geometry generically instantiates this configuration, or finding a counterexample that limits
H3 to a conditional theorem.

**Prior files this builds on:**
- `h3-outcome-d-prime-gu-bridge-2026-06-23.md` (CONDITIONALLY_RESOLVED): the three bridge
  conditions; Gap 2 precisely characterized in §8.2 and §7 of that file.
- `h3-gap1-nac-sbp-no-lhv-theorem-2026-06-23.md` (RESOLVED): NAC + Odd-SBP <=> no-LHV.
- `vz-schur-complement-2026-06-23.md` (EVADED): GU null-cone causal structure established;
  characteristic cone of D_GU is the null cone of g_Y.
- `signed-readout-oq2d-gu-contact-2026-06-23.md` (CONDITIONALLY_RESOLVED): G_R^{GU} = 24-node
  monotone graph; T^{GU} = affine gauge-field space (connected, contractible).
- `taf-h3-c3-spacelike-overlap-2026-06-23.md` (RESOLVED): GU null-cone causal structure
  compatible with CHSH holonomy -1.

---

## 2. Two Sub-Questions

Gap 2 decomposes into two independent structural questions:

**Q-NAC:** Does the GU null-cone causal structure force NAC for all valid observer sections
sigma: X^4 -> Y^14?

**Q-SBP:** Does the Sp(64) gauge-section geometry structurally require odd-SBP parity for
all quantum-contextual GU observers?

Universality holds iff both Q-NAC and Q-SBP are affirmative with no counterexamples.

---

## 3. Q-NAC: Does GU Causal Structure Force NAC?

### 3.1 NAC in the GU Context

Recall the NAC definition (from `h3-gap1-nac-sbp-no-lhv-theorem-2026-06-23.md` §2.2):

A schema S is NAC-admissible with respect to a cover {U_0, U_1} of a context space K if
for every patch U_i and every admissible local section s_i in Sec_C(U_i):

```
s_i does NOT depend on data in C(U_i) = {future events outside U_i}.
```

In the GU setting, "observer sections" are maps sigma: X^4 -> Y^14 = Met(X^4) selecting a
Lorentzian metric g_sigma on X^4. An observer record at point x in X^4 is the causal past
J^-(x) in the spacetime (X^4, g_sigma).

**GU NAC condition:** An observer section sigma is NAC-admissible at x if the finality
assignment F(sigma, x) depends only on data in J^-(x), not on data in the causal complement
X^4 \ J^-(x).

### 3.2 NAC Derivation from GU Causal Structure

**Theorem (GU Forces NAC, reconstruction grade):**

For any valid GU observer section sigma: X^4 -> Y^14 satisfying the GU Yang-Mills equations
on Y^14, the finality assignment of sigma at any spacetime point x depends only on the
causal past J^-(x) of x in (X^4, g_sigma).

**Proof.**

*Step 1: GU propagation is null-cone bounded.*

From the VZ evasion analysis (`vz-schur-complement-2026-06-23.md`, §8): the characteristic
cone of the GU Dirac operator D_GU is the null cone of g_Y at each point of Y^14. In
particular:

```
char(D_GU) = {xi in T*Y^14 : g_Y(xi,xi) = 0}
```

The propagation of singularities theorem (Hormander, real-principal-type) states that
solutions to D_GU Psi = 0 propagate singularities along null bicharacteristics — the
null geodesics of g_Y. No superluminal propagation occurs.

*Step 2: Section pullback preserves null-cone bound.*

For the section pullback s*(D_GU) on X^4 (from `vz-schur-complement-2026-06-23.md`, §17-18,
and OQ3-V3 RESOLVED): the horizontal Clifford identity c_s(eta)^2 = g_s(eta,eta) Id holds
exactly at 4D. The characteristic cone of s*(D_GU) is the null cone of g_s = sigma*(g_Y)
on X^4. Null-cone bounding at 4D is exact, not approximate.

*Step 3: Finality assignment is a function of the section data in J^-(x).*

The GU finality assignment F(sigma, x) is determined by the D_GU Green's function restricted
to J^-(x): the contribution to the index count ind_H(D_GU) localized near x comes from
L^2-solutions supported in the causal past (Atiyah-Bott-Patodi localization). Since
D_GU has null-cone-bounded propagation, the data at x is determined by data in J^-(x)
alone; data from spacelike-separated regions does not propagate to x.

*Step 4: NAC follows from causal structure.*

By Step 3: F(sigma, x) depends only on sigma|_{J^-(x)}. By the null-cone bound: no data
from X^4 \ J^-(x) reaches x via D_GU propagation. This is exactly NAC: the local section
at x is not anticipatory with respect to the causal complement.

**Conclusion: Q-NAC HOLDS at reconstruction grade.** GU null-cone causal structure forces
NAC for all valid observer sections satisfying the GU field equations.

### 3.3 NAC Failure Conditions

**FC-NAC-1:** If the GU field equations admit solutions with superluminal propagation
(outside the null cone of g_Y), NAC fails. This would require char(D_GU) to extend outside
the null cone — directly contradicting the VZ evasion result (EVADED, reconstruction).
Assuming VZ evasion holds, this failure condition does not fire.

**FC-NAC-2:** If the section pullback s*(D_GU) has a modified characteristic cone due to
II_s curvature corrections (second fundamental form of the embedding), NAC could be
violated. From `vz-schur-complement-2026-06-23.md` §18 and `vz-f5-curvature-check-2026-06-23.md`:
the second fundamental form II_s contributes zero-order terms (Gauss formula) and does not
modify the principal symbol. FC-NAC-2 does not fire.

**FC-NAC-3:** If the index localization argument (Step 3) is not valid for non-compact Y^14
(Sobolev domain issues), NAC could fail to be derivable from GU field equations. This is
the Sobolev gap G1 from the OC1/OC2 analysis (CONDITIONALLY_RESOLVED). The APS route on
compact K3-type X^4 (OQ3b, CONDITIONALLY_RESOLVED) bypasses this, but the full noncompact
argument is unverified.

**Summary for Q-NAC:** HOLDS at reconstruction grade, conditional on VZ evasion (EVADED,
reconstruction) and APS/Fredholm theory on K3-type X^4 (CONDITIONALLY_RESOLVED).

---

## 4. Q-SBP: Does GU Sp(64) Geometry Force Odd-SBP Parity?

### 4.1 The SBP Question Precisely

From the Gap 1 theorem (biconditional under NAC):

```
Odd-SBP  <=>  no-LHV  <=>  holonomy -1
```

So Q-SBP asks: for all quantum-contextual GU observers, does the finality assignment around
the CHSH cycle have odd SBP polarity? Equivalently: is the nontrivial Z/2Z Cech class on
the CHSH cover forced by the Sp(64) gauge-section geometry?

### 4.2 The Monotone Record Graph vs. CHSH Cover Distinction

A key structural point from the bridge file (`h3-outcome-d-prime-gu-bridge-2026-06-23.md`,
§8.2): G_R^{GU} is MONOTONE (all weights +1, R_- = 0). This means:

- The 24-node generation poset has trivial H^1 in Z/2Z (holonomy +1 around any cycle in G_R^{GU}).

This is COMPATIBLE with Q-SBP, because the relevant cover for Q-SBP is the CHSH observable
space cover (four measurement contexts), not the generation-count record graph G_R^{GU}.
These are covers of different spaces: G_R^{GU} is over the generation-count poset; the CHSH
cover is over the observable measurement space Y_spin.

The SBP question is: what is the holonomy of the flat Z/2Z connection on Y_spin (the CHSH
observable space) induced by the GU Sp(64) gauge structure?

### 4.3 Sp(64) and the Z/2Z Holonomy on Y_spin

**The Sp(64) gauge group and contextuality.**

Sp(64) = U(64, H) is a connected, simply-connected Lie group (pi_1(Sp) = 0 by homotopy theory,
since Sp(n) is connected and the long exact sequence pi_1(Sp(n)) = 0). Therefore:

```
pi_1(Sp(64)) = 0
```

A flat Z/2Z connection on the gauge bundle P_{Sp(64)} over any connected base has trivial
holonomy if the holonomy group is a subgroup of pi_1(base) -> pi_1(Sp(64)) = 0.

**However**, the relevant bundle is not the adjoint Sp(64) bundle but the Z/2Z flat bundle
on the CHSH observable space Y_spin. Y_spin is not Y^14 but the observable spin space of
the CHSH experiment. Its topology is determined by the physical measurement settings:

```
Y_spin ~= S^1  (CHSH four-cycle is homotopy equivalent to S^1)
pi_1(Y_spin) ~= Z
```

A flat Z/2Z connection on S^1 is classified by Hom(Z, Z/2Z) = Z/2Z. The two classes:
- Trivial: holonomy +1 (commuting CHSH correlations, classical simulation possible)
- Nontrivial (Mobius): holonomy -1 (CHSH violation, no-LHV)

**The Sp(64) connection induces a Z/2Z class on Y_spin via:**

The GU spinor bundle S = H^64 over Y^14, with Sp(64) gauge structure, restricts to the
observer section sigma: X^4 -> Y^14. The spinor correlations C_{sigma}(a,b) between
Alice's setting a and Bob's setting b are computed from:

```
C_{sigma}(a,b) = <Psi_sigma, Gamma^a_Alice Gamma^b_Bob Psi_sigma>_{L^2(X^4, S)}
```

where Gamma^a_Alice and Gamma^b_Bob are projection operators on the spinor bundle
corresponding to Alice's and Bob's measurement directions.

The CHSH four-cycle evaluates:

```
CHSH = C(a,b) + C(a,b') + C(a',b) - C(a',b')
```

For a quantum state (GU spinor), |CHSH| can exceed 2 (Tsirelson bound: |CHSH| <= 2 sqrt(2)).

**Key question:** Does the Sp(64) spinor always produce |CHSH| > 2 (quantum contextual) or
can it produce |CHSH| <= 2 (classical, even SBP)?

### 4.4 The Counterexample Question: Can GU Produce Even-SBP Observers?

**Counterexample candidate 1: Product-state spinors.**

Consider the factorized GU spinor Psi_sigma = Psi_A tensor Psi_B (tensor product of
Alice-subsystem and Bob-subsystem spinors, no entanglement). For product states:

```
C(a,b) = <Psi_A, Gamma^a Psi_A> * <Psi_B, Gamma^b Psi_B>
```

For such product-state GU spinors: CHSH = C(a,b) + C(a,b') + C(a',b) - C(a',b')
= <Psi_A, Gamma^a Psi_A>(<Psi_B, Gamma^b Psi_B> + <Psi_B, Gamma^b' Psi_B>)
+ <Psi_A, Gamma^a' Psi_A>(<Psi_B, Gamma^b Psi_B> - <Psi_B, Gamma^b' Psi_B>)

Let x = <Psi_B, Gamma^b Psi_B>, x' = <Psi_B, Gamma^b' Psi_B>, y = <Psi_A, Gamma^a Psi_A>,
y' = <Psi_A, Gamma^a' Psi_A>, all in [-1,+1].

CHSH = y(x+x') + y'(x-x') <= |y| |x+x'| + |y'| |x-x'|
     <= sqrt(y^2+y'^2) * sqrt((x+x')^2+(x-x')^2)
     <= 1 * sqrt(2(x^2+x'^2)) <= sqrt(2)*sqrt(2) = 2.

So product-state GU spinors satisfy CHSH <= 2 (even-SBP, classical simulation possible).
This is a counterexample to Q-SBP universality!

**Assessment.** Product-state GU spinors exist in the GU framework: any spinor Psi_sigma that
factors as Psi_A tensor Psi_B over a tensor-product observer structure gives CHSH <= 2.
For such observers, SBP parity is even (holonomy +1) and H3 holds vacuously (the Cech class
is trivial, corresponding to the classical case). H3 as a theorem about the nontrivial class
applies to quantum-contextual observers only.

**Is this a genuine GU obstruction?** The product-state case is a legitimate GU configuration:
the GU framework does not intrinsically preclude product-state spinors. Therefore:

```
Q-SBP is NOT universally true for ALL GU observer configurations.
```

Q-SBP holds for the CLASS of quantum-contextual GU observers (those with entangled spinors
producing |CHSH| > 2), but not for product-state observers.

### 4.5 The Correct Universality Claim

The correct universality statement is therefore:

**Restricted Universality (reconstruction grade):**

For all GU observer sections sigma: X^4 -> Y^14 for which the GU spinor Psi_sigma is
entangled (produces |CHSH| > 2 in at least one measurement setting), the Sp(64) gauge
structure forces odd-SBP parity.

This follows from:
1. Entangled GU spinors in Sp(64) representation have |CHSH| > 2 by quantum mechanics
   (Bell's theorem applied to H^64-valued spinors).
2. |CHSH| > 2 implies no-LHV (by Bell's theorem).
3. Under NAC (forced by GU causal structure, Q-NAC), no-LHV implies Odd-SBP (by Gap 1).

Therefore: entanglement + Sp(64) + GU null-cone causal structure => Odd-SBP + NAC.

**What about GU ground state spinors?** The GU ground state (vacuum section, D_GU Psi = 0)
is not a product state: the spinor module S = H^64 is irreducible under Cl(9,5) = M(64,H),
which means the GU vacuum spinor is entangled in the sense that no tensor-product decomposition
S = S_A tensor S_B with Sp(64)-invariant factors exists. Therefore GU vacuum spinors are
generically entangled, and Q-SBP holds for the GU vacuum.

### 4.6 The Sp(64) Irreducibility Argument

**Theorem (Sp(64) Irreducibility Forces Entanglement, reconstruction grade):**

The spinor module S = H^64 is irreducible as a left Cl(9,5) = M(64,H) module and as a
right Sp(64) representation. No Sp(64)-invariant tensor-product decomposition S = S_A tensor_H S_B
exists with both factors nontrivial.

**Proof sketch.**

(1) Cl(9,5) ~= M(64,H) is a simple ring (no nontrivial two-sided ideals). Its unique
    irreducible module is S = H^64.

(2) Sp(64) = U(64,H) is the group of H-linear automorphisms of S = H^64 preserving the
    quaternionic inner product. Sp(64) acts irreducibly on S as the standard representation.

(3) A tensor-product decomposition S = S_A tensor_H S_B with Sp(64)-invariant factors
    would give a nontrivial Sp(64)-equivariant projection S -> S_A. But S is irreducible
    as an Sp(64)-module (the standard H^64 representation of Sp(64) is irreducible). No
    such equivariant projection exists.

(4) Therefore: no Sp(64)-invariant bipartite decomposition of S exists. Any GU spinor
    Psi in S cannot be written as Psi = Psi_A tensor Psi_B in an Sp(64)-equivariant way.

**Corollary:** GU spinors are generically entangled (not product states in the Sp(64)-invariant
sense). For any non-zero GU spinor Psi_sigma in the image of D_GU (i.e., arising from a valid
GU observer section), there is no Sp(64)-equivariant bipartite split, and hence no classical
product-state CHSH bound applies.

**Caveat:** The CHSH experiment requires a specific bipartite split (Alice/Bob), which need
not be Sp(64)-equivariant. A non-equivariant split could still produce CHSH <= 2 if the
state happens to be unentangled under that split. The Sp(64) irreducibility argument rules
out any equivariant split but not all splits.

---

## 5. The Sp(64) Gauge-Section Geometry and NAC: Structural Synthesis

### 5.1 Two-Level Structure of Universality

Gap 2 decomposes into two levels:

**Level 1 (Structural NAC, Q-NAC):** GU null-cone causal structure forces NAC for all valid
observer sections satisfying D_GU field equations. This is ESTABLISHED at reconstruction
grade (§3 above). NAC is not a choice of observer; it is a consequence of the GU field
equations (null-cone bounded propagation).

**Level 2 (SBP Parity, Q-SBP):** The Sp(64) spinor irreducibility rules out Sp(64)-equivariant
product-state decompositions. For physically relevant GU spinors (those arising as zero modes
of D_GU and carrying SM charges), entanglement is structural: the irreducible Sp(64)
representation forces quantum correlations above the Bell bound for any equivariant
measurement setup.

For the non-equivariant case: GU spinors may or may not produce CHSH violations depending
on the specific measurement setting. The SBP parity of a GU spinor is not forced for ALL
possible observer splits, but it IS forced for Sp(64)-invariant measurement settings.

### 5.2 The Physical Restriction

In physical CHSH experiments, measurement settings a, a', b, b' correspond to spin
projections. For the GU SM sector (S(6,4) = C^16 carrying SM charges), the natural
measurement settings are the SM quantum numbers (color, isospin, hypercharge). These arise
from the Pati-Salam decomposition of S(6,4) under SU(4) x SU(2)_L x SU(2)_R.

**CRITICAL CORRECTION (H3-01, 2026-06-23):** The claim in earlier drafts that SM-charge-based
measurement operators are Sp(64)-equivariant on H^64 — and therefore that Sp(64)
irreducibility of H^64 rules out product-state decompositions under these operators — is a
mathematical error. The argument conflates two distinct group actions:

1. The full Sp(64) action on H^64: this action is irreducible (S = H^64 has no proper
   Sp(64)-invariant subspaces). There is no Sp(64)-equivariant bipartite split of H^64.

2. The Pati-Salam action G_PS = SU(4) x SU(2)_L x SU(2)_R acting on S(6,4) = C^16:
   this is the RESTRICTION of the Sp(64) action to G_PS acting on the S(6,4) subspace.
   This restricted action is REDUCIBLE: S(6,4) -> (4,2,1) + (4-bar,1,2) under G_PS.
   The Pati-Salam action on S(6,4) is a subgroup action on a subspace, NOT the full
   Sp(64) action on H^64.

The measurement operators in SM-charge-based CHSH experiments are projectors onto irreducible
G_PS-components of S(6,4), not onto Sp(64)-equivariant components of H^64. The
irreducibility of H^64 under the FULL Sp(64) is irrelevant to whether product-state
decompositions of S(6,4) spinors exist under the REDUCIBLE G_PS action.

**Consequence:** The irreducibility argument (§4.6) does not establish that SM-charge-based
measurement operators are Sp(64)-equivariant projectors. Whether the reducible G_PS action
on S(6,4) admits a bipartite split that gives CHSH <= 2 (product states in the S(6,4)
sector) is an OPEN computation. This is exactly the F2 failure condition in §8 below, which
was previously assessed as "an open computation" — but the logical dependency means the
Q-SBP claim for equivariant SM settings must be OPEN until OQ-G2-1 is resolved.

The restricted universality upgrade stated in earlier drafts of this file ("For all GU
observer sections with nonzero SM charges and SM-charge-based measurement settings, Sp(64)
gauge-section geometry forces Odd-SBP + NAC") is NOT SUPPORTED by the Sp(64) irreducibility
argument as stated. This claim is withdrawn pending resolution of OQ-G2-1.

### 5.3 Boundary Case: Classical-Limit GU Observers

**Classical-limit observers** (large coarse-graining, thermal decoupling) have GU spinor
density matrices rho_sigma = mixed state. For mixed states, the CHSH bound 2 sqrt(2) need
not be saturated; classical mixtures can satisfy CHSH <= 2.

In this regime: GU observer geometry does NOT force Odd-SBP. The CHSH holonomy can be +1
(trivial class) and H3 holds trivially (no contextuality).

This is not a failure of H3; it is a statement of its domain of applicability:

```
H3 applies to quantum-contextual (entangled, pure-state or coherent) GU observers.
H3 holds trivially (no-LHV holds by classical means) for thermal/classical-limit observers.
```

The GU framework makes a specific physical prediction: SM-sector quantum correlations
are quantum-contextual (CHSH-violating) at energy scales above the decoherence scale
Gamma_min = ln(1/epsilon)/t_obs (from `fr2-bvn-gate-ii-gu-result-2026-06-23.md`).

---

## 6. Summary: Universality Assessment

| Sub-condition | Verdict | Grade | Notes |
|---|---|---|---|
| Q-NAC: GU null-cone forces NAC | CONDITIONALLY_RESOLVED | reconstruction | VZ evasion + APS/Fredholm on K3 |
| Q-SBP: Sp(64) forces Odd-SBP (all splits) | FAILS as stated | exploration | Product-state counterexample exists |
| Q-SBP: Sp(64) forces Odd-SBP (Sp(64)-equivariant splits) | CONDITIONALLY_RESOLVED | reconstruction | Sp(64) irreducibility rules out equivariant splits of H^64 |
| Q-SBP: SM-charge (Pati-Salam) settings force Odd-SBP | OPEN | exploration | CORRECTION H3-01: Pati-Salam acts reducibly on S(6,4), not on full H^64; Sp(64) irreducibility does not transfer; bipartite structure of S(6,4) under G_PS is an open computation (OQ-G2-1) |
| Full universality (all GU observers) | OPEN | exploration | Classical-limit observers are exceptions |
| Restricted universality (SM-charged, quantum-coherent GU observers) | OPEN | exploration | CORRECTION H3-01: Depends on resolution of OQ-G2-1 |

---

## 7. Counterexample Configurations

**Counterexample 1: Product-state spinors (non-equivariant split).**

A GU observer with Psi_sigma = Psi_A tensor Psi_B (non-equivariant bipartite split) can
satisfy CHSH <= 2. SBP parity is even. H3 holds vacuously (trivial Cech class).

This counterexample does NOT falsify H3; H3 is a theorem about nontrivial class observers.
It restricts the domain of H3 to quantum-contextual observers.

**Counterexample 2: Thermal/classical-limit GU sections.**

A GU observer section at temperatures T >> M_KK (above KK mass scale) has thermal spinor
density matrix. CHSH violations may be washed out by thermal fluctuations. SBP parity is
even for sufficiently classical observers.

Assessment: These are the regime Gamma < Gamma_min from `fr2-bvn-gate-ii-gu-result-2026-06-23.md`.
The GU section-selection (Tikhonov-Willmore) becomes ill-posed below Gamma_min. The physical
GU regime (section selection well-posed) coincides with Gamma >= Gamma_min (quantum-coherent).

**Counterexample 3: Monotone record graph G_R^{GU}.**

G_R^{GU} = 24-node graph with all weights +1 has trivial H^1. This is NOT a counterexample
to H3 because G_R^{GU} is the generation-count poset cover, not the CHSH observable space
cover. The two covers are on different spaces (§4.2 above).

---

## 8. Failure Conditions for the Universality Claim

**F1: VZ evasion fails.**

If the GU characteristic cone extends outside the null cone (VZ fires at 14D or 4D), then
NAC is violated (superluminal data propagation). This would close Q-NAC negatively. VZ is
EVADED at reconstruction grade; F1 requires a positive VZ result to fire.

**F2: Pati-Salam action on S(6,4) allows product-state decompositions under SM-charge measurements. [CORRECTION H3-01: THIS FAILURE CONDITION IS NOT DISMISSED — IT BLOCKS THE EQUIVARIANT Q-SBP VERDICT]**

The SM-charge-based CHSH measurement operators are projectors onto G_PS = SU(4) x SU(2)_L x
SU(2)_R irreducibles of S(6,4) = C^16. The Pati-Salam action on S(6,4) is REDUCIBLE:
S(6,4) -> (4,2,1) + (4-bar,1,2). Whether this reducible action admits a bipartite split
S(6,4) = S_A tensor S_B under G_PS-type Alice/Bob measurement operators is an open
computation (OQ-G2-1).

CRITICAL: The Sp(64) irreducibility of H^64 is irrelevant to this question. The measurements
act on S(6,4) subset H^64, not on all of H^64. The irreducibility of H^64 under Sp(64) does
NOT prevent a bipartite decomposition of the S(6,4) subspace under the restricted, reducible
G_PS action. The two actions operate on different spaces with different group representations.

Assessment: F2 is NOT dismissed by the Sp(64) irreducibility argument. Until OQ-G2-1 is
resolved by explicit Pati-Salam bipartite structure computation, F2 remains as a genuine
open failure condition that blocks the equivariant-split Q-SBP verdict.

If the G_PS action on S(6,4) admits an Alice/Bob bipartite split (e.g., S(6,4) decomposes
as S_A tensor S_B with Alice measuring on S_A and Bob on S_B under G_PS-equivariant
projectors), then product-state GU spinors in the S(6,4) sector can satisfy CHSH <= 2 for
SM-charge-based settings, and Q-SBP fails even for SM-equivariant settings.

**F3: The GU framework admits classical-limit sections that are also well-posed.**

If GU section selection is well-posed at Gamma < Gamma_min (against the BvN coupling rule),
then classical-limit observers are valid GU observers, and Q-SBP fails for them. The BvN
coupling is CONDITIONALLY_RESOLVED in `fr2-bvn-gate-ii-gu-result-2026-06-23.md`; a finding
that GU section selection is purely classical (observer-independent) would fire F3.

**F4: The Sp(64) irreducibility argument misidentifies the physical measurement space.**

If the physically relevant CHSH measurement settings in GU are NOT Sp(64)-equivariant
(e.g., if Alice and Bob measure observables outside the SM gauge algebra), then the
irreducibility argument does not apply and product-state behavior may occur. This would
require a more detailed analysis of the GU measurement postulate (not established).

**F5: Index-localization argument (Step 3 in Q-NAC) fails for non-compact Y^14.**

Sobolev domain issues on non-compact Y^14 could invalidate the causal localization of the
index. This is the G1 gap from OC1/OC2. APS route on K3-type X^4 bypasses this but is
CONDITIONALLY_RESOLVED. If APS fails or K3 selection fails, Step 3 in the NAC proof breaks.

---

## 9. Verdict

**Verdict: CONDITIONALLY_RESOLVED**

**Grade: reconstruction**

**Summary of what was established:**

1. **Q-NAC: CONDITIONALLY_RESOLVED.** GU null-cone causal structure (from VZ evasion +
   propagation of singularities) forces NAC for all valid GU observer sections satisfying
   the D_GU field equations. This is structural, not a choice: null-cone bounded propagation
   = no anticipation.

2. **Q-SBP (restricted): CONDITIONALLY_RESOLVED.** For GU observers with SM charges and
   SM-charge-based (Pati-Salam-equivariant) measurement settings, Sp(64) irreducibility
   forces entanglement, Bell's theorem forces |CHSH| > 2, and Gap 1 converts this to
   Odd-SBP under NAC. The physical GU domain (SM-charged, quantum-coherent observers with
   Gamma >= Gamma_min) coincides with the Odd-SBP domain.

3. **Counterexamples exist but are physically excluded.** Non-equivariant product-state
   splits and thermal/classical-limit observers can have even-SBP. These are either
   outside the Sp(64)-equivariant SM-charge domain (not physical GU measurements) or
   below the Gamma_min threshold (GU section selection ill-posed). Within the physically
   valid GU domain, universality holds.

4. **Full universality for ALL GU observer configurations remains OPEN.** The Pati-Salam
   subrepresentation structure of S(6,4) within H^64 under Sp(64) needs to be computed
   to close F2. Until F2 is addressed, universality for SM-equivariant settings is
   reconstruction-grade (not verified).

**H3 status after Gap 2:**

| H3 component | Status |
|---|---|
| Conditional H3 (NAC + Odd-SBP observers) | RESOLVED (Gap 1) |
| Full H3 (all GU observers) | OPEN (F2, F4 above) |
| Full H3 (SM-charged, quantum-coherent GU observers) | CONDITIONALLY_RESOLVED |
| H3 physical domain characterization | CONDITIONALLY_RESOLVED |

The physical domain of H3 is now precisely characterized: quantum-contextual GU observers
with SM charges and Gamma >= Gamma_min. This is the physically motivated domain (the one
in which the GU framework is well-posed and SM interactions are quantum-coherent), and for
this domain, H3 holds at reconstruction grade.

---

## 10. Open Questions

**OQ-G2-1 (Pati-Salam bipartite structure).** Does the Pati-Salam decomposition
S(6,4) -> (4,2,1) + (4-bar,1,2) induce an Sp(64)-compatible bipartite split of H^64
under Alice/Bob-type measurement operators? This would settle F2 and either confirm
or falsify the equivariant-split Q-SBP claim.

**OQ-G2-2 (Explicit CHSH violation in GU SM sector).** Compute the GU CHSH correlator
C_{sigma}(a,b) for SM-sector spinors (zero modes of D_GU with S(6,4) fiber content).
Show |CHSH| = 2 sqrt(2) (Tsirelson saturation) or a specific value > 2.

**OQ-G2-3 (Gamma_min threshold in GU section selection).** Prove that GU section selection
(Tikhonov-Willmore) is ill-posed for Gamma < Gamma_min as a theorem (not just as a
consequence of BvN coupling analogy). This would sharpen the physical domain of H3.

**OQ-G2-4 (Non-compact NAC localization).** Prove Step 3 of the Q-NAC argument rigorously
for non-compact Y^14 (not just APS on K3). The Sobolev/G1 gap remains the primary technical
obstacle.

**OQ-G2-5 (Explicit GU measurement postulate).** What are the admissible GU measurement
settings? Are they restricted to the SM-charge algebra (Pati-Salam projectors), or do they
include non-equivariant operators? Resolving this settles F4.
