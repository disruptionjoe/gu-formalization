#!/usr/bin/env python3
"""DE-14: official DES Dovekie pure-supernova-shape likelihood replay.

The two official release files are external inputs and are not vendored.  Pass
their directory with --data-dir.  The script verifies exact SHA-256 digests,
unpacks the released inverse covariance, analytically marginalizes the additive
absolute-magnitude/H0 offset, and compares the existing GU M2=8, f0=0.125
background with flat-LCDM controls.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import minimize_scalar


DATA_SHA256 = {
    "DES-Dovekie_HD.csv": "2f57019d783eaa976df80a41b0054171a2d994ee9808d715ce850c2df5720aaf",
    "STAT+SYS.npz": "ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b",
}
RELEASE_COMMIT = "c9a4fcafc4cbd19bd750dee47fc76194a45c181f"
EXPECTED = {
    "n": 1820,
    "lcdm_planck": 1632.45156,
    "lcdm_same_om": 1633.35213,
    "lcdm_best_om": 0.3303173,
    "lcdm_best": 1631.42056,
    "gu_h": 0.6374932,
    "gu_om": 0.3518722,
    "gu": 1652.55789,
    "delta_same_om": 19.20577,
    "delta_best": 21.13734,
}

FAILURES: list[str] = []
CHECKS = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(("PASS: " if condition else "FAIL: ") + label + ((" -- " + detail) if detail else ""))
    if not condition:
        FAILURES.append(label)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def parse_release(data_dir: Path):
    hd = data_dir / "DES-Dovekie_HD.csv"
    packed_path = data_dir / "STAT+SYS.npz"
    for path in (hd, packed_path):
        check(f"official input digest {path.name}", digest(path) == DATA_SHA256[path.name])

    rows = []
    for line in hd.read_text(encoding="utf-8").splitlines():
        if line.startswith("SN:"):
            parts = line.split()
            rows.append((float(parts[3]), float(parts[4]), float(parts[5])))
    z_cmb = np.array([row[0] for row in rows])
    z_hel = np.array([row[1] for row in rows])
    mu_obs = np.array([row[2] for row in rows])

    packed = np.load(packed_path)
    n = int(packed[packed.files[0]][0])
    precision = np.zeros((n, n))
    precision[np.triu_indices(n)] = packed[packed.files[1]]
    lower = np.tril_indices(n, -1)
    precision[lower] = precision.T[lower]
    check("release has 1820 supernovae", n == len(rows) == EXPECTED["n"])
    check("released precision matrix is symmetric", np.max(np.abs(precision - precision.T)) == 0.0)
    return z_cmb, z_hel, mu_obs, precision


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--selftest", "--self-test", action="store_true")
    args = parser.parse_args()

    z_cmb, z_hel, mu_obs, precision = parse_release(args.data_dir)
    n = len(mu_obs)
    ones = np.ones(n)
    c_norm = float(ones @ precision @ ones)
    check("offset-normalization quadratic form is positive", c_norm > 0)

    def chi2_marg(mu_model: np.ndarray) -> float:
        delta = np.asarray(mu_model) - mu_obs
        raw = float(delta @ precision @ delta)
        b = float(ones @ precision @ delta)
        return raw - b * b / c_norm

    def mu_from_grid(z_grid: np.ndarray, e_grid: np.ndarray) -> np.ndarray:
        order = np.argsort(z_grid)
        z = np.asarray(z_grid)[order]
        e = np.asarray(e_grid)[order]
        if z[0] > 0:
            z = np.r_[0.0, z]
            e = np.r_[1.0, e]
        dc = cumulative_trapezoid(1.0 / e, z, initial=0.0)
        da = np.interp(z_cmb, z, dc) / (1.0 + z_cmb)
        return 5.0 * np.log10((1.0 + z_cmb) * (1.0 + z_hel) * da) + 25.0

    def lcdm(omega_m: float) -> float:
        z = np.linspace(0.0, max(1.5, float(z_cmb.max()) + 0.02), 5000)
        e = np.sqrt(omega_m * (1.0 + z) ** 3 + 1.0 - omega_m)
        return chi2_marg(mu_from_grid(z, e))

    best = minimize_scalar(lcdm, bounds=(0.1, 0.6), method="bounded", options={"xatol": 1e-10})
    check("flat-LCDM Planck-Om regression", abs(lcdm(0.315) - EXPECTED["lcdm_planck"]) < 0.02)
    check("flat-LCDM best Om regression", abs(best.x - EXPECTED["lcdm_best_om"]) < 2e-5)
    check("flat-LCDM best chi2 regression", abs(best.fun - EXPECTED["lcdm_best"]) < 0.02)

    repo = Path(__file__).resolve().parents[2]
    h46c = load_module(repo / "tests/wave46/H46C_theta_star_cmb_calibration.py", "de14_h46c")
    h_raw = h46c.calibrate_h(h46c.F0_CANON)
    h_lcdm = h46c.calibrate_h(1e-10)
    h_gu = h_raw * (h46c.H_PLANCK / h_lcdm)
    omega_m_gu = h46c.OMH2 / h_gu**2
    background, _ = h46c._gu_background(h_gu, h46c.F0_CANON, npts=3000, n_iter=80)
    h46c._restore_module_cosmology()
    order = np.argsort(background["z"])
    chi_gu = chi2_marg(mu_from_grid(background["z"][order], np.sqrt(background["H2"][order])))
    chi_same_om = lcdm(omega_m_gu)
    delta_same = chi_gu - chi_same_om
    delta_best = chi_gu - best.fun

    check("GU calibrated h regression", abs(h_gu - EXPECTED["gu_h"]) < 2e-5)
    check("GU calibrated Om regression", abs(omega_m_gu - EXPECTED["gu_om"]) < 2e-5)
    check("GU pure-shape chi2 regression", abs(chi_gu - EXPECTED["gu"]) < 0.03)
    check("same-Om LCDM control is reproduced", abs(chi_same_om - EXPECTED["lcdm_same_om"]) < 0.03)
    check("GU is penalized by about 19.2 against same-Om LCDM", abs(delta_same - EXPECTED["delta_same_om"]) < 0.05)
    check("GU is penalized by about 21.1 against best flat LCDM", abs(delta_best - EXPECTED["delta_best"]) < 0.05)

    # Absolute magnitude/H0 is a nuisance offset.  The analytic formula must
    # be invariant under adding an arbitrary constant to every model modulus.
    mu_guard = np.linspace(35.0, 44.0, n)
    check("analytic M-offset marginalization is shift invariant", abs(chi2_marg(mu_guard + 3.7) - chi2_marg(mu_guard)) < 1e-7)

    if args.selftest:
        raw_delta = mu_guard - mu_obs
        raw0 = float(raw_delta @ precision @ raw_delta)
        raw_shift = float((raw_delta + 3.7) @ precision @ (raw_delta + 3.7))
        mutations = [
            ("omit absolute-magnitude marginalization", abs(raw_shift - raw0) > 1.0),
            ("read supernovae as an H0 measurement", abs(chi2_marg(mu_guard + 3.7) - chi2_marg(mu_guard)) < 1e-7),
            ("claim GU beats same-Om LCDM", delta_same > 0),
            ("claim current data erase the shape penalty", delta_best > 10),
        ]
        caught = 0
        for label, detected in mutations:
            check("selftest catches " + label, detected)
            caught += int(detected)
        print(f"selftest mutations caught: {caught}/{len(mutations)}")

    print(f"release commit: {RELEASE_COMMIT}")
    print(f"LCDM best: Om={best.x:.7f}, chi2_Mmarg={best.fun:.5f}")
    print(f"GU: h={h_gu:.7f}, Om={omega_m_gu:.7f}, chi2_Mmarg={chi_gu:.5f}")
    print(f"RESULT: delta_chi2_same_Om={delta_same:+.5f}; delta_chi2_best_LCDM={delta_best:+.5f}")
    print("This is a supernova pure-shape comparator, not an H0 measurement and not a GU source-action verdict.")
    if FAILURES:
        print("FAILED:", FAILURES)
        raise SystemExit(1)
    print(f"checks passed: {CHECKS}/{CHECKS}")


if __name__ == "__main__":
    main()
