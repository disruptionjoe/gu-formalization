# Independent mathematical and source-scope review

Basis 3e8fa792e93e8a58e804364c842080a7e6c72810. Internal T2 review, not external peer review or Lean certification. Independent reviewer checked the exact arithmetic/proof/parser and final machine evidence; root integrated corrections. Concrete author of the optimized arithmetic is not its independent reviewer.


## Arithmetic, covariance and replay boundaries

# Follow-up review: native integer P, fused 2PN and covariance diagnostic

Read-only review dated 2026-11-26. Inputs: scratch integer projection and proof at hashes in its control record; uncommitted integration in `/private/tmp/gu-spin4-wt-20261126/tests/program-focus/source_action_spin4_compatibility_probe.py`; root0/source5 numerical trial. No heavy computation or owner write performed.

## Accepted arithmetic derivation

Native P on each paired-time XOR block is `Z Ginv Z^T W`, using the owned native real bilinear pairing weights. The implementation constructs `B=Z^T W`, clears three independent positive rational denominators, applies `Bi`, `Gi`, `Zi` in that order to Gaussian integer pairs, and divides by their product and the input denominator. This exactly reconstructs P. There is no omitted Gram factor, conjugation, signature sign, or cross-block sum. The grouping `(e XOR c)&~8` and its 28 keys match the owned implementation. Distinct block supports are disjoint. The per-factor reconstruction assertions are sufficient for every input in a generated block; the finite controls are supplementary.

The standalone 190-control artifact's projection, integer-engine and native paired-probe hashes match the files I read. I did not rerun those native controls.

The fused closure call is correct:

    integer cubic numerator = 6 Dphi du dv * N(T,b),
    P(numerator / (3 Dphi du dv)) = 2 P N(T,b).

The three numerator summands share their denominator because `L*Dadj=Dphi`; bilinearity contributes both input denominators. Thus the integrated use of `ip.apply_integer(numerator,3*E.Dphi*du*dv)` has the right factor of two. Identity is added later in `M=Id+sum_j x_j A_j`; it must not be added in these A_j closure columns.

The prepared-input cache retains the original dictionary reference, preventing object-ID reuse. The actual closure loop never mutates Ts or bb after preparation; reduction rebinds its working vector using `add`, rather than mutating a cached input. This use is sound. Mutating a prepared dictionary later would violate the documented API and silently stale its cached numerator/adjoint, so that invariant should remain explicit.

## Replay/parser observations

1. `integer_binding` deliberately distinguishes v2, projection, engine, closure procedure, basis, background and native input hashes. Existing v1 checkpoints remain separate. That is correct. Resumed output requires matching bindings and matching completed/column counts.
2. The standalone projection-control record binds only three files. A complete receiver certificate must additionally bind native geometry, algebra and symbol machinery; the integrated `w.native_bindings` currently supplies those. Do not promote the standalone three-file record as sufficient receiver provenance.
3. The integrated closure binding does not directly hash the `context`/`load` functions or the weak-response probe file that supplies `build_seed_context`; the stored `engine_controls.bindings.native_weak_probe_sha256` does record the latter. Current arithmetic is not thereby invalid. For robust replay, the final certificate should verify that stored weak-probe hash plus the source reconstruction/geometry context, or add explicit relevant function/file hashes without pretending old checkpoints had them.
4. The closure reader assumes recorded basis coordinate keys/pivots are unique and the basis is normalized in echelon order. Native stage_basis constructs them that way. Final certification should validate dimensions, pivot count/uniqueness/normalization, exact source reduction, and basis independence/membership, rather than trusting descriptive metadata.
5. Sparse integer columns have shape `[receiver_row, real_string, imag_string]`, grouped by input basis column and then 59 backgrounds. The inverse parser must reject duplicate/out-of-range row indices and wrong counts, initialize omitted entries to exact zero, and retain the 2PN convention. Do not parse them as the old dense rows or silently zip-truncate.
6. The normal `--mode certify` path currently reads the old dense closure filename and calls the old dense parser. The new sparse-v2 certificate must have its own validated reader or an explicitly verified conversion; merely renaming the sparse file is incorrect.
7. Native exact coefficient readers presently accept anything `Fraction` can parse, including floats. The actual basis/background payload uses exact rational strings/integers. Preserve this boundary; inverse candidate floats may be rationalized deliberately, while finite precision discovery payload must not silently become an authenticated basis/source.

These are narrow provenance and parser conditions, not evidence that the current exact column images are wrong.

## Covariance trial reading

Only root0 and source basis index5 were requested and completed. `complete:true` refers to that selected case; it does not mean both roots and sources were tested.

- Old coordinate residual: `4.16e-16`.
- Old full-native response residual: `4.19e-16`.
- Trial spin4 and native-kernel errors: `6.62e-15`, `2.25e-16`.
- Trial residual weighted norm: `22.7003` against source norm `1072.1295`.
- Relative residual: `0.0211731`.

This is a clear numerical failure of `x4=Pi4 P rho(H03)Y5` as that case's preimage, at the exploratory precision and pruning used. It is not an exact root-ball exclusion, not an adjoint cokernel witness, and not evidence that another preimage fails. The residual is not a physical norm. Raw trial/residual payload supports (6233/6663 positions) contain floating cancellation dust; they are not exact support certificates.

## Countermodel scope and integrated control

The generic `Sym^2(H*) + H*` countermodel remains valid under the stated structural premises. It does not identify its carrier, symbol or J with W2/K95, and does not kill a candidate or source claim. It disproves only the implication from covariance/reciprocity/PKP=0/old source solvability to all new fixed-P boost sources being solvable.

The old sources being zero in its smallest 14-dimensional version is not essential. Take its direct sum with an identical symbol carrier with `J'=Id`. In the first summand choose `V=(0,tau)` as before; in the second choose `W=(0,e1)`. The old b=e1 source in the second summand is `e1 tensor e1`, nonzero and solved by itself. All old sources lie in the second summand's invertible N. The first summand's new source still pairs to1 with its adjoint kernel, so the obstruction survives. This gives a 28-dimensional nonzero-old-source variant.

The algebraic `J=Id+2N(T,.)` form can also be realized generically without changing the countermodel. Set `T=(g,0)` and

    N((S,v),(U,w)) = (-(1/24) g tr_g(S) tr_g(U),0).

Then `J(S,v)=(S-(1/3)g tr_g(S),v)`, and `<N(X,Y),Z>=-(1/24)tr(X)tr(Y)tr(Z)` is fully symmetric and Lorentz invariant. This is an auxiliary generic cubic construction, not the native W2 cubic, a stationary-background assertion or a source action.

A standalone exact function suitable for copying into integrated `--controls` is saved at `/private/tmp/gu-spin4-covariance-controls-function-20261126.py`. It has local names, uses only `Fraction`, performs the same 2856 finite premise checks plus the nonzero-source direct-sum controls, and returns a scoped dictionary. Syntax was checked; no new heavy/native run was performed for this follow-up.


## Independent Neumann and draft review

# Independent mathematical review: reached-spin4 Neumann certificate and draft

Review date: 2026-11-26. Reviewed the pending draft in `/private/tmp/gu-spin4-wt-20261126` and `/private/tmp/gu-spin4-fast-neumann-20261126.py`. This review concerns formulas, representation types and the verifier path; actual 282-dimensional run bounds and complete validation evidence were still pending when written. No heavy job or owner edit was performed.

## Mathematical verdict, pending actual certificate numbers

The Neumann norm, affine root-box perturbation bound and reported source-error formula are correct. Sparse affine assembly has the correct input-column/output-row orientation, uses the 2PN columns, and adds identity exactly once. The generic covariance countermodel remains valid after a notation correction explained below. No mathematical defect was found in these formulas.

This is not yet acceptance of numerical bounds, a completed receiver certificate, or the final report: the lead still needs the completed exact closure, native basis/source validation and both passing root records.

## 1. Norm and invertibility proof

Define the scalar computational norm `|a+ib|_1=|a|+|b|`, vector norm `||v||=max_i |v_i|_1`, and matrix bound `||C||=max_i sum_j |C_ij|_1`. The scalar norm is submultiplicative, hence these matrix bounds dominate operator norms and are submultiplicative. This requires no positive physical pairing.

Let `M(x)=I+sum_k x_k A_k`, with real coordinates `|x_k-x0_k|<=r`. Let B be any exact rational complex square matrix, and `E0=I-B M(x0)`. If

    eta0 = ||E0||,
    S_jl = sum_k |(A_k)_jl|_1,
    eta_delta = r max_i sum_j |B_ij|_1 sum_l S_jl,
    eta = eta0 + eta_delta < 1,

then `||I-BM(x)||<=eta` throughout the box. The Neumann series proves BM(x) invertible. Since B and M(x) are square finite matrices, this implies M(x) invertible; a separate proof that the proposed B is invertible is unnecessary. Moreover

    M(x)^(-1)=(B M(x))^(-1) B,
    ||M(x)^(-1)|| <= ||B||/(1-eta).

A finite invariant receiver with source membership therefore supplies actual full-native particular preimages. The proof establishes invertibility only on that receiver; an ambient kernel elsewhere is immaterial to existence of these preimages.

The draft's eta_delta expression agrees with this formula: its nested `(k,l)` sum is exactly the row sum of S.

## 2. Exact integer implementation

`sn_assemble` chooses Da clearing every real/imaginary coefficient of all A_k. It builds nonnegative integer S with `S/Da=sum_k |A_k|_1`. A root's Dx clears its 59 exact coordinates, and Dm=Da*Dx. The root arrays initialize their real diagonal to Dm and then add `X_k * (Da*A_k)`, so `(Mr+iMi)/Dm=M(x0)` exactly.

For `B=(Rr+iRi)/Dr`, the verifier forms

    Er+iEi = Dr*Dm*(I-BM(x0)),

using object-array products of Python arbitrary-precision integers. The row sum divided by `Dr*Dm` is eta0. The exact perturbation bound is `r * max(Rabs @ rowsum(S))/(Dr*Da)`, as required. No floating residual, machine-integer overflow or spectral-radius proxy replaces the norm bound.

Floating inversion is used solely to choose B when explicitly requested. The resulting common-denominator integer candidate is independently checked by the exact products. Rounding quality affects success, not validity.

The sparse parser requires a complete closure, exactly n columns, exactly 59 maps per column, strictly increasing valid receiver row indices, three entries per sparse coefficient, and nonzero rational coefficients. Missing rows become exact zero in assembly. It rejects duplicate rows, incomplete closure and the old dense layout. The finite orientation control explicitly checks `columns[j][k][i] -> A_k[i,j]`.

## 3. Source forward-error proof

Let fixed source s have exact coordinates, `y=B s`, and `x=M(x)^(-1)s`. Then

    x-y = (BM(x))^(-1) B(s-M(x)y).

The center term satisfies

    B(M(x0)y-s) = -E0 y,

because y=Bs. Thus its norm equals `||E0 y||`. The code intentionally drops this minus sign only inside a norm; that is correct.

For the perturbation, coordinatewise

    |B (M(x)-M(x0)) y|_1 <= r |B|_1 S |y|_1.

Consequently

    ||x-y|| <= [ ||E0 y|| + r max_i(|B|_1 S |y|_1)_i ]/(1-eta).

This is exactly the code's `coefficient_error_inf`. Its denominators are correct: dy=Dr*Ds for y, de=Dr*Dm for E0, de*dy for E0*y, and Dr*Da*dy for the affine source perturbation. The raw center residual subtracts `s` at common denominator `Dm*Dr*Ds`, correctly implemented by multiplying the source numerator by `Dm*Dr`.

The fixed-source premise is satisfied for the two owned principal-symbol/boost sources: their native definitions do not depend on the 59 background coordinates. This bound is not automatically a bound for a background-dependent source without adding its variation.

## 4. Basis/source and provenance conditions

The verifier reconstructs both owned seeds from current native geometry, compares them with the stored exact source data, and reduces them exactly in the echelon basis. It separately executes all receiver basis equations (time kernel, weight4, raising and Casimir20), and its triangular normalized pivot checks prove linear independence. The direct weak-probe hash and source context hash address the provenance seams identified in the earlier review.

The verifier does not recompute all 16,638 N-images itself; it consumes the separately executed complete closure and verifies its implementation/data bindings. That is a valid modular proof boundary, provided the actual closure record was produced by the native exact closure execution and the reproducible bundle preserves that record, basis, source payloads, preconditioner and current implementation. It must not be described as independently rerunning every closure image during the Neumann stage.

A source preimage in a complex highest-weight receiver also yields preimages for its real and imaginary parts because the held native operator is real. This does not supply every remaining full-R first-jet source, full-R regularity, further derivative closure, or physical admission.

## 5. Required countermodel notation correction

With the draft's declared `F=Sym²(H*)⊕H*`, use

    K_b(S,v)=(b odot v, -i_(b#)S),
    V=(0,tau),
    rho(A)tau=e^1,       b=e^1.

The current `V=(0,tau#)` is a vector/covector type mismatch, and writing `i_b S` suppresses the necessary metric identification. Either use the formulas above consistently, or declare the entire carrier contravariantly and convert all occurrences. The covariant version aligns with the owned symbol notation.

The controls' matrices can consistently represent the action on the covector representation itself. Given their matrix a, the underlying tangent generator is `-a^T`; this merely changes which signed boost is being named. It does not alter the Lorentz covariance checks or the obstruction. The chosen generators satisfy `a^T g^(-1)+g^(-1)a=0` (the diagonal metric equals its inverse).

The obstruction is exact: spatial metric h belongs to ker M, and its native pairing with the new source `e^1 tensor e^1` is1. This disproves the displayed general algebraic implication only. The carrier and symbol are not identified with W2/K95; the result is not a source or candidate kill. If nonzero old sources are desired in the illustration, the documented direct sum with an identity-J copy supplies them while retaining the obstruction.

## 6. Draft wording checks

- Keep pending markers until the actual closure and both Neumann inequalities pass.
- The covariance trial's 0.02117 residual is numerical discovery for root0/source0 only. It declines the proposed x4, and is not an exact candidate obstruction.
- `282` is the proved finite receiver dimension after exact echelon validation; it is not the complete ambient spin4 multiplicity or a physical count.
- Successful certification removes these two reached spin4 sources as possible cokernel witnesses at the two root boxes. It does not establish complete full-R auxiliary solvability.
- Minor prose correction: remove the repeated word in “The source source-specific2+1 distinction”.

Final acceptance remains conditional on inspecting the actual completed evidence and final wording.


## Final evidence disposition

# Final independent review: reached-spin4 compatibility evidence

Date: 2026-11-26. Decision: **APPROVE the bounded mathematical result and its stated claim ceiling. No blocking mathematical or evidence issue found.** The draft's pending result/verification markers still need replacement with the completed facts below before publication.

Reviewed integrated probe:

`tests/program-focus/source_action_spin4_compatibility_probe.py`

SHA256: `e78ec1956858f8d6fd8868e84a622a2f31131452e6a1259a04f6f82a169857a8`.

This approval concerns the held W2/K95 candidate, its native pairing and closed-time kernel, the exact 282-dimensional reached receiver, and the two specified source vectors at both already-certified root boxes. It is not approval of complete full-R/full-N invertibility, a physical domain or propagation claim, class-C necessity, or a GU verdict.

## 1. Evidence independently inspected

I read the complete closure/certificate metadata and relevant implementations; checked all 16,638 sparse map records for exact rational coefficient strings, correct map count, strict receiver-index ordering and valid indices; verified the actual data and function hashes; and checked the exact rational relationships among stored bounds. I did not rerun heavy closure or matrix products during this review.

The closure contains exactly282 input basis columns, each with59 background maps, `completed=282`, and no failure record. Its engine, projection and closure-procedure function hashes match the final integrated source. Basis, background and all native dependency hashes match the files used for review. The final certificate's closure binding is identical to that closure's binding.

The exact basis-validation record is complete, with1128 native equations (four per basis vector), normalized independent echelon pivots, time-kernel membership, weight4, raising annihilation and Casimir20. The final certificate embeds that record unchanged. Both exact source vectors were reconstructed and reduced by the reviewed native-source procedure.

The certificate's verifier hash matches the final integrated probe. Its direct weak-probe and source-context hashes match. Both candidate matrices have282-by282 exact integer numerator arrays and positive exact denominators. Both frozen root-record hashes, radii and shared candidate-file hash match the actual files.

The following exact certificate relationships were independently checked using Fraction arithmetic:

- `eta=eta0+eta_delta<1` for both roots;
- `inverse_bound=preconditioner_norm/(1-eta)`;
- each source-error bound equals `(preconditioned_center_residual+rootball_source_perturbation)/(1-eta)`;
- both sources have282-coordinate exact numerator payloads at each root.

## 2. Completed root-box results

The stored bounds are exact rational numbers. Decimal values below are readable approximations, not the certifying arithmetic.

| Root | Center defect eta0 | Box perturbation | Total eta | Inverse norm upper bound |
|---|---:|---:|---:|---:|
| 0 | 1.73681234e-14 | 1.39333486e-6 | 1.39333488e-6 | 1.92472548 |
| 1 | 1.43202504e-13 | 1.58448990e-5 | 1.58448992e-5 | 29.7289763 |

The reported source-coordinate error bounds, uniformly over the held root boxes, are approximately:

| Root | Source0 (b5) | Source1 (b12) |
|---|---:|---:|
| 0 | 1.01512699e-9 | 1.98965169e-9 |
| 1 | 1.15116654e-8 | 3.86784835e-8 |

Both root records explicitly pass invertibility and contain both source solutions; `both_roots_solved=true` is supported by the records, not merely a descriptive flag.

The mathematical proof previously reviewed applies: exact full-native closure makes M preserve the receiver throughout the59-coordinate affine family, and the two strict Neumann inequalities make its restriction invertible throughout both boxes. Exact source membership therefore supplies genuine native particular preimages for both reached spin4 sources. An ambient kernel outside the receiver does not negate this existence result.

## 3. Arithmetic, parser and reproduction checks

The final control record reports161 exact cubic-engine controls,190 exact integer-projector controls, and2856 exact generic covariance-premise controls. Their current file/function bindings agree with the integrated implementation. The Neumann certificate retains14 tiny literal-Fraction and parser controls.

The final sparse parser rejects float coefficient payloads, duplicate/out-of-range indices and incomplete closures. Root coordinates/radii reject inexact payload types. Preconditioner integer parsing rejects float/truncation inputs. The new sparse `certify` CLI is separate from `legacy-certify`; the integer-resume guard checks direct weak/algebra dependencies before continuation. These address the earlier review observations without changing the proved arithmetic formulas.

I independently decoded all eight data-only records in `lab/process/source-action-spin4-certificates.json`, verified their stated byte lengths and SHA256 hashes, and confirmed byte equality with the reviewed scratch records:

- exact sources;
- exact basis;
- complete sparse closure;
- native basis validation;
- frozen rational inverse candidates;
- final Neumann certificate;
- arithmetic/covariance controls;
- scoped benchmark.

The lead's fresh-cache replay log shows exact certification without generating new candidates, with both passing bounds unchanged and completion in about33.3seconds. This review inspected that log and the matching frozen artifacts; it does not claim the reviewer independently executed that replay.

## 4. Covariance and countermodel

The final draft corrects the covector types: `F=Sym²(H*)⊕H*`, `K_b(S,v)=(b⊙v,-i_(b#)S)`, `V=(0,tau)`, and the boost takes the covector tau to e^1. This is consistent with the finite controls' representation convention.

The generic countermodel proves that the displayed covariance/reciprocity/kernel hypotheses do not by themselves imply fixed-P boosted-source solvability. Its exact adjoint-kernel pairing is1. It remains explicitly independent of the actual W2/K95 carrier and does not exclude that candidate. The current successful receiver certificate is fully compatible with this general counterexample.

The root0/b5 numerical trial residual about2.117% only rejected the trial `Pi4 P rho(H03)Y5` at discovery precision. It was not used as an exact obstruction or certificate of support. The final exact receiver result, not that trial, settles the two reached sources' image membership.

## 5. Benchmark and final wording

The benchmark's three warm exact maps all agree with their native references. Its measured total times0.130463seconds and0.00202725seconds give a64.3547 ratio. The record correctly describes a local, hardware-dependent three-map microbenchmark. Do not call it a measured64x speedup of the whole closure or entire research workflow.

The final report may state:

> The two owned connection-generated highest-spin4 sources have native auxiliary preimages throughout both certified stationary-root boxes, via a282-dimensional exact common invariant receiver. They therefore do not furnish a cokernel obstruction to the stated W2 full-R continuation.

It should retain:

> Remaining first-jet source components, smooth complete full-R elimination, the remaining dynamical equations, physical admission/quotient/normalization/propagation, and source necessity remain open.

The suggested horizontal-Nomizu and old-E spin5 membership continuation is a proposed next finite test, not a result established by this certificate. The earlier constrained-Q result and its limited scope remain unchanged.

## Final disposition

Approve the scientific result at Tier2's declared scope. No new heavy validation is requested by this review. Complete the pending report/accounting surfaces using the exact evidence; keep the three-map timing and general covariance countermodel separate from the native image-membership theorem. No source, physics, canon or class-C verdict follows.


## Source relevance and quick20 selection

# Hostile source / selection rerank — 2026-11-26

## Result

**Retain the bounded full-R reached-spin4 compatibility test as the best executable next discriminator among the supplied live options.** I found no already-supplied, short, source-necessary class-level discriminator that outranks it. This is a relative selection judgment from the named current evidence, not a theorem that no other useful GU attack exists. The test is candidate-only: even a certified failure does not falsify GU or source-required class C.

Read-only review at clean `HEAD = origin/main = 3e8fa792e93e8a58e804364c842080a7e6c72810`, freshly fetched by the parent. No repository edits or verification jobs. Sources are owned repository records below, rather than a repeated primary-source custody search.

Preflight: target `LB-CLASS / full_range_auxiliary_spin4`; tier T2 for compatibility, T1 if a scoped kill is proposed; expected delta is exact range/cokernel disposition for an actually reached full-R first-jet source; kill condition is a genuine obstruction in the entire relevant native receiver, not failure of an ansatz or departure from the previously inverted envelope. Source bridge is absent for necessity of W2 and conditional for source-compatible carrier motivation.

## Exact premise, evidence, exclusion, delta

**Required mathematical premise.** The realization under test requires a differentiable full-range auxiliary elimination `Y:R→N` with `M Y^b = L^b`, using the actual induced N/R and covector connections on each held W2/K95 coupling-one background. If the only required realization is the already constructed diagnostic subbundle Q, this premise is unnecessary: the Q result survives independently. Nor has the source required unrestricted full-R auxiliary elimination as its physical rule.

**Owned evidence.** `explorations/conditional-build/source-normal-tensor-class-2026-11-26.md`, §§6.1–6.7, supplies the actual affine adapted frame, N/R projectors and induced connection, the two Q7 vectors, and two exact nonzero spin4 sources. In the displayed frame, after manifest range terms are removed, the tested first-jet compatibility class is represented by `L_b Γ_R,a V`. For normal axis10, `Γ_R,10` contains `R ρ(H03) R`; its spin6 part W6 then gives `L4 = Π_spin4 P K^5 W6`. The two L4 support sizes are344 and472, with exhibited coefficients `-i/18` and `4/15`, and exact Casimir eigenvalues42/20. These are geometric SO3 labels, not physical particle spins.

**Already tested.** The exact120-dimensional highest5 envelope E is invariant under all59 background coefficient maps (7080 full-image reductions) and invertible over both certified root boxes. Four scalar goals lie in conjugate(E) throughout the affine59 family (240 exact checks), so the corresponding highest5 kernel ambiguity is gone in the stated equivariant category. Complete spin6/7 inverses and the actual moving Q7 bundle give a smooth constrained-Q response including its second fundamental lower source. A nonzero local compact-test first-variation functional is realized. See `source-action-weak-response-2026-11-26.md` and normal-tensor §§6.3–6.6. Recomputing those inverses, contracted consistency, restricted-Q derivatives or current nonzero tests adds no delta.

**Untested delta.** Decide whether the actual spin4 sources belong to `range M` at both certified roots; a spin5 component outside the E orbit, if actually reached, is a separate uncovered source. Start with the exact reached module or a genuine adjoint-kernel certificate. A nonzero `<k,L_b Γ_R,a V>` with `M† k=0` in the full native receiver proves the necessary compatibility fails. Merely `L4∉E`, a nonzero projection outside U, or a null vector of a truncated matrix does not. Positive membership for two seeds is a necessary-condition success, not full-R sufficiency. Keep a zero receiver pairing distinct from invertibility.

**Pairing and root control.** Use the W2 native bilinear/Hermitian adapter actually stated, correct dual weight and full-carrier residual. A numerical approximate kernel is not an adjoint-kernel certificate, and checking rational centers does not decide the exact algebraic roots/root boxes. A root-specific exact or rigorous interval certificate must carry the decisive equality/inequality. No physical positive norm is implicit.

## Why the tempting shorter alternatives do not beat it

| Proposed discriminator | Required premise / owned result | Disposition now |
|---|---|---|
| Fixed normal tensor optional-C emptiness | Printed conjugation/minus adjoint, actual fixed symmetry and optional C | Consumed and **fails as an exclusion**: source-compatible fixed4R survives. The zero theorem belongs only to the plus/reversion comparator. |
| Truly-spinless source mass insertion | SC-MAS-02 grade1 `Λ1⊗Λ1`, actual exterior order and independent fields | Consumed primitive placement: real `μ c_V` survives with contraction14μI; normal component10μI. Physical curvature/mass/readout identification is not supplied. |
| Weak/chiral decoupling as μ→0 | SC-CHI-51/52 require an effective physical regime, actual source equation/background/scalar/readout and an appropriate limiting quantifier | Strongest source-level alternative in value, but not presently executable from the supplied data. Primitive current or fixed off-shell horizontal anticommutator is not the admitted physical response. No repeat custody pass. |
| Index/parity/generation contradiction | A physical2+1-to-index bridge, compatible grading, observation chain map and domains | Existing grading/branching exclusions consumed. K95 quaternionic evenness does not become a source physical-family count; K77 and K95 differ. |
| Anomaly or Spin-Z4 obstruction | Exact physical action/symmetry, charge spectrum and admitted backgrounds | Bounded symmetry applicability audit complete. No source-established nonzero residue supplied; an additional Z4 is not compulsory. |
| Localization/trace obstruction | Source-required normal-L2 and native Krein transfer | Both load-bearing premises remain unproved; W175 native gap withdrawn. Stronger positive-space estimates cannot replace them. |
| Old A01 positivity/hidden E2 comparison | A genuinely common admitted domain | Already excluded: every nonzero E2 witness lies outside the injective old selected graph. Reusing its norm, cutoff or positivity is invalid. |
| Boundary/index or scalar-mass ledger route | Native end/physical receiver; action-owned scalar descent/spectrum or quotient | Physics ledger retains precisely these missing inputs. Multiplicities, Bott3 or a one-form contraction do not supply them. |

The opportunity register's O01–O29 distinguishes completed local work from these explicit revival inputs. Its current `primary_adjoint_spinless_2026_11_26` update names only the reached full-R test as ready and physical weak readout as lacking authentic admission/normalization. The source-required-class packet steps0–5 and six-spinor grading packet are done. Their old tasks are not fresh competitors.

## Source and ledger custody applied to this ranking

- `source-adjoint-spinless-placement-2026-11-26.md` corrects the source pairing: minus/conjugation has optional-C normal36R/image24/kernel12 and fixed4R/image4/kernel0. C is an anti-isometry there; do not import the old Sp label. The W2 auxiliary calculation was already on its separately stated opposite-to-plus convention, so the source-attribution correction does not erase its calculations or make its action source-necessary.
- SC-OP-04 is a candidate-strength displayed operator on four independent classical fields. SC-OP-05 retains rival southeast terms. Neither selects W2/SEminusonehalf, its bosonic stationary roots or a physical barred graph.
- SC-GEO-51 names full U(64,64); additional C preservation is conditional. SC-MAS-02 names a truly-spinless connection component, not a conventional scalar-Higgs field. SC-CHI-51/52 concern an effectively chiral low-curvature regime; they do not require the exact full off-shell grading previously excluded. SC-META-53 does not supply a positive physical quotient.
- Section observation is contraction. Preserve source2+1: imposter128 is spin1/2 with observed gamma-trace placement; the RS384 cousin is separately labeled. Spin4 here is a rotation type of an auxiliary coefficient computation, not a fourth physical family or a massive spin4 particle.
- The current append-only physics ledger v0.263 is historical owned evidence, not current steering. RA-E3/E4 keep scalar descent and mass spectrum open after the contraction correction; RA-G1/G2 require a physical quotient/spectrum and physical mirror decoupling, respectively. Its `source_return` says no source claim killed. The newer live assumption view agrees that W2 is one directed reconstruction with absent source necessity. Its bookkeeping10 families/4 obligations/net6 is not a GU necessity bound.

## Quick20 mathematical descriptions for this rerank

1. Linear algebra: solve actual reached-source range, not a larger arbitrary inverse.
2. Representation theory: use spin4 multiplicity and intertwiners; do not equate geometric rotation spin with particle spin.
3. Clifford algebra: maintain the minus source adapter and ordered products; old plus-zero is inapplicable.
4. Differential geometry: Γ_R mixing, including the time-adapted boost, supplies the genuinely new source.
5. PDE constraints: Q constraint elimination is solved; full-R differentiable elimination is a distinct necessary condition.
6. Functional analysis: local compact test functions do not confer physical domain membership.
7. Symplectic geometry: no supplied physical presymplectic radical turns the candidate test into a quotient theorem.
8. Gauge theory: full U remains the parent; optional C and fixed reductions cannot be smuggled in as source laws.
9. Category theory: preserve carrier, pairing, real structure, observation and field independence under each claimed identification.
10. Number theory: exact Gaussian-rational weights/Casimir arithmetic certify coefficients; integer multiplicities are not generation counts.
11. Algebraic geometry: distinguish generic59-family statements from the two certified root loci.
12. Topology: Bott/end classes have no supplied physical receiver for this source.
13. Index theory: no grading/domain/observation bridge means no fast physical2+1 index contradiction.
14. Anomaly theory: closed applicability audit supplies no fresh compulsory anomalous symmetry.
15. Variational calculus: a nonzero first variation is not a propagated physical response or an energy instability.
16. Perturbation theory: individual jet compatibility is stronger than its already-tested contracted identity.
17. Harmonic analysis: normal frequency and support cannot be replaced by base bandwidth.
18. Probability/measure theory: physical state normalization does not require finite invariant background probability.
19. Control/observability: arbitrary covariant bulk histories and hidden jets are already demonstrated; the physical readout law is still unselected.
20. Optimization/experimental design: two reached seeds plus a full-receiver residual are the least-cost fresh decision supplied; no expanded inverse backlog is justified in advance.

## Review outcome

No source or physics verdict change. Finish the finite reached-spin4 test, then rerank on its actual result. If it survives, report only that this necessary condition survived. If it fails, report the exact candidate full-range realization excluded while preserving restricted-Q evidence and all source-compatible alternatives. A T1 kill still requires the repository's normal independent acceptance work. This report supplies selection and scope review, not mathematical certification of a new result.


## Conditional post-result reranking

# Conditional rerank after successful reached-spin4 solves

Basis: owned repository source/physics context at `3e8fa792e93e8a58e804364c842080a7e6c72810`, plus parent's provisional discovery report:282-dimensional highest4 receiver in4032 coefficient positions; full59-map invariance and actual-root certificates pending. Numerical root-center residuals are not yet acceptance evidence. This recommendation is conditional on exact source membership, full-carrier invariance and both actual-root solve certificates passing.

## Recommendation

**The next fresh finite tests are (1) horizontal-spatial-connection spin4 sources against the new E4 orbit and (2) the actual spin5 remainder against the already certified E5 orbit, before constructing another inverse.** A proposed connection-rank lemma can reduce the spin4 census to up to four reduced sources: two normal-boost sources already tested and two horizontal Nomizu sources not yet certified. See `/private/tmp/gu-actual-connection-spin-census-lemma-20261126.md`. Then make one bounded census of the actual first-jet source family generated from the two Q7 inputs, quotienting by all already certified receiver spaces. This is completion of the present necessary-condition test, not an automatic descent through all auxiliary spins or an all-R inverse project.

First compute the spin6 part of `R rho_W(Lambda_0) R V7` for each input Q7 copy, retaining both the one-form and Clifford legs, apply the normal rank2 principal map, and reduce its spin4 part in E4. SO3 alone does not identify this horizontal-spatial connection family with the normal time-space boost family. After the actual connection-rank lemma and these two reduced checks are established, no other spin4 family is expected at this first-jet scope. This remains a lemma to certify, not a completed source census.

For each owned V7 and its actual boost image W6, retain the unprojected source `L=P K^5 W6` rather than only its spin4 part. Compute `Π5 L`; where L has weight4, apply the native raising operator once to get its highest5 representative, with the nonzero ladder factor explicitly accounted for. Reduce that representative in the known120-dimensional E5 (and required conjugate/realification). The two displayed spin4 tests have not decided this membership. Normal axis8 gives the known i-related source; do not count it as independent work without checking the full unprojected identity.

The follow-through census covers the **actual** `L_b Γ_R,a V` for the two input Q7 modules, all induced connection directions a and principal covector slots b, under their SO3 orbit. Use the already-owned symmetry to minimize representatives only after proving those representatives span the real source maps. Retain all connection/lift terms; covariance alone has just failed as a right-inverse construction. Reduce the resulting source space modulo

`E4_orbit + E5_orbit + complete_N6 + complete_N7`

with full native residuals. Include any actual lower source entering the particular jet equation; distinguish it from the already-solved restricted-Q lower response. Do not assume the known boost example exhausts other connection directions.

### Honest outcomes

- **Zero quotient:** every source in this explicitly generated first-jet family is covered by existing certified receivers. This closes this necessary-condition family. It does not prove full-R elimination on every input, higher jets, an interacting constraint solution, physical propagation or source necessity.
- **Nonzero quotient:** report the first actual residual and its spin/multiplicity. It is an uncovered source, not a cokernel. Test a true adjoint-cokernel pairing or only its reached M-module if the residual is needed for the stated compatibility goal. No obligation to invert every lower-spin block follows.
- **Certified nonzero cokernel pairing:** excludes this candidate's specified full-range first-jet realization. It leaves the existing restricted-Q functional and source GU outside that conclusion.

The generic countermodel excluding automatic covariance implication is worth retaining as a method correction. It proves neither failure nor success of these W2 sources. Numerical2.1% failure of a shortcut likewise rejects the shortcut, not the true range solve.

## Source relevance and strongest alternative

The required premise remains existence of a differentiable full-range auxiliary lift for this W2/K95 realization. Source SC-OP-04 permits a candidate four-independent-field operator; it does not require W2/SEminusonehalf or this lift. Full-U, K77/K95, source2+1, literal contraction and optional-C boundaries remain unchanged.

The strongest alternative in potential falsification value is a source-admitted low-curvature/weak-response discriminator for SC-CHI-51/52. Its exact unavailable input remains an authenticated common physical domain/quotient, actual dynamical equations/background and curvature parameter, normalized readout and propagation law. The new spin4 solve supplies none of those. Thus it does not make that alternative newly executable. Repeating source custody, primitive spinless insertion, fixed-normal tensor classification, same-grading exclusions, anomaly applicability, normal-L2 arguments or oldA01/E2 transfer would repeat consumed work or reuse a withdrawn premise. The current physics ledger's scalar-descent, mass-spectrum and physical-quotient demands do not supply a shortcut.

If the bounded first-jet quotient is zero, there is no evidenced reason yet to promote “invert spin3 next” as the successor. Rerank from the actual surviving residual/observable question under current program_focus; a second-jet calculation needs its specific new decision link. This is a scope warning, not a new stop gate, waiting rule or change of cadence.

## Quick20 retention

Retain the20 descriptions in `/private/tmp/gu-spin4-rerank-20261126.md`; this result changes their application, not their count. Key deltas: linear algebra becomes quotient membership before inverse growth; representation theory must prove source-map spanning; category theory forbids promoting equivariance to the missing commuting lift; number theory preserves exact Gaussian-rational/ladder arithmetic rather than a numerical center solve; rigorous analysis certifies actual roots; constraint theory separates first-jet necessity from all-range/higher-jet sufficiency; source relevance remains candidate-only. No GU falsification is claimed.


## Proposed source-map reduction, not yet certified

# Proposed bounded source-census lemma

Status: next-wave lemma / read-only analytical derivation. Not a new accepted repository theorem or numerical certificate. Grounding: `tests/program-focus/source_action_deep_geometry.py`, its Nomizu formula and declared basis; `source-action-homogeneous-analytic-vacuum-2026-11-25.md` A1–A2; `source-normal-tensor-class-2026-11-26.md` §§6.1–6.7. No probe was run.

## What the owned data support

At the SO3 stabilizer of the timelike line,

`T_pY = H_time(V0) + H_spatial(V1) + N_scalar(2 V0) + N_timespace(V1) + N_spatial-traceless(V2)`.

Thus the tangent representation is `3 V0 + 2 V1 + V2`. The two spin1 copies are distinct. A rank-one family of connection matrices can be present on **both** of them.

The displayed Nomizu formula proves the original homogeneous-frame LC matrices vanish for every normal direction A. For horizontal v,w, its potentially nonzero component is proportional to

`<Av,w>_eta - <v,Aw>_eta = 0`

because A is eta-selfadjoint. All other normal-first-index components vanish by bracket type. For horizontal x, however, Lambda_x is generally nonzero: it takes a normal A to `-A x`, and a horizontal v into the normal vector characterized by `<Lambda_x v,A>_N = <A x,v>_eta`. This is a genuine H/N-mixing ambient connection action, not the Lorentz-isotropy boost action.

Use a local SO3-equivariant time-adapting gauge with h(0)=1 and canonical pure-boost first derivative. At first order the condition is

`tau (S + h') = scalar * tau`.

For spatial normal traceless S (the V2 copy) and the two scalar normal directions this requires no boost. Only normal time-space S supplies a boost. In the displayed basis these are axes10,12,13; scalar axes4,7 change lapse only. P and R depend on the time **line**, so lapse changes add no projector rotation. Thus, in this chosen adapted frame at p, the actual LC connection family has only the horizontal V0/V1 Nomizu components and the normal V1 boost correction. The full action on the one-form/End carrier must be used, not only the spinor commutator.

## Frame-independent statement to prove/record

Raw connection coefficients are not tensors; an arbitrary local frame change can insert additional-looking terms. The useful tensor is the second fundamental map

`B_a = (R - Pi_Q) nabla^R_a i_Q`

or, equivalently for the spin4 source, `Pi_4 L_b Gamma_R,a i_Q` modulo the Q-internal connection. Changing an adapted frame by SO3 adds a rotation acting inside the SO3-invariant Q7. Applying L_b to that added Q7 vector has spin at least5 because the principal covector has spin at most2. Therefore it cannot alter the spin4 source. The canonical-gauge computation should be presented as a computation of this tensorial quotient, not as an invariant assertion that every frame's Gamma has rank≤1.

In the declared LC-plus-algebraic-J derivative split, these data support the lemma that B has no normal-spin2 input component. Then Gamma_R Q7 modulo its irrelevant internal connection has spins6/7 (ambient maximum7). Applying K_b, whose covector has spin at most2, produces no new cokernel-source component belowspin4. The covector-index connection terms L_c V7 are already in the pointwise principal-source family and have spin≥5; terms explicitly M times a vector remain in range M. This bound concerns this first-jet quotient, not arbitrary R inputs, higher derivatives, a different derivative/lower-term split, or nonlinear equations.

## Why two existing seeds do not establish completeness

Spin4 can arise only through

`V1 (connection input) tensor V7 -> V6`, followed by
`V2 (principal covector) tensor V6 -> V4`.

Both Clebsch–Gordan couplings have multiplicity one. But the connection input has **two distinct V1 copies**:

1. normal time-space frame-adaptation boosts;
2. horizontal spatial Nomizu connection.

For each of the two input Q7 copies, these can give two different reduced vectors in the N4 multiplicity space. Hence there are **up to four reduced spin4 source seeds**, not automatically two. The existing two seeds certify the first family. SO3 multiplicity-one fixes dependence on magnetic weights within a given family; it does not identify the two families' reduced vectors, and does not make the N4 multiplicity space one-dimensional.

The exact missing small check is therefore, for j=5,12,

`W6_horizontal,j = Pi_6 R rho_W(Lambda_0) R V_j`,
`S4_horizontal,j = Pi_4 P K^5 W6_horizontal,j`,

with native coordinate normalization and the same raising/phase conventions as the already owned normal-boost source. Here rho_W includes the one-form leg and End/Clifford leg. Test zero or membership in the new certified E4 highest-weight orbit. If the selected real component is not already highest weight, raise/project with the exact known nonzero ladder factors. Derive the x1/x2 relations from the SO3 tensor law; do not assume them from the boost implementation.

A zero or contained horizontal source would reduce the complete spin4 census to the existing two receivers. A nonzero uncontained source is a new reached source, not a cokernel obstruction. Its discovery would still not justify all-lower-block inversion.

## Remaining proof seams and practical next step

The native Nomizu identities and representation bounds above have short written derivations. Before calling the census complete, explicitly record (a) the first derivative of the actual chosen time-adapting gauge, (b) the induced projector/one-form/Clifford connection identity, (c) the tensorial quotient under residual SO3 gauge, and (d) both horizontal reduced-source memberships. These are bounded checks; no new physical domain or source law is needed for this candidate-level lemma. They have not been verified here as an integrated exact source-map certificate.

After that, reduce the genuine spin5 remainder against the old E5 orbit, using SO3 to enumerate the actual source maps rather than all coordinate slots. Complete N6/N7 already cover higher outputs. The lemma shrinks the first-jet census; it does not make an auxiliary right inverse follow from covariance. The parent's generic countermodel and failed covariance trial remain compatible with all statements above.

Source relevance is unchanged: K95 W2 candidate only, full U retained, independent fields and literal observation preserved, no physical particle-spin or GU-falsification claim.
