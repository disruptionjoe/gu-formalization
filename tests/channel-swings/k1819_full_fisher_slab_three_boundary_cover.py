#!/usr/bin/env python3
"""K1819: transfer compact Cauchy witnesses onto closed slab-three faces.

For C=[-11,11], H=1_C h0 belongs to L2(rho) and requires no derivatives.
With A_C=<s,H> and B_C=||H||², full J=||s||² >= A_C²/B_C.
Thus K1816's uniform positive A_C²-T B_C bounds hold on closed box faces
without estimating the tails of the different, untruncated witness h0.
"""
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1819-full-fisher-slab-three-boundary-cover.json"
THRESHOLD = F(7958932265249, 50000000000000000000)
ANCHOR = {"t": "265664669701527/5000000000000000", "z": "8805034043103/15625000000000"}


def load(name):
    return json.loads((ROOT / f"lab/process/{name}.json").read_text())


def interval_lower(text):
    """Read a serialized Arb decimal enclosure using exact rational arithmetic."""
    match = re.fullmatch(r"\[([^ ]+) \+/- ([^ ]+)\]", text)
    if not match:
        raise ValueError("expected a finite midpoint +/- radius enclosure")
    midpoint, radius = map(F, match.groups())
    if radius < 0:
        raise ValueError("negative interval radius")
    return midpoint - radius


def value_evidence(rows, partition):
    evidence = {}
    if [row["leaf"] for row in rows] != list(range(78)):
        raise ValueError("incomplete slab-three value bank")
    for row in rows:
        payload = dict(row)
        digest = payload.pop("checkpoint_digest")
        if sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest() != digest:
            raise ValueError("K1816 checkpoint digest mismatch")
        cert = row["certificate"]
        bounds = cert["compact_bounds"]
        box = [str(F(value)) for value in row["box"]]
        rectangle = cert["rectangle"]["t"] + cert["rectangle"]["z"]
        if (row["input_partition_digest"] != partition or box != rectangle
                or F(cert["threshold"]) != THRESHOLD or cert["window"] != "[-11,11]"
                or cert["anchor"] != ANCHOR):
            raise ValueError("K1816 witness provenance mismatch")
        ta, tb, za, zb = map(F, box)
        if not (0 < ta < tb < 1 and 0 < za < zb < 1 and 2*ta*ta > F(1, 1024)):
            raise ValueError("K1816 box outside positive-density chart")
        positive = interval_lower(bounds["cross_margin_lower"]) > 0
        if positive != row["decision"]["compact_cross_margin_positive"]:
            raise ValueError("K1816 margin decision mismatch")
        if positive:
            if interval_lower(bounds["a_lower"]) <= 0 or interval_lower(bounds["b_upper"]) <= 0:
                raise ValueError("K1816 nonzero witness not certified")
            evidence[row["leaf"]] = {
                "checkpoint_digest": digest,
                "compact_cross_margin_lower": bounds["cross_margin_lower"],
            }
    return evidence


def boundary_rows(boxes, value_ids):
    """Split collinear edges at exact endpoints and retain incidence-one faces."""
    groups = defaultdict(list)
    for leaf, (ta, tb, za, zb) in boxes.items():
        if not ta < tb or not za < zb:
            raise ValueError("degenerate parameter box")
        for key, interval in ((("v", ta), (za, zb)), (("v", tb), (za, zb)),
                              (("h", za), (ta, tb)), (("h", zb), (ta, tb))):
            groups[key].append((*interval, leaf))
    faces = []
    for (axis, fixed), intervals in sorted(groups.items()):
        points = sorted({p for lo, hi, _ in intervals for p in (lo, hi)})
        for lo, hi in zip(points, points[1:]):
            owners = sorted(leaf for a, b, leaf in intervals if a <= lo and hi <= b)
            if len(owners) == 1:
                faces.append((axis, fixed, lo, hi, owners[0]))
    vertices = sorted({(fixed, p) if axis == "v" else (p, fixed)
                       for axis, fixed, lo, hi, _ in faces for p in (lo, hi)})

    def containing(t, z):
        return [leaf for leaf in sorted(value_ids)
                if boxes[leaf][0] <= t <= boxes[leaf][1]
                and boxes[leaf][2] <= z <= boxes[leaf][3]]

    face_rows = []
    for axis, fixed, lo, hi, owner in faces:
        ends = ((fixed, lo), (fixed, hi)) if axis == "v" else ((lo, fixed), (hi, fixed))
        witnesses = sorted(set(containing(*ends[0])) & set(containing(*ends[1])))
        face_rows.append({"face": [axis, str(fixed), str(lo), str(hi)],
                          "incident_leaf": owner, "value_witness_leaves": witnesses})
    vertex_rows = [{"vertex": [str(t), str(z)], "value_witness_leaves": containing(t, z)}
                   for t, z in vertices]
    return face_rows, vertex_rows


def close_boundary(faces, vertices, boxes, topology, first, second):
    """Compose accepted finite closed partitions; do not rerun their numerics.

    D=P union R, P a finite union of closed pruned boxes, R the retained
    closed union. For p in boundary(R) intersect interior(D), a sequence
    in D minus R tends to p. Its points lie in P, so closedness gives p in P.
    Original-domain boundary points require a separate direct witness.
    """
    one, two = first["partition"], second["enclosure"]
    if not (one["input_topology_digest"] == topology["topology_digest"]
            and two["input_partition_digest"] == one["partition_digest"]
            and one["unresolved_leaves"] == 0
            and one["terminal_leaves"] == one["pruned_leaves"] + one["retained_leaves"]
            and two["terminal_leaves"] == two["pruned_leaves"] + two["retained_leaves"]
            and two["input_retained_leaves"] == one["retained_leaves"]
            and first["decision"]["complete_adaptive_partition_emitted"]
            and first["decision"]["every_pruned_leaf_has_positive_bernstein_lower_bound"]
            and second["decision"]["strict_retained_area_contraction"]
            and F(one["threshold"]) == F(two["threshold"]) > THRESHOLD):
        raise ValueError("incomplete or mismatched strict partition chain")
    slab = topology["slabs"][2]
    ta, tb = map(F, slab["t"])
    za, zb = map(F, slab["z"])
    if not all(ta <= a < b <= tb and za <= c < d <= zb for a, b, c, d in boxes.values()):
        raise ValueError("retained box outside original slab-three domain")

    def interior(point):
        t, z = point
        return ta < t < tb and za < z < zb

    for row in faces:
        axis, fixed, lo, hi = row["face"]
        fixed, lo, hi = map(F, (fixed, lo, hi))
        ends = ((fixed, lo), (fixed, hi)) if axis == "v" else ((lo, fixed), (hi, fixed))
        row["closure"] = ("compact_support_value" if row["value_witness_leaves"]
                          else "finite_closed_pruned_cover" if all(map(interior, ends))
                          else "open")
    for row in vertices:
        row["closure"] = ("compact_support_value" if row["value_witness_leaves"]
                          else "finite_closed_pruned_cover" if interior(tuple(map(F, row["vertex"])))
                          else "open")
    return {
        "original_slab_three_domain": {"t": slab["t"], "z": slab["z"]},
        "input_topology_digest": topology["topology_digest"],
        "first_partition_digest": one["partition_digest"],
        "second_partition_digest": two["partition_digest"],
        "strict_pruning_threshold": two["threshold"],
        "threshold_slack": str(F(two["threshold"]) - THRESHOLD),
        "proof": "boundary(R) intersect interior(D) is contained in P when D=P union R and P is finite closed",
        "evidence_kind": "composition of accepted K1791/K1796 finite closed strict partitions; numerical predicates reused",
    }


def compute():
    atlas = load("k1804-full-fisher-deduplicated-boundary-atlas")
    cover = load("k1818-full-fisher-slab-three-stationary-cover")
    certificate = cover["certificate"]
    bank = load("k1816-full-fisher-slab-three-leafwise-score-bank")["certificate"]
    partition = atlas["certificate"]["input_partition_digest"]
    evidence = value_evidence(bank["leaves"], partition)
    boxes = {row["leaf"]: tuple(map(F, row["box"])) for row in bank["leaves"]}
    faces, vertices = boundary_rows(boxes, evidence)
    topology = load("k1771-interior-survivor-topology")["topology"]
    first = load("k1791-full-fisher-three-slab-tail-cover")
    second = load("k1796-full-fisher-retained-box-enclosure-bank")
    if second["enclosure"]["partition_digest"] != partition:
        raise ValueError("boundary and pruning partition mismatch")
    closure = close_boundary(faces, vertices, boxes, topology, first, second)
    value_certified = sorted(evidence)
    if certificate["candidate_leaf_ids"] != [i for i in range(78) if i not in evidence]:
        raise ValueError("value and stationary bank candidate mismatch")
    return {
        "input_partition_digest": atlas["certificate"]["input_partition_digest"],
        "retained_slab_three_leaves": atlas["certificate"]["by_slab"]["3"],
        "compact_value_certified_leaf_ids": value_certified,
        "whole_line_stationary_rejected_leaf_ids": certificate.get("stationary_rejected_leaf_ids", []),
        "whole_line_stationary_retained_leaf_ids": certificate.get(
            "stationary_retained_leaf_ids", certificate["candidate_leaf_ids"]
        ),
        "whole_line_value_certified_leaf_ids": value_certified,
        "whole_line_value_threshold": str(THRESHOLD),
        "value_transfer": "J_full >= A_C^2/B_C for H=1_[-11,11]*h_K1787; no derivative of H",
        "value_evidence": {str(i): evidence[i] for i in value_certified},
        "closed_partition_composition": closure,
        "ancestor_two_slab_atlas_counts": {
            "faces": atlas["certificate"]["exposed_atomic_faces"],
            "vertices": atlas["certificate"]["exposed_boundary_vertices"],
        },
        "boundary_scope": "boundary of the 78 closed slab-three retained boxes only",
        "exposed_atomic_faces": len(faces),
        "exposed_boundary_vertices": len(vertices),
        "direct_value_certified_faces": sum(bool(row["value_witness_leaves"]) for row in faces),
        "direct_value_certified_vertices": sum(bool(row["value_witness_leaves"]) for row in vertices),
        "certified_exposed_atomic_faces": sum(row["closure"] != "open" for row in faces),
        "certified_exposed_boundary_vertices": sum(row["closure"] != "open" for row in vertices),
        "faces": faces,
        "vertices": vertices,
    }


def validate(data, got=None):
    got = compute() if got is None else got
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1819"),
        ("exact replay", data["certificate"] == got),
        ("78 leaves", got["retained_slab_three_leaves"] == 78),
        ("ancestor atlas scope", got["ancestor_two_slab_atlas_counts"] == {"faces": 122, "vertices": 122}),
        ("slab-three boundary census", got["exposed_atomic_faces"] == 114 and got["exposed_boundary_vertices"] == 114),
        ("26 value leaves", len(got["compact_value_certified_leaf_ids"]) == 26),
        ("compact support transfer", got["whole_line_value_certified_leaf_ids"] == got["compact_value_certified_leaf_ids"]),
        ("stationary partition preserved", sorted(got["whole_line_stationary_rejected_leaf_ids"] + got["whole_line_stationary_retained_leaf_ids"]) == list(range(13, 65))),
        ("direct boundary inheritance", got["direct_value_certified_faces"] == 45 and got["direct_value_certified_vertices"] == 47),
        ("strict pruning threshold", F(got["closed_partition_composition"]["threshold_slack"]) == F(1, 50000000000000000000)),
        ("complete boundary composition", got["certified_exposed_atomic_faces"] == 114 and got["certified_exposed_boundary_vertices"] == 114),
        ("boundary certified", data["decision"]["all_slab_three_faces_and_vertices_certified"]),
        ("stationary uniqueness open", not data["decision"]["complete_stationary_uniqueness_proved"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
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
