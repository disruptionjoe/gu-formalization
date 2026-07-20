---
title: "Sector-relative spectral-section theory, prototyped at truncated-real grade on the faithful Y14 end: the section symbol M = Ku D (gauge-rigid, entire across the walls, M^2 = qI, deck-odd) makes the definition decidable; sections EXIST on gapped, crossing, undecided rays and at the boundary-at-infinity, wall-matched by q+i0 continuation; K-c FIRED -- classification is exactly Z/2 (the deck twist) at this grade, with the +-i0 orientation bit typed as the m1 scheme gauge (the only K-d shadow, operator-grade); the EP collapse law gets its closed form (margin = sqrt(q/P), r = sqrt(-q/T): one rate); F5's real accounting provably does NOT extend past the wall (Re k = 0 exact) while its imaginary width channel does"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (sequential tail: section-theory prototype)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/n2-end-family-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
inputs:
  - explorations/n2-end-family-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/f5-signed-fraction-2026-07-20.md
  - explorations/master-identity-mechanism-2026-07-20.md
  - explorations/araki-scale-route-2026-07-20.md
  - tests/channel-swings/n2_end_family_probe.py
  - tests/channel-swings/m1_third_reading_probe.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/sector_relative_section_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

> **CORRECTION (2026-07-20, second dry round — verify-section-theory-2026-07-20.md, commit 5afb44b).**
> The census sentence in the classification section ("EXACTLY eight
> involutions") is FALSE AS STATED: the crossed-fiber commutant algebra is
> C^4 with SIXTEEN involutions (a ninth exhibited machine-exactly). The
> correct and sufficient statement, proven symbolically in the verify
> pass: the K_S-SKEW involutions are exactly +-d~ and +-J_c, and the
> remaining eight are neither K_S-skew nor half-splittings. The Z/2
> classification, existence, wall-matching, and all downstream
> consequences are UNAFFECTED. Original text below retained unedited per
> record discipline.

# The sector-relative section theory, built

N2 named the missing mathematics precisely: no spectral-section theorem
covers a boundary family whose symbol changes Krein type across the end
(gapped rays / cone-crossing rays with Krein collisions / a K-null
timelike regime). M1 supplied the candidate wall treatment: a conserved,
K_S-derivable, deck-compatible indefinite pairing across the walls, with
a universal-null lemma and an exceptional-point collapse law. This swing
builds the object both pointed at: a DEFINITION of "sector-relative
Krein section" precise enough that existence and classification are
decidable, an existence proof at matrix grade on the actual faithful end
model, and the classification -- with the pre-declared kill conditions
adjudicated.

Receipt: `tests/channel-swings/sector_relative_section_probe.py` --
deterministic (two runs byte-identical), numpy only, seeded 20260720,
exit 0 -- HEADLINE `16 [E] + 4 [F] = 20 (setup [T] = 3 excluded) ALL
PASS`.

**Verdict up front: K-c FIRED.** Sector-relative sections exist on the
full end (domain P > 0), including across the crossing rays, through
the walls and t-holes, and at the boundary-at-infinity; the
classification at truncated-real grade is exactly Z/2, the standing
deck twist -- the two-section structure extends to the WHOLE end. K-a
did not fire (wall matching has a continuous, gauge-invariant, unique
formulation); K-b did not fire (the datum never trivializes). The one
honest K-d shadow -- the +-i0 orientation bit -- is proven J-conjugate
and identified with M1's decay-orientation gauge: scheme, not data, at
this grade; whether operator grade promotes it is part of the residual
N2 gap spec (Section 7). No claim, canon, scorecard, or posture moves.

## 1. The discovery that makes the definition decidable: the section symbol

Everything rests on one derived object. For the K_S-self-adjoint family
D(t,s), define (from {D, K_S} ALONE -- no frame, no xi-components):

    c_s := (D + K_S D K_S)/2        (the Hermitian part = the space part)
    c_t := (D - K_S D K_S)/2        (the anti-Hermitian = time part)
    P := tr(c_s^2)/128,  T := -tr(c_t^2)/128,  q = P - T  (the Krein norm)
    Ku := K_S c_s / sqrt(P)         (a Hermitian traceless involution)
    M  := Ku D                      (THE SECTION SYMBOL)

Little theorems, all unconditional algebra machine-corroborated at
gapped, crossed, and wall points of the actual family ([E] receipts):

- **[Ku, D] = 0** and **M^2 = q I** at every regime -- on the gapped
  side M/sqrt(q) is an involution, past the wall M/(i g) is (g =
  sqrt(-q)), and AT the wall M is nilpotent (M^2 = 0, rank 64,
  Ker M = Range M = Ker D: exactly the m1 Jordan structure).
- **M is K_S-self-adjoint, commutes with D, and is LINEAR in D** --
  hence entire across the walls, where every eigenprojection blows up.
  The wall singularity of the section problem is relocated ENTIRELY
  into one scalar normalization.
- **Gauge rigidity (two lines):** if [G, D] = [G, K_S] = 0 then G
  commutes with c_s, hence with Ku and M. Every K_S-preserving symmetry
  of the family fixes the symbol; frame/gauge redefinitions act
  trivially. Only Krein ANTI-isometries flip it: the out-of-plane mixed
  involution V = c_m c_tau (commutes with D, sends K_S -> -K_S) sends
  M -> -M -- the deck's character, pointwise. This kills the
  "relabeled bookkeeping" reading: M is forced, and the only moves that
  exchange section data are K_S-reversing.
- **M is DECK-ODD:** U_h M(0,s) U_h^-1 = -M(1,s) at gapped AND crossing
  radii (K_S is deck-odd, c_s deck-covariant). The standing Z/2 twist
  is carried by one object over the whole end.
- Because M is built from {D, K_S} only, the per-s cluster-gauge spikes
  of the frame machinery (the m1 caveat -- re-observed in this build,
  in D itself, at d = 0.002 from the wall) CANNOT touch any section
  object. Continuity statements are made for smooth symbol paths and
  for gauge-invariant scalars; the probe verifies |dM|/|dD| stays
  bounded (~0.9) across the wall, i.e. the symbol adds no roughness of
  its own.

On the gapped sector, M/sqrt(q) = K_S e^{alpha w} EXACTLY (the f5
canonical cut, 4e-16) and equals the n2 Gram-spectral cut symmetry
Q_+ - Q_-, with margin sqrt(q/P) = sech(alpha). Past the wall,
-iM/g is a K_S-SKEW involution whose +1 eigenspace is (growing half on
Ku = +1) + (decaying half on Ku = -1), and whose induced pairing
K_S N is anti-Hermitian, conserved, nondegenerate, null on each half --
M1's both-modes pairing, now derived rather than transposed. The
section datum CHANGES ADJOINT TYPE at the wall (self-adjoint involution
= cut; skew involution = polarization): that typed flip is the sector
structure itself.

## 2. The definition

**Sector-relative Krein section** (truncated-real grade). Let Omega be
a parameter domain of the end family with P > 0 on Omega. A
sector-relative Krein section over Omega is a continuous family
N(t,s) = z(t,s) M(t,s), z scalar, with z^2 q = 1 wherever q != 0, whose
wall matching is ANALYTIC: N is the delta -> 0 limit of a regularized
family

    N_delta := M / sqrt(q + i delta)      (one global principal branch),

each N_delta being globally continuous on Omega. Unpacked: on gapped
components N = +-M/sqrt(q) (an admissible canonical cut -- sign per
component is the datum); on crossed components N = -+iM/g (a pair-block
polarization); at walls the datum is the normalized Jordan nilpotent;
and the matching rule is z_crossed = -i z_gapped at every wall (q+i0)
or its global conjugate (q-i0). The two regularized families +-N_delta
are, for each delta, the ONLY continuous canonical-class candidates --
which is what makes existence and classification decidable questions.

Three facts give the matching clause its content (it is not a
convention dressed up):

1. **It is forced.** Subspace-continuity matching is provably vacuous
   at a wall: all four candidate eigenlines (two cuts, two halves)
   collapse onto the SAME Jordan kernel line at the EP. Matching must
   happen at the level of the blow-up normalization, and the analytic
   rule is the unique continuous one (the regularized family exists
   for every delta; [E] receipt).
2. **It has teeth.** A family glued from the (q+i0) convention on one
   side and (q-i0) on the other has an O(1) relative jump (-> 2) that
   does NOT vanish as delta -> 0: per-wall independent sign choices
   are NOT sections ([F] receipt). The K-a gluing obstruction exists
   precisely for non-analytic matchings, nowhere else. K-a: not fired.
3. **It is gauge-invariant.** Everything is built from {D, K_S} and
   one scalar; the rigidity theorem covers the rest.

The EP collapse law is the two-sided shadow of the single scalar: the
gapped margin is sqrt(q/P) = sech(alpha) (f5) and the crossed
cross-weight is r = sqrt(-q/T) = sech(alpha~), alpha~ = artanh
sqrt(P/T) -- both DERIVED closed forms now, both machine-equal to the
measured Gram quantities, both reproducing m1's measured collapse
sequences (0.661/0.209/0.066 and 0.508/0.202/0.066) and its wall
weights (0.5810 conf-down, 0.7265 boost). Their ratio -> 1 at the wall
because P = T there: **one collapse rate, sqrt(|q|/P*)** -- m1's named
open computation ("one rate or two") is closed: one.

## 3. Existence (theorem-grade vs sampled, named exactly)

**Theorem-grade (exact identities, machine-corroborated at actual
points):** the construction identities c_s = Herm(D); [Ku, D] = 0;
M^2 = qI (all regimes); K_S-self-adjointness; linearity/entirety in D;
deck-oddness given the seam identity; the rigidity theorem; the gapped
identification with the f5 closed form and the n2-built cut; the
crossed identification (eigenspaces, conservation, half-nullity via
universal-null); the wall Jordan structure; the regularized involution
law N_delta^2 = (q/(q+i delta)) I; the seam law N_delta(1) =
-U_h N_delta(0) U_h^-1 (every delta); the double-cover closure
(U_h^2 = I); margin and r closed forms; the k-extension identities of
Section 6.

**Sampled (finite grids, seeded rays):** continuity certificates
(Lipschitz constants of M(t), q(t) on 41-point grids with 8x
refinement at worst steps; the exact scalar derivative bound
(1/2)|q+id|^{-3/2} supplies the rest); coverage -- deep-checked at the
conf-down wall, boost wall, four seeded sweep crossing rays (incl. a
mid-catalogue one), two seeded gapped rays, three resolved undecided
rays, and the conf-down boundary-at-infinity (closed-form limit) plus
one numerical sweep-ray limit; the P > 0 domain bound (min P/(P+T) =
0.36 over all sampled loops). The n2 sweep (132/53/0/15) is reproduced
same-seed-same-stream, so these are the SAME rays as n2/m1.

Existence result: sections exist over every sampled configuration --
including the 53-ray crossing class (represented by five deep-checked
walls plus the full-catalogue reproduction), the t-holes (the datum is
defined at every t at crossing radii, where the cut is not), and the
boundary-at-infinity, where the conf-down limit loop is ITSELF a
crossing loop (q_hat changes sign in t): the walls survive to the
boundary; so does the section structure.

## 4. Classification

Equivalence moves examined, per the mission: (i) continuous
deformation, (ii) frame/gauge redefinition, (iii) scheme choice within
the conserved-pairing class.

**(ii) is trivial by the rigidity theorem** -- gauge moves fix M and
hence act trivially on section data.

**(i) fiberwise connectedness.** Gapped side: the fiber of admissible
cuts over a point is connected onto the canonical one -- witnessed by
the exact graph family V_+(lam) = {x + lam V x} (V the out-of-plane
anti-isometry), admissible for all lam in [0,1) with K-norm exactly
(1 - lam^2)<x, K_S x> (mechanism: K_S V is anti-Hermitian, so the
cross term has no real part), retracting to the canonical cut at
lam = 0. The general step (the Krein contraction ball is convex) is
typed IMPORTED-standard. Crossed side: the census below leaves no
continuous freedom at all beyond gauge. So deformation cannot create
or merge classes beyond the discrete data.

**The crossed-fiber census (the decisive step).** The commutant
algebra span{I, d~ = -iD/g, Ku, J_c = d~ Ku} is 4-dim commutative with
EXACTLY eight involutions +-{I, d~, Ku, J_c}; the K_S-skew,
half-reading candidates are +-d~ and +-J_c only. And d~ -- the bare
spectral-half choice, using no K_S -- is DECK-EVEN (it descends:
sector-blind, the standard fork's crossed cousin) and its gapped
continuation D/sqrt(q) is K-INDEFINITE (signature (64,64)):
inadmissible as a cut, so wall matching EXCLUDES it. Past the wall the
canonical-class section data are +-J_c and nothing else.

**Monodromy.** For each delta the continuous candidates are +-N_delta.
The seam sends N_delta to -N_delta exactly (descent gap 2.00 measured,
gapped and crossing radii alike): NO section exists on the closed base
loop. On the double cover the family closes exactly (U_h^2 = I): TWO
sections, exchanged by the deck. Wall transport contributes nothing --
the regularized family is one global continuous object, so there is no
per-wall freedom to accumulate; the undecided rays resolve at depth
(s = 5, 6) into ordinary classes with the same facts. **Classifying
set: Z/2, the deck twist, uniformly over gapped radii, crossing radii,
resolved undecided rays, and the boundary-at-infinity. K-c.**

**(iii) and the one honest caveat: the +-i0 orientation bit.** The two
global conventions (q+i0, q-i0) agree on the gapped sector and differ
by the sign of the crossed-sector polarization. Machine-exact facts:
J_quat maps the (q+i delta) section to the (q-i delta) section at
every delta and fixes the gapped limit; no real-valued conserved
K_S-linear reading separates the conventions (Re k = 0 past the wall,
an exact identity -- Section 6); the bit is precisely M1's
decay-vs-anti-damping orientation, which m1's [F] receipt establishes
as a GAUGE at matrix grade. On those three grounds the conventions are
identified as a scheme move, and the classification is Z/2. Refusing
that identification would double the count to Z/2 x Z/2 -- and
deciding whether the orientation is data is an OPERATOR-grade question
(W172's dynamical sign, H59's open object). That is the K-d shadow:
named, typed, not fired at this grade.

**Kill adjudication.** K-a: not fired (Section 2). K-b: not fired --
the datum is deck-odd and non-descending everywhere; nothing
trivializes, F2-real is not re-opened (it is extended). K-c: FIRED.
K-d: not fired at this grade; its only candidate (the orientation bit)
is typed scheme with the operator-grade condition stated.

## 5. Consequence for F2-real: two-section structure on the WHOLE end

Yes -- with the domain named. The two-section structure, previously a
property of the spacelike sub-end (n2), is now definable and PRESENT on
the full end wherever P > 0: the two global sections restrict to the
two canonical cuts on gapped arcs, to the two pair-block polarizations
on crossed arcs, cover the walls as normalized Jordan data, fill the
n2 t-holes, and persist at the boundary-at-infinity (where crossing
rays keep genuine walls: the limit loop q_hat changes sign -- the
sector-relative structure is a feature of the boundary itself, not a
finite-collar transient). The F2 kill shape (triviality) fires nowhere
in the extended theory; the existence-domain boundary moves from
"q > 0" to "P > 0", and the P = 0 stratum (pure-timelike symbols;
empty on all 200 sampled rays) is the residual outside. The n2 verdict
"outside the spacelike sector the accounting is UNDEFINED" is hereby
superseded IN THE SECTION SENSE: the cut-level statement stands
(theorem-backed by universal-null), but the section-level datum is
defined and Z/2-classified across the crossing sector.

## 6. Consequence for F5: the k-accounting past the wall, settled

One closed form covers everything. With A the C2 density (built
gauge-invariantly from {D, K_S} via the derived master-identity form)
and k(N) := (1/2) tr(K_S N A):

    k(N_delta) = (128/7) (13 P + 15 T) sqrt(P) / sqrt(q + i delta).

On the gapped side (delta -> 0) this is REAL and is exactly the f5
functional -- base value 14421.0033 reproduced. Past the wall it is
PURELY IMAGINARY: Re k = 0 to machine precision, and this is an exact
trace identity (tr(u D A) is real because u D = sqrt(P) + sqrt(T) w
and A is scalar + w -- only grade-0 terms survive the trace), not a
numerical smallness. So:

- **The F5 signed REAL accounting does NOT extend past the wall.** M1
  declined to extend k_sigma; the sector-relative framework now proves
  the obstruction rather than inheriting the abstention: any
  section-valued extension of k has identically vanishing real part on
  the crossed sector.
- **What does extend is the imaginary width channel**, closed form
  -(128/7)(13P + 15T) sqrt(P)/g -- the Lorentzian-width (decay-rate)
  reading, whose SIGN is the +-i0 orientation gauge at this grade.
  Zero-sum k(N) + k(-N) = 0 survives trivially on the whole end, and
  the deck flip is reproduced in section language (the transported
  section pulled back to the base fiber reads -14421.0033).
- Consistency with the araki even/odd selection rule, verified: every
  deck-even reading (margin, |k|, N^2) is section-blind; the K_S-linear
  k is the unique separator -- the section datum is K_S-linear by
  construction (M carries exactly one factor of K_S).

## 7. Consequence for N2: the residual operator-grade gap, spec'd

What this prototype proves is the symbol-grade half of the missing
theorem: the sector-relative section OBJECT exists, is canonical, and
is Z/2-classified for the actual end symbol family. The residual gap,
stated as sharply as n2 stated its obstruction:

1. **The operator lift.** Promote z M(t,s) to a spectral-section
   analog for the boundary Dirac OPERATOR family on the non-compact
   fiber: an L^2 theory of K_S-self-adjoint operators whose symbols
   change Krein type, with the section entering as the boundary
   condition (APS-type) -- the natural candidate definition is the
   norm-resolvent boundary value of the SAME regularization,
   M_op (q_op + i delta)^{-1/2}, and the theorem to prove is that its
   delta -> 0 limit exists on a domain and is deck-odd; no
   off-the-shelf result covers this (n2's statement, unchanged in
   location, now with the object to lift in hand).
2. **The orientation bit.** Decide at operator grade whether the +-i0
   convention is gauge or data (equivalently: whether the imaginary
   width channel's sign is physical -- W172's dynamical-sign question,
   H59's open object). If data, the classification doubles to
   Z/2 x Z/2; every other part of the Z/2 result is insensitive.
3. **The P = 0 stratum.** The theory's domain is P > 0; pure-timelike
   degenerations (structurally empty of cuts by K-nullity, empty in
   the 200-ray sweep) need either an excision argument or a third
   costume.
4. **The index shadow.** The classifying invariant is the deck class
   in H^1(base loop; Z/2) -- a KO/KR-shadow (J_quat makes it
   KR-flavored); no K-group is computed anywhere. IMPORTED-standard
   steps consumed: separates-components (as in n2) and the Krein
   contraction-ball convexity (Section 4).

## 8. Council pass (inline, five lenses)

- **Spectral geometer (is this a section theory or relabeled pairing
  bookkeeping? -- answered with the definition's decidability):** a
  definition earns "theory" status if it makes existence and
  classification decidable and can FAIL. This one does both: existence
  reduces to global continuity of an explicitly constructed family
  (and a wrong matching clause demonstrably fails -- the [F] gluing
  control); classification reduces to a monodromy computation with
  three possible outcomes, two of which (K-b, K-d) were live -- the
  crossed-fiber census could have produced extra invariants (it
  instead excluded d~ by deck-evenness plus wall-inadmissibility), and
  the wall transport could have accumulated signs (it provably cannot:
  one global regularized object). The content beyond bookkeeping: the
  symbol M itself (nobody had written the canonical cut as
  sqrt(q)-rescaled-entire before; its linearity in D is what makes the
  EP harmless), the census, and the no-descent persistence at crossing
  radii. What is NOT claimed: any operator statement; the Melrose-
  Piazza-shaped theorem remains open with its spec in Section 7.
- **Krein analyst (universal-null consistency):** the crossed-side
  section induces the pairing K_S N = -+i u D / g -- ANTI-Hermitian,
  so no definiteness claim is even expressible for it; the Hermitian
  conserved elements of the section algebra (K_S, u D) are measured
  indefinite past the wall ((64,64) both); the halves are exactly
  null. Nothing anywhere asserts a positive conserved pairing past a
  wall -- the theory is consistent with the universal-null lemma BY
  CONSTRUCTION, and in fact uses it (half-nullity is what makes the
  skew involution's eigenspaces the right datum). The adjoint-type
  flip of N at the wall (self-adjoint <-> skew) is the cleanest
  structural expression yet of "the sector changes Krein type."
- **Index theorist (what classifies; K-theory shadow):** the invariant
  is the orientation class of the section pair under the deck --
  H^1(S^1; Z/2), detected by the exact -1 seam transport, uniform in
  collar radius and stable at the boundary-at-infinity; with J_quat in
  the picture the natural home is a KR-type group, NOT computed. The
  census argument is the finite-dimensional stand-in for a
  classifying-space computation and is the step most in need of an
  operator-grade upgrade. Warning kept in writing: if the orientation
  bit is ever promoted to data, the invariant is Z/2 x Z/2 and the
  second factor is invisible to every real conserved functional at
  this grade -- exactly why symbol grade cannot see it.
- **Numerical analyst (wall conditioning + the gauge-spike caveat):**
  the probe never diagonalizes near the EP: all wall-adjacent objects
  are linear in D (M), closed-form scalars (q, P, T), or the exact
  regularized family; conditioning receipts: M^2 - qI at 1e-10
  relative through the wall, |dM|/|dD| bounded (0.86-0.93), the
  continuity certificate with the exact scalar bound
  (1/2)|q+id|^{-3/2} in place of naive grid steps (grid steps alone
  would be meaningless near t-walls where the excursion is
  delta^{-1/2}-large -- stated, not hidden). The frame's per-s
  cluster-gauge spikes were RE-OBSERVED in D itself (d = 0.002 off the
  wall) and are quarantined structurally: every section object is a
  function of (D, K_S), and all continuity claims are on smooth symbol
  paths or gauge-invariant scalars. Nothing upstream consumed
  s-continuity of the gauge (n2's discipline, kept).
- **Adversarial referee (attack K-c as assumed-not-proven -- in
  writing):** three charges. (1) "Z/2 was imported from n2, not
  proved here." Answer: the new content is the crossing-sector half --
  the census (excluding d~ BY ARGUMENT: deck-even + gapped
  continuation K-indefinite), the rigidity theorem (no gauge move
  flips a section), the wall-transport rigidity (one global
  regularized object, no per-wall freedom -- and the mixed-convention
  [F] shows the alternative fails), and the measured -1 seam at
  crossing radii and at infinity. Each step is receipted; the n2
  import is only the gapped-sector identification, which is verified
  machine-exactly, not assumed. (2) "The J-identification of the +-i0
  conventions is doing load-bearing work and is a choice." Conceded in
  part and typed in full: without it the answer is Z/2 x Z/2; the
  identification rests on three receipts (J-conjugacy, Re k = 0
  exactly, m1's orientation-gauge [F]), all matrix-grade; the doc
  states the doubling condition rather than hiding it (Sections 4, 7).
  (3) "Existence 'across the 53 rays' is really 5 deep checks plus a
  catalogue reproduction." Correct, and stated in Section 3's
  theorem-vs-sampled ledger; the staged method traded exhaustive
  sweeps for exact identities at representative walls, and every
  identity consumed is closed-form in ray data (r = sqrt(-q/T) leaves
  no room for ray-by-ray surprises in the quantities it governs).
  With these concessions the verdict stands: K-c, scoped to
  truncated-real grade, domain P > 0.

## 9. Typed claims

- The section symbol M = Ku D and its little theorems (gauge-invariant
  construction, M^2 = qI on all regimes, K_S-self-adjointness,
  entirety, deck-oddness, rigidity): **NATIVE-DERIVED (paper grade,
  two-line proofs, machine-corroborated on the actual end family).**
- Gapped/crossed/wall identifications (f5 cut, Ku-graded both-modes
  polarization with conserved pairing, Jordan nilpotent): **NATIVE-
  PROVEN (matrix grade, actual walls and rays).**
- Existence of sector-relative sections (regularized definition) on
  gapped/crossing/undecided rays and at the boundary-at-infinity:
  **NATIVE-PROVEN (matrix grade)**, coverage sampled as ledgered in
  Section 3.
- Classification Z/2 (deck) at truncated-real grade, with the +-i0
  bit typed as scheme: **NATIVE-PROVEN (matrix grade)** modulo two
  IMPORTED-standard steps (separates-components; contraction-ball
  convexity) and the named operator-grade condition on the
  orientation bit.
- EP collapse law closed forms (margin = sqrt(q/P), r = sqrt(-q/T),
  one rate): **NATIVE-DERIVED (paper grade)** -- m1's open item
  closed; m1's measured numbers reproduced.
- k-extension: Re k = 0 past the wall (exact identity) + the
  imaginary width channel closed form: **NATIVE-DERIVED (paper
  grade)**; the SIGN of the width channel: orientation gauge at this
  grade (operator-grade data, as in m1/W172).
- The sector-relative spectral-section THEOREM (operator grade):
  **open** -- residual spec in Section 7.

## 10. Receipts

- Probe (deterministic, two runs byte-identical, numpy only, seeded
  20260720, exit 0): `tests/channel-swings/
  sector_relative_section_probe.py` -- HEADLINE `16 [E] + 4 [F] = 20
  (setup [T] = 3 excluded) ALL PASS`.
- Test bed: the n2 end-model machinery replicated verbatim (same seed,
  same stream; sweep 132/53/0/15 reproduced in-probe); anchors
  xi(0,0) = XI, C2 = 155.3625, q(XI) = 30.13 reproduced; K_S/J_quat
  conventions identical to the n2/m1/f2/f5 probes.
- Consumed as regression targets, not re-derived: the f5 closed form
  S = K_S e^{alpha w} (matched at 4e-16) and exact base value
  14421.0033 (matched at 1e-6 relative); m1's collapse sequences and
  wall weights (matched at 5e-4); the n2 Gram-spectral cut
  construction (matched at 1e-15); the universal-null lemma (used, and
  re-verified as half-nullity at the sampled walls).
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` -- the
  Krein-native fork is load-bearing everywhere and NAMED; the standard
  positive-Hilbert fork is recorded at depth ([F]: no continuation
  past the wall exists for it at all -- its defining object is empty
  there -- and it descends where defined, signature (32,32)); killed
  list honored (C2 never an index; no positive pairing asserted past
  any wall; no eta-based count; no equivariant compensator).

## 11. Boundary

Exploration tier under the standing axiom, R0_COND working grade
(except the little theorems, closed forms, and trace identities marked
NATIVE-DERIVED, which are unconditional algebra). Truncated-real
grade throughout: symbol families on the faithful end model, no Dirac
operator on the end, no L^2/Fredholm/K-theory -- the N2 theorem
remains the missing object, now with its symbol half built and its
residual spec in Section 7. Domain P > 0, named. NOT done, named: the
operator lift (Section 7.1); the orientation-bit decision (7.2); the
P = 0 stratum (7.3); any K-group computation (7.4); ray coverage
beyond the sampled ledger of Section 3. Nothing here moves claim
status, canon verdicts, scorecard rows, N-accounting, or public
posture; the bit's VALUE remains externally posited (p2c-owned); W172
and H59 are untouched (the orientation question is cited, not
advanced); no cross-owner writes; no external actions; no commits or
pushes (hourly cadence owns the working tree). Next rungs in order of
exposure: (i) the operator-lift definition via the same regularization
(the one theorem-shaped step this swing makes concrete); (ii) the
orientation-bit question joined to H59/W48; (iii) the KR-shadow
computation for the deck class.
