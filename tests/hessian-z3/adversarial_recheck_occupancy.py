#!/usr/bin/env python3
"""
ADVERSARIAL RE-CHECK of carrier_occupancy_hessian.py.

Independent re-derivation + stress tests of the central claims:
  (A) B = Wt^dag K Wt is a reflection (B^2 = I, spectrum {+1 x96, -1 x96}).
  (B) the "occupancy" Rayleigh quotient = 0 is TAUTOLOGICAL for ANY indefinite form:
      a unit +eigvec a plus a unit -eigvec b (orthogonal) gives v^dag B v = 0 exactly,
      independent of the substrate. Demonstrate with a RANDOM Hermitian reflection.
  (C) THE GATING GAP: add a mass/identity term m*I to the Hessian (a legitimate piece of
      any quadratic action) and show the occupancy "eigenvalue" moves to m -- i.e. the
      flatness is gated on the action having NO diagonal mass term, not on the substrate.
  (D) is "0" a kernel/zero-mode of B (a real flat direction), or a null direction of a
      NONDEGENERATE saddle? Report B's actual spectrum / kernel dimension.
"""
import numpy as np

N, DIM = 14, 128

def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0,1],[1,0]], dtype=complex)
    s2 = np.array([[0,-1j],[1j,0]], dtype=complex)
    s3 = np.array([[1,0],[0,-1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3]*k, [I]*(n-1-k)
        for mid in (s1, s2):
            o = np.array([[1+0j]])
            for m in L+[mid]+R: o = np.kron(o, m)
            G.append(o)
    return G

def sgen(e,i,j): return 0.25*(e[i]@e[j]-e[j]@e[i])
def lvec(i,j):
    M = np.zeros((N,N), dtype=complex); M[i,j]=1; M[j,i]=-1; return M
SD = [(0,1,2,3),(0,2,3,1),(0,3,1,2)]

def build_B(timelike={4,5,6,7,8}):
    base = jw(7)
    I128, I14 = np.eye(DIM,dtype=complex), np.eye(N,dtype=complex)
    e = [(1j*base[a] if a in timelike else base[a]) for a in range(14)]
    spacelike = [a for a in range(14) if a not in timelike]
    Gamma = np.hstack(e)
    Pi = np.eye(N*DIM,dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma@Gamma.conj().T) @ Gamma
    J = [np.kron(I14, sgen(e,a,b)+sgen(e,c,d)) + np.kron(lvec(a,b)+lvec(c,d), I128)
         for (a,b,c,d) in SD]
    w, Vv = np.linalg.eigh(Pi); W = Vv[:, w>0.5]
    Cas = -(J[0]@J[0]+J[1]@J[1]+J[2]@J[2])
    CasK = W.conj().T@Cas@W; CasK = 0.5*(CasK+CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    top = max(round(x.real,3) for x in ev)
    Wt = W @ U[:, np.abs(ev-top)<1e-3]
    bS = I128.copy()
    for s in spacelike: bS = bS@e[s]
    if np.linalg.norm(bS.conj().T+bS)<1e-9: bS = 1j*bS
    bS = bS/np.sqrt(abs((bS@bS)[0,0].real))
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
    K = np.kron(etaV, bS)
    B = Wt.conj().T@K@Wt; B = 0.5*(B+B.conj().T)
    return B

def rq(B,v):
    v = v/np.linalg.norm(v); return float((v.conj()@B@v).real)

B = build_B()
ev = np.linalg.eigvalsh(B)
print("="*80)
print("(A) IS B A REFLECTION?")
B2 = B@B
print(f"  ||B^2 - I||_F = {np.linalg.norm(B2-np.eye(B.shape[0])):.3e}")
print(f"  spectrum: unique rounded eigenvalues = {sorted(set(np.round(ev,6)))}")
print(f"  #(+1)={int((ev>0.5).sum())}, #(-1)={int((ev<-0.5).sum())}")

print("\n(D) IS '0' A KERNEL OF B (real flat mode) OR A NULL DIR OF A SADDLE?")
print(f"  dim ker(B) (|eig|<1e-9) = {int((np.abs(ev)<1e-9).sum())}  "
      f"(0 -> B NONDEGENERATE; no actual flat eigen-mode)")
print(f"  min|eig(B)| = {np.min(np.abs(ev)):.4f}  -> B has 96 strictly + and 96 strictly - dirs (a SADDLE)")

print("\n(B) IS occupancy=0 TAUTOLOGICAL? Test on a RANDOM 192-dim Hermitian reflection")
rng = np.random.default_rng(1)
Q,_ = np.linalg.qr(rng.standard_normal((192,192))+1j*rng.standard_normal((192,192)))
Drand = np.diag([1.0]*96+[-1.0]*96)
Brand = Q@Drand@Q.conj().T; Brand = 0.5*(Brand+Brand.conj().T)
evr, Vr = np.linalg.eigh(Brand)
ap = Vr[:,evr>0]; an = Vr[:,evr<0]
a = ap.sum(1); a/=np.linalg.norm(a); b = an.sum(1); b/=np.linalg.norm(b)
vbal = (a+b)/np.linalg.norm(a+b)
print(f"  random reflection (NOTHING to do with GU): balanced +/- occupancy lambda = {rq(Brand,vbal):+.3e}")
print(f"  -> EXACTLY 0 on a random operator too: the zero is a property of indefinite forms,")
print(f"     not of the GU substrate. 'occupancy=balanced' SELECTS a null ray by construction.")

print("\n(C) THE GATING GAP: add a mass term m*I (legitimate in any quadratic action)")
# reuse GU B's eigenbasis to build the same occupancy direction
evb, Vb = np.linalg.eigh(B)
up = Vb[:,evb>0].sum(1); up/=np.linalg.norm(up)
un = Vb[:,evb<0].sum(1); un/=np.linalg.norm(un)
occ = (up+un)/np.linalg.norm(up+un)
for m in [0.0, 0.05, 0.2, 0.5]:
    Bm = B + m*np.eye(B.shape[0])
    print(f"  m={m:>4}:  occupancy lambda = {rq(Bm,occ):+.4f}   "
          f"(= m -> a mass/forcing term moves it OFF 0; flatness gated on m=0)")

print("\n" + "="*80)
print("SUMMARY: B^2=I confirmed; occupancy=0 is tautological for ANY indefinite form")
print("(verified on a random reflection); '0' is a NULL DIRECTION of a NONDEGENERATE")
print("SADDLE (ker B = 0), NOT a flat zero-eigenvalue MODE; and a diagonal mass term")
print("moves it off 0 -> the result is gated on the action being massless on the carrier.")
