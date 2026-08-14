---
artifact_type: exact_wholesale_variational_and_reality_classification
created: 2026-08-14
status: REAL_ACTION_AT_CONJUGATION_FIXED_BACKGROUND_CANNOT_SPLIT_W_MIRROR_FINGERPRINTS__SPONTANEOUS_NONFIXED_VACUUM_BV_AND_DOMAIN_EXITS_SURVIVE
source_return: SOURCE_CONFIRMS_NONCHIRAL_TOTAL_AND_EMERGENT_CHIRAL_TARGET__SOURCE_SILENT_REAL_ACTION_VACUUM_SELECTOR_BV_AND_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-G1a]
canon_verdict_change: none
---

# Selected K77 W/mirror real-action wholesale gate

## Result first

Do **not** build another large W/mirror Hessian at a conjugation-fixed
background. An entire class is decided before its coefficients are known.

Let `tau` be the exact anti-linear involution exchanging the rank-192 K77
sector `W` with its ASD mirror `M`. If a complex-linear operator preserves
`W+M` and is even or odd under `tau`, its two diagonal blocks have the form

```text
A_even = diag(B,  conjugate(B)),
A_odd  = diag(B, -conjugate(B)).
```

Consequently the two blocks have equal rank and nullity, and their
characteristic polynomials are conjugate up to the odd-class sign. Therefore
no real conjugation-invariant spectral fingerprint separates them. This
decides the complete `tau`-even block-preserving class on complex rank 192,
of real dimension

```text
2 * 192^2 = 73,728,
```

without enumerating a basis of 73,728 matrices.

The variational consequence is immediate. At a `tau`-fixed stationary
background, the Hessian of a real `tau`-invariant action is `tau`-even and
formally Helmholtz symmetric (graded-symmetric in the fermionic category).
If it preserves W and mirror separately, it cannot distinguish them by rank
or nullity, and their characteristic polynomials remain conjugate. If it
mixes them, separate W/mirror
fingerprints are not defined and the physical object must instead be sought
on the combined complex.

This is a class-relative no-selection theorem, not a no-go against emergent
chirality. A real invariant action can have two non-fixed stationary vacua
exchanged by `tau`; the Hessian at either chosen vacuum can distinguish its
two component directions. The exact control

```text
S(x,y) = (x^2+y^2-1)^2 + 3 x^2 y^2
```

has conjugate stationary vacua `(1,0)` and `(0,1)` with Hessians
`diag(8,6)` and `diag(6,8)`. The action makes the pair, but does not choose a
member. An observer sector, boundary condition or external datum may still
choose one; a source-derived dynamical rule might do so only if it breaks the
same anti-linear symmetry at the selected solution.

## Why the proposed frozen Helmholtz search was not run

The source-faithful frozen I2B path is already

```text
I2B = 1/2 <Upsilon_print, Q_B Upsilon_print>.
```

It is an explicit action. Its stationary Hessian has the formal Helmholtz
symmetry by construction. The first transgression `E_act` is likewise already
an Euler covector of its written action. The unresolved issue is not whether
either frozen object is variational; it is which moving completion, physical
tangent/BV reduction and vacuum owns the physical equation. Re-running an
inverse-variational test on the frozen residual square would have been a
tautology.

## Exact K77 attachment

The executable certificate verifies over the Gaussian rationals that:

- `conjugate(P_W)=P_M`, while the projectors are not equal;
- a conjugate basis of W is a full rank-192 basis of M;
- both current Spin-natural action pairing lines are homogeneous under
  conjugation and give conjugate-up-to-sign W/mirror restrictions of equal
  rank;
- the positive-base `H_q` comparator is conjugation-odd and still gives equal
  W/mirror bilinear rank;
- the current rolled principal symbol is conjugation-even;
- a planted one-sided projector does split ranks, but only by breaking the
  real structure.

Thus the theorem applies to every current reality-compatible fixed-background
candidate, not only to the three displayed forms. It does not say that W and
mirror are the source's two ambient `C^(32,32)` Weyl halves; those remain
distinct objects.

## Layer 0 and claim ceiling

| object | result here | not established |
| --- | --- | --- |
| source I2B | explicit frozen residual-square action | complete moving physical action |
| Hessian at a `tau`-fixed solution | `tau`-even; W/mirror ranks/nullities equal and characteristic polynomials conjugate when block-preserving | Hessian at a broken non-fixed vacuum |
| W/mirror | exact conjugate rank-192 sectors | the two ambient `C^(32,32)` carrier halves |
| formal Helmholtz symmetry | necessary variational structure | positivity, stability or well-posedness |
| block theorem | all `tau`-homogeneous block-preserving operators | `tau`-breaking BV/domain/observer reduction |
| broken-vacuum control | exact escape exists mathematically | GU constructs or selects such a vacuum |

No mirror is removed, no physical cohomology is constructed, and no anomaly,
index, generation count, residue coordinate, quotient, datum, canon verdict or
public posture changes.

## Source return

The 2021 source asserts a nonchiral total theory with emergent chiral sectors
and gives a stylized low-curvature decoupling mechanism. It does not provide
the repository's W/mirror projectors, a K77 real action whose stationary
vacuum is non-fixed under their conjugation, a vacuum-selection law, a primal
BV differential or a closed asymmetric domain.

```text
SOURCE-CONFIRMS: nonchiral total theory and emergent-chiral target.
SOURCE-SILENT: K77 W/mirror real-action vacuum, its selection, BV/domain exit.
REPO-DERIVES: fixed-background real-action class cannot split W/mirror fingerprints.
```

## Hostile boundary and next gate

The strongest surviving dissent is spontaneous symmetry breaking. The
theorem compares the two sectors at one conjugation-fixed solution; it does
not compare the Hessian at a vacuum with the Hessian at its distinct conjugate
partner. It also assumes the operator preserves W and M separately. These are
fences, not defects.

The efficient successor is therefore:

1. identify the smallest source/action-owned bosonic or fermionic stationary
   background that is **not** fixed by W/mirror conjugation;
2. prove that the two conjugate vacua are stationary in the full owned tangent,
   not only a reconstructed slice;
3. compute the W/mirror Hessian or BV fingerprints there;
4. state what selects one vacuum from the degenerate pair;
5. only then pay for physical cohomology and the analytic domain.

If every source-owned stationary background is conjugation-fixed, stop the
Hessian route and test a genuinely asymmetric BV/BFV or domain construction.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_w_mirror_real_action_wholesale_gate_probe.py
```

The exact probe passes `42/42` checks.
