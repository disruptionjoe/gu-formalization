#!/usr/bin/env python3
r"""
Anchor the RS twisted net-chiral integer +256 by FORWARD analytic decomposition and run the four
fabrication checks. Also test whether ANY twist / chirality choice can make the RS frame-index
operator's net-chiral integer carry a factor of 3.

Tr(gamma5_int . O_RS_tw) with O_RS_tw = sum_{mu,nu in BASE} |mu><nu| (x) P16 gamma_mu gamma_nu P16.
Frame trace |mu><nu| -> delta_{mu nu}; only diagonal mu=nu survive; gamma_mu^2 = +1 (base Euclidean):
   = sum_{mu in BASE} Tr_128( g5i P16 P16 )  =  |BASE| * Tr( g5i P16 ),   P16 = (1+g5i)/2
   Tr(g5i P16) = (1/2)(Tr g5i + Tr g5i^2) = (1/2)(0 + 128) = 64
   => 4 * 64 = 256 = 2^8.
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.normpath(os.path.join(HERE, "..")),
          os.path.normpath(os.path.join(HERE, "..", "generation-sector"))):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as bridge

N, DIM = bridge.N, bridge.DIM
e = bridge.gammas()
I128 = np.eye(DIM, dtype=complex)
BASE = (0, 1, 2, 3)


def chir(dirs):
    g = I128.copy()
    for a in dirs:
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    return g / np.sqrt(abs((np.trace(g @ g) / DIM).real))


def primefac(n):
    n = abs(int(round(n)))
    if n <= 1:
        return str(n)
    out, d = [], 2
    while d * d <= n:
        ee = 0
        while n % d == 0:
            n //= d; ee += 1
        if ee:
            out.append(f"{d}^{ee}" if ee > 1 else f"{d}")
        d += 1
    if n > 1:
        out.append(str(n))
    return ".".join(out)


def three_and_two_part(n):
    n = abs(int(round(n)))
    if n == 0:
        return 0, 0
    t = n
    k = 0
    while t % 3 == 0:
        t //= 3; k += 1
    return 3 ** k, n // (3 ** k)


def main():
    g5i = chir(range(4, N))         # internal Spin(10) chirality
    g5b = chir(BASE)                # base spacetime chirality
    om = chir(range(N))             # volume chirality

    print("=" * 88)
    print("FORWARD analytic decomposition of the RS twisted net-chiral integer")
    print("=" * 88)
    # numeric Tr(g5i P16)
    P16 = 0.5 * (I128 + g5i)
    tr_g5i_P16 = np.trace(g5i @ P16).real
    print(f"  Tr(g5i) = {np.trace(g5i).real:.1f} (expect 0)")
    print(f"  Tr(g5i^2) = {np.trace(g5i @ g5i).real:.1f} (expect 128 = DIM)")
    print(f"  Tr(g5i.P16) = {tr_g5i_P16:.1f}  (analytic (0+128)/2 = 64)")
    print(f"  |BASE| = {len(BASE)} base spacetime directions (= dim TX^4, NOT an assumed rank)")
    net = len(BASE) * tr_g5i_P16
    print(f"  => net-chiral integer = |BASE| * Tr(g5i.P16) = {len(BASE)} * {tr_g5i_P16:.0f} = {net:.0f}")
    t3, t2 = three_and_two_part(net)
    print(f"  primefac({int(net)}) = {primefac(net)} ; 3-part = {t3} ; 2-part = {t2}")

    print("\n" + "=" * 88)
    print("Does ANY twist make the RS net-chiral integer 3-primary? sweep chirality gradings/twists")
    print("=" * 88)
    # build O_RS_tw for several twist projectors P = (1 +/- g5)/2 and grading choices; report integers
    def O_tw(P):
        O = np.zeros((N * DIM, N * DIM), dtype=complex)
        for mu in BASE:
            for nu in BASE:
                Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
                O += np.kron(Emn, P @ (e[mu] @ e[nu]) @ P)
        return O
    twists = {"P16 internal(+)": 0.5 * (I128 + g5i),
              "P16bar internal(-)": 0.5 * (I128 - g5i),
              "base Weyl(+)": 0.5 * (I128 + g5b),
              "no twist": I128}
    gradings = {"int": np.kron(np.eye(N), g5i), "base": np.kron(np.eye(N), g5b),
                "vol": np.kron(np.eye(N), om)}
    any3 = False
    for tname, P in twists.items():
        O = O_tw(P)
        row = []
        for gname, G in gradings.items():
            v = np.trace(G @ O).real
            iv = int(round(v))
            t3, t2 = three_and_two_part(iv)
            if iv != 0 and t3 > 1:
                any3 = True
            row.append(f"{gname}={iv:+d}[3p {t3},2p {t2}]")
        print(f"  twist {tname:<20}: " + "  ".join(row))
    print(f"\n  ANY net-chiral integer with a factor of 3 anywhere in the sweep? {any3}")

    print("\n" + "=" * 88)
    print("FOUR FABRICATION CHECKS on the +256")
    print("=" * 88)
    print(f"  (1) disguised chi: 256 == 24? {256 == 24}; 256 % 24 == 0? {256 % 24 == 0}; "
          f"factor 3? {256 % 3 == 0}.  256 = 4*64 (dim TX^4 * chiral-16 sector dim), NO chi route.")
    print(f"      (the +96 CHIRALIZER control IS 96 = {primefac(96)} -- contains a 3 -- but is "
          f"FRAME-TRIVIAL, so its 3 never reaches the tangential channel.)")
    print(f"  (2) reverse-engineered: 256 derived FORWARD as |BASE|*Tr(g5i.P16) = 4*64, not fitted "
          f"to any target; nothing was tuned toward 3.")
    print(f"  (3) circular rank-4: the '4' is dim TX^4 (the 4 spacetime frame directions), a fixed "
          f"structural count, not an assumed-then-found rank.")
    print(f"  (4) fitted holonomy: NO holonomy used; O_RS_tw is built from raw Cl(9,5) gammas + the "
          f"Spin(10) chiral projector only.")
    return {"net_chiral_integer": int(net), "primefac": primefac(net),
            "three_part": t3, "two_part": t2, "any_3_in_sweep": any3}


if __name__ == "__main__":
    print("\nRETURN:", main())
