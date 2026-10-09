---
title: "A real stationary curved background for the selected canonical I1B reconstruction"
status: active_research
claim_verdict: exact_local_stationary_background_in_declared_reconstruction
doc_type: analytic_construction_and_exact_certificate
created: 2026-10-08
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
spec_row: SA-U1
canon_verdict_change: none
receipt: lab/process/native-zorro-stationary-background.json
probe: tests/channel-swings/native_zorro_stationary_background_probe.py
---

# A stationary curved background

**There is a real, nonzero stationary local bosonic background for the
selected canonical connection metric and `comm/symi/symi` I1B action.**
Its distortion has Clifford grades one and two. All distortion equations
vanish, including variations outside the ansatz. Epsilon stationarity follows
from an exact dressing identity; observing-metric stationarity follows from
the derivative-only dependence on that metric at a constant base metric.
These last two arguments are proved below with their variation domain.

This removes the local-background obstruction for this declared reconstruction.
It does not select the reconstruction uniquely from the source, supply a
global finite-action domain, prove a physical observation quotient, or establish
positive energy or quantum unitarity. No source polarity, SA-U1/H59 status,
hypothesis vote or canon grade changes. In particular SC-META-53 stays
`UNCERTAIN`. The source's printed residual and the actual I1B Euler
derivative are distinct owners: the construction solves the latter.

Classification: `SOURCE_NATIVE_ROUTE` with an explicit reconstructed operator
and geometry. There is no conventional Yang–Mills replacement or physical
comparator inference here. Read
[source-native routing](../../lab/methods/source-native-comparator-routing.md)
before joining this result to another action.

```gu-typed-objects
result: exact local stationary bosonic background and full distortion receiver closure
carrier: real Clifford-valued one-form on the canonical curved metric bundle Y over a constant Lorentzian observing metric; epsilon and base metric varied as specified LAYER=ambient+source-print BRIDGE=declared_canonical_reconstruction CHIRALITY=N/A
pairing: exterior top-degree scalar Clifford trace; Hodge operator of G_Y ON=ambient_forms
real_structure: real grade-one and grade-two background in Cl(7,7); zero full complex-linear Euler covector also annihilates the source phased real slice
grading: de Rham degree and Clifford grade; horizontal, vertical-traceless and vertical-trace projectors
action_owner: source-action -- equation 9.4 with the stated comm/symi/symi realization and kappa-over-two mass normalization; not the printed residual or I2B
target: local stationarity and a background for future constrained perturbations MAP-TYPE=evaluation
```

## 1. Geometry, action and field

Use a coordinate patch of `X=R^4` and a constant observing metric
`g=diag(1,-1,-1,-1)`. At the metric-fibre point `h`, set

```text
G_Y(g) = h_ij dx^i dx^j + D_h(theta,theta),
D_h(A,B) = tr(h^-1 A h^-1 B) - tr(h^-1 A)tr(h^-1 B)/2,
theta_ab = dh_ab - (Gamma(g)^c_ia h_cb + Gamma(g)^c_ib h_ac) dx^i.
```

Here `h` varies independently of `g`. This is the same declared
[canonical reconstruction](../nguyen-gu-critique/section-3-1-end-to-end-assessment-2026-10-08.md)
and plus-first convention used in the preceding curvature certificate.
`Gamma(g)=0` leaves a curved fourteen-dimensional metric: its Ricci
endomorphism is `1/4` on the horizontal and vertical-trace directions and
`-5/4` on the nine vertical-traceless directions. Its scalar curvature is
`-10`. Nothing in this construction sets its spin curvature to zero.

Write `P_H`, `P_0`, `P_r` for those three orthogonal projectors. The vertical
vector `r=(0,h/2)` has norm `-1`. Direct Levi-Civita differentiation gives

```text
nabla r = P_H/4,       P_r z = -G_Y(r,z) r.
```

These are identities of fields on the patch, not values of a freely selected
jet. `gamma` denotes Clifford multiplication. Define the real distortion

```text
T(z) = a gamma((P_H+P_0)z) + c gamma(P_r z)
       - (v/8) gamma(r) gamma(P_H z)
       + w gamma(r) gamma(P_0 z).                         (1)
```

The perpendicular factors in the last two terms make them pure grade two.
All four coefficients are constant. The last term, mixing the vertical
trace and traceless directions, is essential for the branch constructed here.
It is an intrinsic tensor, not an independently substituted connection.
Set epsilon to the identity and set the source translation variable equal
to this `T`; the source connection is `A=B+T`, with `B` the spin
Levi-Civita connection of `G_Y`.

The selected bulk action is exactly the predecessor's normalization:

```text
I = integral_Y Tr[T wedge S(F_B)
       + (1/2) T wedge S(D_B T)
       + (1/3) T wedge S(T wedge T)
       + (kappa/2) T wedge *T].                            (2)
```

The brackets in `S` are the declared `comm/symi/symi` realization of source
equation (9.3). Its two symmetrized channels each carry `i`, so the selected
operator is real on the real Clifford packet. Equation (9.4), including its
displayed normalization ambiguities, motivates this selected action; source
uniqueness of these choices is not asserted. No sum with I2B is introduced.

## 2. The full distortion equations

The calculation varies (2) before imposing (1). In a covariant normal frame,
with compactly supported variation `U`, its first-order contribution is

```text
(1/2) sum_s { <U,S(e^s wedge nabla_s T)>
              - <nabla_s T,S(e^s wedge U)> }.
```

The minus term is the formal adjoint; replacing the derivative by the
printed swerved-curvature equation would give a different calculation.
The cubic derivative is

```text
(1/3) <U,S(T wedge T)>
 + (1/3) <T,S(U wedge T + T wedge U)>.
```

The probe independently reevaluates all five representative first-order
rows from these two varied terms. It derives the entire polynomial image
by exact polarization of the cubic functional.

Take the rational orthonormal frame from the geometry probe, with trace
index `10`. The complete covector has **27 possibly nonzero rows**, all
proportional to these five equations:

```text
16 E_H = 4224 a^2 + 768 ac + 16 a kappa
         + v^2 - 72 vw - 3v + 768 w^2 + 108w - 84,

24 E_0 = 6336 a^2 + 1152 ac + 24 a kappa
         + 3v^2 - 128 vw - 12v + 896 w^2 + 168w - 90,

24 E_r = 7488 a^2 + 24 c kappa
         + v^2 - 144 vw - 6v + 864 w^2 + 216w - 126,

24 E_Hr = 132 av - 3168 aw + 12a
          + 4cv - 288cw - 12c + 3 kappa v,

3 E_0r = 22 av - 352 aw + 3a
         + 2cv - 24cw - 3c - 3 kappa w.                   (3)
```

The multiplicities are respectively `4,9,1,4,9`. The representatives are
`e^0 gamma_0`, `e^4 gamma_4`, `e^10 gamma_10`,
`e^0 gamma_0 gamma_10`, and `e^4 gamma_4 gamma_10`.
No count of physical degrees of freedom is inferred from them.

**Completeness of the receiver calculation.** Label a basis component by
`exterior_mask XOR Clifford_mask`. Each diagonal invariant `Phi_i` has
label zero, a Hodge operation toggles the full exterior mask, and a
top-degree trace pairing cancels that full mask. The fields in (1) have
only labels `0` and `2^10`. Thus every cubic Euler receiver lies in those
two labels, comprising 28 candidate one-form receivers of arbitrary
Clifford grade. The scalar receiver `e^10 1` vanishes identically. The
probe separately computes every linear, curvature and mass receiver,
including any outside this set; there are none. This establishes zero
against all `14 * 2^14` real Clifford basis variations, not merely against
the four ansatz variations. Complex linearity then also gives zero on the
source's phased real adjoint slice. Grades one and two of the background
itself are in the real slice displayed on source p42.

There is a short retained failed route. Omitting the final term in (1)
sets `w=0`, and (3) implies

```text
E_0-E_H = (v^2-5v+24)/16
        = (v-5/2)^2/16 + 71/64 > 0.                     (4)
```

So no member of that smaller family solves the equations. The earlier
three-projector no-solution certificate also remains unchanged. The
successful construction uses a component those failed families omit.

## 3. Exact real algebraic solution

Put `a=kappa alpha`, `c=kappa beta`, and define

```text
D = 22v^2 - 220vw - 15v - 3168w^2 + 732w,
alpha = -3(2v^2 - 20vw - 3v - 288w^2 - 12w)/(8D),
beta  =  3(22v^2 - 220vw + 3v - 3168w^2 + 12w)/(8D).
```

These solve the last two equations of (3). The difference of the first
two gives the conic

```text
B(v,w) = 3v^2 - 40vw - 512w^2 - 15v + 12w + 72 = 0.
```

Let

```text
H = 4224 alpha^2 + 768 alpha beta + 16 alpha,
R = 7488 alpha^2 + 24 beta,
V_H = v^2 - 72vw - 3v + 768w^2 + 108w - 84,
V_r = v^2 - 144vw - 6v + 864w^2 + 216w - 126.
```

The remaining equations are `V_H R - V_r H=0` and
`kappa^2=-V_H/H`. Eliminating `v` with the conic gives a squarefree
degree-ten polynomial `P(w)`. The probe derives its coefficients and
the rational function `v(w)` from the linear remainder on division by
`B`; the [receipt](../../lab/process/native-zorro-stationary-background.json)
records the exact polynomial and all rational parameter formulas.

Define `w_*` to be the unique real root of `P` in

```text
227427945967/10^12 < w_* < 227427945969/10^12.
```

Sturm root counting gives exactly one root there. Exact rational interval
arithmetic bounds every denominator away from zero and gives

```text
2.873978 < kappa_*^2 < 2.874152.
```

Choose the positive square root. All five equations reduce to zero
exactly modulo `P`, with denominator coprimality also checked. This is
an algebraic existence proof, not a small-residual numerical root. For
orientation only, the resulting constants are approximately

```text
(a,c,v,w,kappa) = (0.151945, -0.195077, 3.79821, 0.227428, 1.69531).
```

The coupling is a selected parameter of this background, not a derived
physical mass or a source prediction. This establishes one real branch;
it does not assert existence for every prescribed coupling.

## 4. From a point calculation to a stationary source-variable germ

### The fields solve the equations on an open patch

The displayed metric at `Gamma(g)=0` is invariant under translations of
`x` and the simultaneous affine transformation of `x` and congruence
transformation of `h`. Congruence is transitive on the chosen metric
signature. The trace vector and all projectors in (1) transform naturally,
as do the Levi-Civita connection, Hodge operation, Clifford product and
Euler covector. Local oriented spin lifts suffice. Therefore the exact
equations at `h=diag(1,-1,-1,-1)` transport to the open signature patch.
This uses the actual smooth tensor fields (1), not independently assigned
first jets. It supplies their higher jets and integrability automatically.

### Epsilon is handled by the exact dressing identity

Let `D_0` denote the induced spin connection and let
`B_epsilon=epsilon^-1 D_0 epsilon`, interpreted as a connection.
Define the dressed distortion

```text
tau = epsilon T_epsilon epsilon^-1
    = epsilon varpi epsilon^-1 - (D_0 epsilon) epsilon^-1.
```

Conjugating the source formulas gives

```text
epsilon F_Bepsilon epsilon^-1 = F_D0,
epsilon (D_Bepsilon T_epsilon) epsilon^-1 = D_0 tau,
epsilon S_epsilon(xi) epsilon^-1 = S_1(epsilon xi epsilon^-1).
```

Hodge acts on exterior indices and commutes with coefficient conjugation;
the trace is cyclic. Consequently the **actual selected functional**
satisfies `I(g,epsilon,varpi)=I(g,1,tau)` identically. All epsilon
variations act through `delta tau`. Since its unrestricted Euler covector
vanishes, compactly supported epsilon variations vanish as well. This is
not an appeal to source equation (9.6) or to the printed residual; it is
an identity of the chosen action. It also means that epsilon redundancy
cannot by itself remove a nonzero dressed distortion perturbation.

### The independent observing metric is stationary

In the fixed fibre chart, `G_Y(g)` depends on the observing metric only
through `Gamma(g)`. All other structures in (2) are constructed locally
from this ambient metric and finitely many of its jets. At constant `g`,

```text
delta Gamma(g)^l_ij
 = g^lm (partial_i delta g_mj + partial_j delta g_mi
         - partial_m delta g_ij)/2.
```

There is no undifferentiated `delta g` term. Differentiating in a fibre
direction cannot remove a base derivative of `delta g`. One may choose a
local spin-frame identification depending only on the ambient metric;
its variation has the same property. Thus, at this background, the full
local first variation has the form

```text
delta_g L(x,h) = sum_(|alpha|>=1) C_alpha(h) partial_x^alpha delta g(x).
```

All coefficients are independent of `x`, because the background metric,
distortion and their coordinate jets are. Integration against any
compactly supported base-metric variation in a base coordinate patch
therefore vanishes, by integration by parts in `x` alone. There is no
discarded fibre boundary term in this argument. If a choice of field
identification changes `T` while varying `g`, its extra contribution is
zero because `E_T=0` has already been proved.

The precise variational domain is a product patch `U_x x V_h` with a
relatively compact fibre patch, local action density (2), compact support
in `U_x` for the independent base-metric variations, and compact interior
support for distortion and epsilon variations. The product patch makes
the variational integrals finite. This proves local source-variable
stationarity. It does **not** claim convergence of the integral over the
entire noncompact metric fibre, arbitrary moving fibre boundaries, or a
closed physical Hamiltonian domain. In particular, moving `h` is not
substituted for varying `g`.

## 5. Verification and the next mathematical question

The focused probe passes 22 exact checks. Its certificate covers the
coordinate trace-vector derivative, complete distortion equations,
independent formal-adjoint coefficient checks, Sturm isolation, rational
intervals, algebraic identities and the failed `w=0` control. Its final
observing-connection check verifies the finite jet formula; the local
variation and dressing proofs above are analytic arguments, not a claim
that the script formalizes functional analysis. No new Lean theorem or
independent later verification is claimed.

```bash
uv run --no-project --with sympy==1.14.0 python -B tests/channel-swings/native_zorro_stationary_background_probe.py
```

The next substantive calculation is the **coupled second variation at this
background**. It must retain the observing-metric response, the dressed
distortion constraints, and the actual observation map. A positive mass
matrix on the four ansatz coefficients (`diag(13,1,1/16,9)`) is not the
physical kinetic form, and the ansatz has not been shown to be a closed
perturbation sector. The old flat-background growing mode cannot be
transferred to this curved, nonzero-distortion equilibrium by name.

| Claim | Prior status | Current status | Remaining dependency |
| --- | --- | --- | --- |
| Local stationary background in this canonical I1B reconstruction | Three-projector family excluded; construction open | Exact real grade-one/two local branch | Independent verification before any canon promotion |
| Physical quadratic action and stable positive sector | Open | Open | Coupled constraints, observation reduction and common time/domain |
| SA-U1/H59 and SC-META-53 | Open; UNCERTAIN | Unchanged | Physical and quantum construction, not existence of an equilibrium alone |
