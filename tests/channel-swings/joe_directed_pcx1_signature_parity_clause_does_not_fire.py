#!/usr/bin/env python3
"""PCX-1 probe: does PD-SIGNATURE-PARITY's pre-declared invalidation clause
fire under HE-1's subtractive partition (observed 3 = n_g - 1)?

Certifies, against byte-verified owner text and exact integer arithmetic:

  1. The chain, punchline, evidence rows 6-7 and the invalidation clause are
     pinned verbatim in lab/process/path-dependencies.yaml (source of truth)
     and its generated .md.
  2. The constrained index (canon no-go) lives at the ambient GU-native
     Cl(9,5)-carrier layer; HE-1/HE-2's n_g -> n_g - 1 lives at the complex
     so(10) package/comparator layer with n_g an INPUT; CR-B places the chiral
     input for that comparator on the SG4-bit-2-conditional effective half
     only.  No receipt identifies the two indices (2026-08-08 hostile review,
     plus the NOT-lists of HE-1/HE-2/CR-B).
  3. Exact arithmetic at the package layer: observed 3 = 4 - 1 (SCUR-1's
     arithmetic is CORRECT at that layer); on (9,5) HE-2's uniform symplectic
     doubling keeps every raw multiplicity even before AND after the
     subtraction (2*4 = 8 -> 2*3 = 6), for every n_g.
  4. VERDICT (computed by an explicit firing evaluator over the grounded
     premises, not asserted): CLAUSE DOES NOT FIRE -- neither disjunct.
     Two contrary controls (a synthetic identification receipt; a synthetic
     outside-the-sector mechanism) each make the same evaluator FIRE, so the
     does-not-fire verdict is discriminating, not vacuous.

Selftest (--selftest): clean baseline FIRST, then six machinery/reference
corruptions (never check loosening), each required to produce a genuine
[FAIL] line and a red exit; a nonzero exit without a [FAIL] line is
CRASH-NOT-DETECTION and fails the selftest.  Selftest exits 0 on success.

Run from the repository root:
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_pcx1_signature_parity_clause_does_not_fire.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUTATION = os.environ.get("PCX1_MUTATION", "")

# ---------------------------------------------------------------- files table
FILES = {
    "yaml": "lab/process/path-dependencies.yaml",
    "md": "lab/process/path-dependencies.md",
    "nogo": "canon/no-go-quaternionic-parity-generation-sector.md",
    "he1": "lab/active-research/joe-directed/high-energy-two-plus-one/"
           "he1-imposter-separation-invariant-2026-08-14.md",
    "he2": "lab/active-research/joe-directed/high-energy-two-plus-one/"
           "he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md",
    "crb": "lab/active-research/joe-directed/carrier/"
           "crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md",
    "rev0808": "lab/process/hostile-reviews/"
               "2026-08-08-majorana-weyl-conditional-resolver-review.md",
    "scur1": "lab/active-research/joe-directed/source-currency/"
             "scur1-source-currency-audit-2026-08-17.md",
    "k134probe": "tests/channel-swings/"
                 "selected_k134_native_i1b_t0_kappa_hodge_fingerprint_and_fourier_pencil_probe.py",
}
if MUTATION == "M1":  # machinery corruption: path table redirect
    FILES["yaml"] = "lab/process/path-dependencies.DOES-NOT-EXIST.yaml"

# ------------------------------------------------------------- needle table
# (key, file-key, needle, expected occurrence count)
NEEDLES = [
    # --- the chain, its punchline, rows 6-7, the clause (YAML = source of truth)
    ("headline-forbids", "yaml", "(9,5) forbids an odd generation count", 1),
    ("headline-reach", "yaml", "A computation on the wrong horn cannot reach three.", 1),
    ("row6-kramers-even", "yaml",
     "Quaternionic structure forces Kramers doubling, hence EVEN multiplicity.", 1),
    ("row7-three-odd", "yaml",
     "Three generations is ODD. So (9,5) structurally forbids the target; (7,7) permits it.", 1),
    ("clause-disjunct-a", "yaml",
     "The generation count is shown NOT to be the index whose parity Kramers", 1),
    ("clause-disjunct-b", "yaml", "supplies the odd '+1' outside the Kramers-", 1),
    ("check-evidence-bar", "yaml", "not a mathematical settlement", 1),
    # --- generated .md carries the same clause and punchline
    ("md-clause-a", "md", "shown NOT to be the index whose parity Kramers constrains", 1),
    ("md-clause-b", "md", "outside the Kramers- constrained sector", 1),
    ("md-punchline", "md", "cannot reach three", 1),
    # --- canon no-go: what the constrained index IS, and its own conditionality
    ("nogo-even-index", "nogo",
     "GU's quaternionic structure forces an EVEN generation index.", 1),
    ("nogo-reading", "nogo",
     "Reading the generation count as the index of such a carrier, the count is forced", 1),
    ("nogo-underdetermined", "nogo",
     "GU neither forces nor forbids three generations; it under-determines the", 1),
    ("nogo-77-dissolves", "nogo", "It DISSOLVES under a defensible alternative", 1),
    ("nogo-foreign-import", "nogo",
     "reaching an odd index requires importing a non-quaternionic", 1),
    # --- HE-1: the subtraction, its layer, its fences
    ("he1-ng-input", "he1", "it does not derive `n_g`.", 1),
    ("he1-not-a-count", "he1", "no count\nhere is a generation count.", 1),
    ("he1-map", "he1", "chiral families plus one `144` leaves net chirality `n_g - 1`.", 1),
    ("he1-ng4-net3", "he1", "n_g = 4:  family blocks net  3", 1),
    ("he1-not-list", "he1",
     "NOT: an index, a generation count, a physical-carrier statement", 1),
    # --- HE-2: horn stability, uniform doubling, comparator rule
    ("he2-uniform-doubling", "he2", "doubles families and `144`s alike", 1),
    ("he2-table-95-col", "he2",
     "net chirality, n_g 16s + one 144    n_g - 1           n_g - 1                 n_g - 1", 1),
    ("he2-95-no-mw", "he2", "`(9,5)` admits none", 1),
    ("he2-smw", "he2", "requires symplectic doubling", 1),
    ("he2-comparator-rule", "he2", "a comparator result cannot advance a GU", 1),
    ("he2-not-list", "he2", "NOT: an index, a generation count, a physical carrier", 1),
    # --- CR-B: where the comparator has a chiral input, and the SG4 selector
    ("crb-no-chiral-input", "crb",
     "On the total declaration the conventional n_g comparator has no chiral input", 1),
    ("crb-sg4-unconstructed", "crb", "remains SG4 bit 2 and is not constructed here", 1),
    ("crb-not-list", "crb", "NOT: an index, a generation count, a physical carrier", 1),
    # --- 2026-08-08 hostile review: the identification was never settled true
    ("rev-no-receipt", "rev0808",
     "No listed receipt constructs the GU operator whose index is the observed family", 1),
    ("rev-link-does-not-fire", "rev0808", "the downstream link does not fire", 1),
    # --- SCUR-1: the watch this probe answers
    ("scur1-watch", "scur1",
     "plausibly fires the chain's own pre-declared invalidation clause", 1),
    ("scur1-crosscheck", "scur1", "run the HE-1 cross-check", 1),
    ("scur1-dissolve-arith", "scur1", "(9,5)-forbids-three conclusion", 1),
    # --- downstream byte-pin: the k134 probe requires the punchline string
    ("k134-pin", "k134probe", '"cannot reach three" in dependencies', 1),
]
if MUTATION == "M2":  # reference corruption: tamper one needle
    NEEDLES = [(k, f, n.replace("EVEN multiplicity", "ODD multiplicity"), c)
               for (k, f, n, c) in NEEDLES]
if MUTATION == "M6":  # reference corruption: blank a needle (guard must catch)
    NEEDLES = [(k, f, ("" if k == "row6-kramers-even" else n), c)
               for (k, f, n, c) in NEEDLES]

# --------------------------------------------------------- arithmetic engine
def net_chirality(n_g: int) -> int:
    """HE-1 section 3.6: n_g chiral 16s plus one 144 -> net n_g - 1 (package layer)."""
    return n_g - 1


def smw_raw(mult: int) -> int:
    """HE-2 section 3.3: on (9,5) the symplectic doubling is uniform (x2 raw)."""
    return 2 * mult


if MUTATION == "M3":
    def net_chirality(n_g: int) -> int:  # noqa: F811  (machinery corruption)
        return n_g
if MUTATION == "M4":
    def smw_raw(mult: int) -> int:  # noqa: F811  (machinery corruption)
        return 2 * mult + 1


def parity(n: int) -> str:
    return "EVEN" if n % 2 == 0 else "ODD"


# ------------------------------------------------------------ firing evaluator
def clause_fires(premises: dict) -> tuple[bool, list[str]]:
    """The clause's two disjuncts, evaluated over an explicit premise set.

    (a) fires iff a constructed receipt identifies the Kramers-constrained
        index and its value differs from the observed generation count
        ("is shown NOT to be the index whose parity Kramers constrains").
    (b) fires iff a CONSTRUCTED mechanism supplies an odd offset (+1 or -1)
        and is located OUTSIDE the Kramers-constrained sector.
    """
    fired = []
    receipt = premises.get("identification_receipt")
    if (receipt is not None and receipt.get("constructed")
            and receipt.get("constrained_index_value") != premises["observed_count"]):
        fired.append("a")
    mech = premises.get("mechanism")
    if (mech is not None and mech.get("constructed")
            and mech.get("location") == "outside"
            and mech.get("offset") in (1, -1)):
        fired.append("b")
    return (len(fired) > 0, fired)


# Live premises.  Each field is grounded in a byte-verified needle above:
#   identification_receipt = None   <- rev-no-receipt + he1/he2/crb NOT-lists
#                                      (no receipt constructs the operator
#                                      whose index is the observed count, and
#                                      none of HE-1/HE-2/CR-B claims an index,
#                                      a generation count or a physical carrier)
#   mechanism not constructed       <- crb-sg4-unconstructed (SG4 bit 2 open;
#                                      partner placement an obligation), and
#                                      located inside-or-unlocated on (9,5)
#                                      <- he2-uniform-doubling (families and
#                                      144s doubled alike inside the sector)
LIVE_PREMISES = {
    "observed_count": 3,
    "constrained_index_layer": "ambient-gu-native-carrier-Cl(9,5)",   # nogo-reading
    "subtraction_layer": "package-comparator-so10",                   # he1-ng-input
    "identification_receipt": None,
    "mechanism": {"constructed": False, "location": "inside-or-unlocated",
                  "offset": -1},
}
if MUTATION == "M5":  # machinery corruption: fabricate an identification receipt
    LIVE_PREMISES["identification_receipt"] = {
        "constructed": True, "constrained_index_value": 4}

# Contrary controls: configurations in which the clause PROVABLY FIRES, so the
# evaluator discriminates and the live DOES-NOT-FIRE is informative.
CONTROL_A_FIRES = {  # a constructed identification receipt: index = n_g = 4 != 3
    "observed_count": 3,
    "identification_receipt": {"constructed": True, "constrained_index_value": 4},
    "mechanism": None,
}
CONTROL_B_FIRES = {  # a constructed odd-offset mechanism outside the sector
    "observed_count": 3,
    "identification_receipt": None,
    "mechanism": {"constructed": True, "location": "outside", "offset": -1},
}

VERDICT_PIN = "DOES_NOT_FIRE"

# ------------------------------------------------------------------- harness
PASS = 0
FAIL = 0


def check(tag: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"[ok]   {tag}")
    else:
        FAIL += 1
        print(f"[FAIL] {tag}  {detail}")


def load(file_key: str) -> str:
    path = ROOT / FILES[file_key]
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def main() -> int:
    # -- needle guard: an empty or trivially short needle would vacuously pass
    for key, _fk, needle, _c in NEEDLES:
        check(f"guard:{key}", len(needle) >= 12,
              f"needle too short ({len(needle)} chars) -- vacuous match risk")

    # -- byte pins
    texts = {}
    for key, fk, needle, expected in NEEDLES:
        if fk not in texts:
            texts[fk] = load(fk)
            check(f"file:{fk}", bool(texts[fk]), f"missing/empty {FILES[fk]}")
        got = texts[fk].count(needle)
        check(f"pin:{key}", got == expected,
              f"count {got} != {expected} in {FILES[fk]}")

    # -- the chain's one CONDITIONAL row is row 7, inside this chain's span
    yaml_text = texts.get("yaml", "")
    lo = yaml_text.find("id: PD-SIGNATURE-PARITY")
    hi = yaml_text.find("id: PD-GHOST-PARITY")
    span = yaml_text[lo:hi] if (lo != -1 and hi != -1 and hi > lo) else ""
    check("span:chain-found", bool(span), "chain span not located in YAML")
    check("span:row7-conditional", span.count("evidence: CONDITIONAL") == 1,
          "row 7 is no longer the chain's single CONDITIONAL step")

    # -- exact arithmetic, package layer (SCUR-1's arithmetic, verified)
    check("arith:observed-3-needs-ng-4", net_chirality(4) == 3,
          f"net_chirality(4) = {net_chirality(4)}")
    check("arith:package-4-even", parity(4) == "EVEN")
    check("arith:identity-3-odd", parity(3) == "ODD")
    check("arith:he1-map-at-3", net_chirality(3) == 2,
          f"net_chirality(3) = {net_chirality(3)}")

    # -- exact arithmetic, (9,5) raw layer (HE-2 uniform doubling)
    check("arith:95-raw-before-even", smw_raw(4) == 8 and parity(smw_raw(4)) == "EVEN",
          f"smw_raw(4) = {smw_raw(4)}")
    check("arith:95-raw-after-even",
          smw_raw(net_chirality(4)) == 6 and parity(smw_raw(net_chirality(4))) == "EVEN",
          f"smw_raw(net) = {smw_raw(net_chirality(4))}")
    sweep_ok = all(parity(smw_raw(n)) == "EVEN"
                   and parity(smw_raw(net_chirality(n))) == "EVEN"
                   for n in range(1, 9))
    check("arith:95-subtraction-preserves-evenness-sweep", sweep_ok,
          "some n_g in 1..8 yields an odd (9,5) raw multiplicity")

    # -- firing evaluator: live verdict and contrary controls
    live_fired, live_which = clause_fires(LIVE_PREMISES)
    verdict = "FIRES" if live_fired else "DOES_NOT_FIRE"
    check("verdict:live", verdict == VERDICT_PIN,
          f"computed {verdict} (disjuncts {live_which}), pinned {VERDICT_PIN}")
    check("verdict:live-no-disjunct", live_which == [],
          f"live disjuncts: {live_which}")
    a_fired, a_which = clause_fires(CONTROL_A_FIRES)
    check("control:A-identification-fires", a_fired and a_which == ["a"],
          f"control A: fired={a_fired} which={a_which}")
    b_fired, b_which = clause_fires(CONTROL_B_FIRES)
    check("control:B-outside-mechanism-fires", b_fired and b_which == ["b"],
          f"control B: fired={b_fired} which={b_which}")

    # -- planted-false assertions: each must be observed False
    planted = [
        ("planted:net-is-identity", net_chirality(4) == 4),
        ("planted:three-is-even", parity(3) == "EVEN"),
        ("planted:95-raw-can-be-odd", smw_raw(3) % 2 == 1),
        ("planted:clause-fires-live", clause_fires(LIVE_PREMISES)[0]),
        ("planted:punchline-lives-in-canon-nogo",
         "A computation on the wrong horn cannot reach three." in texts.get("nogo", "")),
        ("planted:he1-ng4-nets-4",
         "n_g = 4:  family blocks net  4" in texts.get("he1", "")),
    ]
    for tag, value in planted:
        check(tag, value is False or value == False,  # noqa: E712
              f"planted-false observed {value!r}")

    print(f"\n{PASS}/{PASS + FAIL} checks"
          + ("" if FAIL == 0 else f"  ({FAIL} FAILED)"))
    if FAIL == 0:
        print("ALL CHECKS PASS -- verdict pinned: PD-SIGNATURE-PARITY invalidation "
              "clause DOES NOT FIRE under HE-1/HE-2/CR-B at their stated layers.")
        return 0
    return 1


# ------------------------------------------------------------------ selftest
MUTATIONS = {
    "M1": "path-table redirect: YAML pointed at a nonexistent file",
    "M2": "reference tamper: row-6 needle EVEN->ODD",
    "M3": "arithmetic engine: net_chirality drops the subtraction",
    "M4": "arithmetic engine: smw_raw breaks uniform doubling (2m+1)",
    "M5": "premise fabrication: a fake identification receipt is injected",
    "M6": "needle blanked: empty-needle guard must catch",
}


def selftest() -> int:
    me = str(Path(__file__).resolve())
    env0 = {k: v for k, v in os.environ.items() if k != "PCX1_MUTATION"}
    # 1) clean baseline FIRST -- a red baseline voids every mutation result.
    base = subprocess.run([sys.executable, me], cwd=str(ROOT), env=env0,
                          capture_output=True, text=True)
    if base.returncode != 0 or "ALL CHECKS PASS" not in base.stdout:
        print("[selftest FAIL] clean baseline is RED; aborting before mutations")
        print(base.stdout[-2000:])
        return 1
    print("[selftest] clean baseline verified FIRST: exit 0, all checks pass")
    # 2) each machinery corruption must produce a GENUINE catch.
    bad = 0
    for mut, desc in MUTATIONS.items():
        env = dict(env0, PCX1_MUTATION=mut)
        run = subprocess.run([sys.executable, me], cwd=str(ROOT), env=env,
                             capture_output=True, text=True)
        caught = run.returncode != 0 and "[FAIL]" in run.stdout
        crashed = "Traceback" in run.stderr
        if caught and not crashed:
            print(f"[selftest] {mut} CAUGHT via genuine [FAIL]  ({desc})")
        elif run.returncode != 0 and "[FAIL]" not in run.stdout:
            print(f"[selftest FAIL] {mut}: CRASH-NOT-DETECTION "
                  f"(red exit, no [FAIL] line)  ({desc})")
            bad += 1
        elif crashed:
            print(f"[selftest FAIL] {mut}: crash in harness  ({desc})")
            bad += 1
        else:
            print(f"[selftest FAIL] {mut}: NOT caught (exit 0)  ({desc})")
            bad += 1
    if bad == 0:
        print(f"[selftest] {len(MUTATIONS)}/{len(MUTATIONS)} mutations caught "
              "genuinely; selftest PASS (exit 0)")
        return 0
    print(f"[selftest] {bad} mutation(s) escaped or crashed; selftest FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
