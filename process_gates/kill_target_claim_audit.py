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
"""
import re, sys, glob, os, datetime, json

REG = "lab/sources/source-claim-register.yaml"
LEDGER_GLOB = "lab/process/conditional-physics-ledger-v0.*.json"
# Untyped kill-bearing rows at extension time (2026-08-13). Lower this as
# rows are typed; never raise it to make a red go green.
LEDGER_BASELINE = 8
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

def audit(paths=None):
    ids = register_ids()
    if ids is None:
        print("RED kill_target_claim_audit: register missing at " + REG)
        return 1, 0
    red, hatch_uses = [], 0
    for f in paths or glob.glob("explorations/**/*.md", recursive=True):
        try:
            text = open(f, encoding="utf-8").read()
        except OSError:
            continue
        fm = frontmatter(text)
        created = fm.get("created", "")
        if not created or created < CUTOFF:
            continue
        head = " ".join(fm.get(k, "") for k in ("title", "result", "status", "doc_type"))
        if not TRIGGER.search(head):
            continue
        target = fm.get("target_claim", "")
        if HATCH in target:
            hatch_uses += 1
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
    print(f"kill_target_claim_audit: {len(red)} red, escape-hatch uses this scan: {hatch_uses}")
    return (1 if red else 0), hatch_uses

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
            }
            for name, content in cases.items():
                open(os.path.join("explorations", name), "w").write(content)
            code, hatches = audit()
            ok = (code == 1) and (hatches == 1)
            out = []
            code2, _ = audit([os.path.join("explorations", "pass_typed.md"),
                              os.path.join("explorations", "pass_hatch.md"),
                              os.path.join("explorations", "pass_old.md")])
            ok = ok and (code2 == 0)

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
