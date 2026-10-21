---
title: "K1887: Bounded variable-frame rotation has a nonlinear distance barrier"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: canonical-base bounded or periodic coefficient obstruction and necessary nonlinear distance/residual bounds; no exclusion of all rotating lifts or native GU identification
scripts:
  - tests/channel-swings/k1887_bounded_variable_frame_rotation.py
  - tests/channel-swings/k1887_bounded_variable_frame_rotation_probe.py
---

# Bounded variable frames cannot perturbatively repair the canonical rotating base

K1885 excludes differentiable constant-frame mass branches from its canonical
massless base. Allowing arbitrary variable-frame coefficients does not supply
a uniformly small repair: an exact dual flux forces a nonlinear distance
barrier for every bounded whole-line or periodic candidate. In particular,
there is no amplitude family differentiable at zero with a bounded tangent.
The new bound also constrains isolated finite-amplitude and nondifferentiable
candidates near that same base. It does not exclude a sufficiently distant
base, unbounded coefficients or every local solution.

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
result: exact dual flux, nonlinear distance and residual barriers for bounded variable-frame rotating observation candidates
carrier: K1840 real16 source and real4 target in all four coordinate types LAYER=toy CHIRALITY=N/A
pairing: fixed positive source H and Euclidean target; coefficient bounds use the declared coordinate Frobenius norm ON=smooth_local_tests_and_bounded_or_periodic_coefficients
real_structure: real travelling coefficients and actual real source-target complex structures
grading: differential order and amplitude regularity; no physical grading
action_owner: repository-construction -- fixed-symbol conservative first-order equations
target: full differential observation factorization near the canonical massless rotating frame MAP-TYPE=quotient
```

## 1. Preflight, inherited data and precise question

The pinned data are K1832's positive energy and principal matrices, K1836's
leading differential observation, K1840's complete conservative pointwise
bank and K1885's exact all-speed dual. K1879 supplies the frame change; it
need not be rerun to prove covariance here. The nearest earlier result is
K1885's constant-frame tangent exclusion. The present result retains the
coefficient derivatives which that constant ansatz lacks, then controls their
boundary flux instead of discarding them.

The operative construction is the repository's compressed real16-to-real4
system. SC-OP-04 ASSERTS candidate four-field grammar; SC-MAS-01 and SC-CHI-02
ASSERTS stylized curvature-mass and decoupling claims; SC-OP-05 and
SC-META-53 remain UNCERTAIN. The actual full-C/injection/pairing/domain adapter
is not supplied by this result. No source adherence, RA-F1, AC-F1, LT-SM8,
physics-ledger mapping or canon verdict changes. This is neither a physical
chirality calculation nor a native GU exclusion.

The structural PDE lens asks whether a differential left obstruction survives
variable coefficients. The nonlinear-analysis lens retains quadratic terms
and distinguishes uniform norm differentiability from pointwise parameter
differentiability. The algebra lens checks every conservative direction and
all nonzero speeds, including characteristic speeds. The domain lens checks
finite intervals, the line and circles separately. A nonlinear existence
search far from the canonical base is a distinct surviving alternative.
Object searches for variable-frame/bounded branches and secular obstructions
found K1885 and the different null-source range problem in K1861, not this
flux barrier. This is a repository comparison, not a priority or novelty claim.

## 2. Full variable-frame equations and exact dual flux

Set z=x1-vt and h=omega/2. Work with real v,h,R, initially allowing zero
values as controls. Let d_i=D_i/24 and use the actual intertwiners L,J.
The canonical unit-frequency massless frame is

```
Cbar=(vI-A1)L, Bbar=(vI-d1)J, Sbar=-T1L.
```

The constant-frequency canonical base is h times this triple. Keep its
principal symbols and leading observation fixed and write

```
C=h Cbar+c(z), S=h Sbar+s(z), B=h Bbar+R B1.              (1)
```

The target is the constant frame of the pure mass-plane uniformly rotating
profile in K1885. C,S may be arbitrary C1 functions of z. They must satisfy
HC+C^T H=0 and all three first-order equations

```
T_i C-B T_i+S A_i-d_i S=0.
```

The complete bank therefore contains (c,R B1,s) pointwise; no preferred
slope, offset or mass-local dependence is imposed. The full zeroth-order
residual, defined with the OP-QO sign, is

```
E=T1 c'+(vI-d1)s'
  +h(Sbar c+s Cbar-Bbar s-R B1 Sbar)+s c-R B1 s.          (2)
```

The +v s' sign comes from subtracting partial_t S=-v S'. Exact
intertwining means E=0.

Write K1885's 70-entry polynomial dual as y=(yt,yb), with six target-skew
coordinates followed by 64 row-major residual coordinates. Put
Y=reshape(yb,4,16). The certified complete-bank identities are

```
yt dot b + <Y,Sbar c+s Cbar-Bbar s>_F=0,
yt dot b1+<Y,B1 Sbar>_F=v.                              (3)
```

Here b lists the six upper-triangular entries of the target coefficient,
and b=R b1 for the actual deviations. Thus no generic-rank assumption or
exceptional-speed division enters. Define

```
lambda=<Y,T1 c+(vI-d1)s>_F.
```

Pair (2) with Y and use (3):

```
<Y,E>_F=lambda'-h R v+<Y,s c-R B1 s>_F.                 (4)
```

For exact factorization this proves the central identity

```
lambda'=h R v-<Y,s c-R B1 s>_F.                         (5)
```

The eight nonzero Y entries in types0,1 are

```
(0,1):11/192-v/4, (0,2):11/192+v/4,
(0,5):1/16, (0,6):-1/16, (0,12):f, (0,15):f,
(2,1):25/192, (2,2):-25/192,
```

where f=1/16 for type0 and f=1/8 for type1. Type3 is the negative of type0;
type2 is the negative of type1. Hence the exact norm is

```
N_v²=||Y||_F²=v²/8+517/9216  (types0,3),
                  v²/8+733/9216  (types1,2).            (6)
```

The six-coordinate dual part is retained in the certificate, even though
only Y occurs in the final flux. Dropping it before using (3) would lose the
inhomogeneous mass forcing.

## 3. Nonlinear barrier for bounded or periodic candidates

Suppose c,s are bounded on the whole line, and define finite coordinate norms

```
epsilon_c=sup_z ||c(z)||_F, epsilon_s=sup_z ||s(z)||_F.
```

B1^T B1=I, so ||B1||op=1. Cauchy-Schwarz and matrix norm submultiplicativity
give

```
|<Y,s c-R B1 s>| <= N_v epsilon_s(epsilon_c+|R|).        (7)
```

Integrate (5) over any interval of length ell. Bounded c,s imply bounded
lambda; after division by ell, its endpoint contribution tends to zero
as ell tends to infinity. This proves

```
|h R v| <= N_v epsilon_s(epsilon_c+|R|).                 (8)
```

No average limit for the nonlinear term is assumed. Periodic coefficients
satisfy the same inequality by integration over one period, with zero
endpoint term. A finite interval without matching endpoints is different.

If both deviations are at most epsilon, solve the quadratic inequality:

```
epsilon >= [sqrt(R²+4|h R v|/N_v)-|R|]/2.               (9)
```

At fixed nonzero h,v and R approaching zero this is asymptotic to
sqrt(|h v| |R|/N_v). Thus a uniform O(R) perturbation cannot supply the lift.
The bound covers isolated finite-R candidates and families without amplitude
differentiability. It is a necessary distance bound, not evidence that a
square-root branch or any other branch exists. The norms are fixed-coordinate
Frobenius norms, not an invariant physical distance.

More generally, if epsilon_s=O(|R|^a) and epsilon_c=O(|R|^b), with a,b>0,
then (8) rules out a+b>1. It does not prove that a+b<=1 is sufficient.
If s vanishes identically, no exact lift in this class exists for hRv!=0,
regardless of how c varies. If epsilon_c stays small while R is fixed,
(8) gives an explicit necessary lower bound on epsilon_s.

## 4. Bounded variable tangents and the correct regularity statement

Suppose an amplitude family satisfies the equations near R=0, equals the
canonical base at R=0, and is differentiable there in C1_loc so that the
coefficient equations can be differentiated. Let c1,s1 be its parameter
derivatives. The nonlinear term in (5) is second order, giving

```
lambda1'=h v,
lambda1=<Y,T1 c1+(vI-d1)s1>_F.                          (10)
```

For h v!=0 this is incompatible with a bounded c1,s1 on the whole line,
or periodic c1,s1. Differentiability into the uniform bounded-coefficient
norm is a sufficient boundedness hypothesis. Alternatively (8) directly
excludes uniformly O(R) families without differentiating equations.

Pointwise-in-z differentiability of individually bounded family members is
NOT enough: tanh(Rz) has bounded members and unbounded derivative z at R=0.
No theorem here excludes such nonuniform parameter behavior merely because
each member is bounded. The nonlinear bound still applies to each exact
member, but a pointwise limit need not approach the base in the uniform norm.
Likewise the scalar necessary equation lambda1=hvz+constant shows why a
local or secular escape is not excluded; it does not construct a full lift.

On a circle, omega ell=2pi n makes the original mass periodic. U,W change
by the same sign(-1)^n, so the two signs cancel in the transformed C,S
coefficients. Periodic original coefficients therefore give periodic frame
coefficients. Odd winding cannot evade (8) or (10) through this sign.
The field domain itself still changes between periodic and antiperiodic
when n is odd, exactly as in K1879/K1885; coefficient periodicity and field
domain are different statements.

## 5. Finite intervals expose the boundary-flux cost

Let t=||T1||_F. The actual matrices give

```
t²=12888/625 (types0,3), 12792/625 (types1,2).
```

Since D1 is a symmetric involution,
||vI-d1||op=|v|+1/24. On an interval of length ell, bounding the two endpoint
values of lambda yields

```
|h R v| <= 2 N_v[t epsilon_c+(|v|+1/24)epsilon_s]/ell
           +N_v epsilon_s(epsilon_c+|R|).              (11)
```

If d=|hRv|-N_v epsilon_s(epsilon_c+|R|)>0, any candidate kept inside these
coefficient bounds has length at most

```
ell <= 2 N_v[t epsilon_c+(|v|+1/24)epsilon_s]/d.         (12)
```

This is a spatial travelling-coordinate interval, not a universal time bound.
Along a fixed spatial location with v!=0, traversing such an interval takes
ell/|v|; the same bound becomes a duration bound for maintaining these
coefficient bounds along that trajectory. It is not a bound on a maximal
existence time outside the stated neighborhood.

For the tangent problem, if both ||c1||F and ||s1||F are at most epsilon,
(10) instead requires

```
epsilon >= |h v| ell/[2 N_v(t+|v|+1/24)].               (13)
```

Thus a local perturbative attempt cannot keep one fixed coefficient bound
on arbitrarily long intervals. The endpoint term must not be omitted for a
local problem.

## 6. A residual floor for approximate nonlinear searches

Retain exact conservation and the pointwise first-order bank, but allow the
zeroth-order residual E in (2), with sup||E||F<=delta. Equation (4), integrated
for bounded whole-line or periodic coefficients, gives

```
delta >= max(0,|h R v|/N_v-epsilon_s(epsilon_c+|R|)).     (14)
```

A finite-interval version subtracts the endpoint term in (11), divided by N_v,
inside the maximum. This is a useful rejection threshold before a large
nonlinear search near the canonical base: a target residual below the floor
cannot be achieved in that neighborhood. It is not a posterior error bound
for arbitrary approximate solutions; errors in the first-order bank would
need additional terms and are not covered.

## 7. Verification, contrary controls and next question

The producer reuses K1885's matrix assembly without rerunning its rank search,
checks the full polynomial dual, norms, frequency scaling, actual static-slope
projected defect and exact quadratic budget. The independent probe reconstructs
every conservative bank row and its energy/first-order equations, rebuilds the
dual action, and expands OP-QO on constant test fields with arbitrary exact
coefficient jets. The latter verifies derivatives and nonlinear products;
complete-bank membership is verified separately, not assumed for those arbitrary
jets. A clean baseline precedes matrix, operator, boundary-flux, reporting and
input-pin mutations. Only explicit FAIL assertions count as detected faults.
The executed producer passes 34 exact dual/budget groups and five input pins.
The independent clean baseline passes 544 bank/matrix controls, 12 operator
checks, ten budget controls and 17 reporting/pin checks. Eight mathematical
faults and six reporting/pin faults are rejected by explicit assertions.
These totals combine different evidence kinds and are not independent
continuum proofs. The analytic expansion and integration above carry the continuum conclusions.
No proof assistant, external expert acceptance or novelty is claimed.

The actual saved static repair has sc-RB1s=0, and its projected residual at
the canonical rotating base is exactly -hRv in all four types. This confirms
that its good static nonlinear cancellation cannot hide the rotating defect.
For v=0, h=0 or R=0 the obstruction vanishes; static mass repairs and the
massless canonical frame survive. K1879's non-mass connection changes the
target class and remains valid. Characteristic speeds v=+/-1/24 require no
special exception because the dual is polynomial and N_v remains positive.

Hostile review targets bounded tangent versus bounded family members,
canonical-base versus all-base quantifiers, necessary versus sufficient
square-root scaling, both derivative signs, the full 44-dimensional bank,
Frobenius versus operator norms, finite-interval endpoint flux and odd winding.
The result eliminates uniformly perturbative bounded/periodic searches from
this canonical base. A different base, a finite-amplitude solution outside
the quantified neighborhood, or an unbounded/local construction remains a
meaningfully different research task. Native GU credit separately requires
the actual full-C, injection, pairing and observation-domain adapter.
