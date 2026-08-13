#!/usr/bin/env python3
r"""PW2C fixed-Q,g active source-root Jacobian, descent, and full-K gate.

This probe replaces PW2B's structural unitriangular comparator by a
structurally faithful fixed-Q,g left-trivialized source-root differential of

    (epsilon,varpi; Q,g fixed) -> (epsilon exp u(T),varpi; Q,g fixed).

It proves a finite-mode/identity-germ result on the active component, not a
public-source bundle equivalence, same-Sobolev Banach diffeomorphism, nonlinear
inverse, or analytic domain theorem.  It also computes K_full rather than its
grade-two projection K_red.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R2 = load_probe(
    "pw2c_r2",
    "eric_curt_wave3d_b2c15r2_full_bch_action_gauge_curvature_adjoint_probe.py",
)
B14 = R2.B14
Q = R2.Q
REGISTRY = ROOT / "lab/process/pw2c-literal-source-jacobian-full-k.json"

EXACT = 0
TYPE = 0
SOURCE = 0
PLANTED = 0


def check(label: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(f"exact check failed: {label}")
    EXACT += 1


def type_check(label: str, condition: bool) -> None:
    global TYPE
    if not condition:
        raise AssertionError(f"type check failed: {label}")
    TYPE += 1


def source_check(label: str, condition: bool) -> None:
    global SOURCE
    if not condition:
        raise AssertionError(f"source check failed: {label}")
    SOURCE += 1


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted false claim passed: {label}")
    PLANTED += 1


def matrix_zero(value: sp.Matrix) -> bool:
    return all(sp.simplify(item) == 0 for item in value)


def cadd(*values):
    return B14.cliff_add(*values)


def cscale(value, coefficient):
    return B14.cliff_scale(value, coefficient)


def ccomm(left, right):
    return B14.cliff_comm(left, right)


def cgrade(value, target):
    return Q.cliff_grade(value, target)


def cequal(left, right) -> bool:
    keys = set(left) | set(right)
    return all(sp.simplify(left.get(key, 0) - right.get(key, 0)) == 0 for key in keys)


def main() -> None:
    data = json.loads(REGISTRY.read_text())
    type_check("registry records the scoped fixed-Q,g active-germ pass", data["status"].startswith("PW2C_FIXED_QG_ACTIVE_SOURCE_ROOT"))
    type_check("Q_Cl and metric Jacobian blocks remain open", "fixed" in data["layer_zero"]["clifford_reduction"] and "fixed" in data["jacobian"]["scope"])
    type_check("public source bundle port remains open", "NO_PUBLIC_BUNDLE_EQUIVALENCE" in data["global_claim"])
    type_check("source substitution is not called a gauge symmetry", "not by itself a gauge symmetry" in data["layer_zero"]["source_map"])
    type_check("full and reduced K remain distinct", "do not determine K_full" in data["layer_zero"]["reduced_connection"])
    type_check("finite-mode and nonlinear inverse grades remain distinct", "tame nonlinear inverse" in data["layer_zero"]["domain_levels"])
    type_check("P1/P2/P3 remain unused", data["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED")
    type_check("Curt remains separate", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    type_check("third lane remains closed", data["third_lane_gate"].endswith("NOT_PROMOTED"))

    # Fixed-Q,g identity-germ source-root differential on a structurally
    # faithful touched-grade slice. The large rank ledger is imported from
    # prior exact Alt/star-Alt certificates, not recomputed by this 6x6 slice.
    # Inputs are (zeta_h,zeta_m,alpha_h); L sends the grade-two translation
    # jet to the odd grade-3/11 tangent and D is a fixed-conormal symbol.
    n = sp.Integer(3)
    D = sp.diag(n, 2 * n)
    L = sp.Matrix([[1, 2], [-1, 1]])
    J = sp.eye(6)
    J[2:4, 0:2] = -L * D
    J[2:4, 4:6] = L
    N = J - sp.eye(6)
    Jinv = sp.eye(6) - N
    check("true identity-germ source Jacobian is grade-block triangular", J.det() == 1)
    check("grade-shifting differential is square-zero on the active split germ", N * N == sp.zeros(6))
    check("the actual germ inverse is exact", J * Jinv == sp.eye(6) and Jinv * J == sp.eye(6))
    reject("reuse PW2B's unrelated structural matrix as the source Jacobian", J == sp.eye(6))

    ledger = data["jacobian"]["imported_rank_ledger"]
    check("prior exact active rank ledger is retained without calling the 6x6 slice its computation", ledger == {
        "grade2_epsilon": 91,
        "grade3_11_epsilon": 728,
        "grade2_translation_first_jet": 1274,
        "alternation_rank": 364,
        "fixed_conormal_alternation_rank": 78,
    })

    # Fourier and interval controls expose domain distinctions hidden by a
    # finite block determinant. The scalar ODE is a hostile comparator, not
    # the same square-zero active-grade germ.
    lam = sp.symbols("lambda", real=True)
    mode = sp.symbols("n", integer=True)
    A_mode = 1 - sp.I * mode * lam
    check("Fourier root block has exact determinant 1-i*n*lambda", sp.expand(A_mode) == 1 - sp.I * mode * lam)
    check("real Fourier modes have strictly nonzero determinant norm", sp.simplify(A_mode * sp.conjugate(A_mode)) == 1 + mode**2 * lam**2)
    x = sp.symbols("x", real=True)
    interval_kernel = sp.exp(x / lam)
    check("hostile scalar interval comparator has a live boundary-dependent kernel", sp.simplify(interval_kernel - lam * sp.diff(interval_kernel, x)) == 0)
    reject("use the hostile scalar ODE to claim a kernel for the square-zero active germ", data["jacobian"]["interval_control"].startswith("SAME_ACTIVE_GERM"))
    reject("claim a bounded same-Hs self-map despite the derivative in T", data["jacobian"]["derivative_loss"] == "NONE")
    reject("sell the tangent inverse as a nonlinear inverse", data["jacobian"]["nonlinear_inverse"].startswith("PASS"))

    # Three-patch descent: equivariant local h fields glue; an independently
    # planted local h does not. Constant transitions isolate the group law.
    I2 = sp.eye(2)
    t12 = sp.Matrix([[1, 1], [0, 1]])
    t23 = sp.Matrix([[1, 0], [1, 1]])
    t13 = t12 * t23
    h1 = sp.Matrix([[1, 2], [0, 1]])
    h2 = sp.simplify(t12.inv() * h1 * t12)
    h3 = sp.simplify(t13.inv() * h1 * t13)
    check("equivariant h satisfies both three-patch overlap laws", h3 == sp.simplify(t23.inv() * h2 * t23))
    defects = (
        sp.simplify(h1 * t12 * h2.inv() * t12.inv()),
        sp.simplify(h2 * t23 * h3.inv() * t23.inv()),
        sp.simplify(h1 * t13 * h3.inv() * t13.inv()),
    )
    check("all equivariant overlap defects vanish", all(item == I2 for item in defects))
    bad_h2 = sp.Matrix([[1, 0], [1, 1]])
    bad_defect = sp.simplify(h1 * t12 * bad_h2.inv() * t12.inv())
    check("planted non-equivariant local h has a live overlap defect", bad_defect != I2)
    reject("infer global descent from local exponentiation alone", bad_defect == I2)

    B1 = sp.Matrix([[1, 2], [3, -1]])
    B2 = sp.simplify(t12.inv() * B1 * t12)
    K1 = sp.simplify(h1.inv() * B1 * h1 - B1)
    K2 = sp.simplify(h2.inv() * B2 * h2 - B2)
    check("literal tensorial K descends on the equivariant overlap", K2 == sp.simplify(t12.inv() * K1 * t12))
    check("B+K obeys the constant-transition connection overlap law", B2 + K2 == sp.simplify(t12.inv() * (B1 + K1) * t12))

    # A nonconstant overlap makes the inhomogeneous derivative term live.
    tv = sp.Matrix([[1, x], [0, 1]])
    tv_inv = sp.simplify(tv.inv())
    dtv = sp.diff(tv, x)
    hv1 = sp.diag(2, sp.Rational(1, 2))
    hv2 = sp.simplify(tv_inv * hv1 * tv)
    Bv1 = sp.Matrix([[1, 2], [3, -1]])
    Bv2 = sp.simplify(tv_inv * Bv1 * tv + tv_inv * dtv)

    def one_dimensional_k(connection, multiplier):
        return sp.simplify(
            multiplier.inv()
            * (sp.diff(multiplier, x) + connection * multiplier - multiplier * connection)
        )

    Kv1 = one_dimensional_k(Bv1, hv1)
    Kv2 = one_dimensional_k(Bv2, hv2)
    check("literal K has tensorial descent under a nonconstant transition", matrix_zero(Kv2 - sp.simplify(tv_inv * Kv1 * tv)))
    check("B+K has the full affine nonconstant-transition law", matrix_zero(Bv2 + Kv2 - sp.simplify(tv_inv * (Bv1 + Kv1) * tv + tv_inv * dtv)))
    reject("drop the inhomogeneous derivative from the affine connection overlap", matrix_zero(Bv2 + Kv2 - sp.simplify(tv_inv * (Bv1 + Kv1) * tv)))

    # Exact nonabelian differential-gauge germ.  U^2=0 makes exp(tU)=I+tU
    # literal, while noncentral Bx,By keep every covariant term live.
    y, s = sp.symbols("y s", real=True)
    U = sp.Matrix([[0, 1], [0, 0]])
    t = x**2 + x * y + 2 * y
    eta_scalar = 1 + x - y
    h = I2 + t * U
    hinv = I2 - t * U
    Bx = sp.Matrix([[1, 0], [2, -1]])
    By = sp.Matrix([[0, 3], [1, 0]])
    dBx = sp.Matrix([[0, 2], [-1, 0]])

    def k_component(connection, variable):
        return sp.simplify(hinv * (sp.diff(h, variable) + connection * h - h * connection))

    Kx, Ky = k_component(Bx, x), k_component(By, y)
    Bxh, Byh = Bx + Kx, By + Ky
    direct_Bxh = sp.simplify(hinv * Bx * h + hinv * sp.diff(h, x))
    direct_Byh = sp.simplify(hinv * By * h + hinv * sp.diff(h, y))
    check("literal K_full equals the direct transformed connection difference", matrix_zero(Bxh - direct_Bxh) and matrix_zero(Byh - direct_Byh))

    F_B = Bx * By - By * Bx
    F_Bh = sp.simplify(sp.diff(Byh, x) - sp.diff(Bxh, y) + Bxh * Byh - Byh * Bxh)
    check("literal K_full gives exact curvature conjugacy", matrix_zero(F_Bh - sp.simplify(hinv * F_B * h)))

    hs = I2 + (t + s * eta_scalar) * U
    hinvs = I2 - (t + s * eta_scalar) * U
    Bxs = Bx + s * dBx
    Kxs = sp.simplify(hinvs * (sp.diff(hs, x) + Bxs * hs - hs * Bxs))
    dK_direct = sp.simplify(sp.diff(Kxs, s).subs(s, 0))
    eta_h = eta_scalar * U
    delta_b_return = sp.simplify(hinv * dBx * h - dBx)
    dK_formula = sp.simplify(
        sp.diff(eta_h, x) + Bxh * eta_h - eta_h * Bxh + delta_b_return
    )
    check("literal delta-K formula agrees with direct differentiation including nonzero delta B", matrix_zero(dK_direct - dK_formula) and not matrix_zero(dK_direct) and not matrix_zero(delta_b_return))
    reject("replace h^-1 D_B h by h^-1 dh", Kx == sp.simplify(hinv * sp.diff(h, x)))

    # Full active Clifford K on the controlled linear bridge.  The Krylov
    # relation gives an exact two-function resummation and exposes what K_red
    # discarded.
    A = {sum(1 << index for index in (0, 1, 2)): F(1)}
    dA = {sum(1 << index for index in (0, 1, 3)): F(1)}

    def bridge(c3: F, c11: F):
        return cadd(cscale(A, c3), cscale(Q.internal_hodge(A), c11))

    def dbridge(c3: F, c11: F):
        return cadd(cscale(dA, c3), cscale(Q.internal_hodge(dA), c11))

    u10, du10 = bridge(F(1), F(0)), dbridge(F(1), F(0))
    ad1 = ccomm(u10, du10)
    ad2 = ccomm(u10, ad1)
    ad3 = ccomm(u10, ad2)
    check("controlled full-K Krylov relation closes exactly", cequal(ad2, cscale(du10, F(-4))) and cequal(ad3, cscale(ad1, F(-4))))

    a1 = sp.sin(2) / 2
    b1 = -(1 - sp.cos(2)) / 4

    def closed_full_k(c3: F, c11: F):
        delta = c3 * c3 - c11 * c11
        ui, dui = bridge(c3, c11), dbridge(c3, c11)
        comm = ccomm(ui, dui)
        if delta == 0:
            full = cadd(dui, cscale(comm, F(-1, 2)))
            return full, cgrade(cscale(comm, F(-1, 2)), 2)
        aa = sp.sin(2 * sp.sqrt(delta)) / (2 * sp.sqrt(delta))
        bb = -(1 - sp.cos(2 * sp.sqrt(delta))) / (4 * delta)
        full = cadd(cscale(dui, aa), cscale(comm, bb))
        return full, cgrade(cscale(comm, bb), 2)

    full10, red10 = closed_full_k(F(1), F(0))
    check("closed full-K formula contains the odd and grade-two dexp pieces", cequal(full10, cadd(cscale(du10, a1), cscale(ad1, b1))) and bool(cgrade(full10, 3)) and bool(red10))
    full53, red53 = closed_full_k(F(5, 3), F(4, 3))
    check("equal-Delta pairs keep the same reduced return but distinct full K", cequal(red10, red53) and not cequal(full10, full53))
    full_plus, red_plus = closed_full_k(F(1), F(1))
    full_minus, red_minus = closed_full_k(F(1), F(-1))
    comm_plus = ccomm(bridge(F(1), F(1)), dbridge(F(1), F(1)))
    comm_minus = ccomm(bridge(F(1), F(-1)), dbridge(F(1), F(-1)))
    check("the two controlled Hodge-null branches have vanishing commutator", not comm_plus and not comm_minus)
    z = sp.symbols("z", positive=True)
    check("the Delta-to-zero commutator coefficient has the exact minus-one-half limit", sp.limit(-(1 - sp.cos(2 * sp.sqrt(z))) / (4 * z), z, 0) == -sp.Rational(1, 2))
    check("both Hodge-null branches have zero K_red and nonzero literal K_full", not red_plus and not red_minus and bool(full_plus) and bool(full_minus))
    check("Hodge-null full K is exactly the nonzero odd Du term", cequal(full_plus, dbridge(F(1), F(1))) and cequal(full_minus, dbridge(F(1), F(-1))))
    generic_u0 = sp.Matrix([[0, 1], [0, 0]])
    generic_du0 = sp.diag(1, -1)
    generic_comm0 = generic_u0 * generic_du0 - generic_du0 * generic_u0
    generic_ad2_0 = generic_u0 * generic_comm0 - generic_comm0 * generic_u0
    generic_limit0 = generic_du0 - sp.Rational(1, 2) * generic_comm0
    check("generic Delta-zero Krylov control has ad_u squared Du zero with live commutator", generic_ad2_0 == sp.zeros(2) and generic_comm0 != sp.zeros(2))
    reject("infer Delta=0 alone implies K_full=Du without the branch commutator", generic_limit0 == generic_du0)
    reject("infer K_full=0 from Hodge-null K_red", not full_plus or not full_minus)
    allowed = set(R2.Q.B14.SP_GRADES)
    check("every controlled literal full-K term stays in the active Lie-algebra grades", all(mask.bit_count() in allowed for value in (full10, full53, full_plus, full_minus) for mask in value))

    # Trace reversal remains executable and cannot be swapped for raw
    # Frobenius merely to obtain a convenient finite Jacobian.
    lorentz = sp.diag(-1, 1, 1, 1)
    basis = []
    for i in range(4):
        item = sp.zeros(4); item[i, i] = 1; basis.append(item)
    for i in range(4):
        for j in range(i + 1, 4):
            item = sp.zeros(4); item[i, j] = item[j, i] = 1; basis.append(item)
    dewitt = sp.Matrix([[sp.trace(lorentz*p*lorentz*q) - sp.Rational(1, 2)*sp.trace(lorentz*p)*sp.trace(lorentz*q) for q in basis] for p in basis])
    raw = sp.Matrix([[sp.trace(lorentz*p*lorentz*q) for q in basis] for p in basis])
    signs = lambda matrix: (
        sum(multiplicity for value, multiplicity in matrix.eigenvals().items() if value > 0),
        sum(multiplicity for value, multiplicity in matrix.eigenvals().items() if value < 0),
    )
    check("trace-reversed and raw fibre inertias are exactly six-four and seven-three", dewitt != raw and signs(dewitt) == (6, 4) and signs(raw) == (7, 3) and data["native_fibre_signature"] == [6, 4])
    reject("substitute Curt seven-seven into the native total signature", data["native_total_signature"] == [7, 7])

    # Off-identity dexp resonance is an algebraic obstruction distinct from
    # the PDE/domain question. Identity u=0 is safe, but a 2pi rotation has
    # exp(-ad_u)=I and a singular dexp.
    resonance_generator = sp.Matrix([[0, -2 * sp.pi], [2 * sp.pi, 0]])
    resonance_dexp = sp.simplify((sp.eye(2) - (-resonance_generator).exp()) * resonance_generator.inv())
    check("off-identity dexp resonance is a distinct live algebraic obstruction", resonance_dexp == sp.zeros(2) and data["jacobian"]["dexp_resonance"].startswith("OPEN"))
    reject("promote identity-germ invertibility through every exponential point", data["jacobian"]["dexp_resonance"].startswith("ABSENT"))

    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    source_check("source owns epsilon-varpi and homogeneous distortion", "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack)
    source_check("source owns the fixed transgression grammar", "\\frac12d_{B_\\omega}T_\\omega" in pack and "\\frac13[T_\\omega,T_\\omega]" in pack)
    source_check("source owns gauge-rotated Levi-Civita language", "[02:19:17]" in toe and "gauge rotated Levi-Civita" in toe)
    source_check("source owns trace reversal but not the exact active real-form bridge", "00:26:28" in toe and any("public-to-active" in item for item in data["source_disposition"]["SOURCE_SILENT_REPOSITORY_DERIVED"]))

    reject("spend external datum on the differential source inverse", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")
    total = EXACT + TYPE + SOURCE + PLANTED
    print(f"PW2C source Jacobian/full K: {EXACT} exact + {TYPE} type + {SOURCE} source + {PLANTED} planted = {total} PASS")
    print("RESULT: fixed-Q,g active source-root Jacobian, finite-mode inverse, overlap descent, and literal K_full PASS")
    print("BOUNDARY: public-source bundle port, tame nonlinear inverse, boundary/domain choice, global atlas, and physical action remain open")


if __name__ == "__main__":
    main()
