---
title: "Channel swing CH-SM: the breaking-chain sweep and the parameter card"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (deep research swing on CH-SM)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/adapter-assumed-four-leg-swing-2026-07-19.md
  - explorations/five-leg-swing-2026-07-19.md
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
inputs:
  - lab/process/source-object-interface-contract.md
  - lab/process/integration-readiness-scorecard.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - explorations/construction-space-sm-r0-harness-c5-2026-07-19.md
  - tests/recovery-contract/construction_space_sm_r0_c5_harness.py
  - "papers/drafts/Transcript into the impossible.md (Pati-Salam / trace-reversal passage, [00:43:04]-[00:47:18])"
  - "lab/process/recovery-no-go-defense-register.json (RECOVERY-NOGO-SM-SELECTOR)"
test: tests/channel-swings/ch_sm_chain_sweep.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Channel swing CH-SM: the chain sweep, VEV conditioning, and the parameter card

> **2026-07-21 typing correction (`P-54-WELD`):** the native distortion is
> valued in one vertical `10`, not in `Sym^2_0(10)`. There is no linear
> equivariant `10 -> 54` weld. A `54` can be formed only as an explicit
> quadratic vertical Gram composite with additional source, nonzero/stabilizer,
> and real-form data. Accordingly, statements below that the metric slot or
> curvature-locked `theta` itself forces the Pati-Salam first step are retained
> as historical probe hypotheses, not current conclusions. See
> `explorations/p54-weld-typing-2026-07-21.md`.

Scorecard said this was the cheapest card-freeze on the board: enumerate the
Spin(10)/Pati-Salam breaking chains, run each through the R0 arithmetic, and
the surviving list IS the candidate adapter range for the subgroup-chain
datum. Done, machine-checked, all exact rational arithmetic:
`tests/channel-swings/ch_sm_chain_sweep.py` (30 checks, ALL PASS; extends the
P2 harness, does not modify it — the P2 harness still passes independently).

The headline is stronger than "a finite list survives": **the surviving
chains are R0-EQUIVALENT** — every chain delivers the identical gauge group,
chirality, anomaly arithmetic, electric charges, and absolute hypercharge
normalization. At R0 the chain datum carries almost no freedom; nearly all of
its content is forced by GU-native structure plus consistency, and what
remains free is scale/RG-level data outside R0.

## 1. The chain sweep (machine-checked results)

### 1a. Kill taxonomy — what the arithmetic eliminates

- **Kill class 1 (chirality / rank loss).** The 16 branches vectorlike
  through every rank-losing symmetric subgroup: SO(9), SO(7)xSO(3),
  SO(5)xSO(5). General lemma (S2c): negating any 4 of the 5 spinor
  coordinates closes the 16's weight multiset, so ANY intermediate stage
  that drops Cartan rank before reaching G_SM kills chirality. Chirality
  survives only through full-rank (rank-5) descent, with the single final
  rank drop landing on G_SM itself.
- **Kill class 2 (G_SM hosting; the A1-lock).** Brute-force over all 40
  roots of D5 (S1a): for a regular su(3)_c on any coordinate triple, the
  ONLY root-su(2)s commuting with it are the two complement-pair su(2)s —
  exactly the Pati-Salam SU(2)_L = +-(e4+e5) and SU(2)_R = +-(e4-e5). Both
  use coordinate 5, so SO(8)xSO(2) — the one full-rank symmetric subgroup
  outside the U(5)/PS lattice — cannot host G_SM at all (regular-embedding
  scope; a special embedding would fail the spectrum screen instead).
- **Kill class 3 (hypercharge line).** Exact solve in the 2-plane
  orthogonal to su(3)+su(2)_L (S3): Y = a*T3R + b*(B-L) reproduces the SM
  multiset for exactly two lines, (a,b) = (1, 1/2) [standard] and
  (-1, 1/2) [flipped]. The SU(2)_R Weyl element (w4 <-> w5) preserves the
  16 and maps one to the other, so they are Spin(10)-gauge-conjugate:
  **ONE physical hypercharge line.** Controls fail as they should: T3R
  alone, (B-L)/2 alone, the X-line, and a wrong-slope mixture all miss the
  multiset.

### 1b. Real-form reading (the transcript's derivation, sharpened)

Each first step is the maximal compact of a real form of Spin(10):
SO(9,1)->SO(9); SO(8,2)->SO(8)xSO(2); SO(7,3)->SO(7)xSO(3);
SO(6,4)->Spin(6)xSpin(4) = Pati-Salam; SO(5,5)->SO(5)xSO(5);
SO*(10)->U(5). The sweep therefore says: **among the five vector
signatures, ONLY (6,4) survives both screens** (plus the non-vector form
SO*(10), whose compact is the SU(5)xU(1) side). GU's trace reversal of the
Frobenius metric maps (7,3) -> (6,4) (transcript [00:43:04]) — it lands on
the unique surviving vector signature. Had it landed on (9,1), (8,2), or
(5,5), the SM recovery would be dead at R0. Conditional retrodiction-grade
coherence, stated as such, no verdict moved. The transcript's second
noncompact stage ("SU(3,2) ... maximal compact SU(3)xSU(2)xU(1)",
[00:43:47] and [00:45:00]) is the noncompact shadow of the U(5)-side step:
U(3,2) sits in SO(6,4) via a complex structure on the 10, so both lattice
sides exist inside the (6,4) form and the transcript voices both.

### 1c. The surviving chain list — 16 chains, all R0-equivalent

Nodes (fixed G_SM inside all of them; subgroup relations machine-verified
by root-set inclusion): Spin(10); SU(5)xU(1); SU(5); PS =
SU(4)xSU(2)_LxSU(2)_R; SU(4)xSU(2)_LxU(1)_R; SU(3)xSU(2)_LxSU(2)_RxU(1)_{B-L};
G_SMxU(1); G_SM. Note: the "penultimate" rank-5 stage is UNIQUE —
SU(3)xSU(2)xU(1)_RxU(1)_{B-L} and G_SMxU(1)_X are the same subgroup in
different bases, so the lattice funnels. All descending chains (S6d): 16
total — 4 SU(5)-side, 10 PS-side, 2 direct. Full list in the script output;
representative named chains: #1 Georgi-Glashow-through-SO(10)
(Spin(10)->SU(5)xU(1)->SU(5)->G_SM); #7 the canonical left-right chain
(Spin(10)->PS->SU(3)xSU(2)_LxSU(2)_RxU(1)->G_SMxU(1)->G_SM); #10 the minimal
PS chain; #16 one-step breaking. D-parity refines the PS-side entries
(PS-with-D via 54 vs PS-without-D via 210) — a Z/2 annotation affecting RG
running only, invisible to R0 arithmetic.

**Per-chain R0 arithmetic (identical for every one of the 16, S4/S6f):**

| Check | Result (exact) |
|---|---|
| 16 -> SM multiset + nu_c | exact match |
| U(1)^3, grav-U(1), [SU(2)]^2 U(1), su(3) triality | all 0 |
| Witten SU(2) parity (doublet count) | 4, even |
| Chirality (no vectorlike pair) | chiral |
| Electric charges Q = T3L + Y | exact SM values |
| Absolute normalization Tr(Y^2)/Tr(T3L^2) | 5/3 |
| sin^2(theta_W) at the boundary = Tr(T3L^2)/Tr(Q^2) | 3/8 |

**The rank-drop lemma (S5), the sweep's sharpest structural output:** the
G_SM-invariant direction with nonzero X is u = (1,1,1,-1,1), whose
coordinate sum is ODD — so u lies outside the root lattice and is absent
from EVERY tensor irrep (45, 54, 210, ...). u/2 is the nu_c weight of the
16 and u is the nu_c.nu_c weight of the 126. **The final rank-reducing step
of every chain demands a spinorial condensate (16- or 126-type); no tensor
VEV can do it.** The 126 route leaves matter parity (-1)^(3(B-L)) unbroken
— a physical Z/2 output of the chain (flagged; NOT to be conflated with the
transmitted Krein-orientation Z/2 without proof).

## 2. VEV conditioning — what the distortion VEV must transform as

This is the concrete content of "chirality conditioned on a VEV"
(transcript [00:46:02]: three families of chiral fermions "if you have a
decreased VEV in the total space taking a Dirac equation into two Weyl
equations" — the group-theory face of that Dirac->2 Weyl split is exactly
the spinorial rank-drop step above). Per-edge demands, typed:

| Breaking step | VEV irrep (invariant direction) | Tensor type | GU-native candidate |
|---|---|---|---|
| Spin(10) -> PS (D-even) | 54 | Sym^2(10)_0 | **trace-reversed Frobenius-metric distortion**: Sym^2(10) = 1 + 54 exactly — the metric slot IS this rep |
| Spin(10) -> PS (D-odd) | 210 (1,1,1) | Lambda^4(10) | 4-form condensate; not exhibited natively |
| Spin(10) -> SU(5)xU(1) | 45 (X-direction) | Lambda^2(10) | complex structure J on the 10 (transcript [00:45:00]: the distinguished dimension "has a complex structure") |
| PS -> SU(3)xSU(2)_LxSU(2)_RxU(1) | 45 (15,1,1), B-L direction | Lambda^2 | curvature/field-strength-type |
| PS -> SU(4)xSU(2)_LxU(1)_R | 45 (1,1,3), T3R direction | Lambda^2 | curvature/field-strength-type |
| any rank-5 stage -> G_SM (rank drop) | 16 (nu_c) or 126 (10bar,1,3) | spinor coset (odd-sum lattice) | spinor bilinear: Sym^2(16) = 10 + 126 — a fermion condensate supplies the 126 class |

**The CH-GR coupling, now sharp.** The C10 distortion field occupies the
metric slot; a symmetric two-tensor on the 10 decomposes as 1 + 54 and
NOTHING ELSE. So a metric-type distortion VEV can select exactly one first
step: **Spin(10) -> Pati-Salam, D-parity even.** It cannot reach the
SU(5) side (needs Lambda^2 = a complex-structure/curvature condensate) and
cannot finish the chain (rank drop needs a spinor bilinear). Consequences:

- Conditional on H-GR' (metric-slot VEV), the chain's first step is FORCED
  and the surviving range collapses from 16 chains to the 6 PS-descendant
  paths (chains 5-10), D-even at the PS stage.
- H-GR' sub-branch map: (a) curvature-locked anisotropic VEV — can align a
  54 direction, live; (b) homogeneous VEV — pure trace (the 1 of 1+54),
  selects NOTHING, so if (b) is the only C10 survivor, CH-SM's
  conditioning dies with it (**shared co-kill with CH-GR**);
  (c) gradient-dominated — undetermined until C10 is formalized.
- The full chain needs three typed condensate slots beyond the first:
  Sym^2-type (native: the distortion), Lambda^2-type (candidate: GU's own
  gauge curvature / the complex structure), spinor-bilinear-type
  (candidate: a fermion condensate; record-current-adjacent objects exist
  but no identification is claimed). These go on the adapter demand ledger
  as typed demands, not as new payload items, since they are activation
  directions of the SAME branch selection (payload item 2).

## 3. What the chain datum buys / cannot buy / what would buy it

**Buys (machine-checked):** the gauge group G_SM; chirality of one 16;
full anomaly cancellation including Witten parity; electric charges;
**absolute hypercharge normalization** (Tr(Y^2)/Tr(T3L^2) = 5/3, i.e.
sin^2(theta_W) = 3/8 at the unification boundary — the "absolute
normalization" item the P2 harness demanded, delivered because Y sits
inside spin(10) where the trace form fixes it); matter parity Z/2 if the
rank drop is 126-type.

**Cannot buy (bounded by prior no-gos; not re-derived here):** an odd
generation count. The chain sweep is per-16 arithmetic; multiplicity is
orthogonal to it. The quaternionic-parity no-go
(`canon/no-go-quaternionic-parity-generation-sector.md`) forces every
GU-native Hermitian carrier to even index, and ch2(S_X)[K3] = -5376 killed
the natural characteristic-class count (archaeology items 4-5). No element
of the surviving chain list touches either obstruction. The chain datum
also cannot buy absolute scales (M_U, intermediate scales — R0-blind), the
physical Higgs sector, or spectrum completion beyond one 16; those remain
open interface-contract items.

**Would buy generations:** an a-priori rank pin (half-index reading) or a
non-quaternionic structure (literal reading). The decisive live probe is
CH-QM's: whether the transmitted Z/2 orientation is itself
non-quaternionic — one payload bit discharging Krein sign + parity + arrow
at once, keeping N <= 4. That probe is CH-QM's to run; this card only
holds the hook open. If the orientation is J_quat-commuting, generations
force a fifth payload item and this card's ledger gains D-SM-4.

## 4. Card conditions: alignment rigidity and the varying-constants tripwire

- **Alignment-rigidity condition.** The chain datum must be a GLOBAL rigid
  datum (p2c-style topologically stored selection — locally unreadable,
  hence locally unvariable), or the construction must show the
  misalignment/rotation modes of the breaking direction are frozen,
  massive, or decoupled. If the datum is topologically stored, the
  tripwire below is discharged structurally, for free.
- **Varying-constants tripwire (observational kill, available now).** If
  the formalized construction predicts detectable spatial or temporal
  drift of the selected chain (couplings dragged by a curvature-responding
  breaking direction, per H-GR'), existing bounds falsify that branch.
  Constraint classes (types named, per card convention; no precise numbers
  required at R0): (i) quasar-absorption-spectra varying-alpha bounds,
  temporal and spatial; (ii) laboratory atomic-clock comparison drift
  bounds; (iii) Oklo natural-reactor bound; (iv) weak-equivalence-principle
  / fifth-force bounds (a spatially varying alignment field couples
  compositionally); (v) strong-field spectroscopy (white-dwarf /
  neutron-star lines) for the curvature-conditioned variant specifically.
- **R1-level constraint class (phenomenologist note, beyond R0):** the
  chains differ physically only through intermediate scales; proton-decay
  lifetime bounds (Super-K class) and n-nbar oscillation bounds (for low
  B-L scales) prune the chain list at R1. Named for the card; not part of
  the R0 sweep.

## 5. CH-SM parameter card (draft)

- **Channel:** CH-SM (Standard Model selector). **Payload item:** PI-4,
  the subgroup-chain datum, conditioned on PI-2 (VEV branch).
- **Datum type and range (frozen by this sweep):** one element of the
  enumerated chain set. Unconditionally: 16 chains (4 SU(5)-side, 10
  PS-side, 2 direct), ALL R0-equivalent. Conditional on H-GR'
  (metric-type distortion VEV): 6 PS-side chains, first step forced to
  Spin(10) -> PS x D. Decomposition of the datum's information content:
  - real form: FORCED to (6,4) (unique surviving vector signature; GU's
    trace reversal supplies it natively) — 0 adapter bits, conditional;
  - first-step side: FORCED to PS by metric-type VEV — 0 bits,
    conditional on H-GR';
  - hypercharge line: UNIQUE mod Spin(10) Weyl — 0 bits;
  - rank-drop direction: forced to nu_c mod gauge — 0 bits, but demands a
    spinor-type condensate (typed demand D-SM-2);
  - residual freedom: descent path among 6 (R0-equivalent; physical
    content = intermediate scales, RG-level) + D-parity Z/2 — approx. 2-3
    bits, none of them R0-visible.
- **Buys / cannot buy / would buy:** section 3 verbatim.
- **Conditions:** alignment rigidity + varying-constants tripwire
  (section 4); co-kill with CH-GR's homogeneous-only branch (section 2).
- **Adapter demand ledger entries (typed, for routing to the interface
  contract per standing-axiom rule 4):**
  - D-SM-1: one chain-path selection from the surviving set (<= 6 after
    conditioning; R0-equivalence class — content is scale-level);
  - D-SM-2: activation of a spinor-coset (16/126-type) condensate
    direction for the rank drop (no tensor VEV can substitute — lemma S5);
  - D-SM-3: rigidity certificate for the alignment (or topological
    storage of the datum, which supplies it structurally);
  - D-SM-4 (HELD, pending CH-QM's orientation probe): generation payload
    (rank pin or non-quaternionic structure) — only materializes if the
    transmitted Z/2 is J_quat-commuting; if non-quaternionic, discharged
    by payload item 1 and N stays <= 4.
- **Kills on record for this card:** ch2 = -5376 (generation count via
  characteristic class); quaternionic-parity even-index no-go;
  RECOVERY-NOGO-SM-SELECTOR (host is not a selector — unchanged: nothing
  here promotes the host; the chain datum is adapter-supplied, typed,
  conditional); wrong-Y-line and rank-losing chains (this sweep).

## 6. Proposed scorecard row update (proposal only; not applied here)

- **Q1: PARTIAL (strengthened).** Chain-level existence is now
  machine-checked end to end, with a conditional forced chain
  Spin(6,4) -> PS x D -> ... -> G_SM; the SELECTOR construction (Higgs
  sector, spectrum completion, decoupling) remains unexhibited, so not YES.
- **Q2: YES (unchanged, sharpened).** Seven harness constraints + alignment
  rigidity now stated with named observational bound classes + R1
  constraint classes (proton decay, n-nbar).
- **Q3: YES, conditional (was PARTIAL).** The adapter range is FROZEN as
  the surviving chain list; the datum's R0-visible freedom is approx. zero
  (everything forced except the R0-equivalent path choice + D-parity).
  Named residual gaps: (g1) generation payload excluded from what the
  datum buys — CH-QM orientation probe decides D-SM-4; (g2) C10
  branch-space match (existence of an alignable 54 direction) — CH-GR
  dependency, with a shared co-kill; (g3) intermediate scales are
  RG-level, outside R0 — an R1 treatment is the next rung, not a payload
  change.

## 7. Inline persona passes (three, inline in this worker per policy)

- **GUT model-builder:** the lattice and its funnel through the unique
  rank-5 penultimate stage match the standard SO(10) chain tables
  (Georgi-Glashow, Pati-Salam, left-right, flipped-as-Weyl-artifact);
  D-parity handled correctly as an RG-level refinement; the
  "126 preserves matter parity" output is the standard result and is the
  right thing to flag as a distinct Z/2. No missing standard chain found
  (adding nodes like SU(5)xU(1) with flipped labeling would double-count
  Weyl-conjugates the sweep already identifies).
- **Representation theorist:** the two nontrivial lemmas are sound and the
  proofs are the right ones — the A1-lock is a root-pairing computation
  (brute-forced, no case left), and the rank-drop lemma is coset parity in
  the weight lattice (odd coordinate sum separates spinor coset from root
  lattice; machine-checked on 16, 10, Sym^2(16)). Scope honesty: the
  A1-lock covers regular embeddings; special embeddings are excluded by
  the spectrum screen, not by the lock — stated in the doc.
- **Phenomenologist:** the R0-equivalence finding is exactly why GUT
  phenomenology lives in RG space — the card correctly refuses to import
  scale physics into R0 and instead names the constraint classes (varying
  constants for rigidity; proton decay / n-nbar for chain pruning at R1).
  The sin^2(theta_W) = 3/8 boundary value is a boundary condition, not a
  low-energy prediction; the card says so.

## Receipts

- `tests/channel-swings/ch_sm_chain_sweep.py` — 30 checks, ALL PASS
  (exact Fraction arithmetic; sections S1-S6 as cited above).
- `tests/recovery-contract/construction_space_sm_r0_c5_harness.py` —
  re-run unmodified after this swing: ALL PASS (anomaly formulas here are
  the same formulas, reimplemented, on the sweep's surviving spectrum).
- Transcript anchors: [00:43:04] trace reversal (7,3)->(6,4);
  [00:43:47]+[00:45:00] maximal-compact chain and the complex structure;
  [00:46:02] VEV-conditioned chirality (Dirac -> two Weyl);
  [00:46:40] "general relativity knows Pati-Salam" / one grand unified
  generation.
- Prior kills honored, none re-run: ch2 = -5376; quaternionic-parity
  no-go; RECOVERY-NOGO-SM-SELECTOR host-is-not-selector.

## Boundary

All results are conditional constructions under the standing axiom
(`A_boundary`). The sweep's arithmetic is unconditional group theory; its
reading as an adapter range is conditional. No claim status, canon
verdict, public posture, or cross-repo surface moves. The scorecard row
update and the demand-ledger entries are PROPOSALS routed via this doc;
the generation hook stays with CH-QM. Host evidence remains typed support,
not a selector — nothing here resurrects RECOVERY-NOGO-SM-SELECTOR.
