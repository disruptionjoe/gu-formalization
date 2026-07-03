#!/usr/bin/env python3
r"""
R1 BIG-SWING (B) -- the KILL attempt, on the ACTUAL carrier.

Target: construct (or prove impossible) a covariant operator INTERIOR to the delimited
class C -- real Cl(p,q), p+q=14, gamma-traceless rank-3/2 field, the j=1 self-dual triplet
carrying the cross-chirality (+96,-96) Krein form, equivariant under the sector's split
symmetry so(4) (+) so(10) -- that FORCES an ODD net chiral count. Such an operator would
break Theorem 1 / the 2-primary structural law.

REDUCTION (rigorous, proved in the header comment, checked in code):
  Chirality Gamma_15 (the full 14-dim chirality) is central in the even Clifford algebra,
  hence commutes with so(4) (+) so(10). So each so(4)+so(10)-IRREDUCIBLE subrep of the
  192-dim carrier W lies entirely in W+ or in W- (Schur: Gamma is a scalar on it). Writing
  the carrier as  W = (+)_R [ a_R copies of R in W+ ] (+) [ b_R copies of R in W- ], any
  EQUIVARIANT projector P has net chiral count
        chi(P) = tr(Gamma P) = sum_R d_R (k_R - l_R),   0<=k_R<=a_R, 0<=l_R<=b_R,
  where d_R = dim R. The set of ACHIEVABLE net chiral counts is therefore the integer lattice
  { sum_R d_R (k_R - l_R) }. Its PARITY is odd for some choice IFF there exists an irrep R with
  d_R ODD that actually appears (a_R + b_R >= 1). Equivalently:

     *** an odd covariant net chiral count is possible  <=>  the carrier contains an
         ODD-DIMENSIONAL so(4)+so(10) irrep. ***

  (This also covers the antilinear / re-grading escapes: any equivariant grading is an
   equivariant projector, same lattice; a chirality-odd equivariant operator has index
   dim W+ - dim W- = 0 by rank-nullity, so the only route to a nonzero count is an equivariant
   RE-GRADING projector, exactly the tr(Gamma P) computed here.)

So the KILL is DECIDABLE: enumerate the irrep dimensions of the carrier. If any is odd, probe
it for a genuine forced odd count; if all are even, the KILL is impossible interior to C and the
2-primary law is HARDENED (from the census's generator list to a table-free parity theorem).

Method (table-free, no so(10) Casimir table imported):
  - Build the carrier from EUCLIDEAN (14,0) gammas. The isotypic content of W as a COMPLEX
    rep of so(4)_C (+) so(10)_C is signature-independent (the real form only changes the
    invariant/Krein form, verified separately in net_chiral_index_invariant.py); Euclidean
    gammas make every Casimir Hermitian so the decomposition is clean and real-eigenvalued.
  - Split W into JOINT eigenblocks of the commuting Casimirs (so(4), so(10), and su(2)_+, su(2)_-).
  - For each block, recover the irrep dimension d_R WITHOUT any lookup table, via
        m_R = sqrt( dim commutant of {generators restricted to block} ),   d_R = (block dim)/m_R,
    (Schur: on an isotypic block the commutant is M_{m_R}(C), dimension m_R^2).
  - Read off chirality (Gamma constant on each irrep block) -> a_R (in W+) and b_R (in W-).
  - Search the achievable-count lattice for an ODD value. Report FOUND (=> KILL) or NOT FOUND.

Covariances tested (weakest wins the strongest no-go): so(4)+so(10); su(2)_+ + so(10); so(10) alone.

Run: python tests/big-swing/R1_kill_odd_index_isotypic.py
"""
from __future__ import annotations
import os, sys, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tests"))
sys.path.insert(0, os.path.join(REPO, "tests", "generation-sector"))
import oq_rk1_cl95_explicit_rep as cl95  # verified Cl gamma construction

N, DIM = 14, 128
BASE = [0, 1, 2, 3]
INTERNAL = list(range(4, 14))
TOL = 1e-7


def euclidean_gammas():
    """All-Hermitian (14,0) gammas -- clean rep-theory substrate (signature-independent isotypic)."""
    G = cl95.jordan_wigner_gammas(7)  # 14 Hermitian gammas, {G_a,G_b}=2 delta
    return [G[a] for a in range(N)]


def sg(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


def so_gens_restricted(e, idx, Wt):
    """so(k) generators J_ij = kron(I14, sg_ij) + kron(lvec_ij, I128), restricted to the carrier
    Wt (columns), computed WITHOUT materializing the 1792x1792 operators (einsum on reshaped Wt).
    Wt : (N*DIM) x 192.  Returns list of 192x192 restricted generators."""
    n = Wt.shape[1]
    W4 = Wt.reshape(N, DIM, n)            # [v, s, c]
    Wc = W4.conj()
    G = []
    for a in range(len(idx)):
        for b in range(a + 1, len(idx)):
            i, j = idx[a], idx[b]
            s_ij = sg(e, i, j)             # 128x128 spinor part
            l_ij = lvec(i, j)             # 14x14 vector part
            # spinor part: sum_{v,s,s'} conj(W[v,s,c]) s_ij[s,s'] W[v,s',c']
            Rs = np.einsum('vsc,st,vtd->cd', Wc, s_ij, W4, optimize=True)
            # vector part: sum_{v,v',s} conj(W[v,s,c]) l_ij[v,v'] W[v',s,d]
            Rv = np.einsum('vsc,vw,wsd->cd', Wc, l_ij, W4, optimize=True)
            G.append(Rs + Rv)
    return G


def build_carrier(e):
    """Return (Wt, Gamma) : Wt columns = orthonormal basis of the 192-dim j=1 self-dual triplet
    inside V(x)S; Gamma = full 14-chirality restricted to the carrier (the generation grading)."""
    I128 = np.eye(DIM, dtype=complex)
    I14 = np.eye(N, dtype=complex)
    # gamma-trace kernel Pi (the RS constraint)
    Gam = np.hstack(e)  # 128 x (14*128)
    Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    # self-dual su(2)_+ generators J[k] on V(x)S
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J = [np.kron(I14, sg(e, a, b) + sg(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]
    # restrict to Pi-kernel, then pick the top su(2)_+ Casimir eigenspace (j=1 triplet)
    w, V = np.linalg.eigh(Pi); Wk = V[:, w > 0.5]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
    ev, Ue = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
    Wt = Wk @ Ue[:, np.abs(ev - top) < 1e-3]
    Wt, _ = np.linalg.qr(Wt)  # orthonormal
    # full chirality
    om = I128.copy()
    for a in range(N):
        om = om @ e[a]
    om = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
    chir = np.kron(I14, om)
    Gt = Wt.conj().T @ chir @ Wt; Gt = 0.5 * (Gt + Gt.conj().T)
    return Wt, Gt


def restrict(Wt, ops):
    return [Wt.conj().T @ O @ Wt for O in ops]


def _gcd_list(xs):
    from math import gcd
    g = 0
    for x in xs:
        g = gcd(g, int(x))
    return g


def block_mult(gens, rng, tol=1e-4):
    """Multiplicity m_R of the (single) irrep filling an isotypic block that is R^{(+)m_R}.
    Cheap method: a generic Hermitian combination H = sum c_i (i g_i) acts as rho(x) (x) I_m,
    so every eigenvalue (weight of R) has degeneracy that is a multiple of m_R and generically
    EXACTLY m_R. So m_R = gcd of the eigenvalue degeneracies. No d^2 kron, no big SVD."""
    d = gens[0].shape[0]
    H = np.zeros((d, d), dtype=complex)
    for g in gens:
        H += rng.standard_normal() * (1j * g)
    H = 0.5 * (H + H.conj().T)
    ev = np.linalg.eigvalsh(H)
    # cluster eigenvalues
    ev = np.sort(ev.real)
    degs = []
    i = 0
    scale = max(1.0, np.abs(ev).max())
    while i < d:
        j = i + 1
        while j < d and abs(ev[j] - ev[i]) < tol * scale:
            j += 1
        degs.append(j - i)
        i = j
    m = _gcd_list(degs)
    return max(m, 1)


def joint_casimir_blocks(gens_by_algebra, dim, extra_seps=None, tol=1e-5):
    """Split C^dim into simultaneous eigenblocks of the quadratic Casimirs of each subalgebra
    (plus any extra commuting Hermitian separators, e.g. the internal so(10) chirality that
    distinguishes 16 from 16bar -- they share a quadratic Casimir).
    Returns list of (basis-block, mean-eigenvalue)."""
    rng = np.random.default_rng(1)
    Csum = np.zeros((dim, dim), dtype=complex)
    for gens in gens_by_algebra:
        C = np.zeros((dim, dim), dtype=complex)
        for g in gens:
            C += (-1.0) * (g @ g)  # -sum g^2 : Hermitian positive (g anti-Hermitian)
        C = 0.5 * (C + C.conj().T)
        Csum += rng.uniform(0.5, 1.5) * C
    for S in (extra_seps or []):
        S = 0.5 * (S + S.conj().T)
        Csum += rng.uniform(0.5, 1.5) * S
    Csum = 0.5 * (Csum + Csum.conj().T)
    ev, U = np.linalg.eigh(Csum)
    blocks = []
    i = 0
    while i < dim:
        j = i + 1
        while j < dim and abs(ev[j] - ev[i]) < tol:
            j += 1
        blocks.append((U[:, i:j], ev[i:j].mean()))
        i = j
    return blocks


def analyze(name, gens_by_algebra, Gt, extra_seps=None):
    """Full isotypic analysis under the given covariance. Returns achievable-parity report.
    Splits by the generation grading Gamma (full Gamma_15) FIRST -- each irrep sits in a definite
    chirality by Schur -- then decomposes each chirality sector into isotypic blocks using the
    quadratic Casimir(s) plus extra separators (i*om_int distinguishes conjugate irreps 16/16bar
    that share a quadratic Casimir). Within each isotypic block, m_R = gcd of generic-weight
    degeneracies (table-free), d_R = blockdim / m_R."""
    from collections import defaultdict
    dim = Gt.shape[0]
    allgens = [g for gens in gens_by_algebra for g in gens]
    rng = np.random.default_rng(7)
    print(f"\n=== covariance: {name} ===")
    Gh = 0.5 * (Gt + Gt.conj().T)
    gev, gU = np.linalg.eigh(Gh)
    chir_sectors = [("W+", gU[:, gev > 0.5]), ("W-", gU[:, gev < -0.5])]
    agg = defaultdict(lambda: [0, 0])  # d -> [copies in W+, copies in W-]
    tot_comm = 0
    total = 0
    for ci, (clab, P) in enumerate(chir_sectors):  # P: dim x 96 basis of the chirality sector
        gens_c = [P.conj().T @ g @ P for g in allgens]
        seps_c = [P.conj().T @ S @ P for S in (extra_seps or [])]
        blocks = joint_casimir_blocks([gens_c], P.shape[1], extra_seps=seps_c)
        for (B, lam) in blocks:  # B: 96 x gd  basis within the chirality sector
            gsub = [B.conj().T @ g @ B for g in gens_c]
            m = block_mult(gsub, rng)
            gd = B.shape[1]
            if gd % max(m, 1) != 0:
                m = 1
            d = gd // m
            tot_comm += m * m
            total += gd
            agg[d][ci] += m
    print(f"  total commutant dim (sum m_R^2) = {tot_comm}  (census cross-check)")
    print("  irrep-dim census (table-free; chirality-split; d_R = blockdim / m_R):")
    odd_dim_present = False
    for d in sorted(agg):
        a, b = agg[d]
        parity = "ODD" if d % 2 == 1 else "even"
        flag = "   <== ODD-DIM IRREP (parity crack!)" if d % 2 == 1 and (a + b) > 0 else ""
        if d % 2 == 1 and (a + b) > 0:
            odd_dim_present = True
        print(f"     d_R = {d:>4} [{parity}] : copies in W+ = {a}, in W- = {b}{flag}")
    assert total == dim, (total, dim)
    # achievable net-count parity search
    # odd achievable <=> exists odd-dim irrep present (proof in header)
    # do an explicit brute lattice check as an independent confirmation (small):
    achievable_parities = set()
    # net = sum_R d_R (k_R - l_R). Parity only depends on odd-d irreps' (k-l) parity.
    odd_ds = [(d, a, b) for d, (a, b) in agg.items() if d % 2 == 1 and (a + b) > 0]
    if not odd_ds:
        achievable_parities = {0}
    else:
        for combo in itertools.product(*[range(-b, a + 1) for (d, a, b) in odd_ds]):
            s = sum(c for c in combo)  # d odd => contributes c mod 2
            achievable_parities.add(s % 2)
    can_odd = 1 in achievable_parities
    print(f"  achievable net-chiral-count parities = {sorted(achievable_parities)}")
    print(f"  >>> ODD covariant count possible under {name}: {can_odd}  "
          f"({'KILL' if can_odd else 'no interior odd count'})")
    return can_odd, dict(agg)


def main():
    print("=" * 88)
    print("R1 KILL ATTEMPT (B): can a covariant operator interior to class C force an ODD count?")
    print("Reduction: odd covariant count possible  <=>  carrier has an ODD-DIM so(4)+so(10) irrep.")
    print("=" * 88)
    e = euclidean_gammas()
    Wt, Gt = build_carrier(e)
    dim = Gt.shape[0]
    gvals = np.linalg.eigvalsh(0.5 * (Gt + Gt.conj().T))
    print(f"\ncarrier dim = {dim} (expect 192); W+ dim = {(gvals>0.5).sum()}, "
          f"W- dim = {(gvals<-0.5).sum()} (expect 96, 96)")
    assert dim == 192, dim
    assert (gvals > 0.5).sum() == 96 and (gvals < -0.5).sum() == 96

    so4 = so_gens_restricted(e, BASE, Wt)
    so10 = so_gens_restricted(e, INTERNAL, Wt)
    # su(2)_+ (self-dual) generators inside so(4): J_k = kron(I14, sg_ab+sg_cd) + kron(lvec_ab+lvec_cd, I128)
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    n = Wt.shape[1]; W4 = Wt.reshape(N, DIM, n); Wc = W4.conj()
    sup = []
    for (a, b, c, d) in SD:
        s_op = sg(e, a, b) + sg(e, c, d)
        l_op = lvec(a, b) + lvec(c, d)
        Rs = np.einsum('vsc,st,vtd->cd', Wc, s_op, W4, optimize=True)
        Rv = np.einsum('vsc,vw,wsd->cd', Wc, l_op, W4, optimize=True)
        sup.append(Rs + Rv)

    # internal so(10) chirality (product of the 10 internal gammas), restricted to carrier:
    # commutes with so(4)+so(10); distinguishes 16 from 16bar (same quadratic Casimir).
    # 10 gammas => om_int^2 = -1 (anti-Hermitian), so use i*om_int to get a Hermitian +-1 separator.
    om_int = np.eye(DIM, dtype=complex)
    for a in INTERNAL:
        om_int = om_int @ e[a]
    om_int = 1j * om_int  # Hermitian, eigenvalues +-1 => internal chirality operator
    OmInt = np.einsum('vsc,st,vtd->cd', Wc, om_int, W4, optimize=True)
    OmInt = 0.5 * (OmInt + OmInt.conj().T)

    results = {}
    results["so(10) alone"] = analyze("so(10) alone  (WEAKEST covariance => most permissive => decisive)",
                                      [so10], Gt, extra_seps=[OmInt])
    results["su(2)_+ + so(10)"] = analyze("su(2)_+ + so(10)", [sup, so10], Gt, extra_seps=[OmInt])
    results["so(4)+so(10)"] = analyze("so(4)+so(10)  (class-C covariance)", [so4, so10], Gt, extra_seps=[OmInt])

    print("\n" + "=" * 88)
    print("VERDICT (R1 KILL ATTEMPT)")
    print("=" * 88)
    any_kill = any(v[0] for v in results.values())
    for name, (can_odd, agg) in results.items():
        odd_irreps = {d: ab for d, ab in agg.items() if d % 2 == 1 and sum(ab) > 0}
        print(f"  {name:<20}: odd count possible = {can_odd}; odd-dim irreps present = "
              f"{odd_irreps if odd_irreps else 'NONE'}")
    if any_kill:
        print("\n  *** KILL: an odd-dimensional interior irrep exists -> a covariant operator CAN")
        print("      force an odd count. Theorem 1 / the 2-primary law is BROKEN. ***")
    else:
        print("\n  NO KILL. Under every sector-interior covariance the carrier contains ONLY")
        print("  EVEN-DIMENSIONAL irreps, so EVERY covariant net chiral count is even. The odd count")
        print("  is arithmetically unreachable interior to class C -- Theorem 1 HARDENED from the")
        print("  census's enumerated generator list to a table-free parity theorem on the actual carrier.")
    # guards
    assert not any_kill, "if this fires, a genuine KILL was found -- investigate"
    print("\n[OK] KILL attempt completed; no odd interior count exists (no-go hardened).")
    return results


if __name__ == "__main__":
    main()
