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



def correlated_controls():
    zero = {(i,j):(F(0),F(0)) for i in range(9) for j in range(9-i)}
    tails = {k:F(0) for k in ('t','z','tt','tz','zz')}
    direction = [(2,0,1),(1,1,-16),(0,2,64)]
    box = (F(-1),F(2),F(-2),F(1))
    for name,coeffs,expected in [
        ('mixed quadratic', {(1,1):1}, -16),
        ('rank-one cancellation', {(2,0):64,(1,1):16,(0,2):1}, 0),
        ('positive quadratic', {(2,0):1,(0,2):1},130),
    ]:
        point = dict(zero)
        point.update({key:(F(v),F(v)) for key,v in coeffs.items()})
        assert m.correlated_component(point,zero,box,tails,direction) == (F(expected),F(expected)), name
    # Highest-order Taylor remainder is nonzero although all lower terms at
    # the origin vanish. These analytic t^8 derivatives are independent of
    # the producer's coefficient transform.
    hull = dict(zero);hull[8,0] = (F(1),F(1))
    target = (F(1,2),F(1),F(0),F(1))
    for terms,multiplier,power in [([(2,0,1)],56,6), ([(1,0,1)],8,7)]:
        lo,hi = m.correlated_component(zero,hull,target,tails,terms)
        assert (lo,hi) == (-F(multiplier),F(multiplier))
        for x in (F(1,2),F(3,4),F(1)):
            assert lo <= multiplier*x**power <= hi
    # Independent normalized derivatives of f=(t+2z)^8 on a shifted
    # rectangle exercise mixed terms, a nonzero anchor and a nonzero remainder.
    from math import comb
    anchor = (F(1,4),F(-1,5))
    absolute_box = (F(-1,3),F(2,3),F(-1,2),F(1,4))
    offset = (absolute_box[0]-anchor[0],absolute_box[1]-anchor[0],absolute_box[2]-anchor[1],absolute_box[3]-anchor[1])
    linear = (absolute_box[0]+2*absolute_box[2],absolute_box[1]+2*absolute_box[3])
    point,hull = {},{}
    for i,j in zero:
        power = 8-i-j
        factor = comb(8,i)*comb(8-i,j)*2**j
        value = factor*(anchor[0]+2*anchor[1])**power
        point[i,j] = (value,value)
        endpoints = [x**power for x in linear]
        low = F(0) if power>0 and power%2==0 and linear[0]<=0<=linear[1] else min(endpoints)
        hull[i,j] = (factor*low,factor*max(endpoints))
    for terms,factor,power in [(direction,56*225,6), ([(1,0,1),(0,1,-8)],-120,7)]:
        lo,hi = m.correlated_component(point,hull,offset,tails,terms)
        for t in (absolute_box[0],F(0),absolute_box[1]):
            for z in (absolute_box[2],F(0),absolute_box[3]):
                assert lo <= factor*(t+2*z)**power <= hi
    # A directional tail cannot be canceled with an unknown cross-tail sign.
    errors = dict(tails,t=F(2),z=F(3),tt=F(2),tz=F(3),zz=F(5))
    assert m.correlated_component(zero,zero,box,errors,[(1,0,1),(0,1,-8)]) == (F(-26),F(26))
    assert m.correlated_component(zero,zero,box,errors,direction) == (F(-370),F(370))
    point = dict(zero);point[1,0]=(F(1),F(1))
    assert m.profile_partition(point,zero,(F(0),F(0)),box,tails,F(8))['status']=='gradient_excluded'
    point = dict(zero);point[2,0]=point[0,2]=(F(1),F(1))
    assert m.profile_partition(point,zero,(F(0),F(0)),box,tails,F(8))['status']=='positive_hessian'
    point[0,2]=(F(-1),F(-1))
    assert m.profile_partition(point,zero,(F(0),F(0)),box,tails,F(8),depth=8)['status']=='unresolved'
    try:
        m.correlated_component(zero,zero,box,tails,[(1,0,1),(2,0,1)])
    except ValueError:
        pass
    else:
        raise AssertionError('mixed derivative-order remainder escaped')
    print('PASS correlated controls: three analytic quadratics, two degree-eight remainders, shifted mixed degree-eight control, two tail bounds, three terminal cases, mixed-order rejection')

def main():
    baseline = json.loads(m.ARTIFACT.read_text())
    got = m.compute()
    baseline_checks = m.validate(baseline, got)
    assert all(ok for _, ok in baseline_checks), baseline_checks
    print('PASS clean baseline before all controls and mutations')
    controls()
    correlated_controls()
    rows = baseline['stationary_transport_inputs']
    assert m.vertical_zero_graph(rows)['connected_unique_vertical_zero_graph']
    for label,mutate in [
        ('vertical gap', lambda rs: rs.pop(3)),
        ('lost monotonicity', lambda rs: rs[0]['certificate']['whole_line_hessian'].__setitem__('zz','-1')),
        ('lost top bracket', lambda rs: next(r for r in rs if r['leaf']==40)['certificate']['whole_line_gradient'].__setitem__('z','-1')),
        ('lost first-top monotonicity', lambda rs: next(r for r in rs if r['leaf']==26)['certificate']['whole_line_hessian'].__setitem__('tz','0')),
    ]:
        rs=copy.deepcopy(rows);mutate(rs)
        assert not m.vertical_zero_graph(rs)['connected_unique_vertical_zero_graph'],label
    graph_boxes = []
    for column,zs in enumerate([[-1,0,3,F(7,2)],[-1,0,F(31,10),F(13,4)],[-1,0,F(21,10),F(5,2)],[-2,-1,F(11,10),F(3,2)]]):
        graph_boxes.extend((F(column),F(column+1),F(a),F(b)) for a,b in zip(zs,zs[1:]))
    analytic,_ = fixture(((F(3),F(1)),(F(1),F(1))),(F(2),F(2)),graph_boxes)
    graph = m.vertical_zero_graph(analytic)
    assert graph['connected_unique_vertical_zero_graph']
    assert not graph['stationary_uniqueness_from_geometry_alone']
    # For J=(z+t-4)^2/2 + (t-2)^3/3-(t-2), the same Jz=t+z-4
    # graph has two full-gradient zeros, at t=1 and t=3. Their Schur signs
    # are -2 and +2. Geometry alone must never imply uniqueness.
    for t in (F(1),F(3)):
        z=4-t
        assert z+t-4 == (t-2)**2-1 == 0
    assert [2*(t-2) for t in (F(1),F(3))] == [-2,2]
    print('PASS connected-graph hypotheses: gap, monotonicity and bracket mutations rejected')
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
        ('contradict global certificate', lambda d: d['decision'].__setitem__('global_optimizer_proved', not d['decision']['global_optimizer_proved'])),
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
    if 'correlated_profile_inputs' in baseline:
        import hashlib
        packet=baseline['correlated_profile_inputs'][0]
        for name,mutate in [
            ('missing jet coefficient',lambda p:p['point_jet'].pop('0,0')),
            ('inverted jet interval',lambda p:p['point_jet'].__setitem__('0,0',['1','0'])),
            ('anchor outside remainder hull',lambda p:p.__setitem__('anchor',['0','0'])),
            ('hull outside chart',lambda p:p.__setitem__('hull',['0','1','0','1'])),
            ('omitted leaf input',lambda p:p['leaf_inputs'].pop()),
            ('negative tail radius',lambda p:p['leaf_inputs'][0]['tail_upper'].__setitem__('t','-1')),
            ('wrong root box',lambda p:p['leaf_inputs'][0].__setitem__('box',['0','1','0','1'])),
            ('wrong numerical configuration',lambda p:p.__setitem__('parameter_order',6)),
        ]:
            changed=copy.deepcopy(packet);mutate(changed)
            changed['digest']=hashlib.sha256(json.dumps({k:v for k,v in changed.items() if k!='digest'},sort_keys=True,separators=(',',':')).encode()).hexdigest()
            try:
                m.correlated_profile(changed,profile)
            except (ValueError,KeyError):
                pass
            else:
                raise AssertionError(name)
        for packets in [baseline['correlated_profile_inputs'][:-1],baseline['correlated_profile_inputs']+[packet]]:
            try:
                m.correlated_bundle(packets,profile)
            except ValueError:
                pass
            else:
                raise AssertionError('incomplete/duplicate correlated coverage escaped')
        mutations.extend([
            ('forge correlated input',lambda d:d['correlated_profile_inputs'][0]['point_jet'].__setitem__('0,0',['0','0'])),
            ('forge partition',lambda d:d['certificate']['correlated_profile']['packets'][0]['leaves'][0]['partition'].__setitem__('status','positive_hessian')),
            ('invent global from graph',lambda d:d['certificate']['vertical_zero_graph'].__setitem__('stationary_uniqueness_from_geometry_alone',True)),
        ])
        print('PASS eight rehashed packet faults and two cover faults rejected')
    for name, mutate in mutations:
        changed = copy.deepcopy(baseline)
        mutate(changed)
        failed = [label for label, ok in m.validate(changed, got) if not ok]
        assert failed, name
        print(f'PASS mutation: {name}; failing checks: {failed}')
    print(f'RESULT: PASS analytic controls, graph controls, 38 witness checks, {len(mutations)} rejected reporting mutations')


if __name__ == '__main__':
    main()
