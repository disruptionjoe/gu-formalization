---
artifact_type: exploration
status: exploration (the scoped FIRST DECISIVE COMPUTATION of steelman 3 / W105: the per-state/sup separation theorem on the W98 interacting Krein model; kill-mode run honestly; analytic derivation + deterministic quadrature)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture critical path, post-W98) -- the ONE-SIDEDNESS THEOREM's step 1
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "THE PER-STATE/SUP SEPARATION THEOREM (scoped by W105 Sec 4 as the first decisive, kill-capable computation). Target: on the W98 continuum/interacting Krein model, the definitizability divergence is carried ENTIRELY by uniformity (the sup over the mode tower) and NEVER by any fixed physical matrix element. (I) For every fixed admissible state in a SHARP class (to be found, not assumed), every audited physical form -- expectation values, the per-state strip continuation (KMS/crossing), the Araki relative-modular form -- is FINITE and cutoff-convergent, at every order the model supports. (II) The divergence appears IFF one demands uniformity over the whole state space (the operator-norm sup): the failure is exactly the non-existence of the bounded intertwiner, never of any individual number. Pre-registered kill-modes: (a) a physical packet class with non-integrable per-state growth; (b) higher-order compounding of the growth exponent beyond polynomial (exponential swallows Schwartz decay and kills); (c) local-operator states whose OPE-mandated UV tails fall outside the sharp class."
title: "VERDICT = THEOREM-WITH-EXCLUSIONS (on the model; exclusions named and benign-by-parallel). Parts (I)+(II) HOLD with a SHARP state class: the strip (KMS/crossing) form is the quadratic form of the unbounded multiplication operator ~ |k|^{(p+1)/2} (vertex growth g_k = G k^p; p=0 is the W98 run), so per-state finiteness holds EXACTLY on its form domain D(|k|^{(p+1)/4}) -- power-law boundary alpha*(p) = (p+3)/4 (= 3/4 at p=0), endpoint log-divergent (excluded, no log improvement) -- while the unit-ball sup diverges like sqrt(2) per UV doubling (the W98 break, restated as the converse leg). The dichotomy is EXACT: finiteness-per-state on a dense domain + divergence-of-sup is precisely the dichotomy of an unbounded densely-defined quadratic form; the sup is realized by normalized UV-edge runaway states, so no third regime and no approximation artifact. THE AUDITED FORMS ARE NESTED: expectation values need only L^2 (eta is bounded -- it is the INVERSE powers that grow); Araki entropy (log Delta_rel) needs only a log weight (class: essentially all of L^2, alpha > 1/2); the strip continuation needs D(|k|^{1/4}); the Delta^{-1} face needs D(|k|^{1/2}). The load-bearing physical bottleneck is the STRIP form. MANDATORY STATES INSIDE: Schwartz packets (all polynomial orders); smooth-smeared (C-inf-compact, Reeh-Schlieder/Wightman-class) local-operator states -- Paley-Wiener superpolynomial momentum decay beats k^{(p+1)/2} for every p (kill-mode (c) survives: the physical smearing class is inside); the p=0 perturbative interacting vacuum (pair tail c_k ~ G/2k, strip form convergent). NAMED EXCLUSIONS (the honesty): (i) sharp-boundary chi_O states (characteristic-function smearing, tail alpha=(d+1)/2) sit exactly ON the boundary at derivative coupling p>=1 and log-diverge -- an idealization exclusion, parallel to the standard sharp-edge energy divergences of ordinary QFT; (ii) the dense image M(O)|0> as a WHOLE necessarily leaks outside the class (structural: an unbounded form is never finite on a dense set's entirety -- exactly parallel to 'bounded local operators can create infinite-energy states' in ordinary QFT, which nobody counts against QFT); (iii) at p>=1 the perturbative Fock vacuum is non-normalizable BEFORE any Krein issue (the Haag obstruction) -- the vacuum then enters only as a GNS state functional (grade C3). HIGHER ORDERS (kill-mode (b)): the growth exponent is (p+1)/2 -- polynomial for every polynomial vertex, loop logs subleading (measured); the honest WOULD-KILL is demonstrated: an exponential effective vertex g ~ e^{k/50} makes the form diverge on a FIXED superpolynomially-decaying (Schwartz-decay-class) packet -- so the all-orders leg rests exactly on Weinberg's asymptotic power-counting theorem (polynomial momentum growth at every order of local finite-derivative perturbation theory), a named, load-bearing, literature-grade input, not decoration. UPSHOT: the one-sidedness steelman's mechanism claim is upgraded from audit-grade (W105) to theorem-grade ON THE MODEL: the W98 break is carried entirely by uniformity; every physically-mandatory fixed matrix element converges."
grade: "exploration / one theorem-grade result ON THE W98 MODEL (sharp class = form domain D(|k|^{(p+1)/4}); exact unbounded-form dichotomy; mandatory states inside; three named exclusions) + one honest would-kill demonstration (exponential compounding kills; excluded by Weinberg power counting -- the named all-orders input). Two-derivation status: AGREE (D1 analytic exponent/boundary computation with predicted doubling-ratios; D2 direct numerical quadrature -- predictions 0.500/1.000/1.414 matched to <0.06 in every test). Encoded in tests/W106_per_state_sup_separation.py (8/8, numpy-only, exit 0). NOT a continuum operator-algebra theorem beyond the model: the model is the W98 mode tower (the same surface the break itself was established on -- symmetric rigor); the continuum statement inherits C3 (Gottschalk-grade interacting strip analyticity). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change."
depends_on:
  - explorations/steelman3-j-freeness-2026-07-11.md
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - explorations/cond-iii-w54-all-orders-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W105_steelman3_j_freeness.py
  - tests/W98_break_sectorial_closure.py
  - tests/W97_cond_iii_all_orders.py
scripts:
  - tests/W106_per_state_sup_separation.py
external_refs:
  - "M. Reed & B. Simon, Methods of Modern Mathematical Physics I/II -- quadratic forms of unbounded self-adjoint operators: a positive form is finite exactly on its form domain Q(A)=D(A^{1/2}), dense; the unit-ball sup equals ||A|| (infinite iff A unbounded). The exact-dichotomy backbone of Part (II)."
  - "S. Weinberg, Phys. Rev. 118 (1960) 838 -- the asymptotic-behavior theorem: renormalized perturbation-theory amplitudes grow at most polynomially (times logs) in momenta at every order. The named all-orders input excluding exponential compounding of the per-mode growth exponent."
  - "R. Paley & N. Wiener / standard Fourier theory -- the Fourier transform of a C^inf compactly supported function decays faster than any polynomial (for this bump class ~ e^{-c sqrt(k)}). The reason the physical (Reeh-Schlieder/Wightman) smearing class is inside the sharp class at every polynomial order."
  - "H. Reeh & S. Schlieder, Nuovo Cimento 22 (1961) 1051 -- local-operator states A|0> for A in a LOCAL algebra are dense; the density is exactly why the FULL set M(O)|0> cannot lie inside any unbounded form's domain (named exclusion (ii)), and why the physical statement is about the smeared-field core, which is."
  - "R. Haag, Kgl. Danske Videnskab. Selskab Mat.-Fys. Medd. 29 (1955) no. 12 (Haag's theorem) -- the interacting vacuum is not a vector of the free Fock space; at p>=1 the perturbative pair tail is non-normalizable BEFORE the Krein question arises (named exclusion (iii))."
  - "H. Gottschalk, J. Math. Phys. 43 (2002) 4753 -- Krein Bisognano-Wichmann: the flow and its strip analyticity on dense analytic vectors survive the indefinite metric; the continuum-side grade (C3) that the model-level theorem inherits."
  - "J. Bros, H. Epstein, V. Glaser, Comm. Math. Phys. 1 (1965) 240 -- crossing as per-state analytic continuation (no operator J); the physical quantity whose per-state cost the strip form models."
  - "D. Krejcirik & P. Siegl, Phys. Rev. D 86 (2012) 121702 -- bounded metric with UNBOUNDED inverse: the reason the metric form (expectations) needs only L^2 while the inverse powers (strip, Delta^{-1}) carry the growth."
---

# The per-state/sup separation theorem: is the W98 break carried entirely by uniformity?

**Role.** `W105` (steelman 3) closed its audit with a scoped path to the ONE-SIDEDNESS THEOREM and named
its **step 1 -- the first decisive, kill-capable computation**: prove on the `W98` interacting Krein model
that the definitizability divergence is carried **entirely by the sup over modes** and **never by any
fixed physical matrix element** -- or find the kill (a physical packet class or a loop order where the
per-state growth becomes non-integrable). This swing runs exactly that computation, with the kill-modes
pre-registered and run for real.

**The target theorem.**
> **(I)** For every fixed admissible state in a sharp class (found, not assumed), every audited physical
> form -- the metric form (expectation values / transition amplitudes), the strip-continued form
> (per-state KMS/crossing at `Im t = 1/2`), the relative-modular / Araki-entropy form (`log Delta_rel`)
> -- is **finite and cutoff-convergent**, at every order the model supports.
> **(II)** The divergence appears **iff** one demands uniformity over the whole state space (the
> operator-norm sup): the failure is exactly the non-existence of the **bounded intertwiner**, never of
> any individual number.

**Answer: THEOREM-WITH-EXCLUSIONS (on the model).** Parts (I)+(II) hold with the sharp class
`D(|k|^{(p+1)/4})`; the class contains every physically-mandatory state tested (Schwartz packets,
smooth-smeared local-operator states at all polynomial orders, the `p=0` perturbative vacuum); three
exclusions are named, each with its standard-QFT parallel. The growth exponent is stable (polynomial) at
higher orders, with the honest would-kill demonstrated and the input that excludes it named.

**Artifacts:** this file + deterministic `tests/W106_per_state_sup_separation.py` (8/8, numpy-only,
exit 0). **Not committed by this run. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **Ghost clearance** | GU-native **keep-and-grade** (Krein), as everywhere on this path. | The strip/inverse-metric growth IS the kept ghost's UV degeneracy (`W98` mode data, unchanged). |
| **The mode data** | the `W98` model itself: `1 - r_k = (Dw/2)/(g_k + Dw/2)`, `Dw ~ m2^2/2k`, vertex growth `g_k = G k^p`. | Symmetric rigor: the theorem is proved on exactly the surface the break was established on. `p` is the **named** vertex-growth fork (p=0: W98's run; p=1: the physical derivative-coupled ghost; the exploration treats it as a parameter, not a default). |
| **The state class** | **standard-physics side**: Schwartz packets, Paley-Wiener smearing classes, Reeh-Schlieder local-operator states, the perturbative vacuum. The classifier "is this state physically mandatory?" is standard QFT, fixed before the audit. | The kill-mode question is whether physics FORCES states outside the class -- so the mandatory list must come from the standard side, independent of the theorem's outcome. |
| **The dichotomy backbone** | **standard-mathematics side**: Reed-Simon quadratic-form theory (form domain = D(A^{1/2}); unit-ball sup = ||A||). | The exactness of the per-state/sup dichotomy is not model-specific: it is the definition of an unbounded densely-defined form. The model supplies WHICH operator; form theory supplies the dichotomy. |

**The one fork this swing turns on (named):** *the vertex-growth exponent `p`.* The sharp class depends
on it (`alpha*(p) = (p+3)/4`); the physically honest case is arguably `p=1` (derivative-coupled Weyl^2
ghost), where one named exclusion (sharp-boundary states) appears at the endpoint. The theorem is proved
for **all polynomial p simultaneously**, so no silent default.

---

## 1. The analytic derivation (D1)

**The per-mode costs.** From the repo's exceptional-point metric `eta_+(r)` (eigenvalues `1 -+ r`) and
the `W98` mode data with `g_k = G k^p`:

```
  1 - r_k  ~  m2^2 / (4 G k^{p+1})            (UV)
  metric form         cost_eta(k)   = 1 + r_k                    <= 2      BOUNDED
  entropy / log form  cost_log(k)   = log((1+r_k)/(1-r_k))       ~ (p+1) log k
  strip continuation  cost_strip(k) = (1-r_k)^{-1/2}             ~ sqrt(4G/m2^2) k^{(p+1)/2}
  Delta^{-1} face     cost_inv(k)   = (1-r_k)^{-1}               ~ (4G/m2^2) k^{p+1}
```

(`W106` T1 measures the strip exponents `0.4999 / 1.000 / 1.500` at `p = 0, 1, 2` -- the analytic
`(p+1)/2` to `<0.03`.)

**The sharp class (the theorem's real content).** The strip form is the quadratic form of the unbounded
positive **multiplication operator** `A_p ~ |k|^{(p+1)/2}`. Standard form theory (Reed-Simon):

- `<f, A_p f>` is finite **exactly** on the form domain `Q(A_p) = D(A_p^{1/2}) = D(|k|^{(p+1)/4})` --
  a **dense** subspace;
- `sup_{||f||=1} <f, A_p f> = ||A_p|| = infinity`.

So Part (I) + Part (II) together are **precisely** the statement that the strip form is an unbounded,
densely-defined form -- the dichotomy is exact by definition, not an approximation artifact. The model's
contribution is identifying **which** operator (`|k|^{(p+1)/2}`, polynomial) and hence **which** dense
class.

**The power-law boundary.** For `|f(k)| ~ k^{-alpha}` in the model measure `dk`:
`integral k^{(p+1)/2 - 2 alpha} dk` converges iff `alpha > alpha*(p) = (p+3)/4` (p=0: **3/4**); the
**endpoint** `alpha = alpha*` is log-divergent -- excluded, with no log improvement. (Physical `d=3`
measure `k^2 dk`: `alpha*_3D = alpha*_1D + 1`; e.g. `7/4` at p=0. Same structure, shifted boundary.)

**The nested hierarchy of audited forms** (which physical quantity needs which class):

| Form | Physical quantity | Per-mode cost | Sharp class (p=0, model measure) |
|---|---|---|---|
| metric `eta` | expectation values, transition amplitudes | bounded (`<= 2`) | **all of L^2** (Krejcirik-Siegl: it is the INVERSE that is unbounded) |
| `log Delta_rel` | **Araki relative entropy** | `~ log k` | log weight: essentially all of L^2 (`alpha > 1/2`) |
| `Delta^{-1/2}` strip | **KMS / crossing continuation** | `~ k^{1/2}` | `D(|k|^{1/4})`, `alpha > 3/4` |
| `Delta^{-1}` | the operator-packaging face | `~ k` | `D(|k|^{1/2})`, `alpha > 1` |

The **load-bearing physical bottleneck is the strip form** (KMS/crossing); the Araki entropy is far more
forgiving. `W106` T3 verifies the nesting on a single probe state (`alpha = 0.65`: metric and entropy
converge, strip and `Delta^{-1}` diverge; on a Schwartz packet all four converge).

---

## 2. The kill-modes, run honestly

### (a) Physical packet classes with slow decay

- **Smooth-smeared local-operator states (the mandatory class).** The Reeh-Schlieder / Wightman smearing
  class is `C^inf_c` test functions, whose Fourier transforms decay **faster than any polynomial**
  (Paley-Wiener; for the bump class `~ e^{-c sqrt(k)}`). `W106` T5 measures a genuine bump FT envelope:
  `env(100)/env(25) = 2.9e-3 < 4^{-3.5}`, superpolynomial. So the physical smearing class is **inside
  the sharp class for every polynomial order p**. Kill-mode (a) does not fire on the mandatory class.
- **Sharp-boundary states (the idealization).** Characteristic-function smearing `chi_O` has tail
  `alpha = (d+1)/2` (model measure: `alpha = 1`). At `p=0` this is inside (`rho = 0.707`, converges).
  At `p=1` it sits **exactly on the boundary** and log-diverges (`rho = 1.000`) -- **named exclusion
  (i)**. Parallel: in ordinary QFT sharp-boundary states already carry divergent edge energy
  (vacuum-entanglement edge divergences); the exclusion tracks a known idealization pathology, not a new
  physical loss. Same structure in the `d=3` measure (chi-ball `alpha = 2` vs `alpha*_3D`: inside at
  p=0, endpoint at p=1).
- **Infrared tails (bremsstrahlung-like).** Not a threat here: the strip cost is **bounded at k -> 0**
  (`r_0 = G/(G + m2/2) < 1`); soft tails that break L^2-normalizability are an IR issue prior to and
  independent of this UV question.

### (b) Higher-order compounding of the growth exponent

- **Polynomial vertices stay polynomial:** exponent `(p+1)/2` at every `p` (T1); a loop-log surrogate
  `g ~ k log k` shifts the measured exponent only to `1.057` (log-subleading, class unchanged); Schwartz
  packets converge at `p = 0, 1, 2` and with loop logs (T7).
- **The honest WOULD-KILL, demonstrated:** an exponential effective vertex `g_k = G e^{k/50}` gives
  `cost_strip ~ e^{k/100}`, and the packet `|f|^2 = e^{-2 ln^2(1+k)}` -- which decays **faster than any
  polynomial** (Schwartz-decay class) -- has log-integrand growing without bound (`-64 -> +272`,
  monotone): the form **diverges on a fixed Schwartz-class state**, and the theorem would die. So the
  polynomial bound is genuinely load-bearing.
- **What excludes it:** Weinberg's asymptotic theorem -- renormalized perturbation theory with local,
  finite-derivative vertices produces at most polynomial (times log) momentum growth **at every order**.
  This is the **named all-orders input**: the theorem's higher-order leg is exactly as strong as
  Weinberg power counting on the Krein tower (literature-grade on the Hilbert side; its Krein transfer
  shares C3's grade).

### (c) Local-operator / OPE tails and the interacting vacuum

- **The perturbative interacting vacuum (p=0):** pair tail `c_k ~ G/2k`; Fock norm converges AND the
  strip form on it converges (T6, `rho = 0.5 / 0.707`). **Inside the class.**
- **p>=1:** the Fock norm itself diverges (`rho ~ 2` per doubling) -- **Haag's obstruction** (the
  interacting vacuum is not a free-Fock vector), which fires **before** any Krein/definitizability
  question. **Named exclusion (iii):** at derivative coupling the vacuum enters only as a GNS state
  functional; its per-state KMS statement is the C3 (Gottschalk-grade) frontier, inherited, not new.
- **The dense set M(O)|0> as a whole:** cannot lie inside any unbounded form's domain (it is dense;
  the form domain is a proper dense subspace). **Named exclusion (ii)** -- structural, and exactly
  parallel to ordinary QFT, where bounded local operators can create states of **infinite energy** and
  nobody counts that against the theory: the physically-preparable states are the smeared-field core,
  which IS inside.

---

## 3. VERDICT: THEOREM-WITH-EXCLUSIONS (on the model)

**The earned statement.**
> On the `W98` interacting Krein mode tower with polynomial vertex growth `g_k = G k^p`: the strip
> (KMS/crossing) form is the quadratic form of the unbounded multiplication operator `~ |k|^{(p+1)/2}`;
> it is finite and cutoff-convergent **exactly** on the dense sharp class `D(|k|^{(p+1)/4})` (power
> boundary `alpha*(p) = (p+3)/4`, endpoint log-divergent), and the unit-ball sup diverges (`sqrt(2)` per
> UV doubling -- the `W98` break as the converse leg), realized by normalized UV-edge runaway states.
> The dichotomy is the exact unbounded-form dichotomy: **the break is carried entirely by uniformity;
> no fixed matrix element in the class ever diverges.** The class contains the physically-mandatory
> states -- Schwartz packets and smooth-smeared local-operator states at every polynomial order, and the
> `p=0` perturbative vacuum. Excluded, by name: sharp-boundary `chi_O` states at `p>=1` (endpoint);
> the dense image `M(O)|0>` as a whole (structural); the `p>=1` Fock vacuum (Haag, prior to Krein).
> The audited-form hierarchy is nested: expectations need only L^2; Araki entropy only a log weight;
> the strip is the bottleneck.

**Why this is earned, not manufactured.** (1) The kill was reachable three ways and was genuinely
hunted: a mandatory packet class outside the class (T5 -- smooth smearing measured superpolynomial, the
sharp-boundary case honestly logged as an exclusion); non-polynomial compounding (T7 -- the exponential
would-kill is **demonstrated**, not waved at, and the input excluding it is named as load-bearing);
OPE/vacuum tails (T6 -- the p>=1 vacuum failure is found and attributed to Haag, the correct prior
obstruction). (2) D1 and D2 agree quantitatively: every predicted doubling ratio (0.500 / 1.000 / 1.414
/ 0.707 / 2.0) matched measurement to `<0.06`. (3) The endpoint is excluded, not fudged: `alpha = alpha*`
log-diverges and the test requires the marginal signature (constant increments), distinguishing it from
both convergence and power divergence.

**What this upgrades.** `W105`'s sharp mechanism ("the break is sup-level; physical quantities are
per-state") was audit-grade with the separation *prototyped* (W105 T3, one packet). It is now
**theorem-grade on the model**: sharp class identified and proven exact (form-domain characterization +
boundary with endpoint), mandatory states verified inside at all polynomial orders, converse leg
restated as the same form's unit-ball sup, dichotomy exactness reduced to standard form theory. This is
step 1 of the scoped ONE-SIDEDNESS THEOREM (`W105` Sec 4) -- done, with exclusions named.

**What VIABLE/THEOREM here does NOT mean (do not overclaim):**
- It is **not** a continuum operator-algebra theorem. The model is the `W98` mode tower -- the same
  surface the break itself lives on (symmetric rigor, as `W98` vs `W94`). The continuum statement
  inherits **C3** (Gottschalk-grade interacting strip analyticity) and, for the all-orders leg, the
  Krein transfer of Weinberg power counting.
- It does **not** repair `W94` or weaken `W98`: the sup DOES diverge -- that leg is re-proven here.
- The exclusions are real: at derivative coupling (`p>=1`, arguably the physical case) sharp-boundary
  idealizations and the Fock-vacuum picture both fail -- for standard-QFT reasons (edge divergence;
  Haag) that precede the Krein question, which is exactly why they are exclusions and not kills.

---

## 4. Confidence grade and what would move it

- **Sharp class = form domain `D(|k|^{(p+1)/4})`, boundary `(p+3)/4`, endpoint excluded:** **HIGH on
  the model** (exact form theory + measured boundary signatures at `<0.06`).
- **Dichotomy exactness (Part II; no artifact):** **HIGH** -- reduced to the definition of an unbounded
  densely-defined form; the sup's runaway witnesses are normalized states.
- **Mandatory states inside (smooth smearing, all polynomial p):** **HIGH** (Paley-Wiener + measured
  bump FT); the "mandatory" classifier is standard QFT, fixed ex-ante.
- **Growth exponent polynomial at all orders:** **MEDIUM-HIGH** -- exact for polynomial vertices and
  loop-log surrogates on the model; the all-orders claim rests on Weinberg power counting, whose Krein
  transfer shares C3's grade. The would-kill is demonstrated, so this input is named as load-bearing.
- **Continuum transfer:** **MEDIUM** -- C3 (Gottschalk) is the inherited frontier; nothing here worsens
  or improves it.
- **VERDICT = THEOREM-WITH-EXCLUSIONS:** **MEDIUM-HIGH** overall -- theorem-grade on the model,
  exclusions named with standard-QFT parallels, capped below HIGH by the continuum/C3 inheritance and
  the Weinberg-transfer grade.

**What would move it most:** (a) a Krein-side proof (or refutation) of polynomial power counting for the
interacting doublet at two loops -- the one place kill-mode (b) could still fire; (b) upgrading C3
(interacting Krein strip analyticity, Gottschalk -> theorem) -- promotes the model theorem toward a
continuum one; (c) adversarially: any physically-forced state with tail exactly at or below
`alpha*(p_physical)` that is NOT an idealization artifact -- would convert exclusion (i) into a kill.

---

## 5. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; the `W98` break
STANDS (its sup-divergence leg is re-proven here as Part (II)); the `W94` retraction is untouched. What
this swing adds: the `W105` one-sidedness mechanism upgraded to **theorem-grade on the model** -- the
sharp state class (`D(|k|^{(p+1)/4})`, boundary `(p+3)/4`, endpoint excluded), the exact per-state/sup
dichotomy, the mandatory-state verification (kill-modes (a)/(c) survive on the physical smearing class),
the higher-order exponent stability with the honest would-kill demonstrated (kill-mode (b) survives
conditional on Weinberg power counting, named), and three named exclusions each with its standard-QFT
parallel. This branch **presents, does not decide** -- it hands the orchestrator: the theorem statement,
the class boundary, the exclusions, the named all-orders input, and the verdict --
**THEOREM-WITH-EXCLUSIONS**. Reproducible: `tests/W106_per_state_sup_separation.py` (8/8, exit 0).
