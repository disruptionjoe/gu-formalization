---
title: "K1361--K1365 compact-charge graph-domain control"
status: active_research
doc_type: conditional-build-result
classification: INTERNAL_STRUCTURAL_ONLY
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1361--K1365 compact-charge graph-domain control

## Routing notice and claim ceiling

This packet follows the source-native route but constructs repository-owned
control mathematics. It does not identify K1356's coordinate circle with a
source-selected compact reduction, hypercharge, an observed particle charge,
or the source observation map. It does not move SC-ACT-01/02/06,
SC-META-53, LT-SM8, LT-GR6b, RA-F1, AC-F1, K1145/K1150, canon, the physics
ledger, a paper, a prediction, or a confirmation.

```gu-typed-objects
result: minimal spatially local circle-gauge completion, radial-domain preservation, separate scalar-flow propagation, and an ordinary-energy noncoercivity counterexample
carrier: completed compact charge Hilbert sum over integer weights with spatial H1 charge-graph domain on T3 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert sum and Sobolev graph pairing ON=repository_owned_control_domain
real_structure: complex Hilbert charge representation with self-adjoint integer generator and real gauge parameter
grading: integer compact charge, spatial Sobolev order, and finite charge-graph order
action_owner: repository-construction -- no source action selects the compact reduction or supplies charge-graph coercivity
target: SC-META-53 conditional analytic control boundary MAP-TYPE=evaluation
```

The question is narrower and analytic. K1358 makes the compact charge `Q`
self-adjoint and unbounded. K1359's interacting gauge/BRST/BV-BFV identities
close on the algebraic K-finite core. Which completion is actually preserved
by spacetime-dependent circle gauge transformations and the existing radial
nonlinear flow, and does K1359's positive energy control the required charge
graph norm?

## K1361 — the minimal local-gauge graph domain

Write the completed compact picture as

```text
H_ps = direct_sum_(q in Z) H_q,
D(Q) = {v=sum_q v_q : sum_q q^2 ||v_q||^2 < infinity}.
```

On the spatial slice `Sigma=T3`, define

```text
X_Q^1 = {phi in H1(Sigma;H_ps) : Q phi in L2(Sigma;H_ps)}
```

with sum graph norm `||phi||_H1+||Q phi||_L2`. Joint spatial smoothing and
finite charge truncation prove that
`C^infinity(Sigma) algebraic_tensor H_Kfin` is dense in this completion.

For real `alpha in W1_infinity(Sigma)`, let

```text
(G_alpha phi)(x) = exp(i alpha(x) Q) phi(x).
```

Functional calculus gives `QG_alpha=G_alpha Q`, and approximation from the
dense core gives the weak derivative identity

```text
partial_j(G_alpha phi)
  = G_alpha(partial_j phi + i (partial_j alpha) Q phi).
```

Consequently `G_alpha` is a bounded automorphism of `X_Q^1`, with inverse
`G_minus_alpha` and the estimate

```text
||G_alpha phi||_X
  <= max(1,1+||grad alpha||_infinity) ||phi||_X.
```

Ordinary `H1(Sigma;H_ps)` is not enough. Choose orthonormal charge vectors
`e_(4n)` with `Qe_(4n)=4n e_(4n)` and

```text
v = sum_(n>=1) n^-1 e_(4n).
```

Then `v in H_ps` because `sum n^-2<infinity`, but `v notin D(Q)` because
`sum (4n)^2 n^-2=infinity`. The constant field `phi(x)=v` lies in ordinary
`H1`. For `alpha(x)=sin(x1)`, its transformed derivative contains
`cos(x1)Qv` and is not square integrable. Thus the charge graph term is
necessary, not decorative.

## K1362 — radial nonlinearities preserve the charge domain

Let

```text
N_f(v) = f(||v||^2) v,
```

where `f` is continuously differentiable and `f,f_prime` are bounded on
bounded intervals. For `v in D(Q)`, the scalar coefficient is invisible to
the internal operator, so

```text
Q N_f(v) = f(||v||^2) Qv.
```

Every unitary `U` on `H_ps` preserves the norm and hence
`N_f(Uv)=U N_f(v)`. In particular the pointwise local circle action obeys
`N_f(G_alpha phi)=G_alpha N_f(phi)`.

On a graph-norm ball, the difference is controlled by splitting

```text
Q(N_f(v)-N_f(w))
 = f(||v||^2) Q(v-w)
 + [f(||v||^2)-f(||w||^2)] Qw.
```

The mean-value theorem supplies the local graph-Lipschitz bound. K1343's
defocusing cubic is the exact instance `f(r)=lambda r`. The scalar radial
nonlinearity is therefore not the obstruction to completing the `Q` domain.

## K1363 — global charge-regular propagation for the scalar control

K1343 already proves global finite-energy evolution and finite propagation
for

```text
u_tt - Delta_T3 u + m^2 u + lambda ||u||_Hps^2 u = 0,
m>0, lambda>0.
```

Because `Q` acts only on the internal output vector, for every integer
`r>=1`,

```text
Q^r(||u||^2u) = ||u||^2 Q^r u.
```

Therefore `w_r=Q^r u` satisfies the linear equation

```text
(partial_t^2 - Delta_T3 + m^2 + lambda||u||^2) w_r = 0.
```

For smooth base solutions, the usual linear energy estimate on every finite
time interval propagates

```text
Q^r u(0) in H1(T3;H_ps),
Q^r u_t(0) in L2(T3;H_ps)
```

for all real times. Iterating in `r` preserves every admitted finite charge
graph order. The principal wave operator is unchanged, so the same causal
cone and finite-speed statement apply. These higher graph energies obey
finite-interval Gronwall bounds; they are not claimed conserved.

This is a completed global graph-domain theorem for the separate radial scalar
control. It is not a theorem for the dynamical gauge field, Gauss constraint,
or nonlinear KT/BV-BFV quotient.

## K1364 — positive coupled energy is not charge coercivity

The remaining domain gap is real. For the same charge witnesses, define

```text
phi_N(x) = sum_(n=1)^N n^-1 e_(4n)
```

as a constant field on `T3`, and set the gauge field, electric field, magnetic
field, and matter momentum to zero. Then

```text
||phi_N||^2 = sum_(n=1)^N n^-2 <= pi^2/6,
||Q phi_N||^2 = sum_(n=1)^N (4n)^2 n^-2 = 16N.
```

The spatial-gradient term vanishes, while the mass and quartic terms are
uniformly bounded. Hence K1359's ordinary positive energy admits no coercive
estimate of the form `||Qphi|| <= C(E)`, even on the algebraic core and even
in the zero-gauge sector. The seagull term does not repair this because it
vanishes when `A=0`; finite K-type truncations do not repair it without a
uniform estimate.

Three honest routes remain:

1. impose graph-regular initial data and prove its propagation for the fully
   coupled equations;
2. derive an action-owned positive regularizer such as `mu||Qphi||^2`; or
3. derive another source-owned coercive estimate controlling the complete
   charge graph norm.

The counterexample does not exclude any of those repairs and is not a no-go
for a source-selected alternative.

## K1365 — admission replay

The bridge census now has 41 rows: 27 satisfied, four conditional, six
excluded, and four missing. Three rows move to satisfied: the completed local
gauge graph domain, radial nonlinear graph preservation, and global charge-
regular propagation for the separate defocusing causal flow. One implication
is newly excluded: ordinary positive coupled energy by itself does not control
the unbounded charge graph norm.

The four missing rows remain source selection/normalization on the observed
carrier, one source-action-derived interacting constraint complex, a closed
fully coupled nonlinear KT/BV-BFV quotient with positive physical Hilbert
cohomology, and a source-owned observed-state/export map.

## Hostile review

The strongest overclaim would be to call K1363 the requested interacting
closure. It is not: the wave is the separate repository radial scalar control,
and K1364 proves that the positive coupled energy does not supply the missing
charge coercivity. The strongest contrary construction is precisely the
zero-gauge sequence with bounded ordinary energy and divergent `Q` norm. The
weakest reproducibility seam is the functional-analytic passage from the
dense core to weak derivatives and higher graph orders; K1361 states the
approximation route and K1363 limits itself to smooth graph-regular data plus
finite-interval energy estimates.

No source selector, observed-particle assignment, graph-coercive GU action,
closed interacting physical quotient, or positive physical cohomology is
inferred.

## Exact next input

The compact route now needs two independent inputs. First, a source/action-
owned selector and normalization on the actual observed carrier, with proof
that the source constraint and observation maps preserve the completed `Q`
graph domain. Second, a fully coupled graph estimate: either propagate
graph-regular initial data through the Maxwell--matter/Gauss system or derive
an action-owned positive `Q` regularizer or equivalent coercive bound, then
construct the closed KT/BV-BFV quotient and test positive nonzero physical
Hilbert cohomology.

The independent challenger remains a typed nonlinear, differential, integral,
or distributional map from released source section spaces to the principal-
series carrier, with declared domain, equivariance reduction, action owner,
and observed semantics.
