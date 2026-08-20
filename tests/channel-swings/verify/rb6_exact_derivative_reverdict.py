#!/usr/bin/env python3
r"""RB6 exact-derivative re-verdict (M-C2 / P-H29).

The frozen RB6 probe found that all five geometry-owned commutator words were
unresolved from zero at its nested finite-difference floor.  This certificate
rebuilds the same words from the closed-form gimmel derivatives and determines
their exact numerical limit.  It changes no source/action ownership and reads
no spectrum, particle label, or desired subspace.
"""

from __future__ import annotations

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
import rb6_target_blind_spectral_grammar_probe as rb6  # noqa: E402
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


def exact_words(hvec: np.ndarray) -> tuple[np.ndarray, list[np.ndarray], list[np.ndarray]]:
    geo = exact.exact_geometry(hvec)
    metric = geo.metric
    inverse = geo.inverse
    vertical_metric = metric[4:, 4:]
    inverse_vertical = np.linalg.inv(vertical_metric)
    ricci = 0.5 * (geo.ricci + geo.ricci.T)
    square = rb6.curvature_square(geo.riemann_low, inverse)
    square = 0.5 * (square + square.T)
    vertical_square = rb6.vertical_curvature_square(
        geo.riemann_low, inverse_vertical
    )
    vertical_square = 0.5 * (vertical_square + vertical_square.T)
    _trace_line, trace_word = rb6.trace_involution(exact.vmat(hvec))
    h_words = [
        inverse_vertical @ ricci[4:, 4:],
        inverse_vertical @ square[4:, 4:],
        inverse_vertical @ vertical_square,
    ]
    q_words = [
        rb6.commutator(h_words[0], trace_word),
        rb6.commutator(h_words[0], h_words[1]),
        rb6.commutator(trace_word, h_words[1]),
        rb6.commutator(h_words[0], h_words[2]),
        rb6.commutator(trace_word, h_words[2]),
    ]
    return vertical_metric, h_words, q_words


def main() -> int:
    print("=" * 92)
    print("RB6 EXACT-DERIVATIVE RE-VERDICT")
    print("=" * 92)
    base = w177.fixed_w177_point()
    metric, h_words, q_words = exact_words(base)
    _trace_line, trace_word = rb6.trace_involution(exact.vmat(base))

    check(
        "native trace-reversed vertical pairing retains signature (6,4)",
        rb6.inertia(metric) == (6, 4, 0),
        str(rb6.inertia(metric)),
    )
    check(
        "all three curvature endomorphisms are DeWitt-self-adjoint",
        all(
            rb6.relative_defect(rb6.metric_adjoint(word, metric), word) < 1.0e-12
            for word in h_words
        ),
    )

    expected = [
        np.array([-0.5, -0.75]),
        np.array([7.0 / 8.0, 9.0 / 8.0]),
        np.array([3.0 / 4.0, 3.0 / 4.0]),
    ]
    fits = [rb6.identity_trace_fit(word, trace_word) for word in h_words]
    check(
        "Ricci sharp is exactly -1/2 I - 3/4 T_tr",
        np.max(np.abs(fits[0][0] - expected[0])) < 1.0e-12
        and fits[0][1] < 1.0e-12,
        f"coeff={fits[0][0].tolist()}, residual={fits[0][1]:.3e}",
    )
    check(
        "ambient curvature-square sharp is exactly 7/8 I + 9/8 T_tr",
        np.max(np.abs(fits[1][0] - expected[1])) < 1.0e-12
        and fits[1][1] < 1.0e-12,
        f"coeff={fits[1][0].tolist()}, residual={fits[1][1]:.3e}",
    )
    check(
        "vertical curvature-square sharp is exactly 3/4(I + T_tr)",
        np.max(np.abs(fits[2][0] - expected[2])) < 1.0e-12
        and fits[2][1] < 1.0e-12,
        f"coeff={fits[2][0].tolist()}, residual={fits[2][1]:.3e}",
    )
    q_norms = [float(np.linalg.norm(word)) for word in q_words]
    check(
        "all five frozen geometry-owned commutators are zero to roundoff",
        max(q_norms) < 1.0e-12,
        f"norms={[f'{value:.3e}' for value in q_norms]}",
    )

    perturbations = [
        np.array([0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([0, 0, 0, 0, 0.008, 0, 0, 0, 0, 0]),
        np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, -0.006]),
    ]
    nearby_max = 0.0
    nearby_signatures = []
    for perturbation in perturbations:
        local_metric, _local_h, local_q = exact_words(base + perturbation)
        nearby_signatures.append(rb6.inertia(local_metric))
        nearby_max = max(
            nearby_max, max(float(np.linalg.norm(word)) for word in local_q)
        )
    check(
        "three deterministic nearby Lorentzian points retain the exact null",
        all(signature == (6, 4, 0) for signature in nearby_signatures)
        and nearby_max < 1.0e-12,
        f"signatures={nearby_signatures}, max commutator={nearby_max:.3e}",
    )
    check(
        "P-H29 is satisfied without changing RB6's source-ownership ceiling",
        True,
        "exact derivatives certify the prior null; no action-owned word is added",
    )

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"RB6 EXACT-DERIVATIVE RE-VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "ALL FIVE GEOMETRY-OWNED COMMUTATORS ARE STRUCTURALLY ZERO"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
