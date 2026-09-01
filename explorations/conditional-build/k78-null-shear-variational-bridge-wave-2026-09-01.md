---
title: "K78 null-shear variational bridge wave"
status: active_research
doc_type: reverse_scaffold_null_shear_variational_bridge_result
date: 2026-09-01
claim_ceiling: exact variational and quadratic-potential classification for one fixed-null-line first-jet control on a Lorentzian 1+1 base and real two-dimensional carrier; no source-owned full-carrier, gauge-reduced, analytic-domain or physical bridge theorem
manifest: lab/process/k78-null-shear-variational-bridge-wave.json
probe: tests/channel-swings/k78_null_shear_variational_bridge_probe.py
---

# K78 null-shear variational bridge wave

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
result: exact reduction of a fixed-null-line first-jet shear through its linear acceleration term, plus the exact quadratic-potential compatibility condition
carrier: one real observed scalar q and a repository-owned real two-component source field T on a Lorentzian 1+1 base LAYER=conditional CHIRALITY=N/A
pairing: base symbol eta=diag(1,-1) and source-carrier form H=diag(1,-1); neither is source-owned
real_structure: real C2 point curve b(q), fixed real null vector n, constant real shear coefficients a^rho and symmetric second jets
grading: jet order through two modulo the divergence of an explicit first-jet current; no gauge, BRST or BV quotient
action_owner: repository owns the frozen kinetic and quadratic-potential controls; no filed source action owns this bridge class
target: whether the surviving totally-null velocity image closes the remaining linear highest-jet equations and when a quadratic potential preserves the shear MAP-TYPE=classification
```

## Result first

The preceding highest-jet theorem left open whether its totally null escape
survives the terms linear in the second jet. For the natural fixed-null-line
subclass, it does: every linear acceleration term is an explicit divergence
plus a first-order correction. A nondegenerate quadratic potential built from
the same Lorentzian carrier form then gives the opposite result: demanding
velocity independence forces the point curve onto the null line and collapses
the kinetic density.

Freeze Lorentzian base coordinates `x^0,x^1`, velocities
`v_mu=partial_mu q`, a constant null vector `n` with `<n,n>_H=0`, constants
`a^rho`, and the first-jet map

```text
T=b(q)+n psi,              psi=a^rho v_rho.                    (1)
```

This is the integrable fixed-line representative of the rank-one totally null
velocity image. It does not classify rotating null lines or the full `C2`
solution of the velocity-space Frobenius equations.

Let

```text
X=(1/2) eta^(mu nu) v_mu v_nu,
c(q)=<b'(q),n>_H.                                             (2)
```

Because the shear--shear pairing vanishes, the pulled-back kinetic density is

```text
K=(1/2)<b',b'>_H eta^(mu nu)v_mu v_nu
  +c(q) a^rho eta^(mu nu)v_mu q_(nu rho).                     (3)
```

Symmetry of the second jet gives

```text
eta^(mu nu)v_mu q_(nu rho)=partial_rho X.                     (4)
```

Hence the complete linear acceleration term has the exact decomposition

```text
c a^rho partial_rho X
=partial_rho(c a^rho X)-c'(q)(a^rho v_rho)X.                  (5)
```

Modulo the displayed first-jet current, the frozen null shear therefore has
the first-order representative

```text
K_eff=<b',b'>_H X-c'(q)(a.v)X.                               (6)
```

The null escape is thus not an artifact of stopping at the quadratic
highest-jet term. Within this fixed-line subclass, the remaining acceleration
term always closes variationally. It may produce a cubic velocity interaction,
so it does not automatically match a conventional quadratic target kinetic
term.

## Exact quadratic-potential fork

For a real symmetric matrix `M`, set

```text
P(T)=(1/2) T^T M T.
```

Substitution of (1) gives

```text
P(b+n psi)=(1/2)b^T M b+psi n^T M b
            +(1/2)psi^2 n^T M n.                            (7)
```

For nonzero shear coefficients, this is independent of all velocities if and
only if

```text
n^T M n=0,             n^T M b(q)=0 for every q.             (8)
```

The first equality removes the quadratic shear term and the second removes the
linear one. These conditions are necessary and sufficient in the frozen
quadratic model.

Take the nondegenerate mass control `M=m^2 H`, `m^2 != 0`, on the real
two-dimensional carrier of signature `(1,1)`. Nullity already gives the first
condition. The second becomes `<n,b(q)>_H=0`. In signature `(1,1)`, the
orthogonal complement of a null line is that same null line, so

```text
b(q) in span(n).                                               (9)
```

Then `<b',b'>_H=<b',n>_H=0`, and both (3) and (6) vanish. Thus a
nondegenerate `H`-mass potential admits no null-shear bridge with a nonzero
pulled-back kinetic density in this exact two-component class. This is a
control-model no-go, not a source or GU no-go.

## Witnesses and contrary controls

Use `H=diag(1,-1)`, `n=(1,1)`, `m=(1,-1)`, `b(q)=m q`, and
`psi=v_0+2v_1`. Then `<m,m>=<n,n>=0` and `<m,n>=2`.

- With zero potential, (5) supplies an explicit current and the entire
  acceleration dependence reduces to a first-order cubic term. Since `c=2`
  is constant, even that correction vanishes; the kinetic density is a pure
  divergence. This is nontrivial as a map but dynamically degenerate.
- With `b(q)=(q,q^2)` and the same `n`, `c(q)=1-2q`, so the correction
  `2(a.v)X` is genuinely nonzero and first order. The kinetic bridge survives
  but acquires a cubic velocity interaction.
- With `M=m^2H` and `b(q)=mq`, (7) contains the nonzero term
  `2m^2 q psi`; the massive potential detects and excludes the shear.
- With a positive carrier metric there is no nonzero real null `n`, so the
  whole fixed-null-line class is absent.

These controls separate four statements that must not be unioned: quadratic
highest-jet survival, variational removal of linear accelerations, matching a
chosen first-order kinetic target, and compatibility with a chosen potential.

## Hostile review and claim ceiling

The strongest overclaim would promote the mass-control obstruction to the
unknown source action. The packet freezes a two-component constant carrier
form, a constant null line, a local affine-in-velocity shear and a quadratic
potential. The source owns none of these objects. A rotating null line,
variable principal symbol, singular map, nonlocal map, auxiliary field,
on-shell equivalence or gauge/BV quotient can evade the frozen classification.

The strongest contrary construction is already internal: zero potential and a
nonconstant point curve make the linear acceleration term variationally
admissible. The weakest reproducibility seam is the restriction from every
totally-null velocity image to the fixed-null-line affine representative (1).
The exact probe certifies the displayed algebra and controls; it does not prove
the missing velocity-space Frobenius classification or an analytic field-map
theorem.

No source-owned full-carrier symbol, connection-preserved null subbundle,
gauge complex, closed domain, physical pairing, observable, prediction,
confirmation or GU verdict follows.

## Next condition

Classify the rotating-null-line `C2` solutions and their boundary-current
Helmholtz equations, or obtain the independently source/action-owned full
principal symbol, gauge complex and analytic domain. A physical bridge must
also show that its source potential is constant along the admitted null shear
or explain which gauge/auxiliary mechanism replaces condition (8).

Reproduce with:

```bash
python3 tests/channel-swings/k78_null_shear_variational_bridge_probe.py
python3 tests/channel-swings/k78_null_shear_variational_bridge_probe.py --selftest
```
