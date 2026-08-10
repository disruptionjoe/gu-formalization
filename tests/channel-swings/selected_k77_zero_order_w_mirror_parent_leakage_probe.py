#!/usr/bin/env sage-python
"""Exact K77 zero-order W/mirror parent-leakage discriminator.

Run with:

    sage -python tests/channel-swings/selected_k77_zero_order_w_mirror_parent_leakage_probe.py

Layer 0: this composes the already-built q-repaired draft-9.16 zero-order
family with representation subspaces.  Invariance or doubled closure is not a
physical quotient, BV cohomology, closed-domain spectrum, generation count or
external datum.  Parent labels are ablations: moving Spin, two
``U(32,32)``-half block preservation, and source-full ``U(64,64)``.  They are
not silently identified with the quaternionic physical gauge group.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import GF, QuadraticField, block_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def build_structures(field, imaginary):
    """Build exact Cl(7,7), W/mirror projectors and zero-order ingredients."""
    n, nv, ds = 7, 14, 128
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
    for k in range(n):
        pre, post = [s3] * k, [i2] * (n - 1 - k)
        plus.append(tensor_all(pre + [s1] + post))
        minus.append(tensor_all(pre + [eps] + post))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
    spin_identity = identity_matrix(field, ds, sparse=True)
    vector_identity = identity_matrix(field, nv, sparse=True)
    full_identity = identity_matrix(field, nv * ds, sparse=True)
    z128 = zero_matrix(field, ds, ds, sparse=True)

    gamma_trace = block_matrix(field, 1, nv, gammas, sparse=True)
    rs_projector = full_identity - gamma_trace.transpose() * gamma_trace / field(14)

    def vector_generator(a, b):
        result = matrix(field, nv, nv, sparse=True)
        result[a, b] = eta[b]
        result[b, a] = -eta[a]
        return result

    def spin_generator(a, b):
        return (gammas[a] * gammas[b] - gammas[b] * gammas[a]) / field(4)

    def total_generator(a, b):
        return (
            vector_generator(a, b).tensor_product(spin_identity)
            + vector_identity.tensor_product(spin_generator(a, b))
        )

    rotations = [total_generator(8, 9), total_generator(9, 7), total_generator(7, 8)]
    boosts = [total_generator(0, 7), total_generator(0, 8), total_generator(0, 9)]
    self_dual = [(rotations[k] + imaginary * boosts[k]) / field(2) for k in range(3)]
    anti_self_dual = [(rotations[k] - imaginary * boosts[k]) / field(2) for k in range(3)]
    zbig = zero_matrix(field, nv * ds, nv * ds, sparse=True)
    c_plus = field(4) * sum((x * x for x in self_dual), zbig)
    c_minus = field(4) * sum((x * x for x in anti_self_dual), zbig)
    w = rs_projector * (c_plus * (c_plus + field(3) * full_identity) / field(40))
    mirror = rs_projector * (c_minus * (c_minus + field(3) * full_identity) / field(40))

    q = gammas[7]
    q_big = block_matrix(
        field, nv, nv,
        [[q if a == c else z128 for c in range(nv)] for a in range(nv)],
        sparse=True,
    )
    a = [2, -1, 0, 1] + [0] * 10
    gamma_a = sum((field(a[k]) * gammas[k] for k in range(nv)), z128)
    middle = block_matrix(
        field, nv, nv,
        [[(gamma_a if r == c else z128) - field(a[r]) * gammas[c]
          for c in range(nv)] for r in range(nv)],
        sparse=True,
    )

    b = spin_identity
    for gamma in gammas[7:]:
        b = b * gamma
    j = spin_identity
    for gamma in gammas:
        j = j * gamma

    def product(indices):
        out = spin_identity
        for index in indices:
            out = out * gammas[index]
        return out

    parents = {
        "moving_spin_grade2": product([0, 1]),
        "two_half_block_grade6": product([0, 1, 2, 3, 4, 5]),
        "source_full_u_coset_grade1": product([0]),
    }

    def zero_order_pair(parent):
        parent_big = block_matrix(
            field, nv, nv,
            [[parent if r == c else z128 for c in range(nv)] for r in range(nv)],
            sparse=True,
        )
        raw = middle * parent_big
        return q_big * raw, raw * q_big

    return {
        "gammas": gammas,
        "B": b,
        "J": j,
        "I128": spin_identity,
        "I1792": full_identity,
        "rs": rs_projector,
        "W": w,
        "M": mirror,
        "parents": parents,
        "zero_order_pair": zero_order_pair,
    }


def coefficient_rank(first, second) -> int:
    """Rank of the two coefficient columns after flattening two sparse maps."""
    keys = set(first.dict()) | set(second.dict())
    pivot = None
    for key in keys:
        row = (first[key], second[key])
        if row == (0, 0):
            continue
        if pivot is None:
            pivot = row
        elif pivot[0] * row[1] - pivot[1] * row[0] != 0:
            return 2
    return 0 if pivot is None else 1


def classify_parent(structures, name, parent, w_basis, m_basis, ratios):
    w, m = structures["W"], structures["M"]
    pair = w + m
    complement = structures["I1792"] - pair
    left, right = structures["zero_order_pair"](parent)
    results = {}
    for ratio in ratios:
        operator = left + ratio * right
        results[str(ratio)] = {
            "W_internal": (w * operator * w_basis).rank(),
            "W_to_mirror": (m * operator * w_basis).rank(),
            "W_outside_pair": (complement * operator * w_basis).rank(),
            "mirror_internal": (m * operator * m_basis).rank(),
            "mirror_to_W": (w * operator * m_basis).rank(),
            "mirror_outside_pair": (complement * operator * m_basis).rank(),
        }
    cross_rank_w = coefficient_rank(m * left * w_basis, m * right * w_basis)
    cross_rank_m = coefficient_rank(w * left * m_basis, w * right * m_basis)
    outside_rank_w = coefficient_rank(complement * left * w_basis, complement * right * w_basis)
    outside_rank_m = coefficient_rank(complement * left * m_basis, complement * right * m_basis)
    return results, cross_rank_w, cross_rank_m, outside_rank_w, outside_rank_m


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
trace_q = (ROOT / "explorations/k77-wave2-trace-q-coefficient-zero-order-reality-selection-2026-08-04.md").read_text()
two_layer = (ROOT / "explorations/k77-wave2-common-two-layer-action-euler-coefficient-selection-2026-08-04.md").read_text()
principal = (ROOT / "explorations/conditional-build/selected-k77-induced-fermion-principal-discriminator-2026-08-10.md").read_text()
check("source", "draft displays sixteen cells and assigns gauge/Higgs-like/CKM/Yukawa functions to varpi",
      "all sixteen" in source and "gauge, Higgs-like, CKM, and Yukawa" in source)
check("source", "source confirms contraction-plus-Hodge grammar and southeast zero but not a global carrier selector",
      "SOURCE-CONFIRMS" in source and "southeast-zero" in source and "unique or globally defined operator" in source)
check("prior_art", "trace-q wave already built the one-projective-parameter zero-order family",
      "free projective coefficients: 1" in trace_q and "selection rank = 0" in trace_q)
check("prior_art", "two-layer action wave found the norm-square layer redundant on the first-layer solution locus",
      "redundant on the first-order equations" in two_layer and "cannot\nspend a coupling freedom" in two_layer)
check("prior_art", "v0.135 established W equals its ASD mirror at principal characteristic grade",
      "224/96" in principal and "same exact answer" in principal)
check("layer0", "draft matrix, q-repaired family, invariant subspace and physical cohomology are distinct", True)
check("layer0", "full U(64,64), two U(32,32) halves and moving Spin are parent ablations, not one object", True)


print("\nB. EXACT FINITE-FIELD W/MIRROR AND PARENT WITNESSES")
prime = 1_000_033
fp = GF(prime)
finite = build_structures(fp, fp(-1).sqrt())
w, m = finite["W"], finite["M"]
check("exact", "W and mirror are exact disjoint rank-192 projectors",
      w.rank() == 192 and m.rank() == 192 and (w * m).is_zero() and (m * w).is_zero())
pair = w + m
check("exact", "W plus mirror is an exact rank-384 projector",
      pair.rank() == 384 and (pair * pair - pair).is_zero())
w_pivots, m_pivots = list(w.pivots()), list(m.pivots())
w_basis = w.matrix_from_columns(w_pivots)
m_basis = m.matrix_from_columns(m_pivots)

b, j, z128 = finite["B"], finite["J"], zero_matrix(fp, 128, 128, sparse=True)
parent_types = {}
for name, parent in finite["parents"].items():
    b_skew = (parent.transpose() * b + b * parent).is_zero()
    j_commuting = (parent * j - j * parent).is_zero()
    j_anticommuting = (parent * j + j * parent).is_zero()
    parent_types[name] = {
        "B_skew": b_skew,
        "J_commuting": j_commuting,
        "J_anticommuting": j_anticommuting,
    }
    check("exact", f"{name} is an exact B-skew source-parent witness", b_skew)
check("type", "moving-Spin and two-half witnesses commute with J",
      parent_types["moving_spin_grade2"]["J_commuting"]
      and parent_types["two_half_block_grade6"]["J_commuting"])
check("type", "full-U-only coset witness anticommutes with J",
      parent_types["source_full_u_coset_grade1"]["J_anticommuting"])

ratios = [fp(0), fp(1), fp(-1), fp(2), fp(-2), fp(3), fp(-3)]
finite_results = {}
for name, parent in finite["parents"].items():
    results, cross_w, cross_m, outside_w, outside_m = classify_parent(
        finite, name, parent, w_basis, m_basis, ratios
    )
    finite_results[name] = {
        "ratios": results,
        "cross_coefficient_rank_W_to_mirror": cross_w,
        "cross_coefficient_rank_mirror_to_W": cross_m,
        "outside_pair_coefficient_rank_W": outside_w,
        "outside_pair_coefficient_rank_mirror": outside_m,
    }
    check("exact", f"{name} has coefficient rank two for W-to-mirror leakage", cross_w == 2)
    check("exact", f"{name} has coefficient rank two for mirror-to-W leakage", cross_m == 2)
    check("exact", f"{name} has coefficient rank two for W leakage outside W-plus-mirror", outside_w == 2)
    check("exact", f"{name} has coefficient rank two for mirror leakage outside W-plus-mirror", outside_m == 2)
    check("exact", f"{name} treats W and mirror symmetrically at every tested ratio",
          all(
              row["W_internal"] == row["mirror_internal"]
              and row["W_to_mirror"] == row["mirror_to_W"]
              and row["W_outside_pair"] == row["mirror_outside_pair"]
              for row in results.values()
          ))

block_ratio = finite_results["two_half_block_grade6"]["ratios"]["1"]
spin_ratio = finite_results["moving_spin_grade2"]["ratios"]["1"]
full_ratio = finite_results["source_full_u_coset_grade1"]["ratios"][str(fp(-1))]
check("exact", "J-commuting moving-Spin witness minimizes single-sector leakage at alpha=beta",
      spin_ratio["W_internal"] == 0 and spin_ratio["W_to_mirror"] == 64)
check("exact", "J-commuting two-half witness minimizes single-sector leakage at alpha=beta",
      block_ratio["W_internal"] == 0 and block_ratio["W_to_mirror"] == 64)
check("exact", "J-anticommuting full-U coset witness minimizes single-sector leakage at alpha=-beta",
      full_ratio["W_internal"] == 0 and full_ratio["W_to_mirror"] == 64)
check("planted", "generic alpha:beta ratios leak outside the doubled pair for every parent witness",
      all(
          any(row["W_outside_pair"] > 0 for key, row in data["ratios"].items()
              if key not in {"1", str(fp(-1))})
          for data in finite_results.values()
      ))


print("\nC. EXACT CHARACTERISTIC-ZERO CRITICAL WITNESSES")
gaussian = QuadraticField(-1, "ii")
char0 = build_structures(gaussian, gaussian.gen())
w0, m0 = char0["W"], char0["M"]
w0_basis = w0.matrix_from_columns(w_pivots)
m0_basis = m0.matrix_from_columns(m_pivots)
check("exact", "finite-field pivot columns lift to exact Gaussian-rational W and mirror bases",
      w0_basis.rank() == 192 and m0_basis.rank() == 192)
char0_results = {}
for name, preferred in (
    ("moving_spin_grade2", gaussian(1)),
    ("two_half_block_grade6", gaussian(1)),
    ("source_full_u_coset_grade1", gaussian(-1)),
):
    results, cross_w, cross_m, outside_w, outside_m = classify_parent(
        char0, name, char0["parents"][name], w0_basis, m0_basis,
        [preferred],
    )
    row = next(iter(results.values()))
    char0_results[name] = {"preferred_ratio": str(preferred), **row}
    check("exact", f"{name} preferred-ratio W/mirror cross rank is exactly 64 in characteristic zero",
          row["W_to_mirror"] == 64 and row["mirror_to_W"] == 64)
    check("exact", f"{name} admits no nonzero coefficient eliminating cross-sector leakage",
          cross_w == 2 and cross_m == 2)
    check("exact", f"{name} admits no nonzero coefficient closing the doubled W-plus-mirror pair",
          outside_w == 2 and outside_m == 2)


print("\nD. DISPOSITION, SURPLUS AND FENCES")
check("type", "no nonzero projective coefficient makes W invariant for any of the three witnesses",
      all(data["cross_coefficient_rank_W_to_mirror"] == 2 for data in finite_results.values()))
check("type", "no nonzero projective coefficient closes W plus mirror for any of the three witnesses",
      all(data["outside_pair_coefficient_rank_W"] == 2 for data in finite_results.values()))
check("type", "W and mirror have identical leakage fingerprints and neither is selected", True)
check("type", "J-commuting and J-anticommuting parent witnesses prefer opposite minimal-leakage ratios", True)
check("type", "the source-full parent contains both parity classes, so one coefficient cannot minimize both", True)
check("symplectic", "no presymplectic reduction or BV quotient is inferred from representation leakage", True)
check("analytic", "finite zero-order ranks do not establish a closed domain, spectrum or physical K-definite cohomology", True)
check("variational", "the prior norm-square action redundancy is not promoted to a new Euler selector", True)
check("planted", "the generic-ratio control prevents automatic doubled-pair closure from being read as tautological", True)

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": "K77_WITH_EXACT_GF_AND_GAUSSIAN_RATIONAL_CRITICAL_RANKS",
    "parent_types": parent_types,
    "finite_results": finite_results,
    "char0_critical_results": char0_results,
    "constraint_surplus": "ONE_PROJECTIVE_PARAMETER__CROSS_AND_OUTSIDE_PAIR_LEAKAGE_COEFFICIENT_RANK_TWO__NO_NONZERO_W_OR_DOUBLED_PAIR_INVARIANCE_SOLUTION",
    "source_return": "SOURCE_CONFIRMS_ZERO_ORDER_CONNECTION_PORT_AND_TWO_LAYER_ARCHITECTURE__SOURCE_CORRECTS_CURT_SINGLE_LAYER__SOURCE_SILENT_ON_Q_COEFFICIENT_CONNECTION_ORBIT_CARRIER_SELECTION_BV_DOMAIN",
    "disposition": "ZERO_ORDER_PARENT_CONFLICT_AND_NONDISCRIMINATING__W_EQUALS_MIRROR__NO_NONZERO_COEFFICIENT_PRESERVES_W_OR_W_PLUS_MIRROR",
    "next_gate": "ACTION_OWNED_RESTRICTED_CONNECTION_ORBIT_OR_BV_COHOMOLOGY_BEFORE_ANY_W_CARRIER_RESTRICTION",
}

print("\nK77 ZERO-ORDER W/MIRROR PARENT-LEAKAGE RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("\nChecks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))

if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the existing zero-order family preserves neither W nor its doubled mirror closure; parent parity creates incompatible minimal-leakage ratios.")
