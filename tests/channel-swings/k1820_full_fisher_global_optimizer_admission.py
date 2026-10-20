#!/usr/bin/env python3
"""K1820: protected global admission after route calibration."""
import hashlib
import json
import re
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1820-full-fisher-global-optimizer-admission.json"


def load(name):
    return json.loads((ROOT / f"lab/process/{name}.json").read_text())


def interval(text):
    """Read a serialized Arb enclosure as outward exact decimal rationals."""
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", text)
    if match:
        midpoint, radius = map(F, match.groups())
        if radius < 0:
            raise ValueError("negative enclosure radius")
        return midpoint - radius, midpoint + radius
    value = F(text)
    return value, value


def intersect(*bounds):
    result = max(b[0] for b in bounds), min(b[1] for b in bounds)
    if result[0] > result[1]:
        raise ValueError("inconsistent certified intervals")
    return result


def inside(point, box):
    return box[0] <= point[0] <= box[1] and box[2] <= point[1] <= box[3]


def corners(box):
    a, b, c, d = box
    return [(a, c), (b, c), (b, d), (a, d)]


def clip(polygon, a, b, c):
    """Intersect a closed convex polygon with a*x+b*y+c >= 0 exactly."""
    if not polygon:
        return []
    result = []
    for p, q in zip(polygon, polygon[1:] + polygon[:1]):
        fp, fq = a*p[0] + b*p[1] + c, a*q[0] + b*q[1] + c
        if fp >= 0:
            result.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            weight = fp / (fp - fq)
            result.append(tuple(p[i] + weight*(q[i]-p[i]) for i in (0, 1)))
    # Keep points and segments: zero area is not evidence of emptiness.
    return list(dict.fromkeys(result))


def area(polygon):
    if not polygon:
        return F(0)
    return abs(sum(p[0]*q[1]-q[0]*p[1]
                   for p, q in zip(polygon, polygon[1:]+polygon[:1]))) / 2


def singular_hessian_witness(tt, tz, zz):
    """Find an exact rank-one matrix in a component interval box, if possible.

    This is an obstruction to certifying every matrix in that box as regular,
    not an assertion that the actual function has a singular Hessian.
    Failure of this sufficient search has no mathematical implication.
    """
    if tz[0] <= 0 or zz[0] <= 0:
        return None
    ratio = sum(tz) / sum(zz)
    lo = max(zz[0], tz[0]/ratio, tt[0]/ratio**2)
    hi = min(zz[1], tz[1]/ratio, tt[1]/ratio**2)
    if lo > hi:
        return None
    scale = (lo+hi)/2
    return {"tt": str(ratio**2*scale), "tz": str(ratio*scale),
            "zz": str(scale), "kernel_vector": ["1", str(-ratio)]}


def transport(rows, anchor, anchor_gradient):
    """Bound gradient potentials on covered edges, then constrain every zero.

    Each edge integrates a certified Hessian component over a segment contained
    in a single closed leaf. At most N-1 sweeps cover every simple path; a final
    check rejects inconsistent negative cycles. No quadrature is performed.
    """
    boxes = [tuple(map(F, row["box"])) for row in rows]
    gradients = [tuple(interval(row["certificate"]["whole_line_gradient"][k])
                       for k in ("t", "z")) for row in rows]
    hessians = []
    for row in rows:
        h = row["certificate"]["whole_line_hessian"]
        tt, tz, zz = [interval(h[k]) for k in ("tt", "tz", "zz")]
        hessians.append(((tt, tz), (tz, zz)))
    xs = sorted({x for box in boxes for x in box[:2]} | {anchor[0]})
    ys = sorted({y for box in boxes for y in box[2:]} | {anchor[1]})
    nodes = [(x, y) for x in xs for y in ys
             if any(inside((x, y), box) for box in boxes)]
    index = {point: i for i, point in enumerate(nodes)}
    if anchor not in index:
        raise ValueError("anchor is outside the certified cover")
    incident = [[i for i, box in enumerate(boxes) if inside(p, box)] for p in nodes]
    bounds = [[intersect(*(gradients[i][axis] for i in members)) for members in incident]
              for axis in (0, 1)]
    for axis in (0, 1):
        i = index[anchor]
        bounds[axis][i] = intersect(bounds[axis][i], anchor_gradient[axis])
    edges = []
    for p in nodes:
        for direction, grid in enumerate((xs, ys)):
            pos = grid.index(p[direction])
            if pos + 1 == len(grid):
                continue
            q = list(p)
            q[direction] = grid[pos + 1]
            q = tuple(q)
            if q not in index:
                continue
            owners = [i for i in incident[index[p]] if inside(q, boxes[i])]
            if not owners:
                continue
            length = q[direction] - p[direction]
            delta = [tuple(v*length for v in intersect(*(hessians[i][axis][direction]
                                                       for i in owners)))
                     for axis in (0, 1)]
            edges.append((index[p], index[q], delta))

    def relax(axis, update):
        changed = False
        for u, v, delta in edges:
            for start, end, step in ((u, v, delta[axis]),
                                     (v, u, (-delta[axis][1], -delta[axis][0]))):
                current = bounds[axis][end]
                source = bounds[axis][start]
                new = intersect(current, (source[0]+step[0], source[1]+step[1]))
                if new != current:
                    changed = True
                    if update:
                        bounds[axis][end] = new
        return changed

    for axis in (0, 1):
        for _ in range(len(nodes)-1):
            if not relax(axis, True):
                break
        if relax(axis, False):
            raise ValueError("inconsistent difference-bound cycle")
    results = []
    for row, box, hessian in zip(rows, boxes, hessians):
        polygon = corners(box)
        # For a corner q and any p in its rectangle, a rectilinear path stays
        # inside that rectangle. Integrate each Hessian bound along its leg.
        for q in corners(box):
            for axis in (0, 1):
                lo, hi = bounds[axis][index[q]]
                low_coeff, high_coeff = [], []
                for direction in (0, 1):
                    hlow, hhigh = hessian[axis][direction]
                    at_lower = q[direction] == box[2*direction]
                    low_coeff.append(hlow if at_lower else hhigh)
                    high_coeff.append(hhigh if at_lower else hlow)
                # A zero must have lower_affine <= 0 <= upper_affine.
                a, b = low_coeff
                polygon = clip(polygon, -a, -b, -lo+a*q[0]+b*q[1])
                a, b = high_coeff
                polygon = clip(polygon, a, b, hi-a*q[0]-b*q[1])
        results.append({"leaf": row["leaf"],
                        "root_feasible_polygon": [[str(v) for v in p] for p in polygon],
                        "stationary_excluded": not polygon})
        if hessian[1][1][0] > 0:
            # Along a local J_z=0 graph, d(J_t)/dt is this Schur complement.
            aa, bb, cc = hessian[0][0], hessian[0][1], hessian[1][1]
            square_min = F(0) if bb[0] <= 0 <= bb[1] else min(v*v for v in bb)
            square_max = max(v*v for v in bb)
            schur = (aa[0]-square_max/cc[0], aa[1]-square_min/cc[1])
            results[-1]["profile_schur_interval"] = list(map(str, schur))
            results[-1]["positive_profile_curvature_certified"] = schur[0] > 0
        results[-1]["component_box_singular_witness"] = singular_hessian_witness(
            hessian[0][0], hessian[0][1], hessian[1][1])
    input_area = sum((b[1]-b[0])*(b[3]-b[2]) for b in boxes)
    retained_area = sum(area([tuple(map(F, p)) for p in r["root_feasible_polygon"]]) for r in results)
    return {"vertex_count": len(nodes), "edge_count": len(edges),
            "candidate_area": str(input_area),
            "root_feasible_area": str(retained_area),
            "root_feasible_area_fraction": str(retained_area/input_area),
            "positive_tz_on_every_leaf": all(h[0][1][0] > 0 for h in hessians),
            "positive_zz_on_every_leaf": all(h[1][1][0] > 0 for h in hessians),
            "leaf_results": results,
            "stationary_excluded_leaf_ids": [r["leaf"] for r in results if r["stationary_excluded"]],
            "retained_leaf_ids": [r["leaf"] for r in results if not r["stationary_excluded"]],
            "retained_leaves_with_positive_profile_curvature": [
                r["leaf"] for r in results
                if not r["stationary_excluded"] and r.get("positive_profile_curvature_certified", False)],
            "retained_leaves_with_component_box_singular_witness": [
                r["leaf"] for r in results
                if not r["stationary_excluded"] and r["component_box_singular_witness"] is not None],
            "singular_witness_is_actual_hessian": False,
            "retained_polygon_proves_existence": False,
            "complete_stationary_uniqueness_proved": False}


def check_transport_inputs(rows):
    """Authenticate full corrected checkpoints against the published bank."""
    stationary = load("k1818-full-fisher-slab-three-stationary-cover")["certificate"]
    value = load("k1816-full-fisher-slab-three-leafwise-score-bank")["certificate"]
    expected_ids = stationary["candidate_leaf_ids"]
    if [r["leaf"] for r in rows] != expected_ids:
        raise ValueError("incomplete or duplicate transport inputs")
    for row in rows:
        payload = dict(row)
        digest = payload.pop("checkpoint_digest")
        actual = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        native = value["leaves"][row["leaf"]]
        if actual != digest or digest != stationary["checkpoint_digests"][str(row["leaf"])]:
            raise ValueError("transport input checkpoint digest mismatch")
        if row["box"] != native["box"] or row["input_k1816_checkpoint_digest"] != native["checkpoint_digest"]:
            raise ValueError("transport input box or provenance mismatch")
        if row["input_partition_digest"] != value["input_partition_digest"]:
            raise ValueError("transport input partition mismatch")


def iadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def imul(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def iscale(c, a):
    return imul((c, c), a)


def bernstein_interval(coefficients, box, degree):
    """Exact rational interval replay of a power polynomial on a rectangle."""
    a,b,c,d = box
    unit = {}
    for (i,j), value in coefficients.items():
        for k in range(i+1):
            for ell in range(j+1):
                weight = comb(i,k)*a**(i-k)*(b-a)**k*comb(j,ell)*c**(j-ell)*(d-c)**ell
                unit[k,ell] = iadd(unit.get((k,ell),(F(0),F(0))), iscale(weight,value))
    controls = []
    for i in range(degree+1):
        for j in range(degree+1):
            value = (F(0),F(0))
            for k in range(i+1):
                for ell in range(j+1):
                    weight = F(comb(i,k)*comb(j,ell),comb(degree,k)*comb(degree,ell))
                    value = iadd(value,iscale(weight,unit.get((k,ell),(F(0),F(0)))))
            controls.append(value)
    return min(v[0] for v in controls), max(v[1] for v in controls)


def correlated_component(point, hull_jet, offset_box, tails, terms):
    """A constant linear combination of equal-order derivatives, before ranging.

    The degree-six integral remainder has a common segment and kernel for
    every second derivative. Combine its coefficients before taking absolute
    values; the jet must enclose the entire anchor-to-target hull.
    """
    orders = {at+az for at,az,_ in terms}
    if len(orders) != 1 or next(iter(orders)) not in (1,2):
        raise ValueError('correlated terms must have one derivative order')
    remainder_degree = 8-next(iter(orders))
    polynomial = {}
    remainder = F(0)
    dx,dy = max(map(abs,offset_box[:2])),max(map(abs,offset_box[2:]))
    for i in range(remainder_degree+1):
        for j in range(remainder_degree+1-i):
            source = point if i+j < remainder_degree else hull_jet
            value = (F(0),F(0))
            for at,az,weight in terms:
                factor = F(weight)*F(factorial(i+at),factorial(i))*F(factorial(j+az),factorial(j))
                value = iadd(value,iscale(factor,source[i+at,j+az]))
            if i+j < remainder_degree:
                polynomial[i,j] = value
            else:
                remainder += max(map(abs,value))*dx**i*dy**j
    tail_keys = {(2,0):'tt',(1,1):'tz',(0,2):'zz',(1,0):'t',(0,1):'z'}
    remainder += sum(abs(F(w))*tails[tail_keys[at,az]] for at,az,w in terms)
    lo,hi = bernstein_interval(polynomial,offset_box,remainder_degree-1)
    return lo-remainder,hi+remainder


def correlated_profile(inputs, profile):
    """Replay a frozen whole-line profile certificate using only rationals."""
    payload = {k:v for k,v in inputs.items() if k != 'digest'}
    if hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest() != inputs['digest']:
        raise ValueError('correlated input digest mismatch')
    if inputs['parameter_order'] != 8 or inputs['observation_order'] != 14 or inputs['cell_half_width'] != '1/4':
        raise ValueError('correlated quadrature configuration mismatch')
    anchor = tuple(map(F,inputs['anchor']))
    if len(anchor) != 2:
        raise ValueError('correlated anchor dimension mismatch')
    required = {(i,j) for i in range(9) for j in range(9-i)}
    def jet(values):
        result = {tuple(map(int,k.split(','))):tuple(map(F,v)) for k,v in values.items()}
        if set(result) != required or any(len(v)!=2 or v[0]>v[1] for v in result.values()):
            raise ValueError('incomplete or malformed correlated jet')
        return result
    point = jet(inputs['point_jet'])
    hull = tuple(map(F,inputs['hull']))
    if len(hull) != 4 or not (0<hull[0]<=hull[1]<1 and 0<hull[2]<=hull[3]<1 and 2*hull[0]**2>F(1,1024)):
        raise ValueError('correlated hull outside positive-density chart')
    if not inside(anchor,hull):
        raise ValueError('correlated remainder hull omits anchor')
    hull_jet = jet(inputs['hull_jet'])
    expected = [row for row in profile['leaf_results'] if not row['stationary_excluded']
                and row['leaf'] in inputs['leaf_ids']]
    if not expected or [row['leaf'] for row in expected] != inputs['leaf_ids']:
        raise ValueError('correlated requested leaf IDs invalid')
    if [row['leaf'] for row in inputs['leaf_inputs']] != [row['leaf'] for row in expected]:
        raise ValueError('correlated profile coverage mismatch')
    ratio = F(inputs['direction_ratio'])
    output = []
    for data, feasible in zip(inputs['leaf_inputs'],expected):
        polygon = [tuple(map(F,p)) for p in feasible['root_feasible_polygon']]
        box = (min(p[0] for p in polygon),max(p[0] for p in polygon),min(p[1] for p in polygon),max(p[1] for p in polygon))
        if tuple(map(F,data['box'])) != box or not all(inside(p,hull) for p in corners(box)):
            raise ValueError('correlated box/hull mismatch')
        tails = {k:F(v) for k,v in data['tail_upper'].items()}
        if set(tails) != {'t','z','tt','tz','zz'} or min(tails.values()) < 0:
            raise ValueError('correlated tails invalid')
        offset = (box[0]-anchor[0],box[1]-anchor[0],box[2]-anchor[1],box[3]-anchor[1])
        a = correlated_component(point,hull_jet,offset,tails,[(2,0,1),(1,1,-2*ratio),(0,2,ratio**2)])
        b = correlated_component(point,hull_jet,offset,tails,[(1,1,1),(0,2,-ratio)])
        c = correlated_component(point,hull_jet,offset,tails,[(0,2,1)])
        square = (F(0) if b[0]<=0<=b[1] else min(x*x for x in b),max(x*x for x in b))
        determinant = iadd(imul(a,c),(-square[1],-square[0]))
        output.append({'leaf':data['leaf'],'transformed_hessian':{k:list(map(str,v)) for k,v in [('a',a),('b',b),('c',c),('determinant',determinant)]},
                       'positive_definite_on_root_box':a[0]>0 and determinant[0]>0})
        output[-1]['partition'] = profile_partition(point,hull_jet,anchor,box,tails,ratio)
    return {'input_digest':inputs['digest'],'leaves':output,
            'positive_leaf_ids':[r['leaf'] for r in output if r['positive_definite_on_root_box']],
            'positive_definite_on_all_root_boxes':all(r['positive_definite_on_root_box'] for r in output),
            'global_uniqueness_proved':False,'source_owned_physics':False}


def profile_partition(point, hull, anchor, box, tails, ratio, depth=0):
    """Closed-box binary cover: gradient exclusion or positive Hessian.

    The depth bound limits this particular replay, never grants a theorem.
    Unresolved nodes stay explicit. Children share their splitting boundary.
    Original-box tail errors and the full packet remainder hull remain valid
    for every child; no new numerical integral is evaluated here.
    """
    offset = (box[0]-anchor[0],box[1]-anchor[0],box[2]-anchor[1],box[3]-anchor[1])
    def bound(terms):
        return correlated_component(point,hull,offset,tails,terms)
    for label,terms in [('t',[(1,0,1)]),('z',[(0,1,1)]),
                        ('t_minus_r_z',[(1,0,1),(0,1,-ratio)])]:
        lo,hi = bound(terms)
        if lo>0 or hi<0:
            return {'status':'gradient_excluded','axis':label,'bound':list(map(str,(lo,hi)))}
    a = bound([(2,0,1),(1,1,-2*ratio),(0,2,ratio**2)])
    b = bound([(1,1,1),(0,2,-ratio)])
    c = bound([(0,2,1)])
    square = (F(0) if b[0]<=0<=b[1] else min(x*x for x in b),max(x*x for x in b))
    det = iadd(imul(a,c),(-square[1],-square[0]))
    if a[0]>0 and det[0]>0:
        return {'status':'positive_hessian','a_lower':str(a[0]),'det_lower':str(det[0])}
    if depth == 8:
        return {'status':'unresolved'}
    axis = 0 if 8*(box[1]-box[0]) >= box[3]-box[2] else 2
    middle = (box[axis]+box[axis+1])/2
    left,right = list(box),list(box)
    left[axis+1] = right[axis] = middle
    return {'status':'split','axis':axis,'children':[
        profile_partition(point,hull,anchor,tuple(child),tails,ratio,depth+1)
        for child in (left,right)]}


def partition_counts(node):
    if node['status'] == 'split':
        result = {'gradient_excluded':0,'positive_hessian':0,'unresolved':0}
        for child in node['children']:
            for key,value in partition_counts(child).items():
                result[key] += value
        return result
    return {key:int(node['status']==key) for key in ('gradient_excluded','positive_hessian','unresolved')}



def correlated_bundle(inputs, profile):
    expected = profile['retained_leaf_ids']
    coverage = [leaf for packet in inputs for leaf in packet['leaf_ids']]
    if sorted(coverage) != expected or len(set(coverage)) != len(coverage):
        raise ValueError('correlated packets do not partition retained leaves')
    packets = [correlated_profile(packet,profile) for packet in inputs]
    counts = {'gradient_excluded':0,'positive_hessian':0,'unresolved':0}
    excluded,covered = [],[]
    for packet in packets:
        for leaf in packet['leaves']:
            local = partition_counts(leaf['partition'])
            for key,value in local.items():
                counts[key] += value
            if local['positive_hessian'] == local['unresolved'] == 0:
                excluded.append(leaf['leaf'])
            if local['unresolved'] == 0:
                covered.append(leaf['leaf'])
    return {'packets':packets,'terminal_counts':counts,
            'additional_stationary_excluded_leaf_ids':sorted(excluded),
            'stationary_positive_hessian_covered_leaf_ids':sorted(covered),
            'positive_hessian_at_every_remaining_stationary_point':counts['unresolved']==0,
            'global_uniqueness_proved':False,'source_owned_physics':False}


def vertical_zero_graph(rows):
    """Check the geometry/sign hypotheses of the connected J_z-zero graph.

    Each closed column is a contiguous vertical stack with J_zz,J_tz>0.
    Bottoms have J_z<0; all tops except the first have J_z>0. The first
    top's J_z increases strictly in t, so its zero-existence set is an
    interval. Adjacent stacks share a vertical overlap whose bottom/top
    have opposite signs, giving the same unique zero at every join.
    """
    columns = {}
    for row in rows:
        box = tuple(map(F,row['box']))
        columns.setdefault(box[:2],[]).append((box,row))
    ordered = sorted(columns.items())
    checks,records = [],[]
    for n,(ts,stack) in enumerate(ordered):
        stack.sort(key=lambda item:item[0][2])
        checks.append(all(a[0][3]==b[0][2] for a,b in zip(stack,stack[1:])))
        checks.append(all(interval(row['certificate']['whole_line_hessian'][key])[0]>0
                          for _,row in stack for key in ('tz','zz')))
        bottom,top = stack[0],stack[-1]
        low = interval(bottom[1]['certificate']['whole_line_gradient']['z'])
        high = interval(top[1]['certificate']['whole_line_gradient']['z'])
        checks.append(low[1]<0)
        if n:
            checks.append(high[0]>0)
        records.append({'t':list(map(str,ts)), 'z':[str(bottom[0][2]),str(top[0][3])],
                        'bottom_leaf':bottom[1]['leaf'],'top_leaf':top[1]['leaf'],
                        'bottom_gradient':list(map(str,low)),'top_gradient':list(map(str,high))})
    joins = []
    for left,right in zip(records,records[1:]):
        checks.append(F(left['t'][1])==F(right['t'][0]))
        lower = max((left,right),key=lambda r:F(r['z'][0]))
        upper = min((left,right),key=lambda r:F(r['z'][1]))
        overlap = (F(lower['z'][0]),F(upper['z'][1]))
        signs = F(lower['bottom_gradient'][1])<0 and F(upper['top_gradient'][0])>0
        checks.append(overlap[0]<overlap[1] and signs)
        joins.append({'t':left['t'][1],'overlap':list(map(str,overlap)),
                      'negative_bottom_leaf':lower['bottom_leaf'],'positive_top_leaf':upper['top_leaf']})
    return {'columns':records,'joins':joins,
            'connected_unique_vertical_zero_graph':len(records)>=2 and all(checks),
            'stationary_uniqueness_from_geometry_alone':False}


def optimizer_admission(result, rows, local, boundary):
    """Compose the single convex root box with the accepted sublevel cover.

    All other candidate boxes exclude gradients. On the remaining convex
    rectangle a positive Hessian makes the gradient strictly monotone, hence
    injective. K1787 supplies existence. A minimum on the compact retained
    union exists, cannot lie on its value-excluded boundary, and must be this
    stationary point. The accepted outer cover excludes every other point of
    the same fixed-q two-radius chart above the comparison threshold.
    """
    correlated = result['correlated_profile']
    remaining = sorted(set(result['stationary_derivative_transport']['retained_leaf_ids'])
                       -set(correlated['additional_stationary_excluded_leaf_ids']))
    by_leaf = {leaf['leaf']:leaf for packet in correlated['packets'] for leaf in packet['leaves']}
    root_box = []
    for key in ('t','z'):
        center,radius = (F(local['parameter_box'][name][key]) for name in ('center','radius'))
        root_box.extend((center-radius,center+radius))
    original = next(tuple(map(F,row['box'])) for row in rows if row['leaf']==50)
    existence = all(local['strict_inclusion'].values()) and all(inside(p,original) for p in corners(root_box))
    one_convex_box = remaining == [50] and by_leaf[50]['positive_definite_on_root_box']
    unique = existence and one_convex_box and correlated['terminal_counts']['unresolved']==0
    threshold = F(boundary['whole_line_value_threshold'])
    value_upper = interval(local['stationary_value_enclosure'])[1]
    outer = load('k1769-degree-seven-survivor-refinement')
    strip = load('k1777-full-fisher-boundary-exclusion')
    first = load('k1792-full-fisher-slab-one-global-kkt')
    collars = load('k1760-two-radius-collar-admission')
    incumbent = load('k1763-hermite-degree-escalation')
    outer_threshold = F(outer['refinement']['threshold'])
    value_ids = boundary['whole_line_value_certified_leaf_ids']
    total_cover = sorted(value_ids+[row['leaf'] for row in rows]) == list(range(78))
    hypotheses = {
        'unique_stationary_point_in_candidate_union':unique,
        'local_stationary_value_below_threshold':value_upper<threshold,
        'threshold_below_outer_pruning_threshold':threshold<outer_threshold,
        'outer_threshold_matches_slab_one':outer_threshold==F(first['certificate']['threshold']),
        'boundary_collars_complete':collars['residual_domain']['q']=='1/1024' and all(collars['decision'][key] for key in ('zero_noise_collar_completed','joint_rare_zero_corner_completed','quantitative_rare_atom_collar_completed','compact_residual_rectangle_frozen')),
        'local_value_below_collar_incumbent':value_upper<interval(incumbent['certificate']['candidate_compact'])[0],
        'complete_candidate_and_value_partition':total_cover,
        'lower_boundary_strip_excluded':strip['decision']['both_boundary_cells_excluded'] and strip['certificate']['q']=='1/1024' and interval(strip['certificate']['residual_gap_lower'])[0]>0,
        'outer_refinement_complete':outer['refinement']['unresolved_leaves']==0 and outer['decision']['survivor_union_is_replayable'],
        'first_two_slabs_excluded':result['slab_one_excluded'] and result['slab_two_excluded'],
        'retained_union_boundary_value_excluded':result['slab_three_complete_boundary_cover'],
    }
    return {'hypotheses':hypotheses,'remaining_stationary_leaf_ids':remaining,
            'stationary_value_upper':str(value_upper),'comparison_threshold':str(threshold),
            'strict_threshold_slack':str(threshold-value_upper),
            'unique_global_minimizer_in_fixed_q_two_radius_chart':all(hypotheses.values()),
            'unique_stationary_point_on_entire_slab':False,
            'unrestricted_channel_optimizer':False,'source_owned_physics':False}

def compute(transport_rows=None):
    two = load("k1809-full-fisher-slab-two-global-exclusion")
    three = load("k1819-full-fisher-slab-three-boundary-cover")
    if transport_rows is None:
        transport_rows = json.loads(ARTIFACT.read_text())["stationary_transport_inputs"]
    check_transport_inputs(transport_rows)
    local = load("k1787-full-fisher-stationary-krawczyk")["certificate"]
    anchor = tuple(F(local["parameter_box"]["center"][k]) for k in ("t", "z"))
    anchor_gradient = tuple(interval(local["full_gradient_at_center"][k]) for k in ("t", "z"))
    result = {
        "slab_one_excluded": two["certificate"]["slab_one_already_excluded"],
        "slab_two_excluded": two["decision"]["slab_two_complete_sublevel_excluded"],
        "slab_three_retained_leaves": three["certificate"]["retained_slab_three_leaves"],
        "slab_three_compact_value_certified_leaves": len(three["certificate"]["compact_value_certified_leaf_ids"]),
        "slab_three_stationary_rejected_leaves": len(three["certificate"]["whole_line_stationary_rejected_leaf_ids"]),
        "slab_three_stationary_retained_leaves": len(three["certificate"]["whole_line_stationary_retained_leaf_ids"]),
        "slab_three_complete_stationary_cover": three["decision"]["complete_stationary_uniqueness_proved"],
        "slab_three_complete_boundary_cover": three["decision"]["all_slab_three_faces_and_vertices_certified"],
        "slab_three_whole_line_value_certified_leaves": len(three["certificate"]["whole_line_value_certified_leaf_ids"]),
        "slab_three_certified_boundary_faces": three["certificate"]["certified_exposed_atomic_faces"],
        "slab_three_certified_boundary_vertices": three["certificate"]["certified_exposed_boundary_vertices"],
        "stationary_derivative_transport": transport(transport_rows, anchor, anchor_gradient),
        "vertical_zero_graph": vertical_zero_graph(transport_rows),
    }
    if ARTIFACT.exists():
        correlated = json.loads(ARTIFACT.read_text()).get('correlated_profile_inputs')
        if correlated is not None:
            result['correlated_profile'] = correlated_bundle(correlated,result['stationary_derivative_transport'])
            result['optimizer_admission'] = optimizer_admission(result,transport_rows,local,three['certificate'])
    return result


def validate(data, got=None):
    got = compute() if got is None else got
    profile = got["stationary_derivative_transport"]
    try:
        check_transport_inputs(data["stationary_transport_inputs"])
        authenticated = True
    except (ValueError, KeyError):
        authenticated = False
    correlated_authenticated = True
    if 'correlated_profile' in got:
        try:
            packets = data['correlated_profile_inputs']
            hashes = [hashlib.sha256(json.dumps({k:v for k,v in p.items() if k!='digest'},sort_keys=True,separators=(',',':')).encode()).hexdigest() for p in packets]
            correlated_authenticated = hashes == [p['digest'] for p in packets] == [p['input_digest'] for p in got['correlated_profile']['packets']]
        except (KeyError,TypeError):
            correlated_authenticated = False
    return [
        ("correlated packets authenticated", correlated_authenticated),
        ("connected vertical zero graph", got['vertical_zero_graph']['connected_unique_vertical_zero_graph']),
        ("graph alone does not prove stationary uniqueness", not got['vertical_zero_graph']['stationary_uniqueness_from_geometry_alone']),
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1820"),
        ("exact replay", data["certificate"] == got),
        ("two slabs closed", got["slab_one_excluded"] and got["slab_two_excluded"]),
        ("26 value leaves certified", got["slab_three_compact_value_certified_leaves"] == 26),
        ("saved stationary bank partition", got["slab_three_stationary_rejected_leaves"] >= 13
         and got["slab_three_stationary_rejected_leaves"] + got["slab_three_stationary_retained_leaves"] == 52),
        ("whole-line value transfer", got["slab_three_whole_line_value_certified_leaves"] == 26),
        ("boundary closed", got["slab_three_complete_boundary_cover"] and got["slab_three_certified_boundary_faces"] == got["slab_three_certified_boundary_vertices"] == 114),
        ("stationary uniqueness remains open", not got["slab_three_complete_stationary_cover"]),
        ("transport inputs bound", data["inputs"] == ["K1760", "K1763", "K1769", "K1777", "K1787", "K1792", "K1809", "K1816", "K1818", "K1819"]),
        ("embedded transport evidence authenticated", authenticated),
        ("covered transport graph", profile["vertex_count"] == 110 and profile["edge_count"] == 177),
        ("fourteen stationary exclusions", profile["stationary_excluded_leaf_ids"] == [13, 14, 27, 28, 29, 39, 40, 41, 42, 52, 53, 54, 63, 64]),
        ("thirty-eight candidates remain", len(profile["retained_leaf_ids"]) == 38 and 50 in profile["retained_leaf_ids"]),
        ("monotone vertical gradient", profile["positive_tz_on_every_leaf"] and profile["positive_zz_on_every_leaf"]),
        ("exact area contraction", 0 < F(profile["root_feasible_area_fraction"]) < F(14,100)),
        ("polygons do not prove roots", not profile["retained_polygon_proves_existence"]),
        ("transport does not prove uniqueness", not profile["complete_stationary_uniqueness_proved"]),
        ("profile curvature still unresolved", profile["retained_leaves_with_positive_profile_curvature"] == []),
        ("component boxes cannot certify uniform regularity", profile["retained_leaves_with_component_box_singular_witness"] == profile["retained_leaf_ids"]),
        ("no actual singularity inferred", not profile["singular_witness_is_actual_hessian"]),
        ("global decision follows complete certificate", data["decision"]["global_optimizer_proved"] == got.get('optimizer_admission',{}).get('unique_global_minimizer_in_fixed_q_two_radius_chart',False)),
        ("global scope remains fixed-q two-radius", not got.get('optimizer_admission',{}).get('unrestricted_channel_optimizer',False)),
        ("physical withheld", not data["decision"]["source_owned_physical_theory"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2)); return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
