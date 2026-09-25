---
title: "K463 K152 Complement-Count and Coercivity Composition"
status: active_research
doc_type: conditional-build
updated_at: "2026-09-25"
---

# K463 — compose the complete M-complement count with coercivity

GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or
borders a conventional particle-physics comparator. Any result about a
standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
Majorana mechanism, anomaly selector, VEV-only breaking or familiar
vector-mass route binds only that named model. It is not evidence for or
against Weinstein's source-native mechanism without an explicit typed bridge.
Read `lab/methods/source-native-comparator-routing.md` and follow its
source-native pointers before reusing this result.

## Typed scope

This packet is an exact certificate-interface theorem in the physical
`M=S* S` Hilbert geometry. Its carrier is one complete K162 charge sector in
the fixed limiting K139 form domain. Its split is the M-orthogonal sum

```text
span(u) direct-sum u^(perp_M),       ||u||_M=1.
```

The action owner, extension selection, state, scalar center and numerical
native constants are repository inputs, not source-selected GU data. The
result is `INTERNAL_STRUCTURAL_ONLY` and moves no source or physics ledger row.

## Opening bookend

K461 accepts three possible rank-one routes. Direct M-orthogonal-complement
positivity is the only route whose count kernel, physical complement and
same-form K162 carrier are already serialized by K156, K165, K162 and K450.
K456/K457 now serialize the trial action column and residual, but K458 proves
those data do not determine the complete complement. K169 supplies a native
neutral-cluster threshold member and an upper cap on a possible margin, not a
Q lower floor. The missing composition is therefore: if the true Q floor and
the cross-column norm are later supplied on the same form, do they close both
the count and the center-zero coercivity field required by K461?

The strongest alternative is a same-form Lehmann--Goerisch count. It remains
available if the direct Q inequality fails. A finite independent rebuild or a
finite contour is not admitted as the same fixed limiting form.

## Exact theorem

Let `R` be a self-adjoint form with positive physical Gram `M`. For an
M-normalized trial vector `u`, put

```text
rho = R[u,u],              P=|u><u|_M,              Q=1-P.
```

Assume exact or outward-certified data

```text
rho < b < beta,
Q R Q >= beta Q_M                       on the complete charge sector,
|| Q(R-rho M)u ||_(Q,M-dual) <= eta.
```

Equivalently `Q(R-bM)Q >= (beta-b)Q_M>0`. Relative to
`span(u) direct-sum u^(perp_M)`, the pencil `R-bM` has a positive Q block.
Its scalar Schur complement is

```text
rho-b - ell* (Q(R-bM)Q)^(-1) ell < 0.
```

Congruence therefore gives exactly one negative direction:

```text
rank 1_(-infinity,b)(R,M)=1.
```

The same premises give, for `v=a u+q`,

```text
R[v,v] >= rho |a|^2 - 2 eta |a| ||q||_M + beta ||q||_M^2.
```

The lower eigenvalue of that scalar two-by-two form is

```text
lambda_- = (rho+beta-sqrt((beta-rho)^2+4 eta^2))/2.
```

Thus `R>=lambda_- M`; any rational shift `s` whose outward lower evaluation
satisfies `lambda_-+s>0` proves the center-zero shifted coercivity demanded by
K461. This composes the count and coercivity but does not evaluate any native
constant.

## Exact nonidentity-M control

Use

```text
M = [[1,1,0], [1,2,0], [0,0,1]],
R = [[-2,-1/2,0], [-1/2,3,0], [0,0,3]].
```

The vectors `u=e1`, `q1=(-1,1,0)`, `q2=e3` are M-orthonormal. In those
coordinates the form is

```text
[[-2, 3/2, 0], [3/2, 2, 0], [0,0,3]].
```

At `b=0`, `rho=-2`, `beta=2`, and `eta=3/2`. The discriminant is exactly
`25`; hence `lambda_-=-5/2`. The generalized spectrum is
`(-5/2,5/2,3)`, the pencil inertia is `(1,0,2)`, and shift `s=3` gives the
positive coercivity floor `1/2`. This is an exact control, not a native K162
packet.

A second control uses `rho=-1`, `b=0`, `beta=2`, `eta=1`, and shift `2`.
Its discriminant is the nonsquare integer `13`; 16-bit dyadic square-root
rounding encloses both `lambda_-` and the positive shifted floor outward.
Thus the executable checks genuinely outward arithmetic rather than relying
only on the first control's perfect-square discriminant.

## Substitution boundary

- K169's `E_ref(q)+5/2` is a threshold-set member and margin cap. It is not
  `beta`, does not exclude hidden discrete Q modes, and cannot enter the
  theorem as a complete Q floor.
- A K447/K453 finite independent rebuild is not a restriction of the fixed
  limiting K139 form. Its finite inertia, Rayleigh value or gap is a control,
  not a native certificate.
- K456/K457's complete trial column and residual can supply the same-form
  cross bound `eta` only after numerical enclosure. They cannot supply the
  Q-Q lower bound.
- A finite Ritz count cannot substitute for a complete charge-sector count.

## Closing bookend

The exact composition is complete and hostile-testable. The native constants
remain open: no fixed-K162 `rho`, rational `b`, complete Q floor `beta`,
same-form cross norm `eta`, or certified center-zero shift is evaluated here.
Consequently K461 remains false and no K152 interval is emitted.

The decisive successor is one direct same-form K162 block packet: evaluate a
trial Rayleigh value, choose `rho<b` strictly below the K169 member, prove
`Q R Q>=beta Q_M` on the complete M-orthogonal complement with `beta>b`, and
enclose the same action-column cross norm. Success immediately returns both
rank one and a coercive shift through this theorem. A certified nonpositive Q
witness should instead trigger the same-form Lehmann--Goerisch route.

Claim ceiling: exact generalized M-Hilbert composition theorem and exact
nonidentity-M control only. No native K162 count, coercivity value, K152
interval, source, ledger, canon, paper, public, Born, prediction,
confirmation, or physical GU conclusion follows.

## Reproduction

```bash
python3 tests/channel-swings/k463_k152_complement_coercivity_composition.py --demo
python3 tests/channel-swings/k463_k152_complement_coercivity_composition_probe.py
python3 tests/channel-swings/k463_k152_complement_coercivity_composition_probe.py --selftest
```
