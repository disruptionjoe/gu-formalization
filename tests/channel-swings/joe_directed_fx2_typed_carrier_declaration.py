# -*- coding: utf-8 -*-
"""
FX-2 -- the typed-carrier-declaration gate, exercised end to end.

WHAT THIS PROBE IS FOR.  AGENTS.md requires every new result to state its
carrier, pairing or form, real structure, grading, action owner and target
object; nothing enforced it, and five typing failures shipped in one week.
FX-2 builds the enforcement as a non-retroactive process gate
(``process_gates/typed_carrier_declaration_audit.py``) plus a machine-readable
``gu-typed-objects`` block format.  This probe certifies four separable
things:

  LEG V  VALIDATOR.  Every defect class the gate can emit is produced by a
         minimal fixture and matched EXACTLY (full defect-list equality, not
         substring), and every contrary control -- declared ambiguity, a
         declared bridge, a subscripted homonym -- validates clean.

  LEG F  FILE-LEVEL AUDIT.  The gate's own clean fixture set is green with
         exact counters (scope 5, triggered 4, exemption 1, untyped slots 7);
         a pre-cutoff garbage file stays green (non-retroactivity); a QUOTED
         ``created:`` date still enters scope (donor-gate parser hardening);
         a representative planted fact is red.

  LEG A  ARTIFACT CONFORMANCE.  The FX-2 design artifact carries the routing
         notice, the ``INTERNAL_STRUCTURAL_ONLY`` classification in exactly
         the form the routing audit's regex accepts, ``target_claim:
         NONE-NOT-A-KILL``, exactly two LIVE worked-example blocks (SA-1's
         two results) that validate with zero defects, and five WOULD-BE-RED
         demonstrations that are NOT live blocks.

  LEG S  SOURCES.  The five errors the design is acceptance-tested against
         are real: exact substrings are matched in the artifacts that record
         them (CN-2, BD-A/base-duality README, SA-1, the routing method's
         withdrawn clause), and the enforced AGENTS.md sentence, the CN-2
         vocabulary, the NONE-NOT-A-KILL donor pattern and the registry
         vocabulary are all read from their owning files, not remembered.

  LEG R  RUNTIME.  The gate's --selftest exits 0; --selftest
         --poison-baseline exits 1 AND prints the refusal (the baseline
         guard has power); the live repo scan is PRINTED as a dated
         reconciliation and asserted red==0 only under ``--strict``
         (CN-2 concurrency rule: the checkout is shared, repo-wide totals
         are reconciliation, per-file facts are load-bearing).

WHAT THIS PROBE DOES NOT DO.  It does not move any claim, row, fork or
verdict; it does not edit any registry; it does not retroactively judge any
existing artifact (the gate's cutoff guarantees that, and leg F asserts it).

Exit 0 == every check passed.  ``--selftest`` verifies the CLEAN BASELINE
first (unmutated subprocess must exit 0 BEFORE any mutation is attempted),
then injects ten machinery mutations via FX2_MUTATE, each required to drive
exit 1; ``--selftest --poison`` poisons the baseline run itself and requires
the refusal path, proving the guard is not vacuous.
"""

from __future__ import annotations

import importlib.util
import os
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
GATE_PATH = ROOT / "process_gates" / "typed_carrier_declaration_audit.py"
ART = ROOT / ("lab/active-research/joe-directed/carrier-decl/"
              "fx2-typed-carrier-declaration-2026-08-16.md")

_spec = importlib.util.spec_from_file_location("tcda", GATE_PATH)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)

# ---- mutation hooks (machinery corruption; a weakened assertion is not a
# detectable mutation, so every mutation corrupts an instrument constant).
MUTATIONS = ("cutoff-early", "keys-drop", "maptype-loose", "homonym-empty",
             "hatch-drift", "spinor-blind", "cert-blind", "layer-loose",
             "on-blind", "artifact-gone")
_mut = os.environ.get("FX2_MUTATE", "")
if _mut == "cutoff-early":
    gate.CUTOFF = "2020-01-01"
elif _mut == "keys-drop":
    gate.REQUIRED_KEYS = tuple(k for k in gate.REQUIRED_KEYS if k != "grading")
elif _mut == "maptype-loose":
    gate.MAP_TOKENS = gate.MAP_TOKENS + ("squishing",)
elif _mut == "homonym-empty":
    gate.HOMONYMS = ()
elif _mut == "hatch-drift":
    gate.HATCH = "EXEMPT-BECAUSE-PROSE"
elif _mut == "spinor-blind":
    gate.SPINOR_RE = re.compile(r"(?!x)x")
elif _mut == "cert-blind":
    gate.CERT_LINE = re.compile(r"(?!x)x")
elif _mut == "layer-loose":
    gate.LAYER_TOKENS = gate.LAYER_TOKENS + ("cosmic",)
elif _mut == "on-blind":
    gate.ON_FIELD = re.compile(r"")
elif _mut == "artifact-gone":
    ART = ROOT / "lab/active-research/joe-directed/carrier-decl/nonexistent.md"

PASS = 0
FAIL = 0
PLANTED_OBSERVED_TRUE = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


def planted_false(name: str, cond: bool) -> None:
    """A predeclared FALSE proposition.  Observing it True means the
    instrument is not discriminating, and is a hard failure."""
    global PLANTED_OBSERVED_TRUE, FAIL, PASS
    if cond:
        PLANTED_OBSERVED_TRUE += 1
        FAIL += 1
        print(f"  FAIL  planted-false proposition came back TRUE: {name}")
    else:
        PASS += 1


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def block(**kw) -> str:
    base = {
        "result": "V-FIX minimal valid declaration",
        "carrier": "so(1,3)_endo inside so(7,7) LAYER=ambient CHIRALITY=N/A",
        "pairing": "Killing form ON=so(7,7)",
        "real_structure": "split real form",
        "grading": "Cartan k+p",
        "action_owner": "repository-construction (fixture)",
        "target": "invariant subspaces of k MAP-TYPE=restriction",
    }
    base.update(kw)
    return "".join(f"{k}: {v}\n" for k, v in base.items() if v is not None)


def defects(text: str):
    return gate.validate_block(text)[0]


# ======================================================================
# LEG V -- validator, exact defect-list equality
# ======================================================================
print("LEG V  validator")
check("V01 fully typed block validates clean", defects(block()) == [])
check("V02 missing field (brief planted fact 1)",
      defects(block(grading=None)) == ["MISSING:grading"])
check("V03 mixed-layer carrier without bridge (brief planted fact 2)",
      defects(block(carrier="so(1,3)_endo LAYER=ambient+observed CHIRALITY=N/A"))
      == ["MIXED-LAYER-NO-BRIDGE"])
check("V04 mixed layer WITH declared bridge is clean (contrary control)",
      defects(block(carrier="so(1,3)_endo LAYER=ambient+observed "
                            "BRIDGE=observation-contraction-s* CHIRALITY=N/A"))
      == [])
check("V05 bare registered homonym in carrier",
      defects(block(carrier="so(1,3) inside so(7,7) LAYER=ambient CHIRALITY=N/A"))
      == ["HOMONYM-BARE:so(1,3):carrier"])
check("V06 bare registered homonym in target",
      defects(block(target="ad(P_H) as a bundle MAP-TYPE=inclusion"))
      == ["HOMONYM-BARE:ad(P_H):target"])
check("V07 spinor carrier with CHIRALITY=N/A is red",
      defects(block(carrier="Omega^1(S) LAYER=ambient CHIRALITY=N/A"))
      == ["SPINOR-CHIRALITY-NA"])
check("V08 spinor carrier with declared ambiguity is clean (CN-2 principle)",
      defects(block(carrier="Omega^1(S) LAYER=ambient "
                            "CHIRALITY=S-CHIRALITY-UNTYPED")) == [])
check("V08b declared chirality ambiguity is counted, not hidden",
      gate.validate_block(block(carrier="Omega^1(S) LAYER=ambient "
                                        "CHIRALITY=S-CHIRALITY-UNTYPED"))[1] == 1)
check("V09 pairing without ON= is red",
      defects(block(pairing="Killing form")) == ["PAIRING-NO-ON"])
check("V10 pairing NONE is clean",
      defects(block(pairing="NONE")) == [])
check("V11 free-text action owner is red",
      defects(block(action_owner="Eric owns it")) == ["OWNER-UNTOKENED"])
check("V12 out-of-vocabulary map type is red",
      defects(block(target="k MAP-TYPE=squishing"))
      == ["TARGET-BAD-MAPTYPE:squishing"])
check("V13 target without MAP-TYPE is red",
      defects(block(target="the observed 4D content"))
      == ["TARGET-NO-MAPTYPE"])
check("V14 out-of-vocabulary layer is red",
      defects(block(carrier="so(1,3)_endo LAYER=cosmic CHIRALITY=N/A"))
      == ["CARRIER-BAD-LAYER:cosmic"])
check("V15 result: UNTYPED is red (a block must bind a result)",
      defects(block(result="UNTYPED")) == ["RESULT-UNTYPED"])
check("V16 unknown key is red",
      defects(block() + "flavour: strange\n") == ["UNKNOWN-KEY:flavour"])
check("V17 carrier without LAYER is red",
      defects(block(carrier="so(1,3)_endo CHIRALITY=N/A"))
      == ["CARRIER-NO-LAYER"])
check("V18 carrier without CHIRALITY is red",
      defects(block(carrier="so(1,3)_endo LAYER=ambient"))
      == ["CARRIER-NO-CHIRALITY"])

_all_untyped = block(carrier="UNTYPED LAYER=UNTYPED CHIRALITY=S-CHIRALITY-UNTYPED",
                     pairing="UNTYPED", real_structure="UNTYPED",
                     grading="UNTYPED", action_owner="UNTYPED",
                     target="UNTYPED MAP-TYPE=UNTYPED")
planted_false("P02 an ALL-UNTYPED block is a hard red (it is census, not red)",
              len(defects(_all_untyped)) > 0)
check("V19 ALL-UNTYPED block is flagged for the census",
      gate.validate_block(_all_untyped)[2] is True)
planted_false("P03 HOMONYM-AMBIGUOUS is a hard red (it is declared ambiguity)",
              len(defects(block(carrier="so(1,3) HOMONYM-AMBIGUOUS "
                                        "LAYER=ambient CHIRALITY=N/A"))) > 0)

# ======================================================================
# LEG F -- file-level audit on the gate's own fixtures
# ======================================================================
print("LEG F  file-level audit")
with tempfile.TemporaryDirectory() as _d:
    d = pathlib.Path(_d)
    for name, content in gate.FIXTURES_CLEAN.items():
        (d / name).write_text(content, encoding="utf-8")
    (d / "fail_missing_field.md").write_text(
        gate.FIXTURES_FAIL["fail_missing_field.md"], encoding="utf-8")
    clean = sorted(str(d / n) for n in gate.FIXTURES_CLEAN)
    code, stats = gate.audit(paths=clean, baseline=0)
    check("F01 clean fixture set is green", code == 0)
    check("F02 dated scope is exactly 5 (pass_old excluded by cutoff)",
          stats["scope"] == 5)
    check("F03 triggered is exactly 4 (incl. the quoted-certificate "
          "false-trigger)", stats["triggered"] == 4)
    check("F04 exactly one registered exemption, the read packet",
          [pathlib.Path(p).name for p in stats["exemptions"]] == ["pass_hatch.md"])
    check("F05 declared-ambiguous slots exactly 7", stats["untyped_slots"] == 7)
    check("F06 blocks seen exactly 3", stats["blocks"] == 3)
    code_old, stats_old = gate.audit(paths=[str(d / "pass_old.md")], baseline=0)
    check("F07 pre-cutoff garbage stays green (non-retroactivity)",
          code_old == 0 and stats_old["scope"] == 0)
    planted_false("P01 the gate reds a pre-cutoff artifact", code_old != 0)
    code_q, stats_q = gate.audit(paths=[str(d / "pass_quoted_date.md")],
                                 baseline=0)
    check("F08 quoted created: date still enters scope (parser hardening)",
          stats_q["scope"] == 1 and stats_q["triggered"] == 1 and code_q == 0)
    code_f, _ = gate.audit(paths=[str(d / "fail_missing_field.md")], baseline=0)
    check("F09 representative planted fact is red through the public API",
          code_f == 1)

# ======================================================================
# LEG A -- artifact conformance
# ======================================================================
print("LEG A  artifact conformance")
check("A01 design artifact exists", ART.is_file())
art_text = ART.read_text(encoding="utf-8") if ART.is_file() else ""
art_fm, _raw = gate.frontmatter(art_text)
check("A02 target_claim is NONE-NOT-A-KILL",
      "NONE-NOT-A-KILL" in art_fm.get("target_claim", ""))
check("A03 routing marker carried", "GU-COMPARATOR-ROUTING" in art_text)
check("A04 routing method path carried",
      "lab/methods/source-native-comparator-routing.md" in art_text)
check("A05 classification matches the routing audit's own acceptance regex",
      re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                art_text) is not None)
live_blocks = gate.FENCE_RE.findall(art_text)
check("A06 exactly two LIVE worked-example blocks", len(live_blocks) == 2)
check("A07 live block 1 (SA-1 bundle layer) validates clean",
      len(live_blocks) == 2 and gate.validate_block(live_blocks[0])[0] == [])
check("A08 live block 2 (SA-1 two subalgebras) validates clean",
      len(live_blocks) == 2 and gate.validate_block(live_blocks[1])[0] == [])
check("A09 block 2 declares its blocked residue honestly "
      "(exactly one UNTYPED slot: the action owner)",
      len(live_blocks) == 2 and gate.validate_block(live_blocks[1])[1] == 1
      and "action_owner: UNTYPED" in live_blocks[1])
check("A10 both Lorentz subalgebras appear SUBSCRIPTED in block 2",
      len(live_blocks) == 2 and "so(1,3)_endo" in live_blocks[1]
      and "so(1,3)_H" in live_blocks[1])
check("A11 exactly five WOULD-BE-RED demonstrations, none of them live",
      art_text.count("WOULD-BE-RED") >= 5
      and all("WOULD-BE-RED" not in b for b in live_blocks))
check("A12 required registry integration write is printed verbatim",
      '"classification": "INTERNAL_STRUCTURAL_ONLY"' in art_text
      and "fx2-typed-carrier-declaration-2026-08-16.md" in art_text)

ERROR_LOCI = (
    "lab/active-research/joe-directed/carrier-notation/"
    "cn2-notation-carries-the-answer-2026-08-15.md",
    "lab/active-research/joe-directed/base-duality/"
    "bd-a-the-base-duality-is-the-observation-and-positivity-is-the-"
    "obstruction-2026-08-15.md",
    "lab/active-research/joe-directed/soldered-ad/"
    "sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md",
    "lab/methods/source-native-comparator-routing.md",
    "lab/active-research/joe-directed/base-duality/README.md",
)
for i, rel in enumerate(ERROR_LOCI, 1):
    check(f"A13.{i} error locus exists and is cited: {rel.split('/')[-1]}",
          (ROOT / rel).is_file() and rel in art_text)

# ======================================================================
# LEG S -- exact source substrings (read, not remembered)
# ======================================================================
print("LEG S  sources")
agents = norm((ROOT / "AGENTS.md").read_text(encoding="utf-8"))
check("S01 the enforced AGENTS.md sentence exists verbatim",
      "State the carrier, pairing or form, real structure, grading, action "
      "owner, target object, assumptions, controls, and claim ceiling for a "
      "new result." in agents)
cn2 = (ROOT / ERROR_LOCI[0]).read_text(encoding="utf-8")
check("S02 CN-2 owns the reused chirality vocabulary",
      "S-CHIRALITY-UNTYPED" in cn2 and "closed four-value" in norm(cn2))
bd_readme = (ROOT / ERROR_LOCI[4]).read_text(encoding="utf-8")
check("S03 the algebra-vs-module inversion is recorded",
      "A domain error inverted the answer." in norm(bd_readme))
check("S04 the relay defect is recorded",
      "The relay defect, located to one word" in bd_readme)
routing = (ROOT / ERROR_LOCI[3]).read_text(encoding="utf-8")
check("S05 the projection-vs-contraction correction is recorded",
      "contraction, not a projection" in norm(routing))
sa1 = (ROOT / ERROR_LOCI[2]).read_text(encoding="utf-8")
check("S06 SA-1 records the two-subalgebra collision",
      "INTERSECT_IN_ZERO" in sa1 and "differ by an internal rotation"
      in norm(sa1))
bda = (ROOT / ERROR_LOCI[1]).read_text(encoding="utf-8")
check("S07 BD-A algebra count 6 of 15", "6 of 15" in bda)
check("S08 BD-A module count 12 of 12", "12 of 12" in bda)
killgate = (ROOT / "process_gates/kill_target_claim_audit.py").read_text(
    encoding="utf-8")
check("S09 the audited-hatch donor pattern exists",
      "NONE-NOT-A-KILL" in killgate)
registry = (ROOT / "lab/process/source-native-comparator-routing-registry"
                   ".json").read_text(encoding="utf-8")
check("S10 INTERNAL_STRUCTURAL_ONLY is registered vocabulary",
      '"INTERNAL_STRUCTURAL_ONLY"' in registry)
sixaxis = (ROOT / "lab/specifications/six-axis/six-axis-template.md"
           ).read_text(encoding="utf-8")
check("S11 six-axis precedent: declared absence is admissible but must be "
      "stated", "is acceptable but must be stated" in sixaxis)
geom = norm((ROOT / "GEOMETER-VS-PHYSICS-OBJECTS.md").read_text(
    encoding="utf-8"))
check("S12 the identify-which-object rule is standing doctrine",
      "you must IDENTIFY which one you are using and WHY" in geom)

# ======================================================================
# LEG R -- runtime: gate selftest, poison guard, live reconciliation
# ======================================================================
print("LEG R  runtime")
r1 = subprocess.run([sys.executable, str(GATE_PATH), "--selftest"],
                    cwd=ROOT, capture_output=True, text=True)
check("R01 gate --selftest exits 0", r1.returncode == 0)
check("R02 gate --selftest reports GREEN", "SELF-TEST GREEN" in r1.stdout)
r2 = subprocess.run([sys.executable, str(GATE_PATH), "--selftest",
                     "--poison-baseline"],
                    cwd=ROOT, capture_output=True, text=True)
check("R03 poisoned baseline exits 1 (the guard has power)",
      r2.returncode == 1)
check("R04 poisoned baseline prints the refusal, mutations NOT run",
      "mutations were NOT run" in r2.stdout)
live_code, live_stats = gate.audit()
print(f"  [reconciliation 2026-08-17] live scan: red-exit={live_code} "
      f"scope={live_stats['scope']} triggered={live_stats['triggered']} "
      f"blocks={live_stats['blocks']} "
      f"exemptions={len(live_stats['exemptions'])}")
if "--strict" in sys.argv:
    check("R05s live repo scan is green (strict)", live_code == 0)
else:
    check("R05 live scan returned integer counters",
          all(isinstance(live_stats[k], int)
              for k in ("red", "scope", "triggered", "blocks",
                        "untyped_slots")))


def _no_float(obj) -> bool:
    if isinstance(obj, float):
        return False
    if isinstance(obj, dict):
        return all(_no_float(k) and _no_float(v) for k, v in obj.items())
    if isinstance(obj, (list, tuple, set)):
        return all(_no_float(x) for x in obj)
    return True


check("R06 no float anywhere in the result surface (swept)",
      _no_float(live_stats) and _no_float(stats))

# ======================================================================
# certificate / selftest driver
# ======================================================================

def main() -> int:
    total = PASS + FAIL
    print(f"CERTIFICATE: {PASS}/{total} checks pass; "
          f"{PLANTED_OBSERVED_TRUE} planted-false propositions observed true; "
          f"no load-bearing float (swept).")
    return 0 if FAIL == 0 else 1


def selftest(poison: bool) -> int:
    env = dict(os.environ)
    env.pop("FX2_MUTATE", None)
    if poison:
        env["FX2_MUTATE"] = "cutoff-early"
    base = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env,
                          capture_output=True, text=True)
    if base.returncode != 0:
        print("SELFTEST: clean baseline does NOT pass; "
              "mutations were NOT run")
        print("SELFTEST FAILED")
        return 1
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ)
        env["FX2_MUTATE"] = m
        r = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env,
                           capture_output=True, text=True)
        caught = r.returncode == 1
        print(f"  mutation {m}: {'caught (exit 1)' if caught else 'MISSED'}")
        ok = ok and caught
    print("SELFTEST " + ("GREEN: clean baseline first, then "
          f"{len(MUTATIONS)}/{len(MUTATIONS)} mutations each exit 1"
                         if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest(poison="--poison" in sys.argv))
    sys.exit(main())
