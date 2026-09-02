---
title: "K105 K91 positive retract and polarization nonselection"
status: active_research
doc_type: exact_action_domain_Green_retract_and_positive_polarization_nonselection_result
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact split injection-retraction of the K91 free action, domain, Green pair and boundary form inside the K105 K155-carrier action, plus an exact e0/e1 symmetry witness against a uniquely selected positive line; no equivalence theorem for all positive subspaces, no source or physical quotient selection, state, Born law, prediction, confirmation or GU verdict
manifest: lab/process/k105-k91-positive-retract-nonselection-wave.json
probe: tests/channel-swings/k105_k91_positive_retract_nonselection_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K105 K91 positive retract and polarization nonselection

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet tests whether the K105 K155-carrier action contains K91 as
an exact action/cochain/domain/Green retract and whether K155's frozen data
select that retract. Existence closes the bridge obligation only at repository-
construction grade; it does not create a physical polarization.

```gu-typed-objects
result: K91 is an exact positive action-domain-Green retract of K105, but the frozen action has an exact symmetry exchanging two distinct retracts and therefore selects no unique positive line
carrier: K91 real split l2 gauge-plus-physical complex mapped into rapid l2 copies of K155 metric-10 plus distortion-448 LAYER=observed CHIRALITY=N/A
pairing: positive real l2 on the chosen K91 line, induced from the K155 lowerer without changing its ambient inertia (260,188,0) ON=repository_owned_action_control
real_structure: real injection and retraction; no complexification and no identification with the separate Cl(9,5) corpus
grading: one K91 shift ghost maps to the first of four K105 diffeomorphism ghosts; antifields restrict contragrediently
action_owner: repository-construction -- the retract maps are explicit but the positive-line choice is not source or physically selected
target: K91 action/cochain/domain/Green recovery and positive-polarization selection test MAP-TYPE=quotient
```

## Inline preflight bookend

This gate was released only after the K155-carrier correction action cleared
K104's mixed-pairing prerequisite and constructed the action-correction horn.
The distinct raw-`A_0` Noether owner remains open. The lens census covered chain
retractions, indefinite subspaces, coefficient kernels, action restriction,
closed-domain reducing subspaces, causal Green intertwining, symmetry
nonselection and state-positivity ceilings.

The cheapest test is coordinate zero in K155's frozen basis. It is positive
for `K`, lies in `ker(C_*^T K)`, and its paired metric gauge vector lies in
`im G_n`. The independent hostile question is whether another line has the
same data. Coordinate one does, and swapping zero with one preserves both `K`
and `C_*`.

## Exact split retract

Let `v=e_0 in D`, whose frozen basis label is `(0,0,1)`. Then

```text
v^T K v=1,             C_*^T K v=0.                         (1)
```

Let `a in R^4` be its first standard vector and put `u=G_n a`. Define the K91
field injection

```text
j(g,p)=(u g,v p)                                             (2)
```

and the field retraction

```text
r_g(h,T)=a^T(G_n^T G_n)^(-1)G_n^T h,
r_p(h,T)=v^T K T.                                            (3)
```

Then `rj=I`. The K91 gauge map `alpha -> (alpha,0)` intertwines with
`alpha -> (G_n a alpha,0)`. Since `Qu=0`, `C_*u=0` and (1) holds, restricting
the K105 action gives exactly

```text
S(j(g,p))=1/2 integral_R (|partial_t p|^2-|Omega p|^2)dt,    (4)
```

mode by mode. The Hessian and Euler operator preserve the line because the
off-diagonal coupling annihilates both `u` and `v`. Hence the maximal closed
domain, rapid core, retarded/advanced sine kernels and Green boundary form
restrict exactly to K91. This is a split action/domain/Green retract, not a
same-carrier congruence from K104's positive 448-space.

## Exact nonselection

In the frozen K155 coordinate basis, `256` positive and `183` negative
coordinate lines lie in `ker(C_*^T K)`. The statement is deliberately about
coordinate lines, not a classification of every positive subspace.

In particular, both `e_0` and `e_1` have `K`-norm one and both corresponding
rows of `C_*` vanish. The swap

```text
e_0 <-> e_1                                                  (5)
```

preserves `K`, `C_*`, the modal kinetic and potential terms, the gauge sector
and therefore the full K105 action, while exchanging two distinct K91
retracts. No unique line is invariant under this exact action symmetry.

Thus K105 proves existence but not selection. Choosing the K91 positive line
removes all 188 ambient negative directions and 259 additional positive
directions; K155's action does not own that removal. A source/action symmetry,
boundary polarization, positive state cone or observable interface must break
(5) before the retract can be called physical.

## Inline postflight bookend

- **Strongest overclaim:** reading one positive retract as K155's physical
  state space. Refused: the action has at least the exact `e_0/e_1` symmetry.
- **Strongest contrary construction:** a later boundary condition or state
  cone may select one line or a higher-dimensional positive subspace.
  Preserved; that is the exact reopener.
- **Weakest reproducibility seam:** the coordinate census is not an invariant
  classification of all positive subspaces. The nonselection result needs only
  the explicit action-preserving swap (5), which the probe checks exactly.

The exact probe passes `19/19`; its baseline-first hostile selftest catches
`14/14` mutations. K155's ambient pairing and rank-one leakage stay unchanged;
no source, physical-state, Born, prediction, confirmation, canon or public-
posture state moves.

## Reproduction

```bash
uv run --offline --with sympy python \
  tests/channel-swings/k105_k91_positive_retract_nonselection_probe.py
uv run --offline --with sympy python \
  tests/channel-swings/k105_k91_positive_retract_nonselection_probe.py --selftest
```
