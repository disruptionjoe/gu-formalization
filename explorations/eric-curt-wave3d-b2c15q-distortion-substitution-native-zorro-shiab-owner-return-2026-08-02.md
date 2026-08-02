---
title: "Eric/Curt Wave 3D-B2C15Q: quadratic distortion connection and native Zorro--Shiab response"
status: active_research
doc_type: construction_result
created: 2026-08-02
branch: agent/null-clifford-omega1-repair
run: RUN-20260802-083641-gu-formalization-ecw3d-b2c15q-direct
registry: lab/process/eric-curt-wave3d-b2c15q-distortion-substitution-native-zorro-shiab-owner-return.json
probe: tests/channel-swings/eric_curt_wave3d_b2c15q_distortion_substitution_native_zorro_shiab_owner_return_probe.py
grade: "B2C15Q PARTIAL CONSTRUCTION PASS WITH ACTION-PLACEMENT AND OWNER-ORDER STOPS. The leading quadratic BCH connection term of the B2C15P distortion reduction depends only on Delta=c3^2-c11^2. Exhaustive exact Clifford algebra checks all 66,066 grade-three pairs; 6,006 live brackets span the 91 connection directions, and one common reduction value has quadratic rank 91. This is not the full Maurer--Cartan connection: higher BCH h-terms remain. The actual 71-leg Zorro curvature maps to 13 compatible grade-two Shiab coefficients. A shaped realizable quadratic connection pattern pairs by 51/8, but Weinstein's written I1 pairs T rather than q_red with the Shiab image. Adding this pairing is a new lambda_red-weighted action ansatz, so no physical constraint or surplus is claimed. Exact finite Green and source-owner comparators pass but are not the native tensorial variation. All eight fixed-curvature moving-Shiab slots are live and the local ten-metric-direction response has rank 10. The raw curvature linearization, Zorro graph, expanded formal adjoint, and background/variation jet burdens remain to be assembled. The 13-form observation coefficient splits into four (3,10) and nine (4,9) legs; raw pullback is zero, ordinary fibre Gysin can retain only the former with proper-support data, and an equation-dual is a separate unbuilt map."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# B2C15Q quadratic connection and native response

## Result first

B2C15Q found a real piece of the missing construction and, during hostile
review, found that it had initially put that piece into the action too early.

The B2C15P partial reduction is

\[
u(T)=c_3\operatorname{Alt}(T)+c_{11}*\operatorname{Alt}(T)
\in\Lambda^3V\oplus\Lambda^{11}V.
\]

For a coset representative `exp(u)`, the reductive Maurer--Cartan connection
is the `h`-part of `exp(-u)d exp(u)`. Its leading nonzero term is

\[
q_{\rm red}^{(2)}=-\frac12\operatorname{pr}_{\mathfrak h}[u,du].
\]

The exact exhaustive calculation proves

\[
\boxed{
q_{\rm red}^{(2)}(c_3,c_{11})
=(c_3^2-c_{11}^2)q_{\rm red}^{(2)}(1,0).
}
\]

This is a theorem about the quadratic connection jet, not the full BCH
series. Higher even-order `h` terms can occur and have not been summed.

Applying the native trace-adapted Shiab to B2C15P's actual `71`-leg Zorro spin
curvature gives `13` external thirteen-form legs, each with one internal
grade-two coefficient. All thirteen internal coefficients pass the active
right-`H`, Krein, and `C+` word checks.

A shaped quadratic connection pattern, realizable at one common reduction
value, pairs with that coefficient by

\[
\langle q_{\rm red}^{(2)},\mathscr S(F_{\rm spin})\rangle
=\frac{51}{8}(c_3^2-c_{11}^2).
\]

But this is a response, not yet an action constraint. Weinstein's written
first action pairs `T` with the Shiab image; it does not display `q_red` in
that slot. The proposed term

\[
I_{\rm red}=\lambda_{\rm red}
\langle q_{\rm red},\mathscr S(F_{\rm spin})\rangle
\]

is therefore a new repository action ansatz with a third free coefficient.
Its physical constraint surplus is `UNCOMPUTED`. Setting `Delta=1` would be a
chosen normalization, not evidence.

## Plain English

The distortion can make the beginning of a genuine connection. At leading
quadratic order, all of its apparent two-coefficient freedom collapses to one
Lorentzian-style norm, `c3^2-c11^2`, and one generic reduction state can make
every one of the 91 ordinary connection directions.

What we do not yet know is whether the full nonlinear connection keeps that
collapse. More importantly, the written source action does not plainly say
to pair this new connection with the Shiab curvature. That pairing is a good
candidate term, but it must be introduced and varied honestly as a candidate,
including its coefficient. This is exactly where writing the action exposed a
new construction burden that abstract hardening did not.

## Layer 0

| object | type | disposition |
| --- | --- | --- |
| source `epsilon_H` | `H`-valued gauge field | source explicit |
| source distortion `T` | `varpi-q_g(epsilon_H)` | source explicit |
| derived `epsilon_red(T)` | finite Clifford-plane reduction | repository candidate |
| `q_red^(2)` | quadratic BCH `h`-connection jet | repository exact |
| full `q_red` | `pr_h(exp(-u)d exp(u))` including higher BCH terms | open |
| source first action `I1` | pairs `T` with the Shiab image | source explicit |
| proposed `I_red` | pairs `q_red` with the Shiab image | new repository ansatz |
| fixed-curvature Shiab motion | derivative of contraction coefficients | constructed locally |
| raw curvature linearization | `D_G F_spin[H]` | order-two total-metric operator, not yet assembled here |
| base-metric graph linearization | `D_gG_Y[h]` | order one because Zorro contains `Gamma(g)` |
| expanded owner | `(D_gG_Y)^!(D_GF_spin)^!E` | formal-adjoint/order ledger open |
| upstairs coefficient | thirteen-form on `Y` | constructed for shaped term |
| ordinary pullback | pullback to `X4` | zero by degree |
| fibre Gysin | integration over the ten-dimensional metric fibre | only four legs eligible; support data open |
| equation-dual | adjoint of a specified observation-variation lift | separate and unbuilt |

## Source collision

- `SOURCE-CONFIRMS`: draft pp.43--44 and pp.56--57 own one epsilon, one
  `varpi`, and `T=varpi-epsilon^-1 d0 epsilon`.
- `SOURCE-CONFIRMS`: draft equation 9.4 owns the curvature plus
  `1/2 d_B T` plus `1/3[T,T]` first-action grammar.
- `SOURCE-CONFIRMS`: Portal/Oxford `02:23:30--02:23:52` owns the chain metric
  to Levi--Civita to gimmel to spin connection.
- `SOURCE-CONFIRMS`: TOE `00:26:28--00:29:16` owns trace reversal in the
  Frobenius fibre.
- `SOURCE-CORRECTS`: Shiab is a contraction rather than a projector; source
  epsilon and the finite reduction are different objects.
- `SOURCE-SILENT`: the distortion reduction, full reductive BCH connection,
  `c3:c11`, `lambda_red`, placement of `I_red`, genuine direct
  `D_varpi odot_omega`, formal-adjoint owner, observation map, BV, and domain.
- `WATCH-ONLY`: the unreleased modern `D^2` construction supplies none of the
  missing formulas.

Author statements guide construction and attribution. They do not prove the
repository algebra or the proposed action term.

## Quadratic connection theorem

There are `364` grade-three blades and `66,066` unordered pairs. Every pair
passes

\[
\operatorname{pr}_2[*a,*b]=-​\operatorname{pr}_2[a,b],
\qquad
\operatorname{pr}_2([a,*b]+[*a,b])=0.
\]

The exact census is:

```text
all pairs checked                 66,066
live grade-two brackets            6,006
grade-two span                         91 / 91
Hodge-identity failures                 0
```

One deterministic grade-three `u` makes

\[
v\mapsto\operatorname{pr}_2[u,v]
\]

rank `91`. Thus all thirteen connection directions used in the shaped Shiab
pairing can be realized with different `du_i` at the same `u`; the assembly
does not silently choose a different reduction background for each leg.

At this order both Hodge eigenbranches `c11=+c3` and `c11=-c3` vanish. That
does not prove the full Maurer--Cartan connection vanishes there. The next
nonzero `h` contribution can occur at quartic order, schematically
`-pr_h[u,[u,[u,du]]]/24` in the displayed convention.

An exact quartic plant confirms that this term is live: its unscaled nested
commutator has `11` grade-two components and coefficient `36000` in one selected direction at
`(c3,c11)=(2,1)`. Two same-`Delta` pairs agree on the tested component, and
the `Delta=3` value scales it by nine. That suggests a higher-power `Delta`
pattern but is one fixture, not an all-orders theorem.

## Native Zorro--Shiab response

The exact output has `13` legs. Every exterior key contains trace index `10`,
and its missing index ranges over `0..9,11,12,13`. The internal blade is the
corresponding `(i,10)` direction.

The active word checks apply only to those thirteen internal coefficients.
They do not port the distortion graph, full Maurer--Cartan connection,
proposed action term, or its formal adjoint through the entire source `(7,7)`
to active `(9,5)` fork.

The normalized shaped pairing is `51/8`. An earlier scratch value `21/8` was
caught by the executable gate and never promoted. The response of the
proposed term is

\[
\frac{51}{8}\lambda_{\rm red}(c_3^2-c_{11}^2),
\]

whose Jacobian has rank one at a generic coefficient point. That rank says
how many coefficient combinations this one response can see. It is not a
constraint count because no target equation has yet been derived. The probe
rejects both counting the thirteen tensor legs independently and turning the
chosen normalization `Delta=1` into evidence.

## Conditional Green and owner comparators

For a one-dimensional differential model of the proposed term, exact
integration by parts gives

```text
unscaled: direct -17/6, bulk 13/6, boundary -5
scaled by 51/8: direct -289/16, bulk 221/16, boundary -255/8
```

In both rows `direct = bulk + boundary`. A finite symbolic pullback also
returns the induced response through the existing `varpi`, source-epsilon,
and metric owners without inventing a second `varpi` owner.

These are two separate exact comparators: the first is differential and the
second is a finite algebraic three-owner chain. They have not been composed
into one differential source-coordinate action. They are not the native
tensorial first variation of the written source action. Before promotion,
`I_red` needs its actual form degree, density, Krein pairing, Hodge, full BCH,
and source-coordinate variation assembled together.

There is also a gauge-placement kill gate. Unlike the tensorial distortion,
an actual connection transforms inhomogeneously. Infinitesimally the proposed
pairing acquires

\[
\langle D_q\zeta,\mathscr S(F)\rangle
=d\langle\zeta,\mathscr S(F)\rangle
-\langle\zeta,D_q^!\mathscr S(F)\rangle.
\]

An exact compact-support plant leaves a nonzero bulk value `-1/6`. Therefore
`I_red` is viable only if a Bianchi/Noether identity and boundary condition
kill this term, or if the construction is tensorialized using a connection
difference, transgression, or curvature. It is not automatically gauge
invariant.

## Moving coefficient and curvature-owner order

At fixed reconstructed curvature, all eight named moving-Shiab coefficient
slots are live. Across the ten physical metric directions their combined
local response has `339` rows and rank `10` in the declared Clifford gauge.
This is not a complete or global metric-owner rank.

The remaining curvature route factors as

\[
L_g=D_GF_{\rm spin}\circ D_gG_Y.
\]

`D_GF_spin` is second order in a total-metric variation `H`. Because the
Zorro horizontal metric contains `Gamma(g)`, `D_gG_Y` is first order in the
base variation `h`. Thus raw `L_g` is order three in `h` and can be built from
the background total-metric two-jet plus the induced variation two-jet
(equivalently a base-variation three-jet).

The expanded Euler owner is

\[
L_g^!E=(D_gG_Y)^!(D_GF_{\rm spin})^!E.
\]

The outer adjoint differentiates curvature-dependent coefficients. Hence
`nabla R`, a background total-metric three-jet, and after source substitution
possibly a base four-jet can enter. The exact cap must be derived from the
complete coefficient/order ledger.

This curvature route is one isolated missing part, not the only unbuilt metric
term. The native explicit-`q_red`, pairing, density, Krein-lowerer, and
fixed-source graph adjoints must also be reconciled in the same action.

The conformal plant `g_a=e^{2ax^3}(dx^2+dy^2)` proves only the needed
distinction: all `a` share the same metric two-jet at the origin, while
`partial_x R(0)=-12a`. It proves that a two-jet does not determine the first
curvature derivative; it does not say raw `D_gF` needs a background third
jet.

## Nonlinear reduction opportunity

Explicit Clifford polynomials in `A=Alt(T)` populate all quotient grades that
the linear bridge misses:

- degree two: grades `10` and `14`;
- degree three: two Hodge-related grade-`7` channels;
- degree four: two distinct grade-`6` Clifford-word channels, one obtained by
  Hodge-dualizing a grade-eight word.

With the two linear channels this is an eight-coefficient trial family, not a
complete equivariant census. The declared words depend only on `A=Alt(T)`, so
their derivative factors through a `364`-dimensional image: their rank is at
most `364` into `8165`, leaving at least `7801` transverse directions. A more
general zero-jet concomitant using every component of `T` has the weaker
ceiling `1274`, leaving at least `6891`. The selected sample's two grade-seven
supports and two grade-six supports are pairwise disjoint. First-jet,
nonlocal, or constrained-submanifold completion remains open.

## Observation split

Ordinary pullback of a thirteen-form to `X4` is zero. Relative to the `4+10`
base/fibre split, the thirteen legs divide as

```text
4 legs: (horizontal 3, vertical 10)
9 legs: (horizontal 4, vertical 9)
```

Ordinary ten-fibre integration can retain only the first four, producing base
three-forms of the right degree to pair with connection variations. It kills
the other nine unless another vertical contraction/current is supplied. The
metric fibre is noncompact, so even the four eligible legs require orientation
and proper or compact vertical support.

An equation-dual `L^!` obtained from a specified observation-variation lift is
not the same map as fibre integration. It must independently pass overlap
descent and the existing leakage controls.

## External datum and scope

P1/P2/P3 remain unchanged and unused. None supplies `c3:c11`, `lambda_red`,
the higher BCH terms, action placement, the curvature-adjoint order ledger,
observation support/dual, BV differential, or analytic domain.

This gate claims no stationary vacuum, Standard Model recovery, generation
count, hyperbolicity, positivity, BV phase space, or cosmological prediction.
Curt remains formally separate inside the Eric lane. `TG-1 AND TG-2 AND TG-3`
remains `NOT_PROMOTED`.

## Next gate

The highest-information successor is

`ECW3D-B2C15R2-FULL-BCH-REDUCTION-ACTION-PLACEMENT-AND-CURVATURE-ADJOINT-ORDER`:

1. compute the next live BCH `h` term and test whether the all-orders
   connection still depends only on `Delta`, or find the first ratio-sensitive
   invariant;
2. derive or reject the action placement of `q_red`; if retained, write the
   full `lambda_red` term with degrees, density, Krein pairing, and reality,
   then prove its Bianchi/Noether identity and boundary law or replace it by a
   tensorial connection difference, transgression, or curvature term;
3. assemble `D_GFspin`, `D_gG_Y`, their formal adjoints and Green terms, and
   derive rather than assume the required background/variation jet caps;
4. separately test a properly supported fibre-Gysin route for the four
   eligible `(3,10)` legs and an equation-dual route from a specified lift;
5. only after an actual action and observation condition exists, compute the
   independent constraint rank and coefficient surplus.

Do not spend the datum, normalize `Delta`, or begin BV/domain work before
those action and observation maps exist.
