#!/usr/bin/env python3
"""K255: compose K250 source underdetermination with K254 exact local closure.

The output is a source/data gate and a general operator-theoretic
nonuniqueness certificate.  It does not construct a GU full operator.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "lab/process/k255-native-i1b-full-operator-data-gate.json"

INPUTS = {
    "k250": ROOT / "lab/process/k250-native-i1b-source-selection-and-all-direction-growth.json",
    "k254": ROOT / "lab/process/k254-native-i1b-exact-closure.json",
    "source_register": ROOT / "lab/sources/source-claim-register.yaml",
    "source_extraction": ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md",
    "bulk_source_return": ROOT / "lab/sources/selected-k77-bulk-operator-source-reinspection-2026-08-09.md",
    "fermion_source_return": ROOT / "lab/sources/selected-k77-nonzero-fermion-stationary-schur-reduction-source-return-2026-08-10.md",
    "physics_ledger_v0_263": ROOT / "lab/process/conditional-physics-ledger-v0.263.json",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def spectral_window(alpha: Fraction, mass: Fraction, radius: int = 4) -> list[str]:
    # D_{alpha,m}=-i d/dtheta+m on psi(2pi)=exp(2pi i alpha)psi(0).
    return [q(Fraction(n) + alpha + mass) for n in range(-radius, radius + 1)]


def ledger_row(ledger: dict, row_id: str) -> dict:
    return next(row for row in ledger["rows"] if row["id"] == row_id)


def main() -> None:
    k250 = json.loads(INPUTS["k250"].read_text())
    k254 = json.loads(INPUTS["k254"].read_text())
    register = yaml.safe_load(INPUTS["source_register"].read_text())
    extraction = INPUTS["source_extraction"].read_text()
    bulk_return = INPUTS["bulk_source_return"].read_text()
    fermion_return = INPUTS["fermion_source_return"].read_text()
    ledger = json.loads(INPUTS["physics_ledger_v0_263"].read_text())

    assert k250["source_selection"]["decision"] == (
        "current source corpus does not select a unique full fermion operator"
    )
    assert k254["exact_characteristic_zero_dimension"] == 1106
    assert k254["exact_rational_closure"]["stabilization_depth"] == 6

    claims = {row["id"]: row for row in register["claims"]}
    assert claims["SC-OP-04"]["polarity"] == "ASSERTS"
    assert claims["SC-OP-05"]["polarity"] == "UNCERTAIN"
    assert "begin with operators like" in claims["SC-OP-04"]["verbatim"]
    assert "non-trivial map in the lower right quadrant" in claims["SC-OP-05"]["verbatim"]

    for needle in (
        "unique or globally defined operator",
        "common variational domain",
        "closed physical evolution domain",
    ):
        assert needle in extraction
    for needle in ("closed maximal/minimal graph domains", "coupled bulk BV and boundary BFV complex"):
        assert needle in bulk_return
    for needle in ("final C-reality/Krein placement", "a common Green/BV domain"):
        assert needle in fermion_return

    gr6b = ledger_row(ledger, "LT-GR6b")
    sm8 = ledger_row(ledger, "LT-SM8")
    assert gr6b["verdict"] == "NEEDS"
    assert sm8["verdict"] == "NEEDS"

    baseline = spectral_window(Fraction(0), Fraction(0))
    lower_order = spectral_window(Fraction(0), Fraction(1, 3))
    changed_domain = spectral_window(Fraction(1, 2), Fraction(0))
    assert baseline != lower_order
    assert baseline != changed_domain

    result = {
        "schema_version": "1.0",
        "classification": "SOURCE_NATIVE_ROUTE__K250_K254_COMPOSITION_AND_GENERAL_OPERATOR_DATA_GATE",
        "input_sha256": {name: sha256(path) for name, path in INPUTS.items()},
        "object": (
            "K254's conditional selected comm/symi/symi local I1B principal family, "
            "composed with K250's authenticated source-selection result"
        ),
        "source_selection_baseline": {
            "reused_result": "K250",
            "decision": k250["source_selection"]["decision"],
            "registered_claims": [
                {"id": "SC-OP-04", "polarity": "ASSERTS", "effect": "candidate-strength four-field matrix grammar"},
                {"id": "SC-OP-05", "polarity": "UNCERTAIN", "effect": "nonzero-southeast rival admitted without selection"},
            ],
            "current_delta": "no newer registered source evidence selects one full operator or one common closed domain",
        },
        "principal_data_nonuniqueness": {
            "general_lower_order_theorem": (
                "For every first-order differential expression D and every zero-order bundle endomorphism V, "
                "sigma_1(D+V)=sigma_1(D). Therefore a selected principal symbol cannot determine the lower-order operator."
            ),
            "fixed_realization_shift_theorem": (
                "For any closed realization D on a fixed domain and scalar c, D+cI has the same principal symbol; "
                "whenever spectral translation is defined, spec(D+cI)=spec(D)+c."
            ),
            "domain_theorem": (
                "A local differential expression does not determine its closed realization; boundary or holonomy "
                "conditions can change the spectrum without changing the differential expression or principal symbol."
            ),
            "model": "D_{alpha,m}=-i d/dtheta+m on L2([0,2pi]) with psi(2pi)=exp(2pi i alpha)psi(0)",
            "common_principal_symbol": "xi",
            "witnesses": [
                {
                    "id": "baseline-periodic-zero-order-zero",
                    "alpha": "0",
                    "zero_order_m": "0",
                    "spectrum_formula": "Z",
                    "window_n_minus4_to4": baseline,
                },
                {
                    "id": "lower-order-only",
                    "alpha": "0",
                    "zero_order_m": "1/3",
                    "spectrum_formula": "Z+1/3",
                    "window_n_minus4_to4": lower_order,
                    "changed_data": "zero_order_term_only",
                },
                {
                    "id": "domain-only",
                    "alpha": "1/2",
                    "zero_order_m": "0",
                    "spectrum_formula": "Z+1/2",
                    "window_n_minus4_to4": changed_domain,
                    "changed_data": "closed_domain_only",
                },
            ],
            "application_to_k254": (
                "K254 fixes a finite local invariant hull for one principal family. Even if that family extends to a "
                "global closed operator, its principal data alone cannot select the zero-order completion or closed domain, "
                "and therefore cannot select a spectrum."
            ),
        },
        "full_operator_admission_contract": {
            "required_before_spectrum": [
                "authenticated selection of one full differential expression and southeast branch",
                "global invariant bundle and overlap/descent data",
                "all lower-order coefficients on a frozen background",
                "reality structure, density/pairing and operative adjoint",
                "global base/topology and boundary or asymptotic geometry",
                "one common closed domain with trace/Green compatibility",
            ],
            "additional_before_physical_mode": [
                "action-owned gauge/BRST/BV quotient and constraints",
                "physical state space and positive or otherwise interpreted pairing",
                "observable map connecting the operator mode to the claimed physics",
            ],
            "current_status": "DEPENDENCY_OPEN__NO_SPECTRAL_OR_PHYSICAL_INFERENCE_ADMITTED",
            "exact_wake": (
                "authenticated source evidence or an explicitly conditional repository construction supplies all six "
                "full-operator fields on one frozen branch and a native check proves a common closed realization; physical "
                "mode claims additionally require the quotient, state-space pairing and observable map"
            ),
        },
        "source_routing": (
            "SC-OP-04 ASSERTS and SC-OP-05 UNCERTAIN remain unchanged; SC-ACT-01/02 ASSERTS, "
            "SC-META-53 UNCERTAIN, and LT-GR6b/LT-SM8 NEEDS do not move."
        ),
        "interpretation": (
            "K250 already closed unique source selection negatively and K254 closed the finite local hull positively. "
            "K255 composes those results into a decisive data-sufficiency theorem: principal closure is not full-operator "
            "closure, and two independent missing data classes can change spectrum while principal data stays fixed."
        ),
        "claim_ceiling": (
            "Authenticated source-data composition, general principal-data nonuniqueness, exact scalar-circle witnesses, "
            "and a minimum future admission contract only. No claim that GU lacks a valid completion; no constructed GU "
            "full operator, spectrum, quotient, positivity, physical mode, source/ledger/canon/public change, or K218 theorem."
        ),
    }

    OUT.write_text(json.dumps(result, indent=2, sort_keys=False) + "\n")
    print("K255 full-operator data gate: PASS")
    print(f"record={OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
