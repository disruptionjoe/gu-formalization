#!/usr/bin/env python3
"""Exact infinitesimal quotient test for the O(6,4)/U(3,2) J family.

The trace direction q is taken negative in the filed (6,4) DeWitt form.
At a standard compatible J, the q-stabilizer orbit has the same dimension as
the full J family.  Thus the continuous local quotient is zero-dimensional IF
the action and observation retain the full q-stabilizer.  The probe does not
establish that physical symmetry premise or remove discrete components.
"""

import sympy as sp


N = 10


def linear_solution_dimension(extra_equations) -> int:
    symbols = sp.symbols(f"x0:{N*N}")
    x = sp.Matrix(N, N, symbols)
    eta = sp.diag(*([1] * 6 + [-1] * 4))
    equations = list(x.T * eta + eta * x)
    equations.extend(extra_equations(x))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, symbols)
    return len(symbols) - coefficient_matrix.rank()


def main() -> None:
    q = sp.zeros(N, 1)
    q[8, 0] = 1  # a negative trace line
    j = sp.zeros(N)
    for a, b in ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9)):
        j[b, a] = 1
        j[a, b] = -1

    eta = sp.diag(*([1] * 6 + [-1] * 4))
    checks: list[tuple[str, bool]] = []

    def check(name, condition):
        checks.append((name, bool(condition)))
        print(("PASS" if condition else "FAIL") + " :: " + name)

    check("J^2=-I", j * j == -sp.eye(N))
    check("J is eta-orthogonal", j.T * eta * j == eta)
    check("q is negative", (q.T * eta * q)[0] == -1)

    so64 = linear_solution_dimension(lambda _x: [])
    u32 = linear_solution_dimension(lambda x: list(x * j - j * x))
    q_stab = linear_solution_dimension(lambda x: list(x * q))
    joint = linear_solution_dimension(lambda x: list(x * q) + list(x * j - j * x))

    check("dim so(6,4)=45", so64 == 45)
    check("dim u(3,2)=25", u32 == 25)
    check("J orbit dimension is 20", so64 - u32 == 20)
    check("dim stabilizer(q)=dim so(6,3)=36", q_stab == 36)
    check("dim stabilizer(q,J)=dim u(3,1)=16", joint == 16)
    check("q-stabilizer orbit spans all 20 J tangents", q_stab - joint == so64 - u32 == 20)
    check("conditional local physical quotient has dimension zero",
          (so64 - u32) - (q_stab - joint) == 0)

    passed = sum(ok for _, ok in checks)
    print(f"\nJ-orbit local quotient: {passed}/{len(checks)} exact checks PASS")
    print("RESULT: LOCAL_CONTINUOUS_QUOTIENT_POINT_IF_FULL_Q_STABILIZER_IS_PHYSICAL_SYMMETRY")
    print("OPEN: action/observation preservation of that group; global component quotient")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
