#!/usr/bin/env python3
"""Mint context-projection audit (CT-2, joe-directed brief 2026-08-17).

THE RULE, enforced here.  From conditional-physics ledger version v0.260
onward, every row a mint TOUCHES -- appends, or changes the content of --
carries a `context` object giving that row's (layer, grant, carrier)
projection into the three base categories of lab/methods/gu-base-categories.md
(CT-1).  Authors' statement of the rule, with the naming traps and the worked
shape: lab/methods/mint-context-projection.md.  Shape: the additive sibling
schema lab/process/conditional-physics-ledger-schema-v0.2.json (v0.1 is not
edited; all 259 live ledgers validate against v0.2 unchanged).

WHY A GATE AND NOT JUST A SCHEMA.  "Touched" is a TWO-DOCUMENT predicate --
this ledger versus its `predecessor` -- and no single-document JSON Schema can
decide it.  The schema pins the SHAPE of a projection token (the L#/G#/C#
grammar); this gate pins MEMBERSHIP (that `L3` is an object CT-1 actually
carries today) and AGREEMENT (that the projection does not contradict the row
it describes).  The split is deliberate: a schema that hardcoded CT-1's object
list would drift from CT-1 silently, so membership is read from that file on
every run and fails closed.

SCOPE (non-retroactive BY CONSTRUCTION, not by tolerance):
  in scope      ledger version >= 0.260
  out of scope  v0.259 and every earlier version -- permanently.  The ledger
                series is append-only and each version immutable, so this
                boundary cannot move backward: v0.259 will still be v0.259
                next year.  No existing row is edited, no sweep is run, and
                the baseline is 0 and stays 0.  Nothing in today's checkout is
                in scope at all, so the clean baseline is green by
                construction and the probe asserts it.
  VERSION ORDER IS NUMERIC ON THE MINOR COMPONENT.  0.26 is twenty-six and
  precedes 0.259; string ordering of these values is WRONG and would drag
  every v0.3x/v0.9x ledger into scope.  Versions are compared as int tuples.
  Scope is decided by max(filename version, internal schema_version) so a
  ledger cannot leave scope by being misfiled -- measured 2026-08-17, exactly
  one live file disagrees with its own name (v0.134 declares 0.133), which is
  why this is a max and not a trust.

WHAT "TOUCHED" MEANS.  A row is touched at version V if its id is absent from
V's predecessor, or if its content differs from the predecessor row of that
id.  Content comparison EXCLUDES the `context` key, so accreting context onto
an otherwise-unchanged row is not itself a content change -- that is what
makes voluntary accretion free.  Unresolvable predecessor => every row counts
as touched (fail closed: an unresolvable base is a reason to type more).

CN-2 PRINCIPLE, load-bearing and unaltered.  UNTYPED is always in codomain,
always legal, always counted, printed every run; HOMONYM-AMBIGUOUS is the
same for the registered-homonym class.  An all-UNTYPED context is GREEN and
is path/row-printed by the census.  Making honesty red would train
plausible-token lying, which is strictly worse than a declared gap.  One
notch is added over FX-2 and stated rather than smuggled: any UNTYPED slot
requires a non-empty `note`, because a bare UNTYPED is a blank and a
DECLARATION of ambiguity is a sentence.  The gate checks the note EXISTS and
prints it verbatim.  It cannot check that it is TRUE and claims no such power.

THE NEVER-LAUNDER INTERACTION.  A grant projection must AGREE with the
conditions the row already states in its own fields; disagreement is a RED for
adjudication, never a silent fix of either side.  Three mechanical forms:
  L  LAUNDER-IN-PROJECTION -- `G0` (the empty assumption set) on a row whose
     reason_kind is DERIVED_CONDITIONAL.  This performs, in the projection,
     exactly the move the ledger forbids in the row ("DERIVED_CONDITIONAL ->
     DERIVED is forbidden", v0.259 migration_policy).
  O  OVERCLAIM -- a non-empty node on a row whose reason_kind is exactly
     DERIVED.  CT-1 defines G0 AS the DERIVED family.
  M  GRANT-OMITS-NAMED-CONDITION -- the row's own text names a condition CT-1
     assigns to a node, and the projection omits that node.  The markers are
     NOT invented here: they are extracted from the braced names of CT-1's own
     Grant-poset objects ({GRANT-ACA1-C1}, {INHERITANCE_BRIDGE}, {SC-CHI-01
     ...}, {HYP-TW-COHERENCE-01 ...}).  If CT-1 renames a node the marker set
     follows; if CT-1 ever carries NO extractable marker the gate REDS rather
     than passing silently, because a rule that has quietly lost its teeth
     must not read as green.
  Rule M is the ONE place UNTYPED is not an escape, and that is the
  principled line: declared ambiguity is compliance about what is GENUINELY
  ambiguous, and a row that spells its own condition out is not ambiguous.

WHAT THIS GATE CANNOT DO, stated rather than implied.  Token ids are opaque
and in-codomain by construction: a mint that writes `L2` where `L1` is right,
or `C9` where `C8` is right, produces a projection this gate calls green.
Membership and agreement are checkable; CORRECTNESS is not.  The instrument's
honest claim is that the projection EXISTS, is IN CODOMAIN, and does NOT
CONTRADICT the row -- and that every ambiguity and every note is printed where
a reader can see it.  A green scan bounds exactly that and nothing more.

Report-only census, printed EVERY run: per-ledger touched/typed/untyped
counts as exact fractions (no float anywhere), per-slot token histograms,
ALL-UNTYPED row ids, conditional rows whose grant is UNTYPED, and every note
verbatim.  The census never contributes to the exit code.

Self-test: --selftest builds fixture ledgers and a fixture CT-1 reference,
verifies the CLEAN BASELINE exits 0 BEFORE any planted fact, then plants
twelve false facts -- a touched row with no context, out-of-codomain tokens,
the launder, the overclaim, the omitted named condition, an undeclared
UNTYPED, a mixed slot, a malformed context, an unknown context key, a
corrupted reference and a toothless reference -- each required to drive
exit 1; exits 0 iff all behave.  --selftest --poison-baseline corrupts the
clean set to prove the baseline guard itself has power (prints the refusal
and exits 1).
"""

from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import sys

BASELINE = 0  # nothing existing is in scope; never raise this to green a red
SCOPE_MIN = (0, 260)  # ledger versions >= v0.260; v0.259 and earlier never

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     os.pardir))
REFERENCE_REL = "lab/methods/gu-base-categories.md"
REFERENCE_PATH = os.path.join(ROOT, "lab", "methods", "gu-base-categories.md")
RULE_REL = "lab/methods/mint-context-projection.md"
SCHEMA_REL = "lab/process/conditional-physics-ledger-schema-v0.2.json"
LEDGER_GLOB = os.path.join(ROOT, "lab", "process",
                           "conditional-physics-ledger-v*.json")
HISTORY_REPAIR_REL = "lab/process/mint-context-history-repairs.json"
HISTORY_REPAIR_PATH = os.path.join(ROOT, "lab", "process",
                                   "mint-context-history-repairs.json")

CONTEXT_KEY = "context"
SLOTS = ("layer", "grant", "carrier")
NOTE_KEY = "note"
CONTEXT_KEYS = SLOTS + (NOTE_KEY,)
UNTYPED = "UNTYPED"
HOMONYM_AMBIGUOUS = "HOMONYM-AMBIGUOUS"
# One class of declared unknown, per CT-1 markers M1 and M4: both are always
# legal, both are counted in the ambiguity census, both need a note.
DECLARED_UNKNOWNS = (UNTYPED, HOMONYM_AMBIGUOUS)

# reason_kind vocabulary this gate reads out of the ledger (CT-1 section 2.1
# defines G0 as the `reason_kind: DERIVED` family; v0.259's migration_policy
# forbids DERIVED_CONDITIONAL -> DERIVED).  These are ledger constants, not
# predicates: corrupting one is a machinery corruption the selftest plants.
KIND_UNCONDITIONAL = "DERIVED"
KIND_CONDITIONAL = "DERIVED_CONDITIONAL"
NODE_EMPTY = "G0"

VERSION_IN_NAME = re.compile(r"-v(\d+)\.(\d+)\.json$")
VERSION_VALUE = re.compile(r"^(\d+)\.(\d+)$")

# CT-1 table row shapes.  Object/marker rows have exactly five cells:
# | <ID> | <name> | <role> | <statement> | <receipts> |
OBJ_ROW_RE = re.compile(
    r"^\|\s*([LGCM]\d+)\s*\|\s*([^|]+?)\s*\|\s*([a-z-]+)\s*\|"
    r"\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$", re.M)
# A braced assumption-set name, e.g. `{GRANT-ACA1-C1}`, `{SC-CHI-01 VEV if}`.
BRACED_RE = re.compile(r"\{([^}]*)\}")
# A condition marker: an ALL-CAPS token with at least one -/_ separator.
# `SELECTED` (no separator) is deliberately too generic to be a marker.
MARKER_RE = re.compile(r"[A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)+")

_MUT = os.environ.get("CT2_GATE_MUTATE", "")


# ======================================================================
# codomains -- read from CT-1 on every run, fail closed
# ======================================================================
def read_codomains(path=None):
    """Return (codomains, errors) read from CT-1's object/marker tables.

    Fails closed in every direction: a missing file, an empty codomain, a
    missing required marker, a category over CT-1's own <= 12 budget, or a
    Grant poset carrying no extractable condition marker are each an error.
    The last one matters most: a rule that has quietly lost its teeth must
    RED, never read as green.
    """
    path = REFERENCE_PATH if path is None else path
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return None, ["codomain reference missing: " + REFERENCE_REL]

    layers, grants, carriers, markers = set(), set(), set(), {}
    for rid, name, role, _stmt, _rcpt in OBJ_ROW_RE.findall(text):
        if rid.startswith("L") and role == "object":
            layers.add(rid)
        elif rid.startswith("G") and role in ("object", "bucket"):
            # role `bucket` is a presentation class, not a single set, but a
            # row can legitimately OCCUPY it (CT-1 2.1: RA-F2 sits at G8), so
            # it is in the codomain of the grant slot.
            grants.add(rid)
        elif rid.startswith("C") and role == "object":
            carriers.add(rid)
        elif rid.startswith("M") and role.endswith("marker"):
            tok = re.match(r"^([A-Z][A-Z0-9/-]*)", name)
            if tok:
                markers[tok.group(1)] = role

    # condition markers, derived from CT-1's own braced Grant-object names
    condition_markers = {}
    for rid, name, role, _stmt, _rcpt in OBJ_ROW_RE.findall(text):
        if not rid.startswith("G") or role not in ("object", "bucket"):
            continue
        for braced in BRACED_RE.findall(name):
            for marker in MARKER_RE.findall(braced):
                condition_markers.setdefault(marker, rid)

    errors = []
    for label, got in (("layer", layers), ("grant", grants),
                       ("carrier", carriers)):
        if not got:
            errors.append("codomain reference yields no %s objects" % label)
        elif len(got) > 12:
            errors.append("codomain reference exceeds CT-1's <=12 budget on "
                          "%s (%d)" % (label, len(got)))
    for required in (UNTYPED, HOMONYM_AMBIGUOUS):
        if required not in markers:
            errors.append("codomain reference no longer declares the marker "
                          + required)
    if not condition_markers:
        errors.append("codomain reference yields no grant condition markers: "
                      "the never-launder agreement rule would be toothless "
                      "and must not read as green")
    if errors:
        return None, errors

    if _MUT == "carrier-cod-drop":
        carriers = set(sorted(carriers)[:1])
    return ({"layer": layers | {UNTYPED},
             "grant": grants | {UNTYPED},
             "carrier": carriers | {UNTYPED, HOMONYM_AMBIGUOUS},
             "condition_markers": condition_markers}, [])


# ======================================================================
# versions, scope and predecessors
# ======================================================================
def parse_version(value):
    m = VERSION_VALUE.match(str(value).strip().strip('"').strip("'"))
    return (int(m.group(1)), int(m.group(2))) if m else None


def ledger_version(path, doc):
    """max(filename version, internal schema_version); None if neither parses.

    A max, not a trust: a ledger must not be able to leave scope by being
    misfiled.  Measured 2026-08-17, v0.134.json declares schema_version 0.133.
    """
    seen = []
    m = VERSION_IN_NAME.search(os.path.basename(path))
    if m:
        seen.append((int(m.group(1)), int(m.group(2))))
    if isinstance(doc, dict):
        inner = parse_version(doc.get("schema_version", ""))
        if inner:
            seen.append(inner)
    return max(seen) if seen else None


def in_scope(version):
    return version is not None and version >= SCOPE_MIN


def resolve_predecessor(path, doc, catalogue):
    """Declared `predecessor` first, else the greatest earlier version."""
    declared = doc.get("predecessor") if isinstance(doc, dict) else None
    if isinstance(declared, str) and declared.strip():
        cand = declared.strip()
        for guess in (os.path.join(ROOT, cand), cand,
                      os.path.join(os.path.dirname(path),
                                   os.path.basename(cand))):
            if os.path.isfile(guess):
                return guess
    mine = ledger_version(path, doc)
    best, best_v = None, None
    for other, other_v in catalogue.items():
        if other == path or other_v is None or mine is None:
            continue
        if other_v < mine and (best_v is None or other_v > best_v):
            best, best_v = other, other_v
    return best


def row_content(row):
    """Row content for the touched-comparison: everything but `context`."""
    key = "ctx" if _MUT == "context-key-drift" else CONTEXT_KEY
    return {k: v for k, v in row.items() if k != key}


def _sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _row_jsonl_sha256(row):
    payload = json.dumps(row_content(row), sort_keys=True,
                         separators=(",", ":")) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def read_history_repairs(path=HISTORY_REPAIR_PATH):
    """Load exact, append-only exceptions for already-immutable mint history.

    A repair is not a tolerance. It pins the complete historical ledger, the
    canonical historical row, and an exact context carried by a named
    successor. Any byte drift or missing successor fails closed.
    """
    if not os.path.isfile(path):
        return {}, []
    try:
        payload = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return {}, ["history repair registry unreadable: %s" % exc]
    rows = payload.get("repairs") if isinstance(payload, dict) else None
    if not isinstance(rows, list):
        return {}, ["history repair registry has no repairs array"]
    result, errors = {}, []
    required = ("repair_id", "source_ledger_ref", "source_ledger_sha256",
                "row_id", "source_row_jsonl_sha256",
                "successor_ledger_ref", "context")
    for i, item in enumerate(rows):
        if not isinstance(item, dict):
            errors.append("history repair %d is not an object" % i)
            continue
        missing = [key for key in required if key not in item]
        if missing:
            errors.append("history repair %d missing %s" %
                          (i, ", ".join(missing)))
            continue
        key = (item["source_ledger_ref"], item["row_id"])
        if key in result:
            errors.append("duplicate history repair for %s row %s" % key)
            continue
        result[key] = item
    return result, errors


def validate_history_repair(source_path, source_rel, row, repair):
    failures = []
    try:
        if _sha256_file(source_path) != repair["source_ledger_sha256"]:
            failures.append("source ledger SHA-256 drift")
    except OSError:
        failures.append("source ledger unreadable")
    if _row_jsonl_sha256(row) != repair["source_row_jsonl_sha256"]:
        failures.append("source row canonical JSON-line SHA-256 drift")
    successor_path = os.path.join(ROOT, repair["successor_ledger_ref"])
    try:
        successor = json.load(open(successor_path, encoding="utf-8"))
        matches = [candidate for candidate in successor.get("rows", [])
                   if isinstance(candidate, dict) and
                   candidate.get("id") == row.get("id")]
        if len(matches) != 1:
            failures.append("successor does not carry exactly one matching row")
        elif matches[0].get(CONTEXT_KEY) != repair["context"]:
            failures.append("successor context differs from repair registry")
    except (OSError, ValueError, AttributeError):
        failures.append("successor ledger unreadable")
    return failures


# ======================================================================
# context validation
# ======================================================================
def _tokens(value):
    if isinstance(value, str):
        return [value], []
    if isinstance(value, list):
        if not value:
            return [], ["empty array (absence of an opinion is spelled "
                        "UNTYPED, not omitted)"]
        bad = [t for t in value if not isinstance(t, str) or not t]
        if bad:
            return [], ["array holds a non-string or empty token"]
        if len(set(value)) != len(value):
            return [], ["array repeats a token"]
        return list(value), []
    return [], ["slot is neither a token nor an array of tokens"]


def marker_hits(row, condition_markers):
    """Condition markers the row's own text names, mapped to their nodes."""
    if _MUT == "marker-scan-blind":
        return {}
    text = json.dumps(row_content(row), sort_keys=True)
    hits = {}
    for marker, node in condition_markers.items():
        if re.search(r"(?<![A-Za-z0-9_-])%s(?![A-Za-z0-9_-])"
                     % re.escape(marker), text):
            hits[marker] = node
    return hits


def validate_context(row, cod):
    """Return (defects, per-slot tokens, untyped_slot_count, all_untyped)."""
    ctx = row.get(CONTEXT_KEY)
    if not isinstance(ctx, dict):
        return (["`context` is not an object"], {}, 0, False)

    defects = []
    for key in sorted(set(ctx) - set(CONTEXT_KEYS)):
        defects.append("unknown key in context: " + key)

    tokens, untyped_slots = {}, 0
    for slot in SLOTS:
        if slot not in ctx:
            defects.append("context missing slot: " + slot)
            continue
        toks, shape = _tokens(ctx[slot])
        for why in shape:
            defects.append("%s %s" % (slot, why))
        if shape:
            continue
        tokens[slot] = toks
        outside = [t for t in toks if t not in cod[slot]]
        for t in outside:
            defects.append("out-of-codomain %s token %r (codomain owner %s)"
                           % (slot, t, REFERENCE_REL))
        # Declared unknowns are counted in the ambiguity census exactly as
        # FX-2's gate counts them and as CT-1 M4 states ("counted in the
        # ambiguity census like every declared unknown"): UNTYPED and
        # HOMONYM-AMBIGUOUS are one class, so they share the count, the note
        # requirement and the no-mixing rule.
        declared_unknown = [t for t in toks if t in DECLARED_UNKNOWNS]
        if declared_unknown:
            untyped_slots += 1
            if len(toks) > 1:
                defects.append("%s mixes %s with objects: a slot that names "
                               "an object and also declares ignorance says "
                               "nothing" % (slot, declared_unknown[0]))

    note = ctx.get(NOTE_KEY)
    if untyped_slots and not (isinstance(note, str) and note.strip()):
        defects.append("declared-unknown slot without a `note`: declared "
                       "ambiguity is compliance, but a declaration is a "
                       "sentence, not a blank (%d declared-unknown slot(s))"
                       % untyped_slots)
    if note is not None and not isinstance(note, str):
        defects.append("`note` is not a string")

    all_untyped = bool(tokens) and len(tokens) == len(SLOTS) and all(
        set(v) <= {UNTYPED, HOMONYM_AMBIGUOUS} for v in tokens.values())

    # ---- the never-launder interaction: grant must agree with the row ----
    grant = tokens.get("grant")
    kind = str(row.get("reason_kind", ""))
    if grant is not None:
        if kind.startswith(KIND_CONDITIONAL) and NODE_EMPTY in grant:
            defects.append(
                "LAUNDER-IN-PROJECTION: grant names %s (the empty assumption "
                "set) on a reason_kind %s row. The row advances under a "
                "condition; the projection says it advances under none. "
                "Adjudicate which is wrong -- do not silently fix either"
                % (NODE_EMPTY, kind))
        if kind == KIND_UNCONDITIONAL:
            over = [g for g in grant if g not in (NODE_EMPTY, UNTYPED)]
            if over:
                defects.append(
                    "GRANT-ROW DISAGREEMENT: grant names %s on a reason_kind "
                    "%s row, and %s defines %s as the %s family (%s). "
                    "Adjudicate -- do not silently fix either"
                    % (", ".join(sorted(over)), KIND_UNCONDITIONAL,
                       REFERENCE_REL, NODE_EMPTY, KIND_UNCONDITIONAL,
                       "CT-1 section 2.1"))
        for marker, node in sorted(marker_hits(row, cod["condition_markers"]).items()):
            if node not in grant:
                defects.append(
                    "GRANT-OMITS-NAMED-CONDITION: the row's own text names "
                    "%s, which %s assigns to %s, and the grant projection "
                    "(%s) omits it. A row that spells its own condition out "
                    "is not ambiguous about it, so UNTYPED is not an escape "
                    "here" % (marker, REFERENCE_REL, node,
                              ", ".join(grant)))
    return defects, tokens, untyped_slots, all_untyped


# ======================================================================
# audit
# ======================================================================
def audit(paths=None, baseline=None, reference=None, verbose=True):
    baseline = BASELINE if baseline is None else baseline
    out = []

    def say(line):
        out.append(line)
        if verbose:
            print(line)

    files = sorted(paths) if paths is not None else sorted(glob.glob(LEDGER_GLOB))
    catalogue, docs = {}, {}
    for f in files:
        try:
            docs[f] = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError):
            docs[f] = None
        catalogue[f] = ledger_version(f, docs[f])

    scoped = [f for f in files if in_scope(catalogue[f])]
    out_of_scope = [f for f in files if not in_scope(catalogue[f])]

    red = []
    repairs, repair_errors = read_history_repairs() if paths is None else ({}, [])
    used_repairs = set()
    for why in repair_errors:
        red.append((HISTORY_REPAIR_REL, why))
    cod, cod_errors = read_codomains(reference)
    if cod_errors and scoped:
        for why in cod_errors:
            red.append((REFERENCE_REL, why))

    census = []
    for f in scoped:
        rel = os.path.relpath(f, ROOT)
        doc = docs[f]
        if doc is None or not isinstance(doc.get("rows"), list):
            red.append((rel, "in-scope ledger is unreadable or has no rows"))
            continue
        pred_path = resolve_predecessor(f, doc, catalogue)
        pred_rows = {}
        pred_ok = False
        if pred_path:
            try:
                pdoc = json.load(open(pred_path, encoding="utf-8"))
                pred_rows = {r.get("id"): r for r in pdoc.get("rows", [])
                             if isinstance(r, dict)}
                pred_ok = True
            except (OSError, ValueError):
                pred_ok = False
        if _MUT == "pred-blind":
            pred_rows = {r.get("id"): r for r in doc.get("rows", [])}
            pred_ok = True

        stat = {"ledger": rel, "version": "%d.%d" % catalogue[f],
                "predecessor": (os.path.relpath(pred_path, ROOT)
                                if pred_path else "UNRESOLVED"),
                "rows": 0, "touched": 0, "touched_typed": 0,
                "history_repaired": 0,
                "untouched_typed": 0, "untyped_slots": 0,
                "all_untyped_rows": [], "cond_untyped_grant": [],
                "notes": [], "hist": {s: {} for s in SLOTS}}
        for row in doc["rows"]:
            if not isinstance(row, dict):
                red.append((rel, "row is not an object"))
                continue
            stat["rows"] += 1
            rid = row.get("id", "<no id>")
            prev = pred_rows.get(rid)
            touched = (not pred_ok) or prev is None or \
                row_content(row) != row_content(prev)
            if touched:
                stat["touched"] += 1
            has = CONTEXT_KEY in row
            if touched and not has:
                repair_key = (rel, rid)
                repair = repairs.get(repair_key)
                if repair is not None:
                    failures = validate_history_repair(f, rel, row, repair)
                    used_repairs.add(repair_key)
                    if failures:
                        for why in failures:
                            red.append((rel, "row %s history repair invalid: %s"
                                        % (rid, why)))
                    else:
                        stat["history_repaired"] += 1
                        stat["notes"].append((rid, "HISTORY-REPAIRED via %s; "
                                              "context accreted at %s" %
                                              (repair["repair_id"],
                                               repair["successor_ledger_ref"])))
                    continue
                red.append((rel, "row %s is touched at v%s and carries no "
                                 "`%s` (rule: %s)"
                            % (rid, stat["version"], CONTEXT_KEY, RULE_REL)))
                continue
            if not has:
                continue
            if cod is None:
                continue  # codomain already red; do not double-report
            defects, tokens, untyped, all_untyped = validate_context(row, cod)
            for d in defects:
                red.append((rel, "row %s context: %s" % (rid, d)))
            if touched:
                stat["touched_typed"] += 1
            else:
                stat["untouched_typed"] += 1
            stat["untyped_slots"] += untyped
            if all_untyped:
                stat["all_untyped_rows"].append(rid)
            for slot, toks in tokens.items():
                for t in toks:
                    stat["hist"][slot][t] = stat["hist"][slot].get(t, 0) + 1
            kind = str(row.get("reason_kind", ""))
            if kind.startswith(KIND_CONDITIONAL) and \
                    tokens.get("grant") == [UNTYPED]:
                stat["cond_untyped_grant"].append(rid)
            ctx = row[CONTEXT_KEY]
            note = ctx.get(NOTE_KEY) if isinstance(ctx, dict) else None
            if isinstance(note, str) and note.strip():
                stat["notes"].append((rid, note.strip()))
        census.append(stat)

    if paths is None:
        for repair_key in sorted(set(repairs) - used_repairs):
            red.append((HISTORY_REPAIR_REL,
                        "unused repair does not match a live touched row: %s row %s"
                        % repair_key))

    for f, why in red:
        say("RED  %s: %s" % (f, why))
    say("mint_context_projection_audit: %d red (baseline %d); %d ledger(s) in "
        "scope >= v%d.%d; %d out of scope BY CONSTRUCTION (non-retroactive)"
        % (len(red), baseline, len(scoped), SCOPE_MIN[0], SCOPE_MIN[1],
           len(out_of_scope)))
    if out_of_scope:
        top = max((catalogue[f] for f in out_of_scope
                   if catalogue[f] is not None), default=None)
        say("mint_context_projection_audit[non-retroactive]: highest "
            "out-of-scope version v%s; those rows are never required to carry "
            "`%s` and none was edited to add one"
            % ("%d.%d" % top if top else "?", CONTEXT_KEY))
    say("mint_context_projection_audit[codomain]: %s vs %s: %s"
        % ("layer/grant/carrier", REFERENCE_REL,
           ("read (%d/%d/%d objects incl. markers; %d condition markers)"
            % (len(cod["layer"]), len(cod["grant"]), len(cod["carrier"]),
               len(cod["condition_markers"]))) if cod
           else "%d error(s) -- fail closed" % len(cod_errors)))

    # ---- report-only census, printed every run ----
    if not census:
        say("mint_context_projection_audit[census]: no in-scope ledger; "
            "context coverage is vacuously complete and proves nothing")
    for stat in census:
        say("mint_context_projection_audit[census] %s (v%s, base %s): "
            "%d rows; touched %d; touched-with-context %d/%d; historical "
            "repairs %d; voluntary "
            "accretion on untouched rows %d; UNTYPED slots %d"
            % (stat["ledger"], stat["version"], stat["predecessor"],
               stat["rows"], stat["touched"], stat["touched_typed"],
               stat["touched"], stat["history_repaired"],
               stat["untouched_typed"],
               stat["untyped_slots"]))
        for slot in SLOTS:
            hist = stat["hist"][slot]
            say("  [census:%s] %s" % (slot, ", ".join(
                "%s=%d" % (k, hist[k]) for k in sorted(hist)) or "(none)"))
        say("  [census:all-untyped] %s"
            % (", ".join(stat["all_untyped_rows"]) or "none"))
        say("  [census:conditional-row-with-UNTYPED-grant] %s"
            % (", ".join(stat["cond_untyped_grant"]) or "none"))
        for rid, note in stat["notes"]:
            say("  [census:note] %s: %s" % (rid, note))
    say("mint_context_projection_audit[ceiling]: token ids are opaque and "
        "in-codomain by construction, so a projection that is WRONG but "
        "well-formed passes. This gate bounds existence, codomain membership "
        "and non-contradiction with the row -- never correctness.")

    stats = {"red": len(red), "scoped": len(scoped),
             "out_of_scope": len(out_of_scope),
             "codomain_errors": len(cod_errors), "census": census,
             "lines": out}
    return (1 if len(red) > baseline else 0), stats


# ======================================================================
# self-test
# ======================================================================
REF_FIXTURE = """---
title: fixture
---
### 1.1 Objects

| ID | object | role | statement | receipts |
|---|---|---|---|---|
| L1 | declared-total | object | the unsubscripted four-corner arena | r |
| L2 | pullback | object | the Weyl-pullback layer | r |

### 2.1 Objects

| ID | object | role | statement | receipts |
|---|---|---|---|---|
| G0 | empty set (unconditional) | object | `reason_kind: DERIVED` | r |
| G1 | {GRANT-ACA1-C1} | object | the declared grant | r |
| G5 | {INHERITANCE_BRIDGE} | object | the typed named condition | r |
| G8 | in-row stated conditional | bucket | condition stated in-row | r |

### 3.1 Objects

| ID | object | role | statement | receipts |
|---|---|---|---|---|
| C1 | ambient | object | LAYER stratum: ambient geometry | r |
| C5 | S-FULL-DIRAC | object | the full 128-complex Dirac bundle | r |

### 3.2 Markers

| ID | token | role | statement | receipts |
|---|---|---|---|---|
| M1 | UNTYPED (LAYER slot and elsewhere) | declared-unknown-marker | legal | r |
| M4 | HOMONYM-AMBIGUOUS | declared-unknown-marker | the escape | r |
"""


def _row(rid, kind="MISSING_CONSTRUCTION", ctx=None, extra=None, tail="x"):
    row = {"id": rid, "axis": "LAGRANGIAN", "source_row": "CB-B:" + rid,
           "summary": "s " + tail, "verdict": "NEEDS", "reason_kind": kind,
           "distance": "d " + tail, "revival_trigger": "t", "evidence": "e",
           "mapping_grade": "M"}
    if extra:
        row.update(extra)
    if ctx is not None:
        row[CONTEXT_KEY] = ctx
    return row


def _ledger(version, rows, predecessor=None):
    doc = {"schema_version": version, "rows": rows}
    if predecessor:
        doc["predecessor"] = predecessor
    return doc


def _write(tmp, name, doc):
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh)
    return path


def _clean_fixtures(tmp, poison=False):
    """Base v0.259 + the clean in-scope set. Every file here must be GREEN."""
    base_rows = [
        _row("R1"), _row("R2"), _row("R3"),
        _row("R4", kind="DERIVED"), _row("R5", kind="DERIVED_CONDITIONAL"),
        _row("R6", extra={"debt": "carries INHERITANCE_BRIDGE"}),
    ]
    files = []
    # out of scope by construction: touched rows, no context anywhere.
    files.append(_write(tmp, "conditional-physics-ledger-v0.259.json",
                        _ledger("0.259", base_rows)))
    # out of scope and NUMERICALLY earlier though lexically later: v0.30 is
    # thirty.  Carries a defect that would red if scope compared strings.
    files.append(_write(tmp, "conditional-physics-ledger-v0.30.json",
                        _ledger("0.30", [_row("R1", tail="changed")])))
    ok_rows = [
        _row("R1"),                                    # untouched, no context
        _row("R2", tail="moved", ctx={"layer": "L1", "grant": "G0",
                                      "carrier": "C5"}),
        _row("R3", tail="moved", ctx={"layer": UNTYPED, "grant": UNTYPED,
                                      "carrier": UNTYPED,
                                      "note": "honestly nothing is named"}),
        _row("R4", kind="DERIVED", tail="moved",
             ctx={"layer": "L2", "grant": UNTYPED, "carrier": "C1",
                  "note": "unconditional; no node asserted"}),
        _row("R5", kind="DERIVED_CONDITIONAL", tail="moved",
             ctx={"layer": "L1", "grant": ["G1", "G5"],
                  "carrier": HOMONYM_AMBIGUOUS,
                  "note": "bare ad(P_H) names no object",
                  }, extra={"why": "GRANT-ACA1-C1 and INHERITANCE_BRIDGE"}),
        _row("R6", extra={"debt": "carries INHERITANCE_BRIDGE"},
             ctx={"layer": UNTYPED, "grant": "G5", "carrier": "C1",
                  "note": "voluntary accretion on an untouched row"}),
        _row("R7", tail="new", ctx={"layer": "L1", "grant": "G8",
                                    "carrier": "C5"}),
    ]
    if poison:
        ok_rows[1][CONTEXT_KEY]["layer"] = "L9"  # corrupt the clean set
    files.append(_write(tmp, "conditional-physics-ledger-v0.260.json",
                        _ledger("0.260", ok_rows,
                                predecessor="conditional-physics-ledger-"
                                            "v0.259.json")))
    return files


def _planted(tmp):
    """(label, files, reference) triples that MUST each drive exit 1."""
    base = [_row("R1"), _row("R4", kind="DERIVED"),
            _row("R5", kind="DERIVED_CONDITIONAL"),
            _row("R6", extra={"debt": "carries INHERITANCE_BRIDGE"})]
    pred = _write(tmp, "conditional-physics-ledger-v0.259.json",
                  _ledger("0.259", base))
    pred_name = os.path.basename(pred)

    def one(label, rows):
        name = "conditional-physics-ledger-v0.260.json"
        path = os.path.join(tmp, label)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, name), "w", encoding="utf-8") as fh:
            json.dump(_ledger("0.260", rows, predecessor=pred_name), fh)
        return (label, [pred, os.path.join(path, name)], None)

    good = {"layer": "L1", "grant": "G0", "carrier": "C5"}
    cases = [
        one("missing-context", [_row("R1", tail="moved")]),
        one("layer-out-of-codomain",
            [_row("R1", tail="moved", ctx=dict(good, layer="L9"))]),
        one("carrier-out-of-codomain",
            [_row("R1", tail="moved", ctx=dict(good, carrier="C99"))]),
        one("grant-out-of-codomain",
            [_row("R1", tail="moved", ctx=dict(good, grant="G4"))]),
        one("launder-in-projection",
            [_row("R5", kind="DERIVED_CONDITIONAL", tail="moved",
                  ctx=dict(good, grant="G0"))]),
        one("overclaim-on-derived",
            [_row("R4", kind="DERIVED", tail="moved",
                  ctx=dict(good, grant="G1"))]),
        one("grant-omits-named-condition",
            [_row("R6", tail="moved",
                  extra={"debt": "carries INHERITANCE_BRIDGE"},
                  ctx=dict(good, grant=UNTYPED, note="claims ignorance"))]),
        one("untyped-without-note",
            [_row("R1", tail="moved", ctx=dict(good, layer=UNTYPED))]),
        one("mixed-untyped-slot",
            [_row("R1", tail="moved",
                  ctx=dict(good, layer=["L1", UNTYPED], note="n"))]),
        one("context-not-an-object",
            [_row("R1", tail="moved", ctx="L1")]),
        one("unknown-context-key",
            [_row("R1", tail="moved", ctx=dict(good, bogus=1))]),
        one("empty-slot-array",
            [_row("R1", tail="moved", ctx=dict(good, layer=[]))]),
    ]
    # reference corruptions: the clean ledger set, a broken CT-1
    clean = _clean_fixtures(tmp)
    missing_ref = os.path.join(tmp, "no-such-reference.md")
    cases.append(("reference-missing", clean, missing_ref))
    toothless = os.path.join(tmp, "toothless-reference.md")
    with open(toothless, "w", encoding="utf-8") as fh:
        fh.write(REF_FIXTURE.replace("{GRANT-ACA1-C1}", "grant one")
                 .replace("{INHERITANCE_BRIDGE}", "the bridge"))
    cases.append(("reference-toothless", clean, toothless))
    no_marker = os.path.join(tmp, "no-marker-reference.md")
    with open(no_marker, "w", encoding="utf-8") as fh:
        fh.write(REF_FIXTURE.replace("| M4 | HOMONYM-AMBIGUOUS ", "| M4 | x "))
    cases.append(("reference-lost-marker", clean, no_marker))
    return cases


def selftest(poison=False):
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix="ct2-gate-")
    try:
        ref = os.path.join(tmp, "reference.md")
        with open(ref, "w", encoding="utf-8") as fh:
            fh.write(REF_FIXTURE)

        clean_dir = os.path.join(tmp, "clean")
        os.makedirs(clean_dir, exist_ok=True)
        clean = _clean_fixtures(clean_dir, poison=poison)
        code, stats = audit(paths=clean, reference=ref, verbose=False)
        if code != 0:
            print("SELFTEST: clean baseline does NOT pass (%d red); planted "
                  "facts were NOT run" % stats["red"])
            for line in stats["lines"]:
                if line.startswith("RED"):
                    print("  " + line)
            print("SELFTEST FAILED")
            return 1
        if poison:
            print("SELFTEST: poisoned baseline was accepted as clean -- the "
                  "baseline guard has no power")
            print("SELFTEST FAILED")
            return 1
        print("SELFTEST: clean baseline verified first (%d in scope, "
              "%d out of scope, 0 red)"
              % (stats["scoped"], stats["out_of_scope"]))

        planted_dir = os.path.join(tmp, "planted")
        os.makedirs(planted_dir, exist_ok=True)
        ok = True
        cases = _planted(planted_dir)
        for label, files, ref_override in cases:
            code, st = audit(paths=files,
                             reference=ref_override or ref, verbose=False)
            caught = code == 1 and st["red"] > 0
            print("  planted %-30s %s" % (
                label, "caught (exit 1, %d red)" % st["red"] if caught
                else "MISSED"))
            ok = ok and caught
        print("SELFTEST " + ("GREEN: clean baseline first, then %d/%d planted "
                             "false facts each exit 1" % (len(cases),
                                                          len(cases))
                             if ok else "FAILED"))
        return 0 if ok else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        return selftest(poison="--poison-baseline" in sys.argv)
    return audit()[0]


if __name__ == "__main__":
    sys.exit(main())
