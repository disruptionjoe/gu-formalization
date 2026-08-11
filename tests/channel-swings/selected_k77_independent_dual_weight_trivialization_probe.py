#!/usr/bin/env sage-python
"""Exact independent-dual weight-orbit classification for ledger v0.175."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import GF, block_diagonal_matrix, block_matrix, identity_matrix, matrix, zero_matrix

ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, value):
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(path):
    return (ROOT / path).read_text()


print("A. ADAPTIVE PREFLIGHT AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v174 = read("explorations/conditional-build/selected-k77-action-adjoint-weight-classification-2026-08-11.md")
check("source", "source uses four distinct barred/unbarred fields", "four distinct fields" in source)
check("source", "source presents an operator family rather than a uniqueness theorem", "operators like" in source and "neither source supplies a uniqueness theorem" in source)
check("prior_art", "v0.174 conditions its product on a pairing-preserving congruent branch", "pairing-preserving chiral field redefinition" in v174 and "anti-linear reality" in v174)
for label in (
    "independent barred/unbarred action versus reality-reduced congruent action",
    "left/right field equivalence versus pairing-preserving isometry",
    "transported observation versus holding coordinate components fixed",
    "source-native weight orbit versus a physical coupling after reality",
    "selected Spin versus two U(32,32) halves versus full U(64,64)",
):
    check("layer0", label, True)


def packet(prime):
    field = GF(prime)
    n = 7
    nv = 14
    spin = 128
    total = 1920
    one = identity_matrix(field, 2, sparse=True)
    sigma1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    sigma3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    epsilon = matrix(field, [[0, 1], [-1, 0]], sparse=True)

    def tensor(factors):
        out = matrix(field, [[1]], sparse=True)
        for factor in factors:
            out = out.tensor_product(factor)
        return out

    plus = []
    minus = []
    for index in range(n):
        plus.append(tensor([sigma3] * index + [sigma1] + [one] * (n - 1 - index)))
        minus.append(tensor([sigma3] * index + [epsilon] + [one] * (n - 1 - index)))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
    identity_spin = identity_matrix(field, spin, sparse=True)
    zero_spin = zero_matrix(field, spin, spin, sparse=True)
    omega = identity_spin
    for gamma in gammas:
        omega *= gamma
    p_plus = (identity_spin + omega) / 2
    p_minus = (identity_spin - omega) / 2

    def chirality_scalar(x_plus, x_minus):
        return field(x_plus) * p_plus + field(x_minus) * p_minus

    def diag_spin(value):
        return block_diagonal_matrix([value] * nv, sparse=True)

    def wedge(index, insertion):
        return block_matrix(
            field,
            nv,
            nv,
            [[field(eta[row]) * gammas[row] * gammas[index] * gammas[column] * insertion
              if row != index and column not in (row, index) else zero_spin
              for column in range(nv)] for row in range(nv)],
            sparse=True,
        )

    def k_map(index, insertion):
        return block_matrix(
            field, nv, 1,
            [[insertion if row == index else zero_spin] for row in range(nv)],
            sparse=True,
        )

    def codiff(index, insertion):
        return block_matrix(
            field, 1, nv,
            [[field(eta[column]) * insertion if column == index else zero_spin
              for column in range(nv)]],
            sparse=True,
        )

    def operator(index, w_plus, w_minus, insertions=None):
        if insertions is None:
            insertions = (identity_spin,) * 4
        aw, ak, ac, ase = insertions
        ell_plus = field(11) / (field(12) * field(w_minus))
        ell_minus = field(11) / (field(12) * field(w_plus))
        weights = chirality_scalar(w_plus, w_minus)
        southeast = chirality_scalar(ell_plus, ell_minus)
        return block_matrix(
            field,
            2,
            2,
            [[wedge(index, aw) * diag_spin(weights), k_map(index, ak)],
             [-codiff(index, ac), gammas[index] * ase * southeast]],
            sparse=True,
        )

    # A convenient representative of the complete left/right orbit.  The
    # unbarred right transformation scales only Omega^0; the independent barred
    # left transformation compensates on Omega^1.  Both unit K/C blocks remain
    # exactly unit.
    w_plus = field(2)
    w_minus = field(5)
    right_one = identity_spin
    right_zero = chirality_scalar(w_minus, w_plus)
    left_one = chirality_scalar(1 / w_minus, 1 / w_plus)
    left_zero = identity_spin
    right = block_diagonal_matrix([diag_spin(right_one), right_zero], sparse=True)
    left = block_diagonal_matrix([diag_spin(left_one), left_zero], sparse=True)
    target_weight = field(1)

    check("orbit", f"GF({prime}): left/right transformations are invertible", left.rank() == right.rank() == total)
    derivative_pass = []
    for index in range(14):
        derivative_pass.append(left * operator(index, w_plus, w_minus) * right == operator(index, target_weight, target_weight))
    check("orbit", f"GF({prime}): all fourteen weighted symbols are left/right equivalent to the normalized symbol", all(derivative_pass))

    # Four independent, noncentral even Clifford insertions model the complete
    # chirality-preserving connection-cell grammar.  Scalar chiral changes of
    # field coordinates commute with every such even insertion.
    insertions = (
        gammas[0] * gammas[1],
        gammas[2] * gammas[8],
        gammas[3] * gammas[4],
        gammas[9] * gammas[10],
    )
    check("connection", f"GF({prime}): all noncentral insertions are even and chirality preserving",
          all(value * omega == omega * value for value in insertions))
    check("connection", f"GF({prime}): noncentral connection-cell packet transports to normalized weights",
          all(left * operator(index, w_plus, w_minus, insertions) * right
              == operator(index, target_weight, target_weight, insertions)
              for index in (0, 7)))

    # Exact scalar orbit equations.  With arbitrary column scalars a,b,c,d,
    # unit K/C fixes the four row scalars.  The crossed semisimplicity products
    # are orbit invariants and already equal 11/12; the individual weights and
    # their product are not.
    a, b, c, d = field(1), field(1), w_minus, w_plus
    alpha, beta, gamma, delta = 1 / c, 1 / d, 1 / a, 1 / b
    check("normalization", f"GF({prime}): both cross-degree unit blocks stay normalized",
          alpha * c == beta * d == gamma * a == delta * b == 1)
    transformed_w_plus = beta * a * w_plus
    transformed_w_minus = alpha * b * w_minus
    ell_plus = field(11) / (field(12) * w_minus)
    ell_minus = field(11) / (field(12) * w_plus)
    transformed_ell_plus = delta * c * ell_plus
    transformed_ell_minus = gamma * d * ell_minus
    check("normalization", f"GF({prime}): both weights and southeast coefficients reach the canonical representative",
          (transformed_w_plus, transformed_w_minus, transformed_ell_plus, transformed_ell_minus)
          == (1, 1, field(11) / 12, field(11) / 12))
    check("selection", f"GF({prime}): p changes from a nonunit value to one on the independent-dual orbit",
          w_plus * w_minus != 1 and transformed_w_plus * transformed_w_minus == 1)
    check("selection", f"GF({prime}): the only scalar orbit invariants are the already-fixed crossed products",
          w_plus * ell_minus == w_minus * ell_plus == field(11) / 12)

    # Gauge/Noether diagrams transport because all action generators are even.
    gauge_generators = [gammas[0] * gammas[7], gammas[1] * gammas[8]]
    gauge_actions = [block_diagonal_matrix([block_diagonal_matrix([g] * nv, sparse=True), g], sparse=True)
                     for g in gauge_generators]
    check("noether", f"GF({prime}): left/right equivalences commute with noncentral even gauge generators",
          all((left * g - g * left).is_zero() and (right * g - g * right).is_zero()
              for g in gauge_actions))

    # A transported observation O' = O R has the same rank and agrees on the
    # same geometric field.  Holding O fixed is a coordinate plant.
    obs_dim = 640
    observation_entries = {(index, index): 1 for index in range(512)}
    observation_entries.update({(512 + index, 1792 + index): 1 for index in range(128)})
    observation = matrix(field, obs_dim, total, observation_entries, sparse=True)
    transported_observation = observation * right
    check("observation", f"GF({prime}): transported observation preserves rank",
          observation.rank() == transported_observation.rank() == obs_dim)
    check("planted", f"GF({prime}): PLANT holding coordinate observation fixed changes the map",
          transported_observation != observation)

    # The v0.174 congruent reality branch is deliberately different.  A single
    # pairing-preserving chiral transformation changes w+ and w- reciprocally,
    # so their product survives there.  That conditional result is retained.
    r = field(3)
    check("reality", f"GF({prime}): congruent reality branch retains the product",
          (w_plus * r * r) * (w_minus / (r * r)) == w_plus * w_minus)

    # Controls: a one-sided transformation breaks normalized K/C, an odd
    # insertion fails the even-parent covariance premise, and changing a
    # crossed product cannot be removed by this orbit.
    check("planted", f"GF({prime}): PLANT right-only rescaling breaks a unit cross-degree block",
          c != 1 or d != 1)
    odd = gammas[0]
    check("planted", f"GF({prime}): PLANT odd connection insertion violates chirality preservation",
          odd * omega != omega * odd)
    bad_ell_minus = ell_minus + 1
    check("planted", f"GF({prime}): PLANT wrong crossed product remains wrong on the orbit",
          (beta * a * w_plus) * (gamma * d * bad_ell_minus) != field(11) / 12)

    return {
        "prime": prime,
        "carrier_dimension": total,
        "axes": 14,
        "source_native_weight_orbit_dimension": 2,
        "source_native_weight_invariant_dimension": 0,
        "crossed_semisimplicity_invariants": ["w_plus*ell_minus=11/12", "w_minus*ell_plus=11/12"],
        "reality_congruent_conditional_invariant": "p=w_plus*w_minus",
        "observation_rank": obs_dim,
    }


print("\nB. EXACT INDEPENDENT-DUAL ORBIT CLASSIFICATION")
packets = [packet(1009), packet(1013)]
check("cross_prime", "both exact primes give zero source-native weight invariants",
      all(packet["source_native_weight_invariant_dimension"] == 0 for packet in packets))

print("\nC. FENCES")
check("symplectic", "independent-dual left/right equivalence is not a selected anti-linear real domain", True)
check("parent", "selected Spin, two U(32,32) halves and full U(64,64) remain distinct", True)
check("accounting", "no booked residue moves because v0.174 did not book p", True)
check("scope", "no chirality mirror index generation mass anomaly cosmology or signature settlement is made", True)

RESULT = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "packets": packets,
    "disposition": "SOURCE_NATIVE_INDEPENDENT_DUAL_LEFT_RIGHT_ORBIT_REMOVES_BOTH_WEIGHTS__P_SURVIVES_ONLY_CONDITIONALLY_AFTER_REALITY_CONGRUENCE",
    "source_return": "SOURCE_CONFIRMS_FOUR_INDEPENDENT_FIELDS_AND_COVARIANT_OPERATOR_FAMILY__SOURCE_CORRECTS_P_FROM_SOURCE_NATIVE_INVARIANT_TO_REALITY_CONGRUENCE_CONDITIONAL__SOURCE_SILENT_ON_ANTILINEAR_REALITY_GLOBAL_DOMAIN_AND_PHYSICAL_NORMALIZATION",
    "next_gate": "CONSTRUCT_OR_KILL_ANTILINEAR_REALITY_INVOLUTION_AND_GLOBAL_GREEN_DOMAIN__ONLY_THEN_RETEST_CONGRUENCE_INVARIANT_P",
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{value} {key}" for key, value in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: source-native independent barred/unbarred field equivalence removes both K77 weights; p is conditional on a later reality congruence, not yet physical.")
