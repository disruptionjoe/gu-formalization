---
artifact_type: exploration
status: exploration
created: 2026-07-13
hypothesis: H41
title: "W125 -- THE FIRST BUILD ATTEMPT AGAINST THE COMPLETE REQUIREMENTS SPEC (H41, the North Star). VERDICT: PARTIAL BUILD, acceptance criterion 5.3 NOT met, with a sharp map of exactly which legs fail. What IS built (symbol level, carrier B): the g=1 ker-Gamma cure with zero VZ leakage including the mass term; the SA-C2 shiab REVISION written into the candidate (the unique constraint-preserving vertex contract - (1/6) wedge, t* = -1/6 exact, revising GU's written (1,0,1,0)); the massive Krein-self-adjoint RS symbol ([K,Pi]=0 exactly, tree [P,S]=0 survives on the built object); and -- the wave's one genuine status movement -- the SA-C4 subprincipal FC-VZ-4 test, BUILT for the first time: TEST-BUILT-PASSES for the built candidate (characteristic variety exactly the eta(9,5) null cone; zeroth-order II_s provably subprincipal because the constant projector cannot mix symbol degrees; positive control shows the failure mode is detectable). What FAILS: acceptance (a)'s curved-Y14 clause (symbol-level model only), SA-G9 (from-scratch linearization with matter sources, unbuilt), and most of the H59 loop packet (d). PAYOFF: gated numbers unlocked = NONE, with machine-checked reasons (the cure is a dimensionless kinematic point in a Hom-disjoint sector). All 9 DECLARATIONs stated as named postulates; FITs emitted source-first: 0 of 10. The count stays {1,3}; H41 stays not-fully-built; H59 stays OPEN."
grade: "COMPUTED (exact, on the verified Cl(9,5)=M(64,H) rep): the built term's zero leakage with the mass term; C2 = 155.3625 and the leakage law reproduced; ||Gamma . contract|| = 215.8518 and t* = -1/6 exact (residual 0); [K,Pi] = 0 exactly and Krein self-adjointness of the built symbol; the SA-C4 blocks (off-cone non-degeneracy both signs, on-cone degeneracy to machine precision, exact degree-1 homogeneity of the restricted symbol, subprincipal insert homogenization, first-order-insert positive control). ARGUED: that the flat 14-dim symbol model carries the curved-Y14 subprincipal content via II_s entering at zeroth order (rides tests/vz_fcvz4_subprincipal.py Block B, not re-derived on the bundle); the EFT status of the guardian-free branch (wave 34, cited). Per the spec's own E1 rule this wave is a CONSTRUCTION with zero prediction-grade emissions: NOT progress by itself except where a row's status moved (SA-C4: no-test -> test-built-passes for the built candidate). No canon movement, no count movement ({1,3}), no verdict movement; H59 stays OPEN."
construction: "program-native throughout (GEOMETER-VS-PHYSICS-OBJECTS.md): the cure is the geometer's constant equivariant ker-Gamma projector (g=1), NOT the physicist's F-analytic Porrati-Rahman vertex -- the fork is carried, and this wave shows the two routes differ EXACTLY on SA-C4 decidability (the constant projector cannot mix symbol degrees; the Schur/E-block route of cure A stays blocked). Standard-field objects used where they are the right ones: the eta(9,5) null cone as the causality standard; Stelle form for the gravity sector rows (cited, untouched)."
depends_on:
  - explorations/source-action-requirements-spec-2026-07-13.md
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - explorations/wave35/source-action-carve-2026-07-11.md
  - explorations/yukawa-scoping-2026-07-13.md
  - explorations/obj5-minimal-source-action-2026-07-11.md
  - explorations/firewall-and-two-geometries/source-action-necessary-conditions-and-causality-2026-06-27.md
  - tests/vz_fcvz4_subprincipal.py
  - canon/shiab-existence-cl95.md
scripts:
  - tests/W125_built_candidate_assembly.py
  - tests/W125_sac4_subprincipal_built.py
---

# W125 -- building the minimal source-action candidate against the 27-row spec

Tests: `tests/W125_built_candidate_assembly.py` (14/14, exit 0) and
`tests/W125_sac4_subprincipal_built.py` (9/9, exit 0). Deterministic; the SA-C4 test uses a
fixed seed (20260713) for its sampled covectors and inserts; every anchor number is reproduced
from the repo's verified Cl(9,5) = M(64,H) representation.

Run as a 5-persona inline team (one worker, sequential): (1) constructive field theorist;
(2) representation theorist; (3) higher-spin/causality specialist; (4) Krein/loop specialist;
(5) honesty auditor (E1/Lakatos).

**What this wave is.** The first build ATTEMPT with the complete requirements list in hand
(the 2026-07-13 spec: 8 FORCED, 9 DECLARATION, 10 FIT; acceptance criterion 5.3). The
pre-declared honest expected outcome was a PARTIAL build with a sharp failure map, and that is
what it returns. W102 built a skeleton before the spec existed; the deltas here are (i) the
complete-spec discipline (every consumption explicit, the ledger below), (ii) the SA-C4 test,
which did not exist (the spec's "one genuinely unbuilt FORCED check"), (iii) the shiab
revision written INTO the candidate as an exact repo test (t* = -1/6, previously only in a
committed scratch), and (iv) the payoff question answered with machine-checked reasons.

---

## 1. Persona 1 (constructive field theorist): the BUILT-CANDIDATE

### BUILT-CANDIDATE (symbol level, carrier B) -- the action, term by term

Explicitly declared field space (the DECLARATION layer, each row a named postulate -- see the
consumption ledger, section 5): fields are theta (the IG one-form / gravity field, soldered to
the spin-lift by POSTULATE SA-G1), the connection A = spin-lift(grad^gimmel) (the same datum,
wave 34), the RS matter Psi constrained to ker Gamma = carrier B (POSTULATE SA-C1, the
B-leaning lean taken openly), the k = 0 scalar Higgs phi_0 (POSTULATE SA-Y2), fermions in the
128-dim Dirac module.

| # | Term | Consumes (FORCED) | Machine check |
|---|------|-------------------|---------------|
| T0 | `S_grav = alpha |II|^2 + beta |H|^2` | inherited rows (H45/H48 two-invariant count); SA-G9 NOT discharged (see failure map) | wave35 rank-10/rank-1 Hessians (rerun, exit 0) |
| T1 | `S_RS,kin = <Psi, Pi M_D Pi Psi>` on ker Gamma | SA-C2 (the g = 1 cure; leakage(g) = (1-g) C2, unique root g = 1; built leakage = 6.3e-14) | W125 assembly B1 |
| T2 | `S_RS,mass = m2 <Psi, Pi Psi>`, m2 = sqrt(m2_eff) mu_DW a FIT | SA-U4 (massive branch forced); leakage stays 0 with the mass; Krein-self-adjoint | W125 assembly B2 |
| T3 | `S_int = <Psi, [contract - (1/6) wedge](F) Psi>` | SA-C2's revision clause: canon (1,0,1,0) is gamma-traceFUL (215.8518); the UNIQUE constraint-preserving vertex has t* = -1/6 EXACTLY (residual 0); its image lies in ker Gamma automatically | W125 assembly B3-B4 |
| T4 | `S_Yuk = y_ij <psi_+, C phi_0 chi_->` | SA-Y1 (the unique equivariant k = 0 cross-chirality channel; non-form carriers and Majorana scalar forbidden) | tests/yukawa-scoping (20/20, exit 0, same-day recorded run; VERIFIED-BY-PRIOR-RUN-UNMODIFIED-DEPS) |
| -- | spurion sector: NOT instantiated | SA-Y7a honored by deferral (if a family-breaking spurion is added it MUST be the Sym^2(Lambda^2_+) doublet; its values SA-Y7b are FITs) | W76 (standing) |

The revision cost is paid openly: **T3 is not GU-as-written.** "Reconstruct GU as written
(1,0,1,0)" and "make it causal" are jointly unsatisfiable (wave 34); the built candidate takes
causality and revises the written shiab to the gamma-traceless line, exactly as the spec's
SA-C2 row demands.

What T1-T3 jointly are, structurally: the geometer's cure. The constraint is enforced by the
CONSTANT so(9,5)-equivariant projector Pi (rank 1664), not by an F-analytic vertex and not by
a Stueckelberg/BRST gauging. That choice is exactly the named construction fork
(GEOMETER-VS-PHYSICS-OBJECTS, RS-cure row), and section 3 shows it is load-bearing: it is WHY
SA-C4 became decidable this wave.

## 2. Persona 2 (representation theorist): exactness of every claimed uniqueness

All checks on the verified rep, exact:

- **The cure family and point.** Leakage law leakage(g) = (1-g) C2 with C2 = 155.3625069
  reproduced; g = 1 unique root; rank(Pi) = 1664 = 1792 - 128 (Gamma surjective). [W125 B1]
- **The vertex line.** The equivariant family Hom(Lambda^2 V x S, V x S) is 2-dim per chiral
  block (SHIAB-03, cited); the gamma-trace functional on it has a 1-dim kernel, computed here
  directly on the full module without materializing the 334MB tensors:
  ||Gamma . contract|| = 215.8518, t* = -<Gw, Gc>/<Gw, Gw> = -1/6 to 1e-12, residual
  ||Gamma . (contract + t* wedge)|| = 0.0. So the constraint-preserving vertex is a LINE and
  the built T3 is its normalized representative. [W125 B3]
- **No-p-hack certificates.** Gamma is so(9,5)-equivariant (residual exactly 0 on the
  self-dual generators), so the cure closes on BOTH carriers: building T1 does NOT decide
  SA-C1 -- carrier B stays a named postulate. M_D is theta-locus-free (kron(I, c(xi))
  identity, exact), so the build does not silently consume the soldering SA-G1. The count
  residues (-42 % 3 = 0, -38 % 3 = 1, net-3 residue 0) keep the residue trap active: SA-C3
  stays open, the realized rank stays {1,3} in the built candidate. [W125 C1-C3]
- **New exactness this wave (feeding SA-C4):** gamma^a gamma_a = 14 I and
  gamma^a c(xi) gamma_a = -12 c(xi) (both to machine zero). These are the arithmetic skeleton
  of the off-cone injectivity of the restricted symbol: if (Pi M_D Pi) psi = 0 with
  psi in ker Gamma and psi != 0, then c(xi) psi_a = gamma_a chi for a trace spinor chi, and
  contracting with gamma^a gives -12 c(xi) chi = 0, impossible at q != 0. [W125 SA-C4 A1]

## 3. Persona 3 (higher-spin/causality specialist): SA-C4, built and passed

The spec's sharpest single gap was SA-C4: "the built cure term must survive subprincipal-order
causality (FC-VZ-4, the II_s-sourced spacelike characteristics); no test exists." The prior
leg (tests/vz_fcvz4_subprincipal.py) reduced FC-VZ-4 to a dichotomy -- the outcome is decided
by the DEGENERACY of the top-order constraint-reduced symbol -- and then BLOCKED, because the
Schur-elimination route needs the unpinned D_GU E-block.

**The wave's structural observation: the built candidate takes the other route, and that route
makes SA-C4 decidable.** The g = 1 cure enforces the constraint kinematically with a CONSTANT
(xi-independent) projector, so the reduced symbol R(xi) = K^dag M_D(xi) K on ker Gamma is
EXACTLY degree-1 homogeneous (machine-checked to 0.0): symbol degrees cannot mix, so a
zeroth-order II_s insertion is strictly subprincipal BY STRUCTURE, not by estimate. The test
(`tests/W125_sac4_subprincipal_built.py`, 9/9, exit 0) then computes:

1. **Off-cone non-degeneracy:** sigma_min(R(xi)) in [0.079, 0.50] for sampled q != 0 of both
   signs -- no characteristic off the null cone (the non-degenerate branch of the dichotomy
   OBTAINS for the built candidate).
2. **On-cone degeneracy:** an exact null covector gives sigma_min = 2.4e-27; approaching the
   cone along a fixed path, sigma_min falls monotonically by > 100x. Characteristic variety =
   the eta(9,5) null cone, exactly.
3. **Subprincipal immunity:** for an arbitrary zeroth-order II_s-type insert (unit spectral
   norm), the homogenized symbol returns R(xi) (residual 1.9e-7 at L = 1e6). Combined with
   (1)-(2): FC-VZ-4 cannot fire at subprincipal order on the built candidate.
4. **Positive control (the test has power):** a FIRST-order (principal-symbol-modifying)
   II_s-type insert kron(II_s, c(xi)) DOES drive sigma_min down 30x within the scanned
   strength window (0.143 -> 4.8e-3 at s = 1.6) while weak strengths leave the cone intact --
   the Velo-Zwanziger-type finite causal window is real and detectable by this machinery.
   This is the regime the Schur route (cure A) risks and the constrained route does not
   generate.

**SA-C4 status for the built candidate: TEST-BUILT-PASSES** at principal + subprincipal symbol
order on the flat 14-dim model. Honest boundary: the curved-Y14 statement rides the standard
fact that II_s enters the section-pulled operator as a zeroth-order tensor datum (prior leg,
Block B, cited not re-derived); if a future construction makes II_s enter at first order, the
window of (4) applies and SA-C4 reopens quantitatively. The repo-level VZ verdict
(CONDITIONALLY_RESOLVED) is NOT upgraded; the cure-A route stays blocked exactly as before.

## 4. Persona 4 (Krein/loop specialist): acceptance leg (d), what the built action makes computable

- **Tree [P,S] = 0 SURVIVES on the built object [COMPUTED]:** with K = eta_V x beta_S (the
  Cartan/Krein parity), [K, Pi] = 0 EXACTLY (0.0), and the full massive built symbol is
  Krein-self-adjoint: ||K O_built - O_built^dag K|| = 6.4e-15. The spec's Hom-disjointness of
  the FORCED set is verified on the built object at this level: adding the cure and the mass
  did not disturb the Krein structure. [W125 B2]
- **H59 minimum-packet items the built action now makes COMPUTABLE (not computed):**
  (i) ker-Gamma constraint closure under the dynamics -- built (that IS T1, g = 1);
  (ii) tree-to-renormalized [P,S] = 0 -- the tree side is now an explicit checked identity on
  an explicit operator, so the renormalized question is posed against a concrete object;
  (iii) the cubic vertex for the loop integrand exists explicitly (T3, the t* = -1/6 line).
- **Items the built action does NOT yet make computable:** counterterm closure under P, the
  odd/internal ghost-parity loop rule, the IR regulator + inclusive-observable layer -- these
  need the propagator and vertex ON Y14 (the covariant operator, not the flat symbol), which
  is the same missing object as acceptance leg (a)'s curved clause. Leg (d) is therefore
  PARTIAL, sharply: 3 of the packet's action-owned items land, the loop-arena items do not.

## 5. Persona 5 (honesty auditor, E1/Lakatos): ledger, scorecard, payoff, verdict

### 5.1 Consumption ledger (nothing silently consumed)

**DECLARATIONS -- 9/9 stated as named postulates** (machine-pinned in W125 assembly Block A):
SA-Y2 (k = 0; texture fork CARRIED OPEN), SA-Y5 (free-couplings branch taken; exclusive-or
with the larger-symmetry route recorded), SA-Y6 (flavor map postulated free), SA-Y8 (Majorana
spurion NOT included), SA-G1 (soldering POSTULATE), SA-C1 (carrier B POSTULATE, with the
equivariance certificate that the build did not manufacture it), SA-C3 (realized rank
postulated free in {1,3}), SA-U2 (ghost-mass fork CARRIED OPEN), SA-U5 (guardian-free branch
accepted openly: finite-cutoff EFT status).

**FORCED -- 8 rows:** SA-Y1 CONSUMED (T4, standing test rerun); SA-Y7a HONORED-BY-DEFERRAL
(no spurion term in the minimal candidate; type-forcing recorded); SA-G9 **UNMET** (named
blocker: the from-scratch massive spin-2 linearization with matter sources is not built --
even-sector work this odd-sector wave did not touch); SA-C2 BUILT (both facets: g = 1 kinetic
cure + the t* = -1/6 vertex revision); SA-C4 **TEST-BUILT-PASSES** (the wave's one status
movement); SA-U1 PARTIAL (section 4); SA-U3 NAMED-OPEN (the Krein-modified positivity bound
remains underived; note it could at most accept/kill the dimensionless point g = 1 -- it
cannot emit a scale); SA-U4 BUILT (T2).

**FITs -- 10 rows, emitted source-first: 0. All 10 named FREE.** The build pins none of
mu_DW, B_i, f0, beta/alpha, alpha, c_L, m2_eff, the vev, the y's, the spurion values.

### 5.2 Acceptance scorecard (spec 5.3)

| Leg | Status | Reason |
|-----|--------|--------|
| (a) g=1 cure realized, leakage 0, survives FC-VZ-4 | **PARTIAL** | leakage = 0 on the actual operator incl. mass (COMPUTED); SA-C4 test built and PASSES at principal+subprincipal symbol order -- but on the flat 14-dim model; the curved-Y14 clause rides an argued (cited) reduction, not a bundle computation |
| (b) every DECLARATION stated, none silently consumed | **PASS** | 9/9 named postulates + no-p-hack certificates (equivariance 0, theta-locus independence, residue trap intact) |
| (c) every FIT emitted source-first or named free | **PASS (with the E1 rider)** | all 10 named free; ZERO prediction-grade emissions -- the letter of (c) is met and its predictive content is empty |
| (d) H59 loop packet supplied | **PARTIAL** | tree [P,S]=0 verified on the built object; constraint closure built; vertex explicit; counterterm/loop-rule/IR items still blocked on the Y14 covariant operator |
| (e) standing machine checks pass unmodified | **PASS** | rerun this wave, all exit 0, untouched: wave17 14/14, wave35 15/15, spec-consistency 33/33, wave34, track2 T2A 8/8, vz_fcvz4, W102, W76 16/16. yukawa-scoping 20/20: VERIFIED-BY-PRIOR-RUN-UNMODIFIED-DEPS (same-day recorded exit-0 run; W125 touches none of its dependencies) |

**The acceptance criterion is NOT met** (legs (a) and (d) partial; SA-G9 unmet inside the
FORCED set). The candidate is a completed SYMBOL-LEVEL construction skeleton -- explicitly
"a partial fragment" in the spec's sense, now with the failure map exact: the single object
blocking (a)-full, (d)-full, and SA-G9 alike is the covariant operator on Y14 (the same
missing object FC-VZ-1 named).

### 5.3 The payoff question

**Gated numbers unlocked: NONE -- not even a one-sided bound.** And the reasons are now
machine-checked rather than felt (W125 assembly Block D): (i) causality pins a DIMENSIONLESS
point (the root g = 1 is invariant under xi -> 2 xi while C2 doubles); (ii) the built terms
introduce no new dimensionful coefficient (Pi idempotent and constant; g = 1 and t* = -1/6
pure numbers); (iii) the cure sector is Hom-disjoint from the gravity and Yukawa clusters, so
no equation of the candidate couples the cure to mu_DW, beta/alpha, or B_i. SA-U3, once its
Krein form is derived, bears on the sign/admissibility of g = 1, not on any scale. The first
source-action-derived NUMBER, if it ever comes, must come from the gravity cluster (SA-G9's
linearization emitting the matter coupling), not from the cure.

### 5.4 Epistemic-status verdict (the sentence)

**This build changes GU's epistemic status in exactly one narrow way and no other: SA-C4 --
a FORCED item that could have killed the built cure -- moved from "no test exists" to "test
built, PASSES for the built candidate at symbol level"; everything else in the wave is
assembly, which under the standing E1 rule is a construction, not progress, because zero FIT
rows became prediction-grade emissions and no gated number unlocked.** No FORCED item proved
unbuildable (SA-G9 is unbuilt, not shown unbuildable). The count stays {1,3}; H41 stays short
of acceptance 5.3; H59 stays OPEN; no canon, verdict, or posture movement.

## Honest limits

- Symbol level throughout: the "action" is an operator-and-vertex skeleton on the verified
  rep, not a functional on sections of the Y14 bundle. The three failing legs all trace to
  that one gap, which is the honest content of "PARTIAL".
- The SA-C4 pass is candidate-relative and model-relative: it certifies the BUILT (cure-B,
  constant-projector) candidate on the flat 14-dim symbol model with arbitrary zeroth-order
  inserts. It does not certify cure A, does not upgrade the repo VZ verdict, and reopens
  quantitatively (with a computed finite window as the instrument) if II_s ever enters at
  first order.
- The m2 in T2 is a stand-in numeric value in the test (0.7); the physical mass stays the FIT
  m2 = sqrt(m2_eff) mu_DW, and nothing in the wave narrows it.
- The Yukawa and spurion sectors are consumed by citation to their standing tests (W76 rerun
  exit 0 this wave; yukawa-scoping verified by its same-day recorded exit-0 run, no dependency
  touched); no new flavor computation was done here.
- W102's skeleton overlaps T0-T2; the wave's genuinely new computations are T3-as-test,
  the SA-C4 test, the Krein checks on the built massive symbol, and the payoff arithmetic.

*Filed 2026-07-13. Wave W125, five personas inline in one session. Reproducible:
`python -u tests/W125_built_candidate_assembly.py` (14/14, exit 0) and
`python -u tests/W125_sac4_subprincipal_built.py` (9/9, exit 0). Exploration-grade; no canon
movement; the spec document receives an append-only status note for the SA-C4 row only.*
