---
title: "K156 common-carrier regular core and exterior-count criterion wave"
status: active_research
doc_type: conditional_common_carrier_renormalized_regular_core_total_action_tail_and_exterior_count_criterion_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned common-carrier and certificate-interface theorem for the equal-coupling two-edge signed hard-core control; K141's normalized momentum cells put K155's cutoffs on one positive Fock carrier, exact normal ordering cancels the logarithmically divergent endpoint counterterm against the vacuum contraction in G_N^*A_NG_N, and a complete propagated graph-relative error controls the regular action on fixed cylinder cores; independently, Schur inertia proves a rank-one exterior-count criterion, but the complete native exterior floor and numerical residual remain absent, so no native count, energy interval, threshold/Gram closure, scattering, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k156-common-carrier-regular-core-exterior-count-criterion-wave.json
solver: tests/channel-swings/k156_common_carrier_regular_core.py
probe: tests/channel-swings/k156_common_carrier_regular_core_exterior_count_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K156 common-carrier regular core and exterior-count criterion wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet joins K155's exact finite regular pullback to K141's common
continuum carrier. It corrects one impossible intermediate demand: the raw
endpoint counterterm does not converge separately. The convergent object is
the normal-ordered renormalized core after exact vacuum-contraction
cancellation. The count branch proves the exact theorem a future native
certificate must satisfy; it does not manufacture its still-missing exterior
lower bound.

```gu-typed-objects
result: common-cylinder identification of the normal-ordered regular representative with a complete propagated graph-relative action tail, plus an exact rank-one exterior-compression spectral-count criterion and a fail-closed native readiness verdict
carrier: the hard-core subspace of the impurity C3 tensor antisymmetric Fock space over L2(R;C4) for the two-edge control, decomposed by q=(q1,q2), with finite circles embedded as normalized momentum-step subspaces and fixed finite-particle cylinder cores LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive exterior-Fock Hilbert pairing; regular cores act from the shifted-free graph domain to Hilbert space, and the singular form is pulled back by the bounded nonunitary K139 chart ON=repository_signed_point_control
real_structure: CAR adjoint and momentum conjugation; endpoint subtraction is Hermitian and the signed exterior flavor permutation intertwines the representative charge blocks before and after the limit
grading: conserved incidence charges q_i=n_i+N_i+-N_i-, finite-particle cylinder degree, cutoff/volume approximation, boundary-word order and trial-line versus complete orthogonal spectral compression
action_owner: repository-construction -- polarization, finite extension, couplings, auxiliary chart, trial state, exterior floor and physical state are not selected by Weinstein's source or a GU action
target: renormalized common-carrier R_256 identification, total regular-action tail and exact exterior-count admission criterion for K154/K152 MAP-TYPE=intertwiner
```

## Inline preflight bookend

K155 requested convergence of `A_N`, `G_N`, `V_N` and
`G_N^*A_NG_N` separately. Mechanism retrieval against K139 and K141 exposes a
necessary correction: for a point form factor, the coefficient of `V_N`
contains a harmonic ultraviolet divergence. K139's theorem has always paired
that term with the vacuum contraction in `G_N^*A_NG_N`; separating their
limits would undo the renormalization.

The route census compared literal coefficient limits, Wick/normal ordering,
boundary triples, norm-resolvent uniqueness, form-core convergence, abstract
cone positivity, Schur inertia, min--max comparison and Lehmann--Goerisch
enclosures. Normal ordering is the only route that both preserves K139's
fixed operator and exposes convergent coefficients. On the count branch,
rank-one Schur inertia isolates the precise complete-complement bound needed
before any numerical enclosure is meaningful.

## 1. The common cylinder carrier is already fixed by K141

Let `delta=2 pi/L` and use K141's isometry

```text
J_delta e_n=delta^(-1/2) 1_[n delta,(n+1)delta)         (1)
```

into `L2(R)`. After adding free spectators, every finite-circle hard-core
charge block is a reducing subspace of one Fock carrier. On the `r`-particle
sector,

```text
|dGamma(omega_delta)-dGamma(omega)|
 <= r delta <= (delta/m)dGamma(omega).                 (2)
```

The dressed point vector

```text
h_(delta,lambda)(p)
 =(2 pi)^(-1/2)(omega_delta(p)+lambda)^(-1)             (3)
```

converges in `L2(R)` to `h_lambda`. Fermionic creation and annihilation by an
`L2` vector are bounded, so the finite boundary maps converge in Hilbert
operator norm. K139's particle/free-graph estimate supplies the graph version.
At `lambda=256`, K153 gives the common Hilbert contraction `q<=3/8`; after the
stated graph enlargement, the graph contraction is also strictly below one.

Thus the finite free-domain cylinder vectors, including `Omega` and
`d_1^*Omega`, live on one carrier, not merely on changing isomorphic spaces.

## 2. The raw counterterm cannot converge separately

On K155's exact cutoff block,

```text
A_N=H0_N+lambda,
G_N=-A_N^-1 C_N^*,
G_N^*A_NG_N=C_N A_N^-1 C_N^*.                          (4)
```

Normal ordering the right side gives

```text
C_N A_N^-1 C_N^*=c_N(lambda)D+X_N,                     (5)
```

where `D=2|0><0|+|1><1|+|2><2|` is the endpoint incidence
and `X_N` is the normal-ordered finite remainder: it includes the diagonal
Pauli/spectator resolvent difference and the four polarity exchange blocks.
The physical finite counterterm is

```text
V_N=c_N(lambda)D+E_R I.                                (6)
```

For a point coefficient,

```text
c_N(lambda)=sum_(|k|<=N)(sqrt(1+k^2)+lambda)^(-1)      (7)
```

diverges logarithmically: for all sufficiently large `k`, its positive
summand is bounded below by a fixed multiple of `1/k`. Therefore `V_N` has no
separate norm or coefficient limit. This is expected subtraction data, not a
failure of K139's operator.

Equations (5)--(6) cancel before the limit:

```text
W_N=V_N-lambda I-G_N^*A_NG_N
   =(E_R-lambda)I-X_N.                                 (8)
```

The companion solver checks (8) entry by entry over exact rationals on K155's
canonical finite charge blocks. It never subtracts two floating divergent
approximations.

## 3. The normal-ordered finite remainder converges

The four exchange blocks in `X_N` contain one free-graph point annihilation
trace and one resolvent-dressed creation vector. K139 proves the first is
bounded from the free graph domain; (3) makes the second an `L2` vector
converging in norm. The diagonal Pauli/spectator remainder is a subtracted
resolvent difference with K141's common `p^-2` tail. Finite edge and polarity
count then gives

```text
||(X_N-X)(H0+a)^-1|| -> 0.                             (9)
```

The same bounds dominate every fixed cylinder coefficient, so (9) is stronger
than entrywise convergence. Higher bidirected words do not add a new
ultraviolet problem: each adds a boundary map and is dominated by K139's
common geometric majorant. Hence (8) identifies

```text
W=(E_R-lambda)I-X                                      (10)
```

as the coefficient-complete normal-ordered regular core. Signed flavor swap
intertwines `A_N,G_N,X_N,W_N` and passes to the norm limits, transporting
`q=(1,0)` to `q=(0,1)`.

## 4. A complete propagated regular-action tail

Put `S_N=(1-G_N)^-1`, `S=(1-G)^-1`. Let

```text
d_A,N = ||(A_N-A)(H0+a)^-1||,
d_G,N = ||G_N-G||,
d_GD,N= ||G_N-G||_(D->D),
d_W,N = ||(W_N-W)(H0+a)^-1||.                          (11)
```

Assume the already-proved uniform bounds

```text
||G_N||,||G||<=q_H<1,
||G_N||_(D->D),||G||_(D->D)<=q_D<1,
||W_N||_(D->H),||W||_(D->H)<=B.                        (12)
```

With `alpha=(1-q_H)^-1`, `beta=(1-q_D)^-1`, the inverse
resolvent identity gives

```text
||S_N-S||<=alpha^2 d_G,N,
||S_N-S||_(D->D)<=beta^2 d_GD,N.                       (13)
```

Expanding exactly one factor at a time in
`R_N=A_N+S_N^*W_NS_N` yields

```text
||(R_N-R)(H0+a)^-1||
 <= d_A,N
  + alpha^2 d_G,N B beta
  + alpha d_W,N beta
  + alpha B beta^2 d_GD,N
 =: tau_N.                                             (14)
```

Every term in (14) tends to zero by K139--K141. Both inverse-chart sides are
present; omitting either is an invalid residual claim. For any fixed cylinder
core vector `phi`,

```text
||(R_N-R)phi||<=tau_N||(H0+a)phi||.                    (15)
```

Equation (15) is the total Hilbert action tail K154 requires at the regular
level. Turning it into a numerical K152 residual still requires evaluated
finite action columns and outward numerical component bounds; this packet
does not invent them.

## 5. Exact rank-one exterior count criterion

Let `u` be normalized, `P=|u><u|`, `Q=1-P`, and suppose the complete selected
charge-sector compression obeys

```text
QHQ>=d Q.                                               (16)
```

Choose `b` with

```text
rho=<u,Hu> < b < d.                                    (17)
```

Then `Q(H-b)Q` is strictly positive. Congruence by the exact block Gaussian
elimination gives the scalar Schur complement

```text
rho-b-PHQ[Q(H-b)Q]^-1QHP < rho-b < 0.                  (18)
```

Therefore `H-b` has exactly one negative direction and no kernel. Equivalently,
the spectral projection `1_(-infinity,b)(H)` has rank one. This simultaneously
proves a complete ground count and makes `b` a next-distinct-spectrum floor.
The result permits arbitrary trial/exterior coupling; no stoquastic cone is
required.

The exact finite positive control passes congruence inertia. Native
applicability remains fail-closed: K148 gives an essential edge, not (16), and
K151/K155 finite second eigenvalues do not bound the infinite orthogonal
compression. K139--K155 also do not serialize a numerical `d` satisfying
(16). Consequently the count compiler must reject a native claim today. No
held-out score, prediction or confirmation is licensed by this structural
criterion.

## Inline postflight bookend

- **Strongest correction:** raw `V_N` is divergent subtraction data and cannot
  be assigned a separate limit. Exact normal ordering cancels it before any
  limiting operation.
- **Strongest construction:** K141's carrier plus K139's graph estimates turn
  K155's finite identity into one identified graph-relative `R_256`, with the
  complete propagated action error (14).
- **Strongest count result:** a complete exterior compression above `b` and
  one rank-one trial below `b` imply exactly one spectral value below `b` by
  exact Schur inertia, without positivity-improving matrix entries.
- **Strongest overclaim:** “K156 proves the native representative ground state
  is simple.” Refused. The criterion is proved; its complete native exterior
  premise is not.
- **Strongest contrary route:** a non-diagonal invariant cone could still prove
  simplicity without (16). No such cone is constructed here.
- **Weakest reproducibility seam:** qualitative convergence does not yet give
  K152 a numerical residual; every component of (14) must be outward evaluated
  on a named nested core.

The four admitted arcs share one proof/compiler/probe footprint and executed
inline. No external source retrieval or second writer was needed.

## Next condition

Choose explicit nested cylinder cores in `q=(0,0)` and `q=(1,0)`, evaluate the
finite regular form/action and every component of (14) with outward bounds,
and derive a complete exterior estimate (16), for example from a free-gap
minorant plus a certified graph-form bound for `X`. If `rho<b<d` closes, feed
the resulting count, total residual, Gram and coercivity packet to K154/K152
and transport `q=(0,1)` through the complete signed flavor intertwiner. If the
free-gap minorant fails, switch to equal-rank Lehmann--Goerisch rather than
reusing a finite cutoff gap or the HVZ edge.

## Reproduction

```bash
python3 tests/channel-swings/k156_common_carrier_regular_core.py --demo
python3 tests/channel-swings/k156_common_carrier_regular_core_exterior_count_probe.py
python3 tests/channel-swings/k156_common_carrier_regular_core_exterior_count_probe.py --selftest
```
