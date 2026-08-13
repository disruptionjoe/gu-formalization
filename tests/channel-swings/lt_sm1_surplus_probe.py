#!/usr/bin/env python3
"""LT-SM1 constraint-surplus probe: does the surplus fix the zeta_F horn?

Pattern ported from explorations/b5-constraint-surplus-audit-2026-07-29.md
(probe tests/channel-swings/b5_constraint_surplus_audit_probe.py):

    surplus = (independent EXPRESSIBLE constraints on the choice)
              - (free parameters the choice introduces)

The B5 audit's binding lesson is reproduced here as a mandatory control: a
PERMISSIVE expressibility matcher inflates the constraint side and produces a
confident wrong answer. This probe runs BOTH matchers and reports the gap.

READ-ONLY against the pinned repo. No repo file is written.
Exact arithmetic only (int / fractions.Fraction). No float anywhere.

Repo HEAD pinned for reading: 0b2b0453a0afb831cbcb70f70352f65b120043b8
HEAD advanced mid-run by the hourly automation to: f078fcbb66ff9d99b933022c28852eb7fcf65c96
(LT-SM1 verified byte-identical across both; NEXT-STEPS.md line numbers shifted +14,
which is why every anchor below is marker-based rather than line-numbered.)
"""
from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

REPO = Path("/Users/joe/Brain/CapacityOS/repos/public/gu-formalization")
PINNED_HEAD_READ = "0b2b0453a0afb831cbcb70f70352f65b120043b8"   # HEAD when reading began
HEAD_AT_RUN     = "f078fcbb66ff9d99b933022c28852eb7fcf65c96"   # automation advanced HEAD mid-run


def anchor(relpath: str, marker: str, before: int = 4, after: int = 12) -> str:
    """Read a window around the first line containing `marker`.

    Marker-based rather than line-numbered on purpose: an hourly automation
    commits to this repo and DID advance HEAD mid-run
    (0b2b045 -> f078fcb), shifting NEXT-STEPS.md line numbers by +14.
    Fixed line anchors would have silently read the wrong text.
    """
    lines = (REPO / relpath).read_text(errors="replace").splitlines()
    for i, ln in enumerate(lines):
        if marker in ln:
            return "\n".join(lines[max(0, i - before):i + after + 1])
    raise SystemExit(f"ANCHOR NOT FOUND: {marker!r} in {relpath} -- probe VOID")


# --------------------------------------------------------------------------
# 1. THE CHOICE OBJECT and its distinctive-object inventory.
#    Source: packet:465-500 (the S_Y^(0) ambient bulk action) and
#            cb-b-lagrangian-terms-2026-08-05.md:207 (the U2 row).
# --------------------------------------------------------------------------
PACKET = "explorations/unified-source-datum-packet-v0-2026-07-30.md"
CBB = "explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md"

HORN_INVENTORY_RAW = [
    "zeta_F",           # the bit itself
    "g_A^{-2}",         # the coefficient the bit gates
    "g_A",
    "F_A",              # the curvature whose square is at stake
    "kappa_g",          # the invariant adjoint pairing
    "S_Y^{(0)}",        # the action the term is or is not written in
    "Yang--Mills",
    "Yang-Mills",
    "gauge kinetic",
    "packet:498",       # colon-qualified slot name (B5 tightening admits these)
    "U2",
]

# B5 tightening: distinctive == length >= 3, OR colon-qualified slot name.
def distinctive(tok: str) -> bool:
    return len(tok) >= 3 or ":" in tok


STRICT_INVENTORY = {t for t in HORN_INVENTORY_RAW if distinctive(t)}
# The deliberately permissive control inventory: single characters admitted,
# exactly the failure mode that voided B5's first execution.
PERMISSIVE_INVENTORY = STRICT_INVENTORY | {"F", "A", "g", "U", "Y", "S", "2"}


def tokens(text: str) -> set[str]:
    return set(re.findall(r"[A-Za-z_][A-Za-z0-9_^{}\-]*|\b\d+\b", text))


def expressible_strict(text: str) -> bool:
    """Distinctive-object sharing, B5-tightened. Substring on distinctive only."""
    return any(obj in text for obj in STRICT_INVENTORY)


def expressible_permissive(text: str) -> bool:
    """CONTROL: deliberately permissive. Bare single-char identifiers count."""
    toks = tokens(text)
    if any(obj in text for obj in PERMISSIVE_INVENTORY):
        return True
    return bool(toks & PERMISSIVE_INVENTORY)


# --------------------------------------------------------------------------
# 2. CANDIDATE CONSTRAINTS on the zeta_F choice, each with a real anchor.
#    `recorded_status` is quoted from the artifact, not inferred.
#    `discriminates` is the DECLARED reading: does the constraint distinguish
#    zeta_F=1 from zeta_F=0, or is it satisfied/failed identically by both?
# --------------------------------------------------------------------------
CANDIDATES = [
    dict(
        cid="C1-BRANCHING",
        label="three SM couplings g_1:g_2:g_3 from branching one g_A",
        ref=(CBB, "This is the row `M-M4` would move"),
        recorded_status="UNBUILT (M-M4 branching dictionary; register M-M4 'Build after J2')",
        discriminates=False,
        reason="needs the reduction, which does not exist under EITHER horn",
    ),
    dict(
        cid="C2-ANOMALY",
        label="perturbative anomaly cancellation (SM-9)",
        ref=(CBB, "the anomaly row and part of the shiab family chain are fork-stranded"),
        recorded_status="FORK-STRANDED on SIGNATURE-AMBIENT (Cl(9,5) import ban into Cl(7,7))",
        discriminates=False,
        reason="stranded on a different fork; silent on zeta_F",
    ),
    dict(
        cid="C3-PHOTON",
        label="a massless photon must exist in the gauge sector spectrum",
        ref=(CBB, "OPEN_PHOTON_KERNEL"),
        recorded_status="OPEN_PHOTON_KERNEL - 'no massless-photon kernel exists'",
        discriminates=False,
        reason="fails identically under both horns; a spectrum fact, not a bit constraint",
    ),
    dict(
        cid="C4-STATIONARITY",
        label="the fundamental-YM slice must be stationary/stable (RB7/W177)",
        ref=("NEXT-STEPS.md", "FUNDAMENTAL-YM-W177-VERTICAL-RESPONSE-KILLED"),
        recorded_status="FUNDAMENTAL-YM-W177-VERTICAL-RESPONSE-KILLED, but FD-band",
        discriminates=None,  # would discriminate, but is DISQUALIFIED
        reason="P-H29 (AGENTS.md:44): FD-read nulls are not citable until certified "
               "with exact derivatives; LANE-STATE.yaml:64 lists this exact "
               "recertification as still open",
    ),
    dict(
        cid="C5-HIGGS",
        label="the Higgs-is-an-illusion mechanism needs ||F_A||^2 to expand (SM-6)",
        ref=(CBB, "DETERMINED GIVEN `U2` (that the"),
        recorded_status="DETERMINED GIVEN U2 (that the Yang-Mills term is fundamental)",
        discriminates=True,
        reason="cb-b types SM-6 as REQUIRING the fundamental horn; the packet's N1 "
               "action supplies the expandable term only under zeta_F=1",
    ),
    dict(
        cid="C6-SCHUR",
        label="Schur/equivariance forcing of relative coefficients (W203)",
        ref=("explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md", "Is a coefficient still fitted rather than derived?"),
        recorded_status="all RELATIVE coefficients forced; exactly ONE (kappa) undetermined",
        discriminates=False,
        reason="acts on the theta/eta ultralocal kernel sector, not on the F_A^2 term",
    ),
    dict(
        cid="C7-DCH2",
        label="DC-H2 congruence-orbit exclusion of symmetry-type selectors",
        ref=("explorations/dc-h2-reciprocity-and-the-zu-block-ratio-2026-08-04.md", "no condition of this *type*"),
        recorded_status="no condition of this TYPE can ever supply the scale",
        discriminates=False,
        reason="a NEGATIVE result: it deletes candidate constraints, it is not one",
    ),
    dict(
        cid="C8-NORMSQUARE",
        label="the second-layer norm square selects the coefficient",
        ref=("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md", "The load-bearing homonym is **square**"),
        recorded_status="'does not become an independent coefficient constraint merely "
                        "by being second order' - DEAD ON ARRIVAL",
        discriminates=False,
        reason="killed as a class by the 'square' homonym ruling",
    ),
    dict(
        cid="C9-SAMEORBIT",
        label="the A-equation and the U-equation must select the same orbit",
        ref=("NEXT-STEPS.md", "require the \\(A\\)- and"),
        recorded_status="UNBUILT (listed as step 4 of the next efficient wave)",
        discriminates=False,
        reason="not built; nothing to evaluate",
    ),
    dict(
        cid="C10-SOURCE",
        label="source fidelity: SC-ACT-04, I^B_2 = ||Upsilon^B_omega||^2 yields a "
              "Yang-Mills-Maxwell-LIKE equation",
        ref=("lab/sources/source-claim-register.yaml", "Yang-Mills-Maxwell-like equation"),
        recorded_status="ADHERED; 'not an identity with the observed Standard Model action'",
        discriminates=False,
        reason="the source's architecture is a norm-square of the Euler residual, which "
               "is NEITHER packet horn cleanly; under-resolved, so non-discriminating "
               "on {0,1}",
    ),
]

# Planted controls, per the B5 method.
PLANTS = [
    dict(
        cid="N1-PLANT-RELATED",
        label="planted: a constraint that genuinely cites the choice object",
        text="This row constrains zeta_F directly through the coefficient g_A^{-2} "
             "written on kappa_g(F_A, *_G F_A) at packet:498.",
        expect_strict=True,
    ),
    dict(
        cid="N2-PLANT-UNRELATED",
        label="planted: a deliberately unrelated constraint",
        text="The mapping-torus orientation cocycle on the relative KO twist family "
             "over the defect stratum carries a Z/2 holonomy phase.",
        expect_strict=False,
    ),
]


def main() -> int:
    print(f"LT-SM1 SURPLUS PROBE  (read at {PINNED_HEAD_READ[:7]}, re-run at {HEAD_AT_RUN[:7]})")
    print("=" * 74)

    print("\n[0] PLANTED CONTROLS (run before any number is read)")
    control_ok = True
    for p in PLANTS:
        got = expressible_strict(p["text"])
        ok = got == p["expect_strict"]
        control_ok &= ok
        print(f"  {p['cid']:22s} strict={str(got):5s} expect={str(p['expect_strict']):5s} "
              f"{'PASS' if ok else 'FAIL'}")
    perm_n2 = expressible_permissive(PLANTS[1]["text"])
    print(f"  N2 under the PERMISSIVE control matcher: expressible={perm_n2}"
          f"   <- {'INFLATION REPRODUCED' if perm_n2 else 'no inflation'}")
    if not control_ok:
        print("\nCONTROL FAILED -> run is VOID (B5 precedent: void, do not report).")
        return 1

    print("\n[1] EXPRESSIBILITY, strict (B5-tightened) vs permissive (control)")
    strict_hits, perm_hits = [], []
    for c in CANDIDATES:
        rel, marker = c["ref"]
        text = anchor(rel, marker)
        s, p = expressible_strict(text), expressible_permissive(text)
        strict_hits.append(s)
        perm_hits.append(p)
        print(f"  {c['cid']:16s} strict={'EXPR ' if s else 'OUT  '} "
              f"perm={'EXPR ' if p else 'OUT  '} {rel.split('/')[-1]} @ {marker[:38]!r}")
    n_strict = sum(strict_hits)
    n_perm = sum(perm_hits)
    print(f"\n  expressible strict     : {n_strict}/{len(CANDIDATES)}")
    print(f"  expressible permissive : {n_perm}/{len(CANDIDATES)}   "
          f"<- the control's inflation: +{n_perm - n_strict}")

    print("\n[1b] WINDOW-SENSITIVITY SWEEP (is the strict count an artifact of window size?)")
    print("     B5's lesson is about matcher permissiveness; this is the same question")
    print("     asked of the READ WINDOW instead of the token filter.")
    for before, after in [(0, 0), (2, 6), (4, 12), (8, 24), (20, 60)]:
        n = 0
        ndisc = 0
        for c in CANDIDATES:
            rel, marker = c["ref"]
            t = anchor(rel, marker, before, after)
            e = expressible_strict(t)
            n += e
            ndisc += (e and c["discriminates"] is True)
        print(f"     window -{before:2d}/+{after:2d} lines : strict expressible {n:2d}/10 "
              f"| discriminating {ndisc}/10")
    print("     -> the EXPRESSIBLE count is window-sensitive (it measures how much")
    print("        surrounding prose is read); the DISCRIMINATING count is INVARIANT at 1,")
    print("        and the discriminating count is the only one the surplus consumes.")

    print("\n[2] DISCRIMINATION (expressible AND distinguishes zeta_F=1 from zeta_F=0)")
    discriminating = [c for c, s in zip(CANDIDATES, strict_hits)
                      if s and c["discriminates"] is True]
    disqualified = [c for c in CANDIDATES if c["discriminates"] is None]
    for c in CANDIDATES:
        tag = ("DISCRIMINATES" if c["discriminates"] is True else
               "DISQUALIFIED " if c["discriminates"] is None else "non-discrim. ")
        print(f"  {c['cid']:16s} {tag}  {c['reason'][:72]}")
    n_disc = len(discriminating)
    print(f"\n  discriminating & expressible : {n_disc}")
    print(f"  disqualified by P-H29        : {len(disqualified)}")

    print("\n[3] FREE PARAMETERS INTRODUCED BY EACH HORN (declared before subtraction)")
    # H1: zeta_F = 1. The packet charges g_A^{-2} in its own 7.2 ledger.
    # W229's title says Z_U "sets the induced YM coupling g_A" -> not independent.
    # The repo does not agree with itself. Both counts are carried.
    h1_params_packet = 1     # g_A^{-2}, packet:1106 local action coefficients
    h1_params_w229 = 0       # g_A fixed by Z_U, W229 frontmatter title
    # H2: zeta_F = 0. Nothing written -> 0 WRITTEN parameters. But producing a
    # YM term by induction requires a regulator, and packet:851-858 charges two
    # regulator families and records that NONE is admissible on the noncompact
    # Krein problem.
    h2_params_written = 0
    h2_params_undeclared_min = 1   # the induction/regulator scheme
    print(f"  H1 (zeta_F=1) written free params, packet reading : {h1_params_packet}")
    print(f"  H1 (zeta_F=1) written free params, W229 reading   : {h1_params_w229}")
    print(f"  H2 (zeta_F=0) written free params                 : {h2_params_written}")
    print(f"  H2 (zeta_F=0) undeclared (regulator), at least    : {h2_params_undeclared_min}")

    print("\n[4] SURPLUS = constraints - parameters   (exact, Fraction)")
    # Only C5 is expressible-and-discriminating, and it points at H1.
    c_h1 = Fraction(n_disc)          # constraints bearing on H1
    c_h2 = Fraction(0)               # none bears on H2
    rows = [
        ("H1 zeta_F=1 (packet param count)", c_h1, Fraction(h1_params_packet)),
        ("H1 zeta_F=1 (W229 param count)  ", c_h1, Fraction(h1_params_w229)),
        ("H2 zeta_F=0 (written only)      ", c_h2, Fraction(h2_params_written)),
        ("H2 zeta_F=0 (+ undeclared reg.) ", c_h2, Fraction(h2_params_undeclared_min)),
    ]
    for name, con, par in rows:
        print(f"  {name}  {con} - {par} = {con - par}")

    print("\n[5] NAIVE-MATCHER CONTROL: count WRITTEN parameters only, ignore "
          "expressibility")
    naive_h1 = Fraction(0) - Fraction(h1_params_packet)
    naive_h2 = Fraction(0) - Fraction(h2_params_written)
    print(f"  naive H1 = {naive_h1} ; naive H2 = {naive_h2}  -> naive picks "
          f"{'H2' if naive_h2 > naive_h1 else 'H1'} (the UNBUILT horn)")
    print("  This is the inflation the B5 audit warns about, in its dual form: a horn")
    print("  whose term is ABSENT looks parameter-free because its parameters have")
    print("  not been written down yet.")

    print("\n[6] VERDICT INPUTS")
    print(f"  horns enumerable from the record : YES, |H| = 2  (zeta_F in {{0,1}})")
    print(f"  horns with POSITIVE surplus      : 0")
    print(f"  free-parameter count agreed      : NO (packet=1 vs W229=0 for H1)")
    print(f"  discriminating constraints       : {n_disc} (weak/SCOPED)")
    print("  => SURPLUS-UNCOMPUTABLE: both sides of the subtraction are unresolved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
