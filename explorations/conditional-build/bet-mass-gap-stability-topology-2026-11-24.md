---
title: "BET-MASS-GAP: stationarity, stability and topology"
status: exploration
doc_type: structural-result
created: "2026-11-24"
program_target: BET-MASS-GAP
tier: T2
expected_delta: Distinguish stationary candidates, physical saddles and a stable topological quadratic gap in the existing speculative curvature-square family.
actual_delta: Scoped T2 stationarity, physical-instability and full flat-torus gap classification accepted; source and quantum transfer remain open.
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Stationarity, stability and topology separate classical gap mechanisms

**Result.** In the existing **SPECULATIVE MG1** compact positive Yang–Mills
family, every static spatially constant stationary connection on flat R3 is
commuting and flat. The genuine constant Cartan magnetic solution has an
explicit square-integrable physical negative direction. A nonflat irreducible
stationary connection on round S3 also has a physical negative direction.
Conversely, a flat connection on a specified twisted SO(3) bundle over a cubic
torus has a strictly positive reduced quadratic spectrum: smallest eigenvalue
`pi^2/L^2`, frequency `pi/L`. The gap is caused by holonomy and finite size.

These are new combinations and checks **within the repository**, not claims
of new Yang–Mills mathematics. No quantum mass gap, source realization,
prediction, class-C decision or bet-wide exclusion follows. The S3 and torus
controls explicitly extend MG1's original R3 spatial domain.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

program_target: BET-MASS-GAP
tier: T2
expected_delta: Classify stationary and stable background mechanisms without introducing another action or transferring comparator results to GU.
actual_delta: Scoped T2 stationarity, physical-instability and full flat-torus gap classification accepted; source and quantum transfer remain open.

```gu-typed-objects
result: curvature-square-stability-topology
carrier: observed real adjoint-valued one-form for declared compact Lorentz-inert gauge group LAYER=toy CHIRALITY=N/A
pairing: positive Ad-invariant Lie-algebra form and spatial L2 norm ON=declared_carrier
real_structure: real compact Lie algebra; complex Fourier modes obey conjugate reality
grading: Gauss constraint and transverse spatial fields, not fermionic chirality
action_owner: repository-construction -- SPECULATIVE MG1 Yang-Mills curvature-square family
target: classical reduced Hessian, stationary backgrounds and gauge-bundle topology MAP-TYPE=quotient
```

## 1. Source boundary and common conventions

The [November 11 result](bet-mass-gap-curvature-end-test-2026-11-11.md)
already owns flat/neutral gaplessness, trivial-exterior and decaying-potential
continuum controls, and the finite-energy static R3 virial exclusion. Those
are inherited here, not counted as fresh results. One existing local action
is used; there are **zero new guessed action variants** and no coefficient fit.

For a fixed spatial Riemannian metric and compact gauge algebra with positive
invariant inner product, set

`E(A) = (1/2) integral sum_(i<j) |F_ij|^2`,
`F_ij = partial_i A_j - partial_j A_i + [A_i,A_j]`.

Use temporal gauge and no background electric field. Static source-free
stationarity is `D_A^* F_A=0`; linearized Gauss reduction uses
`D_A^* a = D_A^* e = 0` modulo infinitesimal gauge fields `D_A epsilon`.
Write `q_A(a)=E''(A)[a,a]`. Thus

`q_A(a)=||d_A a||^2 + 2<F_A,a wedge a>`.

The norm of a two-form sums over `i<j`. In flat space, on Coulomb fields,
`(K_A a)_i = -D_j D_j a_i - 2[F_ij,a_j]`.
We use direct energy variation on S3 to avoid omitting its Ricci contribution.
The spectral gap below means the lower bound of this physical **quadratic**
operator, not an interacting quantum energy gap.

Source claim SC-GEO-58 **DISAVOWS** a separate fundamental Higgs; its accompanying
mechanism uses curvature and an ad-valued one-form, including a negative
quadratic term before condensation. SC-GEO-55 **ASSERTS** displacement from a
gauge-rotated Levi-Civita connection. Neither selects compact positive MG1.
The [source steelman](../../lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md)
and [actual contraction](../../lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md)
remain the source-facing owners: `(s* C)_mu = C_mu + C_I partial_mu g^I`.
The observed field stays a one-form. Native indefinite pairing, soldered
adjoint, moving observation and coupled equations have not been supplied by
this comparator. No 2+1, chirality or imposter label is reinterpreted here.

**An instability is not a source falsification.** It rejects a selected
background as an already stable vacuum. A source mechanism that seeks
condensation may require an instability at its starting background. A
negative Hessian eigenvalue here is not an identification with the source's
geometric negative-curvature hypothesis or its eventual condensate.

## 2. All spatially constant compact-positive R3 stationary potentials are flat

Let `A_i` be arbitrary constant elements of a finite-dimensional compact Lie
algebra, `A_0=0`, on Euclidean R3. No finite-background-energy assumption is
made. The full static field equation reduces to

`sum_j [A_j,[A_j,A_i]] = 0` for each i.

Pair with `A_i` and sum over i. Invariance and positivity give

`0 = -sum_(i,j) ||[A_j,A_i]||^2`.

Therefore every commutator vanishes, so `F=0`. Conversely commuting constants
solve the field equation. On simply connected R3 they are gauge-equivalent to
zero, and the unitarily transported transverse Laplacian is gapless. If the
chosen gauge group at infinity excludes that gauge transformation, the
spectral equivalence still follows by the norm-preserving multiplication
operator with its transported magnetic Sobolev domain; no topological boundary
charge is erased by declaration.

This closes the entire **constant-potential repair class** under these
assumptions, independently of the earlier finite-energy virial argument.
It does not say all constant-curvature backgrounds are flat: the Cartan
example below has position-dependent potential. It does not cover indefinite
Lie pairing, electric backgrounds, curvature of the base, sources, or
spatially varying nondecaying solutions. It is a subset classification,
not the bet's all-background kill criterion.

## 3. Cartan magnetic background: a real, L2, physical negative direction

Use orthonormal `su(2)` generators `[T_i,T_j]=epsilon_ijk T_k`. For `B>0`,

`A_x=-(B y/2) T3`, `A_y=(B x/2) T3`, `A_z=0`, `F_xy=B T3`.

This is the symmetric-gauge version of the previously supplied stationary
Cartan field. Its background energy on R3 is infinite. We compare **finite
relative energy**, not subtract two infinite integrals.

For any `L>0`, set

`u=exp[-B(x^2+y^2)/4] exp[-z^2/(2L^2)]`,
`a_x=u T1`, `a_y=-u T2`, `a_z=0`.

Direct computation gives

`D_x a_x+D_y a_y=0`,
`(d_A a)_xy=0`, `(d_A a)_xz=-u_z T1`, `(d_A a)_yz=u_z T2`,
`(a wedge a)_xy=-u^2 T3`.

The linear relative-energy term and cubic term vanish. Pointwise expansion
of the energy-density difference, followed by its convergent integral, gives

`Delta E(t)=t^2 integral (u_z^2-B u^2) + (t^4/2) integral u^4`.

In particular

`q_A(a)/||a||^2 = ||g'||^2/||g||^2 - B = 1/(2L^2)-B`,
`||a||^2 = 4 pi^(3/2) L/B`, where `g(z)=exp[-z^2/(2L^2)]`.

For `L^2>1/(2B)` this is negative, and sufficiently small nonzero t lowers
relative energy. This is an honest real-adjoint, square-integrable direction,
not a plane wave in z or an L2 eigenvector at `-B`. The Gaussian is in the
magnetic H2 domain: covariant derivatives through order two are polynomial
times Gaussian. More precisely, close the semibounded Hessian form on the
magnetic-H1 closure of Schwartz background-Coulomb fields and take its
Friedrichs operator on their L2 closure. The bounded curvature term preserves
semiboundedness; the displayed K a is again Schwartz and Coulomb, establishing
operator-domain membership. An alternative end/domain choice must admit this
perturbation before the conclusion transfers. Gauss-admissible growing
solutions follow from its negative spectral subspace; an explicit packet is
enough to prove that subspace exists, not its full spectral decomposition.

Admissible pure gauge directions have zero stationary Hessian, and Coulomb
directions are orthogonal to them under the stated decay/domain. Our negative
direction is therefore physical at linearized level. The cubic/quartic
formula also verifies the sign without relying on a gauge-fixing convention.
The complex polarization `E=T1+iT2`, `(phi,i phi,0) E g(z)` reproduces the
same real field and the charged branch `-partial_z^2-B`.

This is the known Nielsen–Olesen mechanism; [Tanji and Itakura](https://arxiv.org/abs/1111.6772)
describe the unstable soft modes of a constant color-magnetic field. The new
repository result is the explicit domain-qualified stability control. The
neutral sector was already gapless, so this is **not a new full-gap exclusion**.

## 4. Irreducibility is insufficient: a full stationary S3 saddle

Explicitly change spatial domain to round `S3=SU(2)` with a bi-invariant metric
of radius R. This is a control, not original MG1 on R3. Let
`theta=g^-1 dg` and `A_alpha=alpha theta` on the trivial SU(2) bundle.
With matrix-valued wedge conventions, `d theta=-theta wedge theta`, hence

`F_alpha=alpha(alpha-1) theta wedge theta`.

For a constant `c>0` fixed by the metric normalization,
`*(theta wedge theta)=c theta`. Therefore

`d_A *F = c alpha(alpha-1)(2alpha-1) theta wedge theta`.

The full YM equation, not just its restriction to an ansatz, holds exactly
at `alpha=0,1/2,1`. For `alpha=1/2` the curvature values span `su(2)`.
A parallel adjoint section must commute with all curvature values and is zero:
there is no parallel neutral adjoint direction.

Nevertheless, `E(alpha)=C alpha^2(1-alpha)^2`, `C>0`, so
`E''(1/2)=-C<0`. The amplitude variation is `a=theta`. Left-invariant
one-forms are coclosed in the bi-invariant metric, and in an orthonormal
left-invariant frame `sum_i[A_i,theta_i]=0`. Thus `d_A^* theta=0`:
the negative direction is background-Coulomb and cannot be pure gauge.
It is smooth on compact S3, with no boundary or decay proviso.

With `[T_i,T_j]=epsilon_ijk T_k` and orthonormal coframe e satisfying
`de^i=-(c/2)epsilon_ijk e^j wedge e^k`, one has `theta=c T_i e^i`,
`c=2/R`, `C=3 c^4 Vol(S3)/2`. Thus this direction has Hessian Rayleigh
quotient `-c^2/2=-2/R^2`. Only the negative direction is needed; no full
Morse index or S3 spectral classification is claimed. Related classical
SU(2) sphalerons on S3 are discussed by [Smilga](https://arxiv.org/abs/hep-th/9504117).

## 5. Stable positive control: twisted flat SO(3) on T3

### Bundle and exact physical spectrum

Use the same local positive Yang–Mills action on `R_t x T3`, with periods
`L_x,L_y,L_z`. Change the global gauge group and bundle to SO(3), with
commuting holonomies

`H_x=diag(1,-1,-1)`, `H_y=diag(-1,1,-1)`, `H_z=I`.

The quotient of `R3 x SO(3)` by these deck transformations gives a flat
principal bundle. Locally A=0; it is **not** a globally periodic potential on
the trivial bundle. In the adjoint, the three real color lines have shifts

`nu_1=(0,1/2,0)`, `nu_2=(1/2,0,0)`, `nu_3=(1/2,1/2,0)`.

Their complete Fourier momenta are `k_j=2pi(n_j+nu_c,j)/L_j`, `n in Z3`.
Every k is nonzero. Complex modes are paired by conjugation to form real
fields; no extra color or polarization count is inferred from complexification.

The scalar covariant Laplacian `Delta_0` is invertible. Each infinitesimal
gauge class has its unique Coulomb representative
`a_perp=a-d_0 Delta_0^-1 d_0* a`. At each momentum, `k dot a=k dot e=0`;
two transverse polarizations survive Gauss reduction. In this gauge the
linearized temporal component is removed by Gauss law as well.

The physical Hessian is `T=Delta_1|ker d_0*`, domain twisted
`H2(ad P tensor T*T3) intersect ker d_0*`, with compact resolvent and spectrum

`lambda_(c,n)=4pi^2 sum_j (n_j+nu_c,j)^2/L_j^2`, two transverse polarizations.

Consequently the three color minima are

`pi^2/L_y^2`, `pi^2/L_x^2`, `pi^2(1/L_x^2+1/L_y^2)`.

All are attained by physical polarizations. Thus

**`lambda_min=min(pi^2/L_x^2, pi^2/L_y^2)`**, and on the cube
**`lambda_min=pi^2/L^2`, `omega_min=pi/L`**.

Because F=0 and E is positive, this is an absolute magnetic-energy minimum
and a stable quadratic control. This does not prove full nonlinear dynamical
stability. The finite residual stabilizer is the Klein four group, so the
full local gauge quotient has a finite identification; it creates no
infinitesimal zero mode and does not turn classical modes into quantum
gauge-invariant one-particle states by fiat.

Sending either L_x or L_y to infinity closes the gap. Sending only L_z to
infinity preserves the transverse compactification threshold while the
longitudinal spectrum becomes continuous. Uniform decompactification closes
the gap. This is a **flat holonomy/finite-size gap**, not curvature-generated
bulk mass. Classical twisted torus vacua have established literature, e.g.
[Selivanov and Smilga](https://arxiv.org/abs/hep-th/0010243); the exact spectrum
above follows directly from the stated characters.

### General flat-torus discriminator and lifting price

For any flat compact-gauge connection on a fixed flat rectangular T3, its commuting
unitary adjoint holonomies simultaneously split into characters. The same
Fourier argument proves: the full transverse quadratic gap is positive
**if and only if the common adjoint fixed space is zero**. A trivial character
gives constant adjoint-valued harmonic one-forms. They are physical quadratic
zero modes, not gradients of admissible periodic scalars. Individual commuting
Wilson-line variations integrate to flat deformations, but arbitrary
noncommuting tuples may acquire quartic curvature energy; not every Hessian
zero direction is unobstructed flat moduli. For nontrivial characters,
the finite collection of shifted lattices has positive distance from zero.
This criterion concerns flat connections on a flat compact rectangular T3; it is not
the corresponding criterion for curved backgrounds such as S3 above.

For an ordinary flat SU(2) connection on T3, the three SU(2) holonomies commute
and can be conjugated into a common maximal torus. They fix a Cartan direction
in the adjoint; the full quadratic gap is zero. No analogous assertion about
all triples in every compact group is made. Embedding the SO(3) example into
a larger adjoint carrier can restore a common neutral fixed space and destroy
its full gap; the complete representation, not just this subblock, matters.

Our SO(3) example avoids the SU(2) argument because it does not lift. The lifts
`i sigma_x,i sigma_y` anticommute with commutator `-I`. Equivalently, if
`alpha,beta in H1(T3;Z2)` denote x,y, the three real color lines have
`w1=beta,alpha,alpha+beta`. Whitney multiplication gives
`w1(ad P)=0`, `w2(ad P)=alpha cup beta !=0`.

This yields an exact SO(3)-specific classification: **for a flat SO(3)
connection on fixed flat T3, a positive full physical Hessian gap is equivalent
to `w2 !=0`**. If `w2=0`, the bundle and connection lift to flat SU(2), whose
commuting holonomies fix a Cartan direction. Conversely, a common nonzero
adjoint fixed vector forces all SO(3) holonomies into rotations about one
axis; their lifts can all be chosen in a single U(1) subgroup and commute,
so the lifting obstruction is zero. This classification is limited to flat
SO(3) on T3, with the same full-adjoint and positivity assumptions.

An ordinary fundamental SU(2) doublet cannot be associated to this SO(3)
bundle alone. A combined central quotient would require further explicit
bundle data, not an assumed cancellation by the tangent spin structure.
SC-GRP-02 and SC-GEO-51 **ASSERT** the chimeric spin-derived parent bundle
with U(64,64); they supply neither this SO(3) reduction nor its flux or compact
positive observed pairing. Conversely that parent origin alone does not
prove every possible SO(3) reduction must lift. The source embedding,
representation and observation map decide transfer; none is built here.

## 6. What changed and what remains live

| Declared construction | Stationary? | Physical quadratic result | What this establishes |
|---|---|---|---|
| Constant potentials, compact positive flat R3 | Only when commuting | Flat, gapless | Entire noncommuting constant-potential repair class is off shell |
| Constant Cartan curvature, R3 | Yes | Charged negative direction; inherited neutral continuum | An unstable uncondensed background, not a stable vacuum |
| Round S3, SU(2), A=theta/2 | Yes, full equation | No parallel adjoint section, yet a negative physical direction | Irreducibility alone does not ensure stability |
| Flat twisted SO(3), fixed T3 | Yes | Positive full reduced quadratic spectrum | Holonomy and finite size suffice, with nonliftable bundle price |

BET-MASS-GAP remains active. Spatially varying nondecaying R3 backgrounds,
other specified geometries, quantum mechanisms and the native coupled action
are not exhausted. The torus result is a genuine positive control but does
not evade the original R3 condition by silently changing its domain. No
scientific matrix/ledger result is imported from this discovery bet.

The next useful discriminator within the bet is the **stable endpoint with
the full carrier**: a supplied stationary nonconstant background needs its
complete Gauss-reduced Hessian and domain; a topology route needs its actual
holonomy representation and any neutral centralizer. Repeating an unstable
Cartan mass matrix, assuming irreducibility is enough, or transferring a
gapped subblock to the full source gauge sector supplies none of those data.
The source-native current/physical quotient and action bridge remain open.

## Reproduction and acceptance

Run `python tests/program-focus/bet_mass_gap_stability_topology_probe.py`
with SymPy available. The script checks the exact Lie-algebra/energy,
Gaussian, exterior-form, Fourier and lift identities. The general Lie-algebra
and complete Fourier theorems are the analytic arguments above; a finite
probe is not their proof. See the [structured report](../../lab/process/bet-mass-gap-stability-topology.json)
and [independent review](../../lab/process/hostile-reviews/2026-11-24-mass-gap-stability-topology-review.md).
Acceptance: 77 exact controls PASS. Independent mathematical and hostile T2 reviews accept the scoped results after the domain, zero-mode and source-boundary qualifications. Internal agent review is not external-expert certification or a proof-assistant check.
