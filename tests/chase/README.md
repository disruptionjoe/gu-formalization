# Chase-to-kill verification scripts (2026-06-30)

Runnable, self-contained scripts that drove five PURSUE threads (from the 2026-06-30 triage,
`lab/roadmap/triage-pass-underexplored-movable-objections-2026-06-30.md`) to a **terminal
computational verdict**. Each thread had a chaser + an independent re-verifier that reran with a
different method/codebase; all five reproduced (zero flips). These are real computations, not
`hourly_*` self-asserting bookkeeping — run them.

## Verdicts

| Thread | Verdict | Key number | Authoritative script |
|---|---|---|---|
| MOVE-1 GS factorizability (Sp(1) vs Sp(64) octic) | **PARTIAL** | p4 = −1/2419200 ≠ 0; net chirality −13; Sp(64) octic = 2·P4 (irreducible) vs Sp(1) octic = 128·(y²)⁴ (reducible) | `MOVE-1/move1_octic_sp64_vs_sp1.py`, `MOVE-1/verify/indep_ahat16.py` |
| MOVE-2 θ-field wₐ sign vs DESI | **KILLED** | global CPL fit z≤2: w₀=−0.777, **wₐ=−0.248 (<0, same sign as DESI)**; sign flips with window | `MOVE-2/verify/indep_check.py` (authoritative) |
| MOVE-3 Willmore-EL order on Schwarzschild | **KILLED** | H⁽¹⁾=(M/r)η harmonic → ΔH⁽¹⁾≡0; true residual O(M²/r⁴) | `MOVE-3/willmore_el_order.py` |
| MOVE-4 Majorana channel dim, Spin(9,5) | **CONFIRMED** | checksum 16384=128²; **dim Hom(S⁺⊗S⁺, Λ⁰)=0** | `MOVE-4/move4_spinor_square_forms.py` |
| MOVE-5 Krein SW-source chiral count | **KILLED (no-go hardened)** | **net chiral index of im(M) = 0** exactly (400 samples × 3 signatures), Ψ-independent | `MOVE-5/krein_nogo_chiral_index.py` |

## Important: MOVE-2 authoritative script

`MOVE-2/theta_flrw_wa.py` (the chaser's main script) prints the **superseded** local-derivative
reading ("wₐ>0, clean falsification"). That framing was overturned by the re-verifier: under DESI's
own **global CPL fit** over the measured window (z≤2), wₐ is **negative** (same sign as DESI),
~3× smaller in magnitude → ΛCDM-amplitude-degenerate, not a falsification. The authoritative
computation is `MOVE-2/verify/indep_check.py`. A note to this effect is in the main script's header.

## Grades (honest)

- **Exact / unconditional mathematics** (theorems about the objects, independent of GU): MOVE-1's
  `[Â(TY14)]₁₆` (matches Alvarez-Gaume-Witten to the integer) + octic group theory; MOVE-4's
  Spin(9,5) representation theory (all errors 0.00e+00).
- **Reconstruction-grade numeric checks on assumed/imported inputs**: MOVE-2 (assumed action on an
  imported ΛCDM background), MOVE-3 (imported linearized Schwarzschild metric), MOVE-5 (posited SW
  template action).
- **None is a physics derivation of Geometric Unity.** They adjudicate specific canon claims and
  red-flags. The source-action bottleneck is untouched by all five.

## Running

Python 3.14 + numpy/sympy/scipy. From the repo root, e.g.:

```
python tests/chase/MOVE-1/move1_octic_sp64_vs_sp1.py
python tests/chase/MOVE-2/verify/indep_check.py
```

MOVE-5 samples and takes a few minutes. MOVE-4's main script is slow on this box
(>9 min, may not finish in a short timeout); its verdict was independently confirmed
twice in the chase, so for a quick reproduction reduce the sample count or run the
independent check under `MOVE-4/verify/`.
