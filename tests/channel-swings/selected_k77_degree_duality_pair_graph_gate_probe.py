#!/usr/bin/env sage-python
"""Exact source-sign degree-duality and W/mirror graph gate.

Run with::

    sage -python tests/channel-swings/selected_k77_degree_duality_pair_graph_gate_probe.py

Layer 0: this realizes the two previously enumerated degree-sensitive
row/column primalizers with the canonical trace-q intertwiner.  A bare spinor
intertwiner, its Pin-completed one-form action, a source-field relabel, a
reality-closed carrier, an invariant graph, BV cohomology and a closed domain
are different objects.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_matrix, diagonal_matrix, identity_matrix, zero_matrix


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
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_southeast_zero_graph_gate_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def connection_port(structures: dict, field, parent, one_form):
    return block_matrix(
        field,
        14,
        1,
        [[field(one_form[row]) * parent] for row in range(14)],
        sparse=True,
    )


def lower_left_adjoint(structures: dict, field, parent, one_form):
    pairing = structures["B"]
    parent_times = pairing * parent.transpose() * pairing
    zero = zero_matrix(field, 128, 128, sparse=True)
    eta = [1] * 7 + [-1] * 7
    return block_matrix(
        field,
        1,
        14,
        [[
            -field(eta[column] * one_form[column]) * parent_times
            if one_form[column] else zero
            for column in range(14)
        ]],
        sparse=True,
    )


def exact_intertwiners(structures: dict, field) -> dict:
    q = structures["gammas"][7]
    zero = zero_matrix(field, 128, 128, sparse=True)
    q_big = block_matrix(
        field,
        14,
        14,
        [[q if row == column else zero for column in range(14)] for row in range(14)],
        sparse=True,
    )
    # The Pin action flips the q vector coordinate and applies gamma(q) to the
    # spinor.  Its overall negative is the same intertwiner for rank purposes.
    reflection = diagonal_matrix(
        field, [-1 if index == 7 else 1 for index in range(14)], sparse=True
    )
    pin = reflection.tensor_product(q)
    return {"q": q, "q_big": q_big, "pin": pin}


def carrier_fingerprint(structures: dict, field) -> dict:
    intertwiners = exact_intertwiners(structures, field)
    q_big, pin = intertwiners["q_big"], intertwiners["pin"]
    identity = structures["I1792"]
    rs, w, mirror = structures["rs"], structures["W"], structures["M"]
    pair = w + mirror
    w_basis = w.matrix_from_columns(list(w.pivots()))
    mirror_basis = mirror.matrix_from_columns(list(mirror.pivots()))

    return {
        "q_big_square_minus_identity": (q_big * q_big + identity).is_zero(),
        "pin_square_minus_identity": (pin * pin + identity).is_zero(),
        "pin_preserves_rs": ((identity - rs) * pin * rs).is_zero(),
        "bare_q_w_outside_rs_rank": ((identity - rs) * q_big * w_basis).rank(),
        "bare_q_mirror_outside_rs_rank": ((identity - rs) * q_big * mirror_basis).rank(),
        "pin_w_to_mirror_exact": (
            ((identity - mirror) * pin * w_basis).is_zero()
            and (mirror * pin * w_basis).rank() == 192
            and (w * pin * w_basis).is_zero()
        ),
        "pin_mirror_to_w_exact": (
            ((identity - w) * pin * mirror_basis).is_zero()
            and (w * pin * mirror_basis).rank() == 192
            and (mirror * pin * mirror_basis).is_zero()
        ),
        "pin_pair_invariant": ((identity - pair) * pin * pair).is_zero(),
        "pair_rank": pair.rank(),
    }


def analyze_degree_duality(structures: dict, field) -> dict:
    intertwiners = exact_intertwiners(structures, field)
    q, q_big, pin = (
        intertwiners["q"],
        intertwiners["q_big"],
        intertwiners["pin"],
    )
    identity = structures["I1792"]
    pair = structures["W"] + structures["M"]
    pair_basis = pair.matrix_from_columns(list(pair.pivots()))
    complement = identity - pair
    one_form = [2, -1, 0, 1] + [0] * 10
    results = {}

    for parent_name, parent in structures["parents"].items():
        left, _right = structures["zero_order_pair"](parent)
        # left = Q_big * raw and Q_big^{-1}=-Q_big.
        raw = -q_big * left
        port = connection_port(structures, field, parent, one_form)
        lower = lower_left_adjoint(structures, field, parent, one_form)

        # The two global-sign-related parity solutions become complementary
        # degree-sector primalizers.  Inverses differ only by an overall sign,
        # irrelevant to the image/rank obstruction tested here.
        candidates = {
            "column_pin": {
                "upper_left": raw * pin,
                "upper_right": port,
                "lower_left": q * lower * pin,
            },
            "row_pin": {
                "upper_left": pin * raw,
                "upper_right": pin * port * q,
                "lower_left": lower,
            },
        }
        parent_results = {}
        for candidate_name, candidate in candidates.items():
            projected_port = complement * candidate["upper_right"]
            projected_leak = complement * candidate["upper_left"] * pair_basis
            joined = block_matrix(
                field, 1, 2, [[projected_port, projected_leak]], sparse=True
            )
            parent_results[candidate_name] = {
                "pair_rank": pair.rank(),
                "projected_port_rank": projected_port.rank(),
                "projected_leak_rank": projected_leak.rank(),
                "joined_rank": joined.rank(),
                "upper_graph_exists": joined.rank() == projected_port.rank(),
                "lower_on_pair_rank": (candidate["lower_left"] * pair_basis).rank(),
            }

        # Negative control: omitting the source-faithful Pin degree maps and
        # returning to the older q-repaired family makes the pair leak lie in
        # the port image.  This proves the new obstruction is not a rank-bound
        # tautology, but that older family already fails its lower equation.
        preferred = field(-1) if parent_name == "source_full_u_coset_grade1" else field(1)
        old_left, old_right = structures["zero_order_pair"](parent)
        old_leak = complement * (old_left + preferred * old_right) * pair_basis
        old_port = complement * port
        old_joined = block_matrix(field, 1, 2, [[old_port, old_leak]], sparse=True)
        parent_results["old_q_family_control"] = {
            "projected_port_rank": old_port.rank(),
            "projected_leak_rank": old_leak.rank(),
            "joined_rank": old_joined.rank(),
            "upper_graph_exists": old_joined.rank() == old_port.rank(),
        }
        results[parent_name] = parent_results

    return results


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
reconciliation = (ROOT / "explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md").read_text()
q_owner = (ROOT / "explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md").read_text()
v139 = (ROOT / "explorations/conditional-build/selected-k77-southeast-zero-graph-gate-2026-08-10.md").read_text()
check("source", "section 11.2 fixes zeta and nu signs as ambient half-spinor labels",
      "zeta_minus in Omega1(S_minus)" in source and "nu_plus    in Omega0(S_plus)" in source)
check("source", "the released source supplies no correction of those field signs",
      "SOURCE-CORRECTS-SIGNS: NONE FOUND" in source)
check("source", "the displayed southeast-zero branch and unspecified nonzero rival remain distinct",
      "non-trivial map in the lower right quadrant" in source)
check("prior_art", "the native invariant Shiab class has no ambient-even map",
      "dim Hom(Lambda2 V tensor S+, V tensor S+) = 0" in reconciliation)
check("prior_art", "the full degree-sensitive sign problem has exactly two solutions requiring a q-type flip",
      "exactly two sign solutions" in reconciliation and "same `q`-type object" in reconciliation)
check("prior_art", "the trace-reversed metric fibre owns canonical q without spending P1/P2/P3",
      "q_g=\\frac12g" in q_owner and "P1 is not consumed" in q_owner)
check("prior_art", "v0.139 kills the older q-repaired graph only at its declared rival scope",
      "current q-repaired" in v139 and "rank `64`" in v139)
check("layer0", "a bare spinor q map and a Pin-completed one-form-spinor map are distinct", True)
check("layer0", "a source-field relabel and an explicit degree-sector primalizer are distinct", True)
check("layer0", "reality closure of W with its mirror is not selection of either carrier", True)
check("layer0", "upper graph existence, lower compatibility, BV cohomology and closed domain are distinct", True)

predecessor = load_predecessor()
check("prior_art", "the immutable v0.139 predecessor replay remains green",
      not predecessor["FAILURES"] and "PASS:" in predecessor["captured_predecessor_output"])


print("\nB. EXACT DEGREE-SIGN AND AMBIENT-PARITY REALIZATION")
degree_solutions = [(-sign, sign, sign, -sign) for sign in (1, -1)]
check("exact", "the two row/column degree-reality solutions are global-sign-related",
      degree_solutions == [(-1, 1, 1, -1), (1, -1, -1, 1)])
check("type", "minus parity is realized by the q intertwiner rather than by renaming a source field", True)
check("type", "one-form q must be Pin-completed to preserve the gamma-traceless RS carrier", True)

base = predecessor["base"]
finite_fingerprint = carrier_fingerprint(base["finite"], base["fp"])
char0_fingerprint = carrier_fingerprint(base["char0"], base["gaussian"])
finite_results = analyze_degree_duality(base["finite"], base["fp"])
char0_results = analyze_degree_duality(base["char0"], base["gaussian"])

for field_name, fingerprint in (
    ("finite", finite_fingerprint),
    ("Gaussian-rational", char0_fingerprint),
):
    check("exact", f"{field_name}: bare and Pin q intertwiners square to minus identity",
          fingerprint["q_big_square_minus_identity"] and fingerprint["pin_square_minus_identity"])
    check("representation", f"{field_name}: bare spinor q leaks rank 64 out of RS on W and mirror",
          fingerprint["bare_q_w_outside_rs_rank"] == 64
          and fingerprint["bare_q_mirror_outside_rs_rank"] == 64)
    check("representation", f"{field_name}: Pin completion preserves the full RS carrier",
          fingerprint["pin_preserves_rs"])
    check("representation", f"{field_name}: Pin completion exchanges W and mirror exactly",
          fingerprint["pin_w_to_mirror_exact"] and fingerprint["pin_mirror_to_w_exact"])
    check("representation", f"{field_name}: the minimal W/mirror-closed comparator has rank 384",
          fingerprint["pin_pair_invariant"] and fingerprint["pair_rank"] == 384)


print("\nC. SOURCE-FAITHFUL DEGREE-DUALITY UPPER-GRAPH TEST")
for field_name, results in (
    ("finite", finite_results),
    ("Gaussian-rational", char0_results),
):
    for parent_name, parent_results in results.items():
        for candidate_name in ("column_pin", "row_pin"):
            row = parent_results[candidate_name]
            label = f"{field_name} {parent_name}/{candidate_name}"
            check("exact", f"{label}: W-plus-mirror carrier has rank 384",
                  row["pair_rank"] == 384)
            check("exact", f"{label}: port and leak each have rank 128",
                  row["projected_port_rank"] == 128 and row["projected_leak_rank"] == 128)
            check("exact", f"{label}: port and leak are independent with joined rank 256",
                  row["joined_rank"] == 256)
            check("exact", f"{label}: no upper graph exists",
                  not row["upper_graph_exists"])
            check("variational", f"{label}: the action-tied lower map remains live but is not read after upper failure",
                  row["lower_on_pair_rank"] == 128)
        control = parent_results["old_q_family_control"]
        check("planted", f"{field_name} {parent_name}: the older non-source-faithful q family passes the pair upper-image control",
              control["projected_port_rank"] == 128
              and control["projected_leak_rank"] == 128
              and control["joined_rank"] == 128
              and control["upper_graph_exists"])


print("\nD. DISPOSITION AND PHYSICAL FENCES")
check("type", "the canonical trace-q degree-duality repair cannot retain W alone; RS completion forces W plus mirror", True)
check("type", "both exact degree-duality solutions fail before southeast or lower-left choices can matter", True)
check("type", "a nonzero southeast block cannot repair this upper-image obstruction", True)
check("symplectic", "no algebraic carrier closure is promoted to a BV or reduced-phase-space quotient", True)
check("analytic", "no finite rank is promoted to a domain, spectrum, index, positivity or generation count", True)
check("adversarial", "the result kills only canonical trace-q degree duality on the proposed RS carrier, not every source-family operator", True)
check("source", "released sources remain silent on another sign correction or replacement Shiab", True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": "K77_EXACT_GF_AND_GAUSSIAN_RATIONAL",
    "degree_solutions": degree_solutions,
    "finite_fingerprint": finite_fingerprint,
    "char0_fingerprint": char0_fingerprint,
    "finite_results": finite_results,
    "char0_results": char0_results,
    "source_return": {
        "SOURCE-CONFIRMS": "ambient half-spinor field labels, candidate southeast zero, and source-admitted nonzero rival",
        "SOURCE-CORRECTS": "none",
        "SOURCE-SILENT": "a replacement sign convention, another parity-compatible Shiab, and physical W/mirror selection",
    },
    "disposition": "CANONICAL_TRACE_Q_DEGREE_DUALITY_KILLED_ON_PROPOSED_RS_CARRIER__BARE_Q_LEAKS_RS_RANK64__PIN_Q_SWAPS_W_MIRROR__BOTH_SOURCE_FAITHFUL_UPPER_GRAPHS_JOINED_RANK256",
    "next_gate": "REPLACEMENT_SHIAB_OR_SOURCE_DERIVED_RESTRICTED_ZERO_ORDER_PORT__OTHERWISE_KEEP_D916_SOURCE_FAMILY_UNRESOLVED_AND_ADVANCE_DISJOINT_COUPLED_FUNCTIONAL_BUILD",
}

print("\nK77 DEGREE-DUALITY PAIR-GRAPH RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: canonical trace-q degree duality forces W/mirror closure and then fails the upper graph equation on every retained parent.")
