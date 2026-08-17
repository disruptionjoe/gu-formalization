---
artifact_type: exploration
status: active_research
doc_type: stewardship_record
record_kind: needs_provides_composition_join
created: 2026-08-16
work_item: FX-1
channel: composition
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
row_change: none
registry_change: none
steering_effect: unchanged
canonical_effect: pending_integration
gate: process_gates/needs_provides_composition_audit.py
probe: tests/channel-swings/joe_directed_fx1_needs_provides_join.py
alias_table: lab/process/needs-provides-alias-table.json
diffs_against:
  - lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md (S1/S2 non-execution sweeps)
  - lab/process/path-dependencies.md (trap registry, not a join)
  - lab/process/layer0-fork-registry.yaml (fork list; consumed here as a NEED surface)
  - NEXT-STEPS.md (wave journal, newest-first)
  - conditional-physics-ledger next_work_queue (rank list over rows)
title: "FX-1: the needs/provides JOIN — 63 candidate pairs over the current
  corpus, every one typed; the SA-1 case is retro-detected by the join; the
  live yield is 3 un-composed compositions (wave-D's 126-placement machinery
  vs LT-SM5, the June v_PSB stabilizer gate vs RA-A6's own revival trigger,
  SC-A's chain adjudication vs BD-1's CI-X04 directive); baseline 0, ratchet
  down only; and a sibling agent's mid-pass write was caught by the gate
  within minutes"
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

**Declared doc type, and why.** This file declares `doc_type:
stewardship_record`, which the routing audit excludes from its derived scope
on the gate's own rationale: *"An index or a stewardship record does not
contain or border a comparator: it points at artifacts that do."* That is
exactly this file — it computes nothing physical; every pair below is a
pointer at two other artifacts. The notice and classification are carried
anyway, so the exclusion buys nothing it would not otherwise have
(precedent: AR-1, AR-2, `bd-reg-routing-backlog-disposition-2026-08-15.md`).
`INTERNAL_STRUCTURAL_ONLY` entered the routing vocabulary on 2026-08-16 for
exactly this genus (see the resolution note (b) inside
`process_gates/source_native_comparator_routing_audit.py`). The routing
registry is NOT edited by this pass — a stewardship record must not be
registered (the audit requires every registered path to be in derived scope),
so no registration is owed on commit either.

---

# FX-1 — join what artifacts DECLARE THEY NEED against what artifacts CLAIM TO SUPPLY

The costliest failure class here is measured, and it is not re-derivation. It
is **un-composed adjacency**: both halves of an answer present, never joined.

- **SA-1** (2026-08-16): the `SOLDERED-AD` selector was built **nine days**
  before the fork was declared open — `P_H` is by definition the associated
  bundle of the chimeric frame bundle
  (`k77-global-chimeric-spin-reduction-…-2026-08-05.md`: *"it builds (P_H)
  from the chimeric spinors"*) — while MD-1 (2026-08-14) named the settling
  gate and called it cheap. Nobody composed the two.
- **SC-A** (2026-08-15): the correct arrow-1 object `SU(3,2)` had been in ~20
  files since 2026-07-06 while three sites carried the group-theoretically
  impossible `Spin(3,2)` variant — one token apart.
- **BD-C** (2026-08-15): a 2026-08-09 source re-inspection recorded
  `metric variation | explicit through MET(X)`; six days later two independent
  routes (OT-1, LA-11) called that leg unsupplied.

Retrieval-before-work does not catch this class: the searches would have
succeeded had anyone thought to run them. What was missing is a mechanical
JOIN. This pass builds it (`process_gates/needs_provides_composition_audit.py`),
runs it over the existing corpus, and types every hit. **A hit is a candidate,
never a verdict; the gate auto-closes nothing.**

## 1. PREFLIGHT — six lenses, run inline

**Lens 1 — record linkage / entity resolution.** The classic failure is
fuzzy matching presented as coverage. Design consequence: the join is over
exact token equality in three declared shapes, plus an explicit alias table
where every entry cites the artifact pair that proved the synonymy. A planted
case-variant control (`Qorv_Z` vs `qorv_z`-style) asserts that un-aliased
notations do NOT join, so fuzz cannot creep in silently.

**Lens 2 — requirements traceability.** An RTM decays when requirements and
implementations are inventoried separately and nothing computes the trace.
This repository has four need surfaces that never meet the supply surface:
the ledger's `distance`/`revival_trigger` fields, the fork registry's open
rows, frontmatter `blocked_on`/horn declarations, and body need-statements.
Consequence: all four are NEED classes of one join, and the gate re-derives
the trace on every run rather than storing it.

**Lens 3 — build-system dependency resolution.** RPM/soname resolution works
because provides and requires are DECLARED in one vocabulary. Here the
vocabulary is emergent, so the join must measure its own key selectivity: a
key naming 18 provider files (`P_H`) resolves nothing by itself. Consequence:
the two-tier design — full pairs at ≤ 6 providers, WIDE rows above — with the
cap chosen so the documented cases stay ON the surface (both `P_H` and
`Met(X)` are over-cap, which is why Tier 2 exists at all).

**Lens 4 — information extraction.** Verb-anchored extraction cannot see
grammatical mood: *"build `Pi_RS^phys`"* (imperative) and *"only if a precise
functor … is supplied"* (conditional) both look like supply. Consequence: the
extractor stays exact and dumb, and the ADJUDICATION step is the mood filter
— two pairs below are kept UNTYPED as named receipts of exactly this limit.

**Lens 5 — audit design.** A finding needs criterion, observation,
disposition; a gate needs a ratchet that cannot be raised to go green.
Consequence: baseline = un-adjudicated pairs at introduction = **0** (every
pair found today is typed today); every pair prints every run; the structure
follows `process_gates/source_native_comparator_routing_audit.py`.

**Lens 6 — archival supersession (AR-1's lesson, inherited deliberately).**
AR-1 measured a 40% error rate on rows inherited from prior inventories and
0% on rows verified against a file fact. Consequence: every adjudication
below names a file fact, and my own first-pass typings were hostile-checked
the same way (§7: three of six draft fork typings were overturned).

## 2. RETRIEVAL — what already exists

Searched before building: no needs/provides index or join exists anywhere in
the tree (`needs-provides`, `provides index` and variants: zero hits). The
nearest relatives, each diffed, none a join:

| surface | what it is | why it is not this |
|---|---|---|
| AR-1 S1/S2 | named-probe non-existence; never-run admissions | detects NON-EXECUTION; FX-1 detects UN-COMPOSED ADJACENCY — the SA-1/BD-C failures involve work that WAS executed |
| `lab/process/path-dependencies.md` | why-a-check-exists trap registry | records composed lessons after the fact |
| `lab/process/layer0-fork-registry.yaml` | fork list | a NEED surface; consumed as input here |
| `NEXT-STEPS.md` | wave journal | narrative queue, no provides side |
| ledger `next_work_queue` | rank list over rows | ranks needs; never joins them to supply |

## 3. THE EXTRACTION RULE, and its measured coverage

**NEED sites** (all declared, all greppable): **LEDGER** — `distance` +
`revival_trigger` of non-superseded rows of the latest ledger; **FORK** —
open rows of the fork registry (an open fork is a declared need); **ART** —
first-party joe-directed artifacts (stewardship/overview doc_types and the
archaeology channel excluded as inventory genre, per AR-1's own exclusion):
frontmatter `blocked_on:`/`layer_open:`/`fork_declared` horns, plus body
lines with a need verb (*blocked on / owed / requires / missing / unbuilt /
unsupplied / not supplied*) AND ≥ 1 join key.

**PROVIDE sites**: any first-party corpus line with a non-negated provide
verb (*constructs / builds / built / supplies / establishes*) AND ≥ 1 join
key. The negation guard is load-bearing: *"it never builds X"* is an
admission, not supply, and a planted control asserts it.

**JOIN KEYS — three exact shapes, read inside backticks and bare** (the SA-1
provider writes `(P_H)` with no backticks): K1 underscore identifiers with a
capital (`P_H`, `E_act`, `Pi_RS^phys`); K2 callable/group forms (`SU(3,2)`,
`MET(X)`); K3 ALL-CAPS hyphenated names without digits (`SOLDERED-AD`).
Status vocabulary (`MISSING_CONSTRUCTION`), YAML field names, and
register/work-item IDs (`SC-GEO-07`, `LA-11` — they carry digits) are
excluded by shape or explicit stoplist, each exclusion pinned by a control.

**Aliases**: `lab/process/needs-provides-alias-table.json`, 3 entries, each
with byte-verified receipts — `MET(X)`≡`Met(X)` (BD-C case),
`SU(3,2)`≡`Spin(3,2)` (SC-A case, join-only equivalence — the two GROUPS are
distinct; the receipt is philological), `Pi_RS^phys`≡`Π_RS^phys` (measured
glyph split: 132 ASCII files vs 29 Greek, both in one file for one object).
**No alias without a receipt**; the gate re-verifies receipts every run.

**Measured coverage (exact, from the gate's own extraction):** corpus 3,877
markdown files. Need sites: **16** LEDGER rows of 82 non-superseded (66 rows'
distance/revival text contains no extractable key — that is the honest floor
of exact extraction over free text), **6** of 10 open FORK rows, **34** ART
files; **56** total. Provide lines: **2,886**; distinct provider keys:
**2,156**. Join: **35 Tier-1 pairs + 28 WIDE rows = 63 candidate pairs**;
**18** non-discriminating keys printed with counts every run.

**Recall against the three documented cases** (the only ground truth we
have): **A (SA-1/MD-1): RETRO-DETECTED** — the join emits
`ART:…md1…::P_H [18 providers]` with the 2026-08-05 chimeric construction in
the provider set; had the gate existed on 2026-08-14 the pair would have
printed as NEW-UNADJUDICATED. **C (SC-A): detected via the alias entry** —
`Spin(3,2)`-naming text joins `SU(3,2)` supply (RA-A6 and BD-1 pairs below).
**B (BD-C): the alias is pinned but the original need sentence sits BELOW the
extraction floor** — OT-1's operative line is literally "Neither is supplied."
— a bare sentence with no token on it. Exact extraction cannot see it, a
window does not help (the tokens two lines up are `Γ(Ad P)`-shaped, outside
the key classes), and pretending otherwise would be fuzzy matching in
disguise. Recall on documented cases: 2 of 3 mechanical, 1 of 3 only at the
alias/receipt level. Stated, not papered over.

## 4. THE YIELD — every pair, typed

Type tallies over all **63 candidate pairs** (full printed list: run the
gate; every pair prints every run):

| type | count | of which |
|---|---:|---|
| **LIVE_CANDIDATE** | **4** | 3 distinct compositions (Y_C/Y_K share a provider pair) |
| ALREADY_COMPOSED | 42 | incl. the retro-detected SA-1 case and the mid-pass FX-2 catch |
| UNTYPED | 17 | 2 mood-blindness receipts, 1 measured homonym, 4 live-sibling-channel rows, 10 wide-key rows |
| SUPERSEDED | 0 | none of the current 63 has a dead half (superseded ledger rows are excluded upstream) |

**UNADJUDICATED_BASELINE = 0.** Ratchet down only. Any new pair is red until
a reader types it — and that is not hypothetical: **the concurrent FX-2
agent's `fx2-typed-carrier-declaration-2026-08-16.md` landed mid-pass and the
gate caught it within minutes** (typed ALREADY_COMPOSED; it cites its own
provider). The routing audit's AR-3 event is the precedent for gates going
red on sibling writes; adjudication, not baseline-raising, is the response.

### The 4 LIVE_CANDIDATE pairs (the immediate yield)

**L1 — `LEDGER:LT-SM5::Y_C` and L2 — `LEDGER:LT-SM5::Y_K`.**
`explorations/resolver-wave-d-native-126-connection-placement-2026-08-03.md`
built the native grade-six contraction with exact kernels and says in its own
grade line: *"total P0/Y placement, source selection, VEV, and mass remain
open."* Row LT-SM5's `distance` asks to *"Build the physical
P0/rho(Phi)/Y_K/Y_C placement"* — and its evidence cites only the 2026-08-12
varpi-radial gate, not wave D. Whoever works LT-SM5 should start from wave
D's machinery instead of rebuilding it. (Composition, not advancement: wave D
explicitly did NOT finish the placement.)

**L3 — `LEDGER:RA-A6::v_PSB`.** The row's `revival_trigger` watches for *"a
source-action-selected v_PSB"*.
`explorations/cycle-gates-and-audits/cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md`
already formalizes exactly that object (*"source-selected v_PSB in the
rank-one orbit of V_PSB"*) and records it **not selected by current repo
data**. The row's evidence cites only the 2026-08-12 Higgs-direction gate.
The trigger's baseline is the June gate: any future "v_PSB selected" claim
must be checked against its rank-one orbit construction, and the trigger
should not fire on anything weaker.

**L4 — `ART:…bd1…::SU(3,2)`.** BD-1's CI-X04 directive row presupposes the
`SU(3,2)` real form; the chain adjudication (SC-A R6, ch3's three-site
repair, 2026-08-15) postdates BD-1 and neither cites the other. Anyone
executing CI-X04 must start from SC-A's best-supported reconstruction, not
from H19's impossible variant.

### The 17 UNTYPED, by reason (each with its receipt in the gate)

- **Mood-blindness receipts (2):** `LA-11::Gamma(AdP)` — the sole provider
  line (`DERIVATION-PROGRESS.md:974`) is conditional (*"remains open only if
  … is supplied"*); `FORK:KINEMATIC-VS-PHYSICAL-CARRIER::Pi_RS^phys` — both
  provider lines are imperative/hypothetical while the fork itself states the
  projector DOES NOT EXIST. These two pairs are kept as the named proof that
  the provide-verb surface cannot see grammatical mood.
- **Measured homonym (1):** `SN-2::X_L` — three different objects share the
  token (weak-doublet slot / frame-operator factor / CHSH Pauli-X control).
  Recorded for the homonym channel, which owns that class; nothing repaired
  here.
- **Live sibling channel (4):** H210/SN3 pairs written 2026-08-16 by
  concurrent agents mid-flight; their owner adjudicates, not this pass.
- **Wide-key rows (10):** program-wide tokens (`SU(2)` 36 providers, `U(1)`
  23, `Cl(7,7)` 23, …) where no listed provider line addresses the row's
  specific need. Dismissing them by sampling three files would be exactly the
  unverified typing AR-1 measured at 40% error, so they stay UNTYPED.

## 5. WHAT WAS REPAIRED IN THE EXTRACTOR DURING INTRODUCTION

Three defects were found by running, and each is now pinned by a control:
(1) K1 leaked an unbalanced-paren token (`q_H)` from `gamma(q_H)`) — parens
removed from the continuation class; (2) the first ALL-CAPS-underscore
status-vocabulary stop used `[A-Z]+` segments and **silently deleted `P_H`,
`Q_B`, `Y_C` — including the SA-1 case's own join key**; the pattern now
requires ≥ 2-letter segments and the probe pins both directions; (3) K3
matched the `SC-GEO` fragment inside `SC-GEO-07` — fixed with a digit
lookahead. Defect (2) is the strongest argument this pass produces for
planted controls: an extractor that returns plausible-looking output with a
dead key class is worse than no extractor.

## 6. HOSTILE REVIEW, inline

**Attack 1 — "the join finds citation adjacency, not composition."** Measured
rather than denied: my own first-draft typings, made from the prototype
output before file-fact verification, were wrong on **3 of 6** fork-family
pairs (J-RED `J_red`/`J_h` guessed LIVE — the fork's sources ARE the provider
files; SIGNATURE-AMBIENT `C_perp`/`J_obs` guessed LIVE — the row's own
provenance computes `C_perp = K·J_obs`; LT-SM1 `zeta_F` guessed LIVE — LT-SM7
exists in v0.258, so LA-7's split was already executed). That 50% error rate
on unverified typings, next to 0% on the file-fact-verified ones, reproduces
AR-1's 40%/0% split and is why the gate stores a NOTE naming a file fact for
every adjudication.

**Attack 2 — "Tier 2 is a landfill."** Ten wide rows carry no action, true.
But the cap was not chosen for tidiness: both documented-case keys (`P_H` 18,
`Met(X)` 25 providers) are over-cap, so hiding wide rows would have hidden
the exact failures this gate exists for. Printing beats hiding; the
NON-DISCRIMINATING list prints its counts every run so the cap itself stays
inspectable.

**Attack 3 — "baseline 0 plus concurrent writers = permanent red."** The
FX-2 event is the answer in both directions: yes, a sibling's write tripped
the gate within minutes; and the adjudication cost one map entry with a
mech-verified receipt. The routing audit already lives this way (its AR-3
event is recorded in AR-1 §9) and has ratcheted 17 → 5.

**Attack 4 — "the alias table will drift into fuzz."** Every entry needs the
proving artifact pair; receipts are byte-verified every run (a receipt file
losing its notation REDS the gate); and the contrary control proves
un-aliased case variants do not join. The table can only grow one documented
failure at a time.

**Attack 5 — "the LIVE candidates may already be stale."** Re-checked at
ship time against the live tree: LT-SM5's and RA-A6's evidence fields still
do not cite wave D / the June gate (probe checks C5, run at exit); BD-1
still does not cite `sca-right-chain`. If a sibling composes them tonight,
the probe's C5 goes red and the pair is re-typed ALREADY_COMPOSED — which is
the designed lifecycle, not a defect.

## 7. POSTFLIGHT — five lenses

**Measurement integrity.** Every load-bearing quantity is an integer produced
by the gate or probe: 63 pairs (35+28), 4/42/17/0 types, 56 need sites
(16+6+34), 2,886 provide lines, 2,156 keys, 18 non-discriminating, 3 aliases
with 7 verified receipts, baseline 0, 48 probe checks, 8 selftest plants. No
float is load-bearing anywhere.

**Non-interference.** Four files written, exactly the granted paths. No git
command. Routing registry untouched (and correctly so — see the doc-type
note). No ledger row, fork row, canon file, claim status or sibling-owned
path (`homonym*`, `carrier*`, `carrier-decl*`) was touched; the FX-2 and SN3
material is read and typed, never edited.

**Decay.** This ledger is a snapshot; the gate is not. Pair derivation
re-runs from the live tree every invocation, so the printed list cannot rot
the way SESSION-INDEX §C did; only the ADJUDICATED notes can go stale, and
stale entries print (never fail) so they are visible without being noisy.

**Epistemic honesty.** The extraction floor is stated with its sharpest
counterexample ("Neither is supplied." — no token, no catch); the
mood-blindness pairs are kept UNTYPED as receipts; recall on the documented
cases is 2/3 mechanical, not 3/3.

**Routing hygiene.** The notice and `INTERNAL_STRUCTURAL_ONLY` are carried;
comparator-bordering pairs (LA-3's `SU(5)` fence) are typed as compositions
OWNED BY the routing method, and nothing here re-litigates any of them.
`target_claim: NONE-NOT-A-KILL` — this infrastructure kills nothing.

## 8. CERTIFICATE

- Gate: `process_gates/needs_provides_composition_audit.py` — 8 tests, exit
  0 on the tree as written; prints all 63 candidate pairs + 18
  non-discriminating keys every run; `UNADJUDICATED_BASELINE = 0`.
- Probe: `tests/channel-swings/joe_directed_fx1_needs_provides_join.py` —
  **48 checks, exit 0.**
- `--selftest`: verifies the CLEAN BASELINE passes first, then runs a poison
  meta-control (a deliberately failing run must fail, proving the baseline
  guard has power), then plants **8 false facts — all 8 caught, exit 0.**
- Planted controls that must FIRE every ordinary run: the synthetic
  need/provide pair is found; the case-variant does NOT join without an
  alias receipt; the negated provide claim is NOT supply; `P_H` survives K1
  (the regression that nearly shipped); status vocabulary, register IDs and
  YAML field names are rejected.
- Alias receipts byte-verified: 7 of 7.
- Register pins: hard-core 48 / auxiliary 51 / disavowed-by-source 11; the
  disavowed rows fence the join (pairs whose key appears in a disavowed
  claim's text print with a DISAVOWED-FENCE flag).
- Repository gates re-run after writing:
  `source_native_comparator_routing_audit` exit 0 (5 UNCLASSIFIED, baseline
  5, unchanged — this file is out of derived scope by doc_type and is
  correctly NOT registered); `kill_target_claim_audit` exit 0 at its scope
  baseline; `certificate_shape_audit` exit 0 (untracked files are outside
  its git-tracked sweep until commit; the probe carries asserts and a
  failure path regardless); `tests_manifest_count_audit` exit 0 (the
  channel-swings row is not a counted-format row);
  `lab_active_research_readme_surface_map_audit` exit 0;
  `protected_surface_diff_audit` RED naming exactly this pass's new
  `composition/` path — by construction red for any uncommitted write under
  `lab/active-research/` and resolved on review/commit (SA-1's gate-delta
  note documents the identical behavior); AR-3's live-tree window probe
  re-run after writing: 301/301, unaffected (its window is date-filtered and
  this file sits outside it).
- No git command was run. No file outside the four named paths was written.

## 9. THE BLUNT PARAGRAPH

Does the extractor find real needs, or sentences containing "needs"? Both,
in measurable proportions, and the typing step is what separates them. Of 63
candidates, 4 are real un-composed pairs a person should act on, 42 are
already-composed (most of them citation-adjacency the mech check or a file
fact confirms in seconds), and 17 are honest residue — including two pairs
that exist only because the verb surface cannot tell *"X is supplied"* from
*"only if X is supplied"*, and ten that exist only because `SU(2)` appears
everywhere. So the raw extractor alone is roughly a 1-in-16 signal
instrument, which would be a poor gate if hits were verdicts — and is an
acceptable one because hits are typed candidates, the whole surface is 63
rows read in twenty minutes, and the one class nothing else in this
repository watches — a need whose supply exists uncited — is exactly the
class the 4 LIVE pairs and the retro-detected SA-1 case sit in. The honest
limits: needs stated as bare sentences ("Neither is supplied.") are
invisible; needs stated only in free ledger prose (66 of 82 rows) are
invisible; and imperatives read as supply. Those are the prices of refusing
fuzzy matching, they are printed rather than papered over, and the alias
table is the only sanctioned widening mechanism — one documented failure,
one receipt, at a time.
