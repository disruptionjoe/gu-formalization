---
title: "WHAT-IS-THIS wave, Swing 2 (THE BIT): what IS sigma, most fundamentally? Four inline personas (info theorist, spin/Clifford geometer, philosopher of physics, quantum-foundations theorist) each characterize sigma from their lens, then a synthesis. DEEPEST CHARACTERIZATION: sigma is ONE external degree-1 Z/2 holonomy class -- w_1(L_time), the spin/belt-trick obstruction to globally orienting the arrow-of-time line bundle over F~RP^3 -- and, read against the inside, that SAME class is a superselection charge / one oracle bit the internal (alpha-even) algebra provably cannot resolve (Schur Hom(triv,sign)=0). Geometry says what it IS; blindness says what it is FOR the inside. EXACT-AND-REAL: {w_1(L_time) = spin double-cover class = superselection charge = 1 Hartley/oracle bit = zero-inward-capacity} are one and the same object. ANALOGY: {'the thermodynamic/cosmological arrow of time', einselection/pointer-basis dynamics, 'Shannon H=1' absent the indifference prior}. INDEPENDENT CONSEQUENCE: sigma = w_1(L_time) pulls back to ZERO on the spin double cover S^3 (H^1(S^3;Z/2)=0), so 'the outside that can read the bit' is exactly the orientation/spin double cover -- the same S^3 as the base-uniting F<->S^3 map's target; plus a flagged CANDIDATE identity (Kramers T^2=-1 == belt-trick 2pi=-1)."
status: active_research
doc_type: exploration
created: 2026-07-21
wave: WHAT-IS-THIS
swing: 2 (THE BIT -- ontology of sigma)
method: "four personas INLINE in one worker (each in-character, then synthesize); NEVER one agent per persona; read-only"
inputs:
  - explorations/prereg-what-is-this-wave-2026-07-21.md
  - explorations/prereg-construction-swing-posit-sigma-cycle-2026-07-21.md
  - explorations/oracle-relative-prongI-info-exact-2026-07-21.md
  - explorations/shard-cycle-prong1-geometry-2026-07-21.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Swing 2 -- THE BIT: what IS sigma, most fundamentally?

Four personas reason independently and in-character below, then a synthesis
reconciles them. Discipline (binding): every characterization carries a MODE tag
-- **[EXACT-AND-REAL]** (a literal, computed/theorem-grade identity) or
**[ANALOGY]** (illuminating but not proven-identical / conditional on a posit).
Nothing is reported as forced that the banked facts do not force. The CLOSED
PREMISE (sigma is external) is input, never re-derived. No probe is run here: the
load-bearing computations this swing rests on -- Schur zero-inward-capacity
(`prongI`), `sigma = w_1(L_time)` and the `S^3 -> RP^3` lift (`shard-cycle-prong1`),
the `nulldim 1 -> 2` liberation (`W211`) -- are already machine-checked in the
cited receipts (each exit 0, deterministic); a fresh probe would only re-run them.
The one new independent consequence in Section 5 is already substantiated by the
existing `shard_cycle_prong1_geometry_probe.py` (the loop lifts to a path in `S^3`
from `v(0)` to `-v(0)`; the squared loop closes). Cited, not re-run.

---

## Member 1 -- the INFORMATION THEORIST

**Characterization.** sigma is exactly **one external bit**, and the honest root
of that "one bit" is a stack of three readings, only the innermost of which is the
deep one. (i) **Hartley** `[EXACT-AND-REAL]`: `sigma = log_2|Z/2| = 1`, a choice
among two, prior-free, definitional. (ii) **Shannon** `[ANALOGY]` until you posit
the alpha-symmetric indifference prior: `H(sigma) = 1` bit holds only under the
uniform `(1/2,1/2)` prior, which is canonical-by-symmetry (the only structure
acting on the slot is alpha, which swaps the two values) but is a max-entropy
posit, not a GU-derived probability. (iii) The load-bearing fact is neither of
those magnitudes but the **channel**: the inward channel `sigma -> internal` has
**literally zero Shannon capacity** `[EXACT-AND-REAL, theorem-grade]` -- `Hom(triv,
sign) = 0` (Schur) means every alpha-even observable is constant on an alpha-orbit,
so the two rows of the transition matrix are identical, so `I(sigma; internal) = 0`
for every prior, prior-free. Non-vacuous: the same algebra has full mutual
information (`2` bits) with the alpha-invariant world and exactly `0` with sigma.

**At root: Hartley or Shannon or Kolmogorov?** The deepest reading is
**Kolmogorov / oracle-relative** `[EXACT-AND-REAL]`. sigma is Goedel-independent of
GU's internal axioms (W211, five methods unanimous): no internal derivation
produces it. In relativized-computation terms that is precisely an **oracle bit** --
one bit the internal machine can query but provably cannot compute; algorithmically
incompressible relative to the internal theory. So the magnitude is Hartley (1
choice bit), the channel is Shannon (zero capacity, exact), and the *ontological
status* is Kolmogorov/oracle: the one undecidable bit relative to the inside. The
Shannon-entropy reading and the "hard import ceiling" (that GU imports no more than
sigma+tau+theta) are the ANALOGY layer -- the ceiling has no theorem (no
moduli-completeness result forbids a 4th datum; a continuum theta breaks even
finiteness).

**MODE: EXACT-AND-REAL** for {zero inward capacity; Hartley 1 bit; oracle/Goedel
bit}. **ANALOGY** for {Shannon `H=1` absent the indifference prior; the hard import
ceiling}.

---

## Member 2 -- the SPIN / CLIFFORD GEOMETER

**Characterization.** sigma **is** `w_1(L_time)` `[EXACT-AND-REAL, computed]` -- the
first Stiefel-Whitney class of the tautological timelike-line bundle over the metric
fiber `F = GL(4,R)/O(3,1) ~ RP^3` (`pi_1 = Z/2`). `L_time` is the arrow-of-time line
(the `-1` eigenline of the metric involution `I - 2P_L`); its unit section flips
sign around the canonical loop (`<v(1),v(0)> = -1`), so the bundle is **Moebius**,
`w_1(L_time) != 0`. That non-orientability -- the impossibility of consistently
orienting time around the loop -- IS the co-flip. Computed, canonical, program-native.

**Is sigma fundamentally a SPIN phenomenon of time's direction? Yes, exactly, and
precisely so.** The double cover carrying sigma's `-1` monodromy is `v ~ -v :
S^3 -> RP^3`, which is **connected** (`S^3` simply connected). An *orientation*
double cover of an *orientable* manifold is *disconnected* -- and `RP^3` is
orientable (`w_1(T RP^3) = 0`). Therefore sigma's cover is **NOT an orientation
cover of the base**; it is the **SPIN cover** `SU(2) -> SO(3)` (via `RP^3 ~ SO(3)`),
the belt-trick / 2pi-vs-4pi class `[EXACT-AND-REAL]`. So the "2" in the Z/2 is a
genuine spin datum: the sign a spinor picks up under a `2pi` rotation.

**The mandatory caution `[EXACT-boundary]`.** `H^1(RP^3; Z/2) = Z/2` is
one-dimensional, so *any* nontrivial Z/2 monodromy -- `w_1(L_time)`, the spin-cover
class, sigma -- is automatically the *same* class by pigeonhole. The identification
"sigma = spin class = `w_1(L_time)`" is therefore EXACT at the class level, but the
SEMANTIC content ("which bundle it is the `w_1` of") is carried by the physics (the
frozen packet: this class = the co-flip = time orientation), not distinguished by a
finer cohomological computation. And the falsified slogan must stay dead: sigma is
NOT "the two orientations of the shard circle" -- a circle is orientable
(`w_1(T S^1) = 0`), so its two directions are a *trivial-class torsor*, and
`0 != sigma`. The carrier is the line bundle / spin cover, not the circle.

**MODE: EXACT-AND-REAL** for {`sigma = w_1(L_time)`; the `S^3 -> RP^3` spin/belt-trick
cover; sigma is a spin obstruction of time's arrow-line}. **EXACT-boundary**: the
class-level identification is forced but the *semantic label* is physics-carried,
not cohomologically singled out.

---

## Member 3 -- the PHILOSOPHER OF PHYSICS

**Characterization.** sigma is welded to the **record arrow**: the holonomy
involution flips sigma AND the direction of record accumulation *together* (co-flip
weld, `r*sigma` alpha-invariant `= +1`), leaving the generation count untouched. So
sigma and the record arrow are "two costumes of one alpha-odd datum." The tempting
sentence is "sigma is the direction of time, made a discrete Z/2." **The precise
correction `[EXACT-AND-REAL]`:** sigma is not the arrow (a *section*) -- it is the
**obstruction** (`w_1`, a *class*) to choosing an arrow *globally and consistently*
around the loop. The record arrow is a local section of `L_time`; sigma is the twist
that makes any global choice sign-flip. They are welded because selecting a section
of a Moebius bundle around the loop forces the flip. So: "sigma = the topological
obstruction to a globally consistent direction of time; the record arrow is a local
section of the same bundle" is exact; "sigma = the arrow" is imprecise.

**"Dressed with but unable to read it" `[EXACT-AND-REAL]`.** The first person *has*
a definite record arrow -- an alpha-ODD, symmetry-breaking *lift/section* of the Z/2
torsor (you cannot accumulate records in no direction). But it *cannot read* the
sector VALUE: reading is an alpha-EVEN *map*, and no even map computes an odd datum
(blindness). Being *dressed with* sigma (possessing a section) and being *able to
read* sigma (possessing a valuation map) are two different fibrations of one
alpha-odd object -- `Hom(A,B)` (empty on the even part) versus a point of the
`B`-torsor (a broken-symmetry section). You experience a direction; you cannot
determine, by any internal measurement, which global Z/2 sector you are in, because
the two sectors are alpha-mirror images and every internal observable is alpha-even.

**Is it THE (thermodynamic/cosmological) arrow of time? `[ANALOGY]`.** The banked
object is specifically the **record** arrow (direction of record accumulation),
which is thermodynamic-*flavored* but is nowhere proven equal to an entropy gradient
or a cosmological expansion direction. Identifying the record arrow with the physical
arrow(s) of time is interpretation, not a computed identity. sigma is the discrete
Z/2 shadow of the record arrow (EXACT weld); "sigma = the thermodynamic/cosmological
arrow" is the ANALOGY.

**MODE: EXACT-AND-REAL** for {sigma<->record-arrow weld; sigma = obstruction (not
arrow); dressed-as-section vs blind-as-map}. **ANALOGY** for the identification with
THE thermodynamic/cosmological arrow of physics.

---

## Member 4 -- the QUANTUM-FOUNDATIONS THEORIST

**Characterization.** sigma is a **superselection charge**, and this is EXACT, not a
rhyme. A superselection rule is *precisely* the statement that no observable connects
two sectors -- the observable algebra is block-diagonal and the relative label
between sectors is unobservable. Here the internal observable algebra `A_int` is
*exactly* the alpha-even (block-diagonal) subalgebra, the two values `{+K_S, -K_S}`
are the two sectors, and `Hom(triv,sign) = 0` says no element of `A_int` has a
nonzero matrix element between them. That IS a superselection rule; sigma is the
central Z/2 charge labeling the sector. **Note the identity with Member 1: the
QF-theorist's "superselection charge" and the info-theorist's "zero-inward-capacity
1 bit" are the SAME Schur fact** (`Hom(triv,sign)=0`) in two vocabularies (algebraic
block-diagonality vs channel capacity). `[EXACT-AND-REAL]`.

**Einselection / pointer basis? `[ANALOGY]`.** sigma is "pushed at the seed + pulled
as an opaque token" -- the environment writes it (push), the system can only query it
as a token it cannot resolve (pull). This has the *structure* of einselection
(environment-set, internally-unreadable pointer label) but not its *dynamics*: no
decoherence process is banked. So einselection/pointer-basis is an illuminating
analogy; the exact statement is the static superselection one (algebraic, needs no
dynamics).

**A bridge worth flagging `[ANALOGY -> candidate lemma]`.** The source-packet freeze
protects sigma by **Kramers blindness**: no `J_quat`-commuting GU-native operator
reads the sector. Kramers' theorem rests on antiunitary time-reversal with `T^2 =
-1`. That `-1` is *the same shape* as Member 2's belt-trick sign (a `2pi` rotation
gives `-1`). So the reason sigma is *unreadable* (Kramers, quaternionic) and the
reason it is a *spin obstruction of time* (belt-trick `w_1`) may be one and the same
Z/2 sign. Flagged as an independent consequence in Section 5, not asserted.

**MODE: EXACT-AND-REAL** for {sigma is a superselection charge; = the same Schur/
blindness fact as Member 1}. **ANALOGY** for {einselection/pointer-basis dynamics;
the Kramers `T^2=-1` == belt-trick candidate identity}.

---

## SYNTHESIS -- the deepest characterization of what sigma IS

**One sentence.** *sigma is a single external degree-1 Z/2 holonomy class --
`w_1(L_time)`, the spin/belt-trick obstruction to globally orienting the
arrow-of-time line bundle over the metric fiber `F ~ RP^3` -- and, read against the
inside, that SAME class is a superselection charge / one oracle bit that the internal
(alpha-even) observable algebra provably cannot resolve (`Hom(triv,sign)=0`). The
geometry says what it IS intrinsically; the blindness says what it is FOR the inside.*

The four lenses are not four objects. They are **one class in `H^1(F;Z/2) =
H^1(RP^3;Z/2) = Z/2`** seen from four standpoints, and they split cleanly into two
tiers:

**Tier 1 -- LITERALLY THE SAME OBJECT `[EXACT-AND-REAL]`.** These are proven-identical,
not analogies:
- `w_1(L_time)` (geometer) -- the primary, most literal identity: a *computed
  cohomology class*.
- The **spin / belt-trick double-cover class** `S^3 -> RP^3 = SU(2) -> SO(3)`
  (geometer) -- the same class (one-dimensional `H^1` forces coincidence).
- The **superselection charge** (QF) and the **zero-inward-capacity 1 bit** (info) --
  these two are the *same Schur fact* `Hom(triv,sign)=0` in two vocabularies
  (block-diagonality / channel capacity). The info-theorist and the QF-theorist are
  describing one algebraic fact.
- The **Cech gluing obstruction** and the **loop fixed-point count** (banked
  three-route) -- the same `H^1` class.
- The **oracle / Goedel-independent bit** (info, Kolmogorov reading) -- the same
  class read as "the one bit the internal theory cannot decide" = "external."

The organizing distinction inside Tier 1: the **geometric/topological** reading
(`w_1` = spin class) says *what sigma is intrinsically*; the **observer-relative**
reading (superselection charge = 1 oracle bit = zero-capacity) says *what sigma is
FOR the inside* -- unreadable, external, exactly one bit. Same class, two faces:
intrinsic vs for-the-inside. The record arrow (Member 3) is the **section** of the
same bundle; sigma is its **obstruction/twist**; the co-flip weld is the exact tie
between section and class.

**Tier 2 -- ILLUMINATING ANALOGY `[ANALOGY]`** (not proven-identical / conditional
on a posit):
- "sigma = THE thermodynamic / cosmological arrow of time." The record-arrow weld is
  exact; equating the record arrow with entropy-increase or cosmic expansion is
  interpretation.
- "einselection / pointer basis." The environment-set-and-unreadable *structure* is
  exact; the decoherence *dynamics* is not banked.
- "Shannon `H = 1` bit." Conditional on the alpha-symmetric indifference prior; the
  Hartley `1` bit is exact, the Shannon reading is posit-dependent.
- "hard import ceiling (no 4th bit)." A well-posed conjecture, not a theorem.

**So, to the wave's four candidate answers:** sigma is *the direction of time* --
NO, it is the **obstruction** to a global direction of time (analogy to soften to
"discrete shadow of the record arrow"). sigma is *a spin obstruction* -- **YES,
exactly** (`w_1(L_time)` = spin cover). sigma is *a superselection charge* --
**YES, exactly** (`Hom(triv,sign)=0` is a superselection rule). sigma is *an oracle
bit* -- **YES, exactly** (Goedel-independent = one oracle bit relative to the inside;
Hartley-1, zero inward capacity). The two YESes and the "oracle bit" are the SAME
class; the arrow-of-time is that class's physical clothing.

---

## Independent consequences (flagged)

**IC-1 `[EXACT-AND-REAL]` -- the outside that can read sigma is the spin double
cover, and it is the same `S^3` as the base-uniting map.** `w_1(L_time)` pulls back
functorially along the double cover `p : S^3 -> RP^3`: `p*w_1(L_time) =
w_1(p*L_time)`, and since `H^1(S^3;Z/2) = 0` (simply connected), the pullback is
`0` -- `L_time` becomes *orientable/trivial upstairs*. So sigma **trivializes exactly
on the orientation/spin double cover**: the standpoint that can single-value the bit
is the two-sheeted cover `S^3`, not any internal chart. This is the precise
topological content of "pushed + pulled from outside, unreadable from inside" -- the
"outside" is literally the covering space where the Z/2 torsor is resolved. It is
*already substantiated* by the existing `shard_cycle_prong1_geometry_probe.py` (the
loop lifts to a path in `S^3` from `v(0)` to `-v(0)`; the squared loop closes -- i.e.
the monodromy dies upstairs). **Two productive convergences fall out:** (a) that
`S^3` is the SAME `S^3` targeted by the base-uniting `F <-> S^3` map that Swing 1
gates -- so the base-uniting map is (at the fiber) precisely the spin cover that
trivializes sigma, tying THE BIT to THE LEMMA; and (b) it hands Swing 3 (THE OUTSIDE)
a concrete candidate for "outside": the orientation double cover, a specific compact
`S^3`, not an unbounded beyond.

**IC-2 `[ANALOGY -> candidate lemma, testable]` -- Kramers `T^2=-1` == belt-trick
`2pi=-1`.** The unreadability of sigma (Kramers/quaternionic blindness: no
`J_quat`-commuting operator reads the sector) and its identity as a spin obstruction
(belt-trick `w_1`) may be one Z/2 sign, not two facts: the antiunitary time-reversal
whose square is `-1` would be the generator of `pi_1(RP^3)` realized on `L_time`. If
so, "why sigma is blind" and "why sigma is a spin obstruction of time" collapse to
the single `T^2 = -1` sign. Well-posed and checkable (does the antiunitary
time-reversal on `L_time` generate `pi_1(RP^3)` / act as the deck transformation of
`S^3 -> RP^3`?); flagged, NOT asserted -- the banked facts name Kramers blindness and
the belt-trick separately and do not prove the `-1`s coincide.

**IC-3 `[EXACT-boundary, discipline]` -- "sigma is a spin obstruction" is forced only
at the class level.** Because `H^1(RP^3;Z/2)` is one-dimensional, the geometry cannot
*single out* sigma from "any nontrivial Z/2"; the semantic content (this class = the
record co-flip = time orientation) is physics-carried. Do not upgrade the
class-level identity to a claim that geometry alone *selects* sigma. (This is the
same honesty the `shard-cycle-prong1` G-PARTIAL enforced.)

---

## Boundary

Exploration tier. One artifact written (this file); no probe run (the load-bearing
computations are consumed from the cited W211 / prongI / shard-cycle-prong1 / Q2
receipts, each already exit 0 and deterministic; IC-1 is substantiated by the
existing `shard_cycle_prong1_geometry_probe.py`, cited not re-run). GU otherwise
read-only. No edits to LANE-STATE, research-portfolio, NEXT-STEPS, any prereg, any
decision-tree, the frozen packet, any claim/canon/verdict/ledger file, or any other
agent's artifact. No commit, no push, no external actions. No movement of `bar(b)`,
`H59`, the count `{1,3}`, or public posture; the externality of sigma is the
program's closed premise (input, not re-derived), and sigma's VALUE remains the one
external Z/2 posit (p2c-owned per the tri-repo signed-graph result). Every claim
carries its MODE tag; the two YES identities (spin obstruction; superselection
charge) are EXACT, the arrow-of-time and einselection framings are ANALOGY, and the
sole candidate identity (IC-2, Kramers==belt-trick) is flagged as a conjecture, not a
result.
