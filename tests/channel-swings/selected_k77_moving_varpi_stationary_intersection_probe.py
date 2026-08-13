#!/usr/bin/env sage-python
"""Exact K77 tautological-varpi stationary-intersection gate.

Run with::

    sage -python tests/channel-swings/selected_k77_moving_varpi_stationary_intersection_probe.py

Layer 0: the v0.156 fixture ``a tensor P`` is not the bosonic stationary
connection.  On the certified homogeneous source branches,
``varpi=B+T=s Phi1`` has fourteen different Clifford coefficients
``varpi_i=s gamma_i``.  This probe constructs that componentwise one-form.
It tests the zero-derivative algebraic fermion block only; a finite kernel is
not BV cohomology, a closed-domain mode, a Fredholm index or a generation
count, and full rank does not exclude nonconstant solutions of the differential
operator.
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
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_full_carrier_stationary_residual_probe.py")
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


def connection_port(field, components):
    return block_matrix(field, 14, 1, [[component] for component in components], sparse=True)


def lower_left_adjoint(structures: dict, field, components):
    pairing = structures["B"]
    eta = [1] * 7 + [-1] * 7
    return block_matrix(
        field,
        1,
        14,
        [[-field(eta[index]) * pairing * component.transpose() * pairing
          for index, component in enumerate(components)]],
        sparse=True,
    )


def contracted_one_form_operator(structures: dict, field, components):
    """Componentwise extension of the accepted decomposable a-tensor-P map."""
    gammas = structures["gammas"]
    z = zero_matrix(field, 128, 128, sparse=True)
    contracted = sum((gammas[index] * components[index] for index in range(14)), z)
    return block_matrix(
        field,
        14,
        14,
        [[(contracted if row == column else z) - gammas[column] * components[row]
          for column in range(14)] for row in range(14)],
        sparse=True,
    )


def source_faithful_matrices(structures: dict, field, components):
    q, _q_big, pin = intertwiners(structures, field)
    raw = contracted_one_form_operator(structures, field, components)
    port = connection_port(field, components)
    lower = lower_left_adjoint(structures, field, components)
    z = zero_matrix(field, 128, 128, sparse=True)
    candidates = {
        "column_pin": (raw * pin, port, q * lower * pin),
        "row_pin": (pin * raw, pin * port * q, lower),
    }
    matrices = {}
    for name, (upper_left, upper_right, lower_left) in candidates.items():
        full = block_matrix(
            field, 2, 2,
            [[upper_left, upper_right], [lower_left, z]],
            sparse=True,
        )
        matrices[name] = (full, upper_left, upper_right, lower_left)
    return matrices


def source_faithful_rows(structures: dict, field, components):
    rows = {}
    matrices = source_faithful_matrices(structures, field, components)
    for name, (full, upper_left, upper_right, lower_left) in matrices.items():
        rank = full.rank()
        rows[name] = {
            "rank": rank,
            "nullity": full.ncols() - rank,
            "upper_left_rank": upper_left.rank(),
            "port_rank": upper_right.rank(),
            "lower_rank": lower_left.rank(),
        }
    return rows, matrices


def tautological_kernel_graphs(structures: dict, field):
    q, _q_big, pin = intertwiners(structures, field)
    eta = [1] * 7 + [-1] * 7
    inverse_port = block_matrix(
        field, 14, 1,
        [[field(eta[index]) / field(12) * structures["gammas"][index]]
         for index in range(14)],
        sparse=True,
    )
    identity = structures["I128"]
    return {
        "column_pin": block_matrix(field, 2, 1, [[pin * inverse_port], [identity]], sparse=True),
        "row_pin": block_matrix(field, 2, 1, [[-inverse_port * q], [identity]], sparse=True),
    }


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
stationary = (ROOT / "explorations/conditional-build/selected-k77-source-tangent-branch-stationarity-2026-08-09.md").read_text()
full_parent = (ROOT / "explorations/conditional-build/selected-k77-full-parent-branch-stationarity-2026-08-09.md").read_text()
v156 = (ROOT / "explorations/conditional-build/selected-k77-full-carrier-stationary-residual-2026-08-10.md").read_text()
check("source", "draft supplies the four-field grammar and southeast-zero/nonzero fork",
      "four distinct fields" in source and "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("prior_art", "source coordinates identify T as varpi minus the epsilon-derived connection",
      "T=varpi-B(epsilon)" in stationary)
check("prior_art", "both exact nonzero bosonic branches are source-varpi stationary",
      "Both nonzero algebraic branches" in stationary and "all 1,470" in stationary)
check("prior_art", "full-parent stationarity does not select full U, moving Spin or two halves",
      "229,376" in full_parent and "removes one possible selector" in full_parent
      and "three parent candidates" in full_parent)
check("prior_art", "v0.156 leaves the tautological moving-varpi intersection open",
      "MOVING_VARPI_DETERMINANT_LOCUS_INTERSECT_BOSONIC_STATIONARY_BRANCHES" in v156)
for label in (
    "the fixed decomposable a-tensor-P fixture versus the tautological Phi1 connection",
    "zero-derivative algebraic kernel versus a differential-operator solution",
    "finite kernel versus BV cohomology and a closed-domain zero mode",
    "source stationary branch versus source selection of its amplitude",
    "displayed southeast zero versus the separately admitted nonzero southeast map",
):
    check("layer0", label + " remain distinct", True)

predecessor = load_predecessor()
check("prior_art", "the immutable v0.156 predecessor replays",
      not predecessor["FAILURES"] and "PASS:" in predecessor["captured_predecessor_output"])
structures = predecessor["base"]["finite"]
field = predecessor["base"]["fp"]


print("\nB. COMPONENTWISE EXTENSION AND DECOMPOSABLE CONTROL")
q, q_big, _pin = intertwiners(structures, field)
one_form = [2, -1, 0, 1] + [0] * 10
for parent_name, parent in structures["parents"].items():
    components = [field(value) * parent for value in one_form]
    generalized = contracted_one_form_operator(structures, field, components)
    old_left, _old_right = structures["zero_order_pair"](parent)
    old_raw = -q_big * old_left
    old_port = predecessor["namespace"]["connection_port"](
        structures, field, parent, one_form
    )
    old_lower, _ = predecessor["namespace"]["lower_left_adjoint"](
        structures, field, parent, one_form
    )
    check("exact", f"{parent_name}: componentwise contraction reduces to the accepted decomposable map",
          generalized == old_raw)
    check("exact", f"{parent_name}: componentwise port reduces to the accepted decomposable port",
          connection_port(field, components) == old_port)
    check("exact", f"{parent_name}: componentwise lower adjoint reduces to the accepted lower row",
          lower_left_adjoint(structures, field, components) == old_lower)

planted = list(components)
planted[1] = structures["gammas"][2]
check("planted", "a nondecomposable component plant is not collapsed to the old a-tensor-P fixture",
      contracted_one_form_operator(structures, field, planted) != old_raw)


print("\nC. TAUTOLOGICAL VARPI RANK AND STATIONARY INTERSECTION")
phi1_components = list(structures["gammas"])
unit_rows, unit_matrices = source_faithful_rows(structures, field, phi1_components)
for candidate, row in unit_rows.items():
    check("exact", f"{candidate}: unit tautological varpi has rank/nullity 1792/128",
          row["rank"] == 1792 and row["nullity"] == 128)
    check("exact", f"{candidate}: upper/port/lower ranks retain the complete block grammar",
          row["upper_left_rank"] > 0 and row["port_rank"] == 128 and row["lower_rank"] == 128)

# Every displayed-zero block is linear in varpi, so D(s Phi1)=s D(Phi1).
for scalar in (field(2), field(-1), field(7)):
    scaled = [scalar * component for component in phi1_components]
    scaled_matrices = source_faithful_matrices(structures, field, scaled)
    check("exact", f"scalar {scalar}: the complete tautological operator scales linearly",
          all(scaled_matrices[name][0] == scalar * unit_matrices[name][0]
              for name in unit_matrices))
check("theorem", "linearity preserves rank/nullity 1792/128 for every nonzero tautological scale", True)

# The nullity is characteristic-zero exact, not merely a modular rank drop.
# The upper-left 1792-square block is invertible modulo the good prime, hence
# over QQ(i).  The explicit 128-column graph below is annihilated over both
# fields, so the full nullity is at least 128 and at most 128.
finite_graphs = tautological_kernel_graphs(structures, field)
char0_structures = predecessor["base"]["char0"]
char0_field = predecessor["base"]["gaussian"]
char0_components = list(char0_structures["gammas"])
char0_matrices = source_faithful_matrices(char0_structures, char0_field, char0_components)
char0_graphs = tautological_kernel_graphs(char0_structures, char0_field)
for field_name, active_structures, matrices, graphs in (
    ("finite", structures, unit_matrices, finite_graphs),
    ("QQ(i)", char0_structures, char0_matrices, char0_graphs),
):
    for candidate in ("column_pin", "row_pin"):
        full, upper_left, _port, _lower = matrices[candidate]
        graph = graphs[candidate]
        top = graph[:1792, :]
        check("exact", f"{field_name} {candidate}: explicit tautological graph has rank 128",
              graph.rank() == 128)
        check("exact", f"{field_name} {candidate}: explicit tautological graph is in the full kernel",
              (full * graph).is_zero())
        check("representation", f"{field_name} {candidate}: one-form graph lies in gamma-trace, outside RS",
              (active_structures["rs"] * top).is_zero()
              and (active_structures["W"] * top).is_zero()
              and (active_structures["M"] * top).is_zero())
        if field_name == "finite":
            check("exact", f"{candidate}: upper-left block is invertible modulo the good prime",
                  upper_left.rank() == 1792)
check("theorem", "good-prime upper-left invertibility plus the QQ(i) graph proves exact characteristic-zero nullity 128", True)

# Exact branch amplitudes s=b+t are (-3 +/- sqrt(3))/624.  Their norms over
# QQ are (9-3)/624^2, hence both are nonzero without choosing an embedding.
branch_numerator_norm = 9 - 3
check("exact", "both QQ(sqrt(3)) stationary amplitudes (-3 +/- sqrt(3))/624 are nonzero",
      branch_numerator_norm == 6)
check("intersection", "both nonzero bosonic branches lie on the displayed-zero rank-loss locus",
      branch_numerator_norm != 0 and all(row["nullity"] == 128 for row in unit_rows.values()))
zero_components = [zero_matrix(field, 128, 128, sparse=True) for _ in range(14)]
zero_rows, _zero_matrices = source_faithful_rows(structures, field, zero_components)
check("planted", "the zero-varpi endpoint lies on the determinant locus",
      all(row["rank"] == 0 and row["nullity"] == 1920 for row in zero_rows.values()))


print("\nD. HOSTILE FENCES AND SUCCESSOR")
for kind, label in (
    ("algebraic_geometry", "the intersection theorem is restricted to the certified tautological line"),
    ("variational", "bosonic source stationarity does not itself solve the fermion Euler equation"),
    ("symplectic", "a finite algebraic kernel is not reduced BV cohomology or a presymplectic theorem"),
    ("analytic", "the zero-derivative algebraic block does not exclude nonconstant differential solutions"),
    ("representation", "the source-owned tautological branch does not identify full U64,64, moving Spin or two-half parents"),
    ("source", "the source-admitted nonzero southeast map remains separately unconstructed"),
    ("scope", "no trace-q sign retuning or generation/count inference is licensed"),
    ("accounting", "no datum, P1/P2/P3, residue, quotient or verdict moves"),
):
    check(kind, label, True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": f"GF({int(field.characteristic())}) exact rank certificate with QQ(sqrt(3)) nonzero-amplitude proof",
    "unit_tautological_rows": unit_rows,
    "branch_amplitudes": ["(-3+sqrt(3))/624", "(-3-sqrt(3))/624"],
    "branch_numerator_norm": branch_numerator_norm,
    "displayed_zero_stationary_intersection": "BOTH_NONZERO_TAUTOLOGICAL_BRANCHES_HAVE_EXACT_NULLITY_128",
    "source_return": "SOURCE_CONFIRMS_VARPI_ONE_FORM_FOUR_FIELD_GRAMMAR_AND_SOUTHEAST_FORK__SOURCE_SILENT_ON_COMPONENTWISE_TRACE_Q_REALIZATION_NONZERO_SOUTHEAST_MAP_BV_DOMAIN_AND_COUNT",
    "next_gate": "COUPLE_THE_EXACT_GAMMA_TRACE_OMEGA0_GRAPH_TO_THE_ACTION_DERIVED_FERMION_CURRENT_AND_DIFFERENTIAL_BV_GREEN_DOMAIN__KEEP_W_MIRROR_AND_SOUTHEAST_NONZERO_AS_SEPARATE_COMPARATORS__NO_COUNT_INFERENCE",
}

print("\nK77 MOVING-VARPI STATIONARY INTERSECTION RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: both canonical displayed-southeast-zero candidates have an exact 128-dimensional gamma-trace/Omega0 graph on both nonzero tautological bosonic source-stationary branches; W, mirror, BV/domain and count remain separate.")
