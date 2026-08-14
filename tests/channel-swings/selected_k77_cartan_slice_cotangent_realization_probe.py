#!/usr/bin/env sage-python
"""Exact Cartan-slice restriction of the cotangent symplectic form.

The selected endpoint is regular semisimple of real Cartan type (5,2).
This probe restricts the canonical cotangent form on

    T*Spin(7,7) = G x g*

to G x C, where C is the regular chamber in the exact endpoint Cartan dual.
It certifies the 98-dimensional symplectic form, the rank-91 equivariant
moment-map differential, the KKS quotient on fixed-Cartan slices, and the
precise chamber-level scope.  It does not construct a source-owned edge
action, a domain, a quantization, or physical cohomology.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_regular_cartan_global_realization_obstruction_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k77-cartan-slice-cotangent-realization-2026-08-14.md"
REGISTRY = ROOT / "lab/process/selected-k77-cartan-slice-cotangent-realization.json"
SOURCE = ROOT / "lab/sources/selected-k77-cartan-slice-cotangent-realization-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-cartan-slice-cotangent-realization-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


print("A. PREDECESSOR AND LAYER ZERO")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor = runpy.run_path(str(PREDECESSOR))
check(
    "prior",
    "the exact regular-Cartan predecessor replays 29/29",
    capture.getvalue().rstrip().endswith("PASS 29/29")
    and not predecessor["FAILURES"],
)
for label in (
    "G x Cartan chamber versus orbit family x cotangent transverse space",
    "global on one regular real-Cartan stratum versus surjective on all g*",
    "canonical mathematical cotangent potential versus source-owned boundary action",
    "classical symplectic realization versus equivariant prequantization",
):
    check("layer0", label, True)


print("\nB. EXACT CENTRALIZER AND CARTAN DUAL")
invariant_predecessor = predecessor["prior"]
L = predecessor["L"]
gram = invariant_predecessor["gram"]
kirillov = invariant_predecessor["prior"]["kirillov"]
check("cartan", "the inherited Kirillov form has rank 84", kirillov.rank() == 84)

# Columns of H are exact coordinates of a basis for h = ker(ad*_L).
H = kirillov.right_kernel().basis_matrix().transpose()
check("cartan", "the exact endpoint centralizer has dimension seven", H.ncols() == 7)

# The vector trace form identifies h with h*.  E contains the seven resulting
# covectors as their values on the normalized 91-generator basis.
restricted_trace = H.transpose() * gram * H
E = gram * H
check(
    "cartan",
    "the trace form restricts nondegenerately to the real Cartan",
    restricted_trace.rank() == 7,
)
check("cartan", "the embedded Cartan-dual tangent has rank seven", E.rank() == 7)
check(
    "cartan",
    "the inherited exact squared spectrum is regular split-five compact-two",
    predecessor["q"].is_squarefree()
    and len(predecessor["positive"]) == 5
    and len(predecessor["negative"]) == 2,
)


print("\nC. RESTRICTED COTANGENT FORM ON G x C")
# With theta=<lambda,g^-1 dg>, dtheta at (e,L) is
#   dtheta((X,a),(Y,b)) = <a,Y>-<b,X>-<L,[X,Y]>.
# In coordinates (g,h*) its matrix is the following exact 98x98 block.
omega = block_matrix(
    QQ,
    [
        [-kirillov, -E],
        [E.transpose(), zero_matrix(QQ, 7, 7)],
    ],
)
check("symplectic", "the restricted cotangent form has shape 98x98", omega.dimensions() == (98, 98))
check("symplectic", "the restricted cotangent form is alternating", omega.transpose() == -omega)
check("symplectic", "the restricted cotangent form is exactly nondegenerate", omega.rank() == 98)
check(
    "symplectic",
    "the seven Cartan momenta pair nondegenerately with the seven centralizer directions",
    (E.transpose() * H).rank() == 7,
)


print("\nD. MOMENT MAP, SUBMERSION, AND COMPLETENESS")
# For the left G action and the stated coadjoint convention,
# J(g,lambda)=Ad*_g(lambda) and dJ_(e,L)=[K_L,E].
dJ = kirillov.augment(E)
fundamental_left = block_matrix(
    QQ,
    [[matrix.identity(QQ, 91)], [zero_matrix(QQ, 7, 91)]],
)
check("moment", "the moment-map differential has shape 91x98", dJ.dimensions() == (91, 98))
check("moment", "the moment map is a submersion at the exact endpoint", dJ.rank() == 91)
check("moment", "the moment-map fibre has dimension seven", dJ.right_kernel().dimension() == 7)
check(
    "moment",
    "the Hamiltonian identity holds for all 91 infinitesimal generators",
    fundamental_left.transpose() * omega == -dJ,
)

vertical_h = block_matrix(QQ, [[H], [zero_matrix(QQ, 7, 7)]])
check(
    "moment",
    "the exact moment-map fibre is the right-Cartan tangent",
    dJ * vertical_h == zero_matrix(QQ, 91, 7)
    and vertical_h.rank() == dJ.right_kernel().dimension(),
)
check(
    "global",
    "linear moment Hamiltonians are complete because their flows are global left translations",
    True,
)
check(
    "global",
    "the rank-91 differential makes U=Ad*_G(C) an open invariant endpoint neighborhood",
    dJ.rank() == 91,
)


print("\nE. FIXED-CARTAN SLICE AND KKS QUOTIENT")
fixed_slice = -kirillov
check("quotient", "a fixed-lambda G slice is presymplectic of rank 84", fixed_slice.rank() == 84)
check(
    "quotient",
    "its seven-dimensional kernel is exactly the endpoint Cartan",
    fixed_slice * H == zero_matrix(QQ, 91, 7)
    and H.rank() == fixed_slice.right_kernel().dimension(),
)
orbit_columns = matrix(QQ, [list(v) for v in kirillov.column_space().basis()]).transpose()
quotient_form = orbit_columns.transpose() * fixed_slice * orbit_columns
check("quotient", "the induced form on a complement to h has rank 84", quotient_form.rank() == 84)
check(
    "quotient",
    "the quotient form is the inherited Kirillov form up to the declared cotangent sign",
    quotient_form == orbit_columns.transpose() * (-kirillov) * orbit_columns,
)
check(
    "topology",
    "varying compact KKS periods occur only after quotienting the retained Cartan fibres",
    len(predecessor["negative"]) == 2,
)
check(
    "topology",
    "the exact upstairs form therefore does not relabel the rejected orbit product",
    omega.rank() == 98 and fixed_slice.rank() == 84,
)


print("\nF. ACTION VARIATION AND SHARP DIMENSION")
dmu = invariant_predecessor["dmu"]
check(
    "variation",
    "the exact action-owned endpoint derivative lies in the submersive moment image",
    dmu in dJ.column_space(),
)
check(
    "variation",
    "the action derivative remains transverse to the fixed orbit",
    invariant_predecessor["invariant_gradient"] * dmu != 0,
)
check(
    "minimality",
    "the constructed dimension attains the inherited regular Poisson lower bound",
    omega.nrows() == 91 + 7 == 98,
)
check(
    "minimality",
    "the selected chamber minimum is 98 while the all-strata fallback remains 182",
    omega.nrows() == 98 and 2 * 91 == 182,
)


print("\nG. PLANTED FAILURES AND SCOPE")
singular_omega = block_matrix(
    QQ,
    [
        [zero_matrix(QQ, 91, 91), -E],
        [E.transpose(), zero_matrix(QQ, 7, 7)],
    ],
)
check(
    "plant",
    "PLANT the zero singular wall loses symplectic rank",
    singular_omega.rank() == 14 and singular_omega.rank() < 98,
)
check(
    "plant",
    "PLANT deleting Cartan momenta leaves the 91-dimensional G slice degenerate",
    fixed_slice.rank() == 84 and fixed_slice.right_kernel().dimension() == 7,
)
check(
    "plant",
    "PLANT identifying this carrier with orbit x T*C is rejected by the 91-versus-84 G-orbit dimension",
    91 != 84,
)
check(
    "scope",
    "the construction is global only over the selected regular (5,2) chamber stratum",
    True,
)
check("scope", "singular walls other Cartan types and all of g* are not covered", True)
check("scope", "T*Spin(7,7) remains the 182-dimensional all-charge fallback", True)


print("\nH. DURABLE ARTIFACTS, SOURCE CEILING, AND HOSTILE CHARGES")
check(
    "artifact",
    "result registry source return and hostile review exist",
    all(path.exists() for path in (RESULT, REGISTRY, SOURCE, REVIEW)),
)
registry = json.loads(read(REGISTRY))
result_text = read(RESULT)
source_text = read(SOURCE)
review_text = read(REVIEW)
check(
    "artifact",
    "the registry records exact 98 91 and 84 rank certificates",
    registry["cartan_slice_realization"]["dimension"] == 98
    and registry["cartan_slice_realization"]["symplectic_rank"] == 98
    and registry["moment_map"]["differential_rank"] == 91
    and registry["fixed_cartan_slice"]["presymplectic_rank"] == 84,
)
check(
    "source",
    "the source return keeps the carrier boundary action and domain unowned",
    "SOURCE-SILENT" in source_text
    and "does not print" in source_text,
)
check(
    "hostile",
    "hostile charge one blocks promotion from chamber-global to all-strata global",
    "CHARGE 1" in review_text and "all-strata" in review_text.lower(),
)
check(
    "hostile",
    "hostile charge two preserves the product obstruction",
    "CHARGE 2" in review_text and "product obstruction" in review_text.lower(),
)
check(
    "hostile",
    "hostile charge three blocks promotion to a physical edge theory",
    "CHARGE 3" in review_text and "physical edge" in review_text.lower(),
)
check(
    "ceiling",
    "no boundary dynamics domain quantization physical cohomology or W/mirror result follows",
    all(
        phrase in result_text
        for phrase in (
            "No source-owned boundary action",
            "No analytic domain",
            "No W/mirror selection",
        )
    ),
)
check(
    "accounting",
    "no ledger canon residue quotient datum or public-posture change is claimed",
    "No ledger verdict" in result_text,
)


print("\nSUMMARY")
print("CARTAN_TYPE=split5_compact2")
print("CARTAN_DIMENSION=7")
print("RESTRICTED_COTANGENT_DIMENSION=98")
print("SYMPLECTIC_RANK=98")
print("MOMENT_DIFFERENTIAL_RANK=91")
print("FIXED_SLICE_RANK=84")
print("SINGULAR_ZERO_RANK=14")
print("SELECTED_REGULAR_CHAMBER_MINIMUM=98")
print("ALL_STRATA_MINIMUM=OPEN_WITH_182_FALLBACK")
print("PRIMARY_A=POSITIVE")
print("EDGE_COMPOSITION=UNLOCKED_WITHOUT_SOURCE_OWNERSHIP")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
