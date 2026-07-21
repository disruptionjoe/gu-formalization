#!/usr/bin/env python3
"""T-D1/T-D2 deterministic null-stratum measure-pressure probe.

Reuses the committed Prong-0 end construction, then varies only the probability
law used to sample genuine flat-end directions. All covariance matrices remain
positive definite, so every ensemble has full support on direction space.

The printed findings, not process exit, are the scientific result.
"""
from __future__ import annotations

import os
import runpy

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
PRONG0 = os.path.join(HERE, "oracle_relative_prong0_measure_lemma_probe.py")
ns = runpy.run_path(PRONG0)

ray = ns["ray"]
xi_safe = ns["xi_safe"]
PT = ns["PT"]
boost03 = ns["boost03"]
dewitt_gram = ns["dewitt_gram"]
g_of_ray = ns["g_of_ray"]


def crossing_fraction(*, time_scale: float, radius: float, seed: int,
                      n: int = 800, boosts: bool = True) -> tuple[int, int]:
    """Return (q<0 count, valid count) for a full-support Gaussian direction law."""
    rng = np.random.default_rng(seed)
    crossed = 0
    valid = 0
    for _ in range(n):
        alpha = rng.standard_normal(4)
        alpha[3] *= time_scale
        alpha /= np.linalg.norm(alpha)
        pre = boost03(rng.uniform(-1.5, 1.5)) if boosts and rng.random() < 0.5 else None
        xi = xi_safe(0.0, ray(alpha, radius), pre=pre)
        if xi is None:
            continue
        valid += 1
        p, t = PT(xi)
        crossed += int(p - t < 0.0)
    return crossed, valid


def volume_slope(alpha: np.ndarray, s0: float = 2.0, s1: float = 3.0) -> float:
    """Finite-difference slope of log sqrt|det G| along a genuine flat ray."""
    vals = []
    for s in (s0, s1):
        det = abs(np.linalg.det(dewitt_gram(g_of_ray(alpha, s))))
        vals.append(0.5 * np.log(det))
    return float((vals[1] - vals[0]) / (s1 - s0))


print("\n" + "=" * 74)
print("T-D1 / T-D2 -- NULL-STRATUM FRACTION INVARIANCE PRESSURE")
print("=" * 74)

scales = [0.35, 1.0, 3.0]
radii = [3.0, 5.0, 7.0]
rows: list[tuple[float, float, float, int]] = []
for i, scale in enumerate(scales):
    for j, radius in enumerate(radii):
        crossed, valid = crossing_fraction(
            time_scale=scale,
            radius=radius,
            seed=2026072100 + 10 * i + j,
        )
        fraction = crossed / valid
        rows.append((scale, radius, fraction, valid))
        print(f"[fraction] time_scale={scale:>4.2f} radius={radius:.0f} "
              f"q<0={crossed:>3}/{valid:<3} = {100*fraction:>5.1f}%")

fractions = np.array([row[2] for row in rows])
baseline = [row[2] for row in rows if row[0] == 1.0 and row[1] == 5.0][0]
spread = float(fractions.max() - fractions.min())
positive_rows = int(np.sum(fractions > 0.0))

print(f"\n[summary] original-style baseline (scale=1,radius=5): "
      f"{100*baseline:.1f}%")
print(f"[summary] declared full-support ensemble range: "
      f"{100*fractions.min():.1f}% .. {100*fractions.max():.1f}% "
      f"(spread {100*spread:.1f} percentage points)")
print(f"[summary] positive q<0 fraction in {positive_rows}/{len(rows)} rows")

# The native DeWitt density is a radial volume, not automatically a normalized
# probability law on the noncompact end-direction space. Opposite genuine rays
# already show opposite radial volume behavior, defeating a finite invariant
# probability interpretation without a cutoff/weight prescription.
alpha_up = np.array([1.0, 1.0, 1.0, 1.0]) / 2.0
alpha_down = -alpha_up
slope_up = volume_slope(alpha_up)
slope_down = volume_slope(alpha_down)
print(f"\n[volume] d/ds log sqrt|det G| conf-up   = {slope_up:+.3f}")
print(f"[volume] d/ds log sqrt|det G| conf-down = {slope_down:+.3f}")
print("[volume] opposite radial behavior means the native noncompact volume does")
print("         not itself select a finite probability distribution over ends;")
print("         a cutoff or direction weight is additional data.")

print("\nVERDICT T-D1:", "SURVIVES-QUALITATIVELY" if positive_rows else "FIRES-0-PERCENT")
print("VERDICT T-D2:", "D2-SAMPLER-DEPENDENT" if spread > 0.05 else "D2-UNDERPOWERED")
print("T-D3 is not computed here: it requires an independently defined concurrency")
print("predicate/map and common measure; defining concurrency=q<0 is a planted equality.")
