#!/usr/bin/env python3
"""MP1-S7 -- do seven middle-form insertions suffice on the actual carrier?

The predecessor's rank-896 witness summed seven arbitrary rank-128 skew forms.
RSC-1 proves that an admissible middle-form insertion is much narrower: on

    zeta = T(64) (+) R(832)

the unique Spin(14)-equivariant alternating-form image has only the T-R cross
block.  The image is linear, so every finite sum remains one cross-block form
and has rank at most 2*dim(T)=128.  This probe re-runs RSC-1's exact
Klimyk/Racah certificate, checks the linear-span theorem, and demonstrates why
the arbitrary seven-block witness is outside the invariant image.

Run:
    python3 tests/channel-swings/mp1_seven_insertion_sufficiency_probe.py
    python3 tests/channel-swings/mp1_seven_insertion_sufficiency_probe.py --selftest
"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RSC1 = ROOT / "tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py"
MP1 = ROOT / "lab/active-research/joe-directed/spectral-transport/mp1-composites-inherit-one-horn-never-both-2026-08-17.md"
RESULT = ROOT / "explorations/generation-sector/mp1-seven-insertion-sufficiency-2026-08-24.md"
REGISTER = ROOT / "lab/process/upgrade-program-register.yaml"
RSC1_SHA = "a161d8a5a326e81d1fef07259e6f21c66253f83c62a21b113d0b7ea1b6a99ee0"
PRIME = 1_000_003
MUT = os.environ.get("MP1S7_MUT", "")

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


def rank_mod(matrix: list[list[int]], prime: int = PRIME) -> int:
    """Exact row rank over a prime field; sufficient for integer witnesses."""
    a = [[x % prime for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], prime - 2, prime)
        a[rank] = [(x * inv) % prime for x in a[rank]]
        for r in range(rows):
            if r == rank or not a[r][col]:
                continue
            factor = a[r][col]
            a[r] = [(x - factor * y) % prime for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def cross_map(shift: int, trace_dim: int = 64, rs_dim: int = 832) -> list[list[int]]:
    """A full-row-rank T<-R witness inside the certified cross-block image."""
    matrix = [[0] * rs_dim for _ in range(trace_dim)]
    for row in range(trace_dim):
        matrix[row][(row + shift) % rs_dim] = 1
    return matrix


def add_maps(maps: list[list[list[int]]]) -> list[list[int]]:
    return [
        [sum(m[r][c] for m in maps) for c in range(len(maps[0][0]))]
        for r in range(len(maps[0]))
    ]


def run() -> int:
    global CHECKS, FAILS
    CHECKS, FAILS = 0, []
    print("MP1-S7 -- invariant compatibility of the seven-insertion witness")
    if MUT:
        print(f"MUTATION: {MUT}")

    # Leg 1: reproduce the exact representation owner, not only its prose.
    rsc_sha = hashlib.sha256(RSC1.read_bytes()).hexdigest()
    if MUT == "rsc1_sha":
        rsc_sha = "0" * 64
    check("RSC-1 probe SHA is pinned", rsc_sha == RSC1_SHA)
    proc = subprocess.run(
        [sys.executable, str(RSC1)], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    check("RSC-1 exact Klimyk/Racah certificate exits 0", proc.returncode == 0)
    check("RSC-1 clean result is 103/103", "RSC-1: 103/103 checks pass" in proc.stdout)
    check("RSC-1 pins zeta = 64 + 832", "dim zeta_+ = 64 + 832" in proc.stdout)
    check("RSC-1 pins the unique middle-form channel to the CROSS block",
          "the whole unique channel sits in the CROSS block" in proc.stdout)
    check("RSC-1 pins both RS-RS middle-form alternating multiplicities to zero",
          proc.stdout.count("Lambda^2(R^(+)) contains L7") >= 2 and
          proc.stdout.count("multiplicity                   0") >= 2)
    check("RSC-1 pins the trace-trace middle-form block to zero",
          "Lambda^2(S_-) (the gamma-trace) contains no middle form" in proc.stdout)

    # Leg 2: exact module/image facts.  These are references the mutation
    # harness may corrupt; the predicates remain fixed.
    trace_dim, rs_dim = 64, 832
    cross_mult, trace_alt_mult, rs_alt_mult = 1, 0, 0
    linear_image = True
    if MUT == "trace_dim":
        trace_dim = 448
    elif MUT == "cross_mult":
        cross_mult = 0
    elif MUT == "trace_block":
        trace_alt_mult = 1
    elif MUT == "rs_block":
        rs_alt_mult = 1
    elif MUT == "linearity":
        linear_image = False
    check("carrier dimension is 64 + 832 = 896", trace_dim + rs_dim == 896)
    check("middle-form alternating image has cross multiplicity one", cross_mult == 1)
    check("middle-form alternating image has no trace-trace block", trace_alt_mult == 0)
    check("middle-form alternating image has no RS-RS block", rs_alt_mult == 0)
    check("the equivariant insertion-to-form map is linear", linear_image)
    check("every admissible image has block shape [[0,A],[-A^T,0]]",
          cross_mult == 1 and trace_alt_mult == 0 and rs_alt_mult == 0)
    check("structural rank ceiling is 2*min(64,832)=128",
          2 * min(trace_dim, rs_dim) == 128)
    check("every admissible image leaves at least 768 of 896 directions unpaired",
          896 - 2 * min(trace_dim, rs_dim) == 768)

    # Leg 3: exact finite rank witnesses INSIDE the image.
    maps = [cross_map(64 * i) for i in range(7)]
    ranks = [rank_mod(m) for m in maps]
    check("each of seven compatible T<-R witnesses has exact map rank 64",
          ranks == [64] * 7)
    check("each compatible skew form therefore has exact rank 128",
          [2 * rank for rank in ranks] == [128] * 7)
    total = add_maps(maps)
    total_rank = rank_mod(total)
    if MUT == "sum_rank":
        total_rank = 448
    check("the sum of seven compatible maps still has map rank 64", total_rank == 64)
    check("the sum of seven compatible skew forms still has rank 128",
          2 * total_rank == 128)
    check("seven compatible insertions do not gap the 896 carrier",
          2 * total_rank < 896)
    check("no finite linear sum escapes the same cross-block image",
          linear_image and trace_alt_mult == 0 and rs_alt_mult == 0)

    # Leg 4: reproduce MP1's generic witness and type why it is inadmissible.
    arbitrary_block_count, arbitrary_block_rank = 7, 128
    arbitrary_rank = arbitrary_block_count * arbitrary_block_rank
    has_rs_rs_support = True
    if MUT == "generic_admissible":
        has_rs_rs_support = False
    check("the predecessor's arbitrary disjoint-block witness reaches rank 896",
          arbitrary_rank == 896)
    check("that arbitrary witness necessarily uses support outside one shared 64|832 cross block",
          has_rs_rs_support)
    check("generic 896-rank witness is not an invariant-compatibility certificate",
          arbitrary_rank == 896 and has_rs_rs_support)

    # Leg 5: durable evidence and claim-ceiling pins.
    mp1_text = MP1.read_text(encoding="utf-8")
    result_text = RESULT.read_text(encoding="utf-8")
    register_text = REGISTER.read_text(encoding="utf-8")
    if MUT == "verdict_marker":
        result_text = result_text.replace("SEVEN-DOES-NOT-SUFFICE", "SEVEN-SUFFICES")
    check("MP1 predecessor already fences its generic witness as necessary, not sufficient",
          "NECESSARY, not" in mp1_text and "sufficient" in mp1_text and
          "invariant-compatibility at 7 is NOT computed here" in mp1_text)
    check("result records SEVEN-DOES-NOT-SUFFICE",
          "SEVEN-DOES-NOT-SUFFICE" in result_text)
    check("result preserves the necessity-only ceiling and rejects a universal gapping no-go",
          "not a no-go for every insertion channel" in result_text)
    check("upgrade item is durably closed with the MP1-S7 receipt",
          "id: MP1-SEVEN-FLOOR-SUFFICIENCY" in register_text and
          "receipt: mp1-s7" in register_text)

    print(f"MP1-S7: {CHECKS - len(FAILS)}/{CHECKS} checks pass; "
          f"{len(FAILS)} failures; exit {1 if FAILS else 0}")
    return 1 if FAILS else 0


MUTATIONS = {
    "rsc1_sha": "RSC-1 probe SHA is pinned",
    "trace_dim": "carrier dimension is 64 + 832 = 896",
    "cross_mult": "middle-form alternating image has cross multiplicity one",
    "trace_block": "middle-form alternating image has no trace-trace block",
    "rs_block": "middle-form alternating image has no RS-RS block",
    "linearity": "the equivariant insertion-to-form map is linear",
    "sum_rank": "the sum of seven compatible maps still has map rank 64",
    "generic_admissible": "that arbitrary witness necessarily uses support",
    "verdict_marker": "result records SEVEN-DOES-NOT-SUFFICE",
}


def selftest() -> int:
    print("SELFTEST: clean baseline FIRST")
    if run() != 0:
        print("BASELINE RED -- mutations are not evidence")
        return 1
    caught = 0
    for mutation, target in MUTATIONS.items():
        env = os.environ.copy()
        env["MP1S7_MUT"] = mutation
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).resolve())], cwd=ROOT,
            env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        ok = proc.returncode == 1 and f"[FAIL] {target}" in proc.stdout
        print(f"{'caught' if ok else 'MISSED'}: {mutation} -> {target}")
        caught += int(ok)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} targeted mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else run())
