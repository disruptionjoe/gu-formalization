#!/usr/bin/env python3
"""Exact polynomial controls and hostile inputs for K1820 derivative transport."""
import copy
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'tests/channel-swings/k1820_full_fisher_global_optimizer_admission.py'
spec = importlib.util.spec_from_file_location('k1820_probe_base', P)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def text_bound(values):
    lo, hi = min(values), max(values)
    return f'[{(lo+hi)/2} +/- {(hi-lo)/2}]'


def fixture(hessian, root, boxes):
    def gradient(p):
        return tuple(sum(hessian[i][j]*(p[j]-root[j]) for j in (0, 1)) for i in (0, 1))
    rows = []
    for i, box in enumerate(boxes):
        values = [gradient(p) for p in m.corners(box)]
        rows.append({'leaf': i, 'box': list(map(str, box)), 'certificate': {
            'whole_line_gradient': {axis: text_bound([v[j] for v in values])
                                    for j, axis in enumerate(('t', 'z'))},
            'whole_line_hessian': {'tt': str(hessian[0][0]), 'tz': str(hessian[0][1]),
                                  'zz': str(hessian[1][1])}}})
    return rows, gradient


def controls():
    boxes = [(F(a, 2), F(a+1, 2), F(b, 2), F(b+1, 2)) for a in (0, 1) for b in (0, 1)]
    for name, h, root in [
        ('positive Hessian with nonzero anchor gradient', ((F(4), F(1)), (F(1), F(6))), (F(1,4), F(3,4))),
        ('saddle with negative derivative', ((F(2), F(0)), (F(0), F(-2))), (F(1,4), F(3,4))),
        ('root on all shared boundaries', ((F(4), F(-1)), (F(-1), F(2))), (F(1,2), F(1,2))),
        ('root outside covered domain', ((F(4), F(-1)), (F(-1), F(2))), (F(2), F(3))),
    ]:
        rows, grad = fixture(h, root, boxes)
        anchor = (F(0), F(0))
        result = m.transport(rows, anchor, tuple((v, v) for v in grad(anchor)))
        for box, row in zip(boxes, result['leaf_results']):
            polygon = [tuple(map(F, p)) for p in row['root_feasible_polygon']]
            expected = [root] if m.inside(root, box) else []
            assert polygon == expected, (name, row)
            assert row['stationary_excluded'] == (not expected), name
        print('PASS exact quadratic:', name)

    square = m.corners((F(0), F(1), F(0), F(1)))
    line = m.clip(square, F(1), F(0), F(-1))
    point = m.clip(line, F(0), F(1), F(-1))
    assert line and m.area(line) == 0 and point == [(F(1), F(1))]
    assert m.clip(point, F(1), F(0), F(-2)) == []
    print('PASS exact clipping: lines and points survive; disjoint halfplane empties')

    boxes_with_gap = [(F(0), F(1), F(0), F(1)), (F(2), F(3), F(0), F(1))]
    rows, _ = fixture(((F(0), F(0)), (F(0), F(0))), (F(0), F(0)), boxes_with_gap)
    for i, row in enumerate(rows):
        row['certificate']['whole_line_gradient'] = {'t': str(1-2*i), 'z': '0'}
    result = m.transport(rows, (F(0), F(0)), ((F(1), F(1)), (F(0), F(0))))
    assert result['vertex_count'] == 8 and result['edge_count'] == 8
    assert result['stationary_excluded_leaf_ids'] == [0, 1]
    print('PASS domain gap: endpoint coverage alone creates no edge')

    rows, grad = fixture(((F(4), F(1)), (F(1), F(6))), (F(1,4), F(3,4)), boxes)
    rows[0]['certificate']['whole_line_hessian']['tt'] = '-4'
    try:
        m.transport(rows, (F(0), F(0)), tuple((v, v) for v in grad((F(0), F(0)))))
    except ValueError as exc:
        assert 'inconsistent' in str(exc)
    else:
        raise AssertionError('inconsistent derivative plant escaped')
    print('PASS semantic inconsistency: wrong derivative raises explicit rejection')

    # Analytic controls: rank-one [[4,2],[2,1]], strictly positive definite
    # [[4,1],[1,1]], and the indefinite [[1,2],[2,1]] are distinct cases.
    for entries, expected in [((4,2,1), True), ((4,1,1), False), ((1,2,1), False)]:
        bounds = tuple((F(v),F(v)) for v in entries)
        witness = m.singular_hessian_witness(*bounds)
        assert (witness is not None) == expected
    print('PASS three exact rank-one/positive/indefinite witness controls')


def main():
    baseline = json.loads(m.ARTIFACT.read_text())
    got = m.compute()
    baseline_checks = m.validate(baseline, got)
    assert all(ok for _, ok in baseline_checks), baseline_checks
    print('PASS clean baseline before all controls and mutations')
    controls()
    # Verify the published witness independently by multiplication, interval
    # membership, and determinant, without invoking the construction routine.
    source = {r['leaf']: r for r in baseline['stationary_transport_inputs']}
    profile = baseline['certificate']['stationary_derivative_transport']
    for result in profile['leaf_results']:
        if result['stationary_excluded']:
            continue
        witness = result['component_box_singular_witness']
        a,b,c = (F(witness[k]) for k in ('tt','tz','zz'))
        x,y = map(F,witness['kernel_vector'])
        assert (x,y) != (0,0) and a*x+b*y == b*x+c*y == a*c-b*b == 0
        for key,value in zip(('tt','tz','zz'),(a,b,c)):
            lo,hi = m.interval(source[result['leaf']]['certificate']['whole_line_hessian'][key])
            assert lo <= value <= hi
    print('PASS independent exact multiplication of all 38 singular-box witnesses')
    mutations = [
        ('invent complete slab three', lambda d: d['certificate'].__setitem__('slab_three_complete_stationary_cover', True)),
        ('invent global', lambda d: d['decision'].__setitem__('global_optimizer_proved', True)),
        ('invent physics', lambda d: d['decision'].__setitem__('source_owned_physical_theory', True)),
        ('erase an admissible polygon', lambda d: d['certificate']['stationary_derivative_transport']['leaf_results'][2].__setitem__('root_feasible_polygon', [])),
        ('invent polygon existence', lambda d: d['certificate']['stationary_derivative_transport'].__setitem__('retained_polygon_proves_existence', True)),
        ('falsify area', lambda d: d['certificate']['stationary_derivative_transport'].__setitem__('root_feasible_area_fraction', '0')),
        ('change saved Hessian', lambda d: d['stationary_transport_inputs'][0]['certificate']['whole_line_hessian'].__setitem__('zz', '1')),
        ('omit checkpoint', lambda d: d['stationary_transport_inputs'].pop()),
        ('duplicate checkpoint', lambda d: d['stationary_transport_inputs'].append(d['stationary_transport_inputs'][0])),
        ('infer actual singularity', lambda d: d['certificate']['stationary_derivative_transport'].__setitem__('singular_witness_is_actual_hessian', True)),
        ('forge singular witness', lambda d: d['certificate']['stationary_derivative_transport']['leaf_results'][2]['component_box_singular_witness'].__setitem__('tt','0')),
    ]
    for name, mutate in mutations:
        changed = copy.deepcopy(baseline)
        mutate(changed)
        failed = [label for label, ok in m.validate(changed, got) if not ok]
        assert failed, name
        print(f'PASS mutation: {name}; failing checks: {failed}')
    print('RESULT: PASS clean baseline, 10 exact/semantic controls, 38 witness checks, 11 rejected mutations')


if __name__ == '__main__':
    main()
