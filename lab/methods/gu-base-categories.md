---
title: "GU base categories: the three context categories the repository already uses"
status: active_reference
doc_type: typed_object_reference
created: 2026-08-17
work_item: CT-1
audit: process_gates/typed_carrier_declaration_audit.py
probe: tests/channel-swings/joe_directed_ct1_base_categories.py
design_record: lab/active-research/joe-directed/ct-hardening/ct1-base-categories-2026-08-17.md
---

# GU base categories — Layer, Grant, Carrier: objects and arrows, once

**What this file is.** The canonical statement of the three context categories
this repository already uses in prose everywhere and had written down nowhere:
the **Source-Layer category** (the four layers of the source construction and
the maps between them), the **Grant poset** (the assumption sets ledger rows
advance under, ordered by inclusion, with the never-launder law), and the
**Carrier category** (the typed-carrier vocabulary the FX-2 gate enforces,
with the MAP-TYPE arrow labels and the registered homonyms as non-objects).
Every object and every arrow carries a receipt — the artifact and locus that
established it. Zero objects are coined here (the FX-3 rule: consolidate,
never rival). This file types what exists; it decides nothing.

**What this file is not.** Not a physics result, not a claim movement, not a
modeling project. The categories are grammar: if material ever demands a
thirteenth object in any category, that is a finding about the theory to be
reported, not a schema extension to be performed silently. Produced under a
directed brief (CT-1); not chat-ratified, and says so. Where two artifacts
type one object differently, §4 records the disagreement with both citations;
adjudication belongs to the channels that own the objects.

**Machine surface.** The three object/arrow tables below parse mechanically
(fixed column schemas, stated in §0). The fenced `gu-token-codomain` block in
§3.4 is the codomain the typed-carrier gate cross-checks its `LAYER=` and
`MAP-TYPE=` token constants against on every run, so the gate and this
reference cannot drift apart silently. Probe:
`tests/channel-swings/joe_directed_ct1_base_categories.py`.

---

## 0. How to read (and parse) the tables

Object rows (IDs `L*`, `G*`, `C*`), marker rows (`M*`) and Carrier
arrow-label rows (`CA*`) have exactly five cells:
`| <ID> | <name> | <role> | <statement> | <receipts> |`. Composable-arrow
rows (`LA*`, `GA*`) have exactly six cells:
`| <ID> | <arrow> | <dom -> cod> | <type> | <injectivity/conditionality> |
<receipts> |`. Non-arrow rows (`N*`) and disagreement rows (`D*`) have four
cells. Roles are `object`, `arrow-class` (a MAP-TYPE arrow label),
`declared-unknown-marker`, `not-applicable-marker`, `non-arrow-declaration`,
or `bucket` (a presentation class, not a single object). **The <= 12 budget
counts rows with role `object` only**; markers are legal utterances that name
no object (the CN-2 principle: declared ambiguity is compliance, and an
UNTYPED token is exactly the honest statement that no object was named).
Receipts are repository paths, semicolon-separated, optionally with `:line`
or section anchors. The probe resolves every path.

---

## 1. The Source-Layer category **L**

The four layers of the source construction. The enumeration is ST-1's
type/layer discipline, verbatim: *"four layers (declared total / pullback /
± package / observed-VEV-conditional), and every clause below must name its
layer"* — and the independent review's standing correction that these are
*"different layers, not competing quotations"* (IV-20260815 §2, §3.3).
CR-B §9 states the source's own triple declaration: *"The source declares all
three layers — the non-chiral total, one Weyl-pullback effective generation,
and the split package — and conditions the split on a VEV mechanism"*; the
conditional phase that mechanism selects is the fourth layer.

### 1.1 Objects (4)

| ID | object | role | statement | receipts |
|---|---|---|---|---|
| L1 | declared-total | object | The unsubscripted four-corner arena: `Omega^0 (+) Omega^1` valued in unsubscripted `S` — the full 128-complex Dirac bundle — printed as four graded corners (`nu±`, `zeta±`; classes 3,1,1,3), no reality condition or chirality projection imposed at the declaration locus; the total theory is explicitly non-chiral | `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §4.1; `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` (eq 9.16, `S` unsubscripted); `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` (p.51 corners, eq 11.6) |
| L2 | pullback | object | The Weyl-pullback / effective-generation layer: one effective SM generation described as the pullback of a properly understood Weyl spinor from `Met(X)` to `X^4` — a reduced 4D description, not the total declaration | `lab/sources/source-claim-register.yaml` `SC-GEN-55` (toe-2025 01:29:19; UCSD twin 00:46:40); `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` (IV-20260815 caution block) |
| L3 | pm-package | object | The opposite-half package `Omega^0(S+) (+) Omega^1(S-)`: the source's only explicit spoken chirality declaration, assigned to its three-generation claim; one of exactly two Z/4 class-homogeneous halves of the four corners (`W_+ = nu_+ (+) zeta_-`) | `lab/sources/source-claim-register.yaml` `SC-GEN-56` (ucsd-seminar-2025 00:32:46); `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §4.1-4.2; `lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` §3 |
| L4 | VEV-observed | object | The post-decoupling chiral phase: the non-chiral total *"splits at the emergent level into two separate chiral theories"* (`SC-CHI-01`, p.52), conditioned in the same passage on the `varpi` VEV hedge; phase membership is SG4 bit 2 (chiral/unbroken vs massive/super-Higgs) | `lab/sources/source-claim-register.yaml` `SC-CHI-01` (:909, p.52 eq 11.6); `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` :137 (the hedge); `lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` §5 V1; `canon/gu-forces-field-space-declaration-RESULTS.md` (SG4 bit 2) |

### 1.2 Arrows (identities, three generators, one composite)

Identities `id_L1..id_L4` exist and are not tabulated. Composition is as
recorded below; no other composite is asserted anywhere in the corpus.

| ID | arrow | dom -> cod | type | injectivity / conditionality | receipts |
|---|---|---|---|---|---|
| LA1 | observation pullback `s^*` | L1 -> L2 | contraction | **NOT injective** (kernel is the section-dependent 10-plane, VZ-4 [A4]); surjective onto the 4D one-form content; unconditional (exists for every section) | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` §2 [A2]-[A4], §3 [B7]; `lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md` §2 E1-E3; `lab/methods/source-native-comparator-routing.md` (withdrawn-clause CAUTION: WG-B06, contraction not projection); `canon/no-go-class-relative-map.md` :401 (CORRECTION IV-20260815 / VZ4-01) |
| LA2 | package inclusion | L3 -> L1 | inclusion | Injective (a subobject); **no declared retraction** — see non-arrow N1 | `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §4.1 (two class-homogeneous halves); `lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` §3 (`W_+ = nu_+ (+) zeta_-`) |
| LA3 | decoupling | L1 -> L4 | quotient | **VEV-conditional**: exists only under the `SC-CHI-01` hedge / SG4 bit 2 grant (Grant-poset node G6) — and the hedge's decoupling holds AT small `varpi`, so the arrow is PRESENT in the `varpi -> 0` (decreased-VEV, bit-2 CHIRAL) phase and ABSENT once a VEV pulls the `varpi` sub-fields significantly above zero (bit-2 MASSIVE) [DIRECTION CORRECTED 2026-08-17 by B1P-1, register item `CT1-LA3-WORDING`: the prior wording read "in the `varpi -> 0` phase the arrow is absent", which inverts the hedge it cites]. Not injective as declared: sectors below the dashed line are dark, not deleted | `lab/sources/source-claim-register.yaml` `SC-CHI-01`; `lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` §5 V1; `lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md` §1 item 6 |
| LA4 | effective-Weyl description = LA1 after LA2 | L3 -> L2 | contraction | Composite of LA2 then LA1; the source's own effective-generation sentence lives on this composite (pull back the package/half) | `lab/sources/source-claim-register.yaml` `SC-GEN-55`, `SC-GEN-56` (both are pullback sentences); `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §9 |

The MAP-TYPE tokens in the `type` column are the Carrier-category arrow
labels of §3.3; `quotient` on LA3 types the source's *"splits ... into two
separate chiral theories"* sentence as a partition-into-sectors at the
emergent level, per `SC-CHI-01` — it is a typing of the declared split, not a
constructed BV/BRST quotient (none exists in the repository; IV-20260815
§3.2).

### 1.3 Named non-arrows (declared absences, with receipts)

| ID | absent arrow | why it is not in the category | receipts |
|---|---|---|---|
| N1 | half-selection L1 -> L3 | No dynamical projection or decoupling selecting a half from the four corners is constructed; the selector is SG4 bit 2 and the unbuilt action. Reading eq (9.16)'s unsubscripted `S` as a half silently performs this non-existent arrow (the `S-HALF-SAME` trap is this error's worst case) | `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §4 ("does not construct the dynamical projection or decoupling that would select it"); `lab/active-research/joe-directed/README.md` (CN-2 S-TYPING block) |
| N2 | inverse observation L2 -> L1 | `s^*(R^14D)` is the whole 4D one-form bundle, so a 4D configuration neither determines nor is determined by a 14D one; the identification "the 4D sector is the observed image of the 14D sector" is unavailable in any gauge (open residual REDUCTION-FIDELITY) | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` frontmatter `residual_declared` + §3 [B8] |
| N3 | operative-half assignment L4 -> L3 | Which source-attested half (or the total) is operative after the still-unbuilt connection/VEV selection is open; the split's realization *"remains SG4 bit 2 and is not constructed"* | `lab/active-research/joe-directed/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md` §3.3; `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` frontmatter verdict |

### 1.4 What the non-injectivity forbids (the X-vs-f(X) confusion class)

LA1 is a **contraction, not a projection** (`WG-B06`; VZ-4 V3b: `s^* = P_H`
iff `d_mu g_ab = 0`), and it is **not injective on the content it transports**
(VZ-4 [A4], [B7]-[B8]). Therefore, for any content `X` at L1:

- `X` and `s^*(X)` are different objects at different layers; properties of
  one may not be credited to the other. The dated instances of this error
  class: the KK-scalar corollary V3c (killed in every gauge, VZ-4), the
  withdrawn *"vertical components become 4D scalars"* clause inside a
  mandatory method boundary (`lab/methods/source-native-comparator-routing.md`
  CAUTION), and the `GEOMETER-VS-PHYSICS-OBJECTS.md` Higgs/VEV cell clause
  (WITHDRAWN 2026-08-15).
- The **one unforgivable regression** (ST-1 Lens 4): crediting the total
  theory (L1) with chirality, or the package (L3) with an unconditional
  spectrum. Chirality is L4-conditional (LA3); the spectrum is
  VEV-conditional (ST-1 §5 V1/V2).
- LA2's injectivity does not license its inverse: naming the package does not
  select it (non-arrow N1).

---

## 2. The Grant poset **G**

Objects are **assumption sets as they actually occur in
`lab/process/conditional-physics-ledger-v0.259.json`** (87 row records = 84
active + 3 superseded; the families below are enumerated from the live rows).
A row *occupies* a node; it is not itself an object. A row carrying several
conditions occupies the union of their sets (LT-SM8 sits at G5 ∪ G7). Order
is **inclusion of assumption sets**: `S <= T iff S is a superset of T`, drawn
with the empty set at the top — fewer assumptions is higher, and "moving to
the top" means becoming unconditional.

### 2.1 Objects (9)

| ID | object | role | statement | receipts |
|---|---|---|---|---|
| G0 | empty set (unconditional) | object | `reason_kind: DERIVED` — no grant carried; 15 active rows (RA-A7, RA-B7, RA-B8, RA-B9, RA-C1, RA-D3, AC-A4, AC-A6, ...) | `lab/process/conditional-physics-ledger-v0.259.json` rows with `DERIVED`; taxonomy `verdict_kinds.SAME` |
| G1 | {GRANT-ACA1-C1} | object | The declared grant: draft-literal Sec 9.3 full-`S` content, branch C1, non-chiral in every form slot, `x = 0` in the signed-multiplicity lattice; *"the grant is declared, not derived"*. Carried by AC-A1; AC-A2/AC-A3 inherit it through AC-A1 (`distance: "none after AC-A1"`) | `lab/process/conditional-physics-ledger-v0.259.json` rows AC-A1/AC-A2/AC-A3 evidence; `conditions_opened_note` |
| G2 | {SELECTED: embedding} | object | The declared-selection conditional on the representation axis: `distance: "none after the embedding is selected"`; rows RA-B1..RA-B5; `revival_trigger: "a different selected embedding"` | `lab/process/conditional-physics-ledger-v0.259.json` rows RA-B1..RA-B5 |
| G3 | {SELECTED: chiral 16 shadow} | object | The declared-selection conditional on the anomaly axis: `distance: "none after the chiral 16 shadow is selected"`; rows AC-D1..AC-D5; `revival_trigger: "a physical carrier not equal to complete 16s"` **(v0.259 datum, preserved: v0.259 is immutable and still carries this string. Ledger v0.263 replaced it on AC-D1..AC-D5 with each row's own recorded anomaly functional, because the quoted trigger is LA-9 mode NR — it fires without moving the row. The G3 node is unchanged: it is still defined by exactly these five rows.)** | `lab/process/conditional-physics-ledger-v0.259.json` rows AC-D1..AC-D5 |
| G4 | {SELECTED: stabilizer} | object | The declared-selection conditional `distance: "none after the stabilizer is selected"`; row RA-A3 | `lab/process/conditional-physics-ledger-v0.259.json` row RA-A3 |
| G5 | {INHERITANCE_BRIDGE} | object | The typed named condition: *"The pairing on the BV/BRST physical quotient descends from the fibre trace form, so its definiteness is controlled by the fibre signature"* — established for `Lambda^1 (x) ad P` free-level by BD-D, NOT established for the RS / ker-Gamma carrier or the interacting level; carries its own rule: *"This re-typing advances carrying this condition or it does not advance"* | `lab/process/conditional-physics-ledger-v0.259.json` LT-SM8 `named_condition`; RA-D4 annotation (n_kappa = 0 priced "under condition INHERITANCE_BRIDGE only") |
| G6 | {SC-CHI-01 VEV if} | object | The source-conditional family: the source's own hedge — chirality/decoupling holds *"when there is no vacuum expectation value pulling the various sub-fields of"* `varpi` — bound by ST-1 to SG4 bit 2. In v0.259 this set occurs on the DEMAND side: NEEDS rows blocked on the vacuum/phase selection (LT-GR2d, RA-G3, AC-F1) | `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` :137; `lab/sources/source-claim-register.yaml` `SC-CHI-01` :922 note; `lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` §5 V1; `lab/process/conditional-physics-ledger-v0.259.json` rows LT-GR2d, RA-G3, AC-F1 |
| G7 | {HYP-TW-COHERENCE-01 antecedent} | object | The ledger's own conditional-mechanism hypothesis (status `..._NOT_A_PHYSICS_RESULT`), attached to LT-SM8: *"If an action-owned coupled BV/detour complex absorbs that current, factors through the GU operator, admits the actual endpoint and a positive Lorentzian physical pairing, then its physical cohomology may represent superposition"* | `lab/process/conditional-physics-ledger-v0.259.json` `conditional_hypotheses[0]` |
| G8 | in-row stated conditional | bucket | DERIVED_CONDITIONAL rows whose condition is stated in-row with no shared name; each such row's actual assumption set is its own `distance` text. Sole current member: RA-F2 (the observed-H640 W/mirror conditional) | `lab/process/conditional-physics-ledger-v0.259.json` row RA-F2 |

Counted objects: G0-G7 (8; G8 is a bucket, role-marked, not a single set).
NEEDS-side occupancy is polarity, not position: a NEEDS row at a node demands
the set; a DERIVED_CONDITIONAL row at the same node advances under it
(AC-A1's migration below is exactly the polarity flip at fixed node G1).

**G6 addendum — the bit-1 price of a bit-2 CHIRAL grant (added 2026-08-17 by
B1P-1, register item `BIT1-PRICE-PRINT`; annotation only — no object is
coined, no row moves, no corner is selected).** G6 is a *phase* node (SG4 bit
2), and the surfaces that route to it present its CHIRAL resolution as free on
the other SG4 bit. It is not. Recomputed here from the SHA-pinned
predeclaration (`tests/gu-forces/leg_a_forcing_enumeration.py`, the frozen
`VERTEX` map at :68-74; SHA-256 `3043d29e...80197`, byte-identical, unedited):
of the four corners of the (invariance, phase) square the **consistent support
is THREE, not four** — `(ABSENT, MASSIVE) -> B (-38)`, `(PRESENT, CHIRAL) -> A
(-42)`, `(PRESENT, MASSIVE) -> CTRL40 (-40)` — because `(ABSENT, CHIRAL)` is
carried as `INCONSISTENT` ("ungauged massless CHARGED spin-3/2 -> GP bites, no
SUSY"). A three-element support inside a 2x2 is not a product set, so the two
bits are **correlated given consistency**: `ABSENT => MASSIVE`, and `CHIRAL =>
PRESENT => carrier A`, the only consistent chiral corner. Both converses FAIL
(`PRESENT` admits CHIRAL and MASSIVE; `MASSIVE` admits ABSENT and PRESENT), so
this is a one-way price, not an equivalence, and it forces nothing in the
ABSENT/MASSIVE direction. **The price:** granting bit 2 = CHIRAL at G6 also
grants bit 1 = PRESENT and lands on carrier A — which collides with the
standing B-tilt, whose own source string is *"A at the chiral point, B at the
massive point"*. **This is banked, not new, and it is not a verdict:** canon
recorded the same collision in Grisaru-Pendleton vocabulary on 2026-07-10
(`canon/escape-corners-campaign-RESULTS.md` :59-64 — *"'Too massive' and
'decreased VEV' are opposing demands on one dial, reconcilable only by an
unstated hierarchy. At the chiral point GU's phenomenology commits to, ... GP's
hypotheses populate, and its conclusion ... collides with 'We will never find
space time Susie' -- UNLESS the demanded SUSY is the upstairs one"*), and the
leg priced its firing conditions at
`tests/escape-corners/lega1_flipped_chiral_adjudication.md` :257 — *"corner (a)
fires only if GU's physical vacuum is taken at the chiral point AND the mass
map is uniform across the fermionic extension"*. The **escape is named and
open**: the second conjunct — a NON-uniform mass map across the fermionic
extension — is exactly what the source's own *"sub-fields"* plural (p.52) and
SN-1's separately-scaled components leave available. So the correlation is
conditional structure about a frozen label map, not a claim about which corner
GU or nature occupies: SG4 remains the sole decider, the residual remains
2-bit, the B-tilt is unmoved. What this addendum adds is only that the two bits
are **not independently grantable**, and that a router handing bit 2 to a lane
as "the open phase bit" is handing bit 1 with it unless the mass map is
non-uniform. Dig and recomputation:
`lab/active-research/joe-directed/lens-digs/ldc-vev-selector-adjudication-2026-08-17.md`
§7; `lab/active-research/joe-directed/bit1-price/b1p1-three-corner-support-prices-the-chiral-grant-2026-08-17.md`.

### 2.2 Order and recorded arrows

| ID | arrow / relation | dom -> cod | type | injectivity / conditionality | receipts |
|---|---|---|---|---|---|
| GA1 | inclusion order | Gi -> G0 (each i >= 1) | inclusion | Every non-empty assumption set contains the empty set; the order relation is not a licence to move — see the law | order by definition; `lab/process/conditional-physics-ledger-v0.259.json` |
| GA2 | grant inheritance | AC-A2/AC-A3 -> AC-A1 (within G1) | restriction | In-ledger recorded dependence: *"the row is true given AC-A1 and not conversely; rank witness satisfies this row and violates AC-A1"* | `lab/process/conditional-physics-ledger-v0.259.json` AC-A2/AC-A3 evidence |
| GA3 | recorded migration (the ONLY movement mechanism) | row position -> row position | not-a-map | Movement of a ROW between nodes is not a functor and not free: it exists only as a dated `migrations[]` record (row_id, old, new, scope, evidence, meaning_changed) minted by the canonical owner. Exemplar: AC-A1 0.258 -> 0.259, `NEEDS/MISSING_CONSTRUCTION -> SAME/DERIVED_CONDITIONAL` *"carrying GRANT-ACA1-C1 as the named condition; ... not laundered to DERIVED"* | `lab/process/conditional-physics-ledger-v0.259.json` `migrations` (258 records at v0.259); `lab/active-research/joe-directed/integration-mint/im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md` |

### 2.3 The never-launder law (the poset law)

**A row's position may move only along a recorded migration arrow, never
silently toward the top.** Concretely, at v0.259:

1. Dropping any assumption (moving toward G0) requires a dated
   `migrations[]` entry with evidence; `DERIVED_CONDITIONAL -> DERIVED`
   occurs nowhere (IM-1 title; frontmatter `rows_laundered: []`; the v0.259
   meter reads *"zero launders"*).
2. The always-legal direction is toward MORE assumptions / more indebted
   kinds: *"Where two honest readings disagree, the channel's standing rule
   takes the more indebted one and names the upgrade gate"* (IM-1
   adjudication A, ground 2); laundering *"never takes"* that direction.
3. **Enforcement receipt (the mint's launder control):** IM-1's probe plants
   a LAUNDER control — re-typing minted AC-A1 unconditional MUST fail the
   validator — and pins the grep-level check *"zero rows carry `DERIVED`
   whose base carried `DERIVED_CONDITIONAL`"* as permanent
   (`lab/active-research/joe-directed/integration-mint/im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md`
   §Non-laundering, §certificate row;
   `tests/channel-swings/joe_directed_im1_two_movers_four_debts_and_three_adjudications.py`).
4. New condition kinds may not be forced into existing ones: the ledger's own
   taxonomy rule is `NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN`
   (`lab/process/conditional-physics-ledger-v0.259.json` `taxonomy`).

No recorded arrow relates G3 (chiral-16-shadow selection) to G6 (the VEV
phase): the two are adjacent in prose (CR-B §9, ST-1 §5) but unidentified in
the ledger, and this file does not identify them (§4 D4).

### 2.4 Discharge is order-sensitive unless a recorded migration proves otherwise

**ORDER-SENSITIVE (typed 2026-08-24).** The Grant poset orders assumption
sets; it does not make the effect of discharging them monotone or commuting.
LA-5 supplies the concrete witness: discharging `AC-A1` is what kills
`AC-F3`, so the grant-to-row map is explicitly *not monotone* and the order of
discharge can change a downstream disposition. Accordingly, no Layer arrow —
including grant-indexed LA3 at G6 — is presumed to commute with grant
discharge. Commutation exists only when a dated owner migration records the
square and its evidence; otherwise order sensitivity remains explicit.

This statement does not identify G3 with G6, construct a functor `L -> G`, or
move either row. It propagates the already-recorded LA-5 witness into the
reference whose readers would otherwise infer order-independence from the
poset alone. Receipt:
`lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md`
§7 postflight (`AC-A1`/`AC-F3`), independently surfaced by
`lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md`
card 5.

---

## 3. The Carrier category **C**

The typed-carrier vocabulary the FX-2 gate
(`process_gates/typed_carrier_declaration_audit.py`) enforces on
`gu-typed-objects` blocks, stated once as objects and arrow labels. Design
record: `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md`.
Prior typed-object surfaces this consolidates with, rather than rivals:
`GEOMETER-VS-PHYSICS-OBJECTS.md` (the standard-vs-native fork table and the
identify-which-object rule) and the six-axis template's Layer-0
semantic-alignment precondition
(`lab/specifications/six-axis/six-axis-template.md`).

**Honesty about mathematical status.** C is a category presentation in the
schema/olog sense: its objects are the closed vocabulary's inhabitants, and
its "arrows" are the MAP-TYPE **arrow labels** — each classifies declared
maps whose actual domain and codomain are supplied per use by the declaring
`gu-typed-objects` block. Composition of declared maps is tracked by the
declaring artifacts (and the needs-provides lane), not here. Claiming more
category structure than that would be false precision.

### 3.1 Objects (11)

| ID | object | role | statement | receipts |
|---|---|---|---|---|
| C1 | ambient | object | LAYER stratum: the ambient geometry on `Y = Met(X)` (14D arena content) | `process_gates/typed_carrier_declaration_audit.py` LAYER_TOKENS; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §1; SA-1 layer split (`lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md`) |
| C2 | observed | object | LAYER stratum: post-observation 4D content (pulled back along the section) | same LAYER_TOKENS receipt; `lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md` |
| C3 | source-print | object | LAYER stratum: content as printed by the source documents themselves (extraction layer, e.g. the eq (9.16) cells) | same LAYER_TOKENS receipt; `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` |
| C4 | toy | object | LAYER stratum: toy/model-grade content, explicitly not the physical carrier | same LAYER_TOKENS receipt; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §1 |
| C5 | S-FULL-DIRAC | object | CHIRALITY reading: `S` is the full 128-complex Dirac bundle, both halves — what eq (9.16) literally declares | `lab/active-research/joe-directed/README.md` CN-2 S-TYPING block; `lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md` |
| C6 | S-HALF-OPPOSITE | object | CHIRALITY reading: the two slots carry opposite halves, `Omega^0(S+) + Omega^1(S-)` — the source's only explicit spoken chirality declaration (L3 of the Layer category is its package) | same CN-2 receipts; `lab/sources/source-claim-register.yaml` `SC-GEN-56` |
| C7 | S-HALF-SAME | object | CHIRALITY reading: both slots the same half. Stated by NEITHER primary and refuted in canon (escape-corners A2, REFUTED-AS-FILED) — kept in the vocabulary precisely so a document that silently selects it can be SAID to have done so | `lab/active-research/joe-directed/README.md` CN-2 S-TYPING block; `canon/escape-corners-campaign-RESULTS.md` |
| C8 | so(1,3)_endo | object | Homonym-subscripted carrier: the endogenous/diagonal six-dimensional Lorentz subalgebra of `so(7,7)` induced by frame rotations of `X`; intersects `so(1,3)_H` in zero; gives 0 on the same `k` where `so(1,3)_H` gives 21 | `lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md` [F05]-[F07], [E09]; `lab/process/homonym-register.yaml` token `so(1,3)` |
| C9 | so(1,3)_H | object | Homonym-subscripted carrier: the block Lorentz subalgebra named by the manuscript's observation chain `Spin(7,7) -> Spin(1,3) x Spin(6,4)`; differs from `so(1,3)_endo` by an internal rotation `delta(X) in so(6,4)` inside the declared gauge group | same SA-1 receipts (:348, :384-:389); `lab/process/homonym-register.yaml` token `so(1,3)` |
| C10 | ad(P_H)_{u(64,64)} | object | Homonym-subscripted carrier: the source's `ad(P_H)` — adjoint of `P_H = P_Spin(C) x_rho U(64,64)`, fibre `u(64,64)`, dim 16384 | `lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md` §2.3 table; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §6 block 1 |
| C11 | Lambda^2 of the 14-dim chimeric carrier (MD-1's ad-leg sense of the shared token) | object | The OTHER referent of the same written token: `Lambda^2` of the 14-dimensional chimeric carrier, i.e. `so(7,7)`/`so(9,5)`, dim 91, with the fork living in its internal `so(6,4)` block (dim 45). SA-1 §2.3 types the two senses in a table; no standard subscript is coined here — writing the referent out, as SA-1 does, is the current disambiguation | `lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md` §2.3 (:315); `lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md` |

### 3.2 Markers (legal utterances that name no object)

| ID | token | role | statement | receipts |
|---|---|---|---|---|
| M1 | UNTYPED (LAYER slot and elsewhere) | declared-unknown-marker | Declared ambiguity is compliance: always legal, always counted, printed every run; it states that no object was named, honestly | `process_gates/typed_carrier_declaration_audit.py` (CN-2 principle, docstring); `lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md` |
| M2 | S-CHIRALITY-UNTYPED | declared-unknown-marker | The chirality slot's declared unknown (CN-2's fourth token) | same CN-2 receipts |
| M3 | N/A (chirality) | not-applicable-marker | Spinor-free carriers only; on a spinor carrier it is the unsubscripted-`S` defect wearing a compliance token and is red (`SPINOR-CHIRALITY-NA`) | `process_gates/typed_carrier_declaration_audit.py` validate_block |
| M4 | HOMONYM-AMBIGUOUS | declared-unknown-marker | The registered-homonym escape: counted in the ambiguity census like every declared unknown | `process_gates/typed_carrier_declaration_audit.py`; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §1 |

### 3.3 Arrow labels — the MAP-TYPE vocabulary (11 arrow classes + 2 non-arrow tokens)

| ID | arrow label | role | statement | receipts |
|---|---|---|---|---|
| CA1 | projection | arrow-class | Idempotent split onto a summand. Its razor use: the FALSE typing of the observation reduction — `s^* = P_H` iff `d_mu g_ab = 0` (VZ-4 V3b), the withdrawn clause's error class (FX-2 E4) | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` [A5]; `lab/methods/source-native-comparator-routing.md` CAUTION |
| CA2 | contraction | arrow-class | The corrected typing of observation pullback: `(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab` — the source's own Layer-0 correction WG-B06 | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` [A2]; `lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md` E2; `lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md` (WG-B06) |
| CA3 | inclusion | arrow-class | Subobject arrow; exemplars: the package inclusion (LA2), fibrewise subgroup inclusions — which *"do not themselves construct a global structure-group reduction"* | `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §4.1; `lab/active-research/joe-directed/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md` §2 |
| CA4 | restriction | arrow-class | Domain restriction; exemplar: V3a survives exactly as a statement about the horizontal subbundle `pi^*(T*X^4)` — a domain restriction, not a property of `s^*`; SA-1 block 2 target | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` §0, §6; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §6 block 2 |
| CA5 | pullback | arrow-class | Pullback along a map/section as a construction; the source's own verb for the effective generation and the package (`SC-GEN-55/56`). The same map `s^*` is a pullback by construction and a contraction as an operation — see §4 D3 | `lab/sources/source-claim-register.yaml` `SC-GEN-55`, `SC-GEN-56`; `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` |
| CA6 | pushforward | arrow-class | Vocabulary member by FX-2 (the dual construction); no live exemplar block in the corpus yet — stated, not implied | `process_gates/typed_carrier_declaration_audit.py` MAP_TOKENS; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §1 |
| CA7 | quotient | arrow-class | Passage to a quotient; exemplars: BD-D's ghost-number-zero symbol quotient (a comparator construction, IV-20260815 §3.2); the base-duality result "the quotient cures the base, not the fibre" | `lab/active-research/joe-directed/base-duality/bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md`; `lab/active-research/joe-directed/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md` §3.2 |
| CA8 | isomorphism | arrow-class | Invertible arrow; exemplar: `s^*` composed with the horizontal inclusion is the identity on `T*X^4` for EVERY section (VZ-4 [A3]; VZ-4 §6 calls it a canonical isomorphism; the integrated canon wording is "restricts canonically for every section") | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` §2 [A3], §6; `canon/no-go-class-relative-map.md` :401 (CORRECTION IV-20260815 / VZ4-01) |
| CA9 | homomorphism | arrow-class | Structure-preserving arrow; exemplar: SA-1 block 1 target (`P_H` as a Spin_0(1,3)-associated bundle via `r~_C`) | `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §6 block 1 |
| CA10 | intertwiner | arrow-class | Equivariant map between modules; exemplar: CR-B's antilinear intertwiners `B_eta`, solved for rather than assumed | `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §3.1 |
| CA11 | evaluation | arrow-class | Vocabulary member by FX-2 (evaluation/pairing-application arrow); no live exemplar block in the corpus yet — stated, not implied | `process_gates/typed_carrier_declaration_audit.py` MAP_TOKENS; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §1 |
| CA12 | not-a-map | non-arrow-declaration | The explicit statement that the target relation is NOT a map; exemplars: `Hom(Z/3, Z) = 0` blocks a direct additive identification (the generation-count fork); SCUR-1's own typed block uses it for an adjudication target | `GEOMETER-VS-PHYSICS-OBJECTS.md` generation-count row; `lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md` typed block |
| CA13 | UNTYPED (map type) | declared-unknown-marker | The arrow-slot declared unknown (counted in the census) | `process_gates/typed_carrier_declaration_audit.py` MAP_TOKENS |

Arrow-class count: CA1-CA11 (11); CA12 and CA13 are a declared non-arrow and
a declared unknown, in the token set but not arrow classes — the same role
split as the object markers.

### 3.4 The codomain block (machine surface; the gate cross-checks this)

The typed-carrier gate's `LAYER=` and `MAP-TYPE=` token constants must equal
these lines exactly (as sets, duplicates forbidden). The gate reds on drift,
in either direction.

```gu-token-codomain
layer-tokens: ambient observed source-print toy UNTYPED
map-type-tokens: projection contraction inclusion restriction pullback pushforward quotient isomorphism homomorphism intertwiner evaluation not-a-map UNTYPED
```

Two gate vocabularies are deliberately NOT wired here, because their
codomains are owned elsewhere, and naming that is part of the reference:
**CHIRALITY tokens** are CN-2's closed vocabulary, reused by the gate
verbatim — the codomain owner is
`lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md`
(this file lists the three reading-objects C5-C7 and the marker M2 but does
not re-own the token set). **OWNER tokens** (`action_owner`) are FX-2's own
vocabulary; the codomain owner is the FX-2 design record. A later CT stage
may wire either; doing it silently here would create rival ownership.

### 3.5 Non-objects: the registered homonyms

**A bare registered token fails to name an object.** The disambiguation
surface is `lab/process/homonym-register.yaml` (38 entries at 2026-08-16,
consolidating five prior surfaces; its own header forbids rival surfaces, so
this file points and does not duplicate). Load-bearing here:

- `so(1,3)` — registered homonym (two subalgebras intersecting in zero, C8
  vs C9); bare use inside a `gu-typed-objects` block is red
  (`HOMONYM-BARE`).
- `ad(P_H)` and `so(3,1)` — seeded in the gate's `HOMONYMS` constant, **not
  yet register entries**: a recorded gap, not a resolved one (§4 D1).
- "layer" — an UNREGISTERED near-collision flagged by this reference (§4
  D2); register candidacy is the homonym lane's call.

The marker `HOMONYM-AMBIGUOUS` (M4) is the legal declared-unknown for exactly
this class.

---

## 4. Recorded typing disagreements and gaps (not adjudicated here)

| ID | surfaces | what disagrees | citations |
|---|---|---|---|
| D1 | gate `HOMONYMS` constant vs homonym register | The gate seeds `so(1,3)`, `so(3,1)`, `ad(P_H)`; the register (38 entries) carries `so(1,3)` but has no `so(3,1)` or `ad(P_H)` entry. FX-2 declared the register "should supersede the gate's seeded constant" when it ships; it shipped the same day and the supersession has not been performed. Both surfaces are live; this file changes neither | `process_gates/typed_carrier_declaration_audit.py` HOMONYMS; `lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md` §1; `lab/process/homonym-register.yaml` |
| D2 | three senses of "layer" | (a) the gate's `LAYER=` stratum axis {ambient, observed, source-print, toy}; (b) the four source-construction layers of §1 (ST-1's vocabulary); (c) "Layer 0", the six-axis semantic-alignment precondition. Three different axes share one word; no register entry exists. This reference uses "Source-Layer category" for (b) and never uses bare "layer" across senses | `process_gates/typed_carrier_declaration_audit.py` LAYER_TOKENS; `lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` Lens 4; `lab/specifications/six-axis/six-axis-template.md` Layer 0 |
| D3 | MAP-TYPE of `s^*`: pullback vs contraction | The same map is typed `pullback` by the source's sentences (SC-GEN-55/56, and CA5) and `contraction` by the corrected operation typing (WG-B06, VZ-4, MD-1, and CA2). Reconciliation as VZ-4 states it: `s^*` is a pullback by construction whose action on components is a contraction; the FALSE member of the triple is `projection` (V3b). Blocks should type the operation (`contraction`) when the projection error is in scope, and may type the construction (`pullback`) otherwise; both remain in the closed vocabulary | `lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md` §0-§2; `lab/sources/source-claim-register.yaml` SC-GEN-55/56 |
| D4 | G3 vs G6 | "none after the chiral 16 shadow is selected" (AC-D rows) and the SC-CHI-01 VEV/phase condition are adjacent in prose (CR-B §9; ST-1 §5 binds the hedge to SG4 bit 2) but no ledger record identifies the two condition families. They are kept incomparable here | `lab/process/conditional-physics-ledger-v0.259.json` AC-D rows; `lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` §9 |

---

## 5. Corrected-fact guardrails (binding on every use of this file)

The five standing source-layer corrections most likely to be regressed by a
careless reading of these categories, each verified at its owner
(`lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md`
§1 is the ten-item register; items below quote it):

1. **Positivity polarity** — ambient Killing/Krein indefiniteness is
   source-attested; observed-quotient positivity is source-OPEN, **not
   disavowed** (IV-20260815 §3.1). Nothing in the Source-Layer category makes
   L4 a positivity claim.
2. **Different layers, not competing quotations** — the four L-objects
   coexist; quoting SC-GEN-55 against eq (9.16) (or vice versa) is a layer
   error, not a contradiction (IV-20260815 §2, §3.3; CR-B caution block).
3. **Contraction, not projection** — LA1's type; V3b/V3c and the withdrawn
   clause are the dated instances (VZ-4; `lab/methods/source-native-comparator-routing.md`
   CAUTION; `GEOMETER-VS-PHYSICS-OBJECTS.md` withdrawn cell).
4. **No GUT** — *"There is no grand unification. It's just a normal bundle in
   your ambient space."* (`papers/drafts/Transcript into the impossible.md`
   :125). The internal-symmetry content is normal-bundle structure; SO(10)
   comparator results bind their comparator only.
5. **2+1 subtractive** — *"three families, really two plus one. The third
   family is an imposter for representation theoretic reasons"* (drafts
   :119); the partition is forced and SUBTRACTIVE (`n_g -> n_g - 1`, HE-1),
   with `n_g` an input. No L-object or arrow may be read as an additive
   three-family derivation.

---

## 6. What this file does not supply

No physics claim, no verdict, no claim movement, no ledger or canon edit, no
registry edit, no new enforcement beyond the single codomain cross-check the
gate now performs against §3.4. It does not resolve SIGNATURE-AMBIENT, SG4,
SOLDERED-AD, REDUCTION-FIDELITY, or any fork; it does not identify G3 with
G6; it does not perform the D1 supersession; it does not register "layer" as
a homonym (the register is another lane's surface). The thirteenth-object
rule stands: additions to any category are findings to be reported to the
owning channels with receipts, not edits to be made silently here.
