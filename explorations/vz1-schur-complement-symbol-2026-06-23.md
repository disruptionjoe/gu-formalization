---
title: "VZ1: Schur Complement Symbol for the GU Rarita-Schwinger Sector"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
verdict: "RS_NON_INDEPENDENCE_CONFIRMED_IN_LOCAL_PRINCIPAL_SYMBOL_MODEL; FULL_14D_SCHUR_COMPLEMENT_OPEN"
---

# VZ1: Schur Complement Symbol for the GU Rarita-Schwinger Sector

## Purpose

This note executes the bounded next step named in
`explorations/vz1-62-persona-steelman-hegelian-2026-06-22.md`: compute the block
structure of `D_GU` in the Rarita-Schwinger/spin-1/2 decomposition and formulate the
Schur complement symbol.

The scope is deliberately narrow:

1. Work at the principal-symbol level of the rolled-up Dirac-DeRham-Einstein operator.
2. Test whether the horizontal spin-3/2 sector is a closed independent subsystem.
3. Compute the Schur complement as far as the existing operator specification permits.
4. Keep the null result live: a later 4D effective RS field can still trigger
   Velo-Zwanziger unless its effective characteristic matrix is causal or a guardian
   symmetry is constructed.

Discipline tags: `[verified]` means standard algebra or already established in the
repo; `[reconstruction]` means inferred from the current GU reconstruction with named
assumptions; `[open]` means a failure/closure condition remains.

## Inputs From Prior Notes

- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`:
  `Y^14` has signature `(9,5)`, `Cl(9,5) ~= M(64,H)`, spinor module `S = H^64`, and the
  shiab exists as a Clifford-contraction map.
- `explorations/generation-count-sm-branching-closure-2026-06-22.md`:
  the 4D RS sector is reconstructed as `RS(3,1) tensor S(6,4)`, with SM charges supplied
  by `S(6,4)`.
- `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md`:
  VZ does not directly apply to the full Dirac-type operator, but applies if an
  independent 4D RS field emerges.
- `explorations/vz1-62-persona-steelman-hegelian-2026-06-22.md`:
  the priority object is the Schur complement
  `D_RS^eff = D_RR - D_RQ (D_QQ)^(-1) D_QR`, where `Q` denotes non-RS sectors.

## Local Model And Assumptions

At a point of `Y^14`, split the cotangent space as

```text
T*Y = H* direct-sum N*
dim H = 4, signature(H) = (3,1)
dim N = 10, signature(N) = (6,4)
```

Here `H*` is the horizontal/pulled-back `X^4` direction and `N*` is the vertical metric
fiber direction. The horizontal Clifford matrices are denoted `gamma_a`, and
`gamma(xi) = xi_a gamma^a`.

The computed part of this note is for horizontal covectors `xi in H*`. This is the
right first test for the 4D-observable characteristic cone. The full 14D computation
must also include vertical covectors and vertical one-form components in the eliminated
block.

The rolled-up operator is taken in the form reconstructed in the generation-count note:

```text
E = (Omega^0(Y) tensor S+) direct-sum (Omega^1(Y) tensor S-)

D_GU(u, psi) = (d_A^* psi, d_A u + Phi(d_A psi))
```

Thus its principal symbol at a covector `xi` is

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
F_xi := sigma(Phi o d_A)(xi).
```

The connection `A` and its curvature are lower order for this first-order principal
symbol. They can still matter for a later constrained RS effective equation; this note
does not compute those lower-order VZ terms.

## Symbol Of The Shiab-Rolled Term

The shiab is

```text
Phi(alpha tensor s) = sum_a e^a tensor c(i_{e_a} alpha) s.
```

For a one-form input `beta tensor s`, the principal symbol of `Phi o d_A` is obtained by
setting `alpha = xi wedge beta`:

```text
i_{e_a}(xi wedge beta) = xi_a beta - beta_a xi
```

so

```text
F_xi(beta tensor s)
  = xi tensor c(beta)s - beta tensor c(xi)s.          (1)
```

For a general horizontal vector-spinor `psi = e^a tensor psi_a`, this is

```text
(F_xi psi)_a = xi_a gamma^b psi_b - gamma(xi) psi_a.  (2)
```

This formula is the main algebraic object in the note. It is independent of the lower
order connection and uses only the existing Clifford-contraction construction.

## RS Projection

Define the horizontal gamma trace

```text
Gamma(psi) = gamma^a psi_a.
```

The horizontal RS subspace is

```text
R = ker Gamma  subset H* tensor S(3,1) tensor S(6,4).
```

The gamma-trace spin-1/2 inclusion is

```text
j(s)_a = (1/4) gamma_a s,
Gamma(j(s)) = s.
```

The horizontal non-RS spin-1/2 trace subspace is `T = im j`. The full non-RS block `Q`
also contains `Omega^0 tensor S`, vertical one-forms `N* tensor S`, and any other
non-horizontal components.

## Non-Independence Test

Let `psi_R in R`, so `Gamma(psi_R) = 0`, and define

```text
chi = xi^a psi_a.
```

The scalar output of the principal symbol is

```text
i_xi psi_R = chi.
```

The one-form output from the shiab-rolled term is, by (2),

```text
(F_xi psi_R)_a = - gamma(xi) psi_a.
```

Its gamma trace is

```text
Gamma(F_xi psi_R)
  = - gamma^a gamma(xi) psi_a
  = -2 xi^a psi_a
  = -2 chi.                                          (3)
```

For generic `xi` and generic `psi_R`, `chi != 0`. Therefore a purely RS input produces:

```text
scalar spinor component      = chi
gamma-trace spin-1/2 output  = -2 chi
```

Both are outside the RS subspace. Hence the RS sector is not closed under the principal
symbol of the rolled-up `D_GU`.

Conversely, non-RS inputs also feed the RS output:

```text
P_R(xi tensor phi)_a
  = xi_a phi - (1/4) gamma_a gamma(xi) phi             (4)

P_R(F_xi j(s))_a
  = (1/2) xi_a s - (1/8) gamma_a gamma(xi) s.          (5)
```

Equations (3), (4), and (5) show that the off-diagonal blocks `D_QR` and `D_RQ` are
nonzero at the principal-symbol level.

**Verdict on independence.** Under the rolled-up operator model above, the 14D
horizontal RS sector is non-independent. It is not a closed first-order subsystem and
does not supply standalone RS Cauchy data at the native `D_GU` level. This is a
principal-symbol result, not merely a lower-order holonomy claim.

## Schur Complement: Formulation

Let `P_R` be the horizontal RS projection and `P_Q = 1 - P_R`. In block form,

```text
sigma_D(xi) =
  [ A(xi)  B(xi) ]
  [ C(xi)  E(xi) ]
```

where

```text
A = P_R sigma_D P_R
B = P_R sigma_D P_Q
C = P_Q sigma_D P_R
E = P_Q sigma_D P_Q.
```

The effective RS symbol is the Schur complement

```text
S_R(xi) = A(xi) - B(xi) E(xi)^(-1) C(xi),             (6)
```

provided `E(xi)` is invertible on the eliminated block. If `E(xi)` is not invertible,
the Schur complement is not defined and the correct object is the full block determinant
or a constrained Hamiltonian analysis.

This invertibility caveat is essential. A Schur complement is not a proof that the RS
sector is independent; it is a way to compute the symbol of an artificial effective RS
equation after non-RS variables have been integrated out.

## Computed Horizontal Minimal Schur Complement

The full `Q` block includes vertical one-forms. The computation below eliminates only the
minimal horizontal spin-1/2 block

```text
Q_min = (Omega^0 tensor S) direct-sum T,
T = gamma-trace horizontal one-forms.
```

This is not yet the full 14D Schur complement, but it is the bounded calculation directly
forced by the RS/gamma-trace decomposition.

For `psi in R`, `phi in Omega^0 tensor S`, and `s` the gamma-trace coordinate in
`j(s)`, the blocks are:

```text
A psi:
  (A psi)_a = - gamma(xi) psi_a + (1/2) gamma_a chi

C psi:
  C psi = (chi, -2 chi)

B(phi, s):
  (B(phi, s))_a =
      xi_a phi - (1/4) gamma_a gamma(xi) phi
    + (1/2) xi_a s - (1/8) gamma_a gamma(xi) s

E(phi, s):
  E(phi, s) =
    ( (1/4) gamma(xi) s,
      gamma(xi) phi + (3/2) gamma(xi) s )
```

Equivalently,

```text
E = gamma(xi) * [ [0, 1/4],
                  [1, 3/2] ].
```

Thus `E` is invertible whenever

```text
xi2 := g_H(xi, xi) != 0,
```

because `gamma(xi)^2 = xi2 * Id` and the scalar `2 x 2` matrix has determinant `-1/4`.

Solving `E(phi, s) = C psi` gives

```text
E^(-1) C psi =
  ( -8 gamma(xi) chi / xi2,
     4 gamma(xi) chi / xi2 ).
```

Substituting into (6) gives the horizontal minimal effective RS symbol:

```text
(S_R^hor(xi) psi)_a =
    - gamma(xi) psi_a
    + 6 (xi_a / xi2) gamma(xi) chi
    - gamma_a chi,                                    (7)

chi = xi^b psi_b,    Gamma(psi) = 0.
```

Sign conventions for `d_A^*` and for the ordering of the Clifford contraction can flip
some signs in (7). The nonzero off-diagonal conclusion and the off-null invertibility
test below do not depend on those convention choices.

### Off-Null Invertibility In The Minimal Model

Assume `xi2 != 0` and `S_R^hor(xi) psi = 0`. Multiplying (7) by `gamma(xi)/xi2` gives

```text
psi_a = 4 (xi_a / xi2) chi + (gamma_a gamma(xi) / xi2) chi.
```

Now impose the RS condition `Gamma(psi) = 0`:

```text
0 = Gamma(psi)
  = 8 gamma(xi) chi / xi2.
```

Since `xi2 != 0`, `gamma(xi)` is invertible, hence `chi = 0`, and then `psi = 0`.

Therefore, in this minimal horizontal model:

```text
ker S_R^hor(xi) = 0 for xi2 != 0.
```

So the computed effective horizontal RS symbol has no spacelike or timelike
characteristics in this model; its possible characteristic set is contained in
`g_H(xi, xi) = 0`.

This is weaker than proving a Clifford relation. On transverse RS data (`chi = 0`),
equation (7) reduces to

```text
S_R^hor(xi) psi = - gamma(xi) psi,
```

so the expected Clifford square holds there. On longitudinal gamma-traceless data
(`chi != 0`), the Schur complement contains rational projection terms. Thus the stronger
criterion

```text
(S_R^hor(xi))^2 = g_H(xi, xi) * Id_R
```

is not established and is probably the wrong literal criterion after integrating out
constraints. The determinant/characteristic test is the meaningful result of the
minimal Schur calculation.

## What Is Still Missing For The Full 14D Symbol

The full `Q` block is larger than `Q_min`. It includes:

1. vertical one-form components `N* tensor S`,
2. possible mixed horizontal/vertical form components if a fuller `Omega^*` model is used,
3. the exact chirality placement of `S+` and `S-` in the rolled-up complex,
4. the precise section-pullback projection used to define the 4D observable RS field.

For horizontal `xi`, vertical one-forms do not appear in `C psi_R`, but they do appear in
`B`: a vertical one-form input `eta tensor s` gives

```text
F_xi(eta tensor s)
  = xi tensor c(eta)s - eta tensor c(xi)s,
```

and the first term has a horizontal one-form component that can project onto `R`. Hence
the full `B E^(-1) C` may differ from (7) once the vertical part of `E` is included.

The complete 14D Schur complement therefore requires an explicit inversion of
`E(xi)` on

```text
Q = (Omega^0 tensor S) direct-sum T direct-sum (N* tensor S) direct-sum ...
```

This note does not claim that inversion has been done.

## VZ Consequences

### What This Supports

The local principal-symbol computation supports the strengthened 14D evasion candidate:

```text
The GU RS sector is not an independent Rarita-Schwinger field at the native 14D level.
```

Reason: a generic RS input is immediately sent into scalar spinor and spin-1/2 trace
components by the principal symbol of `D_GU`. This is exactly the failure of the
standalone-field hypothesis needed by the standard VZ setup.

The minimal horizontal Schur complement also gives a favorable first sign: after
eliminating the scalar and gamma-trace spin-1/2 variables, the effective horizontal RS
symbol is invertible for `g_H(xi, xi) != 0`. No spacelike characteristic appears in this
bounded model.

### What This Does Not Prove

This is not a final VZ evasion proof.

It does not prove:

- that the full 14D Schur complement is causal after vertical sectors are eliminated;
- that the section-pulled `s*(D_GU)` has a causal RS characteristic cone;
- that a low-energy 4D effective RS particle, if it decouples, has a guardian symmetry;
- that lower-order Sp(64) curvature terms cannot modify the constrained effective
  characteristic matrix in the standard VZ way;
- that the RS Kaluza-Klein spectrum never produces an approximately standalone RS field.

## Failure Conditions

The favorable conclusion above fails or becomes inapplicable if any of the following
conditions holds:

**F1. Operator-model failure.** The actual GU operator is not the rolled-up first-order
operator `D_GU(u,psi) = (d_A^* psi, d_A u + Phi(d_A psi))`, or the physical RS sector is
not contained in the horizontal gamma-traceless one-form component.

**F2. Full-block failure.** The full non-RS block `E(xi)` is singular for some spacelike
horizontal or 14D covector where the minimal `Q_min` block is invertible. Then the Schur
complement (6) cannot be used and spacelike characteristics may re-enter through the full
constraint system.

**F3. Vertical-sector failure.** Inverting the vertical part of `Q` changes (7) so that
the full `S_R(xi)` has kernel for some spacelike covector.

**F4. Section-pullback failure.** The 4D pullback `s*(D_GU)` may induce a different
effective RS symbol because of the second fundamental form/Codazzi corrections named in
`explorations/4d-reduction-section-pullback-2026-06-22.md`.

**F5. EFT-decoupling failure.** Even if the 14D system is non-independent, a low-energy
effective theory may integrate out `Q` and leave an approximately standalone charged RS
field. If that happens and no guardian symmetry appears, the usual VZ obstruction is back.

**F6. Curvature-constraint failure.** VZ pathologies often enter when constraints are
commuted and curvature terms alter the reduced characteristic matrix. This note computes
only the first-order principal symbol of `D_GU`; it does not commute constraints in a
curved Sp(64) or gimmel background.

## Bottom Line

**Result 1: non-independence.** In the local rolled-up principal-symbol model, the
horizontal spin-3/2 sector is not independent. The off-diagonal RS/non-RS blocks are
nonzero explicitly:

```text
C psi_R = (xi dot psi_R, -2 xi dot psi_R)
B(phi, s) != 0 generically.
```

So `D_GU` does not restrict to a closed standalone RS subsystem at 14D.

**Result 2: partial Schur complement.** The horizontal minimal Schur complement is
formula (7). It is invertible for `g_H(xi, xi) != 0`, so this bounded model has no
spacelike characteristics.

**Result 3: open full test.** The decisive full object remains:

```text
S_R^14D(xi) = A(xi) - B(xi) E(xi)^(-1) C(xi)
```

with `E` acting on the complete non-RS block, including vertical one-form sectors. That
full inversion is the next computation required before changing VZ1 from OPEN to
EVADED.

## References

- `explorations/vz1-velo-zwanziger-analysis-2026-06-22.md`
- `explorations/vz1-62-persona-steelman-hegelian-2026-06-22.md`
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`
- `explorations/n2-shiab-computation-spin77-branching-rules-2026-06-22.md`
- `explorations/generation-count-cl95-dirac-derham-2026-06-22.md`
- `explorations/generation-count-sm-branching-closure-2026-06-22.md`
- `explorations/4d-reduction-section-pullback-2026-06-22.md`
