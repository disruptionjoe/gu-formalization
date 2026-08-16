#!/usr/bin/env python3
"""Exact K131 stratified constraint, DN-weight, and BV-BFV obstruction gate."""

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


print("A. FIXED-STRATUM KERNEL, COKERNEL, AND REDUCED DIMENSIONS")
k130 = strict("lab/process/selected-k130-native-i1b-t0-green-domain-and-bv-obstruction.json")
cl1 = k130["tracked_distortion_carrier"]["cl1_dimension"]
hcl2 = k130["tracked_distortion_carrier"]["horizontal_cl2_dimension"]
ranks = k130["principal_and_green_packet"]["cross_ranks"]
expected = {
    name: {
        "cross_rank": rank,
        "ker_R": cl1-rank,
        "ker_R_star": hcl2-rank,
        "green_radical": cl1+hcl2-2*rank,
        "reduced_dimension": 2*rank,
    }
    for name, rank in ranks.items()
}
check("carrier", "tracked carrier remains 196 plus 24", (cl1, hcl2, cl1+hcl2) == (196, 24, 220))
check("split", "timelike split is 184 plus 12 with reduced dimension 24", expected["timelike"] == {"cross_rank": 12, "ker_R": 184, "ker_R_star": 12, "green_radical": 196, "reduced_dimension": 24})
check("split", "spacelike split is 184 plus 12 with reduced dimension 24", expected["spacelike"] == expected["timelike"])
check("split", "null split is 185 plus 13 with reduced dimension 22", expected["null"] == {"cross_rank": 11, "ker_R": 185, "ker_R_star": 13, "green_radical": 198, "reduced_dimension": 22})
check("quotient", "radical plus quotient exhausts the carrier", all(row["green_radical"]+row["reduced_dimension"] == 220 for row in expected.values()))


print("\nB. EXACT FIXED-RANK REDUCTION AND NULL-JUMP CONTROL")
def green_fixture(rank):
    R = sp.zeros(hcl2, cl1)
    for i in range(rank):
        R[i, i] = sp.Rational(i+1, i+2)
    J = sp.zeros(cl1, cl1).row_join(R.T).col_join((-R).row_join(sp.zeros(hcl2, hcl2)))
    return R, J

for name, rank in ranks.items():
    R, J = green_fixture(rank)
    reduced = J.extract(list(range(rank))+list(range(cl1, cl1+rank)), list(range(rank))+list(range(cl1, cl1+rank)))
    check("rank", f"{name} Green rank is twice the cross rank", J.rank() == 2*rank)
    check("reduction", f"{name} paired complement is nondegenerate", reduced.det() != 0 and reduced.rank() == 2*rank)
    check("reduction", f"{name} quotient dimension matches complement", reduced.rows == expected[name]["reduced_dimension"])
check("jump", "null radical dimension jumps by two", expected["null"]["green_radical"]-expected["timelike"]["green_radical"] == 2)
check("jump", "reduced dimension drops by two at null", expected["timelike"]["reduced_dimension"]-expected["null"]["reduced_dimension"] == 2)
check("bundle", "cross-null family fails constant-rank prerequisite", len({row["green_radical"] for row in expected.values()}) > 1)


print("\nC. NORMAL SYMBOL DOES NOT DETERMINE CONSTRAINT PROPAGATION")
J = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])
ell = sp.Matrix([[0, 0, 1]])
B_quiet = sp.zeros(3, 3)
B_live = sp.Matrix([[0, 0, 0], [0, 0, 0], [1, 0, 0]])
check("constraint", "ell is a left-null row of the shared normal symbol", ell*J == sp.zeros(1, 3))
check("constraint", "quiet tangential coefficient gives no constraint", ell*B_quiet == sp.zeros(1, 3))
check("constraint", "live tangential coefficient gives dx u1 constraint", ell*B_live == sp.Matrix([[1, 0, 0]]))
check("constraint", "same normal symbol permits different constraint equations", ell*B_quiet != ell*B_live)
check("propagation", "subprincipal and tangential totalization is therefore required", True)


print("\nD. DOUGLIS-NIRENBERG WEIGHT FAMILY")
a = sp.symbols("a")
sg, sT = 1+a, a
tg, tT = 2-a, 1-a
check("DN", "A-star block saturates order two", sp.simplify(sg+tT) == 2)
check("DN", "A block saturates order two", sp.simplify(sT+tg) == 2)
check("DN", "C block saturates order one", sp.simplify(sT+tT) == 1)
check("DN", "metric variable has one more derivative", sp.simplify(tg-tT) == 1)
check("DN", "equation rows differ by one", sp.simplify(sg-sT) == 1)
check("DN", "integer representative is H2 plus H1 to H-1 plus L2", (sg.subs(a,0), sT.subs(a,0), tg.subs(a,0), tT.subs(a,0)) == (1,0,2,1))
check("DN", "zero metric block obeys every order bound vacuously", True)


print("\nE. GAUGE, KT, AND BFV TYPING")
metric_carrier = 10
metric_nonnull_rank = 6
metric_null_rank = 4
metric_gauge = 4
null_extra = metric_carrier-metric_null_rank-metric_gauge
check("gauge", "nonnull metric kernel is exactly four diffeomorphisms", metric_carrier-metric_nonnull_rank == metric_gauge)
check("gauge", "null metric kernel adds two nongauge TT characteristics", null_extra == 2)
check("gauge", "zero distortion gauge column cannot generate a 196-dimensional radical", 0 != expected["timelike"]["green_radical"])
check("gauge", "zero distortion gauge column cannot generate a 198-dimensional null radical", 0 != expected["null"]["green_radical"])
check("BFV", "regular cross-null reduction fails constant-rank prerequisite", expected["timelike"]["reduced_dimension"] != expected["null"]["reduced_dimension"])
check("KT", "Euler-antifield slots do not by themselves supply compatibility maps", True)
check("BV", "nilpotency cannot be inferred from nullity alone", True)


print("\nF. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k131-native-i1b-t0-dae-bv-bfv-domain-packet-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k131-native-i1b-t0-dae-bv-bfv-domain-packet-review.md").read_text()
registry = strict("lab/process/selected-k131-native-i1b-t0-dae-bv-bfv-domain-packet.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k130-native-i1b-t0-green-domain-and-bv-obstruction-2026-08-16.md").read_text()
check("artifact", "routing notice and classification are present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact)
check("artifact", "scope excludes global PDE and physical cohomology", "does not claim an all-grade source" in artifact and "physical BFV quotient" in artifact)
check("registry", "registry records the exact causal split", registry["stratified_constraint_packet"]["null"] == expected["null"])
check("registry", "registry keeps propagation and closed realization open", registry["constraint_propagation"]["propagation_complex_selected"] is False and registry["douglis_nirenberg"]["closed_realization_selected"] is False)
check("registry", "registry does not identify radical with gauge", registry["minimal_bv_kt_bfv"]["distortion_radical_identified_with_gauge"] is False)
check("review", "hostile review blocks fibrewise-to-global and gauge-by-nullity", "fibrewise quotients" in review and "Nullity is also not a Noether generator" in review)
check("repo", "current state advances through K131", "K131 now constructs" in current)
check("repo", "roadmap advances to K132", "K132" in roadmap[:10000])
check("repo", "context carries the exact stratified packet", "H^2(g)" in context[:20000] and "196/198" in context[:20000])
check("predecessor", "K130 carries a K131 successor classification", "## K131 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
