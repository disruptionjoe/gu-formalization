---
title: "K1869: Finite-energy range and optimal lifting of planar wall packets"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional K1840 observation and exact Hilbert range; no native GU wall, physical state, chirality or count
---

# No zero mode does not imply finite-energy observation of every wall packet

On K1840's planar wall in R x R², the target has no nonzero L2 constant
wall mode. Nevertheless a smooth Gaussian wave packet has no finite-source-
energy lift. The exact obstruction is its low-frequency inverse-square
integral, not a point-spectrum kernel. This note classifies all wall packets,
constructs allowed repairs, and derives the optimal source-energy versus
approximation-error curve for the Gaussian.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact planar-wall range, minimum lift norm, gap/cancellation repairs and optimal approximate lift
carrier: K1840 compressed real16 source and real4 target on R times R2 LAYER=toy CHIRALITY=N/A
pairing: source integral u^T H u and target Euclidean L2 ON=real_square_integrable_fields
real_structure: real fields; unitary Fourier complexification with conjugate symmetry
grading: wall projection and Fourier frequency only; no physical cohomology grading
action_owner: repository-construction -- the fixed conditional conservative K1840 interface
target: closed differential observation range and finite-energy approximate reconstruction MAP-TYPE=quotient
```

## 1. Actual object and prior work

[K1840](k1840-k77-conservative-variable-observation-2026-10-20.md) supplies
closed O, its weighted Hilbert adjoint O†, static source/target generators,
and the closed-form identity OO†=-576alpha L_t² with alpha>0. It proves
nonzero-frequency lifts and a bounded inverse when the second mass is nonzero.
Those are reused, not independently rebuilt here. This question concerns
integrating those lifts over arbitrarily low frequencies. A formal inverse
at each nonzero k is not an L2 existence theorem.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN
about southeast alternatives. SC-MAS-01 and SC-CHI-02 ASSERTS stylized
curvature-mass/decoupling claims, not this wall or observation. SC-META-53
remains UNCERTAIN. This fixture is not a source-selected GU operator, physical
Hilbert space or family-count mechanism. RA-F1, AC-F1, LT-SM8 and the entire
88-active/91-stored physics ledger stay unchanged. The classical wall mechanism
is discussed in the primary paper [Lu, Watson and Weinstein](https://arxiv.org/abs/1808.01378);
no novelty is claimed for wall localization or general spectral range theory.

## 2. Closed-operator range criterion and minimal lift

For any densely defined closed O between Hilbert spaces, put T=OO†. Its
polar decomposition is O=T^(1/2)U, where U is a partial isometry from
(ker O)^perp to (ker O†)^perp. This follows from the usual polar decomposition
of O† and taking its adjoint. Consequently, for target psi,

```
psi in Range(O) iff psi perpendicular to ker T
               and int_(lambda>0) lambda^-1 d||E_lambda psi||² < infinity.
minimum ||u||_H² = int lambda^-1 d||E_lambda psi||².             (1)
```

Indeed on (ker T)^perp the unique minimal preimage is
U* T^(-1/2)psi. It belongs to Dom O since applying T^(1/2) to Uu gives
psi. Every other solution adds a vector in ker O and increases its squared
norm. This proves necessity as well as sufficiency. The notation
O†T^-1psi is only formal when T^-1psi does not exist; spectral cutoffs
converge to the minimal lift precisely under(1). No unlicensed inverse domain
is introduced.

## 3. Restriction to the actual planar wall

Use m1(x)=m0 tanh(24m0 x), m0>0, and optional constant m2=mu.
The K1840 normal sector K=D1 B1=+1 has real dimension2. Its normalized
normal profile is

```
n(x)=sqrt(12m0) sech(24m0 x),    integral n²=1.
```

For psi(x,y)=n(x)v(y), y in R² and v valued in that sector, K1840 gives

```
T_wall=alpha(-Delta_y+576mu²),
minimum ||u||_H²=(1/alpha) int_R² |vhat(k)|²/(|k|²+576mu²) dk.   (2)
```

Use the unitary Fourier convention vhat(k)=(2pi)^-1 int exp(-ik.y)v(y)dy.
The wall subspace reduces T; hence(1) applies to it even when the source
is allowed its entire carrier. Off-wall or invisible source additions cannot
lower(2). For mu=0, ker T_wall=0 because an L2 Fourier function supported
only at k=0 is zero. The range is nevertheless proper and nonclosed: functions
with frequency cutoffs away from0 are dense, while(2) need not be finite.
Evolution preserves this weighted Fourier integral because the wall generator
is skew and its squared modulus is |k|²/576+mu².

## 4. Localized packet, exact cancellation criterion and dimension

Take a unit normal-sector vector e and the normalized real Gaussian

```
vhat(k)=pi^(-1/2) exp(-|k|²/2)e.                                 (3)
```

Its unit L2 norm follows from 2 int_0^infinity r exp(-r²)dr=1.
At mu=0, (2) diverges logarithmically at0, so this smooth localized target
has no finite-energy lift. This conclusion uses the full observation range,
not just failure of one proposed right inverse.

For Schwartz v in R², (2) is finite exactly when vhat(0)=0, equivalently
int v=0 componentwise. Necessity follows from continuity and nonzero value
on a neighborhood of0. For sufficiency use vhat(k)=O(|k|), then rapid decay
at infinity. Thus a derivative-of-Gaussian packet is a concrete repair on
the unchanged massless interface. Arbitrary zero-mean L2 data are not covered
by this shortcut; the weighted criterion(2) is the general statement.

More generally an analogous scalar multiplier in d transverse dimensions
with vhat~|k|^ell needs d+2ell>2 near zero. This dimensional comparison is
an analytic control, not an assertion of extra dimensions in K1840.
On the actual d=2 wall, nonvanishing mean is exactly the smooth threshold.
On a transverse torus the zero Fourier mode is a genuine kernel instead;
removing it leaves a discrete spectral gap. These domains cannot be interchanged.

## 5. Approximation and the second-mass repair

Let epsilon>0 and retain(3) only for |k|>=epsilon. The exact minimum lift
norm and target squared approximation error are

```
||u_epsilon||_H²=(1/alpha) E1(epsilon²),
||v-v_epsilon||²=1-exp(-epsilon²),
E1(z)=int_z^infinity exp(-t)/t dt.                              (4)
```

Thus approximation is possible to arbitrary precision but the required source
energy grows logarithmically. Sharp cutoffs are measurable L2 spectral
projections, not claims of compact spatial support; smooth cutoffs give the
same threshold. Equations(1) and(4) keep finite-energy range distinct from
its closure.

The allowed K1840 repair mu!=0 changes the target mass but preserves the
same positive energy and principal fixture. For a=24|mu|, the Gaussian has

```
minimum ||u_mu||_H²=(1/alpha) J(a²),
J(b)=int_0^infinity exp(-t)/(t+b) dt=exp(b)E1(b), b>0.             (5)
```

This is finite and behaves as (1/alpha)log(1/a²)+O(1) when mu->0.
To see the logarithm without an assumed expansion, split the integral at1:
the difference from int_0^1 dt/(t+b) is bounded uniformly, using
|1-exp(-t)|<=t on[0,1] and the exponential tail. The Gaussian energy
therefore diverges much more slowly than the worst-case bound
||u||²<=||v||²/(576alpha mu²). A shrinking gap gives no bounded lift for
the limiting massless Gaussian. This is a repair with a changed target,
not proof that the original target was observable.

## 6. Sharp finite-energy approximation, not only a cutoff construction

For the massless Gaussian, minimize ||Ou-psi||² over ||u||_H²<=B.
For tau>0 the strictly convex penalized problem has spectral solution

```
u_tau=O†(T+tau)^-1 psi,
(Ou_tau)^hat(k)= [alpha |k|²/(alpha |k|²+tau)] vhat(k).
```

Here the resolvent and O† composition is bounded, so its domain is valid.
The spectral formula proves optimality by completing the square frequency
by frequency; source-kernel components waste budget. Put b=tau/alpha.
Differentiating the absolutely convergent integral J for b>0 and integrating
by parts gives -J'(b)=1/b-J(b). Radial integration yields the exact frontier

```
B(b)=[(1+b)J(b)-1]/alpha,
error²(b)=b-b²J(b),                   0<b<infinity.              (6)
```

B decreases continuously and strictly from infinity to0: equivalently
B=(1/alpha) int t exp(-t)/(t+b)² dt, whose derivative is negative.
Thus each B>0 selects exactly one b. Comparing any budget-feasible u with
the minimizer of ||Ou-psi||²+tau||u||² proves(6) is also the constrained
minimum. There is no unknown optimizer or numerical fitting in this curve.
Using J(b)=log(1/b)+O(1) gives

```
log(1/error²)=alpha B+O(1),  B->infinity.                         (7)
```

This is a certified asymptotic rate for a fixed, explicitly normalized packet,
not a uniform recovery rate over all unit targets. Adversarial targets can
concentrate at arbitrarily small frequencies and require arbitrarily large
energy at any fixed relative accuracy. Numerical E1 values may illustrate
(6), but only validated quadrature would supply rigorous decimal budgets.

## 7. Verification and next exact obligations

The symbolic producer checks the normalized radial integrals, resolvent and
budget identities, scale factors and cancellation examples. The independent
probe differentiates rational frequency multipliers and compares alternative
integral expressions; numerical quadrature is labeled numerical evidence.
Mathematical-input mutations fail assertions after a clean baseline; reporting
scope mutations are separate. These controls do not replace the closed-domain
proof in sections2-3 or certify K1840's previously banked matrices afresh.

Hostile review tested absence of point spectrum versus continuous spectrum,
formal O†T^-1 versus polar domains, full source versus restricted lift,
normal-profile normalization, vector mean cancellation, torus versus plane,
unitary Fourier factors, changed target in the mass repair and budget optimality.
The domain-wall profile and adjoint-square proof are reused at their exact
K1840 scope; no external review or formal proof-assistant claim is made.

Reproduce with the two k1869 scripts in tests/channel-swings. The unresolved
source-selected coefficient/observation/domain bridge is unchanged. Within
this conditional class the whole wall range and finite-budget consumer are
now explicit. A new useful continuation must supply actual source data or
study a named multidirectional/nonlinear interface with its full intertwining
equations; another nonzero-frequency example cannot fix the low-frequency
range obstruction.
