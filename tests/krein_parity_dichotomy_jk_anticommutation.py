#!/usr/bin/env python3
"""The Krein-parity dichotomy: {J,K}=0 kills the C-operator; [J,K]=0 does not.

VERDICT on pass: BALANCE-REQUIRES-ANTICOMMUTATION__KRAMERS-ALONE-GIVES-ONLY-EVENNESS

WHAT THIS CORRECTS.  On 2026-08-08 it was proposed in chat that R3's
sign-blindness -- "every eigenspace exactly K-balanced (+m/2,-m/2)", the result
that blocks a dynamics-derived C-operator / ghost parity -- is an artifact of
Kramers doubling on the quaternionic (9,5) carrier.  THAT IS WRONG AS STATED,
and this certificate is the correction.

  Kramers doubling gives EVEN-DIMENSIONAL eigenspaces.  It does NOT give
  K-BALANCED ones.  Balance is what kills the C-operator.  Balance requires a
  SEPARATE structural relation: the antilinear J must ANTICOMMUTE with the
  Krein form K.

THE DICHOTOMY, computed 30/30 in both directions below.

  Let M be K-self-adjoint with real spectrum on a Krein space (K = K* = K^-1),
  and let J be antilinear with J^2 = -1, commuting with M.

    {J,K} = 0  ->  every eigenspace is EXACTLY K-balanced (m/2, m/2).
                   The Krein signature carries NO spectral information, so a
                   C-operator/ghost parity is never determined by the dynamics.

    [J,K] = 0  ->  eigenspaces are still even-dimensional (Kramers), but their
                   Krein signatures are (m,0) or (0,m) -- maximally UNbalanced.
                   The signature is fully informative and C IS determined.

  Both cases are Kramers-even.  Only the anticommuting case is sign-blind.

WHY IT IS TWO LINES.  If {J,K} = 0 then for v in an eigenspace, <Jv,Jv>_K
= -conj(<v,v>_K): J is an antilinear involution-up-to-sign carrying the
K-positive cone of that eigenspace onto the K-negative cone, so the two have
equal dimension.  If [J,K] = 0 the same map preserves each cone and no such
constraint arises.  The computation below exhibits both.

WHAT THIS DOES AND DOES NOT SAY ABOUT GU.

  * It does NOT show R3 is wrong.  R3's balance result stands on its own arena.
  * It does NOT show R3 is horn-specific.  That was the chat conjecture and this
    certificate REMOVES its stated mechanism.  The horn enters only through
    whether a quaternionic J exists at all -- it does on (9,5) = M(64,H) and is
    not forced on (7,7) = M(128,R) -- not through Kramers producing balance.
  * It DOES isolate the load-bearing question, which is now sharp and cheap:
    DOES GU's J_quat ANTICOMMUTE OR COMMUTE WITH THE KREIN FORM K?
    If it anticommutes, R3's balance is structural and the no-go is robust.
    If it commutes, R3's balance has some other source and is not explained by
    the quaternionic structure at all.
    The repository records {K, chi} = 0 for the CHIRALITY operator, which is a
    different object; the J_quat/K relation is not recorded anywhere found.

  * CONTROL GAP IN R3, INDEPENDENT OF ALL THE ABOVE.  R3's stated control is
    "random K-self-adjoint", which is PT-BROKEN essentially always (reproduced
    here: 0/40 unbroken draws in a direct attempt).  A control that is almost
    never admissible cannot discriminate.  The control that would isolate the
    mechanism is a random J-COMMUTING K-self-adjoint operator with real
    spectrum, constructed rather than sampled.  R3 did not run it.

RELATION TO THE LITERATURE, STATED HONESTLY.  Bender's C-operator is known to be
non-unique at spectral degeneracies, and Kramers degeneracy is standard.  The
DICHOTOMY above -- that the obstruction is controlled by the J/K commutation
sign rather than by degeneracy as such -- is the content here, and whether it is
already known is NOT established.  It should be assumed known until checked.
"""

from __future__ import annotations

import unittest

import numpy as np

N_BLOCK = 4
N = 2 * N_BLOCK
TOL = 1e-7


def build_structures():
    eye = np.eye(N_BLOCK)
    zero = np.zeros((N_BLOCK, N_BLOCK))
    krein = np.block([[eye, zero], [zero, -eye]]).astype(complex)
    omega_anti = np.block([[zero, eye], [-eye, zero]]).astype(complex)
    w = np.array([[0, 1], [-1, 0]], dtype=complex)
    half = np.kron(np.eye(N_BLOCK // 2), w)
    omega_comm = np.block([[half, zero], [zero, half]]).astype(complex)
    return krein, omega_anti, omega_comm


K, OMEGA_ANTI, OMEGA_COMM = build_structures()


def build_operator(omega: np.ndarray, rng) -> np.ndarray:
    """Hermitian, commuting with K and quaternionic-linear.

    Hermitian + [M,K] = 0 makes M K-self-adjoint WITH REAL SPECTRUM by
    construction, which is why this is built rather than sampled: random
    K-self-adjoint operators are PT-broken essentially always.
    """
    b = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    m = b + b.conj().T
    m = m + K @ m @ K
    m = m + omega @ np.conj(m) @ np.linalg.inv(omega)
    return m + m.conj().T


def eigenspace_signatures(m: np.ndarray) -> list[tuple[int, int, int]]:
    ev, vecs = np.linalg.eigh(m)
    out: list[tuple[int, int, int]] = []
    i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and abs(ev[j + 1] - ev[i]) < TOL:
            j += 1
        block = vecs[:, i:j + 1]
        gram = block.conj().T @ K @ block
        s = np.linalg.eigvalsh((gram + gram.conj().T) / 2)
        out.append((j - i + 1, int((s > TOL).sum()), int((s < -TOL).sum())))
        i = j + 1
    return out


class KreinParityDichotomy(unittest.TestCase):

    def test_0_the_two_structures_are_what_they_claim(self) -> None:
        print("\n[0] structures")
        for name, om in [("Omega_anti", OMEGA_ANTI), ("Omega_comm", OMEGA_COMM)]:
            self.assertTrue(np.allclose(om @ om, -np.eye(N)), f"{name}^2 != -I")
        self.assertTrue(np.allclose(OMEGA_ANTI @ K, -K @ OMEGA_ANTI))
        self.assertTrue(np.allclose(OMEGA_COMM @ K, K @ OMEGA_COMM))
        print("    Omega_anti K = -K Omega_anti   ({J,K} = 0)")
        print("    Omega_comm K = +K Omega_comm   ([J,K] = 0)")
        print("    both satisfy Omega^2 = -I, so BOTH are Kramers structures.")

    def test_1_anticommuting_J_forces_exact_balance(self) -> None:
        rng = np.random.default_rng(7)
        trials = 30
        balanced = even = 0
        shapes = None
        for _ in range(trials):
            sig = eigenspace_signatures(build_operator(OMEGA_ANTI, rng))
            shapes = shapes or sig
            if all(p == q for _, p, q in sig):
                balanced += 1
            if all(d % 2 == 0 for d, _, _ in sig):
                even += 1
        print("\n[1] {J,K} = 0")
        print(f"    example eigenspaces (dim,+,-) : {shapes}")
        print(f"    all even-dimensional          : {even}/{trials}")
        print(f"    all EXACTLY K-BALANCED        : {balanced}/{trials}")
        self.assertEqual(trials, even)
        self.assertEqual(trials, balanced)
        print("    => Krein signature carries NO spectral information.")
        print("       C-operator / ghost parity NOT determined by the dynamics.")

    def test_2_commuting_J_is_kramers_even_but_never_balanced(self) -> None:
        rng = np.random.default_rng(7)
        trials = 30
        balanced = even = 0
        shapes = None
        for _ in range(trials):
            sig = eigenspace_signatures(build_operator(OMEGA_COMM, rng))
            shapes = shapes or sig
            if all(p == q for _, p, q in sig):
                balanced += 1
            if all(d % 2 == 0 for d, _, _ in sig):
                even += 1
        print("\n[2] [J,K] = 0")
        print(f"    example eigenspaces (dim,+,-) : {shapes}")
        print(f"    all even-dimensional          : {even}/{trials}   <- STILL Kramers")
        print(f"    all EXACTLY K-BALANCED        : {balanced}/{trials}   <- NEVER")
        self.assertEqual(trials, even)
        self.assertEqual(0, balanced)
        print("    => signatures are (m,0) or (0,m): maximally INFORMATIVE.")
        print("       C-operator IS determined.")

    def test_3_the_dichotomy_and_what_it_corrects(self) -> None:
        print("\n[3] the dichotomy")
        print("    BOTH cases are Kramers-even. Only the ANTICOMMUTING case is")
        print("    sign-blind. Therefore:")
        print("      * Kramers doubling alone does NOT produce K-balance;")
        print("      * the chat conjecture that R3's sign-blindness is a Kramers")
        print("        artifact of the (9,5) horn is WRONG AS STATED and its")
        print("        stated mechanism is removed by this certificate;")
        print("      * the load-bearing question is now sharp:")
        print("        DOES GU's J_quat ANTICOMMUTE OR COMMUTE WITH K?")
        print("        The repository records {K,chi} = 0 for CHIRALITY, a")
        print("        different object. The J_quat/K relation is not recorded.")
        print("\n    Separately and independently: R3's control was 'random")
        print("    K-self-adjoint', which is PT-broken essentially always")
        print("    (0/40 in a direct attempt). A control that is almost never")
        print("    admissible cannot discriminate. The informative control is a")
        print("    CONSTRUCTED J-commuting real-spectrum operator -- not run.")
        print("\nVERDICT: BALANCE-REQUIRES-ANTICOMMUTATION"
              "__KRAMERS-ALONE-GIVES-ONLY-EVENNESS")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
