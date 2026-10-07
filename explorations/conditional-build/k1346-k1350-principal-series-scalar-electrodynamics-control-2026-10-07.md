---
title: "K1346--K1350 principal-series scalar-electrodynamics control"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1346--K1350 principal-series scalar-electrodynamics control

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the narrow SC-META-53 question
whether the completed internal carrier itself forbids one interacting gauge
control, positive constrained energy or a nonlinear invariant scalar map. The
U(1) scalar-electrodynamics construction is `INTERNAL_STRUCTURAL_ONLY` and has
no GU claim effect.

Scope: a repository-owned abelian scalar-electrodynamics control on the
ultrastatic globally hyperbolic spacetime `R x T3`, with K1335's supplied
nontrivial regular-imaginary spherical principal-series Hilbert space
`H_ps=L2(K/M)` as matter fibre. Its U(1) gauge group, charge, mass, quartic
coupling and action are repository choices. It is not I1B, Upsilon_B, I2B or a
source-derived observed theory.

```gu-typed-objects
result: one Hilbert-valued scalar-electrodynamics action, interacting Gauss/BRST/classical-BV/boundary-BFV algebra, positive constrained energy, positive nonzero vacuum-linearized cohomology and bounded nonlinear invariant scalar map
carrier: zero-mean U(1) connections plus H1(T3;H_ps) matter, H_ps=L2(K/M) LAYER=toy CHIRALITY=N/A
pairing: positive scalar-electrodynamics Hamiltonian on the declared classical Gauss quotient ON=repository_control
real_structure: real U(1) gauge field with complex unitary principal-series matter fibre
grading: abelian ghost, field, antifield and boundary-BFV grading; physical Hilbert completion unconstructed
action_owner: repository-construction -- one covariantly coupled U(1) scalar-electrodynamics action with imported e,m,lambda
target: whether the principal-series carrier alone obstructs a joint interacting gauge control or nonlinear invariant scalar map MAP-TYPE=evaluation
```

## Preflight bookend

K1341--K1345 show separate feasibility: free transverse Maxwell cohomology,
ungauged defocusing scalar evolution, and a sharp no-go for nonzero bounded
**linear** fully `G`-invariant scalar exports. They do not test whether the
three ingredients coexist in one action. The cheapest structural discriminator
is one ordinary covariantly coupled model, not an attempted reconstruction of
the unreleased GU physical complex.

The positive route constructs exact gauge covariance, Euler/Noether/Gauss
algebra, positive constrained energy and a nonlinear invariant scalar. The
negative route would find an incompatibility caused solely by the internal
principal-series carrier. Neither route can establish source ownership. A
direct I1B/Upsilon_B/I2B transfer remains the strongest source-native
alternative, but it lacks a typed field/action map to this carrier and cannot
be manufactured by renaming the control.

## K1346: one genuinely coupled action

Let `A` be a real U(1) connection and `phi` an `H_ps`-valued complex scalar.
For nonzero `e`, positive `m` and positive `lambda`, set

```text
D_mu phi = partial_mu phi - i e A_mu phi,
F_mu_nu = partial_mu A_nu - partial_nu A_mu,

L = -1/4 F_mu_nu F^mu_nu
    +1/2 Re <D_mu phi,D^mu phi>
    -m^2/2 ||phi||^2-lambda/4 ||phi||^4.
```

Under `A -> A+d chi` and `phi -> exp(i e chi)phi`, one has

```text
D' (exp(i e chi)phi) = exp(i e chi) D phi,   F'=F.
```

The internal principal-series action commutes with the local phase and is
unitary, so `D(pi(g)phi)=pi(g)Dphi`. Thus the same action is locally gauge
invariant and internally `G`-equivariant. Expanding `||Dphi||^2` produces the
current coupling and the `e^2 A^2 ||phi||^2` seagull term. This is not the sum
of K1341's free Maxwell action and K1343's ungauged scalar action.

The smooth finite-Fourier, K-finite fields form a common algebraic core. The
energy form uses `A,phi in H1` and `E,Pi in L2`. These declarations make the
coupling well typed; they do not prove global large-data gauge evolution.

## K1347: interacting Gauss, BRST, BV and boundary BFV algebra

The Euler operators have the schematic exact form

```text
E_phi  = -D_mu D^mu phi + m^2 phi + lambda ||phi||^2 phi,
E_A^mu = partial_nu F^{nu mu} - e Im<phi,D^mu phi>.
```

Gauge invariance gives the Noether identity

```text
-partial_mu E_A^mu + Re<E_phi,i e phi> = 0,
```

and the Hamiltonian moment map is the interacting Gauss constraint

```text
G = div E - e Im<phi,Pi> = 0.
```

With odd ghost `c`, the minimal BRST rules

```text
sA=d c,   s phi=i e c phi,   s c=0
```

square to zero by graded Leibniz and `c^2=0`. The classical minimal BV action

```text
S_BV = S_SED + integral(A* d c + 2 Re<phi*,i e c phi>)
```

satisfies the classical master equation because the action is invariant and
the U(1) gauge algebra is closed and abelian. The Koszul--Tate component sends
field antifields to the Euler operators and the ghost antifield to the Noether
identity. On a Cauchy boundary,

```text
Omega_boundary = integral_T3 c G,   {Omega_boundary,Omega_boundary}=0.
```

This is an interacting classical algebraic BRST/BV-BFV control. It is not a
proof that the functional Koszul--Tate sequence is globally resolving, that
the nonlinear orbit space is a smooth closed Hilbert quotient, or that an
interacting Green system exists.

## K1348: positive constrained energy and the linearized boundary

On the energy phase space the Hamiltonian is

```text
H = 1/2||E||_2^2 + 1/2||B||_2^2
  + 1/2||Pi||_2^2 + 1/2||D phi||_2^2
  + m^2/2||phi||_2^2 + lambda/4||phi||_4^4.
```

Every term is nonnegative. In the zero-mean trivial-holonomy connection sector,
which removes the harmonic flat-potential zero modes, `H` vanishes only at the
vacuum modulo the declared gauge group. The Gauss surface and `H` are gauge
invariant, so the energy descends to classical gauge classes. The surface is
not empty: `A=0`, nonzero smooth real-line-valued `phi`, `Pi=0`, and transverse
`E` give explicit nonvacuum classes.

At the vacuum, the BRST complex linearizes to zero-mean Maxwell plus a massive
complex `H_ps`-valued scalar. Its degree-zero physical modes contain two
transverse photon polarizations per nonzero spatial mode and all massive
matter modes; the quadratic Hamiltonian is positive on nonzero classes.

The nonlinear conclusion is narrower. The positive interacting energy and
formal Gauss reduction exist, but closed nonlinear quotient geometry, global
large-data evolution, quantization and a positive physical Hilbert cohomology
remain unproved.

## K1349: a nonlinear scalar map evades the linear theorem

K1344's Riesz argument applies to bounded **linear** maps. The radial map

```text
O(phi) = ||phi||_Hps^2 / (1+||phi||_Hps^2)
```

instead has codomain `[0,1)`, is nonzero for `phi != 0`, and obeys

```text
O(exp(i e chi)phi)=O(phi),    O(pi(g)phi)=O(phi).
```

Its derivative is

```text
D O_phi[h] = 2 Re<phi,h>/(1+||phi||^2)^2.
```

It is nonlinear because `O(-phi)=O(phi)` while a linear scalar functional is
odd. Thus it needs no chosen internal Riesz covector and preserves the full
internal unitary action. A normalized nonnegative spatial weight can average
the pointwise density to a bounded scalar field observable.

This closes only the map-class question. The repository chose the norm-radial
map; the source did not. No observed-state semantics, apparatus, empirical
export or prediction is constructed.

## K1350: joint control and remaining physical boundary

The 26-row census has eighteen satisfied rows, four conditional rows and four
missing rows. Relative to K1345, a single repository action now jointly
realizes nonzero gauge-matter interaction, classical Gauss/BRST/BV-BFV algebra,
positive constrained energy and a bounded nonlinear invariant scalar map.
This excludes a carrier-only incompatibility for the named control.

The conditional rows keep the hard boundaries visible: positive nonlinear
energy is not a closed nonlinear physical Hilbert cohomology theorem; the
positive nonzero cohomology statement is vacuum-linearized; and the nonlinear
scalar has no source observation semantics. Four rows remain missing:

- a source-owned charge or chamber law;
- identification with one source-action-derived interacting constraint
  complex;
- a closed global nonlinear BV-BFV quotient with positive physical Hilbert
  cohomology; and
- a source-owned observed-state and export map.

K1145/K1150 remain `0/7` for native candidates. SC-ACT-01/02/06 remain
`ASSERTS`, SC-META-53 remains `UNCERTAIN`, and LT-SM8/LT-GR6b/RA-F1/AC-F1
remain `NEEDS`.

## Postflight hostile review

The strongest overclaim is to call the classical BV master equation a complete
functional BV-BFV theory. It is only the exact algebraic minimal complex on the
declared smooth core. The strongest analytic objection is that positive energy
does not by itself prove global large-data Maxwell--matter evolution or closed
nonlinear gauge orbits. Both ceilings are retained.

The strongest source objection is decisive: the fields and U(1) action are not
identified with the released GU action. The construction is therefore a
control, not a completion of SC-ACT-01/02/06. The strongest observation
objection is that a radial scalar can be mathematically invariant without being
the source's observation/pullback or any measured quantity. K1349 changes the
map class; it does not supply physical semantics.

The useful positive result survives all three objections: the principal-series
Hilbert carrier alone does not forbid one internally equivariant interacting
gauge control, positive constrained classical energy, positive nonzero
vacuum-linearized cohomology, or a nonzero bounded nonlinear invariant scalar.

## Exact next input

Preserve the joint control and its ceilings. The physical frontier now needs a
typed bridge from the released GU fields and first-order action into one
Lorentzian interacting constraint complex, followed by a closed nonlinear
orbit/KT resolution, global causal evolution or Green theory, and positive
physical Hilbert cohomology. The observation side must derive a source-owned
map with physical semantics; merely reusing the radial scalar is not such a
derivation.
