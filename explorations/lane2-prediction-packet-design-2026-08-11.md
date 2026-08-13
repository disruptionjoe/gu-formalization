---
title: "Design packet: the prediction research native prediction packet and the typed XS–S decision"
status: active_research
doc_type: design_packet
created: 2026-08-11
target: "prediction research native prediction packet + XS–S decision typing"
head_commit_read_against: bdd2c934335e6e534d4e0f9e7f55d7678eb566d8
relates_to:
  - lab/process/CURRENT-RESEARCH-CONTEXT.md (anchor fact 1, RECORDS↔DE, lines 1643-1666)
  - lab/process/anchor-council-2026-08-03/seat2-cosmology.md (§1.4 origin of the XS–S question)
  - lab/process/anchor-council-2026-08-03/seat4-envelope.md (A6/C11 gating; collision row)
  - explorations/W230-close-a4-derive-w154-2026-07-14.md (the c_kin=0 COMPLETED-POSIT)
  - explorations/de-pipeline-certification-and-bridge-test-2026-08-03.md (Wave A-2 + correction banner)
  - explorations/de-certification-redo-2026-08-03.md (A1-A5 composition ledger; BLOCKED-ON-A4)
  - explorations/dc-h2-reciprocity-and-the-zu-block-ratio-2026-08-04.md (one-scale reduction; escape-variety fork)
  - explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md (§3, r(N)=κ₀√N)
  - explorations/W187-law-shadow-reduction-audit-2026-07-14.md (same-label DIFFERENT file; carries no r(N))
  - explorations/W154-reverse-engineered-source-action-2026-07-14.md (RE1, FIRED)
  - explorations/W158-promotion-gate-boundary-term-C3-2026-07-14.md (RISEb, FIRED)
  - explorations/W215-true-vacuum-dynamical-systems-2026-07-14.md (DS4c reciprocity)
  - explorations/W220-falsify-dark-energy-vs-desi-2026-07-14.md (four-axis character; FC clauses)
  - explorations/W226-harden-de-tripwire-squeeze-data-2026-07-14.md (hardened FC-d, margin +1.11)
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md (Z_U NOT BUILT; KER1-KER4)
  - explorations/unified-source-datum-packet-v0-2026-07-30.md (written action; Z_U charged; ℓ²=Z_Uκ)
  - explorations/gimmel-dewitt-normalization-ledger-2026-07-20.md (λ_GU=1/2; trace-flip)
  - explorations/channel-swing-CH-COSMO-2026-07-19.md (scale bracket; Z_theta>0 never emitted)
  - canon/theta-field-flrw-dark-energy-eos.md (DARK-ENERGY-07)
  - canon/dark-energy-theta-divergence-free.md (θ definition; structural 120-orders claim)
  - lab/process/improvement-register-2026-08-03.md (M-H12/M-H13 + riders)
  - "private orchestration runtime/mailboxes/gu-formalization/20260803-taf-response-records-de-typings.md (T588 N-typing constraint; outside this repo)"
  - explorations/signature-ambient-relative-sign-resolver-design-packet-2026-08-11.md (house-style sibling; interacting fork)
binding: >-
  Design input for a future prediction research wave. This packet binds no wave and makes
  no disposition: it names no horn of the XS–S decision, moves no register
  row, verdict, claim status, canon entry, fork, bar, count, H59, or
  LANE-STATE entry, and touches no observational data. The executing wave
  owns every disposition under the full pre-flight / hostile-review checking
  contract; lens outputs below are planning evidence, never scientific
  evidence.
hostile_review: lab/process/hostile-reviews/2026-08-11-lane2-prediction-packet-design-review.md
canon_verdict_change: none
row_change: none
registry_change: none
---

# Design packet: the prediction research native prediction packet, and the XS–S decision typed

prediction research's standing attention model names a bounded, genuinely GU-native
prediction assembled into a prediction packet as the lane's top internal
precedent (`AGENTS.md:183-187`), and the lane's contract is "discover,
derive, freeze, compute, and confront native predictions and falsification
tripwires without calibration leakage" (`AGENTS.md:170-171`). The leading
candidate route — the dark-energy shape story — is stalled on one named
decision: the anchor fact instructs "decide that XS–S question before
scheduling any r(N(z)) refit" (`lab/process/CURRENT-RESEARCH-CONTEXT.md:1654`).
This packet does two things: it TYPES that decision precisely against the
current tree (the question has moved twice since the anchor was written,
and a wave executing the 2026-08-03 wording would attack a superseded
object), and it scaffolds the prediction packet around it — leakage audit,
fork classification, tripwire freeze, surplus count, and the bounded
decisive test a wave can start executing. It decides nothing.

"XS–S" is an effort grade (extra-small-to-small), not an object: the
council filed the question as "does W230's spatial-gradient `L` map to the
FLRW time-kinetic term? XS–S effort"
(`lab/process/anchor-council-2026-08-03/seat2-cosmology.md:78`,
`seat4-envelope.md:133`). Throughout, "the XS–S decision" names that
question in its CURRENT form (§Decision-typing below), not the superseded
2026-08-03 wording.

## Pre-flight assessment

Failure modes this design could commit, and the mitigations applied:

1. **Typing a superseded question.** The anchor's wording ("c_kin=0 in
   unresolved tension with the FLRW kinetic term — decide that XS–S
   question") predates two decisive artifacts: the 2026-08-03 redo proved
   the k=0 caveat cannot decide it and re-typed the state BLOCKED-ON-A4
   with the decisive object named (`de-certification-redo-2026-08-03.md`
   §3), and DC-H2 (2026-08-04) reduced the residue to one dimensionful
   scale and excluded a whole condition class
   (`dc-h2-reciprocity-and-the-zu-block-ratio-2026-08-04.md` §7).
   Mitigation: the State section carries the full evolution; the decision
   typed here is the current one.
2. **False novelty.** A 2026-08-09 session produced seven false-novelty
   claims in one day (`AGENTS.md:262-275`). Mitigation: `novelty-check.py`
   runs recorded in the Prior-art section; every "new" statement is
   relative to named near hits (PP1-PP3, CH-COSMO, cb-d, the de-certification
   pair).
3. **Calibration leakage inside the design itself.** The mh13 proxy
   witnesses were produced by optimizing against the DR2 likelihood;
   using them to pick a candidate family would launder data into the
   "prediction." Mitigation: the leakage lens quarantines them explicitly.
4. **Layer-0 equivocation.** This neighborhood carries at least six
   load-bearing homonyms (r, N, c_kin, L, "fibre", θ/B/U). Mitigation: the
   object table below; the wave re-runs it as its Layer-0 precondition
   (mandatory per `AGENTS.md:5-8` and the six-axis template's Layer-0).
5. **Summary outrunning artifact.** The pack's own anchor states W230's
   necessity unqualified; W230's stated hypotheses are "L SPD and not
   proportional to M" (`W230...md:189-191`), the escape variety now has a
   certificate-grade non-proportional member, and the "equivariant Gram"
   label is a recorded repo disconnect (DC-H2 §6.3). Mitigation: exact
   scopes carried; verify manifest grades every claim.
6. **Binding overreach / scheduling around the wave rule.** Mitigation:
   binding note in frontmatter; the decisive test moves NAMED gates
   (M-H13 item (a), seat4's A6, hence C11) per P-H28 (`AGENTS.md:43`);
   outcome table is wave-owned.
7. **TaF fence violations.** Mitigation: N(z) typing carried as an
   external datum with provenance; no identity claims; ADAPTER2-01 stays
   withdrawn; the reservoir Krein sign untouched.
8. **Un-run numerics.** Mitigation: every number below is a file citation;
   this packet runs no computation and claims none.

## Layer-0 object table (precondition; the wave re-runs it before work)

| term | sense 1 | sense 2+ | ruling for this packet |
|---|---|---|---|
| `θ` | the connection distortion `θ = π − ε⁻¹Bε`, Ψ-independent (`canon/dark-energy-theta-divergence-free.md` §1; W230 [MISMATCH]) | (b) H44's FLRW scalar mode `B(t)` (`tests/wave25/H44_de_backreacted_background.py`); (c) the source-datum packet's `U`-field, identified upstream, not adjudicated (DC-H2 §0) | three objects; the identification chain θ↔B is exactly the five-arrow A1-A5 composition, UNCERTAIN at A4; θ↔U is carried, not settled |
| `c_kin` | W230's single scalar on an ultralocal 14-frame fixture | (b) the charged parent-action coefficient `Z_U` (`unified-source-datum-packet-v0...md` §7.2); (c) the block split `(c_b : c_s : c_f)` on the A3 configuration (redo A4); (d) after DC-H2: ONE dimensionful scale, `ℓ² = Z_U κ` (packet §7.2 "derived, not independently charged") | the decision below is typed against (c)/(d); (a) is a fixture stand-in |
| `L` | W230's fixed SPD stand-in for `D_A*D_A` | the native gradient quadratic form built from `*_G` of the gimmel metric — vertical block signature (6,4), NOT positive-definite (`gimmel-dewitt-normalization-ledger...md`) | W230 [NEC]'s stated hypotheses (SPD, not ∝M) do not automatically cover the native indefinite object; the indefinite-block variant is the recorded signature fence (`de-pipeline-certification...md` [BLK]) and is a gate of the decisive test |
| `r` | self-energy coupling ratio, bar-(b) basin selection (W187 §2) | any DE coefficient | HOMONYM (seat2 §1.3a); the shared object is `N`, not `r`; a DE-side failure is never a bar-(b) failure |
| `N` | bulk past 4-volume (W146 sense; `Λ = c/√N`) | (b) `N_conf = π√N_bulk` (W149 sense); (c) TaF's confirmed/frontier-side access-audited count | A7: the two normalizations give different laws and the choice is not free (seat2 §2.1(i)); TaF constraint: a single global scalar `N` is TaF's refuted ledger shape (T588 contract B) — `N(z)` must be typed per-observer or regional-reconciling, with FLRW-homogeneity stated as a condition (mailbox response T2) |
| "fibre" | the 14 frame directions of the (9,5) tangent model (W230's fixture) | functions on the metric coset `GL(4,R)/O(3,1)` (rc3 spectrum; H44's mode) | different objects; every fixture number transports to the FLRW mode only through the unproven A3 identification (redo A3 fence) |
| `M² = 8` | fibre normal-Laplacian ground eigenvalue `λ_{N,1} = (9/2)² − (7/2)² = 8`, exact ([EXACT-8]) | the OBSERVABLE oscillator mass `M² = (c_f/c_b)λ_{N,1}` — equals 8 only under `ℓ = R_s = c/H₀`, a reconstruction-grade import; `ℓ = 2R_s` gives 2, `R_s/2` gives 32, continuously (DC-H2 SCALE4) | `M²=8` is import-conditional, not native; any packet statement carrying it must carry the import |
| "prediction packet" | the frozen PP1/PP2/PP3 shelf objects (`de-packet-lane-structure-clarification-2026-07-21.md`) | this design packet (a prediction research packet-assembly scaffold) | distinct; this packet does not reopen, rescore, or duplicate PP1-PP3 |
| "XS–S" | an effort grade (council seat idiom) | (misreadable as) a named object | effort grade; the object is the decision typed below |

### GU-COSMO-DYNAMIC-01 source split (`AGENTS.md:85-90`; run for every cosmology object touched)

| row (do not collapse) | object(s) this packet touches in that row | status here |
|---|---|---|
| Einstein tensor | the induced `\|II\|²` Einstein term / LT-GR2 neighborhood | NOT touched; routed only (recovering an Einstein equation does not recover the dynamical mechanism) |
| matter stress-energy | frozen `ω_m h² = 0.1430`, calibrated `Ω_m` | frozen pipeline inputs, external (Planck digits; seat2 §2.1(iii)) |
| constant `Λg` | the constant umbilic `Λ_eff` component at `w = −1` exactly (canon two-component structure) | held distinct from the dynamical sector; no claim moved |
| Weinstein's variable olive/`varpi`/VEV sector | `θ`, the record-current-sourced connection distortion; the record law `Λ = c/√N`; the `Z_U`/`U` gradient sector | THE object of the XS–S decision; everything below concerns this row and its map to the observable row |
| observable cosmology | `w(z)`, the DR2 BAO 13-vector, `w_a/(w₀+1)`, the amplitude-marginalised shape χ² | confrontation surface only; behind the leakage firewall |

## State of the problem, compressed (every line cited)

1. prediction research has no ordinary hourly-eligible internal computation:
   `DE-AMP-DIAGNOSTIC`, `PRED-FLAVOR-RANK`, `PRED-NORM-RANK` are
   `RESOLVED_NO_GO`; `P-OBS-LEG` and `DE-F1-TRIPWIRE` are passive monitors;
   `FIXED-NATIVE-QUANTITY` / `BLIND-QUANTITATIVE-CONFRONTATION` are gated
   on new native structure frozen before target-data inspection
   (`NEXT-STEPS.md` prediction research disposition block, ~line 4820). The current
   cadence is fully occupied by Lane-1 K77 ledger work (v0.175-0.185,
   `NEXT-STEPS.md` head). This is the packet's reason to exist.
2. The DESI exclusion is signal-level only; its mechanism is SHAPE: at
   GU's own θ★-calibrated cosmology the amplitude-marginalised shape χ²
   is +19.3 vs ΛCDM at M²=8; a correctly-shaped CPL model at the same
   amplitude gains −22.8; family-level dAIC +1.9..+3.2 is below the
   decisive line ("excluded AS the DESI signal; unconstrained-but-null as
   a family") (`canon/theta-field-flrw-dark-energy-eos.md:284-313`,
   DARK-ENERGY-07 items 3 and 5). The gap was recomputed on-disk as
   19.346 (`de-pipeline-certification...md` §2.2).
3. `r(N) = κ₀√N` lives in `explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md`
   §3 (Mechanism 2, `N* = (κ*/κ₀)²`) — NOT in the same-label
   `W187-law-shadow-reduction-audit-2026-07-14.md`, which carries zero
   `r(N)` occurrences (both files verified open in this tree; the anchor's
   warning is confirmed). Layer-0: `r` is a coupling ratio; only the
   direction `dr/dN > 0` is GU-native; the exponent is a model (W187
   §5(b)). Reciprocity: `r·Λ = κ₀` constant, machine-checked
   (`W215...md` DS4c, lines 159-161).
4. FIRED tripwires bound the route: monotone `N` gives
   `Λ_mean = c/√N` monotone DECREASING, `Q_mean < 0` for all `a` —
   monotone withdrawal, no zero-crossing (W154 RE1, 25/25;
   `W154...md:110-114`); the `q=5` Krein grading does NOT convert
   monotone accretion into a rise — `N_K = 9f₊ − 5f₋` stays monotone
   (W158 RISEb; `W158...md:145-152`). The rise must be carried by a
   genuine non-monotone fluctuation whose existence, amplitude, and epoch
   are a FREE realization (RISEc), and the crossing epoch is provably free
   (W160 via seat2 E4 — seat2 itself flags E4 as resting on a secondhand
   statement of the 27/27 result; graded SCOPED here).
5. W230 (COMPLETED-POSIT, 24/24): `θ = J` is equivalent to the single
   named axiom `c_kin = 0` (the marble/wood emergence axiom); necessity
   proven for `L` SPD and not proportional to `M`; not derivable from
   Noether II / equivariance / shiab (rank-14 obstruction); coupling sign
   forced positive, magnitude unbuilt (`W230...md` §§2-5).
6. Wave A-2 and its hostile review broke the naive reading: the θ↔B
   identification is UNCERTAIN across five unbuilt maps; a planted
   `L = M` witness (later sharpened to certificate grade with the
   non-proportional preserver `L = M + (Mt)(Mt)ᵀ`) refutes the universal
   finite-fixture iff (`de-pipeline-certification...md` correction banner
   and §2.3; `de-certification-redo...md` [EXACT-RAY]).
7. The redo composed the five arrows: A1 OBS and A2 PULL defined;
   A3 PROJ reconstruction-grade with the frame-vs-coset fence;
   **A4 NORM is the first unbuildable arrow** — the kinetic split
   `(c_b : c_s : c_f)` of the unbuilt native `Z_U = |D_A U|²` (W203's
   ledger row `Z_U` **NOT BUILT**, `W203...md:127`); A5 EQ mechanical
   given A4. [EXACT-K0]: the k→0 homogeneous limit annihilates exactly
   and only the base-spatial sub-block, so seat2's spatial-gradient
   caveat CANNOT decide the question; "bridge fails as stated" is NOT
   licensed; the state is **BLOCKED-ON-A4**, and the cheapest decisive
   move is named: build the `(c_b : c_f)` ratio of `Z_U` on the A3
   configuration — not another fixture (`de-certification-redo...md` §3).
   Conditional consequences already typed: `c_b > 0` generic ⇒ `θ ~ M⁻¹J`
   fails by [NEC]; `c_b = 0` ⇒ the θ sector loses its FLRW oscillator and
   the object M-H13 would refit does not exist (redo §3, "Effect on
   M-H13"). The pipeline itself is now certified unbiased on synthetic
   known-truth injections (de12b, SI-1..SI-6 all passed; register rider:
   M-H13 item (b) DISCHARGED, `improvement-register...md:359-368`).
8. DC-H2 (2026-08-04, 35/35 exact): reciprocity/self-adjointness
   conditions are exactly invariant under the blockwise congruence group
   whose orbits ARE the block ratios — the entire condition class cannot
   supply `(c_b : c_f)`; what A4 needs is a SCALE. The residue reduces to
   exactly one dimensionful number, the gimmel metric's
   horizontal:vertical scale (a length²; the source-datum packet's
   derived line `ℓ² = Z_U κ`); H44's equation is the choice
   `(c_b : c_f) = 1:1` PLUS the reconstruction-grade import `R_s = c/H₀`
   (SCALE4-5). The non-double-bankable fork: full so(9,5) equivariance of
   the kinetic kernel WOULD fix the ratio (Schur, nulldim 1, generator η)
   but forces `L ∝ M`, landing in [NEC]'s escape variety and destroying
   W230's necessity leg; W230's own text takes the not-proportional horn.
   Nullities 1/2/3 for so(9,5) / so(3,1)+so(6,4) / so(3)+so(6,4). One
   recorded disconnect: W230 calls the Gram "equivariant"; W203 KER4
   proves it is not (`dc-h2...md` §§3-6).
9. The written parent action gives θ an ultralocal quadratic term and NO
   fundamental gradient of its own; the gradient sector enters through
   `P_IG = Z_U D_A U`, with `Z_U` CHARGED as a free local action
   coefficient and the `Z_U → 0` limit reducing to the W203 ultralocal
   bridge `θ = κ η⁻¹ J` (`unified-source-datum-packet-v0...md` action
   display, `P_IG` elimination, and §7.2 ledger).
10. TaF constraint on any `N(z)`: the record-that-counts is the
    confirmed/frontier-side access-audited count; a single global scalar
    monotone ledger is T588's refuted contract B; survivors are
    per-observer and regional-reconciling ledgers; the quantitative
    `π√N_bulk` relation has no earned TaF surface and stays a GU-side
    import (mailbox response `20260803-taf-response-records-de-typings.md`
    T2; register absorption at `improvement-register...md:699`).
11. The live external tripwire is the HARDENED FC-d: fires iff any
    admissible combination's 2σ least-negative edge of `w_a/(w₀+1)` is
    below −3.5 (canon F1 exact). Current tightest edge −2.39 (DESY5),
    live margin **+1.11**; the anchor-era "+0.032" was a DESY5-central
    artifact and is SUPERSEDED (W226 title and §; `NEXT-STEPS.md` prediction research
    block). Resolving releases: DESI DR3 (~2027) / Euclid DR1 cosmology
    (~2027). The DESI clock does not tick before 2027 (seat2 §4.3).

## Scaffolding lens 1 — decision typing (the centerpiece)

**The decision, current form.** Decide the fundamental-kinetic status of
the connection distortion on the A3 configuration `θ = B(t)Y₁(y)`:
operationally, (i) whether the native kinetic quadratic form contributes a
nonzero base-time block `c_b`, (ii) whether its 14-frame kernel lies in
the escape variety `L t ∈ span(M t)` (equivalently, whether full so(9,5)
equivariance is imposed, forcing `L ∝ η ∝ M`), and (iii) what supplies the
one dimensionful scale `ℓ² = Z_U κ`. This is the A6 assumption row of the
seat4 envelope, gating C11 entirely (`seat4-envelope.md:74,133`), the
M-H13 rider's item (a) (`improvement-register...md:359-376`), and the
anchor fact's standing instruction.

**The horns** (each stated as: what it asserts / what it implies for the
r(N(z)) refit and the DE route / which artifacts bear on it):

- **H-K (fundamental kinetic, generic).** Asserts `c_b > 0` with kernel
  outside the escape variety. Then `θ ~ M⁻¹J` fails on-shell (W230 [NEC];
  redo [EXACT-RAY] boundary), A6 fails, C11 detaches, the records↔DE limb
  is severed — seat4's own collision row: "Survives with the record
  functional amputated — and JP5 then leaves the envelope with a shape
  constraint and no record mechanism to satisfy it"
  (`seat4-envelope.md:170`). M-H13 dies as a homonym refit; the r(N(z))
  route closes; prediction research's DE content reduces to the frozen character and
  tripwire surfaces plus E1 (+19.3 as a requirement on ANY completion).
- **H-S (strict-induced; marble/wood exact).** Asserts the connection
  carries no fundamental kinetic term at all (`Z_U`-sector contribution
  to `c_b` is 0). Then `θ = J` holds — but the FLRW oscillator is not
  native: H44's `B''` term loses its support, and the θ-sector's
  distance-level phenomenology (Result 1, `M_KK = 2√2 H₀`, `⟨w_B⟩ = 0`,
  the M²-band exclusion apparatus) retypes as a non-native model
  (redo [PIPE] rows; "the object M-H13 would refit does not exist").
  The native DE law reverts to the record law `Λ = c/√N` plus a free
  fluctuation — exactly the territory the FIRED tripwires already fence
  (state item 4): the mean withdraws, the rise realization is free, so no
  packet-worthy quantitative shape prediction exists on this horn either;
  what survives is character + tripwire. High fan-out: canon banners on
  the θ-sector files would be owed (wave-routed, not this packet).
- **H-E (escape variety; equivariance-forced).** Asserts the kinetic
  kernel is `∝ M` (full so(9,5) equivariance imposed, DC-H2 §4). Then
  `θ ~ M⁻¹J` holds for EVERY `c_kin`: the oscillator and the record
  identification coexist, the tension dissolves — at the price of W230's
  necessity leg (the A4 COMPLETED-POSIT re-types to sufficiency-only) and
  of repairing the recorded Gram-equivariance disconnect. The ratio
  `(c_b : c_f)` is Schur-forced to η's block ratio; the remaining
  freedom is the one scale `ℓ`; the r(N(z)) refit becomes schedulable
  conditional on `ℓ` and on the TaF-compliant `N(z)` typing. This is the
  only horn on which the refit revives.
- **H-∅ (structurally free / source-silent).** Asserts the source neither
  fixes `Z_U`'s status nor `ℓ` — the mu_DW pattern ("the scale-covariant
  geometry fixes only dimensionless ratios; the overall scale is
  STRUCTURALLY free", `GEOMETER-VS-PHYSICS-OBJECTS.md` row H24), and
  `Z_U` is already a CHARGED free coefficient in the parent packet. Then
  the decision re-types EXTERNAL-DATUM-GATED: `M² = 8` is permanently
  import-grade, M-H13 stays blocked, and the XS–S question exits the
  schedulable set. That closure is itself a Lane-2 deliverable (it
  converts a recurring "decide this first" instruction into a typed
  external dependency).

**The decisive bounded test** (one wave; both parts; grades set by which
anchors are secured, patterned on the sibling packet's outcome grading):

- **D1 — directed source extraction (Eric-lane typing:
  `SOURCE-CONFIRMS` / `SOURCE-CORRECTS` / `SOURCE-SILENT`).** Against the
  existing verbatim extractions
  (`lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`, the
  2026-07-31 axiom/iceberg reconstructions) and the draft regions they
  index, answer exactly three questions: (a) does any displayed equation
  give the connection distortion / U-sector a fundamental gradient term
  with a fixed coefficient (a `Z_U` value, or equivalently a fixed
  horizontal:vertical scale for the gimmel metric)? (b) does any display
  or statement fix `ℓ` (the fibre radius in base units) independently of
  the `R_s = c/H₀` observational identification? (c) does the source
  state the connection is purely induced (marble/wood as an axiom of the
  displayed action, i.e. the `Z_U → 0` limit as the intended theory)?
  Source language directs and types; it does not substitute for
  construction (`AGENTS.md:72-74`).
- **D2 — the ℓ-parametrized block computation (exact arithmetic,
  P-H29-compliant; independent implementation per the standing assist
  model — DC-H2's SCALE0-5 and the redo's [EXACT-K0]/[EXACT-RAY] are
  designer-side certificates, and the wave re-implements their checks).**
  Build the gradient quadratic form `κ_g(D_A U, *_G D_A U)` on the A3
  configuration under the WRITTEN gimmel metric at `λ_GU = 1/2`
  (`gimmel-dewitt-normalization-ledger...md`), with the one scale `ℓ`
  explicit. Outputs: the block table `(c_b : c_s : c_f)(ℓ)`; the exact
  test whether the induced 14-frame kernel lies in the escape variety;
  the k=0 reduction.
  **Gate (Layer-0, load-bearing):** W230 [NEC]'s stated hypotheses are
  "L SPD and not proportional to M"; the native vertical block has
  signature (6,4) and is NOT positive-definite. Before any horn is read
  off, the wave must either extend the necessity certificate to the
  indefinite-kernel case or return H-INAPPLICABLE on that leg. This is
  the recorded signature fence ([BLK] "an indefinite-time-block variant
  is run as the signature fence", `de-pipeline-certification...md:188-192`),
  promoted here from a preregistered witness to a hard gate of the test.
- **Planted controls (the test is not a resolver if these cannot fire):**
  PC-a reproduce the nullities 1/2/3 (DC-H2 RES); PC-b reproduce
  SCALE4's `M² ∈ {8, 2, 32}` at `ℓ ∈ {R_s, 2R_s, R_s/2}`; PC-c a planted
  fully-equivariant kernel must return `∝ η` AND be auto-flagged as
  necessity-killing (the double-bank alarm); PC-d the planted
  non-proportional preserver `L = M + (Mt)(Mt)ᵀ` must be caught by the
  ray test; PC-e a generic integer perturbation must break the ray with
  an exactly nonzero minor.
- **Kill conditions for the test itself:** if D2's block table turns out
  to depend on the unadjudicated θ↔U identification in a way D1 cannot
  type, the test returns BLOCKED-ON-IDENTIFICATION rather than a horn
  (an honest failure mode, declared now); if the A3 frame-vs-coset fence
  cannot be discharged for the configuration used, the fixture-to-mode
  transport is refused and only frame-level statements are emitted.

**What the test moves (P-H28 compliance).** A named gate either way:
M-H13 item (a) (register), A6 and hence C11 (seat4 envelope), the prediction research
schedulability of the r(N(z)) refit, and — on H-S — a canon-banner
obligation on the θ-sector files. No suffix-descent: one wave, graded
outcomes, no follow-on run without a new named gate.

## Scaffolding lens 2 — calibration-leakage audit (the packet-wide firewall)

Enumerated leak points, each with its firewall:

| # | leak point | mechanism | firewall |
|---|---|---|---|
| L1 | the +19.3 shape target | it is a DESI-DR2-derived number; selecting or tuning a candidate family to approach it is calibration leakage by construction | +19.3 is confrontation-only; it appears in pass/fail criteria (pre-registered per seat2 §2.1(iv)) and never in construction; the E1 export phrasing ("a completion must supply ≈+19.3") is a requirement statement, not a fitting target |
| L2 | the mh13 proxy witnesses (φ = 1.607 / 1.478 / 1.098 / 1.382 / 0.662) | they were produced by OPTIMIZING deformations against the DR2 likelihood (`de-pipeline-certification...md` §2.2) | quarantined: they certify only that the deformation space is nonempty; no candidate family may be chosen for resembling a witness; the constructive burden is stated in that artifact itself ("derive an actual record law ... then ask whether that low-dimensional family reaches one of these shapes with positive constraint surplus") |
| L3 | `f₀ = 0.125`, the M²-band {3,7,8}, `ρ = −0.8` | fits and assumptions (seat2 §1.1; DE-07 item 1) | frozen as pipeline constants and labeled FIT/ASSUMED; never exported as native |
| L4 | `M² = 8` itself | carries the `ℓ = R_s = c/H₀` observational import (DC-H2 SCALE4-5) | every statement carrying M²=8 carries the import label; a "native M²" claim requires D1(b) to return SOURCE-CONFIRMS on `ℓ` |
| L5 | `N(z)` construction | building `N(z)` after seeing the DR2 mean vector, or typing it as a global scalar ledger | `N(z)` is built from the frozen record law + background self-consistently BEFORE any likelihood evaluation; the DR2 MEAN VECTOR is prohibited during construction (the de12b pattern: covariance admissible as instrument model, mean is the signal); typing per-observer or regional-reconciling, with FLRW-homogeneity declared as a condition (TaF T2/T588) |
| L6 | early-physics inheritance | inheriting the `z_start = 30` frozen-density assertion under an N-coupled coefficient | re-run H46C check Q1, not inherit (seat2 §2.1(iii)); frozen list: `r* = 144.43 Mpc`, `z* = 1089.92`, `r_drag = 147.09 Mpc`, `100θ* = 1.04110`, `ω_m h² = 0.1430` |
| L7 | combination row-picking | W226's finding: the W220 headline margin was a DESY5-central artifact | any confrontation scans ALL admissible combinations and propagates the correlation; single-row statistics are not citable |
| L8 | the XS–S decisive test | none: D1+D2 touch no observational data at all | zero-leakage by design; this is why it is the FIRST step |

**Freeze-before-confrontation list** (what the eventual refit wave freezes
in a preregistration file before any likelihood call): the record law and
its exponent; the `N` normalization choice (A7) with its TaF typing; the
instantiation (A: `f₀ → f₀(N(z))` vs B: `M²(N(z))` — physically distinct,
seat2 §2.1(ii)); the value or status of `ℓ`; the pass/fail pair (W129's
`dAIC < +4` escape criterion AND the DE-07 shape metric with the +2 AIC
cost per new parameter); the three-way failure reporting split (bridge
fails / rescue spent / saturation, seat2 §4.1). **Blind list:** the DR2
mean vector; the φ-witness shapes; any DR3/Euclid data on arrival.

## Scaffolding lens 3 — fork-robustness of candidate prediction statements

Live forks carried (pack "Live forks" block, lines 1607-1639):
`SIGNATURE-AMBIENT` (open; a same-day sibling design packet targets it),
carrier split (three options, one unadjudicated), kinematic-vs-physical
carrier (`Π_RS^phys` does not exist), plus the route-local forks: the
escape-variety fork (DC-H2 §4), the orientation/sign readout (PP1), A7,
A8.

| candidate statement | fork-conditionality | rank |
|---|---|---|
| **P-F1** — hardened FC-d tripwire: falsified if any admissible combination's 2σ edge of `w_a/(w₀+1)` < −3.5 (margin +1.11) | ROBUST: the θ-sector lives on the metric fibre, (6,4) under both signature horns (pack line 1613-1618); no spinor-carrier dependence; background-level statement | 1 (already frozen, live, external-clock-gated) |
| **P-CHAR** — W220's four-axis derived character (dynamical / sign-changing phantom-crossing / clock-coupled z=O(1) / amplitude O(1)~H²) | MOSTLY ROBUST with ONE NAMED FORK: the sign-changing axis vs PP1's frozen non-phantom sign (`w(z) ≥ −1` pointwise, R0_COND, "the side of w=−1 is a readout of the transmitted orientation") — two frozen in-repo surfaces sitting on opposite readouts of the orientation fork; any packet statement must name the fork and not collapse it (this packet does not adjudicate it) | 2 |
| **P-RECIP** — `r·Λ = κ₀` constant (W215 DS4c) | ROBUST as an internal structural relation, but CROSS-TYPE (r is bar-(b)-typed): not directly observable; packet-eligible only as a consistency constraint on completions, never as a confrontable prediction | 3 |
| **P-M2** — `M² = 8` ⇒ `M_KK = 2√2 H₀`, `⟨w_B⟩ = 0` | IMPORT-CONDITIONAL (`ℓ = R_s`); also H-S-fragile (on H-S the oscillator is non-native) | 4 |
| **P-RN** — the r(N(z)) low-z shape recovery | FORK-CONDITIONAL THREE DEEP: schedulable only on H-E; then still conditional on A7, A8, and the TaF typing; and surplus-capped by the free realization (lens 6) | 5 (blocked) |

Packet-worthiness rule applied: a statement ships either fork-robust
(P-F1) or explicitly conditional with the fork named in the statement
itself (P-CHAR with the orientation fork; P-M2 with the import; P-RN with
its horn).

## Scaffolding lens 4 — cosmology-statistics requirements

What the DESI-shape confrontation actually requires, from the artifacts:

- The metric is the amplitude-marginalised shape χ² on the byte-verified
  DR2 13×13 likelihood, evaluated at the candidate's OWN θ★-calibrated
  cosmology (gap definition, redo Layer-0 "+19.3" row; on-disk 19.346).
  The low-z concentration (z ≲ 0.5) is where the deficit lives (seat2
  §1.2, E1).
- The pipeline carrying the confrontation is certified unbiased on
  synthetic known-truth injections (de12b SI-1..SI-6, five a-priori
  truths × 400 realizations, all preregistered thresholds passed) — the
  refit inherits that certificate only if it uses the same reduced
  machinery and conventions.
- Monotonicity constraints from the FIRED tripwires: RE1 (mean withdraws:
  monotone `N` ⇒ `Q_mean < 0` always) and RISEb (the Krein-graded trace
  `N_K = 9f₊ − 5f₋` stays monotone under lagged accretion) mean the
  required low-z-GROWING deformation cannot be carried by the record-law
  mean or by Krein grading of monotone accretion; the JP4 lemma extends
  this to every monotone signed readout under accretion-restricted
  reachability, with the escape template priced as rate-dominance
  `5f₋' > 9f₊'` at low z (`de-pipeline-certification...md` T4).
- The TaF typing constraint changes the test design: `N(z)` must be
  per-observer or regional-reconciling; a refit on an FLRW background
  must carry "FLRW-homogeneity coincidence" as a declared condition, and
  the confirmed-count vs bulk-4-volume choice (A7) changes the law
  (`π√N_bulk` covered by `p → p/2` in the N^p family, per the T3
  preregistration).
- Statistical discipline: 2-dof Mahalanobis radii are not 1-D sigmas
  (DE-07 item 1); each new parameter costs +2 AIC; pre-register targets
  before running (P-H28; seat2 §2.1(iv)).
- Literature-grade facts, flagged FOR INDEPENDENT CITATION-CHECK by the
  wave (not certified by this packet): DESI DR2 = arXiv:2503.14738 with
  full five-year results/DR3 expected 2027; Euclid DR1 late 2026 with
  dark-energy results 2027; the everpresent-Λ import is Ahmed-Dodelson-
  Greene-Sorkin PRD 69 (2004) 103523; the DeWitt supermetric trace-flip
  is classical (DeWitt 1967); oscillating-massive-scalar `⟨w⟩ = 0` is
  Turner PRD 28 (1983) 1243.

## Scaffolding lens 5 — tripwires, frozen

Idiom: pre-declared, one-sided, fires on a named observable, margin
tracked, resolving release named. Already FIRED (inherited exclusions —
these bound every candidate below and are not re-litigated):

- **TW-RE1 (FIRED, W154 RE1, 25/25):** any candidate whose low-z rise is
  carried by the monotone mean `Λ = c/√N` is dead.
- **TW-RISEb (FIRED, W158 RISEb, 26/26):** any candidate claiming the
  `q=5` indefinite grading converts monotone accretion into a rise is
  dead.
- **TW-EPOCH (standing prohibition, W160 via E4, SCOPED):** no completion
  may be required to predict `z_x` and none may be credited for matching
  `z ≈ 0.405`.

Live, per candidate:

- **P-F1 kill:** any admissible current-or-future combination excludes
  `w_a/(w₀+1) ≥ −3.5` at 2σ (least-negative edge below −3.5) ⇒ axis A4
  falsified (`B_i > 3 M_Pl` structurally unphysical). Margin +1.11;
  resolving release DR3/Euclid (~2027). Passive monitor; consumes no run
  before data arrive (W242 rule via seat2 §4.3).
- **P-CHAR kills:** W220's pre-declared FC-a (data favor `w ≡ −1`),
  FC-b (data force monotone `ρ_DE`), FC-c (crossing forced at z not
  O(1)) — none currently fire (`W220...md:59-65,100`).
- **XS–S test kills (this packet's route):** D2 certifies `c_b > 0` with
  the kernel provably outside the escape variety on source-confirmed
  coefficients ⇒ the θ=J native bridge is DEAD as stated (H-K lands);
  D1 returns SOURCE-CONFIRMS on strict-induced ⇒ the H44-based M²-band
  phenomenology retypes non-native (H-S lands; the M²=8 "prediction"
  family dies as native).
- **TW-SAT (standing, W187 §5(b)):** `κ_ext` saturating below `r*κ_int`
  kills the DE application AND W187's magnitude discharge together;
  a DE-side failure is still never a bar-(b) failure (typing, seat2
  §4.1 asymmetry).

## Scaffolding lens 6 — constraint surplus, counted (not eyeballed)

Method per the standing operating note (`AGENTS.md:110-159`): count
independent expressible constraints, count free parameters, declare
before consequences, flag independence-rank risk. Counts are
planning-grade (this packet runs nothing); the wave re-counts with a
planted-tested matcher before citing any number.

**P-RN (the r(N(z)) refit as currently posed):**
constraints: C10 (+19.3 shape recovery), W129 escape (`dAIC < +4`)
[rank-risk: same data as C10 — hostile count merges them], FC-d ceiling,
P-RECIP coupling (fixing the r-law fixes the Λ-law), RE1/RISEb structural
compatibility (rise must be fluctuation-borne) = **5 nominal / ≈3
hostile**. Parameters: `κ₀` (equivalently `N*`), exponent `p` (A8), `N`
normalization (A7), instantiation A-vs-B (discrete), the scale `ℓ` (A4
residue), the fluctuation realization (RISEc: existence + amplitude +
epoch — counted ≥ 3, and W160 makes the epoch irreducibly free), the
observer-typing choice (TaF) = **≥ 9**. Surplus ≤ 5 − 9 = **−4** —
NOT packet-worthy as posed, independent of the XS–S outcome.
**Ceiling under maximal resolution:** H-E fixes `(c_b:c_f)` (−1), a
frozen record law fixes `p` and A7 (−2), instantiation frozen by the
`θ = M⁻¹J` reading (A follows, −1), and IF the realization becomes
derived except the epoch (E4's irreducible freedom), parameters compress
to {κ₀, epoch} = 2, giving surplus ≈ +3 nominal. That ceiling is the
honest best case, and reaching it requires deriving the fluctuation
realization — an object W158 RISEc typed as free. The packet therefore
does NOT stake prediction research's precedent on P-RN.

**P-F1:** constraints 1 (the ceiling), parameters 0 (all inputs frozen) =
**+1**. Already banked; this is the lane's currently strongest surplus.
**P-CHAR:** 4 axis-constraints vs ≈2 free (f₀ window; realization) =
**≈ +2 nominal**, with the orientation fork consuming one axis's
independence under a hostile count. Already confronted
(SURVIVES-WITH-TENSION).
**P-M2:** 1 constraint vs 1 import = **0**; not packet-worthy alone.
**The XS–S decisive test:** not a prediction; no surplus is claimed for
it (`SURPLUS-UNCOMPUTABLE` does not arise — the test is a decision
procedure, not a posit).

## First decisive steps (bounded, independently implementable)

1. **STEP-XS (the first decisive step; effort S; zero data).** Execute
   D1 + D2 of the decision-typing lens as one wave, with the indefinite-
   kernel gate, planted controls PC-a..PC-e, and the declared kill
   conditions. Layer-0 precondition: re-run the object table above.
   Moves named gates M-H13(a) / A6 / C11. Deliverable: a horn (or
   H-INAPPLICABLE / BLOCKED-ON-IDENTIFICATION), graded per the outcome
   table, plus the consequence routing.
2. **STEP-FIREWALL (independent of STEP-XS; effort XS-S; zero data).**
   Build the leakage-audit preregistration skeleton for the eventual
   refit: the freeze-list and blind-list of lens 2 as an on-disk
   preregistration template with hard asserts tying it to the frozen
   inputs (the de12b/dch2 repo-tie pattern), including the TaF
   `N(z)`-typing condition line and the seat2 §2.1(iv) pass/fail pair.
   This is buildable before the horn is known and is required on every
   horn that leaves any confrontation alive.
3. **STEP-REFIT (conditional; schedulable ONLY if STEP-XS lands H-E; and
   only through STEP-FIREWALL).** The r(N(z)) refit per seat2 §2.1
   (i)-(iv) with the surplus ceiling of lens 6 stated in the
   preregistration and the three-way failure split reported per seat2
   §4.1. Not schedulable on H-K, H-S, or H-∅ — on those horns prediction research's
   packet content is the fork-robust monitor set (P-F1, P-CHAR with its
   named fork) plus the typed closure statement, which the wave files as
   the lane's honest deliverable.

## Outcome table (graded; every disposition wave-owned)

| STEP-XS result | horn | what moves (wave-routed) | grade |
|---|---|---|---|
| D1 CONFIRMS a fundamental gradient display with fixed coefficient; D2 kernel outside escape variety, `c_b > 0` | H-K | A6 fails; C11 detaches; M-H13 closed as homonym; r(N(z)) route closed; seat4 collision row executes; prediction research packet = monitors + E1-as-requirement | formula grade if the display is verbatim; presumption grade otherwise |
| D1 CONFIRMS strict-induced (marble/wood as the displayed theory; `Z_U → 0` intended) | H-S | θ=J stands as the axiom's shadow; H44 oscillator retypes non-native; canon banners owed on the θ-sector files (two-phase rule applies); M-H13's refit object does not exist; prediction research packet = character + tripwire | formula grade on the source statement; the banner scope is its own hostile-reviewed edit |
| D2 shows the written `*_G` forces the kernel into the escape variety (equivariance imposed) | H-E | W230's A4 verdict re-types sufficiency-only (verdict-flip contract applies: field-specialist hostile review required); Gram-disconnect repair; refit schedulable conditional on `ℓ` + TaF typing; STEP-REFIT unlocks | certificate grade (exact algebra) on the variety membership; the re-typing is the wave's |
| D1 SOURCE-SILENT and D2 shows `ℓ` enters only as the free chart scale | H-∅ | the decision re-types EXTERNAL-DATUM-GATED; M²=8 typed import-permanent; M-H13 stays blocked with the blocker re-typed; the recurring "decide XS–S first" instruction is discharged by closure | presumption grade; the closure statement is itself the deliverable |
| indefinite-kernel gate cannot be discharged | H-INAPPLICABLE | the necessity certificate's scope is narrowed on the record; a new bounded item (extend [NEC] to Krein kernels) is named; no horn is read | certificate grade on the scope narrowing |

## Why the route is stalled (cited)

Three independent stalls, all on record: (1) the FIRED tripwires — W154
RE1's monotone withdrawal and W158 RISEb's negative on the Krein-grading
escape — removed the naive native law's rise before the anchor was ever
written (`W154...md:110-114`; `W158...md:145-152`); (2) the unresolved
tension is now typed BLOCKED-ON-A4: the first unbuildable arrow of the
W230→FLRW composition is the kinetic split of the unbuilt `Z_U`, the k=0
escape is exactly closed, and DC-H2 proved the entire
symmetry/adjointness condition class cannot supply the missing scale
(`de-certification-redo...md` §3; `dc-h2...md` §7); (3) prediction research's own
disposition — "no ordinary hourly-eligible internal computation," passive
monitors only — plus a cadence fully committed to Lane-1 K77 work
(`NEXT-STEPS.md` prediction research block and head). The packet's answer to the stall
is STEP-XS: bounded, data-free, and gate-moving either way.

## Prior art (in-repo enumerated; literature flagged)

Novelty discipline: `python3 lab/process/novelty-check.py` was run from
the repo root on "prediction packet" (25 exact hits), "XS–S decision"
(0 exact — but the effort-grade usage is in four council files),
"Z_U block ratio" (0 exact; near hits are exactly the de-certification
scripts), "gimmel scale source extraction" / "kinetic term draft
extraction" (0 exact; 4000+ co-occurrence hits read in relevant part).
In-repo prior art this packet builds on rather than replaces: the frozen
prediction shelf PP1 (sign; `blockbuster-p1-de-sign-covariance-2026-07-19.md`),
PP2 (matter parity), PP3 (curve family) and the standing rule; the DE
packet lane-structure clarification; CH-COSMO's scale bracket and its
`Z_theta > 0` "never emitted" finding; cb-d's parameterizing-the-unknown;
the Wave A-2 pair and DC-H2 (the decisive-object naming and one-scale
reduction are THEIRS, not this packet's); the seat2/seat4 council files;
the unified source-datum packet (which already charges `Z_U` and derives
`ℓ² = Z_U κ`); W226's hardened tripwire. **What is new here, relative to
those:** (a) the four-horn typing of the decision composed across
W230 + the redo + DC-H2 + the source-datum packet's charge table, with
per-horn consequence routing; (b) the promotion of the recorded
indefinite-block signature fence to a hard gate of the decisive test
(W230 [NEC]'s SPD hypothesis vs the native (6,4) vertical block); (c) the
counted surplus ceiling for P-RN and the resulting decision not to stake
the lane's precedent on it; (d) the assembled freeze/blind firewall
design. Literature anchors named in lens 4 are flagged for the wave's
independent citation-check; none is certified here.

## What this packet does not do

Binds no wave; selects no horn; moves no register row, claim status,
verdict, canon entry, fork, bar, count, H59, or LANE-STATE; touches no
observational data (the DR2 mean vector was not read); reopens no PP
packet; does not adjudicate PP1-vs-W220's orientation fork, the θ↔U
identification, `SIGNATURE-AMBIENT`, or the carrier split; makes no
cross-repo action (the TaF response is consumed as an external datum with
provenance; no new mailbox note is sent); creates no NEEDS_JOE state;
performs no promotion (two-phase rule untouched). It is a scaffold: the
executing wave owns every disposition under the full checking contract.

## Verify status manifest (absorption protocol)

- HEAD pinned: `bdd2c934335e6e534d4e0f9e7f55d7678eb566d8` (2026-08-11
  17:12:35 -0500). All file:line citations were opened in this tree.
  **CONFIRMED.**
- Anchor fact re-verified verbatim at `agent-context-pack.md:1643-1666`,
  including the two-file W187 warning and the TaF bracket. **CONFIRMED.**
- The two W187 files are distinct; the law-shadow audit contains zero
  `r(N)` occurrences (grep count 0). **CONFIRMED.**
- W230's verdict, [NEC] alignments (1.0 exactly at c_kin=0; 0.99655 /
  0.92007 / 0.70318 at 1/10/100), and its stated necessity hypotheses.
  **CONFIRMED** (file opened; test not re-run — cited at recorded
  strength).
- The A1-A5 composition ledger, [EXACT-K0], [EXACT-RAY], BLOCKED-ON-A4,
  de12b SI-1..SI-6 PASS, and the register riders (item (b) discharged,
  item (a) sharpened). **CONFIRMED** (files opened; scripts not re-run).
- DC-H2 outcome (c), the condition-class exclusion, the one-scale
  reduction, SCALE4's `M² ∈ {8,2,32}`, the equivariance fork, the Gram
  disconnect. **CONFIRMED** (file opened; script not re-run).
- DARK-ENERGY-07 items 1-5 and the +19.3 / −22.8 pair.
  **CONFIRMED** (`canon/theta-field-flrw-dark-energy-eos.md:284-313`).
- W154 RE1 / W158 RISEb FIRED statements. **CONFIRMED** (both files
  opened at the cited lines).
- W215 DS4c reciprocity. **CONFIRMED** (lines 159-161 opened).
- W220 FC clauses and W226's superseding margin +1.11.
  **CONFIRMED** (both opened; the anchor-era +0.032 is superseded).
- TaF T588 per-observer/regional constraint. **CONFIRMED** against the
  mailbox file (outside this repo; provenance noted) and its register
  absorption (`improvement-register...md:699`).
- W160's 27/27 epoch-freedom result. **SCOPED** — cited via seat2 E4 and
  W158, which flag it; the file itself was not opened here.
- E1's "concentrated at low z" phrasing. **SCOPED** — seat2's synthesis
  of DE-07 item 3; the canon text says "too little low-z evolution."
- The surplus counts of lens 6. **PROPOSED** — planning-grade counts,
  declared method, wave re-counts with a planted-tested matcher.
- The four-horn typing, decisive test design, outcome table, and
  firewall design. **PROPOSED** — design content; the cadence schedules
  STEP-XS or declines with reasons per the absorption protocol.

## Self-hostile review

Filed separately per repository convention: `lab/process/hostile-reviews/2026-08-11-lane2-prediction-packet-design-review.md` (the three standing charges, same-run).
