---
title: "K118 K117 finite controller and continuum BV-BFV host boundary"
status: active_research
doc_type: conditional_finite_controller_continuum_bv_bfv_host_result
created: 2026-09-03
date: 2026-09-03
claim_ceiling: exact repository-owned finite nonequilibrium cyclic controller with explicit winding replenishment, finite-fuel finite-window limit and genuine free nongauge continuum Klein-Gordon BV-BFV host only; the ring is not a closed equilibrium bath, the free host is not coupled to K115 and is not Weinstein's source or a GU action, and no interacting gauge theory, AQFT state, Born rule, prediction or confirmation follows
manifest: lab/process/k118-k117-finite-controller-continuum-bv-bfv-host-wave.json
probe: tests/channel-swings/k118_k117_finite_controller_continuum_bv_bfv_host_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K118 K117 finite controller and continuum BV-BFV host boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet answers both exact reopeners left by K117, but does not
quietly join them. It replaces the unbounded work coordinate by a finite
cyclic nonequilibrium controller whose wrap cut explicitly records
replenishment, constructs a finite-fuel open-chain approximation with a
controlled finite-window limit, and replaces the finite causal DAG by a
genuine free nongauge continuum BV-BFV host. The finite controller remains
driven, and no detector-field or source/GU coupling is constructed.

```gu-typed-objects
result: a finite cyclic controller strongly lumps exactly to K115 with positive winding replenishment; bounded fuel converges on finite windows to K117; and a free Klein-Gordon field on a Lorentzian cylinder has Cauchy traces, boundary symplectic flux, an odd bulk BV form, classical master equation and causal Peierls support
carrier: the K115 finite base-record chain times a finite fuel ring or bounded fuel interval, plus the Sobolev real scalar field space on a globally hyperbolic Lorentzian cylinder LAYER=observed CHIRALITY=N/A
pairing: stationary Markov flux and log-rate-ratio pairing for the controller; bulk L2 BV cotangent pairing and boundary Cauchy symplectic pairing for the continuum host ON=repository_finite_controller_and_free_continuum_host
real_structure: real finite-state probabilities and resource steps; real Klein-Gordon fields, momenta and antifields
grading: degree-zero stochastic controller; BV field degree zero and antifield degree minus one; no nontrivial ghost or BRST grading
action_owner: repository-construction -- K115 rates plus a supplied cyclic affinity, and a separate free Klein-Gordon action; not Weinstein's source action, a GU action or a coupled detector-field action
target: finite replenishment and thermodynamic-limit ownership plus continuum causal BV-BFV hosting boundary MAP-TYPE=evaluation
```

## Inline preflight bookend

K117 proved that a finite detailed-balanced strongly lumpable lift is
impossible, not that every finite hidden controller is impossible. The route
census therefore separated a finite nonequilibrium ring, a bounded fuel
register, a chemical chemostat, a Hamiltonian bath, and a source-owned action.
The finite ring is the cheapest exact discriminator: it either strongly lumps
to K115 with an explicit winding current or it does not. Its open-chain cover
then distinguishes finite-time approximation from stationary operation.

For the locality arc, the live routes were a free hyperbolic host, abelian BF,
a nontrivial gauge BV theory, or a direct GU coupling. The free real
Klein-Gordon field is selected because it already has an action, a normally
hyperbolic Euler operator, controlled Cauchy traces, boundary symplectic flux
and causal Green support. Its BV extension is honest but minimal: because
there is no gauge symmetry, the antifield-independent action satisfies the
classical master equation trivially and there is no ghost cohomology to claim.
The strongest rejected route is to invent a GU detector-field coupling; no
source object owns one.

The cheapest controller kill is failure of exact strong lumpability or lifted
stationarity. The cheapest continuum kill is failure of Green's identity,
symplectic Cauchy evolution or the master-equation typing. The strongest
contrary construction is a finite Hamiltonian reservoir plus recurrence and a
controlled thermodynamic limit; it remains open and would supersede the
supplied cyclic affinity.

## 1. Finite cyclic controller

Retain K117's exact control on `x,r in Z/3`, with base rate `kappa=2/5`,
record-refresh rate `lambda=7/11`, and

```text
p_x(r)=81/113 when r=x, and 16/113 otherwise.          (1)
```

Define the integer work step on a base edge by

```text
s(x,y;r)=+1 if p_x(r)/p_y(r)=81/16,
         -1 if p_x(r)/p_y(r)=16/81,
          0 otherwise.                                 (2)
```

Take an odd ring `C_L=Z/L`, here certified at `L=5`. A base jump lifts as

```text
(x,r,z) -> (y,r,z+s(x,y;r)) mod L                      (3)
```

at the unchanged base rate. A record jump leaves `z` fixed and retains the
K115 rate. Summing rates over every fibre gives K115 independently of `z`, so
the finite lift is strongly lumpable and its projection is exactly K115 for
all times. If `nu(x,r)` is K115's stationary law, then
`mu(x,r,z)=nu(x,r)/L` is stationary. The lift is finite, autonomous and
time-homogeneous.

This construction escapes K117's no-go by dropping detailed balance, not by
invalidating it. The lifted four-edge cycle still has ratio `256/6561`.
The controller is a finite stationary nonequilibrium Markov chain.

## 2. Winding is explicit replenishment

Cut the ring between `L-1` and `0`. Count a positive crossing for a `+1` work
step through that cut and a negative crossing for the reverse. Translation
invariance of the stationary lift gives

```text
L J_cut = J_step,
L log(81/16) J_cut = J_W,                               (4)
```

where `J_step` is the stationary signed work-step rate and `J_W` is K117's
positive mean work rate. The lifted edge entropy production equals K115's
projected entropy production exactly: every lifted edge has the same flux
ratio as its coarse edge and the `L` uniform copies cancel the factor `1/L`.

Equation (4) is why the finite ring is not a free finite bath. Each wrap takes
spent resource back to the replenished end. The maintained nonconservative
rate affinity supplies that reset. The wrap is now visible and countable, but
its physical chemical, Hamiltonian or source owner is not derived.

## 3. Bounded fuel and the thermodynamic limit

Replace the ring by `z in {-N,...,N}` and suppress a base jump only when its
work step would leave the interval. Away from the two boundary faces, the
lift is exactly K117. Starting from `z=0`, a boundary attempt requires more
than `N` jumps. Uniformize the complete K115 chain at

```text
Lambda = 2 kappa + lambda (1-16/113)
       = 4/5 + 679/1243.                               (5)
```

For every observation horizon `T`, coupling the bounded and unbounded lifts
by the same uniformized jump proposals gives

```text
d_TV(path laws through T)
  <= Pr[Poisson(Lambda T)>N] -> 0 as N->infinity.       (6)
```

Thus a finite fuel register reproduces K117 on every fixed finite window in a
controlled limit. It does not reproduce stationary K115 exactly at finite
`N`: outward rates are missing on the boundary. More decisively, every
stationary law on a bounded coordinate has mean generator drift of `z` equal
to zero, while K117 has strictly positive mean work. Finite fuel either runs
down, distorts the coarse law at its boundary, or must be replenished.

## 4. A genuine continuum free BV-BFV host

Let `M=[0,T] x S^1` carry metric `dt^2-dx^2` and let `phi` be a real scalar.
On a Sobolev `H^2` domain use

```text
S[phi]=1/2 integral_M ((partial_t phi)^2-(partial_x phi)^2-m^2 phi^2),
P phi=(partial_t^2-partial_x^2+m^2)phi.                 (7)
```

The Cauchy trace is

```text
rho(phi)=(phi|_Sigma, normal_partial phi|_Sigma)
  in H^(3/2)(S^1) x H^(1/2)(S^1).                     (8)
```

Variation of (7) gives the bulk Euler term and the signed boundary one-form

```text
alpha_boundary = integral_SigmaT pi delta phi
                 - integral_Sigma0 pi delta phi,
omega_boundary=delta alpha_boundary.                  (9)
```

Green's identity makes the symplectic flux equal on the two Cauchy
components for solutions. Modewise Cauchy evolution is the usual symplectic
oscillator matrix with determinant one; the exact probe checks Green's
identity on polynomial test functions and an exact quarter-period mode.

The minimal BV extension is the shifted cotangent bundle with antifield
`phi+` of degree `-1` and odd form

```text
Omega_BV=integral_M delta phi+ wedge delta phi.        (10)
```

Set `S_BV=S[phi]`. Since it is independent of `phi+`, its BV antibracket with
itself is zero, so the classical master equation holds. This is a genuine
continuum *nongauge* BV-BFV host. With `Q phi=0` and
`Q phi+=-P phi`, the sign convention used above gives the compatibility
identity

```text
i_Q Omega_BV = delta S_BV - rho* alpha_boundary.       (11)
```

The boundary cohomological vector field and BFV charge are zero. Thus the
trace map, boundary phase space, bulk odd form and action are actually tied by
the BV-BFV identity, but the master equation is trivial and no ghosts, gauge
quotient or nontrivial BV cohomology have been constructed.

Because `P` is normally hyperbolic on the globally hyperbolic cylinder, its
retarded and advanced Green maps have causal support. Hence the causal
propagator pairs spacelike-separated compactly supported linear observables
to zero. This replaces K117's finite-DAG locality precursor by a continuum
causal host theorem, not by a coupled detector field theory or AQFT state.

## 5. Composition boundary

The two constructions coexist but do not interact. No term in (7) depends on
the detector or fuel coordinate, and no transition rate in (3) is derived by
varying (7). Therefore K118 supplies neither a continuum action owner for the
finite controller nor a finite controller for the continuum field.

The exact next object is one owned local interaction whose BV-BFV variation
produces the detector/controller rates, or a controlled scaling law with the
same coarse generator, while also owning the reservoirs that maintain the
ring affinity. Without that bridge, the free host earns continuum locality
and domain credit only; it earns no GU-native derivation, physical
measurement, Born, prediction or confirmation credit.

## Inline postflight bookend

- **Strongest overclaim:** “A finite controller removes K117's thermodynamic
  cost.” Refused. It relocates cost to the explicit winding/replenishment cut.
- **Strongest contrary construction:** a finite closed Hamiltonian reservoir
  can approximate driven behavior before recurrence. K118's bounded-fuel
  estimate permits that finite-window route and denies it stationary exact
  K115 credit without a replenishing limit.
- **Strongest mistyping risk:** calling the free scalar host a GU BV-BFV
  theory. Refused. It is a separate nongauge continuum comparator with a
  trivial master equation and no detector coupling.
- **Weakest reproducibility seam:** finite-state stationarity can hide winding
  when the resource coordinate is read modulo `L`. The certificate audits a
  named cut and proves the factor-`L` current identity before accepting the
  finite controller.

The certificate runs a clean exact baseline before every hostile mutation. No
source/GU action, closed equilibrium bath, interacting gauge BV theory, AQFT
state, Born derivation, held-out score, prediction, confirmation, canon,
paper, release or public-posture surface moves.

## Reproduction

```bash
python3 tests/channel-swings/k118_k117_finite_controller_continuum_bv_bfv_host_probe.py
python3 tests/channel-swings/k118_k117_finite_controller_continuum_bv_bfv_host_probe.py --selftest
```
