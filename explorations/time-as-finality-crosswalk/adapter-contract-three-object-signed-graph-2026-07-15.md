---
title: "Corrected tri-repo signed-graph comparison: one common predicate, not a native-object isomorphism"
status: exploration
doc_type: cross-repo-comparison
created: 2026-07-15
corrected_by: ADAPTER2-01
runnable:
  - explorations/time-as-finality-crosswalk/adapter_three_object.py
verdict: "COMMON HARARY-BALANCE PREDICATE ON A SHARED ENCODING; FULL ADAPTER NOT ESTABLISHED"
---

# Corrected signed-graph comparison

## What is proved

On one shared signed-graph input, three algorithms agree:

```text
XOR satisfiable
= signed graph balanced
= no negative cycle
= Z/2 edge cocycle exact.
```

`adapter_three_object.py` verifies the equivalence on controls and 720
generated instances. This is Harary's balance theorem expressed through three
algorithms.

TaF T39 genuinely uses this binary same/different CSP. GU Gate 2a can also be
encoded as an XOR consistency problem. The comparison is therefore useful at
the common-predicate level.

## What is not proved

Algorithm agreement after all three views have been placed on the same graph
does not construct invertible maps from the complete native GU, TaF, and TI
objects into one another. In particular:

- TI E155 concerns confluence and its fork locus, not a general signed-graph
  object;
- TI E160 says nontrivial `Z/2` transport requires a source-side,
  composition-compatible parity rule and is not derived from bare loops;
- orientations placed on the shared graph do not affect balance;
- the two global colorings of a connected balanced graph are related by a
  relabeling symmetry, with no canonical positive choice; and
- no map from that relabeling freedom to the GU Krein sign is supplied.

## Current grade

The common Harary predicate survives. Calling it an `ISO` of the source objects
or a proven cross-repo adapter is withdrawn. It supplies a candidate interface
and an obstruction vocabulary, not an identity theorem.

See `adapter2-correction-polarity-fiber-not-axis-2026-07-15.md` for the
downstream correction.
