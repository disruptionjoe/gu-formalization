#!/usr/bin/env python3
"""OQ-RK1: attempt to ASSEMBLE E_RS^eff from the four justified component specs
and compute the decisive rank_H( Pi_RS . E_+ . Pi_RS ).

Discipline (FC4-HOLONOMY-01 anti-fabrication):
  - Every matrix below traces to a justified component spec. No matrix is
    constructed by guessing to hit a target.
  - The forbidden moves are NEVER executed, only documented:
      * rank_eff := ind_H / Ahat(K3) = 8/2 = 4      (INVALID_TARGET_DIVISION)
      * inserting ind_H(D_RS) = 8 as an input
  - If a piece cannot be built without guessing, the assembly BLOCKS and returns
    a typed "missing input" verdict rather than a number.

What is computable (all target-free):
  C1  Cl(9,5) anchor      : E_+ rank_H = 32 ; raw 14D gamma-trace kernel = 416_H
  C2  Cl(4,0) toy         : Pi_raw . E_+ . Pi_raw = 96_C = 48_H (naive)
                            + gauge image NOT annihilated (symbol norm != 0)
  C3/C4 K3 index family   : ind_C(q,k,n) = (-40+2q)n + (4+q)k, n=16
                            flat k=0: q in {0,+1,-1} -> {-640,-608,-672}
                            ind_H = ind_C/2 (conditional) -> {-320,-304,-336}

None of these computable numbers is 4 or 8. The decisive rank_H(Pi_RS.E_+.Pi_RS)
is NOT computable because the physical projector Pi_RS^phys / E_RS^eff and the
common right-H module M_RS,H^src do not exist in the repo: the load-bearing
missing object is RS_GU^phys (the source-defined gauge/BRST differential
d_RS,-1, gauge-fixing condition, ghost complex, and resulting K-theory symbol
class). Verdict: BLOCKED_NEEDS_SPEC.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# Reuse the already-verified, target-free constructions.
import oq_rk1_cl95_explicit_rep as cl95          # Cl(9,5) = M(64,H) anchor
import rs_clifford_projector_model as toy         # Cl(4,0) RS gamma-trace toy


# ---------------------------------------------------------------------------
# C2: Cl(4,0) toy composite  Pi_raw . E_+ . Pi_raw  (raw fiber surrogate)
# ---------------------------------------------------------------------------
def cl4_composite_rank() -> dict:
    """rank_C( Pi_raw . E_+ . Pi_raw ) in the Cl(4,0)xF=C^16 toy.

    This is the closest directly-computable surrogate for
    rank_H(Pi_RS . E_+ . Pi_RS), but with the RAW gamma-trace projector
    Pi_raw, NOT the (nonexistent) physical projector Pi_RS^phys.
    """
    gammas = toy.euclidean_gamma_matrices()
    internal = np.eye(toy.INTERNAL_RANK_C, dtype=complex)  # F = C^16
    g_full = np.hstack([np.kron(g, internal) for g in gammas])  # C^256 -> C^32
    pi_raw = toy.kernel_projector(g_full)
    chir_plus = np.diag([0, 0, 1, 1]).astype(complex)           # Cl(4,0) chirality +
    e_plus = np.kron(np.eye(4, dtype=complex), np.kron(chir_plus, internal))
    composite = pi_raw @ e_plus @ pi_raw
    rank_c = int(np.linalg.matrix_rank(composite, tol=toy.TOL))
    return {
        "domain_dim_C": int(g_full.shape[1]),
        "gamma_trace_rank_C": int(np.linalg.matrix_rank(g_full, tol=toy.TOL)),
        "pi_raw_rank_C": int(np.linalg.matrix_rank(pi_raw, tol=toy.TOL)),
        "e_plus_rank_C": int(np.linalg.matrix_rank(e_plus, tol=toy.TOL)),
        "composite_rank_C": rank_c,
        "composite_rank_H_if_halvable": rank_c / 2.0,
        "idempotent_err": float(np.max(np.abs(composite @ composite - composite))),
    }


# ---------------------------------------------------------------------------
# C3 / C4: honest K3 Atiyah-Singer index FAMILY (no target-division)
#   ind_C( D^{(V+q) tensor F} ) = int_K3 Ahat(TK3) ch((V+q) tensor F)
#                               = (4+q) n Ahat + n p1 + (4+q) k
# with Ahat(K3)=2, p1(K3)[K3]=-48, n=rank_C(F), k=ch_2(F)[K3].
# ---------------------------------------------------------------------------
def k3_index_complex(q: int, k: int, n: int = 16) -> int:
    AHAT, P1 = 2, -48
    return (4 + q) * n * AHAT + n * P1 + (4 + q) * k


def k3_index_family(n: int = 16, k: Optional[int] = None) -> dict:
    """If k is None the index is a SYMBOLIC family in (q,k); flat k=0 only as a
    labeled control. Never set k to hit a target."""
    out = {"n": n, "coefficient_form": "(-40+2q)*n + (4+q)*k", "k_status": "SYMBOLIC_UNFIXED"}
    if k is None:
        # report the symbolic coefficients per branch
        out["symbolic_branches"] = {
            "q=0_full_vector_spinor": "(-40)*n + (4)*k",
            "q=+1_raw_gamma_trace_free": "(-38)*n + (5)*k",
            "q=-1_brst_style": "(-42)*n + (3)*k",
        }
        # flat-F CONTROL ONLY (k=0 is imported, not proven)
        out["flat_F_control_k0_ind_C"] = {
            "q=0": k3_index_complex(0, 0, n),
            "q=+1": k3_index_complex(1, 0, n),
            "q=-1": k3_index_complex(-1, 0, n),
        }
        out["flat_F_control_k0_ind_H_if_Htrace"] = {
            kk: vv / 2.0 for kk, vv in out["flat_F_control_k0_ind_C"].items()
        }
    return out


# ---------------------------------------------------------------------------
# The E_RS^eff assembly attempt.  Every required input is a typed slot.
# If any load-bearing slot is missing, we BLOCK (no fabricated matrix).
# ---------------------------------------------------------------------------
@dataclass
class ERSAssemblyInputs:
    # The four components, as the repo supplies them:
    common_right_H_module: Optional[object] = None          # M_RS,H^src  (component 1/2)
    gauge_brst_differential_d_RS_minus_1: Optional[object] = None  # RS_GU^phys quotient (component 1)
    ghost_subtraction_count_a: Optional[int] = None         # fixes q=1-a (component 3)
    ch2_F_K3_value_k: Optional[int] = None                  # ch_2(F)[K3] (component 4)
    H_linear_trace_certificate: Optional[object] = None     # Tr_H (component 4)
    Y14_K3_same_operator_bridge: Optional[object] = None    # transport (component 3)
    E_plus_projector: Optional[object] = None               # component 2 (PINNED)
    missing: list = field(default_factory=list)


def assemble_E_RS_eff(inp: ERSAssemblyInputs) -> dict:
    """Attempt to build E_RS^eff as an H-linear idempotent on a common module and
    return rank_H(Pi_RS^phys . E_+ . Pi_RS^phys).  Blocks on first missing slot."""
    # Slot ordering reflects the dependency DAG: the module + quotient come first
    # because everything else (E_+ action, index coefficient, trace) is defined
    # ON that module.
    required = [
        ("common_right_H_module", inp.common_right_H_module,
         "M_RS,H^src: the source-selected common right-H module on which "
         "Pi_RS^phys, E_+, E_RS^eff all act"),
        ("gauge_brst_differential_d_RS_minus_1", inp.gauge_brst_differential_d_RS_minus_1,
         "RS_GU^phys: source-defined gauge/BRST differential d_RS,-1 + gauge-fixing "
         "condition + ghost complex (defines Pi_RS^phys)"),
        ("ghost_subtraction_count_a", inp.ghost_subtraction_count_a,
         "a (=> q=1-a): virtual-class/ghost count fixing the index coefficient"),
        ("ch2_F_K3_value_k", inp.ch2_F_K3_value_k,
         "k = ch_2(F)[K3] for the actual Sp(64)/section-pullback background"),
        ("H_linear_trace_certificate", inp.H_linear_trace_certificate,
         "Tr_H: global right-H structure preserved by connection + operator (rank_C->rank_H)"),
        ("Y14_K3_same_operator_bridge", inp.Y14_K3_same_operator_bridge,
         "same-operator Y^14 <-> K3 transport (or APS eta/h/SF/end terms)"),
    ]
    missing = [(name, why) for name, val, why in required if val is None]
    if missing:
        first_name, first_why = missing[0]
        return {
            "status": "BLOCKED_NEEDS_SPEC",
            "decisive_rank_H_Pi_E_Pi": "NOT_COMPUTABLE",
            "first_missing_slot": first_name,
            "first_missing_reason": first_why,
            "all_missing_slots": [m[0] for m in missing],
            "note": ("Pi_RS^phys and E_RS^eff cannot be instantiated as H-linear "
                     "idempotents on one common module; the expression "
                     "rank_H(Pi_RS.E_+.Pi_RS) is not uniquely typed."),
        }
    # If we ever get here, all slots are present -> the rank would be computable.
    # We deliberately do NOT fabricate a path to this branch.
    raise RuntimeError("Unreachable: no source data fills the E_RS^eff slots; "
                       "reaching this branch would require fabricating the quotient.")


def main() -> dict:
    report = {}

    # --- C1: Cl(9,5) anchor (re-run the verified construction) -------------
    anchor = cl95.main()
    report["C1_cl95_anchor"] = {
        "E_plus_rank_H": anchor["E_plus_rank_H"],                 # 32
        "raw_14D_gamma_trace_kernel_rank_H": anchor["raw_RS_kernel_rank_H"],  # 416
        "clifford_ok": anchor["clifford_ok"],
        "omega_sq_is_plus_I": anchor["omega_squared_is_plus_I"],
    }

    # --- C2: Cl(4,0) toy composite + gauge-image non-annihilation ----------
    comp = cl4_composite_rank()
    toy_model = toy.compute_model()
    gauge_norm = toy_model["sample_raw_projected_symbol"]["raw_symbol_on_projected_gauge_norm"]
    report["C2_cl4_toy"] = {
        "Pi_raw_E_plus_Pi_raw_rank_C": comp["composite_rank_C"],          # 96
        "Pi_raw_E_plus_Pi_raw_rank_H_if_halvable": comp["composite_rank_H_if_halvable"],  # 48
        "gauge_image_rank_C": toy_model["sample_raw_projected_symbol"]["projected_gauge_rank_C"],
        "RS_symbol_on_gauge_image_norm": gauge_norm,                      # 73.48 != 0
        "pure_gauge_NOT_annihilated": bool(gauge_norm > 1e-6),
    }

    # --- C3/C4: honest K3 index family (no target division) ----------------
    report["C3C4_k3_index_family"] = k3_index_family(n=16, k=None)

    # --- Assembly attempt with repo-supplied (all-None) inputs -------------
    inp = ERSAssemblyInputs(E_plus_projector="PINNED_rank_H_32")  # only E_+ is pinned
    report["assembly"] = assemble_E_RS_eff(inp)

    # --- Forbidden moves: documented, NOT executed -------------------------
    report["forbidden_moves_not_executed"] = {
        "INVALID_TARGET_DIVISION": "rank_eff := ind_H/Ahat(K3) = 8/2 = 4  (REFUSED)",
        "target_index_insertion": "ind_H(D_RS) := 8  (REFUSED)",
    }

    # --- Does any computable number equal 4 or 8? --------------------------
    computable = {
        "E_plus_rank_H": 32,
        "raw_cl95_kernel_rank_H": 416,
        "cl4_toy_composite_rank_C": comp["composite_rank_C"],
        "cl4_toy_composite_rank_H": comp["composite_rank_H_if_halvable"],
        "k3_ind_C_flat_q0": k3_index_complex(0, 0, 16),
        "k3_ind_C_flat_qp1": k3_index_complex(1, 0, 16),
        "k3_ind_C_flat_qm1": k3_index_complex(-1, 0, 16),
        "k3_ind_H_flat_q0": k3_index_complex(0, 0, 16) / 2.0,
        "k3_ind_H_flat_qp1": k3_index_complex(1, 0, 16) / 2.0,
        "k3_ind_H_flat_qm1": k3_index_complex(-1, 0, 16) / 2.0,
    }
    report["any_computable_equals_4_or_8"] = any(v in (4, 8) for v in computable.values())
    report["computable_numbers"] = computable

    # --- print human-readable ---------------------------------------------
    print("\n" + "=" * 78)
    print("OQ-RK1  E_RS^eff ASSEMBLY ATTEMPT  (four justified components)")
    print("=" * 78)
    print("C1 Cl(9,5) anchor : E_+ rank_H = {}, raw 14D kernel = {}_H".format(
        report["C1_cl95_anchor"]["E_plus_rank_H"],
        report["C1_cl95_anchor"]["raw_14D_gamma_trace_kernel_rank_H"]))
    print("C2 Cl(4,0) toy    : Pi_raw.E_+.Pi_raw = {}_C = {}_H ; "
          "gauge image NOT annihilated (symbol norm {:.2f} != 0)".format(
              report["C2_cl4_toy"]["Pi_raw_E_plus_Pi_raw_rank_C"],
              report["C2_cl4_toy"]["Pi_raw_E_plus_Pi_raw_rank_H_if_halvable"],
              report["C2_cl4_toy"]["RS_symbol_on_gauge_image_norm"]))
    print("C3/C4 K3 index    : ind_C=(-40+2q)*16+(4+q)*k ; flat-control k=0 -> "
          "q0={}, q+1={}, q-1={}  (ind_H = /2 -> {}, {}, {})".format(
              k3_index_complex(0, 0, 16), k3_index_complex(1, 0, 16), k3_index_complex(-1, 0, 16),
              k3_index_complex(0, 0, 16) / 2, k3_index_complex(1, 0, 16) / 2,
              k3_index_complex(-1, 0, 16) / 2))
    print("-" * 78)
    print("Any computable number equal to 4 or 8?  {}".format(
        report["any_computable_equals_4_or_8"]))
    print("ASSEMBLY STATUS  : {}".format(report["assembly"]["status"]))
    print("decisive rank_H(Pi_RS.E_+.Pi_RS) : {}".format(
        report["assembly"]["decisive_rank_H_Pi_E_Pi"]))
    print("first missing slot : {}".format(report["assembly"]["first_missing_slot"]))
    print("  -> {}".format(report["assembly"]["first_missing_reason"]))
    print("all missing slots  : {}".format(report["assembly"]["all_missing_slots"]))
    print("4 reachable ONLY via forbidden 8/Ahat(K3)=8/2 (INVALID_TARGET_DIVISION) -> REFUSED")
    print("=" * 78)
    print("\nMACHINE JSON:")
    print(json.dumps(report, indent=2, default=str))
    return report


if __name__ == "__main__":
    main()
