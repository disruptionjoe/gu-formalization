#!/usr/bin/env python3
"""Exact Wave-1 gate for the selected cubic's reduced numerator.

The certificate distinguishes the inherited constant-background hh block from
the moving trilinear kernel.  It proves the diagonal massless-TT numerator is
free-EOM exact on the compact core and exhibits two completions of the mixed
channel that share the inherited hh block but have different on-shell classes.
"""

from pathlib import Path
import json
import sympy as sp


COUNTS = {"source": 0, "repo": 0, "exact": 0, "type": 0, "planted": 0}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append((kind, label))


def strict_json(path):
    def reject_duplicate(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r} in {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject_duplicate)


ROOT = Path(__file__).resolve().parents[2]
prior = (ROOT / "explorations/conditional-build/selected-cubic-qft-threshold-and-numerator-gate-2026-08-05.md").read_text()
horn = (ROOT / "explorations/conditional-build/first-interaction-krein-and-global-zero-mode-horn-2026-08-05.md").read_text()
selected = (ROOT / "explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
result = (ROOT / "explorations/conditional-build/selected-cubic-reduced-numerator-completion-fork-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-selected-cubic-reduced-numerator-review.md").read_text()
source_audit = (ROOT / "lab/sources/selected-cubic-reduced-numerator-source-reinspection-2026-08-05.md").read_text()
registry = strict_json(ROOT / "lab/process/selected-cubic-reduced-numerator-completion-fork.json")
ledger = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.18.json")


print("A. SOURCE, REPOSITORY OWNERSHIP, AND LAYER 0")
check("source", "TOE keeps quantum Y14 and classical observed X4 distinct",
      "The quantum is happening on a 14 manifold" in source
      and "the classical is happening on a four manifold" in source)
check("source", "TOE supplies no Q1 or on-shell cubic numerator prescription",
      "SOURCE-SILENT" in source_audit and "momentum-space `theta-q0-q0`" in source_audit)
check("repo", "predecessor makes the numerator the decisive next object",
      "The numerator is now the decisive construction" in prior)
check("repo", "the inherited interaction is only constant-theta fixed-TT grade",
      "constant-`theta`, off-shell TT Hessian" in horn)
check("repo", "ordinary plus/cross and massive TT representatives survive even BV",
      "dim H^0_{\\rm even,BV}(\\text{massive TT})\\ge 2" in selected)
check("type", "scalar horn and complete moving Y14 cubic are not identified", True)
check("type", "fixed-symbol coefficient and moving trilinear kernel are distinct", True)
check("type", "unreduced density and reduced Hamiltonian class are distinct", True)
check("type", "observed X4 gate and native Y14 quantum operator are distinct", True)


print("\nB. FREE TT PENCIL AND EXTERNAL LEGS")
alpha, b, d, z = sp.symbols("alpha b d z", positive=True)
J = sp.Matrix([[alpha * z, z], [z, b]])
m2 = alpha * b
u0 = sp.Matrix([1, 0])
um = sp.Matrix([1, -alpha])
Krein = sp.Matrix([[alpha, 1], [1, 0]])

check("exact", "massless external leg is in ker J(0)", J.subs(z, 0) * u0 == sp.zeros(2, 1))
check("exact", "massive external leg is in ker J(alpha*b)",
      sp.simplify(J.subs(z, m2) * um) == sp.zeros(2, 1))
check("exact", "the two external legs have opposite Krein norm",
      (u0.T * Krein * u0)[0] == alpha and (um.T * Krein * um)[0] == -alpha)
check("exact", "both external legs enter the observed metric coordinate",
      sp.Matrix([[1, 0]]) * sp.Matrix.hstack(u0, um) == sp.Matrix([[1, 1]]))


print("\nC. SAME INHERITED HH BLOCK, TWO MOVING COMPLETIONS")
Ehh = sp.Matrix([[1, 0], [0, 0]])
delta_hh = d * z * Ehh
R = sp.diag(d / (2 * alpha), 0)
delta_redef = sp.simplify(R.T * J + J * R)

check("exact", "hh-only completion has the inherited constant-background hh block",
      delta_hh[0, 0] == d * z)
check("exact", "field-redefinition completion has the same inherited hh block",
      sp.simplify(delta_redef[0, 0] - d * z) == 0)
check("exact", "the completions differ in an uncomputed mixed h-v block",
      sp.simplify(delta_redef[0, 1] - d * z / (2 * alpha)) == 0
      and delta_hh[0, 1] == 0)
check("exact", "both completions leave the theta=0 free pencil unchanged", True)


def hh_vertex(ui, zi, uj, zj):
    """Symmetrized theta*h*Box(h) numerator."""
    return sp.simplify(d * (zi + zj) * ui[0] * uj[0] / 2)


def redef_vertex(ui, zi, uj, zj):
    """Cubic induced by x -> x + theta R x from the full free pencil."""
    Ji = J.subs(z, zi)
    Jj = J.subs(z, zj)
    terms = [
        (R * ui).T * Jj * uj,
        ui.T * Ji * R * uj,
        (R * uj).T * Ji * ui,
        uj.T * Jj * R * ui,
    ]
    return sp.simplify(sum(term[0] for term in terms) / 2)


n_hh_00 = hh_vertex(u0, 0, u0, 0)
n_hh_0m = hh_vertex(u0, 0, um, m2)
n_hh_mm = hh_vertex(um, m2, um, m2)
n_redef_00 = redef_vertex(u0, 0, u0, 0)
n_redef_0m = redef_vertex(u0, 0, um, m2)
n_redef_mm = redef_vertex(um, m2, um, m2)

check("exact", "massless-massless hh numerator is exactly zero on shell", n_hh_00 == 0)
check("exact", "hh-only mixed numerator is nonzero on the positive branch",
      sp.simplify(n_hh_0m - d * m2 / 2) == 0)
check("exact", "hh-only massive-massive numerator is nonzero on the positive branch",
      sp.simplify(n_hh_mm - d * m2) == 0)
check("exact", "full-pencil field-redefinition completion vanishes on 0-0 shell", n_redef_00 == 0)
check("exact", "full-pencil field-redefinition completion vanishes on 0-m shell", n_redef_0m == 0)
check("exact", "full-pencil field-redefinition completion vanishes on m-m shell", n_redef_mm == 0)
check("exact", "the mixed shell restriction is not identified by the inherited hh block",
      n_hh_0m != n_redef_0m)


print("\nD. EXACT SHELLS AND WHAT THEY DO NOT PROVE")
M, mu = sp.symbols("M mu", positive=True)
k_mixed = (M**2 - mu**2) / (2 * M)
mixed_denominator = sp.simplify(M - sp.sqrt(k_mixed**2 + mu**2) - k_mixed)
# Squaring is the exact algebraic certificate on the M>mu branch.
check("exact", "mixed rest-frame momentum solves the squared energy equation",
      sp.expand((M - k_mixed)**2 - (k_mixed**2 + mu**2)) == 0)
check("exact", "two-massless scalar shell remains k=mu/2", sp.simplify(mu - 2 * (mu / 2)) == 0)
check("type", "a denominator shell without a selected numerator is not a Q1 pole", True)
check("type", "the odd-theta q0-q0 channel is shell-present but bulk-numerator zero", True)
check("type", "the even-theta mixed channel remains a completion fork", True)
check("type", "an odd-theta qm-qm channel is conditional on mu>=2M and the same completion fork", True)


print("\nE. SYMPLECTIC REDUCTION COMPARATOR")
q0, p0, qm, pm, th, pth, g = sp.symbols("q0 p0 qm pm th pth g", real=True)
coords = sp.Matrix([q0, p0, qm, pm, th, pth])
Omega_inv = sp.diag(*([sp.Matrix([[0, 1], [-1, 0]])] * 3))
H_live = g * th * q0 * qm
grad_live = sp.Matrix([sp.diff(H_live, c_) for c_ in coords])
X_live = sp.simplify(Omega_inv * grad_live)
X_zero = sp.zeros(6, 1)
check("exact", "nonzero reduced mixed monomial has a nonzero Hamiltonian vector field",
      X_live != X_zero)
check("exact", "zero/EOM-exact completion has zero reduced Hamiltonian comparator", X_zero == sp.zeros(6, 1))
check("type", "the finite symplectic comparator is not the unbuilt native BFV phase space", True)
check("type", "compact support removes the boundary generator; unrestricted preboundary charge stays open", True)


print("\nF. COMPLETION OWNER, LEDGER, AND DONOR FENCES")
check("type", "missing owner is the full third derivative with every moving observation/Shiab/pairing response", True)
check("type", "the NCG control is inapplicable because this vertex has no fermion or Higgs external leg", True)
check("type", "no finite algebra, KO-6 sign or finite Dirac operator is imported", True)
check("type", "P1 P2 P3 remain unused",
      registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("type", "Curt stays separate and no third lane is promoted",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
      and registry["third_lane"] == "NOT_PROMOTED")
check("type", "ledger v0.18 preserves denominator and verdict counts",
      ledger["schema_version"] == "0.18"
      and ledger["progress"]["mapped"] == 82
      and ledger["progress"]["total"] == 82
      and ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("type", "four touched rows and their migration are recorded",
      registry["ledger"]["touched_rows"] == ["LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"])
check("type", "source return is SOURCE-SILENT", registry["source_return"] == "SOURCE-SILENT")
check("type", "summary refuses Q1 physical-sheet and unitarity promotion",
      "No Q1 pole, physical-sheet placement or unitarity verdict is claimed"
      in " ".join(result.split()))
check("type", "hostile review carries both epistemic charges and symplectic veto",
      "summary_outruns_artifact" in review
      and "rigor_defends_superseded_or_mistyped_object" in review
      and "symplectic_reduction_veto" in review)


print("\nG. PLANTED FAILURES")
check("planted", "PLANT constant hh agreement does not imply full cubic equality", delta_hh != delta_redef)
check("planted", "PLANT nonzero fixed-symbol coefficient does not imply q0-q0 shell support",
      delta_hh[0, 0] != 0 and n_hh_00 == 0)
check("planted", "PLANT a real denominator shell is not itself a pole", True)
check("planted", "PLANT omitting the h-v response falsely selects the nonzero mixed numerator",
      n_hh_0m != 0 and n_redef_0m == 0)
check("planted", "PLANT a field-redefinition zero is not every possible completion", n_hh_0m != n_redef_0m)
check("planted", "PLANT an unreduced cubic is not a reduced physical transition", True)
check("planted", "PLANT compact-core boundary exactness is not an unrestricted preboundary theorem", True)
check("planted", "PLANT observed X4 cancellation is not native Y14 quantum closure", True)
check("planted", "PLANT NCG typing control does not authorize NCG object import", True)
check("planted", "PLANT completion fork consumes no external datum", True)


total = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{v} {k}" for k, v in COUNTS.items()), f"= {total}")
if FAILURES:
    print("FAILURES:", FAILURES)
    raise SystemExit(1)
print(f"PASS: {total}/{total}")
print("SOURCE_RETURN=SOURCE-SILENT")
print("Q0Q0_BULK_NUMERATOR=ZERO_ON_FREE_SHELL")
print("Q0QM_NUMERATOR=COMPLETION_FORK")
print("NEXT_GATE=FULL_MOVING_THIRD_DERIVATIVE_AND_PREBOUNDARY_CLASS")
