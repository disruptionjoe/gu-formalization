---
title: Actual first-jet source census and certified-receiver coverage
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T2
expected_delta: Exhaust the actual low-spin generated source channels and decide membership in existing
  certified receivers before any new inverse
actual_delta: The actual connection reduces the two-Q7 first-jet source question to4 spin4 and18 spin5
  channels. Existing certified receivers cover6/22;16 remain outside their support. This is a coverage
  result, not an obstruction or GU falsification.
class_covered: Held W2/K95 candidate, its two owned Q7 modules, canonical time-adapted LC connection and
  all principal slots at the two certified kappa1 roots; not arbitrary R inputs or class C
premises:
- "source-normal-tensor-class-2026-11-26.md sections6.1\u20136.7: two Q7 modules, affine frame and full-R\
  \ connection question"
- 'source-action-weak-response-2026-11-26.md: E5 and complete N6/N7 certificates'
- 'source-action-spin4-compatibility-2026-11-26.md: E4 all59-family invariant receiver and both-root inverse'
- 'source-adjoint-spinless-placement-2026-11-26.md: primary-minus versus plus-comparator correction'
source_bridge:
  status: conditional
  reason: First-order extension along Q is a necessary condition for the unrestricted auxiliary lift in
    this repository-built candidate; neither the W2 action nor full-R elimination is source-required.
kill_condition: Only a true native adjoint-cokernel pairing inconsistent with an actual root excludes
  this realization. Nonmembership in E4/E5 is not nonmembership in image M.
---

# Actual first-jet source census

program_target: LB-CLASS
tier: T2
expected_delta: Complete the generated low-spin source census and test existing receiver coverage
actual_delta: The actual connection reduces the two-Q7 first-jet source question to4 spin4 and18 spin5 channels. Existing certified receivers cover6/22;16 remain outside their support. This is a coverage result, not an obstruction or GU falsification.

```gu-typed-objects
result: actual first-jet source spanning and receiver coverage
carrier: W2 K95 endomorphism-valued one-forms with N=ker K_dt and two Q7 modules LAYER=ambient BRIDGE=held-candidate-equations CHIRALITY=S-FULL-DIRAC
pairing: native nondegenerate indefinite form defining P and the actual auxiliary compression ON=declared_carrier
real_structure: W2 Clifford conjugation; halfturn-conjugation proves receiver reality closure, not physical positivity
grading: imaginary Clifford degrees0,3 mod4; SO3 spin labels are representation bookkeeping, not physical particle spins or family counts
action_owner: repository-construction source-action W2 with both certified kappa1 root boxes
target: actual connection-generated source map into N modulo certified receivers MAP-TYPE=homomorphism
```

## Scope and result

Basis: fetched clean `fc89c976e6c7cafcd4acb277370dfef4518ea9aa`. The directed falsification task tests an uncovered necessary condition using existing exact inverses. Its breadth is all generated first-jet low-spin channels from the two owned Q7 modules; source relevance remains conditional. The physical weak-readout alternative still lacks an authenticated common domain/quotient, normalization and propagation. The present finite calculation neither waits for nor supplies them.

| Source family | Reduced channel slots | Inside existing certified receiver | Outside |
|---|---:|---:|---:|
| Spin4 | 4 | 2 normal-boost | 2 horizontal Nomizu |
| Spin5 | 18 | 4 | 14 |
| Old pointwise Q controls | 2 | 2 | 0 |

All22 new channel vectors are nonzero. The16 uncovered vectors have their **entire coordinate support** outside the respective E4/E5 receiver support. This shows that those certificates cannot settle them. It does not prove they lack preimages in the full native auxiliary map. The6 covered channels have preimages throughout both owned root boxes by the already certified restrictions. Complete N6/N7 cover higher-spin outputs. No first-jet source generated here has spin below4.

Exact dependence reduction compresses the16 uncovered channel vectors to15 independent directions: spin4 rank2 and spin5 rank13. Certificate case16 is exactly3 times case7. This compression does not change their range status.

E4 has highest-weight dimension282, E5 has120. Halfturn-conjugation maps every one of those402 basis vectors back into its own receiver. Thus the test includes the real SO3 orbits; it did not create false nonmembers by forgetting conjugates.

This is first-order extension **along Q**, not a full-R, higher-jet, nonlinear, propagated-state or physical-energy theorem. K77 versus derived K95, total versus physical grading, source2+1, imposter gamma-trace placement, independent fields and observation by contraction remain distinct. The source minus/conjugation correction stands; sharing that sign does not identify W2 as the source action. Two kappa1 stationary roots are already certified; connection to the small-h branch remains unproved and was not assumed.

## Analytical source-spanning argument

### 1. Objects and claim

Use the actual K95 homogeneous metric-bundle LC connection B and the already owned split `H = K^b nabla_b + J`, `J=I+2N(T,.)`. T remains in J; replacing nabla by a B+T connection would require redoing the split and cannot inherit the raw connection statement below. The two homogeneous roots change M, not the geometric LC/source-spanning argument.

At p, N is the nondegenerate kernel of K_dt, P its native orthogonal projector, R=1-P. Q is the transported sum of the two real SO3 spin7 modules generated by V_5=K_dt b5 and V_12=K_dt b12, with its native nondegenerate orthogonal projector Pi_Q. The actual ambient connection carrier W and its N/R summands have no geometric rotation spin above7. These are the owned facts in `source-normal-tensor-class-2026-11-26.md` §§6.1–6.7 and the complete high-spin certificates.

**Claim proved below:** in the canonical time-adapted frame, the connection input has only one scalar component and two vector components. Consequently the first-jet cokernel sources generated from either Q7 have no output spin below4. Up to SO3 orbit and realification, spin4 needs two reduced representatives per Q7; spin5 needs nine per Q7. These are the *CG channel slots before coefficient identities*, not a claim that all resulting native vectors are nonzero or linearly independent. The native maps can identify or kill channels.

### 2. Exact time-adapting gauge derivative

Let tau=(0,0,0,1), eta=diag(1,1,1,-1), S eta-selfadjoint, g(S)=exp(S), and write

`u(S)=tau g(S)=(v^T,u3)`, `lambda=sqrt(u3^2-v^T v)>0`.

An explicit analytic, SO3-equivariant, rotation-free Lorentz matrix near S=0 is

```
h(S) = [ I + v v^T/(lambda (u3+lambda))    -v/lambda ]
       [             -v^T/lambda          u3/lambda ] .
```

Direct multiplication gives `u h=lambda tau`; h preserves eta, h(0)=I, and spatial rotations conjugate this expression naturally. Thus A(S)=g(S)h(S) lies in the time-line-preserving affine subgroup used to transport Q. No global gauge assertion is needed.

At zero,

`lambda'=S33`,
`h'_(i3)=h'_(3i)=-S_(3i)` for i=0,1,2,

and every other component of h' vanishes. The native vertical basis is precisely S=A_a in `source_action_deep_geometry.py`, whose tangent variation is U=-2 eta S. Therefore:

- normal axes4,7 have only lapse derivatives; no Lorentz rotation/boost;
- normal axes5,6,8,9,11 (spatial symmetric traceless V2) have h'=0;
- normal axes10,12,13 have h'=H03,H13,H23, respectively, in the displayed active frame convention.

A passive frame convention reverses all these gauge signs consistently and does not change the source span. The exact probe uses this active convention consistently.

The original homogeneous-frame normal LC matrix is zero. For vertical A and horizontal v,w, the only potentially nonzero Koszul term is proportional to `<Av,w>_eta - <v,Aw>_eta`, which vanishes by eta-selfadjointness. Other normal-first-index components vanish by bracket type. This proves all Lambda_A=0 directly from the owned Nomizu formula, rather than inferring it from one trace-normal check.

For horizontal x, Lambda_x is generally nonzero:

`Lambda_x A = -A x`,
`<Lambda_x v,A>_N = <A x,v>_eta`.

It mixes H and N and is not the isotropy boost. The horizontal time input is a scalar under SO3, and horizontal spatial inputs form V1. The adapted correction contributes the separate normal time-space V1. Thus the only nonzero connection-input representations at p are

`V0(H_time) + V1(H_spatial) + V1(N_timespace)`.

### 3. Induced connections and the frame-independent quotient

The native tangent representation under SO3 is

`T_pY = 3 V0 + 2 V1 + V2`:

- H_time: V0;
- H_spatial: V1;
- N_scalar: 2 V0;
- N_timespace: V1;
- N_spatial-traceless: V2.

Let rho_W be the full induced action on the one-form/End carrier: it includes the one-form leg and the Clifford/End leg. The actual point connection is

`Gamma_a = rho_W(Lambda_a + h'_a)`

in the chosen active convention. Do not use only the spinor commutator. Since K_dt depends on the time line and A preserves that line, P/R have constant matrices in this adapted frame. Q was defined by A transport, so Pi_Q also has a constant matrix there. Consequently

`Gamma_N,a = P Gamma_a P`, `Gamma_R,a = R Gamma_a R`.

For Q the invariant object is the second fundamental map

`B_a=(R-Pi_Q) nabla^R_a i_Q`,

which in this frame is `(R-Pi_Q) Gamma_a i_Q`. It is a tensor. Raw connection coefficients alone are not. Replacing the time-adapted frame by another such frame changes it through an SO3 gauge; its inhomogeneous derivative acts inside Q because Q is an SO3 module. It therefore drops out of B. The corresponding extra `L_b i_Q Gamma_Q,a` is already in the owned pointwise source range. In particular it has no spin4 part. This prevents frame artifacts from being mistaken for a new normal-spin2 source.

All14 principal covector components decompose as 3V0+2V1+V2 as above. `P K_dt=0` removes one scalar component, but this is not needed for the low-spin bound. The two V1 principal families (horizontal spatial, normal time-space) must remain distinct. The V2 principal family has multiplicity one.

### 4. Differentiated auxiliary equation and what is being spanned

M, P and the natural principal L^b=P K^b R have constant matrices in the adapted homogeneous frame. Constancy of J uses the owned affine-natural T and Lorentz invariance, not covariant parallelness; constancy of P alone would not establish it. For a putative full-R lift `M Y^b=L^b`, differentiating covariantly gives the necessary equation

`M nabla_a Y^b = nabla_a L^b - (nabla_a M)Y^b`.

Using the induced connections, the right side becomes, up to the chosen upper/lower covector-index sign,

`M Gamma_N,a Y^b - L^b Gamma_R,a + Gamma^b_ac L^c`.

Thus, after manifest M-range terms and the already owned `L^c Q` sources are removed, the only new cokernel source is

`S_ab(v) = L^b Gamma_R,a v`, `v in Q`,

or equivalently `L^b B_a v` modulo the already covered Q-internal term. The covector-index connection term may mix slots but is a linear combination of actual L^c v, already covered by E5 and complete N6/N7. It is not dropped from the equation; it is disposed of by certified range membership. Density/frame terms in a later weak-adjoint calculation are separate and are not implicitly omitted there.

The derivative is taken in the ambient Hom(R,N) equation and then evaluated on Q. It is not merely the Hom(Q,N) derivative of the already solved restricted equation, which vanishes automatically. This identifies a necessary range condition for extension; covariance does not supply a right inverse. The explicit native range solve is still required.

For either Q7 module, a scalar connection input produces only spin7. Either vector input produces spins6,7,8 by CG, and ambient spin8 is absent. Every principal covector has spin at most2. Hence S_ab has spin at least4. The first term `M Gamma_N,a Y^b` likewise has no output below4 for the chosen equivariant pointwise responses (Y^b Q has spins5–7), while M preserves each spin. The covector-index term has spin at least5. The new low-spin decision is therefore exhausted by spins4 and5. This statement covers this generated first-jet family, not arbitrary R inputs, higher jets or nonlinear equations.

### 5. Reduced representatives: construct intermediates first

Use complex spherical tensor components and a highest vector v7 of each input Q7. Let A=H,N distinguish the horizontal-spatial and normal-boost connection vector families. Define

`W6^A = Pi_6 R Gamma^A_{-1} v7`,
`W7^A = Pi_7 R Gamma^A_0 v7`,
`W7^0 = R Gamma_(H_time) v7`.

Every Wj is highest of spin j. A zero Wj certifies that *that particular reduced connection map* is zero: by CG, Hom(V1 tensor V7,V6) and Hom(V1 tensor V7,V7) each have dimension one. It does not eliminate the other input family or the other intermediate spin.

There is no need to assume that the same highest-input/lowest-operator component covers all channels. It does not. Distinct components Gamma_-1 and Gamma_0 isolate the two intermediate channels. Once these highest intermediates are formed, their lowered vectors are generated by the actual SO3 lowering operator. This reconstructs the entire image of the corresponding tensor map; explicit lowered-Q input calculations give the same map by equivariance. If the implementation bypasses these intermediate projections, it must instead include lowered Q inputs and resolve the two coupled channels; one raw coefficient is insufficient.

Why these individual component tests cannot miss a nonzero reduced map: for coupling spin s with a highest spin-j vector, the coefficient of the highest output J=j+q in `T_q v_j` is nonzero whenever the triangle conditions hold. The extremal Clebsch–Gordan factorial sum has a single surviving term, so no cancellation is possible. Our selections are (s,j,J,q)=(1,7,6,-1), (1,7,7,0), (2,6,4,-2), (1,6,5,-1), (2,6,5,-1), and (2,7,5,-2), all admissible. Normalization changes only a nonzero scalar and cannot change zero/range membership.

### 6. Complete low-spin channel table

Write K_H^(1), K_N^(1), K^(2) for the two vector and unique rank2 principal families, always followed by P. Apply the output Casimir projection in each formula.

#### Spin4: two representatives per input Q7

For A=H,N:

`S4^A = Pi_4 P K^(2)_{-2} W6^A`.

Only intermediate6 with principal rank2 can reach4. Each composition has one CG channel. Thus the two Q7 copies require up to four reduced vectors. The two existing normal-boost vectors are S4^N; the horizontal Nomizu vectors S4^H are genuinely separate until coefficients prove otherwise.

#### Spin5: nine representatives per input Q7

For each A=H,N, retain all four:

1. `Pi_5 P K_H^(1)_{-1} W6^A`;
2. `Pi_5 P K_N^(1)_{-1} W6^A`;
3. `Pi_5 P K^(2)_{-1} W6^A`;
4. `Pi_5 P K^(2)_{-2} W7^A`.

Add the scalar-connection channel:

5. `Pi_5 P K^(2)_{-2} W7^0` (one total, not one per A).

This is 2*(2+1+1)+1=9 per Q7, at most18 total. Rank0 principal inputs cannot take6 or7 to5. Rank1 principal inputs reach5 only from6, and there are two distinct such principal families. Rank2 reaches5 from6 and7, each with multiplicity one. A scalar connection input reaches only7, giving its one rank2 channel. Normal scalar connection inputs are zero. This exhausts the low-spin tensor product channels of the actual connection family.

These are not necessarily18 independent native vectors. Membership in E5, zero identities and exact dependence can reduce them. The exact census below reduces these representatives in the certified E5 orbit; the nonzero remainders identify uncovered receiver questions. Complete N6/N7 handle the remaining outputs without new inverses.

### 7. Concrete spherical directions in the owned basis

With the current raising convention `rho(H02)+i rho(H12)`, spatial e0+i e1 is highest. Up to nonzero common factors:

- vector q=-1: e0-i e1; vector q=0: e2;
- normal boost vector q=-1: axis10-i axis12; q=0: axis13;
- normal rank2 q=-2: axis5-i axis8;
- normal rank2 q=-1: axis9-i axis11.

The scalar connection is horizontal axis3. For the horizontal vector connection, use Lambda_0-i Lambda_1 and Lambda_2 on the full carrier; for the normal vector use H03-i H13 and H23. Both R projections and the intermediate spin projectors remain required. Adapt signs if the native implementation's spherical convention differs, and check raising annihilation exactly; do not copy these expressions across a reversed active/passive convention.

The existing source normal-axis5 spin4 vector is proportional to the q=-2 choice after output projection, because its conjugate-weight component cannot reach highest4 from highest6. For the spin5 rank2 channel, a direct highest representative uses q=-1, hence axes9/11. There is also a convenient equivalent native implementation: retain `Pi_5 P K^5 W6`, which has weight4, and apply the raising operator E once. The extremal-input CG coefficient `<2,-2;6,6|5,4>` is nonzero, so this cannot miss a nonzero reduced channel. In the native E=J02+iJ12, F=J02-iJ12 convention, verify `F E=-10` on this spin5 weight4 vector; then its original vector is `-(1/10) F(E vector)`. One can therefore reuse axis5 with one exact raising check, but simply discarding its non-highest spin5 piece would miss the channel. This is the main coverage seam hidden by checking only the earlier highest4 source.


## Exact computation and reproducibility

The probe builds the actual Nomizu and adapted-gauge matrices, acts on both the one-form and Clifford/End legs, and reconstructs every source with exact Gaussian-rational coefficients. It checks all normal Nomizu components vanish, the horizontal mixing formulas,42 connection-equivariance equations, all tangent Casimirs, metric compatibility and Clifford generators. For every intermediate/output it verifies the weight, raising equation, Casimir, native P membership and K_dt kernel equation. The rank2 W6-to-spin5 channel uses axis9 with the exact axis5 ladder relations; it is not discarded because its axis5 expression has weight4.

Receiver bases and both-root inverse certificates are byte-authenticated against published bundles. Every source and its exact receiver coordinates or nonmembership witness is retained in the [certificate](../../lab/process/source-action-firstjet-source-census-certificates.json). The [evidence](../../lab/process/source-action-firstjet-source-census.json) records summaries, review and current bindings. No numerical solve or new inverse enters this census.

From the repository root, unpack the existing data-only bundles into a local cache, then reconstruct the census. Heavy jobs run serially with one BLAS thread.

```sh
python tests/program-focus/source_action_spin4_compatibility_probe.py --repo . --cache _local/firstjet-census/e4 --mode unpack
python tests/program-focus/source_action_weak_response_probe.py --repo . --cache _local/firstjet-census/e5 --unpack
python tests/program-focus/source_action_firstjet_source_census_probe.py --repo . --cache _local/firstjet-census --mode census
python tests/program-focus/source_action_firstjet_source_census_probe.py --repo . --cache _local/firstjet-census --mode replay --evidence lab/process/source-action-firstjet-source-census-certificates.json
python tests/program-focus/source_action_firstjet_source_census_probe.py --repo . --cache _local/firstjet-census --mode status
```

`replay` independently reconstructs every source, exact membership/dependence and geometry/reality record and compares the native dependency hashes. `--limit N` supports bounded discovery batches; an incomplete batch is never complete evidence. `controls` checks the geometry and receiver provenance without a source census. The tool reuses authenticated receivers without recomputing their inverses.

Installed exact replay passed in 31.67s, all24 source records, geometry/reality, quotient relations and native bindings identical. No inverse regenerated. Dedicated controls/status entrypoints also pass. These timings describe the finite census, not the whole research workflow.

## Three-state assessment

- **ESTABLISHED:** the complete generated low-spin channel count, six covered channels, sixteen uncovered channels and real-orbit receiver closure.
- **RULED OUT:** none of GU, class C, the candidate, either root or full native source solvability is ruled out by this census. Existing receiver coverage is incomplete.
- **NOT MODELED / UNDETERMINED:** range membership of the remaining source quotient; full-R and higher-jet compatibility; physical admission, quotient, normalization and propagation; source necessity of the reconstruction.

Independent T2 review accepted the bounded spanning and coverage claim after checking all8 positive membership reconstructions, all16 disjoint-support nonmembers, the rank2+13 reduction and the exact dependency. The review required explicit R projections and the constant-component/parallelness distinction above. [Review record](../../lab/process/hostile-reviews/2026-11-26-source-action-firstjet-source-census-review.md). This is internal mathematical review, not external peer review or a new Lean certificate.

## Follow-through and selection

The census and dependency reduction are consumed. The next ready question is the exact15-dimensional uncovered source quotient, starting with its sparse56-term spin5 source. A genuine full-native adjoint-kernel pairing would be a candidate obstruction; a certified preimage would consume that source. A supplied intertwiner may reuse an existing inverse only after exact kernel preservation, injectivity, all59-map identities on the complete receiver, and source membership. No such intertwiner is currently owned. Similar XOR labels, parity or volume multiplication alone supply none of these identities. A failed trial map is only a failed shortcut. No automatic15-inverse backlog is created.

The20 mathematical descriptions, including category theory and number theory, are a quick reassessment, not20 independent experts. Concrete source derivation and independent review are identified separately. No new physical choice family was introduced. Candidate bookkeeping remains10 grouped choices/4 obligation bundles/net6/zero source-selected predictions, not a lower bound for GU. Scientific matrix cells, intersections, shrinkage, class-C width status, source/physics/canon verdicts and papers are unchanged. Directed counter70to71/LB-CLASS29to30 records this result without a scientific verdict.

## Counterfactual proposal boundary

Joe's Nov26(g) memo remains a proposal. This wave completes the previously authorized source census; it does not execute the proposed choice-family sweep, GR/Stelle/conformal/Dirac controls, toy dimensions, Euclidean base or no-observerse counterfactual. Proposed prioritization is recorded with its reasons and outcome-to-action distinctions in the evidence. `program_focus`, ordinary schedules and review rules are unchanged.
