---
artifact_type: exploration
status: exploration
doc_type: source-mechanism-completion-gate
created: 2026-08-15
work_item: SRC-4
channel: majorana_126_neutrino_mechanism
target_claim: "The eddy / Chern-Simons quadratic completion the source insists on (`F_B + (1/2) D_B T + (1/3)[T,T]`, Portal `02:35:10`, `WGS-03`) rescues the unbounded-below Mexican-hat potential that SRC-3 exhibited."
title: "SRC-4: the eddy completion does NOT rescue the potential, and it fails for a DIFFERENT reason in each of the two readings CG-1 separated. In the eddy-SQUARED reading the completion is SIGN-INERT: it multiplies SRC-3's quartic by the strictly positive rational (b*lam)^2 -- exactly 4/9 at the source point (1/2,1/3) -- so SRC-3's -4 becomes -16/9 and CG-1's +4 becomes +16/9. No coefficient in the completion family, and neither bracket convention, can flip a sign. In the source's DISPLAYED first-order reading the completion is actively worse: it is what makes the action a Chern-Simons-type PRIMITIVE, hence ODD (cubic) in T, and an odd-degree polynomial is unbounded below independent of the pairing's signature -- so CG-1's post-reduction repair, which is a completion of SQUARE and therefore a purely even-degree device, is structurally powerless against it. Boundedness reduces to an exactly stated condition on ONE undeclared composite coefficient, kappa_1 * flat_1 >= 0, decided on precisely the abelian directions CG-1 retired as vacuous."
grade: "EXACT integer and rational arithmetic, 44/44, exit 0, no floats. SRC-3's ray (-4, +4), CG-1's B_theta Gram 2*I_45 and its two-sided Ad(K)/Ad(G) invariance price, and PV-2's Killing signature all re-run as live controls. Four planted mutations fail (39/44, 42/44, 40/44, 41/44, all exit 1), two of them aimed at the load-bearing E1 and E2 verdicts rather than at the controls. NOT: a Lagrangian for GU, a derivation of the shiab selector, a vacuum, a mass, a spectrum, a novelty claim for the central-parity mechanism (RB1b prior art) or for the 1456 t^3 branch (K77 prior art), or any claim-status movement."
disposition: EDDY_COMPLETION_DOES_NOT_RESCUE__SIGN_INERT_IN_THE_SQUARED_READING__ODD_DEGREE_IN_THE_FIRST_ORDER_READING__POST_REDUCTION_REPAIR_IS_EVEN_DEGREE_AND_CANNOT_REACH_AN_ODD_RUNAWAY__BOUNDEDNESS_REDUCES_TO_SIGN_OF_KAPPA1_TIMES_FLAT1__BRANCH_DEPENDENT_AND_BOTH_BRANCHES_REALISED_IN_BANKED_ARITHMETIC
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md
  - lab/active-research/joe-directed/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md
  - explorations/rb1b-native-bosonic-shiab-reopener-2026-07-30.md
  - lab/specifications/g2-source-field-and-variational-shiab-packet-2026-07-31.md
  - lab/specifications/g3-graph-variation-noether-bvbfv-packet-2026-07-31.md
  - lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md
  - explorations/weinstein-primary-source-reinspection-overlooked-answers-2026-07-30.md
  - lab/sources/selected-k77-moving-hq-eddy-quartic-source-return-2026-08-12.md
  - canon/shiab-existence-cl95.md
scripts:
  - tests/channel-swings/joe_directed_src4_eddy_completion_boundedness_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `SOURCE_NATIVE_ROUTE`.

# SRC-4 — the eddy completion cannot rescue the potential

## Result first

SRC-3 closed by naming the one thing never attempted: *"the natural candidates
are the eddy / Chern-Simons quadratic completion the source insists on."* It
has now been put into the potential and the boundedness question re-run.

> **The completion does not rescue it. It fails differently in each reading,
> and the second failure is the interesting one, because it is immune to the
> repair CG-1 found.**

| reading | degree in `T` | pre-reduction (Killing, DeWitt) | post-reduction (`B_theta`, `eta_plus`) |
|---|---|---|---|
| **E1** — the source's DISPLAYED first-order action | **3, ODD** | unbounded below | **unbounded below** |
| **E2** — the eddy-SQUARED second-order rival | 4, even | unbounded below (`-16/9`) | bounded, `>= -‖F0‖²` |
| **E2 + the `kappa_1` term** | 4, even | unbounded below | bounded **iff `kappa_1 * flat_1 >= 0`** |

The two failures have genuinely different characters:

- **E2 is SIGN-INERT.** The completion multiplies SRC-3's quartic by the
  strictly positive rational `(b*lam)^2`. At the source point that factor is
  exactly `4/9`, so SRC-3's `-4` becomes `-16/9` and CG-1's `+4` becomes
  `+16/9`. The completion changes the *number* and never the *sign*.
- **E1 is ACTIVELY WORSE, and CG-1's repair cannot reach it.** The completion
  is precisely what makes the action a Chern-Simons-type **primitive** — that
  is the whole point of it, and the reason the source insists the bare
  Shiab-curvature is not exact without it. A primitive of a quadratic Euler
  residual is **cubic**, hence **odd**. A real polynomial of odd degree is
  unbounded below no matter what the coefficients are and no matter what the
  pairing's signature is. CG-1's repair is a completion of *square* — a purely
  **even-degree** device — so it has no purchase here at all.

**The one-line statement.** *Exactness and boundedness are in tension: the
completion buys exactness by making the action a primitive, and a primitive of
this residual is odd in the field.*

---

## Preflight — six lenses, recorded before computing

**L1, Chern-Simons / topological-field-theory specialist.** `<T, S(F + ½D_BT +
⅓[T,T])>` has exactly the shape of a CS form relative to a background: it is
`½<T, 2F + D_BT + ⅔[T,T]>`. Route: read off its **degree in `T`** before doing
any algebra, because for CS-type functionals degree is the whole story. Kill:
if the displayed action is even in `T`, this lens is wrong and boundedness is a
signature question after all.

**L2, real-algebraic-geometry / semialgebraic specialist.** Boundedness below of
a polynomial on a real vector space is decided by its top-degree form on rays.
Route: reduce both readings to `V(tv)` and inspect the leading coefficient.
Prediction: an odd top degree is fatal and no lower-order term, including any
mass term, can repair it. Kill: exhibit a bounded-below odd polynomial — which
would refute the lens outright.

**L3, gauge-theory / equivariance specialist.** The shiab is a *natural*
operator, so its kernel is an invariant tensor and its very existence is
constrained. Route: count the vector indices of the eddy cubic in the arena
SRC-3 actually computed in. Kill: if a nonzero equivariant ad-valued shiab
exists there, the truncation is faithful and the eddy has content in it.

**L4, source-fidelity reader.** The source point is `(a,b) = (1/2, 1/3)`, and
the completion is not a free-parameter family — but the *bracket convention* is
undeclared, and a factor of 2 in `[T,T]` is exactly the kind of thing that
silently flips a verdict. Route: carry `lam` symbolically and prove every
verdict for both values. Kill: a verdict that holds for one convention only is
not a verdict.

**L5, honesty auditor.** Guard against three specific launderings: (i) claiming
the completion "makes it worse" when it is merely a positive rescaling; (ii)
proving unboundedness from a vacuous obstruction that kills every term
including the ones known to be nonzero; (iii) claiming novelty for a parity
argument or a cubic branch the repo has already banked. Route: grep first,
attribute, and plant a non-vacuity control.

**L6, undeclared-coefficient discipline (`SG4` fence).** If the completion needs
a coefficient the source has not declared, it must be carried symbolically and
its required sign reported — never fitted. Route: isolate `kappa_1`, find the
directions on which it alone decides, and report the condition.

**Cheapest kill-or-switch, declared first.** Compute the degree in `T` of the
source's displayed first-order action. If it is even, L1/L2 die together and the
gate reduces to a signature question CG-1 has already answered.

**One contrary route, declared first.** The source says *"there's a first order
theory and then a second order theory that's built from the first order
theory... think double copy"* (`TII` L26, `[00:05:43]`). If the physical
functional is `‖E_T‖²` — the norm-square of the first-order Euler covector —
then it is even by construction and the odd-degree argument never applies.
Disposition after the swing: recorded below as the strongest contrary
construction, and it is **not** defeated.

---

## Prior art, attributed — what is NOT re-claimed here

| object | owner | disposition here |
|---|---|---|
| the potential is unbounded below on an explicit ray, `K = -4` | **SRC-3** | re-run exactly as a live control; the eddy is applied *to* it |
| the Mexican hat is automatic; `M` symmetric and traceless | **SRC-2** | cited; the completion is checked against it and preserves it |
| `p` is a declared coset; `B_theta` Gram `2*I_45`, Ad(K)- but not Ad(G)-invariant; unbounded **iff** pre-reduction forms | **CG-1** | re-run as live controls; this gate supplies the reading its repair does **not** reach |
| an algebraic `Spin(9,5)`-equivariant `Λ²⊗Λ² → V⊗Λ²` is **zero by exact central parity** | **RB1b** (`explorations/rb1b-native-bosonic-shiab-reopener-2026-07-30.md`) | **prior art. The parity MECHANISM is RB1b's.** This gate re-runs it on the 10-dim vertical and checks it survives reduction to `K`. No novelty claimed for the method. |
| the released first-order action on the Spin-invariant constant branch is `I(t) = 1456 t³ + 7 kappa_1 t²`, stationary at `t = -kappa_1/312` | **K77 / vacuum-P2** (`tests/channel-swings/selected_moving_k77_vacuum_p2_norm_probe.py`) | **prior art. Re-used as the banked witness that the cubic coefficient is nonzero.** Both banked probes were run live for this gate. |
| on the four moving-`q` representatives the same first-order action has cubic coefficient **exactly zero** | **K77 HQ action owner** (`tests/channel-swings/selected_k77_hq_action_owner_potential_probe.py`) | prior art; re-used as the witness that the condition is *satisfiable* |
| the written first-order action `I_1^var` with `flat_1` "not a positive Riesz map" | **G2/G3 packets** (`lab/specifications/`) | read from the packet, not assumed; supplies the `kappa_1` fence |
| the eddy completion is not optional in the source (`WGS-03`, Portal `02:35:10`) | source pack | the object under test |
| shiab existence only; the selector is OPEN | `canon/shiab-existence-cl95.md` | respected; no selector is chosen here |

**Grep before novelty.** A mechanism sweep (`eddy`, `Chern-Simons`, `parity`,
`central element`, `kappa_1`, `1456`, `Clifford-odd`) found the parity mechanism
**already banked in RB1b** and the cubic branch **already banked in K77**. What
is *not* anywhere in the repo is the **composition**: nobody had put the eddy
completion into SRC-3's potential and asked the boundedness question in the two
readings CG-1 separated. That composition is this gate's only contribution, and
it is a composition, not a discovery.

---

## The construction

### Reading E2 — the eddy-squared rival is SIGN-INERT

Write the completed object with its coefficients carried, and the bracket
convention carried as `[T,T] = lam * (T∧T)` with `lam = 2` (commutator) or
`lam = 1` (wedge):

```text
I_2(T) = || F_0 + a * D_B T + b * lam * (T^T) ||^2 .
```

For constant modes `D_B T` drops out, exactly as in SRC-3. Along a ray
`T = t v`:

```text
I_2(t v) = t^4 * (b*lam)^2 * ||v^v||^2  +  t^2 * 2*b*lam * <F_0, v^v>  +  const
         = t^4 * (b*lam)^2 * K_SRC3(v)  +  t^2 * (b*lam) * Q_SRC3(v)   +  const.
```

> **The leading quartic is SRC-3's quartic multiplied by `(b*lam)^2`, which is
> strictly positive for every `b != 0` and every convention. The completion
> cannot change a sign.**

Exact values, computed and certified:

- source point `b = 1/3`, `lam = 2`: factor **`4/9`**; SRC-3's `-4` becomes
  **`-16/9`**, and CG-1's post-reduction `+4` becomes **`+16/9`**;
- source point `b = 1/3`, `lam = 1`: factor `1/9`; `-4/9`. **Same sign.** The
  convention risk is retired, not assumed away;
- swept over `b ∈ {1/3, 1/2, 1, -1/3, 2/3, 7/5}` and both `lam`: the sign is
  SRC-3's in every case pre-reduction and CG-1's in every case post-reduction;
- the exploration doc's planted `(0,0)` control, `b = 0`: the quartic vanishes
  **outright**, leaving nothing at all to stabilise the hat — so the bare
  curvature is strictly worse than the completion, which is the one thing the
  source is right about here.

And the quadratic — SRC-2's tachyonic direction — is rescaled by `b*lam > 0`,
so **the completion faithfully preserves the Mexican hat it was asked to
stabilise while failing to stabilise it.**

### Reading E1 — the source's displayed action is ODD, and that is fatal

The action the source actually displays (source pack `WGS-03`; the G2 packet
writes it as `I_1^var`) is:

```text
I_1(T) = < T, S_omega( F_B + (1/2) D_B T + (1/3)[T,T] ) >
       + (kappa_1/2) < T, flat_1 T > .
```

Read off the degrees in `T` — L1's cheapest kill-or-switch, and it did not
switch:

| term | degree in `T` |
|---|---|
| `<T, S(F_B)>` | 1 |
| `(1/2)<T, S(D_B T)>` | 2 |
| `(1/3)<T, S([T,T])>` | **3** |
| `(kappa_1/2)<T, flat_1 T>` | 2 |

Along a ray `T = t v` this is `L t + (D + kappa_1 N/2) t² + C t³`.

> **A real cubic with `C != 0` is unbounded below. This is a statement about
> DEGREE, not about SIGNATURE. Every coefficient — including `kappa_1`,
> including the pairing — is one degree too low to matter.**

Certified constructively rather than asserted: for the banked branch
`I(t) = 1456 t³ + 7 kappa_1 t²`, an explicit exact witness `t` is produced that
drives `I(t)` below `10³`, `10⁶` and `10¹²` in magnitude, for `kappa_1` taken
over `{-7, -1, 0, 1, ±10⁶}` — twelve orders of magnitude and both signs. The
overall sign of the pairing is flipped as a crude model of the pre/post-reduction
switch, and the runaway survives it.

**This is why the completion is worse than sign-inert here.** CG-1's repair is
`V = ‖a∧a + F_0‖² - ‖F_0‖²` — a completion of *square*. Squares are even. An
even-degree device cannot bound an odd-degree runaway, so **the post-reduction
positive-definite pairing, which removed all three of SRC-3's causes, removes
none of this one.** That is the sharpest thing in this gate: it identifies a
reading in which CG-1's repair is not merely undeclared but *structurally
inapplicable*.

**The exact condition, and it is satisfiable.** E1 is bounded below on a branch
iff that branch's cubic coefficient vanishes (and its quadratic is `>= 0`).
Both sides are already realised in banked repo arithmetic:

- **violated**: the Spin-invariant constant branch, `C = 1456 != 0`;
- **satisfied**: the four moving-`q` representatives, `C = 0` exactly.

So the condition is non-vacuous in both directions, and **which branch GU's
vacuum sits on is undeclared.**

### Why SRC-3's own arena cannot see the eddy at all

There is a scope fact that has to be stated or the above is misread. In the
**bosonic vertical truncation SRC-2/SRC-3/CG-1 all computed in** — ad-valued
forms on the internal 10, no spinor index — the eddy terms are not merely small.
They are **identically zero**, by RB1b's central-parity mechanism, re-run here on
the 10-dim vertical:

- `c = -I_10` satisfies `cᵀ η c = η` and `det c = +1`, so `c ∈ SO(6,4)`;
- `c = (-I_6) ⊕ (-I_4)` with both block determinants `+1`, so **`c ∈ K =
  SO(6)×SO(4)`: the obstruction survives CG-1's reduction**;
- `-I_6` and `-I_4` are exact products of π-rotations, so `c` is in the
  **identity component**;
- `Ad(c) = id` on all 45 generators, so `c` acts as `+1` on `ad` and `-1` on the
  form index `V`;
- hence `c` acts as `+1` on `Ω²(ad)` and `-1` on `Ω¹(ad)`, so every equivariant
  `S: Ω²(ad) → Ω¹(ad)` obeys `S = -S`, hence `S = 0`.

**Non-vacuity is planted, not hoped for.** In odd dimension the hypothesis
genuinely fails — `-I_3` has `det = -1`, so it is not in `SO(3)` — and the *same*
eddy cubic is exactly `6` on `T = I_3`, not zero. That is the ordinary
Chern-Simons cubic, and it is why CS theory lives in odd dimensions. And
even-degree objects survive the parity cut untouched: `<v,v>` and `‖v∧v‖²` are
both nonzero. The theorem discriminates by dimension parity; it does not kill
everything it touches.

The consequence is a scope correction, not a rescue:

> **SRC-3's truncation is blind to the eddy completion.** The completion has to
> be evaluated where the shiab is actually nonzero — on the spinorial /
> `epsilon`-soldered odd-Clifford-grade domain that RB1b identified and the G2
> packet writes as `S_epsilon^tr`. That is exactly where the banked `1456 t³`
> lives, which is why this gate uses the banked branch as its E1 witness rather
> than inventing a shiab of its own.

### The undeclared coefficient, carried and not laundered

The only coefficient the completion adds that is not fixed by the source point
is `kappa_1`. It is carried symbolically throughout. Its role is exact and
narrow:

- **Pre-reduction (either reading): `kappa_1` is powerless.** In E2 the quartic
  `-16/9 t⁴` outranks `(kappa_1/2) t²`; in E1 the cubic outranks it. No value of
  `kappa_1` bounds either.
- **Post-reduction E2: `kappa_1` is decisive, and only there.** CG-1's bound
  becomes `V >= -‖F_0‖² + (kappa_1/2)‖a‖²`, so:

> **Bounded below iff `kappa_1 >= 0`** (more precisely iff the composite
> `kappa_1 * flat_1` is positive semi-definite).

**Which directions decide it is the pretty part.** CG-1 retired SRC-3's 630
abelian pairs as *"conditionally vacuous"* — correctly, because on them
`a∧a = 0` kills the quadratic and the quartic together. The `kappa_1` term does
**not** vanish there. So those retired directions become exactly the ones that
fix the sign of `kappa_1`. On the explicit abelian ray `a_0 = J_01`, `a_1 = J_23`
(`[J_01, J_23] = 0` exactly), the entire potential collapses to
`(kappa_1/2) t² ‖a‖²` with `‖a‖² = 4 > 0` — so `kappa_1 < 0` runs to `-∞` on a
direction where nothing else survives to stop it.

**And `kappa_1 >= 0` is not free.** The G2 packet states in its own voice that
`flat_1` *"is not a positive Riesz map"* — read from the packet by the probe,
not assumed. So the condition is on the **composite** `kappa_1 * flat_1`, and
one of its two factors is itself undeclared. This is reported, not resolved.

---

## Postflight — inline hostile review

**Strongest overclaim available, and rejected.** *"The eddy completion kills
GU's symmetry-breaking mechanism."* False, on two counts. First, the E1 result
is **branch-dependent** and the repo has already banked a branch where the cubic
coefficient is exactly zero — so "the action is unbounded" is not a theorem
about GU, it is a theorem about a branch. Second, and worse, an unbounded-below
*first-order* action is not automatically a pathology: first-order/Chern-Simons
functionals are routinely unbounded below and are not meant to be minimised —
their content is in their **stationary points**, and the banked branch has an
explicit one at `t = -kappa_1/312`. Reading "unbounded below" as "the theory is
sick" would be importing a second-order habit into a first-order object. The
honest claim is the narrow one: *the completion does not supply the stabilisation
SRC-3 showed was missing, and in the first-order reading the question of
boundedness is not even the right question.* That caveat cuts against this
gate's own headline and is stated first for that reason.

**Strongest contrary construction — the one recorded at preflight, and it is not
defeated.** The source says GU has *"a first order theory and then a second
order theory that's built from the first order theory... think double copy"*
(`TII` L26, `[00:05:43]`). If the physical functional is `‖E_T‖²` — the
norm-square of the G2 packet's exact Euler covector `E_T^var`, which is
*quadratic* in `T` — then the functional is **quartic and even by construction**,
the odd-degree argument never applies, and under a positive-definite
post-reduction pairing it is bounded below by **zero**, trivially, being a
norm-square. That is a completely live escape from this gate's E1 result, it is
the source's own stated architecture, and this gate does **not** close it. What
this gate does establish is that the escape is *load-bearing*: GU's boundedness
in the first-order reading depends on the second-order theory actually being the
physical one, and on `E_T` being squared under the post-reduction pairing. Both
are undeclared. The exploration doc already flagged the adjacent hazard —
*"first-order `I^B_1`, second-order `‖Υ^B‖²`... are different functional levels
and must not all be called independent fundamental terms without a derivation."*
This gate is a concrete instance of why that fence matters: **the two levels give
opposite boundedness verdicts.**

**Weakest seam.** The identification of `T_omega` with SRC-2/SRC-3's perturbation
`a`. SRC-1/2/3 expand `‖F‖²` about a background in an ad-valued one-form `a`;
the eddy completion is written in the **augmented torsion** `T_omega`, a
difference of two connections. The source return of 2026-08-12 says in terms
that *"identification of the weak-doublet lift with a component of `T` remains
open."* This gate treats them as the same slot because both are ad-valued
one-forms entering the same curvature expansion, and because the source's own
`GU-YM-Δ4` passage runs the two together — but that identification is an
inference, not a declaration, and every E2 number here inherits it. If `T_omega`
is a *constrained* subspace of ad-valued one-forms rather than all of it, the
rays used above may not be admissible, and both the `-16/9` and the abelian
`kappa_1` witness would need re-deriving on the constrained set. Nothing in this
gate tests that constraint.

**Second seam, smaller.** The E2 leading-quartic computation is done on SRC-3's
single published ray, not swept over the whole 450-dimensional space. That is
sufficient for an *unboundedness* verdict (one ray suffices) and for the
sign-inertness verdict (the rescaling factor is ray-independent by construction),
but it is **not** sufficient to characterise the full set of runaway directions,
and no such characterisation is claimed.

**Self-audit of this gate's own probe.** Three defects were found and fixed
before the result was recorded: a floating-point `np.linalg.det` on a
load-bearing group-membership check (replaced with an exact integer determinant
guarded by a diagonality assertion), an unreachable `if False else` dead branch
in the `Ad(c)` check, and one gate hardcoded to `True` (replaced by an actual
read of the G2 packet for the `"not a positive Riesz map"` string). Four
mutations were then planted: `centre-not-in-group` (39/44), `centre-trivial`
(42/44), `eddy-rescale-linear` (40/44) and `eddy-action-even` (41/44), all exit
1. The last two are the important ones — they attack the **E2 sign-inertness**
and **E1 odd-degree** verdicts directly rather than the controls, so both
load-bearing claims are demonstrably falsifiable.

---

## Claim ceiling

This artifact establishes, at EXACT grade:

1. in the eddy-squared reading the completion rescales SRC-3's quartic by
   `(b*lam)^2 > 0` and is therefore **sign-inert**, verified at the source point
   in both bracket conventions and across a six-member coefficient family;
2. the source's displayed first-order action is **cubic** in `T`, hence unbounded
   below whenever its cubic coefficient is nonzero, **independent of the
   pairing's signature**, so CG-1's even-degree repair cannot reach it;
3. boundedness in the post-reduction eddy-squared reading reduces to the single
   condition **`kappa_1 * flat_1 >= 0`**, decided on precisely the abelian
   directions CG-1 retired as vacuous;
4. the bosonic vertical truncation SRC-3 computed in is **blind to the eddy
   completion**, by RB1b's central-parity mechanism, which survives reduction to
   `K` and is shown non-vacuous by an odd-dimensional control.

It does **NOT** establish: a Lagrangian for GU; that the first-order reading is
the physical one (the second-order/double-copy reading is live and would be
even-degree); the shiab selector (`canon/shiab-existence-cl95.md`, OPEN); the
identification of `T_omega` with SRC-3's `a` (flagged as the weakest seam); a
vacuum, mass, spectrum or breaking pattern; a value or sign for `kappa_1`; any
novelty for the central-parity mechanism (RB1b) or the `1456 t³` branch (K77);
or any claim-status, canon, ledger or current-state movement.

## Next gate

**SRC-5 is a one-line question to the source, and it is a different one-liner
than CG-2's.** CG-2 asks *which pairing* enters the norm-square. This gate shows
that question is only decisive in the second-order reading. The prior question
is: **is GU's physical functional the first-order `I_1`, or the second-order
`‖E_T‖²` built from it?** Those two give **opposite** boundedness verdicts under
the *same* pairing, so no amount of work on the pairing settles boundedness until
the functional level is declared. That datum is `SG4`/Lane-1 property, not this
channel's — the same wall SRC-3 and CG-1 both hit, now reached from a third side.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
