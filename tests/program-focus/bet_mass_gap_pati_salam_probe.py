#!/usr/bin/env python3
"""Exact controls for the conditional compact PS flat-torus result; not GU physics."""
import itertools, json
import sympy as s
I=s.I
checks=0
def ck(x):
 global checks
 assert bool(x); checks+=1
def centralizer_dim(mats):
 n=mats[0].rows
 # vec column convention; complexification of compact centralizer, remove scalars
 rows=[s.kronecker_product(s.eye(n),a)-s.kronecker_product(a.T,s.eye(n)) for a in mats]
 return n*n-s.Matrix.vstack(*rows).rank()-1
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);U=I*X;V=I*Z
ck(U*V==-V*U);ck(U.det()==1);ck(V.det()==1)
# Full16 central kernel: SU4 centre i^a, each SU2 sign.
kernel=[]
for a,b,c in itertools.product(range(4),range(2),range(2)):
 z=I**a; left=z*(-1)**b; right=z**-1*(-1)**c
 if left==right==1:kernel.append((a,b,c))
 ck((left==1 and right==1)==((a,b,c) in [(0,0,0),(2,1,1)]))
ck(kernel==[(0,0,0),(2,1,1)])
# All7 nonzero alternating forms in3 dimensions have rank2 overF2;
# exhibit basis (a,b,c) with pair1 and radical c by exact F2 search.
def f2rank(a):
 a=[list(map(lambda x:int(x)%2,r)) for r in a.tolist()];k=0
 for j in range(len(a[0])):
  p=next((i for i in range(k,len(a)) if a[i][j]),None)
  if p is None:continue
  a[k],a[p]=a[p],a[k]
  for i in range(len(a)):
   if i!=k and a[i][j]:a[i]=[(x+y)%2 for x,y in zip(a[i],a[k])]
  k+=1
 return k
vec=[s.Matrix(v) for v in itertools.product(range(2),repeat=3) if any(v)]
for a,b,c in itertools.product(range(2),repeat=3):
 m=s.Matrix([[0,a,b],[a,0,c],[b,c,0]])
 ck(f2rank(m)==(2 if any((a,b,c)) else 0))
 if not any((a,b,c)):continue
 found=False
 for u,v,w in itertools.permutations(vec,3):
  P=s.Matrix.hstack(u,v,w)
  if int(P.det())%2 and (P.T*m*P).applyfunc(lambda z:int(z)%2)==s.Matrix([[0,1,0],[1,0,0],[0,0,0]]):
   found=True;break
 ck(found)
# Nonzero flux: the identical two-copy block and distinct third holonomy cases.
A=s.kronecker_product(U,s.eye(2));B=s.kronecker_product(V,s.eye(2))
for C,expected in [(s.eye(4),3),(s.kronecker_product(s.eye(2),I*Z),1)]:
 for Q in [A,B,C]:ck(Q.det()==1);ck(Q.conjugate().T*Q==s.eye(4))
 ck(A*B==-B*A);ck(A*C==C*A);ck(B*C==C*B)
 ck(centralizer_dim([A,B,C])==expected)
 ck(centralizer_dim([U,V,s.eye(2)])==0)
 H=s.kronecker_product(s.eye(2),I*Z)
 ck(H.trace()==0);ck(H.conjugate().T==-H)
 ck(all(Q*H==H*Q for Q in [A,B,C]))
 # Honest16 holonomies commute: correlated minus signs cancel.
 reps=[s.diag(s.kronecker_product(Q,W),s.kronecker_product(s.conjugate(Q),W)) for Q,W in zip([A,B,C],[U,V,s.eye(2)])]
 ck(all(P*Q==Q*P for P,Q in itertools.combinations(reps,2)))
# Zero flux: partitions of4 for SU4, multiplicities for SU2.
for partition in [(4,),(3,1),(2,2),(2,1,1),(1,1,1,1)]:
 d=sum(x*x for x in partition)-1;ck(d>=3)
 for dl,dr in itertools.product([1,3],repeat=2):ck(d+dl+dr>=5)
# Sharp zero-flux representative: diagonal matrices with simple eigenvalues.
D=s.diag(1,-1,I,-I);ck(D.det()==-1)
# multiply by scalar phase to make SU4; commutant unchanged. Use distinct diagonal determinant1 instead.
D=s.diag(1,-1,s.Rational(3,5)+s.Rational(4,5)*I,-s.Rational(3,5)+s.Rational(4,5)*I)
ck(s.expand(D.det())==1);ck((D.conjugate().T*D).applyfunc(s.simplify)==s.eye(4));ck(centralizer_dim([D,s.eye(4),s.eye(4)])==3)
ck(centralizer_dim([I*Z,s.eye(2),s.eye(2)])==1)
# Mutation1: treating the two-dimensional projective irrep as four-dimensional loses H.
mutant_irreducible_four_rejected=(centralizer_dim([A,B,s.kronecker_product(s.eye(2),I*Z)])!=0)
# Mutation2: full Z4 quotient would annihilate matter; central iI cannot cancel with an SU2 sign.
mutant_z4_quotient_rejected=all(I*(-1)**b!=1 for b in [0,1])
# Mutation3: incorrectly subtracting one neutral dimension per factor removes all the sharp twisted fixed space.
mutant_neutral_removal_rejected=(centralizer_dim([A,B,s.kronecker_product(s.eye(2),I*Z)])==1)
ck(mutant_irreducible_four_rejected);ck(mutant_z4_quotient_rejected);ck(mutant_neutral_removal_rejected)
print(json.dumps({'checks':checks,'mutants_rejected':3,'centre_kernel':kernel,'twisted_common_fixed_dimensions':[1,3],'untwisted_minimum':5,'physical_hessian_kernel_dimension':'3*dim(common adjoint fixed space)','scope':'MG1 compact-positive flatT3; no native or quantum result'},indent=2))
