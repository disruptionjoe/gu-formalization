# A2a — OQ-RK1 `ind_H` rank certificate (no target import) — RESULTS DRAFT

Date: 2026-07-03
Status: DRAFT / staging only. Does NOT promote any claim. OBJ-GEN stays OPEN.
Scope: hardening item "OQ-RK1: ind_H rank certificate (no target import)".

## Question under audit

OBJ-GEN row (NEXT-STEPS.md line 315) asks, as the decisive first test for the
load-bearing `ind_H(D_RS)=8` claim:

> Run OQ-RK1: CAS rank of `Π_RS·E₊·Π_RS` in M(64,ℍ) returning 4 or 8 without
> dividing by the target.

Prior certificates computed the two FACTORS separately (`E₊` → rank_H 32; raw
14D gamma-trace kernel → rank_H 416) and a Cl(4,0) TOY composite (48_H), but the
**composite `Π_RS·E₊·Π_RS` on one common module of the actual Cl(9,5) carrier
was never computed** — because `E₊` lived on the 128-dim spinor while the
gamma-trace projector was pre-restricted to the 896-dim `S⁺` vector-spinor.
This item closes that gap.

## What was computed

Both projectors are placed on the **structurally canonical common
Rarita–Schwinger fiber**

```
V := R^14 ⊗ S ,   dim_C = 14 · 128 = 1792   (= H^896 complexified)
```

This 1792_C space is exactly the "actual 1792-dim M(64,ℍ) vector-spinor carrier"
named in the OQ-RK1 gap. On `V`:

- `Π_RS` = orthogonal projector onto `ker` of the gamma-trace map
  `T : R^14 ⊗ S → S`, `(ψ_a) ↦ Σ_a c(e_a) ψ_a` (the standard RS constraint
  `γ^a ψ_a = 0`). Built only from the Clifford generators `e_a` already in
  `oq_rk1_cl95_explicit_rep.py`.
- `E₊` = `I_14 ⊗ (I+ω)/2`, chirality acting on the spinor factor.

Neither operator is chosen to hit a number. The composite is a genuine matrix
product; its rank is read off, never asserted.

### Direct result (`tests/hardening-pass/oqrk1_indh_rank.py`, exit 0)

| quantity | value |
|---|---|
| `dim_C(V)` | 1792 |
| `rank_C(E₊)` on V | 896 |
| `rank_C(T)` (gamma-trace, surjective) | 128 |
| `rank_C(Π_RS)` = 1792 − 128 | 1664 |
| **`rank_C(Π_RS · E₊ · Π_RS)` (SVD)** | **832** |
| **`rank_C(Π_RS · E₊ · Π_RS)` (Hermitian eigen-count, independent)** | **832** |
| cross-check `rank(E₊ · Π_RS)` | 832 |
| **`rank_H` (= rank_C / 2, halving CERTIFIED)** | **416** |
| returns 4 or 8? | **NO** |

### Quaternionic-structure certificate (licenses the halving)

The `/2` is **not** assumed. An explicit antilinear `J = M·conj` is constructed
from the Clifford generators and VERIFIED by hard assert:

- `J² = −I` (`M conj(M) = −I`, exact, err 0);
- `J` antilinear (err 0);
- `J` commutes with every `e_a` (err 0) ⇒ with `T`, `Π_RS`, `ω`, `E₊` (err 0).

A `J`-commuting operator on a quaternionic space has even complex rank and
`J`-invariant image, so `rank_C = 832` is even and `rank_H = 416` is licensed.
Had the certificate failed, only `rank_C` would be reported.

### Independent re-derivation (`tests/hardening-pass/verify/oqrk1_indh_rank_indep_check.py`, exit 0)

Independent in four ways: (1) reversed Jordan–Wigner tensor ordering **and**
timelike-first signature placement — different concrete gamma matrices;
(2) `Π_RS` from an SVD null-space basis `N` (`Π_RS = N N†`), not the resolvent;
(3) composite rank from the singular values of `E₊N` (rank of `E₊` restricted to
`ker T`), never forming the triple product; (4) the halving certified **on the
actual image** `W = range(composite)`: `J` restricted to `W` induces an
antilinear map squaring to `−I_{832}` (residual 2.5e-15), forcing
`dim_C(W) = 2·416`.

Result: `rank_C = 832`, `rank_H = 416`. **Agrees exactly with the direct route.**

## Interpretation — the honest finding

The direct, target-free composite on the real M(64,ℍ) carrier yields

```
rank_C( Π_RS · E₊ · Π_RS ) = 832 ,   rank_H = 416 .
```

**It does NOT return 4 or 8.** The number 416 also equals the prior raw
gamma-trace kernel rank_H (832_C = 416_H) computed in
`oq_rk1_cl95_explicit_rep.py`: the composite `E₊·Π_RS` simply lands in the
positive-chirality part of `ker T`, which is precisely that `S⁺` vector-spinor
kernel. So the composite adds no new arithmetic toward the target; it reproduces
the raw kernel count.

This is the expected PARTIAL outcome from the honest-outcome menu: the composite
IS now computed on a defensibly-chosen common module (the canonical RS fiber
`R^14 ⊗ S`), the halving is genuinely certified (not conditional), and the honest
integer is a large number (416), **not** the target.

### Does it depend on any target import? NO.

- No division by 8, 4, 24, χ(K3)=24, Â(K3)=2, or 16+8.
- `ind_H(D_RS)=8` is never inserted.
- The `rank_C → rank_H` `/2` is licensed by the executable `J²=−I`
  commutation certificate, not by a target.
- No rank-`r` sub-projector of `E₊` is selected.
- The forbidden move `rank_eff := ind_H/Â(K3) = 8/2 = 4` is documented and
  **refused** — it is the ONLY route to 4, and it is an INVALID_TARGET_DIVISION.
- The RS decomposition split is **not** used as a physical invariant
  (RSDecompositionValidityAudit_V0 firewall respected): the computation is a raw
  finite-dimensional rank on an explicit carrier, not a claim that this split is
  the physical index.

### What this closes, and the standing residual

CLOSED: the specific gap that only the two factors (32, 416) and a Cl(4,0) toy
(48_H) had been computed — the composite on the real 1792-dim carrier is now
computed (416_H) by two independent routes with a certified halving.

RESIDUAL (explicit): 416 is the rank of the *raw / kinematic* RS constraint
composite. Reaching a small effective rank (whatever it is) still requires the
physical projector `Π_RS^phys` / `E_RS^eff` — the gauge/BRST quotient
`d_RS,−1`, K-theory symbol class, `ch₂(F)[K3]`, and the `Y^14 ↔ K3` bridge —
which remain `BLOCKED_NEEDS_SPEC` (see `oq_rk1_e_rs_eff_assembly.py`). Nothing
here derives that spec, and nothing here derives a generation count.

## Grade (internal tier)

- **Honest grade: PARTIAL / SUCCESS.** The decisive composite is now an executed,
  target-free CAS rank with an independent re-derivation and a certified
  (non-conditional) `rank_H`. The literal OQ-RK1 question — "does it return 4 or
  8?" — is answered: **NO, it returns 416.**
- **Tier:** executable certificate + numbers + exit status + independent method,
  consistent with the standing evidence that all analytic routes to
  `ind_H(D_RS)=8` failed.

## Verdict

OBJ-GEN remains **OPEN**. The generation-count verdict stays OPEN; nothing here
derives three (or four). The deliverable is the certificate and the honest
number, not a generation count.

## Artifacts

- `tests/hardening-pass/oqrk1_indh_rank.py` (direct, exit 0)
- `tests/hardening-pass/verify/oqrk1_indh_rank_indep_check.py` (independent, exit 0)
