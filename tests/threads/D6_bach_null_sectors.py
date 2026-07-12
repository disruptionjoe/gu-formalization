#!/usr/bin/env python3
"""D6 -- Bach null-sector audit for the OQ2-A functional gate.

The D-thread showed that the H-class linearized section operator `box^2 h`
matches the linearized Bach operator on the transverse-traceless spin-2 sector.
That is not enough for GU-proper: the exact Schwarzschild graph has a trace
component, and diffeomorphism directions should also be null directions of a
metric field equation.

This test isolates the linearized null-sector requirement:

* TT spin-2: Bach is proportional to `box^2 h`.
* Pure trace/conformal: Bach vanishes, while naive `box^2 h` need not.
* Pure gauge/diffeomorphism: Bach vanishes, while naive `box^2 h` need not.

Therefore the OQ2-A functional must supply the conformal/gauge-invariant Bach
combination, not just the naive componentwise `box^2 h`, if the H-class gravity
reduction is to clear GU-proper rather than only the TT spin-2 sector.

Run: python -u tests/threads/D6_bach_null_sectors.py
"""
from __future__ import annotations

import sympy as sp

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


t, x, y, z = sp.symbols("t x y z", real=True)
coords = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta


def d(expr: sp.Expr, mu: int) -> sp.Expr:
    return sp.diff(expr, coords[mu])


def box_expr(expr: sp.Expr) -> sp.Expr:
    return sp.simplify(
        sum(eta_inv[m, n] * d(d(expr, m), n) for m in range(4) for n in range(4))
    )


def box_tensor(h: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(4, 4, lambda a, b: box_expr(h[a, b]))


def riem_low(h: sp.Matrix) -> dict[tuple[int, int, int, int], sp.Expr]:
    """Linearized all-lower Riemann tensor on flat background."""
    R: dict[tuple[int, int, int, int], sp.Expr] = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for dd in range(4):
                    R[(a, b, c, dd)] = sp.simplify(
                        sp.Rational(1, 2)
                        * (
                            d(d(h[a, dd], b), c)
                            + d(d(h[b, c], a), dd)
                            - d(d(h[b, dd], a), c)
                            - d(d(h[a, c], b), dd)
                        )
                    )
    return R


def ricci_low(R: dict[tuple[int, int, int, int], sp.Expr]) -> sp.Matrix:
    Ric = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            Ric[a, b] = sp.simplify(
                sum(eta_inv[c, dd] * R[(c, a, dd, b)] for c in range(4) for dd in range(4))
            )
    return Ric


def ricci_scalar(Ric: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(eta_inv[a, b] * Ric[a, b] for a in range(4) for b in range(4)))


def weyl_low(
    R: dict[tuple[int, int, int, int], sp.Expr], Ric: sp.Matrix, Rs: sp.Expr
) -> dict[tuple[int, int, int, int], sp.Expr]:
    """Linearized 4D Weyl tensor with all indices lowered."""
    C: dict[tuple[int, int, int, int], sp.Expr] = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for dd in range(4):
                    term_ric = sp.Rational(1, 2) * (
                        eta[a, c] * Ric[dd, b]
                        - eta[a, dd] * Ric[c, b]
                        - eta[b, c] * Ric[dd, a]
                        + eta[b, dd] * Ric[c, a]
                    )
                    term_rs = sp.Rational(1, 6) * Rs * (
                        eta[a, c] * eta[dd, b] - eta[a, dd] * eta[c, b]
                    )
                    C[(a, b, c, dd)] = sp.simplify(R[(a, b, c, dd)] - term_ric + term_rs)
    return C


def bach_lin(C: dict[tuple[int, int, int, int], sp.Expr]) -> sp.Matrix:
    """Linearized Bach tensor B_ab = d^r d^s C_{a r b s}."""
    B = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            B[a, b] = sp.simplify(
                sum(
                    eta_inv[r, rp] * eta_inv[s, sp_] * d(d(C[(a, r, b, s)], rp), sp_)
                    for r in range(4)
                    for s in range(4)
                    for rp in range(4)
                    for sp_ in range(4)
                )
            )
    return B


def linearized_bach(h: sp.Matrix) -> tuple[sp.Matrix, dict[tuple[int, int, int, int], sp.Expr]]:
    R = riem_low(h)
    Ric = ricci_low(R)
    Rs = ricci_scalar(Ric)
    C = weyl_low(R, Ric, Rs)
    return bach_lin(C), R


def all_zero_matrix(M: sp.Matrix) -> bool:
    return all(sp.simplify(M[a, b]) == 0 for a in range(M.rows) for b in range(M.cols))


print("=" * 78)
print("D6 -- Bach null-sector audit")
print("=" * 78)

# Baseline TT graviton: non-null spin-2 sector, same setup as the D-thread but
# using a polynomial profile so the audit stays small.
F = x**4
h_tt = sp.zeros(4, 4)
h_tt[2, 2] = F
h_tt[3, 3] = -F
B_tt, _ = linearized_bach(h_tt)
box2_tt = box_tensor(box_tensor(h_tt))
tt_match = all(
    sp.simplify(box2_tt[a, b] + 4 * B_tt[a, b]) == 0 for a in range(4) for b in range(4)
)
check(
    "TT spin-2 baseline: box^2 h = -4 * Bach^(1), matching the D-thread operator identity",
    tt_match and not all_zero_matrix(B_tt),
    f"box^2 h_yy={box2_tt[2, 2]}, Bach_yy={B_tt[2, 2]}",
)

# Pure conformal/trace mode: Bach must vanish by conformal invariance, while
# componentwise box^2 h can be nonzero.
phi = x**4
h_trace = sp.Matrix(4, 4, lambda a, b: eta[a, b] * phi)
B_trace, _ = linearized_bach(h_trace)
box2_trace = box_tensor(box_tensor(h_trace))
check(
    "pure trace/conformal mode: Bach^(1) vanishes identically",
    all_zero_matrix(B_trace),
)
check(
    "pure trace/conformal mode: naive componentwise box^2 h is not a null operator",
    not all_zero_matrix(box2_trace),
    f"box^2 h_00={box2_trace[0, 0]}, box^2 h_yy={box2_trace[2, 2]}",
)

# Pure diffeomorphism mode h_ab = partial_a xi_b + partial_b xi_a.
# Curvature, Weyl, and Bach must vanish. Naive box^2 h need not.
xi = [x**5, sp.S(0), sp.S(0), sp.S(0)]
h_gauge = sp.Matrix(4, 4, lambda a, b: sp.simplify(d(xi[b], a) + d(xi[a], b)))
B_gauge, R_gauge = linearized_bach(h_gauge)
box2_gauge = box_tensor(box_tensor(h_gauge))
riem_gauge_zero = all(sp.simplify(v) == 0 for v in R_gauge.values())
check(
    "pure gauge/diffeomorphism mode: linearized Riemann vanishes identically",
    riem_gauge_zero,
)
check(
    "pure gauge/diffeomorphism mode: Bach^(1) vanishes identically",
    all_zero_matrix(B_gauge),
)
check(
    "pure gauge/diffeomorphism mode: naive componentwise box^2 h is not gauge-null",
    not all_zero_matrix(box2_gauge),
    f"box^2 h_tx={box2_gauge[0, 1]}",
)

print("\n[verdict -- D6]")
print("  The Bach residual has the null sectors a metric gravity equation needs:")
print("  conformal trace modes and diffeomorphism modes vanish, while the TT spin-2")
print("  sector carries the same fourth-order operator as the H-class D-thread.")
print("  The naive componentwise box^2 h operator fails both null-sector checks.")
print("  Therefore OQ2-A must supply the conformal/gauge-invariant Bach combination")
print("  if the H-class gravity reduction is to clear GU-proper rather than only TT.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)

print("\nexit 0 = Bach null sectors verified; OQ2-A trace/gauge gate sharpened.")
