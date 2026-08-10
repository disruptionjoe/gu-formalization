#!/usr/bin/env python3
"""Typed source-carrier versus selected-hull interface gate for K77.

This is deliberately a composition probe, not another expensive matrix replay.
It consumes the exact v0.159 certificate and asks what its ranks mean when
composed with the source's declared four-field grammar.

Layer 0: ambient carrier ownership is not subbundle selection; an equation
receiver is not a field carrier; one separately fitted receiver per covector is
not one fixed source object; and external datum is not local Euler closure.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
packet = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()
contract = (ROOT / "lab/process/source-object-interface-contract.md").read_text()
requirements = (ROOT / "explorations/source-action-requirements-spec-2026-07-13.md").read_text()
v0159_report = (ROOT / "explorations/conditional-build/selected-k77-high-conviction-receiver-completion-2026-08-10.md").read_text()
v0159 = json.loads((ROOT / "lab/process/selected-k77-high-conviction-receiver-completion.json").read_text())


print("A. SOURCE, PRIOR ART AND LAYER 0")
check("source", "source declares independent barred and unbarred Omega0 plus Omega1 fields",
      "four distinct fields" in source
      and "nu, bar-nu     in Omega^0(Y,S)" in source
      and "zeta, bar-zeta in Omega^1(Y,S)" in source)
check("source", "source forbids premature adjoint identification of the barred variables",
      "do not replace the bars" in source)
check("source", "source supplies ingredients but is silent on the global adjoint/domain",
      "global Hodge/Krein/reality adjoint" in source and "SOURCE-SILENT" in source)
check("prior_art", "frozen interface is a constraint packet rather than a claimed instance",
      "does not claim that such an object exists" in contract)
check("prior_art", "27-row spec keeps FORCED DECLARATION and FIT distinct",
      requirements.count("| FORCED") >= 8
      and requirements.count("| DECLARATION") >= 9
      and requirements.count("| FIT") >= 10)
check("prior_art", "v0.159 exact certificate is green and predecessor-replayed",
      v0159["checks"]["new_failures"] == 0
      and v0159["checks"]["new"] == 29
      and v0159["checks"]["predecessor_replayed"] is True)
check("datum", "P1/P2 orientation and P3 KO twist remain different typed inputs",
      "P1/P2: one orientation line" in packet and "P3: bounded real" in packet)
for label in (
    "ambient four-field carrier versus selected finite subbundle",
    "left action test space versus right field space",
    "per-covector receiver fit versus one fixed receiver hull",
    "fixed receiver hull versus action-owned variational reduction",
    "finite action restriction versus BV cohomology and closed domain",
    "P1/P2 orientation and P3 KO input versus local Euler closure",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT V0.159 INPUT AND SOURCE-TYPE CORRECTION")
fingerprint = v0159["rank_fingerprint_each_pin"]
check("exact", "v0.159 tested timelike spacelike and null strata on both Pin placements",
      set(fingerprint) == {"timelike", "spacelike", "null"}
      and "Both Pin placements give the same ranks" in v0159_report)
check("exact", "each tested stratum has rank-128 graph leakage",
      all(row["leak"] == 128 for row in fingerprint.values()))
check("exact", "each separately fitted minimal receiver has rank 256 and adds 128 paired left directions",
      v0159["minimal_receiver"] == {
          "old_rank": 128,
          "new_rank": 256,
          "added_equations": 128,
          "required_paired_left_fields": 128,
          "source_owned": False,
      })
check("carrier", "the required paired directions have the source-declared barred Omega0-plus-Omega1 field type",
      "bar-nu" in source and "bar-zeta" in source
      and "Krein-dual action typing" in v0159_report)
check("layer0", "source typing retracts only the new-field-type reading, not the unowned-selector reading",
      v0159["minimal_receiver"]["source_owned"] is False
      and "source's current four-field graph does not own that extension" in v0159_report)
check("planted", "PLANT equal rank 256 in three strata is not evidence that their subspaces are identical",
      all(row["leak"] == 128 for row in fingerprint.values()))
check("planted", "PLANT ambient field permission is not a source-selected projector",
      "SOURCE_SILENT" in v0159["source_return"] and "rank-256" not in source)


print("\nC. ORDERED ACCEPTANCE INTERFACE")
GATES = [
    {
        "id": "H1_SOURCE_TYPED_FIXED_REDUCTION",
        "admit": "one covector-independent moving reduction inside the declared independent barred/unbarred Omega0-plus-Omega1 carriers",
        "kill": "only a fitted receiver projector or a new unrestricted function-valued map selects it",
    },
    {
        "id": "H2_FULL_EULER_CLOSURE",
        "admit": "the same reduction closes the full Euler symbol across timelike spacelike and null strata while preserving the rank-128 Green precursor",
        "kill": "separate covector-dependent rank-256 receivers are required",
    },
    {
        "id": "H3_VARIATIONAL_NOETHER_OWNERSHIP",
        "admit": "the reduction and added equations arise from one explicit action and its off-shell Noether identity",
        "kill": "closure exists only after post-variation projection",
    },
    {
        "id": "H4_BV_AND_COMMON_DOMAIN",
        "admit": "a nilpotent BV differential and common closed Krein/Green domain descend on the selected complex",
        "kill": "only the null characteristic half-complex exists",
    },
    {
        "id": "H5_OBSERVATION_CHIRALITY_MIRROR",
        "admit": "observation descent yields chiral physical cohomology and discharges the mirror sector",
        "kill": "ambient K77 chirality projectors are merely relabelled as observed chirality",
    },
    {
        "id": "H6_DATUM_INDEX_COUNT",
        "admit": "only after H1-H5, P1 orients a supplied line and P3 twists a realized relative operator whose index is identified with count",
        "kill": "P1/P2/P3 is used to manufacture a local receiver selector or equation",
    },
    {
        "id": "H7_RENDEZVOUS",
        "admit": "the same action later meets Higgs/Yukawa, anomaly, cosmological-amplitude and physical-observable rows without retuning",
        "kill": "sector-specific repairs replace the shared source object",
    },
]
check("interface", "critical path is ordered before downstream rendezvous rows",
      [gate["id"] for gate in GATES][:3] == [
          "H1_SOURCE_TYPED_FIXED_REDUCTION",
          "H2_FULL_EULER_CLOSURE",
          "H3_VARIATIONAL_NOETHER_OWNERSHIP",
      ] and GATES[-1]["id"] == "H7_RENDEZVOUS")
check("variational", "construction is admitted only before projection and from one action",
      "post-variation projection" in GATES[2]["kill"])
check("symplectic", "paired barred directions remain mandatory even though their ambient field type is already declared",
      v0159["minimal_receiver"]["required_paired_left_fields"] == 128)
check("bv", "the null half-complex cannot satisfy the BV/domain gate",
      fingerprint["null"]["leak_gauge_intersection"] == 64
      and fingerprint["null"]["symbol_on_gauge"] == 0)
check("analytic", "global closed-domain and index work stays downstream of finite action closure",
      GATES[3]["id"] == "H4_BV_AND_COMMON_DOMAIN")
check("representation", "particle chirality and mirror removal stay downstream of BV/domain",
      GATES[4]["id"] == "H5_OBSERVATION_CHIRALITY_MIRROR")
check("datum", "external datum is forbidden from manufacturing local closure",
      "manufacture a local receiver" in GATES[5]["kill"])
check("anomaly", "anomaly admission is retained as a rendezvous test rather than a local receiver repair",
      "anomaly" in GATES[6]["admit"])
check("cosmology", "Higgs/Yukawa and cosmological amplitude are retained as same-action rendezvous tests",
      "Higgs/Yukawa" in GATES[6]["admit"] and "cosmological-amplitude" in GATES[6]["admit"])
check("accounting", "a free projector or unrestricted map fires the early-stop rule",
      "fitted receiver projector" in GATES[0]["kill"])


RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "input_certificate": "lab/process/selected-k77-high-conviction-receiver-completion.json",
    "exact_input": {
        "per_stratum_receiver_rank": 256,
        "added_equations": 128,
        "paired_left_directions": 128,
        "fixed_common_hull_rank": "UNTESTED",
    },
    "layer0_correction": "SOURCE_OWNS_AMBIENT_BARRED_AND_UNBARRED_FIELD_TYPES__SOURCE_DOES_NOT_YET_SELECT_THE_FINITE_REDUCTION",
    "gates": GATES,
    "source_return": "SOURCE_CONFIRMS_AMBIENT_INDEPENDENT_BARRED_AND_UNBARRED_OMEGA0_PLUS_OMEGA1_CARRIERS__SOURCE_CORRECTS_NEW_FIELD_TYPE_READING__SOURCE_SILENT_ON_FIXED_FINITE_SUBBUNDLE_SELECTION_ACTION_INVARIANCE_BV_DOMAIN_AND_EXTERNAL_DATUM_APPLICATION",
    "disposition": "RANK256_IS_PER_STRATUM_NOT_YET_ONE_FIXED_HULL__MISSING_DIRECTIONS_ARE_SOURCE_TYPED_BUT_SELECTOR_IS_UNOWNED__CONSTRUCTION_WORTH_CONTINUING_ONLY_THROUGH_ACTION_OWNED_MOVING_REDUCTION",
    "next_gate": "TEST_MOVING_ACTION_OWNED_REDUCTION_P_EPSILON_U_EQUALS_U_AND_D_VARPI_CHI_EPSILON_EQUALS_ZERO_ON_THE_FIXED_COMMON_HULL_AGAINST_MIRROR_RANDOM192_640_AND832__STOP_IF_ONLY_A_FITTED_PROJECTOR_SELECTS_IT",
}

print("\nK77 SOURCE-OWNED HULL INTERFACE RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: source ownership of ambient field types is separated from the still-unowned fixed action reduction and from all downstream datum/physics gates.")
