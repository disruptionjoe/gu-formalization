---
title: "K80 rotating-null shear and mass-control wave"
status: active_research
doc_type: reverse_scaffold_rotating_null_shear_mass_control_result
date: 2026-09-01
target_claim: internal target K79-TWO-DIMENSIONAL-MASS-CONTROL-CEILING; verdict the collapse is dimension-specific and has an exact rotating signature-(2,1) countercontrol
claim_ceiling: exact arbitrary-null current reduction and one rotating real signature-(2,1) mass-control counterexample; no source-owned full carrier, principal symbol, gauge complex, analytic domain or physical bridge theorem
manifest: lab/process/k80-rotating-null-shear-mass-control-wave.json
probe: tests/channel-swings/k80_rotating_null_shear_mass_control_probe.py
---

# K80 rotating-null shear and mass-control wave

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
result: exact current reduction for every C2 null shear in a constant real indefinite carrier, plus a rotating signature-two-one countercontrol to the two-dimensional mass-collapse conclusion
carrier: one real observed scalar q and a repository-owned finite-dimensional real source field T on a Lorentzian one-plus-one base; the explicit control uses R^(2,1) LAYER=conditional CHIRALITY=N/A
pairing: constant base symbol eta and source-carrier form H; the explicit control has H=diag(1,1,-1), neither source-owned
real_structure: real C2 point curve b(q), real C2 null field n(q), real C1 shear w^rho(q), and symmetric second jets
grading: jet order through two modulo the divergence of an explicit first-jet current; no gauge, BRST or BV quotient
action_owner: repository owns the frozen kinetic and quadratic-potential controls; no filed source action owns this bridge class
target: whether genuinely rotating higher-signature null fields reopen the highest-jet equations and evade the prior nondegenerate mass-control collapse MAP-TYPE=classification
```

## Result first

Null rotation does not reintroduce an acceleration-square term. For every
`C2` null field in any finite-dimensional constant real indefinite carrier,
the complete acceleration dependence of the affine first-jet shear remains an
explicit divergence plus a first-order term. Rotation does, however, destroy
the special two-dimensional mass-control collapse: in signature `(2,1)` an
exact rotating null curve admits a nondegenerate `m^2 H` potential that is
velocity-independent while the pulled-back kinetic density remains nonzero.

This is a repository-owned conditional control. It is not a full-carrier GU
bridge and does not identify Weinstein's source action, symbol, gauge complex
or domain.

## General null-field reduction

Freeze a constant source form `H`, a null field `n(q)` and

```text
T=b(q)+n(q) psi,        psi=w^rho(q)v_rho,
v_mu=partial_mu q,      X=(1/2)eta^(mu nu)v_mu v_nu.         (1)
```

Differentiating `<n,n>_H=0` gives `<n,n'>_H=0`. Hence

```text
partial_mu T=(b'+n' psi)v_mu+n partial_mu psi.               (2)
```

With `c(q)=<b'(q),n(q)>_H`, the null and differentiated-null
identities remove every quadratic `partial psi` term and give

```text
K=(<b',b'>+2<b',n'>psi+<n',n'>psi^2)X
  +c w^rho partial_rho X+2c w^(rho prime)v_rho X.            (3)
```

The only acceleration term obeys

```text
c w^rho partial_rho X
=partial_rho(c w^rho X)
 -(c' w^rho+c w^(rho prime))v_rho X.                         (4)
```

Thus modulo the displayed first-jet current,

```text
K_eff=(<b',b'>+2<b',n'>psi+<n',n'>psi^2)X
     +(c w^(rho prime)-c' w^rho)v_rho X.                    (5)
```

The prior fixed-line formula is the special case `n'=0` after absorbing a
scalar null-field factor into `w`. Equation (5) shows precisely what genuine
projective rotation adds: the first-order coefficients involving `n'`, not a
new highest-jet obstruction.

## Exact rotating signature-`(2,1)` control

Use `H=diag(1,1,-1)` and the polynomial null curve

```text
n(q)=(1-q^2,2q,1+q^2),        b(q)=n'(q)=(-2q,2,2q).         (6)
```

It is nonzero and projectively varying. Direct calculation gives

```text
<n,n>=0,       <n,n'>=0,       <n',n'>=4,
<n'',n>=-4,    <n'',n'>=0,      <n'',n''>=0.                 (7)
```

Take `w=(1,0)`, so `psi=v_0`, and note `c=<b',n>=-4` is
constant. Equation (5) becomes

```text
K_eff=4 v_0^2 X.                                             (8)
```

The exact current removes all acceleration terms, but the first-order kinetic
density is nonzero. Meanwhile the nondegenerate mass control gives

```text
(m^2/2)<T,T>_H
=(m^2/2)(<n',n'>+2v_0<n',n>+v_0^2<n,n>)
=2m^2.                                                       (9)
```

It is independent of velocity. Thus the same nondegenerate carrier form can
own a velocity-blind quadratic potential without forcing the point curve onto
the null line or collapsing the kinetic density.

## Dimension boundary

For a general symmetric quadratic form `M`, velocity independence on an open
shear-support region is still equivalent to

```text
n^T M n=0,        n^T M b=0.                                (10)
```

When `M=m^2H` and `b=n'`, both equations follow from nullity and its first
derivative. The two-dimensional predecessor collapsed because a null line in
signature `(1,1)` is its own orthogonal complement and cannot rotate without a
zero. In higher indefinite dimension `n^perp` is larger and a rotating null
curve can have nonnull tangent. Equation (9) is the exact contrary control.

## Hostile review and claim ceiling

The strongest overclaim would call (5) a source bridge. It is only a universal
identity inside the frozen affine first-jet map class with constant `H`. The
strongest contrary concern is that a rotating direction might hide second jets
inside `n'(q)psi`; equation (2) keeps those terms first-order and exposes the
only `partial psi` contribution explicitly. The weakest reproducibility seam
is trigonometric approximation, avoided here by the polynomial rational null
parameterization (6).

The packet refutes only an attempted extension of the repository's own
two-dimensional mass-control conclusion. Singular and nonlocal maps, higher
jets, auxiliary fields, on-shell equivalence, gauge/BV reduction, source-owned
full-carrier symbols, closed analytic domains, physical observables,
predictions, confirmations and GU verdicts remain outside the result.

## Next condition

Obtain the independently source/action-owned full-carrier principal symbol,
gauge complex and analytic domain. Then test whether its actual derivative
image is an `H`-null subbundle, whether the connection preserves it, and
whether the complete Helmholtz and quotient equations admit the rotating
control rather than merely its repository-owned finite model.

Reproduce with:

```bash
python3 tests/channel-swings/k80_rotating_null_shear_mass_control_probe.py
python3 tests/channel-swings/k80_rotating_null_shear_mass_control_probe.py --selftest
```
