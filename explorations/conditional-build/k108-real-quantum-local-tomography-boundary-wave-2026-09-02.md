---
title: "K108 real-quantum local-tomography boundary"
status: active_research
doc_type: quantum_anchor_composition_countermodel
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact finite-dimensional countermodel showing the two admitted quantum anchors do not select complex scalars or local tomography; no GU-native state, observable, Born or prediction result
manifest: lab/process/k108-real-quantum-local-tomography-boundary-wave.json
probe: tests/channel-swings/k108_real_quantum_local_tomography_boundary_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K108 real-quantum local-tomography boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet asks whether the two admitted calibration anchors—massive
matter-wave interference and spacelike Bell violation with operational
no-signalling—select the complex, locally tomographic quantum composition
rule. It supplies a real-quantum contrary model and makes no source or GU
attribution.

```gu-typed-objects
result: real two-level systems satisfy the frozen interference and Bell no-signalling controls while their real composite contains one globally visible J tensor J direction invisible to every local symmetric-product effect
carrier: Sym2(R2) locally and Sym2(R4) globally LAYER=toy CHIRALITY=N/A
pairing: trace expectation on real symmetric state and effect matrices ON=conditional_comparator
real_structure: real Hilbert spaces with transpose star
grading: bipartite tensor grading A versus B
action_owner: comparator; states, effects and composition are imported data
target: local tomography and scalar-field selection from the two calibration anchors MAP-TYPE=evaluation
```

## Inline preflight bookend

K82 already proves that weak GPT demands do not select the Tsirelson boundary,
while K83 shows that one positive star-state algebra suffices for it. The next
route-changing question is whether interference plus Bell saturation selects
the familiar complex composition itself. Real quantum theory is the cheapest
contrary route: all matrices needed for both anchor controls are real, but its
composite dimension differs from the locally generated product span.

The selected method is an exact dimension-and-orthogonality theorem. A broad
GPT search is dominated because one explicit model is enough to refute
selection. Computation checks the complete two-level basis, state positivity,
interference, Bell value and marginals.

## The hidden composite direction

A local rebit has symmetric observable space `Sym2(R2)`, dimension three, with
basis `I,X,Z`. The bipartite real composite has symmetric observable space
`Sym2(R4)`, dimension ten. Products of local symmetric observables span only

```text
3 times 3 = 9
```

dimensions. Let

```text
J = [[0,-1],[1,0]],       H = J tensor J.
```

Although `J` is antisymmetric, `H` is symmetric, `H^2=I`, and

```text
tr(H(A tensor B)) = tr(JA) tr(JB) = 0
```

for every real symmetric local `A,B`. Thus `H` spans the missing global
direction.

The states

```text
rho_plus  = (I+H)/4,
rho_minus = (I-H)/4
```

are distinct, positive and trace one. They agree on every local product
effect, but `tr(rho_plus H)=1` and `tr(rho_minus H)=-1`. The real composite is
therefore not locally tomographic.

## Both admitted anchors still fit

The same real theory supplies exact two-path interference. The coherent states
`(1,1)/sqrt(2)` and `(1,-1)/sqrt(2)` give probabilities one and zero against
the plus projector, while their incoherent mixture gives one half.

It also supplies the exact Bell control. The real Bell vector
`(|00>+|11>)/sqrt(2)`, real Pauli `X,Z`, and Bob settings
`(Z+X)/sqrt(2),(Z-X)/sqrt(2)` give CHSH `2 sqrt(2)`. Each local marginal is
`I/2`, so the nonselective local statistics obey operational no-signalling.

Therefore the admitted anchors do not distinguish this real, non-locally-
tomographic composite from the usual complex control. A local-tomography,
complex-orientation, composite-dimension or equivalent operational demand must
be independently justified before the reverse scaffold can select that part of
the physical-state interface. Importing it would fit the desired theory rather
than derive it.

## Inline postflight bookend

- **Strongest overclaim:** “the anchors cannot select quantum theory.” Refused.
  They already exclude classical CHSH and PR extensions once the positive
  star-product packet is supplied. This packet shows only that they do not
  select complex scalars or local tomography within quantum alternatives.
- **Strongest contrary route:** an additional operational local-tomography
  axiom excludes the displayed real composite. Preserved as the exact
  reopener; it is not currently produced by GU or the two anchors.
- **Weakest reproducibility seam:** dimension counting alone might hide an
  unphysical direction. The explicit `rho_plus/rho_minus` pair proves the
  tenth direction changes positive normalized global states while remaining
  invisible to every local product effect.

No GU carrier, quotient, observable algebra, Born rule, source owner,
prediction, confirmation, canon, paper, ledger or public posture moves.
Delayed-choice entanglement swapping remains reserved and unscored.

## Reproduction

```bash
uv run --with sympy==1.14.0 python \
  tests/channel-swings/k108_real_quantum_local_tomography_boundary_probe.py
uv run --with sympy==1.14.0 python \
  tests/channel-swings/k108_real_quantum_local_tomography_boundary_probe.py --selftest
```
