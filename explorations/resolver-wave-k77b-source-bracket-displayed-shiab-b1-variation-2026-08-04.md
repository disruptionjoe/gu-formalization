---
artifact_type: exploration
created: 2026-08-04
title: "Resolver Wave K77-B: the source fixes the quadratic bracket, but the displayed low-grade Shiab/B1 family is not yet a common variational equation"
grade: "Exact source-normalization receipt; faithful real Cl(7,7), exterior/Hodge, B-adjoint, 91-generator real-equivariance, and Sage D7 complexified invariant-multiplicity certificates; canonical low-grade raw-product adjoint-codomain counterexamples; eight source-inspired low-grade product-channel classifications; and two-route constant-field B1 variation. No selected Shiab, derivative/Green identity, full Euler/Noether system, domain, observation descent, or physics recovery."
named_gate: RESOLVER-WAVE-K77B-SOURCE-BRACKET-NORMALIZATION-DISPLAYED-SHIAB-AND-B1-VARIATION
gate_before: NONCHIRAL_PARENT_AND_OBSERVATION_BLOCKS_CONFIRMED__VEV_BLOCK_CLASSIFIED_NOT_SELECTED__EFFECTIVE_CHIRALITY_NOT_DERIVED
gate_after: SOURCE_BRACKET_NORMALIZED__CANONICAL_LOW_GRADE_RAW_SHIAB_CODOMAIN_KILL__LOW_GRADE_REPAIRS_NOT_VARIATIONALLY_CERTIFIED
route_disposition: CONTINUE_K77_THROUGH_DISPLAYED_ANSATZ_AND_BROADER_SHIAB_RIVAL_CENSUS
source_collision: SOURCE-CORRECTS-BRACKET-NORMALIZATION; SOURCE-CONFIRMS-MAGIC-BRACKET-FREEDOM-AND-MISSING-SELECTOR
canon_verdict_change: none
third_lane_promoted: false
---

# Resolver Wave K77-B: source bracket, displayed Shiab, and B1 variation

## Result first

K77-B closes one old ambiguity and exposes the next construction object.

The 2021 draft writes the bosonic curvature packet in equation (9.4) as

\[
 F_B+\frac12d_BT+\frac13[T,T],
\]

but equation (12.4) rewrites the same term as

\[
 F_B+\frac12d_BT+\frac13T\wedge T.
\]

For a matrix-valued one-form, the graded self-bracket is

\[
 [T,T]_{\rm graded}=2T\wedge_{\rm matrix}T.
\]

The operative source normalization is therefore `q(T)=T wedge T`, not a
second, doubled quadratic. An independent cyclic-matrix calculation verifies
that the source coefficients `1/2,1/3` vary to unit endpoint weights. Reading
the quadratic as a doubled graded bracket fails that exact check.

The displayed Shiab presents a different problem. If its juxtaposed
Clifford/matrix products are read literally as associative products, the map
does not generally land in the stated real `u(64,64)` adjoint: on two exact
K77 curvature fixtures, its 13-form coefficients split respectively into
`10 B-skew + 4 B-self` and `2 B-skew + 12 B-self` components. This kills only
that literal raw-product reading.

The source itself supplies possible operations for repairs: coefficient
commutators and `i` times anticommutators. It does not independently select an
operation at each displayed product node. All eight source-inspired nodewise low-grade choices are
`B`-skew/ad-valued. But ad closure is not action exactness. On two independent
constant-field fixtures, six channels are nonvacuous and all six disagree
with the endpoint residual obtained by replacing the transgression weights
by unit weights. The other two have zero defect only because both sides are
zero on the bank. They are controls, not survivors.

This does **not** kill the K77 lane or the B1 grammar. Exact `D7`
representation arithmetic finds two invariant copies each for `Phi_1` and
`Phi_2`: the low grades `1,2` and Hodge-dual grades `13,12`. The next honest
object inside the displayed ansatz is therefore the full low/high Phi carrier

\[
 \Phi_1=a\Phi_1^{(1)}+b\Phi_1^{(13)},\qquad
 \Phi_2=c\Phi_2^{(2)}+d\Phi_2^{(12)},
\]

together with product-channel, Bianchi, curvature-trace, and transgression
constraints. P1/P2/P3 cannot choose this family until the action and endpoint
are already admissible; all remain unchanged and unused.

The exact verdict is:

```text
SOURCE_BRACKET_NORMALIZED
LITERAL_RAW_SHIAB_CANDIDATE_MAP_KILLED_AT_AD_CODOMAIN
SIX_LIVE_LOW_GRADE_REPAIRS_FAIL_SAME_ACTION_ENDPOINT_BANK
TWO_ZERO_DEFECT_REPAIRS_ARE_VACUOUS
FULL_LOW_HIGH_PHI_CARRIER_INSIDE_DISPLAYED_ANSATZ_OPEN
BROADER_SOURCE_NATURAL_SHIAB_RIVAL_CENSUS_OPEN
```

## Plain English

We now know what Eric's bracket coefficient means. That part is no longer a
guess.

But simply copying the displayed contraction does not yet produce a valid
gauge-algebra-valued equation. The draft mentions two algebra products that
repair the type. We tested all eight independent nodewise assignments inside
this displayed low-grade ansatz.
They all either fail to be the derivative of the displayed action endpoint or
vanish on the test and therefore teach nothing.

That is useful progress because the failure tells us exactly what must change.
The representation theory says the draft's displayed low-grade forms are only
half of the invariant choices. We should now construct the missing high-grade
partners and solve for the combination that is simultaneously gauge-valued,
Bianchi-compatible, Einstein-like on algebraic curvature, and the derivative
of the same action. We should not use an external bit to patch a failed map,
and we should not skip ahead and call a kinematic fermion block physical.

## 0. Layer 0: six objects that must not be collapsed

| object | type | status |
|---|---|---|
| source quadratic | matrix-valued exterior two-form `T wedge T` | normalized exactly |
| graded self-bracket | `[T,T]_graded=2 T wedge T` | distinct convention |
| augmented/displaced torsion `T=varpi-epsilon^{-1}d_g epsilon` | source-defined adjoint-valued one-form; `A=B+T` additionally requires matching the draft's reference-connection notation | source-defined formula; connection-difference identity derived/uncertain |
| ordinary spacetime torsion | tangent-valued two-form | not identified here |
| B1 top-form density | scalar 14-form after trace/pairing | constructed locally |
| translation Euler covector | adjoint-valued 13-form paired with `delta T` | tested at fixed epsilon/metric |
| observed four-dimensional equation | pullback/quotient of an ambient Euler system | unbuilt |

The source's `T` may occupy a torsion-like role, but K77-B does not identify it
with the ordinary spacetime torsion tensor. Likewise, equality of two written
expressions in the action does not by itself prove that the proposed endpoint
is its variational derivative.

## 1. Primary-source collision

The source collision is classified `SOURCE-CORRECTS` for normalization and
`SOURCE-CONFIRMS` for the open selector burden.

| draft location | source content | use here |
|---|---|---|
| section 8, equation (8.1) | Shiabs may use a matrix commutator or `i` times an anticommutator | emits two operations; the finite nodewise bank is reconstructed here |
| section 8.2 | remembered highest-weight/Bianchi selector is not present; notes could not be located | selector remains construction debt |
| equations (9.2)--(9.3) | candidate `Omega2(ad) -> Omega13(ad)` Shiab and displayed two-term contraction | exact codomain and term-liveness test |
| equations (9.4), (12.4) | same B1 packet written with bracket notation and then with `T wedge T` | internal normalization witness |
| equation (9.7) | varies `varpi` while holding `epsilon,g` fixed | scope of the first translation test |
| appendix (12.26)--(12.27) | explicit commutator and `i`-symmetric matrix products on the unitary algebra | exact repaired channels |

The displayed square brackets in (9.3) can be read as grouping punctuation;
the draft's section 8 and appendix show that a Lie-algebra product still has
to be selected. K77-B therefore kills the literal associative-product reading,
not every source-intended interpretation of the Shiab.

The source definitions

```text
A_omega = nabla_0 + varpi
B_omega = nabla_0 + epsilon^{-1} d_0 epsilon
T_omega = varpi - epsilon^{-1} d_0 epsilon
```

suggest `A_omega=B_omega+T_omega` by direct substitution only if the draft's
`d_0` and `d_{nabla_g}` reference-connection notation is identified exactly.
The identity is therefore `SOURCE_DERIVED/UNCERTAIN`, not a separately printed
or promoted theorem. The endpoint `F_A` is kept logically separate from that
reconstruction.

## 2. Exact K77 coefficient algebra

The executable uses the faithful real algebra

\[
 \mathrm{Cl}(7,7)\cong M_{128}(\mathbb R)
\]

without importing Wave K's K95/right-quaternionic/native-grade machinery.
The signature is the source split `(1,3)+(6,4)`. The exact exterior Hodge
operator satisfies the K77 square law on degrees `1,2,12,13`.

For the invariant symmetric form `B`, a real Clifford blade of grade `r` has
adjoint parity `(-1)^(r(r+1)/2)`. Thus the real B-skew grades are

```text
1, 2, 5, 6, 9, 10, 13, 14
```

with total dimension `8128=dim so(64,64)`. Multiplying the complementary
B-self grades by `i` adds `8256` real dimensions, giving the full
`16384=dim_R u(64,64)`.

The low forms satisfy exactly

\[
 \Phi_2^{(2)}=\frac12\Phi_1^{(1)}\wedge\Phi_1^{(1)}.
\]

Clifford-volume multiplication supplies independent grade-13 and
`i`-grade-12 copies with the correct B-adjoint type. Exact infinitesimal checks
against all 91 `so(7,7)` generators verify equivariance of all four low/high
copies and their grade-disjoint independence. An independent Sage D7 complex
character calculation returns

```text
degree(full Clifford/exterior carrier) = 16384
<V, carrier> = 2
<Lambda2 V, carrier> = 2
```

so a low-grade-only Shiab is not representation-theoretically unique.

## 3. The literal codomain obstruction

Let `S_raw` denote the canonical low-grade realization of equation (9.3) with
every coefficient juxtaposition read as ordinary associative Clifford/matrix multiplication. Both its Ricci-like and
Ricci-scalar-like terms are nonzero 13-forms on the first exact fixture, and
the map is exactly linear in curvature.

Nevertheless, the outputs contain B-self coefficients. Since the advertised
codomain is the real B-skew adjoint, this is a direct domain-to-codomain
counterexample. The disposition is

```text
CANDIDATE_MAP_KILL: literal raw associative-product Shiab
```

It is not a `MECHANISM_KILL`: inserting one of the source's algebra products,
projecting explicitly to the real adjoint, or changing the invariant Phi
combination are distinct candidates.

## 4. Eight low-grade source-inspired reconstructions

At the three coefficient-product occurrences in the displayed expression—one
in the first summand and two nested in the second—K77-B tests every independent
assignment of

\[
 m_-(X,Y)=XY-YX,\qquad
 m_+(X,Y)=i(XY+YX).
\]

These are the draft's exact appendix (12.26)--(12.27) normalizations. The
finite eight-member bank independently assigns an operation at each node;
that choice is source-inspired, not source-selected. The normalizations cannot
be replaced by halves as a common rescaling: the first Shiab summand contains
one exercised product node and the second contains two. The B-adjoint anti-involution proves
universal closure of both operations on B-skew inputs; the executable certifies
the anti-involution on all 16,384 blades times all fourteen generators. All
eight bank members are B-skew/ad-closed, but are not equivalent:

- two kill both displayed terms on the codomain fixture;
- two keep only the Ricci-scalar-like term;
- two keep only the Ricci-like term;
- two keep both.

Therefore `ad` closure cannot serve as the missing selector.

## 5. First B1 variation

For this first, deliberately local gate, `epsilon` and the metric are fixed,
`F_B=d_BT=0`, and only the constant algebraic cubic and mass sectors are
exercised. The density is

\[
 I(T)=\int\operatorname{tr}\left[
 T\wedge\left(S\!\left(\tfrac13T\wedge T\right)
 +\tfrac{\kappa_1}{2}*T\right)\right].
\]

Two routes are compared:

1. substitute `T+s alpha` and differentiate the same density exactly;
2. pair `alpha` with the source-proposed endpoint
   `S(T wedge T)+kappa_1 * T`.

The mass contribution cancels from the defect, so it cannot hide the cubic
classification. Results on the discriminating fixture are:

| product triple | direct | endpoint | defect | disposition |
|---|---:|---:|---:|---|
| `comm/comm/comm` | `0` | `-512` | `512` | nonvacuous fail |
| `comm/comm/symi` | `1024/3` | `0` | `1024/3` | nonvacuous fail |
| `comm/symi/comm` | `1024/3` | `0` | `1024/3` | nonvacuous fail |
| `comm/symi/symi` | `512/3` | `0` | `512/3` | nonvacuous fail |
| `symi/comm/comm` | `-1024/3` | `-512` | `512/3` | nonvacuous fail |
| `symi/comm/symi` | `0` | `0` | `0` | vacuous |
| `symi/symi/comm` | `0` | `0` | `0` | vacuous |
| `symi/symi/symi` | `-512/3` | `0` | `-512/3` | nonvacuous fail |

Every bank density is also exactly real on both fixtures. The first fixture is
retained as a planted vacuity control: it gives zero on
both sides for every corrected channel. The second prevents those zeros from
being misread as a theorem. No live low-grade channel passes the bank.

This is an exact candidate-family obstruction, not a proof over every
invariant Shiab or over the derivative sector. K77-B does not yet exercise
`d_BT`, integration by parts, a moving `epsilon`, a moving Hodge operator, the
metric Euler equation, Bianchi/Noether identities, boundary conditions, or a
Green domain.

## 6. What moved and what did not

Moved:

- the source bracket normalization is closed;
- the canonical low-grade raw-product Shiab reading is killed at its advertised codomain;
- all eight source-inspired low-grade commutator/`i`-anticommutator reconstructions are exactly typed;
- none of the six nonvacuous low-grade repairs passes the same-action endpoint
  bank;
- the full low/high Phi carrier inside the displayed ansatz is now finite and
  explicit; the broader source-natural Shiab rival family is not.

Not moved:

- no source-forced or mathematically selected Shiab exists yet;
- no full derivative/Green/Helmholtz identity has been proved;
- no Euler/Noether/BV/domain or observation-descent construction is complete;
- no K77-C VEV, effective-chirality, particle, Standard Model, gravity,
  cosmological, or dark-sector row advances;
- no claim status, canon verdict, public posture, or third-lane status moves;
- P1/P2/P3 remain unchanged and unused.

## 7. Efficient next gate

The next gate is

`RESOLVER-WAVE-K77-SHIAB-FAMILY-SELECTOR-AND-TRANSGRESSION-EXACTNESS`.

It should proceed in this order:

1. Build the four-coordinate invariant Phi family **inside the displayed
   ansatz**, then enumerate the broader source-natural rival table generated by
   Hodge, wedge/contraction, commutator, symmetric product, volume form, and
   finite sums. The four-coordinate family is not the whole Shiab family.
2. Construct an explicit Spin/soldering injection of the 3,185-dimensional
   algebraic Riemann-curvature module into `Omega2(Y,ad P)`, impose its Bianchi
   restriction, and only then use it as an Einstein-like selector. It is a
   submodule of the displayed Shiab domain, not the whole domain.
3. Compute the same-action field-space Helmholtz/transgression condition as
   polynomial equations in the family coordinates.
4. Add compatible `d_BT` jets and the exact Krein/Green adjoint; then vary
   `B`, `epsilon`, and the metric by ownership.
5. Promote a Shiab/B1 candidate only if the same member passes codomain,
   Bianchi, transgression, reality, and derivative/Green gates.
6. Only then resume K77-C fermion/VEV/effective-chirality work and rerun the
   37 atomic targets against the same action.

This is a surplus-constrained construction problem: the goal is not to reject
every fitted operator, but to see whether one small invariant family can meet
more independent requirements than it has free coordinates.

## Reproduction

```bash
uv run --with sympy==1.14.0 python \
  tests/channel-swings/resolver_wave_k77b_source_bracket_displayed_shiab_b1_variation_probe.py
```

The initial exact probe passed `21 exact + 1 Sage + 6 source + 12 type + 8
planted = 48` checks. Hostile-review repairs and final rerun status are
recorded in the companion disposition and review artifacts. The repaired
probe passes `28 exact + 1 Sage + 6 source + 12 type + 8 planted = 55`, and
all three final specialist reviews pass.
