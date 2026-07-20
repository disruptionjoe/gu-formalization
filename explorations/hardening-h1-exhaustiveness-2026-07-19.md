---
title: "Hardening H1 (gap G-A1): the exhaustiveness theorem — zero-import diagonality over ALL operations, and the exact one-bit price as an identity"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (hardening swing H1, gap G-A1)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/blockbuster-p3-one-bit-dossier-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - tests/channel-swings/ch_rec_coflip_probe.py
  - explorations/blockbuster-p3-one-bit-dossier-2026-07-19.md
  - explorations/d1-coperator-build-2026-07-19.md
runnable:
  - tests/channel-swings/h1_exhaustiveness_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Hardening H1: the exhaustiveness theorem for the one-bit result

Gap G-A1 was the dossier's own top hardening item and the substance of its
one standing un-rebutted concession (R2): "no zero-import operation splits
the pair" was proven only over an ENUMERATED 16-composite involution
inventory, and the abstract was obligated to say so. This swing replaces
the inventory with a characterization and proves the co-flip (P1) and the
one-bit price (P2) as theorems over the FULL class of zero-import
operations — in fact over a quantifier strictly stronger than any
operation-group formulation. One genuine inventory miss is found and
adjudicated (benign, provably so in advance). The continuous families
(the D1 C-operator continuum) are handled by an explicit
connected-component argument. The referee lens closes by re-scoring the
dossier's R1/R2 objections against the theorem.

Everything is conditional work under the standing axiom at R0_COND
working grade. No claim-status, canon, or posture moves; no edits to the
dossier or any sibling file (proposals for their next edit are listed in
Section 7 for the steward; single-file discipline observed).

**Headline.** On the zero-import stratum of the class, the observable
pair is a FAITHFUL COPY of the discrete configuration data:
`(sigma, d) = (eps, mu·eps)`, hence `sigma·d = mu`. Sector-sign rigidity
(`sigma = eps`, forced by the fundamental-symmetry gate `G·J ≻ 0` over
the entire moduli space) and direction rigidity (`d = mu·eps`, forced by
unconditional charge positivity) together make diagonality automatic for
EVERY map between zero-import configurations — natural or not, continuous
or not, invertible or not, dimension-preserving or not. Exhaustiveness is
not a big enumeration; it is two rigidity lemmas and one line. The split
price is exactly one bit, necessary AND sufficient, because the import
counter is itself an observable: `mu = sigma·d` is the split parity.
P1, P2, P3 move from ENUMERATED to THEOREM (action grade, finite
dimension, any signature (p,q) with p,q ≥ 1). What does NOT move: the
cohomological grade (G-A2), membership of GU's actual law (T3/P9, D1/D2),
and everything else the theorem's writ cannot reach — the attack surface
relocates onto the class axioms, which is exactly where the audit already
stands guard.

---

## 0. Five-lens council (inline, before execution)

**Lens 1 — Group theorist.**
*Approach:* do not hunt generators first; hunt the invariant. Compute the
observable map on the whole configuration moduli space and ask what it
factors through. If the map is constant on strata labeled by discrete
data, then ANY stratum-preserving action — group, groupoid, or arbitrary
family — acts through the labels, and "is the inventory exhaustive?"
answers itself: the interesting object is not the operation group (which
is enormous and dull: all of GL(K) worth of relabels, the full
fundamental-symmetry continuum, every dynamics substitution) but its
observable shadow, which should collapse to something tiny. Also insist
on separating the two Z/2's that haunt this program: the relational
anchor exchange (gauge) and the payload flip (physical). If the theorem
is right, one lands in the kernel and one generates the image — that
split IS the theorem's group-theoretic content.
*Feared trap:* chasing a presentation of the full automorphism group of
the class — huge, basis-dependent bookkeeping, no payoff — instead of
its action on observables; and conflating the gauge Z/2 with the payload
Z/2, which is precisely the withdrawn 2026-07-15 ratification's disease.

**Lens 2 — Finite-model theorist.**
*Approach:* treat the class as a first-order structure: admissibility =
axioms, configurations = models, operations = maps between models. The
definition of "zero-import operation" is the whole game: too tight
(requiring operations to preserve eps-strata, or to be natural) and the
theorem is assumed, not proven; too loose and nothing is a theorem.
Resolution discipline: state the theorem under the WEAKEST possible
hypothesis on operations (arbitrary partial maps) and derive diagonality
purely from the axioms — then every structured subfamily anyone ever
proposes (involutions, continuous families, BV-morphisms at action
grade, dimension-changing functors) inherits the result as a special
case. Hunt unintended models: degenerate signatures (p or q zero — the
eps=−1 sector empty), unwitnessed trajectories (d undefined), states
exactly in the mirror sector.
*Feared trap:* a definition of admissible operation that secretly
assumes the conclusion. The tell would be any clause mentioning eps or
the pair. The definition below mentions only the axioms and the import
counter.

**Lens 3 — Hostile referee.**
*Approach:* attack the new theorem the way R1 attacked P1: "you have
proven that a function equal to eps equals a function equal to eps."
Force the write-up to locate the content honestly: it lives in the
rigidity lemmas — specifically in the positivity gate `G·J ≻ 0` doing
structural work (killing every partial-flip attack over the whole moduli
space at once), and in the fact that the observable map's fibers realize
the price. Then re-score R1 and R2 against the theorem WITHOUT a victory
lap: R2 has an exhaustiveness half and a class-boundary half, and only
one of them dies today.
*Feared trap:* declaring R2 dead when only its exhaustiveness half died;
and letting "theorem" language suggest the physics hardened — it did
not; the mathematics hardened and the load moved onto membership
(T3/P9/D1), which is where the honest risk always was.

**Lens 4 — Combinatorialist.**
*Approach:* build the finite shadow that a machine can check exactly:
the widened composite table (five generators, 2^5 = 32 composites,
including the new standalone generator F), the four-stratum (eps, mu)
table verifying `sigma·d = mu` pointwise, sampled rational paths through
the fundamental-symmetry continuum as finite witnesses of the
connected-component argument, and controls in which the load-bearing
gate is removed and the rigidity demonstrably collapses. Keep the script
honest about epistemic roles: the PROOFS carry the quantifiers; the
checks are witnesses on a widened moduli sample (which the original
probe never had — it never left its base structure) plus controls
showing the checks can fail.
*Feared trap:* mistaking sampled paths for a proof of connectedness (the
proof is convexity of the angle-operator parametrization; the samples
are witnesses), and combinatorial theater — 32 composites on three
configurations prove nothing beyond the lemmas, and the script must not
pretend otherwise.

**Lens 5 — Expositor.**
*Approach:* the story is "the inventory was scaffolding; the
load-bearing wall was the admissibility gate all along." One governing
formula the reader can hold: `sigma = eps`, `d = mu·eps`, so
`sigma·d = mu` — the pair (sector-sign, direction) is a faithful copy of
(payload bit, import bit), and NOTHING else in a configuration has an
observable sign. Splitting is not hard at zero import; it is impossible,
because there is nothing else with a sign to use. And the price is
exactly one bit because the import bit is literally the split parity.
*Feared trap:* letting "exhaustiveness proven" leak beyond the class
boundary. Readers will hear "the R2 objection is dead"; it is dead only
where the class axioms reach — action grade, finite dimension. Every
strong sentence must carry the boundary.

**Chair synthesis (execution plan).**
(1) Definitions first, at finite-model discipline: the envelope class at
general signature (p,q), the import counter, and the maximally weak
operation definition (Lens 2 owns; Lens 3 audits for smuggled
conclusions). (2) Rigidity lemmas L0–L2 with complete proofs — this is
where the mathematical content lives (Lens 3's demand). (3) Theorem A
(exhaustive co-flip, all-maps quantifier), Theorem B (exact price as
fiber structure, `sigma·d = mu`), corollaries (P3 upgraded to
propagator-independence at theorem grade; the partial-flip obstruction
explained structurally). (4) Theorem C, the group-theoretic shadow
(Lens 1 owns): observable action = Z/2 × Z/2, gauge/payload split (F in
kernel, E generating), contractibility of the fundamental-symmetry space
and the connected-component argument covering the D1 continuum;
adjudicate the found miss F. (5) Machine check (Lens 4 owns): widened
moduli sample, 32-composite table, path witnesses, gate-removal
controls. (6) Referee close: R1/R2 re-scored, concession ledger
rewritten as proposals, non-claims (Lens 3 owns; Lens 5 words the
boundary). Executed below.

---

## 1. The class, the import counter, and the operation — precise definitions

### 1.1 The envelope class C (general finite signature)

A **configuration** is a tuple `X = (K, G, J, U, eps, tdir, mu)` where:

- `K` is a finite-dimensional real vector space; `G` a symmetric
  nondegenerate bilinear form of signature (p,q) with p ≥ 1 and q ≥ 1
  (both sectors inhabited; see Remark 1.4);
- `J` satisfies `J² = I` with `G·J` symmetric and positive definite
  (fundamental symmetry: equivalently, J is a G-selfadjoint involution
  whose majorant `⟨.,.⟩_J = G(J·,·)` is a definite inner product);
- `U` is invertible with `Uᵀ G U = G` (Krein-unitary) and `UJ = JU`
  (grading-preserving);
- `eps, tdir, mu ∈ {+1, −1}`.

Derived objects: physical projector `P_eps = (I + eps·J)/2`; sector
charge `q(Psi) = eps·G(P_eps Psi, P_eps Psi)`; record register
`N += mu·eps·q(Psi_k)` along the tdir-trajectory of U. This is the
CH-REC class verbatim, with mu carried explicitly as the envelope
parameter: **C_0 = {mu = +1}** (zero import), the mu = −1 stratum
carries import `i(X) = 1`. The complex-Hermitian case is identical with
`ᵀ → †`; the probe is real-rational for exactness.

Observables (the pair under test, as in CH-REC §1.3):

- `sigma(X)` = the G-sign of `ran P_eps` (well-defined by L1 below);
- `d(X, Psi)` = `sgn(N_final)`, the record-accumulation direction, on
  trajectories that are **witnessed** (some `q > 0` along them).

### 1.2 The import counter, formalized

CH-REC's class-defining constraint was: *the record law contains no sign
datum not derived from the structure*. This swing formalizes it:

> **Definition (import).** `i(X) = 0` if `mu = +1`, else `1`. mu is the
> UNIQUE slot in the configuration data where an underived sign can sit.

That uniqueness is not a stipulation — it is the content of L1 and
Theorem C: every other sign-like resource in a configuration (the sign
convention of G, the choice of J, the basis, the dynamics and its
direction, the anchor naming) is either DERIVED (its observable sign
content is forced by admissibility: L1) or GAUGE/INERT (it moves nothing
in the observable pair: Theorem C). After this swing, "no new sign data"
is a theorem-backed bookkeeping rule, not an intuition.

### 1.3 The operation — the admissibility definition (the swing's item 2)

> **Definition (operation; zero-import operation).** An *operation* is
> any partial map `g` on ⋃_dim (C × K) — configurations of any dimension
> together with states — with values in the same union. No naturality,
> continuity, linearity, invertibility, or dimension-preservation is
> assumed. `g` is *zero-import at* `(X, Psi) ∈ dom g` if both `X` and
> the configuration of `g(X, Psi)` are admissible with import 0.

Three design comments (finite-model discipline):

1. **Why so weak?** Because the theorem survives the maximal
   quantifier. Any narrower notion anyone proposes — the involution
   inventory, one-parameter continuous families (the D1 boosts), natural
   transformations commuting with relabels, BV-morphisms at action
   grade, tensoring/restriction functors that change dimension — is a
   subfamily of this one and inherits the theorem. The classical worry
   "which operations count?" becomes moot: all of them count.
2. **What makes it non-vacuous?** The two admissibility requirements at
   source and target. An "operation" that leaves the class (e.g. the
   partial relabel `J → −J` with G fixed) is not a zero-import
   operation because its target is not admissible — that is the
   positivity gate firing, and it is load-bearing (probe control
   `gate-load-bearing`). An operation whose target has `mu = −1` is an
   operation of import 1 — that is the M-composite family.
3. **No smuggled conclusion.** The definition never mentions eps, the
   sector, or the direction. Diagonality is derived from the axioms.

### 1.4 Remarks on edge models

- If p = 0 or q = 0 the space is definite, one eps-sector is {0}, and
  `sigma` is undefined for that eps: hence the hypothesis p, q ≥ 1.
- On unwitnessed trajectories (all q = 0 — the vacuum, or a state
  confined to the mirror sector) `d = 0`: the state has NO direction,
  never a wrong one. This is P10's orientation-witness structure and it
  is not a split resource: "splits" require both observables definite
  and misaligned. The probe's widened sample happened to contain a
  nonzero unwitnessed instance (a generic state landing exactly in a
  relabeled mirror sector), and `d = 0` exactly there — the theorem's
  edge case, exhibited live (L2 check).

---

## 2. The rigidity lemmas

**Lemma L0 (spectral decomposition of admissibility).** For every
admissible (G, J): `K = K_+ ⊕ K_−` G-orthogonally, where
`K_± = ker(J ∓ I)`, with G positive definite on K_+ and negative
definite on K_−; moreover dim K_+ = p, dim K_− = q.

*Proof.* `J² = I` gives `K = K_+ ⊕ K_−`. `G·J` symmetric means
`Jᵀ G = G J`, i.e. J is G-selfadjoint; for `v ∈ K_+`, `w ∈ K_−`:
`G(v, w) = G(Jv, w) = G(v, Jw) = −G(v, w)`, so `G(v, w) = 0`. On K_±,
`G = ±(GJ)|_{K_±}`, and `GJ ≻ 0` makes these ±definite. Sylvester's law
fixes the dimensions. ∎

**Lemma L1 (sector rigidity).** For every admissible configuration:
`ran P_eps = K_eps` and the G-sign of `ran P_eps` is `eps`. Hence
`sigma(X) = eps` **identically on the class** — an identity of
admissibility, not a property of any particular configuration.

*Proof.* Immediate from L0: `P_eps` is the projection onto `K_eps`
along `K_{−eps}`, and G is eps-definite on `K_eps`. ∎

*Structural comment.* L1 is exactly what the CH-REC probe's
partial-relabel attack was probing pointwise. The battleground named in
CH-REC §1.3 — "whether the structure contains any OTHER zero-cost sign
resource (basis relabeling, form-sign convention, dynamics reversal,
anchor exchange) that can reach the pair asymmetrically" — is settled
here in one stroke: the gate `G·J ≻ 0` welds the form-sign convention,
the symmetry choice, and the sector's G-sign into a single rigid
alignment over the ENTIRE moduli space. A resource that would flip the
sector without flipping eps must break the weld, and breaking the weld
is leaving the class (probe controls `partial-flips-rejected`,
`gate-load-bearing`).

**Lemma L2 (charge positivity and direction rigidity).** For every
admissible configuration and EVERY state Psi: `q(Psi) ≥ 0`, with
equality iff `P_eps Psi = 0`. Consequently, on every witnessed state
sequence — in particular every witnessed trajectory of any dynamics,
admissible or not, forward or reversed —
`d = sgn(N_final) = sgn(mu·eps·Σq) = mu·eps`.

*Proof.* `P_eps Psi ∈ K_eps` and G is eps-definite there (L0), so
`eps·G(P_eps Psi, P_eps Psi) ≥ 0` with the stated equality case. The
register total is `mu·eps·Σ_k q(Psi_k)` with `Σq > 0` on witnessed
sequences. ∎

*Structural comment.* d reads (mu, eps) and NOTHING else: not U, not
tdir, not the basis, not the state beyond witnessing, not (G, J) beyond
admissibility. The record law's sign field factorizes completely.

**Corollary (observable factorization).** On witnessed zero-import
configurations the observable map is

> `Obs(X, Psi) = (sigma, d) = (eps, mu·eps)`, so `sigma·d = mu`.

The pair is a **faithful copy of the discrete data (eps, mu)**. Every
continuous datum of a configuration — the form, the symmetry, the
dynamics, the state — is observable-sign-inert. And the import counter
is not bookkeeping: `mu = sigma·d` is itself an observable, the *split
parity* of the pair.

**Remark (shape robustness).** The factorization is stable under
class-shape quibbles about the record law: replace q by ANY
structure-derived nonnegative charge (the mirror charge, the full
majorant norm `⟨Psi,Psi⟩_J`, any monotone reweighting f(q) ≥ 0) and
d = mu·eps still holds wherever witnessed. In any record law of shape
`N += (sign)·(nonnegative charge)`, the only sign slot IS the sign, and
derivedness pins it to eps up to mu. The one-bit price does not depend
on which admissible charge drives the register.

---

## 3. The theorems

**Theorem A (exhaustive co-flip; P1 at theorem grade).** Let `(X, Psi)`
be zero-import and witnessed, and let `g` be ANY operation with
`g(X, Psi) = (X', Psi')` zero-import and witnessed. Then

> `sigma(X) = d(X, Psi)` and `sigma(X') = d(X', Psi')`.

Consequently g flips the sector sign iff it flips the record direction.
No zero-import operation splits the pair — over ALL operations, with no
inventory qualifier.

*Proof.* By L1 and L2, `(sigma, d) = (eps, eps)` at the source and
`(eps', eps')` at the target: both lie on the diagonal
`Δ ⊂ {±1}²`. Any map between diagonal points flips both coordinates or
neither. ∎

*Why the inventory was scaffolding.* While `sigma = eps` was only a
checked instance on one base structure, the adversarial inventory was
the honest instrument — the content of the claim really was "no hidden
resource in the structure," and the only way to probe it was to attack.
L1 converts the checked instance into an identity of admissibility, and
then exhaustiveness is one line. The enumeration did not become wrong;
it became a corollary.

**Theorem B (exact price; P2 at theorem grade).** On witnessed
configurations of the envelope class C:

> `(sigma, d) = (eps, mu·eps)`, equivalently `sigma·d = mu`.

Hence: (i) a split (`sigma ≠ d`) obtains iff `mu = −1` iff the import is
exactly 1 — **necessity and sufficiency**; (ii) the import group
Z/2 = {mu} acts simply transitively on {diagonal, antidiagonal}: one
paid bit always splits, a second paid bit restores diagonality, and no
zero-import dressing composed around a paid bit changes its class;
(iii) which split occurs is also determined: M alone flips the direction
with the sector fixed; M composed with the payload flip flips the sector
with the direction fixed. The N → 5 boundary of CH-REC is the fiber
structure of the observable map, not an inventory fact. ∎
(*Proof:* the display is L1 + L2; (i)–(iii) read off from it.)

**Corollary C1 (P3 at theorem grade: propagator independence).**
`d = mu·eps` holds for arbitrary state sequences with q witnessed — in
particular for ANY dynamics whatsoever, including maps that are not
Krein-unitary and not grading-preserving (both dynamics axioms
violated). Dynamics reversal inertness (CH-REC's `time-reversal-inert`,
the dossier's P3) is the trivial special case. The arrow is stored
entirely in (record law, eps); the propagator never touches it. (Probe
check `propagator-independence` drives the register with a deliberately
inadmissible step matrix and the direction still reads mu·eps.)

**Corollary C2 (the partial-flip obstruction, explained).** Every
"split attack" of the form *flip one structural sign and not its
partner* (J → −J with G fixed; G → −G with J fixed) exits the class:
`G·J` changes sign and the gate fails. Every "split attack" of the form
*flip both* (the total flip F, Section 4) stays in the class and is
inert. The attack surface is closed structurally: partial flips are
inadmissible, total flips are gauge.

---

## 4. Theorem C: the operation group's observable shadow, the benign miss, and the D1 continuum

### 4.1 The observable shadow

**Theorem C.** (i) The action of any operation family on the observable
pair factors through `Z/2 × Z/2`, generated by

- `[E]` (payload flip): `(sigma, d) ↦ (−sigma, −d)` — the co-flip;
- `[M]` (paid insert): `(sigma, d) ↦ (sigma, −d)` — the split, import 1;

and the zero-import subfamily lands in the diagonal subgroup
`{1, [E]} ≅ Z/2`. (ii) The enumerated CH-REC inventory {E, Rl, T}
already realizes the full zero-import image {1, [E]}: **nothing
observable was missed** by the enumeration. (iii) The kernel of the
observable action contains everything else the enumeration did not
test: all covariant relabels `R_S`, S ∈ GL(K) (Obs is basis-invariant);
the total form flip `F: (G, J) → (−G, −J)` (Section 4.2); every
deformation of the fundamental symmetry within `J(G)` (Section 4.3);
every dynamics substitution `U → U'`; tdir; every state map. (iv) The
adjoint-reversal `U → Uᵀ = G U⁻¹ G⁻¹` is a relabel-conjugate of the
dynamics reversal, hence also kernel.

*Proof.* (i) is the Corollary of Section 2 read as a statement about
maps: any operation moves `(eps, mu) ↦ (eps', mu')`, and Obs transports
accordingly; the four possible actions on the pair form Z/2 × Z/2 with
the listed generators. (ii)–(iv): each listed family fixes (eps, mu)
(relabels, F, T, dynamics substitutions, state maps) or realizes
`eps ↦ −eps` (E); apply the Corollary. ∎

This is the group-theoretic content promised by Lens 1: the operation
"group" is enormous (a groupoid containing all of GL(K), the
fundamental-symmetry continuum, and arbitrary dynamics substitutions),
and its observable shadow is exactly `Z/2 × Z/2` — payload times import
— with the zero-import shadow the diagonal Z/2.

### 4.2 The benign miss (first-class finding)

The swing instruction asked whether the enumerated inventory generates
the full group "or find what was missed." A genuine miss exists:

> **F, the total form flip** `(G, J) → (−G, −J)`, U, eps, tdir, mu
> fixed. It is admissible (`(−G)(−J) = GJ ≻ 0`), involutive,
> zero-import, and was NOT in the CH-REC generator inventory as a
> standalone operation. (The probe's block-swap relabel realized a
> conjugated cousin on the (2,2) base structure — S_SWAP happens to
> send (G0, J0) to (−G0, −J0) — but a relabel also transports U and the
> state; F does not. On a configuration whose U fails to commute with
> any such S, F is not a relabel composite: it is an independent
> generator.)

Adjudication: F is **benign, and provably so in advance** — Theorem A
guaranteed any miss must be diagonal before F was ever written down,
which is the practical meaning of exhaustiveness. Its exact action
(probe check `benign-miss F`): the observable pair is FIXED, while the
charge assignment genuinely moves — `q ∘ F = mirror-charge`, i.e. F
exchanges which subspace carries the "physical" charge and co-flips the
form sign so that every SIGNED observable is unchanged. F is the
ADAPTER2-01 anchor exchange as an explicit operation: the relational
relabeling of a balanced signed graph's two global anchors, with no
canonical positive choice, now sitting demonstrably in the kernel of
the observable action.

**The two Z/2's, cleanly separated (the withdrawn ratification's
failure mode, at theorem grade).** The class carries two distinct
Z/2 moves that superficially resemble each other:

- `[F]` — anchor exchange: gauge; kernel of Obs; flips the LABELING
  (which sector is called physical, which register sign is called
  positive) while fixing every G-signed observable;
- `[E]` — payload flip: physical; generates the zero-import image;
  flips both signed observables together.

Their composite `E∘F` — flip the anchor naming AND the payload binding
together — is observably in class `[E]` (co-flip). This is exactly
D1's joint anchor flip `(B, C) → (−B, −C)` (d1-coperator-build §2b,
"sector selection and record direction CO-FLIP — the single Z/2 is the
joint anchor naming"): D1's move is the E∘F composite at presentation
level, and its observable class is the payload bit, consistent with the
audit's typing. The 2026-07-15 ratification failed by conflating the
two Z/2's; here they are separated by a theorem: one is kernel, one is
image.

### 4.3 The continuous families: connected components and the D1 continuum

The swing instruction requires the continuum handled explicitly. Two
statements, one proved and one witnessed:

**Proposition (contractibility of the symmetry space).** For fixed G of
signature (p,q), the set `J(G)` of fundamental symmetries is
parametrized bijectively by the strict contractions
`T: K_+⁰ → K_−⁰` (angle operators): every maximal G-positive subspace
is the graph of a unique such T, it determines J uniquely
(`K_− = K_+^{⊥G}`), and the strict contractions form a CONVEX set.
Hence `J(G)` is contractible — in particular connected.

*Proof sketch.* Fix a reference decomposition `K = K_+⁰ ⊕ K_−⁰` (L0
for any reference J). A subspace W of dimension p is maximal
G-positive iff it meets K_−⁰ trivially and the induced form is positive
definite, iff W = graph(T) with `I − TᵀT ≻ 0` (computing G on
graph vectors), i.e. T a strict contraction w.r.t. the definite norms.
Given W, its G-orthogonal complement is negative definite of dimension
q, and J = P_W − P_{W^⊥G}. Contractions: `‖(1−t)T₀ + tT₁‖ < 1` by
convexity of the operator norm. ∎

**Consequences (the connected-component argument).**

1. `Obs` is constant — equal to `(eps, mu·eps)` — on all of `J(G)`, by
   L1/L2. So the ENTIRE continuum of admissible fundamental symmetries
   (equivalently, of admissible C-operators: same object, `C² = I`,
   `G·C ≻ 0`, here restricted to the finite class) lies in ONE
   connected component on which the observable pair is frozen. **A Z/2
   of observable content requires two components, and the continuum has
   one.** The zero-import connected components carry no bit; the
   co-flip is a π0-level move: it changes the locally-constant datum
   eps, which no continuous path of configurations can do.
2. This is exactly the D1 situation, now at theorem grade for the
   class: D1 found that at gu's exactly-degenerate vacuum anchors the
   admissible C's form a continuum (hyperbolic boosts) and dynamics
   selects none — and typed the continuum as "a continuum datum, not
   one bit." The proposition sharpens that typing into a proof shape:
   the continuum COULD NOT have carried the bit, because it is
   connected and the observable pair is constant along it; the entire
   observable sign content of the completion datum is the discrete
   pair (eps, mu) — one payload bit at zero import, per Theorem B.
   (Honest scope: D1's continuum lives on the interacting toy, not
   literally inside C_0; the statement proven here is the C_0-class
   image of that situation — fixed G, J free in `J(G)`, degenerate
   maximal-commutant dynamics. The probe's `continuum-inert` check
   walks a rational path of five distinct J's under U = I and U = J_t
   and watches the pair sit frozen at (eps, eps).)
3. What the continuum DOES move: everything Obs does not see — which
   states are confined, the charge values q(Psi), the operational
   content D1 cares about. "Inert" is a statement about the signed
   pair, not a claim that the C-choice is operationally empty. The
   payload typing that cuts the continuum to the anchor pair
   (loop-coherence, J_quat-commutation — CH-QM's card) is an input
   from elsewhere in the program and is neither used nor re-derived
   here.

---

## 5. Machine check

Script: `tests/channel-swings/h1_exhaustiveness_probe.py` — standalone,
stdlib-only, exact rational arithmetic, deterministic (seeded),
p2c-fixture style. Run 2026-07-19, **exit 0, headline
`8 [E] + 3 [F] = 11`** (setup `[T] = 2` excluded).

Epistemic role (combinatorialist's ruling, binding): the QUANTIFIERS are
carried by the proofs in Sections 2–4; the script provides (a) finite
witnesses of the lemmas on a widened moduli sample that the original
CH-REC probe never had — it never left its base structure (G0, J0,
S_SWAP) — and (b) failing controls demonstrating the checks can fire.

| check | content |
|---|---|
| [T] setup ×2 | 8 base configs; 12 random-relabel configs (dense G, non-diagonal J, 6 random S ∈ GL(4,Q)); 20 exotic-J configs from the strict-contraction parametrization; exotic J's distinct from J0 and from each other |
| [E] L1 sector-rigidity | `sigma = eps` across all 40 configs × both eps — the weld holds on dense forms and exotic symmetries, not just base |
| [E] L2 direction-rigidity | `d = mu·eps` on every witnessed trajectory, both mu strata; PLUS a live unwitnessed instance (generic state exactly in a relabeled mirror sector) where `d = 0` exactly — no direction, never a wrong one (P10's witness structure at the theorem's edge) |
| [E] Theorem-A all-maps | 200 arbitrary ordered pairs of zero-import witnessed instances treated as operation instances (no structure assumed): the pair is diagonal at both ends; no map of any kind splits |
| [E] Theorem-B price | all four (eps, mu) strata on base + relabeled + exotic configs: `(sigma, d) = (eps, mu·eps)` and `sigma·d = mu` — the import counter is the split parity, observable |
| [E] 32-composite table | all composites of {E, F, Rl(random S), T, M} on three config families: zero-import ⟹ diagonal with flip iff E present; split iff M present, cost exactly 1; which-split determined by E's presence; F/Rl/T never contribute |
| [E] benign-miss F | F admissible, zero-import, inert on the pair, `q ∘ F = mirror-charge` ≠ q — gauge for the pair, genuinely moving the charge assignment |
| [E] continuum-inert | rational path of five distinct J_t (convex contraction path), degenerate maximal-commutant dynamics (U = I and U = J_t): every point admissible, pair frozen at (eps, eps) — the D1-shape connected-component witness |
| [E] propagator-independence | register driven by a deliberately NON-Krein-unitary, NON-grading-preserving step matrix: direction still mu·eps — P3's theorem-grade upgrade |
| [F] partial-flips-rejected | G → −G alone and J → −J alone inadmissible at every sampled config — the weld, sample-wide |
| [F] gate-load-bearing | an involution J′ with G·J′ symmetric-but-INDEFINITE: rejected by the gate; with the gate bypassed, the selected sector is not even G-definite (`sector_sign` raises) — without `G·J ≻ 0`, L1 has no floor |
| [F] mu-import-detected | the only splitting move is flagged at import cost exactly 1 |

One mid-build finding worth recording: the first run FAILED L2 — a
generic state sat exactly in the mirror sector of one random-relabel
configuration, making its trajectory unwitnessed (`d = 0`). That is not
an L2 counterexample (L2 quantifies over witnessed trajectories); it is
the orientation-witness edge case arriving uninvited, and the check now
asserts the sharp dichotomy: witnessed ⟹ `d = mu·eps`; unwitnessed ⟹
`d = 0` exactly. The widened sample thus exercises P10's witness
structure at a place the original probe only reached via the vacuum.

---

## 6. Referee close: R1 and R2 re-scored against the theorem

The hostile-referee lens closes the wave, per the swing instruction.
Both objections are re-scored at the strength they were originally
written; the dossier's ledger is NOT edited here (Section 7 lists the
proposed rewrites for its next assembly pass).

### R1 (triviality-in-C_0) — re-scored

*Original strength:* "You defined the record direction through eps; the
co-flip is a definition, not a theorem. P1 is circular." *Original
disposition:* answered with a partial concession — P1 standing alone is
thin; frame the paper on P2 + P4 + P9.

*Re-score.* The circularity objection loses its remaining target. The
content of P1/P2 is now localized where a referee can weigh it:

- **L1** — the converse direction the definition does not touch. That
  NO structural resource (form sign, symmetry choice, basis, dynamics,
  anchor naming) can move the sector's G-sign against eps is a rigidity
  property of the admissibility gate `G·J ≻ 0`, proven over the whole
  moduli space. The gate is load-bearing, and demonstrably so: remove
  it and sector rigidity collapses (probe control). This is a theorem
  about the structure, not a restatement of a definition.
- **Theorem B's biconditional** — the price. `sigma·d = mu` makes
  "exactly one bit" an identity with necessity AND sufficiency, and
  makes the import counter itself observable. A definition cannot
  supply a biconditional against every operation including
  dimension-changing and discontinuous ones.

*Standing residue (new concession, carried):* the theorem is
ELEMENTARY — two lemmas of finite-dimensional Krein linear algebra and
a one-line factorization. Its value is (a) the exact price statement,
(b) the closure of the exhaustiveness debt, and (c) the relocation of
the attack surface onto the class axioms; it is not proof depth. The
dossier's framing rule — the paper stands on P2 + P4 + P9 with P1 as
the class-level lemma — remains good editorial advice, now with P1/P2
at theorem strength rather than enumeration strength. R1's editorial
concession stands; its mathematical core is discharged.

### R2 (class-generality / gerrymandering) — re-scored

*Original strength:* "C_0 is bespoke, and the 'exactly one bit' price
may be an artifact of the class boundary. STANDING CONCESSION
(un-rebutted): the enumerated inventory has no exhaustiveness proof;
until G-A1/G-A2 are done, 'no zero-import operation splits the pair'
means 'none in the enumerated inventory,' and a referee who insists the
abstract say exactly that is right."

*Re-score, in two halves:*

- **Exhaustiveness half: DISCHARGED** (this swing, G-A1). The claim now
  quantifies over ALL operations between zero-import configurations —
  a quantifier strictly stronger than any group formulation, subsuming
  the enumerated inventory, the found miss F, all continuous families
  including the D1 continuum, and operations nobody has proposed yet.
  The abstract of a Tier-A note may state the class-level claim
  unqualified BY INVENTORY: "no zero-import operation splits" now means
  exactly that, within the class. The signature restriction also
  relaxes: Theorems A/B hold at any finite (p,q), p,q ≥ 1 — the
  (n,n)-specific structure is needed only for the balanced two-anchor
  geometry (F's habitat), partially advancing G-A3.
- **Class-boundary half: STANDING, restated sharper.** The theorem's
  writ ends at the class axioms: action grade, finite dimension, the
  record-law shape of the W229 lineage (M1–M6 as the definition). The
  cohomological/BV grade (G-A2) has more structure than the class sees
  — there the sector exists only through the differential, L1's
  eigenspace-splitting argument does not port as written, and the
  referee's hostile scenario (a zero-import split visible only at that
  grade) remains pre-registered and live. Likewise untouched: whether
  GU's actual law is a member (T3/P9, conditional on D1/D2) — the
  theorem RAISES the stakes on membership, since the mathematics now
  closes every escape within the class, leaving the axioms and the
  membership audit as the entire honest attack surface.

*Net:* R2 moves from "standing, un-rebutted" to "half discharged, half
standing-by-boundary." The required abstract qualifier changes from
"enumerated inventory" to "finite-dimensional class, action grade."

### What the theorem does NOT do (boundary of the win)

1. No cohomological statement (G-A2 open; H-REC-CAUS untested).
2. No membership statement: T3/P9's MEMBER-conditional verdict and its
   D1/D2 dependencies are unchanged; nothing here bears on whether GU's
   built law satisfies the axioms — only on what follows if it does.
3. No physics hardened: no continuum, no field theory, no stat-mech
   coarse-graining (G-B3), no cosmological channel movement (O1).
4. No new payload accounting: N ≤ 4 stands exactly as before,
   conditional exactly as before; the theorem sharpens the price of the
   N → 5 boundary, not the count.
5. The elementarity concession above is real: a referee may fairly say
   "once stated correctly, this is an exercise." The reply is that
   stating it correctly WAS the gap (G-A1 named it "days-to-weeks"),
   and that the exercise closes a standing concession with a
   strictly-stronger-than-requested quantifier. The strength of the
   result is exactly the strength of the class axioms — no more, no
   less — and the program's honest exposure is now concentrated where
   the audit methodology already operates.

---

## 7. Proposals for the steward (no edits made outside this file + probe)

Single-file discipline: this swing writes this document and the probe,
nothing else. For the dossier's next assembly pass, the following
rewrites are proposed (steward/parent's move, per the repo's promotion
conventions):

1. **P1, P2 epistemic tags:** ENUMERATED → THEOREM (C_0, action grade,
   finite dimension, any signature (p,q), p,q ≥ 1), receipt this
   document §2–3 + `h1_exhaustiveness_probe.py` (exit 0, 8 [E] + 3 [F]).
2. **P3 tag:** ENUMERATED → THEOREM (corollary C1, propagator
   independence — strictly stronger than dynamics-reversal inertness).
3. **Concessions ledger item 2:** rewrite from "inventory
   exhaustiveness unproven; abstract must say 'enumerated inventory'"
   to "exhaustiveness proven at action grade/finite dimension over all
   operations; standing qualifier narrows to the cohomological lift
   (G-A2) and the class boundary."
4. **Gap G-A1: CLOSED** (this swing). G-A4 (Lean) is now cleanly
   stateable: the natural target is L0–L2 + Theorems A/B over the
   abstract class — finite-dimensional real bilinear algebra, no
   analysis; the probe's exact-rational structure is a direct guide.
5. **New kernel fact worth a dossier sentence:** the anchor exchange
   (ADAPTER2-01's relabeling symmetry) is now an explicit operation (F)
   PROVEN gauge for the observable pair, and D1's joint anchor flip is
   its E-composite — the two-Z/2 disambiguation at theorem grade.

## 8. What remains (hardening queue after H1)

- **G-A2 (cohomological grade)** — now the sole locus of R2's surviving
  mathematical risk. Needed: a cohomological analog of L1 (a K-grading
  induced on cohomology with a positivity gate playing the `G·J ≻ 0`
  role for representatives); the BV-bicomplex register extension named
  by CH-REC gap G2 / hypothesis H1 is the test vehicle.
- **G-A3 residue** — Theorems A/B are now general-(p,q); what remains
  class-specific is the balanced two-anchor geometry and the
  (7,7)-fork behavior of the package (P6's scope changes per class).
- **G-A4 (Lean)** — unblocked and well-shaped; see §7 item 4.
- **G-B1/G-B2/G-B3, G-C0/G-C1** — untouched by this swing.
- **T3/P9/D1/D2** — untouched and now carrying MORE of the total load:
  with the class mathematics closed, membership is the headline's
  entire external risk, exactly as R5's concession said.

## 9. Boundary

Conditional work under the standing axiom, R0_COND working grade. Files
written: this document and `tests/channel-swings/h1_exhaustiveness_probe.py`
(run 2026-07-19, exit 0, headline `8 [E] + 3 [F] = 11`, setup
`[T] = 2` excluded). No claim-status, canon-verdict, scorecard,
register, ledger, or public-posture moves; no edits to the dossier,
CH-REC exploration, D1 exploration, or any sibling probe; no cross-repo
writes; no external actions; no git operations. bar(b) = finality-axis
polarity remains OPEN and is nowhere reasserted; the killed-selector
ledger is respected; N ≤ 4 stands conditional on T3/P9/D1 exactly as
before this swing — sharper in price, unchanged in condition.
