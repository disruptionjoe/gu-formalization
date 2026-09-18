#!/usr/bin/env python3
"""K236: exact invariant Cl1/Cl2 star inside the selected I1B normal symbol."""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import runpy
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
K235_PROBE = ROOT / "tests/channel-swings/k235_native_i1b_mixed_grade_fermion_insertion_probe.py"
K235 = ROOT / "lab/process/k235-native-i1b-mixed-grade-fermion-insertion.json"
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
OUT = ROOT / "lab/process/k236-native-i1b-invariant-mixed-grade-symbol.json"


def generate():
    with redirect_stdout(StringIO()) as output:
        data = runpy.run_path(str(K235_PROBE))
    assert "[PASS] K235 independent full 28-basis replay" in output.getvalue()
    matrix, basis = data["euler"], data["basis"]
    o = 14
    spokes = tuple(range(2, 14))
    assert basis[o] == (3, 0, 2)
    assert all(basis[i] == (2, i, 2 | (1 << i)) for i in spokes)
    assert matrix.rank() == 6
    assert [i for i in range(28) if matrix[i, o]] == list(spokes)
    assert all(matrix[i, o] == -1 and matrix[o, i] == 1 for i in spokes)
    assert all([i for i in range(28) if matrix[i, j]] == [o] for j in spokes)
    assert matrix[spokes[0], spokes[-1]] == 0

    odd = sp.eye(28)[:, o]
    collective = sum((sp.eye(28)[:, j] for j in spokes), sp.zeros(28, 1))
    assert matrix * odd == -collective
    assert matrix * collective == 12 * odd
    assert matrix * (sp.eye(28)[:, spokes[0]] - sp.eye(28)[:, spokes[1]]) == sp.zeros(28, 1)
    star = sp.Matrix([[0, 12], [-1, 0]])
    assert star * star == -12 * sp.eye(2)
    assert star.rank() == 2
    assert sp.Matrix.hstack(*(sp.eye(28)[:, j] - sp.eye(28)[:, spokes[0]]
                              for j in spokes[1:])).rank() == 11

    return {
        "schema_version": "1.0", "classification": "SOURCE_NATIVE_ROUTE__LOCAL_SELECTED_SYMBOL_ONLY",
        "input_sha256": {"k235_probe": sha256(K235_PROBE.read_bytes()).hexdigest(),
                         "k235_manifest": sha256(K235.read_bytes()).hexdigest(),
                         "backend": sha256(BACKEND.read_bytes()).hexdigest()},
        "object": "Selected I1B comm/symi/symi flat T=0 formal Euler coefficient at normal dx0 in one 28-dimensional invariant label block",
        "odd_basis": "dx0 tensor gamma1",
        "even_spokes": [f"dx{j} tensor gamma1 gamma{j}" for j in spokes],
        "raw_ordered_cross_per_spoke": ["2", "0"],
        "euler_cross_per_spoke": ["1", "-1"],
        "collective": "E=sum_(j=2)^13 dxj tensor gamma1 gammaj",
        "invariant_actions": ["N(o)=-E", "N(E)=12o"],
        "restricted_matrix_basis_o_E": [[0, 12], [-1, 0]],
        "restricted_square": -12,
        "star_rank": 2,
        "eleven_exact_kernel_differences": [f"e{j}-e2" for j in spokes[1:]],
        "full_label_block_rank": 6,
        "interpretation": "The K235 single spoke is not invariant; the collective two-dimensional star is invariant for this one frozen normal coefficient and has 11 linearly independent even null differences. Formal complex symbol roots are +/- i sqrt(12), not a physical frequency, instability or closed-domain spectrum.",
        "fermion_insertion": "By linearity of the displayed draft-2021 candidate, replace each even E block in K235's all-slot insertion by the sum of its twelve even Clifford-valued one-form blocks. The odd block is unchanged. This is only a formal local operator response, not an action-selected physical fermion mode.",
        "claim_ceiling": "Exact rank-two invariant mixed-grade normal-symbol star inside a rank-six 28-label block and 11 even null differences. No tangential/lower-order invariant subbundle, global domain, propagating or physical spectrum, positive quotient, source/ledger/canon/public change, or K224/K229/K215 signed-region result."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K236 invariant twelve-spoke Cl1/Cl2 normal-symbol star")
