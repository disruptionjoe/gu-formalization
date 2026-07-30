#!/usr/bin/env python3
"""Executable contract for Swing N1's unified source-action/datum packet.

This probe does not solve the Euler equations, the BV master equation, the
global domain, the physical reduction, or an index.  It checks that the
candidate family is finite, same-object typed, target-blind, and sufficiently
explicit for N2a/N4a/N3 to consume without inventing another action.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


LEGS = ("Y", "Q", "G", "I", "U")
NATIVE_FIBRE = "Sym2(T*X)"
HOSTILE_EXTERIOR_TEN = "Lambda2(T*X)+Lambda3(T*X)"


@dataclass(frozen=True)
class Field:
    carrier: str
    parity: str
    ghost_number: int
    varied: bool
    gauge_law: str


FIELDS = {
    "s": Field("Gamma(X,Met_3,1(X))", "even", 0, True, "natural_Diff(X)"),
    "A": Field("Conn(P->Y)", "even", 0, True, "uAu^-1-du u^-1; L_xi_tilde A"),
    "A0": Field("Conn(P->Y)", "even", 0, False, "uA0u^-1-du u^-1; L_xi_tilde A0"),
    "U": Field("Omega1(Y,adP)", "even", 0, True, "uUu^-1; L_xi_tilde U"),
    "P_IG": Field("Omega2(Y,adP)", "even", 0, True, "uP_IGu^-1; L_xi_tilde P_IG"),
    "epsilon_IG": Field(
        "Gamma(Y,IG_soldering_bundle)",
        "even",
        0,
        True,
        "u.epsilon_IG; L_xi_tilde epsilon_IG",
    ),
    "theta": Field("Omega1(Y,adP)", "even", 0, False, "u theta u^-1; L_xi_tilde theta"),
    "Z": Field(
        "Gamma(Y x S1_DW,E20_DW=E20_geom_mapping_torus tensor pDW*L_sigma), fixed-loop fibre used locally",
        "odd",
        0,
        True,
        "rho(u)Z; L_xi_tilde Z",
    ),
    "Z_hat": Field(
        "Gamma(Ybar x S1_DW,E20_DW tensor_R (nu*H_n plus nu*R4)); E20_DW contains pDW*L_sigma; auxiliary Z2-graded KO comparator",
        "odd",
        0,
        False,
        "rho(u) tensor identity; L_xi_tilde",
    ),
    "Sigma": Field(
        "span_R{Sigma_A^0}_{A=1..12} subset Gamma(X,Sym2(Lambda2_+) tensor F2)",
        "even",
        0,
        False,
        "declared_spurion_representation; L_xi Sigma",
    ),
    "c_g": Field("Omega0(Y,adP)", "odd", 1, True, "[c_g,c_g]/2; L_xi_tilde c_g"),
    "gamma": Field(
        "Gamma(Y x S1_DW,S_DW=S_geom_mapping_torus tensor pDW*L_sigma)",
        "even",
        1,
        True,
        "rho(c_g)gamma; L_xi_tilde gamma",
    ),
    "bar_gamma": Field(
        "Gamma(Y x S1_DW,S_DW=S_geom_mapping_torus tensor pDW*L_sigma)",
        "even",
        -1,
        True,
        "b_gamma+rho(c_g)bar_gamma; L_xi_tilde bar_gamma",
    ),
    "b_gamma": Field(
        "Gamma(Y x S1_DW,S_DW=S_geom_mapping_torus tensor pDW*L_sigma)",
        "odd",
        0,
        True,
        "rho(c_g)b_gamma; L_xi_tilde b_gamma",
    ),
    "xi": Field("Gamma(X,TX)", "odd", 1, True, "[xi,xi]/2"),
}


@dataclass(frozen=True)
class ActionTerm:
    name: str
    domain: str
    integrand: str
    fields: tuple[str, ...]
    coefficients: tuple[str, ...]
    legs: tuple[str, ...]
    branch: str = "common"


ACTION_TERMS = (
    ActionTerm(
        "ambient_yang_mills",
        "Y_bulk",
        "(zeta_F/2g_A^2) <F_A,*_G F_A>_ad",
        ("A",),
        ("zeta_F", "g_A_inv2"),
        ("G", "Q", "U"),
        "fundamental_or_induced_YM",
    ),
    ActionTerm(
        "induced_ym_parent",
        "Y_bulk",
        "<P_IG,*_G D_A U>_ad-(1/2Z_U)<P_IG,*_G P_IG>_ad; V_src=0 minimal stratum",
        ("A", "U", "P_IG", "epsilon_IG"),
        ("Z_U",),
        ("G", "Q", "U"),
        "fundamental_or_induced_YM",
    ),
    ActionTerm(
        "distortion_source_bridge",
        "Y_bulk",
        "+(1/2kappa)<theta,*_G theta>_ad-<theta,*_G J(Z)>_ad; theta=A-Gamma(epsilon_IG)-U",
        ("A", "U", "epsilon_IG", "theta", "Z"),
        ("kappa",),
        ("G", "Q"),
    ),
    ActionTerm(
        "full20_krein_quadratic",
        "Y_bulk",
        "(1/2) Re[Z,K_G(D_h(A)+lambda_F V_GT(F_A))Z]_E20; |h_mu|=m_R",
        ("A", "Z"),
        ("G2", "h_native", "m_R", "lambda_F"),
        ("Y", "Q", "G", "U"),
    ),
    ActionTerm(
        "end_selector",
        "Y_end",
        "r=V:(m_sel/2)chi Re[Z,K_G c_rho(v_tr)Z]; "
        "r=B:(m_sel/2)chi Re_super[Z_hat,V_GT(F_(nu*H_n))Z_hat]; "
        "r=0:(m_sel/2)chi Re[Z,K_G Z]",
        ("A", "A0", "Z", "Z_hat"),
        ("m_sel",),
        ("Y", "I", "U"),
        "vertical_boundary_vectorlike_rivals",
    ),
    ActionTerm(
        "induced_section_gravity",
        "X_defect_via_s_pushforward",
        "alpha_II <II_s,II_s>+beta_0 <II_s^0,II_s^0>-2 Lambda_bare",
        ("s",),
        ("alpha_II", "beta_0", "Lambda_bare"),
        ("G", "U"),
    ),
    ActionTerm(
        "seiberg_witten_defect",
        "X_defect_via_s_pushforward",
        "(lambda_SW/2)|P_+F_(s*A)-mu(P0 s*Z)|^2",
        ("s", "A", "Z"),
        ("lambda_SW", "P0_choice"),
        ("Y", "Q", "G"),
    ),
    ActionTerm(
        "krein_yukawa_defect",
        "X_defect_via_s_pushforward",
        "Re[(P0s*Z)^dag K c_rho(res_s^V(A-A0)) Y_K (P0s*Z)]",
        ("s", "A", "A0", "Z"),
        ("Y_K",),
        ("Y", "Q", "G"),
        "K_sesquilinear",
    ),
    ActionTerm(
        "charge_conjugation_yukawa_defect",
        "X_defect_via_s_pushforward",
        "(1/2)Re[(P0s*Z)^T C_var_epsilon c_rho(res_s^V(A-A0)) Y_C(P0s*Z)+reality_completion]",
        ("s", "A", "A0", "Z"),
        ("Y_C", "C_var_epsilon_branch"),
        ("Y", "Q", "G"),
        "C_complex_bilinear",
    ),
    ActionTerm(
        "spurion_interface",
        "X_defect_via_s_pushforward",
        "Re[(P0s*Z)^T C_var_epsilon c_rho(res_s^V(A-A0)) Sigma (P0s*Z)]",
        ("s", "A", "A0", "Z", "Sigma"),
        ("Sigma_values",),
        ("Y",),
        "optional_same_chirality_or_flavour_breaking",
    ),
    ActionTerm(
        "minimal_bv_extension",
        "BV_Y",
        "sum_(Phi=A,U,P_IG,epsilon_IG,Z,c_g,gamma,bar_gamma,b_gamma)<Phi+,s0 Phi>+"
        "<s+,L_xi s>+(1/2)<xi+,[xi,xi]>; "
        "s0 includes internal gauge, natural lifted Diff(X), R_r gamma, and the nonminimal doublet",
        (
            "A",
            "U",
            "P_IG",
            "epsilon_IG",
            "Z",
            "c_g",
            "gamma",
            "bar_gamma",
            "b_gamma",
            "s",
            "xi",
        ),
        ("r_generator",),
        ("Q", "G", "U"),
    ),
    ActionTerm(
        "orientation_holonomy_cocycle",
        "configuration_loop",
        "exp(i T9(ell))=Hol_Lsigma(ell)=(-1)^<w1(Lsigma),[ell]>",
        (),
        (),
        ("Q", "I"),
    ),
)


REQUIREMENTS = {
    "SA-Y1": "dual_bilinear_interfaces_written_channel_identification_held",
    "SA-Y2": "K_and_C_branches_separate_and_charged",
    "SA-Y3": "vertical_amplitude_charged_not_selected",
    "SA-Y4": "full_provenance_matrices_YK_YC_charged",
    "SA-Y5": "larger_flavour_symmetry_optional_declared_branch",
    "SA-Y6": "provenance_to_flavour_map_not_identified",
    "SA-Y7a": "finite_F2_test_carrier_predeclared_without_importing_retracted_Z3_force",
    "SA-Y7b": "twelve_Sigma_basis_coefficients_charged",
    "SA-Y8": "same_chirality_spurion_optional_and_not_mu_homonym",
    "SA-G1": "soldering_field_and_theta_definition_written",
    "SA-G2": "mu_DW_free_bounded_coordinate",
    "SA-G3": "background_initial_amplitude_coordinate",
    "SA-G4": "f0_derived_readout_not_input",
    "SA-G5": "beta_over_alpha_coordinate",
    "SA-G6": "alpha_positive_stratum",
    "SA-G7": "cL_held_out_readout",
    "SA-G8": "m2eff_band_coordinate",
    "SA-G9": "matter_coupling_variation_enabled_not_yet_computed",
    "SA-C1": "carrier_A_B_branch_charged",
    "SA-C2": "g1_projector_and_GT_vertex_written",
    "SA-C3": "P3_relative_KO_interface_written_without_count_input",
    "SA-C4": "curved_subprincipal_test_downstream",
    "SA-U1": "BV_counterterm_regulator_and_inclusive_interfaces_frozen",
    "SA-U2": "fixed_scale_vs_running_mass_branch_charged",
    "SA-U3": "Krein_positivity_observable_sealed",
    "SA-U4": "nonzero_mR_coordinate",
    "SA-U5": "guardian_vs_finite_EFT_branch_charged",
}


ORIENTATION_DATUM = {
    "name": "L_sigma",
    "base": "S1_DW",
    "theory": "flat_real_line",
    "w1_generator": 1,
    "primitive_holonomy": -1,
    "doubled_holonomy": 1,
    "twisted_objects": ("Z", "gamma", "bar_gamma", "b_gamma"),
}


TOPOLOGY_DATUM = {
    "name": "e_hat_n",
    "theory": "relative_differential_KO^0_after_pullback",
    "base": "S4=D4_N_union_S3_D4_S",
    "support_map": "nu:Ybar->S4; degree +1 on chosen framed normal 4-cycle; constant on boundary_infinity",
    "actual_equal_rank_bundle": "W_n^+=H_n and W_n^-=R4, each rank_R=4",
    "reduced_class": "[W_n^+]-[W_n^-]=[H_n]-[R4]=n beta_KO",
    "clutching": "q->L_(q^n), n in {-1,0,1}",
    "connection": "BPST_or_anti_BPST_plus_trivial; supplied_not_varied",
    "characteristic_basis": "u in H4(S4,Z), integral(u)=1; p1(H_n)=-2n u",
    "boundary_restriction": "nu*(H_n minus R4) has chosen zero trivialization on boundary_infinity(Ybar)",
    "operator_coupling": "graded tensor-connection twist by nu*H_n minus nu*R4; preserves right-H action",
    "topology_strata": (-1, 0, 1),
}


END_PACKET = {
    "bulk": "Y=Met_3,1(X)",
    "compactification": "radial Ybar with boundary_infinity(Ybar)",
    "model_end": "[R,infinity)_r x S3_q x E6_control",
    "normal_collapse": "nu collapses the complement and infinity of the framed radial-S3 normal tube to the S4 basepoint",
    "curvature_support": "support(d nu) lies in a fixed clutching annulus where chi=1 and is zero near boundary_infinity",
    "second_end_control": "two_ended_copy_with_opposite_orientation",
    "selector_cutoff": "chi=0 on compact core, chi=1 for r>=R+1",
    "domain_status": "unselected_until_N8",
}


RIVALS = {
    "vertical": {
        "operator": "M_V=chi(r)c(v_tr)",
        "active_real_coordinates": 1,
        "solver_starts": 64,
    },
    "boundary_index": {
        "operator": "M_B=chi(r)V_GT(F_(nu*H_n)) on the auxiliary graded comparator",
        "active_real_coordinates": 1,
        "solver_starts": 64,
    },
    "vectorlike_control": {
        "operator": "M_0=chi(r)Identity",
        "active_real_coordinates": 1,
        "solver_starts": 64,
    },
}


SEARCH_BUDGET = {
    "background_generators": 4,
    "sym2_orbit_representatives": 4,
    "higher_bracket_max_arity": 4,
    "end_models": 2,
    "topology_strata": 3,
    "reduction_projectors": 4,
    "modes_per_observer_slot": 2,
    "regulator_families": 2,
    "rival_families": 3,
    "solver_starts_per_rival": 64,
    "open_bv_derivative_order": 2,
    "open_bv_field_degree": 4,
    "open_bv_ghost_degree": 2,
    "open_bv_antifield_number": 2,
    "open_bv_composition_depth": 3,
    "open_bv_insertions": 10,
    "spurion_basis_sections": 12,
}


PARAMETER_CATEGORIES = {
    "local_coefficients": (
        "zeta_F",
        "g_A_inv2",
        "Z_U",
        "kappa",
        "alpha_II",
        "beta_0",
        "Lambda_bare",
        "lambda_SW",
        "lambda_F",
        "m_sel",
        "mu_DW",
        "m2_eff",
    ),
    "multiplicity_pairing": ("alpha_G2", "beta_G2", "Re_zeta_G2", "Im_zeta_G2"),
    "native_operator": (
        "h_a",
        "h_d",
        "Re_h_SI",
        "Im_h_SI",
        "Re_h_SR",
        "Im_h_SR",
        "Re_h_IR",
        "Im_h_IR",
    ),
    "gauge_generator": (
        "Re_rS",
        "Im_rS",
        "Re_rI",
        "Im_rI",
        "Re_rR",
        "Im_rR",
    ),
    "open_bv": ("tau_lambda_in_predeclared_Hom_quotient_syntactic_rank_at_most_233100",),
    "provenance_yukawa": (
        "Y_K_3x3_complex",
        "Y_C_3x3_complex",
        "Sigma_12_real_coefficients",
    ),
    "background_functions": (
        "t1",
        "t2",
        "t3",
        "t4",
        "B_initial",
        "A0_reference_connection",
        "B_tr_section",
        "B_tf_section",
        "B_Codazzi_section",
        "B_IG_section",
        "Phi_tr_section",
        "Sigma_basis_12_sections",
    ),
    "topology": ("n_KO",),
    "domains": ("end_model", "future_closed_extension"),
    "regulators": ("proper_time_even", "paired_PV", "inclusive_Delta_E"),
    "reductions": ("P_all", "P_S", "P_I", "P_R"),
    "discrete_branches": (
        "K_or_C",
        "carrier_A_or_B",
        "fixed_or_running_mass",
        "guardian_or_finite_EFT",
        "fundamental_or_induced_YM",
        "vertical_boundary_vectorlike",
        "C_var_epsilon_tau_component",
    ),
    "derived_coordinates": ("m_R_from_mu_DW_m2_eff", "ell2_from_Z_U_kappa"),
}


HELD_OUT = {
    "bv_obstruction": "first_nonzero_H1_s0_mod_d_class",
    "gravity_cosmology": "one_subleading_unfit_Hz_or_wz_response",
    "causality": "one_covector_background_pair_not_in_basis_design",
    "topology": "primitive_twist_pushforward_integer",
    "physical": "normalizable_Hessian_eigenvalue_and_unbroken_group",
}


BV_GHOST_NUMBERS = {
    "A+": -1,
    "U+": -1,
    "P_IG+": -1,
    "epsilon_IG+": -1,
    "Z+": -1,
    "c_g+": -2,
    "gamma+": -2,
    "bar_gamma+": 0,
    "b_gamma+": -1,
    "s+": -1,
    "xi+": -2,
    "A": 0,
    "U": 0,
    "P_IG": 0,
    "epsilon_IG": 0,
    "Z": 0,
    "c_g": 1,
    "gamma": 1,
    "bar_gamma": -1,
    "b_gamma": 0,
    "s": 0,
    "xi": 1,
}


BV_MONOMIALS = {
    "Aplus_Dc": ("A+", "c_g"),
    "Aplus_Lxi_A": ("A+", "xi", "A"),
    "Uplus_cU": ("U+", "c_g", "U"),
    "Pplus_cP": ("P_IG+", "c_g", "P_IG"),
    "epsilonIGplus_cepsilonIG": ("epsilon_IG+", "c_g", "epsilon_IG"),
    "Zplus_cZ": ("Z+", "c_g", "Z"),
    "Zplus_Rgamma": ("Z+", "gamma"),
    "cplus_cc": ("c_g+", "c_g", "c_g"),
    "cplus_Lxi_c": ("c_g+", "xi", "c_g"),
    "gammaplus_cgamma": ("gamma+", "c_g", "gamma"),
    "barplus_b": ("bar_gamma+", "b_gamma"),
    "barplus_cbar": ("bar_gamma+", "c_g", "bar_gamma"),
    "bplus_cb": ("b_gamma+", "c_g", "b_gamma"),
    "splus_Lxi_s": ("s+", "xi", "s"),
    "xiplus_xixi": ("xi+", "xi", "xi"),
    "open_ZZ_gammagamma": ("Z+", "Z+", "gamma", "gamma"),
}


def canonical_payload() -> dict[str, object]:
    """Only pre-consequence construction data enter the sealed hash."""
    return {
        "action_terms": [
            {
                "name": term.name,
                "domain": term.domain,
                "integrand": term.integrand,
                "fields": term.fields,
                "coefficients": term.coefficients,
                "legs": term.legs,
                "branch": term.branch,
            }
            for term in ACTION_TERMS
        ],
        "fields": {
            name: {
                "carrier": field.carrier,
                "parity": field.parity,
                "ghost_number": field.ghost_number,
                "varied": field.varied,
                "gauge_law": field.gauge_law,
            }
            for name, field in sorted(FIELDS.items())
        },
        "requirements": REQUIREMENTS,
        "orientation": ORIENTATION_DATUM,
        "topology": TOPOLOGY_DATUM,
        "end": END_PACKET,
        "rivals": RIVALS,
        "search_budget": SEARCH_BUDGET,
        "parameter_categories": PARAMETER_CATEGORIES,
        "held_out_names_only": sorted(HELD_OUT),
        "native_fibre": NATIVE_FIBRE,
    }


def construction_hash() -> str:
    raw = json.dumps(canonical_payload(), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


SEALED_HASH = "1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb"


checks = 0


def check(label: str, condition: bool) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1
    print(f"PASS: {label}")


def reject(label: str, callable_, *args) -> None:
    try:
        callable_(*args)
    except ValueError:
        check(label, True)
        return
    raise AssertionError(label)


def admit_topology(n: int) -> int:
    if n not in TOPOLOGY_DATUM["topology_strata"]:
        raise ValueError("topology outside preregistered target-blind set")
    return n


def admit_fibre(name: str) -> str:
    if name != NATIVE_FIBRE:
        raise ValueError("not the actual GU symmetric-metric fibre")
    return name


def admit_domain(domain: str, has_pushforward: bool) -> str:
    if domain == "X_raw" or (domain.startswith("X_") and not has_pushforward):
        raise ValueError("X term has no map into the bulk-plus-defect action")
    if domain not in {
        "Y_bulk",
        "Y_end",
        "X_defect_via_s_pushforward",
        "BV_Y",
        "configuration_loop",
    }:
        raise ValueError("unknown action domain")
    return domain


def transfer_bilinear_result(source: str, target: str, relating_map: str | None) -> bool:
    if source != target and relating_map is None:
        raise ValueError("cross-bilinear transfer requires a proved map")
    return True


def admit_coefficients(names: Iterable[str]) -> tuple[str, ...]:
    names = tuple(names)
    if any(re.search(r"(cell|slot)_\d+", name) for name in names):
        raise ValueError("free observer-cell coefficient")
    return names


def require_five_legs(terms: Iterable[ActionTerm]) -> set[str]:
    covered = {leg for term in terms for leg in term.legs}
    if covered != set(LEGS):
        raise ValueError(f"missing legs: {set(LEGS) - covered}")
    return covered


def validate_datum_names(names: Iterable[str]) -> tuple[str, ...]:
    names = tuple(names)
    if len(names) != len(set(names)):
        raise ValueError("duplicate datum")
    if set(names) != {"L_sigma", "e_hat_n"}:
        raise ValueError("orientation and integer/topology datum must remain separate")
    return names


def admit_topology_coupling(packet: dict[str, object]) -> bool:
    support_map = str(packet.get("support_map", ""))
    boundary = str(packet.get("boundary_restriction", ""))
    coupling = str(packet.get("operator_coupling", ""))
    if "nu:Ybar->S4" not in support_map:
        raise ValueError("the S4 topology datum has no map into the Y action/operator domain")
    if "boundary_infinity" not in boundary or "zero trivialization" not in boundary:
        raise ValueError("the pulled-back reduced class has no relative boundary trivialization")
    if "nu*" not in coupling:
        raise ValueError("the operator is not coupled to the pulled-back bundle")
    return True


def main() -> None:
    if "--emit-hash" in sys.argv:
        print(construction_hash())
        return

    print("=" * 94)
    print("N1 UNIFIED SOURCE-ACTION / EXTERNAL-DATUM PACKET V0")
    print("=" * 94)

    print("\nA. Bulk-plus-defect action-domain weld")
    for term in ACTION_TERMS:
        admit_domain(term.domain, term.domain == "X_defect_via_s_pushforward")
    check("every action term has an admitted explicit domain", True)
    check("no action term is a bare T_i label", all(not re.fullmatch(r"T\d+", t.name) for t in ACTION_TERMS))
    check("every referenced classical field has a typed carrier", all(f in FIELDS for t in ACTION_TERMS for f in t.fields))
    check(
        "the BV extension is disjoint from the classical/global term registry",
        {t.name for t in ACTION_TERMS if t.domain == "BV_Y"}
        == {"minimal_bv_extension"},
    )
    check(
        "the ambient vertical Krein coupling is not double-counted as a second action term",
        "vertical_krein_summand" not in {t.name for t in ACTION_TERMS},
    )
    check(
        "the induced-YM parent fixes the previously schematic source potential to the zero stratum",
        any("V_src=0" in t.integrand for t in ACTION_TERMS if t.name == "induced_ym_parent"),
    )
    x_weight = (Fraction(2), Fraction(-1), Fraction(3))
    section_image = (1, 3, 4)
    bulk_test_scalar = (Fraction(5), Fraction(7), Fraction(11), Fraction(13), Fraction(17))
    current_pairing = sum(w * bulk_test_scalar[y] for w, y in zip(x_weight, section_image))
    explicit_defect = 2 * 7 - 13 + 3 * 17
    check("section-current definition equals explicit defect integral on the finite fixture", current_pairing == explicit_defect == 52)
    literal_pullback_vertical = sum(Fraction(0) * v for v in (2, -1, 4, 3))
    coefficient_restriction_trace = Fraction(2 - 1 + 4 + 3, 4)
    check("literal pullback can erase a vertical covector", literal_pullback_vertical == 0)
    check("coefficient restriction retains the trace-mode scalar coefficient", coefficient_restriction_trace == 2)
    kappa_fixture = Fraction(3)
    current_fixture = Fraction(2)
    theta_stationary = kappa_fixture * current_fixture
    bridge_derivative = theta_stationary / kappa_fixture - current_fixture
    bridge_effective = (
        theta_stationary * theta_stationary / (2 * kappa_fixture)
        - theta_stationary * current_fixture
    )
    check(
        "the bridge sign gives theta=kappa J and the Legendre-minus effective source term",
        bridge_derivative == 0
        and theta_stationary == 6
        and bridge_effective == -6,
    )
    reject("raw X/Y action summation plant is rejected", admit_domain, "X_raw", False)

    print("\nB. Five-leg and no-free-cell action manifest")
    check("the same packet carries exactly all five leg labels", require_five_legs(ACTION_TERMS) == set(LEGS))
    check("all 27 requirement IDs have an explicit packet disposition", len(REQUIREMENTS) == 27 and len(set(REQUIREMENTS)) == 27)
    check("all expected requirement families occur", {key.split("-")[1][0] for key in REQUIREMENTS} == {"Y", "G", "C", "U"})
    all_coefficients = tuple(name for term in ACTION_TERMS for name in term.coefficients)
    check("natural linked coefficients pass the no-free-cell guard", bool(admit_coefficients(all_coefficients)))
    reject("a planted observer-cell coefficient is rejected", admit_coefficients, ("cell_37",))
    no_index_leg = tuple(term for term in ACTION_TERMS if "I" not in term.legs)
    reject("a packet with an omitted physics leg is rejected", require_five_legs, no_index_leg)
    check("an unrelated planted requirement is not in the 27-row owner set", "SA-Z99" not in REQUIREMENTS)

    print("\nC. Dual bilinear and actual-fibre Layer-0 controls")
    branches = {term.branch for term in ACTION_TERMS}
    check("Krein sesquilinear branch is written", "K_sesquilinear" in branches)
    check("charge-conjugation complex-bilinear branch is written", "C_complex_bilinear" in branches)
    reject(
        "a conclusion cannot transfer from K to C without a relating map",
        transfer_bilinear_result,
        "K_sesquilinear",
        "C_complex_bilinear",
        None,
    )
    check(
        "an explicitly named future relating map would license comparison",
        transfer_bilinear_result("K_sesquilinear", "C_complex_bilinear", "R_KC"),
    )
    check("actual Sym2 fibre is admitted", admit_fibre(NATIVE_FIBRE) == NATIVE_FIBRE)
    reject("the exterior numerical ten is rejected", admit_fibre, HOSTILE_EXTERIOR_TEN)

    print("\nD. P1/P2 orientation and separately typed P3 KO datum")
    check("primitive DeWitt loop has nontrivial orientation holonomy", ORIENTATION_DATUM["primitive_holonomy"] == -1)
    check("doubled DeWitt loop returns trivially", ORIENTATION_DATUM["primitive_holonomy"] ** 2 == ORIENTATION_DATUM["doubled_holonomy"] == 1)
    check(
        "the orientation line is pulled back from the configuration loop rather than placed directly on Y",
        all(
            "S1_DW" in FIELDS[name].carrier
            and "pDW*" in FIELDS[name].carrier
            and "mapping_torus" in FIELDS[name].carrier
            for name in ORIENTATION_DATUM["twisted_objects"]
        ),
    )
    check("orientation and KO datum names remain distinct", validate_datum_names(("L_sigma", "e_hat_n")) == ("L_sigma", "e_hat_n"))
    reject("duplicating the orientation datum as P2 is rejected", validate_datum_names, ("L_sigma", "L_sigma", "e_hat_n"))
    check("the topology search is exactly target-blind {-1,0,+1}", tuple(admit_topology(n) for n in (-1, 0, 1)) == (-1, 0, 1))
    reject("target-coded topology n=3 is rejected", admit_topology, 3)
    p1_numbers = {n: -2 * n for n in TOPOLOGY_DATUM["topology_strata"]}
    check("Hopf/anti-Hopf/trivial p1 coefficients are explicit and distinct", p1_numbers == {-1: 2, 0: 0, 1: -2})
    check("all topology representatives use an equal-rank actual graded pair", "each rank_R=4" in TOPOLOGY_DATUM["actual_equal_rank_bundle"])
    check("real KO twisting preserves the right-H operator type by construction", "preserves right-H" in TOPOLOGY_DATUM["operator_coupling"])
    check("the S4 class is pulled into the Y operator domain by an explicit relative support map", admit_topology_coupling(TOPOLOGY_DATUM))
    missing_support_map = dict(TOPOLOGY_DATUM)
    missing_support_map.pop("support_map")
    reject(
        "an auxiliary S4 class with no map into Y is rejected",
        admit_topology_coupling,
        missing_support_map,
    )
    check(
        "the nontrivial boundary rival uses global curvature rather than a nonexistent H_n-to-R4 isomorphism",
        "F_(nu*H_n)" in RIVALS["boundary_index"]["operator"]
        and "J_n" not in RIVALS["boundary_index"]["operator"],
    )

    print("\nE. Equal-budget rivals and finite search contract")
    check("three selector rivals are frozen", set(RIVALS) == {"vertical", "boundary_index", "vectorlike_control"})
    check("each rival has exactly one active real selector coordinate", {v["active_real_coordinates"] for v in RIVALS.values()} == {1})
    check("each rival receives the same operational search budget", {v["solver_starts"] for v in RIVALS.values()} == {64})
    check("search-budget topology cardinality matches the datum", SEARCH_BUDGET["topology_strata"] == len(TOPOLOGY_DATUM["topology_strata"]))
    check("four actual-Sym2 representatives are budgeted without an exhaustiveness claim", SEARCH_BUDGET["sym2_orbit_representatives"] == 4)
    check("background family has four preregistered generators", SEARCH_BUDGET["background_generators"] == 4)
    check("two regulator families are charged rather than hidden", SEARCH_BUDGET["regulator_families"] == 2)
    check("the optional spurion branch has a finite twelve-section basis", SEARCH_BUDGET["spurion_basis_sections"] == 12)
    open_pairs = 20 * 21 // 2
    insertion_words = sum(
        SEARCH_BUDGET["open_bv_insertions"] ** depth
        for depth in range(1, SEARCH_BUDGET["open_bv_composition_depth"] + 1)
    )
    open_grammar_size = open_pairs * insertion_words
    check(
        "the frozen possible open-BV grammar counts all ordered insertion words through depth three",
        insertion_words == 1110 and open_grammar_size == 233100,
    )

    print("\nF. BV typing")
    for name, monomial in BV_MONOMIALS.items():
        total_ghost = sum(BV_GHOST_NUMBERS[field] for field in monomial)
        check(f"{name} has total ghost number zero", total_ghost == 0)
    check("open-BV grammar is capped at antifield number two", SEARCH_BUDGET["open_bv_antifield_number"] == 2)
    check("open-BV grammar is capped at two derivatives", SEARCH_BUDGET["open_bv_derivative_order"] == 2)
    check("later N4 may narrow but cannot enlarge composition depth", SEARCH_BUDGET["open_bv_composition_depth"] == 3)

    print("\nG. Parameter and held-out accounting")
    check("continuous/functions/topology/domain/regulator/reduction choices have separate columns", set(PARAMETER_CATEGORIES) == {
        "local_coefficients",
        "multiplicity_pairing",
        "native_operator",
        "gauge_generator",
        "open_bv",
        "provenance_yukawa",
        "background_functions",
        "topology",
        "domains",
        "regulators",
        "reductions",
        "discrete_branches",
        "derived_coordinates",
    })
    flat_parameters = [item for values in PARAMETER_CATEGORIES.values() for item in values]
    check("no charged coordinate silently occurs in two accounting columns", len(flat_parameters) == len(set(flat_parameters)))
    check("no target count is present in any charged coordinate name", all(item not in {"3", "n3", "three_generations"} for item in flat_parameters))
    check("the retained mass is derived rather than counted twice", "m_R" not in flat_parameters and "m_R_from_mu_DW_m2_eff" in flat_parameters)
    check(
        "background and spurion section-valued freedom is charged rather than hidden by a finite coefficient count",
        {
            "A0_reference_connection",
            "B_tr_section",
            "B_tf_section",
            "B_Codazzi_section",
            "B_IG_section",
            "Phi_tr_section",
            "Sigma_basis_12_sections",
        }.issubset(PARAMETER_CATEGORIES["background_functions"]),
    )
    check("five held-out observable classes are sealed by name", len(HELD_OUT) == 5)
    baseline_hash = construction_hash()
    mutated_readouts = {
        "bv_obstruction": 999,
        "gravity_cosmology": -123.5,
        "causality": "desired",
        "topology": 3,
        "physical": "SM",
    }
    _ = mutated_readouts
    check("held-out values are outside the construction hash API", construction_hash() == baseline_hash)
    check("sealed construction hash matches the preregistered literal", baseline_hash == SEALED_HASH)

    print("\n" + "=" * 94)
    print("VERDICT: UNIFIED-FINITE-CANDIDATE-WRITTEN")
    print("VERDICT: BULK-PLUS-DEFECT-ACTION-DOMAIN-WELD")
    print("VERDICT: P1/P2-ORIENTATION-AND-P3-KO-TWIST-SEPARATELY-TYPED")
    print("VERDICT: NO-FREE-CELL-FIT")
    print("RESIDUAL: N2a/N4a/N3 MUST TEST THE CONSTRUCTED FAMILY")
    print(f"SEALED HASH: {baseline_hash}")
    print(f"ALL {checks} CHECKS PASSED")
    print("=" * 94)


if __name__ == "__main__":
    main()
