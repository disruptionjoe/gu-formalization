---
artifact_type: exploration
status: exploration
doc_type: anomaly-cancellation-gate
created: 2026-08-14
work_item: AC-1
channel: anomaly_cancellation_actual_fermion_content
title: "AC-1: GU's actual spinorial content (Dirac nu + Rarita-Schwinger zeta) is perturbatively anomaly-free in 4d for EVERY horn of every open fork, and the reason is a FACTORISATION: the degree-6 anomaly polynomial of any field splits channel-by-channel into (spin/twist coefficient) x (group-theoretic invariant), and both group invariants vanish identically on a complete 16 of so(6,4). Computed exactly: d^abc = 0 on all 16215 unordered triples for the 16 of so(10), the 16 of so(6,4), the vector 10, and 10 (x) 16 = 144 (+) 16; controls (su(3) fund, so(6) spinor 4) fire NONZERO on the same machinery. The RS spin factors are DERIVED, not asserted: pure-gauge rescaling (3, 4, 5) and mixed gauge-gravitational rescaling (-21, -20, -19) for carriers A / bare / B -- reproducing the AGW/PTZ column the carrier-bit canon holds at literature-fetched grade. CONSEQUENCE, and the real deliverable: 4d anomaly cancellation has EXACTLY ZERO discriminating power over the carrier bit, the SIGNATURE-AMBIENT fork, the chirality assignment, or the multiplicities -- the map (fork horn) -> (anomaly vector) is constant on GU's content and is provably non-constant on a control. ROUTE KILLED, not candidate killed."
grade: "EXACT integer / Gaussian-integer matrix arithmetic (numpy int64, magnitudes bounded far below overflow) plus sympy Rational symbolic algebra; no floating point is load-bearing anywhere. 89/89 checks (73 [E] exact results, 13 [C] controls that must have power, 3 [T] declared table inputs), exit 0. Non-vacuity established two ways: live controls that MUST return nonzero (su(3) fundamental d^abc, so(6) spinor 4 d^abc, su(3) 3(x)3 tensor additivity, dropped charged-lepton singlet, quark doublets alone, single colour triplet Tr C8^3, rank-24 twist killing the mixed channel, odd-doublet content flipping the mod-2 verdict, 13 distinct anomaly values on the control fork sweep); and two mutation tests (drop one weight from the 16 -> 15 failures, exit 1; perturb the AGW/PTZ mixed column by one unit -> 1 failure, exit 1). Every downstream group factor is the MEASURED value from the upstream computation, never a hardcoded zero. NOT: a 14d statement, a claim about the unbuilt reduction, a generation count, a chirality-production claim, or any claim-status movement."
disposition: GU_RS_CONTENT_PERTURBATIVELY_ANOMALY_FREE_IN_4D_FOR_EVERY_CARRIER_AND_MULTIPLICITY__BY_FACTORISATION_THROUGH_VANISHING_GROUP_INVARIANTS__ANOMALY_CANCELLATION_HAS_ZERO_SELECTOR_POWER_OVER_THE_CARRIER_BIT_SIGNATURE_FORK_AND_CHIRALITY_ASSIGNMENT__ROUTE_KILLED_NOT_CANDIDATE_KILLED
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md
  - explorations/dk-chirality-fork-2026-07-20.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - explorations/verify-anomaly-closure-2026-07-20.md
  - explorations/internal-paths-2026-07-03/anomaly-sp64-i16-daifreed.md
  - explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md
  - explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
  - lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md
  - canon/carrier-bit-decision-campaign-RESULTS.md
  - canon/gamma-traceless-38-adjudication-RESULTS.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - canon/exhaustiveness-by-type-RESULTS.md
  - canon/shiab-existence-cl95.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
scripts:
  - tests/channel-swings/joe_directed_anomaly_cancellation_probe.py
---

# AC-1 — the Rarita-Schwinger content cannot obstruct, and anomalies cannot select

## 0. Prior-art sweep first (this route is the most heavily pre-owned of the wave)

Swept by MECHANISM (anomaly, index density, Dai-Freed, bordism, eta invariant,
Green-Schwarz, Witten anomaly, global/gravitational/mixed anomaly, cobordism,
cubic Casimir, anomaly coefficient), not by label. What the sweep found, and how
much of this route it already owns:

| already owned | owner | what it owns |
|---|---|---|
| the **14d local** leg (`I_16`, `tr R^8`, Green-Schwarz reducibility) | `explorations/dk-chirality-fork-2026-07-20.md`; `explorations/internal-paths-2026-07-03/anomaly-sp64-i16-daifreed.md`; MOVE-1 | the whole degree-16 anomaly polynomial on `Y14`, the `-13` net chirality of the C0 truncation, the branch table C0..C5c, the `W = 0` balanced branches |
| the **14d global** leg (Dai-Freed / eta / spin bordism) | `explorations/global-anomaly-leg-2026-07-20.md`; `lab/active-research/anomaly/sp1-2primary-dai-freed-gate-2026-07-06.md` | `Omega^spin_15 = 0`, `Omega~^spin_15(BSp(64)) = 0`, `KO_15 = KSp_15 = 0`, odd-primary arena empty for every `Sp(n)`, the 2-primary AHSS front-page gate, the `pi_4(Sp)` Witten slot killed by even quaternionic multiplicity |
| the adversarial re-verification of both legs | `explorations/verify-anomaly-closure-2026-07-20.md` | second dry round, VERDICT DRY, 56 independent re-derivations |
| the **14d local system solved wholesale** | `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md` | rank 5 on a 15-dim content lattice, kernel dim 10, `W = 0` derived not assumed, gauge-group fork proved irrelevant to the local row |
| **the four SM anomaly zeros of the chiral 16 (spin-1/2)** | `explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md`; `tests/one-residual/sm_mirror_anomaly_free.py`; `tests/W224_falsify_nielsen_ninomiya_chirality.py` | `U(1)^3 = 0`, `grav^2-U(1) = 0`, `SU(2)^2-U(1) = 0`, `SU(3)^3 = 0`; Witten `SU(2)` absent (4 doublets, even); the Pati-Salam hypercharge match |
| the `-21 / -20 / -19` and `-42 / -40 / -38` column | `canon/carrier-bit-decision-campaign-RESULTS.md`; `canon/gamma-traceless-38-adjudication-RESULTS.md` | the carrier bit itself, at literature-fetched grade (PTZ PRD 106 (2022) 025022; Homma-Semmelmann eq (11), Prop 3.1(i); Bilal eq 11.47; Baer-Mazzeo) |
| "nothing routes around SG4" | `canon/exhaustiveness-by-type-RESULTS.md`; `canon/gu-forces-field-space-declaration-RESULTS.md` | the decider is unique; GU-as-stated leaves a measured 2-bit SG4 residual |
| "an anomaly/GS carrier is not a source-action selector" | `absorbed/gu-source-action/ANOMALY-GREEN-SCHWARZ-CARRIER-PACKET-2026-07-05.md` | "No closedness is earned" for the anomaly/GS carrier channel |

**Honest accounting: roughly 40% of this route was already owned.** In
particular the spin-1/2 half of the headline — a chiral 16 of `SO(10)` has
vanishing SM anomaly coefficients — is fully owned by W222 and by
`sm_mirror_anomaly_free.py`, and both the 14d local and 14d global legs are
owned, computed, and adversarially re-verified. **This artifact does not
re-claim any of that.**

Three things the sweep found were **NOT** owned, and they are what AC-1 adds:

1. **The mechanism was asserted, never computed.** W222's own grade line says
   "the `SO(10)`-16 anomaly-freedom ... flagged FROM-MEMORY where standard", and
   `W224_falsify_nielsen_ninomiya_chirality.py` prints "Spin(10) has no cubic
   Casimir" as a label. No probe in the repository builds the 45 generators of
   `so(10)` and evaluates `d^abc`. AC-1 computes it on all 16215 unordered
   triples, for `so(10)` **and** for the actual internal real form `so(6,4)`,
   with a discriminating control (`so(6)` spinor 4 NONZERO next to `so(8)`/`so(10)`
   spinor ZERO).
2. **The Rarita-Schwinger layer of the 4d anomaly did not exist.** Every anomaly
   computation in the repository is degree-16 on `Y14`. There is no degree-6 (4d)
   anomaly polynomial anywhere, and no treatment of `zeta` as an anomaly source
   at all — the 4d work treats the content as spin-1/2. AC-1 derives the RS
   spin factors from the twist character and shows the carrier bit rescales the
   two anomaly channels by `(3, 4, 5)` and `(-21, -20, -19)`.
3. **The selector question was never asked in this channel.** The exhaustiveness
   canon enumerated *odd-primary obstruction types*; the 4d perturbative gauge
   anomaly is not among them. AC-1 closes it, exactly.

## 1. Preflight — six specialist lenses, each proposing a route

Run inline in this one worker (standing rule: N lenses means N sections written
here, never N subagents). Each lens **proposes a route**; the routes are then
ranked and one is taken.

### Lens 1 — Index theorist

The 4d anomaly of a chiral field is the degree-6 part of an index density, and
index densities are *multiplicative*: `I = [Ahat(R) * (twist character) *
ch_R(F)]_6`. That multiplicativity is the whole game. **Proposed route: do not
compute "the anomaly of GU's content" as a lump. Compute the twist character
and the gauge character separately and read off which channel each factor can
possibly touch.** The prediction is that `Ahat` and the twist character depend
only on the tangent bundle, so they can never produce a `tr F^3`; the group
theory enters exactly twice, as `Tr_R X^3` and `Tr_R X`. If both group factors
vanish the spin side is irrelevant no matter what it is. This lens says the
answer is decidable in one page and that the interesting output is not the zero
but the *factorisation*.

### Lens 2 — Dai-Freed / bordism specialist

The perturbative anomaly is the free part; the torsion part lives in
`Hom(Tors Omega_{d+1}, R/Z)`. **Proposed route: skip the free part entirely and
go straight to the 5d torsion receptacle `Omega^spin_5(B G_SM)` with the RS
content, since that is where a higher-spin field could still bite.** This lens
must be told, and is told, that the repo already owns the 15d/`BSp` side
(`sp1-2primary-dai-freed-gate`, `global-anomaly-leg`) and that R2 already
recorded the 5d SM shadow. Its residual proposal survives as the *second*
gate: whether the RS multiplicity changes the mod-2 class. AC-1 answers the
computable shadow of that (doublet parity) and declares the rest out of scope.

### Lens 3 — Rarita-Schwinger / higher-spin specialist

The RS field is not "spin-1/2 with a vector index". Its anomaly density is
`Ahat(R) * (tr e^R + q)` where `q = -1` for the ghost-subtracted gravitino,
`q = 0` bare, `q = +1` for the geometric gamma-traceless operator — precisely
the repo's carrier bit. **Proposed route: compute the 4d degree-6 coefficients
for general `q` and see whether the two channels rescale by the SAME factor.**
If they rescale differently, the carrier bit is in principle observable in the
*ratio* of gauge to mixed anomaly, which would be the first observable
consequence of the carrier bit outside the K3 index. This is the sharpest
proposal in the preflight and it is the one taken.

### Lens 4 — Chiral-gauge-theory anomaly specialist

Anomaly cancellation is a statement about the *chiral* content, and a
vectorlike content is trivially anomaly-free. **Proposed route: before
computing anything, type the content — is GU's 4d content chiral or
vectorlike?** W222 already logged that the raw carrier is `16 + 16bar`
(vectorlike, trivially zero) and that the nontrivial statement is about the
surviving chiral 16. This lens issues the binding warning that a zero obtained
on a vectorlike content is worthless, and demands that the computation be
performed on a single complete 16 so that the zero is the nontrivial kind. It
also demands the standard controls: drop `e^c` and the zero must break.

### Lens 5 — Real-form and signature specialist

`Y14` is `Met(X4)`; the SIGNATURE-AMBIENT fork is open between `(7,7)` and
`(9,5)`, but both horns share the internal `Spin(6,4)`. **Proposed route:
compute every group invariant on `so(6,4)` directly, not on the compact
`so(10)`, and check whether the real form matters.** The prediction is that it
cannot — `d^abc` is a polynomial identity in the complexified algebra — but the
prediction must be certified rather than asserted, because the repository's own
discipline forbids inferring a real-form-independent statement from a compact
computation. AC-1 computes both.

### Lens 6 — Honesty auditor

This route has the highest prior-art density in the wave. **Proposed route:
run the sweep first and, if the substance already exists, report that plainly
and stop.** The auditor's binding conditions, fixed before computing:
(a) any zero must be accompanied by a control that returns nonzero on the same
machinery, or it is not reportable; (b) no downstream quantity may be multiplied
by a hardcoded zero, because `x * 0 == 0` is an unconditional PASS and the repo
runs a `certificate_shape_audit` that flags exactly that shape; (c) the
`-21/-20/-19` numbers are already in canon at literature-fetched grade and must
be attributed, not re-claimed; (d) no count may be inferred from the branching
`S^+(14) -> (2_L,16) + (2_R,16bar)`.

### Ranking, and what was fixed BEFORE computing

Lens 3's route is taken, with Lens 1's factorisation as the frame, Lens 5's
real form as the arena, and Lens 4's and Lens 6's conditions binding.

**Cheapest kill-or-switch condition (declared before computing).** If `d^abc`
is nonzero on any `so(6,4)` triple in the 16, the whole factorisation story
collapses and the route switches immediately to the global/Dai-Freed side where
`sp1-2primary-dai-freed-gate-2026-07-06.md` already has a foothold. Conversely,
if `d^abc` is identically zero AND the `Tr T^a` channel is identically zero,
then the perturbative anomaly is trivially zero for group-theoretic reasons and
**the route must be reported as a route-kill for the selector question, not
dressed up as a cancellation result.** That is what happened.

**One credible contrary route (declared before computing).** The contrary
construction with the best chance of surviving: `zeta` is a **1-form** on
`Y14`, so under reduction its 4d avatar is not only a 4d RS field in the 16 —
`Omega^1(Y14)` also deposits `Omega^0(X4) (x) (internal 10)`, i.e. 4d spin-1/2
towers valued in `10 (x) 16 = 144 (+) 16`. If `144` carried a nonzero cubic
invariant, GU's content would be anomalous and the whole result would invert.
This contrary route was pre-declared and is closed by direct computation in
Part 1b below, not by appeal to the classification theorem.

## 2. The swing — what was computed, exactly

Probe: `tests/channel-swings/joe_directed_anomaly_cancellation_probe.py`,
**89/89 checks, exit 0** (73 `[E]` exact results, 13 `[C]` controls that must
have power, 3 `[T]` declared table inputs).

### 2.1 The group factors vanish — computed, not cited

Built the Clifford algebra over the Gaussian integers, verified
`{Gamma_a, Gamma_b} = 2 eta_ab` exactly, **derived** the chirality operator
(`Gamma_1...Gamma_10 = i^5 sigma_3^{(x5)}`) rather than assuming it, verified
all 2025 commutators close with the exact `so(10)` structure constants, and
then evaluated `d^abc = Tr(T^a {T^b, T^c})` on every unordered triple:

| representation | triples | `d^abc` | `Tr T^a` |
|---|---|---|---|
| **16 of `so(10)`** | 16215 | **all 0** | all 0 |
| **16 of `so(6,4)`** (GU's internal real form) | 16215 | **all 0** | all 0 |
| vector **10** of `so(6,4)` | 16215 | all 0 | all 0 |
| **`10 (x) 16` = `144 (+) 16`** of `so(6,4)` | 16215 | **all 0** | all 0 |
| `8_s` of `so(8)` | 4060 | all 0 | all 0 |
| **CONTROL: 3 of `su(3)`** | 120 | **NONZERO** (max 12) | — |
| **CONTROL: 4 of `so(6)`** | 680 | **NONZERO** | — |
| **CONTROL: `3 (x) 3` of `su(3)`** | 120 | **NONZERO** (max 72 = 6 x 12) | — |

The `so(6)` control is the load-bearing one: the *same* Clifford machinery, on
the *same* kind of chiral spinor of an even orthogonal algebra, returns a
nonzero cubic invariant. So the `so(10)` / `so(6,4)` zero is content, not an
artefact of the construction. The `so(6)` NONZERO next to `so(8)`/`so(10)` ZERO
is a real discrimination inside the `so(2n)` spinor family.

The `10 (x) 16` row closes the pre-declared contrary route: `zeta`'s
reduction-induced tower is anomaly-free too, by direct computation on the
160-dimensional rep, and the `su(3) 3 (x) 3` control proves the tensor
machinery can see a nonvanishing cubic invariant and reproduces the additivity
law `d_{A(x)B} = dim(B) d_A + dim(A) d_B`.

### 2.2 The spin factors — derived, and they are the carrier bit

Expanded `Ahat` from Chern roots (degree-0 term 1, degree-4 term `-p1/24`) and
the twist character `ch(T_C) = 4 + p1 + ...` for a 4-manifold, then read the
degree-6 part of `[Ahat * twist * ch_R(F)]`:

| field | twist | `t0` | pure-gauge coeff | mixed grav coeff | gauge ratio | mixed ratio |
|---|---|---|---|---|---|---|
| Dirac `nu` (spin-1/2) | `1` | 1 | `1/6` | `-1/24` | 1 | 1 |
| RS `zeta`, **carrier A** | `T_C - 1` | 3 | `1/2` | `7/8` | **3** | **-21** |
| RS `zeta`, bare control | `T_C` | 4 | `2/3` | `5/6` | **4** | **-20** |
| RS `zeta`, **carrier B** | `T_C + 1` | 5 | `5/6` | `19/24` | **5** | **-19** |

The `(-21, -20, -19)` column is **derived here from the twist character**, and
it reproduces exactly the column the carrier-bit canon holds at
literature-fetched grade (PTZ `-19 = -21 + 2`, `-21 = -20 - 1`, `-19 = -20 + 1`;
Homma-Semmelmann eq (11); Bilal eq 11.47). **This artifact does not claim those
numbers as new** — it claims the derivation route and the 4d gauge-channel
reading. Control with power: a rank-24 twist kills the mixed channel exactly, so
the formula is not a machine that always returns a negative multiple; and a
one-unit perturbation of the column makes the probe exit 1 (mutation test M2).

Also computed exactly: **there is no degree-6 pure-gravitational term for any
carrier** — no 4d pure gravitational anomaly, as expected, but computed rather
than asserted.

### 2.3 The factorisation identity, and the consequence

For **any** twist `T0 + T1 p1`, the degree-6 anomaly is exactly

```text
(spin coefficient) * Tr_R X^3  +  (spin coefficient) * p1 Tr_R X
```

with **zero residue** — verified symbolically with free symbols. So every
field's anomaly factorises, channel by channel, into a spin/twist datum times a
group-theoretic invariant. With the group invariants of 2.1 measured to be zero
and fed downstream as *measured values* (never as hardcoded zeros):

> **For GU's declared content — `n_nu` Dirac `nu` plus `n_zeta` Rarita-Schwinger
> `zeta`, both valued in a complete 16 of `so(6,4)` — both anomaly channels are
> identically zero as polynomials in `(n_nu, n_zeta, q)`.**

Control with power: on an *incomplete* content (the su(3) colour triplet, whose
cubic invariant was measured nonzero) a single `nu` is anomalous **and the
anomaly depends on `q`**. So GU's zero comes from the group factor, not from the
spin factor — the carrier bit is load-bearing whenever the group factor does not
vanish.

### 2.4 Independent route: explicit SM and B-L charge traces

Weights of the 16 were **derived from the Clifford Cartan** (not hand-listed),
then validated against MJ-5's already-validated conventions before use: 4 leptons
(`|B-L| = 1`) + 12 quark states (`|B-L| = 1/3`), exactly one SM singlet, and the
SM generation's electric-charge multiset. All thirteen channels are then exactly
zero:

```text
grav^2-U(1)_Y   grav^2-U(1)_(B-L)   U(1)_Y^3   U(1)_Y^2 U(1)_(B-L)
U(1)_Y U(1)_(B-L)^2   U(1)_(B-L)^3   SU(2)_L^2-U(1)_Y   SU(2)_L^2-U(1)_(B-L)
SU(3)^2-U(1)_Y   SU(3)^2-U(1)_(B-L)   Tr C8^3   Tr C8 C3^2   Tr C3^3
```

W222 owns the four SM channels. **The `U(1)_{B-L}` channels are new**, and they
carry a cross-channel deliverable: the unbroken gauged `U(1)_{B-L}` that MJ-5
hands to channel 2 (and that PV-2 locates among the 9 surviving non-SM
directions inside `k`) is **exactly anomaly-free**, in every channel, for every
carrier. Controls fire: dropping the charged-lepton singlet breaks cancellation;
the quark doublets alone are anomalous; a single colour triplet has
`Tr C8^3 = -6 != 0`.

### 2.5 Witten `SU(2)_L` mod-2, with the RS multiplicity

The 16 contains exactly 4 `SU(2)_L` doublets (counted from the derived weights).
`zeta` supplies `t0 x 4 = 12, 16, 20` doublets for carriers A / bare / B — all
even, so no Witten anomaly for any carrier. **Control with real teeth:** on an
odd-doublet content the carrier bit *does* flip the mod-2 verdict
(`q = -1 -> 3` odd, `q = 0 -> 4` even). So the mod-2 channel is not blind by
construction; it is blind here **because 4 is even**. Declared table input:
`pi_4(Spin(n)) = 0` for `n >= 7`, so `Spin(6,4)` itself carries no Witten
anomaly and only the `SU(2)_L` subgroup can.

### 2.6 The selector certificate — the actual deliverable

Enumerated 108 fork points: carrier `q in {-1, 0, +1}` x SIGNATURE-AMBIENT horn
`{(7,7), (9,5)}` x chirality assignment `{C0 chiral truncation, C1 draft-literal
full /S}` x a multiplicity grid `(n_nu, n_zeta) in {0,1,2}^2`. Fed the
**measured** group factors from 2.1 and 2.4.

- distinct anomaly vectors on GU's content: **1** (namely `(0, 0)`)
- distinct anomaly vectors on the control (same sweep, measured NONZERO su(3)
  group factor): **13**

> **The map (open fork horn) -> (4d anomaly coefficient vector) is CONSTANT on
> GU's content. Its fibres separate no horn. 4d anomaly cancellation therefore
> has exactly zero discriminating power over the carrier bit, the
> SIGNATURE-AMBIENT fork, the chirality assignment, or the multiplicities.**

The control's 13 distinct values prove the constancy is a fact about the 16 and
not about the parametrisation.

## 3. Inline hostile review

### 3.1 Strongest overclaim available (and rejected)

**"GU is anomaly-free."** Rejected three ways.

1. **Wrong dimension.** This is the 4d effective anomaly, computed *granting*
   the 14 -> 4 reduction, which the repository records as unbuilt (`cb-c`
   residue `U4`, grade T2). The 14d local `I_16` and 14d global Dai-Freed legs
   are different objects with different receptacles — the `cb-c` "anomaly"
   fence is explicit about this — and they are already owned. On the C0
   chiral-truncation branch the 14d local wall still stands (`13/37800`).
2. **Wrong sense of "free".** A vectorlike content is trivially anomaly-free,
   and W222 already logged that GU's raw carrier is `16 + 16bar`. The zero
   computed here is the *nontrivial chiral* zero (a single complete 16, a
   complex rep), but it says nothing about whether GU actually produces a chiral
   4d content. Chirality PRODUCTION remains the gap W222 identified and this
   artifact does not touch it.
3. **Wrong grade for the mechanism at large.** The computation certifies
   `d^abc = 0` for the specific reps GU uses (16, 10, `10 (x) 16`). The
   *universal* statement ("`so(10)` has no third-order symmetric invariant, so
   every rep is safe") is a declared `[T]` literature input (Okubo;
   Georgi-Glashow) that these computations instantiate but do not replace.

### 3.2 Strongest contrary construction / mistyping

The pre-declared contrary route — `zeta`'s 1-form index reducing to
`10 (x) 16 = 144 (+) 16` rather than to the 16 — was the real threat and it is
closed by direct computation (Part 1b, 16215 triples on the 160-dimensional
rep, with a tensor control that fires nonzero).

The **residual** mistyping risk, stated plainly: the identification of `zeta`'s
4d avatar as *a vector-spinor whose gravitational twist is `T_C(X4) + q`* is my
typing, driven by the canon's own carrier bit (whose `-42/-40/-38` indices are
computed on a 4-manifold's tangent bundle, which is why the `t0 = 4 + q`
matching is coherent). If SG4 declares a field space that is not of the form
`(tangent twist) (x) (gauge rep)` — for example if the gamma-trace constraint
mixes the spacetime and internal legs after reduction rather than before — the
factorisation of 2.3 still holds channel-by-channel (it holds for *any* twist),
but the identification of `t0` with `4 + q` would need re-deriving. This does
not threaten the zero (which needs only that the gauge rep is a rep of
`so(6,4)`); it threatens only the `(3,4,5)`/`(-21,-20,-19)` table's binding to
the carrier bit.

A second mistyping trap avoided: the branching
`S^+(14) -> (2_L,16) + (2_R,16bar)` is a **dimension** statement. No generation
count, chirality count, or net index is inferred from it here. AGENTS.md forbids
inferring a count from a decomposition without the index/grade map, and the
repository's own `h2-base-index-chirality` and chirality-fork records place the
net-chirality question on the far side of exactly that fork.

### 3.3 Weakest reproducibility / propagation seam

The weakest seam is **propagation, not reproduction**. The probe is
deterministic, exact, controlled, and mutation-tested. The seam is that this
result is easy to mis-relay as "GU passes the anomaly test", which would be a
frame regression across the boundary. The operative sentence that must travel
with the number is:

> The anomaly zero is a property of the 16 of `so(6,4)`, not of GU's dynamics;
> it holds for every horn of every open fork; and *because* it holds for every
> horn, it decides nothing.

A second, narrower seam: the `[T]` inputs are three and are named
(`pi_4(Spin(n)) = 0` for `n >= 7`; the Okubo/Georgi-Glashow classification; the
literature provenance of the `-21/-20/-19` column). None of them is load-bearing
for the headline — the headline rides the 16215-triple computation — but each is
load-bearing for the *generality* of the surrounding prose.

### 3.4 One thing the hostile pass found and the swing kept

The first version of the probe multiplied the downstream anomaly polynomials by
literal `0` group factors. `x * 0 == 0` is an unconditional PASS and is exactly
the shape the repo's `certificate_shape_audit` flags. Fixed: every downstream
group factor is now the **measured** maximum `|d^abc|` / `|Tr T^a|` / `|channel
trace|` from the upstream computation, so a nonzero measurement would propagate
into a nonzero polynomial and fail the checks. Mutation test M1 (drop one weight
from the 16) now produces 15 failures and exit 1.

## 4. Classification, in target-native vocabulary

| object tested | verdict |
|---|---|
| "the RS field `zeta`'s anomaly contributions could obstruct GU's fermion content" | **ROUTE KILLED.** The RS spin factors are genuinely different from spin-1/2 (3/4/5 and -21/-20/-19, derived), but they multiply group invariants that vanish identically on every rep of `so(6,4)` that GU's content occupies. No obstruction is reachable this way. |
| "4d anomaly cancellation can select the carrier bit (A vs B)" | **ROUTE KILLED**, with a certificate: the fork -> anomaly map is constant. This is a specific instantiation, in a channel the exhaustiveness canon did not enumerate, of the already-owned "nothing routes around SG4". |
| "4d anomaly cancellation can select the SIGNATURE-AMBIENT horn, the chirality assignment, or the multiplicities" | **ROUTE KILLED**, same certificate. |
| "GU's declared content is perturbatively anomaly-free in the 4d effective theory, granting the reduction" | **NOT-YET-FALSIFIED** (and now exactly certified for every carrier and multiplicity, which is strictly more than W222's spin-1/2 statement). |
| "the unbroken gauged `U(1)_{B-L}` of MJ-5 / PV-2 is anomaly-free" | **NOT-YET-FALSIFIED**, newly certified exactly in all `B-L` channels. |
| the 14d local `I_16` leg and the 14d global Dai-Freed leg | **SOURCE-SILENT for this artifact** — owned elsewhere, consumed not moved. |
| whether GU's 4d content is chiral at all (chirality production) | **TYPE-MISSING.** The reduction and the mirror-gapping mechanism are unbuilt; W222 displaced the risk here and it stays here. |
| whether `zeta`'s 4d field space is `(tangent twist) (x) (gauge rep)` | **SOURCE-SILENT.** GU's fermionic action is never stabilised (draft eq 10.10, "Caveat Emptor"); this is SG4's to declare. |

## 5. Claim ceiling

**What is claimed at exact-computation grade, unconditionally:**

- `d^abc = 0` on all 16215 unordered triples for the 16 of `so(10)`, the 16 of
  `so(6,4)`, the vector 10 of `so(6,4)`, and `10 (x) 16 = 144 (+) 16` of
  `so(6,4)`; `Tr T^a = 0` on every generator of each.
- The degree-6 anomaly polynomial factorises, for any twist, into
  `(spin coefficient) x (group invariant)` in each of exactly two channels, with
  zero residue and no 4d pure-gravitational term.
- The RS twist `T_C + q` rescales the pure-gauge channel by `4 + q` and the
  mixed gauge-gravitational channel by `q - 20`, giving `(3, 4, 5)` and
  `(-21, -20, -19)` for `q = -1, 0, +1`.
- All thirteen SM-plus-`B-L` anomaly traces on the 16 vanish exactly, and the 16
  contains exactly 4 `SU(2)_L` doublets.

**What is claimed conditionally, and on what:**

- *GU's content is perturbatively anomaly-free in 4d* — conditional on
  **granting the unbuilt 14 -> 4 reduction** and on the internal matter factor
  being complete `so(6,4)` reps. It is NOT conditional on the carrier bit, the
  signature-ambient horn, the chirality assignment, or the multiplicities, and
  that unconditionality within the fork space is the point.

**What is explicitly NOT claimed:**

- Nothing about the 14d local `I_16` or 14d global Dai-Freed legs (owned
  elsewhere; consumed, not moved).
- Nothing about chirality production, the mirror-gapping condensate, or whether
  the 4d content is chiral rather than vectorlike.
- No generation count, no net chirality, no index. The branching
  `S^+(14) -> (2_L,16) + (2_R,16bar)` is used only for dimensions.
- No movement of the carrier bit, which stays exactly where the canon puts it:
  on SG4.
- No claim-status, canon, ledger, bar, or public-posture movement.

## 6. Standard index theory vs GU-native content — the required separation

**Standard (imported machinery, would be true of any theory):** the Atiyah-Singer
/ Alvarez-Gaume-Witten anomaly-density formalism; `Ahat`; the Chern character;
the RS twist `ch(T_C) + q` and its ghost subtraction; the classification of
simple Lie algebras with a third-order symmetric invariant; `pi_4(Spin(n)) = 0`
for `n >= 7`; Witten's mod-2 multiplicity rule. **None of this is a GU result.**
`SO(10)` grand unification's anomaly-freedom is textbook, and the fact that a
complete 16 is safe is not a discovery about GU.

**GU-native (what is actually about this theory):**

1. That GU's declared content is `nu (+) zeta` with `zeta` a Rarita-Schwinger
   field — draft Sec 9.3 / eq 9.16, candidate 2B — and therefore that the
   textbook spin-1/2 anomaly argument does **not** directly apply to it. That is
   the gap AC-1 fills.
2. That the repository's carrier bit `q in {-1, 0, +1}` is *the same parameter*
   as the RS anomaly twist, so the carrier bit has a well-defined 4d anomaly
   signature `(3,4,5)` / `(-21,-20,-19)` — and that this signature multiplies
   zero on GU's actual internal group.
3. That the internal real form is `so(6,4)`, shared by both horns of the
   SIGNATURE-AMBIENT fork, so the result is fork-independent by computation
   rather than by assertion.
4. The selector certificate: **within GU's own open fork space, anomaly
   cancellation is a constant function.** This is a statement about GU's
   epistemic situation, not about anomalies, and it is the artifact's real
   contribution.

## 7. What would change this verdict

- **A source-action declaration (SG4) that puts `zeta`'s internal index outside
  `so(6,4)` reps.** If SG4 declares a field space whose gauge content is not a
  direct sum of `so(6,4)` representations, the group factors are no longer
  forced to vanish and every number here is live again. This is the only known
  route by which anomaly cancellation could regain selector power.
- **A reduction that truncates the 16.** Every control in the probe shows that
  incomplete content is anomalous *and* carrier-bit-dependent. If the 14 -> 4
  reduction, once built, delivers anything other than complete 16s, the
  factorisation immediately becomes a live constraint on the carrier bit — and
  would then be a genuine selector.
- **An odd `SU(2)_L` doublet count.** The mod-2 channel is the one place where
  the carrier bit's parity (`t0 = 3, 5` odd; `t0 = 4` even) is visible in
  principle. It is invisible here only because the 16 supplies 4 doublets.
