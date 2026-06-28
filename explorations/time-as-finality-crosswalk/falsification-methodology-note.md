---
title: "Falsification Methodology Note"
status: exploration
doc_type: methodology
updated_at: "2026-06-17"
related_artifact: "bridge-audit-crosswalk.md"
---

# Falsification Methodology Note: T26/T27 and GU Framework

**Purpose.** This note records a falsification attempt made during the T27
bridge audit session and the methodology it produced.  The attempt was to
derive the four fundamental forces from the T26 D1RestrictionSystem framework.
It failed.  This note records why, and what a genuine derivation would require.

**Non-goal.** This is not a proof that the forces cannot be derived from the
framework.  It is a record of what falsification tests revealed.

---

## What was attempted

During the T27 session, after confirming that the Projection-Obstruction Pattern
appears across physics (Witten, NN) and distributed systems (CAP), the question
arose: can the four fundamental forces be derived from the T26 D1RestrictionSystem
structure?

A derivation was attempted using the following heuristic mapping:

| Force | T26 analog used |
| --- | --- |
| Gravity | reversal_cost (high cost = strong curvature analog) |
| Electromagnetism | accessible_support=1 + branch_support=1 |
| Weak nuclear | branch_support > 0 (chirality carrying) |
| Strong nuclear | holder_redundancy (confinement analog) |

The argument: sites with these D1Profile configurations appear in the richer
systems that evade chirality no-go theorems, therefore they encode force-like
structure.

---

## Three falsification tests

### Test 1: Ordering dependence

The mapping from D1Profile dimensions to forces is arbitrary.  There is no
principled reason why accessible_support should correspond to electromagnetism
rather than the strong force, or why reversal_cost should correspond to gravity
rather than the weak force.  A genuine derivation would fix a unique mapping
from first principles.  The heuristic mapping can be permuted freely without
violating any constraint in the T26 axioms.

**Result:** FAILS.  The mapping is post-hoc.

### Test 2: Post-hoc counting

The four D1Profile dimensions (accessible_support, holder_redundancy,
branch_support, reversal_cost) happen to match the four fundamental forces in
number.  But the match is coincidental: D1Profile has four dimensions because
T26 was designed to capture four independent aspects of observer access.  The
forces have four members for independent physical reasons.

A genuine derivation would show that the specific values of the D1Profile
dimensions at each site (not just their count) correspond to measurable
properties of the forces: coupling constants, gauge group rank, symmetry
breaking patterns.  No such correspondence was established.

**Result:** FAILS.  Count match is not a derivation.

### Test 3: Numerical correctness

The coupling constants of the four forces (fine structure constant ~1/137,
strong coupling ~1, Fermi constant ~1.17e-5 GeV^-2, Newton constant
~6.67e-11 N m^2 kg^-2) are not derivable from any combination of the
small integer D1Profile values used in T26.  The D1Profile dimensions take
values in {0, 1, 2, 3} for the cases studied.  No dimensionful quantity or
coupling hierarchy emerges.

**Result:** FAILS.  No numerical correspondence.

---

## What a genuine derivation would require

A genuine derivation of the four forces from a restriction-system framework
would require at minimum:

1. **A principled force identification rule** that maps features of the
   restriction system to force carriers uniquely and without free parameters.
   The rule must be derivable from the axioms, not chosen to match.

2. **Symmetry group recovery** from the restriction system.  The forces are
   characterized by their gauge groups (U(1), SU(2), SU(3)).  A derivation
   must recover these groups from the morphism structure or the site categories.

3. **Coupling hierarchy** emerging from the restriction-system structure.
   The ratio of the strong coupling to the electromagnetic coupling (~137)
   must follow from the structure, not from a free parameter.

4. **Exclusion of other "forces."** The derivation must show why exactly four
   forces appear and not three or five.  This requires a completeness argument,
   not just an existence argument.

The T26 framework as of T27/T28 does not supply any of these.  It supplies:
- A finite obstruction structure
- A projection-obstruction pattern across domains
- A morphism structure that distinguishes enrichment from category change

These are genuine and useful.  They are not a force derivation.

---

## What the failed attempt reveals

The failure has a precise structure.  The T26 D1Profile dimensions encode
information-theoretic properties of observer access:

- **accessible_support**: is the data accessible at all?
- **holder_redundancy**: how many independent mechanisms carry it?
- **branch_support**: does it branch (chiral separation)?
- **reversal_cost**: how costly is it to suppress or reverse?

These dimensions were chosen to capture chirality and information flow, not
force mediation.  The fact that they can be loosely analogized to force
properties is a reflection of the general structure of gauge theories (which
also deal with accessibility, redundancy, branching, and suppression costs),
not a derivation.

The correct lesson: the T26 framework captures the class-relative structure
of impossibility results.  It does not capture the dynamics of force
mediation.  A framework that captured both would need to combine restriction-
system structure with gauge-theoretic content.  That is a much harder problem
and an open question in the GU formalization program.

---

## Reusable falsification methodology

The three tests above generalize to a methodology for evaluating any
proposed "derivation" from the T26/T27/T28 framework:

**Test A (Ordering independence):** Can the mapping from framework features
to the claimed object be permuted without violating any constraint?  If yes,
the mapping is arbitrary.

**Test B (Post-hoc counting):** Does the derivation rely on a coincidence
of cardinalities?  If yes, check whether a principled uniqueness argument
exists.  If not, the derivation fails.

**Test C (Numerical correspondence):** Do the quantitative predictions of
the derivation match the measured values of the claimed object?  For physics
claims, this is the hardest and most decisive test.

These tests are listed in order of increasing strength.  A derivation that
fails Test A does not need to be tested against Tests B and C.

---

## Summary

The four-forces derivation attempt failed all three tests.  The failure is
informative: it locates the boundary of T26/T27 precisely.  The framework
captures class-relative obstruction structure.  It does not capture force
dynamics.  Future work that attempts to bridge these should explain, from
first principles, how gauge symmetry groups emerge from restriction-system
morphism structure.
