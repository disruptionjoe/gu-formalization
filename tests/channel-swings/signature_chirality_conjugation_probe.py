#!/usr/bin/env python3
"""H2 corrected: does antilinear conjugation FLIP or PRESERVE chirality?
Bug in v1: used omega = g0g1g2g3 (omega^2 = -I in (1,3)), which is NOT the
chirality operator. Correct: gamma5 normalized so gamma5^2 = +I. The omitted
factor of i is exactly where the signature dependence enters."""
import itertools
def mm(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def smul(c,A): return [[c*x for x in r] for r in A]
def conj(A): return [[x.conjugate() for x in r] for r in A]
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A)))
def kron(A,B):
    na,nb=len(A),len(B)
    return [[A[i//nb][j//nb]*B[i%nb][j%nb] for j in range(na*nb)] for i in range(na*nb)]
I2=eye(2); X=[[0,1],[1,0]]; Y=[[0,-1j],[1j,0]]; Z=[[1,0],[0,-1]]; eps=[[0,1],[-1,0]]

LOR=[kron(Z,I2), kron(eps,X), kron(eps,Y), kron(eps,Z)]          # (1,3)
EUC=[kron(X,I2), kron(Y,I2), kron(Z,X), kron(Z,Y)]               # (4,0)

def gamma5(G, sig):
    n=len(G[0]); w=eye(n)
    for g in G: w=mm(w,g)
    for ph in (1,1j,-1,-1j):
        c=smul(ph,w)
        if eq(mm(c,c),eye(n)): return c,ph
    return None,None

def analyse(G,name):
    print(f"\n=== {name}")
    g5,ph=gamma5(G,name)
    print(f"  gamma5 = ({ph})*g0g1g2g3, gamma5^2 = +I  [normalisation {'REAL' if ph in (1,-1) else 'IMAGINARY'}]")
    print(f"  conj(gamma5) == gamma5 ? {eq(conj(g5),g5)}   conj(gamma5) == -gamma5 ? {eq(conj(g5),smul(-1,g5))}")
    n=len(G[0]); found=[]
    for r in range(len(G)+1):
        for combo in itertools.combinations(range(len(G)),r):
            M=eye(n)
            for i in combo: M=mm(M,G[i])
            for c_ph in (1,1j):
                C=smul(c_ph,M)
                for flip in (1,-1):
                    if all(eq(mm(C,conj(g)), smul(flip,mm(g,C))) for g in G):
                        # antilinear map psi -> C conj(psi); action on chirality:
                        lhs=mm(C,conj(g5)); rhs=mm(g5,C)
                        pres=eq(lhs,rhs); flips=eq(lhs,smul(-1,rhs))
                        found.append((combo,c_ph,flip,'PRESERVES' if pres else ('FLIPS' if flips else '?')))
    seen=set()
    for combo,c_ph,flip,verdict in found:
        k=(verdict,flip)
        if k in seen: continue
        seen.add(k)
        print(f"  C=phase({c_ph})*gamma{combo}, C conj(g)={flip:+d} g C  ->  chirality {verdict}")
    verdicts={v for _,_,_,v in found}
    print(f"  SUMMARY: verdicts present = {sorted(verdicts)}")

analyse(LOR,"Cl(1,3) Lorentzian")
analyse(EUC,"Cl(4,0) Euclidean")
