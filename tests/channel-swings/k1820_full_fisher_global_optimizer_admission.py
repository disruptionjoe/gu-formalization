#!/usr/bin/env python3
"""K1820: protected global admission after route calibration."""
import hashlib
import json
import re
from fractions import Fraction as F
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


def compute(transport_rows=None):
    two = load("k1809-full-fisher-slab-two-global-exclusion")
    three = load("k1819-full-fisher-slab-three-boundary-cover")
    if transport_rows is None:
        transport_rows = json.loads(ARTIFACT.read_text())["stationary_transport_inputs"]
    check_transport_inputs(transport_rows)
    local = load("k1787-full-fisher-stationary-krawczyk")["certificate"]
    anchor = tuple(F(local["parameter_box"]["center"][k]) for k in ("t", "z"))
    anchor_gradient = tuple(interval(local["full_gradient_at_center"][k]) for k in ("t", "z"))
    return {
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
    }


def validate(data, got=None):
    got = compute() if got is None else got
    profile = got["stationary_derivative_transport"]
    try:
        check_transport_inputs(data["stationary_transport_inputs"])
        authenticated = True
    except (ValueError, KeyError):
        authenticated = False
    return [
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
        ("transport inputs bound", data["inputs"] == ["K1787", "K1809", "K1816", "K1818", "K1819"]),
        ("embedded transport evidence authenticated", authenticated),
        ("covered transport graph", profile["vertex_count"] == 110 and profile["edge_count"] == 177),
        ("fourteen stationary exclusions", profile["stationary_excluded_leaf_ids"] == [13, 14, 27, 28, 29, 39, 40, 41, 42, 52, 53, 54, 63, 64]),
        ("thirty-eight candidates remain", len(profile["retained_leaf_ids"]) == 38 and 50 in profile["retained_leaf_ids"]),
        ("monotone vertical gradient", profile["positive_tz_on_every_leaf"] and profile["positive_zz_on_every_leaf"]),
        ("exact area contraction", 0 < F(profile["root_feasible_area_fraction"]) < F(14,100)),
        ("polygons do not prove roots", not profile["retained_polygon_proves_existence"]),
        ("transport does not prove uniqueness", not profile["complete_stationary_uniqueness_proved"]),
        ("profile curvature still unresolved", profile["retained_leaves_with_positive_profile_curvature"] == []),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
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
