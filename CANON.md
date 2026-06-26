---
title: "Project Canon"
status: canon
doc_type: canon
updated_at: "2026-06-25"
---

# Project Canon

Canon means: safe to cite as the current public spine of the project. It does not mean proved physics.

## Canonical Posture

This repository is a Geometric Unity reconstruction program. Its working hypothesis is
that GU is substantially correct, and its objective is to determine whether that
hypothesis can be rigorously reconstructed, extended, or falsified through systematic
mathematical research.

This is not a proof of Geometric Unity. It is not a claim that Eric Weinstein's existing
presentation is complete, and it is not a claim that every current reconstruction is
correct.

See `RESEARCH-POSTURE.md` for the canonical research philosophy.

## Canonical Claims

1. **GU reconstruction is the primary mission.** Assume GU is substantially correct as a
   working hypothesis and try to reconstruct the missing mathematics, derivations,
   physical reductions, categorical language, and analytic machinery.
2. **Constructive obstruction discipline.** When a branch blocks, ask what object,
   stronger structure, richer category, or invariant would remove the obstruction before
   deciding whether the obstruction is intrinsic.
3. **No-go theorem discipline.** The target no-go families must be handled through their
   exact assumptions, known class exits, and failure modes.
4. **Specification before promotion.** Any candidate path must state its substrate,
   observer, pairing, causal order, emergence class, coordination loop, source-to-shadow
   map, or equivalent proof object before making physics claims.
5. **Finite control first.** Type II1 or non-embeddable spectral Standard Model ideas must
   preserve the finite Connes-Chamseddine control case before they can claim relevance.
6. **Independent mathematics is Mission B.** Tools such as signed-readout, six-axis
   specification, no-go class-relativity, and reconstruction methodology are valuable
   secondary outputs, but they do not replace the GU reconstruction mission.
7. **Falsification remains success.** Clean falsification, narrowing, or demotion of a
   path is a successful contribution.

## Canon Documents

- `RESEARCH-POSTURE.md`
- `canon/no-go-class-relative-map.md`
- `canon/six-axis-specification-protocol.md`
- `canon/type-ii1-spectral-sm-checklist.md`
- `canon/shiab-existence-cl95.md`
- `canon/dark-energy-theta-divergence-free.md`
- `canon/w2-y14-spin-structure.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `canon/theta-field-flrw-dark-energy-eos.md`
- `specifications/six-axis/`
- `specifications/type-ii1-spectral-sm/`

## Canon Entries Added 2026-06-23

| entry | verdict | source explorations |
|---|---|---|
| `shiab-existence-cl95.md` | RESOLVED (existence only) | n1-signature-audit + n2-shiab-computation (2026-06-22); CORRECTION SHIAB-01 (2026-06-25): proves existence of one natural real-linear Spin(9,5)-equivariant Clifford-contraction map only; injectivity, rank/kernel, uniqueness, source-forced selector identity, anomaly cancellation, and generation count are not included |
| `dark-energy-theta-divergence-free.md` | CONDITIONALLY_RESOLVED | dark-energy-divergence-free-proof + dark-energy-noether-closure (2026-06-22); CORRECTION DARK-ENERGY-01 plus 2026-06-25 consistency sweep: downgraded from RESOLVED — Assumption 3 (structural identification) is reconstruction grade and unproved; C1+C2 is a cross-check, not an independent Noether route |
| `w2-y14-spin-structure.md` | CONDITIONALLY_RESOLVED | n6-w2-y14-gysin-spin-structure (2026-06-22); CORRECTION W2-01 (2026-06-26): unconditional spin claim RETRACTED — Step 3 dropped a w2(V) term, so w2(Y14)=pi*w2(X4), i.e. Y14 spin iff X4 spin (non-spin for CP2); orientability w1(Y14)=0 unaffected |
| `schwarzschild-weak-field-rfail.md` | CONDITIONALLY_RESOLVED | rfail-schwarzschild-oq2-weak-field (2026-06-23) |
| `theta-field-flrw-dark-energy-eos.md` | OPEN | theta-field-flrw-eos (2026-06-23); CORRECTION DARK-ENERGY-02 (2026-06-26): re-downgraded CONDITIONALLY_RESOLVED -> OPEN — only parameter-free prediction (ratio +1.17) is sign-inconsistent with DESI (w_a=-0.75); w_a sign has two undismissed IC candidates; re-elevation was a process milestone. Structural EOS machinery stays reconstruction-grade |

## Not Yet Canon

These remain exploratory until formal obligations are met:

Before promoting any item from this list, run
`process/runbooks/claim-status-consistency-quality-workflow.md` and update all owner
surfaces that might still carry a stronger historical verdict.

- Anomaly cancellation for Sp(64) — Nguyen's U(128) anomaly pincer is defused by the Sp(64) replacement, but full GU anomaly cancellation is OPEN / not canon: local 14D anomaly requires an explicit I_16/index-density computation for the actual chiral field content; global anomaly requires a spin-bordism/Dai-Freed/eta check, not only pi_15(Sp)
- C_MPR as a category
- the 9-tuple as a complete invariant
- PCP-blindness
- BvN/Classical-Value-Lattice Wall as universal obstruction
- stochastic, Sorkin, RG, CA, bicategorical, and layer-split applications
- Three-generation count (analytic index ind_H(D_gimmel) on non-compact Y14)
- Velo-Zwanziger constraint for GU spin-3/2 sector
