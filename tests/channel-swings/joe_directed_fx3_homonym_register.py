#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FX-3: the homonym register and its gate — prior art, seeding, receipts,
sensing floor, contrary control.

THE TARGET.  Homonyms are the second-largest measured error class in this
repository.  Before FX-3, tracking lived on five disconnected surfaces
(NAMES.md, cb-b's quarantine, the packet's Layer-0 register, per-wave layer0
JSON blocks, the claim register's [ASR] glosses) and none was machine-audited.
FX-3 CONSOLIDATES them into lab/process/homonym-register.yaml, gated by
process_gates/homonym_register_audit.py.  This certificate proves:

  LEG 1  PRIOR ART — every pre-existing surface exists with its exact row
         counts; the consolidation absorbed, it did not invent.
  LEG 2  the register parses, the gate passes on it, and the seeded shape is
         exactly as published (37 entries, 30/1/1/5 by kind, 37/37 receipts,
         4 sensing blocks, 3 documented sensing refusals, 1 contrary control).
  LEG 3  INCIDENT RE-VERIFICATION — each new entry's incident is re-checked
         against the PRIMARY artifact, not against the register's citation of
         it.  Includes the exact heading census that corrects the tasking's
         own undercount (FOUR files carry the claim-status Classification
         heading, not two).
  LEG 4  TRANSCRIPT VARIANTS — exact word-boundary counts in the ASR
         transcripts, with the professionally edited 2020 Portal transcript
         as the engine control (zero variants, canonical spellings only).
  LEG 5  CONTRARY CONTROL — "gimmel" looks like the strongest homonym
         candidate in the repo by breadth and provably is not: zero collision
         evidence across every quarantine surface.  The register demonstrably
         discriminates on receipts, not frequency.

Exit 0 == every check passed.  ``--selftest`` FIRST verifies the clean
baseline exits 0 — a red baseline makes every mutation meaningless, so it
aborts with exit 1 — then plants false machinery into a copy of THIS probe,
requiring each mutant to drive exit 1, and finally requires the gate's own
``--selftest`` (12 planted register corruptions) to exit 0.

target_claim: NONE-NOT-A-KILL.  This certificate adjudicates no physics claim.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

REGISTER = "lab/process/homonym-register.yaml"
GATE = "process_gates/homonym_register_audit.py"
NAMES = "lab/process/NAMES.md"
CBB = "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md"
PACKET = "explorations/unified-source-datum-packet-v0-2026-07-30.md"
WAVE3B = "lab/process/eric-curt-wave3b-cech-domain-quotient.json"
WAVE3C = "lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json"
CLAIM_REG = "lab/sources/source-claim-register.yaml"
TWO_GEOM = "explorations/firewall-and-two-geometries/two-geometries-and-the-adapter-2026-06-29.md"

STEWARD = "lab/active-research/joe-directed/steward-2026-08-14-research-maintenance-pass.md"
MC1 = "lab/active-research/joe-directed/metric-cone-boundedness/mc1-the-cone-does-not-bound-and-the-negative-direction-is-the-cone-itself-2026-08-14.md"
CC1 = "lab/active-research/joe-directed/cosmological-constant-sign/cc1-killing-signature-cannot-sign-lambda-2026-08-14.md"
AC1 = "lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md"
BD1 = "lab/active-research/joe-directed/baryon-number-and-proton-decay/bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md"
SG1 = "lab/active-research/joe-directed/sg4-axis/sg1-c6a-scope-narrowing-2026-08-16.md"
SA1 = "lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md"
SCA = "lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md"
CH3 = "lab/active-research/joe-directed/chain-repair/ch3-the-nested-chain-is-repaired-at-three-sites-and-the-rank-drop-moves-to-arrow-one-2026-08-15.md"
ITC = "lab/active-research/joe-directed/indefiniteness-typing/itc-positivity-rows-are-five-not-ten-2026-08-15.md"
BDREG = "lab/active-research/joe-directed/base-duality/bd-reg-routing-backlog-disposition-2026-08-15.md"
BD_README = "lab/active-research/joe-directed/base-duality/README.md"
ROUTING_AUDIT = "process_gates/source_native_comparator_routing_audit.py"
LEG_A = "tests/gu-forces/leg_a_forcing_enumeration.py"

GU40 = "lab/sources/transcripts/toe-weinstein-gu-40-years.md"
ITI = "papers/drafts/Transcript into the impossible.md"
PORTAL = "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
MANNHEIM = "lab/sources/transcripts/toe-mannheim-conformal-gravity-2026-07-06.md"

JD = "lab/active-research/joe-directed"

CHECKS: list[tuple[bool, str]] = []


def check(label: str, cond: bool) -> bool:
    CHECKS.append((bool(cond), label))
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
    return bool(cond)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def wcount(rel: str, pattern: str, flags: int = re.IGNORECASE) -> int:
    """Word-boundary count.  Substring counting is a planted pitfall of this
    exact channel: case-insensitive substring 'vial' counts 9 in the gu-40
    transcript because of 'trivial(ly)'; the word-boundary count is 1."""
    return len(re.findall(pattern, read(rel), flags))


def names_first_cells() -> list[str]:
    cells, in_table = [], False
    for line in read(NAMES).splitlines():
        if re.match(r"^\|\s*-+", line):
            in_table = True
            continue
        if in_table and line.startswith("|"):
            parts = line.split("|")
            if len(parts) > 2:
                cells.append(parts[1].strip())
    return cells


# --------------------------------------------------------------------------
# LEG 1 — prior art: the five surfaces, exact row counts, retrieval receipts.
# --------------------------------------------------------------------------

def leg1_prior_art() -> None:
    print("\n" + "=" * 74)
    print("LEG 1 — prior art: five pre-existing homonym surfaces, exact counts")
    print("=" * 74)

    names = read(NAMES)
    check("NAMES.md declares itself 'the homonym disambiguation table'",
          "the homonym disambiguation table" in names)
    cells = names_first_cells()
    check(f"NAMES.md has exactly 9 data rows (found {len(cells)})", len(cells) == 9)

    cbb = read(CBB).splitlines()
    quarantine = [ln for ln in cbb[183:189] if "HOMONYM" in ln]
    check("cb-b Layer-0 quarantine: exactly 6 HOMONYM rows at lines 184-189",
          len(quarantine) == 6)
    check("cb-b quarantine covers theta/torsion/Einstein contraction/Z_U/Higgs/square",
          all(t in "".join(cbb[183:189]) for t in
              ('"theta"', '"torsion"', '"Einstein contraction"', "`Z_U`",
               '"the Higgs"', '"square"')))

    packet = read(PACKET).splitlines()
    check("packet section 1.2 'Layer-0 register' heading at line 122",
          packet[121].strip() == "### 1.2 Layer-0 register")
    rows = [ln for ln in packet[125:135] if ln.startswith("| ")]
    check(f"packet register: exactly 10 rows at lines 126-135 (found {len(rows)})",
          len(rows) == 10)
    check("packet register row 'stationary' at line 133 (LA-10's cited line)",
          packet[132].startswith("| stationary |"))
    check("LA-10 cites the packet as 'the ledger's own' homonym register",
          "homonym register in `unified-source-datum-packet-v0-2026-07-30.md:133`"
          in read("lab/active-research/joe-directed/ledger-advancement/"
                  "la10-the-cut-vertex-survives-and-is-not-the-second-action-2026-08-15.md"))

    w3b = read(WAVE3B)
    w3c = read(WAVE3C)
    check("wave3b layer0 block: exactly 4 HOMONYM dispositions",
          w3b.count('"disposition": "HOMONYM"') == 4)
    check("wave3c layer0 block: exactly 4 HOMONYM dispositions (incl. 'null cone')",
          w3c.count('"disposition": "HOMONYM"') == 4 and '"term": "null cone"' in w3c)

    asr = read(CLAIM_REG).count("[ASR]")
    check(f"claim register [ASR] gloss convention: >= 10 glosses (found {asr})", asr >= 10)
    check("earliest precedent (two-geometries torsion pun) exists and types the equivocation",
          "False-by-equivocation" in read(TWO_GEOM))
    check("IT-C already pointed at cb-b's quarantine as the join target",
          "already runs a homonym quarantine" in norm(read(ITC)))


# --------------------------------------------------------------------------
# LEG 2 — the register parses, the gate passes, the seeded shape is exact.
# --------------------------------------------------------------------------

def leg2_register_and_gate() -> None:
    print("\n" + "=" * 74)
    print("LEG 2 — the register, its gate, and the exact seeded shape")
    print("=" * 74)

    import yaml
    reg = yaml.safe_load(read(REGISTER))
    entries = reg["entries"]
    controls = reg["contrary_controls"]

    check(f"register has exactly 37 entries (found {len(entries)})", len(entries) == 37)
    kinds = {}
    for e in entries:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    check(f"kinds: 30 homonym / 1 near_collision / 1 prefix_collision / "
          f"5 transcription_variant (found {kinds})",
          kinds == {"homonym": 30, "near_collision": 1,
                    "prefix_collision": 1, "transcription_variant": 5})
    check("receipts: 37/37 entries carry incident + paid_by",
          sum(1 for e in entries
              if e.get("receipt", {}).get("incident")
              and e.get("receipt", {}).get("paid_by")) == 37)
    check("every disambiguator is attested (0 coined names)",
          sum(1 for e in entries
              if e.get("disambiguator", {}).get("attested_at")) == 37)
    check("sensing blocks: exactly 4 (cone, Classification:, CHIRAL, the impossible chain)",
          sum(1 for e in entries if e.get("sensing")) == 4)
    check("sensing refusals documented: exactly 3 (positive, so(1,3), BD-)",
          sum(1 for e in entries if e.get("sensing_refused")) == 3)
    check("all sensing is warn_only",
          all(e["sensing"].get("mode") == "warn_only"
              for e in entries if e.get("sensing")))
    check("contrary control: exactly 1, kind not_a_homonym, token gimmel",
          len(controls) == 1 and controls[0]["kind"] == "not_a_homonym"
          and controls[0]["token"] == "gimmel")
    carried = {e.get("names_md_row") for e in entries if e.get("names_md_row")}
    check("all 9 NAMES.md rows carried row-for-row (anti-rival coupling)",
          set(names_first_cells()) <= carried and len(carried) == 9)

    gate = subprocess.run([sys.executable, str(ROOT / GATE)],
                          capture_output=True, text=True, cwd=str(ROOT))
    check(f"gate passes on the live register (exit {gate.returncode})",
          gate.returncode == 0)
    check("gate printed the warn-only sensing floor",
          "sensing floor" in gate.stdout + gate.stderr)


# --------------------------------------------------------------------------
# LEG 3 — incidents re-verified against PRIMARY artifacts, not the register.
# --------------------------------------------------------------------------

def leg3_incidents() -> None:
    print("\n" + "=" * 74)
    print("LEG 3 — incident receipts re-verified at their primary loci")
    print("=" * 74)

    steward = read(STEWARD).splitlines()
    check("steward pass line 56 flags the three-cone homonym at severity 'low — homonym'",
          'Three distinct objects are now called a "cone"' in steward[55]
          and "low — homonym" in steward[55])
    check("MC-1 files the three-cone warning and prescribes Met_Lor-cone typing",
          "should be typed `Met_Lor`-cone wherever it appears" in read(MC1))

    # CLOSED CORPUS: only files dated on/before the 2026-08-16 seeding, so
    # this exact count can never rot as the tree grows.  Live drift is the
    # register gate's warn-only sensor, not this certificate's business.
    heading = "Classification, in target-native vocabulary"
    corpus = [p for p in (ROOT / JD).rglob("*.md")
              if re.search(r"-2026-08-1[0-6]\.md$", p.name)]
    carriers = sorted(
        p.name for p in corpus
        if any(ln.lstrip().startswith("#") and heading in ln
               for ln in p.read_text(encoding="utf-8").splitlines()))
    check(f"claim-status Classification heading census (corpus dated <= 2026-08-16): "
          f"exactly 4 files, CORRECTING the tasking's count of 2 (found {carriers})",
          carriers == [pathlib.Path(AC1).name, pathlib.Path(BD1).name,
                       pathlib.Path(CC1).name, pathlib.Path(MC1).name])
    check("CC-1's section is claim-status vocabulary (ROUTE KILLED), not routing",
          "ROUTE KILLED" in read(CC1))
    check("the backlog disposition names the homonym and left CC-1/MC-1 undecidable",
          "no authorial tiebreak" in read(BDREG)
          and "they classify *claim status*" in read(BDREG))
    check("the routing audit's own comment block records 'a homonym, not a routing type'",
          "a homonym, not a" in read(ROUTING_AUDIT))

    leg_a = read(LEG_A).splitlines()
    check("leg_a line 57 defines PHASE = {MASSIVE, CHIRAL} glossed massless/unbroken",
          'PHASE       = {"MASSIVE", "CHIRAL"}' in leg_a[56]
          and "unbroken chiral (decreased-VEV) point" in leg_a[56])
    check("SG-1 names the propagation mechanism: a Layer-0 HOMONYM on the value CHIRAL",
          "a value literally spelled CHIRAL meaning massless/unbroken" in read(SG1))

    sa1 = read(SA1)
    check("SA-1: two so(1,3) subalgebras, dims 6+6 spanning 12, intersect in zero",
          "dim so(1,3)_endo = 6" in sa1 and "=> they INTERSECT IN ZERO" in sa1)
    check("SA-1 disambiguators so(1,3)_endo / so(1,3)_H are SA-1's own coinage",
          "so(1,3)_endo is the GRAPH of delta over so(1,3)_H" in sa1)

    check("SC-A kills the nested chain on 12 > 10",
          "KILLED by exact group theory (12 > 10" in read(SCA))
    check("CH-3: the two notations differ by one token",
          "they differ by one token: `O(6,4)/U(3,2)`" in read(CH3))
    check("five-week window: H19 dated 2026-07-11, SC-A dated 2026-08-15",
          "H19-seven-seven-signature-branch-2026-07-11" in read(SCA)
          and "2026-08-15" in SCA)

    check("BD README posts the prefix-collision warning and the namespace rule",
          "`BD-A/B/C/D` here are NOT `BD-1/BD-2`." in read(BD_README)
          and "Cite by namespace, not by prefix." in read(BD_README))

    itc = norm(read(ITC))
    check("IT-C exhibits four senses of positive/positivity and proposes D5",
          "distinct senses of `positive`/`positivity` in evidence" in itc
          and "Proposed as `D5`" in itc)


# --------------------------------------------------------------------------
# LEG 4 — transcript variants: exact word-boundary counts, engine control.
# --------------------------------------------------------------------------

def leg4_variants() -> None:
    print("\n" + "=" * 74)
    print("LEG 4 — ASR transcript variants, word-boundary exact; Portal = control")
    print("=" * 74)

    check("gu-40: 'vial' word count exactly 1 (substring count is 9 — 'trivial' pollution)",
          wcount(GU40, r"\bvial\b") == 1
          and len(re.findall("vial", read(GU40), re.I)) == 9)
    check("gu-40: spinner(s) 15, spinor(s) 12 — variant and canonical coexist",
          wcount(GU40, r"\bspinners?\b") == 15 and wcount(GU40, r"\bspinors?\b") == 12)
    check("gu-40:716 carries 'vial spinors' verbatim",
          "vial spinors" in read(GU40).splitlines()[715])

    check("ITI: vial 1, spinner(s) 32, Ruidu 1, 'Petit Salaam' 3, 'Salam Strathy' 1",
          wcount(ITI, r"\bvial\b") == 1
          and wcount(ITI, r"\bspinners?\b") == 32
          and wcount(ITI, r"\bRuidu\b", 0) == 1
          and wcount(ITI, r"\bPetit Salaam\b", 0) == 3
          and wcount(ITI, r"\bSalam Strathy\b", 0) == 1)
    iti = read(ITI).splitlines()
    check("ITI:107 = the chirality assignment, spelled 'positive spinners'",
          "positive spinners" in iti[106])
    check("ITI:128 states the Rarita-Schwinger product property as 'Ruidu Schwinger'",
          "Ruidu Schwinger three halves representation" in iti[127])
    check("ITI:161 states the headline claim as 'general relativity knows Petit Salaam'",
          "general relativity knows Petit Salaam" in iti[160])
    check("ITI:158 'We fed Salam Strathy' (Salam-Strathdee, reconstructed; audio unchecked)",
          "We fed Salam Strathy" in iti[157])

    check("ENGINE CONTROL — Portal (edited, 2020): vial 0, spinner 0, spinor(s) 37, "
          "Rarita-Schwinger x5 — canonical spellings only",
          wcount(PORTAL, r"\bvial\b") == 0
          and wcount(PORTAL, r"\bspinners?\b") == 0
          and wcount(PORTAL, r"\bspinors?\b") == 37
          and wcount(PORTAL, r"\bRarita-Schwinger\b", 0) == 5)
    check("comparator-side twin: Mannheim ASR transcript has vial 6 / vile 3 for Weyl",
          wcount(MANNHEIM, r"\bvial\b") == 6 and wcount(MANNHEIM, r"\bvile\b") == 3)
    check("the claim register already glosses both variants ([ASR] rows)",
          "pull back ''vial spinners''" in norm(read(CLAIM_REG))
          and "[ASR] 'petit salam' = Pati-Salam" in read(CLAIM_REG))
    check("SG-1's probe had to carry the variant tokens to read the primary",
          '"positive spinner", "negative spinner"'
          in read("tests/channel-swings/joe_directed_sg1_c6a_scope_narrowing.py"))


# --------------------------------------------------------------------------
# LEG 5 — contrary control: gimmel is NOT a homonym; discrimination shown.
# --------------------------------------------------------------------------

def leg5_contrary_control() -> None:
    print("\n" + "=" * 74)
    print("LEG 5 — contrary control: gimmel (broadest candidate, zero collisions)")
    print("=" * 74)

    total = 0
    metric = 0
    for fp in ROOT.rglob("*"):
        rel = str(fp)
        if "/_local/" in rel or "/.git/" in rel or not fp.is_file():
            continue
        if fp.suffix not in (".md", ".py", ".yaml", ".json", ".txt"):
            continue
        try:
            text = fp.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        total += len(re.findall(r"\bgimmel\b", text, re.I))
        metric += len(re.findall(r"\bgimmel metric\b", text, re.I))
    check(f"breadth: gimmel appears >= 3000 times repo-wide (found {total}) — "
          "broader than every registered homonym", total >= 3000)
    check(f"dominant head 'gimmel metric' >= 300 (found {metric}) — one referent",
          metric >= 300)

    cbb_rows = "\n".join(read(CBB).splitlines()[181:189])
    packet_rows = "\n".join(read(PACKET).splitlines()[123:135])
    check("zero quarantine rows name gimmel across ALL prior surfaces "
          "(NAMES.md, cb-b:182-189, packet:124-135, wave3b/3c layer0 terms)",
          "gimmel" not in " ".join(names_first_cells()).lower()
          and "gimmel" not in cbb_rows.lower()
          and "gimmel" not in packet_rows.lower()
          and not re.search(r'"term": "[^"]*gimmel[^"]*"', read(WAVE3B) + read(WAVE3C),
                            re.I))

    import yaml
    reg = yaml.safe_load(read(REGISTER))
    entry_tokens = {e["token"] for e in reg["entries"]}
    check("the register does NOT register gimmel as a homonym (it is the control)",
          "gimmel" not in entry_tokens
          and reg["contrary_controls"][0]["token"] == "gimmel")
    check("DISCRIMINATION: cone (122 uses, receipts) IN; gimmel "
          f"({total} uses, zero receipts) OUT — registration follows receipts, "
          "not frequency",
          any(e["token"] == "cone" for e in reg["entries"]) and total > 122)


# --------------------------------------------------------------------------
# Planted false facts — each must be observed False on the live repo.
# --------------------------------------------------------------------------

def planted_false_facts() -> None:
    print("\n" + "=" * 74)
    print("PLANTED FALSE FACTS — each observed False")
    print("=" * 74)

    cbb_quarantine = "\n".join(read(CBB).splitlines()[181:189])
    heading = "Classification, in target-native vocabulary"
    n_heading_files = sum(
        1 for p in (ROOT / JD).rglob("*.md")
        if any(ln.lstrip().startswith("#") and heading in ln
               for ln in p.read_text(encoding="utf-8").splitlines()))
    planted = [
        ("cb-b's quarantine table already contains a positivity row "
         "(it does not — IT-C's D5 is executed in the central register)",
         "positiv" in cbb_quarantine.lower()),
        ("NAMES.md has 12 data rows", len(names_first_cells()) == 12),
        ("the steward pass rates the cone homonym high-severity",
         "high — homonym" in read(STEWARD)),
        ("the edited Portal transcript contains the word 'vial'",
         wcount(PORTAL, r"\bvial\b") > 0),
        ("the claim-status Classification heading census finds exactly 2 files "
         "(the tasking's own undercount)", n_heading_files == 2),
        ("substring and word-boundary counts of 'vial' agree on gu-40 "
         "(they must NOT — 'trivial' pollution is the demonstrated pitfall)",
         len(re.findall("vial", read(GU40), re.I)) == wcount(GU40, r"\bvial\b")),
    ]
    for label, observed in planted:
        check(f"planted false fact observed False: {label}", observed is False)


# --------------------------------------------------------------------------
# --selftest — CLEAN BASELINE FIRST, then probe mutations, then gate selftest.
# --------------------------------------------------------------------------

MUTATIONS = (
    ("word-boundary counter loosened to substring counting",
     r'    return len(re.findall(pattern, read(rel), flags))',
     r'    return len(re.findall(pattern.replace("\\b", ""), read(rel), flags))'),
    ("NAMES row parser counts header rows too",
     '        if re.match(r"^\\|\\s*-+", line):\n            in_table = True\n            continue',
     '        in_table = True\n        if re.match(r"^\\|\\s*-+", line):\n            continue'),
    ("cb-b quarantine slice shifted one row off the table",
     'quarantine = [ln for ln in cbb[183:189] if "HOMONYM" in ln]',
     'quarantine = [ln for ln in cbb[182:188] if "HOMONYM" in ln]'),
    ("packet stationary-row line index shifted",
     'packet[132].startswith("| stationary |")',
     'packet[131].startswith("| stationary |")'),
    ("gate subprocess launched on the wrong file (a red gate must red the probe)",
     'gate = subprocess.run([sys.executable, str(ROOT / GATE)],',
     'gate = subprocess.run([sys.executable, str(ROOT / REGISTER)],'),
    ("kind histogram expectation corrupted",
     '{"homonym": 30, "near_collision": 1,\n                    "prefix_collision": 1, "transcription_variant": 5}',
     '{"homonym": 29, "near_collision": 2,\n                    "prefix_collision": 1, "transcription_variant": 5}'),
    ("heading census detector reads prose lines, not headings",
     'carriers = sorted(\n        p.name for p in corpus\n        if any(ln.lstrip().startswith("#") and heading in ln\n               for ln in p.read_text(encoding="utf-8").splitlines()))',
     'carriers = sorted(\n        p.name for p in corpus\n        if heading in p.read_text(encoding="utf-8"))'),
    ("ITI chirality-assignment line index shifted off the locus",
     '"positive spinners" in iti[106]',
     '"positive spinners" in iti[105]'),
    ("gimmel quarantine sweep pointed at a token that IS quarantined",
     'and "gimmel" not in cbb_rows.lower()',
     'and "torsion" not in cbb_rows.lower()'),
    ("a planted 'false' fact that is actually true (machinery must reject it)",
     '("NAMES.md has 12 data rows", len(names_first_cells()) == 12),',
     '("NAMES.md has 12 data rows", len(names_first_cells()) == 9),'),
)


def selftest() -> int:
    me = pathlib.Path(__file__).resolve()
    source = me.read_text(encoding="utf-8")

    print("BASELINE — verifying the UNMUTATED probe exits 0 before mutating")
    base = subprocess.run([sys.executable, str(me)], capture_output=True, text=True)
    if base.returncode != 0:
        print(f"  BASELINE IS RED (exit {base.returncode}). ABORTING — mutation "
              "results would be meaningless.")
        for ln in [l for l in base.stdout.splitlines() if "[FAIL]" in l][:12]:
            print("   ", ln)
        return 1
    print("  baseline GREEN (exit 0) — mutations are now meaningful\n")

    # The mutant runs AT THE PROBE'S OWN DEPTH so ROOT = parents[2] still
    # resolves to the repository.  A deeper scratch directory would misresolve
    # ROOT and red every mutant for the same spurious missing-file reason,
    # banking a false "all caught".  Additionally, every catch must show a
    # genuine [FAIL] check line: an exit 1 with no [FAIL] is a crash, not a
    # detection, and is rejected.
    tmp = me.parent / "_fx3_mutant_tmp.py"
    caught = 0
    try:
        for name, old, new in MUTATIONS:
            if old not in source:
                print(f"  MUTATION NOT APPLICABLE (needle missing): {name}")
                return 1
            tmp.write_text(source.replace(old, new, 1), encoding="utf-8")
            result = subprocess.run([sys.executable, str(tmp)],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  NOT CAUGHT (mutant exited 0): {name}")
                return 1
            if "[FAIL]" not in result.stdout:
                print(f"  NOT A VALID CATCH (exit {result.returncode} but no "
                      f"[FAIL] check — crash, not detection): {name}")
                return 1
            caught += 1
            print(f"  caught (exit {result.returncode}, via a [FAIL] check): {name}")
    finally:
        tmp.unlink(missing_ok=True)

    print("\nCOMPOSED — the gate's own selftest (12 planted register corruptions)")
    gate_st = subprocess.run([sys.executable, str(ROOT / GATE), "--selftest"],
                             capture_output=True, text=True, cwd=str(ROOT))
    if gate_st.returncode != 0:
        print("  GATE SELFTEST FAILED")
        print(gate_st.stdout[-1500:])
        return 1
    print("  gate selftest GREEN (baseline first, 12/12 corruptions caught)")

    print(f"\n--selftest: baseline verified GREEN first, then {caught}/{len(MUTATIONS)} "
          "probe mutations drove exit 1, and the gate's 12-plant selftest passed.")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        print("FX-3 homonym register — SELFTEST (baseline first, then planted "
              "false machinery, then the gate's own selftest)")
        return selftest()

    print("=" * 74)
    print("FX-3 — the homonym register, its gate, and the receipts")
    print("=" * 74)

    leg1_prior_art()
    leg2_register_and_gate()
    leg3_incidents()
    leg4_variants()
    leg5_contrary_control()
    planted_false_facts()

    n_pass = sum(1 for ok, _ in CHECKS if ok)
    n_fail = len(CHECKS) - n_pass
    print("\n" + "=" * 74)
    print(f"CHECKS: {n_pass} passed, {n_fail} failed, {len(CHECKS)} total")
    print("=" * 74)
    if n_fail:
        for ok, label in CHECKS:
            if not ok:
                print(f"  FAILED: {label}")
        return 1

    print("""
DISPOSITION
  CONSOLIDATE, not rival.  lab/process/homonym-register.yaml absorbs
  NAMES.md row-for-row (the gate reds if NAMES.md ever outruns it), mirrors
  cb-b's quarantine and the packet's Layer-0 register as scope-local
  authorities, and leaves the per-wave layer0 blocks and [ASR] glosses in
  place as the scoped instruments they are.

  37 entries, 37 receipts, 0 coined disambiguators.  4 warn-only sensors
  (cone; the claim-status Classification heading; unglossed CHIRAL; the
  killed Spin(6,4)/Spin(3,2) spelling).  3 documented sensing refusals
  (positive, so(1,3), BD-) — a gate that reds on the word "positive" would
  be removed within a week and deserve it.

  target_claim: NONE-NOT-A-KILL.  No physics claim is adjudicated.
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
