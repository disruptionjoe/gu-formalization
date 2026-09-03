---
title: "K117 K116 autonomous reservoir and causal-locality boundary"
status: active_research
doc_type: conditional_autonomous_reservoir_causal_locality_result
created: 2026-09-03
date: 2026-09-03
claim_ceiling: exact repository-owned autonomous Markov-additive work-reservoir dilation, finite detailed-balance/strong-lumpability no-go, resource-current identity and finite causal-lattice local-observable descent precursor for the K116/K115 finite control; no finite microscopic bath, Weinstein/source/GU action, continuum spacetime BV-BFV theory, AQFT state, Born rule, prediction or confirmation follows
manifest: lab/process/k117-k116-autonomous-reservoir-causal-locality-wave.json
probe: tests/channel-swings/k117_k116_autonomous_reservoir_causal_locality_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K117 K116 autonomous reservoir and causal-locality boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet answers K116's controller/resource invoice at the next
mathematical grade. It internalizes the work current in an autonomous,
time-homogeneous Markov-additive path law; proves why a finite closed
detailed-balanced strongly lumpable environment cannot realize the same
informative feed-forward chain; and gives a finite causal-lattice locality
and observable-descent precursor. Its reservoir coordinate is unbounded (or
equivalently chemostatted), not a finite microscopic bath. Its causal graph is
not a continuum BV-BFV field theory.

```gu-typed-objects
result: an autonomous Markov-additive lift exactly projects to K115, owns the K116 controller work as reservoir current, has nonzero informative cycle affinity and positive stationary resource consumption, forbids a finite detailed-balanced strongly lumpable realization, and descends local observables on a finite causal DAG
carrier: the K115 finite base-record chain extended by an additive work coordinate, and finite products of that local carrier on a three-site causal DAG u->v with z spacelike to v LAYER=observed CHIRALITY=N/A
pairing: stationary Markov flux pairing, edge log-rate-ratio pairing and finite observable algebra under generator restriction ON=repository_autonomous_resource_and_causal_locality_control
real_structure: real finite-state probabilities, real logarithmic work coordinate and real-valued local observables
grading: degree-zero classical stochastic process; inherited BRST/BFV grading is not used and no BV master complex is constructed
action_owner: repository-construction -- an autonomous time-homogeneous Markov-additive work ledger or ideal chemostat; not a finite microscopic reservoir, Weinstein's source action or a GU field action
target: exact resource ownership, equilibrium-lift obstruction and finite causal local-observable descent boundary MAP-TYPE=evaluation
```

## Inline preflight bookend

K116 gave an exact conditional path likelihood and priced the otherwise hidden
controller force, but it still inserted cancellation by hand. The route census
separated: a finite closed equilibrium lift, a finite transient fuel register,
an unbounded Markov-additive work reservoir, a chemostatted chemical network,
a Hamiltonian continuum bath, and a spacetime BV-BFV theory. The first route
is testable and fails by a cycle obstruction. A finite transient fuel register
can approximate a bounded observation window but cannot own a stationary
resource current indefinitely. The Markov-additive/chemostat route is the
smallest exact autonomous law that both recovers K115 and exposes where the
resource goes. A finite causal product construction is independently ready and
tests locality without pretending that missing continuum boundary data exist.

The cheapest kill is failure of exact projection or failure of the closed-cycle
work identity. The strongest contrary route is a finite nonequilibrium
controller with internal cycles or a Hamiltonian reservoir in a controlled
thermodynamic limit. Neither is excluded. The continuum BV-BFV route remains
dependency-blocked by the absence of an owned bulk action, boundary trace
domain, odd symplectic form and master equation.

## 1. K115 finite control and the nonreversible square

Use the exact three-state control inherited from K116. The base is
`x in Z/3`, the record is `r in Z/3`, base jumps have rate `kappa=2/5`,
and record refreshes have rate `lambda=7/11` with

```text
p_x(r)=81/113  when r=x,
p_x(r)=16/113  when r!=x.                               (1)
```

The projected generator is

```text
G f(x,r)=kappa sum_(y!=x)(f(y,r)-f(x,r))
          +lambda sum_s p_x(s)(f(x,s)-f(x,r)).          (2)
```

Consider the square

```text
(0,0) -> (0,1) -> (1,1) -> (1,0) -> (0,0).             (3)
```

The base edges are symmetric. The ratio of the product of forward rates to
the product of reverse rates is therefore

```text
C = p_0(1)p_1(0)/(p_0(0)p_1(1))
  = 16^2/81^2 = 256/6561 != 1.                          (4)
```

This is a certified Kolmogorov-cycle obstruction. It is exactly the
nonequilibrium circulation that K115 and K116 saw from stationary currents,
now isolated on a minimal four-edge loop.

## 2. Finite equilibrium strong-lumpability no-go

Suppose a finite hidden environment `e` carried a stationary detailed-balanced
Markov chain on `(x,r,e)` and was strongly lumpable onto the exact Markov chain
(2). Detailed balance of the lift implies reversibility of its stationary path
law. Strong lumpability makes the projected path law Markov with generator
(2), and projection preserves time-reversal invariance. The lumped chain would
therefore be reversible and obey every Kolmogorov cycle identity. Equation (4)
contradicts that conclusion.

Hence no finite stationary detailed-balanced strongly lumpable lift projects
exactly to informative K115. The qualifiers are load-bearing. This does not
exclude a finite nonequilibrium controller, a non-lumpable hidden process with
memory, or a finite fuel device over a bounded time interval. It proves that
the missing resource cannot be erased by merely adding finitely many hidden
equilibrium states while retaining the exact coarse Markov law.

## 3. Autonomous Markov-additive reservoir dilation

Set the dimensionless detector energy

```text
U_r(x)=-log p_x(r).                                      (5)
```

Extend each path by an additive reservoir-work coordinate `Z_t`. For a base
jump `(x,r)->(y,r)`, increment

```text
Delta Z = W((x,r)->(y,r))
        = U_r(y)-U_r(x)
        = log(p_x(r)/p_y(r)).                            (6)
```

For a detector jump `(x,r)->(x,s)`, set `Delta Z=0`. The transition rates are
still exactly those of (2) and do not depend on time or on `Z`. Thus
`(X_t,R_t,Z_t)` is an autonomous time-homogeneous Markov-additive process and
forgetting `Z` recovers K115 path-wise.

Every edge now has exact local detailed balance in the form

```text
log(q_ij/q_ji)=-(U_j-U_i)+W_ij.                          (7)
```

On detector edges `W=0`, so (7) is K116's detector-bath relation. On symmetric
base edges the left side vanishes and (6) supplies precisely the energy change.
The controller is no longer a costless force inserted into the base equation:
its work is an explicit additive current in the extended path law.

Because energy telescopes around any closed cycle, summing (7) gives

```text
cycle affinity = total reservoir work on the cycle.     (8)
```

For (3), the work factor is exactly `256/6561`, matching (4). The orientation
with positive affinity is the reverse cycle. The sign is conventional; the
nonzero magnitude is not.

This is an autonomous *open-resource* realization. The unbounded `Z` coordinate
may be read as a work ledger or as the integrated current supplied by ideal
chemostats. It is not a finite Hamiltonian reservoir. At stationary projected
operation the reservoir current drifts rather than settling to a normalizable
stationary distribution in `Z`, which is exactly where the sustaining resource
lives.

## 4. Stationary work rate equals entropy production in the control

The projected stationary law remains

```text
nu(x,r)=h_x(r)/3,
h_x(r)=1/3 + alpha(p_x(r)-1/3),
alpha=lambda/(lambda+3 kappa)=35/101.                   (9)
```

Direct rational stationarity checks every one of the nine nodes. Averaging
(6) over stationary base jumps gives

```text
J_W=sum_(x,r) nu(x,r) sum_(y!=x) kappa
                    log(p_x(r)/p_y(r)).                 (10)
```

For the exact control,

```text
J_W = 0.25863366222968864... nats per unit time > 0.    (11)
```

The standard edge entropy-production sum for the complete projected chain is
equal to (10), to numerical roundoff after exact rational flux construction.
This equality follows from stationarity: system-energy change averages to zero,
detector edges carry their thermal entropy flow, and the remaining closed-cycle
affinity is the base-edge work current. It is an identity for this declared
dimensionless Markov convention, not a universal Landauer equality or a
microscopic fluctuation theorem.

## 5. Finite causal-lattice local observable descent

Place one local K117 carrier on each vertex of the finite causal DAG

```text
u -> v,       z spacelike to v.                          (12)
```

The local generator at `u` uses `p_(x_u)`. The local generator at `v` may use
the causal-parent-controlled kernel whose preferred record is
`x_v+x_u mod 3`. The generator at `z` uses only its own state. The total
generator is the sum of the three local terms.

The exact certificate proves four finite locality statements:

1. an observable supported on the past-closed region `{u}` evolves under the
   `u` generator alone;
2. the generator of a `v`-supported observable depends only on `{u,v}` and is
   independent of the full state at spacelike site `z`;
3. the local `v` and `z` generators commute exactly; and
4. the causally ordered `u` and `v` generators need not commute, because a
   change in `x_u` changes the later detector kernel at `v`.

Thus finite local observables descend to their causal-past closure, while
spacelike local operations commute. This is a genuine theorem about the finite
causal Markov algebra constructed here. It is only a precursor to spacetime
field theory: there is no continuum manifold, hyperbolic operator, boundary
trace space, odd symplectic BFV form, BV master equation, local AQFT net,
Hadamard state or renormalized measure.

## 6. What K117 closes and what remains

K117 replaces K116's invisible controller cancellation with an explicit
autonomous path coordinate and resource current. It proves that the same exact
informative coarse law cannot come from a finite hidden equilibrium chain under
strong lumpability, and it demonstrates finite causal locality and observable
restriction on a nontrivial DAG.

It does not yet own a finite microscopic bath. The strongest next construction
must either build a finite nonequilibrium controller with a controlled
replenishment/thermodynamic limit, or derive the reservoir and couplings from a
source-owned action. Independently, the causal precursor must be replaced by a
genuine continuum causal BV-BFV bulk-boundary domain with trace maps, odd
symplectic data, a master equation and local observable descent. Only after a
state/probability owner is also supplied can Born or measurement language be
tested.

## Inline postflight bookend

- **Strongest overclaim:** “K117 builds a microscopic autonomous detector.”
  Refused. It builds an autonomous Markov-additive dilation whose sustaining
  coordinate is unbounded or chemostatted.
- **Strongest contrary construction:** a finite nonequilibrium hidden
  controller can sustain circulation when coupled to maintained affinities,
  and a non-lumpable equilibrium lift can generate memory after projection.
  The theorem excludes neither; it excludes finite detailed-balanced strong
  lumpability onto the exact Markov law.
- **Strongest mistyping risk:** calling the finite DAG a BV-BFV spacetime.
  Refused. It proves causal support and commutation in a finite Markov
  observable algebra and leaves every continuum symplectic/domain ingredient
  open.
- **Weakest reproducibility seam:** a simulation could confuse a balanced
  stationary distribution with reversibility. The exact control checks all
  node divergences, then independently checks the nonunit four-edge cycle and
  its work factor.

The certificate runs a clean exact baseline before every hostile mutation. No
source/GU action, finite physical reservoir, continuum BV-BFV theory, AQFT
state, Born derivation, held-out score, prediction, confirmation, canon, paper
or public-posture surface moves.

## Reproduction

```bash
python3 tests/channel-swings/k117_k116_autonomous_reservoir_causal_locality_probe.py
python3 tests/channel-swings/k117_k116_autonomous_reservoir_causal_locality_probe.py --selftest
```
