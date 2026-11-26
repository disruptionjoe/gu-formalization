"""Narrow exact curvature receiver for the two already-certified roots.

Root/integrator owns execution. No root search, inverse, new action or background.
Usage: python3 tests/program-focus/source_action_datum_boundary_probe.py REPO
"""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


def run(repo):
    repo = Path(repo)
    sys.path.insert(0, str(repo / 'tests/program-focus'))
    import source_action_deep_geometry as geo

    data = json.loads((repo / 'lab/process/source-action-deep-coefficients.json').read_text())
    i, j, receiver = 5, 8, 3
    assert i >= 4 and j >= 4
    assert geo.spin[i] == geo.spin[j] == {}
    assert geo.mbracket(i, j) == {}
    background = geo.curvature_spin(i, j).get(receiver, Q(0))
    assert background == -1
    # T_i(x) and T_j(x) in the published 59-coordinate basis.
    slots = [{}, {}]
    for n, basis in enumerate(data['basis']):
        for ext, cliff, value in basis:
            for slot, axis in zip(slots, (i, j)):
                if ext == 1 << axis:
                    slot.setdefault(cliff, {})[n] = Q(value)

    def factors(c):
        partner = c ^ receiver
        mask, ab = geo.cliff_mul(c, partner)
        mask2, ba = geo.cliff_mul(partner, c)
        assert mask == mask2 == receiver
        return partner, ab - ba

    terms = []
    for c, left in sorted(slots[0].items()):
        partner, coefficient = factors(c)
        if coefficient and partner in slots[1]:
            terms.append((left, slots[1][partner], coefficient))

    reports = []
    for root in data['certified_roots']:
        x = list(map(Q, root['coordinates']))
        radius = Q(root['certificate']['radius'])
        assert radius > 0
        value, error = background, Q(0)
        for left, right, coefficient in terms:
            a = sum(v * x[n] for n, v in left.items())
            b = sum(v * x[n] for n, v in right.items())
            da = radius * sum(map(abs, left.values()))
            db = radius * sum(map(abs, right.values()))
            value += coefficient * a * b
            error += abs(coefficient) * (abs(a) * db + abs(b) * da + da * db)
        lo, hi = value - error, value + error
        nonzero = lo > 0 or hi < 0
        reports.append({
            'root': root['id'], 'center_exact': str(value),
            'error_bound_exact': str(error), 'lower_exact': str(lo),
            'upper_exact': str(hi), 'center_display': float(value),
            'error_display': float(error), 'nonzero': nonzero,
            'sign': 'positive' if lo > 0 else ('negative' if hi < 0 else 'undetermined'),
        })
    assert all(x['nonzero'] for x in reports), 'endpoint curvature interval includes zero'
    return {
        'basis_dimension': len(data['basis']),
        'vertical_axes': [i, j], 'clifford_receiver': receiver,
        'reference_receiver': str(background), 'nonzero_product_terms': len(terms),
        'D_B_T_receiver_identically_zero': True,
        'formula': 'F_Ahat(5,8)[3]=F_B(5,8)[3]+[T_5,T_8][3]',
        'roots': reports,
        'ceiling': 'Actual root curvature at a vertical tangent two-plane of the original coordinate sphere horizontal pole; nonzero rejects matching flat Bott boundary, not all charged stationary backgrounds.',
    }


if __name__ == '__main__':
    print(json.dumps(run(sys.argv[1]), indent=2))
