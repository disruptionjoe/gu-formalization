---
title: "Design packet: positivity-exit criteria for the BRST/quotient route (M-H17)"
status: active_research
doc_type: design_packet
created: 2026-08-11
target: "M-H17 positivity/BRST exit criteria"
head_commit: bdd2c934335e6e534d4e0f9e7f55d7678eb566d8  # HEAD at drafting start (2026-08-11 17:12:35 -0500); the ledger advanced from v0.173 to v0.185 during drafting — every campaign citation below is pinned to a file opened at this commit
relates_to:
  - lab/process/improvement-register-2026-08-03.md (M-H17 row :352; M-H4 row :156; M-H4 rider :418)
  - lab/process/CURRENT-RESEARCH-CONTEXT.md (anchor fact 4, POSITIVITY↔BOUNDARY, :1679-1691; kinematic ≠ physical, :1638)
  - explorations/observable-algebra-commutant-trichotomy-2026-08-03.md (uniqueness + existence legs; the two exits)
  - lab/process/hostile-reviews/2026-08-03-trichotomy-review.md (the review that mandated register-tracking this exit)
  - explorations/chirality-grading-and-77-rerun-2026-08-03.md (DQ2: F = ∅ signature-robust; symplectic J-fixed carrier)
  - explorations/resolver-wave-b-q3-dq3-dq1-2026-08-03.md (DQ1: residual family dimension 12 on the Dirac-sense carrier)
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md (free-complex cohomology; quartet demotion channel)
  - explorations/rankN-krein-tt-for-gu-2026-07-11.md (definitizability; HORN Q vs HORN K)
  - explorations/five-lens-analytic-council-2026-08-08.md (Lens 3: the correct positivity type; M-H17 (ii)-(iv) runnable)
  - canon/ghost-parity-krein-synthesis.md (hyperbolic pairs; ghost parity = Cartan involution on the triplet)
  - explorations/conditional-build/conditional-physics-ledger-v0.164.md (ordinary-gauge Noether/BV ghost closure)
  - explorations/conditional-build/conditional-physics-ledger-v0.165.md (symmetrized preboundary form; small-gauge basicness)
  - explorations/conditional-build/selected-k77-wedge-shiab-southeast-completion-2026-08-11.md (v0.173; 960/960 null half)
  - explorations/conditional-build/selected-k77-unreduced-hyperbolic-domain-gate-2026-08-11.md (symmetrizer cone empty; BV reduction explicitly spared)
binding: >-
  Design input for a future wave. This packet binds no wave, makes no
  disposition, updates no register row, moves no verdict, residue, canon
  entry, or posture, and edits nothing outside itself. It supplies a criteria
  layer, an object table, and bounded check specifications; the executing
  wave owns every disposition under the full pre-flight / hostile-review
  contract, and anything approaching canon goes through the two-phase rule.
hostile_review: lab/process/hostile-reviews/2026-08-11-positivity-exit-criteria-design-review.md
canon_verdict_change: none
row_change: none
registry_change: none
---

# Design packet: positivity-exit criteria for the BRST/quotient route (M-H17)

The program's standing anchor (agent-context-pack.md:1679-1691) closes the
direct positivity route: no admissible fundamental symmetry exists on the
kinematic carrier (F = ∅, signature-robust), the classification leg says at
most one could ever have existed, and the exit is register-tracked as M-H17 —
the BRST/quotient exit, whose physical sector is a cohomology, not a subspace.
The hourly campaign is actively building the coupled BV/BFV/domain structure
for the K77 operator. This packet does NOT build any of that. It answers a
different question: **given whatever complex the campaign eventually
constructs, what conditions make its physical sector positive-definite, which
of those conditions can be tested NOW on existing exact banks, and what would
failure mean.** It is a requirements-and-criteria layer, not a construction.

## Pre-flight assessment

Failure modes this packet could commit, and the mitigations applied:

1. **Collision with the hourly campaign (the governing scoping constraint).**
   The campaign owns the construction: ordinary-gauge Noether/BV closure
   (ledger v0.164), the symmetrized preboundary form (v0.165), the completed
   wedge/southeast operator with its 960/960 null characteristic half
   (v0.173), and everything after. During the drafting of this packet the
   ledger advanced from v0.173 to v0.185 — the collision risk is measured,
   not hypothetical. Mitigation: every criterion below is stated as a
   condition on an *interface* (grading, differential, pairing) that any
   constructed complex exposes, never as a prescription for how to construct
   it; the packet's only runnable check (C1) consumes frozen `tests/`
   fixtures and touches no campaign surface (multi-writer protocol,
   AGENTS.md). Where the campaign's own Layer-0 lines already fence this
   packet's territory ("local BRST/BV closure is not global physical
   cohomology", v0.164; "the 960-dimensional null characteristic half is not
   gauge/BV cohomology", v0.173), the packet cites and inherits the fence.
2. **Comparator-horn leakage.** The only built BV bicomplex lives on
   `Cl(9,5) = M(64,H)`, DEMOTED to a conditional comparator on 2026-08-04
   with an explicit ban on importing its right-H/chosen-J machinery into
   `Cl(7,7)`; the register records that any H⁰ sign computed there is a
   comparator statement (improvement-register:352). Mitigation: C1's outputs
   are typed comparator-scoped at birth; the criteria themselves are stated
   pairing-agnostic so they transfer to the K77 side unchanged.
3. **False novelty.** `python3 lab/process/novelty-check.py` was run on
   "quartet pairing" (1 exact + 10 near), "no-ghost theorem" (19 exact),
   "definitizab" (790 exact), "positive quotient" (7 exact), "J-self-adjoint"
   (35 exact), "positivity exit" (0 exact — read per discipline as *unnamed*,
   not new: the object is register-tracked as M-H17). The criteria vocabulary
   exists in-repo, scattered across W173, rankN-Krein-TT, and the five-lens
   council; this packet's contribution is assembly, typing, and check
   specification, and the prior-art section states what is new relative to
   each hit.
4. **Layer-0 equivocation.** Load-bearing homonyms here: three "positivities"
   (state-space metric vs energy/symmetrizer vs probability), four objects
   under the letter C (NAMES.md), two ghost-clearance exits (quotient vs
   keep-and-grade), three differentials none of which is the interacting Q,
   and kinematic vs physical carrier. Mitigation: the object table below runs
   before anything else, per the six-axis Layer-0 precondition.
5. **Summary outrunning artifact.** The strong in-repo prior is that the
   free-level positivity check FAILS (the mirror survives in H⁰ with
   Krein-negative cross-pairing — W173; five-lens Lens 3 calls the expected
   result "a computed obstruction"). A failing free-level check is EXPECTED
   and is not a program kill; a passing planted control is instrument
   certification, not physics. The outcome table types both explicitly.
6. **Arguing around settled no-gos.** F = ∅ on the kinematic carrier is
   settled input, signature-robust. Nothing below re-litigates it; the
   no-go-navigation lens checks each criterion against W219, the uniqueness
   theorem, and DQ2 explicitly.
7. **Lens outputs treated as evidence.** The six lens sections below are
   planning evidence only — they organize criteria and cite artifacts; no
   scientific claim is licensed by a lens section itself.

## Layer-0 object table (run before use; six-axis precondition)

| term | object A | object B | object C | ruling for this packet |
|---|---|---|---|---|
| "positivity" | state-space metric positivity (six-axis L7: signature of the inner product on the state space) | energy positivity / positive symmetrizer (the cone proved EMPTY for the unreduced K77 Cauchy route, 2026-08-11 domain gate) | probability positivity (generalized/projector Born rule, Turok-Bateman) | this packet's target is A on the *physical sector*; B's kill is corroborating context only; C is the native-route criterion (PC-N below), never merged with A |
| "fundamental symmetry" | J ∈ F: a LINEAR commuting involution that is a positivity majorant on the kinematic carrier (the trichotomy's `F_A(η_V)` sense) | definitizing structure: a definitizable Gram operator admitting a spectral function (Langer) — an analytic property, automatic at finite rank | positive quotient: positive-definite *descended* pairing on H⁰(Q) — a cohomological property | three different objects. The no-gos (W219 + uniqueness + DQ2) kill A only. B is untestable on finite banks (Pontryagin collapse, rankN). C is this packet's subject and no filed no-go touches it |
| "the carrier" | kinematic carrier: `ker Γ`, dim 1664, exact fixtures | physical carrier: the gh-0 cohomology of the eventual interacting complex; `Π_RS^phys` does not exist — OQ-RK1 BLOCKED_NEEDS_SPEC (agent-context-pack:1638) | the campaign's K77 four-field carrier (dim 1920 rolled operator; 960/960 null half) | kinematic ≠ physical is repo-marked; criteria are stated on B as a function of the constructed complex; A hosts the finite shadows; C is campaign-owned |
| "the BRST charge Q" | the interacting nilpotent charge on the RS/ker Γ sector — M-H17 step (i), UNBUILT; its sole named blocker is C2 = 155.36 not closing without the Y¹⁴ connection-curvature 2-form | the built FREE BV differential `s = s_KT + s_long`, nilpotent on the (9,5) comparator (`tests/rs_bicomplex_explicit_koszul_tate_bicomplex.py`) | the campaign's source-typed local ordinary-gauge Noether/BRST differential, closing on `varpi, ζ, ν`, barred rows, and the nonabelian ghost (v0.164) — local, not global-physical | three differentials. Criteria are conditions on A; B and C are the stages where finite shadows of the criteria can run today; no result on B or C is a result on A |
| "ghost parity" vs "Krein parity" | ghost parity: the Z2 swapping generation ↔ mirror inside each hyperbolic pair | the Krein form K = η_V ⊗ β_S implementing the Cartan involution of so(9,5) | — | on the 192-triplet they coincide (canon synthesis V2, residual 0.0e+00) — one Z2 at kinematic grade — but they are distinct types, and NAMES.md records four objects under the letter C; no property transfers between senses without the synthesis' explicit identification |
| "the exit" | (A) BRST/quotient exit — standard covariant side: quotient to a positive H⁰ (Gupta-Bleuler, Kugo-Ojima). This is what M-H17 tracks | (B) keep-and-grade — the settled NATIVE ghost clearance (GEOMETER-VS-PHYSICS-OBJECTS.md:20): Krein grading kept, positivity at the probability level via `[P_ghost, S] = 0` + projector Born rule | — | the packet's primary criteria (PC-0..PC-6) serve exit A per the register brief; exit B's distinct criteria are typed separately as PC-N and never silently merged. The fork itself is a settled Layer-0 row; whether the physical answer lives on A or B is OPEN |
| "F = ∅" | the admissible set of positivity-majorant linear commuting involutions on the kinematic carrier is empty (Prop 1 applies; boost witness, exact `Re spec(D) = {±1/2, ±3/2}`) | a statement about the quotient/physical sector | — | A only. The trichotomy states this is the NORMAL covariant indefinite-metric situation (Gupta-Bleuler QED: `F_Lorentz = ∅`, yet unitary on the physical quotient). Reading F = ∅ as B is precisely the error the hostile trichotomy review corrected |

## State of the problem, compressed (every line cited)

- **The anchor.** "POSITIVITY↔BOUNDARY: the fundamental symmetry was never
  free (uniqueness theorem + W219); existence fails on the kinematic carrier
  (F = ∅, normal for covariant indefinite theories — Gupta-Bleuler; the
  BRST/quotient exit is now register-tracked as M-H17). UPDATED 2026-08-03
  (DQ2/DQ1, hostile-reviewed): F = ∅ is SIGNATURE-ROBUST (the boost witness
  transfers to (7,7)) … the canonical J-fixed carrier is SYMPLECTIC, closing
  M-H4's O(p,q) sign-forcing route" — verified verbatim at
  lab/process/CURRENT-RESEARCH-CONTEXT.md:1679-1691, HEAD bdd2c93.
- **The uniqueness theorem.** Commutant triviality gives at most one
  admissible fundamental symmetry (residual family dimension 0); neutrality
  (832,832) is STRUCTURAL (`ωβ + βω = 0` exactly, both chirality halves
  totally isotropic), so ±I both fail; the boost witness kills the rest
  (explorations/observable-algebra-commutant-trichotomy-2026-08-03.md, the
  classification/existence legs; strengthened by the hostile review's C4/C5).
- **Signature robustness.** Both legs transfer to (7,7): linear involutions
  stay {±I}, "at most one" rests on commutant triviality and transfers; the
  boost witness has exact `Re spec(D) = {−3/2,−1/2,+1/2,+3/2}` with
  multiplicities {64, 768, 768, 64} under (7,7); the enlargement is confined
  to an antilinear U(1) orbit that is not a residual modulus; the canonical
  J-fixed real form carries an Sp(1664,R)-type symplectic structure, not an
  O(p,q) form (explorations/chirality-grading-and-77-rerun-2026-08-03.md
  §2.2). Kinematic ≠ physical is stated in the same artifact (§2.3, §3).
- **The register item.** M-H17's five-step decomposition: (i) nilpotent
  interacting BRST charge Q on the RS/ker Γ sector; (ii) state complex;
  (iii) H⁰(Q) genuinely computed; (iv) nondegenerate descended pairing;
  (v) commutant + positive-pairing classification on the quotient. Named
  blocker: C2 = 155.36 does not close without the unbuilt Y¹⁴
  connection-curvature 2-form. Horn dependency recorded 2026-08-08: the free
  bicomplex is (9,5)-comparator machinery; it certifies s² = 0 but computes
  neither H⁰ nor the descended pairing
  (lab/process/improvement-register-2026-08-03.md:352).
- **The correct type, already identified.** Five-lens Lens 3 (2026-08-08):
  the re-typing of the kinematic no-go is REFUTED (J-language and
  positive-majorant language name the same object); the correct positivity
  type is "a BV/BRST differential whose gh = 0 cohomology is
  positive-definite on the Krein carrier"; M-H17 (ii)-(iv) is runnable now,
  ranked next-step 3, with a strong prior on a definite negative at the free
  level (explorations/five-lens-analytic-council-2026-08-08.md).
- **The free-level fact.** In the free BV bicomplex the mirror is
  BRST-closed, neither Koszul-Tate-exact nor ghost-exact (gauge orbit
  transverse to ker Γ, RS-symbol norms 73.48/343.73), hence survives in
  H⁰(s); a Kugo-Ojima doublet pairing demotes it (positive control C1-C4 in
  the W173 test); the sole demotion channel is the C2 closure
  (explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md).
- **The campaign side (input, not target).** Ordinary-gauge Noether/BV
  closure exists locally, including the nonabelian ghost (v0.164, with its
  own fence: "local BRST/BV closure is not global physical cohomology"); the
  symmetrized preboundary form is assembled and nondegenerate, the
  fixed-normal fermion reality is anti-symplectic and its naive extension
  fails on the mixed terms (v0.165); the completed wedge/southeast operator
  has a semisimple 960/960 null characteristic half and adjoint-defect rank
  1920 against the current diagonal pairing — reality adjoint and physical
  BV cohomology explicitly open (v0.173 exploration); the unrestricted
  southeast analysis shows the 896-dim right kernel is characteristic
  propagation, not a BV quotient (2026-08-11); the unreduced positive
  symmetrizer cone is EMPTY — with source-derived constraint/BV reduction
  explicitly spared by that kill (2026-08-11 domain gate); at v0.185 "no
  BV/KT cohomology or global domain follows" remains the campaign's own
  boundary. The pattern is uniform: positivity-adjacent structure fails on
  every unreduced object, and every kill spares the reduction.
- **The stakes, both directions.** Seat1 K6 (in the M-H17 row): positivity
  interior-supplied would END the boundary-supply reading — the kill most
  worth attempting. The converse is the falsification tripwire typed in the
  outcome table below.

## Criteria scaffolding

Everything in this section is planning evidence: it organizes conditions and
cites artifacts. No lens section licenses a scientific claim.

### Lens 1 — Krein operator theory: the criteria vocabulary

The standard ladder of positivity notions on an indefinite (Krein) space, and
what each is worth here:

- **J-self-adjointness / fundamental symmetry.** An operator (or algebra) is
  J-self-adjoint when a fundamental symmetry J intertwines it with its
  adjoint; an invariant J is equivalently an invariant positive majorant.
  This is the notion the program's no-gos already closed on the kinematic
  carrier (F = ∅), and five-lens Lens 3 certified that the two namings are
  one object. Well-posed on finite banks; settled; not the exit.
- **Definitizability.** A self-adjoint operator on a Krein space is
  definitizable when some polynomial in it is nonnegative; definitizable
  operators admit a spectral function (Langer — flagged for independent
  citation-check). On a Pontryagin space Π_κ (finite negative index) every
  such operator is definitizable — so **on the program's finite exact banks
  definitizability is automatic and carries zero information** (rankN
  finite-rank collapse, T1; five-lens: "at the fibre, definitizability is
  automatic and buys nothing"). It becomes contentful only on the open
  analytic domain, where it is exactly what is unproven (H59 has been
  definitizability-typed since 2026-07-12, per five-lens Lens 3).
- **Quasi-Hermiticity / bounded-invertible metric.** The rankN dichotomy:
  HORN Q (quasi-Hermitian: standard theory closes but the ghost is
  removable, keep-and-grade trivial) XOR HORN K (genuine kept ghost:
  keep-and-grade nontrivial, no spectral function guaranteed; the metric may
  have unbounded inverse — Krejcirik-Siegl shape, flagged for independent
  citation-check). Repo-native indication places GU on HORN K
  (explorations/rankN-krein-tt-for-gu-2026-07-11.md). Any analytic-stage
  positivity criterion must declare which horn it assumes.
- **Positive-definite invariant subspace vs positive quotient.** Maximal
  positive invariant subspaces of definitizable operators exist under
  spectral conditions (Bognar-era theory; in-repo cites in W132/W201) — but
  a *subspace* selection is the direct route the program closed. The exit
  object is the *quotient*: positivity of a descended form on cohomology,
  which requires no invariant subspace of the kinematic carrier at all.

Well-posedness typing: on finite exact banks, only ALGEBRAIC criteria are
well-posed (graded compatibility, descent, inertia of a descended Gram —
finite linear algebra, P-H29-clean). Spectral-function, definitizability, and
metric-boundedness criteria are well-posed only on the open analytic domain
and are typed needs-analytic-domain below. Every literature-grade fact in
this lens (Langer, Krejcirik-Siegl, Mostafazadeh, Bognar, Gupta-Bleuler,
Kugo-Ojima, Goddard-Thorn) is flagged **for independent citation-check**;
in-repo anchors exist for all but Goddard-Thorn, which has zero in-repo
mentions and must be sourced fresh if used.

### Lens 2 — BRST/homological: the standard exits as conditions on a graded complex

The three standard covariant exits, restated as conditions a complex must
satisfy — this is the packet's core deliverable. Data the eventual complex
must EXPOSE (the interface contract):

- **D1 (grading):** a Z-grading by ghost number with the differential
  homogeneous of degree +1.
- **D2 (differential):** Q with certified Q² = 0 at the stage tested.
- **D3 (pairing):** an indefinite pairing ⟨·,·⟩ pairing ghost number k with
  −k, with a declared sign convention for ⟨Qx, y⟩ vs ⟨x, Qy⟩. On the
  campaign side the candidate object is the v0.165 symmetrized preboundary
  form; on the comparator side it is the Krein form η_V ⊗ β_S.
- **D4 (quartet data):** for each Krein-negative direction at gh 0, the
  declared partner content (ghost/antighost pairing) — the data that decides
  pairing-off.
- **D5 (reality/adjoint):** the adjoint structure making D3 well-defined —
  currently OPEN on the K77 side (adjoint-defect rank 1920, v0.173), which
  is why the K77 criteria run is typed checkable-after-construction.

The criteria (each with its type: **now** = runnable on existing exact
banks; **post** = checkable once the campaign's complex exposes D1-D5;
**analytic** = needs the open analytic domain):

- **PC-0 (well-posedness).** D1-D3 exist and are mutually compatible. Type:
  now (comparator) / post (K77).
- **PC-1 (pairing compatibility).** Q is (anti-)self-adjoint for ⟨·,·⟩ in
  the declared convention, so that im Q ⊥ ker Q and the pairing descends to
  cohomology. This is the abstract form of the Gupta-Bleuler subsidiary
  condition's consistency (the physical subspace is defined by conditions
  compatible with the form). Type: now / post.
- **PC-2 (descent nondegeneracy).** The descended pairing on H⁰(Q) is
  nondegenerate — M-H17 step (iv) verbatim. Type: now (comparator) / post.
- **PC-3 (no-ghost / quartet completeness).** The inertia of the descended
  form on gh-0 cohomology is (n₊, 0, 0): every Krein-negative closed
  direction at gh 0 is exact — equivalently the negative-norm states pair
  off into BRST quartets that leave cohomology (Kugo-Ojima shape; the
  no-ghost theorems of string theory have this shape — Goddard-Thorn,
  citation-check required). This is THE positivity criterion; everything
  else is its preconditions. Type: now at free-comparator level (with the
  W173 prior of FAILURE there, which is diagnostic, not fatal — see Lens 6)
  / post for the interacting complex, where the verdict is the payoff.
- **PC-4 (cohomology concentration).** The descended pairing between H^k and
  H^{−k} is nondegenerate and physicality is read at gh 0 — without this the
  gh-0 restriction in PC-3 is meaningless. Type: post.
- **PC-5 (analytic implementability).** On the infinite-dimensional physical
  sector, PC-3's positive form must come with a Hilbert completion: a
  definitizable/quasi-Hermitian implementation whose metric has bounded
  inverse (HORN K is the risk case). Finite banks CANNOT test this — the
  Pontryagin collapse makes it automatic there. Type: analytic. Declaring
  PC-5 untestable-now is itself load-bearing: a wave that reports PC-3
  passing on a finite stage must carry a PC-5-open fence.
- **PC-6 (observable compatibility).** M-H17 step (v): the observable
  (constraint-preserving) algebra acts on H⁰ and the positive form is
  admissible for it, with the classification COMPUTED, not assumed — DQ1
  showed the Dirac-sense constraint-preserving algebra has three shared
  quaternionic compact types with residual family dimension 12, so
  uniqueness does not transfer to that carrier by default
  (explorations/resolver-wave-b-q3-dq3-dq1-2026-08-03.md §4). Type: post,
  with finite shadows runnable now on the DQ1 bank.
- **PC-N (native-route criteria, tracked separately).** Exit B
  (keep-and-grade) has different criteria: a ghost parity realized as a
  symmetry of the dynamics ([P_ghost, S] = 0), S Krein-diagonalizable with
  real SIMPLE spectrum (C non-unique at degeneracies — the sharpening in
  canon/ghost-parity-krein-synthesis.md), and projector-Born-rule
  positivity. These are dynamics-level, currently untestable (no S), and
  are listed so that a PC-3 failure is not misread as closing exit B.

### Lens 3 — symplectic/preboundary (repo-native): where the criteria touch the campaign's objects

- **The preboundary form is the pairing candidate.** v0.165's symmetrized
  boson-plus-four-fermion preboundary form is exact, algebraic, and
  nondegenerate — precisely a D3 candidate. Its own Layer-0 fence ("a
  preboundary potential is not its field-space exterior derivative"; "small-
  gauge basicness is not unrestricted BFV reduction") maps onto PC-0/PC-1:
  what the criteria need from it is only its interaction with the eventual
  differential, not any BFV reduction claim.
- **The anti-symplectic reality fact is a criteria input.** v0.165: the
  fixed-normal fermion reality is anti-symplectic, and its naive extension
  to the moving system fails exactly on the mixed terms. Combined with DQ2's
  symplectic J-fixed carrier, this means the criteria MUST be stated for a
  sesquilinear Krein pairing on the complex carrier, never for a real
  orthogonal form — an O(p,q)-shaped criterion has no object on the
  canonical fixed real form (M-H4 rider, improvement-register:418).
- **The 960/960 null half is upstream of, not equal to, the criteria's
  object.** v0.173's semisimple null characteristic half is characteristic
  propagation data; its own artifact fences it from gauge/BV cohomology.
  The criteria consume whatever cohomology the campaign builds OVER such
  data; they never read the null half itself as a physical sector. Same for
  the 896-dim right kernel (southeast analysis) and the dim-256 fermion
  radical left by the edge quotient (radical-BFV ownership gate) — each is
  a candidate *ingredient* for the eventual complex, and each already
  carries a campaign fence against exactly the misreading PC-0 would catch.
- **The ghost sector exists locally.** v0.164's ordinary-gauge differential
  closes on the nonabelian ghost — so D1/D2 data exist at local-symbolic
  grade on the K77 side; what is missing for a criteria run is D3-with-D5
  (a pairing with a selected reality adjoint; adjoint-defect 1920 says not
  yet) and a finite assembled stage.
- **The first finite host.** The existing exact bank that can host the first
  criteria check is the comparator free BV bicomplex
  (`tests/rs_bicomplex_explicit_koszul_tate_bicomplex.py` machinery, s² = 0
  certified) together with the 192-dim triplet Krein bank
  (`tests/generation-sector/ghost_parity_krein.py`: 96 hyperbolic pairs,
  signature (+96, −96, 0)) and the W173 fixture set
  (`tests/W173_brst_cohomology_mirror_sector.py`, whose Part C already
  contains a doublet-pairing positive control). Check C1 below is specified
  on exactly these.

### Lens 4 — no-go navigation: what died, and that this layer does not argue around it

What W219 + the uniqueness theorem + DQ2 killed, restated exactly:

- W219: at the kinematic Cartan level the centralizer is Sp(32) × Sp(32) and
  the admissible grading is unique at canonical compact level; the dynamical
  good-stable stabilizer is UNDEFINED — no object exists on which a
  dynamical-reduction positivity could currently be computed.
- Uniqueness (trichotomy): at most one admissible linear commuting
  involution; and the existence leg returns F = ∅ via the boost witness,
  with structural neutrality (832,832) forced by the Clifford algebra.
- DQ2: both legs are signature-robust; the Kramers wall is (9,5)-only; the
  canonical J-fixed carrier is symplectic, closing M-H4's O(p,q)
  sign-forcing route on that fixed real form.

This packet's criteria layer does not contradict any of these: PC-1..PC-6
quantify over the descended pairing on a cohomology, an object none of the
above theorems addresses. The trichotomy itself names the BRST quotient as
the second standard exit it did not build, and the hostile review made
omitting it a correction — the criteria layer is the register's own next
move, not an evasion. F = ∅ on the kinematic carrier is treated everywhere
below as settled input; no check below re-tests it, and outcome (b) of C1
explicitly routes any apparent conflict to a hand audit rather than a claim.

### Lens 5 — Layer-0 (already run above)

The object table at the top of this packet is this lens's output; the wave
re-runs it as its own precondition. The three rows that have historically
bitten: fundamental symmetry vs definitizing structure vs positive quotient
(this packet exists because they were conflated in one row text — five-lens
found U11 stale on exactly this); the free s vs the ordinary-gauge
differential vs the interacting Q; and quotient-exit vs keep-and-grade.

### Lens 6 — failure meaning (the tripwire, typed)

- **Free-comparator PC-3 failure (expected).** Confirms W173
  quantitatively: at the only level GU currently determines, the mirror is
  physical-and-negative, so interior positivity via exit A depends entirely
  on the interacting pairing term (the C2 closure / Y¹⁴ curvature — the
  same one object). Not a kill; the diagnostic that converts "BRST might
  rescue positivity" into a named burden.
- **Interacting PC-3 unsatisfiable (the tripwire).** If, once the campaign's
  complex exists, PC-3 is PROVABLY unsatisfiable over the source-admitted
  action family (not merely unverified), then interior-supplied positivity
  on exit A is dead. Type: FALSIFICATION TRIPWIRE for the interior reading —
  the surviving options become exactly the program's two standing escapes:
  exit B (keep-and-grade, criteria PC-N, dynamics-gated) and the
  boundary/firewall supply (canon/firewall-boundary-hypothesis.md; the
  deny-Prop-1 escape named in canon/good-stable-compactification-no-go-RESULTS.md).
  If those also close, the program fails at the physical tier. The converse
  payoff is equally typed: interacting PC-3 satisfied ends the
  boundary-supply reading (seat1 K6 — "the kill most worth attempting").
- **Partial / sector-wise positivity.** If PC-3 holds on a proper
  subsector (e.g. positive on singlet/doublet blocks, failing exactly on
  the mirror-paired triplet), the reading is superselection-sector-wise
  physicality: the ghost-parity Z2 becomes a superselection datum and the
  operative quantization shifts to exit B's generalized Born rule (six-axis
  L7 menu (b)). That outcome would fuse the two exits rather than decide
  them — positivity where the quartets close, keep-and-grade where they do
  not — and its disposition belongs to the wave and the register, not this
  packet.

## First decisive steps (bounded; a wave can implement independently)

**C1 — the criteria instrument, certified on existing exact banks.**
Implement a checker taking (graded space, differential, pairing) and
returning: PC-0/PC-1 booleans, H^k ranks, the descended Gram on H⁰, and its
inertia. Run five configurations:

- R1: the free BV bicomplex fixtures (comparator (9,5)) — expect PC-0/PC-1/
  PC-2 PASS and PC-3 FAIL with negative inertia carried by the mirror
  classes. The descended H⁰ Gram inertia is the NEW number: W173 established
  closed-not-exact membership, and the register records that no artifact has
  computed H⁰ or the descended pairing (improvement-register:352). This is
  M-H17 steps (iii)-(iv) executed at comparator scope — the five-lens ranked
  item 3.
- R2 (planted positive control): extend the differential by the W173 Part-C
  doublet pairing δ (the Kugo-Ojima quartet) — PC-3 must FLIP to PASS on the
  paired sector. Certifies the checker can see a pass.
- R3 (planted negative control, mandated): a deliberately NON-quartet
  pairing — either a differential pairing two Krein-negative directions with
  each other, or a Q violating the declared adjointness convention — must
  FAIL PC-1 or PC-3. An instrument whose R3 passes is dead.
- R4 (invariance control): Krein-sign flip must leave all verdicts invariant
  (the W173 D6/D7 shape — exactness is a property of the images, not the
  metric sign).
- R5 (degenerate-input control): feed a positive-definite pairing — no
  negative inertia may appear anywhere (the W173 D4/D5 shape); and feed the
  DQ2 symplectic real form where a sesquilinear Krein pairing is required —
  the checker must raise a TYPE error, not a number (the M-H4-rider trap).

Kill conditions, declared before computation: R2/R3 failing to separate
kills the instrument (no science read); any R1 number cited as K77-primary
violates the comparator scope and must be retracted; all runs are exact
finite linear algebra (P-H29-clean, no FD reads). Cost: hours; consumes only
frozen `tests/` fixtures; writes nothing on any campaign surface.
P-H28 compliance: C1 moves a NAMED register item (M-H17 steps (iii)-(iv), at
comparator scope) — it is schedulable as stated.

**C2 — horn-transfer statement (analysis, no new computation).** Restate the
PC ladder against the DQ2 (7,7) bank objects (J, β = i·e_0…e_6, the
symplectic V^J) to certify the criteria are pairing-agnostic as written —
i.e. nothing in PC-0..PC-6 presupposes an O(p,q) real form or the (9,5)
right-H machinery, so the ladder ports to the K77 side unchanged when its
D5 (reality adjoint) is selected. Deliverable: one table in the wave's
artifact; the R5 type-error control is its computational shadow.

**C3 — the interacting run (specified now, executable only
post-construction).** When the campaign's K77 complex reaches a finite
assembled stage exposing D1-D5, run the SAME checker unchanged and read
PC-0..PC-4; PC-5 remains fenced open at any finite stage; PC-6 runs against
the campaign's constraint-preserving algebra with the DQ1 residual-family
caveat. Pre-registered both ways per the outcome table. This packet does not
schedule C3; the campaign's own gate chain owns when its complex exists.

## Outcome table (graded; every disposition wave-owned)

| outcome | reading | disposition owner |
|---|---|---|
| C1-R1: PC-3 fails with mirror-carried negative inertia (expected) | W173's prior becomes a computed inertia; M-H17 (iii)-(iv) DONE at comparator scope; burden named: the interacting pairing term (C2/Y¹⁴ object) | wave files result + hostile review; register row annotation proposed, not executed |
| C1-R1: PC-3 unexpectedly PASSES at free level | contradicts W173's closed-not-exact reading — mandatory hand audit before any citation (the DQ2 unbalanced-result protocol); either the checker or the 2026-07-14 chain is wrong, and that is itself major information | wave, with an escalation per the over-determined-row rule |
| C1-R2/R3 fail to separate | instrument dead; no science read; packet's C1 spec returns for repair | wave |
| C3 (eventual): PC-0..PC-4 all pass on the interacting complex | interior-supplied positivity at algebraic grade — seat1 K6 payoff: ENDS the boundary-supply reading at that grade, PC-5 still open | wave under the verdict-flip contract (hostile specialist review mandatory) |
| C3 (eventual): PC-3 provably unsatisfiable over the admitted action family | FALSIFICATION TRIPWIRE fires: exit A dead for the interior; survivors are exit B (PC-N, dynamics-gated) and boundary/firewall supply; both closing = physical-tier program failure | wave + register; nothing in this packet pre-judges it |
| C3 (eventual): sector-wise pass | superselection reading; hand-off to exit B criteria (L7(b), generalized Born rule); fusion outcome | wave |

## Why the direct route died (cited)

1. Weyl unitarian trick: the indefinite Krein form exists only because the
   internal group is non-compact — dropping Hilbert positivity is a
   DG-A3 scope exit, so no compact-group rescue exists
   (canon/ghost-parity-krein-synthesis.md, A0 audit).
2. Classification: commutant triviality leaves {±I} as the only linear
   commuting involution candidates — at most one admissible fundamental
   symmetry (trichotomy, elementary warrant substituted by the hostile
   review; transfers to (7,7) because it rests on commutant triviality, DQ2).
3. Existence: both ±I fail by structural neutrality ((832,832) forced by
   ωβ + βω = 0), and the η_V-skew boost witness (exact
   Re spec = {±1/2, ±3/2}) kills every remaining invariance structure
   containing it — Prop 1 APPLIES and returns F = ∅; signature-robust (DQ2
   D-5/D-6). Gupta-Bleuler QED is the normality precedent: F_Lorentz = ∅ on
   the covariant space, unitary on the physical quotient (trichotomy §3).
4. The dynamical escape is not currently an object: the good-stable
   stabilizer is undefined (W219), and the sign-forcing hope on the
   canonical J-fixed (7,7) real form closed symplectically (DQ2; M-H4 rider).
5. Native cores cannot supply the missing grading dynamically: PT-unbroken
   yet spectrally sign-blind, C non-unique at the three-generation
   degeneracy (big-swing R3 via canon synthesis banner and W173 §3).

Hence the exit lives in the quotient — and the physical carrier does not
exist yet (OQ-RK1 BLOCKED_NEEDS_SPEC), which is why the deliverable here is
criteria, not a construction.

## Prior art

In-repo (enumerated; what this packet adds is stated per item):

- W173 + `tests/W173_brst_cohomology_mirror_sector.py` — free-complex
  cohomology of the mirror; quartet demotion as positive control. New here:
  the descended-inertia number is specified (W173 decided membership, not
  inertia), and the controls are reorganized into a reusable criteria
  instrument with a mandated non-quartet planted failure.
- Improvement register M-H17 row — the five-step decomposition and horn
  dependency. New here: the steps are refined into the PC ladder with
  per-criterion testability types and an interface contract (D1-D5).
- Five-lens council Lens 3 — the correct positivity type (CB-B's), the
  runnability of (ii)-(iv), the strong negative prior. New here: the
  criteria are written out, typed, and bound to planted controls; the
  analytic fence (PC-5) is made a named criterion rather than a remark.
- rankN-Krein-TT + branch4/steelman1 — definitizability, Pontryagin
  collapse, HORN Q/K. Consumed as the reason PC-5 is finite-untestable.
- Trichotomy + its hostile review — uniqueness/existence legs, the
  Gupta-Bleuler normality reading, and the mandate that created M-H17.
- DQ2 / DQ1 — signature robustness; the symplectic J-fixed carrier; the
  residual-family-12 caveat consumed by PC-6.
- W219, W207, W132, W235, W177, W184 — stabilizer gate; the decisive-bit
  BRST method (H⁰ not genuinely computed there, per the register); the
  expansion identity A†A = P₊ + B†B pricing retention; record-vs-redundancy;
  C2 construction; mirror superselection decay.
- canon/ghost-parity-krein-synthesis.md + six-axis L7 — the keep-and-grade
  exit's own criteria ([P,S] = 0, simple-spectrum sharpening), consumed as
  PC-N.
- Campaign artifacts v0.163-v0.185 (esp. v0.164 ghost closure, v0.165
  preboundary, v0.173 wedge completion, the southeast/radical/domain gates
  of 2026-08-11) — the construction this packet's criteria will eventually
  consume, cited with their own fences inherited.

Literature (ALL flagged for independent citation-check by the executing
wave; none is load-bearing for any claim graded CONFIRMED below):
Gupta-Bleuler subsidiary conditions; Kugo-Ojima quartet mechanism (PTP
Suppl 66, 1979 — in-repo cite exists in W173); Henneaux-Teitelboim 1992;
Langer's definitizable-operator theory; Krejcirik-Siegl PRD 86 (2012);
Mostafazadeh quasi-Hermiticity; Bognar 1974 (in-repo cites in W132/W201);
Bateman-Turok arXiv:2607.00096; Goddard-Thorn no-ghost theorem (NO in-repo
mention — must be sourced fresh if cited in any wave artifact).

## What this packet does not do

It does not construct, modify, or schedule any part of the BV/BFV/domain
build: no differential, no pairing, no domain, no ghost sector, no reality
adjoint, no quotient is built or prescribed here — the hourly campaign owns
all of it, and this packet's criteria are deliberately stated as conditions
on an interface (D1-D5) so that ANY complex the campaign lands can be tested
without this packet having predicted its shape. It does not run C1 (a wave
does, independently); it does not move M-H17, M-H4, any ledger row, verdict,
residue, canon entry, or posture; it does not adjudicate quotient-vs-keep-
and-grade; it does not touch F = ∅ or any settled no-go; and it creates no
NEEDS_JOE state. The packet is one file in the side-session scratch lane; it
edits nothing inside the repository.

## Verify status manifest (absorption protocol)

- Anchor fact verbatim at agent-context-pack.md:1679-1691; M-H17/M-H4 rows
  and rider at improvement-register:352/:156/:418; kinematic ≠ physical at
  agent-context-pack:1638 — **CONFIRMED** (opened at HEAD bdd2c93).
- Trichotomy legs, hostile-review corrections, Gupta-Bleuler normality
  reading, the two-exits sentence — **CONFIRMED** (files opened; hostile
  review verdict block read).
- DQ2 results (signature-robust F = ∅, exact boost spectrum, symplectic
  V^J, antilinear U(1) orbit) and DQ1 residual-dimension-12 — **CONFIRMED**
  (both explorations opened; numbers transcribed from §2.2 and §4).
- W173 free-complex facts (closed-not-exact, transversality norms
  73.48/343.73, quartet demotion control, C2 = 155.36) — **CONFIRMED** as
  file content; the underlying computations are the cited tests, not re-run
  here.
- Free bicomplex computes neither H⁰ nor a descended pairing — **CONFIRMED**
  by register row and by grep of the 413-line test file (no H⁰/descended
  symbols).
- Campaign facts (v0.164 ghost closure; v0.165 preboundary nondegenerate,
  anti-symplectic reality; v0.173 960/960 and adjoint-defect 1920; southeast
  896 kernel typing; symmetrizer cone empty with BV reduction spared; v0.185
  "no BV/KT cohomology or global domain follows") — **CONFIRMED** as ledger/
  exploration content at HEAD; all are campaign-owned conditional results.
- The PC ladder, D1-D5 interface, C1/C2/C3 specifications, outcome table,
  and tripwire typing — **PROPOSED** (design; no computation run in this
  packet; the wave implements independently).
- The claim that C1 is hours-scale and moves M-H17 (iii)-(iv) at comparator
  scope — **SCOPED** (follows the five-lens ranked-item-3 assessment and the
  register's "steps (ii)-(iv) are runnable"; not independently timed).
- Literature-grade statements (Langer, Krejcirik-Siegl, Kugo-Ojima,
  Goddard-Thorn, Bateman-Turok) — **SCOPED**: carried on in-repo citations
  where they exist, flagged for independent check; none is load-bearing for
  a CONFIRMED line.

## Self-hostile review

Filed separately per repository convention: `lab/process/hostile-reviews/2026-08-11-positivity-exit-criteria-design-review.md` (the three standing charges, same-run).
