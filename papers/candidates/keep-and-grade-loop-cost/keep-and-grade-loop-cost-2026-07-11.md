# The Loop-Level Cost Structure of Keep-and-Grade Fourth-Order Gravity

**Draft, 2026-07-11. GU-INDEPENDENT: the results below are about the class of fourth-order (Stelle-type)
gravities and the indefinite-metric quantization program generally; Geometric Unity appears only as one member
of the class. External publication is Joe-gated (no arXiv, no submission in scope here). Every quantitative claim
ties to a reproducible test in `tests/` (W44-W54, all exit 0).**

## Abstract

Fourth-order (Stelle) gravity is renormalizable and asymptotically free, but propagates a massive spin-2 **ghost**
-- a negative-norm state. The "keep-and-grade" rescue (Krein / PT-symmetric indefinite metric) keeps the ghost
and grades the state space so that the physical inner product is positive and the S-matrix is unitary on it; it
is established at tree level. Whether it survives at **loop** level is a long-standing open question whose
resolution decides the fate of an entire class of theories (Stelle gravity, conformal gravity, agravity). We
attack it through five independent constructions -- Cutkosky cutting, the PT/`C`-operator, the fakeon
prescription, the Lee-Wick complex-pole treatment, and an adversarial no-go -- and report three results. **(1) A
positivity-vs-causality trade:** loop unitarity is achievable, but every construction that achieves it pays in
micro-causality or locality; none pays neither. **(2) RG-stability for asymptotic freedom:** the grading-based
positivity is renormalization-group contingent in general, but along the asymptotically-free flow the spin-2
grading is well-defined at every finite scale, degenerating only at the free ultraviolet fixed point where the
ghost decouples. **(3) A no-local-positive-metric theorem:** for the free theory, no positive metric with a local
(entire-symbol) generator exists -- every keep-and-grade positive metric is non-local, but its kernel decays
exponentially at the ghost scale. The cost of loop unitarity is therefore real, bounded, and microscopic.

## 1. Introduction

Higher-derivative gravity with a Weyl-squared term is perturbatively renormalizable (Stelle 1977) and
asymptotically free in its dimensionless couplings (Fradkin-Tseytlin; Avramidi-Barvinsky; and the modern
"agravity" analysis, Salvio-Strumia). The obstruction to taking it as a fundamental theory is the massive spin-2
excitation in the `1/(p^2(p^2-m_2^2))` propagator: expanded as `(1/m_2^2)[1/p^2 - 1/(p^2-m_2^2)]`, the second
pole has a wrong-sign residue, a state of negative norm. Naively this violates unitarity.

The **keep-and-grade** program does not remove this state. It equips the Fock space with an indefinite (Krein)
inner product and a grading operator (the PT/`C`-operator, or an equivalent hidden discrete symmetry) so that a
*physical* positive inner product is recovered and the S-matrix is unitary with respect to it. In quantum
mechanics this is rigorous and complete: the fourth-order Pais-Uhlenbeck oscillator is unitary under the
Bender-Mannheim PT construction. At tree level in field theory the ghost decouples from physical amplitudes
(Bateman-Turok). The open question is **loop level**, and it is sharp: a general proof would rehabilitate
fourth-order gravity as a unitary ultraviolet completion; a general no-go would close the program.

The question decomposes into three decidable sub-questions:
- **Q-cut** -- do the negative-norm states stay decoupled from the unitarity cuts (optical theorem) at one loop?
- **Q-pos** -- does the grading that defines the positive physical inner product survive renormalization?
- **Q-caus** -- is any loop-consistent construction Lorentz-invariant and micro-causal, or is unitarity bought at
  the price of causality/locality?

We proceed by running five **independent, mutually blind** constructions of "make the ghost consistent," on the
principle that the answer -- if any single construction works -- should not be prejudged by picking the currently
fashionable one. The blindness is methodological: each construction was pursued to a graded verdict without
knowledge of the others, and only then synthesized.

## 2. Setup

**The class.** We work with the Stelle action `a C^2 + b R^2 + (Einstein-Hilbert) + (cosmological)`, its massless
graviton and massive spin-2 ghost at `m_2^2` (and the spin-0 mode from `R^2`). Statements are made for the class;
Geometric Unity's induced `|II|^2` functional and its `ker Gamma`-projected Rarita-Schwinger sector are one
realization, and where the fermionic sector matters we note it, but nothing below requires accepting GU.

**Renormalizability including the fermion sector** (context, `tests/W44`). Power-counting gives superficial
degree of divergence `D <= 4` for every loop order once the spin-3/2 sector is projected: the transverse
projector has momentum-degree zero and removes exactly the `n=2` Velo-Zwanziger modes that would otherwise make a
gravity-coupled spin-3/2 non-renormalizable. The matter sector adds a finite, closed set of counterterms. So the
class is renormalizable; the ghost is the sole barrier to calling it a unitary UV completion, which is why the
loop-positivity question is the whole game.

**The two inner products.** Throughout we distinguish (i) **Krein pseudo-unitarity** `S^dag eta S = eta` with the
indefinite metric `eta` -- an algebraic identity, all-orders, never in dispute (Bateman-Turok) -- from (ii)
**physical-subspace positivity**, the existence of a *positive* metric on which the S-matrix is unitary. The loop
question is entirely about (ii); the loop expansion separates the two.

## 3. Result 1: loop unitarity is a positivity-vs-causality trade

Four of the five constructions achieve (or characterize) loop unitarity, and they converge -- independently and
blind -- on a single structural statement: **the rescue does not remove the ghost problem, it converts it into a
causality/locality problem.** The constructions fall into two families paying in two currencies.

**Family 1 -- grading-based** (keep the ghost, grade the inner product).
- *Cutkosky cut* (`tests/W48`): grading *alone* fails Q-cut. For a stable Krein-graded ghost the one-loop optical
  theorem leaks a negative contribution on the physical subspace, localized at the graviton+ghost threshold
  `s=m_2^2`. Tree/QM positivity is silent here because `0+1`-dimensional QM has no continuum cut -- which is
  precisely why tree positivity does not imply loop positivity. The ghost decouples only if additionally treated
  as a complex-pole/removed object (Family 2).
- *PT/`C`-operator* (`tests/W49`): the positive metric exists order by order (Q-pos passes in QM -- free
  Pais-Uhlenbeck exact, first interacting correction unique, `C^2=1`, `eta>0`), but the equivalent
  Dirac-Hermitian Hamiltonian is **non-local**: its generator carries energy denominators `1/sqrt(k^2+m^2)` with
  a non-entire symbol. One gets manifest positivity (non-local `h`) or manifest locality (PT-Hermitian `H`, whose
  loop causality is exactly what is disputed), never both manifestly. The cost is locality (Q-caus).

**Family 2 -- removal-based** (take the ghost out of the asymptotic spectrum).
- *Fakeon* (Anselmi-Piva; `tests/W50`): Q-cut passes *by construction* (the average-continuation prescription
  cancels the ghost's absorptive part exactly, verified on the one-loop bubble), Q-pos is RG-stable in scheme,
  but micro-causality is violated within `~1/m_2` (Lorentz invariance retained). Bounded/unobservable if `m_2` is
  heavy; fatal only if the ghost is light.
- *Lee-Wick* (Donoghue-Menezes; Grinstein-O'Connell-Wise; `tests/W51`): Q-cut passes at one loop -- the one-loop
  self-energy pushes the ghost pole off-axis in the *proven-correct* direction (`Im Sigma(m_2^2)>0`, fixed by the
  massless-bubble discontinuity and positive spin-2 phase space), and the ghost is above threshold because it is
  the heaviest mode. Micro-causality is violated at `~1/m_2`, Lorentz-invariant. A one-loop proof-of-concept.

**The conservation-like law.** No construction pays neither currency. Family 1 buys positivity at the cost of
locality (or fails at the cut); Family 2 buys unitarity at the cost of bounded micro-causality. This is the
first result: at loop level, unitarity of fourth-order gravity is a **trade against micro-causality/locality**,
and the trade is bounded to the ghost scale `~1/m_2`.

## 4. Result 2: the grading is RG-contingent, but RG-stable for asymptotic freedom

The adversarial construction (`tests/W52`) sharpens Family 1. The positivity-defining grading is **dynamical**
(coupling-dependent, not kinematic): it exists on an open domain and degenerates on a codimension-one exceptional
(Jordan) locus where two eigenvalues collide. Hence loop positivity is **renormalization-group contingent, not
structural** -- tree positivity certifies only the neighborhood of the free point. (This is class-wide at the
level of the grading; it does not touch pseudo-unitarity.)

Whether a *given* theory is safe therefore reduces to a flow question: does its renormalization-group trajectory
reach the exceptional locus? For the asymptotically-free flow we can answer it (`tests/W53`, using the one-loop
beta functions of `tests/W45-W47`). The exceptional locus for the spin-2 sector is `m_2^2 = 0` (the ghost pole
colliding with the massless graviton pole). Two independent derivations (direct integration of the flow;
analytic leading-log at the fixed point) agree to `1.5e-15`:

- **Spin-2 sector:** the grading is well-defined (`m_2^2>0`, PT-unbroken) at **every finite scale**. Because the
  ghost mass tracks the Weyl coupling and asymptotic freedom drives that coupling to zero in the ultraviolet, the
  flow reaches the locus **only at the free ultraviolet fixed point** -- where the ghost decouples anyway. So the
  keep-and-grade grading is **RG-stable across the entire interacting regime**, pinching the locus only at the
  free endpoint.
- **Spin-0 (conformal) sector:** the asymptotically-free trajectory sits at a negative conformal-mode ratio,
  giving a wrong-sign (`M_0^2<0`) mode -- PT-broken *if that mode is physical*. This is the classic
  conformal-factor problem of Euclidean quantum gravity, widely argued to be a gauge artifact; it remains open.

**A construction-fork caveat, stated explicitly.** The spin-2 verdict depends on the convention for the ghost
mass. In the agravity convention `m_2^2 = (1/2) f_2^2 M_Pl^2` the mass runs to zero with the coupling (boundary
at the ultraviolet endpoint, as above); in a convention where the mass is set by a fixed transmutation scale the
mass does not run and the trajectory stays clear of the locus entirely. We do not select the favorable
convention; we record that the verdict is convention-dependent and that both readings leave the *interacting*
regime safe, differing only on the free endpoint.

Net: the grading branch of the rescue is RG-stable for asymptotically-free fourth-order gravity throughout the
interacting regime; the only shadows are the free-endpoint pinch and the conformal-factor mode.

## 5. Result 3: no local positive metric exists (theorem, free case)

Result 1 showed the grading's positivity costs locality at the symbol level; here we prove it.

**Theorem (free fourth-order / Pais-Uhlenbeck field, keep-and-grade quantization).** There is no positive-definite
metric operator `eta` -- intertwining `eta H = H^dag eta` and defining a positive physical inner product -- whose
symbol is entire of finite exponential type (in particular, no polynomial symbol / finite-order differential
operator). Equivalently, **every keep-and-grade positive metric is non-local.** Moreover the non-locality is a
branch point at `k = +- i m_ghost`: the metric kernel decays like `e^{-m|x-y|}`, so it is non-local but
**exponentially localized at the ghost scale**, not long-range. (`tests/W54`, 13/13 checks.)

**Proof sketch.** The full family of positive intertwiners is `eta = J C` with the grading forced, by positivity,
to carry the Krein signature `(+,-,-,+)` on the `(omega_1 pm, omega_2 pm)` modes -- an *odd-in-energy* sign
pattern. Solving the intertwining relation, the metric's symbol is a strictly-signed positive combination of
`1/omega_i = 1/sqrt(k^2+m_i^2)` for every choice of commutant weight; it never vanishes and always carries the
branch cuts at `k=+-i m_i`. The only entire grading is even-in-energy, which cannot separate the positive- from
negative-frequency shells and is therefore indefinite. Hence no positive member of the family is entire. Two
independent derivations locate the obstruction identically: (i) the commutant-plus-positivity argument above; (ii)
a Paley-Wiener argument, independent of positivity -- a local self-adjoint operator has an entire symbol, which
the fourth-order Krein spectral structure forbids.

**Strength and gaps, stated honestly.** Proven: no positive metric with an *entire/polynomial* symbol, plus the
exponential-localization characterization, for the *free* theory, machine-checked. Strong-argument (not theorem):
the *interacting* case (the first-order correction adds its own `1/(omega+omega')` cuts and cannot cancel the free
obstruction -- perturbative, not all-orders) and the *non-translation-invariant* case ("no metric from any local
field operator," where dropping translation invariance is the gap). The load-bearing assumption is that the
ghost's Krein signature is fixed by the local action and not locally re-definable; exhibiting a local re-signing
would overturn the theorem.

## 6. Synthesis and honest scope

The three results cohere into one statement. Keep-and-grade unitarity for fourth-order gravity is **real but
costs locality/causality, and the cost is provably confined to the ghost scale**: the four constructions trade
unitarity for a `~1/m` causality/locality effect (Result 1), the grading survives the renormalization flow for
asymptotically-free gravity across the interacting regime (Result 2), and the positive metric is provably
non-local but with an exponentially localized kernel (Result 3). The `~1/m` scale recurs in all three, from three
different computations -- a nontrivial internal consistency.

What this is, and is not:
- It is **not** a proof that keep-and-grade works: the free ultraviolet endpoint, the conformal-factor mode, and
  the all-orders interacting metric all carry caveats.
- It is **not** a clean no-go: the adversarial construction produced a burden-flip (positivity is RG-contingent),
  not a completed kill, and the spin-2 sector survived it.
- It **is** a correctly-scoped structural map of a class-wide open problem, with one machine-checked theorem
  (Result 3) as its rigorous anchor, and it is independent of any particular unified theory.

Grades throughout: Result 1 is one-loop / by-construction across four independent constructions; Result 2 is
one-loop-truncation RG (proven two ways within the truncation); Result 3 is a free-case theorem plus a
perturbative interacting argument. This is a structural result at honest grade, not a set of proven all-orders
theorems.

## 7. Relation to prior work

- **PT-symmetric quantum mechanics and the `C`-operator:** Bender-Boettcher; Bender-Brody-Jones; Mostafazadeh
  (pseudo-Hermiticity). Delta: we use the `C`-operator only as one of five constructions and locate its loop cost
  (non-locality) rather than asserting positivity.
- **Fourth-order-gravity ghost and PT/conformal-gravity unitarity:** Stelle; Mannheim; Bender-Mannheim
  (Pais-Uhlenbeck). Delta: the tree-to-loop gap made explicit (the Cutkosky leak, `tests/W48`), and the
  RG-contingency of the grading.
- **Fakeons:** Anselmi-Piva. **Lee-Wick / complex poles:** Lee-Wick; Grinstein-O'Connell-Wise; Donoghue-Menezes.
  Delta: we place both in a common "removal-based" family and price their shared bounded-causality cost against
  the grading-based family's locality cost.
- **Tree-level positivity / hidden parity:** Bateman-Turok. Delta: we separate their all-orders *pseudo*-unitarity
  from *physical positivity*, which is where the loop question actually lives.
- **Loop-level indefinite-metric analyses:** Kuntz; Nakayama. Delta: the positivity-vs-causality trade as an
  organizing statement, plus the no-local-positive-metric theorem.

## 8. Status / open gaps

1. **DONE:** the five-construction map + the RG-stability result + the free-case theorem are reproducible in-repo
   (`tests/W44-W54`, all exit 0); each result carries its honest grade.
2. **The load-bearing open items:** the all-orders interacting metric (Result 3 is free-case + first order); the
   physical-vs-gauge status of the conformal-factor mode (Result 2); a `>=2`-loop CLOP-stability check of the
   Lee-Wick branch; and the non-translation-invariant strengthening of the theorem.
3. **Target framing:** the natural paper is exactly this trio -- "the loop-level cost structure of keep-and-grade
   fourth-order gravity" -- as a structural contribution to a class-wide open problem, GU-independent.

Grade: structural result at honest grade; one machine-checked free-case theorem (Result 3); the positivity-vs-
causality trade and the asymptotic-freedom RG-stability are one-loop-truncation results. Target: hep-th /
math-ph. External publication Joe-gated (NOT in scope here: no arXiv, no submission).

**Update 2026-07-13 (wave 3, `tests/W120`-`W121`; appended, prior text unchanged).** Two of the open items
above have moved.
- *The `>=2`-loop CLOP-stability check of the Lee-Wick branch* is now split in half. The graded (Family 1)
  side is answered at the prescription level: the CLOP order-of-limits ambiguity attaches to the
  contour-deformation step of the removal prescription, and the keep-and-grade construction at strict fixed
  order performs no removal and no deformation, so it does not face the ambiguity there (structural, with the
  one-loop bubble toy check: the graded ghost cut is the negative `-(1/16pi)(1-m_2^2/s)` leak while the
  Lee-Wick conjugate-pair contour gives exactly zero, the two separated by a non-commuting width limit;
  `tests/W120`, 16/16). A new structural point: the graded cut sign is `(-1)^{n_ghost}`, so the CLOP locus
  `s=4m_2^2` is an even, positive, Cutkosky-unambiguous cut in the graded theory while the graded leak locus
  `s=m_2^2` is empty under the Lee-Wick contour; the two families pay at disjoint thresholds. The evasion is
  bounded: the graded ghost is broad and unstable, fixed order fails on an O(1) resonance window, and inside
  that window resummation forces complex poles and the contour question returns for both families. The
  removal-side two-loop tensor computation near `s=4m_2^2` (as specified in the wave-2 pre-gate) remains the
  open half, and is now the single object that would settle the family question.
- *The non-translation-invariant strengthening of the theorem* (Result 3) is partially delivered. The
  large-momentum sign-domination argument is pointwise in position, so no finite-order differential operator
  with position-dependent coefficients can implement the grading (symbolic to degree 6 plus a 4000-draw
  sweep; strong-argument, with the positivity-to-pointwise-symbol-sign link the named argued step). The
  equal-energy shell-mixer escapes are power-law non-local, strictly worse than the canonical exponentially
  localized metric. The locality hypothesis itself is proven tight: the canonical metric is quasi-local
  (strip-analytic of width exactly `m_ghost`), so the theorem cannot be strengthened to exclude quasi-local
  metrics; it sits on the true boundary. Remaining gap: position-dependent local kernels with entire
  non-polynomial fiber symbols (`tests/W121`, 11/11). The all-orders interacting item and the conformal-factor
  item are unchanged.

**Update 2026-07-13 (wave 4, `tests/W124` Stage A and Stage B; appended, prior text unchanged).** The
removal-side two-loop computation named above as "the single object that would settle the family question" is
now done at scalar core. The two-loop sunset self-energy with two ghost lines at the mixed threshold
`s ~ 4m_2^2`, computed under both prescriptions: the graded fixed-order theory gives the unique positive
two-ghost cut (`+Im S`, Krein weight `(-1)^2 = +1`, verified regulator-order independent), while the Lee-Wick
pair gives zero in its proper limit order, and the CLOP order-of-limits ambiguity spans
`{-1/2, 0, +1/2, +1}` times the graded cut depending on the deformation family: the ambiguity width equals
exactly the graded cut, its endpoints (`0` and `+1`) are the two families' own answers, and the intermediate
values are realizable by no Krein-signed state space (integer-multiplicity arithmetic). The genuinely
overlapping (kite) topology with one ghost line has no real mixed pinch at all (the CLOP locus needs two or
more ghost lines in one cut); there the prescriptions agree on ghost-free cuts as the width goes to zero and
differ by the odd-ghost leak, and the heavy-ghost anomalous-threshold (leading Landau) hunt comes back empty:
the graded prescription develops no two-loop ambiguity of its own. The disjoint-loci statement of the wave-3
update is sharpened: the even mixed locus is a locus of genuine inter-family disagreement (full cut vs zero),
not merely of removal-side ambiguity, and the CLOP ambiguity is reinterpreted as the removal contour failing
to decide between the two families' answers rather than an independent third pathology. Remaining open on
this item: the spin-2 tensor numerators (left OPEN as Stage C) and the finite-width Lee-Wick boundary value
by full Euclidean continuation; inside the `O(1)` resonance window the dressed graded ghost is itself a
physical-sheet complex pair (model-verified), so the window guard of the wave-3 update stands unchanged
(`tests/W124_stageA`, 16/16; `tests/W124_stageB`, 11/11).
