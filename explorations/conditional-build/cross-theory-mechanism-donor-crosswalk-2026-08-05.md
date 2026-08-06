---
title: "Cross-theory mechanism-donor crosswalk: typed ports from NCG, string/higher gauge, LQG and asymptotic safety"
status: active_research
doc_type: exploration
created: 2026-08-05
functional_channel: COMPOSE
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
machine_receipt: lab/process/cross-theory-mechanism-donor-crosswalk.json
probe: tests/channel-swings/cross_theory_mechanism_donor_crosswalk_probe.py
---

# Cross-theory mechanism-donor crosswalk

## Outcome

This pass does **not** create a fifth theory lane and does not propose making GU
part string theory, loop quantum gravity, noncommutative geometry or asymptotic
safety. It asks a narrower engineering question:

> Does a mature mechanism from another program shorten a named distance in the
> current GU construction without replacing the GU carrier or silently adding
> external data?

Two **method ports** pass that test:

1. **Connes finite-control port.** Use the finite spectral Standard Model as a
   fail-closed recovery checklist for the GU-native zero-order fermion, Higgs,
   Yukawa, gauge and anomaly placement. Do not import its finite algebra or
   Dirac operator.
2. **Higher-gauge/L-infinity integration port.** Use Chevalley--Eilenberg and
   Lie-infinity integration machinery to test whether the source-required local
   super-IG bracket actually descends to a global higher group. Do not import a
   string compactification, flux vacuum or String-group level.

No exact object port was found. The LQG cylindrical measure is currently the
wrong carrier for the missing normalized observer functional; asymptotic-safety
FRG is already present and is downstream of a stable action/domain; string
compactification and flux data would add precisely the external ontology the
conditional build is trying to reconstruct.

The standing ledger does not migrate. This is an ordering and typing result:

```text
Ledger v0.17 — 82/82 active rows mapped
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
ledger_row_changes: none
```

## 1. Port contract

Every candidate is judged on six fields before selection:

1. the donor mechanism;
2. the exact GU recipient;
3. a typed translation map;
4. its datum cost;
5. the named constraint or construction distance it changes; and
6. a kill condition.

The allowed dispositions are `EXACT_PORT`, `METHOD_PORT`, `ANALOGY_ONLY`,
`WRONG_TYPE` and `ALREADY_PRESENT`. A familiar word such as *connection*,
*spectral action*, *quantum geometry* or *fixed point* supplies no translation
map by itself.

## 2. Candidate matrix

| id | donor mechanism | GU recipient | disposition | datum cost | effect and distance | kill / revival |
| --- | --- | --- | --- | --- | --- | --- |
| NCG-CONTROL | real even spectral-triple controls: algebra/representation, grading, real structure, order zero/one, inner fluctuation, unimodularity, fermion representation, anomaly and action recovery | the unbuilt `P0/rho(Phi)/Y_K/Y_C/C`-reality placement and the SM rows `LT-SM1/2/4/5/6/8` | **METHOD_PORT — SELECTED** | zero; the finite algebra and `D_F` are prohibited inputs | replaces the vague demand “recover the SM sector” with binary typed gates; identifies exactly where GU derives, imports or merely hosts each component | kill the port if passing a gate requires importing `A_F=C+H+M3(C)`, KO-6 or the finite `D_F`; revive an object port only if GU itself selects an equivalent subobject |
| NCG-OBJECT | `A_F`, KO-6 real structure and finite `D_F` as the internal geometry | the GU chimeric spin carrier | **WRONG_TYPE** | a new block-sum algebra, real structure and finite Dirac | would replace, rather than complete, the simple quaternionic GU carrier | already killed at current grade by the unforced conjugacy family, KO-sign mismatch and imported order-one Dirac |
| STRING-LINF | CE cocycle / Lie-infinity algebra / higher-group integration used in String-group constructions | the source-required odd bracket into connection one-forms and its global super-IG descent | **METHOD_PORT — SELECTED** | zero only if the bracket and period class are fixed by the existing GU/source data | turns “global descent” into a sequence: local bracket, higher Jacobi, CE cocycle, period/integrality, real/Krein compatibility, integrated action on the connection space | kill if the local bracket fails higher Jacobi, the periods are non-integral, or a free level must be selected; revive after a source-owned bracket is constructed |
| STRING-COMPACT | compactification, branes, fluxes, Calabi--Yau moduli and vacuum selection | generations, gauge breaking or the external datum | **WRONG_TYPE** | many new discrete and continuous choices | increases rather than reduces the unexplained residue | revive only with a proved functor from the GU metric bundle that forces the compactification data |
| STRING-ANOMALY | anomaly cancellation, index and inflow constraints | the source-action consistency rows and chiral/count bridge | **ALREADY_PRESENT** | zero as a control | valuable, but already represented by the anomaly ledgers, 2-/3-primary firewall and boundary/index program | reopen only when a new source action changes the anomaly polynomial or boundary structure |
| LQG-MEASURE | projective/cylindrical completion of generalized connections and the Ashtekar--Lewandowski measure | the missing normalized covariant observer/domain functional | **WRONG_TYPE** at the current gate | would require a graph/projective system, compatible group, measure and continuum interpretation | a probability measure on generalized connection space is not yet a normalized Lorentzian observer functional screening the constant mode | revive after an explicit functor from GU connections/observation domains to a projective compact-Hausdorff system preserves covariance and the constant-mode question |
| LQG-CONSTRAINT | holonomy/flux and constraint-first quantization | the connection and BV constraint sectors | **ANALOGY_ONLY** now | unknown | suggests a method but changes no current distance before a GU holonomy algebra and continuum map exist | revive after the classical reduced connection phase space and its holonomy observables are built |
| AS-FRG | effective-average-action flow, regulator families, fixed-point and critical-surface stability | the selected action's UV/loop rows | **ALREADY_PRESENT**, delayed | no new datum as a test; truncation choices remain methodological | the repo already has Reuter/FRG, matter-budget and multi-regulator work; running it before the action and domain stabilize would test a moving target | admit only after the selected numerator, common domain and action coefficients are stable; kill a claimed UV result when it is not robust across declared parametrization/regulator families |

## 3. Why the selected ports are useful but modest

### 3.1 Connes supplies a receiver test, not GU's missing receiver

The existing GU-as-NCG swing already establishes the decisive Layer-0 split.
The GU carrier is simple and quaternionic; the Connes finite Standard Model is
a block-sum, KO-6 almost-commutative geometry. An embedded copy of the finite
algebra is not selected by the GU structure, and a generic GU Dirac operator
does not become the adapted finite order-one operator merely because both are
called Dirac operators.

What transfers cleanly is the **checklist discipline**. The source-action build
has repeatedly reached a familiar SM noun before constructing the complete
zero-order placement that makes it that object. Applying the finite controls
forces the build to exhibit, separately:

- algebra and left/right representations;
- grading and real/Krein structure;
- order-zero and the relevant order-one replacement;
- the gauge orbit actually generated by connection fluctuations;
- the Higgs representation and its scalar potential;
- the fermion mass/Yukawa map and charge-conjugation placement;
- unimodularity/hypercharge normalization; and
- anomaly cancellation and action recovery.

This shortens the mapping distance without claiming that GU uses the Connes
mechanism.

### 3.2 String-derived higher gauge supplies a global-descent algorithm

Weinstein's current source locus asks for an algebraic odd bracket whose square
lands in connection one-forms, with equivariance, Jacobi, real form and global
descent. It does not require an odd action. Lie-infinity integration is therefore
the closest mature machinery to the stated burden: encode the bracket and any
higher Jacobiator as a CE cocycle, test its periods/integrality, and integrate
the finite-type algebra to a higher group or prove why this cannot be done.

The port is deliberately **conditional and zero-datum**. String-group examples
show that an integral level can be load-bearing. If the GU bracket leaves such
a level free, that level is a newly exposed datum, not a derivation, and the
port stops rather than selecting it.

## 4. Why the other attractive analogies are deferred

### LQG and the observer functional

Ashtekar--Lewandowski projective integration is a genuine construction on an
infinite-dimensional space of generalized connections. The current GU object,
however, is a normalized covariant functional on the physical observation
domain that makes sense of a global constant-mode projector in a Lorentzian/
Krein setting. A cylindrical probability measure on graph holonomies and that
functional do not share a carrier, covariance group or stated observable.
Calling both a measure would repeat the Layer-0 error this program is designed
to prevent.

### Asymptotic safety and the unfinished action

FRG is an excellent *later* adversary: it can ask whether a putative fixed point
and finite critical surface survive larger truncations, field parametrizations
and regulator choices. The repo has already used exactly this machinery and
found both positive evidence and scheme dependence. Until the selected action,
numerator and common domain stop moving, another FRG pass would be precision on
the wrong theory.

### String compactification and flux selection

Compactification can certainly fit gauge groups, matter and chiral indices.
But it does so by supplying manifolds, bundles, flux integers, branes and vacuum
choices not generated by the current GU construction. Those are useful foils
for constraint-surplus accounting, not donors for a program whose central task
is to locate the minimal external datum.

## 5. Lightweight specialist and science-council read

Ten inline lenses converge on the same ordering:

1. **NCG engineer:** port the acceptance tests; refuse the finite algebra.
2. **Higher-gauge geometer:** turn super-IG descent into CE/Jacobi/period/global
   integration gates.
3. **LQG quantization specialist:** do not confuse cylindrical connection-space
   integration with the observer functional.
4. **FRG practitioner:** wait for a stable action; then require scheme families.
5. **Symplectic/BV geometer:** neither selected port proves a physical
   transition until the object descends through the reduced covariant phase
   space.
6. **Representation theorist:** require an equivariant recipient map before
   reading familiar SM representations from a carrier.
7. **Hyperbolic-PDE specialist:** domain and propagation remain native analytic
   burdens; no donor measure repairs signature `(7,7)` by analogy.
8. **QFT engineer:** build the selected on-shell numerator before spending on
   UV flows.
9. **Statistics/ML engineer:** use learned or sparse surrogates only after exact
   labels/evaluators exist; they cannot select a mathematical port.
10. **Systems engineer:** the two-port cap and revival triggers prevent a broad
    comparison exercise from becoming another permanent lane.

The science-council disposition is therefore:

- keep the current numerator, observer-functional and super-IG construction
  threads;
- attach the NCG checklist to SM recovery as a control;
- attach L-infinity integration to super-IG global descent as a method;
- leave LQG as a typed revival candidate;
- schedule AS only after the action/domain admission gate; and
- run Compose again after three material Build outputs.

## 6. Stop rule and claims not made

The donor harvest stops here. A further theory is not searched merely because
it uses connections or geometry. Reopen the crosswalk only when:

- a current Build distance has no native construction route;
- a donor mechanism names the same typed input and output;
- its translation adds no unexplained datum, or explicitly prices one; and
- its kill condition can be executed.

This result does not derive the Standard Model, quantize GU, prove asymptotic
safety, construct a physical measure, close super-IG, change the external datum,
or move any ledger verdict.
