---
artifact_type: exploration_result
created: 2026-08-08
status: DEGENERATE_POINT_IS_A_NAMED_OBJECT__SINGULAR_CRITICAL_POINT_IN_KREIN_THEORY__EP_MONODROMY_IS_Z2_AND_SO_IS_TB_PARITY__PSEUDOSPECTRAL_WARNING_ON_EXISTING_NUMERICS
grade: "SPECIALIST PANEL, run inline. No new computation. Every suggestion is
  labelled with what it would take to confirm and a confidence. The Krein
  critical-point identification (S1) is a literature match to measured repo data
  and is the highest-confidence item; the EP-monodromy/ghost-parity link (S2) is
  a HYPOTHESIS and is labelled as such. Nothing here changes a row or verdict."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - tests/krein_parity_dichotomy_jk_anticommutation.py
  - explorations/big-swing-2026-07-06/VG-V4-quantize-break-commuting-square.md
---

# Specialist panel: what the degenerate point actually is

**The data everyone is looking at**, all from `VG-V4` and already measured:

```text
perturbation-splitting exponent   0.498   (Jordan value 1/2)
eigenvector coalescence overlap   1.000000
||C_A(eps)||  ~  eps^-1.00        "C_A not Cauchy"
at eps = 0, BM chart              C does not exist
at eps = 0, normal-form chart     C exists, NOT unique -- an O(1,1) family,
                                  ||C_theta - C_0|| = 0.822
kinematic ghost parity            EXACTLY well-defined at eps = 0
                                  ([P_tot, H(0)] = 0.0e+00)
```

---

## S1 — Krein-space operator theory (Langer, Ćurgus–Najman, Azizov–Iokhvidov)

**The answer.** This is not ad-hoc pathology. It is a **named object**: the
degenerate point is a **critical point** of a definitizable operator, and
`‖C(ε)‖ ~ ε⁻¹` is the textbook signature of a **SINGULAR** critical point (as
opposed to a *regular* one, where the spectral projections stay bounded).

The relevant theorem is not new mathematics: *a definitizable operator whose
critical points are all regular is similar to a self-adjoint operator in a Hilbert
space* — i.e. a bounded metric operator (a `C`) exists. **A singular critical point
is exactly the obstruction to that similarity.** The repository measured the
obstruction and filed it as a numerical pathology.

**What we are not considering.** The regular/singular dichotomy has *criteria* —
conditions on the operator that decide it without computing `C` at all. If GU's
critical point can be shown regular under some deformation or restriction, a
bounded `C` exists there by theorem, with no scan. This is a mature literature the
repository has not touched.

**Confidence: HIGH** that the identification is correct (the `ε⁻¹` rate and
non-Cauchy behaviour are the defining symptoms). **MEDIUM** that a criterion
applies cleanly to GU's arena, which is finite-dimensional and therefore a
degenerate case of a theory built for infinite dimensions — see S8.

---

## S2 — Exceptional-point / non-Hermitian degeneracy theory (Kato, Heiss, Berry)

**The answer.** Splitting exponent `1/2` plus eigenvector overlap `1.000000` is a
**second-order exceptional point** — a square-root branch point of the eigenvalue
surface, where two eigenvectors coalesce into a Jordan block. The resolvent has a
double pole. This is why `C` fails in the BM chart: **the operator is not
diagonalizable there, so no metric can diagonalize it.**

**What we are not considering — and this is the panel's most interesting
suggestion.** Encircling a second-order EP in the complex parameter plane produces
a **state swap plus a geometric phase**: the monodromy is exactly `ℤ/2`. **Turok–
Bateman's ghost parity is exactly a `ℤ/2` grading.** So the hypothesis:

> **The kinematic ghost parity may BE the monodromy of the exceptional point.**

That would explain the otherwise odd fact `VG-V4` measured — the kinematic parity
is *perfectly well-defined at `ε = 0`* while the spectral `C` dies there. A
monodromy is a property of the *loop around* the branch point, not of the point;
it is naturally finite exactly where the local spectral data degenerates.

**Confidence: MEDIUM-LOW as stated, HIGH value.** The `ℤ/2`-matches-`ℤ/2`
observation is suggestive, not evidence — two groups being isomorphic proves
nothing. **Cheap decisive test:** numerically transport an eigenbasis around a
small complex loop encircling `ε = 0` in the existing Pais–Uhlenbeck fixture and
check whether the induced swap coincides with `P_ghost`. That is hours, on code
that already exists.

---

## S3 — Picard–Lefschetz / resurgence (Witten, Écalle)

**The answer.** `‖C_A(ε)‖ ~ ε⁻¹` diverging with non-Cauchy partial data is the
fingerprint of a **Stokes phenomenon**: the asymptotic series for `C` is divergent
and its Borel transform has a singularity whose location is the thimble that
jumps. The exhibited `O(1,1)` family (`‖C_θ − C_0‖ = 0.822`) is plausibly the
**thimble-choice** freedom, not a formless degeneracy.

**What we are not considering.** Nobody has asked whether **one thimble is
selected** by a positivity or convergence requirement. That is the entire content
of Picard–Lefschetz applied to an indefinite path integral, and it is the standard
answer to "the contour is ambiguous."

**Confidence: MEDIUM** that the framing is right; **LOW** that it resolves GU
specifically, because a thimble decomposition needs an action and GU's is unbuilt.

---

## S4 — Pseudospectra / numerical analysis (Trefethen–Embree)

**The answer, and it is a warning about existing results.** Near a defective
operator, eigenvalues are **exponentially ill-conditioned** and the pseudospectrum
is vastly larger than the spectrum. Computed eigenvalues near `ε = 0` may be
numerical artifacts rather than properties of the operator.

**What we are not considering.** No result in this line reports a **condition
number or pseudospectral radius**. `VG-V4`'s own `K-Gram min eig 2.6e-4 → 6.2e-6
as N: 12 → 16` is a *shrinking-with-refinement* quantity — precisely the sign of
approaching defectiveness, where more resolution makes conditioning worse, not
better. **Any spectral claim in this regime should carry a conditioning number and
currently none does.**

**Confidence: HIGH** that the caution is warranted. **MEDIUM** that it changes a
conclusion — `VG-V4` used three independent detectors, which is good practice and
partially mitigates it.

---

## S5 — Pseudo-Hermitian quantum mechanics (Mostafazadeh)

**The answer.** Already used, and it is what made today's question cheap: `C` is
the **metric operator**, determined only up to the **commutant**. So the question
is algebraic, not spectral — which is how `{K,χ} = 0` settled it from filed data
with no rerun.

**What we are not considering.** The metric is non-unique *by design* in this
framework; uniqueness requires fixing a **complete set of commuting observables**.
The repository has been treating non-uniqueness as failure. **The standard move is
to supply the CSCO and thereby fix the metric — which reframes "C is not derived"
from a wall into a missing input with a name.**

**Confidence: HIGH.** This is textbook in that field.

---

## S6 — Quadratic gravity / Ostrogradsky (Bateman–Turok, Salvio–Strumia)

**The answer.** TB's parity is **kinematic**, arising from the two-field `O(1,1)`
embedding, not from spectra. So `R3`'s spectral no-go does not bear on it, and
neither does today's `{J,K}` dichotomy — both are spectral statements.

**What we are not considering.** TB's construction **enlarges** the arena
(one four-derivative field → two two-derivative fields). Every GU test so far has
searched *inside* a fixed arena's commutant. **The enlargement has never been
attempted on GU's carrier**, and an enlarged arena has a different commutant, so
the dichotomy's obstruction does not transfer to it automatically.

**Confidence: HIGH** that this is a genuine untested route. **LOW** that it
succeeds — GU has no S-matrix, and the repo already flags that importing TB's
rescue is itself the unbuilt work.

---

## S7 — Adiabatic theory / geometric phase (Berry, Wilczek–Zee)

**The answer.** On a degenerate eigenspace, adiabatic transport gives a
**non-abelian Wilczek–Zee holonomy** valued in the unitary group of that
eigenspace. R3's eigenspaces are exactly 2-dimensional and K-balanced.

**What we are not considering.** The `O(1,1)` family of admissible `C` operators
looks like a **holonomy orbit**. If so, "C is not determined" is the statement
that the connection is flat-but-nontrivial, and the right question becomes *what
is its holonomy group*, not *why is C not unique*.

**Confidence: MEDIUM.** The structural match is real; the identification is not
made. Cheap to test on the same fixture as S2.

---

## S8 — Functional analysis, dissenting

**The answer.** Everything above is finite-dimensional. Krein critical-point
theory, definitizability, singular vs regular — these are theorems about
**unbounded operators on infinite-dimensional spaces**. In finite dimensions
"`‖C‖ → ∞` as `ε → 0`" is just a matrix family degenerating; there is no spectral
measure to be singular with respect to.

**What we are not considering — the deflating possibility.** The `ε⁻¹` blow-up may
carry **no more content than "a Jordan block is forming"**, which the repo already
knows from the `1/2` exponent. The impressive-sounding vocabulary may add nothing.

**Confidence: HIGH** that the caution is correct as stated. This lens **reduces**
S1's confidence from HIGH to MEDIUM on applicability, and it is recorded because
a panel that only amplifies is not a panel.

---

## Synthesis

**What actually completes the picture, in order of confidence:**

1. **Supply a CSCO** (S5, HIGH). "C is not determined by the dynamics" is not a
   wall — it is the expected state of affairs with a **named missing input**. This
   is the cheapest reframe and it converts a blocked verdict into a specification.
2. **Report conditioning** (S4, HIGH). Any spectral claim near the degenerate
   point needs a condition number. None currently carries one.
3. **Try the enlargement** (S6, HIGH that it is untested). Every test so far
   searched a fixed arena; TB's mechanism works by enlarging it.
4. **Test the EP monodromy against `P_ghost`** (S2, MEDIUM-LOW confidence, HIGH
   value). Transport an eigenbasis around a complex loop encircling `ε = 0` on the
   existing fixture and compare the induced swap to the ghost parity. Hours of
   work on code that exists.

**What the panel does NOT support.** No specialist endorsed "the degenerate point
is a wall." Four independently described it as a **branch point, a critical point,
a Stokes boundary, or a holonomy** — i.e. an object with structure to be
navigated. One (S8) cautioned that the structure may be less than the vocabulary
suggests, and that caution is retained rather than resolved.

**Nothing here changes a row or a verdict**, and no suggestion above is a result.
Each is a proposal with a stated confidence and a stated test.
