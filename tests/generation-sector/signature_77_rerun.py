import sys, numpy as np
# Build (7,7) Clifford rep (real class, p-q=0 mod 8 => M(128,R), NO quaternionic J) and re-run
# C-04 (prime spectrum), the parity (is odd index now reachable?), and C-05 (connection index).
N=14; DIM=128
def jw(n):
    I=np.eye(2,dtype=complex); s1=np.array([[0,1],[1,0]],dtype=complex)
    s2=np.array([[0,-1j],[1j,0]],dtype=complex); s3=np.array([[1,0],[0,-1]],dtype=complex)
    G=[]
    for k in range(n):
        L=[s3]*k; R=[I]*(n-1-k)
        def kr(ms):
            o=np.array([[1+0j]])
            for m in ms: o=np.kron(o,m)
            return o
        G.append(kr(L+[s1]+R)); G.append(kr(L+[s2]+R))
    return G
G=jw(7)
eta=np.array([1.0]*7+[-1.0]*7)   # (7,7) signature
e=[G[a] if eta[a]>0 else 1j*G[a] for a in range(N)]
# verify Clifford {e_a,e_b}=2 eta_ab
err=max(np.linalg.norm(e[a]@e[b]+e[b]@e[a]-(2*eta[a] if a==b else 0)*np.eye(DIM)) for a in range(N) for b in range(N))
print(f"(7,7) Clifford relations max err = {err:.1e}")
Gamma=np.hstack(e); Pi=np.eye(N*DIM,dtype=complex)-Gamma.conj().T@np.linalg.inv(Gamma@Gamma.conj().T)@Gamma
XI=np.array([1,2,3,4,0.5,1.5,2.5,0.7,1.1,0.3,2.2,1.7,0.9,1.3],dtype=complex)
M_D=np.kron(np.eye(N),sum(XI[a]*e[a] for a in range(N))); Q=np.eye(N*DIM,dtype=complex)-Pi
bare=np.linalg.norm(Pi@M_D-M_D@Pi); C2=np.linalg.norm(Gamma@M_D@Pi)
def fac(n):
    n=int(round(n)); f={}; d=2; m=abs(n)
    while d*d<=m:
        while m%d==0: f[d]=f.get(d,0)+1; m//=d
        d+=1
    if m>1: f[m]=f.get(m,0)+1
    return f
dimker=int(round(np.trace(Pi).real))
print(f"(7,7): bare={bare:.3f} C2={C2:.3f}")
print(f"=== C-04 under (7,7): dimension spectrum ===")
for name,v in [("spinor",128),("RS vector",14),("RS space",1792),("ker(Gamma)",dimker),("rank Gamma",int(round(np.trace(Q).real)))]:
    f=fac(v); print(f"  {name:12}={v:5}  primes={sorted(f)}  {'<-- HAS 3!' if 3 in f else ''}")
# real structure: build J (commuting antiunitary) and check J^2 sign (real class => +1, no Kramers)
def Phi(U):
    o=np.zeros_like(U)
    for a in range(N): o+=eta[a]*(e[a]@U@e[a].conj())
    return o/N
rng=np.random.default_rng(1); U=rng.standard_normal((DIM,DIM))+1j*rng.standard_normal((DIM,DIM))
for _ in range(400): U=0.5*(U+Phi(U)); U/=np.linalg.norm(U)
Us,_,Vs=np.linalg.svd(U); U=Us@Vs
lam=np.trace(U@U.conj())/DIM
print(f"=== parity under (7,7): J^2 = ({lam.real:+.3f})  => {'QUATERNIONIC (wall persists)' if lam.real<0 else 'REAL (NO Kramers wall)'} ===")
def sig(A):
    ev=np.linalg.eigvalsh(0.5*(A+A.conj().T)); tol=1e-7*np.abs(ev).max(); return int((ev>tol).sum())-int((ev<-tol).sum())
def gd(X): return Pi@X@Pi+Q@X@Q
def hm(X): return 0.5*(X+X.conj().T)
# can a NATURAL/metric connection now give ODD or nonzero index? test self-dual + random so(7,7) gens
def Mvec(i,j):
    M=np.zeros((N,N),dtype=complex); M[i,j]=eta[j]; M[j,i]=-eta[i]; return M
def sigma(i,j): return 0.25*(e[i]@e[j]-e[j]@e[i])
def Jfull(i,j): return np.kron(Mvec(i,j),np.eye(DIM))+np.kron(np.eye(N),sigma(i,j))
sd=[sig(hm(gd(1j*(Jfull(0,1)+Jfull(2,3))))) , sig(hm(gd(1j*Jfull(0,1))))]
rng2=np.random.default_rng(3)
algv=[sig(hm(gd(1j*sum(c*Jfull(i,j) for (c,(i,j)) in zip(rng2.standard_normal(6),[(0,1),(2,3),(4,5),(0,9),(2,11),(6,13)]))))) for _ in range(3)]
print(f"=== C-05 under (7,7): connection indices: self-dual+single={sd}  random so(7,7)={algv} ===")
print(f"    (under (9,5) these were all 0/even; if odd/nonzero here, the C-05 leg dissolves under (7,7))")
# parity: do GU-native carriers still force even? test low-rank generic + a J-linear-equivalent
print(f"=== parity check: can GU-native carriers give ODD index now? ===")
w,V=np.linalg.eigh(Pi); Wk=V[:,w>0.5]
for r in [3]:
    cols=rng2.choice(Wk.shape[1],r,replace=False); M=Wk[:,cols]@Wk[:,cols].conj().T
    print(f"  rank-3 kernel carrier sig = {sig(hm(gd(M)))} (free, as before)")
