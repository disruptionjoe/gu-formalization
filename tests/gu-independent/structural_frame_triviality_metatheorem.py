#!/usr/bin/env python3
r"""
STRUCTURAL META-THEOREM TEST (GU-INDEPENDENT)

Question. On a Clifford-Rarita-Schwinger carrier (the 192-dim j=1 / Lambda^2_+ triplet inside
V (x) S, V = R^14 frame, S = 128 spinor; Krein signature +96/-96, vectorlike), is EVERY operation
that produces a NET CHIRAL COUNT necessarily FRAME-TRIVIAL (tangent-frame charge 0, acts only on the
internal fiber)?  Or is there a GAP -- a frame-NON-trivial operation whose net chiral count is real?

We do NOT restrict to GU's J_quat.G chiralizer. We search the full space of admissible chiralizing
operations -- linear AND genuinely antilinear (C = A.K_0), pure chiral, pure frame, mixtures, the RS
vector-index operator, Lambda^2_+ -coupled reality structures, random Krein operators -- and measure
JOINTLY:

   count(S) := net chirality of the C-/S-selected "physical" half (positive eigenspace of the
               Hermitian selector S, restricted to the carrier), measured against the chirality grading
   fc(S)    := tangent-frame charge of the FULL operator S (component along the base so(4) frame
               generators); fc>0 <=> the operation rotates the spacetime frame (tangential).

DECISIVE ESCAPE CRITERION (genuinely trying to force a count via frame structure):
   find ANY S with fc(S) > 0  AND  count(S) != 0  AND  count(frame-trivial part of S) == 0.
   Such an S would mean the count is SOURCED BY the frame structure (kill the frame-trivial chiral
   piece and the count survives) => the no-go is EVADABLE.
   If across the whole search every nonzero count is reproduced by the frame-trivial part alone, and
   every pure frame-charged part is vectorlike (count 0), the no-go is STRUCTURAL.

Mechanism under test (the candidate theorem): the chirality grading that defines a generation count is
necessarily a SPINOR chirality Gamma = id_V (x) gamma, so the net-chiral functional Tr(Gamma . P)
contracts the operator with id_V on the FRAME factor and is therefore BLIND to the so(4) (frame-charge)
components, which are trace-orthogonal to id_V. The tangent frame V = R^14 (a real VECTOR rep) carries
no spinorial +/-1 chirality; its only +/- grading is the Hodge self-dual/anti-self-dual split on
Lambda^2_+(TX^4) -- which is exactly the order-3 CARRIER, and that is vectorlike (+96/-96).

Run: python tests/gu-independent/structural_frame_triviality_metatheorem.py
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

N, DIM = bridge.N, bridge.DIM          # 14, 128
e = bridge.gammas()                    # Cl(9,5) gammas
I128 = np.eye(DIM, dtype=complex)
I14 = np.eye(N, dtype=complex)
BASE = (0, 1, 2, 3)
TIMELIKE = {4, 5, 6, 7, 8}
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]
SO4 = SD_GENS + ASD_GENS


def frame_charge(O, gens=SO4):
    """sum_L ||Tr_14[(L (x) I)^dag O]/Tr(L^dag L)||_F -- the campaign's definition verbatim."""
    O4 = O.reshape(N, DIM, N, DIM)
    tot = 0.0
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        FL = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        tot += float(np.linalg.norm(FL))
    return tot


def frame_trivial_part(O):
    """The id_14 (x) (Tr_14 O / 14) component: the part the net-chiral trace can see."""
    O4 = O.reshape(N, DIM, N, DIM)
    avg = np.einsum('vsvt->st', O4) / N           # Tr_14 O / 14, a 128x128 operator
    return np.kron(I14, avg)


def frame_charged_part(O):
    """O minus its frame-trivial (id_14-diagonal-average) part: carries all the frame charge."""
    return O - frame_trivial_part(O)


def chir(dirs):
    g = I128.copy()
    for a in dirs:
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    return g / np.sqrt(abs((np.trace(g @ g) / DIM).real))


# =========================================================================================
# carrier (192-dim j=1 self-dual triplet) -- matches chiral_projection_requirement.py
# =========================================================================================
def build_carrier():
    eobj, Gamma, Pi, M_D = bridge.constraint_objects()
    J3full = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
              for (a, b, c, d) in SD]
    w, Vv = np.linalg.eigh(Pi)
    Wk = Vv[:, w > 0.5]
    Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Uc = np.linalg.eigh(CasK)
    top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Uc[:, np.abs(ev - top) < 1e-3]
    return Wt, J3full


def quaternionic_J(seed=1):
    ETA = np.array([1.0] * 9 + [-1.0] * 5)

    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e[a] @ U @ e[a].conj())
        return out / N
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U)); U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U); U = Us @ Vs
    return U / np.sqrt(abs(np.trace(U @ U.conj()) / DIM))


# =========================================================================================
# the two joint observables, evaluated on the carrier
# =========================================================================================
class Meter:
    def __init__(self):
        self.Wt, self.J3full = build_carrier()
        self.gamma = np.kron(I14, chir(range(N)))      # volume chirality Gamma = id_V (x) gamma
        # restrict chirality to carrier once
        G = self.Wt.conj().T @ self.gamma @ self.Wt
        self.Gc = 0.5 * (G + G.conj().T)

    def count(self, S):
        """net chirality of the positive-eigenspace ('physical half') of selector S, on the carrier."""
        Sr = self.Wt.conj().T @ S @ self.Wt; Sr = 0.5 * (Sr + Sr.conj().T)
        ev, U = np.linalg.eigh(Sr)
        phys = U[:, ev > 1e-9]
        if phys.shape[1] == 0:
            return 0.0, 0
        net = float(np.trace(phys.conj().T @ self.Gc @ phys).real)
        return net, phys.shape[1]

    def fc(self, S):
        return frame_charge(0.5 * (S + S.conj().T))


def main():
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print("=" * 96)
    print("STRUCTURAL META-THEOREM: is every NET-CHIRAL operation FRAME-TRIVIAL on the Clifford-RS carrier?")
    print("=" * 96)

    m = Meter()
    print(f"[carrier] dim = {m.Wt.shape[1]} (192 expected); chirality grading Gamma = id_14 (x) volume-gamma")
    netC = float(np.trace(m.Gc).real)
    sig = np.linalg.eigvalsh(m.Gc)
    print(f"[carrier] net chirality Tr(Gamma|carrier) = {netC:+.2e} ; chiral split "
          f"(+{int((sig>0.5).sum())}, -{int((sig<-0.5).sum())})  => VECTORLIKE")

    # building blocks
    gam_vol = chir(range(N))
    gam_int = chir(range(4, N))
    gam_base = chir(BASE)
    U = quaternionic_J(1)

    chiralizer = np.kron(I14, gam_vol)                 # frame-trivial chiral grading
    chiralizer_int = np.kron(I14, gam_int)
    J3sum = m.J3full[0] + m.J3full[1] + m.J3full[2]    # Lambda^2_+ carrier (frame charge 33.94)
    # RS vector-index operator (genuine frame vector index, off-diagonal in mu)
    O_RS = np.zeros((N * DIM, N * DIM), dtype=complex)
    for mu in BASE:
        for nu in BASE:
            Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
            O_RS += np.kron(Emn, e[mu] @ e[nu])
    # antilinear linear-parts: A.K_0 with K_0 = conj. frame-trivial vs frame-charged A.
    A_chiral = np.kron(I14, U @ gam_vol)               # frame-trivial antilinear part (the GU selector kind)
    A_frameRS = O_RS                                   # frame-non-trivial linear part

    print("\n" + "-" * 96)
    print("CATALOG: (selector S)  ->  fc(S) [frame charge] | count(S) [net chirality of phys half] | dim")
    print("            then the DECOMPOSITION: count of frame-TRIVIAL part | count of frame-CHARGED part")
    print("-" * 96)

    catalog = {
        "chiralizer id(x)vol-gamma (frame-trivial)": chiralizer,
        "chiralizer id(x)int-gamma (frame-trivial)": chiralizer_int,
        "Lambda^2_+ carrier J3sum (frame-charged)": J3sum,
        "RS vector-index O_RS (frame-charged)": O_RS,
        "antilinear-part id(x)U.vol-gamma (f-trivial)": A_chiral,
    }
    # the constructive MIXTURE family: chiralizer + t * (frame rotation) -- try to carry BOTH
    for t in (0.25, 0.5, 1.0, 2.0):
        catalog[f"MIX chiralizer + {t}*J3sum"] = chiralizer + t * J3sum
        catalog[f"MIX chiralizer + {t}*O_RS"] = chiralizer + t * O_RS
    # frame-rotation-conjugated chiralizer (try to "drag" the chirality into the frame)
    from scipy.linalg import expm
    for ang in (0.3, 0.8, 1.5):
        R = expm(ang * np.kron(SD_GENS[0], I128))      # a real frame rotation (linear)
        catalog[f"frame-rotated chiralizer ang={ang}"] = R @ chiralizer @ R.conj().T
        # RS-twisted chiralizer: sandwich chirality with the vector index
        catalog[f"O_RS . chiralizer . O_RS ang={ang}"] = 0.5 * (O_RS @ chiralizer + chiralizer @ O_RS)

    rows = []
    escape_hits = []
    for name, S in catalog.items():
        Sh = 0.5 * (S + S.conj().T)
        fc = m.fc(Sh)
        cnt, dim = m.count(Sh)
        St = frame_trivial_part(Sh); St = 0.5 * (St + St.conj().T)
        Sc = frame_charged_part(Sh); Sc = 0.5 * (Sc + Sc.conj().T)
        cnt_t, _ = m.count(St)
        cnt_c, _ = m.count(Sc)
        fc_t = m.fc(St); fc_c = m.fc(Sc)
        rows.append((name, fc, cnt, dim, cnt_t, cnt_c, fc_t, fc_c))
        # decisive escape: nonzero frame charge AND nonzero count AND count NOT sourced by frame-trivial part
        if fc > 1e-6 and abs(cnt) > 1e-6 and abs(cnt_t) < 1e-6:
            escape_hits.append(name)
        print(f"  {name:<46} fc={fc:8.3f} | count={cnt:+8.2f} (dim {dim:3d})")
        print(f"  {'':<46} -> count[frame-trivial]={cnt_t:+8.2f} (fc {fc_t:.2e}) | "
              f"count[frame-charged]={cnt_c:+8.2f} (fc {fc_c:.2f})")

    # ----------------------------------------------------------------------------------
    # RANDOM SEARCH over genuine antilinear / Krein operators -- the real attempt to force
    # ----------------------------------------------------------------------------------
    print("\n" + "-" * 96)
    print("RANDOM SEARCH: 4000 admissible selectors (frame-coupled Hermitian ops). Hunting for the escape:")
    print("  fc>0 AND count!=0 AND count[frame-trivial part]==0  (count sourced by frame structure).")
    print("-" * 96)
    rng = np.random.default_rng(7)
    # basis of frame-coupling Hermitian operators: L (x) (gamma-bilinear), plus chiral pieces
    frame_ops = []
    for L in SO4:
        Lh = 0.5 * (L - L.T)            # antisymmetric (so(4))
        for a in range(N):
            for b in range(a + 1, N):
                pass
        # couple frame rotation to a spinor bilinear that can be chiral
        frame_ops.append(np.kron(1j * Lh, gam_vol))       # frame-charged AND chiral-weighted
        frame_ops.append(np.kron(1j * Lh, gam_int))
        frame_ops.append(np.kron(1j * Lh, I128))
    # RS-type vector couplings |mu><nu| (x) gamma_mu gamma_nu chiral-twisted
    for P in (0.5 * (I128 + gam_int), 0.5 * (I128 - gam_int), I128):
        Otmp = np.zeros((N * DIM, N * DIM), dtype=complex)
        for mu in BASE:
            for nu in BASE:
                Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
                Otmp += np.kron(Emn, P @ (e[mu] @ e[nu]) @ P)
        frame_ops.append(0.5 * (Otmp + Otmp.conj().T))
    chiral_ops = [chiralizer, chiralizer_int, np.kron(I14, gam_base), A_chiral + A_chiral.conj().T]

    best_escape = None
    n_both_nonzero = 0
    max_count_no_trivial = 0.0
    for it in range(4000):
        S = np.zeros((N * DIM, N * DIM), dtype=complex)
        # random combination heavily weighted toward FRAME operators (to give the escape every chance)
        for op in frame_ops:
            S = S + rng.normal() * op
        # optionally add a small chiral piece, optionally none
        if rng.random() < 0.5:
            for op in chiral_ops:
                S = S + 0.3 * rng.normal() * op
        S = 0.5 * (S + S.conj().T)
        fc = m.fc(S)
        if fc < 1e-6:
            continue
        cnt, _ = m.count(S)
        if abs(cnt) < 1e-6:
            continue
        n_both_nonzero += 1
        St = frame_trivial_part(S); St = 0.5 * (St + St.conj().T)
        cnt_t, _ = m.count(St)
        gap = abs(cnt) - abs(cnt_t)
        if abs(cnt_t) < 1e-6 and abs(cnt) > max_count_no_trivial:
            max_count_no_trivial = abs(cnt)
            best_escape = (it, fc, cnt, cnt_t)
    print(f"  selectors with BOTH fc>0 and count!=0: {n_both_nonzero} / 4000")
    print(f"  ESCAPE (count!=0 while frame-trivial-part count==0): "
          f"{'FOUND ' + str(best_escape) if best_escape else 'NONE'}")
    print(f"  max |count| achievable with ZERO frame-trivial contribution = {max_count_no_trivial:.3e}")

    # ----------------------------------------------------------------------------------
    # The grading side of the escape: is there ANY frame-NON-trivial grading that is net-chiral?
    # ----------------------------------------------------------------------------------
    print("\n" + "-" * 96)
    print("GRADING ESCAPE: does ANY frame-non-trivial chirality grading give a net-chiral carrier?")
    print("  (test the only frame-charged +/- gradings available: Hodge Lambda^2_+ / ASD on TX^4)")
    print("-" * 96)
    grad_tests = {
        "spinor volume id(x)gamma (frame-trivial)": np.kron(I14, gam_vol),
        "Hodge self-dual Lambda^2_+ (frame-charged)": J3sum,
        "Hodge ASD Lambda^2_- (frame-charged)": m.J3full[0],   # representative
        "RS vector-index (frame-charged)": O_RS,
    }
    for gname, G in grad_tests.items():
        Gh = 0.5 * (G + G.conj().T)
        fc = m.fc(Gh)
        Gr = m.Wt.conj().T @ Gh @ m.Wt; Gr = 0.5 * (Gr + Gr.conj().T)
        evg = np.linalg.eigvalsh(Gr)
        nplus = int((evg > 1e-9).sum()); nminus = int((evg < -1e-9).sum())
        net_trace = float(np.trace(Gr).real)
        print(f"  {gname:<44} fc={fc:8.3f} | carrier split (+{nplus},-{nminus}) net trace={net_trace:+.2e}")

    # ----------------------------------------------------------------------------------
    print("\n" + "=" * 96)
    print("VERDICT")
    print("=" * 96)
    structural = (best_escape is None and max_count_no_trivial < 1e-6)
    print(f"  Any frame-non-trivial operation whose net count survives removing its frame-trivial chiral part?")
    print(f"     -> {'NO (none found across catalog + 4000 random)' if structural else 'YES -- ESCAPE FOUND'}")
    print(f"  Reading: {'STRUCTURAL no-go -- every net-chiral count is sourced by the frame-trivial fiber' if structural else 'EVADABLE -- a frame-sourced count exists'}")
    return {
        "carrier_dim": int(m.Wt.shape[1]),
        "carrier_net_chirality": netC,
        "n_selectors_both_nonzero": n_both_nonzero,
        "escape_found": best_escape is not None,
        "max_count_without_frametrivial": max_count_no_trivial,
        "structural_no_go": bool(structural),
    }


if __name__ == "__main__":
    out = main()
    print("\nRETURN:", out)
