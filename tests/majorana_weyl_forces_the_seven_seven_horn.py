#!/usr/bin/env python3
"""Majorana-Weyl forces (7,7): the split IS the reason, not a coincidence.

VERDICT on pass: MW-REQUIREMENT-FORCES-(7,7)__CONDITIONAL-RESOLVER-FOR-SIGNATURE-AMBIENT

THE CLAIM.  Given (a) GU's 4+10 split, (b) the metric fibre's signature (6,4),
and (c) a requirement that the ambient matter carrier be MAJORANA-WEYL, the
ambient signature is FORCED to (7,7).  There is no residual freedom.  The base
convention is then a CONSEQUENCE, not a convention.

WHY THIS MATTERS.  SIGNATURE-AMBIENT has been carried as "under-determined,
awaiting a resolver", and two proposed resolvers were falsified on 2026-08-08
(M-H9, and the declared-base route).  Both were attempts to READ the answer off
the source.  This one does not read the source at all; it derives the horn from
a carrier requirement plus a mod-8 fact.

THE THREE INPUTS, and each is independently established elsewhere.

  (a) 4 + 10.  GU's Y^14 = Met(X^4); the split is even/even and not in dispute.

  (b) FIBRE (6,4).  The DeWitt/trace-reversed Frobenius form on Sym^2(T*X) has
      signature (6,4) counting positives first.  Crucially this is INDEPENDENT OF
      THE BASE SIGN: G(-g) = G(g) exactly, certified at residual 0.00e+00 in
      tests/signature_fork_equivariance_defect.py.  So the fibre is a FIXED input
      and cannot be traded against the base.

  (c) MAJORANA-WEYL.  A real chiral spinor exists in signature (p,q) iff
      p - q = 0 mod 8 (Weyl needs even dimension; the Majorana reality condition
      is compatible with chirality only in that class).

THE DERIVATION.  With the fibre fixed at (6,4), the base contributes (3,1) or
(1,3), giving ambient (9,5) or (7,7).  Their classes are p-q = 4 and 0.  Only
p-q = 0 admits Majorana-Weyl.  Therefore (7,7), and therefore base (1,3).

WHAT IT IS AND IS NOT.  It is a CONDITIONAL resolver: the condition is (c), and
(c) is a requirement GU adopts rather than a theorem.  A quaternionic carrier on
(9,5) is mathematically available -- the repository built seven waves on one.
So this does not prove GU must be (7,7); it proves that ONE clearly stated
carrier requirement determines the horn completely.  That converts the row from
"undetermined convention" to "determined by a named condition", which is the
shape the ledger is built for.

NOT CIRCULAR, and the distinction is the whole point.  "GU uses the (7,7)
carrier, therefore (7,7)" would be circular.  The non-circular statement is:
GU requires a REAL chiral matter carrier -- motivated independently, and visible
in the draft's own printed real multiplicities (64+/64-, 832+/832-) -- and
reality plus chirality is a mod-8 condition that, against a fixed (6,4) fibre in
dimension 14, has exactly one solution.

CORROBORATION IN BOTH VOICES, neither of which is used as a premise above.
  * EXPOSITOR (Curt, iceberg ~00:41:27): the motivation for (7,7) is that "the
    split Spin(7,7) spinor has real dimension 128" and "admits the desired
    chiral/split presentation".  That is this theorem, stated informally.
  * AUTHOR (Weinstein, Portal 2020 02:42:20): the trace portion is "put in with
    the PROPER SIGN if you're trying to generate the sector that begins as
    X(1,3)", and Spin(6) x Spin(4) Pati-Salam becomes natural.  The proper sign
    is the one that lands on p - q = 0.
"""

from __future__ import annotations

import unittest

ABS_TABLE = {
    0: "M(R)", 1: "M(R)+M(R)", 2: "M(R)", 3: "M(C)",
    4: "M(H)", 5: "M(H)+M(H)", 6: "M(H)", 7: "M(C)",
}

DIM = 14
FIBRE = (6, 4)                      # certified base-sign independent
BASE_HORNS = {"(3,1)": (3, 1), "(1,3)": (1, 3)}


def clifford_class(p: int, q: int) -> str:
    return ABS_TABLE[(p - q) % 8]


def admits_weyl(p: int, q: int) -> bool:
    return (p + q) % 2 == 0


def admits_majorana_weyl(p: int, q: int) -> bool:
    """Real chiral spinors exist exactly when p - q = 0 mod 8 (even dimension)."""
    return admits_weyl(p, q) and (p - q) % 8 == 0


class MajoranaWeylForcesSevenSeven(unittest.TestCase):

    def test_1_only_one_reachable_horn_admits_majorana_weyl(self) -> None:
        print("\n[1] the two horns GU's split can reach, with fibre fixed at (6,4)")
        print(f"    {'base':7} {'ambient':9} {'p-q %8':7} {'class':7} {'Majorana-Weyl':13}")
        surviving = []
        for name, base in BASE_HORNS.items():
            amb = (base[0] + FIBRE[0], base[1] + FIBRE[1])
            mw = admits_majorana_weyl(*amb)
            print(f"    {name:7} {str(amb):9} {(amb[0]-amb[1]) % 8:5}   "
                  f"{clifford_class(*amb):7} {'YES' if mw else 'no':13}")
            if mw:
                surviving.append((name, amb))
        self.assertEqual(1, len(surviving),
                         "exactly one horn must survive the MW requirement")
        self.assertEqual(("(1,3)", (7, 7)), surviving[0])
        print("    => the MW requirement leaves exactly ONE horn: base (1,3), ambient (7,7).")
        print("       The base convention is a CONSEQUENCE here, not a convention.")

    def test_2_the_fibre_cannot_be_traded_against_the_base(self) -> None:
        """If the fibre moved with the base, the argument would be empty."""
        print("\n[2] why the argument is not vacuous")
        print("    G(-g) = G(g) EXACTLY (residual 0.00e+00, certified in")
        print("    tests/signature_fork_equivariance_defect.py), so the fibre is (6,4)")
        print("    on BOTH bases and is a FIXED input. It cannot be flipped to")
        print("    rescue the other horn.")
        for name, base in BASE_HORNS.items():
            amb = (base[0] + FIBRE[0], base[1] + FIBRE[1])
            self.assertEqual(14, amb[0] + amb[1])
        # had the fibre been free, BOTH horns could reach p-q = 0 and nothing is forced
        free_fibre_solutions = [
            (b, f) for b in BASE_HORNS.values()
            for f in [(6, 4), (4, 6)]
            if (b[0] + f[0] - b[1] - f[1]) % 8 == 0
        ]
        print(f"    with a FREE fibre sign, MW-admissible combinations: "
              f"{len(free_fibre_solutions)} -- nothing would be forced")
        self.assertGreater(len(free_fibre_solutions), 1)
        print("    with the fibre PINNED, exactly 1. The pinning does the work.")

    def test_3_the_full_dimension_14_picture(self) -> None:
        print("\n[3] all 14-dimensional signatures admitting Majorana-Weyl")
        mw_all = [(p, DIM - p) for p in range(DIM + 1)
                  if admits_majorana_weyl(p, DIM - p)]
        print(f"    {mw_all}")
        self.assertEqual([(3, 11), (7, 7), (11, 3)], mw_all)
        print("    (11,3) and (3,11) also admit MW but are NOT reachable from a")
        print("    Lorentzian base plus the 10-dimensional metric fibre:")
        reachable = {(b[0] + f[0], b[1] + f[1])
                     for b in [(3, 1), (1, 3)] for f in [(6, 4), (4, 6)]}
        print(f"    reachable from GU's 4+10 split: {sorted(reachable)}")
        self.assertNotIn((11, 3), reachable)
        self.assertNotIn((3, 11), reachable)
        self.assertIn((7, 7), reachable)
        print("    => within GU's construction, (7,7) is the UNIQUE MW signature.")

    def test_4_the_carrier_dimensions_match_the_drafts_printed_numbers(self) -> None:
        print("\n[4] what the surviving horn gives, against the draft's own numbers")
        full_real = 2 ** (DIM // 2)          # 128
        half = full_real // 2                # 64
        print(f"    Cl(7,7) = M(128,R): minimal REAL module R^{full_real},")
        print(f"    Weyl halves {half} + {half}, both REAL.")
        self.assertEqual(128, full_real)
        self.assertEqual(64, half)
        print("    The 2021 draft prints Spin(7,7)+/- multiplicities 64- and 832-")
        print("    (gu-2021-draft-s11-s12-extraction-2026-08-03.md:115-116).")
        print("    64 is exactly the real chiral half. The carrier the draft")
        print("    describes is the one this horn -- and only this horn -- supplies.")
        print("\n    By contrast Cl(9,5) = M(64,H): the minimal module is H^32 = R^128,")
        print("    the same REAL dimension, but with NO Majorana condition available.")
        print("    Same size, different reality. That is the whole fork.")

    def test_5_verdict_and_its_condition(self) -> None:
        print("\nVERDICT: MW-REQUIREMENT-FORCES-(7,7)"
              "__CONDITIONAL-RESOLVER-FOR-SIGNATURE-AMBIENT")
        print("\n  IF the ambient matter carrier must be Majorana-Weyl,")
        print("  THEN the ambient signature is (7,7) and the base is (1,3).")
        print("  No residual freedom. The base is a consequence, not a convention.")
        print("\n  THE CONDITION IS A REQUIREMENT GU ADOPTS, NOT A THEOREM.")
        print("  A quaternionic carrier on (9,5) is mathematically available and")
        print("  the repository built seven waves on one. So this does not prove")
        print("  GU must be (7,7); it proves one named condition determines the")
        print("  horn completely -- which is the shape the ledger is built for.")
        print("\n  NOT DONE HERE: filing this as SIGNATURE-AMBIENT's resolver.")
        print("  Two resolvers were falsified on this row today, both by the")
        print("  agent proposing this one. It goes to review first.")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
