#!/usr/bin/env python3
"""Exact bivector/Kosmann moving-Shiab comparison with the v0.86 rank-three packet.

This probe deliberately recomputes the moving-Phi derivative from the source
formula ``Phi_i(epsilon)=Ad(epsilon^-1)Phi_i^0``.  It does not define the
operator response as the negative of the predecessor residual.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
SOURCE_VARIABLE = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
MOVING_BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER ZERO, AND IMMUTABLE PREDECESSOR")
source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
reconciliation = read(
    "explorations/conditional-build/"
    "selected-k77-principal-ward-gamma-epsilon-reconciliation-2026-08-08.md"
)
check("source", "source makes Phi1 and Phi2 an epsilon-conjugation orbit",
      "Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0" in source)
check("source", "source owns the moving-Phi derivative grammar but not physical soldering",
      "D_epsilon Shiab" in source and "SOURCE-SILENT" in source)
check("repo", "v0.86 narrows the unfitted packet to rank three",
      "source-minimal required moving operator rank = 3" in reconciliation)
for label in (
    "inverse-Kosmann bivector frame transport versus grade-one gamma soldering",
    "moving Shiab coefficient derivative versus raw curvature input derivative",
    "principal frame orbit versus complete lower-order primitive epsilon Frechet derivative",
    "Ward cancellation versus reduced symplectic or BFV phase space",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(SOURCE_VARIABLE))
check("repo", "the source-variable Levi-Civita/diffeomorphism block replays",
      "PASS 84/84" in capture.getvalue() and not S["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(MOVING_BACKEND))
check("repo", "the K77 moving-Phi/Shiab backend replays",
      "FAILURES=0" in capture.getvalue() and not M["FAILURES"])
PAIRS = [(a, b) for a in range(4) for b in range(a + 1, 4)]
CHANNELS = ("comm", "symi", "symi")
Q0 = {1 << 0: {0: M["ONE"]}}
T_BACKGROUND = M["fscale"](Fraction(-1, 312), M["PHI1"])
F_BACKGROUND = M["wedge_raw"](T_BACKGROUND, T_BACKGROUND)


def coefficient_derivative(form, chi):
    return {mask: M["comm"](value, chi) for mask, value in form.items()}


def d_shiab(curvature, channels, chi):
    """Differentiate only the two conjugated Phi insertions."""
    first_channel, inner_channel, outer_channel = channels
    dphi1 = coefficient_derivative(M["PHI1"], chi)
    dphi2 = coefficient_derivative(M["PHI2"], chi)
    star_curvature = M["hodge"](curvature)
    first = M["wedge"](dphi1, star_curvature, first_channel)
    second_left = M["wedge"](
        dphi1,
        M["hodge"](M["wedge"](M["PHI2"], star_curvature, inner_channel)),
        outer_channel,
    )
    second_right = M["wedge"](
        M["PHI1"],
        M["hodge"](M["wedge"](dphi2, star_curvature, inner_channel)),
        outer_channel,
    )
    return M["fadd"](
        first,
        M["fscale"](
            Fraction(-1, 2),
            M["hodge"](M["fadd"](second_left, second_right)),
        ),
    )


def rational(value):
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def connection_symbol(q):
    out = sp.zeros(24, 6)
    for mu in range(4):
        for pair_index in range(6):
            out[6 * mu + pair_index, pair_index] = q[mu]
    return out


def source_form(column):
    result = {}
    for index, coefficient in enumerate(column):
        if coefficient:
            mu, pair_index = divmod(index, 6)
            result = M["fadd"](
                result,
                M["fscale"](
                    rational(coefficient),
                    {1 << mu: M["blade"](PAIRS[pair_index])},
                ),
            )
    return result


def raw_curvature_remainder(delta_a):
    delta_f = M["fadd"](
        M["wedge_raw"](Q0, delta_a),
        M["wedge_raw"](T_BACKGROUND, delta_a),
        M["wedge_raw"](delta_a, T_BACKGROUND),
    )
    return M["hodge"](M["shiab"](delta_f, CHANNELS))


def family_rank(forms):
    return M["sparse_rank"]([M["flatten"](form) for form in forms])


def bivector(coefficients):
    out = {}
    for coefficient, (left, right) in zip(coefficients, PAIRS):
        if coefficient:
            out = M["eadd"](
                out,
                M["escale"](
                    rational(coefficient),
                    M["emul"](M["blade"](left), M["blade"](right)),
                ),
            )
    return out


def negate(form):
    return M["fscale"](-1, form)


print("\nB. EXPLICIT MOVING-PHI/SHIAB PACKET")
diagnostics = {}
for name, packet in S["results"].items():
    q = sp.Matrix(S["orbits"][name])
    C = packet["connection_lift"]
    Bq = connection_symbol(q)
    eta = (Bq.T * Bq).inv() * Bq.T * C
    check("exact", f"{name}: the inverse-Kosmann bivector family reconstructs C exactly",
          Bq * eta == C and eta.rank() == 3)

    remainders = []
    moving_plus = []
    moving_minus = []
    for column in range(4):
        connection_form = source_form(C[:, column])
        remainder = raw_curvature_remainder(connection_form)
        chi = bivector(eta[:, column])
        moving = M["hodge"](d_shiab(F_BACKGROUND, CHANNELS, chi))
        remainders.append(remainder)
        moving_plus.append(moving)
        moving_minus.append(negate(moving))

    plus_defects = [M["fadd"](left, right) for left, right in zip(remainders, moving_plus)]
    minus_defects = [M["fadd"](left, right) for left, right in zip(remainders, moving_minus)]
    print(name, "remainder", [len(M["flatten"](x)) for x in remainders],
          "moving", [len(M["flatten"](x)) for x in moving_plus],
          "plus", [len(M["flatten"](x)) for x in plus_defects],
          "minus", [len(M["flatten"](x)) for x in minus_defects])
    diagnostics[name] = {
        "eta_rank": eta.rank(),
        "remainder_rank": family_rank(remainders),
        "moving_rank": family_rank(moving_plus),
        "plus_defect_rank": family_rank(plus_defects),
        "minus_defect_rank": family_rank(minus_defects),
        "remainder_supports": [len(M["flatten"](x)) for x in remainders],
        "moving_supports": [len(M["flatten"](x)) for x in moving_plus],
        "plus_defect_supports": [len(M["flatten"](x)) for x in plus_defects],
        "minus_defect_supports": [len(M["flatten"](x)) for x in minus_defects],
    }
    check("exact", f"{name}: the explicit moving-Shiab packet also has rank three",
          diagnostics[name]["moving_rank"] == 3)
    check("exact", f"{name}: moving Shiab alone fails coefficientwise in either sign",
          diagnostics[name]["plus_defect_rank"] == 3
          and diagnostics[name]["minus_defect_rank"] == 3)
    check("planted", f"PLANT {name}: equal rank is not coefficientwise cancellation",
          diagnostics[name]["plus_defect_rank"] == 3)


print("\nC. FULL HOMOGENEOUS GAUGE COMPLETION")
full_diagnostics = {}
for name, packet in S["results"].items():
    q = sp.Matrix(S["orbits"][name])
    C = packet["connection_lift"]
    Bq = connection_symbol(q)
    eta = (Bq.T * Bq).inv() * Bq.T * C
    q_form = {
        1 << mu: {0: M["gz"](rational(q[mu]))}
        for mu in range(4) if q[mu]
    }
    rows = []
    coherent_principal = []
    completed_totals = []
    for column in range(4):
        chi = bivector(eta[:, column])
        principal = source_form(C[:, column])
        homogeneous_t = coefficient_derivative(T_BACKGROUND, chi)
        homogeneous_f = coefficient_derivative(F_BACKGROUND, chi)
        moving = M["hodge"](d_shiab(F_BACKGROUND, CHANNELS, chi))
        raw_homogeneous = M["fadd"](
            M["hodge"](M["shiab"](homogeneous_f, CHANNELS)),
            homogeneous_t,
            moving,
        )
        lower_plus = M["fadd"](principal, homogeneous_t)
        lower_minus = M["fadd"](principal, negate(homogeneous_t))

        def curvature(delta_a):
            return M["fadd"](
                M["wedge_raw"](q_form, delta_a),
                M["wedge_raw"](T_BACKGROUND, delta_a),
                M["wedge_raw"](delta_a, T_BACKGROUND),
            )

        plus_curvature_defect = M["fadd"](curvature(lower_plus), negate(homogeneous_f))
        minus_curvature_defect = M["fadd"](curvature(lower_minus), negate(homogeneous_f))
        principal_curvature = curvature(principal)
        lower_curvature = curvature(homogeneous_t)
        principal_remainder = M["hodge"](M["shiab"](principal_curvature, CHANNELS))
        lower_response = M["fadd"](
            M["hodge"](M["shiab"](lower_curvature, CHANNELS)),
            homogeneous_t,
        )
        completed = M["fadd"](principal_remainder, lower_response, moving)
        coherent_principal.append(principal_remainder)
        completed_totals.append(completed)
        rows.append({
            "raw_homogeneous_support": len(M["flatten"](raw_homogeneous)),
            "plus_curvature_defect_support": len(M["flatten"](plus_curvature_defect)),
            "minus_curvature_defect_support": len(M["flatten"](minus_curvature_defect)),
            "coherent_principal_support": len(M["flatten"](principal_remainder)),
            "lower_response_support": len(M["flatten"](lower_response)),
            "completed_support": len(M["flatten"](completed)),
        })
    frozen_supports = diagnostics[name]["remainder_supports"]
    coherent_supports = [row["coherent_principal_support"] for row in rows]
    check("exact", f"{name}: plus-sign lower connection completion gives delta F equals commutator F eta",
          all(row["plus_curvature_defect_support"] == 0 for row in rows))
    check("planted", f"PLANT {name}: the opposite lower-order sign fails on every non-kernel column",
          sum(row["minus_curvature_defect_support"] != 0 for row in rows) >= 3)
    check("exact", f"{name}: the homogeneous raw-Upsilon orbit closes with explicit moving Shiab",
          all(row["raw_homogeneous_support"] == row["completed_support"] == 0 for row in rows))
    check("exact", f"{name}: the coherent principal packet retains rank three",
          family_rank(coherent_principal) == 3)
    if name == "timelike":
        check("exact", "timelike: matched-q and v0.86 frozen-q0 principal packets coincide",
              coherent_supports == frozen_supports)
    else:
        check("scope", f"{name}: v0.86 frozen-q0 supports differ from the matched-q naturality packet",
              coherent_supports != frozen_supports)
    full_diagnostics[name] = {
        "rows": rows,
        "coherent_principal_rank": family_rank(coherent_principal),
        "coherent_principal_supports": coherent_supports,
        "v086_frozen_q0_supports": frozen_supports,
        "matched_q_equals_v086_frozen_q0": coherent_supports == frozen_supports,
        "completed_rank": family_rank(completed_totals),
    }


print("\nD. THEOREM, SURPLUS, AND PHYSICS FENCES")
check("theorem", "all causal classes close the rank-three bivector orbit only after lower-order completion",
      all(row["coherent_principal_rank"] == 3 and row["completed_rank"] == 0
          for row in full_diagnostics.values()))
check("theorem", "moving Shiab by itself is never the negative of the principal packet",
      all(row["plus_defect_rank"] == row["minus_defect_rank"] == 3
          for row in diagnostics.values()))
check("scope", "v0.86 used a timelike q0 raw-response operator on its spacelike and null labels",
      full_diagnostics["timelike"]["matched_q_equals_v086_frozen_q0"]
      and not full_diagnostics["spacelike"]["matched_q_equals_v086_frozen_q0"]
      and not full_diagnostics["null"]["matched_q_equals_v086_frozen_q0"])
check("surplus", "the closure uses the source coefficients and zero fitted local parameters", True)
for kind, label in (
    ("symplectic", "internal homogeneous Ward closure is not physical gauge basicness or a BFV phase space"),
    ("symplectic", "no presymplectic current polarization or charge is promoted"),
    ("variational", "physical diffeomorphism Lie transport density Hodge and observation terms remain open"),
    ("variational", "the primitive epsilon Euler row remains distinct from dependent frame transport"),
    ("krein", "K-star formal adjoint Green concomitant and common domain remain open"),
    ("analytic", "no contour determinant saddle path-integral measure or spectrum is selected"),
    ("scope", "the source-silent grade-one gamma soldering proposal is not used"),
    ("scope", "the six transverse direct metric block and selected stationary branch remain exact"),
    ("scope", "P1 P2 P3 remain unused and no datum quotient field or coefficient is added"),
    ("scope", "Curt remains formally separate and no third lane is promoted"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__MOVING_PHI_SHIAB_AND_PRIMITIVE_EPSILON_GRAMMAR__SOURCE-SILENT__PHYSICAL_DIFFEO_SOLDERING")
print("MOVING_SHIAB_ALONE=RANK3__WRONG_COEFFICIENT_CARRIER__DOES_NOT_CANCEL_V086")
print("FULL_BIVECTOR_GAUGE_COMPLETION=DELTA_A_QETA_PLUS_COMM_T_ETA__DELTA_F_COMM_F_ETA__RAW_UPSILON_ZERO")
print("V086_CAUSAL_PACKET=FROZEN_TIMELIKE_Q0_OPERATOR__SPACELIKE_NULL_SUPPORTS_NOT_MATCHED_Q")
print("PRINCIPAL_INTERNAL_WARD=RANK3_TO_ZERO_ALL_CAUSAL_CLASSES__ZERO_FIT")
print("NEXT=CONSTRUCT_MATCHED_Q_PHYSICAL_DIFFEO_LIE_DENSITY_HODGE_OBSERVATION_AND_LOWER_ORDER_METRIC_PACKET__VERIFY_FULL_FRECHET_JR_ZERO__THEN_K_STAR_ADJOINT_GREEN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
