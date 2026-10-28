---
title: "K2209 Spin connections preserving the raw positive sector"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete fourteen-component Spin coefficient classification on the supplied V1152 sector; no source physical selector
scripts:
  - tests/channel-swings/k2209_spin_common_return_probe.py
---

# K2209 Spin connections preserving the raw positive sector

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
result: complete1274-to28 common Spin coefficient and24-dimensional positive-current classification
carrier: real1920 raw K77 restricted to observed covectors0,7,8,9 and supplied invariant V1152 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: inherited positive Euclidean V current; separate trace-Hq compatibility test ON=declared_carrier
real_structure: real Cl77 spinors, complexification only for Fourier spectrum
grading: Clifford grade2 connection and observed volume Q; neither is a physical-family label
action_owner: repository-construction -- original raw common coefficient and lower return, no fitted adjoint return
target: invariant-sector transfer, conservative potentials and absence of a constant spectral gap MAP-TYPE=intertwiner
```

## Result and exact class

K2206's massive coefficient is grade13, not Spin-valued. This does not
exclude it from the separately mentioned full unitary connection arena.
The new question is what happens if the common connection IS Spin-valued,
without imposing K2206's normal-Clifford commutation in advance.

Keep the full real128 spinor, eta=(+1 seven,-1 seven), observed
O={0,7,8,9}, normal U=its ten-element complement, J=gamma0...gamma13,
W=(3I-J)/2 and Wbar=(3I+J)/2. Use the original raw D_k, normalization
R_a=eta_a gamma_a, R_h=Wbar, and the inherited sector

    V={u_a=0 (a in O), u_h=0, sum_(r in U)u_r=0}.

The present ENTIRE class is

    Omega_k in real Lambda2(R77), k=0,...,13,
    K=sum_(k=0)^13 D_k diag(Omega_k,...,Omega_k),
    L=sum_(k in O) D_k partial_k+K.                         (1)

There are1274 independent real connection coefficients. The principal derivatives
remain observed-only; normal connection components are retained in K. The same Omega acts
in every raw slot; the bottom return is still -eta_c Omega_c, with zero
southeast block. No full-H symmetry is imposed and no lower return is fitted.
For this class:

| Requirement | Coefficient dimension | Induced image dimension |
| --- | ---: | ---: |
| Arbitrary fourteen-component Spin coefficient |1274|not necessarily an endomorphism of V|
| Evolution preserves V |28|8|
| V preserved and inherited positive current conserved |24|4|
| V preserved and trace-Hq compatible for a fixed nonzero normal q |24|8|
| All three requirements |20|4|

The invariant-sector transfer kernel is20-dimensional. Every observed
connection component is a tangent bivector. The ten normal components are
exactly Omega_r=eta_r v gamma_r for one arbitrary tangent vector v. Every
Spin coefficient preserves ambient chirality. Trace-Hq compatibility for even
one fixed nonzero normal q forces v=0; the remaining24-dimensional class
then passes for EVERY normal q.
The conservative induced image is Q(c+b dot C), where Q=gamma0 gamma7 gamma8
gamma9, Cj=gamma0 gamma_j. Constant such coefficients shift two cones and
have no spectral gap anywhere on the real energy line. Smooth variable
coefficients still give exact local positive conservation and finite speed.

This is a complete statement for all1274 Spin-valued coefficients in(1),
not the full unitary parent, not every positive subspace, and not a prohibition
on gaps from variable backgrounds, boundaries or different contractions.

## 1. Invariance forces normal commutation instead of assuming it

D0 preserves V invertibly, so evolution invariance is equivalent to K(V)
being contained in V. The ORIGINAL bottom return has normalized normal-input
block -(W/2)Omega_c gamma_c. Its vanishing on all sum-zero tuples says

    Omega_c gamma_c=v independent of c in U.

For each c, multiplying a bivector by gamma_c produces a vector or a
trivector. A vector blade gamma_a can lie in this image exactly when a!=c;
a trivector can lie in it exactly when c belongs to its support. Intersecting
these images over all ten normals leaves precisely the four tangent vectors:
no trivector contains all ten normals. Thus v is a tangent vector and
Omega_c=eta_c v gamma_c. This is both necessary and sufficient for the
bottom-row equation, including arbitrary cancellation across coefficients.

Put alpha_c(X)=eta_c gamma_c X gamma_c. For an
observed output row a and normal input c, direct substitution in the ORIGINAL
raw formula gives the normalized block

    K_ac = [sum_(k in O, k!=a) gamma_k alpha_c(Omega_k)-9v] Wbar. (2)

Each of the nine normal k!=c terms contributes -v because
Omega_k=eta_k v gamma_k and v is tangent. This contribution is independent
of c, so it cancels from the differences below.

An operator annihilates all sum-zero normal input tuples precisely when its
coefficients are equal across the ten input slots. Hence for c,d in U define
Delta_k=alpha_c(Omega_k)-alpha_d(Omega_k). The four observed leakage equations
are

    E_a=sum_(k!=a) gamma_k Delta_k=0, a in O.

Summing gives sum_a E_a=3 sum_k gamma_k Delta_k, and thus

    Delta_a=eta_a gamma_a[(sum E)/3-E_a].                  (3)

This exact inverse shows that no cancellation between different connection
components can evade the condition: all alpha_c(Omega_a) must be equal.

Conjugation is diagonal on the faithful Clifford-blade basis. On a bivector,
alpha_c has sign minus if c is in its support, plus otherwise. Equal signs
for all ten normal indices require the support to contain none or all ten.
Grade two rules out the latter. Therefore every Omega_a is a tangent
bivector. This necessity uses only the observed output rows; it is not a
numerical rank guess.

Conversely tangent bivectors commute with every normal gamma and with J.
The auxiliary output vanishes by its common-v relation. The full normal output,
including its diagonal, is

    (K u)_r=-[sum_(k in O) gamma_k Omega_k-8v]Wbar u_r, r in U,

on sum-zero tuples; the sum of these outputs is zero. Thus the condition is
sufficient on all fifteen raw rows. Normalizing by D0 yields nine identical
spinor equations

    partial_t u+sum_j Cj partial_j u+N u=0,
    N=gamma0 [sum_(k in O) gamma_k Omega_k-8v].             (4)

## 2. Complete induced image, kernel and current

Clifford multiplication O tensor Lambda2(O) -> Lambda1(O)+Lambda3(O)
is onto: choose k in an exterior triple to obtain that triple, or choose
Omega_k proportional to gamma_k gamma_l for k!=l to obtain gamma_l.
Multiplication by gamma0 is invertible. Thus N spans the entire8-dimensional
even Clifford algebra of O already when v=0. The additional term -8gamma0 v
is in that same image. Thus the28-dimensional coefficient map has kernel20.

Its transpose-symmetric basis elements are I and the three Cj; its
transpose-skew basis elements are the three spatial bivectors and Q. They
are linearly independent. The fixed positive energy condition N^T+N=0
therefore imposes exactly four independent conditions. Its coefficient
preimage has dimension24 and its image dimension4. With v=0 the coefficient
preimage is20-dimensional, recovering the complete observed-only subcase.

Q^T=-Q, Q^2=-I and [Q,Cj]=0. The three Q Cj span the spatial bivectors,
so the entire conservative image is

    N=Q(c I+sum_j b_j Cj), c,b_j real.                    (5)

For example Q C7=gamma8 gamma9. A boost coefficient Omega0=gamma0 gamma7
preserves V but fails positive-energy conservation. A mixed coefficient
Omega0=gamma0 gamma1, with every other component zero, is Spin-valued but
leaks out of V. In contrast a nonzero v with its ten tied normal components
does preserve V; appropriate tangent components can cancel its symmetric
image and give conserved evolution. The normal sector was not discarded. These are actual
coefficient controls, not assertions that every Spin connection is harmless.

There is also NO nonzero element of the entire even tangent Clifford image
anticommuting with all three Cj. The membership equations are
bit(0)+bit(j)=1 modulo2. On the four tangent indices the only solutions are
{0} and {7,8,9}, both odd. This is a useful mass test, but the full spectrum
below is stronger: a failure of the textbook anticommuting ansatz alone
would not prove absence of every spectral gap.

## 3. Exact two-cone spectrum and the common domain

Complexify and define the sector label by iQ=sI, s=+1 or -1; equivalently
Q=-isI. For constant coefficients the Hermitian Fourier Hamiltonian is

    H(p)=p dot C-iN,
    H_s(p)=-s c I+(p-s b) dot C,
    E_s,plus/minus(p)=-s c +/- |p-s b|.                   (6)

Each Q sector has dimension64: gamma0 anticommutes with Q and exchanges
them. Within either sector and for nonzero v, v dot C has both eigenvalues
+|v| and -|v| with equal multiplicity32. Indeed choose a nonzero real w
orthogonal to v; w dot C is invertible, preserves Q and anticommutes with
v dot C. Thus neither frequency branch in(6) was assumed absent. On V
these multiplicities are multiplied by9. At v=0 the eigenvalues coincide.

For any E in R choose |p-s b|=|E+s c| and the appropriate sign in(6).
Every real E occurs in the symbol spectrum; wave packets concentrated near
that momentum give approximate spectral vectors. The full-space operator
therefore has spectrum R and no global gap, even if H(0) is invertible.
This is not a theorem about a bounded spatial domain or a variable potential.

On L2(R3;C1152), H0=-i sum Cj partial_j is self-adjoint on H1 because
H0(p)^2=|p|^2I. Constant -iN is bounded Hermitian, so H=H0-iN is self-adjoint
on that SAME H1 domain; Fourier multiplication gives its unitary evolution.
The domain equivalence also follows directly by bounding the constant
potential in the graph norm. No physical quotient or ambient14D domain is
inferred.

## 4. Variable coefficient consequence and source compatibility

For smooth real c(x,t),b(x,t), equation(4) with(5) obeys

    partial_t(u^dagger u)+sum_j partial_j(u^dagger Cj u)=0. (7)

There is no derivative-of-potential term in this identity. Since C(n)^2=I
for a unit spatial n, |u^dagger C(n)u|<=u^dagger u. Cone integration gives
unit-speed propagation for smooth compactly supported data, with the usual
approximation extension whenever the evolution is constructed.

For a time-independent bounded potential the same H1 self-adjoint domain
works. For a bounded Hermitian potential continuous in time in operator norm,
the interaction-picture Volterra series converges on every finite time
interval, with nth term bounded by (M |t|)^n/n!. Adjoint differentiation and
backward evolution give a unitary propagator. This supplies a controlled
variable-potential construction, not arbitrary unbounded-domain closure.

At the reduced equation level exp(Q theta) supplies an Abelian phase change;
the four potential coefficients transform by a gradient, and a nonzero
exterior derivative is an obstruction to removing them by that phase.
This is NOT automatically a gauge transformation of the raw Spin connection:
Q is grade4, so the derivative of that phase can leave its grade2 class.
No source gauge identification is needed for(7).

Separately, for every normal vector q, gamma(q) commutes with each tangent
Omega, and the B-adjoint of a bivector is minus itself. Therefore, when v=0,

    Omega^dagger Hq+Hq Omega
      = iB[Omega^* gamma(q)+gamma(q)Omega]=0,
    Hq=iB gamma(q).                                      (8)

For the normal coefficient Omega_r=eta_r v gamma_r, the bracket in(8)
is instead [gamma(q),Omega_r]=-2 q_r v, writing gamma(q)=sum q_r gamma_r.
For any fixed nonzero q, at least one q_r is nonzero; compatibility for all
connection components forces v=0. This remains algebraically true for a
nonzero null q, though nondegenerate Hq requires non-null q. Thus the joint
class is exactly24-dimensional, with a20-dimensional conservative subset.
For an explicit converse control, set v=gamma0 and Omega7=8gamma0 gamma7,
with other tangent components zero. Their induced images cancel exactly,
so N=0 conserves the positive current while the normal connection fails(8).
The boost control above passes(8) but fails that current.
Trace-Hq compatibility thus
neither selects the positive current nor creates a mass. It remains a
separate form from the source fermion action's tested pairing lines.

The source extraction for9.16 confirms four independent classical fields,
all sixteen cells and source ambient-half labels; it does not select this
raw contraction, the observation, V or a closed physical domain. The source
full U(64,64) arena permits more than Spin bivectors. K2206 supplies an actual
odd-coefficient massive countercontrol beyond this restricted class.
Hence this result is not adverse evidence against the source-native mechanism.

## Verification and boundary

The sparse probe exhausts the bottom-image supports of all910 normal
bivector coefficients, reconstructs original raw blocks for all364 remaining
observed input basis coefficients, verifies(3) on all nine independent
normal-slot differences, checks every full raw output row for all28 survivors,
and tests induced rank,
energy rank, trace-Hq, chirality, the Clifford identities and actual cone
crossings. The probe also verifies the full128 Clifford spectral polynomial on each
complex Q sector, not only a scalar cone formula. Baseline and exact failure
counts are stored in the report. Mutating the inverse coefficient1/3 to1/2
causes864 failures; adding a false positive squared mass in the actual
frequency equation causes two failures; replacing the normal coefficient8
by9 breaks the full raw sector transfer. Mixed and boost coefficient
countercontrols bind real invariance and current defects. These are exact
rational/Clifford checks, not proof-assistant or external-expert certification.

The universal proofs, not the number of checks, establish completeness.
A bounded duplicate scan found K2036 uses a fixed full-H form and its chosen
adjoint return, while K2206 imposes normal commutation in its arbitrary-grade
mass class. Neither supplies the original-return1274-to28 theorem above.
No external novelty claim follows from that repository scan.

The complete Spin-valued connection class is now exhausted for this fixed
raw positive sector. A substantial successor must change the coefficient
algebra, contraction or selected sector explicitly, or analyze a specified
variable background with a distinct observable; restoring the normal
connection components is already included. Rechecking grade13 is not itself
a new successor.
