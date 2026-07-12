#!/usr/bin/env python3
r"""
W48 / H59 -- Krein loop-positivity gate at the negative AF fixed ratio.

Purpose:
  H57/H60 firmed the coupling-flow side: GU has a Gaussian UV fixed point / asymptotic freedom in
  the induced fourth-order gravity truncation, and the admissible AF trajectory sits at a negative
  fixed ratio f_0^2/f_2^2 < 0. H59 is the other UV condition: whether the GU-native keep-and-grade
  Krein rescue [P,S]=0 makes that negative-ratio direction physically admissible at LOOP level.

This script does NOT compute a loop amplitude and does NOT settle positivity. It turns H59 into an
executable evidence gate so later work cannot accidentally count any of these as enough:
  * AF flow / fixed-point evidence alone;
  * tree-level Bateman-Turok / Bender-Mannheim positivity only;
  * replacing GU's Krein keep-and-grade construction with a positive-Hilbert projection;
  * a signature-only kill that ignores the loop state-space test.

Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), stated explicitly:
  1. Gravity action: GU-native induced |II|^2 -> fourth-order Stelle/agravity couplings
     (f_2^2, f_0^2). H59 uses the negative fixed ratio found in H57; it does not rederive the flow.
  2. Ghost clearance: GU-native keep-and-grade Krein structure [P,S]=0, P the Cartan involution of
     so(9,5). The positive-Hilbert/SUSY projection construction is rejected as the wrong object.
  3. Positivity: loop-level Born-rule / projected probability positivity, not pseudo-unitarity alone.
     Tree-level positivity and all-orders optical-theorem claims are insufficient by themselves.

Verdict vocabulary:
  READY_FOR_LOOP_POSITIVITY_COMPUTE means the evidence packet is well-posed enough to run H59.
  CANDIDATE_ADMISSIBLE_REVIEW_REQUIRED / CANDIDATE_OBSTRUCTION_REVIEW_REQUIRED are review gates,
  not claim-status changes. This file never emits RESOLVED.

Reproducible: python tests/W48_H59_krein_loop_positivity_gate.py
No canon/verdict/claim-status file touched. Exploration-grade gate.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import math
import os
import sys
from dataclasses import dataclass
from enum import Enum

TOL = 1e-9
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# Import the H57 Stage-1 beta system quietly so the H59 target is anchored to the actual AF flow.
_HERE = os.path.dirname(os.path.abspath(__file__))
_STAGE1 = os.path.join(_HERE, "W45_H57_stage1_beta_system.py")
_spec = importlib.util.spec_from_file_location("W45_stage1_for_H59", _STAGE1)
S1 = importlib.util.module_from_spec(_spec)
sys.modules["W45_stage1_for_H59"] = S1
with contextlib.redirect_stdout(io.StringIO()):
    try:
        _spec.loader.exec_module(S1)
    except SystemExit:
        pass

BetaSystem = S1.BetaSystem


class GateStatus(str, Enum):
    REJECT_WRONG_CONSTRUCTION = "REJECT_WRONG_CONSTRUCTION"
    INSUFFICIENT_FLOW_ONLY = "INSUFFICIENT_FLOW_ONLY"
    INSUFFICIENT_TREE_ONLY = "INSUFFICIENT_TREE_ONLY"
    NEEDS_SOURCE_ACTION = "NEEDS_SOURCE_ACTION"
    NEEDS_INTERNAL_GHOST_RULE = "NEEDS_INTERNAL_GHOST_RULE"
    NEEDS_IR_REGULATOR = "NEEDS_IR_REGULATOR"
    NEEDS_COUNTERTERM_CLOSURE = "NEEDS_COUNTERTERM_CLOSURE"
    NEEDS_KREIN_DIAGONALIZABILITY = "NEEDS_KREIN_DIAGONALIZABILITY"
    READY_FOR_LOOP_POSITIVITY_COMPUTE = "READY_FOR_LOOP_POSITIVITY_COMPUTE"
    NO_H59_VERDICT = "NO_H59_VERDICT"
    CANDIDATE_ADMISSIBLE_REVIEW_REQUIRED = "CANDIDATE_ADMISSIBLE_REVIEW_REQUIRED"
    CANDIDATE_OBSTRUCTION_REVIEW_REQUIRED = "CANDIDATE_OBSTRUCTION_REVIEW_REQUIRED"


@dataclass(frozen=True)
class EvidencePacket:
    """Minimal evidence flags for an H59 loop-positivity packet."""

    name: str
    construction: str
    negative_fixed_ratio_target: bool = False
    af_flow_computed: bool = False
    uses_positive_hilbert_projection: bool = False
    tree_p_commutation: bool = False
    tree_projector_born_positive: bool = False
    built_source_action: bool = False
    renormalized_p_commutation: bool = False
    counterterms_p_closed: bool = False
    krein_diagonalizable_real_spectrum: bool = False
    no_jordan_boundary: bool = False
    internal_odd_ghost_rule_or_cancellation: bool = False
    ir_regulator_and_inclusive_sum: bool = False
    loop_amplitudes_computed: bool = False
    loop_optical_theorem_projected: bool = False
    loop_born_rule_positive: bool = False
    cutkosky_or_spectral_density_check: bool = False
    rs_constraint_closure: bool = False
    signature_only_kill: bool = False


def h57_fixed_ratios() -> tuple[float, float]:
    """Return the two f_0^2/f_2^2 fixed-ratio roots from H57 Stage 2."""

    bs = BetaSystem()
    a = 5.0 / 6.0 + bs.d_rs_r2
    b = 5.0 + bs.b2()
    c = 5.0 / 3.0
    disc = b * b - 4.0 * a * c
    assert disc > 0.0
    r1 = (-b + math.sqrt(disc)) / (2.0 * a)
    r2 = (-b - math.sqrt(disc)) / (2.0 * a)
    return tuple(sorted((r1, r2)))


def pre_gate(packet: EvidencePacket) -> GateStatus:
    """Decide whether a packet is ready for an actual H59 loop-positivity computation."""

    if packet.uses_positive_hilbert_projection or packet.construction != "krein_keep_and_grade":
        return GateStatus.REJECT_WRONG_CONSTRUCTION
    if packet.signature_only_kill and not packet.loop_amplitudes_computed:
        return GateStatus.NO_H59_VERDICT
    if packet.af_flow_computed and not packet.tree_p_commutation and not packet.built_source_action:
        return GateStatus.INSUFFICIENT_FLOW_ONLY
    if packet.tree_p_commutation and packet.tree_projector_born_positive and not packet.loop_amplitudes_computed:
        if not packet.built_source_action:
            return GateStatus.INSUFFICIENT_TREE_ONLY
    if not packet.negative_fixed_ratio_target:
        return GateStatus.INSUFFICIENT_FLOW_ONLY
    if not packet.built_source_action:
        return GateStatus.NEEDS_SOURCE_ACTION
    if not packet.renormalized_p_commutation:
        return GateStatus.INSUFFICIENT_TREE_ONLY
    if not packet.counterterms_p_closed:
        return GateStatus.NEEDS_COUNTERTERM_CLOSURE
    if not packet.krein_diagonalizable_real_spectrum or not packet.no_jordan_boundary:
        return GateStatus.NEEDS_KREIN_DIAGONALIZABILITY
    if not packet.internal_odd_ghost_rule_or_cancellation:
        return GateStatus.NEEDS_INTERNAL_GHOST_RULE
    if not packet.ir_regulator_and_inclusive_sum:
        return GateStatus.NEEDS_IR_REGULATOR
    if not packet.rs_constraint_closure:
        return GateStatus.NEEDS_SOURCE_ACTION
    return GateStatus.READY_FOR_LOOP_POSITIVITY_COMPUTE


def verdict_gate(packet: EvidencePacket) -> GateStatus:
    """Review gate after a real loop computation exists. This never changes claim status by itself."""

    ready = pre_gate(packet)
    if ready != GateStatus.READY_FOR_LOOP_POSITIVITY_COMPUTE:
        return ready
    if not packet.loop_amplitudes_computed:
        return GateStatus.NO_H59_VERDICT
    negative_loop_result = (
        not packet.loop_optical_theorem_projected
        or not packet.loop_born_rule_positive
        or not packet.cutkosky_or_spectral_density_check
        or not packet.no_jordan_boundary
    )
    if negative_loop_result:
        return GateStatus.CANDIDATE_OBSTRUCTION_REVIEW_REQUIRED
    return GateStatus.CANDIDATE_ADMISSIBLE_REVIEW_REQUIRED


log("=" * 92)
log("W48 / H59 -- KREIN LOOP-POSITIVITY GATE AT THE NEGATIVE AF FIXED RATIO")
log("=" * 92)

ratios = h57_fixed_ratios()
small_ratio = max(ratios)
large_ratio = min(ratios)
log(f"  H57 fixed ratios r=f_0^2/f_2^2: {large_ratio:.5f}, {small_ratio:.5f}")
check(
    "H1  H59 target is anchored to H57's AF trajectory: both fixed ratios are negative, so the "
    "question is the wrong-sign conformal/Krein admissibility question, not another flow search",
    large_ratio < 0.0 and small_ratio < 0.0 and abs(small_ratio - (-0.0848)) < 0.002,
    f"roots = ({large_ratio:.5f}, {small_ratio:.5f})",
)

wrong_construction = EvidencePacket(
    name="positive Hilbert substitution",
    construction="positive_hilbert_projection",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
    uses_positive_hilbert_projection=True,
)
check(
    "G1  positive-Hilbert / remove-the-ghost substitution is rejected: H59 must use GU's "
    "keep-and-grade Krein construction, not a SUSY/Hilbert projection",
    pre_gate(wrong_construction) == GateStatus.REJECT_WRONG_CONSTRUCTION,
    pre_gate(wrong_construction).value,
)

flow_only = EvidencePacket(
    name="H57/H60 AF flow only",
    construction="krein_keep_and_grade",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
)
check(
    "G2  AF flow evidence alone is insufficient: a UV fixed point in couplings does not settle "
    "loop positivity of states",
    pre_gate(flow_only) == GateStatus.INSUFFICIENT_FLOW_ONLY,
    pre_gate(flow_only).value,
)

tree_only = EvidencePacket(
    name="tree-level Bateman-Turok only",
    construction="krein_keep_and_grade",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
    tree_p_commutation=True,
    tree_projector_born_positive=True,
)
check(
    "G3  tree-level [P,S]=0 / projector positivity is insufficient for H59: loop-level Born-rule "
    "positivity is the open frontier",
    pre_gate(tree_only) == GateStatus.INSUFFICIENT_TREE_ONLY,
    pre_gate(tree_only).value,
)

source_no_internal_rule = EvidencePacket(
    name="source action without internal ghost rule",
    construction="krein_keep_and_grade",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
    tree_p_commutation=True,
    tree_projector_born_positive=True,
    built_source_action=True,
    renormalized_p_commutation=True,
    counterterms_p_closed=True,
    krein_diagonalizable_real_spectrum=True,
    no_jordan_boundary=True,
    ir_regulator_and_inclusive_sum=True,
    rs_constraint_closure=True,
)
check(
    "G4  a built source action still is not enough unless odd/internal ghost-parity states have a "
    "loop rule or cancellation mechanism",
    pre_gate(source_no_internal_rule) == GateStatus.NEEDS_INTERNAL_GHOST_RULE,
    pre_gate(source_no_internal_rule).value,
)

source_no_ir = EvidencePacket(
    name="source action without IR treatment",
    construction="krein_keep_and_grade",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
    tree_p_commutation=True,
    tree_projector_born_positive=True,
    built_source_action=True,
    renormalized_p_commutation=True,
    counterterms_p_closed=True,
    krein_diagonalizable_real_spectrum=True,
    no_jordan_boundary=True,
    internal_odd_ghost_rule_or_cancellation=True,
    rs_constraint_closure=True,
)
check(
    "G5  H59 requires an IR regulator plus inclusive/resummed observable layer, because the known "
    "Bateman-Turok loop obstacle is collinear/asymptotic-state positivity",
    pre_gate(source_no_ir) == GateStatus.NEEDS_IR_REGULATOR,
    pre_gate(source_no_ir).value,
)

signature_kill = EvidencePacket(
    name="negative ratio declared fatal without loop computation",
    construction="krein_keep_and_grade",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
    signature_only_kill=True,
)
check(
    "G6  a signature-only kill is not accepted: the negative fixed ratio is exactly the H59 test "
    "target, not by itself a verdict",
    pre_gate(signature_kill) == GateStatus.NO_H59_VERDICT,
    pre_gate(signature_kill).value,
)

ready_packet = EvidencePacket(
    name="complete H59 precompute packet",
    construction="krein_keep_and_grade",
    negative_fixed_ratio_target=True,
    af_flow_computed=True,
    tree_p_commutation=True,
    tree_projector_born_positive=True,
    built_source_action=True,
    renormalized_p_commutation=True,
    counterterms_p_closed=True,
    krein_diagonalizable_real_spectrum=True,
    no_jordan_boundary=True,
    internal_odd_ghost_rule_or_cancellation=True,
    ir_regulator_and_inclusive_sum=True,
    rs_constraint_closure=True,
)
check(
    "G7  a complete precompute packet is READY_FOR_LOOP_POSITIVITY_COMPUTE, not a positivity verdict",
    pre_gate(ready_packet) == GateStatus.READY_FOR_LOOP_POSITIVITY_COMPUTE
    and verdict_gate(ready_packet) == GateStatus.NO_H59_VERDICT,
    f"pre={pre_gate(ready_packet).value}; verdict={verdict_gate(ready_packet).value}",
)

positive_loop_packet = EvidencePacket(
    **{**ready_packet.__dict__,
       "name": "hypothetical positive loop computation",
       "loop_amplitudes_computed": True,
       "loop_optical_theorem_projected": True,
       "loop_born_rule_positive": True,
       "cutkosky_or_spectral_density_check": True}
)
negative_loop_packet = EvidencePacket(
    **{**ready_packet.__dict__,
       "name": "hypothetical failed loop positivity",
       "loop_amplitudes_computed": True,
       "loop_optical_theorem_projected": True,
       "loop_born_rule_positive": False,
       "cutkosky_or_spectral_density_check": True}
)
check(
    "G8  even after a positive loop computation, the gate emits a review-required candidate rather "
    "than silently changing scientific status",
    verdict_gate(positive_loop_packet) == GateStatus.CANDIDATE_ADMISSIBLE_REVIEW_REQUIRED,
    verdict_gate(positive_loop_packet).value,
)
check(
    "G9  a failed loop Born-rule positivity check becomes a review-required obstruction candidate, "
    "not an automatic repo verdict",
    verdict_gate(negative_loop_packet) == GateStatus.CANDIDATE_OBSTRUCTION_REVIEW_REQUIRED,
    verdict_gate(negative_loop_packet).value,
)

log("\n" + "=" * 92)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert large_ratio < 0.0 and small_ratio < 0.0, "H57 fixed-ratio target is not negative"
assert pre_gate(wrong_construction) == GateStatus.REJECT_WRONG_CONSTRUCTION
assert pre_gate(flow_only) == GateStatus.INSUFFICIENT_FLOW_ONLY
assert pre_gate(tree_only) == GateStatus.INSUFFICIENT_TREE_ONLY
assert pre_gate(source_no_internal_rule) == GateStatus.NEEDS_INTERNAL_GHOST_RULE
assert pre_gate(source_no_ir) == GateStatus.NEEDS_IR_REGULATOR
assert pre_gate(signature_kill) == GateStatus.NO_H59_VERDICT
assert pre_gate(ready_packet) == GateStatus.READY_FOR_LOOP_POSITIVITY_COMPUTE
assert verdict_gate(ready_packet) == GateStatus.NO_H59_VERDICT
assert verdict_gate(positive_loop_packet) == GateStatus.CANDIDATE_ADMISSIBLE_REVIEW_REQUIRED
assert verdict_gate(negative_loop_packet) == GateStatus.CANDIDATE_OBSTRUCTION_REVIEW_REQUIRED
assert npass == ntot, "some H59 gate checks failed"

log("")
log("VERDICT (gate only): H59 remains OPEN. The next valid H59 work is a loop-positivity computation")
log("on a built source action at the negative AF fixed ratio, with internal ghost-state rules, IR")
log("treatment, P-closed counterterms, Krein diagonalizability, and projected Born-rule positivity.")
log("This file records readiness criteria only; it does not settle positivity or change status.")
raise SystemExit(0)
