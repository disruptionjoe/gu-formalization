---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-17
work_item: GB-1
channel: grading-bridge
wave: reverse-scaffold wave 2 (grading-bridge W3 arc)
title: "GB-1: the W3 grading bridge, built to one exact angle and one missing arrow. The four chirality gradings are enumerated as typed objects and the wall circle is computed in closed form on RW-1's own comparator class: for a zero-order wall at fiber angle phi (measured from the source-shaped sigma_3 direction toward sigma_2), the hosted mode's ambient Gamma-charge is EXACTLY -sin(phi), the wall's Gamma-oddness residual is 2|cos(phi)|, and the Krein exit is UNIFORM (commutator norm 2 at every angle) — so FULL canon-graded charge holds IF AND ONLY IF the exit is Krein-only, the hosted mode is K-null at every angle with K cross-pairing it to its anti-normalizable mirror (the model face of LD-B's odd-q parity), and the grading-rotating unitary is a KREIN ISOMETRY that rotates mass direction and grading together, making the relative angle an invariant: no unitary transport can give the source-shaped operator a canon-graded hosted charge. W3 therefore reduces to ONE missing arrow — a source-native supply of the sigma_2-type (Gamma-odd, Krein-breaking) mass direction — and hands off to W6 at the LA1 contraction, unabsorbed."
grade: "EXACT where computed: every comparator statement is closed-form sympy on the continuum fiber of tests/function-space-ext/dirac_spectral_flow_section.py (RW-1 section 4's class) — generic-m(y) zero modes verified symbolically at generic angle phi, charges -sin(phi)/+sin(phi)/0 exact, the residual identities and the Pythagoras identity exact, the unitary-circle statements exact including a symbolic commutant computation, the commuting-K contrast exact. CERTIFIED where pinned: 43 byte pins at cited lines with a planted negative; three absence scans each carrying a planted positive. FLOAT-GRADE only where the two repository instruments are re-run (both exit 0, verdict strings pinned). The comparator binds the model only (routing fence below). NO claim-status movement, NO register edit, NO canon movement, NO kill."
disposition: FOUR_GRADINGS_TYPED__COUNT_LIVES_ON_AMBIENT_GAMMA_IN_ITS_CROSS_KREIN_REALIZATION__WALL_CAN_CARRY_IT_AT_EXACTLY_THE_KREIN_ONLY_ANGLE__CHARGE_IS_MINUS_SINE_RELATIVE_ANGLE_EXACT__TRANSPORT_BRIDGE_IMPOSSIBLE_DIRECTION_SUPPLY_REQUIRED__W3_ONE_MISSING_ARROW_NOT_DISCHARGED_NOT_OBSTRUCTED__W6_HANDOFF_AT_LA1_NOT_ABSORBED
target_claim: "RW-1's bill item W3, verbatim from lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md:276-286: 'W3 — the grading bridge (measured, and it is the sharpest item). The hosted mode's charge is graded by the WALL grading, and on the source-shaped mass direction that charge is EXACTLY ZERO in the ambient Gamma grading (§4d). For the hosted count to be the canon chi (the cross-chirality Krein grading of CANON.md:136/139), a typed bridge from wall grading to ambient grading is required. This is the four-way chirality homonym (packet:69) met concretely, and it is PH-K1-PHYSICAL's open map, not a detail: the sigma_2 wall (which DOES host ambient Gamma-charge -1 exactly) differs from the source-shaped sigma_3 wall only by a grading-rotating unitary (§4e) — the count is a grading question, not an operator question.' Also targeted for verification, rw1:824-826: 'W1 and W3 are the two items on which it can still die, and finding either unsuppliable would be a first-class result of the same rank as this join.' NO registered claim is killed; W3 is a bill item on a construction target, and this artifact prices it."
target_claim_verdict: "W3 SURVIVES, REDUCED AND RE-AIMED — NOT DISCHARGED, NOT OBSTRUCTED, NOT A KILL. Reduced: the four-way adjudication W3 asked for is executed; the bridge from the wall grading to the ambient Gamma grading is quantified to a single exact function (hosted charge = -sin of the relative angle between the mass direction and the ambient grading axis) and the doorway condition fuses with it (full charge iff Krein-only exit — W3 and W4 meet at one angle). Re-aimed: the 'typed bridge from wall grading to ambient grading' CANNOT be a transport — proved exactly: every kinetic-preserving unitary is a Krein isometry rotating mass direction and grading jointly, so the charge in the transported grading is an invariant (0 for the source-shaped wall, at every unitary) — it can only be a DIRECTION SUPPLY: one missing arrow, typed in section 3, held jointly by the SC-CHI-02 register owner and RW-1's executing wave. Not obstructed: the required direction exists inside the model's own gapping plane and no source surface forbids it (absence of assertion, certified same-shape as RW-1's W1). The W3-can-die branch did NOT fire."
canon_verdict_change: none
row_change: none
registry_change: none
steering_effect: unchanged
canonical_effect: pending_integration
scripts:
  - tests/channel-swings/joe_directed_gb1_the_bridge_is_one_angle_and_one_missing_arrow.py
depends_on:
  - lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md
  - tests/channel-swings/joe_directed_rw1_zero_locus_steers_not_hosts.py
  - lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md
  - lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md
  - lab/process/homonym-register.yaml
  - CANON.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - tests/function-space-ext/dirac_spectral_flow_section.py
  - tests/function-space-ext/krein_spectral_flow_probe.py
  - lab/methods/gu-base-categories.md
  - lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md
  - explorations/decoupling-constructibility-packet-2026-08-12.md
  - explorations/chirality-grading-and-77-rerun-2026-08-03.md
  - lab/process/correction-registry.yaml
  - lab/sources/source-claim-register.yaml
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
> The comparator here (§2) is the Jackiw-Rebbi wall circle computed on the
> repository's OWN operator class — the continuum fiber of
> `tests/function-space-ext/dirac_spectral_flow_section.py`, the faithful model
> for the `CANON.md:136` row, exactly RW-1 §4's class. Its results bind that
> model. "Krein", "Gamma-charge", "wall grading" and the whole grading
> vocabulary here are repository vocabulary, not source vocabulary. This
> artifact is ABOUT the semantic boundary (which of four same-word gradings
> carries the canon count), which is why the classification is
> `BRIDGE_OR_SEMANTIC_BOUNDARY` and not `INTERNAL_STRUCTURAL_ONLY`.

> [!NOTE]
> **Registry debt, declared rather than silently incurred (LD-A's precedent,
> lda:50-63).** `process_gates/source_native_comparator_routing_audit.py` was
> **already red at HEAD before this artifact existed** (6 unclassified in a
> scope with `UNCLASSIFIED_BASELINE = 5`). This file carries the notice above
> and self-declares `BRIDGE_OR_SEMANTIC_BOUNDARY` in vocabulary, which is what
> the method asks of an author; the registry row is a **transcription owed to
> the method owner** (`lab/process/source-native-comparator-routing-registry.json`
> is outside GB-1's write scope, and the gate's own comment forbids an auditor
> guessing a classification). GB-1 adds one to the printed gap; the wave owner
> should work the backlog once, for the wave. The typed-carrier gate is green
> on this file (its one red is the pre-existing sibling `selected-k151` debt,
> another lane's); the k149 certificate-shape allowlist red is likewise
> pre-existing and untouched.

# GB-1 — the W3 grading bridge: one exact angle, one missing arrow, one handoff

**The question, from the brief.** Which grading carries the external odd count
canon requires, and can a wall-hosted mode carry THAT grading? The answer,
measured: the count lives on the **ambient Γ grading in its cross-Krein
realization** (§1, COUNT); a wall-hosted mode **can** carry it — at exactly one
angle of the wall circle, the Krein-only-exit angle, and at no other (§2); the
source-shaped direction sits at the charge-zero angle; and the one thing the
bridge still needs is not a map but a **direction supply** (§3). The observed
shadow through the non-invertible contraction is W6 and is handed off, not
absorbed (§4).

---

## 0. PREFLIGHT — six problem-matched lenses, declared before the work

- **L1 — Homonym warden (the channel's own lens).** "Chirality" is a
  registered four-way homonym; the fenced register entry `CHIRAL`
  (`lab/process/homonym-register.yaml:242`) additionally fences the PHASE-value
  collision, and its disambiguator rule binds: *"write \"CHIRAL
  (massless/unbroken)\" when naming the PHASE value ... for handedness use the
  CN-2 closed vocabulary S-HALF-SAME / S-HALF-OPPOSITE, never the bare word"*
  (register:263-265). Design answer: every node of the bridge carries its
  sense and loci (§1); no bare cross-sense use anywhere; the register's new
  three-way `Rarita-Schwinger` entry (register:1186, RS-1/RS-2/RS-3 with
  per-sense loci) is the layer-separation precedent this enumeration follows.
  The lens also caught two mount-vs-corpus mismatches, recorded as deviations
  D1-D3 (§8) rather than silently harmonized.
- **L2 — Krein / indefinite-inner-product specialist (LD-B's lens,
  inherited).** "Which grading carries the count" is only well-posed once the
  form's behavior ON the graded pieces is known: LD-B measured the halves
  totally K-null at both physical horns ({K, chi} = 0 iff q odd, ldb:211).
  Prediction: the model's hosted wall modes must reproduce that K-null
  cross-pairing structure or the model is the wrong instrument. Confirmed
  sharper than predicted: K-charge of the hosted mode is exactly 0 at EVERY
  wall angle, and K maps the hosted mode to its anti-normalizable partner
  (§2.3) — the wall-model face of "the form is purely the cross-pairing".
- **L3 — Index/transport analyst (LD-A's lens, inherited).** A charge
  statement at an interior point of a family is not an invariant unless a
  theorem makes it one (LD-A's ruler-tilts finding, lda:9). Prediction: the
  wall charge at intermediate angles will be non-integer and must be
  presented as a grading measurement, not an invariant. Confirmed: charge =
  -sin(phi) is fractional off the poles; the mode is a genuine Γ eigenstate
  IFF phi = ±π/2 (§2.2); the honest invariant is the U-invariant relative
  angle (§2.4).
- **L4 — Layer-typist (base-categories discipline).** Every node must carry
  its Source-Layer position, and the "one unforgivable regression"
  (`lab/methods/gu-base-categories.md` §1.4 — crediting L1 with chirality, or
  the package with an unconditional spectrum) must be structurally impossible
  to read into the bridge. Design answer: §1's table types each node's layer;
  chirality stays VEV-conditional throughout (CC-06 quoted in §7); the bridge
  STOPS at the LA1 boundary and §4 states the stop.
- **L5 — Hostile self-auditor (the import lens, carried from RW-1 §9).** The
  named strongest attack: "the σ₂-type mass is just the comparator's
  pseudoscalar/iγ⁵ mass — you are importing a model-building object and
  calling GU incomplete for lacking it." §6 runs the attack inline; the short
  answer is that the σ₂ direction is typed as a MODEL object throughout, the
  missing arrow is stated as a typing obligation (absence, not defect), and
  the source's own toy is measured silent-not-contrary on the direction
  (grep records, §5).
- **L6 — Claim-targeting auditor.** Kills and discharges must name real
  claims; the wave's documented failure mode is targeting claims the source
  or repository already disavows. This lens fired during retrieval: the
  tasking's W3 phrase "(the four-way chirality homonym, now quantified)" is
  NOT verbatim in RW-1 (exact-substring scan of the rwall artifact: zero hits
  for "now quantified", certified with a planted positive in the probe). The
  `target_claim` above quotes the file's actual W3 text at rw1:276-286, and
  this artifact moves no claim.

Retrieval-first was run before any computation, including
`process_gates/canonical_currency_audit.py` over every consumed input; the
per-input records are §7.

---

## 1. (a) The four gradings, enumerated as typed objects

The brief's four bridge nodes, each typed: carrier, operator or class map,
owner artifact with file:line attestation, and Source-Layer position
(`lab/methods/gu-base-categories.md` §1: L1 declared-total / L2 pullback / L3
pm-package / L4 VEV-observed).

**Two typed notes before the table, so no ordinal does silent work.**

1. **The four-way homonym's own senses vs the brief's four nodes.** The fenced
   four-way is `explorations/decoupling-constructibility-packet-2026-08-12.md:69`,
   verbatim senses: *"(a) ambient 14d grading `omega = e_0..e_13` (printed
   `64+/-`, `832+/-` halves); (b) observed 4d Weyl chirality of physical
   fields; (c) the `Cl^0` complex-structure choice; (d) base-Lorentz label"*,
   with the ruling at `explorations/chirality-grading-and-77-rerun-2026-08-03.md:59`
   ("HOMONYM (four-way, ruling R5)"). The brief's node 2 (the Krein class) is
   **not a sense of this homonym** — it is a pairing, not a grading, and its
   own four-way collision is a SEPARATE registered homonym (`C` / "the
   parity", `lab/process/NAMES.md:18`, mirrored at homonym-register token
   "C (the parity)"). Typing the door as a non-sense is itself part of the
   bridge: the Krein class carries no count; it admits or refuses count
   carriers.
2. **"Internal chirality" is the THIRD-listed sense, not the fourth.** The
   brief glosses node 4 as "the fenced homonym's fourth sense"; in packet:69's
   parenthesis order the fourth is (d) base-Lorentz label, while the sense the
   corpus itself calls "internal chirality" is (c), the `Cl^0`
   complex-structure choice — attested where the joint grading is computed:
   *"every internal chirality half appears with both base-side chiralities in
   equal multiplicity"* (77-rerun:201, the `(ω_4, ω_10)` split with `ω_4` the
   base-Lorentz word and `ω_10` the internal word). Node 4 below is typed as
   sense (c)/`ω_10`; sense (d)/`ω_4` is typed ADJACENT to node 3 (the
   base-Lorentz LABEL on the ambient carrier is upstream of observed 4d Weyl
   through the observation contraction, and they are distinct senses).
   Recorded as deviation D3 (§8).

| node | typed object | carrier | operator / class map | owner + attestation | layer |
|---|---|---|---|---|---|
| **N1 AMBIENT-GAMMA** (sense a) | the ambient chirality grading | `V (x) S` at `D_7` (ambient); model fiber `C^2 (x) L^2(R)` | ambient: `chi` = the product of all fourteen gammas (ldb §2.1); the 14D volume word `omega = e_0..e_13` (packet:69); model: `Gamma = sigma_3 (x) I` (`tests/function-space-ext/dirac_spectral_flow_section.py:8`). The COUNT OBJECT on it is the graded trace `n_- = tr(Gamma P_<0)` (instrument:18; lda:301) | packet:69; `dirac_spectral_flow_section.py:8`; lda:9, :301 | operator at L1 (exists on the declared total unconditionally); its use AS a chirality count is L4-conditional through LA3 (CC-06; SG4 bit 2 OPEN) |
| **N2 KREIN-CLASS** (the door — NOT a homonym sense) | the (self-adjoint, Γ-odd, Krein-self-adjoint) interior class and its exit | same carriers; ambient Krein form `K = eta_V (x) beta_S` (NAMES.md:18 sense a); model `K = sigma_1 (x) I` (instrument:9) | membership predicate, not a grading: `D^dag K = K D` with `K Gamma = -Gamma K` (cross); the DOORWAY: *"Nonzero flow requires leaving the Krein-Dirac class"* (instrument:29); *"Such a background breaks the interior Krein-self-adjoint class -- exactly why it lies outside (I)"* (synthesis:56-57) | CANON.md:136; synthesis:56-57, :60; ldb:198, :200, :211 (parity: `{K, chi} = 0` exactly at odd `q`; both physical horns odd; halves totally null) | repository-construction on the L1 carrier; the source never uses the pairing vocabulary (RW-1 §4 fence) |
| **N3 OBSERVED-WEYL** (sense b) | observed 4d Weyl chirality of physical fields | post-contraction 4D content (L2) | downstream of LA1, the observation contraction `(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab` (base-cat CA2 :291), **NOT injective** (LA1 row :89), with NO inverse (non-arrow N2 :106); the sense-(a)→(b) bridge is *"exactly PH-K1-PHYSICAL's open map — never silently identified"* (packet:69) | packet:69; gu-base-categories.md:89, :106, :291 | L2; everything at this node is W6's scope, not GB-1's (§4) |
| **N4 INTERNAL** (sense c) | internal chirality — the `Cl^0` complex-structure / `ω_10` grading (the internal `64+/-` halves; one level down, the internal `16` vs `16bar`) | the internal tensor factor of the ambient carrier; model surrogate: the supplied multiplicity space `C^N` | the internal volume word `ω_10` in the joint `(ω_4, ω_10)` grading; banked balance: `tr(ω_4) = 0` inside EACH `ω`-half (77-rerun:201) — the ambient half does not determine the internal half | packet:69 sense (c); 77-rerun:59, :96, :201; RSC-1's RS-2 "internal" layer vocabulary (register:1186 entry) | L1 structure; every COUNT statement touching it is fenced by CC-05 (multiplicity supplied, 2+1 subtractive — §7) |

**Which grading carries the external odd count (the COUNT verdict).** The
canon decomposition is `chi = interior-even + external-topological-index`
(CANON.md:139, *"so any odd count is necessarily external"*, synthesis:60);
the class it is stated on is *"self-adjoint, chirality-odd,
Krein-self-adjoint"* (CANON.md:136); the computed external exemplar carries
*"net chiral index = flux number"* (CANON.md:135); and the count object is the
graded trace `tr(Gamma P_<0)` (instrument:18, lda:301). All four sentences
grade by **N1, the ambient Γ**, with N2 supplying the admissibility structure
(the cross-Krein realization: `{K, chi} = 0` at both physical horns, ldb:211,
:198, :200). The count does NOT live on N2 (a pairing carries no signed
count; the halves are K-null at odd q — nullity is the compatibility
condition, not the ledger), NOT on N3 (downstream of a non-invertible
contraction, W6-untyped), NOT on N4 (a supplied multiplicity factor, CC-05
fence). RW-1's own W3 wording "the canon chi (the cross-chirality Krein
grading of CANON.md:136/139)" is exactly this: the Γ grading OF the
cross-Krein class — N1 qualified by N2, not N2.

**Pairwise maps between the four nodes** (PROVED / CONSTRUCTIBLE / MISSING,
with what each would consume):

| pair | map | status |
|---|---|---|
| N1↔N2 | not a grading-to-grading map: the JOINT-REALIZATION constraint. Model-exact (§2): every gapping wall exits the Krein class uniformly; full N1-graded hosted charge iff the exit is Krein-only; hosted modes K-null with K cross-pairing mode↔mirror. Ambient: the odd-q parity `{K, chi} = 0` (ldb:211) realizes the same cross structure at both physical horns; the (14,0) even-q contrast (K = chi, halves definite) is the contrary control, reproduced in-model by the commuting-K variant whose zero-order class is exactly {0} (§2.5) | **PROVED** (model exact; ambient at ldb's numerical grade, both horns) |
| N1↔N4 | product factorization: the wall mechanism is internal-blind — `ker(D (x) I_N) = ker(D) (x) C^N` exact at generic wall angle (§2.6, extending RW-1 §4g); ambient face banked: the joint `(ω_4, ω_10)` grading is balanced 32/32/32/32 (77-rerun:96, :201). The COUNT transfer N1→N4 (which internal charge the hosted modes carry) is SUPPLIED, never derived — CC-05 fence | factorization **PROVED**; count transfer **MISSING BY TYPE** (supplied input, not an arrow to build) |
| N1↔N3 | the observation contraction LA1 then the sense-(a)→(b) identification: PH-K1-PHYSICAL's open map, never silently identified (packet:69); LA1 non-injective (base-cat:89), no inverse (N2 non-arrow, :106) | **MISSING = W6.** Outside GB-1's scope; handoff §4 |
| N2↔N3 | a Krein/positivity structure on observed content: nothing exists; observed-quotient positivity is source-OPEN, not disavowed (CC-02's operative content, not consumed further here) | **MISSING**, downstream of W6 |
| N2↔N4 | the class conditions are internal-blind in the model (`K (x) I_N` commutes with the internal action — same §2.6 factorization); on the physical carrier this is exactly the (9,5)/ker-Γ transport rung-2 fenced open | model leg **PROVED**; carrier leg **MISSING = M5** (inherited unchanged from RW-1) |
| N3↔N4 | the observed-embedding question (which internal states present as which observed 4d Weyl fields) — comparator-fenced SM-embedding territory | **MISSING and FENCED**; not touched |

---

## 2. (b) The RW-1 unitary, reproduced and extended: the wall circle in closed form

**Routing fence, repeated at the point of use.** Everything in this section is
computed on the repository's own operator class — `Gamma = sigma_3`, Krein
`K = sigma_1`, `D = sigma_1 p + m(y) M` on `C^2 (x) L^2(R)`, the continuum
fiber of `tests/function-space-ext/dirac_spectral_flow_section.py` — RW-1
§4's class, exactly. It binds this model. Certificate: probe LEGs 2-3, all
closed-form sympy.

### 2.1 Pinned re-runs of RW-1's cited legs (reproduction target, §4 a/b/d/e)

Reproduced exactly, as pinned re-runs (probe LEG 2):

- **(a) class/gap algebra.** Over the complete Hermitian zero-order Pauli
  basis: `sigma_1` is the one class member and does not gap; `sigma_2` gaps
  and exits ONLY the Krein condition (Γ-oddness kept); `sigma_3`
  (source-shaped, `m = R/4`) gaps and exits BOTH. Exact eigenvalues
  `±sqrt(p^2 + m^2)` on the gapping directions.
- **(b) mode reduction, generic `m(y)`.** `exp(-∫m) chi_+` / `exp(+∫m) chi_-`
  solve the `sigma_3` wall exactly (`chi_±` the `sigma_2` eigenvectors);
  `exp(-∫m) e_2` / `exp(+∫m) e_1` solve the `sigma_2` wall exactly (Γ
  eigenvectors). The planted wrong-chirality candidate is flagged NONZERO.
- **(d) charges.** `chi_±^dag sigma_3 chi_± = 0` — ambient Γ-charge EXACTLY 0
  on the source-shaped wall's mode (rw1:368). `e_2^dag sigma_3 e_2 = -1` —
  EXACTLY -1 on the `sigma_2` wall's mode, whose class exit is Krein-only
  (rw1:370-371).
- **(e) the grading-rotating unitary.** `U = exp(-i pi sigma_1/4)` is
  unitary, commutes with the kinetic term, carries `sigma_3` to `-sigma_2`
  (the ± ambiguity RW-1's own probe accepts), and does NOT preserve Γ
  (rw1:375-379).

### 2.2 The extension: the full wall circle, one angle parameter

Parametrize the gapping plane by the fiber angle `phi` from the source-shaped
direction: `M(phi) = cos(phi) sigma_3 + sin(phi) sigma_2`, `M(phi)^2 = I`,
`{M(phi), sigma_1} = 0` (every angle gaps: `D^2 = p^2 + m^2`). All of the
following are exact symbolic identities at GENERIC `phi` and generic profile
`m(y)` (probe LEG 3):

1. **The wall grading is the angle-shifted mass direction.** The first-order
   reduction gives `psi' = -m G(phi) psi` with
   `G(phi) = cos(phi) sigma_2 - sin(phi) sigma_3 = M(phi + pi/2)`: the
   hosted mode is graded by the direction a quarter turn from the mass. The
   normalizable solutions are `exp(-∫m) v_+(phi)` and `exp(+∫m) v_-(phi)`
   with `G(phi) v_± = ± v_±` — verified as exact zero modes symbolically.
2. **Hosted ambient Γ-charge = -sin(phi), exactly.**
   `v_+^dag sigma_3 v_+ = -sin(phi)`; the anti-kink mode carries
   `+sin(phi)`. At `phi = 0` (source-shaped): 0 — RW-1's §4d leg. At
   `phi = pi/2` (`sigma_2` wall): -1 — RW-1's other §4d leg. In between the
   charge is FRACTIONAL — the wall-side face of LD-A's ruler-tilt (the graded
   trace is not an integer off the poles; lda:9).
3. **The Γ-eigenstate condition is the pole condition.** `v_+(phi)` is a
   genuine Γ eigenstate iff `|sin(phi)| = 1`. Off the poles the hosted mode
   is a superposition in the canon grading; a COUNT (an integer index entry)
   is carried only at `phi = ±pi/2`.
4. **The two exit residuals, exactly.** Γ-oddness:
   `{M(phi), Gamma} = 2 cos(phi) I` — residual `2|cos(phi)|`. Krein:
   `[M(phi), K]^dag [M(phi), K] = 4 I` — the Krein exit is UNIFORM, operator
   norm 2 at EVERY angle. Every hosting wall walks through canon's door; the
   door is angle-blind. What the angle controls is the GRADING.
5. **The Pythagoras identity.** `(hosted Γ-charge)^2 + ({M, Gamma}
   residual/2)^2 = sin^2 + cos^2 = 1`, exactly: the hosted canon-graded
   charge and the wall's Γ-oddness violation are complementary. **FULL
   canon-graded charge iff the exit is Krein-only** — the three-way iff:
   `|charge| = 1` ⟺ `{M, Gamma} = 0` ⟺ the wall exits the interior class
   through the Krein condition alone. W3's grading demand and W4's doorway
   demand meet at one angle, `phi = ±pi/2`, and nowhere else.

### 2.3 The Krein form on the hosted modes: K-null at every angle, cross-pairing exact

`v_±^dag K v_± = 0` for every `phi` — the hosted mode is **K-null at every
wall angle** — and `K v_+ = i v_-` exactly: K maps the hosted mode to its
anti-normalizable mirror partner, and `{K, G(phi)} = 0` for every `phi`. This
is the wall-model face of LD-B's banked ambient structure at both physical
horns: the halves totally isotropic and *"the form is purely the
cross-pairing between a generation and its mirror"* — here reproduced as
exact fiber algebra, for the whole circle at once. K-nullity of the
count-carrying mode is the EXPECTED odd-q structure, not an obstruction: the
count is the graded trace, not a K-norm.

### 2.4 The unitary questions, answered exactly

- **Does the grading-rotating unitary preserve the Krein class?** YES,
  exactly — and more: the entire kinetic-preserving unitary family is a
  KREIN-ISOMETRY circle. The commutant of `sigma_1` in `M_2(C)` is
  `span{I, sigma_1}` (computed symbolically: `[U, sigma_1] = 0` forces
  `a_21 = a_12, a_22 = a_11`), so every kinetic-preserving unitary is
  `e^{i alpha} exp(-i theta sigma_1/2) = e^{i alpha} U(theta)`, and
  `U(theta)^dag K U(theta) = K` exactly. The Krein structure cannot see the
  rotation. (This is the same circle as
  `tests/function-space-ext/krein_spectral_flow_probe.py`'s control [2] —
  Krein-isometric conjugacy — re-run green in probe LEG 4.)
- **Does it preserve the ambient Γ-charge?** NO — `U(theta)` rotates mass
  directions and the grading by the SAME angle:
  `U(theta) M(phi) U(theta)^dag = M(phi - theta)` and
  `U(theta) Gamma U(theta)^dag = M(-theta)`. The fixed-Γ charge of the
  transported source-shaped wall's mode is `sin(theta)`, exactly: 0 at
  `theta = 0`, full ±1 at `theta = ∓pi/2` (RW-1's U is `theta = pi/2`).
  Within the circle, the Γ-stabilizer is discrete: `Gamma` is preserved only
  at `theta ≡ 0` and negated at `theta = pi` — no continuous rotation fixes
  it.
- **Is there a unitary making the hosted mode Γ-charged AND Krein-exiting
  simultaneously?** YES — realized, not obstructed: `U(pi/2)` carries the
  source-shaped wall to the `sigma_2`-type wall, which hosts full fixed-Γ
  charge AND exits through the Krein condition alone; and by §2.2(5) that
  simultaneous configuration exists at exactly the two poles `phi = ±pi/2`
  of the circle, nowhere else.
- **The exact obstruction (the complementary fact).** The relative angle
  between the mass direction and the grading is a UNITARY INVARIANT
  (both rotate together), so **the charge in the TRANSPORTED grading never
  moves**: computed exactly, the transported source-shaped wall's mode has
  charge 0 in the transported grading at every `theta`. A unitary can
  re-aim the ruler; it cannot change what the pair (operator, ruler)
  measures. Consequence for W3's wording: the *"typed bridge from wall
  grading to ambient grading"* CANNOT be built as a transport — what makes
  the `sigma_2` wall canon-charged is not that a unitary relates it to the
  source-shaped wall (one does; the charge does not follow) but that its
  MASS DIRECTION sits at the Krein-only angle relative to the FIXED ambient
  Γ. The bridge is a direction fact, not a transport fact. RW-1's "the count
  is a grading question, not an operator question" (rw1:285-286) is
  confirmed and sharpened: it is a RELATIVE-ANGLE question.

### 2.5 The contrary control: the even-q / commuting-K face

LD-B's parity criterion says the cross structure this whole bridge lives on
holds IFF `q` is odd (`{K, chi} = 0` exactly at odd `q`, ldb:211; at `(14,0)`,
`beta_S` IS the chirality operator and the halves are definite). The model
face, computed exactly: replacing the cross Krein form by the commuting one
(`K' = Gamma`, the `q = 0` structure `K = I (x) chi`) collapses the zero-order
interior class to `{0}` — `{M, Gamma} = 0` and `[M, K'] = 0` together force
`M = 0` — so the odd-q cross structure is not decoration: it is what makes
the class, the door, and the K-null count-carrying modes possible at all. The
instrument discriminates; the bridge is odd-q-conditional exactly as LD-B's
ambient sweep says.

### 2.6 Internal-blindness at generic angle

`ker(D (x) I_N) = ker(D) (x) C^N` verified symbolically at generic `phi`
(N = 3): the wall mechanism commutes with the internal factor at every angle.
Composed with the banked joint-grading balance (77-rerun:201), the N1↔N4
arrow of §1 is a product factorization with the count transfer SUPPLIED —
and the CC-05 fence binds it (§7): a hosted `N = 3` would be an additive
count; the source's partition is subtractive 2+1.

---

## 3. (c) The W3 verdict: the bridge as a needs/provides chain

**The chain, link by link.** External odd count lives in grading N1 (typed,
with the canon sentences that say so); the wall-hosted mode's charges are
computed in each grading; the missing arrow is exactly one.

- **Link A (canon, PROVED).** The count object is the N1-graded trace; any
  odd `chi` is external; external backgrounds exit the interior class.
  *"chi = interior-even + external-topological-index"* (CANON.md:139);
  *"Net chiral spectral flow 0 for self-adjoint, chirality-odd,
  Krein-self-adjoint Fredholm families"* (CANON.md:136); *"net chiral index
  = flux number"* (CANON.md:135); *"Nonzero flow requires leaving the
  Krein-Dirac class"* (instrument:29); *"any ODD generation count is
  necessarily external"* (synthesis:60).
- **Link B (ambient realization, PROVED at LD-B's numerical grade, both
  horns).** The N1/N2 compatibility structure on the physical carrier is the
  odd-q cross parity: `{K, chi} = 0` exactly at odd `q` (ldb:211), halves
  totally null at `(9,5)` and `(7,7)` (ldb:198, :200). The model's cross
  `K Gamma = -Gamma K` is the same structure (§2.5's contrast shows the
  even-q alternative kills the class).
- **Link C (the wall leg, PROVED exact in the model — GB-1 §2 on RW-1 §4).**
  A zero-order wall hosts `|winding|` modes; the hosted mode's N1-charge is
  `-sin(phi)`; it is a genuine N1 eigenstate iff `phi = ±pi/2` iff the exit
  is Krein-only; hosted modes are K-null with K cross-pairing them to their
  mirrors at every angle; the mechanism is internal-blind (N4 untouched,
  multiplicity supplied). So: **a wall-hosted mode CAN carry the canon
  grading — at, and only at, the Krein-only angle.**
- **Link D — THE MISSING ARROW (exactly one, typed).**
  **MISSING-ARROW-W3-DIRECTION:** *a source-attested or repository-
  constructed zero-order deformation of the Dirac-type operator whose fiber
  direction carries a nonzero `sigma_2`-type component — Γ-odd and
  Krein-breaking, i.e. anticommuting with BOTH the kinetic symbol and the
  ambient grading — on the physical carrier.* The source's one stated
  deformation is `dslash_A psi_L(y) = (R(y)/4) psi_R(y)` (SC-CHI-02,
  register:940): one real coupling, purely the `phi = 0` (`sigma_3`-type)
  direction, hosted N1-charge exactly 0; and *"The source's stylized toy
  does not distinguish these two mass directions (it writes one real
  coupling); the distinction is the W3 bridge"* (rw1:372-373). Holders:
  **jointly** the source-claim register owner for SC-CHI-02 (type which
  fiber direction — if any — the stylized coupling commits to, or record
  direction-silence as a register note) and the wave executing RW-1's
  `TYPED-TARGET-VEV-ORIENTATION-WALL-R-STEERED` (whose Wall-2 construction
  must supply the mass DIRECTION, not just the profile); the exit-typing
  half lands on the external-by-structure owner as W4 inheritance — **with
  the new typed condition that the exit the wall route needs is exactly the
  Krein-only one** (§2.2(5)), the minimal exit canon's control names.
- **Link E (composition ceiling).** Even with D supplied, the chain delivers
  HOSTING of the external odd count on the Y-side wall in grading N1 —
  |winding| = 1 generic (rung-2 null, inherited through RW-1 unchanged),
  multiplicity supplied (CC-05 fence). It does not derive 3. It does not
  derive 1.
- **Link F (termination).** The count now lives at the wall, on N1, on Y.
  Transport to N3 (observed 4d Weyl) is W6 — §4.

**Composition verdict.** Links A-B-C compose exactly; link D is MISSING; so
**W3 is NOT DISCHARGED**. Link D is **not obstructed**: the required
direction exists inside the model's own gapping plane (it is one of RW-1's
two computed gapping directions), and no source surface asserts the mass
direction is exclusively the standard one — direction-silence, certified as
absence-of-assertion (grep records §5), the same evidential shape as W1's
missing crossing. So **the W3-can-die branch did not fire**, and no kill is
declared: `target_claim_verdict` above names what would have been the kill's
target had an obstruction been found (rw1:824-826's "finding either
unsuppliable"), and the measured answer is the opposite — suppliable in
principle, unsupplied in fact.

**What W3 gains from this arc (the reduction).** Before: "a typed bridge from
wall grading to ambient grading is required" — a four-way homonym
adjudication of unknown shape. After: the adjudication is executed; the
bridge is a single exact function (charge = -sin of the U-invariant relative
angle); the transport route is closed exactly (§2.4); the doorway fuses with
the grading at one angle (W3 meets W4 at `phi = ±pi/2`); and the entire
residue is one named arrow with named holders. W3's rank as a
still-can-die item drops accordingly: it dies only if the `sigma_2`-type
direction is shown UNSUPPLIABLE on the physical carrier — which would now be
a one-arrow, kill-rank result, exactly as RW-1 priced it.

---

## 4. (d) The handoff to W6, stated and not absorbed

The bridge built here ends at the wall, on Y: an N1-graded hosted count,
admitted through the N2 door, internal-blind at N4. It does NOT reach N3.
What remains between the wall and observation is exactly RW-1's W6 — *"the
observed shadow"* — UNTYPED, and outside this arc's scope: the observation
arrow is LA1, the contraction `(s^* omega)_mu = omega_mu + omega_(ab) d_mu
g_ab` (base-cat CA2 :291), **NOT injective** (kernel the section-dependent
10-plane, LA1 row :89), with the inverse a NAMED NON-ARROW (N2 row :106) —
so no property of the wall-hosted N1 count may be credited to observed 4d
Weyl content, in either direction, by anything short of the map W6 would
have to construct. GB-1 hands off at that boundary: the deliverable of this
arc is that IF W6 is ever typed, what it receives at the boundary is now
exact — a K-null, N1-eigenstate mode of integer charge at the Krein-only
angle, or nothing. GB-1 absorbs no part of W6 and types none of it.

---

## 5. Grep-before-novelty records (exact-substring, repo-wide, recorded per rule)

Scans run 2026-08-17 over `*.md`/`*.py` outside `_local/` (and excluding this
arc's own two files where marked SELF-EX). Zero hits is NOT evidence of new;
these are collision checks, and the two nonzero collisions were read and are
unrelated.

| claim guarded | pattern(s) | hits | reading |
|---|---|---|---|
| the angle parametrization is unwritten | "wall angle", "gapping circle", "gapping plane", "relative angle", "mass angle", "charge interpolat" | 0 / 0 / 0 / 0 / 0 / 0 (SELF-EX) | no prior angle-parametrized wall treatment found by these tokens |
| the iff is new beyond RW-1's endpoints | "Krein-only" | 1 file: the RW-1 artifact | RW-1 states the `sigma_2` POLE fact; the circle/iff is this arc's extension of it |
| the Pythagoras identity is unwritten | "Pythagor" | 4 files | read: H29's is a `C2` norm split, the others transcripts — unrelated |
| K-null hosted modes could be already banked | "Krein-null" | 52 files | heavily banked FOR THE AMBIENT HALVES (ghost-parity canon, LD-B); §2.3 is presented as the model face / consistency reproduction of that banked structure, NOT as novel |
| stabilizer computation is unwritten | "joint stabilizer" | 13 files | read: all group-orbit/coadjoint stabilizers — unrelated object |
| mount-vs-file W3 phrase | "now quantified" in the rwall artifact | 0 | deviation D1: the tasking's phrase is not RW-1's text; target_claim quotes the file |
| destination duplicate (memory rule) | `grading-bridge/*.md`, `joe_directed_gb1_*` | this arc's two files only | no duplicate seed at the destination |

All three absence claims consumed by verdicts carry planted-positive controls
in the probe (LEG 5).

---

## 6. Hostile review, inline — the strongest attack, named at preflight

**"The `sigma_2` direction is the comparator's pseudoscalar mass. You have
imported a textbook object — every model-builder knows a Dirac operator
admits `m_1 psi-bar psi + m_2 psi-bar i gamma_5 psi` — dressed it as 'the
missing arrow', and indicted GU for not supplying a term nobody promised."**

Three answers, each measured:

1. **The import direction is inverted, and the fence is carried.** GB-1 does
   not claim GU needs the comparator's term; it measures that CANON'S OWN
   count grading is carried by a hosted mode ONLY at that fiber angle — a
   statement internal to the repository's own model class (the same class
   canon's net-0 row is proved on), fenced `BRIDGE_OR_SEMANTIC_BOUNDARY`.
   Whether the PHYSICAL carrier admits such a direction is exactly what link
   D leaves with its holders; §3 states "suppliable in principle, unsupplied
   in fact", not "GU lacks it".
2. **The attack concedes the reduction.** If the `sigma_2`-type direction is
   a standard, easily-available object in any faithful realization, then W3's
   residue is SMALL — which is this artifact's verdict. If instead the
   physical carrier's structure forbids it, that is the one-arrow kill §3
   prices. Either way the four-way adjudication is done and the question is
   now one typed arrow, not a homonym fog.
3. **What the attack genuinely lands on.** The 1D fiber has exactly one
   Krein-only direction; the physical carrier's gapping-direction geometry
   (which zero-order insertions are Γ-odd and Krein-breaking on `V (x) S`
   at `D_7`) is NOT computed here — it is LD-B §2.2-adjacent machinery and
   is named as the natural first computation of link D's holders. Conceded
   as scope, inherited by M5's transport fence, and stated rather than
   papered.

**Second attack, self-run: "charge = -sin(phi) is numerology on a 2x2
fiber."** The function is exact structure, not a fit: it is forced by the
quarter-turn law `G(phi) = M(phi + pi/2)` plus the Bloch geometry of the
fiber, verified at generic `m(y)` symbolically; its two poles are RW-1's two
banked endpoint measurements; and its consequence (the three-way iff) is the
load-bearing item, invariant under reparametrization of the circle.

---

## 7. Frame carried — the standing corrections, quoted at their operative sentences

From `lab/process/correction-registry.yaml` `canonical_source_corrections`
(the key this mount requires read and quoted):

- **CC-06** (registry:291-305): the superseded reading is *"That the source
  has no stated effective-chirality mechanism, or that chirality can only
  come from an unbuilt mirror-gapping condensate"* — corrected: *"when
  observed chirality is VEV-CONDITIONAL (\"exactly three families of chiral
  fermions if you have a decreased VEV ... taking a Dirac equation into two
  [Weyl] equations\", drafts L158 / ucsd 00:46:02) and the selector is SG4
  bit 2, OPEN by design"* (registry:302, :305). Carried: SC-CHI-01's
  declared total is NON-CHIRAL and *"splits at the emergent level"*
  (register:913); every chirality statement here is VEV-conditional through
  LA3; **SG4 bit 2 stays OPEN** — nothing in this artifact assumes the
  split, and the count usage of N1 is typed L4-conditional in §1.
- **CC-05** (registry:258-268): *"That three generations is an ADDITIVE
  target count a mechanism must produce"* — corrected: the source says
  *"really two plus one"* and *"HE-1 makes the partition FORCED and
  SUBTRACTIVE (n_g -> n_g - 1, unlabelled, the distinguished family
  REMOVED)"* (registry:267-268). Carried at §2.6 and link E: multiplicity is
  supplied; a hosted N = 3 would be additive; the 2+1 stays owned by
  representation content. The third family is the spin-3/2-native imposter
  under the settled label fork; nothing here re-litigates it.
- **CC-08** (registry:357-367): *"That the 128 remainder is an established
  DEFECT of the construction"* — corrected: the remainder is a
  *"partner-placement / decoupling OBLIGATION, not an established defect"*
  (registry:367). Carried: N4's typing cites the RS-corner layer separation
  (the 128 inside RS-2 hence RS-1, not RS-3) and imports no defect framing.

### Canonical-currency check records (for the integrator; GB-1 edits no sidecar)

`process_gates/canonical_currency_audit.py` run 2026-08-17 (registry 10
canonical corrections; 183 dirty (file, correction) pairs repo-wide; warn-only
by design). **Zero of GB-1's consumed inputs appear in any dirty queue at
this run.** Per-input records:

1. `explorations/decoupling-constructibility-packet-2026-08-12.md` — was
   dirty under CC-05 and CC-08 at RW-1's writing; now carries recorded
   sidecar checks (`lab/process/canonical-currency-checks.yaml:412-430`, by
   RW-1, 2026-08-17, CLEARED-CONSISTENT both). GB-1 independently re-checked
   the rows it consumes (:69 the homonym row, :259 R3's dark-typing): no
   additive-count framing, placement-obligation framing kept.
   **CLEARED-CONSISTENT — CONCUR** (pointers: packet:69, :259; sidecar
   :412-430; this artifact §1, §2.6, §7).
2. `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` — consumed
   here only THROUGH RW-1's quotes (the SC-CHI-01 hedge chain); its CC-06 and
   CC-08 sidecar checks are recorded (sidecar:393-411, by RW-1,
   CLEARED-CONSISTENT). GB-1's uses keep the VEV-conditional reading
   throughout. **CLEARED-CONSISTENT — CONCUR** (pointer: sidecar:393-411;
   this artifact §7 CC-06 record).
3. All other consumed inputs — the RW-1 artifact + probe, LD-A, LD-B, RSC-1,
   `gu-base-categories.md` (all created 2026-08-17, postdating every
   `canonical_since`), `homonym-register.yaml`, `CANON.md`,
   `canon/external-by-structure-synthesis-RESULTS.md`, both function-space
   instruments, `chirality-grading-and-77-rerun-2026-08-03.md`,
   `source-claim-register.yaml` (CC-06 co-owner), `correction-registry.yaml`
   itself, `VERIFICATION.md` — **absent from every dirty queue at this run**
   (verified by grep over the audit's full output; the audit output is
   reproduced by re-running the gate). No STALE-FOUND. GB-1 records these
   here and edits no sidecar.

---

## 8. Deviations from the mount, recorded

- **D1.** The mount quotes W3 as *"the grading bridge (the four-way chirality
  homonym, now quantified)"*. That phrase is not in RW-1 ("now quantified":
  zero hits in the rwall artifact, planted-positive-certified, probe LEG 5).
  The `target_claim` quotes RW-1's actual W3 text at rw1:276-286. No other
  mount instruction is affected.
- **D2.** The mount's node 2 (the Krein class) is not a sense of the four-way
  chirality homonym; it is typed in §1 as the door, with its OWN separate
  registered collision (`C` / "the parity", NAMES.md:18). The bridge is
  built on the mount's four nodes with that typing explicit.
- **D3.** The mount's "INTERNAL chirality (the fenced homonym's fourth
  sense)": the sense the corpus calls internal is the THIRD listed
  (packet:69 sense (c), `Cl^0` / `ω_10`; attestation 77-rerun:201); the
  literal fourth listed is the base-Lorentz label, typed adjacent to node 3.
  §1 note 2 carries both, identified with loci, nothing silently merged.
- **D4.** The mount says the four-way homonym is "in
  `lab/process/homonym-register.yaml`"; the register's fenced `CHIRAL` entry
  (register:242) is the two-sense PHASE/handedness fence, and the four-way
  itself lives at packet:69 with ruling R5 at 77-rerun:59. Both were read
  first and both discipline this artifact; recorded rather than harmonized.

---

## 9. Machine-readable verdicts and certificate

<!-- GB1-TABLE-BEGIN -->

| id | question | verdict | evidence_key |
|---|---|---|---|
| ENUM | the four gradings as typed objects | FOUR-NODES-TYPED-KREIN-IS-DOOR-NOT-SENSE | typed_node_pins |
| COUNT | which grading carries the external odd count | AMBIENT-GAMMA-IN-CROSS-KREIN-REALIZATION | canon_and_parity_pins |
| REPRO | RW-1's cited comparator legs | REPRODUCED-EXACT | rw1_leg_rerun |
| CIRCLE | the wall circle, quantified | CHARGE-IS-MINUS-SINE-RELATIVE-ANGLE | phi_circle_exact |
| DOOR | hosted charge vs class exit | FULL-CHARGE-IFF-KREIN-ONLY-EXIT | iff_and_uniform_exit |
| UNIT | can a unitary transport deliver the canon grading | TRANSPORT-CANNOT-DIRECTION-MUST | invariance_legs |
| W3 | the bill item | ONE-MISSING-ARROW-NOT-DISCHARGED-NOT-OBSTRUCTED | chain_composition |
| W6 | the observed shadow | HANDOFF-AT-LA1-UNTYPED-NOT-ABSORBED | la1_pins |

<!-- GB1-TABLE-END -->

**Verdict-evidence binding (probe LEG 6 enforces; the selftest's contrary
control flips W3 to DISCHARGED and must be caught).**

| evidence_key | asserted direction | measured |
|---|---|---|
| typed_node_pins | ENUM requires the four senses pinned at packet:69 / 77-rerun:59 and the door pinned as non-sense (NAMES.md C-parity collision separate) | all pins green (LEG 1) |
| canon_and_parity_pins | COUNT requires CANON.md:135/:136/:139 + instrument:18/:29 + ldb:198/:200/:211 all pinned and consistent | all pinned; count object Γ-graded; parity odd-q |
| rw1_leg_rerun | REPRO requires charges 0 and -1 exact, class table exact, U properties exact | reproduced (LEG 2) |
| phi_circle_exact | CIRCLE requires charge(v+) = -sin(phi), charge(v-) = +sin(phi), generic-m solutions exact, K-charge 0, K v+ = i v- | exact at generic phi (LEG 3) |
| iff_and_uniform_exit | DOOR requires {M,Gamma} = 2cos(phi) I, [M,K] norm 2 uniform, Pythagoras, eigenstate-iff | exact (LEG 3) |
| invariance_legs | UNIT requires the commutant computation, Krein isometry of the circle, joint rotation, transported-grading charge invariant at 0, fixed-Gamma charge sin(theta) | exact (LEG 3) |
| chain_composition | W3 requires links A-C pinned/computed green AND link D typed AND no obstruction claim | composed; one missing arrow; absence-not-assertion certified |
| la1_pins | W6 requires LA1 non-injectivity and the N2 non-arrow pinned, and the artifact's own text absorbing nothing | pinned; "NOT absorbed" present (LEG 6) |

**Certificate.**
`tests/channel-swings/joe_directed_gb1_the_bridge_is_one_angle_and_one_missing_arrow.py`

- Live run: all legs green, exit 0 (114 checks) — LEG 1 byte pins (43 +
  planted negative); LEG 2 RW-1 reproduction (exact); LEG 3 the circle (exact,
  generic `phi` and generic `m(y)`, including the planted wrong-chirality
  control and the commuting-K contrast); LEG 4 both repository instruments
  re-run with pinned verdict strings; LEG 5 the three certified absence
  scans with planted positives; LEG 6 the artifact binding with SHA-pinned
  table, closed verdict set, and claim-ceiling strings.
- `--selftest`: clean baseline verified FIRST (count pinned independently)
  and a red baseline aborts; 9 mutations, every one corrupting machinery or
  a reference (a pin's line number, the Γ constant, the residual flagger,
  the charge-law reference, the unitary generator, the scan tokens, the
  contrary-control artifact copy, the instrument path, the contrast form),
  each REQUIRED to be caught by its targeted check with a genuine [FAIL]; a
  crash is CRASH-NOT-DETECTION and fails; an untargeted catch is
  INCIDENTAL-NOT-TARGETED and fails; the failing checks are printed for
  every mutation; baseline re-verified after; exit 0 iff green. Tolerances:
  none — every LEG 2/3 statement is symbolic, so no tolerance can absorb a
  plant.
- Read-only; planted corpora and the contrary-control copy live in a temp
  directory and are removed. Deterministic; sympy + stdlib (numpy only via
  the re-run instruments).
- What the probe does NOT certify: anything about the true RS `Y14` bundle
  or the `(9,5)`/ker-Γ carrier (M5 fence inherited); the gapping-direction
  geometry of the physical carrier (link D's holders' first computation);
  any file joining these vocabularies with tokens outside the scanned
  families; and LD-B's ambient sweep itself (consumed at its own recorded
  grade, not re-run here).

---

## 10. Typed objects (typed-carrier gate)

```gu-typed-objects
result:         The wall circle on RW-1's comparator class, closed form: for
                mass direction M(phi) = cos(phi) sigma_3 + sin(phi) sigma_2,
                the hosted zero mode is graded by G(phi) = M(phi + pi/2), its
                ambient Gamma-charge is exactly -sin(phi) (anti-kink
                +sin(phi)), its Krein charge is exactly 0 with K v+ = i v-,
                the Gamma-oddness residual is 2|cos(phi)|, the Krein exit is
                uniform (norm 2), charge^2 + cos^2 = 1, the mode is a Gamma
                eigenstate iff phi = +-pi/2 iff the exit is Krein-only; the
                kinetic-preserving unitaries are the Krein-isometry circle
                rotating mass and grading jointly, so the relative angle and
                the transported-grading charge are invariants
carrier:        D = sigma_1 (x) p + m(y) M(phi) on C^2 (x) L^2(R), the
                continuum fiber of the periodic-lattice cross-chirality
                Krein-Dirac model of
                tests/function-space-ext/dirac_spectral_flow_section.py
                LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing:        cross-chirality Krein form K = sigma_1, K^2 = I,
                K Gamma = -Gamma K ON=C^2 (x) L^2(R) (the model Krein space,
                NOT the (9,5) / Cl(9,5) S = H^64 carrier; evaluated on the
                hosted modes: K-null, cross-pairing mode to mirror)
real_structure: complex Hermitian symbolic; no quaternionic or real
                structure used or claimed; explicitly NOT the (9,5)
                real-form fork
grading:        Gamma = sigma_3, the model's declared elliptic grading —
                sense (a) of the four-way homonym under the section-1
                crosswalk. HOMONYM-AMBIGUOUS against (b) observed 4d Weyl
                (W6, untouched), (c) internal Cl^0/omega_10 (supplied
                multiplicity, untouched), (d) base-Lorentz label; the whole
                point of this artifact is that these are typed apart and the
                wall grading G(phi) is NONE of them — it is the
                quarter-turned mass direction
action_owner:   repository-construction (the operator class, Krein test and
                circle are the repository's; the one source-typed input is
                the phi = 0 direction of SC-CHI-02, register:940)
target:         which of the four gradings a wall-hosted mode can carry, as
                a function of the mass direction
                MAP-TYPE=not-a-map (a grading/charge adjudication on a
                family, not a map between carriers)
```

```gu-typed-objects
result:         The W3 needs/provides chain: canon count lives on the
                ambient Gamma grading in its cross-Krein (odd-q)
                realization; the wall leg composes exactly; the single
                missing arrow is the sigma_2-type (Gamma-odd, Krein-
                breaking) direction supply on the physical carrier; the
                transport route to the bridge is closed exactly; handoff to
                W6 at LA1
carrier:        the cited canon rows, register verbatim fields, LD-A/LD-B
                measured objects and RW-1 bill items as literal pinned text
                LAYER=source-print CHIRALITY=N/A
pairing:        NONE
# A chain adjudication over pinned text and model computations: no bilinear
# form is involved in this result and none is claimed.  Bare token per the
# FX-2 gate's parser; gloss on these comment lines (LD-A's relay: an
# indented continuation line would be read as part of the value).
real_structure: N/A
grading:        N/A — the four senses this chain adjudicates are typed in
                section 1; no bare cross-sense token is used
action_owner:   repository-construction (the chain and its composition
                verdict are GB-1's; every consumed sentence is pinned to its
                owner)
target:         RW-1 bill item W3 (rw1:276-286), priced not killed
                MAP-TYPE=not-a-map (a composition/obstruction adjudication,
                not a map)
```

---

## 11. Claim ceiling, and what this artifact is not

- **No claim status moves. No canon row moves. No register, ledger, sidecar
  or registry edit.** The generation count stays OPEN; SG4 stays the
  decider; bit 2 stays the selector, OPEN; the wall route still RIDES SG4.
- **This artifact does not derive 3, and does not derive 1.** Its ceiling is
  a grading adjudication plus the pricing of one arrow. Even the full chain
  with link D supplied delivers hosting (|winding| = 1 generic, rung-2 null
  inherited), multiplicity SUPPLIED, CC-05 subtractive fence intact.
- **The comparator binds the model.** Every §2 identity is exact IN THE
  MODEL; none is a statement about the true RS `Y14` bundle or the (9,5)
  carrier; the physical-carrier gapping-direction geometry is named open
  (§6.3) and inherited by M5.
- **No kill.** The one claim this arc was licensed to kill (W3's
  suppliability, rw1:824-826) is measured suppliable-in-principle; the kill
  branch is priced and closed for this arc.
- **W6 is not advanced.** §4 is a boundary statement, not a down payment.

---

## 12. POSTFLIGHT — six lenses, after the work

- **P1 — Did any lens change a verdict?** Yes, two. L6 (claim-targeting)
  changed the target_claim itself before any computation (D1: the mount's W3
  phrase is not RW-1's). L3 (index/transport) forced the fractional-charge
  reading of the circle's interior — the first draft of §2.2 had "the wall
  carries partial charge", which is exactly the over-claim the ruler-tilt
  finding forbids; the shipped wording types the interior as
  non-eigenstate/non-count.
- **P2 — Is any verdict resting on a single receipt?** DOOR and CIRCLE rest
  on closed-form identities (multiple independent checks each). The thinnest
  verdict is COUNT's ambient leg, which leans on LD-B's numerical sweep
  (eigvalsh at 1e-8, LD-B's own declared seam); mitigated by LD-B's
  three-outcome discrimination and by the model realizing the same structure
  exactly (§2.3, §2.5). If LD-B's sweep were ever overturned, COUNT's
  realization clause — not the canon pins — would need re-derivation.
- **P3 — What did NOT move?** SG4; bit 2 (OPEN); the rung-2 null; RW-1's six
  verdicts and its bill (W3 re-priced, not moved as a row — the artifact
  edits nothing); LD-A's cards; LD-B's cards; the IMPOSTER-LABEL-AB
  settlement; SIGNATURE-AMBIENT; every canon row.
- **P4 — Where would a hostile re-runner disagree?** (i) The sign/orientation
  conventions of the circle (which pole is -1 vs +1) — convention-dependent,
  and the iff is convention-free; (ii) whether "the count lives on N1" over-
  reads CANON.md:136's vocabulary — answered by pinning the count object
  itself (instrument:18) rather than paraphrase; (iii) whether the
  commuting-K contrast is a fair model of (14,0) — it models exactly the
  `K = I (x) chi` identification LD-B computed there, and claims nothing
  more.
- **P5 — Regression check against the standing corrected facts.** Four
  layers carried (§1 table types every node's layer); chirality
  VEV-conditional and SG4 bit 2 OPEN (CC-06 quoted, never assumed);
  contraction-not-KK (LA1 typed as contraction; no KK mode-split appears);
  no-GUT (no unification chain appears); 2+1 subtractive (CC-05 quoted and
  applied at the only multiplicity statement); 128 as obligation (CC-08
  quoted; no defect framing). "Krein", "Gamma-charge": zero source
  attribution — fenced as repository vocabulary in the routing block.
- **P6 — Instrument honesty.** The probe's planted negative (pins), planted
  wrong-chirality candidate (residual flagger), and three planted positives
  (absence scans) all fire on the live run; the selftest's 9 machinery
  mutations are each caught by their targeted checks with the clean baseline
  verified first and re-verified after; every LEG 2/3 fact is symbolic so no
  tolerance exists to absorb a plant.

---

## The blunt paragraph: which direction the pressure ran

The comfortable endpoint for this arc was a discharge: W3 was named the
sharpest item, the two walls were already known unitarily equivalent, and the
tempting write-up was "the unitary IS the bridge — W3 closes." The
computation ran the other way and closed that route exactly: the unitary is
a Krein isometry that drags the grading with the wall, the relative angle is
invariant, and no transport ever makes the source-shaped operator host a
canon-graded charge — the bridge W3 asked for, read as a transport, is
impossible, and proving that impossibility is half of this artifact's
content. What survives is smaller and sharper than a discharge: the whole
four-way adjudication compresses to one exact function on one circle, the
doorway and the grading fuse at its poles, and everything W3 still owes the
program is a single direction-supply arrow with named holders — an arrow the
source neither writes nor forbids. I flag plainly what I could not do: the
model has one Krein-only direction by fiat of a 2x2 fiber, and whether the
physical carrier's zero-order geometry offers such a direction at all is the
first real computation the holders of link D must run; if it comes back
empty, W3 dies there, at one arrow, exactly at the rank RW-1 priced.
