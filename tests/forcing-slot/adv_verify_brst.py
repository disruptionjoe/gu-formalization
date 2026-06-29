#!/usr/bin/env python3
"""Independent adversarial recheck of the BRST/FP forcing-slot claim.
Does NOT import the construct; rebuilds everything from scratch."""
import numpy as np
np.random.seed(0)
N, DIM = 14, 128

def jw(n):
    I=np.eye(2,dtype=complex); s1=np.array([[0,1],[1,0]],dtype=complex)
    s2=np.array([[0,-1j],[1j,0]],dtype=complex); s3=np.array([[1,0],[0,-1]],dtype=complex)
    G=[]
    for k in range(n):
        L,R=[s3]*k,[I]*(n-1-k)
        for mid in (s1,s2):
            o=np.array([[1+0j]])
            for m in L+[mid]+R: o=np.kron(o,m)
            G.append(o)
    return G
e=jw(7); I128=np.eye(DIM,dtype=complex); I14=np.eye(N,dtype=complex)

def lvec(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; M[j,i]=-1; return M
def frame_charge(O,gens):
    O4=O.reshape(N,DIM,N,DIM); tot=0.0
    for L in gens:
        nrm=np.tensordot(L.conj(),L,axes=([0,1],[0,1])).real
        F=np.einsum('vw,vswt->st',L.conj(),O4)/nrm; tot+=float(np.linalg.norm(F))
    return tot
sd=[lvec(0,1)+lvec(2,3),lvec(0,2)+lvec(3,1),lvec(0,3)+lvec(1,2)]
asd=[lvec(0,1)-lvec(2,3),lvec(0,2)-lvec(3,1),lvec(0,3)-lvec(1,2)]

def chir(idx):
    om=I128.copy()
    for a in idx: om=om@e[a]
    sq=(om@om)[0,0]
    if abs(sq+1)<1e-6: om=(-1j)*om
    om=0.5*(om+om.conj().T); return om
om14=chir(range(14)); om10=chir(range(4,14)); om4=chir([0,1,2,3])

def proj_ker(G):
    return np.eye(G.shape[1],dtype=complex)-G.conj().T@np.linalg.inv(G@G.conj().T)@G
def netchiral(P,grade):
    M=0.5*(P.conj().T@grade@P+(P.conj().T@grade@P).conj().T)
    ev=np.linalg.eigvalsh(M); return int(np.sum(ev>.5)),int(np.sum(ev<-.5))

Gamma=np.hstack(e)
Pi=proj_ker(Gamma); Q=np.eye(N*DIM,dtype=complex)-Pi
print("ker(Gamma)=",round(np.trace(Pi).real),"Q=",round(np.trace(Q).real))

# CLAIM 1: frame charge of id14 (x) U is identically 0, for RANDOM U (not just c(xi))
U=np.random.randn(DIM,DIM)+1j*np.random.randn(DIM,DIM)
print("frame_charge(id14 x random U) =",frame_charge(np.kron(I14,U),sd+asd))

# CLAIM 2: net chirality of full / phys / ghost via chir14 -- recompute, and test ROBUSTNESS
chir14=np.kron(I14,om14)
def proj_cols(P):
    w,V=np.linalg.eigh(0.5*(P+P.conj().T)); return V[:,w>.5]
for name,P in [("full",np.eye(N*DIM,dtype=complex)),("phys",Pi),("ghost",Q)]:
    a,b=netchiral(proj_cols(P) if name!="full" else np.eye(N*DIM,dtype=complex),chir14)
    print(f"  {name}: +{a}/-{b} net {a-b}")

# CLAIM 3: is the zero net-chiral FITTED to XI? sweep many random XI and check FP frame charge + the
# pure-gauge image net self-dual. (XI shouldn't matter for chirality since Pi is XI-independent,
# but check the gauge image frame charge that the construct attributes to XI.)
for trial in range(3):
    XI=np.random.randn(N)+1j*np.random.randn(N)
    g=np.zeros((N*DIM,DIM),dtype=complex)
    for mu in range(N): g[mu*DIM:(mu+1)*DIM,:]=XI[mu]*I128
    FP=Gamma@g; cxi=sum(XI[a]*e[a] for a in range(N))
    Pg=g@np.linalg.inv(g.conj().T@g)@g.conj().T
    netsd=frame_charge(Pg,sd)-frame_charge(Pg,asd)
    print(f"  XI trial {trial}: ||FP-c(xi)||={np.linalg.norm(FP-cxi):.1e}  "
          f"fc(id14 x c(xi))={frame_charge(np.kron(I14,cxi),sd+asd):.1e}  "
          f"im(g) net self-dual={netsd:.2e}")

# CLAIM 4: the 48. recompute Gamma^dag Gamma frame charge + factor
GtG=Gamma.conj().T@Gamma
fc=frame_charge(GtG,sd+asd); netsdG=frame_charge(GtG,sd)-frame_charge(GtG,asd)
print(f"  Gamma^dag Gamma: frame_charge(all)={fc:.4f} net_self_dual={netsdG:.2e}")
print(f"    48 = 2^4 * 3 ; is GtG Hermitian-positive (=>vectorlike)? min eig =",
      round(float(np.linalg.eigvalsh(0.5*(GtG+GtG.conj().T)).min()),4))

# CLAIM 5: the HARD test for a hidden 3. Build the actual twisted-Dirac-style INDEX, not a fiber
# supertrace. The honest generation count is an INDEX. On a finite fiber the "net chirality" is a
# supertrace = str(grade * Projector). Try to FORCE a nonzero net by twisting with chiral 16 AND
# measuring frame(Spin4) chirality on the gamma-traceless transverse sector. Sweep.
P16=np.kron(I14,0.5*(I128+om10)); chir4=np.kron(I14,om4)
Pi_t=P16@Pi@P16
a,b=netchiral(proj_cols(Pi_t),chir4); print(f"  twisted transverse frame-chirality: +{a}/-{b} net {a-b}")
# also try anti-chiral 16bar and the OTHER frame chirality sign conventions
P16b=np.kron(I14,0.5*(I128-om10))
a2,b2=netchiral(proj_cols(P16b@Pi@P16b),chir4); print(f"  16bar transverse frame-chirality: +{a2}/-{b2} net {a2-b2}")
