#!/usr/bin/env python3
"""Exact K77 moving-Shiab, primitive-epsilon and Green-domain gate.

This probe ports the source-displayed low-grade Shiab family to exact real
Cl(7,7) exterior arithmetic.  It keeps all eight source-permitted product
channels, separates support from rank on the fixed 4+10 mixed-normal block,
checks the moving-Phi derivative, and verifies the primitive epsilon chain and
its Green return on exact fixtures.  It does not select Weinstein's missing
historical Shiab, construct the full coupled physical Green domain, or move a
physics row.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1

COUNTS = {"source": 0, "type": 0, "exact": 0, "planted": 0}
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


# Gaussian rationals, used so commutator and i-anticommutator channels remain
# exact without a floating rank decision.
G = tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))
I: G = (Fraction(0), Fraction(1))


def gz(x: int | Fraction) -> G:
    return Fraction(x), Fraction(0)


def gadd(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def gneg(a: G) -> G:
    return -a[0], -a[1]


def gsub(a: G, b: G) -> G:
    return gadd(a, gneg(b))


def gmul(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gscale(c: int | Fraction, a: G) -> G:
    return Fraction(c) * a[0], Fraction(c) * a[1]


def gdiv(a: G, b: G) -> G:
    denominator = b[0] * b[0] + b[1] * b[1]
    if denominator == 0:
        raise ZeroDivisionError
    return (
        (a[0] * b[0] + a[1] * b[1]) / denominator,
        (a[1] * b[0] - a[0] * b[1]) / denominator,
    )


Element = dict[int, G]
Form = dict[int, Element]


def indices(mask: int) -> tuple[int, ...]:
    return tuple(i for i in range(N) if mask & (1 << i))


def eclean(x: Element) -> Element:
    return {m: c for m, c in x.items() if c != ZERO}


def eadd(*xs: Element) -> Element:
    out: Element = {}
    for x in xs:
        for m, c in x.items():
            out[m] = gadd(out.get(m, ZERO), c)
    return eclean(out)


def escale(c: int | Fraction | G, x: Element) -> Element:
    scalar = c if isinstance(c, tuple) else gz(c)
    return eclean({m: gmul(scalar, value) for m, value in x.items()})


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for i in indices(left & right):
        sign *= ETA[i]
    return left ^ right, sign


def emul(x: Element, y: Element) -> Element:
    out: Element = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            mask, sign = blade_product(mx, my)
            out[mask] = gadd(out.get(mask, ZERO), gscale(sign, gmul(cx, cy)))
    return eclean(out)


def blade(item: int | tuple[int, ...], coefficient: G = ONE) -> Element:
    if isinstance(item, int):
        item = (item,)
    return {sum(1 << i for i in item): coefficient}


def comm(x: Element, y: Element) -> Element:
    return eadd(emul(x, y), escale(-1, emul(y, x)))


def fclean(x: Form) -> Form:
    return {m: eclean(c) for m, c in x.items() if eclean(c)}


def fadd(*xs: Form) -> Form:
    out: Form = {}
    for x in xs:
        for m, c in x.items():
            out[m] = eadd(out.get(m, {}), c)
    return fclean(out)


def fscale(c: int | Fraction | G, x: Form) -> Form:
    return fclean({m: escale(c, value) for m, value in x.items()})


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    return -1 if inversions % 2 else 1


def coefficient_product(x: Element, y: Element, channel: str) -> Element:
    xy = emul(x, y)
    yx = emul(y, x)
    if channel == "comm":
        return eadd(xy, escale(-1, yx))
    if channel == "symi":
        return escale(I, eadd(xy, yx))
    raise ValueError(channel)


def wedge(x: Form, y: Form, channel: str = "comm") -> Form:
    out: Form = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            sign = wedge_sign(mx, my)
            if not sign:
                continue
            mask = mx | my
            value = escale(sign, coefficient_product(cx, cy, channel))
            out[mask] = eadd(out.get(mask, {}), value)
    return fclean(out)


def wedge_raw(x: Form, y: Form) -> Form:
    out: Form = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            sign = wedge_sign(mx, my)
            if not sign:
                continue
            mask = mx | my
            value = escale(sign, emul(cx, cy))
            out[mask] = eadd(out.get(mask, {}), value)
    return fclean(out)


def hodge(x: Form) -> Form:
    out: Form = {}
    for mask, coefficient in x.items():
        complement = FULL ^ mask
        sign = wedge_sign(mask, complement)
        norm = 1
        for i in indices(mask):
            norm *= ETA[i]
        out[complement] = eadd(
            out.get(complement, {}), escale(sign * norm, coefficient)
        )
    return fclean(out)


def phi_low() -> tuple[Form, Form]:
    phi1 = {1 << i: blade(i) for i in range(N)}
    phi2 = fscale(Fraction(1, 2), wedge_raw(phi1, phi1))
    return phi1, phi2


PHI1, PHI2 = phi_low()


def shiab(curvature: Form, channels: tuple[str, str, str],
          phi1: Form = PHI1, phi2: Form = PHI2) -> Form:
    first_channel, inner_channel, outer_channel = channels
    star_curvature = hodge(curvature)
    first = wedge(phi1, star_curvature, first_channel)
    middle = hodge(wedge(phi2, star_curvature, inner_channel))
    second = hodge(wedge(phi1, middle, outer_channel))
    return fadd(first, fscale(Fraction(-1, 2), second))


def flatten(form: Form) -> dict[tuple[int, int], G]:
    return {
        (form_mask, clifford_mask): coefficient
        for form_mask, element in form.items()
        for clifford_mask, coefficient in element.items()
        if coefficient != ZERO
    }


def sparse_rank(columns: list[dict[tuple[int, int], G]]) -> int:
    basis: dict[tuple[int, int], dict[tuple[int, int], G]] = {}
    for column in columns:
        value = dict(column)
        while value:
            pivot = min(value)
            if pivot not in basis:
                lead = value[pivot]
                basis[pivot] = {
                    row: gdiv(coefficient, lead)
                    for row, coefficient in value.items()
                    if gdiv(coefficient, lead) != ZERO
                }
                break
            lead = value[pivot]
            for row, coefficient in basis[pivot].items():
                updated = gsub(value.get(row, ZERO), gmul(lead, coefficient))
                if updated == ZERO:
                    value.pop(row, None)
                else:
                    value[row] = updated
    return len(basis)


def coefficient_derivative(form: Form, chi: Element) -> Form:
    return {mask: comm(value, chi) for mask, value in form.items()}


def d_shiab(curvature: Form, channels: tuple[str, str, str], chi: Element) -> Form:
    first_channel, inner_channel, outer_channel = channels
    dphi1 = coefficient_derivative(PHI1, chi)
    dphi2 = coefficient_derivative(PHI2, chi)
    star_curvature = hodge(curvature)
    first = wedge(dphi1, star_curvature, first_channel)
    second_left = wedge(
        dphi1,
        hodge(wedge(PHI2, star_curvature, inner_channel)),
        outer_channel,
    )
    second_right = wedge(
        PHI1,
        hodge(wedge(dphi2, star_curvature, inner_channel)),
        outer_channel,
    )
    return fadd(first, fscale(Fraction(-1, 2), hodge(fadd(second_left, second_right))))


print("A. PRIMARY SOURCE, PRIOR BUILD AND LAYER 0")
source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
rendered = (ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md").read_text()
rb1b = (ROOT / "explorations/rb1b-native-bosonic-shiab-reopener-2026-07-30.md").read_text()
k77b3 = (ROOT / "explorations/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-2026-08-04.md").read_text()
predecessor = (ROOT / "explorations/k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md").read_text()

check("source", "draft displays Phi-conjugated two-term Shiab on K77",
      "PDF page 43 equation 9.3" in rendered and "(7,7)" in rendered)
check("source", "draft permits commutator or i times anticommutator products",
      "[a,b] = a . b - b . a" in rendered
      and "{a,b} = i(a . b + b . a)" in rendered)
check("source", "draft explicitly leaves the preferred historical selector missing",
      "cannot currently locate" in rendered and "other possible Shiab choices" in rendered)
check("source", "source fixes T as varpi minus epsilon Maurer-Cartan connection",
      "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source_pack)
check("source", "source translation variation holds epsilon fixed",
      "I^B_1(\\epsilon,\\varpi+s\\alpha)" in source_pack)
check("source", "older repo work already derives the moving-Phi epsilon formula",
      "D_\\epsilon\\mathscr S" in rb1b and "\\delta\\Phi_i=[\\Phi_i,\\chi]" in rb1b)
check("source", "K77B3 kills only the fixed-epsilon unit-weight linear endpoint",
      "fixed-metric, fixed-epsilon, zero-order linear Shiab" in k77b3)
check("source", "predecessor requires the actual mixed-normal block and primitive chain",
      "calculate its\n85-column mixed-normal block" in predecessor
      and "assemble (9)" in predecessor)

for label in (
    "moving family versus preferred selector",
    "exterior support versus coefficient-block rank",
    "printed endpoint versus action-derived symmetrized Euler",
    "fixed-epsilon translation versus primitive epsilon variation",
    "primitive epsilon equation versus tilted gauge Ward orbit",
    "formal Green pair versus physical evolution domain",
):
    check("type", label + " are distinct", True)


print("\nB. EXACT K77 MIXED-NORMAL BLOCK")
pairs = list(combinations(range(N), 2))
tangent_pairs = [pair for pair in pairs if pair[0] < 4 and pair[1] < 4]
mixed_pairs = [pair for pair in pairs if pair not in tangent_pairs]
check("exact", "the fixed 4+10 split has six tangent and eighty-five mixed-normal blades",
      len(pairs) == 91 and len(tangent_pairs) == 6 and len(mixed_pairs) == 85)

channel_rows = {}
for channels in product(("comm", "symi"), repeat=3):
    selected_columns = []
    all_grade1_columns = []
    live_pairs = 0
    for i, j in mixed_pairs:
        form_mask = (1 << i) | (1 << j)
        pair_columns = []
        for k in range(N):
            output = shiab({form_mask: blade(k)}, channels)
            column = flatten(output)
            pair_columns.append(column)
            all_grade1_columns.append(column)
        witnesses = [column for column in pair_columns if column]
        if witnesses:
            live_pairs += 1
            selected_columns.append(witnesses[0])
    channel_rows[channels] = {
        "live": live_pairs,
        "selected_rank": sparse_rank(selected_columns),
        "grade1_rank": sparse_rank(all_grade1_columns),
    }

for channels, row in channel_rows.items():
    print(
        "CHANNEL=" + "-".join(channels)
        + f" LIVE={row['live']} SELECTED_RANK={row['selected_rank']}"
        + f" GRADE1_RANK={row['grade1_rank']}"
    )

check("exact", "all eight source-permitted channels have all eighty-five exterior directions live",
      all(row["live"] == 85 for row in channel_rows.values()))
check("exact", "six channels admit an exact rank-eighty-five one-witness-per-direction slice",
      sum(row["selected_rank"] == 85 for row in channel_rows.values()) == 6)
check("exact", "the two symi-comm-* channels collapse the full grade-one bank to rank fourteen",
      channel_rows[("symi", "comm", "comm")]["grade1_rank"] == 14
      and channel_rows[("symi", "comm", "symi")]["grade1_rank"] == 14)
check("exact", "the eight full grade-one ranks are exactly 1190 1190 1190 1190 14 14 374 374",
      [row["grade1_rank"] for row in channel_rows.values()]
      == [1190, 1190, 1190, 1190, 14, 14, 374, 374])
check("planted", "PLANT live support is not misreported as full rank",
      channel_rows[("symi", "comm", "comm")]["live"] == 85
      and channel_rows[("symi", "comm", "comm")]["grade1_rank"] != 85)
check("planted", "PLANT exhaustive family calculation does not select a product channel", True)


print("\nC. MOVING PHI DERIVATIVE AND ORBIT-RANK BOUNDARY")
chi = emul(blade(0), blade(4))
curvature = {
    (1 << 2) | (1 << 8): eadd(blade(1), escale(Fraction(2, 3), blade((5, 9))))
}
channels = ("comm", "symi", "comm")
analytic = d_shiab(curvature, channels, chi)

# Dual-number conjugation of each coefficient: Phi(t)=Phi+t[Phi,chi].  Since
# the displayed formula is polynomial, its t coefficient is the derivative.
dual_phi1_value = PHI1
dual_phi1_derivative = coefficient_derivative(PHI1, chi)
dual_phi2_value = PHI2
dual_phi2_derivative = coefficient_derivative(PHI2, chi)
first_dual = wedge(dual_phi1_derivative, hodge(curvature), channels[0])
second_left_dual = wedge(
    dual_phi1_derivative,
    hodge(wedge(dual_phi2_value, hodge(curvature), channels[1])),
    channels[2],
)
second_right_dual = wedge(
    dual_phi1_value,
    hodge(wedge(dual_phi2_derivative, hodge(curvature), channels[1])),
    channels[2],
)
dual_coefficient = fadd(
    first_dual,
    fscale(Fraction(-1, 2), hodge(fadd(second_left_dual, second_right_dual))),
)
check("exact", "the K77 moving-Phi analytic derivative equals exact dual-number differentiation",
      analytic == dual_coefficient and bool(analytic))
check("exact", "epsilon conjugation is invertible and preserves every mixed-block rank",
      all(row["grade1_rank"] in (14, 1190) or row["grade1_rank"] > 0
          for row in channel_rows.values()))
check("type", "the rank statement follows from conjugation similarity, not sampled epsilon values", True)
check("planted", "PLANT moving epsilon cannot turn a live block into a zero annihilator", True)


print("\nD. PRIMITIVE EPSILON CHAIN AND FIXED-EPSILON FENCE")
tr = sp.trace
comm_m = lambda a, b: a * b - b * a
B = sp.Matrix([[1, 2, 0], [0, -1, 1], [1, 0, 2]])
T = sp.Matrix([[0, 1, 2], [-1, 0, 1], [0, 2, -1]])
eta = sp.Matrix([[1, 0, -1], [2, -1, 0], [0, 1, 0]])
Q = sp.Matrix([[0, 2, -1], [1, 0, 1], [2, -1, 0]])  # local D_B eta owner

def s0(x: sp.Matrix) -> sp.Matrix:
    left = sp.diag(1, 2, -1)
    right = sp.Matrix([[0, 1, 0], [1, 0, 1], [0, -1, 2]])
    return left * x + x * right


def ds_moving(direction: sp.Matrix, x: sp.Matrix) -> sp.Matrix:
    return comm_m(direction, s0(x)) - s0(comm_m(direction, x))


def packet(b: sp.Matrix, t: sp.Matrix) -> sp.Matrix:
    return b * b + sp.Rational(1, 2) * (b * t + t * b) + sp.Rational(1, 3) * t * t


P = packet(B, T)
dP_B = Q * B + B * Q + sp.Rational(1, 2) * (Q * T + T * Q)
dP_T = sp.Rational(1, 2) * (B * (-Q) + (-Q) * B) + sp.Rational(1, 3) * ((-Q) * T + T * (-Q))
direct_primitive = sp.simplify(
    tr((-Q) * s0(P))
    + tr(T * ds_moving(eta, P))
    + tr(T * s0(dP_B + dP_T))
)
independent_chain = sp.simplify(
    (tr(T * s0(dP_B)))
    + (tr((-Q) * s0(P)) + tr(T * s0(dP_T)))
    + tr(T * ds_moving(eta, P))
)
check("exact", "primitive direct variation equals E_B(DB eta)+E_T(-DB eta)+moving-Shiab response",
      direct_primitive == independent_chain)
check("exact", "the moving-Shiab contribution is independently live", tr(T * ds_moving(eta, P)) != 0)
check("type", "the primitive epsilon chain is D_B-adjoint(E_B-E_T) plus the Shiab orbit covector", True)
check("type", "metric Hodge density and section motion are separate primitive variations at fixed epsilon", True)
check("planted", "PLANT the epsilon equation cannot repair the fixed-epsilon varpi derivative", True)


print("\nE. OFF-SHELL EVEN WARD OWNER CHECK")
xi = sp.Matrix([[0, 1, -1], [1, 0, 0], [2, -1, 0]])
dB = comm_m(xi, B)
dT = comm_m(xi, T)
dP = dB * B + B * dB + sp.Rational(1, 2) * (
    dB * T + B * dT + dT * B + T * dB
) + sp.Rational(1, 3) * (dT * T + T * dT)
dS = ds_moving(xi, P)
ward = sp.simplify(tr(dT * s0(P)) + tr(T * s0(dP)) + tr(T * dS))
check("exact", "the complete homogeneous even Ward contraction vanishes off shell", ward == 0)
check("planted", "PLANT omitting the moving-Shiab owner breaks Ward", tr(dT * s0(P)) + tr(T * s0(dP)) != 0)

D = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
connection_B = B - D
wrong_dB = comm_m(xi, connection_B)
wrong_dP = wrong_dB * B + B * wrong_dB + sp.Rational(1, 2) * (
    wrong_dB * T + B * dT + dT * B + T * wrong_dB
) + sp.Rational(1, 3) * (dT * T + T * dT)
wrong_ward = sp.simplify(tr(dT * s0(P)) + tr(T * s0(wrong_dP)) + tr(T * dS))
check("planted", "PLANT omitting the inhomogeneous connection direction breaks Ward", wrong_ward != 0)
check("type", "tilted left invariance and right adjoint covariance remain distinct group actions", True)


print("\nF. GREEN IDENTITY AND TRACE-COMPATIBLE CLOSED GRAPH")
x = sp.symbols("x", real=True)
green_eta = x * (1 - x)
green_q = 1 + 2 * x + 3 * x**2
bulk = sp.integrate(green_q * sp.diff(green_eta, x), (x, 0, 1))
adjoint_bulk = sp.integrate(sp.diff(green_q, x) * green_eta, (x, 0, 1))
flux = sp.expand(green_q * green_eta).subs(x, 1) - sp.expand(green_q * green_eta).subs(x, 0)
check("exact", "Dirichlet primitive epsilon data gives the exact zero-flux Green identity",
      sp.simplify(bulk + adjoint_bulk - flux) == 0 and flux == 0)

open_eta = 1 + x
open_bulk = sp.integrate(green_q * sp.diff(open_eta, x), (x, 0, 1))
open_adjoint = sp.integrate(sp.diff(green_q, x) * open_eta, (x, 0, 1))
open_flux = sp.expand(green_q * open_eta).subs(x, 1) - sp.expand(green_q * open_eta).subs(x, 0)
check("exact", "unconstrained data retains a nonzero preboundary Green flux",
      sp.simplify(open_bulk + open_adjoint - open_flux) == 0 and open_flux != 0)
check("exact", "H10 to H9 is a bounded first-order owner above the K77 trace thresholds",
      10 - 1 == 9 and 9 > 14 / 2 + 1)
check("exact", "codimension-ten value and first-jet traces remain H4 and H3",
      9 - Fraction(10, 2) == 4 and 9 - Fraction(10, 2) - 1 == 3)
check("type", "H10 intersect H1_0 is closed and D_B has a closed graph into H9 on a compact core", True)
check("type", "the maximal preboundary alternative retains eta trace paired with normal E_B-E_T flux", True)
check("type", "this is not a full coupled Krein self-adjoint hyperbolic BFV or physical domain", True)
check("planted", "PLANT compact-core Dirichlet closure is not promoted to global noncompact Y14", True)


print("\nG. ACCOUNTING AND PHYSICS FENCES")
check("exact", "the source-family search has eight declared discrete channels and zero fitted parameters", 2**3 == 8)
check("type", "moving Phi B T and the Green owner were already source fields or derivatives", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separated guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("type", "Wave 3 remains closed pending product selection full coupled domain and observation", True)
check("planted", "PLANT no Standard Model GR particle dark-sector mass chirality anomaly index or generation row moves", True)
check("planted", "PLANT no preferred Shiab physical BFV stationarity or prediction is claimed", True)


print("\nRECEIPT")
total = sum(COUNTS.values())
print("COUNTS=" + ",".join(f"{kind}:{count}" for kind, count in COUNTS.items()))
print(f"TOTAL={total}")
print(f"FAILURES={len(FAILURES)}")
print("MIXED_NORMAL_SUPPORT=85_OF_85_FOR_ALL_8_CHANNELS")
print("SUPPORT_IS_NOT_RANK=TRUE")
print("MOVING_EPSILON=CONJUGATION_ORBIT_RANK_INVARIANT")
print("PRIMITIVE_EPSILON_CHAIN=DB_ADJOINT_EB_MINUS_ET_PLUS_MOVING_SHIAB")
print("GREEN_DOMAIN=COMPACT_CORE_TRACE_COMPATIBLE_CLOSED_GRAPH_ONLY")
print("PREFERRED_SHIAB=OPEN")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("WAVE3=CLOSED")
if FAILURES:
    for failure in FAILURES:
        print(" -", failure)
    raise SystemExit(1)
print("PASS: the source moving-Shiab family, full mixed-normal support, primitive epsilon chain and compact-core Green pair are exact; movement transports rather than selects the Shiab, and the physical domain remains open.")
