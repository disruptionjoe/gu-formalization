#!/usr/bin/env python3
r"""
ANCHORED LEAD: Spin(8) triality as a SYMMETRY-bridge (equivariant Lefschetz integer).

The steelman (genuinely new vs. every prior Z/3 attempt):
  - prior attempts looked for a *pairing* / canonical map Z/8 <-> Z/3, killed by coprime
    linking-form vanishing (Hom(Z/3,Z)=0, the no-go-class-relative-map result).
  - triality is a *symmetry* (order-3 outer automorphism of Spin(8)), so it is NOT a pairing
    and is not bound by that vanishing; and the natural invariant it produces, an EQUIVARIANT
    LEFSCHETZ / G-index number L(g) = sum_i (-1)^i tr(g | H^i), is a genuine INTEGER (in Z[omega]),
    type-correct, unlike the absolute torsion class.

Two decisive, computable obstructions are tested here (NOT fabricated -- run on the verified
Cl(9,5)=M(64,H) substrate / by exact linear algebra):

  CHECK 1 (frame-charge of the triality action).  The boundary-eta DECOUPLE mechanism
  (canon/boundary-eta-of-mu-RESULTS.md) is: an operator that is an INTERNAL-FIBER endomorphism
  id_14 (x) M has tangent-frame charge EXACTLY 0, so it cannot feed the gravitational -p_1/24
  channel where the order-3 lives. We prove the same for ANY internal Spin(8)/Spin(10)-fiber
  order-3 element (the triality / SU(3)_family candidate): frame charge is identically 0 because
  Tr(L^dag)=0 for every antisymmetric frame generator L. A DIAGONAL triality (tangent (x) fiber)
  picks up frame charge ONLY from its tangent SO(4) rotation factor -- which is a generic
  spacetime rotation, not a family symmetry, and whose Lefschetz contribution is the ordinary
  tangent index, not a generation count.

  CHECK 2 (Lefschetz number is a DEFORMATION invariant => blind to located-vs-forced).  The
  located->forced question is precisely DYNAMICAL: does the vectorlike (+96/-96) carrier get a
  DIRAC MASS (massive=forced) or stay massless (modulus=located)?  We exhibit an order-3 symmetry
  g on a toy Z/2-graded index complex and show the equivariant index/Lefschetz number
  ind_g = tr(g|ker) - tr(g|coker) is UNCHANGED as we turn on a g-equivariant mass m: 0 -> large.
  A homotopy-fixed integer cannot discriminate the very deformation that separates located from
  forced -- so even granting an integer-3, triality can only RE-LOCATE the slot, not force it.

Run: python tests/anchored-leads/spin8_triality_lefschetz.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
PAR = os.path.normpath(os.path.join(HERE, ".."))
for p in (GEN, PAR):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gu_bridge  # noqa: E402

N, DIM = gu_bridge.N, gu_bridge.DIM  # 14, 128


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1.0
    M[j, i] = -1.0
    return M


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def frame_charge(O, frame_gens):
    """Component of O along the base tangent-frame generators L (x) I_128.
    F_L = Tr_14[(L (x) I)^dag O]/Tr(L^dag L); returns sum_L ||F_L||_F.
    EXACTLY 0 for any pure internal-fiber endomorphism id_14 (x) M (Tr(L^dag)=0)."""
    O4 = O.reshape(N, DIM, N, DIM)
    total = 0.0
    for L in frame_gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        F_L = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        total += float(np.linalg.norm(F_L))
    return total


def order3_from_generator(G):
    """exp(theta*G) with G a (real-antisymmetric-like) generator scaled so the unitary has order 3.
    We do not need exact order 3 for the frame-charge argument; we DO build an exactly-order-3
    permutation realization in CHECK 2."""
    # exponentiate to a unitary; exact order is irrelevant to frame charge (linear in O is enough
    # via the generator), but we return the group element for completeness.
    from scipy.linalg import expm  # noqa
    theta = 2 * np.pi / 3
    return expm(theta * G)


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=160)
    e = gu_bridge.gammas()
    print("=" * 88)
    print("CHECK 1 -- FRAME CHARGE OF THE TRIALITY / FAMILY-SYMMETRY ORDER-3 ACTION")
    print("=" * 88)

    # tangent base frame TX^4 = {0,1,2,3}: self-dual + anti-self-dual so(4)
    sd = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
    asd = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
    so4 = sd + asd

    # (a) INTERNAL-FIBER order-3 candidate: a Spin(8) sitting in the internal directions {4..11}
    #     (the natural Spin(8) <= Spin(10) internal fiber). Any so(8)-internal generator lifts as
    #     id_14 (x) sgen(e,i,j). Build a representative internal order-3 generator and its element.
    Gint = sgen(e, 4, 5) + sgen(e, 6, 7) + sgen(e, 8, 9)  # an so(8)-internal Cartan-like element
    Oint_gen = np.kron(np.eye(N), Gint)                    # id_14 (x) (internal endomorphism)
    # the FULL group element exp is still id_14 (x) (unitary): still a pure fiber endomorphism
    from scipy.linalg import expm
    Oint = np.kron(np.eye(N), expm((2 * np.pi / 3) * Gint))

    fc_int_gen = frame_charge(Oint_gen, so4)
    fc_int = frame_charge(Oint, so4)

    # (b) DIAGONAL order-3: tangent SO(4) 120-rotation (x) internal order-3
    Gtan = (2 * np.pi / 3) * (lvec(0, 1) + lvec(2, 3)) / 2.0  # a tangent self-dual rotation gen
    Otan = np.kron(expm(Gtan), np.eye(DIM))
    Odiag = Otan @ Oint
    fc_tan = frame_charge(Otan, so4)
    fc_diag = frame_charge(Odiag, so4)
    # net self-dual minus anti-self-dual imbalance of the tangent part (the only thing that can
    # feed -p_1/24): a generic 120-rotation is balanced unless it is a chiral self-dual rotation.
    fc_tan_sd = frame_charge(Otan, sd)
    fc_tan_asd = frame_charge(Otan, asd)

    print(f"(a) INTERNAL-fiber order-3 (triality/SU(3)_family candidate), id_14 (x) M:")
    print(f"      frame charge of generator id_14(x)Gint   = {fc_int_gen:.3e}")
    print(f"      frame charge of group element id_14(x)U   = {fc_int:.3e}")
    print(f"      => EXACTLY 0 (Tr(L^dag)=0 for antisym L). SELECTOR-side, cannot feed -p_1/24.")
    print(f"(b) DIAGONAL order-3 (tangent SO(4) 120-rot (x) internal order-3):")
    print(f"      frame charge of tangent factor            = {fc_tan:.3f}")
    print(f"      frame charge of diagonal element          = {fc_diag:.3f}")
    print(f"      tangent self-dual / anti-self-dual split  = {fc_tan_sd:.3f} / {fc_tan_asd:.3f}")
    print(f"      => the ONLY frame charge comes from the tangent SO(4) rotation, a generic")
    print(f"         spacetime rotation (NOT a family symmetry); its Lefschetz contribution is")
    print(f"         the ordinary tangent index, not a generation count.")

    print()
    print("=" * 88)
    print("CHECK 2 -- EQUIVARIANT LEFSCHETZ NUMBER IS A DEFORMATION (HOMOTOPY) INVARIANT")
    print("=" * 88)
    # Toy Z/2-graded supersymmetric index complex modelling the vectorlike (+96/-96) carrier:
    # H^0 = C^3 (three would-be generations), H^1 = C^3 (their mirrors). An order-3 symmetry g
    # acts as the cyclic permutation rho = diag(1, omega, omega^2) on BOTH (a real triality-type
    # eigenstructure on the triplet). The Dirac/RS operator D maps H^0 -> H^1; a g-equivariant
    # MASS deformation m pairs each generation with its mirror (D += m*Id). The located->forced
    # physics = whether m=0 (massless modulus, located) or m!=0 (massive, forced).
    omega = np.exp(2j * np.pi / 3)
    rho = np.diag([1.0, omega, omega ** 2])           # order-3 g on each graded piece

    def equiv_index(m):
        """ind_g(D_m) = tr(g|ker D_m) - tr(g|coker D_m) for D_m : H^0 -> H^1, D_m = m*Id (+ any
        g-equivariant map). With m=0: ker=H^0, coker=H^1 -> ind_g = tr(rho)-tr(rho)=0.
        With m!=0: D_m invertible -> ker=coker=0 -> ind_g=0. The g-graded refinement is computed
        eigenspace-by-eigenspace to expose that EACH triality sector's index is also deformation-
        invariant."""
        D = m * np.eye(3, dtype=complex)              # g-equivariant (commutes with rho)
        # restrict to each omega-eigenspace of g and compute the per-sector index
        per = {}
        for k, lam in enumerate((1.0, omega, omega ** 2)):
            # 1-dim sector: ker(D) and coker(D) on that line
            d = D[k, k]
            ker = 1 if abs(d) < 1e-9 else 0
            coker = 1 if abs(d) < 1e-9 else 0
            per[k] = lam * (ker - coker)              # contribution to tr(g|ker)-tr(g|coker)
        total = sum(per.values())
        return total, per

    print("  toy carrier: H^0=C^3 (generations), H^1=C^3 (mirrors); g acts as diag(1,w,w^2).")
    print("  D_m = m*Id is g-equivariant; m=0 <=> massless (LOCATED), m!=0 <=> massive (FORCED).")
    print(f"  {'mass m':>10} {'ind_g (Lefschetz)':>20} {'per-triality-sector index':>34}")
    for m in (0.0, 0.5, 1.0, 5.0, 100.0):
        tot, per = equiv_index(m)
        persf = "[" + ", ".join(f"{per[k].real:+.2f}{per[k].imag:+.2f}i" for k in per) + "]"
        print(f"  {m:>10.2f} {tot.real:>+12.3f}{tot.imag:>+8.3f}i {persf:>34}")
    print("  => ind_g and EVERY per-sector index are CONSTANT across m=0 -> 100. The equivariant")
    print("     Lefschetz integer cannot see the Dirac mass that separates LOCATED from FORCED.")

    # invariance assertion
    base, _ = equiv_index(0.0)
    assert all(abs(equiv_index(m)[0] - base) < 1e-9 for m in (0.5, 1.0, 5.0, 100.0)), \
        "Lefschetz number must be deformation-invariant"
    # frame-charge assertions (the load-bearing exact facts)
    assert fc_int_gen < 1e-10 and fc_int < 1e-10, "internal-fiber order-3 must have frame charge 0"
    assert fc_diag > 1e-3, "diagonal order-3 must carry tangent frame charge (from the SO(4) factor)"

    print()
    print("=" * 88)
    print("VERDICT")
    print("=" * 88)
    print("  - Triality permutes the INEQUIVALENT reps 8_v/8_s/8_c, so it is NOT an inner")
    print("    automorphism of Spin(9,5) (inner autos preserve iso-class of each irrep). It is")
    print("    therefore NOT a symmetry already present in GU's frame-bundle structure group; it")
    print("    must be IMPOSED BY HAND as an extra discrete family symmetry. (= the SU(3)_family")
    print("    Z/3 the CRT result already found 'real group torsion, stranded internal-fiber'.)")
    print("  - Realized in the internal fiber, its frame charge is EXACTLY 0 (CHECK 1): same")
    print("    boundary-eta DECOUPLE as the +96 selector. SELECTOR-ARENA, cannot feed -p_1/24.")
    print("  - Even granting an integer, the equivariant Lefschetz number is DEFORMATION-INVARIANT")
    print("    (CHECK 2): it is blind to the Dirac mass that is the entire located-vs-forced")
    print("    content. So it can RE-LOCATE (a type-correct integer label) but cannot FORCE.")
    print("  - And to compute the H^i it traces, one needs the actual twisted-RS complex = the")
    print("    unbuilt SOURCE ACTION. It gates on the same object as everything else.")
    print("  GRADE: GATED (re-locates + gates on the source action; the symmetry framing does not")
    print("         escape the gate, and homotopy-invariance blocks located->forced even past it).")


if __name__ == "__main__":
    main()
