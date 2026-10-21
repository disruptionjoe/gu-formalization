---
title: "K1871: Separated multidirectional conservative observations and their line-mode range"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact separated conditional interface, line localization and source-energy range; no native GU coefficients, physical chirality, index or family count
---

# Two orthogonal mass directions support a genuine two-coordinate interface

K1840's fixed positive energies and leading observation admit arbitrary static
m1(x1)B1+m2(x2)B2, with the two anticommuting mass matrices on different
axes. The full nonlinear cross defect vanishes. Reusing the same mass
direction on both axes fails this arbitrary-profile ansatz. More generally,
its axis mass vectors must be pairwise orthogonal in the two-dimensional mass
plane, so at most two independent nonzero axis profiles survive.

A double kink then carries a single real line mode per real4 target block.
Its zero frequency is absent from the observation image; a localized line
Gaussian also has no finite-energy massless lift. The optimal approximate
lifting error squared falls as pi/(4alpha B), where B is source energy.
This is much slower than the planar packet's exponential-in-B behavior.
These are facts about the conditional compressed interface, not a GU chiral
particle construction.

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
result: separated-axis conservative interface, cross compatibility and line observation range
carrier: K1840 compressed real16 source and real4 target on a supplied flat three-dimensional spatial product LAYER=toy CHIRALITY=N/A
pairing: fixed source integral u^T H u and target Euclidean L2 ON=real_square_integrable_fields
real_structure: real rational matrices; complex unitary Fourier transform with conjugate symmetry only for analysis
grading: spatial axes, two mass directions and normal involution sectors; no physical cohomology grading
action_owner: repository-construction -- conditional K1832/K1836/K1840 conservative compressed equations
target: separated multidirectional observation and its closed finite-energy image MAP-TYPE=quotient
```

## 1. Custody, prior work and the actual new question

[K1840](k1840-k77-conservative-variable-observation-2026-10-20.md) classifies
a44-dimensional pointwise conservative class, builds arbitrary one-coordinate
profiles, and excludes arbitrary two-coordinate dependence using the SAME
constant triple. The present construction uses DIFFERENT triples for the two
axes. It neither contradicts that exclusion nor solves the full nonlinear44-
dimensional system. [K1869](k1869-wall-observation-finite-energy-range-2026-10-20.md)
supplies the general closed-operator range theorem, reused below.

SC-OP-04 ASSERTS the candidate four-field grammar; SC-OP-05 remains UNCERTAIN
about southeast alternatives. SC-MAS-01 and SC-CHI-02 ASSERTS the stylized
curvature-mass/decoupling toy. SC-META-53 remains UNCERTAIN. WGS05 explicitly
leaves the full spinless-connection/scalar-curvature bundle map unconstructed.
None supplies these fixed compressed coefficients, two independent mass
profiles, positive physical domain or observation. RA-F1, AC-F1 and LT-SM8,
and the entire88-active/91-stored ledger, remain unchanged.

Dirac defect localization is classical; compare the primary work of
[Jackiw and Rossi, 1981](https://osiris.df.unipi.it/~rossi/NuclPhys190_1.pdf)
and [Lu, Watson and Weinstein](https://arxiv.org/abs/1808.01378).
We do not identify their complete models with this fixture or claim a new
index theorem. The question here is whether the held **source observation**
can support and reach a two-coordinate target, which localization alone
cannot settle. No novelty claim or source ownership is made.

## 2. Axis-specific repairs and complete cross compatibility in this ansatz

Keep the rational A_i,H,T_i,D_i,alpha of K1832/K1836; d_i=D_i/24.
The real symmetric D_i anticommute with each other, and the real skew B1,B2
satisfy Ba^2=-I and anticommute with each other and all D_i. For axis j and
mass direction a define

```
S_(j,a)=-24D_j B_a T_j.
```

Solve the held conservative linear system for H-skew C_(j,a):

```
T_i C_(j,a)-B_a T_i+S_(j,a) A_i-d_i S_(j,a)=0.         (1)
```

The certificate gives all six solutions in each of the four coordinate types.
It independently verifies

```
T_j C_(j,a)=d_j S_(j,a),   S_(j,a)C_(j,a)=B_a S_(j,a). (2)
```

At fixed B and S, the solution freedom has dimension6 and consists of
H-skew matrices C0 with T_i C0=0 for every i. Every S_(j,a) also annihilates
that image. Arbitrary smooth coefficients on these invisible directions
therefore cannot alter any cross defect, including their derivative terms.
The producer checks this from the kernel of the fixed-(B,S) projection,
rather than assuming uniqueness of one solver's chosen representative.

For j!=l define

```
R_(j,l;a,b)=S_(j,a)C_(l,b)+S_(l,b)C_(j,a)
            -B_a S_(l,b)-B_b S_(j,a).
```

Exact rational identities in ALL four coordinate types give

```
R_(j,l;1,2)=R_(j,l;2,1)=0,
R_(j,l;1,1)=R_(j,l;2,2)=R_(j,l),  rank R_(j,l)=4.     (3)
```

Thus for mass vectors v,w in R2, bilinearity gives R(v,w)=(v.w)R_(j,l).
Consider the additive separated ansatz with arbitrary independent functions
f_j(x_j), B=sum f_j B(v_j), C=sum f_j C_j(v_j), and S=sum f_j S_j(v_j).
The derivative/self-quadratic terms vanish by(2). The remaining defect is
sum_(j<l) f_j f_l(v_j.v_l)R_(j,l). Since each product coefficient can be
tested independently by setting the other profiles to zero, exact
intertwining for EVERY such profile choice holds iff the nonzero v_j are
pairwise orthogonal. This allows two nonzero axes and excludes three within
this precise additive ansatz. It is not an all-multidirectional no-go.

In particular choose v1=(1,0), v2=(0,1), no third profile, and set

```
M=m1(x1)B1+m2(x2)B2,
C=m1 C_(1,1)+m2 C_(2,2),  S=m1 S_(1,1)+m2 S_(2,2),
L_s=A_i partial_i+C, L_t=d_i partial_i+M, O=T_i partial_i+S.
```

Then O(partial_t+L_s)=(partial_t+L_t)O exactly. Both fixed positive energies
are conserved. No slow variation or small mass is assumed. Time dependence
would add -partial_t S and is not licensed by this static proof.

## 3. The exact adjoint square and closed-domain meaning

For this two-axis pair the independent coefficient checks give

```
T_i H^-1 S_(j,a)^T-S_(j,a)H^-1 T_i^T=0,
T_j H^-1 S_(j,a)^T=-24alpha D_j B_a,
S_(j,a)H^-1 S_(j,a)^T=576alpha I,
S_(1,1)H^-1 S_(2,2)^T+S_(2,2)H^-1 S_(1,1)^T=0.
```

Using the product rule, with only the profile's own coordinate differentiated,

```
OOdagger=alpha[-Delta+576(m1^2+m2^2)I
              -24D1 B1 m1'-24D2 B2 m2']
         =-576alpha L_t^2.                            (4)
```

Cross-mass and cross-derivative terms vanish for stated algebraic reasons;
discarding gradients would be wrong. The same identities hold after a fixed
orthogonal rotation of the mass pair, verified by bilinear coefficient
identities, not merely by two sampled angles.

Use bounded smooth profiles with bounded first derivatives on R3 or
R2 times a circle. The source and target generators are skew-adjoint on H1:
their constant elliptic symbols control that norm, and bounded skew
multiplication is a bounded perturbation. O is the closure of its smooth-
core operator. Dom(Odagger)=H1 by its injectively elliptic principal symbol;
Dom(O) need not equal H1 because the observation is underdetermined.
The norm identity ||Odagger psi||_H^2=576alpha||L_t psi||^2 on H1 identifies
closed nonnegative forms, extending(4). Smooth bounded derivative profiles
give the corresponding H2 target operator. These are supplied flat domains,
not a global curved GU construction.

## 4. Released double-wall test and the observed-image distinction

Let m_j(x_j)=h_j tanh(24h_j x_j), h_j>0. Define K1=D1B1 and K2=D2B2.
They are commuting symmetric involutions. For wall orientations e1,e2 in
{+1,-1}, the projector

```
P_e=(I+e1 K1)(I+e2 K2)/4
```

has real rank1, and D3 P_e=-e1 e2 P_e. With the respective mass signs e_j,
the normalized normal factor is

```
n(x1,x2)=sqrt(12h1)sqrt(12h2)
          sech(24h1 x1)sech(24h2 x2).
```

For a unit vector v in Range(P_e), psi=n v f(x3) solves the normal zero
conditions. The remaining equation is

```
partial_t f-(e1e2/24)partial_3 f=0.                  (5)
```

The normal kernel is exactly this sector for the kink pair: after squaring,
the two nonnegative normal squares add. A zero vector must solve both
first-order normal equations; their opposite involution sectors grow at an
end and are not L2. There is no hidden extra normal zero sector. This is
one real characteristic channel of a supplied model, not a physical particle,
a GU index, or a count obtained by multiplying coordinate-type fixtures.

On R2 times a circle, constant f is an L2 target zero mode. Equation(4)
puts it in ker Odagger, so it is absent from Range(O). On R3 a constant f is
not L2, and there is no nonzero L2 zero mode in this line sector. That does
not make the entire sector reachable with finite source energy.

## 5. All finite-energy line packets and the optimal Gaussian budget

The line subspace reduces T=OOdagger and T_line=alpha(-partial_3^2).
K1869's polar-decomposition theorem gives the exact criterion

```
psi=n v f is in Range(O)
 iff integral_R |fhat(k)|^2/k^2 dk < infinity,
minimum source norm squared = (1/alpha) integral |fhat(k)|^2/k^2 dk. (6)
```

The full source carrier is allowed; invisible/off-line components cannot
reduce this minimum. Use the unitary one-dimensional Fourier transform.
For Schwartz f, the criterion is equivalent to fhat(0)=0. Necessity follows
from continuity; sufficiency from fhat(k)=O(k) and rapid decay. The general
L2 criterion remains(6), not a claim that an undefined integral mean suffices.

Take the normalized Gaussian fhat(k)=pi^(-1/4)exp(-k^2/2).
It fails(6). For b>0 define

```
J(b)=(1/sqrt(pi)) integral_R exp(-k^2)/(k^2+b) dk
    =sqrt(pi) exp(b) erfc(sqrt(b))/sqrt(b).
```

The integral identity follows by writing1/(k^2+b)=integral_0^infinity
exp(-(k^2+b)t)dt, applying Tonelli, then substituting sqrt(1+t).
Differentiation gives J'=(1-1/(2b))J-1/b. The optimal source of a given
energy budget is the resolvent lift Odagger(T+alpha b)^-1 psi. Completing
the square at each frequency proves its constrained optimality exactly as
in K1869. Its energy and squared target error are

```
B(b)=[J+bJ']/alpha=[(b+1/2)J-1]/alpha,
E(b)=-b^2J'=b-(b^2-b/2)J.                            (7)
```

The integral representation B=(1/(alpha sqrt(pi))) integral
k^2 exp(-k^2)/(k^2+b)^2 shows it decreases strictly from infinity to0.
Each B>0 therefore selects one b. Taylor's formula at sqrt(b)=0 gives
J(b)=sqrt(pi)/sqrt(b)-2+O(sqrt(b)), hence

```
alpha B(b) ~ sqrt(pi)/(2sqrt(b)),
E(b) ~ sqrt(pi)sqrt(b)/2,
E_min(B) ~ pi/(4alpha B), B->infinity.                (8)
```

This is a sharp asymptotic for this normalized packet, with an exact implicit
finite-budget curve. It supplies no rigorous decimal budget without validated
transcendental evaluation. The comparison with K1869's planar Gaussian is
now decisive: line localization worsens this observation's low-frequency
cost from exponential accuracy in B to squared error of order1/B. Stronger
localization does not establish easier observation or a physical count.

## 6. A same-class gap repair and its precise threshold

Adding a third independent anticommuting mass is unavailable within this
real4 mass plane. A simpler allowed repair changes an existing profile:
replace m1 by h1 tanh(24h1 x1)+mu.
For |mu|<h1 the normal zero factor becomes

```
exp(-24mu x1)sech(24h1 x1),
```

which is still L2. The line obstruction survives; an arbitrarily small
constant shift is not a gap repair. At |mu|=h1 one end ceases to decay,
so the zero state leaves L2, but the asymptotic mass vanishes on that end;
no positive uniform gap follows at the threshold.

For |mu|>h1 let a=|mu|-h1>0. The shifted first profile has one sign and
absolute value at least a. With Q=(1/24)partial_1+m1, integration by parts
on the core gives |Re<f,Qf>|>=a||f||^2 and the same bound for Qdagger.
Cauchy--Schwarz therefore implies Qdagger Q>=a^2 and QQdagger>=a^2
as closed forms. These are the K1=+/- normal blocks of -L1^2.
The two normal generators anticommute and the profiles use separate
coordinates, so

```
-L_t^2=-L1^2-L2^2-(1/576)partial_3^2 >=a^2 I.        (9)
```

Consequently the entire closed observation is onto target L2, with right
inverse Odagger(-576alpha L_t^2)^-1 and norm at most
1/(24sqrt(alpha)a). This repair changes the supplied target wall profile
and destroys its normalizable line state. It does not make the original
massless line Gaussian observable. It uses the same conditional coefficient
class and positive pairings, with no native selection claim.

## 7. Verification, hostile review and next construction

Run the k1871 Sage producer and Python probe in tests/channel-swings.
The producer verifies305 exact matrix groups and3 dependency pins. The
independent Sympy implementation reconstructs raw entries and checks392
mathematical groups, including full value/derivative jets and the adjoint
square, plus11 reporting/pin checks. Nine coefficient, projector, propagation
and budget input faults, and4 reporting faults, fail genuine assertions
after a clean baseline. Six direct numerical integral comparisons separately
check the closed formulas; they are not rigorous quadrature. The finite checks do not prove closed-domain
extensions, spectral asymptotics or the continuum profile theorem; the
arguments above supply those steps. No formal proof or external acceptance
is claimed.

Preflight tested independent-axis repairs against K1840's actual nonlinear
residual instead of repeating its same-triple exclusion. Hostile review
checked representative freedom, arbitrary-profile quantifiers, the two-mass
plane limit, formal versus closed adjoints, circle versus line, target versus
observed modes, zero mean versus arbitrary L2, Fourier normalization, the
squared-error convention and the constant-shift threshold. Classical defect
localization is reused honestly; the full source/observation image is the
additional question. No unresolved defect is known at the stated scope.

The exact separated class and its useful line-range/gap consumers are now
settled. Further native credit requires the source-owned coefficient,
observation, pairing and domain adapter. A genuinely nonseparable profile
would instead require new S/C dependence solving the full44-dimensional
residual; arbitrary insertion into the six axis repairs is not that solution.
