# H51 (Wave 31) -- c_L threshold gate for the first GU-under-H36 prediction

**Object.** Wave 30 reduced GU-under-H36's first parameter-linked prediction to one uncomputed positive
coefficient:

```text
rho_Lambda = c_L * mu_DW^4
m2 = sqrt(m2_eff) * mu_DW
lambda = hbar_c / m2
```

This Wave 31 gate does **not** compute the geometric DeWitt coefficient `c_L`. It computes the exact decision
thresholds H51 has to hit: how small the normalized positive `c_L` must be for the H36-linked sub-mm gravity
prediction to move from **face-value excluded** back to the live experimental frontier.

**Test:** `tests/wave31/H51_cl_threshold_gate.py` -- deterministic, exit 0.

---

## Result

At `c_L = 1`, the script reproduces H50's face-value prediction:

| `c_L` | `mu_DW` | predicted `lambda` band |
|---:|---:|---:|
| 1.000 | 2.300 meV | 76.74-93.98 um |

Since `mu_DW = rho_Lambda^(1/4) / c_L^(1/4)`, smaller `c_L` raises `mu_DW` and shortens the Yukawa range.
Representative values:

| `c_L` | `mu_DW` | predicted `lambda` band |
|---:|---:|---:|
| 0.375 | 2.939 meV | 60.05-73.55 um |
| 0.250 | 3.253 meV | 54.26-66.46 um |
| 0.200 | 3.439 meV | 51.32-62.85 um |
| 0.125 | 3.868 meV | 45.63-55.88 um |

The fair `alpha = 1/3` frontier band inherited from H50 was `mu_DW ~= 3.0-3.6 meV` (argued from the published
short-range-gravity curves, not digitized). Converted to `c_L`, this gives:

```text
GU-under-H36 returns to the live/frontier band iff c_L is roughly <= 0.17-0.35.
```

More exactly, using `rho_Lambda^(1/4) = 2.3 meV`:

| required `mu_DW` floor | equivalent `c_L` threshold |
|---:|---:|
| 3.0 meV | 0.345 |
| 3.6 meV | 0.166 |

So H51 does **not** require a tiny or cosmologically tuned coefficient. It requires the normalized positive
coefficient to land below an O(1) threshold. The rough horizontal-sectional estimate `c_L = 3/8` gives
`mu_DW = 2.939 meV`, just below the conservative low edge. A value near `c_L = 0.20` gives
`mu_DW = 3.44 meV`, inside the fair alpha=1/3 frontier band.

---

## Computed vs open

| claim | grade | evidence |
|---|---|---|
| `mu_DW = rho_Lambda^(1/4) / c_L^(1/4)` and smaller `c_L` shortens the Yukawa range | **COMPUTED** | exact formula audit |
| `c_L = 1` reproduces H50's 76.7-94.0 um face-value prediction | **COMPUTED** | script reproduction |
| fair alpha=1/3 frontier corresponds to `c_L ~= 0.17-0.35` | **COMPUTED from H50's argued floor** | threshold conversion |
| the exact geometric value of `c_L` | **OPEN** | requires horizontal-sectional constant plus source-action normalization |
| whether GU-under-H36 is finally excluded or live | **OPEN** | depends on the geometric H51 value |

## H51 consequence

The next H51 computation now has a crisp target:

- If the positive normalized `c_L` comes out above about `0.35`, GU-under-H36 stays face-value excluded.
- If it lands between about `0.17` and `0.35`, the prediction is at the live frontier.
- If it lands below about `0.17`, the prediction clears the conservative fair-frontier band more robustly.

The remaining task is geometric, not phenomenological: compute the normalized positive `c_L` from the
horizontal-sectional DeWitt-Lambda constant and the source-action normalization, including the sign convention
that turns the sectional constant into a positive vacuum-energy coefficient.
