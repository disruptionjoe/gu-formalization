#!/usr/bin/env python3
r"""RB7 Track-A re-verdict with exact gimmel derivatives (M-C2 / B4 / P-H29).

The frozen probe ``rb7_stationary_nonmetric_order_parameter_probe.py`` read
its Track-A vertical-response kill inside a three-layer nested finite-
difference pipeline.  Eleven-lens-audit finding B4 and register item M-C2
identified the published Track-A numbers as FD artifacts of that pipeline:

  * the vertical connection-form residual 0.00361491 is s^-3 roundoff of a
    quantity that is exactly zero (and does not reproduce across machines
    past two digits: this machine's frozen probe prints 0.00355180);
  * the signal/floor ratio 0.9702 is a ratio of two noise norms; and
  * the mixed Gram is exactly (9/32)(I + T_tr), a stronger statement than
    the published least-squares fit with residual 4.13e-7.

This script re-derives Track A with the exact closed-form derivative library
``tests/lib/exact_gimmel_derivatives.py`` (the P-H29 acceptance mechanism)
and certifies:

  1. the vertical connection-form residual is structurally ZERO: the fully
     exact evaluation (no FD layer anywhere) gives |vertical| ~ 1e-14
     against a full residual norm 3.19903914;
  2. under exact inner layers with one outer FD step h, the vertical
     residual converges to zero as clean O(h^2) -- the ratio-100 table;
  3. the kill-gate separation is signal/floor = 0.7401 at every outer step
     (three decades), robustly below the frozen probe's 1.1 kill line: the
     KILL VERDICT SURVIVES and is now scale-robust instead of scale-noisy;
  4. the mixed signal Gram equals (9/32)(I + T_tr) = (9/16) P_traceless to
     machine precision (relative residual ~ 2e-15), with lstsq coefficients
     equal to the exact rational 9/32.

Two of the frozen probe's preregistered Track-A controls asserted properties
of the FD noise itself ("vertical residual is nonzero numerically" > 1e-6;
"vertical residual is scale-unstable" spread > 1).  Register M-C2 predicted
those predicates break under any better numerics; this script demonstrates
it (the exact vertical norm is ~1e-14 and the exact-inner-layer ladder is
perfectly scale-stable) and records the supersession explicitly.

Track B of RB7 (the homogeneous su(2) stationary classification) was already
exact and is untouched here.  No verdict changes: the Track-A kill and the
mixed-Gram nonselector verdict stand; only their evidence grade moves from
CONTROLLED LOCAL NUMERICS to EXACT.  The frozen probe is not edited.
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


def inertia(matrix: np.ndarray, tolerance: float = 3.0e-7) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.T))
    scale = max(1.0, float(np.max(np.abs(values))))
    cut = tolerance * scale
    return (
        int(np.sum(values > cut)),
        int(np.sum(values < -cut)),
        int(np.sum(np.abs(values) <= cut)),
    )


def signed_frame(metric: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Identical to the frozen RB7 probe's adapted signed frame."""
    values, vectors = np.linalg.eigh(0.5 * (metric + metric.T))
    order = np.concatenate(
        [np.flatnonzero(values > 0.0), np.flatnonzero(values < 0.0)]
    )
    signed_values = values[order]
    frame = vectors[:, order] / np.sqrt(np.abs(signed_values))
    return frame, np.diag(np.sign(signed_values))


def trace_involution(base_metric: np.ndarray) -> np.ndarray:
    """T_tr = I - 2 P_trace in fibre coordinates (frozen RB7 convention)."""
    inverse = np.linalg.inv(base_metric)
    trace_covector = np.array(
        [float(np.trace(inverse @ element)) for element in exact.EBASIS]
    )
    metric_components = exact.comps_of(base_metric)
    projector = 0.25 * np.outer(metric_components, trace_covector)
    return np.eye(10) - 2.0 * projector


def metric_adjoint(matrix: np.ndarray, metric: np.ndarray) -> np.ndarray:
    return np.linalg.solve(metric, matrix.T @ metric)


def adapt(tensor: np.ndarray, adapted: np.ndarray) -> np.ndarray:
    return np.einsum(
        "ma,jb,lc,mjl->abc", adapted, adapted, adapted, tensor, optimize=True
    )


# Published (2026-07-30 exploration) all-FD Track-A numbers, superseded here.
PUBLISHED = {
    "full_residual_central": 3.19904137,
    "vertical_residual_central": 0.00361491,
    "vertical_discrepancy_central": 0.00372577,
    "signal_to_floor_central": 0.9702446,
    "mixed_fit_residual": 4.1281e-7,
}


def main() -> int:
    hvec = w177.fixed_w177_point()

    print("=" * 96)
    print("RB7 TRACK-A RE-VERDICT WITH EXACT GIMMEL DERIVATIVES")
    print("=" * 96)

    # ---------------------------------------------------------------- exact
    geo, codazzi, direct = exact.exact_codazzi_and_direct(hvec)
    base_frame, eta4 = signed_frame(geo.metric[:4, :4])
    vertical_frame, eta10 = signed_frame(geo.metric[4:, 4:])
    adapted = np.zeros((14, 14))
    adapted[:4, :4] = base_frame
    adapted[4:, 4:] = vertical_frame

    residual = adapt(codazzi, adapted)
    direct_adapted = adapt(direct, adapted)
    full_norm = fro(residual)
    vertical_norm = fro(residual[:, :, 4:])
    vertical_direct_norm = fro(direct_adapted[:, :, 4:])
    discrepancy_norm = fro(direct_adapted - residual)

    check(
        "adapted base and vertical frames reproduce signatures (3,1) and (6,4)",
        inertia(eta4) == (3, 1, 0) and inertia(eta10) == (6, 4, 0),
    )
    check(
        "exact residual is antisymmetric in its adjoint pair to roundoff",
        fro(residual + residual.swapaxes(0, 1)) < 1.0e-12,
        f"{fro(residual + residual.swapaxes(0, 1)):.3e}",
    )
    check(
        "exact full residual norm is the limit of the published stable band",
        abs(full_norm - PUBLISHED["full_residual_central"]) < 1.0e-5,
        f"exact={full_norm:.9f}, published central="
        f"{PUBLISHED['full_residual_central']}",
    )
    check(
        "VERTICAL residual is exactly zero: |vertical| < 1e-12 (got ~1e-14)",
        vertical_norm < 1.0e-12,
        f"|vertical|={vertical_norm:.3e} against full {full_norm:.6f}; "
        f"published FD value {PUBLISHED['vertical_residual_central']} superseded",
    )
    check(
        "vertical direct-divergence block is likewise zero",
        vertical_direct_norm < 1.0e-12,
        f"{vertical_direct_norm:.3e}",
    )
    check(
        "exact contracted-Bianchi discrepancy vanishes to roundoff",
        discrepancy_norm < 1.0e-12,
        f"|direct-codazzi|={discrepancy_norm:.3e}; published floor "
        f"{PUBLISHED['vertical_discrepancy_central']} was FD truncation",
    )

    # -------------------------------------------------- outer-FD ratio table
    print("-" * 96)
    print("O(h^2) CONVERGENCE OF THE VERTICAL RESIDUAL "
          "(exact inner layers, one outer central-FD step h)")
    print(f"{'h':>8} | {'|vertical|':>14} | {'|vert disc|':>14} | "
          f"{'signal/floor':>12} | {'conv ratio':>10}")
    steps = (1.0e-2, 1.0e-3, 1.0e-4)
    ladder = []
    previous = None
    for step in steps:
        _geo, cod_fd, dir_fd = exact.outer_fd_codazzi_and_direct(hvec, step)
        res_fd = adapt(cod_fd, adapted)
        dir_ad = adapt(dir_fd, adapted)
        vert = fro(res_fd[:, :, 4:])
        disc = fro((dir_ad - res_fd)[:, :, 4:])
        separation = vert / max(disc, 1.0e-30)
        ratio = (previous[0] / vert) if previous is not None else float("nan")
        ladder.append(
            {
                "step": step,
                "vertical_norm": vert,
                "vertical_discrepancy_norm": disc,
                "signal_to_floor": separation,
                "convergence_ratio": None if previous is None else ratio,
            }
        )
        print(
            f"{step:8.0e} | {vert:14.6e} | {disc:14.6e} | "
            f"{separation:12.4f} | "
            + (f"{ratio:10.2f}" if previous is not None else " " * 10)
        )
        previous = (vert, disc)

    ratios = [row["convergence_ratio"] for row in ladder[1:]]
    check(
        "vertical residual converges to ZERO at clean O(h^2): ratio ~100 per 10x",
        all(90.0 < ratio < 110.0 for ratio in ratios),
        f"ratios={[f'{r:.2f}' for r in ratios]}",
    )
    separations = [row["signal_to_floor"] for row in ladder]
    check(
        "kill gate SURVIVES with exact derivatives: signal/floor < 1.1 at "
        "every step",
        all(sep < 1.1 for sep in separations),
        f"separations={[f'{s:.4f}' for s in separations]}",
    )
    check(
        "exact-derivative separation is scale-ROBUST at 0.740 "
        "(supersedes the published noise ratio 0.9702)",
        max(separations) - min(separations) < 1.0e-2
        and abs(separations[1] - 0.7401) < 5.0e-3,
        f"published={PUBLISHED['signal_to_floor_central']}, "
        f"exact central={separations[1]:.4f}",
    )
    # M-C2 predicted the two frozen noise-property controls break under
    # better numerics; record the demonstration rather than inheriting them.
    spread = (max(r["vertical_norm"] for r in ladder[:2])
              / max(min(r["vertical_norm"] for r in ladder[:2]), 1.0e-30))
    check(
        "frozen probe's 'vertical residual nonzero (>1e-6)' control predicate "
        "is FALSE in the exact pipeline, as register M-C2 predicted",
        vertical_norm < 1.0e-6,
        f"exact |vertical|={vertical_norm:.3e}",
    )
    check(
        "frozen probe's 'scale-unstable' spread was pure FD noise: the "
        "exact-inner-layer ladder is a deterministic O(h^2) line",
        90.0 < spread < 110.0,
        "spread across one decade of h is exactly the truncation ratio",
    )

    # ------------------------------------------------------------ mixed Gram
    print("-" * 96)
    print("MIXED SIGNAL GRAM: EXACT RATIONAL IDENTITY")
    mixed = residual[:4, 4:, :4]
    mixed_b = np.einsum(
        "aib,cjd,ac,bd->ij", mixed, mixed, eta4, eta4, optimize=True
    )
    mixed_h = eta10 @ mixed_b
    involution_frame = np.linalg.solve(
        vertical_frame, trace_involution(exact.vmat(hvec)) @ vertical_frame
    )
    target = (9.0 / 32.0) * (np.eye(10) + involution_frame)
    identity_residual = fro(mixed_h - target) / fro(mixed_h)
    fit_columns = np.column_stack(
        [np.eye(10).reshape(-1), involution_frame.reshape(-1)]
    )
    coefficients, *_ = np.linalg.lstsq(
        fit_columns, mixed_h.reshape(-1), rcond=None
    )
    commutator = mixed_h @ involution_frame - involution_frame @ mixed_h

    check(
        "mixed Gram equals EXACTLY (9/32)(I + T_tr) [ = (9/16) P_traceless ]",
        identity_residual < 1.0e-12,
        f"relative residual={identity_residual:.3e}; published fit residual "
        f"{PUBLISHED['mixed_fit_residual']} superseded",
    )
    check(
        "lstsq coefficients equal the exact rational 9/32 to 1e-12",
        float(np.max(np.abs(coefficients - 9.0 / 32.0))) < 1.0e-12,
        f"coefficients={coefficients.tolist()}, 9/32={9.0 / 32.0}",
    )
    check(
        "mixed Gram is DeWitt-self-adjoint to roundoff",
        fro(metric_adjoint(mixed_h, eta10) - mixed_h) < 1.0e-12,
        f"{fro(metric_adjoint(mixed_h, eta10) - mixed_h):.3e}",
    )
    check(
        "mixed Gram commutes with the trace involution to roundoff "
        "(no nonzero commutator: exact, not floor-limited)",
        fro(commutator) < 1.0e-12,
        f"{fro(commutator):.3e}",
    )
    check(
        "sqrt(2) * |mixed block| equals the full residual norm to roundoff",
        abs(np.sqrt(2.0) * fro(mixed) - full_norm) < 1.0e-12,
        f"sqrt2*mixed={np.sqrt(2.0) * fro(mixed):.15f}, full={full_norm:.15f}",
    )

    verdict = (
        "RB7-TRACK-A-KILL-SURVIVES-EXACT: vertical response is structurally "
        "zero (not merely below an FD floor); mixed Gram is exactly "
        "(9/32)(I+T_tr), a 1+9 nonselector"
    )
    payload = {
        "acceptance_rule": "P-H29 (exact-derivative certification)",
        "audit_finding": "eleven-lens-audit-2026-08-03 B4",
        "register_item": "improvement-register-2026-08-03 M-C2",
        "check_count": CHECK_COUNT,
        "exact": {
            "full_residual_norm": full_norm,
            "vertical_residual_norm": vertical_norm,
            "vertical_direct_norm": vertical_direct_norm,
            "bianchi_discrepancy_norm": discrepancy_norm,
            "mixed_gram_identity_relative_residual": identity_residual,
            "mixed_gram_coefficients": coefficients.tolist(),
            "mixed_gram_exact_value": "(9/32)(I + T_tr) = (9/16) P_traceless",
        },
        "outer_fd_ladder": ladder,
        "superseded_published_fd_numbers": PUBLISHED,
        "claim_status_change": "none (verdicts unchanged, evidence upgraded)",
        "track_b": "untouched: already exact in the frozen probe",
        "verdict": verdict,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"RB7 EXACT-DERIVATIVE RE-VERDICT: {CHECK_COUNT} CHECKS PASS; "
        "KILL VERDICT SURVIVES; EVIDENCE NOW EXACT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
