#!/usr/bin/env python3
"""Independent raw replay for K248's q=15-to-q=16 shell."""
from __future__ import annotations

import json
from hashlib import sha256
from math import factorial

from flint import fmpq

from k230_order_six_permutation_projection_probe import raw_entries
from k242_order_six_third_shell_signed_taylor import coefficient_hash
from k243_order_six_budget_composition_q6_method_limit import PI_LOWER
from k244_order_six_exact_corner_shell_ladder import sinh_log
import k246_order_six_inner_cube_reallocation_probe as base
from k248_order_six_q16_sign_reversal import (
    ORDER,
    OUT,
    QHIGH,
    QLOW,
    TAIL_START,
)


def main() -> int:
    base.ORDER = ORDER
    base.TAIL_START = TAIL_START
    manifest = json.loads(OUT.read_text())
    groups = base.independent_groups(list(raw_entries()))
    polynomials = base.independent_polynomials(groups)
    assert len(groups) == 307 and len(polynomials) == ORDER + 1
    for degree, polynomial in enumerate(polynomials):
        assert (
            coefficient_hash(polynomial)
            == manifest["expansion"]["degree_sha256"][str(degree)]
        )

    cube_coefficients = {}
    for q in (QLOW, QHIGH):
        moments = base.independent_moments(q)
        coefficients = [fmpq(0)] * 9
        for polynomial in polynomials:
            for power, value in enumerate(
                base.independent_integral(polynomial, moments)
            ):
                coefficients[power] += value
        cube_coefficients[q] = coefficients
        digest = sha256(";".join(map(str, coefficients)).encode()).hexdigest()
        assert (
            digest
            == manifest["expansion"]["integrated_log_polynomial_sha256"][str(q)]
        )

    core_tail = base.independent_tail(groups, QHIGH)
    certificate = manifest["certificate"]
    assert str(core_tail) == certificate["exact_core_tail_majorant"]
    measure = sinh_log(QHIGH) ** 8 - sinh_log(QLOW) ** 8
    tail = (
        fmpq(2**8 * 256**6, factorial(5))
        / PI_LOWER**8
        * measure
        * core_tail
    )
    assert tail == base.row_value(certificate["normalized_tail_upper"])
    assert base.row_value(certificate["complete_lower"]) > 0
    assert manifest["decision"]["shell_strictly_positive"] is True
    assert (
        manifest["decision"]["result"]
        == "q16_shell_positive__first_farther_sign_reversal_not_found"
    )
    print("[PASS] K248 independent raw-orbit, moment, h22-tail replay")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
