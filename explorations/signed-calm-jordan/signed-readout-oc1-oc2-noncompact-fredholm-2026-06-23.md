---
title: "Signed-Readout OC1/OC2: Non-Compact L2 Fredholm Stability and H-Linear Classification"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "signed-readout-oc1-oc2-noncompact-fredholm"
verdict: SHARPENED_TO_CONDITIONAL_THEOREM
---

# Signed-Readout OC1/OC2: Non-Compact L2 Fredholm Stability and H-Linear Classification

## 1. Task

This note runs OC1 and OC2 from
`explorations/signed-calm-jordan/signed-readout-theorem-statement-2026-06-23.md`.

The two open conditions are:

- **OC1:** sharpen Atiyah-Jannich stability in the non-compact `L^2` setting.
- **OC2:** sharpen the `H`-linear Fredholm classification for non-compact `Y^14`.

Inputs read:

- `explorations/signed-calm-jordan/signed-readout-theorem-statement-2026-06-23.md`
- `explorations/signed-calm-jordan/signed-readout-oq2a-k-theory-lift-2026-06-23.md`
- `explorations/signed-calm-jordan/signed-readout-oq2d-gu-contact-2026-06-23.md`
- `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`
- `explorations/analytic-index-fredholm/n5-ind-h-analytic-conditions-2026-06-22.md`
- `explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md`

No web browsing was used. The claims below use only local notes plus the standard shape
of Atiyah-Jannich/Fredholm classifying-space theorems.

---

## 2. Executive Verdict

**OC1 verdict: SHARPENED, CONDITIONAL.**

Atiyah-Jannich stability itself does **not** require `Y^14` to be compact. It is a
statement about continuous maps into a Fredholm-operator space on a fixed separable
Hilbert space. Thus `L^2(Y^14,S)` is an acceptable Hilbert space once fixed.

The real open analytic condition is not "extend Atiyah-Jannich to non-compact `Y^14`."
It is:

> prove that the GU operators, after choosing Sobolev domains or bounded transforms,
> define a continuous family of Fredholm operators on the fixed `L^2` Hilbert space,
> and that the family does not leave the Fredholm locus.

**OC2 verdict: SHARPENED, CONDITIONAL.**

The `H`-linear Fredholm classification also does **not** fail because `Y^14` is
non-compact. For any fixed infinite-dimensional separable quaternionic Hilbert space
`K_H`, the space `Fred_H(K_H)` classifies `KSp^0 = KO^4`.

The real open condition is:

> prove that the GU Dirac family gives a continuous map from the chosen observer
> parameter space into `Fred_H(L^2(Y^14,H^64))`.

For non-compact parameter spaces, one must either restrict to compact parameter
subspaces or supply a continuous extension to a compactification. A one-point
compactification is not automatic.

---

## 3. Local Evidence

The theorem statement records OC1/OC2 as the remaining gates for Parts Z and K. OQ2-A
already identifies the right target group:

```text
[D] in KSp^0(X) = KO^4(X)
```

and explains that `H`-linearity of `S = H^64` selects `KSp`, not `K^0` or `KO^0`.

OQ2-D gives the signed-readout contact for the GU sector:

- `G_R^{GU}` is a 24-node record graph, with no causal edges and weight `1` per node.
- The GU case is monotone: `R_- = 0`, `R = R_+ = 24`.
- The remaining topological-protection gate is exactly "Atiyah-Jannich in the
  non-compact `L^2` setting."

The later `n5-discrete-series` and `rc1` notes sharpen the Fredholm input:

- split-rank for `(SL(4,R), SO_0(3,1))` is verified as `1` by explicit bracket
  computation;
- Flensted-Jensen gives a non-trivial relative discrete sector;
- the RS sector is conditionally placed at the discrete pole `nu_1 = 3/2`;
- `ind_H(S_R^{eff}) = 8` and `ind_H(D_GU) = 16 + 8 = 24` are reconstruction-grade;
- the remaining gates are CAS/root-multiplicity/parabolic-induction checks and the
  analytic Fredholm implementation.

The earlier `n5-ind-h-analytic-conditions` note is more conservative and remains useful:
standard compact-fiber families index theorems do not directly apply to
`GL(4,R)/O(3,1)`. The non-compact issue is reduced to Fredholmness of the `L^2` fiber
operator, not solved by topology alone.

---

## 4. OC1: Atiyah-Jannich Stability in Non-Compact L2

### 4.1 Sharpened Claim

Let `K_H = L^2(Y^14,S)` be the fixed quaternionic Hilbert space, with
`S = H^64`. Let `A_t`, `t in T`, be a family of GU data, and let `D_t` be the
corresponding closed `H`-linear Dirac-type operators. If the bounded transforms

```text
F_t = D_t(1 + D_t^*D_t)^(-1/2)
```

define a continuous map

```text
T -> Fred_H(K_H)
```

in norm topology, or in a standard equivalent gap/graph topology strong enough to
make the bounded transform continuous, then:

1. `ind_H(F_t)` is locally constant on `T`;
2. along every connected path inside the Fredholm locus, `ind_H(D_t)` is constant;
3. for the GU 24-node monotone readout, the signed-readout integer `R(e_max)=24`
   is stable on any connected parameter component satisfying these assumptions.

This is the standard Atiyah-Jannich stability mechanism. Compactness of `Y^14` is
not part of the classifying-space theorem. Compactness matters only insofar as it is
a common way to prove elliptic Fredholmness.

### 4.2 Exact Assumptions Needed

OC1 needs all of the following:

**OC1-A1: Fixed Hilbert model.** The varying geometric `L^2` spaces are identified
unitarily with one fixed separable quaternionic Hilbert space
`K_H = L^2(Y^14,H^64)`.

**OC1-A2: Closed densely-defined operators.** Each `D_t` is closed, densely defined,
and has a specified Sobolev domain, or is replaced by its bounded transform `F_t`.

**OC1-A3: Fredholmness.** Each `F_t` lies in `Fred_H(K_H)`: finite-dimensional
`H`-kernel, finite-dimensional `H`-cokernel, and closed range. In the local notes,
this is expected from the Flensted-Jensen/Atiyah-Schmid discrete-series mechanism,
not from compact elliptic theory.

**OC1-A4: Continuity.** The map `t |-> F_t` is continuous in the topology used for
Fredholm stability. For unbounded operators, graph/gap/resolvent continuity must be
strong enough to imply bounded-transform continuity.

**OC1-A5: No escape from Fredholm locus.** The path must not hit essential spectrum
at zero, lose the discrete-series summand, or allow the range to stop being closed.

**OC1-A6: Discrete-sector compatibility.** If the index is computed only on
`L^2_disc`, the projection to `L^2_disc` must be invariant or vary continuously, and
the operator restricted to that sector must be the Fredholm operator whose index is
being read.

### 4.3 What Can Be Claimed Now

Claimable now:

- Atiyah-Jannich stability applies to non-compact `Y^14` **once** the GU family is
  realized as a continuous family in `Fred_H(L^2(Y^14,H^64))`.
- The local notes give reconstruction-grade evidence for the Fredholm input through
  the relative discrete-series route.
- The non-compactness issue should be restated as a Fredholmness/continuity problem,
  not as a defect in Atiyah-Jannich itself.

Not claimable yet:

- an unconditional theorem that `D_GU(A)` is Fredholm for all gauge fields `A`;
- an unconditional theorem that `ind_H(D_GU(A)) = 24` on the full, unreduced `L^2`
  space rather than on the controlled discrete sector;
- stability across deformations that change the asymptotic operator, close the
  spectral gap, or move discrete summands into continuous spectrum.

### 4.4 OC1 Failure Conditions

OC1 fails if any of the following occurs:

- `D_t` is not Fredholm for some `t`.
- zero enters the essential spectrum.
- the `L^2_disc` sector is not invariant under `D_t`.
- the family is not continuous in graph/gap/bounded-transform topology.
- domains vary without a controlled trivialization.
- the deformation changes the asymptotic geometry of `Y^14` enough to destroy
  invertibility at infinity or the relative discrete-series sector.
- the claimed index uses formal-degree density on a continuous spectrum rather than
  a discrete Fredholm summand.

---

## 5. OC2: H-Linear Fredholm Classification for Non-Compact Y14

### 5.1 Sharpened Claim

Let `K_H = L^2(Y^14,H^64)` be the fixed quaternionic Hilbert space. For any compact
Hausdorff observer parameter space `X`, a continuous family

```text
F: X -> Fred_H(K_H)
```

defines a class

```text
[F] in [X, Fred_H(K_H)] = KSp^0(X) = KO^4(X).
```

The augmentation at a point sends this class to the quaternionic Fredholm index:

```text
eps([F]) = ind_H(F_x) in KSp^0(pt) = Z.
```

This is the correct formal home for the GU signed-readout lift. Non-compactness of
`Y^14` does not alter the classifying space once `K_H` is fixed.

### 5.2 Exact Assumptions Needed

**OC2-A1: Quaternionic Hilbert space.** `L^2(Y^14,S)` carries a right `H`-Hilbert
structure, with `S = H^64`.

**OC2-A2: H-linearity.** Each operator commutes with right multiplication by `H`.
Equivalently, the connection and all projections used in gauge fixing preserve the
`Sp(64)`/quaternionic structure.

**OC2-A3: H-Fredholmness.** The bounded transforms lie in `Fred_H(K_H)`.

**OC2-A4: Continuous family.** The observer data define a continuous map into
`Fred_H(K_H)`.

**OC2-A5: Compact parameter space, or controlled compactification.** If the observer
space is non-compact, one must either:

- restrict to compact parameter subspaces;
- use compactly supported `KSp` theory;
- prove a continuous extension to a chosen compactification.

A one-point compactification only works if the family has a well-defined Fredholm
limit at infinity.

**OC2-A6: Kernel/cokernel interpretation.** The expression
`[ker D] - [coker D]` is an honest virtual bundle only when kernel/cokernel can be
stabilized over `X`. The classifying-space construction still gives the index class
even when raw kernel dimensions jump.

### 5.3 What Can Be Claimed Now

Claimable now:

- The target group for the GU family is `KSp^0(X)=KO^4(X)`, not `K^0(X)` or `KO^0(X)`,
  provided `H`-linearity is preserved.
- The non-compactness of `Y^14` does not block the `Fred_H` classification.
- The integer 24 is the augmentation of a possible `KSp^0` class on any compact
  parameter space satisfying OC2-A1 through OC2-A6.

Not claimable yet:

- a global `KSp^0(M^{GU})` class over the full non-compact GU moduli without a
  specified compactification or compact-support condition;
- an honest 24-rank quaternionic kernel bundle over the full observer space unless
  constant-rank/stabilization hypotheses are verified;
- `KSp` classification if the GU connection or gauge fixing breaks `H`-linearity.

### 5.4 OC2 Failure Conditions

OC2 fails or downgrades if:

- a gauge field breaks the `Sp(64)` structure and the operator is only complex-linear;
- gamma-trace or RS gauge-fixing projections are not `H`-linear;
- the bounded transform is not Fredholm;
- no fixed Hilbert-space trivialization is provided for varying metrics;
- the parameter space is non-compact and the family has no continuous Fredholm limit
  at infinity;
- the kernel dimension jumps in a way not handled by stabilization;
- the index is computed on a sector that is not invariant under the full operator.

---

## 6. Combined Conditional Theorem

**Theorem shape.** Suppose `X` is a compact Hausdorff observer parameter space and
`D_x` is a family of GU Dirac-type operators on `Y^14` satisfying:

1. `D_x` acts on the fixed quaternionic Hilbert space `L^2(Y^14,H^64)`;
2. `D_x` is `H`-linear for every `x`;
3. the bounded transforms `F_x = D_x(1 + D_x^*D_x)^(-1/2)` form a continuous map
   `X -> Fred_H(L^2(Y^14,H^64))`;
4. the Fredholm property is supplied by the relative discrete-series mechanism or
   another valid non-compact Fredholm criterion;
5. the GU 24-node record graph is the correct discrete-sector readout.

Then:

```text
[D] := [F] in KSp^0(X) = KO^4(X)
```

is well-defined, `ind_H(D_x)` is locally constant on connected components of `X`, and
the point augmentation recovers the signed-readout integer:

```text
eps_x([D]) = ind_H(D_x) = R(e_max) = 24
```

on the GU component where the local discrete-series computation applies.

This theorem is the strongest current claim supported by the local notes.

---

## 7. Next Action

The next action should not be another abstract Atiyah-Jannich citation. The needed
check is analytic:

1. Define the exact Sobolev domain and bounded transform for `D_GU(A)` on
   `L^2(Y^14,H^64)`.
2. Prove graph/gap continuity of `A |-> D_GU(A)` for the allowed gauge-field topology.
3. Prove Fredholmness on the relevant `L^2_disc` sector, including closed range and
   finite `H`-kernel/cokernel.
4. Verify that the discrete-sector projection is invariant or continuously transported
   under allowed deformations.
5. Separately, run the remaining CAS checks from the local notes:
   root multiplicities, parabolic-induction parameter `Lambda_RS^{FJ}=3/2`, and the
   Plancherel/Hom multiplicity count giving `16 + 8 = 24`.

Once these are done, OC1 and OC2 can be upgraded from conditional theorem shape to a
verified non-compact Fredholm implementation for the GU signed-readout theorem.

---

## 8. Final Verdict

**OC1:** conditionally resolved after sharpening. Atiyah-Jannich stability is already
the right theorem for a fixed `L^2` Hilbert space; the unresolved part is proving the
GU family is continuous and Fredholm in the non-compact `L^2` topology.

**OC2:** conditionally resolved after sharpening. `Fred_H` classifies `KSp^0=KO^4`
for the fixed quaternionic Hilbert space; the unresolved part is proving that the
non-compact GU Dirac family actually lands continuously in `Fred_H` over the chosen
compact parameter space or compactification.

**Overall:** `SHARPENED_TO_CONDITIONAL_THEOREM`. The local notes support the theorem
shape, but not an unconditional claim for all non-compact `Y^14` gauge-field data.
