---
title: Printed nonlinear transfer — exact frozen sector and the fifth-order correction obstruction
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T1
expected_delta: Decide whether the actual quadratic term and stationary-branch Jacobian inherit the linear scalarizer and frozen growth constructions
actual_delta: An exact real frozen nonlinear growing sector survives self-interaction; its literal native continuation has a nonzero defect; the actual analytic branch obstructs the fixed-leading scalarizer correction first at order h5
class_covered: Selected low-Phi printed equation with scalar mass, primary-minus K95 carrier; named frozen fixed-real-leg solutions and order-at-most38 corrections to the owned scalarizer around the actual homogeneous small-h branch
premises:
- The printed equation is distinct from the I1B Euler equation and reconstructed W2 dynamics
- The source-guided K95 Nomizu frame and low-Phi product dictionary are held
- The actual full216 homogeneous analytic branch and its first four coefficients are reused
- No unrestricted physical state domain or source-unique completion is assumed
source_bridge:
  status: conditional
  reason: Source fixes the endpoint template and full primitive translations, not this unique product dictionary, completion, or physical state domain
kill_condition: A native identity or nonzero receiver failing exact replay invalidates the corresponding scoped exclusion; neither exclusion is a source-GU falsification
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Printed nonlinear transfer

program_target: X-P1-P2
tier: T1
expected_delta: Test actual nonlinear and native lower-term transfer.
actual_delta: Exact frozen nonlinear modes; native continuation defect; actual fifth-order obstruction to the fixed-leading scalarizer correction.

**ESTABLISHED:** self-interaction does not remove one exact growing sector
of the frozen printed equation. However, its unchanged continuation fails
on the native curved background. The actual analytic stationary branch
also defeats the previous linear solution method's first correction at
order `h^5`, although the first four orders pass.

**These are two transfer results, not a nonlinear nonexistence theorem.**
The actual homogeneous branch still exists. No source, physics-ledger or
matrix verdict changes.

```gu-typed-objects
result: Printed nonlinear transfer
carrier: T in T*Y tensor End_C(S128); real primary-minus u(64,64) directions for explicit modes and receivers LAYER=ambient BRIDGE=held-printed-product-dictionary-conditional CHIRALITY=N/A
pairing: source indefinite spin pairing H; no positive physical norm selected ON=End_C(S128)
real_structure: K95 native rational orthogonal frame; vectors and bivectors sharp-skew, also grades5,10,14 in the explicit receiver test
grading: Clifford degree, not physical chirality or family index
action_owner: source-print -- selected printed endpoint, distinct from exact I1B variation and W2 construction
target: actual Q, branch Jacobian and leading scalarizer range MAP-TYPE=intertwiner
```

## 1. Scope, reuse and custody

Write the held printed endpoint as

`Rκ(T)=κT+S_g+P_gT+Q(T,T)`,
`Q(T,U)=Phi(T∧U+U∧T)/2`, `V_T U=2Q(T,U)`.

[Source prescription](source-prescription-current-2026-11-13.md) §§1–2
binds independent `g,T` and full fixed-metric primitive translations to
source draft §§5–7, eqs6.22/7.3 and p45eq9.7. SC-ACT02 concerns p45
eqs9.7–9.10; SC-ACT01/I1B and SC-ACT04/I2B remain distinct. SC-ACT06,
p65 itemx and §10, does not select an unrestricted Lorentzian Cauchy domain.
Primary-minus real-form custody is in
[source homogeneous branch](source-action-homogeneous-analytic-vacuum-2026-11-25.md)
A2 and [real-form transfer](riemann-realform-transfer-2026-11-27.md) §4.
Both printed i-anticommutators are retained by the existing engine.

Reused, not recomputed: [full nonnull decomposition](printed-equation-jets-and-symbol-2026-11-27.md),
[linear differential scalarizer](printed-differential-solvability-2026-11-27.md),
and [actual homogeneous analytic branch](printed-endpoint-analytic-branch-2026-11-27.md).
The latter gives `T_p(h)=Σ h^j u_j`, `h=1/κ`, with a convergent full216
branch near zero. Its `u4` is the printed coefficient, not W2's `t4`.

Older K2378/K2458 ordinary-Euler hook tests and K2255/K2258 polynomial
state-filter results are different carriers or consumers. No new general
selector theorem or novelty claim is made here.

## 2. Exact nonlinear frozen sector

Let `a` be a fixed nonzero real null covector. Use **raised** Clifford
vectors `c(ξ)=ξ_j γ_j/d_j`, not lower-index gamma coefficients. For
`a·ζ=0`, put `q=ζ²`, `Γ=c(ζ)` and `β=a⊗c(a)`. The owned transverse
`p=1` hook identities give

`Pζ β=−2Γβ`, `Pζ(Γβ)=−2qβ`.

These polynomial identities extend to null ζ by density. Hence

`u(ζ)=κβ+2Γβ`, `(κ+Pζ)u=(κ²−4q)β`.

Every component has the same real one-form factor `a`. Thus the full
self-wedge, including the cross terms between real Fourier quadratures,
vanishes. On `q=κ²/4`, the real part of `exp(ζ·x)u(ζ)` is an exact
solution of the **zero-source frozen nonlinear** equation. Its real
coefficients have Clifford grades1/2 and are primary-minus sharp-skew.

More generally, every real scalar solution of

`a#·∂f=0`, `(Box−κ²/4)f=0`

produces

`T=a⊗[κc(a)f+2c(df)c(a)]`.

Commuting derivatives and the polynomial identities prove the equation;
the transport condition removes the scalar Clifford part. Arbitrary sums
within this fixed-a sector retain the vanishing self-interaction.

For unit orthogonal physical-time τ and normal η of the same sign `s`,
choose `a` null and orthogonal to both. Then

`ζ=λτ+i nη`, `λ²=n²+sκ²/4`, so `λ~n`.

This construction applies to the odd-index normalized K95/K77 ports by
the reused symbol formula; the exact native curved test below is K95 only.
It rules out the claim that the printed quadratic self-interaction alone
repairs this entire frozen sector.

### Domain and control

These are analytic local solutions. They also give periodic solutions
when the scalar coordinate along η is periodic and all other spatial
coordinates are periodic, with constant fields in the remaining directions.
For fixed κ and `n→∞`, a fixed-time norm grows like `exp(λt)` while every
fixed finite initial spatial/time derivative norm costs only a power of n.
Thus no fixed finite-loss estimate can hold on a comparison state space
admitting all these periodic modes. Scaling amplitudes exponentially down
keeps any desired finite collection of initial norms small. The same
comparison holds for the explicitly unrestricted local bounded-patch modes.

**Not claimed:** a nonzero global `L²(R13)` packet in this fixed-a family.
The spatial transport condition confines Fourier support to a hyperplane.
Varying `a` with frequency can restore cross-interactions. No physical GU
state, positive energy or curved nonlinear instability follows.

The known [Craig–Steven Weinstein result](https://arxiv.org/abs/0812.0210)
uses nonlocal restrictions to obtain well-posed scalar ultrahyperbolic
problems. It remains an applicable caution about domains, not a supplied
GU prescription or an exclusion of every completion.

## 3. The literal native continuation fails

Use the authenticated rational K95 frame

`d=(1,1,1,−1,−16,8,24,48,8,8,−8,8,−8,−8)`.

Take `τ=θ3`, `η=4θ4`, `a=θ5+θ10`. Their norms are `−1,−1,0` and
pairings vanish. Put `U=c(η)β`. The engine computes the actual constant-
component connection terms, not a flat upstairs surrogate:

| Column | Nonzero components | Example receiver |
|---|---:|---|
| `Phi(Dβ)` | 8 | coefficient of `θ0 γ0γ5` = `1/32` |
| `Phi(D(c(τ)β))` | 4 | coefficient of `θ0 γ5` = `1/32` |
| `Phi(DU)` | 4 | coefficient of `θ5 γ5` = `−1/4` |

The exact κ2, λ3/4, n5/4 fixture passes both real frozen equations but
has a nonzero native lower-term residual.

There is also an analytic branch-relative statement. Write `ρ` for the
`θ5 γ5` receiver. Normalize the real mode as
`t_n=Re(i exp(ζ·x)u/n)` with phase zero at the tested point. Then
`t_n(p)=−2U`, independent of n and κ. Prescribe this literal frame first
jet; the frozen derivative/mass part cancels. Since `T_p(h)` is an actual
background solution, forcing cancels in the perturbation difference.
Self-interaction is zero, but its exact remaining point receiver is

`ρ(Rκ(T_p+t_n)−Rκ(T_p))=1/2−4ρ Q(T_p(h),U)`.

The owned `u1=−S`, and exact native computation gives `2Q(S,U)=21U`
with `ρ(U)=0`. Consequently this receiver is **`1/2+O(h²)`**, nonzero
for sufficiently small real h. This excludes the literal frozen-frame
continuation about the actual branch, not a corrected amplitude or any
other curved solution. Frame first jets exist at a point; no global
commuting-coordinate claim about the Nomizu frame is needed.

## 4. The scalarizer must be tested in the cokernel

Let Bκ be the previous right-ordered scalarizer of order39. At nonnull ξ,
its principal symbol is

`B39(ξ)=K q^19 Pξ Π0(ξ)`,
`K=∏_{a∈A}(4a) ≠0`,
`A={1,12,22,30,36,40,42}∪{−1,…,−12}`.

Here Π0 projects to the generalized-zero symbol sector. This follows from
the leading homogeneous part of the owned polynomial quotient; the
nonzero eigenspaces are annihilated. Its image has dimension8204:
8191 longitudinal zero-Jordan images and13 extra transverse volume
images. The longitudinal portion already includes the longitudinal full
Clifford volume Ω. Thus **all14 volume-valued one-forms** lie in this
image, with explicit native preimages checked.

Nonzero `V_T B39` alone is not an obstruction. A correction C of order
at most38 must solve at degree39

`Pξ C38(ξ)+V_T B39(ξ)=0`.

The necessary test is the image in `coker Pξ`.

For longitudinal `ξX`, the exact algebraic identity is

`V_T(ξX)=−Pξ[T,X]`.

For a grade1 T represented by a symmetric endomorphism L, direct Clifford
contraction gives

`V_T(fΩ)=4(Lf−tr(L)f)Ω`.

Every Clifford-even T commutes with Ω, so its volume Jacobian is zero.
Therefore symmetric-grade1 plus even T has zero cokernel action on the
entire leading range for every nonnull ξ. This is a necessary compatibility
result, not by itself a polynomial correction or nonlinear CK theorem.
The actual `u1,u3` are symmetric diagonal grade1, and `u2,u4` are grade2:
all four pass. At ξ=θ3 the leading nonzero values such as −219 and −225
are still in the symbol image and are not failures.

## 5. The actual branch breaks the protection at order five

We tested the smallest already authenticated candidate subspace: the
first six invariant basis tensors, with three grade1 and three grade2
members. All6 native linear maps close. Of the21 symmetric quadratic
maps, only `Q(B4,B4)` exits it, producing250 grade5 components. Thus the
six-space is not an invariant nonlinear sector.

The actual next coefficient is forced by the printed recurrence:

`u5=−P_g u4−2Q(u1,u3)−Q(u2,u2)`.

It has264 components:14 grade1 and250 grade5. These are not freely added
choices. For example the `θ0 γ0γ1γ2γ8γ9` coefficient is `−9/16`
(Clifford mask775). The existing full216 analytic branch supplies this
coefficient; no new branch or source action was constructed.

Take `τ=θ3`, `w=θ0 Ω` and the output receiver

`ell(Y)= coefficient of θ0 γ0γ2γ4γ5γ6γ7γ8γ9γ10γ12`

(Clifford mask6133). Exact results are

`ell(V_uj w)=(0,0,0,0,1296)` for `j=1,…,5`.

This receiver annihilates **every** image of `Pτ`. In the direct term
`−d3^-1[γ3,Y0]`, the sole possible input has odd grade11 containing3,
so the commutator is zero. In the nested term `−{γ0,Z}/2`, the sole
possible input has odd grade9 lacking0, so the anticommutator is zero.
The exact probe checks all13 Clifford-XOR source columns capable of
reaching it, not a random sample of the229376-dimensional operator.
Also `w=Pτ z` and `Pτ w=0`, with
`z=−θ0 Clifford(top without3)/2`. Hence `B39 z=K q^19 w` is nonzero.

Analyticity now implies

`ell(V_Tp(h) w)=1296h^5+O(h^6)`.

For all sufficiently small real nonzero h, no order-at-most38 correction
to the **fixed leading B39** can cancel degree39 of
`(κ+P_g+V_Tp(h))(Bκ+C)`. The previous unperturbed LC/parallel-Phi
cancellation already accounts for its curved connection terms, leaving
this new Jacobian term at degree39. At the native point the cokernel
receiver therefore cannot be repaired by that C.

**RULED OUT:** this specified extension of the previous linear
scalarization to the actual branch. **NOT RULED OUT:** another leading
symbol, a higher-order or nonlocal reduction, an independent PDE existence
argument, nonlinear curved solutions, or a physical quotient. In
particular the already-owned homogeneous analytic branch still exists.
A calibrated arbitrary grade5 translation also gives a nonzero2048
cokernel receiver, but the actual1296 result is what makes this test
branch-relevant rather than a generic warning.

## 6. A strict stable-frequency repair fails nonlinear closure

The alternative after the scalarizer test was a source-state question:
can one simply retain the stable frequencies of the frozen operator?
This uses the old coupled-support closure argument with the **actual
printed Q**; it does not introduce a physical prescription.

In orthonormal K95 coordinates take physical time τ and normal η of
norm−1, ordinary spatial σ of norm+1, and κ12. The real Fourier covectors

`ξ+=2τ+4σ+3η`, `ξ−=−2τ−4σ+3η`

have `ξ²=3`. The previously authenticated trace polarizations
`v(iξ)=12 O(iξ)+2 c(iξ)O(iξ)` are exact linear modes. Each is
oscillatory with time frequencies±2. The spatial stable band for this
trace channel is `|k_positive|²−|k_negative|²−κ²/48 >= 0`.
Each input gives4. Their sum is `6η`, for which the expression is−39.

The actual mixed nonlinear coefficient

`Phi(v+∧v−+v−∧v+)`

has29 nonzero components; its `θ0γ0` receiver is **−22080**. The common
Fourier coefficient convention here uses amplitudes v at positive
frequencies plus their conjugates, so no factors from a real-part
normalization are suppressed. Realification does not cancel this receiver:
only the two ordered +/− input pairs produce the frequency `6η`.

Consequently a translation-invariant **strict all-field spatial support
cutoff** excluding that frequency, while admitting both modes as freely
superposable first variations, cannot support a twice differentiable
small-amplitude solution family `T=εT1+ε²T2+…` through zero for the
frozen equation. At orderε², the constant-coefficient linear operator
cannot create out-of-support frequencies from T2, whereas Q(T1,T1)
has the displayed nonzero coefficient there. This is an exact
second-order contradiction for the named repair class.

**Limits:** this does not prove that a growing response is forced; the
forcing is temporally stationary and could have a bounded off-shell
response if the strict cutoff is relaxed. Auxiliary/constrained fields
outside the band, a nonlinear state manifold, different admitted
polarizations, nonlocal interactions, a physical quotient and the actual
curved endpoint remain outside the exclusion. The fixed-real-leg sector
above supplies a nontrivial zero-self-interaction countercase. The source
does not assert this cutoff, so its failure earns no source falsification
credit.

## 7. Verification, meaning and next discriminator

The [probe](../../tests/program-focus/printed_nonlinear_transfer_probe.py)
and [certificate](../../lab/process/printed-nonlinear-transfer-certificates.json)
contain179 exact native checks/maps, dependency hashes, full remainders,
u5 and receiver/support controls. All calculations use rational arithmetic.
Four [Lean algebra cores](../../Lean/GUFormalization/PrintedNonlinear.lean)
check the hook lift, self-interaction-free algebra, cokernel obstruction
and dispersion identity. Universal Clifford/range statements, analytic
h-series consequences and PDE/domain conclusions remain written proofs;
these are not full PDE formalizations.

- **ESTABLISHED:** an exact nonlinear frozen sector and two native transfer
  discriminators, including the forced fifth-order branch coefficient.
- **RULED OUT:** automatic self-interaction repair in that frozen sector;
  its literal native first-jet continuation for small h; the specified
  fixed-leading scalarizer correction around the actual branch; and the
  strict all-field stable-support repair admitting the two tested modes.
- **NOT MODELED / UNDETERMINED:** physical admission, corrected nonlinear
  curved modes, a general nonlinear neighborhood existence theorem,
  actual variable-coefficient finite-loss instability, κ1 and source-GU
  viability.

Choice budget remains10 families/4 obligations/net6/0 source-selected
predictions. This is a method exclusion plus a frozen comparison result,
not new source-level falsification credit. Source premises and class-C
representativeness remain conditional. Follow-through must remove the
now-excluded scalarizer correction from the default queue and compare a
new discriminator with the retained source-relevant alternatives.
