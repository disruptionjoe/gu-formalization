---
title: "K1885: Travelling phase rigidity and the rotating-frame boundary"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: necessary fixed-symbol travelling target classification, canonical-base tangent exclusion and one-dimensional target bands; no general rotating-lift exclusion or native GU identification
scripts:
  - tests/channel-swings/k1885_traveling_phase_rigidity_and_frame_reduction.py
  - tests/channel-swings/k1885_traveling_phase_rigidity_and_frame_reduction_probe.py
---

# The surviving travelling mass must rotate uniformly

K1877 proves constant amplitude for a travelling pure mass in the fixed
conservative observation class. The remaining Gram equation also forces
constant angular velocity. Every nonzero allowed target profile is a uniform
circle, including a constant mass as zero angular velocity. Accelerated
rotation and chirped phase are excluded in this class.

The circle is not thereby constructed as an observation lift. An exact
tangent test excludes every differentiable constant-frame mass branch from
the canonical massless frame, even with all 44 conservative coefficient
directions available. Other base points, isolated finite-mass solutions and
variable-frame coefficients remain open. Exact target bands, spatial twists
and time monodromy describe what this unresolved lift would have to reproduce.

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
result: travelling phase rigidity, canonical-base mass-tangent obstruction and target spectral consumers
carrier: K1840 real16 source and real4 target, all four coordinate types LAYER=toy CHIRALITY=N/A
pairing: fixed positive source H and Euclidean target L2 ON=smooth_local_tests_and_stated_line_or_circle_domains
real_structure: real coefficients, complex Fourier representation with conjugate-symmetric real data
grading: differential order, mass-amplitude tangent and spectral involution; no physical grading
action_owner: repository-construction -- fixed-symbol conservative first-order equations
target: differential observation compatibility and separately target evolution MAP-TYPE=quotient
```

## 1. Preflight and source boundary

The operative construction is the corrected compressed K1832/K1836/K1840
system, not the source's complete bundle map. SC-OP-04 **ASSERTS** candidate
four-field grammar; SC-MAS-01 and SC-CHI-02 **ASSERTS** the stylized
curvature-mass and effective-decoupling toy. SC-OP-05 and SC-META-53 remain
**UNCERTAIN**. WGS-05 does not identify this real16 system, pairing, injection
or domain with its full20 placement and spinless gauge-potential mass.
No source claim, RA-F1, AC-F1, LT-SM8, ledger mapping or canon verdict changes.

Prior-object search reused K1877's four-parameter Gram image and amplitude
rigidity, K1879's frame transport and added connection, K1881's raw versus
normalized quotient, and K1883's compact range. None classifies angular
acceleration or the full mass tangent at the canonical rotating-frame base.
K1877 fixes static mass slopes and varies offsets. Here the canonical
massless offset is fixed and every tangent slope varies. Neither test contains
the other. The PDE lens uses Gram traces before nonlinear search; the
representation lens retains all freedoms and actual complex structures;
the algebraic lens seeks an all-speed dual rather than generic ranks;
the domain lens separates spectra, Floquet multipliers and spatial twists.
Native full-C/pairing/domain identification remains a distinct contender.

## 2. Tangential trace and complete necessary target-profile form

Use K1877's fixed A_i,T_i,H,d_i=D_i/24 and skew mass matrices B1,B2.
The D_i are symmetric Clifford generators; J=D1 D2 D3, J²=-I,
B1 J=B2, and both masses anticommute with every D_i. On a connected
z=x1-vt interval, v!=0, take C,S,m,n of class C3:

```
P=partial_t+A_i partial_i+C(z),
Q=partial_t+d_i partial_i+B(z), B=m B1+n B2,
O=T_i partial_i+S(z), OP=QO,
HC+C^T H=0, B^T=-B.
```

K1877's complete bank and Gram argument give, without choosing C or S,

```
K=O O^dagger=-alpha Delta+G_i partial_i+V,
G_i=a_i J+b D_i J, alpha>0,
a_i,b,u constant, m²+n²=R² constant,
V=uI-24alpha D1 B'-24 sum_i a_i D_i B J.
```

These are reused premises. The remaining Gram equation is
Z=(-vI+d1)V'+[B,V]+alpha B''-G1 B'=0. Its exact tangential trace is

```
tr[(D1 B J)^T Z]
 =96alpha v(m n''-n m'')
  +4(24a1 v+b)(m m'+n n').                            (1)
```

The second term vanishes by constant amplitude. If R>0, a C3 phase lift
m=R cos(theta), n=R sin(theta) exists on the interval. Then
m n''-n m''=R² theta'', so theta''=0. Consequently

```
B(z)=R[cos(omega z+theta0)B1+sin(omega z+theta0)B2].     (2)
```

If R=0, B=0 and no phase is defined. No division by omega or
v²-1/576 occurs: zero angular velocity and v=+/-1/24 are included.
For omega!=0, the other projections force a2=a3=0 and
b=-24v(a1+alpha omega). At phase zero they include

```
tr[(D1 B2)^T Z]=96alpha v R theta'',
tr[(D1 B1)^T Z]=-4R omega(24a1 v+24alpha v omega+b),
tr[(Dj B1)^T Z]=-96R aj v omega, j=2,3.
```

Conjugation by exp(-theta J/2) transports these to every phase. Polynomial
identity (1) independently avoids an all-angle claim from finite samples.
The result covers arbitrary smooth coefficient offsets and derivative-dependent
ansatzes evaluating to C(z),S(z), but not static v=0 or general spacetime
profiles, changing pairings/symbols, or additional target components.
K1840's arbitrary static profiles and K1879's connection repair survive.

Uniform rotation survives the necessary Gram test: a1=-alpha omega,
a2=a3=b=0, V=uI gives

```
K=-alpha(partial_1+omega J/2)^2-alpha partial_2²-alpha partial_3²
  +(u-alpha omega²/4)I.
```

It is nonnegative on the Euclidean Schwartz core for u>=alpha omega²/4.
This is an explicit contrary control, not a fixed-T factorization or a lift.

## 3. Exact frame reduction retains variable source coefficients

K1879's actual source L obeys L²=-I, L^T H=-HL, [L,A_i]=0 and
T_i L=J T_i in all four types. Put theta=omega(x1-vt)+theta0,
U=exp(-theta J/2), W=exp(-theta L/2). Then U T_i W^-1=T_i and

```
P_hat=W^-1 P W, Q_hat=U^-1 Q U, O_hat=U^-1 O W,
B_hat=R B1+(v omega/2)J-(omega/48)D1 J,
C_hat=W^-1 C W+(omega/2)(vI-A1)L,
S_hat=U^-1 S W-(omega/2)T1 L.                          (3)
```

Product differentiation proves OP=QO iff O_hat P_hat=Q_hat O_hat,
preserving the leading matrices and positive forms. Arbitrary C(z),S(z)
generally give VARIABLE C_hat(z),S_hat(z). The constant target does not
make its source constant. Constant-frame factorization is a sufficient
construction route, not a reduction of every possible lift to constants.

## 4. All smooth mass branches from the canonical constant base fail

Normalize omega=2. The canonical massless constant base is

```
C0=(vI-A1)L, B0=(vI-D1/24)J, S0=-T1 L.                 (4)
```

It is the transformed free system and satisfies conservation, the three
first-order relations, and S0 C0=B0 S0. Suppose CONSTANT-frame C(R),S(R)
are differentiable at R=0, equal (4) there, and satisfy the full equations
with B(R)=B0+R B1 in a neighborhood of zero. Their derivatives c,s obey

```
T_i c-B1 T_i+s A_i-d_i s=0, Hc+c^T H=0,
S0 c+s C0-B0 s=B1 S0.                                 (5)
```

The first line is the complete K1840 conservative pointwise bank with
target projection fixed to B1. Its 44 coordinates include every allowed
tangent, with no mass slope fixed beforehand. Six target coordinates plus
64 entries in the second line form M(v)x=r, a 70-by-44 polynomial system.
For each of the four types the certificate stores a sparse nine-entry
vector y(v), affine in v, satisfying

```
y(v)^T M(v)=0, y(v)^T r=v.                             (6)
```

Thus (5) is inconsistent at EVERY v!=0, including exceptional matrix-rank
values. The polynomial dual owns this conclusion; generic ranks do not.
At v=0 the linear system is consistent, a necessary static control rather
than a claim that every tangent integrates. For omega!=0 let h=omega/2:
the base (4) scales by h; the first line of (5) is unchanged and its second
line scales by h. Dividing those 64 rows by h gives the same system.

This excludes every affine mass family and every differentiable nonlinear
amplitude family through this canonical base. It does NOT exclude one
isolated finite-R solution, a nonsmooth branch, a different massless base,
or variable-frame coefficients. Together with K1877's complementary
static-slope/all-offset test it removes two natural perturbative routes,
while leaving the genuine nonlinear factorization question open.

## 5. Target bands, circle twist and time monodromy

These results concern the TARGET whether or not a source lift exists.
Use the one-dimensional line problem, or the transverse zero sector of
R x T², on its H1 generator domain. This is not a full three-dimensional
band calculation. With continuous Fourier momentum on the line set

```
p=xi1/24, a=v omega/2, b=-omega/48,
Kc=-iJ, beta=-iB1, F=D1 Kc,
H_hat=-i L_hat=p D1+R beta+a Kc+bF.
```

H_hat is Hermitian. F is a commuting Hermitian involution with rank-two
eigenspaces s=+/-1. On each, Kc=sD1 and D1 anticommutes with beta, hence

```
lambda_(s,+/-)=s b +/- sqrt((p+s a)^2+R²).              (7)
```

Exact sector-square and characteristic-polynomial identities verify this.
The rotating-frame line gap is max(0,abs(R)-abs(omega)/48). Zero-frequency
symbols exist iff abs(R)<=abs(omega)/48, at
p=-s a +/- sqrt(b²-R²). These are continuum spectral points, not L2
eigenfunctions. The supplied mass amplitude alone misses this gradient
threshold. No physical mass or chirality claim follows.

For v=0, U is time independent, so the matched static original line
operator has the same spectrum. For v omega!=0 the original target is
time periodic with T=2pi/abs(v omega), and U(t+T)=-U(t). Its monodromy
is unitarily conjugate to -exp(-T L_hat). A band frequency lambda has
multiplier -exp(-i lambda T), so its quasienergy is shifted by pi/T modulo
2pi/T. The unbounded continuous line bands cover the entire unit circle
after exponentiation. A positive rotating-frame gap is therefore NOT a
Floquet spectral gap. Norm conservation follows separately from skewness.

On a spatial circle of length ell, nonzero rotating mass is periodic only
if omega ell=2pi n. U,W change by (-1)^n; periodic original fields become
(-1)^n-twisted frame fields, with xi1=(2pi k+n pi)/ell. Use (7) on this
discrete momentum set and the same time-monodromy sign when applicable.
Odd winding is not the same periodic domain. Neither the continuum gap
formula nor the whole-unit-circle Floquet-spectrum statement transfers to
the discrete spectrum. Fourier conjugation recovers real fields; F is
not a physical chiral selector.

## 6. Verification, hostile review and next construction

The producer and separate probe in tests/channel-swings pin K1832,K1836,
K1840,K1877,K1879. Complete-bank and amplitude results are reused; the
probe reconstructs every allowed bank row for the new tangent test. A
separate operator-action calculation checks (1). Actual mathematical faults
change derivative signs, potential/trace coefficients, frame signs, band
shifts and a dual entry. Reporting and input-pin checks are counted separately.
Analytic phase lifting, differentiation of a family, product rules and
Fourier/domain arguments establish continuum claims; finite totals alone do
not. No proof assistant or novelty claim is made.

Hostile review checks the radial remainder in (1), nonzero-speed/amplitude
assumptions, all Gram freedoms, the surviving positive circle, all-speed
versus generic-rank evidence, fixed-R versus family quantifiers, variable
versus constant frame coefficients, target versus source spectra, temporal
minus sign and spatial twists. These boundaries remain explicit.

The necessary target-profile classification is closed: only uniform circles
survive. Next construct an actual finite-R factorization from a different
base, or solve the variable-frame equations with B_hat fixed. A smooth
amplitude expansion from (4) cannot supply it. K1879's changed-target
connection remains a valid separate repair; native credit still requires
the actual full-C/injection/pairing/domain adapter. The band calculation
discharges none of those debts.
