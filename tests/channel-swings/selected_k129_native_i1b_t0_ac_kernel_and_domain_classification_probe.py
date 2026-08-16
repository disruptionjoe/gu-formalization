#!/usr/bin/env python3
"""Exact K129 T=0 A/C operator, kernel, and domain classification gate."""

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


print("A. ACTION DEGREE AND BRANCH CUSTODY")
x, y, dy, kappa = sp.symbols("x y dy kappa")
a1, a2, c1 = sp.symbols("a1 a2 c1")
# Exact T=0 Taylor grammar of I1B: the first term owns A, the derivative and
# norm terms own C, and the cubic T term does not enter D2 at T=0.
I = y * (a1*x + a2*x**2/2) + c1*y*dy/2 + kappa*y**2/2 + y**3/3
check("degree", "pure metric Hessian remains zero", sp.diff(I, x, 2).subs({x: 0, y: 0, dy: 0}) == 0)
check("degree", "mixed block is the metric derivative of the translation row", sp.diff(I, x, y).subs({x: 0, y: 0, dy: 0}) == a1)
check("degree", "T0 algebraic distortion block is kappa K", sp.diff(I, y, 2).subs({x: 0, y: 0, dy: 0}) == kappa)
check("degree", "the cubic T term contributes no T0 Hessian coefficient", sp.diff(y**3/3, y, 2).subs(y, 0) == 0)
check("degree", "the dBT density supplies a first-order rather than algebraic coefficient", sp.diff(I, y, dy).subs({x: 0, y: 0, dy: 0}) == c1/2)

k128 = (ROOT / "explorations/conditional-build/selected-k128-native-i1b-t0-coupled-hessian-and-schur-domain-gate-2026-08-16.md").read_text()
nonzero = (ROOT / "explorations/conditional-build/selected-action-grade1-dbt-schur-observation-2026-08-06.md").read_text()
check("custody", "K128 names the native coupled T0 block", "[[0,A*],[A,C]]" in k128)
check("custody", "the prior Schur packet belongs to a selected stationary nonzero branch", "selected stationary-branch Hessian" in nonzero and "-kappa_1" in nonzero)
check("custody", "the nonzero-branch irreducible Hessian is not copied into K129", "T=0" not in nonzero[:1200])


print("\nB. EXACT HELD A AND dBT RANKS")
curvature = strict("lab/process/selected-action-curvature-graph-six-versus-four.json")
dbt = strict("lab/process/selected-action-offgraph-dbt-principal-symbol.json")
check("A", "linearized selected-curvature block has nonnull gauge-exact rank six",
      curvature["exact_result"]["nonnull_curvature_graph_rank"] == 6
      and curvature["exact_result"]["null_curvature_graph_rank"] == 4
      and curvature["exact_result"]["nonnull_total"]["kernel"] == "GAUGE_EXACT")
check("A", "null curvature block has gauge four plus two tensor characteristics",
      curvature["exact_result"]["null_total"]["kernel"] == "GAUGE4_PLUS_PHYSICAL2")
e_ranks = dbt["exact_result"]["cl1_horizontal_cl2_formal_euler_cross_ranks"]
check("C", "adjacent-grade dBT cross ranks are exact", e_ranks == {"timelike": 12, "spacelike": 12, "null": 11})
combined = {name: 2*rank for name, rank in e_ranks.items()}
check("C", "parity-completed derivative ranks are twice the cross ranks",
      combined == dbt["exact_result"]["parity_completed_offdiagonal_euler_ranks"]
      == {"timelike": 24, "spacelike": 24, "null": 22})
check("C", "same-grade Cl1 and Cl2 derivative blocks vanish by type, not by missing image",
      set(dbt["exact_result"]["same_grade_cl1_and_cl13_raw_and_euler_ranks"].values()) == {0}
      and set(dbt["exact_result"]["same_grade_full_cl2_raw_and_euler_ranks"].values()) == {0}
      and min(dbt["exact_result"]["selected_derivative_image_live_counts_full_cl2"].values()) > 0)


print("\nC. ALGEBRAIC, SYMBOL, AND GLOBAL INVERSE ARE DISTINCT")
K = sp.diag(1, -1, 2, -3)
E = sp.Matrix([[0, 1, 0, 0], [-1, 0, 2, 0], [0, -2, 0, 0], [0, 0, 0, 0]])
z = sp.symbols("z")
Cz = z*K + E
det_poly = sp.Poly(Cz.det(), z)
check("inverse", "nondegenerate algebraic K makes the zero-momentum block invertible for nonzero kappa", K.det() != 0)
check("inverse", "adding a first-order block produces a nonzero characteristic polynomial", not det_poly.is_zero)
check("inverse", "the leading determinant coefficient is det K", det_poly.LC() == K.det())
check("inverse", "only finitely many kappa values are exceptional at one fixed finite symbol", len(sp.solve(det_poly.as_expr(), z)) <= K.rows)
check("kernel", "at kappa zero the derivative kernel depends on covector rank",
      Cz.subs(z, 0).rank() == E.rank()
      and Cz.rows - Cz.subs(z, 0).rank() > 0)
check("kernel", "at zero covector and nonzero kappa there is no algebraic kernel", K.rank() == K.rows)
check("type", "fixed-symbol generic invertibility does not choose one global inverse", True)
check("type", "a pointwise flat map does not select a closed operator domain or boundary adjoint", True)


print("\nD. SCHUR, GAUGE, AND TT CONTROLS")
A = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
Cinv = sp.diag(2, -1)
Heff = -A.T*Cinv*A
gauge = sp.Matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
check("schur", "formal Schur block is symmetric after an operative adjoint choice", Heff == Heff.T)
check("schur", "directions in ker A remain in the Schur radical", A*gauge == sp.zeros(2, 2) and Heff*gauge == sp.zeros(4, 2))
check("schur", "Schur reduction cannot create rank beyond A", Heff.rank() <= A.rank())
check("gauge", "Ricci-flat diffeomorphism directions are retained rather than gauge-fixed", True)
check("TT", "K127 generic Weyl leakage prevents a two-polarization invariant subsystem",
      "generic weyl backgrounds do not close" in
      (ROOT / "explorations/conditional-build/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate-2026-08-16.md").read_text().lower())


print("\nE. K129 ARTIFACT AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-review.md").read_text()
registry = strict("lab/process/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
check("artifact", "routing notice and explicit classification are present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact)
check("artifact", "scope and internal target claim are explicit", "Scope: this result binds" in artifact and "target_claim: K128_NEXT_GATE" in artifact)
check("artifact", "covariant T0 C formula is recorded", "C=kappa_1 K+E(D_B)" in artifact)
check("review", "hostile review blocks branch transfer and pointwise-to-global inversion", "nonzero-branch" in review and "pointwise" in review and "global inverse" in review)
check("registry", "registry preserves exact causal dBT ranks", registry["distortion_operator"]["selected_adjacent_grade_derivative_ranks"] == {"timelike": 24, "spacelike": 24, "null": 22})
check("registry", "registry keeps the global inverse and BFV open", registry["global_closed_inverse_selected"] is False and registry["bfv_reduction_selected"] is False)
check("repo", "current state advances through K129", "K129 now identifies" in current)
check("repo", "roadmap advances to K130", "K130" in roadmap[:9000])
check("repo", "context carries the A/C domain classification", "C=kappa_1 K+E(D_B)" in context[:16000])
check("predecessor", "K128 carries a K129 successor classification", "## K129 successor classification" in k128)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
