---
title: "PW2D actual Y14 transported Shiab, quadratic action jet, and residual right-tilted Ward"
status: active_research
doc_type: construction_result
created: 2026-08-02
branch: agent/null-clifford-omega1-repair
run: private orchestration runtime#meta/runs/historical-investigation/run-plan.md
registries:
  - lab/process/pw2d-native-transported-shiab-action.json
  - lab/process/pw2d-right-tilted-ward-green-registry.json
probes:
  - tests/channel-swings/pw2d_native_transported_shiab_action_probe.py
  - tests/channel-swings/pw2d_right_tilted_ward_green_probe.py
grade: "PW2D PARTIAL LOCAL ACTIVE-COMPONENT PASS WITH A REPAIRED DELTA-ONLY BOUNDARY. A fixed-metric covariance-completed Shiab family, literal full-K split, normalized curvature/transgression, and the written kappa1/2 mass sector are evaluated on the B2C15P Y14 fixture. Independent differentiation gives the correct Q-family tangent identity and zero explicit transported-grade-projector response on this fixture; the original projector-failure claim is retracted. Linear response cancels. Curvature second response is 3/8, unweighted mass second response is 2, and full response is 3/8+kappa1, so it is Delta-only but can vanish at kappa1=-3/8. The eight moving-Shiab metric slots remain a separate zero-jet rank-ten coefficient bank, not a mixed action/Euler rank. Separately, an exact GL(2) structural comparator proves the residual right nonabelian Ward identity and, after hostile repair, an explicit old-root Frechet adjoint plus a separate Green layer. The public-to-active port, explicit finite native Q/projector construction, mixed/full Z0+Z1 metric Frechet graph, three-patch coefficient descent, higher action jet, native all-owner Ward, composite reality checks, domain, BV/BFV, observation no leakage, and physics recovery remain open."
canon_verdict_change: none
---

# PW2D actual Y14 transported Shiab and residual right-tilted Ward

## Result first

PW2D finally puts the literal bridge and an actual native Y14 coefficient in
the same calculation. It produces one positive construction and one sharp
limitation.

On the active local `Sp(32,32;H)/Spin0(9,5)` component, transport

\[
Q_s=\operatorname{Ad}_{e^{-su}}Q,
\qquad
p_s=\operatorname{Ad}_{e^{-su}}p\operatorname{Ad}_{e^{su}},
\]

and use

\[
K_s=e^{-su}D_Be^{su}
=\sum_{n\ge 0}\frac{(-1)^n s^{n+1}}{(n+1)!}
\operatorname{ad}_u^n(D_Bu).
\]

The hostile review caught a sign error and a circularly defined projector
term. In the executable left-commutator convention, the corrected tangent
identity is

\[
D_Q\mathscr S(F)-\mathscr S([u,F])=-[u,\mathscr S(F)].
\]

The declared projector `p_s=Ad(e^{-su})pAd(e^{su})` is differentiated
independently on the pre-projection source and gives zero on this curvature
fixture. The separately derived Q/Phi-family tangent is live on all four
nonzero members and agrees with the finite covariance-completed operator
tangent; freezing that Q/Phi family fails four times. This tangent result does
not construct the finite public/native operator through second order. The
panel is

\[
(0,0),\quad(1,0),\quad(5/3,4/3),\quad(1,1),\quad(1,-1).
\]

After normalizing the written source block as

\[
F_B+\frac12D_BT+\frac13q(T,T)
=\frac12(F_A+F_B)-\frac16q(T,T),
\]

the fixed-total-connection substitution is

\[
\widehat B=B+K_s,
\qquad
\widehat T=T-K_s,
\qquad
\widehat Q=Q_s.
\]

Including the written `kappa1/2` mass term, the exact fixed-metric local action
jet has responses

```text
linear:             0, 0,             0,             0, 0
curvature second:   0, 3/8,           3/8,           0, 0
mass-norm second:   0, 2,             2,             0, 0
full second:        0, 3/8 + kappa1,  3/8 + kappa1,  0, 0
```

Thus the full linear response cancels. The quadratic response remains a
function only of

\[
\Delta=c_3^2-c_{11}^2
\]

on this preregistered fixture. Equal-`Delta` pairs coincide and both nonzero
Hodge-null branches vanish. The response is not unconditionally nonzero: it
cancels at `kappa1=-3/8`. This does not prove an all-orders `Delta` theorem,
and it prevents using the quadratic local action as a coefficient selector.

The separate nonabelian result is also substantive. The derivative-bearing
cocycle

\[
q_A(g)=A-\operatorname{Ad}_gA+(dg)g^{-1}
\]

closes the tilted graph. The left action fixes the descended distortion, while
the residual right action is adjoint. In moving-owner variables,

\[
\delta_c C=-D_Cc,
\qquad
\delta_cT=[c,T],
\qquad
\delta_cQ=[c,Q],
\qquad
\delta_cg=0.
\]

For an equivariant `h(T,Q,g)`, literal `K_full` is tensorial:

\[
\delta_cK_{\rm full}=[c,K_{\rm full}].
\]

The exact nonabelian differential comparator has live connection,
distortion, and moving-reduction Euler owners and satisfies

\[
\boxed{
D_CE_C+[T,E_T]+[Q,E_Q]=0.}
\]

Its Ward bulk and boundary are separately nonzero:

```text
bulk integral = 38
boundary      = -38
```

A separate exact conjugation-equivariant local `GL(2)` map
`h(T)=I+T/5=exp(log(I+T/5))` verifies more than the initial forward check.
Generic old-root variations are integrated by parts to construct
`(DF)^! E_hat` explicitly; the resulting owner tuple agrees with an
independent raw pulled-action integration. A separate nonzero graph Green
term is required, so

\[
\Theta_{\rm total}=F^*\widehat\Theta+\mathcal G_{DF}.
\]

The repaired endpoint is `243073/216000`. A component-extraction version of
`h` was killed because it made `K_full` non-tensorial. This is a structural
`GL(2)` comparator, not active `Sp(32,32;H)` membership or the native Shiab
Ward theorem.

## Plain English

The bridge now enters a fixed-metric GU-shaped action fixture with the omitted
mass term restored. The hostile review also removed a false success: the
projector was not the missing moving term. Its explicit derivative is zero
here; the live motion belongs to the Q/Phi coefficient family.

But the first two bridge orders do not choose a mixture of the grade-three and
grade-eleven routes. First order cancels; second order sees only one
combination, `Delta`, and the full response can cancel for one value of
`kappa1`. So this particular action jet still does not fix the bridge.

The symmetry problem is in better shape at structural-comparator grade. The
nonabelian right-tilted Ward identity needs the moving reduction owner and a
live boundary term, and its full-K graph now has a real formal adjoint rather
than only a forward variation. The native all-owner Ward remains open.

## Layer 0

| object | type | status |
| --- | --- | --- |
| public source bundle | public complex/Krein `U/(7,7)`-presented bundle | not identified with active real bundle |
| active native component | local `P_mix/Sp(32,32;H)/Spin0(9,5)` | executable scope |
| `Q,p` | Clifford reduction and its endomorphism projector | Q-family tangent live; explicit projector tangent zero here; finite native construction open |
| `K_full` | full connection difference `h^-1 D_B h` | constructed in the action jet |
| `K_red` | grade-two projection of `K_full` | kept distinct and unused as replacement |
| left tilted action | source-coordinate redundancy fixing descended distortion | exact G1 replay |
| residual right action | nonabelian gauge action on the quotient | exact Ward comparator |
| `Xi=D Upsilon` | displayed Euler redundancy | not a Ward identity |
| actual native Ward | Ward return of the complete native hatted Euler action | still open |
| observed equation | descended equation with no leakage | still open |

## The unexpected `ker Alt` split

The action-dual trace-line coefficient legs have the form index that is
missing from the thirteen-form inside their Clifford two-blade. Alternating
that one-form index with that two-blade therefore gives zero. All thirteen
actual coefficient-dual legs are checked individually and lie in `ker Alt`.

The bridge is not dead: a separately declared repository-chosen lexicographic grade-two source
component has nonzero `Alt(T)` and couples after transport. But the result
means the direct action pairing and the bridge are complementary source
sectors. They cannot be silently treated as one component.

## Native metric owner bank

All eight actual internal coefficient slots remain live on the normalized
source residual:

1. trace Clifford contraction;
2. first `Phi1`;
3. first Hodge star;
4. outer `Phi1`;
5. `Phi2`;
6. inner Hodge star;
7. middle Hodge star;
8. outer Hodge star.

The ten trace-reversed metric owners give coefficient-valued Shiab rank ten.
This is not an action or Euler rank: only four of ten have a nonzero frozen
pairing. The curvature-input derivative is kept separate rather than counted
as a ninth coefficient slot.

This is a separate exact zero-jet metric bank. It is not evaluated jointly
with `K_full`, `T_hat`, or the transported Q family. It does not yet include
the complete

\[
Z_0[m]+Z_1[\nabla m]
\]

total-space metric Frechet graph, the fixed-`varpi` Levi-Civita return, or the
full effective operator

\[
A_2(2\partial Z_1+Z_0)+A_1Z_1.
\]

Trace reversal itself remains exact: the native fibre/total inertias are
`(6,4)/(9,5)` with trace norm `-4`, while unreversed Frobenius has fibre
inertia `(7,3)` and trace norm `+4`. That rejects their identification as the
same metric, but it is not yet a live positive-Hilbert substitution test in
the composed action. Likewise, prior PW2B grade-3/11 membership does not
recertify every PW2D composite under right-H, Krein, and `C+`.

## Source collision

- `SOURCE-CONFIRMS`: source roots, homogeneous two-connection distortion,
  fixed `1/2` and `1/3` completion, left/right tilted grammar, gauge-rotated
  connection, and trace reversal.
- `SOURCE-CORRECTS`: the left kernel, residual right action, field
  substitution, and `Xi` redundancy are four different objects.
- `SOURCE-SILENT/REPOSITORY-DERIVED`: the active quaternionic port,
  grade-3/11 bridge, the all-thirteen-leg `ker Alt` split, transported `Q/p`,
  covariance-completed action jet, structural nonabelian Ward boundary,
  total metric Frechet graph, BV/BFV, domain, and observation no-leakage
  theorem.

The spoken double-coset identification with connection moduli also remains
conditional when the Levi-Civita reference moves. The exact G1 object is the
fixed-reference double-action groupoid; a moving-reference equivalence is an
additional theorem.

## External datum and lanes

P1/P2/P3 remains unchanged and unused. None has the type of a real bundle
port, finite moving reduction/projector, continuous coefficient selector, Ward differential,
Green boundary, analytic domain, or no-leakage map.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`.
`TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.

## Boundary and next gate

PW2D does not construct the public-to-active bundle equivalence, actual
three-patch coefficient descent, explicit finite second-order Q/projector
operator, mixed bridge-by-metric derivative, complete `Z0+Z1` metric Frechet
owner, composite right-H/Krein/C+ certificate, third/fourth action jet, native
all-owner hatted-Euler Ward, common Green domain, graded BV/BFV/CME, physical
quotient, observed no-leakage equation, coefficient selection, constraint
surplus, or SM/GR/quantum/cosmological recovery.

The next gate is
`PW2E-FULL-Z0Z1-METRIC-FRECHET-COEFFICIENT-DESCENT-AND-HIGHER-ACTION-JET`:

1. build the full `D_g G_Y=Z0+Z1` bridge and fixed-`varpi` metric return;
2. put the transported native coefficient on an exact three-patch active
   atlas and require dual descent before reading Ward;
3. compute the cubic and quartic native action jets on the frozen five-pair
   panel to determine whether the `Delta` degeneracy persists;
4. compose the actual native hatted Euler covectors with `(D F)^!`, Green,
   and the residual right-tilted generator;
5. only after those close, revisit effective order/rank, observation, and
   constraint surplus.

PW3 remains blocked.
