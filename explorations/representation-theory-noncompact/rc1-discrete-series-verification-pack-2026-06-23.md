---
title: "RC1 Discrete-Series Verification Pack: OQ1/OQ2/OQ3"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "rc1-discrete-series-verification-pack"
verdict: FAILS_AS_STATED
---

# RC1 Discrete-Series Verification Pack

## Scope

This note checks the three RC1 follow-up gates from
`explorations/generation-sector/rc1-rs-kk-zero-mode-2026-06-23.md`:

- **RC1-OQ1:** parabolic/Flensted-Jensen parameter
  `Lambda_RS^{FJ} = 3/2`.
- **RC1-OQ2:** restricted-root multiplicities `(m_1,m_2)=(7,1)`.
- **RC1-OQ3:** Kobayashi / H-admissibility route for the RS contribution.

Files read: `rc1-rs-kk-zero-mode-2026-06-23.md`,
`rc3-root-multiplicity-bc1-2026-06-23.md`,
`rc3-harish-chandra-c-function-2026-06-23.md`,
`n5-discrete-series-gl4r-2026-06-23.md`, and
`weyl-group-s4-orbit-2026-06-23.md`.

## Executive Verdict

The verification pack **does not pass as stated** for the symmetric pair

```text
(G,H) = (SL(4,R), SO_0(3,1)).
```

The obstruction is structural. The rank-one BC1 chain in RC1/RC3/N5 uses, at the decisive
split-rank step, the involution

```text
sigma_block(X) = J X J^{-1},     J = diag(1,1,1,-1),
```

whose fixed algebra is block diagonal of dimension 9, not `so(3,1)` of dimension 6.
For the actual Lorentz-metric symmetric pair, the involution is

```text
sigma_metric(X) = - eta X^T eta^{-1},     eta = diag(1,1,1,-1),
```

and the split rank is 3, not 1. Therefore the BC1 root multiplicity
`(m_1,m_2)=(7,1)`, the scalar pole ladder `nu_n=(2n+1)/2`, and the
split-rank-one Flensted-Jensen multiplicity-one route are not verified for the stated pair.

| Gate | Verdict | Reason |
|---|---|---|
| RC1-OQ1: `Lambda_RS^{FJ}=3/2` | **Not verified for the stated pair** | The raw one-line value `lambda_RS(H_0)=1` checks after conjugating `H_0` to `diag(1,0,0,-1)`, and `1+1/2=3/2` is arithmetically consistent with the asserted tau-shift. But the local notes do not compute the parabolic `M`-parameter, and the rank-one FJ scalar parameter is not available once the actual pair has rank 3. |
| RC1-OQ2: `(m_1,m_2)=(7,1)` | **Falsified as stated** | Direct matrix checks give actual split rank 3. With a full diagonal Cartan the restricted root system is A3 with six positive roots of multiplicity 1. If one restricts artificially to the line `diag(1,0,0,-1)`, the positive eigenvalue counts are `(4,1)`, not `(7,1)`. The missing dimensions are centralizer/zero-root directions, not short-root multiplicity. |
| RC1-OQ3: Kobayashi H-admissibility route | **Not established** | The current route depends on the same rank-one/Flensted-Jensen premise. Bottom K-type branching is necessary evidence for an H-map, but it is not a Kobayashi admissibility proof. An asymptotic K-support / cone check is still required after the symmetric pair is fixed. |

## Matrix Check

I ran a lightweight exact matrix check over the standard `sl(4,R)` basis.

```text
dim sl4 = 15
metric sigma fixed dim (so(3,1)) = 6
metric sigma anti-fixed q dim = 9
block-conjugation fixed dim = 9
block-conjugation anti-fixed q dim = 6
metric p cap q dim = 6
block p cap q dim = 3
three diagonal traceless matrices in metric q: True, True, True
three diagonal traceless matrices in p: True, True, True
all pairwise diagonal commutators zero: True
therefore metric split rank = 3
ad diag(1,0,0,-1) eigenvalue counts on sl4 off-diagonal:
  -2:1, -1:4, 0:2, +1:4, +2:1
```

The rank conclusion is immediate: the actual metric `p cap q` contains the commuting
diagonal traceless subspace

```text
span{diag(1,-1,0,0), diag(1,0,-1,0), diag(1,0,0,-1)}.
```

Since `rank(sl4)=3`, this proves `split-rank(SL(4,R)/SO_0(3,1)) = 3`.
The rank-one bracket computation in N5 is internally correct for the three off-block
boost generators, but those generators come from `sigma_block`, not from the Lorentz
metric involution with fixed algebra `so(3,1)`.

## OQ1: `Lambda_RS^{FJ}=3/2`

The raw Harish-Chandra parameter used in the notes is

```text
lambda_RS = (1/2)(e_1 - e_4) = (1/2,0,0,-1/2).
```

On the diagonal representative

```text
H_0 = diag(1,0,0,-1),
```

one gets

```text
lambda_RS(H_0) = (1/2)(1 - (-1)) = 1.
```

So the **raw scalar projection** used by RC1 is consistent after replacing the
off-diagonal boost notation by its diagonal Cartan conjugate.

The asserted RS shift is

```text
rho_tau(D(1/2,0)) = 1/2,
Lambda_RS^{FJ} = 1 + 1/2 = 3/2.
```

This remains a conditional reconstruction, not a verified parabolic-induction calculation.
The notes do not compute the Langlands `M`-component for the relevant `MAN` induction.
More importantly, for the actual `SO_0(3,1)` symmetric pair the restricted Cartan is
rank 3, so there is no single BC1 Flensted-Jensen scalar parameter whose pole set is
`nu_n=(2n+1)/2`.

**OQ1 verdict:** `Lambda_RS^{FJ}=3/2` is valid only as a conditional rank-one surrogate
statement. It is **not verified for the stated pair**.

Corrected constants:

- Raw line projection: `lambda_RS(H_0)=1`.
- Claimed tau shift: `+1/2`, still unverified as an `M`-parameter computation.
- If one uses the artificial line `H_0=diag(1,0,0,-1)`, the root counts give
  `rho_line = (1/2)(4*1 + 1*2) = 3`, not `9/2`.
- For the full actual pair, use the A3 vector
  `rho_G = (3/2,1/2,-1/2,-3/2)`, not a BC1 scalar `rho=9/2`.

Failure conditions:

- If the `M`-component shift is not `1/2`, the `3/2` value fails even in the surrogate.
- If the pair is the actual Lorentz-metric pair, the rank-one FJ pole test is unavailable.

## OQ2: Root Multiplicities `(m_1,m_2)=(7,1)`

The RC3 root-multiplicity note obtains `(7,1)` from:

```text
dim(G/H) = 9,
rank = 1,
m_2 = 1,
therefore m_1 = 9 - 1 - 1 = 7.
```

The failure is the rank input. For the actual pair, `rank=3`, and the full diagonal
restricted root system is A3:

```text
dim(G/H) = rank + sum_{alpha>0} m_alpha
9 = 3 + 6*1.
```

This is dimensionally closed without any BC1 multiplicity `(7,1)`.

If one ignores the maximal Cartan and restricts to the single line
`diag(1,0,0,-1)`, the off-diagonal adjoint eigenvalue counts are:

```text
short/eigenvalue +1: 4  from E12, E13, E24, E34
long/eigenvalue  +2: 1  from E14
```

Thus even the one-line restriction gives `(4,1)`, the earlier value noted in
`oq-weyl3`, not `(7,1)`. The extra three tangent dimensions are centralizer/zero-root
directions created by using a non-maximal line; they cannot be reassigned to the
short-root multiplicity.

**OQ2 verdict:** `(m_1,m_2)=(7,1)` is **falsified as stated** for
`SL(4,R)/SO_0(3,1)`. The corrected alternatives are:

- Actual metric pair: rank 3, restricted root system A3, root multiplicities all 1.
- Artificial rank-one line inside the actual pair: positive line counts `(4,1)`,
  with `rho_line=3`.
- Rank-one block-conjugation model: split-rank-one bracket computation applies, but
  its fixed algebra is not `so(3,1)`, so the Lorentz-spinor H-type analysis must be redone.

Failure conditions that fire:

- RC1-F2 / RC3-F6 fires: the CAS-style matrix check does not produce `(7,1)`.
- RC1-F4 fires for the actual pair: split rank is not 1.

## OQ3: Kobayashi H-Admissibility Route

The existing OQ3 route is not independent enough to survive the OQ2 failure. It uses:

1. Flensted-Jensen split-rank-one applicability.
2. Multiplicity-one for the eight RS H-types
   `4D(1/2,0) + 4D(0,1/2)`.
3. Weyl/K-type branching as evidence that the bottom K-type contains the desired
   Lorentz spinors.

The branching evidence is useful, but it does not prove Kobayashi H-admissibility.
For a Kobayashi route, the missing local check is a discrete-decomposability or
admissibility criterion, e.g. an asymptotic K-support cone condition for the relevant
`(g,K)` module and subgroup `H`. The current notes do not compute that cone, and the
Flensted-Jensen premise they lean on has the wrong involution for `SO_0(3,1)`.

**OQ3 verdict:** not established. It remains a possible new route, but not a completed
verification. The current `ind_H(S_R^{eff})=8` conclusion should not be upgraded from
this pack.

Failure conditions:

- If the actual pair has split rank 3, Flensted-Jensen Theorem 4.3 in the rank-one
  form cited by the notes does not apply.
- If the bottom K-type contains `D(1/2,0)` but the restriction is not discretely
  decomposable, the Hom count need not produce a finite H-admissible contribution.
- If `lambda_RS` is only a limit parameter on a wall, Plancherel support must be
  established separately; the Weyl orbit calculation alone does not prove it.

## Next Action

1. **Fix the symmetric-pair choice.** If the target is truly the Lorentz-metric fiber
   `SL(4,R)/SO_0(3,1)`, revise the N5/RC3/RC1 chain with
   `sigma(X)=-eta X^T eta^{-1}`, split rank 3, and A3 restricted roots. If the target is
   the rank-one block-conjugation pair, rename the isotropy accordingly; it is not
   `SO_0(3,1)`.
2. **Redo the spectral model after the pair is fixed.** The BC1 c-function with
   `(m_1,m_2)=(7,1)` and `rho=9/2` should not be used for the stated pair.
3. **Run the actual Kobayashi check.** Compute the asymptotic K-support / cone criterion
   for the candidate RS module restricted to `SO_0(3,1)`, then derive the Hom multiplicity.
4. **Only then revisit RC1-OQ1.** The `+1/2` tau shift needs an explicit `MAN`
   parameter calculation in the corrected symmetric-pair setting.

