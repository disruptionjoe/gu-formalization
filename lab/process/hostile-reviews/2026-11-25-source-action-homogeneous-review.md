---
status: process
doc_type: hostile-review
created: '2026-11-25'
---

# Homogeneous analytic branch: independent acceptance

Three specialist agents cross-reviewed the integrated written proof and exact-control source. Each excluded its own contribution from independent acceptance: full-residual/analytic proof reviewed by the hostile and coupled-geometry specialists; exact metric/boundary proof reviewed by analytic and hostile specialists; fermion response reviewed by analytic and coupled-geometry specialists. These are internal model reviews, not external-expert or Lean certification. Root serialized the300 exact assertions (212 geometry/representation/reduced-polynomial,69 metric-jet/bound,18 native fermion,1 omitted-receiver countercontrol). Assertion count is not independent theorem count.

Accepted at scoped T2. Corrections before acceptance: specify connected isotropy beside216; distinguish original quotient from local/covered Spin construction; hold boundary/framing structures while recomputing the metric-dependent observation section. No numerical native convergence radius, kappa1, full PDE uniqueness, physical vacuum or source/C verdict is claimed.

## Hostile review of the integrated homogeneous analytic branch

Reviewed: `gu/explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md`, sections A, B and their claims in D/E. Base `35a2321af2c7c72e4904319b615fe1f781b5359b`. I previously contributed the section-C response calculation, so I do **not** count this as independent acceptance of C; the other reviewer owns that check. No tests executed in this review. Root reports300 exact controls passed; the existence conclusion rests on the written proof, not that count.

## Verdict

**Accept A+B as a scoped T2 result. No blocking correction found.** The integrated draft closes the plausible mathematical failures identified during selection. It establishes a real analytic local branch of the chosen action for sufficiently small nonzero h, with coupled stationarity only in the expressly defined product-regulator variation class. It does not claim a source-selected or physical GU vacuum.

## Strongest attempted counterarguments

### 1. Noncompact symmetry reduction could lose equations

This would be serious if the construction merely extremized the action restricted to invariant fields. The draft explicitly avoids that. Every operation in the full residual is natural, so the residual of invariant input is invariant; vanishing of its value at p therefore makes it vanish as the full local section. No compact averaging or principle of symmetric criticality is invoked. Even degeneracy of the pairing restricted to E would not invalidate this argument.

### 2. The affine group might not preserve the actual geometry

The displayed transformation is correct for the tautological horizontal y pairing and trace-reversed vertical form. It transforms x as well as y, which is necessary. The only use of constant base g0 in this construction is through its zero affine connection, so failure of a generic GL+ transformation to preserve the numerical matrix g0 does not spoil ambient invariance. Observation is explicitly outside the full-affine invariance assertion.

The original stabilizer ambiguity is repaired: G/H0 is a homogeneous cover with connected H0, and the proof uses a local spin chart. The draft does not assert a global spin lift on the uncovered space. Central spin-lift signs act trivially on the displacement endomorphisms. These conventions suffice for the local theorem.

### 3. S or its adjoints might leave the real Lie algebra

The draft correctly retains both i-anticommutator factors in the actual Shiab recipe. With gamma_a^sharp=−gamma_a, both Clifford one-forms and bivectors have the required skew reality; commutator and i-anticommutator preserve u(H). The nondegenerate real trace/form pairing yields real natural formal adjoints. There is no omitted projection of S and no modification of the mass identity. This matches the actual candidate, not a Euclidean substitute.

### 4. The216-dimensional count might count the wrong object

For connected isotropy the tangent decomposition is V11+V22+V00. End of the full128-dimensional complex spin module is the full Clifford algebra, hence the full exterior algebra of the14-dimensional tangent module. Independent character arithmetic agrees with total multiplicities32,80,104, giving216. The trace trivial line pairs even and odd exterior characters, giving108 per parity. Real invariant dimension equals the complex dimension after complexification of the real coefficient representation. The count is explicitly not a physical degree-of-freedom count, and it is not extended to disconnected isotropy without proof.

### 5. Finite-dimensional IFT might conceal an unbounded PDE inverse

No such inverse is used. On homogeneous sections K becomes a finite linear map, while N remains bilinear; all norms are finite in the selected E. The full normalized map has derivative Id at h=t=0. Its section extension is finite-dimensional, so convergence in E implies convergence in every compact C^ell seminorm with finite evaluation constants. The uniform parameter radius applies to each compact derivative seminorm because the basis is finite, not because an unrestricted differential operator is bounded.

The majorant radius and tail estimate are sound. For q<1/(k+2sqrt(ns)), the discriminant is positive and at most1, and the contraction factor `1−sqrt(discriminant)` lies in[0,1). The n=0 and k=n=0 cases are separately handled. The tail estimate follows by factoring `(q/rho)^(M+1)` from a nonnegative coefficient sum bounded by m(rho); no missing geometric-series factor is required. Norm constants are symbolic and no numerical radius or h=1 claim appears.

Uniqueness is limited to the invariant ball. The original action is singular in parameter at h=0; the draft correctly uses that point only as the normalized analytic anchor, with actual stationary configurations at nonzero h.

### 6. Connection stationarity might not imply base-metric stationarity

The draft supplies an independent exact argument, rather than making that implication. At constant g0, every geometric dependence on base g passes through Gamma(g) and its derivatives. Its linear variation has at least one base derivative of p. In a translation-compatible frame, the fixed branch coefficients and geometry are x-independent. Direct variation of the original finite-jet density is therefore a finite sum C_alpha(h,y) partial_x^alpha p, all |alpha|>=1. Compact base support makes its product-domain integral zero without discarding fibre-boundary terms or exchanging an infinite series with variation.

Holding Ahat fixed still changes T=Ahat−B[g]; that dependence is included through B[g], not omitted. Zero barred and unbarred matter solves both equations; compact dressing variations reduce to compact connection variations. This proves exactly the stated coupled test class, not arbitrary ambient metric or boundary variations. The distinction is clear enough in both the main text and result table.

### 7. The analytic branch might repair the old charged boundary accidentally

The C1-open curvature argument excludes that inference. The nonzero tangential reference curvature is detected by a fixed component; the quadratic curvature perturbation is bounded by C1||T||+C2||T||². The stated delta keeps the component nonzero. Tangentially flat pure-gauge boundary data cannot be gauge-equivalent to such a connection. Since the analytic branch tends to B in C1, it lies in this exclusion neighborhood for sufficiently small h. This applies even to k=0, and its scope is the fixed boundary geometry, not a count or topological no-go.

### 8. Equal base connections might not preserve the whole action

Under the explicit same-frame/same-independent-fields/same-domain assumptions, the candidate's geometric coefficients depend only on Gamma(g), so the equal-connection lemma is correct. Its observation distinction is also exact: the section g is parallel for its own connection, hence the vertical term vanishes on pullback and s_g^*G_g=g. Constant scale c>0 preserves Gamma but moves the section. The draft correctly refuses to call this local Weyl symmetry, physical gauge equivalence or a scale prediction.

## Remaining weakness and accepted wording ceiling

The mathematical branch is now actual, but it is a local zero-matter solution in one chosen source-informed completion and boundary/variation class. It establishes neither physical perturbative stability nor a positive or causal state space. It supplies no family receiver, no finite-h=1 continuation and no global finite-action or normalizability claim. These are material limitations, and the draft carries them prominently.

The most misleading possible summary would be “GU's source action now has a physical vacuum.” The supported summary is **“the fixed K95 candidate has an actual small-inverse-kappa homogeneous coupled stationary branch in the stated local product-regulator problem.”** The integrated text supports that summary. No source, class-C or ledger verdict should move from this result alone.

No mandatory edit requested. Preserve the local/connected-isotropy qualifiers when shortening the executive return.


## Independent specialist review of coupled and response arcs

Reviewed sections B and C, their integration in `source-action-homogeneous-analytic-vacuum-2026-11-25.md`, and the resulting claim ceilings. Section A derives from my own contribution and is **not independently certified by this review**. Root reports300 exact assertions passed; this reviewer performed no additional execution.

## Verdict

**Accept B+C and their integrated scope as candidate T2 mathematics.** No blocking mathematical correction found. One wording clarification in B4 is recommended below, to prevent “held external structures” being read as holding the actual g-dependent observation map fixed.

## B1: exact coupled stationarity

The proof correctly fixes the coordinate coefficients of Ahat while varying the base metric. It does not rely on a bulk envelope identity whose induced connection variation could reach the fibre boundary. In the specified frame, the original action's g dependence enters through Gamma(g), its finite jets and the ensuing G/B/Clifford/Hodge/density constructions. At constant g0, δGamma contains a base derivative of p; varying the inverse g factor produces no bare-p term because ∂g0=0. Ahat(h,y) and the background coefficients are x-independent.

Therefore every term in the exact first variation has at least one x derivative of compactly supported p and an x-independent coefficient. Direct product-domain integration kills it while retaining all fibre dependence and boundary contributions. No infinite series/variation exchange or unjustified independent ambient-metric variation appears. Compact connection variations are settled by the full residual, zero fermions/bars solve their primitive equations, and compact epsilon variations reduce to the candidate's dressed connection redundancy.

This establishes the stated local stationary problem, not arbitrary boundary stationarity, physical evolution, or a native finite-action state. Those limitations remain visible in B2 and the final table.

## B3: open boundary exclusion

The curvature receiver is nonzero for B at the prior explicitly specified spherical pole. The estimate for D_B T+T∧T in a fixed auxiliary C1 norm is standard local algebra with bounded coefficients. The proposed delta makes the curvature change strictly less than m/2, so it excludes flat boundary traces for *all* sufficiently small displacements, not only invariant ones. Since every supplied U_k⁻¹dU_k boundary is flat, the all-k statement is correct and includes k=0. It remains scoped to the fixed leading geometry and boundary chart; gauge equivalence cannot turn nonzero curvature into zero.

## B4: equal-connection identity

The lemma is exact for the candidate: identical Gamma gives identical G_g on the same metric-bundle coordinates, hence identical B, Clifford/Hodge, pairing and ambient action in the same frame. Constant positive scale changes preserve Gamma, whereas variable scale changes generally do not. Metric compatibility gives the section pullback s_g*G_g=g, so the differing section metrics are real mathematical differences even when the ambient geometry is unchanged.

The text correctly withholds a physical gauge or scale-prediction claim: coordinate/unit changes and transport of all external data can change the interpretation. **Suggested wording:** replace “hold ... external structures fixed” with “hold ... boundary/framing structures fixed; recompute the actual observation section from each g.” This avoids apparently fixing q while subsequently varying s_g. It does not alter the lemma.

## C: independent algebra check

For T1_a=t_a gamma_a, five t values are21/4 and nine15/4, hence sum t_a=60. The scalar contraction alone is not the complete zero-order vertex. Applying the Clifford anticommutator to the full repaired connection variation gives exactly

    r_a=(60−2t_a)ζ_a+t_a gamma_a(Gamma ζ+nu),
    s=Gamma_t ζ−30nu.

For Iψ=(10J_Hψ,−4J_Nψ), Gamma I=40−40=0 and Gamma_t I=210−156=54. The horizontal row becomes495J_Hψ+(21/4)J_Hphi. Thus the stated diagnostic matrix, determinant−30267/2 and previous-kernel response(600ψ,−546ψ) are correct. Full rank256 is the rank of two ambient rank128 slots under this diagnostic, not an observed-family count or a claim about propagating modes.

For pure primed scalar eta, F⁻¹ gives ζ=−Jeta/2, nu=−6eta. Before R, the vertex has

    r_a=(−30−12t_a)gamma_a eta,
    s=150eta,
    Gamma r=−1140eta.

R therefore gives v=720eta and u_a=(330−12t_a)gamma_a eta, i.e.267 or285. This directly verifies the slot mixing and defeats the tempting60-as-universal-mass reading. F/R are correctly kept distinct, and the equation-row diagnostic is not confused with a field readout. Since the connection perturbation does not vary g, no derivative-of-F term is missing from this zero-order correction; geometric variations would require those already-recorded terms.

## Integrated reporting

The final text distinguishes actual small-h local stationarity, unknown numeric continuation to h=1, nonphysical compact regulator, external-boundary failure, and missing state/observation interpretation. It acknowledges earlier stationary constructions with different carriers. The pure vacuum branch is not called a GU completion or class-C survivor. The response provides a concrete calculable consequence of the candidate background, not a mass spectrum. These are appropriate scientific ceilings.


## Independent review of analytic reduction and fermion response

Reviewer: networking/observer engineering specialist. Reviewed sections A and C and their integrated scope in `source-action-homogeneous-analytic-vacuum-2026-11-25.md`, plus the corresponding character/majorant/current portions of `source_action_homogeneous_probe.py`. Section B is my contribution and is **not independently certified by this review**. Root reports 300 exact controls passed; I did not rerun tests or edit native files.

## Verdict

**Accept A and C at scoped T2. No mathematical blocker found.** The result is actual local small-h existence for the specified candidate's complete connected-isotropy invariant sector, not a global native-domain theorem, h=1 result or physical mass prediction.

## A: independent checks and hostile challenges

1. **Actual symmetry:** the simultaneous affine action on x and y preserves the horizontal tautological pairing and both vertical trace terms. Full GL+ congruence is available because the reference enters through its flat connection, not a frozen horizontal g0 coefficient. The fixed observation section and external boundary need not share this symmetry; the integrated text retains that distinction.

2. **Connected cover scope:** the use of H0=SO+(3,1), a homogeneous cover and local spin chart is sufficient for a local associated-bundle construction. Disconnected isotropy could impose additional invariance constraints, so216 should not be advertised as the dimension for every original global quotient. The frontmatter/A1 already state the required connected/local scope. A minor clarity improvement would repeat “connected-isotropy” beside216 in the opening plain-language paragraph.

3. **Full invariant dimension:** the complex tangent character is V11+V22+V00. End of the full128-dimensional complex Dirac module is Cl14(C), hence Lambda* of that tangent module. The probe builds every exterior weight and reconstructs the full character from nonnegative irreducible multiplicities. Its multiplicity subtraction formula is correct for sl2×sl2. The reported16,40,52 in each parity sum to108; Hom against the three multiplicity-one domain irreducibles gives216 total, without multiplying again by their dimensions. The real u(H) complexifies to End(S); invariant real kernels complexify to the corresponding complex invariant kernels. Thus the real dimension claim follows. The trace-line factor explains the identical even/odd characters.

4. **No restricted-criticality shortcut:** S,K,N are the actual equivariant full residual operations. An invariant input has invariant full residual, determined by its value at p. Solving that value as a vector in E therefore kills every Euler receiver, not merely the pairing against invariant variations. No averaging over noncompact isotropy, positive restricted pairing, or principle of symmetric criticality is used. K becomes a finite linear map through evaluation of a uniquely transported invariant section; arbitrary normal derivatives are not being discarded.

5. **Real structure and adjoints:** the declared matrix operations preserve u(H), and the local formal adjoint is natural under the same isometry and density. Neither compactification nor quaternionic narrowing is smuggled into the finite-dimensional space. Potential degeneracy of the pairing restricted to E would not invalidate the full vector residual argument.

6. **Majorant and radius:** for n>0 the smaller positive discriminant root is r=1/(k+2 sqrt(ns)). The written m(q) is the nonnegative branch of m=q(s+km+nm²). Its ball-invariance and Lipschitz bound q(k+2nm)=1−sqrt(discriminant)<1 hold for0<q<r. The n=0 and k=n=0 cases are handled. Norms are arbitrary finite-dimensional auxiliary norms, not a physical positive metric.

7. **Tail estimate:** for q<rho<r, positivity of the majorant coefficients gives
   `sum_(j>M) a_j q^j <= (q/rho)^(M+1) sum_(j>M) a_j rho^j <= m(rho)(q/rho)^(M+1)`.
   Thus the stated bound does not need an additional geometric-series denominator. Finite-dimensional section evaluation gives the claimed compact C^ell bounds. It gives no unrestricted PDE inverse or global L2 control. Native numerical s,k,n have not been calculated, so no numerical coupling interval follows.

## C: independent algebra

1. The actual T1 weights sum to `5(21/4)+9(15/4)=60`. Since each gamma_a is H-skew, real weights are appropriate; adding i would change that real-algebra condition.
2. Expanding the ordered current vertex gives `(60−2t_a)zeta_a+t_a gamma_a(Gamma zeta+nu)` and `Gamma_t zeta−30nu`. The anticommutation identity retains the noncommuting lower-order contribution; it is not a scalar slash approximation.
3. On the owned mixed injection and scalar input, the coefficients495,21/4,54,−30 are correct. In particular210−156=54, and the determinant is−30267/2. The former central-horizontal diagnostic kernel phi=20psi is sent to(600psi,−546psi). There is no contradiction with the old central-probe rank loss because this background displacement is noncentral and includes normal components.
4. For pure primed scalar input, F^-1 gives zeta=−J eta/2 and nu=−6eta. The unprimed output is `r_a=(−30−12t_a)gamma_a eta`, scalar150eta, and Gamma r=−1140eta. Applying the distinct row map R gives scalar720eta and one-form `(330−12t_a)gamma_a eta`, hence267/285. The manuscript's numbers and interpretation are correct.
5. The injection and scalar slot are algebraically owned, but are not the completed pair of true-family embeddings. d_E remains an equation-row diagnostic. Full rank256 is a pointwise algebra statement, not a physical family multiplicity. The coupled slot response explicitly prevents interpreting60 as a universal particle mass.

## Acceptance ceiling and continuation

The claim is stronger than a formal recurrence and different from K2529's restricted homogeneous inverse; it is not the first analytic homogeneous construction in the repository. K2519's different independent-ambient-metric seeds remain properly acknowledged. The integrated restrictions to local spin/quotient data, product variation problem, small inverse kappa, zero matter and a source-informed candidate must remain in the executive return.

After acceptance, do not requeue formal existence or additional formal coefficients for this sector. A numerical continuation interval or source-typed perturbation/observation question would add new information. The solved216-dimensional sector is not a reason to replace the standing whole-class/source-relevance prioritization with indefinite candidate tuning.
