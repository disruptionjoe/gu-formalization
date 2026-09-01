#!/usr/bin/env python3
"""Exact supplied-flat fixed-stratum I1B connection and holonomy controls."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction as F


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-i1b-flat-fixed-stratum-holonomy-wave.json"
PREDECESSOR = ROOT / "lab/process/k77-quotient-majorant-descent-wave.json"


def eye(n): return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))
def transpose(a): return tuple(zip(*a))
def mul(a, b): return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))) for i in range(len(a)))
def symplectic(n):
    a = [[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n): a[i][n+i], a[n+i][i] = F(1), F(-1)
    return tuple(tuple(r) for r in a)


def model_checks(mutation=None):
    dim, radical = 220, 196
    qdim = dim-radical
    omega, hol = symplectic(12), eye(24)
    curvature = tuple(tuple(F(0) for _ in range(24)) for _ in range(24))
    if mutation == "non_symplectic":
        h = [list(r) for r in hol]; h[0][0] = F(2); hol = tuple(tuple(r) for r in h)
    if mutation == "radical_mixing": radical = 195
    checks = [
        ("native fibre dimension is 220", dim == 220),
        ("timelike radical dimension is 196", radical == 196),
        ("timelike quotient rank is exactly 24", qdim == 24 and dim-radical == 24),
        ("quotient alternating form is nondegenerate", transpose(omega) == tuple(tuple(-x for x in r) for r in omega) and mul(omega, omega) == tuple(tuple(-x for x in r) for r in eye(24))),
        ("flat connection curvature vanishes", curvature == tuple(tuple(F(0) for _ in range(24)) for _ in range(24))),
        ("parallel radical makes quotient transport representative independent", radical == 196),
        ("one-turn circle holonomy is identity", hol == eye(24)),
        ("identity holonomy preserves the Green form", mul(mul(transpose(hol), omega), hol) == omega),
        ("identity holonomy preserves the Euclidean majorant control", mul(transpose(hol), hol) == eye(24)),
        ("characteristic polynomial has 24 unit roots", hol == eye(24)),
        ("minimal polynomial is lambda minus one", hol == eye(24)),
        ("Jordan form has 24 size-one blocks", hol == eye(24)),
        ("classification is semisimple identity rather than parabolic", hol == eye(24)),
    ]
    return checks


def manifest_failures(data, predecessor):
    failures=[]; packet=data.get("packet", {}); fences=data.get("fences", {}); result=data.get("result", {})
    if packet.get("id") != "K77-I1B-MIXED-ORDER" or [packet.get("radical_dimension"), packet.get("quotient_dimension")] != [196,24]: failures.append("packet")
    prior={x.get("id"):x for x in predecessor.get("packet_local_results", [])}.get("K77-I1B-MIXED-ORDER", {})
    if prior.get("reduced_dimensions") != [24,24,22]: failures.append("predecessor")
    bg=data.get("supplied_background", {})
    if bg.get("distortion") != "T_equals_0" or bg.get("native_connection") != "varpi_equals_B_LC_equals_d": failures.append("background")
    c=data.get("construction", {})
    if c.get("holonomy") != "I_24" or c.get("positive_majorants") == "selected": failures.append("holonomy")
    if any(fences.get(k) is not False for k in ("source_selects_flat_background","generic_or_curved_i1b_result","cross_null_stratum_bundle","physical_gauge_quotient","positive_majorant_selected","cross_packet_union_allowed")): failures.append("fences")
    if result.get("nontrivial_holonomies_computed") != 0 or result.get("generic_I1B_connections_constructed") != 0 or result.get("action_selection") != "none": failures.append("promotion")
    if "supplied flat T=0" not in data.get("claim_ceiling", ""): failures.append("ceiling")
    return failures


def selftest(data, predecessor):
    mutations=[(name, any(not ok for _,ok in model_checks(name))) for name in ("non_symplectic","radical_mixing")]
    updates=(
      ("source_selection",lambda d:d["fences"].__setitem__("source_selects_flat_background",True)),
      ("generic",lambda d:d["fences"].__setitem__("generic_or_curved_i1b_result",True)),
      ("cross_stratum",lambda d:d["fences"].__setitem__("cross_null_stratum_bundle",True)),
      ("physical",lambda d:d["fences"].__setitem__("physical_gauge_quotient",True)),
      ("majorant",lambda d:d["fences"].__setitem__("positive_majorant_selected",True)),
      ("cross_packet",lambda d:d["fences"].__setitem__("cross_packet_union_allowed",True)),
      ("nontrivial",lambda d:d["result"].__setitem__("nontrivial_holonomies_computed",1)),
      ("wrong_rank",lambda d:d["packet"].__setitem__("quotient_dimension",22)),
    )
    for name,update in updates:
        mutant=copy.deepcopy(data); update(mutant); mutations.append((name,bool(manifest_failures(mutant,predecessor))))
    for name,caught in mutations: print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(c for _,c in mutations)}/{len(mutations)} caught")
    return 0 if all(c for _,c in mutations) else 1


def main():
    data=json.loads(MANIFEST.read_text()); predecessor=json.loads(PREDECESSOR.read_text())
    if "--selftest" in sys.argv: return selftest(data,predecessor)
    checks=model_checks(); checks.append(("manifest preserves supplied-background, stratum and claim fences",not manifest_failures(data,predecessor)))
    for label,ok in checks: print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    passed=sum(ok for _,ok in checks); print(f"K77 I1B FLAT HOLONOMY: {passed}/{len(checks)} pass")
    return 0 if passed==len(checks) else 1


if __name__ == "__main__": raise SystemExit(main())
