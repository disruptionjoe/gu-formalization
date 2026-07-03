#!/usr/bin/env python3
"""ADVERSARIAL third-method recheck of OQ-RK1 composite rank.

Independent of BOTH producer scripts:
  - Different gamma construction: build Cl(9,5) via a DIFFERENT pairing order
    (interleave sign assignment) and verify Clifford relations.
  - Different logic: use the CHIRALITY-GRADING block argument.  Because in even
    dim n=14 the volume element omega ANTICOMMUTES with each e_a, chirality
    grades V = V_+ (+) V_-.  Then T maps V_+ -> E_-S and V_- -> E_+S in blocks.
    The +chirality part of ker T is exactly ker(T|V_+).  We compute rank(T|V_+)
    and rank(T|V_-) directly and check ker(T|V_+) dim == composite rank.
  - Cross-check against direct composite rank in THIS rep.

No target number (3,4,8,24) is used.
"""
import numpy as np

def kron_list(mats):
    out = np.array([[1.0+0j]])
    for m in mats:
        out = np.kron(out, m)
    return out

def jw(n):
    I=np.eye(2,dtype=complex)
    s1=np.array([[0,1],[1,0]],dtype=complex)
    s2=np.array([[0,-1j],[1j,0]],dtype=complex)
    s3=np.array([[1,0],[0,-1]],dtype=complex)
    g=[]
    for k in range(n):
        g.append(kron_list([s3]*k+[s1]+[I]*(n-1-k)))
        g.append(kron_list([s3]*k+[s2]+[I]*(n-1-k)))
    return g

n=7; dim=2**n
G=jw(n)
# DIFFERENT signature interleaving: timelike on odd-indexed slots 1,3,5,7,9
eta=[+1]*14
for idx in [1,3,5,7,9]:
    eta[idx]=-1
e=[G[a] if eta[a]==+1 else 1j*G[a] for a in range(14)]
I=np.eye(dim,dtype=complex)

# Clifford check
maxc=0.0
for a in range(14):
    for b in range(14):
        anti=e[a]@e[b]+e[b]@e[a]
        exp=(2*eta[a] if a==b else 0)*I
        maxc=max(maxc,float(np.max(np.abs(anti-exp))))
assert maxc<1e-9, maxc

omega=I.copy()
for a in range(14):
    omega=omega@e[a]
assert float(np.max(np.abs(omega@omega-I)))<1e-9

# omega anticommutes with each e_a (n even)
maxanti=max(float(np.max(np.abs(omega@e[a]+e[a]@omega))) for a in range(14))
print("omega anticommutes with all e_a? max|{omega,e_a}| =", maxanti)

# chirality projectors on S
Ep=0.5*(I+omega); Em=0.5*(I-omega)
rEp=int(np.linalg.matrix_rank(Ep,tol=1e-9))
print("rank E_+ on S =", rEp, "(expect 64)")

# bases for E_+ S and E_- S
wv,vec=np.linalg.eigh(omega)
Vp=vec[:,wv>0]      # 128 x 64 : +chirality spinors
Vm=vec[:,wv<0]      # 128 x 64

d14=14
# T on full V = [e_0...e_13] : 128 x 1792
T=np.hstack([e[a] for a in range(d14)])
# Restrict domain to V_+ = R^14 (x) E_+S : basis is I_14 (x) Vp -> 1792 x 896
Bp=np.kron(np.eye(d14),Vp)   # 1792 x 896
Bm=np.kron(np.eye(d14),Vm)
Tp=T@Bp   # 128 x 896  (image should lie in E_-S)
Tm=T@Bm
rTp=int(np.linalg.matrix_rank(Tp,tol=1e-7))
rTm=int(np.linalg.matrix_rank(Tm,tol=1e-7))
print("rank(T|V_+) =",rTp,"  rank(T|V_-) =",rTm,"(expect 64 each)")
# check image of Tp lies in E_-S
leak=float(np.max(np.abs(Ep@Tp)))
print("Ep @ (T|V_+) leak (expect ~0):", leak)

ker_Tp_dim = Bp.shape[1]-rTp
print("dim ker(T|V_+) = +chirality part of ker T =", ker_Tp_dim, "(this IS composite rank_C)")

# direct composite in this rep
gram=T@T.conj().T
Pi=np.eye(1792,dtype=complex)-T.conj().T@np.linalg.inv(gram)@T
Efull=np.kron(np.eye(d14),Ep)
comp=Pi@Efull@Pi
rc=int(np.linalg.matrix_rank(comp,tol=1e-9))
print("direct rank_C(Pi E_+ Pi) this rep =", rc)
print("MATCH:", ker_Tp_dim==rc, "  rank_H =", rc//2 if rc%2==0 else "odd")
