---
title: 'CW symmetry and state domains: an invariant core does not remove the two-sided threshold obstruction'
status: exploration
doc_type: structural-result
created: '2026-11-27'
completed: '2026-11-28'
program_target: BET-MASS-GAP
tier: T1
expected_delta: Decide the actual time-reflection and observed-Lorentz domain compatibility, classical modal spectrum
  and quadratic closure burden
actual_delta: Two-sided tempered ordinary-L2 quadratic histories fail even for inputs inside the Lorentz core; future-only
  response survives. Core has zero mass kernel and zero spectral infimum, and strict nonlinear support fails.
class_covered: Selected frozen K95 low-Phi printed descriptor; C2 complete-history solution maps admitting the exhibited
  real trace packets, with tempered quadratic coefficients and ordinary Fourier-local L2 traces. Separate branch-complete
  Lorentz-core classification.
premises:
- Fixed real kappa=12 and selected low-Phi printed dictionary, full complex bosonic carrier; actual primary-minus
  real trace witnesses
- C2 in a fixed polynomially weighted complete-history topology, or explicit tempered quadratic coefficient with
  ordinary L2 trace
- Both small input packet neighborhoods admitted independently; no instantaneous graph or translation-equivariant
  selector assumed
- Observed Lorentz covariance is correlated on horizontal and normal representations; ambient rotation is only a
  computational device
source_bridge:
  status: conditional
  reason: SC-ACT-02 supplies endpoint template, SC-META-52/53 name ultrahyperbolic/shielding debt; none selects
    this physical state rule, norm, time-reflection invariance or all input patches.
kill_condition: Failed actual kernel/vertex/descriptor binding invalidates affected claim; nonzero threshold mean
  excludes the stated two-sided history class only. Narrowed inputs, time-oriented domains and changed topologies
  remain separate.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Lane-C context only; no matrix cell, ledger verdict, class-C or bet-wide kill
---

# Time symmetry and finite norm impose a new cost on the CW repair

program_target: BET-MASS-GAP
tier: T1
expected_delta: Test symmetry/domain compatibility and actual nonlinear forcing without constructing a physical norm.
actual_delta: The Lorentz core retains the two-sided tempered-L2 obstruction; future-only completion remains open. No physical mass-gap verdict.

**ESTABLISHED:** the largest branch-complete observed-Lorentz-invariant part of the common frozen CW domain is `N>κ²/4`, with the modewise null exception specified below. Its auxiliary modal mass has no zero eigenvector but has zero spectral infimum. Actual interactions leave strict core support. More strongly, two real core-admitted packet directions force a quadratic response whose unique two-sided tempered history is not ordinary Fourier-local L2 at a time slice.

**RULED OUT:** the declared C2 complete-history class admitting these packets, with tempered second variation and ordinary coefficient-L2 trace; also strict all-field nonlinear core support. This does not exclude every nonlinear CW completion or all GU*.

**NOT MODELED / UNDETERMINED:** source physical state/quotient/current, physical mass operator or quantum gap, changed infrared norm, narrowed packet admission, non-C2 completion and curved/K77 transfer. The existing future-only boundary survivor is unchanged.

```gu-typed-objects
result: CW symmetry/domain and actual threshold response
carrier: T*Y tensor End_C(S128), complex dimension229376 LAYER=ambient+observed BRIDGE=selected-printed-dictionary-and-correlated-normal-representation CHIRALITY=N/A
pairing: ordinary positive coefficient L2 and auxiliary modal norm, not physical energy ON=declared_complex_frozen_state_domain
real_structure: K95 primary-minus real trace controls; no K77 or quantum transfer
grading: Clifford degree only, not physical weak chirality
action_owner: source-print -- selected low-Phi endpoint realization; no W2 or wedge Euler substitution
target: complete-history state admissibility MAP-TYPE=restriction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). The observation contraction, 2+1/chiral decomposition and Krein quotient are not replaced by an auxiliary modal mass or an ordinary coefficient norm. This is a classical state-domain test, not a proof about a physical quantum Hamiltonian.

## 1. Custody, selection and outcomes fixed before execution

Basis `5ccd2ed453e16be535acb18ec927d50080730416`; run opened November27, completed November28. Mandatory LC counter123: all three bets had18 remaining; MASS-GAP selected for the shared state-space/positivity burden. No discovery result is imported into B-lane matrix verdicts. Strongest eligible alternative is the already specified negative-output-factor CW vertex, retained as the next ordinary B test. Wedge budget3/3 and CW step2b budget2/5 remain unchanged.

Source: SC-ACT-02, draft p45 eq9.8 (endpoint template, not unique low-Phi choice); SC-ACT-06 p65 item x (reduced Euclidean ellipticity); SC-META-52 TOE01:17:10 (ultrahyperbolic debt); SC-META-53 TOE01:22:30 (uncertain compact shielding mechanism). No source claim fixes the state class tested here. [Craig–Weinstein](https://arxiv.org/abs/0812.0210v3) supplies a scalar linear nonlocal-constraint precedent, not the nonlinear full-system conclusion below. Public abstract checked November28; no novelty claim is made.

Reuse: [full descriptor/domain](cw-fullsystem-domain-2026-11-27.md), [frequency-locked graph obstruction](cw-nonlinear-completion-2026-11-27.md), [regular future boundary](cw-one-sided-boundary-2026-11-27.md), [uniform boundary estimate](cw-bilinear-boundary-estimate-2026-11-27.md). The new premise is **two-sided tempered complete history**, replacing the earlier instantaneous graph/translation-covariance premises. The new actual input fixture puts the old resonance inside the Lorentz core. No full symbol census, old Jordan classification or positive-metric search is repeated.

Advance outcomes: a nonzero native threshold mean plus the divergent trace excludes the stated history class; a zero mean retains cancellation. Nonzero off-core Q excludes strict support, but an invertible static response remains a survivor. Equation symmetry and state-domain symmetry are tested separately.

## 2. The observed-Lorentz core and its classical mass spectrum

Write spatial frequency `ξ=(p,n)`, `N=n²`, `r²=|p|²+N`. The full owned shell set is

`A={1,12,22,30,36,40,42,-1,...,-12}`,
`ω_a²=|p|²+N+κ²/(4a)`, `M_a²=N+κ²/(4a)`,
`Ωκ={r²>κ²/4}`.

Observed Lorentz acts on the horizontal covector and the normal covector through the actual correlated Sym² representation. The normal components are not inert; their indefinite square N is invariant. The simultaneous form/Clifford action preserves the frozen canonical P,Q tensors. This is not an unfrozen curved-domain theorem.

For a timelike horizontal orbit, a rest point has p=0; its whole orbit stays in Ω precisely when `N>κ²/4`. A spacelike orbit reaches ω=0, where `r²=-κ²/(4a)≤κ²/4`, outside Ω. A nonzero null orbit can approach p=0 without reaching it under a finite boost: the sole extra modewise case is `a=-1,N=κ²/4`, with nonzero horizontal lightlike momentum. Other shells at the same spatial point have timelike rest points outside Ω, so this exception is not branch-complete.

Consequently the maximal **branch-complete** common support is

`D_core={N>κ²/4}`.

All M_a² are positive there; the minimum shift is the a=-1 shift `-κ²/4`. On the auxiliary direct-sum modal Hilbert space, multiplication by M_a² on its maximal domain is nonnegative selfadjoint with zero kernel. The exceptional massless level has Lebesgue measure zero (`dN≠0` at positive N), so adding that level produces no nonzero ordinary Fourier-L2 state. A distributional carrier on it is a different choice.

Yet zero is in the spectrum: normalize smooth a=-1 modal packets in `0<N-κ²/4<ε`, whose nonzero polarizations exist by the full-symbol result. Then `||M²u||≤ε` and `||Mu||≤√ε`. Thus **no massless L2 eigenvector and no positive uniform modal gap** coexist. Adding `N≥κ²/4+ε` creates a modal gap √ε by changing the support premise. It is not a derived quantum gauge gap, and both temporal signs remain.

## 3. A nonresonant control: core support is not nonlinear closure

Use κ12 and a positive normal orthonormal axis e4 in the held D=diag(-1,+1,+1,+1;+1×6,-1×4). This axis is not index4 of a different nonorthonormal native chart. Set

`ξ=(83/13)τ+(86/13)e4`, `ξ²=3`, `N=7396/169>36`.

For ζ=iξ, q=ζ²=-3, let `L=ζ⊗cζ/q`, `O=Φ1-L`, `V=cζ O`, `v±=12O±2V`. These are actual opposed trace-shell kernels, conjugate to one another, with primary-minus real quadratures. The direct native calculation checks

`V∧V=-q O∧O`, `Φ(O∧O)=264O+312L`,
`F=Φ(v+∧v-+v-∧v+)=69696O+82368L`.

The θ1γ1 receiver is69696. Unit Fourier characters give the real field `e^{iξx}v+ + e^{-iξx}v-=2Re(e^{iξx}v+)`; using Re alone divides this force by4. Its sum momentum iszero, outside core support. Small opposed smooth packets have a nonzero convolution nearzero, separated from same-sign sums, so strict full-field support is impossible for regular nonlinear families admitting them.

**Control survivor:** `Lκ(0)=12I`, hence `W=-F/12=-5808O-6864L` is a regular static particular. No forced instability or massless homogeneous state follows from this off-support force. This is why support violation alone cannot settle the repaired domain.

## 4. The actual resonant interaction is also inside the core

Rotate the previously certified resonant pair by the proper positive-plane ambient transformation `θ1,γ1→θ4,γ4`, `θ4,γ4→-θ1,-γ1`. It fixes time τ0 and negative normal η10. It preserves the held metric, Hodge, canonical tensors and primary-minus real structure. This is a **computational ambient rotation**, not an observed physical Lorentz transformation mixing horizontal and normal coordinates. Direct sparse P,Q replay binds the transformed inputs, not merely an analogy.

The new pair is

`ξ±=±(26/3)τ ±(28/3)σ_N +3η`,
`σ_N²=+1`, `η²=-1`, `N=703/9>36`, `p_H=0`.

Both are actual a=-12 trace modes; full small13-dimensional spatial neighborhoods remain in D_core. Their sum remains `K0=6η`. Writing R for the ambient rotation and `ell_rot=ell_b R^-1`, direct checks give

`F_rot=R F_owned`, `ell_rot F_rot=104448`,
`ell_rot U F_rot/6=104448`, `ell_rot V F_rot/6=0` at K0.

Because R fixes τ and K0, it commutes with the time symbol, output symbol and regular threshold coefficients U,V. The probe separately checks the actual U-force kernel and V-force chain, without a dense inverse.

On an output collar let `δ=-r(K)²-36>0`, `λ=√δ`. The owned regular descriptor is

`L(z,K)^-1=(U+zV)/(z²-δ)+H`,
`Π=VA_t`, `N_c=UA_t`, `N_c²=δΠ`, `N_c V=U`.

For x=ΠT define scalar diagnostic receivers (not physical observation)

`z=ell_rot x/6`, `p=ell_rot N_c x/6`,
`g0=ell_rot VF/6`, `g1=ell_rot UF/6`.

Then `z'=p-g0`, `p'=δz-g1`, so

`z''-λ²z=-(g1+g0')`. (1)

## 5. Complete-history obstruction, without an instantaneous graph

Choose independent nonnegative smooth compact amplitudes on sufficiently small neighborhoods of the two inputs, positive on smaller patches; add conjugate patches for real fields. Other pair sums are separated from the output collar. For the mixed temporal phase `ν(k,K)=ω(k)-ω(K-k)`, `ω²=r²-3`, the inherited derivative is `∂_(k,η)ν=-9/13`. Coarea therefore gives

`g_j(t,K)=∫ρ_j(ν,K)e^{iνt}dν`,

where ρ_j is smooth and uniformly compactly supported. The actual g1 numerator has positive real value104448 at the center. Shrinking patches gives a common positive-volume ν=0 coarea subpatch and a uniform lower bound `Re ρ1(0,K)>c0>0`. Thus g_j are uniformly Schwartz in time and

`J1(K)=∫R g1(s,K)ds=2πρ1(0,K)`, `Re J1≥2πc0`. (2)

A nonzero vertex alone would not prove this packet statement; phase submersion, positivity and the common subpatch are required. Conjugate reality does not cancel the isolated output contribution.

For each λ>0, the unique tempered solution of (1) is

`z(t,K)=(1/(2λ))∫R e^{-λ|t-s|}[g1(s,K)+g0'(s,K)]ds`. (3)

The Green kernel for `∂t²-λ²` is `-e^{-λ|t|}/(2λ)`; its derivative jump is1. Uniqueness follows since neither homogeneous exponential is tempered at both ends, or by temporal Fourier division by `-(ν²+λ²)`. For spatial distributions first work on compact subcollars bounded away from δ0, where the inverse has controlled derivatives; this fixes the solution throughout the open δ>0 side.

Integration by parts at t0 gives

`z(0,K)=J1(K)/(2λ)+E(K)`,
`|E|≤(1/2)∫|s g1|ds+(1/2)∫|g0|ds`,

uniformly in K. Since `dδ(K0)=12dK_eta`, a positive-measure tangential patch yields

`Re z(0,K)≥c/√δ`,
`∫|z(0,K)|²dK ≥ c'∫_0^ε dδ/δ =∞`.

An ordinary coefficient-L2 full state would have an L2 projected receiver, because Π and ell_rot are smooth bounded matrices on the compact collar. Complementary modes cannot cancel an already projected receiver. Terms supported exactly on δ0 cannot cancel the open-side divergence and are not ordinary L2 functions.

**Theorem, precise nonlinear class:** consider a solution/selection map based at the frozen equilibrium T=0, whose first derivatives are the two displayed linear trace-packet solutions. Twice differentiating the actual equation must give `L W=-Q(f,g)` for its mixed second variation W (with Q the polarized force used above). No such map can be C2 into a fixed history space

`X_M={T∈C(R_t;L2(output collar)): sup_t(1+|t|)^(-M)||T(t)||_2<∞}`

for finite M, with the equation twice differentiable on those directions. More minimally, it suffices that the mixed second variation is temporally tempered and has an ordinary coefficient-L2 trace at t0. No instantaneous graph or spatial translation-equivariant selector is assumed. Arbitrary homogeneous additions are already accounted for by tempered uniqueness.

**Essential limitation:** bounded finite-amplitude trajectories, or C2 dependence on each finite time interval, do not imply this complete-history derivative premise. Secular parameter derivatives can violate a global bound. Non-C2 or weaker-history completions are not excluded. A physical positive-unitary realization would face the theorem only after its regular nonlinear map, norm-to-coefficient embedding and admitted packets were established.

## 6. The actual antilinear symmetry and retained escapes

The owned Θ reflects horizontal spacetime and conjugates amplitudes. It is a covariance of the selected P,Q, and preserves D_core as a set. It sends a free future decay `e^{-λt}` into a future-growing `e^{+λt}` at transformed momentum. Therefore the full future-no-growth prescription retaining arbitrary decaying states is not Θ-invariant, despite equation covariance.

A single domain closed under Θ and future-tempered has past-tempered histories too. If its C2 quadratic coefficient has the stated complete-history regularity, §5 applies. It cannot retain all tested inputs with ordinary L2 traces. Θ may instead exchange separate time-oriented domains; the future-only survivor and its uniform local boundary estimate remain valid. A union of two prescriptions is not automatically one linear/Hilbert domain or C2 manifold.

The ambient rotation in §4 does **not** commute with Θ: the rotated two-packet field is not asserted pointwise Θ-fixed. The theorem requires independent admission of its packet directions. A restriction to pointwise Θ-fixed inputs needs its own symmetrized vertex calculation and is not ruled out here. Set invariance of a domain is distinct from fixing every state.

Other retained escapes: remove the tested input patches; enforce a genuine zero-mean vertex/cancellation rule; change infrared topology so δ^-1/2 is admitted; allow histories growing at one end; weaken C2 history regularity. These are named costs, not adopted choice families or source predictions. Restricting to the Lorentz core alone does not suffice, because §4 lives inside it.

## 7. Verification, inference limits and continuation

76 exact finite checks authenticate prior dependencies, directly evaluate two new sparse actual vertices and the rotated scalarizer forcing jet, and calibrate the Green jump, nonzero-mean pole, zero-mean bounded control and time-reflection of a free decay. The integrable control force `e^{-|t|}-2e^{-2|t|}` has zero total and a finite limit; it prevents a blanket claim about all forcing. It is a calibration, not the actual smooth packet force. A correlated Sym² boost changes normal components while preserving their DeWitt norm.

Five Lean cores check reversal-closure logic, scalar mass positivity/margin, residue lower-bound arithmetic and exact rational fixture values. They do not formalize the full operator, orbit classification, coarea, PDE or spectral-measure proof. Independent mathematical and hostile review owns those written implications. Verification differs from validation against source intent.

Historical candidate choice budget remains10 families/4 obligations/net6/0 source-selected predictions. No new repair is adopted. In Joe27q language: **FALSIFIED** for the precise two-sided regular completion class and strict all-field core; **SURVIVES** for the prior local future boundary test; **INCOMPLETE** for a physical selection law. SOURCE GU, all class C and the entire MASS-GAP bet are not falsified.

The next ordinary B discriminator remains the actual negative-factor interaction at κ12, output a=-2, K²18, inputs k=5K/2 and l=-3K/2 with factors(-1,+1) and opposite frequencies squared153/2. Test its projected numerator before any degenerate estimate. This LC result is context for that work, not automatic B physics evidence. No repeated norm search or fourth wedge wave is warranted by the present result.
