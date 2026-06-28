"""
A2 -- KR (Atiyah Real) equivariant index discriminator. The swing computed the COMPLEX index of a Real
bundle and got 0; the generation-mirror swap is a Real structure, so the correct invariant might be the
KR-index, a different integer with KR^{p,q} periodicity mod 8 (the natural home of 24/8). A KR refinement
can produce a new Z2 ONLY if a grading-ODD Spin(10)-equivariant operator exists (one anticommuting with the
chirality C while commuting with the gauge group).

RESULT (machine-checked, (9,5) triplet): NO such element exists, so the KR-index collapses to the known
even quaternionic 0 (kill). The decisive fact: on the triplet C is PERFECTLY correlated with the Spin(10)
chirality (16/16bar) -- C=+1 is entirely 16bar, C=-1 is entirely 16. A grading-odd Spin(10)-equivariant map
would have to send 16bar -> 16 equivariantly, impossible since 16 and 16bar are inequivalent irreps. So the
generation-mirror swap (16 <-> 16bar) is exactly NOT Spin(10)-equivariant -- the same reality-structure
obstruction the swing already identified, now confirmed at the level of the full Atiyah-Real refinement.
Escape hatch A2: closed, kill confirmed.
"""
# A2 KR discriminator: is C perfectly correlated with the Spin(10) chirality (16/16bar) on the triplet?
# Perfect correlation -> no grading-odd Spin(10)-equivariant element -> KR-index = known even 0 (kill).
# Mixed -> a grading-odd equivariant map exists -> candidate KR Z2.
import numpy as np
N,DIM=14,128
def jw(n):
    I=np.eye(2,dtype=complex); s1=np.array([[0,1],[1,0]],dtype=complex)
    s2=np.array([[0,-1j],[1j,0]],dtype=complex); s3=np.array([[1,0],[0,-1]],dtype=complex)
    G=[]
    for k in range(n):
        L=[s3]*k; R=[I]*(n-1-k)
        for mid in (s1,s2):
            o=np.array([[1+0j]])
            for m in L+[mid]+R: o=np.kron(o,m)
            G.append(o)
    return G
base=jw(7); I128=np.eye(DIM,dtype=complex); I14=np.eye(N,dtype=complex)
timelike={4,5,6,7,8}
e=[(1j*base[a] if a in timelike else base[a]) for a in range(14)]
def sgen(i,j): return 0.25*(e[i]@e[j]-e[j]@e[i])
def lvec(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; M[j,i]=-1; return M
def gen(i,j): return np.kron(I14,sgen(i,j))+np.kron(lvec(i,j),I128)
def comm(A,B): return A@B-B@A
Gam=np.hstack(e); Pi=np.eye(N*DIM,dtype=complex)-Gam.conj().T@np.linalg.inv(Gam@Gam.conj().T)@Gam
SD=[(0,1,2,3),(0,2,3,1),(0,3,1,2)]
J3=[gen(a,b)+gen(c,d) for (a,b,c,d) in SD]
w,Vv=np.linalg.eigh(Pi); Wk=Vv[:,w>0.5]
Cas=-(J3[0]@J3[0]+J3[1]@J3[1]+J3[2]@J3[2]); CK=Wk.conj().T@Cas@Wk; CK=0.5*(CK+CK.conj().T)
ev,U=np.linalg.eigh(CK); top=max(round(x.real,3) for x in ev); Wt=Wk@U[:,np.abs(ev-top)<1e-3]
# full chirality C
om=I128.copy()
for a in range(14): om=om@e[a]
om2=(np.trace(om@om)/DIM).real
C=Wt.conj().T@np.kron(I14, om if om2>0 else (-1j)*om)@Wt; C=0.5*(C+C.conj().T)
# Spin(10) chirality (16/16bar): internal volume, restricted to triplet
oi=I128.copy()
for a in range(4,14): oi=oi@e[a]
oi2=(np.trace(oi@oi)/DIM).real
W10=Wt.conj().T@np.kron(I14, oi if oi2>0 else (-1j)*oi)@Wt; W10=0.5*(W10+W10.conj().T)
Ggen=[Wt.conj().T@gen(i,j)@Wt for i in range(4,14) for j in range(i+1,14)]
gcom=max(np.linalg.norm(comm(W10,g)) for g in Ggen)
print(f"Spin(10) chirality on triplet: W10^2=I? {np.linalg.norm(W10@W10-np.eye(192)):.1e}; "
      f"[W10,Spin(10)]={gcom:.1e}; [W10,C]={np.linalg.norm(comm(W10,C)):.1e}")
# joint spectrum of (C, W10): four sectors
cev,cU=np.linalg.eigh(C)
from collections import Counter
sect=Counter()
for s in (+1,-1):
    P=cU[:,(cev>0.5) if s>0 else (cev<-0.5)]
    M=P.conj().T@W10@P; we=np.linalg.eigvalsh(0.5*(M+M.conj().T))
    sect[(s,+1)]=int(np.sum(we>0.5)); sect[(s,-1)]=int(np.sum(we<-0.5))
print(f"joint (C, Spin10-chir) sector dims: C+/16={sect[(1,1)]}, C+/16bar={sect[(1,-1)]}, "
      f"C-/16={sect[(-1,1)]}, C-/16bar={sect[(-1,-1)]}")
mixed = sect[(1,1)]>0 and sect[(1,-1)]>0 and sect[(-1,1)]>0 and sect[(-1,-1)]>0
print(f"=> {'MIXED: each C-eigenspace has both 16 and 16bar -> grading-odd Spin(10)-equivariant maps EXIST (candidate KR Z2)' if mixed else 'PERFECT CORRELATION -> no grading-odd equivariant map -> KR collapses to even 0 (KILL)'}")
