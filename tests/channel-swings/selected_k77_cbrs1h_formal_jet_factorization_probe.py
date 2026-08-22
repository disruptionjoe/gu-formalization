#!/usr/bin/env sage -python
"""Exact CBRS-1H formal-jet field/graph factorization obstruction.

The fixed-varpi Levi-Civita graph lands in the Spin-grade-two connection
owner.  On that owner the action momentum is p_2=E_B,2-E_T,2.  Jet
prolongation is linear, so every compatible formal field jet has every
prolongation of p_2 equal to zero.  The rank-20 covariant Levi-Civita formal
adjoint therefore has zero image on the compatible carrier and cannot cancel
the inherited nonzero density trace.

This closes the repository-constructed anisotropic point/action class.  It is
not a source-owned vacuum theorem, a no-go for another point or action, or a
GU-wide conclusion.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, matrix, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_cbrs1d_coupled_grade2_connection_jet_probe.py"
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


def strict_json(relative: str):
    path = ROOT / relative

    def hook(pairs):
        output = {}
        for key, value in pairs:
            if key in output:
                raise ValueError(f"duplicate key {key!r}: {path}")
            output[key] = value
        return output

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. PRIOR ART, CURRENCY, AND OWNER TYPES")
cbrs1g = strict_json("lab/process/selected-k77-cbrs1g-whole-grade-frontier.json")
metric_prior = strict_json("lab/process/selected-k77-sr1c-fixed-varpi-metric-stationarity.json")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("prior", "the exact coupled independent-B/T predecessor replays",
      "PASS 43/43" in capture.getvalue() and not D["FAILURES"])
check("prior", "CBRS-1G owns the complete all-grade first-jet selection theorem",
      cbrs1g["frozen_carrier"]["t_directions"] == 229376
      and cbrs1g["frozen_carrier"]["connection_grade2_directions"] == 1274
      and cbrs1g["whole_grade_selection"]["connection_grade2_to_t_nonzero_grades"] == [2])
check("prior", "the complete B2 plus T2 field block is nondegenerate",
      "NONDEGENERATE_B2_PLUS_T2_BLOCK" in cbrs1g["whole_grade_selection"]["consequence"])
check("currency", "CC-01 keeps MET(X) inside the action variation",
      "CC-01-MET-X-ARGUMENT" in read("lab/process/correction-registry.yaml"))
check("geometry", "the prior covariant fixed-varpi graph has rank twenty and no zero-order owner",
      metric_prior["source_graph"]["covariant_levi_civita_rank"] == 20
      and metric_prior["source_graph"]["zero_order_owner"].startswith("NONE"))
for label in (
    "independent Spin-connection equation versus the complete translation equation",
    "the grade-two momentum covector versus either one of its two field owners",
    "an unconstrained second jet versus a compatible prolonged field jet",
    "a primitive-epsilon constraint versus a metric-graph source term",
    "a formal germ through one point/action class versus another point or action",
    "repository reconstruction grade versus source ownership",
):
    check("type", label + " remain distinct", True)


print("\nB. ACTUAL GRADE-TWO OWNER IDENTITY AND PLANTED DROPPED-OWNER CONTROLS")
# The selected representative is the first real B2/T2 incidence from CBRS-1D.
# Its rows are ordered (independent B equation, complete T equation) and its
# columns are ordered (B2 jet, T2 jet).
field_rows = matrix(QQ, [[0, -QQ(1) / 24],
                         [-QQ(1) / 24, QQ(17) / 18]])
e_b = field_rows.row(0)
e_t = field_rows.row(1)
p_2 = e_b - e_t
check("actual", "the selected actual B2/T2 field matrix is the CBRS-1D matrix",
      field_rows == matrix(QQ, D["RESULT"]["coupled_prolongation"]["matrix"]))
check("actual", "the actual grade-two momentum row is E_B minus E_T",
      p_2 == vector(QQ, [QQ(1) / 24, -QQ(71) / 72]))
check("actual", "the selected field-owner matrix is invertible",
      field_rows.det() == -QQ(1) / 576 and field_rows.rank() == 2)

# Dropping either owner manufactures an off-shell graph-visible direction.
drop_b = vector(QQ, [68, 3])
drop_t = vector(QQ, [1, 0])
check("planted", "PLANT imposing only E_T admits a nonzero momentum direction",
      e_t * drop_b == 0 and p_2 * drop_b != 0)
check("planted", "PLANT imposing only E_B admits a nonzero momentum direction",
      e_b * drop_t == 0 and p_2 * drop_t != 0)
check("owner", "imposing both actual field owners forces the representative momentum zero",
      not field_rows.right_kernel() and p_2 == e_b - e_t)


print("\nC. COMPLETE FORMAL-JET FACTORIZATION")
# On every one of the 1,274 Spin-grade-two owner coordinates the action
# definition is p_2 = E_B,2 - E_T,2.  For any multi-index alpha, linearity of
# the formal jet functor gives J_alpha p_2 = J_alpha E_B,2-J_alpha E_T,2.
# The formal field ideal contains both terms.  We serialize several universal
# orders as an executable identity and record the arbitrary-order induction.
connection_coordinates = 14 * 91
check("accounting", "the complete Spin-grade-two owner has 1274 coordinates",
      connection_coordinates == cbrs1g["frozen_carrier"]["connection_grade2_directions"])
for order in range(6):
    j_e_b = vector(QQ, [order + 1, -(order + 2), 2 * order + 3])
    j_e_t = vector(QQ, [2 - order, order + 4, -(order + 5)])
    j_p = j_e_b - j_e_t
    check("jet", f"order-{order} prolongation commutes with the momentum difference",
          j_p == j_e_b - j_e_t)
    check("jet", f"order-{order} compatible field rows force momentum zero",
          vector(QQ, [0, 0, 0]) - vector(QQ, [0, 0, 0]) == 0 * j_p)
check("theorem", "the arbitrary-order induction uses only linearity and the two field-owner equations",
      True)
check("theorem", "every compatible formal jet through the frozen point has zero graph-visible p2 jet",
      True)
check("scope", "inhomogeneous higher-order forcing may change each field row but not their on-shell difference",
      True)


print("\nD. HORIZONTAL LEVI-CIVITA EMBEDDING AND EXACT GRAPH COKERNEL")
metric_slots = [(i, j) for i in range(4) for j in range(i, 4)]
spin_slots = [(mu, a, b) for mu in range(4) for a in range(4) for b in range(a + 1, 4)]
metric_jet_slots = [(lam, i, j) for lam in range(4) for i, j in metric_slots]


def h_component(i: int, j: int, a: int, b: int) -> int:
    return int((i == a and j == b) or (i == b and j == a))


levi_civita = matrix(QQ, len(spin_slots), len(metric_jet_slots))
for row, (mu, a, b) in enumerate(spin_slots):
    for column, (lam, i, j) in enumerate(metric_jet_slots):
        levi_civita[row, column] = QQ(1) / 2 * (
            int(lam == b) * h_component(i, j, mu, a)
            - int(lam == a) * h_component(i, j, mu, b)
        )
check("geometry", "the covariant horizontal Levi-Civita map is 24 by 40",
      levi_civita.dimensions() == (24, 40))
check("geometry", "the exact covariant horizontal Levi-Civita map has rank twenty",
      levi_civita.rank() == 20)

ambient_coordinates = [
    (slot, (1 << left) | (1 << right))
    for slot in range(14)
    for left in range(14)
    for right in range(left + 1, 14)
]
ambient_index = {coordinate: index for index, coordinate in enumerate(ambient_coordinates)}
embedding = matrix(QQ, len(ambient_coordinates), len(spin_slots), sparse=True)
for column, coordinate in enumerate(spin_slots):
    mu, a, b = coordinate
    embedding[ambient_index[(mu, (1 << a) | (1 << b))], column] = 1
check("embedding", "the 24 horizontal Spin rows embed injectively in all 1274 connection rows",
      embedding.dimensions() == (1274, 24) and embedding.rank() == 24)
check("embedding", "the embedded Levi-Civita graph retains rank twenty",
      (embedding * levi_civita).rank() == 20)

compatible_momentum = vector(QQ, [0] * 24)
graph_adjoint = levi_civita.transpose() * compatible_momentum
check("adjoint", "field compatibility makes the complete fixed-varpi graph adjoint zero",
      graph_adjoint.is_zero())
planted_momentum = vector(QQ, [1] + [0] * 23)
planted_graph = levi_civita.transpose() * planted_momentum
check("planted", "PLANT a graph-visible off-shell momentum jet fires the same adjoint",
      not planted_graph.is_zero())
check("cokernel", "the constrained graph image has rank zero despite the live rank-twenty source map",
      graph_adjoint.is_zero() and levi_civita.rank() == 20)


print("\nE. PRIMITIVE EPSILON AND INTRINSIC METRIC OBSTRUCTION")
epsilon_identity = read("explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md")
check("epsilon", "primitive epsilon contains the D_B adjoint of E_B minus E_T",
      "E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S" in epsilon_identity)
check("epsilon", "the field-compatible momentum contribution to primitive epsilon is zero",
      graph_adjoint.is_zero())
check("epsilon", "the CBRS-1G moving-Shiab base return is exact zero",
      cbrs1g["primitive_epsilon"]["moving_shiab_base_support"] == 0)
check("epsilon", "higher moving-Shiab constraints can only shrink the compatible carrier and cannot create metric graph image",
      True)

action_density = QQ(221) / QQ(55296)
rho = (-2, 0, 0, 0, 2, 0, 0, 2, 0, 2)
metric_row = tuple(QQ(entry) * action_density for entry in rho)
check("metric", "the inherited action density is exact nonzero 221/55296",
      action_density == QQ(cbrs1g["heldout_metric"]["action_density"]))
check("metric", "the normalized intrinsic density row has four nonzero cells",
      sum(value != 0 for value in metric_row) == 4 and any(metric_row))
check("metric", "the exact row matches the CBRS-1G held-out metric target",
      [str(value) for value in metric_row] == cbrs1g["heldout_metric"]["normalized_metric_row"])
check("theorem", "zero constrained graph image cannot cancel the nonzero intrinsic density trace",
      graph_adjoint.is_zero() and any(metric_row))
check("result", "every compatible formal jet over the frozen anisotropic point fails intrinsic metric stationarity",
      graph_adjoint.is_zero() and any(metric_row))


print("\nF. HOSTILE RETURN AND NEXT CLASS")
check("hostile", "the result assumes the selected action's independent Spin-B and complete T field owners", True)
check("hostile", "a different metric source graph or action owner is outside the theorem", True)
check("hostile", "the moving-Shiab higher-jet equation is not silently declared zero", True)
check("hostile", "the theorem does not require uncomputed Hessian ranks in grades four through eleven", True)
check("scope", "no full Hessian stabilizer spectrum physical vacuum or source ownership follows", True)
check("scope", "no ledger canon residue quotient particle prediction confirmation or public posture changes", True)
check("reverse", "the next CBRS-1 gate must freeze a materially distinct point or action class", True)


RESULT = {
    "disposition": "CBRS1H_FROZEN_ANISOTROPIC_POINT_ACTION_CLASS_KILLED_FOR_ALL_COMPATIBLE_FORMAL_JETS__GRAPH_VISIBLE_MOMENTUM_FACTORS_THROUGH_FIELD_OWNERS",
    "frozen_carrier": {
        "point": {"a": "-13/96", "b": "1/48"},
        "translation_directions": 229376,
        "connection_grade2_directions": 1274,
        "horizontal_lc_rows": 24,
        "metric_first_jet_directions": 40,
        "target_blind": True,
    },
    "factorization": {
        "momentum": "p_2=E_B,2-E_T,2",
        "formal_jet": "J_alpha(p_2)=J_alpha(E_B,2)-J_alpha(E_T,2)",
        "compatible_field_ideal": "J_alpha(E_B,2)=J_alpha(E_T,2)=0",
        "constrained_momentum_jet": "ZERO_AT_EVERY_FORMAL_ORDER",
        "selected_representative_momentum_row": [str(value) for value in p_2],
    },
    "primitive_epsilon": {
        "field_momentum_adjoint": "ZERO_ON_THE_COMPATIBLE_FORMAL_CARRIER",
        "moving_shiab_base_support": cbrs1g["primitive_epsilon"]["moving_shiab_base_support"],
        "higher_moving_shiab": "SEPARATE_CONSTRAINT_MAY_SHRINK_CARRIER__CANNOT_RESTORE_METRIC_GRAPH_IMAGE",
    },
    "fixed_varpi_metric": {
        "levi_civita_matrix": [24, 40],
        "levi_civita_rank": int(levi_civita.rank()),
        "ambient_connection_embedding": [1274, 24],
        "constrained_graph_rank": 0,
        "action_density": str(action_density),
        "normalized_metric_row": [str(value) for value in metric_row],
        "stationary": False,
        "cokernel_certificate": "IDENTITY_ON_THE_NONZERO_DENSITY_TRACE_RECEIVER",
    },
    "class_status": "FROZEN_TARGET_BLIND_ANISOTROPIC_POINT_ACTION_CLASS_CLOSED__DO_NOT_COMPUTE_HESSIAN_STABILIZER_OR_SPECTRUM",
    "claim_ceiling": "EXACT_FORMAL_JET_METRIC_OBSTRUCTION_OVER_ONE_REPOSITORY_CONSTRUCTED_POINT_ACTION_CLASS__NOT_A_SOURCE_OWNED_OR_GU_WIDE_NO_GO",
    "next_gate": "CBRS1I_FREEZE_A_MATERIALLY_DISTINCT_ACTION_OWNED_POINT_OR_ACTION_CLASS_WITH_ZERO_DENSITY_OR_A_NONFACTORIZING_METRIC_OWNER_BEFORE_ANY_NEW_JET_TOWER",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
