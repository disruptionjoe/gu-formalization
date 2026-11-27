#!/usr/bin/env python3
"""Read-only projections of existing research owners; never a work selector."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
MATRIX = "lab/process/action-constraint-matrix.json"
BETS = "lab/process/discovery-bets.json"
SOURCES = "lab/sources/source-claim-register.yaml"
REUSE_INDEX = "lab/process/research-reuse-index.json"
PROGRESS_MAP = "lab/process/falsification-progress-map.json"
PROGRESS_PILLARS = ("gravity_shiab", "predictive_dynamics", "positive_energy",
                    "chirality_generations", "dark_energy", "gauge_mass_gap")
PROGRESS_LAYERS = ("source", "class", "candidate")
SIGNATURE_FIELDS = ("object", "carrier", "convention", "class", "premises")
REUSE_CEILING = (
    "Exact signature equality compares declarations only; it is not logical coverage or applicability. "
    "An author must validate that the question, premises and source bridge apply. Unknown or missing "
    "values cannot certify applicability. Recorded verification and current hashes are not fresh verification."
)
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


def repository_ref(root, ref):
    """Resolve a declared local reference without permitting traversal or symlink escapes."""
    if not isinstance(ref, str) or not ref.strip():
        raise ValueError("repository reference must be a nonempty string")
    path = re.sub(r":\d+(?:-\d+)?$", "", ref.split("#", 1)[0])
    parts = PurePosixPath(path)
    if not path or "\\" in path or ":" in path or parts.is_absolute() or ".." in parts.parts:
        raise ValueError(f"reference escapes repository or is not repository-relative: {ref}")
    resolved = (Path(root) / path).resolve()
    if not resolved.is_relative_to(Path(root).resolve()):
        raise ValueError(f"reference escapes repository: {ref}")
    return resolved


def validate_reuse_refs(value, root):
    """Check explicit reference fields, including optional history and cache metadata."""
    if isinstance(value, dict):
        for key, item in value.items():
            if key.endswith("_ref") and item is not None:
                repository_ref(root, item)
            elif key.endswith("_refs") and item is not None:
                if not isinstance(item, list):
                    raise ValueError(f"{key} must be a list of repository references")
                for ref in item:
                    repository_ref(root, ref)
            elif key == "artifacts" and isinstance(item, list):
                for artifact in item:
                    if isinstance(artifact, dict) and artifact.get("path") is not None:
                        repository_ref(root, artifact["path"])
            validate_reuse_refs(item, root)
    elif isinstance(value, list):
        for item in value:
            validate_reuse_refs(item, root)


def named_strings(value, prefix=""):
    if isinstance(value, str):
        yield prefix, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from named_strings(item, f"{prefix}.{key}" if prefix else str(key))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from named_strings(item, f"{prefix}[{i}]")


def unknown_fields(value, prefix=""):
    """Conservative declaration check, not a judgment of scientific completeness."""
    if value is None or value == "" or value == [] or value == {}:
        return [prefix]
    if isinstance(value, str):
        stripped = value.strip().lower()
        if not stripped or re.match(r"^(?:unknown|unspecified|not recorded|not supplied|missing|tbd|unavailable|undetermined)(?:\b|_)", stripped):
            return [prefix]
    if isinstance(value, dict):
        return [p for key, item in value.items() for p in unknown_fields(item, f"{prefix}.{key}")]
    if isinstance(value, list):
        return [p for i, item in enumerate(value) for p in unknown_fields(item, f"{prefix}[{i}]")]
    return []


def declaration_digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                         allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def signature_comparison(signature, hypothesis):
    def describe(value):
        if not isinstance(value, dict):
            return {"sha256": None, "unknown_fields": ["signature"]}
        missing = [f"signature.{key}" for key in SIGNATURE_FIELDS if key not in value]
        return {"sha256": declaration_digest(value), "unknown_fields": missing + unknown_fields(value, "signature")}
    recorded = describe(signature)
    result = {"recorded": recorded, "comparison": "not_requested", "applicability": "not_certified",
              "author_validation_required": True, "ceiling": REUSE_CEILING}
    if hypothesis is not None:
        proposed = describe(hypothesis.get("signature"))
        result["hypothesis"] = proposed
        left = signature if isinstance(signature, dict) else {}
        right = hypothesis.get("signature") if isinstance(hypothesis.get("signature"), dict) else {}
        result["different_fields"] = [key for key in sorted(set(left) | set(right))
                                      if key not in left or key not in right or left[key] != right[key]]
        result["comparison"] = ("unknown" if recorded["unknown_fields"] or proposed["unknown_fields"] else
                                "equal_declarations" if recorded["sha256"] == proposed["sha256"] else "different_declarations")
    return result


def verifier_description(value):
    missing = []
    if not isinstance(value, dict):
        return ["verifier"]
    if not isinstance(value.get("command"), str) or unknown_fields(value.get("command"), "verifier.command"):
        missing.append("verifier.command")
    if not isinstance(value.get("args"), list) or any(not isinstance(arg, str) for arg in value.get("args", [])):
        missing.append("verifier.args")
    elif value["args"]:
        missing += unknown_fields(value["args"], "verifier.args")
    if not isinstance(value.get("environment"), dict) or not value.get("environment"):
        missing.append("verifier.environment")
    else:
        missing += unknown_fields(value["environment"], "verifier.environment")
    return missing


def cache_projection(entry, hypothesis, check, root):
    cache = entry.get("cache")
    cache = cache if isinstance(cache, dict) else {}
    verifier = cache.get("verifier")
    has_expected = hypothesis is not None and "verifier" in hypothesis
    expected = hypothesis.get("verifier") if has_expected else None
    result = {"recorded": {"attributed_status": entry.get("attributed_status"),
                            "status_ref": entry.get("status_ref"), "receipt_ref": cache.get("receipt_ref"),
                            "verifier": verifier},
              "hash_state": "not_checked", "cache_state": "not_checked",
              "freshly_executed": False, "fresh_verification": "not_run",
              "ceiling": "Only declared files are hashed on request. Identity is recorded metadata, not authenticated by this reader. No verifier is imported or executed."}
    missing = verifier_description(verifier)
    identity = {"comparison": "not_requested", "different_fields": []}
    if has_expected:
        expected_missing = verifier_description(expected)
        keys = ("command", "args", "environment")
        identity["different_fields"] = [key for key in keys if not isinstance(verifier, dict) or not isinstance(expected, dict)
                                        or verifier.get(key) != expected.get(key)]
        identity["field_comparisons"] = {
            key: "unknown" if any(path == "verifier" or path.startswith(f"verifier.{key}") for path in missing + expected_missing)
            else "mismatch" if key in identity["different_fields"] else "equal_declarations"
            for key in keys
        }
        identity["comparison"] = ("mismatch" if "mismatch" in identity["field_comparisons"].values()
                                  else "unknown" if missing or expected_missing else "equal_declarations")
        identity["expected"] = expected
        missing += ["expected." + key for key in expected_missing]
    result["expected_verifier"] = identity
    artifacts = cache.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        missing.append("cache.artifacts")
        artifacts = []
    if not cache.get("receipt_ref"):
        missing.append("cache.receipt_ref")
    elif check and not repository_ref(root, cache["receipt_ref"]).is_file():
        missing.append("cache.receipt_ref (file missing)")
    checked = []
    for i, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict) or not isinstance(artifact.get("path"), str) or not re.fullmatch(r"[0-9a-fA-F]{64}", str(artifact.get("sha256", ""))):
            missing.append(f"cache.artifacts[{i}]")
            continue
        item = {"path": artifact["path"], "recorded_sha256": artifact["sha256"], "state": "not_checked"}
        if check:
            try:
                digest = hashlib.sha256()
                with repository_ref(root, artifact["path"]).open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                item.update(current_sha256=digest.hexdigest(), state="current" if digest.hexdigest() == artifact["sha256"].lower() else "stale")
            except FileNotFoundError:
                item.update(state="stale", reason="declared artifact is missing")
            except OSError as exc:
                item.update(state="unknown", reason=str(exc))
                missing.append(f"cache.artifacts[{i}] (unreadable)")
        checked.append(item)
    result["artifacts"] = checked
    result["unknown_fields"] = missing
    if check:
        states = {item["state"] for item in checked}
        result["hash_state"] = "stale" if "stale" in states else "unknown" if not checked or any("cache.artifacts" in item for item in missing) else "current"
        result["cache_state"] = "stale" if result["hash_state"] == "stale" or identity["comparison"] == "mismatch" else "unknown" if missing else "hash_current"
    return result


def reuse_projection(index, query, *, hypothesis=None, check_cache=False, root=None):
    """Literal lookup of a partial index; never rank, select, import or execute its contents."""
    root = Path(root) if root is not None else ROOT
    if not isinstance(index, dict) or index.get("schema_version") != "1.0" or "coverage" not in index or not isinstance(index.get("entries"), list):
        raise ValueError("reuse index requires schema_version '1.0', coverage and entries list")
    if not isinstance(query, str) or not query.strip():
        raise ValueError("--reuse needs a nonempty exact ID or literal text query")
    if hypothesis is not None and not isinstance(hypothesis, dict):
        raise ValueError("hypothesis JSON must be an object containing signature and optional verifier")
    validate_reuse_refs(index, root)
    entries = index["entries"]
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str) or not entry["id"] or entry.get("kind") not in ("result", "control", "dead_end"):
            raise ValueError("each reuse entry needs a nonempty id and kind result/control/dead_end")
        if entry["id"] in seen:
            raise ValueError(f"duplicate reuse entry ID: {entry['id']}")
        seen.add(entry["id"])
    exact = [entry for entry in entries if entry["id"] == query]
    matches = []
    for entry in exact or entries:
        fields = [path for path, value in named_strings(entry) if query.casefold() in value.casefold()]
        if exact or fields:
            matches.append({"entry": entry, "matched_fields": ["id"] if exact else fields,
                            "signature_comparison": signature_comparison(entry.get("signature"), hypothesis),
                            "cache": cache_projection(entry, hypothesis, check_cache, root)})
    return {"index_ref": REUSE_INDEX, "schema_version": index["schema_version"], "coverage": index["coverage"],
            "query": query, "matching": "exact ID" if exact else "case-insensitive literal substring in declared string values; index order retained",
            "match_count": len(matches), "matches": matches,
            "history_policy": "Superseded entries remain searchable; superseded_by is declared history, not inferred applicability.",
            "absence_ceiling": "No match means no literal match in this partial index; it does not mean no prior result exists.",
            "ceiling": REUSE_CEILING}


def progress_projection(data, *, root=None, revision=None):
    """Project an attributed 18-cell map; hashes check custody, never scientific truth."""
    root = Path(root) if root is not None else ROOT
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise ValueError("progress map requires schema_version '1.0'")
    if not re.fullmatch(r"[0-9a-f]{40}", str(data.get("basis_revision", ""))):
        raise ValueError("progress map needs a full basis_revision")
    pillars = data.get("pillars")
    if (not isinstance(pillars, list) or len(pillars) != 6
            or any(not isinstance(p, dict) for p in pillars)
            or {p.get("id") for p in pillars} != set(PROGRESS_PILLARS)):
        raise ValueError("progress map must contain the six distinct named pillars")
    # Validate every declared reference before opening any dependency.
    validate_reuse_refs(data, root)
    assumptions_ref = data.get("assumptions_ref")
    repository_ref(root, assumptions_ref)
    dependencies = data.get("dependencies")
    if not isinstance(dependencies, list):
        raise ValueError("progress map needs a dependencies list")
    pins, checked = {}, []
    for dep in dependencies:
        if not isinstance(dep, dict):
            raise ValueError("progress dependency must be an object")
        path = repository_ref(root, dep.get("ref"))
        if path in pins:
            raise ValueError("duplicate progress dependency file")
        pins[path] = dep
    for pillar in pillars:
        cells = pillar.get("cells")
        if not isinstance(cells, dict) or set(cells) != set(PROGRESS_LAYERS):
            raise ValueError("every pillar requires exactly source/class/candidate cells")
        for cell in cells.values():
            if not isinstance(cell, dict):
                raise ValueError("progress cell must be an object")
            for key in ("attributed_status", "closed", "open", "cheapest_next"):
                if not isinstance(cell.get(key), str) or not cell[key].strip():
                    raise ValueError(f"progress cell requires nonempty {key}")
            repository_ref(root, cell.get("shared_missing_ref"))
            refs = cell.get("evidence_refs")
            if not isinstance(refs, list) or not refs:
                raise ValueError("progress cell needs evidence_refs")
            for ref in refs:
                repository_ref(root, ref)
    states = {}
    for path, dep in pins.items():
        item = {"ref": dep["ref"], "recorded_sha256": dep.get("sha256"),
                "freshness": "needs_recheck"}
        if not re.fullmatch(r"[0-9a-f]{64}", str(dep.get("sha256", ""))):
            item["reason"] = "missing or invalid SHA256 pin"
        else:
            try:
                with path.open("rb") as stream:
                    hasher = hashlib.sha256()
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        hasher.update(chunk)
                    digest = hasher.hexdigest()
                item["current_sha256"] = digest
                if digest == dep["sha256"]:
                    item["freshness"] = "hash_current"
                else:
                    item["reason"] = "dependency bytes changed"
            except OSError:
                item["reason"] = "dependency missing or unreadable"
        states[path] = item
        checked.append(item)
    projected = []
    for pillar in pillars:
        cells = {}
        for layer, cell in pillar["cells"].items():
            refs = [assumptions_ref, cell["shared_missing_ref"], *cell["evidence_refs"]]
            stale = [ref for ref in dict.fromkeys(refs)
                     if states.get(repository_ref(root, ref), {}).get("freshness") != "hash_current"]
            cells[layer] = {**cell, "freshness": "needs_recheck" if stale else "hash_current",
                            "recheck_refs": stale}
        projected.append({"id": pillar["id"], "label": pillar.get("label", pillar["id"]), "cells": cells})
    return {"map_ref": PROGRESS_MAP, "basis_revision": data["basis_revision"],
            "checked_out_revision": revision or "not supplied", "scope": data.get("scope"),
            "assumptions_ref": assumptions_ref, "dependencies": checked, "pillars": projected,
            "freshness": "needs_recheck" if (any(d["freshness"] == "needs_recheck" for d in checked)
                or any(c["freshness"] == "needs_recheck"
                       for p in projected for c in p["cells"].values())) else "hash_current",
            "ceiling": "Linked attributed evidence only; no source verdict, semantic ranking, work selection or global completion percentage. Hash equality checks declared file custody only, not scientific applicability, fresh verification or remote synchronization. Missing or changed dependencies require recheck; omitted evidence is not absent knowledge."}


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
    query.add_argument("--reuse", metavar="QUERY", help="Exact indexed report ID, otherwise literal case-insensitive text search")
    query.add_argument("--progress-map", action="store_true", help="Read the linked six-pillar/three-layer map and check its pinned dependency hashes")
    parser.add_argument("--hypothesis", metavar="JSON_PATH", help="Compare explicit signature and optional verifier declarations; requires --reuse")
    parser.add_argument("--check-cache", action="store_true", help="Hash declared cache artifacts only; never execute the verifier; requires --reuse")
    parser.add_argument("--history", action="store_true", help="Also show full dated focus provenance and explicitly historical lead text")
    args = parser.parse_args(argv)
    if (args.hypothesis or args.check_cache) and args.reuse is None:
        parser.error("--hypothesis and --check-cache require --reuse")
    try:
        if args.progress_map:
            data = json.loads(repository_ref(ROOT, PROGRESS_MAP).read_text(encoding="utf-8"))
            head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, capture_output=True, check=False)
            revision = head.stdout.strip() if head.returncode == 0 else "unavailable (not a Git checkout)"
            view = progress_projection(data, root=ROOT, revision=revision)
            print(NOTICE + "\n\n```yaml\n" + yaml.safe_dump({"progress_map": view}, sort_keys=False, allow_unicode=True) + "```\n", end="")
            return 0
        if args.reuse is not None:
            index = json.loads(repository_ref(ROOT, REUSE_INDEX).read_text(encoding="utf-8"))
            hypothesis = json.loads(Path(args.hypothesis).read_text(encoding="utf-8")) if args.hypothesis else None
            view = reuse_projection(index, args.reuse, hypothesis=hypothesis, check_cache=args.check_cache)
            print(NOTICE + "\n\n```yaml\n" + yaml.safe_dump({"requested_reuse": view}, sort_keys=False, allow_unicode=True) + "```\n", end="")
            return 0
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
