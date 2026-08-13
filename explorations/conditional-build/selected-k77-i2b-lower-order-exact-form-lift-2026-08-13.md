---
artifact_type: conditional_build_variational_result
created: 2026-08-13
run_id: RUN-20260813-115145-gu-i2b-lower-order-exact-form-lift
status: EXACT_FORM_PRINCIPAL_KERNEL_LIFTED_BY_LOWER_ORDER_HESSIAN_ON_FIXED_HQ_RESTRICTED_CRITICAL_BRANCH
target_claim: NONE-NOT-A-KILL
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B lower-order exact-form lift

## Result

The fourteen-dimensional exact-form family

\[
K(k)\xi=k\otimes\xi
\]

is an exact kernel of the selected I2B **principal** Hessian. The predecessor
correctly retyped it as a non-gauge `Cl1` differential degeneracy rather than
the source's rank-25 `Cl2` adjoint-gauge image. This wave asks the distinct
question: does that family remain in the kernel of the full linearized action
Hessian after the already-owned lower-order terms are included?

On the fixed-`H_q`, real-K77 restricted radial critical branch, the answer is
**no**. The restriction of the lower-order Hessian to `im K(k)` has full
column rank `14` for exact timelike, spacelike, generic non-null and null
covectors. The derivative/lower-order cross block vanishes on this family, so
the result is independent of the tested nonzero Fourier scale. Exact
fourteen-row minors are nonzero in all four cases.

This lifts an accidental principal kernel at this background. It does not
remove the principal characteristic variety: lower-order terms cannot alter
the top-order symbol. It also does not define a physical fluctuation spectrum,
because this radial branch is critical only on the selected four-real family
and remains nonstationary on the full 196-cell connection bank.

## The calculation

For the residual-square action `SC-ACT-04`,

\[
I_2^B(A)=\frac12\langle\Upsilon(A),\Upsilon(A)\rangle,
\]

the action Hessian is

\[
D^2I_2^B(\alpha,\beta)
=\langle D\Upsilon\,\alpha,D\Upsilon\,\beta\rangle
+\langle\Upsilon,D^2\Upsilon(\alpha,\beta)\rangle.
\]

The second term is load-bearing here. The branch residual is nonzero but
Krein-null; it nevertheless contributes to the Hessian. For every tested
covector, its restriction has rank `14`, and deleting it changes the exact
lower-order matrix. A Hessian calculation that silently uses only
`(D Upsilon)^*D Upsilon` therefore computes the wrong object at this
nonzero-residual background.

Writing the full restricted Fourier column as

\[
H(tk)K(tk)=tM_1+t^2M_2,
\]

the probe finds

```text
                         rank(M1)   rank(M2)   rank at t=1,-1,2
timelike                    14          0          14,14,14
spacelike                   14          0          14,14,14
generic non-null            14          0          14,14,14
null                        14          0          14,14,14
```

Thus the lifting at this branch is purely lower-order. It is not a disguised
principal or gauge effect.

## Layer 0

| phrase | object proved here | kept distinct |
| --- | --- | --- |
| principal kernel | kernel of the top-order `196 x 196` Hessian symbol | full finite-frequency kernel |
| exact-form family | `Cl1` map `xi -> k tensor xi` | source `Cl2` adjoint-gauge map |
| lower-order lift | fixed-background action Hessian on 14 columns | source BV quotient or physical carrier |
| critical branch | radial critical point inside four selected directions | stationary point of all 196 fields |
| Hessian rank | finite constant-background variational theorem | spectrum, propagator, stability or particle count |

The two `C^(32,32)` halves, their possible block subgroup, full
`U(64,64)` parent, selected K77 connection and source's independent
connections remain separately typed.

## Source return

The source owns the bosonic residual-square architecture (`SC-ACT-04`). It
does not publish this exact K77 reduction, the fixed-`H_q` Hessian, or the
fourteen-column lifting theorem.

```text
SOURCE-CONFIRMS: SC-ACT-04 residual-square architecture.
SOURCE-SILENT: exact real-K77 lower-order Hessian and exact-form lifting.
REPO-DERIVES: the scoped fixed-background finite-frequency theorem above.
```

## Specialist review

- **Variational bicomplex:** both Hessian summands are mandatory away from a
  zero residual. The residual-dependent term fires at full rank here.
- **PDE/microlocal:** the principal null cone survives as top-order data even
  when the complete finite-frequency operator lifts a principal kernel.
- **Krein/operator:** a nonzero null residual can contribute nontrivially to
  second variation; zero norm is not zero vector.
- **Gauge/BV:** this family is not the source gauge image. Its lifting neither
  breaks gauge symmetry nor constructs the physical gauge quotient.
- **Symplectic geometry:** no rank result on a nonstationary finite Hessian is
  promoted to a presymplectic reduction or phase space.
- **Contrary review:** exact null and non-null covectors, nonzero minors,
  symmetry checks, and a planted deletion of the residual term prevent the
  easy overreads.

Hostile verdict:
`SCOPED_RESULT_SURVIVES__FIXED_HQ_RESTRICTED_CRITICAL_BRANCH_ONLY`.

## Progress and next gate

```text
Ledger v0.236 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: fixed-branch lower-order lift closed · physical stationary/BV gate remains
```

No field, parameter, quotient, selector or datum is added. P1/P2/P3 remain
unchanged and unused.

Next construct one source/action-owned **full stationary jet** (or prove none
exists on this carrier), then recompute the full Hessian and induce the actual
rank-25 source BV distribution on the action-owned physical carrier. Only at
that like-for-like grade should the remaining null quotient be compared with
Einstein `2/2`.

## Reproduction

```sh
uv run --cache-dir /private/tmp/gu-uv-cache \
  --with sympy==1.14.0 --with numpy==2.5.1 \
  python -u tests/channel-swings/selected_k77_i2b_lower_order_exact_form_lift_probe.py
```

The exact packet passes `63/63` checks.
