---
title: "K2163 Mixed-degree seven-form adapter obstruction"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: declared fixed-splitting common-connection operator and commutant adapters only
scripts:
  - tests/channel-swings/k2163_mixed_degree_adapter_obstruction_probe.py
---

# K2163 Mixed-degree seven-form adapter obstruction

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2163 no nonzero mixed even-tangent-degree seven-form port descends through the declared commutant family
carrier: full real Cl77 S128 vector-spinor plus scalar with fixed W(3,1) and N(4,6) LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation, no supplied physical Hilbert form ON=declared_carrier
real_structure: real Clifford module, fixed gamma and independently declared reverse row
grading: full Dirac carrier; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction common upper and lower connection
target: complete coupled-equation observation descent MAP-TYPE=intertwiner
```

## Result and exact scope

[K2161](k2161-noncentral-adapter-obstruction-2026-10-27.md) excluded each pure tangent degree
0,2,4 separately. That proof did not exclude mixtures. This result excludes EVERY nonzero
Z in Lambda7(W+N) with tangent degrees0+2+4, jointly with all ten tangent-commutant
adapters, including singular and nondecomposable coefficients. No nonlinear parameter search
or positive-definite inner product is assumed. These are the1752 real coefficient directions
surviving K2155's literal all-null test, not a particle count. The full equation criterion is
stronger than null-functional survival.

SC-OP-04 ASSERTS a candidate four-independent-field operator. The
[source extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
does not select our simple contraction, reverse coefficient, real horn, fixed geometry or
adapter family. LT-SM8/LT-GR6b/AC-F1, full16cell/full20, K/C, physical quotient, native2+1 and
observed chirality are not discharged or falsified. Source, ledger and canon stay unchanged.

## 1. Original equation and mixed reduction

Reuse K2159's fixed W={0,1,2,7}, N its complement, eta=(+^7,-^7),
T_j commuting with every gamma_mu. Set f=sum_N T_j zeta_j and

    A_T(zeta,nu)=(zeta_W+gamma_W f, nu-Gamma_N zeta+2f),
    R_T(E,F)=(E_W-gamma_W sum_N T_j E_j, F-sum_N T_j E_j).

Their tangential principal identity holds. Kernel column j has zeta_j=I,
zeta_mu=-gamma_mu T_j, nu=eta_j gamma_j-2T_j. Set a_i={Z,gamma_i}/2 and use the SAME
coefficient in both rows:

    E_i=sum_l eta_l gamma_l(a_l zeta_i-a_i zeta_l)+a_i nu,
    F=-sum_l eta_l a_l zeta_l.

Every complete descent, constant or smooth T, requires L_mu,j=E_mu^j-gamma_mu F^j=0.
Equation projection cancels, as do the smooth-adapter terms gamma_mu H_j and H_j,
H_j=sum_W eta_mu gamma_mu partial_mu T_j. Fixed gamma/splitting is essential.
For Z=Z0+Z2+Z4 the original maps yield, linearly in each Zr,

    L_mu,j^(r)=[(7-r)gamma_mu Zr-(10+2r)a_mu^(r)]T_j
               +eta_j([gamma_mu,a_j^(r)]+gamma_mu a_j^(r)).       (1)

The derivation uses sum_V eta gamma a=7Zr, sum_W eta a gamma=rZr and
sum_W eta gamma a_mu gamma=(6-2r)a_mu. It is checked against the original maps,
not only against the simplified formula.

Put omega=gamma0 gamma1 gamma2 gamma7, omega²=-I. The exhaustive tangent commutant is
T_j=A_j+omega B_j, A_j even in Cl(N), B_j odd in Cl(N). Normal parity separates the
homogeneous A contribution from the forcing; the even-normal part alone must vanish.
For fixed j let Xr=Zr omega B_j (tangent degree4-r), Nr=eta_j a_j^(r) (degree r).
For even-normal coefficients let epsilon_mu and iota_mu be tangent exterior multiplication
and metric contraction. The W-degree1 and3 parts of that even-normal residual are

    Y_mu=gamma_mu(N0-15X4)+iota_mu(5X2+3N2),
    V_mu=iota_mu(7X0+3N4)+epsilon_mu(N2-9X2).                    (2)

Contracting once more gives exact projection certificates:

    sum_W eta_mu gamma_mu Y_mu=4(N0-15X4)+2(5X2+3N2),
    sum_W eta_mu gamma_mu V_mu=4(7X0+3N4)+2(N2-9X2).             (3)

The first separates W-degrees0,2; the second separates4,2. Hence
N0=15X4, 5X2=-3N2, 7X0=-3N4, 9X2=N2. The last two degree2 equations force N2=0,
and sum_N eta gamma a_j^(2)=5Z2 forces Z2=0. Mixtures cannot hide the degree2 port.

## 2. The remaining coupled degrees0 and4

Write Z0=v in Lambda7N and Z4=omega u, u in Lambda3N. Define d_jx={x,gamma_j}/2
for these odd forms. Equations(3) reduce exactly to

    u B_j=-(eta_j/15)d_jv,
    v B_j=-(3eta_j/7)d_ju.                                    (4)

If one of u,v is zero, contraction injectivity forces the other zero. Assume both nonzero.
Equation(4) puts every d_jv in the right ideal uCl(N); contracting
sum_j eta_j(d_jv)gamma_j=7v yields v in uCl(N). Similarly u in vCl(N), so
I=uCl(N)=vCl(N). All d_ju belong to I, and gamma_j u=2d_ju-u gamma_j belongs to I.
Therefore gamma_j(uc) belongs to I for every c: I is a nonzero TWO-SIDED ideal.
The even-dimensional nondegenerate real Clifford algebra Cl(4,6) is simple, so I is all
Cl(N). Finite dimensionality makes u and v invertible. Singular ports have not been excluded
by assumption; their proposed solution itself would force invertibility.

For completeness, simplicity and scalar center here need no real-type table. In even dimension,
the sign characters of conjugation by the ten invertible generators distinguish all1024
Clifford basis blades. Averaging those conjugations with a blade's character projects any
nonzero ideal element onto a nonzero invertible blade. Thus every nonzero two-sided ideal
contains1. The only blade commuting with every generator is the scalar blade.

## 3. An incompatible second Clifford representation

Define C=sum_j B_j gamma_j, with NO additional eta weight. Contracting(4) yields

    uC=-(7/15)v,  vC=-(9/7)u,  C²=3/5.

Let alpha_j=u^-1 gamma_j u. Substitution, preserving product order, gives

    B_j=(eta_j/14)(C gamma_j+alpha_j C),
    C B_j=(eta_j/10)(gamma_j+alpha_j),
    C alpha_j C=(4gamma_j+7alpha_j)/5.                         (5)

The automorphism tau=Ad_C is an involution because C² is nonzero scalar. Write
alpha_j=p_j+q_j, tau(p_j)=p_j and tau(q_j)=-q_j. Equation(5) gives

    gamma_j=(3/4)tau(alpha_j)-(7/4)alpha_j=-p_j-(5/2)q_j.

Both alpha and gamma obey the original Clifford anticommutators. Separating tau parity
in the alpha relation gives the mixed anticommutator zero and
{p_i,p_j}+{q_i,q_j}=2g_ij. The gamma relation gives
{p_i,p_j}+(25/4){q_i,q_j}=2g_ij. Consequently {q_i,q_j}=0 and {p_i,p_j}=2g_ij.
The p_j therefore define a unital Cl(N) homomorphism whose image commutes with C.
Simplicity makes it injective and equal finite dimensions make it onto Cl(N). Thus C
commutes with ALL Cl(N), so C is a nonzero real scalar. But v=-(15/7)uC would identify
nonzero pure grade7 with a scalar multiple of pure grade3. The direct Clifford grading
makes this impossible. This proves Z=0 is necessary.

## 4. Consumers, controls and next boundary

The argument is pointwise. A smooth mixed Z(x), with fixed gamma/splitting, must vanish
at every point where this complete descent is required. Smooth adapter derivatives cannot
repair the obstruction. At Z=0 the remaining derivative criterion is H_j=0; constant
adapters are positive controls. A supplied scalar tangential connection a_mu=lambda_mu I,
a_N=0 passes every constant commutant adapter and lies outside the seven-form hypothesis.
Changing the lower coefficient, the adapter ansatz, or allowing moving gamma/splitting is
a new mathematical construction; no obstruction for those classes is proved here.

The degree mixture is now exhausted rather than requeued. The next useful source-interface
construction must actually change and type one of those data, then recheck the principal
identity and complete coefficient/derivative kernel jointly. Merely retaining a characteristic
null functional or searching more noncentral parameters cannot undo this result. No full
source-operator uniqueness, global domain theorem or GU verdict follows.

## Evidence and status

The companion probe checks original coupled maps, mixed W-degree projection and trace
certificates, nonzero singular inputs, metric-weighted contractions, distinct conjugation
characters, and scalar/zero positive controls. Genuine changed equations and commutant inputs
must fail after a green baseline. Universal simplicity, right-ideal and representation
arguments are written proofs reviewed independently; finite controls do not prove them alone.
Internal specialist acceptance is not proof-assistant, external-expert or novelty certification.
