#!/usr/bin/env python3
"""Type the needs/provides join: a candidate pair must agree on DOMAIN and
CODOMAIN, not merely on a token shape.

WHAT THIS ADDS TO FX-1 (and what it deliberately does not touch).
process_gates/needs_provides_composition_audit.py (FX-1, 2026-08-16) joins
declared NEEDS against claimed SUPPLY on three exact token shapes.  It is the
MERGE half of a join: its alias table says "these two notations are one
object", under the law NO ALIAS WITHOUT A RECEIPT.  It has no SPLIT half, and
its measured blindness is exactly there.

  THE MEASURED BLIND CLASS (`v_PSB`, homonym-register :1153, filed by CP-1
  on 2026-08-17).  Two different objects wear one token:

    sense 1  the source-selected rank-one vector in the orbit of
             V_PSB = (10bar,1,3), owned by
             explorations/cycle-gates-and-audits/
             cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md;
    sense 2  the independent rank-one vector in (4,1,2) with stabilizer the
             SM, kron(e4, fR), owned by explorations/conditional-build/
             selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md.

  The register records that STABILIZER DIMENSION CANNOT DISCRIMINATE (12
  either way) -- the one numeric a reader would check -- and that the two are
  BYTE-DISJOINT across their owning files.  A token join sees one key.  CP-1
  had to exclude the wrong object BY HAND, in prose, inside the RA-A6
  revival trigger (ledger v0.259, DELTA-2).  That hand-exclusion is the
  receipt that this layer is not decoration.

TYPED MORPHISM RECORDS.  The sidecar lab/process/needs-provides-typed-records.json
stores records of exactly six keys:

    {key, dom, cod, map_type, source_file, receipt}

  `dom`/`cod` are object ids of the CT-1 base categories
  (lab/methods/gu-base-categories.md): Source-Layer objects `L1..L4`, Carrier
  objects `C1..C11`, the declared-unknown markers `UNTYPED` (M1) and
  `HOMONYM-AMBIGUOUS` (M4), or a REGISTERED-HOMONYM SENSE ID `HOM:<token>#<n>`
  resolving in lab/process/homonym-register.yaml.  The sense id coins NO new
  CT-1 object: CT-1 section 3.5 states that a bare registered token FAILS to
  name an object and names the register as the disambiguation surface it
  points at rather than duplicates.  `HOM:` ids point at that surface; the
  <= 12 object budget of every CT-1 category is untouched.
  `map_type` is a CT-1 arrow label (section 3.3 / the gu-token-codomain block).

  Every non-marker typing carries a `receipt` naming the DETERMINISTIC RULE
  that produced it and a byte-verified `quote` from `source_file`, and this
  gate RE-APPLIES the rule to the quote on every run: a hand-edited dom that
  the rule does not reproduce is a red.  Where the text supports no typing,
  the record is UNTYPED.  Nothing is guessed -- the CN-2 principle, carried:
  a declared unknown is compliance, a plausible token is a lie.

THE RULES (checked, in precedence order; most specific wins):

  R4a homonym-sense-by-owning-file -- the text names sense n's owning file
      (basename) and no other sense's.  This is CP-1's own move: "same object
      verified by LINEAGE RECEIPT, not token".
  R4b homonym-sense-by-discriminator -- BOTH of: exactly one sense's
      byte-disjoint discriminator occurs in the text at all (a text carrying
      both, like RA-A6's DELTA-2 trigger which names the excluded object, is
      not resolvable this way), AND that discriminator co-occurs with the
      token on a line (the register's own naming rule, "name the
      representation with the token", read mechanically).  The narrowing is
      deliberate: the register's receipt claims disjointness across the two
      OWNING FILES and claims nothing about an arbitrary file.  Discriminators
      live in the sidecar under NO DISCRIMINATOR WITHOUT A RECEIPT (the mirror
      of FX-1's alias law: FX-1 MERGES two notations, this SPLITS one), and
      every entry cites the register substrings that state it.  Ties, both, or
      neither -> HOMONYM-AMBIGUOUS (CT-1 marker M4), never a guess.
  R1  fx2-block -- a ```gu-typed-objects block (FX-2's gate format).  `dom`
      from a named Carrier object in the carrier field if one occurs
      verbatim, else from `LAYER=`; `cod` from a named Carrier object in the
      target field; `map_type` from `MAP-TYPE=`.  A mixed layer (`a+b`) is
      UNTYPED with the BRIDGE recorded: CT-1 has no product object and this
      gate will not invent one (the thirteenth-object rule).  A key typed by
      two blocks of one file with conflicting doms is UNTYPED
      (fx2-block-conflict) -- declared, not adjudicated.
  R2  ledger-context -- RESERVED and CURRENTLY EMPTY.  CT-2 has not landed;
      lab/process/conditional-physics-ledger-v0.259.json rows carry no
      `context` field (87 rows, checked every run).  Stated rather than
      implied, per the FX-2/CT-1 house rule about unpopulated vocabulary.
  R3  prose-token -- explicit `LAYER=` / `MAP-TYPE=` tokens in prose outside
      any fenced block.

THE TYPED JOIN.  A candidate pair (need site, key) x (provider file) is:
    TYPE-REJECTED    both sides carry object ids and they differ (modulo the
                     sidecar's dom_aliases, which is EMPTY and under the same
                     receipt law);
    TYPE-VERIFIED    both sides carry object ids and they agree;
    TYPE-UNVERIFIED  a marker (UNTYPED / HOMONYM-AMBIGUOUS) on either side --
                     the match is NOT denied, it is FLAGGED as unverified.
A marker matches anything.  That is the honest weakening, and it is why the
coverage fraction is printed every run instead of being buried.

WHAT THIS GATE DOES NOT DO.  It does not edit, import-patch, or re-tune FX-1;
it imports FX-1 read-only for its token shapes and its live join, and asserts
mechanically that FX-1 does not read this gate or this sidecar (so FX-1's
behaviour is preserved by construction, not by promise).  It adjudicates no
pair -- FX-1's ADJUDICATED map remains the only place a pair is typed
LIVE_CANDIDATE / ALREADY_COMPOSED / SUPERSEDED / UNTYPED.  It moves no claim,
edits no ledger, canon, registry or README.

Owning artifact:
lab/active-research/joe-directed/ct-hardening/ct3-typed-morphism-join-2026-08-17.md
(target_claim: NONE-NOT-A-KILL).

Run:  python3 process_gates/needs_provides_typed_join_audit.py
      python3 process_gates/needs_provides_typed_join_audit.py --selftest
      python3 process_gates/needs_provides_typed_join_audit.py --emit  (regenerate sidecar)
      python3 -m unittest process_gates.needs_provides_typed_join_audit  (also runs)
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIDECAR = ROOT / "lab/process/needs-provides-typed-records.json"
REFERENCE = ROOT / "lab/methods/gu-base-categories.md"
REGISTER = ROOT / "lab/process/homonym-register.yaml"
FX1_PATH = ROOT / "process_gates/needs_provides_composition_audit.py"
ARTIFACT = ("lab/active-research/joe-directed/ct-hardening/"
            "ct3-typed-morphism-join-2026-08-17.md")

MUTATE = os.environ.get("CT3_MUTATE", "")

SKIP_DIRS = {"_local", ".git", "__pycache__", ".pytest_cache", "node_modules",
             ".lake", ".ruff_cache", ".hypothesis"}

# CT-1 vocabulary tokens are NOT objects: they are the closed value sets the
# FX-2 gate writes into carrier/target slots.  FX-1's K3 shape reads
# `S-FULL-DIRAC` as the object token `FULL-DIRAC` (its own live join carries
# ART:...ct1-base-categories...::HALF-SAME as an unadjudicated pair for
# exactly this reason).  CT-3 drops them from ITS records and reports the
# leak; repairing FX-1's extractor is FX-1's to do, not this gate's.
VOCAB_STOP = {
    "MAP-TYPE", "FULL-DIRAC", "HALF-SAME", "HALF-OPPOSITE",
    "CHIRALITY-UNTYPED", "HOMONYM-AMBIGUOUS", "ZERO-ORDER-COINDEX-DESCENT",
}

MARKERS = ("UNTYPED", "HOMONYM-AMBIGUOUS")
FENCE_RE = re.compile(r"^```gu-typed-objects[ \t]*\n(.*?)^```", re.M | re.S)
BLOCK_KEYS = ("result", "carrier", "pairing", "real_structure", "grading",
              "action_owner", "target")


# ---------------------------------------------------------------------------
# FX-1, imported READ-ONLY (never edited, never monkey-patched)
# ---------------------------------------------------------------------------
def load_fx1():
    spec = importlib.util.spec_from_file_location("fx1_readonly", FX1_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FX1 = load_fx1()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def object_keys(text: str) -> set[str]:
    """FX-1's token shapes, minus CT-1's own closed vocabulary."""
    return {t for t in FX1.tokens_of(text) if t not in VOCAB_STOP}


# ---------------------------------------------------------------------------
# CT-1 reference: the codomain, parsed from the reference, FAIL CLOSED
# ---------------------------------------------------------------------------
ROW_RE = re.compile(r"^\|\s*([A-Z]{1,2}\d{1,2})\s*\|(.*)$", re.M)
CODOMAIN_RE = re.compile(r"^```gu-token-codomain[ \t]*\n(.*?)^```", re.M | re.S)


class ReferenceMissing(RuntimeError):
    pass


def load_reference() -> dict:
    """Objects, markers and token codomains, DERIVED from CT-1's own tables.

    Fail closed: a missing reference, a missing codomain block, or a layer
    token with no matching object row is an exception, never a default.
    """
    path = REFERENCE
    if MUTATE == "ref-gone":
        path = REFERENCE.with_name("__ct3_absent_reference__.md")
    if not path.is_file():
        raise ReferenceMissing(f"CT-1 reference missing: {path}")
    text = read(path)
    if MUTATE == "ref-layer-drift":
        text = text.replace("layer-tokens: ambient observed",
                            "layer-tokens: ambient observed extra-stratum")

    m = CODOMAIN_RE.search(text)
    if not m:
        raise ReferenceMissing("gu-token-codomain block missing from reference")
    layer_tokens: tuple[str, ...] = ()
    map_tokens: tuple[str, ...] = ()
    for line in m.group(1).splitlines():
        if line.startswith("layer-tokens:"):
            layer_tokens = tuple(line.split(":", 1)[1].split())
        elif line.startswith("map-type-tokens:"):
            map_tokens = tuple(line.split(":", 1)[1].split())
    if not layer_tokens or not map_tokens:
        raise ReferenceMissing("codomain block is missing a token line")

    row_re = ROW_RE
    if MUTATE == "ref-object-row-blind":       # machinery corruption
        row_re = re.compile(r"^\|\s*(ZZ\d{1,2})\s*\|(.*)$", re.M)

    objects: dict[str, dict] = {}
    for oid, rest in row_re.findall(text):
        # rest is "<name> | <role> | <statement> | <receipts> |"
        cells = [c.strip() for c in rest.split("|")]
        if len(cells) < 4 or cells[1] != "object":
            continue
        objects[oid] = {"name": cells[0].strip("`"), "statement": cells[2]}

    # The role of an object row is read from its own statement prefix, so a
    # reference reword reds this gate instead of silently re-typing records.
    layer_object: dict[str, str] = {}
    named_carrier: dict[str, str] = {}
    for oid, rec in objects.items():
        if rec["statement"].startswith("LAYER stratum:"):
            layer_object[rec["name"]] = oid
        elif rec["statement"].startswith("Homonym-subscripted carrier:"):
            named_carrier[rec["name"]] = oid
        # "CHIRALITY reading:" rows (C5-C7) are CN-2's codomain, which CT-1
        # section 3.4 explicitly does NOT wire; CT-3 does not wire it either.

    missing = [t for t in layer_tokens
               if t != "UNTYPED" and t not in layer_object]
    if missing:
        raise ReferenceMissing(
            "layer token(s) with no CT-1 object row: " + ", ".join(missing))

    return {
        "object_ids": set(objects),
        "layer_tokens": layer_tokens,
        "map_tokens": map_tokens,
        "layer_object": layer_object,
        "named_carrier": named_carrier,
    }


# ---------------------------------------------------------------------------
# Homonym register
# ---------------------------------------------------------------------------
def load_register() -> dict[str, dict]:
    """token -> entry, for entries of kind `homonym` with >= 2 senses.

    Parsed with a narrow reader rather than PyYAML so the gate has no
    third-party dependency (the repo's process gates are stdlib-only).
    """
    path = REGISTER
    if MUTATE == "register-gone":
        path = REGISTER.with_name("__ct3_absent_register__.yaml")
    if not path.is_file():
        raise ReferenceMissing(f"homonym register missing: {path}")
    text = read(path)
    out: dict[str, dict] = {}
    blocks = re.split(r"\n  - token: ", text)
    for block in blocks[1:]:
        token = block.split("\n", 1)[0].strip().strip('"').strip("'")
        if not re.search(r"^    kind: homonym\s*$", block, re.M):
            continue
        senses = re.split(r"^      - definition:", block, flags=re.M)[1:]
        if len(senses) < 2:
            continue
        out[token] = {"token": token, "sense_count": len(senses),
                      "text": block}
    return out


# ---------------------------------------------------------------------------
# Sidecar
# ---------------------------------------------------------------------------
def load_sidecar() -> dict:
    data = json.loads(read(SIDECAR))
    if MUTATE == "sidecar-forged-dom":
        for rec in data["records"]:
            if rec["key"] == "v_PSB" and rec["dom"] == "HOM:v_PSB#2":
                rec["dom"] = "HOM:v_PSB#1"
                break
    if MUTATE == "sidecar-forged-alias":
        data.setdefault("dom_aliases", []).append(
            {"class": ["HOM:v_PSB#1", "HOM:v_PSB#2"]})
    if MUTATE == "sidecar-quote-drift":
        for rec in data["records"]:
            if rec["key"] == "v_PSB":
                rec["receipt"]["quote"] = "a quote that is not in the file"
                break
    if MUTATE == "discriminator-not-disjoint":
        for entry in data["sense_discriminators"]:
            entry["senses"][1]["discriminators"] = ["v_PSB"]
    return data


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------
def corpus_md() -> list[str]:
    rels = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                rels.append(os.path.relpath(os.path.join(dirpath, fn), ROOT)
                            .replace(os.sep, "/"))
    return sorted(rels)


def parse_block(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    cur = None
    for line in body.splitlines():
        if line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([a-z_]+):[ \t]*(.*)$", line)
        if m and m.group(1) in BLOCK_KEYS:
            cur = m.group(1)
            fields[cur] = m.group(2)
        elif cur is not None:
            fields[cur] += " " + line.strip()
    return fields


def blocks_of(text: str) -> list[tuple[str, dict[str, str]]]:
    """(raw body, parsed fields) per block -- the raw body is kept so every
    receipt quote is a byte-exact LINE of the file rather than a re-joined
    reconstruction of it."""
    fence = FENCE_RE
    if MUTATE == "block-fence-blind":          # machinery corruption
        fence = re.compile(r"^```gu-typed-nothing[ \t]*\n(.*?)^```", re.M | re.S)
    return [(b, parse_block(b)) for b in fence.findall(text)]


def layer_dom(carrier: str, ref: dict) -> tuple[str, str]:
    """(dom, sub-rule).  Named Carrier object beats LAYER stratum."""
    for name, oid in ref["named_carrier"].items():
        if name in carrier:
            return oid, "fx2-block-named-carrier"
    m = re.search(r"LAYER=([A-Za-z\-]+(?:\+[A-Za-z\-]+)*)", carrier)
    if not m:
        return "UNTYPED", "fx2-block-no-layer"
    tok = m.group(1)
    if "+" in tok:
        return "UNTYPED", "fx2-block-mixed-layer"
    if tok == "UNTYPED":
        return "UNTYPED", "fx2-block-layer"
    oid = ref["layer_object"].get(tok)
    return (oid, "fx2-block-layer") if oid else ("UNTYPED", "fx2-block-layer")


def map_type_of(target: str) -> str:
    pat = r"MAP-TYPE=([A-Za-z\-]+)"
    if MUTATE == "maptype-blind":              # machinery corruption
        pat = r"MAP-KIND=([A-Za-z\-]+)"
    m = re.search(pat, target)
    return m.group(1) if m else "UNTYPED"


def named_cod(target: str, ref: dict) -> str:
    for name, oid in ref["named_carrier"].items():
        if name in target:
            return oid
    return "UNTYPED"


def sense_index(text: str, entry: dict) -> tuple[str, str, str]:
    """Resolve a registered-homonym token in `text` to a sense id.

    Returns (dom, rule, quote).  R4a (owning file / lineage receipt) is tried
    before R4b (byte-disjoint discriminator); both-or-neither is the marker
    HOMONYM-AMBIGUOUS, never a guess.
    """
    token = entry["token"]
    if MUTATE == "sense-collapse":             # machinery corruption
        return f"HOM:{token}#1", "homonym-sense-by-discriminator", token
    hits_file = []
    for sense in entry["senses"]:
        base = os.path.basename(sense["owning_file"])
        if base in text:
            hits_file.append((sense["index"], base))
    if len(hits_file) == 1:
        idx, base = hits_file[0]
        return f"HOM:{token}#{idx}", "homonym-sense-by-owning-file", base
    # R4b is DELIBERATELY NARROW.  The register's receipt claims byte-
    # disjointness across the two OWNING FILES; it claims nothing about an
    # arbitrary file, where a discriminator string may belong to some other
    # sentence entirely.  So R4b fires only when (i) exactly one sense's
    # discriminator occurs in the text at all -- a text carrying both, like
    # RA-A6's DELTA-2 trigger which names the excluded object, is NOT
    # resolvable this way and must fall to R4a -- and (ii) that discriminator
    # co-occurs with the token ON A LINE, which is the register's own naming
    # rule ("name the representation with the token") read mechanically.
    present = [s for s in entry["senses"]
               if any(d in text for d in s["discriminators"])]
    if len(present) == 1:
        sense = present[0]
        for line in text.splitlines():
            if token not in line:
                continue
            for disc in sense["discriminators"]:
                if disc in line:
                    return (f"HOM:{token}#{sense['index']}",
                            "homonym-sense-by-discriminator", disc)
    return "HOMONYM-AMBIGUOUS", "homonym-ambiguous", token


def extract_records(sidecar: dict, ref: dict) -> list[dict]:
    """Derive typed records from the live tree, in rule precedence order."""
    discs = {e["token"]: e for e in sidecar.get("sense_discriminators", [])}
    register_tokens = set(load_register())
    records: list[dict] = []
    seen: set[tuple[str, str]] = set()

    def add(key, dom, cod, map_type, source_file, site, rule, quote):
        if (site, key) in seen:
            return
        seen.add((site, key))
        records.append({
            "key": key, "dom": dom, "cod": cod, "map_type": map_type,
            "source_file": source_file,
            "receipt": {"site": site, "rule": rule, "quote": quote},
        })

    # ---- R4: registered-homonym senses (most specific) --------------------
    # Ledger rows and fork rows first (need-side loci), then corpus files.
    ledger_rel = FX1.latest_ledger_path()
    ledger = json.loads(read(ROOT / ledger_rel))
    for row in ledger["rows"]:
        if row.get("row_status") == "SUPERSEDED":
            continue
        blob = json.dumps(row)
        for token, entry in discs.items():
            if token not in blob:
                continue
            dom, rule, quote = sense_index(blob, entry)
            add(token, dom, "UNTYPED", "UNTYPED", ledger_rel,
                f"LEDGER:{row['id']}", rule, quote)

    fork_rel = "lab/process/layer0-fork-registry.yaml"
    fork_text = read(ROOT / fork_rel)
    for block in re.split(r"\n  - id: ", fork_text)[1:]:
        fork_id = block.split("\n", 1)[0].strip()
        for token, entry in discs.items():
            if token not in block:
                continue
            dom, rule, quote = sense_index(block, entry)
            add(token, dom, "UNTYPED", "UNTYPED", fork_rel,
                f"FORK:{fork_id}", rule, quote)

    md = {rel: read(ROOT / rel) for rel in corpus_md()}
    for rel, text in md.items():
        for token, entry in discs.items():
            if token not in text:
                continue
            dom, rule, quote = sense_index(text, entry)
            if dom in MARKERS:
                continue          # markers add nothing; do not inflate the file
            add(token, dom, "UNTYPED", "UNTYPED", rel, f"FILE:{rel}",
                rule, quote)

    # A registered-homonym token with no receipted discriminator set may NOT
    # be typed by its layer stratum: both senses can sit at one stratum, so a
    # stratum agreement would print TYPE-VERIFIED for two different objects --
    # precisely the failure this lane exists to stop.  CT-1 section 3.5 is the
    # law: a bare registered token FAILS to name an object.  Marker M4.
    unresolved_homonyms = {t for t in register_tokens if t not in discs}

    # ---- R1: FX-2 typed-object blocks -------------------------------------
    for rel, text in md.items():
        parsed = blocks_of(text)
        if not parsed:
            continue
        per_key: dict[str, list[tuple]] = {}
        for body, fields in parsed:
            carrier = fields.get("carrier", "")
            target = fields.get("target", "")
            dom, sub = layer_dom(carrier, ref)
            cod = named_cod(target, ref)
            mt = map_type_of(target)
            if mt not in ref["map_tokens"]:
                mt = "UNTYPED"
            for key in object_keys(carrier):
                per_key.setdefault(key, []).append(
                    (dom, cod, mt, sub + "-carrier", body))
            for key in object_keys(target):
                per_key.setdefault(key, []).append(
                    (dom, cod, mt, sub + "-target", body))
        for key, hits in per_key.items():
            doms = {h[0] for h in hits}
            cods = {h[1] for h in hits}
            mts = {h[2] for h in hits}
            if len(doms) > 1 or len(cods) > 1 or len(mts) > 1:
                add(key, "UNTYPED", "UNTYPED", "UNTYPED", rel, f"FILE:{rel}",
                    "fx2-block-conflict", quote_for(hits[0][4], key))
                continue
            dom, cod, mt, rule, body = hits[0]
            if key in unresolved_homonyms:
                dom = cod = "HOMONYM-AMBIGUOUS"
                rule = "homonym-unresolved"
            if dom in MARKERS and cod in MARKERS and mt == "UNTYPED":
                continue          # nothing typed; an all-marker record is noise
            add(key, dom, cod, mt, rel, f"FILE:{rel}", rule,
                quote_for(body, key))

    # ---- R3: prose LAYER= / MAP-TYPE= outside any block -------------------
    for rel, text in md.items():
        stripped = FENCE_RE.sub("", text)
        for line in stripped.splitlines():
            if "LAYER=" not in line and "MAP-TYPE=" not in line:
                continue
            keys = object_keys(line)
            if not keys:
                continue
            dom, _sub = layer_dom(line, ref)
            mt = map_type_of(line)
            if mt not in ref["map_tokens"]:
                mt = "UNTYPED"
            for key in keys:
                kdom = "HOMONYM-AMBIGUOUS" if key in unresolved_homonyms else dom
                krule = ("homonym-unresolved" if key in unresolved_homonyms
                         else "prose-token")
                if kdom in MARKERS and mt == "UNTYPED":
                    continue
                add(key, kdom, "UNTYPED", mt, rel, f"FILE:{rel}", krule,
                    line.strip()[:120])

    records.sort(key=lambda r: (r["key"], r["receipt"]["site"]))
    return records


def quote_for(body: str, key: str) -> str:
    """The byte-exact LINE of `body` that carries `key`, stripped.

    Stripping only removes leading/trailing whitespace, so the result stays a
    contiguous substring of the source file -- which is what makes the
    receipt check (`quote in file_text`) a real byte-level check rather than
    a check against a reconstruction.
    """
    for line in body.splitlines():
        if key in line:
            return line.strip()[:200]
    return body.strip().splitlines()[0].strip()[:200] if body.strip() else key


# ---------------------------------------------------------------------------
# The typed join
# ---------------------------------------------------------------------------
def record_index(records: list[dict]) -> dict[tuple[str, str], dict]:
    return {(r["receipt"]["site"], r["key"]): r for r in records}


def dom_of(index, site, key, alias) -> tuple[str, str]:
    """(dom, provenance) for a (site, key); markers when nothing is recorded."""
    rec = index.get((site, key))
    if rec is None and site.startswith("ART:"):
        rec = index.get((f"FILE:{site[4:]}", key))
    if rec is None:
        return "UNTYPED", "no-record"
    return alias.get(rec["dom"], rec["dom"]), rec["receipt"]["rule"]


def typed_join(records: list[dict], sidecar: dict,
               extra_md: dict | None = None) -> dict:
    """Type every FX-1 candidate pair.  FX-1 is called, never modified."""
    index = record_index(records)
    alias: dict[str, str] = {}
    for entry in sidecar.get("dom_aliases", []):
        head = entry["class"][0]
        for tok in entry["class"]:
            alias[tok] = head

    pairs, wide, _nd = FX1.join(extra_md=extra_md)
    everything = {**pairs, **wide}
    out = {"verified": [], "rejected": [], "unverified": [], "total": 0,
           "pairs": len(everything), "pairs_decided": 0, "need_typed": 0,
           "wide_sampled": 0}
    for pair_id, rec in sorted(everything.items()):
        site, key = pair_id.rsplit("::", 1)
        need_dom, need_rule = dom_of(index, site, key, alias)
        if need_dom not in MARKERS:
            out["need_typed"] += 1
        # Tier-2 WIDE rows expose only a 3-file SAMPLE of their providers
        # (FX-1's own structure), so the edge denominator under-counts them;
        # the pair denominator does not, and both are printed.
        if "providers" not in rec:
            out["wide_sampled"] += 1
        providers = rec.get("providers") or rec.get("sample") or []
        decided = False
        for prov in providers:
            out["total"] += 1
            prov_dom, prov_rule = dom_of(index, f"FILE:{prov}", key, alias)
            row = {"pair": pair_id, "provider": prov,
                   "need_dom": need_dom, "prov_dom": prov_dom,
                   "need_rule": need_rule, "prov_rule": prov_rule}
            if need_dom in MARKERS or prov_dom in MARKERS:
                out["unverified"].append(row)
            else:
                decided = True
                (out["verified"] if need_dom == prov_dom
                 else out["rejected"]).append(row)
        if decided:
            out["pairs_decided"] += 1
    return out


# ---------------------------------------------------------------------------
# The v_PSB acceptance test, constructed explicitly from the two carriers
# ---------------------------------------------------------------------------
CYCLE1 = ("explorations/cycle-gates-and-audits/"
          "cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md")
TRACEHQ = ("explorations/conditional-build/"
           "selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md")


def vpsb_acceptance(records: list[dict], sidecar: dict) -> dict:
    """Return the four measured facts the acceptance test pins."""
    index = record_index(records)
    alias: dict[str, str] = {}
    for entry in sidecar.get("dom_aliases", []):
        head = entry["class"][0]
        for tok in entry["class"]:
            alias[tok] = head

    need_dom, need_rule = dom_of(index, "LEDGER:RA-A6", "v_PSB", alias)
    c1_dom, c1_rule = dom_of(index, f"FILE:{CYCLE1}", "v_PSB", alias)
    hq_dom, hq_rule = dom_of(index, f"FILE:{TRACEHQ}", "v_PSB", alias)

    # The token join produces the RIGHT provider today only because the
    # trace-hq lines carry no provide verb.  Inject ONE provide verb into an
    # in-memory copy of the real file (FX-1's own extra_md hook; nothing on
    # disk is touched) and the token join hands over the WRONG object.
    hq_text = read(ROOT / TRACEHQ)
    mutated = hq_text.replace(
        "| `v_PSB` | independent rank-one vector in `(4,1,2)`",
        "| `v_PSB` | this gate constructs the independent rank-one vector in `(4,1,2)`",
        1)
    joined = typed_join(records, sidecar, extra_md={TRACEHQ: mutated})
    token_pairs = [r for r in
                   joined["verified"] + joined["rejected"] + joined["unverified"]
                   if r["pair"] == "LEDGER:RA-A6::v_PSB"]
    rejected = [r for r in joined["rejected"]
                if r["pair"] == "LEDGER:RA-A6::v_PSB"
                and r["provider"] == TRACEHQ]
    verified = [r for r in joined["verified"]
                if r["pair"] == "LEDGER:RA-A6::v_PSB"
                and r["provider"] == CYCLE1]
    return {
        "need_dom": need_dom, "need_rule": need_rule,
        "cycle1_dom": c1_dom, "cycle1_rule": c1_rule,
        "tracehq_dom": hq_dom, "tracehq_rule": hq_rule,
        "token_join_providers": sorted(r["provider"] for r in token_pairs),
        "rejected": rejected, "verified": verified,
        "mutation_applied": mutated != hq_text,
    }


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------
REQUIRED_RECORD_KEYS = {"key", "dom", "cod", "map_type", "source_file", "receipt"}
RECORD_FLOOR = 20          # measured at mint: 33; never raise to go green
TYPED_PAIR_FLOOR = 1       # the v_PSB verified pair; never lower to go green


def run_audit() -> tuple[list[str], list[str]]:
    fails: list[str] = []
    report: list[str] = []

    def fail(msg):
        fails.append(msg)
        report.append("  [FAIL] " + msg)

    try:
        ref = load_reference()
    except ReferenceMissing as exc:
        fail(f"CT-1 codomain unavailable (fail closed): {exc}")
        return fails, report
    try:
        register = load_register()
    except ReferenceMissing as exc:
        fail(f"homonym register unavailable (fail closed): {exc}")
        return fails, report

    sidecar = load_sidecar()
    # A malformed sidecar is a RED, never a traceback: fail closed on shape
    # before any check reads a key that may not be there.
    for section in ("records", "sense_discriminators",
                    "sense_discriminators_refused", "dom_aliases", "sources"):
        if section not in sidecar:
            fail(f"sidecar is missing its {section!r} section")
    records = sidecar.get("records", [])
    report.append(f"  reference: {len(ref['object_ids'])} CT-1 object ids, "
                  f"{len(ref['layer_tokens'])} layer tokens, "
                  f"{len(ref['map_tokens'])} map-type tokens; "
                  f"register: {len(register)} homonym tokens")

    # --- A. sidecar well-formedness ---------------------------------------
    for i, rec in enumerate(records):
        where = f"record[{i}] key={rec.get('key')!r}"
        if set(rec) != REQUIRED_RECORD_KEYS:
            fail(f"{where}: keys {sorted(rec)} != the six-key record shape")
            continue
        if not isinstance(rec["key"], str) or not rec["key"].strip():
            fail(f"{where}: empty key")
        src = ROOT / rec["source_file"]
        if not src.is_file():
            fail(f"{where}: source_file missing: {rec['source_file']}")
        r = rec["receipt"]
        if not isinstance(r, dict) or set(r) != {"site", "rule", "quote"}:
            fail(f"{where}: receipt shape is not {{site, rule, quote}}")

    # --- B. codomain compliance against CT-1 (fail closed on drift) --------
    for i, rec in enumerate(records):
        for slot in ("dom", "cod"):
            val = rec.get(slot, "")
            if val in MARKERS:
                continue
            if val.startswith("HOM:"):
                tok = val[4:].rsplit("#", 1)[0]
                try:
                    idx = int(val.rsplit("#", 1)[1])
                except (IndexError, ValueError):
                    fail(f"record[{i}] {slot}={val!r}: malformed sense id")
                    continue
                if tok not in register:
                    fail(f"record[{i}] {slot}={val!r}: token not a registered "
                         f"homonym")
                elif not 1 <= idx <= register[tok]["sense_count"]:
                    fail(f"record[{i}] {slot}={val!r}: sense index out of range "
                         f"(register has {register[tok]['sense_count']})")
                continue
            if val not in ref["object_ids"]:
                fail(f"record[{i}] {slot}={val!r}: not a CT-1 object id, "
                     f"marker, or registered sense id")
        mt = rec.get("map_type", "")
        if mt not in ref["map_tokens"]:
            fail(f"record[{i}] map_type={mt!r}: not a CT-1 arrow label")

    # --- C. receipts live, byte-level -------------------------------------
    for i, rec in enumerate(records):
        src = ROOT / rec["source_file"]
        if not src.is_file():
            continue
        quote = rec["receipt"]["quote"]
        if quote not in read(src):
            fail(f"record[{i}] key={rec['key']!r}: receipt quote absent from "
                 f"{rec['source_file']} -- the record lost its receipt")

    # --- D. every record is RE-DERIVABLE (anti-forgery) --------------------
    live = extract_records(sidecar, ref)
    live_index = {(r["receipt"]["site"], r["key"]): r for r in live}
    for i, rec in enumerate(records):
        found = live_index.get((rec["receipt"]["site"], rec["key"]))
        if found is None:
            fail(f"record[{i}] key={rec['key']!r} site={rec['receipt']['site']!r}"
                 f": no longer derivable from the tree by any rule")
            continue
        for slot in ("dom", "cod", "map_type"):
            if found[slot] != rec.get(slot):
                fail(f"record[{i}] key={rec['key']!r}: recorded {slot}="
                     f"{rec.get(slot)!r} but rule "
                     f"{found['receipt']['rule']!r} re-derives "
                     f"{found[slot]!r}")
    unrecorded = sorted(set(live_index) - {(r["receipt"]["site"], r["key"])
                                           for r in records})
    report.append(f"  records: {len(records)} recorded, {len(live)} derivable "
                  f"live, {len(unrecorded)} UNRECORDED (printed, not ratcheted "
                  f"-- see the docstring)")
    for site, key in unrecorded[:20]:
        report.append(f"    UNRECORDED {key} @ {site}")
    if len(records) < RECORD_FLOOR:
        fail(f"sidecar holds {len(records)} records, below the mint floor "
             f"{RECORD_FLOOR}; never lower the floor to go green")

    # --- E. discriminator law: NO DISCRIMINATOR WITHOUT A RECEIPT ----------
    reg_text = read(REGISTER) if REGISTER.is_file() else ""
    for entry in sidecar.get("sense_discriminators", []):
        tok = entry["token"]
        if tok not in register:
            fail(f"discriminator {tok!r}: not a kind:homonym register entry")
            continue
        if len(entry["senses"]) != register[tok]["sense_count"]:
            fail(f"discriminator {tok!r}: {len(entry['senses'])} senses "
                 f"recorded, register has {register[tok]['sense_count']}")
        for needle in entry["receipts"]["register_must_contain"]:
            if needle not in reg_text:
                fail(f"discriminator {tok!r}: register no longer contains "
                     f"{needle!r}; the discriminator lost its receipt")
        # Disjointness is a FACT ABOUT THE FILES, re-measured every run.
        for sense in entry["senses"]:
            own = ROOT / sense["owning_file"]
            if not own.is_file():
                fail(f"discriminator {tok!r} sense {sense['index']}: owning "
                     f"file missing: {sense['owning_file']}")
                continue
            own_text = read(own)
            if not any(d in own_text for d in sense["discriminators"]):
                fail(f"discriminator {tok!r} sense {sense['index']}: none of "
                     f"{sense['discriminators']} occurs in its owning file")
            for other in entry["senses"]:
                if other["index"] == sense["index"]:
                    continue
                bleed = [d for d in other["discriminators"] if d in own_text]
                if bleed:
                    fail(f"discriminator {tok!r}: sense {other['index']} "
                         f"discriminator(s) {bleed} occur in sense "
                         f"{sense['index']}'s owning file -- NOT byte-disjoint")
    for entry in sidecar.get("sense_discriminators_refused", []):
        if not entry.get("reason", "").strip():
            fail(f"refused discriminator {entry.get('token')!r}: no reason")

    # --- F. dom_aliases under the same receipt law ------------------------
    for entry in sidecar.get("dom_aliases", []):
        receipts = entry.get("receipts")
        if not receipts:
            fail(f"dom_alias {entry.get('class')} has NO receipt -- the alias "
                 f"law forbids it (FX-1's rule, carried)")
            continue
        for receipt in receipts:
            path = ROOT / receipt["path"]
            if not path.is_file() or receipt["must_contain"] not in read(path):
                fail(f"dom_alias {entry.get('class')}: receipt not live")

    # --- G. R2 is declared empty, and that is CHECKED ----------------------
    ledger_rel = FX1.latest_ledger_path()
    ledger = json.loads(read(ROOT / ledger_rel))
    with_context = [r["id"] for r in ledger["rows"] if "context" in r]
    r2 = sidecar.get("sources", {}).get("R2_ledger_context", {})
    if with_context and not r2.get("available", True):
        fail(f"R2 declared unavailable but {len(with_context)} ledger rows now "
             f"carry `context` ({ledger_rel}) -- re-extract and re-mint")
    report.append(f"  R2 ledger-context: {len(with_context)} of "
                  f"{len(ledger['rows'])} rows carry `context` in {ledger_rel}")

    # --- H. the typed join, run on the live corpus ------------------------
    joined = typed_join(records, sidecar)
    tot = joined["total"]
    v, rj, uv = (len(joined["verified"]), len(joined["rejected"]),
                 len(joined["unverified"]))
    frac = (v + rj) / tot if tot else 0.0
    pfrac = joined["pairs_decided"] / joined["pairs"] if joined["pairs"] else 0.0
    report.append(f"  typed join over FX-1's live candidates: {tot} "
                  f"(pair, provider) edges -- {v} TYPE-VERIFIED, {rj} "
                  f"TYPE-REJECTED, {uv} TYPE-UNVERIFIED; typed coverage "
                  f"{v + rj}/{tot} = {frac:.4f}")
    report.append(f"  pair-level: {joined['pairs_decided']}/{joined['pairs']} "
                  f"= {pfrac:.4f} candidate pairs DECIDED; "
                  f"{joined['need_typed']}/{joined['pairs']} carry a typed "
                  f"need side; {joined['wide_sampled']} are Tier-2 WIDE rows "
                  f"whose providers FX-1 exposes only as a 3-file sample")
    for row in joined["verified"]:
        report.append(f"    TYPE-VERIFIED  {row['pair']} <- {row['provider']} "
                      f"[{row['need_dom']} = {row['prov_dom']}] "
                      f"({row['need_rule']} / {row['prov_rule']})")
    for row in joined["rejected"]:
        report.append(f"    TYPE-REJECTED  {row['pair']} <- {row['provider']} "
                      f"[{row['need_dom']} != {row['prov_dom']}] "
                      f"({row['need_rule']} / {row['prov_rule']})")
    if v + rj < TYPED_PAIR_FLOOR:
        fail(f"typed join decided {v + rj} edges, below the mint floor "
             f"{TYPED_PAIR_FLOOR}: the typed layer has gone inert")

    # --- I. THE ACCEPTANCE TEST -------------------------------------------
    acc = vpsb_acceptance(records, sidecar)
    report.append(f"  acceptance: RA-A6 need dom={acc['need_dom']} "
                  f"({acc['need_rule']}); cycle1 dom={acc['cycle1_dom']} "
                  f"({acc['cycle1_rule']}); trace-hq dom={acc['tracehq_dom']} "
                  f"({acc['tracehq_rule']})")
    report.append(f"    token join with one injected provide verb offers "
                  f"providers: {acc['token_join_providers']}")
    if not acc["mutation_applied"]:
        fail("acceptance: the planted provide-verb control did not apply -- "
             "the trace-hq line it targets has changed; re-derive the control")
    if acc["need_dom"] != "HOM:v_PSB#1":
        fail(f"acceptance: RA-A6 must resolve to HOM:v_PSB#1 (the (10bar,1,3) "
             f"sense DELTA-2 names), got {acc['need_dom']!r}")
    if acc["cycle1_dom"] != "HOM:v_PSB#1":
        fail(f"acceptance: the cycle1 carrier must resolve to HOM:v_PSB#1, "
             f"got {acc['cycle1_dom']!r}")
    if acc["tracehq_dom"] != "HOM:v_PSB#2":
        fail(f"acceptance: the trace-hq carrier must resolve to HOM:v_PSB#2 "
             f"(the (4,1,2) sense), got {acc['tracehq_dom']!r}")
    if acc["cycle1_dom"] == acc["tracehq_dom"]:
        fail("acceptance: the two v_PSB carriers were NOT distinguished -- "
             "this is the whole point of the typed layer")
    if not acc["rejected"]:
        fail("acceptance: the typed join did NOT reject the wrong-dom "
             "trace-hq provider for LEDGER:RA-A6::v_PSB")
    else:
        report.append("    ACCEPTANCE PASS: wrong-dom provider REJECTED "
                      f"({acc['rejected'][0]['need_dom']} != "
                      f"{acc['rejected'][0]['prov_dom']})")
    if not acc["verified"]:
        fail("acceptance CONTRARY control: the CORRECT cross-file typed join "
             "LEDGER:RA-A6::v_PSB <- cycle1 must SURVIVE and did not")
    else:
        report.append("    CONTRARY CONTROL PASS: correct cross-file join "
                      "SURVIVES as TYPE-VERIFIED")

    # --- J. FX-1 is not consumed by, and does not consume, this lane -------
    fx1_src = read(FX1_PATH)
    if MUTATE == "fx1-consumption":
        fx1_src += "\nSIDECAR = 'lab/process/needs-provides-typed-records.json'\n"
    for needle in ("needs-provides-typed-records",
                   "needs_provides_typed_join_audit"):
        if needle in fx1_src:
            fail(f"FX-1's gate now references {needle!r}: the typed lane has "
                 f"stopped being behaviour-preserving on FX-1")

    # --- K. owning artifact fenced ----------------------------------------
    art = ROOT / ARTIFACT
    if not art.is_file():
        fail(f"owning artifact missing: {ARTIFACT}")
    else:
        art_text = read(art)
        for needle in ("GU-COMPARATOR-ROUTING",
                       "lab/methods/source-native-comparator-routing.md",
                       "target_claim: NONE-NOT-A-KILL"):
            if needle not in art_text:
                fail(f"owning artifact missing {needle!r}")
        if not re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                         art_text):
            fail("owning artifact missing the INTERNAL_STRUCTURAL_ONLY "
                 "classification in the routing audit's accepted form")

    return fails, report


def main() -> int:
    fails, report = run_audit()
    print("needs_provides_typed_join_audit")
    for line in report:
        print(line)
    print(f"CERTIFICATE: {len(fails)} FAIL, exit {0 if not fails else 1}")
    return 0 if not fails else 1


MUTATIONS = (
    "ref-gone", "ref-layer-drift", "ref-object-row-blind", "register-gone",
    "sidecar-forged-dom", "sidecar-forged-alias", "sidecar-quote-drift",
    "discriminator-not-disjoint", "sense-collapse", "block-fence-blind",
    "maptype-blind", "fx1-consumption",
)


def selftest(poison: bool) -> int:
    env = dict(os.environ)
    env.pop("CT3_MUTATE", None)
    if poison:
        env["CT3_MUTATE"] = "ref-gone"
    base = subprocess.run([sys.executable, str(Path(__file__).resolve())],
                          cwd=str(ROOT), env=env, capture_output=True, text=True)
    print("SELFTEST: clean baseline first --")
    print("  " + (base.stdout.strip().splitlines() or ["<no output>"])[-1])
    if base.returncode != 0:
        print("SELFTEST: clean baseline does NOT pass; mutations were NOT run")
        print("SELFTEST FAILED")
        return 1
    if poison:
        print("SELFTEST: baseline poisoned yet passed -- the guard is inert")
        print("SELFTEST FAILED")
        return 1
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ)
        env["CT3_MUTATE"] = m
        r = subprocess.run([sys.executable, str(Path(__file__).resolve())],
                           cwd=str(ROOT), env=env, capture_output=True, text=True)
        completed = "CERTIFICATE:" in r.stdout
        genuine = "[FAIL]" in r.stdout
        caught = r.returncode == 1 and completed and genuine
        label = ("caught (exit 1, genuine [FAIL])" if caught else
                 "MISSED (exit 0)" if r.returncode == 0 else
                 "CRASH-NOT-DETECTION (no certificate line)")
        print(f"  mutation {m}: {label}")
        ok = ok and caught
    print("SELFTEST " + (f"GREEN: clean baseline first, then {len(MUTATIONS)}/"
                         f"{len(MUTATIONS)} machinery/reference mutations each "
                         f"exit 1 via genuine [FAIL] lines"
                         if ok else "FAILED"))
    return 0 if ok else 1


class NeedsProvidesTypedJoinAudit(unittest.TestCase):
    """The gate's assertions, also runnable under unittest (FX-1's shape)."""

    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.fails, cls.report = run_audit()

    def test_typed_join_audit_is_green(self) -> None:
        for line in self.report:
            print(line)
        self.assertEqual(
            [], self.fails,
            "typed-join audit findings (each is a real red: sidecar schema, "
            "CT-1 codomain drift, a lost receipt, a non-re-derivable record, "
            "a discriminator without a receipt, or the v_PSB acceptance test)")


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(selftest(poison="--poison" in sys.argv
                          or "--poison-baseline" in sys.argv))
    if "--emit" in sys.argv:
        sc = load_sidecar()
        sc["records"] = extract_records(sc, load_reference())
        SIDECAR.write_text(json.dumps(sc, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
        print(f"emitted {len(sc['records'])} records -> {SIDECAR}")
        sys.exit(0)
    sys.exit(main())
