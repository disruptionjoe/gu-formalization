---
title: "Prong I (INFO-EXACT) of the oracle-relative-thesis swing: is the bit-budget information accounting EXACT or ANALOGY? VERDICT I-MIXED. The load-bearing claim is EXACT and theorem-grade: the inward channel sigma -> internal has LITERALLY zero Shannon capacity -- the blindness lemma Hom(triv,sign)=0 (Schur) is exactly the statement that the sigma->internal channel matrix has IDENTICAL rows (every alpha-even observable is constant on an alpha-orbit, so the two sigma-values induce the same output law), whence I(sigma;internal)=0 for EVERY input prior, prior-free, non-vacuous (the same even algebra has HIGH mutual information with the alpha-invariant world). sigma=1 bit is Hartley-exact; the Shannon reading H=1 needs the alpha-symmetric indifference prior (canonical-by-symmetry, forced uniform, but a max-entropy posit, not a GU-derived probability). The IMPORT CEILING (I2) is NOT a theorem: per-slot caps are exact for the finite slots (sigma<=1, tau<=log2 6) and the budget is finite-DIMENSIONAL by finite deformation theory, but the total BIT-count is uncapped because theta can be a continuum, and no moduli-completeness theorem forbids a 4th free datum -- the planted '4th bit' is not caught by any structural bound, only 'not yet found'. The bit-count THEORY-RANKING invariant (C3/N3/I3) is MIXED: co-rank/nullity is a genuine basis-independent invariant for a FIXED theory + fixed internal/external cut + DISCRETE budget, and the coarse digital(finite)-vs-analog(continuum) ranking is cut-robust, but the fine cross-theory integer is cut-relative. PLANTED CONTROL caught: the record arrow gives I(r;sigma)=1 bit but is alpha-ODD hence not in the internal algebra -- epsilon>0 only via an external resource, confirming zero INTERNAL capacity"
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-oracle-relative-thesis-swing-2026-07-21.md
outcome: I-MIXED
inputs:
  - explorations/council-systems-boundary-meaning-2026-07-21.md
  - explorations/council-aggregation-condorcet-2026-07-21.md
  - explorations/prereg-oracle-relative-thesis-swing-2026-07-21.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/decision-tree-Q2-defense-attorney-2026-07-21.md
  - explorations/decision-tree-Q3-one-anchor-vs-two-2026-07-21.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
runnable:
  - tests/channel-swings/prongI_info_channel_probe.py
hostile_verify_flag: "SUB-Q1 zero-inward-capacity is theorem-grade (Schur Hom(triv,sign)=0 = identical channel rows = capacity 0). Flagged for hostile verify."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
---

# Prong I — INFO-EXACT: is the bit-budget literally information theory?

Adversarial. The job is to decide EXACT vs ANALOGY for the info-theoretic
accounting the councils ranked #1 (INFO steelman, Condorcet winner; the
cross-lens C3/N3/I3 bit-invariant cluster; the top-tied question I2), **not** to
cheerlead it. A "capacity" claim with no defined channel/algebra is ANALOGY and
is called so. The CLOSED PREMISE (sigma is external) is not re-derived; Prong I
asks only whether the *accounting* of that externality is literal.

**Verdict up front: I-MIXED.**

- **Sub-Q1 (zero inward capacity): EXACT — theorem-grade.** The blindness lemma
  `Hom(triv,sign)=0` IS a rigorous zero-Shannon-capacity statement under a
  precisely defined channel. Flagged for hostile verify.
- **Sub-Q2 (hard import ceiling): ANALOGY (with an EXACT finiteness skeleton).**
  No ceiling theorem exists; the finite-budget thesis is conditional on theta and
  on an unproven moduli-completeness. The planted "4th bit" is not caught by any
  structural bound.
- **Sub-Q3 (bit-count as theory-ranking invariant): MIXED.** Co-rank is a real
  basis-independent invariant for a fixed cut with a discrete budget, and the
  coarse digital/analog ranking is robust; the fine cross-theory integer is
  cut-relative.

Receipt: `tests/channel-swings/prongI_info_channel_probe.py` — deterministic,
numpy only, no network, foreground, **exit 0**, double-run **byte-identical**,
HEADLINE `5/5 [E] PASS + 2/2 [F] FIRE -> ALL PASS`.

---

## 0. Definitions first (so no claim is a metaphor)

Let `alpha` be the `K_S`-sign flip (the Z/2 whose non-trivial element negates the
Krein orientation). An observable `f` on the state space is **alpha-even** if
`f(alpha x) = f(x)` for all `x`, **alpha-odd** if `f(alpha x) = -f(x)`.

- **The internal observable algebra `A_int`** is the **alpha-even subalgebra**.
  This is not a modelling choice imposed for convenience: it is exactly the
  diagonal-boundary result that "the excluded-reading class = the
  alpha-equivariant class," and W211's five-method finding that every internal
  sense of "compute inside GU" (counterfactual-invariance, BRST cohomology,
  Lawvere fixed-point, topos logic, Helmholtz reconstruction) lands in the
  alpha-even part. `A_int` is rich (energy, generation count, geometry, all
  alpha-invariant data) — it is emphatically not the trivial algebra.
- **The datum `sigma`** is the alpha-ODD sector bit (value set `{+K_S, -K_S}`),
  the C-grading sign W211 proved Gödel-independent.
- **The channel.** Model a "world" as an alpha-orbit `{p_+, p_-}`; `sigma` labels
  which point is actual (`sigma=+1 <-> p_+`). INPUT `X = sigma`; the internal
  observer applies some `f in A_int`; OUTPUT `Y = f(actual point)`. The
  transition kernel is `P[sigma, y] = Pr(Y = y | X = sigma)`. **Channel capacity**
  `C = max over input priors pi of I(sigma ; Y)`.

This is a fully specified Shannon channel: an input alphabet, an output alphabet,
a transition matrix, and a capacity as a max of mutual information over input
priors. Every claim below is a statement about THIS object, computed in the
probe.

**Hartley vs Shannon, stated once.** HARTLEY information of a finite choice set is
`log|choices|` — pure combinatorics, no prior. SHANNON entropy `H(p) =
-sum p log p` needs a prior `p`. For `sigma in Z/2`, Hartley `= log2 2 = 1`
unconditionally; Shannon `= 1` only under the uniform prior.

---

## 1. Sub-Q1 — is the blindness lemma LITERALLY zero inward capacity? EXACT.

### 1.1 The representation-theory fact is Schur, and it is exactly identical rows

`Hom_{Z/2}(triv, sign)` is the space of Z/2-equivariant linear maps from the
trivial rep to the sign rep. By **Schur's lemma** (distinct irreducibles of a
finite group over a field admit no nonzero morphism), `Hom(triv,sign) = 0`. In
observable terms: no alpha-even map (an element of `A_int`, transforming in
`triv` under alpha) can equal or resolve the alpha-odd `sigma` (transforming in
`sign`). This is not a rhyme with information theory; it is the SOURCE of the
channel's structure, because it forces:

> For every `f in A_int` and every alpha-orbit `{p_+, p_-}`,
> `f(p_+) = f(alpha p_-) = f(p_-)`. The output `Y` is the SAME symbol whether
> `sigma = +1` or `sigma = -1`.

Therefore the two rows of the transition matrix `P[+1, :]` and `P[-1, :]` are
**identical**. Shannon's own criterion: a channel whose transition matrix has
identical rows has the output distribution independent of the input, hence
`I(X;Y) = 0` for EVERY input prior, hence **capacity exactly 0**. This is a
theorem, not an estimate (probe E1: capacity 0 across four priors including the
lopsided `(0.999, 0.001)`).

**The zero is prior-FREE.** It does not wait on a canonical prior: identical rows
give `I = 0` for all priors simultaneously. This is a strength — the standard
worry "Shannon MI needs a prior you cannot justify" does not bite a ZERO, because
zero is robust to every prior.

### 1.2 The zero is NON-VACUOUS (the required teeth)

A zero-capacity channel whose output is a constant would be trivially
zero-information about everything — a vacuous zero. That is NOT the situation.
`A_int` is richly informative about the alpha-INVARIANT world: across different
orbits `w`, the even observables vary and resolve `w` completely. Probe E3:
`I(readout ; w) = 2 bits` (`= log2 4`, full resolution of the invariant quotient)
while `I(readout ; sigma) = 0` exactly. The decomposition is
`I(internal ; world) = I(internal ; orbit-label) + I(internal ; sigma) =
(large) + 0`. The inside sees everything alpha-even and is blind to exactly the
one alpha-odd fiber. This is the precise, non-trivial content of "zero inward
capacity": total resolution of the quotient, zero resolution of the odd bit.

### 1.3 Hartley vs Shannon for the "1 bit" magnitude

The **zero** (Section 1.1) is exact and prior-independent. The **"sigma = 1 bit"**
positive magnitude is where Hartley/Shannon matters:

- **Hartley:** `sigma = 1 bit` is `log2 |Z/2| = 1`, definitional, no prior
  (probe E2). This is the honest caveat the info-theorist member already flagged.
- **Shannon:** to read the missing datum as `H(sigma) = 1` bit you need a prior.
  **Is there a canonical GU prior?** The only structure acting on the sigma-slot
  is `alpha` itself, which swaps `sigma=+1 <-> sigma=-1`. The unique
  alpha-INVARIANT prior is therefore the uniform `(1/2, 1/2)` — forced by
  symmetry — under which `H(sigma) = 1` Shannon bit exactly (probe E2). So a
  canonical prior EXISTS, but it is the **maximum-entropy / indifference** prior
  justified by the alpha-symmetry, **not a probability GU derives**. And note the
  deeper consistency: Gödel-independence is precisely WHY GU cannot derive a
  non-uniform prior — any internal structure singling out a sigma-value would be
  partial internal information about sigma, contradicting blindness. So GU is
  entitled to the uniform prior by symmetry/indifference and entitled to NOTHING
  sharper.

**Sub-Q1 steelman EXACT (accepted):** zero inward capacity is a literal Shannon
theorem (identical rows => C=0), needing no prior; the underlying
representation-theory fact is Schur `Hom(triv,sign)=0`; the zero is non-vacuous
(high MI with the invariant world). **Sub-Q1 steelman ANALOGY (rejected for the
zero, partially upheld for the magnitude):** "capacity needs a prior you cannot
supply" — refuted for the zero (prior-free), conceded for the "1 Shannon bit"
magnitude, which is Hartley-exact and Shannon-only-under-indifference.

**SUB-VERDICT 1: EXACT (theorem-grade).** Zero inward capacity is a genuine
zero-Shannon-capacity theorem. The Hartley bit is exact; the Shannon "1 bit"
rests on the alpha-symmetric indifference prior (canonical-by-symmetry, not
GU-derived). **Flagged for hostile verify.**

---

## 2. The PLANTED CONTROL (mandatory): "inward capacity is actually eps>0"

A zero-capacity claim that cannot be challenged is vacuous. I plant a concrete
internal correlate of sigma and require the framework to catch it or admit it.

**The plant (the sharpest available):** the **record arrow `r`**. By Q3's co-flip
weld `r` tracks sigma perfectly (`r*sigma` alpha-invariant `= +1`), so
`I(r ; sigma) = 1 bit > 0` — a full bit of "inward capacity," apparently refuting
blindness. The first person *possesses* `r` (its own direction of record
accumulation), so this is not a strawman: it is exactly the tension the Q2
decision-tree had to resolve.

**Caught (probe F1).** `I(r;sigma) = 1` bit does FIRE. But the parity filter
catches it: `is_even(r) = False`. `r` is alpha-ODD, hence **not an element of
`A_int`** — it is not an admissible internal readout at all. The `eps>0` is bought
only with an alpha-odd resource, and by the parity typing every alpha-odd resource
IS the external coin (or, per the Q2 defense-attorney trichotomy, welded to it /
an unsourced second posit). Possessing `r` is possessing a **lift/section** of the
Z/2 torsor, not a **map** measurable with respect to `A_int`; conditioning on `r`
is conditioning on the answer, put in by hand. So the plant **confirms** zero
INTERNAL capacity: the only way to make the inward MI positive is to smuggle in an
alpha-odd (external) observable, which the framework flags immediately.

**Second control (probe F2): capacity IS the parity boundary.** Maximising
`I(sigma ; Y)` over ALL even readouts gives `0`; over ALL odd readouts gives `1`
bit. No clever even reader smuggles any fraction of a bit (`max_even = 0`, exact);
the even/odd parity line is literally the `0/1` capacity line. The zero is not an
artifact of a weak reader — it is the max over the entire admissible algebra.

This is the "catch it or admit it" test passing in the CATCH direction: the
planted `eps>0` is real but is exposed as external-resourced, confirming the zero.

---

## 3. Sub-Q2 — is there a hard IMPORT CEILING (question I2)? ANALOGY.

The thesis wants a **capped** budget: GU imports no more than `sigma + tau +
theta`. Note first that this is a DIFFERENT (indeed opposite-facing) quantity from
Sub-Q1: blindness caps what the inside can READ (0 inward); a ceiling caps what
the outside can WRITE. Zero-read does not imply bounded-write. So the ceiling
needs its own argument.

**What would structurally bound the import?** The budget is the number of
independent data GU's structure leaves free = the **co-rank (nullity) of GU's
determination map** = the dimension of GU's free-moduli / deformation space. Three
findings, honestly separated:

1. **Per-slot caps are EXACT for the finite slots.** `sigma` lives in `Z/2`, so
   that slot imports at most `log2 2 = 1` bit; `tau` lives in `Z/6` (Q3), so that
   slot imports at most `log2 6 ~ 2.58` bits (probe E4). A slot valued in a finite
   set cannot import more than the log of its cardinality. This much is a genuine
   cap.

2. **The budget is finite-DIMENSIONAL, by finite deformation theory.** GU is a
   finite-dimensional algebraic construction (a specific Lie algebra `so(9,5)`, a
   specific fiber). The deformation/moduli space of such an object is
   finite-dimensional (its deformation cohomology is finite-dimensional) with
   finitely many connected components. So there cannot be infinitely many
   INDEPENDENT free directions — the free budget is finite-dimensional. This is
   the EXACT skeleton the ceiling thesis can lean on.

3. **But the total BIT-count is NOT capped, for two reasons.**
   - **theta is the ceiling-breaker.** If the boundary is limit-circle (no
     GU-owned measure making `A~` J-self-adjoint with equal Krein deficiency
     indices — the Q1a reopen lemma), theta is a **continuum**: a real-valued
     `U(1)` phase, whose Hartley bit-count is INFINITE. Probe E4: a theta slot
     resolved to precision `2^-n` carries `n` bits and `n -> infinity` — there is
     **no fixed global ceiling**. The budget is finite-dimensional but
     infinite-BIT the moment one modulus is continuous. So even the FINITENESS of
     the budget is conditional on `theta = 0` (the pending measure-lemma).
   - **No completeness theorem forbids a 4th datum.** The docs ENUMERATE `sigma`
     (W211), `tau` (Q3), `theta` (Q1a). But "these are ALL" is a survey of found
     moduli, not a proof that GU's determination map has co-rank exactly equal to
     the enumerated slots. The planted "GU secretly imports a 4th bit" is caught
     ONLY if a 4th free datum can be shown to be a new alpha-parity/moduli
     direction — and there is no structural theorem on the table that forbids one.
     "Not currently found" is weaker than "provably capped."

**Steelman EXACT (partially upheld):** finite-dimensional-by-deformation-theory is
real, and the finite slots are individually capped. **Steelman ANALOGY (upheld for
the hard ceiling):** the *hard* ceiling "at most `sigma+tau+theta`, no 4th bit" is
a well-posed CONJECTURE (budget = co-rank = enumerated moduli) requiring a
moduli-completeness theorem that is not proven; and the total bit-count is
unbounded whenever `theta` is a continuum.

**SUB-VERDICT 2: ANALOGY (with an EXACT finiteness skeleton).** There is no hard
import-ceiling theorem. The finite-budget thesis WEAKENS exactly here: it rests on
(i) `theta = 0` (the pending measure-lemma) and (ii) an unproven completeness of
the moduli enumeration. The planted 4th bit is not structurally excluded.

---

## 4. Sub-Q3 — is irreducible-bit-count a well-defined THEORY-RANKING invariant
(C3/N3/I3)? MIXED.

The cluster's claim: "external bits a theory must import" is a basis-independent,
cross-theory-comparable currency ("this theory costs 1 bit, that costs 3").

**The EXACT core.** For a FIXED theory with a FIXED internal/external cut and a
DISCRETE free budget, the bit-count is the **nullity (co-rank) of the
determination map** = the number of independent Gödel-independent completions. By
rank-nullity, nullity is **basis-invariant** (probe E5: change of basis on the
domain leaves nullity `= 1` unchanged). This is a real invariant, exactly like the
dimension of a solution space or the "degree of incompleteness" (the number of
independent undecidable sentences needed to complete a theory in a fixed
language). So "GU imports exactly 1 discrete bit at the sigma-slot" is well-defined
and invariant. That part of C3/N3/I3 is EXACT.

**Where it is NOT canonical.**
- **Cut-relativity (probe E5).** The integer depends on where the
  internal/external boundary is drawn: re-cutting one determined coordinate into
  "imported data" changes nullity from `1` to `2` for the SAME map. Two theories
  that draw the cut differently (is the gauge group derived or imported? are 3
  generations derived or imported?) are not on a common scalar. This is exactly
  the N3 "which parameters are untrainable" question, and it has no canonical
  answer across theories.
- **Continuum-relativity.** A continuous free parameter (GU's theta-continuum, or
  the Standard Model's ~19+ dimensionless constants) has INFINITE Hartley
  bit-count; to make it finite you impose a precision cutoff, which is a
  convention. So "1 discrete bit vs 19 real numbers" is not a clean integer
  comparison without fixing conventions.

**What IS robust across theories: the coarse digital/analog ranking.** Independent
of the cut, the distinction "imports a FINITE discrete budget" vs "imports a
CONTINUUM" is invariant and meaningful (finite `<` uncountable). "GU imports a
finite handful of discrete bits; a rival imports a continuum of real constants" is
a real, defensible comparison — and it is exactly the comparison the thesis most
wants to make. The FINE integer comparison ("1 vs 3") is the part that is
definition-relative.

**SUB-VERDICT 3: MIXED.** Co-rank/nullity is a genuine basis-independent invariant
for a fixed theory + fixed cut + discrete budget (EXACT); the coarse
digital-vs-analog theory-ranking is cut-robust (EXACT-usable); the fine
cross-theory integer is cut-relative and continuum-sensitive (ANALOGY).

---

## 5. Overall verdict

**I-MIXED.** Itemised:

| sub-claim | verdict | one line |
|-----------|---------|----------|
| **Zero inward capacity** (Sub-Q1) | **EXACT (theorem)** | `Hom(triv,sign)=0` (Schur) = identical channel rows = `I(sigma;internal)=0` for every prior; non-vacuous. HV-flagged. |
| **sigma = 1 bit** magnitude | EXACT (Hartley) / conditional (Shannon) | Hartley `log2 2 = 1` unconditional; Shannon `H=1` under the alpha-symmetric indifference prior only. |
| **Hard import ceiling** (Sub-Q2, I2) | **ANALOGY** | no ceiling theorem; finite-dimensional (deformation theory) but bit-count uncapped if theta is a continuum; no moduli-completeness => 4th bit not excluded. |
| **Bit-count theory-ranking invariant** (Sub-Q3, C3/N3/I3) | **MIXED** | co-rank invariant for fixed cut + discrete budget; digital/analog ranking robust; fine cross-theory integer cut-relative. |

**Is zero-inward-capacity a theorem?** **YES.** Precisely: *the channel from
`sigma` to the alpha-even internal observable algebra has identical transition
rows (every alpha-even observable is constant on an alpha-orbit, so both
sigma-values induce the same output law), hence Shannon capacity exactly 0,
prior-independently; this is the representation-theoretic identity
`Hom_{Z/2}(triv, sign) = 0` cast as a channel.* Theorem-grade, non-vacuous,
planted-control-survived. **Flagged for hostile verify.**

The councils' Condorcet winner (INFO: "sigma = 1 external bit / zero inward
capacity") is therefore **EXACT at its load-bearing core** — the "zero inward
capacity" half is a literal theorem, and the "1 bit" half is Hartley-exact with a
symmetry-canonical Shannon reading. But the two ADJACENT accounting claims the
cross-lens cluster wanted — a hard finite import CEILING (I2) and a universal
cross-theory bit-count CURRENCY (C3/N3/I3) — are **not literally established**: the
ceiling is an unproven moduli-completeness conjecture that a continuum-theta would
break, and the ranking invariant is genuine only for a fixed cut with a discrete
budget (with the coarse digital/analog comparison robust and the fine integer
comparison cut-relative). Hence the honest overall grade is **I-MIXED**, not
I-EXACT: the metaphor is a theorem exactly where the councils put their weight
(the zero), and remains a well-posed-but-unproven program exactly where they
reached past it (the ceiling and the universal currency).

---

## 6. Boundary

Exploration tier. One artifact + one foreground probe
(`tests/channel-swings/prongI_info_channel_probe.py`, exit 0, deterministic,
double-run byte-identical, `5/5 [E] + 2/2 [F] ALL PASS`). Externality of `sigma`
is the program's closed premise, nowhere re-derived; Prong I judges only whether
the *accounting* is literal. The finite Z/2 / discrete-MI probe is a faithful toy
of the structural facts it encodes (Schur identical-rows => capacity 0;
Hartley-vs-Shannon; co-rank basis-invariance and cut-dependence; the record-arrow
correlate is alpha-odd hence non-internal); the operator-grade and proof-grade
content it stands on lives in the cited W211 / Q2 / Q3 / council receipts,
consumed not re-run. No edits to LANE-STATE, research-portfolio, NEXT-STEPS, any
decision-tree, any claim/canon/verdict/ledger file, or any other agent's artifact.
No commit/push, no external actions. The single theorem-grade survivor
(zero-inward-capacity) is flagged for hostile verify before any banking; nothing
here moves a claim, canon, verdict, or public posture.
