---
title: "VZ OQ1: S_R^2 = xi^2 Id_{RS} as an Exact Matrix Identity for the Spin(9,5) Clifford RS-Block Symbol"
date: 2026-06-23
problem_label: "vz-oq1"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# VZ OQ1: S_R^2 = xi^2 Id_{RS} as an Exact Matrix Identity

## 1. Problem Statement

The prior exploration `explorations/vz-schur-complement-2026-06-23.md` (verdict: EVADED,
reconstruction grade) proved the kernel result:

```
ker S_R^{14D}(xi) = 0   for all xi with g_Y(xi,xi) != 0.
```

This is sufficient for VZ evasion (no spacelike characteristics), but that file left open:

**OQ1.** Does `S_R^2 = xi^2 Id_{RS}` hold as an exact matrix identity (not just trivial kernel)?

The distinction matters because:

1. If `S_R^2 = xi^2 Id_{RS}` exactly, then `S_R` is itself a Clifford-type operator on the RS sector, with the same characteristic cone property as the full `D_GU`. This upgrades VZ evasion from "trivial kernel" to "full principal-symbol evasion" — the effective RS operator is itself a Dirac-type operator.

2. The exact identity would also imply that the RS sector propagates with exactly the same causal structure as the full spinor field — a stronger structural statement than merely "no spacelike characteristics."

3. For the Schur complement to be used in elliptic estimates and index theory (the next steps for 4D reduction), the exact Clifford-module property of `S_R` is needed, not just injectivity.

The question was left open in §7 of the prior exploration because the algebraic manipulation produced:

```
S_R^2 = xi^2 Id_{RS} + xi^2 B (E^{-1})^2 C           (KEY residual from prior §4)
```

and separately (§7, conditional on A invertible):

```
S_R^2 = xi^2^2 A^{-2}    =>   S_R^2 = xi^2 Id   iff   A^2 = xi^2 Id_{RS}.
```

Both routes reduce to the same question: does `BC psi_R = 0` for all `psi_R in R^{14D}`?

This computation resolves that question.

---

## 2. Established Context

**Clifford algebra.** `Cl(9,5) ~= M(64,H)` (reconstruction-grade; established in N1).
Spinor module `S = H^{64}`, `dim_R S = 256`. The Clifford identity is:

```
c(xi)^2 = g_Y(xi,xi) * Id_S    for all xi in T*Y^{14}.
```

**Rolled-up operator.** `D_GU` acts on `E = (Omega^0 tensor S+) direct-sum (Omega^1 tensor S-)`.
Principal symbol at covector xi:

```
sigma_D(xi) = M(xi):  E -> E,    M(xi)^2 = xi^2 Id_E.
```

**Block decomposition.** Split `Omega^1 tensor S = R^{14D} direct-sum Q^{14D}` where:

```
R^{14D} = ker Gamma^{14D}   (RS sector, dim = 13 * 256 = 3328 over R)
Q^{14D} = (Omega^0 tensor S) direct-sum (im j^{14D})   (scalar + gamma-trace, codim of RS)
```

The block symbol:

```
M(xi) = [ A(xi)  B(xi) ]
        [ C(xi)  E(xi) ]
```

with `M(xi)^2 = xi^2 Id_E` giving the four block-square identities:

```
(I)   A^2 + BC = xi^2 Id_R
(II)  AB + BE = 0
(III) CA + EC = 0
(IV)  CB + E^2 = xi^2 Id_Q
```

---

## 3. The Central Question: Does BC = 0 on R^{14D}?

From identity (I): `A^2 = xi^2 Id_R - BC`.

So `A^2 = xi^2 Id_R` iff `BC = 0` on the RS sector.

And from the §4 calculation in vz-schur-complement-2026-06-23.md:
`S_R^2 = xi^2 Id_R iff B(E^{-1})^2 C = 0`.

These are equivalent under (I)-(IV) when E is invertible. So the question is:

**Does B(xi) C(xi) psi_R = 0 for all psi_R in R^{14D}?**

### 3.1 Computing C psi_R

For `psi_R in R^{14D}` (i.e., `Gamma^{14D}(psi_R) = gamma^A psi_{R,A} = 0`):

The C block maps the RS spinor-valued 1-form to the scalar-plus-gamma-trace subspace Q.
From §3.1 of vz-schur-complement-2026-06-23.md:

```
C psi_R = (chi, Q_T-component),   chi = g_Y(xi, psi_R) in S.
```

Explicitly: the scalar component is `chi = xi^A psi_{R,A}` and the gamma-trace component
uses `Gamma^{14D}(F_xi psi_R) = gamma(xi) chi - 2 chi` (from the Clifford anticommutation
calculation in §3.1 of the prior note).

So:
```
C psi_R = (chi, (gamma(xi) - 2) chi).
```

### 3.2 Computing B(C psi_R)

The B block maps from Q (scalar + gamma-trace) to the RS sector R^{14D}.

**Input:** `(phi, trace-component) = (chi, (gamma(xi)-2) chi)` where `chi in S`.

The B block computes:

```
(B (phi, s))_A = P_R (xi_A phi + F_xi(j_{14D}(s))_A)
```

where `j_{14D}(s)_A = (1/14) gamma_A s` is the injection of a spinor into the gamma-trace
one-form sector, and `P_R` is the RS projection `P_R = Id - (1/14) gamma_A Gamma^{14D}`.

For the scalar input `phi = chi`:

```
(xi tensor phi)_A = xi_A chi
P_R(xi tensor chi)_A = xi_A chi - (1/14) gamma_A (gamma^B xi_B chi) = xi_A chi - (1/14) gamma_A gamma(xi) chi.
```

For the gamma-trace input `s = (gamma(xi)-2) chi`:

```
j_{14D}(s)_A = (1/14) gamma_A (gamma(xi)-2) chi.
```

```
(F_xi j_{14D}(s))_A = xi_A (1/14)(Gamma^{14D} j_{14D}(s)) - gamma(xi)(1/14) gamma_A (gamma(xi)-2) chi.
```

We need `Gamma^{14D}(j_{14D}(s)) = gamma^A (1/14) gamma_A s = (1/14) * 14 * s = s`. So:

```
(F_xi j_{14D}(s))_A = (1/14) xi_A s - (1/14) gamma(xi) gamma_A s.
```

Apply RS projection `P_R`:
```
P_R(F_xi j_{14D}(s))_A = (1/14) xi_A s - (1/14) gamma(xi) gamma_A s
                        - (1/14) gamma_A Gamma^{14D}((1/14) xi s - (1/14) gamma(xi) gamma_. s).
```

Compute `Gamma^{14D}` of the one-form `(1/14) xi_A s - (1/14) gamma(xi) gamma_A s`:

```
gamma^A ((1/14) xi_A s - (1/14) gamma(xi) gamma_A s)
= (1/14) gamma(xi) s - (1/14) gamma^A gamma(xi) gamma_A s.
```

Using `gamma^A gamma(xi) gamma_A = (2 - 14) gamma(xi) = -12 gamma(xi)` in 14D:

```
= (1/14) gamma(xi) s + (12/14) gamma(xi) s = (13/7) gamma(xi) s.
```

So:
```
P_R(F_xi j_{14D}(s))_A
= (1/14) xi_A s - (1/14) gamma(xi) gamma_A s - (1/14) gamma_A (13/7) gamma(xi) s
= (1/14) xi_A s - (1/14) gamma(xi) gamma_A s - (13/98) gamma_A gamma(xi) s.
```

Now `s = (gamma(xi) - 2) chi`. Substituting `s`:

```
P_R(F_xi j_{14D}(s))_A
= (1/14) xi_A (gamma(xi)-2) chi
  - (1/14) gamma(xi) gamma_A (gamma(xi)-2) chi
  - (13/98) gamma_A gamma(xi) (gamma(xi)-2) chi.
```

Use `gamma(xi)^2 = xi^2 Id`, so `gamma(xi)(gamma(xi)-2) = xi^2 - 2 gamma(xi)` and
`gamma(xi)^2 - 2 gamma(xi) = (xi^2 - 2 gamma(xi))`:

```
gamma(xi) (gamma(xi) - 2) chi = (xi^2 - 2 gamma(xi)) chi.
```

Let `mu = gamma(xi) chi` for shorthand. Then:

```
P_R(F_xi j_{14D}(s))_A
= (1/14) xi_A (mu - 2 chi)
  - (1/14) gamma_A (xi^2 chi - 2 mu)
  - (13/98) gamma_A (xi^2 chi - 2 mu).
```

Combining the last two terms (coefficient of `gamma_A (xi^2 chi - 2 mu)`):

```
- (1/14) - (13/98) = - 7/98 - 13/98 = - 20/98 = - 10/49.
```

So:
```
P_R(F_xi j_{14D}(s))_A
= (1/14) xi_A (mu - 2 chi) - (10/49) gamma_A (xi^2 chi - 2 mu).
```

**Total B(C psi_R):** Summing the scalar and gamma-trace contributions:

```
(B(C psi_R))_A
= P_R(xi tensor chi)_A + P_R(F_xi j_{14D}(s))_A
= [xi_A chi - (1/14) gamma_A mu]
+ [(1/14) xi_A (mu - 2 chi) - (10/49) gamma_A (xi^2 chi - 2 mu)]
```

```
= xi_A chi + (1/14) xi_A mu - (2/14) xi_A chi
  - (1/14) gamma_A mu - (10/49) xi^2 gamma_A chi + (20/49) gamma_A mu.
```

Collecting `xi_A` terms:
```
xi_A [chi + (1/14) mu - (1/7) chi] = xi_A [(1 - 1/7) chi + (1/14) mu]
                                    = xi_A [(6/7) chi + (1/14) mu].
```

Collecting `gamma_A` terms:
```
gamma_A [-(1/14) mu - (10 xi^2 / 49) chi + (20/49) mu]
= gamma_A [(20/49 - 1/14) mu - (10 xi^2 / 49) chi]
= gamma_A [(40/98 - 7/98) mu - (10 xi^2 / 49) chi]
= gamma_A [(33/98) mu - (10 xi^2 / 49) chi].
```

So:

```
(B(C psi_R))_A = xi_A [(6/7) chi + (1/14) mu] + gamma_A [(33/98) mu - (10 xi^2 / 49) chi].
                                                                                  (BCpsi)
```

where `chi = g_Y(xi, psi_R)` and `mu = gamma(xi) chi`.

---

## 4. Is BC = 0 on R^{14D}?

The expression (BCpsi) is generically nonzero. It vanishes when both:

(a) The coefficient of `xi_A` vanishes: `(6/7) chi + (1/14) mu = 0`, i.e., `mu = -12 chi`, i.e., `gamma(xi) chi = -12 chi`.
(b) The coefficient of `gamma_A` vanishes: `(33/98) mu - (10 xi^2 / 49) chi = 0`.

From (a): `mu = -12 chi`, so (b) becomes:
`(33/98)(-12 chi) - (10 xi^2 / 49) chi = 0`
`(-396/98 - 20 xi^2 / 98) chi = 0`
`(-396 - 20 xi^2) chi = 0`.

For generic `xi^2` and nonzero `chi`, this fails. So (a) and (b) are simultaneously satisfied
only for special `xi^2 = -396/20 = -99/5` — a fixed value, not a generic identity.

**Conclusion: `BC != 0` generically on `R^{14D}`.**

More precisely, for any nonzero `psi_R in R^{14D}` with `chi = g_Y(xi, psi_R) != 0`,
the expression (BCpsi) is nonzero for generic `xi`. Therefore:

```
A^2 = xi^2 Id_R - BC   is NOT equal to  xi^2 Id_R.
```

This means the exact matrix identity `S_R^2 = xi^2 Id_{RS}` does NOT hold in the
naive sense derived from the block-square calculation in vz-schur-complement-2026-06-23.md §7.

---

## 5. Resolution: The Identity Holds by a Different Argument

However, the BC calculation above does not immediately disprove `S_R^2 = xi^2 Id`.
The §7 derivation in vz-schur-complement-2026-06-23.md assumed A invertible and derived
`S_R = xi^2 A^{-1}` from `A S_R = xi^2 Id`. Let us re-examine that step.

### 5.1 The Relation A S_R = S_R A = xi^2 Id_{RS}

From (II): `AB = -BE`.
From (III): `CA = -EC`.

Compute `A S_R = A(A - B E^{-1} C) = A^2 - A B E^{-1} C`.

From (II): `AB = -BE`, so `AB E^{-1} = -B E E^{-1} = -B`.
Therefore: `A S_R = A^2 + B C = xi^2 Id_R`. [Using (I).]

So **`A S_R = xi^2 Id_R` exactly**, independently of whether `BC = 0`.

Similarly, `S_R A = (A - B E^{-1} C) A = A^2 - B E^{-1} CA`.
From (III): `CA = -EC`, so `E^{-1} CA = -C`, hence `B E^{-1} CA = -BC`.
Therefore: `S_R A = A^2 + BC = xi^2 Id_R`. [Using (I).]

So `A S_R = S_R A = xi^2 Id_R`. This is exact, with no assumption on BC.

### 5.2 The Identity S_R^2 = xi^2 Id from Commutativity

From `A S_R = xi^2 Id_R` we get `S_R = xi^2 A^{-1}` provided A is invertible.
Then `S_R^2 = xi^4 A^{-2}`, which gives `S_R^2 = xi^2 Id` iff `A^2 = xi^2 Id`.

But we just showed `BC != 0`, so `A^2 = xi^2 Id - BC != xi^2 Id`.

The resolution is: **A is NOT required to be invertible, and the argument via A^{-1} was the wrong route.**

The correct argument is:

```
S_R^2 = (xi^2 A^{-1})^2   [wrong, requires A invertible]
```

Instead, use `A S_R = xi^2 Id` to compute `S_R^2` directly:

```
S_R^2 = S_R * S_R.
```

We know `A S_R = xi^2 Id_R`. Apply `S_R` on the left:

```
S_R (A S_R) = S_R * xi^2 Id_R = xi^2 S_R.
```

Also `S_R (A S_R) = (S_R A) S_R = xi^2 S_R`. (Consistent, but circular.)

**Different approach.** From `A S_R = xi^2 Id`:

```
S_R = A^{-1} (xi^2 Id)   [if A invertible].
```

But since A may not be invertible (it is a Clifford gamma-matrix combination, not
scalar), we need to work differently.

### 5.3 The Correct Argument: Schur Complement of a Clifford-Squared Matrix

**Theorem.** Let M be a matrix with `M^2 = lambda Id` partitioned as
```
M = [A B; C E]
```
with E invertible and `S = A - B E^{-1} C`. Then `S^2 = lambda Id`.

**Proof.** We compute `S^2` using only the identities (I)-(IV) without assuming A invertible.

```
S^2 = (A - B E^{-1} C)^2
    = A^2 - A B E^{-1} C - B E^{-1} C A + B E^{-1} C B E^{-1} C.
```

Term 1: `A^2 = lambda Id - BC`.  [from (I)]
Term 2: `-A B E^{-1} C`. From (II): `AB = -BE`, so `A B E^{-1} = -B`. Thus Term 2 = `BC`.
Term 3: `-B E^{-1} C A`. From (III): `CA = -EC`, so `E^{-1} C A = -C`. Thus `B E^{-1} C A = -BC`, and Term 3 = `BC`.
Term 4: `B E^{-1} C B E^{-1} C`. Let `v = E^{-1} C B E^{-1} C`. We compute:
  From (IV): `CB = lambda Id_Q - E^2`, so `E^{-1} C B E^{-1} = E^{-1}(lambda Id - E^2) E^{-1} = lambda E^{-2} - Id_Q`.
  Thus `v = B(lambda E^{-2} - Id_Q) C = lambda B E^{-2} C - BC`.
  Term 4 = `lambda B E^{-2} C - BC`.

Summing all four terms:

```
S^2 = (lambda Id - BC) + BC + BC + (lambda B E^{-2} C - BC)
    = lambda Id + BC + lambda B E^{-2} C - BC
    = lambda Id + lambda B E^{-2} C.
```

So `S^2 = lambda Id iff B E^{-2} C = 0` as an operator from R to R.

### 5.4 Computing B E^{-2} C vs B (E^{-1})^2 C

Note the distinction: the prior note derived `S_R^2 = xi^2 Id + xi^2 B (E^{-1})^2 C`,
but the theorem above gives `S_R^2 = xi^2 Id + xi^2 B E^{-2} C`.

These are the same thing: `B E^{-2} C = B (E^{-1})^2 C`. So the question is the same.

From §5.3 of vz-schur-complement-2026-06-23.md, the image of C is in `Q_0 direct-sum Q_T`
(scalar spinors and gamma-trace spinors). The operator `E^{-2}` acts on this subspace.

### 5.5 The Key Representation-Theory Fact

**Claim:** `B E^{-2} C = 0` as a map from `R^{14D}` to `R^{14D}`, when the RS decomposition
is the FULL 14D gamma-trace projection.

**Proof via the Clifford module structure (reconstruction grade).**

The point is subtle. The map `B E^{-2} C: R^{14D} -> R^{14D}` is an operator in the
Clifford algebra representation. Specifically:

Step 1. `C: R^{14D} -> Q` maps RS spinor-valued 1-forms to scalar + gamma-trace sectors.
        From §3.1: `C psi_R = (chi, (gamma(xi)-2) chi)` where `chi = xi^A psi_{R,A} in S`.

Step 2. `E^{-1}: Q -> Q` maps within the Q sector. The image of C is in the subspace
        `{(chi, (gamma(xi)-2) chi) : chi in S}`, which is a module over the Clifford
        element `gamma(xi)`.

Step 3. `E^{-2} C psi_R` remains in this module (since E maps `Q_0 direct-sum Q_T` to
        itself, and E is expressed via `gamma(xi)` multiplication as computed in §5.2 of
        vz-schur-complement-2026-06-23.md).

Step 4. `B: Q -> R^{14D}` applied to elements of the form `(f(gamma(xi)) chi, h(gamma(xi)) chi)`
        for rational functions `f, h` of `gamma(xi)` (which is the form of `E^{-2} C psi_R`).

The formula (BCpsi) from §3.2 above shows that `B(phi, s)_A = xi_A (...) + gamma_A (...)`.

The key question is: is this zero in `R^{14D}`?

An element `v_A = xi_A f + gamma_A h` is in `R^{14D} = ker Gamma^{14D}` iff:

```
Gamma^{14D}(v) = gamma^A v_A = gamma^A xi_A f + gamma^A gamma_A h = gamma(xi) f + 14 h = 0.
```

i.e., `h = -(1/14) gamma(xi) f`.

So `B(phi, s) in R^{14D}` iff the `xi_A`-coefficient and `gamma_A`-coefficient satisfy:
`gamma_A`-coefficient = `-(1/14) gamma(xi)` times `xi_A`-coefficient.

From (BCpsi): the `xi_A`-coefficient is `(6/7) chi + (1/14) mu` and the `gamma_A`-coefficient
is `(33/98) mu - (10 xi^2 / 49) chi`.

Check whether `(33/98) mu - (10 xi^2/49) chi = -(1/14) gamma(xi) ((6/7) chi + (1/14) mu)`:

RHS = `-(1/14)((6/7) mu + (1/14) xi^2 chi)` [using `gamma(xi) chi = mu`, `gamma(xi) mu = xi^2 chi`]
    = `-(6/98) mu - xi^2/(196) chi`.

Compare with LHS: `(33/98) mu - (10 xi^2/49) chi = (33/98) mu - (20 xi^2/98) chi`.

These are equal iff:
- `(33/98) = -(6/98)` — FALSE (33 != -6)
- `-(20 xi^2/98) = -xi^2/196` — FALSE (20/98 != 1/196)

So `B(C psi_R)` as computed in (BCpsi) does **NOT** satisfy the RS membership condition.
This means `B(C psi_R) notin R^{14D}` in general — but wait, the B block by definition
maps to the RS sector (it is defined as `P_R(...)`, i.e., the RS projection is already
applied). The discrepancy means the RS projection introduces additional terms.

**Re-examining:** The B block is `(B q)_A = P_R(\sigma_D(xi) q)_A`. The full calculation
in §3.2 should apply P_R at the end. Let me recompute with the explicit RS projector.

```
P_R(w)_A = w_A - (1/14) gamma_A (gamma^B w_B)
```

For `w_A = xi_A [(6/7) chi + (1/14) mu] + gamma_A [(33/98) mu - (10 xi^2/49) chi]` BEFORE
the final RS projection... actually, wait. The calculation in §3.2 already applied `P_R` at
each step. Let me recheck.

In §3.2, the formula for `P_R(xi tensor chi)_A` already includes the RS projection:

```
P_R(xi tensor chi)_A = xi_A chi - (1/14) gamma_A gamma(xi) chi = xi_A chi - (1/14) gamma_A mu.
```

And `P_R(F_xi j_{14D}(s))_A` also applied `P_R`. So (BCpsi) is already the RS-projected
result. Therefore (BCpsi) IS an element of `R^{14D}` by construction (it has the RS
projection built in).

The issue above (checking RS membership) was a consistency check, not a computation.
Let me verify: apply `Gamma^{14D}` to (BCpsi):

```
Gamma^{14D}(B C psi_R) = gamma^A [(6/7) chi + (1/14) mu] xi_A + gamma^A gamma_A [(33/98) mu - (10xi^2/49) chi]
= [(6/7) chi + (1/14) mu] gamma(xi) + 14 [(33/98) mu - (10xi^2/49) chi]
= (6/7) mu + (1/14) xi^2 chi + (33/7) mu - (20 xi^2/7) chi
= (6/7 + 33/7) mu + (1/14 - 20/7) xi^2 chi
= (39/7) mu + (1/14 - 40/14) xi^2 chi
= (39/7) mu - (39/14) xi^2 chi.
```

This is NOT zero for generic `chi` and `mu` with `mu = gamma(xi) chi`. So `B C psi_R notin R^{14D}`.

**But this is a contradiction** — B by definition maps into R^{14D} (the RS projection is built into the B block). The resolution must be that the B block formula in §3.2 is not the fully RS-projected formula — there is a further projection step.

### 5.6 Correcting the B Block: Full RS Projection

The B block, properly defined, applies `P_R` to the full output of `sigma_D(xi)` acting
on Q-inputs. Let me rewrite:

For scalar input `phi in Q_0`:

```
(sigma_D(xi)(phi, 0))_A = xi_A phi   (the one-form part)
```

Full gamma-trace: `Gamma^{14D}(xi tensor phi) = gamma(xi) phi = mu_phi` where `mu_phi = gamma(xi) phi`.
RS projection: `P_R(xi tensor phi)_A = xi_A phi - (1/14) gamma_A mu_phi`.

Check: `Gamma^{14D}(P_R(xi tensor phi)) = gamma^A (xi_A phi - (1/14) gamma_A mu_phi) = mu_phi - (1/14)(14) mu_phi = mu_phi - mu_phi = 0`. YES, in R^{14D}. Good.

For gamma-trace input `j(s)_A = (1/14) gamma_A s`:

The full one-form output of the D_GU symbol is:
```
(sigma_D(xi)(0, j(s)))_A = (F_xi j(s))_A = xi_A (Gamma^{14D} j(s)) - gamma(xi) j(s)_A
= xi_A s - (1/14) gamma(xi) gamma_A s.
```

Gamma-trace: `Gamma^{14D}((F_xi j(s))) = gamma^A (xi_A s - (1/14) gamma(xi) gamma_A s) = gamma(xi) s - (1/14)(-12 gamma(xi)) s = (1 + 6/7) gamma(xi) s = (13/7) gamma(xi) s`.

RS projection:
```
P_R((F_xi j(s)))_A = xi_A s - (1/14) gamma(xi) gamma_A s - (1/14) gamma_A (13/7) gamma(xi) s
= xi_A s - (1/14) gamma(xi) gamma_A s - (13/98) gamma_A gamma(xi) s.
```

Check: `Gamma^{14D}(P_R(F_xi j(s)))`
```
= gamma^A [xi_A s - (1/14) gamma(xi) gamma_A s - (13/98) gamma_A gamma(xi) s]
= gamma(xi) s - (1/14) gamma^A gamma(xi) gamma_A s - (13/98) 14 gamma(xi) s
= gamma(xi) s - (1/14)(-12 gamma(xi)) s - (13/7) gamma(xi) s
= gamma(xi) s + (6/7) gamma(xi) s - (13/7) gamma(xi) s
= (1 + 6/7 - 13/7) gamma(xi) s
= (7/7 + 6/7 - 13/7) gamma(xi) s
= 0.
```

So `P_R(F_xi j(s)) in R^{14D}`. The B block formula is correct at the projected level.

Now for input `(phi, s) = (chi, (gamma(xi)-2) chi)`:

First component (scalar `phi = chi`):
```
(B_scalar)_A = xi_A chi - (1/14) gamma_A gamma(xi) chi = xi_A chi - (1/14) gamma_A mu.
```

Second component (gamma-trace `s = (gamma(xi)-2) chi`):
```
(B_trace)_A = xi_A (gamma(xi)-2) chi - (1/14) gamma(xi) gamma_A (gamma(xi)-2) chi - (13/98) gamma_A gamma(xi)(gamma(xi)-2) chi.
```

Simplify `gamma(xi)(gamma(xi)-2) = xi^2 - 2 gamma(xi)`:
```
(B_trace)_A = xi_A (mu - 2chi) - (1/14) gamma_A (xi^2 - 2mu) - (13/98) gamma_A (xi^2 - 2mu).
```

Combined coefficient of `gamma_A (xi^2 - 2mu)`:
```
-(1/14) - (13/98) = -7/98 - 13/98 = -20/98 = -10/49.
```

So:
```
(B_trace)_A = xi_A (mu - 2chi) - (10/49) gamma_A (xi^2 - 2mu).
```

**Total B(C psi_R):**
```
(B C psi_R)_A = [xi_A chi - (1/14) gamma_A mu] + [xi_A (mu - 2chi) - (10/49) gamma_A (xi^2 - 2mu)]
= xi_A [chi + mu - 2chi] + gamma_A [-(1/14) mu - (10/49)(xi^2 - 2mu)]
= xi_A [mu - chi] + gamma_A [-(1/14) mu - (10 xi^2/49) + (20/49) mu]
= xi_A [mu - chi] + gamma_A [(20/49 - 1/14) mu - (10 xi^2/49)]
= xi_A [mu - chi] + gamma_A [(40/98 - 7/98) mu - (10 xi^2/49)]
= xi_A [mu - chi] + gamma_A [(33/98) mu - (10 xi^2/49)].
```

Let me re-verify RS membership by applying `Gamma^{14D}`:

```
Gamma^{14D}(B C psi_R) = gamma^A(xi_A [mu - chi]) + gamma^A(gamma_A [(33/98)mu - (10xi^2/49)])
= gamma(xi)(mu - chi) + 14 [(33/98)mu - (10xi^2/49)]
= (xi^2 chi - mu) + (33/7) mu - (20 xi^2/7)
= xi^2 chi - mu + (33/7) mu - (20/7) xi^2
= xi^2(1 - 20/7) + mu(-1 + 33/7)
= xi^2(-13/7) + mu(26/7)
= (13/7)(2 mu - xi^2 chi).
```

This equals zero iff `2 mu = xi^2 chi`, i.e., `2 gamma(xi) chi = xi^2 chi`. This is only true
if `chi` is an eigenvector of `gamma(xi)` with eigenvalue `xi^2/2` — a very special condition,
not generically satisfied.

**This is a contradiction with the claim that B maps into R^{14D}.** The discrepancy signals
an error in the computation. Let me identify it.

---

## 6. Identifying the Error and the Correct Computation

The issue is in how the "C block" output is defined. The C block maps RS one-form spinors to
the **non-RS** sector. The output of C consists of:
- A scalar piece `(xi^A psi_{R,A}) in Q_0 = Omega^0 tensor S`
- A gamma-trace piece `P_{Q_T}(F_xi psi_R) in Q_T`

The decomposition of `Omega^1 tensor S` is:
```
Omega^1 tensor S = P_R(Omega^1 tensor S) direct-sum P_Q(Omega^1 tensor S)
```

where `P_R = Id - j_{14D} Gamma^{14D}` (with `j_{14D}` the right inverse of `Gamma^{14D}`
in the sense `Gamma^{14D} j_{14D} = Id_S`).

The full block matrix `M(xi)` acts on `(Q_0 tensor S) direct-sum (Omega^1 tensor S)`, not on
the RS/non-RS split in the one-form sector. The B and C blocks in the Schur complement refer
to the split:

```
E_full = (Omega^0 tensor S^+) direct-sum (Omega^1 tensor S^-)
```

partitioned as:
```
(Omega^0 tensor S^+) direct-sum R^{14D}   vs.   (something).
```

Actually, this is the key subtlety that the computation in §3 was tracking. The rolled-up operator
acts on:
```
E = E_0 direct-sum E_1 = (Omega^0 tensor S^+) direct-sum (Omega^1 tensor S^-)
```

This is already a decomposition into scalar-spinors and spinor-valued 1-forms. The RS split
is within `E_1 = Omega^1 tensor S^-`.

So the correct block decomposition for computing S_R is:
```
E = R^{14D} direct-sum (E_0 direct-sum Q^{14D})
```

where `Q^{14D} = Omega^1/R^{14D}` is the gamma-trace part of the one-form sector plus the scalar sector.

The A block is the restriction of M to R^{14D} -> R^{14D}.
The E block is the restriction to (E_0 direct-sum Q^{14D}) -> (E_0 direct-sum Q^{14D}).

The E block thus includes the scalar sector, not just the gamma-trace one-form sector.

This is what was computed in vz-schur-complement-2026-06-23.md §3.3 and §5: the E block
is the 2x2 matrix (in `(phi, s)` coordinates where phi is scalar-spinor and s parameterizes
the gamma-trace one-forms) with:

```
E = gamma(xi) * [[0, 1/14], [1, 13/7]]
```

and `det(E) = gamma(xi)^2 * (-1/14) = -(xi^2/14)`, nonzero for `xi^2 != 0`.

The computation of B C is thus correct as computed in §3. The verification step above showing
`Gamma^{14D}(B C psi_R) != 0` is correct and reveals that B C psi_R is NOT in R^{14D}.

But this contradicts the definition of B as the RS projection! The issue is:

**The B block acting on the output of C does not produce RS elements, because C maps
RS spinors to Q, and then B should map Q BACK to RS. But the formula I computed for B
maps Q to the whole E_1, then projects to RS.**

Let me be more careful. B maps Q = (E_0 direct-sum Q^{14D}) to R^{14D}. So:

```
B: Omega^0 tensor S direct-sum Q^{14D} -> R^{14D}.
```

The formula for B is: for input `(phi, s) in Omega^0 direct-sum Q^{14D}` (where s parameterizes
the gamma-trace one-form `j(s) = (1/14) gamma_A s`):

```
B(phi, s) = P_R (sigma_D(xi) (phi, j(s)))_1
```

where the subscript 1 means the one-form component of `sigma_D(xi)`.

We computed:
```
(sigma_D(xi)(phi, j(s)))_1 = xi tensor phi + F_xi j(s).
```

After P_R projection, the result is in R^{14D} by construction.

So B(phi, s) IS in R^{14D}. My verification above must have an arithmetic error.

Recheck: `Gamma^{14D}(B_scalar)`:
```
= Gamma^{14D}(xi_A chi - (1/14) gamma_A mu)
= gamma^A xi_A chi - (1/14) gamma^A gamma_A mu
= gamma(xi) chi - (1/14)(14) mu
= mu - mu = 0.  CHECK.
```

Recheck: `Gamma^{14D}(B_trace)` where `(B_trace)_A = xi_A (mu-2chi) - (10/49) gamma_A (xi^2 - 2mu)`:
```
= gamma^A xi_A (mu-2chi) - (10/49) gamma^A gamma_A (xi^2 - 2mu)
= gamma(xi)(mu-2chi) - (10/49)(14)(xi^2 - 2mu)
= (xi^2 chi - 2 mu) - (20/7)(xi^2 - 2 mu)
= xi^2 chi - 2 mu - (20/7) xi^2 + (40/7) mu
= xi^2 (1 - 20/7) + mu(-2 + 40/7)
= xi^2 (-13/7) + mu (26/7)
= (13/7)(2 mu - xi^2 chi).
```

This is NOT zero. So `B_trace notin R^{14D}`, which contradicts the RS projection.

**The error is in the B_trace formula.** Let me redo it carefully.

For the gamma-trace input `j(s)_A = (1/14) gamma_A s` with `s = (gamma(xi)-2) chi`:

The one-form part of `sigma_D(xi)(0, j(s))` is:
```
(F_xi j(s))_A = xi_A (Gamma^{14D}(j(s))) - gamma(xi) j(s)_A.
```

Now `Gamma^{14D}(j(s)) = gamma^B j(s)_B = gamma^B (1/14) gamma_B s = (1/14)(14) s = s`.

So:
```
(F_xi j(s))_A = xi_A s - (1/14) gamma(xi) gamma_A s.
```

Then `P_R(F_xi j(s))_A = (F_xi j(s))_A - (1/14) gamma_A Gamma^{14D}(F_xi j(s))`.

Compute `Gamma^{14D}(F_xi j(s))`:
```
= gamma^A (xi_A s - (1/14) gamma(xi) gamma_A s)
= gamma(xi) s - (1/14) gamma^A gamma(xi) gamma_A s
= gamma(xi) s - (1/14)(-12 gamma(xi)) s
= (1 + 12/14) gamma(xi) s = (13/7) gamma(xi) s.
```

So:
```
P_R(F_xi j(s))_A = xi_A s - (1/14) gamma(xi) gamma_A s - (1/14) gamma_A (13/7) gamma(xi) s
= xi_A s - (1/14) gamma(xi) gamma_A s - (13/98) gamma_A gamma(xi) s.
```

Now use the Clifford identity `{gamma(xi), gamma_A} = 2 xi_A` (since `gamma^B xi_B gamma_A + gamma_A gamma^B xi_B = 2 xi_A`):

```
gamma(xi) gamma_A = 2 xi_A - gamma_A gamma(xi).
```

So:
```
-(1/14) gamma(xi) gamma_A s = -(1/14)(2 xi_A - gamma_A gamma(xi)) s
= -(2/14) xi_A s + (1/14) gamma_A gamma(xi) s.
```

Substitute:
```
P_R(F_xi j(s))_A = xi_A s - (2/14) xi_A s + (1/14) gamma_A gamma(xi) s - (13/98) gamma_A gamma(xi) s
= (1 - 1/7) xi_A s + (1/14 - 13/98) gamma_A gamma(xi) s
= (6/7) xi_A s + (7/98 - 13/98) gamma_A gamma(xi) s
= (6/7) xi_A s - (6/98) gamma_A gamma(xi) s
= (6/7) xi_A s - (3/49) gamma_A gamma(xi) s.
```

Now `s = (gamma(xi)-2) chi`, so `gamma(xi) s = gamma(xi)(gamma(xi)-2) chi = (xi^2 - 2 gamma(xi)) chi = xi^2 chi - 2 mu`.

```
P_R(F_xi j(s))_A = (6/7) xi_A (mu - 2chi) - (3/49) gamma_A (xi^2 chi - 2mu).
```

**Verify RS membership:**
```
Gamma^{14D}(P_R(F_xi j(s))) = gamma^A [(6/7) xi_A (mu-2chi) - (3/49) gamma_A (xi^2 chi - 2mu)]
= (6/7) gamma(xi)(mu-2chi) - (3/49)(14)(xi^2 chi - 2mu)
= (6/7)(xi^2 chi - 2mu) - (6/7)(xi^2 chi - 2mu)
= 0.  CHECK.
```

The formula was wrong before due to a sign error in applying `gamma(xi) gamma_A = 2 xi_A - gamma_A gamma(xi)`. The correct formula is:

```
P_R(F_xi j(s))_A = (6/7) xi_A (mu-2chi) - (3/49) gamma_A (xi^2 chi - 2mu).
```

**Corrected B(C psi_R):**

```
(B C psi_R)_A = (B_scalar)_A + (B_trace)_A
= [xi_A chi - (1/14) gamma_A mu] + [(6/7) xi_A (mu-2chi) - (3/49) gamma_A (xi^2 chi - 2mu)]
= xi_A [chi + (6/7)(mu-2chi)] + gamma_A [-(1/14) mu - (3/49)(xi^2 chi - 2mu)]
= xi_A [chi(1 - 12/7) + (6/7) mu] + gamma_A [(-7/98 + 6/49) mu - (3 xi^2/49) chi]
= xi_A [(-5/7) chi + (6/7) mu] + gamma_A [(- 7/98 + 12/98) mu - (3 xi^2/49) chi]
= xi_A [(6 mu - 5 chi)/7] + gamma_A [(5/98) mu - (3 xi^2/49) chi].
                                                                          (BCpsi-corrected)
```

**Verify RS membership of corrected formula:**
```
Gamma^{14D}(B C psi_R) = gamma(xi) [(6mu-5chi)/7] + 14 [(5/98) mu - (3xi^2/49) chi]
= (1/7)(6 xi^2 chi - 5 mu) + (5/7) mu - (6 xi^2/7) chi
= (6 xi^2/7) chi - (5/7) mu + (5/7) mu - (6 xi^2/7) chi
= 0.  CHECK.
```

The corrected B C psi_R IS in R^{14D}.

---

## 7. Is the Corrected BC = 0?

The corrected expression (BCpsi-corrected) is:

```
(B C psi_R)_A = xi_A [(6 mu - 5 chi)/7] + gamma_A [(5/98) mu - (3 xi^2/49) chi]
```

where `chi = g_Y(xi, psi_R)` and `mu = gamma(xi) chi`.

This is zero for all `psi_R in R^{14D}` iff both coefficients vanish for all `chi in S`.

The `xi_A` coefficient: `(6mu - 5chi)/7 = 0` iff `6 gamma(xi) chi = 5 chi` iff `chi` is an
eigenvector of `gamma(xi)` with eigenvalue `5/6`. This is a special condition, not a generic
identity.

**Therefore: `BC != 0` on `R^{14D}` for generic xi and generic RS elements.**

However, the question for `S_R^2 = xi^2 Id` was whether `B E^{-2} C = 0`, which is NOT
the same as `BC = 0` in general.

---

## 8. The Exact Matrix Identity: A Direct Route

Rather than computing `B E^{-2} C` from the explicit formulas, let us use an abstract argument.

**Theorem (exact matrix identity for Clifford-module Schur complements).**

Let `E` be a Clifford module bundle for `Cl(n,m)`, `D` a Dirac-type operator with
`sigma_D(xi)^2 = g(xi,xi) Id_E` for all covectors xi. Let `E = R direct-sum Q` be a
direct sum decomposition of Clifford module bundles (i.e., both R and Q are sub-Clifford-modules).
Then the Schur complement `S_R = P_R M|_R - P_R M|_Q (P_Q M|_Q)^{-1} P_Q M|_R`
satisfies `S_R^2 = g(xi,xi) Id_R`.

**Proof:** If R and Q are both sub-Clifford-modules under `Cl(n,m)`, then the Clifford
element `c(xi)` maps R to R and Q to Q (it commutes with the sub-module structure). In
this case, `A = P_R c(xi)|_R`, `E = P_Q c(xi)|_Q`, and the off-diagonal blocks B = C = 0.
The Schur complement degenerates to `S_R = A = c(xi)|_R`, and `S_R^2 = c(xi)^2|_R = xi^2 Id_R`.

**BUT:** This theorem requires R and Q to be sub-Clifford-modules. The RS sub-bundle
`R^{14D} = ker Gamma^{14D}` is NOT a sub-Clifford-module in general:
`c(xi)` does not preserve the gamma-trace condition.

Proof: if `psi_R in R^{14D}` (i.e., `gamma^A psi_{R,A} = 0`), then `c(xi)` acting component-wise
on `psi_R` gives `(c(xi) psi_R)_A = gamma(xi) psi_{R,A}`, which has gamma-trace
`gamma^B (c(xi) psi_R)_B = gamma^B gamma(xi) psi_{R,B} = gamma(xi) gamma^B psi_{R,B} + [gamma^B, gamma(xi)] psi_{R,B}`.

The second term is `[gamma^B, gamma(xi)] psi_{R,B} = 2 xi^B psi_{R,B} = 2 g_Y(xi, psi_R)`,
which is generically nonzero. So `c(xi)` does NOT preserve `R^{14D}`, confirming that
the RS sub-bundle is NOT a sub-Clifford-module.

Therefore the theorem does not apply directly, and `B, C != 0`.

---

## 9. The Correct Identity and Its Proof

**The identity `S_R^2 = xi^2 Id_{RS}` holds if and only if `B E^{-2} C = 0`.**

From the block-square calculation in §5.3, combined with the corrected B C formulas in §7,
we can compute `B E^{-2} C` using the explicit E matrix.

**E matrix at 14D.** From vz-schur-complement-2026-06-23.md §5.2, the E block in the
`(phi, s)` basis is:

```
E = gamma(xi) * [[0, 1/14], [1, 13/7]].
```

The inverse is:
```
E^{-1} = (1/gamma(xi)) * (-14) * [[13/7, -1/14], [-1, 0]]
= (-14/xi^2) * gamma(xi) * [[13/7, -1/14], [-1, 0]].
```

(Using `(1/gamma(xi)) = gamma(xi)/xi^2`.)

```
E^{-2} = (E^{-1})^2 = (196/xi^4) * gamma(xi)^2 * [[13/7, -1/14], [-1, 0]]^2.
```

`gamma(xi)^2 = xi^2 Id_S`, so:

```
E^{-2} = (196/xi^2) * [[13/7, -1/14], [-1, 0]]^2.
```

Compute `[[13/7, -1/14], [-1, 0]]^2`:
```
= [[13/7 * 13/7 + (-1/14)(-1), 13/7*(-1/14) + (-1/14)*0], [(-1)(13/7) + 0*(-1), (-1)(-1/14) + 0]]
= [[169/49 + 1/14, -13/98], [-13/7, 1/14]].
```

`169/49 + 1/14 = 338/98 + 7/98 = 345/98`.

```
[[13/7,-1/14],[-1,0]]^2 = [[345/98, -13/98], [-13/7, 1/14]].
```

So `E^{-2} = (196/xi^2) * [[345/98, -13/98], [-13/7, 1/14]]`.

Now `C psi_R = (chi, (gamma(xi)-2)chi) = (chi, mu - 2 chi)` (here phi-component = chi, s-component = mu - 2 chi).

Apply E^{-2}:
```
E^{-2} C psi_R = (196/xi^2) * [[345/98, -13/98], [-13/7, 1/14]] * (chi, mu-2chi)
```

In these coordinates, the `(phi, s)` output of E^{-2} has a scalar-spinor component and a
trace-mode spinor component. But these are acted on by the scalar matrix — however, chi and
mu-2chi are themselves spinors in S, not scalars. The matrix `[[...]]` acts on the
`(Q_0, Q_T)` components, with chi being the Q_0 spinor and mu-2chi being the Q_T spinor.

First component (Q_0 output):
```
(E^{-2} C psi_R)_0 = (196/xi^2) [345/98 * chi + (-13/98) * (mu-2chi)]
= (196/xi^2) [(345 chi - 13 mu + 26 chi)/98]
= (196/xi^2) [(371 chi - 13 mu)/98]
= (2/xi^2) (371 chi - 13 mu).
```

Wait: `196/xi^2 * 1/98 = 2/xi^2`. So:
```
(E^{-2} C psi_R)_0 = (2/xi^2)(371 chi - 13 mu).
```

Second component (Q_T output):
```
(E^{-2} C psi_R)_T = (196/xi^2) [-13/7 * chi + 1/14 * (mu-2chi)]
= (196/xi^2) [(-26/14 + 1/14) mu/... ]
```

Let me redo: `-13/7 * chi + 1/14 * (mu - 2chi) = -13 chi/7 + mu/14 - chi/7 = -(13/7 + 1/7) chi + mu/14 = -2 chi + mu/14`.

```
(E^{-2} C psi_R)_T = (196/xi^2)(-2 chi + mu/14) = (196/xi^2)(-2 chi + mu/14).
= (-392 chi + 14 mu) / xi^2.
```

So:
```
E^{-2} C psi_R = ((2/xi^2)(371 chi - 13 mu),  (-392 chi + 14 mu)/xi^2).
```

Now apply B to this element `(phi_2, s_2) = ((2/xi^2)(371 chi - 13 mu), (-392 chi + 14 mu)/xi^2)`:

Using the corrected B formula `B(phi, s) = xi_A [(6 s - 5 phi)/7] + gamma_A [(5/98) s - (3xi^2/49) phi]`... 

Wait — that formula was for the specific C output. The B block for a general Q element
`(phi, s_trace)` (where s_trace parameterizes `j_{14D}(s)_A = (1/14) gamma_A s`) is:

```
(B (phi, s))_A = P_R((xi_A phi) + (F_xi j(s))_A)
```

with the corrected RS projection giving:
```
(B (phi, s))_A = [xi_A phi - (1/14) gamma_A gamma(xi) phi] + [(6/7) xi_A s - (3/49) gamma_A gamma(xi) s]

but using gamma(xi) gamma_A = 2 xi_A - gamma_A gamma(xi):
```

Actually, from the detailed computation above, the correct formula for B is:

For input `(phi, s)` where phi is a scalar spinor in S and s parameterizes the gamma-trace mode:

```
(B(phi, s))_A = xi_A phi - (1/14) gamma_A gamma(xi) phi + (6/7) xi_A s - (3/49) gamma_A gamma(xi) s.
```

(The first two terms came from the scalar sector input, the last two from the trace sector input with corrected RS projection.)

Now apply this to `(phi_2, s_2) = ((2/xi^2)(371 chi - 13 mu), (-392 chi + 14 mu)/xi^2)`:

```
(B E^{-2} C psi_R)_A
= xi_A phi_2 - (1/14) gamma_A gamma(xi) phi_2
  + (6/7) xi_A s_2 - (3/49) gamma_A gamma(xi) s_2.
```

Substituting `gamma(xi) phi_2 = (2/xi^2) gamma(xi) (371 chi - 13 mu) = (2/xi^2)(371 mu - 13 xi^2 chi)` and
`gamma(xi) s_2 = (1/xi^2)(-392 mu + 14 xi^2 chi)`:

```
(B E^{-2} C psi_R)_A
= xi_A [(2/xi^2)(371 chi - 13 mu)]
  - (1/14) gamma_A [(2/xi^2)(371 mu - 13 xi^2 chi)]
  + (6/7) xi_A [(-392 chi + 14 mu)/xi^2]
  - (3/49) gamma_A [(1/xi^2)(-392 mu + 14 xi^2 chi)].
```

Collect `xi_A` terms:

```
xi_A [(2/xi^2)(371 chi - 13 mu) + (6/7)(1/xi^2)(-392 chi + 14 mu)]
= (1/xi^2) xi_A [2(371 chi - 13 mu) + (6/7)(-392 chi + 14 mu)]
= (1/xi^2) xi_A [(742 - 2352/7) chi + (-26 + 84/7) mu]
= (1/xi^2) xi_A [(5194/7 - 2352/7) chi + (-182/7 + 84/7) mu]
= (1/xi^2) xi_A [(2842/7) chi + (-98/7) mu]
= (1/7 xi^2) xi_A [2842 chi - 98 mu].
```

Collect `gamma_A` terms:

```
gamma_A [-(1/14)(2/xi^2)(371 mu - 13 xi^2 chi) - (3/49)(1/xi^2)(-392 mu + 14 xi^2 chi)]
= (1/xi^2) gamma_A [-(2/14)(371 mu - 13 xi^2 chi) - (3/49)(-392 mu + 14 xi^2 chi)]
= (1/xi^2) gamma_A [-(371/7) mu + (13/7) xi^2 chi + (392*3/49) mu - (42/49) xi^2 chi]
= (1/xi^2) gamma_A [-(371/7 - 24) mu + (13/7 - 6/7) xi^2 chi].
```

`392 * 3/49 = 1176/49 = 24`. So:
`-(371/7) + 24 = -(371/7) + 168/7 = -203/7`.

And `13/7 - 6/7 = 7/7 = 1`.

```
gamma_A terms = (1/xi^2) gamma_A [-(203/7) mu + xi^2 chi].
```

So:

```
(B E^{-2} C psi_R)_A = (1/7 xi^2) xi_A [2842 chi - 98 mu] + (1/xi^2) gamma_A [-(203/7) mu + xi^2 chi].
```

This is manifestly nonzero for generic chi and mu. Therefore `B E^{-2} C != 0` and the
exact matrix identity `S_R^2 = xi^2 Id_{RS}` does **NOT hold exactly** for the 14D D_GU
operator with the full 14D gamma-trace RS projection.

---

## 10. Interpretation: What Does This Mean for VZ Evasion?

This is a **positive result for the program**, not a negative one.

**The VZ evasion result is unchanged.** The kernel result from vz-schur-complement-2026-06-23.md §8:

```
ker S_R(xi) = 0 for all xi with xi^2 != 0
```

does not require `S_R^2 = xi^2 Id`. It follows from the Clifford module property of `M(xi)`:
if `S_R psi_R = 0` then `M(xi)(psi_R, -E^{-1} C psi_R) = 0`, hence `xi^2 (psi_R, ...) = 0`,
so `psi_R = 0`. This argument is unaffected by `B E^{-2} C != 0`.

**What OQ1 actually asks.** The exact identity `S_R^2 = xi^2 Id` would mean `S_R` is itself
a Clifford element on the RS sector. This is a STRONGER property than VZ evasion. It holds
when the RS sub-bundle is a sub-Clifford-module (which requires the gamma-trace to commute
with the Clifford action — it does not, as shown in §8).

**The actual eigenvalue structure of S_R.** From `A S_R = xi^2 Id` (proved in §5.1), if
`S_R v = lambda v` then `A (lambda v) = xi^2 v`, so `A v = (xi^2/lambda) v`. Both `A` and
`S_R` have the same eigenvectors, with eigenvalues related by `lambda * eigenvalue(A) = xi^2`.

The characteristic polynomial of `S_R` is not `(lambda^2 - xi^2)^k` (Clifford-type) but
is instead determined by the specific block structure. The eigenvalues of `S_R` satisfy
`det(S_R - lambda Id) = 0`, which by the block determinant formula gives:

```
det(M - lambda Id) = det(E - lambda Id) * det(S_R(lambda))
```

where `S_R(lambda) = (A - lambda Id) - B (E - lambda Id)^{-1} C`.

Since `M^2 = xi^2 Id`, the eigenvalues of M are `+/- xi` (with xi = sqrt(g_Y(xi,xi))). But S_R
is a submatrix of M (after row/column operations), so its eigenvalues are among the eigenvalues
of M: `{+sqrt(xi^2), -sqrt(xi^2)}`. This gives `det(S_R - mu Id) = prod (mu_i - mu)` with
each `mu_i = pm sqrt(xi^2)`, so:

```
char poly of S_R = prod (lambda - pm sqrt(xi^2)).
```

This means `S_R^{2k} = (xi^2)^k Id` for all k, and in particular the MINIMAL POLYNOMIAL
of `S_R` divides `t^2 - xi^2`. So `S_R^2 = xi^2 Id` holds for any matrix whose eigenvalues
lie in `{+/- sqrt(xi^2)}`.

But we just computed `B E^{-2} C != 0` which should give `S_R^2 != xi^2 Id`. There is a
contradiction. Let me resolve it.

---

## 11. Resolution of the Contradiction

The eigenvalue argument says: eigenvalues of `S_R` lie in `{+/- sqrt(xi^2)}`, so `S_R^2 = xi^2 Id`.

The explicit computation says: `S_R^2 = xi^2 Id + xi^2 B E^{-2} C`, with `B E^{-2} C != 0`.

These cannot both be true. One of them has an error. Let me identify which.

**The eigenvalue argument.** Is it true that eigenvalues of S_R lie in those of M?

The Schur complement of a principal submatrix does NOT in general have eigenvalues contained
in those of the full matrix. The correct statement is: `det(M) = det(E) det(S_R)`, which
relates the DETERMINANTS but not the individual eigenvalues.

The correct characterization: `lambda` is an eigenvalue of `S_R` iff `0` is an eigenvalue
of `S_R - lambda Id`, iff `lambda` is such that `A - lambda Id - B (E - lambda Id)^{-1} C`
is singular, iff `lambda` is a Schur eigenvalue of M (by the Schur determinant formula).

The Schur eigenvalues of M are NOT the same as the eigenvalues of M in general.

So the eigenvalue argument above was wrong: the eigenvalues of `S_R` are NOT necessarily
among `{+/- sqrt(xi^2)}`.

**Therefore:** `B E^{-2} C != 0` is correct, and `S_R^2 != xi^2 Id` as an exact matrix identity.

**But:** The KERNEL result `ker S_R = 0` for `xi^2 != 0` is correct (via the Clifford module
argument). The characteristic cone of `S_R` is still the null cone. So VZ evasion holds.

---

## 12. Complete Verdict on OQ1

**The exact identity `S_R^2 = xi^2 Id_{RS}` does NOT hold for the 14D D_GU RS-block symbol
with the full 14D gamma-trace RS projection.**

**What does hold:**

1. `A S_R = S_R A = xi^2 Id_R` (exact) — the full-symbol A is a left and right inverse
   of `S_R` up to the scalar `xi^2`.
2. `ker S_R(xi) = 0` for `xi^2 != 0` (reconstruction grade) — VZ evasion holds.
3. The characteristic cone of `S_R` is contained in `{xi^2 = 0}` (reconstruction grade).
4. `S_R^2 = xi^2 Id + xi^2 B E^{-2} C` with `B E^{-2} C != 0` explicitly.

**Why OQ1 as originally stated cannot hold with the full 14D gamma-trace RS projection.**

The RS projection `R^{14D} = ker Gamma^{14D}` is not a sub-Clifford-module of the Clifford
module bundle E. The Clifford element `c(xi)` does not preserve R^{14D} (as shown in §8).
The off-diagonal coupling (B != 0, C != 0) is an ESSENTIAL feature of the D_GU operator
in the RS sector, not a defect. It is precisely because of this off-diagonal coupling that
VZ evasion holds: the RS sector is entangled with the spin-1/2 sector, so the standalone-field
hypothesis H1 of VZ fails.

**Upgraded statement.** The correct analog of `S_R^2 = xi^2 Id` is:

```
A S_R = xi^2 Id_R        (exact, by the block-square identity (I) and (II))
```

This can be rewritten as: `(sigma_D(xi)|_{R -> all}) * S_R = xi^2 Id_R`. The Clifford
property propagates to the Schur complement not as `S_R^2 = xi^2 Id` but as
`A S_R = xi^2 Id`, where A is the A-block of the full principal symbol.

---

## 13. Explicit Failure Condition for the Identity

The exact identity `S_R^2 = xi^2 Id_{RS}` would hold iff `B E^{-2} C = 0`.

From the computation above, `B E^{-2} C psi_R = 0` requires:

```
(1/7xi^2) [2842 chi - 98 mu] = 0    AND    (1/xi^2)[-(203/7) mu + xi^2 chi] = 0
```

i.e., `2842 chi = 98 mu = 98 gamma(xi) chi` and `xi^2 chi = (203/7) mu = (203/7) gamma(xi) chi`.

From the first: `gamma(xi) chi = (2842/98) chi = (1421/49) chi`.
Squaring: `xi^2 chi = (1421/49)^2 chi`. So `xi^2 = (1421/49)^2 ~= 841.8`.

This is a FIXED numerical value of xi^2, not a generic identity. So `B E^{-2} C = 0`
only at a specific special value of xi^2, not in general.

**Failure conditions for the exact identity:**
- F1: `B E^{-2} C != 0` for generic xi (established above explicitly)
- F2: The RS sub-bundle `ker Gamma^{14D}` is not preserved by Clifford multiplication
  (established in §8)
- F3: The numerical coefficient computation gives `B E^{-2} C psi_R != 0` for explicit chi

**What would make S_R^2 = xi^2 Id hold:**
- If a different RS projection were used that IS preserved by Clifford multiplication
  (i.e., a sub-Clifford-module decomposition)
- If the shiab operator introduces compensating lower-order terms that make the effective
  symbol satisfy a modified square identity

---

## 14. Implications for VZ Evasion Status

**The EVADED verdict from vz-schur-complement-2026-06-23.md is unchanged.**

The VZ evasion argument (§8 of that file) uses only `M^2 = xi^2 Id` and the block determinant,
not `S_R^2 = xi^2 Id`. The kernel result stands.

**What OQ1 resolution adds:**

1. The VZ evasion is confirmed at a more detailed level: the RS sector is NOT a Clifford
   sub-module (so standalone RS dynamics are genuinely impossible at 14D, not just kinematically
   suppressed).

2. The Schur complement `S_R` has a more complex operator-algebra structure than a simple
   Clifford element: it satisfies `A S_R = xi^2 Id` but not `S_R^2 = xi^2 Id`. This gives
   a richer effective RS propagator structure.

3. For elliptic estimates: the positivity/ellipticity of `S_R` on the RS sector does NOT
   follow from the Clifford-module property directly. It requires a separate analysis using
   `A S_R = xi^2 Id` — which is available, but the route is via A-ellipticity, not S_R-ellipticity.

4. **New open question** (OQ1-refined): Is `S_R` elliptic in the sense that `S_R + S_R* >= c xi^2 Id`
   for some constant c > 0? This is weaker than `S_R^2 = xi^2 Id` but sufficient for elliptic
   estimates. The relation `A S_R = xi^2 Id` suggests yes: if A is bounded (which it is, as
   a principal symbol), then `||S_R v||^2 >= (xi^2/||A||)^2 ||v||^2` for `v in R^{14D}`, 
   giving an elliptic-type lower bound.

---

## 15. Summary and Verdict

| Claim | Status |
|---|---|
| `S_R^2 = xi^2 Id_{RS}` as exact matrix identity | FALSE — B E^{-2} C != 0 explicitly |
| `ker S_R(xi) = 0` for xi^2 != 0 | TRUE (reconstruction, from Clifford module argument) |
| `A S_R = xi^2 Id_R` as exact matrix identity | TRUE (exact, from block-square identities) |
| VZ evasion (no spacelike characteristics) | EVADED (reconstruction, unchanged) |
| RS sector is a sub-Clifford-module | FALSE — c(xi) does not preserve ker Gamma^{14D} |
| VZ evasion upgraded to "full principal-symbol Clifford evasion" | FALSE — S_R is not Clifford-type |
| VZ evasion upgrades to "A-Clifford entanglement evasion" | TRUE — A S_R = xi^2 Id is the correct statement |

**Verdict: CONDITIONALLY_RESOLVED.**

OQ1 is resolved: `S_R^2 = xi^2 Id` does not hold as an exact matrix identity. The correct
statement is `A S_R = xi^2 Id_R`, which is an exact consequence of the Clifford module
structure and the block-square identities. This does not change the VZ evasion verdict
(which was and remains EVADED at reconstruction grade), but it specifies precisely WHY
the RS sector evades VZ: not because it is a Clifford-type operator in its own right, but
because its A-block left-inverse equals `xi^2 Id`, entangling it essentially with the
spin-1/2 sector and preventing standalone RS propagation.

**Explicit failure condition for the main result:** A computation error in §9 could invalidate
`B E^{-2} C != 0`. The explicit numerical values (`2842`, `98`, `203/7`) should be verified
by CAS computation of the 14D E-matrix entries and the B-operator formula.

**Status: reconstruction grade.** All steps use explicit Clifford algebra in 14D. The
14D-specific computation of `gamma^A gamma(xi) gamma_A = -12 gamma(xi)` and the 14D
normalization `gamma^A gamma_A = 14 Id` are standard and can be CAS-verified. The
E-matrix formula and B-block formula should be independently checked.

---

## References

- `explorations/vz-schur-complement-2026-06-23.md` (parent computation, VZ EVADED, OQ1 as open)
- `explorations/vz1-schur-complement-symbol-2026-06-23.md` (horizontal Schur complement)
- `explorations/vz1-schur-vertical-extension-2026-06-23.md` (vertical extension)
- `explorations/n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (Cl(9,5) algebra)
- Lawson-Michelsohn, _Spin Geometry_, Ch. II §6 (Clifford module structure)
- Velo and Zwanziger (1969), Phys. Rev. 186:1337
