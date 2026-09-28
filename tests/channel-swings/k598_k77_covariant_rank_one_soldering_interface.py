#!/usr/bin/env python3
"""K598 covariant completion of K596 rank-one corrected-carrier packets."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k598-k77-covariant-rank-one-soldering-interface.json"


def strict(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


def mm(a, b):
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b):
    return [[Fraction(x) + Fraction(y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a, b):
    return [[Fraction(x) - Fraction(y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def tr(a):
    return [list(row) for row in zip(*a)]


def scale(c, a):
    return [[Fraction(c) * Fraction(x) for x in row] for row in a]


def outer(y, x, c=1):
    return [[Fraction(c) * Fraction(yi) * Fraction(xj) for xj in x] for yi in y]


def zero(a):
    return all(Fraction(x) == 0 for row in a for x in row)


def frob2(a):
    return sum(Fraction(x) ** 2 for row in a for x in row)


def q(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_q(a):
    return [[q(x) for x in row] for row in a]


def rotation(t: Fraction):
    d = 1 + t * t
    return [[(1 - t * t) / d, -2 * t / d], [2 * t / d, (1 - t * t) / d]]


def rotation_prime(t: Fraction):
    d2 = (1 + t * t) ** 2
    return [[-4 * t / d2, 2 * (t * t - 1) / d2], [2 * (1 - t * t) / d2, -4 * t / d2]]


def transported(t: Fraction, base):
    u = rotation(t)
    return mm(mm(u, base), tr(u))


def transported_prime(t: Fraction, base):
    u, up = rotation(t), rotation_prime(t)
    return add(mm(mm(up, base), tr(u)), mm(mm(u, base), tr(up)))


def sample(arrow: str, coefficient: Fraction, source, target, t: Fraction) -> dict:
    p0 = [[1, 0], [0, 0]]
    c0 = outer(target, source, coefficient)
    u, up = rotation(t), rotation_prime(t)
    p, c = transported(t, p0), transported(t, c0)
    b = scale(-1, mm(up, tr(u)))
    defect = sub(mm(p, c), mm(c, p))
    covariant = add(transported_prime(t, c0), sub(mm(b, c), mm(c, b)))
    fixed_defect = sub(mm(p, c0), mm(c0, p))
    return {
        "arrow": arrow,
        "coefficient": q(coefficient),
        "t": q(t),
        "transported_typed_square_defect_norm_square": q(frob2(defect)),
        "covariant_derivative_norm_square": q(frob2(covariant)),
        "fixed_vector_shortcut_defect_norm_square": q(frob2(fixed_defect)),
        "transported_square_passes": zero(defect),
        "covariantly_parallel": zero(covariant),
    }


def build() -> dict:
    k441 = strict("lab/process/k441-k77-moving-corrected-boundary-transport.json")
    k589 = strict("lab/process/k589-k77-action-kt-exact-completion.json")
    k596 = strict("lab/process/k596-k77-rank-one-soldering-discriminator.json")
    coefficients = {"D2": Fraction(8736), "D1": Fraction(-56, 3)}
    times = [Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1)]
    rows = [sample(a, c, [1, 0], [1, 0], t) for a, c in coefficients.items() for t in times]
    cross_rows = [sample(a, c, [1, 0], [0, 1], t) for a, c in coefficients.items() for t in times]
    return {
        "schema_version": "1.0",
        "result_id": "K598-K77-COVARIANT-RANK-ONE-SOLDERING-INTERFACE",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "The minimal K441-covariant extension of a declared initial rank-one corrected-carrier packet for each K589 arrow, separating transport from action ownership of the initial vectors and Riesz return.",
        "gu_typed_objects": {
            "carrier": "one K441 fast/slow outgoing-incoming sign pair, repeated factorwise on the corrected rank-512 carrier",
            "projector": "Pi(t)=U(t)Pi(0)U(t)^T",
            "connection": "B(t)=-U'(t)U(t)^T",
            "coupling": "C(t)=U(t)C(0)U(t)^T with C(0)=c|y_0><x_0|",
            "result": "covariant rank-one soldering interface MAP-TYPE=graded-projector-intertwiner",
            "target": "both K589 arrows D2:H^21->Q^91 and D1:Q^91->M^70 after corrected-carrier lift",
        },
        "theorem": {
            "transported_typed_square": "Pi_target(t)C(t)=C(t)Pi_source(t) whenever the initial square holds",
            "covariant_parallelism": "C'(t)+B_target(t)C(t)-C(t)B_source(t)=0",
            "same_half_initial_packet": "K596 supplies the initial square for matching corrected-carrier halves",
            "opposite_half_initial_packet": "K596 rejects the initial square with rank-one defect norm |c|",
            "fixed_vectors_are_not_covariant": "Holding C(0) fixed while Pi(t) moves generally creates a nonzero defect.",
            "rank512_extension": "Repeat the exact two-dimensional identity on K441's 192 fast and 64 slow sign pairs and tensor with the K589 degree arrow.",
        },
        "exact_controls": {
            "K441_sample_points_replayed": [q(t) for t in times],
            "matching_half_rows": rows,
            "opposite_half_rows": cross_rows,
            "matching_half_all_squares_pass": all(r["transported_square_passes"] for r in rows),
            "matching_half_all_covariantly_parallel": all(r["covariantly_parallel"] for r in rows),
            "fixed_vector_shortcut_fires_at_mixed_points": all(Fraction(r["fixed_vector_shortcut_defect_norm_square"]) > 0 for r in rows if r["t"] in {"1/3", "1/2"}),
            "opposite_half_all_squares_fail": all(not r["transported_square_passes"] for r in cross_rows),
            "both_K589_arrows_exercised": {r["arrow"] for r in rows} == {"D1", "D2"},
        },
        "ownership_boundary": {
            "K441_owns_transport_and_moving_projector": k441["decision"]["moving_corrected_projectors_constructed"],
            "K589_owns_base_degree_arrows": k589["decision"]["K587_base_exact_completion_constructed"],
            "K596_owns_initial_rank_one_discriminator": k596["decision"]["conditional_rank_one_discriminator_emitted"],
            "selected_action_owns_initial_corrected_vectors": False,
            "selected_action_owns_K441_Riesz_return": False,
            "conditional_covariant_packet_constructed": True,
            "actual_action_owned_packet_constructed": False,
        },
        "decision": {
            "K596_extended_from_one_fibre_to_K441_transport": True,
            "fixed_vector_shortcut_rejected": True,
            "both_conditional_covariant_K444_squares_emitted": True,
            "actual_action_owned_soldering_constructed": False,
            "K590_factorized_completion_retracted": False,
            "selected_source_action_rejected": False,
            "next_exact_input": "Supply, for one declared selected-I1B variation, action-owned initial corrected-carrier vectors x_0,y_0 and the Riesz return for D2 and D1. K598 then transports them uniquely and K596 decides the initial square; no expanded 512-by-512 search is required.",
        },
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Use K441's already exact associated-bundle transport before searching an unconstrained 512-by-512 coupling.",
            "retrieval_collision_result": "K596 decides one fibre and K441 owns transport; neither owns the action-selected initial vector/Riesz datum.",
            "strongest_alternative": "A full-field third derivative can supply the initial action datum but should not redundantly reconstruct the known carrier transport.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling the conditional transported packet action-owned, or holding the initial vectors fixed while the corrected projector moves.",
            "strongest_contrary_construction": "Opposite-half initial data remain obstructed at every transported fibre with the same rank-one defect norm.",
            "weakest_reproducibility_seam": "The exact rank-512 statement uses K441's repeated two-dimensional factorization rather than an expanded matrix.",
        },
        "claim_ceiling": "Exact minimal covariant completion of K596 on K441: a matching-half initial rank-one packet transports through every corrected-carrier fibre, remains parallel and satisfies both conditional K444 squares; a fixed-vector shortcut fails and an opposite-half packet stays obstructed. K441 transport does not action-own the initial vectors or Riesz return, so no actual selected-action square, nonlinear properness, source, ledger, canon, paper, public, novelty or physical conclusion moves.",
    }


def validate(p: dict) -> None:
    c, o, d = p["exact_controls"], p["ownership_boundary"], p["decision"]
    assert c["matching_half_all_squares_pass"] and c["matching_half_all_covariantly_parallel"]
    assert c["fixed_vector_shortcut_fires_at_mixed_points"] and c["opposite_half_all_squares_fail"] and c["both_K589_arrows_exercised"]
    assert o["conditional_covariant_packet_constructed"] and not o["actual_action_owned_packet_constructed"]
    assert d["both_conditional_covariant_K444_squares_emitted"] and not d["actual_action_owned_soldering_constructed"]
    assert not d["K590_factorized_completion_retracted"] and not d["selected_source_action_rejected"]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    payload = build(); validate(payload); rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered)
    else: print(rendered, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
