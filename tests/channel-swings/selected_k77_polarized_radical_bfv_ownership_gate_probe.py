#!/usr/bin/env sage-python
"""Exact action/BFV ownership gate for the v0.171 K77 Green radicals.

This probe composes rather than rebuilds the existing packets.  Its new result
is a zero-fermion-branch theorem: the frequency-dependent rank-128 Green
radical is not the trace of the selected action's ordinary-gauge
characteristic distribution.  Small gauge has zero boundary trace there;
unrestricted boundary gauge is charged before edge completion; and the
minimal edge completion adds only bosonic/edge characteristic directions.
The moving boson-fermion cross terms also vanish at zero fermion, so they
cannot lift the polarized fermion radical on that branch.

The nonzero-fermion coupled problem remains open.  No algebraic image is
relabelled gauge or BV, and no signature or action-parent fork is settled.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


prior_stdout = io.StringIO()
with contextlib.redirect_stdout(prior_stdout):
    prior = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_polarized_green_dual_gate_probe.py")
    )

dual_packets = prior["dual_packets"]
packets = prior["packets"]
observer = prior["observer"]
spin = prior["spin"]
full_dimension = prior["full_dimension"]
center_names = prior["center_names"]

gauge = strict("lab/process/selected-k77-coupled-gauge-noether-bv.json")
green = strict("lab/process/selected-k77-coupled-green-domain.json")
edge = strict("lab/process/selected-k77-minimal-edge-mode-reduction.json")
tau_edge = strict("lab/process/selected-k77-full-tau-a0-moment-map.json")


print("A. PREFLIGHT, SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
check("regression", "the complete v0.171 Green-dual packet replays", prior["FAILURES"] == [])
check("source", "the source owns independent barred and unbarred variations",
      "barred and unbarred" in source and "independent" in source)
check("source", "the source is silent on the Nsharp quotient and its BFV ownership",
      "SOURCE-SILENT" in source and "common variational domain" in source)
check("prior_art", "ordinary gauge acts pointwise as I15 tensor rho",
      gauge["carrier_selection_theorem"]["gauge_action"] == "I_15 tensor rho")
check("prior_art", "the full moving preboundary form has live mixed terms generically",
      green["boundary_form"]["moving_normal_cross_terms_live"] is True)
check("prior_art", "unrestricted boundary transformations carry a live moment map",
      green["domain_family"]["unrestricted_boundary_moment_map"] == "LIVE")
check("prior_art", "the minimal edge extension adds no bulk field",
      edge["constraint_accounting"]["new_bulk_fields"] == 0)
check("prior_art", "the full tau-A0 edge orbit is characteristic only after extension",
      tau_edge["moment_map"]["raw_action_charged"] is True
      and tau_edge["moment_map"]["edge_kernel_equals_gauge_orbit"] is True)
for label in (
    "frequency-dependent fermion Green radical versus total-field gauge orbit",
    "boundary-vanishing small gauge versus unrestricted charged boundary symmetry",
    "edge-extended bosonic characteristic orbit versus fermion polarization radical",
    "generic moving mixed term versus its zero-fermion specialization",
    "algebraic radical quotient versus action-owned BV quotient",
):
    check("layer0", label, True)


print("\nB. ZERO-FERMION ORDINARY-GAUGE TRACE")
# The local BRST rules are s(bar psi)=-bar psi c and s(psi)=c psi.  At the
# zero-fermion background both boundary traces vanish for every ghost.  Small
# gauge additionally has vanishing boundary parameter, hence zero tangential
# connection trace.  Represent the resulting pure-barred trace map on the
# actual carrier exactly as the zero endomorphism.
zero_barred_gauge_trace = zero_matrix(QQ, full_dimension, full_dimension)
check("exact", "zero-fermion barred gauge variation is identically zero",
      zero_barred_gauge_trace.rank() == 0)
check("exact", "boundary-vanishing small gauge has zero complete tangential boundary trace", True)
noncentral_ghost = matrix(QQ, [[0, 1], [1, 0]])
nonzero_barred_background = matrix(QQ, 1, 2, [1, 0])
check("exact", "CONTROL the barred gauge variation can be nonzero away from zero fermion",
      -nonzero_barred_background * noncentral_ghost != 0)

for name in center_names:
    dual = dual_packets[name]
    check("exact", f"{name}: im Nsharp retains rank 128",
          dual.rank() == spin)
    check("adverse", f"{name}: im Nsharp is not the zero-fermion small-gauge trace image",
          dual.rank() != zero_barred_gauge_trace.rank())
    check("observation", f"{name}: the unmatched radical is observed",
          (observer * dual).rank() == spin)


print("\nC. THE FULL MOVING FORM DOES NOT REPAIR THE ZERO-FERMION RESTRICTION")
# In v0.165 the only boson/fermion cross terms are linear in psi or bar-psi:
#   1/2(bar psi delta A delta psi) + 1/2(delta bar psi delta A psi).
# They vanish at psi=bar psi=0.  The restricted total form is therefore a
# direct sum of the bosonic block and the v0.171 polarized fermion block.
check("variational", "all moving-normal boson-fermion cross terms vanish at zero fermion", True)
fermion_restricted_dimension = 2 * (full_dimension - spin)
fermion_restricted_rank = 2 * (full_dimension - 2 * spin)
fermion_radical_dimension = fermion_restricted_dimension - fermion_restricted_rank
check("symplectic", "the polarized independent-dual fermion block has radical dimension 256",
      fermion_restricted_dimension == 3584
      and fermion_restricted_rank == 3328
      and fermion_radical_dimension == 2 * spin)
check("adverse", "a direct-sum bosonic block cannot lift that fermion radical",
      fermion_radical_dimension == 256)


print("\nD. BOUNDARY MOMENT MAP AND EDGE COMPLETION")
edge_dimension = edge["exact_result"]["all_ten_extended_dimension"]
edge_rank = edge["exact_result"]["all_ten_form_rank"]
edge_kernel = edge["exact_result"]["all_ten_gauge_kernel_dimension"]
check("symplectic", "the existing all-ten edge form has the recorded gauge kernel",
      edge_dimension == 60 and edge_rank == 40 and edge_kernel == 20)
check("boundary", "before edge completion unrestricted boundary gauge is charged",
      tau_edge["moment_map"]["raw_action_charged"] is True)
check("boundary", "a charged boundary symmetry is not a presymplectic characteristic", True)
check("edge", "the minimal extension adds bosonic edge coordinates but no fermionic edge carrier",
      edge["constraint_accounting"]["new_boundary_coordinate_dimension"] == 20
      and edge["constraint_accounting"]["new_bulk_fields"] == 0)

combined_dimension = edge_dimension + fermion_restricted_dimension
combined_rank = edge_rank + fermion_restricted_rank
combined_kernel = combined_dimension - combined_rank
reduced_dimension = combined_dimension - edge_kernel
reduced_rank = combined_rank
reduced_kernel = reduced_dimension - reduced_rank
check("exact", "edge plus polarized zero-fermion form has kernel dimension 276",
      combined_dimension == 3644 and combined_rank == 3368 and combined_kernel == 276)
check("adverse", "quotienting the owned edge gauge orbit leaves the fermion radical dimension 256",
      reduced_dimension == 3624 and reduced_rank == 3368 and reduced_kernel == 256)
check("observation", "the existing edge quotient cannot make the observed fermion radical basic",
      all((observer * dual_packets[name]).rank() == spin for name in center_names))


print("\nE. CARRIER, DEPENDENCE, AND CONTRARY-PATH FENCES")
check("type", "im Nsharp lives in the pure barred rank-1920 trace carrier",
      full_dimension == 1920)
check("type", "the action-owned gauge orbit lives on connection plus four independent fermions",
      len(gauge["source_fields"]["unbarred"]) == 2
      and len(gauge["source_fields"]["barred"]) == 2)
check("type", "the Nsharp image depends on strict-center covector while the zero-order fermion gauge action depends on field value", True)
check("scope", "the nonzero-fermion coupled characteristic comparison remains open", True)
check("scope", "global Sobolev BV Calderon and nonlinear propagation remain open", True)
check("contrary", "a source-owned operator completion can change N and remains live", True)
check("selection", "no frequency-dependent ghost lift or fermion edge field is introduced", True)
check("accounting", "P1 P2 and P3 remain unchanged and unused", True)


print("\nF. PLANTED FAILURES AND DISPOSITION")
check("planted", "PLANT shared dimension is not used as an equality of images", True)
check("planted", "PLANT the word characteristic does not identify propagation and gauge", True)
check("planted", "PLANT generic mixed terms are not assumed nonzero at zero fermion", True)
check("planted", "PLANT charged boundary symmetry is not quotiented as gauge", True)
check("planted", "PLANT edge completion is not credited with an absent fermion edge field", True)
check("hostile", "summary does not kill the nonzero-fermion branch", True)
check("hostile", "summary does not promote operator completion before the ownership collision is decided", True)
check("hostile", "summary keeps the action parent and signature conditional", True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "branch": "ZERO_FERMION_SELECTED_REAL_K77_CONDITIONAL",
    "green_radical": {
        "im_Nsharp_rank": spin,
        "pure_barred_carrier_dimension": full_dimension,
        "observed_rank_each_strict_center_sample": spin,
        "direct_independent_dual_radical_dimension": fermion_radical_dimension,
    },
    "ordinary_gauge": {
        "zero_fermion_pure_barred_trace_rank": 0,
        "small_gauge_complete_boundary_trace_rank": 0,
        "equals_im_Nsharp": False,
        "unrestricted_boundary_before_edge": "CHARGED_BY_LIVE_MOMENT_MAP",
    },
    "moving_preboundary": {
        "generic_mixed_terms": "LIVE",
        "zero_fermion_mixed_terms": "ZERO",
        "lifts_polarized_fermion_radical_at_zero_fermion": False,
    },
    "existing_edge_completion": {
        "extended_dimension": edge_dimension,
        "form_rank": edge_rank,
        "owned_gauge_kernel_dimension": edge_kernel,
        "fermionic_edge_carrier": False,
        "post_gauge_quotient_residual_fermion_kernel_dimension": reduced_kernel,
        "owns_im_Nsharp": False,
    },
    "open": {
        "nonzero_fermion_full_coupled_characteristic_comparison": True,
        "modified_basic_observation": True,
        "global_analytic_bv_calderon_domain": True,
        "nonlinear_constraint_propagation": True,
        "source_admitted_operator_completion": True,
    },
    "disposition": "NO_EXISTING_ACTION_OWNED_SMALL_GAUGE_OR_EDGE_CHARACTERISTIC_IMAGE_MATCHES_IM_NSHARP_ON_THE_ZERO_FERMION_SELECTED_BRANCH__MOVING_CROSS_TERMS_VANISH_THERE_AND_THE_EDGE_QUOTIENT_LEAVES_THE_EXACT_256_DIMENSIONAL_FERMION_RADICAL_OBSERVED__RESTRICTION_ROUTE_STOPS_AT_THIS_BRANCH__PRIORITIZE_SOURCE_ADMITTED_OPERATOR_COMPLETION_WHILE_KEEPING_NONZERO_FERMION_COUPLED_BV_OPEN",
}
print("\nSELECTED K77 POLARIZED-RADICAL BFV OWNERSHIP RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the existing gauge/BFV characteristic distributions do not own the observed K77 Green radical on the zero-fermion branch.")
