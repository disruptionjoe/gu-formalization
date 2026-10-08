#!/usr/bin/env python3
"""Hostile mutations for K1488."""
import copy, importlib.util
from pathlib import Path

P = Path(__file__).with_name("k1488_wick_quadratic_krylov_direction.py")
S = importlib.util.spec_from_file_location("k1488", P); M = importlib.util.module_from_spec(S); S.loader.exec_module(M)
mutations = [
    ("claim_id", "K0000"),
    ("quadratic_krylov_direction.notation", "none"),
    ("quadratic_krylov_direction.product_formula", "none"),
    ("quadratic_krylov_direction.orthogonal_residual", "not orthogonal"),
    ("quadratic_krylov_direction.top_chaos_survives", "removed"),
    ("quadratic_krylov_direction.symmetrization_lower_bound", "zero"),
    ("quadratic_krylov_direction.normalized_lower_bound", "zero"),
    ("quadratic_krylov_direction.multiplication_coupling", "zero"),
    ("decision.quadratic_krylov_direction_constructed", False),
    ("decision.eighth_chaos_projection_survives_orthogonalization", False),
    ("decision.eighth_chaos_squared_norm_lower_scale", "0"),
    ("decision.normalized_residual_squared_norm_lower", 0),
    ("decision.uniform_next_krylov_coupling_lower", 0),
    ("decision.ground_energy_lower_bound_proved", True),
    ("decision.protected_status_change", True),
]
for i, (path, value) in enumerate(mutations, 1):
    d = copy.deepcopy(M.D); node = d
    bits = path.split(".")
    for key in bits[:-1]: node = node[key]
    node[bits[-1]] = value
    assert not all(M.validate(d)), path
    print(f"PASS {i:02d}: rejected {path}")
print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")
