---
artifact_type: construction_result
created: 2026-08-08
status: ARBITRARY_X_LORENTZ_SECTION_FALSE__LOCAL_HOLONOMIC_JETS_EXIST__ORDINARY_PULLBACK_NOT_FAITHFUL_ON_SELECTED_ACTION_IMAGE__COMPLETE_RECEIVER_OR_SOURCE_DERIVED_BV_CONSTRAINT_REQUIRED
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CORRECTS__NO_ARBITRARY_X_GLOBAL_OBSERVATION_SECTION__SOURCE-CONFIRMS__LOCAL_SECTION_AND_PULLBACK_GRAMMAR__SOURCE-SILENT__PHYSICAL_FAITHFULNESS_AND_BV_QUOTIENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_physical_section_faithfulness_probe.py
  - tests/channel-swings/selected_k77_physical_section_faithfulness_independent.sage
registry: lab/process/selected-k77-physical-section-faithfulness-gate.json
---

# Selected K77 physical observation-section and faithfulness gate

## Result first

The v0.78 successor was partly impossible as written.

A local observation section can have an exact holonomic first and second jet.
But a spin four-manifold does not automatically admit a global Lorentz metric:
`S^4` is spin and has Euler characteristic two, so it cannot carry the required
timelike line/vector field.  The primary source agrees on scope: metric-bundle
global behavior depends on topology, and Weinstein rejects Curt's claim that
the needed global section is already present.

Even when a Lorentz section is admitted, holonomicity does not make ordinary
pullback faithful.  For every graph section with

\[
  ds=\begin{bmatrix}I_4\\J\end{bmatrix},
  \qquad s^*=\begin{bmatrix}I_4&J^T\end{bmatrix},
\]

ordinary covector restriction has rank four and the exact ten-dimensional
kernel

\[
  N_s^*Y=\operatorname{im}
  \begin{bmatrix}-J^T\\I_{10}\end{bmatrix}.
\]

That rank fact alone would not prove physical leakage.  The decisive
composition is with the already-owned source-action witness: the nonzero
`kappa_1 <T,*T>/2` augmented-torsion term emits a nonzero Euler covector in
this conormal kernel on the displayed local translation domain.  The same
action covector participates in the v0.78 overlap theorem.  Therefore a real,
descended action equation is invisible to ordinary pullback.

The correct next construction is a fork:

1. retain the exact complete `4+10` equation receiver and determine what the
   ten vertical equations are physically; or
2. derive from the source action a constraint/BV differential whose physical
   image removes the conormal Euler sector.

No sixth quotient is booked.  Neither route has yet been constructed globally.

## 1. Layer 0: three burdens, not one

| phrase | exact object | disposition |
| --- | --- | --- |
| section jet | local value, first derivative and symmetric second derivative of a metric section | locally constructible |
| global observation section | a global Lorentz metric/reduction on the chosen `X` | topology-dependent; not arbitrary-`X` |
| ordinary pullback | rank-four map `s*:T*Y -> T*X` | never faithful on all fourteen covector directions |
| complete receiver | pullback plus vertical coefficient restriction, with inverse-transpose Euler dual | exact rank fourteen at fixed section jet |
| physical no leakage | selected action Euler image has zero conormal component, or that component is removed by a derived quotient | false automatically on the displayed full local translation domain; constrained rival open |
| BV quotient | cohomological reduction owned by an explicit differential/moment map | not constructed |

The result does not say GU cannot use observation sections.  It says a section
cannot, merely by being genuine, solve a rank and action-image problem.

## 2. Global existence is a sector condition

Take `X=S^4`.  Its standard cell structure gives

\[
  \chi(S^4)=1+1=2,
  \qquad H^1(S^4;\mathbb Z/2)=H^2(S^4;\mathbb Z/2)=0.
\]

Thus `S^4` is spin.  Any real line bundle on it is trivial.  If `S^4` carried
a Lorentz metric, its timelike line distribution would therefore give a
nowhere-zero vector field, contradicting Poincare--Hopf because `chi` is
nonzero.  Hence

\[
  \text{spin four-manifold}\not\Longrightarrow
  \text{global Lorentz observation section}.
\]

If “one temporal dimension” means an already supplied Lorentz reduction, the
construction begins in the admissible sector.  If it is only a signature
request, it does not manufacture the section.  No P1/P2/P3 datum is consumed
by stating this admissibility condition.

## 3. Local holonomicity passes

The exact control constructs ten polynomial metric components

\[
  g_A(x)=g_A(0)+J_{A\mu}x^\mu
  +\frac12 H_{A\mu\nu}x^\mu x^\nu,
  \qquad H_{A\mu\nu}=H_{A\nu\mu}.
\]

Their derivatives reproduce the chosen rational `J`, the graph derivative has
rank four, and the second jet has the required mixed-derivative symmetry.  An
antisymmetric second-jet plant fails.  This establishes local realizability;
it does not glue a global Lorentz section.

## 4. Holonomicity cannot repair ordinary pullback

For every graph `J`,

\[
  \operatorname{rank}s^*=4,
  \qquad \dim\ker s^*=10,
  \qquad
  s^*\begin{bmatrix}-J^T\\I\end{bmatrix}=0.
\]

The complete field map and equation dual remain the prior exact objects

\[
  M=\begin{bmatrix}I_4&J^T\\0&I_{10}\end{bmatrix},
  \qquad e_{4+10}=M^{-T}e_Y,
  \qquad \det M=1.
\]

They detect the action witness that ordinary pullback erases.  This proves why
the complete receiver is mathematically sufficient at fixed section jet, but
does not identify its ten vertical equations with Higgs fields, constraints,
gauge, or propagating particles.

## 5. The action-image collision is the decisive step

The preceding augmented-torsion receiver gate constructed

\[
  T=N_sb,\qquad b\ne0,
\]

on a constant one-generator local stratum.  There `dT=0`, `[T,T]=0`, and the
curvature contribution may vanish, while the explicit action term gives

\[
  e_T=\kappa_1T\ne0,
  \qquad s^*e_T=0.
\]

Therefore the full local translation-domain action is not automatically
horizontal for nonzero `kappa_1`.  Setting `kappa_1=0` removes this witness but
does not prove faithfulness.  A separately derived constrained domain may
still exclude it; that is route 2, not a rebuttal of the computation.

## 6. Seven-axis disposition

- **Layer 0:** local jet, global section, ordinary pullback, complete receiver,
  conormal action image and BV quotient are separated.
- **L1 source:** source corrects arbitrary-`X` global attribution, confirms
  local section/pullback grammar and is silent on faithful Euler reception.
- **L2 algebra:** two exact routes reproduce the `4+10` rank split and live
  conormal action witness.
- **L3 geometry:** local holonomic jets exist on an admitted Lorentz section;
  `S^4` supplies a spin/no-Lorentz counterexample to arbitrary `X`.
- **L4 variation:** the complete inverse-transpose receiver preserves the
  full first-variation pairing and detects the hidden action equation.
- **L5 gauge/BV:** no conormal direction is called gauge without a differential
  and moment-map owner.
- **L6 analytic:** global BFV, Green/Krein domain, constraint propagation and
  hyperbolicity remain open.
- **L7 physical:** no spectrum, equation, particle, cosmology or theory verdict
  is promoted.

## 7. Exact controls and progress

The composed SymPy route passes `55/55`, including all three predecessor
replays.  The independent Sage/QQ route passes `16/16`.  Plants reject an
antisymmetric second jet, arbitrary-`X` existence, ordinary pullback as a
complete receiver, and descended-projector-as-satisfied-no-leakage.

```text
new fitted coefficient/selector: 0
new external datum:              0
new scoped quotient:             0
P1/P2/P3 consumed:               0

Ledger v0.79 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: NONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed are arbitrary-`X` existence, local first/second-jet realizability, and
ordinary-pullback faithfulness on the displayed full action domain.  Opened is
the sharply typed receiver-versus-BV-constraint fork.  The two remaining
conditions are (a) adjudicate and construct one fork horn, then (b) globalize
it through `tau_A0`/BFV and a common domain.

No verdict, residue, quotient count, datum, canon or public posture moves.

## Next gate

`COMPLETE_4_PLUS_10_EQUATION_SYSTEM_VERSUS_SOURCE_DERIVED_CONORMAL_CONSTRAINT_BV_QUOTIENT`.

First classify the ten vertical equations already emitted by the complete
receiver and simultaneously test whether the tilted Ward/BV complex supplies
a differential whose image is exactly the conormal action sector.  Whichever
horn survives must then descend through global `tau_A0`, moment-map/charge
algebra and a common Green/Krein domain.  Preferred-Shiab, coupled fermions and
the separate `I2B <-> ||II||^2` map remain separate.
