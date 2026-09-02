---
title: "K91 observed functional causal-complex wave"
status: active_research
doc_type: reverse_scaffold_functional_causal_complex_result
created: 2026-09-01
date: 2026-09-01
claim_ceiling: exact repository-owned split short exact l2 constraint sequence, closed gapped diagonal physical generator, rapid-sequence invariant core, modewise retarded and advanced wave Green operators, and gauge-basic descent; no source GU functional BV-BFV complex, curved-spacetime Green hyperbolicity, boundary trace theorem, spatial AQFT, microlocal or Hadamard state, prediction, confirmation, or verdict
manifest: lab/process/k91-observed-functional-causal-complex-wave.json
probe: tests/channel-swings/k91_observed_functional_causal_complex_probe.py
---

# K91 observed functional causal-complex wave

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
result: exact split l2 functional constraint sequence with one closed gapped physical generator and modewise causal Green pair
carrier: G and P copies of complex l2(N), their split ambient sum G direct-sum P, and rapid-sequence test functions LAYER=observed CHIRALITY=N/A
pairing: real part of the l2 pairing and its antisymmetric retarded-minus-advanced source form ON=repository_owned_functional_control
real_structure: coefficientwise complex conjugation, preserved by the diagonal operator and Green kernels
grading: three-term short exact sequence degrees minus one, zero and one; no source BV or BFV grading
action_owner: repository-construction wave control; no GU source action or Euler operator is supplied
target: K89 closed-gap criteria composed with K90 retarded/advanced support and gauge-basicness on one explicit physical quotient MAP-TYPE=quotient
```

Scope: this result binds only the repository-owned split sequence, diagonal
operator, rapid test core and one-dimensional-time Green formulas below; it
does not bind a GU action, source constraint complex, spacetime geometry,
boundary theory, state, detector law or physical verdict.

## Inline preflight bookend

The problem-matched lens census covered closed-operator and graph-domain
analysis, Hilbert complexes and split exact sequences, nuclear Fréchet test
spaces, energy/evolution equations, distributional Green kernels,
Peierls/symplectic descent, gauge-basic observables, BRST/BFV ownership,
curved-spacetime Green hyperbolicity, boundary traces, algebraic locality,
microlocal spectrum and exact finite computation. The split Hilbert sequence
with a diagonal wave operator was the smallest object that puts K89's gap and
domain owner together with K90's support and basicness owners without importing
spatial, boundary or microlocal structure.

Repository retrieval found K89's closed diagonal `Omega` and bounded stationary
inverse, and K90's separate finite integer-time Green pair. It found no
object-level duplicate of the short exact `l2` sequence below equipped with
the continuous-time modewise wave pair. The positive controls are exactness,
the unit gap, graph closedness, core invariance, Green identities, opposite
temporal support, antisymmetry and representative independence. Negative
controls separately mutate the gap, the quotient map, one support direction,
the advanced sign, the observation's gauge coefficient and the distinction
between the rapid core and a closed Hilbert domain.

## Result first

Let

```text
G = l2(N,C),       P = l2(N,C),       H = G direct-sum P,
d0(g) = (g,0),     q(g,p) = p.                              (1)
```

Then

```text
0 -> G --d0--> H --q--> P -> 0                             (2)
```

is a split short exact Hilbert-space sequence: `d0` is an isometry, `q` is a
bounded surjection, `q d0=0`, and `ker q=im d0`. The bounded section
`j(p)=(0,p)` identifies the physical quotient `H/im d0` with `P`. Equation
(2) is a constraint/quotient sequence, not a claim that its exact cochain
cohomology supplies a nonzero physical sector.

On the physical quotient define

```text
Omega e_n = (n+1)e_n,
D(Omega) = {x in P : sum_n (n+1)^2 |x_n|^2 < infinity}.     (3)
```

`Omega` is positive self-adjoint and closed on the graph-complete Hilbert
domain `D(Omega)`, has lower spectral bound one and bounded inverse of norm
one. Thus it is exactly K89's gapped diagonal owner on the `P` term of one
explicit quotient sequence.

The common invariant test core is the rapid-sequence space

```text
s = {x : ||Omega^k x||_2 < infinity for every k >= 0}.      (4)
```

With seminorms `p_k(x)=||Omega^k x||_2`, this is a complete nuclear Fréchet
space. Completeness follows by taking a sequence Cauchy in every weighted
Hilbert norm and identifying the compatible coordinatewise limits. Nuclearity
follows from the Hilbert-scale criterion: the inclusion from the `(k+1)`
weighted completion to the `k` weighted completion has singular values
`1/(n+1)`, whose squares are summable. Multiplication by `Omega` maps `s`
continuously into itself. Finite truncations of any `x in D(Omega)` converge
to `x` in the graph norm, so `s` is a core for `Omega`.

That last sentence does not make `s` a closed Hilbert operator domain. It is a
dense proper subspace of `D(Omega)`: the sequence `x_n=(n+1)^(-2)` lies in
`D(Omega)` but not in `s`, and its finite truncations lie in `s` and converge
in the graph norm. The closed Hilbert domain is (3); the complete nuclear
Fréchet core is (4). The pointwise square `Omega^2` likewise has its natural
closed domain `D(Omega^2)`, which must not be silently replaced by `D(Omega)`.

## The causal pair on the same physical term

For `f in C_c^infinity(R;s)`, define modewise

```text
(G_ret f)(t) =  integral_(-infinity)^t
                Omega^(-1) sin(Omega(t-s)) f(s) ds,

(G_adv f)(t) = -integral_t^(infinity)
                Omega^(-1) sin(Omega(t-s)) f(s) ds.         (5)
```

Both maps take `C_c^infinity(R;s)` to `C^infinity(R;s)`. Indeed the kernel in
mode `n` is bounded by `1/(n+1)`; time differentiation only introduces finite
powers of `Omega`, which every seminorm in (4) controls. Their outputs are
therefore in `D(Omega^2)` at every time, so

```text
L = partial_t^2 + Omega^2                                 (6)
```

acts legitimately on them.

For each mode the sine kernel solves the homogeneous equation away from
`t=s`, is continuous there, and its first time derivative has unit jump. Hence
`L G_ret f=f=L G_adv f`. Conversely, two integrations by parts for a compactly
supported `s`-valued test function give `G_ret Lf=f=G_adv Lf`; all endpoint
terms vanish. These are analytic modewise identities on the infinite test
space, not conclusions extrapolated from finite truncations.

The retarded kernel vanishes for `t<=s`; the advanced kernel vanishes for
`t>=s`. Thus their supports lie in the future and past temporal half-lines of
the source, respectively. There is no spatial variable or metric here, so this
is an exact time-order support statement, not curved-spacetime Green
hyperbolicity or spatial finite propagation.

Their difference has kernel

```text
E_n(t,s) = sin((n+1)(t-s))/(n+1),                          (7)
```

which is antisymmetric under interchange of `t,s`. The real part of the
`l2` pairing therefore gives an antisymmetric source form
`sigma(f,h)=integral <f,E h>_R dt` whenever the named compact supports make the
iterated integral finite.

## Gauge-basic descent

Extend either physical Green map across the ambient sequence by zero on `G`:

```text
G_tilde(g,f) = (0,G f).                                   (8)
```

Then `q G_tilde = G q`, `G_tilde d0=0`, and changing a representative
`(g,f)` by `d0(gamma)` changes neither its physical Green output nor any basic
observation. More generally, a continuous linear observation `ell` on `H`
descends through `q` exactly when `ell d0=0`; in the split coordinates this is
exactly the absence of a `G` coefficient. Thus zero extension and observation
basicness are consequences of the same explicit short exact sequence rather
than independent finite declarations.

## What moved and what did not

The control composes the previously separate K89 and K90 criteria on one
functional object. The physical diagonal generator has one closed gapped
Hilbert domain and one invariant nuclear test core; the corresponding wave
operator has distinct retarded and advanced maps on that core; and both maps
descend through the same gauge quotient used by the observations.

The construction is repository-selected. It contains no coefficients,
variation, gauge generator or observation map authenticated to Weinstein's
source. It has only a time line, no spatial causal cone, no boundary trace or
global boundary condition, no local observable net, no wavefront set, no
Hadamard state and no detector or probability rule.

## Inline postflight bookend

- Strongest overclaim: renaming this split diagonal control a source GU
  functional BV--BFV complex. Nothing here supplies source ownership, an
  action-selected differential, BV/BFV brackets or a GU observation map.
- Strongest contrary construction: replacing `Omega_n=n+1` by
  `Omega_n=1/(n+1)` preserves modewise positive frequencies but removes the
  uniform gap and makes the inverse norms diverge; independently, mixing the
  retained quotient with the gauge injection makes `q d0` nonzero, while a
  future leak or reversed advanced sign breaks only the relevant Green test.
- Weakest reproducibility seam: the probe checks finitely many exact modes and
  half-`pi` kernel values. The infinite-dimensional completeness, nuclearity,
  graph closedness, core density and Green identities are proved above; the
  finite probe is a regression control for the formulas and fences, not their
  proof.

The exact finite-mode probe passes its declared checks and its hostile selftest
catches gap, sequence, support, sign, basicness, core/domain and promotion
mutations. No source functional complex, curved-spacetime theorem, boundary
trace result, spatial AQFT net, microlocal/Hadamard state, prediction,
confirmation, canon or public posture moves.

## Next condition

Supply an authenticated source action and source constraint differential on a
specified GU carrier. Prove a closed invariant quotient domain, identify the
source Euler operator, and construct its retarded/advanced pair with the
source spacetime support and boundary conditions. Only after those maps are
shown cochain/basic may microlocal spectrum, local observables and detector
dynamics be assessed.
