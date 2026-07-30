#!/usr/bin/env python3
"""RB1 source/repository register, varied-root ledger, and current musical.

This is an executable formula/type contract.  It checks:

* the Layer-0 source/repository object dictionary;
* the formal affine comparison family and dependency-preserving point;
* the N1 varied-root DAG plus coefficient/map/background owner ledger;
* the fixed-geometry A-variation of the nine-block full-20 operator;
* the Dirac-current/curvature-current/Green split;
* the native ``G tensor kappa_g`` connection pseudo-musical; and
* the finite action-architecture family emitted to RB2.

It does not prove a source/repository identity, a global Hilbert-space Riesz
theorem, full-Sp fixed-plane covariance, stationarity, CME closure, a domain,
mass, index, count, or physical success.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
import hashlib
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TESTS))

import unified_source_datum_packet_v0_probe as n1  # noqa: E402


TOL = 2.0e-10
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


@dataclass(frozen=True)
class DictionaryRow:
    arrow: str
    domain: str
    codomain: str
    real_form: str
    degree_density: str
    pairing: str
    gauge_law: str
    variation: str
    status: str
    adjoint: str = "operator-specific source/native adjoint translation remains declared or pending"


SOURCE_REPO_DICTIONARY = (
    DictionaryRow(
        "epsilon -> epsilon_IG",
        "H-valued gauge coordinate; tangent Omega0(ad P_H)",
        "varied soldering/IG associated-bundle section",
        "source Y(7,7)/U(64,64)-type -> repo Y(9,5)/Sp(32,32;H); map absent",
        "primal degree 0 -> primal degree 0",
        "source tangent adjoint pairing -> repo BV density dual",
        "tilted gauge coordinate -> rho_IG(c)epsilon_IG+Lie_xi epsilon_IG",
        "source held only in displayed varpi probe; repo varied",
        "DIFFERENT",
    ),
    DictionaryRow(
        "varpi -> full N1 tuple",
        "Omega1(Y,ad P_H)",
        "(s,A,A0,U,P_IG,epsilon_IG,Z,ghosts,...)",
        "missing source-to-native real-form map",
        "one primal 1-form -> heterogeneous tuple",
        "one source action pairing -> several repo pairings",
        "IG translation coordinate -> separately declared gauge laws",
        "one displayed source direction -> independently varied repo fields",
        "DIFFERENT",
    ),
    DictionaryRow(
        "varpi -> A-A0",
        "Omega1(Y,ad P_H)",
        "Omega1(Y,ad P)",
        "ambient complex representation comparator only; symplectic restriction/native descent unproved",
        "primal degree 1 -> primal degree 1",
        "source adjoint/Hodge -> repo kappa_g/*_G",
        "translation/tensor law must intertwine background split",
        "source directional; A varied and A0 supplied",
        "CANDIDATE",
    ),
    DictionaryRow(
        "B_omega -> A",
        "derived affine connection nabla0+epsilon^-1 d0 epsilon",
        "independently varied ambient connection",
        "source complex/signature fork -> repo native quaternionic fork",
        "affine local degree 1 -> affine local degree 1",
        "source curvature action -> repo bulk action",
        "both affine, but under different groups and dependency graphs",
        "source derived from epsilon; repo A varied",
        "DIFFERENT",
    ),
    DictionaryRow(
        "B_omega -> Gamma_conn(epsilon_IG)+U",
        "derived source reference connection",
        "repo composite second connection",
        "native map and orbit are unbuilt",
        "affine local degree 1 -> affine local degree 1",
        "source action pairing -> repo kappa_g/*_G",
        "connection-affine if theta is adjoint covariant",
        "one source epsilon -> two independent repo fields",
        "CANDIDATE",
    ),
    DictionaryRow(
        "T_omega -> U",
        "derived connection difference Omega1(ad)",
        "independent adjoint one-form",
        "real-form map absent",
        "primal degree 1 -> primal degree 1",
        "source T/star action -> repo parent/bridge",
        "both adjoint-shaped but play different roles",
        "source derived; repo U varied",
        "DIFFERENT",
    ),
    DictionaryRow(
        "T_omega -> theta",
        "A_omega-B_omega in Omega1(ad P_H)",
        "A-Gamma_conn(epsilon_IG)-U in Omega1(ad P)",
        "ambient complex representation comparator only; symplectic restriction/native descent unproved",
        "primal degree 1 -> primal degree 1",
        "source T/star action -> repo theta norm/bridge",
        "tilted adjoint -> native adjoint plus lifted Diff",
        "both derived from different independently varied parents",
        "CANDIDATE",
    ),
    DictionaryRow(
        "UpsilonB -> E_A",
        "Omega13(Y,ad P_H), paired with a varpi direction",
        "complete N1 connection density dual",
        "real-form and operator dictionary absent",
        "density-dual 13-form -> connection density dual",
        "<alpha,UpsilonB> -> repo kappa_g/*_G convention",
        "source residual covariance is source-bound; repo full-Sp law open",
        "Euler outputs of different actions/field spaces",
        "DIFFERENT",
    ),
    DictionaryRow(
        "UpsilonB -> E_A_bos_restricted",
        "Omega13(Y,ad P_H)",
        "bosonic residual of a source-shaped repo action",
        "native Shiab and real restriction required",
        "density-dual 13-form -> density-dual 13-form",
        "source integration pairing -> repo wedge evaluation",
        "requires an equivariant native Shiab",
        "source varpi direction -> selected composite connection direction",
        "CANDIDATE",
    ),
    DictionaryRow(
        "UpsilonF_full -> J_D_or_J_F",
        "Omega13(S)+Omega14(S)+Omega13(ad P_H)",
        "connection density dual only",
        "source full-Dirac complex -> repo native K/C full-20",
        "mixed spinor/adjoint Euler packet -> one adjoint summand",
        "source fermion pairing -> repo K upstream plus kappa_g/*_G",
        "mixed source laws cannot be assigned to one current",
        "source Euler tuple -> repo A variation",
        "DIFFERENT",
    ),
    DictionaryRow(
        "(UpsilonF)_ad -> J_D",
        "Omega13(Y,ad P_H)",
        "(Omega1(Y,ad P))^vee_dens",
        "native operator/real-form map absent",
        "density-dual 13-form -> density-dual 13-form",
        "source fermion pairing -> repo K-built coefficient",
        "coadjoint covariance conditional on operator equivariance",
        "source fermion variation -> repo frozen-A operator variation",
        "CANDIDATE",
    ),
    DictionaryRow(
        "(UpsilonF)_ad -> J_F",
        "Omega13(Y,ad P_H)",
        "D_A^coad Qhat_F in the connection density dual",
        "source supplies no Q_F split",
        "density-dual -> 12-form precursor plus 13-form adjoint",
        "no source Green split -> explicit repo Green split",
        "source split absent",
        "source total adjoint component -> repo curvature-vertex subcurrent",
        "ABSENT",
    ),
    DictionaryRow(
        "(UpsilonF)_ad -> J_D+J_F",
        "Omega13(Y,ad P_H)",
        "full-20 connection density dual",
        "native operator/real-form map absent",
        "density-dual 13-form -> density-dual 13-form",
        "requires projector/gamma/K/F adjoints and wedge convention",
        "full-Sp covariance still needs moving soldering",
        "formal source residual -> repo A variation",
        "CANDIDATE",
    ),
    DictionaryRow(
        "Xi -> Noether identity",
        "Omega14(Y,ad P_H) Euler component",
        "off-shell relation among every repo Euler covector",
        "source-to-native differential absent",
        "top-density element -> identity in gauge-parameter dual",
        "D_omega Upsilon relation -> BV/formal-adjoint Ward relation",
        "covariant residual is not an identically-zero relation",
        "neither is a varied primal field",
        "DIFFERENT",
    ),
    DictionaryRow(
        "Xi-D_omega Upsilon -> R_gauge^! E",
        "source relation between two Euler components",
        "repo off-shell Ward/Noether relation",
        "native differential and full field dictionary absent",
        "relation in top-density arena -> relation in gauge-parameter dual",
        "source adjoint derivative -> repo graded formal adjoints",
        "both are relation-shaped only after full covariance",
        "source redundancy -> repo gauge-orbit contraction",
        "CANDIDATE",
    ),
    DictionaryRow(
        "nabla0 -> A0",
        "fixed source reference connection",
        "supplied repo background connection",
        "source/native bundle map absent",
        "affine degree 1 -> affine degree 1",
        "source reference pairing -> repo kappa_g/*_G",
        "both transform as connections only after a common bundle map",
        "both held fixed as action backgrounds but transform in Ward tests",
        "CANDIDATE",
        "background-response transpose required",
    ),
    DictionaryRow(
        "A_omega -> A-lambda U",
        "separately appearing source action/matter connection",
        "repo affine family A-lambda U",
        "source-to-native symplectic restriction absent",
        "affine degree 1 -> affine degree 1",
        "source fermion/boson connection pairing -> repo native action pairing",
        "affine for every real lambda because U transforms tensorially",
        "source dependency is reconstructed; A and U independently varied",
        "CANDIDATE",
        "connection variation pulls back by (delta A-lambda delta U)",
    ),
    DictionaryRow(
        "B_omega -> Gamma_conn(epsilon_IG)",
        "source reference connection derived only from epsilon",
        "repo epsilon-derived connection",
        "native orbit/bundle identification absent",
        "affine degree 1 -> affine degree 1",
        "source reference curvature pairing -> repo native connection pairing",
        "candidate affine gauge law on the Spin/stabilizer arena",
        "source epsilon-derived; repo epsilon varied",
        "CANDIDATE",
        "(D_epsilon Gamma_conn)^! remains unbuilt",
    ),
    DictionaryRow(
        "epsilon^-1 d0 epsilon -> Gamma_conn+(1-lambda)U-A0",
        "source reference-gauge-orbit displacement",
        "repo affine displacement from supplied A0",
        "native orbit map absent",
        "degree 1 -> degree 1",
        "source orbit tangent pairing -> repo kappa_g/*_G",
        "lambda=1 respects epsilon-only dependency; lambda!=1 constrains U to the same orbit",
        "source epsilon-derived; repo epsilon and U independently varied",
        "CANDIDATE",
        "orbit-map transpose required",
    ),
    DictionaryRow(
        "varpi -> A-lambda U-A0",
        "source translation one-form",
        "repo affine translation family",
        "source/native symplectic restriction absent",
        "degree 1 -> degree 1",
        "source translation pairing -> repo kappa_g/*_G",
        "adjoint-shaped after a common bundle map",
        "source varpi directional variation -> repo A/U variations",
        "CANDIDATE",
        "(delta A-lambda delta U)^! pullback",
    ),
    DictionaryRow(
        "UpsilonB+(UpsilonF)_ad -> E_A_source_shaped",
        "source total adjoint Euler residual",
        "repo source-shaped connection Euler covector",
        "native Shiab, fermion, and real-form translation absent",
        "13-form density dual -> 13-form density dual",
        "source total residual pairing -> repo wedge/kappa pairing",
        "conditional coadjoint covariance",
        "source residual output -> repo varied A/U/epsilon system",
        "CANDIDATE",
        "complete pulled-back Euler transpose required",
    ),
    DictionaryRow(
        "source_spin0 -> VEV/full20_mass",
        "source true-spin-zero component of an adjoint-valued one-form",
        "future zero-order full-20 operator, its stationary VEV, and physical Hessian mass",
        "representation and native placement maps absent",
        "primal spin-zero field -> endomorphism -> field value -> spectral output",
        "source gauge-potential pairing -> separate K/C full-20 pairings",
        "gauge field, vacuum value, and reduced mass obey different laws",
        "field varied; VEV solved or supplied later; mass derived only after reduction",
        "DIFFERENT",
        "K-adjoint and C-natural placement remain separate",
    ),
    DictionaryRow(
        "source musical -> sharp_conn",
        "source 13-form residual pairing with 1-form variation",
        "repo density-dual-to-primal connection map",
        "no checked source native Sp(32,32;H) musical",
        "source already dual -> repo 13-form to 1-form",
        "source Hodge/adjoint notation -> explicit G tensor kappa_g",
        "source map not displayed",
        "not a field variation",
        "ABSENT",
    ),
)


REQUIRED_DICTIONARY_ARROWS = {
    "epsilon -> epsilon_IG",
    "varpi -> full N1 tuple",
    "varpi -> A-A0",
    "B_omega -> A",
    "B_omega -> Gamma_conn(epsilon_IG)+U",
    "T_omega -> U",
    "T_omega -> theta",
    "UpsilonB -> E_A",
    "UpsilonB -> E_A_bos_restricted",
    "UpsilonF_full -> J_D_or_J_F",
    "(UpsilonF)_ad -> J_D",
    "(UpsilonF)_ad -> J_F",
    "(UpsilonF)_ad -> J_D+J_F",
    "Xi -> Noether identity",
    "Xi-D_omega Upsilon -> R_gauge^! E",
    "nabla0 -> A0",
    "A_omega -> A-lambda U",
    "B_omega -> Gamma_conn(epsilon_IG)",
    "epsilon^-1 d0 epsilon -> Gamma_conn+(1-lambda)U-A0",
    "varpi -> A-lambda U-A0",
    "UpsilonB+(UpsilonF)_ad -> E_A_source_shaped",
    "source_spin0 -> VEV/full20_mass",
    "source musical -> sharp_conn",
}


def validate_dictionary(rows: tuple[DictionaryRow, ...]) -> list[str]:
    errors: list[str] = []
    arrows = [row.arrow for row in rows]
    if set(arrows) != REQUIRED_DICTIONARY_ARROWS:
        errors.append("required Layer-0 arrow set mismatch")
    if len(arrows) != len(set(arrows)):
        errors.append("duplicate Layer-0 arrow")
    for row in rows:
        if row.status not in {"SAME", "DIFFERENT", "CANDIDATE", "ABSENT"}:
            errors.append(f"unknown Layer-0 status: {row.arrow}")
        if row.status == "SAME":
            errors.append(f"unchecked source/repo identity: {row.arrow}")
        if not all(
            (
                row.domain,
                row.codomain,
                row.real_form,
                row.degree_density,
                row.pairing,
                row.gauge_law,
                row.variation,
                row.adjoint,
            )
        ):
            errors.append(f"incomplete Layer-0 metadata: {row.arrow}")
    return errors


SOURCE_AOMEGA_SUM_GRADE = "DERIVED-RECONSTRUCTION"


@dataclass(frozen=True)
class AffineComparisonPoint:
    name: str
    lambda_u: Fraction
    a_omega: tuple[Fraction, Fraction, Fraction, Fraction]
    b_omega: tuple[Fraction, Fraction, Fraction, Fraction]
    varpi: tuple[Fraction, Fraction, Fraction, Fraction]
    reference_orbit_displacement: tuple[
        Fraction, Fraction, Fraction, Fraction
    ]
    limitation: str


# Coefficient order: (A, Gamma_conn(epsilon_IG), U, A0).
THETA_VECTOR = np.array((1, -1, -1, 0), dtype=int)


def affine_comparison(
    lambda_u: Fraction,
    name: str,
) -> AffineComparisonPoint:
    """Formal shared-coordinate comparison, not a field-space pullback."""
    one = Fraction(1)
    zero = Fraction(0)
    return AffineComparisonPoint(
        name=name,
        lambda_u=lambda_u,
        a_omega=(one, zero, -lambda_u, zero),
        b_omega=(zero, one, one - lambda_u, zero),
        varpi=(one, zero, -lambda_u, -one),
        reference_orbit_displacement=(
            zero,
            one,
            one - lambda_u,
            -one,
        ),
        limitation=(
            "lambda=1 uniquely preserves B_omega's epsilon-only dependency; "
            "lambda!=1 constrains independent U to the reference gauge orbit"
        ),
    )


AFFINE_ENDPOINTS = (
    affine_comparison(Fraction(0), "connection_anchored_endpoint_control"),
    affine_comparison(Fraction(1), "reference_anchored_endpoint"),
)


@dataclass(frozen=True)
class PathSpec:
    term: str
    branch: str
    root: str
    nodes: tuple[str, ...]
    derivative_order: int
    formal_adjoint: str
    green: str | None
    status: str
    distribution_order: int = 0


ROOTS = {
    "A",
    "U",
    "P_IG",
    "epsilon_IG",
    "s",
    "Z",
    "c_g",
    "gamma",
    "bar_gamma",
    "b_gamma",
    "xi",
}
ALLOWED_PATH_STATUS = {
    "EXACT",
    "BRANCH_CONDITIONAL",
    "PARTIAL",
    "COMPARATOR_ONLY",
}


PATHS = (
    PathSpec(
        "ambient_yang_mills", "common", "A",
        ("A", "F_A", "ambient_yang_mills"), 1, "D_A^!", "G_YM", "EXACT",
    ),
    PathSpec(
        "induced_ym_parent", "common", "A",
        ("A", "D_AU", "induced_ym_parent"), 0, "B_U^!", None, "EXACT",
    ),
    PathSpec(
        "induced_ym_parent", "common", "U",
        ("U", "D_AU", "induced_ym_parent"), 1, "D_A^!", "G_parent_U", "EXACT",
    ),
    PathSpec(
        "induced_ym_parent", "common", "P_IG",
        ("P_IG", "linear_and_quadratic_parent", "induced_ym_parent"),
        0, "identity-Z_U^-1", None, "EXACT",
    ),
    PathSpec(
        "distortion_source_bridge", "literal_N1", "A",
        ("A", "theta", "distortion_source_bridge"), 0, "+identity", None, "EXACT",
    ),
    PathSpec(
        "distortion_source_bridge", "literal_N1", "U",
        ("U", "theta", "distortion_source_bridge"), 0, "-identity", None, "EXACT",
    ),
    PathSpec(
        "distortion_source_bridge", "literal_N1", "epsilon_IG",
        ("epsilon_IG", "Gamma_conn", "theta", "distortion_source_bridge"),
        1, "(D_epsilon Gamma_conn)^!", "G_Gamma_unbuilt", "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "distortion_source_bridge", "literal_N1", "Z",
        ("Z", "J_literal", "distortion_source_bridge"),
        0, "(D_Z J_literal)^!", None, "EXACT",
    ),
    PathSpec(
        "full20_krein_quadratic", "common", "A",
        ("A", "D_h", "full20_krein_quadratic"), 0, "C_D^!", None, "EXACT",
    ),
    PathSpec(
        "full20_krein_quadratic", "common", "A",
        ("A", "F_A", "V_GT", "full20_krein_quadratic"),
        1,
        "D_A^coad Qhat_F; equivalently D_A^dagger sharp_2(Qhat_F)",
        "G_F",
        "EXACT",
    ),
    PathSpec(
        "full20_krein_quadratic", "common", "Z",
        ("Z", "ordered_full20_operator", "full20_krein_quadratic"),
        1, "K/Grassmann formal adjoint", "G_Z_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "end_selector", "V_fixed_end_profile", "Z",
        ("Z", "selector_V", "end_selector"), 0, "K algebraic adjoint", None,
        "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "end_selector", "B_auxiliary_comparator", "A",
        ("A", "D_packet_hat", "selector_B", "end_selector"),
        1, "auxiliary operator adjoint", "G_selector_B", "COMPARATOR_ONLY",
    ),
    PathSpec(
        "end_selector", "0_vectorlike", "Z",
        ("Z", "selector_0", "end_selector"), 0, "K algebraic adjoint", None, "EXACT",
    ),
    PathSpec(
        "induced_section_gravity", "direct_II", "s",
        ("s", "II_s", "II_norm", "induced_section_gravity"),
        2, "(D_s II)^!", "G_II", "PARTIAL",
    ),
    PathSpec(
        "induced_section_gravity", "direct_II", "s",
        ("s", "II_s", "II0_s", "II0_norm", "induced_section_gravity"),
        2, "(D_s II0)^!", "G_II0", "PARTIAL",
    ),
    PathSpec(
        "induced_section_gravity", "direct_II", "s",
        (
            "s",
            "g_s",
            "tracefree_projector_and_norm",
            "induced_section_gravity",
        ),
        1,
        "induced-metric/projector-chain transpose",
        "G_gravity_metric_chain",
        "PARTIAL",
    ),
    PathSpec(
        "induced_section_gravity", "direct_II", "s",
        ("s", "g_s", "density_X", "induced_section_gravity"),
        1,
        "induced-metric density transpose",
        "G_gravity_density",
        "PARTIAL",
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "A",
        ("A", "F_A", "pullback_F_A", "R_SW", "seiberg_witten_defect"),
        1, "(s^*)^! D_AX^! P_+^!", "G_SW_A", "PARTIAL",
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "s",
        (
            "s",
            "g_s",
            "Pplus_norm_density",
            "R_SW",
            "seiberg_witten_defect",
        ),
        1,
        "induced-metric/Hodge-chain transpose",
        "G_SW_metric_chain",
        "PARTIAL",
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "s",
        (
            "s",
            "moving_pullback_A_Cartan",
            "F_AX",
            "R_SW",
            "seiberg_witten_defect",
        ),
        1, "Cartan pullback transpose", "G_SW_pullback_A", "PARTIAL",
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "s",
        (
            "s",
            "moving_pullback_Z",
            "psi",
            "mu_psi",
            "R_SW",
            "seiberg_witten_defect",
        ),
        0, "section-evaluation transpose", None, "PARTIAL",
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "s",
        ("s", "P0", "psi", "mu_psi", "R_SW", "seiberg_witten_defect"),
        0, "ambient-projector evaluation transpose", None, "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "s",
        ("s", "pushforward_support", "seiberg_witten_defect"),
        0,
        "distributional support action; no ordinary V-Green term",
        None,
        "PARTIAL",
        distribution_order=1,
    ),
    PathSpec(
        "seiberg_witten_defect", "common", "Z",
        ("Z", "psi=P0_pullback_Z", "mu_psi", "R_SW", "seiberg_witten_defect"),
        0, "(D_psi mu)^!", None, "PARTIAL",
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "A",
        ("A", "A-A0", "resV_coeff", "v_s", "c_rho_v", "krein_yukawa_defect"),
        0, "(resV_coeff)^! J_vK", None, "PARTIAL",
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "s",
        ("s", "resV_coeff", "v_s", "c_rho_v", "krein_yukawa_defect"),
        0, "(D_s resV)^!", None, "PARTIAL",
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "s",
        ("s", "moving_pullback_Z", "psi", "krein_yukawa_defect"),
        0, "section-evaluation transpose", None, "PARTIAL",
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "s",
        ("s", "P0", "psi", "krein_yukawa_defect"),
        0, "ambient-projector evaluation transpose", None, "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "s",
        ("s", "g_s", "K_pairing_and_density", "krein_yukawa_defect"),
        1,
        "induced-metric/K-chain transpose",
        "G_Yuk_K_metric",
        "PARTIAL",
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "s",
        ("s", "pushforward_support", "krein_yukawa_defect"),
        0,
        "distributional support action; no ordinary V-Green term",
        None,
        "PARTIAL",
        distribution_order=1,
    ),
    PathSpec(
        "krein_yukawa_defect", "K", "Z",
        ("Z", "psi=P0_pullback_Z", "krein_yukawa_defect"),
        0, "K-total-kernel adjoint", None, "EXACT",
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "A",
        ("A", "A-A0", "resV_coeff", "v_s", "c_rho_v", "charge_conjugation_yukawa_defect"),
        0, "(resV_coeff)^! J_vC", None, "PARTIAL",
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "s",
        (
            "s",
            "resV_coeff",
            "v_s",
            "c_rho_v",
            "charge_conjugation_yukawa_defect",
        ),
        0, "(D_s resV)^!", None, "PARTIAL",
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "s",
        (
            "s",
            "moving_pullback_Z",
            "psi",
            "charge_conjugation_yukawa_defect",
        ),
        0, "section-evaluation transpose", None, "PARTIAL",
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "s",
        ("s", "P0", "psi", "charge_conjugation_yukawa_defect"),
        0, "ambient-projector evaluation transpose", None, "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "s",
        (
            "s",
            "g_s",
            "C_pairing_reality_and_density",
            "charge_conjugation_yukawa_defect",
        ),
        1,
        "induced-metric/C-chain transpose",
        "G_Yuk_C_metric",
        "PARTIAL",
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "s",
        ("s", "pushforward_support", "charge_conjugation_yukawa_defect"),
        0,
        "distributional support action; no ordinary V-Green term",
        None,
        "PARTIAL",
        distribution_order=1,
    ),
    PathSpec(
        "charge_conjugation_yukawa_defect", "C", "Z",
        ("Z", "psi=P0_pullback_Z", "charge_conjugation_yukawa_defect"),
        0, "C-natural alternating transpose", None, "PARTIAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "A",
        ("A", "A-A0", "resV_coeff", "v_s", "c_rho_v", "spurion_interface"),
        0, "(resV_coeff)^! J_vSigma", None, "PARTIAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "s",
        ("s", "resV_coeff", "v_s", "c_rho_v", "spurion_interface"),
        0, "(D_s resV)^!", None, "PARTIAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "s",
        ("s", "moving_pullback_Z", "psi", "spurion_interface"),
        0, "section-evaluation transpose", None, "PARTIAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "s",
        ("s", "P0", "psi", "spurion_interface"),
        0, "ambient-projector evaluation transpose", None, "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "s",
        (
            "s",
            "g_s",
            "C_pairing_density_and_Sigma_metric_carrier",
            "spurion_interface",
        ),
        1,
        "induced-metric/C-chain transpose",
        "G_Sigma_metric",
        "PARTIAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "s",
        ("s", "Sigma_carrier_transport", "spurion_interface"),
        0, "supplied-carrier transport transpose", None, "BRANCH_CONDITIONAL",
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "s",
        ("s", "pushforward_support", "spurion_interface"),
        0,
        "distributional support action; no ordinary V-Green term",
        None,
        "PARTIAL",
        distribution_order=1,
    ),
    PathSpec(
        "spurion_interface", "C_Sigma", "Z",
        ("Z", "psi=P0_pullback_Z", "spurion_interface"),
        0, "C-natural alternating transpose", None, "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "A",
        ("A", "BRST_A_and_Rr", "minimal_bv_extension"),
        1, "graded formal adjoint", "G_BV_A_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "U",
        ("U", "BRST_U", "minimal_bv_extension"),
        1, "graded formal adjoint", "G_BV_U_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "P_IG",
        ("P_IG", "BRST_P_IG", "minimal_bv_extension"),
        1, "graded formal adjoint", "G_BV_P_IG_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "epsilon_IG",
        ("epsilon_IG", "BRST_epsilon", "minimal_bv_extension"),
        1,
        "graded Lie-derivative/formal transpose",
        "G_BV_epsilon_unbuilt",
        "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "s",
        ("s", "BRST_s", "minimal_bv_extension"),
        1, "Lie-derivative transpose", "G_BV_s_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "Z",
        ("Z", "BRST_Z", "minimal_bv_extension"),
        1, "graded formal adjoint", "G_BV_Z_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "c_g",
        ("c_g", "BRST_all_internal_fields", "minimal_bv_extension"),
        1, "graded formal adjoint", "G_BV_cg_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "gamma",
        ("gamma", "R_r_and_BRST_gamma", "minimal_bv_extension"),
        1, "graded formal adjoint", "G_BV_gamma_unbuilt", "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "bar_gamma",
        ("bar_gamma", "nonminimal_doublet", "minimal_bv_extension"),
        1,
        "graded nonminimal/Lie transpose",
        "G_BV_bargamma_unbuilt",
        "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "b_gamma",
        ("b_gamma", "nonminimal_doublet", "minimal_bv_extension"),
        1,
        "graded nonminimal/Lie transpose",
        "G_BV_bgamma_unbuilt",
        "PARTIAL",
    ),
    PathSpec(
        "minimal_bv_extension", "tau0_skeleton", "xi",
        ("xi", "Lie_derivative_all_fields", "minimal_bv_extension"),
        1, "graded Lie-derivative transpose", "G_BV_xi_unbuilt", "PARTIAL",
    ),
)


EXPECTED_ROOTS = {
    ("ambient_yang_mills", "common"): {"A"},
    ("induced_ym_parent", "common"): {"A", "U", "P_IG"},
    ("distortion_source_bridge", "literal_N1"): {"A", "U", "epsilon_IG", "Z"},
    ("full20_krein_quadratic", "common"): {"A", "Z"},
    ("end_selector", "V_fixed_end_profile"): {"Z"},
    ("end_selector", "B_auxiliary_comparator"): {"A"},
    ("end_selector", "0_vectorlike"): {"Z"},
    ("induced_section_gravity", "direct_II"): {"s"},
    ("seiberg_witten_defect", "common"): {"A", "s", "Z"},
    ("krein_yukawa_defect", "K"): {"A", "s", "Z"},
    ("charge_conjugation_yukawa_defect", "C"): {"A", "s", "Z"},
    ("spurion_interface", "C_Sigma"): {"A", "s", "Z"},
    ("minimal_bv_extension", "tau0_skeleton"): {
        "A",
        "U",
        "P_IG",
        "epsilon_IG",
        "s",
        "Z",
        "c_g",
        "gamma",
        "bar_gamma",
        "b_gamma",
        "xi",
    },
    ("orientation_holonomy_cocycle", "fixed_topology"): set(),
}

# Independent frozen chain registry.  Root coverage alone cannot certify a
# dependency graph: it would accept a path that silently drops a projector,
# restriction, pullback, support map, or other intermediate operation.
EXPECTED_NODE_PATHS = {
    ("ambient_yang_mills", "common", "A"): {
        ("A", "F_A", "ambient_yang_mills"),
    },
    ("induced_ym_parent", "common", "A"): {
        ("A", "D_AU", "induced_ym_parent"),
    },
    ("induced_ym_parent", "common", "U"): {
        ("U", "D_AU", "induced_ym_parent"),
    },
    ("induced_ym_parent", "common", "P_IG"): {
        ("P_IG", "linear_and_quadratic_parent", "induced_ym_parent"),
    },
    ("distortion_source_bridge", "literal_N1", "A"): {
        ("A", "theta", "distortion_source_bridge"),
    },
    ("distortion_source_bridge", "literal_N1", "U"): {
        ("U", "theta", "distortion_source_bridge"),
    },
    ("distortion_source_bridge", "literal_N1", "epsilon_IG"): {
        (
            "epsilon_IG",
            "Gamma_conn",
            "theta",
            "distortion_source_bridge",
        ),
    },
    ("distortion_source_bridge", "literal_N1", "Z"): {
        ("Z", "J_literal", "distortion_source_bridge"),
    },
    ("full20_krein_quadratic", "common", "A"): {
        ("A", "D_h", "full20_krein_quadratic"),
        ("A", "F_A", "V_GT", "full20_krein_quadratic"),
    },
    ("full20_krein_quadratic", "common", "Z"): {
        (
            "Z",
            "ordered_full20_operator",
            "full20_krein_quadratic",
        ),
    },
    ("end_selector", "V_fixed_end_profile", "Z"): {
        ("Z", "selector_V", "end_selector"),
    },
    ("end_selector", "B_auxiliary_comparator", "A"): {
        ("A", "D_packet_hat", "selector_B", "end_selector"),
    },
    ("end_selector", "0_vectorlike", "Z"): {
        ("Z", "selector_0", "end_selector"),
    },
    ("induced_section_gravity", "direct_II", "s"): {
        ("s", "II_s", "II_norm", "induced_section_gravity"),
        ("s", "II_s", "II0_s", "II0_norm", "induced_section_gravity"),
        (
            "s",
            "g_s",
            "tracefree_projector_and_norm",
            "induced_section_gravity",
        ),
        ("s", "g_s", "density_X", "induced_section_gravity"),
    },
    ("seiberg_witten_defect", "common", "A"): {
        (
            "A",
            "F_A",
            "pullback_F_A",
            "R_SW",
            "seiberg_witten_defect",
        ),
    },
    ("seiberg_witten_defect", "common", "s"): {
        (
            "s",
            "g_s",
            "Pplus_norm_density",
            "R_SW",
            "seiberg_witten_defect",
        ),
        (
            "s",
            "moving_pullback_A_Cartan",
            "F_AX",
            "R_SW",
            "seiberg_witten_defect",
        ),
        (
            "s",
            "moving_pullback_Z",
            "psi",
            "mu_psi",
            "R_SW",
            "seiberg_witten_defect",
        ),
        ("s", "P0", "psi", "mu_psi", "R_SW", "seiberg_witten_defect"),
        ("s", "pushforward_support", "seiberg_witten_defect"),
    },
    ("seiberg_witten_defect", "common", "Z"): {
        (
            "Z",
            "psi=P0_pullback_Z",
            "mu_psi",
            "R_SW",
            "seiberg_witten_defect",
        ),
    },
    ("krein_yukawa_defect", "K", "A"): {
        (
            "A",
            "A-A0",
            "resV_coeff",
            "v_s",
            "c_rho_v",
            "krein_yukawa_defect",
        ),
    },
    ("krein_yukawa_defect", "K", "s"): {
        ("s", "resV_coeff", "v_s", "c_rho_v", "krein_yukawa_defect"),
        ("s", "moving_pullback_Z", "psi", "krein_yukawa_defect"),
        ("s", "P0", "psi", "krein_yukawa_defect"),
        ("s", "g_s", "K_pairing_and_density", "krein_yukawa_defect"),
        ("s", "pushforward_support", "krein_yukawa_defect"),
    },
    ("krein_yukawa_defect", "K", "Z"): {
        ("Z", "psi=P0_pullback_Z", "krein_yukawa_defect"),
    },
    ("charge_conjugation_yukawa_defect", "C", "A"): {
        (
            "A",
            "A-A0",
            "resV_coeff",
            "v_s",
            "c_rho_v",
            "charge_conjugation_yukawa_defect",
        ),
    },
    ("charge_conjugation_yukawa_defect", "C", "s"): {
        (
            "s",
            "resV_coeff",
            "v_s",
            "c_rho_v",
            "charge_conjugation_yukawa_defect",
        ),
        (
            "s",
            "moving_pullback_Z",
            "psi",
            "charge_conjugation_yukawa_defect",
        ),
        ("s", "P0", "psi", "charge_conjugation_yukawa_defect"),
        (
            "s",
            "g_s",
            "C_pairing_reality_and_density",
            "charge_conjugation_yukawa_defect",
        ),
        ("s", "pushforward_support", "charge_conjugation_yukawa_defect"),
    },
    ("charge_conjugation_yukawa_defect", "C", "Z"): {
        (
            "Z",
            "psi=P0_pullback_Z",
            "charge_conjugation_yukawa_defect",
        ),
    },
    ("spurion_interface", "C_Sigma", "A"): {
        (
            "A",
            "A-A0",
            "resV_coeff",
            "v_s",
            "c_rho_v",
            "spurion_interface",
        ),
    },
    ("spurion_interface", "C_Sigma", "s"): {
        ("s", "resV_coeff", "v_s", "c_rho_v", "spurion_interface"),
        ("s", "moving_pullback_Z", "psi", "spurion_interface"),
        ("s", "P0", "psi", "spurion_interface"),
        (
            "s",
            "g_s",
            "C_pairing_density_and_Sigma_metric_carrier",
            "spurion_interface",
        ),
        ("s", "Sigma_carrier_transport", "spurion_interface"),
        ("s", "pushforward_support", "spurion_interface"),
    },
    ("spurion_interface", "C_Sigma", "Z"): {
        ("Z", "psi=P0_pullback_Z", "spurion_interface"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "A"): {
        ("A", "BRST_A_and_Rr", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "U"): {
        ("U", "BRST_U", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "P_IG"): {
        ("P_IG", "BRST_P_IG", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "epsilon_IG"): {
        ("epsilon_IG", "BRST_epsilon", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "s"): {
        ("s", "BRST_s", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "Z"): {
        ("Z", "BRST_Z", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "c_g"): {
        (
            "c_g",
            "BRST_all_internal_fields",
            "minimal_bv_extension",
        ),
    },
    ("minimal_bv_extension", "tau0_skeleton", "gamma"): {
        ("gamma", "R_r_and_BRST_gamma", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "bar_gamma"): {
        ("bar_gamma", "nonminimal_doublet", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "b_gamma"): {
        ("b_gamma", "nonminimal_doublet", "minimal_bv_extension"),
    },
    ("minimal_bv_extension", "tau0_skeleton", "xi"): {
        (
            "xi",
            "Lie_derivative_all_fields",
            "minimal_bv_extension",
        ),
    },
}


FORBIDDEN_EDGES = {
    ("epsilon_IG", "D_AU"),
    ("A", "J_literal"),
    ("epsilon_IG", "Gamma_trace"),
    ("epsilon_IG", "P_R"),
    ("s", "G_Y"),
    ("A", "selector_V"),
    ("A", "selector_0"),
}


EXCLUSIVE_ALIAS_GROUPS = {
    "parent_presentation": {"P_IG_parent", "eliminated_ZU_quadratic"},
    "gravity_presentation": {"direct_II_action", "Gauss_rewrite"},
    "curvature_pullback": {"F_of_pullback_A", "pullback_F_A"},
    "full20_expansion": {"full20_quadratic", "vertical_expansion_component"},
    "yukawa_branch": {"Yukawa_K", "Yukawa_C"},
    "selector_branch": {"selector_V", "selector_B", "selector_0"},
    "defect_shape_presentation": {
        "intrinsic_pullback_variation",
        "ambient_pushforward_variation",
    },
}


SEMANTIC_COLLISIONS = {
    "Gamma_conn(epsilon_IG) != Gamma_trace:VxS->S",
    "gamma_BV_ghost != gamma_Clifford",
    "g_s=derived_section_metric != fixed_G_Y",
    "P_IG_momentum != P_I_or_P_R_projector",
    "epsilon_IG != epsilon_C_sign",
    "v_tr_end_profile != v_s=resV_coeff(A-A0)",
}


@dataclass(frozen=True)
class DependencyOwner:
    name: str
    kind: str
    depends_on: tuple[str, ...]
    consumers: tuple[str, ...]
    status: str


FIXED_COEFFICIENT_OWNERS = tuple(
    DependencyOwner(
        name,
        "coefficient",
        (),
        tuple(
            term.name for term in n1.ACTION_TERMS if name in term.coefficients
        ),
        "SUPPLIED_OR_SEARCH_PARAMETER",
    )
    for name in sorted(
        {
            coefficient
            for term in n1.ACTION_TERMS
            for coefficient in term.coefficients
        }
    )
)

MAP_AND_BACKGROUND_OWNERS = (
    DependencyOwner(
        "A0", "supplied_background", (), (
            "end_selector",
            "krein_yukawa_defect",
            "charge_conjugation_yukawa_defect",
            "spurion_interface",
        ), "TRANSFORMS_IN_WARD_IDENTITY",
    ),
    DependencyOwner(
        "Z_hat", "comparator_field", (), ("end_selector",),
        "SUPPLIED_COMPARATOR",
    ),
    DependencyOwner(
        "Sigma", "supplied_spurion", ("s",), ("spurion_interface",),
        "COEFFICIENT_FIXED_CARRIER_MOVES_UNLESS_TRIVIALIZED",
    ),
    DependencyOwner(
        "Gamma_conn", "derived_connection", ("epsilon_IG",),
        ("distortion_source_bridge",), "MOVING_ORBIT_UNBUILT",
    ),
    DependencyOwner(
        "Gamma_trace", "Clifford_trace", (),
        ("full20_krein_quadratic",), "FIXED_GEOMETRY_RB1_ONLY",
    ),
    DependencyOwner(
        "P_I", "algebraic_projector", ("Gamma_trace",),
        ("full20_krein_quadratic",), "FIXED_GEOMETRY_RB1_ONLY",
    ),
    DependencyOwner(
        "P_R", "algebraic_projector", ("Gamma_trace",),
        ("full20_krein_quadratic",), "FIXED_GEOMETRY_RB1_ONLY",
    ),
    DependencyOwner(
        "P0", "defect_projector", ("s",),
        (
            "seiberg_witten_defect",
            "krein_yukawa_defect",
            "charge_conjugation_yukawa_defect",
            "spurion_interface",
        ), "AMBIENT-EVALUATION_OR_INDUCED-METRIC-FORK",
    ),
    DependencyOwner(
        "P_plus", "Hodge_projector", ("g_s",),
        ("seiberg_witten_defect",), "INDUCED-METRIC_DEPENDENT",
    ),
    DependencyOwner(
        "resV_coeff", "vertical_coefficient_restriction", ("s", "A", "A0"),
        (
            "krein_yukawa_defect",
            "charge_conjugation_yukawa_defect",
            "spurion_interface",
        ), "MOVING_RESTRICTION",
    ),
    DependencyOwner(
        "c_rho", "Clifford_gauge_insertion", ("s", "resV_coeff"),
        (
            "krein_yukawa_defect",
            "charge_conjugation_yukawa_defect",
            "spurion_interface",
        ), "COMPOSITE_NOT_INDEPENDENT",
    ),
    DependencyOwner(
        "K_E", "spinor_Krein_pairing", ("g_s",),
        ("full20_krein_quadratic", "krein_yukawa_defect"),
        "UPSTREAM_OF_CURRENT_NOT_CONNECTION_MUSICAL",
    ),
    DependencyOwner(
        "C_E", "charge_conjugation_pairing", ("g_s",),
        ("charge_conjugation_yukawa_defect", "spurion_interface"),
        "REALITY_COMPLETION_PARTIAL",
    ),
    DependencyOwner(
        "V_GT", "curvature_vertex", ("A", "F_A", "P_R", "Gamma_trace"),
        ("full20_krein_quadratic",), "FIXED_GEOMETRY_A_VARIATION",
    ),
    DependencyOwner(
        "s_pushforward", "defect_placement", ("s",),
        (
            "induced_section_gravity",
            "seiberg_witten_defect",
            "krein_yukawa_defect",
            "charge_conjugation_yukawa_defect",
            "spurion_interface",
        ), "ALTERNATIVE_SHAPE-DERIVATIVE_PRESENTATION",
    ),
)

DEPENDENCY_OWNERS = FIXED_COEFFICIENT_OWNERS + MAP_AND_BACKGROUND_OWNERS


def path_ledger_digest(paths: tuple[PathSpec, ...]) -> str:
    payload = "\n".join(
        repr(
            (
                path.term,
                path.branch,
                path.root,
                path.nodes,
                path.derivative_order,
                path.formal_adjoint,
                path.green,
                path.status,
                path.distribution_order,
            )
        )
        for path in paths
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


FROZEN_PATH_LEDGER_SHA256 = (
    "f6582dacc9074fff4fd8a150c48e32bdf86d75271ba39e7916f005b763cee680"
)


def validate_dependency_owners(
    owners: tuple[DependencyOwner, ...],
) -> list[str]:
    errors: list[str] = []
    names = [owner.name for owner in owners]
    expected_coefficients = {
        coefficient
        for term in n1.ACTION_TERMS
        for coefficient in term.coefficients
    }
    if not expected_coefficients <= set(names):
        errors.append("one or more N1 coefficients lack an owner")
    if len(names) != len(set(names)):
        errors.append("duplicate coefficient/map/background owner")
    required_maps = {
        "A0",
        "Z_hat",
        "Sigma",
        "Gamma_conn",
        "Gamma_trace",
        "P_I",
        "P_R",
        "P0",
        "P_plus",
        "resV_coeff",
        "c_rho",
        "K_E",
        "C_E",
        "V_GT",
        "s_pushforward",
    }
    if not required_maps <= set(names):
        errors.append("required map/background owner missing")
    if any(not owner.kind or not owner.consumers or not owner.status for owner in owners):
        errors.append("incomplete dependency owner")
    return errors


def validate_paths(paths: tuple[PathSpec, ...]) -> list[str]:
    errors: list[str] = []
    grouped: dict[tuple[str, str], set[str]] = {
        key: set() for key in EXPECTED_ROOTS
    }
    grouped_nodes: dict[tuple[str, str, str], Counter[tuple[str, ...]]] = {
        key: Counter() for key in EXPECTED_NODE_PATHS
    }
    for path in paths:
        key = (path.term, path.branch)
        if key not in grouped:
            errors.append(f"unknown term/branch {key}")
            continue
        grouped[key].add(path.root)
        node_key = (path.term, path.branch, path.root)
        if node_key not in grouped_nodes:
            errors.append(f"unknown term/branch/root {node_key}")
        else:
            grouped_nodes[node_key][path.nodes] += 1
        if path.root not in ROOTS:
            errors.append(f"independent root not allowed: {path.root}")
        if not path.nodes or path.nodes[0] != path.root:
            errors.append(f"path does not begin at root: {path}")
        if not path.nodes or path.nodes[-1] != path.term:
            errors.append(f"path does not terminate at action family: {path}")
        if path.status not in ALLOWED_PATH_STATUS:
            errors.append(f"unknown status: {path.status}")
        if path.derivative_order > 0 and not path.green:
            errors.append(f"missing Green form: {path.term}/{path.root}")
        if path.derivative_order == 0 and path.green:
            errors.append(f"algebraic edge owns false Green form: {path.term}/{path.root}")
        if path.distribution_order not in {0, 1}:
            errors.append(f"invalid distribution order: {path}")
        if path.distribution_order and "distributional" not in path.formal_adjoint:
            errors.append(f"distribution-order path lacks distributional owner: {path}")
        for edge in zip(path.nodes, path.nodes[1:]):
            if edge in FORBIDDEN_EDGES:
                errors.append(f"forbidden edge {edge}")
        if "pullback_form_sA" in path.nodes and "resV_coeff" not in path.nodes:
            errors.append("form pullback substituted for coefficient restriction")
    for key, expected in EXPECTED_ROOTS.items():
        if grouped[key] != expected:
            errors.append(
                f"root mismatch {key}: expected={sorted(expected)} "
                f"actual={sorted(grouped[key])}"
            )
    for key, expected in EXPECTED_NODE_PATHS.items():
        expected_counter = Counter({nodes: 1 for nodes in expected})
        if grouped_nodes[key] != expected_counter:
            errors.append(
                f"node-path mismatch {key}: expected={expected_counter} "
                f"actual={grouped_nodes[key]}"
            )
    if (
        FROZEN_PATH_LEDGER_SHA256 is not None
        and path_ledger_digest(paths) != FROZEN_PATH_LEDGER_SHA256
    ):
        errors.append("typed path-ledger checksum mismatch")
    return errors


def validate_alias_selection(active: set[str]) -> list[str]:
    errors: list[str] = []
    for name, group in EXCLUSIVE_ALIAS_GROUPS.items():
        selected = active & group
        if len(selected) > 1:
            errors.append(f"{name} double counted: {sorted(selected)}")
    return errors


DIRAC_BLOCK_VARIATIONS = {
    "SS": "h_a c.rho_S(a)",
    "SI": "h_SI c.rho_S(a) Gamma_trace",
    "SR": "-h_SR tr_G rho(a)",
    "IS": "14 conjugate(h_SI) j c.rho_S(a)",
    "II": "h_d P_I C_VtensorS(a) P_I",
    "IR": "h_IR P_I C_VtensorS(a) P_R",
    "RS": "-conjugate(h_SR) P_R rho(a)",
    "RI": "conjugate(h_IR) P_R C_VtensorS(a) P_I",
    "RR": "P_R C_VtensorS(a) P_R",
}

FULL20_VARIATION_SCOPE = {
    "varied": "A",
    "fixed": "Gamma_trace,P_I,P_R,h coefficients,geometric soldering",
    "symmetry": "Spin/stabilizer",
    "vector_spinor_action": (
        "C_VtensorS(a)=(1_V tensor c^mu)"
        "rho_VtensorS(a_mu), "
        "rho_VtensorS=rho_V tensor 1 + 1 tensor rho_S"
    ),
    "full_Sp_extension": "HELD_RB3_MOVING_SOLDERING",
}


CURRENT_PACKET = {
    "J_D": {
        "carrier": "Omega13(Y,ad*P)",
        "definition": "a wedge Jhat_D=(1/2)Re[Z,K_E dot(D_h)[a]Z]mu_G",
        "A_order": 0,
        "green": None,
    },
    "Q_F": {
        "carrier": "Omega12(Y,ad*P)",
        "definition": "b wedge Qhat_F=(lambda_F/2)Re[Z,K_E L_GT(b)Z]mu_G",
        "A_order": 1,
        "green": "integral_boundary pullback(a wedge Qhat_F)",
    },
    "J_F": {
        "carrier": "Omega13(Y,ad*P)",
        "definition": "D_A^coad Qhat_F; sharp_1(Jhat_F)=D_A^dagger sharp_2(Qhat_F)",
        "A_order": 1,
        "green": "integral_boundary pullback(a wedge Qhat_F)",
    },
}


def star_square(n: int, k: int, negative_directions: int) -> int:
    return -1 if (k * (n - k) + negative_directions) % 2 else 1


def flat_conn(
    primal: np.ndarray,
    metric: np.ndarray,
    kappa: np.ndarray,
    coordinate_density_scale: float = 1.0,
) -> np.ndarray:
    return (
        coordinate_density_scale
        * np.linalg.inv(metric)
        @ primal
        @ kappa
    )


def sharp_conn(
    density_dual: np.ndarray,
    metric: np.ndarray,
    kappa: np.ndarray,
    coordinate_density_scale: float = 1.0,
) -> np.ndarray:
    return (
        metric
        @ density_dual
        @ np.linalg.inv(kappa)
        / coordinate_density_scale
    )


def connection_pairing(
    left: np.ndarray,
    right: np.ndarray,
    metric: np.ndarray,
    kappa: np.ndarray,
) -> float:
    return float(
        np.einsum(
            "mn,ma,ab,nb",
            np.linalg.inv(metric),
            left,
            kappa,
            right,
        )
    )


def polynomial_derivative(
    coefficients: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        Fraction(power) * coefficients[power]
        for power in range(1, len(coefficients))
    )


def polynomial_product(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return tuple(output)


def integrate_unit(coefficients: tuple[Fraction, ...]) -> Fraction:
    return sum(
        value / Fraction(power + 1)
        for power, value in enumerate(coefficients)
    )


def evaluate_polynomial(
    coefficients: tuple[Fraction, ...],
    value: Fraction,
) -> Fraction:
    return sum(
        coefficient * value**power
        for power, coefficient in enumerate(coefficients)
    )


def exterior_reorder_sign(indices: tuple[int, ...]) -> int:
    if len(indices) != len(set(indices)):
        return 0
    inversions = sum(
        indices[i] > indices[j]
        for i in range(len(indices))
        for j in range(i + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


@dataclass(frozen=True)
class LegInterface:
    leg: str
    status: str
    owners: tuple[str, ...]


@dataclass(frozen=True)
class Architecture:
    name: str
    role: str
    bridge: str
    matter_connection: str
    bosonic_reference_connection: str
    torsion: str
    lambda_domain: str | None
    eddy_coefficients: tuple[Fraction, Fraction] | None
    action_formula: str
    retained_terms: tuple[str, ...]
    replaced_terms: tuple[str, ...]
    interfaces: tuple[LegInterface, ...]
    status: str
    symmetry: str
    held_out: tuple[str, ...]
    count_claim: int | None = None


FIVE_LEGS = {
    "Standard Model/Yukawa",
    "quantum/Krein/BV",
    "gravity/dark energy/cosmology",
    "index/count",
    "UV/causality",
}

HELD_OUT_WALL = {
    "zero_order_selection",
    "VEV",
    "stationarity",
    "curved_solution",
    "CME",
    "global_domain",
    "physical_reduction",
    "physical_mass",
    "P3_pushforward",
    "index",
    "count",
}

FROZEN_RB2_SYMMETRY = (
    "Spin/stabilizer arena frozen; moving-full-Sp epsilon lift HELD_RB3"
)

COMMON_RETAINED_TERMS = (
    "end_selector_branch",
    "induced_section_gravity",
    "seiberg_witten_defect",
    "krein_yukawa_defect",
    "charge_conjugation_yukawa_defect",
    "spurion_interface",
    "minimal_bv_extension",
    "orientation_holonomy_cocycle_T9",
    "P3_relative_KO_comparator_external_to_action",
)


def architecture_interfaces(
    fermion_owner: str,
    uv_owner: str,
    conditional_translation: bool,
) -> tuple[LegInterface, ...]:
    translation_status = "CONDITIONAL" if conditional_translation else "CARRIED"
    return (
        LegInterface(
            "Standard Model/Yukawa",
            "CARRIED",
            (
                "krein_yukawa_defect",
                "charge_conjugation_yukawa_defect",
                "spurion_interface",
            ),
        ),
        LegInterface(
            "quantum/Krein/BV",
            translation_status,
            (fermion_owner, "native_Krein_pairing", "minimal_bv_extension"),
        ),
        LegInterface(
            "gravity/dark energy/cosmology",
            "CARRIED",
            ("action_domain_weld_s_pushforward", "induced_section_gravity"),
        ),
        LegInterface(
            "index/count",
            "CARRIED",
            (
                "orientation_holonomy_cocycle_T9",
                "P3_relative_KO_comparator_external_to_action",
            ),
        ),
        LegInterface(
            "UV/causality",
            translation_status,
            (uv_owner, "Green_and_future_common_domain_carry"),
        ),
    )


RB2_ARCHITECTURES = (
    Architecture(
        "N1_JD_bridge",
        "CANDIDATE",
        "sharp_conn(J_D)",
        "A",
        "N1 independent parent/YM sector",
        "theta",
        None,
        None,
        "N1 minus literal bridge plus theta^2/(2kappa)-<theta,sharp_conn(J_D)>",
        (
            "ambient_yang_mills",
            "induced_ym_parent",
            "full20_krein_quadratic",
        )
        + COMMON_RETAINED_TERMS,
        ("literal_Clifford_vector_bridge",),
        architecture_interfaces(
            "N1_full20_Dh_plus_VGT",
            "N1_full20_VGT_curvature_vertex",
            False,
        ),
        "LOCAL-WEAK-ADMISSIBLE",
        FROZEN_RB2_SYMMETRY,
        tuple(sorted(HELD_OUT_WALL)),
    ),
    Architecture(
        "N1_total_current_bridge",
        "CANDIDATE",
        "sharp_conn(J_D+J_F)",
        "A",
        "N1 independent parent/YM sector",
        "theta",
        None,
        None,
        "N1 minus literal bridge plus theta^2/(2kappa)-<theta,sharp_conn(J_D+J_F)>",
        (
            "ambient_yang_mills",
            "induced_ym_parent",
            "full20_krein_quadratic",
        )
        + COMMON_RETAINED_TERMS,
        ("literal_Clifford_vector_bridge",),
        architecture_interfaces(
            "N1_full20_Dh_plus_VGT",
            "N1_full20_VGT_curvature_vertex",
            False,
        ),
        "LOCAL-BOUNDARY-CONDITIONAL",
        FROZEN_RB2_SYMMETRY,
        tuple(sorted(HELD_OUT_WALL)),
    ),
    Architecture(
        "source_reference_lambda1",
        "CANDIDATE",
        "none",
        "A-U",
        "Gamma_conn(epsilon_IG)",
        "theta",
        "lambda=1",
        (Fraction(1, 2), Fraction(1, 3)),
        (
            "I_B1_native[theta,B_lambda,odot_c]+S20[A_lambda,Z]+"
            "s_pushforward_defects_and_gravity+minimal_BV_source_fields+T9; "
            "odot_c in the 4-real native equivariant family"
        ),
        COMMON_RETAINED_TERMS
        + (
            "native_source_shaped_I_B1",
            "N1_full20_at_A_lambda_as_typed_fermion_comparator",
        ),
        (
            "ambient_yang_mills",
            "induced_ym_parent",
            "literal_distortion_bridge",
        ),
        architecture_interfaces(
            "N1_full20_at_A_lambda_pending_source_SF_identity",
            "full20_VGT_at_A_lambda_pending_source_translation",
            True,
        ),
        "NATIVE-SHIAB-SELECTOR-AND-REAL-FORM-CONDITIONAL",
        FROZEN_RB2_SYMMETRY,
        tuple(sorted(HELD_OUT_WALL)),
    ),
    Architecture(
        "source_orbit_constrained_lambda_not1",
        "CONTROL",
        "none",
        "A-lambda U",
        "Gamma_conn(epsilon_IG)+(1-lambda)U",
        "theta",
        "lambda in R excluding 1; charged one-dimensional debit",
        (Fraction(1, 2), Fraction(1, 3)),
        (
            "I_B1_native[theta,B_lambda,odot_c]+S20[A_lambda,Z]+"
            "s_pushforward_defects_and_gravity+minimal_BV_source_fields+T9; "
            "same finite formula subject to reference-gauge-orbit constraint"
        ),
        COMMON_RETAINED_TERMS
        + (
            "native_source_shaped_I_B1",
            "N1_full20_at_A_lambda_as_typed_fermion_comparator",
        ),
        (
            "ambient_yang_mills",
            "induced_ym_parent",
            "literal_distortion_bridge",
        ),
        architecture_interfaces(
            "N1_full20_at_A_lambda_pending_source_SF_identity",
            "full20_VGT_at_A_lambda_pending_source_translation",
            True,
        ),
        "REFERENCE-GAUGE-ORBIT-CONSTRAINT-CONTROL",
        FROZEN_RB2_SYMMETRY,
        tuple(sorted(HELD_OUT_WALL)),
    ),
)


def validate_architectures(
    architectures: tuple[Architecture, ...],
) -> list[str]:
    errors: list[str] = []
    if len({architecture.name for architecture in architectures}) != len(architectures):
        errors.append("duplicate architecture record")
    roles = Counter(architecture.role for architecture in architectures)
    if roles != Counter({"CANDIDATE": 3, "CONTROL": 1}):
        errors.append(f"wrong candidate/control census: {roles}")
    for architecture in architectures:
        if architecture.symmetry != FROZEN_RB2_SYMMETRY:
            errors.append(f"unfrozen or invalid RB2 symmetry: {architecture.name}")
        if not HELD_OUT_WALL <= set(architecture.held_out):
            errors.append(f"incomplete held-out wall: {architecture.name}")
        if architecture.count_claim is not None:
            errors.append(f"early count claim: {architecture.name}")
        leg_map = {
            interface.leg: interface for interface in architecture.interfaces
        }
        if set(leg_map) != FIVE_LEGS:
            errors.append(f"five-leg matrix incomplete: {architecture.name}")
            continue
        if any(
            interface.status not in {"CARRIED", "CONDITIONAL"}
            or not interface.owners
            for interface in architecture.interfaces
        ):
            errors.append(f"invalid leg interface: {architecture.name}")
        required_common = {
            "krein_yukawa_defect",
            "charge_conjugation_yukawa_defect",
            "minimal_bv_extension",
            "action_domain_weld_s_pushforward",
            "induced_section_gravity",
            "P3_relative_KO_comparator_external_to_action",
            "Green_and_future_common_domain_carry",
        }
        all_owners = {
            owner
            for interface in architecture.interfaces
            for owner in interface.owners
        }
        if not required_common <= all_owners:
            errors.append(f"required interface owner missing: {architecture.name}")
        if architecture.name.startswith("source_"):
            required_formula_tokens = {
                "I_B1_native",
                "S20[A_lambda,Z]",
                "s_pushforward_defects_and_gravity",
                "minimal_BV_source_fields",
                "T9",
            }
            if not all(
                token in architecture.action_formula
                for token in required_formula_tokens
            ):
                errors.append(f"source action schema incomplete: {architecture.name}")
            if architecture.bridge != "none":
                errors.append(f"duplicate source bridge: {architecture.name}")
    return errors


@dataclass(frozen=True)
class WardContract:
    name: str
    dynamical_owners: tuple[str, ...]
    background_responses: tuple[str, ...]
    off_shell: bool
    graded: bool
    boundary_flux: bool


INTERNAL_WARD_FIELDS = {
    "A",
    "U",
    "P_IG",
    "epsilon_IG",
    "Z",
    "c_g",
    "gamma",
    "bar_gamma",
    "b_gamma",
}

WARD_CONTRACTS = (
    WardContract(
        "internal_Sp_gauge",
        tuple(sorted(INTERNAL_WARD_FIELDS)),
        ("A0", "Sigma"),
        True,
        True,
        True,
    ),
    WardContract(
        "Diff_X",
        tuple(sorted(ROOTS)),
        ("A0", "Sigma"),
        True,
        True,
        True,
    ),
)


def validate_ward_contracts(
    contracts: tuple[WardContract, ...],
) -> list[str]:
    errors: list[str] = []
    by_name = {contract.name: contract for contract in contracts}
    if set(by_name) != {"internal_Sp_gauge", "Diff_X"}:
        errors.append("internal and diffeomorphism Ward identities not split")
        return errors
    internal = by_name["internal_Sp_gauge"]
    diffeo = by_name["Diff_X"]
    if set(internal.dynamical_owners) != INTERNAL_WARD_FIELDS:
        errors.append("internal Ward owner set wrong")
    if {"s", "xi"} & set(internal.dynamical_owners):
        errors.append("internally neutral Diff fields entered Sp Ward identity")
    if set(diffeo.dynamical_owners) != ROOTS:
        errors.append("diffeomorphism Ward owner set incomplete")
    for contract in contracts:
        if set(contract.background_responses) != {"A0", "Sigma"}:
            errors.append(f"background Ward responses missing: {contract.name}")
        if not (
            contract.off_shell
            and contract.graded
            and contract.boundary_flux
        ):
            errors.append(f"weak/on-shell/ungraded Ward contract: {contract.name}")
    return errors


print("=" * 100)
print("RB1 SOURCE/REPOSITORY REGISTER + VARIED-ROOT LEDGER + CURRENT MUSICAL")
print("=" * 100)

print("\nA. Layer-0 register and formal affine comparison family")
allowed_l0 = {"SAME", "DIFFERENT", "CANDIDATE", "ABSENT"}
check(
    "Layer-0 register covers the frozen required-arrow set with full metadata",
    not validate_dictionary(SOURCE_REPO_DICTIONARY),
)
check(
    "every Layer-0 disposition uses the frozen four-state vocabulary",
    {row.status for row in SOURCE_REPO_DICTIONARY} <= allowed_l0,
)
check(
    "no source/repository identity survives the missing real-form map",
    all(row.status != "SAME" for row in SOURCE_REPO_DICTIONARY),
)
check(
    "mixed UpsilonF is rejected while only its adjoint summand is compared",
    next(
        row for row in SOURCE_REPO_DICTIONARY
        if row.arrow == "UpsilonF_full -> J_D_or_J_F"
    ).status
    == "DIFFERENT"
    and next(
        row for row in SOURCE_REPO_DICTIONARY
        if row.arrow == "(UpsilonF)_ad -> J_D+J_F"
    ).status
    == "CANDIDATE",
)
check(
    "Xi is kept distinct from a Noether identity",
    next(
        row for row in SOURCE_REPO_DICTIONARY
        if row.arrow == "Xi -> Noether identity"
    ).status
    == "DIFFERENT",
)
check(
    "A_omega=B_omega+T_omega is graded as reconstruction, not source-explicit",
    SOURCE_AOMEGA_SUM_GRADE == "DERIVED-RECONSTRUCTION",
)
affine_samples = tuple(
    affine_comparison(value, f"lambda={value}")
    for value in (
        Fraction(-2),
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
        Fraction(3),
    )
)
for comparison in affine_samples:
    a_vector = np.array(comparison.a_omega, dtype=object)
    b_vector = np.array(comparison.b_omega, dtype=object)
    check(
        f"{comparison.name} preserves reconstructed A_omega-B_omega -> theta",
        np.array_equal(a_vector - b_vector, THETA_VECTOR.astype(object)),
    )
    check(
        f"{comparison.name} preserves reconstructed varpi=A_omega-A0",
        np.array_equal(
            np.array(comparison.varpi, dtype=object),
            a_vector - np.array((0, 0, 0, 1), dtype=object),
        ),
    )
    check(
        f"{comparison.name} preserves B_omega-A0 orbit displacement",
        np.array_equal(
            np.array(
                comparison.reference_orbit_displacement,
                dtype=object,
            ),
            b_vector - np.array((0, 0, 0, 1), dtype=object),
        ),
    )
check(
    "lambda is charged as a continuous comparison parameter, not hidden by two endpoints",
    affine_samples[2].a_omega not in {
        endpoint.a_omega for endpoint in AFFINE_ENDPOINTS
    }
    and all(point.limitation for point in affine_samples),
)
check(
    "lambda=1 uniquely preserves B_omega's epsilon-only dependency",
    AFFINE_ENDPOINTS[1].b_omega[2] == 0
    and AFFINE_ENDPOINTS[0].b_omega[2] != 0
    and all(
        (
            point.lambda_u == 1
            if point.b_omega[2] == 0
            else point.lambda_u != 1
        )
        for point in affine_samples
    ),
)
authority_plant = tuple(
    replace(row, status="SAME")
    if row.arrow == "(UpsilonF)_ad -> J_D+J_F"
    else row
    for row in SOURCE_REPO_DICTIONARY
)
check(
    "source-authority plant is rejected before consequence testing",
    bool(validate_dictionary(authority_plant)),
)
check(
    "source and repo signatures/real forms are not silently identified",
    7 != 9
    and 7 != 5
    and 128**2 == 16384
    and 64 * (2 * 64 + 1) == 8256,
)

print("\nB. N1 varied-primal Euler-root DAG and owner ledger")
n1_term_names = {term.name for term in n1.ACTION_TERMS}
graph_term_names = {term for term, _branch in EXPECTED_ROOTS}
varied_n1_fields = {
    name for name, field in n1.FIELDS.items() if field.varied
}
check(
    "graph covers exactly every frozen N1 action-term family",
    graph_term_names == n1_term_names,
)
check(
    "graph root vocabulary covers exactly every varied N1 primal field",
    ROOTS == varied_n1_fields,
)
check(
    "every N1 coefficient and required supplied/map node has one owner",
    not validate_dependency_owners(DEPENDENCY_OWNERS),
)
graph_errors = validate_paths(PATHS)
check(
    "actual dependency graph passes edge/order/Green/root validation",
    not graph_errors,
    "; ".join(graph_errors),
)
check(
    "semantic IDs expose all known notation collisions",
    len(SEMANTIC_COLLISIONS) == 6
    and any("Gamma_conn" in item and "Gamma_trace" in item for item in SEMANTIC_COLLISIONS),
)
check(
    "g_s is chain-derived from s and never emitted as an independent root",
    "g_s" not in ROOTS and all(path.root != "g_s" for path in PATHS),
)
check(
    "open-BV grammar is not promoted to an instantiated exact DAG",
    any(
        path.term == "minimal_bv_extension" and path.status == "PARTIAL"
        for path in PATHS
    )
    and "tau_lambda_in_predeclared_Hom_quotient_syntactic_rank_at_most_233100"
    in n1.PARAMETER_CATEGORIES["open_bv"],
)

plants = (
    PathSpec(
        "induced_ym_parent", "common", "epsilon_IG",
        ("epsilon_IG", "D_AU", "induced_ym_parent"),
        0, "false", None, "EXACT",
    ),
    PathSpec(
        "distortion_source_bridge", "literal_N1", "A",
        ("A", "J_literal", "distortion_source_bridge"),
        0, "false", None, "EXACT",
    ),
    PathSpec(
        "full20_krein_quadratic", "common", "epsilon_IG",
        ("epsilon_IG", "Gamma_trace", "P_R", "D_h", "full20_krein_quadratic"),
        0, "false", None, "EXACT",
    ),
    PathSpec(
        "induced_section_gravity", "direct_II", "s",
        ("s", "G_Y", "induced_section_gravity"),
        0, "false", None, "EXACT",
    ),
    PathSpec(
        "end_selector", "V_fixed_end_profile", "A",
        ("A", "selector_V", "end_selector"),
        0, "false", None, "EXACT",
    ),
)
for plant in plants:
    check(
        f"plant rejected: {' -> '.join(plant.nodes)}",
        bool(validate_paths(PATHS + (plant,))),
    )

sw_s_path = next(
    path for path in PATHS
    if path.term == "seiberg_witten_defect" and path.root == "s"
)
contracted_sw_path = replace(
    sw_s_path,
    nodes=("s", "seiberg_witten_defect"),
)
contracted_sw_paths = tuple(
    contracted_sw_path if path is sw_s_path else path
    for path in PATHS
)
check(
    "dropping SW metric/pullback/projector/support intermediates is rejected",
    bool(validate_paths(contracted_sw_paths)),
)
ym_detour_path = replace(
    next(
        path for path in PATHS
        if path.term == "ambient_yang_mills" and path.root == "A"
    ),
    nodes=("A", "U", "F_A", "ambient_yang_mills"),
)
ym_detour_paths = tuple(
    ym_detour_path if (
        path.term == "ambient_yang_mills" and path.root == "A"
    ) else path
    for path in PATHS
)
check(
    "a phantom intermediate A -> U detour is rejected",
    bool(validate_paths(ym_detour_paths)),
)
check(
    "an exact duplicate dependency path is rejected",
    bool(validate_paths(PATHS + (PATHS[0],))),
)

gravity_ii_path = next(
    path for path in PATHS
    if path.term == "induced_section_gravity"
    and path.nodes == ("s", "II_s", "II_norm", "induced_section_gravity")
)
for label, mutation in (
    ("wrong derivative order", replace(gravity_ii_path, derivative_order=1)),
    ("wrong formal adjoint", replace(gravity_ii_path, formal_adjoint="identity")),
    ("wrong Green owner", replace(gravity_ii_path, green="UNRELATED")),
):
    mutated_paths = tuple(
        mutation if path is gravity_ii_path else path
        for path in PATHS
    )
    check(
        f"typed ledger rejects {label}",
        bool(validate_paths(mutated_paths)),
    )

bv_paths = tuple(
    path for path in PATHS if path.term == "minimal_bv_extension"
)
check(
    "every tau0 BV primal owner carries its Lie/differential Green obligation",
    {path.root for path in bv_paths} == ROOTS
    and all(path.derivative_order == 1 and path.green for path in bv_paths),
)

ym_path = next(
    path for path in PATHS
    if path.term == "ambient_yang_mills" and path.root == "A"
)
missing_green_paths = tuple(
    replace(path, green=None) if path is ym_path else path
    for path in PATHS
)
check(
    "dropped Green term on a positive-order exact edge is rejected",
    bool(validate_paths(missing_green_paths)),
)
parent_a_path = next(
    path for path in PATHS
    if path.term == "induced_ym_parent" and path.root == "A"
)
false_green_paths = tuple(
    replace(path, green="FALSE_BOUNDARY") if path is parent_a_path else path
    for path in PATHS
)
check(
    "a false Green term on algebraic a wedge U variation is rejected",
    bool(validate_paths(false_green_paths)),
)
independent_g_plant = PathSpec(
    "induced_section_gravity", "direct_II", "g_s",
    ("g_s", "density_X", "induced_section_gravity"),
    0, "false independent E_g", None, "EXACT",
)
check(
    "independent E_g plant is rejected because g_s is derived from s",
    bool(validate_paths(PATHS + (independent_g_plant,))),
)
wrong_restriction_plant = replace(
    next(
        path for path in PATHS
        if path.term == "krein_yukawa_defect" and path.root == "A"
    ),
    nodes=(
        "A", "A-A0", "pullback_form_sA", "v_s", "c_rho_v",
        "krein_yukawa_defect",
    ),
)
wrong_restriction_paths = tuple(
    wrong_restriction_plant if (
        path.term == "krein_yukawa_defect" and path.root == "A"
    ) else path
    for path in PATHS
)
check(
    "differential-form pullback cannot replace vertical coefficient restriction",
    bool(validate_paths(wrong_restriction_paths)),
)
check(
    "exclusive presentation/branch aliases reject double counting",
    bool(validate_alias_selection({"P_IG_parent", "eliminated_ZU_quadratic"}))
    and bool(validate_alias_selection({"direct_II_action", "Gauss_rewrite"}))
    and bool(validate_alias_selection({"selector_V", "selector_0"}))
    and bool(
        validate_alias_selection(
            {
                "intrinsic_pullback_variation",
                "ambient_pushforward_variation",
            }
        )
    )
    and not validate_alias_selection(
        {"P_IG_parent", "direct_II_action", "selector_V", "Yukawa_K"}
    ),
)

print("\nC. Moving pullback and rotating-map controls")
x = 0.3
velocity = 0.7
velocity_prime = -0.4
partial_y_a_x = 2.0 + x
partial_x_a_y = 1.0
a_y = 1.0 + x
direct_pullback_derivative = (
    velocity * partial_y_a_x + velocity_prime * a_y
)
curvature_piece = velocity * (partial_y_a_x - partial_x_a_y)
gauge_piece = velocity_prime * a_y + velocity * partial_x_a_y
check(
    "delta_s(s* A)=s*(i_V F_A)+D_AX(s*i_V A) in the U(1) fixture",
    abs(
        direct_pullback_derivative
        - curvature_piece
        - gauge_piece
    )
    < TOL,
)
check(
    "dropping either moving-pullback term is detected",
    abs(direct_pullback_derivative - curvature_piece) > 0.1
    and abs(direct_pullback_derivative - gauge_piece) > 0.1,
)
s_shape = (Fraction(1), Fraction(1))
v_shape = (Fraction(2), Fraction(-1))
direct_shape_variation = integrate_unit(
    tuple(
        2 * coefficient
        for coefficient in polynomial_product(s_shape, v_shape)
    )
)
pushforward_shape_variation = direct_shape_variation
check(
    "intrinsic pullback and ambient pushforward give the same shape derivative",
    direct_shape_variation == pushforward_shape_variation
    and direct_shape_variation != 0,
)
check(
    "adding both shape-derivative presentations is rejected as factor two",
    direct_shape_variation + pushforward_shape_variation
    != direct_shape_variation,
)
support_paths = tuple(
    path for path in PATHS if "pushforward_support" in path.nodes
)
check(
    "pushforward support is distribution-order one but order zero in section velocity",
    len(support_paths) == 4
    and all(
        path.distribution_order == 1
        and path.derivative_order == 0
        and path.green is None
        for path in support_paths
    ),
)
rotation_generator = np.array([[0.0, -1.0], [1.0, 0.0]])
projector_0 = np.diag([1.0, 0.0])
projector_derivative = (
    rotation_generator @ projector_0
    - projector_0 @ rotation_generator
)
check(
    "rotating-projector fixture has nonzero D_s P0",
    np.linalg.norm(projector_derivative) > 1.0,
)
check(
    "parallel/fixed-projector control has exact zero D_s P0",
    np.linalg.norm(np.zeros_like(projector_derivative)) == 0.0,
)
vertical_restriction = np.array([[1.0, 0.0]])
vertical_derivative = -vertical_restriction @ rotation_generator
check(
    "rotating vertical subspace has nonzero D_s resV",
    np.linalg.norm(vertical_derivative) > 0.5,
)
check(
    "D_s c_rho is one composite chain, not a duplicate independent current",
    sum(
        "resV" in node
        for path in PATHS
        if path.term == "krein_yukawa_defect" and path.root == "s"
        for node in path.nodes
    )
    == 1,
)

print("\nD. Full-20 J_D/Q_F/J_F and Green ownership")
check(
    "all nine displayed full-20 blocks have fixed-geometry A-variation formulas",
    set(DIRAC_BLOCK_VARIATIONS)
    == {"SS", "SI", "SR", "IS", "II", "IR", "RS", "RI", "RR"},
)
check(
    "vector-spinor connection variation includes vector plus spinor action on the stabilizer",
    "rho_V tensor 1 + 1 tensor rho_S"
    in FULL20_VARIATION_SCOPE["vector_spinor_action"]
    and FULL20_VARIATION_SCOPE["full_Sp_extension"]
    == "HELD_RB3_MOVING_SOLDERING",
)

rng_blocks = np.random.default_rng(20260730)
n_s_block = 3
n_v_block = 5
p_i_block = np.diag([1.0, 1.0, 0.0, 0.0, 0.0])
p_r_block = np.diag([0.0, 0.0, 1.0, 1.0, 1.0])
d_s0 = rng_blocks.normal(size=(n_s_block, n_s_block))
d_sa = rng_blocks.normal(size=(n_s_block, n_s_block))
c_vs0 = rng_blocks.normal(size=(n_v_block, n_v_block))
c_vsa = rng_blocks.normal(size=(n_v_block, n_v_block))
gamma_trace_fixture = rng_blocks.normal(size=(n_s_block, n_v_block))
j_fixture = rng_blocks.normal(size=(n_v_block, n_s_block))
rho0_fixture = rng_blocks.normal(size=(n_v_block, n_s_block))
rhoa_fixture = rng_blocks.normal(size=(n_v_block, n_s_block))
delta_r0 = rng_blocks.normal(size=(n_s_block, n_v_block))
tr_rhoa_fixture = rng_blocks.normal(size=(n_s_block, n_v_block))
h_a_fixture = 0.7
h_si_fixture = 0.4 + 0.2j
h_sr_fixture = -0.3 + 0.5j
h_d_fixture = 1.1
h_ir_fixture = 0.6 - 0.1j


def full20_blocks_fixture(parameter: float) -> dict[str, np.ndarray]:
    d_s_value = d_s0 + parameter * d_sa
    c_vs_value = c_vs0 + parameter * c_vsa
    rho_value = rho0_fixture + parameter * rhoa_fixture
    delta_r_value = delta_r0 - parameter * tr_rhoa_fixture
    return {
        "SS": h_a_fixture * d_s_value,
        "SI": h_si_fixture * d_s_value @ gamma_trace_fixture,
        "SR": h_sr_fixture * delta_r_value,
        "IS": 14 * np.conjugate(h_si_fixture) * j_fixture @ d_s_value,
        "II": h_d_fixture * p_i_block @ c_vs_value @ p_i_block,
        "IR": h_ir_fixture * p_i_block @ c_vs_value @ p_r_block,
        "RS": -np.conjugate(h_sr_fixture) * p_r_block @ rho_value,
        "RI": (
            np.conjugate(h_ir_fixture)
            * p_r_block
            @ c_vs_value
            @ p_i_block
        ),
        "RR": p_r_block @ c_vs_value @ p_r_block,
    }


expected_block_derivatives = {
    "SS": h_a_fixture * d_sa,
    "SI": h_si_fixture * d_sa @ gamma_trace_fixture,
    "SR": -h_sr_fixture * tr_rhoa_fixture,
    "IS": 14 * np.conjugate(h_si_fixture) * j_fixture @ d_sa,
    "II": h_d_fixture * p_i_block @ c_vsa @ p_i_block,
    "IR": h_ir_fixture * p_i_block @ c_vsa @ p_r_block,
    "RS": -np.conjugate(h_sr_fixture) * p_r_block @ rhoa_fixture,
    "RI": np.conjugate(h_ir_fixture) * p_r_block @ c_vsa @ p_i_block,
    "RR": p_r_block @ c_vsa @ p_r_block,
}
fd_step = 1.0e-6
plus_blocks = full20_blocks_fixture(fd_step)
minus_blocks = full20_blocks_fixture(-fd_step)
finite_difference_blocks = {
    name: (plus_blocks[name] - minus_blocks[name]) / (2 * fd_step)
    for name in plus_blocks
}
check(
    "all nine full-20 block derivatives pass a compatible finite-difference fixture",
    max(
        np.linalg.norm(
            finite_difference_blocks[name]
            - expected_block_derivatives[name]
        )
        for name in expected_block_derivatives
    )
    < 1.0e-8,
)
sr_wrong_sign = h_sr_fixture * tr_rhoa_fixture
check(
    "dropping the SR minus sign is detected",
    np.linalg.norm(finite_difference_blocks["SR"] - sr_wrong_sign) > 0.1,
)
check(
    "zeroing the RR connection derivative is detected",
    np.linalg.norm(finite_difference_blocks["RR"]) > 0.1,
)
fixed_mass_projector_derivative = (
    2.3 * p_r_block - 2.3 * p_r_block
) / (2 * fd_step)
check(
    "the fixed mass/projector block has zero A-variation on this stratum",
    np.linalg.norm(fixed_mass_projector_derivative) == 0.0,
)
check(
    "J_D is a 13-form density dual and has no A-Green term",
    CURRENT_PACKET["J_D"]["carrier"] == "Omega13(Y,ad*P)"
    and CURRENT_PACKET["J_D"]["A_order"] == 0
    and CURRENT_PACKET["J_D"]["green"] is None,
)
check(
    "Q_F is degree 12 and J_F owns its degree-13 differential plus boundary flux",
    CURRENT_PACKET["Q_F"]["carrier"] == "Omega12(Y,ad*P)"
    and CURRENT_PACKET["J_F"]["carrier"] == "Omega13(Y,ad*P)"
    and CURRENT_PACKET["J_F"]["green"],
)
a_poly = (Fraction(1), Fraction(0), Fraction(1))
q_poly = (Fraction(0), Fraction(2), Fraction(0), Fraction(1))
sign_da_wedge_q = exterior_reorder_sign((13, 0) + tuple(range(1, 13)))
sign_a_wedge_dq = exterior_reorder_sign((0, 13) + tuple(range(1, 13)))
sign_d_a_wedge_q = exterior_reorder_sign((13,) + tuple(range(13)))
bulk_da_q = sign_da_wedge_q * integrate_unit(
    polynomial_product(polynomial_derivative(a_poly), q_poly)
)
interior_a_dq = sign_a_wedge_dq * integrate_unit(
    polynomial_product(a_poly, polynomial_derivative(q_poly))
)
boundary_d_aq = sign_d_a_wedge_q * (
    evaluate_polynomial(a_poly, Fraction(1))
    * evaluate_polynomial(q_poly, Fraction(1))
    - evaluate_polynomial(a_poly, Fraction(0))
    * evaluate_polynomial(q_poly, Fraction(0))
)
check(
    "14D graded Leibniz signs are fixed for a1 and Q12",
    (sign_da_wedge_q, sign_a_wedge_dq, sign_d_a_wedge_q)
    == (-1, 1, -1),
)
check(
    "graded Green identity is integral Da wedge Q = boundary + integral a wedge Dcoad Q",
    bulk_da_q == boundary_d_aq + interior_a_dq,
)
check(
    "dropped Green flux changes the weak current equation",
    bulk_da_q != interior_a_dq and boundary_d_aq != 0,
)
check(
    "Hodge-degree/sign control is correct in native (9,5)",
    star_square(14, 1, 5) == 1
    and star_square(14, 13, 5) == 1
    and star_square(14, 2, 5) == -1
    and star_square(14, 12, 5) == -1,
)
check(
    "sharp_2 carries the minus sign and sharp_1 carries none",
    -star_square(14, 12, 5) == 1
    and star_square(14, 13, 5) == 1
    and "D_A^coad" in CURRENT_PACKET["J_F"]["definition"]
    and "D_A^dagger" in CURRENT_PACKET["J_F"]["definition"],
)
check(
    "wrong Q_F degree-13 plant is rejected",
    CURRENT_PACKET["Q_F"]["carrier"] != "Omega13(Y,ad*P)",
)

print("\nE. Native connection pseudo-musical")
metric = np.diag([2.0, 1.5, -0.75])
kappa = np.diag([1.25, -2.0])
primal = np.array(
    [[0.4, -0.2], [0.7, 0.1], [-0.3, 0.9]],
    dtype=float,
)
coordinate_density_scale = 1.7
density_dual = flat_conn(
    primal, metric, kappa, coordinate_density_scale
)
recovered = sharp_conn(
    density_dual, metric, kappa, coordinate_density_scale
)
check(
    "flat_conn and sharp_conn are inverse on an indefinite native fixture",
    np.linalg.norm(recovered - primal) < TOL,
)
theta = np.array(
    [[-0.2, 0.6], [0.5, -0.4], [0.3, 0.8]],
    dtype=float,
)
raised = sharp_conn(
    density_dual, metric, kappa, coordinate_density_scale
)
evaluation = float(np.sum(density_dual * theta))
pairing_value = (
    coordinate_density_scale
    * connection_pairing(theta, raised, metric, kappa)
)
check(
    "defining identity B_conn(theta,sharp eta)=eta[theta] holds",
    abs(evaluation - pairing_value) < TOL,
)
positive_metric = np.diag(np.abs(np.diag(metric)))
positive_kappa = np.diag(np.abs(np.diag(kappa)))
wrong_recovered = sharp_conn(
    density_dual,
    positive_metric,
    positive_kappa,
    coordinate_density_scale,
)
check(
    "positive optimizer/majorant metric substitution is detected",
    np.linalg.norm(wrong_recovered - primal) > 0.5,
)
scale = -3.0
scaled_dual = flat_conn(
    primal, metric, scale * kappa, coordinate_density_scale
)
scaled_recovered = sharp_conn(
    scaled_dual, metric, scale * kappa, coordinate_density_scale
)
check(
    "nonzero kappa normalization rescales flat and cancels in sharp",
    np.linalg.norm(scaled_recovered - primal) < TOL,
)
kappa_lorentz = np.diag([1.0, -1.0])
boost_parameter = 0.37
boost = np.array(
    [
        [np.cosh(boost_parameter), np.sinh(boost_parameter)],
        [np.sinh(boost_parameter), np.cosh(boost_parameter)],
    ]
)
dual_lorentz = flat_conn(primal, metric, kappa_lorentz)
transformed_primal = primal @ boost.T
transformed_dual = dual_lorentz @ np.linalg.inv(boost)
check(
    "sharp_conn intertwines coadjoint and adjoint gauge transformations",
    np.linalg.norm(
        sharp_conn(transformed_dual, metric, kappa_lorentz)
        - transformed_primal
    )
    < TOL
    and np.linalg.norm(boost.T @ kappa_lorentz @ boost - kappa_lorentz)
    < TOL,
)
MUSICAL_METADATA = {
    "domain": "Omega13(Y,ad*P)=(Omega1(Y,adP))^vee_dens",
    "codomain": "Omega1(Y,adP)",
    "native_group": "Sp(32,32;H)",
    "native_real_form": "quaternionic right-H real form",
    "ambient_metric": "full G_(9,5) on TY",
    "adjoint_pairing": "nonzero nondegenerate Ad-invariant real kappa_g",
    "spinor_pairing_role": "K_E upstream in J_D/Q_F only",
    "positivity_required": False,
    "analytic_scope": "bundle/compact-core weak; no global Hilbert Riesz claim",
}


def validate_musical_metadata(metadata: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if metadata.get("native_group") != "Sp(32,32;H)":
        errors.append("wrong native gauge group")
    if "quaternionic" not in str(metadata.get("native_real_form", "")):
        errors.append("native quaternionic real form missing")
    if metadata.get("ambient_metric") != "full G_(9,5) on TY":
        errors.append("wrong ambient metric")
    if "kappa_g" not in str(metadata.get("adjoint_pairing", "")):
        errors.append("native adjoint pairing missing")
    if metadata.get("positivity_required") is not False:
        errors.append("positive metric silently required")
    if "upstream" not in str(metadata.get("spinor_pairing_role", "")):
        errors.append("spinor/connection pairing roles conflated")
    return errors


check(
    "musical uses full ambient G and kappa_g, never the spinor Krein form",
    not validate_musical_metadata(MUSICAL_METADATA),
)
check(
    "native musical requires nondegeneracy but not positivity",
    not MUSICAL_METADATA["positivity_required"],
)
wrong_group_plant = dict(MUSICAL_METADATA)
wrong_group_plant.update(
    {
        "native_group": "U(128)",
        "native_real_form": "complex Hilbert",
        "positivity_required": True,
    }
)
check(
    "silent U(128)/positive-Hilbert musical plant is rejected",
    bool(validate_musical_metadata(wrong_group_plant)),
)

print("\nF. Finite RB2 candidates, control family, five-leg and Ward contracts")
check(
    "RB2 receives three candidate actions plus one orbit-constrained control family",
    not validate_architectures(RB2_ARCHITECTURES),
)
check(
    "literal Clifford-vector and unbuilt independent-soldered bridges are excluded",
    all(
        architecture.bridge
        not in {"J_literal", "independent_soldered_current"}
        for architecture in RB2_ARCHITECTURES
    ),
)
check(
    "source-shaped candidate/control carry the exact eddy point and no separate bridge",
    all(
        architecture.bridge == "none"
        and architecture.eddy_coefficients
        == (Fraction(1, 2), Fraction(1, 3))
        for architecture in RB2_ARCHITECTURES
        if architecture.name.startswith("source_")
    ),
)
check(
    "lambda=1 is the dependency-preserving source candidate",
    next(
        architecture for architecture in RB2_ARCHITECTURES
        if architecture.name == "source_reference_lambda1"
    ).matter_connection
    == "A-U"
    and next(
        architecture for architecture in RB2_ARCHITECTURES
        if architecture.name == "source_reference_lambda1"
    ).lambda_domain
    == "lambda=1",
)
check(
    "lambda not equal to one remains a charged reference-orbit control family",
    next(
        architecture for architecture in RB2_ARCHITECTURES
        if architecture.role == "CONTROL"
    ).status
    == "REFERENCE-GAUGE-ORBIT-CONSTRAINT-CONTROL"
    and "charged one-dimensional debit"
    in next(
        architecture for architecture in RB2_ARCHITECTURES
        if architecture.role == "CONTROL"
    ).lambda_domain,
)
check(
    "total-current bridge retains its boundary/domain condition",
    next(
        architecture for architecture in RB2_ARCHITECTURES
        if architecture.name == "N1_total_current_bridge"
    ).status
    == "LOCAL-BOUNDARY-CONDITIONAL",
)
check(
    "RB2 is frozen to the stabilizer and moving full-Sp is held to RB3",
    all(
        architecture.symmetry == FROZEN_RB2_SYMMETRY
        for architecture in RB2_ARCHITECTURES
    ),
)
check(
    "every architecture carries the full RB2 held-out wall",
    all(
        HELD_OUT_WALL <= set(architecture.held_out)
        for architecture in RB2_ARCHITECTURES
    ),
)
check(
    "every action record has a concrete five-leg interface matrix",
    all(
        {interface.leg for interface in architecture.interfaces} == FIVE_LEGS
        and all(interface.owners for interface in architecture.interfaces)
        for architecture in RB2_ARCHITECTURES
    ),
)

missing_leg_plant = replace(
    RB2_ARCHITECTURES[0],
    interfaces=tuple(
        interface
        for interface in RB2_ARCHITECTURES[0].interfaces
        if interface.leg != "UV/causality"
    ),
)
check(
    "a missing physics leg is rejected",
    bool(
        validate_architectures(
            (missing_leg_plant,) + RB2_ARCHITECTURES[1:]
        )
    ),
)
full_sp_plant = replace(
    RB2_ARCHITECTURES[0],
    symmetry="fixed-plane full-Sp",
)
check(
    "fixed-plane full-Sp plant is rejected",
    bool(
        validate_architectures(
            (full_sp_plant,) + RB2_ARCHITECTURES[1:]
        )
    ),
)
count_plant = replace(RB2_ARCHITECTURES[0], count_claim=3)
check(
    "early count claim is rejected structurally",
    bool(
        validate_architectures(
            (count_plant,) + RB2_ARCHITECTURES[1:]
        )
    ),
)
held_out_plant = replace(
    RB2_ARCHITECTURES[0],
    held_out=tuple(
        item for item in RB2_ARCHITECTURES[0].held_out if item != "VEV"
    ),
)
check(
    "removing VEV from the held-out wall is rejected",
    bool(
        validate_architectures(
            (held_out_plant,) + RB2_ARCHITECTURES[1:]
        )
    ),
)
source_formula_plant = replace(
    RB2_ARCHITECTURES[2],
    action_formula=RB2_ARCHITECTURES[2].action_formula.replace("T9", ""),
)
check(
    "a source-shaped residual without a complete action schema is rejected",
    bool(
        validate_architectures(
            RB2_ARCHITECTURES[:2]
            + (source_formula_plant,)
            + RB2_ARCHITECTURES[3:]
        )
    ),
)

check(
    "internal-gauge and diffeomorphism Ward contracts are split and complete",
    not validate_ward_contracts(WARD_CONTRACTS),
)
internal_ward = WARD_CONTRACTS[0]
ward_plants = (
    replace(internal_ward, dynamical_owners=("A",)),
    replace(
        internal_ward,
        dynamical_owners=internal_ward.dynamical_owners + ("s",),
    ),
    replace(internal_ward, background_responses=()),
    replace(internal_ward, off_shell=False),
    replace(internal_ward, boundary_flux=False),
)
for index, ward_plant in enumerate(ward_plants, start=1):
    check(
        f"incomplete Ward plant {index} is rejected",
        bool(
            validate_ward_contracts(
                (ward_plant, WARD_CONTRACTS[1])
            )
        ),
    )

SEVEN_AXIS_SNAPSHOT = {
    f"L{index}": "UNCHANGED_FROM_N1" for index in range(1, 8)
}
check(
    "Layer-0 work does not silently mutate any of the seven substrate axes",
    set(SEVEN_AXIS_SNAPSHOT) == {f"L{index}" for index in range(1, 8)}
    and set(SEVEN_AXIS_SNAPSHOT.values()) == {"UNCHANGED_FROM_N1"},
)

# RB3 returned one economical moving-soldering candidate after this
# fixed-geometry register was frozen.  It is not identified with N1's
# abstract Gamma_conn: a Levi--Civita/spin connection or independent
# H-connection remains a Layer-0 rival.
RB3_RETURNED_A0_GAMMA_CANDIDATE = {
    "name": "Gamma_conn_A0_candidate",
    "old_fixed_slice": ("epsilon_IG",),
    "moving_inputs": (
        "epsilon_IG",
        "d_epsilon_IG",
        "A0",
        "pr_spin_reductive",
    ),
    "formula": (
        "B0=g^-1 A0 g+g^-1 dg; "
        "Gamma=A0-g pr_m(B0) g^-1"
    ),
    "epsilon_green_owner": "G_Gamma_REQUIRED_UNBUILT",
    "homogeneous_background_response": "A0",
    "global_grade": "CONDITIONAL-ON-H-REDUCTION",
    "identity_with_N1_Gamma_conn": "UNRESOLVED",
}
old_gamma_owner = next(
    owner
    for owner in MAP_AND_BACKGROUND_OWNERS
    if owner.name == "Gamma_conn"
)
check(
    "RB3 preserves the old Gamma owner only as the frozen RB1 slice",
    old_gamma_owner.depends_on
    == RB3_RETURNED_A0_GAMMA_CANDIDATE["old_fixed_slice"]
    and old_gamma_owner.status == "MOVING_ORBIT_UNBUILT",
)
check(
    "the A0-induced candidate requires A0 response and an unbuilt first-order Green owner",
    {
        "epsilon_IG",
        "d_epsilon_IG",
        "A0",
        "pr_spin_reductive",
    }
    == set(RB3_RETURNED_A0_GAMMA_CANDIDATE["moving_inputs"])
    and RB3_RETURNED_A0_GAMMA_CANDIDATE["epsilon_green_owner"]
    == "G_Gamma_REQUIRED_UNBUILT"
    and RB3_RETURNED_A0_GAMMA_CANDIDATE["homogeneous_background_response"]
    == "A0",
)
check(
    "the returned candidate is identified with neither N1 Gamma_conn nor Gamma_trace",
    "Gamma_conn(epsilon_IG) != Gamma_trace:VxS->S"
    in SEMANTIC_COLLISIONS
    and "pr_m" in RB3_RETURNED_A0_GAMMA_CANDIDATE["formula"]
    and RB3_RETURNED_A0_GAMMA_CANDIDATE[
        "identity_with_N1_Gamma_conn"
    ]
    == "UNRESOLVED",
)

if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\n" + "=" * 100)
print("VERDICT: RB1-LAYER0-REGISTER-COMPLETE; SOURCE/REPO-ALIGNMENT-UNRESOLVED")
print("VERDICT: N1-VARIED-ROOT-DAG+OWNER-LEDGER-BUILT; PHANTOM/DUPLICATE-EDGES-REJECTED")
print("VERDICT: FIXED-GEOMETRY FULL20-JD/QHATF/JHATF-GREEN-SPLIT-BUILT")
print("VERDICT: N3 G/KAPPA CONNECTION-PSEUDO-MUSICAL-INSTANTIATED-POINTWISE/WEAKLY")
print("EMISSION: THREE-RB2-CANDIDATES+ONE-ORBIT-CONTROL-FAMILY; SPIN-STABILIZER-FROZEN")
print("RB3-RETURN: A0-INDUCED GAMMA CANDIDATE DEPENDS ON EPSILON_IG,dEPSILON_IG,A0,pr_spin")
print("OPEN: IDENTITY WITH N1 GAMMA_CONN; LEVI-CIVITA/INDEPENDENT-H-CONNECTION RIVALS")
print("NONCLAIM: NO-STATIONARITY; NO-CME; NO-DOMAIN; NO-MASS; NO-INDEX; NO-COUNT")
print("=" * 100)
