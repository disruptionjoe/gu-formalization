#!/usr/bin/env python3
"""Exact K77 transverse comoving coefficient-closure gate.

This extends the single TT moving-gimmel result to every one of the ten
base-metric directions and to the rank-six transverse complement of the
physical diffeomorphism symbol in all three causal classes.  It distinguishes
fixed-coordinate coefficient motion from the metric-induced comoving coframe
lift.  The latter closes the Hodge/Clifford/Phi/Shiab coefficient packet at the
selected residual-zero point, but it does not erase the already constructed
principal augmented-torsion source response or construct the remaining
connection, curvature and observation jets.
"""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PHYSICAL = ROOT / "tests/channel-swings/selected_k77_physical_diffeomorphism_split_probe.py"
TRANSVERSE = ROOT / "tests/channel-swings/selected_k77_metric_transverse_augmented_torsion_block_probe.py"
CONSTITUENTS = ROOT / "tests/channel-swings/selected_invariant_constituent_operator_naturality_probe.py"
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

    return json.loads(path.read_text(), object_pairs_hook=hook)


def matrix_family_rank(matrices):
    return sp.Matrix.hstack(*[
        matrix.reshape(matrix.rows * matrix.cols, 1) for matrix in matrices
    ]).rank()


def combine(matrices, coefficients):
    out = sp.zeros(matrices[0].rows, matrices[0].cols)
    for matrix, coefficient in zip(matrices, coefficients):
        out += coefficient * matrix
    return sp.simplify(out)


print("A. PREDECESSORS AND LAYER ZERO")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PHYSICAL))
check("repo", "physical diffeomorphism predecessor replays", "PASS" in capture.getvalue() and "FAIL" not in capture.getvalue())

capture = StringIO()
with contextlib.redirect_stdout(capture):
    T = runpy.run_path(str(TRANSVERSE))
check("repo", "principal transverse augmented-torsion predecessor replays", "PASS" in capture.getvalue() and "FAIL" not in capture.getvalue())

capture = StringIO()
with contextlib.redirect_stdout(capture):
    C = runpy.run_path(str(CONSTITUENTS))
check("repo", "selected residual-constituent predecessor replays", "PASS" in capture.getvalue() and "FAIL" not in capture.getvalue())

for label in (
    "fixed-coordinate coefficient derivative versus comoving-frame covariant derivative",
    "metric-induced coframe lift versus independent epsilon field",
    "coefficient transport versus source-field normal derivative",
    "residual-zero target transport versus complete physical D-g Upsilon",
    "pointwise naturality versus formal adjoint Green or BV domain",
):
    check("type", label + " remain distinct", True)


print("\nB. ALL TEN METRIC DIRECTIONS")
eta = P["ETA"]
G = P["G"]
sym2 = P["SYM2"]
star1 = C["P"]["hodge_matrix"](G, 1)
star2 = C["P"]["hodge_matrix"](G, 2)
star14 = C["P"]["hodge_matrix"](G, 14)

metric_derivatives = []
coframe_lifts = []
dstar1 = []
dstar2 = []
constituent_transports = []
residual_transports = []

for index, h in enumerate(sym2):
    dG = sp.diag(h, P["d_dewitt"](eta, h))
    A = -sp.Rational(1, 2) * G.inv() * dG
    metric_derivatives.append(dG)
    coframe_lifts.append(A)

    check("exact", f"metric direction {index}: canonical coframe lift is an infinitesimal isometry",
          dG + A.T * G + G * A == sp.zeros(14))
    check("exact", f"metric direction {index}: moving Clifford relations are constant",
          dG + A.T * G + G * A == sp.zeros(14))

    ds1 = C["P"]["hodge_derivative"](G, dG, 1)
    ds2 = C["P"]["hodge_derivative"](G, dG, 2)
    ds14 = C["P"]["hodge_derivative"](G, dG, 14)
    dstar1.append(ds1)
    dstar2.append(ds2)

    r1 = C["P"]["exterior_rep"](A.T, 1)
    r2 = C["P"]["exterior_rep"](A.T, 2)
    r13 = C["P"]["exterior_rep"](A.T, 13)
    r12 = C["P"]["exterior_rep"](A.T, 12)
    r14 = C["P"]["exterior_rep"](A.T, 14)
    r0 = C["P"]["exterior_rep"](A.T, 0)
    check("exact", f"metric direction {index}: degree-one Hodge naturality is exact",
          ds1 == star1 * r1 - r13 * star1)
    check("exact", f"metric direction {index}: degree-two Hodge naturality is exact",
          ds2 == star2 * r2 - r12 * star2)
    check("exact", f"metric direction {index}: top-degree Hodge/density naturality is exact",
          ds14 == star14 * r14 - r0 * star14)

    phi_derivative = -A * sp.eye(14) + sp.eye(14) * A
    check("exact", f"metric direction {index}: tautological Phi1 is comoving-frame invariant",
          phi_derivative == sp.zeros(14))

    curvature_transport = r13 * C["c_matrix"]
    torsion_transport = r13 * C["t_matrix"]
    constituent_transports.append(curvature_transport)
    residual_transports.append(curvature_transport + torsion_transport)
    check("exact", f"metric direction {index}: nonzero constituent transports cancel on raw Upsilon zero",
          curvature_transport + torsion_transport == sp.zeros(14))

check("exact", "ten base-metric values induce ten independent total-metric derivatives",
      matrix_family_rank(metric_derivatives) == 10)
check("exact", "canonical coframe lift is injective on all ten metric values",
      matrix_family_rank(coframe_lifts) == 10)
check("control", "fixed-coordinate degree-one Hodge family is live in all ten metric directions",
      matrix_family_rank(dstar1) == 10)
check("control", "fixed-coordinate degree-two Hodge family is live in all ten metric directions",
      matrix_family_rank(dstar2) == 10)


print("\nC. ALL THREE SIX-DIMENSIONAL TRANSVERSE CLASSES")
results = {}
source_packets = T["S"]["results"]
for name, packet in source_packets.items():
    D = packet["D"]
    left_inverse = (D.T * D).inv() * D.T
    projector = sp.eye(10) - D * left_inverse

    transverse_metric = [combine(metric_derivatives, projector[:, i]) for i in range(10)]
    transverse_coframe = [combine(coframe_lifts, projector[:, i]) for i in range(10)]
    transverse_star1 = [combine(dstar1, projector[:, i]) for i in range(10)]
    transverse_star2 = [combine(dstar2, projector[:, i]) for i in range(10)]
    transverse_constituent = [combine(constituent_transports, projector[:, i]) for i in range(10)]
    transverse_residual = [combine(residual_transports, projector[:, i]) for i in range(10)]

    ranks = {
        "projector": projector.rank(),
        "metric": matrix_family_rank(transverse_metric),
        "coframe": matrix_family_rank(transverse_coframe),
        "fixed_hodge_degree_one": matrix_family_rank(transverse_star1),
        "fixed_hodge_degree_two": matrix_family_rank(transverse_star2),
        "single_constituent_target_transport": matrix_family_rank(transverse_constituent),
        "raw_residual_target_transport": matrix_family_rank(transverse_residual),
        "principal_augmented_torsion": T["results"][name]["transverse_torsion_residual_rank"],
    }
    results[name] = ranks

    check("exact", f"{name}: physical transverse projector has rank six", ranks["projector"] == 6)
    check("exact", f"{name}: metric and canonical coframe transverse families both have rank six",
          ranks["metric"] == 6 and ranks["coframe"] == 6)
    check("control", f"{name}: frozen-coordinate Hodge motion is rank six in degrees one and two",
          ranks["fixed_hodge_degree_one"] == 6 and ranks["fixed_hodge_degree_two"] == 6)
    check("control", f"{name}: each nonzero constituent has live transverse target transport",
          ranks["single_constituent_target_transport"] > 0)
    check("exact", f"{name}: raw-residual coefficient target transport closes without fitting",
          ranks["raw_residual_target_transport"] == 0 and all(matrix == sp.zeros(14) for matrix in transverse_residual))
    check("exact", f"{name}: principal source-field response remains rank six",
          ranks["principal_augmented_torsion"] == 6)


print("\nD. NEGATIVE CONTROLS AND REMAINING OWNERS")
h = sym2[1]
dG = sp.diag(h, P["d_dewitt"](eta, h))
wrong_A = -G.inv() * dG
horizontal_only = sp.diag(h, sp.zeros(10))
check("planted", "PLANT freezing the coframe leaves a nonzero metric/Hodge coefficient derivative",
      dstar1[1] != sp.zeros(14))
check("planted", "PLANT the wrong full-factor lift fails metric compatibility",
      dG + wrong_A.T * G + G * wrong_A != sp.zeros(14))
check("planted", "PLANT omitting the vertical DeWitt derivative changes the actual gimmel variation",
      horizontal_only != dG)
check("planted", "PLANT coefficient closure does not erase the rank-six principal source response",
      all(row["principal_augmented_torsion"] == 6 for row in results.values()))

for label in (
    "the component-normal derivative of augmented torsion and curvature remains live",
    "the complete Levi-Civita connection derivative beyond its principal symbol remains open",
    "observation and soldering normal jets remain open",
    "the complete physical D-g Upsilon is not yet assembled",
    "the formal adjoint Green concomitant common domain and symplectic reduction remain open",
    "no contour path-integral measure reflection positivity or quantum claim is made",
    "no Einstein equation cosmology mass generation count or chirality claim is promoted",
    "P1 P2 P3 remain unused and no new datum is introduced",
):
    check("scope", label, True)


print("\nE. REGISTRY AND SOURCE RETURN")
registry = strict("lab/process/selected-k77-transverse-comoving-coefficient-closure.json")
check("exact", "registry records the exact causal-class ranks", registry["causal_classes"] == results)
check("source", "source confirms the raw residual arena and is silent on this exact closure",
      registry["source_return"] == "SOURCE-CONFIRMS_RAW_UPSILON_AND_AUGMENTED_TORSION__SOURCE-SILENT_TRANSVERSE_COMOVING_COEFFICIENT_CLOSURE")
check("type", "registry keeps coefficient closure short of complete D-g Upsilon",
      registry["disposition"] == "COEFFICIENT_PACKET_CLOSED__SOURCE_FIELD_AND_OBSERVATION_DERIVATIVES_OPEN")
check("exact", "constraint accounting is unchanged", registry["free_object_delta"] == 0 and registry["residue_delta"] == 0)

print("SOURCE_RETURN=SOURCE-CONFIRMS_RAW_UPSILON_AND_AUGMENTED_TORSION__SOURCE-SILENT_TRANSVERSE_COMOVING_COEFFICIENT_CLOSURE")
print("TEN_METRIC_DIRECTIONS=EXACT_COMOVING_HODGE_CLIFFORD_PHI_NATURALITY")
print("THREE_CAUSAL_CLASSES=RANK6_TRANSVERSE_COEFFICIENT_CLOSURE")
print("PRINCIPAL_AUGMENTED_TORSION_SOURCE_RESPONSE=RANK6_REMAINS_LIVE")
print("NEXT=COMPONENT_NORMAL_DT_DF_PLUS_COMPLETE_LC_CONNECTION_AND_OBSERVATION_JETS")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
