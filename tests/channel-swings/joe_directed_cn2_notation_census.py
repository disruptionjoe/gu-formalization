# -*- coding: utf-8 -*-
"""
CN-2 -- the field-content notation census, and the arithmetic that makes the
notation consequential.

WHAT THIS PROBE IS FOR.  The repository writes GU's candidate-2B fermionic
content as ``nu in Omega^0(S)``, ``zeta in Omega^1(S)`` with the spinor bundle
UNSUBSCRIPTED.  Read naively -- as the SAME Weyl half in both slots -- that
names a Z/4 centre-class MIXED pairing, under which the ambient chirality tie
does not engage.  The source's spoken form is the OPPOSITE-half pairing
``Omega^0(S+) + Omega^1(S-)``, which is class-homogeneous.  So the shorthand can
carry an answer inside it.  This probe does three separable things:

  LEG 1  CENSUS.  Re-runs the notation sweep mechanically and asserts exact
         per-file occurrence counts, so the census is reproducible rather than
         remembered.

  LEG 2  REPAIR COVERAGE.  Asserts that every site CN-2 repaired now carries an
         explicit ``[CN-2 S-TYPING: <token>]`` declaration drawn from a CLOSED
         four-value vocabulary, and that canon carries NONE of them -- i.e. that
         canon was left alone, as the repository rule requires.

  LEG 3  INTEGRITY.  Asserts the SHA-pinned eq (9.16) verbatim block is
         byte-identical to what four unrelated probes string-match, so the
         repair was additive and broke nothing; and asserts the source and canon
         attestations the repair leans on are actually present at their loci.

  LEG 4  ARITHMETIC.  Independently recomputes the D_n centre-class invariant
         from scratch (exact integers, no import from the CR-B probe) and shows
         WHY the notation is consequential: both SAME-half pairings are
         class-mixed, both OPPOSITE-half pairings are class-homogeneous and odd,
         and the D_6 contrary control shows the protection genuinely failing in
         twelve dimensions.

WHAT THIS PROBE DOES NOT DO.  It does not decide which reading is GU's operative
content.  Nothing here asserts that GU is chiral, that it is not chiral, that
n_g is anything, or that any claim-register row moves.  The four-value token
vocabulary contains ``S-CHIRALITY-UNTYPED`` precisely so that a site can be
repaired by SAYING it is ambiguous rather than by being silently resolved.

CONCURRENCY NOTE.  The checkout is shared by several agents.  Repo-wide totals
are therefore PRINTED as a dated reconciliation and asserted only under
``--strict``; the load-bearing assertions are per-file and set-membership, which
are immune to another agent adding an unrelated file.

Exit 0 == every check passed.  ``--selftest`` plants false facts and requires
each to drive exit 1; the selftest itself exits 0 when all mutations are caught.
"""

from __future__ import annotations

import itertools
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

PASS = 0
FAIL = 0
PLANTED_OBSERVED_FALSE = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


def planted_false(name: str, cond: bool) -> None:
    """A predeclared FALSE assertion.  Observing it True means the instrument is
    not discriminating and is a hard failure."""
    global PLANTED_OBSERVED_FALSE, FAIL
    if cond:
        FAIL += 1
        print(f"  FAIL  planted-false assertion came back TRUE: {name}")
    else:
        PLANTED_OBSERVED_FALSE += 1


# --------------------------------------------------------------------------
# The sweep.  ONE regex pair, reused everywhere, so the census cannot drift
# between the artifact's prose and this file.
# --------------------------------------------------------------------------

UNSUB = re.compile(r"(?:\\?Omega|Ω)\s*\^\s*\{?[01]\}?\s*\(\s*(?:Y\s*\^?\d*\s*,\s*)?S\s*\)")
SUB = re.compile(r"(?:\\?Omega|Ω)\s*\^\s*\{?[01]\}?\s*\(\s*(?:Y\s*\^?\d*\s*,\s*)?S\s*[_^]?\s*[+−±-]")
TOKEN = re.compile(r"\[CN-2 S-TYPING: (S-FULL-DIRAC|S-HALF-OPPOSITE|S-HALF-SAME|S-CHIRALITY-UNTYPED)\]")

VOCABULARY = {"S-FULL-DIRAC", "S-HALF-OPPOSITE", "S-HALF-SAME", "S-CHIRALITY-UNTYPED"}

SWEEP_EXTENSIONS = {".md", ".yaml", ".yml", ".py", ".json", ".lean", ".txt"}
SWEEP_SKIP = {".git", ".lake", "_local", ".hypothesis", ".ruff_cache"}


SELF = pathlib.Path(__file__).resolve()


def sweep() -> dict[str, tuple[int, int, list[str]]]:
    out: dict[str, tuple[int, int, list[str]]] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in SWEEP_EXTENSIONS:
            continue
        if any(part in SWEEP_SKIP for part in path.parts):
            continue
        # The instrument is not a site.  This probe and the CN-2 artifact it
        # certifies both discuss the notation at length; counting them would
        # make the census self-referential.
        if path.resolve() == SELF or path.name.startswith("_cn2_mutant_tmp"):
            continue
        if path.as_posix().endswith("cn2-notation-carries-the-answer-2026-08-15.md"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        n_unsub = len(UNSUB.findall(text))
        n_sub = len(SUB.findall(text))
        tokens = TOKEN.findall(text)
        if n_unsub or n_sub or tokens:
            out[path.relative_to(ROOT).as_posix()] = (n_unsub, n_sub, tokens)
    return out


# --------------------------------------------------------------------------
# LEG 1/2 constants.  Recorded 2026-08-15 after the CN-2 repair pass.
# (unsubscripted occurrences, CN-2 tokens, token values)
# --------------------------------------------------------------------------

REPAIRED = {
    "docs/paper-formalization-candidates.md": (0, 2, ["S-CHIRALITY-UNTYPED"]),
    "explorations/README.md": (2, 1, ["S-CHIRALITY-UNTYPED"]),
    "explorations/b5-middle-source-freeze-2026-07-21.md": (4, 1, ["S-FULL-DIRAC"]),
    "explorations/conditional-build/selected-k77-zero-seed-h640-action-closure-controls-2026-08-11.md": (5, 1, ["S-FULL-DIRAC"]),
    "explorations/de-packet-lane-structure-clarification-2026-07-21.md": (2, 1, ["S-FULL-DIRAC"]),
    "explorations/eric-curt-wave3d-b2c2-null-clifford-omega1-completion-2026-07-31.md": (2, 1, ["S-CHIRALITY-UNTYPED"]),
    "explorations/eric-source-directed-native-closure-swing-2026-07-31.md": (2, 1, ["S-CHIRALITY-UNTYPED"]),
    "explorations/observation-to-family-b5-campaign-2026-07-20.md": (2, 1, ["S-CHIRALITY-UNTYPED"]),
    "lab/active-research/joe-directed/README.md": (2, 1, ["S-CHIRALITY-UNTYPED"]),
    "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md": (2, 1, ["S-CHIRALITY-UNTYPED"]),
    "lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md": (3, 1, ["S-CHIRALITY-UNTYPED"]),
    "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md": (2, 1, ["S-FULL-DIRAC"]),
    "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md": (4, 1, ["S-CHIRALITY-UNTYPED"]),
}

# canon/ is NOT CN-2's to rewrite.  These three are the canon sites the census
# found; the assertion is that they still read exactly as they did and carry
# ZERO CN-2 tokens.  (unsubscripted, subscripted, tokens)
CANON_LEFT_ALONE = {
    "canon/boundary-einvariant-and-the-tangential-fork.md": (1, 0, 0),
    "canon/source-action-seiberg-witten-construction.md": (2, 0, 0),
    "canon/escape-corners-campaign-RESULTS.md": (0, 2, 0),
}

# Ledger / predeclaration surfaces CN-2 deliberately did NOT touch.  Same rule.
NOT_MINE_TO_EDIT = {
    "NEXT-STEPS.md",
    "DERIVATION-PROGRESS.md",
    "tests/gu-forces/leg_a_forcing_enumeration.py",
    "tests/gu-forces/referee_leg_a_independent.py",
}

# The full census file set (files carrying the unsubscripted notation), recorded
# 2026-08-15.  Membership is asserted; other agents may legitimately add files,
# which are printed as UNCENSUSED rather than failing outside --strict.
CENSUS_FILES = 57
CENSUS_OCCURRENCES = 182


def leg1_and_2_census(found: dict[str, tuple[int, int, list[str]]]) -> None:
    print("\n[LEG 1] mechanical census")

    unsub_files = {k for k, v in found.items() if v[0]}
    total_unsub = sum(v[0] for v in found.values())
    total_sub = sum(v[1] for v in found.values())
    print(f"  unsubscripted: {total_unsub} occurrences in {len(unsub_files)} files")
    print(f"  subscripted:   {total_sub} occurrences in "
          f"{len({k for k, v in found.items() if v[1]})} files")

    for relative, (want_unsub, want_tokens, want_values) in sorted(REPAIRED.items()):
        got = found.get(relative)
        check(f"repaired site present: {relative}", got is not None)
        if got is None:
            continue
        check(f"exact unsubscripted count {want_unsub}: {relative}", got[0] == want_unsub)
        check(f"exact CN-2 token count {want_tokens}: {relative}", len(got[2]) == want_tokens)
        check(f"token values {want_values}: {relative}", sorted(set(got[2])) == sorted(set(want_values)))

    print("\n[LEG 2] repair coverage and the closed vocabulary")

    all_tokens = [t for v in found.values() for t in v[2]]
    check("every emitted token is in the closed four-value vocabulary",
          set(all_tokens) <= VOCABULARY)
    check("the vocabulary contains an explicit AMBIGUOUS value, so a site can be "
          "repaired without being resolved", "S-CHIRALITY-UNTYPED" in VOCABULARY)
    check("at least one site is typed AMBIGUOUS rather than resolved",
          "S-CHIRALITY-UNTYPED" in all_tokens)
    check("at least one site is typed S-FULL-DIRAC", "S-FULL-DIRAC" in all_tokens)
    check("NO site was silently typed to the protected half-pairing "
          "(that would be inventing a source commitment)",
          "S-HALF-OPPOSITE" not in all_tokens)
    check("NO site was typed to the same-half reading",
          "S-HALF-SAME" not in all_tokens)

    token_files = {k for k, v in found.items() if v[2]}
    check(f"exactly {len(REPAIRED)} files carry a CN-2 token",
          len(token_files) == len(REPAIRED))
    check("the token-carrying file set is exactly the repaired set",
          token_files == set(REPAIRED))

    print("\n[LEG 2b] canon and ledger surfaces left alone")
    for relative, (want_unsub, want_sub, want_tokens) in sorted(CANON_LEFT_ALONE.items()):
        got = found.get(relative, (0, 0, []))
        check(f"canon unchanged, unsubscripted={want_unsub}: {relative}", got[0] == want_unsub)
        check(f"canon unchanged, subscripted={want_sub}: {relative}", got[1] == want_sub)
        check(f"canon carries ZERO CN-2 tokens: {relative}", len(got[2]) == want_tokens)

    for relative in sorted(NOT_MINE_TO_EDIT):
        got = found.get(relative, (0, 0, []))
        check(f"ledger/predeclaration surface carries ZERO CN-2 tokens: {relative}",
              len(got[2]) == 0)

    uncensused = sorted(unsub_files - set(REPAIRED) - set(CANON_LEFT_ALONE) - NOT_MINE_TO_EDIT)
    print(f"  {len(uncensused)} further files carry the unsubscripted notation and were "
          f"LEFT AS FOUND (toy-arena, operator-domain, or verbatim-quote class)")

    if "--strict" in sys.argv:
        check(f"strict: repo-wide file count is {CENSUS_FILES}", len(unsub_files) == CENSUS_FILES)
        check(f"strict: repo-wide occurrence count is {CENSUS_OCCURRENCES}",
              total_unsub == CENSUS_OCCURRENCES)


# --------------------------------------------------------------------------
# LEG 3 -- integrity of what the repair leaned on.
# --------------------------------------------------------------------------

EQ916_VERBATIM = "nu, bar-nu     in Omega^0(Y,S)\nzeta, bar-zeta in Omega^1(Y,S)."

# The exact needles four unrelated probes string-match against the extraction.
FOREIGN_NEEDLES = (
    "nu, bar-nu     in Omega^0(Y,S)",
    "zeta, bar-zeta in Omega^1(Y,S)",
)

FOREIGN_PROBES = (
    "tests/channel-swings/selected_k77_source_owned_hull_interface_probe.py",
    "tests/channel-swings/selected_k77_h640_observation_pullback_bv_typing_probe.py",
    "tests/channel-swings/selected_k77_zero_seed_h640_action_closure_controls_probe.py",
    "tests/channel-swings/selected_k77_h640_ambient_observed_riccati_boundary_probe.py",
)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def leg3_integrity() -> None:
    print("\n[LEG 3] integrity -- the repair was additive, and its warrants are at their loci")

    extraction = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
    check("eq (9.16) verbatim block is byte-identical after the repair",
          EQ916_VERBATIM in extraction)
    for needle in FOREIGN_NEEDLES:
        check(f"foreign probe needle intact: {needle!r}", needle in extraction)
    for probe in FOREIGN_PROBES:
        body = read(probe)
        # Three match the padded needles; the riccati probe matches the bare
        # bundle names.  Both classes survive an additive repair; both are
        # asserted so a rewrite of the block would be caught either way.
        check(f"{pathlib.Path(probe).name} still matches on the extraction",
              any(n in body for n in FOREIGN_NEEDLES)
              or ('"Omega^0(Y,S)" in source' in body and '"Omega^1(Y,S)" in source' in body))
    check("the bare bundle names the riccati probe matches are intact",
          "Omega^0(Y,S)" in extraction and "Omega^1(Y,S)" in extraction)
    check("the extraction now SAYS the bundle is unsubscripted at the locus",
          "S` is UNSUBSCRIPTED at this locus" in extraction)
    check("the extraction records the four distinct fields that force the "
          "full-Dirac reading", "four distinct fields" in extraction)

    # The source's ONLY explicit spoken chirality declaration -- opposite halves.
    transcript = read("papers/drafts/Transcript into the impossible.md")
    check("L107 opposite-half declaration present verbatim in the transcript",
          "zero forms valued in the positive spinners" in transcript
          and "one forms valued in the negative spinners" in transcript)

    # Canon already refuted the SAME-half reading.  The repair cites this; if it
    # ever stops being true the repair's warrant is gone and this must fail.
    canon_ec = read("canon/escape-corners-campaign-RESULTS.md")
    check("canon records the A2 leg as REFUTED-AS-FILED", "A2 REFUTED-AS-FILED" in canon_ec)
    check("canon says the same-Weyl-half content is stated by NEITHER primary",
          "stated by NEITHER primary" in canon_ec)
    check("canon names the same-half pairing explicitly",
          "Omega^0(S+) + Omega^1(S+)" in canon_ec)
    check("canon quotes the draft's non-chiral section title",
          "Fundamentally Non-Chiral Theory" in canon_ec)

    # SC-CHI-01 -- the selector statement.  It must NOT presuppose a declared
    # chirality; it must say chirality is EMERGENT from a non-chiral total.
    register = read("lab/sources/source-claim-register.yaml")
    check("SC-CHI-01 is present in the register", "id: SC-CHI-01" in register)
    check("SC-CHI-01 predicates the split on a NON-chiral total theory, so it "
          "does not presuppose the same-half reading",
          "non-chiral total theory splits at the emergent level" in register)
    check("SC-CHI-01 records its VEV condition, which is the actual selector",
          "vacuum expectation value" in register)

    # SG4 bit 2 -- likewise a PHASE bit, not a content declaration.
    sg4 = read("canon/gu-forces-field-space-declaration-RESULTS.md")
    check("SG4 bit 2 is stated as a PHASE bit (chiral vs massive), not as a "
          "chirality assignment on the field content",
          "Bit 2 -- phase:" in sg4 and "chiral/unbroken vs massive/super-Higgs" in sg4)
    check("SG4's residual is 2 bits and neither is a chirality-of-S bit",
          "2-bit" in sg4 or "2 bits" in sg4 or "2-dimensional residual" in sg4)


# --------------------------------------------------------------------------
# LEG 4 -- why the distinction is consequential.  Independent exact arithmetic:
# the Z/4 grading of the D_n representation ring, built from weights, with NO
# import from any other probe.
# --------------------------------------------------------------------------

def half_spinor_weights(n: int, parity: int) -> list[tuple[int, ...]]:
    """Weights of the half-spinor of D_n in DOUBLED integer coordinates: all
    sign vectors (+-1)^n with an even (parity 0) or odd (parity 1) number of
    -1 entries.  Doubling clears the 1/2 and keeps the arithmetic in Z."""
    return [w for w in itertools.product((1, -1), repeat=n)
            if sum(1 for x in w if x == -1) % 2 == parity]


def vector_weights(n: int) -> list[tuple[int, ...]]:
    """Weights of the 2n-dimensional vector rep, doubled: +-2 e_i."""
    out = []
    for i in range(n):
        for sign in (2, -2):
            w = [0] * n
            w[i] = sign
            out.append(tuple(w))
    return out


def root_weights(n: int) -> list[tuple[int, ...]]:
    """D_n roots, doubled: +-2 e_i +- 2 e_j, i < j."""
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            for si in (2, -2):
                for sj in (2, -2):
                    w = [0] * n
                    w[i] = si
                    w[j] = sj
                    out.append(tuple(w))
    return out


def cls_of(weights: list[tuple[int, ...]]) -> int | None:
    """The centre class = doubled-coordinate-sum mod 4, defined only when every
    weight of the module agrees.  Returns None when the module is not
    class-homogeneous -- which is itself the load-bearing signal."""
    classes = {sum(w) % 4 for w in weights}
    return classes.pop() if len(classes) == 1 else None


def leg4_arithmetic() -> None:
    print("\n[LEG 4] the Z/4 centre-class arithmetic, recomputed from weights")

    # Well-definedness: the class map descends to P/Q only because every root
    # has doubled-coordinate sum 0 mod 4.
    for n in (4, 5, 6, 7):
        check(f"D_{n}: every root has doubled-coordinate sum 0 mod 4",
              all(sum(r) % 4 == 0 for r in root_weights(n)))

    n = 7  # Y^14 -> ambient D_7
    sp = half_spinor_weights(n, 0)
    sm = half_spinor_weights(n, 1)
    check("D_7 half-spinors have 64 weights each", len(sp) == 64 and len(sm) == 64)
    check("D_7 vector rep has 14 weights", len(vector_weights(n)) == 14)

    c_sp, c_sm, c_v = cls_of(sp), cls_of(sm), cls_of(vector_weights(n))
    check("cls(S^+) = 3", c_sp == 3)
    check("cls(S^-) = 1", c_sm == 1)
    check("cls(V) = 2", c_v == 2)
    check("cls(ad) = 0", cls_of(root_weights(n)) == 0)
    check("each half-spinor is class-HOMOGENEOUS (the class is a property of the "
          "module, not of a chosen weight)", c_sp is not None and c_sm is not None)

    # A 1-form valued in a module shifts the class by cls(V) = 2.
    def omega1(c: int) -> int:
        return (c + c_v) % 4

    pairings = {
        ("S+", "S+"): (c_sp, omega1(c_sp)),
        ("S+", "S-"): (c_sp, omega1(c_sm)),
        ("S-", "S+"): (c_sm, omega1(c_sp)),
        ("S-", "S-"): (c_sm, omega1(c_sm)),
    }
    homogeneous = {k: (a == b) for k, (a, b) in pairings.items()}
    print("      0-form | 1-form      classes    homogeneous  protected(odd)")
    for (a, b), (ca, cb) in pairings.items():
        hom = ca == cb
        print(f"      Omega^0({a}) | Omega^1({b})   ({ca},{cb})      "
              f"{str(hom):<12} {str(hom and ca % 2 == 1)}")

    check("SAME-half pairing (S+,S+) is class-MIXED", homogeneous[("S+", "S+")] is False)
    check("SAME-half pairing (S-,S-) is class-MIXED", homogeneous[("S-", "S-")] is False)
    check("OPPOSITE-half pairing (S+,S-) is class-HOMOGENEOUS", homogeneous[("S+", "S-")] is True)
    check("OPPOSITE-half pairing (S-,S+) is class-HOMOGENEOUS", homogeneous[("S-", "S+")] is True)
    check("exactly 2 of the 4 pairings are class-homogeneous",
          sum(homogeneous.values()) == 2)
    check("both class-homogeneous pairings carry ODD class, hence admit no "
          "invariant bilinear on M (x) M",
          all(pairings[k][0] % 2 == 1 for k, v in homogeneous.items() if v))
    check("the verdict is invariant under the global +/- relabelling, so no "
          "sign convention is load-bearing",
          homogeneous[("S+", "S-")] == homogeneous[("S-", "S+")]
          and homogeneous[("S+", "S+")] == homogeneous[("S-", "S-")])

    # THE POINT: reading one unsubscripted symbol as the same half twice lands
    # on a class-mixed pairing.  Reading it as the full Dirac bundle gives a
    # content carrying BOTH classes, which is likewise not homogeneous.
    full_dirac_classes = {c_sp, c_sm}
    check("the FULL Dirac bundle carries BOTH classes {1,3}, so the total "
          "declared content is not class-homogeneous either",
          full_dirac_classes == {1, 3})
    # Exercise the inhomogeneous branch directly: cls_of MUST refuse to return a
    # class for a module that does not have one.  Without this the instrument
    # could silently pick a representative and report protection that is not there.
    check("cls_of returns None on the full Dirac bundle S^+ (+) S^-, i.e. it "
          "REFUSES to assign a class to an inhomogeneous module",
          cls_of(sp + sm) is None)
    check("cls_of returns None on the class-MIXED same-half pairing content",
          cls_of(sp + [tuple(a + b for a, b in zip(w, v))
                       for w in sp for v in vector_weights(n)[:1]]) is None)
    check("odd class forbids a BARE invariant bilinear: cls(M (x) M) = 2 mod 4",
          (2 * c_sp) % 4 == 2 and (2 * c_sm) % 4 == 2)

    # CONTRARY CONTROL -- twelve dimensions, where the protection genuinely FAILS.
    c6 = cls_of(half_spinor_weights(6, 0))
    check("D_6 (TWELVE dimensions): cls(S^+) = 2, EVEN", c6 == 2)
    check("D_6: same-chirality invariant is ALLOWED -- the instrument can see "
          "the protection fail", (2 * c6) % 4 == 0)
    parity = {m: cls_of(half_spinor_weights(m, 0)) % 2 == 1 for m in (4, 5, 6, 7)}
    check("the mechanism is D_n rank parity {4:F, 5:T, 6:F, 7:T}, and nothing "
          "about signature",
          parity == {4: False, 5: True, 6: False, 7: True})

    # A second, independent leg on the same fact: -w_0 acts on the half-spinor
    # weight multiset by global negation, which swaps the halves iff n is odd.
    negated = {tuple(-x for x in w) for w in sp}
    check("D_7: -w_0 maps S^+ weights onto S^- weights (the halves are dual, "
          "not self-dual) -- second independent leg",
          negated == set(sm))
    sp6 = half_spinor_weights(6, 0)
    check("D_6: -w_0 preserves the S^+ weight multiset (self-dual) -- the same "
          "leg, returning the opposite verdict on the control",
          {tuple(-x for x in w) for w in sp6} == set(sp6))


# --------------------------------------------------------------------------
# Planted false assertions -- predeclared, each REQUIRED to come back False.
# --------------------------------------------------------------------------

def planted_controls(found: dict[str, tuple[int, int, list[str]]]) -> None:
    print("\n[CONTROLS] predeclared FALSE assertions, each required to be observed False")

    n = 7
    sp = half_spinor_weights(n, 0)
    sm = half_spinor_weights(n, 1)
    c_sp, c_sm, c_v = cls_of(sp), cls_of(sm), cls_of(vector_weights(n))

    planted_false("cls(S^+) == cls(S^-)", c_sp == c_sm)
    planted_false("cls(V) is odd", c_v % 2 == 1)
    planted_false("the same-half pairing is class-homogeneous",
                  c_sp == (c_sp + c_v) % 4)
    planted_false("the opposite-half pairing is class-MIXED",
                  c_sp != (c_sm + c_v) % 4)
    planted_false("all four pairings are homogeneous",
                  c_sp == (c_sp + c_v) % 4 and c_sp == (c_sm + c_v) % 4)
    planted_false("D_7 half-spinor is self-dual under -w_0",
                  {tuple(-x for x in w) for w in sp} == set(sp))
    planted_false("D_6 half-spinor has ODD class",
                  cls_of(half_spinor_weights(6, 0)) % 2 == 1)
    planted_false("the full Dirac bundle is class-homogeneous",
                  len({c_sp, c_sm}) == 1)
    planted_false("canon carries a CN-2 token",
                  any(found.get(k, (0, 0, []))[2] for k in CANON_LEFT_ALONE))
    planted_false("some site was typed S-HALF-OPPOSITE (a source commitment "
                  "CN-2 must not invent)",
                  any("S-HALF-OPPOSITE" in v[2] for v in found.values()))
    planted_false("some site was typed S-HALF-SAME",
                  any("S-HALF-SAME" in v[2] for v in found.values()))
    planted_false("the unsubscripted notation has been eliminated repo-wide",
                  sum(v[0] for v in found.values()) == 0)
    planted_false("NEXT-STEPS.md was edited by CN-2",
                  bool(found.get("NEXT-STEPS.md", (0, 0, []))[2]))


# --------------------------------------------------------------------------
# --selftest: mutate the machinery and require each mutant to drive exit 1.
# --------------------------------------------------------------------------

MUTATIONS = (
    ("class map mod 3 instead of mod 4", "sum(w) % 4", "sum(w) % 3"),
    ("class map without doubling", "return [w for w in itertools.product((1, -1), repeat=n)",
     "return [w for w in itertools.product((2, -2), repeat=n)"),
    ("vector weight sign flipped to +-1", "for sign in (2, -2):", "for sign in (1, -1):"),
    ("half-spinor parity filter inverted", "% 2 == parity", "% 2 != parity"),
    ("1-form class shift dropped", "return (c + c_v) % 4", "return c % 4"),
    ("1-form class shift set to 1", "return (c + c_v) % 4", "return (c + 1) % 4"),
    ("D_7 replaced by D_6 in the pairing table", "    n = 7  # Y^14", "    n = 6  # Y^14"),
    ("homogeneity test inverted", "homogeneous = {k: (a == b)", "homogeneous = {k: (a != b)"),
    ("cls_of ignores inhomogeneity", "return classes.pop() if len(classes) == 1 else None",
     "return sorted(classes)[0]"),
    ("token vocabulary opened up", 'VOCABULARY = {"S-FULL-DIRAC", "S-HALF-OPPOSITE", "S-HALF-SAME", "S-CHIRALITY-UNTYPED"}',
     'VOCABULARY = set()'),
    ("census regex stops seeing Y-qualified sites", r"(?:Y\s*\^?\d*\s*,\s*)?S\s*\)", r"S\s*\)"),
    ("canon exemption removed from the repaired set",
     '"lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md": (2, 1, ["S-FULL-DIRAC"]),',
     '"canon/escape-corners-campaign-RESULTS.md": (0, 1, ["S-FULL-DIRAC"]),'),
    ("eq (9.16) verbatim needle corrupted",
     'EQ916_VERBATIM = "nu, bar-nu     in Omega^0(Y,S)\\nzeta, bar-zeta in Omega^1(Y,S)."',
     'EQ916_VERBATIM = "nu, bar-nu in Omega^0(Y,S+)\\nzeta, bar-zeta in Omega^1(Y,S-)."'),
    # NOTE on mutation design: mutating an ASSERTION to something weaker
    # (e.g. `== 0` -> `>= 0`) is not a detectable mutation -- a vacuous check
    # still passes on true data.  Every mutation below therefore corrupts
    # MACHINERY, not a predicate, which is the only kind a probe can catch.
    ("root lattice corrupted so P/Q grading is no longer well defined",
     "                    w[j] = sj", "                    w[j] = sj + 1"),
    ("half-spinor weight count broken", "repeat=n)", "repeat=n - 1)"),
)


def selftest() -> int:
    source = pathlib.Path(__file__).read_text(encoding="utf-8")
    tmp = ROOT / "tests" / "channel-swings" / "_cn2_mutant_tmp.py"
    caught = 0
    for name, old, new in MUTATIONS:
        if old not in source:
            print(f"  MUTATION NOT APPLICABLE (needle missing): {name}")
            return 1
        tmp.write_text(source.replace(old, new, 1), encoding="utf-8")
        try:
            result = subprocess.run([sys.executable, str(tmp)], capture_output=True, text=True)
        finally:
            pass
        if result.returncode == 0:
            print(f"  NOT CAUGHT (mutant exited 0): {name}")
            tmp.unlink(missing_ok=True)
            return 1
        caught += 1
        print(f"  caught (exit {result.returncode}): {name}")
    tmp.unlink(missing_ok=True)
    print(f"\n--selftest: {caught}/{len(MUTATIONS)} injected mutations drove exit 1.")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        print("CN-2 notation census -- SELFTEST (planting false machinery)")
        return selftest()

    print("CN-2 -- field-content notation census, repair coverage, and the "
          "arithmetic that makes the distinction consequential")
    found = sweep()
    leg1_and_2_census(found)
    leg3_integrity()
    leg4_arithmetic()
    planted_controls(found)

    print(f"\n{PASS}/{PASS + FAIL} checks passed; "
          f"{PLANTED_OBSERVED_FALSE}/13 planted false assertions observed False.")
    if FAIL or PLANTED_OBSERVED_FALSE != 13:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS -- census reproduced, canon untouched, ambiguity preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
