#!/usr/bin/env python3
"""Independent python-flint exact-rank cross-check for PW2F.

Run with the repository CAS environment recorded by PW2F.  This script does
not own the verdict; it rebuilds the native rational matrices and asks FLINT,
rather than SymPy, for their exact ranks.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

from flint import arb, arb_mat, ctx, fmpq, fmpq_mat
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


T = load_probe(
    "pw2f_flint_primary", "pw2f_native_top_order_metric_composition_probe.py"
)


def as_fmpq(value) -> fmpq:
    rational = sp.Rational(value)
    return fmpq(int(rational.p), int(rational.q))


def as_fmpq_matrix(value: sp.Matrix) -> fmpq_mat:
    return fmpq_mat(
        value.rows,
        value.cols,
        [as_fmpq(value[row, column]) for row in range(value.rows) for column in range(value.cols)],
    )


def as_arb(value) -> arb:
    """Rigorous radical enclosure, without decimal reconstruction."""
    expression = sp.expand(value)
    if expression.is_Rational:
        rational = sp.Rational(expression)
        return arb(int(rational.p)) / arb(int(rational.q))
    if expression.is_Add:
        return sum((as_arb(term) for term in expression.args), arb(0))
    if expression.is_Mul:
        result = arb(1)
        for factor in expression.args:
            result *= as_arb(factor)
        return result
    if expression.is_Pow:
        base, exponent = expression.args
        if exponent == sp.Rational(1, 2):
            return as_arb(base).sqrt()
        if exponent.is_Integer:
            return as_arb(base) ** int(exponent)
    raise TypeError(f"unsupported exact radical expression: {expression}")


def native_inputs():
    curvature = T.D.to_sympy_form(T.P.SPIN_CURVATURE)
    source_t = T.D.build_source_t(T.D.shiab(curvature))
    d_t = {(0, 7): T.M.sscale(T.M.sblade(1, 3), -1)}
    q_t = T.M.sfwedge(source_t, source_t)
    written = T.M.sfadd(
        curvature,
        T.M.sfscale(d_t, sp.Rational(1, 2)),
        T.M.sfscale(q_t, sp.Rational(1, 3)),
    )
    return written, source_t


def main() -> None:
    ctx.prec = 192
    written, source_t = native_inputs()
    _, second, _, _, coefficient, _ = T.build_native_rank_matrices(
        written, source_t, include_third=False
    )
    checks = 0
    assert as_fmpq_matrix(second).rank() == 7
    checks += 1
    # The moving coefficient bank lies in a real multiquadratic extension,
    # while python-flint 0.9 exposes rational and Arb matrices but no
    # algebraic-number matrix.  Pick
    # an exact SymPy pivot minor, rebuild every entry in Arb directly from its
    # rational plus rational*sqrt(2) representation, and require its rigorous
    # determinant interval to exclude zero.  Ten columns then force rank ten.
    _, pivot_rows = coefficient.T.rref()
    assert len(pivot_rows) == 10
    minor = coefficient[list(pivot_rows), :]
    arb_minor = arb_mat(
        10,
        10,
        [as_arb(minor[row, column]) for row in range(10) for column in range(10)],
    )
    determinant = arb_minor.det()
    assert not determinant.contains(0)
    checks += 1
    assert second.rank() == as_fmpq_matrix(second).rank()
    checks += 1
    assert coefficient.rank() == 10
    checks += 1
    print(
        "PW2F FLINT EXACT CROSS-CHECK: "
        f"{checks} PASS; second_fmpq_rank=7; coefficient_arb_minor_excludes_zero; "
        "rank_upper_bounds_follow_from_10_COLUMNS"
    )


if __name__ == "__main__":
    main()
