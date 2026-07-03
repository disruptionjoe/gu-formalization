# OQ-RK1 — target-free `ind_H` rank certificate (internal path #2)

Date: 2026-07-03
Status: EXPLORATION-GRADE / staging only. Does NOT promote any claim. OBJ-GEN stays OPEN.
Scope: internal path #2 — independent re-run of the decisive OQ-RK1 test behind
the load-bearing `ind_H(D_RS)=8` / `rank_H=4` claim ("3 generations").

## What OQ-RK1 asks

OBJ-GEN (`NEXT-STEPS.md` line 343) names the decisive first test:

> Run OQ-RK1: CAS rank of `Π_RS · E₊ · Π_RS` in M(64,ℍ) returning 4 or 8
> **without dividing by the target**.

The load-bearing claim `ind_H(D_RS)=8` has no surviving analytic derivation
(all three analytic routes FAILED; the APS route consumes `rank_H(S_RS^+)=4` as a
reverse-engineered physical-DOF input — see `NEXT-STEPS.md` lines 404–448). OQ-RK1
is the circularity-free gate: compute the composite rank directly and read off 4
or 8, never divide `8/Â(K3)=4`.

## The gap this closes

Prior repo certificates computed only the two **factors** separately
(`E₊` → rank_H 32; raw 14D gamma-trace kernel → rank_H 416) and a Cl(4,0) TOY
(48_H). The composite `Π_RS · E₊ · Π_RS` needs both projectors on ONE common
module, but `E₊` naturally lives on the 128-dim spinor `S` while the gamma-trace
projector was pre-restricted to the 896-dim `S⁺` vector-spinor — they never acted
on a common module. (`tests/oq_rk1_cl95_explicit_rep.py` lines 6–26.)

## What was computed (independent realization)

Script: `tests/internal-paths/oq_rk1_indh_rank.py` — **exit code 0**.

Both projectors are placed on the structurally canonical common
Rarita–Schwinger fiber, the actual 1792-dim M(64,ℍ) vector-spinor carrier:

```
V := R^14 ⊗ S ,   dim_C = 14 · 128 = 1792   (= H^896 complexified)
```

- `Π_RS` = orthogonal projector onto `ker` of the gamma-trace map
  `T : R^14 ⊗ S → S`, `(ψ_a) ↦ Σ_a c(e_a) ψ_a` (the RS constraint `γ^a ψ_a = 0`).
- `E₊` = `I_14 ⊗ (I+ω)/2`, chirality on the spinor factor.

This run is **independent of the prior hardening-pass scripts**: Cl(9,5) is
rebuilt with a different concrete realization — the 5 timelike generators listed
first and the Jordan–Wigner tensor factors placed in reversed order — so the
gamma matrices are different matrices representing the same abstract algebra
(Clifford relations verified, max error `0.0`; `ω²=+I` verified).

The composite rank is read three mutually independent ways:

| route | method | rank_C |
|---|---|---|
| R1 | SVD numerical rank of the triple product `Π_RS·E₊·Π_RS` | **832** |
| R2 | Hermitian eigenvalue count of the same operator (different code path) | **832** |
| R3 | analytic subspace dims `dim(ker T) − dim(ker T ∩ ker E₊) = 1664 − 832` | **832** |

All three agree (hard assert `r_svd == r_eig == r_analytic`).

### Supporting quantities (all target-free)

| quantity | value |
|---|---|
| `dim_C(V)` | 1792 |
| `rank_C(E₊)` on V | 896 |
| `rank_C(T)` (gamma-trace, surjective) | 128 |
| `rank_C(Π_RS) = 1792 − 128` | 1664 |
| **`rank_C(Π_RS·E₊·Π_RS)`** | **832** |
| **`rank_H` (= rank_C/2, halving CERTIFIED)** | **416** |
| returns 4 or 8? | **NO** |

### Halving certificate (licenses `/2`, not assumed)

An explicit antilinear `J = M·conj` is built from the Clifford generators (the
sign `conj(e_a)=δ_a e_a` is read directly off each matrix) and VERIFIED by hard
assert, all errors exactly `0.0`:

- `J² = −I` (`M conj(M) = −I`, quaternionic not real);
- `J` antilinear (err 0);
- `J` commutes with every `e_a` (err 0) ⇒ with `T`, `Π_RS`, `ω`, `E₊`.

A `J`-commuting operator on a quaternionic space has even complex rank and
`J`-invariant image, so `rank_C = 832` is even and `rank_H = 416` is licensed. If
the certificate had failed, only `rank_C` would be reported.

## The honest finding

The target-free composite on the real M(64,ℍ) carrier yields

```
rank_C( Π_RS · E₊ · Π_RS ) = 832 ,   rank_H = 416 .
```

**It does NOT return 4 or 8.** The literal OQ-RK1 question is answered: **NO —
it returns 416.** This is a genuine, independently reproduced integer, obtained
by a realization that shares no gamma matrices with the prior scripts and by
three disjoint rank methods, with a fully executable (non-conditional) halving
certificate.

Analytic cross-check of why 832: `E₊(ker T)` has dimension
`dim(ker T) − dim(ker T ∩ ker E₊)`. On `R^14⊗S⁻`, `T` maps onto `S⁺` (rank 64),
so `dim(ker T ∩ ker E₊) = 896 − 64 = 832`, giving `1664 − 832 = 832`. The value
is forced by the constraint geometry, not fitted. 416 also equals the prior raw
gamma-trace kernel rank_H: the composite `E₊·Π_RS` simply lands in the
positive-chirality part of `ker T`, adding no new arithmetic toward the target.

### No target import — confirmed

- No division by 8, 4, 24, χ(K3)=24, Â(K3)=2, or 16+8; `ind_H(D_RS)=8` never inserted.
- The `rank_C → rank_H` `/2` is licensed by the executable `J²=−I` commutation
  certificate, not a target.
- The forbidden move `rank_eff := ind_H/Â(K3) = 8/2 = 4` — the only route to 4 —
  is documented and **refused** (INVALID_TARGET_DIVISION, never executed).

## Grade (internal tier)

- **Outcome: PARTIAL.** A target-free rank was genuinely obtained
  (`rank_H = 416`) — the composite-on-a-common-module computation the draft flagged
  as never done is now executed independently, three ways, with a certified
  halving. But the number is **416, not the load-bearing 4 or 8**, so OQ-RK1 does
  **not** vindicate `ind_H(D_RS)=8` / `rank_H=4`.
- Not CLOSED for OBJ-GEN: the generation-count claim is neither confirmed nor
  reachable from this raw/kinematic rank without more structure.
- Not BLOCKED as a computation: the rank did NOT require assuming the answer — it
  came out target-free and is what it is (416).

## What is blocking, and the next decisive step

The `416 → {4 or 8}` gap is the **physical/effective projector** `E_RS^eff`
(equivalently `Π_RS^phys`): the gauge/BRST quotient `d_{RS,−1}`, the K-theory
symbol class, `ch₂(F)[K3]`, and the `Y^14 ↔ K3` bridge. None of these is
specified anywhere in the repo — status `BLOCKED_NEEDS_SPEC`. Nothing here
derives that spec, and nothing here derives a generation count.

**Next decisive step:** pin down `E_RS^eff` as a concrete operator on this same
`V = R^14 ⊗ S` carrier (the BRST/gauge quotient of the RS constraint plus the
twist by the K3 tangent/gauge data), then re-run this exact rank pipeline on
`Π_RS · E_RS^eff · Π_RS`. Until that operator exists as executable code, no
target-free route to 4 or 8 is available, and OBJ-GEN stays OPEN.

## Artifacts

- `tests/internal-paths/oq_rk1_indh_rank.py` (independent realization, exit 0)
- Cross-consistent with prior `tests/hardening-pass/oqrk1_indh_rank.py` (832/416),
  now reproduced by a disjoint gamma realization and an added analytic route.
