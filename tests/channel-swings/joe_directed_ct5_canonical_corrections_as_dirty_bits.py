#!/usr/bin/env python3
"""CT-5 -- canonical corrections as dirty bits, and the Z/3 packet both-states proof.

GU-COMPARATOR-ROUTING: this probe's object is the REPOSITORY'S BOOKKEEPING, not
the physics.  Every number below is a property of file dates, recorded checks
and lowercased substrings.  Classification: INTERNAL_STRUCTURAL_ONLY.  Nothing
here is evidence for or against Weinstein's source-native mechanism and nothing
here binds any conventional comparator.

QUESTION.  `correction_propagation_audit.py` walks CITATION edges and therefore
CANNOT reach a document written before a correction existed -- such a document
never cites the correction's owner, so no edge exists to walk.  Can that class
be made mechanically detectable, and does the detector actually fire on the
incident that motivated it?

ANSWER, in four parts, all certified below.

  (1) THE DETECTOR FIRES ON THE INCIDENT.  `explorations/z3-receptacle-design-
      packet-2026-08-11.md` -- the packet that engaged a route the following
      week's 2+1 sharpening superseded, and which no gate could see -- is
      DIRTY-UNCHECKED for CC-05-SUBTRACTIVE-TWO-PLUS-ONE in the live state,
      and CLEAR once an adjudication for it is recorded.  BOTH states are
      exercised here (tags Z4, Z5), so the detector is shown to have two
      outcomes rather than one.

  (2) IT IS SPECIFIC, NOT INDISCRIMINATE.  A post-correction file that matches
      the same signature is NOT dirty (K1); a fenced comparator resolves
      FENCED, not stale (K2); SCUR-1's declared contrary control CB-E is clean
      (K3); and the packet is dirty for exactly one of CT-5's original ten
      corrections (Z6). Later independently governed canonical corrections may
      extend the registry without weakening these historical pins.

  (3) THE HAND WORK IS BANKED, NOT RE-DONE.  40 records transcribed from
      SCUR-1, FIX-A and RW-1 clear 18 (file, correction) pairs.  That historical
      seed is reconstructed from exact author provenance rather than confused
      with later live sidecar extensions.  The six FIX-A records are
      load-bearing: removing one flips CB-A back to DIRTY-KNOWN-STALE (K5), and
      the five RW-1 records are pinned to their exact provenance rather than
      absorbed into a moving count.

  (4) THE CEILING IS MEASURED, NOT ASSERTED.  Exactly ONE hand-recorded pair
      that a human thought worth writing down does NOT fire its own signature
      (D13: CB-B under CC-08).  That is the recall miss, scored against SCUR-1
      as ground truth, and it is printed every run by the gate itself.

REPRODUCE
    cd /path/to/gu-formalization
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ct5_canonical_corrections_as_dirty_bits.py
    ... --selftest      (failure path: each mutation must drive a genuine [FAIL])

Exact integer arithmetic; no float is constructed anywhere.  The engine, the
registry and the sidecar live in process_gates/canonical_currency_audit.py,
lab/process/correction-registry.yaml and
lab/process/canonical-currency-checks.yaml and are IMPORTED, not copied, so
this probe and the gate cannot drift apart.

NOT: a canon edit, a ledger edit, a verdict movement, a currency adjudication,
a physics derivation, or a claim that the dirty set is the set of stale
documents.  The dirty set is the set of documents NOBODY HAS CHECKED.
"""
from __future__ import annotations

import copy
import importlib.util
import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location(
    "cca", ROOT / "process_gates" / "canonical_currency_audit.py")
G = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(G)

# --------------------------------------------------------------------------
# Pins.  Held HERE, independently of the sidecar's own ratchet baseline, so
# that editing the baseline cannot silently absorb this probe's controls
# (VERIFICATION.md rule 6).
# --------------------------------------------------------------------------
CANON_IDS = (
    "CC-01-MET-X-ARGUMENT",
    "CC-02-OBSERVED-POSITIVITY-OPEN",
    "CC-03-FOUR-CORNER-NONCHIRAL",
    "CC-04-NORMAL-BUNDLE-RIGHT-CHAIN",
    "CC-05-SUBTRACTIVE-TWO-PLUS-ONE",
    "CC-06-CHIRALITY-VEV-CONDITIONAL",
    "CC-07-CONTRACTION-NOT-KK",
    "CC-08-DARK-PARTNER-OBLIGATION",
    "CC-09-YUKAWA-REPULSIVE-SIGN",
    "CC-10-UCSD-EDITED-DERIVATIVE",
)
CANON_SINCE = {
    "CC-01-MET-X-ARGUMENT": "2026-08-15",
    "CC-02-OBSERVED-POSITIVITY-OPEN": "2026-08-15",
    "CC-03-FOUR-CORNER-NONCHIRAL": "2026-08-15",
    "CC-04-NORMAL-BUNDLE-RIGHT-CHAIN": "2026-08-15",
    "CC-05-SUBTRACTIVE-TWO-PLUS-ONE": "2026-08-14",
    "CC-06-CHIRALITY-VEV-CONDITIONAL": "2026-08-16",
    "CC-07-CONTRACTION-NOT-KK": "2026-08-14",
    "CC-08-DARK-PARTNER-OBLIGATION": "2026-08-15",
    "CC-09-YUKAWA-REPULSIVE-SIGN": "2026-08-15",
    "CC-10-UCSD-EDITED-DERIVATIVE": "2026-08-15",
}
PINNED_DIRTY = {
    "CC-01-MET-X-ARGUMENT": 22, "CC-02-OBSERVED-POSITIVITY-OPEN": 11,
    "CC-03-FOUR-CORNER-NONCHIRAL": 2, "CC-04-NORMAL-BUNDLE-RIGHT-CHAIN": 2,
    "CC-05-SUBTRACTIVE-TWO-PLUS-ONE": 39, "CC-06-CHIRALITY-VEV-CONDITIONAL": 26,
    "CC-07-CONTRACTION-NOT-KK": 5, "CC-08-DARK-PARTNER-OBLIGATION": 4,
    "CC-09-YUKAWA-REPULSIVE-SIGN": 28, "CC-10-UCSD-EDITED-DERIVATIVE": 44,
}
PINNED_TOTAL_DIRTY = 183
PINNED_TOTAL_CLEARED = 18
PINNED_RECORDS = 40
PINNED_ALL_REGISTER = 23
PINNED_STALE_FOUND = 6
PINNED_FIXA = 6
PINNED_RW1 = 5
SEED_AUTHORS = frozenset({"SCUR-1", "FIX-A", "RW-1"})

# The ten citation-edge corrections present when CT-5 shipped.  They stay
# independently pinned as an ordered, unique historical subsequence; the
# separately governed citation class may add later corrections without making
# this canonical-currency certificate stale.  The no-leak check below still
# forbids every CT-5 canonical-source correction from entering that class.
CITATION_IDS = (
    "V15-1", "V15-2", "CARRIER-20260810", "W2-01", "SD-01", "RFAIL-03",
    "DARK-ENERGY-06", "HQ-PHASE-20260812", "HQ-CONTACT-20260812",
    "I2B-PRINCIPAL-GAUGE-20260813",
)

Z3_PACKET = "explorations/z3-receptacle-design-packet-2026-08-11.md"
Z3_CORRECTION = "CC-05-SUBTRACTIVE-TWO-PLUS-ONE"
POST_CORRECTION_FILE = (
    "lab/active-research/joe-directed/z3-receptacle/"
    "z3r1-nu-trivial-w-untwisted-2026-08-17.md")
FENCED_FILE = (
    "lab/active-research/joe-directed/coupling-unification/"
    "cu1-left-right-degeneracy-forbids-unification-2026-08-14.md")
FENCED_CORRECTION = "CC-09-YUKAWA-REPULSIVE-SIGN"
CBE_CONTROL = "explorations/conditional-build/cb-e-source-contact-rows-2026-08-05.md"
CBA = "explorations/conditional-build/cb-a-representation-content-2026-08-05.md"
CBB = "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md"
AGED_AS_OF = "2026-08-25"      # >= 7 days past every canonical_since

CHECKS: list[tuple[str, str, bool, str]] = []


def check(tag: str, label: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((tag, label, bool(ok), str(detail)))
    return bool(ok)


# --------------------------------------------------------------------------
# planted cases
# --------------------------------------------------------------------------

def _plant_z3_cleared() -> dict:
    """SYNTHETIC.  No such record exists in the live sidecar and CT-5 did not
    write one: LD-A/Arc-3 adjudicated SG4 bit 2, not this packet's currency,
    and CT-5 is not licensed to adjudicate it.  The record is planted HERE so
    the CLEARED half of the both-states proof is exercised without asserting an
    adjudication that has not happened."""
    return {
        "file": Z3_PACKET, "correction_id": Z3_CORRECTION,
        "verdict": "CLEARED-CONSISTENT", "date": "2026-08-17",
        "by": "LD-A/Arc-3 (SELFTEST PLANT -- not a live record)",
        "note": "planted second state for the both-states proof",
    }


def _plant_z3_stale() -> dict:
    return {
        "file": Z3_PACKET, "correction_id": Z3_CORRECTION,
        "verdict": "STALE-FOUND", "date": "2026-08-17",
        "by": "SELFTEST PLANT",
        "pointer": "planted third state: found stale, not yet repaired",
    }


def _plant_owner_case() -> dict:
    """A synthetic correction whose OWNER predates it and matches its own
    signature, so the owner-exemption path has a live failure mode."""
    return {
        "id": "CC-SELFTEST-OWNER", "entry_class": "canonical_source_correction",
        "canonical_since": "2026-08-17", "owner": Z3_PACKET,
        "superseded_reading": "planted: exercises the owner exemption",
        "signature": {
            "match": "all_families",
            "token_families": [["the dim-13 z/3 count receptacle"], ["design packet"]],
            "blindness": "planted",
            "known_synonyms_outside_signature": ["planted"],
        },
    }


def _plant_power_case() -> dict:
    """Planted-positive detector-power control (VERIFICATION.md rule 4): a
    correction the detector is REQUIRED to fire on.  Corrupting the matcher
    cannot flip an absence result, so power must be shown on a positive."""
    return {
        "id": "CC-SELFTEST-POWER", "entry_class": "canonical_source_correction",
        "canonical_since": "2026-08-17", "owner": "VERIFICATION.md",
        "superseded_reading": "planted: the detector must find this file",
        "signature": {
            "match": "all_families",
            "token_families": [["the dim-13 z/3 count receptacle"], ["design packet"]],
            "blindness": "planted",
            "known_synonyms_outside_signature": ["planted"],
        },
    }


def _fixa_pairs() -> tuple:
    return ((CBA, "CC-06-CHIRALITY-VEV-CONDITIONAL"), (CBA, "CC-07-CONTRACTION-NOT-KK"),
            (CBA, "CC-05-SUBTRACTIVE-TWO-PLUS-ONE"), (CBB, "CC-07-CONTRACTION-NOT-KK"),
            (CBB, "CC-06-CHIRALITY-VEV-CONDITIONAL"), (CBB, "CC-08-DARK-PARTNER-OBLIGATION"))


def _fixa_drops() -> tuple:
    """Drop keys that remove FIX-A's REPAIR while leaving SCUR-1's FINDING in
    place -- otherwise the pair would fall back to the ALL-REGISTER clearance
    and the control would be testing the wrong thing."""
    return tuple((f, c, "FIX-A") for f, c in _fixa_pairs())


def _rw1_pairs() -> tuple:
    s11 = "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
    decoupling = "explorations/decoupling-constructibility-packet-2026-08-12.md"
    source_pack = "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    return (
        (s11, "CC-06-CHIRALITY-VEV-CONDITIONAL"),
        (s11, "CC-08-DARK-PARTNER-OBLIGATION"),
        (decoupling, "CC-05-SUBTRACTIVE-TWO-PLUS-ONE"),
        (decoupling, "CC-08-DARK-PARTNER-OBLIGATION"),
        (source_pack, "CC-10-UCSD-EDITED-DERIVATIVE"),
    )


# --------------------------------------------------------------------------

def run_probe(cfg: dict | None = None) -> dict:
    CHECKS.clear()
    cfg = copy.deepcopy(cfg if cfg is not None else G.default_cfg())
    cfg["as_of"] = cfg.get("as_of") or "2026-08-17"

    res = G.compute(cfg)
    per = res["per"]

    # ---------------------------------------------------------------- R ---
    entries = res["entries"]
    live = [e for e in entries if str(e.get("id")).startswith("CC-") and "SELFTEST" not in str(e.get("id"))]
    historical_ids = tuple(str(e["id"]) for e in live if str(e.get("id")) in set(CANON_IDS))
    check("R", "registry retains CT-5's original ten as an ordered unique historical subsequence",
          historical_ids == CANON_IDS
          and all(sum(1 for e in live if str(e.get("id")) == cid) == 1 for cid in CANON_IDS),
          historical_ids)
    historical = [e for e in live if str(e.get("id")) in set(CANON_IDS)]
    check("R", "the historical canonical ids are exactly SCUR-1's ten register items",
          tuple(sorted(str(e["id"]) for e in historical)) == tuple(sorted(CANON_IDS)),
          sorted(str(e.get("id")) for e in historical))
    check("R", "every canonical entry declares entry_class canonical_source_correction",
          all(e.get("entry_class") == "canonical_source_correction" for e in live))
    check("R", "canonical_since dates match SCUR-1's owner artifacts",
          {str(e["id"]): str(e["canonical_since"]) for e in historical} == CANON_SINCE,
          {str(e["id"]): str(e["canonical_since"]) for e in historical})
    check("R", "every signature has >= 1 family and every family >= 1 nonempty token",
          all(G.families_of(e) and all(any(str(t).strip() for t in f) for f in G.families_of(e))
              for e in live))
    check("R", "every entry states its one-token-blindness caveat",
          all(str((e.get("signature") or {}).get("blindness") or "").strip() for e in live))
    check("R", "every entry cites known synonym families left outside the signature",
          all(list((e.get("signature") or {}).get("known_synonyms_outside_signature") or [])
              for e in live))
    check("R", "every owner and co-owner path exists on disk",
          all((ROOT / str(p)).exists()
              for e in live for p in [e.get("owner")] + list(e.get("co_owners") or ())))

    # ---------------------------------------------------------------- C ---
    raw = yaml.safe_load((ROOT / "lab" / "process" / "correction-registry.yaml")
                         .read_text(encoding="utf-8"))
    check("C", "registry has exactly two top-level keys: the citation class and the new one",
          sorted(raw.keys()) == ["canonical_source_corrections", "corrections"],
          sorted(raw.keys()))
    citation_ids = tuple(str(e.get("id")) for e in raw["corrections"])
    historical = tuple(cid for cid in citation_ids if cid in set(CITATION_IDS))
    check("C", "the citation gate retains CT-5's historical ten in order and uniquely",
          historical == CITATION_IDS
          and all(citation_ids.count(cid) == 1 for cid in CITATION_IDS),
          citation_ids)
    check("C", "no canonical entry leaked into the citation gate's list",
          not ({str(e.get("id")) for e in live}
               & {str(e.get("id")) for e in raw["corrections"]}))
    check("C", "the citation gate still passes on the extended registry",
          _citation_gate_passes(), "correction_propagation_audit exit status")

    # ---------------------------------------------------------------- S ---
    checks_ = [c for c in res["checks"] if "SELFTEST" not in str(c.get("by", ""))]
    historical_checks = [c for c in checks_ if c.get("by") in SEED_AUTHORS]
    check("S", "sidecar seed is SCUR-1's 23 documents + 6 findings, 6 FIX-A repairs, and 5 RW-1 clearances",
          len(historical_checks) == PINNED_RECORDS, len(historical_checks))
    check("S", "23 ALL-REGISTER records (SCUR-1's per-document verdicts)",
          sum(1 for c in historical_checks if c.get("correction_id") == "ALL-REGISTER") == PINNED_ALL_REGISTER,
          sum(1 for c in historical_checks if c.get("correction_id") == "ALL-REGISTER"))
    stale = [c for c in historical_checks if c.get("verdict") == "STALE-FOUND"]
    check("S", "6 STALE-FOUND records = SCUR-1's five findings over six pairs",
          len(stale) == PINNED_STALE_FOUND, len(stale))
    check("S", "every STALE-FOUND record carries a pointer to where the finding lives",
          all(str(c.get("pointer") or "").strip() for c in stale))
    check("S", "every STALE-FOUND record is attributed to SCUR-1",
          all(c.get("by") == "SCUR-1" for c in stale))
    fixa = [c for c in checks_ if c.get("by") == "FIX-A"]
    check("S", "6 FIX-A repair records over the same six pairs",
          len(fixa) == PINNED_FIXA and
          tuple(sorted((str(c["file"]), str(c["correction_id"])) for c in fixa))
          == tuple(sorted(_fixa_pairs())), len(fixa))
    rw1 = [c for c in checks_ if c.get("by") == "RW-1"]
    check("S", "5 RW-1 clearances are pinned to the exact artifact-owned pairs",
          len(rw1) == PINNED_RW1 and
          tuple(sorted((str(c["file"]), str(c["correction_id"])) for c in rw1))
          == tuple(sorted(_rw1_pairs())), len(rw1))
    check("S", "every RW-1 record is an exact CLEARED-CONSISTENT verdict",
          all(c.get("verdict") == "CLEARED-CONSISTENT"
              and c.get("correction_id") != "ALL-REGISTER" for c in rw1))
    check("S", "every recorded verdict is inside the closed vocabulary",
          all(c.get("verdict") in G.VERDICTS for c in checks_))
    check("S", "every recorded check names a file that exists",
          all((ROOT / str(c.get("file"))).exists() for c in checks_))
    check("S", "SUPERSEDED-DOC is deliberately unused in the live seed (no invented record)",
          not any(c.get("verdict") == "SUPERSEDED-DOC" for c in checks_))

    # ---------------------------------------------------------------- W ---
    wf = G.wellformedness(res, cfg)
    check("W", "live registry + sidecar are well-formed (zero RED conditions)",
          wf == [], wf[:3])
    rt = G.ratchet_failures(res)
    check("W", "live ratchet is intact", rt == [], rt[:3])

    # Reconstruct CT-5's historical view from its exact seed provenance.  The
    # live sidecar is intentionally append-only, so deriving these pins from
    # every current record would make legitimate later adjudication look like
    # corruption of the historical certificate.
    extension_drops = tuple(
        (str(c.get("file")), str(c.get("correction_id")), str(c.get("by")))
        for c in checks_
        if c.get("by") not in SEED_AUTHORS
        and (c.get("correction_id") == "ALL-REGISTER"
             or c.get("correction_id") in set(CANON_IDS))
    )
    historical_cfg = copy.deepcopy(cfg)
    historical_cfg["drop_check_ids"] = tuple(
        historical_cfg.get("drop_check_ids") or ()) + extension_drops
    historical_res = G.compute(historical_cfg)
    historical_per = historical_res["per"]

    # ---------------------------------------------------------------- D ---
    for cid in CANON_IDS:
        p = historical_per.get(cid)
        check("D", f"dirty count pinned for {cid}",
              p is not None and p["dirty"] == PINNED_DIRTY[cid],
              None if p is None else p["dirty"])
    total = sum(historical_per[c]["dirty"] for c in CANON_IDS if c in historical_per)
    check("D", "total dirty (file, correction) pairs",
          total == PINNED_TOTAL_DIRTY, total)
    cleared_total = sum(
        len(historical_per[c]["cleared"]) + len(historical_per[c]["fenced"])
        + len(historical_per[c]["repaired"])
        for c in CANON_IDS if c in historical_per)
    check("D", "total pairs cleared by the seeded records",
          cleared_total == PINNED_TOTAL_CLEARED, cleared_total)
    missed = [(cid, rel) for cid in CANON_IDS if cid in historical_per
              for rel, _v in historical_per[cid]["signature_missed"]]
    check("D", "measured signature blindness is exactly one pair, and it is CB-B under CC-08",
          missed == [("CC-08-DARK-PARTNER-OBLIGATION", CBB)], missed)
    check("D", "every correction's topic_reach is >= its dirty count (conjunction only narrows)",
          all(historical_per[c]["topic_reach"] >= historical_per[c]["dirty"]
              for c in CANON_IDS if c in historical_per))
    leaked = sorted({d["rel"].split("/", 1)[0] for d in historical_res["corpus"]}
                    & {"absorbed", "papers", "_local", ".git"})
    check("D", "audited scope excludes absorbed/, papers/, _local/ -- nothing leaks in",
          leaked == [], leaked)
    surfaces_seen = sorted({d["rel"].split("/", 1)[0] if "/" in d["rel"] else "<root>"
                            for d in historical_res["corpus"]})
    check("D", "audited scope is exactly the five live surfaces plus root markdown",
          surfaces_seen == ["<root>", "canon", "docs", "explorations", "lab", "packets"],
          surfaces_seen)

    # ------------------------------------------------- Z: both-states proof ---
    corpus = {d["rel"]: d for d in res["corpus"]}
    pkt = corpus.get(Z3_PACKET)
    check("Z", "the Z/3 packet is in the audited corpus", pkt is not None)
    check("Z", "the Z/3 packet's dated frontmatter is 2026-08-11",
          pkt is not None and pkt["date"] == "2026-08-11", None if pkt is None else pkt["date"])
    e05 = next((e for e in entries if str(e.get("id")) == Z3_CORRECTION), None)
    check("Z", "the Z/3 packet matches the 2+1 signature",
          e05 is not None and pkt is not None and G.signature_match(e05, pkt["low"]))
    check("Z", "the Z/3 packet predates CC-05's canonical_since (2026-08-11 < 2026-08-14)",
          pkt is not None and e05 is not None and pkt["date"] is not None
          and pkt["date"] < str(e05["canonical_since"]),
          None if pkt is None else pkt["date"])
    check("Z", "STATE A -- live, no recorded check: the packet is DIRTY-UNCHECKED",
          Z3_CORRECTION in per and Z3_PACKET in per[Z3_CORRECTION]["unchecked"])
    check("Z", "STATE A -- and it is not silently sitting in some cleared bucket",
          Z3_CORRECTION in per and Z3_PACKET not in (
              per[Z3_CORRECTION]["cleared"] + per[Z3_CORRECTION]["fenced"]
              + per[Z3_CORRECTION]["repaired"]))

    cfg_b = copy.deepcopy(cfg)
    cfg_b["injected_checks"] = tuple(cfg_b.get("injected_checks") or ()) + (_plant_z3_cleared(),)
    res_b = G.compute(cfg_b)
    pb = res_b["per"].get(Z3_CORRECTION)
    check("Z", "STATE B -- adjudication recorded: the packet leaves the dirty set",
          pb is not None and Z3_PACKET not in pb["unchecked"] and Z3_PACKET not in pb["known_stale"])
    check("Z", "STATE B -- it lands in the cleared bucket, not merely vanishes",
          pb is not None and Z3_PACKET in pb["cleared"])
    check("Z", "STATE B -- CC-05's dirty count falls by exactly one",
          pb is not None and Z3_CORRECTION in per
          and per[Z3_CORRECTION]["dirty"] - pb["dirty"] == 1,
          None if pb is None else (per[Z3_CORRECTION]["dirty"], pb["dirty"]))

    cfg_c = copy.deepcopy(cfg)
    cfg_c["injected_checks"] = tuple(cfg_c.get("injected_checks") or ()) + (_plant_z3_stale(),)
    pc = G.compute(cfg_c)["per"].get(Z3_CORRECTION)
    check("Z", "STATE C -- a STALE-FOUND record does NOT clear: it becomes DIRTY-KNOWN-STALE",
          pc is not None and Z3_PACKET in pc["known_stale"] and Z3_PACKET not in pc["unchecked"])
    check("Z", "STATE C -- and the dirty count is unchanged (found is not fixed)",
          pc is not None and Z3_CORRECTION in per and pc["dirty"] == per[Z3_CORRECTION]["dirty"],
          None if pc is None else pc["dirty"])

    other = [cid for cid in CANON_IDS if cid != Z3_CORRECTION and cid in per
             and (Z3_PACKET in per[cid]["unchecked"] or Z3_PACKET in per[cid]["known_stale"])]
    check("Z", "specificity -- the packet is dirty for CC-05 and no other correction",
          other == [], other)

    # ------------------------------------------------- K: contrary controls ---
    post = corpus.get(POST_CORRECTION_FILE)
    check("K", "contrary control: the post-correction Z/3 file is dated after CC-05",
          post is not None and e05 is not None and post["date"] is not None
          and post["date"] > str(e05["canonical_since"]),
          None if post is None else post["date"])
    check("K", "contrary control: it matches the same signature (so the test is not vacuous)",
          post is not None and e05 is not None and G.signature_match(e05, post["low"]))
    dirty_post = [cid for cid in CANON_IDS if cid in per
                  and (POST_CORRECTION_FILE in per[cid]["unchecked"]
                       or POST_CORRECTION_FILE in per[cid]["known_stale"])]
    check("K", "contrary control: a post-correction file must NOT be dirty, for any correction",
          dirty_post == [], dirty_post)

    pf = per.get(FENCED_CORRECTION)
    check("K", "contrary control: the fenced comparator resolves FENCED, not stale",
          pf is not None and FENCED_FILE in pf["fenced"])
    check("K", "contrary control: and is therefore absent from the dirty set",
          pf is not None and FENCED_FILE not in pf["unchecked"] + pf["known_stale"])

    dirty_cbe = [cid for cid in CANON_IDS if cid in per
                 and (CBE_CONTROL in per[cid]["unchecked"] or CBE_CONTROL in per[cid]["known_stale"])]
    check("K", "contrary control: SCUR-1's own CB-E control is dirty for nothing",
          dirty_cbe == [], dirty_cbe)

    p06 = per.get("CC-06-CHIRALITY-VEV-CONDITIONAL")
    check("K", "CB-A resolves REPAIRED under CC-06 (FIX-A's clearance beat SCUR-1's finding)",
          p06 is not None and CBA in p06["repaired"])
    cfg_d = copy.deepcopy(cfg)
    cfg_d["drop_check_ids"] = ((CBA, "CC-06-CHIRALITY-VEV-CONDITIONAL", "FIX-A"),)
    pd = G.compute(cfg_d)["per"].get("CC-06-CHIRALITY-VEV-CONDITIONAL")
    check("K", "the repair is load-bearing: drop FIX-A's record and CB-A returns DIRTY-KNOWN-STALE",
          pd is not None and CBA in pd["known_stale"])
    check("K", "and CC-06's dirty count rises by exactly one when the repair is dropped",
          pd is not None and p06 is not None and pd["dirty"] - p06["dirty"] == 1,
          None if pd is None else (p06["dirty"], pd["dirty"]))

    # ------------------------------------------------ P: planted positives ---
    cfg_p = copy.deepcopy(cfg)
    cfg_p["injected_corrections"] = tuple(cfg_p.get("injected_corrections") or ()) + (_plant_power_case(),)
    pp = G.compute(cfg_p)["per"].get("CC-SELFTEST-POWER")
    check("P", "planted-positive control: the detector fires on a correction it must find",
          pp is not None and Z3_PACKET in pp["unchecked"],
          None if pp is None else pp["dirty"])

    cfg_o = copy.deepcopy(cfg)
    cfg_o["injected_corrections"] = tuple(cfg_o.get("injected_corrections") or ()) + (_plant_owner_case(),)
    po = G.compute(cfg_o)["per"].get("CC-SELFTEST-OWNER")
    check("P", "owner exemption: a correction's own owner is never dirty for it",
          po is not None and po["dirty"] == 0, None if po is None else po["dirty"])

    cfg_x = copy.deepcopy(cfg)
    cfg_x["injected_checks"] = tuple(cfg_x.get("injected_checks") or ()) + (
        _plant_z3_stale(),
        {"file": Z3_PACKET, "correction_id": "ALL-REGISTER", "verdict": "CLEARED-CONSISTENT",
         "date": "2026-08-17", "by": "SELFTEST PLANT", "note": "broad clearance"},
    )
    px = G.compute(cfg_x)["per"].get(Z3_CORRECTION)
    check("P", "precedence: an explicit STALE-FOUND beats a broad ALL-REGISTER clearance",
          px is not None and Z3_PACKET in px["known_stale"])

    # ------------------------------------------------------ T: ratchet teeth ---
    cfg_t = copy.deepcopy(cfg)
    cfg_t["as_of"] = AGED_AS_OF
    res_t = G.compute(cfg_t)
    check("T", "at as-of 2026-08-25 every correction is AGED (grace expired)",
          all(res_t["per"][c]["aged"] for c in CANON_IDS if c in res_t["per"]))
    check("T", "aged and unchanged: the ratchet is green",
          G.ratchet_failures(res_t) == [], G.ratchet_failures(res_t)[:2])
    check("T", "at as-of 2026-08-17 no correction is aged yet (ratchet honestly inert)",
          not any(per[c]["aged"] for c in CANON_IDS if c in per))

    cfg_t2 = copy.deepcopy(cfg_t)
    cfg_t2["drop_check_ids"] = _fixa_drops()
    rt2 = G.ratchet_failures(G.compute(cfg_t2))
    check("T", "aged with the six repairs dropped: the ratchet BREAKS (dirty grew past baseline)",
          len(rt2) >= 1 and any("RATCHET BROKEN" in s for s in rt2), rt2[:2])

    cfg_t3 = copy.deepcopy(cfg_t)
    cfg_t3["injected_corrections"] = tuple(cfg_t3.get("injected_corrections") or ()) + (_plant_power_case(),)
    rt3 = G.ratchet_failures(G.compute(cfg_t3))
    check("T", "an aged correction with no recorded baseline is RED, not silently accepted",
          any("CC-SELFTEST-POWER" in s and "NO ratchet baseline" in s for s in rt3), rt3[:2])

    return res


def _citation_gate_passes() -> bool:
    """Run correction_propagation_audit.py in-process against the extended
    registry.  This is the durable form of CT-5's before/after identity claim:
    the citation gate must keep passing as its separately governed correction
    class grows, while CT-5's original ten remain independently pinned."""
    spec = importlib.util.spec_from_file_location(
        "cpa", ROOT / "process_gates" / "correction_propagation_audit.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    buf = io.StringIO()
    with redirect_stdout(buf), redirect_stderr(buf):
        suite = unittest.defaultTestLoader.loadTestsFromModule(mod)
        result = unittest.TextTestRunner(stream=buf, verbosity=0).run(suite)
    return result.wasSuccessful()


# --------------------------------------------------------------------------

def emit(_res: dict | None = None) -> int:
    npass = sum(1 for _t, _l, o, _d in CHECKS if o)
    by: dict[str, list[int]] = {}
    for tag, _l, o, _d in CHECKS:
        e = by.setdefault(tag, [0, 0])
        e[1] += 1
        e[0] += 1 if o else 0
    print()
    for tag, label, ok, detail in CHECKS:
        if not ok:
            print(f"  [FAIL] [{tag}] {label}   got: {detail}")
    print("-" * 78)
    print(f"CERTIFICATE: {npass}/{len(CHECKS)} checks pass; no load-bearing float (none constructed).")
    print("  by class:", {k: f"{v[0]}/{v[1]}" for k, v in sorted(by.items())})
    print("-" * 78)
    return 0 if npass == len(CHECKS) else 1


# =========================================================================
# --selftest: clean baseline FIRST, machinery-corruption mutations only
# =========================================================================

def _m_dates_off(cfg):
    cfg["frontmatter_date_keys"] = ()
    cfg["filename_date_fallback"] = False


def _m_filename_fallback(cfg):
    cfg["filename_date_fallback"] = False


def _m_predate_loose(cfg):
    cfg["strict_predate"] = False


def _m_clearing_loses(cfg):
    cfg["clearing_beats_stale"] = False


def _m_explicit_loses(cfg):
    cfg["explicit_beats_all_register"] = False


def _m_owner_not_exempt(cfg):
    cfg["owner_exempt"] = False


def _m_surfaces(cfg):
    cfg["surfaces"] = ("canon",)


def _m_root_md(cfg):
    # NOTE: mutating skip_dirs was tried and REMOVED as unfalsifiable-by-
    # construction: measured 2026-08-17, every skip_dirs entry excludes zero
    # files (the big archives are top-level siblings `surfaces` already omits),
    # so no corruption of it can be detected.  Corpus scope is instead
    # corrupted here in a way that is live.
    cfg["include_root_md"] = False


def _m_all_register_token(cfg):
    cfg["all_register_token"] = "NOT-A-REAL-TOKEN"


def _m_drop_repairs(cfg):
    cfg["drop_check_ids"] = _fixa_drops()


def _m_empty_family(cfg):
    bad = copy.deepcopy(_plant_power_case())
    bad["id"] = "CC-SELFTEST-MALFORMED"
    bad["signature"]["token_families"] = [[]]
    cfg["injected_corrections"] = tuple(cfg.get("injected_corrections") or ()) + (bad,)


def _m_ghost_file_record(cfg):
    cfg["injected_checks"] = tuple(cfg.get("injected_checks") or ()) + (
        {"file": "explorations/this-file-does-not-exist-ct5.md",
         "correction_id": Z3_CORRECTION, "verdict": "CLEARED-CONSISTENT",
         "date": "2026-08-17", "by": "CORRUPTION"},)


def _m_frontmatter_window(cfg):
    cfg["frontmatter_window"] = 20


MUTATIONS = [
    ("all_date_extraction_disabled", _m_dates_off),
    ("filename_date_fallback_removed", _m_filename_fallback),
    ("predate_test_loosened_to_inclusive", _m_predate_loose),
    ("clearing_no_longer_beats_stale", _m_clearing_loses),
    ("explicit_no_longer_beats_all_register", _m_explicit_loses),
    ("owner_exemption_removed", _m_owner_not_exempt),
    ("surfaces_narrowed_to_canon", _m_surfaces),
    ("root_markdown_dropped_from_scope", _m_root_md),
    ("all_register_token_renamed", _m_all_register_token),
    ("fixa_repair_records_dropped", _m_drop_repairs),
    ("registry_entry_with_empty_token_family", _m_empty_family),
    ("sidecar_record_pointing_at_a_ghost_file", _m_ghost_file_record),
    ("frontmatter_window_truncated", _m_frontmatter_window),
]


def selftest() -> int:
    print("=" * 78)
    print("CT-5 SELFTEST -- clean baseline verified FIRST, then mutations")
    print("=" * 78)
    try:
        run_probe(G.default_cfg())
    except Exception as exc:                                     # noqa: BLE001
        print(f"  BASELINE CRASHED: {type(exc).__name__}: {exc}")
        print("  ABORT RED (VERIFICATION.md rule 1).")
        return 1
    base_fail = [c for c in CHECKS if not c[2]]
    if base_fail:
        print(f"  CLEAN BASELINE IS RED ({len(base_fail)} failures) -- ABORT RED.")
        for tag, label, _o, detail in base_fail:
            print(f"    [FAIL] [{tag}] {label}  got: {detail}")
        return 1
    print(f"  clean baseline: {len(CHECKS)}/{len(CHECKS)} checks pass  [OK]")
    print()

    bad = []
    for name, mutate in MUTATIONS:
        cfg = G.default_cfg()
        mutate(cfg)
        try:
            run_probe(cfg)
            fails = [c for c in CHECKS if not c[2]]
            if fails:
                verdict, note = "CAUGHT", f"{len(fails)} [FAIL]: {fails[0][1][:56]}"
            else:
                verdict, note = "MISSED", "no [FAIL] line -- mutation is invisible"
        except Exception as exc:                                 # noqa: BLE001
            verdict, note = "CRASH-NOT-DETECTION", f"{type(exc).__name__}: {exc}"
        if verdict != "CAUGHT":
            bad.append((name, verdict, note))
        print(f"  mutation {name:<42s} {verdict:<20s} {note}")

    print()
    for name, verdict, note in bad:
        print(f"  [FAIL] mutation {name}: {verdict} -- {note}")
    print("-" * 78)
    print(f"SELFTEST: {len(MUTATIONS) - len(bad)}/{len(MUTATIONS)} mutations produced "
          "a GENUINE failing check; crash-catches are rejected.")
    print("-" * 78)
    return 1 if bad else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(selftest())
    sys.exit(emit(run_probe()))
