#!/usr/bin/env python3
"""Exact controls for the fixed-geometric-weak Lorentz-lift theorem.

Root executes this serialized. Universal all-lift scope is proved in the note;
finite controls do not establish source selection or a physical current.
"""
import argparse
import json
import sympy as s

p = argparse.ArgumentParser()
p.add_argument('--mutant', choices=['weak-diagonal', 'spin-only-as-geometric', 'frozen-moving-q'])
args = p.parse_args()
checks = []

def check(name, predicate):
    ok = bool(predicate)
    checks.append({'name': name, 'pass': ok})
    if not ok:
        raise AssertionError(name)

def comm(a, b):
    return a*b-b*a

def unit(n, i, j):
    a=s.zeros(n); a[i,j]=1; return a

def embed4(a):
    b=s.zeros(10); b[6:10,6:10]=a; return b

def flat(a):
    return a.reshape(a.rows*a.cols, 1)

I4=s.eye(4)
Li=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
Lj=s.Matrix([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
Lk=Li*Lj
Ri=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,1],[0,0,-1,0]])
Rj=s.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])
Rk=-Ri*Rj
left=[Li,Lj,Lk]; right=[Ri,Rj,Rk]
check('left quaternion products', Li*Lj==Lk and Lj*Li==-Lk and all(a*a==-I4 for a in left))
check('left-right centralization', all(comm(a,b)==s.zeros(4) for a in left for b in right))
check('right imaginary skewness', all(a.T==-a for a in right))

K=s.diag(*([1]*6+[-1]*4))
metric_basis=[]
for i in range(10):
    for j in range(i+1,10):
        metric_basis.append(unit(10,i,j)-K[i,i]*K[j,j]*unit(10,j,i))
check('all45 metric generators', len(metric_basis)==45 and all(a.T*K+K*a==s.zeros(10) for a in metric_basis))
weak=[embed4(a) for a in left]
if args.mutant=='weak-diagonal':
    weak=[embed4(a-b) for a,b in zip(left,right)]
cols=[s.Matrix.vstack(*[flat(comm(a,w)) for w in weak]) for a in metric_basis]
centralizer_equations=s.Matrix.hstack(*cols)
centralizer_rank=centralizer_equations.rank()
check('complete metric centralizer dimension18', 45-centralizer_rank==18)
centralizer_basis=[]
for i in range(6):
    for j in range(i+1,6):
        centralizer_basis.append(unit(10,i,j)-unit(10,j,i))
centralizer_basis += [embed4(a) for a in right]
check('18 independent explicit centralizer generators', s.Matrix.hstack(*map(flat,centralizer_basis)).rank()==18)
check('explicit centralizer commutes weak', all(comm(a,w)==s.zeros(10) for a in centralizer_basis for w in weak))
check('centralizer positive-form skew', all(a.T==-a for a in centralizer_basis))

K1=unit(4,0,3)+unit(4,3,0)
K2=unit(4,1,3)+unit(4,3,1)
J12=unit(4,0,1)-unit(4,1,0)
Y=K2+J12
check('real Lorentz boost adjoint eigenvalue1', Y!=s.zeros(4) and comm(K1,Y)==Y)
check('Lorentz boost and rotation brackets', comm(K1,K2)==J12 and comm(K1,J12)==K2)

# Changing to the diagonal weak subgroup changes the vector representation.
diagonal_weak=[embed4(a-b) for a,b in zip(left,right)]
noncompact_subalgebra=[]
for i in range(3):
    noncompact_subalgebra.append(unit(10,i,6)+unit(10,6,i))
for i in range(3):
    for j in range(i+1,3):
        noncompact_subalgebra.append(unit(10,i,j)-unit(10,j,i))
check('diagonal weak admits noncompact Lorentz control', all(comm(a,w)==s.zeros(10) for a in noncompact_subalgebra for w in diagonal_weak))
check('control really has boosts', noncompact_subalgebra[0].T==noncompact_subalgebra[0] and noncompact_subalgebra[0]!=s.zeros(10))
check('source factor rejects those boosts', any(comm(noncompact_subalgebra[0],w)!=s.zeros(10) for w in [embed4(a) for a in left]))

# Independent small Clifford control, Cl(2,2). This checks the exact generic
# compensation/observation identities, not a second native rank computation.
X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1); J=s.Matrix([[0,1],[-1,0]])
gamma=[s.kronecker_product(X,s.eye(2)), s.kronecker_product(Z,X), s.kronecker_product(Z,J), s.kronecker_product(J,s.eye(2))]
signs=[1,1,-1,-1]
check('Cl22 exact generator relations', all(gamma[i]*gamma[j]+gamma[j]*gamma[i]==(2*signs[i]*I4 if i==j else s.zeros(4)) for i in range(4) for j in range(4)))
r=unit(4,0,1)-unit(4,1,0)
t=gamma[0]*gamma[1]/2
check('normal spin-vector covariance', all(comm(t,gamma[j])==sum((r[i,j]*gamma[i] for i in range(4)),s.zeros(4)) for j in range(4)))
Gamma=s.Matrix.hstack(*gamma)
j=s.Matrix.vstack(*[signs[i]*gamma[i]/4 for i in range(4)])
Pker=s.eye(16)-j*Gamma
check('gamma trace right inverse', Gamma*j==I4)
check('hidden projector exact', Gamma*Pker==s.zeros(4,16) and Pker*Pker==Pker)
Rform=s.kronecker_product(r,I4)
Tspin=s.kronecker_product(I4,t)
Tgeom=Rform+Tspin
if args.mutant=='spin-only-as-geometric': Tgeom=Tspin
check('full geometric gamma intertwiner', Gamma*Tgeom==t*Gamma)
check('spin-only compensation leaves form action', (Rform+Tspin)-Tspin==Rform)
check('fixed-q compensation fails on hidden fields', (Gamma*Rform*Pker).rank()==4)
check('hidden form defect opposite spin defect', Gamma*Rform*Pker==-Gamma*Tspin*Pker)
dotGamma=-t*Gamma+Gamma*Tspin
if args.mutant=='frozen-moving-q': dotGamma=s.zeros(4,16)
check('moving contraction cancels residual form action', dotGamma+Gamma*Rform==s.zeros(4,16))

volume=gamma[0]*gamma[1]*gamma[2]*gamma[3]
vector_columns=s.Matrix.hstack(*map(flat,gamma))
check('higher Clifford parent need not normalize vectors', s.Matrix.hstack(vector_columns,flat(comm(volume,gamma[0]))).rank()>vector_columns.rank())
print(json.dumps({'checks':len(checks),'passed':len(checks),'metric_centralizer_dimension':45-centralizer_rank,'scope':'fixed geometric weak / split metric lift; source realization not inferred','results':checks},indent=2))
