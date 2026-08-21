---
title: "B5 domain-compatible BRST cohomology: a marked class survives the reduced hit quotient"
status: active_research
doc_type: exact_closed_hilbert_complex_cohomology
created: "2026-08-21"
registry: lab/process/b5-domain-compatible-brst-cohomology.json
probes:
  - tests/channel-swings/b5_domain_compatible_brst_cohomology_probe.py
grade: "ON THE REPOSITORY-CONSTRUCTED FLAT B5 HALF-CYLINDER, THE STRICT FOUR-STAGE RARITA--SCHWINGER COMPLEX ADMITS CLOSED COFLIP-COMPATIBLE STAGE REALIZATIONS SUBORDINATE TO THE HIT AND MISS WITT TRACE LINES. THE EXACT DECAYING K=E4 MODE DEFINES A NONZERO MARKED MIDDLE-STAGE CLASS IN BOTH THE ALGEBRAIC AND REDUCED HIT QUOTIENTS: A BOUNDED FOURIER-TRANSVERSE PROJECTION ANNIHILATES THE COMPLETE GAUGE RANGE BUT NOT THE MODE. THE SAME SECTION IS EXCLUDED FROM THE MISS MIDDLE DOMAIN. THIS PROVES EXTENSION-SENSITIVITY OF THE MARKED LINEAR GAUGE/BRST CLASS, NOT TOTAL COHOMOLOGY, POSITIVITY, A PHYSICAL STATE SPACE OR A SOURCE-SELECTED DOMAIN."
target_verdict: B5_MARKED_MIDDLE_STAGE_BRST_CLASS_IS_EXTENSION_SENSITIVE
target_claim: internal target B5-DOMAIN-COMPATIBLE-BRST-COHOMOLOGY-DISCRIMINATOR; verdict closed stage domains constructed and marked class survives algebraic and reduced hit quotients but is absent from miss
canon_verdict_change: none
---

# B5 domain-compatible BRST cohomology

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the repository-owned strict linear Rarita--Schwinger
gauge/BV complex on the named flat complexified `(9,5)` half-cylinder. It is
not the separate graph-mixing Stage-B Euler family, Weinstein's unreleased
source action, quantum BRST cohomology, a positive physical Hilbert space, or
the global geometry of `Y=Met(X)`.

```gu-typed-objects
result: the exact decaying e4 Fourier mode defines a marked nonzero middle-stage class in the algebraic and reduced hit quotients and is absent from the miss middle domain
carrier: L2 stages U0=S rank128, U1=V* tensor S rank1792, U2=density dual rank1792, U3=S density dual rank128 over [0,infinity) times T13 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: auxiliary positive L2 graph topology plus the program-native middle and folded Krein Green forms at n=dr ON=independent-B5-curved-strict-carrier
real_structure: relative Gamma-natural antilinear coflip covering the integral torus sign involution and fixing the selected Fourier mode and both real Witt lines
grading: linear abelian gauge/BV stage grading; cohomology target is ker K divided by im A at U1
action_owner: repository-construction strict massless quadratic Rarita--Schwinger action; hit and miss stage extensions remain mathematically available and action/source-unselected
target: comparison of the marked class in algebraic and reduced U1 cohomology for two closed stage realizations subordinate to the hit and miss trace lines MAP-TYPE=quotient
```

## Result first

The strict native complex is

```text
U0=S --A--> U1=V* tensor S --K--> U2=(V* tensor S)^vee_dens
     --A^vee--> U3=S^vee_dens.
```

On the named flat half-cylinder, let `A_max`, `K_max` and `A^vee_max`
denote the maximal distributional `L2` realizations and let `K_min` be the
closed minimal graph realization of the middle operator. Constant-coefficient
Noether identities hold distributionally:

```text
K A=0,                  A^vee K=0.
```

The prior exact massless mode has

```text
u(r,y)=exp(-r) exp(i y4) v,
v_1=gamma_2 c(xi)s,
v_2=gamma_1 c(xi)s,
xi=-e0+i e4,
```

with all other vector components zero. It obeys `K u=0`, `A^vee u=0`, is
coflip-real and square-integrable.

This result constructs closed stage domains and proves that the marked class
`[u]` is nonzero in both

```text
H_hit^1       = ker(K_hit)/im(A_hit),
H_hit,red^1   = ker(K_hit)/closure(im(A_hit)).
```

The miss middle domain excludes `u`. Thus the marked class is extension-
sensitive at closed linear gauge/BRST-complex grade.

## The middle Green quotient and field-stage Witt lines

For the positive non-null normal `n=dr`, the exact noncharacteristic symbol
sequence has ranks

```text
rank A_n=128,     rank K_n=1664,     rank A_n^vee=128.
```

Therefore the middle Green coefficient on `U1` has radical
`im A_n` of dimension `128`. The complete folded coefficient on
`U0 plus U1` has inertia `(960,960,0)`. The `U0`/radical cross block is a
nondegenerate hyperbolic block of inertia `(128,128)`, so the nondegenerate
middle quotient has inertia `(832,832)`.

The field-stage form therefore has inertia `(832,832,128)` and field-stage
maximal isotropics have dimension `832+128=960`, exactly half the folded
rank. The previous hit/miss Witt construction can consequently be chosen
inside `U1`; no ghost/field mixing is required merely to contain the witness.

The witness is null but not radical. Exact Clifford evaluation gives
`K_n v != 0`. Choose a coflip-real null Witt partner `w` with
`h_K(v,w)=1`, a common coflip-real isotropic complement `E`, and the radical
`R=im A_n`. Then

```text
W_hit  = R plus C v plus E,
W_miss = R plus C w plus E
```

are field-stage maximal isotropics. Viewed in the folded trace carrier, they
are the refined `L_hit` and `L_miss`: the first contains the massless trace,
the second replaces its Witt line.

## Closed stage domains

The full folded domains do not automatically define a Hilbert complex: a
folded kernel is not a substitute for stage-domain preservation. The stage
construction is therefore explicit.

Let `z_w` be any smooth square-integrable coflip-real lift of the `w` trace
line in the selected Fourier block. Green pairing with the opposite Witt line
vanishes on `Dom(K_min)` but is nonzero on `u` or `z_w`; hence neither lift is
in the minimal domain. Define

```text
Dom(K_hit)  = Dom(K_min) direct-sum C u,
Dom(K_miss) = Dom(K_min) direct-sum C z_w.
```

The graph of `K_min` is closed. Adding one finite-dimensional graph line gives
a closed graph, so both middle realizations are densely defined and closed.
They are subordinate to the respective folded trace realizations: their only
nonminimal trace line lies in `W_hit` or `W_miss`. The compact-interior core
is common, and the Gamma-natural coflip preserves the minimal graph and both
real extension lines.

Now pull each middle domain back through the maximal gauge operator:

```text
Dom(A_L)={phi in Dom(A_max): A phi in Dom(K_L)},   L=hit,miss.
```

Because `A_max` is closed and `K A=0`, the map

```text
A:Dom(A_max)_graph -> Dom(K_max)_graph
```

is continuous. The preimage of the graph-closed `Dom(K_L)` is closed, so
`A_hit` and `A_miss` are closed. They remain dense because compactly supported
smooth gauge parameters map into `Dom(K_min)`. By construction,
`K_L A_L=0`.

Use `A^vee_max` at the terminal stage. It is closed, and
`A^vee K_L=0` distributionally implies `K_L Dom(K_L)` lies in
`Dom(A^vee_max)`. Thus both triples `A_L, K_L, A^vee_max` are closed
coflip-compatible Hilbert complexes.

## Algebraic and reduced non-exactness

Symbol-level nongauge support proves only algebraic non-exactness at one
covector. Reduced cohomology requires separation from the closure of the
global gauge range.

Let `P` be the bounded `L2` projection that first takes tangential Fourier
mode `k=e4` and then retains only vector components `1` and `2`. For any
distributional gauge parameter `phi`, `(A phi)_a=partial_a phi`. At Fourier
mode `e4`, the components `a=1,2` vanish because `k_1=k_2=0`. The normal and
`e4` components are the only possible gauge support. Therefore

```text
P A_hit=0,              P A_miss=0.
```

But `P u=u` and `u` is nonzero. Since `P` is bounded, it also annihilates the
closure of either gauge range. Hence

```text
u notin im(A_hit),
u notin closure(im(A_hit)).
```

The hit class survives both the algebraic and reduced quotients without any
assumption that the full gauge range is closed. The miss realization excludes
`u` at the middle-domain boundary, so the same marked class is absent there.

This proves marked-class extension sensitivity. It does not prove that the
two complete cohomology spaces have different total dimension or cannot be
abstractly isomorphic through some unrelated map.

## Ownership and claim ceiling

The quadratic bulk action still admits both refined isotropics and selects
neither. The filed primary source remains silent on endpoint, asymptotic and
real/Krein selectors. The result is therefore a mathematical availability and
extension-sensitivity theorem, not a physical-domain selection.

No Hilbert self-adjointness, Fredholmness, global closed-range theorem,
positivity, probability rule, physical state space, quantum BRST measure,
source-selected global `Met(X)` geometry, particle result, canon change, or GU
verdict is claimed.

## Reproduction and continuation

`tests/channel-swings/b5_domain_compatible_brst_cohomology_probe.py` certifies
the exact symbol identities, normal middle rank/radical arithmetic, field-
stage Witt refinement, graph-extension and pullback-domain lemmas, coflip
compatibility, bounded Fourier separator, algebraic quotient, reduced
quotient, planted hostile controls, and claim ceiling. It passes `50/50`.

The next honest gate is `B5-KREIN-TO-PROBABILITY-POSITIVITY-DISCRIMINATOR`:
decide whether either mathematically available reduced class carries a
domain-selected positive physical pairing or prove that the action/source
silence leaves positivity extension-underdetermined. Total cohomology,
Fredholmness and source selection remain separate reopen conditions.

## Positivity continuation closed

The continuation is now decided in
`b5-krein-probability-positivity-discriminator-2026-08-21.md`. The marked hit
class is null for the native Green form. Exact positive fundamental symmetries
on its Witt plane necessarily mix the hit line with the opposite partner and
therefore do not preserve the admitted hit trace line. Arbitrary positive
auxiliary quotient norms exist, but the action and filed source select none
as a physical probability pairing. The correct current verdict is extension-
and metric-underdetermination, not a universal positivity no-go.
