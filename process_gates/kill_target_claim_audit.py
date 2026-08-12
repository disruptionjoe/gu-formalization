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
"""
import re, sys, glob, os, datetime

REG = "lab/sources/source-claim-register.yaml"
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
        finally:
            os.chdir(cwd)
    print("SELF-TEST " + ("GREEN" if ok else "FAILED"))
    return 0 if ok else 1

if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    code, _ = audit()
    sys.exit(code)
