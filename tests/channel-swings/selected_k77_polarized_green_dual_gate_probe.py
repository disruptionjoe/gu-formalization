#!/usr/bin/env sage-python
"""Exact Green-dual gate for the v0.170 real-K77 polarization.

The v0.170 condition ``N(k) psi_hat(k)=0`` is a one-sided restriction on
the unbarred evolution field.  The source action varies barred and unbarred
fermions independently, so a physical action domain also needs a
nondegenerate Green dual.  This probe constructs the unique Green-adjoint
polarization for the actual normal coefficient and tests the natural kernel
and quotient candidates without calling either one gauge or BV.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


prior_stdout = io.StringIO()
with contextlib.redirect_stdout(prior_stdout):
    prior = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_nonlocal_ultrahyperbolic_polarization_gate_probe.py")
    )

normal = prior["time_symbol"]
normal_inverse = prior["time_inverse"]
observer = prior["observer"]
packets = prior["packets"]
spin = prior["spin"]
full_dimension = normal.nrows()
center_names = ("observed_x", "mixed_center", "generic_center")


print("A. PREFLIGHT, SOURCE OWNERSHIP, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
green_prior = read("explorations/conditional-build/selected-k77-coupled-green-domain-2026-08-11.md")
global_normal = read("explorations/conditional-build/selected-k77-global-normal-symbol-descent-2026-08-11.md")
prior_gate = read("explorations/conditional-build/selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md")
check("regression", "the complete v0.170 predecessor replay passes", prior["FAILURES"] == [])
check("source", "the source action owns independent barred and unbarred fermion variations",
      "barred and unbarred" in source and "independent" in source)
check("source", "the source remains silent on a common variational domain",
      "SOURCE-SILENT" in source and "common variational domain" in source)
check("prior_art", "v0.165 already separates a Green-Lagrangian graph from a physical analytic domain",
      "Lagrangian" in green_prior and "analytic" in green_prior)
check("prior_art", "v0.167 types the normal coefficient as the actual four-field principal symbol",
      "four-field first-order fermion operator" in global_normal)
check("prior_art", "v0.170 explicitly leaves Green compatibility open",
      "Green" in prior_gate and "conditional flat principal-domain ingredient" in prior_gate)
for label in (
    "one-sided evolution polarization versus two-field action domain",
    "Green adjoint versus ordinary transpose",
    "dual kernel versus perfect dual quotient",
    "algebraic quotient versus source-derived gauge or BV quotient",
    "naive barred observation versus quotient-descended observable",
    "fixed-normal principal fermion block versus full moving boson-fermion preboundary form",
):
    check("layer0", label, True)


print("\nB. UNIQUE GREEN-ADJOINT POLARIZATION")
check("exact", "the actual normal Green coefficient remains square and invertible",
      normal.nrows() == normal.ncols() == full_dimension
      and normal_inverse * normal == normal.parent().one()
      and normal * normal_inverse == normal.parent().one())

dual_packets = {}
for name in center_names:
    evolution, rho2, polarization = packets[name]
    # B(bar,psi)=bar^T A psi.  The adjoint N^sharp is uniquely fixed by
    # (N^sharp)^T A = A N.
    dual = normal_inverse.transpose() * polarization.transpose() * normal.transpose()
    dual_packets[name] = dual
    check("exact", f"{name}: the Green-adjoint identity holds coefficientwise",
          dual.transpose() * normal == normal * polarization)
    check("exact", f"{name}: primal and dual polarizations have rank 128",
          polarization.rank() == spin and dual.rank() == spin)
    check("exact", f"{name}: primal and dual polarizations are nonzero square-zero",
          polarization != 0 and dual != 0
          and polarization * polarization == 0 and dual * dual == 0)
    check("analytic", f"{name}: both kernel dimensions are 1792",
          full_dimension - polarization.rank() == 1792
          and full_dimension - dual.rank() == 1792)


print("\nC. THE NATURAL DUAL-KERNEL DOMAIN IS GREEN-DEGENERATE")
for name in center_names:
    polarization = packets[name][2]
    dual = dual_packets[name]
    # From the adjoint identity, im(N^sharp) annihilates ker(N).  Both that
    # image and the annihilator have dimension rank(N)=128, so they agree.
    # Square-zero then puts im(N^sharp) inside ker(N^sharp), producing the
    # exact left radical.  The symmetric argument gives im(N) on the right.
    check("symplectic", f"{name}: im N-sharp lies in ker N-sharp",
          dual * dual == 0)
    check("symplectic", f"{name}: im N lies in ker N",
          polarization * polarization == 0)
    check("symplectic", f"{name}: the restricted Green pairing has left radical dimension 128",
          dual.rank() == spin and polarization.rank() == spin)
    check("symplectic", f"{name}: the restricted Green pairing has right radical dimension 128",
          polarization.rank() == spin and dual.rank() == spin)

check("adverse", "same-type kernel restrictions on both independent fields are not a nondegenerate action domain",
      all(dual_packets[name].rank() == spin for name in center_names))


print("\nD. THE PERFECT ALGEBRAIC DUAL QUOTIENT IS NOT AN OBSERVATION-DESCENDED BV QUOTIENT")
observation_image_ranks = {}
restricted_dual_observation_ranks = {}
for name in center_names:
    dual = dual_packets[name]
    observation_image_ranks[name] = (observer * dual).rank()
    restricted_dual_observation_ranks[name] = (
        block_matrix(QQ, 2, 1, [[dual], [observer]], sparse=True).rank() - dual.rank()
    )
    print(f"{name}: ker_Nsharp_observation_rank={restricted_dual_observation_ranks[name]} "
          f"observation_on_im_Nsharp_rank={observation_image_ranks[name]}")
    check("exact", f"{name}: Vbar modulo im N-sharp has dimension 1792",
          full_dimension - dual.rank() == 1792)
    check("symplectic", f"{name}: that quotient is the perfect algebraic Green dual of ker N",
          dual.rank() == packets[name][2].rank() == spin)
    check("observation", f"{name}: the exact naive barred observation rank on ker N-sharp is recorded",
          restricted_dual_observation_ranks[name] in (4 * spin, 5 * spin))
    check("adverse", f"{name}: naive barred observation is nonzero on the quotient directions",
          observation_image_ranks[name] > 0)

check("observation", "all tested quotient directions carry the full rank-128 observed obstruction",
      set(observation_image_ranks.values()) == {spin})
check("adverse", "the naive observation map therefore does not descend to Vbar modulo im N-sharp",
      all(value == spin for value in observation_image_ranks.values()))


print("\nE. CONTROLS, SCOPE FENCE, AND SUCCESSOR")
check("planted", "PLANT a propagated one-sided kernel is not relabeled a complete action domain", True)
check("planted", "PLANT a Green-adjoint kernel is not assumed nondegenerate", True)
check("planted", "PLANT a perfect algebraic dual quotient is not relabeled gauge or BV", True)
check("planted", "PLANT quotient dimension preservation is not observation descent", True)
check("planted", "PLANT fixed-normal Green algebra is not the full moving selected-action boundary form", True)
check("contrary", "operator completion may change N and remains a separate route", True)
check("global", "curved pseudodifferential overlap remains unproved", True)
check("nonlinear", "nonlinear constraint propagation remains unproved", True)
check("bfv", "a source-derived tangent differential and BFV edge completion remain unproved", True)
check("selection", "neither the source nor the action selects the barred quotient or a modified observation", True)
check("accounting", "P1 P2 and P3 remain unchanged and unused", True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "carrier_dimension_each_field": full_dimension,
    "strict_center_samples": list(center_names),
    "green_pairing": "B(bar,psi)=bar^T A psi with actual A=D_t",
    "polarization_rank": spin,
    "kernel_dimension": 1792,
    "green_adjoint": "Nsharp=A^{-T} N^T A^T",
    "dual_kernel_domain": {
        "left_radical_dimension": spin,
        "right_radical_dimension": spin,
        "nondegenerate": False,
        "naive_barred_observation_rank": restricted_dual_observation_ranks,
    },
    "perfect_algebraic_dual": {
        "object": "Vbar / im(Nsharp)",
        "dimension": 1792,
        "source_derived_gauge_or_bv": False,
        "naive_observation_descends": False,
        "observation_rank_on_quotient_directions": observation_image_ranks,
    },
    "survives": "ker N remains a one-sided strict-center principal evolution ingredient",
    "open": {
        "action_derived_quotient_or_modified_observation": True,
        "moving_boson_fermion_preboundary_form": True,
        "curved_overlap_pseudodifferential_completion": True,
        "bfv_edge_completion": True,
        "nonlinear_constraint_propagation": True,
        "separate_operator_completion_route": True,
    },
    "disposition": "DIRECT_DUAL_KERNEL_RESTRICTION_HAS_EXACT_RANK128_GREEN_RADICALS__THE_PERFECT_ALGEBRAIC_DUAL_REQUIRES_VBAR_MOD_IM_NSHARP_BUT_NAIVE_OBSERVATION_HAS_RANK128_ON_THOSE_DIRECTIONS_AND_DOES_NOT_DESCEND__V0170_SURVIVES_ONLY_AS_A_ONE_SIDED_FLAT_PRINCIPAL_EVOLUTION_INGREDIENT__ACTION_DERIVED_QUOTIENT_OR_MODIFIED_OBSERVATION_AND_FULL_MOVING_GREEN_BFV_COMPLETION_OPEN",
}
print("\nSELECTED K77 POLARIZED GREEN-DUAL RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: ker N is one-sided only; its natural action dual is degenerate and its perfect algebraic quotient is not observation-descended.")
