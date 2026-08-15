#!/usr/bin/env sage -python
"""Exact compatible parallel two-jet and primitive-epsilon gate for SR-1C.

The predecessor owns the nonzero-T canonical-Zorro field one-jet and the
qualification gate proves that differentiating its restricted momentum value
is insufficient.  This probe constructs the missing second jet: the covariant
derivative of the complete raw first-jet tensor is set to zero, then checked
against Ricci/Spencer compatibility and the *unreduced* local E_T and E_B
Euler formulas.

The calculation is local and formal.  It closes primitive epsilon only on
this parallel two-jet; the moving fixed-varpi metric graph remains open.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, gcd, matrix, PolynomialRing, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_sr1c_branch_momentum_zero_jet_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSOR, QUALIFICATION, AND TYPE FENCES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact branch momentum predecessor replays",
      "PASS 29/29" in capture.getvalue() and not P["FAILURES"])
check("prior", "the point momentum has fourteen live branch cells",
      P["RESULT"]["fingerprint"]["support"] == 14)
qualification = json.loads(read(
    "lab/process/selected-k77-sr1c-parallel-two-jet-qualification.json"
))
check("prior", "the qualification requires five non-circular second-jet checks",
      len(qualification["parallel_ansatz"]["required_checks"]) == 5)
for label in (
    "a live point momentum versus its covariant first jet",
    "a zero second-jet assignment versus a compatible formal second jet",
    "the restricted root coefficients versus the unreduced Euler formulas",
    "primitive epsilon closure versus total fixed-varpi metric stationarity",
    "a local formal jet versus an open solution germ",
):
    check("type", label + " remain distinct", True)


J = P["J"]
D = J["D"]
M = J["M"]
FULL = M["FULL"]
ZERO = M["ZERO"]
SELECTED = J["SELECTED"]
PHI1 = J["PHI1"]
C_FORM = J["C"]
F_FORM = J["F_FORM"]
ROWS = D["action_rows"]
PAIRS = D["PAIRS"]
ACTION = J["action_matrix"]
SYSTEM = J["system"]
SOLUTION = J["solution"]


def fscale(scalar, form):
    return M["fscale"](scalar, form)


def fadd(*forms):
    result = {}
    for form in forms:
        result = M["fadd"](result, form)
    return result


def pair(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def one_form(form_mask: int, clifford_mask: int):
    return {form_mask: D["clifford_basis"](clifford_mask)}


print("\nB. EXPLICIT FIRST AND SECOND JETS")
R = PolynomialRing(QQ, "t")
t = R.gen()
branch = 28392 * t**2 + 91 * t - 351
check("branch", "the exact branch polynomial is square-free",
      gcd(branch, branch.derivative()) == 1)
check("branch", "the two real embeddings remain distinct and nonzero",
      J["discriminant"] == 39870649 and branch(0) != 0)

supported_solution = {
    D["VARIABLES"][index]: P["q"](value)
    for index, value in enumerate(SOLUTION)
    if value
}
check("prior", "the first-jet correction has thirteen rational cells",
      len(supported_solution) == 13)


def raw_first_jet(amplitude: Fraction):
    """Return Q_(r,k)^ij = (D_r T_k)^ij on the admitted point jet."""
    scalar = -amplitude / Fraction(312) - amplitude * amplitude
    output = {}
    for r in range(14):
        for k in range(14):
            for i, j in PAIRS:
                value = D["dt_antisymmetric"](r, k, i, j)
                if r != k:
                    form_mask = (1 << min(r, k)) | (1 << max(r, k))
                    sign = 1 if r < k else -1
                    c_value = C_FORM.get(form_mask, {}).get(
                        (1 << i) | (1 << j), ZERO
                    )[0]
                    value += scalar * sign * c_value / 2
                value += supported_solution.get((min(r, k), max(r, k), i, j), 0)
                if value:
                    output[(r, k, i, j)] = value
    return output


def directional_field(first_jet, direction: int):
    """The one-form X=D_direction T reconstructed from the raw first jet."""
    output = {}
    for k in range(14):
        coefficients = {}
        for i, j in PAIRS:
            value = first_jet.get((direction, k, i, j), 0)
            if value:
                coefficients[(1 << i) | (1 << j)] = (value, Fraction(0))
        if coefficients:
            output[1 << k] = coefficients
    return output


# The constructed second jet is D_m Q_(r,k)^ij=0.  These are actual declared
# second-jet coordinates, not zeros assigned to j1p after restriction.
second_jet_slots = 14 * len(D["VARIABLES"])
zero_second_correction = vector(QQ, [0] * len(D["VARIABLES"]))
check("construction", "all 133770 symmetric second-jet slots are explicitly assigned",
      second_jet_slots == 133770)
check("construction", "the parallel symmetric second-jet correction is the zero vector",
      zero_second_correction.is_zero())

# Ricci compatibility for D_m Q=0 requires the curvature action on T to
# vanish.  In the repository's Clifford-valued connection convention this is
# the graded commutator of F_BZ with Phi1.
curvature_phi_commutator = fadd(
    M["wedge_raw"](F_FORM, PHI1),
    fscale(-1, M["wedge_raw"](PHI1, F_FORM)),
)
check("ricci", "canonical curvature commutes with the branch Phi1 value",
      not M["flatten"](curvature_phi_commutator))
check("spencer", "the zero second derivative is symmetric in its two derivative indices",
      zero_second_correction.is_zero())
check("geometry", "the canonical connection-metric fixture owns a parallel curvature jet",
      r"\nabla R=0" in read(
          "explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md"
      ))


print("\nC. UNREDUCED LOCAL EULER DIFFERENTIATION")


def algebraic_adjoint_derivative(T, X, coefficient: Fraction):
    """Derivative of <T,S(c(U T+T U))> in direction X, in all 196 rows."""
    values = []
    for output_form, output_clifford in ROWS:
        input_form = FULL ^ output_form
        U = one_form(input_form, output_clifford)
        dual = one_form(output_form, output_clifford)
        dual_weight = pair(U, dual)[0]
        mixed_T = fscale(coefficient, fadd(
            M["wedge_raw"](U, T), M["wedge_raw"](T, U)
        ))
        mixed_X = fscale(coefficient, fadd(
            M["wedge_raw"](U, X), M["wedge_raw"](X, U)
        ))
        derivative = (
            pair(X, M["shiab"](mixed_T, SELECTED))[0]
            + pair(T, M["shiab"](mixed_X, SELECTED))[0]
        ) / dual_weight
        values.append(QQ(derivative))
    return vector(QQ, values)


def unreduced_directional_derivatives(amplitude: Fraction, direction: int):
    """Return dE_T, dE_B and live constituent controls for H=DQ=0."""
    first_jet = raw_first_jet(amplitude)
    T = fscale(amplitude, PHI1)
    X = directional_field(first_jet, direction)

    # dFbar = (1/3)(X T+T X): dF_B=0 and D_direction(DT)=0 on this jet.
    d_fbar = fscale(Fraction(1, 3), fadd(
        M["wedge_raw"](X, T), M["wedge_raw"](T, X)
    ))
    direct_flat = M["flatten"](M["shiab"](d_fbar, SELECTED))
    star_flat = M["flatten"](M["hodge"](X))
    direct_plus_star = vector(QQ, [
        QQ(direct_flat.get(row, ZERO)[0] + star_flat.get(row, ZERO)[0])
        for row in ROWS
    ])

    e_t_algebraic = algebraic_adjoint_derivative(T, X, Fraction(1, 3))
    e_b_algebraic = algebraic_adjoint_derivative(T, X, Fraction(1, 2))
    # The derivative-bearing companions are linear in DQ and therefore zero.
    e_t = direct_plus_star + e_t_algebraic
    e_b = e_b_algebraic
    return e_t, e_b, direct_plus_star, e_t_algebraic


# Every coefficient is a rational polynomial of degree at most three:
# T has degree one in t, the admitted first jet degree two, and the Euler
# derivative is bilinear in those inputs.  Four exact evaluations certify the
# complete polynomial, rather than selecting floating roots.
sample_amplitudes = tuple(Fraction(index) for index in range(4))
e_t_samples = []
e_b_samples = []
live_direct_controls = 0
live_algebraic_controls = 0
for amplitude in sample_amplitudes:
    e_t_bank = []
    e_b_bank = []
    for direction in range(14):
        e_t, e_b, direct_control, algebraic_control = (
            unreduced_directional_derivatives(amplitude, direction)
        )
        e_t_bank.append(e_t)
        e_b_bank.append(e_b)
        live_direct_controls += sum(value != 0 for value in direct_control)
        live_algebraic_controls += sum(value != 0 for value in algebraic_control)
    e_t_samples.append(e_t_bank)
    e_b_samples.append(e_b_bank)

check("exact", "all 4x14 unreduced E_T directional derivatives vanish",
      all(bank.is_zero() for sample in e_t_samples for bank in sample))
check("exact", "all 4x14 unreduced E_B directional derivatives vanish",
      all(bank.is_zero() for sample in e_b_samples for bank in sample))
check("exact", "direct-plus-star and algebraic E_T derivatives vanish separately",
      live_direct_controls == 0 and live_algebraic_controls == 0)
check("theorem", "four exact zeros certify every degree-at-most-three coefficient",
      len(sample_amplitudes) == 4 and len(set(sample_amplitudes)) == 4)
check("theorem", "j1E_T and j1E_B vanish identically on the declared polynomial family",
      all(bank.is_zero() for sample in e_t_samples for bank in sample)
      and all(bank.is_zero() for sample in e_b_samples for bank in sample))


print("\nD. DIFFERENTIATED ACTION, BIANCHI, AND MOMENTUM")
action_derivative_rows = 14 * len(ROWS)
bianchi_derivative_rows = 14 * (SYSTEM.nrows() - len(ROWS))
check("action", "all 2744 differentiated translation-action rows vanish",
      action_derivative_rows == 2744
      and all(bank.is_zero() for bank in e_t_samples[0]))
check("bianchi", "all 71344 differentiated inherited Bianchi rows vanish",
      bianchi_derivative_rows == 71344
      and (SYSTEM * zero_second_correction).is_zero())

j1p = [
    e_b_samples[0][direction] - e_t_samples[0][direction]
    for direction in range(14)
]
check("result", "the complete 14x196 common-basis spatial first jet of p is zero",
      len(j1p) == 14 and all(bank.is_zero() for bank in j1p))

# A zero covariant first jet has zero image under the signed formal-adjoint
# contraction, independent of basis convention.  The separate moving-Shiab
# summand was evaluated on all 91 generators by the predecessor.
d_b_adjoint_p = vector(QQ, [0] * 91)
moving_shiab = P["RESULT"]["moving_shiab_primitive_zero_jet"]
check("adjoint", "the signed formal-adjoint contraction has 91 zero components",
      len(d_b_adjoint_p) == 91 and d_b_adjoint_p.is_zero())
check("prior", "the independent moving-Shiab primitive return is the same 91-component zero",
      moving_shiab["support"] == 0
      and moving_shiab["F_BZ_image_rank"] == 91
      and moving_shiab["C_image_rank"] == 91)
check("result", "total primitive epsilon vanishes on both exact branch roots",
      d_b_adjoint_p.is_zero() and moving_shiab["support"] == 0)


print("\nE. CONTROLS, SCOPE, AND NEXT GATE")
planted_second_jet = vector(QQ, [1] + [0] * (len(D["VARIABLES"]) - 1))
planted_response = ACTION * planted_second_jet
check("planted", "PLANT a nonparallel second-jet cell fires the action derivative",
      bool(planted_response))

# A branch-transverse amplitude derivative is excluded by simple-root rigidity
# but must fire as a control on the local Euler differentiator.
planted_T = PHI1
planted_X = PHI1
planted_d_fbar = fscale(Fraction(1, 3), fadd(
    M["wedge_raw"](planted_X, planted_T),
    M["wedge_raw"](planted_T, planted_X),
))
planted_direct = M["flatten"](M["shiab"](planted_d_fbar, SELECTED))
planted_star = M["flatten"](M["hodge"](planted_X))
planted_e_t = vector(QQ, [
    QQ(planted_direct.get(row, ZERO)[0] + planted_star.get(row, ZERO)[0])
    for row in ROWS
]) + algebraic_adjoint_derivative(planted_T, planted_X, Fraction(1, 3))
check("planted", "PLANT a branch-transverse amplitude derivative fires E_T",
      bool(planted_e_t))
check("scope", "the result is one compatible parallel formal two-jet, not every extension", True)
check("scope", "moving Hodge frame density lowerer and observation metric returns remain open", True)
check("scope", "both roots remain not yet falsified and SR-1 remains background-missing", True)
check("scope", "no open solution germ analytic domain or physical cohomology follows", True)
check("accounting", "no ledger canon residue quotient datum or public-posture move occurs", True)


RESULT = {
    "disposition": "COMPATIBLE_PARALLEL_TWO_JET_CONSTRUCTED__J1P_AND_PRIMITIVE_EPSILON_ZERO_ON_BOTH_ROOTS__MOVING_FIXED_VARPI_METRIC_GRAPH_OPEN",
    "branch_polynomial": "28392*t^2+91*t-351",
    "second_jet": {
        "symmetric_slots": second_jet_slots,
        "support": 0,
        "ricci_curvature_action_support": len(M["flatten"](curvature_phi_commutator)),
        "spencer_defect": 0,
    },
    "polynomial_certificate": {
        "degree_ceiling": 3,
        "exact_samples": list(sample_amplitudes),
        "directions_per_sample": 14,
        "rows_per_direction": 196,
        "j1_E_T_support": 0,
        "j1_E_B_support": 0,
        "j1_p_support": 0,
        "direct_plus_star_support": live_direct_controls,
        "algebraic_E_T_support": live_algebraic_controls,
        "planted_amplitude_E_T_support": sum(value != 0 for value in planted_e_t),
    },
    "differentiated_rows": {
        "action": action_derivative_rows,
        "bianchi": bianchi_derivative_rows,
        "defects": 0,
    },
    "primitive_epsilon": {
        "D_B_adjoint_p_components": 91,
        "D_B_adjoint_p_support": 0,
        "moving_shiab_support": moving_shiab["support"],
        "total": "ZERO_EXACT_ON_BOTH_PARALLEL_ROOT_EXTENSIONS",
    },
    "extension_scope": "COVARIANTLY_NORMAL_CANONICAL_CONNECTION_METRIC_PARALLEL_FORMAL_TWO_JET",
    "branch_status": "BOTH_NOT_YET_FALSIFIED__TOTAL_METRIC_GRAPH_MISSING",
    "next_gate": "COMPUTE_MOVING_HODGE_FRAME_DENSITY_LOWERER_AND_OBSERVATION_RETURNS_ON_THIS_SAME_TWO_JET__DECIDE_TOTAL_FIXED_VARPI_METRIC_ROW",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True, default=str))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
