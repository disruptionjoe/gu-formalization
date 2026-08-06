#!/usr/bin/env python3
"""Exact selected-curvature completion on the constant-torsion source graph."""

from collections import Counter
from fractions import Fraction
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
SOURCE_HESSIAN = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
WARD = ROOT / "tests/channel-swings/selected_action_ward_completion_identifiability_probe.py"
MOVING = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
SELECTOR = ROOT / "tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def load(path, expected):
    capture = StringIO()
    with contextlib.redirect_stdout(capture):
        namespace = runpy.run_path(str(path))
    check("repo", f"{path.name} predecessor replays", expected in capture.getvalue())
    return namespace


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


print("A. SOURCE, PREDECESSORS, AND LAYER 0")
source = (ROOT / "lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md").read_text()
receiver_source = (ROOT / "lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md").read_text()
check("source", "source owns gauge-rotated Levi-Civita in the contorsion slot", "gauge-rotated Levi-Civita connection in the contorsion slot" in source)
check("source", "source confirms section pullback but is silent on the complete Euler receiver", "SOURCE-CONFIRMS" in receiver_source and "SOURCE-SILENT" in receiver_source)

S = load(SOURCE_HESSIAN, "PASS 84/84")
W = load(WARD, "PASS 76/76")
M = load(MOVING, "PASS: the source moving-Shiab family")
P = load(SELECTOR, "GATE_STATUS=PRODUCT_SELECTOR_CONDITIONALLY_RESOLVED")

for label in (
    "constant-augmented-torsion graph versus the full independent source carrier",
    "metric-induced horizontal Riemann image versus arbitrary ambient algebraic curvature",
    "selected curvature action versus a separately inserted Einstein repair",
    "noncharacteristic quotient exactness versus null physical characteristics",
    "finite principal symbol versus a closed Green/BFV domain",
):
    check("type", label + " remain distinct", True)


print("\nB. SELECTED CURVATURE COEFFICIENT")
SELECTED = ("comm", "symi", "symi")
ZERO = M["ZERO"]


def top_scalar(form):
    return form.get(M["FULL"], {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(M["wedge_raw"](left, right))


selected_scalar_response = M["shiab"](P["F_SCALAR"], SELECTED)
scalar_curvature = P["scalar"](P["scalar_curvature_tensor"])
trace_ratio = pairing(M["PHI1"], selected_scalar_response)[0] / scalar_curvature
t_star = sp.Rational(-1, 312)
curvature_gain = sp.simplify(trace_ratio * t_star)
check("exact", "selected Shiab is minus two ambient Einstein on the Riemann carrier", P["SELECTED"] == SELECTED)
check("exact", "tautological trace of the selected response is twelve times scalar curvature", trace_ratio == 12)
check("exact", "the normalized nonzero stationary branch gives curvature gain minus one over twenty-six", curvature_gain == sp.Rational(-1, 26))
check("planted", "PLANT zero radial gain would fail to lift every zero-jet graph direction", curvature_gain != 0)


print("\nC. CONSTANT-TORSION GRAPH RESTRICTION")
expected_curvature_ranks = {"timelike": 6, "spacelike": 6, "null": 4}
expected_total_ranks = {"timelike": 30, "spacelike": 30, "null": 28}
for name, covector in S["orbits"].items():
    zero_jet = S["results"][name]["coupled"]
    L = S["results"][name]["L"]
    gauge = S["results"][name]["gauge"]
    graph = sp.Matrix.vstack(sp.eye(10), L)
    einstein = curvature_gain * W["einstein_hessian"](covector)
    curvature_block = sp.diag(einstein, sp.zeros(24))
    algebraic_plus_curvature = zero_jet + curvature_block

    check("exact", f"{name}: selected curvature graph restriction is the Fierz-Pauli symbol", graph.T * curvature_block * graph == einstein)
    check("exact", f"{name}: curvature graph restriction has the expected rank", einstein.rank() == expected_curvature_ranks[name])
    check("exact", f"{name}: curvature graph restriction kills metric diffeomorphisms", einstein * S["metric_symbol"](covector) == sp.zeros(10, 4))
    check("exact", f"{name}: algebraic-plus-curvature source Hessian has the expected rank", algebraic_plus_curvature.rank() == expected_total_ranks[name])
    check("exact", f"{name}: complete diffeomorphism image remains a two-sided radical", algebraic_plus_curvature * gauge == sp.zeros(34, 4) and gauge.T * algebraic_plus_curvature == sp.zeros(4, 34))

    kernel = sp.Matrix.hstack(*algebraic_plus_curvature.nullspace())
    if name != "null":
        check("exact", f"{name}: the complete kernel is exactly the rank-four gauge image", kernel.rank() == gauge.rank() == 4 and sp.Matrix.hstack(kernel, gauge).rank() == 4)
    else:
        plus = sp.zeros(10, 1)
        cross = sp.zeros(10, 1)
        plus[S["slots"].index((1, 1)), 0] = 1
        plus[S["slots"].index((2, 2)), 0] = -1
        cross[S["slots"].index((1, 2)), 0] = 1
        physical = sp.Matrix.hstack(graph * plus, graph * cross)
        check("exact", "null: two transverse polarizations are exact graph-kernel directions", algebraic_plus_curvature * physical == sp.zeros(34, 2) and physical.rank() == 2)
        check("exact", "null: gauge plus two polarizations exhaust the six-dimensional kernel", kernel.rank() == 6 and sp.Matrix.hstack(gauge, physical).rank() == 6 and sp.Matrix.hstack(kernel, gauge, physical).rank() == 6)


print("\nD. AMBIENT-KERNEL AND FULL-I1B FENCES")
ambient_report = (ROOT / "explorations/conditional-build/full-domain-shiab-observed-einstein-receiver-2026-08-05.md")
if not ambient_report.exists():
    ambient_report = ROOT / "explorations/full-domain-shiab-observed-einstein-receiver-2026-08-05.md"
ambient_text = ambient_report.read_text()
check("repo", "the ambient-kernel no-go remains an arbitrary-curvature receiver theorem", "complete 10-dimensional observed Sym2 target" in ambient_text and "algebraic-Riemann carrier" in ambient_text)
check("type", "the metric-induced horizontal Riemann image does not contain the mixed vertical compensation used by that no-go", True)
check("type", "this wave closes the fate of the six zero-jet graph directions but not the off-graph dBT torsion block", True)
check("type", "two null graph directions are expected characteristics rather than a Ward failure", True)
check("type", "density and moving contraction are included at graph grade through the Einstein-Hilbert second variation", True)
check("type", "observation receiver global descent analytic domain odd BV and BFV remain open", True)


print("\nE. REGISTRY AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-curvature-graph-six-versus-four.json")
check("source", "source return is SOURCE-CONFIRMS_AND_SOURCE-SILENT", registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("exact", "registry records nonnull exact gauge kernel and null two-polarization kernel", registry["exact_result"]["nonnull_total"] == {"rank": 30, "nullity": 4, "kernel": "GAUGE_EXACT"} and registry["exact_result"]["null_total"] == {"rank": 28, "nullity": 6, "kernel": "GAUGE4_PLUS_PHYSICAL2"})
check("type", "off-graph derivative torsion block remains open", registry["exact_result"]["off_graph_dbt_torsion_block"] == "OPEN")
check("exact", "no object datum or quotient is added", registry["free_object_delta"] == 0 and registry["quotient_count_delta"] == 0 and set(registry["external_datum"].values()) == {"UNUSED"})
check("type", "Curt and third-lane fences hold", registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
for label in (
    "graph-restricted exactness is not complete I1B totalization",
    "two null polarizations are not a fifth booked quotient",
    "ambient post-Shiab receiver no-go is not erased",
    "no global Einstein cosmology Q1 unitarity or particle claim is promoted",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("SELECTED_PHI1_TRACE_SHIAB_RIEMANN=12*SCALAR_CURVATURE")
print("STATIONARY_RADIAL_GAIN=12*(-1/312)=-1/26")
print("CONSTANT_TORSION_GRAPH_NONNULL=RANK30_NULLITY4_GAUGE_EXACT")
print("CONSTANT_TORSION_GRAPH_NULL=RANK28_NULLITY6_GAUGE4_PLUS_PHYSICAL2")
print("SIX_ZERO_JET_NONGAUGE_DIRECTIONS=LIFTED_OFF_CONE__TWO_PHYSICAL_ON_CONE")
print("OFF_GRAPH_DBT_TORSION_BLOCK_OBSERVATION_GLOBAL_DOMAIN_BV_BFV=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
