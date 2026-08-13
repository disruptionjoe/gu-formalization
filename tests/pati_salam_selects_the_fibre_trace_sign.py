#!/usr/bin/env python3
"""The author's Pati-Salam criterion DOES select the fibre trace sign.

VERDICT on pass: PATI-SALAM-SELECTS-(6,4)__CRITERION-IS-REAL-BUT-EXTERNAL

WHAT THIS ANSWERS.  The 2026-08-08 hostile review falsified the Majorana-Weyl
candidate as a resolver for SIGNATURE-AMBIENT, correctly, and one of its three
grounds was:

    "G(-g)=G(g) proves base-sign invariance AFTER fixing lambda=1/2 and the
     trace sign; it does not derive those choices."

That is right, and it left an open question the review named but did not test:
Weinstein supplies a CRITERION for the trace sign, and nobody had checked
whether the criterion actually works.  It does.  This certificate tests it.

THE CRITERION, in the author's own voice (Portal 2020, 02:42:20, quoted in
lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md:525):
Pati-Salam "is really much more naturally Spin(6) x Spin(4) when the trace
portion of the space of metrics is put in with the proper sign", and the
signatures are the ones "that make it look like the Pati-Salam rather than
directly in the Spin(10), SU(5) line of thinking."

THE TEST.  The 10-dimensional metric fibre Sym^2(T*X) has two trace-sign
options, and they give different isometry groups:

    raw Frobenius   (trace line +)   signature (7,3)   SO(7,3)
    trace-reversed  (trace line -)   signature (6,4)   SO(6,4)

The maximal compact subgroup of SO(p,q) is SO(p) x SO(q).  So:

    SO(7,3) -> SO(7) x SO(3),  dim 21 + 3  = 24
    SO(6,4) -> SO(6) x SO(4),  dim 15 + 6  = 21

and Pati-Salam is SU(4) x SU(2) x SU(2), dim 15 + 3 + 3 = 21, with
Spin(6) = SU(4) and Spin(4) = SU(2) x SU(2).

ONLY (6,4) MATCHES.  The criterion selects the trace-reversed sign and excludes
the raw one.

SECOND CORROBORATION, from the same sentence.  Every so(p,q) with p+q=10 has
COMPACT FORM so(10) -- the SO(10) GUT line.  What distinguishes the signatures
is the MAXIMAL COMPACT.  So the author's contrast, "Pati-Salam rather than
directly in the Spin(10), SU(5) line", is precisely the distinction between the
maximal compact subgroup of SO(6,4) and its compact form SO(10).  That the
contrast he draws is exactly the one this reading produces is evidence that
"maximal compact" is the intended reading and not an interpolation.

WHAT THIS DOES AND DOES NOT DO.

  IT DOES retire "there is no criterion for the trace sign".  There is one, it
  is authorial, it is stated in the author's own voice, and it works.

  IT DOES NOT derive the trace sign from GU's action, and therefore does NOT
  overturn the review's verdict.  Wanting Pati-Salam is an EXTERNAL physical
  target, exactly like the TT-positivity criterion recorded earlier: it selects,
  but it is imported.  SIGNATURE-AMBIENT stays open.

  IT DOES NOT touch the base sign.  This pins the FIBRE only.  The Majorana-Weyl
  argument was about the BASE.  Two separate pinnings, two separate conditions.

  The review's other two grounds are untouched: the MW requirement is still not
  independently established, and Kramers still constrains a realized index
  rather than "three generations".
"""

from __future__ import annotations

import itertools
import unittest

import numpy as np

TOL = 1e-9


def sym2_basis(n: int = 4):
    out = []
    for i, j in itertools.combinations_with_replacement(range(n), 2):
        b = np.zeros((n, n))
        b[i, j] = b[j, i] = 1.0
        out.append(b)
    return out


BASIS = sym2_basis()
G_BASE = np.diag([1.0, 1.0, 1.0, -1.0])


def fibre_form(lam: float) -> np.ndarray:
    gi = np.linalg.inv(G_BASE)
    a = [gi @ b for b in BASIS]
    n = len(a)
    return np.array([[np.trace(a[i] @ a[j]) - lam * np.trace(a[i]) * np.trace(a[j])
                      for j in range(n)] for i in range(n)])


def signature(m: np.ndarray) -> tuple[int, int]:
    e = np.linalg.eigvalsh((m + m.T) / 2)
    return int((e > TOL).sum()), int((e < -TOL).sum())


def so_dim(n: int) -> int:
    return n * (n - 1) // 2


PATI_SALAM_DIM = 15 + 3 + 3          # su(4) + su(2) + su(2)


class PatiSalamSelectsTheTraceSign(unittest.TestCase):

    def test_1_the_two_trace_sign_options(self) -> None:
        print("\n[1] the two trace-sign options for the 10-dim metric fibre")
        raw, reversed_ = signature(fibre_form(0.0)), signature(fibre_form(0.5))
        print(f"    raw Frobenius  (trace +) : {raw}   -> SO{raw}")
        print(f"    trace-reversed (trace -) : {reversed_}   -> SO{reversed_}")
        self.assertEqual((7, 3), raw)
        self.assertEqual((6, 4), reversed_)

    def test_2_only_one_has_pati_salam_as_maximal_compact(self) -> None:
        print("\n[2] maximal compact subgroups; PS = SU(4)xSU(2)xSU(2), dim "
              f"{PATI_SALAM_DIM}")
        matches = []
        for lam, label in [(0.0, "raw (trace +)   "), (0.5, "trace-reversed  ")]:
            p, q = signature(fibre_form(lam))
            d = so_dim(p) + so_dim(q)
            is_ps = ({p, q} == {6, 4}) and (d == PATI_SALAM_DIM)
            print(f"    {label} ({p},{q}) -> SO({p})xSO({q}) dim {so_dim(p)}+{so_dim(q)}={d:2}"
                  f"   {'== PATI-SALAM' if is_ps else '!= Pati-Salam'}")
            if is_ps:
                matches.append((p, q))
        self.assertEqual([(6, 4)], matches,
                         "exactly the trace-reversed option must match Pati-Salam")
        print("    => the criterion SELECTS (6,4) and EXCLUDES (7,3).")
        # Spin(6) = SU(4), Spin(4) = SU(2)xSU(2)
        self.assertEqual(15, so_dim(6))
        self.assertEqual(6, so_dim(4))

    def test_3_the_compact_form_contrast_the_author_draws(self) -> None:
        print("\n[3] why the author's own contrast corroborates the reading")
        print("    Every so(p,q) with p+q=10 has COMPACT FORM so(10), dim "
              f"{so_dim(10)} -- the SO(10)/SU(5) line.")
        self.assertEqual(45, so_dim(10))
        print("    What differs between signatures is the MAXIMAL COMPACT.")
        print("    The author contrasts 'Pati-Salam rather than directly in the")
        print("    Spin(10), SU(5) line' -- which IS the maximal-compact vs")
        print("    compact-form distinction. The contrast he draws is exactly the")
        print("    one this reading produces, which is evidence that 'maximal")
        print("    compact' is intended and not interpolated.")

    def test_4_scope(self) -> None:
        print("\n[4] scope -- what this does NOT do")
        print("    * does NOT derive the trace sign from GU's action. Wanting")
        print("      Pati-Salam is an EXTERNAL target, like TT-positivity: it")
        print("      selects, but it is imported. SIGNATURE-AMBIENT stays OPEN.")
        print("    * does NOT touch the BASE sign. This pins the FIBRE only;")
        print("      the Majorana-Weyl argument was about the base. Two separate")
        print("      pinnings, two separate conditions.")
        print("    * does NOT disturb the 2026-08-08 review's other two grounds:")
        print("      the MW requirement is still not independently established,")
        print("      and Kramers still constrains a realized index rather than")
        print("      'three generations'.")
        print("\n    WHAT IT DOES RETIRE: 'there is no criterion for the trace")
        print("    sign'. There is one, it is authorial, and it works.")
        print("\nVERDICT: PATI-SALAM-SELECTS-(6,4)__CRITERION-IS-REAL-BUT-EXTERNAL")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
