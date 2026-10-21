---
title: "K1875: Nonlinear mass-local repairs cannot carry moving zero crossings"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: regular zero-normalized mass-local class only; no exclusion of offset, derivative-dependent or general moving coefficients and no GU verdict
---

# Smooth nonlinear mass-local coefficients do not rescue a moving zero

Keep K1840's fixed principal operators, leading observation and positive
pairings. At any fixed nonzero real speed v, let C(r),B(r),S(r) be C1
functions of a single real mass parameter, vanishing at r=0, with nonzero
B'(0) in the two-dimensional target mass plane. They may be nonlinear and
B(r) may turn away from that plane at higher order. If they satisfy the
conservative first-order identities and exactly intertwine along a C1
profile r=m(x1-vt), then a nonconstant such profile cannot reach zero at a
finite coordinate. Near zero it must obey `|m'|<=K |m|²` for some finite K.
Consequently a smooth moving kink, compactly supported pulse, or exponentially
decaying pulse cannot be realized in this class with the fixed symbols.

This is a profile-specific theorem, unlike K1873's constant-triple,
arbitrary-profile result. It still does not exclude arbitrary coefficient
functions, nonzero offsets at m=0, derivative-dependent corrections, moving
pairings or leading observations, or changed principal operators. No actual
GU source coefficient map is identified by this conditional calculation.

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
result: nonlinear mass-local zero-crossing obstruction and tail-rate necessary condition
carrier: fixed real16 compressed source and real4 target, four coordinate types LAYER=toy CHIRALITY=N/A
pairing: fixed positive H and target Euclidean form ON=real_square_integrable_fields
real_structure: real C1 matrix curves and real traveling mass profile
grading: differential order and first mass derivative at zero only
action_owner: repository-construction -- conditional K1840 conservative first-order equations
target: exact fixed-symbol intertwining along a single profile MAP-TYPE=quotient
```

## 1. Source boundary and reused complete-bank result

[K1840](k1840-k77-conservative-variable-observation-2026-10-20.md) supplies
all44 conservative pointwise directions. [K1873](k1873-traveling-mass-compatibility-2026-10-20.md)
proves, by polynomial dual witnesses plus exceptional-speed witnesses, that
no tangent triple with nonzero B in the two-dimensional mass plane satisfies
both the first-order equations and `T1 C+(v I-d1)S=0` for v!=0.
This uses the complete bank, not just six preferred static repairs.
We reuse that exact theorem and its independent coefficientwise checker.
The new proof is the nonlinear and single-profile transfer below.

SC-OP-04 ASSERTS candidate four-field grammar; SC-MAS-01 and SC-CHI-02
ASSERTS the stylized mass/decoupling toy. SC-OP-05 and SC-META-53 remain
UNCERTAIN. WGS05 leaves the full spinless-connection/scalar-curvature bundle
map open. These source assertions do not supply the compressed matrices,
positive H, observation or mass-local ansatz here. RA-F1, AC-F1, LT-SM8 and
all source/physics-ledger/canon verdicts are unchanged.

## 2. Full residual for one nonlinear profile

Let d_i=D_i/24, z=x1-vt, and write

```
P=partial_t+A_i partial_i+C(m(z)),
Q=partial_t+d_i partial_i+B(m(z)),
O=T_i partial_i+S(m(z)).
```

The pairings are fixed. Conservation requires HC+C^T H=0 and B+B^T=0.
In addition to the already fixed second-order symbol identity, OP=QO means

```
T_i C-B T_i+S A_i-d_i S=0,                  all i,      (2)
m' L(m)+N(m)=0,
L(r)=T1 C'(r)+(v I-d1) S'(r),
N(r)=S(r)C(r)-B(r)S(r).                                (3)
```

The +v sign comes from -partial_t S(m). No requirement that m and m'
be independently specifiable is imposed. Equation (3) is tested along the
ONE supplied profile; that is the difference from the preceding result.
We assume (2) and conservation on a mass interval around0. It suffices on
the one-sided interval actually attained by the profile, with C1 extension
to0; the derivative at the endpoint is then one-sided.

## 3. Tangent obstruction forces an ODE inequality

Differentiate (2) and conservation at r=0. The tangent triple
(C'(0),B'(0),S'(0)) belongs to K1840's full44-dimensional bank. Since
B'(0) is a nonzero mass-plane vector, K1873 implies L(0)!=0 for every
v!=0, including v=+1 and -1, where its separate witnesses are required.
Continuity gives a mass neighborhood with `||L(r)||>=ell>0`.
C1 regularity and C(0)=B(0)=S(0)=0 give bounds
`||C(r)||<=c_C |r|`, `||B(r)||<=c_B |r|`, `||S(r)||<=c_S |r|`.
Choose compatible operator/Frobenius norms. Thus

```
||N(r)|| <= c_S(c_C+c_B) r²,
|m'| <= [c_S(c_C+c_B)/ell] |m|² = K |m|².              (4)
```

The equality `||m'L||=|m'| ||L||` is exact, so this norm estimate cannot
hide a matrix cancellation. The coefficient K is finite for each specified
curve and speed; no universal speed-independent K is asserted.

If m(z0)=0, continuity places m in this neighborhood on some interval about
z0. There `|m'|<=K epsilon |m|`, and Gronwall with zero initial value gives
m=0 throughout that interval. The zero set is therefore open and closed in
the connected profile domain. Either m is identically0, or it has no zeros.
This rules out even flat finite-order or infinitely flat crossings; a
transverse-crossing argument alone would not establish that stronger claim.

For a nonzero profile approaching0 along an infinite tail, (4) gives
`|(1/m)'|<=K`, hence, after the tail first enters the mass neighborhood,

```
|m(z)| >= 1/(1/|m(z0)|+K |z-z0|).                     (5)
```

Exponential, Gaussian and faster-than-reciprocal power decay are impossible.
An inverse-distance tail is only a necessary allowed rate, not a constructed
solution. The coefficient data and exact nonlinear residual still have to be
solved. Sign-changing tanh walls are excluded by the finite-zero theorem;
sech pulses are excluded by (5), even though they never vanish at finite z.

## 4. Executed constant-triple classification and controls

For the simpler C=r C1, B=r B1, S=r S1 subclass, L is a constant nonzero
matrix at v!=0 and N=r² N1. On every nonzero part of a nonconstant profile,
(3) forces N1=-a L for one real constant a and `m'=a m²`.
If N1 is not proportional to L, no such profile exists. If proportional,
the only nonzero solutions are `m(z)=m0/(1-a m0(z-z0))`.
For a!=0 this has a finite pole on the full real line; for a=0 it is constant.
Thus there is no nonconstant globally C1 full-line profile in this constant-
triple class, even if no sign change is demanded. The Riccati branch is a
necessary conditional classification; we do not claim a coefficient triple
realizing a!=0. It cannot be promoted to an existence construction.

Positive controls matter. At v=0, the saved static repairs satisfy L=0,N=0
and allow arbitrary profiles including zero crossings. For any speed, a
constant mass has m'=0 and the same static triple works since N=0.
A nonlinear reparameterization C(r)=f(r)C1, B(r)=f(r)B1, S(r)=f(r)S1
with f=r+r³ has N=0 and L=v f'(r)S1 for those static repairs: it still
fails wherever m'!=0. Exact matrix controls check all four types and both
mass directions, along with preservation of first-order identities and
pairings. The scalar profile and tail checks use exact derivatives, not
sampled guesses about zero crossings.

## 5. Repair boundaries and what remains genuinely open

K1873's common-drift repair changes both principal symbols by q'(t)I and
transports static profiles unitarily. It remains a valid changed-assumption
repair and explains why the current obstruction is not a universal motion
no-go. Repeating that repair gives no new fixed-symbol construction.

An affine offset C(0) or S(0) invalidates the O(r²) estimate for N; a
nonzero B(0) likewise changes its leading order. Dependence on m' introduces
higher profile jets, and dependence on additional independent fields need
not reduce to one C1 curve with nonzero mass tangent. A mass with B'(0)=0
is also outside the stated theorem. None is excluded or asserted viable.
A tempting stronger shortcut fails on the actual full bank. For a general
observation, the Gram operator O O^dagger has first-derivative coefficients
`G_i=T_i H^-1 S^T-S H^-1 T_i^T`. Their joint image on the complete bank
has dimension4 for each coordinate type. Even restricting B=0 leaves an
image of dimension4. Thus massless coefficient offsets can carry nonzero
first derivatives in the Gram operator. Treating it automatically as
`-alpha Delta+V` discards allowed data and cannot prove a universal moving-
mass obstruction. Exact full-bank and separately reconstructed B=0 checks
establish this counterexample to the shortcut; no offset solution is thereby
constructed. The conjectured proportionality of G_i to {d_i,B} fails for the
same reason and was not used as evidence.

We also execute the first affine-offset repair test. Fix B=m B1,
C=C0+m C1 and S=S0+m S1, with each constant triple satisfying the full
first-order/conservation bank (B0=0). For the supplied kink
`m=a tanh(kappa a z)`, a,kappa>0, define

```
L=T1 C1+(v I-d1)S1,
N0=S0 C0,  N1=S0 C1+S1 C0-B1 S0,  N2=S1 C1-B1 S1.
```

The residual vanishes for every z exactly when

```
N0=-kappa a² L,       N1=0,       N2=kappa L.           (6)
```

Polynomial coefficient matching is legitimate because this one kink attains
an open interval of mass values. In particular, adding ANY conservative
affine offsets to a static compatible slope (N2=0) cannot repair the moving
kink: (6) forces L=0, contradicting K1873 for B1!=0,v!=0. This contains
all choices of offset, not just the six invisible C directions. The remaining
general affine kink must use a slope with nonzero nonlinear defect to balance
the derivative. The target-skew image has rank6, so fixing each target B
leaves38 coordinates in the full44 bank. Thus the specific new construction
is a system of192 scalar quadratic equations (three4-by16 matrices) in76
real free coordinates for fixed a,kappa,v,B1. These are equation counts,
not an independence count, inconsistency proof or existence construction.
This reduction and the static-slope repair exclusion are checked exactly.
A future affine solution must solve that system; it cannot reuse a static
slope or assume away the four Gram freedoms. If coefficients are source-identified,
the actual native pairings and global observation domain must still be
constructed; merely renaming these finite matrices is not that adapter.

## 6. Verification and hostile review

The new producer checks the nonlinear reparameterization identities, positive
controls, scalar Riccati solution and profile derivative ratios. The independent
probe reruns K1873's polynomial coefficient witnesses against the raw full
bank, including exceptional speeds; it does not trust a saved pass flag.
It also reconstructs the B=0 Gram image and affine-kink coefficient equations, then separately evaluates the nonlinear residual at rational mass/speed/jet
values and corrupts input signs/coefficients after a clean baseline.
Pins and reporting controls are separate from mathematical checks.

The main new continuum proof is (2)-(5), reviewed inline for the quantifier
change, differentiability at0, one-sided values, nonzero tangent mass,
fixed versus moving pairings, matrix norms, Gronwall and infinite-tail
integration. No external reviewer or proof assistant is claimed. No remaining
flaw is known within these hypotheses; offset/general coefficient solutions
remain explicitly outside the theorem. Smoothness, zero normalization and
mass locality are real assumptions, not a derived feature of the GU source.
