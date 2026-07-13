---
artifact_type: exploration
status: exploration (steelman-2 follow-on swing 3 -- does the W104 SIGN-DEFINITIZATION survive MODE-MIXING? the 2-doublet + SHARED-CLOCK toy; directed single-agent swing; deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- the residual kernel of the killed Steelman 2 (W104 T3), tested against the W98 P2 mixing setting
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "W104's one genuinely new structure: group averaging over H_mod + q = 0 with observer energy q >= 0 keeps exactly one survivor per mode, uniformly NEGATIVE Krein norm -- definitization IN SIGN (not in norm; survivor norm s_k -> 0). But it was computed MODE-BY-MODE (each doublet its own clock-constraint). Under interactions the modes MIX (W98 P2) and the physical CLPW observer is ONE clock. Named next computation: does the uniform sign survive mode-mixing through a shared clock? If yes, the residual becomes 'completion of a degenerate-but-definite form' -- a different, possibly tractable question. Kill-or-learn."
title: "VERDICT = SIGN-KILLED-BY-MIXING (in the physical regime); the completion back-door does NOT open. Weak mixing (below the first Krein collision) preserves the uniform sign -- Krein-norm shifts O(eps^2), perturbative = exact. But the PHYSICAL regime (fixed mixing, splitting s_k -> 0: the W98 UV tower has eps/s -> inf) is past the boundary for every UV doublet pair, and there the kernel dies, with an EXACT mechanism: the shared clock constrains only the TOTAL modular energy, so for mixing eps > s the h=+s POSITIVE-Krein-norm mode is dragged below zero total energy and slips UNDER the constraint -- survivors of BOTH signs (analytic in the commuting case: spectrum {+-s+-eps}, survivor -(eps-s) has Krein norm +s > 0). Phase diagram: I (eps < eps_EP: 2 negative survivors, the W104 structure; isotropic window closes ~ s_2, generic ANISOTROPIC window closes QUADRATICALLY ~ s_1*s_2) -> II (Krein collision at h=0 ejects an opposite-signature pair as a Krein-NEUTRAL complex/PT-broken pair with NO constraint solution: 1 survivor or empty) -> III (re-emergence with EXCHANGED signatures: both signs). Genericity census at eps >> s: 186/200 random eta-s.a. couplings in the ejection phase, 7 indefinite, 7 empty, 0/200 retaining the W104 structure. COMPLETION: phase I completes canonically and the modular FLOW descends unitarily, but compressed observables have physical norm 1/s_1 EXACTLY (unbounded over the tower) and the honestly-projected algebra is ABELIAN (multiplicity-free constraint spectrum) -- the completion carries the flow and an abelian remnant, not the algebra (already latent in W104); phase II completes to a genuine NON-degenerate Hilbert space but has already lost HALF the mode content (the ejected neutral pairs connect continuously to genuine healthy+ghost modes -- the quotient kills the ghost physics). ADVERSARY INVERTED: per-mode clocks are what MADE W104's uniform sign (separate constraints); the single shared clock -- the physical CLPW observer -- is what kills it, and with mixing per-mode constraints are not even defined. The W104 kernel is a mode-diagonal artifact; it does not earn continuation."
grade: "exploration / one directed follow-on result at reconstruction grade: the decisive kill (both signs for eps > s under isotropic mixing) is EXACT (commuting case, machine-checked to 1e-15) and the mechanism (the shared clock constrains only the TOTAL energy) is structural; the phase diagram, genericity census, and completion checks are toy-grade (2-doublet 4-dim field space + the W98 tower reading). Encoded in tests/W108_sign_definitization_mixing.py (7/7, numpy-only, exit 0). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The W98 break stands; the conjecture remains a conjecture."
depends_on:
  - explorations/steelman2-krein-crossed-product-2026-07-11.md
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W104_steelman2_crossed_product.py
  - tests/W98_break_sectorial_closure.py
scripts:
  - tests/W108_sign_definitization_mixing.py
external_refs:
  - "V. Chandrasekaran, R. Longo, G. Penington, E. Witten, arXiv:2206.10780 -- the observer is ONE clock with energy bounded below; the constraint is on the TOTAL (field + observer) generator. The shared-clock reading tested here is the CLPW-faithful one."
  - "Krein-space eigenvalue perturbation / Krein collision theory (Gelfand-Lidskii/MacKay-style signature rules): real eigenvalues of opposite Krein signature can leave the real axis only by COLLIDING; same-signature eigenvalues pass through. The phase-II ejection window is exactly an opposite-signature collision at h=0."
  - "PT-symmetric quantum mechanics (Bender et al.): the complex-pair window is the PT-broken phase; complex-conjugate eigenvector pairs are Krein-NEUTRAL (zero self-norm)."
---

# Swing 3 on the killed steelman's kernel: does the sign-definitization survive mode-mixing?

**Role.** W104 killed the CLPW crossed-product rescue (the wall is conserved under dressing: cond_after =
cond_before exactly) but found one genuinely new structure -- **definitization in sign**: group averaging
over `H_mod + q = 0` with observer energy `q >= 0` keeps, per mode, exactly one survivor with uniformly
NEGATIVE Krein norm. Not in norm (survivor norm `s_k -> 0`), but the sign structure was real. W104's own
honesty register named the decisive next computation: the sign selection was **mode-diagonal** (each
doublet paired against its own constraint), and under interactions the modes **mix** (the W98 P2 setting)
through **one** shared observer clock. If the uniform sign survived mixing, the residual would become
"completion of a degenerate-but-definite form" -- a standard, possibly tractable operation, and a
potential back-door to a positive physical sector. This swing does that computation, kill-or-learn.

**Answer: SIGN-KILLED-BY-MIXING (in the physical regime); the completion back-door does not open.**
The uniform sign survives weak mixing and dies exactly where the physics lives, with an exact and
structural mechanism. The W104 kernel was a mode-diagonal artifact of per-mode constraints.

**Artifacts:** this file + deterministic `tests/W108_sign_definitization_mixing.py` (7/7, numpy-only,
exit 0). **Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The mixing** | standard-field: an `eta`-self-adjoint block-off-diagonal coupling `eps*V` between two W52/W98 Krein doublets (`eta_4 V` hermitian forces `C' = sigma_x C^dag sigma_x`); swept over 4 named + 200 random couplings | The Krein-legitimate interaction class -- the same surrogate grade as W98's mixing. The kill is computed inside the program's own Krein structure, not a positive-Hilbert import. |
| **The observer / clock** | CLPW-faithful: **ONE** clock, energy `q >= 0`, constraint `H_1 + H_2 + eps V + q = 0` on the **TOTAL** generator | This is the fork that decides everything. W104's per-mode constraint pairing was the **toy** of group averaging; the physical CLPW observer is a single clock constraining only the total. The kill mechanism lives exactly in that difference. |
| **The survivor rule** | group averaging: a field eigenvector with **real** eigenvalue `h` pairs with the clock state `q = -h`, which exists iff `h <= 0`; **complex**-pair eigenvectors solve no constraint (annihilated) | Named assumption (iv) in the test. Standard rigged-Hilbert group-averaging reading; the complex-pair ejection is its direct consequence. |
| **The load-bearing FORK** | **per-mode clocks (W104's toy) vs one shared clock (CLPW's physics)** | Identified as the decisive fork, and the shared-clock side is the physical one. Per-mode constraints are not even **defined** once the modes mix (`H_total` does not factorize). The uniform sign was an artifact of the toy side of this fork. |

---

## 1. The model (built, not gestured at)

Two W52/W98 Krein doublets with parameters `r_1, r_2`: per doublet `H_mod(r) = [[ir,1],[1,-ir]]`,
`eta_K = sigma_x`, spectrum `+-s`, `s = sqrt(1-r^2)`. Field space `C^4 = C^2 (+) C^2`, Krein form
`eta_4 = sigma_x (+) sigma_x` (signature (2,2)). Mixing `eps*V`, `V` `eta_4`-self-adjoint
block-off-diagonal. One clock, `q >= 0`; constraint `H_field + q = 0`; survivors = eigenvectors of the
**mixed** `H_field` with real eigenvalue `h < 0`. Distinct real eigenvalues are `eta`-orthogonal and
carry orthogonal clock states, so the induced physical Gram is **diagonal** with entries = the Krein
norms (verified to 6e-16): sign-definiteness of the physical form = uniformity of survivor-norm signs.

---

## 2. The computed results (tests/W108, 7/7, exit 0)

### T1 -- control (eps = 0): W104 reproduced exactly
Two survivors `h = -s_1, -s_2`, Krein norms `-s_1, -s_2` -- uniformly negative, degenerate as `r -> 1`,
Gram diagonal. The kernel we are extending is intact in the model.

### T2 -- weak mixing: the sign SURVIVES (phase I)
For `eps = 0.1 s_1 s_2` (inside phase I for **every** coupling class) the survivor subspace stays 2-dim
and uniformly negative across all couplings and the whole `(r_1, r_2)` grid up to `r = 0.9995`. The
Krein-norm shift is `O(eps^2)` (shift/eps^2 constant to <1% over a dyadic ladder): no first-order sign
motion. **Perturbative derivation (D2a) and exact diagonalization (D1) agree.**

### T3 -- THE EXACT KILL (D2b): both signs for eps > s, analytically
At `r_1 = r_2 = r` the isotropic coupling `V = sigma_x (x) I_2` **commutes** with
`H_0 = I_2 (x) H_mod(r)`. Joint eigenvectors `u_a (x) w_b`, eigenvalues `h = b s + a eps`, and the Krein
norm of each is the **doublet** norm `b s`, independent of the mixing branch `a`. For `eps > s` the
survivor set is exactly

> `{ h = -(eps+s): kn = -s < 0 ;   h = -(eps-s): kn = +s > 0 }` -- **BOTH SIGNS.**

Machine-checked to 1e-15 at `r in {0.3, 0.9, 0.99}`. **The mechanism is structural:** the shared clock
constrains only the **TOTAL** modular energy. Mixing redistributes energy between the doublets, so the
`h = +s` positive-Krein-norm mode is dragged below zero total energy and **slips under the constraint**
the moment the mixing exceeds the splitting. W104's uniform sign existed because per-mode constraints
forbade exactly this.

### T4 -- the phase diagram and the boundary
Three phases in `(eps; r_1, r_2)`, mechanism = a **Krein collision at h = 0** (the `-s_2 / +s_2`
opposite-signature pair):

| Phase | Range (isotropic) | Survivors | Sign |
|---|---|---|---|
| **I** | `eps < eps_EP ~= s_2` | 2, norms `~ -s` (degenerate) | uniform negative -- the W104 structure |
| **II** | `s_2 < eps < s_1` | 1 (or 0): the collided pair is COMPLEX (PT-broken), Krein-**neutral**, solves NO constraint -- **ejected** | survivor negative, but half the content gone |
| **III** | `eps > eps_flip ~= s_1` | 2, re-emerged with **EXCHANGED** signatures | **both signs -- killed** |

Boundary verified on the grid: `eps_EP = s_2` and `eps_flip = s_1` to <5%. **Anisotropic couplings:**
the phase-I window closes **quadratically**, `eps_EP ~ O(s_1 s_2)` (constant ratio 0.50 / 1.27 over the
r-grid for the two tested classes) -- for generic mixing the sign-definite phase is even narrower near
the exceptional locus, and the re-emergence point is set by the coupling anisotropy scale, `O(1)`.

### T5 -- the physical regime is on the failing side
The W98 tower has **fixed** interaction strength and `s_k -> 0` in the UV: `eps/s -> inf` -- every UV
doublet pair sits past the phase-I boundary (which itself closes at least linearly, generically
quadratically, in `s`). Computed at fixed `eps`, `r -> 1` (0.99 -> 0.9999):

- **isotropic coupling: INDEFINITE** at every `r` -- both signs, norms `+-O(s)`: indefinite **and**
  degenerate, the worst case;
- **generic anisotropic couplings: the EJECTION phase** -- 1 survivor per pair, negative, norm `O(1)`
  (non-degenerate!) but **half the mode content annihilated** as Krein-neutral PT-broken pairs;
- **genericity census** (200 random `eta`-s.a. couplings at `eps >> s`): **186 ejection / 7 indefinite /
  7 empty / 0 retaining the W104 structure.** Zero.

In **no** coupling class does "one uniformly-negative survivor per mode" survive the physical regime.

### T6 -- the completion back-door does NOT open
- **Phase I** (where the sign survives): the definite-but-degenerate form completes canonically
  (quotient trivial at finite rank; over the tower the completion is a genuine Hilbert space) and the
  modular **FLOW descends unitarily** (survivors are eigenvectors; phases `e^{ihp}`). **But the algebra
  does not:** the compressed generic observable has physical-norm operator norm `= 1/s_1` **exactly**
  (computed: 2.3 -> 7.1 -> 22.4 -> 70.7 tracking `1/s_1` to <5% as `r -> 1`) -- unbounded over the
  tower. And clock-orthogonality of distinct survivors forces the honestly-projected algebra to be
  **diagonal** in the survivor basis: an **abelian** remnant (functions of `H_field`). *Honest note:
  this was already latent in W104 -- a multiplicity-free constraint spectrum compresses any algebra to
  an abelian one; the completion was never going to carry the noncommutative algebra.*
- **Phase II** (the generic physical regime): the completion is a genuine **non-degenerate** Hilbert
  space (survivor norm `O(1)`) -- but it carries **half** the modes and is 1-dim per doublet-pair
  (abelian again). The ejected neutral pairs are genuine field content: at `eps -> 0` they connect
  continuously to one healthy + one ghost mode (verified: all 4 eigenvalues real at `eps = 1e-6`,
  2 complex at `eps = 1`). **What the quotient/ejection kills IS the ghost physics.**
- **Phase III**: indefinite; nothing to complete.

---

## 3. Adversary presses, answered

- **(a) "The shared clock is one observer -- multiple observers/clocks would break it again."**
  **INVERTED by the computation.** Multiple (per-mode) clocks are exactly what **made** W104's uniform
  sign: separate constraints per mode forbid the energy redistribution that smuggles the positive-norm
  mode under the constraint. The **single shared clock is the physical CLPW setting** (one observer,
  one worldline, one energy bound), and it is the one that kills. Worse for the rescue: once the modes
  mix, `H_total` does not factorize, so per-mode constraints are not even **defined** -- there is no
  multi-clock version of the interacting model to retreat to. The more physical the observer model,
  the deader the kernel.
- **(b) "The null directions you quotient away ARE the ghost physics."** **CONFIRMED**, in the precise
  phase-II form: the directions the physical projection annihilates are not marginal null junk -- the
  ejected Krein-neutral complex pairs connect continuously to genuine healthy+ghost mode content, i.e.
  the annihilated sector is exactly the ghost-graded physics the conjecture is about. And in phase I the
  quotient's cost appears instead as operator-norm degeneration (`1/s_1`): the algebra, not the vectors,
  is what the completion loses there. Either way the completion never carries the physics.
- **(c) "The kill is an artifact of the isotropic coupling."** No: the isotropic case is where the kill
  is **exact** (T3), and the genericity census (T5) shows the alternative for generic couplings is not
  survival but **ejection** (86% of random couplings) or indefiniteness/emptiness (14%) -- 0/200 retain
  the W104 structure. "Sign survives" in the ejection phase is vacuous for the kernel's purpose: the
  surviving sector no longer contains the mixed modes' content, and its compressed algebra is abelian.
- **(d) "Maybe the ejection phase is the interesting object"** (steelmanning what remains): the phase-II
  completion IS a genuine non-degenerate Hilbert space with a unitary flow -- noted honestly. But it is
  half the modes, abelian, coupling-dependent (which phase you land in depends on the anisotropy of the
  mixing), and it is not the W104 kernel surviving -- it is a different, smaller object whose physical
  reading is "the constraint discards the ghost sector wholesale," which is a positive-subspace
  **removal** in disguise, exactly what the program's keep-and-grade discipline rejects as the answer to
  HORN K.

**Load-bearing assumptions (named):** (i) the W52 doublet + W98 tower as the Krein type-III surrogate
(same toy grade as W91/W98/W104); (ii) the `eta`-self-adjoint block-off-diagonal class as the mixing
surrogate (4 named + 200 random couplings); (iii) mixing not UV-soft faster than the splitting -- the
same W98 assumption, the one honest survival window (`eps(k) = o(s_k)` would pin every UV pair in phase
I), not the physical derivative-coupled case; (iv) survivors = real eigenvalues `h < 0` (group averaging
with a `q >= 0` clock; complex pairs solve no constraint).

---

## 4. VERDICT: SIGN-KILLED-BY-MIXING (physical regime); the kernel does not earn continuation

Per the task's trichotomy:

- **NOT** SIGN-SURVIVES + COMPLETION-VIABLE: in the physical regime the sign structure does not survive
  in any coupling class (indefinite, ejected, or empty; 0/200 retain W104's structure).
- **SIGN-SURVIVES-BUT-COMPLETION-LOSES-PHYSICS holds only in phase I** (weak mixing, `eps` below the
  first Krein collision) -- and even there the completion carries the flow plus an abelian remnant, not
  the algebra (compressed norms `1/s_1`, unbounded over the tower). Phase I excludes the physical regime.
- **SIGN-KILLED-BY-MIXING in the physical regime** -- the verdict. The kill is exact (T3), the mechanism
  structural (the shared clock constrains only the total energy), the boundary located (T4), the
  physical regime unambiguously past it (T5), and the completion back-door closed at both ends (T6).

**The theorem-shaped statement of the swing:** *W104's sign-definitization is a mode-diagonal artifact
of per-mode constraints. A single shared positive-energy clock constrains only the TOTAL modular energy;
under mode-mixing stronger than the modular splitting -- the generic UV situation of the W98 tower --
either a positive-Krein-norm mode slips under the constraint (both signs; isotropic/exact) or the
constraint ejects Krein-neutral PT-broken pairs wholesale (generic; the ghost content is discarded, not
graded). The "completion of a degenerate-but-definite form" residual never materializes as a back-door:
where the form is definite-degenerate the completion loses the algebra; where it is definite-nondegenerate
it has already lost half the physics.*

**Two-derivation status: AGREE.** D1 = exact diagonalization (control, sweep, phase diagram, census,
completion); D2 = perturbation theory at weak mixing (O(eps^2) norm shifts, matching D1 to <1%) + the
exact commuting-case analytic kill (spectrum `{+-s+-eps}`, survivor norms `+-s`, machine-checked).

**Confidence.** The exact kill (T3) and its mechanism: **HIGH** (analytic, structural, machine-verified).
The phase diagram and boundary scaling (T4): **MEDIUM-HIGH** (clean numerics, 2-doublet toy). The
physical-regime placement (T5): **MEDIUM-HIGH** -- it inherits W98's non-UV-soft coupling assumption
(named); if the cross-mode mixing were UV-soft faster than the splitting, phase I would survive, and that
window is not the physical derivative-coupled case. The completion verdict (T6): **MEDIUM** -- the
abelianization argument is structural (multiplicity-free constraint spectrum), but a continuum
group-averaging treatment (clock with genuinely continuous spectrum, dressed-operator algebra rather than
compressions) is frontier work this toy does not decide. Overall SIGN-KILLED-BY-MIXING: **MEDIUM-HIGH**.

**What would move it.** (a) A multi-doublet (N > 2) shared-clock model with tower-realistic couplings --
would test whether the ejection fraction or the indefinite fraction dominates at scale (does not change
the verdict's direction: neither branch is the W104 kernel). (b) A continuum group-averaging construction
with a genuine `L^2(R)` clock and the dressed-operator (rather than compression) reading of the physical
algebra -- the one place a nontrivial physical algebra could still hide; frontier, do not start without
new input. (c) If someone proves the physical cross-mode mixing IS UV-soft faster than the splitting,
phase I becomes the physical regime and the degenerate-definite completion question reopens (with its
T6a losses still standing).

---

## 5. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action. The conjecture remains a conjecture; the W98 break stands; H61/H61a remain OPEN. This swing
closes W104's named next computation with an honest kill: the sign-definitization -- the killed
steelman's kernel of truth -- does not survive mode-mixing in the physical regime, and the
degenerate-but-definite completion residual is not a back-door. This branch **presents, does not
decide** -- it hands the orchestrator: the 2-doublet shared-clock model, the exact kill mechanism (the
shared clock constrains only the total energy), the three-phase diagram with located boundaries
(`eps_EP ~= s_2` isotropic / `O(s_1 s_2)` generic; `eps_flip ~= s_1`), the 0/200 genericity census, the
two-ended closure of the completion back-door, and the verdict -- **SIGN-KILLED-BY-MIXING**.
Reproducible: `tests/W108_sign_definitization_mixing.py` (7/7, exit 0).
