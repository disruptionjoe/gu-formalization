---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-17
work_item: WB-1
channel: wall-bill
wave: wall-bill W1 arc of RS wave 2
title: "WB-1: W1's crossing requirement, typed for the VEV-orientation wall. The object that must flip is NOT R's sign — it is the vacuum-component label of the order parameter phi (which connected component of the vacuum set the VEV sits in, locally), and 'sign-crossing zero' becomes a transversal zero of phi at which that pi_0-label jumps, entirely inside a one-signed R < 0 region (measured: a phi-kink under R = -4(2+tanh y) < 0 everywhere hosts exactly 1 while chain-1's m = R/4 on the same region hosts exactly 0). Rung-2's 'unfixable orientation Z/2' is a DEGENERACY-AND-UNSELECTABILITY theorem, not a flip-REALIZATION theorem — in the one run where a flip exists, the flip was the frozen INPUT (prereg:51-52 boundary sector; probe:138 endpoint pinning), and the run's own verdict SECTOR-SUPPLIED types the realization as an external supply. R-steering cannot pay the relocated bill: the source's stated coupling (quartic + R-set quadratic, drafts:146/:149) enters even in phi, and E[-phi] = E[phi] EXACTLY for arbitrary lambda(y), v(y) — even modulation steers location while provably never forcing or preferring an orientation; the only phi-odd source datum is chain-1's m = R/4, which reimports the R-crossing RW-1 certified absent. New certified absence: over all eight Weinstein primary surfaces the VEV-FLIP and VEV-NEGATIVE families score ZERO and the VEV language is exclusively one-sided magnitude ('significantly above zero', 'decreased VEV' — exactly 5 hits, all the same two utterances). VERDICT ON W1: RELOCATED to an external Z/2 sector datum (= winding mod 2, exactly the oddness-carrying external datum canon's decomposition requires), with a stacked gate OPEN: pi_0 of the NATIVE varpi vacuum set is uncomputed and the repo's two proxies pull opposite ways (rung-2's disconnected {+-v} is an INPUT; VG-V5's candidate coset D is measured CONNECTED). Kill branch named, not fired."
grade: "EXACT where computed (sympy: the evenness identity I(-phi) - I(phi) = -2 g phi for arbitrary lambda(y), v(y); the composite hosting rows with exact modes and integrals; the sector-parity identity verified EXHAUSTIVELY over all sign sequences to length 12; the winding functional's endpoint-only dependence). CERTIFIED where scanned (the VEV-orientation scan over the eight primary surfaces with a planted positive and two planted near-misses). MACHINE-EXACT where numeric (E_lambda[-phi] == E_lambda[phi] bitwise under even modulation; location spread > 0 under the same modulation). FLOAT-GRADE only in the rung-2 re-run (the repo's own instrument, exit 0). The comparator binds the model only (routing fence below). NO claim-status movement, NO register edit, NO canon movement, NO kill."
disposition: W1_CROSSING_RELOCATES_FROM_R_SIGN_TO_PHI_VACUUM_COMPONENT_LABEL__RUNG2_PROVED_DEGENERACY_AND_UNSELECTABILITY_NOT_REALIZATION__SECTOR_SUPPLIED_TYPES_THE_RELOCATED_ITEM_EXTERNAL__EVEN_R_STEERING_CAN_NEVER_PAY_IT__PI0_NATIVE_VACUUM_GATE_OPEN__NOT_A_KILL
target_claim: "RW-1's bill item W1, verbatim: 'W1 — a sign-crossing zero (the load-bearing missing item). The mass profile must cross zero with odd winding on a codimension-1 locus.' (lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md:260-262, continuing through :269 'Status: OPEN, not forbidden')."
target_claim_verdict: "SURVIVES-RETYPED, NOT-A-KILL. W1 stands as stated for the generic Jackiw-Rebbi consumption. For the VEV-orientation wall specifically, the flipping object is typed (phi's vacuum-component label, not R's sign; the two live in different spaces and index different interfaces), and the item RELOCATES: rung-2's proved existence condition does NOT supply the crossing — it proves the crossing-equivalent datum (the boundary sector) is exactly what the action cannot select, i.e. it types the relocated W1 as EXTERNAL-CLASS. W1's 'OPEN, not forbidden' status is refined to RELOCATED-TYPED-EXTERNAL with a named pi_0 gate; the kill branch is named and does not fire today."
canon_verdict_change: none
row_change: none
registry_change: none
steering_effect: unchanged
canonical_effect: pending_integration
scripts:
  - tests/channel-swings/joe_directed_wb1_crossing_is_a_sector_datum_r_cannot_supply.py
inputs:
  - lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md
  - tests/channel-swings/joe_directed_rw1_zero_locus_steers_not_hosts.py
  - explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md
  - tests/channel-swings/rung2_dynamical_wall_selectability_probe.py
  - explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md
  - explorations/decoupling-constructibility-packet-2026-08-12.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - CANON.md
  - lab/methods/gu-base-categories.md
  - lab/sources/source-claim-register.yaml
  - lab/process/correction-registry.yaml
  - papers/drafts/Transcript into the impossible.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - explorations/big-swing-2026-07-06/VG-V5-breaking-coset-topology.md
  - explorations/time-as-finality-crosswalk/ten-perspective-steelman-live-dark-observer-sheaf-2026-07-15.md
  - explorations/adapter-assumed-four-leg-swing-2026-07-19.md
  - explorations/shard-cycle-prong1-geometry-2026-07-21.md
  - VERIFICATION.md
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result. Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.
>
> The comparator here (§4) is the rung-2 standard-field wall system — the
> double-well energy functional and the 1D Jackiw-Rebbi hosting judge on the
> repository's own operator class, the same instruments rung-2 and RW-1 §4
> already fenced — with the SOURCE's own potential-shape ingredient (quartic +
> curvature-set quadratic, drafts:146/:149, SC-GEO-58). Its results bind that
> model. They adjudicate what the W1 crossing requirement IS for the
> VEV-orientation wall and who can pay it, not whether GU realizes the wall.
> The Mexican-hat form is the stylized shape the source itself asserts
> curvature produces (drafts:149); it is typed `FENCED-COMPARATOR` wherever
> consumed. The (9,5) transport gap is rung-2's own declared fence
> (prereg:43-45) and is inherited unchanged.

# WB-1 — W1 for the VEV-orientation wall: what must cross, who proved what, and who can pay

**What this is.** RW-1 re-aimed the R(y)/wall join at a named construction
target — "VEV-orientation (Z/2) domain walls inside the broken region,
steered by R(y)" (rw1:457) — and named W1 ("a sign-crossing zero — the
load-bearing missing item") as one of the two items on which the target can
die. This artifact executes W1 alone: (a) it types EXACTLY what object must
flip for the VEV-orientation wall (not the refused R-constituted wall);
(b) it adjudicates whether rung-2's proved "unfixable orientation Z/2"
supplies that flip, relocates it, or leaves it open; (c) it types what R(y)
must do for the wall to exist versus merely be steered, and measures what R
provably can never do; (d) it renders the W1 verdict with the kill branch
stated; (e) it applies the CC-05 fence to every count-adjacent statement.
The answer, measured: **the crossing requirement survives, changes variable
(from R to phi), changes type (from a missing source assertion to an
external sector datum), and lands exactly on the shape canon already
requires of any odd count — external by structure.**

---

## 0. PREFLIGHT — six problem-matched lenses, declared before the work

- **L1 — Interface-vs-phase topologist.** The wall literature hosts on
  interfaces BETWEEN vacua, not on phase boundaries; predicts the two
  candidate interfaces ({R = 0} and {phi = 0 inside R < 0}) are different
  objects with different hosting behavior and W1 must be typed against the
  second. Confirmed and measured: the same broken region hosts 1 via phi's
  crossing and 0 via chain-1's one-signed m = R/4 (§4b) — the two interfaces
  separate cleanly in one computation.
- **L2 — Theorem-typist (the (b) lens).** "Existence condition proved" can
  name three different theorems: choice-degeneracy, flip-realization, or a
  global orientation obstruction. Predicts rung-2 proved only the first.
  Confirmed with byte pins: the prereg's own wording is degeneracy language
  ("exactly degenerate", prereg:63-64), the flip in the run was a frozen
  INPUT (prereg:51-52; probe:138), and the verdict token SECTOR-SUPPLIED is
  the probe's own typing of the realization as external (§2).
- **L3 — Symmetry auditor (even/odd in phi).** Every claim "R steers/sizes/
  locates the wall" must state whether the R-coupling is even or odd in the
  order parameter, because only an odd term can prefer an orientation.
  Predicts the source's stated coupling is even and the rung-2 N2 instrument
  term is odd — an instrument/carrier seam nobody had typed. Confirmed
  exactly (§3, §4a): the evenness identity holds for arbitrary lambda(y),
  v(y); the N2/N1 term g·y·phi is the odd one; the location-selection
  CONCLUSION transfers to even modulation (measured, §4d) while the
  orientation-selection power does not exist to transfer.
- **L4 — Coverage archaeologist (grep before novelty).** Found four things
  that materially changed this artifact (§9): the repo already holds a
  CONNECTED candidate vacuum manifold for the decreased-VEV datum (VG-V5:75)
  — the anti-Z/2 data point; a Kibble-Zurek domain argument at perspective
  grade with INVERTED polarity on a different Z/2 (KZ steelman:104-107); the
  "Z/2 sector datum" vocabulary precedent (adapter:29-36, p2c); and a
  nontrivial-w_1 forcing result in the shard-cycle lane (shard:125) — the
  T-OBST theorem-shape exists in-repo for a DIFFERENT bundle. Without L4
  this artifact would have claimed two false novelties and missed the
  pi_0 gate entirely.
- **L5 — Hostile self-auditor (the import lens).** The named attack: "you
  are importing the Kibble-mechanism expectation that spontaneous Z/2
  breaking automatically yields walls." §5 runs it; the measured guards
  point against the import: the Z/2 itself is an INPUT at rung-2 (the
  double-well is a frozen declared input, prereg:51), the repo's one
  GU-shaped vacuum-manifold measurement came back CONNECTED (no Z/2 at
  all in that model), and the source's own "sub-fields" plural (register:922)
  points at a multi-component order parameter whose Mexican hat generically
  has a CONNECTED vacuum set. The honest output is a gate, not a wall.
- **L6 — Homonym warden.** "The VEV" is a registered multi-sense term
  (packet:70: (i) varpi sub-fields / (ii) spoken Dirac-operator VEV /
  (iii) curvature-coaxed augmented-torsion VEV / (iv) repo weight pair), and
  "chirality" is the registered four-way homonym (packet:69). Predicts the
  order parameter of the VEV-orientation wall must be typed against (i)/(iii)
  without silently identifying them, and the wall grading question (RW-1's
  W3) must not be re-opened here. Held throughout: this artifact types the
  orientation space (§1), does not identify the VEV senses, and inherits W3
  untouched.

Retrieval-first was run before any computation, including
`process_gates/canonical_currency_audit.py` over all consumed inputs; the
per-input records are §10.

**Frame carried (quoted; the three standing corrections this lane most
touches, from `lab/process/correction-registry.yaml` key
`canonical_source_corrections`):**

- **CC-06-CHIRALITY-VEV-CONDITIONAL** (canonical_since 2026-08-16), superseded
  reading quoted: *"That the source has no stated effective-chirality
  mechanism, or that chirality can only come from an unbuilt mirror-gapping
  condensate — when observed chirality is VEV-CONDITIONAL ('exactly three
  families of chiral fermions if you have a decreased VEV ... taking a Dirac
  equation into two [Weyl] equations', drafts L158 / ucsd 00:46:02) and the
  selector is SG4 bit 2, OPEN by design."* Carried with SC-CHI-01's own
  declaration: *"a non-chiral total theory splits at the emergent level into
  two separate chiral theories"* (register:913-915), hedged in the same
  passage on no VEV *"pulling the various sub-fields of varpi to values
  significantly above zero"* (register:922). The declared total is NON-CHIRAL;
  the split is L4-conditional (LA3, grant G6); SG4 bit 2 stays OPEN.
- **CC-05-SUBTRACTIVE-TWO-PLUS-ONE** (canonical_since 2026-08-14), quoted:
  *"That three generations is an ADDITIVE target count a mechanism must
  produce — when the source says it is 'really two plus one' with the third
  family an imposter 'for representation theoretic reasons' (drafts
  L119/L128/L131) and HE-1 makes the partition FORCED and SUBTRACTIVE
  (n_g -> n_g - 1, unlabelled, the distinguished family REMOVED)."* Applied
  as a fence at §6; no statement here treats three as an additive production
  target.
- **CC-08-DARK-PARTNER-OBLIGATION** (canonical_since 2026-08-15), quoted:
  *"That the 128 remainder is an established DEFECT of the construction —
  when the source NAMES dark sectors ... and the remainder is a
  partner-placement / decoupling OBLIGATION, not an established defect."*
  No defect framing of the mirror half appears here; the dark half enters
  only through the consumed R3 typing (packet:259).
- **CC-10-UCSD-EDITED-DERIVATIVE** (canonical_since 2026-08-15), quoted:
  *"That the repository's UCSD 2025-04 transcript copy is a PRIMARY SOURCE —
  when it is an EDITED DERIVATIVE whose chain sentence at [00:45:00] had to
  be restored on 2026-08-15 and whose audio confirmation is still owed."*
  Every UCSD-lineage quote here (drafts:146/:149/:158 and the ucsd:244 twin)
  is treated as transcript-verified edited-derivative material, nothing more.

---

## 1. (a) The crossing, typed: what object flips for the VEV-orientation wall

**What the hosted-mode theorem consumes.** The Jackiw-Rebbi machinery (the
rung-2/RW-1 instrument class) consumes ONE field-theoretic input: a mass
profile m(y) whose sign flips across an interface, with hosted count =
|winding| exactly (RW-1 §4c, exact, six profiles). For the VEV-orientation
wall the mass chain is chain 2: m_2(y) = y_Yuk · phi(y) — the rung-2 probe's
own consumption, `A = D + np.diag(y * phi)` (rung-2 probe:168), with phi the
order parameter.

**The object that flips.** phi is the order-parameter section — in the
comparator, a real scalar over the base interval (trivial real line bundle
over rung-2's grid `[-L, L]`, prereg:53); in the source's vocabulary, the
candidate object is the VEV direction of *"the various sub-fields of varpi"*
(register:922), one of the registered senses (i)/(iii) of "the VEV"
(packet:70), NOT silently identified with each other or with the repo weight
pair (iv). What flips is **the vacuum-component label of phi: which
connected component of the vacuum set V = {phi : V(phi) = min} the field
occupies, locally.** The orientation class lives in **pi_0(V)** — in the
toy, V = {-v, +v} and pi_0(V) is a Z/2-torsor; natively, pi_0 of the varpi
vacuum set is UNCOMPUTED (§3, §5).

**What "sign-crossing zero" becomes in this variable.** A transversal zero
of phi at which the pi_0-label jumps — a point where the section exits the
vacuum set to interpolate between components. In the toy the winding is
exactly the rung-2 probe's own formula,
`winding = int(np.sign(phi[-1]) - np.sign(phi[0])) // 2` (rung-2 probe:173)
— and that formula consumes ONLY the endpoints (measured, §4c: scrambling
every interior value leaves it unchanged). **The crossing datum and the
sector datum are the same object.** The crossing count's parity is forced by
the sector: for any profile with ends in different components the number of
transversal zeros is ODD, and with ends in the same component EVEN —
verified exhaustively over all sign sequences to length 12 (§4c). The Z/2
sector class IS the winding mod 2.

**Distinguished cleanly from R's sign.** sgn R and sgn phi live in different
spaces and index different interfaces:

| | sgn R | sgn phi (toy rendering of the pi_0-label) |
|---|---|---|
| what it dials | PHASE at y: whether the Mexican hat exists at all (*"So if your curvature is negative, now you start to get a Mexican hat potential"*, drafts:149; SC-GEO-58 register:2336) | CHOICE OF VACUUM within the broken phase: which well of the existing hat |
| its interface | {R = 0}: the broken-to-unbroken phase boundary — chain 2's one-sided, gapless-end profile, hosts EXACTLY 0 (RW-1 §4c row 6) | {phi = 0} inside {R < 0}: the vacuum-component interface — the tanh row, hosts |winding| per supplied flavor (RW-1 §4c rows 1-2; W3 grading caveat inherited untouched) |
| does the source cross it? | never — CROSSING and POSITIVE families certified ZERO over the eight primary surfaces (RW-1 LEG 2) | never — VEV-FLIP and VEV-NEGATIVE families certified ZERO over the same eight surfaces (this artifact, §4e); the source's VEV language is exclusively one-sided magnitude (*"significantly above zero"*, extraction:138; *"a decreased VEV"*, drafts:158) |
| does the wall need it crossed? | **NO.** The VEV-orientation wall lives entirely in the interior of {R < 0}; R stays one-signed on both sides (measured, §4b: hosting 1 under R = -4(2+tanh y) < 0 everywhere) | **YES.** This is where W1's crossing requirement actually lives |

The re-aim's virtue, now exact: the source names ONLY the negative side of
R (drafts:149, its one sign passage), and only the negative side is needed —
the one-sidedness that killed the R-constituted wall (RW-1) is exactly
sufficient for the VEV-orientation wall's R-role (region + envelope +
steering). The crossing burden has moved wholly onto phi.

---

## 2. (b) Rung-2's result, typed: three different theorems, and which one was proved

The three theorems the phrase "existence condition proved" could name:

- **T-DEG (choice-degeneracy / unselectability).** Both orientations are
  exactly degenerate and no declared invariant or exact symmetry can prefer
  one; the choice is unmakeable from inside. A statement about the ACTION.
- **T-REAL (flip realization).** Somewhere in the actual broken region both
  vacuum components are inhabited with an interface between them. A
  statement about the STATE (dynamics/initial data).
- **T-OBST (global orientation obstruction).** The orientation choice, as a
  Z/2 bundle class over the base, is nontrivial (w_1-type), so NO global
  single-component section exists and a flip is forced by topology. A
  statement about the BUNDLE.

**Rung-2 proved T-DEG, at standard-field comparator grade — and its own
wording says so.** The pre-registered prediction: *"orientation is expected
unselected because `phi -> -phi` is an exact symmetry of the potential, so
kink and antikink are exactly degenerate"* (prereg:63-64). The probe's
verdict text: *"The orientation is a Z/2 the action provably cannot fix"*
(rung-2 probe:272-273) — "cannot fix" = cannot select = T-DEG. The probe's
computed objects are all T-DEG objects: E[kink] = E[antikink] to measured
degeneracy, the `selectable(...)` instrument returning False under the exact
symmetry `phi -> -phi` with all declared invariants equal. Re-run live for
this artifact: exit 0, `VERDICT: SECTOR-SUPPLIED`, *"derived winding +1,
supplied multiplicity 3 -> accessible rank 3"* (§4f).

**T-REAL was not proved — it was INPUT.** In the one run where a flip
exists, the flip was a frozen declared input: *"boundary sector
`phi(-L) = -v`, `phi(+L) = +v`"* (prereg:51-52), enforced every iteration by
endpoint pinning, `phi[0], phi[-1] = -sign * V, sign * V` (rung-2
probe:138), seeded sector-respecting (probe:137). The derivation produced
the PROFILE given the sector; the sector produced the flip. The probe's own
summary: *"a dynamical source at this rung determines the PROFILE but not
the sector, the location, or the orientation"* (probe:271-272). RW-1's P7
already carried the honest parenthesis: *"(What is NOT proved: that domains
of both orientations are realized; that is a dynamics/initial-data question,
open.)"* (rw1:430-432).

**T-OBST was not proved and is not even formulable on rung-2's base.** The
rung-2 base is an interval with pinned endpoints — it carries no
non-contractible loop and no bundle class; the sector is put in by hand at
the boundary. The T-OBST theorem-SHAPE does exist in-repo, for a DIFFERENT
bundle in a different lane: *"`w_1(L_time) = 1 != 0`. This non-orientability
-- you cannot consistently orient"* (shard-cycle:125) — the shard-cycle
`L_time` over the shard cycle, not the VEV-orientation bundle over any
region of Y. Nothing computes a w_1-type class for the vacuum bundle this
wall needs.

**Is the prereg's wording ambiguous between the readings?** No. The prereg
and probe are unambiguous T-DEG (quotes above). RW-1's P7 is T-DEG correctly
glossed, with T-REAL explicitly excluded in the parenthesis. The one surface
a downstream reader could misread is RW-1's compressed join-disposition
string — *"existence condition = the unfixable orientation Z/2 (P7)"*
(rw1:458) — which drops the parenthesis; read alone, "existence condition"
invites the T-REAL reading. This artifact types the compression, per the
relay-frame discipline: **"existence condition" is correct only in the
NECESSARY-condition sense (the permission: exact degeneracy makes both
domains available and walls energetically unforbidden, GIVEN a disconnected
vacuum set), never the SUFFICIENT sense (nothing realizes the flip).**

**The sharpest fact, and it is rung-2's own verdict token: what rung-2
proved about the relocated W1 item is that it is EXTERNAL.** Since the
crossing datum and the sector datum are the same object (§1), and rung-2's
headline verdict is `SECTOR-SUPPLIED` — the sector is an input the action
provably cannot select (T-DEG applied to the sector choice itself, probe
[Q-ORIENTATION] + the guard) — rung-2 does not leave W1 merely open for the
VEV-orientation wall: **it proves, at toy grade, that the action cannot pay
W1, and types the payment as an external supply.** That is a relocation with
a typed holder, not a discharge and not a bare unknown.

---

## 3. (c) The R-steering seam: what R must do, what R may do, what R can never do

**For the wall to EXIST (three stacked requirements, typed):**

- **E1 — a broken region with nonempty interior.** The potential must be
  symmetry-breaking somewhere: source-supplied as the negative side —
  *"So if your curvature is negative, now you start to get a Mexican hat
  potential"* (drafts:149; SC-GEO-58, register:2329/:2336, DISAVOWS row: no
  fundamental Higgs, the hat is curvature-produced) — with the epoch
  dynamics of the dial supplied by SC-CHI-52 (*"The scalar curvature drops
  and the masses drop. If the mass drops sufficiently, then a Dirac type
  operator decouples into Weyl type operators"*, register:1611-1613) and the
  two-way reconnection by SC-CHI-53 (register:1638-1641). R's role in E1 is
  a REGION role; no R-crossing is required — {R < 0} needs an interior, not
  a boundary through zero in the region under study (§4b).
- **E2 — a disconnected vacuum set: pi_0(V) != 0.** The orientation Z/2
  exists as an object only if the broken-phase vacuum set has at least two
  components. NOT source-stated. In the toy it holds by INPUT (the
  double-well over a one-component real phi, prereg:51 — a frozen declared
  input, not a derivation). Natively it is UNCOMPUTED, and the repo's two
  proxies pull opposite ways: (i) rung-2's {-v, +v} (disconnected, but
  input-shaped, one real component); (ii) VG-V5's candidate breaking coset
  for the [00:46:40] decreased-VEV datum, MEASURED connected — *"every orbit
  is open, D is connected (it retracts, below)"* (VG-V5:75) — under VG-V5's
  own two fences (*"the identification of the [00:46:40] VEV's"* vacuum
  manifold *"with D is unproven"*, VG-V5:239-240; "positive lines" a flagged
  modeling choice). The source's own plural — *"the various sub-fields of
  varpi"* (register:922) — points at a multi-component order parameter, for
  which an unstructured Mexican hat has a CONNECTED vacuum sphere/orbit and
  hosts NO Z/2 walls; a Z/2 survives only if the native potential's residual
  discrete symmetry leaves pi_0 nontrivial. **E2 is the gate.**
- **E3 — the sector realized: both components inhabited with an interface.**
  The relocated W1 item proper. External-class by rung-2's own verdict
  (§2); the action cannot pay it (T-DEG, exact at comparator grade); the
  source never asserts it (the certified VEV-FLIP absence, §4e).

**For the wall to be merely STEERED (R's licensed roles, all even-in-phi):**
R modulates the potential's coefficients over the base — depth, vacuum
modulus v(R(y)), envelope (RW-1's P2/P3). Measured here (§4d): an even
modulation lambda(y) selects wall LOCATION (energy spread across shifted
walls > 0) while preserving orientation degeneracy EXACTLY (E[-phi] =
E[phi] bitwise). So rung-2's N2 CONCLUSION — *"linear-gradient term makes
location selectable"* (prereg:95) — transfers to the source-native even
channel, with one seam typed that neither rung-2 nor RW-1 had stated: **the
N2/N1 instrument term `grad * x * phi` is ODD in phi** (it breaks
orientation symmetry along with translation — the probe's own comment
concedes the translation half: *"This same term also breaks translation
invariance; noted, not hidden"*, rung-2 probe:222), while the source-native
R-coupling is EVEN. The instrument selects location by a mechanism the
carrier does not have; the carrier selects location anyway (through
tension/depth variation, §4d); the conclusions agree, the mechanisms do not,
and only the even one is source-licensed.

**What R can NEVER do (exact): pay E3.** The source's stated coupling
structure enters the potential even in phi — *"They both have a Klein Gordon
kinetic term. They both have a quartic term. ... So when you take its norm
square, you get a quartic"* (drafts:146); *"you also get a term that looks
like the unperturbed curvature, interproducted with a wedge a, which is a
quadratic"* (drafts:149) — quartic + R-set quadratic, no phi-odd term
stated. The exact identity (§4a): for I = phi'^2/2 + lambda(y)(phi^2 -
v(y)^2)^2 + g(y)·phi, I(-phi) - I(phi) = -2 g(y) phi. With g = 0 — every
R-steering through the stated coupling, ARBITRARY profiles lambda(y), v(y),
including any R that crosses zero — phi -> -phi remains an exact symmetry,
kink and antikink remain exactly degenerate, and no R profile forces or
prefers a flip. **The only phi-odd mass datum the source states is chain
1's m = R/4 (register:940), and consuming it reimports the R-crossing
burden RW-1 certified absent (rw1 LEG 2). The two chains exchange the W1
burden and neither pays it:** chain 1 puts it on R's sign (unasserted —
certified absence); chain 2 puts it on the sector datum (external — the
action provably cannot).

**What NEW datum would make the flip FORCED rather than allowed** (if the
source or a construction supplied it):

1. **pi_0(V) != 0 for the native varpi vacuum set** (E2's gate) — the
   possibility precondition. Uncomputed; the deciding computation is named
   in §5. Without it there is no Z/2 to flip.
2. **A realization mechanism**, any one of:
   - *Initial-data/quench (Kibble-class).* The source supplies a
     quench-SHAPED narrative (SC-CHI-52/53 epochs) but no fluctuation or
     causal-patch datum; the argument form exists in-repo at perspective
     grade with INVERTED polarity on a DIFFERENT Z/2 — *"a large network
     freezes into **domains** of `+` and `−` separated by walls
     (Kibble–Zurek)"* (KZ steelman:105-106, where domains were the FALSIFIER
     for a universal Krein sign). Any use here is a comparator import and
     stays fenced.
   - *Topological forcing (T-OBST).* A nontrivial Z/2 class of the vacuum
     bundle over a base with non-contractible loops — the shard-cycle
     precedent shape (shard:125) computed for THIS bundle. Unformulated for
     the VEV-orientation object; rung-2's interval base cannot carry it.
   - *A phi-odd coupling.* None source-stated (this artifact's certified
     absence + the quartic/quadratic structure above); asserting one would
     be new source data, and note it would cut BOTH ways — a phi-odd term
     with one sign globally LIFTS the degeneracy and destabilizes walls
     rather than forcing them (biased-wall collapse), so "odd term" is not
     a free rescue.
3. **Failing all of 2: the sector datum stays an external supply** — which
   is not a defect of the route but its convergence with canon (§5).

---

## 4. The measured legs — TYPED AS COMPARATOR, fenced

**Routing fence, repeated at the point of use.** Everything in this section
is computed on the rung-2 standard-field wall system (double-well energy
functional; 1D Dirac hosting judge D = sigma_1 p + sigma_3 m(y) on
C^2 (x) L^2(R), the same continuum fiber RW-1 §4 used) or is a text scan
over the eight Weinstein primary surfaces. The functional results bind the
model; the scans bind the surfaces; nothing here is a statement about the
true RS Y^14 bundle or the (9,5) carrier (prereg:43-45's transport fence
inherited unchanged). "Winding", "sector", "vacuum set" are repository/
comparator vocabulary; the source's own words are "curvature", "VEV",
"decreased", "Mexican hat".

**(a) The evenness identity (sympy, exact; arbitrary steering profiles).**
With lambda(y), v(y), g(y) arbitrary function symbols:

    I(phi, phi', y) = phi'^2/2 + lambda(y) (phi^2 - v(y)^2)^2 + g(y) phi
    I(-phi, -phi', y) - I(phi, phi', y) = -2 g(y) phi   (exact)

- g = 0 (the source-stated coupling class: quartic + R-set quadratic):
  the difference is IDENTICALLY ZERO — phi -> -phi is an exact symmetry for
  EVERY steering profile, so orientation degeneracy is not a constant-
  coefficient accident of rung-2 but a structural property of even
  R-steering. No R(y), including sign-crossing R(y), can prefer an
  orientation through this channel.
- g != 0 (the rung-2 N1/N2 instrument term g·y·phi): the difference is
  -2 g y phi != 0 — the instrument's selector is phi-odd. The probe's
  planted control requires the odd term to be FLAGGED (a stuck-at-even
  checker is a selftest mutation and must be caught).

**(b) Composite hosting inside a one-signed R region (sympy, exact).** Take
R(y) = -4 (2 + tanh y): R <= -4 < 0 for all y (with t = tanh y in (-1,1),
2 + t >= 1, so R = -4(2+t) <= -4; exact arithmetic, verified at the
endpoints of t). On this SAME region:

| chain | mass profile | winding | hosted modes | note |
|---|---|---|---|---|
| chain 2 (VEV-orientation kink inside broken region) | m_2 = tanh y (phi-kink, y_Yuk = 1) | +1 | **1** (mode sech y, integral of sech^2 = 2, exact) | the crossing is phi's; R never crosses |
| chain 1 (direct m = R/4 on the same region) | m_1 = R/4 = -(2 + tanh y) | 0 (no zero) | **0** (both candidate modes blow up at an end, exact) | one-signed R hosts nothing via chain 1 |

The crossing burden for the VEV-orientation wall lives entirely in phi; R
supplies the region and the envelope and is never required to cross. This
is §1's table row measured.

**(c) The sector-parity identity and the winding functional (exact).**

- For every finite sign sequence with nonzero entries, (number of adjacent
  strict sign alternations) mod 2 = [ends have opposite sign] — verified
  EXHAUSTIVELY over all 2^n sign patterns for every n = 2..12 (8,188
  sequences), plus 200 seeded random-sequence renderings with pinned
  opposite ends (always odd) and an equal-ends control family (always even).
  Sector class nontrivial <=> odd crossing count: **the Z/2 sector datum is
  an ODDNESS datum.** (The continuum statement is the intermediate value
  theorem, classical, not re-proved; the discrete rendering is what the
  instruments consume.)
- The rung-2 winding functional (probe:173) consumes ONLY the endpoints:
  scrambling every interior sample leaves it unchanged (measured);
  flipping one endpoint's sign changes it. The winding rung-2 "derives" is
  the sector class read back — the crossing datum IS the sector datum, as
  an exact property of the instrument itself.

**(d) Even modulation steers location while preserving orientation
(numeric, machine-exact where stated).** On the rung-2 grid ([-12, 12],
N = 241) with even modulation lambda(y) = 1 + 0.3 tanh(y/2) and the kink
family phi_s = tanh(y - s), s in {-2, 0, +2}:

- location: the modulated energies split (spread > 1e-3 measured) — an even
  R-steering channel selects WHERE the wall sits (tension varies over the
  base), transferring rung-2's N2 conclusion without the odd instrument
  term;
- orientation: E_lambda[-phi_s] == E_lambda[phi_s] with difference EXACTLY
  0.0 at machine level for every s (the functional is even in phi, so the
  computation is bit-identical);
- contrast: adding the rung-2 instrument term g·y·phi (g = 0.05) splits
  kink from antikink (asymmetry > 1e-3) — the odd term, and only the odd
  term, touches orientation.

**(e) The VEV-orientation scan (certified absence; the phi-side mirror of
RW-1's R-side LEG 2).** Over the eight Weinstein primary surfaces (the same
scope as RW-1: drafts transcript, TOE 2025, Portal 2020, UCSD 2025,
s11-s12 extraction, s9 extraction, primary-source pack, source-claim
register):

- **VEV-FLIP family** ("changes sign", "flips sign", "crosses zero",
  "either sign", "both signs", "opposite sign", "both orientations",
  "opposite orientation", ... with a VEV co-token — vev / vacuum
  expectation / varpi — within +-2 lines): **ZERO hits.**
- **VEV-NEGATIVE family** ("negative vev", "vev is negative", "vev becomes
  negative", ...): **ZERO hits.**
- **VEV-MAGNITUDE family** ("significantly above zero", "decreased vev"):
  **exactly 5 hits, all the same two utterances across surfaces** —
  drafts:158 / ucsd:244 (the edited-derivative twin) for *"a decreased
  VEV"*, and extraction:138 / register:923 / register:1805 for the p.52
  hedge and its register copies.

**The source's VEV language is exclusively one-sided magnitude.** It states
the VEV pulled *above zero* and *decreased* — never both orientations,
never a sign, never a flip. W1's certified-absence status SURVIVES THE
RELOCATION in the new variable: the source asserts neither the R-crossing
(RW-1's scan) nor the phi-crossing (this scan). Certified with a planted
positive the detector must flag and two planted near-misses it must not
(one with a family token but no VEV co-token in window; one with VEV but no
family token).

**(f) The rung-2 instrument re-run (float-grade, the repo's own
instrument).** `tests/channel-swings/rung2_dynamical_wall_selectability_probe.py`
re-run live: exit 0; `VERDICT: SECTOR-SUPPLIED`; *"The orientation is a Z/2
the action provably cannot fix"* present; *"accessible rank 3"* (supplied
multiplicity) present.

---

## 5. (d) VERDICT on W1 — RELOCATED (typed), with the kill branch stated

**W1 for the VEV-orientation wall: RELOCATED — not discharged, not merely
open.**

- **Relocated FROM:** "R(y) crosses zero with odd winding" — the reading
  RW-1 already measured non-hosting as stated and certified unasserted
  (rw1 §4c, LEG 2). For THIS wall, R need not cross anywhere (§4b).
- **Relocated TO:** **the orientation sector datum** — phi realized in both
  components of a disconnected vacuum set with an interface, inside the
  broken region. Equal to the crossing datum exactly (§1, §4c), it is a Z/2
  topological charge equal to winding mod 2 — an ODDNESS datum.
- **Held by:** the EXTERNAL-DATA family. Twice over: (i) rung-2's own
  verdict token types it so at comparator grade — the sector is
  `SECTOR-SUPPLIED`, the action provably cannot select it (§2); (ii) canon
  requires it so by structure — *"chi = interior-even +
  external-topological-index"* (CANON.md:139), *"any ODD generation count is
  necessarily external"* (external-by-structure-synthesis:60), and the
  computed external exemplar *"net chiral index = flux number (any integer,
  odd for odd flux)"* (CANON.md:135). The sector class is precisely the
  mod-2 part of such an external datum in the 1D model. **The relocation is
  CONVERGENT with canon: W1's burden moving to an external sector datum is
  not a defect of the wall route — it is the wall route arriving at the
  same external-by-structure decomposition canon proved for the count
  itself.** Membership typing of a VEV-sector datum in canon's external
  family (the class-C sense) remains the external-by-structure owner's
  call — this is RW-1's W4 seam, inherited, not duplicated.
- **What rung-2's proved result supplies and does not supply:** it supplies
  the PERMISSION half of existence (exact degeneracy: both domains
  available, walls energetically unforbidden — GIVEN E2's disconnected
  vacuum set, which in rung-2 was an input) and the TYPE of the relocated
  obligation (external, unselectable-from-inside). It does NOT supply the
  crossing itself (T-REAL open; T-OBST unformulated — §2).
- **The stacked gate left OPEN, named:** **pi_0(native varpi vacuum set)**
  is uncomputed, and the repo's proxies disagree — rung-2's disconnected
  {-v, +v} is an INPUT (one real component, declared); VG-V5's candidate
  coset D is MEASURED connected (VG-V5:75), double-fenced by its own
  caveats (VG-V5:239-240). The deciding computation, stated so the
  executing wave can aim at it: construct the broken-phase vacuum set of
  the native varpi potential (the actual sub-field content, SC-CHI-01's
  plural) and compute pi_0 with its residual symmetry action.

**The kill branch (what measured fact would kill the typed target at W1):**

- **KILL-1 (the live one): pi_0(native vacuum set) computed TRIVIAL** —
  a connected vacuum set on the actual carrier leaves no Z/2 sector, no
  stable orientation wall, and the typed target
  `TYPED-TARGET-VEV-ORIENTATION-WALL-R-STEERED` (rw1:525, the JOIN verdict;
  a repository construction target, not a source claim — the source asserts
  no wall, so no register row would die) loses its hosting candidate at W1.
  VG-V5's connected D is a first data point LEANING this way in its model;
  under VG-V5's own two fences it is not a kill today. This is the branch
  the pi_0 computation decides.
- **KILL-2 (the other direction): a strict orientation-selection theorem**
  — a source-asserted or construction-derived phi-odd term making one
  orientation strictly preferred would lift the degeneracy and collapse
  walls (biased-wall decay), killing the target from the opposite side.
  None exists: the certified FLIP/NEGATIVE absences (§4e) and the exact
  evenness of the stated coupling (§4a) are evidence against, and rung-2's
  exact degeneracy is the toy-grade measurement of its absence.
- **Neither fires today.** The crossing is not FORBIDDEN on present
  material — it is unpaid, with the payer typed external and one named gate
  (pi_0) between the target and its existence condition. W1's RW-1 status
  "OPEN, not forbidden" (rw1:267-269) is refined, not contradicted:
  RELOCATED-TYPED-EXTERNAL, pi_0 gate OPEN, kill branch named.

> [!NOTE]
> **STATUS PV1-20260817 — the stacked pi_0 gate closed against the wall.**
> PV-1 (`lab/active-research/joe-directed/wall-bill/pv1-pi0-trivial-in-every-live-typing-w1-kill-fires-2026-08-17.md`)
> computed the gate this verdict left OPEN: pi_0 is trivial in every
> grounded typing of the native varpi vacuum set, the two proxies typed
> different objects (the native object sides with VG-V5's connected coset
> everywhere), and the kill branch this artifact named FIRED. W1's
> RELOCATED verdict stands — the relocation is exactly why the kill lands
> on the sector datum's carrier rather than on any source claim. Revival
> forks: PV1-REVIVAL-FORKS in the upgrade register.

---

## 6. (e) The CC-05 fence on every count statement

Binding here, quoted from the registry (§0): the partition is *"FORCED and
SUBTRACTIVE (n_g -> n_g - 1, unlabelled, the distinguished family
REMOVED)"* — never an additive production target.

- Hosted count on any realized wall = |winding| x N with **N SUPPLIED**,
  never derived (RW-1 §4g exact; rung-2 P2: supplied multiplicity 3 ->
  accessible rank 3, re-run green §4f). Nothing in this artifact derives
  any count.
- The relocated sector datum forces only PARITY: sector class nontrivial
  <=> odd winding (§4c). It makes an odd hosted count possible; it does not
  produce 3, and |winding| = 1 remains the preregistered generic null —
  *"the run has demonstrated hosting, not selection (the Jackiw-Rebbi
  standard"* (prereg:111).
- Even a hosted N = 3 would be an ADDITIVE count, while the source's
  partition is SUBTRACTIVE 2+1 with the removed family UNLABELLED and the
  third-family imposter spin-3/2-native (CC-05). The wall route's ceiling
  is hosting the external odd count; the 2+1 structure remains owned by
  representation content, not by wall degeneracy. This is RW-1's W5 fence,
  re-applied to the relocated item.

---

## 7. Machine-readable verdicts and certificate

<!-- WB1-TABLE-BEGIN -->

| id | question | verdict | evidence_key |
|---|---|---|---|
| CROSS | what object must flip for the VEV-orientation wall | VACUUM-COMPONENT-LABEL-OF-PHI-NOT-SIGN-OF-R | composite_hosting |
| SCAN | does any primary surface assert a VEV flip or negative VEV | VEV-FLIP-ABSENT-MAGNITUDE-ONLY | vev_orientation_scan |
| RUNG2 | which theorem rung-2's orientation result is | DEGENERACY-AND-UNSELECTABILITY-NOT-REALIZATION | rung2_pins_and_rerun |
| STEER | can R-steering through the stated coupling force the flip | EVEN-MODULATION-STEERS-LOCATION-NEVER-ORIENTATION | evenness_and_location |
| W1 | the bill item's disposition | RELOCATED-TO-EXTERNAL-SECTOR-DATUM-PI0-GATE-OPEN | sector_parity_and_canon_pins |
| KILL | did a kill branch fire | NAMED-NOT-FIRED-PI0-NATIVE-UNCOMPUTED | proxy_pins |

<!-- WB1-TABLE-END -->

**Verdict-evidence binding (the probe enforces this; the selftest's contrary
control flips W1 to DISCHARGED-BY-RUNG2 and must be caught).**

| evidence_key | asserted direction | measured |
|---|---|---|
| composite_hosting | CROSS requires: phi-kink hosts 1 under one-signed R < 0 AND chain-1 m = R/4 hosts 0 on the same region | 1 / 0, exact (§4b) |
| vev_orientation_scan | SCAN requires FLIP = 0, NEGATIVE = 0, MAGNITUDE = exactly the 5 pinned one-sided hits | 0 / 0 / 5, certified with planted controls (§4e) |
| rung2_pins_and_rerun | RUNG2 requires the T-DEG wording pins, the sector-input pins (prereg:51-52, probe:138), and the live re-run SECTOR-SUPPLIED | all pinned; exit 0 (§2, §4f) |
| evenness_and_location | STEER requires I(-phi) - I(phi) = -2 g phi exactly; location spread > 0 and orientation difference exactly 0.0 under even modulation | measured (§4a, §4d) |
| sector_parity_and_canon_pins | W1 requires parity identity (exhaustive n <= 12), endpoint-only winding, and the canon external pins (CANON.md:135/:136/:139, synthesis:60) | all measured/pinned (§4c, §5) |
| proxy_pins | KILL requires the two proxy pins (VG-V5:75 connected; prereg:51 double-well input) and both kill branches unfired in present material | pinned; no firing datum exists (§5) |

**Certificate.** `tests/channel-swings/joe_directed_wb1_crossing_is_a_sector_datum_r_cannot_supply.py`

- Live run: all legs green, exit 0 — quote pins with a planted negative;
  the certified VEV-orientation scan (planted positive + two near-misses);
  the exact comparator (evenness identity, composite hosting, exhaustive
  sector parity, endpoint-only winding, even-modulation location/orientation
  split); the rung-2 re-run; the artifact binding with SHA-pinned table.
- `--selftest`: clean baseline verified FIRST with an independently pinned
  check count, and a red baseline aborts; 8 mutations, every one corrupting
  machinery or a reference (a pin's line number, the scan's FLIP family,
  the scan scope, the phi-flip map, the normalizability judge's far-end
  gate, the parity counter, the rung-2 runner path, and a contrary-control
  artifact copy claiming DISCHARGED-BY-RUNG2), each REQUIRED to be caught
  by its targeted check with a genuine [FAIL]; a crash is
  CRASH-NOT-DETECTION; an untargeted catch is INCIDENTAL-NOT-TARGETED;
  the failing check is printed for every mutation; baseline re-verified
  after; exit 0 on success.
- Read-only; planted corpora and the contrary-control copy live in a temp
  directory and are removed. Deterministic; sympy + numpy + stdlib.
- What the probe does NOT certify: anything about the true RS Y^14 bundle
  or the (9,5) carrier; pi_0 of any native vacuum set (the OPEN gate);
  files phrasing a VEV flip outside the scanned token families; the
  Kibble-class argument (perspective-grade prior art only); and the
  stylized Mexican-hat fences (§4 routing paragraph).

---

## 8. Typed objects (typed-carrier gate)

```gu-typed-objects
result:         Exact comparator on the rung-2 wall system: the energy
                integrand obeys I(-phi) - I(phi) = -2 g(y) phi for arbitrary
                lambda(y), v(y), g(y), so every even (source-stated)
                R-steering preserves phi -> -phi exactly and cannot prefer
                an orientation; a phi-kink hosts exactly 1 mode under
                one-signed R = -4(2+tanh y) < 0 while chain-1's m = R/4
                hosts exactly 0 on the same region; crossing-count parity =
                sector class (exhaustive to length 12); the rung-2 winding
                functional depends on endpoints only; even modulation
                selects location with orientation difference exactly zero
carrier:        real scalar profiles phi over the rung-2 base interval with
                energy E[phi] = int phi'^2/2 + lambda(y)(phi^2 - v(y)^2)^2
                + g(y) phi dy, plus the 1D hosting judge D = sigma_1 p +
                sigma_3 m(y) on C^2 (x) L^2(R) with m = y_Yuk phi (chain 2)
                or m = R/4 (chain 1)
                LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing:        L^2 norm on profiles and on C^2 (x) L^2(R) for the
                normalizability judge; no Krein form is used in this
                artifact's own legs (the class-membership algebra is RW-1
                section 4a, consumed, not recomputed) ON=C^2 (x) L^2(R)
real_structure: real scalar order parameter; complex Hermitian symbolic on
                the hosting judge; explicitly NOT the (9,5) real-form fork
                (prereg:43-45 transport fence inherited)
grading:        Gamma = sigma_3 on the hosting judge (the model's declared
                elliptic grading). HOMONYM-AMBIGUOUS against the wall
                grading sigma_2, the ambient-half grading, and observed 4d
                Weyl chirality — the four-way homonym (packet:69); the
                bridge is RW-1's W3 and is UNTYPED here by inheritance
action_owner:   repository-construction (the functional, judge, scans and
                parity identity are WB-1's; the potential-shape ingredient
                is source-print SC-GEO-58 drafts:146/:149, and the sector
                input is rung-2's declared prereg:51-52)
target:         what the W1 crossing requirement IS for the VEV-orientation
                wall and which structure can supply it
                MAP-TYPE=not-a-map (a typing/adjudication of a bill item on
                a class, not a map between carriers)
```

```gu-typed-objects
result:         Source adjudication: over the eight Weinstein primary
                surfaces the VEV-FLIP and VEV-NEGATIVE token families score
                ZERO with co-token discipline, and the VEV-MAGNITUDE family
                scores exactly 5 — the same two one-sided utterances
                ('significantly above zero' p.52; 'a decreased VEV' spoken)
                across surfaces; the source's VEV language is exclusively
                one-sided magnitude and never asserts both orientations,
                a sign, or a flip
carrier:        the register verbatim/notes fields and the primary-surface
                lines as literal text (byte-pinned at cited lines)
                LAYER=source-print CHIRALITY=N/A
pairing:        NONE
# A text parse: no bilinear form is involved in this result and none is
# claimed.  Bare token per the FX-2 gate's parser; gloss lives on these
# comment lines (RW-1's relay: an indented continuation line would be
# read as part of the value).
real_structure: N/A
grading:        N/A — the parsed lines contain the source's own words
                ("VEV", "decreased", "above zero"); their operator-level
                grading sense is the four-way homonym, not resolved here
action_owner:   repository-construction (the scan families and co-token
                discipline are WB-1's; the parsed content is source-print)
target:         whether any primary surface asserts the VEV taking both
                orientations or crossing zero — the phi-side mirror of
                RW-1's R-side crossing scan
                MAP-TYPE=not-a-map (an adjudication of stated commitments,
                not a map)
```

---

## 9. Grep-before-novelty record (exact-substring searches, run before any first/never claim)

Searches run over the repository (md/py, `_local/` excluded), with the
material hits and what each did to this artifact:

- `"flip realization"` — HITS: construction-prong1/three-seam prongA files
  (the shard-cycle sigma flip/no-flip handle). Different object (shard-cycle
  closure orientation, not the VEV orientation); the three-theorem typology
  of §2 is applied HERE to rung-2's result for the first time, but the
  flip-vs-no-flip vocabulary is not new in-repo.
- `"sector datum"` — HITS: adapter-assumed-four-leg-swing-2026-07-19.md:29-36
  (*"one external Z/2 posit, home p2c ... a Z2 sector datum can live
  topologically ... a topological sector datum, not a local field"*),
  blockbuster-p5, CH-REC. The "external Z/2 sector datum" TYPE is
  established repo vocabulary — for the KREIN-half choice. This artifact's
  claim is therefore not "GU needs a Z/2 sector datum" (prior art) but the
  specific relocation: W1's crossing = the VEV-orientation sector datum,
  with rung-2's SECTOR-SUPPLIED as its typing proof.
- `"non-orientability"` / `"w_1"` — HITS: shard-cycle-prong1-geometry:125
  (`w_1(L_time) = 1 != 0`). The T-OBST theorem-shape exists in-repo for
  L_time over the shard cycle; NOT for the VEV-orientation bundle. Cited in
  §2/§3 as the named precedent shape.
- `"Kibble"` — HITS: ten-perspective-steelman-live-dark-observer-sheaf:104-107
  (Kibble-Zurek domains as the FALSIFIER for a universal Krein sign) plus
  Einstein-Cartan citations. The quench argument exists at perspective
  grade, different Z/2, inverted polarity. Cited in §3; not imported.
- `"vacuum manifold"` — HITS: VG-V5 (D connected, measured, double-fenced),
  path3-branchB (winding = degree to vacuum manifold), VG-V7. VG-V5 is the
  anti-Z/2 proxy consumed in §3/§5.
- `"SECTOR-SUPPLIED"` — consumers: only the prereg and RW-1 (and their
  probes). Its use as the TYPING of the relocated W1 item is new here.
- `"VEV-orientation"` / `"orientation wall"` outside the rwall lane — zero
  hits. `"crossing requirement"` — zero hits. Zero hits recorded as zero
  hits, not as proof of novelty.

---

## 10. Canonical-currency check records (for the integrator; WB-1 edits no sidecar)

`process_gates/canonical_currency_audit.py` run 2026-08-17 (183 dirty
pairs repo-wide, 18 cleared by recorded checks). **Finding: NONE of WB-1's
consumed inputs appears in the CURRENT dirty queues.** Several predate every
canonical correction and are exactly the class the queue exists for; the
audit's own registry documents per-entry signature blindness ("zero exact
hits is not evidence of clean"), so a per-input verdict is recorded here for
every pre-dating consumed input regardless of queue membership. Sidecar
untouched by WB-1.

1. `explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md`
   + `tests/channel-swings/rung2_dynamical_wall_selectability_probe.py`
   (2026-07-29; predate all ten corrections; in NO current dirty queue —
   CC-05's conjunction signature does not fire on them).
   - vs CC-05 (subtractive 2+1): the prereg's own posture is anti-additive
     by construction — *"The triplet is **supplied**, inherited from Rung 1,
     and no result here derives three"* (prereg:46-47), and the
     preregistered null types hosting-not-selection (prereg:109-113).
     **CLEARED-CONSISTENT** (pointer: prereg:46-47, :109-113; this artifact
     §6).
   - vs CC-06 (chirality VEV-conditional): the prereg forecloses no
     mechanism; its wall matrix is "the chirality grading" at declared toy
     grade with the (9,5) transport fenced (prereg:43-45).
     **CLEARED-CONSISTENT**.
   - NOTE for the integrator: the prereg's `implements:` parent,
     `lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md`,
     IS in CC-06's current dirty queue. WB-1 does not consume the parent;
     no verdict recorded for it here.
2. `explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md`
   (2026-07-10; predates all; in NO current dirty queue — invisible to
   CC-05's signature despite carrying "generation-count" vocabulary, the
   entry's own documented escape surface).
   - vs CC-05: consumed content (the terminus identification :25-34, the
     scope-exit :88-92) treats the count as external hosting — *"Not a
     derivation of three (or any) generations"* (:107) — no additive
     production framing. **CLEARED-CONSISTENT** (pointer: nn:107, :90).
   - vs CC-06: the NN lane's chirality is the lattice/edge-mode sense with
     its own scope-exit (*"it rides SG4, exactly as the carrier bit does"*,
     nn:90); no foreclosure of the source's VEV mechanism.
     **CLEARED-CONSISTENT**.
3. `explorations/decoupling-constructibility-packet-2026-08-12.md`
   (predates CC-05/06/08/10; formerly dirty under CC-05 and CC-08, now
   CLEARED in the sidecar by RW-1's recorded checks,
   `lab/process/canonical-currency-checks.yaml:412` and `:423`).
   - WB-1 re-checked its own consumed rows independently: the homonym rows
     (:69, :70) and R3's dark-typing (:259) contain no additive-count
     framing and treat the mirror half as a placement obligation.
     **CLEARED-CONSISTENT**, concurring with RW-1's recorded verdicts
     (pointers: packet:69-70, :259; sidecar :412, :423).
4. `canon/external-by-structure-synthesis-RESULTS.md` (2026-07-02; predates
   all ten; in NO current dirty queue).
   - vs CC-05: its count posture is the origin of the fence — *"Does NOT
     derive three. `chi_external` is the flux / instanton number, ANY
     integer; nothing here privileges 3"* — external datum, no additive
     production. **CLEARED-CONSISTENT** (pointer: synthesis "What this does
     and does not do" bullet 2; :60).
5. `explorations/big-swing-2026-07-06/VG-V5-breaking-coset-topology.md`
   (2026-07-06; predates all; in NO current dirty queue). Consumed content:
   the connectedness measurement (:75) and the two honest-gap fences
   (:239-243) ONLY.
   - vs CC-05: the consumed rows are a topology measurement and its fences;
     the file's broader 3-divisibility program is NOT consumed here and its
     own guard (*"{3, ...} never assumed, inserted, or divided by"*, grade
     block) plus honest gap (3) (*"the channel provably cannot produce an
     odd count"*) keep it off the additive reading. **CLEARED-CONSISTENT
     for the consumed content**; flagged for the integrator that VG-V5's
     count-adjacent framing predates CC-05 and has never been queue-checked
     (signature blindness).
6. `explorations/time-as-finality-crosswalk/ten-perspective-steelman-live-dark-observer-sheaf-2026-07-15.md`
   (:104-107 consumed), `explorations/adapter-assumed-four-leg-swing-2026-07-19.md`
   (:29-36 consumed), `explorations/shard-cycle-prong1-geometry-2026-07-21.md`
   (:125 consumed) — all predate all ten; none in a current queue; consumed
   as prior-art pins only (a falsifier argument, a vocabulary precedent, a
   theorem-shape precedent). Checked against CC-05/CC-06 on the consumed
   lines: no count production, no mechanism foreclosure.
   **CLEARED-CONSISTENT (scoped to consumed lines)** for each.
7. UCSD-lineage quotes (drafts:146/:149/:158; ucsd:244 scan hit) — vs
   **CC-10**: every use carries the edited-derivative caveat; the ucsd twin
   is cited AS the derivative copy of the drafts utterance; audio
   confirmation remains owed. **CLEARED-CONSISTENT** (pointer: §0 frame
   block; CC-10 owner banner).
8. Post-correction or owner inputs, checked current by inspection at read
   time: `rw1-...-2026-08-17.md` + probe (2026-08-17, postdates all;
   carries the fences it inherits), `lab/methods/gu-base-categories.md`
   (2026-08-17), `lab/sources/source-claim-register.yaml` (CC-06 co-owner),
   `lab/process/correction-registry.yaml` (the registry itself), `CANON.md`,
   `VERIFICATION.md`. No verdicts owed.

---

## 11. Claim ceiling, and what this artifact is not

- **No claim status moves. No canon row moves. No register, ledger, sidecar
  or registry edit.** The generation count stays OPEN; SG4 stays the
  decider; SG4 bit 2 stays OPEN; the wall route RIDES it (nn:90 unchanged).
- **This artifact does not derive 3, and does not derive 1.** Hosted count
  stays |winding| x N with N SUPPLIED; |winding| = 1 stays the
  preregistered null; the sector datum contributes PARITY only (§6).
- **The comparator binds the model.** Every §4 identity is exact IN THE
  MODEL; the (9,5)/ker-Gamma transport is rung-2's declared gap, inherited
  (prereg:43-45). RW-1's W3 (grading bridge) and W4 (external-family
  membership) are inherited seams, not re-adjudicated.
- **RELOCATED is not DISCHARGED.** Naming the relocated item's holder
  creates no presumption the datum exists; E2 (pi_0 gate) and E3
  (realization) are both open, and KILL-1 is live for the executing wave.
- **Relation to RW-1.** This artifact executes W1 of RW-1's bill, refines
  its "OPEN, not forbidden" status to RELOCATED-TYPED-EXTERNAL with a named
  gate, types the compression risk in RW-1's join-disposition wording
  (§2), and corrects nothing in RW-1's verdicts. W3 remains, with W1's
  residue, an item on which the target can still die.

---

## 12. POSTFLIGHT — six lenses, after the work

- **P1 — Did any lens change a verdict?** Yes, two. L4 (coverage
  archaeologist) surfaced VG-V5's connected D, which converted the
  existence condition from "proved by rung-2" (the naive reading) to a
  two-proxy DISAGREEMENT gated on an uncomputed pi_0 — the artifact's
  stacked-gate structure exists because of that hit. L3 (symmetry auditor)
  found the N2 instrument term is phi-odd, which split "R steers location"
  (survives, via the even channel, measured) from "R could pick
  orientation" (provably cannot, exact) — without it the steering seam
  would have transferred the instrument's power wholesale.
- **P2 — Is any verdict resting on a single receipt?** The KILL-1 lean
  rests on VG-V5's one measurement, and is treated as a lean, not a
  verdict, under VG-V5's own two fences (identification unproven; modeling
  choice). The RUNG2 verdict rests on multiple independent pins (prereg
  wording, probe wording, the frozen-input lines, the live re-run). The
  SCAN verdict is scan-grade over eight surfaces with planted controls.
- **P3 — What did NOT move?** SG4; the generation count; RW-1's six
  verdicts and six-item bill (W1's row refined in disposition, not in
  content); the NN scope-exit; rung-2's null and its (9,5) fence; the
  register; canon.
- **P4 — Where would a hostile re-runner disagree?** (i) The scan families
  are finite; a VEV-flip assertion phrased outside them ("the condensate
  points the other way in dark regions") would escape — declared in §7's
  does-not-certify list. (ii) The evenness argument binds the STATED
  coupling class; a construction could add phi-odd terms from the fermion
  determinant (Yukawa back-reaction) — that is comparator QFT beyond this
  artifact's scope and is named here rather than hidden. (iii) Discrete
  parity on sampled profiles is exact combinatorics; a reader wanting the
  continuum IVT statement gets it as classical math, not re-proved.
- **P5 — Regression check against the standing corrected facts.** Layer
  discipline: every source locus carries its layer (§1, §3); the toy is
  never credited to L1 (base-categories §1.4's unforgivable regression
  avoided — the R(y) equation stays a stylized LA3 attachment). No KK
  language. No GUT chain. Positivity untouched. CC-05 applied at §6;
  CC-08 posture kept (dark = obligation); CC-10 caveat carried on every
  UCSD-lineage quote. Chirality's four senses never silently identified
  (L6 held; W3 inherited UNTYPED).
- **P6 — Instrument honesty.** The scan's planted positive and two
  near-misses behaved on the live run; the parity identity was verified
  exhaustively (8,190 sequences), not sampled; the selftest's 8 machinery
  mutations were each caught by their targeted checks with the clean
  baseline verified first and re-verified after; the rung-2 re-run is the
  unmodified repo instrument.

---

## The blunt paragraph: which direction the pressure ran

The brief handed this arc a target that wanted to be discharged: rung-2's
"unfixable orientation Z/2" was sitting one paraphrase away from "the
existence condition is proved, W1 is paid," and RW-1's own compressed
join-disposition wording leans that way if you drop its parenthesis. The
pressure ran toward reading T-DEG as T-REAL and closing the bill's
load-bearing item, and the byte-level record pushed back at every step: the
flip in the only realized run was a frozen INPUT (prereg:51-52, probe:138),
the verdict token on the run's own face types the sector as SUPPLIED, the
source's VEV language is measurably one-sided in the new variable exactly
as its curvature language was in the old one (0/0/5, certified), and the
one steering channel the source actually states is even in phi and so
provably cannot pay the item under any R profile whatsoever. What survived
is, I judge, stronger than the discharge would have been: W1 relocates to
an external Z/2 sector datum — the same external-by-structure shape canon
already proved the odd count must have — with rung-2 supplying the TYPE of
the obligation rather than its payment, and with one honest gate (pi_0 of
the native vacuum set, where the repo's two proxies currently disagree)
standing between the typed target and its existence condition. I flag
plainly what I could not settle: whether the native varpi vacuum set is
even disconnected is uncomputed, VG-V5's connected candidate leans against
it inside its own fences, and if that computation lands connected, KILL-1
fires and the VEV-orientation wall dies at W1 — a first-class result of the
same rank as this relocation.
