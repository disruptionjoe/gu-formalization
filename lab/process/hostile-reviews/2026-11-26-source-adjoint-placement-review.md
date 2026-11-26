# Independent review: primary adjoint reconciliation and placement

Basis f754e924e6bdf9c9506a09e1bec2c8248dd6e941. Internal specialist reviews, not external-expert certification. Adjoint reviewer is independent of correction derivation; placement reviewer independently checks placement but previously identified primary custody and does not certify that contribution independently. Root reconciled all findings.

## Integrated findings

- Preserve plus theorem; primary source label withdrawn.
- Minus fixed class4R and blockC36/image24/kernel12; C anti-isometry prevents Sp label transfer.
- Horizontal12R survives with changed coefficients/witness.
- Ordered insertion and literal O descent f=g=0 pass; trace block determinant is -mu²neg.
- No source exclusion, physical mass or source-selected completion.


## Pairing and class review

# Independent adjoint-convention review — 2026-11-26

**Disposition:** The proposed minus-adjoint correction is mathematically required. The old plus/reversion calculation is a valid comparator, but its designation as the source convention is wrong. Its optional-C zero does not survive the corrected convention. This review does not establish a source K77-to-K95 geometric bridge, mandatory C-preservation, physical fluctuations, or a GU verdict.

**Evidence pin:** inspected clean mounted GU `origin/main` = `f754e924e6bdf9c9506a09e1bec2c8248dd6e941`. A fresh local `git fetch origin` was attempted and failed because github.com DNS was unavailable; therefore this is an explicitly revision-pinned review, not independent confirmation that upstream has not advanced. Reviewed the Nov26 normal note/JSON/probe, Nov24 horizontal note/probe, Nov13 lower-term note, native Clifford fixture, and contributor/source-routing prerequisites. No owner edits or heavy jobs.

**Review target:** LB-CLASS adjoint/source-authentication correction; T1 because it withdraws an internal zero-class exclusion. Expected delta: replace incorrectly attributed zero with the correct four-real-parameter C-commuting family while retaining the old comparator. Kill condition: an explicit algebraic inconsistency in the proposed minus construction. All fixed K95 geometric actions and C are held unchanged; only the Hermitian pairing changes. Full source relevance remains conditional.

## 1. Source custody

The [primary April 2021 draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf), printed p23, §3.5 eq3.27, explicitly includes real grades1 and2 in the unitary Lie algebra and defines the adjoint by composing the canonical automorphism with reversal. Hence a real degree-k blade has adjoint sign

    s_minus(k) = (-1)^[k(k+1)/2].

Its accompanying caution about the historical decomposition does not turn reversal alone into the stated adjoint. The Nov13 `source-lower-term-compatibility` note already records this correct interpretation. Source uses K77; the following is an explicit K95 realization of the same algebraic adjoint law, not authentication of a signature migration.

## 2. Pairing change in the SAME Clifford representation

Let H+ be the native product gamma0...gamma8, with gamma(v)^sharp+ = gamma(v). Let h=omega_H, n=omega_N, Omega=h n, with h²=n²=-1, Omega²=1. Then Omega^sharp+ = -Omega and Omega anticommutes with every real Clifford vector. Set

    H- = i H+ Omega.

It is Hermitian since (H+Omega)†=-H+Omega, nondegenerate, and

    T^sharp- = Omega T^sharp+ Omega.

Thus all even Clifford grades have their old sharp sign; all odd grades reverse sign. The native exact fixture also gives H-²=1 and trace(H-)=0, so H- has signature(64,64). This constructs the required U(64,64) pairing without replacing gamma, the split, or C. It is not a mere phase change of T inside the old pairing.

## 3. Complete normal-tensor class

The all-End representation-theoretic decomposition remains unchanged:

    span_C{1,h} tensor direct_sum_(k odd) Hom_G(N_C,Lambda^k N_C).

For k=1,3,5,7,9, normal multiplicities are m=(4,8,10,8,4). For degrees0,2,4,6,8,10, invariant multiplicities are I=(1,2,3,3,2,1). The real coefficient spaces have these same dimensions because the underlying actions and real Clifford algebra are real; C fixes all their real blades.

For sharp-minus skewness, coefficients are REAL in degrees1,5,9 and IMAGINARY in degrees3,7. Optional commutation with C retains exactly the real coefficients. The sharp-plus comparator reverses those choices.

| Pairing/category | tensor coefficients | contraction image | contraction kernel |
| --- | ---: | ---: | ---: |
| Complexified block class | 68 complex | 24 complex | 44 complex |
| Minus sharp-skew block class | 68 real | 44 real | 24 real |
| Minus sharp-skew plus C commutation | 36 real | 24 real | 12 real |
| Plus sharp-skew block comparator | 68 real | 44 real | 24 real |
| Plus sharp-skew plus C comparator | 32 real | 20 real | 12 real |

Derivation: for degree-k alpha, Gamma_N maps into invariant degrees k-1,k+1. The maps alpha(v)=v-flat wedge psi and alpha(v)=iota_v theta independently hit these two outputs with nonzero factors 11-k and k+1. Degreewise kernel multiplicities are therefore (1,3,4,3,1). In the sharp-real spaces adjacent input degrees have opposite scalar phases, preventing real cancellation in a shared output degree. Thus real full-image dimension is 2 sum_j(I_j+I_(j+1))=44 and kernel24. Minus+C retains k1,5,9, whose supports partition all six even degrees: image2 sum I=24, kernel2(1+4+1)=12. Plus+C retains k3,7: image20, kernel12.

## 4. Fixed endogenous plus SAME weak action

The existing Lie-generation theorem is a representation statement, unchanged by the pairing. It reduces the class to

    alpha(n)=c_N(n) A,
    A=a+b h+c n+d Omega.

Each real tensor c_N(n), c_N(n)h, c_N(n)n, c_N(n)Omega is plus-selfadjoint, ambient-odd, and C-even. Consequently every one is minus-skew. The corrected sharp-minus class is a,b,c,d REAL, and **all four directions commute with C**. Under sharp-plus the class is i times that real span, and its C-commuting intersection is zero. These are two different pairing statements.

Gamma_N(alpha)=10A, so corrected tensor/image/kernel dimensions are(4,4,0), also after C commutation. The old plus comparator has(4,4,0) without C and(0,0,0) with C.

On joint h,n eigenblocks with eigenvalues is,it, s,t=±1, each block has dimension32 and

    lambda_(s,t)=a-d st+i(bs+ct).

Opposite labels have conjugate eigenvalues. Rank is0,64,128; rank64 occurs exactly when one of (a+d,b-c) or (a-d,b+c) is zero and the other is not. Each pair occupies an entire ambient half. These support facts do not identify a physical chirality or family.

The source-named real grade1 scalar is now alpha(n)=a c_N(n), Gamma=10aI, C-commuting and rank128 when a!=0. Likewise the full-ambient class c(v)(a+bOmega) has two REAL sharp-minus/C-commuting directions. The source's specifically grade1 piece is only the a direction.

The old moving-reduction degree3 control is plus-skew/minus-self and must not remain the minus counterexample. A replacement needing no coefficient fit is alpha_J(n)=c_N(P_color(J)n): real grade1, minus-skew, C-commuting, fixed-SM equivariant, Gamma_N=6I. The family transforms when J transforms; a fixed value is not invariant under full normal mixing. This preserves the category distinction without claiming physical admission.

## 5. Horizontal Nov24 theorem

Its all-End Schur argument remains valid: alpha(X)=c_H(X)A with

    A=sum_(h,j) a_hj P_h E_j,

24 complex coefficients before sharp/reality. Because P_h,E_j are ambient-even, their sharp laws are unchanged: P_L^sharp-=P_R and E_j^sharp-=E_j. Clifford multiplication swaps P_L/P_R. Thus

    (c_H(X)A)^sharp-=-c_H(X) sum_(h,j) conjugate(a_hj)P_hE_j.

Sharp-minus skewness gives a_hj=conjugate(a_hj), hence REAL coefficients. C commutation still gives a_R,barj=conjugate(a_Lj). Therefore

    A=sum_j t_j(P_L E_j+P_R E_barj), t_j real.

This is again exactly12 real parameters. The plus comparator retains the previous i times DIFFERENCE formula. Same support pairs imply the same rank formula 4 sum_(t_j!=0)dim(E_j), same maximal ranks128 and64 per ambient half, and the unchanged actual observation (J_H A,4A,0).

The corrected simple witness is alpha(X)=c_H(X), i.e. all t_j=1 and A=I. It is minus-skew, C-commuting, normal-spin neutral, and endogenous-covariant; observation is(J_H,4I,0), with trace-slot inverse1/4. The old c_H(X)h witness is minus-SELFadjoint, and therefore fails the corrected sharp-skew class. Multiplying it by i restores minus-skewness but loses C commutation. The12-dimensional survival claim survives; its coefficient equation and witness must change.

## 6. C commutation is NOT the same pairing compatibility

The SAME anti-linear C still has C²=-1 and fixes each real Clifford vector. However, writing C=C0 conjugation, the exact identities are

    C0† H+ C0 = conjugate(H+),
    C0† H- C0 = -conjugate(H-).

Thus C is an anti-linear isometry of h+ but an anti-linear ANTI-ISOMETRY of h-. The complex bilinear form B±(v,w)=h±(Cv,w) is alternating for plus and symmetric for minus. Therefore the corrected intersection must not inherit the label Sp(32,32): that label relies on the plus-compatible quaternionic Hermitian structure. State the corrected class explicitly as sharp-minus skew AND commuting with the fixed C. A group-name identification needs its own real-form proof. No source claim makes this C condition mandatory.

## Verification and acceptance limit

`/private/tmp/gu_adjoint_independent_probe_20261126.py` independently reconstructs the native Clifford algebra using exact Gaussian dyadic sparse blades, without numpy or BLAS. **30 exact controls passed**, including H± laws, C laws and pairing signs, symmetric/alternating bilinear forms, all four normal basis tensors/contractions, all12 corrected horizontal coefficient directions, and finite exterior-character counts. No numerical rank or tolerance is used. Completeness and dimension formulas use the written representation and right-inverse proofs above; this is internal mathematical review, not a Lean or external-expert certificate.

The correction is supported. Downstream source-side uses of the plus-sign fixture, source-labelled zero exclusion, old degree3 countercontrol, horizontal axial witness, and opposite-pairing descriptions must be reconciled. W2 calculations should retain their actual declared matrices and equations; a relation to the corrected source adjoint must be checked rather than silently inferred from an old label. No action-class, ledger, physical-prediction, or global GU verdict is justified by this correction.

## Integrated artifact follow-up

Reviewed `/private/tmp/gu-adjoint-wt-20261126/explorations/conditional-build/source-adjoint-spinless-placement-2026-11-26.md` and its `source_adjoint_spinless_probe.py` without rerunning heavy verification. The new pairing/class theorem and symbolic placement have no mathematical obstruction found. In particular the ordered exterior identity gives `(n-2)I+JGamma`; trace gives `2(n-1)Gamma`; the chiral right-input weights acquire `op` because they must cross the inserted odd Clifford vector. Its contracted trace acts by `(n-1)(2A+nB)`. The scalar q formulas, O-descent iff f=g=0, determinant `-mu²neg` and full15S invertibility under mu,a,e,g nonzero follow as stated. No physical mass or source density transfer is asserted.

Requested before acceptance: repair the old normal report's contradictory source-labelled frontmatter/lead and the accidental correction sentence “incorrectly called plus-comparator”; define `C=C0 conjugation` before writing the matrix equations with `C0†H±C0`; rename “changed real structure” to changed pairing compatibility, since C itself is fixed. These are correction-custody/notation requirements, not objections to the new counts or placement derivation. The scalar sterile-support result and Z4 dimensions remain as stated; this does not mean the old odd coefficient fixtures retain their source interpretation.


## Source custody challenge

# Independent source/coverage challenge — 2026-11-26

Read-only review of `gu-formalization` at supplied/fetched-by-parent `main` / `origin/main` revision `f754e924e6bdf9c9506a09e1bec2c8248dd6e941` (both local refs checked). No repository edits or heavy verification. Target: LB-CLASS / SC-MAS-02 full-ambient grade-one primitive placement. This is a source and novelty review, not acceptance of a newly computed class result.

## Highest-priority finding: primitive source adjoint attribution is wrong in Nov26 result

The official draft, printed p.23, eqs.3.24–3.28, explicitly uses the adjoint obtained by composing grade involution with reversal. I downloaded the official PDF, computed SHA256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4` (matching custody), rendered p.23 and visually checked eq3.27 and the accompanying prose/footnote.

For a real Clifford k-word, the printed involution gives

    sharp_minus = (-1)^(k(k+1)/2).

Thus real vectors are skew, and the printed unitary Lie algebra contains real degrees 1,2,5,6,9,10,13,14 and imaginary degrees 0,3,4,7,8,11,12. The footnote cautions that the old checkerboard decomposition should be checked; the sign follows directly from the stated involution and does not depend on trusting the whole table. The primitive Majorana pairing in eq3.24 pairs the two null Weyl halves. Neither this primitive pairing nor the table alone supplies the full §9.16 density-dual barred action.

This is ALREADY owned evidence: `explorations/conditional-build/source-lower-term-compatibility-2026-11-13.md:47` explicitly authenticates the same minus sign and real grade1 in u(64,64).

By contrast, `source-normal-tensor-class-2026-11-26.md:112` calls the reversion-only sign `(-1)^(k(k-1)/2)` the source pairing, and :178 calls `i c(n)` the source spinless line. Its finite theorem with the chosen plus pairing may be perfectly valid. Its attribution and source applicability are not. Preserve that theorem as the explicitly chosen K95 plus-pairing result; do not transfer its optional-C zero to the printed source primitive.

### Exact proposed repair checks (not independently run here)

In the existing K95 matrices, with plus-pairing matrix H_plus and real ambient volume Omega, take

    H_minus = i H_plus Omega.

Since Omega is plus-sharp-skew and anticommutes with every Clifford vector, H_minus is Hermitian and makes all real vectors sharp-skew. Keep the existing real Clifford C law separate. Under the same condition `[alpha,C]=0`, the odd phases swap. Reusing the already-proved multiplicities `(4,8,10,8,4)` gives:

| Conditional K95 tensor class | coefficient dimension | image | kernel |
|---|---:|---:|---:|
| block-Lorentz×SM, minus-sharp | 68 real | 44 real | 24 real |
| same plus `[alpha,C]=0` | 36 real | 24 real | 12 real |
| fixed endogenous+weak, minus-sharp | 4 real | 4 real | 0 |
| same plus `[alpha,C]=0` | 4 real | 4 real | 0 |

The 36 is `2*(4+10+4)` from degrees1,5,9. Its image is `2*((1+2)+(3+3)+(2+1))=24`; kernel is `2*(1+4+1)=12`. The four real fixed tensors `c_N(n)*{1,omega_H,omega_N,Omega}` all survive. Full ambient grade1 `alpha(v)=m c(v)` survives and is C-even, with `Gamma alpha=14m Id`.

**Important:** the adapter can also change the relation of C to the Hermitian form. Do not automatically call the resulting C-commuting group Sp(32,32), or identify K77 with K95. Directly check real form, pairing/C compatibility, signature and the required bridge. These arithmetic consequences are proposed verification targets, not a silent accepted migration.

Primary PDF: https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf

Read-only source artifacts: `/private/tmp/gu-source-spinless-20261126.pdf` and `/private/tmp/gu-source-spinless-p23.png`.

## What SC-MAS-02 actually fixes

The true-spin-zero claim is a diagonal geometric Spin invariant in `V* tensor V*`, embedded via Clifford grade1 in `V* tensor End(S)`. It is NOT a scalar resulting from dropping the one-form index, a normal-only tensor extended by zero, or an arbitrary all-End pseudoscalar. The full invariant line is the metric contraction, represented after a fixed Clifford identification by `alpha(v)=m c(v)` with the primitive real phase above.

For a nondegenerate H4+N10 split the same full tensor has both horizontal and normal pieces. Their coefficients are tied if this is one full ambient Spin scalar. Its separate contractions are 4m and 10m, with total14m. Allowing independent mH and mN is a split-isotropy class, not the single ambient scalar.

The source gives the group, primitive adjoint and this tensor carrier. It does not choose m(x,y), prove m=R/4 as a full bundle map, require C compatibility of every full-U connection, or supply a physical mass observable. Source §12.9's R(y)/4 is explicitly stylized; SC-MAS-01's local Weyl algebra is already closed. Equation11.10 labels both horizontal and fibre grade1×grade1 sectors, but their names do not construct full operator mass eigenvalues.

Covariance of the grade-one subspace requires transporting the Clifford reduction when the full U spinor frame acts. A fixed Clifford plane is preserved by its geometric normalizer, not by arbitrary U conjugation. That is a bridge condition, not an inconsistency: an adjoint-valued field need not itself be invariant under full gauge-frame changes. With a moving reduction `c -> U c U^-1`, the family `alpha=m c` transforms correctly. Do not substitute fixed-alpha invariance for this covariance.

## Unambiguous primitive placement and the remaining unknown cells

The authenticated NE variation is `delta_varpi d_A[alpha] nu = rho(alpha) nu`. This is source-fixed and independent of Shiab or SE choice. For the scalar line,

    delta D_NE nu = m J_Y nu,
    P_H delta D_NE nu = m J_H nu,
    Gamma_Y delta D_NE nu = 14m nu.

Thus under the retained q=(P_H,Gamma_Y,nu) output convention its NE image is `(m J_H nu,14m nu,0)`. Literal pullback alone keeps the horizontal one-form output; it does not turn it into an ordinary scalar. Nonzero m has spinor rank128 in the total-trace receiver. Its isolated independent-row/current coefficient is nonzero by polarization and invertibility of a nonnull gamma. This is a positive fixed bridge, not a physics theorem.

The rest of the raw operator must retain separate symbols:

- NW: actual declared Shiab map applied to `alpha wedge zeta`; its natural two-channel models are known, but no selected universal source coefficient can be inserted.
- SW: the printed negative barred/star operation; a particular formal metric adjoint adds a premise. Independent bars do not force it before the density/dual realization is specified.
- SE: zero for the displayed candidate; an admitted rival has an unspecified additional map. Keep its alpha derivative symbolic.
- Physical field readout: compose equation response with the actual time-symbol inverse before applying field observation. The equation-row map is not a field map.

No failure of the source's fundamental-mass claim follows merely because this matrix is not a scalar multiple of the full identity. The source never states that the full rolled fifteen-spinor operator is such a multiple, nor that its entire spectrum is one mass.

## Coverage / rediscovery warnings

1. `source-current-grading-membership-2026-11-12.md` already proves the independent-field pure scalar current discriminator, complete pointwise counterterm criterion, exact trace/scalar coordinate observation theorem, native hidden-K_t countercontrol, and zero-SE mixed-Shiab survivor. Recomputing current nonvanishing or using a fixed wedge-only condition will not shrink a new class.
2. `source-exterior-connection-2026-11-13.md` and `source-lower-term-compatibility-2026-11-13.md` already compute exterior versus coherent connection corrections and all-U lower-map obstruction, with paired metric-adjoint, normal-jet and geometric weighted-adjoint survivors explicitly separated. They already contain the primitive minus-adjoint custody.
3. `source-action-homogeneous-analytic-vacuum-2026-11-25.md`, §§C1–C4, already computes all zero-order blocks of the W2 leading grade1 tensor T1, the imposter/scalar 2×2 diagnostic, and the nonzero off-diagonal primed response. Its gamma contraction60 is explicitly not a universal physical mass. Substituting equal t_a gives the isotropic special case of existing formulae, not a new full candidate response theorem.
4. `source-action-physical-dynamics-2026-11-25.md`, §5, already computes canonical mY, mH,mN and actual `q_F[-sigma(dt)^-1 V_T](0,nu)` at both certified roots. Same geometry and RY=-10 give different exact spinless and observed instantaneous responses. Repeating that scalar-input root comparison is fully covered.
5. WGS-05's full20 K/C/P0/provenance/SM-incidence join remains open. `resolver-wave-e-source-owned-moving-252-full20-placement-2026-08-03.md` concerns a grade6 connection/grade5 252 insertion; it is not the grade1 spinless map. Older full20 Clifford contractions are reusable infrastructure, not authentication of the mass join.

## Can an exact source-required algebraic test fail independently of SE/Shiab/domain choice?

There is one genuine current failure: the repository's source-adjoint attribution is contradicted by the printed primitive and its own Nov13 custody. Repairing that does not falsify GU; it removes a false source transfer.

For SC-MAS-02, the representation-theoretic invariant line and its NE contraction are directly testable without SE/Shiab/domain choices, and they SURVIVE. No presently authenticated source statement says the line must satisfy the additional optional-C/plus-pairing zero, fixed full-U invariance, an identity mass matrix on the whole rolled carrier, or an autonomous literal observed evolution. Imposing any of those to obtain failure would change the tested class.

If a completed required map M is supplied, the sharp bridge test is to compare its restriction to the line with the claimed primitive/observable tensor, including all rows and field readout. A missing map cannot be assigned zero. A candidate-local response is not an exclusion of all source-compatible choices.

## Ranked next work

0. **Correct source pairing custody and its downstream optional-C applicability now.** This is concrete, finite and necessary before any new spinless placement claim. Preserve the plus-pairing theorem, verify the minus-pairing adapter/category and update source labels without erasing history. This has higher value than another unspecified-bridge narrative.
1. **Bounded full-ambient primitive placement after that correction.** Finish one table of source-fixed NE and symbolic NW/SW/SE cells, the full versus split scalar relation, and the moving-Clifford covariance identity. It closes a small bridge, but should not be advertised as a new physical full20 mass result. The all-equal-t W2 calculation itself is already covered algebraically.
2. **Strongest currently executable distinct whole-class alternative:** full-R reached-spin4 auxiliary compatibility, or one true adjoint-cokernel pairing, using the exact existing seeds. The Nov26 normal result §6.7 explicitly distinguishes this from completed constrained-Q realization. It can remove a genuine class of response completions if a true cokernel functional detects the residual. It remains candidate-only until source necessity/physical admission is shown. An image outside the existing envelope is not a failure certificate.
3. **Defer a purported source full20 physical-mass kill** until an authenticated density/row/operator/readout or exact source necessity of the proposed constraint exists. WGS-05 is a construction prompt, not permission to guess that datum.

No new tests run in this review. The primary checksum and visual source check were performed; existing proof/probe claims were inspected at their declared scope.


## Independent placement review

# Independent T2 review: full ambient spinless placement

Reviewed `/private/tmp/gu-spinless-placement-20261126.md` and `/private/tmp/gu-spinless-placement-probe-20261126.py` against supplied revision `f754e924e6bdf9c9506a09e1bec2c8248dd6e941`. No owner edits or heavy computation. Replayed the dependency-free probe: **392 exact identities pass**.

## Disposition

**PASS for the conditional finite algebra and stated source ceiling, with two wording clarifications below.** No mathematical defect found in the ordered insertion, right-input chiral-weight transport, conditional SW adjoint, or literal-observation descent criterion. This is an internal mathematical review, not proof-assistant or external certification.

The primary-adjoint correction came from my earlier source review. I do **not** count this as an independent review of mathematical/source content I supplied. The placement derivation and probe being reviewed were supplied by another agent.

## Independent derivation checks

### 1. Ordered exterior insertion

For each output slot u,

    sum_v eta_v c_v(c_v zeta_u-c_u zeta_v)
      = n zeta_u - (2 zeta_u-c_u Gamma zeta)
      = (n-2)zeta_u+c_u Gamma zeta.

Hence Gamma C = `((n-2)+n)Gamma=2(n-1)Gamma`, and the actual exterior map `a C+(c0/2)J Gamma C` gives exactly `mu[(n-2)a I+(a+(n-1)c0)JGamma]`. The reversed multiplication produces a different map; it is not an equivalent convention. The probe independently builds alpha wedge zeta before contraction and checks all coefficient blocks, rather than only substituting the final closed expression.

Pure-wedge control: `c0=-a` gives `(n-2)a(I-JGamma)`, agreeing with the stated conversion. No principal coefficient substitution that commutes alpha past gamma is valid here.

### 2. Chiral right-input weights

Since alpha is odd, `A alpha=alpha A^op`. Since JGamma is even, it commutes with A and A^op. Thus `Phi_A(alpha wedge zeta)` is precisely equation(5). On applying Gamma, `Gamma A^op=A Gamma`, explaining why the trace coefficient returns to `(n-1)(2A+nB)` while the gamma-traceless coefficient retains `(n-2)A^op`. This checks the potentially easy-to-miss second swap.

For southeast principal `c(xi)S`, minimal covariantization gives `sum_v c^v S alpha_v=mu n S^op`; left-input `S c(xi)` instead gives `mu n S`. These statements require the fixed-weight/right-input convention expressly stated in the note; moving weights or arbitrary source rivals are not covered.

### 3. SW adjoint

For fixed metric density and a specified nondegenerate Hermitian pairing, `(alpha wedge)^*` is contraction by alpha-sharp. Thus `delta(delta_A)=chi conjugate(mu)Gamma`. Multiplication by `-g` gives the note's `-g chi conjugate(mu)Gamma`, reducing to `mu g Gamma` only after imposing the sharp-skew connection relation. This is correct for either uniform Clifford sign.

This does not constrain independent barred fields to be adjoints. It does require the connection/dual prescription defining the formal star to be the declared one. The note correctly retains B_SW otherwise. Preserve that distinction in owner wording.

### 4. Observation and exact iff condition

The kernel of literal `O=(P_H zeta,nu)` consists of `(zeta_N,0)`. Its Gamma_N image is all S: `zeta_N=J_N psi/m_N` realizes any psi. For this hidden input the observed output is

    mu (f J_H psi, g psi).

For mu nonzero, injectivity of J_H and independence of the two output slots imply necessity of `f=g=0`. The same substitution into equation(1) proves sufficiency; Z_SE has no effect because hidden nu=0. This iff concerns the stated primitive zeroth-order endomorphism in fixed coordinates. It is not an autonomous physical evolution or full PDE descent theorem.

The augmented q kernel has additionally Gamma_N zeta=0, so its output remains hidden for every a,c0,e,g in this grammar. Equations(2)–(4) follow. Direct subtraction verifies `beta-(h/n)tau` has coefficient mu k, as does b_RS. Therefore no distinct coefficient for those two ambient-RS pieces can appear in this scalar Phi slice.

### 5. Rank and provenance

With SE=0, the trace/nu coefficient matrix after factoring mu is `[[ell,n e],[g,0]]`, determinant `-n e g`. For a,e,g,mu nonzero and n14, the independent gamma-traceless coefficient `mu(n-2)a` is also nonzero, giving full raw15S algebraic rank. Unknown SE can change this; physical masses cannot be read from these eigenvalues.

## Two clarifications for integration

1. State the actual 2x2 determinant as **`-mu^2 n e g`**, or explicitly say mu has been factored out before reporting `-n e g`. The note currently says “coefficient determinant,” so this is clarification, not a failed argument.
2. Replace “new source-faithful content” by **“new conditional placement in the natural two-channel family”** where the non-NE coefficients are discussed. Source-fixed carrier/NE content, the declared natural Phi, conditional formal SW, and unbuilt SE must retain separate labels. The present note otherwise states these boundaries correctly.

## Novelty / hostile scope check

The prior W2 leading-connection formula already contains equal-t isotropic placement as a specialization; scalar root responses and current nonvanishing are also covered. The defensible new contribution is the organized all-coefficient natural-family placement, its chiral input-weight swap, independent-field provenance, and exact literal-versus-augmented primitive descent criterion. Do not call it full20 physical mass recovery, a source-selected matrix, or a source exclusion.

The newly authenticated primitive minus-adjoint does not fix §9.16's global density/dualization or solve K77/K95 transport. The old plus-pairing tensor theorem can survive as a comparator, but its source label and optional-C transfer cannot be retained. This source-custody point is carried from my earlier report, not counted as an independent acceptance result here.

## Integrated follow-up

Reviewer checked the owner draft and exact probe. Remaining old source labels were changed to plus/reversion comparator; the correction sentence retains original source-side attribution as history. Matrix equations now distinguish C0 from antilinear C; heading names changed pairing compatibility. Ordered insertion and all displayed rank/descent claims rechecked. No mathematical objection remains.
