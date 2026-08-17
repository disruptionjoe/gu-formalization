#!/usr/bin/env python3
"""Canonical-correction currency audit (CT-5, joe-directed CT-hardening wave).

WHAT THIS IS FOR
----------------
`process_gates/correction_propagation_audit.py` walks CITATION edges: if a file
cites a corrected owner, it must acknowledge the correction.  That gate is
sound and it stays exactly as it is.  But it has a REACHABILITY CEILING that no
amount of tuning removes:

    a document written BEFORE a correction existed never cites the
    correction's owner, so there is no edge to walk, so the citation gate
    cannot see it -- ever.

That is a proof, not a bug report.  It is also a real failure class: the Z/3
receptacle design packet (`explorations/z3-receptacle-design-packet-2026-08-11.md`)
engaged a route the following week's 2+1 sharpening superseded, cited nothing
that had been corrected, and no instrument in the repository could flag it.
SCUR-1 found that class by hand, over three days, with grep and judgement.

This gate makes the class MECHANICALLY DETECTABLE by propagating corrections
along CONSUMPTION edges instead of citation edges:

    a file is DIRTY for canonical correction K iff
        (1) its dated frontmatter is STRICTLY EARLIER than K.canonical_since
        (2) its text matches K's topic SIGNATURE
        (3) no recorded check in the sidecar clears it

The registry class is `canonical_source_corrections:` in
`lab/process/correction-registry.yaml` (a second top-level key, invisible to
the citation gate by construction).  The recorded checks are
`lab/process/canonical-currency-checks.yaml`.

GATE SEMANTICS -- deliberately asymmetric
-----------------------------------------
WARN-ONLY, every run, never red:
    the dirty set itself.  Every file, every correction, printed.
    This follows the FX-3 rule the hard way: a gate that goes RED on prose gets
    deleted, and a deleted gate detects nothing.  The dirty set is a WORK
    QUEUE, not a compliance target.

RED, and only these:
    (a) WELL-FORMEDNESS.  Registry and sidecar parse; every entry has a
        nonempty signature with nonempty token families; every recorded check
        names a real correction and a real file; STALE-FOUND records carry a
        pointer; verdict vocabulary is closed; dates parse.
    (b) RATCHET.  For a correction OLDER than `grace_days` (7), the dirty count
        may not GROW beyond its recorded baseline.  Inside the grace period the
        count may move freely and the gate says so.

THE CEILING, STATED NOT IMPLIED
-------------------------------
A signature is a co-occurrence test over lowercased substrings.  It is not a
parse and not a semantic model.  Vocabulary outside the signature ESCAPES --
this is the alias-table lesson, and every entry in the registry carries its own
`blindness:` note and a `known_synonyms_outside_signature:` list naming the
families that were considered and rejected, with the reason and, where it was
measured, the count.

The gate does not merely assert that ceiling, it MEASURES two proxies for it
every run:

  * `topic_reach` -- how many pre-date files touch the entry's ANCHOR family
    alone.  The gap between topic_reach and the dirty count is the price of
    the conjunction: files on the topic that the narrow signature does not
    claim.
  * `signature_missed` -- recorded checks whose (file, correction) pair a human
    adjudicator thought worth writing down and whose signature does NOT fire.
    This is the honest recall test, scored against SCUR-1's hand verdicts as
    ground truth: every one of these is a document the signature would not have
    found on its own.

REPRODUCE
    cd /path/to/gu-formalization
    _local/cas-venv/bin/python process_gates/canonical_currency_audit.py
    _local/cas-venv/bin/python process_gates/canonical_currency_audit.py --as-of 2026-08-25

NOT: a canon edit, a ledger edit, a verdict movement, a physics claim, a
re-adjudication of any SCUR-1 finding, or an assertion that the dirty set is
the set of stale documents.  It is the set of documents NOBODY HAS CHECKED.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / "lab" / "process" / "correction-registry.yaml"
SIDECAR = ROOT / "lab" / "process" / "canonical-currency-checks.yaml"

ALL_REGISTER = "ALL-REGISTER"

CLEARING_VERDICTS = ("CLEARED-CONSISTENT", "FENCED-COMPARATOR", "SUPERSEDED-DOC")
STALE_VERDICTS = ("STALE-FOUND",)
VERDICTS = CLEARING_VERDICTS + STALE_VERDICTS

_DATE_IN_NAME = re.compile(r"(\d{4}-\d{2}-\d{2})")
_ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def default_cfg() -> dict:
    """Every knob the probe is allowed to corrupt.  Machinery only -- there is
    no knob here that loosens a CHECK, because a knob like that would make the
    selftest unfalsifiable (VERIFICATION.md rule 2)."""
    return {
        "registry_path": REGISTRY,
        "sidecar_path": SIDECAR,
        "surfaces": ("canon", "docs", "explorations", "lab", "packets"),
        "include_root_md": True,
        # Defensive nesting guard.  MEASURED 2026-08-17: it currently excludes
        # ZERO files, because the big archives (papers/, absorbed/, _local/) are
        # top-level siblings that `surfaces` already omits.  It exists for the
        # nested case (a vendored `explorations/_local/`), and the probe pins the
        # exclusion by scope composition rather than by this knob.
        "skip_dirs": {"_local", "papers", "absorbed", ".git", "__pycache__", "node_modules"},
        "suffixes": (".md",),
        "frontmatter_date_keys": ("created", "date", "created_date", "filed"),
        "filename_date_fallback": True,
        "frontmatter_window": 4000,
        "clearing_verdicts": CLEARING_VERDICTS,
        "stale_verdicts": STALE_VERDICTS,
        "all_register_token": ALL_REGISTER,
        "strict_predate": True,      # `<` not `<=`; the owner-day file is not dirty
        "owner_exempt": True,        # an entry's own owner/co-owners are never dirty for it
        "explicit_beats_all_register": True,
        "clearing_beats_stale": True,
        "grace_days": None,          # None -> take from the sidecar
        "as_of": None,               # None -> today
        "injected_corrections": (),  # probe-planted registry entries
        "injected_checks": (),       # probe-planted sidecar records
        "drop_check_ids": (),        # probe-planted removal of live records
    }


# ---------------------------------------------------------------- loading ---

def _as_date_str(v) -> str:
    if isinstance(v, _dt.date):
        return v.isoformat()
    return str(v).strip()


def load_registry(cfg: dict) -> list[dict]:
    data = yaml.safe_load(Path(cfg["registry_path"]).read_text(encoding="utf-8"))
    entries = list(data.get("canonical_source_corrections") or [])
    entries.extend(cfg.get("injected_corrections") or ())
    for e in entries:
        e["canonical_since"] = _as_date_str(e.get("canonical_since"))
    return entries


def load_sidecar(cfg: dict) -> tuple[list[dict], dict]:
    data = yaml.safe_load(Path(cfg["sidecar_path"]).read_text(encoding="utf-8")) or {}
    checks = list(data.get("checks") or [])
    # drop_check_ids entries are (file, correction_id, by) triples -- the author
    # is part of the key so a probe can remove ONE lane's record (FIX-A's repair)
    # while leaving another lane's record for the same pair (SCUR-1's finding)
    # in place.  A 2-tuple drops every author for that pair.
    drop = {tuple(str(x) for x in k) for k in (cfg.get("drop_check_ids") or ())}
    if drop:
        checks = [c for c in checks
                  if (str(c.get("file")), str(c.get("correction_id")),
                      str(c.get("by"))) not in drop
                  and (str(c.get("file")), str(c.get("correction_id"))) not in drop]
    checks.extend(cfg.get("injected_checks") or ())
    for c in checks:
        c["date"] = _as_date_str(c.get("date"))
    ratchet = dict(data.get("ratchet") or {})
    return checks, ratchet


# ----------------------------------------------------------------- corpus ---

def doc_date(path: Path, text: str, cfg: dict) -> str | None:
    """Dated frontmatter, else the date in the filename, else None."""
    head = text[: cfg["frontmatter_window"]]
    if head.startswith("---"):
        end = head.find("\n---", 3)
        block = head[:end] if end > 0 else head
    else:
        block = head
    for key in cfg["frontmatter_date_keys"]:
        m = re.search(rf"^{re.escape(key)}\s*:\s*['\"]?(\d{{4}}-\d{{2}}-\d{{2}})", block, re.M)
        if m:
            return m.group(1)
    if cfg["filename_date_fallback"]:
        m = _DATE_IN_NAME.search(path.name)
        if m:
            return m.group(1)
    return None


_RAW_CACHE: dict[tuple, list[tuple[Path, str, str]]] = {}
_HEAD_KEEP = 8192


def _raw_files(cfg: dict) -> list[tuple[Path, str, str]]:
    """(path, raw head, lowercased body) for the selected surfaces.  Cached on
    the FILE-SELECTION knobs only, so a probe may vary date/verdict/signature
    machinery across many computes without re-reading 47 MB each time.  The
    cache key includes every knob that can change which bytes are loaded, so a
    mutation of those knobs cannot be masked by a stale cache."""
    key = (tuple(cfg["surfaces"]), tuple(sorted(cfg["skip_dirs"])),
           tuple(cfg["suffixes"]), bool(cfg["include_root_md"]))
    hit = _RAW_CACHE.get(key)
    if hit is not None:
        return hit
    paths: list[Path] = []
    for surface in cfg["surfaces"]:
        base = ROOT / surface
        if not base.exists():
            continue
        for suf in cfg["suffixes"]:
            paths.extend(sorted(base.rglob(f"*{suf}")))
    if cfg["include_root_md"]:
        for suf in cfg["suffixes"]:
            paths.extend(sorted(ROOT.glob(f"*{suf}")))
    out: list[tuple[Path, str, str]] = []
    seen: set[str] = set()
    for p in sorted(set(paths)):
        if any(part in cfg["skip_dirs"] for part in p.parts):
            continue
        rel = str(p.relative_to(ROOT))
        if rel in seen:
            continue
        seen.add(rel)
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        out.append((p, text[:_HEAD_KEEP], text.lower()))
    _RAW_CACHE[key] = out
    return out


def build_corpus(cfg: dict) -> list[dict]:
    return [{"rel": str(p.relative_to(ROOT)), "date": doc_date(p, head, cfg), "low": low}
            for p, head, low in _raw_files(cfg)]


_MATCH_CACHE: dict[tuple, tuple[frozenset, frozenset]] = {}


def _corpus_key(cfg: dict) -> tuple:
    return (tuple(cfg["surfaces"]), tuple(sorted(cfg["skip_dirs"])),
            tuple(cfg["suffixes"]), bool(cfg["include_root_md"]))


def match_sets(entry: dict, corpus: list[dict], cfg: dict) -> tuple[frozenset, frozenset]:
    """(files matching the full conjunctive signature, files matching the anchor
    family alone).  Cached on the SIGNATURE CONTENT and the corpus selection, so
    corrupting either invalidates the cache -- a mutation of a token family
    cannot be hidden by a stale entry."""
    fams = tuple(tuple(str(t) for t in fam) for fam in families_of(entry))
    key = (_corpus_key(cfg), fams)
    hit = _MATCH_CACHE.get(key)
    if hit is not None:
        return hit
    full, anchor = set(), set()
    for doc in corpus:
        if signature_match(entry, doc["low"]):
            full.add(doc["rel"])
        if anchor_match(entry, doc["low"]):
            anchor.add(doc["rel"])
    hit = (frozenset(full), frozenset(anchor))
    _MATCH_CACHE[key] = hit
    return hit


# -------------------------------------------------------------- signatures ---

def families_of(entry: dict) -> list[list[str]]:
    sig = entry.get("signature") or {}
    return [list(f) for f in (sig.get("token_families") or [])]


def signature_match(entry: dict, low: str) -> bool:
    """Conjunction across families, disjunction within a family.  An entry with
    zero families matches NOTHING (an empty signature is a well-formedness RED,
    never a universal match)."""
    fams = families_of(entry)
    if not fams:
        return False
    for fam in fams:
        toks = [t for t in fam if str(t).strip()]
        if not toks:
            return False
        if not any(str(t).lower() in low for t in toks):
            return False
    return True


def anchor_match(entry: dict, low: str) -> bool:
    fams = families_of(entry)
    if not fams:
        return False
    return any(str(t).lower() in low for t in fams[0] if str(t).strip())


# ---------------------------------------------------------------- verdicts ---

def resolve(records: list[dict], cid: str, since: str, cfg: dict) -> tuple[str, dict | None]:
    """Which recorded check governs (file, correction)?  Precedence:
       1. a record scoped to this exact correction beats an ALL-REGISTER one
       2. at equal scope, a clearing verdict beats STALE-FOUND
    Returns (state, governing_record) with state in
    {CLEAR, KNOWN-STALE, UNCHECKED}."""
    exact = [r for r in records if str(r.get("correction_id")) == cid]
    broad = [r for r in records
             if str(r.get("correction_id")) == cfg["all_register_token"]
             and _as_date_str(r.get("date")) >= since]

    def pick(bucket):
        clearing = [r for r in bucket if r.get("verdict") in cfg["clearing_verdicts"]]
        stale = [r for r in bucket if r.get("verdict") in cfg["stale_verdicts"]]
        if clearing and (cfg["clearing_beats_stale"] or not stale):
            return "CLEAR", clearing[-1]
        if stale:
            return "KNOWN-STALE", stale[-1]
        if clearing:
            return "CLEAR", clearing[-1]
        return None, None

    if exact:
        state, rec = pick(exact)
        if state and cfg["explicit_beats_all_register"]:
            return state, rec
        if state and not broad:
            return state, rec
    if broad:
        state, rec = pick(broad)
        if state:
            return state, rec
    if exact:
        state, rec = pick(exact)
        if state:
            return state, rec
    return "UNCHECKED", None


# ------------------------------------------------------------------ engine ---

def compute(cfg: dict) -> dict:
    entries = load_registry(cfg)
    checks, ratchet = load_sidecar(cfg)
    corpus = build_corpus(cfg)

    by_file: dict[str, list[dict]] = {}
    for c in checks:
        by_file.setdefault(str(c.get("file")), []).append(c)

    as_of = cfg["as_of"] or _dt.date.today().isoformat()
    grace = cfg["grace_days"] if cfg["grace_days"] is not None else int(ratchet.get("grace_days", 7))
    baseline = dict(ratchet.get("baseline") or {})

    per: dict[str, dict] = {}
    for e in entries:
        cid = str(e.get("id"))
        since = str(e.get("canonical_since"))
        owners = {str(e.get("owner"))} | {str(o) for o in (e.get("co_owners") or ())}

        full_set, anchor_set = match_sets(e, corpus, cfg)
        unchecked, known_stale, cleared, repaired, fenced = [], [], [], [], []
        reach = 0
        for doc in corpus:
            d = doc["date"]
            if not d:
                continue
            predates = (d < since) if cfg["strict_predate"] else (d <= since)
            if not predates:
                continue
            if doc["rel"] in anchor_set:
                reach += 1
            if cfg["owner_exempt"] and doc["rel"] in owners:
                continue
            if doc["rel"] not in full_set:
                continue
            state, rec = resolve(by_file.get(doc["rel"], []), cid, since, cfg)
            if state == "UNCHECKED":
                unchecked.append(doc["rel"])
            elif state == "KNOWN-STALE":
                known_stale.append(doc["rel"])
            else:
                had_stale = any(str(r.get("correction_id")) == cid
                                and r.get("verdict") in cfg["stale_verdicts"]
                                for r in by_file.get(doc["rel"], []))
                if had_stale:
                    repaired.append(doc["rel"])
                elif rec is not None and rec.get("verdict") == "FENCED-COMPARATOR":
                    fenced.append(doc["rel"])
                else:
                    cleared.append(doc["rel"])

        # measured blindness: a hand-recorded pair whose signature does not fire.
        # Only EXPLICIT records count as ground truth -- an adjudicator who wrote
        # this correction's id next to this file thought the pair mattered.
        # ALL-REGISTER records are excluded: a blanket clearance is not evidence
        # that the signature ought to have fired.  Deduplicated by file, so a
        # finding and its later repair count once.
        missed_by_file: dict[str, list[str]] = {}
        for r in checks:
            if str(r.get("correction_id")) != cid:
                continue
            rel = str(r.get("file"))
            doc = next((x for x in corpus if x["rel"] == rel), None)
            if doc is None or not doc["date"]:
                continue
            if doc["date"] >= since:
                continue
            if not signature_match(e, doc["low"]):
                missed_by_file.setdefault(rel, []).append(str(r.get("verdict")))
        missed = [(rel, "/".join(vs)) for rel, vs in sorted(missed_by_file.items())]

        age = _days(as_of, since)
        per[cid] = {
            "id": cid, "since": since, "age": age, "aged": age >= grace,
            "unchecked": unchecked, "known_stale": known_stale,
            "cleared": cleared, "fenced": fenced, "repaired": repaired,
            "dirty": len(unchecked) + len(known_stale),
            "topic_reach": reach,
            "signature_missed": missed,
            "baseline": baseline.get(cid),
        }

    return {
        "entries": entries, "checks": checks, "ratchet": ratchet, "corpus": corpus,
        "as_of": as_of, "grace_days": grace, "per": per,
        "n_dated": sum(1 for d in corpus if d["date"]),
        "n_undated": sum(1 for d in corpus if not d["date"]),
    }


def _days(a: str, b: str) -> int:
    try:
        return (_dt.date.fromisoformat(a) - _dt.date.fromisoformat(b)).days
    except ValueError:
        return -10**6


# --------------------------------------------------------- well-formedness ---

def wellformedness(res: dict, cfg: dict) -> list[str]:
    bad: list[str] = []
    entries, checks = res["entries"], res["checks"]

    if not entries:
        bad.append("registry: canonical_source_corrections is empty or absent")
    ids: set[str] = set()
    for e in entries:
        cid = str(e.get("id") or "")
        tag = f"registry[{cid or '<no id>'}]"
        if not cid:
            bad.append(f"{tag}: missing id")
        if cid in ids:
            bad.append(f"{tag}: duplicate id")
        ids.add(cid)
        if e.get("entry_class") != "canonical_source_correction":
            bad.append(f"{tag}: entry_class must be 'canonical_source_correction'")
        since = str(e.get("canonical_since") or "")
        if not _ISO.match(since):
            bad.append(f"{tag}: canonical_since '{since}' is not an ISO date")
        for key in ("owner", "superseded_reading"):
            if not str(e.get(key) or "").strip():
                bad.append(f"{tag}: {key} is empty")
        for owner in [e.get("owner")] + list(e.get("co_owners") or ()):
            if owner and not (ROOT / str(owner)).exists():
                bad.append(f"{tag}: owner path does not exist: {owner}")
        sig = e.get("signature") or {}
        fams = families_of(e)
        if not fams:
            bad.append(f"{tag}: signature has no token families -- an empty signature "
                       "would silently match nothing and hide the correction")
        for i, fam in enumerate(fams):
            toks = [str(t) for t in fam if str(t).strip()]
            if not toks:
                bad.append(f"{tag}: token family {i} is empty after stripping")
        if not str(sig.get("blindness") or "").strip():
            bad.append(f"{tag}: signature.blindness is empty -- the one-token-blindness "
                       "caveat is mandatory per entry")
        if not list(e.get("signature", {}).get("known_synonyms_outside_signature") or []):
            bad.append(f"{tag}: known_synonyms_outside_signature is empty -- entries must "
                       "cite their known synonym families")

    for i, c in enumerate(checks):
        tag = f"sidecar[{i}:{c.get('file')}]"
        rel = str(c.get("file") or "")
        if not rel or not (ROOT / rel).exists():
            bad.append(f"{tag}: check references a file that does not exist")
        cid = str(c.get("correction_id") or "")
        if cid != cfg["all_register_token"] and cid not in ids:
            bad.append(f"{tag}: check references unknown correction '{cid}'")
        verdict = str(c.get("verdict") or "")
        if verdict not in VERDICTS:
            bad.append(f"{tag}: verdict '{verdict}' outside the closed vocabulary {VERDICTS}")
        if not _ISO.match(str(c.get("date") or "")):
            bad.append(f"{tag}: date '{c.get('date')}' is not an ISO date")
        if not str(c.get("by") or "").strip():
            bad.append(f"{tag}: 'by' is empty -- a check with no author is not a check")
        if verdict in cfg["stale_verdicts"] and not str(c.get("pointer") or "").strip():
            bad.append(f"{tag}: STALE-FOUND requires a pointer to where the finding is written")

    ratchet = res["ratchet"]
    if not isinstance(ratchet.get("grace_days"), int) or int(ratchet.get("grace_days", 0)) <= 0:
        bad.append("sidecar: ratchet.grace_days must be a positive integer")
    for cid in (ratchet.get("baseline") or {}):
        if cid not in ids:
            bad.append(f"sidecar: ratchet baseline names unknown correction '{cid}'")
    return bad


def ratchet_failures(res: dict) -> list[str]:
    bad: list[str] = []
    for cid, p in sorted(res["per"].items()):
        if not p["aged"]:
            continue
        if p["baseline"] is None:
            bad.append(f"{cid}: aged {p['age']}d past canonical_since with NO ratchet baseline "
                       f"recorded (dirty={p['dirty']}); record one or the ratchet cannot bite")
        elif p["dirty"] > int(p["baseline"]):
            bad.append(f"{cid}: RATCHET BROKEN -- dirty {p['dirty']} > baseline {p['baseline']} "
                       f"for a correction {p['age']} days old")
    return bad


# ------------------------------------------------------------------ report ---

def report(res: dict, cfg: dict, verbose: bool = True) -> None:
    print("=" * 78)
    print("CANONICAL-CORRECTION CURRENCY AUDIT (CT-5)")
    print("=" * 78)
    print(f"as-of {res['as_of']}   corpus {len(res['corpus'])} files "
          f"({res['n_dated']} dated, {res['n_undated']} undated -> undated files are "
          "OUT OF THE DIRTY SET and cannot be, since 'predates' is undecidable for them)")
    print(f"registry {len(res['entries'])} canonical corrections; sidecar "
          f"{len(res['checks'])} recorded checks; grace {res['grace_days']} days")
    print()

    total_dirty = total_unchecked = total_stale = 0
    total_cleared = total_missed = 0
    for cid, p in sorted(res["per"].items()):
        grace_note = "AGED (ratchet armed)" if p["aged"] else f"in grace ({p['age']}d old, ratchet inert)"
        print("-" * 78)
        print(f"{cid}   canonical_since {p['since']}   {grace_note}")
        print(f"    DIRTY {p['dirty']}  = {len(p['unchecked'])} unchecked "
              f"+ {len(p['known_stale'])} known-stale       "
              f"baseline {p['baseline'] if p['baseline'] is not None else '-'}")
        print(f"    clear {len(p['cleared'])} consistent / {len(p['fenced'])} fenced-comparator "
              f"/ {len(p['repaired'])} repaired-after-STALE-FOUND")
        print(f"    topic_reach {p['topic_reach']} pre-date files touch the anchor family "
              f"(conjunction discards {p['topic_reach'] - p['dirty'] - len(p['cleared']) - len(p['fenced']) - len(p['repaired'])} "
              "of them as off-signature)")
        if p["signature_missed"]:
            print(f"    signature_missed {len(p['signature_missed'])} -- hand-recorded pairs the "
                  "signature does NOT fire on (measured blindness):")
            for rel, v in p["signature_missed"]:
                print(f"        [{v}] {rel}")
        if verbose:
            for rel in p["unchecked"]:
                print(f"      DIRTY-UNCHECKED    {rel}")
            for rel in p["known_stale"]:
                print(f"      DIRTY-KNOWN-STALE  {rel}")
        total_dirty += p["dirty"]
        total_unchecked += len(p["unchecked"])
        total_stale += len(p["known_stale"])
        total_cleared += len(p["cleared"]) + len(p["fenced"]) + len(p["repaired"])
        total_missed += len(p["signature_missed"])

    print("-" * 78)
    print(f"TOTAL dirty (file, correction) pairs: {total_dirty}   "
          f"({total_unchecked} unchecked, {total_stale} known-stale)")
    print(f"TOTAL cleared by recorded checks:     {total_cleared}")
    print(f"TOTAL measured signature blindness:   {total_missed} hand-recorded pairs missed")
    print("The dirty set is WARN-ONLY and never turns this gate red (FX-3: a gate that")
    print("goes red on prose gets deleted, and a deleted gate detects nothing).")
    print("-" * 78)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--as-of", dest="as_of", default=None,
                    help="date to age corrections against (default: today)")
    ap.add_argument("--quiet", action="store_true", help="counts only, no file lists")
    args = ap.parse_args(argv)

    cfg = default_cfg()
    if args.as_of:
        if not _ISO.match(args.as_of):
            print(f"--as-of must be an ISO date, got {args.as_of!r}")
            return 2
        cfg["as_of"] = args.as_of

    try:
        res = compute(cfg)
    except Exception as exc:                                        # noqa: BLE001
        print(f"[RED] audit could not run: {type(exc).__name__}: {exc}")
        return 1

    report(res, cfg, verbose=not args.quiet)

    wf = wellformedness(res, cfg)
    rt = ratchet_failures(res)
    for line in wf:
        print(f"[RED][well-formedness] {line}")
    for line in rt:
        print(f"[RED][ratchet] {line}")
    if wf or rt:
        print(f"FAIL: {len(wf)} well-formedness + {len(rt)} ratchet failures.")
        return 1
    print("OK: registry and sidecar well-formed; ratchet intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
