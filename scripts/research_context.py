#!/usr/bin/env python3
"""Read-only projections of existing research owners; never a work selector."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
MATRIX = "lab/process/action-constraint-matrix.json"
BETS = "lab/process/discovery-bets.json"
SOURCES = "lab/sources/source-claim-register.yaml"
NOTICE = (
    "PARTIAL READ-ONLY VIEW — local file facts, not a work selector or freshness certificate. "
    "This view does not select work, certify scientific claims, or replace program_focus, "
    "source-routing rules and exact evidence. Omitted history is not retired; use --history. "
    "Packet readiness is declared status, not proof of scientific applicability."
)
CLAIM_ID = re.compile(r"\bSC-[A-Z]+-\d+\b")
FILE_REF = re.compile(
    r"(?:lab|explorations|canon|papers|tests|Lean|process_gates|docs)/"
    r"[^\s<>\[\]{}\"']+?\.(?:md|json|yaml|lean|py)"
    r"(?:#[\w./:-]+|:\d+(?:-\d+)?)?"
)


def first_verification_section(text):
    """Legacy importable helper: retain a complete first level-two section."""
    section, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence is not None:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker:
            fence = marker[1]
        elif re.match(r"^ {0,3}#{1,2}\s+", line):
            if section:
                break
            if not re.match(r"^ {0,3}##\s+", line):
                continue
            section.append(line)
            continue
        if section:
            section.append(line)
    if not section or fence is not None:
        raise ValueError("VERIFICATION.md lacks a complete first level-two section")
    return "\n".join(section).rstrip()


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def references(value):
    return sorted({match.group(0) for text in strings(value) for match in FILE_REF.finditer(text)})


def recorded_fields(value, names, prefix=""):
    """Expose declared burdens/corrections with their original field path; do not infer them."""
    found = {}
    if isinstance(value, dict):
        for key, item in value.items():
            path = f"{prefix}.{key}" if prefix else key
            if any(name in str(key).lower() for name in names):
                found[path] = item
            else:
                found.update(recorded_fields(item, names, path))
    return found


def packet_projection(text, path):
    """Read the two existing packet encodings: fenced YAML or Step/Status table."""
    meta, steps, declared, packet_data = {}, [], None, {}
    if text.startswith("---\n"):
        parts = text.split("\n---", 1)
        if len(parts) == 2:
            meta = yaml.safe_load(parts[0][4:]) or {}
    for block in re.findall(r"(?ms)^```ya?ml\s*\n(.*?)^```\s*$", text):
        data = yaml.safe_load(block)
        if isinstance(data, dict) and isinstance(data.get("steps"), list):
            steps = data["steps"]
            packet_data = data
            declared = data.get("packet_status")
            break
    if not steps:
        columns = None
        for line in text.splitlines():
            if not line.lstrip().startswith("|"):
                columns = None
                continue
            cells = [x.strip() for x in line.strip().strip("|").split("|")]
            lowered = [x.lower() for x in cells]
            if "step" in lowered and "status" in lowered:
                columns = lowered
            elif columns and len(cells) == len(columns) and not all(re.fullmatch(r":?-+:?", x) for x in cells):
                row = dict(zip(columns, cells))
                steps.append({"id": row["step"], "status": row["status"], "detail": row})
    steps = [s for s in steps if isinstance(s, dict) and "status" in s]
    counts = {}
    for step in steps:
        status = str(step["status"])
        counts[status] = counts.get(status, 0) + 1
    result = {"path": path, "declared_status": declared or meta.get("operational_state"),
              "step_counts": counts, "ready_steps": [s.get("id") for s in steps if s["status"] == "ready"]}
    if not steps:
        result["readiness_note"] = "No supported step table found; no readiness inferred."
    result["blocked_steps"] = [s.get("id") for s in steps if s["status"] == "blocked"]
    if steps and all(s["status"] == "done" for s in steps):
        result["step_summary"] = "all listed steps done"
    result["declared_missing_inputs"] = recorded_fields(
        {k: v for k, v in packet_data.items() if k != "steps"},
        ("blocked_on", "missing", "reopen_condition"),
    )
    result["blocked_step_dependencies"] = recorded_fields(
        {str(s.get("id")): s for s in steps if s["status"] == "blocked"},
        ("blocked_on", "missing", "depends_on", "reason"),
    )
    return result


def target_records(matrix, bets):
    records = {f"{x['row']}x{x['column']}": x for x in matrix.get("cells", [])}
    records.update({x["id"]: x for x in matrix.get("intersections", [])})
    records.update({x["id"]: x for x in bets.get("bets", [])})
    records.update({x["id"]: x for x in bets.get("closed_bets", []) if isinstance(x, dict) and "id" in x})
    return records


def source_card(record, include_quote=False):
    keys = ("id", "polarity", "claim", "locus", "grade", "notes")
    card = {k: record[k] for k in keys if k in record}
    if include_quote and "verbatim" in record:
        card["verbatim"] = record["verbatim"]
    adherence = record.get("adherence", {})
    if isinstance(adherence, dict):
        card["adherence_record"] = {k: adherence[k] for k in ("adherence", "pinned_at", "date", "note") if k in adherence}
    card["recorded_corrections_and_reconciliations"] = recorded_fields(record, ("correction", "reconciliation"))
    card["linked_evidence_and_custody"] = references(record)
    card["ceiling"] = "Source polarity/adherence is not physical verification; dated records are not automatically current verdicts."
    return card


def query_projection(target, claim, matrix, bets, register, packets):
    records = target_records(matrix, bets)
    claims = {x["id"]: x for x in register.get("claims", [])}
    assumptions = matrix.get("source_relevance_assumption_view", {}).get("entries", [])
    if claim:
        if claim not in claims:
            raise ValueError(f"unknown source claim {claim}; use an exact SC-ID from {SOURCES}")
        related = [a for a in assumptions if claim in set(CLAIM_ID.findall(json.dumps(a)))]
        return {"source_claim": source_card(claims[claim], include_quote=True),
                "linked_assumption_view_entries": related,
                "targets_with_explicit_claim_reference": [key for key, value in records.items() if claim in set(CLAIM_ID.findall(json.dumps(value)))],
                "coverage": "Explicit recorded references only; absence is not absence of a semantic dependency."}
    if target not in records:
        raise ValueError(f"unknown target {target}; expected a cell such as P3xglobal_index, an intersection or a bet ID")
    record = records[target]
    refs = set(references(record))
    ids = set(CLAIM_ID.findall(json.dumps(record)))
    related = [a for a in assumptions if refs.intersection(references(a)) or ids.intersection(CLAIM_ID.findall(json.dumps(a)))]
    ids.update(CLAIM_ID.findall(json.dumps(related)))
    fields = ("status", "question", "requirement", "grade", "actual_delta", "known", "routing_note", "kill_criterion")
    selected = {k: record[k] for k in fields if k in record}
    result = record.get("result", {})
    return {"target": target, "recorded_target_fields": selected,
            "recorded_result": result if target.startswith("BET-") else None,
            "continuation_note_not_selection": record.get("next_run"),
            "packet_records": [packets[p] for p in (record.get("packet"), record.get("alongside_packet")) if p in packets],
            "declared_missing_inputs": recorded_fields(record, ("blocked_on", "missing_inputs", "missing_input", "remaining_burdens", "blocker")),
            "linked_evidence_and_corrections": sorted(refs),
            "linked_assumption_view_entries": related,
            "source_claims": [source_card(claims[c]) for c in sorted(ids) if c in claims],
            "unresolved_claim_references": sorted(ids - claims.keys()),
            "coverage": "Existing record and explicit links, including dated evidence; no inferred newest result or whole-source validation."}


def render_context(state, verification, *, matrix=None, bets=None, register=None, packets=None,
                   target=None, claim=None, history=False, revision=None):
    """Importable renderer; two-argument use reports missing live inputs explicitly."""
    if not isinstance(state, dict):
        raise ValueError("CURRENT-STATE.yaml must be a mapping")
    for field in ("purpose", "current_question", "next_condition"):
        if not isinstance(state.get(field), str) or not state[field].strip():
            raise ValueError(f"CURRENT-STATE.yaml needs nonempty {field}")
    if not isinstance(state.get("current_result"), dict):
        raise ValueError("CURRENT-STATE.yaml needs a current_result mapping")
    if target and claim:
        raise ValueError("choose --target or --claim, not both")
    matrix, bets, register, packets = matrix or {}, bets or {}, register or {}, packets or {}
    focus = state.get("program_focus") or {}
    count = matrix.get("program_run_counter", {}).get("count")
    current = {"counter": count, "counter_ref": MATRIX + "#program_run_counter",
               "ordinary_LC_arithmetic_condition": count % 4 == 3 if isinstance(count, int) and not isinstance(count, bool) else None,
               "condition_scope": "Existing rule2 arithmetic only; Tier1 completion, direct authority and full selection still govern.",
               "carry_records": {k: {field: v[field] for field in ("status", "due_counter", "consumed_bet", "counter_after") if field in v} for k, v in matrix.items() if "carry" in k.lower() and isinstance(v, dict)},
               "active_bets": [{"id": b["id"], "runs_used": b.get("runs_used"), "remaining_runs": b.get("result", {}).get("remaining_runs")} for b in bets.get("bets", []) if b.get("status") == "active"],
               "priority_packets": [{k: v for k, v in packets[path].items() if k not in ("declared_missing_inputs", "blocked_step_dependencies")} for path in focus.get("priority_packets", []) if path in packets]}
    assumption_view = matrix.get("source_relevance_assumption_view", {})
    current["consumed_directions"] = [
        {k: d[k] for k in ("id", "status", "evidence") if k in d}
        for d in matrix.get("priority_direction_history", {}).get("directions", [])
        if d.get("status") == "consumed"
    ]
    current["class_C_representativeness"] = [
        a for a in assumption_view.get("entries", [])
        if "lab/process/action-class.json" in a.get("evidence", [])
    ]
    current["shared_prerequisites"] = assumption_view.get("shared_prerequisites", [])
    current["follow_through"] = matrix.get("priority_follow_through_2026_11_25", {})
    entry = {
        "snapshot": {"checked_out_revision": revision or "not supplied", "state_revision_basis": state.get("revision_basis"),
                     "scope": "Local files; this helper does not fetch or certify synchronization."},
        "live_facts": current,
        "program_focus": state.get("program_focus"),
        "purpose": state["purpose"],
        "method_boundary": {k: state.get("research_method_control", {}).get(k) for k in ("reverse_search", "forward_certification", "work_posture")} if isinstance(state.get("research_method_control"), dict) else state.get("research_method_control"),
        "what_needs_joe": state.get("what_needs_joe"),
        "expanded_reading": {"governing_rules_and_history": "CURRENT-STATE.yaml", "matrix": MATRIX, "bets": BETS,
                             "source_register": SOURCES, "object_routing": "GEOMETER-VS-PHYSICS-OBJECTS.md",
                             "physics_ledger_pointer": "lab/methods/research-evidence-contract-v1.0.json",
                             "acceptance_and_claim_verification": "VERIFICATION.md"},
    }
    if not matrix:
        current["availability"] = "Live matrix not supplied; no current continuation inferred from historical prose."
    if target or claim:
        entry["requested_context"] = query_projection(target, claim, matrix, bets, register, packets)
    if history:
        entry["history_not_live_selection"] = {"program_focus_provenance": focus,
            "priority_direction_history": matrix.get("priority_direction_history", {}),
            "current_question_lead_partial": state["current_question"].strip().splitlines()[0],
            "next_condition_lead_partial": state["next_condition"].strip().splitlines()[0]}
    return NOTICE + "\n\n```yaml\n" + yaml.safe_dump(entry, sort_keys=False, allow_unicode=True) + "```\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    query = parser.add_mutually_exclusive_group()
    query.add_argument("--target", help="Exact cell (P3xglobal_index), intersection or bet ID")
    query.add_argument("--claim", help="Exact SC-ID; show its registered polarity and source custody")
    parser.add_argument("--history", action="store_true", help="Also show full dated focus provenance and explicitly historical lead text")
    args = parser.parse_args(argv)
    try:
        state = yaml.safe_load((ROOT / "CURRENT-STATE.yaml").read_text(encoding="utf-8"))
        matrix = json.loads((ROOT / MATRIX).read_text(encoding="utf-8"))
        bets = json.loads((ROOT / BETS).read_text(encoding="utf-8"))
        register = yaml.safe_load((ROOT / SOURCES).read_text(encoding="utf-8")) if args.target or args.claim else {}
        for name, value in (("CURRENT-STATE.yaml", state), (MATRIX, matrix), (BETS, bets), (SOURCES, register)):
            if not isinstance(value, dict):
                raise ValueError(f"{name} must be a mapping")
        paths = list(state.get("program_focus", {}).get("priority_packets", []))
        if args.target:
            record = target_records(matrix, bets).get(args.target, {})
            paths += [p for p in (record.get("packet"), record.get("alongside_packet")) if p]
        packets = {}
        for rel in dict.fromkeys(paths):
            path = (ROOT / rel).resolve()
            if not path.is_relative_to(ROOT.resolve()):
                raise ValueError(f"packet path escapes repository: {rel}")
            packets[rel] = packet_projection(path.read_text(encoding="utf-8"), rel)
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=False)
        revision = head.stdout.strip() if head.returncode == 0 else "unavailable (not a Git checkout)"
        print(render_context(state, "", matrix=matrix, bets=bets, register=register, packets=packets,
                             target=args.target, claim=args.claim, history=args.history, revision=revision), end="")
    except (OSError, ValueError, TypeError, KeyError, yaml.YAMLError) as exc:
        print(f"research_context: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
