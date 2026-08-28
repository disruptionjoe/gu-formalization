#!/usr/bin/env python3
"""Guard M-M26's primary citation and evidence-bounded modular scope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULT = ROOT / "explorations/rankN-krein-tt-for-gu-2026-07-11.md"
COUNCIL = ROOT / "explorations/council-inherited-tension-resolution-2026-07-21.md"
REGISTER = ROOT / "lab/process/improvement-register-2026-08-03.md"


def valid(result: str, council: str, register: str) -> bool:
    required_result = (
        "Victor S. Shulman's",
        "10.1142/S0129055X97000270",
        "weakly closed",
        "pre-existing Pi1",
        "cyclic and separating vector",
        "does not construct the indefinite form",
        "or prove that no higher-rank result exists",
    )
    required_register = (
        "| M-M26 | **EXECUTED",
        "higher-rank/infinite-index construction needed by GU remains unestablished here",
        "absence from the Pi1 paper is not a literature no-go",
    )
    forbidden = (
        "Jakóbczyk's analogue",
        "no Pi_kappa (kappa>=2) conjugation theorem exists",
        "non-existent infinite-rank Krein",
    )
    return (
        all(token in result for token in required_result)
        and "Shulman's cited theorem closes the specified Pi1 slice only" in council
        and all(token in register for token in required_register)
        and not any(token in result + council + register for token in forbidden)
    )


def main() -> int:
    result = RESULT.read_text(encoding="utf-8")
    council = COUNCIL.read_text(encoding="utf-8")
    register = REGISTER.read_text(encoding="utf-8")
    assert valid(result, council, register)

    mutants = (
        result.replace("Victor S. Shulman's", "Jakobczyk's", 1),
        result.replace("weakly closed", "arbitrary"),
        result.replace("pre-existing Pi1", "general Krein"),
        result.replace(
            "or prove that no higher-rank result exists",
            "and proves that no higher-rank result exists",
            1,
        ),
    )
    caught = sum(not valid(mutant, council, register) for mutant in mutants)
    assert caught == 4

    print("PASS: Shulman Pi1 metadata and hypotheses are explicit")
    print("PASS: installed J/indefinite structure and GU infinite-index gaps remain explicit")
    print("PASS: higher-rank literature nonexistence is not inferred")
    print(f"PASS: {caught}/4 planted attribution, hypothesis and ceiling mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
