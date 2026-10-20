#!/usr/bin/env sage-python
"""K1822: rational lift of the declared K435--K439 principal fixture.

No predecessor numerical producer is imported. All identities are over QQ;
finite characteristic is used only for a rigorous rank lower bound and
comparison with historical matrix digests. Run with Sage's Python.
"""
from __future__ import annotations

import argparse
from copy import copy
import hashlib
import json
from math import lcm, gcd
import time
from pathlib import Path

from sage.all import QQ, GF, block_matrix, block_diagonal_matrix, identity_matrix, matrix, zero_matrix

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1822-k77-rational-corrected-carrier.json"
OBS = (0, 7, 8, 9)
PRIMES = (1009, 1013)


def digest(m, rational=False):
    entries = [[int(i), int(j), str(v) if rational else int(v)]
               for (i, j), v in sorted(m.dict().items()) if v]
    payload = {"shape": [int(m.nrows()), int(m.ncols())], "entries": entries}
    return "sha256:" + hashlib.sha256(json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def tensor(factors):
    out = matrix(QQ, [[1]], sparse=True)
    for f in factors:
        out = out.tensor_product(f)
    return out


def sparse_block_inverse(m):
    """Invert disconnected bipartite support components, then verify globally."""
    n = m.nrows()
    assert m.ncols() == n
    adjacency = {j:set() for j in range(2*n)}
    for r,c in m.dict():
        adjacency[r].add(n+c)
        adjacency[n+c].add(r)
    seen, result, sizes = set(), {}, []
    for vertex in range(2*n):
        if vertex in seen:
            continue
        pending, component = [vertex], set()
        while pending:
            v = pending.pop()
            if v in component:
                continue
            component.add(v)
            pending.extend(adjacency[v]-component)
        seen.update(component)
        rows = sorted(v for v in component if v < n)
        cols = sorted(v-n for v in component if v >= n)
        assert len(rows) == len(cols) and rows
        inv = m.matrix_from_rows_and_columns(rows, cols).inverse()
        sizes.append(len(rows))
        for (r,c),v in inv.dict().items():
            result[cols[r],rows[c]] = v
    out = matrix(QQ,n,n,result,sparse=True)
    assert out*m == identity_matrix(QQ,n,sparse=True) == m*out
    return out, sizes


def construct():
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    i2 = identity_matrix(QQ, 2, sparse=True)
    s1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)
    gs = [tensor([s3] * j + [v] + [i2] * (6-j))
          for v in (s1, eps) for j in range(7)]
    eta = [1]*7 + [-1]*7
    I = identity_matrix(QQ, 128, sparse=True)
    Z = zero_matrix(QQ, 128, 128, sparse=True)
    volume = I
    for g in gs:
        volume = volume*g
    check("all_Clifford_relations", all(gs[i]*gs[j]+gs[j]*gs[i] == (2*eta[i]*I if i == j else Z)
                                               for i in range(14) for j in range(i, 14)))
    pp, pm = (I+volume)/2, (I-volume)/2
    W, Wi = pp+2*pm, pp+pm/2
    S = 11*pp/24+11*pm/12
    check("chirality_weights_inverse", W*Wi == I)

    def blocks(rows):
        return block_matrix(QQ, rows, sparse=True)

    def symbol(k):
        rows = []
        for r in range(14):
            rows.append([eta[r]*gs[r]*gs[k]*gs[c]*W
                         if r != k and c not in (r, k) else Z for c in range(14)]
                        + [I if r == k else Z])
        rows.append([-eta[c]*I if c == k else Z for c in range(14)] + [gs[k]*S])
        return blocks(rows)

    # Exact elimination of D0, derived in the accompanying proof.
    inverse_rows = [[Z]*15 for _ in range(15)]
    inverse_rows[0][0], inverse_rows[0][14] = gs[0]*S, -I
    inverse_rows[14][0] = I
    for r in range(1, 14):
        for c in range(1, 14):
            inverse_rows[r][c] = Wi*eta[r]*gs[r]*gs[0]*gs[c]*(QQ(1)/12-(1 if r == c else 0))
    D0, D0i = symbol(0), blocks(inverse_rows)
    I1920 = identity_matrix(QQ, 1920, sparse=True)
    check("rational_time_right_inverse", D0*D0i == I1920)
    check("rational_time_left_inverse", D0i*D0 == I1920)

    observation = blocks([[I if r == s else Z for r in range(15)] for s in OBS+(14,)])
    gamma = blocks([[eta[j]*gs[j] for j in OBS]])
    I640 = identity_matrix(QQ, 640, sparse=True)
    seed = blocks([[I if r == 14 else Z] for r in range(15)])
    evolutions = {k:D0i*symbol(k) for k in (7,8,9)}
    words = [seed, evolutions[7]*seed, evolutions[8]*seed, evolutions[9]*seed,
             evolutions[7]*evolutions[8]*seed, evolutions[7]*evolutions[9]*seed,
             evolutions[8]*evolutions[9]*seed, evolutions[7]*evolutions[8]*evolutions[9]*seed]
    span = block_matrix(QQ, 1, 8, [words], sparse=True)
    observed_span = observation*span
    span_denominator = lcm(*(int(v.denominator()) for v in observed_span.dict().values()))
    check("rank_witness_denominators_invertible", gcd(span_denominator, 1009) == 1)
    pivots = observed_span.change_ring(GF(1009)).pivots()
    rank_lower = len(pivots)
    check("good_reduction_rank_lower_640", rank_lower == 640)
    basis = span.matrix_from_columns(pivots)
    observed_inverse, inverse_block_sizes = sparse_block_inverse(observation*basis)
    lift = basis*observed_inverse
    check("observation_lift_identity", observation*lift == I640)
    check("seed_in_graph", lift*observation*seed == seed)
    for k,e in evolutions.items():
        check("rational_graph_invariant_"+str(k), lift*observation*e*lift == e*lift)
    check("all_words_in_graph", lift*observation*span == span)
    check("rational_word_span_rank_640", rank_lower == 640)

    trace_lift = blocks([[gs[j]/4] for j in OBS])
    check("gamma_trace_split", gamma*trace_lift == I)
    P = block_diagonal_matrix([identity_matrix(QQ, 512, sparse=True)-trace_lift*gamma, I], sparse=True)
    check("rational_corrected_projector", P*P == P and P.trace() == 512)
    reduced = observation*evolutions[7]*lift
    check("rational_observed_normal_involution", reduced*reduced == I640)
    A = P*reduced*P
    check("rational_compressed_endomorphism", P*A == A and A*P == A)
    A2 = A*A
    check("rational_quartic", 576*A2*A2-577*A2+P == 0)
    fast, slow = (576*A2-P)/575, 576*(P-A2)/575
    projectors = [(P+A)*fast/2, (P-A)*fast/2, (P+24*A)*slow/2, (P-24*A)*slow/2]
    roots = [QQ(1), QQ(-1), QQ(1)/24, QQ(-1)/24]
    check("four_projectors_sum", sum(projectors) == P)
    check("four_projectors_idempotent_orthogonal", all(x*y == (x if i == j else 0)
          for i, x in enumerate(projectors) for j, y in enumerate(projectors)))
    check("four_projectors_eigenvalue_equations", all(A*x == lam*x for x, lam in zip(projectors, roots)))
    ranks = [int(x.trace()) for x in projectors]
    check("rational_spectral_multiplicities", ranks == [192,192,64,64])
    sign = sum((1 if lam > 0 else -1)*x for x,lam in zip(projectors,roots))
    check("rational_sign_cubic", sign == (-QQ(576)/25*A*A2+QQ(601)/25*A))
    check("rational_sign_involution", sign*sign == P)
    check("rational_split_half_ranks", (P+sign).trace()/2 == 256 and (P-sign).trace()/2 == 256)

    # Computation-level faults: retain observation identity but break the graph;
    # retain BOTH old modular matrices but break the rational polynomial.
    bad_lift = copy(lift)
    bad_lift[128, 0] += 1
    check("planted_wrong_graph_rejected", observation*bad_lift == I640 and
          bad_lift*observation*evolutions[7]*bad_lift != evolutions[7]*bad_lift)
    bad_A = A + (1009*1013)*P
    check("planted_two_prime_invisible_error_rejected",
          all(bad_A.change_ring(GF(p)) == A.change_ring(GF(p)) for p in PRIMES) and
          576*bad_A**4-577*bad_A**2+P != 0)

    old435 = json.loads((ROOT/"lab/process/k435-k77-full-h640-observed-map.json").read_text())
    old438 = json.loads((ROOT/"lab/process/k438-k77-constraint-compressed-boundary-symbol.json").read_text())
    old_bindings = {}
    for prime in PRIMES:
        field = GF(prime)
        actual = {"ambient_inverse_lift": digest(lift.change_ring(field)),
                  "compressed_symbol": digest(A.change_ring(field)),
                  "fast_projector": digest(fast.change_ring(field)),
                  "slow_projector": digest(slow.change_ring(field))}
        expected = {"ambient_inverse_lift": old435["serialization_contract"][f"gf{prime}_digests"]["ambient_inverse_lift"],
                    **{k: old438["cross_characteristic_result"][f"gf{prime}_digests"][k]
                       for k in ("compressed_symbol", "fast_projector", "slow_projector")}}
        check("historical_fixture_digests_"+str(prime), actual == expected)
        old_bindings[str(prime)] = actual
    return {"checks": checks, "rational_spectral_multiplicities": ranks,
            "corrected_lift_equals_coordinate_lift":bool(lift*P == observation.transpose()*P),
            "observed_inverse_blocks":{"count":len(inverse_block_sizes),"largest":max(inverse_block_sizes)},
            "rank_lower_bound": {"prime":1009,"rank":rank_lower,"denominator_lcm":span_denominator,
                                 "argument":"good reduction nonzero minor plus rational invariant graph upper bound"},
            "rational_matrices": {name:{"shape":[int(x.nrows()),int(x.ncols())],"nnz":len(x.dict()),"digest":digest(x, True)}
                                  for name,x in (("lift",lift),("P",P),("A",A),("fast",fast),("slow",slow),("sign",sign))},
            "historical_fixture_digests":old_bindings}


def produce():
    return {"schema_version":"1.0", "result_id":"K1822-K77-RATIONAL-CORRECTED-CARRIER",
            "created":"2026-10-20", "status":"active_research", "classification":"INTERNAL_STRUCTURAL_ONLY",
            "target_claim":"NONE-NOT-A-KILL",
            "scope":"Exact rational coefficient lift of the conditional K435-K439 principal fixture; no functional or physical completion.",
            "certificate":construct(),
            "algebra_consequences": {"carrier":"im(P), dimension 512, with identity P; not the full observed 640-space",
                "minimal_polynomial":"(x^2-1)(x^2-1/576)",
                "characteristic_polynomial":"(x^2-1)^192 (x^2-1/576)^64",
                "real_polynomial_algebra_dimension":4,"minimum_nonzero_idempotent_rank":64,
                "base_map_tensor_polynomial_arrow_rank_divisor":64,
                "corrected_incoming_outgoing_ranks":[256,256]},
            "claim_boundary":{"new_source_action_coefficients":False,"physical_state":False,
                "nonfactorized_KT_differential":False,"Euclidean_ellipticity":False,"ledger_effect":"none","canon_effect":"none"}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the admitted native certificate")
    parser.add_argument("--check", action="store_true", help="recompute and compare the native certificate")
    args = parser.parse_args()
    started = time.monotonic()
    data = produce()
    if args.write:
        ARTIFACT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    if args.check:
        assert json.loads(ARTIFACT.read_text()) == data, "artifact differs from exact recomputation"
    print(json.dumps({"checks":len(data["certificate"]["checks"]),"seconds":round(time.monotonic()-started,3),
                      "ranks":data["certificate"]["rational_spectral_multiplicities"],"artifact_written":args.write},sort_keys=True))


if __name__ == "__main__":
    main()
