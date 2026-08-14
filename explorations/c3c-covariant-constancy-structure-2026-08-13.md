---
title: "C3c structure: the split-layer complex structure is parallel exactly when the connection has no mixed component, plus a ten-lens redirection of the research question"
status: draft_result
doc_type: construction_result
artifact_type: construction_result
created: 2026-08-13
target_claim: NONE-NOT-A-KILL
binding: >-
  Binds nothing. No disposition, no verdict, no claim-status, canon, ledger,
  registry or posture change. Section 1 is exact integer computation on a
  constructed representation. Sections 2-4 are PROPOSED interpretation and lens
  critique, not results. The physics reading of J as "superposition" is a
  hypothesis under test, not a repository claim.
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# C3c covariant constancy, computed — and why the question should change

Origin: a Joe-directed hypothesis ("Steelman A") that superposition and chirality
are the *same* emergence, because the ambient real Clifford algebra has no complex
structure and the split layer natively supplies one. The decisive condition for that
hypothesis is `C3c`: is the emergent complex structure covariantly constant?

## 1. What was computed (exact, integer)

Construction: `Cl(7,7)` built as a real `128x128` representation by a
Jordan-Wigner tensor scheme, 7 generators squaring to `+I` and 7 to `-I`. All 105
Clifford relations verified exactly (14 squares, 91 anticommutators), 0 failures.

Split taken as `(1,3) + (6,4)`: a 4-generator block (1 positive, 3 negative) and a
10-generator block (6 positive, 4 negative). This yields 51 split bivector
generators (`C(4,2) + C(10,2) = 6 + 45`) and 40 mixed generators (`4 x 10`), total
91 = `dim spin(7,7)`.

Let `J = vol(6,4)`, `K = vol(1,3)`, and `omega = JK` (the ambient volume element up
to sign).

| fact | result |
| --- | --- |
| `J^2` | `-I` (J is a complex structure) |
| `K^2` | `-I` |
| `omega^2 = (JK)^2` | `+I` (an involution, not a complex structure) |
| `[X, J] = 0` for the 51 split generators | **51 / 51** |
| `[X, J] = 0` for the 40 mixed generators | **0 / 40** |
| `{X, J} = 0` for the 40 mixed generators | **40 / 40** (exact anticommutation) |
| rank of `m -> [., J]` | **40 of 40, kernel dimension 0** |
| `[X, omega] = 0` over all 91 generators | **91 / 91** |

**Result 1 (`D_varpi J = 0`).** Since `J` is constant in the algebraic frame,
`D_varpi J = [varpi, J]`. `J` commutes with the entire split subalgebra and
anticommutes with every mixed generator, and the obstruction map on the mixed block
has **zero kernel**. Therefore `D_varpi J = 0` **if and only if the connection has
no mixed component** — a strict holonomy reduction to `Spin(1,3) x Spin(6,4)`, with
no partial escape in any of the 40 directions.

**Result 2 (`D_varpi omega = 0`).** `omega` is central in `spin(7,7)` — it commutes
with all 91 generators. So the second `C3c` leg holds **identically, for every spin
connection**. The two legs are not comparable in difficulty: one is free, the other
is a full reduction.

**Structural reading.** The *existence of two halves* is unconditional: `omega` is a
parallel involution whatever the connection does, and its `+/-1` eigenspaces split
the module always. What is conditional is the **complex structure on them**.

**Correction to an earlier claim in this session.** The commutant was expected to be
quaternionic (`dim 4` was read as `H`). It is not. `{1, J, K, JK}` are linearly
independent (rank 4 of 4) and **mutually commuting**, so the algebra is `C (+) C`,
not `H`. Consequence: this construction predicts **no quaternionic phase structure
at all**, which is consistent with the existing null results, but it also means the
"quaternionic sphere collapses to `+/-`" story told earlier is wrong and is
withdrawn.

Probe: `scratchpad/c3c/c3c_probe.py`, `scratchpad/c3c/commutant2.py` (deterministic,
exact integers, no floating point in the verdicts).

## 2. The hypothesis this was meant to test

That `varpi` having mixed components is exactly what couples the two halves; that
the source's stated mechanism (two chiral halves coupled by a VEV, decoupling as
curvature drops) is the same off-block component; and therefore that stable
superposition and emergent chirality switch on together, governed by the same 40
generators.

Section 1 is consistent with that picture and makes it precise. It does not
establish it.

## 3. Ten specialist lenses on whether this is the right question

Run inline. Each is a critique of the approach, not of the arithmetic.

1. **Clifford / representation theory.** For any split of an even-dimensional
   Clifford algebra into two *even-dimensional* blocks, each block volume element is
   central in its own even subalgebra and commutes with the other block. So the
   `C (+) C` commutant and the commutes-with-split / anticommutes-with-mixed pattern
   are **generic consequences of an even-even split**, not features of `(1,3)+(6,4)`.
   *This is the most damaging critique in the list.* Test: repeat on several other
   even-even splits. If the pattern is identical, Section 1 carries no GU content.
2. **Holonomy geometry.** `D J = 0` with `J^2 = -1` is the classical Kähler
   condition: holonomy contained in a unitary subgroup. The pointwise algebra is the
   easy half; the real content is the **topological obstruction to a global
   reduction** of the frame bundle, which is a characteristic-class question, not a
   commutator question.
3. **Quantum foundations.** A complex structure on a Clifford module is not the `C`
   of quantum amplitudes. Superposition lives on the **state space** and needs a
   symplectic form with a compatible `J` (a Kähler pair), not a spinor-module
   endomorphism. Identifying the two is a Layer-0 homonym risk of exactly the kind
   this repository documents.
4. **Geometric quantization.** The right frame is **polarization**. A compatible `J`
   is a Kähler polarization, and inequivalent polarizations generally give
   unitarily inequivalent quantizations. That converts the `+/-` bit from a story
   into a computable question: **are the two polarizations unitarily equivalent?**
   Equivalent implies the bit is unphysical; inequivalent implies superselection.
5. **Krein-space / indefinite-metric QFT.** On a Krein space the positive subspace is
   not unique — fundamental decompositions form a large family. Checking four
   candidate volume elements does not determine the space of admissible `J`. The
   `+/-` may be an artifact of the candidates chosen rather than a real binary.
6. **Index theory.** A holonomy reduction to a unitary subgroup changes the index
   theory available (Todd/Chern rather than `A-hat`/Pontryagin). That is a **direct
   line to the generation count**, which is the program's actual open question, and
   it is unexploited here.
7. **PDE / well-posedness.** Covariant constancy is pointwise and algebraic. Stable
   superposition is dynamical and needs well-posed evolution — on an ultrahyperbolic
   domain with no initial-value formulation. `D J = 0` is necessary and nowhere near
   sufficient.
8. **Interferometry / experiment.** Nothing here yields a **rate**. What is
   measurable is a decoherence rate against an environmental parameter. Without
   `decoherence ~ f(|varpi_mixed|)` there is no contact with matter-wave bounds.
9. **Statistics / identifiability.** The repository already proves `sigma` is a
   capacity-0 read channel with Fisher information identically zero. If the `+/-`
   bit is `sigma`-like, it is **non-identifiable**, and a non-identifiable parameter
   cannot be what a measurement selects. Establish identifiability *before*
   investing further.
10. **Adversarial referee.** "Superposition holds where `J` is parallel" risks being
    a redescription: quantum mechanics works where the structure quantum mechanics
    needs is present. Name one thing the hypothesis **forbids** that standard quantum
    mechanics permits, or it is not yet physics.

## 4. The better approach these converge on

Lenses 1, 2, 6 and 9 point the same way, and 3, 4, 10 rule out the naive framing.

**Do not ask "what causes superposition." Ask instead: does the required holonomy
reduction to `Spin(1,3) x Spin(6,4)` carry a topological obstruction on `Y14`, and
is that obstruction the same one that controls the generation count?**

Why this is the stronger question:

- It survives lens 1, because the pointwise algebra being generic is precisely the
  point: **the content is topological, not algebraic.** A characteristic-class
  obstruction is not generic.
- It avoids the category error in lens 3 entirely. No claim about amplitudes is
  needed to state or test it.
- It answers lens 10, because an obstruction **forbids** something concrete: if the
  reduction is obstructed, no connection anywhere on `Y14` has vanishing mixed
  component, and the emergent structure cannot be global.
- It sidesteps lens 9's identifiability trap, because it is a statement about the
  bundle rather than about an unreadable bit.
- It plugs into the repository's existing strengths — characteristic classes, spin
  bordism, `AHSS`, index theory — rather than requiring new machinery.
- Per lens 6, it may connect directly to the count, which is the open question that
  actually matters.

**Concretely:** compute the obstruction to reducing the structure group of `Y14`'s
frame bundle from `Spin(7,7)` to `Spin(1,3) x Spin(6,4)`, on the actual `Met(X4)`
geometry rather than pointwise. This is the same class of computation as the
existing `AHSS` and bordism work, and non-compactness of `Y14` is a known
complication the repo has already met elsewhere.

**Lens-1 control: RUN, and it splits the verdict.** Section 1 was rerun on six
further even-even splits of `(7,7)`. Probe: `scratchpad/c3c/control.py`.

| split | `J^2` | `[split,J]=0` | `[mix,J]=0` | `{mix,J}=0` |
| --- | --- | --- | --- | --- |
| **(1,3)+(6,4)** | **`-I`** | 51/51 | 0/40 | 40/40 |
| (2,2)+(5,5) | `+I` | 51/51 | 0/40 | 40/40 |
| **(3,1)+(4,6)** | **`-I`** | 51/51 | 0/40 | 40/40 |
| (0,4)+(7,3) | `+I` | 51/51 | 0/40 | 40/40 |
| (4,0)+(3,7) | `+I` | 51/51 | 0/40 | 40/40 |
| (1,1)+(6,6) | `+I` | 67/67 | 0/24 | 24/24 |
| (3,3)+(4,4) | `+I` | 43/43 | 0/48 | 48/48 |

**Lens 1 is correct that the commutation pattern is generic.** Commutes-with-split
and anticommutes-with-mixed hold for every even-even split tested, with zero kernel
every time. Section 1's *pattern* therefore carries no signature-specific content
and must not be cited as evidence for the hypothesis.

**Lens 1 is wrong that the whole result is generic.** The volume-element squares are
not. `J^2 = -I` in only **2 of 7** splits: `(1,3)+(6,4)` and `(3,1)+(4,6)`, which are
the same physical split under the metric sign convention. Everywhere else the volume
element is an involution, not a complex structure.

The arithmetic behind it: for a block of dimension `d` and signature `(p,q)`,
`vol^2 = (-1)^{d(d-1)/2} (-1)^q`. For a 4-block this is `-1` exactly when `q` is
**odd**, i.e. exactly for Lorentzian signature; for a 10-block it is `-1` exactly
when `q` is **even**.

**Result 3 (signature selection).** Among even-even splits of `(7,7)` into a 4-block
and a 10-block, a complex structure exists on both factors **only for Lorentzian
`(1,3)` with `(6,4)`**. The emergent complex structure is not generic: it selects
Lorentzian signature on the 4-block.

This is the first thing in this pass that is about the geometry rather than about
Clifford bookkeeping, and it is what the hypothesis needed.

## 5. Three standing charges

**Where the summary outruns the artifact.** Section 1's headline reads as support
for Steelman A. Lens 1 may reduce it to a generic fact about even-even splits, and
that control has not been run. Until it is, Section 1 supports nothing about GU.

**Where rigor defends a superseded or mistyped object.** The quaternionic-collapse
reading told earlier in the same session is withdrawn here; the commutant is
commutative. Any downstream use of the quaternionic framing is mistyped.

**Downstream dispositions.** Dissolved: the quaternionic-collapse story. Survives:
the exact `C3c` structure in Section 1, and the `ROR`-style research move in
Section 4. Needs-recheck: whether `J = vol(6,4)` is the repository's `+/-J10`, which
was not verified here, and whether B-compatibility narrows the admissible `J` beyond
the four candidates tested (lens 5).

---

## 6. Index-change hypothesis: computed, and dead on this background

Tested the lens-6 suggestion that the holonomy reduction switches the relevant index
theory from `A-hat`/Pontryagin to Todd/Chern and thereby moves the generation count.
Probe: `scratchpad/c3c/index_change.py`, exact rational arithmetic.

**The two index theories are not independent.** Verified in six cases:

> `Td = A-hat * exp(c1/2)`, and on a 4-manifold `Td - A-hat = c1^2 / 8` exactly.

So a reduction can move the count **only through `c1`**.

**On the repository's actual background it cannot.** K3 is hyperkähler, so `c1 = 0`,
and with `c2 = chi = 24`, `p1 = -48`:

> `A-hat(K3) = 2` and `Td(K3) = 2`. **Equal.**

The generation work runs on K3 with `A-hat(K3) = 2` as a load-bearing input.
Switching index theories there changes nothing. **The hypothesis is dead as stated.**

**It also carries a prior Layer-0 defect.** The `J` computed in Section 1 is the
volume element of the `(6,4)` block acting on the **128-dimensional spinor module**.
The `A-hat -> Td` switch requires a complex structure on the **14-dimensional
tangent bundle**. Different objects. This is the same J-on-vectors versus
J-on-spinors homonym that produced a refuted hypothesis earlier in the same session,
and it must be typed before any future version of this claim is computed.

**Permanent constraint, cheap to apply:** any future claim that a holonomy reduction
moves the generation count must first exhibit `c1 != 0` on the manifold carrying the
reduction. On a Calabi-Yau or hyperkähler background the claim is identically empty.

**What the reduction does change instead.** A reduction to a *product* group makes
the Dirac operator factor, so the index becomes a **product** of block indices. The
repo's current count is a **sum**: `ind_H(D_GU) = 8*A-hat(K3) + 8 = 16 + 8 = 24`.
Sum and product are different arithmetics on the same reduction. Whether the
factorization actually fires depends on the bundles distributing across the two
blocks, and on the parallel-splitting condition — for which the repo has already
computed the relevant O'Neill A- and T-tensors at the totally geodesic LC section.
That is the version worth computing; it is not the version tested here.

---

## 7. Falsification record: the Willmore-coherence hypothesis

**Hypothesis tested (strong form).** GU's variational principle is a coherence
principle: `E[s]` is the functional whose minimum is exactly the condition for the
emergent complex structure to be parallel, because `D_varpi J = 0` iff the mixed
connection block vanishes iff `II_s = 0` iff `E[s] = 0`.

**VERDICT: FALSIFIED.** Three independent attacks, two of them decisive.

**Attack 1 — the functional is narrower than the claim (LANDS).** The canon form is
`E[s] = integral |II_s^H|^2` (`canon/schwarzschild-weak-field-rfail.md:22`;
`DERIVATION-PROGRESS.md:1433`) — the *horizontal* second fundamental form.
`DERIVATION-PROGRESS.md:543` and `:640` write `|II_s|^2` without the superscript, so
the repository is inconsistent here and the canon form governs. `E[s] = 0` therefore
forces only `II^H = 0`, while `D_varpi J = 0` requires the entire mixed block to
vanish. The central equivalence does not hold.

**Attack 2 — the physical section is not even critical (DECISIVE).**
`DERIVATION-PROGRESS.md:1293`: three independent lines establish that **Schwarzschild
is NOT a critical section** of `E[s]`. That is the solar system. Combined with
Section 1's **kernel-zero** result — parallel or not is binary, no protected
direction, no partial escape — the strong hypothesis predicts **no stable
superposition anywhere near a mass.** Refuted by every interference experiment
performed.

**Attack 3 — the surviving weak form makes no measurable prediction (LANDS).** The
rate version ("the functional penalizes incoherence rather than enforcing coherence,
with decoherence rate proportional to `|II_s^H|^2`") survives Attacks 1 and 2, but
yields a **dimensionless suppression**, not a rate, until a frequency scale is
supplied. Near a mass `RFAIL-03` gives a linear-order residual that vanishes
identically (`H^(1) ~ M/r` is harmonic) with the leading term at `O(M^2/r^4)`, so
the suppression is second order in mass. Whether that is observable depends entirely
on the undetermined scale: with an ordinary laboratory frequency the effect sits far
above graviton-induced decoherence (recent estimates put that at `10^-64` to
`10^-74` across matter-wave platforms) and could be reachable; with a Planck-scale
frequency it would already be excluded. **The hypothesis does not predict; it
awaits a scale.**

**What the external bounds actually do.** They constrain the missing scale rather
than the hypothesis. Collapse-model limits from matter-wave interferometry
(underground experiments pushing `tau > 10^3 s` at `~10^4 Da`, exceeding naive
Diósi-Penrose by two orders of magnitude) bound any candidate frequency. That
converts "unfalsifiable" into "constrained but undetermined" — an improvement, not a
result.

**Third weak link, recorded for completeness.** The 4-block in Section 1 was chosen
*algebraically* (four Clifford generators). Whether that split coincides with the
geometric tangent/normal split of an actual section is an assumption the algebra
cannot see. The identification "mixed block = second fundamental form" requires that
correspondence, and the canon `^H` superscript indicates the operative object is
narrower still.

**What would revive it.** A derivation of the frequency scale from the geometry,
turning `|II_s^H|^2` into an actual rate. Absent that, this line should not be
carried as support for anything.

**What survives from this whole pass, independent of the falsified hypothesis:**
Section 1's exact `C3c` structure (kernel zero; `omega` central so the two-half split
is unconditional), Result 3's Lorentzian selection (robust across all ambient
signatures tested), and Section 6's permanent `c1` constraint on index-change claims.

---

## 8. CORRECTION (2026-08-13, superseded by the J10 BV / Green-domain descent gate)

An independent pass — `selected_k77_j10_bv_green_descent_gate_probe.py`, 112/112
exact — supersedes this artifact's technical core and corrects it on four points.
Its result should be read in place of Sections 2 and 7 wherever they conflict.

**Independently replicated.** That pass reproduces Section 1's structure exactly on
the same real `128x128` module: 51 commuting split generators, 40 anticommuting
mixed, `J10^2 = -I`. Two independent constructions, same numbers. Section 1 stands.

**Correction 1 — the lift was mistyped.** Section 1 used spinor-only `J10`. On the
owned fermion carrier `Omega1(S) + Omega0(S)` the naive diagonal lift fails to
preserve the gamma-trace projector. The correct object is the reflection-twisted
`Jhat = (R_split tensor J10) + J10` with `R_split = diag(+1_BASE, -1_NORMAL)`.
Anything here that treats `J10` directly as an endomorphism of the rolled carrier is
mistyped.

**Correction 2 — positivity was assumed, and it does not hold.** Section 7's rate
argument, and the whole `E[s] = 0 iff II^H = 0` step, silently assumed a
positive-definite norm. **The normal DeWitt metric is indefinite on K77.** A nonzero
null tensor can therefore have zero quadratic density, so `|II_s^H|^2 = 0` does not
imply `II_s^H = 0`. This is the worst error in this artifact: a Euclidean
positive-norm default imported into an indefinite setting, inside a program whose
substrate is explicitly Krein.

**Correction 3 — the `II` versus `II^H` discrepancy is not repository sloppiness.**
Section 7 Attack 1 called it an inconsistency. It is a deliberate **reference
normalization**: `II_s^H = II_s^raw - II_s^ref`, and at the tautological LC section
`II_s^raw` is a nonzero algebraic slice term while `II_s^H = 0`. The real gap is that
`[varpi, J10]` senses the **raw** mixed block of whatever connection it is handed,
so closing the equivalence requires constructing a normalized `varpi^H` and proving
its mixed block is exactly `II_s^H`. Attack 1's *conclusion* survives; its
*diagnosis* was wrong and is retracted.

**Correction 4 — the K3 endpoint is not selective.** Section 7 leaned on
`E[s_LC] = 0` at the K3 Yau metric as though it were special. It is not:
`E[s_g] = 0` holds for **every** tautological LC section, and the functional is flat
in that metric direction. The zero selects neither a metric nor a topology.

**Corrected standing verdict**, adopting the superseding pass's language: the
defensible claim is **coherence-compatible observed reduction**, not "the Willmore
action is a decoherence functional." Fixed `J10` fails to descend through the owned
ordinary-gauge BRST quotient — 8 of the 25 selected gauge directions are mixed and
every one breaks it — while moving `J10` is exactly covariant. The moving-reduction /
BV formulation is therefore **mandatory, not optional**.

**What from this artifact is not in the superseding pass, and should not be lost:**

- **Result 3, Lorentzian selection.** `vol^2 = -1` on the 4-block iff `q` is odd; the
  complex structure exists only for a Lorentzian 4-block, verified robust across
  ambient `(7,7)`, `(9,5)`, `(3,11)`, `(11,3)`, `(5,9)`. Ambient-independent, so it
  survives the open `SIGNATURE-AMBIENT` fork rather than depending on it.
- **Section 6, the `c1` constraint.** `Td = A-hat * exp(c1/2)`; on a 4-manifold
  `Td - A-hat = c1^2/8`; `A-hat(K3) = Td(K3) = 2`. Any future claim that a holonomy
  reduction moves the generation count must first exhibit `c1 != 0`.
