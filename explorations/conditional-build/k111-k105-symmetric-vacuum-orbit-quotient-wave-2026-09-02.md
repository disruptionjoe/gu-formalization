---
title: "K111 K105 symmetric nonlinear vacuum orbit and quotient-descent boundary"
status: active_research
doc_type: conditional_symmetric_vacuum_orbit_and_quotient_descent_result
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact finite nonlinear variational and finite-group quotient theorem on the repository-coordinate K105 positive blind simplex; a symmetric quartic owner generates the 256 K110 weights as degenerate strict global minima and the retract family descends abstractly but not as a distinguished embedded K105 line; no source/GU action, physical branch law, spacetime or BV-BFV global quotient, Born derivation, prediction or confirmation follows
manifest: lab/process/k111-k105-symmetric-vacuum-orbit-quotient-wave.json
probe: tests/channel-swings/k111_k105_symmetric_vacuum_orbit_quotient_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K111 K105 symmetric nonlinear vacuum orbit and quotient-descent boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet is a finite nonlinear variational control on K105's exact
256-dimensional positive coefficient-blind seed simplex. It derives the
*values* in K110's nonuniform weight from permutation-symmetric coefficients,
classifies the complete degenerate vacuum orbit, and tests global finite-group
quotient descent. It is not Weinstein's action, a spacetime boundary theory,
or a BV-BFV quotient.

```gu-typed-objects
result: one S_256-invariant quartic boundary-vacuum functional has exactly the 256 permutations of (2,1,...,1)/257 as strict global minima; their K91 retract family descends abstractly through the orbit quotient but no invariant vacuum section or distinguished embedded K105 line descends
carrier: K105 positive coefficient-blind seed space B_plus of dimension 256 and its closed normalized nonnegative weight simplex Delta_255 LAYER=observed CHIRALITY=N/A
pairing: Euclidean coordinate pairing for the finite variational control, followed by K105's mixed lowerer only when each vacuum is transported to its already-proved retract ON=repository_boundary_vacuum_control
real_structure: real weights, real polynomial functional, real K105/K91 histories and real finite operational interface
grading: degree-zero boundary weight/action and inherited minimal K91 BRST grading on each retract
action_owner: repository-construction -- a finite symmetric nonlinear boundary-vacuum functional; not authenticated as Weinstein's source action or a physical GU boundary law
target: vacuum-orbit generation, equivariant retract-family transport and finite group orbit-quotient descent MAP-TYPE=quotient
```

## Inline preflight bookend

K107 proves that equivariant algebraic repackaging of the frozen K105 linear
data cannot select a positive blind line. K110 then supplies a nonuniform
weight, but its heavy coordinate is visible in the input. The present question
is narrower and different: can a nonlinear mechanism generate the exact
nonuniform *shape* without naming a coordinate, and can quotienting all
branches remove the remaining choice?

The route census compared a coordinate-biased source, another generated
operator, stochastic tie-breaking, symmetric convex optimization and a
symmetric nonconvex vacuum action. The first two repeat the known debit;
stochastic selection imports a measure and sample; a unique convex optimum is
fixed by the full symmetry. The exact nonconvex route is decisive because its
zero set, tangent Hessian, orbit and quotient can all be classified without a
numerical search. Its switch condition is simple: if the normalized zero set
contains anything besides the K110 orbit, the construction does not own the
claimed denominator.

## 1. A coordinate-free nonlinear owner of the weight values

Let

```text
n=256,                  a=2/257,                  b=1/257,
Delta={w in R^n : w_i >= 0 and sum_i w_i=1}.
```

Define the repository-constructed boundary-vacuum functional

```text
V(w)=sum_i ((w_i-a)(w_i-b))^2.                              (1)
```

It is nonnegative, quartic and invariant under every coordinate permutation.
Its coefficients contain `a` and `b` but no preferred coordinate. A point has
`V=0` exactly when every coordinate equals `a` or `b`. If `k` coordinates
equal `a`, normalization gives

```text
k a+(256-k)b=(256+k)/257=1,
```

so `k=1`. Therefore the complete global-minimum set is

```text
M={w^(j): w^(j)_j=2/257 and w^(j)_i=1/257 for i != j},       (2)
```

with exactly 256 elements. The full `S_256` action is transitive on `M`, and
each vacuum has stabilizer `S_255`.

For `f(x)=((x-a)(x-b))^2`, both wells have

```text
f''(a)=f''(b)=2(a-b)^2=2/257^2.                             (3)
```

Thus the ambient Hessian is positive diagonal at every vacuum, and its
restriction to the simplex tangent hyperplane is positive definite. Every
vacuum is a strict global minimum. This is an exact finite spontaneous-
symmetry-breaking control: the action does not encode `j`, but the set of
minima does not pick one `j` either.

## 2. Symmetric dynamics does not supply the missing branch

The uniform weight `u_i=1/256` is fixed by every permutation. Since all
coordinate derivatives of (1) agree there, the simplex-projected gradient
vanishes. In this exact control its restricted Hessian is also positive, so
the symmetric point is a metastable critical state rather than a dynamical
instruction to choose a vacuum.

Any deterministic `S_256`-equivariant evolution started from `u` remains
fixed by `S_256`; if it reaches a member of `M`, some asymmetry must enter
through initial data, a boundary condition, a superselection rule, noise, or a
different owned datum. The nonlinear action therefore removes the coordinate
label from its coefficients while preserving the branch-selection invoice.

## 3. Equivariant retract family over the complete vacuum orbit

For each `w^(j)` let

```text
P(w^(j))=P_j=e_j e_j^T.                                    (4)
```

The map is `S_256`-equivariant: `P(sigma w)=sigma P(w)
sigma^-1`. Every `P_j` is the K-self-adjoint positive projector already
licensed by the K105/K110 coefficient-blind premise. It owns the quotient by
its kernel and selects the corresponding existing K91 action/domain/Green
retract. Transporting K110's finite real state/effect, tensor, trace, domain
and bounded-dynamics interface along the same permutation gives a complete
equivariant family over all 256 vacua.

Nothing in (1)--(4) chooses a member of that family. The construction derives
one orbit of equivalent conditional interfaces, not one embedded physical
interface.

## 4. Global orbit quotient: abstract descent succeeds, embedded descent fails

Because `M` is transitive, `M/S_256` has one point. Form the total retract
family

```text
E={(w^(j), t e_j): j in {0,...,255}, t in R}.
```

Its orbit quotient is canonically an abstract real line: the scalar `t` is
unchanged by coordinate permutations. The K91 algebraic interface consequently
descends up to isomorphism. This is genuine global quotient descent for the
finite nonlinear configuration-space control.

But a section from the one-point quotient back to `M` would have to choose a
vacuum fixed by all of `S_256`, and no such vacuum exists. Equivalently, no
rank-one coordinate projector is invariant. Averaging the orbit gives

```text
(1/256) sum_j P_j = I_256/256,                              (5)
```

which has rank 256, not rank one. The quotient therefore remembers the
abstract one-mode interface and forgets which line embeds it into K105. An
abstract physical type can descend while concrete positive-polarization
selection remains open.

## 5. Ownership and claim ceiling

The exact advance over K110 is twofold. First, the nonuniform rational values
now arise as the complete global minima of one permutation-symmetric nonlinear
functional rather than from a coordinate-labelled weight input. Second, the
global orbit quotient cleanly separates abstract descent from embedded
selection. The remaining missing information is not the weight ratio; it is a
law or datum choosing an orbit representative when such a concrete embedding
is physically required.

This does not authenticate (1) as a source/GU action or boundary law. It does
not construct an actual spacetime, nonlinear field, BV-BFV or analytic domain
quotient. It does not derive the finite trace pairing as Born structure,
select a physical branch, score the delayed-choice holdout, or earn prediction
or confirmation credit.

## Inline postflight bookend

- **Strongest overclaim:** “spontaneous symmetry breaking selects the K105
  physical line.” Refused. The action produces a transitive set of 256 minima;
  it does not choose one member.
- **Strongest contrary construction:** an actual source-owned dynamical law
  with asymmetric boundary or superselection data may select one branch.
  Preserved as the exact reopener.
- **Strongest mistyping risk:** calling `M/S_256` a physical BV-BFV quotient.
  Refused. It is a finite configuration-space orbit quotient.
- **Weakest reproducibility seam:** checking only the displayed vacua would
  miss extra zero-action points. The certificate proves that every zero has
  coordinates in `{a,b}` and exhausts the normalization equation over all
  possible heavy-coordinate counts.

The standard-library exact certificate passes its baseline before hostile
mutation. It verifies the zero-set exhaustion, tangent Hessians, symmetric
critical control, orbit/stabilizer, equivariant family, abstract quotient and
full-rank average projector, then catches mutations of the mechanism,
selection, descent and claim ceilings. No source/GU action, physical branch,
spacetime/global BV-BFV quotient, Born derivation, held-out score, prediction,
confirmation, canon, paper or public posture moves.

## Reproduction

```bash
python3 tests/channel-swings/k111_k105_symmetric_vacuum_orbit_quotient_probe.py
python3 tests/channel-swings/k111_k105_symmetric_vacuum_orbit_quotient_probe.py --selftest
```
