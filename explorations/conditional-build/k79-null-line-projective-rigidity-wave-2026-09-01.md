---
title: "K79 null-line projective rigidity wave"
status: active_research
doc_type: reverse_scaffold_null_line_projective_rigidity_result
date: 2026-09-01
claim_ceiling: exact projective-null and variable-shear variational classification for one real two-dimensional carrier of signature one-one; no higher-signature, zero-crossing, source-owned full-carrier, gauge-reduced, analytic-domain or physical bridge theorem
manifest: lab/process/k79-null-line-projective-rigidity-wave.json
probe: tests/channel-swings/k79_null_line_projective_rigidity_probe.py
---

# K79 null-line projective rigidity wave

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
result: exact reduction of every nonvanishing C1 null direction in a connected real signature-one-one carrier to one fixed projective null line, followed by the variable-shear current and quadratic-potential classification
carrier: one real observed scalar q and a repository-owned real two-component source field T on a Lorentzian one-plus-one base LAYER=conditional CHIRALITY=N/A
pairing: base symbol eta=diag(1,-1) and source-carrier form H=diag(1,-1); neither is source-owned
real_structure: real C2 point curve b(q), nonvanishing real C1 null field n(q), real C1 shear coefficients A^rho(q), and symmetric second jets
grading: jet order through two modulo the divergence of an explicit first-jet current; no gauge, BRST or BV quotient
action_owner: repository owns the frozen kinetic and quadratic-potential controls; no filed source action owns this bridge class
target: whether the previously open rotating-null-line horn exists in the same two-component carrier and whether its variable shear closes the remaining linear highest-jet equations MAP-TYPE=classification
```

## Result first

There is no genuinely rotating nonzero null line in a real two-dimensional
carrier of signature `(1,1)`. On a connected interval every continuous null
direction lies in one of the two fixed projective null lines. The only allowed
motion is a nonzero scale, which can be absorbed into a variable first-jet
shear coefficient. That larger variable-shear class still closes every linear
acceleration term modulo an explicit first-jet current.

Write a nonvanishing null field as `n(q)=(x(q),y(q))`. Nullity gives

```text
x(q)^2-y(q)^2=0.                                               (1)
```

Nonvanishing implies `x(q) != 0`, so `s(q)=y(q)/x(q)` is continuous and
`s(q)^2=1`. A continuous map from a connected interval into `{+1,-1}` is
constant. Therefore

```text
n(q)=r(q)n_sigma,       n_sigma=(1,sigma),
sigma in {+1,-1},       r(q) != 0.                            (2)
```

Thus the proposed rotating line reduces exactly to a fixed projective line.
This argument is dimension- and nonvanishing-specific. It does not apply
through zeros of `n`, and it fails in higher indefinite signature where the
projectivized null cone has positive dimension.

## Variable-shear variational reduction

Absorb the scale `r(q)` into the shear coefficients and freeze

```text
T=b(q)+n_sigma psi,       psi=w^rho(q)v_rho,
v_mu=partial_mu q.                                             (3)
```

Let

```text
X=(1/2)eta^(mu nu)v_mu v_nu,
c(q)=<b'(q),n_sigma>_H.                                      (4)
```

Since `n_sigma` is null, all shear--shear terms vanish. Direct differentiation
gives

```text
K=<b',b'>_H X
  +c w^rho partial_rho X
  +2c w^(rho prime)v_rho X.                                  (5)
```

The acceleration term obeys

```text
c w^rho partial_rho X
=partial_rho(c w^rho X)
 -(c' w^rho+c w^(rho prime))v_rho X.                         (6)
```

Combining (5) and (6), the complete first-order representative is

```text
K_eff=<b',b'>_H X
      +(c w^(rho prime)-c' w^rho)v_rho X.                    (7)
```

Hence allowing the null scale and shear direction in base cotangent space to
vary with `q` does not reopen the linear highest-jet obstruction. It changes
the surviving cubic velocity coefficient from `-c'w` to the Wronskian-like
combination `c w'-c'w`.

For the exact control `n_+=(1,1)`, `b(q)=(q,q^2)` and
`w(q)=(q,1)`, one has `c=1-2q`, and (7) becomes

```text
K_eff=<b',b'>_H X+(v_0+2v_1)X.                               (8)
```

This supplies a nonconstant variable-shear witness rather than merely
relabeling the constant-coefficient predecessor.

## Quadratic-potential fork

For a real symmetric matrix `M`, substitution into
`P(T)=(1/2)T^T M T` gives

```text
P(b+n_sigma psi)=(1/2)b^T M b
 +psi n_sigma^T M b
 +(1/2)psi^2 n_sigma^T M n_sigma.                            (9)
```

On any open shear-support region where `w` is not the zero covector, velocity
independence holds exactly when

```text
n_sigma^T M n_sigma=0,
n_sigma^T M b(q)=0.                                          (10)
```

For nonzero `M=m^2H`, the second condition forces `b(q)` into the same null
line, because a null line in signature `(1,1)` is its own orthogonal
complement. Equations (5)--(7) then vanish identically. The prior mass-control
obstruction therefore extends from constant shear coefficients to the entire
nonvanishing null-field class in this exact two-component carrier.

## Boundary controls

- A direction switch can occur only through a zero. The continuous null field
  `n(q)=(q,|q|)` changes projective component at `q=0`, precisely where it
  vanishes and the division used in (2) is unavailable.
- Higher signature genuinely permits rotation. For
  `H_3=diag(1,1,-1)`, the field
  `n(theta)=(cos(theta),sin(theta),1)` is nonzero, null and projectively
  nonconstant.
- A positive carrier metric has no nonzero real null direction, so neither the
  fixed nor variable shear class exists.
- A degenerate or specially aligned `M` can satisfy (10) without forcing the
  point curve onto the null line. The mass conclusion uses the exact
  nondegenerate `m^2H` control.

These controls prevent a two-dimensional projective theorem from becoming a
full-carrier statement.

## Hostile review and claim ceiling

The strongest overclaim would say that rotating-null bridges are impossible.
What is proved is narrower: in one real two-dimensional carrier of signature
`(1,1)`, a nonvanishing continuous null direction cannot rotate
projectively. Zeros, higher-dimensional indefinite carriers, complex null
cones, singular maps, nonlocal maps, auxiliary fields, on-shell equivalence
and gauge/BV quotients remain outside the theorem.

The strongest contrary construction is the explicit rotating null circle in
signature `(2,1)`. The weakest reproducibility seam is regularity at zeros of
the null field; the packet excludes them rather than silently extending (2).
The probe certifies the null-cone reduction, exact current identity, potential
conditions and all boundary controls.

No source-owned full-carrier symbol, connection-preserved null subbundle,
gauge complex, closed analytic domain, physical pairing, observable,
prediction, confirmation or GU verdict follows.

## Next condition

Obtain the independently source/action-owned full-carrier principal symbol,
gauge complex and analytic domain, then determine whether its actual
higher-dimensional null cone admits a connection-preserved derivative-image
subbundle satisfying the full Helmholtz equations. If zeros or singular
directions are essential, freeze their admissible map class and matching law
before assigning bridge credit.

Reproduce with:

```bash
python3 tests/channel-swings/k79_null_line_projective_rigidity_probe.py
python3 tests/channel-swings/k79_null_line_projective_rigidity_probe.py --selftest
```
