#!/usr/bin/env python3
"""RS_GU^phys assembly from the FOUR justified sub-structure specs, and the
determination of whether GU itself determines the BRST structure needed to make
rank_H( Pi_RS . E_+ . Pi_RS ) computable (4 => 3 generations, 8 => 4).

This is the 2026-06-26 follow-on to tests/oq_rk1_e_rs_eff_assembly.py. It adds,
on top of the prior BLOCKED verdict, a *typed origin determination*: for each of
the four pieces, is it (i) gu_derived, (ii) textbook_import, or (iii) a genuine
GU gap -- and it independently re-verifies the single load-bearing machine fact
(the pure-gauge image is NOT annihilated inside the gamma-trace kernel) that
turns "compute q" into "GU must first supply a gauge-fixing/BRST differential it
does not have".

DISCIPLINE (FC4-HOLONOMY-01 anti-fabrication):
  * No BRST/ghost structure is invented to make the count come out 3 (rank 4) or
    4 (rank 8). The ghost-subtraction count q is left FREE; building Pi_RS^phys
    would require choosing it, which is exactly the fabrication step we refuse.
  * The forbidden moves are documented, NEVER executed:
        rank_eff := ind_H / Ahat(K3) = 8/2 = 4   (INVALID_TARGET_DIVISION)
        inserting ind_H(D_RS) = 8 as an input
  * If a piece cannot be built without guessing, the assembly BLOCKS and returns
    a typed verdict naming the single remaining gap.
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

import oq_rk1_cl95_explicit_rep as cl95          # Cl(9,5) = M(64,H) anchor (verified)
import rs_clifford_projector_model as toy         # Cl(4,0) RS gamma-trace toy (verified)


# ---------------------------------------------------------------------------
# Part A. The FOUR sub-structure specs, encoded as origin-typed records.
# Each record states what GU's OWN source (tau+ / inhomogeneous gauge group /
# the action / the transcript / the 2021 draft) fixes, vs what must be imported,
# vs what is a genuine GU gap. Tags come from reading the source, not from a
# desired rank.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ComponentOrigin:
    name: str
    gu_derived: str          # what GU's own source genuinely fixes
    textbook_import: str     # what any spin-3/2 gauge theory supplies (not GU-specific)
    genuine_gu_gap: str      # what GU does NOT determine
    specifiable: str         # fully | partially | not


FOUR_COMPONENTS = [
    ComponentOrigin(
        name="C1: RS gauge symmetry / d_RS,-1 (gauge differential)",
        gu_derived=("SHAPE + H-structure: d_RS,-1 = d_A : Omega^0(Y14,/S) -> Omega^1(Y14,/S), "
                    "eps |-> D_mu eps, H-linear via the FORCED Sp(64)=U(64,H) connection "
                    "(Cl(9,5)=M(64,H)). Field zeta in Omega^1(/S) and a deg -1 differential EXIST "
                    "(transcript [00:49:16]: '0-forms and 1-forms valued in ad or the spinors')."),
        textbook_import=("Same shape psi_mu -> psi_mu + D_mu eps as textbook spin-3/2; GU adds the "
                         "bundle, the IG-augmented connection, and the H-structure."),
        genuine_gu_gap=("CANONICAL-OBJECT status: the pure-RS projection P_RS / quotient semantics; "
                        "an ACCEPTED explicit spinorial differential (only eq 10.10, author-disclaimed "
                        "'Caveat Emptor', repo-typed zero accepted RS-(-1) cells); and the action-FORCING "
                        "identity (Noether: delta_2 o d_RS,-1 = 0) that would make it canonical rather "
                        "than analogy-driven. tau-action lane uninhabited."),
        specifiable="partially",
    ),
    ComponentOrigin(
        name="C2: Gauge-fixing condition (Lorenz/de Donder analog)",
        gu_derived=("the gauge SYMMETRY to be fixed (IG = G semidirect Omega^1(ad P), SUSY-extended)."),
        textbook_import=("a gauge-fixing condition is the standard necessity: covariant nabla^a psi_a = 0, "
                         "or a Feynman term, or a BRST complex. (gamma^a psi_a = 0 is GU's DEFINITIONAL "
                         "irreducibility constraint R = ker Gamma, NOT a slice.)"),
        genuine_gu_gap=("GU PICKS NONE. It leaves the slice FREE: 'the entire universe without making any "
                        "choices' [00:49:16] retains the full IG as physical content -- structurally "
                        "ANTI-gauge-fixing. Candidate aleph/LC and tau+ references are 'natural but "
                        "underderived'. Upstream: the IG action field space "
                        "(FULL_IG / FIXED_ALEPH_GRAPH / DYNAMIC_A_GRAPH) is itself unselected."),
        specifiable="not",
    ),
    ComponentOrigin(
        name="C3: Ghost/BRST complex (degrees, signs, H-structure)",
        gu_derived=("the SKELETON + grading + H-structure: spinor-valued covariant de Rham complex "
                    "C^{-1}=Omega^0(/S) -d_A-> C^0=ker(Gamma) -Phi.d_A-> C^1=Omega^2(/S); form-degree "
                    "grading forced (ghost at deg 0, field at deg 1); d_A^2=0 asserted; S=H^64 right-H, "
                    "ghost a quaternionic 0-form spinor."),
        textbook_import=("promotion eps -> ghost c (commuting spinor, van Nieuwenhuizen statistics); "
                         "antighost/NL trivial pair; Nielsen-Kallosh ghost; physical = gh-0 BRST cohomology; "
                         "field-minus-ghost alternating sum = index."),
        genuine_gu_gap=("the SIGNED ghost multiplicities / net ghost count q = 1 - a (q in {0,+1,-1} NOT "
                        "source-derived); the gauge-fixing condition; the gamma-trace<->d_A compatibility "
                        "(machine-obstructed); ghost chirality (full S vs S^+); reducibility."),
        specifiable="partially",
    ),
    ComponentOrigin(
        name="C4: Elliptic symbol / K-theory class of the gauge-fixed complex",
        gu_derived=("the FORM: virtual class E(q) = (V+q) tensor F on T*K3, V=T_C^*K3 (rk 4, ch_2=-48), "
                    "F=s^*S(6,4) (rk 16); closed index ind_C = (-40+2q)n + (4+q)k. Raw (gamma-trace-free, "
                    "NO gauge-fixing) endpoint E_raw=(V+1)F is a genuine elliptic class."),
        textbook_import=("the whole spin-3/2 BRST apparatus: gauge-fixing, FP ghost/antighost, the q=-1 "
                         "'subtract two spinor Dirac complexes' E_BRST=(V-1)F, the Atiyah-Singer integral."),
        genuine_gu_gap=("the PHYSICAL member: q (ghost count) itself; d_RS,-1; whether the gauge-fixed "
                        "complex is even elliptic (raw symbol does NOT kill the gauge image -> naive 3-term "
                        "complex non-exact); k = ch_2(F)[K3]; the global Tr_H certificate; the Y14<->K3 bridge."),
        specifiable="partially",
    ),
]


# ---------------------------------------------------------------------------
# Part B. Independently RE-VERIFY the single load-bearing machine fact, in BOTH
# the Cl(4,0) toy and (newly) the Cl(9,5) anchor: the pure-gauge image
#   g_+(xi) : eps |-> P_+( xi tensor eps )
# is NOT annihilated by the constrained RS symbol inside the gamma-trace kernel.
# If it were annihilated, R^phys = ker(Gamma)/im(gauge) would be a clean subspace
# subtraction and NO ghost complex would be needed. It is not -> a genuine
# gauge-fixing + ghost complex is REQUIRED, and GU supplies none.
# ---------------------------------------------------------------------------
def obstruction_cl4() -> dict:
    m = toy.compute_model()
    s = m["sample_raw_projected_symbol"]
    return {
        "model": "Cl(4,0) x F=C^16",
        "projected_gauge_rank_C": s["projected_gauge_rank_C"],
        "RS_symbol_on_gauge_image_norm": s["raw_symbol_on_projected_gauge_norm"],
        "pure_gauge_annihilated_within_gamma_trace_kernel": bool(
            s["raw_symbol_on_projected_gauge_norm"] < 1e-6),
    }


def obstruction_cl95(xi=(1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
                         1.1, 0.3, 2.2, 1.7, 0.9, 1.3)) -> dict:
    """Cl(9,5) anchor version of the obstruction. Build the gamma-trace kernel
    projector P_+ on (R^14 tensor S^+), then check whether the RS symbol kills
    the projected pure-gauge image eps |-> P_+( xi tensor eps ).

    All matrices come from the verified Cl(9,5) rep; nothing is tuned to a target.
    """
    n_pairs = 7
    dim = 2 ** n_pairs
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = [+1] * 9 + [-1] * 5
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]
    Iden = np.eye(dim, dtype=complex)
    omega = Iden.copy()
    for a in range(14):
        omega = omega @ e[a]
    w, V = np.linalg.eigh(omega)
    Bplus = V[:, w > 0.5]    # 128 x 64  (S^+)
    Bminus = V[:, w < -0.5]  # 128 x 64  (S^-)

    # gamma-trace map Gamma : R^14 tensor S^+ -> S^- ,  (xi_a, psi) |-> sum xi_a c(e_a) psi
    blocks = [Bminus.conj().T @ e[a] @ Bplus for a in range(14)]  # each 64x64
    Gamma = np.hstack(blocks)                                     # 64 x 896
    # orthogonal projector onto ker(Gamma) in C^896
    gram = Gamma @ Gamma.conj().T
    P_plus = np.eye(Gamma.shape[1], dtype=complex) - Gamma.conj().T @ np.linalg.inv(gram) @ Gamma
    ker_rank_C = int(np.linalg.matrix_rank(P_plus, tol=cl95.TOL))

    # constrained RS symbol on the kernel: sigma(xi) = P_- c(xi) P_+   (S^- side projector)
    blocks_m = [Bplus.conj().T @ e[a] @ Bminus for a in range(14)]
    Gamma_m = np.hstack(blocks_m)
    gram_m = Gamma_m @ Gamma_m.conj().T
    P_minus = np.eye(Gamma_m.shape[1], dtype=complex) - Gamma_m.conj().T @ np.linalg.inv(gram_m) @ Gamma_m

    # c(xi) lifted to the vector-spinor space R^14 tensor S: block-diagonal c(xi) on each S^+ copy.
    # symbol mapping vector-spinor (896) -> vector-spinor (896): act c(xi)=sum xi_a e_a within S, per slot.
    cxi_S = np.zeros((dim, dim), dtype=complex)
    for a in range(14):
        cxi_S += xi[a] * e[a]
    # restrict c(xi): S^+ -> S^- then re-embed; build on the 64-dim chiral spaces
    cxi_pm = Bminus.conj().T @ cxi_S @ Bplus          # 64x64  (S^+ -> S^-)
    full_symbol = np.kron(np.eye(14, dtype=complex), cxi_pm)  # 896(S^- slots) x 896(S^+ slots)
    full_symbol = P_minus @ full_symbol @ P_plus

    # pure-gauge image  g_+(xi): eps in S^+ (C^64) |-> xi tensor eps in R^14 tensor S^+ (C^896)
    gauge = np.vstack([xi[a] * np.eye(64, dtype=complex) for a in range(14)])  # 896 x 64
    projected_gauge = P_plus @ gauge
    symbol_on_gauge = full_symbol @ projected_gauge
    return {
        "model": "Cl(9,5) = M(64,H) anchor",
        "ker_Gamma_rank_C": ker_rank_C,                       # 832
        "projected_gauge_rank_C": int(np.linalg.matrix_rank(projected_gauge, tol=cl95.TOL)),
        "RS_symbol_on_gauge_image_norm": float(np.linalg.norm(symbol_on_gauge)),
        "pure_gauge_annihilated_within_gamma_trace_kernel": bool(
            np.linalg.norm(symbol_on_gauge) < 1e-6),
    }


# ---------------------------------------------------------------------------
# Part C. The K3 index family (honest, no target-division). q stays SYMBOLIC.
# ---------------------------------------------------------------------------
def k3_index_complex(q: int, k: int, n: int = 16) -> int:
    AHAT, P1 = 2, -48
    return (4 + q) * n * AHAT + n * P1 + (4 + q) * k


# ---------------------------------------------------------------------------
# Part D. The assembly: try to build Pi_RS^phys and the decisive rank. Blocks at
# the first missing slot. The dependency DAG: gauge-fixing/ghost differential
# (d_RS,-1) defines Pi_RS^phys AND the ghost count q; without it nothing downstream
# is typed.
# ---------------------------------------------------------------------------
@dataclass
class RSGuPhysInputs:
    # what the repo + GU source actually supply:
    E_plus_projector: Optional[object] = "PINNED_rank_H_32"   # C2 of OQ-RK1: pinned
    gauge_symmetry_d_A: Optional[object] = "GU_DERIVED_shape_and_H_structure"  # C1 shape: pinned
    # what GU does NOT supply (all None == genuine gap):
    gauge_fixing_condition: Optional[object] = None           # C2: GU picks none
    ghost_BRST_differential_d_RS_minus_1: Optional[object] = None  # C1/C3: not source-derived
    ghost_subtraction_count_q: Optional[int] = None           # C3: q = 1 - a, undetermined
    gamma_trace_vs_gauge_reconciliation: Optional[object] = None   # machine-obstructed, no GU fix
    stabilized_RS_action: Optional[object] = None             # eq 10.10 author-disclaimed; lane uninhabited
    ch2_F_K3_value_k: Optional[int] = None                    # C4: background curvature
    H_linear_trace_certificate: Optional[object] = None       # C4: Tr_H
    Y14_K3_same_operator_bridge: Optional[object] = None       # C3/C4: transport


def assemble_RS_GU_phys(inp: RSGuPhysInputs) -> dict:
    """Attempt to instantiate Pi_RS^phys on a common right-H module and return
    rank_H(Pi_RS^phys . E_+ . Pi_RS^phys). Blocks on the first missing slot.

    Slot order = dependency DAG. The FIRST missing slot is the load-bearing gap.
    """
    required = [
        ("stabilized_RS_action", inp.stabilized_RS_action,
         "GU has no stabilized RS/IG-sector action: eq 10.10 is author-disclaimed "
         "('Caveat Emptor'); the 2021 draft 'does not emit a source action, operator, "
         "differential, Noether identity, or BRST rule' for d_RS,-1; the tau-action "
         "field-space declaration is uninhabited and FULL_IG/FIXED_ALEPH/DYNAMIC_A "
         "is source-unselected. Without the action it is not even well-posed whether "
         "the spinor 1-form is pure gauge, dynamical, or constrained."),
        ("gauge_fixing_condition", inp.gauge_fixing_condition,
         "GU picks NO gauge slice; 'without making any choices' retains the full IG. "
         "Needed because (machine fact) im(d_A) is NOT inside ker(Gamma), so R^phys is "
         "not a subspace subtraction."),
        ("ghost_BRST_differential_d_RS_minus_1", inp.ghost_BRST_differential_d_RS_minus_1,
         "the source-defined gauge/BRST differential that would define Pi_RS^phys."),
        ("ghost_subtraction_count_q", inp.ghost_subtraction_count_q,
         "q = 1 - a: selects the physical member E(q)=(V+q)F; not source-derived."),
        ("gamma_trace_vs_gauge_reconciliation", inp.gamma_trace_vs_gauge_reconciliation,
         "how GU's definitional gamma-trace irreducibility reconciles with the gauge "
         "symmetry whose image escapes it; GU asserts an 'elliptic deformation complex "
         "after redundant EL equations discarded' (p.65) but never constructs it."),
        ("ch2_F_K3_value_k", inp.ch2_F_K3_value_k, "k = ch_2(F)[K3] background curvature."),
        ("H_linear_trace_certificate", inp.H_linear_trace_certificate, "global Tr_H (rank_C -> rank_H)."),
        ("Y14_K3_same_operator_bridge", inp.Y14_K3_same_operator_bridge, "Y14<->K3 transport."),
    ]
    missing = [(n, why) for n, v, why in required if v is None]
    if missing:
        first_name, first_why = missing[0]
        return {
            "status": "BLOCKED_NEEDS_SPEC",
            "decisive_rank_H_Pi_E_Pi": "NOT_COMPUTABLE",
            "single_load_bearing_gap": first_name,
            "single_load_bearing_reason": first_why,
            "all_missing_slots": [m[0] for m in missing],
        }
    raise RuntimeError("Unreachable: no GU source data fills these slots; reaching this "
                       "branch would require fabricating the BRST quotient (FC4-HOLONOMY-01).")


def main() -> dict:
    report = {}

    # --- Part A: origin classification table ------------------------------
    report["origin_classification"] = [
        {"component": c.name, "specifiable": c.specifiable,
         "gu_derived": c.gu_derived, "textbook_import": c.textbook_import,
         "genuine_gu_gap": c.genuine_gu_gap}
        for c in FOUR_COMPONENTS
    ]

    # --- Part B: independently re-verify the obstruction (toy + anchor) ----
    obs_toy = obstruction_cl4()
    obs_anchor = obstruction_cl95()
    report["load_bearing_obstruction"] = {
        "claim": "pure-gauge image im(d_A) is NOT annihilated within the gamma-trace kernel",
        "cl4_toy": obs_toy,
        "cl95_anchor": obs_anchor,
        "consequence": ("R^phys != ker(Gamma)/im(gauge) as a subspace difference; a genuine "
                        "gauge-fixing + ghost/BRST complex is REQUIRED, not optional."),
    }

    # --- Part C: honest K3 index, q symbolic -------------------------------
    report["k3_index_family"] = {
        "form": "ind_C = (-40+2q)*16 + (4+q)*k ; ind_H = ind_C/2 (conditional Tr_H)",
        "flat_control_k0": {
            "q=0": k3_index_complex(0, 0), "q=+1": k3_index_complex(1, 0),
            "q=-1": k3_index_complex(-1, 0),
        },
        "flat_control_k0_ind_H": {
            "q=0": k3_index_complex(0, 0) / 2, "q=+1": k3_index_complex(1, 0) / 2,
            "q=-1": k3_index_complex(-1, 0) / 2,
        },
        "note": "k left SYMBOLIC/unfixed; flat k=0 is an imported control, not proven.",
    }

    # --- Part D: the assembly attempt with GU-supplied (mostly-None) inputs -
    report["assembly"] = assemble_RS_GU_phys(RSGuPhysInputs())

    # --- forbidden moves: documented, NOT executed ------------------------
    report["forbidden_moves_not_executed"] = {
        "INVALID_TARGET_DIVISION": "rank_eff := ind_H/Ahat(K3) = 8/2 = 4  (REFUSED)",
        "target_index_insertion": "ind_H(D_RS) := 8  (REFUSED)",
    }

    # --- does any honest number equal 4 or 8? -----------------------------
    honest_numbers = {
        "E_plus_rank_H": 32.0,
        "raw_cl95_kernel_rank_H": 416.0,
        "cl4_toy_Pi_raw_E_Pi_raw_rank_H": 48.0,
        "k3_ind_H_flat_q0": k3_index_complex(0, 0) / 2,
        "k3_ind_H_flat_qp1": k3_index_complex(1, 0) / 2,
        "k3_ind_H_flat_qm1": k3_index_complex(-1, 0) / 2,
    }
    report["honest_numbers"] = honest_numbers
    report["any_honest_number_equals_4_or_8"] = any(v in (4, 8) for v in honest_numbers.values())

    # --- print -------------------------------------------------------------
    print("=" * 80)
    print("RS_GU^phys ASSEMBLY + ORIGIN DETERMINATION (four justified sub-structures)")
    print("=" * 80)
    print("\nORIGIN of each piece (gu_derived / textbook_import / genuine_gu_gap):")
    for c in FOUR_COMPONENTS:
        print(f"  [{c.specifiable:>9}] {c.name}")
    print("\nLOAD-BEARING OBSTRUCTION (independently re-verified this run):")
    print("  Cl(4,0) toy : RS symbol on pure-gauge image norm = {:.2f}  -> annihilated? {}".format(
        obs_toy["RS_symbol_on_gauge_image_norm"],
        obs_toy["pure_gauge_annihilated_within_gamma_trace_kernel"]))
    print("  Cl(9,5) anc : RS symbol on pure-gauge image norm = {:.2f}  -> annihilated? {}".format(
        obs_anchor["RS_symbol_on_gauge_image_norm"],
        obs_anchor["pure_gauge_annihilated_within_gamma_trace_kernel"]))
    print("  => im(d_A) escapes ker(Gamma): a genuine gauge-fixing+ghost complex is REQUIRED.")
    print("\nK3 index (q symbolic), flat k=0: ind_H = {q0}, {qp}, {qm} for q=0,+1,-1".format(
        q0=k3_index_complex(0, 0) / 2, qp=k3_index_complex(1, 0) / 2, qm=k3_index_complex(-1, 0) / 2))
    print("\nANY honest number equal to 4 or 8? {}".format(report["any_honest_number_equals_4_or_8"]))
    print("ASSEMBLY STATUS : {}".format(report["assembly"]["status"]))
    print("decisive rank_H(Pi_RS.E_+.Pi_RS) : {}".format(report["assembly"]["decisive_rank_H_Pi_E_Pi"]))
    print("SINGLE load-bearing gap : {}".format(report["assembly"]["single_load_bearing_gap"]))
    print("  -> {}".format(report["assembly"]["single_load_bearing_reason"]))
    print("4/8 reachable ONLY via forbidden 8/Ahat(K3)=8/2 (INVALID_TARGET_DIVISION) -> REFUSED")
    print("=" * 80)
    print("\nMACHINE JSON:")
    print(json.dumps(report, indent=2, default=str))
    return report


if __name__ == "__main__":
    main()
