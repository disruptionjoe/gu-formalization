#!/usr/bin/env python3
"""Join declared NEEDS against claimed SUPPLY, so both halves of an answer
cannot sit in the tree unjoined.

THE FAILURE CLASS (measured, not hypothesized).  The costliest recurring
failure in this repository is no longer re-derivation; it is UN-COMPOSED
ADJACENCY: both halves of an answer present, never joined.

  * SA-1 (2026-08-16): the `SOLDERED-AD` selector was built NINE DAYS before
    MD-1 declared the fork open — `P_H` is by definition the associated bundle
    of the chimeric frame bundle (k77-global-chimeric-spin-reduction-…
    -2026-08-05), while MD-1 (2026-08-14) named the settling gate and called
    it cheap.  Nobody composed the two.
  * SC-A (2026-08-15): the correct chain node `SU(3,2)` had been in ~20 files
    since 2026-07-06 while three sites carried the group-theoretically
    impossible `Spin(3,2)` variant — one token apart.
  * BD-C (2026-08-15): a 2026-08-09 source re-inspection recorded the metric
    variation as "explicit through `MET(X)`"; six days later two independent
    routes (OT-1, LA-11) called that leg unsupplied.

Retrieval-before-work does not catch this class: the searches would have
succeeded had anyone thought to run them.  This gate is the mechanical JOIN
between what artifacts DECLARE THEY NEED and what artifacts CLAIM TO SUPPLY.

WHAT IS JOINED — exact surfaces only, no semantic matching:

  NEED sites (declared, greppable):
    LEDGER  the latest conditional-physics-ledger's `distance` and
            `revival_trigger` fields, non-superseded rows;
    FORK    open rows of lab/process/layer0-fork-registry.yaml (an open fork
            is a declared need: its horns name what would settle it);
    ART     first-party joe-directed artifacts: frontmatter `blocked_on:` /
            `layer_open:` / `fork_declared` horn lines, plus body lines
            containing a NEED VERB (blocked on / owed / requires / missing /
            unbuilt / unsupplied / not supplied) AND at least one join key.

  PROVIDE sites: any first-party corpus line containing a non-negated
  PROVIDE VERB (constructs / builds / built / supplies / establishes) AND at
  least one join key.

  JOIN KEYS — three exact shapes, nothing else:
    K1  underscore identifiers with >= 1 capital (`P_H`, `Q_B`, `E_act`,
        `Pi_RS^phys`), excluding ALL_CAPS_UNDERSCORE status vocabulary and
        YAML field names;
    K2  callable/group forms (`SU(3,2)`, `Cl(7,7)`, `MET(X)`, `Sym^2(Q*)`);
    K3  ALL-CAPS hyphenated names without digits (`SOLDERED-AD`), excluding
        an explicit status-vocabulary stoplist and register/work-item IDs
        (those carry digits).
  Tokens are read both inside backticks and bare, because the 2026-08-05
  provider of the SA-1 case writes `(P_H)` with no backticks.

  ALIASES.  Where one object lives under two notations, the join uses the
  explicit table lab/process/needs-provides-alias-table.json.  Every entry
  cites the artifact pair that proved the synonymy, and this gate verifies
  those receipts byte-level every run.  NO ALIAS WITHOUT A RECEIPT: a planted
  case-variant control asserts that un-aliased notations do NOT join.

  TIERS.  A key naming <= WIDE_CAP provider files yields full pairs (Tier 1).
  A key with more providers is NON-DISCRIMINATING; the need site still
  surfaces as a WIDE row (Tier 2) with the provider count, because the two
  documented cases (`P_H`, `Met(X)`) are exactly of this kind — the join must
  not hide them behind a frequency cutoff.

A HIT IS A CANDIDATE, NEVER A VERDICT.  This gate auto-closes nothing.  Every
pair is printed every run, typed from the ADJUDICATED map below the way AR-1
typed its rows: LIVE_CANDIDATE / ALREADY_COMPOSED / SUPERSEDED / UNTYPED.
Preserved negative results and correctly-killed routes must not be
resurrected: pairs whose key appears in a disavowed-by-source register claim
are printed with a DISAVOWED-FENCE flag, and adjudications cite their
receipts.  AR-1's hostile pass measured a 40% error rate on rows inherited
from prior inventories and 0% on rows verified against a file fact — every
adjudication below names a file fact.

RATCHET.  UNADJUDICATED_BASELINE is the number of un-adjudicated candidate
pairs at introduction.  It may only ratchet DOWN; never raise it to go green.
Structure follows process_gates/source_native_comparator_routing_audit.py.

This is a process gate about composition hygiene.  It adjudicates no physics,
moves no verdict and kills nothing (target_claim: NONE-NOT-A-KILL at the
owning artifact,
lab/active-research/joe-directed/composition/fx1-needs-provides-join-2026-08-16.md).
"""

from __future__ import annotations

import json
import os
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALIAS_TABLE = ROOT / "lab/process/needs-provides-alias-table.json"
FORK_REGISTRY = ROOT / "lab/process/layer0-fork-registry.yaml"
CLAIM_REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
ARTIFACT = "lab/active-research/joe-directed/composition/fx1-needs-provides-join-2026-08-16.md"

SKIP_DIRS = {"_local", ".git", "__pycache__", ".pytest_cache", "node_modules"}
# The composition channel is excluded from the corpus for the same reason
# AR-1 excluded archaeology from its sweeps: an artifact ABOUT needs/provides
# quotes the language and keys the join detects, so counting it would make the
# join a measure of its own genre.  The frozen Zenodo copy duplicates tracked
# files and is excluded so one object cannot count as two providers.
CORPUS_EXCLUDE = (
    "lab/active-research/joe-directed/composition/",
    "papers/candidates/located-not-forced/zenodo-package-v1.0.0/",
)
NEED_ART_PREFIX = "lab/active-research/joe-directed/"
# The archaeology channel is inventory genre: it QUOTES need statements it
# catalogues (AR-1 excluded the same channel from its own sweeps for the same
# reason).  Its rows cite the first-party bearer, which is in scope directly.
NEED_ART_EXCLUDE = ("lab/active-research/joe-directed/archaeology/",)
# Stewardship records and overviews POINT AT bearers of needs and supply;
# they do not bear either (same doc_type rationale as the routing audit's
# derived scope).  Counting them would double-count every inventoried row —
# and AR-1 measured 40% decay on exactly such inherited inventory rows.
NON_BEARER_DOC_TYPES = ("stewardship_record", "overview")

NEED_VERB = re.compile(
    r"\b(?:blocked\s+on|blocked_on|owed|requires?|required|missing|unbuilt"
    r"|unsupplied|not\s+supplied)\b",
    re.IGNORECASE,
)
PROVIDE_VERB = re.compile(
    r"\b(?:constructs?|constructed|builds?|built|supplies|supplied"
    r"|establish(?:es|ed)?)\b",
    re.IGNORECASE,
)
# "does not build", "never constructed", "nothing supplies", "un-built":
# a negated provide claim is an ADMISSION, not supply.
NEG_TAIL = re.compile(
    r"\b(?:not|never|no|nor|cannot|nothing|neither|without|un)[\s-]*$",
    re.IGNORECASE,
)

# Parens are deliberately NOT in K1's continuation class: `gamma(q_H)` must
# yield `q_H`, not the unbalanced `q_H)` (leak found at introduction).
K1 = re.compile(r"\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9{}^\\*]+)+(?:\^[A-Za-z0-9{}\\*]+)?")
K2 = re.compile(r"\b[A-Z][A-Za-z0-9^]{0,11}\(\s*[A-Za-z0-9,*^{}\- ]{1,12}\s*\)")
K3 = re.compile(r"\b[A-Z]{2,}(?:-[A-Z]{2,})+\b(?!-?\d)")

# YAML/frontmatter field names look like K1 tokens; they are infrastructure,
# not objects.
INFRA_STOP = {
    "artifact_type", "blocked_on", "canon_verdict_change", "canonical_effect",
    "construction_scope", "depends_on", "doc_type", "fan_out", "fork_assumed",
    "fork_declared", "fork_decided_partially", "frontier_grade",
    "grants_retyped", "layer_decided", "layer_open", "mapping_grade",
    "next_work_queue", "pair_count", "pinned_at", "priority_change",
    "record_kind", "reason_kind", "registry_change", "revival_trigger",
    "row_change", "row_status", "rows_advanced", "rows_touched",
    "schema_version", "settled_at", "settled_by", "settled_how",
    "settled_side", "source_row", "split_from", "steering_effect",
    "target_claim", "updated_at", "updated_by_evidence", "work_item",
}
# Status/verdict vocabulary in CAPS-hyphen shape.  These type statements;
# they do not name objects.  Explicit, printable, extendable only here.
STOP_K3 = {
    "AUTHOR-STATED", "CURRENT-STATE", "DONE-ELSEWHERE", "GU-COMPARATOR-ROUTING",
    "LIVE-CHECK", "LIVE-GAP", "LIVE-HYGIENE", "NEVER-BUILT", "NEXT-STEPS",
    "NONE-NOT-A-KILL", "NOT-DETERMINED", "OUT-OF-SCOPE", "PATH-DRIFT",
    "README", "REQUIRES-UNKNOWN", "ROUTE-KILLED", "SOURCE-CONFIRMED",
    "SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-DENIES", "SOURCE-EXACT",
    "SOURCE-OPEN", "SOURCE-SILENT", "TYPE-MISSING", "UNDER-DETERMINED",
    "UTF-8", "WRONG-TYPE",
}
# Status vocabulary is CAPS WORDS joined by underscores (MISSING_CONSTRUCTION,
# DEWITT_FRAME): every segment >= 2 letters.  Single-letter segments are math
# subscripts (`P_H`, `Q_B`, `Y_C`) and MUST survive — the first draft of this
# pattern used [A-Z]+ and silently deleted the SA-1 case's own join key P_H;
# test_key_classes_reject_noise now pins both directions.
ALL_CAPS_UNDERSCORE = re.compile(r"^[A-Z]{2,}(?:_[A-Z]{2,})+$")

# Keys naming more provider files than this are non-discriminating; their
# need sites surface as WIDE rows instead of per-provider pairs.  6 was
# measured at introduction: `P_H` (18 providers) and `Met(X)` (25) — the two
# documented-case keys — sit above it, which is WHY Tier 2 exists.
WIDE_CAP = 6


def tokens_of(text: str) -> set[str]:
    out: set[str] = set()
    for m in K1.finditer(text):
        tok = m.group(0)
        if tok.lower() in INFRA_STOP:
            continue
        if ALL_CAPS_UNDERSCORE.fullmatch(tok):
            continue
        if not any(c.isupper() for c in tok):
            continue
        if tok.endswith((".py", ".md", ".json", ".yaml")):
            continue
        out.add(tok)
    for m in K2.finditer(text):
        out.add(re.sub(r"\s+", "", m.group(0)))
    for m in K3.finditer(text):
        tok = m.group(0)
        if tok in STOP_K3:
            continue
        out.add(tok)
    return out


def walk_md() -> list[str]:
    rels: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), ROOT).replace(os.sep, "/")
            if any(rel.startswith(p) for p in CORPUS_EXCLUDE):
                continue
            rels.append(rel)
    return sorted(rels)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8", errors="replace")


def is_non_bearer(text: str) -> bool:
    head = text[:400]
    return any(f"doc_type: {kind}" in head for kind in NON_BEARER_DOC_TYPES)


def latest_ledger_path() -> str:
    best, best_n = None, -1
    for fn in os.listdir(ROOT / "lab/process"):
        m = re.fullmatch(r"conditional-physics-ledger-v0\.(\d+)\.json", fn)
        if m and int(m.group(1)) > best_n:
            best_n, best = int(m.group(1)), fn
    if best is None:
        raise AssertionError("no conditional-physics-ledger found")
    return f"lab/process/{best}"


def load_aliases() -> tuple[list[dict], dict[str, str]]:
    """Return (entries, token -> class representative)."""
    table = json.loads(ALIAS_TABLE.read_text(encoding="utf-8"))
    entries = table["aliases"]
    rep: dict[str, str] = {}
    for entry in entries:
        cls = entry["class"]
        head = cls[0]
        for tok in cls:
            rep[tok] = head
    return entries, rep


def disavowed_key_texts() -> str:
    """Concatenated claim/verbatim text of disavowed-by-source register rows."""
    text = CLAIM_REGISTER.read_text(encoding="utf-8")
    blocks = re.split(r"\n- id: ", text)
    out: list[str] = []
    for block in blocks[1:]:
        if re.search(r"^  core: disavowed-by-source$", block, re.M):
            out.append(block)
    return "\n".join(out)


def extract(extra_md: dict[str, str] | None = None):
    """Return (need_sites, provider_files, provider_lines, bearer_text).

    need_sites: list of (site_id, keys, excerpt) where site_id is
      LEDGER:<row>, FORK:<id>, or ART:<relpath> (stable across line drift).
    provider_files: key -> set of provider rel paths.
    bearer_text: site_id -> full carrier text (for composition pre-typing).
    """
    md: dict[str, str] = {rel: read(rel) for rel in walk_md()}
    if extra_md:
        md.update(extra_md)

    need_sites: list[tuple[str, set[str], str]] = []
    bearer_text: dict[str, str] = {}

    ledger_rel = latest_ledger_path()
    ledger = json.loads(read(ledger_rel))
    for row in ledger["rows"]:
        if row.get("row_status") == "SUPERSEDED":
            continue
        text = f"{row.get('distance') or ''} ; {row.get('revival_trigger') or ''}"
        keys = tokens_of(text)
        if keys:
            sid = f"LEDGER:{row['id']}"
            need_sites.append((sid, keys, text.strip()[:150]))
            bearer_text[sid] = json.dumps(row)

    fork_text = FORK_REGISTRY.read_text(encoding="utf-8")
    for block in re.split(r"\n  - id: ", fork_text)[1:]:
        fork_id = block.split("\n", 1)[0].strip()
        if not re.search(r"^\s{4}status: open$", block, re.M):
            continue
        keys = tokens_of(block.split("sources:")[0]) - {fork_id}
        if keys:
            sid = f"FORK:{fork_id}"
            need_sites.append((sid, keys, f"open fork {fork_id}"))
            bearer_text[sid] = block

    art_hits: dict[str, tuple[set[str], str]] = {}
    for rel, text in sorted(md.items()):
        synthetic = extra_md is not None and rel in extra_md
        if not synthetic and not rel.startswith(NEED_ART_PREFIX):
            continue
        if not synthetic and any(rel.startswith(p) for p in NEED_ART_EXCLUDE):
            continue
        if is_non_bearer(text):
            continue
        lines = text.splitlines()
        fm_end = 0
        if lines and lines[0].strip() == "---":
            for i in range(1, min(len(lines), 200)):
                if lines[i].strip() == "---":
                    fm_end = i
                    break
        in_horns = False
        for i, line in enumerate(lines, 1):
            hit = False
            if i <= fm_end:
                if re.match(r"\s*horns:", line):
                    in_horns = True
                    continue
                if in_horns and re.match(r'\s*- "', line):
                    hit = True
                elif in_horns and not re.match(r"\s*- ", line):
                    in_horns = False
                if re.match(r"\s*(blocked_on|layer_open):", line):
                    hit = True
            elif NEED_VERB.search(line):
                hit = True
            if not hit:
                continue
            keys = tokens_of(line)
            if not keys:
                continue
            old_keys, old_excerpt = art_hits.get(rel, (set(), line.strip()[:150]))
            art_hits[rel] = (old_keys | keys, old_excerpt)
        if rel in art_hits:
            sid = f"ART:{rel}"
            keys, excerpt = art_hits[rel]
            need_sites.append((sid, keys, excerpt))
            bearer_text[sid] = text

    provider_files: dict[str, set[str]] = {}
    provider_lines = 0
    for rel, text in sorted(md.items()):
        if is_non_bearer(text):
            continue
        for line in text.splitlines():
            m = PROVIDE_VERB.search(line)
            if not m:
                continue
            if NEG_TAIL.search(line[: m.start()]):
                continue
            keys = tokens_of(line)
            if not keys:
                continue
            provider_lines += 1
            for key in keys:
                provider_files.setdefault(key, set()).add(rel)
    return need_sites, provider_files, provider_lines, bearer_text


def join(extra_md: dict[str, str] | None = None):
    """Return (pairs, wide, non_discriminating) after alias closure.

    pairs: pair_id -> dict(key, providers, excerpt, mech)
    wide:  pair_id -> dict(key, provider_count, sample, excerpt, mech)
    pair_id = "<site_id>::<key representative>"
    """
    entries, rep_map = load_aliases()
    need_sites, provider_files, _, bearer_text = extract(extra_md)

    rep_providers: dict[str, set[str]] = {}
    for key, rels in provider_files.items():
        rep_providers.setdefault(rep_map.get(key, key), set()).update(rels)

    disavowed = disavowed_key_texts()
    pairs: dict[str, dict] = {}
    wide: dict[str, dict] = {}
    non_discriminating: dict[str, int] = {}
    for sid, keys, excerpt in need_sites:
        own_rel = sid.split(":", 1)[1] if sid.startswith("ART:") else None
        for key in sorted(keys):
            rep = rep_map.get(key, key)
            providers = set(rep_providers.get(rep, set()))
            if own_rel:
                providers.discard(own_rel)
            if not providers:
                continue
            carrier = bearer_text.get(sid, "")
            composed = sorted(
                p for p in providers if os.path.basename(p) in carrier
            )
            mech = "cites-a-provider" if composed else "uncited"
            fence = " DISAVOWED-FENCE" if rep in disavowed or key in disavowed else ""
            record = {
                "key": rep,
                "excerpt": excerpt,
                "mech": mech + fence,
                "composed_with": composed,
            }
            pair_id = f"{sid}::{rep}"
            if len(providers) > WIDE_CAP:
                non_discriminating[rep] = len(providers)
                record["provider_count"] = len(providers)
                record["sample"] = sorted(providers)[:3]
                wide[pair_id] = record
            else:
                record["providers"] = sorted(providers)
                pairs[pair_id] = record
    return pairs, wide, non_discriminating


# ---------------------------------------------------------------------------
# ADJUDICATIONS — every pair found at introduction (2026-08-16), typed by a
# reader against file facts, the way AR-1 typed its rows.  A type here is a
# reading, not an auto-close: LIVE_CANDIDATE pairs are open work; the note
# names the file fact each typing stands on.  Full receipts:
# lab/active-research/joe-directed/composition/fx1-needs-provides-join-2026-08-16.md §5.
# Never delete a row to go green; supersede it with a dated note.
# ---------------------------------------------------------------------------
LIVE_CANDIDATE = "LIVE_CANDIDATE"
ALREADY_COMPOSED = "ALREADY_COMPOSED"
SUPERSEDED = "SUPERSEDED"
UNTYPED = "UNTYPED"

ADJUDICATED: dict[str, tuple[str, str]] = {
    # ================= TIER 1 (35 pairs) =================
    "ART:lab/active-research/joe-directed/baryon-number-and-proton-decay/bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md::SU(3,2)": (
        LIVE_CANDIDATE,
        "CP-1 2026-08-17 adjudication (supersedes the FX-1 introduction note; "
        "dated-note mechanism per this file's header): CONSISTENT, no "
        "amendment owed on either side.  The presupposition sits in CI-X04 "
        "itself (curt-iceberg-native-crosswalk.json: CURT_REPORT_OF_AUTHOR_"
        "CLAIM / UNTESTED_PHENOMENOLOGY), and BD-1 already fences the "
        "identification ('the reported object is `SU(3,2)`, the computed "
        "object is `so(6,4)`', its section 5) and keeps the grade unchanged.  "
        "SC-A's R6 is reconstruction-grade with the audio check still owed "
        "and SC-GRP-50 proposed-unwritten, so no composition may promote it "
        "to a source determination, and none does.  Executor routing plus "
        "the one new computable object (B-charge classification of "
        "su(3,2)'s image under SC-A's fibrewise embedding against BD-1's "
        "k/p partition): composition/cp1-three-live-pairs-adjudicated-"
        "2026-08-17.md section 5.  BD-1 (08-14) is frozen and predates SC-A "
        "(08-15); the ledger has no surface for this pair, so NO DELTA IS "
        "OWED ANYWHERE.  Type stays LIVE_CANDIDATE only because the FX-1 "
        "probe's C6 pins the introduction counts/set by equality and is not "
        "CP-1's to edit; the FX-1 owner should flip this entry to "
        "ALREADY_COMPOSED (composed-by-adjudication) at the next C6 refresh "
        "and preserve this note.",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb4-h210-fixed-versus-comoving-ps-typing-2026-08-16.md::V_10": (
        UNTYPED,
        "live sibling channel mid-flight (2026-08-16): he4-source-owner-"
        "intersection may already be the join; the channel owner adjudicates, "
        "not this pass",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb4-wave-h210-naturality-reprioritization-2026-08-16.md::O(6,4)": (
        UNTYPED,
        "live sibling channel; O(6,4) is the shared ambient group token — "
        "owner adjudicates",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb8-h210-reverse-nabla-q-completion-2026-08-16.md::L_q": (
        ALREADY_COMPOSED,
        "mech: the need file itself cites provider cb8-h210-derivative-"
        "adapter-forward-covariance-2026-08-16.md — same-wave family join",
    ),
    "ART:lab/active-research/joe-directed/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md::Ad(W)": (
        ALREADY_COMPOSED,
        "bd-b-…-2026-08-15.md cites LA-11 29 times; the base-duality channel "
        "is the composition LA-11 asked for",
    ),
    "ART:lab/active-research/joe-directed/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md::Gamma(AdP)": (
        UNTYPED,
        "the sole provider line (DERIVATION-PROGRESS.md:974) is CONDITIONAL "
        "language — 'remains open only if a precise functor … is supplied' — "
        "not a supply claim.  Kept as the named receipt that the provide-verb "
        "surface cannot see grammatical mood; adjudication is the mood filter.",
    ),
    "ART:lab/active-research/joe-directed/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md::Lie(W)": (
        ALREADY_COMPOSED,
        "same BD-B composition as Ad(W)",
    ),
    "ART:lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md::SU(5)": (
        ALREADY_COMPOSED,
        "SU(5) is the comparator group LA-3 itself fences as comparator-scope; "
        "providers sit on the other side of the routing boundary the fence "
        "names — the composition IS the fence "
        "(lab/methods/source-native-comparator-routing.md)",
    ),
    "ART:lab/active-research/joe-directed/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md::SOLDERED-AD": (
        ALREADY_COMPOSED,
        "sa1-the-selector-is-built-…-2026-08-16.md IS the composition and "
        "lists la4 in its depends_on",
    ),
    "ART:lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-reality-charge-admissibility-2026-08-16.md::X_L": (
        UNTYPED,
        "measured HOMONYM, not a composition: SN-2's X_L is a weak-doublet "
        "neutral slot; canon frame-triviality's X_L is a frame-operator "
        "factor; the CHSH gate's X_L is a Pauli-X control observable.  "
        "Recorded for the homonym channel, which owns that class — no repair "
        "attempted here.",
    ),
    "ART:lab/active-research/joe-directed/majorana-126-neutrino/sn3-existing-varpi-xr-incidence-census-2026-08-16.md::X_R": (
        UNTYPED,
        "live sibling channel (census/classifier written the same day); "
        "owner adjudicates",
    ),
    "ART:lab/active-research/joe-directed/majorana-126-neutrino/sn3-source-slot-neutral-line-incidence-classifier-2026-08-16.md::X_D": (
        ALREADY_COMPOSED,
        "the sole provider is the artifact's own hostile review "
        "(lab/process/hostile-reviews/2026-08-16-joe-directed-sn3-varpi-"
        "incidence-review.md)",
    ),
    "ART:lab/active-research/joe-directed/majorana-126-neutrino/sn3-wave-varpi-incidence-reprioritization-2026-08-16.md::X_R": (
        ALREADY_COMPOSED,
        "mech: the wave file cites both the census and the classifier by name",
    ),
    "ART:lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md::D_varpi": (
        ALREADY_COMPOSED,
        "SA-1's blocked_on names its owner gate BY PATH (selected-k77-moving-"
        "parent-bundle-observation-reduction-2026-08-10.md) — composed by "
        "construction; listed providers are that gate's lineage",
    ),
    "ART:lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md::Spin(1,3)": (
        ALREADY_COMPOSED,
        "context token of the same blocked_on sentence; owner named by path",
    ),
    "ART:lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md::SU(3,2)": (
        ALREADY_COMPOSED,
        "SC-A is itself the composition artifact for this token and cites "
        "H19 and the ch3 repair (mech: cites-a-provider)",
    ),
    "ART:lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md::U(3)": (
        ALREADY_COMPOSED,
        "ch3-…-2026-08-15.md executes SC-A's three-site repair; joint "
        "artifacts of one adjudication",
    ),
    "FORK:EPS-CHARACTER::CH-REC": (
        ALREADY_COMPOSED,
        "the fork row's sources name the provider "
        "(time-orientation-home-for-the-orientation-datum-2026-08-04.md)",
    ),
    "FORK:J-RED-OWNERSHIP::J_h": (
        ALREADY_COMPOSED,
        "the fork row's sources ARE the provider files; its notes track "
        "J_red/J_h as the council's PRE-3 un-owned-object exemplar — open "
        "status is the ownership judgment, not blindness to the port",
    ),
    "FORK:J-RED-OWNERSHIP::J_red": (
        ALREADY_COMPOSED,
        "same file fact as J_h: sources = providers "
        "(resolver-wave-h disposition + science-council 2026-08-04)",
    ),
    "FORK:KINEMATIC-VS-PHYSICAL-CARRIER::Pi_RS^phys": (
        UNTYPED,
        "both provider lines are imperative or hypothetical — 'build "
        "Pi_RS^phys' (portfolio-correction-wave:218), 'through an explicitly "
        "constructed Pi_RS^phys' (woit twistor:610) — need-side language in "
        "provide-verb clothing; the fork itself states the projector DOES NOT "
        "EXIST.  Kept as the second mood-blindness receipt.",
    ),
    "FORK:SIGNATURE-AMBIENT::C_perp": (
        ALREADY_COMPOSED,
        "the fork row's own provenance text computes C_perp = K . J_obs "
        "(registry lines 163-193); providers are that provenance's lineage",
    ),
    "FORK:SIGNATURE-AMBIENT::J_obs": (
        ALREADY_COMPOSED,
        "same provenance file fact as C_perp",
    ),
    "FORK:SIGNATURE-AMBIENT::REAL-CLIFFORD-FORM": (
        ALREADY_COMPOSED,
        "the registry itself settles REAL-CLIFFORD-FORM as a distinct row and "
        "cross-references the distinction inside this row's notes",
    ),
    "FORK:SIGNATURE-AMBIENT::Spin(1,3)": (
        ALREADY_COMPOSED,
        "SA-1 explicitly declines to decide this fork (its NOT list); "
        "Spin(1,3) is the shared observation-chain token",
    ),
    "LEDGER:LT-SM1::zeta_F": (
        ALREADY_COMPOSED,
        "LT-SM7 exists in v0.258, i.e. LA-7's banked split WAS executed; the "
        "current row is the post-split row even though its evidence string "
        "still cites cb-b rather than LA-7",
    ),
    "LEDGER:LT-SM5::Y_C": (
        LIVE_CANDIDATE,
        "CP-1 2026-08-17 adjudication (supersedes the FX-1 introduction "
        "note): CONDITION -- not discharge, not neighbor.  Wave D types the "
        "row's exact objects (Layer-0 rows carry the ordered "
        "Herm(P0^dagger K_G c_rho(T) Y_K P0) / Alt(P0^T C c_rho(T) Y_C P0) "
        "densities) and its section-8 wave-E step 4 is the row's demanded "
        "placement at machinery level -- but its grade line keeps 'total "
        "P0/Y placement, source selection, VEV, and mass remain open' and "
        "its section 9 says 'No total P0/rho/Y_K/Y_C/C full-20 kernel is "
        "built', so NOTHING IS DISCHARGED.  Versionless DELTA-1 against "
        "v0.258 (evidence field gains wave D typed 'machinery only'; "
        "verdict/reason/mapping_grade untouched): composition/cp1-three-"
        "live-pairs-adjudicated-2026-08-17.md section 3.  The second listed "
        "provider (rb4 predecessor record) DOES NOT COMPOSE: its matched "
        "line reads 'no ... placement until the moving reduction and "
        "zero-order P_0/rho/Y_K/Y_C-reality map are built' -- a "
        "non-regression requirement wearing the provide verb (PROVIDER-SIDE "
        "mood-blindness, the supply-side mirror of the two need-side "
        "receipts); rb4's own final boundary reads TYPED / UNSELECTED and "
        "OPEN.  rb4 remains genuine machinery for wave-E step 2 only.  Pair "
        "stays LIVE until the ledger owner applies DELTA-1; then re-type "
        "ALREADY_COMPOSED with the C5/C6 refresh.",
    ),
    "LEDGER:LT-SM5::Y_K": (
        LIVE_CANDIDATE,
        "same pair and same CP-1 2026-08-17 adjudication as Y_C: CONDITION "
        "via wave D (DELTA-1), and the rb4 leg re-typed provider-side "
        "mood-blindness -- see the Y_C note and cp1-three-live-pairs-"
        "adjudicated-2026-08-17.md section 3.",
    ),
    "LEDGER:LT-SM6::E_act": (
        ALREADY_COMPOSED,
        "row evidence cites the v0.237 action-Euler principal-owner "
        "comparison; PD-I2B-ACTION-OWNER carries the composition",
    ),
    "LEDGER:RA-A2::U(3)": (
        ALREADY_COMPOSED,
        "the row summary itself carries the exact S(U(3)xU(2)) result; the "
        "two providers are the chain-repair lineage of that result",
    ),
    "LEDGER:RA-A6::SU(3,2)": (
        ALREADY_COMPOSED,
        "the row's distance already states the Pati-Salam/SU(3,2) "
        "intersection; the SC-A/CH-3 adjudication is banked in the summary "
        "language",
    ),
    "LEDGER:RA-A6::v_PSB": (
        LIVE_CANDIDATE,
        "CP-1 2026-08-17 adjudication (supersedes the FX-1 introduction "
        "note): COMPOSES -- same object verified by LINEAGE RECEIPT, not "
        "token: RA-A6.source_row = CB-A:A6 and cb-a:222 reads 'conditional "
        "on a source-selected rank-one v_PSB in (10bar,1,3)' citing "
        "cycle1:275-283 by filename; the homonym register carries no v_PSB "
        "entry.  The June gate FORMALIZES the object ('source-selected "
        "v_PSB in the rank-one orbit of V_PSB', V_PSB = (10bar,1,3)) and "
        "records it 'not selected by current repo data', so the trigger "
        "fires on a SourceCriticalRankOnePSBSelectionCertificate, never on "
        "formalization.  Versionless DELTA-2 against v0.258 (revival_trigger "
        "field only): composition/cp1-three-live-pairs-adjudicated-"
        "2026-08-17.md section 4.  Surfaced while verifying, first-class "
        "and UNREGISTERED: the 2026-08-12 trace-hq family computes a "
        "DIFFERENT rank-one v_psb = kron(e4, fR) in (4,1,2) under the same "
        "token (stabilizer dim 12 either way, so a numeric check cannot "
        "discriminate; byte-level: cycle1 has zero '(4,1,2)', the trace-hq "
        "gate zero '(10bar,1,3)').  Flagged to the homonym channel, which "
        "owns near-collisions; NOT written into the register by CP-1.  Pair "
        "stays LIVE until the ledger owner applies DELTA-2; then re-type "
        "ALREADY_COMPOSED with the C5/C6 refresh.",
    ),
    "LEDGER:RA-E3::C^(32,32)": (
        ALREADY_COMPOSED,
        "the row's own summary performs the C^(32,32)+C^(32,32) vs U(64,64) "
        "separation; PD-STRUCTURE-TRANSPORT owns the composed lesson",
    ),
    "LEDGER:RA-E3::E_act": (
        ALREADY_COMPOSED,
        "same composition as LT-SM6::E_act",
    ),
    "ART:lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md::FULL-DIRAC": (
        ALREADY_COMPOSED,
        "landed mid-pass from the concurrent FX-2 agent and was caught by "
        "this gate within minutes — the ratchet's designed behavior.  mech: "
        "FX-2 itself cites the provider (cn2-notation-carries-the-answer-"
        "2026-08-15.md) by name; the sibling channel owns both halves.",
    ),
    # ================= TIER 2 WIDE (28 rows) =================
    "ART:lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md::P_H": (
        ALREADY_COMPOSED,
        "DOCUMENTED CASE A, RETRO-DETECTED BY THIS JOIN: MD-1's fork horns "
        "(2026-08-14) name P_H; the 18-file provider set includes "
        "k77-global-chimeric-spin-reduction-and-support-normalization-"
        "2026-08-05.md ('it builds (P_H) from the chimeric spinors'), nine "
        "days older than the fork.  sa1-…-2026-08-16.md is the composition; "
        "had this gate existed on 2026-08-14 the pair would have printed as "
        "NEW-UNADJUDICATED.",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb3-wave-h210-observation-reprioritization-2026-08-16.md::M_3": (
        ALREADY_COMPOSED,
        "mech: wave file cites its own successors (cb5 source-fq bridge)",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb4-wave-h210-naturality-reprioritization-2026-08-16.md::U(3,2)": (
        UNTYPED,
        "live sibling channel plus a 12-provider token; owner adjudicates",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb7-h210-minimal-odd-adapter-classifier-2026-08-16.md::q_H": (
        ALREADY_COMPOSED,
        "mech: cites cb7-forward-reverse-density-duality-composition — "
        "same-wave family",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb8-h210-line-twist-stage-cb6-compatibility-2026-08-16.md::q_H": (
        ALREADY_COMPOSED,
        "mech: same-wave family self-citation",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb8-h210-reverse-nabla-q-completion-2026-08-16.md::q_H": (
        ALREADY_COMPOSED,
        "mech: same-wave family self-citation",
    ),
    "ART:lab/active-research/joe-directed/high-energy-two-plus-one/cb8-wave-h210-derivative-adapter-reprioritization-2026-08-16.md::q_H": (
        ALREADY_COMPOSED,
        "mech: same-wave family self-citation",
    ),
    "ART:lab/active-research/joe-directed/indefiniteness-typing/itc-positivity-rows-are-five-not-ten-2026-08-15.md::Cl(9,5)": (
        ALREADY_COMPOSED,
        "settled-algebra token (77 providers); ITC quotes the G3/M-H17 "
        "lineage it already cites; REAL-CLIFFORD-FORM settlement owns it",
    ),
    "ART:lab/active-research/joe-directed/massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md::mu_DW": (
        ALREADY_COMPOSED,
        "mech: MV-1's directive row cites the W136/W138 issuance battery it "
        "quotes the bound from",
    ),
    "ART:lab/active-research/joe-directed/ownership-theorem/ot2-lt-sm3b-is-not-an-ownership-row-and-the-cheapest-pair-is-the-terminal-pair-2026-08-15.md::d_A": (
        UNTYPED,
        "d_A is a near-floor generic token (10 providers); none of the "
        "listed provider lines addresses the O3b adapter-domain need "
        "(R(R^d) as a proper so(d)-submodule).  Dismissing it by sampling "
        "three of ten files would be exactly the unverified typing AR-1 "
        "measured at 40% error.",
    ),
    "ART:lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md::P_H": (
        ALREADY_COMPOSED,
        "SA-1 is itself the P_H composition (mech: cites the 2026-08-05 "
        "chimeric construction)",
    ),
    "ART:lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md::Spin(6,4)": (
        ALREADY_COMPOSED,
        "ambient block token inside the blocked_on whose owner is named by "
        "path",
    ),
    "ART:lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md::Spin(7,7)": (
        ALREADY_COMPOSED,
        "same blocked_on context; provider sample includes the chimeric "
        "construction SA-1 cites (mech)",
    ),
    "ART:lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md::Spin(6,4)": (
        ALREADY_COMPOSED,
        "SC-A cites its chain sources (mech); Spin(6,4) is the chain's top "
        "node",
    ),
    "FORK:NUMBER-14-METRIC-VS-EXTERIOR::Met(X^4)": (
        UNTYPED,
        "no provider claims the missing GL(4)-equivariant identification the "
        "fork's notes say does not exist; 9-provider token, no composition "
        "opportunity established",
    ),
    "FORK:SIGNATURE-AMBIENT::Cl(7,7)": (
        ALREADY_COMPOSED,
        "horn token (23 providers); PD-SIGNATURE-PARITY is the composed "
        "evidence chain for this fork",
    ),
    "FORK:SIGNATURE-AMBIENT::Spin(6,4)": (
        ALREADY_COMPOSED,
        "the row's own notes state the (6,4) fibre holds on both horns; "
        "fibre token, not unjoined supply",
    ),
    "LEDGER:AC-B2::Cl(7,7)": (
        UNTYPED,
        "wide settled-horn token (23 providers); no provider claims the "
        "Cl(7,7)-appropriate BSO(128)-type receptacle the row asks for",
    ),
    "LEDGER:AC-G1a::Cl(7,7)": (
        UNTYPED,
        "same wide-token reason as AC-B2",
    ),
    "LEDGER:LT-SM8::D_A": (
        UNTYPED,
        "D_A is the generic gauge covariant derivative (9 providers); the "
        "row's coupled BV/detour need is not what any listed line supplies",
    ),
    "LEDGER:RA-A2::SU(2)": (
        UNTYPED,
        "program-wide group token (36 providers); the row's J-selection need "
        "is not addressable through it",
    ),
    "LEDGER:RA-A4::U(1)": (
        UNTYPED,
        "program-wide token (23 providers); the row needs a vacuum mass "
        "matrix for the extra U(1), which no provider line claims",
    ),
    "LEDGER:RA-A6::SU(3)": (
        UNTYPED,
        "program-wide token at the cap boundary (8 providers); the row's "
        "mu_6-quotient need is not what the lines supply",
    ),
    "LEDGER:RA-B9::Spin(10)": (
        UNTYPED,
        "program-wide token (17 providers); row is at 'none at unifying-"
        "representation grade' and watches for a reduction FAILURE",
    ),
    "LEDGER:RA-E1::Q_B": (
        ALREADY_COMPOSED,
        "the row's own distance text performs the Q_B separation; providers "
        "are the K77 BV lineage it quotes",
    ),
    "LEDGER:RA-E3::Q_B": (
        ALREADY_COMPOSED,
        "same in-row separation as RA-E1",
    ),
    "LEDGER:RA-E3::U(64,64)": (
        ALREADY_COMPOSED,
        "the row itself separates U(64,64) from its block subgroups; "
        "providers are that lineage",
    ),
    "LEDGER:RA-E6::U(1)": (
        UNTYPED,
        "program-wide token (23 providers); the row's photon-kernel need is "
        "not what the lines supply",
    ),
}

# Number of un-adjudicated candidate pairs at introduction (2026-08-16).
# Every pair found by the introduction join was typed above, so the baseline
# is ZERO: any new un-adjudicated pair is a red until a reader types it.
# This may only RATCHET DOWN; never raise it to make a new pair go green.
UNADJUDICATED_BASELINE = 0


class NeedsProvidesCompositionAudit(unittest.TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.alias_entries, cls.rep_map = load_aliases()
        cls.pairs, cls.wide, cls.nondisc = join()

    def test_alias_entries_carry_live_receipts(self) -> None:
        """No alias without a receipt — verified byte-level, every run."""
        self.assertGreaterEqual(len(self.alias_entries), 3)
        for entry in self.alias_entries:
            with self.subTest(alias=entry["class"]):
                self.assertGreaterEqual(len(entry["class"]), 2)
                self.assertTrue(entry.get("proved_by"),
                                "alias entry missing its proving artifact")
                receipts = entry["receipts"]
                self.assertGreaterEqual(len(receipts), 2,
                                        "an alias needs the artifact PAIR")
                for receipt in receipts:
                    path = ROOT / receipt["path"]
                    self.assertTrue(path.is_file(), f"receipt gone: {receipt['path']}")
                    text = path.read_text(encoding="utf-8", errors="replace")
                    for needle in receipt["must_contain"]:
                        self.assertIn(needle, text,
                                      f"{receipt['path']} no longer contains "
                                      f"{needle!r}; the alias lost its receipt")

    def test_join_prints_every_pair_and_ratchets(self) -> None:
        everything = {**self.pairs, **self.wide}
        unadjudicated = sorted(set(everything) - set(ADJUDICATED))
        stale = sorted(set(ADJUDICATED) - set(everything))
        counts = {t: 0 for t in (LIVE_CANDIDATE, ALREADY_COMPOSED, SUPERSEDED, UNTYPED)}
        for pair_id, (typ, _) in ADJUDICATED.items():
            if pair_id in everything:
                counts[typ] += 1

        print(f"\nneeds_provides_composition_audit[join]: "
              f"{len(self.pairs)} pairs + {len(self.wide)} wide rows = "
              f"{len(everything)} candidates; "
              f"{len(unadjudicated)} UNADJUDICATED "
              f"(baseline {UNADJUDICATED_BASELINE}); "
              f"types {counts}; "
              f"{len(self.nondisc)} non-discriminating keys; "
              f"{len(stale)} stale adjudications.")
        for pair_id in sorted(everything):
            rec = everything[pair_id]
            typ = ADJUDICATED.get(pair_id, ("NEW-UNADJUDICATED", ""))[0]
            if "providers" in rec:
                supply = "; ".join(rec["providers"][:3])
                extra = len(rec["providers"]) - 3
                if extra > 0:
                    supply += f" (+{extra})"
            else:
                supply = f"{rec['provider_count']} provider files, e.g. " + \
                         "; ".join(rec["sample"])
            print(f"  [{typ:>17}] {pair_id}")
            print(f"        mech={rec['mech']}  supply: {supply}")
        for key, count in sorted(self.nondisc.items()):
            print(f"  NON-DISCRIMINATING {key!r}: {count} provider files")
        for pair_id in stale:
            print(f"  STALE-ADJUDICATION {pair_id} (pair no longer derived; "
                  f"keep the row, mark it superseded when convenient)")

        self.assertLessEqual(
            len(unadjudicated), UNADJUDICATED_BASELINE,
            "NEW un-composed candidate pair(s): "
            + ", ".join(unadjudicated)
            + " — read both halves, type the pair in ADJUDICATED "
            "(LIVE_CANDIDATE / ALREADY_COMPOSED / SUPERSEDED / UNTYPED) with "
            "the file fact that types it, or repair the extractor "
            "deliberately.  Never raise the baseline.")

    def test_adjudication_types_are_typed(self) -> None:
        allowed = {LIVE_CANDIDATE, ALREADY_COMPOSED, SUPERSEDED, UNTYPED}
        for pair_id, (typ, note) in ADJUDICATED.items():
            with self.subTest(pair=pair_id):
                self.assertIn(typ, allowed)
                self.assertTrue(note.strip(), "adjudication without a receipt note")

    def test_documented_cases_stay_composed(self) -> None:
        """The three documented failures must remain joined — regression
        controls, verified against file facts, not against memory."""
        sa1 = read("lab/active-research/joe-directed/soldered-ad/"
                   "sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md")
        self.assertIn("md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md", sa1)
        self.assertIn("k77-global-chimeric-spin-reduction", sa1)
        provider = read("explorations/conditional-build/"
                        "k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
        self.assertIn("it builds (P_H) from the chimeric spinors", provider)

        bdc = read("lab/active-research/joe-directed/base-duality/"
                   "bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md")
        self.assertIn("selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md", bdc)
        reinspection = read("lab/sources/"
                            "selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md")
        self.assertIn("explicit through `MET(X)`", reinspection)

        sca = read("lab/active-research/joe-directed/source-chain/"
                   "sca-right-chain-2026-08-15.md")
        self.assertIn("H19-seven-seven-signature-branch-2026-07-11.md", sca)
        self.assertIn("group-theoretically impossible", sca)

    def test_planted_pair_is_found_and_case_variant_is_not(self) -> None:
        """Detector liveness (a join that returns nothing must fail here) and
        the contrary control: without an alias receipt, notations do NOT join."""
        plant = {
            "lab/active-research/joe-directed/__fx1_plant__.md": (
                "---\ncreated: 2026-08-16\n---\n"
                "The next step requires the `Zorb_Q(7)` compensator.\n"
                "Also missing: the `Vlem_W(3)` half, under its lowercase "
                "spelling `vlem_w(3)` elsewhere.\n"
            ),
            "explorations/__fx1_plant_supply__.md": (
                "---\ncreated: 2026-08-16\n---\n"
                "This artifact constructs the `Zorb_Q(7)` compensator exactly.\n"
                "And it establishes `vlem_w(3)` in the lowercase spelling only.\n"
                "A negated line: it never builds `Zorb_neg(5)`.\n"
            ),
            "lab/active-research/joe-directed/__fx1_plant_neg__.md": (
                "---\ncreated: 2026-08-16\n---\n"
                "This route is blocked on `Zorb_neg(5)`.\n"
            ),
        }
        pairs, wide, _ = join(extra_md=plant)
        everything = {**pairs, **wide}
        self.assertIn(
            "ART:lab/active-research/joe-directed/__fx1_plant__.md::Zorb_Q",
            everything,
            "planted need/provide pair NOT found — the extractor is inert")
        variant_hits = [p for p in everything if "Vlem_W(3)" in p or "vlem_w(3)" in p]
        self.assertEqual(
            [], variant_hits,
            "case-variant joined WITHOUT an alias receipt — fuzzy matching "
            "has crept in")
        neg_hits = [p for p in everything if "Zorb_neg(5)" in p]
        self.assertEqual(
            [], neg_hits,
            "a NEGATED provide claim ('never builds') was counted as supply")

    def test_key_classes_reject_noise(self) -> None:
        self.assertEqual(set(), tokens_of("the row is MISSING_CONSTRUCTION here"))
        self.assertEqual(set(), tokens_of("see register row SC-GEO-07 and LA-11"))
        self.assertEqual(set(), tokens_of("frontmatter blocked_on: and doc_type: here"))
        self.assertEqual({"P_H"}, tokens_of("it builds (P_H) from the chimeric spinors"))
        self.assertEqual({"SU(3,2)"}, tokens_of("the middle node is SU(3,2), not spin"))
        self.assertEqual({"SOLDERED-AD"}, tokens_of("the SOLDERED-AD fork is open"))

    def test_alias_classes_map_documented_notations(self) -> None:
        self.assertEqual(self.rep_map.get("MET(X)"), self.rep_map.get("Met(X)"))
        self.assertEqual(self.rep_map.get("Spin(3,2)"), self.rep_map.get("SU(3,2)"))
        self.assertEqual(self.rep_map.get("Π_RS^phys"), self.rep_map.get("Pi_RS^phys"))
        # And nothing merges classes that have no receipt.
        self.assertNotEqual(self.rep_map.get("MET(X)"), self.rep_map.get("SU(3,2)"))

    def test_owning_artifact_exists_and_is_fenced(self) -> None:
        art = read(ARTIFACT)
        self.assertIn("GU-COMPARATOR-ROUTING", art)
        self.assertIn("lab/methods/source-native-comparator-routing.md", art)
        self.assertRegex(art, r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`")
        self.assertIn("target_claim: NONE-NOT-A-KILL", art)


if __name__ == "__main__":
    unittest.main(verbosity=2)
