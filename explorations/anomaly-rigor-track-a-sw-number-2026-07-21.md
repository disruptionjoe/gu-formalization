---
title: "ANOMALY-RIGOR Track A: the sigma-FREE, minimum-sufficient shot at rigorously EXCLUDING ANOMALY-TRIVIAL, per the anomaly-rigor scoping's rung-1. TEST: does a w1(L_time)-monomial Stiefel-Whitney number of the observerse 14-geometry SURVIVE the forgetful map Omega^{Pin+}_14 -> Omega^O_14? (Thom: Omega^O is FULLY detected by SW numbers, so a nonzero w1-monomial => sigma != 0 in Omega^O_14 => sigma != 0 in Omega^{Pin+}_14 via the forgetful homomorphism => ANOMALY-TRIVIAL excluded, WITHOUT the group order and WITHOUT the sigma-circular deck action.) VERDICT: Track A VANISHES from committed structure -> ANOMALY-TRIVIAL remains INCONCLUSIVE (neither excluded nor trivialized). The decisive committed fact: sigma = w1(L_time) is the pullback of the degree-1 generator of H^*(F;Z/2) with F ~ RP^3 (the spin double cover S^3=Sp(1)->RP^3~F, wave-swing1 Members 3/4, EXACT), and H^*(RP^3)=F_2[a]/(a^4), so sigma^4 = 0 (COMMITTED, EXACT). Consequences, all machine-computed: (i) the pure power w1(L)^14 = sigma^14 = 0 -- the only FULLY-committed w1-monomial vanishes; (ii) a Kunneth collapse on the parallelizable base (TRP^3 trivial) forces the ONLY surviving w1-monomial family to be sigma^3 * P_11(w(TY)) = a degree-11 SW number of the 14-geometry's 11-dim COMPLEMENT Y; (iii) a genuine COMPLETE enumeration of all degree-14 w1(L)-monomials on the concrete committed-consistent Pin+ representative RP^3 x RP^11 returns ALL ZERO. The survivor sigma^3*P_11(w(TY)) is not a function of committed data -- it depends on the un-committed bordism class [Y] in Omega^{Pin+}_11 (the deck/fiber structure), which IS the T2 object. So the sigma-free SW route's entire committed reach = the pure powers of sigma = forced 0 by sigma's 3-DIMENSIONAL base origin, and every candidate-firing monomial is T2-gated. Track A therefore COLLAPSES BACK onto the sigma-circular T2 class-gate. Anti-toy DISCRIMINATION holds: the instrument FIRES on the genuine w1-generators (w1(L)^14[RP^14]=1, w1(L)^4[RP^4]=1 with RP^4 Pin+) and returns 0 on a trivial input, so the vanish is a REAL finding about sigma's geometry, not a vacuous instrument. GRADE: does NOT make sigma's anomaly-protection rigorous; does NOT trivialize it either. Rigorous exclusion still waits on external operator-grade deck input (or rung-2: the Pin+ eta-invariant on sigma's deck geometry -- the SW-blind ker(forgetful) torsion, like the Z/16 at n=4 = an ABK eta-invariant, not an SW number)."
status: active_research
doc_type: exploration
created: 2026-07-21
outcome: "VANISH -> ANOMALY-TRIVIAL INCONCLUSIVE (Track A cannot fire from committed structure; the sigma-free SW route collapses onto the sigma-circular T2 class-gate; NOT excluded, NOT trivialized)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
directed_by: "Joe direct chat, 2026-07-21 (run Track A from the anomaly-rigor scoping; minimum-sufficient sigma-FREE shot at excluding ANOMALY-TRIVIAL; one foreground pass, deterministic, no commit/push)"
inputs:
  - explorations/anomaly-rigor-approach-scoping-2026-07-21.md
  - explorations/pin-bordism-cardinality-2026-07-21.md
  - explorations/operator-grade-anomaly-banking-2026-07-21.md
  - explorations/pin14-anomaly-number-2026-07-21.md
  - explorations/wave-swing1-the-lemma-2026-07-21.md
  - canon/source-action-seiberg-witten-construction.md
  - tests/channel-swings/pin_bordism_cardinality_probe.py
  - tests/channel-swings/pin14_anomaly_number_probe.py
probe: tests/channel-swings/anomaly_rigor_track_a_probe.py (foreground, deterministic/no-RNG, exact mod-2 cohomology-ring arithmetic, EXIT 0, double-run byte-identical, 23/23 PASS)
---

# ANOMALY-RIGOR Track A -- the w1-SW-number survival check

Single foreground pass, maximum honesty about grade. This runs **Track A** from
`anomaly-rigor-approach-scoping-2026-07-21.md` (rung 1): the **minimum-sufficient,
sigma-FREE** shot at rigorously excluding `ANOMALY-TRIVIAL` **without** the group order
`|Omega^{Pin+}_14|` and **without** the sigma-circular T2 deck action. Everything is
CONDITIONAL on the proposal-grade anomaly-inflow identification (`sigma` = the `w1`
reflection/`T` `Z/2`, receptacle `Omega^{Pin+}_14`); nothing here promotes it -- it is
consumed.

## 0. Verdict up front

> **OUTCOME: Track A VANISHES from committed structure -> `ANOMALY-TRIVIAL` stays
> INCONCLUSIVE** (neither excluded nor trivialized). No `w1(L_time)`-monomial
> Stiefel-Whitney number fires on `sigma`'s geometry using committed structure, and the
> **reason is structural, not numerical accident**: the committed reach of `sigma` is
> exactly its pure powers, and those are forced `0` by `sigma`'s **3-dimensional base
> origin**.
>
> - **The test.** The forgetful map `f: Omega^{Pin+}_14 -> Omega^O_14`. Unoriented
>   bordism `Omega^O_*` (of manifolds-with-a-real-line-bundle, i.e. `Omega^O_*(BZ/2)`) is
>   **completely detected by Stiefel-Whitney numbers** (Thom). So if **any**
>   `w1(L_time)`-monomial SW number of `sigma`'s representative is **nonzero**, then
>   `sigma != 0` in `Omega^O_14`, hence `sigma != 0` in `Omega^{Pin+}_14` (a nonzero image
>   under the forgetful HOMOMORPHISM forces a nonzero domain element) -- `ANOMALY-TRIVIAL`
>   **rigorously excluded**, `sigma`-free.
> - **The decisive committed fact.** `sigma = w1(L_time)` is the deck `Z/2` of the spin
>   double cover `S^3 = Sp(1) -> RP^3 ~ F`, `= pi_1(RP^3) =` the Cech-`H^1` descent
>   obstruction (`wave-swing1` Members 3/4, tagged **EXACT**). So `sigma` is the **pullback
>   of the degree-1 generator of `H^*(F;Z/2)`**, and `H^*(RP^3;Z/2) = F_2[a]/(a^4)`. Hence
>   **`sigma^4 = 0`** (COMMITTED, EXACT).
> - **What that forces (all machine-computed).**
>   1. **The pure power `w1(L)^14 = sigma^14 = 0`.** The only *fully-committed*
>      `w1`-monomial (a pure power of `sigma`) **vanishes**.
>   2. **Kunneth collapse.** `TRP^3` is trivial (`RP^3 ~ SO(3)` parallelizable, `w(TRP^3)=1`),
>      so on `M = RP^3 x Y^11` the base contributes only `sigma^k` (`k <= 3`) and
>      `<sigma^k * T, [M]> = [k=3] * <T,[Y]>`. The **only** surviving `w1`-monomial family
>      is `sigma^3 * P_11(w(TY))` -- a **degree-11 SW number of the 11-dim complement `Y`**.
>   3. **Complete enumeration.** On the concrete committed-consistent Pin+ representative
>      `M = RP^3 x RP^11` (14-dim, `w2(TM)=0`), a GENUINE complete enumeration of every
>      degree-14 `w1(L)`-monomial returns **ALL ZERO**.
> - **Why VANISH, not exclusion.** The survivor `sigma^3 * P_11(w(TY))` is **not a function
>   of committed data**: it depends on the un-committed bordism class `[Y]` in
>   `Omega^{Pin+}_11` (the deck/fiber structure), which **is the T2 object**. So the
>   `sigma`-free SW route's entire committed reach = the pure powers of `sigma` = forced `0`,
>   and **every candidate-firing monomial is T2-gated.** Track A **collapses back onto the
>   sigma-circular T2 class-gate.**
> - **Grade (honest).** This does **NOT** make `sigma`'s anomaly-protection rigorous. It
>   also does **NOT** trivialize it: a vanish only says `sigma`'s **image** in `Omega^O_14`
>   is zero; `sigma` may live in `ker(f) =` the Pin+ **torsion** that SW numbers miss (the
>   `Z/16` at `n=4` is an **ABK eta-invariant, not an SW number**). Rigorous exclusion still
>   waits on **external operator-grade deck input** (or rung-2: the Pin+ eta-invariant on
>   `sigma`'s deck geometry).

Probe: `tests/channel-swings/anomaly_rigor_track_a_probe.py` -- foreground, exact mod-2
cohomology-ring arithmetic, **DETERMINISTIC (no RNG)**, **EXIT 0**, double-run
**byte-identical**, **23/23 PASS**.

## 1. Pre-declared kill-conditions (written BEFORE computation)

- **KILL-A (instrument, anti-toy):** the `w1`-detector must **discriminate** -- FIRE (`=1`)
  on the genuine `w1`-generators (`w1(L)^14[RP^14]`, `w1(L)^4[RP^4]`) and return `0` on a
  known-trivial input. If it fails to separate, the instrument is broken -> discard.
- **DECISION (FIRE):** `ANOMALY-TRIVIAL` counts as **EXCLUDED** only if a `w1(L_time)`-monomial
  SW number is certified **nonzero from committed structure** (`sigma = w1`, the observerse
  characteristic numbers) -- i.e. **independent of the T2-gated deck representative**.
- **DECISION (VANISH):** if every committed `w1`-monomial is `0`, report **INCONCLUSIVE** --
  do **not** over-claim a vanish as either exclusion (it is not: `ker(f)` torsion is
  SW-blind) or trivialization (it is not: `w1 != 0` does not force the bordism class to
  vanish).
- **Pre-declared expectation:** the pure powers likely die (`sigma` sits on a low-dim base);
  the mixed survivors likely T2-gated; so Track A likely **VANISHES from committed structure**
  and rigorous exclusion stays gated -- but the instrument must be shown to be capable of
  firing, so the vanish is a real finding.

<!-- RESULTS BELOW WERE WRITTEN AFTER RUNNING THE PROBE -->

## 2. The instrument discriminates (KILL-A cleared)

Exact mod-2 cohomology-ring arithmetic in `H^*(prod_i RP^{c_i}) = F_2[a_i]/(a_i^{c_i+1})`;
SW number = coefficient of the top monomial `(c_0,..)` (the fundamental-class pairing).

- **FIRES on the degree-14 `w1`-generator:** `w1(L)^14[RP^14] = 1` (`RP^14` with its
  tautological line = the `w1`-generator of `Omega^O_14(BZ/2)`). The instrument **can output
  1**. *Honest note:* `RP^14` is **Pin-**, not Pin+ (`w2(TRP^14) = C(15,2) = 1 != 0`) -- so
  it is an **instrument control**, not a Pin+ representative (exactly the T2-gate flagged in
  `pin14_anomaly_number_probe` C8).
- **FIRES on a Pin+ manifold:** `w1(L)^4[RP^4] = 1` and `RP^4` **is Pin+** (`w2 = C(5,2) = 0`,
  the `Z/16` flavor). So a Pin+ manifold **can** carry a firing `w1`-monomial (in dim 4) --
  the detector is not vacuously zero on the Pin+ side.
- **VANISHES on a trivial input:** `L` trivial (`w1(L) = 0`) -> every `w1`-monomial `= 0`.

With FIRE-on-generators and 0-on-trivial, the instrument **separates** trivial from
generator; a vanish on `sigma`'s geometry is therefore a real finding, not a tautology.

## 3. The decisive committed fact: `sigma^4 = 0`

`sigma = w1(L_time)` is, at committed grade, the pullback of the degree-1 generator `a` of
`H^*(F;Z/2)` with `F ~ RP^3` (the spin double cover `S^3 = Sp(1) -> RP^3 ~ F`; `wave-swing1`
Members 3/4, **EXACT** at the topological level -- "the deck `Z/2` IS a `w1`"). Since
`H^*(RP^3;Z/2) = F_2[a]/(a^4)`:

    sigma^0..sigma^3  nonzero  (a^0..a^3),      sigma^{>=4} = 0.

The probe verifies `sigma^k` is nonzero **iff** `k <= 3`, and in particular
**`w1(L)^14 = sigma^14 = 0`**. This is the load-bearing input: **the only fully-committed
`w1`-monomial -- a pure power of `sigma` -- vanishes**, because `sigma` originates on a
**3-dimensional** base and cannot be raised to the degree needed to detect a 14-dim class.

## 4. The Kunneth collapse: the only survivor is `sigma^3 * P_11(w(TY))`

The base `F ~ RP^3 ~ SO(3)` is a Lie group, **parallelizable**, so `w(TRP^3) = 1`: **all**
tangent SW classes of the 14-geometry come from the 11-dim complement `Y`, and the base
contributes **only** powers of `sigma` (`<= 3`). On `M = RP^3 x Y^11`,

    < sigma^k * T , [RP^3 x Y] >  =  < a^k, [RP^3] > * < T, [Y] >  =  [k == 3] * < T, [Y] >.

So a degree-14 `w1`-monomial `sigma^k * T` (`T` a tangent monomial of degree `14 - k`) can be
nonzero **only** for `k = 3` (probe: `<sigma^k * top_Y, [M]> = 1` iff `k = 3`). Combined with
`sigma^{>=4} = 0` (Section 3), the **entire** surviving `w1`-monomial family is

    sigma^3 * P_11(w(TY))   =   a degree-11 Stiefel-Whitney number of the complement Y.

Everything else in the degree-14 `w1`-monomial set is forced `0` by committed structure.

## 5. The actual evaluation (complete enumeration) -> ALL ZERO

On the concrete **committed-consistent Pin+ representative** `M = RP^3 x RP^11`
(`w(TM) = 1 + a1^4 + a1^8`, so `w1(TM) = 0`, `w2(TM) = 0` -> Pin+, in fact Spin; `sigma`
pulled from the `RP^3` base), the only nonzero tangent SW classes are `w4 = a1^4` and
`w8 = a1^8`. A **genuine complete enumeration** of every degree-14 `w1(L)`-monomial
`sigma^k * w4^x * w8^y` with `k + 4x + 8y = 14`, `k >= 1`:

| monomial | value | why 0 |
|---|---|---|
| `sigma^14` (the pure power) | 0 | `sigma^{>=4} = 0` |
| `sigma^6 w8` | 0 | `sigma^{>=4} = 0` |
| `sigma^10 w4` | 0 | `sigma^{>=4} = 0` |
| `sigma^6 w4^2` | 0 | `sigma^{>=4} = 0` |
| `sigma^2 w4 w8` | 0 | tangent hits `a1^12 = 0` on `RP^11` |
| `sigma^2 w4^3` | 0 | tangent hits `a1^12 = 0` on `RP^11` |

**Every degree-14 `w1(L)`-monomial SW number `= 0`.** (The two `k=2` survivors would need
`sigma^3` to pair on the base *and* a degree-11 tangent number on `RP^11`; `RP^11` has no
degree-11 tangent number -- `4x + 8y = 11` is unsolvable -- so they die on the complement
side too.) This concrete admissible completion of the observerse geometry gives **Track A
VANISH**.

## 6. Why VANISH is INCONCLUSIVE, not exclusion and not trivialization

The survivor `sigma^3 * P_11(w(TY))` is a **degree-11 SW number of the 11-dim complement `Y`**.
Committed structure fixes `sigma` (and `sigma^4 = 0`) but **not** the bordism class `[Y]` in
`Omega^{Pin+}_11` -- that is the **deck/fiber data = the T2 object** (`operator-grade-anomaly-banking`
T2; `pin14-anomaly-number` C8). It does not even fix `w1(TY)` (the `RP^11` completion is Spin,
`w1(TY) = 0`; the true observerse complement's orientation and high SW classes are
un-committed). So:

- **The only committed-determined `w1`-monomials** (those with `sigma`-exponent `>= 4`,
  including the pure power `w1(L)^14`) **are all `0`** (probe C5).
- **Every candidate-firing monomial** (`sigma`-exponent `<= 3`, i.e. the `sigma^3 * P_11`
  family) **is T2-gated.**

Hence **Track A cannot FIRE from committed structure**: the `sigma`-free SW shot's committed
reach is exactly the pure powers of `sigma`, forced `0` by `sigma`'s 3-dimensional base
origin, and its firing monomials all sit behind the T2 class-gate. **The `sigma`-free route
collapses back onto the sigma-circular T2 wall** -- precisely the honest caveat the scoping
pre-declared for rung 1.

**This is INCONCLUSIVE, held between two forbidden over-claims:**

- **NOT exclusion.** A vanish says only that `sigma`'s *image* in `Omega^O_14` is zero.
  `sigma` may live in `ker(f) =` the Pin+ **torsion** that SW numbers cannot see -- exactly
  the `Z/16` at `n = 4`, which is an **ABK eta-invariant, not an SW number**. So a vanish
  does not exclude `ANOMALY-TRIVIAL`.
- **NOT trivialization.** A vanish also does not *prove* `sigma = 0`: `w1 != 0` in `H^1` does
  not force the bordism class to bound, and the eta-detected torsion is invisible here. So a
  vanish does not establish `ANOMALY-TRIVIAL` either.

## 7. Logical strength of each branch (the exact grade)

- **FIRE branch (NOT realized this pass):** a nonzero `w1(L)`-monomial SW number of `sigma`'s
  representative `=> sigma != 0` in `Omega^O_14(BZ/2)` (Thom) `=> sigma != 0` in
  `Omega^{Pin+}_14` (nonzero image under the forgetful homomorphism). **Strength:** this
  would prove `sigma != 0` in the receptacle **directly and `sigma`-free** -- no group order,
  no deck action -- a genuine rigorous exclusion of `ANOMALY-TRIVIAL`. The scoping's rung-1
  logic is **correct**; it simply does not fire on `sigma`'s committed geometry.
- **VANISH branch (realized):** `INCONCLUSIVE` -- see Section 6. Rigorous exclusion of
  `ANOMALY-TRIVIAL` **cannot be completed from committed structure** and waits on breaking
  the T2 class-gate non-circularly (external operator-grade deck input), or on **rung 2**:
  the Pin+ eta-invariant on `sigma`'s deck geometry (the SW-blind detector of the
  `ker(f)` torsion) -- both T2-gated / larger, exactly as the scoping placed them.

## 8. Contribution and honest ledger

**Contribution.** A genuine, `sigma`-free, minimum-sufficient run of Track A: it enumerates
and evaluates the `w1(L_time)`-monomial Stiefel-Whitney numbers of the observerse
14-geometry against the forgetful map `Omega^{Pin+}_14 -> Omega^O_14`, and delivers a
**decisive structural negative** -- the sigma-free SW shot **cannot fire from committed
structure**, because `sigma`'s committed reach is its pure powers and those die at `sigma^4`
(the 3-dimensional base origin `F ~ RP^3`), while every candidate-firing monomial is a
degree-11 SW number of the un-committed, T2-gated 11-dim complement. This is stronger than
"a number came out zero": it locates **why** the cheap `sigma`-free route is blocked (a
dimensional mismatch -- `sigma` reaches degree 3, detection of a 14-class needs 11 more
degrees living in the gated fiber) and shows Track A collapses back onto the same
sigma-circular T2 wall the operator-grade swing pinned.

- **EXACT (machine-computed):** `sigma^4 = 0` from `H^*(F ~ RP^3) = F_2[a]/(a^4)`; the pure
  power `w1(L)^14 = 0`; the Kunneth collapse `<sigma^k T,[M]> = [k=3]<T,[Y]>` on the
  parallelizable base; the complete degree-14 `w1`-monomial enumeration on `RP^3 x RP^11`
  returning all zero; the instrument discrimination (`RP^14`, `RP^4` fire; trivial `-> 0`);
  the Pin+ flavor criterion `w2 = 0` (`RP^4` Pin+, `RP^2` Pin-, `RP^14` Pin-).
- **DERIVED / STRUCTURAL:** the survivor family `= sigma^3 * P_11(w(TY))`; its value `=` a
  degree-11 SW number of the complement `Y`; committed data determines only the pure powers
  (all `0`), so **no committed `w1`-monomial fires**.
- **GATED / OPEN (named, not papered):** `sigma`'s specific 14-class -- the bordism class
  `[Y]` in `Omega^{Pin+}_11` (the deck/fiber structure) is the **T2 object** (`sigma`-circular
  at operator grade); rung-2's Pin+ eta-invariant on `sigma`'s deck geometry (the SW-blind
  `ker(f)` torsion detector). These are what a rigorous exclusion still needs.
- **Falls (do not ship):** "Track A excludes `ANOMALY-TRIVIAL`" (it VANISHED); "the vanish
  trivializes `sigma`" (SW-blind `ker(f)` torsion is invisible here); "`sigma`'s protection
  is now rigorous" (it is not -- the sigma-free shot collapses onto the T2 gate).

## 9. Boundary

Exploration tier. Only two NEW files written -- this document and the probe
`tests/channel-swings/anomaly_rigor_track_a_probe.py` (foreground, exact mod-2
cohomology-ring arithmetic, **DETERMINISTIC (no RNG)**, **EXIT 0**, double-run
**byte-identical**, **23/23 PASS**; kill-conditions declared in Section 1 BEFORE the probe
was run). GU otherwise read-only. **No commit, no push** (the coordinator commits with
explicit paths). No edit to LANE-STATE, research-portfolio, NEXT-STEPS, canon, PP1/PP2/PP3,
the anomaly-rigor scoping, `pin-bordism-cardinality`, `operator-grade-anomaly-banking`,
`pin14-anomaly-number`, the anomaly-inflow swing, `wave-swing-1`, the LP-LC receipt, or any
other agent's artifact, or any claim/canon/verdict/ledger/portfolio file. No claim-status,
canon-verdict, paper-status, or public-posture change; the externality of `sigma`/`tau`, the
receptacle `Omega^{Pin+}_14`, the verdicts `LC-SELECTOR` and `CARDINALITY-1 + PROTECTED`
(proposal), and the proposal-grade anomaly-inflow identification are **consumed, not moved or
promoted**. Track A is run as the scoping specified and reported at its true grade: a
`sigma`-free VANISH that leaves `ANOMALY-TRIVIAL` INCONCLUSIVE and returns the burden to the
T2 class-gate. Nothing routes externally (Joe alone publishes).
