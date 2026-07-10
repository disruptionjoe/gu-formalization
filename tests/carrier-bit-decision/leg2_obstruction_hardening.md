# LEG-2: Obstruction hardening — exact re-verification + the nilpotent-extension dichotomy

Script: `LEG-2-obstruction-hardening.py` (this directory). 46/46 checks PASS, exit 0, ~75 s,
single process, python/numpy/sympy, exact arithmetic (Fraction-coefficient sparse Clifford algebra
grounded entry-for-entry against the repo's own Jordan-Wigner Cl(9,5) rep; mod-p ranks at 3 primes
p = 1 mod 4 with exact upper bounds so every quoted rank is EXACT unless labeled otherwise).

## 0. What was re-verified (the original machine fact)

Source: `tests/rs_gu_phys_brst_specification.py` (deps `tests/oq_rk1_cl95_explicit_rep.py`,
`tests/rs_clifford_projector_model.py`), rerun in-process this session, exit 0:

> `Cl(4,0) toy : RS symbol on pure-gauge image norm = 73.48  -> annihilated? False`
> `Cl(9,5) anc : RS symbol on pure-gauge image norm = 343.73  -> annihilated? False`

(Full-precision floats from the module dicts: 73.484692283, 343.730237057.) The canon reading being
hardened (`explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md` section 3, verbatim):

> "Both confirm: `im(d_A)` escapes `ker(Gamma)`. Therefore the physical RS space is NOT a naive
> subtraction (that easy case is rigorously ruled out), and **some nontrivial gauge-fixing
> apparatus is required** (the naive quotient is obstructed; the machine fact rules out the easy
> subtraction but does not prove a ghost complex is the *unique* resolution)"

Note the PS exit-255 artifact named in the design does not reproduce under bash: the repo script
exits 0 cleanly.

## 1. Exactification (the 343.73 is now a derived number)

**Theorem 1 (closed form; polynomial identity in xi).** With Gamma the algebraic gamma-trace on
T (x) S^+, P_+/P_- the constraint projectors (Hermitian = metric adjoint because e_a^dag = eta_a
e_a — verified exactly, all 14 generators; the repo's `inv(gram)` is exactly `I/14` because
Gamma Gamma^dag = n E_- exactly), g(xi): eps -> xi (x) eps the gauge symbol, and
sigma_Q(xi) = P_-(1 (x) c(xi))P_+ the constrained RS symbol:

    sigma_Q(xi) . P_+ . g(xi)  =  ((n-2)/n) * P_-( xi (x) c(xi) . )
    slotwise:  ((n-2)/n) [ xi_a c(xi) - (q_eta(xi)/n) eta_a e_a ] E_+

Certified as a POLYNOMIAL IDENTITY over Q (both sides are matrix-valued quadratic forms in xi;
verified exactly at all e_i and e_i+e_j — 105 points on the Cl(9,5) anchor, 10 on the Cl(4,0)
toy). It holds in ANY signature, including on the null cone. The identity never divides by q.

- Anchor: 343.730237...^2 * 10^4 = **405256132224/343** exactly (denominator 7^3; the (6/7) is
  the n=14 Weitzenboeck-family factor). Composite rank = **64 = full** (exact: mod-p x3 + upper
  bound rank <= rank E_+ = 64 with tr E_+ = 64 exact) at the original xi and two random integer xi
  with q_eta != 0. The obstruction is an ISOMORPHISM onto its image, not a one-xi accident.
- Toy (its own coefficient derived honestly, (n-2)/n|_{n=4} = **1/2**; internal F = C^16 multiplies
  norm^2 by 16): 73.484692...^2 = 16 * (675/2) = **5400 exactly**. The design's LEG-1 risk
  ("toy wiring differs, might not match") CLOSED: same closed form, honest per-model coefficient.
- P_+ Gamma^dag = 0 exact; P_+, P_- idempotent with trace 832 exact (so rank P_+ = 832 exact).

## 2. TEST A — no consistent gauging on the CONSTRAINED field space (carrier B's)

**Theorem 2 (ellipticity, exactified).** At xi with q_eta(xi) != 0 (verified at the original point,
q = 3013 exact): rank(sigma_Q) = **832 = dim ker Gamma** exactly (mod-p x3 lower + rank <= rank
P_+ = 832 upper). So sigma_Q: ker Gamma -> ker Gamma' is a bijection.

**Theorem 3 (pointwise no-go — UNCONDITIONAL).** Corollary of Theorem 2 by two lines of linear
algebra: for ANY linear ghost map h: Xi -> ker Gamma (ANY parameter space Xi — spinor, opposite
chirality, or S_{3/2}-valued "gauging upstairs" shadows; ANY xi-dependence/pseudodifferential
dressing; NO equivariance hypothesis), sigma_Q . h = 0 forces h = 0. No nonzero nilpotent
extension of any gauge variation exists on the constrained field space off the null cone.
This SUBSUMES the design's LEG-2 Schur plan: the equivariance conditionality (design risk 2)
DISSOLVES — Schur/character arithmetic is not needed for the no-go, and the design's expectation
that a non-equivariant counterexample search "SHOULD find solutions" is REFUTED off-cone: every
solution annihilates the ghost map. The canonical candidate h = P_+ g is itself nonzero (rank 64,
||P_+ g||^2 = 2112032/7 exact) and lands in ker Gamma exactly (Gamma(P_+ g) = 0 exact); what fails
is nilpotency, by exactly the ((n-2)/n)-isomorphism of Theorem 1.

**Bonus (why Theorem 2 holds).** Exact block identity at xi0:
sigma'_Q sigma_Q = q Id - (4/n) xi_a tau + (4/n^2) eta_a e_a c(xi) tau on ker Gamma
(tau = Sigma_b eta_b xi_b psi_b) — on the 768-dim tau = 0 subspace the composite is q*Id exactly.

**Escape flag (DEAD-ENDS compliance).** The only "solutions" to sigma_Q h = 0 are h = 0 =
annihilated gauge action — the decoupling shape. `absorbed/gu-source-action/DEAD-ENDS.md`
(verbatim): "Any construction that drives the **bare** `||[Pi_RS, M_D]||` (58.72) to 0 — that
decouples the RS sector and reinstates Velo-Zwanziger acausality." Flagged, never adopted. No
mass operator appears anywhere in this leg; nothing bare or dressed is moved. Also per DEAD-ENDS:
"the 'obstruction = a specific commutator number (343.73)' — FALSE (different object)" — this leg
makes no shiab claims; 343.73 is treated only as the gauge-image composite it is.

**Degraded-EOM escape (named).** Replacing sigma_Q on ker Gamma by an operator with kernel
containing im(h) sacrifices ellipticity (rank < 832) — no index, not carrier B. So on the
constrained space the choice is exact: elliptic operator (carrier B) XOR gauge orbit. Not both.

## 3. TEST B — the BRST rescue EXISTS on the FULL field space (carrier A's)

With R(xi) the first-order gamma^{abc} RS symbol and g' the (Euclidean-contraction) antighost
symbol: **R.g == 0 and g'.R == 0 IDENTICALLY in xi** (105-point polynomial certificates — pure
antisymmetry, no constraint needed, valid ON the null cone too), and at q_eta != 0 the 4-term
complex 0 -> S^+ -g-> T(x)S^+ -R-> T(x)S^- -g'-> S^- -> 0 is EXACT: rank g = 64 (Gram = |xi|^2 E_+
exact), rank R = 832 (mod-p x3 + exact upper bound via ker >= T(x)S^- + im g), rank g' = 64
(Gram exact), inclusions + dimension counts exact. Carrier A's mechanism (gauge variation +
nilpotent ghost extension + elliptic gauge-fixed complex) EXISTS in the finite model — on the
full, unconstrained field space. Euler-class SHAPE = ghost-subtracted (T-1)-twist. Per the
anti-story-shopping discipline the index roll-up (-42 vs -44) is NOT computed here — that is
LEG-3's machine-decided job.

## 4. The dichotomy (the leg's headline)

The same symbol data supports EXACTLY ONE of the two structures, and which one is selected by a
single off-symbol datum:

- Field space = ker Gamma (gamma-trace DEFINITIONAL) => sigma_Q elliptic, NO gauge symmetry can
  be BRST-implemented (Theorems 2-3) => carrier B's bookkeeping (T_C + 1C) is the only coherent
  one on that space.
- Field space = full T (x) S^+ (gamma-trace a gauge SLICE) => the exact BRST complex exists,
  ghost subtraction is available and its class shape is (T-1) => carrier A.
- The full-space complex does NOT descend along P_+: the descent failure IS the exact
  ((n-2)/n)-isomorphism. 343.73 is the MUTUAL-EXCLUSION certificate between the carriers, not
  evidence against either.

So the finite model separates "BRST rescues" from "no consistent gauging" SHARPLY — as a
field-space dichotomy — and simultaneously proves the choice between them is not a symbol-level
fact. The carrier bit is exactly SG4: which field space the unbuilt source action declares. GU's
transcript-tier language cuts both ways and stays off-symbol: "R = ker Gamma" as definitional
irreducibility (canon spec C2: "gamma^a psi_a = 0 is GU's DEFINITIONAL irreducibility constraint
R = ker Gamma, NOT a slice") vs the supergravity reading of the same words as a gauge-fixed
description (design steelman (i)).

## 5. Null-cone hole — exact witnesses BOTH ways (story-shopping guard)

At q_eta(xi) = 0 (xi = e_0 + e_9): c(xi)^2 = 0 exactly; with N = 1 + e_0 e_9 (N^2 = 2N,
[N, omega] = 0, (N/2)E_+ idempotent of trace 32) the obstruction composite drops to rank **32
EXACT**; and sigma_Q acquires the exact kernel vector psi = xi (x) c(xi)u — so a NONZERO
characteristic-supported ghost map (sigma_Q h = 0, h != 0) EXISTS on the cone. This is a real,
certified carrier-A-flavored crack in the constrained no-go: a gauging supported on the
characteristic variety is not excluded (it is the finite shadow of the VZ characteristic locus).
Symmetrically, full-space exactness also degenerates there (rank R: mod-p 480 < 832, 3 primes
agree — measured/lower-bound grade). Riemannian K3 has no real null cone (q > 0), so carrier B's
ellipticity certificate on K3 (adjudication LEG-A; Homma-Semmelmann/Baer-Mazzeo) is untouched.

## 6. What rides off-symbol (NOT settled by this leg)

1. WHICH field space the source action declares — the bit itself (SG4; eq 10.10 author-disclaimed
   "Caveat Emptor"; receipt verdict: the manuscript "does not emit a source action, operator,
   differential, Noether identity, or BRST rule" — repo-relayed, canon spec :92-97).
2. BV master-equation / curvature obstructions on Y14 ((S,S) != 0, BICOMPLEX-01) — my complex is
   principal-symbol-level on a fixed fiber.
3. Interacting-level consistency: Grisaru-Pendleton / Velo-Zwanziger / Deser-Waldron are
   S-matrix/PDE statements; nothing here matches their hypotheses (LEG-4's job).
4. The Y14<->K3 bridge and the Lorentzian<->Riemannian bridge (the dichotomy is proven on the
   (9,5) fiber; its transport to the Riemannian generation arena is program semantics).
5. Nonlinear/field-dependent gauge structure (my ghost maps are linear in fields).
6. The index roll-up (-42 vs -44 for the 4-term resolution) — LEG-3.

## 7. Strongest surviving carrier-A case (after this leg — STRENGTHENED)

This leg PROVES carrier A's mechanism is available in the finite model (Test B): nothing in the
343.73 record refutes A. The strongest A-case now reads: (i) GU's "R = ker Gamma" may describe
gauge-fixed solution content, not the off-shell field space — the supergravity reading of
identical words; a stabilization of eq 10.10 on the full vector-spinor space forces A with its
published bookkeeping (Bilal 11.47, HS Remark 3.6), and the machine-verified BRST complex of Test
B is exactly the structure it would quantize with; the draft's own subtraction-shaped language
("elliptic deformation complex after redundant EL equations are discarded", p.65, repo-relayed)
leans this way. (ii) The graded-IG odd invariance upstairs (tau+-twist shape eps -> D_aleph eps,
repo-tagged gu_derived) would live on the FULL space where Test B says BRST works — no spacetime
SUSY needed. (iii) The null-cone crack is exact: characteristic-supported gauging on the (9,5)
substrate is NOT excluded, and GU's signature commitments live on the mixed-signature side.
(iv) A massive/super-Higgsed gravitino keeps its local invariance and ghosts; the carrier's
vectorlike mass-admitting Krein structure is compatible with A. What A can NO LONGER claim: a
BRST rescue ON the constrained field space off the cone (Theorem 3 kills every linear version,
equivariant or not) — A now NEEDS the full field space (or the cone, or nonlinear/off-symbol
structure) as a matter of exact theorem.

## 8. Grades and honesty ledger

- Theorem 1: EXACT, polynomial-identity grade (both models, any signature).
- Theorems 2-3: EXACT at the certified points (original xi0, q = 3013; rank certificates
  mod-p x3 + exact upper bounds), pointwise statements; generic xi by the same certificates'
  semicontinuity, NOT re-certified per-xi.
- Test B exactness: EXACT at xi0; nilpotency identities: polynomial grade (all xi).
- Null-cone: composite rank 32 EXACT; sigma_Q kernel witness EXACT; rank(R) = 480 on cone:
  measured (mod-p, 3 primes) = lower-bound grade only.
- The dichotomy's bearing on the generation arena rides the off-symbol items in section 6.
- No fabrication: every check is an assert in the script; a FAIL aborts with nonzero exit.
