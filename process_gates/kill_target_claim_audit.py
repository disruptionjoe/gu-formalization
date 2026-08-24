#!/usr/bin/env python3
"""Kill-target-claim audit (ratified, Joe direct chat 2026-08-11).

Every NEW kill/no-go-bearing artifact must name the source claim it kills,
by ID, from lab/sources/source-claim-register.yaml — or declare itself not
a kill. Rationale and council conditions:
explorations/source-claim-register-and-adherence-ledger-2026-08-11.md.

Scope (fail-closed, non-retroactive): explorations/**/*.md with frontmatter
`created:` >= 2026-08-12. Trigger: kill-language in the frontmatter title/
result/status fields. Requirement: frontmatter key `target_claim:` listing
register IDs (SC-AREA-NN) or the audited escape hatch NONE-NOT-A-KILL.
Also flagged: trigger-matching artifacts quoting the draft/transcripts
(page/timestamp cite patterns) with no register ID anywhere (quote-without-
locus). Escape-hatch uses are counted and reported every run; sustained
zero-red with zero hatch abuse is the documented retirement condition.
Self-test: --self-test runs planted pass/fail controls and exits nonzero
if any control misbehaves.

LEDGER EXTENSION (2026-08-13, Joe direct chat). The gate originally read
exploration frontmatter only, so the conditional-physics ledger sat
entirely outside enforcement. A sweep on 2026-08-13 found 0 of 84 rows
naming any register ID. Under this gate's kill-language trigger that is
8 untyped kill-bearing rows, including all three GENUINE_FALSIFICATION
verdicts (RA-D2, LT-GR1b, AC-F3). A broader OVER_DETERMINED sweep counts
11; the extra 3 are superseded-premise rows, not kills. That is how
RA-D2, our strongest negative verdict type, came to target a claim the
source never made.

Ledger rows carry no creation date, so a date cutoff is unavailable.
The gate therefore ratchets: LEDGER_BASELINE records the untyped
kill-bearing count at extension time, the audit RED-fails if the count
rises above it, and the baseline is lowered as rows are typed. Rows name
their target by adding a `target_claim` field (register IDs, or the same
NONE-NOT-A-KILL hatch). Retirement condition: baseline reaches 0.

CLAIM-AFFINITY EXTENSION (2026-08-24). Source-mechanism results can bear on a
registered claim without using kill vocabulary, so the red/green trigger above
cannot see them. A dated artifact may declare `bears_on: SC-AREA-NN`; this
gate prints known claim links and WARNs on missing or unknown IDs. Affinity is
deliberately warn-only: it improves adherence routing and never turns a work
queue into a kill-gate failure.
"""
import re, sys, glob, os, datetime, json, io, contextlib

REG = "lab/sources/source-claim-register.yaml"
LEDGER_GLOB = "lab/process/conditional-physics-ledger-v0.*.json"
# Untyped kill-bearing rows at extension time (2026-08-13). Lower this as
# rows are typed; never raise it to make a red go green.
# 2026-08-23: driven to 0 -- all kill-bearing rows are now typed. Seven of the
# eight name NONE-NOT-A-KILL because they kill comparator routes, repo-selected
# candidates, or readings the source disavows; only RA-D2 engages a registered
# source claim (SC-CHI-51), and there the claim survives a bounded realization
# exclusion. This is the gate's documented retirement condition.
LEDGER_BASELINE = 0
# Reds present when scope was widened from `explorations/` to the whole repo
# (2026-08-14).  These are pre-existing, owned elsewhere, and enumerated in the
# control-change record.  Never raise this to make a new red go green.
SCOPE_BASELINE = 3
CUTOFF = "2026-08-12"
# House style writes results both in prose ("route killed") and in
# UNDERSCORE_CAPS tokens ("..._ROUTE_KILLED"); underscores are word chars,
# so plain \b misses the token form — hence the (?:\b|_) guards.
TRIGGER = re.compile(r"(?:\b|_)(kill(?:ed|s)?|no[-_ ]?go|falsifi\w+|dead|fatal)(?:\b|_)", re.I)
CLAIM_ID = re.compile(r"SC-[A-Z]+-\d+")
QUOTE_CITE = re.compile(r"\bp\.\s?\d{1,3}\b|\b\d{2}:\d{2}:\d{2}\b")
HATCH = "NONE-NOT-A-KILL"

def frontmatter(text):
    if not text.startswith("﻿") and not text.startswith("---"):
        return {}
    parts = text.lstrip("﻿").split("---")
    if len(parts) < 3:
        return {}
    fm = {}
    for line in parts[1].splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm

def register_ids():
    try:
        return set(CLAIM_ID.findall(open(REG).read()))
    except OSError:
        return None

# Scope is DERIVED FROM CONVENTION, not enumerated.  A claim-bearing artifact
# in this repo is a markdown file with dated YAML frontmatter; the `created`
# cutoff below does the real filtering.  Enumerating directories is what let
# `lab/active-research/joe-directed/` escape this gate entirely on 2026-08-14 --
# a namespace created after the gate shipped.  Any new namespace is now in
# scope automatically.
VENDOR = ("_local/", ".lake/", "node_modules/", "__pycache__/", ".git/")


def scan_set():
    return [f for f in glob.glob("**/*.md", recursive=True)
            if not any(v in f for v in VENDOR)]


def coverage():
    """Register coverage is the CEILING on what this gate can catch: it only
    sees disavowals that are registered.  Emit the count so Observation can
    sense a coverage gap rather than reading a green scan as safety."""
    try:
        text = open(REG).read()
    except OSError:
        return None
    # Count ROWS, not mentions: the rules block and the adjudication headline
    # both contain the phrase, and an inflated coverage number is exactly the
    # kind of vacuous reassurance this control exists to prevent.
    return len(re.findall(r"^\s+core:\s*disavowed-by-source\s*$", text, re.M))


def audit(paths=None, baseline=None):
    # `baseline` is injectable for the same reason audit_ledger's already is:
    # SELF-TEST VACUITY.  SCOPE_BASELINE was added 2026-08-14 for the repo-wide
    # scope widening, and it silently absorbed the self-test's two planted
    # reds -- the harness asserted exit 1 and got 0, so the gate's own
    # failure-path check has been FAILING since that commit, unnoticed because
    # normal runs never invoke --self-test.  A tolerance that swallows planted
    # controls makes the control vacuous, which is the precise defect this
    # gate family exists to detect.  The self-test now pins baseline=0.
    baseline = SCOPE_BASELINE if baseline is None else baseline
    ids = register_ids()
    if ids is None:
        print("RED kill_target_claim_audit: register missing at " + REG)
        return 1, 0
    red, hatch_uses, internal_targets = [], 0, 0
    affinities, affinity_warn = [], []
    for f in paths or scan_set():
        try:
            text = open(f, encoding="utf-8").read()
        except OSError:
            continue
        fm = frontmatter(text)
        created = fm.get("created", "")
        if not created or created < CUTOFF:
            continue
        bears_on = fm.get("bears_on", "")
        if bears_on:
            named_affinity = set(CLAIM_ID.findall(bears_on))
            unknown_affinity = named_affinity - ids
            if not named_affinity:
                affinity_warn.append((f, "bears_on carries no SC- claim id"))
            elif unknown_affinity:
                affinity_warn.append((
                    f, "bears_on names unknown claim ids: "
                    + ",".join(sorted(unknown_affinity))))
            for claim_id in sorted(named_affinity & ids):
                affinities.append((f, claim_id))
        head = " ".join(fm.get(k, "") for k in ("title", "result", "status", "doc_type"))
        if not TRIGGER.search(head):
            continue
        target = fm.get("target_claim", "")
        if HATCH in target:
            hatch_uses += 1
            continue
        # INTERNAL-TARGET FORM (2026-08-15).  The gate assumed every kill either
        # targets a registered SOURCE claim or is not a kill.  LA-10 is a third
        # thing the channel now produces routinely: a kill aimed at a
        # repository-internal claim -- here its own channel's published
        # headline.  Forcing it onto the NONE-NOT-A-KILL hatch would make it
        # assert something false (it IS a kill), and inventing an SC- id would
        # be the unsourced attribution this gate exists to prevent.
        #
        # This form is deliberately HARDER to satisfy than the hatch, which
        # demands nothing: it requires a named target AND a recorded verdict
        # against it, so an internal kill must state what happened to its
        # target.  Counted and printed separately -- an internal kill is not
        # evidence about the source, and must never be summarised as one.
        if target and fm.get("target_claim_verdict", "") and not CLAIM_ID.search(target):
            internal_targets += 1
            continue
        named = set(CLAIM_ID.findall(target))
        if not named:
            red.append((f, "kill-language with no target_claim"))
            continue
        unknown = named - ids
        if unknown:
            red.append((f, "unknown claim ids: " + ",".join(sorted(unknown))))
            continue
        if QUOTE_CITE.search(text) and not CLAIM_ID.search(text.split("---", 2)[-1]) and not named:
            red.append((f, "source quotes without register locus"))
    for f, why in red:
        print(f"RED  {f}: {why}")
    for f, why in affinity_warn:
        print(f"WARN {f}: {why}")
    cov = coverage()
    print(f"kill_target_claim_audit: {len(red)} red "
          f"(scope baseline {baseline}), escape-hatch uses this scan: {hatch_uses}, "
          f"internal-target kills: {internal_targets}")
    print(f"kill_target_claim_audit[coverage]: {cov} disavowed-by-source rows in register; "
          f"{len(paths or scan_set())} markdown files in derived scope. "
          f"A green scan bounds only the REGISTERED class.")
    claims = sorted({claim_id for _f, claim_id in affinities})
    print(f"kill_target_claim_audit[affinity]: {len(affinities)} typed links "
          f"across {len(claims)} registered claims; {len(affinity_warn)} "
          f"warn-only defects. claims={','.join(claims) if claims else 'none'}")
    return (1 if len(red) > baseline else 0), hatch_uses

def latest_ledger(pattern=None):
    paths = glob.glob(pattern or LEDGER_GLOB)
    if not paths:
        return None
    # numeric sort: v0.29 is older than v0.236, lexical sort gets this wrong
    return max(paths, key=lambda p: int(re.search(r"v0\.(\d+)", p).group(1)))

def audit_ledger(pattern=None, baseline=None):
    """Ratchet: kill-bearing ledger rows that name no register claim.

    RED if the untyped count exceeds the recorded baseline. Reports the
    offending row ids every run so the baseline can be driven to zero.
    """
    baseline = LEDGER_BASELINE if baseline is None else baseline
    path = latest_ledger(pattern)
    if not path:
        print("RED kill_target_claim_audit[ledger]: no ledger found at " + (pattern or LEDGER_GLOB))
        return 1
    try:
        data = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"RED kill_target_claim_audit[ledger]: unreadable {path}: {exc}")
        return 1
    rows = data if isinstance(data, list) else data.get("rows", data.get("claims", []))
    untyped = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        blob = json.dumps(r)
        if not TRIGGER.search(blob):
            continue
        target = str(r.get("target_claim", ""))
        if HATCH in target:
            continue
        if not CLAIM_ID.search(blob):
            untyped.append(r.get("id", "?"))
    status = "RED " if len(untyped) > baseline else "ok  "
    print(f"{status}kill_target_claim_audit[ledger]: {len(untyped)} untyped kill-bearing rows "
          f"(baseline {baseline}) in {os.path.basename(path)}")
    if untyped:
        print("     untyped: " + ", ".join(sorted(untyped)))
    if len(untyped) < baseline:
        print(f"     NOTE baseline can be lowered to {len(untyped)}")
    return 1 if len(untyped) > baseline else 0

def self_test():
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "explorations"))
        os.makedirs(os.path.join(d, "lab", "sources"))
        cwd = os.getcwd()
        os.chdir(d)
        try:
            open(REG, "w").write("claims:\n- id: SC-TEST-01\n")
            cases = {
                "pass_typed.md": ("---\ntitle: route killed\ncreated: 2026-09-01\n"
                                  "target_claim: SC-TEST-01\n---\nbody"),
                "pass_hatch.md": ("---\ntitle: killed route summary\ncreated: 2026-09-01\n"
                                  "target_claim: NONE-NOT-A-KILL\n---\nbody"),
                "pass_old.md":   ("---\ntitle: killed\ncreated: 2026-01-01\n---\nbody"),
                "fail_untyped.md": ("---\ntitle: route killed\ncreated: 2026-09-01\n---\nbody"),
                "fail_unknown.md": ("---\ntitle: no-go filed\ncreated: 2026-09-01\n"
                                    "target_claim: SC-FAKE-99\n---\nbody"),
                # Controls for the internal-target form.  The FAIL case is the
                # load-bearing one: it proves the new path does not wave through
                # any non-SC target string, only one carrying a verdict.
                "pass_internal.md": ("---\ntitle: route killed\ncreated: 2026-09-01\n"
                                     "target_claim: CHANNEL-HEADLINE-X\n"
                                     "target_claim_verdict: PARTIALLY_BROKEN\n---\nbody"),
                "fail_internal_noverdict.md": ("---\ntitle: route killed\n"
                                     "created: 2026-09-01\n"
                                     "target_claim: CHANNEL-HEADLINE-X\n---\nbody"),
                "pass_affinity.md": ("---\ntitle: source mechanism result\n"
                                     "created: 2026-09-01\n"
                                     "bears_on: SC-TEST-01\n---\nbody"),
                "warn_affinity_unknown.md": ("---\ntitle: source mechanism result\n"
                                     "created: 2026-09-01\n"
                                     "bears_on: SC-FAKE-99\n---\nbody"),
                "warn_affinity_untyped.md": ("---\ntitle: source mechanism result\n"
                                     "created: 2026-09-01\n"
                                     "bears_on: source mechanism\n---\nbody"),
            }
            for name, content in cases.items():
                open(os.path.join("explorations", name), "w").write(content)
            code, hatches = audit(baseline=0)
            ok = (code == 1) and (hatches == 1)
            # 3 reds now: fail_untyped, fail_unknown, fail_internal_noverdict.
            _c, _h = audit(baseline=2)
            ok = ok and (_c == 1)   # the no-verdict internal kill IS caught
            out = []
            affinity_out = io.StringIO()
            with contextlib.redirect_stdout(affinity_out):
                code2, _ = audit(baseline=0, paths=[
                    os.path.join("explorations", "pass_typed.md"),
                    os.path.join("explorations", "pass_hatch.md"),
                    os.path.join("explorations", "pass_old.md"),
                    os.path.join("explorations", "pass_affinity.md"),
                    os.path.join("explorations", "warn_affinity_unknown.md"),
                    os.path.join("explorations", "warn_affinity_untyped.md")])
            affinity_text = affinity_out.getvalue()
            ok = ok and (code2 == 0)
            ok = ok and "1 typed links across 1 registered claims" in affinity_text
            ok = ok and affinity_text.count("WARN ") == 2

            # ---- ledger-extension controls
            os.makedirs(os.path.join("lab", "process"), exist_ok=True)
            lg = "lab/process/conditional-physics-ledger-v0.%d.json"
            # numeric-vs-lexical sort control: v0.9 must NOT win over v0.10
            open(lg % 9, "w").write(json.dumps([
                {"id": "OLD-1", "verdict": "OVER_DETERMINED",
                 "reason_kind": "GENUINE_FALSIFICATION", "summary": "stale file, must be ignored"}]))
            open(lg % 10, "w").write(json.dumps([
                {"id": "TYPED-1", "verdict": "OVER_DETERMINED",
                 "reason_kind": "GENUINE_FALSIFICATION", "target_claim": "SC-TEST-01"},
                {"id": "HATCH-1", "reason_kind": "ROUTE_KILLED",
                 "target_claim": HATCH},
                {"id": "UNTYPED-1", "verdict": "OVER_DETERMINED",
                 "reason_kind": "GENUINE_FALSIFICATION", "summary": "names nothing"},
                {"id": "CLEAN-1", "verdict": "SAME", "reason_kind": "DERIVED"}]))
            picked = latest_ledger("lab/process/conditional-physics-ledger-v0.*.json")
            ok = ok and picked.endswith("v0.10.json")           # numeric sort held
            ok = ok and audit_ledger(baseline=1) == 0           # at baseline: green
            ok = ok and audit_ledger(baseline=0) == 1           # over baseline: red
            ok = ok and audit_ledger(baseline=5) == 0           # under baseline: green
            ok = ok and audit_ledger(pattern="lab/process/nonexistent-*.json") == 1
        finally:
            os.chdir(cwd)
    print("SELF-TEST " + ("GREEN" if ok else "FAILED"))
    return 0 if ok else 1

if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    code, _ = audit()
    code |= audit_ledger()
    sys.exit(code)
