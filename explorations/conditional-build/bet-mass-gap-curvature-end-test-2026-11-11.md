---
title: "BET-MASS-GAP: curvature-square transverse modes and asymptotic ends"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: BET-MASS-GAP
tier: T2
expected_delta: "Test one speculative observed curvature-square family and its localized-background repair for a classical quadratic gap."
actual_delta: "Active bet: finite-energy static R3 backgrounds are flat; a stationary constant Cartan background retains a gapless neutral sector. Exterior and decaying-potential controls do not repair the threshold. No quantum mass-gap or GU verdict."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# A local curvature mass matrix does not establish a global quadratic gap

**Result.** One explicitly **SPECULATIVE** observed compact-gauge
curvature-square action family has gapless physical transverse fluctuations
at its flat vacuum. The useful follow-through is global: any static purely
magnetic stationary background in this family that is gauge-trivial outside
a compact set still has zero in the essential spectrum of its admitted
reduced selfadjoint Hessian. A bounded decaying transverse potential also
cannot open a positive gap. The finite-energy virial identity further forces
every smooth source-free static magnetic R3 background to be flat. An actual
nondecaying constant Cartan magnetic background is stationary, but its
parallel neutral sector still has the full gapless continuum. Its infinite
background energy is explicit. These results constrain this candidate and its
asymptotic repairs; they do not test the nonperturbative quantum Yang-Mills
mass gap or decide the source mechanism.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: BET-MASS-GAP
tier: T2
expected_delta: Distinguish a typed classical quadratic gap from curvature eigenvalues and quantum mass gap.
actual_delta: One speculative action family tested; virial forces finite-energy static R3 backgrounds flat, while an actual constant Cartan background retains a gapless neutral sector.

```gu-typed-objects
result: curvature-square-end-gap-test
carrier: observed adjoint-valued one-form for a declared compact Lorentz-inert gauge group LAYER=toy CHIRALITY=N/A
pairing: positive Ad-invariant Lie-algebra form and spatial L2 norm; Lorentzian action is indefinite ON=declared_carrier
real_structure: real compact Lie algebra, complexified for spectral analysis
grading: temporal constraint and spatial transverse fields, not family grading
action_owner: repository-construction -- SPECULATIVE observed Yang-Mills curvature-square family
target: reduced spatial Hessian and its essential spectrum MAP-TYPE=quotient
```

## 1. Source route and the single guessed family

SC-GEO-58 **DISAVOWS** a separate fundamental Higgs. The
[source steelman](../../lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md)
locates the proposed quadratic/quartic mechanism in the curvature of an
ad-valued one-form. SC-GEO-55 **ASSERTS** displacement from gauge-rotated
Levi-Civita. Neither source claim selects the compact positive observed
action used here. The native indefinite chimeric pairing, soldered adjoint
horn, moving observation and coupled field equations are not replaced by
this comparator.

The existing
[MD1 contraction](../../lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md)
gives, for an observation section s(x)=(x,g(x)),
`c_mu=C_mu(s(x))+C_I(s(x)) partial_mu g^I`. This is one observed
one-form, not extra scalar multiplets. Curvature is natural under pullback:

`F_(s*C)=s*(dC+C wedge C)=s*F_C`.

This uses the exterior derivative and wedge product, not a projection to
horizontal components. It does **not** identify `s*(*_Y F)` with
`*_X(s*F)` or derive an observed action by pulling back an ambient volume
density. The note below therefore chooses its observed action explicitly.
The probe checks a nonabelian curved-section example where dropping the
vertical contraction fails the curvature equation.

**Variant MG1, SPECULATIVE.** On Minkowski X=R^(1,3) with signature
(-+++), choose a nonzero compact Lie algebra with a positive invariant
inner product and a Lorentz-inert adjoint bundle. For c=s*(A+a), take

`S[c]=-(1/4) integral <F_mu_nu(c),F^mu_nu(c)> d^4x`.

Only c is dynamical here; A+a is a parametrization of the connection,
not two independent gauge fields. The coefficient is a fixed normalization,
not fitted. This is one familiar Yang-Mills structural ansatz, not a new
action or a certified member of C. The positive quantities are its spatial
magnetic energy and reduced kinetic metric; the Lorentzian action is not
positive. No scalar potential, mass term or guessed additional variant is
introduced. Source SRC2 already studies a curvature cross-term; its local
form is reused, not promoted to the complete physical Hessian.

## 2. Flat reduced operator: actual transverse modes survive

The flat c0=0 vacuum is stationary. Writing c=t a gives
`F=t da+t² a wedge a`, so the quadratic action is Maxwell in each
Lie-algebra direction. In temporal gauge the linear Gauss constraint is
`div dot(a)=0`; restrict to the transverse physical sector `div a=0`.
Then `ddot a+K a=0`, with `K=-Delta` on

`H_T={a in L2(R3,C3 tensor g_C): div a=0}`,
`Dom K=H2(R3) intersect H_T`.

At nonzero spatial momentum k, the magnetic symbol is
`M(k)=|k|² I-k k^T`. The longitudinal vector k is gauge, but the two
orthogonal polarizations have eigenvalue |k|². Removing the gauge direction
therefore does not remove the modes with arbitrarily small positive
frequency. The zero-momentum constant mode is not an L2 eigenfunction on
R3; the gap statement is about spectral infimum, not a normalizable zero
state. A finite box's lowest nonzero Fourier momentum is a size-dependent
infrared cutoff and tends to zero as box size increases.

For a static purely magnetic stationary background c0, the magnetic energy
`E(c)=1/2 ||F(c)||²`, with the two-form norm summed over i<j, has Hessian

`q_c0(a)=||d_c0 a||²+2 <F(c0),a wedge a>`.

This includes the derivative term omitted by a local algebraic mass-matrix
test. Gauge fixing and domain realization remain necessary. No claim of
stability follows from this formula alone.

## 3. Executed successor: compact curvature cores cannot open a global gap

### Source-free stationary finite-energy cores already reduce to flatness

There is a stronger model-specific restriction before the spectral test.
For a smooth static source-free stationary Yang-Mills connection on R3,
let `T_ij=sum_l <F_i_l,F_j_l>-(1/4)delta_ij sum_ab <F_ab,F_ab>`.
The Yang-Mills equation `D_j F_j_l=0`, Bianchi identity and invariant
inner product give `partial_j T_ij=0`. In three spatial dimensions
`sum_i T_ii=(1/4)sum_ab |F_ab|²`, exactly the magnetic energy density.

Integrate `partial_j(chi_R x_i T_ij)` for a smooth cutoff chi_R equal
to one on the radius-R ball, zero outside radius-2R and with
`|grad chi_R|<=C/R`. The resulting identity is
`integral chi_R trace T = -integral x_i (partial_j chi_R) T_ij`.
If the total magnetic energy is finite, the right side tends to zero:
`|x grad chi_R|` is uniformly bounded on the shell and |T| is bounded
by a constant times |F|². Dominated convergence on the left gives E=0.
Positivity then forces F=0 everywhere. This is the standard static virial
argument, not a novelty claim. Smoothness, no sources/singularities,
R3 geometry, positive Lie form and finite magnetic energy are essential.

Thus the proposed nontrivial compact-curvature stationary repair in MG1
is absent. The exterior proof below also applies to other admitted Hessians
with external cores, but does not construct a nonzero stationary solution
of this source-free action. Its flat case is genuinely realized.
Nondecaying fields escape the finite-energy hypothesis and are tested below.

### Exterior Hessian test, with the existence boundary retained

Assume c0 is time independent, purely magnetic, stationary, and can be
gauged to zero outside a compact spatial set. Assume a selfadjoint reduced
Hessian K exists on the closure of the background-Coulomb sector
`d_c0* a=0`, contains smooth compactly supported transverse fluctuations
in the trivial exterior, and agrees there with -Delta. No nontrivial
background satisfying these conditions is constructed or asserted to exist.
The flat case is already a realized example of the assumptions.

Choose a nonzero compactly supported smooth divergence-free field
`f=curl(phi e3) T`, where T is one fixed Lie-algebra direction, and
normalize its L2 norm to one. Let R tend to infinity and choose centers
x_R so the support balls of

`f_R(x)=R^(-3/2) f((x-x_R)/R)`

lie wholly in the trivial exterior and escape every fixed compact set.
Then `||f_R||=1`, `div f_R=0`, and
`||K f_R||=R^(-2)||Delta f|| -> 0`.

These are actual reduced directions: on their support d_c0*=d*, and
integration by parts makes them orthogonal to the closure of infinitesimal
gauge directions im d_c0. A nonzero such vector cannot itself belong to
that closed gauge subspace. Escaping supports imply weak convergence to
zero by the L2 tail bound. They form a singular Weyl sequence, proving
`0 in spectrum_essential(K)` by
[Teschl, Lemma 6.17](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
Thus no bound `K>=m² I` with m>0 is possible. Negative bound states, if
present, do not restore a positive gap or stability.

The probe independently constructs a compact H2 polynomial curl fixture:
`phi=(1-x²)^4(1-y²)^4(1-z²)^4` on the cube, zero outside. Its needed
traces vanish, so no distributional face terms enter its Laplacian. Exact
rational norms verify the scaling constants. The universal proof uses a
smooth bump; the polynomial is a control, not an implicit replacement of
the stated smooth domain. Standard local mollification preserves the curl
and can also put that control in the smooth test domain.

This reuses standard Weyl-sequence reasoning, not a claimed new theorem in
spectral theory. Earlier GU operator work already distinguishes curvature,
local mass and spectral gap; the present consumer is the reduced observed
curvature-square bet, with its gauge directions explicitly removed.

### Released extension: the full nonnegative continuum survives

The same method proves more than a zero spectral point. For any nonzero
k choose a constant vector w with `k cross w !=0` and a real smooth
compact bump phi. Form the exactly divergence-free packet

`a_R=curl(R^(-3/2) phi((x-x_R)/R) exp(i k.x) w) T`.

Its leading term is `i(k cross w) phi_R exp(i k.x)` and its remainder
has norm O(R^-1). Its norm therefore tends to the nonzero constant
`|k cross w| ||phi||`. The identity

`(-Delta-|k|²)(exp(i k.x)v)=exp(i k.x)(-Delta v-2i k.grad v)`

and commutation of curl with the Laplacian give residual O(R^-1).
Normalize, send the supports into the trivial exterior, and apply the same
gauge and weak-convergence argument. Hence
`[0,infinity) subset spectrum_essential(K)`. This does not exclude negative
core bound states. It rules out interpreting the zero result as an isolated
degeneracy above which this candidate might still have a positive threshold.

## 4. Decaying repair and a genuinely different sufficient input

For a separate, fully typed operator comparison let P be the orthogonal
Helmholtz projection to H_T and V(x) a bounded selfadjoint matrix potential
with `ess sup_(|x|>r)||V(x)|| -> 0`. Define

`K_V=-Delta+P V P` on `H2 intersect H_T`.

It is selfadjoint as a bounded symmetric perturbation. The same escaping
transverse functions satisfy

`||K_V f_R|| <= R^(-2)||Delta f|| + ess sup_(supp f_R)||V|| -> 0`.

The oscillatory packets also give every positive spectral value, so
`[0,infinity) subset spectrum_essential(K_V)`. P need not be local and V need not preserve transversality: its norm is at
most one, which is all the estimate uses. Thus even a positive, everywhere
nonzero but decaying potential does not give a uniform gap. For example
`V=m²/(1+|x|²) I` is positive pointwise and still fails a positive lower
bound. This is a statement about the declared operator, not a derivation
of V from the source or a new guessed action.

In contrast, if a bounded selfadjoint V satisfies `V>=m²I` uniformly,
then for every transverse u in the form domain,
`<u,K_V u>=||grad u||²+<u,V u> >=m²||u||²`.
That is a sufficient asymptotic/coercive input, not something a local
curvature value provides. Nonzero asymptotic backgrounds, different spatial
geometry or confinement may change the operator class and require their
own stability, gauge and domain analysis. The present theorem does not
exclude them.

## 5. Bet disposition and claim ceiling

### Genuine nondecaying successor: a parallel neutral direction

Keep the same single action family. Suppose a static stationary spatial
connection admits a nonzero globally parallel adjoint section T:
`D_c0 T=0`. Its norm is constant; normalize it. Curvature integrability
gives `[F(c0),T]=0`. For fluctuations `a_i=f_i T`,
`d_c0 a=df T` and `d_c0* a=-(div f) T`. The curvature part of the
full Hessian operator annihilates this sector because ad F kills T.
Thus the formal reduced Hessian acts as -Delta on transverse f. For the
spectral conclusion, assume an admitted selfadjoint reduced realization
containing all compact smooth neutral transverse fields and agreeing with
this formal Hessian on them. This is a separate domain assumption for the
nondecaying class; the trivial-exterior assumption in section 3 does not
supply it. The neutral Weyl packets then give the entire nonnegative
essential continuum without assuming every extension preserves the whole
neutral subspace. In the Cartan example, the neutral realization is the
free transverse Laplacian on H2 intersect H_T; the stated conclusion for
the full reduced operator retains the explicit domain assumption. T denotes a parallel bundle section,
not necessarily constant components in every gauge.

An explicit nondecaying example exists: in compact so(3), take a unit
Cartan generator T and `c0=B x T dy`, with constant nonzero B. Then
`F=B T dx wedge dy`, `D_j F_ji=0`, and `D T=0`.
This smooth local stationary solution is tested by compactly supported
relative variations; its infinite total magnetic energy on R3 means it is
not a finite-energy vacuum and does not contradict the virial result.
Its neutral L2 fluctuations are physical reduced directions and gapless.
No stability of the charged sectors is claimed; instability would not
restore a positive gap. This tests a genuinely nondecaying background
without adding or tuning another action variant.

Absence of a nonzero parallel adjoint section is necessary to evade this
particular obstruction, not sufficient for a gap. Irreducible nondecaying
stationary backgrounds, different geometry and quantum confinement remain
untested possibilities.

### Disposition

MG1 at flat, admitted trivial-exterior and parallel-neutral backgrounds fails the tested
positive **classical quadratic** gap assertion. BET-MASS-GAP remains active:
one of24 runs used, one speculative action family, no coefficient tuning.
This does not exhaust the bet's allowed backgrounds, source contractions
or possible interacting mechanisms. It supplies an asymptotic requirement
for later candidates rather than a matrix entry. The bet's eventual kill
criterion cannot be inferred from one candidate subset.

Massless free gluon modes do not decide a nonperturbative quantum mass gap:
that concerns a gauge-invariant physical quantum spectrum and interacting
vacuum, neither supplied here. No claim in the bet register about an
unverified external proof is used as evidence. No source polarity, ledger,
matrix scientific cell, class C, canon or public verdict changes.

[Exact probe](../../tests/program-focus/bet_mass_gap_curvature_end_probe.py)
and [evidence](../../lab/process/bet-mass-gap-curvature-end-test.json)
separate finite symbolic checks from the written infinite-domain argument.
Independent internal specialist and hostile review are required; neither
finite checks nor internal review is Lean or external-expert certification.
