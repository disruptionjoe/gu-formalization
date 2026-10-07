---
title: "K1341--K1345 principal-series gauge, interaction and observation controls"
status: active_research
doc_type: conditional_research_result
created: "2026-10-07"
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
claim_effect: none
---

# K1341--K1345 principal-series gauge, interaction and observation controls

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only for the narrow SC-META-53 question
whether the completed internal carrier itself forbids gauge reduction,
nonlinear positive evolution or scalar export. The Maxwell, semilinear-wave
and Riesz controls are `INTERNAL_STRUCTURAL_ONLY` and have no GU claim effect.

Scope: repository-owned controls on the ultrastatic globally hyperbolic
spacetime `R x T3`, with K1335's supplied nontrivial regular-imaginary
spherical principal-series Hilbert space `H_ps=L2(K/M)` as internal fibre.
The Maxwell and nonlinear scalar controls are different actions. Neither is
the GU action, and no source-owned observation map is supplied.

```gu-typed-objects
result: free Hilbert-valued Maxwell detour/BRST complex, positive transverse quotient, defocusing nonlinear wave, bounded scalar-export classification and joint admission replay
carrier: zero-mean spacetime one-forms valued in H_ps plus a separate scalar H1(T3;H_ps) carrier, H_ps=L2(K/M) LAYER=toy CHIRALITY=N/A
pairing: positive transverse Maxwell energy and separate defocusing scalar energy ON=repository_controls
real_structure: real spacetime fields with complex unitary principal-series internal fibre
grading: Maxwell ghost/potential/Euler/Noether detour grading; separate ungraded nonlinear scalar control
action_owner: repository-construction -- free abelian Maxwell and separate defocusing radial scalar actions after an imported regular charge
target: whether gauge reduction, local interaction or bounded scalar export is blocked by the internal carrier alone MAP-TYPE=evaluation
```

## Preflight bookend

K1336--K1340 prove only a trivial-constraint free scalar control. The next
question is not whether that control can be renamed physical, but which of the
missing ingredients fail already at carrier level. Three independent tests
are cheaper and more discriminating than inventing one unowned GU completion:

1. tensor a standard Maxwell detour complex with `H_ps` and test closed gauge
   reduction, causal Green structure and positive nonzero transverse modes;
2. add a local defocusing radial interaction to the scalar carrier and test
   positive global causal evolution; and
3. classify bounded linear scalar exports and test whether full internal
   `Spin_0(7,7)` invariance permits a nonzero one.

The first kill is a nonclosed gauge image or indefinite transverse energy.
The second is failure of the cubic map on the energy domain or loss of
coercive conserved energy. The third is a nonzero invariant vector in the
nontrivial irreducible principal series. Positive controls can exclude only
the corresponding carrier-level obstruction; they cannot compose themselves
into one source-owned action.

## K1341: a nontrivial free Maxwell detour/BRST control

Let `M=R x T3` and tensor the abelian Maxwell detour sequence with `H_ps`:

```text
Omega0(M;H_ps) --d--> Omega1(M;H_ps)
  --delta d--> Omega1(M;H_ps) --delta--> Omega0(M;H_ps).
```

The identities `d^2=0` and `delta^2=0` give

```text
(delta d)d=0,             delta(delta d)=0.
```

Thus the Maxwell Euler operator has the exact gauge and Noether identities.
In BRST notation `sA=dc`, `sc=0`, so `s^2=0`. Lorenz gauge adds `d delta` and
gives the normally hyperbolic one-form wave operator `Box_1 tensor I_Hps`.
Finite spatial Fourier sums with K-finite internal values give a common core.

For the zero-mean control, every spatial mode has `k != 0` and

```text
P_T(k)=I-k k^T/|k|^2,      rank P_T(k)=2.
```

The harmonic `k=0` flat-potential sector is explicitly excluded rather than
called positive. The remaining spatial Laplacian has Poincare floor one on
the `2pi` torus.

## K1342: closed transverse quotient, causal Green and boundary reduction

The zero-mean Hodge splitting is

```text
Omega1_0(T3;H_ps)=closure(im d) orthogonal_sum ker delta.
```

The Poincare inequality bounds the inverse gradient on mean-zero scalars, so
`im d` is closed. Every gauge class has the unique Coulomb representative
`P_T A`; its nonzero-mode fibre is `k^perp tensor H_ps`. The reduced free
space is therefore nonzero and infinite-dimensional, with two transverse
polarizations per nonzero spatial mode. Its energy

```text
E=1/2 (||E_T||^2+||curl A_T||^2)
```

is positive and coercive on the declared zero-mean energy space.

The Lorenz-gauge advanced and retarded Green operators are the one-form wave
Green operators tensored with `I_Hps`, hence retain causal support. The
constraint propagates from `delta Box_1=Box_0 delta`. On the Gauss-law
surface the standard Cauchy form annihilates infinitesimal gauge directions
and descends to transverse classes. This is a genuine nontrivial free gauge
quotient, but only for the repository Maxwell control.

## K1343: a separate defocusing nonlinear control

On the scalar carrier take

```text
u_tt-Delta u+m^2 u+lambda ||u||_Hps^2 u=0,   m>0, lambda>0.
```

Its potential and energy are

```text
V(u)=m^2/2 ||u||^2+lambda/4 ||u||^4,
E=1/2||u_t||_2^2+1/2||grad u||_2^2
  +m^2/2||u||_2^2+lambda/4||u||_4^4.
```

The vector-valued Sobolev estimate `H1(T3;H_ps) -> L6` makes the cubic
Nemytskii map locally Lipschitz from `H1` to `L2`. Standard energy-subcritical
local theory, together with the positive conserved defocusing energy, gives
global finite-energy evolution. The pointwise spacetime nonlinearity retains
finite propagation speed. For every internal unitary `U`,

```text
N(Uu)=lambda ||Uu||^2 Uu=U N(u).
```

The interaction therefore commutes with the principal-series action. It is
not coupled to K1341's gauge complex and is not source-owned.

## K1344: bounded scalar observation requires a symmetry-breaking choice

By Riesz representation, every bounded linear scalar export from `H_ps` is

```text
O_eta(v)=<eta,v>,       ||O_eta||=||eta||.
```

For the internal unitary representation,

```text
O_eta(pi(g)v)=O_(pi(g)^* eta)(v).
```

Thus `O_eta` intertwines the full group with the trivial scalar
representation exactly when `eta` is invariant. K1335 fixes a nontrivial
irreducible regular-imaginary principal series, so its invariant-vector space
is zero. The only fully `G`-invariant bounded linear scalar export is
therefore zero.

Every nonzero chosen `eta` still defines a bounded export and commutes with
the spacetime scalar evolution; it selects an internal covector and preserves
at most its stabilizer. The theorem does not address nonlinear, unbounded or
nontrivial-target observation maps. It proves a precise selection cost, not a
global observation no-go.

## K1345: separate feasibility is not joint physical admission

The expanded 21-row control census has fifteen satisfied rows, two
conditional rows and four missing rows. The carrier supports the prior free
scalar package, a nontrivial free Maxwell detour complex with closed positive
transverse quotient, a separate defocusing nonlinear positive causal flow,
and an exact classification of bounded scalar exports.

The two conditional rows are deliberately scoped: positive nonzero
cohomology belongs only to the repository-owned free Maxwell quotient, and a
nonzero scalar export exists only after choosing `eta` and reducing internal
symmetry. Four load-bearing rows remain missing:

- source-owned charge or chamber selection;
- one source-action-derived **interacting constraint** KT/BV-BFV complex on
  one common Lorentzian domain;
- positive nonzero cohomology of that joint GU physical quotient; and
- a source-owned observed-state/export map.

The Maxwell and nonlinear scalar actions cannot be added as if they were one
source action. K1145/K1150 therefore remain `0/7` for native candidates.

## Postflight hostile review

The strongest overclaim is that K1342 supplies GU physical cohomology. It
supplies free Maxwell transverse modes after a zero-mean restriction, not the
cohomology of Weinstein's interacting action. The strongest composition error
is to combine K1341's constrained free theory with K1343's unconstrained
nonlinear theory. They are independent controls with different actions.

The strongest contrary construction is a source-owned interacting constraint
whose quotient is nonclosed, indefinite or empty even though both controls
pass separately. Nothing here excludes that. The observation theorem is also
narrow: a nonlinear or nontrivial-target map can evade the scalar Riesz
boundary, but must still be source-owned and typed.

The weakest analytic seam is the infinite-dimensional internal target in the
semilinear equation. The argument uses only Hilbert-norm unitarity, the
vector-valued `H1 -> L6` estimate, local Lipschitz cubic control and conserved
coercive energy; the finite certificates test algebraic identities and hostile
claim ceilings rather than substituting for those standard theorems.

SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains `UNCERTAIN`, and
LT-SM8/LT-GR6b/RA-F1/AC-F1 remain `NEEDS`. No source, ledger, canon, paper,
prediction, confirmation or public status moves.

## Exact next input

Preserve all three scoped controls. The next physical admission step must
derive one interacting constraint/KT/BV-BFV complex from the released GU
action on one common Lorentzian domain and prove its closed range, causal
evolution, boundary reduction and positive nonzero physical cohomology. Its
observation map must either select and justify an internal covector/symmetry
reduction or provide a typed nonlinear or nontrivial-target alternative. The
separate Maxwell, scalar and export controls cannot substitute.
