---
title: "K100 observed faithful-thermal record-floor wave"
status: active_research
doc_type: reverse_scaffold_thermal_record_floor_result
created: 2026-09-02
date: 2026-09-02
target_claim: INTERNAL_TARGET:K100_FIXED_FAITHFUL_THERMAL_AUTONOMOUS_RECORD_FLOOR
claim_ceiling: exact fixed-finite faithful-apparatus unitary record floor only; no infinite thermal reservoir, open dynamics, universal work, source, Born, prediction, confirmation, held-out score, promotion or verdict
manifest: lab/process/k100-observed-faithful-thermal-record-floor-wave.json
probe: tests/channel-swings/k100_observed_faithful_thermal_record_floor_probe.py
---

# K100 observed faithful-thermal record-floor wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: faithful finite thermal apparatus exact-record obstruction
carrier: M_d(C) apparatus with faithful density tau and q-conditioned unitary orbits LAYER=observed CHIRALITY=N/A
pairing: imported trace state-effect pairing ON=repository_owned_finite_thermal_control
real_structure: matrix adjoint and occupation-basis conjugation
grading: binary q label and apparatus spectral decomposition; no source BV, BFV or ghost grading
action_owner: repository-construction
target: uniform Helstrom-error lower bound MAP-TYPE=evaluation
```

Scope: this result quantifies a fixed finite-dimensional apparatus initialized
in one faithful positive-temperature state. It includes autonomous
time-independent Hamiltonian branches, but not infinite KMS representations,
nonunitary reservoirs or source dynamics.

## Inline preflight bookend

The route census covered faithful Gibbs states, support projections, Helstrom
discrimination, unitary spectral invariance, autonomous Hamiltonian flow,
finite apparatus capacity, zero-temperature escape and infinite-system
limits. Retrieval found K95 recurrence and K99's growing-stream cost, but no
time-uniform lower bound over every unitary orbit of one faithful apparatus
state. The selected route uses operator order and therefore resolves all
unitaries at once.

## Uniform error floor

Let `tau>0` be a density matrix on `C^d` and put
`m=lambda_min(tau)>0`. For arbitrary branch unitaries `U_i(t)`,

```text
rho_i(t)=U_i(t) tau U_i(t)^* >= m I.                       (1)
```

Let `0<=E_t<=I` be any effect whose outcome one identifies `q=1`. With equal
priors its error is

```text
e_t(E)=1/2[Tr(rho_0(t)E_t)+Tr(rho_1(t)(I-E_t))].           (2)
```

Applying (1) to both positive effects gives

```text
e_t(E) >= (m/2)[Tr(E_t)+Tr(I-E_t)] = d m/2 > 0.            (3)
```

The bound is uniform in time, in the readout effect and in both branch
unitaries. In particular it applies to every pair of autonomous branches
`U_i(t)=exp(-itK_i)`. Hence a fixed faithful finite thermal apparatus cannot
approach an exact projective binary record by closed unitary dynamics, even as
`t` tends to infinity.

For `tau=diag(3/4,1/4)`, `U_0=I` and `U_1=X`, the optimal error is `1/4` and
`d m/2=1/4`; the floor is sharp. This is a formation result. An already
orthogonal record supplied in a nonfaithful state is outside the premise.

## Exact boundary

The obstruction disappears as a statement when `m=0`, as at zero
temperature; when apparatus dimension grows without a positive uniform
`d m` floor; or when branch evolution is nonunitary. Those are live contrary
routes. The theorem does not say that infinite KMS systems cannot carry
records, and it does not quantify the work required by every architecture.

## Owner accounting and maximum conclusion

Repository-owned: equations (1)--(3), the time-uniform Helstrom consequence,
the autonomous subset and the sharp qubit control. Imported: the apparatus
algebra, faithful state, q-conditioned dynamics, effect algebra, equal priors,
trace/Born pairing and record semantics. No source owner is acquired.

The maximum conclusion is exact: fixed finite positive-temperature capacity
cannot close K99's asymptotic record gap under closed unitary dynamics. A
successful exact thermal record must use a growing/infinite carrier, a
nonfaithful or pre-separated sector, or nonunitary/open resources.

## Inline postflight bookend

- Strongest overclaim: extending (3) to infinite type-III KMS systems,
  dissipative channels, nonfaithful vacua or phase-coexistence sectors.
- Strongest contrary construction: at zero temperature `m=0`, and a pure
  ready state can be unitarily mapped into orthogonal branch records.
- Weakest reproducibility seam: finite matrix controls witness sharpness and
  boundary behavior; the universal quantifier is certified by the analytic
  operator inequality, not enumeration.

The exact probe mutation-tests the formula, the autonomous inclusion and all
scope fences. Delayed choice remains reserved and unscored. No source, Born,
prediction, confirmation, canon, paper or hypothesis status moves.

## Next condition

Test whether a growing but finite-work autonomous local reservoir can produce a
record in an asymptotic scattering algebra, or prove which divergent capacity,
free-energy or disjoint-sector resource replaces the fixed-apparatus floor.
