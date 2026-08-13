---
title: "K77 Wave 2: the trace-reversed metric fibre owns q, but Ward covariance does not select its D916 placement"
status: active_research
doc_type: construction_result
created: 2026-08-04
gate: RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD
result: "PARTIAL__TRACE_REVERSED_TAUTOLOGICAL_Q_GEOMETRY_OWNED__LEFT_RIGHT_ADJOINT_EXCHANGE_AND_CURRENTS_EXACT__WARD_DOES_NOT_SELECT_COEFFICIENT__ZERO_ORDER_REALITY_FULL_H_OPEN"
canon_verdict_change: none
---

# K77 q-receiver ownership / adjoint / Ward selection

## Result first

The odd Clifford receiver required by the preceding D916 repair does **not**
need to be introduced as a new free direction.  The actual metric bundle
already carries a canonical candidate:

\[
Y=\operatorname{Met}_{3,1}(X),
\qquad
V_{(x,g)}Y\simeq\operatorname{Sym}^2T_x^*X,
\qquad
t_{(x,g)}=g.
\]

The point `g` in the open metric fibre is itself its tautological vertical
Euler/trace vector.  With the trace-reversed Frobenius--DeWitt form

\[
G_{\rm DW}(h,k)
=\operatorname{tr}(g^{-1}hg^{-1}k)
-\frac12\operatorname{tr}(g^{-1}h)\operatorname{tr}(g^{-1}k),
\]

the four-dimensional trace vector satisfies

\[
G_{\rm DW}(g,g)=4-\frac12(4)^2=-4.
\]

Therefore

\[
\boxed{q_g=\frac12g}
\]

is a nowhere-zero, unit negative, natural vertical section.  Since the
chimeric Clifford bundle is `C=V plus H-star`, `q` is already of the exact odd
Clifford-vector type needed by the previous repair.  The earlier language
“odd covector” is corrected: `q` is first a Clifford vector; the chimeric
metric supplies its musical covector.

This changes the provisional constraint invoice materially:

```text
free-q projective parameters:       13 -> 0
left/right projective coefficient:       1
current selecting-constraint rank:       0
constraint surplus:                -14 -> -1
```

The sign is canonical as well: `t_g=g` is the positive radial Euler section,
not merely an unoriented line.  Replacing `g` by `-g` also changes the chosen
Lorentz-signature component.  P1 is not consumed, and no new `q` datum is
added to P1/P2/P3.

The placement question does not close.  For the native middle symbol

\[
A(\xi)_a{}^c
=\delta_a^c\gamma(\xi)-\xi_a\gamma^c,
\]

the two repaired maps

\[
L_q(\xi)=\gamma(q)A(\xi),
\qquad
R_q(\xi)=A(\xi)\gamma(q)
\]

remain independent.  Their sum and difference are the natural eigenbranches:

\[
\begin{aligned}
L_q+R_q
&=\{\gamma(q),A(\xi)\},\\
L_q-R_q
&=[\gamma(q),A(\xi)].
\end{aligned}
\]

The anticommutator collapses exactly to a scalar-on-spinors tensor map,

\[
\{\gamma(q),A(\xi)\}_a{}^c
=2\left(\delta_a^c\langle q,\xi\rangle
-\xi_aq^c\right)\mathbf1,
\]

while the commutator is an even bivector-valued Clifford map.

With the complete one-form-index times spinor Krein pairing, adjunction
exchanges left and right:

\[
L_q(A)^\times=-R_q(A^\times),
\qquad
R_q(A)^\times=-L_q(A^\times).
\]

Consequently the commutator and anticommutator diagonalize the algebraic
adjoint exchange.  When `q` moves, the formal adjoint of `P(x) partial_x`
contains

\[
(P\partial_x)^\times
=-P^\times\partial_x-(P^\times)',
\]

and the `dq` term is nonzero.  The exact fixture verifies that its placement
also exchanges left and right; freezing `q` deletes a live lower-order term.

Both `q` and one actual even spin-connection direction emit nonzero,
placement-sensitive fermion currents.  Two held-out responses have exact rank
two, so downstream equations can distinguish the coefficient pair.  But
sensitivity rank is not constraint rank: no source Euler equation presently
sets either response to a target value.

Finally, both left and right families descend when `q`, `xi`, the form
indices, and spinors move together.  Therefore the differentiated Ward
identity transports **every** linear combination and has coefficient-selection
rank zero.  Ward covariance cannot choose the placement.

The exact probe passes:

```text
6 source + 20 type + 25 exact + 5 planted = 56 PASS
```

Wave 2 remains partial.  Wave 3 does not open.

## Plain English

The last swing found that the fermion operator needed one additional
direction, `q`, to make its chiral bookkeeping coherent.  At first that looked
expensive: choosing a direction in fourteen dimensions costs thirteen
continuous choices.

Trace reversal changes that.  Every point of the observerse's metric fibre is
itself a metric.  That metric points radially through the fibre and gives a
distinguished trace direction everywhere.  After trace reversal it has
exactly the negative norm needed to act as `q`.  So the geometry supplies the
direction for free; we do not need an observer-aether vector or another
external datum.

The unresolved question is where to put it in the operator.  Multiplying the
old contraction by `q` on the left and on the right gives two different maps.
The Krein adjoint swaps them, and their symmetric and antisymmetric
combinations have clean algebraic meanings.  But gauge covariance respects
both.  It tells us how the entire two-dimensional family moves, not which
member nature uses.

The next decision therefore has to come from the actual zero-order connection
blocks, barred/unbarred reality convention, and full moving action—not another
symmetry slogan and not a new datum.

## 1. Layer 0

| phrase | object at this gate | not identified with it |
| --- | --- | --- |
| `q` | a section of the chimeric Clifford vector bundle `C` | initially a covector, external bit, or coefficient |
| tautological trace `t` | `t_(x,g)=g` in the vertical `Sym2 T-star X` fibre | an internally rotated trace spurion `tau` |
| normalized trace receiver | `q=t/2`, with DeWitt norm `-1` | a free projective direction |
| observation vector `u` | a future unit timelike base vector after an observer reduction | the vertical trace vector |
| metric section `s:X->Y` | a chosen Lorentz metric on `X` | needed to define `t` on `Y` itself |
| `epsilon` | the source gauge conjugator | an extra vector index |
| `epsilon_IG` | the already-varied moving Clifford-plane/soldering field | the owner of the tautological trace formula |
| augmented torsion | an ad-valued one-form | a chimeric vector without an adapter |
| source coefficient bracket | commutator or `i`-Jordan operation in the coefficient/Lie factor | the new Clifford left/right product |
| P1/P2/P3 | existing orientation/phase and relative-KO data | `q` or its coefficient |

This final row about brackets is load-bearing.  The draft's “magic bracket”
can choose commutator or `i` times anticommutator in the coefficient algebra.
Our sum/difference multiplies the Clifford receiver and the form-spinor
contraction.  The words match, but the factors do not.  No selection is
inferred without a typed map between them.

## 2. Primary-source collision

The source record supports two parts of this construction and is silent on the
third:

| claim | disposition |
| --- | --- |
| the vertical fibre uses trace-reversed rather than raw Frobenius | `SOURCE-CONFIRMS` |
| the pointwise metric space has one distinguished direction | `SOURCE-CONFIRMS` |
| the correction changes `(7,3)` to the `Spin(6) x Spin(4)` route | `SOURCE-CONFIRMS` |
| insert the normalized trace vector into equation 9.16 | `SOURCE-SILENT` |
| uniquely choose left, right, sum, or difference | `SOURCE-SILENT` |

The `00:20:51--00:29:16` Weinstein--Jaimungal passage explicitly corrects raw
Frobenius to trace-reversed Frobenius and connects that choice to the
`Spin(6) x Spin(4)` route.  The Into the Impossible transcript describes “the
one dimension that's distinguished in the space of all metrics.”  Neither
source writes `q=t/2` into D916.

Accordingly this result is a source-compatible conditional construction, not
an attribution that Weinstein supplied the repaired fermion operator.

## 3. Why the trace receiver is canonical

For fixed Lorentz signature, each fibre of `Met(X)` is an open subset of the
vector space `Sym2 T-star X`.  The radial Euler vector is therefore tangent:

\[
t_{(x,g)}
=\left.\frac{d}{ds}\right|_{s=0}e^s g
=g.
\]

It is natural under every base change `L`:

\[
g\mapsto L^TgL,
\qquad
t_g\mapsto L^Tt_gL=t_{L^TgL}.
\]

The executable checks this with an exact unimodular change of frame and the
intrinsic DeWitt formula.  It also gives an explicit congruence decomposition:

- raw Frobenius has four positive diagonal directions, three positive spatial
  off-diagonals, and three negative time-space off-diagonals: `(7,3)`;
- trace reversal changes only the trace line, yielding `(6,4)`;
- the three diagonal traceless directions remain positive;
- the trace line becomes negative with norm `-4`.

In a local orthonormal K77 frame, `q` is one negative Clifford generator, so

\[
\gamma(q)^2=-1,
\qquad
\gamma(q)J=-J\gamma(q).
\]

This is exactly the half-spinor flip that the preceding `D7` Hom computation
said one supplied vector would provide.

### 3.1 What this does not own

The trace line does not construct RB4's full Cartan four-plane, compatible
complex structure, or Standard Model reduction.  Under a base Lorentz action
the canonical trace direction is fixed; under a generic selected internal
`Spin(4)` motion it moves away from the trace line and becomes a different
spurion `tau`.  This swing uses only the native tautological `t`, not the full
moving flag.

## 4. Multi-index Krein adjoint

Let the one-form pairing be

\[
K_1=\operatorname{diag}(\eta_1B,\ldots,\eta_{14}B),
\]

where every real K77 Clifford generator is `B`-skew:

\[
B\gamma_a^TB=-\gamma_a.
\]

For a block map `P_a^c`,

\[
(P^\times)_c{}^a
=\eta_a\eta_cB(P_a{}^c)^TB.
\]

Applying this to all `14 x 14` blocks proves the left/right exchange above.
This is stronger than a spinor-only transpose and weaker than a full global
D916 adjoint: the source Hodge, density, moving pairing, connection, and all
sixteen zero-order blocks still have to be assembled.

## 5. Variations and currents

For coefficients `(alpha,beta)`,

\[
P_{\alpha\beta}
=\alpha\gamma(q)A+\beta A\gamma(q).
\]

The local bilinear emits

\[
\begin{aligned}
\delta_qP
&=\alpha\gamma(\delta q)A
+\beta A\gamma(\delta q),\\
\delta_AP
&=\alpha\gamma(q)\delta A
+\beta\delta A\gamma(q),\\
\delta_\alpha P&=\gamma(q)A,\\
\delta_\beta P&=A\gamma(q).
\end{aligned}
\]

The executable evaluates the first line and one actual even spin-connection
direction against nonzero barred/unbarred one-form spinors.  Both responses
are nonzero and placement-sensitive; their `2 x 2` exact determinant is
nonzero.

Because `q` is composite,

\[
D_gq[\delta g]=\frac12\delta g
\]

in the canonical vertical identification.  Its current is therefore pulled
back into the metric/soldering Euler equation:

\[
\mathcal E_g
\supset(D_gq)^!\mathcal E_q.
\]

There is no separate `q` Euler field.  The complete chain rule must also vary
the DeWitt metric, Clifford frame, Hodge star, density, connection, and Krein
pairing.

## 6. Ward identity and symmetry boundary

For an even moving Clifford transition `h`,

\[
q\mapsto hq,
\quad
\xi\mapsto h\xi,
\quad
A\mapsto hAh^{-1}.
\]

Both `L_q` and `R_q` intertwine exactly.  Every linear combination therefore
intertwines, so differentiating the family gives a Ward identity for arbitrary
`alpha,beta`.  Its coefficient-selection rank is zero.

This is associated-bundle covariance on the moving real-K77 reduction.  It is
not yet invariance under the full fixed `U(64,64)`-type source group.  A fixed
nonzero Clifford vector has a stabilizer; the existing `epsilon_IG` can carry
the associated vector only after the real-K77/Clifford reduction is accepted.
The next action must either establish that descent or name the honest reduced
group.

## 7. Constraint surplus

The old invoice treated `q` as a free pointwise projective vector:

\[
13\text{ q parameters}+1\text{ placement parameter}.
\]

The tautological trace construction sets the first term to zero.  The current
and Ward calculations reveal sensitivity to the placement but no equation
that selects it:

\[
\operatorname{surplus}=0-0-1=-1.
\]

This is a genuine improvement from `-14`, not closure.  The efficient next
move is to write the trace receiver into the complete source-shaped sixteen
blocks and let zero-order reality and action variation supply—or fail to
supply—the missing independent equation.

## 8. Divergent specialist pre-assessment

The ten inline lenses predicted:

1. source confirmation for trace reversal but silence on D916 insertion;
2. a natural tautological vertical Euler section;
3. a Clifford-vector rather than initially covector type;
4. left/right exchange only after the full form-spinor Krein pairing;
5. mandatory nonzero `dq` terms;
6. no domain conclusion from formal adjunction;
7. composite-current routing into the metric/soldering equation;
8. associated-family covariance rather than fixed-vector full-group
   invariance;
9. no particle or family inference; and
10. exact identities backed by frozen-owner and wrong-pairing plants.

All ten predictions survived after the hostile repairs described below.

## 9. Hostile review repairs

The inline post-review found and repaired three summary-layer overreaches:

1. an arbitrary-frame naturality check used floating inversion while being
   called exact; it was replaced by an integral unimodular frame and exact
   integer inverse;
2. the first “connection current” varied only a one-form coefficient; it was
   replaced by an actual even spin-connection generator;
3. the source coefficient-algebra commutator/`i`-anticommutator was being read
   as support for the new Clifford sum/difference.  Layer 0 now forbids that
   homonym.

The superseded-object reviewer also checked whether the prior `-14` fence was
defending a free receiver after RB4 had already constructed the trace line.
It was.  The free-`q` parameter count is now retired on the conditional trace
branch.

## 10. Seven axes plus Layer 0

| level | disposition |
| --- | --- |
| Layer 0 | trace vector, observer vector, epsilon, soldering, augmented torsion, coefficient bracket, and Clifford placement separated |
| L1 | trace reversal/distinguished direction confirmed; D916 insertion and unique placement source-silent |
| L2 | exact DeWitt, Clifford, adjoint, `dq`, current, and moving-family witnesses |
| L3 | conditional natural section and associated Spin descent; full fixed source group open |
| L4 | no fit to data or statistical claim |
| L5 | no particle, physical chirality, family, mass, or seesaw inference |
| L6 | hostile review completed with three material scope repairs |
| L7 | exact executable, strict registry, scope audit, predecessor regression, and campaign frontier required |

## 11. Honest boundary and next gate

This swing closes `q` ownership **conditionally on the primary real-K77
trace-reversed chimeric construction**.  It does not close the common D916
action.

Still open:

- the complete sixteen trace-`q` blocks;
- the zero-order `varpi` coefficients;
- barred/unbarred `C`-reality;
- the moving Hodge, density, pairing, and Clifford-frame derivatives;
- a coefficient-selecting Euler/reality equation;
- full source-group descent or an honest reduction;
- a common Green/domain precheck; and
- all downstream observation and physics.

The next named build is

```text
K77_D916_TRACE_Q_COEFFICIENT_ZERO_ORDER_REALITY_SELECTION
```

It should construct the complete trace-`q` source matrix and decide whether
zero-order reality selects the commutator, `i`-anticommutator, left, right, or
no admissible branch.  Wave 3 remains closed until that common action exists.
