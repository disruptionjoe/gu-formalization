#!/usr/bin/env python3
"""Typed-carrier-declaration audit (FX-2, joe-directed brief 2026-08-16).

AGENTS.md already requires, verbatim: "State the carrier, pairing or form,
real structure, grading, action owner, target object, assumptions, controls,
and claim ceiling for a new result."  Nothing enforced it.  That is how
`Omega^1(S)` was written without saying which `S` (CN-2 found 13 declaration
sites, none typed), how an algebra-vs-module domain error inverted an answer
one hop from its canonical owner (BD-A: `6 of 15` on the algebra vs `12 of 12`
on the module, same group, same d), how two Lorentz subalgebras intersecting
in zero wore one name (SA-1: `so(1,3)_endo` vs `so(1,3)_H`), how a contraction
was retyped as a projection inside a mandatory method boundary (the withdrawn
clause in lab/methods/source-native-comparator-routing.md), and how the word
"observer" -- the action owner -- dropped out of a relay (base-duality README,
"The relay defect, located to one word").  Design record and the five-error
acceptance test: lab/active-research/joe-directed/carrier-decl/
fx2-typed-carrier-declaration-2026-08-16.md.  This gate is a process artifact
produced under a directed brief; it is NOT chat-ratified and says so.

Scope (fail-closed, non-retroactive; modelled on kill_target_claim_audit.py):
every markdown file with dated YAML frontmatter `created:` >= 2026-08-17.
Scope is DERIVED FROM CONVENTION, not enumerated -- the donor gate's lesson:
enumerating directories is what let a post-hoc namespace escape entirely.
Nothing existing goes red: the cutoff is tomorrow relative to the build date,
so today's checkout is a clean baseline by construction, and the probe asserts
it (0 triggered artifacts at ship time).

Trigger (does this artifact STATE a mathematical result?), any of:
  (a) a certificate line -- an `N/N` equal-count plus `exit 0`/`checks` on one
      line, the house certificate shape ("105/105 checks pass ... exit 0");
  (b) a `scripts:` frontmatter key referencing `tests/` (a probe reference);
  (c) a result-bearing `doc_type` (result/construction/certificate/theorem/
      proof/classifier/census/crosswalk/determination/no-go/delta/gate);
  (d) a `grade:` frontmatter field declaring EXACT arithmetic.
WHAT THE TRIGGER MISSES, stated rather than implied: a result asserted in
prose with none of the four signals is invisible (same ceiling as the donor
gate's kill-language trigger); non-markdown surfaces (JSON ledgers, probe
docstrings) are out of scope; a file with no `created:` field is out of scope
entirely.  A QUOTED certificate ("LA-8, 78/78, exit 0" cited in a read
packet) FALSE-TRIGGERS by design; the audited exemption is the pressure
valve, and every use of it is printed.

Requirement: at least one machine-readable typed-objects block, fenced as
```gu-typed-objects, with exactly these keys:

    result:         which result this block types (never UNTYPED -- a block
                    that binds nothing is boilerplate)
    carrier:        the object the result lives on, WITH `LAYER=` (ambient /
                    observed / source-print / toy / UNTYPED; a mixed layer
                    `a+b` REQUIRES `BRIDGE=<named map>`) and WITH
                    `CHIRALITY=` from CN-2's closed vocabulary (S-FULL-DIRAC
                    / S-HALF-OPPOSITE / S-HALF-SAME / S-CHIRALITY-UNTYPED)
                    or N/A for spinor-free carriers
    pairing:        the form/pairing WITH `ON=<what it lives on>`, or NONE,
                    or UNTYPED  (the BD-A slot: algebra or module is decided
                    by what you write after ON=)
    real_structure: or N/A or UNTYPED
    grading:        or N/A or UNTYPED
    action_owner:   who supplies/owns the object -- source-action / observer /
                    repository-construction / comparator / source-print / N/A
                    / UNTYPED  (the relay slot: the word that dropped)
    target:         the object/codomain the result is about, WITH
                    `MAP-TYPE=` from a closed vocabulary (projection,
                    contraction, ... , not-a-map, UNTYPED)  (the slot that
                    separates a projection from a contraction)

REGISTERED HOMONYMS (`so(1,3)`, `so(3,1)`, `ad(P_H)` -- seeded from this
week's actual collisions) may not appear bare in carrier/pairing/target: they
need a subscript (`so(1,3)_endo`) or the explicit token HOMONYM-AMBIGUOUS.
If lab/process/ later grows a homonym registry (owned by another lane), it
should supersede this constant; this gate deliberately does not read files
another agent is concurrently creating.

CN-2 PRINCIPLE, load-bearing: a site can comply by DECLARING its ambiguity.
UNTYPED / S-CHIRALITY-UNTYPED / HOMONYM-AMBIGUOUS are always legal, always
counted, and printed every run.  A block with every object slot UNTYPED is
named per-path as ALL-UNTYPED -- visible, not red.  Making honesty red would
train plausible-token lying, which is strictly worse than a declared gap.

Escape hatch, audited (the NONE-NOT-A-KILL pattern): a prose-only artifact
(index, disposition, read packet) declares frontmatter
`typed_objects: EXEMPT-PROSE-ONLY`.  Uses are counted and path-printed every
run.  Any OTHER value of `typed_objects:` is red (unregistered exemption).
The hatch is DISALLOWED where it would be self-contradictory: a doc_type that
itself declares a result (result/construction/certificate/theorem/proof)
cannot simultaneously claim to state none.

Baseline is 0 and injectable; the self-test pins baseline=0 -- the donor
gate's SELF-TEST VACUITY lesson (a tolerance that swallows planted controls
makes the control vacuous).  Parser hardening over the donor: `created:`
values are unquoted before the date compare (a quoted "2026-09-01" lexically
precedes "2" and would silently leave scope).

Self-test: --selftest (also --self-test) builds fixtures, verifies the CLEAN
BASELINE exits 0 BEFORE any mutation, then plants false facts -- a missing
field, a mixed-layer carrier without a declared bridge, an unregistered
exemption, and seven more -- each required to drive exit 1; exits 0 iff all
behave.  --selftest --poison-baseline corrupts the clean set to prove the
baseline guard itself has power (prints the refusal and exits 1).

CODOMAIN WIRING (CT-1, 2026-08-17): the LAYER= and MAP-TYPE= vocabularies are
canonically stated in lab/methods/gu-base-categories.md; every audit run
cross-checks this module's token constants against that reference's
gu-token-codomain block and reds on drift (fail-closed if the reference is
missing).  The self-test plants a mismatched and a missing reference and
requires both to be caught.
"""

import glob
import os
import re
import sys

CUTOFF = "2026-08-17"
BASELINE = 0  # nothing existing is in scope; never raise this to green a red
VENDOR = ("_local/", ".lake/", "node_modules/", "__pycache__/", ".git/")

FENCE_RE = re.compile(r"^```gu-typed-objects[ \t]*\n(.*?)^```", re.M | re.S)
REQUIRED_KEYS = ("result", "carrier", "pairing", "real_structure", "grading",
                 "action_owner", "target")
OBJECT_KEYS = ("carrier", "pairing", "real_structure", "grading",
               "action_owner", "target")
UNTYPED = "UNTYPED"

# CN-2's closed four-value chirality vocabulary, verbatim, plus N/A for
# spinor-free carriers.  Reusing it rather than inventing a rival is the
# point: one vocabulary, one census.
CHIRALITY_TOKENS = ("S-FULL-DIRAC", "S-HALF-OPPOSITE", "S-HALF-SAME",
                    "S-CHIRALITY-UNTYPED", "N/A")
# CODOMAIN (CT-1, 2026-08-17): LAYER_TOKENS and MAP_TOKENS are this gate's
# working copies of vocabularies whose canonical statement lives in
# lab/methods/gu-base-categories.md (Carrier-category objects/markers for
# LAYER, arrow labels for MAP-TYPE).  audit() cross-checks both sets against
# that reference's `gu-token-codomain` block every run and REDS on any drift,
# in either direction, so the two surfaces cannot diverge silently.
# CHIRALITY_TOKENS' codomain owner remains CN-2 and OWNER_TOKENS' remains the
# FX-2 design record (stated in the reference §3.4); neither is wired here.
LAYER_TOKENS = ("ambient", "observed", "source-print", "toy", UNTYPED)
OWNER_TOKENS = ("source-action", "observer", "repository-construction",
                "comparator", "source-print", "N/A", UNTYPED)
MAP_TOKENS = ("projection", "contraction", "inclusion", "restriction",
              "pullback", "pushforward", "quotient", "isomorphism",
              "homomorphism", "intertwiner", "evaluation", "not-a-map",
              UNTYPED)
REFERENCE_REL = "lab/methods/gu-base-categories.md"
REFERENCE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              os.pardir, "lab", "methods",
                              "gu-base-categories.md")
CODOMAIN_FENCE_RE = re.compile(r"^```gu-token-codomain[ \t]*\n(.*?)^```",
                               re.M | re.S)


def codomain_drift(path=None):
    """Compare LAYER_TOKENS/MAP_TOKENS against the base-category reference.

    Returns a list of drift descriptions; empty means the two surfaces agree.
    Fails closed: a missing reference, a missing block or a missing line is
    drift.  Reads the module constants (not the source text) so a runtime
    mutation of either surface is also caught.
    """
    path = REFERENCE_PATH if path is None else path
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return ["codomain reference missing: " + REFERENCE_REL]
    m = CODOMAIN_FENCE_RE.search(text)
    if not m:
        return ["codomain reference has no gu-token-codomain block"]
    declared = {}
    for line in m.group(1).splitlines():
        lm = re.match(r"^([a-z-]+):\s*(.*)$", line)
        if lm:
            declared[lm.group(1)] = tuple(lm.group(2).split())
    drift = []
    for key, tokens in (("layer-tokens", LAYER_TOKENS),
                        ("map-type-tokens", MAP_TOKENS)):
        ref = declared.get(key)
        if ref is None:
            drift.append("codomain reference missing line: " + key)
        elif len(ref) != len(set(ref)):
            drift.append("codomain reference duplicates tokens on " + key)
        elif set(ref) != set(tokens):
            drift.append("codomain drift on %s: gate=%s reference=%s"
                         % (key, sorted(tokens), sorted(ref)))
    return drift
HOMONYMS = ("so(1,3)", "so(3,1)", "ad(P_H)")
HOMONYM_ESCAPE = "HOMONYM-AMBIGUOUS"

HATCH = "EXEMPT-PROSE-ONLY"
# doc_types whose NAME declares a result: the prose-only hatch on these is a
# self-contradiction and is red.  Deliberately narrower than the trigger.
HATCH_FORBIDDEN_DOCTYPE = re.compile(
    r"(result|construction|certificate|theorem|proof)(?:\b|_)", re.I)

TRIGGER_DOCTYPE = re.compile(
    r"(result|construction|certificate|theorem|proof|classifier|census|"
    r"crosswalk|determination|no[-_ ]?go|delta|gate)(?:\b|_)", re.I)
# N/N with equal numerator/denominator plus exit 0 / checks on the same line:
# the house certificate shape.  \1 makes 105/106 not match.
CERT_LINE = re.compile(r"^.*\b(\d+)/\1\b.*(exit\s*0|\bchecks?\b).*$", re.M)
SCRIPTS_TESTS = re.compile(r"^scripts:|^\s+-\s+tests/", re.M)
GRADE_EXACT = re.compile(r"\bEXACT\b")
SPINOR_RE = re.compile(r"\(S[+-]?\)|\bspinor", re.I)

LAYER_FIELD = re.compile(r"LAYER=([A-Za-z+\-]+)")
CHIRALITY_FIELD = re.compile(r"CHIRALITY=([A-Za-z0-9/\-]+)")
BRIDGE_FIELD = re.compile(r"BRIDGE=(\S+)")
ON_FIELD = re.compile(r"\bON=(\S+)")
MAPTYPE_FIELD = re.compile(r"MAP-TYPE=([A-Za-z\-]+)")


def frontmatter(text):
    """Line-based key: value map plus the raw frontmatter text."""
    if not text.startswith("﻿") and not text.startswith("---"):
        return {}, ""
    parts = text.lstrip("﻿").split("---")
    if len(parts) < 3:
        return {}, ""
    fm = {}
    for line in parts[1].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, parts[1]


def unquote(value):
    return value.strip().strip('"').strip("'")


def scan_set():
    return [f for f in glob.glob("**/*.md", recursive=True)
            if not any(v in f for v in VENDOR)]


def trigger_reasons(fm, fm_raw, body):
    reasons = []
    if TRIGGER_DOCTYPE.search(fm.get("doc_type", "")):
        reasons.append("result-bearing doc_type")
    if CERT_LINE.search(body):
        reasons.append("certificate line")
    if SCRIPTS_TESTS.search(fm_raw):
        reasons.append("scripts probe reference")
    if GRADE_EXACT.search(fm.get("grade", "")):
        reasons.append("grade: EXACT")
    return reasons


def parse_block(block_text):
    """Return (fields dict, defects list) for one fenced block.

    Grammar is line-based: `key: value`, indented lines continue the previous
    key, `#` lines are comments.  Anything else is an UNPARSED-LINE defect --
    a block you cannot parse is a block that cannot be audited.
    """
    fields, defects, last_key = {}, [], None
    for n, line in enumerate(block_text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1] in (" ", "\t") and last_key:
            fields[last_key] += " " + line.strip()
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m:
            defects.append("UNPARSED-LINE:%d" % n)
            continue
        key, value = m.group(1), m.group(2).strip()
        if key not in REQUIRED_KEYS:
            defects.append("UNKNOWN-KEY:" + key)
            continue
        if key in fields:
            defects.append("DUP-KEY:" + key)
            continue
        fields[key] = value
        last_key = key
    return fields, defects


def validate_block(block_text):
    """Return (defects, untyped_slot_count, all_untyped_flag)."""
    fields, defects = parse_block(block_text)
    untyped = 0
    for key in REQUIRED_KEYS:
        if key not in fields:
            defects.append("MISSING:" + key)
        elif not fields[key]:
            defects.append("EMPTY:" + key)
    # result must bind: a block that names no result is boilerplate.
    result = fields.get("result", "")
    if result and result.split()[0] == UNTYPED:
        defects.append("RESULT-UNTYPED")

    carrier = fields.get("carrier", "")
    if carrier:
        lm = LAYER_FIELD.search(carrier)
        if not lm:
            defects.append("CARRIER-NO-LAYER")
        else:
            parts = lm.group(1).split("+")
            for p in parts:
                if p not in LAYER_TOKENS:
                    defects.append("CARRIER-BAD-LAYER:" + p)
            if len(parts) > 1 and not BRIDGE_FIELD.search(carrier):
                defects.append("MIXED-LAYER-NO-BRIDGE")
            if lm.group(1) == UNTYPED:
                untyped += 1
        cm = CHIRALITY_FIELD.search(carrier)
        if not cm:
            defects.append("CARRIER-NO-CHIRALITY")
        elif cm.group(1) not in CHIRALITY_TOKENS:
            defects.append("CARRIER-BAD-CHIRALITY:" + cm.group(1))
        else:
            if cm.group(1) == "S-CHIRALITY-UNTYPED":
                untyped += 1
            # a spinor-bundle carrier cannot declare chirality N/A: that is
            # the unsubscripted-S defect wearing a compliance token.
            carrier_object = CHIRALITY_FIELD.sub("", LAYER_FIELD.sub("", carrier))
            if cm.group(1) == "N/A" and SPINOR_RE.search(carrier_object):
                defects.append("SPINOR-CHIRALITY-NA")

    pairing = fields.get("pairing", "")
    if pairing and pairing not in ("NONE", UNTYPED):
        if not ON_FIELD.search(pairing):
            defects.append("PAIRING-NO-ON")

    owner = fields.get("action_owner", "")
    if owner and not any(owner.startswith(t) for t in OWNER_TOKENS):
        defects.append("OWNER-UNTOKENED")

    target = fields.get("target", "")
    if target:
        tm = MAPTYPE_FIELD.search(target)
        if not tm:
            defects.append("TARGET-NO-MAPTYPE")
        elif tm.group(1) not in MAP_TOKENS:
            defects.append("TARGET-BAD-MAPTYPE:" + tm.group(1))
        elif tm.group(1) == UNTYPED:
            untyped += 1

    for key in ("carrier", "pairing", "target"):
        value = fields.get(key, "")
        if HOMONYM_ESCAPE in value:
            untyped += 1
            continue
        for h in HOMONYMS:
            if re.search(re.escape(h) + r"(?![_\w])", value):
                defects.append("HOMONYM-BARE:%s:%s" % (h, key))

    untyped += sum(1 for k in OBJECT_KEYS
                   if fields.get(k, "").split()[:1] == [UNTYPED])
    all_untyped = bool(fields) and all(
        fields.get(k, "").split()[:1] == [UNTYPED] for k in OBJECT_KEYS)
    return defects, untyped, all_untyped


def audit(paths=None, baseline=None):
    baseline = BASELINE if baseline is None else baseline
    red, exemptions, all_untyped_paths = [], [], []
    scope = triggered = blocks_seen = untyped_slots = 0
    files = paths if paths is not None else scan_set()
    for f in files:
        try:
            text = open(f, encoding="utf-8").read()
        except OSError:
            continue
        fm, fm_raw = frontmatter(text)
        created = unquote(fm.get("created", ""))
        if not created or created < CUTOFF:
            continue
        scope += 1
        body = text.split("---", 2)[-1]
        reasons = trigger_reasons(fm, fm_raw, body)
        if reasons:
            triggered += 1
        blocks = FENCE_RE.findall(body)
        for b in blocks:
            blocks_seen += 1
            defects, untyped, is_all_untyped = validate_block(b)
            untyped_slots += untyped
            if is_all_untyped:
                all_untyped_paths.append(f)
            for d in defects:
                red.append((f, "typed-objects block defect " + d))
        hatch_value = unquote(fm.get("typed_objects", ""))
        hatch_ok = False
        if hatch_value:
            if hatch_value != HATCH:
                red.append((f, "unregistered exemption token: " + hatch_value))
            elif HATCH_FORBIDDEN_DOCTYPE.search(fm.get("doc_type", "")):
                red.append((f, "prose-only exemption on result-declaring "
                               "doc_type: " + fm.get("doc_type", "")))
            else:
                hatch_ok = True
                exemptions.append(f)
        if reasons and not blocks and not hatch_ok:
            red.append((f, "states a result (%s) with no gu-typed-objects "
                           "block and no registered exemption"
                        % ", ".join(reasons)))
    drift = codomain_drift()
    for why in drift:
        red.append((REFERENCE_REL, why))
    for f, why in red:
        print("RED  %s: %s" % (f, why))
    print("typed_carrier_declaration_audit: %d red (baseline %d); "
          "%d files in dated scope >= %s; %d triggered; %d blocks; "
          "%d exemptions" % (len(red), baseline, scope, CUTOFF, triggered,
                             blocks_seen, len(exemptions)))
    for f in exemptions:
        print("typed_carrier_declaration_audit[exemption]: " + f)
    print("typed_carrier_declaration_audit[untyped]: %d declared-ambiguous "
          "slots across %d blocks; ALL-UNTYPED blocks: %s"
          % (untyped_slots, blocks_seen,
             ", ".join(all_untyped_paths) if all_untyped_paths else "none"))
    print("typed_carrier_declaration_audit[trigger-ceiling]: the trigger "
          "reads declared metadata and certificate shapes only; a result "
          "stated in prose with none of the four signals is invisible. "
          "A green scan bounds only the SIGNALLED class.")
    print("typed_carrier_declaration_audit[codomain]: LAYER/MAP-TYPE token "
          "sets vs %s: %s" % (REFERENCE_REL,
                              "match" if not drift
                              else "%d drift red" % len(drift)))
    stats = {"red": len(red), "scope": scope, "triggered": triggered,
             "blocks": blocks_seen, "exemptions": list(exemptions),
             "untyped_slots": untyped_slots,
             "all_untyped": list(all_untyped_paths),
             "codomain_drift": len(drift)}
    return (1 if len(red) > baseline else 0), stats


VALID_BLOCK = """result: F-TEST minimal valid declaration
carrier: so(1,3)_endo inside so(7,7) LAYER=ambient CHIRALITY=N/A
pairing: Killing form ON=so(7,7)
real_structure: split real form
grading: Cartan k+p
action_owner: repository-construction (fixture)
target: invariant subspaces of k MAP-TYPE=restriction
"""

FIXTURES_CLEAN = {
    # triggered (doc_type + certificate line), fully typed block: green.
    "pass_full.md": ("---\ntitle: t\ncreated: 2026-09-01\n"
                     "doc_type: construction_result\n---\n"
                     "12/12 checks pass, exit 0\n\n"
                     "```gu-typed-objects\n" + VALID_BLOCK + "```\n"),
    # declared ambiguity everywhere it is legal: green, counted (CN-2).
    "pass_untyped_declared.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: classifier\n---\n"
        "```gu-typed-objects\n"
        "result: F-TEST declared-ambiguity control\n"
        "carrier: Omega^1(S) LAYER=UNTYPED CHIRALITY=S-CHIRALITY-UNTYPED\n"
        "pairing: UNTYPED\nreal_structure: UNTYPED\ngrading: UNTYPED\n"
        "action_owner: UNTYPED -- selector is action-owned and unbuilt\n"
        "target: observed content MAP-TYPE=UNTYPED\n```\n"),
    # prose artifact QUOTING a certificate (false-trigger) + registered hatch.
    "pass_hatch.md": ("---\ntitle: t\ncreated: 2026-09-01\n"
                      "doc_type: read_packet\ntyped_objects: EXEMPT-PROSE-ONLY\n"
                      "---\nquotes LA-8, 78/78, exit 0\n"),
    # pre-cutoff garbage: out of scope, green (non-retroactivity control).
    "pass_old.md": ("---\ntitle: t\ncreated: 2026-01-01\n"
                    "doc_type: construction_result\n---\n99/99 checks, exit 0\n"),
    # in scope, untriggered, no block: green.
    "pass_untriggered.md": ("---\ntitle: t\ncreated: 2026-09-01\n"
                            "doc_type: overview\n---\nprose only\n"),
    # quoted created date must still enter scope (donor-gate hardening).
    "pass_quoted_date.md": ('---\ntitle: t\ncreated: "2026-09-01"\n'
                            "doc_type: census\n---\n"
                            "```gu-typed-objects\n" + VALID_BLOCK + "```\n"),
}

FIXTURES_FAIL = {
    # the brief's three named planted facts:
    "fail_missing_field.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace("grading: Cartan k+p\n", "") + "```\n"),
    "fail_mixed_layer_no_bridge.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace("LAYER=ambient", "LAYER=ambient+observed")
        + "```\n"),
    "fail_unregistered_exemption.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: read_packet\n"
        "typed_objects: EXEMPT-BECAUSE-PROSE\n---\nprose\n"),
    # and the rest of the failure surface:
    "fail_no_block.md": ("---\ntitle: t\ncreated: 2026-09-01\n"
                         "doc_type: construction_result\n---\n"
                         "44/44 checks pass, exit 0\n"),
    "fail_bare_homonym.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace("so(1,3)_endo", "so(1,3)") + "```\n"),
    "fail_spinor_na.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace(
            "carrier: so(1,3)_endo inside so(7,7) LAYER=ambient CHIRALITY=N/A",
            "carrier: Omega^1(S) LAYER=ambient CHIRALITY=N/A") + "```\n"),
    "fail_pairing_no_on.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace("pairing: Killing form ON=so(7,7)",
                              "pairing: Killing form") + "```\n"),
    "fail_bad_maptype.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace("MAP-TYPE=restriction", "MAP-TYPE=squishing")
        + "```\n"),
    "fail_hatch_on_result_doctype.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "typed_objects: EXEMPT-PROSE-ONLY\n---\n7/7 checks, exit 0\n"),
    "fail_result_untyped.md": (
        "---\ntitle: t\ncreated: 2026-09-01\ndoc_type: construction_result\n"
        "---\n```gu-typed-objects\n"
        + VALID_BLOCK.replace("result: F-TEST minimal valid declaration",
                              "result: UNTYPED") + "```\n"),
}


def self_test(poison=False):
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as d:
        cwd = os.getcwd()
        os.chdir(d)
        try:
            for name, content in FIXTURES_CLEAN.items():
                open(name, "w", encoding="utf-8").write(content)
            if poison:
                # meta-control: prove the baseline guard has power.
                open("pass_full.md", "w", encoding="utf-8").write(
                    FIXTURES_FAIL["fail_no_block.md"])
            clean_paths = sorted(FIXTURES_CLEAN)
            code, stats = audit(paths=clean_paths, baseline=0)
            baseline_green = (
                code == 0
                and stats["scope"] == 5           # pass_old is out of scope
                and stats["triggered"] == 4       # full, untyped, hatch, quoted
                and stats["exemptions"] == ["pass_hatch.md"]
                and stats["untyped_slots"] == 7   # 6 slots + S-CHIRALITY-UNTYPED
                and stats["all_untyped"] == []    # owner has a qualifier, but
                )                                 # carrier/pairing/... count
            # NOTE all_untyped: pass_untyped_declared's six object slots all
            # begin with UNTYPED except carrier (a real object with UNTYPED
            # markers), so it is counted slot-wise, not ALL-UNTYPED.
            if not baseline_green:
                print("SELF-TEST: clean baseline does NOT pass; "
                      "mutations were NOT run")
                print("SELF-TEST FAILED")
                return 1
            # CT-1 codomain controls: the reference cross-check must be
            # green against the live reference, catch a planted mismatch,
            # and fail closed on a missing reference.
            if codomain_drift():
                ok = False
                print("SELF-TEST: codomain check red against the live "
                      "reference (must be green)")
            open("bad_reference.md", "w", encoding="utf-8").write(
                "```gu-token-codomain\nlayer-tokens: ambient observed\n"
                "map-type-tokens: projection\n```\n")
            if not codomain_drift("bad_reference.md"):
                ok = False
                print("SELF-TEST: planted codomain drift NOT caught")
            if not codomain_drift("no_such_reference.md"):
                ok = False
                print("SELF-TEST: missing codomain reference NOT caught")
            for name, content in FIXTURES_FAIL.items():
                open(name, "w", encoding="utf-8").write(content)
                code, _stats = audit(paths=[name], baseline=0)
                if code != 1:
                    ok = False
                    print("SELF-TEST: planted false fact NOT caught: " + name)
            # contrary controls: these must PASS despite smelling wrong.
            code, _stats = audit(paths=["pass_old.md"], baseline=0)
            ok = ok and code == 0            # pre-cutoff garbage stays green
            code, _stats = audit(paths=["pass_untyped_declared.md"], baseline=0)
            ok = ok and code == 0            # declared ambiguity is compliance
            # baseline injection must not be vacuous: at baseline 1 the
            # single-red missing-field fixture goes green.
            code, _stats = audit(paths=["fail_missing_field.md"], baseline=1)
            ok = ok and code == 0
        finally:
            os.chdir(cwd)
    print("SELF-TEST " + ("GREEN" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(self_test(poison="--poison-baseline" in sys.argv))
    exit_code, _ = audit()
    sys.exit(exit_code)
