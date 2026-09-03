---
title: "K122 K121 autonomous fermionic-reservoir bulk gauge-net wave"
status: active_research
doc_type: reverse_scaffold_autonomous_fermionic_reservoir_result
created: 2026-09-03
date: 2026-09-03
target_claim: INTERNAL_TARGET:K121_AUTONOMOUS_NONEQUILIBRIUM_FIELD_OWNER_AND_BULK_GAUGE_DESCENT
claim_ceiling: exact repository-owned 18-lead CAR factorization of K115, time-independent autonomous thermodynamic-limit defect Hamiltonian with controlled Davies or white-noise reduction, explicit affinity-resource accounting and free 1+1-dimensional gauge-even reservoir observable net; lead modular data and spectral couplings remain selected, only the free reservoir net is constructed, and no source/GU ownership, finite closed bath, exact finite-time Markov reduction, full interacting AQFT, nontrivial gauge BV, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k122-k121-autonomous-fermionic-reservoir-bulk-gauge-net-wave.json
probe: tests/channel-swings/k122_k121_autonomous_fermionic_reservoir_bulk_gauge_net_probe.py
---

# K122 K121 autonomous fermionic-reservoir bulk gauge-net wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: exact autonomous thermodynamic-limit CAR lead owner of the K115 generator and free bulk gauge-even reservoir net
carrier: nine-state K115 system tensor 18 species of full left-right massless 1+1-dimensional Dirac CAR fields LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: grand-canonical quasifree CAR state, Hilbert/Fock inner product and imported finite-system trace/effect pairing ON=repository_owned_nonequilibrium_field_control
real_structure: CAR adjoint, complex conjugation of spinor test functions and finite-system matrix adjoint
grading: fermion parity and species U(1)^18 charge; no source BV, BFV or ghost grading
action_owner: repository-construction
target: lead modular data, autonomous boundary tunnelling, free bulk observable subnet and K115 reduced dynamics MAP-TYPE=evaluation
```

Scope: this result binds one repository-selected thermodynamic-limit fermionic
lead model of the finite K115 generator. It does not bind Weinstein's action,
a GU-native quantization, a finite closed bath, or the interacting physical
observable net.

## Inline preflight bookend

The rebuilt frontier contained five substantial arcs: derive one CAR lead per
undirected transition; replace K121's externally routed channels by a constant
defect interaction; identify the chemical/thermal resource current; extend the
boundary input through a free bulk gauge quotient; and test whether the
mathematical state/effect tuple gains any physical meaning. These arcs are
compatible and share the exact K115 pair census, so they form one Big Wave.

The primary route is fermionic rather than K121's bosonic thermal/vacuum split.
Fermi occupation is finite at one half, so symmetric pairs and biased pairs
obey one formula. One undirected lead supplies particle and hole processes and
therefore removes external channel switching. A generic fitted Lindbladian was
rejected because it would conceal this owner; a finite repeated-interaction
tape was rejected as already K119 and nonstationary under reuse; direct source-
action invention was rejected by the source gap. The fallback is K121's
declared bosonic multi-reservoir owner if exact CAR factorization fails.

Retrieval found K97's CAR KMS state without record preparation, K99's finite
product-KMS stream and Davies graph, K117's cycle affinity, K119's collision
tape, K120's continuum HP dilation and K121's thermal pair census. The new
content is their all-edge single-pair CAR composition, autonomous defect
owner, exact stationary affinity accounting and gauge-even bulk completion.
The used inputs postdate or respect the applicable canonical corrections; no
superseded source-native reading is consumed.

The route-changing lenses were open quantum systems, CAR/KMS theory,
grand-canonical thermodynamics, stochastic limits, defect field theory,
algebraic QFT, graded locality, gauge observables, BV boundary structure,
source fidelity, state/effect semantics and hostile philosophy of science.
The first kills are failure of exact pair factorization, dependence on a time-
varying switch, unowned reservoir free energy, failure of the entropy identity,
or confusing graded field locality with ordinary observable locality.

## 1. One CAR lead per K115 pair

Let `i <-> j` be one of K121's 18 undirected pairs. Orient the system partial
isometry `V_ji=|j><i|` and write its two target rates as `q_ij,q_ji>0`. Define

```text
kappa_ij = q_ij + q_ji,
f_ij     = q_ji/(q_ij+q_ji).                              (1)
```

One fermionic lead with occupation `f_ij` then supplies the particle/hole
coefficients

```text
kappa_ij(1-f_ij)=q_ij,
kappa_ij f_ij   =q_ji.                                    (2)
```

Equation (2) is an identity, but its uniform application is informative. For
the six asymmetric record pairs,

```text
kappa=679/1243,  f=112/679,  1-f=567/679,
f/(1-f)=16/81.                                            (3)
```

For the nine symmetric base pairs, `kappa=4/5`; for the three symmetric
wrong-record pairs, `kappa=224/1243`. Both classes have `f=1/2`. Thus all 18
pairs use the same finite CAR formula. Each lead has particle and hole noise,
so the stochastic-limit multiplicity is `18*2=36`, matching K120/K121 without
declaring 36 independent switched inputs.

A grand-canonical quasifree lead has

```text
f_e(omega)=1/(1+exp(beta_e(omega-mu_e))).                  (4)
```

At the transition frequency, (3) requires
`beta_e(omega_e-mu_e)=log(81/16)` up to the chosen
orientation; symmetric leads require zero modular offset. Only these modular
combinations are fixed. Neither `beta_e`, `mu_e`, the dispersion nor the
spectral density is separately derived.

## 2. Autonomous defect interaction and controlled reduction

Let `a_e(omega)` be the CAR field of lead `e` and choose a fixed form factor
`g_e`. On the finite system tensored with the 18 infinite leads, take

```text
H = H_S + sum_e H_e
      + lambda sum_e integral d omega [
          g_e(omega) V_e tensor a_e(omega)^*
        + conjugate(g_e(omega)) V_e^* tensor a_e(omega)]. (5)
```

This Hamiltonian is time independent. Every pair coupling is present
continuously; no external clock selects which directed edge is active. In the
Davies/white-noise scaling, the on-shell spectral rate

```text
2 pi |g_e(omega_e)|^2 rho_e(omega_e)=kappa_e             (6)
```

and the quasifree contractions `(1-f_e),f_e` give (2). The diagonal restriction
of the limiting generator is therefore exactly K115 and preserves its inherited
stationary law.

The qualification is essential. Equation (5) is an autonomous microscopic
field Hamiltonian, while exact K115 is the controlled weak-coupling/stochastic
limit of its reduced dynamics. No exact equality at finite `lambda` and finite
time is asserted. The stationary inputs are infinite thermodynamic leads; a
finite closed lead recurs and cannot sustain the same stationary semigroup.

## 3. The work source is the lead modular data

For each oriented pair define its local affinity

```text
A_ij = log(q_ij/q_ji)=log((1-f_ij)/f_ij).                 (7)
```

The twelve symmetric pairs have `A_ij=0`; the six biased pairs have magnitude
`log(81/16)`. If `nu` is K115's stationary law and
`J_ij=nu_i q_ij-nu_j q_ji`, the environmental entropy flow is

```text
sigma_env = sum_{i<j} J_ij A_ij.                          (8)
```

The stationary system-Shannon boundary term telescopes to zero, so (8) equals
the full Schnakenberg expression

```text
sum_{i<j} J_ij log[(nu_i q_ij)/(nu_j q_ji)]
  = 0.25863366222968864... .                              (9)
```

This recovers K117's entropy production and locates K121's hidden work in the
incoming lead modular offsets. It does not make reservoir preparation or the
thermodynamic asymptotic condition free. The product of unequal lead KMS
states is a nonequilibrium resource, not one global equilibrium state.

## 4. Free bulk CAR net and gauge-even observables

Complete each incoming chiral lead by a left/right massless Dirac field on
1+1-dimensional Minkowski spacetime. For a double cone
`O=I_R x I_L`, let `F(O)` be the CAR algebra generated by spinor test functions
supported in its two null intervals. Support inclusion gives isotony and
causal disjointness gives graded locality:

```text
F_1 F_2 = (-1)^(|F_1||F_2|) F_2 F_1.                     (10)
```

The species phase action `U(1)^18` commutes with free propagation. Its even
fixed-point subnet

```text
A(O)=F(O)^(U(1)^18) intersect F(O)_even                  (11)
```

is ordinarily local: observables in spacelike separated double cones commute.
The tensor product of the 18 grand-canonical quasifree states restricts to a
positive normalized state on (11). Folding the right-moving legs at the
defect gives the boundary fields used in (5).

This is a genuine free bulk reservoir observable net and an explicitly local
defect coupling. K122 does not construct the Haag--Kastler net of the fully
interacting defect theory. Nor does taking a fixed-point algebra produce a
nontrivial gauge/ghost BV complex; only a global species-phase quotient is
owned.

## 5. State/effect boundary

For a CAR mode, `N=a^*a` is a projection, hence `0<=N<=1`, and the quasifree
state gives `omega(N)=f in [0,1]`. Tensor products, finite-system spectral
projections and the limiting output counting processes therefore supply a
positive normalized mathematical state/effect tuple. This improves K121's
effect typing: the same CAR algebra owns both occupation and its number
projection.

It does not derive why a physical detector realizes those projections or why
the state-on-effect pairing is nature's probability law. That identification
is still imported. No Born rule follows from positivity alone.

## Inline postflight bookend

- **Strongest overclaim:** calling (5) an exact finite-coupling derivation of
  K115. Refused: exact K115 belongs to the declared Davies/white-noise limit.
- **Strongest hidden resource:** treating time independence as equilibrium.
  Refused: unequal grand-canonical lead states and their infinite asymptotic
  preparation carry the affinity and work.
- **Strongest contrary construction:** a source-owned GU action could select a
  different carrier, modular state, coupling and observable quotient. K122
  neither constructs nor excludes it.
- **Strongest mistyping risk:** promoting the free even CAR reservoir subnet
  into the full interacting physical net. The interacting defect net and
  nontrivial gauge BV reduction remain open.
- **Weakest reproducibility seam:** the certificate verifies finite rate,
  stationarity, affinity and parity/locality identities, not the analytic
  Davies-limit theorem or interacting-net existence. Those are invoked only
  at their standard controlled scope.

All five admitted arcs completed. The result removes external switching,
uniformizes every pair under one CAR formula, identifies the stationary work
source, and extends the reservoir through a free bulk observable net. It still
does not authenticate the selected modular data or couplings from GU.

## Next condition

Replace the selected lead modular offsets and on-shell spectral couplings by
coefficients derived from an actual source-owned GU action. Then construct the
interacting defect net and its physical gauge/BV quotient before testing
detector semantics, Born ownership, prediction or export.

## Reproduction

```bash
python3 tests/channel-swings/k122_k121_autonomous_fermionic_reservoir_bulk_gauge_net_probe.py
python3 tests/channel-swings/k122_k121_autonomous_fermionic_reservoir_bulk_gauge_net_probe.py --selftest
```
