---
title: "S_IG/B.5 F2/F5 shadows: the two-section structure EXISTS at toy grade (F2 does not fire); the C2 magnitude test is theorem-blind at symbol grade while the Krein-signed accounting co-flips exactly (F5 not fired, not discharged) — plus a new machine-exact master identity of the C2 density"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (big-swing orchestration: S_IG/B.5 stakes)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/sig-b5-habitat-verification-2026-07-20.md
inputs:
  - explorations/sig-b5-habitat-verification-2026-07-20.md
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
  - explorations/pt3-w229-membership-audit-2026-07-19.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/channel-swings/sig_b5_habitat_probe.py
  - tests/channel-swings/pt3_w229_membership_probe.py
  - tests/channel-swings/ch_src_minimal_action_toy.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/oq_rk1_cl95_explicit_rep.py
runnable:
  - tests/channel-swings/f2_shadow_two_section_probe.py
  - tests/channel-swings/f5_shadow_c2_flip_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# S_IG/B.5: the two named computations, run

The habitat swing left the P5 candidate's live stakes on exactly two named
computations: F2 (does the two-section structure exist over the proven
generator loop, or is the classifying invariant trivial?) and F5 (does the
C2 accounting respond to the holonomy-sector flip, or is the carrier
coherent but irrelevant?). Both are now built and run at toy/shadow grade
on the ACTUAL W229 objects. Receipts: two deterministic probes, both exit 0:

- `tests/channel-swings/f2_shadow_two_section_probe.py`
  — HEADLINE `11 [E] + 4 [F] = 15 (setup [T] = 3 excluded)`.
- `tests/channel-swings/f5_shadow_c2_flip_probe.py`
  — HEADLINE `6 [E] + 3 [F] = 9 (setup [T] = 3 excluded)`.

## Headline results

**F2 shadow: the two-section structure EXISTS; the kill does not fire.**
Over the machine-proven mixed-plane generator loop (frame trivialization,
seam holonomy U_h = e_0 e_9, which reproduces the proven K_S -> -K_S
transport endpoint exactly), the native Dirac-family shadow
D(t) = c(A_t xi) is K_S-self-adjoint, J_quat-commuting, seam-covariant, and
gapped along the whole loop (q(t) in [28.13, 30.31]). Its canonical
Krein-compatible cuts — maximal K-definite, D-invariant, half-rank,
Krein-orthogonal splittings — exist at every point of the loop (Gram
signature exactly (32,32), definiteness margin >= 0.84, never degenerate),
and the machine identities

    Q_+(1) = U_h Q_-(0) U_h^{-1},   Q_-(1) = U_h Q_+(0) U_h^{-1}

hold to 1e-15: the monodromy of the canonical cut IS the deck exchange.
Neither cut descends to the base loop (descent gap O(10)); both close on
the double cover (U_h^2 = I exactly). The K-sign of an admissible cut is a
continuous plus/minus-valued invariant with bounded margin, so the two
sections are not homotopic through admissible cuts: the classifying set at
this grade is exactly Z/2, NONTRIVIAL. This is the dossier 1.3 structure
("two Krein-compatible spectral sections exchanged by the deck
transformation") realized as matrices, upgraded from posited shape to
NATIVE-PROVEN at toy grade.

**F5 shadow: not fired, not discharged — and the falsifier itself is
sharpened.** In the end-model where the sector datum enters as the boundary
condition (cut projector) on the output leg of the real obstruction map
X = Gamma M_D Pi_RS (real anchors reproduced: bare 58.7215, C2 155.3625):

- the MAGNITUDE accounting is exactly invariant under the sector flip
  (r_+ = r_- = 129.2640; full singular-value spectra coincide to 1e-15) —
  but this invariance is THEOREM-FORCED, not evidence. It follows from a
  new machine-exact master identity of the obstruction density (below) and
  holds for EVERY Krein-orthogonal half-splitting, including a seeded
  random one. An invariance that holds for every splitting has zero
  discriminating power about this carrier: **the F5 magnitude test is
  structurally incapable of firing at symbol grade.** (It is also exactly
  the invariance SRC-REJ-1 demands: symbol-level data must not move C2.)
- the KREIN-SIGNED accounting responds exactly: k_sigma = sigma x
  14421.0033 (|k|/C2^2 = 0.5975 — a large resolved fraction of the
  obstruction content), zero-sum, and holonomy-tied: flipping the sign is
  literally "transport the boundary condition once around the mixed loop"
  (deck identity), while the same operation around a same-sign-plane loop
  changes nothing at machine precision, and the fully covariant frame
  dressing changes nothing either (trichotomy + frame-artifact controls).

So the carrier is NOT inert in the C2 accounting: its footprint at symbol
grade is relational (sign), not absolute (magnitude) — the C2-level image
of the storable-but-locally-unreadable typing. The decisive F5 test remains
an N2-grade computation, exactly where the dossier filed it.

**New exact structure (surprise of the swing).** The C2 obstruction density
A = X X^+ satisfies, machine-exactly (residual 3e-13 against norms ~4e3),

    A + K_S A K_S = (C2^2 / 64) I        and so        tr(K_S A) = 0.

The K_S-even part of the C2 density is pure scalar. This single identity
forces the magnitude blindness for every Krein splitting and the exact
equal-and-opposite signed split. Its derivation is OPEN (a named short
computation: presumably a gamma-tracelessness/Fierz argument on the
Gamma...Pi_RS block structure); until derived it is typed NATIVE-PROVEN
(matrix grade, this xi) with mechanism underived.

## Council pass (inline, five lenses, compact)

- **Spectral geometer:** the F2 shadow is the M1+M2 rungs on the real loop,
  not the N2 theorem: the "boundary Dirac family" is the transported
  SYMBOL, the base is one loop (not the full non-compact fiber), and the
  classifying computation is finite. What it establishes: nothing in the
  Krein/quaternionic structure of the actual W229 objects obstructs the
  two-section geometry — the obstruction candidates that could have killed
  it (Gram degeneracy, gap closure, descent) were all computed and all
  land on the alive side. The N2 question (the actual end family) is
  narrowed, not answered. Also note: the plain spectral cut DESCENDS — a
  team using the positive-Hilbert APS default would see no datum and could
  wrongly report triviality; the fork discipline did real work here.
- **Topological-QFT theorist:** sector count stays TWO; the classifying
  invariant realized is the expected Z/2 (deck action on definiteness
  classes), with the trichotomy exact: monodromy fires on mixed loops
  only. No anyon/TEE language imported; the "spectral section" vocabulary
  is IMPORTED-shape as before. The signed zero-sum split (k_+ + k_- = 0)
  is the correct flat-Z/2 phenomenology: no absolute charge, only a
  relational orientation of the pair.
- **Condensed-matter theorist:** Kramers did exactly what the blindness
  derivation predicts, now at the accounting level: J-commuting probes are
  doubly degenerate (checked at 128-dim, including the Gram spectra), the
  odd rank-1 reader has J-defect 1, the null-cone crossing has EVEN
  (64-dim) kernel, and the only sector-sensitive readout is relational.
  The bit's VALUE remains externally posited; nothing here reads it. The
  magnitude-blindness theorem is the strongest form yet of "no GU-native
  absolute readout": it is not merely that no probe was found — the
  channel is closed by an exact identity.
- **Category theorist:** one datum, consistent costumes: the deck exchange
  (F2 probe) = the anchor exchange (habitat probe) = the sign flip of the
  signed C2 split (F5 probe) — verified as the SAME U_h on the same
  objects, so no new payload item appears; N-accounting unchanged (core 3,
  ceiling 4, triggers intact). The F5 refinement discharges a typing debt
  in the dossier: falsifier F5's "identical C2 accounting" clause must be
  read as excluding symbol-grade magnitude tests, else it is vacuously
  triggered by a theorem that holds for every splitting. That is a repair
  to the falsifier's operational form, not to its intent.
- **Buildability engineer:** total cost: two probes, no new mathematics
  consumed. Cheap follow-ups now exposed: (i) derive the master identity
  (short, symbol-level, high value — it is a new exact statement about C2
  itself); (ii) the M2 scale-dial leg (lambda_0 as the only dimensionful
  datum of a cut) was NOT built here and remains the cheapest untouched
  rung; (iii) the N-rungs stand unchanged as the real frontier (N1
  pushforward, N2 actual end family, N3 weld).

## What moved and what did not

Moved (working grade only, R0_COND, conditional on the standing axiom):

1. F2 at toy grade is DECIDED on the alive side: the two-section structure
   exists on the actual W229 objects over the proven loop, deck-exchanged,
   Z/2-classified, machine-exact. Dossier 1.3's boxed two-section claim:
   NATIVE-PLAUSIBLE -> NATIVE-PROVEN (matrix grade, toy family).
2. F5 at symbol grade is shown to be the WRONG GRADE for the magnitude
   form of the test (theorem-blind channel), and the signed channel is
   shown load-bearing and holonomy-tied. F5 stays open at N2 grade, now
   with a sharper operational form: a faithful end-model must consume the
   sector through the Krein-signed channel.
3. New exact identity A + K_S A K_S = (C2^2/64) I (with tr K_S A = 0),
   mechanism underived — a named open computation.
4. The candidate has now survived every falsifier that is runnable below
   theorem grade: F1, F3 (habitat swing), F2-toy, F5-symbol (this swing).
   Its stakes sit entirely at N1-N3 plus the F4 double edge.

Not moved: no claim status, no canon verdict, no scorecard row, no public
posture, no N-accounting change. Nothing here builds S_IG, the actual
boundary Dirac family of the non-compact end, the families pushforward, or
the BV weld; the bit's VALUE remains externally posited (p2c-owned); the
scale element (including M2's lambda_0 dial) is untouched; Door B is
untouched. The kills that did not fire are construction-local results at
toy grade, not global verdicts — and symmetrically, the survivals are not
existence proofs at N2 grade.

## Typed claims

NATIVE-PROVEN (matrix grade, this swing; IMPORTED-standard steps named in
the probes: the covering step and the "continuous +-1 invariant separates
path components" step):

- Two-section existence over the generator loop for the native symbol
  family: cuts exist everywhere, deck-exchanged exactly, non-descending,
  double-cover-closed, Z/2-classified. (F2 probe, 11 E + 4 F.)
- Master identity and corollary tr(K_S A) = 0; magnitude blindness for
  every Krein-orthogonal half-splitting; exact signed co-flip with
  trichotomy and frame-artifact controls. (F5 probe, 6 E + 3 F.)
- Kramers evenness of J-commuting Hermitian probes at 128-dim, with J_quat
  now in closed form (subset product of JW gammas; J^2 = -I exact).

OPEN (named): derivation of the master identity; the actual N2 boundary
family and its section classification; N1 pushforward; N3 weld; the M2
scale-dial leg; the F5 decisive test at N2; Door B property P.

## Falsifier ledger (dossier Section 6, updated at this grade)

- F1 habitat: did not fire (habitat swing).
- F2 existence: did NOT fire at toy grade — two-section structure exists;
  N2-grade existence still open. Verdict is native-fork-local: the
  standard positive-Hilbert cut sees no datum (recorded in the probe); a
  triviality claim derived on the standard fork would not transfer.
- F3 twist: did not fire (habitat swing).
- F4 blindness (double edge): untouched; the odd-reader control
  re-corroborated (rank-1 J-defect = sqrt(2) at 128-dim).
- F5 relevance: NOT fired, NOT discharged; operational form repaired —
  magnitude invariance at symbol grade is theorem-forced and evidentially
  null; the signed channel responds exactly and is the channel a faithful
  end-model must use.
- F6-F8: untouched; SRC-REJ-1 re-verified as a guard (no dressing reduces
  C2 at symbol level).

## Receipts

- Probes (deterministic, numpy only, seeded 20260720, both exit 0):
  `tests/channel-swings/f2_shadow_two_section_probe.py`,
  `tests/channel-swings/f5_shadow_c2_flip_probe.py`.
- Objects: verified Cl(9,5) = M(64,H) rep via
  `tests/generation-sector/gen_sector_bridge.py` /
  `tests/oq_rk1_cl95_explicit_rep.py`; K_S, loop, transport identical to
  `tests/channel-swings/sig_b5_habitat_probe.py`; anchors 58.7215 /
  155.3625 reproduced in-probe.
- Dossier under test:
  `explorations/blockbuster-p5-instance-dossier-2026-07-19.md` (Element 1
  sec. 1.3, Element 5 rungs M1/M2, Element 6 falsifiers F2/F5).
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` — both cut
  forks computed; every load-bearing object's construction named in the
  probe headers; killed list honored (C2 treated as a norm, never an
  index; no eta-based count; no positive-Hilbert default).

## Boundary

Exploration tier under the standing axiom, R0_COND working grade. The F2
result is a toy-grade shadow: one loop, the symbol family, finite
classification — it narrows but does not answer B.5(ii)/N2. The F5 result
closes the symbol-grade magnitude route honestly rather than pretending to
run the N2 test. The master identity is verified for the frozen xi and the
mixed-plane loop family at machine precision; its generality and mechanism
are open. No claim-status, canon, scorecard, or posture movement; no
cross-owner writes; no external actions. Next rungs in order of exposure:
(i) derive the master identity; (ii) the M2 lambda_0 scale-dial toy;
(iii) N1-N3 as named, with F5's decisive form waiting at N2.
