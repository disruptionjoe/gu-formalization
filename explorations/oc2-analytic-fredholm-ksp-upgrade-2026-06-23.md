---
title: "OC2 Analytic Fredholm/KSp Upgrade for D_GU on Y^14"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "oc2-analytic-fredholm-ksp-upgrade"
verdict: "BOUNDED_CONDITIONAL_UPGRADE: KSp_FORMAL_PART_RESOLVED; FULL_Y14_WEIGHTED_FREDHOLM_REQUIRES_OPERATOR_ANALYSIS_REFERENCES"
---

# OC2 Analytic Fredholm/KSp Upgrade for D_GU on Y^14

## 1. Task

This note runs the requested OC2 upgrade:

- sharpen the `W^{1,2}_H` domain statement for `D_GU`;
- isolate what can be said about KK-zero-mode unitarity;
- state the bounded-transform continuity condition into `Fred_H`;
- formulate the weighted / b-calculus / scattering-calculus parametrix needed for
  `D_GU` on `Y^14` or on the controlled discrete sector;
- separate resolved parts from parts that still require external operator-analysis
  references and proof.

Inputs inspected:

- `explorations/oc2-h-linear-fredholm-y14-2026-06-23.md`
- `explorations/oc1-noncompact-atiyah-jannich-2026-06-23.md`
- `explorations/signed-readout-oc1-oc2-noncompact-fredholm-2026-06-23.md`
- `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`
- `explorations/rc1-rs-kk-zero-mode-2026-06-23.md`
- `explorations/vz-schur-complement-2026-06-23.md`
- `explorations/vz1-schur-complement-symbol-2026-06-23.md`
- `explorations/vz-oq1-sr-squared-identity-2026-06-23.md`
- `explorations/vz-oq2-lower-order-curvature-2026-06-23.md`
- `explorations/vz-subprincipal-symbol-rs-2026-06-23.md`
- `explorations/vz-f6-eft-decoupling-2026-06-23.md`
- `explorations/n5-discrete-series-gl4r-2026-06-23.md`
- `explorations/n5-ind-h-analytic-conditions-2026-06-22.md`
- related RC3 / Weyl-root notes by targeted search.

No shared status document is edited by this note.

## 2. Executive Verdict

**Strongest bounded statement now supportable:**

Let `K_H` be either

```text
L2_disc(Y^14, S)
```

or a weighted Sobolev completion of that discrete sector, with `S = H^64`. If the
following analytic hypotheses are supplied:

1. `D_GU` has a closed right-`H`-linear realization
   `D_delta: W^{1,2}_{H,delta,disc}(Y^14,S) -> L^2_{H,delta,disc}(Y^14,S)`;
2. the discrete-sector projection `P_disc` is bounded on the chosen Sobolev scale and
   commutes with `D_GU` modulo compact or controlled lower-order terms;
3. a sectoral parametrix exists,
   ```text
   Q_delta D_delta = P_disc - P_ker + K_L,
   D_delta Q_delta = P_disc - P_coker + K_R,
   ```
   with `P_ker`, `P_coker` finite-rank `H`-linear projections and `K_L`, `K_R` compact;
4. the bounded transforms
   ```text
   F_x = D_x(1 + D_x^*D_x)^(-1/2)
   ```
   vary continuously in norm as maps into `Fred_H(K_H)`;

then the OC2 KSp conclusion is valid:

```text
[F] in [X, Fred_H(K_H)] = KSp^0(X) = KO^4(X),
eps_x([F]) = ind_H(D_x).
```

On the GU component where the current reconstruction-grade count applies,

```text
ind_H(D_GU) = 16 + 8 = 24.
```

**What is resolved locally:** `H`-linearity, preservation of the right-`H` structure
under section pullback, the formal `Fred_H -> KSp^0` classification, compact `X^4`
pullback Fredholmness, and the principal/subprincipal VZ symbolic compatibility.

**What is not resolved locally:** the full non-compact `Y^14` weighted Fredholm theorem,
bounded-transform norm continuity, KK zero-mode unitarity as an actual isometry onto a
finite-rank zero-mode bundle, and a b/scattering/0-calculus parametrix with compact
remainders. These require operator-analysis references and proof, not more formal
Atiyah-Janich discussion.

## 3. Domain Upgrade: W^{1,2}_H

### 3.1 Definition that can be used now

Fix an auxiliary positive density and a positive quaternionic Hermitian bundle metric on
`S = H^64`. The right-`H` Hilbert space is

```text
L^2_H(Y^14,S) = completion of C_c^\infty(Y^14,S)
```

with inner product

```text
<psi,phi>_H = integral_Y <psi(y),phi(y)>_{S,H} dvol_aux(y).
```

For a connection `nabla^A` preserving the `Sp(64)` structure, define

```text
W^{1,2}_H(Y^14,S)
  = { psi in L^2_H : nabla^A psi in L^2_H(T^*Y^14 tensor S) }
```

with graph/Sobolev norm

```text
||psi||^2_{W^{1,2}}
  = ||psi||^2_{L^2} + ||nabla^A psi||^2_{L^2}.
```

For a radial function `r` along the non-compact `GL(4,R)/O(3,1)` fiber, the weighted
version is

```text
W^{1,2}_{H,delta}(Y^14,S)
  = { psi : e^{delta r} psi in W^{1,2}_H(Y^14,S) }.
```

The discrete-sector domain is

```text
W^{1,2}_{H,delta,disc}
  = P_disc W^{1,2}_{H,delta}(Y^14,S)
```

provided `P_disc` is bounded on this Sobolev scale.

### 3.2 Resolved part

The right-`H` module structure is algebraically secure:

- `Cl(9,5) ~= M(64,H)` acts on the left.
- Right multiplication by `H` commutes with left `M(64,H)` Clifford multiplication.
- `Sp(64) = U(64,H)` connections act by left quaternionic-linear matrices.
- Shiab and RS gamma-trace projections are built from Clifford contractions and tensor
  contractions, so they are right-`H` linear in the local model.

Therefore the Sobolev spaces above are right-`H` Hilbert spaces and `D_GU` is a
right-`H`-linear operator on its natural domain.

### 3.3 Operator-analysis gap

The notes do not yet prove that the graph closure of the formal operator equals the
weighted Sobolev space above on full `Y^14`. That needs:

- bounded geometry, or a specified compactification/end model for `Y^14`;
- a density and unitary trivialization for varying metrics;
- closedness and regularity of the first-order operator in the chosen positive Hilbert
  structure;
- comparison between minimal and maximal domains;
- a proof that `P_disc` is bounded on `W^{1,2}_{H,delta}`.

The compact pullback case avoids this gap: on compact Riemannian `X^4` (for the K3
sector), `s^*D_GU: W^{1,2}_H(X^4,s^*S) -> L^2_H(X^4,s^*S)` is Fredholm by ordinary
elliptic theory once the pulled-back symbol is elliptic.

## 4. KK-Zero-Mode Unitarity

### 4.1 What the local notes establish

The VZ/F6 notes establish the principal-symbol compatibility:

```text
[c_s(eta), P_(0)] = 0
```

provided `P_(0)` is the spectral projection onto normal/KK zero modes and `c_s(eta)` is
the horizontal Clifford element. This is enough to show that the zero-mode sector
inherits the same horizontal Clifford identity:

```text
(c_s(eta)|_{E_s^(0)})^2 = g_s(eta,eta) Id.
```

This is a symbolic and algebraic result. It supports VZ evasion and compact pullback
Fredholmness, but it is not yet a Hilbert-space unitarity theorem.

### 4.2 Strongest bounded unitarity statement

Assume the normal operator `Delta_N` over the section has a finite-dimensional
right-`H` zero/discrete-mode bundle

```text
Z -> X^4
```

with a smooth local orthonormal frame `{varphi_j(x,n)}` in the fiber variable. Define

```text
U: L^2_H(X^4,Z) -> P_(0)L^2_H(Y^14,S)
U(a_1,...,a_N)(x,n) = sum_j a_j(x) varphi_j(x,n).
```

If the fiber modes are normalized by

```text
integral_{F_x} <varphi_i(x,n), varphi_j(x,n)>_H dvol_F(n) = delta_ij,
```

then `U` is an `H`-linear unitary onto `P_(0)L^2_H(Y^14,S)` by Fubini. Under the same
assumptions, the pulled-back zero-mode operator is

```text
D_0 = U^{-1} P_(0) D_GU P_(0) U
```

with domain `U^{-1}(P_(0) dom D_GU)`.

### 4.3 What remains open

The current repo supports the ingredients only conditionally:

- RC1 gives an RS discrete-mode existence argument at reconstruction grade, using the
  tau-shift to place the RS parameter at `nu_1 = 3/2`.
- RC3 gives a discrete normal spectrum `{8,14,18,20}/R_s^2` and a continuum threshold
  `81/(4R_s^2)` at reconstruction grade.
- `oq-weyl3` exposes a real tension: without the tau-shift, raw `Lambda_RS = 1` can fall
  between half-integer poles and look continuous rather than discrete.

Therefore the unitarity map is resolved only as a conditional Hilbert-space construction.
It still needs an operator-analysis / representation-theory proof that the zero/discrete
mode projection is finite-rank, smooth in the base/parameter, `H`-linear, and bounded on
the chosen Sobolev scale.

## 5. Bounded-Transform Continuity into Fred_H

### 5.1 Formal KSp part is resolved

For any fixed infinite-dimensional separable quaternionic Hilbert space `K_H`,

```text
[X, Fred_H(K_H)] = KSp^0(X) = KO^4(X)
```

for compact Hausdorff `X`. Thus, once the GU family supplies a continuous map

```text
F: X -> Fred_H(K_H),
```

the KSp class exists. Non-compactness of `Y^14` does not alter the classifying-space
statement after the Hilbert space is fixed.

### 5.2 Sufficient continuity criterion

A usable analytic criterion is:

1. all `D_x` are closed, densely defined, right-`H`-linear Fredholm operators on the
   same `K_H`;
2. their domains are identified with one fixed `W^{1,2}_{H,delta,disc}` by an
   `H`-unitary trivialization;
3. the map
   ```text
   x |-> D_x
   ```
   is continuous as a bounded map
   ```text
   W^{1,2}_{H,delta,disc} -> L^2_{H,delta,disc};
   ```
4. there is a uniform Fredholm gap: zero stays out of the essential spectrum and the
   parametrix remainders remain compact uniformly in `x`.

Then the graph/gap topology is continuous, and standard functional calculus should give
norm continuity of

```text
F_x = D_x(1 + D_x^*D_x)^(-1/2)
```

into `Fred_H(K_H)`.

### 5.3 Gap requiring references

The note set has not proved this criterion for GU. In particular, it has not proved:

- norm continuity of the bounded transform under variation of `Sp(64)` connections and
  section data;
- continuity of `P_disc` or `P_(0)` under the same deformations;
- common-domain trivialization for varying `L^2` densities and metrics;
- uniform invertibility at infinity / uniform spectral gap in the weighted calculus;
- continuity for the Schur-complement/LDU Fredholm decomposition in the unbounded
  quaternionic setting.

This is the main analytic OC2 gate.

## 6. Weighted / b-Calculus / Scattering Parametrix

### 6.1 What cannot be claimed

The full operator on `Y^14` is not elliptic in the ordinary Riemannian sense: the gimmel
metric has split signature `(9,5)`, so

```text
sigma(D_GU)(xi)^2 = g_Y(xi,xi) Id
```

has a null cone. Therefore an ordinary elliptic b-calculus or scattering-calculus
parametrix for the full unprojected operator

```text
D_GU: W^{1,2}_{H,delta}(Y^14,S) -> L^2_{H,delta}(Y^14,S)
```

cannot be asserted from the local notes.

The correct target is narrower:

- the compact section-pullback operator;
- the vertical/normal elliptic spectral problem defining the KK/discrete sector;
- or the projected operator `P_disc D_GU P_disc` after the continuous spectrum is removed.

### 6.2 Spectral parametrix on the discrete sector

Assume a Harish-Chandra / Flensted-Jensen decomposition

```text
L^2_H(Y^14,S) = L^2_disc oplus L^2_cont
```

with `P_disc` the corresponding `H`-linear spectral projection and with `D_GU` invariant
on `L^2_disc`. On the discrete sector, define

```text
Q_disc = sum_{lambda_j != 0} lambda_j^{-1} P_j
```

where `P_j` are the finite-multiplicity spectral projections for the discrete summands.
Then

```text
Q_disc D_GU = P_disc - P_ker,
D_GU Q_disc = P_disc - P_coker.
```

If only finitely many zero modes occur and the nonzero discrete eigenvalues are separated
from zero, `P_ker` and `P_coker` are finite-rank and the remainders are compact. This is
the cleanest Fredholm mechanism already suggested by OC1.

This is not yet a proof because the note set still needs the representation-theoretic
spectral theorem in exactly this twisted `S(6,4)` / RS setting.

### 6.3 Weighted end parametrix formulation

Equivalently, compactify the non-compact fiber at infinity and work with a radial
coordinate `r`. Conjugate by the weight:

```text
D_delta = e^{delta r} D_GU e^{-delta r}.
```

A b/0/scattering-style theorem would need to prove:

1. the chosen compactification models the `A`-infinity end of `GL(4,R)/O(3,1)`;
2. the normal/indicial family `I(D,lambda)` is invertible for `lambda` on the line
   determined by `delta`, except at the known discrete atoms;
3. the weight `delta` avoids indicial roots and the continuous spectrum threshold;
4. the calculus gives a parametrix
   ```text
   Q_delta D_delta = I - Pi_ker + K_L,
   D_delta Q_delta = I - Pi_coker + K_R
   ```
   with compact residual terms on the weighted Sobolev scale.

The local notes suggest a natural spectral gap:

```text
discrete eigenvalues: {8,14,18,20}/R_s^2
continuous threshold: 81/(4R_s^2)
```

but this remains reconstruction-grade and depends on root multiplicities, the correct
BC_1 c-function, and the tau-shift placing the RS sector in the discrete part.

### 6.4 Which calculus is the likely fit

The end of a rank-one symmetric-space fiber is better modeled by a radial compactification
and a normal/indicial family than by compact elliptic theory. Depending on the exact
metric model, the likely tools are:

- b-calculus for cylindrical or conformally cylindrical ends;
- 0-calculus for asymptotically hyperbolic rank-one ends;
- scattering calculus for asymptotically conic choices of compactification;
- edge/fibred-boundary calculus if the `Y^14 -> X^4` fibration is kept throughout.

This note does not choose among them. The required deliverable is the same in each:
full ellipticity or invertibility at infinity for the projected/weighted operator and
compactness of the residual terms.

## 7. Resolved vs. Still Requiring Operator-Analysis References

### Resolved locally

| Item | Status | Reason |
|---|---|---|
| Right-`H` structure on `S = H^64` | RESOLVED | `Cl(9,5) ~= M(64,H)` left action commutes with right `H` |
| `D_GU` is `H`-linear | RESOLVED algebraically | Clifford, `Sp(64)`, Shiab, and RS projections preserve right `H` |
| Section pullback preserves `H` | RESOLVED algebraically | `s^*(psi q) = (s^*psi)q` |
| Compact `X^4` pullback Fredholmness | RESOLVED under elliptic/K3 pullback | Standard compact elliptic theory or APS variant |
| Formal `Fred_H` classification | RESOLVED | `Fred_H` represents `KSp^0 = KO^4` for fixed `K_H` |
| VZ principal/subprincipal cone control | CONDITIONALLY_RESOLVED | Symbolic argument gives null cone; lower-order terms do not change principal symbol |

### Still requiring operator-analysis references

| Item | Needed proof/reference |
|---|---|
| Full `W^{1,2}_{H,delta}` realization on `Y^14` | Closedness, domain equality, bounded geometry/end model |
| `P_disc` bounded on weighted Sobolev spaces | Spectral projection estimates for the twisted symmetric-space sector |
| RS tau-shift and discrete placement | Flensted-Jensen/Oshima-Matsuki/Kobayashi-style theorem in the precise normalization |
| Parametrix with compact residuals | b/0/scattering/edge calculus or Harish-Chandra spectral parametrix |
| KK-zero-mode unitarity | Smooth finite-rank zero-mode bundle, spectral gap, normalized fiber modes, Berry connection control |
| Bounded-transform norm continuity | Kato/gap-resolvent functional calculus with common domains and uniform Fredholm gap |
| Unbounded Schur/LDU index additivity | Atkinson-Schur theorem for closed unbounded `H`-linear Fredholm operators |
| Compact/non-compact observer space | Compact parameter space, compactification, or compactly supported `KSp` model |

## 8. Conditional Theorem Statement

**Theorem shape (OC2 analytic Fredholm/KSp upgrade).** Let `X` be a compact Hausdorff
observer parameter space. Let `D_x` be the GU family acting on a fixed quaternionic
Hilbert space

```text
K_H = L^2_{H,delta,disc}(Y^14,S)
```

with domain `W^{1,2}_{H,delta,disc}`. Assume:

1. `D_x` is closed, densely defined, and right-`H` linear.
2. `D_x` is Fredholm on the discrete/weighted sector by a parametrix with compact
   residuals.
3. the bounded transforms `F_x = D_x(1+D_x^*D_x)^(-1/2)` form a norm-continuous map
   `X -> Fred_H(K_H)`.
4. the discrete-sector index computation is the GU one:
   spin-1/2 contribution `16`, RS contribution `8`, and Schur/LDU additivity holds.

Then

```text
[D_GU] := [F] in KSp^0(X) = KO^4(X)
```

is defined, and on the GU component

```text
eps_x([D_GU]) = ind_H(D_x) = 24.
```

If the compact pullback to K3 is used instead of full `Y^14`, the Fredholm input is
classical and only the identification of the pullback/KK sector with the `Y^14` discrete
sector remains conditional.

## 9. Failure Conditions

OC2 fails or downgrades if any of the following occurs:

- `D_GU` is not Fredholm on the chosen weighted/discrete sector.
- zero lies in the essential spectrum after weighting or under deformation.
- `P_disc` is not bounded or not invariant under the GU operator.
- the RS tau-shift to the discrete pole is wrong, putting the RS contribution in the
  continuous spectrum.
- the KK zero-mode projection is not unitary onto its range or does not commute with
  horizontal Clifford multiplication beyond the principal-symbol model.
- bounded transforms fail to be norm-continuous.
- the observer parameter space is non-compact with no controlled compactification or
  compact-support formulation.
- a gauge or gauge-fixing choice breaks right-`H` linearity.

## 10. Final Verdict

**Verdict:** bounded conditional upgrade.

The formal OC2/KSp side is as strong as it can be: once the GU family lands continuously
in `Fred_H`, the class is in `KSp^0(X)=KO^4(X)`, and the point augmentation recovers the
quaternionic Fredholm index.

The analytic `Y^14` side is not yet fully resolved. The compact section-pullback domain is
Fredholm by standard elliptic theory, and the discrete-sector strategy is coherent, but
the full weighted `W^{1,2}_H` Fredholm theorem and parametrix for `D_GU` on the non-compact
sector still require a real operator-analysis proof.

