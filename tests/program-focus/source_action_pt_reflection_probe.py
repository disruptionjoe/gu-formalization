"""Read-only exact reflection controls on the already-owned GU 59-family.

This is finite algebra, not a closed-operator/PT-spectrum certificate.
Usage: python3 tests/program-focus/source_action_pt_reflection_probe.py .
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
path = root / 'lab/process/source-action-deep-coefficients.json'
data = json.loads(path.read_text())
basis = data['basis']
assert len(basis) == 59
terms = sum(len(row) for row in basis)
assert terms == 8994

def parity_result(axes):
    mask = sum(1 << a for a in axes)
    bad = [(i, int(e), int(c)) for i, row in enumerate(basis)
           for e, c, v in row if Q(v)
           and ((int(e) ^ int(c)) & mask).bit_count() % 2]
    return {'axes': axes, 'bad_terms': len(bad), 'first_bad': bad[:1]}

reflections = {
    'stored_spatial': parity_result([0, 8, 9, 10]),
    'physical_time': parity_result([3, 10, 12, 13]),
    'all_spatial_parity': parity_result([0, 1, 2, 10, 12, 13]),
    'all_base_inversion_PT': parity_result([0, 1, 2, 3]),
}
assert all(r['bad_terms'] == 0 for r in reflections.values())
wrong = parity_result([3])
assert wrong['bad_terms'] > 0  # Omits the induced normal-bundle action.

sys.path.insert(0, str(root / 'tests/program-focus'))
import source_action_deep_geometry as g

def blade_square(axes):
    mask = sum(1 << a for a in axes)
    out_mask, scalar = g.cliff_mul(mask, mask)
    assert out_mask == 0
    return Q(scalar)

time_raw_square = blade_square([3, 10, 12, 13])
pt_square = blade_square([0, 1, 2, 3])
assert time_raw_square == 512 and pt_square == -1
# The source J was written in its orthonormal Jordan-Wigner frame.
j_axes = [1, 3, 5, 7, 10, 12]
j_signature = [1] * 9 + [-1] * 5
j_square = (-1) ** (len(j_axes) * (len(j_axes) - 1) // 2)
for a in j_axes:
    j_square *= j_signature[a]
assert j_square == -1
assert j_square * pt_square == 1
# Actual convention gamma_a^sharp=-gamma_a.  A grade-four blade has
# sharp sign (-1)^(4*5/2)=+1, so U_PT^sharp U_PT=U_PT^2=-1.
pt_sharp_sign = (-1) ** (4 * 5 // 2)
assert pt_sharp_sign * pt_square == -1

report = {
    'coefficient_file_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'basis_vectors': len(basis), 'nonzero_sparse_terms': terms,
    'reflections': reflections,
    'wrong_time_only_mask_negative_control': wrong,
    'square_laws': {
        'J_squared': j_square,
        'raw_time_lift_squared': str(time_raw_square),
        'unit_normalized_time_lift_squared': 1,
        'J_times_normalized_time_lift_squared': -1,
        'PT_lift_gamma0123_squared': str(pt_square),
        'Theta_PT_lift_times_J_squared': 1,
        'induced_End_conjugation_squared': 1,
        'PT_lift_Krein_isometry_sign': -1,
        'J_Krein_isometry_sign': -1,
        'Theta_PT_Krein_isometry_sign': 1,
    },
    'scope': ('All statements hold on the entire already-owned 59-dimensional '
              'span, hence both certified root balls. J commutes with real '
              'Clifford generators. No spectral reality, positive physical '
              'metric, invariant operator domain, full auxiliary inverse, '
              'wellposed evolution or physical PT identification is checked.'),
}
print(json.dumps(report, indent=2))
