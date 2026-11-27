# Independent first-jet source-census review

Basis `fc89c976e6c7cafcd4acb277370dfef4518ea9aa`. Internal T2 mathematical and hostile scope review, not external peer review or a Lean proof. The concrete source author and independent reviewer are distinct. Root integrated the required R projections and distinguished constant components from parallelness.

# Final hostile mathematical review: actual first-jet source census

Date: 2026-11-26. Review role: concrete independent mathematical reviewer, not a persona panel. Base revision: `fc89c976e6c7cafcd4acb277370dfef4518ea9aa`.

**Disposition: approve the bounded source-spanning and certified-receiver coverage result, with the two notation/explanation corrections already acknowledged by the lead. No native cokernel, candidate exclusion, full-R construction or physical result is approved.** Necessary-condition wording is sufficient throughout the owner report; no additional sufficiency theorem needs promotion.

## Reviewed inputs

- Scratch exact source probe SHA256: `a99dc05cc2fe5db239e7902150493cad8b8f0406a449ef38e653c8abfe827c7a`.
- Completed census SHA256: `0ae56b2e201eb4836c3951bf2442a10e24b5135525341cf65acf78a3cf440985`.
- Analytical spanning memo SHA256: `5c16534cfbf0b312988ce9be4f73ad10f65ca2bf94ae48153c6392b7d7235318`.
- Owner draft: `explorations/conditional-build/source-action-firstjet-source-census-2026-11-26.md` in the firstjet worktree, with final verification/continuation markers still pending during review.

I inspected the actual connection/Clifford lift, channel constructions, exact source records, receiver provenance and the analytical proof. I independently reconstructed all eight positive membership cases from their exact coordinates and verified disjoint receiver support for all sixteen negative cases. I also independently performed a tiny exact Gaussian-rational dependency reduction. I did not rerun the native geometry/source computation or any heavy inverse/closure job.

## 1. The strongest scope is correct when kept necessary-only

The source census concerns the ambient `Hom(R,N)` differentiated equation evaluated on the two Q7 input modules. It does not concern arbitrary R inputs, arbitrary higher jets, or the already-solved restricted `Hom(Q,N)` differentiated equation.

In an adapted homogeneous frame, the reduced derivative source is

    M Gamma_N,a Y_Q,b - L_b Gamma_R,a i_Q
      + principal-index connection combinations of L_c i_Q.

The first term is manifestly in range M, and the last terms have owned principal-source preimages. Thus `L_b Gamma_R,a i_Q` is the remaining necessary range question. Passing coverage in an invariant receiver with its certified inverse is sufficient to dispose of that particular source; failure of coverage is not failure of range membership.

There is no need to claim an unqualified iff about “first-jet compatibility.” If such a statement is retained elsewhere, its precise formulation must be: existence of a smooth extension Yhat of the known Y_Q to R such that the **ambient Hom(R,N) residual derivative**, evaluated on Q at p, vanishes. This differs from differentiating the restricted Hom(Q,N) residual, which already vanishes automatically. With `F=MYhat-L`, the exact identity is

    (nabla_a F_b)i_Q = -F_b B_a,
    B_a=(R-Pi_Q)nabla_a^R i_Q.

That yields the precisely defined first-order extension criterion in the earlier precheck. It does not yield a full-R right inverse. The draft's necessary-only language avoids this ambiguity and is mathematically sound.

## 2. Constant matrices and genuine connection content

The constancy of P/R uses preservation of the dt line. The constancy of M additionally uses the owned affine-natural background T and its full Lorentz invariance, hence constant T/J components in the transported adapted frame. Constancy of L uses the natural symbol tensor and simultaneous transport of its principal index. It does **not** assert covariant parallelness: the nonzero connection commutators are exactly the derivative terms being evaluated.

The lead should include that explanation explicitly; P constancy alone would not prove M constancy.

The native formula correctly uses `g.L[a] + isotropy(h'_a)` on ambient tangent space, then `-A^T` on the one-form leg and the full spin commutator on End. The metric-compatibility/Clifford-generator checks authenticate the lift. The 42 SO3 matrix-intertwining equations validate the connection-input representation, and the normal Nomizu/horizontal mixing identities match the written Koszul derivation.

In the canonical gauge only axes0,1,2,3,10,12,13 are nonzero. This gives input representation V0+2V1. Its tensorial meaning is the second fundamental map B; raw connection coefficients in arbitrary frames are not being declared tensorial. Residual SO3 gauge additions act inside Q and contribute only already-solved L(Q) sources. The normal V0/V2 vanishing and the no-output-below4 conclusion are therefore correctly scoped.

## 3. The representative construction is complete

The probe retains both connection V1 families and both intermediate spins6/7 separately. For each Q copy, real axis0 provides `raw=R Gamma_0 V`; exact checks give

    R Gamma_1 V = i raw,
    E raw = -W7,
    Pi7 raw = (1/14) F W7,

while `W6=Pi6 raw` is highest6 and the axis2 component W7 is highest7. These relations prevent the naive single-weight-component loss of the W7 channel.

The principal representatives correctly distinguish both V1 copies (axes0 and10) and the unique V2 copy. Axis5 isolates the needed highest spin4 or spin5 component from W6 or W7 after Casimir projection. For `V2 tensor W6 -> N5`, axis9 is the correct direct highest representative. Its exact axis5 relations

    E low = -2 source,
    F E low = -10 low,
    low=(1/5)F source

show that the earlier weight4 component was retained, not silently discarded.

Thus four spin4 and eighteen spin5 CG slots are exhausted. These are channel slots, not independent native vectors. Every concrete source is then checked for native P membership, K_dt annihilation, target Casimir, highest weight and raising annihilation.

**Notation correction:** the draft's intermediate definitions must explicitly include R, matching the code:

    W6^A=Pi6 R Gamma^A_-1 V,
    W7^A=Pi7 R Gamma^A_0 V,
    W7^0=R Gamma_3 V.

This does not change the reported sources: the omitted N part would be annihilated by `PK_bP=0`, with spin projectors commuting with P. It does fix their declared intermediate carrier and avoids an unnecessary proof mismatch. The lead has agreed to this correction.

## 4. Independently checked receiver results

The census contains24 exact cases:22 channel vectors and2 old pointwise controls. All24 are nonzero.

| Class | Inside | Outside |
|---|---:|---:|
| Spin4 channels | 2 | 2 |
| Spin5 channels | 4 | 14 |
| Pointwise Q controls | 2 | 0 |

I independently multiplied the stored exact receiver coordinates by the authenticated basis for all eight inside cases and recovered the complete source dictionaries exactly. For every outside case I checked that its entire source support is disjoint from the union of its receiver basis supports, that the recorded receiver coordinates are empty, and that its remainder witnesses equal the corresponding source coefficients. The receiver, inverse certificate, native spin4 probe and background hashes match the recorded bindings.

The earlier all-basis halfturn/conjugation test establishes that both receiver orbits are real-closed. Since the sources are pure highest4 or highest5, their membership in the corresponding full SO3 orbit is exactly the highest-weight membership tested here. Complete N6/N7 cannot absorb a pure spin4/5 source. Thus the outside results are genuine nonmembership in the advertised known receiver, rather than omitted conjugates or higher-spin mixing.

Matching or differing XOR-coset labels do not establish equality or independence. In particular the new horizontal spin4 sources share the reported coset labels with old sources while having disjoint receiver support. The exact coordinate checks, not the coset labels, establish the coverage result.

## 5. Independently checked quotient rank

A separate exact Gaussian-rational reduction of the sixteen uncovered source payloads gives:

- spin4 rank2;
- spin5 rank13;
- total rank15, with the spins separated by Casimir.

The displayed dependency is exact, coefficient by coefficient:

    source[16] = 3 * source[7].

Because the entire uncovered-source support is disjoint from the respective receiver support, these ordinary source ranks equal their ranks modulo those existing receivers. This does **not** compute the dimension of a new M-invariant closure or the number of required unknown physical quantities. The independent check completed in about0.018seconds and is recorded in `/private/tmp/gu-firstjet-independent-rank-check-20261126.json`.

## 6. Hostile overclaim checks

The evidence defeats the statement “the existing E4/E5 source receivers cover every generated first-jet low-spin source.” It does not defeat the W2 candidate, either stationary root, full native M-range membership, or GU.

In particular, an uncovered source might have a preimage supplied by another structural identity, by a known manifest M-range term, or by a new small receiver. Nonmembership in E4/E5 does not prove a new inversion is mandatory. Existing inverse restrictions simply cannot be applied directly to those outside sources.

The report should retain the first-order/along-Q scope, all root and source bridges, and the separation of new source channels from actual independent quotient directions. The no-spin-below4 result applies only to this LC-plus-algebraic-J first-jet family; it cannot be transferred to a different derivative split or repeated derivatives.

## Final acceptance

Approve the current source-spanning, reality-closure, exact coverage and15-dimensional uncovered-quotient results. No new inverse or cokernel claim is supported. The agreed R insertions and constant-component explanation should be made before final gates. Final integration should preserve the hardened native dependency bindings and replay the same exact source/membership payloads, rather than relying on unbound scratch code. No additional heavy run is requested by this review.


## Source relevance and quick20 reassessment

# Post-census selection and Nov26g proposal assessment

**Established:** the complete generated first-jet census has4 spin4 and18 spin5 channels. Two spin4 and four spin5 channels lie in the certified receivers; the two old controls also pass. **Ruled out:** those receivers cover every generated source. **Undetermined:** solvability of the remaining2+14 channels, full-R compatibility and every physical/GU consequence. Exact dependence reduces the16 uncovered channels to15 directions: spin4 rank2 and spin5 rank13; case16=3 case7. Coordinate-support separation is not a cokernel obstruction.

**Next scientific discriminator:** exact source compression is now consumed. If a concrete bounded intertwiner is supplied, test its full-carrier source and M-intertwining identities against the certified receiver before constructing an inverse; success transfers only the stated certificate, failure rejects only that shortcut. Otherwise attempt one actual-root adjoint-cokernel/range test on a small independent reached source—the56-term normal-connection/horizontal-principal spin5 source is the sparsest exposed seed, although support size alone does not predict module size. Grow only a receiver justified by that actual test. A nonzero pairing with a true full-carrier adjoint kernel excludes the stated candidate realization; successful range membership consumes that source; inability to find a kernel proves neither. Do not pre-allocate16 inverses or all lower-spin blocks. This is W2/K95 candidate science; source necessity and physical admission remain unproved.

## Nov26g proposals: rank by expected time saved

Qualitative ranking; no timing or success probabilities were measured. **All new counterfactual suites below remain proposals, not executed or authorized tests.**

| Rank | Proposal | Expected benefit and limit |
|---|---|---|
| 1 | Outcome→action / value-of-information table | Very low preparation cost. Defer only if no outcome changes claim status/scope, a scientific decision, a reusable constraint or the next action. A bound/certificate can be valuable with the same successor. Proposed lightweight field, not a new stop gate. |
| 2 | Success requirements, with premise typing | Cheap filter against large irrelevant constructions. Require an empirically acceptable weak-field regime and physical stability only at an explicitly defined observable/domain. Connection to *these* roots or the selected zero-matter branch is a repository assumption unless separately required; do not promote it to GU necessity. |
| 3 | Matched known-theory pipeline controls | Potentially high savings before a physical-ghost inference. Start with one diagnostic whose pass/fail would change that inference. GR's conformal direction is not a physical ghost after constraints; specify the actual Stelle action/signs; conformal gravity needs boundary/domain qualifications. Ordinary Dirac tests its correctly typed fermion observable. A detached benchmark suite would save little. |
| 4 | Targeted choice sensitivity | Change only the load-bearing family for one pending verdict, with all dependent structures transported consistently. A10-family×4-verdict grid is costly and mixes conditional constructions. Plus/reversion is a comparator, not a source-permitted alternative to the authenticated minus/conjugation adjoint; its flip diagnoses build dependence only. |
| 5 | Same-content4D comparator | Useful only for one matched obstruction: persistence flags generic mechanism/pipeline dependence; disappearance identifies dependence on the removed construction. Neither outcome is GU evidence. Define the actual reduction/deletion map first. |
| 6 | Euclidean-base counterfactual | Can locate signature dependence, but changes fibre geometry, real form and the meaning of time/energy. A persistent raw negative direction does not answer the Lorentzian physical-ghost question. No silent retention of K95 data. |
| 7 | Base2/Y5 and base3/Y9 toys | Highest setup risk for little immediate decision value: dimension changes Clifford type, grading, Hodge/vertex typing and representation multiplicities. Useful only after an identified dimension-stable mechanism and an outcome that changes the14D plan. Independent toy results do not transfer automatically. |

### Four queued questions: outcomes → actions

- **Weak response:** admitted normalized physical response nonzero → test the stated source/observable bound; zero → close that channel only. No common admitted domain/readout → defer this *physical inference*, while continuing the finite candidate work. The existing local-Q nonzero functional is already banked.
- **Path continuation:** proved connection → use it only for a named shared-boundary/branch theorem; proved disconnection → exclude only that continuation route. Defer only if neither outcome changes claim status/scope, a scientific decision, a reusable constraint or the next action; the same successor alone is insufficient. GU success does not require classical continuation to our two stationary roots.
- **Spin4/spin5 compatibility:** true nonzero adjoint-kernel pairing → scoped candidate exclusion; certified solve → consume that source and rerank; no certificate → unresolved. The current support census has not selected either outcome.
- **BRST:** an actual action/domain-compatible differential fails nilpotency or its claimed quotient property → reject that completion; succeeds → use precisely the proved quotient. With no supplied physical differential/domain, constructing one is not a short discriminator. Algebraic BRST success alone is not positivity or GU consistency.

No new choice family, source-claim verdict or governance change is proposed. Strongest source-level alternative remains a genuinely admitted low-curvature/readout test; the census supplies none of its missing physical data.

## Quick20 mathematical-description pass (retained, not20 agents)

1 Linear algebra: exact compression is consumed at rank15; test certified relations before enlarging a receiver. 2 Representation theory: census4/18 is complete at its declared input scope. 3 Clifford algebra: preserve native products and adjoint. 4 Differential geometry: horizontal/normal vector families remain distinct. 5 Constraint PDE: first-jet range is necessary, not full dynamics. 6 Functional analysis: support outside a finite receiver is not outside the full range. 7 Symplectic geometry: no physical radical supplied. 8 Gauge theory: test actual constraints before interpreting negative modes. 9 Category theory: a comparator must preserve the relevant maps/structures before transfer. 10 Number theory: exact Gaussian-rational dependence and certified root arithmetic replace numerical ranks. 11 Algebraic geometry: distinguish two root loci from the59-parameter family. 12 Topology: no boundary receiver is supplied by a local solve. 13 Index theory: no family count follows. 14 Anomaly theory: prior applicability audit remains consumed. 15 Variational calculus: local first variation is not a physical energy instability. 16 Perturbation theory: uncovered jets cannot be repaired by repeating contracted identities. 17 Harmonic analysis: base bandwidth does not constrain normal frequencies. 18 Probability/measure: no new physical norm is selected. 19 Observability: physical readout remains separate from coefficient nonzero. 20 Decision theory: prefer a result that changes claim/scope, scientific decision, reusable constraint or action; the completed compression informs bounded intertwiner/dual tests before inverse construction.

Evidence read: `/private/tmp/gu-firstjet-cache-20261126/firstjet-census.json`; current owned source/assumption/physics-ledger review preserved in `/private/tmp/gu-spin4-rerank-20261126.md`. No new suite or heavy job executed.


## Publication interpretation

Only the bounded candidate result is accepted at T2. All Nov26(g) counterfactual suites remain proposals. The source census and rank compression are consumed; no source/physics/class-C verdict or policy moves. No prior inverse is extended by similarity unless the exact full-carrier intertwining hypotheses are proved.
