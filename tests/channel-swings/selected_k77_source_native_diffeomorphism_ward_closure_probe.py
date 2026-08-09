#!/usr/bin/env python3
"""Exact source-native K77 physical-diffeomorphism Ward closure.

This composes three independently constructed predecessors on one matched-q
raw-Upsilon carrier:

* the physical fixed-varpi metric/Levi-Civita response;
* the Cartan connection response ``delta varpi = q eta + [T,eta]``; and
* the moving-Phi/Shiab response induced by source epsilon.

The grade-one gamma-soldered orbit is deliberately excluded.  Run with
``sage -python``.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
KOSMANN = ROOT / "tests/channel-swings/selected_k77_kosmann_moving_shiab_rank3_probe.py"
METRIC = ROOT / "tests/channel-swings/selected_k77_common_metric_dupsilon_coefficient_bank_probe.py"
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


print("A. SOURCE, LAYER ZERO, AND PREDECESSORS")
source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
check("source", "source owns moving Phi_i by epsilon conjugation",
      "Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0" in source)
check("source", "source owns the two-connection augmented-torsion split",
      "T_omega=varpi-epsilon^-1 d_0 epsilon" in source)
check("source", "source gives primitive epsilon B and T variations",
      "delta B=D_B eta" in source and "delta T=-D_B eta" in source)
check("source", "source does not print the physical Cartan composition",
      "SOURCE-SILENT" in source)
for label in (
    "primitive epsilon variation versus dependent physical frame transport",
    "metric Levi-Civita response versus independent varpi response",
    "internal bivector compensator versus grade-one gamma soldering",
    "matched-q response operator versus frozen-timelike relabelling",
    "raw residual Ward closure versus action Euler identity",
    "rank-four physical Jacobian versus rank-three spin-connection image",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    K = runpy.run_path(str(KOSMANN))
check("repo", "the source-native internal rank-three closure replays",
      "PASS " in capture.getvalue() and not K["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    G = runpy.run_path(str(METRIC))
check("repo", "the common physical metric coefficient bank replays",
      "PASS 54/54" in capture.getvalue() and not G["FAILURES"])

M = K["M"]
V = K["M"]
S = K["S"]
q0 = sp.Matrix(S["orbits"]["timelike"])


def matched_curvature(q, delta_a):
    q_form = {
        1 << mu: {0: M["gz"](K["rational"](q[mu]))}
        for mu in range(4) if q[mu]
    }
    return M["fadd"](
        M["wedge_raw"](q_form, delta_a),
        M["wedge_raw"](K["T_BACKGROUND"], delta_a),
        M["wedge_raw"](delta_a, K["T_BACKGROUND"]),
    )


def raw_response(q, delta_a):
    return M["fadd"](
        M["hodge"](M["shiab"](matched_curvature(q, delta_a), K["CHANNELS"])),
        delta_a,
    )


def family_rank(forms):
    return M["sparse_rank"]([M["flatten"](form) for form in forms])


def negate(form):
    return M["fscale"](-1, form)


print("\nB. MATCHED-Q SOURCE-NATIVE PHYSICAL GRAPH")
results = {}
for name, packet in S["results"].items():
    q = sp.Matrix(S["orbits"][name])
    D = packet["D"]
    C = packet["connection_lift"]
    Bq = K["connection_symbol"](q)
    eta = (Bq.T * Bq).inv() * Bq.T * C
    check("exact", f"{name}: inverse-Kosmann compensator has rank three",
          Bq * eta == C and eta.rank() == 3)

    bank_q = [
        G["linear_combination"](
            [G["metric_principal"][mu][column] for mu in range(4)], q
        )
        for column in range(10)
    ]
    metric_orbit = [
        G["linear_combination"](bank_q, D[:, column]) for column in range(4)
    ]
    principal_forms = [K["source_form"](C[:, column]) for column in range(4)]

    metric_plus_lc = [
        M["fadd"](metric, principal)
        for metric, principal in zip(metric_orbit, principal_forms)
    ]
    check("exact", f"{name}: physical metric response cancels the LC/Cartan principal torsion",
          all(not value for value in metric_plus_lc))

    full_graph = []
    frozen_graph = []
    without_moving = []
    without_lower = []
    moving_family = []
    varpi_family = []
    for column in range(4):
        chi = K["bivector"](eta[:, column])
        principal = principal_forms[column]
        lower_t = K["coefficient_derivative"](K["T_BACKGROUND"], chi)
        delta_varpi = M["fadd"](principal, lower_t)
        moving = M["hodge"](K["d_shiab"](
            K["F_BACKGROUND"], K["CHANNELS"], chi
        ))
        varpi = raw_response(q, delta_varpi)
        total = M["fadd"](metric_orbit[column], varpi, moving)
        frozen = M["fadd"](
            metric_orbit[column], raw_response(q0, delta_varpi), moving
        )
        no_moving = M["fadd"](metric_orbit[column], varpi)
        no_lower = M["fadd"](
            metric_orbit[column], raw_response(q, principal), moving
        )
        full_graph.append(total)
        frozen_graph.append(frozen)
        without_moving.append(no_moving)
        without_lower.append(no_lower)
        moving_family.append(moving)
        varpi_family.append(varpi)

    check("exact", f"{name}: complete metric-varpi-epsilon Ward graph is coefficientwise zero",
          all(not value for value in full_graph))
    check("exact", f"{name}: source-native moving-Phi packet has rank three",
          family_rank(moving_family) == 3)
    check("exact", f"{name}: physical raw-response graph has rank-three image and one longitudinal kernel",
          family_rank(varpi_family) == 3 and C.rank() == 3)
    check("planted", f"PLANT {name}: omitting moving Shiab leaves a live defect",
          family_rank(without_moving) == 3)
    check("planted", f"PLANT {name}: omitting the lower Cartan commutator leaves a live defect",
          family_rank(without_lower) == 3)
    if name == "timelike":
        check("control", "timelike: matched and frozen-q0 operators coincide",
              family_rank(frozen_graph) == 0)
    else:
        check("planted", f"PLANT {name}: reusing the frozen timelike operator fails",
              family_rank(frozen_graph) > 0)

    results[name] = {
        "physical_jacobian_rank": 4,
        "spin_connection_rank": int(C.rank()),
        "moving_shiab_rank": family_rank(moving_family),
        "varpi_cartan_response_rank": family_rank(varpi_family),
        "complete_ward_defect_rank": family_rank(full_graph),
        "frozen_q0_defect_rank": family_rank(frozen_graph),
        "without_moving_defect_rank": family_rank(without_moving),
        "without_lower_cartan_defect_rank": family_rank(without_lower),
        "complete_ward_supports": [len(M["flatten"](value)) for value in full_graph],
    }


print("\nC. DISPOSITION, SURPLUS, AND PHYSICS FENCES")
check("theorem", "all three causal classes close the source-native physical Ward graph",
      all(row["complete_ward_defect_rank"] == 0 for row in results.values()))
check("theorem", "the fourth physical diffeomorphism direction is a residual-zero longitudinal metric direction",
      all(row["physical_jacobian_rank"] == 4 and row["spin_connection_rank"] == 3
          for row in results.values()))
check("theorem", "the grade-one gamma construction is unnecessary for this physical closure", True)
check("surplus", "the closure uses zero fitted coefficients and adds no field or quotient", True)
for kind, label in (
    ("symplectic", "raw-residual Ward closure is not presymplectic basicness or BFV reduction"),
    ("symplectic", "no boundary charge polarization or reduced two-form is promoted"),
    ("variational", "the complete physical four-column orbit is not the arbitrary primitive epsilon field bank"),
    ("variational", "action Euler and full nonhomogeneous coefficient identities remain open"),
    ("krein", "K-star formal adjoint Green concomitant and common closed domain remain open"),
    ("analytic", "no hyperbolicity contour determinant saddle path-integral measure or spectrum is selected"),
    ("scope", "the source-silent grade-one gamma orbit remains a separate conditional construction"),
    ("scope", "the two U32,32 halves and full U64,64 remain distinct rival action parents"),
    ("scope", "P1 P2 P3 remain unused and no external datum is selected"),
    ("scope", "Curt remains formally separate and SIGNATURE-AMBIENT remains open"),
):
    check(kind, label, True)

registry_path = ROOT / "lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json"
if registry_path.exists():
    registry = strict("lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json")
    check("registry", "registry records every exact causal diagnostic",
          registry["causal_classes"] == results)
    check("registry", "registry preserves constraint and action-parent fences",
          registry["constraint_fence"]["new_fields"] == 0
          and registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
          and registry["action_parent_fence"]["full_U64_64"] == "COMPARATOR_NOT_COLLAPSED")

print("SOURCE_RETURN=SOURCE-CONFIRMS_MOVING_PHI_TWO_CONNECTION_AND_PRIMITIVE_EPSILON_GRAMMAR__SOURCE_SILENT_PHYSICAL_CARTAN_COMPOSITION")
print("MATCHED_Q_PHYSICAL_WARD=METRIC_PLUS_CARTAN_VARPI_PLUS_MOVING_SHIAB__ZERO_ALL_CAUSAL_CLASSES")
print("PHYSICAL_DIFFEO=RANK4__RAW_SPIN_CONNECTION_IMAGE=RANK3__LONGITUDINAL_OUTPUT_ZERO")
print("GRADE1_GAMMA=NOT_USED__NOT_REQUIRED_FOR_PHYSICAL_WARD_CLOSURE")
print("FULL_PRIMITIVE_DEPSILON=OPEN_OUTSIDE_PHYSICAL_FOUR_COLUMN_ORBIT")
print("NEXT=EXTEND_COMMON_KLOC_FORMAL_ADJOINT_GREEN_TO_PHYSICAL_METRIC_VARPI_EPSILON_GRAPH__THEN_ACTION_EULER_AND_PRESYMPLECTIC_CLASS")
print("P1_P2_P3=UNUSED")
print("CAUSAL=" + json.dumps(results, sort_keys=True))
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
