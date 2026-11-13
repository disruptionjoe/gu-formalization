---
title: "Source exterior derivative and coherent connection comparison"
status: exploration
doc_type: structural-result
created: '2026-11-13'
program_target: X-P2-P3
tier: T2
expected_delta: Test complete source-category membership without discarding independent fields or changing observation silently
actual_delta: "Constrained - exact exterior and adjoint correction, extension constraint and determinant-density survivor"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
bears_on: [SC-OP-04, SC-OP-05]
canon_verdict_change: none
---

# Source exterior derivative and coherent connection comparison

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P2-P3
tier: T2
expected_delta: Exact source-exterior lower-term membership and admissible survivor comparison
actual_delta: Constrained - exact exterior and adjoint correction, extension constraint and determinant-density survivor

```gu-typed-objects
result: Source exterior derivative and coherent connection comparison
carrier: source-guided H4 plus symmetric-metric N10, full one-form spinor and scalar; explicit coherent normal jets LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: metric volume and compatible spin pairing versus explicitly weighted adjoint; no silent source identification ON=declared_carrier
real_structure: complex Clifford identities; K77 real and K95 quaternionic structures separately typed; no signature transfer inferred
grading: ambient chirality and auxiliary operator grade remain distinct from effective physical sectors
action_owner: repository-construction -- structural comparison of source-print ingredients; no selected full action
target: exterior operator versus coherent vector form spin transport MAP-TYPE=intertwiner
```

## 1. Existing objects and what is new

Reuse without rediscovery:

- `native-rs-moving-section-index-2026-11-11.md`: coherent split-preserving metric connection on s*TY; it changes both vector/form and spin legs. Extension away from the section is additional data.
- `source-symbol-quotient-membership-2026-11-12.md`: the natural two-channel NW symbol, complete q=(P_H,Gamma_Y,nu), stable zero-SE relation c0=−a/12, nonzero a,e,g, and invertible tangential time coefficient.
- `source-chimeric-trace-compatibility-2026-11-13.md`: source-adapted section, II, mean H=t/2, t²=−4, full minimal coherent operator failure under LC and successful coherent full split correction. Trace-only correction is insufficient.
- Source extraction `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`, and primary §§8,9.3: actual printed arrows are Phi d_A on one-form spinors, d_A on scalar spinors, and starred codifferential-like SW arrows. Phi is an algebraic contraction, not a replacement definition of exterior derivative. The source's general Shiab family does not choose the natural two-channel weights used here, nor establish its global adjoint.

The new calculation keeps d_A as the exterior connection derivative and computes its exact difference from covariantizing every slot by a non-LC connection. It then follows this difference through the full observed quotient.

## 2. Exact exterior and adjoint identities

Let V=TY with fixed pseudo-Riemannian metric G, metric volume density, and a compatible nondegenerate spin pairing. Work locally with compactly supported fields to avoid boundary terms. Let

    nabla'=nabla^LC+B,    B_U in so(V,G),

and A be its induced compatible spin connection. Let D' be the induced tensor connection on Lambda*T*Y tensor S. Ordinary tangent torsion and its vector trace are

    T_B(U,V)=B_U V−B_V U,
    w_B=sum_i eta_i B_(e_i)e_i.

These are NOT source augmented torsion T_omega=A_omega−B_omega. That source displacement need not be the lift of any tangent metric connection.

For a spinor-valued one-form zeta,

    (d_A zeta)(U,V)
      =(D'_U zeta)(V)−(D'_V zeta)(U)+zeta(T_B(U,V)).      (E1)

Proof: expand covariant derivatives and use nabla'_U V−nabla'_V U−[U,V]=T_B(U,V). The last term has a PLUS sign. On scalar spinors,

    d_A nu(U)=nabla^A_U nu,                              (E2)

with no form-leg correction. For the formal codifferential from one-forms to scalars,

    delta_A zeta=−sum_i eta_i(D'_(e_i)zeta)(e_i)
                 −zeta(w_B).                          (E3)

Proof: the usual integration-by-parts formula uses the LC connection on the covector slot and A on S. Since D'_U zeta=(nabla^LC tensor A)_U zeta−zeta composed B_U, the stated formula follows. No derivative of B occurs. Equivalently, if tau(U)=sum_i eta_i G(T_B(e_i,U),e_i), then tau=−w_B^flat and the correction is +i_(tau^sharp). This is the degree1-to0 formula; silently using the same formula at every exterior degree would omit further adjoint torsion-insertion terms.

If density is changed to exp(f) times metric volume, the exact replacement is

    delta_(A,f)=delta_A−i_(grad f).                     (E4)

If the spin connection does not preserve the stated pairing, or the barred connection is independently held instead of paired, its dual-connection discrepancy must be added. Therefore E3 is a declared metric-spin/fixed-pairing test, not an identification of every printed source bar/star by assumption.

## 3. Complete source-shaped operator difference

Define C(F)_a=sum_i eta_i c(e_i)F(e_i,e_a). The natural two-channel algebraic contraction is

    Phi(F)=a C(F)+(c0/2)J Gamma_Y C(F).                 (E5)

For F=xi wedge zeta, Gamma C(F)=2(i_xi zeta−c(xi)Gamma zeta), so E5 reproduces exactly the already-owned NW symbol. No new action coefficient is selected.

Take the exterior completion

    D_ext(zeta,nu)=(Phi d_A zeta+e d_A nu, −g delta_A zeta),

and D_coh the same symbol covariantized through D' on every form/spin slot, including the scalar divergence. Their exact difference is

    D_ext−D_coh=V_B,
    V_B(zeta,nu)=(Phi[zeta composed T_B], g zeta(w_B)).  (E6)

The NE scalar arrow has no correction. The NW correction is torsion insertion followed by the actual declared Phi. The SW correction is the vector trace of contorsion evaluated by zeta. This is zero order in fermions, not necessarily in section/metric background fields.

With weighted adjoint, replace w_B by w_B+grad f. No assertion that the source chose this weighted adjoint is made.

## 4. Apply the same source-adapted geometry

Along the observation section, use the established full split correction

    B_X Y=−II(X,Y),    B_X n=S_nX,
    G(S_nX,Y)=G(II(X,Y),n),

for X,Y tangent and n normal. Its coherent connection preserves H and N along H. The source-reconstructed II is symmetric and Hmean=tr_H II=t/2 with t²=−4. Here Hmean is a vector, while H denotes the horizontal bundle.

Choose first the definite normal extension B_n=0 at the section. Then

    T_B(X,Y)=0,
    T_B(X,n)=S_nX in H,
    T_B(n,m)=0,
    w_B=−Hmean.                                      (E7)

For every hidden normal z in K=ker Gamma_N, z composed T_B=0. Hence

    q V_B z=(0,0,−g z(Hmean)).                       (E8)

**The NW exterior correction does not reintroduce II on these hidden fields. The SW formal-adjoint correction does.** An undifferentiated claim that 'torsion restores all canceled II' is false.

Use z=K_t psi=t^flat tensor psi−(1/10)J_N c(t)psi. Then Gamma_Nz=0, z(t)=−18psi/5, and E8 has scalar component 9g psi/5. Thus it has rank128 on the full complex Dirac module. The induced time coefficient is invertible, so normalization cannot remove the defect.

This is not a bare-connection argument: E6 is the complete operator difference, and D_coh already preserves the hidden sector. With a declared normal-jet convention the normalized defect is −d_time^−1 qV_B|K.

## 5. Arbitrary metric normal extensions do not solve both visible blocks

This is a stronger conditional result than E7. Keep B_X fixed as the full split correction, but allow every B_n in so(V) at the point. The exterior completion and pairing/density remain as in E6. Hold the natural stable zero-SE family c0=−a/12, a,e,g nonzero; then L=2a+14c0=5a/6 is nonzero.

Suppose the NW total-Gamma row vanishes on every hidden z. Since

    Gamma Phi(F)=(L/2)Gamma C(F),

we obtain Gamma C(z composed T_B)=0 for all z in ker Gamma_N. Write this map as sum_k M_k z_k, where k ranges over normal slots. Every M_k is a PURE Clifford bivector: torsion is antisymmetric in its two form inputs, so scalar parts cancel. Since Gamma_N is surjective, annihilating its kernel is equivalent to

    M_k=M c(n^k)                                    (E9)

for one endomorphism M of the full spin module (with the usual signed dual basis).

The full complex Cl14 representation identifies End(S) with the Clifford algebra. For any nonnull normal basis vector, E9 implies M has only grades1 and3. Write M=v+omega_3. Requiring M c(n) to be pure grade2 for every n in N gives:

- scalar part G(v,n)=0, so v is horizontal;
- degree4 part omega_3 wedge n=0 for every n in N, so omega_3=0 because dim N=10>3.

The second statement follows coefficient by coefficient: any nonzero3-blade omits at least one of ten independent normal basis directions, and wedging by that direction cannot cancel its unique coefficient. Consequently

    M=c(v_H),    M_k=c(v_H)c(n^k).

In particular M_k has NO pure-normal bivector component. Faithfulness then forces

    P_N T_B(n,m)=0 for every n,m in N.               (E10)

Let C(n,m,l)=G(B_n m,l) for normal arguments. Metricity makes C skew in its last two entries; E10 makes it symmetric in the first two. These two symmetries imply C=0 by cycling indices. Hence P_N B_n m=0, so

    P_N w_B=−Hmean                                 (E11)

independently of the remaining mixed or horizontal normal-extension blocks.

Since hidden z annihilates horizontal vectors, the SW row is again −g z(Hmean), rank128 on K_t psi. Therefore:

> For every metric normal extension of the coherent full split correction, either the NW total-Gamma row already detects a hidden field, or the SW row has the fixed rank128 mean-curvature witness. There is no complete q closure in this declared exterior-completion category with the fixed metric-volume formal adjoint.

This is an exact condition on a structural subfamily; it is NOT an all-source-parent, all-connection, all-density, or all-lower-completion exclusion. The unnormalized q defect is converted to a normalized lower defect using the already-proved quotient and invertible tangential time coefficient. The normal directions are treated under the explicit jet convention below, not silently thrown away from a14D PDE.

## 6. Explicit tradeoff control and a surviving density comparison

A normal vectorial extension illustrates E10–E11. Set

    B_n m=alpha[G(n,m)Hmean−G(Hmean,m)n],

and let B_n vanish on H. For r=dimN=10,

    P_N w_B=[−1+(r−1)alpha]Hmean,
    z(T_B)|_(N,N)=alpha(Hmean^flat wedge z).

On hidden z, Gamma C(zT)=2alpha z(Hmean), so

    P_H Phi(zT)=c0 alpha J_H z(Hmean),
    Gamma Phi(zT)=L alpha z(Hmean),
    SW=g[−1+9alpha] z(Hmean).                       (E12)

Alpha=0 recovers the pure SW witness. Alpha=1/9 cancels SW but makes the NW trace row nonzero. This is a comparison over connection structure, not a guessed action or fitted Lagrangian.

A genuinely surviving **operator change** is visible in E4. For the B_n=0 extension, choosing a density jet with

    P_N grad f=Hmean

cancels the SW term, while the NW hidden torsion term is already zero. Thus this weighted-adjoint comparison restores local q closure for the minimal tangential restriction. Locally a smooth positive density with any prescribed smooth normal first jet along a section exists by tubular coordinates. No integrability condition requires Hmean to be a tangential gradient because the prescribed data are normal first derivatives.

**Multiplying an already-written bilinear density by rho does not accomplish this.** If its Euler expression is merely rho D_ext, the invertible equation-row rescaling leaves the normalized evolution and hidden defect unchanged. The survivor requires replacing the SW block by the weighted formal adjoint delta_(A,f), or equivalently adding the definite zero-order operator correction +g i_(grad f) in that block. Reconstructing the adjoint relative to a new pairing is an operator change, not an algebraic display of the old one. Whether the variational owner actually demands that reconstructed block must be checked separately.

This density has a source-geometric expression, not an arbitrary local fit. On the same-signature metric bundle set

    f(x,y)=−(1/2) log |det(g_x^−1 y)|,
    rho=exp(f)=vol_g/vol_y.                            (E13)

The quotient of positive densities is a scalar at x. Thus E13 is invariant under coordinate changes on X, smooth throughout the fixed-signature metric bundle, and uses no extra metric beyond the already-selected observing g. It has f(x,g_x)=0 and rho(x,g_x)=1. For a vertical v,

    df(v)=−(1/2)tr(y^−1 v),
    K_y(t,v)=−tr(y^−1 v),    t=y.

Consequently the vertical gradient is t/2. Its LC(g)-horizontal derivative is zero because both g and y are parallel along the horizontal lift. Since the reconstructed ambient metric is block orthogonal, the FULL gradient is t/2, and in particular equals Hmean along s_g.

The ambient metric density factors into the tautological horizontal vol_y and vertical DeWitt density. Multiplying it by rho replaces vol_y by the observer's vol_g. Therefore the survivor corresponds to the natural product of fixed observing-base density with the vertical metric density. This is a concrete geometric alternative; the source has not selected it as the fermionic pairing or replaced its printed Hodge/star accordingly.

At fixed g and y, grad f is independent of the source connection displacement. Thus the added SW term has zero primitive varpi derivative; an overall rho still rescales the current density and equals1 on the observing section. Metric/section variation and the complete source current require separate testing. This observation does not repair previously failed paired odd trace-current transformations by itself.

This is not a free source repair: the adjoint operator and variational pairing prescription change. It supplies a precise surviving condition for the next SAME-object current/density test. Alternatively one may add the explicit lower counterterm −V_B, or use independently transported barred/readout data; those are changes requiring ownership, not consequences of a spin-only varpi displacement.

## 7. Normal jets and source ceiling

The preceding normalized lower-operator statements concern a tangential restriction with zero coherent normal covariant jet, nabla'_n(zeta,nu)=0 at the point. The full14D source principal symbol still acts on free normal derivatives; arbitrary ambient solutions are not shown to descend. Changing B_n while keeping a different normal-jet convention fixed changes an additional term sum_n D_n times the change of normal connection. It cannot be concealed as the same restriction.

E1–E6 are full ambient identities and remain valid before choosing any jet restriction. The pointwise hidden-field witness can be realized by choosing its first jet to be D'-parallel at the point; along tangent directions q then also has zero covariant jet because the full split correction preserves q. This is why V_B is the actual remaining zero-order obstruction for the stated restriction.

Source boundaries retained:

- A source spin-only varpi in the larger parent need not be induced by any metric tangent B; the theorem does not exhaust it.
- A0 is not redefined; A=A0+varpi remains independent source data, and augmented source torsion is not ordinary tangent torsion.
- Independent bars do not automatically select the compatible formal adjoint used here.
- The source Phi/epsilon contractions and lower-order rivals remain unselected beyond the declared natural family.
- Exact autonomous6S is a structural comparator, not the source's effective2+1, nonchirality or physical-family assertion.
- No ambient global domain, source stationary solution, real-form bridge, class-C inhabitant, physical prediction or universal source exclusion follows.


## Evidence and acceptance

- [Primary 2021 draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf), §3.5 eq3.27 and §§5–9. SHA256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`; page23 adjoint definition visually verified.
- `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` and full relevant records in `lab/sources/source-claim-register.yaml`.
- Prior natural-family proof: `explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md`; prior source geometry/current: `explorations/conditional-build/source-chimeric-trace-compatibility-2026-11-13.md` and `explorations/conditional-build/source-prescription-current-2026-11-13.md`.
- Companion: `explorations/conditional-build/source-lower-term-compatibility-2026-11-13.md`.
- Exact replay: `tests/program-focus/source_exterior_connection_probe.py`; proof/dependency hashes and scope: `lab/process/source-exterior-connection.json`.

Independent specialist cross-review and four exact supporting/contrary suites
support conditional T2 acceptance. Universal proofs carry the dimension-general
claims; reduced matrices and native blade-support controls are not source
selection or full-physics certification. No Lean or class-C decision is claimed.
The full14D unrestricted-normal-jet problem and effective physical2+1 remain
separate; Matrix18/18 remains constrained and the triple intersection open.
