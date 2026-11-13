---
title: "Native weak-action transport and effective chirality conditions"
status: exploration
doc_type: structural-result
created: '2026-11-13'
program_target: X-P1-P2
tier: T2
expected_delta: Test complete source-category membership without discarding independent fields or changing observation silently
actual_delta: "Constrained - exact weak-action fork, correlated grades and conditional effective bounds"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
bears_on: [SC-OP-04, SC-OP-05]
canon_verdict_change: none
---

# Native weak-action transport and effective chirality conditions

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Source-correct weak action and density-duality compatibility
actual_delta: Constrained - exact weak-action fork, correlated grades and conditional effective bounds

```gu-typed-objects
result: Native weak-action transport and effective chirality conditions
carrier: full independent vector-spinor and scalar with q retaining horizontal pullback and gamma trace LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: independent density-dual rows; positive norm assumed only for the stated conditional analytic bounds ON=declared_carrier
real_structure: complex Clifford identities; K77 real and K95 quaternionic structures separately typed; finite reduced-Clifford controls only
grading: ambient, horizontal, normal and auxiliary grades explicitly transported
action_owner: repository-construction -- structural comparison of source-print ingredients; no selected full action
target: native observation and weak action MAP-TYPE=intertwiner
```

## Source custody

Uses the primary source register/extractions and the existing November12 full-symbol/current notes, Pati–Salam branching, August30 real Spin(6,4) observation-sector theorem, HE1 and chirality-real-form results. The old guide's unconditional quaternionic parent is superseded here: SC-GRP-02 ASSERTS U(64,64) (2021 pp24–25); SC-GEO-51 ASSERTS the same (2025 TOE 02:41:57). This is distinct from a chosen Spin reduction and its normal weak subgroup.

SC-GRP-03 ASSERTS the simultaneous normal reductions/intersection (2021 p29); SC-GRP-06 ASSERTS no internal symmetry groups (p64); SC-FER-07 ASSERTS normal-spinor quantum numbers (p27). Use the already-derived normal Spin(6,4), its compact Spin(6)×Spin(4), and SU(2)_L in Spin(4). No independent internal group or repeated16/144 census is introduced. SC-FER-05/06 ASSERT the correlated labels (pp51–52); their collision with9.16 remains open. SC-GEN-56 ASSERTS an opposite-half package in the2025 UCSD edition, not a reconciled replacement. SC-CHI-01/04 ASSERT a nonchiral total and effective observed split; SC-CHI-02 and MAS-01 ASSERT only the stylized m=R/4 toy. SC-CHI-52 ASSERTS sufficiently-low-mass decoupling without supplying a numerical threshold. SC-GEN-01 DISAVOWS simple triplication; META-05 cautions against mass/flavor identity. OP04 is candidate-strength and OP05 UNCERTAIN admits alternatives.

The current result uses the complexified full Clifford carrier S (rank s, s=128 in the standard14-dimensional complex Dirac model). Real forms are not identified: K77/K95 require their own real structures. The paired normal16/144 real theorem is reused, not reproved or made a physical count.

## 1. Fixed action categories and exact six-spinor intertwiner

At one point along a nondegenerate section write V*=H*⊕N*, ranks4,10; choose the adapted splitting so literal pullback is P_H. Let

 E=(V*⊗S)⊕S, O(ζ,ν)=(b=P_Hζ,ν),
 q(ζ,ν)=(b,τ=Γζ,ν), K=ker q=ker Γ_N⊂N*⊗S.

The November12 theorem already establishes K as the largest normalized-tangential-evolution invariant kernel inside kerO for the time-invertible natural family. Its quotient has6s dimensions, with stable zero-SE locus c_±=−a_±/12. We do not repeat that result.

Let t be a normal Spin bivector, r its vector action. Our convention is [t,c(v)]=c(rv).

**Category F (fixed spin-only gauge action):** T_Fζ=(1⊗t)ζ, T_Fν=tν, with form legs and Γ fixed. Horizontal Clifford multiplication commutes with t, so O intertwines. But

 qT_F−diag(t,t,t)q=(0,D_tζ_N,0),
 D_tζ_N=Σ_a[c(n_a),t]ζ_a.

A possibly non-diagonal action on the6s receiver exists iff D_t|K=0; a clever receiver representation cannot bypass kernel invariance. In fact all normal spin-only endomorphisms u preserving K satisfy

 c(n_a)u c(n_a)^−1=B, independently of a.

This follows by factoring Γ_N(1⊗u)=BΓ_N, using the surjectivity of Γ_N. Equivalently u commutes with every c(n_a)^−1c(n_b). For an irreducible complex normal Dirac module this is exactly the span of its two chirality projectors (with arbitrary spectator endomorphisms if allowed). Intersecting with the normal spin Lie algebra gives zero: no nonzero normal bivector satisfies it. This classifies the obstruction, not merely one failed weak generator.

**Surjective SU(2) defect control.** Normalize the four compact weak Clifford directions to γ_i²=1 over C. Take

 t=(γ_1γ_2+γ_3γ_4)/2,
 k_1=γ_1^−1u, k_5=−γ_5^−1u, other k_a=0,

where direction5 belongs to the normal6-plane fixed by SU(2)_L. Then Γ_Nk=0, but

 Γ_NT_Fk=(γ_1tγ_1^−1−γ_5tγ_5^−1)u=−γ_1γ_2u.

The last matrix is invertible. Thus D_t|K is onto S. The defect survives with zero curvature and zero mass; it cannot be estimated by C|R| on all hidden fields. This obstructs only fixed-spin-only descent through this q, not the effective source mechanism.

**Category G (simultaneous geometric form+spin action):** T_Gζ=(r⊗1+1⊗t)ζ, T_Gν=tν. Clifford covariance gives ΓT_G=tΓ and P_HT_G=tP_H. Hence

 qT_G=diag(t,t,t)q.

All three q slots carry the inherited normal spin action. This is the actual geometric positive control. Every horizontal coefficient in the6s symbol commutes with t: c_H, J_H, i_ξ and the scalar-on-ambient-half weights. Therefore the entire tangential principal pencil intertwines on q, including independent a_± and c_±=−a_±/12. Local weak covariance additionally uses the normal connection on BOTH form and spin factors; omission of its form part returns Category F. This result authenticates the normal geometric subgroup, not full U(64,64) invariance.

**Category M (moving Clifford/epsilon transport):** for invertible spin U, set c^U(v)=Uc(v)U^−1, Γ^U=UΓ(1⊗U^−1), and q^U=(P_H,Γ^U,1). Then

 q^U diag(1⊗U,U)=diag(U,U,U)q.

This is exact covariance between moving observation tensors. Its differential version must include derivatives of U and the transported connection. A simultaneous geometric Spin action realizes Category G; generic parent U acts on the Clifford embedding instead. Holding q numerically fixed after transporting only fields discards the term that proves covariance. Epsilon may supply such transport when its actual source law is used; it does not automatically select the reduction, real structure or physical current.

## 2. Stronger optional result: the maximal spin-only weak-invariant hidden kernel

This theorem assumes the chosen native compact reduction N_C=W6⊕W4, W4=A2⊗B2 under SU(2)_L×SU(2)_R. It does not assume a physical compactification. Let S_a be the half of S on which SU(2)_L is fundamental (with multiplicities), and S_i the equal-rank half on which it is trivial. Write Γ_N=Γ6+Γ4.

The largest SU(2)_L-spin-only-invariant subspace inside K is

 K_core=ker Γ6 ⊕ ker(Γ4:W4⊗S_i→S_a),

with the entire W4⊗S_a component zero. Here kerΓ6 lies in W6⊗S. Consequently dimK_core=5s+3s/2=13s/2 (versus dimK=9s).

Proof. K_core is the intersection of the group translates of K. Average the conjugated trace equation U^−1Γ_NU: Γ6 is invariant, while the rotated4-vector has zero average, giving Γ6=0; the remaining condition is Γ4(1⊗U)ζ4=0 for every U. On S_i this is simply Γ4ζ4=0; Γ4 is onto S_a, so its kernel has dimension4(s/2)−s/2=3s/2. On S_a, identify the weak factors as A_form⊗A_spin: Γ4 contracts these two2-dimensional factors. The linear span of SU(2) matrices is End(A_spin); contraction after every such matrix is nondegenerate on the whole tensor, forcing ζ4,a=0. Conversely these conditions visibly suffice. The6-plane contraction is surjective, giving5s.

All horizontal Clifford matrices preserve K_core, as do the scalar-on-ambient-half coefficients. Thus the original time-invertible natural evolution preserves K_core. Combining with the already-proved maximal evolution kernel K inside kerO, any value-only output that both retains O and permits spin-only weak action plus autonomous tangential evolution has rank at least

 15s−13s/2=17s/2.

The quotient by K_core attains this joint-invariance bound. IMPORTANT: this says both actions descend separately; it does NOT say the descended weak action commutes with evolution. The original fixed-spin-only pencil still has a covariance defect. A larger receiver is not a repair of gauge covariance. Category G retains the smaller6s receiver and genuine principal equivariance.

## 3. Transport the correlated gradings rather than guessing slot labels

Choose normalized commuting volume operators χ_H,χ_N with squares1; Ω=χ_Hχ_N, up to the declared normalization sign. χ_H anticommutes with horizontal Clifford matrices and commutes with normal ones; χ_N has the opposite rule. Both spin-only gradings preserve K, despite nonzero weak bivectors not doing so. Their actual quotient actions are

 C_H^q(b,τ,ν)=(χ_Hb, χ_H(τ−2Γ_Hb), χ_Hν),
 C_N^q(b,τ,ν)=(χ_Nb, χ_N(2Γ_Hb−τ), χ_Nν).

These square to1, commute, and commute with Category G normal weak action. In coordinates σ=τ−Γ_Hb=Γ_Nζ, they become

 C_H^q=diag(χ_H,χ_H,χ_H),
 C_N^q=diag(χ_N,−χ_N,χ_N).

Their product is diag(Ω,−Ω,Ω). The auxiliary odd source grading Gsrc=diag(Ω onζ,−Ω onν) therefore transports to diag(Ω,−Ω,−Ω) on q. This derives the trace crossing used in November12 and separates it from printed ambient labels. The real normal conjugation exchanges complex normal halves, as already proved in the August30 note; selecting a single complex grade is not by itself an admissible real sector.

No statement here identifies C_H^q with a conserved physical chirality of the full source dynamics. In particular weak commutation and kinematic chirality do not prove a V−A current or source-selected luminous/dark projector. The full Dirac normal-spinor carrier contains both horizontal chiralities. A physical readout requires more than its branching character; masses/flavors may mix.

## 4. Low-curvature source toy: exact response and a nonuniformity control

Use only the stated stylized m=R/4 coupling, and supply an explicit common closed-domain resolvent assumption rather than demanding exact off-shell decoupling. After identifying the two equation receivers on a frozen spectral problem, write

 L_m(z)=[[A(z),−mI],[−mI,B(z)]],
 ||A^−1||≤a, ||B^−1||≤b, |m|²ab<1.

Schur complementation gives

 (L_m^−1)_LR=A^−1 m (B−m²A^−1)^−1,
 ||(L_m^−1)_LR||≤|m|ab/(1−|m|²ab),
 ||(L_m^−1)_LL−A^−1||≤|m|²a²b/(1−|m|²ab).

The reverse block has the same cross bound. Proof uses the Neumann inverse of I−m²B^−1A^−1; no commutativity of A,B is needed. For a bounded variable coupling M the same proof uses ε=||M|| and the corresponding two direction maps, assuming their norms≤ε. It cannot identify ε with a physical curvature scale absent the source-to-action map and units.

If a,b≤1/Δ, the cross response is at most |m|/(Δ²−|m|²); the useful dimensionless parameter is |m|/Δ. Thus source-toy effective decoupling is uniform on a declared gapped resolvent region. It is not uniform near the uncoupled characteristic locus: for A=B=zI the exact cross block is m/(z²−m²). At z=2m it is1/(3m), and its ratio to the diagonal block is1/2 for every nonzero m. At fixed nonzero z the cross block is O(m). Degeneracy therefore defeats a universal low-curvature estimate without refuting an effective regime with specified scales.

A time-domain alternative does not require a spectral gap: on a common positive Hilbert realization with block-diagonal self-adjoint H0, bounded self-adjoint off-diagonal V and real m, set U(t)=exp[−it(H0+mV)]. The perturbed evolution is unitary, and Duhamel gives ||P_R U(t)P_L||≤|m| ||V|| |t|. This is a conditional norm estimate, not an assertion of source physical positivity. Small mass over a fixed time and uniformly small mixing for arbitrarily long time are different claims.

## 5. What a weak-current leakage claim actually needs

Keep barred fields independent. If a specified current vertex V_T measures the hidden sector only, and a source in L generates right amplitude bounded by δ=|m|ab/(1−|m|²ab), then a matched bounded dual response gives a pure right-sector bilinear bound O(δ²); a mixed vertex generally gives O(δ), and a direct unsuppressed wrong-sector vertex gives O(1). These distinctions survive family mixing. No probability or positive norm is inferred merely from independent barred polarization.

Exact current descent through q would additionally require V_T ker q=0 and (ker barq)V_T=0, for the actual barred observation barq. That optional exact property is not imposed on SC-CHI-01/04/52. Effective current suppression instead requires quantitative bounds on the actual solution maps and vertex blocks; neither the group character nor a small scalar coefficient alone supplies them.

The first unproved native bridge is now more specific than “weak map missing”: the source must identify whether its connection variation acts geometrically on the normal form leg, or via a moving Clifford/epsilon realization, when the full independent ζ/ν carrier is reduced to q. Category F fails by the surjective algebraic defect; G and M explicitly survive. After that choice the map δA_weak→δD (including form connection, epsilon and dual variation) must be compared to the displayed9.18 current. The six-spinor pencil proves the geometric principal intertwiner, but does not identify that source Euler-current map. A physical luminous/dark or wrong-handed projection and a common domain then determine whether the toy suppression applies. No new action, torsion substitution or exact-autonomy requirement is smuggled into that comparison.

## Exact checks and acceptance

1. Clifford control on6 normal directions, with a4-plane weak factor and2 inert directions: verify su2 brackets, defect witness and full-rank invertible defect; this is a low-dimensional faithful local algebra control, not a dimension14 proof.
2. Compute common-kernel rank for Γ2,Γ4 and Γ4 times the weak matrix algebra: expected dimension5s/2 for normal dimension6, generalizing13s/2 for normal dimension10.
3. Check q chirality identities, involutions and commuting product with a minimal even/even Clifford split; prove general formulas as above.
4. Symbolic2×2 inverse verifies the resolvent countercontrol at z=2m, plus m=0 and fixed z controls.
5. Exact zero-SE two-sided repair, normalized evolution, quotient transport and bilinear-congruence controls are in the same replay; the universal Category G coefficient argument uses the established full6s formula.

None of these checks manufactures the source current or analytic domain. The proofs above, not finite ranks alone, support the stated general dimensions and action classification.

## 6. Joint result with Test B: weak stabilizer of the concrete repair

Test B's §5 now owns the detailed constant left/right equivalences, q transport, independent-bar congruence and current limits for its two one-tensor repairs. This subsection supplies the actual weak criterion. Let v be the added non-null vector and A=c(v); avoid confusing this vector with a weak generator t. Under Category G,

 [t,A]=c(r_t v).

Clifford multiplication is injective on vectors, so A is a fixed-background weak intertwiner exactly when v is weak-fixed. The invariant ambient-vector subspace for the chosen native normal compact reduction is

 V^{SU(2)_L}=H⊕W6,

where W6 is the positive normal6-plane and the negative normal4-plane W4 is the real fundamental quaternion module. No nonzero vector in W4 is invariant. A nonzero weak Lie generator acts invertibly on W4 (its square is a negative nonzero scalar), so a vector with nonzero W4 component has zero weak Lie stabilizer.

Consequently a negative-norm normal trace vector cannot supply a fixed-weak repair: it cannot belong to positive-definite W6. This remains true for every chosen maximal-compact6+4 splitting with that signature; one need not assume the trace is already a pureW4 vector. The statement is conditional on the actual source-to-normal transport preserving that negative norm, since the existing metric-trace normalization and global transport have their own custody. Gauge-rotating the vector and weak reduction together preserves the relative obstruction. Moving A as a tensor restores covariance across backgrounds, not invariance of a fixed background.

Two concrete algebraic survivors remain: a nonnull v∈W6, or a nonnull horizontal v∈H. The first costs an additional invariant-normal-direction selection; the second costs a preferred Lorentz direction. Neither is derived by the source. Both retain geometric weak equivariance, printed-support repair and the frozen6s stable zero-SE principal dynamics, by Test B's exact scalar-field/equation-row equivalences. A raw qD kernel defect alone does not refute this: normalized evolution uses the transformed time row. For moving v the principal result is pointwise; exact differential equivalence additionally carries derivatives of A and the transported domain. These are structural survivors, not source action ownership or physical weak symmetry breaking predictions.

This joint result is stronger than either standalone test: the already-available negative metric trace does not furnish the fixed-weak tensor repair, while the one-tensor repair category remains nonempty and has explicit costs. No class-wide kill or new physical-current inference follows.

## Evidence and acceptance

- Primary matrix and exact labels: `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` and `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`.
- Full source-shaped carrier and stable locus: `explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md`.
- Independent bars, current, coordinate and grade custody: `explorations/conditional-build/source-current-grading-membership-2026-11-12.md`.
- Existing branching and real observation result: `lab/active-research/pati-salam-chain-verification.md` (branching only; its old real/complex count is not reused) and `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md`.
- Paired result: `explorations/conditional-build/source-degree-duality-compatibility-2026-11-13.md`.
- Replay: `tests/program-focus/source_weak_duality_probe.py`; retained evidence: `lab/process/source-weak-duality.json`.

Independent mathematical/source review and exact supporting/contrary controls
support conditional T2 acceptance. Universal claims rest on the written proofs,
not sampled ranks. No Lean, external-expert certification, source/canon verdict,
physical prediction or class-C decision is claimed. Matrix18/18 remains
constrained; its joint realization remains open.
