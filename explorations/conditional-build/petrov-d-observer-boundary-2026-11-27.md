---
status: exploration
doc_type: structural-result
created: '2026-11-27'
tier: T2
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Evidence only; no verdict change.
title: Type-D observer limits have no universal positive escape fraction
program_target: LB-CLASS
expected_delta: Test whether the II/III compact-mass bounds extend to type D; exhibit exact opposite behaviors
  if not.
actual_delta: One smooth equivariant Julia point-law has a type-I approach to D with all probability retained
  and another approach to the same D tensor with all mass escaping. Thus no positive universal escape
  fraction extends to D; the exact-D no-law obstruction remains.
class_covered: Actual complex binary quartics encoding real4D Lorentz Weyl tensors, exact SL2C action
  and normalized probabilities on future-unit timelike observer spaceH3. Pointwise Weyl-only laws; no
  spacetime PDE or black-hole field equation assumed.
premises:
- explorations/conditional-build/petrov-probability-selection-2026-11-26.md
- lab/sources/source-claim-register.yaml#SC-GEO-03
- Classical smooth Julia covariant on squarefree complex quartics, Stoll-Cremona2003
source_bridge:
  status: absent
  reason: GU supplies neither a required pointwise Weyl-only timelike observer probability nor a bridge
    to physical observation, bulk charge or metric-fibre measure.
kill_condition: Failure of exact quartic invariance or covariance/limit calculation cancels the counterexample.
  No candidate-GU kill is intended.
classification: INTERNAL_STRUCTURAL_ONLY
---

# Type D is different from types II and III

Basis: `c083eefcb2c6196f3a686596aeb2c596c2bdb42a`.

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Test whether the II/III compact-mass bounds extend to type D; exhibit exact opposite behaviors
  if not.
actual_delta: One smooth equivariant Julia point-law has a type-I approach to D with all probability retained
  and another approach to the same D tensor with all mass escaping. Thus no positive universal escape
  fraction extends to D; the exact-D no-law obstruction remains.
```

The old type-II/III bounds are universal over approaches and laws. That kind
of **positive escape fraction cannot be extended to type D**. We give two
paths to the same nonzero type-D tensor for one smooth covariant point-law:
all probability stays on one path and all probability escapes on the other.
This is compatible with the already-owned absence of any equivariant
probability at the exact type-D tensor.

```gu-typed-objects
result: type-D nonescape and escape counterfamilies for the same observer law
carrier: real4D Weyl tensors encoded by actual complex binary quartics; H3 future unit timelike observers LAYER=observed BRIDGE=none CHIRALITY=N/A
pairing: fixed downstairs Lorentz metric, orientation and time orientation; positive Borel probability ON=observed_H3
real_structure: PSL2C proper orthochronous Lorentz action; not ambient K95 or K77
grading: Petrov root multiplicity, not fermion or source grading
action_owner: repository-construction mathematical comparator; no source action selected
target: continuous equivariant Weyl-only observer law MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** See
> [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> A pointwise Weyl clock is not the source observation contraction or a
> physical state prescription. This test has no source-necessity bridge.

## 1. Exact forms and a compact stabilizer

Use the previous left action `rho(g)f(z)=f(g^-1 z)` and observer action
`X -> g X g*` on positive Hermitian determinant-one matrices. Put

    f_e = e x^4 + x²y² + e y^4,   0<e<1/2,
    f_D = x²y².

The binary discriminant is `16e²(1-4e²)²`, so every f_e is type I;
f_D is nonzero type D. The determinant-one matrices

    R=diag(i,-i),       S=[[0,i],[i,0]]

fix the actual f_e, not only its root set. They generate a projective
Klein four and lie in SU2. Their common fixed point on H3 is exactly
`o=I`: R forces a fixed Hermitian matrix to be diagonal, S equates its
two diagonal entries, and positivity/determinant1 give I.

Let J(f) be the classical smooth equivariant Julia covariant on type I,
reused from the prior theorem. Covariance forces J(f_e) to be fixed by R
and S, hence J(f_e)=o. Therefore the single globally defined type-I law

    P(f)=delta_(J(f))

satisfies P(f_e)=delta_o. It retains mass1 in every compact neighborhood
of o along f_e -> f_D. Thus the sharp universal compact-mass upper bound
at D is the trivial1; the universal forced escape lower bound is0.

## 2. The same law can lose all mass at the same tensor

For t>=2 choose e=t^-6 and `g_t=diag(t,t^-1)`. Exact substitution gives

    rho(g_t) f_(t^-6) = t^-10 x^4 + x²y² + t^-2 y^4 -> f_D.

These are still type I because g_t is invertible. Yet equivariance gives

    J(rho(g_t) f_(t^-6))=g_t o g_t*=diag(t²,t^-2).

Its rapidity is2log(t), which tends to infinity; it leaves every compact
subset of H3. P on this path therefore assigns eventually zero mass to
any given compact set. These are opposite limiting behaviors of the
**same smooth covariant law**, not an arbitrary choice of unrelated
measures at each point. Neither path supplies a probability value at D.

More generally, replacing t^-6 by t^-a keeps the same D limit precisely
when a>4. The source supplies no such scaling path or probability law;
this is a mathematical condition for the explicit example only.

## 3. Every intermediate retained mass is also possible

For completeness, let Delta be the binary discriminant, and on type I put
`R(f)=log(1+1/|Delta(f)|)`. This positive smooth scalar is SL2C invariant.
Let U_(u,R) be uniform hyperbolic surface probability on the geodesic
sphere of radius R about u. For any fixed alpha in[0,1],

    P_alpha(f)=alpha delta_(J(f))+(1-alpha) U_(J(f),R(f))

is a continuous equivariant probability law. On the balanced f_e path,
J=o and R tends to infinity. Every compact neighborhood of o therefore
has mass exactly alpha eventually. This constructs all retained fractions,
not a physical randomization prescription. Its chosen function R and alpha
are comparator data and are not added to the GU candidate choice budget.

## 4. Why no law exists at the endpoint

The exact type-D tensor f_D is fixed by the noncompact group
`diag(t,t^-1)`, t>0. The proper Lorentz action on H3 cannot support a
probability invariant under that group: if a compact K has mass>1/2,
every measure-preserving element belongs to the compact transporter of K
with itself. This is the prior pointwise obstruction, reused unchanged.
The balanced path's weak limit delta_o breaks the enlarged type-D
stabilizer; a pathwise probability limit is not an equivariant endpoint law.

The old II/III argument bounded the number of stabilizers that can stay in
a compact transporter by2 or1. At D, all four exact Klein elements can
remain in SU2 along the balanced path. That is the precise failed premise
of the attempted positive escape-bound extension.

## 5. Black-hole and source limits

Type D is relevant to idealized stationary black-hole curvature, but these
are pointwise tensors, not lifted Schwarzschild/Kerr sections or solutions
of GU's printed endpoint. Classical principal-observer studies already
allow type-D rest observers; their existence does not select one invariant
observer or normalized observer distribution from Weyl data alone.
[Wylleman–Costa–Natario2021](https://arxiv.org/abs/2007.15384) is the primary
comparison, not evidence for a GU physical identification.

The Julia covariant and its smooth type-I construction are established:
[Stoll–Cremona, On the reduction theory of binary forms](https://www.mathe2.uni-bayreuth.de/stoll/papers/reduction-part-1.pdf),
Proposition3.4 and sections4–5. The repo's prior report supplies the
same-action proof and its probability scope. This extension claims no
world novelty and does not equate Julia observers with every physical
principal-observer construction.

- **ESTABLISHED:** explicit all-retained and all-escaping paths to the same
  D tensor for one smooth equivariant law; all intermediate fractions for
  the stated family of laws.
- **RULED OUT:** a positive path-independent forced escape fraction at D
  for arbitrary equivariant observer probabilities. Exact-D pointwise
  normalization remains impossible in this class by the reused theorem.
- **NOT MODELED / UNDETERMINED:** physical clocks, hidden hair/bulk charges,
  black-hole stability or fidelity, source necessity, curvature-derivative,
  Ricci/matter/boundary inputs and metric-fibre probability transfer.

The exact probe checks the polynomial, group, discriminant and boost
formulas, not a numerical simulation of infinite-dimensional probabilities.
Topology, tightness and smooth covariance use the written argument and
reused Julia theorem. No new Lean or physical prediction claim. Choice
budget remains10/4/net6/0. No ledger verdict changes.
