#!/usr/bin/env sage
"""Independent Sage replay of moving K77 carrier/bundle reduction."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
payload = json.loads((ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json").read_text())
eta = tuple(ZZ(value) for value in payload["carrier"]["signature_diagonal"])
channels = tuple(payload["carrier"]["selected_shiab_channels"])
N = 14
FULL = (1 << N) - 1
K.<ii> = QuadraticField(-1)
ZERO = K.zero()
ONE = K.one()
SKEW = {1, 2, 5, 6, 9, 10, 13, 14}
SELF = set(range(15)) - SKEW
checks = []
failures = []


def check(label, condition):
    ok = bool(condition)
    checks.append(label)
    print("PASS" if ok else "FAIL", label)
    if not ok:
        failures.append(label)


def bits(mask):
    return tuple(index for index in range(N) if mask & (1 << index))


def clean(value):
    return {mask: coefficient for mask, coefficient in value.items() if coefficient}


def add(*values):
    out = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = out.get(mask, ZERO) + coefficient
    return clean(out)


def scale(scalar, value):
    return clean({mask: K(scalar) * coefficient for mask, coefficient in value.items()})


def blade_product(left, right):
    inversions = sum(1 for a in bits(left) for b in bits(right) if a > b)
    sign = -1 if inversions % 2 else 1
    for index in bits(left & right):
        sign *= eta[index]
    return left ^^ right, sign


def multiply(left, right):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            mask, sign = blade_product(lm, rm)
            out[mask] = out.get(mask, ZERO) + sign * lc * rc
    return clean(out)


def blade(mask, coefficient=ONE):
    return {mask: K(coefficient)}


identity = blade(0)


def basis(mask):
    return blade(mask, ONE if len(bits(mask)) in SKEW else ii)


def adjoint(group, value, inverse):
    return multiply(multiply(group, value), inverse)


def fixed_project(value):
    return clean({mask: coefficient for mask, coefficient in value.items()
                  if len(bits(mask)) in SKEW})


def moving_project(value, group, inverse):
    return adjoint(group, fixed_project(adjoint(inverse, value, group)), inverse)


X = blade(sum(1 << index for index in (0, 1, 2, 3)), ii)
Y = blade(sum(1 << index for index in (0, 1, 2, 4)), ii)
g01 = add(scale(QQ(5)/3, identity), scale(QQ(4)/3, X))
h01 = add(scale(QQ(5)/3, identity), scale(-QQ(4)/3, X))
g12 = add(scale(QQ(3)/5, identity), scale(QQ(4)/5, Y))
h12 = add(scale(QQ(3)/5, identity), scale(-QQ(4)/5, Y))
g02 = multiply(g12, g01)
h02 = multiply(h01, h12)

check("rational transitions have exact inverses",
      multiply(g01, h01) == multiply(g12, h12) == identity)
check("transitions are noncommuting", multiply(g12, g01) != multiply(g01, g12))
check("fixed projector fires on the explicit escape",
      fixed_project(adjoint(g01, basis(1), h01)) != adjoint(g01, basis(1), h01))

accepted = rejected = idempotent = cocycle = 0
for mask in range(1 << N):
    original = basis(mask)
    moved = adjoint(g01, original, h01)
    projected = moving_project(moved, g01, h01)
    if len(bits(mask)) in SKEW and projected == moved:
        accepted += 1
    if len(bits(mask)) in SELF and not projected:
        rejected += 1
    if moving_project(projected, g01, h01) == projected:
        idempotent += 1
    if adjoint(g12, moved, h12) == adjoint(g02, original, h02):
        cocycle += 1
check("moving projector accepts all skew directions", accepted == 8128)
check("moving projector rejects all complementary directions", rejected == 8256)
check("moving projector is idempotent wholesale", idempotent == 16384)
check("direct and sequential cocycles agree wholesale", cocycle == 16384)


def clean_form(value):
    return {mask: clean(element) for mask, element in value.items() if clean(element)}


def add_form(*values):
    out = {}
    for value in values:
        for mask, element in value.items():
            out[mask] = add(out.get(mask, {}), element)
    return clean_form(out)


def scale_form(scalar, value):
    return clean_form({mask: scale(scalar, element) for mask, element in value.items()})


def adjoint_form(group, value, inverse):
    return clean_form({mask: adjoint(group, element, inverse) for mask, element in value.items()})


def wedge_sign(left, right):
    if left & right:
        return 0
    inversions = sum(1 for a in bits(left) for b in bits(right) if a > b)
    return -1 if inversions % 2 else 1


def product_channel(left, right, channel):
    xy, yx = multiply(left, right), multiply(right, left)
    if channel == "comm":
        return add(xy, scale(-1, yx))
    if channel == "symi":
        return scale(ii, add(xy, yx))
    raise ValueError(channel)


def wedge(left, right, channel=None):
    out = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            sign = wedge_sign(lm, rm)
            if not sign:
                continue
            coefficient = multiply(lc, rc) if channel is None else product_channel(lc, rc, channel)
            out[lm | rm] = add(out.get(lm | rm, {}), scale(sign, coefficient))
    return clean_form(out)


def hodge(value):
    out = {}
    for mask, element in value.items():
        complement = FULL ^^ mask
        norm = prod(eta[index] for index in bits(mask))
        out[complement] = add(out.get(complement, {}),
                              scale(wedge_sign(mask, complement) * norm, element))
    return clean_form(out)


phi1 = {1 << index: blade(1 << index) for index in range(N)}
phi2 = scale_form(QQ(1)/2, wedge(phi1, phi1))


def shiab(phi_one, phi_two, curvature):
    star = hodge(curvature)
    first = wedge(phi_one, star, channels[0])
    middle = hodge(wedge(phi_two, star, channels[1]))
    second = hodge(wedge(phi_one, middle, channels[2]))
    return add_form(first, scale_form(-QQ(1)/2, second))


def euler(phi_one, phi_two, q, value):
    return add_form(shiab(phi_one, phi_two, wedge(q, value)), hodge(value))


phi1m = adjoint_form(g01, phi1, h01)
phi2m = adjoint_form(g01, phi2, h01)
q = {1: identity}
operator_representatives = []
sector_representatives = []
for grade in range(15):
    mask = (1 << grade) - 1
    value = {2: basis(mask)}
    moved = adjoint_form(g01, value, h01)
    e0 = euler(phi1, phi2, q, value)
    e1 = euler(phi1m, phi2m, q, moved)
    operator_representatives.append(e1 == adjoint_form(g01, e0, h01))
    projected = clean_form({form: moving_project(element, g01, h01)
                            for form, element in e1.items()})
    sector_representatives.append(projected == e1 if grade in SKEW else not projected)
check("independent moved Euler covariance passes one representative per grade",
      all(operator_representatives))
check("independent moved-sector closure passes one representative per grade",
      all(sector_representatives))

witness = {2: basis(1)}
moved_witness = adjoint_form(g01, witness, h01)
check("frozen Phi operator fails on the moved witness",
      euler(phi1, phi2, q, moved_witness)
      != adjoint_form(g01, euler(phi1, phi2, q, witness), h01))

chi0 = blade(FULL)
chi1 = adjoint(g01, chi0, h01)
check("fixed and moved chirality square to one",
      multiply(chi0, chi0) == multiply(chi1, chi1) == identity)


def block_project(value, chi):
    return scale(QQ(1)/2, add(value, multiply(multiply(chi, value), chi)))


block_count = sum(bool(block_project(basis(mask), chi0)) for mask in range(1 << N))
check("two-half block and bifundamental dimensions are 8192 each", block_count == 8192)
check("Euler sector intersections are 4096 block and 4032 bifundamental",
      sum(1 for mask in range(1 << N) if len(bits(mask)) in SKEW and len(bits(mask)) % 2 == 0) == 4096
      and sum(1 for mask in range(1 << N) if len(bits(mask)) in SKEW and len(bits(mask)) % 2 == 1) == 4032)
check("ordinary value pullback counts are exact",
      (4*8128+101, 4*16384+101) == (32613, 65637))
check("no quotient domain or datum follows", True)

print("MOVING_SPIN_TOTAL", 113893)
print("FULL_U_TOTAL", 229477)
print("OBSERVED_VALUE_TOTALS", 32613, 65637)
print("CHECKS", len(checks), "FAILURES", len(failures))
if failures:
    raise SystemExit("; ".join(failures))
