#!/usr/bin/env python3
"""BA-1 probe: recompute the flattening-bias audit from its own table.

Reads lab/active-research/joe-directed/bias-audit/
ba1-flattening-bias-audit-2026-08-17.md, parses the fenced
```ba1-classification``` block (the canonical corpus of documented correction
events, 2026-08-14..17) and the machine-readable COUNT lines, then:

  1. recomputes every count (rule memberships R-A0/R-A/R-B/R-C, the
     direction splits, the R-C' item expansion, the layer cross-tab, the
     caught-by cross-tab, the hostile-recoding band, the exact binomial
     tails) from the table and asserts equality with the COUNT lines;
  2. verifies every `pin=` quote against its named file on disk, with
     blockquote markers stripped and whitespace normalized before a
     fixed-string match (AR-3's two demonstrated burial mechanisms: hard
     wrap and regex metacharacters -- no pin is ever fed to a regex);
  3. exercises three controls: C1 REJECT (a fabricated quote the verifier
     must fail to find -- proof the pin machinery has power), C2 WRAP (a
     quote invisible to raw line-based search and found only after
     normalization -- both directions asserted), C3 CONTRARY (the corrected
     text of a toward-favorable error, on disk, independent of this coder's
     typings -- the refutation of the claim's universal quantifier does not
     rest on direction-typing alone);
  4. asserts structural discipline: rule nesting A0 within A within B within
     C, flip flags only where the artifact argues them, exactly four
     commit-only traces, the declared made=pre set, and no float constant
     anywhere in this module's AST.

--selftest: verifies the CLEAN BASELINE passes FIRST (a red baseline aborts
rather than banking a false all-mutations-caught receipt), then runs a
RELOCATION control (an unmutated copy of this probe, run from the scratch
directory with BA1_ROOT set, must still pass -- so a mutant's failure cannot
be an artifact of relocation), then plants 10 mutations that CORRUPT
MACHINERY OR REFERENCES -- a tally swap, a parser column shift, a reversed
pin reference, an inverted control gate, a blinded normalizer, a corrupted
binomial null, a flipped layer filter, a caught-by double-increment, a
band-flag retarget, and an emptied rule parser -- never a loosened check.
Mutation needles are assembled at runtime from split pieces so the mutation
table cannot shadow its own targets. A catch counts only if the mutant fails
via a genuine [FAIL] line; a nonzero exit with no [FAIL] is reported as
CRASH-NOT-DETECTION and fails the selftest (the SG-1 harness-repair
convention, 2026-08-17).

No git command is run. No file is written outside the scratch directory.
The window commit counts (24/39/4/5) are declared constants carried from the
artifact; the probe asserts their internal consistency, not their
derivation, which requires git and is outside this probe's fence.
"""

import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

ROOT = Path(os.environ.get("BA1_ROOT") or Path(__file__).resolve().parents[2])
ARTIFACT = ROOT / ("lab/active-research/joe-directed/bias-audit/"
                   "ba1-flattening-bias-audit-2026-08-17.md")

HALF = Fraction(1, 2)
DIRECTIONS = ("A", "F", "X", "N")
LAYERS = ("Y", "N")
CAUGHT = ("independent_review", "sibling", "self", "self_channel", "gate")
MADE = ("in", "pre")
RULE_TOKENS = ("A0", "A", "B", "C", "NONE")
KINDS = ("S", "P", "G")
COMMIT_ONLY_EXPECTED = ("P5", "G9", "G10", "G11")
MADE_PRE_EXPECTED = ("S6", "S7", "S8", "S9", "P7", "P8", "P9", "P10")

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    line = ("[PASS] " if ok else "[FAIL] ") + label
    if detail and not ok:
        line += " :: " + detail
    print(line)
    return ok


def norm(s):
    """Strip blockquote markers, then collapse all whitespace runs."""
    out = re.sub(r"(?m)^[>\s]+", " ", s)
    out = re.sub(r"\s+", " ", out)
    return out


def pin_in_text(pin, text):
    return pin in text


class Ev(object):
    __slots__ = ("kind", "rid", "slug", "direction", "layer", "caught",
                 "made", "rules", "kv")

    def __init__(self, kind, rid, slug, direction, layer, caught, made,
                 rules, kv):
        self.kind = kind
        self.rid = rid
        self.slug = slug
        self.direction = direction
        self.layer = layer
        self.caught = caught
        self.made = made
        self.rules = rules
        self.kv = kv

    @property
    def flip(self):
        return self.kv.get("flip", "none")

    @property
    def items(self):
        return int(self.kv.get("items", "1"))


def parse_rows(block):
    rows = []
    for raw in block.splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split("|")
        if len(parts) < 8:
            check("table row has >= 8 fields", False, line[:60])
            continue
        kind = parts[0]
        rid = parts[1]
        slug = parts[2]
        direction = parts[3]
        layer = parts[4]
        caught = parts[5]
        made = parts[6]
        rules = frozenset(t.strip() for t in parts[7].split(","))
        kv = {}
        for extra in parts[8:]:
            if "=" in extra:
                k, v = extra.split("=", 1)
                kv[k] = v
        rows.append(Ev(kind, rid, slug, direction, layer, caught, made,
                       rules, kv))
    return rows


def tally(events):
    counts = {"A": 0, "F": 0, "X": 0, "N": 0}
    for e in events:
        if e.direction in counts:
            counts[e.direction] += 1
    return counts


def binom_upper_tail(k, n):
    """P(X >= k) for X ~ Binomial(n, HALF), exact Fraction."""
    total = Fraction(0)
    for j in range(k, n + 1):
        c = 1
        for i in range(j):
            c = c * (n - i) // (i + 1)
        total += c * (HALF ** n)
    return total


def parse_counts(text):
    out = {}
    for m in re.finditer(r"^COUNT ([^:]+): (.+)$", text, re.M):
        out[m.group(1).strip()] = m.group(2).strip()
    return out


def kv_ints(spec):
    out = {}
    for tok in spec.split():
        k, v = tok.split("=", 1)
        out[k] = v
    return out


def main():
    if not ARTIFACT.is_file():
        check("artifact exists at declared path", False, str(ARTIFACT))
        return finish()
    text = ARTIFACT.read_text(encoding="utf-8")
    ntext = norm(text)

    fence = re.search(r"```ba1-classification\n(.*?)```", text, re.S)
    if not check("ba1-classification block present", bool(fence)):
        return finish()
    rows = parse_rows(fence.group(1))

    # -- structural validation ------------------------------------------
    bad_rows = []
    for e in rows:
        ok = (e.kind in KINDS + ("CTRL",) and e.direction in DIRECTIONS
              and e.layer in LAYERS and e.caught in CAUGHT
              and e.made in MADE and e.rules
              and e.rules.issubset(set(RULE_TOKENS)))
        if not ok:
            bad_rows.append(e.rid)
    check("all table rows carry valid closed-vocabulary tokens",
          not bad_rows, " ".join(bad_rows))

    evs = [e for e in rows if e.kind in KINDS]
    ctrls = {e.rid: e for e in rows if e.kind == "CTRL"}
    check("row census: 13 S + 10 P + 16 G + 3 CTRL",
          (sum(1 for e in evs if e.kind == "S") == 13
           and sum(1 for e in evs if e.kind == "P") == 10
           and sum(1 for e in evs if e.kind == "G") == 16
           and len(ctrls) == 3),
          "S=%d P=%d G=%d CTRL=%d" % (
              sum(1 for e in evs if e.kind == "S"),
              sum(1 for e in evs if e.kind == "P"),
              sum(1 for e in evs if e.kind == "G"), len(ctrls)))

    nest_ok = True
    for e in evs:
        if "A0" in e.rules and "A" not in e.rules:
            nest_ok = False
        if "A" in e.rules and "B" not in e.rules:
            nest_ok = False
        if "B" in e.rules and "C" not in e.rules:
            nest_ok = False
        if e.kind in ("P", "G") and e.rules != frozenset(["C"]):
            nest_ok = False
    check("rule nesting A0<=A<=B<=C; P/G rows carry exactly C", nest_ok)

    check("R-A0 members are all made=in",
          all(e.made == "in" for e in evs if "A0" in e.rules))
    pre = sorted(e.rid for e in evs if e.made == "pre")
    check("made=pre set is exactly the declared eight",
          pre == sorted(MADE_PRE_EXPECTED), " ".join(pre))

    flips_ok = True
    for e in evs:
        if e.flip == "both" and e.direction != "X":
            flips_ok = False
        if e.flip == "F" and e.direction != "A":
            flips_ok = False
        if e.flip not in ("none", "F", "both"):
            flips_ok = False
    check("flip flags: both only on X rows, F only on A rows", flips_ok)

    commit_only = sorted(e.rid for e in evs
                         if "commit" in e.kv and "file" not in e.kv)
    check("exactly four commit-only traces (P5,G9,G10,G11)",
          commit_only == sorted(COMMIT_ONLY_EXPECTED), " ".join(commit_only))
    check("every non-commit-only event names a file and a pin",
          all(("file" in e.kv and "pin" in e.kv) for e in evs
              if e.rid not in COMMIT_ONLY_EXPECTED))
    check("every pin is at least 12 characters",
          all(len(e.kv["pin"]) >= 12 for e in rows if "pin" in e.kv))

    # -- recompute the COUNT lines --------------------------------------
    counts = parse_counts(text)

    def rule_members(tok):
        return [e for e in evs if tok in e.rules]

    for rule, key in (("A0", "R-A0"), ("A", "R-A"), ("B", "R-B"),
                      ("C", "R-C")):
        mem = rule_members(rule)
        t = tally(mem)
        want = kv_ints(counts.get(key, ""))
        got = {"n": str(len(mem)), "A": str(t["A"]), "F": str(t["F"]),
               "X": str(t["X"]), "N": str(t["N"])}
        check("COUNT %s recomputed from the table" % key, got == want,
              "got %s want %s" % (got, want))

    rc_items = sum(e.items for e in rule_members("C"))
    check("COUNT R-Cprime-items recomputed",
          kv_ints(counts.get("R-Cprime-items", "")) == {"n": str(rc_items)},
          "got n=%d" % rc_items)

    rb = rule_members("B")
    ly = sum(1 for e in rb if e.layer == "Y")
    layer_tab = {}
    for dname, dtok in (("adverse", "A"), ("favorable", "F"),
                        ("ambiguous", "X"), ("neutral", "N")):
        layer_tab[dname + "Y"] = sum(1 for e in rb if e.direction == dtok
                                     and e.layer == "Y")
        layer_tab[dname + "N"] = sum(1 for e in rb if e.direction == dtok
                                     and e.layer == "N")
    got_layer = {"layerY": str(ly), "layerN": str(len(rb) - ly)}
    got_layer.update({k: str(v) for k, v in layer_tab.items()})
    check("COUNT layer-RB recomputed",
          got_layer == kv_ints(counts.get("layer-RB", "")),
          "got %s" % got_layer)
    check("mechanism fragment: all 5 toward-adverse R-B events are layer "
          "collapses, and layer collapses are NOT all adverse",
          layer_tab["adverseY"] == 5 and layer_tab["adverseN"] == 0
          and layer_tab["favorableY"] >= 2)

    cbt = {}
    for e in rb:
        cbt[e.caught] = cbt.get(e.caught, 0) + 1
    check("COUNT caught-RB recomputed",
          kv_ints(counts.get("caught-RB", "")) == {
              k: str(v) for k, v in cbt.items()},
          "got %s" % cbt)

    def dirvec(channel):
        t = tally([e for e in rb if e.caught == channel])
        return "%d,%d,%d,%d" % (t["A"], t["F"], t["X"], t["N"])

    got_cd = {"iv": dirvec("independent_review"),
              "sibling": dirvec("sibling"),
              "self": dirvec("self_channel")}
    check("COUNT caught-RB-direction recomputed",
          got_cd == kv_ints(counts.get("caught-RB-direction", "")),
          "got %s" % got_cd)
    check("independent review and siblings each caught a toward-favorable "
          "error (selection is not one-directional among catches)",
          int(got_cd["iv"].split(",")[1]) > 0
          and int(got_cd["sibling"].split(",")[1]) > 0)

    t_rb = tally(rb)
    amb = [e for e in rb if e.direction == "X"]
    aflip = [e for e in rb if e.direction == "A" and e.flip == "F"]
    denom = t_rb["A"] + t_rb["F"] + len(amb)
    band_max = Fraction(t_rb["A"] + len(amb), denom)
    band_min = Fraction(t_rb["A"] - len(aflip), denom)
    want_band = kv_ints(counts.get("band-RB", ""))
    check("COUNT band-RB recomputed from flip flags",
          (want_band.get("min") == "%d/%d" % (band_min.numerator,
                                              band_min.denominator)
           and want_band.get("max") == "%d/%d" % (band_max.numerator,
                                                  band_max.denominator)),
          "got %s..%s" % (band_min, band_max))
    check("the hostile-recoding band straddles one half",
          band_min < HALF < band_max)

    tails_want = kv_ints(counts.get("tails", ""))
    tails_got = {}
    for rule, key in (("A0", "RA0"), ("A", "RA"), ("B", "RB")):
        t = tally(rule_members(rule))
        tail = binom_upper_tail(t["A"], t["A"] + t["F"])
        tails_got[key] = "%d/%d" % (tail.numerator, tail.denominator)
    check("COUNT tails recomputed (exact binomial upper tails)",
          tails_got == tails_want, "got %s want %s" % (tails_got, tails_want))
    check("no rule's directional split approaches the claim's universal "
          "(every upper tail >= 1/4 under the symmetric null)",
          all(Fraction(*(int(x) for x in v.split("/"))) >= Fraction(1, 4)
              for v in tails_got.values()))

    wc = kv_ints(counts.get("window-commits", ""))
    check("window commit constants internally consistent (24+39+4+5=72)",
          (wc and int(wc["d14"]) + int(wc["d15"]) + int(wc["d16"])
           + int(wc["d17"]) == int(wc["total"]) == 72
           and wc["d15"] == "39"),
          "got %s" % wc)

    # -- pin verification against the live tree -------------------------
    cache = {}

    def file_norm(rel):
        if rel not in cache:
            p = ROOT / rel
            cache[rel] = (norm(p.read_text(encoding="utf-8"))
                          if p.is_file() else None)
        return cache[rel]

    for e in evs:
        if "file" not in e.kv:
            continue
        body = file_norm(e.kv["file"])
        if body is None:
            check("pin %s: file present" % e.rid, False, e.kv["file"])
            continue
        check("pin %s verified in %s" % (e.rid, Path(e.kv["file"]).name),
              pin_in_text(e.kv["pin"], body), e.kv["pin"][:50])

    # -- controls --------------------------------------------------------
    c1 = ctrls.get("C1")
    if check("control C1 present with expect=REJECT",
             c1 is not None and c1.kv.get("expect") == "REJECT"):
        body = file_norm(c1.kv["file"])
        found_fake = body is not None and pin_in_text(c1.kv["pin"], body)
        c1_ok = not found_fake
        check("[C] C1 fabricated quote REJECTED by the same verifier that "
              "accepts the real pins", c1_ok)

    c2 = ctrls.get("C2")
    if check("control C2 present with expect=WRAP",
             c2 is not None and c2.kv.get("expect") == "WRAP"):
        p = ROOT / c2.kv["file"]
        raw_lines = (p.read_text(encoding="utf-8").splitlines()
                     if p.is_file() else [])
        on_one_line = any(c2.kv["pin"] in ln for ln in raw_lines)
        body = file_norm(c2.kv["file"])
        found_norm = body is not None and pin_in_text(c2.kv["pin"], body)
        check("[C] C2 wrap-power: raw line search misses the quote",
              not on_one_line)
        check("[C] C2 wrap-power: normalized search finds the quote",
              found_norm)

    c3 = ctrls.get("C3")
    if check("control C3 present with expect=CONTRARY and direction F",
             c3 is not None and c3.kv.get("expect") == "CONTRARY"
             and c3.direction == "F"):
        body = file_norm(c3.kv["file"])
        check("[C] C3 contrary control: a toward-favorable error's "
              "correction of record exists on disk",
              body is not None and pin_in_text(c3.kv["pin"], body))

    # -- residual and verdict integrity ----------------------------------
    ar3 = file_norm("lab/active-research/joe-directed/archaeology/"
                    "ar3-rediscovery-rate-2026-08-15.md")
    check("residual reported in section 7 is real: AR-3 still carries the "
          "withdrawn disavowal reading",
          ar3 is not None and "disavowed by the source" in ar3)
    check("artifact quotes the claim verbatim",
          "toward the MORE DAMNING reading of GU" in text)
    check("artifact retires the claim and forbids citing it either way",
          "RETIRED AND MAY NOT BE CITED IN EITHER DIRECTION" in text
          and "REFUTED AS STATED" in text)
    check("artifact carries the corrected source polarity, not the "
          "withdrawn one",
          "observed-sector positivity is source-OPEN" in ntext)

    # -- self-hygiene -----------------------------------------------------
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    has_float = any(isinstance(n, ast.Constant)
                    and isinstance(n.value, (float, complex))
                    for n in ast.walk(tree))
    check("no float or complex constant anywhere in this module's AST",
          not has_float)

    return finish()


def finish():
    total = len(RESULTS)
    passed = sum(1 for r in RESULTS if r)
    print("%d/%d checks passed" % (passed, total))
    if passed == total:
        print("joe_directed_ba1_flattening_bias_audit: exit 0")
        return 0
    print("joe_directed_ba1_flattening_bias_audit: exit 1")
    return 1


# ---------------------------------------------------------------------------
# Selftest: baseline first, relocation control, then machinery mutations.
# Needles are assembled from split pieces at runtime so the entries below
# cannot shadow their own targets in the source text.
# ---------------------------------------------------------------------------

MUTATIONS = [
    ("tally-direction-swap",
     ("            counts[e.dir", "ection] += 1"),
     "            counts[{'A': 'F', 'F': 'A', 'X': 'X', 'N': 'N'}"
     "[e.direction]] += 1"),
    ("parser-column-shift",
     ("        direction = par", "ts[3]"),
     "        direction = parts[4]"),
    ("pin-reference-reversed",
     ("def pin_in_text(pin, text):\n    return p", "in in text"),
     "def pin_in_text(pin, text):\n    return pin[::-1] in text"),
    ("control-gate-inverted",
     ("        c1_ok = not fo", "und_fake"),
     "        c1_ok = found_fake"),
    ("normalizer-blinded",
     ('    out = re.sub(r"\\s+', '", " ", out)'),
     "    out = out"),
    ("binomial-null-corrupted",
     ("HALF = Fraction(", "1, 2)"),
     "HALF = Fraction(1, 3)"),
    ("layer-filter-flipped",
     ('    ly = sum(1 for e in rb if e.la', 'yer == "Y")'),
     '    ly = sum(1 for e in rb if e.layer == "N")'),
    ("caught-tally-double-increment",
     ("        cbt[e.caught] = cbt.get(e.ca", "ught, 0) + 1"),
     "        cbt[e.caught] = cbt.get(e.caught, 0) + 2"),
    ("band-flag-retargeted",
     ('    aflip = [e for e in rb if e.direction == "A" and e.fl',
      'ip == "F"]'),
     '    aflip = [e for e in rb if e.direction == "A" and e.flip == "Q"]'),
    ("rule-parser-emptied",
     ("        rules = frozenset(t.strip() for t in par",
      'ts[7].split(","))'),
     "        rules = frozenset()"),
]


def run_copy(path, env):
    proc = subprocess.run([sys.executable, str(path)], cwd=str(ROOT),
                          env=env, capture_output=True, text=True,
                          timeout=300)
    return proc.returncode, proc.stdout + proc.stderr


def self_test():
    env = dict(os.environ)
    env["BA1_ROOT"] = str(ROOT)
    src_path = Path(__file__).resolve()
    source = src_path.read_text(encoding="utf-8")

    print("== selftest: clean baseline first ==")
    rc, out = run_copy(src_path, env)
    if rc != 0:
        print(out)
        print("SELFTEST ABORT: clean baseline is RED; mutations were NOT "
              "run (a red baseline cannot certify catches).")
        return 1
    print("[PASS] clean baseline exits 0")

    scratch = Path(tempfile.mkdtemp(
        prefix="ba1-selftest-",
        dir=os.environ.get("BA1_SCRATCH") or None))
    try:
        print("== selftest: relocation control ==")
        reloc = scratch / "reloc_unmutated.py"
        reloc.write_text(source, encoding="utf-8")
        rc, out = run_copy(reloc, env)
        if rc != 0:
            print(out)
            print("SELFTEST ABORT: unmutated relocated copy is RED; a "
                  "mutant failure would be a relocation artifact, not a "
                  "detection (the SG-1 lesson).")
            return 1
        print("[PASS] relocated unmutated copy exits 0")

        ok = True
        for name, pieces, repl in MUTATIONS:
            target = pieces[0] + pieces[1]
            n_hits = source.count(target)
            if n_hits != 1:
                print("[FAIL] mutation %s: target substring count %d != 1"
                      % (name, n_hits))
                ok = False
                continue
            mutant = scratch / ("mutant_%s.py" % name.replace("-", "_"))
            mutant.write_text(source.replace(target, repl),
                              encoding="utf-8")
            rc, out = run_copy(mutant, env)
            if rc == 0:
                print("[FAIL] mutation %s NOT CAUGHT (exit 0)" % name)
                ok = False
            elif "[FAIL]" not in out:
                print("[FAIL] mutation %s CRASH-NOT-DETECTION (nonzero "
                      "exit with no [FAIL] line)" % name)
                ok = False
            else:
                print("[PASS] mutation %s caught via genuine [FAIL] "
                      "(exit %d)" % (name, rc))
        print("SELFTEST " + ("GREEN: baseline green first, relocation "
                             "control green, 10/10 mutations caught via "
                             "genuine [FAIL] lines" if ok else "FAILED"))
        return 0 if ok else 1
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
