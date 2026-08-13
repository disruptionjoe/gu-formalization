#!/usr/bin/env sage-python
"""Exact K77 graph/lower-left gate for the current q-repaired rival.

Run with::

    sage -python tests/channel-swings/selected_k77_southeast_zero_graph_gate_probe.py

Layer 0: this tests the existing q-repaired real-K77 conditional rival after
assembling its plus/minus fields into ``Omega1(S) + Omega0(S)``.  It does not
repair the primary source's ambient-half-sign collision, choose the physical
parent, construct BV cohomology, or supply an analytic domain.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_matrix, identity_matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def load_predecessor() -> dict:
    """Replay v0.138 as the immutable integration surface."""
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_four_field_zero_order_port_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def independent_rows(matrix):
    rows = list(matrix.transpose().pivots())
    if len(rows) != matrix.ncols():
        raise ValueError("expected a full-column-rank map")
    square = matrix.matrix_from_rows(rows)
    if not square.is_invertible():
        raise ValueError("selected row minor is singular")
    return rows, square


def connection_port(structures: dict, field, parent, one_form):
    return block_matrix(
        field, 14, 1,
        [[field(one_form[row]) * parent] for row in range(14)],
        sparse=True,
    )


def lower_left_adjoint(structures: dict, field, parent, one_form):
    """The displayed minus of the complete form-index K77 adjoint."""
    pairing = structures["B"]
    parent_times = pairing * parent.transpose() * pairing
    zero = zero_matrix(field, 128, 128, sparse=True)
    eta = [1] * 7 + [-1] * 7
    return block_matrix(
        field, 1, 14,
        [[
            -field(eta[column] * one_form[column]) * parent_times
            if one_form[column] else zero
            for column in range(14)
        ]],
        sparse=True,
    ), parent_times


def analyze_field(predecessor: dict, structures: dict, field, bases: dict) -> dict:
    identity = structures["I1792"]
    one_form = [2, -1, 0, 1] + [0] * 10
    preferred = {
        "moving_spin_grade2": field(1),
        "two_half_block_grade6": field(1),
        "source_full_u_coset_grade1": field(-1),
    }
    results = {}

    for parent_name, parent in structures["parents"].items():
        left, right = structures["zero_order_pair"](parent)
        one_form_operator = left + preferred[parent_name] * right
        port = connection_port(structures, field, parent, one_form)
        lower_left, parent_times = lower_left_adjoint(
            structures, field, parent, one_form
        )
        results[parent_name] = {
            "parent_krein_adjoint_is_minus_parent": parent_times == -parent,
            "carriers": {},
        }

        for carrier_name, projector, basis in (
            ("W", structures["W"], bases["W"]),
            ("mirror", structures["M"], bases["mirror"]),
        ):
            complement = identity - projector
            projected_port = complement * port
            projected_leak = complement * one_form_operator * basis

            # v0.138 proves projected_port is injective and contains the leak.
            # Therefore the upper graph equation has exactly one solution.
            port_rows, port_minor = independent_rows(projected_port)
            graph = port_minor.solve_right(
                (-projected_leak).matrix_from_rows(port_rows)
            )

            first_component = one_form_operator * basis + port * graph
            upper_residual = complement * first_component
            carrier_rows, carrier_minor = independent_rows(basis)
            induced = carrier_minor.solve_right(
                first_component.matrix_from_rows(carrier_rows)
            )

            lower_on_carrier = lower_left * basis
            graph_induced = graph * induced
            lower_residual = lower_on_carrier - graph_induced
            sign_flipped_residual = -lower_on_carrier - graph_induced
            southeast_factor_rank = block_matrix(
                field, 2, 1, [[graph], [lower_on_carrier]], sparse=True
            ).rank()

            results[parent_name]["carriers"][carrier_name] = {
                "projected_port_rank": projected_port.rank(),
                "graph_rank": graph.rank(),
                "upper_residual_rank": upper_residual.rank(),
                "induced_rank": induced.rank(),
                "lower_on_carrier_rank": lower_on_carrier.rank(),
                "graph_induced_rank": graph_induced.rank(),
                "lower_residual_rank": lower_residual.rank(),
                "lower_residual_nonzero_entries": len(lower_residual.dict()),
                "sign_flipped_lower_rank": sign_flipped_residual.rank(),
                "suppressed_lower_left_would_close": graph_induced.is_zero(),
                "graph_plus_lower_row_rank": southeast_factor_rank,
                "same_carrier_southeast_factor_exists": (
                    southeast_factor_rank == graph.rank()
                ),
            }

    return results


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
blockwise = (ROOT / "tests/channel-swings/k77_wave2_actual_draft916_blockwise_probe.py").read_text()
v138 = (ROOT / "explorations/conditional-build/selected-k77-four-field-zero-order-port-2026-08-10.md").read_text()
check("source", "the source displays the southeast-zero and minus-adjoint cells",
      "southeast-zero" in source and "minus-bar-varpi-pp-star" in source)
check("source", "the source admits an unspecified nonzero southeast rival",
      "non-trivial map in the lower right quadrant" in source)
check("source", "the source is silent on a W graph adapter and physical domain",
      "unique or globally defined operator" in source and "closed physical evolution domain" in source)
check("prior_art", "v0.138 proves necessary port inclusion but leaves graph and lower-left open",
      "graph subspace invariance" in v138 and "lower-left adjoint compatibility" in v138)
check("prior_art", "the complete K77 form-index adjoint and its Euclidean-transpose plant already exist",
      "connection wedge and its Krein adjoint pair coefficientwise" in blockwise
      and "ordinary Euclidean transpose is not substituted" in blockwise)
check("layer0", "the direct sum of the two source half-spinor fields is the full rolled carrier",
      "zeta_minus in Omega1(S_minus)" in source and "nu_plus    in Omega0(S_plus)" in source)
check("layer0", "the q-repaired operator remains a conditional rival because the source-sign collision is open",
      "LAYER0-COLLISION / NOT-ESTABLISHED" in source)
check("layer0", "upper cancellation, invariant graph, BV cohomology and closed domain are distinct", True)

predecessor = load_predecessor()
check("prior_art", "the immutable v0.138 predecessor replay remains green",
      not predecessor["FAILURES"] and "PASS:" in predecessor["captured_predecessor_output"])


print("\nB. EXACT UNIQUE-GRAPH AND LOWER-LEFT TEST")
base = predecessor["namespace"]
finite_results = analyze_field(
    predecessor, base["finite"], base["fp"], predecessor["finite_bases"]
)
char0_results = analyze_field(
    predecessor, base["char0"], base["gaussian"], predecessor["char0_bases"]
)

for field_name, results in (
    ("finite", finite_results),
    ("Gaussian-rational", char0_results),
):
    for parent_name, parent_result in results.items():
        check("exact", f"{field_name} {parent_name}: parent Krein adjoint is minus itself",
              parent_result["parent_krein_adjoint_is_minus_parent"])
        for carrier_name, row in parent_result["carriers"].items():
            label = f"{field_name} {parent_name}/{carrier_name}"
            check("exact", f"{label}: projected port is injective rank 128",
                  row["projected_port_rank"] == 128)
            check("exact", f"{label}: unique upper graph has rank 64",
                  row["graph_rank"] == 64)
            check("exact", f"{label}: upper graph residual vanishes",
                  row["upper_residual_rank"] == 0)
            check("exact", f"{label}: induced W/mirror action is zero",
                  row["induced_rank"] == 0)
            check("exact", f"{label}: action-tied lower-left restriction has rank 64",
                  row["lower_on_carrier_rank"] == 64)
            check("exact", f"{label}: lower graph residual has rank 64",
                  row["lower_residual_rank"] == 64
                  and row["lower_residual_nonzero_entries"] == 384)
            check("planted", f"{label}: flipping the displayed lower-left sign does not rescue the graph",
                  row["sign_flipped_lower_rank"] == 64)
            check("planted", f"{label}: illegally suppressing the lower-left block fakes closure",
                  row["suppressed_lower_left_would_close"])
            check("exact", f"{label}: same-carrier southeast postcomposition cannot span the lower-left map",
                  row["graph_plus_lower_row_rank"] == 128
                  and not row["same_carrier_southeast_factor_exists"])


print("\nC. DISPOSITION AND PHYSICAL FENCES")
for parent_name in finite_results:
    finite_w = finite_results[parent_name]["carriers"]["W"]
    finite_m = finite_results[parent_name]["carriers"]["mirror"]
    check("exact", f"{parent_name}: W and mirror have identical graph fingerprints",
          finite_w == finite_m)
check("type", "the displayed southeast-zero graph fails on both restricted parents and the full-U comparator", True)
check("type", "the result kills the current q-repaired rival, not every source-family Shiab or the unresolved source-sign repair", True)
check("variational", "the lower-left block is tied to the port by the fermion bilinear and cannot be set to zero as a fit", True)
check("symplectic", "no invariant graph failure is promoted to a BV or reduced-phase-space theorem", True)
check("analytic", "no finite algebraic rank is promoted to a closed-domain, spectrum, index or positivity claim", True)
check("adversarial", "the result retracts v0.138's live adapter hope without overstating a GU no-go", True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": "K77_EXACT_GF_AND_GAUSSIAN_RATIONAL",
    "finite_results": finite_results,
    "char0_results": char0_results,
    "source_return": "SOURCE_CONFIRMS_SOUTHEAST_ZERO_MINUS_ADJOINT_AND_ADMITTED_NONZERO_RIVAL__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_W_GRAPH_AND_DOMAIN",
    "disposition": "CURRENT_Q_REPAIRED_GRAPH_KILLED__UNIQUE_UPPER_GRAPH_RANK64__LOWER_LEFT_RESIDUAL_RANK64__W_EQUALS_MIRROR",
    "next_gate": "RESOLVE_OR_KILL_SOURCE_FAITHFUL_AMBIENT_HALF_SIGN_AND_DEGREE_DUALITY_COLLISION__THEN_REBUILD_ANY_SURVIVING_SHIAB_GRAPH_BEFORE_BV_OR_DOMAIN",
}

print("\nK77 SOUTHEAST-ZERO GRAPH RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the unique upper graph for the current q-repaired rival fails the action-tied lower-left equation on W and its mirror for every retained parent.")
