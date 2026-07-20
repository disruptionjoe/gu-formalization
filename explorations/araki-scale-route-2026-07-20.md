---
title: "Araki scale route: the entropy functional between the two Krein cuts is structurally dead at toy grade (K-a + K-b, mechanism named -- the cut-swap involutions make every entropy K_S-even while the sector datum is the relative K_S sign); Bianconi's absolute scale rides on the measure normalization and couplings while her entropy core is ratio-only like GU's; her dressed metric is a homonym of S = K_S e^{alpha w}"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (parallel wave: Araki scale route)"
axiom: "lab/process/boundary-adapter-standing-axiom.md for the SECTOR reading of the cuts (R0_COND, as in F2/F5); the vanishing theorems themselves are unconditional linear algebra on the verified rep"
extends:
  - explorations/f2-cut-relative-entropy-2026-07-20.md
  - explorations/intake-bianconi-entropic-gravity-2026-07-20.md
inputs:
  - explorations/f2-cut-relative-entropy-2026-07-20.md
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
  - explorations/f5-signed-fraction-2026-07-20.md
  - lab/sources/claim-mining-toe-bianconi-2026-07-20.md
  - tests/channel-swings/f2_shadow_two_section_probe.py
  - tests/channel-swings/f2_cut_relative_entropy_probe.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/araki_cut_entropy_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# The Araki retry, and the two paper questions

Three bounded questions from the Bianconi mining report, answered. Receipt
for the computational leg: `tests/channel-swings/araki_cut_entropy_probe.py`,
deterministic (double-run byte-identical), numpy only, seeded 20260720,
exit 0 -- HEADLINE `12 [E] + 3 [F] = 15 (setup [T] = 4 excluded) ALL PASS`.

Pre-declared kill conditions (filed in the dispatch before the probe ran):
K-a divergent/ill-defined on the pair; K-b finite but identically zero or
holonomy-even; K-c finite, nonzero, holonomy-odd but scale-free; K-d finite,
nonzero, holonomy-odd, scale-bearing. **What fired: K-a for every direct
pairing of the two cuts, and K-b -- structurally, by an exact symmetry, not
numerically -- for every finite covariant retry.** The route is dead at toy
grade with the mechanism named, and the mechanism is worth more than the
functional would have been.

## Q1. Does the measure term carry scale? YES -- and the entropy core is still ratio-only. The two pre-declared readings both hold because they factorize.

**The action** (arXiv:2408.14391, Eq. 38): `S = INT dr sqrt|-g| L` with
`L = Tr g-tilde ln G-tilde^{-1} - Lambda` (Eq. 36), induced metric
`G-tilde = g-tilde + alpha (D|Phi><Phi|D + (m^2 + R)|Phi><Phi|) - beta RIC`
(Eq. 32). The relative-entropy Lagrangian is a trace of a logarithm --
DIMENSIONLESS, and invariant under joint rescaling of the metric pair. The
dimensions live in exactly two places, both external to the entropy:

1. **The couplings:** `alpha = alpha' l_P^d`, `beta = beta' l_P^2` with
   alpha', beta' dimensionless (2408.14391, Sec. on the topological action).
   The Planck length is INSERTED as the unit that makes the induced-metric
   corrections dimensionally consistent.
2. **The measure normalization:** the Yangzhou worked example writes it
   explicitly: `S = l_P^{-4} INT sqrt(-g) L d^4x` (arXiv:2602.13694, Eq. 4).
   A dimensionless Lagrangian against a `d^4x sqrt(-g)` volume element
   FORCES an absolute `l_P^{-4}` in front. This is the honest cash value of
   the spoken remark ([00:12:59], mining row: "the measure plays an
   important term"): the measure factor is where the dimensions -- and the
   Lagrangian-vs-total-entropy split of her second-law claim -- live.

**Worked-example check** (2602.13694): every strong-field coefficient
carries beta, i.e. carries `l_P^2`: `A(r) = 1 - 2M/r - beta M^2/(12 r^4)`,
`B(r) = (1 - 2M/r)^{-1} + beta M^2/(3 r^4)` (Eq. 18), horizon shift
`r_h = r_S + beta/(48 r_S)` (Eq. 20), mass-loss law
`Mdot = beta(-1/24 - 0.17/M^2 + 0.005/M^4)` (Eq. 43) with the constant
entropic leakage `-beta/24`. An ABSOLUTE scale is present in the
observables -- and it is the posited `beta' l_P^2`, not a derived number.
The emergent-Lambda functional is
`Lambda_G = -(1/2 beta) Tr(G - I - log G)` (2602.13694, Eq. 12): the
G-dependence is dimensionless; beta again carries the units.

**Verdict: both horns, factorized.** Her structure is scale-bearing as a
FRAMEWORK (absolute l_P enters through measure normalization and couplings,
and reaches the worked solution's coefficients) while her entropy CORE is
ratio-only exactly like GU's (H24). So (a) the relocation criticism applies
to her too -- l_P and beta' are inputs; the Lambda magnitude is no more
derived there than our B.5 amplitude is here -- which strengthens the
honest PP3 framing; and (b) there IS a mechanism-shape for the B.5
cut-scale slot: **dimensionless native functional x external unit slot
(measure/coupling), a factorized dial.** The scale never comes from the
entropy; it comes from what the entropy is integrated against.

## Q2. Dressed metric: cousin or homonym? HOMONYM at formula level.

**Her dressing** (2408.14391): additive -- `G-tilde = g-tilde + alpha(...)
- beta RIC` (Eq. 32; components Eq. 33); matter EOM couples through the
inverse: `D G-tilde^{-1} D |Phi> + G-tilde^{-1} (m^2 + R)|Phi> = 0`
(Eq. 43). In G-field variables (Eqs. 50-51, v5): the multiplier field
enforces `G-tilde g-tilde^{-1} = Theta-tilde` via
`L = -Tr ln Theta - Tr G(G-tilde g-tilde^{-1} - Theta)`, and on shell the
G-field is the inverse mismatch `G = Theta^{-1}`, so the dressed inverse
metric matter feels is the bare inverse times a generic positive
multiplier factor ([00:24:46]).

**Our object** (f5-signed-fraction doc): `S = K_S e^{alpha w}` -- the
EXACT exponential of the commutant bivector w, a one-parameter hyperbolic
orbit through K_S, parametrized by the symbol's own rapidity
`alpha = artanh sqrt(T/P)`, acting on an INDEFINITE fundamental symmetry,
with positivity of the factor `e^{alpha w} = K_S S` DERIVED, and with the
deck flip realized as the orbit's antipode (S -> -S).

**Comparison, formula against formula.** Shared: only the coarsest shape --
a reference structure multiplied by a positive factor measuring the
mismatch of two metric-like structures, before matter/accounting couples.
Not shared, and each difference load-bearing: (i) additive-generic
correction (linear in field bilinears and curvature) vs exact exponential
orbit -- her dressing has no exponential, no group orbit, no antipode;
(ii) operand: positive-definite metric-as-operator vs Krein fundamental
symmetry; (iii) parameter: dynamical matter/curvature content vs kinematic
rapidity of the frozen symbol; (iv) positivity: ASSUMED (her tensors are
"positively defined" by hypothesis, stated before Eq. 3) vs DERIVED.
**Verdict: homonym.** Both are merely called dressing; the mathematical
operations differ. No fork-table row is opened.

**Bridge datum** (probe [E]): her Lambda_G functional evaluated on our
native positive dressing, `Tr(G - I - ln G)` at `G = e^{alpha w}`, equals
`128 (cosh alpha - 1) = 20.3097` -- finite and positive automatically
(because the dressing's positivity is derived), but w-even and scale-free:
transplanted onto the native pair, her own functional lands in the
sector-blind even channel. The homonym verdict and the Q3 theorem agree.

## Q3. The Araki retry: K-a + K-b, with the mechanism named

**The definition, stated precisely** (probe docstring, machine-checked):
for positive trace-one rho, sigma on finite-dimensional H with M = B(H)
(type-I factor), GNS = Hilbert-Schmidt space, `xi_rho = rho^{1/2}`,
relative modular operator `Delta_{sigma|rho} X = sigma X rho^{-1}`, and

    S(rho||sigma) = -<xi_rho, ln Delta_{sigma|rho} xi_rho>
                  =  Tr rho (ln rho - ln sigma)   if supp rho <= supp sigma,
                  =  +infinity                    otherwise.

At type I, Araki IS Umegaki-with-the-support-law. The probe implements the
modular form independently and matches Umegaki at 1e-10 on a seeded
faithful pair; the support law is verified QUANTITATIVELY (the regularized
value diverges with slope = violating mass x ln(1/eps), matched to 0.5%).
What the modular formulation buys in QFT is type-III/same-folium
finiteness (Dorau & Much, arXiv:2510.24491, Eq. 8: coherent displacements
of the vacuum on horizon algebras -- footnote 2 notes finiteness is of
that setting); it does NOT repair a genuine support violation, and it
assigns +infinity to distinct pure states. The b895d95 disease was
purity/support, not UV -- so the "Araki cures it" hope was miscast from
the start, and the honest retry is: correct supports plus NATIVE faithful
states the naive run lacked.

**What the retry found, in order:**

1. **K-a for every direct pairing.** The Hilbertized projector states
   (violating masses 0.745 both directions) and the native K_S-TWISTED cut
   states `M_sigma = sigma K_S Q_sigma = Q_sigma^+ K_S Q_sigma` (Hermitian
   PSD rank 64, positivity from K-definiteness of the cut ranges --
   derived, not assumed; `Tr M_+ = 64 cosh alpha = 74.1549`) both have
   mutually violating supports: Araki = +infinity in both directions. The
   twist fixes positivity, not mutual support.
2. **Finiteness is achievable natively.** Against the faithful derived
   reference `gamma = e^{alpha w}/Z`, both twisted states have finite
   entropy: `S(rho_sigma||gamma) = 0.5595142229` for BOTH sigma. Equal to
   1.5e-15: **the deck-odd difference is identically zero (K-b).**
3. **The mechanism, machine-exact.** The unit mixed involution w conjugates
   `Q_+ <-> Q_-`, `M_+ <-> M_-`, sends `K_S -> -K_S`, and FIXES gamma and
   the C2 density A (defects 8e-16 or better). And the swap group is
   LARGER than w: the out-of-plane mixed bivector `V = c_m c_tau` (m a
   spatial unit vector K-orthogonal to xi_s, tau a timelike unit vector
   K-orthogonal to xi_t) is a Hermitian unitary involution that commutes
   with u, w, AND D ITSELF, anticommutes with K_S, swaps the cuts, and
   fixes even the w-broken reference `e^{alpha w + 0.3 u}` (whose deck-odd
   difference is duly 1.7e-15). Consequence, at theorem strength for this
   toy: **the sector datum is stored ONLY in the relative sign between K_S
   and the cut. Positivity forces any state-valued K_S-twist to absorb
   that sign into the sector label (sigma K_S Q_sigma), so every
   Araki-form functional of the pair -- normalized or Lindblad-weighted,
   any K_S-even reference -- is swap-symmetric, and its deck-odd part
   vanishes identically.** Entropy is K_S-even; the sector is K_S-odd.
4. **The Bianconi-mirror variant dies the same way.** The unnormalized
   Lindblad form with the C2 density as measure-like weight
   (`C_sigma = A^{1/2} rho_sigma A^{1/2}` vs reference A) is finite both
   directions (23133.986593 each) and exactly degree-2 homogeneous under
   `xi -> lambda xi` -- it would have carried the symbol's normalization,
   k_sigma-style -- but w fixes A, so its odd part is also identically
   zero. A dial location with no lever on it.
5. **The only nonzero escape collapses to the linear channel.** A
   K_S-LINEAR reference term (`gamma_K ~ e^{alpha w + eps K_S}`, eps
   inserted by hand) gives a nonzero difference -- but EXACTLY
   `F = -2 eps sech(alpha) = -eps [Tr rho_+ K_S - Tr rho_- K_S]`: the
   Gibbs reference linearizes the relative entropy in its exponent, and
   the value is the K_S-linear odd moment `Tr rho_sigma K_S = sigma
   sech(alpha)` (the F5 definiteness margin, reappearing as the odd
   moment) times the hand coefficient. The entropic wrapper contributes
   nothing beyond a k_sigma-type linear pairing; eps is a dial someone
   turned, not a derived scale; the value is scale-free.
6. **Holonomy-oddness was never the problem.** Seam covariance holds
   machine-exactly (`gamma(1) = U_h gamma(0) U_h^{-1}`,
   `rho_+(1) = U_h rho_-(0) U_h^{-1}`), so every covariant functional
   satisfies F(1) = -F(0) by unitary invariance. The odd functional
   exists; its value is forced to be 0.

**Which kill fired: K-a + K-b.** Not K-c (the finite candidates are zero,
not merely scale-free); not K-d. **The entropic route between the two cuts
is dead at toy grade,** and the named negative is stronger than the sum of
its runs: it is an even/odd selection rule. The defense-attorney pass
(single-construction kill discipline): the kill is local to Araki-form
(positive, state-valued) functionals of THIS pair at symbol grade; the
reframe that explains more, rather than less, is the selection rule
itself -- it unifies the b895d95 Umegaki negative, the F5
magnitude-blindness (master identity: K_S-even part of A is pure scalar),
the Kramers evenness of J-commuting probes, and this result under one
statement: **every even channel is blind to the sector; the K_S-linear
signed channel k_sigma is the reader, and it already exists.** Exhaustion
as pre-declared: naive pair, twisted pair, twisted-vs-faithful-reference,
A-weighted unnormalized, and symmetry-broken references were all run; the
symmetric ones vanish by the exhibited involutions, the broken one reduces
provably to the linear channel.

## Council pass (inline, five lenses)

- **Modular-theory specialist (is the finite-dim specialization honest?):**
  Yes. Type I has no type-III subtleties to fake: Araki = Umegaki + the
  support law, and both legs were verified against an independent modular
  implementation (1e-10) with the divergence slope matching the violating
  mass to 0.5%. The one thing the modular formulation genuinely adds in
  QFT -- same-folium finiteness on type-III algebras (the Leipzig paper's
  coherent states) -- was named and explicitly NOT imported as a cure,
  because the toy disease (mutual support violation of rank-64 subspaces)
  is exactly what modular theory does not and should not cure.
- **Krein analyst (positivity adaptations):** every place her formalism
  had to be adapted is named: (i) her tensors are positive by hypothesis
  ("assuming T-hat positively defined", before Eq. 3 of 2408.14391); the
  native cuts are oblique Krein projectors, so the ln is undefined --
  adaptation: use only the two DERIVED positive objects,
  `e^{alpha w} = K_S S` and `M_sigma = sigma K_S Q_sigma`; (ii) her
  `Tr ln = ln det` identity (mining trap T1) breaks on indefinite
  pairings -- adaptation: all logs taken on supports of Hermitian PSD
  operators only. The bitter finding is that these adaptations are not
  incidental: forcing positivity is exactly what erases the sector, since
  the datum IS a relative sign. The two forks both computed as required:
  the standard fork (Hilbertized states) dies of support; the native fork
  dies of evenness.
- **Cosmologist (worked-example scale check):** the Yangzhou coefficients
  settle Q1 empirically for the framework: `-beta M^2/12 r^4`,
  `beta/48 r_S`, leakage `-beta/24` -- an absolute scale reaches the
  observables, and it is `beta' l_P^2` all the way down: posited unit,
  dimensionless entropic structure. Her program now has a strong-field
  prediction surface (a second group's stress test), but the DE amplitude
  is exactly as relocated as ours: the honest comparator statement for
  PP3 is "her Lambda is a relocation with a mechanism; our B.5 is a slot
  with a carrier; neither derives a magnitude."
- **GU-native geometer (what the B.5 slot actually needs):** the slot
  needs a lever and a value. This swing proves the entropy dress-up
  provides neither on the cut pair: the lever (deck-odd part) is
  symmetry-killed, and the would-be value was always going to be
  homogeneous, not absolute. What survives for B.5 is the factorized
  Bianconi shape: dimensionless native functional x external unit -- and
  the native functional that actually reads the sector is already k_sigma
  (degree-2 homogeneous, exact closed form). So the scale hunt belongs
  where the dossier filed it: the measure/normalization leg of the actual
  N2 family (the M2 lambda_0 dial), not in entropies of the cut pair.
- **Adversarial referee (attack any positive result as an artifact of the
  K_S-twisted state choice -- in writing):** there is no positive result
  to attack; the referee instead attacks the negative and the near-miss.
  (i) The twisted-state CHOICE is indeed attackable -- but the vanishing
  is choice-robust: positivity forces ANY covariant state construction to
  absorb the K_S sign into the sector label, and the exhibited swap
  involutions (w, V, and their products -- V even commutes with D) then
  kill the odd part regardless of which positive normalization was
  picked. (ii) The one nonzero value (-2 eps sech alpha) is conceded in
  advance to be an artifact in the precise sense charged: it is
  proportional to a hand-inserted breaker coefficient and identically
  equal to a linear moment -- publishing it as "entropy reads the sector"
  would be false advertising for k_sigma. (iii) Remaining evasion the
  probe does NOT close: antiunitary (J_quat-composed) functionals and
  non-state sesquilinear "weights" are outside the Araki class tested;
  named as residue, not as hope -- any such object gives up positivity,
  which was the entire selling point of the entropic route.

## Receipts

- Probe: `tests/channel-swings/araki_cut_entropy_probe.py` -- HEADLINE
  `12 [E] + 3 [F] = 15 (setup [T] = 4 excluded) ALL PASS`, exit 0,
  deterministic (two runs byte-identical), numpy only, seeded 20260720.
- Anchors reproduced in-probe: q(xi) = 30.13; alpha = 0.556134;
  `S = K_S e^{alpha w}` at 8.9e-16; `Tr A = C2^2 = 24137.51`;
  `k_sigma = sigma 14421.0033` (F5 functional, zero-sum at 0.0e+00);
  deck exchange at the seam 6.7e-16.
- Sources (fetched 2026-07-20, arXiv HTML renderings): 2408.14391
  (Eqs. 3, 6-7, 32-38, 43, 50-51; the v3/v5 HTML truncates Sec. III.5, so
  the on-shell G-field reading combines Eqs. 50-51 with the spoken
  three-term account [00:24:46] -- flagged, not load-bearing for the
  homonym verdict, which rests on Eq. 32/43 vs the F5 closed form);
  2602.13694 (Eqs. 4, 12, 18, 20, 43, 45); 2510.24491 (Eq. 8 +
  footnote 2). Timestamped rows from
  `lab/sources/claim-mining-toe-bianconi-2026-07-20.md` ([00:12:59],
  [00:18:18], [00:24:46]).
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` -- both forks
  computed for the states (Hilbertized standard vs K_S-twisted native);
  every load-bearing positive object's positivity derived, never assumed;
  imported mathematics (finite type-I modular theory) named and verified.

## Boundary

Exploration tier; no claim-status, canon, scorecard, or posture movement;
no external actions; no edits to existing files; nothing committed. Toy
grade throughout: one loop, the symbol family, the frozen xi -- the
selection rule is machine-exact here and its general-(p,q)/loop-family
statement is a short named computation, not done; nothing touches the N2
boundary family, S_IG, N1/N3, or the bit's value (p2c-owned). The
Q1/Q2 answers are read off arXiv HTML renderings with one flagged
truncation (Sec. III.5 of 2408.14391); equation numbers may shift between
arXiv versions. Named residues: (i) antiunitary/weight-functional evasion
of the selection rule (outside the Araki class, would surrender
positivity); (ii) the swap group was exhibited by two generators, not
classified; (iii) the factorized-dial reading of B.5 Element 2 (native
homogeneous functional x external unit, with k_sigma as the functional)
is a framing, not a construction -- its construction lives at M2/N2 where
the dossier already filed it.
