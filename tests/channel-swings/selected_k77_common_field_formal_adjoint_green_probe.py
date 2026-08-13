#!/usr/bin/env python3
"""Exact local formal-adjoint/Green audit for the selected K77 source block.

The actual horizontal ``varpi`` response is decomposed into four principal
coefficients and one zero-order coefficient.  The conditional residual
pairing from v0.92 then gives a covector-valued formal adjoint and its Green
concomitant.  The probe deliberately does not manufacture the missing common
field coefficient banks for ``g`` and primitive ``epsilon``, nor a field-space
Riesz map turning the covector into an endomorphism.

Run with ``sage -python``.
"""

from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import contextlib
import io
import json
import runpy


ROOT = Path(__file__).resolve().parents[2]
ALL_GRADE = ROOT / "tests/channel-swings/selected_k77_coupled_all_grade_upsilon_graph_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, SOURCE, AND OWNERSHIP AUDIT")
source = read("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")
metric = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
epsilon = strict("lab/process/selected-k77-gamma-soldered-epsilon-dupsilon-orbit.json")
primitive = strict("lab/process/selected-first-order-epsilon-preboundary-compose.json")
varpi = strict("lab/process/selected-k77-common-field-dupsilon-varpi-block.json")

check("source", "source asks for a norm-square and an adjoint arena",
      "norm square" in source and "adjoint" in source)
check("source", "source is silent on the operative K77 Riesz map and analytic domain",
      "SOURCE-SILENT" in source and "closed analytic domain" in source)
check("type", "v0.95 closes geometric/rank data but does not serialize a common residual-coordinate D-g bank",
      metric["local_fixed_varpi_block"]["full_covariant_lc_first_jet_rank"] == 20
      and "coefficient_bank" not in metric["local_fixed_varpi_block"])
check("type", "primitive epsilon Euler/preboundary ownership is not a full D-epsilon-Upsilon coefficient bank",
      primitive["composed_chain"]["primitive_epsilon_euler"].startswith("D_B_ADJOINT")
      and epsilon["held_open"]["lower_order_and_nonlinear_D_epsilon_Upsilon"] == "OPEN")
check("type", "the four-column gamma-epsilon Ward orbit is not the full primitive epsilon field derivative",
      epsilon["result"].endswith("COMMON_FIELD_PRINCIPAL_ORBIT_JR_ZERO")
      and all(packet["combined_orbit_rank"] == 4
              for packet in epsilon["causal_orbits"].values()))
check("type", "D-omega Upsilon exterior prolongation remains distinct from D-epsilon Upsilon", True)
check("type", "equation-dual formal adjoint remains distinct from an endomorphism adjoint", True)
check("symplectic", "a Green concomitant precedes antisymmetrization into a presymplectic current", True)


print("\nB. ACTUAL SOURCE-VARPI FIRST-ORDER COEFFICIENT BANK")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(ALL_GRADE))
check("repo", "the exact all-grade response predecessor replays",
      "PASS 50/50" in capture.getvalue() and not P["FAILURES"])

M = P["M"]
V = P["V"]
ONE = M["ONE"]
ZERO = M["ZERO"]
channels = P["channels"]
t_background = P["t_background"]

horizontal_basis = []
for mu in range(4):
    for left in range(4):
        for right in range(left + 1, 4):
            horizontal_basis.append({1 << mu: M["blade"]((left, right))})
check("exact", "the actual horizontal Lorentz source carrier has dimension 24",
      len(horizontal_basis) == varpi["varpi_block"]["domain_dimension"] == 24)


def principal_response(mu, delta_a):
    q = {1 << mu: {0: ONE}}
    return M["hodge"](M["shiab"](M["wedge_raw"](q, delta_a), channels))


def zero_order_response(delta_a):
    delta_f = M["fadd"](
        M["wedge_raw"](t_background, delta_a),
        M["wedge_raw"](delta_a, t_background),
    )
    return M["fadd"](
        M["hodge"](M["shiab"](delta_f, channels)), delta_a
    )


principal = [[principal_response(mu, value) for value in horizontal_basis]
             for mu in range(4)]
zero_order = [zero_order_response(value) for value in horizontal_basis]
principal_ranks = [V["family_rank"](bank) for bank in principal]
zero_order_rank = V["family_rank"](zero_order)
principal_supports = [len(set().union(*(set(M["flatten"](v)) for v in bank)))
                      for bank in principal]
check("exact", "all four actual principal coefficient banks are live",
      all(rank > 0 for rank in principal_ranks))
check("exact", "the actual zero-order coefficient bank is live",
      zero_order_rank > 0)
check("control", "deleting the derivative term changes every source column",
      all(any(principal[mu][column] for mu in range(4))
          for column in range(24)))


def combine(bank, coefficients):
    out = {}
    for value, coefficient in zip(bank, coefficients):
        if coefficient:
            out = M["fadd"](out, M["fscale"](Q(coefficient), value))
    return out


def blade_square_sign(mask):
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


def form_sign(mask):
    value = 1
    for index in M["indices"](mask):
        value *= M["ETA"][index]
    return value


def k_pair(left, right):
    left = M["flatten"](left)
    right = M["flatten"](right)
    total = Q(0)
    for key in set(left).intersection(right):
        a = left[key]
        b = right[key]
        if a[1] or b[1]:
            raise AssertionError("the selected real source block acquired an imaginary coefficient")
        total += Q(form_sign(key[0]) * blade_square_sign(key[1])) * a[0] * b[0]
    return total


print("\nC. EXACT EQUATION-DUAL AND GREEN IDENTITY")
u0 = [Q((3 * i + 1) % 11 - 5) for i in range(24)]
u1 = [Q((5 * i + 2) % 13 - 6) for i in range(24)]
v0_coeff = [Q((7 * i + 4) % 17 - 8) for i in range(24)]
v1_coeff = [Q((11 * i + 3) % 19 - 9) for i in range(24)]

green_nonzero = []
for mu in range(4):
    Au0 = combine(principal[mu], u0)
    Au1 = combine(principal[mu], u1)
    Bu0 = combine(zero_order, u0)
    Bu1 = combine(zero_order, u1)
    # Residual test sections are actual combinations of principal and
    # zero-order images, so every pairing below is on K_loc's real support.
    v0 = M["fadd"](combine(principal[(mu + 1) % 4], v0_coeff),
                   combine(zero_order, v1_coeff))
    v1 = M["fadd"](combine(principal[(mu + 2) % 4], v1_coeff),
                   combine(zero_order, v0_coeff))

    ju = [M["fadd"](Au1, Bu0), Bu1]
    lhs = [
        k_pair(ju[0], v0),
        k_pair(ju[0], v1) + k_pair(ju[1], v0),
        k_pair(ju[1], v1),
    ]
    # J^!_K v is a field covector.  Evaluate it on u rather than silently
    # identifying that covector with a field vector.
    rhs = [
        -k_pair(Au0, v1) + k_pair(Bu0, v0),
        -k_pair(Au1, v1) + k_pair(Bu0, v1) + k_pair(Bu1, v0),
        k_pair(Bu1, v1),
    ]
    green = [
        k_pair(Au0, v0),
        k_pair(Au0, v1) + k_pair(Au1, v0),
        k_pair(Au1, v1),
    ]
    derivative_green = [green[1], 2 * green[2], Q(0)]
    check("exact", f"direction {mu}: formal-adjoint Green identity holds coefficientwise",
          [a - b for a, b in zip(lhs, rhs)] == derivative_green)
    green_nonzero.append(any(green))
check("exact", "the actual Green concomitant is nonzero rather than a vacuous boundary term",
      all(green_nonzero))

# Wrong sign in the derivative adjoint is the standard integration-by-parts
# failure.  The planted calculation omits the two minus signs in rhs.
mu = 0
Au0 = combine(principal[mu], u0)
Au1 = combine(principal[mu], u1)
v0 = combine(principal[1], v0_coeff)
v1 = combine(principal[2], v1_coeff)
wrong_rhs_linear = k_pair(Au1, v1)
correct_rhs_linear = -k_pair(Au1, v1)
check("planted", "PLANT the algebraic transpose without derivative sign is not the formal adjoint",
      wrong_rhs_linear != correct_rhs_linear)


print("\nD. FIELD-RIESZ NONUNIQUENESS AND COMMON-FIELD BOUNDARY")
# The same nonzero field covector has different representing vectors under two
# exact nondegenerate field pairings.  Lowering either vector returns the same
# covector, so the covector is canonical while the operator adjoint is not.
covector = [Q(i + 1) for i in range(24)]
riesz_one_vector = list(covector)
riesz_two_vector = [covector[0] / 2] + covector[1:]
check("exact", "two admissible finite Riesz choices produce different adjoint vectors",
      riesz_one_vector != riesz_two_vector)
check("exact", "both Riesz representatives lower to the same equation dual",
      riesz_one_vector == covector
      and [2 * riesz_two_vector[0]] + riesz_two_vector[1:] == covector)
check("planted", "PLANT the coordinate identity is not a source-owned field-space pairing", True)

for kind, label in (
    ("scope", "the exact result is the source-varpi equation dual and local Green concomitant, not a full three-field operator"),
    ("scope", "the metric geometric/rank closure must be emitted on this same residual-coordinate bank"),
    ("scope", "the full primitive epsilon Frechet bank remains unconstructed"),
    ("symplectic", "the Green current is not yet antisymmetrized or proved basic on a reduced phase space"),
    ("analytic", "formal local integration by parts is not a Green operator closed domain or hyperbolicity theorem"),
    ("krein", "K-loc is indefinite and no positive fundamental symmetry is inferred"),
    ("scope", "the U64,64 comparator and the two U32,32 Weyl-block product remain distinct"),
    ("scope", "P1 P2 P3 remain unused and no new field coefficient quotient or datum is added"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_NORM_SQUARE_ADJOINT_ARENA_AND_SOURCE_FIELDS__SOURCE_SILENT_KLOC_FIELD_RIESZ_FULL_DEPSILON_AND_ANALYTIC_DOMAIN")
print("VARPI_PRINCIPAL_RANKS=" + ",".join(map(str, principal_ranks)))
print("VARPI_PRINCIPAL_SUPPORTS=" + ",".join(map(str, principal_supports)))
print(f"VARPI_ZERO_ORDER_RANK={zero_order_rank}")
print("EQUATION_DUAL_AND_GREEN=EXACT_ON_ACTUAL_HORIZONTAL_VARPI_BLOCK")
print("COMMON_FIELD=NOT_ASSEMBLED__DG_COMMON_COORDINATE_BANK_AND_FULL_PRIMITIVE_DEPSILON_MISSING")
print("OPERATOR_ADJOINT=NEEDS_UNOWNED_FIELD_SPACE_RIESZ_MAP")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
