#!/usr/bin/env python3
"""The source writes signature pairs in the MIRROR of the repository's notation.

VERDICT on pass: NOTATION-MIRRORED__NO-CONVENTION-DIVERGENCE__DECLARED-BASE-ROUTE-FALSIFIED

WHAT THIS KILLS.  On 2026-08-08 a hostile review filed a candidate resolver for
SIGNATURE-AMBIENT -- "the declared-base route" -- resting on the observation that
the source declares the base as (1,3) in five places while the repository runs
(3,1).  THAT OBSERVATION WAS A NOTATIONAL ARTEFACT.  This certificate falsifies
the route.  The named_resolver field is retracted to NONE.

THE TEST, and it is not a judgement call.  The source states THREE signature
pairs for objects the repository computes independently
(lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md, timestamps
00:39:55-00:40:53 and 00:46:06-00:47:20):

    raw Lorentzian symmetric-matrix form        source (3,7)
    traceless sector (9-dim)                    source (3,6)
    after flipping the trace line               source (4,6)

Computed here from the same construction, counting POSITIVE eigenvalues first:

    raw Frobenius form  tr(A_i A_j)             repo   (7,3)
    traceless sector                            repo   (6,3)
    DeWitt form, lambda = 1/2                   repo   (6,4)

EXACT MIRRORS, three for three.  One coincidence is possible; three is not.

THE CONTROL THAT MAKES IT DECISIVE.  A sceptic would say the source simply
computes at a different base signature.  It cannot: every form here is EVEN in
A = g^{-1}B, so g -> -g leaves all three fixed, and permuting which axis is
timelike is a coordinate relabeling.  This certificate evaluates all three at
THREE different bases and gets bit-identical plus-first numbers each time.  The
source's pairs are therefore NOT reachable by any base sign choice.  The only
remaining explanation is notation: the source writes (negatives, positives).

WHAT FOLLOWS.

  * source horizontal "(1,3)" IS the repository's base  (3,1).  Same object.
  * source vertical   "(4,6)" IS the repository's fibre (6,4).  Same object.
  * source total      "(5,9)" IS the repository's total (9,5).  Same object.
  * THERE IS NO SOURCE/REPOSITORY CONVENTION DIVERGENCE.  The repository has
    been running the source's own convention all along.

AND A SHARPER CONSEQUENCE, WHICH IS THE REASON THIS FILE MATTERS.  The source's
own block arithmetic is CORRECT and lands on the repository's answer:

    (4,6) + (1,3) = (5,9)        in source notation
       == (6,4) + (3,1) = (9,5)  in repository notation

The step that does NOT follow from the source's own numbers is its ASSERTED
total (7,7).  Reaching (7,7) requires reading the horizontal block in the
OPPOSITE notation from the vertical block -- mixing the two conventions inside a
single sum.  The reinspection file already typed that step SOURCE-UNTYPED and
noted the arithmetic gives (5,9); what is new is the DIAGNOSIS of why.

PRESSURE ON A SETTLED ROW, FILED AND NOT ACTED ON.  REAL-CLIFFORD-FORM is
settled at Cl(7,7) = M128(R), "derived from Curt/Eric's exact source-typed
arithmetic rather than choosing it", with the highest measured fan-out in the
program.  If the source's arithmetic self-consistently yields (5,9) == (9,5),
then the (7,7) settlement rests on the source's ASSERTION rather than on its
arithmetic.  That is a real pressure on a settled row and it is recorded here.
IT IS NOT ACTED ON: unsettling the program's highest-fan-out row requires its
own review, and this certificate establishes a notation fact, not a disposition.
Note also that REAL-CLIFFORD-FORM asks which algebra THE SOURCE COMPUTES IN,
which the registry marks as distinct from the ambient signature -- so the
pressure is real but is not automatically decisive.
"""

from __future__ import annotations

import itertools
import unittest

import numpy as np

TOL = 1e-9

BASIS = []
for _i, _j in itertools.combinations_with_replacement(range(4), 2):
    _b = np.zeros((4, 4))
    _b[_i, _j] = _b[_j, _i] = 1.0
    BASIS.append(((_i, _j), _b))

# What the source states, as transcribed in the reinspection note.
SOURCE_RAW = (3, 7)
SOURCE_TRACELESS = (3, 6)
SOURCE_FLIPPED = (4, 6)


def forms(g: np.ndarray):
    """Raw Frobenius form, its traceless restriction, and the DeWitt form."""
    gi = np.linalg.inv(g)
    a = [gi @ b for _, b in BASIS]
    raw = np.array([[np.trace(a[i] @ a[j]) for j in range(10)] for i in range(10)])
    dewitt = np.array([[np.trace(a[i] @ a[j]) - 0.5 * np.trace(a[i]) * np.trace(a[j])
                        for j in range(10)] for i in range(10)])
    trace_row = np.array([[np.trace(a[k]) for k in range(10)]])
    traceless = np.linalg.svd(trace_row)[2][1:]        # 9-dim complement
    return raw, traceless @ raw @ traceless.T, dewitt


def signature(m: np.ndarray) -> tuple[int, int]:
    """(positives, negatives) -- PLUS-FIRST, the repository's convention."""
    e = np.linalg.eigvalsh((m + m.T) / 2)
    return int((e > TOL).sum()), int((e < -TOL).sum())


def mirror(s: tuple[int, int]) -> tuple[int, int]:
    return s[1], s[0]


BASES = [
    ("3 plus / 1 minus", np.diag([1.0, 1.0, 1.0, -1.0])),
    ("1 plus / 3 minus", np.diag([1.0, -1.0, -1.0, -1.0])),
    ("all signs negated", np.diag([-1.0, -1.0, -1.0, 1.0])),
]


class SourceNotationIsMirrored(unittest.TestCase):

    def test_1_three_stated_pairs_are_exact_mirrors(self) -> None:
        raw, traceless, dewitt = forms(BASES[0][1])
        got = [signature(raw), signature(traceless), signature(dewitt)]
        said = [SOURCE_RAW, SOURCE_TRACELESS, SOURCE_FLIPPED]
        labels = ["raw Frobenius form", "traceless sector (9-dim)", "trace-flipped (DeWitt)"]
        print("\n[1] the source's three stated pairs vs the repository's computation")
        print(f"    {'object':26} {'source':8} {'repo':8}  mirror?")
        for label, s, r in zip(labels, said, got):
            print(f"    {label:26} {str(s):8} {str(r):8}  {mirror(s) == r}")
            self.assertEqual(mirror(s), r,
                             f"{label}: source pair is not the mirror of the computed one")
        print("    three for three. One coincidence is possible; three is not.")

    def test_2_no_base_sign_choice_reproduces_the_source_numbers(self) -> None:
        print("\n[2] the control -- could the source just be at a different base?")
        print(f"    {'base':20} {'raw':8} {'traceless':10} {'DeWitt':8}")
        reference = None
        for name, g in BASES:
            raw, traceless, dewitt = forms(g)
            trio = (signature(raw), signature(traceless), signature(dewitt))
            print(f"    {name:20} {str(trio[0]):8} {str(trio[1]):10} {str(trio[2]):8}")
            if reference is None:
                reference = trio
            self.assertEqual(trio, reference,
                             "the three forms must be independent of the base sign")
        self.assertEqual(reference, ((7, 3), (6, 3), (6, 4)))
        for stated in (SOURCE_RAW, SOURCE_TRACELESS, SOURCE_FLIPPED):
            self.assertNotIn(stated, reference,
                             "a source pair was reproduced by a base choice -- "
                             "the notation argument would then not be forced")
        print("    identical at every base: every form is EVEN in A = g^-1 B.")
        print("    => the source's pairs are NOT reachable by any base sign choice.")
        print("       The only remaining explanation is mirrored notation.")

    def test_3_the_divergence_dissolves_and_the_route_dies(self) -> None:
        print("\n[3] what the mirror does to the 'declared-base route'")
        pairs = [("horizontal", (1, 3), (3, 1)),
                 ("vertical", (4, 6), (6, 4)),
                 ("total", (5, 9), (9, 5))]
        for what, src, repo in pairs:
            print(f"    source {what:11} {str(src):7} == repo {str(repo):7}  SAME OBJECT")
            self.assertEqual(mirror(src), repo)
        print("\n    => there is NO source/repository convention divergence.")
        print("       The repository has been on the source's own convention throughout.")
        print("    => the DECLARED-BASE ROUTE filed as SIGNATURE-AMBIENT's")
        print("       named_resolver is FALSIFIED. It read a notational mirror as a")
        print("       substantive disagreement. Retracted to NONE.")

    def test_4_the_sources_own_arithmetic_lands_on_the_repository_answer(self) -> None:
        print("\n[4] the consequence that matters")
        src_sum = (4 + 1, 6 + 3)
        self.assertEqual(src_sum, (5, 9), "source blocks must sum to its spoken (5,9)")
        self.assertEqual(mirror(src_sum), (9, 5))
        print(f"    source blocks: (4,6) + (1,3) = {src_sum}   -- its own spoken arithmetic")
        print(f"    in repository notation that is {mirror(src_sum)}  -- the repository's answer")
        print("    So the source's arithmetic is CORRECT and agrees with the repo.")
        print("\n    The step that does NOT follow from the source's own numbers is its")
        print("    ASSERTED total (7,7). Reaching (7,7) needs the horizontal block read")
        print("    in the OPPOSITE notation from the vertical -- two conventions mixed")
        print("    inside one sum. The reinspection already typed that step")
        print("    SOURCE-UNTYPED; what is new is WHY it fails.")
        # (7,7) is not reachable from the source's own blocks in a single notation
        for horiz in [(1, 3), (3, 1)]:
            for vert in [(4, 6), (6, 4)]:
                total = (horiz[0] + vert[0], horiz[1] + vert[1])
                consistent = (horiz == (1, 3) and vert == (4, 6)) or \
                             (horiz == (3, 1) and vert == (6, 4))
                if consistent:
                    self.assertNotEqual(total, (7, 7),
                                        "a single-notation sum must not give (7,7)")
        print("    Verified: neither single-notation pairing sums to (7,7).")

    def test_5_pressure_on_a_settled_row_recorded_not_acted_on(self) -> None:
        print("\n[5] pressure on REAL-CLIFFORD-FORM -- RECORDED, NOT ACTED ON")
        print("    That row is SETTLED at Cl(7,7) = M128(R), 'derived from Curt/Eric's")
        print("    exact source-typed arithmetic rather than choosing it', and carries")
        print("    the highest measured fan-out in the program.")
        print("    If the source's arithmetic self-consistently yields (5,9) == (9,5),")
        print("    the (7,7) settlement rests on the source's ASSERTION, not on its")
        print("    arithmetic. That is a real pressure and it is filed.")
        print("\n    NOT ACTED ON, for two reasons:")
        print("      * unsettling the program's highest-fan-out row needs its own")
        print("        review; this certificate establishes a notation fact, not a")
        print("        disposition;")
        print("      * REAL-CLIFFORD-FORM asks which algebra THE SOURCE COMPUTES IN,")
        print("        which the registry marks DISTINCT from the ambient signature.")
        print("        The pressure is real but not automatically decisive.")
        print("\nVERDICT: NOTATION-MIRRORED__NO-CONVENTION-DIVERGENCE"
              "__DECLARED-BASE-ROUTE-FALSIFIED")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
