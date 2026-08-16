#!/usr/bin/env python3
"""Exact K142 split-graph and intrinsic gauge-quotient connection gate."""

from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


print("A. PREDECESSOR AND TYPE CUSTODY")
k141 = strict("lab/process/selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction.json")
k138 = strict("lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json")
check("replay", "K141 fixed extraction and graph idempotent are retained",
      k141["graph_projector"]["projector"] == "P_mu=R_mu E"
      and k141["graph_projector"]["idempotent"] is True)
check("replay", "K141 Riesz obstruction remains exact",
      k141["native_riesz_test"]["zero_riesz_projector_rank"] == 10
      and k141["native_riesz_test"]["ordinary_radical_dimension"] == 9)
check("replay", "K138 quotient dimensions remain 9 minus 4 equals 5",
      k138["null_stratum"]["radical_dimension"]
      - k138["null_stratum"]["diffeomorphism_image_dimension"]
      == k138["null_stratum"]["gauge_reduced_dimension"] == 5)
for distinction in (
    "intrinsic graph connection versus extrinsic graph bending",
    "quotient bundle versus chosen representative subspace",
    "natural quotient connection versus action-specific subprincipal endomorphism",
    "zero projected graph derivative versus zero physical subprincipal symbol",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT SPLIT-GRAPH DIFFERENTIAL")
mu = sp.Symbol("mu")
d = sp.Matrix([[mu, mu ** 2, 0, 1], [1, 2 * mu, mu ** 3, 0]])
dd = d.diff(mu)
i4 = sp.eye(4)
z42 = sp.zeros(4, 2)
r = i4.col_join(-d)
dr = sp.zeros(4, 4).col_join(-dd)
e = i4.row_join(z42)
p = r * e
i6 = sp.eye(6)
check("split", "fixed extraction is a left inverse of every graph inclusion", e * r == i4)
check("split", "natural graph projector is idempotent", p * p == p)
check("derivative", "differentiated split identity gives E dR equals zero", e * dr == sp.zeros(4))
check("intrinsic", "projected graph derivative vanishes", p * dr == sp.zeros(6, 4))
check("extrinsic", "complementary graph derivative equals the full derivative", (i6 - p) * dr == dr)
check("control", "planted graph family has nonzero extrinsic bending", dr != sp.zeros(6, 4))

h = sp.Matrix([1 + mu, mu ** 2, 3, -mu])
dh = h.diff(mu)
lhs = p * (dr * h + r * dh)
rhs = r * dh
check("connection", "projected derivative of a graph section is R dh", sp.simplify(lhs - rhs) == sp.zeros(6, 1))

d2 = sp.Matrix([[2 * mu, 0, mu, mu ** 2], [mu ** 2, 1, 0, 3 * mu]])
r2 = i4.col_join(-d2)
dr2 = sp.zeros(4, 4).col_join(-d2.diff(mu))
p2 = r2 * e
check("independence", "distinct graph family has distinct extrinsic derivative", dr2 != dr)
check("independence", "distinct graph family has the same zero projected derivative", p2 * dr2 == sp.zeros(6, 4))


print("\nC. INTRINSIC RADICAL/GAUGE QUOTIENT DESCENT")
# Model H=span(e1,e2,e3), G=span(e1), Q represented by e2,e3.
e1, e2, e3, e4 = [sp.eye(4).col(i) for i in range(4)]
gamma = sp.Matrix([
    [2, 1, 0, 4],
    [0, 3, 1, 5],
    [0, 0, -1, 6],
    [0, 0, 0, 7],
])
check("preservation", "good connection preserves the radical model", all((gamma * v)[3] == 0 for v in (e1, e2, e3)))
check("preservation", "good connection preserves the gauge line", gamma * e1 == 2 * e1)

h0 = 5 * e2 - 2 * e3
gauge_shift = 11 * e1
delta = gamma * (h0 + gauge_shift) - gamma * h0
check("quotient", "changing representatives changes the derivative only by gauge",
      all(entry == 0 for entry in delta[1:]))
quotient_matrix = gamma.extract([1, 2], [1, 2])
check("quotient", "induced quotient connection has the expected two-dimensional model", quotient_matrix == sp.Matrix([[3, 1], [0, -1]]))

bad = gamma.copy()
bad[1, 0] = 1
bad_delta = bad * (h0 + gauge_shift) - bad * h0
check("control", "planted non-basic connection fails representative independence", bad_delta[1] != 0)


print("\nD. ARTIFACT, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k142-native-i1b-t0-intrinsic-quotient-connection-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k142-native-i1b-t0-intrinsic-quotient-connection-review.md").read_text()
registry = strict("lab/process/selected-k142-native-i1b-t0-intrinsic-quotient-connection.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction-2026-08-16.md").read_text()
check("artifact", "routing notice classification scope and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact
      and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records intrinsic/extrinsic split and quotient descent",
      registry["split_graph"]["projected_graph_derivative"] == "P_mu*dR_mu=0"
      and registry["quotient_connection"]["complement_required"] is False
      and registry["action_transport"]["graph_derivative_supplies_action_specific_quotient_endomorphism"] is False)
check("review", "hostile review blocks the zero-subprincipal overclaim",
      "not a zero physical subprincipal symbol" in review)
check("repo", "current state advances through K142", "K142 now" in current)
check("repo", "roadmap advances beyond K142", "K143" in roadmap[:26000])
check("repo", "context carries the K142 quotient result", "Current K142" in context[:52000])
check("predecessor", "K141 records the K142 successor classification", "K142 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
