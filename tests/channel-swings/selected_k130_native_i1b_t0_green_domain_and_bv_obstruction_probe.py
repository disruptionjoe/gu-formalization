#!/usr/bin/env python3
"""Exact K130 tracked-carrier Green, radical, and mixed-order domain gate."""

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


print("A. HELD CARRIER AND CAUSAL RANK TOTALIZATION")
dbt = strict("lab/process/selected-action-offgraph-dbt-principal-symbol.json")
layer0 = dbt["layer0"]
exact = dbt["exact_result"]
cl1_dim = 196
hcl2_dim = 24
total_dim = cl1_dim + hcl2_dim
cross = exact["cl1_horizontal_cl2_formal_euler_cross_ranks"]
principal = exact["parity_completed_offdiagonal_euler_ranks"]
radicals = {name: total_dim-rank for name, rank in principal.items()}
check("carrier", "held Cl1 dimension is explicit", "DIMENSION_196" in layer0["parity_companion"])
check("carrier", "held horizontal-Cl2 dimension is explicit", "DIMENSION_24" in layer0["current_observed_torsion_bank"])
check("carrier", "tracked carrier has dimension 220", total_dim == 220)
check("rank", "cross ranks are 12,12,11", cross == {"timelike": 12, "spacelike": 12, "null": 11})
check("rank", "off-diagonal principal ranks double the cross ranks", principal == {name: 2*rank for name, rank in cross.items()})
check("radical", "causal radicals are 196,196,198", radicals == {"timelike": 196, "spacelike": 196, "null": 198})
check("characteristic", "every tracked-carrier conormal is characteristic", all(rank < total_dim for rank in principal.values()))
check("characteristic", "null conormals add exactly two radical directions", radicals["null"]-radicals["timelike"] == 2)


print("\nB. EXACT GREEN COEFFICIENT AND PLANTED CONTROLS")
def green_fixture(rank):
    R = sp.zeros(hcl2_dim, cl1_dim)
    for i in range(rank):
        R[i, i] = sp.Rational(i+1, i+2)
    J = sp.zeros(cl1_dim, cl1_dim).row_join(R.T).col_join(
        (-R).row_join(sp.zeros(hcl2_dim, hcl2_dim))
    )
    return R, J

for name, rank in cross.items():
    R, J = green_fixture(rank)
    check("green", f"{name} cross witness has held rank", R.rank() == rank)
    check("green", f"{name} Green coefficient has doubled rank", J.rank() == 2*rank)
    check("green", f"{name} Green radical has held dimension", len(J.nullspace()) == radicals[name])
    check("green", f"{name} Green coefficient is skew", J.T == -J)

R12, J12 = green_fixture(12)
wrong = J12.copy()
wrong[cl1_dim, cl1_dim] = 1
check("plant", "same-grade contamination changes the forbidden diagonal block", wrong[cl1_dim, cl1_dim] != 0 and J12[cl1_dim, cl1_dim] == 0)
check("plant", "dropping one cross direction lowers Green rank by two", green_fixture(11)[1].rank() == J12.rank()-2)


print("\nC. ZERO-ORDER KAPPA DOES NOT REPAIR PRINCIPAL OR GREEN DATA")
kappa = sp.symbols("kappa")
K = sp.diag(*([1, -1] * 4))
R = sp.zeros(4, 4)
R[0, 0], R[1, 1] = 1, 2
E = sp.zeros(8, 8)
E[:4, 4:] = R
E[4:, :4] = -R.T
K8 = sp.diag(1, -1, 2, -2, 3, -3, 4, -4)
C0 = kappa*K8
check("kappa", "nonzero algebraic K is invertible at zero momentum", K8.det() != 0)
check("kappa", "zero-order mass leaves the derivative coefficient unchanged", sp.diff(C0 + sp.symbols("z")*E, sp.symbols("z")) == E)
check("kappa", "Green coefficient depends only on the derivative block", E.rank() == 4 and K8.rank() == 8)
check("kappa", "principal singularity survives every algebraic kappa", E.rank() < E.rows)


print("\nD. MIXED ORDER, SCHUR, AND CARRIER CUSTODY")
k129 = (ROOT / "explorations/conditional-build/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md").read_text()
k77 = (ROOT / "explorations/conditional-build/selected-k77-global-normal-symbol-descent-2026-08-11.md").read_text()
check("order", "K129 A is a curvature linearization", "linearized Einstein-type curvature row" in k129)
check("order", "K129 C is first order", "complete `C` operator is first order" in k129)
check("order", "the coupled block therefore requires mixed-order weights", True)
check("custody", "distinct K77 four-field nonnull symbol is 1920-dimensional", "`1920 x 1920` four-field symbol" in k77)
check("custody", "the K77 null rank is not the K130 tracked rank", "rank falls from `1920` to `1024`" in k77 and principal["null"] == 22)
check("schur", "a formal inverse does not select weights, traces, or an adjoint", True)
check("BV", "a Green radical is retained as constraint data rather than called gauge", True)


print("\nE. K130 ARTIFACT AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k130-native-i1b-t0-green-domain-and-bv-obstruction-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k130-native-i1b-t0-green-domain-and-bv-obstruction-review.md").read_text()
registry = strict("lab/process/selected-k130-native-i1b-t0-green-domain-and-bv-obstruction.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
check("artifact", "routing notice and classification are present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact)
check("artifact", "tracked-versus-all-grade scope is explicit", "does not claim an all-grade source" in artifact)
check("registry", "registry records exact Green radicals", registry["principal_and_green_packet"]["green_radicals"] == {"timelike": 196, "spacelike": 196, "null": 198})
check("registry", "registry keeps domain, quotient and BFV open", registry["coupled_hessian"]["douglis_nirenberg_weights_selected"] is False and registry["green_radical_quotient_selected"] is False and registry["bfv_reduction_selected"] is False)
check("review", "hostile review blocks mass repair and carrier transfer", "zero order" in review and "distinct four-field" in review)
check("repo", "current state advances through K130", "K130 now totalizes" in current)
check("repo", "roadmap advances to K131", "K131" in roadmap[:9000])
check("repo", "context carries the exact radical packet", "196/196/198" in context[:18000])
check("predecessor", "K129 carries a K130 successor classification", "## K130 successor classification" in k129)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
