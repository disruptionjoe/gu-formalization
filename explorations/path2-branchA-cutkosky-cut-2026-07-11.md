# Path 2, Branch A -- the Cutkosky / unitarity-cut test of keep-and-grade at one loop

**Status:** exploration-grade. GU-INDEPENDENT (Stelle massive-spin-2 as the concrete example). Blind
branch of the H59 loop-positivity wave. Changes NO claim status; drops no verdict into canon.
Companion test: `tests/W48_path2_A_cutkosky.py` (deterministic, exit 0).

**One-line result:** at one loop the ghost cut is PRESENT and NEGATIVE for a stable Krein-graded
ghost (the optical theorem leaks negative probability, case c); it decouples on the physical
subspace ONLY under a complex-pole / CLOP / fakeon prescription, which is the load-bearing
assumption and which buys unitarity at the price of micro-causality.

---

## 0. Constructions used (fork discipline, GEOMETER-VS-PHYSICS-OBJECTS.md)

Two load-bearing objects have rival constructions here; both named explicitly, neither defaulted.

- **"the ghost."** Construction used: the **wrong-sign-residue pole** in the partial-fraction split
  of the fourth-order (induced `|II|^2` / Stelle) spin-2 propagator. I sit on the **keep-and-grade
  side** (do NOT remove it; the Krein `[P,S]=0` grading is the intended physical-subspace selector).
  I test at the level of the propagator and its cut, which is *grading-agnostic*: the cut arithmetic
  is the same object whether the grading is the GU-native Cartan involution of `so(9,5)` or a generic
  PT `C`-operator. This is deliberate -- Branch A's job is the direct cut test, not the grading
  construction (that is Branch B's object).
- **"unitarity / the cutting rules."** Construction used: **Cutkosky rules + largest-time equation
  (Veltman) in the INDEFINITE (Krein) metric.** The loop forces a split I keep sharp throughout:
  - **(K) Krein pseudo-unitarity** `S^dag eta S = eta` -- the S-matrix is unitary *with respect to
    the indefinite metric* `eta`. This is an algebraic identity (the LTE is just combinatorics of
    theta-functions); it survives to all orders for `eta`-real counterterms.
  - **(P) physical-subspace positivity** `2 Im M = sum_phys |M|^2 >= 0` -- the RHS summed over a
    complete set of POSITIVE-norm asymptotic states. This is the prize, and it is what the loop can
    break.

  The textbook error is to conflate (K) with (P). Tree-level and QM rescues establish (K) and, in
  the absence of a continuum cut, (P) for free. The loop separates them.

**Overall-sign honesty.** The brief writes `1/(p^2(p^2-m2^2)) = (1/m2^2)[1/p^2 - 1/(p^2-m2^2)]`.
Worked out, `(1/m2^2)[1/p^2 - 1/(p^2-m2^2)] = -1/(p^2(p^2-m2^2))` -- the split equals *minus* the
bare product. The overall sign is a convention (fixed by the overall sign of the action / which pole
you call the physical graviton); it has no physics. The physics is entirely the **relative** minus
between the two poles. The companion test asserts the identity in this honest form (check A1).

---

## 1. The computation (Cutting-Rules Specialist)

### 1.1 Propagator split and spectral density
Spin-2 sector: `D(p) = (1/m2^2)[ 1/p^2 - 1/(p^2 - m2^2) ]`. Residues: `+1` at `p^2=0` (healthy
massless graviton), `-1` at `p^2=m2^2` (ghost). The Kallen-Lehmann density is therefore

    rho(s) = (1/m2^2) [ delta(s) - delta(s - m2^2) ].

The massive pole has **negative spectral weight**. In a positive Hilbert space the KL theorem forces
`rho(s) >= 0`; negativity is the unambiguous fingerprint of the indefinite (Krein) metric. Per the
fork table this is a *feature* (the (9,5)/Krein structure), but it is also exactly the object that
makes a cut go negative.

### 1.2 The one-loop bubble and its cuts
Take a physical process: light matter `chi chi -> chi chi` with an `s`-channel graviton exchange
whose propagator is dressed at one loop by the bubble `Pi(s)`, the internal lines being the
higher-derivative graviton (equivalently a scalar Pais-Uhlenbeck field carrying the same split
propagator). Cutkosky gives `2 Im Pi(s)` as a sum over two-particle cuts, each weighted by the
product of the two cut lines' spectral weights:

| cut channel        | weight        | threshold     | sign of disc |
|--------------------|---------------|---------------|--------------|
| graviton+graviton  | (+1)(+1) = +1 | `s > 0`       | **positive** |
| graviton+ghost     | (+1)(-1) = -1 | `s > m2^2`    | **NEGATIVE** |
| ghost+ghost        | (-1)(-1) = +1 | `s > 4 m2^2`  | positive     |

Each channel's contribution is `weight x sqrt(lambda(s,ma^2,mb^2))/s /(16 pi) x theta(s-thr)`. The
test computes these numerically at `s = 2.5 m2^2` (test A5): `gg = +0.0199`, `graviton+ghost =
-0.0119`, `ghost+ghost = 0` (still below its threshold). **In the window `m2^2 < s < 4 m2^2` a
negative discontinuity is unavoidably present in the amplitude.**

### 1.3 The optical-theorem test
Unitarity on the physical subspace requires `2 Im M = sum_phys |M_phys|^2`, RHS `>= 0` because it
is a sum of squared amplitudes over POSITIVE-norm complete states. But Cutkosky (the actual analytic
discontinuity of the diagram) delivers the *signed* sum including the negative graviton+ghost cut.
For the two to agree the negative cut would have to be reproduced by some positive-norm final state
-- impossible. Two exits:

- **Stable ghost, Krein-grade only.** The ghost is an asymptotic state graded by `eta`. Then
  `2 Im M` contains the `-0.0119` piece with no positive-norm origin. Residual `LHS - RHS = -0.0119
  != 0`: **negative probability leaks** (test A6). Case (c). Krein pseudo-unitarity (K) still holds
  -- `S^dag eta S = eta` is fine -- but physical positivity (P) fails. This is the honest bad news:
  the grading by itself does NOT confine the cut.
- **Unstable ghost + prescription.** In Stelle gravity `m2 > 0` always allows decay to two massless
  gravitons (threshold at `s = 0`), so the ghost is a **resonance above threshold, not an asymptotic
  state.** Remove it from the physical sum AND deform its cut off the real axis with a
  complex-conjugate-pole (Lee-Wick), CLOP contour, or Anselmi fakeon average-continuation
  prescription. Then `2 Im M = ` (graviton+graviton + matter cuts) only, residual `= 0` on the
  physical subspace **at one loop** (test A7). Positivity (P) is restored -- but by the prescription,
  not by the grading.

**The prescription is the load-bearing assumption.** Krein/keep-and-grade supplies (K) automatically
and supplies nothing for (P); the contour prescription is a separate, additional input.

---

## 2. Referee's grading (Math-Physics Referee)

| claim | status |
|---|---|
| Split propagator, residues `+1/-1`, `rho` negative at `m2^2` | **PROVEN** (algebra; test A1-A3) |
| Cut weights `+1/-1/+1`; graviton+ghost cut negative in `(m2^2, 4m2^2)` | **PROVEN** (Cutkosky + 2-body phase space; A4-A5) |
| Stable Krein-graded ghost -> optical theorem leaks negative | **PROVEN one-loop** for this cut (A6). This is the standard result, honestly reproduced -- keep-and-grade does NOT save (P) by itself |
| Unstable ghost + prescription -> (P) restored on physical subspace | **ARGUED, one-loop-only.** The residual-zero (A7) is exact given "remove the ghost cut"; that removal is *assumed* to be a consistent contour, established at one loop, **not proven all-orders** |
| Krein pseudo-unitarity (K) survives all orders | **ARGUED** (LTE is an algebraic identity; standard, not re-derived here) |
| Positive physical inner product survives renormalization (Q-pos) | **NOT ESTABLISHED here** -- prescription-dependent; Branch B's object |
| Prescription violates micro-causality (Q-caus) | **ARGUED from known results** (Lee-Wick/fakeon acausality); not independently computed here |

The referee's sharp flag: everything that works is **one-loop and prescription-conditional.** The
word "unitary" is earned only in sense (K); sense (P) is bought with an extra assumption whose
higher-loop uniqueness is unproven.

---

## 3. Adversary (attack the branch's own emerging claim)

The emerging claim is "unstable ghost + prescription rescues (P) at one loop." Two attacks:

1. **No kinematic escape.** Across the *entire* window `m2^2 < s < 4 m2^2` the graviton+ghost cut is
   negative (test A10) -- there is no region of a physical `chi chi -> chi chi` amplitude where the
   ghost cut is simply absent. The rescue is therefore *entirely* carried by the prescription; if the
   prescription is illegitimate, there is no fallback. The claim cannot retreat to "the cut doesn't
   actually appear."
2. **Wrong-sign width / anti-resonance.** The ghost's own self-energy has a wrong-sign imaginary
   part, so the naive resummed pole moves to the "wrong" side / wrong Riemann sheet -- it is an
   anti-resonance, not a garden-variety unstable particle. "Just give it a width" is illegitimate;
   the prescription MUST be the full Lee-Wick complex-conjugate *pair* (or the fakeon
   average-continuation) that is engineered to handle exactly this sign. This sharpens -- does not
   rescue -- the load-bearing assumption: it must be a specific, non-generic contour.

The adversary does not overturn the one-loop conditional pass, but it shows the pass hangs on a
single, non-generic prescription with a known higher-loop weakness.

---

## 4. Cross-check (independent second derivation + known limit)

**(a) Largest-time equation, independently.** The LTE proves perturbative unitarity diagram-by-
diagram: `M + M^dag = sum_cuts (products of Delta_+)`. It is an algebraic identity in the theta-
functions, so it holds in the Krein metric regardless of positivity. What it *equals* is the signed
cut sum -- and the ghost line's `Delta_+` carries negative weight. So the LTE independently
reproduces the specialist's split: **(K) is automatic (the identity holds); (P) requires the ghost
cut to be projected/deformed out.** Two derivations, same conclusion -- the discipline that caught
the `M^2/r^2` bug in the gravity arc is satisfied here.

**(b) Pais-Uhlenbeck / Bender-Mannheim QM limit.** The tree/QM rescue lives in 0+1 dimensions:
there is NO continuum, so no two-particle cut ever opens (test A9, `qm_continuum_cut == 0`). The
Bender-Mannheim PT positivity of the PU oscillator is therefore *silent* about the loop cut -- it
establishes (P) in a setting where the object that breaks (P) does not exist. This is the precise
reason **tree/QM positivity does NOT imply loop positivity**, and it pinpoints where the extrapolation
fails: the continuum threshold at `s = m2^2`. The QFT must reduce to the QM result in the no-decay
limit, and it does -- but that limit is exactly the one with no cut, so it cannot certify the loop.

---

## 5. Synthesizer -- the branch verdict

**Construction:** ghost = wrong-sign-residue pole of the fourth-order propagator (kept, grading-
agnostic cut test); unitarity = Cutkosky + LTE in the Krein metric, with (K) pseudo-unitarity and
(P) physical-subspace positivity held distinct.

| sub-question | verdict | grade |
|---|---|---|
| **Q-cut** | The ghost cut is **present and negative** at one loop; for a *stable* Krein-graded ghost the optical theorem **leaks negative probability on the physical subspace** (case c). It **decouples at one loop ONLY** under a complex-pole / CLOP / fakeon prescription (ghost above threshold, unstable). Conditional pass. | **one-loop indication**, load-bearing on the prescription. NOT a proof. |
| **Q-pos** | Krein pseudo-unitarity `S^dag eta S = eta` survives trivially. The **positive physical inner product surviving renormalization is prescription-dependent and NOT settled by the cut analysis** (it is Branch B's object). | **plausibility only** from this vantage. |
| **Q-caus** | The prescription that saves Q-cut (Lee-Wick complex poles / fakeon average-continuation) **violates micro-causality at the ghost scale** -- unitarity is bought with causality. | **one-loop indication (NEGATIVE / traded).** |

**Confidence grade (overall): one-loop indication.** Strongest honest grade. It is not a proof
because the prescription's higher-loop *uniqueness* is unproven and is precisely the crux.

**Single load-bearing assumption:** a **specific, unique contour prescription** (Lee-Wick complex-
conjugate pole pair, or Anselmi fakeon average-continuation) that (i) removes the ghost from the
asymptotic Hilbert space and (ii) deforms its cut off the physical discontinuity. Krein/keep-and-
grade supplies pseudo-unitarity but does NOT supply this; it is an additional, non-generic input.

**The one obstruction that would kill this construction:** the **CLOP ambiguity / wrong-sign width.**
If no *unique* contour prescription reproduces the same physical S-matrix beyond one loop -- the
known CLOP non-uniqueness at two loops, aggravated by the ghost's anti-resonant (wrong-sign) width --
then there is no construction-independent "physical subspace," the one-loop success does not extend,
and the ghost cut re-leaks. A two-loop demonstration that the prescription is either unique (kills
the obstruction) or ambiguous (confirms the kill) is the decisive next computation.

**Honest bottom line for the orchestrator:** keep-and-grade, *as a grading alone*, does **not** pass
the one-loop cut test -- the ghost cut leaks negative. What passes at one loop is keep-and-grade
*plus a Lee-Wick/fakeon contour prescription*, and that combination pays with micro-causality
(Q-caus) and rests on an all-orders-unproven prescription (Q-cut). The negative result (leak,
exactly located at the graviton+ghost threshold) is as much the deliverable as the conditional pass.
