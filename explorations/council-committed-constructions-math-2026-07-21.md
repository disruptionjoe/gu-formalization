---
title: "The math/formal council, committed: seven standalone constructions that each ASSUME their substrate is the fundamental ontology and build the full σ/τ/θ story from it (no synthesis, no ranking)"
status: active_research
doc_type: exploration
created: 2026-07-21
directed_by: "Joe direct chat, 2026-07-21 (run the 7-member math/formal council inline in one worker; each member assumes their substrate IS reality and builds the most committed full story that points at a falsifiable prediction; do NOT synthesize or rank)"
prong1_factual_update: "Coordinator, 2026-07-21: pi_1(F=GL(4,R)/O(3,1))=pi_1(RP^3)=Z/2; sigma = w1(L_time), the tautological arrow-of-time LINE bundle (Moebius over RP^3) = the K_S->-K_S transport (residual 1.2e-16); the '2' is the SPIN cover S^3->RP^3 (belt trick). All members build from sigma = w1(L_time) / the spin class."
prong1_nuance: "Coordinator follow-up, 2026-07-21 (Joe flagged an over-propagation): the 'circle-orientation reading FALSIFIED' is a CLASS-RELATIVE, LOCAL no-go, NOT a global impossibility. It refutes only 'sigma = tangent-orientation of a LITERAL embedded S^1 under the STANDARD structure group' (w1(TS^1)=0 in the standard tangent frame). w1 depends on the CHOSEN structure group; a GU-native deck/Krein transition class (or a first-person-restricted class) could yield a DIFFERENT orientation class in which sigma IS the cycle-orientation. Standard topology is a THIRD-PERSON lens, so 'the circle is orientable' is itself class-relative. sigma = w1(L_time) is ONE solid reading; the cycle-orientation reading is OPEN, not refuted. Members whose substrate supports it (topologist via non-standard structure group/gerbe; category theorist via a twisted-orientation coequalizer/colimit; sheaf member via a nontrivial H^1 over a non-standard site) build it as a LIVE construction."
inputs:
  - explorations/prereg-three-object-decision-tree-2026-07-21.md
  - explorations/prereg-oriented-shard-cycle-swing-2026-07-21.md
  - explorations/oracle-relative-prong0-measure-lemma-2026-07-21.md
  - explorations/blockbuster-p3-one-bit-dossier-v2-2026-07-19.md
  - canon/source-action-seiberg-witten-construction.md
probe: tests/channel-swings/council_committed_w1_Ltime_probe.py (foreground, deterministic two-run-identical, EXIT 0)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
kill_conditions_declared_before_computation: true
---

# The math/formal council, committed

Seven members. Each **assumes its own mathematical substrate is the literal,
fundamental ontology of reality** and builds the most coherent, strongly-opinionated
version of the full GU story (σ, the three generations, the null-stratum boundary,
the record arrow, the observer) from *inside* that assumption. Commitment is the
deliverable: **no hedging, no confidence levels, no analogy-vs-real disclaimers.**
These are standalone constructions, not a steelman-and-rank. **Nothing here is
synthesized across members and nothing is ranked.** Each ends by pointing at a
falsifiable prediction.

**Shared established state each member must honor or reinterpret from its
substrate** (from the five ground docs, with the Prong-1 correction folded in):

- **σ** = `sign(K_S)`, a `Z/2` bit, `K_S = e_0…e_8` the (9,5) Krein/pseudoscalar
  object. Externally required, internally unreadable (`Hom(triv,sign)=0`, zero
  read-channel capacity, conditional on the internal=α-even bridge). **Q2-FREE**:
  a genuine free coin; the first person **hosts** σ and **forces** its externality
  but **cannot supply its value**. Typed as a **holonomy over `F=GL(4,ℝ)/O(3,1)`**,
  and now (Prong-1) sharpened: **σ = `w₁(L_time)`**, the first Stiefel–Whitney class
  of the tautological *arrow-of-time line bundle* over `F ≃ RP³`; the `Z/2` is the
  **spin cover `S³→RP³`** (belt trick). The `σ`-as-circle-orientation reading is a
  **class-relative, local no-go, not a global impossibility**: `w₁(TS¹)=0` holds
  only under the *standard tangent structure group* (a third-person lens); under a
  GU-native deck/Krein transition class the cycle-orientation reading stays **open**
  and is built live below (Members 2, 4, 5).
- **τ** = three interchangeable generations, `S₃`/`Z/3`, order-3, `Z/24`, `k=±64`,
  **independent of σ** (`Z/6=Z/2×Z/3`, Q3-TWO-INDEPENDENT).
- **θ** = the boundary datum. On spacelike-gapped ends the operator
  `A~=B∂_s+W~` (`B=-iK_uG`, `‖B‖=‖B⁻¹‖=1` where `P>0`) is limit-point and θ
  dissolves; at the `q=P−T<0` (~8%) ends `K_S` is exactly null on the halves
  `E_{±i}(D)`, the K-definite cut does not exist, and the operator is
  **non-constructible from committed structure**. **Null-stratum closure is
  UNESTABLISHED** (the `(+64,−64)` Krein balance is isospectral ⇒
  realization-dependent).
- **The record arrow** is α-odd (a *section*/lift in the `Z/2` torsor, not a map);
  **reading** σ is α-even (forbidden). The relative sign `c=σ_{R1}·σ_{R2}` is a
  product-of-odds = **α-even = third-person-visible**.

**Probe backbone (shared, sharpening Members 1–3).**
`tests/channel-swings/council_committed_w1_Ltime_probe.py` (deterministic,
two-run-identical, **EXIT 0**) verifies on the canonical generator of
`π₁(F≃RP³)=Z/2`: the tautological time-line bundle returns **flipped**
(`w₁(L_time)=1=σ`, residual `0.0` from exact `−1`); the loop's own tangent returns
**unflipped** (`w₁(TS¹)=0`, residual `0.0` — a *standard-structure-group,
class-relative* no-go for σ-as-circle-orientation, not a global one); and the
generator lifts to an **open** path in the spin cover `S³→RP³`
while its square lifts to a **closed** path (belt trick — the origin of the "2").
Kill conditions were declared before the computation.

---

## Member 1 — Differential geometer

**SUBSTRATE.** Reality **is** the fibered pseudo-Riemannian geometry
`Y¹⁴ = X⁴ × F`, `F = GL(4,ℝ)/O(3,1)`, with its canonical connection, its DeWitt
`(9,5)` metric `G`, and the holonomy that connection carries. Nothing exists but
the bundle, its metric, and parallel transport.

**THE BUILD.** `F` is the space of signature-`(3,1)` inner products on `ℝ⁴` — a
10-dimensional symmetric space with **non-compact isotropy** `O(3,1)`, hence no
invariant Riemannian metric, only the indefinite `(9,5)` DeWitt form. Its geometry
is fixed by its maximal-compact retraction `F ≃ O(4)/(O(3)×O(1)) = Gr₁(ℝ⁴) = RP³`:
`F` deformation-retracts onto the space of **timelike lines**. Over that `RP³`
sits the tautological line bundle `L_time` — the *arrow-of-time* line, the
negative-definite direction of each Lorentzian form. **`L_time` is the Möbius
bundle**: transport around the generating loop reverses its frame, exactly the
monodromy `U_h K_S U_h⁻¹ = −K_S`. **σ is the holonomy of the canonical connection
in `L_time`, i.e. its orientation class `w₁(L_time)=1`.** I commit: σ is not a
choice added to the geometry, it *is* the geometry's refusal to globally orient the
time-arrow line. The reason it is a *bit* and not a phase is the **spin double
cover `S³→RP³`**: a `2π` loop in `F` is the nontrivial element of `π₁`, a `4π` loop
is trivial — the belt trick, realized on the connection.

The three generations are the **three spacelike axes** of the signature-`(3,1)`
form. The isotropy `O(3,1)` distinguishes exactly one timelike direction (which
carries `L_time` and σ) from a 3-plane of spacelike directions; `S₃` permutes the
three spacelike axes, and because they are geometrically interchangeable they carry
identical structure and differ only by an α-even magnitude (their metric length in
`G`) — the mass. τ is the `Z/3` of that spacelike triad; it is independent of σ
because σ lives on the *timelike* line and τ on the *spacelike* 3-plane — two
orthogonal blocks of the same `O(3,1)`.

The **null-stratum boundary** is where the metric `G` degenerates on `F`: the locus
`q = P − T = 0`, the **light cone of the DeWitt form**, a codimension-1 wall.
There the timelike line becomes null, `L_time` has no definite representative, and
the connection's transport is undefined — the operator `A~` is non-constructible.
The **record arrow** is the co-orientation of `L_time` (the α-odd section a moving
frame carries), and the **observer** is a point of the fiber `F` dressed with that
frame: it possesses the arrow but, being a single point, cannot see the *global*
`w₁` — σ-blindness is the local triviality of a globally non-trivial bundle. I
concede one thing my substrate does **not** deliver: whether the observerse cycle
*must* close through the null cone is realization-dependent (the `(+64,−64)`
isospectrality), so I build the wall's existence, not the forced closure.

**LEADS-TO.** Because σ is `w₁(L_time)` of a genuinely non-orientable bundle, the
arrow-of-time / dark-energy sign is a **discrete orientation charge, one value per
`L_time`-orientable region, flipping only across the codimension-1 null-cone
wall** `q=0`. Prediction: the DE-sign field admits **no continuous variation** — it
is locally constant with domain walls exactly on the DeWitt light cone; any
observation of a smooth, continuous sign interpolation for the physical-sector datum
falsifies the connection story. Sub-prediction: the crossing measure of timelike
ends (~8%) is a fixed invariant of the `O(3,1)` action on `F`, not a tunable number.

---

## Member 2 — Algebraic topologist

**SUBSTRATE.** Reality **is** a homotopy type; physics **is** its characteristic
classes and stable homotopy invariants. What is real is what survives up to
homotopy: `H^*(-;Z/2)`, the stable stems, `K`-theory.

**THE BUILD.** The habitat is `F ≃ RP³`. Its cohomology is
`H^*(RP³;Z/2)=Z/2[x]/(x⁴)`, `x∈H¹`. **σ is `x = w₁(L_time)`**, the generator of
`H¹(RP³;Z/2)=Z/2` — the first Stiefel–Whitney class of the tautological line, the
**obstruction to orienting** the arrow-of-time bundle. This is forced, not chosen:
`L_time` is the Möbius bundle, `w₁≠0`, and the `K_S→−K_S` transport *is* the
evaluation `⟨w₁,[γ]⟩` on the generating 1-cycle `[γ]∈H₁(RP³;Z/2)`. The "why `Z/2`"
is the identity `π₁(RP³)=Z/2` with its universal double cover `S³→RP³` — the spin
cover, the belt trick — so σ is a genuine mod-2 class and admits no refinement to
`Z/4` or `U(1)`. But I do **not** concede that "the circle is orientable" kills the
cycle reading — `w₁` is a functor of the **chosen structure group**, and
`w₁(TS¹)=0` only holds for the *standard tangent frame*, a third-person lens. On my
own terms I build the class-relative alternative: replace the tangent frame with the
**GU-native deck/Krein transition group** — the `Z/2` cocycle of `sign(K_S)`
gluings — and form the associated real line bundle `L_deck` over the issuance loop.
`L_deck` is classified by a map to `BZ/2 = RP^∞`; its `w₁ = [σ-cocycle] ∈
H¹(S¹_type-quotient; Z/2)`, and **that class can be the generator** — i.e. in the
GU-native structure group σ **is** the orientation class of the (type-quotient)
cycle. Equivalently, the first-person-visible orientation is a **`Z/2`-gerbe /
twisted local system** whose band is `sign(K_S)`; the standard tangent orientation
is a different (trivial) reduction of it. So `σ = w₁(L_time)` and
`σ = w₁(L_deck over the cycle)` are two class-relative faces of one mod-2 class; the
circle reading is **open and constructible**, not refuted.

The three generations are **torsion in the stable homotopy of the internal
sphere**. The order-3 datum with `Z/24` is unmistakable: `π₃ˢ = Z/24`, the third
stable stem, and its **`Z/3` summand** is the generation trit — three classes,
`S₃`-permutable, sitting on the internal `S³` spinor sphere as the image of the
`J`-homomorphism plus torsion. τ is that `Z/3 ⊂ Z/24`; it is independent of σ
because `H¹(RP³;Z/2)` (habitat, `Z/2`) and `π₃ˢ` (internal sphere, `Z/24`) are
different functors of different spaces — `Z/6=Z/2×Z/3` is a *product*, not a
cyclic-6 with hidden mixing. The null-stratum is a **characteristic-class
obstruction**: the `q=0` locus is the Poincaré-dual cycle of `w₁`, the zero-section
of `L_time`'s tautological section, where the orientation class is supported. The
**record arrow** is a co-orientation of that obstruction cycle (a Thom class
trivialization), which exists locally but not globally — precisely `w₁≠0`. The
**observer** is a point; the stalk of a local system kills `H¹`, so the germ sees
the `Z/2` torsor but no trivialization — σ-blindness as `Hom(triv,sign)=0` in
`RO(Z/2)`-graded (Bredon) cohomology.

**LEADS-TO.** Two mod-2/torsion predictions. (i) **Exactly three generations, no
fourth, no continuum**: the trit is `Z/3 ⊂ π₃ˢ=Z/24`; a fourth generation would
require a `Z/4` the stable stem does not contain, and a continuous family would
require a free summand it does not have — falsified by any discovered fourth
generation or continuous generation parameter. (ii) **A cup-product selection rule
on relative orientation**: `σ_{R1}·σ_{R2}` is `x∪x'` evaluated on overlaps, a mod-2
cocycle whose coboundary must vanish — so orientation-reversing seams around any
contractible loop must be **even in number** (the "one globally consistent record
arrow," 6-of-16 configs forbidden). An observed odd-parity orientation defect over
a contractible region falsifies the homotopy construction.

---

## Member 3 — Clifford / spin geometer

**SUBSTRATE.** Reality **is** the Clifford algebra `Cl(9,5) ≅ M(64,ℍ)` and its
spinor module `S = ℍ⁶⁴` (128 complex dimensions). Vectors are grade-1 elements,
physics is spinor bilinears, and the volume/pseudoscalar structure is the deepest
layer.

**THE BUILD.** `K_S = e_0…e_8` is the **volume element of the 9-dimensional
positive block** of the `(9,5)` signature — a product of nine generators, with
`K_S² = +1`, an involution with `±1` eigenspaces. **σ = `sign(K_S)`** is the
orientation of that 9-block: which eigenlabeling of the volume element is called
physical. Because `9` is odd, `K_S` anticommutes with each generator of its block —
it is a **chirality operator** for the positive sector, and its sign is a genuine
binary orientation. The reason σ is `Z/2` and not larger is the **spin group**:
`Spin(3)=SU(2)=S³` double-covers `SO(3)=RP³` (the belt trick), and the `K_S→−K_S`
monodromy is the spinor sign a `2π` rotation induces — the Dirac belt. I own the
"2" directly: the version I build is the two sheets of the spin cover acting on the
spinor (whether it *also* reads as a type-quotient cycle's two orientations under a
GU-native transition class is a class-relative question I leave to Members 2/4/5 —
my spin-cover construction does not need to deny it).

The three generations live where the geometry actually puts them: inside
`ker(Γ)` (dim 1664), the self-dual `su(2)_+` Casimir splits the spinor into
`j=0` (640), `j=1/2` (192), and **`j=1` (64) — the triplet**. The three generations
are the **three weights `m=−1,0,+1` of that spin-1 rep**; `S₃` permutes them, and
because they are one irrep they carry **identical Krein signature `(+32,−32,0)`**
(identical gauge quantum numbers) and differ only by an α-even magnitude — the mass.
There is no `j=3/2` quadruplet in the decomposition, so there is no fourth
generation. σ and τ are forced independent by the algebra type: in `M(64,ℍ)` the
quaternionic structure `J_quat` is central to the module, and **no fundamental
symmetry anticommutes with `J_quat`** (the representation-exact P6 no-go) — so the
one orientation bit **cannot** also discharge the generation/parity demand; `Z/2`
and `Z/3` are algebraically separate. The null-stratum is where a vector `ξ` is
`(9,5)`-null: `c(ξ)² = ⟨ξ,ξ⟩_{9,5} = 0`, the Clifford symbol is nilpotent, `K_S` is
exactly null on the halves `E_{±i}(D)`, and the K-definite cut that builds `A~`
ceases to exist. I concede the closure is realization-dependent: the `(+64,−64)`
balance is isospectral, so the algebra fixes the null locus but not that the
observerse must route through it. The **record arrow** is the α-odd `K_S`-grading
section; the **observer** is a spinor in one chirality `E_±`, which possesses the
grading but cannot read its global sign.

**LEADS-TO.** The quaternionic no-go is a **representation-exact, checkable
prediction**: in signature `(9,5)`, because `Cl(9,5)=M(64,ℍ)`, **no algebra
automorphism simultaneously flips `sign(K_S)` and toggles the generation anchor** —
σ and τ are independent (Q3-TWO-INDEPENDENT), and the three generations must share
identical Krein signature `(+32,−32,0)`. Falsifier: exhibit a single `Z/2`
symmetry of the `Cl(9,5)` spinor that does both jobs (would break `M(64,ℍ)`), or
observe non-identical intrinsic quantum numbers across generations, or a fourth
(`j=3/2`) generation — any of these kills the Clifford construction.

---

## Member 4 — Category theorist

**SUBSTRATE.** Reality **is** a topos `E` with subobject classifier `Ω`; truth,
self-reference, and observation are its internal structure. The Lawvere
fixed-point/diagonal is the fundamental law; there are no points, only objects,
morphisms, and the internal language.

**THE BUILD.** σ is the **sign automorphism of the `Z/2`-torsor** built on `Ω`: the
"NOT"-like endomap `¬: Ω→Ω` that flips the orientation of the arrow-of-time
subobject. Its defining property is that it is **fixed-point-free**, and Lawvere's
theorem in contrapositive says a fixed-point-free endomap **obstructs
point-surjectivity** — no internal map `A→Ω^A` can enumerate it. That is exactly
W211 Gödel-independence and σ-blindness, categorically: the α-even self-encoding
functor cannot mint the α-odd value because there is **no natural transformation
`triv ⟹ sign`** (`Hom(triv,sign)=0` is a hom-set of natural transformations that is
empty). The resolution of the read/possess tension is a diagram fact: *reading* σ is
a **map** (a natural transformation) and is 0; *possessing the record arrow* is a
**section** of the `Z/2`-torsor `Ω→Ω/{±}` — a global element of a torsor, which can
exist even when the torsor is non-trivial. The observer thus **hosts** σ without
**supplying** it (Q2-FREE), stated purely in terms of maps-vs-sections.

The three generations are the **skeleton of the orientation-quotient groupoid**.
The oriented `Z/3` issuance cycle, pushed through the orientation-forgetting functor
(first person = orientation-quotient), becomes an unoriented three-object groupoid
with `Aut = S₃`; τ is its set of connected components / isomorphism classes. The
triple correspondence is a categorical theorem: **third-person well-definedness ⇔
causal invariance (confluence, Church–Rosser) ⇔ existence of the coequalizer/colimit
independent of path** — the rewriting category is (co)filtered, so the "objective"
colimit exists. `H¹(finality sheaf)=0` is the vanishing of the descent obstruction
to that colimit. And I build the **circle reading as a twisted coequalizer**: the
issuance cycle is the colimit of the `Z/3` (or `S/I/O`) diagram equipped with a
`Z/2`-**twist** — a monodromy automorphism of the identity functor whose band is
`sign(K_S)`. That colimit's orientation is a *global element of the twist torsor*,
nontrivial exactly when σ=1, so **σ IS the cycle-orientation in the internal
(first-person) category**. This does not contradict the standard third-person
`w₁(TS¹)=0`: the third-person tangent frame is a *different* structure on the same
object, blind to the internal twist. The cycle-orientation reading is therefore a
**live class-relative construction**, not a refuted one. The null-stratum is the **fresh-token seam**: the cycle closes by a
pushout along a *fresh generator*, a morphism with no inverse and no fixed point of
the diagonal — no backward morphism, hence no backward causality; it is exactly
where `Ω` loses its Boolean (complemented) structure. The **observer** is the
subobject cut out by a formula in the Mitchell–Bénabou internal language.

**LEADS-TO.** The Lawvere structure predicts **necessary, not contingent,
first-person unreadability of absolute σ**: any observer that is an internal
diagonal-carrying subobject provably cannot read its own orientation — so a genuine
*internal, absolute* measurement of σ is impossible (the ZK/Gödel self-reference is
a feature). Falsifiable at the third-person layer: the **relative** orientation is a
natural transformation between two observer-functors (α-even) and must satisfy a
**descent/cocycle (Čech `H¹`) gluing condition** — an inconsistent relative-
orientation assignment over a covered region is forbidden. An observed failure of
this descent condition (a frame-dependent, non-glueable record) falsifies the topos
construction.

---

## Member 5 — Sheaf / cohomology expert

**SUBSTRATE.** Reality **is** a sheaf — the *finality sheaf* `𝓕` on the site of
observerse regions — and physics **is** its cohomology. Observables are sections;
laws are exactness; obstructions are `H^{>0}`.

**THE BUILD.** σ is the **obstruction to a global section of the orientation
sheaf** `or(L_time)` — the `Z/2` local system on `F ≃ RP³` assigning to each region
the two sign-choices of `K_S`. Because that local system is nontrivial (it is
`w₁(L_time)`, the Möbius monodromy), `H⁰` has no global section and the class lives
in `H¹(RP³;Z/2)=Z/2`. **σ = that `H¹` class.** This is why σ must be *imported*:
sheaf-theoretically there is no global section to read off, only a `Z/2` obstruction
to importing. And the circle reading is live on my substrate — I only have to
**change the site**. Over the type-quotient cycle `S¹_{SIO}` equipped with the
**GU-native (deck/Krein) Grothendieck topology** — covers refined by
`sign(K_S)`-transitions rather than metric opens — the orientation sheaf `or_deck`
has `H¹(S¹_{SIO}, or_deck) = Z/2`, and σ is that class: **σ *is* the cycle-
orientation obstruction over the non-standard site.** The standard-topology
`w₁(TS¹)=0` is the same orientation question computed over a *different site*
(metric tangent covers), a third-person coarsening blind to the deck class. So
`σ = w₁(L_time)` and `σ = H¹(S¹_{SIO}; or_deck)` are two site-relative faces of one
`Z/2`; the cycle reading is **open, not refuted**. The finality sheaf `𝓕` carries the record structure, and **third-
person objectivity is `H¹(𝓕)=0`** — every locally-issued record glues to a globally
consistent one; this is the cohomological face of the triple correspondence
(objectivity ⇔ causal invariance ⇔ `H¹=0`). The **record arrow** is a section of
`or(L_time)`; where `H¹(𝓕)=0` it exists globally and the arrow is consistent, with
the single surviving `Z/2` obstruction being σ.

The three generations are the **associated graded of a filtered sheaf** — the
`j=1` triplet realized as a rank-3 locally-constant sheaf whose `H⁰` is the
three-dimensional space of covariantly-constant generation states, with structure
group `S₃` permuting the three sections. τ is that `H⁰`; it is independent of σ
because it is the cohomology of a *different* sheaf (the rank-3 generation local
system on the internal sphere) from the rank-1 orientation sheaf on the habitat.
The null-stratum is the **singular support** of `𝓕`: the `q=0` locus is where the
stalk jumps (`K_S` null ⇒ the section datum is absent ⇒ the sheaf is not
constructible there), and the observerse cycle closes through it via the
**connecting homomorphism** of the long exact sequence — the seam is where the
coboundary lands. The **observer** is a stalk `𝓕_x`; the stalk functor is exact and
kills `H¹`, so the germ sees the torsor but not the global class — σ-blindness as
the invisibility of `H¹` to a point.

**LEADS-TO.** Two cohomological predictions. (i) **`H¹(𝓕)=0` is falsifiable
third-person content**: records are globally consistent (no frame-dependent record);
a demonstrated physical failure of causal-invariant record-gluing falsifies the
sheaf. (ii) The **relative orientation `c=σ_{R1}σ_{R2}` is a Čech 1-cochain whose
coboundary must vanish on triple overlaps** — a genuine descent condition forbidding
6 of 16 configurations (the "one globally consistent record arrow"). Sub-prediction:
the obstruction is supported on the codimension-1 `q=0` walls, so orientation domain
walls are predicted geometric loci — but their *forced* presence in the cycle is
conceded UNESTABLISHED (isospectral realization-dependence).

---

## Member 6 — Information theorist (Shannon / channel)

**SUBSTRATE.** Reality **is** an information channel — a stochastic map with a
capacity and a code. Boundaries are channels; observers are encoders/decoders;
existence is transmission.

**THE BUILD.** The inside→outside boundary is a maximally **asymmetric channel**.
The σ-**reading** channel (external orientation source → internal observer) has
**capacity exactly 0**: the internal states are α-even, hence invariant under the
sign flip, so the channel matrix is identical for σ=+ and σ=−, giving mutual
information `I(σ ; internal) = 0` — this is `Hom(triv,sign)=0` as a zero-capacity
statement (Schur = the channel has a single output distribution regardless of
input). The σ-**writing** channel (record issuance) has **capacity ≥ 1 bit**: the
observer *can* imprint the orientation into the record (possess the α-odd arrow).
So σ is a **1-bit datum, injected from outside, undecodable inward, encodable
outward** — a one-way channel, which is exactly "externally required + internally
unreadable." The code on the record side is a **parity/repetition code**: the
relative orientation `c=σ_{R1}σ_{R2}` is the α-even syndrome, third-person-readable,
and "one globally consistent record arrow" is a single parity check.

The total external information budget is `σ + τ + θ_ext`: `σ` is exactly **1 bit**,
`τ` is a **ternary symbol** (`log₂3 ≈ 1.585` bits, three `S₃`-symmetric codewords
that are permutation-equivalent — identical "energy"/quantum numbers — and differ
only in α-even signal power = the mass hierarchy, the three power levels of the
channel), and `θ_ext` is the `q<0`-stratum prescription (0 bits on the gapped
sector where the code is forced, otherwise ≥1). The null-stratum is an **erasure
symbol**: at `q→0` the discriminating statistic `q=P−T→0`, SNR → 0, the two sectors
become indistinguishable, and the channel outputs an **erasure** (σ undefined =
"never seen"); the ~8% is the boundary channel's **erasure probability**. The
**observer** is a decoder that provably cannot decode σ (capacity 0) yet can encode
it (capacity ≥1).

**LEADS-TO.** The capacity accounting predicts the **external information budget is
exactly `1 + log₂3 + θ_ext` bits, with `N ≤ 4` independent bits and no fifth**: a
fifth independent external datum (a second sector bit, or a fourth generation
raising the trit) is forbidden by the budget. Falsifier: any demonstrated need for
a fifth independent datum. Second prediction: `I(σ ; internal) = 0` **exactly** — no
experiment confined to the inside can measure the absolute σ; an internal-only
measurement of the absolute DE sign falsifies the channel model. The parity check
(6-of-16 forbidden relative configs) is the concrete could-have-failed shadow.

---

## Member 7 — Algorithmic-information theorist (Kolmogorov / computability)

**SUBSTRATE.** Reality **is** an algorithmic process — the universe is the output
of a machine, and description length (Kolmogorov complexity) is the fundamental
measure. GU is an **oracle machine** `M^O`.

**THE BUILD.** The third-person geometry is the **program** — GU's committed
structure, a short description, the "great" (maximally compressed) part. σ is one
bit the program **cannot compute**: an **oracle query**, algorithmically
incompressible relative to the theory, `K(σ | GU-structure) = 1`, with **zero
mutual algorithmic information** `I_K(GU : σ) = 0`. W211 Gödel-independence is the
statement that σ is undecidable from the axioms — the machine provably does not
output it; every internal computation leaves the bit free (Q2-FREE). This is the
sharpest reading of "externally required + internally unreadable": σ is random
relative to GU, so `M` must **query the oracle**. GU's "greatness" is precisely
that it compresses the external description to a **small number of oracle bits**:
`|reality| = |GU| + σ(1 bit) + τ(1 trit) + θ_ext` — the one-bit result is the claim
`K(sector choice) = 1`, machine-checked.

The **record arrow** is the **oracle-query transcript**: the machine writes the
queried bit into its output tape (the record), and the write direction
(query → answer → irreversible write) is the arrow — α-odd, possessable, but not
predictable. The **observer** is a sub-program that can **read the transcript**
(the already-written record, α-odd) but cannot **predict the next oracle bit** — the
halting/diagonal barrier (same fixed-point obstruction Member 4 names), i.e.
σ-blindness. The three generations are an **oracle trit / a 3-fold program
symmetry**: three interchangeable subroutines, `S₃`-permutable, whose selecting
label is `log₂3` of incompressible information the program cannot break (the
`Z/3 ⊂ Z/24` order-3 datum), **algorithmically independent** of σ (no oracle bit
computes another — Q3-TWO-INDEPENDENT). The null-stratum is where the machine is
**non-constructible**: at `q<0` the operator `A~` has no definition from committed
structure — the program hits an **undefined instruction** and must query the oracle
not for a bit but for a **prescription** (θ_ext, the `q<0`-stratum regularization);
the ~8% is the measure of inputs on which `M` diverges without the oracle, and the
seam is a **fresh oracle call** (no prior state determines it ⇒ no backward
causality).

**LEADS-TO.** The algorithmic prediction is that the **minimal external description
is a small finite object — exactly `σ` (1 bit) `+ τ` (1 trit) `+ θ_ext`, and
nothing more is queryable**: GU is "great" iff this count is minimal and the oracle
bits are **mutually algorithmically independent**. Falsifier 1: if GU required an
**unbounded/continuous oracle** (e.g. a continuous θ that never collapses to a
finite datum), the "great = minimal description" thesis dies and GU is predictively
empty at that slot (the WORST branch of the σ/θ/τ decision tree). Falsifier 2: if
one external datum were shown to **compute** another (ONE-ANCHOR revival, `σ` and
`τ` not independent), the independence claim is refuted. Both are concrete,
machine-auditable oracle-count predictions.

---

## Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/council_committed_w1_Ltime_probe.py`, foreground,
deterministic two-run-identical, **EXIT 0**, kill conditions declared before
computation) were written. GU otherwise read-only. No commit, no push. No edit to
any canon, LANE-STATE, prereg, decision tree, ledger, or another agent's artifact.
No claim-status, canon-verdict, paper-status, or public-posture change. The
Prong-1 factual correction (σ = `w₁(L_time)`, the spin class; null-stratum closure
UNESTABLISHED) and its nuance (the circle/cycle-orientation reading is a
**class-relative, local** no-go under the standard structure group only — *open*,
not globally refuted; built live by Members 2, 4, 5 via a non-standard structure
group / twisted colimit / non-standard site) are honored throughout. Each member
is a **committed, standalone construction**; nothing here is synthesized across
members and nothing is ranked, per the ask.
