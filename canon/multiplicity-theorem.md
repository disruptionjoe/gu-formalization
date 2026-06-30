---
title: "The Multiplicity Theorem: GU fixes one generation's structure but not the count"
status: canon
doc_type: theorem
verdict: "ESTABLISHED CONDITIONALLY (firewall / under-determination form, proof-grade within enumerated GU-native object classes; evidence-grade as a universal statement). The positive canonical-external-index form is OPEN / partially refuted."
established: 2026-06-28
tests: "tests/generation-sector/{signature_sweep_fast,signature_77_rerun,step9_selfdual_connection_index,leg3_external_base_characterization,leg4_branching_multiplicity_search}.py"
---

# The Multiplicity Theorem

> **SUPERSEDED (2026-06-28)** by `papers/drafts/generation-multiplicity-vs-chirality-2026-06-28.md` and the
> corrected results in `canon/h2-base-index-chirality.md`, `canon/leg3-closure-and-spinor-2smoothness.md`,
> and `canon/ghost-parity-krein-synthesis.md`. Retained for the correction record. The sharp "count = 3 iff
> import the prime 3" framing and the 1664-implies-multiplicity argument are RETIRED.

This is the round-3 result of the firewall-hypothesis program (`canon/firewall-boundary-hypothesis.md`)
and the publishable core of the generation-sector campaign. It states precisely what GU's internal data
does and does not determine about matter.

## Statement

> Let GU's RS sector be reconstructed as the Clifford-algebraic / signature-class data of a `Cl(p,q)` with
> `p+q=14` (spinor dimension `2^7 = 128`) carrying the verified Pati-Salam `Spin(2k)` chain. Then GU-internal
> data **determines the STRUCTURE of exactly one Standard-Model generation** (the 16 of `Spin(10)`: right-
> handed neutrino, anomaly-free, charges `{0,+/-1/3,+/-2/3,+/-1}` -- the verified Pati-Salam result) but does
> **NOT fix the generation MULTIPLICITY.** The multiplicity is a free integer of the internal data: across
> every GU-native object class it is either (a) a module dimension or branching multiplicity, which is
> `{2,7,13}`-smooth (a power-of-2 half-spinor dimension of the commutant) and so can never equal an odd prime,
> in particular never 3; (b) a metric `so(p,q)` connection index, which is identically 0; or (c) a free,
> operator-dependent carrier rank that nothing internal pins.

**Equivalent sharp form.** The integer 3 is prime and divides no GU-internal Clifford dimension or
branching multiplicity (all `{2,7,13}`-smooth). Therefore **"the generation count is 3" is exactly
equivalent to importing the prime factor 3 from outside** the internal algebra. GU gives the shape of a
generation; the number of copies must come from elsewhere.

## Proof-grade core (within the enumerated GU-native object classes)

1. **The count is not a GU-native dimension or branching multiplicity (independently confirmed).** The
   family rep on the `Spin(14)` spinor is always a `Spin(2k)` half-spinor of dimension `2^(k-1)`, a power of
   2. An exhaustive branching search (Leg 4: all 21 maximal-rank D5 splits x the 5 native reps
   `{64, 64bar, 128, 14, 91}`) found **0** cases giving a multiplicity or net-chiral count of 3. And the
   constraint-surface dimension is **structurally** `ker(Gamma) = (14-1)*128 = 1664 = 2^7 * 13` for ANY
   signature (Gamma is surjective onto `C^128` because every gamma is invertible), so the native dimension
   spectrum is `{2,7,13}`-smooth and 3-free with no computation needed. INDEPENDENTLY VERIFIED here across
   9 signatures spanning both module classes (`signature_sweep_fast.py`): `(9,5),(10,4),(5,9),(14,0),(13,1)`
   [H-class, `J^2=-1`] and `(7,7),(8,6),(11,3),(12,2)` [real class, `J^2=+1`] all give `rank(Gamma)=128`,
   `ker=1664=2^7*13`, prime 3 absent, with `J^2` sign tracking `p-q mod 8` exactly.
2. **The count is not a metric-connection index.** Every metric `so(p,q)` connection gives generation index
   0: under `(9,5)` this is closed for all 91 generators by the phase-unique particle-hole certificate
   (`step9`), and it reproduces (=0) under the real `(7,7)` class (`signature_77_rerun.py`).
3. **The lone internal pin was a signature artifact.** The C-07 quaternionic-parity (Kramers) wall, which
   alone ever forced anything about the count, exists only for H-class signatures (`J^2=-1`); under the
   real `(7,7)` class `J^2=+1`, there is no Kramers wall and the rank is fully free. So even the one
   internal constraint dissolves under a defensible alternative signature.

## What is NOT closed (why conditional, not absolute)

- **Universality is evidence-grade.** "No OTHER class of GU-internal invariant fixes the count" is asserted
  over a finite catalog (dimensions, branching multiplicities, regular-commutant embeddings, metric-
  connection indices, degree-0 ratio invariants), not proven exhaustive.
- **C-05 is finite-sample per signature** plus the one closed `so(9,5)` certificate, not yet a genuine
  families / spectral-flow index theorem over the full orbit (FamiliesIndexPushforwardGate open).
- **Leg 4's no-horizontal-SU(3)** exclusion is dimension-count grade for regular embeddings
  (`dim su(3)=8 > dim` commutant `su(2)+su(2)=6`); non-regular / principal `su(2)` embeddings not brute-forced.
- **Honest appearance of 3 (flagged, not suppressed):** `|Weyl(D7)| = 2^10 * 3^2 * 5 * 7` contains the prime
  3, but it is a Weyl-chamber / group-order count, not a generation multiplicity.

## Firewall implication

The firewall's WEAK form HOLDS and is reinforced to a (conditional) theorem: the internal Clifford /
signature sector is sealed off from fixing the family count -- every internal integer is `{2,7,13}`-smooth
and every metric-connection index vanishes, so a multiplicity of 3 is unreachable from inside and is exactly
equivalent to importing the prime 3. This is stronger than rounds 1-2: the obstruction is now shown across
all even-signature module classes, not a `(9,5)`+`(7,7)` coincidence.

The firewall's STRONG / POSITIVE form (the count = a single canonical EXTERNAL topological index that GU
forces) does NOT hold and is partially refuted. GU fixes the signature (`p-q=4`), which points at the
metric-fiber base `GL(4,R)/O(3,1) ~ RP^3`, whose torsion is 2-primary and hence provably 3-FREE; the only
3-carrying base (the K3-end) is an unforced import whose honest characteristic class is
`ch2(S_X)[K3] = -5376`, with the clean `24` and the `/8` normalization target-fitted. GU pins neither the
base, the value, nor the normalization. So the honest firewall reading is: **GU explains the SHAPE of one
generation; the NUMBER three is neither computed internally nor cleanly reduced to a single GU-forced
external invariant -- it is imported.**

## What would finish it (round 4 / publication-hardening)

1. Close universality: prove every degree-0 GU-internal invariant is necessarily a `{2,7,13}`-smooth
   dimension/branching multiplicity or a vanishing metric-connection index (no third class).
2. Upgrade C-05 to a families/spectral-flow index theorem over the full `so(p,q)` orbit and fiber.
3. Brute-force the non-regular/principal `su(2)` embeddings to retire the horizontal-`SU(3)` gap at
   proof grade.
4. Publish the NEGATIVE (firewall / prime-sieve) theorem; do NOT claim the canonical-external-reduction.

## Reproducibility

`tests/generation-sector/signature_sweep_fast.py` (9-signature ker/prime/parity sweep, fast),
`signature_77_rerun.py` (the (7,7) re-run), `step9_selfdual_connection_index.py` (connections -> 0 under
(9,5)), `leg3_external_base_characterization.py`, `leg4_branching_multiplicity_search.py`. Anchors hold in
all: bare `||[Pi_RS,M_D]|| = 58.7215`, `C2 = 155.3625`, Clifford error 0.
