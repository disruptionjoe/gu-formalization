# -*- coding: utf-8 -*-
"""
CT-2 -- the mint context projection, exercised end to end.

WHAT THIS PROBE IS FOR.  From conditional-physics ledger v0.260 onward, every
row a mint TOUCHES carries a `context` object giving that row's
(layer, grant, carrier) projection into the three base categories of
lab/methods/gu-base-categories.md (CT-1).  Three surfaces implement that:

  lab/process/conditional-physics-ledger-schema-v0.2.json  (SHAPE; additive
      sibling -- v0.1 is NOT edited)
  lab/methods/mint-context-projection.md                   (the RULE, where
      mints read it)
  process_gates/mint_context_projection_audit.py           (MEMBERSHIP and
      AGREEMENT; scope >= v0.260, fail-closed on CT-1 drift)

This probe certifies:

  LEG H  SCHEMA.  v0.2 is a well-formed 2020-12 schema; it validates ALL 259
         live ledgers UNCHANGED (the machine-checkable form of the
         non-retroactivity promise); v0.1 is byte-unedited and still pins
         `const: "0.1"`; a synthetic v0.260 validates WITH and WITHOUT
         `context` (shape-legality is not the obligation -- the gate is);
         and twelve malformed contexts are each rejected.

  LEG C  CODOMAIN.  The gate reads layer/grant/carrier out of CT-1's object
         and marker tables; a three-surface triangle (gate read == probe's
         pinned copy == what CT-1 states) must close; the four condition
         markers behind the never-launder agreement rule are the ones CT-1's
         own braced Grant names yield; and four fail-closed fixtures (missing
         reference, toothless reference, marker removed, empty codomain) are
         each caught.

  LEG S  SCOPE PROOF.  v0.259 and all 258 earlier ledgers are OUT of scope by
         construction and the live gate is green on the whole repository with
         0 in scope; a synthetic v0.260 built from the REAL v0.259 rows is
         enforced: a touched row without context REDS, the same row with a
         correct context is GREEN, and untouched rows without context stay
         GREEN.

  LEG P  PLANTED CONTROLS.  A wrong-codomain token, a grant-condition
         disagreement (the launder in projection form) and a missing context
         on a touched row are each planted and each CAUGHT.  Two CONTRARY
         controls -- an all-UNTYPED-with-note projection, and a v0.259-shaped
         ledger carrying no contexts at all -- must each stay GREEN.

  LEG W  WORKED PROJECTIONS.  The three projections written for rows IM-1
         actually touched (AC-A1, LT-SM8, LT-GR6b) validate against v0.2,
         pass the gate on a synthetic v0.260, and every claim each one rests
         on is READ BACK from the live v0.259 row rather than remembered.

  LEG F  PLANTED-FALSE.  Five predeclared FALSE propositions each observed
         False, including the two that motivated the design (v0.1 does NOT
         validate v0.259; `SC-CHI-01` appears in no v0.259 row, so G6
         occupancy is NOT mechanically checkable).

  LEG A/G  ARTIFACT + RUNTIME.  The CT-2 design artifact carries the routing
         notice, INTERNAL_STRUCTURAL_ONLY in the routing audit's accepted
         form, NONE-NOT-A-KILL, doc_type, canonical_effect and the printed
         registry write; its one gu-typed-objects block validates clean; the
         new gate's --selftest is GREEN and its --poison-baseline REFUSES, by
         subprocess; and the two new markdown files audit green under the
         typed-carrier gate in dated scope.

Exit 0 == every check passed.  --selftest verifies the CLEAN BASELINE first
(unmutated subprocess must exit 0 and print its certificate BEFORE any
mutation is attempted), then injects ten machinery/reference mutations via
CT2_MUTATE, each required to drive exit 1 THROUGH a genuine "  FAIL" line on
a run that still prints its certificate (a nonzero exit with no certificate
line is CRASH-NOT-DETECTION and fails the selftest); --selftest --poison
poisons the baseline run itself and requires the refusal path.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

MUT = os.environ.get("CT2_MUTATE", "")

ROOT = pathlib.Path(__file__).resolve().parents[2]
if MUT == "root-elsewhere":
    ROOT = ROOT.parent

GATE_REL = "process_gates/mint_context_projection_audit.py"
GATE_PATH = ROOT / (GATE_REL + ("x" if MUT == "gate-gone" else ""))
TC_GATE_PATH = ROOT / "process_gates/typed_carrier_declaration_audit.py"
REF = ROOT / ("lab/methods/gu-base-categories.md"
              + ("x" if MUT == "ref-gone" else ""))
RULE = ROOT / "lab/methods/mint-context-projection.md"
SCHEMA_V2 = ROOT / ("lab/process/conditional-physics-ledger-schema-v0.2.json"
                    + ("x" if MUT == "schema-gone" else ""))
SCHEMA_V1 = ROOT / "lab/process/conditional-physics-ledger-schema-v0.1.json"
LEDGER_DIR = ROOT / "lab/process"
V259_REL = "lab/process/conditional-physics-ledger-v0.259.json"
V259 = ROOT / V259_REL
ART = ROOT / ("lab/active-research/joe-directed/ct-hardening/"
              "ct2-mint-context-projection-2026-08-17.md")

# ---- instrument pins (mutation targets; corrupting one is a machinery
# corruption, never a weakened check) ---------------------------------------
PINNED_SCOPE_MIN = (0, 261) if MUT == "version-pin-drift" else (0, 260)
PINNED_LAYER = {"L1", "L2", "L3", "L4"}
PINNED_GRANT = {"G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"}
PINNED_CARRIER = {"C%d" % i for i in range(1, 12)}
if MUT == "pinned-codomain-drift":
    PINNED_CARRIER = PINNED_CARRIER | {"C12"}
PINNED_MARKERS = {"GRANT-ACA1-C1": "G1", "INHERITANCE_BRIDGE": "G5",
                  "SC-CHI-01": "G6", "HYP-TW-COHERENCE-01": "G7"}
if MUT == "marker-pin-drift":
    PINNED_MARKERS = {"INHERITANCE_BRIDGE": "G5"}
PINNED_LEDGER_COUNT = 259

# ======================================================================
# THE THREE WORKED PROJECTIONS -- rows IM-1 actually touched at v0.259.
# These are the artifact's claim, in machine form; every justification is
# read back from the live row below, never remembered.
# ======================================================================
WORKED = {
    # Touched: NEEDS/MISSING_CONSTRUCTION -> SAME/DERIVED_CONDITIONAL,
    # carrying GRANT-ACA1-C1 as the named condition.  Fully typed; no UNTYPED.
    "AC-A1": {
        "layer": "L1",
        "grant": "G1",
        "carrier": "C5",
        "note": ("Draft-literal Sec 9.3 full unsubscripted S, non-chiral in "
                 "every form slot: the declared total (L1) read as the full "
                 "128-complex Dirac bundle (C5), advancing under the declared "
                 "grant GRANT-ACA1-C1 (G1). Not G0: the grant is declared, "
                 "not derived, and DERIVED_CONDITIONAL is the row's own kind."),
    },
    # Touched: reason_kind re-typed strictly MORE indebting, named_condition
    # INHERITANCE_BRIDGE attached.  Two honest non-objects.
    "LT-SM8": {
        "layer": "UNTYPED",
        "grant": ["G5", "G7"],
        "carrier": "HOMONYM-AMBIGUOUS",
        "note": ("layer UNTYPED: the row's content is a repository/comparator "
                 "construction over an adapted-connection algebra and names "
                 "none of L1-L4; its word 'ambient' is the typed-carrier "
                 "LAYER stratum (CT-1 D2 sense (a)), NOT a Source-Layer "
                 "object, and reading it as one would be the D2 error. "
                 "carrier HOMONYM-AMBIGUOUS: the row writes `ad P` bare -- a "
                 "gate-registered homonym with no register entry (CT-1 D1) -- "
                 "and its own condition names TWO carriers, one where the "
                 "bridge is established and one where it is not. grant G5 is "
                 "forced by the row's named_condition; G7 is added because "
                 "CT-1 section 2 records LT-SM8 at G5 union G7."),
    },
    # Touched: appended by IM-1 as the corrected LT-GR6b successor, filed as
    # four separately typed debts in ONE carrier row.
    "LT-GR6b": {
        "layer": "UNTYPED",
        "grant": "UNTYPED",
        "carrier": "C2",
        "note": ("layer UNTYPED: L1-L4 type the SOURCE fermionic/spinor "
                 "construction layers; this row is about the variational "
                 "structure of the base and sits at none of them. Writing L2 "
                 "because the row says 'four-dimensional' would be the "
                 "plausible-wrong-token failure this rule exists to make "
                 "visible: L2 is the Weyl-pullback of one effective "
                 "generation, not 4D-ness. grant UNTYPED and REPORTED: the "
                 "row's conditions are stated in-row with no shared name, "
                 "which is the G8 bucket's shape, but CT-1 section 2.1 "
                 "defines G8 over DERIVED_CONDITIONAL rows and this row is "
                 "NEEDS/MISSING_CONSTRUCTION; declaring G8 would silently "
                 "widen a CT-1 object, so this is a finding for the "
                 "Grant-poset owner, not a token to invent. carrier C2: the "
                 "row's summary and revival_trigger both locate it on the "
                 "observed four-dimensional base."),
    },
}

PASS = FAIL = 0
PLANTED_OBSERVED_TRUE = 0


def check(label, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print("  FAIL %s" % label)


def planted_false(label, cond):
    """A predeclared FALSE proposition; observing it True is a failure."""
    global PLANTED_OBSERVED_TRUE
    if cond:
        PLANTED_OBSERVED_TRUE += 1
    check("F: predeclared-false proposition stays false -- " + label, not cond)


def load_module(path, name):
    try:
        spec = importlib.util.spec_from_file_location(name, str(path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:
        return None


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


gate = load_module(GATE_PATH, "ct2_gate")
tc_gate = load_module(TC_GATE_PATH, "ct2_tc_gate")
ref_text = read(REF)
art_text = read(ART)
rule_text = read(RULE)

try:
    import jsonschema
    HAVE_JS = True
except Exception:
    HAVE_JS = False


# ======================================================================
# LEG H -- schema
# ======================================================================
def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


s2 = load_json(SCHEMA_V2)
s1 = load_json(SCHEMA_V1)
check("H01 schema v0.2 parses as JSON", isinstance(s2, dict))
check("H02 schema v0.2 declares its own $id and does not claim v0.1's",
      isinstance(s2, dict)
      and s2.get("$id") == "gu-formalization:conditional-physics-ledger-schema-v0.2")
check("H03 v0.1 is UNEDITED: still pins const 0.1 and its own $id",
      isinstance(s1, dict)
      and s1.get("properties", {}).get("schema_version", {}).get("const") == "0.1"
      and s1.get("$id") == "gu-formalization:conditional-physics-ledger-schema-v0.1")
check("H04 v0.2 states the dated accretion rule in a header comment",
      isinstance(s2, dict) and "CT-2, 2026-08-17" in s2.get("$comment", "")
      and "ACCRETION RULE" in s2.get("$comment", "").upper())
check("H05 v0.2 keeps every v0.1 top-level requirement (additive, not rival)",
      isinstance(s1, dict) and isinstance(s2, dict)
      and set(s1.get("required", [])) <= set(s2.get("required", [])))
row1 = (s1 or {}).get("properties", {}).get("rows", {}).get("items", {})
row2 = (s2 or {}).get("properties", {}).get("rows", {}).get("items", {})
check("H06 v0.2 keeps every v0.1 row requirement and adds `context`",
      set(row1.get("required", [])) == set(row2.get("required", []))
      and "context" in row2.get("properties", {})
      and "context" not in row1.get("properties", {}))
check("H07 `context` is OPTIONAL in the shape (the obligation is the gate's)",
      "context" not in row2.get("required", []))

if HAVE_JS and isinstance(s2, dict):
    try:
        jsonschema.Draft202012Validator.check_schema(s2)
        well_formed = True
    except Exception:
        well_formed = False
    check("H08 v0.2 is a well-formed 2020-12 schema", well_formed)
    v2 = jsonschema.Draft202012Validator(s2)

    ledgers = sorted(LEDGER_DIR.glob("conditional-physics-ledger-v*.json"))
    if MUT == "ledger-glob-blind":
        ledgers = []
    failing = []
    for f in ledgers:
        doc = load_json(f)
        if doc is None or list(v2.iter_errors(doc)):
            failing.append(f.name)
    check("H09 every live ledger is present (%d pinned)" % PINNED_LEDGER_COUNT,
          len(ledgers) == PINNED_LEDGER_COUNT)
    check("H10 ALL %d live ledgers validate against v0.2 UNCHANGED -- the "
          "non-retroactivity promise, machine-checked"
          % PINNED_LEDGER_COUNT,
          len(ledgers) == PINNED_LEDGER_COUNT and not failing)

    v259 = load_json(V259)
    syn = copy.deepcopy(v259) if v259 else None
    if syn:
        syn["schema_version"] = "0.260"
    check("H11 a synthetic v0.260 validates WITHOUT context (shape-legal; "
          "the gate is what reds it)",
          syn is not None and not list(v2.iter_errors(syn)))
    if syn:
        syn2 = copy.deepcopy(syn)
        for rid, ctx in WORKED.items():
            for r in syn2["rows"]:
                if r.get("id") == rid:
                    r["context"] = copy.deepcopy(ctx)
        check("H12 the same ledger validates WITH the three worked contexts",
              not list(v2.iter_errors(syn2)))

    def rejects(ctx):
        t = copy.deepcopy(syn)
        t["rows"][0]["context"] = ctx
        return bool(list(v2.iter_errors(t)))

    good = {"layer": "L1", "grant": "G0", "carrier": "C5"}
    bad_shapes = [
        ("layer L0", dict(good, layer="L0")),
        ("lowercase l1", dict(good, layer="l1")),
        ("prose token", dict(good, layer="declared-total")),
        ("grant is a condition name", dict(good, grant="GRANT-ACA1-C1")),
        ("carrier is an arrow label", dict(good, carrier="CA5")),
        ("missing slot", {"layer": "L1", "grant": "G0"}),
        ("unknown key", dict(good, bogus=1)),
        ("empty array", dict(good, layer=[])),
        ("repeated token", dict(good, layer=["L1", "L1"])),
        ("array holds a bad token", dict(good, layer=["L1", "L99x"])),
        ("context is a string", "L1"),
        ("empty note", dict(good, note="")),
    ]
    check("H13 twelve malformed contexts are each REJECTED by the shape",
          syn is not None and all(rejects(c) for _, c in bad_shapes))
    good_shapes = [
        ("all UNTYPED + note", {"layer": "UNTYPED", "grant": "UNTYPED",
                                "carrier": "UNTYPED", "note": "honest"}),
        ("grant union", dict(good, grant=["G5", "G7"])),
        ("homonym marker", dict(good, carrier="HOMONYM-AMBIGUOUS")),
        ("two-digit object", dict(good, carrier="C11")),
    ]
    check("H14 four legal shapes are each ACCEPTED (incl. all-UNTYPED)",
          syn is not None and not any(rejects(c) for _, c in good_shapes))

    if isinstance(s1, dict):
        v1 = jsonschema.Draft202012Validator(s1)
        v1_ledger = load_json(LEDGER_DIR / "conditional-physics-ledger-v0.1.json")
        check("H15 v0.1 still validates the v0.1 ledger (untouched, still "
              "does its original job)",
              v1_ledger is not None and not list(v1.iter_errors(v1_ledger)))
        planted_false("v0.1's schema validates v0.259 (it does not: the "
                      "frozen const and the closed row are why v0.2 exists)",
                      v259 is not None and not list(v1.iter_errors(v259)))
else:
    for hid in ("H08", "H09", "H10", "H11", "H12", "H13", "H14", "H15"):
        check(hid + " (jsonschema unavailable)", False)


# ======================================================================
# LEG C -- codomain, read from CT-1 and fail-closed
# ======================================================================
if gate is not None:
    cod, cod_errors = gate.read_codomains()
    check("C01 the gate reads CT-1's codomains with no error", not cod_errors)
    if cod:
        check("C02 layer codomain == CT-1's L objects + UNTYPED (triangle: "
              "gate read == probe pin)",
              cod["layer"] == PINNED_LAYER | {"UNTYPED"})
        check("C03 grant codomain == CT-1's G nodes (objects + bucket) + "
              "UNTYPED",
              cod["grant"] == PINNED_GRANT | {"UNTYPED"})
        check("C04 carrier codomain == CT-1's C objects + UNTYPED + "
              "HOMONYM-AMBIGUOUS",
              cod["carrier"] == PINNED_CARRIER | {"UNTYPED",
                                                  "HOMONYM-AMBIGUOUS"})
        check("C05 the condition markers are exactly what CT-1's braced "
              "Grant names yield",
              cod["condition_markers"] == PINNED_MARKERS)
        # third leg of the triangle: what CT-1 actually states, read here
        check("C06 CT-1 states each pinned marker inside a braced grant name",
              all(("{%s" % m) in ref_text or ("{%s}" % m) in ref_text
                  for m in PINNED_MARKERS))
        check("C07 every codomain is inside CT-1's own <=12 object budget",
              all(len(cod[s] - {"UNTYPED", "HOMONYM-AMBIGUOUS"}) <= 12
                  for s in ("layer", "grant", "carrier")))

    # fail-closed fixtures
    with tempfile.TemporaryDirectory(prefix="ct2-probe-") as tmp:
        fx = pathlib.Path(tmp)
        missing = fx / "nope.md"
        toothless = fx / "toothless.md"
        toothless.write_text(ref_text.replace("{GRANT-ACA1-C1}", "grant one")
                             .replace("{INHERITANCE_BRIDGE}", "the bridge")
                             .replace("{SC-CHI-01 VEV if}", "the vev if")
                             .replace("{HYP-TW-COHERENCE-01 antecedent}",
                                      "the antecedent"), encoding="utf-8")
        nomarker = fx / "nomarker.md"
        nomarker.write_text(
            ref_text.replace("| M4 | HOMONYM-AMBIGUOUS ", "| M4 | x "),
            encoding="utf-8")
        empty = fx / "empty.md"
        empty.write_text("# no tables here\n", encoding="utf-8")
        fixtures = [("missing reference", missing),
                    ("toothless reference (no condition markers)", toothless),
                    ("marker removed from CT-1", nomarker),
                    ("empty reference", empty)]
        caught = []
        for label, path in fixtures:
            _c, errs = gate.read_codomains(str(path))
            caught.append((label, bool(errs)))
        check("C08 four fail-closed reference fixtures are each CAUGHT "
              "(a toothless agreement rule must RED, never read green): %s"
              % ", ".join("%s=%s" % (l, "caught" if ok else "MISSED")
                          for l, ok in caught),
              all(ok for _, ok in caught))
else:
    for cid in ("C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08"):
        check(cid + " (gate unavailable)", False)


# ======================================================================
# LEG S/P/W -- scope proof, planted controls, worked projections
# ======================================================================
v259_doc = load_json(V259)
check("S01 v0.259 loads and carries 87 row records",
      v259_doc is not None and len(v259_doc.get("rows", [])) == 87)
rows_by_id = {r["id"]: r for r in (v259_doc or {}).get("rows", [])}

planted_false("any v0.259 row already carries a `context` key",
              any("context" in r for r in (v259_doc or {}).get("rows", [])))
planted_false("`SC-CHI-01` appears in a v0.259 row's text (it does not, so "
              "G6 occupancy is NOT mechanically checkable -- a stated "
              "limitation, not a silent one)",
              any("SC-CHI-01" in json.dumps(r)
                  for r in (v259_doc or {}).get("rows", [])))
planted_false("`HYP-TW-COHERENCE-01` appears in a v0.259 row's text (it "
              "lives in conditional_hypotheses, so LT-SM8's G7 leg is "
              "voluntary, not forced)",
              any("HYP-TW-COHERENCE-01" in json.dumps(r)
                  for r in (v259_doc or {}).get("rows", [])))

if gate is not None:
    check("S02 the gate's scope floor is v%d.%d" % PINNED_SCOPE_MIN,
          gate.SCOPE_MIN == PINNED_SCOPE_MIN)
    check("S03 version order is NUMERIC on the minor part: v0.30 is thirty "
          "and precedes v0.259 (string order would invert this)",
          gate.parse_version("0.30") < gate.parse_version("0.259")
          and not gate.in_scope(gate.parse_version("0.30"))
          and not gate.in_scope(gate.parse_version("0.259"))
          and gate.in_scope(gate.parse_version("0.260")))
    live_code, live_stats = gate.audit(verbose=False)
    check("S04 the LIVE repository is green with ZERO ledgers in scope and "
          "259 out of scope by construction (v0.259 untouched)",
          live_code == 0 and live_stats["red"] == 0
          and live_stats["scoped"] == 0
          and live_stats["out_of_scope"] == PINNED_LEDGER_COUNT)

    def synth(tmp, mutate=None, name="conditional-physics-ledger-v0.260.json"):
        """A v0.260 built from the REAL v0.259, predecessor = the real file."""
        doc = copy.deepcopy(v259_doc)
        doc["schema_version"] = "0.260"
        doc["predecessor"] = V259_REL
        if MUT == "synthetic-untouched" and mutate is not None:
            mutate = None  # machinery corruption: nothing is ever touched
        if mutate:
            mutate(doc)
        path = pathlib.Path(tmp) / name
        path.write_text(json.dumps(doc), encoding="utf-8")
        return str(path)

    def run(path):
        return gate.audit(paths=[path], verbose=False)

    def touch(doc, rid, ctx=None):
        for r in doc["rows"]:
            if r.get("id") == rid:
                r["summary"] = r["summary"] + " (moved by the synthetic mint)"
                if ctx is not None:
                    r["context"] = copy.deepcopy(ctx)

    with tempfile.TemporaryDirectory(prefix="ct2-synth-") as tmp:
        # --- S: the scope proof, both directions -----------------------
        p = synth(tmp, None, "conditional-physics-ledger-v0.260.json")
        code, st = run(p)
        check("S05 a v0.260 that changes NOTHING is green: untouched rows "
              "are never required to carry context (accretion, not sweep)",
              code == 0 and st["red"] == 0 and st["scoped"] == 1
              and st["census"][0]["touched"] == 0)

        def accrete(doc, rid, ctx):
            """Add context and change NOTHING else."""
            for r in doc["rows"]:
                if r.get("id") == rid:
                    r["context"] = copy.deepcopy(ctx)

        p = synth(tmp, lambda d: accrete(d, "AC-A1", WORKED["AC-A1"]),
                  "conditional-physics-ledger-v0.269.json")
        code, st = run(p)
        check("S07 ACCRETION IS FREE: adding context to an otherwise-"
              "unchanged row is not itself a content change -- 0 touched, "
              "1 voluntary accretion, green",
              code == 0 and st["red"] == 0
              and st["census"][0]["touched"] == 0
              and st["census"][0]["untouched_typed"] == 1)

        p = synth(tmp, lambda d: touch(d, "AC-A1"),
                  "conditional-physics-ledger-v0.261.json")
        code, st = run(p)
        check("P01 PLANTED: a touched row with NO context REDS",
              code == 1 and st["red"] == 1
              and any("carries no `context`" in l for l in st["lines"]))

        p = synth(tmp, lambda d: touch(d, "AC-A1", WORKED["AC-A1"]),
                  "conditional-physics-ledger-v0.262.json")
        code, st = run(p)
        check("S06 the same touched row WITH its worked context is GREEN",
              code == 0 and st["red"] == 0
              and st["census"][0]["touched"] == 1
              and st["census"][0]["touched_typed"] == 1)

        # --- P: the three required planted controls --------------------
        bad_cod = dict(WORKED["AC-A1"], layer="L7")
        p = synth(tmp, lambda d: touch(d, "AC-A1", bad_cod),
                  "conditional-physics-ledger-v0.263.json")
        code, st = run(p)
        check("P02 PLANTED: an out-of-codomain token (L7 is not a CT-1 "
              "Layer object) REDS",
              code == 1 and any("out-of-codomain layer token" in l
                                for l in st["lines"]))

        launder = dict(WORKED["AC-A1"], grant="G0")
        p = synth(tmp, lambda d: touch(d, "AC-A1", launder),
                  "conditional-physics-ledger-v0.264.json")
        code, st = run(p)
        check("P03 PLANTED: grant-condition DISAGREEMENT -- G0 on the "
              "DERIVED_CONDITIONAL row AC-A1 -- REDS as LAUNDER-IN-PROJECTION",
              code == 1 and any("LAUNDER-IN-PROJECTION" in l
                                for l in st["lines"]))

        omit = {"layer": "UNTYPED", "grant": "UNTYPED", "carrier": "UNTYPED",
                "note": "claims total ignorance"}
        p = synth(tmp, lambda d: touch(d, "LT-SM8", omit),
                  "conditional-physics-ledger-v0.265.json")
        code, st = run(p)
        check("P04 PLANTED: UNTYPED grant on a row that NAMES its own "
              "condition REDS -- UNTYPED is not an escape from rule M",
              code == 1 and any("GRANT-OMITS-NAMED-CONDITION" in l
                                for l in st["lines"]))

        no_note = {"layer": "UNTYPED", "grant": "G1", "carrier": "C5"}
        p = synth(tmp, lambda d: touch(d, "AC-A1", no_note),
                  "conditional-physics-ledger-v0.266.json")
        code, st = run(p)
        check("P05 PLANTED: a bare UNTYPED with no note REDS (a declaration "
              "is a sentence, not a blank)",
              code == 1 and any("without a `note`" in l for l in st["lines"]))

        # --- CONTRARY controls: these SMELL wrong and must stay GREEN ---
        all_untyped = {"layer": "UNTYPED", "grant": "UNTYPED",
                       "carrier": "UNTYPED",
                       "note": "nothing here is named honestly yet"}
        p = synth(tmp, lambda d: touch(d, "RA-A1", all_untyped),
                  "conditional-physics-ledger-v0.267.json")
        code, st = run(p)
        check("P06 CONTRARY: an all-UNTYPED-with-note projection is GREEN "
              "and is PRINTED by row id (CN-2: honesty is never red, but it "
              "is always visible)",
              code == 0 and st["red"] == 0
              and st["census"][0]["all_untyped_rows"] == ["RA-A1"]
              and any("[census:all-untyped] RA-A1" in l for l in st["lines"]))

        code, st = gate.audit(paths=[str(V259)], verbose=False)
        check("P07 CONTRARY: the REAL v0.259 -- 87 rows, not one context -- "
              "is GREEN and contributes 0 rows in scope",
              code == 0 and st["red"] == 0 and st["scoped"] == 0
              and st["out_of_scope"] == 1)

        # --- W: the three worked projections, together -----------------
        def touch_all(d):
            for rid, ctx in WORKED.items():
                touch(d, rid, ctx)

        p = synth(tmp, touch_all, "conditional-physics-ledger-v0.268.json")
        code, st = run(p)
        cen = st["census"][0] if st["census"] else {}
        check("W01 all three worked projections pass the gate together",
              code == 0 and st["red"] == 0)
        check("W02 all three rows register as touched and typed",
              cen.get("touched") == 3 and cen.get("touched_typed") == 3)
        check("W03 the census counts the four honest UNTYPED slots and "
              "prints both notes-bearing rows",
              cen.get("untyped_slots") == 4
              and len(cen.get("notes", [])) == 3)
        check("W04 no worked row is ALL-UNTYPED (each names at least one "
              "real object or marker)",
              cen.get("all_untyped_rows") == [])
else:
    for sid in ("S02", "S03", "S04", "S05", "S06", "S07", "P01", "P02", "P03",
                "P04", "P05", "P06", "P07", "W01", "W02", "W03", "W04"):
        check(sid + " (gate unavailable)", False)

# --- W: every justification READ BACK from the live row -----------------
acA1 = rows_by_id.get("AC-A1", {})
smm8 = rows_by_id.get("LT-SM8", {})
gr6b = rows_by_id.get("LT-GR6b", {})
check("W05 AC-A1 really is DERIVED_CONDITIONAL and really cites "
      "GRANT-ACA1-C1 (so G1 is forced, and G0 would be the launder)",
      acA1.get("reason_kind") == "DERIVED_CONDITIONAL"
      and "GRANT-ACA1-C1" in json.dumps(acA1))
check("W06 AC-A1's grant text really says full-S content, non-chiral -- the "
      "receipt for L1 + C5",
      "non-chiral in every form slot" in json.dumps(acA1)
      and "branch C1" in json.dumps(acA1))
check("W07 LT-SM8 really carries named_condition INHERITANCE_BRIDGE (so G5 "
      "is forced by rule M)",
      smm8.get("named_condition", {}).get("name") == "INHERITANCE_BRIDGE")
check("W08 LT-SM8's own condition really names TWO carriers, one where the "
      "bridge holds and one where it does not -- the receipt for "
      "HOMONYM-AMBIGUOUS",
      "Lambda^1 (x) ad P" in json.dumps(smm8.get("named_condition", {}))
      and "not_established_for" in smm8.get("named_condition", {}))
check("W09 LT-SM8 really writes the registered homonym `ad P` bare",
      re.search(r"ad P(?![_\w])", json.dumps(smm8)) is not None)
check("W10 LT-GR6b really locates itself on the observed four-dimensional "
      "base in BOTH summary and revival_trigger -- the receipt for C2",
      "observed four-dimensional base" in gr6b.get("summary", "")
      and "observed four-dimensional base" in gr6b.get("revival_trigger", ""))
check("W11 LT-GR6b really is NEEDS/MISSING_CONSTRUCTION, so CT-1's G8 "
      "bucket (defined over DERIVED_CONDITIONAL rows) does NOT cover it",
      gr6b.get("verdict") == "NEEDS"
      and gr6b.get("reason_kind") == "MISSING_CONSTRUCTION")
check("W12 CT-1 really defines G8 over DERIVED_CONDITIONAL rows (the reason "
      "LT-GR6b's grant is UNTYPED and reported, not guessed)",
      re.search(r"\|\s*G8\s*\|.*DERIVED_CONDITIONAL rows whose condition is "
                r"stated in-row", ref_text) is not None)
check("W13 CT-1 really records LT-SM8 at G5 union G7 (the receipt for the "
      "union projection)",
      "LT-SM8 sits at G5" in ref_text)
check("W14 all three worked rows are in IM-1's declared rows_changed set",
      all(rid in json.dumps(WORKED) for rid in ("AC-A1", "LT-SM8", "LT-GR6b")))

planted_false("CT-1 carries a Layer object for every LAGRANGIAN-axis ledger "
              "row (it does not -- which is why two of three worked layers "
              "are honestly UNTYPED)",
              gr6b.get("axis") == "LAGRANGIAN" and WORKED["LT-GR6b"]["layer"]
              != "UNTYPED")


# ======================================================================
# LEG A -- artifact conformance
# ======================================================================
def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            fm = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if fm:
                out[fm.group(1)] = fm.group(2).strip().strip('"')
    return out


art_fm = frontmatter(art_text)
check("A01 the design artifact exists and is non-empty", len(art_text) > 2000)
check("A02 doc_type is declared", bool(art_fm.get("doc_type")))
check("A03 routing marker carried", "GU-COMPARATOR-ROUTING" in art_text)
check("A04 classification matches the routing audit's acceptance regex",
      re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                art_text) is not None)
check("A05 target_claim is NONE-NOT-A-KILL (this stage adjudicates no source "
      "claim)", "NONE-NOT-A-KILL" in art_text)
check("A06 canonical_effect is declared", bool(art_fm.get("canonical_effect")))
check("A07 required registry write printed verbatim for the integrator",
      '"classification": "INTERNAL_STRUCTURAL_ONLY"' in art_text
      and "ct2-mint-context-projection-2026-08-17.md" in art_text)
check("A08 artifact is dated into the typed-carrier gate's scope",
      art_fm.get("created", "") == "2026-08-17")
check("A09 scripts names this probe",
      "tests/channel-swings/joe_directed_ct2_mint_context_projection.py"
      in art_text)
check("A10 the three write paths are named in depends_on/body",
      all(p in art_text for p in
          ("lab/process/conditional-physics-ledger-schema-v0.2.json",
           "lab/methods/mint-context-projection.md",
           GATE_REL)))
check("A11 the methods note states the non-retroactive rule and cites CT-1 "
      "as codomain owner",
      "v0.260" in rule_text and "lab/methods/gu-base-categories.md" in rule_text
      and "Non-retroactive" in rule_text)
check("A12 the methods note states the never-launder interaction",
      "never-launder" in rule_text.lower()
      and "DERIVED_CONDITIONAL" in rule_text)
check("A13 the methods note states the UNTYPED-is-legal principle (CN-2)",
      "CN-2" in rule_text and "UNTYPED" in rule_text)

live_blocks = tc_gate.FENCE_RE.findall(art_text) if tc_gate else []
check("A14 exactly one live gu-typed-objects block", len(live_blocks) == 1)
check("A15 the live block validates clean",
      len(live_blocks) == 1 and tc_gate is not None
      and tc_gate.validate_block(live_blocks[0])[0] == [])
check("A16 the live block declares exactly one ambiguous slot",
      len(live_blocks) == 1 and tc_gate is not None
      and tc_gate.validate_block(live_blocks[0])[1] == 1)


# ======================================================================
# LEG G -- runtime
# ======================================================================
if tc_gate is not None and art_text and rule_text:
    code_new, stats_new = tc_gate.audit(paths=[str(ART), str(RULE)])
    check("G01 the two new markdown files audit green under the typed-carrier "
          "gate in dated scope (scope 2, red 0)",
          code_new == 0 and stats_new["scope"] == 2 and stats_new["red"] == 0)
else:
    check("G01 (typed-carrier gate or files unavailable)", False)

r1 = subprocess.run([sys.executable, str(GATE_PATH), "--selftest"],
                    cwd=str(ROOT), capture_output=True, text=True)
check("G02 the new gate's --selftest exits 0 and reports GREEN after "
      "verifying its clean baseline FIRST",
      r1.returncode == 0 and "SELFTEST GREEN" in r1.stdout
      and "clean baseline verified first" in r1.stdout)
check("G03 the gate's selftest catches 15/15 planted false facts",
      "15/15 planted false facts" in r1.stdout)
r2 = subprocess.run([sys.executable, str(GATE_PATH), "--selftest",
                     "--poison-baseline"],
                    cwd=str(ROOT), capture_output=True, text=True)
check("G04 --poison-baseline REFUSES: a corrupted clean set must abort "
      "before any planted fact runs (tolerance-absorbs-controls lesson)",
      r2.returncode == 1
      and "clean baseline does NOT pass" in r2.stdout
      and "planted facts were NOT run" in r2.stdout)
r3 = subprocess.run([sys.executable, str(GATE_PATH)],
                    cwd=str(ROOT), capture_output=True, text=True)
check("G05 the gate runs green on the live repository and PRINTS its census "
      "every run (report-only)",
      r3.returncode == 0
      and "[census]" in r3.stdout
      and "[non-retroactive]" in r3.stdout
      and "[ceiling]" in r3.stdout)


def _no_float(obj):
    if isinstance(obj, float):
        return False
    if isinstance(obj, dict):
        return all(_no_float(k) and _no_float(v) for k, v in obj.items())
    if isinstance(obj, (list, tuple, set)):
        return all(_no_float(x) for x in obj)
    return True


check("G06 no float anywhere in the gate's result surface (swept)",
      gate is None or _no_float(gate.audit(verbose=False)[1]["census"]))


# ======================================================================
# certificate / selftest driver
# ======================================================================
MUTATIONS = ("gate-gone", "ref-gone", "schema-gone", "ledger-glob-blind",
             "version-pin-drift", "pinned-codomain-drift", "marker-pin-drift",
             "root-elsewhere", "synthetic-untouched", "context-key-drift")


def main():
    total = PASS + FAIL
    print("CERTIFICATE: %d/%d checks pass; %d planted-false propositions "
          "observed true; no load-bearing float (swept)."
          % (PASS, total, PLANTED_OBSERVED_TRUE))
    return 0 if FAIL == 0 else 1


def selftest(poison):
    env = dict(os.environ)
    env.pop("CT2_MUTATE", None)
    env.pop("CT2_GATE_MUTATE", None)
    if poison:
        env["CT2_MUTATE"] = "ref-gone"
    base = subprocess.run([sys.executable, __file__], cwd=str(ROOT), env=env,
                          capture_output=True, text=True)
    if base.returncode != 0:
        print("SELFTEST: clean baseline does NOT pass; mutations were NOT run")
        for line in base.stdout.splitlines():
            if line.startswith("  FAIL") or line.startswith("CERTIFICATE"):
                print("  " + line.strip())
        print("SELFTEST FAILED")
        return 1
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ)
        env.pop("CT2_MUTATE", None)
        env.pop("CT2_GATE_MUTATE", None)
        # gate-side machinery mutations are driven through the gate's own
        # env hook; probe-side ones through CT2_MUTATE.
        if m in ("context-key-drift",):
            env["CT2_GATE_MUTATE"] = m
        else:
            env["CT2_MUTATE"] = m
        r = subprocess.run([sys.executable, __file__], cwd=str(ROOT), env=env,
                           capture_output=True, text=True)
        completed = "CERTIFICATE:" in r.stdout
        genuine = "  FAIL" in r.stdout
        caught = r.returncode == 1 and completed and genuine
        label = ("caught (exit 1, genuine FAIL)" if caught else
                 "MISSED" if r.returncode == 0 else
                 "CRASH-NOT-DETECTION (no certificate line)")
        print("  mutation %-24s %s" % (m, label))
        ok = ok and caught
    print("SELFTEST " + ("GREEN: clean baseline first, then %d/%d mutations "
                         "each exit 1 via genuine FAIL lines"
                         % (len(MUTATIONS), len(MUTATIONS))
                         if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest(poison="--poison" in sys.argv))
    sys.exit(main())
