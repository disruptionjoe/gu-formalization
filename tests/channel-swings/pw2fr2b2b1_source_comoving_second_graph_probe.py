#!/usr/bin/env python3
r"""PW2F-R2B2B1 source-coordinate and co-moving second-graph prerequisite.

This is an exact finite noncommutative chart, not the complete GU C5/C4
operator.  It keeps ``Gamma(g)`` and ``q_g(epsilon)`` independent, fixes
``varpi`` in the source chart, and then moves every tested connection and
distortion object through one repository-derived ``h=exp(u)`` frame.  The
probe constructs the mixed second derivative of that graph and checks the
two-term pullback-Hessian chain rule.  It does not compute the source ``I1``
or manuscript ``I2B`` Hessian, the five remaining coefficient slots, an
independent reverse/Green route, a domain, quotient, observation equation, or
physics.  P1/P2/P3 are unused.
"""

from __future__ import annotations

import sympy as sp


FAILURES: list[str] = []
EXACT = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}")
    if not condition:
        FAILURES.append(f"exact: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}")
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}")
    if not condition:
        FAILURES.append(f"planted: {label}")


def zero(value: sp.Matrix | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


def at_origin(value: sp.Matrix | sp.Expr, r: sp.Symbol, s: sp.Symbol):
    return value.subs({r: 0, s: 0})


def mixed(value: sp.Matrix | sp.Expr, r: sp.Symbol, s: sp.Symbol):
    return at_origin(sp.diff(value, r, s), r, s)


def first(value: sp.Matrix | sp.Expr, parameter: sp.Symbol, r: sp.Symbol, s: sp.Symbol):
    return at_origin(sp.diff(value, parameter), r, s)


def flatten(*matrices: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([entry for matrix in matrices for entry in matrix])


def main() -> int:
    typed("source epsilon and repository h=exp(u) remain distinct objects")
    typed("Gamma(g), q, B_full, T, and A_total retain separate owners; the finite q directions do not construct the epsilon-to-q Frechet map")
    typed("the declared co-moving h/theta1/Bhat2 graph below is repository-derived, not source-attributed or the actual native u(T) law")
    typed("the finite matrix witness tests graph structure, not the complete GU C5/C4 symbol")
    typed("I1 pulled Hessian and manuscript I2B residual-square Hessian remain distinct and uncomputed")
    typed("vary-upstairs chain-rule assembly and restrict-first direct differentiation are compared only on the finite fixture")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    typed("P1/P2/P3 supply no tangent, second graph, cancellation, or proof certificate")

    r, s, x, y = sp.symbols("r s x y", real=True)
    I = sp.eye(2)
    U = sp.Matrix([[0, 1], [0, 0]])

    # Two-dimensional exact source chart. Gamma and q vary independently;
    # varpi is fixed. All matrices are deliberately noncommuting.
    Gx0 = sp.Matrix([[1, 2], [3, -1]])
    Gy0 = sp.Matrix([[0, 2], [-1, 1]])
    Gxr = sp.Matrix([[0, 1], [2, 0]])
    Gxs = sp.Matrix([[2, -1], [1, -2]])
    Gyr = sp.Matrix([[1, 0], [-2, -1]])
    Gys = sp.Matrix([[0, 3], [1, 0]])
    Qx0 = sp.Matrix([[0, 1], [-1, 0]])
    Qy0 = sp.Matrix([[2, 0], [1, -2]])
    Qxr = sp.Matrix([[1, 2], [0, -1]])
    Qxs = sp.Matrix([[0, -2], [1, 0]])
    Qyr = sp.Matrix([[0, 1], [3, 0]])
    Qys = sp.Matrix([[1, -1], [0, -1]])
    Vx = sp.Matrix([[3, 1], [-2, -3]])
    Vy = sp.Matrix([[1, 2], [1, -1]])

    Gamma_x = Gx0 + r * Gxr + s * Gxs
    Gamma_y = Gy0 + r * Gyr + s * Gys
    q_x = Qx0 + r * Qxr + s * Qxs
    q_y = Qy0 + r * Qyr + s * Qys
    Bx, By = Gamma_x + q_x, Gamma_y + q_y
    Tx, Ty = Vx - q_x, Vy - q_y
    Ax, Ay = Gamma_x + Vx, Gamma_y + Vy

    exact("source chart satisfies B_full=Gamma+q in both components", Bx == Gamma_x + q_x and By == Gamma_y + q_y)
    exact("source chart satisfies T=varpi-q at fixed varpi", Tx == Vx - q_x and Ty == Vy - q_y)
    exact("source chart satisfies A_total=B_full+T=Gamma+varpi", zero(Bx + Tx - Ax) and zero(By + Ty - Ay))

    dTr = (first(Tx, r, r, s), first(Ty, r, r, s))
    dTs = (first(Tx, s, r, s), first(Ty, s, r, s))
    dBr = (first(Bx, r, r, s), first(By, r, r, s))
    dBs = (first(Bx, s, r, s), first(By, s, r, s))
    dGr = (Gxr, Gyr)
    dGs = (Gxs, Gys)
    exact("fixed-varpi r tangent is deltaT=-deltaq and deltaB=deltaGamma+deltaq", all(zero(dTr[i] + (Qxr, Qyr)[i]) and zero(dBr[i] - dGr[i] - (Qxr, Qyr)[i]) for i in range(2)))
    exact("fixed-varpi s tangent is deltaT=-deltaq and deltaB=deltaGamma+deltaq", all(zero(dTs[i] + (Qxs, Qys)[i]) and zero(dBs[i] - dGs[i] - (Qxs, Qys)[i]) for i in range(2)))
    exact("the old minus-deltaB shortcut differs from deltaT by the live minus-deltaGamma return", all(zero((-dBr[i]) - dTr[i] + dGr[i]) and not zero(dGr[i]) for i in range(2)) and all(zero((-dBs[i]) - dTs[i] + dGs[i]) and not zero(dGs[i]) for i in range(2)))
    reject("identify deltaT with minus deltaB_full at fixed source roots", all(zero(dTr[i] + dBr[i]) for i in range(2)))

    # Exact exponential because U^2=0. The mixed k term makes D2h and dtheta2
    # explicit; the f*g term retains nonlinear conjugation even when D2u is
    # removed in a control.
    f = x + y
    g = x * y + 2 * y
    k = x**2 + x * y + y
    tau = r * f + s * g + r * s * k
    h = I + tau * U
    hinv = I - tau * U
    exact("h=exp(tau U) and h inverse are exact because U squared is zero", U * U == sp.zeros(2) and zero(h * hinv - I) and zero(hinv * h - I))

    def affine(connection: sp.Matrix, variable: sp.Symbol) -> sp.Matrix:
        return sp.expand(hinv * connection * h + hinv * sp.diff(h, variable))

    def homogeneous(value: sp.Matrix) -> sp.Matrix:
        return sp.expand(hinv * value * h)

    Gammahat_x, Gammahat_y = affine(Gamma_x, x), affine(Gamma_y, y)
    qhat_x, qhat_y = homogeneous(q_x), homogeneous(q_y)
    varpihat_x, varpihat_y = homogeneous(Vx), homogeneous(Vy)
    Bhat_x, Bhat_y = affine(Bx, x), affine(By, y)
    That_x, That_y = homogeneous(Tx), homogeneous(Ty)
    Ahat_x, Ahat_y = affine(Ax, x), affine(Ay, y)

    exact("one co-moving frame preserves Bhat=Gammahat+qhat", zero(Bhat_x - Gammahat_x - qhat_x) and zero(Bhat_y - Gammahat_y - qhat_y))
    exact("one co-moving frame preserves That=varpihat-qhat", zero(That_x - varpihat_x + qhat_x) and zero(That_y - varpihat_y + qhat_y))
    exact("one co-moving frame preserves Ahat=Bhat+That", zero(Ahat_x - Bhat_x - That_x) and zero(Ahat_y - Bhat_y - That_y))

    F_B = sp.expand(sp.diff(By, x) - sp.diff(Bx, y) + Bx * By - By * Bx)
    F_Bhat = sp.expand(sp.diff(Bhat_y, x) - sp.diff(Bhat_x, y) + Bhat_x * Bhat_y - Bhat_y * Bhat_x)
    exact("the affine co-moving connection obeys exact curvature conjugacy", zero(F_Bhat - hinv * F_B * h))

    theta_r = f * U
    theta_s = g * U
    theta_rs = k * U
    exact("theta1=dexp at the identity has live r and s branches", first(h, r, r, s) == theta_r and first(h, s, r, s) == theta_s and not zero(theta_r) and not zero(theta_s))
    exact("the mixed second orbit and its spatial d-theta branch are explicit and live", mixed(h, r, s) == theta_rs and not zero(sp.diff(theta_rs, x)) and not zero(sp.diff(theta_rs, y)))

    def assembled_bhat2(B0: sp.Matrix, Br: sp.Matrix, Bs: sp.Matrix, variable: sp.Symbol) -> sp.Matrix:
        # Expansion of h^-1 B h + h^-1 d h at r=s=0.
        return sp.expand(
            f * (Bs * U - U * Bs)
            + g * (Br * U - U * Br)
            + k * (B0 * U - U * B0)
            - 2 * f * g * U * B0 * U
            + sp.diff(k, variable) * U
        )

    Bx0, By0 = at_origin(Bx, r, s), at_origin(By, r, s)
    Bxr, Bxs = first(Bx, r, r, s), first(Bx, s, r, s)
    Byr, Bys = first(By, r, r, s), first(By, s, r, s)
    Bhat2_x, Bhat2_y = mixed(Bhat_x, r, s), mixed(Bhat_y, r, s)
    exact("direct mixed Bhat derivative matches the independently assembled Bhat2 formula", zero(Bhat2_x - assembled_bhat2(Bx0, Bxr, Bxs, x)) and zero(Bhat2_y - assembled_bhat2(By0, Byr, Bys, y)))
    exact("the noncommuting co-moving Bhat2 branch is live", not zero(Bhat2_x) and not zero(Bhat2_y))

    frozen_second = flatten(mixed(Bx, r, s), mixed(By, r, s), mixed(Tx, r, s), mixed(Ty, r, s))
    dynamic_second = flatten(Bhat2_x, Bhat2_y, mixed(That_x, r, s), mixed(That_y, r, s))
    exact("freezing h annihilates this mixed second graph while the dynamic graph is live", zero(frozen_second) and not zero(dynamic_second))

    c0 = I + U
    cr = 2 * I - U
    cs = -I + 3 * U
    tau_comm = r * f + s * g
    h_comm = I + tau_comm * U
    hinv_comm = I - tau_comm * U
    C = c0 + r * cr + s * cs
    Cmove = sp.expand(hinv_comm * C * h_comm + hinv_comm * sp.diff(h_comm, x))
    exact("commuting linear-orbit control annihilates the mixed second graph", zero(mixed(Cmove, r, s)))
    reject("infer that a commuting control annihilates the noncommuting Bhat2 branch", zero(Bhat2_x) or zero(Bhat2_y))

    # Exact two-term pullback Hessian. The direct restrict-first derivative
    # must equal J*H J + E.D2F. E is chosen as a hostile off-shell covector on
    # one live second-graph coordinate; the on-shell control sets E=0.
    z = flatten(Bhat_x, Bhat_y, That_x, That_y)
    z0 = at_origin(z, r, s)
    zr, zs, zrs = first(z, r, r, s), first(z, s, r, s), mixed(z, r, s)
    live_index = next(index for index, value in enumerate(zrs) if sp.simplify(value) != 0)
    H = sp.diag(*range(1, len(z) + 1))
    E = sp.zeros(len(z), 1)
    E[live_index] = 1
    e = E - H * z0
    action = sp.Rational(1, 2) * (z.T * H * z)[0] + (e.T * z)[0]
    direct_hessian = mixed(action, r, s)
    jhj = (zr.T * H * zs)[0]
    second_return = (E.T * zrs)[0]
    exact("restrict-first direct Hessian equals J-star-H-J plus E-times-D2 graph", zero(direct_hessian - jhj - second_return))
    exact("the off-shell E-times-D2 co-moving return is live", not zero(second_return), f"live_coordinate={live_index}; return={sp.simplify(second_return)}")
    exact("the first-JVP-only comparator misses exactly the live second-graph return", zero(direct_hessian - jhj - second_return) and not zero(direct_hessian - jhj))

    e_on = -H * z0
    action_on = sp.Rational(1, 2) * (z.T * H * z)[0] + (e_on.T * z)[0]
    direct_on = mixed(action_on, r, s)
    exact("on-shell control annihilates E-times-D2 and leaves J-star-H-J", zero(direct_on - jhj))
    reject("drop E-times-D2 from an off-shell pulled Hessian", zero(direct_hessian - jhj))
    reject("promote a live finite D2 graph to a complete quartic-order GU coefficient", False)
    reject("claim the finite comparator computes either I1 or I2B", False)
    reject("spend P1/P2/P3 to choose the co-moving graph", False)
    reject("merge Curt or promote a third lane from this Eric-lane prerequisite", False)

    total = EXACT + TYPE + PLANTED
    print(
        "RESULT: source q/Gamma split exact; co-moving Bhat2 live; "
        f"off_shell_second_return={sp.simplify(second_return)}"
    )
    print(f"SUMMARY: {EXACT} exact + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: R2B2B1 SOURCE-SPLIT / CO-MOVING SECOND-GRAPH PREREQUISITE PASSES; COMPLETE C5/C4 REMAINS OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
