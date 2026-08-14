#!/usr/bin/env python3
"""Exact SR-1 conditional complex theorem and GU background audit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LANE = ROOT / "lab/process/source-residual-cohomology-lane.json"
INDEX = ROOT / "lab/active-research/source-residual-cohomology/README.md"
REPORT = ROOT / "lab/active-research/source-residual-cohomology/sr1-total-residual-complex-background-gate-2026-08-14.md"
SCAFFOLD = ROOT / "lab/active-research/source-residual-cohomology/sr1c-source-coordinate-variational-prolongation-scaffold-2026-08-14.md"
SOURCE_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
SOURCE_PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
RADIAL = ROOT / "explorations/conditional-build/selected-k77-i2b-lower-order-exact-form-lift-2026-08-13.md"
FACTOR = ROOT / "explorations/conditional-build/selected-k77-stationary-two-layer-hessian-factorization-2026-08-08.md"
WARD = ROOT / "explorations/conditional-build/selected-k77-source-native-diffeomorphism-ward-closure-2026-08-08.md"
BVKT = ROOT / "explorations/conditional-build/selected-k77-i2b-source-bvkt-exact-sequence-2026-08-13.md"
FULL_FERMION = ROOT / "explorations/conditional-build/selected-k77-full-carrier-stationary-residual-2026-08-10.md"
GRAMMAR = ROOT / "explorations/conditional-build/selected-k77-i2b-source-action-grammar-exhaustion-2026-08-13.md"

checks = 0


def check(label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1
    print(f"PASS [{label}]")


def add(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[left[i][j] + right[i][j] for j in range(2)] for i in range(2)]


def sub(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[left[i][j] - right[i][j] for j in range(2)] for i in range(2)]


def mul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def comm(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return sub(mul(left, right), mul(right, left))


zero = [[0, 0], [0, 0]]
lane = json.loads(LANE.read_text())
index = INDEX.read_text()
report = REPORT.read_text()
scaffold = SCAFFOLD.read_text()
source_register = SOURCE_REGISTER.read_text()
source_pack = SOURCE_PACK.read_text()
radial = RADIAL.read_text()
factor = FACTOR.read_text()
ward = WARD.read_text()
bvkt = BVKT.read_text()
full_fermion = FULL_FERMION.read_text()
grammar = GRAMMAR.read_text()

# Lane state and source typing.
check("SR-1 records an executed negative gate", lane["swings"][1]["status"] == "executed_negative")
check("SR-1 disposition is background missing", lane["swings"][1]["disposition"] == "BACKGROUND-MISSING")
check("SR-1 result exists", (ROOT / lane["swings"][1]["result"]).is_file())
check("SR-1 probe points to this executable", (ROOT / lane["swings"][1]["probe"]).resolve() == Path(__file__).resolve())
check("SR-2 is blocked by the failed premise", lane["swings"][2]["status"] == "blocked" and lane["swings"][2]["blocked_by"] == "SR-1:BACKGROUND-MISSING")
check("SR-1C is the next construction", lane["next_required_construction"]["id"] == "SR-1C")
check("the SR-1C scaffold exists", (ROOT / lane["next_required_construction"]["scaffold"]).is_file())
check("the lane forbids manufacturing a background", "manufacture a background" in lane["next_required_construction"]["failure_rule"])
check("the lane pauses RF-3 until the total carrier exists", "RF_3_PAUSED_UNTIL_K_TOTAL_L_TOTAL_EXIST" in lane["next_required_construction"]["reverse_falsification_status"])
check("the index exposes the negative result", "executed negative: `BACKGROUND-MISSING`" in index)
check("the index keeps the lane active", "status: active_research" in index)
check("H0 remains mandatory", lane["mandatory_null"]["id"] == "H0")

check("SC-ACT-06 is registered", "- id: SC-ACT-06" in source_register)
check("SC-ACT-06 is only partially adhered", "adherence: PARTIAL" in source_register[source_register.index("- id: SC-ACT-06"):source_register.index("- id: SC-FER-01")])
check("source asserts rather than constructs a rich moduli", "rich moduli of classical solutions" in source_register)
check("source pack distinguishes redundancy from Noether", "redundancy identity is displayed, but a Noether identity is not" in source_pack)
check("source pack types Upsilon as the obstruction", "Upsilon_\\omega" in source_pack and "obstruction" in source_pack)

# Exact generic covariance control: U(A1,A2)=[A1,A2], K_eta Ai=[eta,Ai].
eta = [[0, 1], [1, 0]]
a1_on = [[1, 0], [0, -1]]
a2_on = [[2, 0], [0, -2]]
u_on = comm(a1_on, a2_on)
k1_on = comm(eta, a1_on)
k2_on = comm(eta, a2_on)
du1_on = comm(k1_on, a2_on)
du2_on = comm(a1_on, k2_on)
composition_on = add(du1_on, du2_on)

check("on-shell control has zero residual", u_on == zero)
check("on-shell gauge generator is nonzero on both fields", k1_on != zero and k2_on != zero)
check("both on-shell derivative contributions are live", du1_on != zero and du2_on != zero)
check("coupled on-shell composition cancels exactly", composition_on == zero)
check("on-shell composition equals the covariance response", composition_on == comm(eta, u_on))
check("freezing the first field response fails", du2_on != zero)
check("freezing the second field response fails", du1_on != zero)

a1_off = [[1, 0], [0, -1]]
a2_off = [[0, 1], [0, 0]]
u_off = comm(a1_off, a2_off)
k1_off = comm(eta, a1_off)
k2_off = comm(eta, a2_off)
composition_off = add(comm(k1_off, a2_off), comm(a1_off, k2_off))

check("off-shell control has nonzero residual", u_off != zero)
check("off-shell composition is nonzero", composition_off != zero)
check("off-shell composition equals eta acting on the residual", composition_off == comm(eta, u_off))
check("covariance is not off-shell nilpotence", composition_off != zero and composition_on == zero)

# Repository candidate audit.
check("selected radial branch has nonzero Krein-null residual", "branch residual is nonzero but\nKrein-null" in radial)
check("selected radial branch is not stationary on the full bank", "nonstationary on the full 196-cell connection bank" in radial)
check("factorization packet assumes complete residual zero", "complete** first-layer equation\n`Upsilon*=0`" in factor)
check("factorization packet leaves common-field D Upsilon open", "construct every action-owned common-field block of D Upsilon" in factor)
check("physical Ward packet is only a four-column orbit", "dependent physical four-column diffeomorphism orbit" in ward)
check("physical Ward packet disclaims a completed action calculation", "not yet an action-level Noether identity" in ward)
check("BVKT owns rank twenty-five and sixty-six reducibilities", "rank G = 25" in bvkt and "R^66" in bvkt)
check("BVKT leaves both Euler covectors nonzero", "E_source != 0" in bvkt)
check("full fermion packet is fixed-fixture rather than a moving background", "fixed fixture" in full_fermion)
check("full fermion packet leaves moving varpi locus open", "moving-coefficient rank-loss locus" in full_fermion)
check("released grammar leaves moving background or nonzero fermion open", "moving background jets" in grammar and "nonzero-fermion stationary saddle" in grammar)
check("released grammar asks for a full stationary jet", "full stationary" in radial)

# Report fences and terminal disposition.
check("report states the exact conditional composition", "L_Upsilon(Phi) K_Phi(eta) = rho_*(eta) Upsilon(Phi)" in report)
check("report refuses to promote the trivial ansatz", "trivial flat-zero ansatz" in report and "not shown to be a legal global" in report)
check("report keeps the total gauge map unassembled", "not yet one owned map" in report)
check("report blocks SR-2", "`SR-2` is blocked at its premise" in report)
check("report preserves the historical SR-1B stage", "The next construction is\n`SR-1B`" in report)
check("report names SR-1C as the current next construction", "The next construction, now named `SR-1C`" in report)
check("scaffold keeps SR-1 background missing", "`SR-1` remains `BACKGROUND-MISSING`" in scaffold)
check("scaffold keeps observation dependent", "not an additional independently varied action field" in scaffold)
check("report changes no canon verdict", "canon_verdict_change: none" in report)
check("report claims no physical cohomology", "No quantum state space" in report)

print(f"PASS {checks}/{checks}")
