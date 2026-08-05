#!/usr/bin/env python3
"""Executable contract checks for GU functional-channel dispatch and freshness."""

from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


contract = strict(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
ledger = strict(ROOT / contract["standing_ledger"]["ref"])
rows = {row["id"]: row for row in ledger["rows"]}


def dispatch(*, uncertain=False, adverse=False, buildable=False,
             material_builds=0, immediate=False, verification_risk=False):
    if uncertain:
        return "SOURCE_OR_COMPOSE"
    if adverse:
        return "INDEPENDENT_ADJUDICATION"
    if buildable:
        return "BUILD"
    if material_builds >= contract["channels"]["COMPOSE"]["cadence"]["after_material_build_outputs"] or immediate:
        return "COMPOSE"
    if verification_risk:
        return "VERIFY"
    return "NO_MAKE_WORK"


def wave_admitted(channel, *, rows_declared=False, meter=False, changed=False,
                  no_change_reason=False, source_return=None,
                  replay_changed=False, replay_risk=None,
                  finder_is_adjudicator=False):
    if channel in {"BUILD", "COMPOSE"}:
        if not rows_declared or not meter or not (changed or no_change_reason):
            return False
    if channel == "SOURCE":
        if source_return not in contract["channels"]["SOURCE"]["return_codes"]:
            return False
    if channel == "VERIFY" and not replay_changed:
        if replay_risk not in contract["channels"]["VERIFY"]["replay_admission"]:
            return False
    if finder_is_adjudicator:
        return False
    return True


print("A. CHANNEL AND LANE SEPARATION")
check("exact", "contract is ratified", contract["status"] == "RATIFIED")
check("exact", "purpose lanes remain exactly 1/2/3/A",
      contract["purpose_lanes_preserved"] == ["1", "2", "3", "A"])
check("type", "functional channels are not lanes", contract["functional_channels_are_not_lanes"])
check("exact", "the four functions are complete and distinct",
      set(contract["channels"]) == {"BUILD", "COMPOSE", "SOURCE", "VERIFY"})
check("exact", "dispatch has no fixed percentages", contract["dispatch"]["fixed_percentages"] is False)
check("type", "thin triggers load owner refs rather than duplicate science",
      "DO_NOT_DUPLICATE" in contract["thin_trigger_rule"])
check("type", "owner-local durability does not overclaim fleet runner integration",
      contract["durability_level"] == "OWNER_LOCAL_MANDATORY_CONTEXT_PLUS_MACHINE_TESTED_CONTRACT"
      and contract["fleet_runner_interpretation_change"] == "NOT_CHANGED_IN_THIS_RUN")
check("type", "Compose owns the ledger with Lane A reconciliation",
      contract["standing_ledger"]["owner"] == "COMPOSE_CHANNEL_WITH_LANE_A_RECONCILIATION")

print("\nB. CONDITION-BASED DISPATCH")
check("exact", "semantic uncertainty routes to Source/Compose",
      dispatch(uncertain=True, buildable=True) == "SOURCE_OR_COMPOSE")
check("exact", "high-fanout adverse row routes to independent adjudication",
      dispatch(adverse=True, buildable=True) == "INDEPENDENT_ADJUDICATION")
check("exact", "current typed constructible distance routes to Build",
      dispatch(buildable=True) == "BUILD")
check("exact", "three material builds trigger Compose",
      dispatch(material_builds=3) == "COMPOSE")
check("exact", "high-fanout premise change triggers Compose immediately",
      dispatch(immediate=True) == "COMPOSE")
check("exact", "named integrity risk admits Verify",
      dispatch(verification_risk=True) == "VERIFY")
check("planted", "PLANT empty capacity does not manufacture Verify work",
      dispatch() == "NO_MAKE_WORK")

print("\nC. WAVE ADMISSION AND INFORMATION PRESERVATION")
check("exact", "Build with rows, meter and change is admitted",
      wave_admitted("BUILD", rows_declared=True, meter=True, changed=True))
check("exact", "Compose with explicit evidence-backed no-change reason is admitted",
      wave_admitted("COMPOSE", rows_declared=True, meter=True, no_change_reason=True))
check("planted", "PLANT Build without declared rows is rejected",
      not wave_admitted("BUILD", meter=True, changed=True))
check("planted", "PLANT Compose without meter is rejected",
      not wave_admitted("COMPOSE", rows_declared=True, changed=True))
check("planted", "PLANT row-touching no-op without a reason is rejected",
      not wave_admitted("BUILD", rows_declared=True, meter=True))
check("source", "all three typed Source returns are admitted",
      all(wave_admitted("SOURCE", source_return=code)
          for code in ["SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"]))
check("planted", "PLANT generic source success is rejected",
      not wave_admitted("SOURCE", source_return="SUCCESS"))
check("planted", "PLANT unchanged replay without named risk is rejected",
      not wave_admitted("VERIFY", replay_changed=False))
check("exact", "unchanged replay with a declared dependency change is admitted",
      wave_admitted("VERIFY", replay_changed=False, replay_risk="dependency_changed"))
check("planted", "PLANT adverse-row finder cannot self-adjudicate",
      not wave_admitted("COMPOSE", rows_declared=True, meter=True, changed=True,
                        finder_is_adjudicator=True))
check("type", "unknown kind remains a new-kind event",
      contract["standing_ledger"]["unknown_kind_rule"] == "NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN")
check("exact", "every current row retains all required information fields",
      all(set(contract["standing_ledger"]["row_required_fields"]) <= set(row)
          for row in ledger["rows"]))

print("\nD. DYNAMIC COSMOLOGICAL SECTOR")
directive = next(d for d in contract["active_scientific_directives"]
                 if d["id"] == "GU-COSMO-DYNAMIC-01")
required = directive["required_layer0_objects"]
check("exact", "the original Layer-0 split hold is released into typed successor rows",
      directive["primary_row_on_hold"] is None
      and directive["release_condition_met"] is True
      and "PHYSICAL_COHOMOLOGY_AND_TWO_FIELD_COSMOLOGY_OPEN" in directive["status"])
check("type", "Source plus Compose own the split independently from Build",
      directive["owner"] == "SOURCE_PLUS_COMPOSE__INDEPENDENT_FROM_NEXT_BUILD_FINDER")
check("type", "historical and active directive rows exist in the current ledger",
      set(directive["historically_held_rows"] + directive["active_rows"]) <= set(rows))
check("exact", "seven cosmological Layer-0 objects are separately named",
      len(required) == len(set(required)) == 7)
check("type", "Einstein tensor and action-derived stress-energy are separate",
      "OBSERVED_EINSTEIN_TENSOR" in required
      and "ACTION_DERIVED_MATTER_STRESS_ENERGY" in required)
check("type", "constant Lambda and variable olive/varpi VEV are separate",
      "LITERAL_CONSTANT_LAMBDA_G" in required
      and "VARIABLE_OLIVE_VARPI_AUGMENTED_TORSION_VEV" in required)
check("type", "curvature co-variation, VEV scale and w(z) remain separate burdens",
      {"EINSTEIN_CURVATURE_COVARIATION", "VEV_SIGN_MAGNITUDE_NORMALIZATION",
       "EFFECTIVE_W_OF_Z_OBSERVABLE"} <= set(required))
check("planted", "PLANT Einstein recovery cannot discharge cosmology",
      directive["forbidden_collapse"] ==
      "EINSTEIN_RECOVERY_DOES_NOT_IMPLY_DYNAMIC_COSMOLOGICAL_SECTOR_RECOVERY")
check("type", "evidence boundary keeps exact movement and open ownership together",
      "GAUSS_TRACE_AND_TRACELESS_HESSIANS_100_OVER117_AND_124_OVER117"
      in directive["current_evidence_boundary"]
      and "COUPLED_OBSERVED_DEFECT_KREIN_GREEN_DOMAIN"
      in directive["current_evidence_boundary"]
      and "FULL_METRIC_COFRAME_SOLDERING_BV_PHYSICAL_COHOMOLOGY_AND_TWO_FIELD_CURVATURE_VEV_COSMOLOGY_OPEN"
      in directive["current_evidence_boundary"])
check("source", "current composed-locus source disposition is typed",
      directive["source_return"] == "SOURCE-CORRECTS")
check("type", "next gate preserves both physical-cohomology and two-field cosmology branches",
      "BV_PHYSICAL_COHOMOLOGY" in directive["next_gate"]
      and "TWO_FIELD_CURVATURE_VEV_FLRW" in directive["next_gate"])

toe = (ROOT / "lab/sources/claim-mining-toe-weinstein-2026-07-20.md").read_text(encoding="utf-8")
pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text(encoding="utf-8")
check("source", "TOE ledger records variable rather than constant cosmological term",
      "there isn't a cosmological constant, it's variable" in toe)
check("source", "TOE ledger records co-variation with Einstein curvature",
      "go up and down with [Einstein curvature]" in toe)
check("source", "primary-source pack records the VEV/fundamental-mass link",
      "cosmological constant is the VEV" in pack)
check("planted", "PLANT directive cannot be released without source plus append-only decision",
      "PRIMARY_SOURCE_REINSPECTION" in directive["release_condition"]
      and "APPEND_ONLY_LEDGER_SPLIT" in directive["release_condition"])

print("\nE. NON-EFFECTS AND REVIEW")
check("exact", "two hostile charges remain mandatory",
      contract["channels"]["VERIFY"]["hostile_charges"] ==
      ["SUMMARY_OUTRUNS_ARTIFACT", "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT"])
check("exact", "reset changes no scheduler, trigger, grants, lane count or scientific posture",
      set(contract["non_effects"]) >= {
          "NO_SCHEDULER_CHANGE", "NO_TRIGGER_CHANGE", "NO_ACTIVATION_GRANT_CHANGE",
          "NO_LANE_COUNT_CHANGE", "NO_CANON_CHANGE",
          "NO_EXTERNAL_P1_P2_P3_CHANGE", "NO_PUBLIC_POSTURE_CHANGE"
      })

print("\nCOUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
