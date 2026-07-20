---
title: "F5 signed fraction DERIVED: the canonical Krein cut is S = K_S e^{alpha w} (K_S boosted by xi's rapidity), and k_sigma = sigma (C2^2/2)[cosh a + tanh(2a) sinh(a)/13] — exact algebraic value (435616/35) sqrt(4045/3013) = 14421.0033 at the frozen XI, fraction 0.5975 = one point on a universal curve with floor 1/2, domain exactly {spacelike xi}, and only a 1/(n-1)-weighted sliver of genuine bivector coupling"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (five-path fan-out: F5 signed fraction)"
axiom: "none consumed for the algebra (unconditional Clifford/Krein linear algebra on the verified rep); the SECTOR reading of the cut inherits lab/process/boundary-adapter-standing-axiom.md exactly as in the parent F5 shadow"
extends:
  - explorations/master-identity-mechanism-2026-07-20.md
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
inputs:
  - explorations/master-identity-mechanism-2026-07-20.md
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
  - tests/channel-swings/master_identity_mechanism_probe.py
  - tests/channel-swings/f5_shadow_c2_flip_probe.py
  - tests/channel-swings/sig_b5_habitat_probe.py
  - tests/generation-sector/gen_sector_bridge.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/f5_signed_fraction_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# The signed fraction, derived

The master-identity swing left one named leftover: the F5 shadow's signed
accounting k_sigma = sigma x 14421.0033 (|k|/C2^2 = 0.5975) had to be a
functional of the mixed bivector B against the canonical Krein cut —
"derivable now in principle, not derived here." It is now derived, at paper
grade, and the derivation delivers more than the number: a closed form for
the canonical cut itself, the exact algebraic value of the fraction, its
full scope in xi, its cut-dependence class, and a quantified verdict on the
adversarial worry ("is the 60% just bookkeeping?") that the F5 doc filed.

Receipt: `tests/channel-swings/f5_signed_fraction_probe.py`, deterministic,
numpy only, seeded 20260720, exit 0 — HEADLINE
`9 [E] + 4 [F] = 13 (setup [T] = 2 excluded) ALL PASS`. Worst residual in
the derivation chain: 1e-12 relative (most steps at 1e-15).

Notation (all from the master-identity doc): verified Cl(9,5) gammas e_a,
eta = diag(+1 x9, -1 x5), n = 14, DIM = 128, xi real, D = c(xi),
X = Gamma M_D Pi_RS, A = X X^+ = (26/7)|xi|^2_E I - (2/7) B with
B = xi ^ (eta xi), K_S = e_0...e_8. New: split xi = xi_s + xi_t
(space/time), P = |xi_s|^2, T = |xi_t|^2, s = P + T = |xi|^2_E,
q = P - T = <xi,xi>_eta; c_s = c(xi_s), c_t = c(xi_t);
w = c_s c_t / sqrt(PT), the UNIT MIXED INVOLUTION of xi's own plane pair
(w^2 = I, B = -2 sqrt(PT) w, K_S w = -w K_S); and

    alpha = artanh( sqrt(T/P) )  —  the RAPIDITY of xi with respect to
    the space/time split that K_S defines.  (Frozen XI: alpha = 0.556134.)

## The derivation

**Step 1 (the commutant of D is a Klein four-group).** Set u = c_s/sqrt(P),
v = c_t/sqrt(T), so u^2 = I, v^2 = -I, uv = -vu = w, and K_S commutes with
u, anticommutes with v and w. Then Ku := K_S u COMMUTES with D (machine:
5.5e-16), and inside the 8-dim algebra spanned by {1, u, v, w} x {1, K_S}
the commutant of D is exactly

    span{ I, d, Ku, E^ },     d = D/sqrt(q),   E^ = d Ku,

a commuting Klein four-group of involutions (d^2 = Ku^2 = E^2 = I,
d Ku = E^), with the closed forms

    E^ = K_S (sqrt(P) I + sqrt(T) w) / sqrt(q)
       = K_S (2P I - B) / (2 sqrt(Pq))
       = K_S e^{alpha w}.

The joint (d, Ku) eigenspaces are four 32-dim sectors — exactly the
(32,32) Gram signature the F2 probe measured.

**Step 2 (the canonical cut IS E^).** The compressed Krein Gram on the
D-eigenspaces E_+-(D) collapses into the same algebra:

    ch_+- K_S ch_+- = (sqrt(P/q)/2)(E^ +- Ku) = +- sqrt(P/q) Ku  on E_+-,

(machine: 1.5e-16). So the Gram-sign splitting the F2/F5 construction
performs inside each eigenspace is precisely the Ku eigensplitting: the
K-positive parts are {d=+1, Ku=+1} and {d=-1, Ku=-1}, i.e.
V_+ = {E^ = +1}, V_- = {E^ = -1}, and the canonical fundamental symmetry is

    S = Q_+ - Q_- = E^ = K_S e^{alpha w}.

Machine: the probe-built cut equals (I +- E^)/2 to 1.3e-15. Positivity is
DERIVED, not assumed: K_S S = e^{alpha w} > 0 with spectrum {e^{-a}, e^{+a}}
— which also identifies the F2 probe's "definiteness margin" as
sech(alpha) = sqrt(q/P) (frozen XI: 0.8631; the loop's reported >= 0.84 is
this quantity along the loop). Uniqueness: an admissible S in the
commutant takes values +-1 on the four sectors, and K_S is positive on
sectors with epsilon_d epsilon_Ku = +1, negative on the others (Step 2's
Gram signs), so K_S S > 0 forces S = E^ — the canonical cut is the UNIQUE
Krein cut whose symmetry lies in alg{D, K_S}.

**Step 3 (the functional).** k_sigma = Re tr(X^+ K_S Q_sigma X) =
Re tr(K_S Q_sigma A); tr(K_S A) = 0 (master identity) leaves
k_sigma = (sigma/2) tr(K_S S A) = (sigma/2) tr(e^{alpha w} A). With
A = (4(n-1)/n) s I + (8/n) sqrt(PT) w, only the scalar-scalar and w-w
terms survive the trace (w is traceless), giving the closed form

    k_sigma = sigma (2 DIM / n) sqrt(P/q) [ (n-1) s + 2T ]
            = sigma (128/7) sqrt(P/q) (13 P + 15 T)                (n = 14)
            = sigma (C2^2 / 2) [ cosh(alpha) + tanh(2 alpha) sinh(alpha)/13 ],

and the fraction (using C2^2 = (3328/7) s):

    f := k_+ / C2^2 = (13 + 15 rho) / ( 26 (1 + rho) sqrt(1 - rho) ),
    rho = T/P in [0, 1)
        = (1/2)[ cosh(alpha) + tanh(2 alpha) sinh(alpha) / (n-1) ].

Machine agreement with the canonical-cut readout: 1e-12 relative, for the
frozen XI and every seeded spacelike draw.

**Exact value at the frozen XI.** P = 809/20, T = 258/25, q = 3013/100
(exact decimals of gen_sector_bridge.XI):

    k_+ = (435616/35) sqrt(4045/3013) = 14421.0032799...
    f   = (68065/132002) sqrt(4045/3013) = 0.5974520211...

The F5 shadow's 14421.0033 and 0.5975 are exact ALGEBRAIC (irrational —
4045 x 3013 = 5·809·23·131 is not a square) numbers, derived, not
measured. Machine match: 1e-11 relative (the residue is the
binary-vs-decimal representation of XI's entries).

## The corrected shape, and the decomposition

The expected shape going in — "the scalar part cancels in the signed
difference and everything is carried by B against the cut" — is WRONG in
detail and the correction is load-bearing. The scalar channel cancels only
in the zero SUM k_+ + k_- = 0; per-sector it survives, because the tilted
canonical cut has tr(K_S Q_sigma) = sigma 64 cosh(alpha) != 0. Exactly:

    k_+ = (26/7) s tr(K_S Q_+)  -  (2/7) tr(K_S Q_+ B)
        = (C2^2/2) cosh(alpha)  +  (256/7) sqrt(PT) sinh(alpha)
        =      13983.70         +          437.30        (frozen XI)
    f   =       0.5793          +          0.0181  =  0.5975.

Three layers, each with a name:

1. **1/2 — the universal floor.** Any Krein-definite half of a pure-scalar
   density reads half the trace. The naive K_S eigencut (not D-invariant)
   gives exactly f = 1/2 with zero B-coupling ([F] check, 1e-14).
2. **(cosh(alpha) - 1)/2 = 0.0793 — the cut's D-compatibility tilt.** The
   canonical cut is K_S boosted toward xi by rapidity alpha; the boost
   raises the scalar reading by cosh(alpha). This term reads xi ONLY
   through the cut's geometry — it would be present for a pure-scalar
   density.
3. **tanh(2a) sinh(a)/26 = 0.0181 — the B channel.** The only term where
   the cut reads A's non-scalar (mixed-bivector) content. Its weight
   relative to the scalar channel is 1/(n-1) = 1/13 — the ratio of the
   grade-2 to grade-0 contraction coefficients (4/n)/(4(n-1)/n) — verified
   verbatim in Cl(5,3) at n = 8 with weight 1/7 ([F] control).

## Scope: the frozen XI is not special; the domain is exactly {q > 0}

- **Universality on the domain.** The functional holds for every real
  spacelike xi (machine sweep: generic, rho = 0.05, 0.55, 0.98, plus
  scale 1e3); f is scale-invariant and depends only on rho = T/P.
- **Domain boundary is sharp.** For timelike xi (q < 0) the D-eigenspaces
  (eigenvalues +-i sqrt(-q)) are K-NEUTRAL; for null xi (q = 0), D^2 = 0
  and Ker D = Range D is K-neutral (both machine: Gram norm 7e-15). Either
  way no maximal K-definite D-invariant subspace exists: the canonical cut
  — and with it the fraction — is defined EXACTLY on the spacelike cone
  q > 0. (This is a theorem-grade version of the F2 probe's empirical
  "never degenerate along the loop": the loop stays spacelike.)
- **Range [1/2, infinity).** f is strictly increasing in rho, with
  f(0) = 1/2 attained exactly at pure-space xi (where alpha = 0, B = 0,
  and the canonical cut degenerates to the K_S eigencut — machine-exact),
  and f -> infinity at the null cone (the Gram margin sech(alpha) -> 0).
  At rho = 0.98, f = 3.80 > 1: **|k|/C2^2 is NOT a proportion** of the
  obstruction content. The F5 shadow's "resolves ~60% of C2^2" framing is
  retired: k is a rapidity-weighted Krein reading, and it can exceed the
  total trace. The frozen XI's 0.5975 is one point on this curve
  (rho = 1032/4045 = 0.2551), in no way distinguished.

## Cut-dependence: which cut owns the number

- **Zero-sum is cut-generic.** k_+ + k_- = 0 for EVERY Krein splitting
  (master identity corollary) — including the deformed and naive cuts
  below. The relational sign structure needs no cut choice.
- **The magnitude is cut-specific.** A Gram-boosted cut satisfying EVERY
  admissibility property (K-self-adjoint idempotent complementary
  half-rank, D-invariant, K-definite ranges, magnitude-blind, zero-sum)
  reads k = 14680.33 instead of 14421.00 ([F] check, shift +259.33 at
  boost 0.7): the fraction is NOT invariant across the admissible family.
- **The canonical cut is intrinsically pinned.** It is the unique
  admissible cut whose symmetry lies in alg{D, K_S} (algebra residual:
  canonical 3e-15, deformed 0.24). Within the canonical class — the unique
  pair {Q_+, Q_-} and its deck transports — |k| is invariant and only the
  sign moves: transporting the cut around the mixed loop sends S = +E^ to
  -E^ (machine: 1.6e-15), the closed-form version of the F5 shadow's
  holonomy tie. So F5's operational form must NAME the cut: "the
  Krein-signed accounting against the canonical (Gram-spectral,
  D-compatible) cut," not "against a Krein cut."

## Geometric meaning

The whole object is one hyperbolic angle. K_S defines a space/time split
of the 14 directions; xi sits at rapidity alpha = artanh(sqrt(T/P)) off
the space subspace, in the plane pair whose unit mixed involution is w.
The canonical cut is K_S BOOSTED toward xi by exactly that rapidity,
S = K_S e^{alpha w}; its definiteness margin is sech(alpha); and the
signed C2 accounting is the boost-weighted trace of the C2 density,
k_sigma = (sigma/2) tr(e^{alpha w} A). The same B that carries A's entire
non-scalar content also generates the cut's tilt — one bivector, two
costumes. The answer to the symplectic lens's question ("is the fraction
an angle between xi's plane and the cut?") is yes, literally: f is a
function of that one angle, and of nothing else.

## Council pass (inline, five lenses, compact)

- **Clifford algebraist:** the calculus is three collapses: the commutant
  of a vector element in alg{c_s, c_t, K_S} is a Klein four-group; the
  compressed Gram lands in it; the trace kills everything but grade-0.
  No Fierz beyond the master identity's two contractions is consumed. The
  1/13 is 1/(n-1), general-n verified — combinatorics, not (9,5) magic.
- **Krein analyst:** the uniqueness argument is the honest core: maximal
  K-definite D-invariant subspaces are NOT unique (graph deformations
  survive every admissibility test and move |k| by O(hundreds)), so the
  number 0.5975 belongs to the Gram-spectral cut specifically, which is
  pinned intrinsically as the unique cut in alg{D, K_S}. Domain finding:
  the canonical cut exists iff xi is spacelike — neutrality of the
  eigenspaces kills q <= 0. Both forks of the cut discipline stay
  computed: the positive-Hilbert (plain spectral) cut still sees no datum.
- **Symplectic/structure theorist:** S = K_S e^{alpha w} says the sector
  boundary condition is a POINT ON A HYPERBOLIC ORBIT of K_S through xi's
  mixed plane. The deck flip is the antipode (alpha w -> alpha w + i pi
  in the involution's sense: S -> -S). The fraction is the moment map of
  the boost: floor 1/2 at the fixed point, divergent at the boundary of
  the domain (null cone). "Margin = sech alpha" makes the F2 probe's
  empirical margin a geometric invariant.
- **Numerical analyst:** exactness discipline held: every symbolic step
  machine-corroborated at 1e-12..1e-16 relative; the headline constants
  are exact rationals times one quadratic surd, checked against machine
  at 1e-11 (binary-decimal representation of XI is the floor); the
  near-null draw (rho = 0.98, margin 0.14) still matches at 3e-15 — the
  formula is not conditioned out near its singularity. Frozen-XI decimals
  in prior docs (14421.0033, 0.5975) are confirmed as roundings of the
  exact surd.
- **Adversarial referee (the F5 doc's own worry, answered):** "is the 60%
  just generic bivector bookkeeping with no sector content?" VERDICT:
  the magnitude is ~97% bookkeeping — 0.5 universal floor + 0.0793 cut
  tilt, both readable off A's SCALAR part — and only 0.0181 (3% of f) is
  genuine bivector-against-cut coupling, weighted 1/(n-1). Anyone
  advertising "the sector resolves 60% of the obstruction" would be
  overclaiming; the honest statement is that the sector datum is the
  SIGN (cut-generic, theorem-forced, holonomy-tied), while the magnitude
  is a derived property of the canonical cut's rapidity with a small,
  exactly-known B sliver. The worry was RIGHT about the number and WRONG
  about the channel: the signed channel's load-bearing content was never
  the 0.5975 — it is the flip, plus, now, the exact functional form that
  any faithful end-model must reproduce.

## What this means for F5's decisive form at N2 grade

The F5 shadow already sharpened the falsifier once (magnitude tests are
theorem-vacuous at symbol grade; the channel is Krein-signed). This
derivation sharpens it again, from "the signed channel responds" to a
QUANTITATIVE fingerprint. A faithful end-model, consuming the sector as
the canonical boundary condition on the obstruction map's output leg,
must reproduce at symbol grade:

1. the sign flip under deck transport (relational; cut-generic;
   necessary but NOT discriminating);
2. the canonical cut itself — S = K_S e^{alpha w}, the unique admissible
   cut in alg{D, K_S}, with margin sech(alpha) — since any other
   admissible cut changes the accounting;
3. the exact functional k_sigma = sigma (C2^2/2)[cosh a +
   tanh(2a) sinh(a)/(n-1)] on the spacelike domain, with the floor 1/2,
   the divergence at the null cone, and the B-weight 1/(n-1).

Deviations now DIAGNOSE: a wrong magnitude with the right sign means a
non-canonical cut (or non-symbol content leaking in); a magnitude test
pinned to "0.5975" as such would be testing the frozen XI, not the
carrier. The decisive F5 test remains an N2-grade computation on the
actual boundary family — unchanged in location — but its symbol-grade
shadow is no longer a measured number: it is a two-parameter-free curve
that the end-model has to hit.

## Typing

- Canonical-cut closed form S = K_S e^{alpha w} (with uniqueness in
  alg{D, K_S}), the signed functional, the exact frozen-XI value, the
  domain statement (q > 0), and the floor/range: **NATIVE-DERIVED (paper
  grade, all real spacelike xi)** — unconditional algebra, each step
  machine-corroborated; general-n form controlled at n = 8.
- The SECTOR reading of the cut (that S is "the sector datum's boundary
  condition"): unchanged, R0_COND under the standing boundary-adapter
  axiom, exactly as in the F5 shadow.
- The F5 shadow's numbers 14421.0033 and 0.5975: upgraded from
  NATIVE-PROVEN (matrix grade, frozen xi, mechanism open) to
  NATIVE-DERIVED with exact algebraic values; its "resolves ~60% of the
  obstruction content" FRAMING is retired (f is not a proportion; it
  exceeds 1 near the null cone).

## Receipts

- Probe (deterministic, numpy only, seeded 20260720, exit 0):
  `tests/channel-swings/f5_signed_fraction_probe.py` — HEADLINE
  `9 [E] + 4 [F] = 13 (setup [T] = 2 excluded) ALL PASS`.
- Anchors reproduced in-probe: bare 58.7215, C2 155.3625; canonical-cut
  construction bit-identical to `tests/channel-swings/
  f5_shadow_c2_flip_probe.py` (whose k_sigma = sigma 14421.0033 is
  reproduced before being derived); K_S conventions as in
  `tests/channel-swings/sig_b5_habitat_probe.py`; closed form of A from
  `tests/channel-swings/master_identity_mechanism_probe.py`.
- No overlap with this morning's `explorations/
  f2-cut-relative-entropy-2026-07-20.md` (b895d95): that bounded an
  entropy functional of the cut pair; this derives the signed-trace
  functional. Its "cuts are not density matrices" observation is
  consistent with (and explained by) K_S S = e^{alpha w}.
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` — all
  load-bearing objects PROGRAM-NATIVE (verified rep, native C2 norm,
  Krein-native canonical cut; the standard positive-Hilbert cut's
  emptiness re-recorded); killed list honored (C2 never an index; no
  positivity assumed — the one positivity statement is derived).

## Boundary

Exploration tier; no claim-status, canon, scorecard, or posture movement;
no cross-owner writes; no external actions. What this does NOT do: it
does not run the N2 test, build S_IG or the actual boundary family, read
the bit's value, or touch the scale element; the sector interpretation
stays conditional on the standing axiom; the general-(p,q) statement
beyond the two checked signatures remains an exposure. Named residue: the
deformed-cut family's k values were shown cut-dependent but not mapped as
a function on the space of admissible cuts (a bounded computation, of
value only if some future construction motivates a non-spectral cut).
