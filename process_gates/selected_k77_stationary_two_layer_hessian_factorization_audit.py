#!/usr/bin/env python3
"""Scope audit for the stationary K77 two-layer Hessian factorization."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-stationary-two-layer-hessian-factorization-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-stationary-two-layer-hessian-factorization-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-stationary-two-layer-hessian-factorization-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.82.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-stationary-two-layer-hessian-factorization.json").read_text())

for phrase in (
    "H2 = (D Upsilon)^! K* (D Upsilon)",
    "physical metric movement of Shiab and Hodge",
    "dependent receiver/evaluation unless separately varied by the action",
    "first-layer Schur Hessian is not retyped as `D Upsilon`",
    "injective `J` can have",
    "a real Gram operator does not choose a contour",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert registry["result"] == "AT_UPSILON_ZERO__H2_EQUALS_DUPSILON_ADJOINT_K_DUPSILON"
assert "D2_UPSILON_TIMES_UPSILON_STAR" in registry["stationary_factorization"]["dropped_from_bulk_quadratic_operator"]
assert "PHYSICAL_DSHIAB_ON_FA_STAR" in registry["stationary_factorization"]["retained"]
assert registry["krein_control"]["physical_kernel_or_energy_derived"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.82"
assert "Symplectic geometry" in review
assert "Complex/path-integral analysis" in review
assert "PASS_AFTER_SCOPE_REPAIRS" in review
print("PASS selected K77 stationary two-layer Hessian factorization audit")
