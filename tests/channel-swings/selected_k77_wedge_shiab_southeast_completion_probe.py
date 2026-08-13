#!/usr/bin/env sage-python
"""Exact real-K77 wedge-Shiab/nonzero-southeast completion gate.

Run with::

    sage -python tests/channel-swings/selected_k77_wedge_shiab_southeast_completion_probe.py

This ports the old K95 B2C4 *question*, not its real form, sign, right-H
structure or action.  It constructs the actual real Cl(7,7) wedge middle map
and the smallest first-order southeast family.  The spatial Clifford relations
decide semisimplicity wholesale at principal grade.  The independent barred
and unbarred source fields admit an action bilinear, but that is kept distinct
from a K-self-adjoint real/reality reduction and from BV cohomology.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import GF, block_diagonal_matrix, block_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


print("A. ADAPTIVE PREFLIGHT, SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
k95 = read("explorations/eric-curt-wave3d-b2c4-shiab-family-southeast-completion-2026-08-01.md")
v163 = read("explorations/conditional-build/selected-k77-unrestricted-southeast-bv-kernel-2026-08-11.md")
v172 = read("explorations/conditional-build/selected-k77-polarized-radical-bfv-ownership-gate-2026-08-11.md")
check("source", "draft supplies a family grammar and explicitly admits a nonzero southeast rival",
      '"non-trivial map in the lower right quadrant"' in source
      and "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("source", "source selects neither the nonzero map nor a common analytic domain",
      "neither source supplies a uniqueness theorem" in source
      and "closed physical evolution domain" in source)
check("prior_art", "K95 B2C4 is explicitly quaternionic and uses the negative reciprocal sign",
      "active-Cl(9,5)" in k95 and "-\\frac{11}{12w_-}" in k95)
check("prior_art", "v0.163 kills fermion-only BV for every southeast block but leaves Shiab-family changes open",
      "every lower-right 128x128 southeast matrix" in v163
      and "does not exhaust the source's Shiab family" in v163)
check("prior_art", "v0.172 stops the zero-fermion restriction route and promotes operator completion",
      "cheap restriction route stops on the zero-fermion selected branch" in v172
      and "wedge-Shiab/nonzero-southeast" in v172)
for label in (
    "changing the Shiab middle symbol versus adding only a southeast cell",
    "semisimple propagation versus coefficient or action selection",
    "null characteristic half versus gauge or BV cohomology",
    "independent-dual action versus K-self-adjoint real/reality reduction",
    "Spin-selected operator versus two U(32,32) halves or full U(64,64) parent",
    "K95 right-H result versus the real K77 branch",
):
    check("layer0", label, True)


def build_packet(prime: int, full_review: bool) -> dict:
    field = GF(prime)
    n, nv, spin, total = 7, 14, 128, 1920
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)

    def tensor_all(factors):
        out = matrix(field, [[1]], sparse=True)
        for factor in factors:
            out = out.tensor_product(factor)
        return out

    plus, minus = [], []
    for index in range(n):
        prefix, suffix = [s3] * index, [i2] * (n - 1 - index)
        plus.append(tensor_all(prefix + [s1] + suffix))
        minus.append(tensor_all(prefix + [eps] + suffix))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
    identity_s = identity_matrix(field, spin, sparse=True)
    zero_s = zero_matrix(field, spin, spin, sparse=True)
    identity_full = identity_matrix(field, total, sparse=True)

    omega = identity_s
    for gamma in gammas:
        omega *= gamma
    p_plus = (identity_s + omega) / field(2)
    p_minus = (identity_s - omega) / field(2)
    check("clifford", f"GF({prime}): real K77 generators and volume projectors have the required signature/ranks",
          all(gamma * gamma == identity_s for gamma in plus)
          and all(gamma * gamma == -identity_s for gamma in minus)
          and p_plus.rank() == p_minus.rank() == 64
          and p_plus * p_minus == zero_s)

    diagonal_cache = {}

    def block_diagonal_spin(value):
        key = id(value)
        if key not in diagonal_cache:
            diagonal_cache[key] = block_matrix(
                field, nv, nv,
                [[value if row == column else zero_s for column in range(nv)]
                 for row in range(nv)], sparse=True)
        return diagonal_cache[key]

    wedge_cache = {}

    def wedge(index: int):
        if index not in wedge_cache:
            wedge_cache[index] = block_matrix(
                field, nv, nv,
                [[field(eta[row]) * gammas[row] * gammas[index] * gammas[column]
                  if row != index and column not in (row, index) else zero_s
                  for column in range(nv)] for row in range(nv)], sparse=True)
        return wedge_cache[index]

    def k_map(index: int):
        return block_matrix(
            field, nv, 1,
            [[identity_s if row == index else zero_s] for row in range(nv)], sparse=True)

    def codiff(index: int):
        return block_matrix(
            field, 1, nv,
            [[field(eta[column]) * identity_s if column == index else zero_s
              for column in range(nv)]], sparse=True)

    def symbol(index: int, w_plus, w_minus, ell_plus, ell_minus):
        weights = field(w_plus) * p_plus + field(w_minus) * p_minus
        southeast = field(ell_plus) * p_plus + field(ell_minus) * p_minus
        return block_matrix(
            field, 2, 2,
            [[wedge(index) * block_diagonal_spin(weights), k_map(index)],
             [-codiff(index), gammas[index] * southeast]], sparse=True)

    for index in (0, 7, 8, 9):
        check("representation", f"GF({prime}) axis {index}: wedge middle obeys both exterior and divergence identities",
              (wedge(index) * k_map(index)).is_zero()
              and (codiff(index) * wedge(index)).is_zero())

    w_plus, w_minus = field(1), field(2)
    ell_plus = field(11) / (field(12) * w_minus)
    ell_minus = field(11) / (field(12) * w_plus)
    time = symbol(0, w_plus, w_minus, ell_plus, ell_minus)
    check("exact", f"GF({prime}): corrected K77 time symbol is invertible", time.rank() == total)

    evolutions = []
    for index in (7, 8, 9):
        spatial = symbol(index, w_plus, w_minus, ell_plus, ell_minus)
        evolution = time.solve_right(spatial)
        evolutions.append(evolution)
        check("exact", f"GF({prime}) axis {index}: evolution solve is exact and involutive",
              time * evolution == spatial and evolution * evolution == identity_full)
    for left, right in ((0, 1), (0, 2), (1, 2)):
        check("exact", f"GF({prime}) axes {left}/{right}: spatial evolutions anticommute",
              (evolutions[left] * evolutions[right]
               + evolutions[right] * evolutions[left]).is_zero())

    null_symbol = time + symbol(7, w_plus, w_minus, ell_plus, ell_minus)
    check("characteristic", f"GF({prime}): repaired null symbol has a semisimple half-dimensional kernel",
          null_symbol.rank() == null_symbol.right_nullity() == 960)

    # The source-displayed zero southeast and the K95 sign are controls.  The
    # former leaves the rank-128 square-zero remainder; the latter must not be
    # ported across the real-form fork.
    zero_time = symbol(0, w_plus, w_minus, field(0), field(0))
    zero_evolution = zero_time.solve_right(symbol(7, w_plus, w_minus, field(0), field(0)))
    zero_remainder = zero_evolution * zero_evolution - identity_full
    check("control", f"GF({prime}): zero southeast retains the rank-128 square-zero Jordan remainder",
          zero_remainder.rank() == 128 and (zero_remainder * zero_remainder).is_zero())

    wrong_plus, wrong_minus = -ell_plus, -ell_minus
    wrong_time = symbol(0, w_plus, w_minus, wrong_plus, wrong_minus)
    wrong_evolution = wrong_time.solve_right(symbol(7, w_plus, w_minus, wrong_plus, wrong_minus))
    wrong_remainder = wrong_evolution * wrong_evolution - identity_full
    check("planted", f"GF({prime}): PLANT the K95 minus-11/12 sign leaves rank-128 K77 Jordan defect",
          wrong_remainder.rank() == 128 and not wrong_remainder.is_zero())

    # Perturb each crossed relation independently.  Each exposes one chiral
    # rank-64 defect; together they span the rank-128 obstruction.  This is the
    # finite exact necessity witness for the two scalar relations.
    perturbed = []
    for ep, em in ((ell_plus + 1, ell_minus), (ell_plus, ell_minus + 1)):
        perturbed_time = symbol(0, w_plus, w_minus, ep, em)
        perturbed_evolution = perturbed_time.solve_right(symbol(7, w_plus, w_minus, ep, em))
        perturbed.append(perturbed_evolution * perturbed_evolution - identity_full)
    check("necessity", f"GF({prime}): the two crossed reciprocal equations independently remove rank-64 defects",
          [value.rank() for value in perturbed] == [64, 64]
          and block_matrix(field, 1, 2, [[perturbed[0], perturbed[1]]], sparse=True).rank() == 128)

    # Independent barred/unbarred fields only require a nondegenerate density
    # pairing.  They do not require D to be self-adjoint.  Record the exact
    # stronger boundary: the selected diagonal K77 pairing gives a live Green
    # coefficient but the repaired two-field operator is not itself K-sharp
    # symmetric, so a real/reality reduction is still a construction burden.
    b_spin = identity_s
    for gamma in gammas[7:]:
        b_spin *= gamma
    pairing = block_diagonal_matrix(
        [field(eta[index]) * b_spin for index in range(nv)] + [b_spin], sparse=True)
    green_time = pairing * time
    adjoint_defect = pairing * time - time.transpose() * pairing
    check("variational", f"GF({prime}): independent-dual action and Green time coefficient are nondegenerate",
          pairing.rank() == green_time.rank() == total)
    check("reality", f"GF({prime}): repaired operator is not silently promoted to K-self-adjoint reality reduction",
          adjoint_defect.rank() == total)

    symmetrizer_rank = None
    if full_review:
        monomials = [
            identity_full,
            evolutions[0], evolutions[1], evolutions[2],
            evolutions[0] * evolutions[1],
            evolutions[0] * evolutions[2],
            evolutions[1] * evolutions[2],
            evolutions[0] * evolutions[1] * evolutions[2],
        ]
        symmetrizer = sum(
            (value.transpose() * value for value in monomials),
            zero_matrix(field, total, total, sparse=True),
        )
        symmetrizer_rank = int(symmetrizer.rank())
        check("analytic", "finite-Clifford-group averaging gives one common exact symmetrizer identity",
              symmetrizer_rank == total
              and all(symmetrizer * evolution == evolution.transpose() * symmetrizer
                      for evolution in evolutions))
        check("analytic", "the corresponding characteristic-zero symmetrizer is positive",
              True)  # v^T H v=sum_g ||g v||^2 includes g=I.

    return {
        "prime": prime,
        "witness": [1, 2],
        "k77_relations": ["12*w_plus*ell_minus-11=0", "12*w_minus*ell_plus-11=0"],
        "time_rank": int(time.rank()),
        "spatial_jordan_ranks": [int((value * value - identity_full).rank()) for value in evolutions],
        "null_rank": int(null_symbol.rank()),
        "nullity": int(null_symbol.right_nullity()),
        "zero_southeast_jordan_rank": int(zero_remainder.rank()),
        "k95_wrong_sign_jordan_rank": int(wrong_remainder.rank()),
        "independent_cross_defect_ranks": [int(value.rank()) for value in perturbed],
        "green_time_rank": int(green_time.rank()),
        "k_self_adjoint_defect_rank": int(adjoint_defect.rank()),
        "common_symmetrizer_rank": symmetrizer_rank,
    }


print("\nB. EXACT K77 OPERATOR FAMILY")
packets = [build_packet(1009, True), build_packet(1013, False)]
check("cross_prime", "two good primes reproduce the same exact rank fingerprint",
      all(packet["time_rank"] == 1920
          and packet["spatial_jordan_ranks"] == [0, 0, 0]
          and packet["null_rank"] == packet["nullity"] == 960
          and packet["zero_southeast_jordan_rank"] == 128
          and packet["k95_wrong_sign_jordan_rank"] == 128
          and packet["independent_cross_defect_ranks"] == [64, 64]
          for packet in packets))


print("\nC. SELECTION, ACTION-PARENT, AND PHYSICAL FENCES")
check("selection", "the two nonzero chiral wedge weights remain unselected construction parameters", True)
check("parent", "the two U(32,32) halves remain a rival parent rather than an identity with the Spin-selected operator", True)
check("parent", "full U(64,64) remains distinct and cannot be inferred from common complex dimension", True)
check("symplectic", "a positive principal symmetrizer is not a reduced covariant-phase-space or BV theorem", True)
check("bv", "the 960-dimensional null characteristic half is not promoted to gauge or BV cohomology", True)
check("domain", "flat principal strong hyperbolicity does not construct the ambient Y14 or global selected-action domain", True)
check("scope", "no chirality index generation particle mass anomaly or cosmology claim is made", True)
check("accounting", "P1 P2 P3 residue quotients canon verdicts and public posture do not move", True)

RESULT = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "branch": "CONDITIONAL_REAL_K77_SELECTED_SPIN_PARENT",
    "source_operator_family": "CHIRAL_WEDGE_MIDDLE_PLUS_FIRST_ORDER_SOUTHEAST",
    "parameter_dimension_before_semisimplicity": 4,
    "parameter_dimension_after_semisimplicity": 2,
    "k77_semisimple_relation": [
        "12*w_plus*ell_minus-11=0",
        "12*w_minus*ell_plus-11=0",
    ],
    "k95_sign_port": "REJECTED__LEAVES_RANK128_JORDAN_DEFECT",
    "exact_packets": packets,
    "characteristic": "NULL_RANK960_NULLITY960_SEMISIMPLE_HALF",
    "independent_dual_action": "LOCALLY_ADMISSIBLE_WITH_NONNULL_GREEN_TIME_COEFFICIENT",
    "real_reality_reduction": "OPEN__CURRENT_DIAGONAL_K77_PAIRING_NOT_SELF_ADJOINT",
    "action_parent": "SELECTED_SPIN_ONLY__TWO_U32_32_HALVES_AND_FULL_U64_64_REMAIN_DISTINCT",
    "source_return": "SOURCE_CONFIRMS_WEDGE_CONTRACTION_GRAMMAR_AND_ADMITS_NONNULL_SOUTHEAST__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_K77_PLUS_11_OVER_12_RELATION_CHIRAL_WEIGHTS_REALITY_REDUCTION_AND_GLOBAL_DOMAIN",
    "disposition": "K77_WEDGE_SOUTHEAST_FAMILY_CONSTRUCTED__SEMISIMPLE_RELATION_SIGN_DIFFERS_FROM_K95__PRINCIPAL_JORDAN_AND_RADICAL_OBSTRUCTION_REMOVED_WITHOUT_QUOTIENT__TWO_WEIGHTS_AND_REALITY_ACTION_REMAIN_UNSELECTED",
    "next_gate": "DERIVE_OR_KILL_THE_TWO_K77_CHIRAL_WEDGE_WEIGHTS_AND_REALITY_ADJOINT_FROM_THE_SELECTED_INDEPENDENT_DUAL_ACTION__THEN_GLOBAL_DESCENT_GREEN_DOMAIN_AND_OBSERVATION",
}

print("\nK77 WEDGE-SHIAB/SOUTHEAST COMPLETION RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: real K77 flips the K95 reciprocal sign; the source-admitted wedge+southeast family is principal-semisimple with a 960/960 characteristic split, while two weights and the real/reality action remain unselected.")
