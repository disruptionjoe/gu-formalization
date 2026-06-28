import numpy as np
N=14; DIM=128
def jw(n):
    I=np.eye(2,dtype=complex); s1=np.array([[0,1],[1,0]],dtype=complex)
    s2=np.array([[0,-1j],[1j,0]],dtype=complex); s3=np.array([[1,0],[0,-1]],dtype=complex)
    G=[]
    for k in range(n):
        L=[s3]*k; R=[I]*(n-1-k)
        o=np.array([[1+0j]])
        for m in L+[s1]+R: o=np.kron(o,m)
        G.append(o); o=np.array([[1+0j]])
        for m in L+[s2]+R: o=np.kron(o,m)
        G.append(o)
    return G
G=jw(7)
def fac(n):
    n=int(round(n)); f={}; d=2; m=abs(n)
    while d*d<=m:
        while m%d==0: f[d]=f.get(d,0)+1; m//=d
        d+=1
    if m>1: f[m]=f.get(m,0)+1
    return f
def Jsq(e,eta):
    def Phi(U):
        o=np.zeros_like(U)
        for a in range(N): o+=eta[a]*(e[a]@U@e[a].conj())
        return o/N
    rng=np.random.default_rng(1); U=rng.standard_normal((DIM,DIM))+1j*rng.standard_normal((DIM,DIM))
    for _ in range(150): U=0.5*(U+Phi(U)); U/=np.linalg.norm(U)
    Us,_,Vs=np.linalg.svd(U); U=Us@Vs
    return (np.trace(U@U.conj())/DIM).real
print(f"{'sig':8} {'p-q%8':6} {'class':6} {'rankGamma':9} {'ker':6} {'ker primes':12} {'3 in ker?':9} {'J^2':6}")
for p in [9,7,10,8,11,5,12,14,13]:
    q=N-p; eta=np.array([1.0]*p+[-1.0]*q)
    e=[G[a] if eta[a]>0 else 1j*G[a] for a in range(N)]
    Gamma=np.hstack(e); r=np.linalg.matrix_rank(Gamma,tol=1e-9); ker=N*DIM-r
    cls={0:'R',2:'R',4:'H',6:'H'}.get((p-q)%8,'C/other')
    j=Jsq(e,eta)
    print(f"({p},{q})    {(p-q)%8:<6} {cls:6} {r:<9} {ker:<6} {str(sorted(fac(ker))):12} {str(3 in fac(ker)):9} {j:+.2f}")
print("\nker(Gamma) = 14*128 - rank(Gamma); rank=128 (Gamma surjective, each gamma invertible) => ker=13*128=1664=2^7*13 for ALL signatures. Prime 3 absent universally (structural).")
