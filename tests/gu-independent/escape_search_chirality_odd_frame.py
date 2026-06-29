#!/usr/bin/env python3
r"""
ESCAPE SEARCH v2 (GU-INDEPENDENT) -- the genuine constructive attempt to FORCE a frame-sourced count.

Baseline weakness fixed: a selector that ROTATES the frame can only bias the chiral count if it also
FLIPS spinor chirality (anticommutes, in part, with Gamma = id_V (x) gamma). Frame rotations alone
commute with the spinor chirality, so they leave the carrier balanced. The real escape candidates are
CHIRALITY-ODD frame-coupled operators: L (x) gamma_a (single gamma), the Dirac/gamma-trace operator
|mu><nu| (x) gamma_mu, etc. -- operators that simultaneously rotate the tangent frame AND exchange the
two spinor chiralities. We build a rich basis of such operators and search HARD (50k random Hermitian
combinations) for the decisive escape:

    fc(S) > 0  AND  count(S) != 0  AND  count(frame-trivial part of S) == 0.

Speed: every observable is precomputed as a linear functional of the coefficient vector, so the search
is matrix-cheap. count needs one 192x192 eigh per sample; fc and count_triv are O(basis) assembles.

Run: python tests/gu-independent/escape_search_chirality_odd_frame.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
for p in (os.path.normpath(os.path.join(HERE, "..")),
          os.path.normpath(os.path.join(HERE, "..", "generation-sector"))):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as bridge  # noqa: E402

N, DIM = bridge.N, bridge.DIM
e = bridge.gammas()
I128 = np.eye(DIM, dtype=complex)
I14 = np.eye(N, dtype=complex)
BASE = (0, 1, 2, 3)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
SO4 = SD_GENS + ASD_GENS


def chir(dirs):
    g = I128.copy()
    for a in dirs:
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    return g / np.sqrt(abs((np.trace(g @ g) / DIM).real))


def herm(M):
    return 0.5 * (M + M.conj().T)


def frame_trivial_part(O):
    O4 = O.reshape(N, DIM, N, DIM)
    avg = np.einsum('vsvt->st', O4) / N
    return np.kron(I14, avg)


def FL_components(O):
    """per-generator frame-charge functionals FL (128x128) for each L in SO4."""
    O4 = O.reshape(N, DIM, N, DIM)
    out = []
    for L in SO4:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        out.append(np.einsum('vw,vswt->st', L.conj(), O4) / nrm)
    return out


def build_carrier():
    eobj, Gamma, Pi, M_D = bridge.constraint_objects()
    J3full = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
              for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = herm(Wk.conj().T @ Cas @ Wk)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]
    return Wt, J3full


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print("=" * 96)
    print("ESCAPE SEARCH v2: chirality-ODD frame-coupled selectors -- can frame structure SOURCE a count?")
    print("=" * 96)
    Wt, J3full = build_carrier()
    gam_vol = chir(range(N)); gam_int = chir(range(4, N)); gam_base = chir(BASE)
    Gamma_full = np.kron(I14, gam_vol)
    Gc = herm(Wt.conj().T @ Gamma_full @ Wt)
    print(f"[carrier] dim {Wt.shape[1]}; chirality Gamma = id_14 (x) gamma_vol")

    # ---------------- operator basis -------------------------------------------------------
    basis = {}
    # (A) frame-trivial chiral gradings (the legitimate count source)
    basis["id(x)gam_vol"] = np.kron(I14, gam_vol)
    basis["id(x)gam_int"] = np.kron(I14, gam_int)
    basis["id(x)gam_base"] = np.kron(I14, gam_base)
    # (B) frame-charged, chirality-EVEN (Lambda^2_+ carrier + RS vector index gamma_mu gamma_nu)
    for k, J in enumerate(J3full):
        basis[f"J3_{k}"] = herm(J)
    O_RS = np.zeros((N * DIM, N * DIM), dtype=complex)
    for mu in BASE:
        for nu in BASE:
            Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
            O_RS += np.kron(Emn, e[mu] @ e[nu])
    basis["O_RS(even)"] = herm(O_RS)
    # (C) frame-charged, chirality-ODD : L (x) gamma_a (single gamma) -- rotates frame AND flips chirality
    nodd = 0
    for (i, j) in [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (1, 3)]:
        for a in range(N):
            Op = herm(np.kron(1j * lvec(i, j), e[a]))
            if np.linalg.norm(Op) > 1e-9:
                basis[f"L{i}{j}(x)g{a}"] = Op
                nodd += 1
    # (D) Dirac / gamma-trace operator (the genuine RS vector index, chirality-odd):
    #     D = sum_mu |mu><b| (x) gamma_mu + h.c.  -- couples frame direction to its own gamma
    for b in BASE:
        Dop = np.zeros((N * DIM, N * DIM), dtype=complex)
        for mu in range(N):
            Emn = np.zeros((N, N), dtype=complex); Emn[mu, b] = 1.0
            Dop += np.kron(Emn, e[mu])
        basis[f"Dirac_b{b}(odd)"] = herm(Dop)

    names = list(basis.keys())
    ops = [basis[n] for n in names]
    nb = len(ops)
    print(f"[basis] {nb} operators: 3 frame-trivial chiral, {3+1} frame-charged even, "
          f"{nodd} chirality-ODD L(x)gamma, 4 Dirac(odd)")

    # ---------------- precompute linear functionals ----------------------------------------
    R = [herm(Wt.conj().T @ O @ Wt) for O in ops]                  # restricted selectors (192x192)
    T = [herm(Wt.conj().T @ frame_trivial_part(O) @ Wt) for O in ops]   # restricted frame-trivial parts
    FLk = [FL_components(O) for O in ops]                          # per-op list of 6 (128x128) FL mats
    # Gamma commute/anticommute structure per op -- CHEAP version: gamma_vol is diagonal in the
    # eigenbasis; classify each op by parity using the precomputed FL/restriction is not enough, so
    # we test the (sparse-friendly) products only on a representative subset, plus full only for the
    # few frame-EVEN ops. Most ops are either pure commute or pure anticommute by construction.
    print("\n[diagnostic] Gamma-parity of representative frame ops (cheap: einsum on reshaped blocks):")
    gv = gam_vol  # 128x128
    def parity_tag(O):
        # [O, id(x)gv] in V(x)S: block-wise O4[v,:,w,:] commutator with gv. Cheap 128-dim matmuls.
        O4 = O.reshape(N, DIM, N, DIM)
        cc = 0.0; aa = 0.0
        for v in range(N):
            for w in range(N):
                B = O4[v, :, w, :]
                cc += np.linalg.norm(B @ gv - gv @ B)
                aa += np.linalg.norm(B @ gv + gv @ B)
        return ("commutes" if cc < 1e-6 else ("anticommutes" if aa < 1e-6 else "mixed")), cc, aa
    for n in ["J3_0", "O_RS(even)", "L01(x)g0", "L01(x)g4", "Dirac_b0(odd)"]:
        if n in basis:
            tg, cc, aa = parity_tag(basis[n])
            print(f"     {n:<16} ||[.,G]||={cc:8.2f}  ||{{.,G}}||={aa:8.2f}  -> {tg}")

    def count_from_restricted(Sr):
        ev, U = np.linalg.eigh(herm(Sr))
        phys = U[:, ev > 1e-9]
        if phys.shape[1] == 0:
            return 0.0
        return float(np.trace(phys.conj().T @ Gc @ phys).real)

    def fc_from_coeffs(c):
        tot = 0.0
        for L in range(len(SO4)):
            acc = np.zeros((DIM, DIM), dtype=complex)
            for k in range(nb):
                acc += c[k] * FLk[k][L]
            tot += float(np.linalg.norm(acc))
        return tot

    # ---------------- targeted single-operator readout ------------------------------------
    print("\n[single-op readout] fc | count | count(frame-trivial part)")
    for k, n in enumerate(names):
        cvec = np.zeros(nb); cvec[k] = 1.0
        fc = fc_from_coeffs(cvec)
        cnt = count_from_restricted(R[k])
        cntt = count_from_restricted(T[k])
        flag = "  <== ESCAPE?" if (fc > 1e-6 and abs(cnt) > 1e-6 and abs(cntt) < 1e-6) else ""
        if (not n.startswith("id(")) or abs(cnt) > 1e-6:
            print(f"   {n:<16} fc={fc:8.3f} | count={cnt:+8.2f} | count_triv={cntt:+8.2f}{flag}")

    # ---------------- HARD random search ---------------------------------------------------
    print("\n[hard search] 50000 random Hermitian combinations weighted toward frame-charged + odd ops")
    rng = np.random.default_rng(11)
    # index sets
    idx_chiral = [i for i, n in enumerate(names) if n.startswith("id(")]
    idx_frame = [i for i, n in enumerate(names) if not n.startswith("id(")]
    n_both = 0
    escape = None
    max_count_zero_triv = 0.0
    best_gap = -1.0
    best_gap_rec = None
    for it in range(50000):
        c = np.zeros(nb)
        # always give frame-charged ops strong weight (the escape must be frame-sourced)
        for i in idx_frame:
            c[i] = rng.normal()
        # half the time add chiral pieces, half the time NONE (pure frame-sourced attempt)
        include_chiral = rng.random() < 0.5
        if include_chiral:
            for i in idx_chiral:
                c[i] = 0.5 * rng.normal()
        fc = fc_from_coeffs(c)
        if fc < 1e-6:
            continue
        Sr = sum(c[k] * R[k] for k in range(nb))
        cnt = count_from_restricted(Sr)
        if abs(cnt) < 1e-6:
            continue
        n_both += 1
        St = sum(c[k] * T[k] for k in range(nb))
        cntt = count_from_restricted(St)
        gap = abs(cnt) - abs(cntt)
        if gap > best_gap:
            best_gap = gap; best_gap_rec = (it, fc, cnt, cntt)
        if abs(cntt) < 1e-6 and abs(cnt) > max_count_zero_triv:
            max_count_zero_triv = abs(cnt)
            escape = (it, fc, cnt, cntt)
    print(f"   samples with fc>0 AND count!=0 : {n_both} / 50000")
    print(f"   max |count| with count_triv==0 (FRAME-SOURCED count) : {max_count_zero_triv:.3e}")
    print(f"   ESCAPE record : {escape}")
    print(f"   max (|count| - |count_triv|) gap : {best_gap:.3e}  at {best_gap_rec}")

    structural = (escape is None and max_count_zero_triv < 1e-6)
    print("\n" + "=" * 96)
    print("VERDICT")
    print("=" * 96)
    if structural:
        print("  STRUCTURAL NO-GO: no selector -- including chirality-odd frame-coupled and Dirac/gamma-trace")
        print("  operators -- produces a net chiral count that survives deleting its frame-trivial part.")
        print("  Every nonzero count is reproduced by the frame-trivial (internal-fiber) component alone;")
        print("  the frame charge is inert for the count. The frame-triviality of the chiralizer is STRUCTURAL.")
    else:
        print("  EVADABLE: a frame-non-trivial, frame-SOURCED net chiral count exists. Escape found:")
        print(f"     {escape}")
    return {
        "carrier_dim": int(Wt.shape[1]),
        "basis_size": nb,
        "n_chirality_odd_frame_ops": nodd,
        "samples_both_nonzero": n_both,
        "max_count_with_zero_frametrivial": max_count_zero_triv,
        "best_count_minus_counttriv_gap": best_gap,
        "escape_found": escape is not None,
        "structural_no_go": bool(structural),
    }


if __name__ == "__main__":
    out = main()
    print("\nRETURN:", out)
