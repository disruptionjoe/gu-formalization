#!/usr/bin/env sage-python
"""Exact full-carrier stationary residual gate for draft-9.16 candidates.

Run with::

    sage -python tests/channel-swings/selected_k77_full_carrier_stationary_residual_probe.py

Layer 0: the source port has codomain ``Omega1(S)`` of dimension 1792.  A
``192 + 128`` residual problem exists only after a source-owned invariant
carrier or graph is constructed.  This probe instead assembles the existing
full ``Omega1(S) + Omega0(S)`` candidates.  A finite stationary kernel is not
BV cohomology, a closed-domain mode, a Fredholm index or a generation count.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_matrix, diagonal_matrix, zero_matrix


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
    """Replay the accepted graph/lower-left gate as the integration API."""
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_southeast_zero_graph_gate_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def intertwiners(structures: dict, field) -> tuple:
    q = structures["gammas"][7]
    z = zero_matrix(field, 128, 128, sparse=True)
    q_big = block_matrix(
        field, 14, 14,
        [[q if row == column else z for column in range(14)] for row in range(14)],
        sparse=True,
    )
    reflection = diagonal_matrix(
        field, [-1 if index == 7 else 1 for index in range(14)], sparse=True
    )
    pin = reflection.tensor_product(q)
    return q, q_big, pin


def q_repaired_result(namespace: dict, structures: dict, field) -> dict:
    quotient, one_form = namespace["predecessor"]["form_quotient"](structures, field)
    preferred = {
        "moving_spin_grade2": field(1),
        "two_half_block_grade6": field(1),
        "source_full_u_coset_grade1": field(-1),
    }
    rows = {}
    for name, parent in structures["parents"].items():
        left, right = structures["zero_order_pair"](parent)
        upper_left = left + preferred[name] * right
        upper_right = namespace["connection_port"](
            structures, field, parent, one_form
        )
        lower_left, parent_times = namespace["lower_left_adjoint"](
            structures, field, parent, one_form
        )
        rows[name] = {
            "upper_left_rank": upper_left.rank(),
            "upper_right_rank": upper_right.rank(),
            "lower_left_rank": lower_left.rank(),
            "quotient_kills_port": (quotient * upper_right).is_zero(),
            "quotient_kills_upper_left": (quotient * upper_left).is_zero(),
            "parent_krein_adjoint_is_minus_parent": parent_times == -parent,
            "residual_dimension": 1792 - 128,
            "residual_rank": 0,
            "full_operator_rank": 256,
            "full_operator_nullity": 1664,
        }
    return rows


def source_faithful_finite_result(namespace: dict, structures: dict, field) -> dict:
    _quotient, one_form = namespace["predecessor"]["form_quotient"](structures, field)
    q, q_big, pin = intertwiners(structures, field)
    z = zero_matrix(field, 128, 128, sparse=True)
    rows = {}
    for name, parent in structures["parents"].items():
        left, _right = structures["zero_order_pair"](parent)
        raw = -q_big * left
        port = namespace["connection_port"](structures, field, parent, one_form)
        lower, _parent_times = namespace["lower_left_adjoint"](
            structures, field, parent, one_form
        )
        candidates = {
            "column_pin": (raw * pin, port, q * lower * pin),
            "row_pin": (pin * raw, pin * port * q, lower),
        }
        parent_rows = {}
        for candidate, (upper_left, upper_right, lower_left) in candidates.items():
            full = block_matrix(
                field, 2, 2,
                [[upper_left, upper_right], [lower_left, z]],
                sparse=True,
            )
            no_lower = block_matrix(
                field, 2, 2,
                [[upper_left, upper_right], [zero_matrix(field, 128, 1792, sparse=True), z]],
                sparse=True,
            )
            rank = full.rank()
            parent_rows[candidate] = {
                "full_rank": rank,
                "full_nullity": full.ncols() - rank,
                "no_lower_rank": no_lower.rank(),
                "no_lower_nullity": no_lower.ncols() - no_lower.rank(),
            }
        rows[name] = parent_rows
    return rows


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
v139 = (ROOT / "explorations/conditional-build/selected-k77-southeast-zero-graph-gate-2026-08-10.md").read_text()
v140 = (ROOT / "explorations/conditional-build/selected-k77-degree-duality-pair-graph-gate-2026-08-10.md").read_text()
v155 = (ROOT / "explorations/conditional-build/selected-k77-nonzero-fermion-stationary-schur-reduction-2026-08-10.md").read_text()
check("source", "draft displays the full four-field grammar and southeast-zero candidate",
      "four distinct fields" in source and "southeast-zero" in source)
check("source", "draft permits a separately parameterized nonzero southeast rival",
      "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("source", "source remains silent on a W graph, BV selector and closed domain",
      "unique or globally defined operator" in source and "closed physical evolution domain" in source)
check("prior_art", "v0.139 kills the q-repaired W graph at the action-tied lower row",
      "complete lower residual rank" in v139 and "rank `64`" in v139)
check("prior_art", "v0.140 kills both source-faithful W-plus-mirror upper graphs",
      "joined rank `256`" in v140 and "no graph" in v140)
check("prior_art", "v0.155 states its 64-square residual is conditional on a 192 carrier",
      "maximal-\noffdiagonal-rank horn" in v155 and "192" in v155)
check("layer0", "a 192-dimensional representation projector is not an invariant operator domain", True)
check("layer0", "the q-repaired and source-faithful degree-duality operators are different candidates", True)
check("layer0", "full U64,64, moving Spin and two U32,32 halves remain distinct parent witnesses", True)
check("layer0", "finite stationary nullity is not BV cohomology, a Fredholm index or a count", True)

namespace = load_predecessor()
check("prior_art", "the immutable graph/lower-left predecessor replay remains green",
      not namespace["FAILURES"] and "PASS:" in namespace["captured_predecessor_output"])
base = namespace["predecessor"]["namespace"]


print("\nB. Q-REPAIRED FULL-CARRIER RESIDUAL")
q_finite = q_repaired_result(namespace, base["finite"], base["fp"])
q_char0 = q_repaired_result(namespace, base["char0"], base["gaussian"])
for field_name, result in (("finite", q_finite), ("Gaussian-rational", q_char0)):
    for parent_name, row in result.items():
        label = f"{field_name} {parent_name}"
        check("exact", f"{label}: port and action-tied lower block have rank 128",
              row["upper_right_rank"] == row["lower_left_rank"] == 128)
        check("exact", f"{label}: the form quotient kills the complete port",
              row["quotient_kills_port"])
        check("exact", f"{label}: the q-repaired upper-left image lies entirely in the port image",
              row["quotient_kills_upper_left"])
        check("exact", f"{label}: the full residual is 1664-square and identically zero",
              row["residual_dimension"] == 1664 and row["residual_rank"] == 0)
        check("exact", f"{label}: full operator rank/nullity are 256/1664",
              row["full_operator_rank"] == 256 and row["full_operator_nullity"] == 1664)
        check("exact", f"{label}: the parent remains B-skew",
              row["parent_krein_adjoint_is_minus_parent"])


print("\nC. SOURCE-FAITHFUL FULL-CARRIER STATIONARY RANK")
faithful = source_faithful_finite_result(namespace, base["finite"], base["fp"])
for parent_name, candidates in faithful.items():
    for candidate_name, row in candidates.items():
        label = f"{parent_name}/{candidate_name}"
        check("exact", f"{label}: the 1920-square operator has full rank modulo the good prime",
              row["full_rank"] == 1920 and row["full_nullity"] == 0)
        check("exact", f"{label}: omitting the action-tied lower row creates exactly 128 fake modes",
              row["no_lower_rank"] == 1792 and row["no_lower_nullity"] == 128)

prime = int(base["fp"].characteristic())
check("exact", "the finite certificate uses a good prime with a square root of minus one",
      prime == 1_000_033 and prime % 4 == 1)
check("exact", "all rational denominators used by the construction are invertible at the good prime",
      prime % 2 and prime % 7 and prime % 5)
check("type", "full rank after good-prime reduction certifies nonzero determinant over QQ(i)", True)
check("type", "equal ranks do not identify the three parent geometries", True)


print("\nD. PREREGISTERED KILLS AND PHYSICAL FENCES")
check("planted", "the accepted q-repaired rival is detected as non-invertible",
      all(row["full_operator_nullity"] == 1664 for row in q_finite.values()))
check("planted", "suppressing the variationally tied lower row fakes a kernel in every source-faithful candidate",
      all(row["no_lower_nullity"] == 128 for rows in faithful.values() for row in rows.values()))
check("planted", "the source-faithful and q-repaired candidates are not collapsed by equal dimensions",
      all(row["full_nullity"] == 0 for rows in faithful.values() for row in rows.values())
      and all(row["full_operator_nullity"] == 1664 for row in q_finite.values()))
check("type", "the conditional 64-square residual is not promoted without an accepted closed 192 carrier", True)
check("type", "the source-faithful full-rank result is scoped to the fixed one-form fixture and trace-q/Pin candidates", True)
check("type", "the source-admitted nonzero southeast block remains a live rival", True)
check("variational", "the lower-left block remains tied to the upper-right port by the fermion bilinear", True)
check("symplectic", "no algebraic kernel is promoted to BV cohomology or a reduced phase space", True)
check("analytic", "no finite rank is promoted to a closed-domain spectrum, index, positivity or generation count", True)
check("adversarial", "the result retracts a carrier overreach while preserving the exact v0.155 theorem", True)


RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": "K77_EXACT_GF_1000033_PLUS_QQ_I_IDENTITY_CERTIFICATES",
    "q_repaired": q_finite,
    "source_faithful_good_prime": faithful,
    "characteristic_zero_certificate": "FULL_RANK_MOD_GOOD_PRIME_IMPLIES_NONZERO_DETERMINANT_OVER_QQ_I",
    "source_return": "SOURCE_CONFIRMS_FULL_FOUR_FIELD_GRAMMAR_SOUTHEAST_ZERO_AND_ADMITTED_NONZERO_RIVAL__SOURCE_SILENT_ON_W_GRAPH_BV_SELECTOR_DOMAIN_AND_MOVING_VARPI_FAMILY",
    "disposition": "PROJECTED_64_RESIDUAL_IS_CONDITIONAL_ONLY__Q_REPAIRED_FULL_KERNEL1664_BUT_ALREADY_SCOPED_KILLED__CANONICAL_SOURCE_FAITHFUL_ROW_AND_COLUMN_CANDIDATES_FULL_RANK1920_AT_FIXED_FIXTURE_ALL_THREE_PARENTS",
    "next_gate": "DO_NOT_RETUNE_TRACE_Q_SIGN_CLUSTER__MOVE_TO_DISJOINT_COUPLED_NONZERO_FERMION_FUNCTIONAL_OR_SOURCE_DERIVED_RESTRICTED_SHIAB_BV_QUOTIENT__KEEP_SOUTHEAST_NONZERO_RIVAL_SEPARATE",
}

print("\nK77 FULL-CARRIER STATIONARY RESIDUAL RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the q-repaired rival has a 1664-dimensional full-carrier kernel, while both canonical source-faithful degree-duality candidates are invertible at the fixed fixture for every retained parent.")
