#!/usr/bin/env python3
"""Exact SR-0 discriminator for source residual-square versus ordinary YM."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LANE = ROOT / "lab/process/source-residual-cohomology-lane.json"
INDEX = ROOT / "lab/active-research/source-residual-cohomology/README.md"
REPORT = ROOT / "lab/active-research/source-residual-cohomology/sr0-operator-owner-rebase-2026-08-14.md"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
SOURCE_PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
I2_OWNER = ROOT / "explorations/conditional-build/selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md"
I2_HESSIAN = ROOT / "explorations/conditional-build/selected-k77-i2b-lower-order-exact-form-lift-2026-08-13.md"
YM_GATE = ROOT / "explorations/conditional-build/selected-k77-total-twisted-yang-mills-current-gate-2026-08-14.md"
TWISTOR_GATE = ROOT / "explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md"

checks = 0


def check(label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1
    print(f"PASS [{label}]")


def matvec(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(column) for column in zip(*matrix)]


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


lane = json.loads(LANE.read_text())
index = INDEX.read_text()
report = REPORT.read_text()
source_register = SOURCE_REGISTER.read_text()
source_pack = SOURCE_PACK.read_text()
i2_owner = I2_OWNER.read_text()
i2_hessian = I2_HESSIAN.read_text()
ym_gate = YM_GATE.read_text()
twistor_gate = TWISTOR_GATE.read_text()

check("lane schema is one", lane["schema_version"] == "1.0")
check("lane is repo-native research, not a service lane", lane["lane_kind"] == "repo_native_research_workstream")
check("lane is active research", lane["status"] == "active_research")
check("H1-R is the primary hypothesis", lane["primary_hypothesis"]["id"] == "H1-R")
check("H0 remains mandatory", lane["mandatory_null"]["id"] == "H0")
check("there are eight dependency-ordered swings", [s["id"] for s in lane["swings"]] == [f"SR-{i}" for i in range(8)])
check("SR-0 alone is executed", [s["status"] for s in lane["swings"]].count("executed") == 1 and lane["swings"][0]["status"] == "executed")
check("every exact-floor predecessor exists", all((ROOT / path).is_file() for path in lane["exact_floor"]))
check("SR-1 starts only after the operator-owner rebase", lane["swings"][1]["depends_on"] == ["SR-0"])
check("SR-2 starts only after the residual complex", lane["swings"][2]["depends_on"] == ["SR-1"])
check("SR-6 requires both factorization branches", lane["swings"][6]["depends_on"] == ["SR-2", "SR-3"])
check("SR-7 depends on both dynamics and physical-state gates", lane["swings"][7]["depends_on"] == ["SR-5", "SR-6"])
check("claim ceiling rejects a superposition law", "superposition law" in lane["claim_ceiling"])
check("index distinguishes research workstream from CapacityOS service Lane", "not a CapacityOS" in index)

check("SC-ACT-01 is registered", "- id: SC-ACT-01" in source_register)
check("SC-ACT-04 is registered", "- id: SC-ACT-04" in source_register)
check("SC-ACT-05 is registered", "- id: SC-ACT-05" in source_register)
check("SC-ACT-04 records I2 as a residual square", "I^B_2 = ||Upsilon^B_omega||^2" in source_register)
check("source pack separates total boson and fermion residual", "\\Upsilon^B_\\omega+\\Upsilon^F_\\omega=0" in source_pack)
check("source pack records the cohomology obstruction", "obstruction" in source_pack and "cohomology" in source_pack)
check("source-natural fixed-grade I2 owner is resolved", "SOURCE_FAITHFUL_FIXED_NATURAL_I2B_OWNER_RESOLVED" in i2_owner)
check("source-natural owner uses Q_B on Upsilon_print", "Q_B Upsilon_print" in i2_owner)
check("existing exact Hessian retains the residual-dependent term", "Upsilon,D^2" in i2_hessian)
check("ordinary YM iff II zero fails both ways", "false in both directions" in ym_gate)
check("ordinary YM gate exposes a reduction current", "[R,D_A R]" in ym_gate)
check("twistor detour requires a Yang-Mills connection", "Yang--Mills" in twistor_gate and "detour" in twistor_gate)

# Exact finite operator-owner discriminator.
shiab = [[2, 0], [0, 1]]
torsion = (-2, 0)
j_upsilon = shiab


def f(point: tuple[int, int]) -> tuple[int, int]:
    return point


def upsilon(point: tuple[int, int]) -> tuple[int, int]:
    sf = matvec(shiab, f(point))
    return tuple(sf[i] + torsion[i] for i in range(2))


def e_ym(point: tuple[int, int]) -> tuple[int, int]:
    return f(point)


def e_i2(point: tuple[int, int]) -> tuple[int, int]:
    return matvec(transpose(j_upsilon), upsilon(point))


check("finite residual is exactly S F plus T", upsilon((3, 5)) == (4, 5))
check("ordinary YM vanishes at the origin", e_ym((0, 0)) == (0, 0))
check("source residual-square Euler does not vanish there", e_i2((0, 0)) == (-4, 0))
check("source residual-square Euler vanishes at its shifted shell", e_i2((1, 0)) == (0, 0))
check("ordinary YM does not vanish on that shifted shell", e_ym((1, 0)) == (1, 0))
check("operator zero sets differ in both directions", e_ym((0, 0)) == (0, 0) != e_i2((0, 0)) and e_i2((1, 0)) == (0, 0) != e_ym((1, 0)))

# Exact Hessian identity for U=(x^2-x+y-1, x-y), Q=I.
def nonlinear_data(point: tuple[int, int]) -> tuple[tuple[int, int], list[list[int]], list[list[int]]]:
    x, y = point
    u = (x * x - x + y - 1, x - y)
    jac = [[2 * x - 1, 1], [1, -1]]
    residual_term = [[2 * u[0], 0], [0, 0]]
    return u, jac, residual_term


u_on, jac_on, residual_on = nonlinear_data((1, 1))
gauss_newton_on = matmul(transpose(jac_on), jac_on)
full_on = [[gauss_newton_on[i][j] + residual_on[i][j] for j in range(2)] for i in range(2)]
check("chosen on-shell point has zero residual", u_on == (0, 0))
check("on-shell residual Hessian term vanishes", residual_on == [[0, 0], [0, 0]])
check("on-shell full Hessian equals Gauss-Newton square", full_on == gauss_newton_on == [[2, 0], [0, 2]])

u_off, jac_off, residual_off = nonlinear_data((0, 0))
gauss_newton_off = matmul(transpose(jac_off), jac_off)
full_off = [[gauss_newton_off[i][j] + residual_off[i][j] for j in range(2)] for i in range(2)]
check("chosen off-shell point has nonzero residual", u_off == (-1, 0))
check("off-shell residual Hessian term is nonzero", residual_off == [[-2, 0], [0, 0]])
check("off-shell full Hessian differs from Gauss-Newton square", full_off == [[0, -2], [-2, 2]] and full_off != gauss_newton_off)

check("report identifies source residual as primitive", "source residual/deformation complex is the primitive candidate" in report)
check("report keeps ordinary YM as comparator", "ordinary-YM comparator only" in report)
check("report requires a residual-zero stationary background for SR-1", "Upsilon(Phi_*) = 0" in report)
check("report forbids manufacturing the background by tangent restriction", "does not\nmanufacture one by restricting the tangent" in report)
check("report changes no canon verdict", "canon_verdict_change: none" in report)

print(f"PASS {checks}/{checks}")
