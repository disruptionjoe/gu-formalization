---
title: What an observed slice needs for predictive completion
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T1
expected_delta: Test actual observed-history completeness and a structurally defined finite local predictive
  completion class.
actual_delta: Actual unrestricted analytic solution germs realize every local observed field history and
  have an infinite-dimensional whole-history kernel. A varying-cone theorem excludes the stated finite-local
  lift class. Finite normalization does not select a signed coefficient average. No source/physical/class-C
  verdict.
class_covered: Analytic first-order operators with an invertible normal symbol and surjective literal
  section map; for the exclusion, the open Lorentz metric-fibre shifted-Clifford-cone symbol class and
  finite-order spatial differential lifts from finite-rank fibre-independent analytic first-order base
  evolution with arbitrary local analytic Cauchy data. The actual W2 K95 candidate belongs; class-C/source
  necessity is not established.
premises:
- lab/sources/source-claim-register.yaml#SC-GEO-52
- lab/sources/source-claim-register.yaml#SC-OP-04
- lab/sources/source-claim-register.yaml#SC-OP-05
- lab/sources/source-claim-register.yaml#SC-META-52
- lab/sources/source-claim-register.yaml#SC-META-53
- explorations/conditional-build/source-action-physical-dynamics-2026-11-25.md
- explorations/conditional-build/source-action-offsection-metric-2026-11-25.md
source_bridge:
  status: conditional
  reason: Source observation and operator ingredients motivate the test; source has not selected this
    repaired symbol, a physical domain/contour, or the excluded finite local lift. SC-META52/53 explicitly
    leave boundary and positive-state work open.
kill_condition: Exclude only INTERNAL-FINITE-LOCAL-METRIC-FIBRE-LIFT under its complete hypotheses. Neither
  all four-dimensional completions nor GU/class C is excluded.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-FINITE-LOCAL-METRIC-FIBRE-LIFT
internal_target_verdict: excluded under the stated open-fibre, finite-order, fixed-first-order-dynamics
  and free-data premises
canon_verdict_change: none
---

# What an observed slice needs for predictive completion

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: A concrete actual-domain and finite-local-completion discriminator.
actual_delta: Onto but noninjective observed analytic histories; precisely scoped finite-local lift exclusion; separate finite-normalization selection burden.
```

## One-page synthesis

**The equations alone, in their unrestricted local analytic category, do not select the observed history.** Every analytic observed field history can be extended to an actual ambient solution. Moreover, infinitely many nonzero ambient solution germs have exactly zero observed history. These are stronger statements than two initially indistinguishable fields later separating.

**A large simple repair class is unavailable.** No nonzero finite-order spatial differential lift can embed freely initialized, finite-rank four-dimensional fields obeying a fibre-independent analytic first-order evolution into these ambient equations across an open metric-fibre patch. The reason is geometric: the horizontal propagation cone varies with the fibre metric, while the proposed finite base system has one fixed characteristic polynomial at each base point/covector.

**Finite normalization is another requirement, not the missing predictive law.** A finite smooth weight does not repair literal thin trace on the same off-shell graph core. Even bounded averaging can retain unresolved initial information. The owned sign-changing metric coefficient also admits opposite signed averages under different added normalized weights. This does not construct two physical gravity theories.

| Epistemic state | Result or remaining possibility |
|---|---|
| ESTABLISHED | Analytic history surjectivity, infinite whole-history kernel, exact finite-jet ranks and the conditional weighting lemma. |
| RULED OUT | The explicitly defined finite-local lift class below; finite normalization alone as a selection of the signed receiver average. |
| UNDETERMINED | A source-admitted physical domain, conjugacy contour, boundary law, nonlocal completion, or actual effective gravitational reduction. |
| NOT MODELED | Server/client ontology, minds, agents and information-processing architecture. None is established or excluded here. |

A predictive observed theory need not reconstruct every ambient state. It must supply a law governing observed histories and make any retained hidden information sufficient for the claimed predictions. Deterministic field equations may select a proper solution class; a stochastic or quantum law may instead assign nontrivial probabilities with full history support. Surjectivity alone excludes neither option. A compatible boundary, nonlocal or statistical rule could supply the missing law; none is selected by these theorems.

**Grade:** internal T1 acceptance of the precisely named mathematical class exclusion; two independent mathematical reviews, separate hostile/source review, exact controls and Lean finite-algebra core. CK, free-jet comparison and the determinant/continuity argument are written mathematics, not fully formalized Lean. No source, physics-ledger, class-C, canon or paper verdict changes. **Weakest unproved link:** source/physical necessity of the tested domain and completion category. **Class-C representativeness:** not established.

```gu-typed-objects
result: analytic observed-history image and finite-local completion exclusion
carrier: full rank1920 complex rolled Dirac module to rank640 literal observed field module LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=S-FULL-DIRAC
pairing: independent dual row action; no selected positive Hilbert quotient ON=full_Dirac_field_module
real_structure: K95 full complex spinors; physical conjugacy contour unselected
grading: no physical chiral or family grading is imposed
action_owner: repository-construction fixed W2 full-U completion and explicit structural symbol class
target: actual solution history restriction and finite differential lifts MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). Preserve source2+1, independent bars, full U(64,64), literal contraction and K95/K77 distinctions. The source's boundary-value posture is not a freely initialized four-dimensional Cauchy system. An exclusion of the latter is not a refutation of the former.

## 1. Domain and symbol actually used

Let D=A^I(X)partial_I+C(X) be the actual repaired candidate fermion operator at either certified stationary zero-matter background. The local analytic coefficients include the curved metric-fibre connection, stationary displacement and all lower terms. Its full rolled carrier is E=(T*Y tensor S) direct-sum S, complex rank1920. Literal field observation is q_F(zeta,nu)=(zeta_H,nu)|section, complex rank640; the six-slot equation/trace diagnostic is a different map.

The owned factorization is

    R sigma(D)(xi) F^-1 = diag(c(xi),-c(xi)).

F and R differ. This gives a similarity for temporal evolution ratios, not for D itself. A non-null normal principal coefficient is invertible. The section has codimension10 and admits a local analytic coordinate chart z1=...=z10=0. No claim about a global section or a global spin trivialization is needed.

The domain here consists of local analytic solution germs. Existence neighborhoods may depend on the input. This is not a uniform Sobolev evolution space, a C0 semigroup, a physical contour, normal-L2 admission or a causal prescription. The sharp4/9/2 trace thresholds remain scoped to the earlier frozen benchmark.

## 2. Every local analytic observed history has an actual lift

**Theorem (structural analytic class).** Suppose D is an analytic first-order system, an analytic hypersurface H contains the observation section, D has invertible normal principal coefficient along H near a point, and q is a constant-rank surjective analytic bundle map on the section. Then the restriction from local analytic solutions of D to analytic observed field germs is onto.

**Proof.** In coordinates choose H={z1=0}. For an arbitrary observed analytic history f(t,x), choose a local analytic right inverse J of q and extend Jf analytically to H, for example constant in the other normal variables in an analytic trivialization. Cauchy–Kowalevski applied with z1 as the solving coordinate yields a unique local analytic solution with these hypersurface data. Its section restriction is f. The actual lower terms are retained. The standard analytic noncharacteristic existence theorem is the input; see [Princeton PDE notes, CK theorem](https://web.math.princeton.edu/~seri/courses/theNotes.pdf). This application and its GU scope are derived here.

For the actual candidate, a positive normal direction suffices, the factorization supplies invertibility, and q_F has an analytic right inverse. Thus both stationary backgrounds, and every analytic lower-term change retaining these symbol/readout premises, satisfy the theorem.

**Consequences.** Every finite observed jet is realizable. Any purported necessary local differential relation F(j^k f)=0 on the observed fields alone must hold for all analytic f, hence for every jet (realized by polynomials). It cannot select a proper observed solution class in this unrestricted category.

This is not a causal prediction algorithm: the normal-hypersurface data already contain the entire prescribed base-time history. It does not establish that every history is physically admitted or empirically possible.

With independent barred rows set to zero, these fermion solutions also give exact local classical coupled solutions on the already stationary bosonic background: every matter contribution to bosonic variation is bilinear in bar and chi, hence zero. This stronger lift uses the candidate's independent-bar grammar. A physical conjugacy condition bar=chi-dagger H would change that premise; it is not assumed satisfied.

## 3. Even the entire observed history does not reconstruct the ambient germ

Use the same normal hypersurface H and choose data z2^j v, j=1,2,..., with nonzero analytic carrier section v. They vanish on the observation section for all base times and positions but are independent nonzero analytic germs on H. CK extends each to an actual solution. Therefore the entire-history restriction has an infinite-dimensional kernel.

This is dynamical invisibility, not merely membership in instantaneous ker(q). The earlier initially-hidden/later-visible witnesses remain distinct. The new invisible solution space is not automatically a gauge symmetry: the prior additive local gauge-identity result remains. A chosen nonlocal quotient may identify some states, but that is extra structure.

### Quantified finite temporal-jet burden

At one base-time Cauchy slice restrict initial fields to

    psi(0,x,z)=sum_(j=0)^N z1^j v_j/j!,   v_j in C^1920.

All other initial spatial dependence is fixed. The actual map to observed temporal jets y_j=partial_t^j(q_F psi) at a point is block triangular. Its jth diagonal block is q_F M_n^j, with M_n=-A_t^-1 A_n. Coefficient/readout derivatives enter lower blocks. Since M_n is invertible and q_F is onto, every diagonal block has rank640. Therefore

    rank = 640(N+1),   nullity = 1280(N+1),  over C.

The corresponding real rank/nullity are1280(N+1) and2560(N+1). This is a finite initial-jet subfamily, not a dimension of the full ambient state.

A finite-dimensional differentiable state statistic with a differentiable prediction map recovering all these jets needs at least1280(N+1) real dimensions, by the chain rule on this polynomial-data family. No fixed finite point-state can meet all N. Both encoder and decoder regularity are required; arbitrary discontinuous set encodings are not addressed. This does not count four-dimensional field species, since a field has infinitely many spatial degrees of freedom. The next theorem addresses a specific finite-field completion class instead.

## 4. Varying-cone exclusion of finite local lifts

This tests a genuine differential-restriction escape from unrestricted-normal-jet non-autonomy. It does not reuse unrestricted witnesses against a restricted domain.

### Structural class and complete hypotheses

1. Work on an open Lorentz metric-fibre patch on which a fixed base-time covector tau is timelike. The actual K95 candidate has the symbol below; any analytic operator with the same shifted-cone property and arbitrary analytic lower terms is covered.
2. A base field u(t,x) in C^m, m finite, obeys a fibre-independent analytic first-order system

       partial_t u = sum_i B_i(t,x) partial_i u + B_0(t,x)u.

   Arbitrary local analytic spatial Cauchy data at every base point/time slice are admitted.
3. A finite-order spatial differential lift

       psi=E_y(t,x,partial_x)u=sum_(|alpha|<=N) E_alpha(t,x,y)partial_x^alpha u

   with analytic coefficients sends **every** such local base solution to an actual ambient Dpsi=0 solution throughout the open fibre patch. It need not be injective or full rank.

**Conclusion:** E=0. In particular no nonzero literal observed field can be retained by such a lift. This does not exclude all finite four-dimensional completions.

### Proof

For spatial covector k put a=y^-1(tau,tau)<0, d=y^-1(tau,k), e=y^-1(k,k). On the full rolled carrier, temporal evolution M_y(k)=-A_t^-1 A(k) is F-similar to repeated -c(tau)^-1 c(k). Clifford anticommutation yields

    M_y(k)^2+(2d/a)M_y(k)+(e/a)I=0,
    (M_y(k)-bI)^2=cI,
    b=-d/a,   c=d^2/a^2-e/a.

Through every fibre point vary only the spatial block of the inverse metric by lambda v tensor v, preserving its temporal row/column. Then a,d,b remain fixed and c_lambda=c_0-lambda(v dot k)^2/a. For small lambda the metric stays Lorentzian and tau timelike. For generic k, c_lambda ranges through an interval.

Let E_N be the leading spatial symbol. Freely admitted orderN+1 spatial Cauchy jets force

    M_y(k) E_N(y,k)=E_N(y,k) B(k),   B(k)=sum_i B_i k_i.

Normal/time derivatives of lift coefficients and connection lower terms contribute at most orderN: u has no independent fibre dependence. The common-shift squared relation therefore gives

    E_N(y_lambda,k) [(B(k)-bI)^2-c_lambda I]=0.

The determinant in brackets is a nonzero polynomial in c of degree m, leading coefficient(-1)^m. Except at finitely many c values it is invertible, forcing E_N=0. Continuity in lambda also forces zero at the exceptional values. Generic k is open dense, so polynomial continuity kills the complete spatial symbol. The deformation passed through every y; descend through the finite derivative orders, including order zero. QED.

Testing only one k direction or only diagonal fibre points would be insufficient; both gaps are explicitly avoided. The finite matrix identities are checked in [SliceCompletion.lean](../../Lean/GUFormalization/SliceCompletion.lean). The analytic/free-jet and finite-exceptional-set continuity steps remain written proofs reviewed by specialists.

### Corollaries, controls and survivors

An integrable order-zero normal transport law partial_a psi=L_a psi, admitting arbitrary finite-rank base data and preserved by a fixed first-order base evolution, gives an order-zero lift and is covered. A nonintegrable law already fails its own compatibility premise.

If B is allowed to depend on y, the principal relation can instead use E=I and B_y=M_y; the obstruction disappears at principal level. If spatial data are constrained, arbitrary highest jets are unavailable. These controls show exactly which assumptions do work; they are not constructed full solutions.

Survivors include nonlocal/spectral or infinite-order lifts, restricted Cauchy data, boundary/global selection, lower-dimensional/singular fibre support, reduced dynamics not satisfying a valid freely initialized finite first-order formulation, and different source symbols. A normal law containing tangential derivatives must be classified by its resulting lift; exponential tangential transport need not have finite differential order. No survivor is thereby established physically.

**A constructive local survivor.** After choosing J and an analytic extension to H, the CK construction gives a right inverse K of q on full local analytic spacetime-history germs. Restricting K to histories solving any chosen analytic base law embeds those histories into ambient solution germs. For a nontrivial fibre-independent analytic linear first-order finite-rank base system with freely admitted Cauchy data, using the observed history itself as state (or an injective observed output), the varying-cone theorem prevents this K from being a finite-order spatial differential lift across an open metric fibre. This exhibits a history-germ completion outside the excluded class. It is not canonical or source-selected, and supplies no causal, bounded, global or physical-admission guarantee.

## 5. Finite reduction needs selection as well as normalization

A smooth strictly positive finite fibre weight is locally equivalent to the existing smooth norm. Consequently the owned off-shell graph-trace cutoff sequence still has norm O(epsilon^5), derivative norm O(epsilon^4) and fixed nonzero thin trace in codimension10. Normalization cannot repair that same cutoff-stable graph core. This is a consequence of the existing theorem, not a fresh solution-space estimate.

A bounded average is a different measurement. For example, standard Gaussian probability on R gives a norm-one mean M and a constant lift J. Nevertheless f(y)=y satisfies Mf=0 and M(partial_y f)=1; the exact polynomial transport solution y+t acquires mean t. Thus bounded projection and finite normalization alone do not give closed mean dynamics. This is an explicit comparator, not the native observation or a claim that translations generate a bounded semigroup on the entire Gaussian L2 space.

The latest metric result supplies a separate discriminator. Its first-root coefficient has strict positive and negative values on a fixed-base fibre curve. By continuity it has opposite-sign open neighborhoods. On any domain containing these neighborhoods, let mu0 be a smooth positive probability with finite absolute coefficient moment. Normalized smooth bumps beta± in the two regions give signed means m±. Then

    dmu_(±,epsilon)=[(1-epsilon)beta±+epsilon]dmu0

is smooth, strictly positive and normalized. Its coefficient mean retains the sign of m± whenever

    0<epsilon<|m±|/(|m±|+|m0|).

This gives opposite signed averages despite finite normalization. Global full-support versions require a globally defined coefficient and reference measure with the stated moment; coefficient-dependent damping can ensure the moment if those data are supplied. These are added choices, not source-selected natural weights. The existing (g,y)-natural infinite-volume theorem is unchanged.

The lemma averages an **existing local coefficient**. It does not compute the metric variation of a new g-dependent weighted action, which would add weight/boundary terms. Neither a physical ghost nor an effective Einstein/Newton coefficient is inferred. LT-GR7 already treats an unfixed dimensional ruler as consistent with the source's ratio-only structure.

## 6. Source relevance and the bounded memory decision

| Source or mechanism | Supplied status | Consequence |
|---|---|---|
| SC-GEO-52, observation slice | ASSERTS the slice posture; local contraction owned | Does not supply a physical trajectory/state domain or fibre average. |
| SC-OP-04/05 | Source operator grammar and unresolved completion | The repaired candidate's regular symbol is one owned realization, not every source construction. |
| SC-CHI-01/51/52, SC-GEN-01/03/50 | Total/effective separation obligations; physical realization open | Neither theorem replaces these with repeated families or a mandatory Fredholm count. |
| SC-META-52 | UNCERTAIN; boundary-value posture, ultrahyperbolic problem explicitly unresolved | A global boundary law could change the free-data premises. None is selected here. |
| SC-META-53, SC-GEO-51 | Physical positivity unresolved; full U(64,64) asserted | Compact shielding alone does not give an evolution/projection tuple. |
| Extra finite weight/timelike reference | Mathematically constructible added data | Finite mass does not select a predictive law, signed response or physical norm. |
| Nonlocal/boundary completion | UNDETERMINED | Remains a substantive survivor, with existence/selection and response still to test. |

The analytic-germ results do not provide the fixed evolution space, generator domain, compatible idempotent projection and hidden propagator needed for a rigorous Mori–Zwanzig calculation. The literal rectangular q is not that projection. No source-selected tuple was found in the bounded audit. Writing the formal memory identity would add no established native dynamics, and hidden initial forcing would remain even if that tuple were supplied. The approved second-wave alternative was therefore used: the actual varying-cone completion discriminator above, accompanied by the finite-reduction selection test. No memory decay or Markov approximation is asserted from SC-CHI-52.

The actionable result is more precise than 'boundary conditions are missing': a successful completion must specify the law governing observed histories. A nonzero deterministic lift into this actual operator must leave at least one hypothesis of the excluded finite-local class; a predictive probability law is a different question. Finite normalization alone answers neither requirement. Interpretive analogies may suggest such constructions; they are not evidence that any particular construction exists.

## Verification and continuation

The exact probe checks full15-by15 Clifford operator columns (covering rank1920), two-sided non-null principal inverses, literal qJ=I, right inverses for observed temporal-jet diagonals, nonzero-shift/generic-covector cone relations, polynomial visible/invisible principal controls and nontrivial triangular lower blocks. Principal polynomial controls are not mislabeled as actual curved solutions; the latter are supplied by the written CK proof. The new finite algebra Lean core checks five statements without proof placeholders. Independent reviewers corrected the analytic reduced-coefficient requirement and real/complex rank and differentiable-decoder qualifications before acceptance.

No source, physics-ledger, class-C, canon, paper or scientific matrix verdict changes. This wave consumes the finite-local-lift and whole-history observation questions in their stated scopes. It preserves boundary/nonlocal/restricted-domain alternatives and all retained opportunities. Scheduled priorities and governance are unchanged; no new pause, approval checkpoint or stop rule is installed.
