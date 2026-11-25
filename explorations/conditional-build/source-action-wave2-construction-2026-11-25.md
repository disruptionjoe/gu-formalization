---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Improve the directed source-informed action through actual native operator, Euler and
  formal connection construction.
actual_delta: Source-admitted SE completion has exact Dirac principal blocks and explicit non-Clifford
  lower terms; actual K95 bosonic coefficients and Helmholtz defect checked; unique all-component formal
  connection series and induced effective action constructed.
class_covered: One local K95 source-informed reconstruction; fixed six fermion arrows with source-admitted
  SE variation; formal inverse-kappa connection branch at fixed geometry and matter. No whole-C coverage.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-OP-05
- explorations/conditional-build/source-action-external-datum-candidate-2026-11-25.md
- explorations/conditional-build/exterior-symbol-orbits-conormal-2026-11-25.md
source_bridge:
  status: conditional
  reason: The source admits SE rivals and prints kappa, but does not select semisimplicity, this coefficient/product
    completion, a large-kappa regime or a physical integer receiver.
kill_condition: Internal defects diagnose this fixed candidate and its added assumptions; no source, GU
  or class-C exclusion or verdict follows.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
title: 'Source-action wave2: Dirac completion and formal connection construction'
---

# Source-action wave2: Dirac completion and formal connection construction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Improve the directed source-informed action through actual native operator, Euler and
  formal connection construction.
actual_delta: Source-admitted SE completion has exact Dirac principal blocks and explicit non-Clifford
  lower terms; actual K95 bosonic coefficients and Helmholtz defect checked; unique all-component formal
  connection series and induced effective action constructed.
```


## Result and scope

The [first construction](source-action-external-datum-candidate-2026-11-25.md) supplied an explicit local action but missed applying an already-owned symbol discriminator. Its non-null inverse remains correct; its horizontal evolution has a Jordan defect. The source-admitted southeast completion below removes that defect. The bosonic part is now evaluated on its actual K95 Clifford/form coefficients, and every connection equation has a unique formal inverse-kappa solution including the matter current. These are constructive gains, not a stationary physical GU solution.

This is Joe's specifically directed second construction attempt, not a permanent governance change, GU-min freeze or source selection. **Weakest physical link:** no native physical observation/index receiver connects the supplied boundary integer to families. **Source necessity:** conditional only. **Class-C membership:** unproved; full coupled stationary solution, domain, physical gauge/positivity and derivative-order clauses remain. The original source `2+1`, non-chiral-total, independent-bar and non-LC distinctions are retained.

```gu-typed-objects
result: source-informed action wave2
carrier: full Dirac one-form plus scalar-spinor with independent dual rows LAYER=ambient+observed BRIDGE=transported_literal_section_contraction CHIRALITY=S-FULL-DIRAC
pairing: real Krein/form action pairing, independent dual rows; auxiliary horizontal norm is separate ON=full_Dirac_field_module
real_structure: K95 complex Clifford and U64,64; K77 and quaternionic restrictions not transferred
grading: auxiliary diag(Omega,-Omega); not physical family grading
action_owner: repository-construction using source-print ingredients
target: repaired local functional and formal all-component connection equation MAP-TYPE=contraction
```

## 1. One revised action, with declared choices

Keep exactly the original geometry, trace reversal lambda1/2, K95 rank128 module, two-frame dressing, Shiab coefficient products, independent dual rows and literal section map. Write B=A0[g], T=Ahat-B, Phi=*^-1 S0, and use the original nondegenerate real integrated pairing. The chosen fermion operator becomes

    D_rep = [ C d_Ahat        d_Ahat    ]
            [ -delta_Ahat   -(1/2)L0  ],
    L0=gamma^a nabla_a on scalar-spinors.

The revised action is

    S_rep^kappa = <T,Phi F_B>
       +1/2<T,Phi D_B T> +1/3<T,Phi(T wedge T)>
       +kappa/2<T,T> + Re integral bar_chi D_rep chi dmu.

Primary numerical normalization remains kappa=1. Section4 also restores the source-printed kappa as a formal parameter; no value is fitted. Relative normalization remains the previous independent-row convention. This is one SE-completed action with its source coupling, not a coefficient scan. No Yang-Mills square, residual-square replacement, conventional Higgs potential or independent current term is added.

**Why -1/2?** In the existing exterior14 classification the fixed other arrows are (a,c,e,f,g,h)=(1,0,1,0,1,0). Time regularity is aTZ=1 and semisimplicity is P=2s+1=0. Thus s=-1/2 is uniquely required in this fixed six-coordinate slice by that additional principal-evolution demand. SC-OP-05 leaves a nonzero SE rival open; it does not authenticate this coefficient. The source's printed SE0 candidate remains historical evidence. This revision improves our chosen completion under a stated requirement, not a source verdict.

## 2. Exact fermion factorization, action and observation together

Put c_xi=gamma^a xi_a, Gamma zeta=gamma^a zeta_a, (J eta)_a=gamma_a eta and i_xi zeta=G^{ab}xi_a zeta_b. The repaired symbol is

    sigma_rep(xi)(zeta,nu)
      =(c_xi zeta-xi Gamma zeta+xi nu, i_xi zeta-(1/2)c_xi nu).

Define invertible field and equation maps F,R:

    eta=nu-Gamma zeta,       zeta'=zeta+(1/2)J eta;
    v=s_out-(1/2)Gamma r,    u=r+(1/2)J v.

Their inverses, valid for n14 (indeed any n), are

    zeta=zeta'-(1/2)J eta,    nu=Gamma zeta'+(1-n/2)eta;
    r=u-(1/2)J v,            s_out=(1/2)Gamma u+(1-n/4)v.

The identities c_xi J+J c_xi=2xi and c_xi Gamma+Gamma c_xi=2i_xi give

    R sigma_rep(xi) F^-1 = diag(c_xi on one-forms, -c_xi on scalars).

No division by xi² is used, so this includes null covectors. R and F differ: this is left/right operator equivalence, not an isospectral similarity. It does not identify 15 spinor components with physical families.

The independent barred row transforms as bar_chi'=bar_chi R^-1. Therefore the action is exactly rewritten as bar_chi' (R D_rep F^-1) chi'. Literal observation must transform to q'=q F^-1:

    q'(zeta',eta)=(s_g^*zeta'-(1/2)s_g^*(J eta),
                   [Gamma zeta'+(1-n/2)eta]|_section).

The normal components in Gamma zeta' remain. Applying the old numerical decoder to the primed fields would change the theory. The original2+1 labels are carried through F^-1, not replaced by independent Dirac-family labels.

### Full differential remainder

Let nabla combine LC on form indices with Ahat on spinors, L1=gamma^a nabla_a on spinor-valued one-forms. Define the zero-order maps

    Q(zeta)_a=(nabla_a gamma^b)zeta_b=[T_a,gamma^b]zeta_b,
    K_gamma(eta)_a=gamma^b(nabla_b gamma_a)eta.

A0 is Clifford compatible; arbitrary full-U displacement need not be. Direct differentiation gives

    r=L1 zeta+nabla eta+Q zeta,
    Gamma L1 zeta+L0 Gamma zeta=2 div zeta+Gamma Q zeta,
    v=-L0 eta-Gamma Q zeta,
    u=L1 zeta'+(I-J Gamma/2)Q zeta-K_gamma eta/2,
    zeta=zeta'-J eta/2.

Thus the actual differential operator is block Dirac plus an explicit zero-order endomorphism. For Q=0, K_gamma=0 and the factorization is exact at differential order too. Neither vanishing is imposed on the generic U64,64 field. Derivatives of moving Clifford tensors are included.

### Current and variation

The new action term is -1/2 Re integral bar_nu L0 nu dmu. Its connection-current increment is

    delta J[a]=-(1/2) Re integral bar_nu gamma^a a_a nu dmu.

Together with the previous three vertices, this gives four actual current vertices. Define their unique algebraic metric-dual representative J_F using the nondegenerate field pairing. The current is algebraic in held matter fields and independent of T. Independent-bar equations are D_rep chi=0 and its density-correct formal dual. The previous fixed-A metric chain is retained, with the new explicit gamma/density term; identical current terms still cancel in E_B^tot-E_T^tot. Changing to primed variables requires differentiating F/R as well; no metric equation is inferred from principal equivalence.

### What improves and what does not

The old s0 symbol has horizontal square-zero Jordan defect rank128 (64 per auxiliary sector); this follows from the existing complete classifier. Its null kernel dimension is896, while the repaired symbol's is960=15*64. For the old count use a null frame: one light-cone one-form component is free128, twelve screen components lie in ker c_xi (64 each), the other light-cone component vanishes and nu is fixed by the screen gamma trace. Both non-null determinants are proportional to (xi²)^960: determinants alone miss the defect.

In the declared horizontal(3,1) Hermitian gamma frame, transformed evolution matrices are Hermitian Clifford involutions, so H_aux=F^dagger F is a positive principal symmetrizer. This is an auxiliary horizontal norm, not the Krein action pairing. Normal timelike directions can still give imaginary temporal roots; no estimate uniform in arbitrary normal frequencies or full K95 Cauchy theory follows. Known literal-observation nonclosure and solution-trace limitations remain.

## 3. Actual bosonic calculation and the equation-owner gap

The new sparse exterior/Clifford evaluator implements exactly the original comm/symi/symi S0, including both factors of i. Normalize its scalar coefficient pairing by b=-Re tr/128 solely for reporting. Actual K95 receiver coefficients are: mass -1; radial cubic -312; Phi2-curvature -156. For a real diagonal metric-self-adjoint A and T=Phi1 composed A, the cubic Euler coefficient is

    -4[A²-tr(A)A+e2(A)I],    e2=((tr A)²-tr A²)/2.

These are exact rational controls of the actual convention. The full-receiver polynomial and support proof are reused from K2357/K2360: simultaneous even axis sign flips permit only internal grade1 or13 on a diagonal receiver; the cubic construction has grade at most5, excluding13. Non-diagonal or non-diagonalizable fields are not silently covered. K2345's tensor Ricci calculation on the actual flat-base metric has signature-independent raised eigenvalues1/4 on horizontal+trace and -5/4 on traceless, scalar-10. The Ricci transfer uses the same rational coordinate tensor formula in nondegenerate y: clearing denominators makes the identity polynomial, and validity on the open old-signature component extends it to every nondegenerate component. This does not identify their Clifford real structures. The K95 convention check is new; those earlier geometric/classification results are reused.

**Spin-curvature normalization correction.** The historical algebraic injection uses sum over a<b of R_ij^ab gamma_a gamma_b with coefficient1. The actual spin-LC connection selected here has

    F_B=(1/4) sum_ordered_ab R_ab gamma^a gamma^b.

Consequently constant sectional curvature k gives F_B=(k/2)Phi2, and the actual source is Phi F_B=-Einstein, not the historical -2Einstein. The bare Phi2 receiver value -156 above is correct; the actual unit-sectional spin-curvature value is -78. Independent rational sectional-basis controls detect the factor-two substitution. On the actual flat-base bundle the Clifford-vector S_curv amplitudes are -21/4 on horizontal+trace and -15/4 on traceless. This corrects a transfer error found during this wave, not the geometric Ricci formula or the general Euler identities.

At T=0 and zero matter, the curvature source does not vanish. Constant radial or constant three-projector odd fields do not solve the full connection equations: the omitted even derivative-adjoint rows force equal amplitudes, while the two Ricci-source rows require different ones. We reuse that limited diagnostic rather than enumerate another neighboring ansatz or claim a GU exclusion. Variable and mixed-parity fields remain live.

**The actual endpoint is still different.** For dx=e0, O=Phi1 and Z=e1 gamma01, the native evaluator gives

    left=<Z,Phi(dx wedge O)>=-2,
    right=<O,Phi(dx wedge Z)>=-24,
    actual derivative Euler row=(left-right)/2=11,
    printed endpoint derivative row=left=-2.

The formal Helmholtz principal condition would require left+right=0; here it is -26. These are coefficients in compact-support integration-by-parts conventions, not a boundary oversight. This supplies an actual native witness, beyond the prior generic polynomial control.

More generally I1 is the radial homotopy integral of the printed residual R_print(T)=Phi(F_B+D_BT+T²)+kappa T. Differentiating the homotopy gives

    E_I(T)=R_print(T)+integral_0^1 t[(DR_print(tT))^dagger-DR_print(tT)]T dt.

Consequently this chosen Shiab completion cannot identify its action Euler with the printed endpoint on the unrestricted field class. We retain the action-derived equation. The source glyph's product/coupling choices and full moving structures are not uniquely fixed by this candidate, so this is not a source contradiction.

## 4. Constructing every connection component formally

Fix smooth g and matter fields and compact-support variations (or a boundary convention that cancels the displayed Green terms). Set

    S_curv=Phi F_B,
    K=(Phi D_B+D_B^dagger Phi^dagger)/2,
    Q_U(v)=v wedge U+U wedge v,
    N(U,V)=[Phi(U wedge V+V wedge U)
            +Q_U^dagger Phi^dagger V+Q_V^dagger Phi^dagger U]/6,
    R_cur=S_curv+J_F.

K is formally self-adjoint. N is the symmetric quadratic Euler term of the actual cubic; its integrated trilinear polarization is fully symmetric. This is distinct from K_gamma above. The full connection equation is exactly

    kappa T+R_cur+K T+N(T,T)=0.

The action itself equals

    S_F[B]+<R_cur,T>+kappa/2<T,T>
          +1/2<T,K T>+1/3<T,N(T,T)>.

No positivity, spectral inverse or dropped equation is needed for the following formal construction. Let h=kappa^-1 and seek T(h) in h M[[h]], smooth sections with formal coefficients:

    T1=-R_cur,
    Tn=-K T_(n-1)-sum_(i+j=n-1; i,j>=1) N(Ti,Tj), n>=2.

At each order the new coefficient has identity coefficient and depends only on known earlier terms, proving existence and uniqueness as a formal differential series. In particular,

    T=-h R_cur+h² K R_cur
       -h³[K² R_cur+N(R_cur,R_cur)]
       +h⁴[K³ R_cur+K N(R_cur,R_cur)+2N(R_cur,K R_cur)]+... .

Every connection receiver is included. A truncation through h^m has normalized residual O(h^(m+1)), or unnormalized Euler residual O(h^m). These are formal orders, not numerical error bounds. In the zero-matter sector, S_curv is Clifford-odd, K flips parity, and N(U,V) has parity1+parity(U)+parity(V). Thus odd orders are odd and even orders even. The first correction K S_curv supplies precisely the mixed parity missed by pure-odd stationary ansätze. On the flat-base native bundle T1=-S_curv has amplitudes21/4 on horizontal+trace and15/4 on traceless. In an adapted K95 frame with horizontal indices(0,1,2,9), negative trace index10 and positive traceless index3, the normalized b=-tr/128 paired receiver of T2=K S_curv at Z=e0 gamma03 is -3/4. This is a covector pairing, not an unraised field component. It exhibits a nonzero even correction forced by the actual geometry, rather than a guessed extra field.

### The induced effective action

Substituting this formal critical connection into the same action gives

    S_eff=S_F[B] -h/2<R_cur,R_cur> +h²/2<R_cur,K R_cur>
       -h³[1/2<K R_cur,K R_cur>
             +1/3<R_cur,N(R_cur,R_cur)>]+O(h⁴).

Its leading geometric and matter interaction is

    -h/2<S_curv,S_curv> -h<S_curv,J_F> -h/2<J_F,J_F>.

The curvature-current and current-current terms are induced by elimination, not added by hand. Current-current is quartic in the independent classical matter fields. Grassmann quantization, physical signs and scales remain separate. The formal envelope identity eliminates the connection-chain term coefficientwise; the remaining effective metric and matter equations still need to be solved. Earlier K128/K140/K145 linear Schur/Neumann work already warns against treating formal elimination as a bounded inverse. This specific nonlinear current-inclusive recurrence is the present extension, not a global novelty claim.

**No convergence claim:** derivatives grow with order; no bound makes the series converge at kappa1. No full stationary g/chi, prescribed Bott boundary value or physical solution has been constructed. An arbitrary nonzero boundary charge is not automatically compatible with a formal branch around T=0.

## 5. External datum: preserve it, test its limitation

Retain the existing actual smooth connection with imported charges(+3,-3), the chosen J splitting and boundary framing. The scalar3 remains supplied input and the same construction works for every integer. Its smooth extension is established; stationary extension and a physical observed-index receiver are separate open problems.

A new local scaling check explains why this datum cannot supply an easy variational existence argument. On a fixed smooth metric chart take A_epsilon=f(r/epsilon)alpha, alpha=U_k^-1dU_k. These fields have the same outer boundary and charge; they agree outside radius2epsilon with the punctured pure gauge A_star=alpha. In the core A=O(epsilon^-1), dA=O(epsilon^-2). The first-order/cubic action contribution changes by O(epsilon^11) in dimension14, and its mass term by O(epsilon^12), while the Chern7 integral is unchanged. Curvature L7 is the scale-critical comparator (14-2*7=0).

This is an absolute local coefficient estimate using an auxiliary coordinate norm, not a lower bound for the indefinite action. A_star has finite punctured action but is not a smooth admissible extension. Concentration obstructs inferring compactness/minimizer existence from finite action and charge alone; it does not prove that stationary solutions do not exist. No Euclidean minimization or stationary solution is imported.

## 6. Evidence map and remaining construction burden

| Claim | Evidence | Ceiling |
|---|---|---|
| Old Jordan defect / unique s repair in fixed slice | Existing complete classifier + native horizontal evolution controls | Conditional principal requirement; not source-selected |
| New principal and differential formulas | Clifford derivation + native128 positive/negative/null/mixed and noncommuting first-jet controls | Left/right local equivalence, not spectrum or domain equivalence |
| Actual bosonic coefficients / endpoint mismatch | Independent rational Clifford/form evaluator + inherited all-receiver proof | Chosen K95 product convention, not all source completions |
| Formal nonlinear connection completion | Recursive proof + positive/indefinite noncommuting polynomial countercontrols | All formal connection components, no convergence/full coupled solution |
| Charge concentration | Written scaling derivation | No stationary no-go or count prediction |

All results are internally reviewed T2 candidate mathematics, with no Lean or external peer-review claim. The [assessment](source-action-wave2-specialist-assessment-2026-11-25.md) records20 simulated specialist lenses and the efficiency lessons. Exact reproducibility: `tests/program-focus/source_action_wave2_probe.py`. Review: `lab/process/hostile-reviews/2026-11-25-source-action-wave2-review.md`.

The substantive next construction problem is a controlled analytic realization of the completed action: a stationary coupled background/domain or a justified convergent sector, with the actual observation and prescribed external data. The source endpoint/action ownership gap is explicitly retained. Repeating winding arithmetic, scanning already-classified SE coefficients or treating formal truncations as solutions would add no such bridge. Standing research selection remains unchanged.
