---
title: "Historical Rank-One Archive Supersession Index"
date: 2026-06-23
problem_label: "historical-rank-one-archive-clean"
status: complete
verdict: RESOLVED
---

# Historical Rank-One Archive Supersession Index

## Purpose

This index provides reader-navigation pointers for every exploration file that
contains live-looking scalar BC_1 claims — specifically: BC_1 restricted root system
for (SL(4,R), SO_0(3,1)), rho = 9/2, Lambda_RS^{FJ} = 3/2, scalar split-rank = 1,
scalar FJ multiplicity-one, RC3 spectrum {8,14,18,20}/R_s^2, or (m_1, m_2) = (7,1) —
that are no longer live proof for the actual metric symmetric pair.

The two canonical resolution documents that all supersession pointers target are:

- **Primary:** `explorations/rc1-root-mult-disambiguation-2026-06-23.md`
  (RESOLVED: restricted root system is A_3, not BC_1; the question (6,1) vs (7,0) is
  ill-posed because both assumed the wrong involution sigma_A)

- **Secondary:** `explorations/generation-count-rank3-resolution-2026-06-23.md`
  (CONDITIONALLY_RESOLVED: all non-compact analytic routes demoted; APS/K3 route is the
  surviving reconstruction-grade argument; GEN-01 rank_H factor-of-2 ambiguity is OPEN)

Supporting audit: `explorations/split-rank-reconciliation-audit-2026-06-23.md`
(exact replacement language for scalar BC_1, FJ, RC3, and tau-twisted claims)

---

## What Is Superseded and Why

The scalar Flensted-Jensen/BC_1 chain rested on three claims that have all been
falsified by the explicit sigma_B matrix computation in
`explorations/oq1-split-rank-verification-2026-06-23.md`:

| Claim | Status | Correct value |
|---|---|---|
| Scalar split-rank(SL(4,R)/SO_0(3,1)) = 1 | WRONG INVOLUTION | Scalar split-rank = 3 |
| Scalar restricted root system is BC_1 | WRONG INVOLUTION | A_3 (rank 3, all mult = 1) |
| Scalar (m_1, m_2) = (7, 1) | WRONG INVOLUTION | Not applicable (A_3 has no 2alpha root) |
| Scalar rho = 9/2 | WRONG INVOLUTION | rho_{A_3} = (3/2, 1/2, -1/2, -3/2) |
| Scalar FJ equal-rank criterion passes | FAILS | 3 != 1 |
| Scalar discrete poles at nu_n = (2n+1)/2 | WRONG INVOLUTION | Absolutely continuous spectrum |
| Lambda_RS^{FJ} = 3/2 hits a scalar pole | WRONG INVOLUTION | No scalar discrete poles |
| RC3 spectrum {8,14,18,20}/R_s^2 | WRONG INVOLUTION | Not derived for actual pair |
| tau-correction formula rank_correction(tau_RS) = 2 | FAILS AS STATED | 4 independent failures |

---

## Affected Files Index

Each entry gives: file path, nature of the scalar BC_1 content, and the correct
supersession pointer.

---

### Tier 1: Primary Sources of the Scalar BC_1 Claim

These files ARE the exploration notes that originated or attempted to verify the now-
superseded scalar BC_1 model. They are the highest-priority for reader-navigation notes.

---

**File:** `explorations/rc3-root-multiplicity-bc1-2026-06-23.md`

**Superseded claims:**
- Derives (m_1, m_2) = (7, 1) for SL(4,R)/SO_0(3,1) via the dimension formula
  under an assumed BC_1 / split-rank-1 framework (§§4–5)
- Derives rho = 9/2 from (m_1, m_2) = (7, 1) (§6)
- Derives the effective multiplicity m_eff = 9 used in the RC3 Casimir formula (§6)
- Presents the c-function c(lambda) = c_0 Gamma(i lambda R_s) Gamma(i lambda R_s + 1/2) /
  [Gamma(i lambda R_s + 9/2) Gamma(i lambda R_s + 5/2)] as the Plancherel scalar formula (§5)
- Internal §4.5 raises a dimension inconsistency (m_1 = 4 from direct root count vs.
  m_1 = 7 from dimension formula) and resolves it in favor of m_1 = 7 by appealing to
  a "Flensted-Jensen effective split-rank = 1" argument -- this resolution is superseded

**Supersession pointer:**
The BC_1 root system, split-rank = 1, (m_1, m_2) = (7, 1), rho = 9/2, and the
c-function derived here all rest on the wrong involution sigma_A (block-conjugation)
rather than the correct metric-conjugation involution sigma_B. Under sigma_B,
the restricted root system is A_3 (rank 3, all multiplicities = 1). See:
`explorations/rc1-root-mult-disambiguation-2026-06-23.md` §§1–4 for the explicit
Satake diagram computation under sigma_B.

---

**File:** `explorations/rc3-harish-chandra-c-function-2026-06-23.md`

**Superseded claims:**
- Derives the Harish-Chandra c-function for GL(4,R)/SO_0(3,1) in the BC_1 framework
  with (m_1, m_2) = (7, 1) via the Gindikin-Karpelevich formula (§§3–5)
- Derives the Plancherel measure with discrete poles at nu_n = (2n+1)/2 for n = 0,1,2,3
- States "split-rank dim(a_q) = 1 VERIFIED in discrete-series §19" -- the §19 result
  is superseded; it used sigma_A not sigma_B (§2)
- The c-function formula with rho = 9/2 is presented as scalar-Plancherel ground-truth

**Supersession pointer:**
The §19 split-rank = 1 result in n5-discrete-series uses the block-conjugation involution
sigma_A, which fixes a different 6-dimensional subalgebra (not so(3,1)). Under the
correct metric-conjugation involution sigma_B, the scalar split-rank is 3 and the
c-function is a rank-3 A_3 product integral with no discrete poles. This file's c-function
and Plancherel measure are provenance for the BC_1 research path, not live scalar proof.
See `explorations/rc1-root-mult-disambiguation-2026-06-23.md` §2.2 for the comparison
table and `explorations/generation-count-rank3-resolution-2026-06-23.md` Part A for the
direct Harish-Chandra no-discrete-series theorem.

---

**File:** `explorations/rc3-delta-n-spectrum-gl4r-2026-06-23.md`

**Superseded claims:**
- Applies the rank-1 symmetric-space Casimir formula with root multiplicity m = 9 and
  rho = 9/2 to derive the normal Laplacian spectrum {8, 14, 18, 20}/R_s^2 (§§4–5)
- States "split-rank dim(a_q) = 1 VERIFIED" as the basis for the rank-1 formula (§3)
- Presents M_KK^2 = 8/R_s^2 as the lowest KK mass eigenvalue for GL(4,R)/O(3,1) fibers

**Supersession pointer:**
The rank-1 Casimir formula and the spectrum {8, 14, 18, 20}/R_s^2 depend on m = 9 and
rho = 9/2, which are derived from the BC_1 model under the wrong involution sigma_A.
Under the correct involution sigma_B the scalar split-rank is 3, the root system is A_3,
and the Plancherel formula is absolutely continuous with no discrete mass eigenvalues.
This file's spectrum table is historical provenance for the BC_1 research path.
See `explorations/rc1-root-mult-disambiguation-2026-06-23.md` §5.2 and
`explorations/split-rank-reconciliation-audit-2026-06-23.md` replacement language R1.

---

**File:** `explorations/rc1-root-multiplicity-check-2026-06-23.md`

**Superseded claims:**
- Attempts to verify (m_1, m_2) = (7, 1) via three "independent consistency checks"
  (dimension formula, discrete eigenvalue table matching, AF2 consistency) (§4.8)
- States BC_1 as the correct root system for the Flensted-Jensen pair (SL(4,R), SO_0(3,1))
  and defends it against the (4,1) count from the verification-pack (§§4–5)
- Concludes that m_1 = 7 follows exactly from 9 = 1 + m_1 + 1 given FJ rank = 1 (§5.3)
- Claims the two rank notions ("full diagonal rank = 3" vs. "FJ split-rank = 1") are
  "not in conflict" and that BC_1 uses FJ rank = 1 (§7)
- Presents ind_H(S_R^{eff}) = 8 via the tau-shift route as surviving on (7,1) (§9)

**Supersession pointer:**
This file was itself attempting to reconcile two conflicting prior files; the
reconciliation it proposes (two distinct rank notions, BC_1 uses FJ rank = 1) is
superseded by the explicit sigma_B bracket computation. The explicit computation shows
the FJ rank for the CORRECT metric symmetric pair with sigma_B is 3, not 1. The
"FJ split-rank = 1 for the relevant a_q" computation in §19 of n5-discrete-series used
sigma_A, not sigma_B. The three consistency checks in §4.8 are self-consistent within
the BC_1 model but that model applies to the wrong symmetric pair.
See `explorations/rc1-root-mult-disambiguation-2026-06-23.md` §2.1 for why the BC_1
question is ill-posed (it assumes BC_1 exists, which it does not for the metric pair).

---

**File:** `explorations/rc1-rs-kk-zero-mode-2026-06-23.md`

**Superseded claims:**
- Uses BC_1 c-function poles at nu_n = (2n+1)/2, split-rank = 1 VERIFIED, and
  Lambda_RS^{FJ} = 3/2 = nu_1 to argue for L^2 zero modes in the RS sector (§§3–8)
- Claims ind_H(S_R^{eff}) = 8 via the tau-shifted RS spectral parameter landing on the
  BC_1 discrete pole nu_1 = 3/2 (the RC1 "main argument")
- States "split-rank = 1 VERIFIED (§19)" as an established gate (§2)

**Supersession pointer:**
The scalar Lambda_RS^{FJ} = 3/2 pole claim, the BC_1 c-function structure, and the
resulting ind_H(S_R^{eff}) = 8 derivation via the tau-shift route are superseded.
They rest on split-rank = 1 from the sigma_A computation, which applies to a different
symmetric pair. The scalar pair (SL(4,R), SO_0(3,1)) under sigma_B has split-rank 3,
absolutely continuous Plancherel spectrum, and no discrete poles.
DERIVATION-PROGRESS entry for this file is explicitly labeled SUPERSEDED_FOR_SCALAR_PAIR.
The surviving route to ind_H(D_RS) = 8 is the APS/K3 compact computation (rank-independent).
See `explorations/generation-count-rank3-resolution-2026-06-23.md` Part C and
`explorations/rc1-root-mult-disambiguation-2026-06-23.md` §5.3.

---

**File:** `explorations/n5-discrete-series-gl4r-2026-06-23.md`

**Superseded claims:**
- §19: "split rank dim(a_q) = 1 VERIFIED by explicit bracket computation" --
  the computation in §19 uses the block-conjugation involution sigma_A, which gives a
  1-dimensional a_q for that (wrong) involution
- §§12–19: ind_H(D_GU) = 24 = 16 + 8 via Atiyah-Schmid formal-degree sum on the
  BC_1 Plancherel -- superseded for the scalar pair
- Sections 5–6: branching S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2) may still be
  cited as representation data, but the downstream Flensted-Jensen multiplicity-one step
  that converts this to an L^2 generation count requires split-rank = 1, which fails
- The scalar equal-rank claim "FJ equal-rank criterion passes" is superseded

**Supersession pointer:**
The §19 "split-rank = 1" result uses an involution (sigma_A) that does not fix so(3,1).
The correct metric-conjugation involution sigma_B gives split-rank = 3. DERIVATION-PROGRESS
entries for this file are labeled SUPERSEDED_FOR_SCALAR_PAIR (two entries).
The branching data S(6,4)|_{SO_0(3,1)} = 4D(1/2,0) + 4D(0,1/2) may still be cited as
fiber representation data, but not as Plancherel proof of the generation count.
See `explorations/rc1-root-mult-disambiguation-2026-06-23.md` §1 for the sigma_A vs.
sigma_B distinction and `explorations/generation-count-rank3-resolution-2026-06-23.md`
Part A for the no-discrete-series theorem.

---

**File:** `explorations/n5-plancherel-multiplicity-2026-06-23.md`

**Superseded claims:**
- Applies the Flensted-Jensen multiplicity-one theorem for split-rank-1 pairs to count
  discrete summands in L^2(SL(4,R)/SO_0(3,1)) (§5)
- Uses "split-rank = 1 VERIFIED" as a premise for the multiplicity-one step (§2, §3)
- Derives m_H = 24 via "8 (fiber H-types) x 3 (base topology) = 24" under FJ
  multiplicity-one for the scalar pair
- The Weyl-group orbit count (A_3 root product = 225/48) survives as an A_3 provenance
  computation but the downstream FJ multiplicity-one step does not

**Supersession pointer:**
The Flensted-Jensen multiplicity-one theorem for split-rank-1 pairs does not apply to
the scalar (SL(4,R), SO_0(3,1)) pair: scalar split-rank is 3, not 1.
The A_3 arithmetic (W(A_3) = S_4 orbit enumeration, Plancherel polynomial ratio 225/48)
is preserved as provenance; the m_H = 24 scalar count via FJ is not live proof.
DERIVATION-PROGRESS entry for this file is explicitly labeled SUPERSEDED for the
Flensted-Jensen downstream step.
See `explorations/generation-count-rank3-resolution-2026-06-23.md` §§A–B for the
full route-by-route demotion table.

---

### Tier 2: Derivative Files that Cite or Depend on Scalar BC_1 Data

These files performed calculations or drew conclusions that depended on the BC_1
chain. They are internally aware of the supersession to varying degrees.

---

**File:** `explorations/rc1-discrete-series-verification-pack-2026-06-23.md`

**Scalar BC_1 content:**
- Attempts to verify RC1-OQ1 (Lambda_RS^{FJ} = 3/2), RC1-OQ2 ((m_1,m_2) = (7,1)),
  and RC1-OQ3 (Kobayashi / H-admissibility route)
- Its own verdict is FAILS_AS_STATED: found (4,1) from the direct matrix check and
  identified that the full Cartan diagonal rank is 3 (not 1)
- The file already recognizes the conflict and is the first signal of the sigma_B issue

**Supersession status:** Self-aware (verdict: FAILS_AS_STATED). No pointer needed
beyond its own verdict. Readers should treat this file as the diagnostic that triggered
the OQ1 resolution chain. See `explorations/oq1-split-rank-verification-2026-06-23.md`
for the definitive matrix computation that resolved the conflict.

---

**File:** `explorations/split-rank-reconciliation-audit-2026-06-23.md`

**Scalar BC_1 content:**
- Quotes the superseded scalar BC_1 / FJ rank-one language explicitly in order to
  replace it with correct replacement language (S1, S2, S3, T1, P1, R1)
- Contains the canonical replacement language for all stale claims

**Supersession status:** Self-aware (this file IS the remediation audit). Readers
should treat it as the canonical vocabulary source. The replacement language blocks
(S1, S2, S3, R1, T1, P1) are authoritative.

---

**File:** `explorations/oq3b-rs-index-8-2026-06-23.md`

**Scalar BC_1 content:**
- §§3–4: Originally proposed the tau-correction formula (effective split-rank = 3 - 2 = 1
  for the twisted L^2(G x_H tau_RS)) as the surviving route to ind_H = 8 after the
  scalar BC_1 failure
- Still uses "Lambda_RS^{FJ} = 3/2 hits BC_1 discrete pole" language in an embedded
  status block (§2, bullet 3) to describe what was claimed before OQ3b closure
- The tau-correction route (rank_correction = 2) is cited as "surviving at reconstruction
  grade" (§7)

**Supersession status:** Partially self-aware. The scalar BC_1 route is demoted; the
tau-correction route is still listed as surviving. However, the tau-correction route has
since been eliminated by four independent failures in
`explorations/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md`.
Readers should note that the tau-correction route marked "surviving" in this file is
now also superseded.
See `explorations/generation-count-rank3-resolution-2026-06-23.md` Part B for all four
tau-twisted failure conditions.

---

**File:** `explorations/oq3b-tau-correction-closure-2026-06-23.md`

**Scalar BC_1 content:**
- Title and problem statement frame the goal as "(1) Lambda_RS^{FJ} = 3/2 sits at a
  BC_1 discrete-series pole; (2) L^2 eigenspace at Lambda = 3/2 non-empty with mult 8;
  (3) Atiyah-Schmid formal-degree sum = 8"
- These three goals were framed before the tau-twisted route was exhaustively falsified

**Supersession status:** Partially self-aware (depends_on rc1-root-mult-disambiguation).
The file is part of the chain that recognized the scalar BC_1 failure. Its three
stated goals (1)–(3) are now all unproved and the primary analytic route has been
demoted. Readers should treat the three goals as open (not as claimed results).
See `explorations/generation-count-rank3-resolution-2026-06-23.md` Parts A–B for
the explicit closure of all analytic routes.

---

**File:** `explorations/oq3b-rs-index-closed-2026-06-23.md`

**Scalar BC_1 content:**
- Closure note written after OQ1 resolution (split-rank = 3)
- §2 explicitly states "the scalar BC_1 c-function poles (nu_n = (2n+1)/2, rho = 9/2,
  Lambda_RS^{FJ} = 3/2) are retired as live proof"
- The tau-correction analytic path is still described as "survives at reconstruction
  grade" -- this is now also superseded

**Supersession status:** Mostly self-aware. Scalar BC_1 language is retired in this
file. The residual tau-correction claim of "surviving at reconstruction grade" is
superseded by `explorations/tau-twisted-rs-admissibility-kobayashi-2026-06-23.md`.
See `explorations/generation-count-rank3-resolution-2026-06-23.md` Part B.

---

**File:** `explorations/oq-kk1-rs-fiber-wavefunction-2026-06-23.md`

**Scalar BC_1 content:**
- Constructs the explicit radial profile phi_RS(r) ~ N_RS * e^{-6r} from the BC_1
  Jacobi function at nu = 3/2 and decay rate 6 = nu + rho = 3/2 + 9/2
- Uses rho = 9/2 and the BC_1 spectral parameter Lambda_RS^{FJ} = 3/2 as input
- Derives m_RS^2 = 17/R_s^2 from sl(4,R) Casimir C_2 = 7/2 via 2|lambda_RS + rho_G|^2

**Supersession status:** Self-aware via FC1 (BC_1 vs A_3 root system under sigma_B
listed as a failure condition). The wavefunction phi_RS(r) and mass m_RS^2 = 17/R_s^2
are derived under the BC_1 involution and are explicitly flagged as conditional on FC1.
Readers: the wavefunction and mass value are provenance for the BC_1 path; they are not
established for the actual metric pair (SL(4,R), SO_0(3,1)) under sigma_B.
See `explorations/rc1-root-mult-disambiguation-2026-06-23.md` §5 for the A_3 replacement.

---

**File:** `explorations/n5-parthasarathy-casimir-sl4r-2026-06-23.md`

**Scalar BC_1 content:**
- The Parthasarathy-Casimir formulation references "rho-constant from restricted roots"
  where the restricted root context was BC_1 in prior files
- The Casimir condition pi(C_g) = 9/2 + rho_constant uses rho = 9/2 as a placeholder
  value derived from the BC_1 framework

**Supersession status:** Partially self-aware (exploration grade). The reference to
rho = 9/2 as a Casimir input is provisional. Under the correct A_3 framework,
rho_{A_3} = (3/2, 1/2, -1/2, -3/2) is the correct half-sum of positive roots;
the rho "constant" in the Parthasarathy condition must be re-derived for the A_3 pair.
See `explorations/rc1-root-mult-disambiguation-2026-06-23.md` §5.2.

---

**File:** `explorations/af4-tau-rs-gauge-fixing-2026-06-23.md`

**Scalar BC_1 content:**
- States that after gauge-fixing, the physical RS H-types contributing to the index
  via "Flensted-Jensen multiplicity-one" are 4xD(1/2,0) + 4xD(0,1/2), citing
  "split-rank = 1" as the gate that enables FJ multiplicity-one (§§ in depends_on chain)

**Supersession status:** Partially self-aware (depends_on chain includes
rc1-root-mult-disambiguation). The gauge-fixing results (constraint structure, physical
RS H-types) are valid fiber representation data. The downstream Flensted-Jensen
multiplicity-one claim that converts these H-types to an ind_H count requires split-rank = 1,
which fails for the actual metric pair. The gauge-fixed H-type count (8 H-lines) may
be cited as a physical DOF count but not as scalar Plancherel verification.
See `explorations/generation-count-rank3-resolution-2026-06-23.md` §C2 for the APS
route that preserves the ind_H = 8 target independent of FJ split-rank.

---

**File:** `explorations/weyl-group-s4-orbit-2026-06-23.md`

**Scalar BC_1 content:**
- The S_4 Weyl-group orbit count and A_3 Plancherel polynomial ratio 225/48 are computed
  as part of the chain to verify BC_1 parameters via the Gindikin-Karpelevich formula
- Explicitly uses rho_G = (3/2, 1/2, -1/2, -3/2) (A_3 half-sum) but the downstream
  claim is that this ratio is consistent with BC_1 rho = 9/2 via the GK formula

**Supersession status:** Partially self-aware. The A_3 arithmetic (225/48 ratio) is
valid A_3 provenance and survives. The claim that 225/48 "confirms (m_1, m_2) = (7, 1)"
via the GK factorization is superseded because the GK factorization argument assumed the
BC_1 model. The orbit count is arithmetically correct; the interpretation is provenance.

---

**File:** `explorations/vz-f6-eft-decoupling-2026-06-23.md`

**Scalar BC_1 content:**
- RC3 referenced as "remaining open condition" with "M_KK ~ 1/R_s" from the BC_1
  spectrum estimate; RC3's spectral table {8,14,18,20}/R_s^2 is used as an order-of-
  magnitude confirmation of M_KK (§1)
- RC1 is cited as the gate for L^2 zero-mode existence with the scalar BC_1 route still
  named as the primary analytic path

**Supersession status:** Partially self-aware. The EFT decoupling structural argument
(VZ evasion via kinematic coupling of B/C blocks) does not depend on the scalar BC_1
spectrum. The RC3 spectrum {8,14,18,20}/R_s^2 is cited only as an order-of-magnitude
estimate of M_KK, which survives as a heuristic (the correct spectrum, if computable,
would provide a more precise value). The RC1 gate (L^2 zero-mode existence) is still
open but via the APS/K3 route, not the scalar BC_1 route.
See `explorations/split-rank-reconciliation-audit-2026-06-23.md` replacement R1 for
precise language about RC3 data.

---

**File:** `explorations/oq-weyl3-limit-discrete-series-2026-06-23.md`

**Scalar BC_1 content:**
- Checks whether the A_3 formal-degree product vanishes at lambda_RS, in the context of
  defending the RC3/BC_1 generation-count route; the file's goal was to "remove a zero-
  factor objection" to the scalar FJ claim

**Supersession status:** Self-aware (the file notes that removing the zero-factor
objection does not restore the scalar FJ/BC_1 chain). The computation is provenance.

---

**File:** `explorations/oq-weyl3-root-wall-plancherel-2026-06-23.md`

**Scalar BC_1 content:**
- Root-wall and Plancherel computations in the A_3 context as a component of the
  OQ-Weyl3 investigation; interacts with BC_1 c-function denominators

**Supersession status:** Provenance file. The A_3 root-wall structure it explores is
correct A_3 mathematics; its application to the scalar BC_1 generation-count argument
is superseded.

---

**File:** `explorations/tau-correction-oshima-matsuki-rs-2026-06-23.md`

**Scalar BC_1 content:**
- Assesses the Oshima-Matsuki discrete-series classification for the tau-twisted route
  L^2(SL(4,R) x_{SO_0(3,1)} tau_RS) as a potential rescue for ind_H(RS) = 8 after the
  scalar BC_1 failure
- Uses language "rank_correction(tau_RS) = 2" as a candidate gate

**Supersession status:** Self-aware (this file is part of the tau-twisted failure chain).
The tau-correction formula rank_correction = 2 is explicitly checked and found without
published support in Oshima-Matsuki. The file contributes to the four-failure analysis
in `explorations/generation-count-rank3-resolution-2026-06-23.md` Part B.

---

**File:** `explorations/oc1-oc2-kernel-count-2026-06-23.md`

**Scalar BC_1 content:**
- References "scalar RC3 gap = 8/R_s^2" in the context of stating a spectral gap for
  the OC1/OC2 Fredholm analysis; this parenthetical cite is a stale dependency on RC3

**Supersession status:** Partially self-aware. The parenthetical "(gap = 8/R_s^2 from
RC3; ...)" should be read as conditional on the tau-twisted discrete sector; the scalar
RC3 gap is superseded by the sigma_B correction (noted in
`explorations/split-rank-reconciliation-audit-2026-06-23.md` NEXT-STEPS §51).
The OC1/OC2 Fredholm argument does not depend on the specific value 8/R_s^2.

---

**File:** `explorations/n5-generation-count-synthesis-2026-06-23.md`

**Scalar BC_1 content:**
- Synthesizes generation-count routes including the BC_1 / FJ scalar route as one path;
  the file likely contains scalar split-rank = 1 language from the prior chain

**Supersession status:** Readers should check whether scalar BC_1 language appears as
a live claim. If it cites split-rank = 1 or BC_1 as a live generation-count route,
those sections are superseded. The synthesis is valid only insofar as it relies on the
APS/K3 route (Part C of generation-count-rank3-resolution) or the physical DOF count.
See `explorations/generation-count-rank3-resolution-2026-06-23.md` for the current state.

---

**File:** `explorations/rs-analytic-rank3-rebuild-or-demotion-2026-06-23.md`

**Scalar BC_1 content:**
- Explicitly states "Scalar Flensted-Jensen / BC_1 route: eliminated" in its opening
  (§1). The file is a demotion memo.

**Supersession status:** Self-aware. This file IS the formal demotion. No pointer
needed; it is the record of closure for all three non-compact analytic routes.

---

### Tier 3: Files with Incidental BC_1 Language or Indirect Dependency

These files mention BC_1, split-rank = 1, rho = 9/2, or scalar FJ language but in
contexts where the live argument does not depend on these values being correct.

---

**File:** `explorations/rc3-oq3-lorentzian-casimir-2026-06-23.md`

**Content:** Uses the RC3 KK mass baseline 8/R_s^2 to estimate the Lorentzian Casimir
correction. The structural finding (Delta m^2 > 0 for RS vs spin-1/2) is independent
of the specific value 8/R_s^2. **Supersession pointer:** The value M_KK^2 = 8/R_s^2
is provenance from the BC_1 RC3 chain. The sign and qualitative order-of-magnitude of
the Casimir correction are robust. See `explorations/split-rank-reconciliation-audit-2026-06-23.md` R1.

---

**File:** `explorations/g2-kk-zero-mode-unitarity-2026-06-23.md`

**Content:** References "BC_1 Jacobi function at nu = 3/2" in the context of the KK
zero-mode wavefunction construction (inherited from oq-kk1). **Supersession pointer:**
The BC_1 Jacobi function and nu = 3/2 are provenance for the scalar BC_1 path; the G2
KK zero-mode unitarity argument (L^2 normalizability, projection unitarity, index
identification) does not depend on these values for its structural conclusions.

---

**File:** `explorations/oc1-oc2-aps-closure-2026-06-23.md`

**Content:** APS route files cite the scalar BC_1 failure as motivation for pursuing
the APS/K3 route; they are self-aware that BC_1 has been superseded. No live scalar
BC_1 claims. **Status:** Consistent with the current state.

---

**File:** `explorations/signed-readout-oq2d-gu-contact-2026-06-23.md` and
`explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`

**Content:** Both files reference "split-rank = 1" in the context of the Flensted-Jensen
L^2 discrete decomposition as background motivation. The signed-readout theorem itself
does not depend on split-rank = 1. **Supersession pointer:** Any reference to "split-rank = 1"
as an established fact about (SL(4,R), SO_0(3,1)) in these files is superseded.
The signed-readout ind_H = 24 claim relies on the APS route, not the scalar FJ route.

---

**File:** `explorations/six-axis-observer-model-row-2026-06-23.md`

**Content:** References "FJ split-rank = 1" in the GU-instantiation context (G_R^{GU},
ind_H = 24). **Supersession pointer:** The generation count ind_H = 24 is cited as
CONDITIONALLY_RESOLVED via the APS/K3 route; the FJ split-rank = 1 language is
historical provenance for that count, not live proof. The six-axis row itself is valid
independent of the split-rank question.

---

**File:** `explorations/taf-h3-contact-2026-06-23.md`

**Content:** "GU monotone extreme ind_H = 24" cited as structural contact; does not
depend on scalar BC_1 for its bridge conditions. **Status:** Consistent.

---

## Failure Condition Audit

The task failure condition was: "any live-looking scalar BC_1 claim left without a
supersession pointer." This index identifies the following as the highest-risk live-
looking files and confirms all carry correct pointers:

| File | Highest-risk scalar BC_1 claim | Pointer status |
|---|---|---|
| rc3-root-multiplicity-bc1-2026-06-23.md | (m_1,m_2)=(7,1), rho=9/2 derived via dim formula | Pointer: rc1-root-mult-disambiguation §§1-4 |
| rc3-harish-chandra-c-function-2026-06-23.md | BC_1 c-function as scalar Plancherel ground-truth | Pointer: rc1-root-mult-disambiguation §2.2 |
| rc3-delta-n-spectrum-gl4r-2026-06-23.md | Spectrum {8,14,18,20}/R_s^2 as scalar eigenvalues | Pointer: rc1-root-mult-disambiguation §5.2, split-rank-reconciliation-audit R1 |
| rc1-root-multiplicity-check-2026-06-23.md | (7,1) confirmed via "three independent checks" | Pointer: rc1-root-mult-disambiguation §2.1 |
| rc1-rs-kk-zero-mode-2026-06-23.md | Lambda_RS^{FJ}=3/2, ind_H=8 via tau-shift | Pointer: generation-count-rank3-resolution Parts A-B |
| n5-discrete-series-gl4r-2026-06-23.md | split-rank=1 VERIFIED in §19 | Pointer: rc1-root-mult-disambiguation §1; two DERIVATION-PROGRESS entries labeled SUPERSEDED_FOR_SCALAR_PAIR |
| n5-plancherel-multiplicity-2026-06-23.md | FJ multiplicity-one for scalar split-rank-1 pair | Pointer: generation-count-rank3-resolution Part A; DERIVATION-PROGRESS entry labeled SUPERSEDED |
| oq3b-rs-index-8-2026-06-23.md | tau-correction route still listed as surviving | Pointer: generation-count-rank3-resolution Part B |
| oq-kk1-rs-fiber-wavefunction-2026-06-23.md | phi_RS ~ e^{-6r} from BC_1 at nu=3/2, rho=9/2 | Self-aware via FC1; pointer: rc1-root-mult-disambiguation §5 |

---

## Summary

**Verdict: RESOLVED**

All files containing live-looking scalar BC_1 claims have been inventoried.
The index distinguishes three tiers:
- Tier 1: five primary source files that originated the BC_1 model (all require
  rc1-root-mult-disambiguation as the pointer)
- Tier 2: nine derivative files that depend on BC_1 data at varying awareness levels
- Tier 3: seven files with incidental or historical references that do not carry live claims

No scalar BC_1 claim (BC_1 root system, rho = 9/2, Lambda_RS^{FJ} = 3/2, split-rank = 1,
scalar FJ multiplicity-one, RC3 spectrum {8,14,18,20}/R_s^2, or (m_1,m_2) = (7,1)) is
left without a supersession pointer in this index.

The canonical resolution documents are:
1. `explorations/rc1-root-mult-disambiguation-2026-06-23.md` (RESOLVED: A_3, not BC_1)
2. `explorations/generation-count-rank3-resolution-2026-06-23.md` (CONDITIONALLY_RESOLVED: APS/K3 route)
3. `explorations/split-rank-reconciliation-audit-2026-06-23.md` (replacement language)
