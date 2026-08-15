---
title: "Selected-K98 balanced RSAP BFV and selection classifier"
status: active_research
doc_type: exact_classical_bfv_construction_and_variational_ownership_classifier
created: "2026-08-15"
registry: lab/process/selected-k98-rsap-balanced-bfv-selection-classifier.json
probe: tests/channel-swings/selected_k98_rsap_balanced_bfv_selection_classifier_probe.py
grade: "CANONICAL RIGHT-H_BAL BFV REDUCTION IS REGULAR AND IRREDUCIBLE; CURRENT BARE ACTION STILL DOES NOT OWN THE GAUGE LAW"
target_claim: K97_NEXT_GATE__CURRENT_ACTION_OWNS_RIGHT_H_BAL_COISOTROPIC_AND_GAUGE_LAW
target_verdict: CURRENT_BARE_ACTION_NO__CANONICAL_MATHEMATICAL_BFV_COMPLETION_YES
canon_verdict_change: none
---

# Selected-K98 balanced RSAP BFV and selection classifier

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE`

Scope: this result binds the finite-dimensional classical epsilon-preboundary
cotangent carrier and the reverse-constructed balanced subgroup only. It does
not bind an analytic field theory, physical phase space, quantum state space or
particle comparator.

## Result first

K97's missing law has a canonical **mathematical** BFV completion. Let

```text
G = Spin_0(7,7),
H_bal = Spin_0(3,4) x Spin_0(4,3)     (up to the finite central quotient),
h_bal = so(3,4) + so(4,3).
```

On the action-owned formal parent `T*G`, the cotangent-lifted right action has
moment map

```text
J_R(g,lambda) = lambda restricted to h_bal
```

up to the harmless global sign convention. The right action of `H_bal` on
`G` is free. Its fundamental-vector map is injective at every `g`, and the
fibre derivative of `J_R` is the surjective restriction
`g* -> h_bal*`. Therefore:

```text
rank(dJ_R) = 42 everywhere,
0 is a regular value,
the 42 constraints are irreducible,
J_R^(-1)(0)/H_bal = T*(G/H_bal),
dim = 182 - 2(42) = 98.
```

For a basis `e_a` of `h_bal`, structure constants
`[e_a,e_b]=f_ab^c e_c`, ghosts `c^a` and conjugate ghost momenta `b_c`, the
minimal classical charge is

```text
Omega_bal = c^a J_a - (1/2) f_ab^c c^a c^b b_c.
```

Moment-map equivariance and Jacobi give `{Omega_bal,Omega_bal}=0` exactly.
Unlike the earlier full-`so(7,7)` frozen-distortion presentation, this
constraint system has no stabilizer-induced reducibility: right multiplication
on `G` is free. No ghosts-for-ghosts are required at this finite classical
grade.

This closes BFV **constructibility**, not action selection. The selected bare
epsilon action still contains no declaration that right `H_bal` is gauge and
no multiplier or ghost sector enforcing `J_R=0`. The exact disposition is:

```text
canonical finite-dimensional classical BFV completion: CONSTRUCTED
regularity and irreducibility of its 42 constraints: PROVED
current bare action ownership of that gauge law: NOT CONSTRUCTED
physical GU phase-space selection: OPEN
```

## Why a boundary functional alone cannot supply the full law

A scalar boundary functional `F:G->R` produces the Lagrangian graph

```text
Gamma_dF = {(g,dF_g)} inside T*G,
dim Gamma_dF = 91.
```

If `F` is right-`H_bal` invariant, then `dF_g` annihilates the vertical
right-`h_bal` directions, so `Gamma_dF` lies inside `J_R^(-1)(0)`. But the
complete zero set has dimension `140`, not `91`. After quotient,

```text
Gamma_dF/H_bal has dimension 49,
T*(G/H_bal) has dimension 98.
```

The quotient graph is one Lagrangian inside the reduced phase space; it is not
the reduced phase space itself. If `F` is not right-invariant, its graph does
not even lie in the desired zero level. Thus an ordinary endpoint functional
can select a state or Lagrangian boundary condition inside the balanced
reduction, but it cannot by itself manufacture the whole coisotropic
constraint surface plus the declaration that its characteristic directions
are gauge.

The full law requires new dynamical ownership: at minimum a right-`H_bal`
gauge declaration and a multiplier/connection sector imposing the 42 moment
constraints; its BFV presentation then adds the corresponding 42 ghost and 42
ghost-momentum variables. Those data are canonical once the gauge law is
postulated, but the postulate is not derived from dimension `98`, global
surjectivity, or the success of the reduction.

## Compatibility with the certified boundary horns

- **Free epsilon endpoint variation** forces the entire covector to zero. It
  lies inside `J_R=0` but is strictly stronger and collapses the nonzero
  balanced fibres; it does not recover the K96 carrier.
- **Fixed epsilon endpoint data** leaves the covector unrestricted and treats
  transformations moving the datum as boundary symmetries; it supplies
  neither the 42 constraints nor their gauge quotient.
- **Generated/Robin graph** reaches the zero level only when its generator is
  right-`H_bal` invariant, and then selects only a 49-dimensional reduced
  Lagrangian rather than the full 98-dimensional phase space.
- **Gauged/multiplier completion** can construct the exact law and its minimal
  BFV charge, but it is a new completion not present in the selected bare
  action record.

## Exact certificate

The companion probe uses the fixed K88/K97 `Q` and balanced involution. It
checks the exact `91=42+49` symmetric decomposition, rank `42` of restriction
to `h_bal`, nondegeneracy of the trace pairing on both summands, closure of all
`861` unordered `h_bal` brackets, Jacobi on all `11,480` unordered triples,
commutation of the two direct-sum factors, and the missing-generator negative
control. It replays K97 before testing the new registry and claim ceilings.

Computation is only the finite certificate. Freeness, submersivity, graph
dimension and the ownership conclusion are structural.

## Route comparison and hostile boundary

- **Cotangent reduction/BFV — selected:** directly decides regularity,
  irreducibility and master closure.
- **Variational geometry — selected:** separates a boundary graph from a
  coisotropic constraint and gauge quotient.
- **Lie theory — exact support:** verifies the concrete real form and direct
  sum rather than transferring the full-`so(7,7)` fixture.
- **Koszul--Tate — simplifying result:** no relation bundle or
  ghost-for-ghost tower is needed for this free action.
- **Analytic/PDE — downstream:** an ultrahyperbolic functional domain cannot
  create missing gauge ownership and remains unconstructed.
- **Source criticism — adverse:** the source owns the parent epsilon
  potential, not this subgroup declaration or BFV extension.
- **Physics — bounded:** classical reduction is not positivity, quantization,
  particle content or phenomenology.

The strongest overclaim would be that BFV closure makes the 98-dimensional
horn physical. It does not. The strongest contrary route is an explicit
source/action boundary gauge completion whose Euler and Noether data produce
the right `H_bal` constraints. That would change ownership, not the present
mathematical BFV theorem. The weakest seam is precisely that absent completed
action; no amount of exact finite Lie algebra checking supplies it.

## Next gate

The mathematical branch is now maximally sharp. Reopen physical selection
only with an explicit source/action-owned right-`H_bal` multiplier,
connection or boundary gauge term, and verify that its Noether identity,
boundary variation and constraint surface reproduce `J_R=0`. If such a term
is constructed, the next dependent gate is its analytic BFV domain and
positivity. Without that new owner, retain charged boundary symmetry or the
full formal `182D` parent; do not repeat the finite BFV algebra.

No ledger, datum, quotient booking, canon claim, public posture, W/mirror
choice, chirality or generation count changes.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k98_rsap_balanced_bfv_selection_classifier_probe.py
```
