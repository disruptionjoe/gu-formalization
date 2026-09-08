---
title: "K155 finite regular pullback and stoquasticity-obstruction wave"
status: active_research
doc_type: conditional_exact_finite_regular_pullback_neumann_tail_and_ground_count_route_obstruction_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned finite-regulator pullback and route-discriminator theorem only; the K139 chart gives an exact rational R_N identity and certified finite Neumann truncation error on K151 charge blocks, while exact frustrated six-cycles in the first two-mode representative occupation graphs block the standard diagonal-gauge stoquastic Perron--Frobenius ground-count route without proving degeneracy or excluding another cone; common-carrier coefficient/graph convergence and a native count remain absent, so no native energy interval, threshold/Gram closure, scattering, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k155-finite-regular-pullback-stoquasticity-obstruction-wave.json
solver: tests/channel-swings/k155_finite_regular_pullback.py
probe: tests/channel-swings/k155_finite_regular_pullback_stoquasticity_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K155 finite regular pullback and stoquasticity-obstruction wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet takes the two independent continuations exposed by K154 as
far as the current public data permit. It derives the exact finite-cutoff
regular pullback for K151's canonical charge blocks and tests one concrete
ground-count route. A finite exact matrix is neither the common-carrier K139
limit nor a native spectral-count certificate.

```gu-typed-objects
result: exact finite regular-pullback identity with certified two-sided Neumann truncation error, signed flavor covariance, and a frustrated-cycle obstruction to the standard occupation-basis stoquastic Perron--Frobenius ground-count route
carrier: the hard-core n1*n2=0 subspace of Lambda(C2_impurity direct-sum C^(4M)_bath), in fixed q=(q1,q2), with K151 canonical wedge order and only finite M identified here LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive finite exterior-Fock Hilbert pairing; transpose is adjoint for the exact real rational control, while the continuum meaning remains K139's closed pulled-back form ON=repository_signed_point_control
real_structure: canonical CAR adjoint, real diagonal endpoint subtraction and signed exterior flavor permutation; the tested gauge group is only diagonal +/-1 on the occupation basis
grading: conserved q_i=n_i+N_i+-N_i-, hard-core impurity degree, finite boundary-word order and ground-versus-orthogonal spectral grading
action_owner: repository-construction -- cutoff profile, finite counterterm coordinate, chart, polarization, couplings, state, positivity cone and spectral floor are not selected by Weinstein's source or a GU action
target: finite coefficient-complete pullback and exact count-route discriminator before any common-carrier R_256 or native K152 claim MAP-TYPE=intertwiner
```

## Inline preflight bookend

K154 split the apparent matrix task into operator identification and spectral
exclusion. Retrieval found K139's defining chart
`G_N=-(H0_N+lambda)^(-1)C_N^*`, K151's exact occupation blocks, K153's
contraction calculus and K154's fail-closed packet. It found no serialized
common-carrier coefficient expansion, termwise graph-tail constants or
complete representative-sector count theorem.

The route census compared direct pullback algebra, word-by-word normal
ordering, boundary triples, finite Galerkin inversion, diagonal-gauge
stoquasticity, abstract cone positivity, min--max counting and exterior-form
lower bounds. The direct identity closes the finite operator algebra without
inventing continuum coefficients. Exact signed-cycle detection decides whether
the simplest positivity route survives beyond the one-mode fixture.

## 1. Separate the boundary halves before pulling back

On K151's finite charge basis, split the interaction exactly as

```text
C_N=sum_(i,j) g_j[d_i^* a_(i,+,j)+a_(i,-,j)d_i],
C_N^*=sum_(i,j) g_j[a_(i,+,j)^*d_i+d_i^*a_(i,-,j)^*].       (1)
```

Canonical CAR signs give `C_N^*=C_N^T` entry by entry. Let

```text
A_N=H0_N+lambda I,
G_N=-A_N^-1 C_N^*,
U_N=I-G_N.                                                   (2)
```

For the equal two-edge C3 control, the matched endpoint incidence matrix is

```text
D=2|0><0|+|1><1|+|2><2|.                                   (3)
```

The finite supplied counterterm is `V_N=c_N(lambda)D+E_R I`, with
`c_N=sum_j g_j^2/(epsilon_j+lambda)`. This is the K139 subtraction coordinate
for the finite control, not a source-selected physical extension.

## 2. The exact finite regular representative

Put `H_N=H0_N+C_N+C_N^*+V_N`. Equation (2) implies

```text
C_N^*=-A_N G_N,                 C_N=-G_N^* A_N,
U_N^* A_N U_N
  =A_N+C_N+C_N^*+G_N^*A_NG_N.                              (4)
```

Therefore, with

```text
W_N=V_N-lambda I-G_N^*A_NG_N,                              (5)
```

the exact two forms of the regular pullback are

```text
R_N=U_N^(-*) H_N U_N^-1
   =A_N+U_N^(-*) W_N U_N^-1.                               (6)
```

The solver constructs every matrix over exact rationals and verifies both
`U_N^*R_NU_N=H_N` and the equality of the two expressions in (6). This is the
coefficient-complete *finite* formula missing from K154. Passing `N` to
infinity still requires one common carrier, explicit embeddings, convergence
of `A_N`, `G_N`, `V_N` and the quadratic term, and a graph-relative bound for
the complete series. K139 asserts the needed term-class convergence but does
not serialize those coefficient/tail data, so (6) alone does not identify a
native `R_256` packet.

## 3. A certified finite Neumann matrix tail

For a finite block set

```text
q_1=||G_N||_1,        q_infinity=||G_N||_infinity.           (7)
```

When both are below one, the order-`J` partial inverse
`S_J=sum_(j=0)^J G_N^j` has exact tails

```text
t_1=q_1^(J+1)/(1-q_1),
t_infinity=q_infinity^(J+1)/(1-q_infinity).                 (8)
```

Submultiplicativity applied to
`S^*W_NS-S_J^*W_NS_J` gives

```text
||R_N-[A_N+S_J^*W_NS_J]||_infinity
 <= ||W_N||_infinity[
      t_1/(1-q_infinity)+t_infinity/(1-q_1)].               (9)
```

The exact solver computes the actual rational matrix error and refuses the
certificate unless (9) dominates it. At `lambda=256`, two rational modes
`epsilon=(5/4,3/2)` and equal unit coefficients, the q=(0,0) block has
dimension 84, `q_infinity=4/267` and `q_1=8236/529935`; its order-three
certificate is strict. Equation (9) is a finite matrix truncation theorem. It
is not K139's missing uniform common-carrier graph tail.

Signed flavor permutation intertwines every ingredient of (1)--(6), so the
exact `q=(1,0)` regular pullback transports to `q=(0,1)`. As in K151, verbal
equal coupling is not the certificate; the signed exterior matrix is.

## 4. The occupation-basis positivity route fails at two modes

For a real symmetric matrix, a diagonal occupation-basis gauge
`S=diag(s_x)`, `s_x in {+1,-1}`, makes every nonzero off-diagonal entry
nonpositive exactly when each edge constraint

```text
s_x s_y=-sign(H_xy)                                         (10)
```

is consistent. Around a cycle of length `ell`, consistency requires

```text
product_cycle sign(H_xy)=(-1)^ell.                          (11)
```

The one-mode q=(0,0) and q=(1,0) interaction graphs are connected and satisfy
(10), which explains why the smallest fixtures tempt a Perron--Frobenius
argument. The first two-mode graphs remain connected but fail (11). In
q=(0,0), one exact six-cycle is

```text
|0;1+:0,1-:1> -> |1;1-:1> -> |0;-> -> |1;1-:0>
 -> |0;1+:0,1-:0> -> |1;1+:0,1-:0,1-:1> -> start,          (12)
```

with edge signs `(+, +, +, +, +, -)`. Their product is `-1`, while (11)
requires `+1`. The q=(1,0) representative has its own exact frustrated
six-cycle, and flavor transport carries the obstruction to q=(0,1).

Thus no diagonal `+/-` occupation gauge makes these first nontrivial blocks
stoquastic. The standard entrywise Perron--Frobenius proof cannot supply
K154's ground-count certificate. This does **not** prove a degenerate finite or
continuum ground state, and it does not exclude a non-diagonal cone, a
positivity-improving representation after a deeper transform, or an exterior-
subspace lower-bound route.

## Inline postflight bookend

- **Strongest construction:** the finite countertermed charge block now has an
  exact coefficient-complete regular representative and an independently
  checked pullback identity.
- **Strongest quantitative control:** exact one-/infinity-norm Neumann tails
  bound the full finite regular-matrix truncation error, not only the inverse.
- **Strongest route change:** connected one-mode graphs are misleading; exact
  fermionic exchange creates frustrated six-cycles as soon as two modes are
  present, blocking the standard diagonal-gauge stoquastic count proof.
- **Strongest overclaim:** “the native ground state is degenerate.” Refused.
  Only one basis/gauge positivity route is excluded.
- **Strongest contrary route:** a non-diagonal positivity cone or a direct
  exterior-form lower bound may still prove simplicity/count; neither is
  supplied here.
- **Weakest reproducibility seam:** the finite tail in (9) does not compare
  different cutoff carriers and therefore cannot be relabeled as K139's
  continuum graph tail.

All admitted arcs share one exact solver/probe footprint and ran inline. No
independent source context or second writer was needed.

## Next condition

Place all finite charge blocks on an explicit common cylinder-core carrier and
serialize the normal-ordered coefficients of `A_N`, `G_N`, `V_N` and
`G_N^*A_NG_N`; prove coefficientwise and graph-relative convergence of (6) to
one `R_256`, including total residual tails. For the independent count
obligation, abandon occupation-basis diagonal stoquasticity: either construct
and prove an invariant non-diagonal positivity cone, or certify a complete
exterior-subspace lower bound/count below a chosen `b`. Only then feed K154 and
K152.

## Reproduction

```bash
python3 tests/channel-swings/k155_finite_regular_pullback.py --demo
python3 tests/channel-swings/k155_finite_regular_pullback_stoquasticity_probe.py
python3 tests/channel-swings/k155_finite_regular_pullback_stoquasticity_probe.py --selftest
```
