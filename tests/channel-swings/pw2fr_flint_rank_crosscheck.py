#!/usr/bin/env python3
"""Independent FLINT rank certificate for PW2F-R's induced C4 subblock."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

from flint import fmpq, fmpq_mat
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


T = load_probe("pw2fr_flint_primary", "pw2fr_complete_derived_k_c3_probe.py")


def as_fmpq(value) -> fmpq:
    rational = sp.Rational(sp.simplify(value))
    return fmpq(int(rational.p), int(rational.q))


def as_fmpq_matrix(value: sp.Matrix) -> fmpq_mat:
    return fmpq_mat(
        value.rows,
        value.cols,
        [as_fmpq(value[row, column]) for row in range(value.rows) for column in range(value.cols)],
    )


def mass_matrix(eta):
    _, _, bridge_u, _ = T.E.native_inputs()
    c3, c11 = sp.symbols("c3 c11", real=True)
    null_u = T.M.sclean(
        {mask: sp.simplify(value.subs({c3: 1, c11: 1})) for mask, value in bridge_u.items()}
    )
    h, hinv = T.E.exponential_pair(null_u, sp.Integer(0))
    forms = [
        T.E.fconj(
            hinv,
            T.principal_b_form(eta, owner, False, True),
            h,
        )
        for owner in range(10)
    ]
    return T.gram(forms)


def main() -> None:
    nonnull = mass_matrix(T.coordinate_eta(0))
    null = mass_matrix(T.coordinate_eta(0, 3))
    nonnull_flint = as_fmpq_matrix(nonnull)
    null_flint = as_fmpq_matrix(null)
    checks = 0
    assert nonnull_flint.rank() == 10
    checks += 1
    assert nonnull_flint.det() != 0
    checks += 1
    assert null_flint.rank() == 0 and null_flint == fmpq_mat(10, 10)
    checks += 1
    assert nonnull.rank() == nonnull_flint.rank() and null.rank() == null_flint.rank()
    checks += 1
    print(
        "PW2F-R FLINT EXACT CROSS-CHECK: "
        f"{checks} PASS; nonnull_fmpq_rank=10; null_fmpq_rank=0; determinant_nonzero"
    )


if __name__ == "__main__":
    main()
