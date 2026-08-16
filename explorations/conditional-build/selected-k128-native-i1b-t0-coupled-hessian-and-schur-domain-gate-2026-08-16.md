---
title: "Selected-K128 native I1B T=0 coupled Hessian and Schur/domain gate"
status: active_research
doc_type: exact_action_degree_coupled_hessian_derivative_order_and_conditional_reduction_gate
created: "2026-08-16"
registry: lab/process/selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate.json
probe: tests/channel-swings/selected_k128_native_i1b_t0_coupled_hessian_and_schur_domain_gate_probe.py
grade: "K128 PROVES THAT THE SOURCE-NATIVE FIRST ACTION VANISHES IDENTICALLY ON THE ENTIRE LEVI-CIVITA T=0 METRIC GRAPH. AT EVERY K127 RICCI-FLAT STATIONARY GERM THE PURE METRIC HESSIAN BLOCK IS THEREFORE EXACTLY ZERO. THE ACTUAL QUADRATIC OPERATOR ON NATIVE (h,t) FLUCTUATIONS HAS COUPLED FORM [[0,A*,A],[A,C]] IN BLOCK NOTATION: A IS THE METRIC DERIVATIVE OF THE SHIAB-CURVATURE TRANSLATION ROW AND C IS THE DISTORTION BLOCK. K127'S 24 K_PERP I2 RESPONSE IS D3I1B[t,h,h], NOT D2I1B[h,h] AND NOT A T=0 GRAVITON PENCIL. ELIMINATING t FORMALLY GIVES -A* C^{-1} A ONLY AFTER AN OWNED INVERSE, KERNEL/GAUGE QUOTIENT, BOUNDARY ADJOINT AND COMMON CLOSED DOMAIN ARE SELECTED. IF C IS SINGULAR, ITS KERNEL ROWS ARE CONSTRAINTS AND MULTIPLIERS, NOT COEFFICIENTS TO FILL WITH A PSEUDOINVERSE. K129 MUST EVALUATE A AND C ON THE K127 BACKGROUND BEFORE BFV OR SPECTRAL REDUCTION."
target_claim: K127_NEXT_GATE__TEST_SOURCE_GLOBAL_LEGALITY_AND_METRIC_CONSTRAINT_CLOSURE_OF_RICCI_FLAT_WEYL_FAMILY
target_verdict: T0_GRAPH_ACTION_ZERO__PURE_HH_HESSIAN_ZERO__COUPLED_HT_TT_BLOCK_EXACT__K127_RADIAL_RESPONSE_RETYPED_AS_THIRD_DERIVATIVE__SCHUR_AND_BFV_REQUIRE_OWNED_OPERATOR_KERNEL_AND_DOMAIN_K129
canon_verdict_change: none
---

# Selected-K128 native I1B T=0 coupled Hessian and Schur/domain gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, native-coordinate, variational-Hessian and domain
> calculation. Ordinary Einstein/Lichnerowicz, Higgs/VEV, particle-spectrum,
> family-index, chirality, anomaly and symmetry-breaking constructions do not
> adjudicate it without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: this result binds the source-native `I1B` action germ in independent
coordinates `(g,T)` at K127's local Ricci-flat `T=0` fixed-boundary stationary
family. It does not bind a conventional GR action, a source-global GU vacuum,
or a closed physical domain.

## Result in plain English

K127 constructed nonflat Ricci-flat stationary metric germs and evaluated the
one-radial response `C_t_h_h`. K128 now asks what the actual quadratic
fluctuation operator is at those `T=0` germs.

The answer is structurally different from a curved metric pencil. In native
coordinates,

```text
varpi = B_LC(g)+T,
I1B = <T,S(F_B+(1/2)D_B T+(1/3)T^2)> + (kappa_1/2)<T,*T>.
```

Hence

```text
I1B(g,0)=0                                             (1)
```

for every metric `g`, not only Ricci-flat ones. Every pure metric derivative
along that graph is zero. Ricci-flatness is still required for full
stationarity because the first `T` derivative is the Shiab-curvature
translation row, but once that row vanishes the quadratic Hessian on
`(h,t)` has the universal form

```text
             h       t
H_T=0 = h [  0      A* ]
        t [  A       C ],                              (2)
```

where

```text
A = D_g S(F_B),
C = D_T(E_T) at T=0,
```

with the formal adjoint `A*` depending on the integration-by-parts and
boundary convention.

K127's aligned `24 K_perp I_2` is therefore

```text
D3 I1B[t,h,h],                                        (3)
```

the variation of the metric response when a radial `T` background is turned
on. It is not `D2 I1B[h,h]`, not the pure metric Hessian at `T=0`, and not a
physical two-polarization graviton operator.

## 1. Exact action-degree theorem

Write the local action germ schematically as

```text
I(x,y)=y F(x)+(1/2)y C(x)y+(1/3)Q(y,y,y),             (4)
```

with metric coordinate `x`, distortion coordinate `y`, and `F(0)=0` at the
K127 Ricci-flat stationary point. Direct differentiation gives

```text
D2_xx I = 0,
D2_xy I = DF,
D2_yy I = C(0),
D3_yxx I = D2F.                                      (5)
```

Equation (5) is coordinate and derivative-order custody, not a model fit. It
explains why K122 correctly kept native metric and distortion columns
separate, why K127's curved response is real, and why that response cannot be
inserted as a quadratic metric mass term at `T=0`.

A linear coordinate mixing `y'=y+s x` can create an apparent `x-x` entry by
congruence, but the native graph coordinate keeps the actual block in (2)
legible. Such a generated entry is a coordinate representative, not a newly
owned pure metric action term.

## 2. Conditional Schur reduction

If `C` is invertible on a specified common domain, the `t` equation formally
gives

```text
t = -C^{-1} A h
```

and substitution produces the effective metric expression

```text
H_eff = -A* C^{-1} A.                                (6)
```

Equation (6) is not yet an owner result. In the field theory, `C^{-1}` requires
all of the following:

- the actual coefficientwise `T-T` differential operator on the K127
  background;
- a treatment of its gauge and null directions;
- one closed domain shared with `A` and `A*`;
- boundary conditions that make the stated formal adjoint the operative one.

Without those, (6) is a reverse conditional only. It may be nonlocal even
when `A` and `C` are local.

## 3. Singular block and constraint control

The exact planted control takes

```text
C=diag(c,0),  A=diag(a1,a2).
```

Then the `t` equation is

```text
c t1+a1 h1=0,
a2 h2=0.                                             (7)
```

The first row eliminates `t1`; the second is a constraint on `h2`, while the
kernel variable `t2` remains a multiplier. Replacing `C` by
`diag(c,epsilon)` gives an effective coefficient `-a2^2/epsilon`, which
depends on the regularization and diverges as the kernel returns. A fitted
pseudoinverse would silently choose a quotient and pairing.

Therefore a singular distortion block routes to constraint/BV-BFV analysis,
not to a guessed two-field pencil.

## 4. Consequences for K127 and the Green/domain seam

K127 remains exact at its stated grade:

- Ricci-flat `T=0` local stationary germs exist;
- the aligned one-radial response is `24 K_perp I_2`;
- generic Weyl curvature leaks outside the selected plus/cross plane.

K128 changes the interpretation of the next operator gate. Neither the
aligned compression nor its local Green representative is the full quadratic
`T=0` Hessian current. The operative quadratic boundary form must be derived
from the complete coupled blocks `A,A*,C`. A conventional Ricci-flat
Lichnerowicz/Einstein operator cannot be imported as `H_eff`; it would need to
be derived from (6), including coefficient, kernel, gauge and domain custody.

The current source bank does not yet serialize the complete background-
evaluated `A,C` packet or a common closed domain. Source-global background
legality is likewise not promoted by the local K127 germ. These are precise
dependencies, not permission to fit missing entries.

## 5. Reverse scaffold

```text
R0 K127: local Ricci-flat T=0 stationary family is exact.
R1 K127: D3[t,h,h] gives aligned 24 K_perp I2; generic Weyl leaks off TT.
R2 K128: I1B(g,0)=0 identically, so D2[h,h]=0.
R3 K128: actual T=0 Hessian is [[0,A*],[A,C]].
R4 K128: -A*C^{-1}A is conditional on inverse, quotient and domain.
R5 K129: evaluate A and C on the same background; classify kernels/gauge.
R6 later: choose a common Green/Krein domain and construct BV-BFV reduction.
R7 only then: test a physical spectrum, positive cohomology and superposition.
```

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k128_native_i1b_t0_coupled_hessian_and_schur_domain_gate_probe.py
```

## K129 successor classification

K129 evaluates the two blocks without importing the repository's earlier
nonzero-`Phi1` stationary Hessian. On K127's Ricci-flat `T=0` germ,
`A=D_g[S_g(F_B)]` is the natural selected curvature linearization, with
principal ranks `6/6/4`, exact diffeomorphism radical and two additional null
TT characteristics; generic Weyl curvature still leaks off the selected TT
plane. The distortion operator is `C=kappa_1 K+E(D_B)`. Its nondegenerate
algebraic map removes the zero-momentum kernel only for nonzero `kappa_1`,
while its covariant first-order adjacent-grade block has exact parity-completed
ranks `24/24/22`. This does not select `kappa_1`, a global inverse, boundary
adjoint, common closed domain or BFV quotient. K130 owns the complete
characteristic/Green and coupled constraint-domain packet.
