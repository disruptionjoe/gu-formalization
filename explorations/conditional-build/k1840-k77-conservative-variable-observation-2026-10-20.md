---
title: "K1840: conservative variable-mass observation and its missing wall zero mode"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional compressed variable-coefficient interface; no source curvature identification, physical mass or chiral count
---

# An exact non-frame repair permits arbitrary one-coordinate mass profiles

The fixed leading observation from K1836 can support a genuinely varying mass
magnitude while preserving the original positive energies. It needs a specific
zeroth-order correction and a different conservative source coefficient. The
repair works for any two smooth static mass profiles depending on one spatial
coordinate. It solves the full equations of K1838, beyond its separately
imposed pointwise-lift subclass.

The repair has a consequential limitation. Its observation times its weighted
adjoint equals a positive multiple of the squared target spatial generator.
A chosen domain-wall profile therefore has target zero modes which the
observation misses in the natural L2 domain. Nonzero wall frequencies can be
lifted; a second allowed mass gaps the wall and removes that particular
zero-mode obstruction. These are conditional interface results, not a source
chirality mechanism.

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
result: conservative variable-mass intertwiner, exact adjoint square and wall-mode image boundary
carrier: corrected compressed real16 module and real4 target; four coordinate types LAYER=toy CHIRALITY=N/A
pairing: fixed K1832 positive source H and Euclidean target L2 ON=real_smooth_fields
real_structure: rational matrices and real mass profiles; complex Fourier modes only for spectral analysis
grading: differential order and spectral frequency; no physical cohomology grading
action_owner: repository-construction -- demand-selected massive Dirac target and conditional compression
target: one-coordinate variable-coefficient differential observation MAP-TYPE=quotient
```

## 1. Source boundary, preflight and corrected expectation

SC-OP-04 ASSERTS the candidate four-field operator grammar. SC-OP-05 is
UNCERTAIN about its southeast alternatives. SC-MAS-01 ASSERTS a **stylized**
R(y)/4 mass on approximately constant-curvature regions; SC-CHI-02 ASSERTS
its stylized coupled Weyl decoupling, not a physical threshold or a selected
wall. The source pack WGS-05, lines236-291, leaves the scalar-curvature and
spinless connection coefficient's full bundle-map identification open.
SC-META-53 is UNCERTAIN. None of these supplies the present compressed
matrices, observation, energy or profile. RA-F1, AC-F1 and LT-SM8 remain NEEDS;
source adherence and all ledger dispositions are unchanged.

The actual question is whether locality and a fixed positive energy obstruct
variable mass in the existing interface. The preflight compared a complete
conservative coefficient classification, an arbitrary fitted potential, and
source-owned coefficient identification. Complete classification is the
cheapest way to test the claimed obstruction without fitting a source fact.
K1084's variable-mass Laplacian commutator is already known but is not this
first-order intertwining problem. The August11 moving anti-dualizer Darboux
construction concerns a preboundary potential and does not solve it either.

The first hypothesis was that only a12-dimensional connection/mass/invisible
class survives conservation. Exact elimination **rejects that hypothesis**:
the full class has dimension44. The additional32 correction directions are
essential for the repair below. Its explicit positive construction makes a
broad conservative variable-mass no-go unavailable. The ordinary Dirac target,
positive pairing and its mass parameters are imported conditional choices;
none is silently identified with a same-named source object.

## 2. Complete conservative pointwise classification

Use the actual rational A_i,H,T_i,D_i and positive alpha from K1832/K1836,
with d_i=D_i/24. The source matrices are H-self-adjoint, the D_i are symmetric
Clifford generators, and T(xi)H^-1T(xi)^T=alpha|xi|²I. Set

```
P=partial_t+A_i partial_i+C, Q=partial_t+d_i partial_i+B,
O=T_i partial_i+S.
```

Repeated spatial indices are summed. Impose fixed-energy conservation
HC+C^T H=0 and B+B^T=0. The first-order intertwining equations are

```
T_i C-B T_i+S A_i-d_i S=0.                                      (1)
```

Parametrize C=H^-1U with U skew (120 coordinates), B skew (6), and arbitrary
S (64). The resulting192-by190 rational system has rank146 and nullity44
in each of the four coordinate types. Its B projection is all six skew4-by4
matrices; its S projection has dimension35. The complete rational kernel is
serialized, and independently assembled finite-field rank plus rational
kernel identities verify completeness. Counting an asserted dimension alone
would not verify this classification.

Equation(1) is only the pointwise first-order part. The remaining exact
condition is

```
T_i partial_i C+S C-partial_t S-d_i partial_i S-B S=0.             (2)
```

No general nonlinear classification of all44 directions is claimed.

For comparison, covariantizing the old constant mass lifts with one common
complex structure J gives a12-dimensional subclass: six invisible skew
coefficients, temporal and three spatial U(1) connection coefficients, and
two masses. In that subclass the remaining defect is linear in six curvature
components and six spatial covariant mass derivatives. Their exact coefficient
map has rank12. Thus it forces flat connection and covariantly constant mass
spatially **within that subclass**. This is a local conclusion; flat global
holonomy need not be trivial. The full44-dimensional class is larger.

## 3. Exact arbitrary-profile repair

Let B1,B2 be K1836's two real skew mass matrices, satisfying

```
Ba²=-I, B1B2+B2B1=0, Ba D_i+D_i Ba=0.
```

For each a=1,2 put

```
Sa=-24 D1 Ba T1.                                                (3)
```

The rational system(1) has an H-skew solution Ca with B=Ba,S=Sa in every
coordinate type. All matrices and full identity checks are in the certificate.
No source coefficient is adjusted after an empirical comparison. These
constant triples obey

```
T1 Ca=d1 Sa,   Sa Ca=Ba Sa,
S1 C2+S2 C1=B1 S2+B2 S1.                                      (4)
```

For arbitrary smooth real functions m1(x1),m2(x1), define

```
M=m1 B1+m2 B2, C=m1 C1+m2 C2, S=m1 S1+m2 S2,
L_s=A_i partial_i+C, L_t=d_i partial_i+M, O=T_i partial_i+S.
```

Then OP=QO exactly, where P=partial_t+L_s and Q=partial_t+L_t.
The first-order terms vanish by(1). The derivative part of(2) vanishes by
T1 Ca=d1 Sa, and the quadratic part by(4). Thus the proof permits arbitrary
profile magnitude, orientation, zeros and derivatives, without a slow-variation
approximation. The static and one-coordinate hypotheses matter.

There is also a structural explanation for the nonlinear cancellation. From
(3) and the Clifford relation, S A1=M T1. Equation(1) for i=1 therefore gives
T1 C=d1 S. Hence SC=-24D1 M T1C=-24D1 M d1 S=M S.
The choice of conservative C solving(1) is not unique: arbitrary skew maps
supported on the common kernel of the T_i may be added; they are invisible
to S as well. Their arbitrary spacetime-dependent coefficients preserve the
intertwiner. They do not change M or select a source mechanism.

This is a genuine mass-magnitude repair. M²=-(m1²+m2²)I may vary; the fixed
positive source and target energies survive. It is not the pure-frame rotation
of constant mass in K1838 and does not use that artifact's varying scalar
energy weight. The separate pointwise equations T_iC=M T_i generally fail,
so K1838's correctly scoped obstruction remains valid.

### A dimensional limitation of this particular factorization

Suppose one SAME constant conservative triple(C*,B*,S*) must support
C=f(x1,x2)C*, B=f(x1,x2)B*, S=f(x1,x2)S* for every smooth f, including arbitrary
independent first derivatives. Besides(1), it must satisfy
T1 C*=d1 S* and T2 C*=d2 S*. Exact elimination gives only dimension6, all with
B*=S*=0 and T_iC*=0. Thus this factorized ansatz cannot carry a nonzero
arbitrary two-coordinate mass. It does not exclude special two-coordinate
solutions, multiple profile-dependent coefficients, moving principal symbols,
or general solutions of(2). No rotational covariance beyond the checked
coordinate statements is assumed.

## 4. Adjoint square, domains and exact image boundary

Let the source inner product be integral u^T H v and the target Euclidean L2
product. On smooth compactly supported fields the weighted adjoint is

```
O†=-H^-1 T_i^T partial_i+H^-1 S^T.
```

Exact coefficient identities, for each a, give

```
T_i H^-1 Sa^T-Sa H^-1 T_i^T=0,
T1 H^-1 Sa^T=-24 alpha D1 Ba,
Sa H^-1 Sa^T=576 alpha I,
S1 H^-1 S2^T+S2 H^-1 S1^T=0.
```

Together with the K1836 principal Gram identity, they prove

```
O O†=alpha[-Delta+576(m1²+m2²)I-24D1 M']
     =-576 alpha L_t².                                        (5)
```

The sign is fixed by L_t being a **skew-adjoint spatial evolution generator**.
The squared target equation is

```
psi_tt-Delta psi/576+(m1²+m2²)psi-d1 M' psi=0.                  (6)
```

The gradient term cannot be dropped; a pointwise negative eigenvalue of its
potential does not contradict nonnegativity of the full factored operator
-L_t². Its arbitrary second-order solutions still owe the first-order equation.

For this paragraph use the static constructed C, with no additional time-dependent
invisible term. For bounded smooth profiles with bounded derivatives, use R×T², R³, or a
periodic three-torus as appropriate. The particular source symbols have
spectral moduli |xi| and |xi|/24 in the H energy, while the target Clifford
symbol has modulus |xi|/24. Their graph norms therefore control H1. Bounded
skew multiplication perturbations preserve skew-adjointness and the H1
generator domains. Smooth compactly supported/periodic functions are a core.
Both conserved L2 energies and their isometric evolutions are well-defined
(unitary after the stated Fourier complexification).

Define O as the closure of its smooth-core operator, and O† as its Hilbert
adjoint. The formal adjoint has injectively elliptic principal symbol, with
||H^-1 T_i^T partial_i psi||_H²=alpha||gradient psi||². Its bounded zeroth
term preserves the graph norm, so Dom(O†)=H1. O itself is underdetermined;
its closed source domain is not asserted to be H1. By density, the core
identity extends to

```
||O†psi||_H²=576 alpha ||L_t psi||², psi in H1.
```

Thus(5) identifies the closed nonnegative target quadratic forms. Smooth
bounded coefficients with bounded derivatives also give their H2 operator
realizations. These are the conditional flat-product systems, not a global
curved GU domain theorem.

On the smooth core, integration by parts in O L_s=L_t O gives
L_s O†=O† L_t. On a spectral subspace of
-L_t² bounded away from zero, an explicit right inverse is

```
R=O†(-576 alpha L_t²)^-1.                                     (7)
```

Intertwining follows first on smooth spectral vectors from the adjoint identity,
then by closure on the compatible evolution domains. Conversely, any
L2 target vector in ker L_t lies in ker O† by(5), and is orthogonal to the
L2 image of O. Nonzero such vectors cannot be observed from any source in
Dom(O). Equation(7) is not a bounded inverse through zero; no all-target
surjectivity follows from the nonzero-frequency principal symbol.

## 5. Released test: a wall, its lost zero mode, and a permitted gap

Choose, purely as a conditional test on R×T²,

```
m1(x1)=m0 tanh(24m0 x1), m0>0, m2=0,
K=D1 B1, K²=I, K^T=K, rank((I+K)/2)=2 per real4 target.
```

For every constant v with Kv=v,

```
psi(x1)=sech(24m0 x1)v
```

is an L2 normal zero mode of L_t: its derivative is -24m1 psi. Its constant
transverse extension is L2 on R×T² and remains stationary. It is a nonzero
member of ker O†, so it is **absent from the observation image** on that
domain. Directly, (24T1^T+S1^T)v=0 proves the same fact. On R³ a transverse
constant is not L2, so that particular global statement must use the stated
product domain or a fiberwise Fourier interpretation.

D2,D3 commute with K. The rank2 normal sector therefore supports a tangential
massless2+1 Dirac equation with speed1/24. At nonzero transverse Fourier
wavevector k, -L_t²=|k|²/576 on that sector, and(7) becomes
u=O†psi/(alpha|k|²). It is a true lift at each nonzero k, with the declared
low-frequency loss, not an inferred physical family count. For normal static
source solutions another direct identity is O=T1 A1^-1 L_s, so their
observations vanish as well.

A simple admissible repair tests robustness: retain the kink but choose the
second allowed profile m2=mu, a nonzero constant. B2 commutes with K and
anticommutes with D2,D3. The same normal sector is invariant and now has

```
-L_t²=|k|²/576+mu².
```

The entire wall sector, including k=0, admits(7). There is a stronger global
consequence. Write L0=d_i partial_i+m1(x1)B1. Since B2 anticommutes with every
term of L0, for ANY bounded smooth real m1 the constant second mass gives

```
-L_t²=-L0²+mu²I >= mu²I.
```

Therefore(7) is a bounded right inverse on the **entire target L2 space**,
with norm at most1/(24 sqrt(alpha)|mu|). Indeed
||R psi||_H²=<psi,(-576alpha L_t²)^-1 psi>, and the displayed gap gives the
bound. The observation is surjective in its closed L2 domain, ker L_t=0, and
the right inverse transports the target dynamics to source dynamics. Source
ker O may still contain invisible fields. This supplied second mass removes
the zero-frequency obstruction without changing the principal fixture or
energy. It does not supply a source-selected sign change, symmetry protection,
or physical chirality. A wall in a fitted conditional target is not the source's effective
non-chiral-to-chiral mechanism.

## 6. Verification, hostile review and next question

```
sage -python tests/channel-swings/k1840_k77_conservative_variable_observation.py
sage -python tests/channel-swings/k1840_k77_conservative_variable_observation_probe.py
```

The producer solves the complete conservative rational system and checks all
repair, adjoint-square, two-axis and wall Clifford identities in every
coordinate type. The separate probe reconstructs raw-entry coefficient
systems over a finite field, verifies the rational kernel and repair directly,
and applies the operators to polynomial fields with two different mass
profiles. Wrong derivatives, omitted S, and altered coefficients fail concrete
identities. Reporting-scope mutations are counted separately. The written
product rule, factorization and domain argument own the arbitrary-profile
and continuum conclusions; no sampled direction or manifest assertion does.

Hostile review checks the false12-dimensional premise, conservation versus
source pairing, static versus moving mass, both cross-profile terms, exact
adjoint signs, one-coordinate versus all-space claims, target zero modes
versus observed modes, global L2 domains and the second-mass repair. Remaining
work is the general nonlinear44-dimensional class, genuine multidirectional
mass or variable-principal compatibility, and the actual source-owned
coefficient/observation/pairing bridge. No source/ledger/canon promotion,
novelty assertion or external specialist acceptance is claimed. The domain-wall
mechanism itself is classical; compare the primary mathematical treatment
[Dirac operators and domain walls](https://arxiv.org/abs/1808.01378).
The new conditional contribution is this fixture's exact conservative
observation, its adjoint square, and the resulting image/repair statements.
