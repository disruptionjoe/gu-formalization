---
title: "Anchored-leads screen: all 6 sweep leads GATE on (or DIE before) the same unbuilt source action; none escapes it. Decision: ATTEMPT THE CARRIER-MASS BUILD -- no lead dominates it, all five live leads route INTO it. Spin(8) triality is the one standout (a real NEW bridge TYPE -- symmetry not pairing, type-correct equivariant integer that COULD force on the far side of the gate) but it too needs the twisted-RS complex; hold it as the integer TOOL to deploy once the source action exists."
status: active
doc_type: result
created: 2026-06-29
grade: "computed + adversarially verified. 6 leads x (initial-result + independent refutation) + meta-synthesis; 13 agents, ~829k tokens (workflow wf_48684ee0-87d); each lead ran python on the verified Cl(9,5)=M(64,H) substrate, all reproduced under refutation. Grades after refutation: spin8-triality GATED (maybe-build); tmf-elliptic GATED; km-n-geq-3 GATED; thooft-rg-lever GATED; sm-z6 DEAD; jones-subfactor DEAD. Zero PROMISING, zero genuinely-new source-action-free routes, NO fabricated 3. The screen's positive contribution is convergence, not a forcing route: five independent heterodox routes all terminate at the carrier Dirac-mass question."
method: "anchored-leads-screen workflow: 6 leads (Spin(8) triality; SM Z/6 global form; Jones subfactor in M(64,H); tmf/elliptic genus; KM n>=3; 't Hooft RG matching) -> initial check (python where possible) -> adversarial verify -> meta-synthesis ranking + carrier-mass decision."
depends_on:
  - canon/double-major-persona-sweep-RESULTS.md
  - canon/hessian-z3-carrier-occupancy-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
  - canon/forcing-slot-toy-rs-RESULTS.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - canon/two-primary-lemma.md
---

# Anchored-Leads Screen: Ranking, the Source-Action Gate, and the Carrier-Mass Decision

Six heterodox-but-anchored leads from the double-major sweep were screened for initial results, each graded
after an adversarial refutation pass. The decisive cross-cutting question for every lead: is it a genuinely new
route that could move LOCATED -> FORCED (or prove a type-correct smaller theorem) WITHOUT the unbuilt GU source
action, or does it re-locate / re-encode / gate on the same source action like every prior pass? All six
terminate at the same gate. None escapes it.

## 1. Ranking

| Lead | Final grade | New route? | One-line reason | Full build? |
|---|---|---|---|---|
| spin8-triality | GATED | n | Symmetry (not pairing) escapes the linking-form vanishing and gives a type-correct integer, but internal-fiber realization has frame charge exactly 0 and computing its index traces needs the unbuilt twisted-RS complex | maybe |
| tmf-elliptic | GATED | n | At generation degree 3, tmf = pi_3^s exactly (order-3 part IS e_R=1/12); co-varying q-coefficients are free-part cardinals mod 3 (kind-mismatch); only finer fragment gates on the source action | no |
| km-n-geq-3 | GATED | n | "n>=3" forcing needs an irremovable CP phase from the Yukawa/mass matrices (= source action); GU's one forced antilinear ingredient is a reality structure that REMOVES the phase (Jarlskog -> 0) | no |
| thooft-rg-lever | GATED | n | 't Hooft matching = the single-decider inflow computation in RG language; vacuous for the count (homogeneous in n_gen; surviving anomalies vanish; carrier vectorlike => zero 't Hooft anomaly) | no |
| sm-z6-global-form | DEAD | n | SM color-center Z/3 is the already-killed frame-trivial gauge Z/3 (frame charge 0, computed); a coprime product has Hom-between-factors=0, so "product not pairing" guarantees decoupling, not bridging | no |
| jones-subfactor | DEAD | n | M(64,H) is type I_finite not II_1 (Jones rigidity inapplicable); every GU-natural inclusion gives a 2-primary index, never 3; output is a fusion cardinal with no map to the order-3 carrier | no |

Three GATED, two DEAD, one GATED-with-a-live-residue. Zero PROMISING, zero genuinely-new routes.

## 2. The single most promising lead

**spin8-triality** is the only lead worth flagging forward, and only because the refutation pass surfaced a
correction the original report missed.

What makes it the standout: it clears the two bars that killed every prior pairing attempt. Triality is a
SYMMETRY (order-3 outer automorphism), not a linking PAIRING, so it is not bound by the coprime linking-form /
Hom(Z/3,Z)=0 vanishing that decouples canonical Z/8 <-> Z/3 maps. And an equivariant Lefschetz /
representation-valued index is a type-correct INTEGER in Z[omega], not a cardinal.

The original report claimed a third, structural ceiling: that the equivariant Lefschetz number is
deformation-invariant and therefore "blind" to the Dirac mass that separates located from forced, foreclosing
the route even past the gate. The refutation showed this is an OVERCLAIM (not a fabrication). The report's toy
assigned the same triality rep to both generations and their mirrors, forcing tr(g|H^0) - tr(g|H^1) = 0 BY
CONSTRUCTION, then read that engineered cancellation as a ceiling. But deformation-invariance is exactly the
FORCING mechanism of index theory: in a regular-rep configuration the equivariant index is -1, stable across
m = 0 -> 100, and a g-equivariant mass provably cannot lift the omega, omega^2 modes -> forced chirality. So a
NONZERO equivariant index in some omega-sector WOULD force.

What a full build would compute: triality's action on the ACTUAL twisted-RS complex H^i, and the equivariant
index ind_g = tr(g|ker) - tr(g|coker) decomposed into omega-sectors.

- CONFIRM (forces): a nonzero equivariant index in an omega-sector, with a proof that a g-equivariant Dirac
  mass cannot lift the protected modes -> rep-valued chirality protection -> the count is FORCED.
- REFUTE (re-locates only): the index vanishes in every omega-sector (as the internal-fiber frame-charge-0
  realization suggests it would, since triality there sits in the selector arena), confirming triality attaches
  a type-correct integer LABEL to the slot but does not fill it.

Critical caveat: computing those H^i requires the genuine twisted-RS complex, which IS the unbuilt source
action. So even the standout gates on the same object. Its value is as the most type-correct integer tool to
deploy ONCE the source action exists, not as a standalone build now.

## 3. Cross-lead patterns

The convergence is near-total and is the headline structural finding.

**All six gate on, re-encode, or die before the same object: the unbuilt twisted-RS source action.**

- spin8-triality needs the twisted-RS complex to compute its index traces.
- tmf-elliptic's only genuinely-finer fragment (higher-degree tmf 3-torsion) is geometry-dependent only once
  the geometry is pinned = the source action.
- km-n-geq-3's forcing route needs an irremovable CP phase that lives in the Yukawa/mass matrices = the source
  action.
- thooft-rg-lever IS the single-decider inflow computation re-described in RG language; the only inhomogeneous
  (forcing) source is the fixed bulk -p_1/24 inflow on GU's 14-manifold = the source action, sharpened to the
  carrier Dirac-mass question.
- sm-z6 and jones-subfactor are the two that die EARLIER, on type/frame-charge grounds, before even reaching
  the gate.

Two recurring sub-patterns explain the deaths:

1. **The frame-charge DECOUPLE recurs verbatim.** Every internal/gauge order-3 object computed -- triality's
   id_14(x)M, the SM color-center Z/3, the diagonal Z/6 -- has tangent-frame charge EXACTLY 0 by the same
   proven mechanism (Tr(L^dag)=0 for antisymmetric frame generators) that gave the +96 selector frame charge 0.
   They sit in the 2-primary selector arena and cannot feed the gravitational -p_1/24 channel where the carrier
   e_R=1/12 lives.

2. **The cardinal-vs-torsion type wall recurs.** Jones gives a fusion cardinal; the elliptic genus gives
   free-part integer modular-form coefficients (cardinal mod 3); the KM threshold is a U(n) parameter-count
   cardinal; 't Hooft matching is homogeneous in n_gen. None has a canonical map to the order-3 torsion summand
   Z/3 < pi_3^s. Hom(Z/3, Z) = 0, Hom(Z/6, Z) = 0, Hom(Z/2, Z/3) = 0 -- the same order-3-class -> integer-3
   category error, restated in five vocabularies.

**Does any lead genuinely escape the gate? No.** All routes terminate at the source action. The triality lead is
the only one that even reaches the gate carrying a tool (the equivariant integer) that could, in principle,
force on the far side -- but it cannot evaluate that tool without the source action.

One honest residue: a discrete Z/3 't Hooft anomaly could yield a mod-3 CONGRUENCE (a type-correct smaller
theorem, not the integer 3). The obvious 3*(B-L) proxy computes to 0 mod 3, and the real candidate
(baryon-triality / the Z/6=Z/2xZ/3 quotient) is the sm-z6 lead -- which is DEAD on frame charge. So the
congruence residue exists but its two tested realizations are both already killed, and at best it yields a
family {3, 6, 9, ...}, not 3.

## 4. The decision: is the carrier-mass build worth attempting now?

**Yes. Attempt the carrier-mass build. No lead here dominates it; all six route INTO it.**

Reasoning, weighed against the dominance test:

- **Does any lead offer a route to FORCE without the source action?** No. The only lead with a forcing
  mechanism on the far side of the gate (triality's nonzero equivariant index) cannot be evaluated without the
  twisted-RS complex, which is the source action.
- **Does any lead prove a type-correct SMALLER theorem without the source action?** No. The candidate smaller
  theorems are either dead-on-substrate ("net != 0 mod 3" is FALSE: computed net = 0, and 0 mod 3 = 0, robust
  under both gradings) or gate on the same object (KM "n>=3" needs the CP phase) or reduce to an already-killed
  realization (the Z/3 congruence -> baryon-triality -> frame-charge-0).
- **Do all leads gate on the source action?** Effectively yes -- four gate on it directly, two die before it on
  grounds that REINFORCE why the source action is decisive (the count cannot live in any frame-trivial or
  cardinal object).

Five independent heterodox routes, run to their honest ends, all point at one object: whether the GU source
action gives the vectorlike +96/-96 carrier a Dirac mass. The leads have done their job -- they ruled out the
side-doors and sharpened the gate. The 't Hooft lead in particular re-derives that the carrier is vectorlike
(computed zero 't Hooft anomaly), so e_R=1/12 is a genuine chiral coefficient ONLY if the carrier stays
massless. That is the carrier-mass question stated in anomaly language. The single-decider, the forcing-slot
test, the two-geometries reading, the Hessian test, and now five of six anchored leads all terminate at the
same Dirac-mass fork.

Recommendation: build the carrier-mass computation now (does the GU source action give the vectorlike carrier a
Dirac mass: massless -> modulus -> located; massive -> forced). Hold the triality equivariant index as the
type-correct integer tool to deploy on top of the source action ONCE it exists -- it is the right instrument for
reading FORCED off the result, but it is not a substitute for building the object, and it should not be
scaffolded standalone now.

## 5. Bottom line

Nothing here moves "located, not forced." Two leads (sm-z6, jones-subfactor) are dead on type and frame-charge
grounds before reaching the gate. Three (tmf-elliptic, km-n-geq-3, thooft-rg-lever) re-encode the existing
position and gate on the unbuilt source action. One (spin8-triality) is the most promising of the six -- a real
new bridge TYPE whose index could in principle force -- but it still cannot be evaluated without the twisted-RS
complex, so it too gates.

The screen's positive contribution is not a forcing route. It is convergence: five independent heterodox
routes, screened honestly with no fabricated 3, all terminate at the carrier Dirac-mass question. That makes the
carrier-mass build the right next move, and it makes the triality equivariant index the right tool to read its
result. The generation count remains LOCATED, NOT FORCED, and the gate is now as sharp and as singular as the
campaign has yet made it.

Scripts (all on the verified Cl(9,5)=M(64,H) substrate, all reproduced under refutation):
`tests/anchored-leads/spin8_triality_lefschetz.py`, `sm_z6_quotient_bridge.py`, `jones_subfactor_index_m64h.py`,
`tmf_elliptic_genus_covary_screen.py`, `km_n3_phase_and_reality_structure.py`,
`thooft_anomaly_matching_lever.py`. (Minor: the jones script attributes its G1 verdict to
`canon/no-go-class-relative-map.md`; the verdict actually lives in `canon/six-axis-escape-hatch-map-RESULTS.md`
-- claim correct, filename ref wrong.)
