#!/usr/bin/env python
"""Blockbuster P4 probe: the two generation doors.

PART A (Door A, the rank fold): signature-NEUTRAL internal Spin(10)/D5 weight
arithmetic plus exact bookkeeping of the Lambda^2_+ triplet ledger. Consumed
only by the Door A ((9,5)-side) section of the companion exploration. No
(7,7) quantity is computed here.

PART B (Door B, the eta pinning): (7,7)-class BDI/spectral-section arithmetic
at minimal scale -- crossing quanta, section-charge additivity, the T4
relocated-wall shape (base Cl(1,3) = M(2,H) of the (7,7)-inducing
convention). The Kramers-doubled family in B1b is a CLASS-GENERIC
Altland-Zirnbauer control (abstract J^2 = -1 arithmetic), labeled as such; it
is not a recomputation of any (9,5) GU quantity. No (9,5) quantity is
computed here.

K6 signature purity: the two parts share no computations; each part is cited
only by its own door's section in
explorations/blockbuster-p4-generation-doors-2026-07-19.md.

Run: python tests/channel-swings/bb_p4_generation_doors_probe.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product

import numpy as np

FAIL: list[str] = []
HALF = F(1, 2)


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ============================================================================
# PART A -- DOOR A: signature-neutral D5 weight arithmetic + triplet ledger
# ============================================================================

def unit(i: int, sign: int = 1) -> tuple:
    r = [F(0)] * 5
    r[i] = F(sign)
    return tuple(r)


def vsum(*ws) -> tuple:
    return tuple(sum(c) for c in zip(*ws))


def spinor16() -> list[tuple]:
    out = []
    for signs in product([HALF, -HALF], repeat=5):
        if sum(1 for s in signs if s < 0) % 2 == 1:
            out.append(signs)
    return out


def coord_sum(w) -> F:
    return sum(w, F(0))


def part_a() -> None:
    log("=" * 86)
    log("PART A  DOOR A -- the rank fold (signature-neutral internal group theory)")
    log("=" * 86)

    W16 = spinor16()
    B10 = [unit(i, s) for i in range(5) for s in (1, -1)]
    U = (F(1), F(1), F(1), F(-1), F(1))  # the G_SM-singlet X-direction (CH-SM S5)

    # ---- A1: every VEV-capable tensor irrep is generation-blind at the weight level
    lam2 = [vsum(a, b) for a, b in combinations(B10, 2)]                      # 45
    sym2 = [vsum(a, b) for a, b in combinations_with_replacement(B10, 2)]     # 55 = 1 + 54
    lam4 = [vsum(*q) for q in combinations(B10, 4)]                           # 210
    check("A1a  dims: Lambda^2(10)=45, Sym^2(10)=55=1+54, Lambda^4(10)=210",
          len(lam2) == 45 and len(sym2) == 55 and len(lam4) == 210)
    all_tensor = lam2 + sym2 + lam4
    check("A1b  every tensor-VEV weight is an INTEGER vector with EVEN coordinate sum (root lattice)",
          all(all(x.denominator == 1 for x in w) and coord_sum(w) % 2 == 0 for w in all_tensor))
    check("A1c  the rank-drop direction u (odd coordinate sum) is absent from 45, 54, 210",
          U not in set(all_tensor), "extends CH-SM lemma S5 to the full VEV menu used by the chain table")
    check("A1d  u/2 IS a weight of the 16 and u of Sym^2(16) (the 126's nu_c.nu_c direction)",
          tuple(x / 2 for x in U) in W16
          and U in {vsum(a, b) for a in W16 for b in W16})

    # ---- A2: matter parity is a UNIFORM scalar on the 16 -- it cannot grade flavor space
    # (-1)^(3(B-L)) with 3(B-L)(w) = 2(w1+w2+w3)
    exps16 = [2 * (w[0] + w[1] + w[2]) for w in W16]
    check("A2a  3(B-L) is an ODD integer on every one of the 16 states -> matter parity = -1 uniformly",
          all(e.denominator == 1 and e % 2 == 1 for e in exps16),
          "parity is a scalar on the matter 16: it carries NO projector on generation space")
    expsT = [2 * (w[0] + w[1] + w[2]) for w in all_tensor]
    check("A2b  3(B-L) is an EVEN integer on every 45/54/210 weight -> matter parity = +1 on all VEVs",
          all(e.denominator == 1 and e % 2 == 0 for e in expsT))

    # ---- A3: the constraint set on the Majorana (126-condensate) rank is EMPTY
    # Generation space C^N (N=3 demo): chain data act on the generation index as
    # the identity; the invariance equations for M (x) (nu_c nu_c) reduce to
    # charge(u) * M = 0 with charge(u) = 0 for every G_SM generator, and matter
    # parity contributes (-1)*(-1) = +1. So the induced constraint matrix on
    # Sym(N) is ZERO: every rank is admissible.
    SU3 = []
    for i, j in combinations(range(3), 2):
        for si, sj in ((1, -1), (-1, 1)):   # su(3) regular roots: +-(ei - ej) only
            r = [F(0)] * 5
            r[i], r[j] = F(si), F(sj)
            SU3.append(tuple(r))
    T3L_u = (U[3] + U[4]) / 2
    Y_u = (U[3] - U[4]) / 2 + F(1, 3) * (U[0] + U[1] + U[2])
    charges = [F(0) if all(sum(a * b for a, b in zip(U, rt)) == 0 for rt in SU3) else F(1), T3L_u, Y_u]
    check("A3a  every G_SM charge of the nu_c.nu_c direction is exactly 0 (su3 pairing, T3L, Y)",
          all(c == 0 for c in charges))
    parity_factor = (-1) * (-1)
    check("A3b  matter-parity factor on nu_c.nu_c is (+1): no equation on M from the Z/2 either",
          parity_factor == 1)

    def frac_rank(rows: list[list[F]]) -> int:
        m = [row[:] for row in rows]
        rank, ncols = 0, len(m[0]) if m else 0
        for col in range(ncols):
            piv = next((r for r in range(rank, len(m)) if m[r][col] != 0), None)
            if piv is None:
                continue
            m[rank], m[piv] = m[piv], m[rank]
            pv = m[rank][col]
            m[rank] = [x / pv for x in m[rank]]
            for r in range(len(m)):
                if r != rank and m[r][col] != 0:
                    fac = m[r][col]
                    m[r] = [a - fac * b for a, b in zip(m[r], m[rank])]
            rank += 1
        return rank

    for r_target in (1, 2, 3):
        M = [[F(1) if (i == j and i < r_target) else F(0) for j in range(3)] for i in range(3)]
        # the constraint system is the zero matrix (A3a/A3b), so residual == 0 for every M
        residual_rows = [[c * M[i][j] for j in range(3) for i in range(3)] for c in charges]
        resid_ok = all(x == 0 for row in residual_rows for x in row)
        check(f"A3c  symmetric Majorana matrix of rank {r_target}: constraint residual exactly 0, rank verified",
              resid_ok and frac_rank(M) == r_target,
              "the 54-lock + matter parity impose ZERO equations on the condensate rank")

    # ---- A4: the Lambda^2_+ provenance of the native 3 (exact bookkeeping)
    # Hodge star on Lambda^2(R^4), Euclidean: e12<->e34, e13<->-e24, e14<->e23.
    basis = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    star = [[F(0)] * 6 for _ in range(6)]
    pairs = {(1, 2): ((3, 4), 1), (3, 4): ((1, 2), 1),
             (1, 3): ((2, 4), -1), (2, 4): ((1, 3), -1),
             (1, 4): ((2, 3), 1), (2, 3): ((1, 4), 1)}
    for a, bi in enumerate(basis):
        tgt, sg = pairs[bi]
        star[basis.index(tgt)][a] = F(sg)
    sq = [[sum(star[i][k] * star[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
    check("A4a  star^2 = +1 on Lambda^2(R^4) exactly", all(sq[i][j] == (1 if i == j else 0)
          for i in range(6) for j in range(6)))
    minus_id = [[star[i][j] - (1 if i == j else 0) for j in range(6)] for i in range(6)]
    plus_id = [[star[i][j] + (1 if i == j else 0) for j in range(6)] for i in range(6)]

    def frac_rank_sq(m):
        return_rows = [row[:] for row in m]
        return frac_rank(return_rows)

    check("A4b  eigenspace split 3 + 3: dim Lambda^2_+ = 3 exactly (rank of star -/+ 1 is 3/3)",
          frac_rank_sq(minus_id) == 3 and frac_rank_sq(plus_id) == 3,
          "the native 3 = dim Lambda^2_+(4-base): conditional on d = 4, which is a declared INPUT (canon C-04 caveat)")
    check("A4c  triplet ledger: 640*1 + 416*2 + 64*3 = 1664 = ker(Gamma); 64*3 = 192; 3*2*16 = 96/chirality",
          640 * 1 + 416 * 2 + 64 * 3 == 1664 and 64 * 3 == 192 and 3 * 2 * 16 == 96 and 2 * 96 == 192,
          "cited decomposition (ghost-parity synthesis H1); arithmetic re-verified exactly")

    # ---- A5: the x2 debt -- the physical half of the triplet counts SIX 16-units
    check("A5   naive per-16 count of one Krein half of the triplet: 96/16 = 6 != 3 (= 3 x SU(2)- doublet)",
          F(96, 16) == 6 and F(96, 16) != 3,
          "even a successful mirror-selection leaves a x2 (SU(2)-) collapse unaccounted -- the '3 not 6' debt")


# ============================================================================
# PART B -- DOOR B: (7,7)-class BDI / spectral-section arithmetic
# ============================================================================

def part_b() -> None:
    log("")
    log("=" * 86)
    log("PART B  DOOR B -- the eta pinning ((7,7)-class arithmetic; control labeled class-generic)")
    log("=" * 86)
    rng = np.random.default_rng(20260719)
    TOL = 1e-9

    def eta_of(mat: np.ndarray) -> int:
        ev = np.linalg.eigvalsh(mat)
        return int(np.sum(ev > TOL) - np.sum(ev < -TOL))

    # ---- B1a: BDI (T'^2 = +1) family -- simple crossings, flow quantum 2, odd kernels
    d = 6
    Q, _ = np.linalg.qr(rng.standard_normal((d, d)))
    base = np.array([-0.5, -1.5, 0.8, -0.7, 1.2, -2.3])
    slope = np.array([1.0, 1.0, 0.0, 0.0, 0.0, 1.0])

    def A(t: float) -> np.ndarray:
        return Q @ np.diag(base + t * slope) @ Q.T

    ts = np.linspace(0.0, 2.6, 261)
    # eta is only well-defined away from a crossing: keep sample points where
    # the spectrum is safely invertible (gap > 1e-3)
    etas = [eta_of(A(t)) for t in ts if float(np.min(np.abs(np.linalg.eigvalsh(A(t))))) > 1e-3]
    jumps = sorted({abs(b - a) for a, b in zip(etas, etas[1:]) if a != b})
    kernel_at_half = int(np.sum(np.abs(np.linalg.eigvalsh(A(0.5))) < 1e-7))
    seen_mod4 = sorted({e % 4 for e in etas})
    check("B1a  BDI family (real symmetric): every eta jump is 2, a simple crossing has kernel dim 1 (ODD)",
          jumps == [2] and kernel_at_half == 1,
          f"eta path {sorted(set(etas))}, jumps {jumps}")
    check("B1b  BDI reaches BOTH eta classes mod 4 -> count = eta/2 reaches odd AND even values",
          seen_mod4 == [0, 2],
          f"eta mod 4 classes observed: {seen_mod4} (odd counts are boundary-reachable in the real class)")

    # ---- B1c: CLASS-GENERIC Kramers control (J^2 = -1, abstract AZ arithmetic;
    #           NOT a recomputation of any (9,5) GU quantity)
    n = 4
    Sig = np.block([[np.zeros((n, n)), -np.eye(n)], [np.eye(n), np.zeros((n, n))]])

    def kramers_avg(h: np.ndarray) -> np.ndarray:
        h = (h + h.conj().T) / 2
        return (h + Sig @ h.conj() @ Sig.T) / 2

    Ha = kramers_avg(rng.standard_normal((2 * n, 2 * n)) + 1j * rng.standard_normal((2 * n, 2 * n)))
    Hb = kramers_avg(rng.standard_normal((2 * n, 2 * n)) + 1j * rng.standard_normal((2 * n, 2 * n)))
    Hb = Hb + 3.0 * np.eye(2 * n)  # drive crossings
    max_pair_gap = 0.0
    ketas = []
    kernel_parities_even = True
    for t in np.linspace(0.0, 2.5, 251):
        H = Ha + t * Hb
        ev = np.sort(np.linalg.eigvalsh(H))
        max_pair_gap = max(max_pair_gap, float(np.max(np.abs(ev[0::2] - ev[1::2]))))
        kdim = int(np.sum(np.abs(ev) < 1e-6))
        if kdim % 2 == 1:
            kernel_parities_even = False
        if float(np.min(np.abs(ev))) > 1e-3:   # eta well-defined away from crossings
            ketas.append(int(np.sum(ev > TOL) - np.sum(ev < -TOL)))
    kjumps = sorted({abs(b - a) for a, b in zip(ketas, ketas[1:]) if a != b})
    check("B1c  Kramers control (class-generic J^2=-1): spectrum doubly degenerate, jumps in 4Z, kernels EVEN",
          max_pair_gap < 1e-9 and all(j % 4 == 0 for j in kjumps) and kernel_parities_even,
          f"max Kramers pair gap {max_pair_gap:.1e}, jumps {kjumps} -> count parity FROZEN; contrast B1a/B1b")
    check("B1d  Kramers control: count = eta/2 is even at every sampled point (odd counts unreachable)",
          all((e // 2) % 2 == 0 for e in ketas),
          f"eta values observed {sorted(set(ketas))}")

    # ---- B2: spectral-section charge additivity (the arithmetic behind clauses R and V)
    signs = [-1, -1, -1, 1, 1, 1, 1, -1, 1, -1]      # APS-style assignment for an invertible D
    eta_aps = sum(signs)
    flipped = signs[:]
    for k in (0, 1, 7):                                # a section of relative charge 3
        flipped[k] = +1
    eta_sec = sum(flipped)
    check("B2a  two sections differing by a rank-r reassignment shift eta by exactly 2r (r=3 -> shift 6)",
          eta_sec - eta_aps == 2 * 3,
          f"eta_APS {eta_aps} -> eta_section {eta_sec}: pinning the count IS pinning the section charge")
    check("B2b  hence count(eta/2) shifts by exactly the section's charge: the integer lives on the section",
          (eta_sec - eta_aps) // 2 == 3)

    # ---- B3: odd-count arithmetic on the CITED (7,7) flow values (input data, not recomputed)
    flow_values = [0, 2, -2, -4, -6]                   # W1 Part C3 table, cited
    counts = [v // 2 for v in flow_values]
    check("B3a  count odd <=> eta = 2 mod 4, over the cited (7,7) flow value set",
          all((c % 2 == 1) == (v % 4 == 2) for c, v in zip(counts, flow_values)),
          f"counts {counts}")
    check("B3b  |count| = 3 is reached exactly at |eta| = 6 (the value clause V must select)",
          [v for v in flow_values if abs(v) == 6] == [-6] and abs(-6 // 2) == 3)

    # ---- B4: the T4 relocated wall at minimal scale -- base Cl(1,3) = M(2,H)
    #          of the (7,7)-inducing convention: base-linear carriers land in 8Z
    Li = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], dtype=float)
    Lj = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]], dtype=float)
    I4, Z4 = np.eye(4), np.zeros((4, 4))
    e0 = np.block([[Z4, I4], [I4, Z4]])
    e1 = np.block([[Z4, -I4], [I4, Z4]])
    e2 = np.block([[Li, Z4], [Z4, -Li]])
    e3 = np.block([[Lj, Z4], [Z4, -Lj]])
    gammas = [e0, e1, e2, e3]
    sig_ok = (np.allclose(e0 @ e0, np.eye(8)) and all(np.allclose(g @ g, -np.eye(8)) for g in gammas[1:])
              and all(np.allclose(gammas[i] @ gammas[j] + gammas[j] @ gammas[i], 0)
                      for i in range(4) for j in range(i + 1, 4)))
    check("B4a  explicit real 8-dim Cl(1,3) rep: relations exact (e0^2=+1, ei^2=-1, anticommuting)", sig_ok)

    def commutant_dim(gens: list[np.ndarray]) -> tuple[int, np.ndarray]:
        m = gens[0].shape[0]
        rows = [np.kron(g, np.eye(m)) - np.kron(np.eye(m), g.T) for g in gens]
        K = np.vstack(rows)
        _, s, Vh = np.linalg.svd(K)
        null = Vh[np.sum(s > 1e-8):].conj()
        return null.shape[0], null

    dim_c, _ = commutant_dim(gammas)
    check("B4b  commutant of Cl(1,3) on R^8 has real dimension 4 (quaternionic; irreducible module R^8)",
          dim_c == 4, "the (7,7)-inducing convention's base algebra is M(2,H): the wall RELOCATED, not deleted")

    kgen = [np.kron(g, np.eye(3)) for g in gammas]     # base action on R^8 (x) R^3
    dim_c24, null24 = commutant_dim(kgen)
    check("B4c  base-linear operators on R^8(x)R^3: commutant dimension 36 = dim_R M(3,H)",
          dim_c24 == 36)
    coeffs = rng.standard_normal(null24.shape[0])
    X = np.tensordot(coeffs, null24, axes=(0, 0)).reshape(24, 24)
    S = (X + X.T) / 2
    S = sum((g @ S @ np.linalg.inv(g) for g in kgen), start=4 * S) / 8   # re-average symmetric part into commutant
    comm_res = max(float(np.linalg.norm(g @ S - S @ g)) for g in kgen)
    ev = np.sort(np.linalg.eigvalsh(S))
    mults, cur = [], 1
    for a, b in zip(ev, ev[1:]):
        if abs(b - a) < 1e-7:
            cur += 1
        else:
            mults.append(cur)
            cur = 1
    mults.append(cur)
    sig = int(np.sum(ev > TOL) - np.sum(ev < -TOL))
    check("B4d  a generic SYMMETRIC base-linear carrier: every eigenvalue multiplicity divisible by 8",
          comm_res < 1e-8 and all(m % 8 == 0 for m in mults),
          f"multiplicities {mults}, commutation residual {comm_res:.1e}")
    check("B4e  hence base-linear signature lies in 8Z: literal count 3 UNREACHABLE under spacetime-scalar typing",
          sig % 8 == 0 and 3 not in {abs(sig)},
          f"signature {sig} -- clause E(c) of the p2c demand (declared base-typing) is load-bearing")


def main() -> None:
    part_a()
    part_b()
    log("")
    log("=" * 86)
    log("VERDICT")
    log("=" * 86)
    if not FAIL:
        log("Door A computable legs: the VEV/parity data are generation-blind (A1-A3: zero equations")
        log("on the condensate rank); the native 3 = dim Lambda^2_+(4-base) is exact and forced")
        log("conditional on d=4 (A4), and the physical half counts SIX 16-units, not three (A5).")
        log("Door B computable legs: BDI flow quantum 2 with odd kernels vs class-generic Kramers")
        log("quantum 4 with frozen count parity (B1); eta shifts by exactly twice the section charge")
        log("(B2); |count|=3 <=> |eta|=6 on the cited flow set (B3); base-linear carriers land in 8Z,")
        log("so the p2c section demand must declare non-base-scalar typing (B4).")
        log("\nRESULT: ALL PASS")
    else:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
