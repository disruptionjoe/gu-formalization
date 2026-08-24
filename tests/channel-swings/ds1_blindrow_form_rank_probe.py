#!/usr/bin/env python3
"""DS1-BR -- exact invariant-form ranks for the Lambda1/Lambda5 blind rows.

RSC-1 gives only the multiplicities of the alternating channels on

    zeta = V_14 tensor S_+ = T(64) direct-sum R(832).

Multiplicity does not determine rank.  This probe constructs the D7
highest-weight intertwiners in Lambda^2(zeta), splits them with the exact
gamma-trace projector, transports one common insertion direction through
lower-root unipotents, and computes all ranks exactly over two prime fields.
A full-rank witness modulo either prime proves that the corresponding
determinant polynomial is nonzero over Q and hence generically nonzero over C.

Run:
    python3 tests/channel-swings/ds1_blindrow_form_rank_probe.py
    python3 tests/channel-swings/ds1_blindrow_form_rank_probe.py --selftest
"""

from __future__ import annotations

from collections import defaultdict
import hashlib
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
import scipy.sparse as sp


ROOT = Path(__file__).resolve().parents[2]
RSC1 = ROOT / "tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py"
RESULT = ROOT / "explorations/generation-sector/ds1-blindrow-form-rank-2026-08-24.md"
REGISTER = ROOT / "lab/process/upgrade-program-register.yaml"
RSC1_SHA = "a161d8a5a326e81d1fef07259e6f21c66253f83c62a21b113d0b7ea1b6a99ee0"
PRIMES = (1_000_003, 1_000_033)
N = 7
DIM_ZETA = 896
MUT = os.environ.get("DS1BR_MUT", "")

CHECKS = 0
FAILS: list[str] = []


def check(label: str, condition: bool) -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print(f"[OK]   {label}")
    else:
        FAILS.append(label)
        print(f"[FAIL] {label}")


SPIN = [bits for bits in range(1 << N) if bits.bit_count() % 2 == 0]
SPIN_INDEX = {bits: i for i, bits in enumerate(SPIN)}
VEC = [(i, sign) for i in range(N) for sign in (1, -1)]
VEC_INDEX = {v: i for i, v in enumerate(VEC)}
ZETA = [(vi, si) for vi in range(14) for si in range(64)]


def spin_weight(bits: int) -> tuple[int, ...]:
    return tuple(1 if bits >> i & 1 else -1 for i in range(N))


def vec_weight(v: tuple[int, int]) -> tuple[int, ...]:
    out = [0] * N
    out[v[0]] = 2 * v[1]
    return tuple(out)


ZETA_WEIGHTS = [
    tuple(a + b for a, b in zip(vec_weight(VEC[vi]), spin_weight(SPIN[si])))
    for vi, si in ZETA
]


def annihilate(bits: int, i: int):
    if not bits >> i & 1:
        return None
    sign = -1 if (bits & ((1 << i) - 1)).bit_count() % 2 else 1
    return bits ^ (1 << i), sign


def create(bits: int, i: int):
    if bits >> i & 1:
        return None
    sign = -1 if (bits & ((1 << i) - 1)).bit_count() % 2 else 1
    return bits | (1 << i), sign


def spin_raise(si: int, root: int):
    bits = SPIN[si]
    if root < 6:
        first = annihilate(bits, root + 1)
        if first is None:
            return []
        second = create(first[0], root)
    else:
        first = create(bits, 6)
        if first is None:
            return []
        second = create(first[0], 5)
    if second is None:
        return []
    return [(SPIN_INDEX[second[0]], first[1] * second[1])]


def vec_raise(vi: int, root: int):
    item = VEC[vi]
    if root < 6:
        if item == (root + 1, 1):
            return [(VEC_INDEX[(root, 1)], 1)]
        if item == (root, -1):
            sign = 1 if MUT == "bad_raise" and root == 0 else -1
            return [(VEC_INDEX[(root + 1, -1)], sign)]
    else:
        if item == (6, -1):
            return [(VEC_INDEX[(5, 1)], 1)]
        if item == (5, -1):
            return [(VEC_INDEX[(6, 1)], -1)]
    return []


def zeta_raise(zi: int, root: int):
    vi, si = ZETA[zi]
    out = [(v2 * 64 + si, c) for v2, c in vec_raise(vi, root)]
    out += [(vi * 64 + s2, c) for s2, c in spin_raise(si, root)]
    return out


def sparse_nullspace(target: tuple[int, ...], prime: int):
    by_weight: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for i, weight in enumerate(ZETA_WEIGHTS):
        by_weight[weight].append(i)
    pairs: list[tuple[int, int]] = []
    pair_index: dict[tuple[int, int], int] = {}
    for i, weight in enumerate(ZETA_WEIGHTS):
        need = tuple(t - x for t, x in zip(target, weight))
        for j in by_weight.get(need, []):
            if i < j:
                pair_index[(i, j)] = len(pairs)
                pairs.append((i, j))

    equations: dict[tuple[int, tuple[int, int]], dict[int, int]] = defaultdict(dict)
    for column, (i, j) in enumerate(pairs):
        for root in range(N):
            for k, value in zeta_raise(i, root):
                if k == j:
                    continue
                pair = (k, j) if k < j else (j, k)
                sign = 1 if k < j else -1
                row = equations[(root, pair)]
                row[column] = (row.get(column, 0) + sign * value) % prime
            for k, value in zeta_raise(j, root):
                if i == k:
                    continue
                pair = (i, k) if i < k else (k, i)
                sign = 1 if i < k else -1
                row = equations[(root, pair)]
                row[column] = (row.get(column, 0) + sign * value) % prime

    pivots: dict[int, dict[int, int]] = {}
    for raw in equations.values():
        row = {c: v for c, v in raw.items() if v}
        while row:
            column = min(row)
            if column not in pivots:
                inv = pow(row[column], prime - 2, prime)
                pivots[column] = {k: v * inv % prime for k, v in row.items()}
                break
            factor = row[column]
            for k, value in pivots[column].items():
                new = (row.get(k, 0) - factor * value) % prime
                if new:
                    row[k] = new
                else:
                    row.pop(k, None)

    free = [c for c in range(len(pairs)) if c not in pivots]
    basis = []
    for free_column in free:
        vector = {free_column: 1}
        for column in sorted(pivots, reverse=True):
            value = -sum(
                coefficient * vector.get(k, 0)
                for k, coefficient in pivots[column].items()
                if k != column
            ) % prime
            if value:
                vector[column] = value
        basis.append(vector)
    return pairs, basis


def dense_form(pairs, vector, prime):
    matrix = np.zeros((DIM_ZETA, DIM_ZETA), dtype=np.int64)
    for column, value in vector.items():
        i, j = pairs[column]
        matrix[i, j] = value
        matrix[j, i] = -value % prime
    return matrix


def rank_mod(matrix, prime):
    matrix = matrix.copy() % prime
    rank = 0
    for column in range(DIM_ZETA):
        nonzero = np.flatnonzero(matrix[rank:, column])
        if not len(nonzero):
            continue
        pivot = rank + int(nonzero[0])
        matrix[[rank, pivot]] = matrix[[pivot, rank]]
        inv = pow(int(matrix[rank, column]), prime - 2, prime)
        matrix[rank, column:] = matrix[rank, column:] * inv % prime
        rows = np.flatnonzero(matrix[rank + 1 :, column]) + rank + 1
        if len(rows):
            factors = matrix[rows, column].copy()
            matrix[rows, column:] = (
                matrix[rows, column:]
                - factors[:, None] * matrix[rank, column:]
            ) % prime
        rank += 1
        if rank == DIM_ZETA:
            break
    return rank


def spin_lower(si: int, root: int):
    bits = SPIN[si]
    if root < 6:
        first = annihilate(bits, root)
        if first is None:
            return []
        second = create(first[0], root + 1)
    else:
        first = annihilate(bits, 5)
        if first is None:
            return []
        second = annihilate(first[0], 6)
    if second is None:
        return []
    return [(SPIN_INDEX[second[0]], first[1] * second[1])]


def vec_lower(vi: int, root: int):
    item = VEC[vi]
    if root < 6:
        if item == (root, 1):
            return [(VEC_INDEX[(root + 1, 1)], 1)]
        if item == (root + 1, -1):
            return [(VEC_INDEX[(root, -1)], -1)]
    else:
        if item == (6, 1):
            return [(VEC_INDEX[(5, -1)], -1)]
        if item == (5, 1):
            return [(VEC_INDEX[(6, -1)], 1)]
    return []


def lower_unipotent(root: int, parameter: int):
    rows, columns, data = [], [], []
    for zi, (vi, si) in enumerate(ZETA):
        rows.append(zi)
        columns.append(zi)
        data.append(1)
        vector_terms = vec_lower(vi, root)
        spinor_terms = spin_lower(si, root)
        for v2, a in vector_terms:
            rows.append(v2 * 64 + si)
            columns.append(zi)
            data.append(parameter * a)
        for s2, a in spinor_terms:
            rows.append(vi * 64 + s2)
            columns.append(zi)
            data.append(parameter * a)
        for v2, a in vector_terms:
            for s2, b in spinor_terms:
                rows.append(v2 * 64 + s2)
                columns.append(zi)
                data.append(parameter * parameter * a * b)
    return sp.csr_matrix(
        (data, (rows, columns)), shape=(DIM_ZETA, DIM_ZETA), dtype=np.int64
    )


def gamma_projectors(prime: int):
    odd = [bits for bits in range(1 << N) if bits.bit_count() % 2]
    odd_index = {bits: i for i, bits in enumerate(odd)}
    cr, cc, cd, jr, jc, jd = [], [], [], [], [], []
    for zi, (vi, si) in enumerate(ZETA):
        index, sign = VEC[vi]
        image = create(SPIN[si], index) if sign == 1 else annihilate(SPIN[si], index)
        if image is not None:
            cr.append(odd_index[image[0]])
            cc.append(zi)
            cd.append(image[1])
    for column, bits in enumerate(odd):
        for index in range(N):
            image = annihilate(bits, index)
            if image is not None:
                jr.append(VEC_INDEX[(index, 1)] * 64 + SPIN_INDEX[image[0]])
                jc.append(column)
                jd.append(image[1])
            image = create(bits, index)
            if image is not None:
                jr.append(VEC_INDEX[(index, -1)] * 64 + SPIN_INDEX[image[0]])
                jc.append(column)
                jd.append(image[1])
    contraction = sp.csr_matrix((cd, (cr, cc)), shape=(64, DIM_ZETA), dtype=np.int64)
    injection = sp.csr_matrix((jd, (jr, jc)), shape=(DIM_ZETA, 64), dtype=np.int64)
    cj = np.asarray((contraction @ injection).todense()) % prime
    denominator = 8 if MUT == "bad_projector" else 7
    trace = (injection @ contraction).tocsr()
    trace.data = trace.data * pow(denominator, prime - 2, prime) % prime
    remainder = sp.identity(DIM_ZETA, dtype=np.int64, format="csr") - trace
    remainder.data %= prime
    return trace, remainder, cj


def project(left, form, right, prime):
    first = np.asarray(left @ form) % prime
    return np.asarray(right @ first.transpose()).transpose() % prime


def row_basis(matrices, prime):
    width = len(matrices)
    pivots = []
    for index in range(DIM_ZETA * DIM_ZETA):
        row = [int(matrix.flat[index]) % prime for matrix in matrices]
        if not any(row):
            continue
        for column, pivot in pivots:
            if row[column]:
                factor = row[column]
                row = [(x - factor * y) % prime for x, y in zip(row, pivot)]
        if not any(row):
            continue
        column = next(i for i, value in enumerate(row) if value)
        inv = pow(row[column], prime - 2, prime)
        row = [value * inv % prime for value in row]
        pivots.append((column, row))
        if len(pivots) == width:
            break
    return [row for _, row in pivots]


def small_nullspace(rows, width, prime):
    pivots = []
    for raw in rows:
        row = list(raw)
        for column, pivot in pivots:
            if row[column]:
                factor = row[column]
                row = [(x - factor * y) % prime for x, y in zip(row, pivot)]
        if any(row):
            column = next(i for i, value in enumerate(row) if value)
            inv = pow(row[column], prime - 2, prime)
            pivots.append((column, [value * inv % prime for value in row]))
    pivot_columns = {column for column, _ in pivots}
    basis = []
    for free in (i for i in range(width) if i not in pivot_columns):
        vector = [0] * width
        vector[free] = 1
        for column, row in reversed(pivots):
            vector[column] = -sum(
                row[k] * vector[k] for k in range(column + 1, width)
            ) % prime
        basis.append(vector)
    return basis


def combine_basis(basis, coefficients, prime):
    out = {}
    for coefficient, vector in zip(coefficients, basis):
        for column, value in vector.items():
            out[column] = (out.get(column, 0) + coefficient * value) % prime
    return {column: value for column, value in out.items() if value}


def align_channels(pairs, basis, prime):
    trace, remainder, cj = gamma_projectors(prime)
    projected = [[], [], []]
    split_residuals = []
    for vector in basis:
        form = dense_form(pairs, vector, prime)
        trace_block = project(trace, form, trace, prime)
        cross_block = (
            project(trace, form, remainder, prime)
            + project(remainder, form, trace, prime)
        ) % prime
        rs_block = project(remainder, form, remainder, prime)
        split_residuals.append(np.count_nonzero((trace_block + cross_block + rs_block - form) % prime))
        for output, block in zip(projected, (trace_block, cross_block, rs_block)):
            output.append(block)
    block_rows = [row_basis(block, prime) for block in projected]
    aligned = []
    for wanted in range(3):
        constraints = []
        for block_index, rows in enumerate(block_rows):
            if block_index != wanted:
                constraints.extend(rows)
        for coefficients in small_nullspace(constraints, len(basis), prime):
            aligned.append(combine_basis(basis, coefficients, prime))
    return aligned, tuple(len(rows) for rows in block_rows), tuple(split_residuals), cj


def orbit_ranks(pairs, aligned, prime):
    current = [dense_form(pairs, vector, prime) for vector in aligned]
    accumulators = [np.zeros((DIM_ZETA, DIM_ZETA), dtype=np.int64) for _ in aligned]
    steps = 28 if MUT == "short_orbit" else 70
    for step in range(steps):
        coefficient = (17 * step + 3) % prime
        for i in range(len(aligned)):
            accumulators[i] = (accumulators[i] + coefficient * current[i]) % prime
        group = lower_unipotent((3 * step + 1) % 7, (5 * step + 2) % prime)
        group_t = group.transpose().tocsr()
        for i in range(len(aligned)):
            current[i] = np.asarray(group @ current[i] @ group_t) % prime
    if MUT == "drop_l1_rs" and len(accumulators) == 3:
        accumulators[-1].fill(0)
    if MUT == "drop_l5_trace" and len(accumulators) == 4:
        # Remove both channels that touch the 64-dimensional trace summand.
        accumulators[0].fill(0)
        accumulators[1].fill(0)
    individual = tuple(rank_mod(matrix, prime) for matrix in accumulators)
    coefficients = tuple(range(1, len(accumulators) + 1))
    combined = sum(c * matrix for c, matrix in zip(coefficients, accumulators)) % prime
    return individual, rank_mod(combined, prime)


def certify(prime: int):
    facts = {}
    targets = {
        "L1": (2, 0, 0, 0, 0, 0, 0),
        "L5": (2, 2, 2, 2, 2, 0, 0),
    }
    for name, target in targets.items():
        pairs, basis = sparse_nullspace(target, prime)
        aligned, multiplicities, residuals, cj = align_channels(pairs, basis, prime)
        individual, combined = orbit_ranks(pairs, aligned, prime)
        facts[name] = {
            "variables": len(pairs),
            "nullity": len(basis),
            "multiplicities": multiplicities,
            "split_residuals": residuals,
            "cj": cj,
            "ranks": individual,
            "combined": combined,
        }
    if MUT == "bad_l1_mult":
        facts["L1"]["multiplicities"] = (1, 1, 2)
    if MUT == "bad_l5_mult":
        facts["L5"]["multiplicities"] = (1, 1, 1)
    return facts


def run() -> int:
    global CHECKS, FAILS
    CHECKS, FAILS = 0, []
    print("DS1-BR -- exact Lambda1/Lambda5 invariant-form rank census")
    if MUT:
        print(f"MUTATION: {MUT}")

    rsc_sha = hashlib.sha256(RSC1.read_bytes()).hexdigest()
    check("RSC-1 probe SHA is pinned", rsc_sha == RSC1_SHA)
    rsc = subprocess.run(
        [sys.executable, str(RSC1)], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    check("RSC-1 exact decomposition exits 0", rsc.returncode == 0)
    check("RSC-1 clean result is 103/103", "RSC-1: 103/103 checks pass" in rsc.stdout)
    check("RSC-1 supplies L1/L5 RS positive controls",
          "Lambda^2(R^(+)) contains L1 with multiplicity" in rsc.stdout and
          "Lambda^2(R^(+)) contains L5 with multiplicity" in rsc.stdout)

    all_facts = []
    # The clean certificate runs both independent primes.  Each hostile mutant
    # reruns one complete exact field construction; the baseline-first guard
    # has already established the two-prime result before mutations begin.
    active_primes = PRIMES if not MUT else PRIMES[:1]
    for prime in active_primes:
        facts = certify(prime)
        all_facts.append(facts)
        l1, l5 = facts["L1"], facts["L5"]
        check(f"p={prime}: gamma contraction-injection is 7*identity",
              set(int(x) for x in l1["cj"].diagonal()) == {7} and
              np.count_nonzero(l1["cj"] - np.diag(l1["cj"].diagonal())) == 0)
        check(f"p={prime}: all trace/cross/RS projector splits are exact",
              l1["split_residuals"] == (0, 0, 0) and
              l5["split_residuals"] == (0, 0, 0, 0))
        check(f"p={prime}: Lambda1 highest-weight system has 1104 variables and nullity 3",
              (l1["variables"], l1["nullity"]) == (1104, 3))
        check(f"p={prime}: Lambda1 block multiplicities are trace/cross/RS = 1/1/1",
              l1["multiplicities"] == (1, 1, 1))
        check(f"p={prime}: Lambda1 generic pure-channel ranks are 64/128/832",
              l1["ranks"] == (64, 128, 832))
        check(f"p={prime}: one shared Lambda1 direction plus diagonal channels reaches rank 896",
              l1["combined"] == 896)
        check(f"p={prime}: Lambda5 highest-weight system has 141 variables and nullity 4",
              (l5["variables"], l5["nullity"]) == (141, 4))
        check(f"p={prime}: Lambda5 block multiplicities are trace/cross/RS = 1/1/2",
              l5["multiplicities"] == (1, 1, 2))
        check(f"p={prime}: Lambda5 generic pure-channel ranks are 64/128/832/832",
              l5["ranks"] == (64, 128, 832, 832))
        check(f"p={prime}: one shared Lambda5 direction plus diagonal channels reaches rank 896",
              l5["combined"] == 896)

    if not MUT:
        check("both independent primes reproduce the same rank census",
              all_facts[0]["L1"]["ranks"] == all_facts[1]["L1"]["ranks"] and
              all_facts[0]["L5"]["ranks"] == all_facts[1]["L5"]["ranks"])

    result_text = RESULT.read_text(encoding="utf-8")
    register_text = REGISTER.read_text(encoding="utf-8")
    if MUT == "result_marker":
        result_text = result_text.replace("BLIND-ROWS-ADMIT-FULL-RANK-FORMS", "BLIND-ROWS-STAY-OPEN")
    if MUT == "register_marker":
        register_text = register_text.replace("receipt: ds1-br", "receipt: missing")
    check("result records BLIND-ROWS-ADMIT-FULL-RANK-FORMS",
          "BLIND-ROWS-ADMIT-FULL-RANK-FORMS" in result_text)
    check("result rejects a physical mass/gap conclusion",
          "not a physical mass-gap certificate" in result_text)
    check("upgrade item is durably closed with the DS1-BR receipt",
          "id: DS1-BLINDROW-FORM-RANK" in register_text and
          "receipt: ds1-br" in register_text)

    print(f"DS1-BR: {CHECKS - len(FAILS)}/{CHECKS} checks pass; "
          f"{len(FAILS)} failures; exit {1 if FAILS else 0}")
    return 1 if FAILS else 0


MUTATIONS = {
    "bad_raise": "Lambda1 block multiplicities are trace/cross/RS = 1/1/1",
    "bad_projector": "Lambda1 block multiplicities are trace/cross/RS = 1/1/1",
    "bad_l1_mult": "Lambda1 block multiplicities are trace/cross/RS = 1/1/1",
    "bad_l5_mult": "Lambda5 block multiplicities are trace/cross/RS = 1/1/2",
    "short_orbit": "one shared Lambda1 direction plus diagonal channels reaches rank 896",
    "drop_l1_rs": "Lambda1 generic pure-channel ranks are 64/128/832",
    "drop_l5_trace": "one shared Lambda5 direction plus diagonal channels reaches rank 896",
    "result_marker": "result records BLIND-ROWS-ADMIT-FULL-RANK-FORMS",
    "register_marker": "upgrade item is durably closed with the DS1-BR receipt",
}


def selftest() -> int:
    print("SELFTEST: clean baseline FIRST")
    if run() != 0:
        print("BASELINE RED -- mutations are not evidence")
        return 1
    caught = 0
    for mutation, target in MUTATIONS.items():
        env = os.environ.copy()
        env["DS1BR_MUT"] = mutation
        process = subprocess.run(
            [sys.executable, str(Path(__file__).resolve())], cwd=ROOT, env=env,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        ok = process.returncode == 1 and any(
            line.startswith("[FAIL]") and target in line
            for line in process.stdout.splitlines()
        )
        print(f"{'caught' if ok else 'MISSED'}: {mutation} -> {target}")
        caught += int(ok)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} targeted mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else run())
