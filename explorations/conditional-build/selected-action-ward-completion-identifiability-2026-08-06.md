---
artifact_type: construction_target_and_owner_scope_correction
created: 2026-08-06
status: WARD_COMPLETION_TARGET_EXACT__AFFINE_DIMENSION21__SAME_I1B_DIRECT_PACKET_OPEN
source_return: SOURCE-CONFIRMS_AND_SOURCE-SILENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_ward_completion_identifiability_probe.py
registry: lab/process/selected-action-ward-completion-identifiability.json
---

# Selected-action Ward-completion identifiability

## Result first

The exact diffeomorphism residual from v0.30 is repairable, but Ward symmetry
does not determine the completed action.

For each timelike, spacelike and null covector, write `H_spin` for the
stationary selected-action spin-Levi-Civita Hessian and `D` for the rank-four
metric diffeomorphism symbol. A symmetric same-action companion `C` must obey

\[
 C D=-H_{\rm spin}D. \tag{1}
\]

The exact rational system has rank 34 inside the 55-dimensional space of
symmetric metric coefficients. It is compatible on all three causal orbits,
so symmetric completions exist. But they form a 21-dimensional affine space:
Ward fixes the gauge columns and leaves an arbitrary symmetric bilinear form
on the six-dimensional metric quotient.

This gives the construction a much sharper target while refusing a fit. The
if the completed first-layer `I1B` is to satisfy that Ward standard, its
missing companion must come from the **same first-layer action `I1B`**: its
explicit metric, coframe, Hodge, Shiab, Krein, density, field and moving-
observation variations. A separately diffeomorphism-invariant Einstein block
already kills `D`, so adding it cannot cancel a nonzero `H_spin D`. The
observer full-`II` functional is additionally a distinct action owner; it
cannot be imported into `I1B` without the still-open owner map. Invertible
observation only transports the residual and preserves its rank three.

No counterterm, coefficient, field, quotient or datum is added.

## Plain English

The last wave found that one piece of the action still pushes in three gauge
directions where the completed theory must push in none. This wave asks how
much that fact tells us about the missing pieces.

It tells us a lot, but not everything. Of the 55 entries in a symmetric
ten-by-ten metric Hessian, the requirement of diffeomorphism symmetry fixes 34
directions. The remaining 21 are the actual dynamics on the six metric
directions left after quotienting gauge. So symmetry gives us an exact test
for the next calculation; it does not give us permission to choose the
physical coefficients.

It also removes a misleading shortcut. Adding an ordinary Einstein or other
already gauge-invariant action cannot repair this particular defect, because
such a block is zero on the gauge directions already. The cancellation has to
come from the metric and frame dependence omitted when we isolated the spin-
connection contribution of the same GU action.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| isolated residual | `H_spin D`, rank three | a failure of the complete action |
| same-action companion | omitted explicit metric/coframe/Hodge/Shiab/Krein/density/field/observation variation of `I1B` | an added counterterm |
| invariant Einstein control | a separately diffeomorphism-radical Fierz--Pauli Hessian | the missing non-invariant decomposition piece of `I1B` |
| observer full-`II` | separate functional `I_II` | `I1B` or `I2B` without a constructed owner map |
| Ward target | any symmetric `C` satisfying (1) | an action-derived completion |
| observation | invertible first-germ congruence with transported gauge generator | dynamical cancellation |
| quotient form | the 21-dimensional ambiguity after (1) | a fifth ranked physical quotient |

The first-layer transgression action, its second-layer residual norm square and
the observer full-`II` action remain the three distinct owners established in
v0.24.

## Source collision

At UCSD `00:25:03--00:25:56`, Weinstein describes Einstein's corrected tensor
as “perpendicular to orbits under the diffeomorphism group” and immediately
ties that fact to being exact for the scalar-curvature action. This confirms
the Ward/radical standard used here. His sources also retain the gauge-rotated
Levi-Civita/two-connection route.

They do not provide the direct `I1B` metric/coframe coefficients, the
`34+21` count, an `I1B/I2B` to observer-full-`II` map, or the BV/BFV and domain
completion.

```text
SOURCE-CONFIRMS: diffeomorphism-orbit perpendicularity as an action identity,
                 gauge-rotated Levi-Civita and two-connection route
SOURCE-SILENT:   direct companion coefficients, 34+21 count, owner map,
                 BV/BFV and analytic completion
```

## Exact Ward-completion theorem

The metric coefficient carrier is `Sym2(R^10)`, dimension 55. For every
nonzero causal-orbit representative, `rank D=4`. Define

\[
 \mathcal L_D:\operatorname{Sym}^2(\mathbb R^{10})\longrightarrow
 \operatorname{Mat}_{10\times4},\qquad C\longmapsto CD. \tag{2}
\]

Exact row reduction gives

\[
 \operatorname{rank}\mathcal L_D=34,
 \qquad \dim\ker\mathcal L_D=55-34=21. \tag{3}
\]

The target `-H_spin D` lies in the image because the stationary compatibility
matrix `D^T H_spin D` is symmetric. Thus (1) is solvable. If `C_0` is one
solution, every solution is

\[
 C=C_0+ZKZ^T,\qquad K\in\operatorname{Sym}^2(\mathbb R^6), \tag{4}
\]

where the columns of `Z` span `ker D^T`. Equation (4) proves that the 21
unfixed directions are precisely symmetric forms on the metric quotient.

## Diagnostic completion, not a construction

For a planted finite target, choose the Euclidean slot projector

\[
 P=1-D(D^TD)^{-1}D^T,
 \qquad C_0=P^TH_{\rm spin}P-H_{\rm spin}. \tag{5}
\]

It satisfies (1) exactly. Its completion rank/inertia and total rank are

| orbit | `rank C_0` | `inertia C_0` | `rank(H_spin+C_0)` |
| --- | ---: | ---: | ---: |
| timelike | 3 | `(0,3,7)` | 6 |
| spacelike | 3 | `(1,2,7)` | 6 |
| null | 6 | `(3,3,4)` | 2 |

These numbers are a regression target only. The Euclidean coefficient-space
projector in (5) is not Lorentz-natural, not sourced and not selected by the
action. Adding any nonzero `ZKZ^T` gives a different exact completion, which
is the planted proof against silently promoting (5).

## Wrong-owner theorem

The exact Fierz--Pauli/linearized-Einstein control is symmetric,
diffeomorphism-radical and has causal-orbit ranks `6,6,4`. Hence for every
coefficient `a`,

\[
 (H_{\rm spin}+aH_{\rm Einstein})D=H_{\rm spin}D. \tag{6}
\]

This is a type theorem, not a rejection of Einstein or full-`II` physics. A
separately invariant stationary action cannot cancel a residual confined to
one non-invariant decomposition piece. The cancellation must be among pieces
of the same natural action, unless an explicit owner map and common stationary
background are first constructed.

Likewise, under an invertible observation change `O`,

\[
 H'=O^THO,\qquad D'=O^{-1}D,
 \qquad H'D'=O^THD. \tag{7}
\]

The exact residual rank remains three. Observation can expose or transport a
companion term, but coordinate congruence alone cannot manufacture one.

## Queue correction

The former rank-one phrase “direct curvature/full-II/defect/observation” was
too broad. It could invite a second action owner into the first action's Ward
identity. The corrected order is:

1. expand the same-`I1B` explicit metric/coframe/Hodge/Shiab/Krein/density/
   field/observation second variation;
2. require its gauge columns to match the 34 fixed Ward directions in (1),
   while letting the written action determine the 21 quotient coefficients;
3. only then construct diffeomorphism/odd BV, the global domain and BFV;
4. keep `I2B <-> I_II` and `LT-GR3` as the separate second queue.

This is construction guidance generated by the written action and its Ward
failure, not hardening for its own sake.

## Ledger v0.31

```text
Ledger v0.31 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances migrate. Verdicts, reason kinds, revival triggers, residue,
quotients and P1/P2/P3 do not move.

## Seven-axis disposition

- **Layer 0:** same-action companion, separate invariant action, observation
  transport, Ward target and physical quotient are separated.
- **L1 syntactic:** equation (1) names the missing coefficient block.
- **L2 type:** its owner is the explicit metric/frame dependence of `I1B`.
- **L3 algebraic:** rank 34, affine dimension 21, causal controls and
  observation transport are exact.
- **L4 geometric:** local observed Lorentz coefficient only; the diagnostic
  projector is explicitly non-natural.
- **L5 variational/symplectic:** the stationary Ward target closes;
  action-derived completion and BV/BFV remain open.
- **L6 analytic:** no global Green/Krein or hyperbolic-domain claim.
- **L7 physical:** no Einstein recovery, graviton, cosmology, Q1 or unitarity
  claim.

## Constraint fence

```text
new fields: 0
new coefficients: 0
new counterterms: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

## K123 successor closure — 2026-08-15

K123 turns the open same-action packet into a rank-two native coefficient
deficit on the selected TT control. Equation (1) remains a mandatory Ward
check, but its 21-dimensional quotient-form freedom proves it cannot select
the two TT cubic numbers. K124 must derive them from the common full-14D
`I1B` evaluator and only then test the Ward columns; the diagnostic completion
is not an admissible coefficient source.

## K124 principal-TT successor closure — 2026-08-15

K124 derives the principal values directly, without using this Ward family:
`C_t_h_h^prin=-12q^2<DW>` and `C_t_h_v^prin=0`. Retest the Ward columns only
after K125 completes the lower-order/noncyclic-Cartan packet; the
21-dimensional quotient freedom remains unavailable for fitting.
