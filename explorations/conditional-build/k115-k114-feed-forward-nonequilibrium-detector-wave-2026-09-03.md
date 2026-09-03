---
title: "K115 K114 feed-forward nonequilibrium detector and autonomous-base boundary"
status: active_research
doc_type: conditional_feed_forward_diffusion_refresh_detector_result
created: 2026-09-03
date: 2026-09-03
claim_ceiling: exact finite-dimensional feed-forward diffusion-refresh, autonomous-base, stationary-resolvent, finite-energy record, nonequilibrium-current and response-lag theorem on the K113/K114 carrier; the one-way detector avoids K114's reversible record-conditioned drift backreaction, but its kernel, clock and preparation remain supplied; finite contrast retains error and finite clock rate produces stationary lag; no source/GU physical environment, thermodynamic derivation, spacetime causal BV-BFV descent, Born derivation, prediction or confirmation follows
manifest: lab/process/k115-k114-feed-forward-nonequilibrium-detector-wave.json
probe: tests/channel-swings/k115_k114_feed_forward_nonequilibrium_detector_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K115 K114 feed-forward nonequilibrium detector and autonomous-base boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet constructs the one-way finite-dimensional detector left
open by K114. It preserves K113's base diffusion exactly, derives the joint
stationary law through the base resolvent, proves finite record energy and
shows that informative feed-forward readout is necessarily nonequilibrium.
It does not authenticate a physical bath, clock, apparatus, preparation or
source action and does not construct a spacetime stochastic field theory.

```gu-typed-objects
result: one S_256-equivariant Poisson-refresh detector reads the unchanged K113 base process without record-conditioned drift backreaction; its stationary conditional record is the resolvent-smoothed event kernel, sharp detector indicators have bounded energy, informative readout carries nonzero stationary currents, finite score contrast leaves error and finite clock rate leaves lag
carrier: K111 closed normalized nonnegative weight simplex Delta_255 times a finite 256-state detector coordinate LAYER=observed CHIRALITY=N/A
pairing: K113 classical Gibbs law mu on the simplex, counting measure on detector labels and the stationary conditional densities h_r=lambda(lambda-A)^-1 p_r; inherited K105 lowerer appears only after record-center evaluation ON=repository_feed_forward_detector_control
real_structure: real simplex coordinates, real reflected diffusion, positive real readout kernel and real classical Poisson refresh process
grading: degree-zero classical diffusion-refresh process and detector center, with inherited minimal K91 BRST grading only after conditional branch transport
action_owner: repository-construction -- unchanged K113 generator plus supplied readout kernel and independent Poisson clock; not authenticated as Weinstein's source action, a physical bath or a thermodynamic apparatus
target: exact base autonomy, stationary resolvent, finite-energy record, nonequilibrium current and response-lag boundary MAP-TYPE=evaluation
```

## Inline preflight bookend

K114 proves that an informative reversible score detector changes the
record-conditioned K113 drift. Its strongest open contrary route is one-way:
let the base evolve autonomously and allow information to flow only from the
base into a detector refresh. The cheapest decisive condition is literal
generator autonomy. A construction that merely preserves the unconditional
base marginal, as K114 does for affine scores, does not pass.

The route census separated absorbing memory, a discontinuous `argmax` slave,
K114's reversible score coupling, feed-forward refresh, a doubled-clock
apparatus and a field-theoretic detector. Absorption assumes permanence;
`argmax` repeats K113's wall singularity; the reversible route is already
closed; the doubled clock adds no needed mathematics; and the spacetime route
lacks an owned action and domain. Feed-forward refresh is selected because it
makes autonomy, stationarity, finite energy and nonequilibrium exact in one
minimal carrier while keeping every physical owner visible.

## 1. Feed-forward generator and exact autonomy

Let `A` be K113's conservative, irreducible, self-adjoint reflected diffusion
generator on the closed simplex `Delta`, with invariant Gibbs probability
`mu`. Retain K114's positive equivariant scores and normalize them:

```text
a_r(w)=(epsilon+w_r)^m,
p_r(w)=a_r(w)/sum_s a_s(w),
epsilon>0, m>=1.                                         (1)
```

At the event times of an independent Poisson clock of rate `lambda>0`, erase
the prior detector value and sample a new value from `p(w)`. Between refreshes
the detector is constant. The generator on
`Omega=Delta x {0,...,255}` is

```text
Gf(w,r)=A[f_r](w)
       +lambda(sum_s p_s(w)f(w,s)-f(w,r)).                (2)
```

For every base observable `g(w)`, equation (2) gives

```text
G(g circ pr_W)(w,r)=Ag(w).                               (3)
```

This is stronger than preservation of one stationary marginal: the complete
base path law is K113's for every detector preparation. No record-conditioned
logarithmic score appears in the drift. Simultaneous permutation of base
coordinates and detector labels preserves (1)--(2), so the law is
`S_256`-equivariant.

The clock and sampling kernel are imported. Equation (2) does not say what
physical apparatus erases, samples or stores the record, nor what energy or
entropy budget pays for that operation.

## 2. Exact stationary law is a resolvent-smoothed record

Write the stationary joint law as

```text
nu(dw,r)=mu(dw) h_r(w).                                  (4)
```

Because `A` is self-adjoint in `L2(mu)`, the stationary forward equation is

```text
A h_r+lambda(p_r-h_r)=0,
(lambda-A)h_r=lambda p_r.                                (5)
```

Therefore

```text
h_r=lambda(lambda-A)^(-1)p_r.                            (6)
```

The Markov resolvent preserves positivity and constants. Hence

```text
sum_r h_r=1,
min_Delta p_r <= h_r <= max_Delta p_r.                   (7)
```

Summing (4) over `r` gives exactly `mu`; the detector does not reweight the
K113 base Gibbs law. Equivariance and transitivity give

```text
nu(R=r)=1/256.                                            (8)
```

K113 irreducibility plus the strictly positive refresh kernel make (4)--(6)
the unique stationary law. The record conditional at a stationary observation
time is `h`, not the instantaneous event kernel `p`: the detector contains a
finite response lag because the base can move between refreshes.

## 3. Sharp detector records remain finite-energy

For a fixed label `j`, let

```text
g_j(w,r)=1 if r=j, and 0 otherwise.                       (9)
```

It has zero continuous gradient and

```text
Gg_j=lambda(p_j-1_{r=j}).                               (10)
```

Thus `Gg_j` is bounded in absolute value by `lambda`. Its carré du champ is

```text
Gamma(g_j)(w,r)
 =lambda/2 * {1-p_j(w), r=j; p_j(w), r!=j},              (11)
```

so `0<=Gamma(g_j)<=lambda/2`. The sharp record is in the finite joint
generator/energy domain. A continuous crossing of any base tie wall cannot
change `R`; only a Poisson refresh can. The refresh may return the same label,
so the actual label-change rate is
`lambda(1-p_r(w))<=lambda`. The record is durable between refreshes but is not
an absorbing or permanent branch.

## 4. Informative feed-forward readout is nonequilibrium

Suppose the joint law were reversible. Detailed balance for detector refresh
edges at fixed `w` would require

```text
h_r(w)p_s(w)=h_s(w)p_r(w) for all r,s.                   (12)
```

Strict positivity and normalization force `h=p`. Substitution in (5) gives
`A p_r=0` for every `r`. K113 irreducibility makes every bounded harmonic
`p_r` constant. Hence any informative, state-dependent readout kernel violates
joint reversibility.

The exact three-state complete-graph control in the certificate makes the
currents explicit. For base jump rate `kappa`, the centered modes have
eigenvalue `-3kappa`, so

```text
h_r=1/3+[lambda/(lambda+3kappa)](p_r-1/3).               (13)
```

At finite positive `lambda` and `kappa`, both base-sector current and refresh
current are nonzero and their divergences cancel in stationarity. This closes
K114's mathematical one-way escape: informative readout can avoid
record-conditioned drift backreaction, but only by leaving equilibrium.

It does not derive a physical entropy-production rate. Thermodynamic meaning
requires an owned bath, clock, reset implementation and fluctuation relation;
the Markov current alone is a structural nonequilibrium certificate.

## 5. Event accuracy and stationary lag are different controls

At a K111 vacuum `w^(j)`, with `epsilon=1/257`, the event-time kernel is still

```text
p_j(w^(j))=3^m/(3^m+255*2^m),                            (14)
p_s(w^(j))=2^m/(3^m+255*2^m), s!=j.                     (15)
```

Every finite `m` leaves nonzero event-time error. The clock `lambda` does not
change (14)--(15); it changes how quickly the stationary record tracks them.
Let `E_A(u,u)=-<u,Au>_mu` be the K113 base Dirichlet form. Spectral calculus
for nonnegative `-A` gives the exact bound

```text
||h_r-p_r||^2_L2(mu) <= E_A(p_r,p_r)/lambda.             (16)
```

Thus `h_r -> p_r` in `L2(mu)` as `lambda -> infinity`. On centered modes,
`lambda(lambda-A)^-1 -> 0` as `lambda -> 0`; the stationary record then tends
to its orbit-symmetric marginal `1/256`. Fast refresh reduces lag but does not
remove finite score error. Increasing score contrast reduces event error but
does not source-own the kernel or turn classical conditioning into Born
structure.

## 6. Branch interface and remaining physical invoice

After a refresh returns `R=r`, center evaluation names K110's `P_r` and the
corresponding K91 action/domain/Green retract. That name persists through base
tie-wall crossings and changes only at a later refresh. It is still a
classical external center, not a local spacetime observable derived from a GU
field algebra.

The remaining invoice is now sharper. A physical successor must own:

1. a source/action coupling whose reduction gives the one-way kernel (1)--(2);
2. a bath and reset clock with a declared preparation and dissipation law;
3. a genuine spacetime causal BV-BFV domain and boundary trace;
4. local detector-observable descent compatible with that domain; and
5. state/probability ownership before any Born, measurement or prediction
   claim.

K115 supplies none of those owners. It shows only that the finite-dimensional
nonbackreacting detector is mathematically coherent and necessarily driven.

## Inline postflight bookend

- **Strongest overclaim:** “K115 derives a non-invasive physical
  measurement.” Refused. It derives autonomy only after supplying a classical
  readout kernel and erasing Poisson refresh.
- **Strongest contrary construction:** a source-owned unitary detector or
  autonomous field apparatus could realize the same operational map without
  fundamental reset. That is not excluded; it must produce the kernel, clock,
  preparation, bath and causal domain rather than inherit them.
- **Strongest mistyping risk:** identifying event-time `p` with stationary
  conditional `h`. Refused. They differ by the resolvent lag at every finite
  clock rate for an informative kernel.
- **Weakest reproducibility seam:** a simulation can hide nonzero stationary
  currents or mistake a large clock for zero lag. The exact three-state control
  checks the stationary equation, both currents and the rational attenuation
  before any numerical interpretation.

The certificate runs a clean exact baseline before every hostile mutation.
No source/GU stochastic action, physical environment, measurement or collapse,
thermodynamic derivation, spacetime causal BV-BFV quotient, Born derivation,
held-out score, prediction, confirmation, canon, paper or public posture moves.

## Reproduction

```bash
python3 tests/channel-swings/k115_k114_feed_forward_nonequilibrium_detector_probe.py
python3 tests/channel-swings/k115_k114_feed_forward_nonequilibrium_detector_probe.py --selftest
```
