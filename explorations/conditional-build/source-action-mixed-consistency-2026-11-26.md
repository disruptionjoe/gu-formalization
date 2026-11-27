---
title: Actual mixed spacetime-fibre constraint consistency
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T2
expected_delta: Decide the actual mixed principal consistency sources using existing certified receivers
actual_delta: Four of eight mixed principal channel types have native M preimages at both roots. The other four lie outside the old receivers, with no M-cokernel verdict. Their full-M range test reduces exhaustively to the complete even highest5 time-kernel inside512 ambient directions.
class_covered: Autonomous imaginary-connection quadratic W2/K95 block at both real zero-matter kappa1 roots; the mixed horizontal-normal Hessian map on the two-copy Q7 sector, with all allowed multiplier corrections retained.
premises:
- 'source-action-constraint-consistency-2026-11-26.md: actual first-consistency equation, geometric cancellation and Lorentz covariance'
- 'source-action-constraint-source-repair-2026-11-26.md: horizontal two-jet absorption and exact mixed quotient formula'
- 'source-action-kappa1-constraints-2026-11-25.md: complete N6/N7 inverses at both roots'
- 'source-normal-tensor-class-2026-11-26.md: primary Q lift and native transported carrier'
source_bridge:
  status: conditional
  reason: These are necessary consistency conditions for the named candidate jets. W2 and arbitrary Q jets are not source-required physical states; propagation and the physical quotient remain unproved.
kill_condition: A genuine obstruction requires a dual annihilating full M and all permitted normal and zero-order kernel repairs. Failure of membership in existing receivers or a stronger sufficient enclosure is inconclusive, not a W2 or GU exclusion.
---

# Actual mixed spacetime-fibre consistency

program_target: LB-CLASS
tier: T2
expected_delta: Decide the actual mixed principal consistency sources using existing certified receivers
actual_delta: Four of eight mixed principal channel types have native M preimages at both roots. The other four lie outside the old receivers, with no M-cokernel verdict. Their full-M range test reduces exhaustively to the complete even highest5 time-kernel inside512 ambient directions.

Basis: freshly fetched `4ee3a8bb90b418216eff0fb740df935af08a4ce5`.

## Result in plain terms

**Half of the eight mixed consistency channel types pass at both held backgrounds.** The other half reach a different symmetry block. They are outside the spaces previously certified, but that is not an inconsistency: the full equation may have a response in that other block.

The useful reduction is exhaustive. Any possible constraint response for the remaining sources can be projected into a complete space of at most512 highest-weight directions. The next test can cover that whole block, instead of repeatedly guessing small response spaces. Neither this reduction nor the four passing channels establishes propagation, a physical state space, or a GU verdict.

```gu-typed-objects
result: mixed horizontal-normal principal first-consistency source
carrier: imaginary-U connection one-forms of W2 K95; N=ker K_dt; Q=two real geometric SO3 spin7 modules LAYER=ambient BRIDGE=physical_admission_unproved CHIRALITY=N/A
pairing: native indefinite trace/form pairing ON=declared_carrier
real_structure: full native U64_64 real carrier; highest-weight complexification for exact arithmetic
grading: geometric SO3 spin and derivative order; not physical chirality or family number
action_owner: repository W2 candidate, actual coupled quadratic Hessian at held roots
target: mixed Hessian coefficients in full augmented constraint cokernel MAP-TYPE=homomorphism
```

SC-ACT-01 asserts action grammar, not uniquely selected W2. SC-ACT-06 concerns the Euclidean Upsilon complex, not this Lorentzian propagation. SC-GEO-51 names full U(64,64); SC-GEO-55 uses gauge-rotated Levi-Civita displacement. SC-META-53 remains UNCERTAIN about indefinite spectra. Source2+1, contraction observation, independent fields, primary-minus adjoint, K95/K77 and geometric/physical gradings remain distinct. LT-GR1, LT-GR6b and LT-SM8 retain their verdicts.

## 1. Actual mixed source and the owned shortcut

Use A=K_dt, N=kerA, P the native orthogonal projector, R=1-P, G=(A|R)^-1 extended by zero, C=I+2N(T,.), M=PCP. The polarized cubic map N(T,.) and the kernel bundle N are distinct objects. Let Y_a V be the owned primary response satisfying M Y_a V=P K_a V.

For horizontal xi and normal eta, use the full cross coefficient, without1/2:

    r_mix = P K_xi G K_eta V + P K_eta G K_xi V
            - L_xi Y_eta V - L_eta Y_xi V,
    L_a = P K_a G C P + P C G K_a P.

With the actual horizontal Lorentz boost S satisfying [S,A]=K_xi and j=PSP, the previously proved identity is

    r_mix = P K_eta G S A V - L_eta Y_xi V
            + M( Y_(S eta) V - j Y_eta V ).

This quotient formula uses the owned existence of normal primary responses, but need not evaluate them. It retains the full normal symbol and the exact horizontal response; approximate root-center responses cannot certify range membership.

## 2. Pointwise ambient covariance removes G from this calculation

Let eta=theta_a with a normal and tau=theta3. Choose the tangent metric-skew generator U with

    U[3,a]=-1,  U[a,3]=-1/d_a,

and all other entries zero, since d3=-1. Its active covector action is -U^T and sends tau to eta. Its action on connection fields is the full dual one-form action plus the spin commutator on End(S). Write U for that induced action as well.

The actual Phi construction uses the canonical phi1=sum theta^a tensor gamma_a, its wedge-square phi2, Clifford products, native Hodge stars and the actual pointwise trace/form adjoints. These are equivariant under connected oriented metric-Spin(9,5) frame changes. Consequently the actual principal symbol and algebraic cubic term obey

    [U,A]=K_eta,
    U N(T,y)=N(U T,y)+N(T,U y),
    [U,C]=2N(U T,.).

This is pointwise algebra. U mixes horizontal and normal directions; it is **not** a symmetry of the held differential connection or background. In particular U T must be retained and need not lie in the59-dimensional invariant background family.

Put j_eta=PUP. The exact projector identities give

    L_eta=M j_eta-j_eta M+2P N(U T,.)P.

Using M y=P K_xi V=P S A V for y=Y_xi V, the mixed source modulo imM has the cheaper representative

    q_mix = P U S A V - 2P N(U T,y).                  (1)

Indeed P K_eta G=P U R, so

    P K_eta G S A V-L_eta y = q_mix-M(j_eta y).

No time-symbol inverse G is applied in (1). For an approximate y with residual e=My-PK_xiV, the omitted correction is +j_eta e; it is not permitted to discard it. The corresponding actual mixed source remains equivalent only after the owned primary identities are used.

A familywise sufficient test is to put the constant source and every projected cubic image N(U T_alpha,b) into existing certified receivers, for all59 backgrounds and each b in the relevant horizontal response block. Passing settles both exact roots at once. Failure does not prove failure for the constrained actual y(T); coefficient relations can cancel the remainder.

## 3. Complete mixed channel types

Under spatial rotations H*=V1 and the normal cotangent is2V0+V1+V2. Thus

    H* tensor Nnormal* = V0 + 4V1 + 2V2 + V3.

With Q=2V7 and maximum target spin7, the only targets outside complete N6/N7 inverses are two spin4 and six spin5 reduced channels over both Q copies. These are channel types, not eight asserted independent native vectors.

For each highest Q vector, four raw axis pairs detect them: (theta0,theta5)->spin4; (theta0,theta10)->spin5; and (theta0,theta9), (theta2,theta5)->spin5. The last two must span both input ranks2 and3, not be mislabeled as a single irreducible. The native derivative-input Casimir and nonzero output Clebsch-Gordan factors must be verified before a completeness claim.

The native derivative-input calculation uses

    a=(theta0-i theta1) tensor (theta9-i theta11),
    b=theta2 tensor (theta5-i theta8).

The Casimir matrix on (a,b) has rows [[10,2],[4,8]]. Both have weight-2; a-2b has eigenvalue6 (rank2) and a+b eigenvalue12 (rank3). For the projected raw spin5 outputs A=q(theta0,theta9), B=q(theta2,theta5), complex lowest-weight extraction gives q(a)=4A and q(b)=2B. Thus the two distinct reduced outputs are4(A-B) and2(2A+B). This identifies the derivative-input ranks rather than labeling a raw axis sample irreducible.

The owned horizontal source s0=P K0 V_highest is entirely highest spin6. Let E be the native raising operator. Because E theta0=-theta2, EV=0 and P is equivariant,

    0=E s0=-P K2 V_highest.

Thus a zero primary response is available for xi=theta2. This also explains the owned absence of a reduced N7 horizontal component. Native verification of the source zero makes the fourth raw channel root-independent:

    q_(theta2,theta5)=P U5 S2 A V.

No physical state or inverse choice is introduced by using zero for a zero primary source. It does **not** make the constant mixed term zero. The corrected native calculation gives a nonzero B=P U5 S2 A V for both Q copies. In particular P S2 A V=0 only puts S2 A V in the complementary range; U5 can map it back into the constraint space, so P cannot be moved past U5. Keep the two distinct reduced outputs 4(A-B) and 2(2A+B).

The corrected constant-column test uses the actual base-Lorentz S, including its induced normal action, separately from the ambient time-normal U. It finds covered spin4 constants (352/480 terms) and covered eta10 spin5 constants (280/144 terms). The eta9 spin5 constants (160/200 terms) and xi2/eta5 spin5 constants (184/296 terms) lie outside the old receivers. These are ambient term counts for the two Q copies, not invariant dimensions. An earlier work-in-progress summary claimed those spin5 constants were zero; the stored native output contradicts that claim and controls this report.

Consequently the actual eta9 source is A=d9-2 Pi5 P N(U9 T,y0), including its nonzero constant d9, while B=d25 is root-independent. Failing inclusion in existing receivers is not a constraint obstruction. The complete source and both reduced combinations still require an actual range test.

## 4. Why the old spin5 receivers miss the new terms

For native one-form/Clifford coordinates (e,c), define

    chi(e,c) = popcount((e XOR c) & 13319) mod 2.

The mask selects axes {0,1,2,10,12,13}, the two geometric rotation-vector copies. Simultaneously reversing these six axes is an orientation-preserving diagonal metric involution; it commutes with spatial rotations. Its coefficient action preserves the native Phi construction and time symbol, and all 59 background vectors are even. Hence the entire affine constraint operator M preserves chi. No assertion that this involution lies in a particular connected Spin component is needed. This is coefficient parity, **not physical chirality**.

Both certified spin5 receivers are odd. The eta9 constant, its entire background-dependent term, and the xi2/eta5 constant are even. Thus expanding calculations inside those old receivers cannot settle the remaining range question. A nonzero even source is outside their sum but may still have a preimage elsewhere in the full native constraint space.

The complete even ambient highest-spin5 space has dimension 512. Its weight5 and weight6 multiplicities are respectively 664 and 152 in the exact one-form tensor exterior-Clifford character. The relevant auxiliary space is the time-symbol kernel inside those 512 directions; its dimension and M invertibility are not established by this character count. A complete finite-block calculation can replace repeated guesses at small response spaces. A candidate source's sparse coordinate support is not that complete carrier. For an even highest5 source, any full-N M preimage can be projected first to even parity, then to spin5 and weight5. These projectors commute with M and preserve N. Thus this complete finite space is sufficient **and necessary** for the M-range question. If its restriction is singular, the full augmented kernel-multiplier test below still remains; singularity alone is not inconsistency.

## 5. The complete negative test depends on target spin

Existing full N6/N7 inverses imply Z6=Z7=0 for Z=kerM. The kernel may be degenerate in the native form; do not project onto it using an invented positive metric.

For target spin5, the full remaining augmented test has seven normal derivative types (two scalars from Z5; vector from Z4,Z5; tensor from Z3,Z4,Z5) plus the zero-order Z5 term.

For target spin4, it has **nine** normal derivative types (two scalars from Z4; vector from Z3,Z4,Z5; tensor from Z2,Z3,Z4,Z5) plus zero-order Z4. In particular Z2 cannot be omitted. Moving frames do not change this intrinsic jet decomposition, though their coefficients redistribute between derivative and zero-order terms.

For each full repair map T_(ell,j):Vell tensor Nj -> Ns, an actual dual z must satisfy M_s z=0, T_(ell,j)^dagger z=(id tensor Mj)w_(ell,j) for some w, and nonzero source pairing. Use full native tensor pairings or properly induced multiplicity Grams. Highest-weight bilinear self-pairing is zero and cannot serve as that adjoint. A failed receiver inclusion is much weaker than this criterion.

## 6. Evidence, review and continuation

[Evidence](../../lab/process/source-action-mixed-consistency.json) · [data-only bundle](../../lab/process/source-action-mixed-consistency-certificates.json) · [probe](../../tests/program-focus/source_action_mixed_consistency_probe.py) · [review](../../lab/process/hostile-reviews/2026-11-26-source-action-mixed-consistency-review.md).

The family test checks all32 horizontal-response basis vectors against all59 background directions and three normal/target channels: **5,664 exact full-ambient image checks**. No ambient remainder is discarded. Every spin4 eta5 and spin5 eta10 image lies in an existing certified receiver, as do their four constant columns. Those receivers are invertible throughout both owned root boxes, so these four reduced channel types have native M preimages at the actual roots. This proves the positive result without approximating the horizontal response.

The eta9 channel fails that stronger inclusion. To test the actual roots, the probe retains the exact horizontal-response error bounds. For each of two coordinate rows annihilating both old spin5 receivers, it computes

    center = sum_i y_i sum_j t_j B_ji,
    error <= sum_i epsilon_i |sum_j t_j B_ji|
             + radius (|y_i|+epsilon_i) sum_j |B_ji|.

Here all values are exact Gaussian rationals, and absolute value denotes the conservative coefficient l1 norm. Native checks prove these rows also annihilate the two nonzero constants d9 and B. Therefore they measure the full A source, and both reduced maps have four times the same row value. This is a row-level annihilation, never a claim that the constant fields vanish.

| Root | Q representative5: positive witness margin | Q representative12: positive witness margin |
|---|---:|---:|
| 0 | 0.01317820117 | 0.3402949865 |
| 1 | 0.2882231916 | 1.58833729 |

Every margin is strictly positive with the root/response uncertainties included. Since B is nonzero, wholly even and annihilated by these rows, A and B are linearly independent modulo the old odd receiver sum **within each Q copy**. No independence modulo imM, or across the two Q copies, is asserted. This proves a limitation of the old certificates, not a candidate failure.

A separate numerical discovery solve uses the corrected full A at root0/representative5 and the full native M action. Its recorded result is diagnostic only; rational-center convergence cannot certify the exact root or all four channels. At the rational center, GMRES returned info0 with relative residual8.4464343563e-11 in14 matrix-vector actions (about34 seconds). The2304-coordinate response is discovery evidence suggesting repair; it is not an exact-root preimage, a complete carrier or a physical solution.

### Reproduction and faster repeated checks

The probe moves the Casimir projection onto the small derivative/response input and fuses Gaussian-integer numerators before one native projection. All177 images of its first column agree exactly with the direct output-projection implementation. This avoids repeating expensive output operations without changing the equation or truncating a field. Family execution took about830 seconds on this run; no general speedup ratio is inferred from that one timing.

The seven-record bundle contains data only and authenticates the direct reference, all family checks, exact constants, native controls, root witnesses, N6 basis and numerical discovery record. Receiver inputs are restored from their existing committed bundles. From an empty cache:

```sh
python3 tests/program-focus/source_action_mixed_consistency_probe.py --repo . --cache _local/mixed-consistency --mode unpack
python3 tests/program-focus/source_action_mixed_consistency_probe.py --repo . --cache _local/mixed-consistency --mode replay
python3 tests/program-focus/source_action_mixed_consistency_probe.py --repo . --cache _local/mixed-consistency --mode status
```

The bounded replay recomputes native controls, constants and exact root-witness bounds, and authenticates the complete family record. It **does not** recompute all5,664 images a second time. To reproduce those independently, use `--mode family --steps 0 --output _local/mixed-consistency/family-recomputed.json` after unpacking; the explicit new output avoids resuming the completed record. The full-family procedure and native inputs are hash-bound. Numerical discovery is not an acceptance certificate.

Independent mathematical/source and hostile reviews check the mixed identity, corrected constants, channel completeness, exact uncertainty bound and exhaustive finite-block reduction. The quick20 mathematical description lenses include category theory and number theory; there is no agent per persona. These are internal reviews, not external peer review or a new full-PDE Lean proof.

- **ESTABLISHED:** four mixed reduced channel types repaired at both roots; exact noncoverage of the four remaining types by the old receivers; coefficient-parity separation; exhaustive full-M reduction to the complete even highest5 time-kernel within512 ambient directions.
- **RULED OUT:** claiming that the old receivers already settle every mixed source, or that the zero theta2 primary response makes its mixed constant vanish. No candidate, physical or GU exclusion is established.
- **NOT MODELED / UNDETERMINED:** the complete even time-kernel dimension and its root-box invertibility, remaining augmented repairs if singular, lower/higher consistency, actual propagation, physical admission and source necessity.

Next is the complete even block and both corrected sources A/B. Normal-first lower coefficients remain the alternative; their transverse derivatives, frame brackets and zero-order terms cannot be dropped. Completed horizontal and covered mixed work stays consumed.

No new action, norm, physical quotient, boundary condition or choice family is introduced. Choice budget10 families/4 obligation bundles/net6/zero source-selected predictions stays unchanged. No canon, source/physics ledger, class-C, paper, policy or scheduler change. Nov26(g) comparator suites remain proposal-only.

## 7. Joe's counterfactual memo: proposal only

The existing proposal is retained; no suite or governance change is authorized by this result. Ranked by qualitative expected time saved at the current bottleneck:

1. **Outcome-to-action table.** Distinguish a whole-block repair, an actual augmented obstruction, old-receiver noncoverage and a failed numerical search. Identical next actions do not make a test valueless if its scope, bound or reusable certificate changes.
2. **Necessary-success conditions, with source premises named.** Physical stability and weak-field requirements need an admitted domain and observable. A path to these chosen stationary roots is not automatically required by GU.
3. **Targeted dependency checks before a ten-family sensitivity sweep.** Test only a choice that can change a pending conclusion. A plus-adjoint convention is a comparator to the authenticated minus construction, not a source-authorized alternative.
4. **One matched known-theory control before physical-ghost inference.** The present exact algebraic image question does not require constructing a GR/Stelle/conformal/Dirac suite. A later control must match the constraints, quotient, pairing and observable being tested.
5. **A precisely mapped four-dimensional comparator.** Useful only for identifying dependence of a specific obstruction on the removed geometry; neither outcome transfers to GU by itself.
6. **Euclidean-base comparison.** Changes the geometry and meaning of energy; defer without a specific signature-dependent identity to test.
7. **Lower-dimensional toys.** Clifford, Hodge and grading structures change with dimension; use only when a dimension-stable mechanism and its transfer are identified.

Compared with the earlier ranking, targeted choice dependence moves just ahead of physics controls because the present bottleneck is finite M-range membership. This is a recommendation for Joe, not an applied process change or a new stop rule. Source claims, existing principles, schedules and the choice budget remain unchanged.
