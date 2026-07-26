---
title: "Conditional Source-Action Toy Construction Program"
date: "2026-07-26"
status: active_research
doc_type: conditional_construction_program
program_id: SRC-TOY-01
verdict: "PROGRAM_SPECIFIED; TOYS_UNBUILT; PROGRAM_NATIVE_LIFT_OPEN"
claim_grade: "CONDITIONAL CONSTRUCTION SPECIFICATION / NO SOURCE ACTION, CHIRALITY, GENERATION, OR FLAVOR DERIVATION"
owned_path: "lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md"
depends_on:
  - "GEOMETER-VS-PHYSICS-OBJECTS.md"
  - "explorations/source-action-requirements-spec-2026-07-13.md"
  - "canon/source-action-seiberg-witten-RESULTS.md"
  - "explorations/W154-reverse-engineered-source-action-2026-07-14.md"
  - "lab/process/construction-space-exploration-protocol.md"
  - "lab/active-research/triplet-boundary-flavor-conjecture-2026-07-25.md"
---

# Conditional Source-Action Toy Construction Program

## The question this program answers

Assume the strongest useful GU starting structure instead of asking the toy to
derive it:

- the gimmel geometry and the distinction between base and metric-on-metrics
  geometry;
- the `(9,5)` physical signature and Krein carrier;
- existence of the natural shiab/Clifford-contraction map at its earned scope,
  without assuming its unresolved rank, kernel, or uniqueness;
- the `ker Gamma` physicalization/cure requirement;
- a structurally located triplet carrier;
- the vectorlike completion `3E_+ + 3E_- + X`; and
- a source action that must own any physical selector, domain, boundary, and
  symmetry breaking it uses.

Under those assumptions:

> Can one small, target-blind action dynamically create a physical boundary or
> phase whose protected low-energy sector contains one chiral mode for each
> member of the independently located triplet, while keeping the global
> completion, anomaly accounting, mirrors, resources, and flavor provenance
> explicit?

This is a conditional construction question. It does not treat the assumptions
as evidence for GU or for three generations.

## Why the source action remains difficult after its shape is known

The known shape is an inverse constraint surface, not yet a generative law.
One can always manufacture

\[
S_{\mathrm{penalty}}=\sum_i \lambda_i\lVert C_i\rVert^2
\]

so that the desired constraints \(C_i=0\) minimize an action. That establishes
joint consistency at most. It does not explain why nature chooses those
constraints, why one operator domain is physical, why one chirality remains
accessible, or why a count or flavor texture is selected.

The scientific burden is therefore **rigidity**, not mere existence:

1. the action and admissible field space exist before the target is inspected;
2. the equations of motion generate the selecting background rather than
   receiving it as a boundary condition;
3. the result survives perturbation, regulator, anomaly, and mirror checks;
4. zero, non-three, vectorlike, and wrong-flavor outcomes remain possible
   returns; and
5. the same compact source structure addresses more than one requirement
   without sector-specific repair.

The existing Seiberg--Witten-like attempt supplies a sharp warning. A
Krein-isometric moment-map source has exact net chiral index zero. Therefore a
successful route must identify which assumption changes: a physical boundary
or defect, a non-Krein-isometric source term, a topological background, a
different operator domain, or an explicitly observer/access-relative result.
The change is part of the theory and cannot be hidden in notation.

## Construction fork: never transfer silently

| object | standard-field toy | program-native GU target |
|---|---|---|
| inner product | positive Hilbert pairing | split-signature Krein pairing and physical quotient |
| chirality mechanism | domain wall, APS boundary, overlap/Ginsparg--Wilson index | source-owned operator/domain on the gimmel/RS carrier |
| geometry | fixed \(d+1\)-dimensional background | \(Y^{14}=\mathrm{Met}(X^4)\), base/fiber geometry, and soldering |
| physicalization | ordinary spinor projection | `ker Gamma`, shiab, real/Krein closure, and super-IG/BV consistency |
| three | supplied independent triplet factor or selected topological index | independently located GU triplet plus a lawful physical selector |
| flavor | explicit spurions or Yukawa matrices | source-derived restricted noncommuting triplet breaking with a held-out result |

A standard-field toy can prove conditional compatibility and expose necessary
structure. It cannot establish the GU-native source action without a transport
map preserving the load-bearing operator, domain, index, real structure,
anomalies, and physical observables.

## The construction ladder

### Rung 0 — constraint compiler

Build a finite penalty action whose stationary locus realizes the full typed
constraint intersection.

**Earns:** nonempty conditional compatibility and a debugging oracle for later
rungs.

**Does not earn:** selection, explanation, uniqueness, physical locality,
chirality, or generation count.

**Required negative control:** delete or alter each penalty term and show which
desired property disappears. If no property changes, the term is ornamental.

### Rung 1 — finite spectral/matrix selector

Use

\[
\mathcal H_{\mathrm{toy}}
  = (T\otimes E_+)\oplus(T\otimes E_-)\oplus X,
\qquad \dim T=3,
\]

with explicit grading, real/Krein structure, mirror map, source coordinate
\(\phi\), and a finite operator \(D(\phi)\). Enumerate the smallest coefficient
space permitted by the chosen symmetries before selecting a favorable matrix.

**Questions:**

- Can a source coordinate open a protected gap for the mirror sector without
  setting a rank-three projector by hand?
- Which term first breaks the index-zero pairing?
- Does the selected subspace remain stable under admissible perturbations?
- Is the result global index three or only accessible rank three?

**Earns:** an exact algebraic feasibility theorem or scoped no-go.

**Does not earn:** locality, anomaly inflow, a physical boundary, or GU-native
operator status.

### Rung 2 — dynamical domain-wall source

This is the best first physical toy. On a simple \(d+1\)-dimensional
background, define

\[
S_{\mathrm{wall}}[\phi,\Psi,A]
=\int
\left[
 \frac12 |d\phi|^2
 \lambda(\phi^2-v^2)^2
 [\Psi,(i\!\not D_A+y\phi\,\Gamma_{\mathrm w})\Psi]_K
\right]
+S_{\mathrm{gauge}}+S_{\mathrm{inflow}} .
\]

Here \(T\) is the independently supplied triplet factor, \(\Psi\) is globally
vectorlike, and \(\phi\) is a candidate source field. The first comparator may
use the standard positive-Hilbert/domain-wall construction. A separate
program-native branch must replace it with a real Krein action and prove the
physical quotient rather than assuming transfer.

Run three versions in order:

1. **Imposed wall control.** Fix a sign-changing \(\phi\). This establishes
   only that unit index times an independent triplet hosts three localized
   chiral modes.
2. **Dynamical wall.** Derive the wall from the source-field equations and
   declared global/topological sector. This asks whether the action selects
   the region and orientation.
3. **Finite-volume completion.** Include the second wall, boundary, or other
   mirror completion and measure its gap and accessibility. Do not discard the
   partner by truncation.

The intended conditional result is:

> Given a GU-motivated vectorlike triplet carrier, a target-blind dynamical
> source can produce a protected chiral accessible sector while the complete
> theory and mirror accounting remain explicit.

That statement would still inherit the factor of three from the located
triplet. It would advance physical selection, not derive the triplet.

### Rung 3 — regulated overlap/Ginsparg--Wilson lift

Discretize the Rung-2 system with an exact finite regulator:

- overlap or Ginsparg--Wilson operator;
- explicit lattice index;
- determinant/measure and anomaly accounting;
- complete mirror census;
- boundary or defect inflow;
- deformation and finite-volume scaling; and
- source-field motion between topological phases.

This is the first rung at which a continuum index story is not protected by
an implicit regulator or omitted mirror. It should compare \(N=1,2,3,4\)
triplet-dimension controls and topological charges \(q=0,\pm1,\pm2,\pm3\).
Choosing \(q=3\) because the target is three must return
`THREE_TARGET_IMPORTED`.

### Rung 4 — program-native GU lift

Only after Rungs 1--3 expose the minimal mechanism, attempt the actual
operator-grade lift:

1. specify fields and configuration space on the gimmel/RS carrier;
2. replace the standard adjoint with the correct Krein pairing and prove the
   action is real;
3. derive the `ker Gamma` projection and shiab role from the action;
4. construct the physical operator and domain;
5. prove Fredholm/APS or other index admissibility;
6. establish BV/BRST closure, anomaly consistency, hyperbolicity, and the
   physical positive quotient;
7. classify global index, accessible rank, mirrors, and boundary inflow
   separately; and
8. expose every imported \(\sigma\), \(\tau\), flux, holonomy, K-class,
   boundary, scale, and comparator assumption.

This rung interfaces with `B5-INDEPENDENT-RECONSTRUCTION` and
`OrderThreeSourceActionSpectralPacket_V0`. It does not replace the required
full symbol-space enumeration or the source-action requirements specification.

### Rung 5 — flavor only after selection

Do not add flavor while the chirality/selection mechanism is still
underidentified. Once a protected triplet boundary sector exists, introduce
the smallest source-derived restricted algebra capable of producing two
noncommuting projected flavor operators.

Requirements:

- full triplet equivariance and one common cyclic algebra are retained as
  null controls;
- generic Yukawa matrices are fit-only positive controls;
- the symmetry-breaking fields and their representation are fixed before the
  observed spectrum is inspected;
- parameter and resource budgets are frozen; and
- at least one mass, mixing, CP, running, or partner relation is held out.

## Predeclared return contract

```text
TOY_ACTION_INCONSISTENT
PENALTY_COMPATIBILITY_ONLY
FINITE_SELECTOR_NO_LOCAL_LIFT
IMPOSED_BOUNDARY_HOSTING
DYNAMIC_BOUNDARY_SELECTED
THREE_TARGET_IMPORTED
THREE_VECTORLIKE_ONLY
EFFECTIVE_ACCESS_THREE
GLOBAL_INDEX_THREE_CONDITIONAL
MIRROR_OR_ANOMALY_FAILURE
FLAVOR_DEGENERATE
FLAVOR_FIT_ONLY
HELD_OUT_FLAVOR_RELATION
PROGRAM_NATIVE_TRANSPORT_FAILED
PROGRAM_NATIVE_OPERATOR_PACKET
```

No return below `PROGRAM_NATIVE_OPERATOR_PACKET` supplies GU's actual source
action. `GLOBAL_INDEX_THREE_CONDITIONAL` is not a generation derivation unless
the triplet, operator, domain, and relevant source data are independently
derived rather than assumed.

## Target-blind controls

Every rung that can emit a count or chiral sector must include:

1. triplet dimensions \(N=1,2,3,4\);
2. source sectors with zero, opposite, and non-target index;
3. the global vectorlike completion and every omitted mirror;
4. boundary-orientation reversal;
5. inert direct-sum stabilization and benign subdivision/refinement;
6. perturbations of every free coefficient inside a declared ball;
7. anomaly and inflow accounting;
8. restricted versus enlarged observer/intervention access;
9. explicit source, controller, environment, decoder, and resource ledgers;
10. a target-coded construction as a positive control that must be detected;
    and
11. a held-out observable fixed before parameter fitting.

## Relation to the 27-row requirements specification

This program attacks a narrow dependency slice:

- `SA-C1`: field-space/K-class declaration;
- `SA-C2`: `ker Gamma` physicalization/cure;
- `SA-C3`: realized chiral rank;
- `SA-Y1/Y2`: the allowed mass-type channel and its construction choice;
- `SA-Y5/Y7`: the need for structure beyond bare `Z/3` to differentiate
  flavor; and
- the UV requirements needed for the regulator, anomaly, causality, and
  physical quotient.

It does **not** solve the gravity, dark-energy, soldering, absolute-scale, or
full quantum-completion rows. A successful toy narrows the source action; it
does not silently become the complete source action.

## Best implementation order

1. Build the Rung-1 finite matrix compiler and enumerate the complete allowed
   coefficient class.
2. Build the Rung-2 imposed-wall control and then the dynamical-wall variant.
3. Lift the survivor to the Rung-3 overlap/Ginsparg--Wilson regulator.
4. Attempt the Rung-4 GU transport with an explicit standard/native fork
   audit.
5. Add Rung-5 flavor only if physical selection survives.

Each step returns an artifact useful under success or failure: a construction,
a scoped no-go, a minimal-extra-structure certificate, or a precise transport
obstruction. No step is justified merely because it makes the target appear.

## Completion and reopening

This document specifies the program; it does not execute a toy.

The immediate executable target is the complete Rung-1 coefficient
enumeration already demanded by `B5-INDEPENDENT-RECONSTRUCTION`, followed by a
minimal dynamical-wall comparator. Reopen a higher rung only when the lower
rung produces a target-blind survivor or a transport question that cannot be
answered below it.
