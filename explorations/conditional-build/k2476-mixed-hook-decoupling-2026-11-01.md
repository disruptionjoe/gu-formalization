---
title: "K2476 Ordinary-first hook inverse and analytic reduction"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "sufficient linear estimates and equivalence only; general analytic and nonlinear existence remain open"
---

# K2476 Ordinary-first hook inverse and analytic reduction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2476
carrier: original fourteen-coordinate repeated-polar hook bank and original E=0 boundary ideal LAYER=toy CHIRALITY=N/A
pairing: summed coefficient l1 norm in fixed adapted coordinates ON=declared_carrier
real_structure: fixed real embedding of Q(sqrt2); complex coefficients allowed for analytic estimates
grading: homogeneous field, receiver, transverse and passive polynomial degree
action_owner: repository-construction -- supplied conditional mathematical models
target: Original joint ordinary-scalar linear inversion MAP-TYPE=evaluation
```

## Result and exact scope

The full scalar inverse of [K2470](k2470-mixed-hook-syzygies-2026-11-01.md)
allows the scalar equation to be corrected **once**, after solving the ordinary
mixed equation. Scalar mixed transfers therefore need not occur in the ordinary
recurrence. This yields an ordinary inverse with sufficient coefficient bound

    ||O_d|| <= b^(d-1) d! C^[d(d+1)/2], d>=4.             (1)

Here C>=1 and b=max(1,B)>=1 are fixed existence constants in one fixed adapted
coordinate norm. Compared using a common enlarged C, the sufficient borderline
forcing class improves from K2473's factorial power three to power one.
This is an upper bound on a constructed inverse, not a necessary growth rate.
General analytic ordinary inversion remains open. Joint analytic solvability
is equivalent to ordinary analytic solvability as germs in the original
boundary-preserving field class. Nonlinear convergence does not follow.

These are conditional original-hook results, not native GU solutions.
SC-ACT-01/06 and SC-GEO-55 remain ASSERTS, SC-META-53 remains UNCERTAIN;
source polarities, ledger0.263 and canon remain unchanged.

## 1. Exact splitting removes an entire repeated correction

Write D=D_E+D_W for the actual ordinary first-order constant-coefficient Euler
map, and J_d=(4/d)Jstar for the original scalar map on degree-d fields.
K2449's generators depend on transverse E coordinates; passive W monomials
are parameters for the transverse solver. K2446 section1 explicitly gives
K2443's actual-field ordinary inverse R_k with ||R_k||<=C^(k+1), preserving each
passive monomial. Its later factor d is introduced to invert the augmented
scalar normalization; it is not part of this ordinary estimate. Off-range
projections, if used as bookkeeping, act separately at each W monomial.

K2455's compatibility induction uses ordinary trace/double-divergence alone:
subtracting an actual D-field preserves those identities, and after larger
passive degrees vanish the next residual obeys the true transverse identities.
Thus the ordinary recurrence uses R_k only on its actual compatible range.
Arbitrary incompatible ordinary forcing is excluded. Every correction retains
the repeated-polar and E=0 boundary restrictions of the inherited bank.

Let S_d be K2470's full scalar inverse: D S_d=0, J_d S_d=id, in that same
allowed field space. Then for compatible Q and arbitrary g,

    V=O_d Q+S_d(g-J_d O_d Q),
    D V=Q,                    J_d V=g.                  (2)

No scalar EW/WW transfer is needed in O_d. A transverse-only scalar kernel
would not suffice; K2470's full ordinary-kernel statement is essential.

## 2. Falling factorial estimate on the original filtration

Put n=d-1. On a receiver block of transverse degree k and passive degree n-k,
R_k raises transverse degree by one and preserves passive degree. D_W is a
fixed first-order passive derivative bank, so on passive degree m its induced
summed-coefficient norm is at most B m. Each transfer raises the receiver
transverse degree by exactly one and lowers passive degree by one.

A j-transfer term, 0<=j<=n-k, is bounded by

    B^j (n-k)!/(n-k-j)!
      * C^[(j+1)(k+1)+j(j+1)/2].                        (3)

There are j+1 transverse inverses at indices k,...,k+j. The norm product
already sums all derivative/generator branches; no additional path count is
required. The exact inverse on compatible residuals is the finite alternating
series sum_j(-R D_W)^j R. Its telescoping identity uses the residual compatibility
above, not merely nilpotence on an arbitrary off-range extension.

The exponent in (3) is <=d(d+1)/2, the falling factorial is <=(d-1)!, and
there are at most d terms. Taking the maximum column sum over initial blocks
proves (1). Constants can be enlarged to one C that also bounds the predecessor
construction. The new constant has no numerical conditioning interpretation.

K2470 gives ||S_d||<=576 d(d+5)^5 210^(d-1) in original equal-coordinate norms.
In the adapted norm a fixed invertible coordinate change gives
||S_d||<=A d^6 L^d for some fixed A,L. Original Jstar has fixed first-order and
linear-coefficient second-order terms, so ||J_d||<=H d. Equation(2) then gives

    ||V|| <= (1+A H d^7 L^d)||O_d Q|| + A d^6 L^d||g||.  (4)

Do not use210 as an adapted-coordinate radius without pricing the actual map.

## 3. Released analytic classes and equivalence

For compatible homogeneous receivers Q_d, suppose

    ||Q_d|| <= M C^[-d(d+1)/2] (d!)^-1 R^-d.

Equation(1) yields ||O_d Q_d||<=M b^(d-1)R^-d, hence an analytic ordinary
solution for adapted radius r<R/b. Its scalar residual and the correction
in(2) remain analytic on a further fixed smaller polydisc, intersected with
the radius for the arbitrary analytic g. Formula(4) gives an explicit
sufficient adapted radius r<R/(b max(1,L)) for the Q-dependent part.
A polynomial d^7 affects the strict radius endpoint, not this radius of
convergence. Factorial power s>1 makes the Q-dependent ordinary solution and
its scalar correction entire. Strict Gaussian forcing A0>log(C)/2 likewise
remains entire. Only the independent g then restricts the scalar domain.

For the germ equivalence, a joint solution for(Q,0) projects to an ordinary
solution. Conversely any analytic ordinary solution in the allowed class has
analytic J V: the degreewise4/d multiplier is bounded for d>=4, and Jstar is a
finite differential operator with polynomial coefficients. Applying S to
(g-JV) proves a joint analytic solution. Finitely many excluded low-degree
components must be supplied separately. This is equivalence of linear
solvability, not a uniform right-inverse estimate for an arbitrary choice of
ordinary solutions. No closure of a nonlinear majorant is established.

## 4. Controls and retained open problem

Finite exact scalar block models test the falling-factorial coefficient and
alternating inverse; exact matrix splitting controls test both equations and
show why an S with D S!=0 fails. These do not constitute fresh original tensor
computations: original K2443/K2446/K2455/K2470 proofs and reports are authenticated
and reused. Written filtration, splitting and coefficient summation establish
the general result. No sampled degree or report hash proves convergence.

The estimate-level model R_k=C^(k+1), D_W e_k=(n-k)e_(k+1) still gives a last
coefficient n! C^[(n+1)(n+2)/2]. It rejects a claim that decoupling alone forces
geometric growth; it is not the original hook operator or its lower bound.
The next substantial question is now solely an original ordinary composed-map
or quotient estimate. Repeated augmented scalar corrections and additional
scalar rank censuses cannot discharge it. Internal review is not external,
proof-assistant or novelty certification.

[Probe](../../tests/channel-swings/k2476_mixed_hook_decoupling_probe.py) and [report](../../lab/process/k2476-mixed-hook-decoupling.json).
