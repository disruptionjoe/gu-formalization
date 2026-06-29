#!/usr/bin/env python3
r"""
INDEPENDENT adversarial recheck of the RS frame-index forcing-slot claim.
Recompute every key number from the raw verified gammas; do NOT trust the construct's framing.
Specifically interrogate:
  (1) Is +256 a genuine CHIRAL INDEX (n+ - n-), or a tautological projector trace?
  (2) The physical-sector net chirality (the LEGITIMATE swing_ghost_parity-style measure).
  (3) Vectorlike SD=ASD frame coupling (tangential leg).
  (4) Hunt for a disguised 3 / chi=24 anywhere (192=2^6*3 triplet, 96=2^5*3 chiralizer).
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
I14 = np.eye(N, dtype=complex)
BASE = (0, 1, 2, 3)


def chir(dirs):
    g = I128.copy()
    for a in dirs:
        g = g @ e[a]
    if (np.trace(g @ g) / DIM).real < 0:
        g = 1j * g
    return g / np.sqrt(abs((np.trace(g @ g) / DIM).real))


g5i = chir(range(4, N))
g5b = chir(BASE)
P16 = 0.5 * (I128 + g5i)

print("=" * 80)
print("(0) Sanity: gammas square correctly, chirality projector idempotent")
print("=" * 80)
for a in BASE:
    sq = (e[a] @ e[a] / np.eye(DIM)[0, 0])
    print(f"   e[{a}]^2 = {np.trace(e[a]@e[a]).real/DIM:+.1f} * I (base Euclidean expect +1)")
print(f"   P16^2 - P16 norm = {np.linalg.norm(P16@P16 - P16):.2e}  (idempotent)")
print(f"   Tr P16 = {np.trace(P16).real:.1f}  (dim of chiral-16 sector; expect 64)")

# -------------------------------------------------------------------------
# THE OPERATOR TRACE +256: is it an index or a tautology?
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("(1) Is Tr(g5i . O_RS_tw)=+256 a chiral INDEX or a projector tautology?")
print("=" * 80)
# O_RS_tw = sum_mu,nu |mu><nu| (x) P16 e_mu e_nu P16
O_tw = np.zeros((N * DIM, N * DIM), dtype=complex)
for mu in BASE:
    for nu in BASE:
        Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
        O_tw += np.kron(Emn, P16 @ (e[mu] @ e[nu]) @ P16)
G_int = np.kron(I14, g5i)
tr = np.trace(G_int @ O_tw).real
print(f"   Tr(g5i . O_RS_tw) = {tr:+.1f}")
# Decompose: frame trace forces mu=nu, e_mu^2=+1, so = sum_mu Tr(g5i P16 P16) = 4*Tr(g5i P16)
# Tr(g5i P16) = Tr(g5i (1+g5i)/2) = (Tr g5i + Tr I)/2 = (0+128)/2 = 64 = +dim of P16 sector.
print(f"   Decomp: 4 * Tr(g5i P16) = 4 * {np.trace(g5i@P16).real:.0f}")
print(f"   Tr(g5i P16) = Tr(g5i on the +sector) = (+1)*dim(+sector) = +{int(np.trace(g5i@P16).real)}")
print("   READING: g5i restricted to the image of P16 is the IDENTITY (+1). So Tr(g5i P16)")
print("   literally COUNTS the +chirality subspace dimension. After you sandwich by P16, the")
print("   operator lives ONLY on the +sector, so 'measuring its chirality' returns +dim, by")
print("   construction. n+ = 64, n- = 0 is FORCED by the P16 sandwich, not measured.")
# Show the negative-chirality content was deleted by the sandwich:
P16bar = 0.5 * (I128 - g5i)
leak = np.linalg.norm(P16bar @ (P16 @ (e[0]@e[1]) @ P16) @ P16bar)
print(f"   minus-sector content of a sandwiched block ||P16bar(.)P16bar|| = {leak:.2e} (deleted)")

# -------------------------------------------------------------------------
# THE LEGITIMATE physical-sector net chirality (swing_ghost_parity style)
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("(2) LEGITIMATE physical-sector net chirality on the 192 triplet (their own method)")
print("=" * 80)


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1.0; M[j, i] = -1.0; return M


Gam = np.hstack(e)
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J3 = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
      for (a, b, c, d) in SD]
w, Vv = np.linalg.eigh(Pi); Wk = Vv[:, w > 0.5]
Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
ev, Uu = np.linalg.eigh(CasK); top = max(round(x.real, 3) for x in ev)
Wt = Wk @ Uu[:, np.abs(ev - top) < 1e-3]
print(f"   triplet dim = {Wt.shape[1]}  (192 = 2^6 * 3 -- note the lurking factor 3)")


def phys_net(grading_full, chir_full):
    G = Wt.conj().T @ grading_full @ Wt; G = 0.5 * (G + G.conj().T)
    C = Wt.conj().T @ chir_full @ Wt; C = 0.5 * (C + C.conj().T)
    kev, kU = np.linalg.eigh(G)
    phys = kU[:, kev > 1e-9]
    if phys.shape[1] == 0:
        return 0.0, 0, 0, 0
    cc = phys.conj().T @ C @ phys; cc = 0.5 * (cc + cc.conj().T)
    cev = np.linalg.eigvalsh(cc)
    return float(np.trace(cc).real), int(np.sum(cev > 1e-6)), int(np.sum(cev < -1e-6)), phys.shape[1]


for nm, Cg in [("internal", np.kron(I14, g5i)), ("base", np.kron(I14, g5b))]:
    net, npp, nmm, dd = phys_net(O_tw, Cg)
    print(f"   O_RS_tw physical-sector net chirality [{nm:>8} grading] = {net:+.1f} "
          f"sig(+{npp},-{nmm}) physdim {dd}")
print("   => the ONLY honest net-chirality measure gives 0 / empty sector for the RS operator.")
print("      The construct's 'net_chiral: yes' rests entirely on the projector-tautology trace.")

# -------------------------------------------------------------------------
# Frame coupling: vectorlike SD=ASD (tangential leg)
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("(3) Frame coupling self-dual vs anti-self-dual (tangential / p1 leg)")
print("=" * 80)
SD_GENS = [lvec(0, 1) + lvec(2, 3), lvec(0, 2) + lvec(3, 1), lvec(0, 3) + lvec(1, 2)]
ASD_GENS = [lvec(0, 1) - lvec(2, 3), lvec(0, 2) - lvec(3, 1), lvec(0, 3) - lvec(1, 2)]


def fc(O, gens):
    O4 = O.reshape(N, DIM, N, DIM); tot = 0.0
    for L in gens:
        nrm = np.tensordot(L.conj(), L, axes=([0, 1], [0, 1])).real
        FL = np.einsum('vw,vswt->st', L.conj(), O4) / nrm
        tot += float(np.linalg.norm(FL))
    return tot


O_un = np.zeros((N * DIM, N * DIM), dtype=complex)
for mu in BASE:
    for nu in BASE:
        Emn = np.zeros((N, N), dtype=complex); Emn[mu, nu] = 1.0
        O_un += np.kron(Emn, e[mu] @ e[nu])
for tag, O in [("O_RS untwisted", O_un), ("O_RS twisted", O_tw)]:
    sd, asd = fc(O, SD_GENS), fc(O, ASD_GENS)
    print(f"   {tag:<16}: SD={sd:.3f} ASD={asd:.3f}  net(SD-ASD)={sd-asd:+.3f}  total={sd+asd:.3f}")
print("   => net self-dual = 0 (vectorlike). NO net p1 => FAILS tangential leg (a).")

# -------------------------------------------------------------------------
# Disguised-3 hunt
# -------------------------------------------------------------------------
print("\n" + "=" * 80)
print("(4) Disguised-3 / chi=24 hunt")
print("=" * 80)
def pf(n):
    n=abs(int(round(n)));
    if n<=1: return str(n)
    o=[];d=2
    while d*d<=n:
        k=0
        while n%d==0: n//=d;k+=1
        if k:o.append(f"{d}^{k}" if k>1 else f"{d}")
        d+=1
    if n>1:o.append(str(n))
    return ".".join(o)
for label,val in [("net trace +256",256),("triplet dim 192",192),("chiralizer +96",96),
                  ("Tr P16 = 64",64),("V(x)S 1792",1792),("chi(K3) 24",24)]:
    n=abs(val); k=0; t=n
    while t%3==0: t//=3;k+=1
    print(f"   {label:<18} = {pf(val):<10} 3-part={3**k}  ==24?{n==24} %24=={n%24==0}")
print("   256 has NO factor of 3. The factor-3 carriers (192, 96) are either the ambient")
print("   sector dim or the FRAME-TRIVIAL chiralizer -- neither reaches the tangential net-chiral slot.")
