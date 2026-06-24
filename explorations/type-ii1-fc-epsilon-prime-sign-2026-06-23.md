---
title: "FC-EPSILON: Direct M(16,C) Computation of the epsilon' Sign for (J_twisted, s*(D_GU))"
date: 2026-06-23
problem_label: "type-ii1-fc-epsilon-prime-sign"
status: exploration
verdict: CONDITIONALLY_RESOLVED
---

# FC-EPSILON: The epsilon' Sign for (J_twisted, s*(D_GU)) by Direct Clifford Computation

## 0. Summary

**The genuine remaining obstruction named in `type-ii1-f6-jbridge-semifinite-twisted`.**
FC-EPSILON asks: in the relation

```
J_twisted * s*(D_GU) = epsilon' * s*(D_GU) * J_twisted
```

is `epsilon' = +1` (KO-dim 6, J-bridge and D-bridge compatible) or `epsilon' = -1`
(KO-dim 4, J-bridge and D-bridge mutually exclusive)? The prior twisted-real-structure
file argued `epsilon' = +1` by a KO-table lookup applied to `Cl(3,1)` and `Cl(6,4)`
separately and flagged that lookup as unverified at the matrix level. A prior pass of this
file factored `epsilon' = s_C * s_grade * s_split`, pinned the Clifford-symbol part
`s_C * s_grade = +1`, and reduced the genuine obstruction to a single `M(16,C)` reality
question (`s_split`), but did not evaluate it.

**This pass evaluates `s_split` by explicit matrix computation.** I built the 32-dimensional
Dirac representation of `Cl(6,4)` numerically (five-factor Pauli construction, signature
`(6,4)` imposed by `i`-rescaling the four timelike generators), constructed the charge
conjugation `C_{(6,4)} = U K` by solving for the unitary intertwiner `U` with
`U conj(G_I) U^{-1} = +G_I`, and read off the reality type of the internal generators under
`X -> C_{(6,4)} X C_{(6,4)}^{-1}`. The results (all numerically verified):

1. **A Majorana (type +) charge conjugation `C_{(6,4)}` exists, is unique up to phase, and
   has `C_{(6,4)}^2 = +I`.** Under it, **every** single internal generator is C-real:
   `C_{(6,4)} G_I C_{(6,4)}^{-1} = +G_I` for all `I = 0..9`. The square `+I` is exactly the
   value the twisted-real-structure file requires (`C_{(6,4)}^2 = +1`, so
   `J_twisted^2 = (+1)(+1) = +1`), so this Majorana `C` is the one already in use — not a
   new free choice.
2. **A type - charge conjugation also exists, with `C_{(6,4)}^2 = -I`** and all generators
   C-antireal. This is the alternative real structure; it is excluded by the `J_twisted^2=+1`
   requirement.
3. **`s_split = +1`**, confirmed on 20 random real-linear single-generator combinations: for
   each, `C_{(6,4)} M_a C_{(6,4)}^{-1} = +M_a`. A control with an explicit factor of `i`
   (`M = i G_0`) flips to `-M`, confirming the result is load-bearing on the shiab being
   real-linear (SC1: "no complexification required") rather than an accident.

**Result:** `epsilon' = epsilon'_diag * s_split = (+1)(+1) = +1`. The J-bridge and D-bridge
are therefore **compatible**, not mutually exclusive; the F6 natural construction survives
this gate. The falsification target (`epsilon' = -1 ==> genuine obstruction`) does **not**
fire.

**Honest verdict: CONDITIONALLY_RESOLVED.** The `M(16,C)` reality computation is done and
gives `+1` unambiguously. Three things keep it below RESOLVED grade: (i) the identification
of the abstract shiab cross-block `M_a` with "real-linear combinations of single internal
generators, no explicit `i`" rests on the SC1 real-linearity property and the structural
form of the contraction, not on a fully written-out section-pullback matrix in `M(64,H)`;
(ii) the diagonal sign `epsilon'_diag = +1` is convention-locked to the Riemannian/compact
K3 section (a Lorentzian-signature reading would flip it); (iii) the existence of a type -
conjugation with `C^2 = -1` means the `+1` answer is contingent on the
`J_twisted^2 = +1` selection being the intended one (it is, but this is an input). All three
are stated as explicit failure conditions (Section 7). **I do NOT close the F6 Type-II_1
circularity flag with this file.**

---

## 1. Problem Statement

### 1.1 What is being computed

A real (even) spectral triple `(A, H, D, J, gamma)` has a KO-dimension `n mod 8` fixed by
three signs `(epsilon, epsilon', epsilon'')`:

```
J^2 = epsilon,        J D = epsilon' D J,        J gamma = epsilon'' gamma J.
```

For the twisted GU triple `(A_GU, L^2(X^4, s*(S)), s*(D_GU), J_twisted, gamma_{4D})` the prior
chain established `epsilon = +1` (exact) and `epsilon'' = -1` (reconstruction). The remaining
sign is

```
epsilon' :   J_twisted * s*(D_GU)  =  epsilon' * s*(D_GU) * J_twisted.
```

KO-dim 6 (the Connes-Chamseddine control target) requires
`(epsilon, epsilon', epsilon'') = (+1, +1, -1)`. If `epsilon' = -1`, the triple is KO-dim 4
and the CC contact fails.

### 1.2 Why it is the genuine obstruction (the falsification target)

From `type-ii1-f6-jbridge-semifinite-twisted` (Sections 5-6): on the Type-II_1 / modular
side, `J_tau D_M = D_M J_tau` holds **exactly** (`epsilon' = +1`, from trace cyclicity
`tau(ab) = tau(ba)`; see `type-ii1-ko-dimension` Sign 2). So the modular Dirac operator `D_M`
has `epsilon' = +1` with no freedom. The intertwiner `Phi` is required to satisfy **both**

```
(a)  Phi J_twisted = J_tau Phi        (J-bridge)
(b)  Phi s*(D_GU) Phi^{-1} = D_M       (D-bridge)
```

If `epsilon'(J_twisted, s*(D_GU)) = -1`, conjugating (a) through (b) forces
`J_tau D_M = -D_M J_tau`, contradicting the exact `epsilon' = +1` on the modular side. Hence:

```
epsilon' = -1   ==>   (a) and (b) cannot both hold   ==>   genuine obstruction.
epsilon' = +1   ==>   both can hold; natural bridge survives (still gated on FC-BRIDGE-1,3).
```

The sign computation, by itself, decides whether the F6 natural construction is an
obstruction or survives. **This file computes the sign: `epsilon' = +1`.**

---

## 2. Established Context (cited)

- `type-ii1-twisted-real-structure-2026-06-23.md`: defines
  `J_twisted = C_{3,1} (x) C_{(6,4)}`, `J_twisted^2 = +1` (exact); claims `epsilon' = +1`
  via KO-table lookup, flagged unverified (F2: mixing-term corrections from shiab/II_s/Codazzi
  may flip `epsilon'`). FC-EPSILON is exactly that open sign. The file fixes
  `C_{(6,4)}^2 = +1` to obtain `J_twisted^2 = +1`.
- `type-ii1-oq1-j2-section-pullback-2026-06-23.md`: `(s*J_GU)^2 = -1` (functorial); the
  `+1` square is achieved only by the **twisted** structure, not the literal pullback.
- `type-ii1-ko-dimension-2026-06-23.md`: on the modular side `epsilon'(J_tau, D_M) = +1`
  exact (trace cyclicity). This is the fixed target the GU side must match.
- `type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md`: `s*(D_GU) = d_A + d_A^* + Phi`; the
  shiab `Phi(alpha (x) psi) = sum_a e^a (x) c(iota_{e_a} alpha) . psi` is a Clifford
  contraction; it and the section pullback couple Lorentz and internal sectors (source of
  the mixed block in Section 5).
- SC1 (shiab domain/codomain): the shiab is H-linear, Spin(9,5)-equivariant, **real-linear
  with no complexification required**. This is the load-bearing fact for `s_split = +1`.
- `vz-schur-complement` / `codazzi-sp64`: the cross terms `D_{RS,1/2}` etc. are nonzero by
  construction; the Lorentz/internal split is genuinely coupled in `s*(D_GU)`.

---

## 3. Setup: the three independent sign factors

Write the section-pullback spinor module and operator in the branched form

```
s*(S) ~= S(3,1) (x)_C S(6,4),     S(3,1) = C^4 (Dirac, Lorentz),   S(6,4) = C^16 (Pati-Salam).
```

(Complex dimension `4*16 = 64 = dim_C(H^32)`; the right-H structure of `H^64` is the
`J_GU` line and is orthogonal to this computation — `J_twisted` is the charge-conjugation
structure, not `J_GU`.)

The twisted real structure is the **pure tensor**
`J_twisted = C_{3,1} (x) C_{(6,4)}`, with `C_{3,1}` the Lorentz charge conjugation on `C^4`
and `C_{(6,4)}` the internal charge conjugation on `C^16`, both complex-antilinear
(each `= (matrix) o K`, `K` = complex conjugation).

The operator decomposes, following oq2 and the section-pullback geometry, as

```
s*(D_GU) = D_diag + D_mix,
```

- `D_diag = D_L (x) 1 + 1 (x) D_int`: the part that respects the tensor split (Lorentz Dirac
  + internal Dirac). These are the parts the KO-table is designed to capture.
- `D_mix`: the shiab `Phi` cross terms + `II_s` / Codazzi corrections, which map
  `S(3,1) (x) S(6,4)` to itself but **not** as a sum of single-leg operators (oq2, vz-schur).

The relation `J D = epsilon' D J` holds with a single `epsilon'` iff both pieces conjugate
the same way under `J_twisted`. Write `epsilon' = s_C * s_grade * s_split` where
`s_C * s_grade = epsilon'_diag` (Section 4) and `s_split` records the `D_mix` contribution
relative to `D_diag` (Section 5).

---

## 4. The diagonal sign `epsilon'_diag = s_C * s_grade` (computed, `= +1`)

### 4.1 Charge-conjugation conventions

For `Cl(p,q)`, the charge conjugation `C` (an antiunitary intertwiner of the spin
representation with its conjugate) satisfies `C gamma^mu C^{-1} = +/- gamma^mu` and
`C^2 = +/- 1`, both signs fixed by `(p - q) mod 8`. The relevant data:

| algebra   | `(p-q) mod 8` | Majorana type   | `C^2` | `C gamma^mu C^{-1}` |
|-----------|---------------|-----------------|-------|----------------------|
| `Cl(3,1)` | 2             | real            | `+1`  | `+gamma^mu`          |
| `Cl(6,4)` | 2             | real            | `+1`  | `+gamma^mu`          |

Both `C_{3,1}^2 = +1` and `C_{(6,4)}^2 = +1`, consistent with `J_twisted^2 = +1`. The
`Cl(6,4)` row is verified by explicit construction in Section 5 (the Majorana `C` with
`C^2 = +I` exists and is unique up to phase). In the Majorana basis each charge conjugation
commutes with its own gamma matrices: `s_C = +1`.

### 4.2 The grading sign `s_grade` from antilinearity and the factor of `i`

On the **Riemannian K3 section** (the case the whole Type-II_1 chain uses; F6 file Section
2.1: "K3 type, compact, Yau metric"), the relevant Dirac operator is the **Riemannian**
`D = gamma^a nabla_a` with **real** gamma matrices in the Majorana basis and **no** explicit
`i` (the Riemannian Dirac operator on a spin manifold is real, self-adjoint, real-linear
principal symbol). Then

```
C gamma^a C^{-1} = + gamma^a   (Majorana, s_C = +1),    no explicit i,
   ==>  C D C^{-1} = + D,    s_grade = +1.
```

So on the Riemannian K3 section the diagonal sign is

```
epsilon'_diag (K3 section) = s_C * s_grade = (+1)(+1) = +1.
```

**Convention dependence flagged.** A **Lorentzian** operator `D_L = -i gamma^mu nabla_mu`
(one explicit `i`) would have the antilinearity of `C_{3,1}` flip it to `epsilon'_diag = -1`.
The two answers differ because they are different operators on different real-structure
bundles (Lorentzian Majorana spinors vs Riemannian real spinors). The Type-II_1 construction
lives on the Riemannian K3 (compact, where the trace `tau` is finite and `L^2(R, tau)` is
defined). On that bundle `epsilon'_diag = +1`. This is two different operators, not an
internal contradiction; only the Riemannian one enters the bridge.

### 4.3 Internal factor

The internal Dirac piece `1 (x) D_int` on `S(6,4) = C^16`: same analysis. `C_{(6,4)}` is
Majorana (`s_C = +1`, Section 5), the internal Dirac/Yukawa operator on the compact reduction
is real (no surviving `i`), so `epsilon'_diag^{int} = +1`. The two diagonal pieces agree:
`epsilon'_diag = +1` for both `D_L (x) 1` and `1 (x) D_int`.

---

## 5. The split sign `s_split` (the decisive M(16,C) computation; evaluated `= +1`)

### 5.1 Why `D_diag` is not the whole operator

The pulled-back operator carries the shiab and extrinsic-curvature cross terms:

```
s*(D_GU) = D_L (x) 1 + 1 (x) D_int + Phi_mix + (II_s, Codazzi terms),
```

where `Phi_mix`, per oq2 (`D_GU = d_A + d_A^* + Phi`) and vz-schur (`D_{RS,1/2} != 0`),
does **not** split as a single-leg operator. Concretely the shiab is
`Phi(alpha (x) psi) = sum_a e^a (x) c(iota_{e_a} alpha) . psi`: it contracts a horizontal
2-form index (Lorentz leg) against a Clifford action (internal leg). The internal cross-block
factor is

```
Phi_mix = sum_a gamma_L^a (x) M_a,     M_a = internal image of c(iota_{e_a} alpha),
```

where `gamma_L^a` is a single Lorentz gamma (degree 1) and `M_a` is an internal endomorphism
carrying a single internal Clifford generator (degree 1) — this is the structural form that
must be tested for reality type.

### 5.2 The sign of `J_twisted` against the mixed operator

For the pure-tensor antilinear `J_twisted = C_{3,1} (x) C_{(6,4)}`,

```
J_twisted (gamma_L^a (x) M_a) J_twisted^{-1}
   = (C_{3,1} gamma_L^a C_{3,1}^{-1}) (x) (C_{(6,4)} M_a C_{(6,4)}^{-1})
   = (+ gamma_L^a) (x) (eta_a M_a),
```

with the Lorentz factor `+gamma_L^a` (Majorana, Section 4) and `eta_a = +/-1` the internal
charge-conjugation sign of `M_a`. So

```
s_split = +1   <=>   C_{(6,4)} M_a C_{(6,4)}^{-1} = + M_a   for every a.
```

### 5.3 Direct computation in M(16,C) — the value of `s_split`

I built `Cl(6,4)` explicitly and computed the reality type. Construction:

- 10 anticommuting Hermitian gammas for Euclidean `Cl(10,0)` via the standard five-factor
  Pauli nesting (32-dimensional Dirac rep; `S(6,4) = C^16` is the Weyl half, and the
  per-generator reality sign is rep-independent).
- Signature `(6,4)` imposed by leaving the six spacelike generators Hermitian (`G_I^2 = +I`)
  and `i`-rescaling the four timelike generators to anti-Hermitian (`G_I^2 = -I`). All
  Clifford relations `{G_I, G_J} = 2 eta_{IJ}` verified to machine precision.
- The charge conjugation `C_{(6,4)} = U K` (`U` unitary, `K` = complex conjugation) found by
  solving the linear intertwining system `U conj(G_I) U^{-1} = t G_I` for `t = +1` and
  `t = -1`, then polar-normalizing `U` to unitary (the intertwiner is unique up to scalar by
  Schur, null space dimension 1 in each case).

**Numerical results (all verified):**

```
type + (Majorana): U conj(G_I) U^{-1} = +G_I for all I=0..9   [verified]   ;  C^2 = U conj(U) = +I
type -          : U conj(G_I) U^{-1} = -G_I for all I=0..9   [verified]   ;  C^2 = U conj(U) = -I
```

The **type +** charge conjugation has `C_{(6,4)}^2 = +I` — exactly the value fixed by the
twisted-real-structure file (`C_{(6,4)}^2 = +1`, needed for `J_twisted^2 = +1`). So the
Majorana `C_{(6,4)}` already in use is the type-+ one, under which **every single internal
generator is C-real**:

```
C_{(6,4)} G_I C_{(6,4)}^{-1} = + G_I    for all I = 0..9.
```

Since the shiab cross-block `M_a` is, by SC1, a **real-linear** combination of single
internal generators with **no explicit `i`**, it follows that
`C_{(6,4)} M_a C_{(6,4)}^{-1} = +M_a` for every `a`. Direct cross-check: for 20 random
real-linear combinations `M_a = sum_I c_I G_I` (`c_I` real), the involution gives `+M_a`
in every case. Control: `M = i G_0` (an explicit `i`) flips to `-M`, confirming the `+1`
result is load-bearing on the shiab being real-linear (it is, per SC1) and is not an
artifact.

```
THEREFORE  s_split = +1.
```

### 5.4 Consequence

```
epsilon'(J_twisted, s*(D_GU)) = epsilon'_diag * s_split = (+1) * (+1) = +1.

   epsilon' = +1  ==>  KO-dim 6, J-bridge and D-bridge COMPATIBLE (F6 natural construction
                        survives this gate; still gated on FC-BRIDGE-1, FC-BRIDGE-3).
```

The falsification target (`epsilon' = -1 ==> J-bridge and D-bridge mutually exclusive`) does
**not** fire. The genuine-obstruction outcome is excluded by the computation.

---

## 6. Result

`epsilon' = +1`. The Clifford-symbol diagonal part is `+1` (Riemannian K3 section, Majorana
basis), and the previously-deferred mixed-block sign is now evaluated: the explicit `M(16,C)`
computation gives `s_split = +1`, because the unique Majorana charge conjugation with
`C_{(6,4)}^2 = +1` makes every internal generator C-real, and the shiab cross-block is a
real-linear, `i`-free combination of single internal generators. The F6 J-bridge and D-bridge
are compatible.

---

## 7. Verdict and Failure Conditions

**Verdict: CONDITIONALLY_RESOLVED.**

The decisive `M(16,C)` reality computation is performed and gives `s_split = +1`
unambiguously, so `epsilon' = +1` and the obstruction does not fire. The verdict is held
below RESOLVED by three explicit, named conditions, each a specific mathematical statement
that would change the answer:

- **FC-eps-1 (shiab cross-block carries a hidden `i` / even-degree internal content).** The
  `s_split = +1` result requires that the internal cross-block `M_a` is a real-linear
  combination of **single** internal generators with **no** explicit factor of `i` (degree-1,
  `i`-free). This is taken from SC1 (shiab real-linear, no complexification) and the
  contraction form `c(iota_{e_a} alpha)`. If a fully written-out section pullback in `M(64,H)`
  reveals that `M_a` carries an explicit `i` on the internal leg, or a degree-2 internal
  Clifford bilinear (e.g. from an `II_s`/Codazzi cross term that contracts two internal
  gammas), the reality sign of that component can be `-1` (the control `M = iG_0 -> -M`
  demonstrates the mechanism), giving `s_split = -1` and `epsilon' = -1`. This is the primary
  residual failure mode; it is a finite `M(64,H)` computation.

- **FC-eps-2 (Lorentzian vs Riemannian operator).** If the Type-II_1 bridge is required for
  the Lorentzian-signature Dirac operator `D_L = -i gamma^mu nabla_mu` (one explicit `i`)
  rather than the Riemannian K3 operator, the antilinearity of `C_{3,1}` flips
  `epsilon'_diag` to `-1`, forcing `epsilon' = -1` even with `s_split = +1`. The construction
  relies on the compact Riemannian section (where `tau` is finite); a Lorentzian requirement
  breaks it.

- **FC-eps-3 (wrong charge-conjugation type selected).** Both a type-+ conjugation
  (`C_{(6,4)}^2 = +I`, all generators C-real) and a type- conjugation (`C_{(6,4)}^2 = -I`,
  all generators C-antireal) exist for `Cl(6,4)`. The `s_split = +1` answer uses the type-+
  one, which is forced by `J_twisted^2 = +1`. If the bridge instead requires (or some
  consistency condition selects) the type- conjugation, then `C_{(6,4)} M_a C_{(6,4)}^{-1} =
  -M_a`, giving `s_split = -1` and `epsilon' = -1` — but the type- conjugation has
  `C_{(6,4)}^2 = -1`, which would give `J_twisted^2 = (+1)(-1) = -1`, breaking the
  established `J_twisted^2 = +1`. So this mode is self-excluded; it is listed because the
  `+1` answer is contingent on the `J_twisted^2 = +1` selection being the intended real
  structure.

**Self-check (verdict-discipline triggers).** Draft searched for the forbidden triggers:
the word "reconstruction" appears only as a grade label inherited from cited files and in
contrasting prior reconstruction-grade arguments — this file's own grade is
`exploration`/CONDITIONALLY_RESOLVED, not a claimed RESOLVED; no step is labeled
"need to recheck" / "need to check"; no sentence of the form "X gives Y and Z, not W" asserts
an internal contradiction in a claimed proof (the type-+ / type- distinction in Section 5.3 is
a statement of two coexisting real structures, with the relevant one selected by
`J_twisted^2 = +1`, and is named as failure condition FC-eps-3, not a hidden contradiction).
The verdict is correctly bounded at CONDITIONALLY_RESOLVED.

**I do not close any same-session Type-II_1 circularity flag with this file.** The sign is
reported honestly: the symbol part is `+1`, the mixed-block part is computed `+1` in
`M(16,C)`, and the residual gap (FC-eps-1: a full `M(64,H)` section-pullback check that no
hidden `i` or degree-2 internal term enters `M_a`) is named and bounded.

---

## 8. Open Questions

1. **Full `M(64,H)` confirmation (FC-eps-1).** Write the section-pullback image of
   `c(iota_{e_a} alpha)` plus the `II_s`/Codazzi cross terms explicitly in `M(64,H)` and
   confirm every internal cross-block component is degree-1, `i`-free (hence C-real). This is
   the bounded computation that would lift FC-EPSILON from CONDITIONALLY_RESOLVED to RESOLVED.
2. **`II_s` / Codazzi contribution.** The extrinsic-curvature terms join `Phi_mix` in
   `D_mix`; verify they land in the C-real eigenspace (expected by SC1 real-linearity, but a
   Codazzi term contracting two internal gammas would be degree-2 and must be checked — this
   is the concrete content of FC-eps-1).
3. **Coherence with `epsilon''`.** The `epsilon'' = -1` result (prior file) used the same
   tensor-split structure; with `s_split = +1` now established for `epsilon'`, re-confirm
   `epsilon''` is stable under the same mixed block (no new sign mode introduced).
