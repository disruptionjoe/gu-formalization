"""
A3 -- G_SM-only equivariant ghost parity. Relax the swing's full-Spin(10)-equivariance of the ghost parity
to commuting only with the unbroken G_SM. Forecast: the kill is robust, because cross-chirality is a
property of the PHYSICAL Dirac Krein form, not of the ghost parity's equivariance group.

RESULT (machine-checked, (9,5) triplet): the physical Dirac form Kd is cross-chirality (same-chirality
blocks ~1e-14), so the Dirac-physical sector has net chirality 0 regardless of the ghost parity's
equivariance group -- the last open native route is CLOSED. The one real sliver, located precisely: a
NON-Dirac so(p,q)-invariant indefinite form (the chirality C itself, gauge-invariant and indefinite) has a
positive sector with net chirality +96, genuinely net-chiral. So the kill rests on exactly one named
assumption -- that the matter sector's physical inner product is the gamma-adjoint Dirac form. Using a
different invariant form chiralizes, but is not the physical matter inner product. Escape hatch A3: closed,
contingent on the Dirac form (the load-bearing assumption now explicitly named).
"""
# A3: is the kill robust to relaxing the ghost-parity equivariance to G_SM-only?
# Key fact: cross-chirality is a property of the PHYSICAL (Dirac) Krein form K, not of the equivariance
# group. The only chiralizing forms are NON-Dirac so(p,q)-invariant forms (e.g. the chirality C itself),
# which are not the matter sector's physical inner product.
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
spacelike=[a for a in range(14) if a not in timelike]
def sgen(i,j): return 0.25*(e[i]@e[j]-e[j]@e[i])
def lvec(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=1; M[j,i]=-1; return M
def gen(i,j): return np.kron(I14,sgen(i,j))+np.kron(lvec(i,j),I128)
def comm(A,B): return A@B-B@A
Gam=np.hstack(e); Pi=np.eye(N*DIM,dtype=complex)-Gam.conj().T@np.linalg.inv(Gam@Gam.conj().T)@Gam
SD=[(0,1,2,3),(0,2,3,1),(0,3,1,2)]; J3=[gen(a,b)+gen(c,d) for (a,b,c,d) in SD]
w,Vv=np.linalg.eigh(Pi); Wk=Vv[:,w>0.5]
Cas=-(J3[0]@J3[0]+J3[1]@J3[1]+J3[2]@J3[2]); CK=Wk.conj().T@Cas@Wk; CK=0.5*(CK+CK.conj().T)
ev,U=np.linalg.eigh(CK); top=max(round(x.real,3) for x in ev); Wt=Wk@U[:,np.abs(ev-top)<1e-3]
bS=I128.copy()
for s in spacelike: bS=bS@e[s]
if np.linalg.norm(bS.conj().T+bS)<1e-9: bS=1j*bS
bS=bS/np.sqrt(abs((bS@bS)[0,0].real))
etaV=np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
Kd=Wt.conj().T@np.kron(etaV,bS)@Wt; Kd=0.5*(Kd+Kd.conj().T)               # PHYSICAL Dirac Krein form
om=I128.copy()
for a in range(14): om=om@e[a]
om2=(np.trace(om@om)/DIM).real
C=Wt.conj().T@np.kron(I14, om if om2>0 else (-1j)*om)@Wt; C=0.5*(C+C.conj().T)
Ggen=[Wt.conj().T@gen(i,j)@Wt for i in range(4,14) for j in range(i+1,14)]
# G_SM-invariance of C: C is central in even Clifford -> so(p,q)- (hence G_SM-) invariant
print(f"chirality C: so(p,q)-invariant? max[C,Spin(10)]={max(np.linalg.norm(comm(C,g)) for g in Ggen):.1e}; C^2=I {np.linalg.norm(C@C-np.eye(192)):.1e}")
# PHYSICAL Dirac form Kd: cross-chirality -> physical sector 50/50 -> net 0 (kill, holds for any equivariance)
cev,cU=np.linalg.eigh(C); Pp=cU[:,cev>0.5]; Pm=cU[:,cev<-0.5]
print(f"physical Dirac Kd: same-chirality blocks ||Kd(+,+)||={np.linalg.norm(Pp.conj().T@Kd@Pp):.1e}, ||Kd(-,-)||={np.linalg.norm(Pm.conj().T@Kd@Pm):.1e} (cross-chirality)")
kev,kU=np.linalg.eigh(Kd); phys=kU[:,kev>1e-9]
print(f"   -> net chirality of Dirac-physical sector = {np.trace(phys.conj().T@C@phys).real:+.1e} (KILL, independent of ghost-parity equivariance)")
# the sliver: a NON-Dirac so(p,q)-invariant indefinite form K'=C; its positive sector IS net-chiral
kev2,kU2=np.linalg.eigh(C); phys2=kU2[:,kev2>0]
print(f"non-Dirac form K'=C (so(p,q)- and G_SM-invariant, indefinite): positive sector net chirality = {np.trace(phys2.conj().T@C@phys2).real:+.0f} (NET-CHIRAL!)")
print("=> A3 verdict: the kill is a property of the PHYSICAL Dirac form (cross-chirality), unchanged by")
print("   relaxing to G_SM-equivariance. A non-Dirac invariant form (C) CAN chiralize, but it is not the")
print("   matter sector's physical inner product. Last open native route closed, contingent on the Dirac form.")
