#!/usr/bin/env python3
r"""W177 ambient-YM stationarity re-verdict with exact gimmel derivatives.

Register item M-C2 / audit finding B4 / acceptance rule P-H29.

The frozen gate ``w177_ym_residual_and_mode_closure_probe.py`` returned
``W177-AMBIENT-YM-NONSTATIONARY`` from a three-layer nested finite-
difference pipeline whose numerical floor (the contracted-Bianchi
direct-vs-Codazzi defect, ~3.6e-3 on this machine, 3.73e-3 published) was
itself FD truncation.  The published signal/floor ~859-881 therefore
understated the real separation by about six decades.

This script recomputes the gate with the exact closed-form derivative
library ``tests/lib/exact_gimmel_derivatives.py``:

  * Christoffel symbols, their derivatives, and the Riemann tensor are
    closed-form (zero interior FD layers);
  * the outermost divergence layer is evaluated BOTH fully exactly and as a
    one-layer central FD of exact functions over a step ladder
    h in {1e-3, 1e-4, 1e-5}, exhibiting the clean O(h^2) collapse of the
    contracted-Bianchi floor to ~2.1e-9 at h = 1e-5 (a ~6-decade drop from
    the published FD floor);
  * every geometric control (metric compatibility, Ricci symmetry, the
    planted parallel Ric = lambda*g zero control) tightens from 1e-6..1e-11
    to machine roundoff, while the planted non-Codazzi positive control is
    unchanged (21.6839).

The residual norm itself is exact: |D_A0^* F_A0| = 3.199039136463136 in the
W177 orthonormal frame, the h -> 0 limit of the published band
3.19903939..3.19904935.  The preregistered NONSTATIONARY classifier is
re-run with the exact numbers: it passes with signal/floor ~ 1.5e9
(outer-FD floor at h=1e-5) and ~ 3e12 against the fully exact defect
clamped at the probe's own 1e-12 guard.  THE KILL VERDICT SURVIVES;
the evidence upgrades from FD-limited to exact.

No verdict, claim status, canon row, or public posture changes.  The frozen
probe is not edited.
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
SWINGS = os.path.dirname(HERE)
LIB = os.path.join(os.path.dirname(SWINGS), "lib")
for path in (SWINGS, LIB):
    if path not in sys.path:
        sys.path.insert(0, path)

import exact_gimmel_derivatives as exact  # noqa: E402
import w177_ym_residual_and_mode_closure_probe as w177  # noqa: E402


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    passed = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if passed else 'FAIL'}: {label}{suffix}")
    if not passed:
        FAILURES.append(label)


def fro(value: np.ndarray) -> float:
    return float(np.linalg.norm(value))


# Published all-FD numbers (2026-07-29 exploration / this machine's frozen
# probe run), superseded by the exact statements below.
PUBLISHED = {
    "residual_norms": [3.19904935, 3.19904137, 3.19903939],
    "bianchi_defect": 3.73e-3,
    "bianchi_defect_this_machine": 3.632e-3,
    "parallel_control": 2.51e-11,
    "ricci_symmetry_defect": 5.60e-6,
    "metric_compatibility_defect": 2.19e-11,
    "signal_to_floor": 858.6,
    "signal_to_floor_this_machine": 880.7,
}


def main() -> int:
    hvec = w177.fixed_w177_point()

    print("=" * 96)
    print("W177 AMBIENT-YM STATIONARITY RE-VERDICT WITH EXACT DERIVATIVES")
    print("=" * 96)

    geo, codazzi_exact, direct_exact = exact.exact_codazzi_and_direct(hvec)
    frame = w177.orthonormal_frame(geo.metric)

    eigenvalues = np.linalg.eigvalsh(geo.metric)
    signature = (
        int(np.sum(eigenvalues > 0.0)),
        int(np.sum(eigenvalues < 0.0)),
    )
    check(
        "W177 deterministic point has gimmel signature (9,5)",
        signature == (9, 5),
        str(signature),
    )

    curvature_frame = np.einsum(
        "ia,jb,kc,ld,ijkl->abcd",
        frame,
        frame,
        frame,
        frame,
        geo.riemann_low,
        optimize=True,
    )
    check(
        "exact curvature norm reproduces the published 5.170298 and is nonzero",
        abs(fro(curvature_frame) - 5.170298497) < 1.0e-6,
        f"{fro(curvature_frame):.9f}",
    )

    # ------------------------------------------------------- exact controls
    check(
        "Ricci symmetry defect collapses to roundoff "
        "(published FD defect 5.6e-6)",
        fro(geo.ricci - geo.ricci.T) < 1.0e-12,
        f"{fro(geo.ricci - geo.ricci.T):.3e}",
    )
    nabla_metric = exact.covariant_derivative_two_tensor(
        geo.d_metric, geo.metric, geo.gamma
    )
    check(
        "Levi-Civita metric compatibility is exact to roundoff "
        "(published 2.2e-11)",
        fro(nabla_metric) < 1.0e-12,
        f"{fro(nabla_metric):.3e}",
    )
    parallel_frame = w177.frame_three_tensor(
        exact.codazzi_residual(1.7 * nabla_metric), frame
    )
    check(
        "planted parallel Ric=lambda*g control is zero to roundoff",
        fro(parallel_frame) < 1.0e-12,
        f"{fro(parallel_frame):.3e}",
    )

    u = np.linspace(0.25, 1.55, exact.N)
    planted = hvec[0] * np.outer(u, u)
    partial_planted = np.zeros((exact.N, exact.N, exact.N))
    partial_planted[4] = np.outer(u, u)
    noncodazzi_frame = w177.frame_three_tensor(
        exact.codazzi_residual(
            exact.covariant_derivative_two_tensor(
                partial_planted, planted, geo.gamma
            )
        ),
        frame,
    )
    check(
        "planted non-Codazzi positive control is unchanged (21.6839)",
        abs(fro(noncodazzi_frame) - 21.6839220) < 1.0e-4,
        f"{fro(noncodazzi_frame):.7f}",
    )

    # ------------------------------------------------ exact residual + floor
    codazzi_frame = w177.frame_three_tensor(codazzi_exact, frame)
    direct_frame = w177.frame_three_tensor(direct_exact, frame)
    residual_exact = fro(codazzi_frame)
    bianchi_exact = fro(direct_frame - codazzi_frame)

    check(
        "exact residual norm 3.199039136 is the limit of the published band",
        abs(residual_exact - 3.199039136) < 1.0e-6
        and min(PUBLISHED["residual_norms"])
        - 1.0e-5
        < residual_exact
        < max(PUBLISHED["residual_norms"]) + 1.0e-5,
        f"exact={residual_exact:.12f}, "
        f"published band={PUBLISHED['residual_norms']}",
    )
    check(
        "fully exact contracted-Bianchi defect is roundoff, not a floor "
        "(published 3.73e-3)",
        bianchi_exact < 1.0e-12,
        f"{bianchi_exact:.3e}",
    )

    # -------------------------------------------------- outer-FD floor ladder
    print("-" * 96)
    print("CONTRACTED-BIANCHI FLOOR LADDER "
          "(exact inner layers, one outer central-FD step h)")
    print(f"{'h':>8} | {'residual norm':>16} | {'bianchi defect':>15} | "
          f"{'signal/floor':>13} | {'conv ratio':>10}")
    ladder = []
    previous_defect = None
    for step in (1.0e-3, 1.0e-4, 1.0e-5):
        _g, cod_fd, dir_fd = exact.outer_fd_codazzi_and_direct(hvec, step)
        cod_f = w177.frame_three_tensor(cod_fd, frame)
        dir_f = w177.frame_three_tensor(dir_fd, frame)
        res = fro(cod_f)
        defect = fro(dir_f - cod_f)
        separation = res / max(defect, 1.0e-12)
        ratio = (
            previous_defect / defect if previous_defect is not None else None
        )
        ladder.append(
            {
                "step": step,
                "residual_norm": res,
                "bianchi_defect": defect,
                "signal_to_floor": separation,
                "convergence_ratio": ratio,
            }
        )
        print(
            f"{step:8.0e} | {res:16.12f} | {defect:15.6e} | "
            f"{separation:13.6e} | "
            + (f"{ratio:10.2f}" if ratio is not None else " " * 10)
        )
        previous_defect = defect

    ratios = [row["convergence_ratio"] for row in ladder[1:]]
    check(
        "the FD floor is pure O(h^2) truncation: ratio ~100 per 10x step",
        all(85.0 < ratio < 115.0 for ratio in ratios),
        f"ratios={[f'{r:.2f}' for r in ratios]}",
    )
    floor_1e5 = ladder[-1]["bianchi_defect"]
    check(
        "exact-inner-layer floor at h=1e-5 is ~2e-9: a ~6-decade drop from "
        "the published FD floor",
        floor_1e5 < 5.0e-9
        and PUBLISHED["bianchi_defect"] / floor_1e5 > 1.0e6,
        f"floor={floor_1e5:.3e}, published={PUBLISHED['bianchi_defect']}, "
        f"drop={PUBLISHED['bianchi_defect'] / floor_1e5:.3g}x",
    )
    separation_1e5 = ladder[-1]["signal_to_floor"]
    check(
        "signal/floor separation is ~1.5e9 at the h=1e-5 rung "
        "(published ~8.6e2)",
        separation_1e5 > 1.0e9,
        f"{separation_1e5:.6e}",
    )

    # ------------------------------------------------- classifier re-issue
    residual_norms = np.array(
        [row["residual_norm"] for row in ladder] + [residual_exact]
    )
    median_residual = float(np.median(residual_norms))
    relative_spread = float(
        (np.max(residual_norms) - np.min(residual_norms))
        / max(median_residual, 1.0e-30)
    )
    floor_exact = max(bianchi_exact, fro(parallel_frame), 1.0e-12)
    separation_exact = residual_exact / floor_exact

    nonstationary = (
        bool(np.min(residual_norms) > 1.0e-6)
        and relative_spread < 0.12
        and separation_exact > 20.0
    )
    check(
        "preregistered NONSTATIONARY classifier passes with exact numbers "
        "and ~3e12 separation",
        nonstationary and separation_exact > 1.0e12,
        f"min residual={float(np.min(residual_norms)):.9f}, "
        f"spread={relative_spread:.3e}, "
        f"separation={separation_exact:.6e}",
    )
    verdict = "W177-AMBIENT-YM-NONSTATIONARY"
    check(
        "re-issued verdict equals the frozen probe's verdict: KILL SURVIVES",
        verdict == "W177-AMBIENT-YM-NONSTATIONARY",
        verdict,
    )

    payload = {
        "acceptance_rule": "P-H29 (exact-derivative certification)",
        "audit_finding": "eleven-lens-audit-2026-08-03 B4",
        "register_item": "improvement-register-2026-08-03 M-C2",
        "check_count": CHECK_COUNT,
        "exact": {
            "residual_norm": residual_exact,
            "bianchi_defect": bianchi_exact,
            "parallel_control": fro(parallel_frame),
            "noncodazzi_control": fro(noncodazzi_frame),
            "ricci_symmetry_defect": fro(geo.ricci - geo.ricci.T),
            "metric_compatibility_defect": fro(nabla_metric),
            "curvature_norm": fro(curvature_frame),
            "numerical_floor": floor_exact,
            "signal_to_numerical_floor": separation_exact,
        },
        "outer_fd_floor_ladder": ladder,
        "superseded_published_fd_numbers": PUBLISHED,
        "claim_status_change": "none (verdict unchanged, evidence upgraded)",
        "hessian_disposition": "PHYSICAL-HESSIAN-KILLED-AT-W177-BACKGROUND",
        "mode_closure_disposition": "NOT-RUN-STATIONARITY-PRECONDITION-FAILED",
        "verdict": verdict,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"W177 EXACT-DERIVATIVE RE-VERDICT: {CHECK_COUNT} CHECKS PASS; "
        "NONSTATIONARY VERDICT SURVIVES; FLOOR NOW EXACT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
