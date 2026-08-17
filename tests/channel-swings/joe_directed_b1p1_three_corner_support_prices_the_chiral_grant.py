#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B1P-1 -- the bit-1 price, printed and verified.

WHAT THIS PROBE IS FOR.  SG4's residual is a 2-bit square (invariance x phase),
and the repository's routing surfaces present bit 2 (the phase) as
independently grantable.  It is not.  The frozen predeclaration
tests/gu-forces/leg_a_forcing_enumeration.py carries a VERTEX map whose fourth
corner is labelled INCONSISTENT, so the CONSISTENT support is three corners,
not four -- and a three-element support inside a 2x2 is not a product set.
This probe certifies:

  LEG V  VERTEX.  The predeclaration is byte-identical to SG-1's SHA-256 pin;
         its VERTEX map is parsed (never restated) and the correlation is
         RECOMPUTED: support size 3, the excluded corner, the non-product
         witness, ABSENT=>MASSIVE, CHIRAL=>PRESENT, CHIRAL=>carrier A uniquely,
         and the frozen index labels.  Two CONTRARY controls assert that BOTH
         converses FAIL and must PASS -- they look like they weaken the result
         and are exactly what keeps it a one-way price rather than a verdict.

  LEG Q  RECEIPTS.  Fourteen exact substrings read from their owning files, not
         remembered, plus line-locus checks that canon :59-64 and lega1 :257
         really carry their clauses at those lines.

  LEG P  PRINT.  Seven clauses of the dated G6 addendum are present in
         lab/methods/gu-base-categories.md, including the "no corner is
         selected" disclaimer, both receipts, the failing converses and the
         non-uniform-mass-map escape.

  LEG L  LA3.  The corrected LA3 row re-parsed with CT-1's own arrow regex:
         six cells, type `quotient`, `VEV-conditional` preserved, the corrected
         direction present, the dated marker present, and the inverted claim
         ASSERTED nowhere (the old string survives only inside the correction
         marker, and the check requires that context).  CT-1's R02 receipt-path
         count and the 4/8/11 object counts are recomputed independently.

  LEG M  MISSES + COUPLING RULE.  Absence checks (zero SC-CHI-01, zero
         "bit 2"/"bit-2" in SRC-1..4; zero SRC paths in the source register),
         each with a PLANTED-POSITIVE control proving the detector fires
         (VERIFICATION.md rule 4).  The target_claim state of the four SRC
         files.  The CC-06 reach measurement computed LIVE through the currency
         gate's own signature_match -- family 2 hits 4/4, family 1 hits 0/4,
         conjunction False on all four -- with its own planted-positive.

  LEG F  PLANTED-FALSE.  Six predeclared FALSE propositions each observed False.

  LEG A/G  ARTIFACT + RUNTIME.  The B1P-1 artifact carries the routing notice,
         INTERNAL_STRUCTURAL_ONLY in the routing audit's accepted form,
         NONE-NOT-A-KILL, canonical_effect: pending_integration, the dated
         frontmatter and the scripts/depends_on wiring, and exactly one
         gu-typed-objects block validating clean.  By subprocess: CT-1's probe
         still exits 0 (the LA3 repair did not red it) and the typed-carrier
         gate's --selftest is GREEN.

Exit 0 == every check passed.  --selftest verifies the CLEAN BASELINE FIRST
(an unmutated subprocess must exit 0 and print its certificate BEFORE any
mutation is attempted; a red baseline aborts rather than banking false
catches), then injects ten machinery/reference corruptions via B1P1_MUTATE.
Every mutation corrupts MACHINERY OR A REFERENCE -- none loosens a check's
predicate (VERIFICATION.md rule 2).  Each is required to drive exit 1 THROUGH
a genuine "[FAIL]" line on a run that still prints its certificate; a nonzero
exit without one is CRASH-NOT-DETECTION and fails the selftest (rule 3).
The selftest exits 0 on success (rule 5).  --selftest --poison poisons the
baseline run itself and requires the refusal path.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]

# ---- instrument constants (mutation targets; corrupting any of these is a
# machinery/reference corruption, never a weakened check) -------------------
LEG_A_REL = "tests/gu-forces/leg_a_forcing_enumeration.py"
# SG-1's pin (tests/channel-swings/joe_directed_sg1_c6a_scope_narrowing.py:78).
# Two instruments now red on any edit of the predeclaration, not one.
LEG_A_SHA256 = "3043d29ef2ca97b527113b16a399f7f5256ba8df85902ccff3b3d69a58380197"
REF_REL = "lab/methods/gu-base-categories.md"
ART_REL = ("lab/active-research/joe-directed/bit1-price/"
           "b1p1-three-corner-support-prices-the-chiral-grant-2026-08-17.md")
CT1_REL = "tests/channel-swings/joe_directed_ct1_base_categories.py"
GATE_REL = "process_gates/typed_carrier_declaration_audit.py"
CURRENCY_REL = "process_gates/canonical_currency_audit.py"
REGISTER_REL = "lab/sources/source-claim-register.yaml"

SRC_RELS = [
    "lab/active-research/joe-directed/majorana-126-neutrino/"
    "src1-source-steelman-of-the-vev-2026-08-14.md",
    "lab/active-research/joe-directed/majorana-126-neutrino/"
    "src2-mexican-hat-is-automatic-2026-08-14.md",
    "lab/active-research/joe-directed/majorana-126-neutrino/"
    "src3-potential-unbounded-below-2026-08-14.md",
    "lab/active-research/joe-directed/majorana-126-neutrino/"
    "src4-eddy-completion-cannot-rescue-the-potential-2026-08-15.md",
]

# CT-1's own arrow-row regex, reused verbatim so this probe measures the same
# object CT-1 measures (a divergent private regex would certify nothing).
ARROW_ROW_RE = re.compile(
    r"^\|\s*([LG]A\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
    r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", re.M)
OBJ_ROW_RE = re.compile(
    r"^\|\s*([LGM]\d+|C(?:A)?\d+)\s*\|\s*([^|]+?)\s*\|\s*([a-z-]+)\s*\|"
    r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", re.M)
NONARROW_ROW_RE = re.compile(
    r"^\|\s*(N\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$",
    re.M)
PATH_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|py|yaml|json)")
CT1_RECEIPT_COUNT = 24          # CT-1's R02 pin; recomputed, not trusted
CT1_OBJECT_COUNTS = {"L": 4, "G": 8, "C": 11}

# the tokens whose ABSENCE from the SRC arc is the measured miss
MISS_TOKENS = ("SC-CHI-01", "bit 2", "bit-2")
SRC_PATH_MARKER = "majorana-126-neutrino/src"

# (id, repo-relative path, whitespace-normalize?, exact substring)
QUOTES = [
 ("Q01", "canon/escape-corners-campaign-RESULTS.md", 1,
  '"Too massive" and "decreased VEV" are opposing demands on one dial'),
 ("Q02", "canon/escape-corners-campaign-RESULTS.md", 1,
  "At the chiral point GU's phenomenology commits to"),
 ("Q03", "canon/escape-corners-campaign-RESULTS.md", 1,
  "UNLESS the demanded SUSY is the upstairs one"),
 ("Q04", "canon/escape-corners-campaign-RESULTS.md", 1,
  "NO invariant mass channel"),
 ("Q05", "tests/escape-corners/lega1_flipped_chiral_adjudication.md", 1,
  "corner (a) fires only if GU's physical vacuum is taken at the chiral point "
  "AND the mass map is uniform across the fermionic extension"),
 ("Q06", "canon/gu-forces-field-space-declaration-RESULTS.md", 1,
  "Bit 1 -- invariance-selection:"),
 ("Q07", "canon/gu-forces-field-space-declaration-RESULTS.md", 1,
  "chiral/unbroken vs massive/super-Higgs"),
 ("Q08", LEG_A_REL, 1, "A at the chiral point, B at the massive point"),
 ("Q09", LEG_A_REL, 1,
  "ungauged massless CHARGED spin-3/2 -> GP bites, no SUSY"),
 ("Q10", "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 1,
  "no vacuum expectation value pulling the various"),
 ("Q11", REGISTER_REL, 1,
  "pulling the various sub-fields of varpi to values significantly above zero"),
 ("Q12", "papers/drafts/Transcript into the impossible.md", 1,
  "exactly three families of chiral fermions if you have a decreased VEV"),
 ("Q13", "lab/active-research/joe-directed/lens-digs/"
         "ldc-vev-selector-adjudication-2026-08-17.md", 1,
  "three corners, not four, hence NOT a product set"),
 ("Q14", "lab/process/upgrade-program-register.yaml", 1, "BIT1-PRICE-PRINT"),
]

# (id, repo-relative path, 1-based line span, exact substring on those lines)
LOCI = [
 ("X01", "canon/escape-corners-campaign-RESULTS.md", 59, 64,
  "opposing demands on one"),
 ("X02", "canon/escape-corners-campaign-RESULTS.md", 59, 64,
  "UNLESS the demanded SUSY is the upstairs one"),
 ("X03", "tests/escape-corners/lega1_flipped_chiral_adjudication.md", 257, 258,
  "corner (a) fires only if GU's physical vacuum is taken at the chiral point"),
]

# clauses of the printed G6 addendum (LEG P)
PRINT_CLAUSES = [
 ("P01", "the bit-1 price of a bit-2 CHIRAL grant"),
 ("P02", "consistent support is THREE, not four"),
 ("P03", "CHIRAL => PRESENT => carrier A"),
 ("P04", "Both converses FAIL"),
 ("P05", "no corner is selected"),
 ("P06", "NON-uniform mass map across the fermionic extension"),
 ("P07", "not independently grantable"),
]

# ---- mutation hooks -------------------------------------------------------
MUTATIONS = ("vertex-corner-drop", "support-admits-inconsistent", "sha-drift",
             "ref-gone", "root-elsewhere", "quote-drift",
             "absence-detector-blind", "cc-family-blind", "arrow-regex-blind",
             "planted-eval-invert")
_mut = os.environ.get("B1P1_MUTATE", "")
_MUT_DROP_CORNER = _mut == "vertex-corner-drop"
_MUT_SUPPORT_LOOSE = _mut == "support-admits-inconsistent"
_MUT_ABSENCE_BLIND = _mut == "absence-detector-blind"
_MUT_PLANTED_INVERT = _mut == "planted-eval-invert"
if _mut == "sha-drift":
    LEG_A_SHA256 = LEG_A_SHA256[::-1]
elif _mut == "ref-gone":
    REF_REL = "lab/methods/nonexistent-b1p1-reference.md"
elif _mut == "root-elsewhere":
    ROOT = pathlib.Path(tempfile.gettempdir())
elif _mut == "quote-drift":
    QUOTES[0] = ("Q01", QUOTES[0][1], 1,
                 '"Too massive" and "increased VEV" are complementary demands')
elif _mut == "arrow-regex-blind":
    ARROW_ROW_RE = re.compile(r"(?!x)x")

PASS = 0
FAIL = 0
PLANTED_OBSERVED_TRUE = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  [PASS] " + name)
    else:
        FAIL += 1
        print("  [FAIL] " + name)


def planted_false(name: str, cond: bool) -> None:
    """A predeclared FALSE proposition.  Observing it True is a failure."""
    global PLANTED_OBSERVED_TRUE, FAIL, PASS
    observed = (not cond) if _MUT_PLANTED_INVERT else cond
    if observed:
        PLANTED_OBSERVED_TRUE += 1
        FAIL += 1
        print("  [FAIL] planted-false proposition came back TRUE: " + name)
    else:
        PASS += 1
        print("  [PASS] planted-false stays False: " + name)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def rd(rel) -> str:
    try:
        return (ROOT / rel).read_text(encoding="utf-8")
    except OSError:
        return ""


# ---- machinery under test -------------------------------------------------
def parse_vertex(src: str):
    """Parse the frozen VERTEX map out of the predeclaration's source."""
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == "VERTEX":
                    v = ast.literal_eval(node.value)
                    if _MUT_DROP_CORNER:
                        v = {k: val for k, val in v.items()
                             if k != ("ABSENT", "CHIRAL")}
                    return v
    return {}


def consistent_support(vertex: dict) -> dict:
    """The corners carrying a LIVE carrier."""
    if _MUT_SUPPORT_LOOSE:
        return dict(vertex)
    return {k: v for k, v in vertex.items()
            if v.get("carrier") != "INCONSISTENT"}


def is_product_set(support: dict) -> bool:
    axis0 = {k[0] for k in support}
    axis1 = {k[1] for k in support}
    return {(a, b) for a in axis0 for b in axis1} == set(support)


def non_product_witnesses(support: dict):
    axis0 = {k[0] for k in support}
    axis1 = {k[1] for k in support}
    return sorted({(a, b) for a in axis0 for b in axis1} - set(support))


def forces(support: dict, ant_axis: int, ant_val: str,
           con_axis: int, con_val: str) -> bool:
    """Given consistency, does ant_val on one axis force con_val on the other?"""
    rows = [k for k in support if k[ant_axis] == ant_val]
    return bool(rows) and all(k[con_axis] == con_val for k in rows)


def carriers_over(support: dict, axis: int, val: str) -> set:
    return {v["carrier"] for k, v in support.items() if k[axis] == val}


def token_hits(text: str, tokens) -> list:
    """Absence detector.  Blinding it must be caught by the planted positive."""
    if _MUT_ABSENCE_BLIND:
        return []
    return [t for t in tokens if t in text]


def arrow_rows(text: str) -> dict:
    return {m[0]: m for m in ARROW_ROW_RE.findall(text)}


def receipt_paths(text: str) -> list:
    paths = set()
    for row in OBJ_ROW_RE.findall(text) + NONARROW_ROW_RE.findall(text):
        paths.update(PATH_RE.findall(row[-1]))
    for row in ARROW_ROW_RE.findall(text):
        paths.update(PATH_RE.findall(row[-1]))
    return sorted(paths)


def object_counts(text: str) -> dict:
    counts = {"L": 0, "G": 0, "C": 0}
    for oid, _n, role, _s, _r in OBJ_ROW_RE.findall(text):
        if role == "object" and oid[0] in counts:
            counts[oid[0]] += 1
    return counts


def load_module(rel: str):
    try:
        spec = importlib.util.spec_from_file_location(
            "b1p1_" + re.sub(r"\W", "_", rel), ROOT / rel)
        if not spec or not spec.loader:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except (OSError, ImportError, AttributeError, SyntaxError):
        return None


# ======================================================================
# LEG V -- the correlation, recomputed from the frozen predeclaration
# ======================================================================
print("LEG V  vertex")
leg_a_raw = (ROOT / LEG_A_REL).read_bytes() if (ROOT / LEG_A_REL).is_file() \
    else b""
check("V01 predeclaration exists and is byte-identical to SG-1's SHA-256 pin "
      "(any edit reds this and SG-1 together)",
      bool(leg_a_raw)
      and hashlib.sha256(leg_a_raw).hexdigest() == LEG_A_SHA256)
VERTEX = parse_vertex(leg_a_raw.decode("utf-8")) if leg_a_raw else {}
check("V02 VERTEX parses to the full 2x2 over INVARIANCE x PHASE (4 keys)",
      len(VERTEX) == 4
      and {k[0] for k in VERTEX} == {"ABSENT", "PRESENT"}
      and {k[1] for k in VERTEX} == {"CHIRAL", "MASSIVE"})
SUPPORT = consistent_support(VERTEX)
check("V03 the CONSISTENT support is exactly THREE corners, not four",
      len(SUPPORT) == 3)
check("V04 the single excluded corner is (ABSENT, CHIRAL), carried "
      "INCONSISTENT",
      [k for k in VERTEX if k not in SUPPORT] == [("ABSENT", "CHIRAL")]
      and VERTEX.get(("ABSENT", "CHIRAL"), {}).get("carrier") == "INCONSISTENT")
check("V05 the support is NOT a product set, witness (ABSENT, CHIRAL)",
      not is_product_set(SUPPORT)
      and non_product_witnesses(SUPPORT) == [("ABSENT", "CHIRAL")])
check("V06 given consistency: ABSENT => MASSIVE",
      forces(SUPPORT, 0, "ABSENT", 1, "MASSIVE"))
check("V07 given consistency: CHIRAL => PRESENT",
      forces(SUPPORT, 1, "CHIRAL", 0, "PRESENT"))
check("V08 given consistency: CHIRAL => carrier A, uniquely",
      carriers_over(SUPPORT, 1, "CHIRAL") == {"A"})
check("V09 CONTRARY control: PRESENT does NOT force CHIRAL (the price is "
      "one-way, not an equivalence)",
      not forces(SUPPORT, 0, "PRESENT", 1, "CHIRAL")
      and carriers_over(SUPPORT, 0, "PRESENT") == {"A", "CTRL40"})
check("V10 CONTRARY control: MASSIVE does NOT force ABSENT (nothing is "
      "priced in the massive direction)",
      not forces(SUPPORT, 1, "MASSIVE", 0, "ABSENT")
      and carriers_over(SUPPORT, 1, "MASSIVE") == {"B", "CTRL40"})
check("V11 the three live corners carry the frozen carrier/index labels "
      "B/-38, A/-42, CTRL40/-40 (opaque labels; no arithmetic performed)",
      {k: (v["carrier"], v["index"]) for k, v in SUPPORT.items()} == {
          ("ABSENT", "MASSIVE"): ("B", -38),
          ("PRESENT", "CHIRAL"): ("A", -42),
          ("PRESENT", "MASSIVE"): ("CTRL40", -40)})
check("V12 field-space is DEPENDENT on the pair, as the predeclaration "
      "states (three distinct values across the three live corners)",
      len({v["field_space"] for v in SUPPORT.values()}) == 3)

# ======================================================================
# LEG Q -- receipts, read from the owners
# ======================================================================
print("LEG Q  receipts")
for qid, rel, do_norm, sub in QUOTES:
    text = rd(rel)
    hay = norm(text) if do_norm else text
    needle = norm(sub) if do_norm else sub
    check("%s owner carries the quoted string: %s" % (qid, rel.split("/")[-1]),
          bool(text) and needle in hay)
for xid, rel, lo, hi, sub in LOCI:
    text = rd(rel)
    lines = text.splitlines()
    window = norm(" ".join(lines[lo - 1:hi])) if lines else ""
    check("%s the cited locus %s:%d-%d really carries its clause"
          % (xid, rel.split("/")[-1], lo, hi),
          bool(window) and norm(sub) in window)

# ======================================================================
# LEG P -- the printed price
# ======================================================================
print("LEG P  print")
ref_text = rd(REF_REL)
ref_norm = norm(ref_text)
check("P00 the base-category reference exists and is non-empty", bool(ref_text))
for pid, clause in PRINT_CLAUSES:
    check("%s the G6 addendum carries: %s" % (pid, clause[:58]),
          norm(clause) in ref_norm)
check("P08 the addendum is dated 2026-08-17 and names its register item",
      "added 2026-08-17 by" in ref_norm and "BIT1-PRICE-PRINT" in ref_text)
check("P09 the addendum carries BOTH receipts by path and line",
      "canon/escape-corners-campaign-RESULTS.md` :59-64" in ref_text
      and "lega1_flipped_chiral_adjudication.md` :257" in ref_text)
check("P10 the addendum states SG4 remains the sole decider and the residual "
      "stays 2-bit",
      "SG4 remains the sole decider" in ref_norm
      and "residual remains" in ref_norm)
check("P11 the addendum re-pins the predeclaration hash prefix (the reader "
      "can check the map was frozen)",
      LEG_A_SHA256[:8] in ref_text)

# ======================================================================
# LEG L -- the LA3 repair
# ======================================================================
print("LEG L  LA3")
rows = arrow_rows(ref_text)
la3 = rows.get("LA3", ("",) * 6)
check("L01 LA3 parses with CT-1's own six-cell arrow schema", len(la3) == 6)
check("L02 LA3's MAP-TYPE cell is still exactly `quotient` (CT-1 pin P10)",
      la3[3].strip() == "quotient")
check("L03 LA3's conditionality cell still contains `VEV-conditional` "
      "(CT-1 pin P11)", "VEV-conditional" in la3[4])
check("L04 LA3 still declares its domain/codomain L1 -> L4",
      "L1 -> L4" in la3[2])
check("L05 the CORRECTED direction is stated: the arrow is PRESENT in the "
      "varpi -> 0 phase",
      "arrow is PRESENT in the `varpi -> 0`" in la3[4])
check("L06 and ABSENT once the VEV pulls the sub-fields above zero",
      "ABSENT once a VEV pulls the `varpi` sub-fields significantly above zero"
      in la3[4])
check("L07 the correction is dated and attributed to its register item",
      "DIRECTION CORRECTED 2026-08-17" in la3[4]
      and "CT1-LA3-WORDING" in la3[4])
_inverted = "in the `varpi -> 0` phase the arrow is absent"
check("L08 the INVERTED claim is asserted nowhere: the old string survives "
      "only inside the dated correction marker (struck, not deleted)",
      (_inverted not in ref_text)
      or all("DIRECTION CORRECTED" in ref_text[max(0, i - 320):i + 120]
             for i in [m.start() for m in
                       re.finditer(re.escape(_inverted), ref_text)]))
check("L09 CT-1's R02 receipt-path count is unchanged at 24 (neither edit "
      "adds a table-row receipt; the addendum is prose)",
      len(receipt_paths(ref_text)) == CT1_RECEIPT_COUNT)
check("L10 the object counts are unchanged at 4 / 8 / 11 (the addendum coins "
      "no object; CT-1 pins P04-P06)",
      object_counts(ref_text) == CT1_OBJECT_COUNTS)
check("L11 no Grant-poset arrow row was created relating G3 to G6 "
      "(CT-1 planted-false F05 stays False)",
      not any(("G3" in a[1] + a[2] and "G6" in a[1] + a[2])
              for a in rows.values() if a[0].startswith("GA")))
check("L12 the gu-token-codomain block is untouched (both token lines "
      "present, so the gate's three-surface triangle is unaffected)",
      "```gu-token-codomain" in ref_text
      and "layer-tokens:" in ref_text and "map-type-tokens:" in ref_text)

# ======================================================================
# LEG M -- the three dated misses and the coupling-rule sensing
# ======================================================================
print("LEG M  misses + coupling rule")
src_texts = {rel: rd(rel) for rel in SRC_RELS}
check("M01 all four SRC artifacts are present and non-empty",
      all(bool(t) for t in src_texts.values()))
check("M02 ABSENCE: zero occurrences of SC-CHI-01 / bit 2 / bit-2 across all "
      "four SRC artifacts (the three dated misses)",
      all(token_hits(t, MISS_TOKENS) == [] for t in src_texts.values()))
check("M03 PLANTED-POSITIVE control: the same detector DOES fire on a "
      "synthetic file carrying SC-CHI-01 (rule 4: an absence check on a clean "
      "corpus proves nothing without a demonstrated positive)",
      token_hits("prose ... SC-CHI-01 hedge-watch ping ... prose",
                 MISS_TOKENS) == ["SC-CHI-01"])
check("M04 PLANTED-POSITIVE control: the detector fires on the 'bit 2' token "
      "too", token_hits("routed to bit 2 alone", MISS_TOKENS) == ["bit 2"])
register_text = rd(REGISTER_REL)
check("M05 ABSENCE: zero SRC paths anywhere in the source-claim register "
      "(SC-CHI-01's adherence cites none of them)",
      bool(register_text) and SRC_PATH_MARKER not in register_text)
check("M06 PLANTED-POSITIVE control: the SRC-path detector fires on a "
      "synthetic register line citing one",
      SRC_PATH_MARKER in
      "    - lab/active-research/joe-directed/majorana-126-neutrino/src2-x.md")
_fm = {}
for rel, text in src_texts.items():
    m = re.search(r"^target_claim:\s*(.*)$", text, re.M)
    _fm[rel] = m.group(1).strip() if m else None
check("M07 SRC-2 and SRC-3 carry NO target_claim key at all (the mechanical "
      "reason the kill-target gate never surfaced them)",
      _fm[SRC_RELS[1]] is None and _fm[SRC_RELS[2]] is None)
check("M08 SRC-1's target_claim names a DIFFERENT claim (SC-GEO-58) and "
      "SRC-4's carries no SC- ID at all",
      (_fm[SRC_RELS[0]] or "").startswith("SC-GEO-58")
      and not re.search(r"SC-[A-Z]+-\d+", _fm[SRC_RELS[3]] or ""))
check("M09 none of the four SRC target_claim values names SC-CHI-01",
      all("SC-CHI-01" not in (v or "") for v in _fm.values()))

currency = load_module(CURRENCY_REL)
cc06 = None
if currency is not None:
    try:
        _entries = currency.load_registry(currency.default_cfg())
        cc06 = next((e for e in _entries
                     if e.get("id") == "CC-06-CHIRALITY-VEV-CONDITIONAL"), None)
    except Exception:                                   # noqa: BLE001
        cc06 = None
if _mut == "cc-family-blind" and cc06 is not None:
    cc06 = dict(cc06)
    cc06["signature"] = dict(cc06.get("signature") or {})
    cc06["signature"]["token_families"] = [["vev"], ["vev"]]
check("M10 the live correction registry loads and carries "
      "CC-06-CHIRALITY-VEV-CONDITIONAL with a two-family signature",
      cc06 is not None and len(currency.families_of(cc06)) == 2)
if cc06 is not None and currency is not None:
    fams = currency.families_of(cc06)
    fam1_hits = sum(1 for t in src_texts.values()
                    if any(tok.lower() in t.lower() for tok in fams[0]))
    fam2_hits = sum(1 for t in src_texts.values()
                    if any(tok.lower() in t.lower() for tok in fams[1]))
    conj = [currency.signature_match(cc06, t.lower())
            for t in src_texts.values()]
    check("M11 MEASURED: CC-06's family 2 reaches 4/4 SRC artifacts",
          fam2_hits == 4)
    check("M12 MEASURED: CC-06's family 1 (the chirality-mechanism anchor) "
          "reaches 0/4 -- the declared blindness", fam1_hits == 0)
    check("M13 MEASURED: the CC-06 conjunction is False on all four, so the "
          "currency gate CANNOT carry the hedge-watch sensing as written",
          conj == [False, False, False, False])
    check("M14 PLANTED-POSITIVE control: the same signature_match DOES fire "
          "on a synthetic string hitting both families (the detector has "
          "power; the miss is the corpus, not the instrument)",
          currency.signature_match(
              cc06, "the source's stated mechanism for effective chirality "
                    "under a vev and a condensate"))
else:
    for cid in ("M11", "M12", "M13", "M14"):
        check(cid + " (currency gate or CC-06 entry unavailable)", False)

# ======================================================================
# LEG F -- planted-false propositions
# ======================================================================
print("LEG F  planted-false")
planted_false("F01 the consistent support is a product set (i.e. the bits are "
              "independent given consistency)",
              bool(SUPPORT) and is_product_set(SUPPORT))
planted_false("F02 the converse holds: PRESENT => CHIRAL",
              bool(SUPPORT) and forces(SUPPORT, 0, "PRESENT", 1, "CHIRAL"))
planted_false("F03 the (ABSENT, CHIRAL) corner carries a live carrier",
              VERTEX.get(("ABSENT", "CHIRAL"), {}).get("carrier")
              not in (None, "INCONSISTENT"))
planted_false("F04 CC-06's signature as written reaches SRC-2",
              cc06 is not None and currency is not None
              and currency.signature_match(cc06,
                                           src_texts[SRC_RELS[1]].lower()))
planted_false("F05 the source-claim register cites an SRC artifact path",
              bool(register_text) and SRC_PATH_MARKER in register_text)
planted_false("F06 the reference still ASSERTS the inverted LA3 direction "
              "outside a correction marker",
              bool(ref_text) and _inverted in ref_text
              and not any("DIRECTION CORRECTED"
                          in ref_text[max(0, i - 320):i + 120]
                          for i in [m.start() for m in
                                    re.finditer(re.escape(_inverted),
                                                ref_text)]))

# ======================================================================
# LEG A/G -- artifact conformance + runtime
# ======================================================================
print("LEG A/G  artifact + runtime")
gate = load_module(GATE_REL)
art_text = rd(ART_REL)
art_fm = gate.frontmatter(art_text)[0] if (gate is not None and art_text) \
    else {}
check("A01 the B1P-1 artifact exists", bool(art_text))
check("A02 routing marker carried", "GU-COMPARATOR-ROUTING" in art_text)
check("A03 classification matches the routing audit's acceptance regex "
      "(INTERNAL_STRUCTURAL_ONLY)",
      re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                art_text) is not None)
check("A04 target_claim is NONE-NOT-A-KILL with an internal scope statement",
      "NONE-NOT-A-KILL" in art_fm.get("target_claim", "")
      and "INTERNAL" in art_fm.get("target_claim", ""))
check("A05 canonical_effect is pending_integration",
      art_fm.get("canonical_effect", "") == "pending_integration")
check("A06 no status is claimed to move (canon/ledger/register/priority)",
      art_fm.get("canon_verdict_change") == "none"
      and art_fm.get("ledger_edit") == "none"
      and art_fm.get("register_edit") == "none"
      and art_fm.get("steering_effect") == "unchanged")
check("A07 artifact is dated into the typed-carrier gate's scope",
      art_fm.get("created", "") == "2026-08-17")
check("A08 scripts names this probe and depends_on names the predeclaration "
      "and both receipts",
      "joe_directed_b1p1_three_corner_support_prices_the_chiral_grant.py"
      in art_text and LEG_A_REL in art_text
      and "canon/escape-corners-campaign-RESULTS.md" in art_text
      and "tests/escape-corners/lega1_flipped_chiral_adjudication.md"
      in art_text)
live_blocks = gate.FENCE_RE.findall(art_text) if gate is not None else []
check("A09 exactly one live gu-typed-objects block", len(live_blocks) == 1)
check("A10 the live block validates clean",
      len(live_blocks) == 1 and gate is not None
      and gate.validate_block(live_blocks[0])[0] == [])
check("A11 the artifact prints all three proposed diffs as PROPOSED, "
      "not applied",
      "PROPOSED diff A" in art_text and "PROPOSED diff B" in art_text
      and "PROPOSED source-register diff" in art_text
      and "NOT applied" in art_text)
check("A12 the artifact states the coupling rule and its proposed location",
      "Adverse-Mechanism News Fires the Hedge-Watch" in art_text
      and "lab/methods/claim-status-consistency.md" in art_text)

r_ct1 = subprocess.run([sys.executable, str(ROOT / CT1_REL)],
                       cwd=str(ROOT), capture_output=True, text=True)
check("G01 CT-1's probe still exits 0 after the two methods edits, and says "
      "so on its own certificate line (rule 7: read the catches, not the "
      "summary)",
      r_ct1.returncode == 0 and "CERTIFICATE:" in r_ct1.stdout
      and "[FAIL]" not in r_ct1.stdout and "  FAIL" not in r_ct1.stdout)
r_gate = subprocess.run([sys.executable, str(ROOT / GATE_REL), "--selftest"],
                        cwd=str(ROOT), capture_output=True, text=True)
check("G02 the typed-carrier gate --selftest is GREEN (the codomain triangle "
      "survives the edits)",
      r_gate.returncode == 0 and "SELF-TEST GREEN" in r_gate.stdout)
if gate is not None and art_text and ref_text:
    code_new, stats_new = gate.audit(paths=[str(ROOT / REF_REL),
                                            str(ROOT / ART_REL)])
    check("G03 the reference and this artifact audit green in dated scope "
          "(scope 2, red 0)",
          code_new == 0 and stats_new["scope"] == 2 and stats_new["red"] == 0)
    check("G04 the reference stays UNTRIGGERED and the artifact is triggered "
          "with its one block",
          stats_new["triggered"] == 1 and stats_new["blocks"] == 1)
    check("G05 codomain drift is zero against the edited reference",
          stats_new.get("codomain_drift") == 0)

    def _no_float(obj) -> bool:
        if isinstance(obj, float):
            return False
        if isinstance(obj, dict):
            return all(_no_float(k) and _no_float(v) for k, v in obj.items())
        if isinstance(obj, (list, tuple, set)):
            return all(_no_float(x) for x in obj)
        return True

    check("G06 no float anywhere in the result surface (swept)",
          _no_float(stats_new) and _no_float(VERTEX) and _no_float(SUPPORT))
else:
    for gid in ("G03", "G04", "G05", "G06"):
        check(gid + " (gate or files unavailable)", False)


# ======================================================================
# certificate / selftest driver
# ======================================================================
def main() -> int:
    total = PASS + FAIL
    print("CERTIFICATE: %d/%d checks pass; %d planted-false propositions "
          "observed true; 2 contrary controls PASS; 4 planted-positive "
          "controls across 3 detectors fire; no load-bearing float (swept)."
          % (PASS, total, PLANTED_OBSERVED_TRUE))
    return 0 if FAIL == 0 else 1


def selftest(poison: bool) -> int:
    env = dict(os.environ)
    env.pop("B1P1_MUTATE", None)
    if poison:
        env["B1P1_MUTATE"] = "ref-gone"
    base = subprocess.run([sys.executable, __file__], cwd=str(ROOT), env=env,
                          capture_output=True, text=True)
    if base.returncode != 0:
        print("SELFTEST: clean baseline does NOT pass; mutations were NOT run")
        print("SELFTEST FAILED")
        return 1
    print("SELFTEST: clean baseline verified first (exit 0, certificate "
          "printed); running mutations")
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ)
        env["B1P1_MUTATE"] = m
        r = subprocess.run([sys.executable, __file__], cwd=str(ROOT), env=env,
                           capture_output=True, text=True)
        completed = "CERTIFICATE:" in r.stdout
        genuine = "[FAIL]" in r.stdout
        caught = r.returncode == 1 and completed and genuine
        label = ("caught (exit 1, genuine [FAIL], certificate printed)"
                 if caught else "MISSED" if r.returncode == 0 else
                 "CRASH-NOT-DETECTION (no certificate line)")
        print("  mutation %-28s %s" % (m, label))
        ok = ok and caught
    print("SELFTEST " + ("GREEN: clean baseline first, then %d/%d "
                         "machinery/reference mutations each exit 1 via a "
                         "genuine [FAIL] line"
                         % (len(MUTATIONS), len(MUTATIONS))
                         if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest(poison="--poison" in sys.argv))
    sys.exit(main())
