# -*- coding: utf-8 -*-
"""
CT-1 -- the base-category reference, exercised end to end.

WHAT THIS PROBE IS FOR.  lab/methods/gu-base-categories.md is the canonical
statement of the three context categories the repository already used in
prose everywhere and had written down nowhere: the Source-Layer category
(4 objects), the Grant poset (8 objects + 1 bucket, from the v0.259
conditional-physics ledger), and the Carrier category (11 objects, 4
markers, 11 MAP-TYPE arrow classes + 2 non-arrow tokens).  The typed-carrier
gate (process_gates/typed_carrier_declaration_audit.py) cross-checks its
LAYER= and MAP-TYPE= token constants against the reference's
gu-token-codomain block on every run.  This probe certifies:

  LEG P  PARSE.  The reference's object/arrow tables parse mechanically
         (fixed schemas, unique IDs, role vocabulary), the object counts are
         exactly 4 / 8 / 11 with the <= 12 budget enforced per category, the
         named non-arrows and the codomain block are present, and no
         object-name cell is a bare registered homonym token.

  LEG R  RECEIPTS.  Every repository path cited in any table resolves to an
         existing file (exact count pinned).

  LEG C  CODOMAIN.  The gate's drift check is green against the live
         reference; the reference's token lines equal the gate's constants
         AND the probe's own pinned copies (a three-surface triangle); five
         planted drift fixtures (missing token, extra token, no block,
         missing file, duplicate token) are each caught; a CONTRARY control
         (reordered tokens -- smells wrong, set-equal) must pass.

  LEG S  SOURCES.  49 exact substrings are read from the owning files, not
         remembered: the four-layer sentence (ST-1), different-layers-not-
         competing-quotations (IV-20260815), the contraction correction
         (VZ-4/canon/routing method), the four-corner declaration (CR-B),
         SC-GEN-55/56 and SC-CHI-01 verbatims plus the p.52 varpi hedge, the
         no-GUT / 2+1-imposter / KK-disavowal transcript sentences, SG4 bit
         2, the never-launder pins (IM-1 + v0.259), the grant/condition/
         migration/taxonomy strings, and the register's so(1,3) entry.

  LEG F  PLANTED-FALSE.  Five predeclared FALSE propositions each observed
         False (a category over 12; a bare-token object name; a dangling
         receipt; gate-reference drift; a recorded G3=G6 identification).

  LEG D  DETECTOR POWER.  Absence checks on a clean corpus prove nothing
         unless the detector fires on a synthetic positive (VERIFICATION.md
         rule 4): a 13-object fixture, a dangling-receipt fixture and a
         bare-homonym-name fixture are each planted and each DETECTED.

  LEG A/G  ARTIFACT + RUNTIME.  The CT-1 design artifact carries the routing
         notice, INTERNAL_STRUCTURAL_ONLY in the routing audit's accepted
         form, NONE-NOT-A-KILL, the printed registry write, and exactly one
         live gu-typed-objects block validating clean with exactly one
         declared-ambiguous slot; the edited gate's --selftest is GREEN by
         subprocess; the two new markdown files audit green in dated scope;
         the live repo scan is PRINTED as a dated reconciliation and
         asserted red==0 only under --strict (shared-checkout rule).

Exit 0 == every check passed.  --selftest verifies the CLEAN BASELINE first
(unmutated subprocess must exit 0 and print its certificate BEFORE any
mutation is attempted), then injects ten machinery/reference mutations via
CT1_MUTATE, each required to drive exit 1 THROUGH a genuine "  FAIL" line on
a run that still prints its certificate (a crash without a certificate line
is CRASH-NOT-DETECTION and fails the selftest); --selftest --poison poisons
the baseline run itself and requires the refusal path.
"""

from __future__ import annotations

import importlib.util
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
REF = ROOT / "lab" / "methods" / "gu-base-categories.md"
GATE_PATH = ROOT / "process_gates" / "typed_carrier_declaration_audit.py"
ART = ROOT / ("lab/active-research/joe-directed/ct-hardening/"
              "ct1-base-categories-2026-08-17.md")

# ---- instrument constants (mutation targets; corrupting any of these is a
# machinery/reference corruption, never a weakened check) -------------------
OBJ_ROW_RE = re.compile(
    r"^\|\s*([LGM]\d+|C(?:A)?\d+)\s*\|\s*([^|]+?)\s*\|\s*([a-z-]+)\s*\|"
    r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", re.M)
ARROW_ROW_RE = re.compile(
    r"^\|\s*([LG]A\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
    r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", re.M)
NONARROW_ROW_RE = re.compile(
    r"^\|\s*(N\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$",
    re.M)
CODOMAIN_RE = re.compile(r"^```gu-token-codomain[ \t]*\n(.*?)^```",
                         re.M | re.S)
PATH_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|py|yaml|json)")
MAX_OBJECTS = 12
EXPECTED_LAYER = ("ambient", "observed", "source-print", "toy", "UNTYPED")
EXPECTED_MAP = ("projection", "contraction", "inclusion", "restriction",
                "pullback", "pushforward", "quotient", "isomorphism",
                "homomorphism", "intertwiner", "evaluation", "not-a-map",
                "UNTYPED")
REGISTERED_BARE = ("so(1,3)", "so(3,1)", "ad(P_H)")

# (id, repo-relative path, whitespace-normalize?, exact substring)
QUOTES = [
 ("S01", "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", 1,
  "four layers (declared total / pullback / ± package / observed-VEV-conditional)"),
 ("S02", "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", 1,
  "crediting the total theory with chirality or the package with an unconditional spectrum"),
 ("S03", "lab/active-research/joe-directed/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md", 1,
  "Those are different layers, not competing quotations."),
 ("S04", "lab/active-research/joe-directed/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md", 1,
  "Observation pullback is contraction along the section."),
 ("S05", "lab/active-research/joe-directed/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md", 1,
  "The repair therefore withdraws the global statement"),
 ("S06", "lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md", 0,
  "REDUCTION-FIDELITY"),
 ("S07", "lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md", 1,
  "neither determines nor is determined by"),
 ("S08", "canon/no-go-class-relative-map.md", 0,
  "CORRECTION IV-20260815 / VZ4-01"),
 ("S09", "canon/no-go-class-relative-map.md", 1,
  "restricts canonically for every section"),
 ("S10", "lab/methods/source-native-comparator-routing.md", 1,
  "contraction, not a projection"),
 ("S11", "lab/methods/source-native-comparator-routing.md", 1,
  "not to scalars"),
 ("S12", "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md", 1,
  "printed as FOUR graded corners"),
 ("S13", "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md", 1,
  "The source declares all three layers"),
 ("S14", "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md", 1,
  "class-homogeneous halves"),
 ("S15", "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md", 1,
  "package-to-three claim"),
 ("S16", "lab/sources/source-claim-register.yaml", 1,
  "one generation of standard model fermions is just the pullback of a Weyl spinor Properly understood"),
 ("S17", "lab/sources/source-claim-register.yaml", 1,
  "you're gonna get three generations of standard model fermions"),
 ("S18", "lab/sources/source-claim-register.yaml", 1,
  "splits at the emergent level into two separate chiral theories"),
 ("S19", "lab/sources/source-claim-register.yaml", 1,
  "pulling the various sub-fields of varpi"),
 ("S20", "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 1,
  "no vacuum expectation value pulling the various"),
 ("S21", "papers/drafts/Transcript into the impossible.md", 0,
  "There is no grand unification. It's just a normal bundle in your ambient space."),
 ("S22", "papers/drafts/Transcript into the impossible.md", 0,
  "really two plus one. The third family is an imposter for representation theoretic reasons"),
 ("S23", "papers/drafts/Transcript into the impossible.md", 0,
  "It's not Kaluza Klein. The space that is four dimensional births its own 14 dimensional ambient space."),
 ("S24", "papers/drafts/Transcript into the impossible.md", 0,
  "exactly three families of chiral fermions if you have a decreased VEV"),
 ("S25", "canon/gu-forces-field-space-declaration-RESULTS.md", 0,
  "chiral/unbroken vs massive/super-Higgs"),
 ("S26", "canon/escape-corners-campaign-RESULTS.md", 0,
  "REFUTED-AS-FILED"),
 ("S27", "lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md", 0,
  "INTERSECT IN ZERO"),
 ("S28", "lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md", 0,
  "dim 16384"),
 ("S29", "lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md", 0,
  "dim 91"),
 ("S30", "lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md", 1,
  "differ by an internal rotation"),
 ("S31", "lab/active-research/joe-directed/integration-mint/im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md", 0,
  "rows_laundered: []"),
 ("S32", "lab/active-research/joe-directed/integration-mint/im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md", 0,
  "DERIVED_CONDITIONAL -> DERIVED occurs nowhere"),
 ("S33", "lab/active-research/joe-directed/integration-mint/im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md", 1,
  "whose base carried"),
 ("S34", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "the grant is declared, not derived"),
 ("S35", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  '"name": "INHERITANCE_BRIDGE"'),
 ("S36", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "descends from the fibre trace form"),
 ("S37", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "not laundered to DERIVED"),
 ("S38", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN"),
 ("S39", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "zero launders"),
 ("S40", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "none after the embedding is selected"),
 ("S41", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "none after the chiral 16 shadow is selected"),
 ("S42", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "none after the stabilizer is selected"),
 ("S43", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "none after AC-A1"),
 ("S44", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "HYP-TW-COHERENCE-01"),
 ("S45", "lab/process/conditional-physics-ledger-v0.259.json", 0,
  "may represent superposition"),
 ("S46", "lab/specifications/six-axis/six-axis-template.md", 1,
  "is acceptable but must be stated"),
 ("S47", "GEOMETER-VS-PHYSICS-OBJECTS.md", 1,
  "you must IDENTIFY which one you are using and WHY"),
 ("S48", "lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md", 0,
  "S-CHIRALITY-UNTYPED"),
 ("S49", "lab/active-research/joe-directed/README.md", 1,
  "already refuted in canon"),
]

# ---- mutation hooks -------------------------------------------------------
MUTATIONS = ("ref-gone", "row-regex-blind", "limit-loose", "root-elsewhere",
             "layer-expect-drift", "map-expect-drift", "quote-drift",
             "gate-gone", "fence-blind", "bare-name-blind")
_mut = os.environ.get("CT1_MUTATE", "")
if _mut == "ref-gone":
    REF = ROOT / "lab" / "methods" / "nonexistent-reference.md"
elif _mut == "row-regex-blind":
    OBJ_ROW_RE = re.compile(r"(?!x)x")
elif _mut == "limit-loose":
    MAX_OBJECTS = 999
elif _mut == "root-elsewhere":
    ROOT = pathlib.Path(tempfile.gettempdir())
elif _mut == "layer-expect-drift":
    EXPECTED_LAYER = EXPECTED_LAYER + ("cosmic",)
elif _mut == "map-expect-drift":
    EXPECTED_MAP = EXPECTED_MAP[:-1]
elif _mut == "quote-drift":
    QUOTES[0] = ("S01", QUOTES[0][1], 1, "five layers (declared total)")
elif _mut == "gate-gone":
    GATE_PATH = ROOT / "process_gates" / "nonexistent_gate.py"
elif _mut == "fence-blind":
    CODOMAIN_RE = re.compile(r"(?!x)x")
elif _mut == "bare-name-blind":
    REGISTERED_BARE = ()

PASS = 0
FAIL = 0
PLANTED_OBSERVED_TRUE = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


def planted_false(name: str, cond: bool) -> None:
    global PLANTED_OBSERVED_TRUE, FAIL, PASS
    if cond:
        PLANTED_OBSERVED_TRUE += 1
        FAIL += 1
        print(f"  FAIL  planted-false proposition came back TRUE: {name}")
    else:
        PASS += 1


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def rd(path) -> str:
    try:
        return pathlib.Path(path).read_text(encoding="utf-8")
    except OSError:
        return ""


# ---- reference parser (the instrument under test in leg D) ---------------
def parse_reference(text: str):
    objects = OBJ_ROW_RE.findall(text)
    arrows = ARROW_ROW_RE.findall(text)
    nonarrows = NONARROW_ROW_RE.findall(text)
    return objects, arrows, nonarrows


def category_counts(objects):
    counts = {"L": 0, "G": 0, "C": 0}
    for oid, _name, role, _stmt, _rcpt in objects:
        if role == "object" and oid[0] in counts:
            counts[oid[0]] += 1
    return counts


def over_budget(objects):
    return [k for k, v in category_counts(objects).items() if v > MAX_OBJECTS]


def receipt_paths(text: str):
    """All repository paths cited anywhere in the reference's table rows."""
    paths = set()
    for row in OBJ_ROW_RE.findall(text) + NONARROW_ROW_RE.findall(text):
        paths.update(PATH_RE.findall(row[-1]))
    for row in ARROW_ROW_RE.findall(text):
        paths.update(PATH_RE.findall(row[-1]))
    return sorted(paths)


def dangling(paths):
    return [p for p in paths if not (ROOT / p).is_file()]


def bare_named_objects(objects):
    hits = []
    for oid, name, role, _stmt, _rcpt in objects:
        if role != "object":
            continue
        cell = name.strip().strip("`")
        if cell in REGISTERED_BARE:
            hits.append(oid)
    return hits


def parse_codomain(text: str):
    m = CODOMAIN_RE.search(text)
    if not m:
        return None
    declared = {}
    for line in m.group(1).splitlines():
        lm = re.match(r"^([a-z-]+):\s*(.*)$", line)
        if lm:
            declared[lm.group(1)] = tuple(lm.group(2).split())
    return declared


# ---- gate import (guarded: a missing gate is a check failure, not a crash)
gate = None
try:
    _spec = importlib.util.spec_from_file_location("tcda", GATE_PATH)
    if _spec and _spec.loader:
        gate = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(gate)
except (OSError, ImportError, AttributeError):
    gate = None

ref_text = rd(REF)
objects, arrows, nonarrows = parse_reference(ref_text)
obj_by_id = {o[0]: o for o in objects}
arrow_by_id = {a[0]: a for a in arrows}

# ======================================================================
# LEG P -- parse
# ======================================================================
print("LEG P  parse")
check("P01 reference exists and is non-empty", bool(ref_text))
check("P02 every object row has a known role",
      bool(objects) and all(o[2] in ("object", "arrow-class",
                                     "declared-unknown-marker",
                                     "not-applicable-marker",
                                     "non-arrow-declaration", "bucket")
                            for o in objects))
check("P03 all row IDs unique",
      bool(objects) and
      len([o[0] for o in objects] + [a[0] for a in arrows]) ==
      len(set([o[0] for o in objects] + [a[0] for a in arrows])))
counts = category_counts(objects)
check("P04 Source-Layer category has exactly 4 objects (L1..L4)",
      counts.get("L") == 4 and all("L%d" % i in obj_by_id
                                   for i in range(1, 5)))
check("P05 Grant poset has exactly 8 objects (G0..G7) plus bucket G8",
      counts.get("G") == 8 and all("G%d" % i in obj_by_id
                                   for i in range(0, 8))
      and obj_by_id.get("G8", ("", "", ""))[2] == "bucket")
check("P06 Carrier category has exactly 11 objects (C1..C11)",
      counts.get("C") == 11 and all("C%d" % i in obj_by_id
                                    for i in range(1, 12)))
check("P07 every category is within the <= 12 object budget",
      bool(objects) and over_budget(objects) == [])
check("P08 markers M1..M4 present with marker roles",
      all("M%d" % i in obj_by_id for i in range(1, 5))
      and obj_by_id.get("M1", ("",) * 3)[2] == "declared-unknown-marker"
      and obj_by_id.get("M3", ("",) * 3)[2] == "not-applicable-marker")
check("P09 arrow labels CA1..CA13 with the role split 11 + not-a-map + "
      "UNTYPED",
      sum(1 for o in objects if o[0].startswith("CA")
          and o[2] == "arrow-class") == 11
      and obj_by_id.get("CA12", ("",) * 5)[2] == "non-arrow-declaration"
      and obj_by_id.get("CA13", ("",) * 5)[2] == "declared-unknown-marker")
check("P10 Layer arrows LA1..LA4 typed contraction / inclusion / quotient "
      "/ contraction-composite",
      arrow_by_id.get("LA1", ("",) * 6)[3].strip() == "contraction"
      and arrow_by_id.get("LA2", ("",) * 6)[3].strip() == "inclusion"
      and arrow_by_id.get("LA3", ("",) * 6)[3].strip() == "quotient"
      and "LA1" in arrow_by_id.get("LA4", ("",) * 6)[2] + " "
      + arrow_by_id.get("LA4", ("",) * 6)[1])
check("P11 LA3 is VEV-conditional and LA1 carries NOT injective",
      "VEV-conditional" in arrow_by_id.get("LA3", ("",) * 6)[4]
      and "NOT injective" in arrow_by_id.get("LA1", ("",) * 6)[4])
check("P12 named non-arrows N1..N3 present",
      len([n for n in nonarrows if n[0] in ("N1", "N2", "N3")]) == 3)
check("P12a Grant discharge is explicitly order-sensitive at the LA-5 "
      "AC-A1/AC-F3 witness without identifying G3 and G6",
      "**ORDER-SENSITIVE (typed 2026-08-24).**" in ref_text
      and "discharging `AC-A1` is what kills" in ref_text
      and "`AC-F3`" in ref_text
      and "does not identify G3 with G6" in ref_text)
codomain = parse_codomain(ref_text)
check("P13 codomain block present with both token lines",
      codomain is not None and "layer-tokens" in codomain
      and "map-type-tokens" in codomain)
check("P14 no object-name cell is a bare registered homonym token",
      bool(objects) and bare_named_objects(objects) == [])

# ======================================================================
# LEG R -- receipts
# ======================================================================
print("LEG R  receipts")
paths = receipt_paths(ref_text)
check("R01 every receipt path in the tables resolves to a real file",
      bool(paths) and dangling(paths) == [])
check("R02 distinct receipt paths exactly 24",
      len(paths) == 24)

# ======================================================================
# LEG C -- codomain triangle + planted drift fixtures + contrary control
# ======================================================================
print("LEG C  codomain")
check("C01 gate imports and its drift check is green against the live "
      "reference",
      gate is not None and gate.codomain_drift() == [])
check("C02 reference layer-tokens == probe pin == gate constant (sets and "
      "sizes)",
      codomain is not None and gate is not None
      and set(codomain.get("layer-tokens", ())) == set(EXPECTED_LAYER)
      == set(gate.LAYER_TOKENS)
      and len(codomain.get("layer-tokens", ())) == len(EXPECTED_LAYER)
      == len(gate.LAYER_TOKENS))
check("C03 reference map-type-tokens == probe pin == gate constant (sets "
      "and sizes)",
      codomain is not None and gate is not None
      and set(codomain.get("map-type-tokens", ())) == set(EXPECTED_MAP)
      == set(gate.MAP_TOKENS)
      and len(codomain.get("map-type-tokens", ())) == len(EXPECTED_MAP)
      == len(gate.MAP_TOKENS))

_fixture_block = ("```gu-token-codomain\nlayer-tokens: %s\n"
                  "map-type-tokens: %s\n```\n")
with tempfile.TemporaryDirectory() as _d:
    d = pathlib.Path(_d)
    fixtures = {
        "missing_token.md": _fixture_block % (
            " ".join(EXPECTED_LAYER[:-1]), " ".join(EXPECTED_MAP)),
        "extra_token.md": _fixture_block % (
            " ".join(EXPECTED_LAYER + ("cosmic",)), " ".join(EXPECTED_MAP)),
        "no_block.md": "no fenced block here\n",
        "dup_token.md": _fixture_block % (
            " ".join(EXPECTED_LAYER + ("ambient",)), " ".join(EXPECTED_MAP)),
        "reordered.md": _fixture_block % (
            " ".join(reversed(EXPECTED_LAYER)),
            " ".join(reversed(EXPECTED_MAP))),
    }
    for name, content in fixtures.items():
        (d / name).write_text(content, encoding="utf-8")
    if gate is not None:
        check("C04 planted drift: missing token is caught",
              gate.codomain_drift(str(d / "missing_token.md")) != [])
        check("C05 planted drift: extra token is caught",
              gate.codomain_drift(str(d / "extra_token.md")) != [])
        check("C06 planted drift: missing block is caught",
              gate.codomain_drift(str(d / "no_block.md")) != [])
        check("C07 planted drift: missing file is caught",
              gate.codomain_drift(str(d / "does_not_exist.md")) != [])
        check("C08 planted drift: duplicated token is caught",
              gate.codomain_drift(str(d / "dup_token.md")) != [])
        check("C09 CONTRARY control: reordered tokens are NOT drift "
              "(set semantics)",
              gate.codomain_drift(str(d / "reordered.md")) == [])
    else:
        for cid in ("C04", "C05", "C06", "C07", "C08", "C09"):
            check(cid + " (gate unavailable)", False)
check("C10 audit stats carry codomain_drift == 0 on the reference",
      gate is not None
      and gate.audit(paths=[str(REF)])[1].get("codomain_drift") == 0)

# ======================================================================
# LEG S -- exact substrings, read from the owners
# ======================================================================
print("LEG S  sources")
for sid, rel, do_norm, sub in QUOTES:
    text = rd(ROOT / rel)
    hay = norm(text) if do_norm else text
    needle = norm(sub) if do_norm else sub
    check("%s owner carries the quoted sentence: %s" % (sid, rel.split("/")[-1]),
          bool(text) and needle in hay)

# ======================================================================
# LEG F -- planted-false propositions
# ======================================================================
print("LEG F  planted-false")
planted_false("F01 some category exceeds the 12-object budget",
              bool(objects) and over_budget(objects) != [])
planted_false("F02 an object-name cell is a bare registered homonym token",
              bool(objects) and bare_named_objects(objects) != [])
planted_false("F03 a receipt path cited in the tables does not resolve",
              bool(paths) and dangling(paths) != [])
planted_false("F04 the gate's token sets drift from the reference",
              gate is not None and gate.codomain_drift() != [])
planted_false("F05 a Grant-poset relation row identifies G3 with G6",
              any(("G3" in a[1] + a[2] and "G6" in a[1] + a[2])
                  for a in arrows if a[0].startswith("GA")))

# ======================================================================
# LEG D -- detector power on synthetic positives
# ======================================================================
print("LEG D  detector power")
_row = "| %s | fixture-object-%d | object | synthetic | lab/methods/gu-base-categories.md |"
_thirteen = "\n".join(_row % ("L%d" % i, i) for i in range(1, 14))
_objs13, _, _ = parse_reference(_thirteen + "\n")
check("D01 a planted 13-object category IS detected as over budget",
      over_budget(_objs13) == ["L"])
_dangle = ("| G1 | fixture | object | synthetic | "
           "lab/methods/does-not-exist-ct1-fixture.md |\n")
_objsD, _, _ = parse_reference(_dangle)
_pathsD = receipt_paths(_dangle)
check("D02 a planted dangling receipt IS detected",
      "lab/methods/does-not-exist-ct1-fixture.md" in _pathsD
      and dangling(_pathsD) == ["lab/methods/does-not-exist-ct1-fixture.md"])
_bare = "| C1 | `so(1,3)` | object | synthetic | GEOMETER-VS-PHYSICS-OBJECTS.md |\n"
_objsB, _, _ = parse_reference(_bare)
check("D03 a planted bare-homonym object name IS detected",
      bare_named_objects(_objsB) == ["C1"])

# ======================================================================
# LEG A/G -- artifact conformance + runtime
# ======================================================================
print("LEG A/G  artifact + runtime")
art_text = rd(ART)
check("A01 design artifact exists", bool(art_text))
if gate is not None and art_text:
    art_fm, _raw = gate.frontmatter(art_text)
else:
    art_fm = {}
check("A02 target_claim is NONE-NOT-A-KILL",
      "NONE-NOT-A-KILL" in art_fm.get("target_claim", ""))
check("A03 routing marker carried", "GU-COMPARATOR-ROUTING" in art_text)
check("A04 classification matches the routing audit's acceptance regex",
      re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                art_text) is not None)
check("A05 required registry write printed verbatim",
      '"classification": "INTERNAL_STRUCTURAL_ONLY"' in art_text
      and "ct1-base-categories-2026-08-17.md" in art_text)
live_blocks = gate.FENCE_RE.findall(art_text) if gate is not None else []
check("A06 exactly one live gu-typed-objects block", len(live_blocks) == 1)
check("A07 the live block validates clean",
      len(live_blocks) == 1 and gate is not None
      and gate.validate_block(live_blocks[0])[0] == [])
check("A08 the live block declares exactly one ambiguous slot (the LAYER "
      "marker)",
      len(live_blocks) == 1 and gate is not None
      and gate.validate_block(live_blocks[0])[1] == 1)
check("A09 depends_on names the reference",
      "lab/methods/gu-base-categories.md" in art_text)
check("A10 scripts names this probe",
      "tests/channel-swings/joe_directed_ct1_base_categories.py" in art_text)
check("A11 artifact is dated into the gate's scope",
      art_fm.get("created", "") == "2026-08-17")

if gate is not None and art_text and ref_text:
    code_new, stats_new = gate.audit(paths=[str(REF), str(ART)])
    check("G01 the two new files audit green in dated scope "
          "(scope 2, red 0)",
          code_new == 0 and stats_new["scope"] == 2
          and stats_new["red"] == 0)
    check("G02 the reference is untriggered; the artifact is triggered "
          "with its one block",
          stats_new["triggered"] == 1 and stats_new["blocks"] == 1)

    def _no_float(obj) -> bool:
        if isinstance(obj, float):
            return False
        if isinstance(obj, dict):
            return all(_no_float(k) and _no_float(v) for k, v in obj.items())
        if isinstance(obj, (list, tuple, set)):
            return all(_no_float(x) for x in obj)
        return True

    check("G03 no float anywhere in the result surface (swept)",
          _no_float(stats_new) and _no_float(counts))
else:
    for gid in ("G01", "G02", "G03"):
        check(gid + " (gate or files unavailable)", False)

r1 = subprocess.run([sys.executable, str(GATE_PATH), "--selftest"],
                    cwd=ROOT, capture_output=True, text=True)
check("G04 edited gate --selftest exits 0 and reports GREEN "
      "(incl. the codomain controls)",
      r1.returncode == 0 and "SELF-TEST GREEN" in r1.stdout)

if gate is not None:
    live_code, live_stats = gate.audit()
    print("  [reconciliation 2026-08-17] live scan: red-exit=%d scope=%d "
          "triggered=%d blocks=%d codomain_drift=%d"
          % (live_code, live_stats["scope"], live_stats["triggered"],
             live_stats["blocks"], live_stats["codomain_drift"]))
    if "--strict" in sys.argv:
        check("G05s live repo scan is green (strict)", live_code == 0)
    else:
        check("G05 live scan returns integer counters (reconciliation, "
              "not asserted; shared checkout)",
              all(isinstance(live_stats[k], int)
                  for k in ("red", "scope", "triggered", "blocks",
                            "untyped_slots", "codomain_drift")))
else:
    check("G05 (gate unavailable)", False)


# ======================================================================
# certificate / selftest driver
# ======================================================================
def main() -> int:
    total = PASS + FAIL
    print("CERTIFICATE: %d/%d checks pass; %d planted-false propositions "
          "observed true; no load-bearing float (swept)."
          % (PASS, total, PLANTED_OBSERVED_TRUE))
    return 0 if FAIL == 0 else 1


def selftest(poison: bool) -> int:
    env = dict(os.environ)
    env.pop("CT1_MUTATE", None)
    if poison:
        env["CT1_MUTATE"] = "ref-gone"
    base = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env,
                          capture_output=True, text=True)
    if base.returncode != 0:
        print("SELFTEST: clean baseline does NOT pass; mutations were "
              "NOT run")
        print("SELFTEST FAILED")
        return 1
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ)
        env["CT1_MUTATE"] = m
        r = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env,
                           capture_output=True, text=True)
        completed = "CERTIFICATE:" in r.stdout
        genuine = "  FAIL" in r.stdout
        caught = r.returncode == 1 and completed and genuine
        label = ("caught (exit 1, genuine FAIL)" if caught else
                 "MISSED" if r.returncode == 0 else
                 "CRASH-NOT-DETECTION (no certificate line)")
        print("  mutation %s: %s" % (m, label))
        ok = ok and caught
    print("SELFTEST " + ("GREEN: clean baseline first, then %d/%d "
                         "mutations each exit 1 via genuine FAIL lines"
                         % (len(MUTATIONS), len(MUTATIONS))
                         if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest(poison="--poison" in sys.argv))
    sys.exit(main())
