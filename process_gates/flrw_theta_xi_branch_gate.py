"""Audit the FLRW theta-xi branch reduction.

This is not a physics simulation. It checks that the branch-reduction note keeps
the coefficient logic synchronized with the source files:

* the DESI-sign threshold is the negative non-minimal value from the mechanism note;
* the minimal action baseline does not include a bare R theta^2 term;
* every viable branch with missing action data reports xi_eff as undefined;
* the free-beta branch reports an absent theta scalar rather than a negative xi.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "explorations" / "flrw-theta-xi-branch-reduction-2026-06-24.md"
MINIMAL_ACTION = ROOT / "explorations" / "gu-minimal-action-spec-2026-06-24.md"
CLOSED_LOOP = ROOT / "explorations" / "gu-closed-loop-action-ig-branch-2026-06-24.md"
MECHANISM = ROOT / "explorations" / "dark-energy-w-window-mechanism-2026-06-23.md"
DAG = ROOT / "explorations" / "live-claim-dag-fault-finality-ledger-2026-06-24.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_summary(note_text: str) -> dict[str, Any]:
    match = re.search(
        r"## Machine-Auditable Summary.*?```json\s*(\{.*?\})\s*```",
        note_text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Auditable Summary JSON block")
    return json.loads(match.group(1))


def assert_source_consistency() -> None:
    minimal = read(MINIMAL_ACTION)
    closed = read(CLOSED_LOOP)
    mechanism = read(MECHANISM)
    dag = read(DAG)

    required_minimal = [
        "S_Rtheta,bare = 0",
        "xi_eff = C_Rtheta / Z_theta",
        "delta_beta S_theta alone forces theta = 0",
    ]
    for needle in required_minimal:
        if needle not in minimal:
            raise AssertionError(f"minimal action source missing {needle!r}")

    required_closed = [
        "No branch currently derives",
        "xi_eff < -0.319",
        "Without a fixed `S_IG-dyn`, `xi_eff` is an adjustable model parameter",
        "theta = 0,",
    ]
    for needle in required_closed:
        if needle not in closed:
            raise AssertionError(f"closed-loop source missing {needle!r}")

    mechanism_needles = [
        "xi < xi_c1 = -0.319",
        "xi ~ -0.6",
        "supply the sign or magnitude of any `xi R theta^2` term",
    ]
    for needle in mechanism_needles:
        if needle not in mechanism:
            raise AssertionError(f"mechanism source missing {needle!r}")

    dag_needles = [
        "canonical normalization `B = sqrt(Z_theta) b_raw`",
        "`xi_eff < -0.319`, preferably near `-0.6`",
        "the needed negative coupling depends on unspecified `S_IG-dyn`",
    ]
    for needle in dag_needles:
        if needle not in dag:
            raise AssertionError(f"DAG source missing {needle!r}")


def assert_summary(summary: dict[str, Any]) -> None:
    window = summary["xi_window"]
    assert window["negative_wa_threshold"] == -0.319
    assert window["desi_ratio_match"] == -0.6
    assert window["formula"] == "xi_eff = C_Rtheta / Z_theta"

    baseline = summary["baseline"]
    assert baseline["bare_Rtheta_present"] is False
    assert baseline["bare_lambda_present"] is False
    assert baseline["bare_free_beta_forces_theta_zero"] is True

    branches = {branch["key"]: branch for branch in summary["branches"]}
    expected = {
        "background_stueckelberg",
        "constrained_ig_a_independent",
        "constrained_ig_a_dependent",
        "dynamical_ig_total_current",
        "bare_free_beta_norm",
    }
    if set(branches) != expected:
        raise AssertionError(f"unexpected branch keys: {sorted(branches)}")

    generated = [
        branch["key"]
        for branch in branches.values()
        if branch["negative_xi"] == "generated"
    ]
    if generated:
        raise AssertionError(f"no current branch should generate negative xi: {generated}")

    for key, branch in branches.items():
        if key == "bare_free_beta_norm":
            assert branch["viable"] is False
            assert branch["scalar_mode"] == "absent_theta_equals_zero"
            assert branch["negative_xi"] == "absent"
            assert branch["xi_eff"] == "undefined"
            continue

        assert branch["viable"] is True
        assert branch["verdict"] == "branch-undefined"
        assert branch["Z_theta"] == "undefined"
        assert branch["C_Rtheta"] == "undefined"
        assert branch["xi_eff"] == "undefined"
        assert branch["negative_xi"] == "not_generated"


def audit() -> dict[str, Any]:
    note_text = read(NOTE)
    summary = extract_summary(note_text)
    assert_source_consistency()
    assert_summary(summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print audited summary JSON.")
    args = parser.parse_args()

    summary = audit()
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print("FLRW theta-xi branch gate: PASS")
        print("generated_negative_xi: False")
        print("viable_branch_coefficients: undefined")
        print("bare_free_beta_theta_mode: absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
