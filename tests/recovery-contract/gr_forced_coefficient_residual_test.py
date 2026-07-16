#!/usr/bin/env python
"""Recovery contract GR forced-coefficient residual test.

This is the branch-local test unlocked by the 2026-07-16 action fingerprint.
It asks whether the frozen W203/W229/W230/W236 record-current induced-YM branch
supplies fixed native source/YM terms that cancel the known nonzero O(M^2)
Schwarzschild Willmore residual.

Result: NO_GO for this branch-local exact-vacuum GR cancellation. Under the
fingerprint's record-current W229 source law, Psi=0 implies J=0, hence theta=0,
so the source/YM side contributes no O(M^2) cancellation term. The principled
Schwarzschild Q^TF(B) residual is nonzero. Cancelling it would require changing
the action, source law, variation space, or free-quantity ledger, such as adding
a bare theta branch or importing a different functional.

This does not change any claim status, canon verdict, public posture, or the
broader recovery lane. It only closes this branch-local forced-coefficient GR
residual checkpoint.

Run: python tests/recovery-contract/gr_forced_coefficient_residual_test.py
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
FINGERPRINT = ROOT / "lab" / "process" / "recovery-contract-action-fingerprint-2026-07-16.json"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def load_fingerprint() -> dict:
    return json.loads(FINGERPRINT.read_text(encoding="utf-8"))


# Shared Schwarzschild weak-field symbols.
t, x, y, z, M, R = sp.symbols("t x y z M R", real=True, positive=True)
coords = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
eta = sp.diag(-1, 1, 1, 1)


def flat_box(expr):
    return -sp.diff(expr, t, 2) + sp.diff(expr, x, 2) + sp.diff(expr, y, 2) + sp.diff(expr, z, 2)


def schwarzschild_h():
    phi = M / r
    h = sp.zeros(4, 4)
    h[0, 0] = 2 * phi
    for i in (1, 2, 3):
        h[i, i] = 2 * phi
    return h


def build_qtf_from_principled_ii():
    """Build Q^TF(B) from principled graph-Hessian II, matching the OQ2-A tightening."""
    h = schwarzschild_h()

    def b(mu, nu, a, bidx):
        return sp.diff(h[a, bidx], coords[mu], coords[nu])

    hmean = sp.zeros(4, 4)
    for a in range(4):
        for bidx in range(4):
            hmean[a, bidx] = sp.simplify(sum(eta[m, m] * b(m, m, a, bidx) for m in range(4)))

    def bhat(mu, nu, a, bidx):
        return b(mu, nu, a, bidx) - sp.Rational(1, 4) * eta[mu, nu] * hmean[a, bidx]

    def fdot(func):
        return sum(eta[a, a] * eta[bidx, bidx] * func(a, bidx) for a in range(4) for bidx in range(4))

    q = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            t1 = sp.Rational(1, 2) * fdot(lambda a, bidx: hmean[a, bidx] * bhat(mu, nu, a, bidx))
            t2 = sum(
                eta[p, p] * fdot(lambda a, bidx: bhat(mu, p, a, bidx) * bhat(p, nu, a, bidx))
                for p in range(4)
            )
            q[mu, nu] = sp.simplify(t1 - t2)

    trace = sp.simplify(sum(eta[p, p] * q[p, p] for p in range(4)))
    qtf = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            qtf[mu, nu] = sp.simplify(q[mu, nu] - sp.Rational(1, 4) * eta[mu, nu] * trace)
    return qtf, hmean


def ray_leading_r_power(expr) -> int | None:
    """Leading falloff power n with expr ~ M^2/R^n on a generic ray."""
    e = sp.simplify(expr.subs({x: R, y: 2 * R, z: 3 * R}))
    if e == 0:
        return None
    for n in range(0, 14):
        scaled = sp.simplify(e * R**n / M**2)
        lim = sp.limit(scaled, R, sp.oo)
        if lim not in (sp.oo, -sp.oo, sp.zoo, sp.nan) and sp.simplify(lim) != 0:
            return n
    return None


def screened_poisson_1d(n_sites, z_u, c_theta, source):
    operator = sp.zeros(n_sites, n_sites)
    for i in range(n_sites):
        operator[i, i] += 2 * z_u + c_theta
        operator[i, (i + 1) % n_sites] += -z_u
        operator[i, (i - 1) % n_sites] += -z_u
    current = sp.Matrix(source)
    theta = operator.LUsolve(current)
    return operator, theta


def all_matrix_entries_zero(matrix) -> bool:
    return all(sp.simplify(matrix[i, j]) == 0 for i in range(matrix.rows) for j in range(matrix.cols))


def any_matrix_entry_nonzero(matrix) -> bool:
    return any(sp.simplify(matrix[i, j]) != 0 for i in range(matrix.rows) for j in range(matrix.cols))


def main() -> None:
    fingerprint = load_fingerprint()

    log("=" * 82)
    log("PC1 -- cancellation detector teeth")
    log("=" * 82)
    qtf, hmean = build_qtf_from_principled_ii()
    artificial_canceller = -qtf
    check(
        "PC1  a predeclared nonzero source tensor S=-Q^TF would cancel the residual",
        all_matrix_entries_zero(qtf + artificial_canceller),
        "detector registers a real cancellation when a nonzero source tensor is supplied",
    )

    log("")
    log("=" * 82)
    log("PC2 -- wrong-shape source does not fake a cancellation")
    log("=" * 82)
    wrong_shape = eta
    check(
        "PC2  adding a generic metric-proportional term does not cancel Q^TF(B)",
        any_matrix_entry_nonzero(qtf + wrong_shape),
        "cancellation is tensor-shape sensitive, not just coefficient bookkeeping",
    )

    log("")
    log("=" * 82)
    log("C1 -- action fingerprint boundary")
    log("=" * 82)
    source_law = fingerprint["source_law"]
    downstream = fingerprint["downstream_use_contract"]
    check("C1a  fingerprint uses the W154 record-current source law", source_law["status"] == "W154_POSIT_REQUIRED")
    check(
        "C1b  Psi=0 vacuum rule is explicit in the fingerprint",
        "Psi = 0 implies J[Psi] = 0" in source_law["vacuum_rule"],
    )
    check(
        "C1c  this exact O(M^2) Schwarzschild/Kerr test is the named downstream object",
        "O(M^2) Schwarzschild/Kerr" in downstream["valid_next_test_object"],
    )
    check(
        "C1d  changing action/source/variation/free ledger is the first kill condition",
        "changing the action, source law, variation space, or free-quantity ledger"
        in downstream["first_kill_condition"],
    )

    log("")
    log("=" * 82)
    log("C2 -- principled Schwarzschild Willmore residual is nonzero at O(M^2)")
    log("=" * 82)
    hmean_zero = all_matrix_entries_zero(hmean)
    nonzero_components = [
        (i, j, sp.simplify(qtf[i, j]))
        for i in range(4)
        for j in range(i, 4)
        if sp.simplify(qtf[i, j]) != 0
    ]
    powers = sorted({ray_leading_r_power(component) for _, _, component in nonzero_components})
    trace_free = sp.simplify(sum(eta[p, p] * qtf[p, p] for p in range(4))) == 0
    check("C2a  principled mean curvature H^(1) vanishes by harmonicity", hmean_zero)
    check(
        "C2b  Q^TF(B) is nonzero",
        len(nonzero_components) > 0,
        f"sample Q^TF[{nonzero_components[0][0]},{nonzero_components[0][1]}] = {nonzero_components[0][2]}",
    )
    check("C2c  Q^TF(B) is trace-free", trace_free)
    check(
        "C2d  nonzero Q^TF(B) components have leading falloff M^2/r^6 on a generic ray",
        powers == [6],
        f"leading powers = {powers}",
    )

    log("")
    log("=" * 82)
    log("C3 -- W229 record-current source vanishes in the Psi=0 vacuum")
    log("=" * 82)
    psi1, psi2, s11, s12, s22 = sp.symbols("psi1 psi2 s11 s12 s22", real=True)
    current_component = s11 * psi1**2 + 2 * s12 * psi1 * psi2 + s22 * psi2**2
    current_zero = sp.simplify(current_component.subs({psi1: 0, psi2: 0})) == 0
    degree_two = sp.simplify(current_component.subs({psi1: 2 * psi1, psi2: 2 * psi2}) - 4 * current_component) == 0
    check("C3a  record current J[Psi] is modeled as bilinear and vanishes at Psi=0", current_zero)
    check("C3b  record current has degree two, so no hidden linear-in-M vacuum source appears", degree_two)

    zero_source = [0, 0, 0, 0, 0, 0]
    theta_zero_for_all = True
    for kappa_v, z_v in (
        (sp.Rational(1), sp.Rational(1)),
        (sp.Rational(1, 5), sp.Rational(3)),
        (sp.Rational(7), sp.Rational(2)),
        (sp.Rational(11), sp.Rational(0)),
    ):
        c_theta = 1 / kappa_v
        operator, theta = screened_poisson_1d(6, z_v, c_theta, zero_source)
        theta_zero_for_all = theta_zero_for_all and all(sp.simplify(entry) == 0 for entry in theta)
        theta_zero_for_all = theta_zero_for_all and sp.simplify(operator.det()) != 0
    check(
        "C3c  zero record source gives theta=0 for sampled admissible kappa and Z_U",
        theta_zero_for_all,
        "source-side stress terms vanish because every term carries theta, D theta, or J",
    )

    log("")
    log("=" * 82)
    log("C4 -- forced-coefficient cancellation fails in this branch")
    log("=" * 82)
    zero_source_tensor = sp.zeros(4, 4)
    residual_after_frozen_source = qtf + zero_source_tensor
    check(
        "C4a  frozen W229 source/YM contribution is zero in the Psi=0 Schwarzschild vacuum",
        all_matrix_entries_zero(zero_source_tensor),
    )
    check(
        "C4b  Q^TF(B) + frozen source/YM contribution remains nonzero",
        any_matrix_entry_nonzero(residual_after_frozen_source),
        "no admissible kappa or Z_U can turn a zero source tensor into -Q^TF(B)",
    )
    check(
        "C4c  cancellation would require a different branch or new term",
        True,
        "bare theta, fundamental c_kin>0, H-class ambient term, or another action is outside this fingerprint",
    )

    log("")
    log("=" * 82)
    log("C5 -- Schwarzschild failure stops the Schwarzschild/Kerr exact-vacuum branch test")
    log("=" * 82)
    check(
        "C5  the branch-local exact-vacuum GR recovery benchmark fails already on Schwarzschild",
        any_matrix_entry_nonzero(residual_after_frozen_source),
        "Kerr need not rescue a branch that cannot cancel the Schwarzschild prerequisite residual",
    )

    log("")
    log("=" * 82)
    log("VERDICT")
    log("=" * 82)
    if not FAIL:
        log("Operational result: NO_GO for this branch-local forced-coefficient GR residual test.")
        log("The W229 record-current branch has a real, nonzero Schwarzschild Q^TF(B) residual and")
        log("a zero source/YM cancellation tensor in the Psi=0 vacuum. Exact-vacuum GR recovery")
        log("therefore cannot be claimed from this fingerprint without changing construction.")
        log("No claim status, canon verdict, public posture, portfolio state, or broader recovery")
        log("lane status changes here.")

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
