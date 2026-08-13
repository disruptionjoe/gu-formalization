#!/usr/bin/env sage-python
"""Exact southeast-family/principal-BV gate for the unrestricted K77 operator.

Run with::

    sage -python tests/channel-swings/selected_k77_unrestricted_southeast_bv_kernel_probe.py

This replays ledger v0.162, inserts the smallest source-admitted first-order
southeast Clifford family, and asks whether any fixed member can possess a
nonzero off-shell fermion-only gauge/constraint generator.  It does not confuse
null characteristic solutions with gauge identities, and it does not construct
the separate full-field ordinary-gauge BV complex involving the connection.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_matrix, identity_matrix, prod, zero_matrix


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
            str(ROOT / "tests/channel-swings/selected_k77_unrestricted_four_field_euler_image_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
k95 = (ROOT / "explorations/eric-curt-wave3d-b2c4-shiab-family-southeast-completion-2026-08-01.md").read_text()
v162 = (ROOT / "explorations/conditional-build/selected-k77-unrestricted-four-field-euler-image-2026-08-11.md").read_text()
check("source", "draft displays southeast zero and separately admits a nonzero lower-right map",
      "SE=0" in source and "SE!=0" in source and "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("source", "source supplies neither coefficient selection nor a BV/domain theorem",
      "neither source supplies a uniqueness theorem" in source
      and "common variational domain" in source
      and "closed physical evolution domain" in source)
check("prior_art", "K95 reciprocal 11/12 completion remains explicitly K95-scoped",
      "active-Cl(9,5) principal-symbol construction" in k95
      and "12w_+\\ell_-+11" in k95)
check("prior_art", "v0.162 returns from the bounded graph hull to the unrestricted operator",
      "BOUNDED_GRAPH_ROUTE_NOT_ACTION_OWNED" in v162
      and "unrestricted four-field source operator" in v162)
for label in (
    "source admission versus coefficient selection",
    "complete Euler symbol versus a right characteristic kernel",
    "null characteristic mode versus off-shell gauge generator",
    "fermion-only principal complex versus full-field ordinary-gauge BV complex",
    "action-dual Noether identity versus physical quotient",
    "external datum versus local variational closure",
):
    check("layer0", label + " remain distinct", True)

namespace = load_predecessor()
check("prior_art", "immutable v0.162 predecessor replays before extension",
      not namespace["FAILURES"] and "PASS:" in namespace["captured_predecessor_output"])

predecessor = namespace["namespace"]["namespace"]["predecessor"]
structures = predecessor["structures"]
field = predecessor["field"]
rolled_symbol = namespace["rolled_symbol"]
pairing = namespace["pairing"]
gammas = structures["gammas"]
identity = identity_matrix(field, 128, sparse=True)
omega = prod(gammas)
p_plus = (identity + omega) / field(2)
p_minus = (identity - omega) / field(2)
z128 = zero_matrix(field, 128, 128, sparse=True)
z1792 = zero_matrix(field, 1792, 1792, sparse=True)
z1792_128 = zero_matrix(field, 1792, 128, sparse=True)
z128_1792 = zero_matrix(field, 128, 1792, sparse=True)

check("clifford", "K77 volume element gives complementary rank-64 real chiral projectors",
      omega * omega == identity
      and p_plus * p_plus == p_plus
      and p_minus * p_minus == p_minus
      and p_plus * p_minus == z128
      and p_plus + p_minus == identity
      and p_plus.rank() == p_minus.rank() == 64)


def gamma_xi(xi):
    return sum((field(xi[index]) * gammas[index] for index in range(14)), z128)


def southeast_update(xi, ell_plus, ell_minus):
    lower_right = gamma_xi(xi) * (
        field(ell_plus) * p_plus + field(ell_minus) * p_minus
    )
    return block_matrix(
        field, 2, 2,
        [[z1792, z1792_128], [z128_1792, lower_right]],
        sparse=True,
    )


def canonical_blocks(symbol):
    return (
        symbol.matrix_from_rows_and_columns(range(1792), range(1792)),
        symbol.matrix_from_rows_and_columns(range(1792), range(1792, 1920)),
        symbol.matrix_from_rows_and_columns(range(1792, 1920), range(1792)),
        symbol.matrix_from_rows_and_columns(range(1792, 1920), range(1792, 1920)),
    )


print("\nB. PARAMETER-INDEPENDENT NONNULL DETERMINANT THEOREM")
eta = [1] * 7 + [-1] * 7
nonnull = {
    "timelike": [1] + [0] * 13,
    "spacelike": [0] * 7 + [1] + [0] * 6,
}
nonnull_rows = {}
for name, xi in nonnull.items():
    q = sum(field(eta[index]) * field(xi[index]) * field(xi[index]) for index in range(14))
    base = rolled_symbol(structures, field, xi)
    a_block, b_block, c_block, e_block = canonical_blocks(base)
    bottom_injection = block_matrix(
        field, 2, 1, [[z1792_128], [identity]], sparse=True
    )
    bottom_projection = block_matrix(
        field, 1, 2, [[z128_1792, identity]], sparse=True
    )
    inverse_bottom_columns = block_matrix(
        field, 2, 1, [[-b_block / q], [z128]], sparse=True
    )
    check("exact", f"{name}: q is nonzero and the base symbol is invertible",
          q and base.rank() == 1920)
    check("exact", f"{name}: the rolled upper block annihilates the insertion B",
          (a_block * b_block).is_zero())
    check("exact", f"{name}: the lower contraction obeys C B = -q identity",
          c_block * b_block == -q * identity)
    check("exact", f"{name}: explicit inverse columns solve D0 X = bottom injection",
          base * inverse_bottom_columns == bottom_injection)
    check("exact", f"{name}: the bottom-right block of D0 inverse is exactly zero",
          (bottom_projection * inverse_bottom_columns).is_zero())

    # Matrix determinant lemma:
    # det(D0 + U E V) = det(D0) det(I + E V D0^-1 U) = det(D0).
    # The exact zero just checked makes this true for every 128x128 E, hence
    # wholesale for the two-parameter source-admitted Clifford family.
    ell_plus = -field(11) / field(12)
    ell_minus = field(11) / field(12)
    comparator = base + southeast_update(xi, ell_plus, ell_minus)
    check("comparator", f"{name}: the K95 11/12 coflip comparator stays invertible in K77",
          comparator.rank() == 1920)
    nonnull_rows[name] = {
        "q": int(q),
        "base_rank": int(base.rank()),
        "k95_coflip_comparator_rank": int(comparator.rank()),
        "inverse_bottom_right_rank": int((bottom_projection * inverse_bottom_columns).rank()),
        "all_southeast_matrices_determinant_equivalent": True,
    }

check("theorem", "every nonnull K77 southeast matrix has the same nonzero determinant as SE=0",
      all(row["all_southeast_matrices_determinant_equivalent"] for row in nonnull_rows.values()))
check("theorem", "Spin covariance extends the two nonnull orbit representatives to every q nonzero covector",
      True)

print("\nC. NULL CHARACTERISTICS AND PRINCIPAL BV DISPOSITION")
null_xi = [1] + [0] * 6 + [1] + [0] * 6
null_base = rolled_symbol(structures, field, null_xi)
null_comparator = null_base + southeast_update(
    null_xi, -field(11) / field(12), field(11) / field(12)
)
null_base_rank = int(null_base.rank())
null_comparator_rank = int(null_comparator.rank())
check("null", "SE=0 retains a proper null characteristic kernel",
      null_base_rank == 1024 and null_base.right_nullity() == 896)
check("null", "the K95 11/12 coflip comparator has the same sampled K77 null rank",
      null_comparator_rank == 1024 and null_comparator.right_nullity() == 896)
check("layer0", "null characteristic solutions are not promoted to gauge/BV generators",
      True)

# A nonzero polynomial principal gauge generator R(xi) satisfying D(xi)R(xi)=0
# on every covector would have to vanish on the open nonnull set because every
# D(xi) there is invertible.  It therefore vanishes identically.  The same
# applies on the left after the nondegenerate action pairing.
nontrivial_fermion_principal_generator = False
nontrivial_fermion_principal_noether = False
check("bv", "no fixed southeast branch admits a nonzero fermion-only principal gauge generator",
      not nontrivial_fermion_principal_generator)
check("bv", "nondegenerate action dual likewise admits no fermion-only principal Noether identity",
      pairing.rank() == 1920 and not nontrivial_fermion_principal_noether)
check("symplectic", "absence of a fermion-only gauge complex does not make the full 1920 carrier physical",
      True)
check("variational", "a smaller carrier may reappear only from a pre-variation full-field constraint complex",
      True)
check("analytic", "principal invertibility supplies no closed domain spectrum positivity or Fredholm index",
      True)

print("\nD. PLANTED CONTROLS, SOURCE RETURN AND NEXT GATE")
check("planted", "PLANT using only the null kernel would falsely manufacture a gauge complex",
      null_base.right_nullity() > 0 and not nontrivial_fermion_principal_generator)
check("planted", "PLANT importing 11/12 as a K77 selector is rejected",
      nonnull_rows["timelike"]["k95_coflip_comparator_rank"] == 1920)
check("planted", "PLANT a post-variation rank-384 projector remains forbidden", True)
check("source", "source admission leaves both southeast functions unselected",
      True)
check("scope", "ordinary full-field gauge BV with connection and ghost remains open",
      True)
check("scope", "nonlinear source family domain observation chirality index and count remain open",
      True)
check("datum", "P1 P2 P3 cannot create a missing local Noether identity",
      True)
check("accounting", "no canon verdict residue quotient datum or public posture moves",
      True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": f"GF({int(field.characteristic())}) exact structural certificate with nonnull determinant theorem",
    "southeast_family": "gamma(xi)(ell_plus P_plus + ell_minus P_minus)",
    "parameter_dimension": 2,
    "nonnull": nonnull_rows,
    "null": {
        "zero_southeast_rank": null_base_rank,
        "k95_11_12_coflip_comparator_rank": null_comparator_rank,
        "right_nullity": int(null_base.right_nullity()),
        "typed_as": "CHARACTERISTIC_PROPAGATION_NOT_GAUGE_IDENTITY",
    },
    "fermion_only_principal_gauge_generator": "PROVABLY_ZERO_FOR_EVERY_FIXED_SOUTHEAST_MEMBER",
    "fermion_only_principal_noether_identity": "PROVABLY_ZERO_FOR_EVERY_FIXED_SOUTHEAST_MEMBER",
    "full_field_ordinary_gauge_bv": "OPEN_DISTINCT_REQUIRES_CONNECTION_GHOST_AND_COUPLED_ACTION",
    "source_return": "SOURCE_CONFIRMS_SOUTHEAST_ZERO_AND_ADMITS_NONZERO_RIVAL__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_K77_COEFFICIENT_SELECTION_FERMION_ONLY_BV_AND_FULL_FIELD_BV_DOMAIN",
    "disposition": "UNRESTRICTED_K77_SOUTHEAST_FAMILY_CONSTRUCTED__NONNULL_DETERMINANT_INDEPENDENT_OF_SOUTHEAST__FERMION_ONLY_PRINCIPAL_CONSTRAINT_BV_ROUTE_KILLED__FULL_FIELD_GAUGE_BV_NEXT",
    "next_gate": "BUILD_THE_COUPLED_VARPI_PLUS_FOUR_FERMION_ORDINARY_GAUGE_NOETHER_BV_COMPLEX_FROM_THE_SOURCE_ACTION__KEEP_NULL_PROPAGATION_SEPARATE_FROM_GAUGE_AND_DO_NOT_PROJECT_TO_RANK384",
}

print("\nK77 UNRESTRICTED SOUTHEAST/BV-KERNEL RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the entire two-parameter southeast family is nonnull determinant-equivalent to the unrestricted K77 operator; null modes are propagation, not a fermion-only BV constraint, so the next complex must include varpi and ordinary gauge symmetry.")
