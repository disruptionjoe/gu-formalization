---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: H59
branch: "Path-2 wave, Branch E (adversarial red-team / no-go)"
title: "Path-2 Branch E no-go: the positivity-defining grading of the keep-and-grade rescue is DYNAMICAL, lives on an open PT-unbroken domain, and DEGENERATES to zero on a codimension-1 exceptional (Jordan) locus. Therefore loop-level positivity is RG-CONTINGENT, not structural: tree-level positivity certifies only 'safe at the free point' and gives zero protection against the renormalization-group flow reaching the boundary, on which -- by the repo's own R1 two-line theorem -- NO positivity-compatible grading of any kind exists. The obstruction is CLASS-WIDE (Krein / PT-Bender-Mannheim / Bateman-Turok) at the level of the positivity-defining grading, but it is NOT a completed kill of any specific theory: whether GU/Stelle's actual flow crosses the locus is an open per-theory computation. Honest headline: the burden is flipped onto the rescuer."
grade: "exploration / rigorous obstruction-mechanism on a solvable toy + inherited R1 theorem; PLAUSIBILITY for the completed class-wide kill (no specific flow shown to cross the locus). Deterministic arithmetic in tests/W52_path2_E_nogo.py, 7/7 checks, closed-form 2x2 exceptional-point model, no dependencies. No loop amplitude computed. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public posture changed. H59 remains OPEN."
depends_on:
  - explorations/H59-krein-loop-positivity-gate-2026-07-12.md
  - explorations/H59-path2-loop-positivity-blockbuster-wave-design-2026-07-11.md
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
  - explorations/big-swing-2026-07-06/VG-SC-bateman-turok-loop-and-degenerate.md
scripts:
  - tests/W52_path2_E_nogo.py
---

# Path-2 Branch E — the adversarial no-go

**Role.** Branch E of the blind Path-2 keep-and-grade loop-positivity wave. My job is the opposite of
A–D: not to make the rescue work, but to construct the strongest explicit **obstruction** and grade it
honestly. I ran the five-persona team inline (below). I did **not** synthesize across the other blind
branches; this is Branch E's kill-attempt only.

## The construction forks I attack (stated per GEOMETER-VS-PHYSICS-OBJECTS.md)

A no-go is only as strong as the construction it holds in. Three forks are load-bearing here.

| Object | Construction I attack | Why this one |
|---|---|---|
| **Ghost clearance** | GU-native **keep-and-grade** Krein/PT indefinite metric `[P,S]=0` (NOT positive-Hilbert removal, SUSY, Lee-Wick, or fakeon) | This is GU's object and the whole class's rescue. |
| **Grading** | the **positivity-defining** grading (C-operator / positivity-compatible ghost parity / metric operator `eta_+`), NOT the kinematic Krein form `eta` | The kill turns on the distinction: `eta` (Cartan involution of `so(9,5)`) is kinematic and survives RG but is **indefinite**; the object that makes probabilities positive is dynamical. |
| **Unitarity** | **positive Born-rule probability on the physical subspace**, NOT pseudo-unitarity `S†S=1` | Bateman–Turok establish pseudo-unitarity/optical-theorem **to all orders**; I do not dispute that. The frontier is positivity, so that is what I attack. |

The single most important fork call: **the GU-native hope that "the grading is the kinematic Cartan
involution, so it cannot run" is already closed by the repo's R1 result.** R1 proved (in the shared
Pais–Uhlenbeck toy, machine-checked) a two-line theorem: a positivity-compatible grading `P`
(`P²=I`, `[P,H]=0`, `eta P > 0`) exists **iff** `H` is Krein-diagonalizable with real spectrum. The
kinematic `eta` alone never selects the positive half; the positivity-defining object is
**dynamical**. So the obvious GU repair does not defuse the obstruction — it is pre-empted.

## The obstruction, in one paragraph

Keep-and-grade unitarity has two objects that must not be conflated: the kinematic indefinite Krein
form `eta` (fixed, survives everything, but defines no positive probability) and the positivity-defining
grading `eta_+` / `C` (the thing that makes the physical inner product positive). By R1, the second
exists **iff the interacting action is Krein-diagonalizable with real spectrum** — a property of the
couplings, not a kinematic datum. Hence the positive physical inner product is a **function of the
couplings**, and the region of coupling space where it exists is **open, with a boundary**: the
PT-breaking / exceptional (Jordan) locus. Tree-level positivity is only "at the free point we are
safely inside." It gives **zero** protection against the renormalization-group trajectory reaching the
boundary, on which the grading provably ceases to exist. **Loop positivity is therefore RG-contingent,
not structural.**

## Persona 1 — the no-go / locality-theorem specialist: the explicit construction

The mechanism is exhibited in closed form on the minimal exceptional-point model — the 2×2 PT
Hamiltonian, which is the per-mode skeleton of every fourth-order ghost problem (Pais–Uhlenbeck reduces
to it mode by mode):

```
H(a,b) = [[ i a,  b ],
          [  b, -i a ]],     a, b real (effective, running, couplings).
```

Everything is analytic:

- **Spectrum:** `lambda = ± sqrt(b² − a²)`.
- **Positive intertwining metric (the positivity-defining grading):** the unique (up to scale/family)
  positive solution of `eta_+ H = H† eta_+` is
  ```
  eta_+ = [[   1, −i a/b ],
           [ i a/b,   1  ]],   eigenvalues 1 ∓ a/b.
  ```
- **PT-unbroken** (real spectrum, `eta_+ > 0`) **⇔ |a| < b.**
- **Exceptional locus a = b:** eigenvalues collide, `H` is a defective **Jordan block**,
  `lambda_min(eta_+) = 0` — the positive metric **degenerates**; no positive inner product.
- **PT-broken |a| > b:** imaginary spectrum, `eta_+` **indefinite** — positivity is gone.

Reading `a, b` as effective couplings that run, `eta_+(a,b)` depends on the ratio `a/b` and is
**not RG-invariant**; and `lambda_min(eta_+) = 1 − a/b → 0` as `a/b → 1`. The positive metric is
destroyed by **degeneration** on a codimension-1 locus — a failure no sign-flip-catching grading can
repair (there is no negative probability to project away; the norm simply collapses to zero).

This is exactly the structure R1 measured on the full Pais–Uhlenbeck oscillator (`min|nu| ~ eps²`,
`||C|| ~ eps^−2`, joint blow-up of the BM `C`-operator and the TB ghost parity at `w1 = w2`, and a
two-line nonexistence theorem at the boundary). The 2×2 model is the clean analytic distillate:
same mechanism, closed form, no truncation.

## Persona 2 — the math-physics referee: grade, and the circularity check

- **What is rigorous.** (i) `eta_+` genuinely intertwines `H` (checked to machine zero). (ii) The
  domain structure unbroken/exceptional/broken is exact and closed-form. (iii) The degeneration
  `lambda_min → 0` on the locus is exact. (iv) The R1 two-line theorem (`positive grading ⇔
  Krein-diagonalizable real spectrum`) is a proven repo result. Together these establish the
  **RG-contingency + fatal boundary** rigorously.
- **What is NOT rigorous / not claimed.** That any *specific* theory's actual RG flow reaches the
  locus. The 2×2 model does not carry Stelle/GU beta functions; the exceptional point in it is a
  submanifold, not a demonstrated attractor of a physical flow. So the completed class-wide kill
  ("the rescue provably fails") is **plausibility**, not theorem.
- **Circularity check.** The argument does **not** assume the ghost breaks unitarity and then conclude
  it. It grants the rescue its best case (tree positivity = "safe interior", pseudo-unitarity all
  orders) and derives a *contingency* purely from the domain geometry of the positivity-defining
  object. No step presupposes the conclusion. Clean.
- **Grade issued.** Q-pos obstruction-mechanism: **rigorous (toy + R1)**. Completed specific kill:
  **plausibility**. This is a *reframing-strength* no-go: it flips the burden, it does not close the
  question.

## Persona 3 — the adversary-to-the-adversary: a fair repair attempt

I genuinely tried to repair the theory against my own obstruction. Four repairs, honestly assessed:

1. **"The grading is kinematic (Cartan involution), so it cannot run."** *Pre-empted by R1:* the
   kinematic form is indefinite and not positivity-defining. **Fails.**
2. **"Pseudo-unitarity is all-orders (Bateman–Turok), so unitarity is safe."** True but off-target:
   pseudo-unitarity is `S†S=1` in the indefinite metric; **positivity** is the separate property that
   degenerates. BT themselves prove positivity only at tree level. **Does not defuse.**
3. **"Prove the specific flow stays PT-unbroken for all μ."** This *would* defuse it — and it is
   **exactly the missing H59 computation.** So this repair is not a rebuttal; it is a concession that
   converts my obstruction into a sharp, decidable demand: *exhibit the flow and show it never reaches
   `a/b = 1` (no ghost-mass → 0, no pole collision, no exceptional crossing).* Tree positivity gives
   zero evidence on it.
4. **"The exceptional locus is measure-zero, so generic flows miss it."** Weak: (a) fourth-order
   gravity has a *physically distinguished* degeneration — the conformal / massless-spin-2-ghost limit
   `m2 → 0` — which is not a random point but a symmetry-enhanced one the flow can be *driven toward*;
   (b) measure-zero in coupling space is not measure-zero along a *one-dimensional* RG trajectory that
   can be aimed at it; (c) even *approaching* it makes `||C|| → ∞`, so the physical Hilbert space
   becomes arbitrarily ill-conditioned — a soft failure short of the locus.

**Verdict of the repair attempt:** repairs 1–2 fail outright; repair 4 is weak. Repair 3 *succeeds in
principle* but only by performing the exact open computation — so it confirms the obstruction is a real,
unmet burden rather than an artifact. **The no-go is class-wide at the grading level and survives fair
steelmanning, but it is not a completed kill.** Honest.

## Persona 4 — the cross-checker: the concrete toy

Encoded deterministically in `tests/W52_path2_E_nogo.py` (pure Python, no numpy, exit 0, 7/7):

- **E1** `eta_+` really intertwines `H` (`max||eta_+ H − H† eta_+|| = 0`) — it is the genuine
  positive metric, not a strawman.
- **E2** unbroken `|a|<b`: real spectrum, `eta_+ > 0` (the tree-level safe interior).
- **E3** `a/b → 1`: `lambda_min(eta_+) → 0`, matching the closed form `1 − a/b` — the kill core.
- **E4** on the locus `a=b`: spectrum collides, defective Jordan block, `lambda_min(eta_+)=0` — the
  R1 nonexistence theorem realized.
- **E5** past the locus `|a|>b`: imaginary spectrum, `eta_+` indefinite — positivity lost.
- **E6** `eta_+(a,b)` runs with `a/b`; the only RG-fixed grading (the kinematic Krein form) is
  indefinite — so nothing RG-stable rescues positivity.
- **E7** honesty guard: the file asserts it has **not** proven any specific flow crosses the locus.

Independent numeric confirmation (numpy, off-line): eigenvalues and metric eigenvalues match the
closed forms to `~1e-16` across `a ∈ {0.3, 0.7, 0.95, 0.999, 1.0, 1.3}`, and the intertwining residual
is `≤ 5.6e-17`. This is the same qualitative structure R1 found on the four-mode PU oscillator
(`min|nu| ~ eps²`), here reduced to an exact 2×2 skeleton — a genuine second derivation of the
degeneration, not a re-run.

## Persona 5 — the synthesizer: branch verdict

**Graded verdict on the three sub-questions.**

- **Q-pos (primary target) — OBSTRUCTION LANDS.** The grading that defines the positive physical inner
  product is dynamical, exists only on an open PT-unbroken domain, and degenerates to zero on a
  codimension-1 exceptional locus. Loop positivity is **RG-contingent, not structural**. *Grade:
  rigorous* for the contingency + fatal boundary (toy + R1 theorem); *plausibility* for any completed
  "the flow crosses it" kill of a specific theory.
- **Q-cut — INHERITS the contingency.** Pseudo-unitarity `S†S=1` is all-orders (Bateman–Turok) and
  **not disputed**. But ghost/cut *decoupling* is a positivity statement (the ghost must not add
  negative spectral weight to `Im M` on the physical subspace), so it holds only in the PT-unbroken
  phase and degenerates at the locus (double poles / secular growth). *Grade: plausibility.*
- **Q-caus — the locality cost, honestly a folk-theorem.** The map to an equivalent Hermitian theory is
  the similarity transform `eta_+^{1/2}`; because `eta_+` is bilinear/nonlocal in the fields
  (`eta_+ = e^{−Q}`, `Q` a field bilinear), the Hermitian-equivalent theory is **generically
  non-local**. This is the standard critique of PT-QFT. I checked whether it is a *theorem*: it is
  **not** in general — there exist PT models with local Hermitian equivalents — so the honest status is
  *plausibility / folk-claim*: unitarity is bought at a locality cost **unless** the ghost-sector
  metric is local, which is unestablished. *Grade: plausibility.*

**Class-wide or construction-specific?** **CLASS-WIDE** at the level of the positivity-defining
grading — R1's equivalence (`positive grading ⇔ Krein-diagonalizable real-spectrum action`) is
construction-independent within the keep-and-grade class, so the contingency and the fatal locus apply
to Krein, PT/Bender–Mannheim, and Bateman–Turok alike. It is *construction-specific* only in the honest
sense that it does **not** touch pseudo-unitarity (all-orders) or the kinematic Krein form (survives);
it attacks specifically the claim that a *positive* physical inner product is RG-stable.

**The one assumption the whole kill rests on.** R1's equivalence transfers from the Pais–Uhlenbeck
quantum-mechanical toy to the interacting QFT: at loop level too, a positivity-compatible grading exists
iff the renormalized action is Krein-diagonalizable with real spectrum. If a purely **kinematic**
positive grading existed for the ghost sector in QFT, the RG-contingency would vanish and this kill
would fail.

**Confidence grade.** *Rigorous theorem* for the obstruction mechanism (grading dynamical +
finite-domain + fatal exceptional boundary), backed by the closed-form toy and the repo R1 theorem.
*Plausibility* for the completed class-wide kill "the rescue fails" — because no specific RG flow is
shown to cross the locus. **This is not a completed kill; it is a rigorous demonstration that loop
positivity is dynamically contingent with a concrete, named failure locus, which flips the burden onto
the rescuer.** Per the wave's honest pre-registration, this is the "split / precise map" outcome, not the
"class-shared kill" outcome — reported as such, not dressed up.

## What this does NOT do

No GU/Stelle loop amplitude is computed. No proof that any physical flow reaches `a/b = 1`. No change to
`CANON.md`, `RESEARCH-STATUS.md`, claim status, verdicts, or public posture. H59 stays **OPEN**. The
contribution is a sharpened, decidable burden for whoever would complete the rescue: **exhibit the RG
flow of the fourth-order (+RS) sector and prove it never reaches the exceptional (Jordan / pole-collision
/ `m2 → 0`) locus** — because on that locus, positivity is unrescuable by any grading.

## Next valid Branch-E swing

1. Push the toy from QM to a one-loop QFT self-energy: does the running of the effective spin-2 ghost
   mass `m2(μ)` in Stelle/agravity drive `a/b → 1` (pole collision) in the UV or IR? This is the
   computation repair-3 demands.
2. Decide Q-caus properly: is the ghost-sector metric operator `eta_+` local or not for the fourth-order
   graviton? That converts the folk-theorem into a theorem or refutes it.
3. Cross-test (for the orchestrator, not done here): does this exceptional-locus obstruction bite the
   fakeon (C) and Lee-Wick (D) constructions, which move the ghost pole off the real axis and may thereby
   *evade* the real-axis collision — or merely relocate it?
