"""Lean decisive-number extraction for the BV/BRST SW-compensator gate (fast path).
Computes ONLY: anchors, the escape=C2/sqrt(N) identity, the SW compensator chirality grading,
the decisive escape-minimization scan (precomputed, affine), and the chirality decomposition.
Skips the 3840-dim BV s^2 assembly and the expm holonomy scan (those are in the full artifact
sw_bv_master_equation_c2.py). Reuses build_substrate from that file."""
import numpy as np
import sw_bv_master_equation_c2 as M

fro = M.fro
N, DIM = M.N, M.DIM

e, Gamma, Pi_RS, M_D, J, W_trip, K, chir = M.build_substrate()
VS = N * DIM
I_VS = np.eye(VS, dtype=complex)
Pi_perp = I_VS - Pi_RS

anti_trap = fro(Pi_RS @ M_D - M_D @ Pi_RS)
escape0 = fro(Pi_perp @ M_D @ Pi_RS)
C2_0 = fro(Gamma @ M_D @ Pi_RS)
print(f"[A] anti-trap={anti_trap:.4f} escape0={escape0:.4f} C2_0={C2_0:.4f} ratio={C2_0/escape0:.4f} sqrt14={np.sqrt(14):.4f}")

KJ = [K @ J[k] for k in range(3)]
def mu(psi): return np.array([np.vdot(psi, KJ[k] @ psi) for k in range(3)])
rng = np.random.default_rng(2026)
cpsi = rng.standard_normal(W_trip.shape[1]) + 1j*rng.standard_normal(W_trip.shape[1])
Psi0 = W_trip @ cpsi; Psi0 /= np.linalg.norm(Psi0)
v = mu(Psi0).imag
print(f"[B] v(su2+)={v}  ||v||={np.linalg.norm(v):.4f}")

sigma_rot = sum(v[k]*J[k] for k in range(3))
sigma_maj = sum(v[k]*KJ[k] for k in range(3))
sigma_aK  = sum(v[k]*(J[k].conj().T @ K) for k in range(3))
Pp = 0.5*(I_VS+chir); Pm = 0.5*(I_VS-chir)
def Sigma_full(a,b): return np.kron(np.eye(N,dtype=complex), M.sgen(e,a,b))
tg=[(0,1),(4,5),(0,9),(2,11)]
for nm,S in [("rot",sigma_rot),("maj",sigma_maj),("antiK",sigma_aK)]:
    ne=max(fro(Sigma_full(a,b)@S-S@Sigma_full(a,b)) for (a,b) in tg)
    pres=fro(Pp@S@Pp)+fro(Pm@S@Pm); flip=fro(Pp@S@Pm)+fro(Pm@S@Pp)
    print(f"[C] sigma_{nm:6s} ||S||={fro(S):8.3f} nonequiv={ne:8.3f} chir-preserve={pres:8.3f} chir-flip={flip:8.3f}")

sig=[sigma_rot,sigma_maj,sigma_aK]
E0=Pi_perp@M_D@Pi_RS; G0=Gamma@M_D@Pi_RS; AT0=Pi_RS@M_D-M_D@Pi_RS
Ek=[Pi_perp@S@Pi_RS for S in sig]; Gk=[Gamma@S@Pi_RS for S in sig]; ATk=[Pi_RS@S-S@Pi_RS for S in sig]
def mc(c):
    E=E0+sum(c[k]*Ek[k] for k in range(3)); G=G0+sum(c[k]*Gk[k] for k in range(3)); A=AT0+sum(c[k]*ATk[k] for k in range(3))
    return fro(E),fro(G),fro(A)
lams=np.concatenate([-np.geomspace(3,0.05,12),[0.0],np.geomspace(0.05,3,12)])
print("[D] single-channel min-escape:")
for idx,nm in enumerate(["rot","maj","antiK"]):
    best=(None,np.inf,None,None)
    for lam in lams:
        c=np.zeros(3); c[idx]=lam; esc,c2,at=mc(c)
        if esc<best[1]: best=(lam,esc,c2,at)
    print(f"    {nm:6s}: min escape={best[1]:8.4f} at lam={best[0]:+.3f} (C2={best[2]:8.3f} anti-trap={best[3]:8.3f}) reaches0={best[1]<1e-6}")
# greedy combined
coeffs=np.zeros(3); cur=mc(coeffs)[0]; grid=np.linspace(-2,2,81)
for _ in range(6):
    for ci in range(3):
        bl=(coeffs[ci],cur)
        for g in grid:
            t=coeffs.copy(); t[ci]=g; esc,_,at=mc(t)
            if esc<bl[1] and at>1e-6: bl=(g,esc)
        coeffs[ci],cur=bl
ec,cc,ac=mc(coeffs)
print(f"    COMBINED {coeffs}: escape={ec:.4f} C2={cc:.3f} anti-trap={ac:.3f} reaches0={ec<1e-6}")

esc_op=Pi_perp@M_D@Pi_RS
blocks={kk:fro(P1@esc_op@P2) for kk,(P1,P2) in {"++":(Pp,Pp),"+-":(Pp,Pm),"-+":(Pm,Pp),"--":(Pm,Pm)}.items()}
print(f"[E] bare escape chirality blocks: {blocks}")
for nm,S in [("rot",sigma_rot),("maj",sigma_maj),("antiK",sigma_aK)]:
    so=Pi_perp@S@Pi_RS
    b={kk:fro(P1@so@P2) for kk,(P1,P2) in {"++":(Pp,Pp),"+-":(Pp,Pm),"-+":(Pm,Pp),"--":(Pm,Pm)}.items()}
    print(f"    sigma_{nm:6s} escape blocks: {b}")
print(f"[VERDICT] bare escape={escape0:.4f} C2={C2_0:.4f}")
print(f"[VERDICT] combined min escape={ec:.4f} reaches0={ec<1e-6}; anti-trap stays {anti_trap:.4f}")
print("EXIT 0")
