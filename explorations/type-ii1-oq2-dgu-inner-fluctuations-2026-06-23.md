---
title: "Type II_1 OQ2: D_GU Inner-Fluctuation Analog and the Sp(64) Orbit"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "type-ii1-oq2-dgu-inner-fluctuations"
verdict: "CONDITIONAL_FAIL_FOR_CC_STYLE_SELECTION; GU_CONNECTION_ORBIT_IS_SP64_IF_SP64_BUNDLE_IS_INPUT"
depends_on:
  - "explorations/type-ii1-sm-checklist-tightening-2026-06-23.md"
  - "specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md"
  - "specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md"
  - "explorations/sc1-shiab-domain-codomain-2026-06-23.md"
  - "explorations/sc1-oq3-gauge-equivariance-2026-06-23.md"
  - "explorations/sc1-oq1-shiab-uniqueness-2026-06-23.md"
  - "explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md"
  - "explorations/codazzi-sp64-bundle-2026-06-23.md"
  - "explorations/codazzi-sp64-2026-06-23.md"
  - "explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md"
  - "explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
---

# Type II_1 OQ2: D_GU Inner-Fluctuation Analog and the Sp(64) Orbit

## 1. Question

Run OQ2 from `type-ii1-sm-checklist-tightening`: compute/analyze the
Connes-Chamseddine style

```text
D -> D + A + JAJ^{-1}
```

analog for the GU Dirac-DeRham operator on

```text
Y^14 = Met(X^4)
```

and ask what gauge group the fluctuation orbit generates.

The target gates are:

```text
F7.1  gauge group extraction
F7.2  Type II_1 compact Lie selection
FX.3  GU connection one-forms vs CC bimodule one-forms
```

## 2. Inputs Fixed by the Local Notes

The GU side has the following fixed data.

1. `Y^14` has signature `(9,5)`, so

   ```text
   Cl(9,5) ~= M(64,H),     S = H^64.
   ```

   This is resolved in the N1 signature audit and used throughout SC1.

2. The natural compact structure group of the quaternionic Hermitian spinor module
   is

   ```text
   Sp(64) = U(64,H),       dim_R sp(64) = 8256.
   ```

   The anomaly and IG/tau-plus notes treat this as the GU gauge group in the corrected
   `(9,5)` setting. It is selected by the Clifford/quaternionic spinor geometry, not
   by a Connes-Chamseddine inner-fluctuation computation.

3. SC1 fixes the shiab type:

   ```text
   Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S,
   Phi(alpha tensor psi) = sum_a e^a tensor c(iota_{e_a} alpha).psi.
   ```

   The gauge-equivariance pass upgrades this, in the physical ad-valued setting, to

   ```text
   Phi: Omega^2(Y^14, ad P) tensor S -> Omega^1(Y^14) tensor S
   ```

   with

   ```text
   Phi(Ad(g) alpha, rho(g) psi) = rho(g) Phi(alpha, psi)
   ```

   for `g in Sp(64)`.

4. The Codazzi notes assume a principal bundle

   ```text
   Sp(64) -> P -> Y^14
   ```

   with connection `A`, curvature `F_A`, and a tautological spin/Levi-Civita part
   `A^0`. They analyze the consequences of pulling this connection back along a
   section `s: X^4 -> Y^14`.

5. The Type II_1 checklist control item 7 is stricter: CC inner fluctuations must
   produce a one-form bimodule and recover `SU(3) x SU(2) x U(1) / Z_6`, or a specified
   enlargement, from the algebraic unitary orbit. In a Type II_1 factor, the unitary
   group is too large unless a separate compact Lie selection mechanism is supplied.

## 3. The GU Connection-Fluctuation Analog

Use the operator form established in SC1:

```text
D_GU(A) = d_A + d_A^* + Phi
```

where `A` is an `Sp(64)` connection on `P -> Y^14`, acting on the associated spinor
and form bundles through the defining representation and its adjoint action.

Choose a reference connection `A0` and write a fluctuation

```text
A = A0 + Psi,       Psi in Omega^1(Y^14, ad P).
```

Then, at the operator level,

```text
D_GU(A0 + Psi) - D_GU(A0)
  = (rho_*(Psi) wedge -) + (rho_*(Psi) wedge -)^*
```

up to the usual metric adjoint convention for the de Rham part. Equivalently, in a
Dirac-symbol presentation this is the zero-order Clifford contraction of the
connection one-form:

```text
c(Psi): Gamma(E) -> Gamma(E),
E = Lambda^bullet T^*Y^14 tensor S_P.
```

The shiab `Phi` is not the source of the first-order gauge fluctuation. It is a fixed
Clifford-contraction piece, and the SC1 gauge-equivariance note shows that it is
compatible with the `Sp(64)` action once its input is ad-valued.

So the closest GU analog of `D + A + JAJ^{-1}` is not literally produced by a universal
one-form `sum a_i[D,b_i]`. It is the affine connection shift:

```text
D_GU(A0) -> D_GU(A0 + Psi),
Psi in Omega^1(Y^14, ad P).
```

Gauge transformations act by the standard connection formula:

```text
A -> A^g = g A g^{-1} + g d g^{-1},       g in Gamma(Ad P).
```

Therefore the GU connection-fluctuation orbit is the orbit of `Conn(P)` under the
infinite-dimensional gauge group

```text
G_GU = Gamma(Ad P) ~= Maps(Y^14, Sp(64))        locally/trivially.
```

The finite fiber group is compact Lie `Sp(64)`. The orbit does not generate the SM
group; it generates the GU `Sp(64)` gauge orbit, provided the `Sp(64)` bundle has
already been chosen.

## 4. Comparison with CC Bimodule One-Forms

In the finite CC model:

```text
Omega_D^1(A) = { sum_i a_i [D,b_i] : a_i,b_i in A },
D_A = D + A + JAJ^{-1},
```

and the effective gauge group is extracted from the unitary group of the finite
algebra after quotienting the trivially acting center.

For the GU data there are three possible readings.

### Reading A: Algebra is C^\infty(Y^14)

Then

```text
[D_GU,f] = c(df)
```

produces ordinary scalar one-forms on `Y^14`, not arbitrary
`Omega^1(Y^14, ad P)` connection perturbations. The unitary group is
`Maps(Y^14,U(1))`, so it does not select `Sp(64)`.

Verdict: fails as a source of the GU gauge connection.

### Reading B: Algebra is sections of End_H(S_P)

If one instead takes something like

```text
A_GU = C^\infty(Y^14, End_H(S_P))
```

then its unitary group, after imposing the quaternionic Hermitian structure, has local
fiber `Sp(64)`. In that setting, commutators with a covariant Dirac operator can
produce endomorphism-valued one-forms, and the connection variation `Psi` can be
represented operatorially.

But this is not a derivation of `Sp(64)` from inner fluctuations. The algebra was
chosen so that its unitary group is already the `Sp(64)` gauge group. The CC-style
real structure, opposite action, order-one condition, and quotient by the trivially
acting center are also not supplied. Since the GU quaternionic `J` has `J^2=-1`, it
does not automatically play the CC KO-6 role where `J^2=+1`.

Verdict: possible operator-level embedding, not a completed CC bimodule calculus.

### Reading C: Type II_1 internal factor M

If the intended bridge is a Type II_1 spectral triple, then the inner-fluctuation
orbit is controlled by the unitary group `U(M)`, which is vastly larger than a compact
finite-dimensional Lie group. The local notes do not provide:

```text
N subset M              finite-index subfactor selecting Sp(64),
Phi_Connes              shadow functor selecting Sp(64),
or a proof that only Sp(64) acts nontrivially on D_GU.
```

Verdict: no Type II_1 compact-reduction mechanism is established here.

## 5. Is Sp(64) Selected?

Yes, but only in the GU Clifford-geometric sense:

```text
Cl(9,5) ~= M(64,H), S = H^64
=> compact quaternionic-unitary automorphism group Sp(64).
```

This is a structure-group selection. It is the selection used by the anomaly,
IG/tau-plus, SC1 gauge-equivariance, and Codazzi notes.

No, not in the CC inner-fluctuation sense. The current local sources do not show that
the orbit

```text
D_GU -> D_GU + mathcal A + J mathcal A J^{-1}
```

for a specified spectral algebra has `Sp(64)` as its recovered compact gauge group.
The closest proven statement is:

```text
If P is already an Sp(64)-bundle, then D_GU(A) is Sp(64)-gauge-covariant,
and connection fluctuations have orbit Gamma(Ad P).
```

That is compatibility, not algebraic recovery.

## 6. Gate Verdicts

### F7.1: Gauge Group Extraction

**Verdict: CONDITIONAL / FAIL against the finite CC target.**

Computed orbit:

```text
Conn(P) / Gamma(Ad P),     fiber group Sp(64),
```

assuming the GU principal `Sp(64)` bundle is part of the input. This is a compact
Lie fiber group and therefore a coherent specified enlargement of the SM gauge group.

It does not pass the CC control target because it does not recover
`SU(3) x SU(2) x U(1) / Z_6`, and the local notes do not supply a spontaneous-breaking
or Connes-channel map from the `Sp(64)` orbit to the SM gauge group.

### F7.2: Type II_1 Selection Problem

**Verdict: FAIL for the current Type II_1 bridge.**

The current computation does not reduce the unitary group of a Type II_1 factor to a
compact Lie-group orbit by any of the three allowed routes:

```text
(a) Jones subfactor selection,
(b) Connes-channel shadow,
(c) direct proof that only a compact Lie subgroup acts nontrivially on D.
```

The GU notes solve a different problem: they start with the finite-dimensional compact
structure group `Sp(64)` selected by the quaternionic spinor module. That does not
discharge the Type II_1 unitary-selection gate.

### FX.3: Inner-Fluctuation Compatibility

**Verdict: CONDITIONAL_FAIL / OPEN.**

There is a natural operator-level map

```text
Psi in Omega^1(Y^14, ad P)
  |-> D_GU(A0 + Psi) - D_GU(A0),
```

so GU gauge connections do map to connection-one-form perturbations of `D_GU`.

But no canonical functor has been specified that maps these GU connection one-forms
to CC bimodule one-forms

```text
sum_i a_i [D,b_i]
```

with a compatible `J`, opposite action, order-one condition, and gauge-group quotient.
For `C^\infty(Y^14)` the map fails to produce `ad P`-valued one-forms. For
`C^\infty(Y^14,End_H(S_P))` it becomes plausible only by building the `Sp(64)` data
into the algebra.

Thus FX.3 is not a pass. It is a precise open construction problem.

## 7. What Remains Open

1. **Algebra choice.** Specify the spectral algebra `A_GU` whose universal or represented
   one-forms are meant to reproduce `Omega^1(Y^14, ad P)`.

2. **Real structure.** Define the `J` used in `JAJ^{-1}`. The GU quaternionic structure
   has `J^2=-1`; the CC finite KO-6 control has `J^2=+1`. The bridge cannot ignore this.

3. **Order-one test.** Check whether the proposed `A_GU` satisfies the order-zero and
   order-one conditions with `D_GU`.

4. **Gauge quotient.** Compute the actual unitary orbit and quotient by trivially acting
   center/commutant. This is where CC recovers the exact SM quotient.

5. **SM reduction.** If `Sp(64)` is the specified enlargement, produce the mechanism
   taking the observer-facing shadow to `SU(3) x SU(2) x U(1) / Z_6` with correct
   hypercharge normalization.

6. **Type II_1 reduction.** If a Type II_1 factor is introduced, provide the compact
   Lie selection mechanism required by F7.2. GU's Clifford-geometric `Sp(64)` selection
   is not enough by itself.

## 8. Bottom Line

The bounded computation gives a clean split:

```text
GU connection calculus:
  D_GU(A0) -> D_GU(A0 + Psi), Psi in Omega^1(ad P)
  orbit under Gamma(Ad P), fiber group Sp(64).

CC/Type-II_1 inner-fluctuation calculus:
  not constructed for D_GU; no algebraic derivation of Sp(64) or SM gauge group yet.
```

So `Sp(64)` is selected by the corrected GU Clifford/quaternionic spinor geometry and
is compatible with the shiab, tau-plus, and Codazzi structures. It is not currently
selected by a Connes-Chamseddine or Type II_1 inner-fluctuation orbit.

