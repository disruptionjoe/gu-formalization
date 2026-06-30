---
title: "OC2: Weighted Fredholm Parametrix for D_GU on Noncompact Y^14"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "oc2-y14-weighted-fredholm-parametrix"
verdict: "CONDITIONAL_TAU_DISCRETE_SECTOR_THEOREM; FULL_UNPROJECTED_Y14_FREDHOLM_NOT_DEFENSIBLE"
owned_path: "explorations/analytic-index-fredholm/oc2-y14-weighted-fredholm-parametrix-2026-06-23.md"
---

# OC2: Weighted Fredholm Parametrix for D_GU on Noncompact Y^14

## 1. Scope

This note pushes OC2 past the formal `Fred_H -> KSp` statement and isolates the analytic
operator package needed for `D_GU` on noncompact `Y^14`.

Inputs inspected:

- `explorations/analytic-index-fredholm/oc2-analytic-fredholm-ksp-upgrade-2026-06-23.md`
- `explorations/analytic-index-fredholm/oc2-h-linear-fredholm-y14-2026-06-23.md`
- `explorations/analytic-index-fredholm/oc1-noncompact-atiyah-jannich-2026-06-23.md`
- `explorations/signed-calm-jordan/signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md`
- `explorations/representation-theory-noncompact/oq-weyl3-root-wall-plancherel-2026-06-23.md`
- `explorations/vz-evasion/vz-schur-complement-2026-06-23.md`
- `explorations/vz-evasion/vz1-schur-complement-symbol-2026-06-23.md`
- `explorations/vz-evasion/vz1-schur-vertical-extension-2026-06-23.md`
- `explorations/vz-evasion/vz-oq1-sr-squared-identity-2026-06-23.md`
- `explorations/vz-evasion/vz-oq2-lower-order-curvature-2026-06-23.md`
- `explorations/vz-evasion/vz-subprincipal-symbol-rs-2026-06-23.md`
- `explorations/vz-evasion/vz-f5-curvature-check-2026-06-23.md`
- `explorations/vz-evasion/vz-f6-eft-decoupling-2026-06-23.md`

Additional relevant checks inspected because they directly affect `P_disc`:

- `explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md`
- `explorations/representation-theory-noncompact/rc1-discrete-series-verification-pack-2026-06-23.md`
- `explorations/representation-theory-noncompact/rc3-delta-n-spectrum-gl4r-2026-06-23.md`
- `explorations/representation-theory-noncompact/rc3-harish-chandra-c-function-2026-06-23.md`
- `explorations/representation-theory-noncompact/rc3-root-multiplicity-bc1-2026-06-23.md`
- `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`
- `explorations/analytic-index-fredholm/n5-ind-h-analytic-conditions-2026-06-22.md`

No shared status document is edited here.

## 2. Executive Verdict

**Strongest defensible result now:** a conditional Fredholm/KSp theorem on a
tau-twisted discrete or residual sector, not an unconditional Fredholm theorem for the
full unprojected operator on all of `Y^14`.

The formal part is already stable:

```text
Fred_H(K_H) classifies KSp^0 = KO^4
```

for a fixed separable quaternionic Hilbert space `K_H`. The analytic burden is to prove
that the GU family actually lands in `Fred_H(K_H)` continuously in norm after bounded
transform.

The full unprojected claim is not defensible from the current notes. `D_GU` has split
signature principal symbol

```text
sigma(D_GU)(xi)^2 = g_Y(xi,xi) Id,
```

so ordinary ellipticity fails on the null cone. Noncompactness then adds continuous
spectrum and end behavior. A standard compact elliptic, b-elliptic, or scattering-elliptic
parametrix for the full unprojected operator cannot be asserted.

The correct analytic target is:

```text
D_delta,disc = P_disc e^{delta r} D_GU e^{-delta r} P_disc
  : W^{1,2}_{H,delta,disc}(Y^14,S) -> L^2_{H,delta,disc}(Y^14,S),
```

where `P_disc` is the tau-twisted relative discrete/residual spectral projection for the
`SL(4,R)/SO_0(3,1)` fiber problem with coefficient data from `S(6,4)` and the RS block.

The current note resolves one subgate negatively:

```text
Do not claim the scalar rank-one BC1 Plancherel ladder proves OC2 for the actual
Lorentz-metric pair.
```

The root-wall note shows the `e_2-e_3` wall does not by itself kill the shifted formal
degree. But it also demotes the scalar atom: for the corrected metric pair, the surviving
route is tau-twisted admissibility, not scalar BC1 discrete series. The RC1 verification
pack reinforces this: the rank-one BC1 chain fails as stated for the actual
`SO_0(3,1)` pair. Therefore `P_disc` is still a theorem to prove, not an established
operator.

## 3. Weighted H-Sobolev Domain

Fix:

- `S = H^64`, with right `H` multiplication.
- A positive auxiliary density on `Y^14`.
- A positive quaternionic Hermitian bundle metric on `S`.
- An `Sp(64)` connection preserving the right-`H` structure.
- A radial/end function `r` on the noncompact metric fiber.

Define:

```text
L^2_{H,delta}(Y^14,S)
  = { psi in L^2_loc : e^{delta r} psi in L^2_H(Y^14,S) },

W^{1,2}_{H,delta}(Y^14,S)
  = { psi : e^{delta r} psi in W^{1,2}_H(Y^14,S) }.
```

Equivalently, after conjugation,

```text
D_delta = e^{delta r} D_GU e^{-delta r}
```

acts on unweighted `L^2_H` with graph domain identified with the weighted domain.

The right-`H` algebraic part is resolved:

- `Cl(9,5) ~= M(64,H)` acts on the left and commutes with right `H`.
- `Sp(64) = U(64,H)` connections are right-`H` linear.
- Shiab and RS gamma-trace projections are built from left Clifford/tensor operations.
- Section pullback satisfies `s*(psi q) = (s*psi)q`.

What remains analytic is not `H`-linearity. It is the closed realization:

```text
D_delta : W^{1,2}_{H,delta} -> L^2_{H,delta}
```

with a specified minimal/maximal domain comparison. On the full split-signature,
noncompact `Y^14`, equality between the graph closure and the naive weighted Sobolev
space is an assumption until a bounded-geometry/end-calculus theorem is supplied.

## 4. P_disc Boundedness

The needed projection is not the scalar projection for an old rank-one model. It must be
the projection onto the tau-twisted relative discrete/residual sector:

```text
P_disc : L^2_H(Y^14,S) -> L^2_{H,disc}(Y^14,S),
```

with coefficient bundle carrying the relevant `S(6,4)` and RS H-types.

The required theorem must prove all of:

1. `P_disc` is an `H`-linear orthogonal projection on `L^2_H`.
2. `P_disc` extends boundedly to `L^2_{H,delta}` and `W^{1,2}_{H,delta}` for weights
   `delta` in an interval avoiding indicial roots or Plancherel walls.
3. `P_disc D_delta = D_delta P_disc` exactly, or up to lower-order compact terms, on the
   chosen domain.
4. The projected zero/discrete multiplicities are finite.
5. Under allowed parameter variation, `x |-> P_disc,x` is norm-continuous or is carried
   by a norm-continuous unitary trivialization.

Local status:

- The shifted A3 formal-degree product at `lambda_RS + rho_G` is nonzero.
- The scalar rank-one BC1 proof is not available for the actual Lorentz-metric pair.
- The live route is a tau-twisted Oshima-Matsuki/Kobayashi admissibility theorem for
  `L^2(SL(4,R) x_{SO_0(3,1)} tau_RS)`.

Thus `P_disc` boundedness is the primary OC2 analytic gate.

## 5. Compact-Remainder Parametrix

If `P_disc` exists with the properties above, the Fredholm package can be stated
concretely.

Let:

```text
K_H = L^2_{H,delta,disc}(Y^14,S),
Dom(D_delta,disc) = W^{1,2}_{H,delta,disc}(Y^14,S).
```

Assume zero is isolated from the nonzero projected spectrum and the kernel/cokernel are
finite-dimensional right-`H` modules. Then a sectoral parametrix has the form:

```text
Q_delta D_delta,disc = I_disc - Pi_ker + K_L,
D_delta,disc Q_delta = I_disc - Pi_coker + K_R,
```

where:

- `Pi_ker` and `Pi_coker` are finite-rank `H`-linear projections.
- `K_L` and `K_R` are compact on `K_H`.

In a pure spectral model, `Q_delta` is the inverse on the nonzero discrete summands:

```text
Q_delta = sum_{lambda_j != 0} lambda_j^{-1} P_j,
```

and the remainders are finite-rank projections. In an end-calculus model, `Q_delta` is a
b/0/scattering/edge parametrix and compactness of the residual terms follows from
residual-kernel decay plus weighted Rellich compactness.

This note cannot choose a final calculus. The likely model depends on the true end
geometry:

- b-calculus for cylindrical or conformally cylindrical ends;
- 0-calculus for asymptotically hyperbolic rank-one ends;
- scattering calculus for asymptotically conic compactifications;
- edge or fibred-boundary calculus if the `Y^14 -> X^4` fibration is kept in the operator.

The common requirement is the same:

```text
the normal/indicial family at infinity must be invertible on the chosen weight line,
after projecting to the tau-twisted discrete/residual sector.
```

Without that theorem, no compact-remainder parametrix is proved.

## 6. Bounded-Transform Norm Continuity

Let `X` be the compact observer parameter space and `D_x` the allowed GU family. OC2
requires a norm-continuous map:

```text
F_x = D_x(1 + D_x^* D_x)^(-1/2) : X -> Fred_H(K_H).
```

A sufficient analytic criterion is:

1. The varying `L^2` spaces are identified by `H`-unitaries with one fixed `K_H`.
2. The domains are identified with one fixed `W^{1,2}_{H,delta,disc}`.
3. `x |-> D_x` is norm-continuous as a bounded map
   `W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc}`.
4. `x |-> P_disc,x` is norm-continuous, or the discrete sector is transported by the
   same unitary trivialization.
5. The parametrix above is uniform in `x`; equivalently, zero does not enter the
   essential spectrum and the discrete spectral gap does not close.
6. The functional calculus theorem used is strong enough to convert common-domain
   graph continuity into norm continuity of the bounded transform.

This is not a formal Atiyah-Jannich issue. It is a Kato/gap-resolvent/functional-calculus
issue for a family of closed unbounded right-`H` linear operators with a parameter-dependent
projection.

## 7. KK Zero-Mode Unitarity

The VZ/F6 notes establish the useful principal-symbol fact:

```text
[c_s(eta), P_(0)] = 0
```

for the horizontal Clifford element and the KK zero/discrete-mode projection, under the
horizontal/vertical split. This is enough to preserve the 4D characteristic cone in the
zero-mode sector at reconstruction grade.

It is not yet a Hilbert-space unitarity theorem.

The needed unitary statement is:

Let `Z -> X^4` be a finite-rank right-`H` bundle of normalized tau-twisted discrete modes
in the fiber variable. Let `{varphi_j(x,n)}` be a smooth orthonormal frame in the fiber
Hilbert space. Define

```text
U : L^2_H(X^4,Z) -> P_disc L^2_H(Y^14,S)
U(a)(x,n) = sum_j a_j(x) varphi_j(x,n).
```

If the fiber density disintegrates as `dvol_Y = dvol_X dvol_F`, the modes are normalized by

```text
int_{F_x} <varphi_i(x,n), varphi_j(x,n)>_H dvol_F(n) = delta_ij,
```

and the frame is complete for `P_disc`, then `U` is an `H`-linear unitary onto the
discrete/zero-mode range by Fubini.

What remains open:

- finite-rank tau-twisted discrete mode bundle;
- smooth dependence on `x`;
- boundedness on weighted Sobolev spaces;
- exact `H`-linearity of the projection;
- compatibility of the zero/discrete projection with the full operator, not just the
  horizontal principal symbol.

## 8. Conditional Theorem

**Theorem (OC2 weighted tau-discrete Fredholm/KSp package).** Let `X` be a compact
Hausdorff observer parameter space. Let `delta` avoid the indicial/Plancherel walls of
the chosen end model. Suppose the GU family admits:

1. A fixed right-`H` Hilbert model
   ```text
   K_H = L^2_{H,delta,disc}(Y^14,S).
   ```
2. Closed, densely defined, right-`H` linear realizations
   ```text
   D_x : W^{1,2}_{H,delta,disc} -> K_H.
   ```
3. A bounded tau-twisted projection `P_disc,x` on the weighted Sobolev scale, invariant
   under `D_x` up to compact controlled terms.
4. A uniform compact-remainder parametrix
   ```text
   Q_x D_x = I_disc - Pi_ker,x + K_L,x,
   D_x Q_x = I_disc - Pi_coker,x + K_R,x.
   ```
5. Norm continuity of the bounded transforms
   ```text
   F_x = D_x(1 + D_x^*D_x)^(-1/2).
   ```
6. KK zero/discrete-mode unitarity identifying the projected 14D sector with the 4D
   finite-rank mode bundle.
7. The local index count and additivity theorem:
   ```text
   ind_H(D_x) = ind_H(spin-1/2 block) + ind_H(RS Schur block) = 16 + 8.
   ```

Then:

```text
F : X -> Fred_H(K_H)
```

is a norm-continuous family of quaternionic Fredholm operators, and hence defines

```text
[D_GU] = [F] in KSp^0(X) = KO^4(X).
```

At every point in the GU component where the index count hypotheses hold,

```text
epsilon_x([D_GU]) = ind_H(D_x) = 24.
```

## 9. Proof Sketch

1. Right-`H` linearity follows algebraically from the left `M(64,H)` Clifford action,
   the `Sp(64)` connection, and `H`-linear projections.
2. The weighted domain gives closed unbounded operators after the closed-realization
   theorem is assumed.
3. Bounded `P_disc` makes the projected domain and Hilbert space honest right-`H`
   Sobolev/Hilbert spaces.
4. The compact-remainder parametrix implies Fredholmness by Atkinson's theorem:
   finite-dimensional kernel/cokernel and closed range.
5. Uniformity and common-domain continuity give norm-continuity of the bounded transform
   by functional calculus.
6. Norm-continuity into `Fred_H(K_H)` gives the `KSp^0` class by quaternionic
   Atiyah-Jannich.
7. The point augmentation is the quaternionic Fredholm index. Under the Schur/LDU
   additivity and discrete RS count hypotheses, it is `16 + 8 = 24`.

## 10. No-Go and Unsafe Claims

The following claims should not be made from the current notes:

1. **Full unprojected Fredholmness on `Y^14`.** The split-signature symbol has a null cone
   and the noncompact fiber has continuous spectrum. Ordinary elliptic Fredholmness is not
   available.
2. **Scalar BC1 proof for the actual Lorentz pair.** The corrected Weyl/root-wall notes and
   the RC1 verification pack demote the scalar rank-one chain. The surviving claim is
   tau-twisted and conditional.
3. **Automatic boundedness of `P_disc` on weighted Sobolev spaces.** Spectral projections
   bounded on plain `L^2` do not automatically extend to exponential weighted Sobolev
   spaces without kernel estimates or a calculus theorem.
4. **KK zero-mode unitarity from principal-symbol commutation alone.** The commutator
   `[c_s(eta),P_(0)] = 0` is necessary but not sufficient for smooth finite-rank unitary
   identification of the projected Hilbert spaces.
5. **Bounded-transform norm continuity from pointwise Fredholmness.** Fredholmness at each
   parameter does not imply norm-continuity of `D(1+D^*D)^(-1/2)`.

## 11. Missing Analytic References or Theorems

The exact missing theorem is a combined spectral and operator-calculus statement:

> For the corrected symmetric pair `(SL(4,R), SO_0(3,1))` with coefficient
> `tau_RS = 4D(1/2,0) + 4D(0,1/2)` and the full GU/RS Schur block, prove a finite
> tau-twisted relative discrete/residual sector with a projection `P_disc` that is
> bounded on the weighted `L^2` and `W^{1,2}` scales, invariant for `D_GU`, and stable
> under allowed parameter variation. Then construct a compact-remainder parametrix for
> the projected weighted operator and prove bounded-transform norm continuity.

Likely external tools:

- Flensted-Jensen discrete series for semisimple symmetric spaces, but in the correct
  tau-twisted form.
- Oshima-Matsuki classification and Plancherel support for discrete series on reductive
  symmetric spaces.
- Kobayashi discrete decomposability and asymptotic K-support criteria for the
  `SO_0(3,1)` restriction.
- Matrix-valued Harish-Chandra c-functions for the RS/tau coefficient system.
- Melrose/Mazzeo b-, 0-, scattering-, or edge-calculus Fredholm theorem for the selected
  compactification of the `GL(4,R)/O(3,1)` end.
- Kato-type graph/gap-resolvent perturbation theory, plus a theorem converting the chosen
  topology to norm-continuity of bounded transforms.
- Quaternionic Fredholm/Atkinson theorem for closed unbounded right-`H` linear operators,
  including Schur/LDU index additivity.

## 12. Failure Conditions

OC2 fails or downgrades if any of the following occurs:

- The tau-twisted discrete/residual sector does not exist for the corrected pair.
- The RS contribution is continuous Plancherel support only, not finite multiplicity.
- `P_disc` is not bounded on `L^2_{H,delta}` or `W^{1,2}_{H,delta}`.
- `P_disc` is not invariant under `D_GU` and the commutator is not compact.
- The weight `delta` crosses an indicial root or Plancherel wall.
- Zero enters essential spectrum of the projected operator.
- The compact-remainder parametrix cannot be constructed.
- The KK/discrete projection is not unitary onto a smooth finite-rank mode bundle.
- The bounded transforms fail to be norm-continuous.
- The parameter space is noncompact without compact support or a controlled compactification.
- Gauge fixing or curvature terms break right-`H` linearity.

## 13. Next Action

The next action is not another formal `KSp` note. The hard analytic path is:

1. Fix the symmetric-pair model used for the noncompact fiber and retire the scalar BC1
   shortcut unless the isotropy is renamed and justified.
2. Prove the tau-twisted Oshima-Matsuki/Kobayashi admissibility theorem for
   `tau_RS = 4D(1/2,0) + 4D(0,1/2)`.
3. Build `P_disc` and prove boundedness on `L^2_{H,delta}` and `W^{1,2}_{H,delta}`.
4. Choose the end calculus and compute the normal/indicial family of `D_delta,disc`.
5. Construct the compact-remainder parametrix uniformly in the allowed GU parameters.
6. Prove norm continuity of the bounded transform.
7. Only after those steps upgrade OC2 from conditional theorem shape to resolved
   noncompact Fredholm/KSp implementation.

## 14. Final Verdict

**Verdict:** conditional tau-discrete sector theorem; full unprojected `Y^14` Fredholmness
is not established.

The formal `KSp^0(X)=KO^4(X)` classification is resolved once a norm-continuous
`Fred_H` family is supplied. The VZ notes support the principal/subprincipal symbol and
KK projection compatibility side. The unresolved OC2 core is the operator-analysis package:
bounded weighted `P_disc`, compact-remainder parametrix, bounded-transform norm
continuity, and Hilbert-space zero/discrete-mode unitarity.
