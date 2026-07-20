---
artifact_type: exploration
doc_type: results_of_preregistered_check
status: "Execution of the pre-registered trit-internal successor check (binding: explorations/prereg-trit-internal-successor-2026-07-20.md, commit 6b384c5). OUTCOME: K-a (NOT CANONICAL) -- the N4-identified Z/3 cannot occupy the trit-anchor role without a new choice beyond the admissible inversion. The N4 data canonically supplies the TARGET side of the mod-3 matching (the canonical cube roots in the commutant scalars, unique up to inversion) but supplies NO fiber-side Z/3: the trit remains external, the minimal input stays Z/6, the N4 identification is arena-side only."
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (pre-registered successor executed)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
preregistration: "explorations/prereg-trit-internal-successor-2026-07-20.md (commit 6b384c5); hypothesis, test, allowed freedom, and outcome conditions executed exactly as bound; no mid-flight scope change; the N6 no-convention-shopping lesson honored"
probe: tests/channel-swings/trit_internal_check_probe.py
grade: "COMPUTED (float64 with exact structural anchors; the character chain in exact Fraction arithmetic; the battery machinery imported UNMODIFIED from the f513fcf probe and re-run live inside this probe). No claim/canon/verdict/posture movement."
related:
  - explorations/prereg-trit-internal-successor-2026-07-20.md
  - explorations/conditional-forcing-minimal-input-2026-07-20.md
  - explorations/n4-two-z3s-2026-07-20.md
  - explorations/n6-fingerprint-2026-07-20.md
  - tests/channel-swings/conditional_forcing_probe.py
  - tests/channel-swings/n4_two_z3s_probe.py
  - tests/channel-swings/k1_reframe_probe.py
sources:
  - "P. Olum, 'Mappings of manifolds and the notion of degree' (Ann. of Math. 1953) -- r^2 pinning; both Z/3 generators give r^2 = 1 mod 3 (cited via the parent probe, re-verified exactly)."
  - "Adams, On the groups J(X) IV -- e_KO(nu) = 1/24 (via the N4 probe's frozen table inputs, imported live)."
---

# The trit-internal check (pre-registered successor, executed)

## 0. What was bound, and what fired

The binding (commit 6b384c5) fixed everything before any computation looked:
the hypothesis (N4's frozen Z/3 already supplies the trit half of the minimal
Z/6 input), the test (construct the candidate anchor from the N4
identification data ONLY -- rho characters, Phi maps, admissible inversion --
and run the EXACT f513fcf sufficiency battery, imported unmodified), the
allowed freedom (the inversion {Phi_D, Phi_B} and nothing else), and the three
outcome conditions.

**Outcome fired: K-a (NOT CANONICAL).** The N4 Z/3 cannot occupy the
trit-anchor role without a new choice beyond the inversion. The trit remains
external; the minimal external input stays Z/6 = one bit x one trit; the N4
identification is arena-side only. Per the binding, this adverse outcome
stays adverse: the sharpenings recorded below are boundary data, not saves.

Probe: `python tests/channel-swings/trit_internal_check_probe.py` -- ALL
PASS, 5 [E] + 3 [F] (setup [T] = 2), exit 0, deterministic; it re-runs the
full N4 probe AND the full conditional-forcing battery (with k1 and phase0
nested inside) live, so every receipt cited here is refreshed in the same
run that reads the new verdicts.

## 1. What the N4 data DOES supply: the target side, canonically

The trit-anchor role (f513fcf) is a mod-3 equivariance constraint on oracle
transports f: fiber-core S^3 -> commutant S^3. It has two halves: a Z/3
ACTION on the fiber (an axis), and a matched winding onto the canonical cube
roots of unity in the commutant scalars. The check constructs what the N4
data can reach:

- **The chain** chi = exp(2 pi i * e_KO o Phi): monodromy characters ->
  <J(k)> = {0, 8nu, 16nu} -> {0, 1/3, 2/3} -> {1, omega, omega^2}. Exact
  Fraction arithmetic end to end: chi is an injective character;
  chi_D(alpha_1) = omega, chi_B(alpha_1) = omega^2; the two differ by
  exactly complex conjugation = the admissible inversion; the admissible set
  (recomputed live in the imported N4 probe) has size exactly 2.
- **The landing set is canonical.** The image is the cube-root subgroup of
  the C-linear commutant scalars -- the same canonical Z/3 the N6 node
  identified as THE distinguished order-3 subgroup of the frozen commutant
  ({omega I, omega^2 I}, unique up to inversion). And the trit slot of the
  Z/6 phase reference is exactly the square of the sixth root
  (zeta_6^2 = zeta_3, exact).
- **The inversion is harmless to the count**, as the binding anticipated:
  Olum's pinning gives r^2 = 1 mod 3 for BOTH generators. Nothing in the
  count can distinguish Phi_D from Phi_B.

So the identification arrives at the commutant scalars with no new choice.
If the trit-anchor role were target-side only, the hypothesis would stand.
It is not.

## 2. What the N4 data does NOT supply: the fiber side (the decisive computations)

The role requires the Z/3 to ACT on the fiber-core S^3 (the spin-lift family
parameter). The probe exhausts every frozen route from the N4 landing set to
the fiber:

1. **Scalars pass through the family without moving it.** For both habitat
   pins, generic fiber points, and generic states:
   omega^m (Lambda(v) psi) = Lambda(v) (omega^m psi) at machine identity.
   The operator realization of the N4 trit is C-linear-scalar, and scalars
   commute with every C-linear operator: the induced action on the fiber
   parameter is the IDENTITY. A trivial fiber Z/3 is not an anchor.
2. **The conjugation route delivers a bit, never a trit.** J-conjugation
   preserves the family and acts on the fiber as v -> vbar (quaternion
   conjugation; defect < 1e-13, both pins) -- an ORDER-TWO map. Generic
   commutant conjugations, and specifically the non-scalar order-3 elements
   cos(2pi/3) + sin(2pi/3) J, BREAK the family span (residual O(0.3-0.5)):
   they induce no fiber map at all. And the family-normalizing subgroup of
   the commutant has NO order-3 elements outside the scalars: every J-coset
   element squares to -I exactly ((aJ)^2 = -|a|^2), hence has order 4. The
   only native fiber symmetry the commutant supplies is one more Z/2 -- the
   geometry hands out another bit, never the trit.
3. **Therefore:** no frozen datum carries the N4-identified Z/3 -- which
   lives entirely on the commutant/character side -- to a nontrivial action
   on the fiber. The fiber-side axis is not in the N4 data, and the
   commutant offers no bridge. This is the same structural lesson N6 found
   one level up (fiber rotation vs slot permutation, no frozen converter),
   now landed on the fiber-core itself.

## 3. The battery, re-applied exactly as bound

The unmodified f513fcf probe re-runs clean inside this one (exit 0; generic
Z/6 degrees [1, 1]; twisted member +7; every power certificate of the degree
counter refreshed live). Against it, the candidate constructions:

- **T1 -- the identification transported literally** (trivial fiber action,
  weight omega): the demand f(v) = omega f(v) is INFEASIBLE for every
  sphere-valued map; the defect is the constant |1 - omega| = sqrt(3) on
  every sampled member (identity, the degree-3 join map, a generic Z/6
  survivor; spread < 1e-12). The type is EMPTY: no admissible transport
  exists, nothing is forced.
- **T2 -- the identification as a vacuous constraint** (trivial action,
  trivial weight): the constrained type collapses to X1, the bit alone --
  and the battery's own order-killer sits inside it live: the exactly
  deck-odd join map (z1^3, z2) with certified degree +3, k = 192 = 0 mod
  24, order 1. Not forcing.
- **Nontrivial occupancy requires the axis, and the battery cannot select
  it.** A conjugated axis (u' = q_r zeta_3 q_r^{-1}; exactly order 3;
  distance 1.22 from both members of the canonical-coordinates axis
  subgroup, hence outside the inversion orbit -- the inversion relabels a
  generator WITHIN an axis, it never moves the axis) passes the IDENTICAL
  battery: composed members are axis-2 equivariant at < 1e-12 with the SAME
  canonical scalar weights, exactly deck-odd, with certified degrees +1
  (generic) and +7 (twisted; provably NOT axis-1 equivariant, defect O(1)),
  two regular values each on the unmodified power-certified counter --
  every degree = 1 mod 6, order 3 forced in the axis-2 type exactly as in
  axis-1. The axis is invisible to every bound test. It is therefore a
  genuinely free choice, and the N4 data does not make it.

**Adjudication among the bound outcomes.** K-c requires the battery passed
with no choice beyond the inversion: it did not -- both no-choice candidates
fail (empty / vacuous), and every passing candidate imports an axis. K-b
("transports canonically but fails gates/degree") does not describe the
finding either: the canonical transport of the N4 trit to the fiber exists
and is the IDENTITY -- it lands outside the anchor role altogether rather
than inside-it-but-failing; the failure is at occupancy, not at gates or
degree. The condition that fired is K-a verbatim: occupying the trit-anchor
role requires a new choice (one fiber axis, an S^2 worth) beyond the
inversion. The residue is characterized exactly anyway, as K-b would have
demanded: what is missing is precisely the axis -- the same
transport/torsor-shaped external datum the program has now met from three
independent directions (ID-1/B.5, the N6 boundary finding, and here).

## 4. Controls (all three bound controls, demonstrated power)

1. **Scrambled-character trit FAILS.** (0, 1/3, 1/3) is rejected by the
   live N4 gate (not a homomorphism, not injective, no intertwiner); at
   battery level its demand pair is internally contradictory -- the honest
   equivariant member satisfies the k = 1 demand at 1e-15 and fails the
   scrambled k = 2 demand at |omega - omega^2| = sqrt(3); any exact
   solution of both is forced to |f| = 0, off the sphere.
2. **X1.5 scatter unchanged** in the unmodified live run: witnessed reader
   degrees {-1, +1, +3} with the 3-divisible member on a fully generic
   draw. Reading is still not anchoring.
3. **Planted weight-blind oracle still rejected** in the unmodified live
   run: passes the Z/2 deck shadow at exactly 0.0, fails G1 at exactly 0.0
   commutant reach, Borsuk-Ulam discontinuity witnessed (2.0 jump across a
   2e-9 gap).

## 5. Five-lens council (inline, answered in writing)

**Representation theorist.** The construction correctly separates the two
halves of an equivariance datum: a G-action on the source and a character
into the target. N4 supplies the character (exactly, and only up to the
unavoidable Aut(Z/3)); it supplies no source action, and the probe's
exhaustion is the right one -- the only frozen operators realizing the
character values are the C-linear scalars, whose adjoint action on any
C-linear family is trivial by Schur-trivial arithmetic, not by accident.
The normalizer computation is the load-bearing new fact: the fiber-facing
quotient of the commutant is Z/2 (scalars act trivially; the J-coset is
order-4 elements inducing the conjugation involution), and Z/2 has no
order-3 subgroup -- the obstruction is group-theoretic, not numerical. One
discipline note: the axis-2 battery pass must not be read as "any axis is
as good as the canonical one natively"; it says the SUFFICIENCY test cannot
see the axis, which is exactly why the axis is an import. Passed.

**Krein analyst.** No nondegeneracy claim in this check divides by a small
quantity: the pass-through identity is exact scalar arithmetic, the
J-conjugation action lands on Lambda(vbar) at 1e-15, and the span-break
residuals are O(0.3-0.5) against an orthonormalized fit -- comfortably far
from any tolerance. The G2-side of the battery is inherited unchanged from
the imported run (commutant Gram exactly orthonormal on confined states;
K_S twisted-commute 0.0), so nothing in this check touches the habitat
analysis. The one place a hostile reader should push -- whether the
family-span fit could hide a near-miss action -- is answered by the
residual's size: half the vector norm is unfittable. Passed.

**Stable-homotopy / degree specialist.** All degree reads use the imported
power-certified counter, refreshed live in the same run (+1/+3 known maps
inside k1; 1/3/7/9 separated inside the parent battery). The new reads
(axis-2 members: +1, +1 and +7, +7 on two regular values each) are
target-consistent and match the lens-space prediction 1 + 6Z for the
conjugated type, as they must: conjugating the axis conjugates the whole
type, and degree is conjugation-invariant. That invariance is exactly the
formal content of "the battery is axis-blind" -- the K-a mechanism is a
theorem of degree theory, witnessed, not just sampled. The mod-24
bookkeeping (16 mod 24 for c = 1, 7) is re-read from the live order24.
Passed.

**Statistician.** The check's negative is not a null result from
underpowered sampling: T1's infeasibility is a constant-defect identity
(spread < 1e-12 across 36 member-point samples), the normalizer obstruction
is exact arithmetic, and the axis-2 pass is a positive control
demonstrating the pipeline CAN pass a trit candidate -- so failure to pass
the N4-only candidates is discriminating. Control power is demonstrated on
all three bound controls, two of them re-run unmodified from the parent
probe (same seeds, same draws -- the scatter and the plant rejection are
bit-identical re-reads, the strongest form of "unchanged"). No p-values are
needed where the load-bearing steps are identities. Passed.

**Adversarial referee.** Attacks run: (a) *outcome shopping between K-a and
K-b* -- the adjudication is in Section 3 and I pressed it: K-b's wording
("transports canonically but fails gates/degree") would be a MORE
hypothesis-friendly reading, since it leaves the identification holding the
role-shaped object; the finding does not support it -- the canonical
transport is the identity map on the fiber, which is not a candidate that
fails, it is no candidate at all. K-a's wording ("cannot occupy without a
new choice") is the literal finding. (b) *convention-shopping the axis* --
the temptation the N6 lesson forbids: read the fixture's z1/z2 pairing (the
coordinate complex structure on v-space) as frozen and declare the axis
native. Rejected: the binding restricts inputs to the N4 identification
data, which nowhere references the fiber frame; and the axis-2 experiment
shows the battery cannot ratify any such reading -- a shopped convention
would be doing all the work. (c) *is the exhaustion exhaustive?* -- the
routes tested are left/right scalar transport, conjugation by every
commutant shape (scalar, J-pure, generic, non-scalar order-3), and the
normalizer's group structure; a route outside these would have to act on
the fiber through something other than the frozen commutant, and the N4
data contains nothing else operator-valued. (d) *does the axis-2 pass
smuggle in a rescue?* -- no: it is the instrument of the kill (it proves
axis-freedom), and its members are built by composing battery-native maps
with a fixed rotation, not by tuning. (e) *strongest surviving
hypothesis-side objection*: the target-side half IS canonically supplied,
and a future frozen datum tying the commutant scalars to a fiber axis would
complete the anchor with no further freedom -- recorded, and correctly
typed: that is a NEW pre-registered node with an import price, not this
check, whose adverse outcome stays adverse as bound. Passed as declared.

## 6. Receipts

- Probe: `tests/channel-swings/trit_internal_check_probe.py` -- ALL PASS,
  5 [E] + 3 [F] = 8 (setup [T] = 2 excluded), exit 0, deterministic;
  n4_two_z3s_probe re-runs clean inside it (exit 0, 27 checks) and
  conditional_forcing_probe re-runs clean inside it UNMODIFIED (exit 0,
  with k1_reframe_probe and phase0_torsor_checks nested live).
- Key witnessed values: chi_D(alpha_1) = omega and chi_B(alpha_1) = omega^2
  exactly (Fraction chain); scalar pass-through defect < 1e-14 (machine
  identity); J-conjugation vs Lambda(vbar) < 1e-13; family-span break
  residual >= 0.3 for generic and non-scalar order-3 conjugations;
  (aJ)^2 + 1 = 0 at 1e-15 (order 4, no order-3 outside scalars); T1 defect
  constant sqrt(3) (spread < 1e-12); axis-2 distance 1.22 from the
  canonical axis subgroup; axis-2 degrees +1, +1 and +7, +7; scrambled
  demand-2 defect sqrt(3).
- HEADLINE (verbatim from the run): recorded in Section 8 below.

## 7. Boundary

- Everything is fixture grade on the frozen (9,5) spine, R0_COND, both
  habitat pins, exactly as the parent lines; no Lean/lake; no claim, canon,
  verdict, or posture movement; no edits to any existing file; no commits
  by this executor.
- K-a is scoped exactly: the N4 identification data cannot occupy the
  trit-anchor role without one new fiber-axis datum. It does NOT say the
  identification is wrong (N4 stands as computed), and it does NOT shrink
  or grow the minimal input (Z/6 stands as computed at f513fcf).
- Boundary data, not a save: the commutant's native fiber-facing symmetry
  computed here is exactly Z/2 (v -> vbar) -- the program's recurring
  external-datum silhouette (one bit supplied natively at best, the trit
  always imported) now has a fourth independent witness. A frozen transport
  datum tying the commutant scalars to a fiber axis would collapse the
  external input to the payload bit alone; that is a NEW Joe-gated
  pre-registered node with its own import price, per the binding and the
  N6 precedent.
- Pauses for Joe.

## 8. Run headline (verbatim)

(to be pasted from the probe run below)
