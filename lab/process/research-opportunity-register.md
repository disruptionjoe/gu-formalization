# Research opportunity register

Backlog of candidate research moves, cut by **what each one depends on** rather than
by impact-if-successful. Impact ranking floats the standing blocker to the top and
reads as an instruction to go build it; the dependency cut shows what is actually
runnable. Each entry names its lane owner, what it would move, and its gate. The process
analogue is `lab/process/improvement-register-2026-08-03.md`; this is its
research-side counterpart, which did not exist before 2026-08-13.

**Binds nothing.** Entries are candidate work, not dispositions, not claim-status
changes, and not scheduling commitments. The executing wave and the owning lane
decide what runs. An entry appearing here asserts no verdict about GU.

**Why it exists.** Well-formed candidate agendas were being produced and then lost,
because the only places to put them were a chat message or a system-attention
exploration. Lanes hold *state*; this holds *options*.

## How to use it

- Before proposing new work, read this file and `LANE-STATE.yaml`. If the move is
  already an entry, reference its ID rather than restating it.
- Every entry names its **lane owner**. Work is executed under that lane's
  discipline and admission rules, not from this file.
- Entries are killed or completed in place with a dated line, never deleted.
- `tractability` is an estimate of agent-workflow accessibility only. It is not a
  probability of success and carries no scientific weight.

## Standing admission constraints (read before scheduling anything)

- **P-H29 / M-C2 gate:** Lane 1 admits no new interior wave until the RB6/RB7/W177
  nulls are recertified with exact derivatives. Several entries below sit behind
  this and cannot simply be started.
- **Multi-writer protocol:** the scheduled cadence owns `NEXT-STEPS.md`, the
  conditional-build ledgers, and `lab/process/agent-context-pack.md`;
  `explorations/` is shared append-only staging. Side runs mount with
  `repo-session-sync.sh --scope`.
- **Trunk rule (2026-08-13):** scheduled progress and stewardship runs commit and
  push to `main`.

---

## Entries

Provenance: Joe direct chat, 2026-08-13, a ranked assessment of moves that would
most raise the assessed likelihood of the Observerse/GU-class picture. Filed
verbatim in substance, re-anchored here against `CURRENT-STATE.yaml`,
`LANE-STATE.yaml` and `NEXT-STEPS.md` at `06084deb`.

| ID | Move | Lane | What it would move | Tractability | Gate / status |
| --- | --- | --- | --- | --- | --- |
| **ROR-01** | Physical fermion/BV operator, owned by **the selected action**, producing half-asymmetric cohomology or a fermion projector that discriminates `W` / mirror / random 192s / `H640` / `832` without fitting the large trace-`Hq` fibre | 1 | The whole carrier-selection problem. Would convert connection-arena structure into something that actually *selects* a physical carrier | high effort, well-typed | **This is the live front, not backlog.** Verbatim the repo's `current_question`; `next_condition` prescribes it. Do not rerun `Hq` compatibility; do not apply the bosonic projector to fermion subspaces |
| **ROR-02** | Principal-*changing* action / `Q_B` owner with zero torsion class or controlled absorption through cubic/quartic order | 1 | The open half of the selected action's owner structure. Principal-*preserving* absorption is already universal; the changing case is not | high effort | **Explicitly typed a disjoint fallback in `next_condition`.** Genuinely parallel to ROR-01 by construction, so it is the strongest candidate for a non-colliding second track |
| **ROR-03** | Physical tangent / BV graph with a full Layer-0 fingerprint reset, shown consistent with existing stationary jets and Ward data | 1 | Closes the compositional gate Lane 1 names as its next parallel gate | moderate; composition + type checking | Named in Lane 1's own summary. Layer-0 reset is the load-bearing part, not the composition |
| **ROR-04** | Close the remaining Clifford grades and the total residual of the selected action, beyond the exact `Cl2` second-layer pullback | 1 | Tightens the action's uniqueness | moderate; finite rank/linear algebra | Behind the P-H29 gate if it constitutes a new interior wave |
| **ROR-05** | Recover a clean projected Einstein / GR limit, or a controlled residual, from the selected action plus the observation map | 1 | Would connect the construction to the sector everyone checks first | moderate | Project current Euler/preboundary owners onto the metric sector under existing soldering. Note the standing caution: compatibility-on-an-imported-metric is not a derivation (`CORRECTION RFAIL-02/03`) |
| **ROR-06** | Certificate-backed dark-energy sign / no-phantom-crossing prediction tied only to the external orientation bit `sigma`, with no added free coefficients | 2 | A genuine falsifiable, on the lane whose job is falsifiables | moderate | Lane 2 is `blocked_on_internal_decision`; standing instruction is monitor exact reopen signals and **do not rerun DE-AMP**. Sequence behind that decision |
| **ROR-07** | Shrink the external generation datum (`tau ~ Z/3`) to a short discrete list compatible with anomaly inflow, index theorems, or the 2-primary blindness structure | 1 / 2 | Does not force three; shrinking the external choice set is the credible win | moderate; finite topological / rep searches | Must not be written as forcing three. The count is currently typed **accommodation, not prediction** |
| **ROR-08** | Formalize the newest Cartan-involutivity and torsion-absorption results in Lean, or raise existing Python certificates to machine-checked statements | 3 | Confidence in the construction surface itself | moderate; content is already exact and finite-dimensional | **Runnable now.** Lane 3 is green and operates on frozen results, so it cannot collide with Lane 1 |
| **ROR-09** | Exhaustive adversarial hunt for counter-examples to the remaining antilinear / index-conservation claims in the Clifford-RS class, or a clean non-existence proof under stated assumptions | 3 | Solidifies the central located-not-forced structural law; the linear leg is theorem-grade, the antilinear side is only "no counter-example found" | moderate | **Runnable now**, same reason as ROR-08 |
| **ROR-10** | Demonstrate a measurable, certificate-reproducible improvement on the public parsimony ledger versus SM+GR+LCDM, once a candidate source-action packet exists | 2 / 3 | External persuasiveness; a checkable win beats internal claims | low once the ledger is automated | Gated on a candidate source-action packet existing, so downstream of ROR-01/02 |

## Dependency cut (read this before ranking by impact)

**CORRECTION 2026-08-13, Joe direct chat.** The first version of this file ranked by
impact-if-successful, which floats GU's unbuilt source action to the top and reads
as an instruction to go build it. That is the wrong steer and it rested on a
conflation. The register is re-cut by *what a move depends on*.

**`the selected action` is not GU's source action.** They are different objects.
The selected action exists and is what `explorations/conditional-build/` (500 files)
has been working on for months. GU's own source action is unbuilt and gates
*promotion of conditional results to physical claims* — it does not gate the
construction work itself. `CURRENT-STATE`'s `current_question` asks whether **the
selected action** can produce a half-asymmetric cohomology, which is conditional-build
work, not source-action work.

**Standing strategy (Joe, 2026-08-13): do not turn the repo back toward building the
source action.** Build conditionally, accumulate structure that is valid conditional
on it, and let the blocker stay blocked.

### Buildable now, no source action required

| ID | Why it is unblocked |
| --- | --- |
| ROR-01 | Operates on **the selected action** and the physical BV/domain complex, both of which exist. It is the live front for that reason |
| ROR-02 | Principal-changing I2B work is typed a **disjoint fallback** in `next_condition`; it is a second conditional track, not a source-action build |
| ROR-03 | Composition and Layer-0 type checking over existing stationary jets and Ward data |
| ROR-04 | Finite rank / linear algebra on the **selected** action's residual carrier |
| ROR-05 | Projection of existing Euler/preboundary owners under existing soldering |
| ROR-07 | Finite topological and representation searches; touches no action |
| ROR-08 | Lean formalization of results that are already exact and finite-dimensional |
| ROR-09 | Adversarial search over an existing class |

That is eight of ten runnable without the blocker.

### Gated

| ID | Gate |
| --- | --- |
| ROR-06 | Lane 2's open internal decision, plus the standing do-not-rerun-DE-AMP instruction. Not a source-action gate |
| ROR-10 | Needs a candidate source-action packet to compare against, so it genuinely sits downstream |

### Remaining honest notes

**ROR-08 and ROR-09 are the safest parallel track**, because Lane 3 hardens frozen
results and by construction cannot contend with Lane 1's live work. ROR-02 is the
strongest *second construction* track, because the repo already typed it disjoint.

**Several of these could produce clean negatives that lower the assessed
likelihood.** That is the point, and a negative filed as a negative is a success of
this register, not a failure.

**What stays blocked is promotion, not construction.** Conditional results remain
conditional until the source action exists. Nothing here licenses promoting a
conditional build to a physical claim, and the P-H29 exact-derivative rule and the
two-phase canon promotion contract both still apply.

## Maintenance

- Add entries with the next `ROR-nn`. Never renumber.
- On completion or kill, append a dated line to the row's Gate/status cell with the
  artifact reference. Do not delete rows.
- Re-anchor the table against `CURRENT-STATE.yaml` and `LANE-STATE.yaml` whenever a
  lane's rank-one changes; a stale opportunity register is worse than none, and the
  repo's own audit meta-pattern is honest artifacts with optimistically stale
  coordination surfaces.
