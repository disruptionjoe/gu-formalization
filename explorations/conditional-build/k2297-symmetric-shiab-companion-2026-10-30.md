---
title: "K2297 Symmetric Shiab injection and companion constraint"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
claim_ceiling: selected flat T0 quadratic germ and restricted symmetric lift only
scripts:
  - tests/channel-swings/k2297_symmetric_shiab_companion_probe.py
---

# K2297 Symmetric Shiab injection and companion constraint

> **GU-COMPARATOR-ROUTING — scope before inference.** This calculation uses the selected K77 I1B trace/Hodge operator, not a freely substituted Einstein action. Its Einstein pairing is proved on the specified flat horizontal packet. It supplies no observation, physical source, quotient or global-domain bridge. See [source-native routing](../../lab/methods/source-native-comparator-routing.md).

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: K2297 Symmetric Shiab injection and companion constraint
carrier: real symmetric horizontal metric variations injected into K77 Clifford-valued one-forms LAYER=ambient CHIRALITY=N/A
pairing: scalar Clifford trace and fourteen-dimensional Hodge wedge ON=declared_carrier
real_structure: exact Cl(7,7) real coefficients in selected comm/symi/symi row
grading: distortion grade1 and full companion grade2; metric symmetric rank2 is not exterior grade2
action_owner: source-action -- I1B grammar with repository-selected Shiab and flat T0 germ
target: coupled metric and distortion Euler covectors MAP-TYPE=evaluation
```

## Result and scope

The ten-input horizontal symmetric injection has the required Einstein dual pairing, but it is not closed under the full companion equation. The exact derivative companion is equivalent to the curl of the symmetric tensor. On a contractible flat horizontal patch its homogeneous solutions are scalar Hessians; their linearized Einstein tensor is zero. Consequently the bare symmetric-distortion ansatz cannot support a nonzero smooth metric-row source when the full distortion companion is unsourced. An enlarged distortion solution or a typed distortion source is necessary before consuming the projected Einstein inverse.

This resolves the injection/companion condition left open after K1861 and [K129](selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md). It is a scoped construction obstruction, not a GU verdict. SC-ACT-01/02 ASSERTS the I1B/Einstein-like action and equation, and SC-GEO-55 ASSERTS connection displacement from gauge-rotated Levi-Civita. Their source polarity does not change. The source does not uniquely select the tested Shiab row; [the source reinspection](../../lab/sources/gu-i1b-conormal-weld-domain-source-reinspection-2026-08-05.md) preserves that caveat. LT-GR1b/GR6b/GR10/GR11 and ledger0.263 are unchanged.

## 1. Exact injection and curvature normalization

Use the existing K77 orthogonal frame, eta=(+---,++++++,----), with horizontal indices0..3. For a real symmetric4x4 tensor u define

    j(u)=sum_{a,b<4} eta_b u_ab dx^a gamma_b.                       (1)

There is no extra factor1/2 or trace reversal. With normalized scalar Clifford trace and the14D Hodge star,

    <j(u),*j(v)>=sum_{a,b<4} eta_a eta_b u_ab v_ab.                 (2)

Off-diagonal symmetric basis elements have norm2eta_a eta_b; treating only the upper triangle as an orthonormal basis loses a factor2.

At the flat T=0 germ set S=selected Shiab(comm,symi,symi), and A h=S(F'_B(h)). For real derivative symbol k (replace derivative by k, NOT ik), use

    R'_{ijab}=1/2[k_j k_a h_ib+k_i k_b h_ja
                 -k_j k_b h_ia-k_i k_a h_jb],
    F'_{ij}=sum_{a<b}eta_a eta_b R'_{ijab} gamma_ab,
    Ric'_{mn}=sum_a eta_a R'_{a m a n},
    G'=Ric'-eta R'/2.                                             (3)

This is -1/2 the unnormalized K132 rank tensor. The Fourier convention flips the second-derivative sign; no rank-only normalization is imported as an equation coefficient. Direct evaluation on all ten h inputs and all ten quadratic covector coefficients proves

    A h=-2 *j14(G'14 h),
    <j(u),A h>=<u,-2G'4 h>_metric.                                (4)

The ambient G'14 includes vertical diagonal -eta_alpha R'/2. They are orthogonal to horizontal j(u), not absent from A. Equation(4), the flat formal self-adjointness of G', and fixed-boundary integration give A* j(u)=-2G'4u. No physical matter interpretation follows from this pairing alone.

## 2. Complete companion coefficient

K129's actual quadratic action is [[0,A*],[A,C]], with

    C=kappa K+E(D),
    E_k(v,j(u))=1/2[<v,S(k wedge j(u))>-<j(u),S(k wedge v)>].       (5)

The minus sign is essential: integration by parts makes a real first-order formal-Euler coefficient skew. The raw density and its transpose are not separately the Euler equation. K is the nondegenerate Hodge flat map, of grade1 on j(u); E(D)j(u) is grade2, so kappa K cannot cancel its grade2 equations.

Clifford grade rules exhaust the receivers: commutation with grade1 takes grade1 to grade2, while the two anticommutator stages in the selected second term also yield grade2. Conversely S(k wedge v) can have grade1 only when v has grade2. This is the1--2 edge of [K132's complete grade graph](selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md), not extrapolation from24 horizontal receivers. The probe evaluates all14*91=1274 grade2 receivers for each of the four horizontal derivative directions.

Each axis matrix has rank9,58 nonzero receiver rows, and kernel span{e_t tensor e_t}. The null representative e0+e3 also has rank9 with kernel span{k tensor k}. Their four-axis common kernel is zero. This last statement alone would not exclude nonconstant solutions, so the differential condition is evaluated next.

Two exact witnesses illustrate the missed equations. At k=e0, u=diag(0,1,-1,0), v=dx1 gamma01, the forward coefficient is-2, transpose+2, and Euler coefficient-2. For u01=u10=1 and v=dx4 gamma14, forward0, transpose-2, Euler+1. The latter is genuine vertical leakage lost by dropping the transpose or horizontal projection.

## 3. Universal first-jet identity and local consequences

Flatten the four coefficient matrices into one1274x40 matrix, acting on the40 independent first derivatives p_t,ab with a<=b. It has64 nonzero union rows and rank20. Independently construct the24 curl rows

    B_(a,b,c)=p_a,bc-p_b,ac, a<b<4, c<4.

Exact rational elimination gives

    rank(E)=rank(B)=rank([E;B])=20.                               (6)

The stored nonzero coefficients and reduced row basis are reproducible from the native operator. Equality of rowspaces is a constant linear algebra identity on arbitrary first jets, not a finite sampling of k. Hence on a flat constant-coefficient horizontal patch

    E(D)j(u)=0 iff partial_a u_bc-partial_b u_ac=0.                 (7)

On a contractible smooth patch, apply the Poincare lemma to each column: u_ac=partial_a w_c. Symmetry gives partial_a w_c=partial_c w_a, so a second application gives u=Hess(phi). Such a tensor is a linearized diffeomorphism (vector=grad(phi)/2), and G'u=0. Equivalently, for any nonzero real k, curl(k)u=0 implies u=c k tensor k: choose any nonzero component of k, solve each column as a multiple of k, then use symmetry. This also covers null k without division by k².

For the coupled equations with metric source J_g, distortion source J_T=0, and restricted T=j(u), the grade2 part of A h+Cj(u)=0 is(7), because A h and kappa Kj(u) are grade1. It follows that

    J_g=A* j(u)=-2G'u=0.                                         (8)

This rules out a nonzero metric source within that restricted flat unsourced-companion lift. It does NOT assert that arbitrary solutions of the full I1B have zero matter source. Extra distortion grades, an explicit J_T, curved lower-order terms, nontrivial topology, boundary/distributional effects and changed operator/domain are outside the theorem. For kappa!=0, Cj(u)=0 alone additionally forces u=0 by its separate grade1 part; the coupled equation also contains A h and must not be replaced by Cj=0.

## 4. A sourced repair has an explicit compatibility condition

The same curl computation prices the simplest sourceful escape. Define

    v_b=sum_a eta_a B_(a,b,a),
    Ric'_bc=1/2[-sum_a eta_a partial_a B_(a,b,c)+partial_c v_b].    (9)

Taking the metric trace and subtracting half that trace reconstructs G'u. Thus the grade2 component of an allowed distortion source J_T fixes B through the constant rowspace equivalence(6), and its derivative fixes the necessary metric source J_g=-2G'u. The two sources cannot be supplied independently within this restricted ansatz. This is a local compatibility requirement, not existence for arbitrary source pairs or a physical source-selection rule.

For a concrete nonzero-source countercontrol, set h=0, u11=(x0)²/2 and all other u components zero. Then B_(0,1,1)=x0, Ric'00=1/2,Ric'11=-1/2,R'=1 and G'22=G'33=1/2. Set J_g22=J_g33=-1 and choose J_T=Cj(u), including its grade2 part and its kappa K grade1 part. This constructed pair satisfies both linear coupled equations and has nonzero metric source. It exits the theorem by sourcing the companion; it is not a native matter or observation construction. Equation(9) is verified symbolically on general symmetric u first-jet data, and the example separately checks the signs.

## 5. Repair requirement and verification

The next usable native packet must solve the enlarged coupled distortion grades or provide a source-owned nonzero distortion Euler source, retaining all offslice rows. Projecting away the companion is not an admissible inverse. A metric/source/readout packet and a closed Green domain remain necessary for motion/light predictions; pointwise solvability or a projected Einstein tensor is insufficient.

Exact coefficient construction checks(2)-(6), including all mixed quadratic k terms in A, full receiver coverage and meaningful normalization/transpose/projection faults. The curl equivalence is extended to smooth local fields by the explicit analytic argument, not inferred from ranks at a few k values. API/bank dependencies are hash verified without historical runpy replay. Independent internal review is distinct from Lean, external-expert certification, novelty or physical GU acceptance.
