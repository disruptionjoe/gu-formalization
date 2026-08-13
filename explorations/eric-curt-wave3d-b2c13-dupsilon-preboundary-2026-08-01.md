---
title: "Eric/Curt Wave 3D-B2C13: the two bosonic residuals split at principal-symbol and finite preboundary-jet grade"
status: active_research
doc_type: construction_result
created: 2026-08-01
branch: agent/null-clifford-omega1-repair
run: private orchestration runtime#meta/runs/historical-investigation/run-plan.md
registry: lab/process/eric-curt-wave3d-b2c13-dupsilon-preboundary.json
probe: tests/channel-swings/eric_curt_wave3d_b2c13_dupsilon_preboundary_probe.py
grade: "B2C13 SPLIT CONSTRUCTION PASS. The manuscript-compressed residual and the selected G2 action's exact Euler covector are differentiated as separate operators. On the existing exact noncentral G2 fixture their principal symbols differ in 60/144 entries; a fixed-A graph-jet direction gives source response 0 and exact-G2 response 1/2. Exact polynomial residual squares return every representative graph/Shiab/Hodge/density/primalizer term and produce nonzero, unequal preboundary forms. The rational/B2C9 comparator source branch remains first order while its exact-action branch is second order and requires a prolonged Ostrogradsky packet. The active (9,5) R_res coefficient port passes separately, but nonvanishing of the corresponding active Y14 graph symbol is open. The global native Y14 Shiab first jet, trace theorem, closed domain, and mixed boson-fermion polarization remain open."
canon_verdict_change: none
---

# B2C13 residual symbols and staged preboundary jets

## Result first

The two bosonic residuals we inherited from B2C12 are not merely different
ways of writing the same equation. Their structural first-derivative symbols
differ, and the existing exact noncentral comparator proves that this
difference is nonzero and requires different boundary data there. Whether
the corresponding active `Y^14` graph symbol is nonzero is the next gate.

The manuscript-compressed branch is

\[
E_{\rm src}=\Upsilon_B^{\rm src}
=\mathscr S_{\epsilon,g}(F_{A_{\rm tr}})
+\kappa_1\flat_{\epsilon,g}T,
\qquad T=A_{\rm tr}-B_{\rm rot}.
\]

The selected G2 action actually emits

\[
E_{\rm var}
=\mathscr S_{\epsilon,g}(F_{B_{\rm rot}})
+\frac12(L+L^!)T
+M_{\epsilon,g}(T,T)
+\kappa_1\flat_{\epsilon,g}T,
\qquad L=\mathscr S_{\epsilon,g}D_{B_{\rm rot}}.
\]

Using

\[
F_{A_{\rm tr}}=F_{B_{\rm rot}}+D_{B_{\rm rot}}T+q(T,T),
\]

their difference is

\[
\boxed{
E_{\rm var}-E_{\rm src}
=\frac12(L^!-L)T
+\bigl[M(T,T)-\mathscr S q(T,T)\bigr].
}
\]

The second bracket is lower order. The first is not. It changes the
principal symbol unless the needed cyclic/formal-self-adjoint identity holds.
That identity already failed for the selected native-shaped noncentral
contraction.

The existing exact B2C9 noncentral fixture now gives a direct measurement:

```text
T-jet principal-symbol entries that differ: 60 / 144
fixed-A graph-jet source response:          0
fixed-A graph-jet exact-G2 response:        1/2
```

This is the decisive construction result of B2C13. The action correction is
not just a modified potential or mass term. It changes which normal jets
reach the boundary.

## Plain English

Imagine two recipes that produce a “failure signal” from the same fields.
One is Eric's compressed formula; the other is what our written candidate
action actually produces when every slot is varied. B2C12 showed that their
values need not agree. B2C13 shows something stronger: they respond
differently to rapidly changing fields.

When the reference connection moves while the total connection is held
fixed, the derivative pieces in the compressed formula cancel. In the
action-derived formula, half of the mismatch between an operator and its
formal adjoint survives. Because the reference connection is already built
from a first derivative of the reduction and metric, that surviving piece
makes the exact finite comparator branch second order in those graph fields.
Its active nonvanishing is not inferred.

So in the rational/B2C9 comparator the exact branch needs boundary values for
both the graph field and its first normal derivative, with a momentum paired
to each. Reusing the older first-order boundary matrix there would throw away
a real, nonzero boundary channel. The active branch needs that prolonged
packet only if B2C14 proves the analogous active graph coefficient nonzero;
an active zero would instead collapse the order.

## Layer 0: objects that remain separate

The gate keeps the following distinctions load-bearing:

| object | meaning | not identified with |
| --- | --- | --- |
| `Upsilon_B_src` | compressed manuscript obstruction/residual | exact Euler covector of the selected G2 action |
| `E_T_var` | slot-complete Euler covector of the repository's selected G2 action | Weinstein's displayed residual |
| `(D E)^!` | formal adjoint of a residual derivative for declared pairings and Green form | the draft glyph `D_omega^*`, a Noether differential, or unreleased `D^2` |
| `I2_src` | source-anchored typed realization of the manuscript bosonic norm | a source-displayed total action |
| `I2_var` | repository diagnostic square of the actual G2 Euler covector | a manuscript formula |
| `Theta_G3` | preboundary potential of the first G2 action | either residual-square preboundary potential |
| `Theta_2_src`, `Theta_2_var` | separate residual-square preboundary potentials | a selected BFV phase space or domain |
| active `(9,5)` port | repo trace-reversed right-`H` / `Sp(32,32;H)` carrier | draft `Y^(7,7)` plus complex `C^(64,64)` / `u(64,64)`-type carrier; no global metric, Clifford, group, residual, or domain intertwiner is built |

The three uses of “square” remain distinct: the 2021 scalar bosonic residual
norm, the spoken inter-layer square/root analogy, and the unreleased modern
two-connection `D^2` complex.

## The two complete derivatives

Write

\[
B=B_{\rm rot}(\epsilon,g),
\qquad
\dot B=DB[\dot\epsilon,\dot g],
\qquad
\dot T=\dot A-\dot B.
\]

The compressed branch differentiates to

\[
\begin{aligned}
DE_{\rm src}[\dot\phi]
={}&(D\mathscr S)[\dot\epsilon,\dot g]F_A
+\mathscr S(D_A\dot A)\\
&+\kappa_1(D\flat)[\dot\epsilon,\dot g]T
+\kappa_1\flat(\dot A-\dot B).
\end{aligned}
\]

The exact action branch differentiates to

\[
\begin{aligned}
DE_{\rm var}[\dot\phi]
={}&(D\mathscr S)F_B+\mathscr S(D_B\dot B)\\
&+\frac12(DL+DL^!)T
+\frac12(L+L^!)(\dot A-\dot B)\\
&+(DM)(T,T)+2M(T,\dot A-\dot B)\\
&+\kappa_1(D\flat)T
+\kappa_1\flat(\dot A-\dot B).
\end{aligned}
\]

`DM` here is the derivative of the full six-slot polarization that defines
`M`. It is not replaced by `(D S)q`, and it is not frozen. Likewise,

\[
D(L^!)\ne(DL)^!
\]

in general: the input/output lowerers, density, Krein dual, and Green form
also move.

For either branch `r`, with

\[
u_r=R_{\rm res}E_r,
\]

the squared-residual variation is

\[
\boxed{
\delta I_{2,r}
=\langle DE_r[\delta\phi],u_r\rangle
+\frac12\langle E_r,(DR_{\rm res})E_r\rangle
=\langle DE_r[\delta\phi],u_r\rangle
-\frac12\langle u_r,(Db_{\rm res})u_r\rangle.
}
\]

The probe separately returns nonzero representatives of the `A`, reference
graph, Shiab, Hodge/pseudo-musical, density, and `DR` contributions for both
branches. Freezing any of those terms fails on the exact witness.

## Principal-symbol theorem

At fixed independent `(B,T)` the two `T` symbols are

\[
\sigma_T(E_{\rm src})=\sigma(L),
\qquad
\sigma_T(E_{\rm var})
=\frac12\bigl(\sigma(L)+\sigma(L^!)\bigr).
\]

After returning through the fixed-`A` graph direction
`\dot T=-\dot B`, the compressed curvature symbols cancel:

\[
\sigma_{\rm graph}(E_{\rm src})=0.
\]

The exact branch retains

\[
\boxed{
\sigma_{\rm graph}(E_{\rm var})
=\frac12\bigl(\sigma(L)-\sigma(L^!)\bigr)\circ\sigma(DB).
}
\]

The exact B2C9 rational fixture establishes nonzero survival without a
tolerance: `60/144` independent symbol-matrix entries differ, and one
pre-registered graph witness is exactly `0` versus `1/2`. A separate skew/
cyclic control kills the graph residue, proving that the test recognizes the
identity under which the two formulas could collapse.

This is an exact finite noncentral architecture result. It is not yet the
full local-coordinate symbol of the active native `Y^14` Shiab.

## Separate squared actions and preboundary forms

The two scalar constructions are retained separately:

\[
I_{2,{\rm src}}
=\frac12\langle E_{\rm src},R_{\rm res}E_{\rm src}\rangle,
\qquad
I_{2,{\rm var}}
=\frac12\langle E_{\rm var},R_{\rm res}E_{\rm var}\rangle.
\]

The first is the source-anchored norm realization. The second is a repository
diagnostic of the actual selected G2 Euler covector. They are not summed, and
neither is silently substituted for the other.

The exact polynomial model uses a first-jet graph

\[
B=G_0z+G_1z',
\qquad T=A-B,
\]

and derives `E_var` by applying the Euler operator to the written
transgression-shaped first action, not by declaring a correction. It then
types its density-dual residual with

\[
R_{\rm jet}=\rho^{-1}\bar R_{\rm jet},
\qquad b_{\rm jet}=R_{\rm jet}^{-1},
\]

varies each square directly, and integrates every derivative by parts. Thus
the residual density and inverse-density primalizer occur exactly once. The
base density is spatially constant on the deterministic polynomial witness,
but its nonconstant variation is live and returned.

The exact identities are:

```text
source square:
  direct   =  50615253739 / 6486480
  bulk     = -13533330761 / 6486480
  boundary = 118675 / 12

variational square:
  direct   = 56420043749 / 4324320
  bulk     = -2373861421 / 4324320
  boundary = 652613 / 48
```

For the compressed branch the jet orders are

```text
A0: 1, A1: 1, graph z: 1, moving coefficient g: 0.
```

Its preboundary packet is ordinary field plus conormal data:

\[
(A,z;\pi_A,\pi_z).
\]

For the exact rational comparator branch they are

```text
A0: 1, A1: 1, graph z: 2, moving coefficient g: 1.
```

Its graph sector therefore has the prolonged packet

\[
(z,z';\pi_{z,0},\pi_{z,1}),
\]

along with the `A` and moving-coefficient pairs. The extra `z'` conormal
flux is exactly

```text
33707 / 4 != 0.
```

The two action-derived preboundary two-forms are nonzero, antisymmetric, and
unequal on independent variations:

```text
omega_source        =   325618 / 9
omega_variational   = 10674083 / 432
```

Their nonvanishing and antisymmetry do not select or prove a maximal
Green-isotropic boundary domain.

The three available preboundary packets must remain separate:

\[
\Theta_{G3},
\qquad
\Theta_{2,{\rm src}},
\qquad
\Theta_{2,{\rm var}}.
\]

They can be added only after a composite action architecture is selected.

## Active trace-reversed port

B2C13 also reuses the actual B2C12 coefficient port without identifying it
with the rational jet comparator:

\[
G_Y=g\oplus G_{\rm DW},
\qquad
(3,1)+(6,4)=(9,5),
\]

\[
b_{\rm res}=\rho G_Y^{-1}\otimes\kappa,
\qquad
R_{\rm res}=\rho^{-1}G_Y\otimes\kappa^{-1}.
\]

The 28-dimensional slice remains nondegenerate and balanced `(14,14)`, and
two independently labeled test covectors satisfy

\[
DR_{\rm res}=-R_{\rm res}(Db_{\rm res})R_{\rm res}
\]

with the correct minus-sign return. These covectors are not constructed images
of `E_src` and `E_var`; they test the common coefficient-level port. This does
not construct a global carrier identification between the finite jet model
and the native bundle operator.

## Source collision

### `SOURCE-CONFIRMS`

- The 2021 draft writes `I_2^B=||Upsilon_omega^B||^2`, its displayed partial
  `varpi` derivative, and at equation 9.15 the compact unsuperscripted equation
  `D_omega^* Upsilon_omega=0`.
- Draft equations 9.18--9.20 separately keep the first-order-total equation
  and the sourced alternative
  `D_omega^* Upsilon_omega^B=Upsilon_omega^F`. The bosonic superscript in
  9.20 is not retroactively inserted into 9.15.
- TOE `00:41:50--00:43:38` and UCSD/Into the Impossible
  `00:05:43--00:06:32` distinguish the Einstein--Dirac first layer from a
  second Yang--Mills--Higgs/action layer.
- TOE `02:44:06--02:45:13` says the modern two-connection on-shell `D^2`
  construction has not been released.
- The rechecked source set describes restriction/pullback along a metric
  section rather than supplying a defect action: TOE local
  `01:18:26--01:19:15` distinguishes local from disputed global sections;
  TOE `01:29:19--01:29:47` describes a Weyl-spinor pullback; Portal/Oxford
  `02:04:18--02:05:04` and `02:11:07--02:12:34` put the action/equations
  upstairs and then pull them back; Into the Impossible
  `00:32:07--00:33:36` independently describes pullback along the metric
  section. Exact negative searches found no defect-action construction in
  these rechecked transcripts; this is not a corpus-wide absence theorem.

### `SOURCE-CORRECTS`

- `Upsilon_B_src` is not the exact Euler covector of the selected
  reconstructed G2 action.
- Source `D_omega^*` is compact formal notation, not the active Frechet/
  Green adjoint, a Noether differential, or the unreleased modern `D^2`.
- `R_res`, the density-dual norm typing, the active `(9,5)` port, and every
  preboundary form in this gate are repository constructions.
- Pullback of an ambient equation, the dual map on Euler covectors, and
  variation of a pulled-back action remain different maps.

### `SOURCE-SILENT`

The checked sources do not supply:

- the exact signature, density, adjoint pairing, boundary conditions, or
  domain behind `||Upsilon_B||^2`;
- the active local `Y^14` symbol of `D Upsilon`, `D(L^!)`, `DM`, or the full
  moving Shiab/Hodge/density/graph derivative;
- the complete epsilon, metric, and section owner variation;
- the exact inter-layer architecture: sum, sequence, rival equations, or a
  common stationary point;
- a mapping from the unreleased 2025 connection tokens to the 2021
  `A_tr/B_rot` roles;
- a global metric, Clifford, group, residual, or domain intertwiner from the
  draft `Y^(7,7)` plus complex `C^(64,64)`/`u(64,64)`-type carrier to the
  repo active trace-reversed `(9,5)`, right-`H`/`Sp(32,32;H)` port;
- an equation-dual observation map, variation--pullback commutation theorem,
  or source-supplied defect action; or
- a trace theorem, characteristic kernel, boundary polarization, common
  boson--fermion domain, or factorization among the three square objects.

## Seven-axis boundary

- **Layer 0:** the residual, adjoint, square, pullback, and preboundary
  homonyms are separated above.
- **L1/L2:** the finite first-jet bundles and actual active `(9,5)`
  coefficient port are typed. Their global bundle intertwiner is open.
- **L3:** both exact finite residual derivatives, graph symbols, moving
  returns, Euler integrations, conormal packets, and preboundary two-forms
  close. The full native `Y^14` first jet is open.
- **L4:** `I2_src` and `I2_var` remain rival staged diagnostics; no composite
  action is selected by this gate.
- **L5:** the active coefficient port preserves right-`H`, Krein, `C+`, and
  trace-reversed structure. No positive energy, Hilbert space, or unitarity
  follows.
- **L6:** no Standard Model field equation, mass, Higgs/Yukawa coefficient,
  anomaly, count, dark-energy amplitude, dark-matter prediction, or PP3 is
  claimed.
- **L7:** the source boundary and repository additions are explicit above.

P1, P2, and P3 are unchanged and unused. They supply no residual, derivative,
symbol, pairing, conormal momentum, boundary condition, quotient, or action.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`.
`TG-1 AND TG-2 AND TG-3` remains false; no third lane is promoted.

## Validation and next gate

The executable probe passes:

```text
43 exact + 4 source receipts + 15 type-level + 21 planted = 83 PASS
```

The post-construction hostile council also passes without a remaining
blocker.  The affine/cohomology review independently checked the density
typing, symbol split, graph witnesses, and zero/nonzero next-gate fork.  The
Krein/PDE review checked the corrected primalizer density, preboundary
packet, and scope of the finite comparator.  The paired source/axiom review
checked the distinct draft equations, adjoint and square homonyms, source
silences, carrier non-identification, and the explicit openness of the active
`Y^14` symbol.  These are separate specialist verdicts, not an aggregated
vote.

The next construction gate is

```text
ECW3D-B2C14-ACTIVE-Y14-SHIAB-FIRST-JET-AND-GRAPH-CONORMAL-PORT
```

It must port the actual trace-adapted native Shiab, its moving formal adjoint,
the six-slot `DM`, and the full `B_rot` Levi--Civita/reduction graph into a
local active `Y^14` first-jet symbol. It must first compute
`K_act=1/2(sigma(L)-sigma(L^!)) sigma(DB_rot)`. If `K_act` is nonzero, it must
construct the real prolonged boundary trace and characteristic kernel. If it
vanishes, it must record active order collapse and use the reduced trace
packet. Only after that fork closes should B2C6B resume the mixed
boson--fermion common-domain search.
