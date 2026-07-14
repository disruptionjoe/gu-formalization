---
artifact_type: exploration
label: W187
status: "exploration (W187 / law-shadow reduction audit; conditional reconstruction; no claim/status/canon movement; companion deterministic symbolic audit prepared, execution deferred to the orchestrator)"
created: 2026-07-14
wave: W187
posture: coherence-first; construction-fork explicit; honest grading
title: "W187 -- law, auxiliary elimination, and effective shadow: what does and does not imply a propagating scalar"
hypothesis: "A simple linear-curvature law can have a higher-derivative effective shadow without the law and shadow being the same functional. The full gauge-reduced block Hessian, not the words linear curvature or induced |II|^2 and not the sign of one local coefficient, decides whether the shadow contains an additional physical mode."
depends_on:
  - explorations/W161-lens-foundational-action-2026-07-14.md
  - explorations/W167-reduction-direct-sign-alpha-beta-2026-07-14.md
  - explorations/W176-build-reduction-x4-effective-2026-07-14.md
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md
  - explorations/W186-source-content-reservoir-krein-type-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W187_law_shadow_reduction_audit.py
---

# W187 -- the law-shadow reduction audit

## Result in one paragraph

The strongest defensible version of the law-versus-shadow story survives, but it is narrower than
several earlier formulations. GU's stated bosonic law and the geometric `|II|^2` bending functional
are different typed objects; no artifact inspected here supplies the missing map proving that
`|II|^2` is the exact effective action of the law. However, **linearity in curvature does not by
itself prove that the exact theory has no additional scalar mode**. Eliminating a field that is
algebraic in itself but derivatively coupled to the retained field produces a Schur complement with
higher powers of momentum. Its additional zeros are zeros of the full mixed Hessian, not automatically
contact artifacts. Conversely, a local `R^2` coefficient does not by itself prove a physical scalar:
the apparent pole may lie outside the effective theory's validity domain, be killed by gauge or
constraint reduction, or have no admissible positive metric. The honest verdict is therefore
**LAW-SHADOW-SEPARATION: SUPPORTED; PHYSICAL-SCALAR VERDICT: OPEN PENDING THE FULL GAUGE-REDUCED
HESSIAN AND ITS VALIDITY DOMAIN.** No full GU reduction is built here.

## 1. Construction ledger: every load-bearing fork named

The rule is not to prefer the geometer's or the physicist's object. It is to name the construction,
use it consistently, and state whether a conclusion transfers across the fork.

| Object | Construction used here | Why; transfer limit |
|---|---|---|
| Gauge group / inner product | GU-native `Sp(32,32;H)` indefinite/Krein setting, not compact `Sp(64)` | The physical residue test must eventually use the operative Krein grading. Positive-Hilbert examples below are algebra controls only. A Hilbert-positivity no-go does not transfer automatically to GU. |
| Ghost treatment | GU-native **KEEP-AND-GRADE**, via `[P,S]=0` and, if it exists, a `C`-operator with positive `eta_+ = eta C`; not projection/removal | A negative naive DeWitt direction is not yet a physical ghost, but neither does its sign alone construct `C`. The full `[H,C]=0`, positivity, and spectral conditions remain required. |
| Generation count | Native `Z/3` torsion arena, not a `Z`-valued index | Generation counting is not used to infer the scalar spectrum. W176's full-bundle count discussion is outside this audit; no scalar conclusion transfers to or from a `Z` index. |
| Metrics | Base spacetime metric `g_X` on `X4` and gimmel/DeWitt field-space metric `G_DW` on `Y14`/the vertical fiber are kept distinct | `g_X` defines momentum and mass shell; `G_DW` or the completed `eta_+` grades field-space residues. Contracting with one does not decide the role of the other. |
| Fundamental gravity law | Program-native first-order shiab/Einstein action `I1B[B,T]`, stated linear in Ehresmann curvature | This is the law-side input read by W161. Its *full Hessian*, including the `d_B T` and `[T,T]` terms, has not been calculated here. |
| Geometric shadow | Program-native geometric bending energy `W_II[sigma] = integral_X4 |II_sigma|^2` | This is a functional of a section/embedding and carries the W126 curvature-squared coefficients. It is not identified with the effective action unless a reduction theorem supplies the bridge. |
| Auxiliary elimination | Standard, construction-independent Schur complement of a block Hessian | This is exact where the eliminated block is invertible. It diagnoses what follows from elimination without assuming the GU answer. |
| Source / soldering | W180's physicist-style minimal-coupling current and ultralocal kernel are used only as an example; the native projector/current (`ker Gamma`, Krein current) remains a separate construction | Changing from a vertex/current model to the native projector can change the mixed Hessian blocks. No mode verdict from one transfers without recomputation. |

The no-go/result below therefore survives both constructions only at the algebraic level: **one may
not infer the physical pole count from the label “linear-curvature law” or “induced square” alone.**
The actual pole count can differ across the standard vertex and native projector constructions
because their Hessian blocks can differ.

## 2. The typed law-to-shadow diagram

Let

```text
Y14 = Met(X4)
sigma : X4 -> Y14                         a section (a metric field on X4)
C_Y    = Conn(P -> Y14) x F_other         retained GU fields/backgrounds
A_Y    = Gamma(E_T -> Y14)                displaced-torsion sector to be tested
S_Y    : C_Y x A_Y -> R                   the full bosonic law I1B
R_sigma: functionals on Y14 -> functionals on X4
E_T    : S[B,T] |-> S[B,T_*(B)]           classical stationary elimination, if it exists
```

After pullback and linearization, write retained physical fluctuations as
`h in H_sigma` and candidate eliminated fluctuations as `t in A_sigma`. The desired square is

```text
 Fun(C_Y x A_Y, R)  -- E_T -->  Fun(C_Y, R)
          | R_sigma                    | R_sigma
          v                            v
 Fun(H_sigma x A_sigma, R) -- E_t --> Fun(H_sigma, R)

 top-left:    S_Y[B,T] = I1B
 bottom-left: S_sigma[h,t] = R_sigma S_Y, then background expansion
 top-right:   Gamma_Y[B] = S_Y[B,T_*(B)] (or -i log integral DT quantum-mechanically)
 bottom-right:Gamma_sigma[h] = S_sigma[h,t_*(h)]
```

This square commutes classically only if all of the following hold:

1. the same variation space and boundary conditions are used on both paths;
2. the `T` Euler-Lagrange equation has a selected solution and its linearized block is invertible
   on the domain considered;
3. restriction respects that solution:
   `R_sigma(T_*(B)) = t_*(R_sigma B)`;
4. gauge fixing and constraint reduction commute with restriction/elimination;
5. discarded boundary terms vanish or match.

At quantum level, substitution at the stationary point is not enough. The measure and the Gaussian
determinant `+(i/2) Tr log C` (with signature/contour specified) also have to commute with pullback;
non-Gaussian `T` terms generate further vertices. None of W161, W167, W176, W180, or W186 proves
these conditions for the full GU action.

There is also a second, separate arrow:

```text
 Emb(X4,Y14)  -- II -->  Gamma(Sym^2 T*X4 tensor N_sigma)
      sigma   -- norm-square/integrate --> W_II[sigma] in R,
```

where `W_II[sigma] = integral_X4 |II_sigma|^2`. This geometric construction does **not** occupy the
bottom-right corner of the first square by type alone. An additional theorem must identify
`W_II` with `Gamma_sigma`, including coefficients, boundary terms, measure, and validity domain.
W167's Ricci-class/Weyl-content mismatch is evidence against the simplest Gaussian identification;
it is not a theorem that no fuller reduction can ever generate the missing invariants.

## 3. Minimal exact derivation: the block Hessian is the decider

Work after background choice, gauge fixing, and constraint reduction. At quadratic order let

```text
S^(2)[h,t] = 1/2 <h,A h> + <h,B t> + 1/2 <t,C t>,
```

where `A : H -> H*`, `B : A_sigma -> H*`, and `C : A_sigma -> A_sigma*`. Adjoints are taken in
the declared base/field-space pairings. If `C` is invertible on a spectral domain `Omega`, then

```text
t_*(h) = - C^{-1} B^dag h,
K_eff  = A - B C^{-1} B^dag,
S_eff^(2)[h] = 1/2 <h,K_eff h>.
```

For a finite truncation, and formally mode by mode,

```text
det [[A,B],[B^dag,C]] = det(C) det(K_eff).                 (1)
```

Equation (1) gives the disciplined interpretation:

- if `C` is invertible, a zero of `K_eff` is a zero of the **full mixed Hessian**. It is not made
  fictitious merely because `t` was eliminated;
- a pole of `C^{-1}` is not an auxiliary correction. It says the eliminated sector has its own
  on-domain mode and the Schur description fails there;
- `B` may contain momentum. Even constant/invertible `C` can then make `K_eff` higher order in
  momentum and can add zeros to the full system;
- only if the new zeros are outside `Omega`, gauge/constraint-null, or cancelled in all physical
  matrix elements may the higher-order term be treated as a self-energy without a new in-domain
  particle.

This corrects the risky inference in W161 N5. From
`<T,J(F)> + (1/2)<T,C T>` one may derive `-1/2<J,C^{-1}J>`. If `J(F)` is second order in the retained
metric, that term is fourth order. Calling it a “contact term whose propagating sector stays
second-order” requires an additional degeneracy/constraint/cutoff argument; it does not follow from
the Legendre minus sign.

There is an even earlier GU-specific gate. The full displayed `I1B` contains `d_B T` and `[T,T]`.
The quadratic term `<t, shiab(d_B t)>` can give the `C` block momentum dependence unless it is a
boundary, constraint, or degenerate first-order term after the actual pairing and background are
specified. Thus the assertion “`T` is algebraic” is established only for W167's Gaussian toy
`<T,J> + (1/2)<T,T>`, not for full `I1B`.

## 4. Necessary and sufficient quadratic criteria

The following are necessary and sufficient **at quadratic order, on a specified background,
physical sheet, gauge-reduced state space, and validity domain `Omega`**. They are not nonlinear or
nonperturbative theorems.

Let `K_0(s)` be the retained scalar inverse propagator, `Sigma(s)=B(s)C(s)^{-1}B(s)^dag`, and
`K_eff(s)=K_0(s)-Sigma(s)`, with `s=p^2` defined by the base metric `g_X`.

### 4.1 A genuine induced scalar pole

There is an additional scalar mode in `Omega` iff there is an `s_* in Omega` and physical scalar
polarization `v` such that

```text
K_eff(s_*) v = 0,
v is not gauge, constraint-null, or killed by every admissible source,
C(s_*) is invertible,
v^dag K_eff'(s_*) v != 0                     (simple pole case).
```

By (1), this is also a full-Hessian zero. For multiple zeros, replace the last line by the standard
spectral-projector/Jordan analysis.

### 4.2 Healthy

The scalar is healthy iff it is a genuine pole, `s_*=m^2` is real and nonnegative, the pole is on
the admissible sheet, and its residue is positive in the **operative physical metric**. In a
positive Hilbert model this is the sign of `1/(v^dag K_eff'(s_*)v)`. In GU's native branch the
criterion is instead evaluated with a constructed positive `eta_+=eta C_op` satisfying the full
commutation and positivity conditions. A negative DeWitt norm or the sign of `c_R` alone neither
proves nor cures the pole.

### 4.3 Tachyonic, ghost-like, or dynamically unstable

- **Tachyonic:** a genuine physical pole has real `m^2<0`. This is a mass instability, independent
  of the residue-sign question.
- **Ghost-like:** a genuine pole has the wrong residue/norm in the operative metric. It can have
  `m^2>0`; ghost and tachyon are not synonyms.
- **Dynamically unstable / non-operative:** poles form a complex pair or lie on a forbidden sheet.
  A finite-dimensional `C`-metric toy does not by itself settle the QFT lift.

### 4.4 Merely an effective self-energy in the stated theory

The induced scalar channel is merely a self-energy, rather than an additional in-domain particle,
iff `Sigma(s)` changes existing physical poles/residues but `K_eff` has no additional admissible
zero in `Omega`. In particular, a zero produced by resumming a truncated derivative expansion
outside its convergence/cutoff domain is not a particle prediction of that EFT. This classification
must always name `Omega`; without it, “mode” versus “self-energy” is underdetermined.

## 5. Controls: the inference succeeds and fails exactly where it should

The companion script checks the following exact examples.

**Positive control, genuinely auxiliary and nonderivative.** With

```text
A(s)=s-1,  B(s)=1,  C(s)=4,
K_eff(s)=s-5/4.
```

Elimination shifts the one healthy pole but does not increase the polynomial degree. This is the
case in which “auxiliary elimination gives only a self-energy/mass shift” is correct.

**Negative control, auxiliary in itself but derivatively coupled.** With

```text
A(s)=s-1,  B(s)=s,  C(s)=9,
K_eff(s)=s-1-s^2/9.
```

`C` is constant and invertible, yet `K_eff` has two positive roots
`(9 +/- 3 sqrt(5))/2`. Both are zeros of the full determinant. Their residues have opposite signs,
so in a positive-Hilbert control one is healthy and the other ghost-like. This directly falsifies
the general inference “algebraic auxiliary + law linear in a curvature-like derivative implies no
extra propagating mode.” If the declared EFT domain is `0 <= s < 4`, however, the high root lies
outside the domain; within that EFT the same `s^2` term is only a self-energy correction. The exact
UV completion and the truncated EFT therefore support different, both consistent, statements.

**Tachyon control.** `K(s)=s+2` has a simple positive-residue pole at `s=-2`: tachyonic but not a
negative-residue ghost. This keeps the two diagnoses separate.

## 6. Audit of the five inputs

### W161

Supported: it correctly reopens the law/shadow distinction and notes that the stated law is not
literally the `|II|^2` functional. Not established: “linear in curvature” alone does not imply no
scalar after exact elimination. Its own toy produces `Ein(F)^2`; the test does not calculate that
term's pole structure or prove it is a harmless contact term.

### W167

Supported: the Gaussian Schur-complement minus sign and the distinction between a Ricci-class
shiab square and the Weyl-carrying geometric `|II|^2` are useful conditional checks. Not established:
the full `I1B -> X4` reduction. The treatment assumes the eliminated block is algebraic, reduces the
shiab freedom to a trace parameter, omits the `d_B T`/non-Gaussian effects, gauge constraints,
measure determinant, and validity domain. Its `c_R(t)` is therefore the coefficient of a declared
truncation, not yet a physical mass verdict. A schematic Krein sign flip is not a substitute for a
full `C`-operator and residue calculation.

### W176

The artifact calls the vertical Hessian “built,” but the test imports/hardcodes W130's
`c_R=-4/9`, chooses representative oscillator frequencies `0.37` and `1.0`, and tests a finite
two-mode resonance model. It does not differentiate pulled-back `I1B`, derive those frequencies,
or construct the full QFT `C`-operator. Therefore “reduction suffices,” “operative,” and “bar (b)
clears” do not follow from W176's computation. The vertical-Hessian *program* is right; its GU
instance is still the missing object.

### W180

The ultralocal source bridge is a useful positive example of the same Schur logic:
`theta=kappa M^{-1}J` gives `-kappa/2 <J,M^{-1}J>`. It is explicitly conditional, uses a chosen
Frobenius/ultralocal kernel, and does not identify the shiab/torsion Hessian. It shows feasibility of
a law-to-self-energy mechanism, not the GU gravitational spectrum.

### W186

The fixed-point toy addresses boundary selection and the total metric after a modal truncation. It
does not decide whether the candidate scalar pole exists in the first place. Its honest result,
that existence of a favorable metric is not selection of it and that the QFT `C`-operator remains
unbuilt, reinforces the order of operations here:

```text
derive full physical Hessian -> locate admissible poles -> construct/choose operative metric
-> classify residues and boundary selection.
```

Using the boundary fixed point before deriving the Hessian would assume the candidate mode content.

## 7. Verdict, feasibility, and crisp falsifiers

### Honest grade

- **Exact / computed in the companion symbolic audit:** the stationary elimination formula,
  determinant identity, positive/negative controls, residue signs, tachyon control, and the
  cutoff-dependent self-energy classification.
- **Reconstruction from named artifacts:** the type separation between `I1B`, its putative effective
  action, and `W_II`; the list of missing commutation conditions.
- **Open GU physics:** the actual block operators `A,B,C`, their physical projectors, the full
  `C`-operator/positive metric, the cutoff, and the resulting pole classification.

### Verdict

**LAW-SHADOW-SEPARATION: SUPPORTED. PROPAGATING-MODE VERDICT: OPEN.** It is plausible and feasible
that a simple geometric law generates a complicated observable shadow: the Schur complement is the
explicit mechanism. But it is not yet known whether GU's shadow has no scalar, a healthy scalar, a
tachyon, a ghost, or only an out-of-domain self-energy. W187 does not build the full GU reduction
and moves no claim, canon, status, H-number, or bar.

### The next decisive construction

Choose one declared background and branch, then:

1. expand the **full** `I1B` to quadratic order, retaining `d_B T` and every background-dependent
   contribution of `[T,T]`;
2. fix gauge and solve constraints before calling any scalar physical;
3. derive typed `A(s),B(s),C(s)` using `g_X` for momentum and `G_DW`/Krein pairing for field space;
4. determine where `C(s)` is invertible and compute `K_eff=A-BC^{-1}B^dag`;
5. state the validity domain/cutoff, locate full-Hessian zeros, test source overlap, and compute
   residues using an actually constructed operative `eta_+` if following KEEP-AND-GRADE;
6. separately compare the result with `W_II` instead of inserting `W_II` as the Hessian.

This is finite in specification even if technically difficult; it is the feasible test that can
turn the plain-English “law and shadow” story into physics.

### Falsifiers

1. **Auxiliary premise falsifier:** the full `C(s)` has on-domain zeros or a nondegenerate kinetic
   principal symbol. Then `T` is not auxiliary on that domain and the algebraic W167 reduction is
   inapplicable.
2. **No-new-mode falsifier:** gauge-reduced `K_eff` has an additional admissible zero with nonzero
   source overlap and residue. Then the shadow carries a genuine full-system mode even though the
   parent action is linear in curvature.
3. **Tachyon claim falsifier:** the alleged negative-`m^2` zero is absent, gauge-null, on the wrong
   sheet, or outside the validity domain. Then a negative local `c_R` was not a physical tachyon.
4. **Healthy claim falsifier:** the pole has negative/undefined residue in every admissible
   operative metric, or no full QFT `C`-operator exists. A naive DeWitt sign flip cannot rescue it.
5. **Self-energy-only falsifier:** an additional pole remains inside `Omega` and is a full-Hessian
   zero with physical overlap. Then it cannot be dismissed as a truncation artifact.
6. **Separate-shadow falsifier:** a complete commuting reduction derives `Gamma_sigma=W_II` with
   matching Weyl/Ricci content, measure, boundary terms, and domain. Then `|II|^2` is the derived
   shadow after all, although it remains conceptually distinct from the fundamental law.
7. **Commutativity falsifier:** eliminating then pulling back differs from pulling back then
   eliminating. Then there is no unique “the GU shadow” until the section/boundary prescription is
   supplied.

These falsifiers are construction-specific. A result obtained with a positive-Hilbert removal of
the ghost does not kill the native KEEP-AND-GRADE branch; a favorable finite-dimensional Krein model
does not clear the QFT branch; and a vertex-source result does not settle the native projector/current
branch without an explicit comparison map.

## 8. Scope guard

This is a conditional exploration only. It does not claim the full GU reduction is built; it does
not identify `|II|^2` with the effective action; it does not assert that GU has or lacks a scalar;
it does not construct a `C`-operator; and it does not move indexes, canon, research status, bars,
or cross-repository truth. The companion test is lightweight and deterministic; execution was
deliberately left to the root orchestrator under the workspace's serialized-resource rule.
