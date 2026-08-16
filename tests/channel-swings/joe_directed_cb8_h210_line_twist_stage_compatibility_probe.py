#!/usr/bin/env python3
"""Exact CB-8C line-twist, stage, and CB-6 compatibility classifier.

H210 and every q/line datum are declared conditional horns.  This probe
classifies types and functor order; it never constructs or selects q_H, an
observer, a graph, an action, a reduction, or a physical quotient.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / (
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb8-h210-line-twist-stage-cb6-compatibility-2026-08-16.md"
)


@dataclass(frozen=True)
class Stage:
    name: str
    base: str
    order: int
    can_change_source_equation: bool


@dataclass(frozen=True)
class Branch:
    name: str
    stage: Stage
    grammar: str
    line: bool = True
    section: bool = False
    coherent_transport: bool = False
    nowhere_null: bool = False
    h210_line_lift: bool = False
    line_stage_bridge: bool = False


Y = Stage("source-Y", "Y", 0, True)
X = Stage("pullback-X", "X", 1, False)
HJ = Stage("graph-H_J", "X", 2, False)
STAGES = (Y, X, HJ)

UNTWISTED = "untwisted"
LINE_DUAL = "line-dual"


def derivative_typed(branch: Branch) -> bool:
    """Whether the derivative adapter has its declared target type."""
    if not branch.line:
        return False
    if branch.grammar == UNTWISTED:
        # Evaluation c(q,-) needs an actual section, not just its line.
        return branch.section
    if branch.grammar == LINE_DUAL:
        # Currying c|_L gives S -> L* tensor S from the bare line.
        return True
    raise ValueError(branch.grammar)


def h210_typed(branch: Branch) -> bool:
    """Whether unchanged H210 has the same target as the derivative."""
    if branch.grammar == UNTWISTED:
        return True
    if branch.grammar == LINE_DUAL:
        return branch.h210_line_lift
    raise ValueError(branch.grammar)


def full_cell_typed(branch: Branch) -> bool:
    return derivative_typed(branch) and h210_typed(branch)


def repairs_original_source_cell(branch: Branch) -> bool:
    """Only an untwisted, coherent source-Y branch repairs eq. (9.16)."""
    return (
        branch.stage.can_change_source_equation
        and branch.grammar == UNTWISTED
        and full_cell_typed(branch)
        and branch.coherent_transport
    )


def defines_new_line_valued_source_cell(branch: Branch) -> bool:
    return (
        branch.stage.can_change_source_equation
        and branch.grammar == LINE_DUAL
        and full_cell_typed(branch)
        and branch.coherent_transport
    )


def preserves_adapter_rank(branch: Branch) -> bool:
    """Clifford multiplication is invertible only off the null cone."""
    return derivative_typed(branch) and branch.section and branch.nowhere_null


def observed_only(branch: Branch) -> bool:
    return full_cell_typed(branch) and not branch.stage.can_change_source_equation


def cb6_target(branch: Branch) -> str:
    """Target of the isolated Z -> O -> Gamma -> kappa chain."""
    if branch.grammar == UNTWISTED:
        return "F_corr"
    if branch.grammar == LINE_DUAL and branch.h210_line_lift and branch.line_stage_bridge:
        return "L_H* tensor F_corr"
    return "TYPE_MISSING"


def validate_semantics(state: dict[str, object]) -> None:
    forbidden = (
        "constructed_q",
        "selected_q",
        "x_repairs_y_without_lift",
        "hj_repairs_y_without_bridge",
        "bare_line_is_endomorphism",
        "derivative_is_z144",
        "derivative_recovers_z144",
        "kappa_before_observation",
        "kappa_in_varpi",
        "f_is_z",
        "f_is_m3",
        "deleted_half",
        "physical_chirality",
        "named_family",
        "mass_or_spectrum",
        "derived_action",
        "selected_graph",
        "constructed_reduction",
        "physical_quotient",
    )
    if any(state.get(flag) for flag in forbidden):
        raise AssertionError("forbidden stage, custody, or physical promotion")
    branch = state.get("branch")
    if branch is not None:
        assert isinstance(branch, Branch)
        if state.get("claims_source_repair") and not repairs_original_source_cell(branch):
            raise AssertionError("source repair claimed without source-stage untwisted horn")
        if state.get("claims_line_cell") and not defines_new_line_valued_source_cell(branch):
            raise AssertionError("line-valued cell claimed without H210 line lift")
        if state.get("claims_rank_preserved") and not preserves_adapter_rank(branch):
            raise AssertionError("rank preservation claimed on zero/null or unsectioned line")
        claimed_cb6 = state.get("claimed_cb6_target")
        if claimed_cb6 is not None and claimed_cb6 != cb6_target(branch):
            raise AssertionError("CB-6 target forgot the line twist or stage bridge")


def exact_checks() -> list[str]:
    passed: list[str] = []

    assert [stage.order for stage in STAGES] == [0, 1, 2]
    assert [stage.base for stage in STAGES] == ["Y", "X", "X"]
    assert [stage.can_change_source_equation for stage in STAGES] == [True, False, False]
    passed.append("source-Y/pullback-X/graph-H_J stage order")

    bare = Branch("bare source line", Y, UNTWISTED)
    sectioned = Branch(
        "coherent source section", Y, UNTWISTED,
        section=True, coherent_transport=True, nowhere_null=True,
    )
    null_section = Branch(
        "null source section", Y, UNTWISTED,
        section=True, coherent_transport=True, nowhere_null=False,
    )
    curried = Branch(
        "curried bare line", Y, LINE_DUAL, coherent_transport=True,
    )
    line_cell = Branch(
        "line-valued source grammar", Y, LINE_DUAL,
        coherent_transport=True, h210_line_lift=True,
        line_stage_bridge=True,
    )
    x_section = Branch(
        "independent pullback section", X, UNTWISTED,
        section=True, coherent_transport=True, nowhere_null=True,
    )
    hj_section = Branch(
        "graph-plane section", HJ, UNTWISTED,
        section=True, coherent_transport=True, nowhere_null=True,
    )

    assert not derivative_typed(bare)
    assert derivative_typed(sectioned)
    passed.append("bare line versus evaluated Clifford endomorphism")

    assert derivative_typed(curried)
    assert not h210_typed(curried)
    assert not full_cell_typed(curried)
    passed.append("canonical curried derivative has L_H* target but unchanged H210 does not")

    assert full_cell_typed(line_cell)
    assert not repairs_original_source_cell(line_cell)
    assert defines_new_line_valued_source_cell(line_cell)
    passed.append("line-valued H210 lift defines a new source grammar, not the original target")

    assert repairs_original_source_cell(sectioned)
    # Nullness is a rank fence, not a bundle-typing fence.
    assert full_cell_typed(null_section) and repairs_original_source_cell(null_section)
    assert preserves_adapter_rank(sectioned) and not preserves_adapter_rank(null_section)
    passed.append("source section types the cell while nowhere-nullness separately protects rank")

    # Reproduce the CB-7 candidate class rather than silently changing its
    # half or form-degree grammar.  Half bits are plus=0 and minus=1.
    forward_cells = {
        (1, 2): {"input_half": 0, "row_half": 0, "degree": (0, 1)},
        (0, 3): {"input_half": 1, "row_half": 1, "degree": (0, 1)},
    }
    derivative_half_parity = 0
    gamma_q_half_parity = 1
    h210_half_parity = 1
    opposite_density_dual = 1
    assert set(forward_cells) == {(1, 2), (0, 3)}
    assert all(
        cell["input_half"] ^ derivative_half_parity ^ gamma_q_half_parity
        == cell["row_half"] ^ opposite_density_dual
        == cell["input_half"] ^ h210_half_parity
        for cell in forward_cells.values()
    )
    assert all(cell["degree"] == (0, 1) for cell in forward_cells.values())
    passed.append("CB-7 odd-derivative/opposite-dual parity and Omega0-to-Omega1 degree")

    assert observed_only(x_section) and observed_only(hj_section)
    assert not repairs_original_source_cell(x_section)
    assert not repairs_original_source_cell(hj_section)
    passed.append("X and H_J data decorate only post-pullback operators")

    assert cb6_target(sectioned) == "F_corr"
    assert cb6_target(line_cell) == "L_H* tensor F_corr"
    no_line_bridge = Branch(
        "line cell without stage bridge", Y, LINE_DUAL,
        coherent_transport=True, h210_line_lift=True,
    )
    assert cb6_target(no_line_bridge) == "TYPE_MISSING"
    passed.append("CB-6 chain is unchanged or tensor-extended only with an explicit line-stage bridge")

    # Exact sequence 0 -> C --q--> L -> 0 in a one-dimensional fibre holds
    # precisely when q is nonzero.  Isotropic nonzero q still trivializes L,
    # but Clifford multiplication is not invertible.
    fibre_sections = {
        "zero": (0, False, False),
        "nonzero-null": (1, True, False),
        "nonzero-nonnull": (1, True, True),
    }
    assert Counter(rank for rank, _, _ in fibre_sections.values()) == {1: 2, 0: 1}
    assert all((rank == 1) == trivial for rank, trivial, _ in fibre_sections.values())
    assert [name for name, (_, _, invertible) in fibre_sections.items() if invertible] == ["nonzero-nonnull"]
    passed.append("line trivialization exact-sequence and null-cone control")

    # Both source halves carry the same stage fingerprint.  The H210 images
    # are internal Z partners; the derivative images are only total-zeta.
    halves = {
        "A": ("nu+", "bar-zeta+", "Z/144bar", "total-zeta", "F_corr,-"),
        "B": ("nu-", "bar-zeta-", "Z/144", "total-zeta", "F_corr,+"),
    }
    assert set(halves) == {"A", "B"}
    assert {row[2] for row in halves.values()} == {"Z/144", "Z/144bar"}
    assert {row[3] for row in halves.values()} == {"total-zeta"}
    assert {row[4] for row in halves.values()} == {"F_corr,+", "F_corr,-"}
    passed.append("both-half Z-partner versus total-zeta custody")

    # The only accepted functor words keep the isolated H210 port forward.
    accepted_words = {
        ("Z", "O_J", "Gamma_H_intr", "kappa_J", "F_corr"),
        ("L*Z", "id_L* tensor O_J", "id_L* tensor Gamma_H_intr",
         "id_L* tensor kappa_J", "L*F_corr"),
    }
    assert all(word.index("O_J") < word.index("Gamma_H_intr") < word.index("kappa_J")
               for word in accepted_words if "O_J" in word)
    assert ("Z", "kappa_J", "O_J", "Gamma_H_intr", "F_corr") not in accepted_words
    passed.append("forward CB-6 functor order and tensor-extension control")

    # Pullback naturality is conditional on q_X being the actual pullback of
    # q_Y.  Equality of base dimensions or a same-named line is insufficient.
    pullback_cases = {
        "declared q_X=s*q_Y": True,
        "independent q_X": False,
        "graph q_HJ": False,
    }
    assert sum(pullback_cases.values()) == 1
    passed.append("source-to-observed q pullback bridge classifier")

    validate_semantics({"branch": sectioned, "claims_source_repair": True,
                        "claims_rank_preserved": True,
                        "claimed_cb6_target": "F_corr"})
    validate_semantics({"branch": line_cell, "claims_line_cell": True,
                        "claimed_cb6_target": "L_H* tensor F_corr"})
    passed.append("two surviving conditional branch states")
    return passed


def semantic_mutants() -> list[tuple[str, dict[str, object]]]:
    x_section = Branch("X", X, UNTWISTED, section=True, coherent_transport=True,
                       nowhere_null=True)
    bare = Branch("bare", Y, UNTWISTED)
    curried = Branch("curried", Y, LINE_DUAL, coherent_transport=True)
    null_section = Branch("null", Y, UNTWISTED, section=True,
                          coherent_transport=True, nowhere_null=False)
    line_no_bridge = Branch("line-no-bridge", Y, LINE_DUAL,
                            coherent_transport=True, h210_line_lift=True)
    flags = [
        "constructed_q", "selected_q", "x_repairs_y_without_lift",
        "hj_repairs_y_without_bridge", "bare_line_is_endomorphism",
        "derivative_is_z144", "derivative_recovers_z144",
        "kappa_before_observation", "kappa_in_varpi", "f_is_z", "f_is_m3",
        "deleted_half", "physical_chirality", "named_family",
        "mass_or_spectrum", "derived_action", "selected_graph",
        "constructed_reduction", "physical_quotient",
    ]
    mutants = [(flag.replace("_", " "), {flag: True}) for flag in flags]
    mutants.extend([
        ("X section promoted upstream", {"branch": x_section, "claims_source_repair": True}),
        ("bare line called source repair", {"branch": bare, "claims_source_repair": True}),
        ("curried derivative called full line cell", {"branch": curried, "claims_line_cell": True}),
        ("null section called rank preserving", {"branch": null_section, "claims_rank_preserved": True}),
        ("line twist erased at CB6 target", {"branch": line_no_bridge,
                                             "claimed_cb6_target": "F_corr"}),
    ])
    return mutants


def artifact_checks() -> list[str]:
    text = ARTIFACT.read_text(encoding="utf-8")
    required = (
        "GU-COMPARATOR-ROUTING",
        "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "L_H \\otimes S \\longrightarrow S",
        "S \\longrightarrow L_H^* \\otimes S",
        "source `Y`",
        "pullback `X`",
        "graph plane `H_J`",
        "total `zeta` bundle",
        "Z/internal-`144`",
        "M_3",
        "F/imposter",
        "O_J \\longrightarrow \\Gamma_{H,J}^{\\mathrm{intr}} \\longrightarrow \\kappa_J",
        "both conjugate halves",
        "does not construct or select `q_H`",
        "Strict inference ceiling",
    )
    missing = [token for token in required if token not in text]
    assert not missing, f"artifact missing required tokens: {missing}"
    return ["artifact routing, type, stage, custody, order, both-half, and scope contract"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    passed = exact_checks() + artifact_checks()
    fired = 0
    if args.selftest:
        for name, mutant in semantic_mutants():
            try:
                validate_semantics(mutant)
            except AssertionError:
                fired += 1
                print(f"MUTANT FIRED: {name}")
            else:
                print(f"MUTANT SURVIVED: {name}")
        assert fired == len(semantic_mutants())

    for item in passed:
        print(f"PASS: {item}")
    print(f"CB8-C PASS ({len(passed)} exact groups; {fired} semantic mutants fired)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
