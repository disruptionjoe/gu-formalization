# Figure assets -- One Residual paper

Figure-ready source for the three paper figures. Each is reproducible from an in-repo test; a
LaTeX/matplotlib pass can render these directly. Data are exact (existence-computed) at the grades marked.

---

## Figure 1 -- Sector scoreboard (the headline)

*A geometric framework accommodates the five physics sectors; four cleared, none falsified; all residual
freedom in one object.* Suggested render: 5-row status chart, green = cleared, amber = reduced.

| Sector | Status | Grade | Reproducible test (exit 0) |
|---|---|---|---|
| Standard Model (gauge + content) | CLEARED | existence | `tests/one-residual/sm_pati_salam_stabilizer.py`, `sm_mirror_anomaly_free.py`, `sm_so10_cubic_casimir_and_mirror.py` |
| Forces | CLEARED | existence | `tests/one-residual/forces_maxcompact_independent.py`, `tests/legs/forces_maximal_compact_is_sm.py` |
| Quantum / unitarity | CLEARED | existence (faithful model) | `tests/one-residual/qm_krein_unitary_repair.py` |
| Dark energy | CONSISTENT (sign-only) | consistency; canon OPEN | `tests/one-residual/dark_energy_desi_sign.py` |
| Gravity | REDUCED (1 scalar) | disproof of 1 branch | `tests/one-residual/gravity_branch2a_eliminated.py` |
| **Residual** | -- | **one object: the source action's declaration + coefficients** | (unwritten) |

Caption: "Four of five sectors are cleared at existence/consistency grade with reproducible computation;
gravity is reduced to a single undetermined coefficient. All remaining freedom -- gauge-vacuum selection,
the generation count, the gravity coefficient -- is jointly fixed by one object."

---

## Figure 2 -- The SM gauge algebra as a maximal compact (no extra photon)

*The maximal compact of `su(3,2)` is exactly `su(3)+su(2)+u(1)`.* Suggested render: a 5x5 block diagram
(3+2) with the compact `u(3)+u(2)` blocks highlighted and the single relative-trace `u(1)` labeled.

```
su(3,2)  (dim 24)                 maximal compact  (Cartan involution / Krein form)
  [ 3x3 | 3x2 ]                     [ su(3)  |   0   ]   dim 8   (gluons)
  [-----+-----]   -- theta -->      [--------+-------]   dim 3   (weak SU(2))
  [ 2x3 | 2x2 ]                     [   0    | su(2) ]   dim 1   (ONE u(1): hypercharge)
                                    off-block norm = 0.00e+00;  extra U(1)s = 0
```

Key numbers (from `forces_maxcompact_independent.py`): dim k = 12 (= 8+3+1); block-diagonal (off-block
norm 0); exactly one `u(1)`. Caveat to print: `su(3,2)` is a non-native sub-block (native `so(5,5)` has
maximal compact `so(5)+so(5)`, not the SM); which sub-block is selected is the residual.

---

## Figure 3 -- The primary-partition of the family-puzzle toolkit

*In `pi_3^s = Z/24 = Z/8 (+) Z/3`, only 3-primary-reaching invariants can force an odd generation count.*
Suggested render: two columns (CANNOT | CAN), split by CRT summand.

| CANNOT force odd count (2-primary / free) | CAN reach the 3-primary summand |
|---|---|
| Dirac / Atiyah-Singer index (`Z`) | Adams e-invariant / J-hom (`Z/24`) |
| per-generation anomaly (`Z`) | Garcia-Etxebarria-Montero (`Z/9`) |
| mod-2 Witten anomaly (`Z/2`) | Wan-Wang-Yau beyond-cohomology |
| Rokhlin (`Z/16`), spinor `2^k` | equivariant Spin/KO `G`-index (`Z/3`) |

Key fact (from `tests/family-puzzle/primary_partition_lemma.py`): a finite-2-group- or `Z`-valued invariant
vanishes on the 3-primary summand (`gcd(3,2^k)=1`, `Hom(Z/24,Z)=0`). Caption: "The literature's successes
are exactly the 3-primary-reaching tools; the count is located there (prior art: GEM 1808.00009, WWY
2605.26202) and, by no-net-chirality, at a boundary."

---

## Rendering notes

- Figures 1 and 3 are tables -> typeset directly. Figure 2 is a block diagram -> tikz/matplotlib.
- Optional plot (not required): dark-energy `w_DE(z)` vs the DESI CPL band, generatable from
  `dark_energy_desi_sign.py` (shows the non-monotone curve and the sign-window mechanism). Weakest-leg,
  include only if space allows.
- All data are existence/consistency grade per the paper's Hardening-pass ledger; do not render "derived".
