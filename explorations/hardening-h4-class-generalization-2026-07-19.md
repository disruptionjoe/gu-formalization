---
title: "Hardening swing H4: the class axiomatized and the co-flip proven over it (G-A3); the BV-grade co-flip decided on the verified bicomplex (G-A2)"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (hardening swing H4: class generalization + BV-grade co-flip)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/blockbuster-p3-one-bit-dossier-2026-07-19.md
  - explorations/channel-swing-CH-REC-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - explorations/blockbuster-p3-one-bit-dossier-2026-07-19.md
  - explorations/channel-swing-CH-SIG77-port-2026-07-19.md
  - explorations/channel-swing-CH-SRC-2026-07-19.md
  - explorations/d1-coperator-build-2026-07-19.md
  - tests/rs_bicomplex_spin95_connection_2form.py
  - tests/channel-swings/ch_rec_coflip_probe.py
  - tests/oq_rk1_cl95_explicit_rep.py
runnable:
  - tests/channel-swings/h4_class_generalization_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# H4: class generalization (G-A3) + BV-grade co-flip (G-A2)

Two dossier gaps swung in one probe
(`tests/channel-swings/h4_class_generalization_probe.py`, exit 0, headline
`28 [E] + 4 [F] = 32`, setup `[T] = 12` excluded):

- **G-A3 discharged at kinematic grade.** The construction class is
  axiomatized (`C(p,q; Phi)`, Section 1) at the generality the results
  actually support — arbitrary finite signature `(p,q)`, arbitrary
  fundamental symmetry, arbitrary sign-free record-law coupling — and the
  co-flip + split-costs-one statements are now a **proved theorem over the
  class's operation calculus** (Section 1.3), machine-verified over an
  8-instance exact-rational family with an ENLARGED operation inventory
  (1408 composites, all four couplings). The single-instance concession of
  CH-REC and dossier objection R2 is discharged in its original form.
- **G-A2 decided at fixture grade — the headline (Section 4).** The
  BV/cohomological grade adds **exactly one genuinely new zero-import
  operation: representative choice.** It SPLITS the pair against any
  register that reads raw representatives (a structural identity makes the
  representative-level charge unboundedly shiftable), and it has **zero
  grip on the descended (harmonic/confined) reading.** The enumerated
  BV-grade inventory acts diagonally. The internal-mu (H-REC-CAUS) probe
  finds a three-layer enforcement structure and closes the round-11 N->5
  route at this grade, conditional on the canonical/confined reading —
  which is D1's condition: **the two named N->5 routes are co-conditioned.**

Everything is conditional work under the standing axiom at `R0_COND`
working grade. No claim-status, canon-verdict, scorecard, or posture moves.
K6 signature purity: Sections 2 ((9,5)-typed) and 3 ((7,7)-typed) are
cleanly separated; Section 1 and its family theorem are signature-neutral;
Section 4 (the BV fixture) is computed entirely in the quaternionic-class
channel and says so.

---

## 0. Five-lens council (inline, before execution)

**Lens 1 — Operator algebraist.**
*Approach:* replace enumeration with structure theory. Prove sector
rigidity (the selected sector's G-sign is identically eps for every
admissible pair (G, J) — one line from positive-definiteness of G.J), and
then show every operation in the class acts on the observable pair through
the two parameters (eps, m) alone. That converts "no zero-import composite
splits" from a 16-composite computation into a theorem quantified over the
whole class and ALL covariant transports (the full GL orbit, not one block
swap).
*Feared trap:* proving a theorem about a smaller operation set than the
words claim. "Every zero-import operation" must be DEFINED — here, the
parameter-map calculus of the class — and the theorem statement must carry
that definition, or H4 repeats R2's overclaim one level up.

**Lens 2 — Homological algebraist (BV).**
*Approach:* the genuinely new zero-import resources at cohomological grade
are representative choice, ghost/antifield redefinitions, and homotopy
data. The split question is a DESCENT question: does the register
observable descend to H(s)? Compute the Krein pairing between the exact
space and the harmonic space on the verified fixture, and if the
representative-level charge does not descend, exhibit the splitting shift
constructively — a found split is first-class, not an embarrassment.
*Feared trap:* letting "commutes with s" masquerade as protection. On
harmonic representatives s acts trivially, so ANY grade-flipper commutes
with s there; the enforcement, if it exists, must be located in the
constraint surface and the coupling, and the probe must test those
directly or the survival verdict is hollow.

**Lens 3 — Category theorist.**
*Approach:* two-sorted operation calculus, stated explicitly. Sort one:
covariant transports (isomorphisms of configurations) — observable-trivial
by construction, and now proven so for the WHOLE GL orbit, which is what
"gauge" means here. Sort two: parameter moves that do not transport (the
payload flip, dynamics reversal/substitution, the record-law sign). The
theorem's content is exactly the interaction of the two sorts. Separately:
anchor EXCHANGE is an isomorphism question — it exists iff p = q — so the
relational two-anchor reading is an (n,n) feature while the accounting is
signature-blind; state that as a corollary, it sharpens ADAPTER2-01.
*Feared trap:* quotienting everything into gauge until the theorem is
empty. The distinction transported-vs-not must stay explicit, or the
co-flip becomes a tautology about isomorphism invariance.

**Lens 4 — Signature specialist.**
*Approach:* keep the family theorem signature-neutral; put ALL typing
content in two per-class sections keyed to the antiunitary commutation
type: quaternionic type (J_q^2 = -1, grading-COMMUTING — sector-preserving
bit) versus real type (T^2 = +1, grading-ANTICOMMUTING — sector-exchanging
bit), each with an exact miniature model, and exhibit the GRAM-PIN-77 fork
as data: two antiunitaries on ONE real-type instance giving two typings
and one accounting.
*Feared trap:* cross-contamination (K6) — recomputing (9,5) facts in the
(7,7) section or vice versa — and scale-porting trace facts: K-balance of
symbol eigenspaces is a trace identity that holds at (9,5)
(tr(beta e_a) = 0 for the 9-factor Gram) and FAILS at the (1,3) miniature
(tr(beta c) != 0), so no mini number about balance may be ported upward.

**Lens 5 — Hostile referee.**
*Approach:* attack the theorem's quantifier ("every zero-import operation"
vs "every operation in your calculus") and the BV verdict's dependence on
the canonical reading — isn't "the descended reading is immune" just
assuming D1? Demand that the found split (representative shift) be
reported AS a split with its blast radius stated, not as a footnote to a
survival headline; and demand the residual loci (where the fixture cannot
see) be named as gaps, not absorbed.
*Feared trap:* accepting the harmless framing. A register GU might
actually have written down could read representatives; the honest verdict
is conditional survival with the condition named (confined/canonical
reading = D1's condition), and the co-conditioning of the two N->5 routes
belongs in the headline, not the appendix.

**Chair synthesis.** Adopt all five. Order of battle: axioms + lemmas +
theorem with the calculus-definition carried in the statement (Lens 1 +
Lens 3, Section 1); family sweep receipts (Section 1.4); per-class typing
sections, K6-separated, mini-scale trace caveat recorded (Lens 4,
Sections 2-3); BV grade as a descent computation first, enforcement
located by direct test of constraint and coupling second, found-split
reported as a finding with blast radius, verdict stated conditionally with
the D1 co-conditioning in the headline (Lens 2 + Lens 5, Section 4);
re-scored R2 and residual gaps last (Lens 5, Sections 5-6). Executed.

---

## 1. Part 1 — the class, axiomatized, and the theorem (signature-neutral)

### 1.1 Axioms: the class C(p,q; Phi)

A **finite oriented Krein system with sign-free record law** is:

- **A1 (space and form).** A finite-dimensional real vector space V,
  dim V = p + q with p, q >= 1, with a symmetric nondegenerate bilinear
  form G of signature (p, q).
- **A2 (fundamental symmetry).** J in End(V) with J^2 = I and G.J
  symmetric positive definite.
- **A3 (payload and sector).** A transmitted orientation eps in {+1, -1};
  physical projector P_eps = (I + eps J)/2; physical inner product
  eps.G on ran P_eps.
- **A4 (dynamics).** One or more U with U^T G U = G and [U, J] = 0, plus a
  direction datum tdir in {+1, -1} (step U or U^-1).
- **A5 (record register).** Mode projectors Pi_i commuting with J; sector
  charges q_i(Psi) = eps.G(Pi_i P_eps Psi, Pi_i P_eps Psi); register
  increment  delta N = m . eps . Phi(q_1, ..., q_r)  with Phi >= 0
  monotone, Phi(0) = 0, Phi(x) > 0 for x != 0 (**sign-free coupling** —
  the record law contains no sign datum), and m in {+1, -1} with m = +1 in
  the zero-import class; **m = -1 is one underived Z/2 import** (the mu of
  CH-REC, now typed as the unique sign slot the axioms leave).

C_0 of CH-REC is the single instance (2,2), standard J, r = 1, Phi = id.

**Operation calculus (the definition Lens 1 demanded).** The zero-import
operations of the class are generated by:
(i) **covariant transports** by ANY invertible S (G -> S^T G S,
J -> S^-1 J S, U -> S^-1 U S, Pi_i -> S^-1 Pi_i S, Psi -> S^-1 Psi);
(ii) **dynamics substitution** within the admissible set and **reversal**
(tdir flip); (iii) the **payload flip** E: eps -> -eps.
The one paid operation is M: m -> -m (one Z/2). Operations outside this
calculus (grade-mixing resources that need MORE structure than the class
has) are exactly what Part 2 hunts at BV grade.

### 1.2 Lemmas

**Lemma 1 (sector rigidity).** For every admissible (G, J):
G restricted to ker(J - I) is positive definite and G restricted to
ker(J + I) is negative definite. Hence the G-sign of ran P_eps is
identically eps, and every sector charge q_i >= 0 — automatically, not by
assumption. *Proof.* For Jv = v: G(v,v) = G(v,Jv) = (G.J)(v,v) > 0; for
Jv = -v: G(v,v) = -(G.J)(v,v) < 0. q_i is eps times a G-value on the
eps-sector.  []

**Lemma 2 (transport triviality).** Every covariant transport preserves
admissibility and every observable (sector sign, charge trajectories,
register trajectory). *Proof.* Admissibility: J'^2 = I,
G'J' = S^T(G.J)S > 0 (congruence), U'-conditions by conjugation. Every
observable is a G-contraction of transported data and is invariant by
substitution.  []

**Lemma 3 (drive positivity).** Under grading-preserving invertible
dynamics, P_eps Psi_t = U^(+-t) P_eps Psi_0, so eps-sector content is
either identically zero along the trajectory or never zero; with content,
the total Phi-drive is > 0, hence  dir := sgn(Delta N) = m . eps.
With zero eps-content (vacuum, or mirror-only states), dir = 0 and the
state is orientation-unwitnessed.  []

### 1.3 Theorem (co-flip + one-bit price, class form)

**On every instance of C(p,q; Phi), on states with eps-content, the
observable pair is identically  (sector, dir) = (eps, m.eps).**
Consequently, for every operation in the calculus of 1.1:

1. **Diagonality.** Covariant transports and dynamics
   substitution/reversal fix both entries (Lemmas 2, 3); E flips both
   together; hence every zero-import composite acts diagonally — it flips
   both entries iff it contains E an odd number of times, and **no
   zero-import composite splits the pair**.
2. **Exact price.** A composite splits the pair iff it flips m — i.e. iff
   it pays exactly one underived Z/2 in the record law. The N -> 5
   boundary is the accounting identity  split <=> one paid bit, now at
   class generality.
3. **Blindness.** Both statements are blind to dimension, signature
   (p, q), the choice of fundamental symmetry, the dynamics, and the
   record-law coupling Phi.

*Proof.* Immediate from Lemmas 1-3: the pair is a function of (eps, m)
only, the calculus acts on (eps, m) by (E, M) only, and zero-import means
m is fixed.  []

**Corollary (anchor exchange is an (n,n) phenomenon).** An isomorphism of
the structure exchanging the two sectors exists iff p = q (sector
dimensions must match). For p != q both payload VALUES remain admissible
(both anchors carry positive physical norm), but the anchors are
structurally inequivalent: the RELATIONAL two-anchor symmetry
(ADAPTER2-01's relabeling freedom) is an (n,n) feature, while the co-flip
and its price hold for all (p, q).

**Honest scope (Lens 1's trap, honored).** This is a theorem about the
axiomatized operation calculus, not about "all conceivable operations."
What it upgrades: CH-REC's enumerated 16-composite result on one (2,2)
fixture becomes a proof over ALL covariant transports (the full GL orbit),
all admissible dynamics, all signatures and couplings. What it does not
touch: operations needing structure the class lacks — the cohomological
grade's resources. That residue is exactly Part 2.

### 1.4 Family sweep receipts (machine verification, exact arithmetic)

Instances: (1,1), (2,2), (3,3), (2,1), (3,1), (4,2) standard, plus
transported (de-standardized) (2,2)T and (2,1)T under generic rational GL
moves. Four couplings Phi (linear, weighted two-mode, quadratic, mixed);
up to four dynamics per instance; both tdir. Enlarged generator set per
instance: {E, T, Usub, generic-GL transport, anchor swap (n,n only)} x
{M}; **1408 composites checked against the theorem's prediction — sector
flips iff E, direction flips iff exactly one of {E, M}, split iff M,
import 1 iff M — all exact** ([E], probe Part 1). Controls: the paid M
split is flagged by the import counter, and the partial-relabel attack
(move J, transport nothing) is rejected by the admissibility gate in
every instance ([F] x 2). Vacuum unwitnessed in every instance; mirror-only
content drives no record ([E] x 2, the family form of CH-REC's
vacuum/witness structure).

---

## 2. Per-signature-class statement — quaternionic type ((9,5)-like)

*This section carries only (9,5)-cited facts and the probe's
quaternionic-type model. No (7,7) computation appears here.*

**Statement (quaternionic typing).** In the quaternionic class the
orientation bit is **J_quat-COMMUTING by type**: the antiunitary
J_q (J_q^2 = -1) commutes with the grading, so it PRESERVES each
orientation sector and the Krein sign, and Kramers doubling operates
inside sectors. The bit cannot anticommute with the quaternionic
structure — at (9,5) this is the representation-exact theorem (canon
quaternionic-parity no-go / CH-QM P6; mini-corroborated in CH-SRC
Dc1-Dc5). **Same accounting identity as the class theorem; the typing is
an annotation on payload item 1, not a change in the accounting.**

Probe receipts (exact Gaussian-rational model, probe Part 1b): J_q^2 = -1;
[J_q, P_eps] = 0 (sector-preserving); Krein sign preserved exactly;
co-flip + split-costs-one hold verbatim with quaternionic-compatible
dynamics ([U, J_q] = 0).

The BV-grade computation of Section 4 lives entirely in this class (the
verified Spin(9,5) fixture and its Cl(1,3) = M(2,H) miniature).

---

## 3. Per-signature-class statement — real type ((7,7)-like)

*This section carries only (7,7)-cited facts and the probe's real-type
model. No (9,5) computation appears here; nothing from Section 4 is
claimed for this class.*

**Statement (real typing).** In the real class the native antiunitary
J' has J'^2 = +1, and under the canonical Gram it ANTICOMMUTES with the
grading (CH-SIG-77 probe 1c): it **EXCHANGES the two orientation
sectors** and flips the Krein sign — the bit picks one of two
J'-conjugate sectors, i.e. the orientation choice breaks the real
structure (CH-SIG-77 1g). **Same accounting identity; different typing.**
The typing annotation is Gram-convention-dependent (the GRAM-PIN-77
fork): under the chirality-twisted Gram the sectors are J'-invariant.
The accounting is Gram-robust.

Probe receipts (exact Gaussian-rational model, probe Part 1b): T_c^2 = +1;
T_c P_eps = P_(-eps) T_c (sector-exchanging); Krein sign flipped exactly;
the anchor-exchange identity q_(-eps)(T v) = q_eps(v) — the antiunitary
implements the relational anchor move, NOT a split; the fork twin
T'_c = conj on the SAME instance is sector-preserving and sign-preserving
(the GRAM-PIN-77 image: two antiunitaries, one instance, two typings, one
accounting); co-flip + split-costs-one hold verbatim.

**Named gap for this class:** the BV-grade questions of Section 4 are NOT
computed in the real channel (G-H4-4, Section 6).

---

## 4. Part 2 — the BV-grade co-flip (G-A2): the headline

*Computed entirely in the quaternionic-class channel: the verified
Spin(9,5) bicomplex machinery (rep, connection dressing, constraint
co-differential, Koszul-Tate leg exactly as
`tests/rs_bicomplex_spin95_connection_2form.py`; named a-priori
single-boost connection W = 0.8 Sigma_09; blockwise closure re-verified,
raw-generator control fires at 460.61) plus its Cl(1,3) miniature (the
CH-SRC mini-rep scale). Krein form K = eta_V (x) beta with
beta = e_0...e_8 (Hermitian, involutive, c(xi) K-Hermitian — all
[T]-checked).*

### 4.1 The one new zero-import operation, found: representative choice

The BV grade adds exactly one operation the kinematic calculus does not
have: **replacing a cohomology representative by an s-exact shift.** The
probe decides what it does to the pair:

- **Structural identity ([E], rel. residual 1.3e-16):**
  `B K B^dag = 14 beta` exactly. Hence the Krein form restricted to the
  s-exact space at ghost number 0 has signature **(64, 64) — indefinite**
  — so the representative-level Krein charge is UNBOUNDEDLY shiftable by
  zero-import exact moves (and the linear exact-harmonic pairing is also
  nonzero, ||E^dag K H|| = 5.89: the attack is live at linear and
  quadratic order).
- **The split, exhibited ([E]):** an explicit s-exact shift takes a
  physical class representative's charge from +0.085 to -0.659 (sign
  FLIPPED) with the cohomology class unchanged (drift 1.5e-15) and the
  sector selection untouched. **Any register that reads raw
  representatives is split at zero import.** This is a genuine found
  split with a stated blast radius: representative-level readings.
- **The immunity, exhibited ([E]):** the canonical (harmonic/confined)
  reading is exactly representative-independent — the harmonic projection
  annihilates the shift (descended charge equal to 6+ decimals). The
  harmonic gh-0 space has Krein signature **(+768, -768, 0)** ([E]): the
  confined reading is well-posed, and the graded two-sided content is
  exactly W235's record structure at this grade.

### 4.2 Inventory diagonality on descended observables

All enumerated BV-grade zero-import operations act diagonally on
(sector selection, confined-register direction) ([E] each, [F] controls):

| operation | action on the pair |
|---|---|
| anchor flip (eps / K -> -K) | flips BOTH (co-flip) |
| representative shift | inert on the descended reading (4.1) |
| ghost-sign flip (c, c* -> -c, -c*) | inert; closure survives all four leg-sign patterns |
| antifield-sign flip | inert; same |
| xi -> -xi (symbol/propagation direction) | **inert — the BV-grade image of P3** (projector drift 0.0; the arrow is not in the propagator at cohomological grade either) |
| connection flip W -> -W | diagonal (harmonic K-signature and confined direction unchanged) |
| mu insert | flips direction only — **flagged as the one paid Z/2** ([F], fires) |

### 4.3 The internal-mu question (H-REC-CAUS): a three-layer answer

The round-11 route asked: does the cohomological realization forbid an
internal mu while a cleanly-decoupled variant permits one? The fixture
answers with more structure than the hypothesis had:

1. **The unpaid mu exists FREE at the structure-free grade, and its locus
   is exactly the d1 shape.** The bare symbol dynamics M_D has
   K-INDEFINITE degenerate diagonalizable eigenspaces (the +sqrt(Q)
   eigenspace of the miniature: K-signature (+2, -6)) — the
   vacuum-anchor/Casimir degeneracy shape from the D1 build — and a
   K-grade-reversing symmetry R' of the dynamics alone exists there
   ([R', M_D] = 4.8e-15; charge +1 -> -1). Without constraint structure,
   the grade flip costs nothing. (Mini-scale caveat, per Lens 4: the
   (9,5) eigenspaces are K-BALANCED by the trace identity
   tr(beta e_a) = 0; the miniature's are indefinite but unbalanced
   because tr(beta c) != 0 at (1,3). Indefiniteness is what matters;
   balance is not ported from mini scale.)
2. **The constraint structure is the enforcement.** The same R' breaks
   the sector projector ([R', Pi] = 1.70). And at every gapped locus, the
   compressed sector dynamics of the block-diagonally DECOUPLED (VZ-trap)
   variant has ONLY K-definite eigengroups (six groups at the probe
   locus; spectrum table in the probe output) — and since the commutant
   of a diagonalizable operator preserves each eigenspace, **no
   dynamics-commuting sector-preserving operator can reverse the record
   K-grade: no unpaid mu exists at the gapped locus even under clean
   decoupling.** That is exhaustive over the commutant there, and
   STRONGER than the H-REC-CAUS hypothesis (which expected the decoupled
   variant to permit the mu).
3. **The fixture's own degenerate surface is the Jordan wall, and it is
   vacuous rather than split.** At null xi (c(xi)^2 = 0 exactly, escape
   still 2.449 != 0), the decoupled sector dynamics is exactly nilpotent
   with ranks D^k = [8, 4, 2, 0] and its diagonalizable zero block
   N_0 = ker(D) cap (im D)^perp is EMPTY — every kernel vector is a chain
   end, and the kernel's K-Gram is totally null (0:4). No admissible
   grading exists there at all (R1's positivity-unrescuable wall): the
   direction observable is VACUOUS at this locus, not split. The
   K-indefinite-diagonalizable SECTOR locus — where the
   coupled-vs-decoupled contrast would be decisive and the coupling the
   only defense — is NOT realized by this fixture's symbol family
   (named residual G-H4-3).
4. **The escape identity.** A decoupled-ONLY symmetry (spectral
   reflection through a compression-born eigendirection — an eigenvalue
   of the decoupled sector dynamics that is NOT an eigenvalue of M_D)
   commutes with the decoupled dynamics and the sector projector
   (residuals 1.7e-14, 1.9e-15) yet pays, in the coupled theory, a defect
   EXACTLY equal to its non-commutation with the escape term:
   **||[R, M_D]|| = 9.3974 = ||[R, M_off]||, identically** (since
   [R, M_dec] = 0, [R, M_D] = [R, M_off] is an operator identity). The
   causality-required coupling removes the decoupled variant's symmetry
   surplus — the reservoir from which any internal mu would have to come.
   (The block-diagonal decoupling and its nonzero escape term were also
   verified at full (9,5) scale: [Pi, M_dec] = 5.2e-14,
   ||escape|| = 39.12.)

### 4.4 The BV verdict (G-A2)

**The arrow/sector coupling SURVIVES at cohomological grade — on
descended observables, conditionally, with the condition named.**
Precisely:

- The BV grade contributes exactly one new zero-import attack
  (representative choice). It kills any representative-level reading
  (found split, 4.1) and has zero grip on the canonical
  (harmonic/confined) reading. The rest of the enumerated inventory is
  diagonal (4.2). The internal mu is removed by the constraint structure
  at every gapped locus (exhaustively over the commutant), the fixture's
  own degenerate surface is the ungradable Jordan wall, and every surplus
  decoupled symmetry pays exactly the escape term (4.3).
- **Therefore the round-11 N->5 route through G-A2 is CLOSED at this
  fixture grade, conditional on the register being a descended/confined
  observable — which is precisely D1's condition** (the interacting
  C-operator/confinement grading records). The two named N->5 routes of
  the dossier (BV-grade split; D1 second-anchor freedom) are
  **co-conditioned**: both live or die with the canonical confined
  reading. They are not identical (D1 can also fail through a second
  anchor freedom, which the d1 build did not find), but a single
  condition guards both.
- H-REC-CAUS (dossier H1) is **partially promoted and partially
  corrected** at fixture grade: the enforcement mechanism is real but
  layered — the constraint surface does the work at gapped loci (clean
  decoupling does NOT create the mu there, contra the hypothesis's
  expectation), and the coupling's enforcement role is the exact escape
  identity plus the removal of the decoupled symmetry surplus. The
  decisive locus (K-indefinite diagonalizable sector spectrum with
  coupling on) awaits an S_IG-type gapped-pair dynamics (G-H4-3, = G-B2
  territory).

---

## 5. Re-scored R2 (the dossier's standing concession)

Dossier R2 stood un-rebutted as: *"the enumerated inventory has no
exhaustiveness proof, the cohomological/BV grade has more involutions
than the action level, and the class has one signature instance at
theorem strength."* After H4:

- **"One signature instance at theorem strength" — discharged.** The
  class is axiomatized (A1-A5); co-flip + price are a theorem over the
  class (Section 1.3), exact-verified over 8 instances x 4 couplings x
  1408 composites; per-signature-class typing stated and machine-anchored
  on both sides of the fork.
- **"No exhaustiveness proof" — upgraded, not closed.** At kinematic
  grade the theorem now covers the ENTIRE operation calculus (all GL
  transports, all admissible dynamics moves) — a characterization
  relative to the calculus, replacing the 16-composite enumeration. The
  residual is calculus-adequacy (G-H4-1), which is an axiom-completeness
  question, not a computation gap.
- **"The BV grade has more involutions" — engaged head-on.** The one
  genuinely new operation was found, shown to split non-observable
  readings, and shown inert on observables; the inventory there remains
  ENUMERATED (G-H4-2) and the abstract-level qualifier should now read:
  *"no operation in the parameter-map calculus of the axiomatized class
  (theorem), and none in the enumerated BV-grade inventory (fixture),
  splits the pair — the BV grade's representative freedom splits exactly
  the readings that fail to be observables."*
- **New honest debit created by H4:** the BV-grade survival is explicitly
  conditional on the confined/canonical reading, i.e. co-conditioned with
  D1. R2's successor concession is smaller but sharper: one condition now
  guards two routes, so a D1 failure would open both at once.

---

## 6. Remaining generality gaps (named, pre-registered)

- **G-H4-1 (calculus adequacy).** The kinematic theorem quantifies over
  the class's operation calculus. A characterization of all zero-import
  operations from first principles (what CAN act, given only the
  structure) would close G-A1 fully; the found BV resource shows such
  residues are real and findable.
- **G-H4-2 (BV enumeration).** The BV-grade inventory (representative
  shifts, ghost/antifield redefinitions, anchor/connection/symbol flips,
  mu) is enumerated, not characterized. Grade-mixing operations beyond it
  are unprobed.
- **G-H4-3 (the S_IG locus; = G-B2 territory).** The
  K-indefinite-diagonalizable SECTOR locus with coupling on — where the
  coupling would be the only line of defense — is not realized by this
  fixture's symbol family (gapped loci are K-definite; the null locus is
  the ungradable Jordan wall). Needs a gapped-pair interaction dynamics.
  Co-conditioned with D1.
- **G-H4-4 (real-class BV grade).** Part 2 is quaternionic-channel only.
  The (7,7)/M(128,R) port of the BV-grade questions (descent, inventory,
  internal mu) is typed by Section 3 but not computed.
- **G-H4-5 (finiteness).** Everything is finite-dimensional; no
  continuum statement.
- **G-H4-6 (Lean; = G-A4).** The Section 1 theorem (Lemmas 1-3 +
  diagonality + price) is now in Lean-amenable shape over the abstract
  class — the natural first formalization target, unchanged from the
  dossier's estimate.

---

## 7. Receipts

- Probe: `tests/channel-swings/h4_class_generalization_probe.py`, run
  this swing, exit 0, headline `28 [E] + 4 [F] = 32` (setup `[T] = 12`
  excluded). Part 1 exact rational (stdlib); Part 1b exact
  Gaussian-rational complex; Part 2 numpy/scipy on the verified Cl(9,5)
  rep (`tests/oq_rk1_cl95_explicit_rep.py`) with the
  `rs_bicomplex_spin95_connection_2form.py` machinery rebuilt blockwise
  (closure c1 = c2 = 1.4e-13, leg ranks 128/128, raw control 460.61).
- Key numbers: 1408 composites exact; B K B^dag = 14 beta (1.3e-16);
  exact-space K-signature (64,64); harmonic K-signature (768,768,0);
  representative split +0.085 -> -0.659 with class drift 1.5e-15;
  canonical reading drift < 1e-8; ||E^dag K H|| = 5.89; xi-flip projector
  drift 0.0; (9,5) decoupling [Pi, M_dec] = 5.2e-14 with escape 39.12;
  mini gapped spectrum 6 groups all K-definite; null locus ranks
  [8,4,2,0], N_0 empty, kernel K-Gram totally null; bare-dynamics R'
  ([R', M_D] = 4.8e-15, charge +1 -> -1, [R', Pi] = 1.70); escape
  identity 9.3974 = 9.3974 (operator identity).
- In-repo evidence read: CH-REC swing (C_0, co-flip, T3, G2); blockbuster
  dossier (R2 concession, G-A2/G-A3, H1, N->5 routes); CH-SIG-77 port
  (1c/1g retyping, GRAM-PIN-77); CH-SRC (mini-rep, trap C4, SRC-COH-1);
  d1 co-operator build (degeneracy shapes, Jordan-vs-diagonalizable,
  Casimir anchor); W235 docstring (record Z2 closed-not-exact);
  `rs_bicomplex_spin95_connection_2form.py` (fixture machinery).
- No cross-repo reads or writes; no external actions. Files touched:
  this document and the probe script only.

## 8. Boundary

Conditional work under the standing axiom, `R0_COND` working grade. The
Section 1 theorem is a finite-dimensional statement about an axiomatized
class and its declared operation calculus; the Section 4 results are
fixture-grade computations on the verified bicomplex machinery and its
miniature, not field theory; nothing here is a GU verdict. The (7,7)
statements are typing-level with their computation gap named. No claim
status, canon verdict, scorecard, register, ledger, or public posture
moves; bar(b) = finality-axis polarity remains OPEN and is nowhere
reasserted; the killed-selector ledger is untouched. Joe alone publishes;
no external actions.
