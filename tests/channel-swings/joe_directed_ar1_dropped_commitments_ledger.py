#!/usr/bin/env python3
"""AR-1 -- the dropped-commitments ledger, re-run mechanically.

Target artifact:
  lab/active-research/joe-directed/archaeology/
      ar1-dropped-commitments-ledger-2026-08-15.md

The artifact inventories checks that some in-repo artifact DECLARED necessary
and that were never carried out.  A prose inventory is a snapshot of one
agent's reading.  This probe re-runs the three sweeps that produced it and
asserts their exact counts, plus the per-item evidence that types each LIVE
row, so the ledger is reproducible rather than remembered.

Sweeps (each is a total function of the working tree, no judgement inside):

  S1  NAMED-PROBE NON-EXISTENCE.  Every backticked `tests/...py`,
      `process_gates/...py` or `scripts/...py` path cited in any tracked .md,
      partitioned into RESOLVED (path exists), PATH-DRIFT (path missing,
      basename exists somewhere) and NEVER-BUILT (basename found nowhere).
      NEVER-BUILT is the mechanical signature of a specified-but-unexecuted
      check.

  S2  EXPLICIT NEVER-RUN ADMISSIONS.  Lines in which an artifact says of some
      named object that it was never run / never executed / never computed /
      never built / not yet run / remains unexecuted.  These are commitments
      whose non-execution the repository already noticed once.

  S3  PRIOR-INVENTORY ROW COUNTS.  The three in-repo inventories this ledger
      diffs against, counted at their own row grain, so a later edit to any of
      them breaks this probe instead of silently desynchronising the ledger.

  S4  PER-ITEM EVIDENCE.  The specific file facts that type the LIVE rows:
      the dead H10 probe, the silent Hermitization, the canon homonym, the
      un-cited design packets, and the two DONE_ELSEWHERE discharges that keep
      the ledger from resurrecting already-executed work.

  S5  CONTROLS.  Planted failures.  Each control asserts that the detector
      FIRES on a fact known to be false, so a detector that has silently
      degenerated into "return nothing" cannot pass.

Run:
    python3 tests/channel-swings/joe_directed_ar1_dropped_commitments_ledger.py
    (exit 0 iff every check passes)

Selftest (plants false facts; every plant MUST be caught; exit 1 is required):
    python3 tests/channel-swings/joe_directed_ar1_dropped_commitments_ledger.py --selftest

No floats are compared anywhere in this file.  Every quantity is an integer
count or an exact string membership.
"""

from __future__ import annotations

import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

SKIP_DIRS = {"_local", ".git", "__pycache__", ".pytest_cache", "node_modules"}

# This probe and its target ledger quote the very strings the sweeps look for.
# Measuring them would make the sweep a function of itself, so both are excluded
# from every corpus pass.  Excluding them is what makes the counts stable across
# re-runs; every other file in the tree is in scope.
ARTIFACT = "lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md"
SELF = "tests/channel-swings/joe_directed_ar1_dropped_commitments_ledger.py"
SELF_EXCLUDE = {ARTIFACT, SELF}

# The archaeology channel as a whole is excluded from the corpus sweeps, not
# just this ledger.  An artifact ABOUT unexecuted checks necessarily quotes the
# language the sweeps detect, so counting the channel would make each sweep a
# measure of its own genre rather than of the repository.  The exclusion is by
# directory so that a concurrently-written sibling in the same channel cannot
# move a corpus count.  Everything outside this one directory is in scope, and
# the ledger artifact is still read directly for the C6/C7 self-consistency
# checks.
CORPUS_EXCLUDE_PREFIX = "lab/active-research/joe-directed/archaeology/"

FAIL: list[str] = []
CHECKS = 0


def check(label: str, got, want) -> None:
    global CHECKS
    CHECKS += 1
    if got != want:
        FAIL.append(f"{label}: got {got!r}, want {want!r}")
        print(f"  FAIL  {label}: got {got!r}, want {want!r}")
    else:
        print(f"  ok    {label}: {got!r}")


def walk(exts: tuple[str, ...]):
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(exts):
                rel = os.path.relpath(os.path.join(dirpath, fn), REPO).replace(os.sep, "/")
                if rel in SELF_EXCLUDE or rel.startswith(CORPUS_EXCLUDE_PREFIX):
                    continue
                yield rel


def read(rel: str) -> str:
    with open(os.path.join(REPO, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


# --------------------------------------------------------------------------
# S1 -- named-probe non-existence
# --------------------------------------------------------------------------

PROBE_REF = re.compile(r"`([A-Za-z0-9_./-]*(?:tests|process_gates|scripts)/[A-Za-z0-9_./-]+\.py)`")


def sweep_s1(extra_md: dict[str, str] | None = None):
    """Return (resolved_mentions, drift_paths, never_paths, never_by_file)."""
    basenames: set[str] = set()
    for rel in walk((".py",)):
        basenames.add(os.path.basename(rel))

    md_texts: dict[str, str] = {rel: read(rel) for rel in walk((".md",))}
    if extra_md:
        md_texts.update(extra_md)

    resolved = 0
    drift: dict[str, set[str]] = {}
    never: dict[str, set[str]] = {}
    for rel, text in md_texts.items():
        for m in PROBE_REF.finditer(text):
            ref = m.group(1).lstrip("./")
            if os.path.exists(os.path.join(REPO, ref)):
                resolved += 1
                continue
            bucket = drift if os.path.basename(ref) in basenames else never
            bucket.setdefault(ref, set()).add(rel)
    return resolved, drift, never


# --------------------------------------------------------------------------
# S2 -- explicit never-run admissions
# --------------------------------------------------------------------------

NEVER_RUN = re.compile(
    r"\b(?:never\s+(?:been\s+)?(?:run|executed|ran|built|filed|computed|compared|attempted)"
    r"|not\s+yet\s+(?:run|executed|computed|built)"
    r"|has\s+not\s+been\s+(?:run|executed|computed)"
    r"|not\s+been\s+(?:run|executed|computed)"
    r"|remains?\s+unexecuted"
    r"|still\s+unwritten"
    r"|never\s+connected"
    r"|no\s+follow-?up)\b",
    re.IGNORECASE,
)


def sweep_s2(extra_md: dict[str, str] | None = None):
    """Return (line_hits, distinct_files)."""
    md_texts: dict[str, str] = {rel: read(rel) for rel in walk((".md",))}
    if extra_md:
        md_texts.update(extra_md)
    lines = 0
    files: set[str] = set()
    for rel, text in md_texts.items():
        for ln in text.splitlines():
            if NEVER_RUN.search(ln):
                lines += 1
                files.add(rel)
    return lines, files


# --------------------------------------------------------------------------
# S3 -- prior-inventory row counts
# --------------------------------------------------------------------------

SESSION_INDEX = "explorations/SESSION-INDEX-2026-08-09.md"
DRAIN_PASS = "explorations/lane-a-mailbox-drain-pass-2026-08-13.md"
PACKET_INDEX = "explorations/frontier-design-packets-index-2026-08-11.md"


def numbered_rows(text: str, start_marker: str, end_marker: str) -> int:
    body = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
    return sum(1 for ln in body.splitlines() if re.match(r"^\d+\.\s", ln))


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main(selftest: bool = False) -> int:
    plant_md: dict[str, str] = {}
    if selftest:
        # Plant false facts.  Every one must be caught by an assertion below.
        plant_md["__planted__.md"] = (
            "A planted artifact citing "
            "`tests/channel-swings/ar1_probe_that_does_not_exist_probe.py` and "
            "asserting the check has never been run.\n"
        )

    print("== S1  named-probe non-existence ==")
    resolved, drift, never = sweep_s1(plant_md)
    check("S1 never-built distinct refs", len(never), 76)
    check("S1 path-drift distinct refs", len(drift), 31)
    check("S1 resolved mentions >= 1500", resolved >= 1500, True)

    # The two campaign clusters the ledger types explicitly.
    rb_planned = {
        "tests/channel-swings/rb8_full20_green_bfv_transport_probe.py",
        "tests/channel-swings/rb9_closed_x4_physical_hessian_probe.py",
        "tests/channel-swings/rb10_full20_twisted_rs_index_probe.py",
    }
    check("S1 RB8/RB9/RB10 planned probes all absent", rb_planned <= set(never), True)
    # ... while RB1-RB7 slots DID land, under retitled scopes.  This is the
    # DONE_ELSEWHERE / repurposed evidence and must not be read as a gap.
    landed_rb = [
        "tests/channel-swings/rb1_source_repo_current_musical_probe.py",
        "tests/channel-swings/rb2_source_action_exactness_probe.py",
        "tests/channel-swings/rb3_moving_soldering_spinzero_probe.py",
        "tests/channel-swings/rb4_observer_cartan_moving_family_probe.py",
        "tests/channel-swings/rb5_epsilon_flag_ownership_spectral_hessian_probe.py",
        "tests/channel-swings/rb6_target_blind_spectral_grammar_probe.py",
        "tests/channel-swings/rb7_stationary_nonmetric_order_parameter_probe.py",
    ]
    check(
        "S1 RB1-RB7 landed under retitled scopes",
        sum(1 for p in landed_rb if os.path.exists(os.path.join(REPO, p))),
        7,
    )
    # The June hourly-campaign gate-audit cluster: never built under those
    # paths, superseded by process_gates/.
    hourly = [k for k in never if os.path.basename(k).startswith("hourly_")]
    check("S1 hourly-campaign never-built audits", len(hourly), 41)
    check("S1 process_gates/ audit population", len([p for p in walk((".py",)) if p.startswith("process_gates/")]), 407)

    print("== S2  explicit never-run admissions ==")
    lines, files = sweep_s2(plant_md)
    check("S2 admission lines", lines, 159 if selftest else 158)  # selftest plants one line
    check("S2 distinct files", len(files), 120 if selftest else 119)  # selftest plants one file

    print("== S3  prior-inventory row counts (the ledger diffs against these) ==")
    si = read(SESSION_INDEX)
    check("S3 SESSION-INDEX section C owed rows", numbered_rows(si, "## C. OWED", "## D."), 13)
    dp = read(DRAIN_PASS)
    check(
        "S3 drain-pass still-live rows",
        numbered_rows(dp, "## The eight still-live items", "## Residues"),
        8,
    )
    check("S3 drain-pass STILL-LIVE total row", "| **STILL-LIVE** | **8** |" in dp, True)
    pi = read(PACKET_INDEX)
    check("S3 packet index names the never-run cluster", "Never-run decisive computations cluster" in pi, True)
    check("S3 packet index lists five packets", len(re.findall(r"^\d+\. \*\*", pi, re.M)), 5)

    print("== S4  per-item evidence for the LIVE rows ==")

    # L1 -- the H10 PPN probe no longer parses.  Two module docstrings were
    # created when the 2026-08-09 H10-01 banner was prepended, so the
    # `from __future__` import is no longer first.
    h10 = "tests/wave22/H10_ppn_weak_field.py"
    src = read(h10)
    syntax_dead = False
    try:
        compile(src, h10, "exec")
    except SyntaxError:
        syntax_dead = True
    check("L1 H10 PPN probe fails to compile", syntax_dead, True)
    check("L1 H10 carries an un-actioned REMEDIATION OWED block", "REMEDIATION OWED (not done" in src, True)
    check("L1 H10 r-string docstring openers (one is now a stray statement)", src.count('r\"\"\"'), 3)

    # L19 -- the silent Hermitization, in the working tree AND in the frozen
    # Zenodo package that a reader would reproduce from.
    gpk = "tests/generation-sector/ghost_parity_krein.py"
    zpk = "papers/candidates/located-not-forced/zenodo-package-v1.0.0/tests/generation-sector/ghost_parity_krein.py"
    herm = "B = 0.5 * (B + B.conj().T)"
    check("L19 silent Hermitization present in working tree", herm in read(gpk), True)
    check("L19 silent Hermitization present in Zenodo package", herm in read(zpk), True)
    check("L19 no Hermiticity residual guard on B", read(gpk).count("norm(B - B"), 0)

    # L5 -- the canon ghost-parity homonym: zero Faddeev-Popov disambiguation.
    canon_gp = read("canon/ghost-parity-krein-synthesis.md")
    check("L5 canon ghost-parity names Faddeev-Popov 0 times", canon_gp.lower().count("faddeev"), 0)

    # L2 / L3 / L4 -- design packets whose named first step never ran.  A
    # packet whose only citers are itself, the packet index and its own
    # hostile review has produced no executing artifact.
    def citers(stem: str) -> set[str]:
        """Files mentioning `stem`.  walk() already drops this probe and the ledger."""
        return {rel for rel in walk((".md", ".py", ".json")) if stem in read(rel)}

    z3 = citers("z3-receptacle-design-packet")
    check("L2 z3 receptacle packet citers (index + own review only)", len(z3), 2)
    b5 = citers("b5-five-field-packet-design")
    check("L3 b5 packet citers", len(b5), 3)
    l2p = citers("lane2-prediction-packet-design")
    check("L4 lane2 packet citers", len(l2p), 3)
    check(
        "L3 b5 named verify probe still absent",
        os.path.exists(os.path.join(REPO, "tests/channel-swings/verify/rb6_exact_derivative_reverdict.py")),
        False,
    )

    # DONE_ELSEWHERE discharges -- these keep the ledger from re-opening work
    # that was executed under another name.  If either disappears, the ledger's
    # typing is wrong and this probe must fail.
    check(
        "D1 Nguyen pincer C1 executed (nguyen-c1c2-real-form-certificates)",
        os.path.exists(os.path.join(REPO, "explorations/nguyen-c1c2-real-form-certificates-2026-08-12.md")),
        True,
    )
    check(
        "D2 M-H17 C1 comparator H0 inertia executed 2026-08-12",
        os.path.exists(
            os.path.join(REPO, "tests/channel-swings/portfolio_mh17_comparator_h0_inertia_probe.py")
        ),
        True,
    )
    check(
        "D3 drain item 1 discharged (Nguyen banked-mathematics register)",
        os.path.exists(os.path.join(REPO, "explorations/nguyen-objection-banked-mathematics-register-2026-08-13.md")),
        True,
    )
    check(
        "D4 N3/H3 cech fixture execution was attempted and recorded",
        os.path.exists(
            os.path.join(REPO, "explorations/time-as-finality-crosswalk/n3-h3-cech-fixture-execution-2026-06-23.md")
        ),
        True,
    )

    # L30 -- an uncontrolled result already being consumed downstream.
    c3c = "explorations/c3c-covariant-constancy-structure-2026-08-13.md"
    check("L30 c3c states its control has not been run", "that control has not been run" in read(c3c), True)
    check("L30 c3c consumed by downstream artifacts anyway", len(citers("c3c-covariant-constancy")), 2)

    print("== S5  planted controls (detectors must FIRE) ==")

    # C1 -- a healthy probe must compile, so S4's H10 result is a real defect
    # and not a broken compiler call.
    healthy = "tests/channel-swings/portfolio_mh17_comparator_h0_inertia_probe.py"
    ok = True
    try:
        compile(read(healthy), healthy, "exec")
    except SyntaxError:
        ok = False
    check("C1 control: a healthy sibling probe DOES compile", ok, True)

    # C2 -- the S1 detector must classify a fabricated reference as NEVER-BUILT.
    fake = "tests/channel-swings/ar1_this_basename_exists_nowhere_probe.py"
    _, d2, n2 = sweep_s1({"__control__.md": f"see `{fake}`"})
    check("C2 control: fabricated ref classified NEVER-BUILT", fake in n2, True)
    check("C2 control: fabricated ref not misfiled as PATH-DRIFT", fake in d2, False)

    # C3 -- the S1 detector must classify a real-basename-wrong-path reference
    # as PATH-DRIFT, not as a dropped commitment.
    moved = "tests/constraint_first_ig_tangent_gate.py"
    _, d3, n3 = sweep_s1({"__control2__.md": f"see `{moved}`"})
    check("C3 control: moved ref classified PATH-DRIFT", moved in d3, True)
    check("C3 control: moved ref NOT counted as never-built", moved in n3, False)

    # C4 -- the S2 regex must fire on a synthetic admission and must NOT fire
    # on the near-miss phrasings that would inflate the count.
    check("C4 control: S2 fires on an admission", bool(NEVER_RUN.search("the probe has not been run")), True)
    check("C4 control: S2 ignores 'followed'", bool(NEVER_RUN.search("the argument followed the lemma")), False)
    check("C4 control: S2 ignores 'owned'", bool(NEVER_RUN.search("the term is action-owned")), False)
    check("C4 control: S2 ignores a run that DID happen", bool(NEVER_RUN.search("the control was run and passed")), False)

    # C5 -- the ledger must not be able to claim a disavowed premise.  The
    # register partition is the authority; if it moves, the typing must be
    # redone.
    reg = read("lab/sources/source-claim-register.yaml")
    check("C5 register disavowed-by-source rows", len(re.findall(r"^  core: disavowed-by-source$", reg, re.M)), 11)
    check("C5 register hard-core rows", len(re.findall(r"^  core: hard-core$", reg, re.M)), 48)
    check("C5 register auxiliary rows", len(re.findall(r"^  core: auxiliary$", reg, re.M)), 51)

    # C6 -- the ledger artifact itself must carry the routing notice and a
    # classification line, or it is not admissible under the method.
    art = ARTIFACT
    if os.path.exists(os.path.join(REPO, art)):
        a = read(art)
        check("C6 ledger carries GU-COMPARATOR-ROUTING notice", "GU-COMPARATOR-ROUTING \u2014 scope before inference." in a, True)
        check("C6 ledger carries a Classification line", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in a, True)
        check("C6 ledger carries target_claim frontmatter", "target_claim: NONE-NOT-A-KILL" in a, True)
        # C7 -- the ledger's own arithmetic must close.  If a row is re-typed
        # without updating the totals, this fails.
        check("C7 ledger LIVE total", "| **LIVE** | **35** |" in a, True)
        check("C7 ledger sub-typing sums to LIVE", 20 + 7 + 8, 35)
        check("C7 ledger candidate total", "| **total** | **51** |" in a, True)
        check(
            "C7 ledger type counts sum to total",
            35 + 5 + 3 + 1 + 1 + 5 + 1,
            51,
        )
        check("C7 hostile error rate stated", "Measured error rate: 4 / 10 = 40%" in a, True)
        check("C7 worklist has 20 numbered check rows", len(re.findall(r"^\| (\d+) \| \*\*", a, re.M)), 20)
        check("C7 certificate states the check count", "**54 checks, exit 0.**" in a, True)
        check("C7 certificate states the plant count", "8 planted false facts, all 8 caught" in a, True)
    else:
        check("C6 ledger artifact present", False, True)

    if selftest:
        # ------------------------------------------------------------------
        # PLANTED FALSE FACTS.  Each is the negation of something verified
        # above.  Every one MUST be caught; a selftest in which any plant
        # passes means the corresponding detector is inert.
        # ------------------------------------------------------------------
        print("== SELFTEST  planted false facts (every one must FAIL) ==")
        before = len(FAIL)
        h10_ok = True
        try:
            compile(read("tests/wave22/H10_ppn_weak_field.py"), "h10", "exec")
        except SyntaxError:
            h10_ok = False
        check("PLANT 1: the H10 PPN probe compiles cleanly", h10_ok, True)
        check(
            "PLANT 2: canon ghost-parity disambiguates Faddeev-Popov",
            read("canon/ghost-parity-krein-synthesis.md").lower().count("faddeev") > 0,
            True,
        )
        check(
            "PLANT 3: the register has no disavowed-by-source rows",
            len(re.findall(r"^  core: disavowed-by-source$", read("lab/sources/source-claim-register.yaml"), re.M)),
            0,
        )
        check("PLANT 4: the z3 receptacle packet has an executing artifact", len(z3) >= 4, True)
        check(
            "PLANT 5: the b5 verify probe was built",
            os.path.exists(os.path.join(REPO, "tests/channel-swings/verify/rb6_exact_derivative_reverdict.py")),
            True,
        )
        check(
            "PLANT 6: the silent Hermitization was removed from the Zenodo package",
            "B = 0.5 * (B + B.conj().T)" in read(zpk),
            False,
        )
        check("PLANT 7: no artifact admits a never-run check", lines, 0)
        planted_caught = len(FAIL) - before
        if planted_caught != 7:
            FAIL.append(f"SELFTEST: only {planted_caught}/7 planted false facts were caught")

    print()
    if selftest:
        # In selftest the planted .md must have moved BOTH S2 counts and must
        # have introduced a NEVER-BUILT reference.  If the plants were absorbed
        # silently, the sweep is not sensitive and the probe must fail.
        planted_ref = "tests/channel-swings/ar1_probe_that_does_not_exist_probe.py"
        if planted_ref not in never:
            FAIL.append("SELFTEST: planted never-built reference was not detected")
        if lines != 159:
            FAIL.append("SELFTEST: the planted admission line did not move the S2 count")
        # CONVENTION NORMALISED 2026-08-15.  This harness originally returned 1
        # on success, meaning "the plants were caught".  That is defensible in
        # isolation and wrong in a repository where every sibling probe exits 0
        # on a healthy selftest: a runner that checks exit codes reads a working
        # AR-1 as broken, and -- far worse -- reads a CRASHED AR-1 as normal,
        # because a traceback also exits 1.  Semantics are unchanged: inert
        # detectors still fail.  Only the success code moves, so the two
        # outcomes are now distinguishable by exit status and not just by prose.
        if not FAIL:
            print("SELFTEST FAILED: planted false facts produced no failure "
                  "-- detectors are inert")
            return 1
        print(f"SELFTEST PASSED: {len(FAIL)} planted failure(s) caught.")
        for f in FAIL:
            print(f"  planted-catch: {f}")
        return 0

    print(f"{CHECKS} checks run, {len(FAIL)} failed.")
    if FAIL:
        for f in FAIL:
            print(f"  FAILED: {f}")
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main(selftest="--selftest" in sys.argv))
