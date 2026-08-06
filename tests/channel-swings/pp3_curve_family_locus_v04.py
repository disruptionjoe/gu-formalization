#!/usr/bin/env python3
"""Emit and verify the PP3 v0.4 three-branch dark-energy prediction.

The registered object is the union of three one-parameter curves, one for each
unresolved program-native mass assignment M^2/H0^2 in {3, 7, 8}.  The script
uses the standard flat-FLRW canonical-scalar truncation implemented by
``de_amplitude_audit_probe.py``.  It never evaluates a likelihood.

The projection is frozen independently of a survey covariance: x = 1-a,
z in [0, 2.33], and 512 samples uniform in x.  The standard CPL coefficients
come from the linear fit w(x) = w0 + wa*x.  Curvature wb is then the leading
quadratic coefficient of that fit's residual; it is not allowed to redefine
the CPL slope.  ``--output-dir`` writes machine-readable CSV and JSON receipts.
Exit zero requires all structural and resolution checks.

Run:
  python tests/channel-swings/pp3_curve_family_locus_v04.py
  python tests/channel-swings/pp3_curve_family_locus_v04.py --output-dir DIR
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import de_amplitude_audit_probe as de  # noqa: E402

Z_MAX = 2.33
N_PROJECTION = 512
M2_BAND = (3.0, 7.0, 8.0)
F0_LIMITS = {3.0: 0.2076, 7.0: 0.0389, 8.0: 0.0274}
F0_CPL_MATCH = {3.0: 1.628, 7.0: 0.228, 8.0: 0.174}
BASE_NODES = (0.0001, 0.0005, 0.001, 0.002, 0.005, 0.010, 0.015, 0.020)
RESULTS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, ok: bool, detail: str = "") -> bool:
    RESULTS.append((tag, name, bool(ok)))
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
          + (f"   ({detail})" if detail else ""), flush=True)
    return bool(ok)


def f0_nodes(m2: float) -> list[float]:
    endpoint = 1.10 * max(0.125, F0_LIMITS[m2], F0_CPL_MATCH[m2])
    values = set(BASE_NODES)
    values.update((F0_LIMITS[m2], 0.125, F0_CPL_MATCH[m2], endpoint))
    return sorted(v for v in values if v <= endpoint + 1e-12)


def calibrated_h(m2: float, f0: float, npts: int) -> float:
    """Own-theta-star calibration with a bracket wide enough for stress nodes."""
    return de.calibrate(f0, treatment="B", M2=m2, npts=npts,
                        lo=0.45, hi=1.50)


def cumulative_trapezoid(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    out = np.zeros_like(x)
    out[1:] = np.cumsum(0.5 * np.diff(x) * (y[1:] + y[:-1]))
    return out


def family_point(m2: float, f0: float, npts: int = 700) -> dict:
    h = calibrated_h(m2, f0, npts)
    om = de.OMH2 / h**2
    orad = de.OMEGA_R_H2 / h**2
    bg = de.solve_bg(m2, f0, om, Or=orad, npts=npts)
    order = np.argsort(bg["z"])
    z_native = bg["z"][order]
    w_native = de.w_de(bg)[order]
    e_native = np.sqrt(bg["H2"][order])

    x_max = Z_MAX / (1.0 + Z_MAX)
    x = np.linspace(0.0, x_max, N_PROJECTION)
    z = x / (1.0 - x)
    w = np.interp(z, z_native, w_native)
    design = np.column_stack((np.ones_like(x), x))
    w0, wa = (float(v) for v in np.linalg.lstsq(design, w, rcond=None)[0])
    residual = w - (w0 + wa * x)
    quadratic = x**2 - np.mean(x**2)
    wb = float(np.linalg.lstsq(quadratic.reshape(-1, 1), residual,
                               rcond=None)[0][0])
    denom = w0 + 1.0

    z_obs = np.linspace(0.0, Z_MAX, 65)
    e_obs = np.interp(z_obs, z_native, e_native)
    integral = cumulative_trapezoid(1.0 / e_obs, z_obs)
    amp = de.C_KMS / (100.0 * h * de.RD)
    dm_rd = amp * integral
    dh_rd = amp / e_obs

    return {
        "M2": m2,
        "f0": f0,
        "h": h,
        "w0": w0,
        "wa": wa,
        "wb": wb,
        "R": wa / denom,
        "S2": wb / denom,
        "min_wp1": float(np.min(w_native + 1.0)),
        "max_dev": float(np.max(np.abs(w_native + 1.0))),
        "z": z_obs,
        "dm_rd": dm_rd,
        "dh_rd": dh_rd,
    }


def relative_max(a: np.ndarray, b: np.ndarray) -> float:
    mask = np.maximum(np.abs(a), np.abs(b)) > 1e-12
    return float(np.max(np.abs(a[mask] - b[mask])
                        / np.maximum(np.abs(a[mask]), np.abs(b[mask]))))


def write_outputs(outdir: Path, points: list[dict], summary: dict) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    with (outdir / "pp3-v0.4-locus.csv").open("w", newline="") as fh:
        fields = ("M2", "f0", "h", "w0", "wa", "wb", "R", "S2",
                  "min_wp1", "max_dev", "calibration_segment")
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for p in points:
            row = {k: p[k] for k in fields[:-1]}
            row["calibration_segment"] = p["f0"] <= F0_LIMITS[p["M2"]] + 1e-12
            writer.writerow(row)
    with (outdir / "pp3-v0.4-observables.csv").open("w", newline="") as fh:
        fields = ("M2", "f0", "z", "DM_over_rd", "DH_over_rd")
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for p in points:
            for z, dm, dh in zip(p["z"], p["dm_rd"], p["dh_rd"]):
                writer.writerow({"M2": p["M2"], "f0": p["f0"], "z": z,
                                 "DM_over_rd": dm, "DH_over_rd": dh})
    with (outdir / "pp3-v0.4-summary.json").open("w") as fh:
        json.dump(summary, fh, indent=2, sort_keys=True)
        fh.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    print("computing PP3 v0.4: three branches, fixed CPL + residual projection")
    points = [family_point(m2, f0) for m2 in M2_BAND for f0 in f0_nodes(m2)]
    by_branch = {m2: [p for p in points if p["M2"] == m2] for m2 in M2_BAND}

    calibration_ends = {
        m2: family_point(m2, F0_LIMITS[m2]) for m2 in M2_BAND
    }
    print("\nCALIBRATION-SEGMENT ENDPOINTS (fixed CPL + residual projection):")
    print(f"{'M^2':>5} {'f0':>8} {'w0+1':>10} {'wa':>10} {'R':>10} {'S2':>10}")
    for m2, p in calibration_ends.items():
        print(f"{m2:5.0f} {p['f0']:8.4f} {p['w0'] + 1:10.5f} "
              f"{p['wa']:10.5f} {p['R']:10.4f} {p['S2']:10.4f}")

    check("T", "mimic calibration returns the imported Planck point",
          all(abs(by_branch[m2][0]["h"] - de.H_PLANCK) < 0.004
              for m2 in M2_BAND))
    check("E", "all computed points are pointwise non-phantom",
          all(p["min_wp1"] > -2e-12 for p in points))
    check("E", "w0+1 is monotone along every branch",
          all(np.all(np.diff([p["w0"] + 1 for p in by_branch[m2]]) > 0)
              for m2 in M2_BAND))
    check("E", "R and S2 are finite on the full extended grid",
          all(np.isfinite(p["R"]) and np.isfinite(p["S2"]) for p in points))
    check("E", "the three calibration ceilings are branch-specific",
          calibration_ends[3.0]["w0"] > calibration_ends[7.0]["w0"]
          > calibration_ends[8.0]["w0"])

    convergence = []
    for m2 in M2_BAND:
        for f0 in f0_nodes(m2):
            coarse = next(p for p in by_branch[m2] if p["f0"] == f0)
            fine = family_point(m2, f0, npts=1400)
            convergence.append({
                "dw0": abs(coarse["w0"] - fine["w0"]),
                "dwa": abs(coarse["wa"] - fine["wa"]),
                "dR": abs(coarse["R"] - fine["R"]),
                "dS2": abs(coarse["S2"] - fine["S2"]),
                "dDM": relative_max(coarse["dm_rd"], fine["dm_rd"]),
                "dDH": relative_max(coarse["dh_rd"], fine["dh_rd"]),
            })
    maxima = {key: max(c[key] for c in convergence) for key in convergence[0]}
    check("V", "resolution doubling meets the frozen numerical tolerances",
          maxima["dw0"] < 5e-4 and maxima["dwa"] < 5e-4
          and maxima["dR"] < 5e-3 and maxima["dS2"] < 5e-3
          and maxima["dDM"] < 1e-4 and maxima["dDH"] < 1e-4,
          ", ".join(f"{k}={v:.2e}" for k, v in maxima.items()))

    summary = {
        "package": "PP3", "version": "0.4", "projection": {
            "x": "1-a", "z_range": [0.0, Z_MAX],
            "samples_uniform_in_x": N_PROJECTION,
            "fit": "linear CPL w(x)=w0+wa*x; wb from quadratic residual",
        },
        "masses_M2_over_H0_squared": list(M2_BAND),
        "f0_calibration_limits": {str(int(k)): v for k, v in F0_LIMITS.items()},
        "f0_extended_endpoints": {str(int(m2)): f0_nodes(m2)[-1]
                                  for m2 in M2_BAND},
        "calibration_endpoints": {
            str(int(m2)): {k: calibration_ends[m2][k]
                           for k in ("f0", "w0", "wa", "wb", "R", "S2")}
            for m2 in M2_BAND
        },
        "resolution_doubling_maxima": maxima,
        "checks": [{"tag": t, "name": n, "pass": ok}
                   for t, n, ok in RESULTS],
    }
    if args.output_dir:
        write_outputs(args.output_dir, points, summary)
        print(f"wrote receipts to {args.output_dir}")

    all_ok = all(ok for _tag, _name, ok in RESULTS)
    print(f"\nHEADLINE: {sum(t == 'E' for t, _n, _o in RESULTS)} [E] + "
          f"{sum(t == 'V' for t, _n, _o in RESULTS)} [V]; "
          f"setup [T]={sum(t == 'T' for t, _n, _o in RESULTS)}; "
          f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
