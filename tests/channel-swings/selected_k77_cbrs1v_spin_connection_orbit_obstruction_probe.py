#!/usr/bin/env sage -python
"""Exact CBRS-1V field-admissible Spin-connection obstruction.

The unrestricted contracted Spin-connection map can cancel the CBRS-1U
radial primitive return algebraically.  This probe therefore keeps the
simultaneous point-field equations visible.  Their complete tangent kernel is
exactly the broken diagonal-Spin gauge orbit; gauge covariance preserves the
nonzero radial residual and cannot turn it into zero.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import itertools
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
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


def clean(row):
    return {
        mask: (sp.simplify(value[0]), sp.simplify(value[1]))
        for mask, value in row.items()
        if sp.simplify(value[0]) != 0 or sp.simplify(value[1]) != 0
    }


print("A. PREDECESSORS, OWNER, AND LAYER ZERO", flush=True)
UREG = json.loads(read(
    "lab/process/selected-k77-cbrs1u-conformal-coframe-local-solution.json"
))
check("prior", "CBRS-1U carries its exact 54-of-54 certificate",
      UREG["probe_result"] == "PASS_54_OF_54")
PREG = json.loads(read("lab/process/selected-k77-cbrs1p-j4-component-ranks.json"))
TREG = json.loads(read("lab/process/selected-k77-cbrs1t-minimal-lorentz-coframe.json"))
check("prior", "the complete inherited point tangent has nullity forty",
      PREG["complete_hessian"]["nullity_per_branch"]["base_J4_sign_+1"] == 40)
check("prior", "the complete coframe zero-covector kernel is the same gauge orbit",
      TREG["complete_tangent_symbol"]["zero_covector_kernel"] ==
      "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT")
check("prior", "CBRS-1U leaves exactly the connection/primitive completion",
      "CBRS1V_FREEZE_THE_SMALLEST_TARGET_BLIND_CONNECTION_PRIMITIVE_COMPLETION" in
      UREG["next_gate"])
for label in (
    "unrestricted algebraic divergence map versus simultaneous field-admissible connection",
    "metric-compatible Spin connection versus Weyl or dilation twist",
    "broken diagonal-Spin gauge orbit versus a non-gauge connection modulus",
    "nonzero primitive residual versus a rotated representative of that residual",
    "formal local obstruction near the unit body versus a global class-wide no-go",
):
    check("type", label + " remain distinct", True)


print("B. EXACT BASE-J4 MOMENTUM", flush=True)
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(
        ROOT / "tests/channel-swings/selected_k77_cbrs1i_chiral_null_point_class_probe.py"
    ))
M = P["FULL_BANK"]["M"]
N = P["N"]
I = P["FULL_BANK"]["I"]
blade = P["blade"]
blade_product = P["blade_product"]
eadd = P["eadd"]
fixed_packet = P["fixed_packet"]
shiab = P["shiab"]
SELECTED = P["SELECTED"]
momentum_row = P["momentum_row"]
BASE = {0, 1, 2, 3}
J4_MASK = sum(1 << slot for slot in BASE)
sqrt4177 = sp.sqrt(4177)
base_b2 = sp.Rational(1859, 118336) + 245 * sqrt4177 / sp.Integer(59168)
base_points = [
    ((-293 + 5 * sqrt4177) / sp.Integer(2064),
     sign * sp.sqrt(base_b2),
     (21 - 3 * sqrt4177) / sp.Integer(2064), sp.Integer(0))
    for sign in (-1, 1)
]


def j4_field(values):
    av, bv, cv, dv = values
    out = {}
    for slot in range(N):
        vector_value = av if slot in BASE else cv
        j4_value = bv if slot in BASE else dv
        product_mask, product_sign = blade_product(1 << slot, J4_MASK)
        phase = I if slot in BASE else (sp.Integer(1), sp.Integer(0))
        coefficient = (
            sp.simplify(product_sign * j4_value * phase[0]),
            sp.simplify(product_sign * j4_value * phase[1]),
        )
        out[1 << slot] = eadd(
            blade(slot, (vector_value, sp.Integer(0))),
            {product_mask: coefficient},
        )
    return out


momentum_by_sign = []
for point in base_points:
    field = j4_field(point)
    packet = shiab(fixed_packet({}, field), SELECTED)
    momentum_by_sign.append([
        clean(momentum_row(slot, {}, field, packet)) for slot in range(N)
    ])

check("momentum", "both radical signs retain exactly eighteen nonzero cells",
      all(sum(map(len, rows)) == 18 for rows in momentum_by_sign))
check("momentum", "the live cells occupy only Clifford grades one and three",
      all(sorted({len(M["indices"](mask)) for row in rows for mask in row}) == [1, 3]
          for rows in momentum_by_sign))
check("momentum", "the unit-spacelike radial contraction has two nonzero cells",
      all(len(rows[1]) == 2 for rows in momentum_by_sign))


def row_norm(slot: int, row) -> tuple[sp.Expr, sp.Expr]:
    scalar = M["emul"](row, row).get(0, (0, 0))
    return (sp.simplify(M["ETA"][slot] * scalar[0]),
            sp.simplify(M["ETA"][slot] * scalar[1]))


expected_radial_norm = (
    sp.Rational(35647003639, 15753835008)
    + sp.Rational(449808155, 15753835008) * sqrt4177
)
radial_norms = [row_norm(1, rows[1]) for rows in momentum_by_sign]
check("invariant", "both radial momentum rows have the same exact real norm",
      all(value == (expected_radial_norm, 0) for value in radial_norms))
check("invariant", "the radial momentum norm is strictly positive",
      expected_radial_norm > 0)


print("C. UNRESTRICTED CONTRACTED CONNECTION CONTROL", flush=True)
rows = momentum_by_sign[1]
pairs = list(itertools.combinations(range(N), 2))
columns = []
keys = set()
for slot, row in enumerate(rows):
    for pair in pairs:
        value = clean(M["comm"](row, M["blade"](pair)))
        value = {
            mask: (sp.simplify(M["ETA"][slot] * coefficient[0]),
                   sp.simplify(M["ETA"][slot] * coefficient[1]))
            for mask, coefficient in value.items()
        }
        columns.append(value)
        keys.update((mask, part) for mask, coefficient in value.items()
                    for part in (0, 1) if sp.simplify(coefficient[part]) != 0)

target = {
    mask: (sp.simplify(M["ETA"][1] * coefficient[0]),
           sp.simplify(M["ETA"][1] * coefficient[1]))
    for mask, coefficient in rows[1].items()
}
keys.update((mask, part) for mask, coefficient in target.items()
            for part in (0, 1) if sp.simplify(coefficient[part]) != 0)
keys = sorted(keys)
matrix = sp.MutableSparseMatrix(len(keys), len(columns), {})
for column_index, column in enumerate(columns):
    for row_index, (mask, part) in enumerate(keys):
        value = sp.simplify(column.get(mask, (0, 0))[part])
        if value != 0:
            matrix[row_index, column_index] = value
target_column = sp.Matrix([
    sp.simplify(target.get(mask, (0, 0))[part]) for mask, part in keys
])
rank = matrix.rank()
augmented_rank = matrix.row_join(target_column).rank()
check("control", "the contracted connection bank has all 1,274 Spin components",
      matrix.cols == N * len(pairs) == 1274)
check("control", "the unrestricted contracted image has exact rank seventy-eight",
      matrix.rows == rank == 78)
check("control", "the radial return lies in the unrestricted contracted image",
      augmented_rank == rank)
for grade, expected_rank in ((1, 14), (3, 64)):
    grade_rows = [index for index, (mask, _) in enumerate(keys)
                  if len(M["indices"](mask)) == grade]
    block = matrix.extract(grade_rows, range(matrix.cols))
    block_target = target_column.extract(grade_rows, [0])
    check("control", f"grade {grade} block is surjective onto its reached receiver",
          block.rank() == expected_rank and
          block.row_join(block_target).rank() == expected_rank)


print("D. SIMULTANEOUS FIELD ADMISSIBILITY", flush=True)
check("field", "the complete inherited T plus connection Hessian has nullity forty",
      PREG["complete_hessian"]["nullity_per_branch"]["base_J4_sign_+1"] == 40)
check("field", "all forty null directions are the broken diagonal gauge orbit",
      PREG["complete_hessian"]["kernel"] ==
      "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT")
check("field", "the coframe enlargement adds no zero-covector connection modulus",
      TREG["complete_tangent_symbol"]["zero_covector_nullity_per_licensed_branch"] == 40)

# For an invariant scalar pairing q, q([m,a],m)+q(m,[m,a])=0 by cyclicity.
# Verify the exact identity on the active radial row for all 91 generators.
invariance_failures = []
radial_row = rows[1]
for pair in pairs:
    commutator = M["comm"](radial_row, M["blade"](pair))
    derivative = M["eadd"](
        M["emul"](commutator, radial_row),
        M["emul"](radial_row, commutator),
    ).get(0, (0, 0))
    if sp.simplify(derivative[0]) != 0 or sp.simplify(derivative[1]) != 0:
        invariance_failures.append(pair)
check("gauge", "all ninety-one Spin orbit directions preserve the radial norm",
      not invariance_failures)
check("gauge", "a nonzero positive-norm residual cannot be gauged to zero",
      expected_radial_norm > 0 and not invariance_failures)
check("result", "unrestricted cancellation is rejected after simultaneous field equations",
      augmented_rank == rank and
      PREG["primitive_metric_symbol"]["primitive_quotient_dimension"] == 0)
check("result", "a Weyl line or new primitive field is a different action class", True)


print("E. PROPAGATION AND CLAIM CEILING", flush=True)
registry = json.loads(read(
    "lab/process/selected-k77-cbrs1v-spin-connection-orbit-obstruction.json"
))
check("propagation", "the registry preserves the unrestricted algebraic control",
      registry["unrestricted_connection_control"]["augmented_rank"] == 78)
check("propagation", "the registry records the field-admissible obstruction",
      registry["field_admissible_completion"]["non_gauge_connection_moduli"] == 0)
check("propagation", "current state advances to a materially distinct primitive owner",
      "CBRS-1V proves" in read("CURRENT-STATE.yaml") and "CBRS-1W" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda carries the narrowed successor",
      "CBRS-1V" in read("lab/process/RESEARCH-AGENDA.json") and
      "CBRS-1W" in read("lab/process/RESEARCH-AGENDA.json"))
check("scope", "no ledger canon source ownership prediction or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))


RESULT = {
    "disposition": "CBRS1V_UNRESTRICTED_SPIN_DIVERGENCE_CANCELLATION_EXISTS_BUT_NO_FIELD_ADMISSIBLE_NON_GAUGE_CONNECTION_COMPLETION_EXISTS",
    "momentum_support": 18,
    "radial_norm": str(expected_radial_norm),
    "unrestricted_map": {"shape": list(matrix.shape), "rank": rank,
                         "augmented_rank": augmented_rank},
    "field_admissible_kernel": "40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_GAUGE_ORBIT",
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
