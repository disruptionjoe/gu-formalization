---
title: "K119 K118 collision Hamiltonian and thermodynamic reservoir boundary"
status: active_research
doc_type: conditional_collision_hamiltonian_thermodynamic_reservoir_result
created: 2026-09-03
date: 2026-09-03
claim_ceiling: exact repository-owned local collision-Hamiltonian dilation, K115 reduced-rate scaling law, fresh-tape Hamiltonian thermodynamic limit, finite collision-slab nongauge BV-BFV owner and outgoing flux accounting only; the fresh-tape limit is not a finite closed equilibrium bath, is not K118's Klein-Gordon field and is not Weinstein's source or a GU action, and no relativistic continuum limit, nontrivial gauge theory, AQFT state, Born rule, prediction or confirmation follows
manifest: lab/process/k119-k118-collision-hamiltonian-thermodynamic-reservoir-wave.json
probe: tests/channel-swings/k119_k118_collision_hamiltonian_thermodynamic_reservoir_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K119 K118 collision Hamiltonian and thermodynamic reservoir boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet constructs a local, reversible Hamiltonian interaction
between the nine-state K115 controller and one cell of an edge-labelled
reservoir tape. Tracing a freshly prepared cell gives the exact Euler channel
`I+hQ`, and repeated fresh collisions converge to the K115 semigroup with a
quantitative binomial-to-Poisson bound. The finite collision action owns its
unitary variational dynamics and minimal nongauge BV-BFV boundary identity.
It does not couple K118's Klein-Gordon field, derive a probability postulate,
or turn the fresh reservoir state and shift into source/GU data.

```gu-typed-objects
result: an explicit local collision Hamiltonian whose fresh-cell reduction is exactly I+hQ for K115, with a controlled repeated-collision thermodynamic limit, environmental flux record and finite collision-slab BV-BFV owner
carrier: C9 K115 base-record system times an edge-labelled finite reservoir cell, extended to finite and infinite one-dimensional cell tapes LAYER=observed CHIRALITY=N/A
pairing: finite Hilbert inner product and boundary symplectic pairing for each collision; stationary Markov flux and forward-reverse output-label likelihood pairing ON=repository_collision_model
real_structure: computational-basis conjugation on the real orthogonal collision amplitudes, with complex Schrödinger phase in the Hamiltonian action
grading: degree-zero system and tape states; BV antifields of degree minus one; no ghost, BRST or nontrivial gauge grading
action_owner: repository-construction -- explicit step-dependent collision Hamiltonian plus supplied fresh vacuum cells and one-pass shift; not Weinstein's source action or a GU action
target: local interaction-to-rate scaling, Hamiltonian reservoir limit and exported nonequilibrium accounting MAP-TYPE=evaluation
```

## Inline preflight bookend

The reverse-scaffold frontier contained five serious routes: a generic
Stinespring dilation of K115, a repeated-interaction/collision model, a Davies
weak-coupling reservoir, a chiral continuum input-output field, and a direct
coupling to K118's Klein-Gordon host. K91 already owns one stipulated finite
unitary instrument; K95 owns a supplied GKSL generator; K99 derives a graph
from an admitted Davies interaction but explicitly lacks a microscopic
weak-coupling theorem. K118 owns a separate free relativistic host and a
finite driven ring, but no common coupling.

The collision route is selected because an explicit star rotation derives
every Kraus amplitude from the K115 rate matrix and exposes the reservoir
resource rather than hiding it behind an existence theorem. The chiral-field
and Davies routes would require a common unbounded-domain and white-noise
limit that the repository does not own. Direct Klein-Gordon coupling would
invent a physical interaction. The cheapest kill is failure of exact channel
recovery or of the fixed-horizon product limit. The strongest contrary route
is a relativistic reservoir with a proved weak-coupling limit on K118's
Sobolev domain; if constructed, it supersedes the tape as the common host.

The route-changing lenses were finite Markov generators, exact unitary
dilation, repeated interactions, Hamiltonian recurrence, open-system limits,
stochastic thermodynamics, first-order variational/BV-BFV structure,
continuum locality, source custody, probability semantics, and hostile
philosophy of science. Exact finite algebra is the primary method;
computation is a certificate and hostile-mutation instrument, not the source
of the theorem.

## 1. The K115 rate matrix

Use the exact three-state control from K115--K118. A state is
`i=(x,r)` with `x,r in Z/3`. Put `kappa=2/5`, `lambda=7/11`, and

```text
p_x(s)=81/113 when s=x, and 16/113 otherwise.                (1)
```

The nonzero off-diagonal rates are

```text
q_((x,r),(y,r))=kappa                    for y != x,
q_((x,r),(x,s))=lambda p_x(s)            for s != r.         (2)
```

Let `q_i=sum_(j!=i) q_ij` and `Q_ii=-q_i`. The largest exit
rate is

```text
Lambda=max_i q_i=4/5+(7/11)(97/113)=8367/6215.              (3)
```

K115's stationary law `nu` obeys `nu Q=0`. No new stochastic
law has been selected here; (1)--(2) are the exact inherited target whose
microscopic ownership K119 tests.

## 2. One explicit local Hamiltonian collision

Let the system space have basis `|i>` for the nine K115 states. A single
reservoir cell has a vacuum `|0>` and one orthogonal label `|j<-i>` for every
directed edge with `q_ij>0`. For each source state define

```text
|a_i> = |i>|0>,
|B_i> = q_i^(-1/2) sum_(j!=i) sqrt(q_ij)|j>|j<-i>.          (4)
```

The planes `span{|a_i>,|B_i>}` are mutually orthogonal because the emitted
label remembers its source. For `0<h<=Lambda^(-1)` choose

```text
cos(theta_i)=sqrt(1-h q_i),       sin(theta_i)=sqrt(h q_i),
H_h=sum_i (theta_i/h) i(|B_i><a_i|-|a_i><B_i|).            (5)
```

`H_h` is self-adjoint and local to the system plus the cell at the tape
boundary. Its unitary `U_h=exp(-ihH_h)` acts by the star rotation

```text
U_h|a_i>=sqrt(1-hq_i)|i>|0>
          +sum_(j!=i)sqrt(hq_ij)|j>|j<-i>.                 (6)
```

The reverse rotation is present on every excited star plane. Thus the joint
collision is microscopically reversible even though the reduced channel on a
fresh vacuum cell is not.

## 3. Exact reduced channel and the controlled rate limit

Tracing the cell in its named label basis gives Kraus operators

```text
K_0=sum_i sqrt(1-hq_i)|i><i|,
K_(j<-i)=sqrt(hq_ij)|j><i|.                                (7)
```

On diagonal system states the channel is exactly the stochastic matrix

```text
P_h=I+hQ.                                                   (8)
```

Consequently `(P_h-I)/h=Q` coefficient by coefficient and `nu P_h=nu` for
every admitted `h`. For `h=1/m` and an integer horizon `t`, the deterministic
collision law is `P_(1/m)^(mt)`. Uniformize
`Q=Lambda(P-I)`. Then one Euler step is

```text
I+Q/m=(1-Lambda/m)I+(Lambda/m)P.                            (9)
```

The number of effective `P` updates in `mt` steps is binomial with parameters
`(mt,Lambda/m)`, while `exp(tQ)` uses a Poisson variable of mean
`Lambda t`. Le Cam's elementary binomial-to-Poisson bound and contraction by
the Markov kernel give

```text
d_TV(delta_i P_(1/m)^(mt), delta_i exp(tQ))
 <= t Lambda^2/m -> 0.                                     (10)
```

The exact probe independently evaluates the matrix exponential at `t=1`.
For `m=4,8,16,32` the measured total-variation errors are approximately
`0.04433,0.02099,0.01022,0.00504`, strictly decreasing and below (10).

Variation has not directly generated randomness. Equations (5)--(6) come
from the action; the reduced rates appear only after the supplied cell
preparation, partial trace, and scaling limit. This owner decomposition is
load-bearing.

## 4. The fresh tape is the thermodynamic resource

Take `N` cells in the product vacuum and let the same local `U_h` interact
with the next unused cell at each tick. Equivalently, a one-pass tape shift
brings a fresh cell to the boundary. After `n<=N` interactions, tracing the
used cells gives exactly `Phi_h^n`; no independence approximation is made.

For every fixed collision horizon `n`, the reduced law is therefore
identical for all `N>=n`. The infinite product tape is a controlled
thermodynamic limit in the local-prefix topology. It replaces K118's supplied
ring wrap by an explicit stream of initialized incoming degrees of freedom.
The initialization and one-pass shift are the resource: the output cells are
not reset for free.

A finite tape reused cyclically does not preserve this result. Used cells are
correlated with the system; feeding them back creates memory and finite-unitary
recurrence. Thus K119 is not a finite closed equilibrium-bath construction.
It gives a Hamiltonian thermodynamic reservoir limit with an explicit boundary
condition.

## 5. The reservoir records activity and affinity

At stationarity, the probability that one cell leaves with directed label
`j<-i` is

```text
Pr(j<-i)=h nu_i q_ij.                                      (11)
```

The expected number of nonvacuum output labels per unit scaled time is the
stationary jump activity

```text
A=sum_i nu_i q_i=83387296/70931795.                         (12)
```

Comparing every output label with its reversed label gives

```text
sum_(i!=j) nu_i q_ij log[(nu_i q_ij)/(nu_j q_ji)]
 = 0.25863366222968864... .                                (13)
```

Equation (13) is exactly K117--K118's projected entropy-production rate.
The tape therefore exports the activity and forward/reverse likelihood
as physical record labels of the repository model. This does not make the
incoming pure cells free, thermal, source-selected, or uniquely physical.

## 6. A finite collision-slab BV-BFV owner

On one collision interval `[0,h]`, let `Psi` be the joint system-cell vector
and use the first-order action

```text
S_h[Psi]=integral_0^h [(i/2)(<Psi,dot Psi>-<dot Psi,Psi>)
                       -<Psi,H_h Psi>] dt.                 (14)
```

Its variation gives `i dot Psi=H_h Psi` and the endpoint canonical one-form.
The induced real symplectic form is preserved by (6), so the input and output
boundary data are joined by a canonical relation. The minimal shifted
cotangent BV extension adds degree-minus-one antifields. Because the model has
no gauge symmetry and the action is antifield-independent, the classical
master equation is trivial and

```text
i_Q Omega_BV=delta S_h-rho*alpha_boundary.                 (15)
```

This is an owned nongauge BV-BFV action for each finite local collision slab.
It is not a relativistic continuum field theory, not K118's Klein-Gordon
cylinder, and not a nontrivial ghost or BRST complex.

## 7. Composition boundary

K119 closes the exact microscopic-dilation seam left by the supplied K95
GKSL and K99 Davies controls: one explicit local Hamiltonian family, one
fresh-tape limit, and one output accounting now yield K115's generator. It
also improves K118's replenishment boundary by locating the resource in
fresh incoming cells rather than a modular ring wrap.

It does not close the common-host seam. No theorem identifies the tape limit
with a relativistic chiral field or couples it to K118's real Klein-Gordon
field on one Sobolev/microlocal domain. The tape vacuum, shift, partial trace,
diagonal classical algebra, and state-effect meaning remain supplied
repository choices. No source/GU action or physical measurement follows.

## Inline postflight bookend

- **Strongest overclaim:** “The Hamiltonian action directly derives the K115
  stochastic law.” Refused. It derives a unitary collision. Fresh-cell
  preparation, reduction and the collision limit are separate owners.
- **Strongest contrary construction:** a finite closed Hamiltonian reservoir
  can mimic a fixed prefix. It cannot provide an indefinitely fresh prefix;
  reuse returns correlations and recurrence. K119 claims only the controlled
  thermodynamic limit.
- **Strongest mistyping risk:** calling the tape a discretization of K118's
  Klein-Gordon field. Refused. No relativistic dispersion, Sobolev-domain
  convergence, microlocal state or common BV-BFV limit is proved.
- **Weakest reproducibility seam:** the star Hamiltonian uses square roots and
  angles. The certificate checks their normalization through exact rational
  squared amplitudes, then separately checks floating matrix evolution only
  as a redundant product-limit control.

The certificate runs a clean exact baseline before every hostile mutation.
No source/GU action, finite closed equilibrium bath, relativistic continuum
limit, nontrivial gauge BV theory, AQFT/Hadamard state, derived Born rule,
held-out score, prediction, confirmation, canon, paper, release or public-
posture surface moves.

## Reproduction

```bash
python3 tests/channel-swings/k119_k118_collision_hamiltonian_thermodynamic_reservoir_probe.py
python3 tests/channel-swings/k119_k118_collision_hamiltonian_thermodynamic_reservoir_probe.py --selftest
```
