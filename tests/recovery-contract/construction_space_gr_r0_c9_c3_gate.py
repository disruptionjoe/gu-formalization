#!/usr/bin/env python
"""Construction-space GR R0 gate for C9 before C3.

This is P1-GR-R0-LEMMA-C9-C3 from the construction-space exploration map.
It is a process/research checkpoint, not a claim-status move. It asks what
the current repo evidence can say at Rung 0 consistency strength about:

* C9 ambient/H-class residual bookkeeping, before
* C3 bare-theta/fundamental-stiffness vacuum support.

Run: python tests/recovery-contract/construction_space_gr_r0_c9_c3_gate.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
FINGERPRINT = ROOT / "lab" / "process" / "recovery-contract-action-fingerprint-2026-07-16.json"
REGISTER = ROOT / "lab" / "process" / "recovery-no-go-defense-register.json"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cell(map_data: dict, cell_id: str) -> dict:
    for entry in map_data["cells"]:
        if entry["id"] == cell_id:
            return entry
    raise AssertionError(f"missing construction-space cell {cell_id}")


def target(register: dict, target_id: str) -> dict:
    for entry in register["targets"]:
        if entry["id"] == target_id:
            return entry
    raise AssertionError(f"missing defense-register target {target_id}")


# Shared Schwarzschild weak-field symbols.
t, x, y, z, M, R = sp.symbols("t x y z M R", real=True, positive=True)
coords = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
eta = sp.diag(-1, 1, 1, 1)


def schwarzschild_h() -> sp.Matrix:
    phi = M / r
    h = sp.zeros(4, 4)
    h[0, 0] = 2 * phi
    for i in (1, 2, 3):
        h[i, i] = 2 * phi
    return h


def build_qtf_from_principled_ii() -> sp.Matrix:
    """Build the trace-free quadratic residual used by the GR recovery gates."""
    h = schwarzschild_h()

    def b(mu: int, nu: int, a: int, bidx: int) -> sp.Expr:
        return sp.diff(h[a, bidx], coords[mu], coords[nu])

    hmean = sp.zeros(4, 4)
    for a in range(4):
        for bidx in range(4):
            hmean[a, bidx] = sp.simplify(sum(eta[m, m] * b(m, m, a, bidx) for m in range(4)))

    def bhat(mu: int, nu: int, a: int, bidx: int) -> sp.Expr:
        return b(mu, nu, a, bidx) - sp.Rational(1, 4) * eta[mu, nu] * hmean[a, bidx]

    def fdot(func) -> sp.Expr:
        return sum(eta[a, a] * eta[bidx, bidx] * func(a, bidx) for a in range(4) for bidx in range(4))

    q = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            t1 = sp.Rational(1, 2) * fdot(lambda a, bidx: hmean[a, bidx] * bhat(mu, nu, a, bidx))
            t2 = sum(
                eta[p, p] * fdot(lambda a, bidx: bhat(mu, p, a, bidx) * bhat(p, nu, a, bidx))
                for p in range(4)
            )
            q[mu, nu] = sp.simplify(t1 - t2)

    trace = sp.simplify(sum(eta[p, p] * q[p, p] for p in range(4)))
    qtf = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            qtf[mu, nu] = sp.simplify(q[mu, nu] - sp.Rational(1, 4) * eta[mu, nu] * trace)
    return qtf


def all_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(matrix[i, j]) == 0 for i in range(matrix.rows) for j in range(matrix.cols))


def any_nonzero(matrix: sp.Matrix) -> bool:
    return any(sp.simplify(matrix[i, j]) != 0 for i in range(matrix.rows) for j in range(matrix.cols))


def trace_free_part(matrix: sp.Matrix) -> sp.Matrix:
    trace = sp.simplify(sum(eta[p, p] * matrix[p, p] for p in range(4)))
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            out[mu, nu] = sp.simplify(matrix[mu, nu] - sp.Rational(1, 4) * eta[mu, nu] * trace)
    return out


@dataclass(frozen=True)
class GrR0Candidate:
    cell_id: str
    source_owned_first_variation: bool
    coefficient_frozen_before_target: bool
    vacuum_supported_source: bool
    different_residual_bookkeeping: bool
    tensor_shape: str
    target_shaped_stress_import: bool
    preserves_linear_cheap_read: bool


def gr_r0_status(candidate: GrR0Candidate) -> str:
    if candidate.target_shaped_stress_import:
        return "INVALID_ESCAPE"
    if not candidate.preserves_linear_cheap_read:
        return "R0_FAIL"
    if candidate.different_residual_bookkeeping:
        if candidate.source_owned_first_variation and candidate.coefficient_frozen_before_target:
            return "R0"
        return "GATED"
    if candidate.vacuum_supported_source and candidate.tensor_shape == "trace_free_source_owned":
        return "R0"
    return "R0_FAIL"


def main() -> None:
    map_data = load_json(MAP)
    fingerprint = load_json(FINGERPRINT)
    register = load_json(REGISTER)
    gr_target = target(register, "RECOVERY-NOGO-GR-W229-VACUUM")

    qtf = build_qtf_from_principled_ii()
    lam = sp.symbols("lambda", real=True)
    metric_source = lam * eta
    target_source = -qtf

    log("=" * 82)
    log("PC controls - residual detector has teeth")
    log("=" * 82)
    check("PC1  the principled Q^TF(B) residual is nonzero", any_nonzero(qtf))
    check("PC2  a source tensor S = -Q^TF(B) would algebraically cancel", all_zero(qtf + target_source))
    check(
        "PC3  a metric-proportional stiffness stress has zero trace-free part",
        all_zero(trace_free_part(metric_source)),
    )
    check(
        "PC4  metric-proportional stress cannot cancel nonzero Q^TF(B)",
        any_nonzero(qtf + metric_source),
        "scalar/isotropic vacuum energy is in the wrong tensor slot",
    )

    log("")
    log("=" * 82)
    log("C1 - map and defense-register alignment")
    log("=" * 82)
    c9 = cell(map_data, "C9-AMBIENT-H-CLASS")
    c3 = cell(map_data, "C3-BARE-THETA-STIFFNESS")
    check("C1a  P1 evaluates C9 before C3", c9["id"].startswith("C9") and c3["id"].startswith("C3"))
    check(
        "C1b  map records the completed P1 GR dispositions",
        c9["tracks"]["GR"]["grade"] == "GATED"
        and c3["tracks"]["GR"]["grade"] == "R0_FAIL"
        and c9["tracks"]["GR"]["verification_needed"] is False
        and c3["tracks"]["GR"]["verification_needed"] is False,
    )
    check(
        "C1c  map evidence points back to the P1 note and test",
        "construction-space-gr-r0-lemma-c9-c3-2026-07-19.md" in c9["tracks"]["GR"]["evidence"]
        and "construction_space_gr_r0_c9_c3_gate.py" in c3["tracks"]["GR"]["evidence"],
    )
    check("C1d  GR defense target is bounded no-go for prior tested construction space", gr_target["challenge_state"] == "BOUNDED_NO_GO")
    check("C1e  resurrection triggers name C9 and C3 style dependencies", any("ambient or H-class" in item for item in gr_target["completed_swings"][-1]["resurrection_triggers"]) and any("bare-theta" in item for item in gr_target["completed_swings"][-1]["resurrection_triggers"]))

    log("")
    log("=" * 82)
    log("C2 - native-vacuum reframe sub-question")
    log("=" * 82)
    source_law = fingerprint["source_law"]
    check("C2a  current built action uses record-current vacuum rule", source_law["vacuum_rule"] == "Psi = 0 implies J[Psi] = 0.")
    check("C2b  current no-go uses imported Psi=0 benchmark, not a native vacuum selector", "Psi=0 in the imported vacuum gives J=0" in gr_target["completed_swings"][0]["minimized_obstruction"])
    check(
        "C2c  nonzero bare-theta vacuum support is a different branch dependency",
        any("bare-theta or fundamental-stiffness field equation" in item for item in gr_target["completed_swings"][-1]["resurrection_triggers"]),
    )

    log("")
    log("=" * 82)
    log("C3 - C9 ambient/H-class R0 status")
    log("=" * 82)
    c9_candidate = GrR0Candidate(
        cell_id="C9-AMBIENT-H-CLASS",
        source_owned_first_variation=False,
        coefficient_frozen_before_target=False,
        vacuum_supported_source=False,
        different_residual_bookkeeping=True,
        tensor_shape="ambient_h_class_unfrozen",
        target_shaped_stress_import=False,
        preserves_linear_cheap_read=True,
    )
    c9_status = gr_r0_status(c9_candidate)
    check("C3a  C9 is not an invalid target-stress import", c9_status != "INVALID_ESCAPE")
    check("C3b  C9 preserves the linear cheap-read clear as a bookkeeping/functor fork", c9_candidate.preserves_linear_cheap_read)
    check(
        "C3c  C9 is gated, not failed, until its first variation and coefficient are source-owned",
        c9_status == "GATED",
        c9_status,
    )

    log("")
    log("=" * 82)
    log("C4 - C3 bare-theta/stiffness lemma")
    log("=" * 82)
    c3_candidate = GrR0Candidate(
        cell_id="C3-BARE-THETA-STIFFNESS",
        source_owned_first_variation=False,
        coefficient_frozen_before_target=False,
        vacuum_supported_source=True,
        different_residual_bookkeeping=False,
        tensor_shape="metric_proportional_or_underived",
        target_shaped_stress_import=False,
        preserves_linear_cheap_read=True,
    )
    c3_status = gr_r0_status(c3_candidate)
    check("C4a  scalar/isotropic bare-theta stiffness is in the wrong trace-free slot", any_nonzero(qtf + metric_source))
    check("C4b  C3 lacks source-owned tensor shape and normalization in current records", not c3_candidate.source_owned_first_variation and not c3_candidate.coefficient_frozen_before_target)
    check("C4c  current C3 seed fails GR R0 consistency", c3_status == "R0_FAIL", c3_status)

    log("")
    log("=" * 82)
    log("VERDICT")
    log("=" * 82)
    if not FAIL:
        log("Operational result: P1 complete.")
        log("C9-AMBIENT-H-CLASS is GATED at GR R0 on a source-owned higher-codimension")
        log("first variation plus coefficient frozen before target use. C3-BARE-THETA-STIFFNESS")
        log("fails the current scalar/isotropic bare-theta GR R0 lemma: it supplies no")
        log("source-owned trace-free Q^TF(B)-slot tensor, and metric-proportional stress cannot")
        log("cancel Q^TF(B). The native-vacuum question remains a named reframe dependency,")
        log("not a verdict or claim-status move.")

    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
