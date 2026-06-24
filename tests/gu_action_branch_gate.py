"""Branch gate checker for the closed-loop GU action / IG lane.

This is not a physics simulation. It records the explicit logical outcomes of the
branch analysis in explorations/gu-closed-loop-action-ig-branch-2026-06-24.md.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Iterable


@dataclass(frozen=True)
class BranchOutcome:
    key: str
    label: str
    nonzero_theta: str
    source_equation: str
    exact_schwarzschild_kerr: str
    flrw_xi_gate: str
    decision: str
    proof_obligation: str

    @property
    def derives_negative_xi(self) -> bool:
        return self.flrw_xi_gate.startswith("PASS")

    @property
    def passes_exact_gr(self) -> bool:
        return self.exact_schwarzschild_kerr.startswith("PASS")


BRANCHES: tuple[BranchOutcome, ...] = (
    BranchOutcome(
        key="background_stueckelberg",
        label="Background/Stueckelberg IG variables",
        nonzero_theta="PASS: no free beta EL equation",
        source_equation="PASS: D_A^*F_A = theta after normalization",
        exact_schwarzschild_kerr=(
            "OPEN_FAIL: exact Willmore residual not cancelled by a derived full EL solution"
        ),
        flrw_xi_gate="FAIL_UNPROVED: no generated xi_eff coefficient",
        decision="viable but physically thin",
        proof_obligation=(
            "derive section variation and FLRW reduction from fixed-spurion action"
        ),
    ),
    BranchOutcome(
        key="constrained_ig_a_independent",
        label="A-independent constrained IG",
        nonzero_theta="PASS_CONDITIONAL: constraint removes free beta variations",
        source_equation="PASS: D_A^*F_A = theta",
        exact_schwarzschild_kerr=(
            "OPEN_FAIL: full E_s cancellation for Schwarzschild/Kerr not shown"
        ),
        flrw_xi_gate="FAIL_UNPROVED: xi_eff undefined until Phi and reduction are explicit",
        decision="recommended branch",
        proof_obligation=(
            "derive Phi(eps,beta,s)=0 from written GU action or tau-plus/IG geometry"
        ),
    ),
    BranchOutcome(
        key="constrained_ig_a_dependent",
        label="A-dependent constrained IG",
        nonzero_theta="PASS_CONDITIONAL: constraint removes free beta variations",
        source_equation=(
            "CORRECTED: D_A^*F_A = theta - g_A^2(D_A Phi)^*lambda"
        ),
        exact_schwarzschild_kerr=(
            "OPEN_FAIL: multiplier current and section equation not solved"
        ),
        flrw_xi_gate="FAIL_UNPROVED: no generated xi_eff coefficient",
        decision="possible but source equation changes",
        proof_obligation="show multiplier term vanishes or rewrite canon source law",
    ),
    BranchOutcome(
        key="dynamical_ig_total_current",
        label="Dynamical IG / total current",
        nonzero_theta="PASS: IG equation is differential, not theta=0",
        source_equation="REVISED: D_A^*F_A = theta_eff = c_theta theta - J_IG",
        exact_schwarzschild_kerr=(
            "OPEN_FAIL: no full vacuum EL solution for Schwarzschild/Kerr"
        ),
        flrw_xi_gate="FAIL_UNPROVED: strongest route, but xi_eff is not computed",
        decision="honest fallback if no constraint is sourced",
        proof_obligation="write S_IG-dyn, derive total current, compute xi_eff",
    ),
    BranchOutcome(
        key="bare_free_beta_norm",
        label="Bare free-beta theta norm",
        nonzero_theta="FAIL: E_beta forces theta=0",
        source_equation="FAIL: source collapses to D_A^*F_A=0",
        exact_schwarzschild_kerr="FAIL: Willmore-only obstruction remains",
        flrw_xi_gate="FAIL: theta mode killed",
        decision="reject",
        proof_obligation="none; branch is structurally broken",
    ),
)


def select(branch_key: str | None) -> Iterable[BranchOutcome]:
    if branch_key is None:
        return BRANCHES
    matches = [branch for branch in BRANCHES if branch.key == branch_key]
    if not matches:
        valid = ", ".join(branch.key for branch in BRANCHES)
        raise SystemExit(f"unknown branch {branch_key!r}; valid branches: {valid}")
    return matches


def summarize(branches: Iterable[BranchOutcome]) -> dict[str, object]:
    branch_list = list(branches)
    return {
        "recommended_branch": "constrained_ig_a_independent",
        "any_branch_derives_negative_xi": any(
            branch.derives_negative_xi for branch in BRANCHES
        ),
        "any_branch_passes_exact_schwarzschild_kerr": any(
            branch.passes_exact_gr for branch in BRANCHES
        ),
        "branches": [asdict(branch) for branch in branch_list],
    }


def print_text(summary: dict[str, object]) -> None:
    print(f"recommended_branch: {summary['recommended_branch']}")
    print(f"any_branch_derives_negative_xi: {summary['any_branch_derives_negative_xi']}")
    print(
        "any_branch_passes_exact_schwarzschild_kerr: "
        f"{summary['any_branch_passes_exact_schwarzschild_kerr']}"
    )
    print()
    for branch in summary["branches"]:
        print(branch["key"])
        print(f"  label: {branch['label']}")
        print(f"  nonzero_theta: {branch['nonzero_theta']}")
        print(f"  source_equation: {branch['source_equation']}")
        print(
            "  exact_schwarzschild_kerr: "
            f"{branch['exact_schwarzschild_kerr']}"
        )
        print(f"  flrw_xi_gate: {branch['flrw_xi_gate']}")
        print(f"  decision: {branch['decision']}")
        print(f"  proof_obligation: {branch['proof_obligation']}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", help="Show one branch by key.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    summary = summarize(select(args.branch))
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print_text(summary)

    if summary["any_branch_derives_negative_xi"]:
        raise SystemExit("unexpected PASS: no current branch should derive negative xi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
