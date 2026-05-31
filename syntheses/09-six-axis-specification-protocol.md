# Six-Axis Specification Protocol

This synthesis introduces the contributor-facing specification protocol now housed in [`../specifications/six-axis/`](../specifications/six-axis/).

The six-axis protocol is the control surface for future Geometric Unity-class proposals. A candidate is not admitted as a serious research object until it specifies:

1. **L1 substrate** - the mathematical object on which the candidate invariant lives.
2. **L2 observer** - the observer or computational class extracting the shadow.
3. **L3 pairing** - the channel or coupling between substrate and observer.
4. **L4 causal order** - the causal-order model in force.
5. **L5 emergence** - whether the candidate is a specific object, universality class, fixed point, or attractor.
6. **L6 coordination loop** - the feedback or dynamics that makes observer extraction well-defined.

The full template and worked examples are in:

- [`../specifications/six-axis/six-axis-template.md`](../specifications/six-axis/six-axis-template.md)
- [`../specifications/six-axis/examples/example-01-type-ii1-spectral-sm.md`](../specifications/six-axis/examples/example-01-type-ii1-spectral-sm.md)
- [`../specifications/six-axis/examples/example-02-sorkin-causal-set.md`](../specifications/six-axis/examples/example-02-sorkin-causal-set.md)
- [`../specifications/six-axis/examples/example-03-rg-universality-class.md`](../specifications/six-axis/examples/example-03-rg-universality-class.md)

## Why This Matters

The four no-go theorem families studied in this repository are class-relative. Each theorem assumes a substrate class, locality or causal model, observer-pairing mode, or emergence picture. Without a shared specification unit, "alternative substrate" proposals can look comparable while making incompatible assumptions.

The six-axis protocol forces every proposal to become a typed sextuple plus a chirality bridge claim and a first falsification test. This keeps heterodox work testable rather than atmospheric.

## Current Coupling Rules

The first batch of worked examples surfaced two hard coupling rules:

- **Sorkin causal sets:** L1 = Sorkin causal-set substrate and L4 = Sorkin partial-order causal class are coupled. In the Sorkin frame, the substrate is the causal order.
- **RG universality:** L5 = universality class requires L6 = RG flow as coordination dynamics. A universality class is defined by an equivalence relation under RG flow.

Future revisions should also split the Cartan/twistor L1 option into two distinct entries:

- Cartan/parabolic geometry on `Met(X)`.
- Twistor or Penrose-style substrate inversion.

## Admission Rule

A proposal that leaves any axis blank, vague, or filled by aesthetic language rather than a mathematical class is not rejected on substance. It is returned for sharpening.

That is the core purpose of the protocol: make proposals precise enough to fail well.
