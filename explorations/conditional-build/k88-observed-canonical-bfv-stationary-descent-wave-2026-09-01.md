---
title: "K88 observed canonical BFV stationary descent wave"
status: active_research
doc_type: reverse_scaffold_canonical_bfv_stationary_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact repository-owned finite canonical abelian BFV completion for the full K960 plus W960 phase carrier, exact polynomial H0 and exact quotient-only stationary selector with gauge-fixing independence; no source action, functional continuum BV-BFV, unbounded Green domain, physical GU Hilbert space, Hadamard state, Born rule, prediction, confirmation, or verdict
manifest: lab/process/k88-observed-canonical-bfv-stationary-descent-wave.json
probe: tests/channel-swings/k88_observed_canonical_bfv_stationary_descent_probe.py
---

# K88 observed canonical BFV stationary descent wave

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
result: exact finite canonical abelian BFV completion, degree-zero polynomial cohomology and quotient-only stationary selector for the repository-owned K77/K85/K86/K87 candidate
carrier: cotangent phase carrier of K960 direct-sum W960 plus one ghost-antighost pair per K label LAYER=observed CHIRALITY=N/A
pairing: canonical even symplectic form and the minimal BFV odd differential ON=repository_owned_full_phase_control
real_structure: real canonical carrier and real polynomial BFV algebra
grading: BFV ghost number with c degree plus one and b degree minus one
action_owner: repository-construction
target: full constrained carrier to physical H0 and stationary complex structure MAP-TYPE=quotient
```

## Result first

K87 stated the descent conditions but left the BFV owner abstract. The
smallest canonical completion of the K85/K86 carrier makes the outcome exact.
For each of the 960 internal labels split configuration variables as
`q=(q_K,q_W)` with momenta `p=(p_K,p_W)`, and impose the abelian first-class
constraint

```text
G_a = p_K,a = 0.                                             (1)
```

The repository-owned quadratic action is independent of `q_K` and has the
positive frequency-two oscillator on `W`. Add odd ghosts `c^a` and their odd
momenta `b_a`. The minimal classical BFV charge and differential are

```text
Q = sum_a c^a p_K,a,
s q_K,a = c^a,   s b_a = p_K,a,   s p_K,a = s c^a = 0.      (2)
```

The constraints commute, so `{Q,Q}=0`. The pairs `(q_K,c)` and `(b,p_K)` are
contractible. Therefore

```text
H^0_s = R[q_W,p_W],                                         (3)
```

the polynomial observables on `W960 direct-sum W960`. The exact probe builds
the ghost-graded differential matrices through total polynomial degree three:
both adjacent squares vanish and the computed degree-zero cohomology has the
ten monomials of degree at most three in the two physical variables, exactly
the expected truncation of (3).

## The selector exists after, not before, reduction

On one internal label the full stationary generator, in order
`(q_K,q_W,p_K,p_W)`, is

```text
A_full = diag(0, A_W, 0),      A_W = [ 0  1 ].              (4)
                                         [-4  0 ]
```

Both gauge directions are zero modes. Consequently `-A_full^2` has rank two,
so the K87 inverse square root does not exist on the full four-dimensional
carrier. On BFV cohomology the induced generator is `A_W`, and

```text
J_W = -A_W(-A_W^2)^(-1/2) = [0  -1/2],
                                  [2   0  ],
g_W = omega_W J_W = diag(2,1/2).                            (5)
```

Thus `J_W^2=-1`, `[J_W,A_W]=0`, and the majorant is positive. Introducing a
positive gauge-fixing oscillator makes an ambient selector available, but its
gauge block depends on the chosen gauge frequency. Frequencies one and three
give different ambient complex structures and the same projection (5).
Gauge fixing selects a representative on the contractible sector; it does
not change the physical cohomology selector.

The full finite carrier is a closed common algebraic domain. That sentence is
finite-dimensional: it does not establish closed range, an unbounded Green
operator, boundary traces, microlocal spectrum or a functional continuum
BV--BFV theory.

## Hostile review and boundary

The strongest overclaim would call (2)--(5) the source GU quantum physical
complex. It is a repository-owned finite canonical completion of the earlier
reverse-scaffold candidate. The strongest contrary control is the result
itself: the spectral polar formula is undefined on the ambient gauge zero
modes. A nonnilpotent mutation `s b=p_K+q_K` gives `s^2 b=c`; a physical
gauge-fixing leak makes the cohomology selector depend on the gauge frequency.
The weakest remaining seam is the passage from finite polynomial cohomology
to a functional constrained field theory on one common Green domain.

The probe passes `24/24`; its hostile selftest catches `16/16` mutations. No
source action, continuum BV--BFV, physical GU Hilbert space, Hadamard state,
Born law, prediction, confirmation, canon or public posture moves.

## Next condition

Supply the source-owned full action and stationary background, then construct
its functional constraint complex and one common closed Green domain. Test
whether the induced physical generator remains positive and gapped and
whether its spectral selector descends without a gauge-fixing or anomaly
dependence.
