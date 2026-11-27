#!/usr/bin/env python3
"""Exact rational controls, not a replacement for the all-base Koszul proof.
Requires sympy 1.14.0. Root serializes this probe. No external inputs/network.
"""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
Q=s.Rational;n=4;pairs=[(i,j)for i in range(n)for j in range(i,n)]
E=[]
for i,j in pairs:
 a=s.zeros(n);a[i,j]=1;a[j,i]=1;E.append(a)
def coords(a):return [a[i,j]for i,j in pairs]
def tr(a):return s.trace(a)
def sym(a,b):return (a*b.T+b*a.T)/2

def fixture(port=1,rho=1):
 g=port*s.diag(-1,1,1,1);R=[[s.zeros(n)for _ in range(n)]for _ in range(n)]
 # R_0i boost components; spatial terms imposed by algebraic Ricci-flatness.
 lam=[-2*rho,rho,rho]
 for i in range(1,4):
  R[0][i][0,i]=lam[i-1];R[0][i][i,0]=lam[i-1];R[i][0]=-R[0][i]
 for i,j,k in [(1,2,3),(1,3,2),(2,3,1)]:
  R[i][j][i,j]=lam[k-1];R[i][j][j,i]=-lam[k-1];R[j][i]=-R[i][j]
 return g,R

def blocks(y,R):
 P=y.inv()
 def K(U,V):return tr(P*U*P*V)-tr(P*U)*tr(P*V)/2
 def F(U,V):return -(U*P*V+V*P*U)/2
 O=[[R[i][j].T*y+y*R[i][j]for j in range(n)]for i in range(n)]
 II=[[-sym(y[:,i],y[:,j])/2+y[i,j]*y/4 for j in range(n)]for i in range(n)]
 L0=[P*U/2 for U in E];A=[]
 for U in E:
  a=s.zeros(n)
  for i in range(n):
   for k in range(n):a[k,i]=-sum(P[k,l]*K(O[i][l],U)for l in range(n))/2
  A.append(a)
 L=[a+b for a,b in zip(L0,A)]
 # Raw divergence of Omega in constant symmetric coordinates, including fibre LC.
 def divO(i,j):
  out=sum(coords(R[i][j].T*U+U*R[i][j])[a]for a,U in enumerate(E))
  c=coords(O[i][j]);out+=sum(coords(F(U,V))[a]*c[b]for a,U in enumerate(E)for b,V in enumerate(E))
  return s.simplify(out)
 hdelta=s.zeros(n);vdelta=s.zeros(n)
 for i in range(n):
  for j in range(n):
   # tr A_(II+Omega/2)=0, retained as an independently checked identity below.
   hdelta[i,j]=tr(P*O[i][j]/4)
   for k in range(n):
    for a in range(len(E)):
     hdelta[i,j]-=coords(II[k][j])[a]*A[a][k,i]+coords(O[k][j])[a]*L[a][k,i]/2+coords(O[k][i])[a]*L[a][k,j]
     vdelta[i,j]-=coords(II[i][k])[a]*A[a][k,j]+coords(O[i][k])[a]*L[a][k,j]/2
   vdelta[i,j]+=divO(i,j)/2
 bh=s.Matrix(n,n,lambda i,j:-sum(P[k,l]*K(O[i][k],O[j][l])for k in range(n)for l in range(n))/2)
 def derivativeA(U,V):
  dP=-P*U*P;out=s.zeros(n)
  def dK(Z,W):return -tr(P*U*P*Z*P*W+P*Z*P*U*P*W)+(tr(P*U*P*Z)*tr(P*W)+tr(P*Z)*tr(P*U*P*W))/2
  for i in range(n):
   for k in range(n):
    out[k,i]=-sum(dP[k,l]*K(O[i][l],V)+P[k,l]*(dK(O[i][l],V)+K(R[i][l].T*U+U*R[i][l],V))for l in range(n))/2
  return out
 return P,K,F,O,II,L0,A,L,hdelta,vdelta,bh,derivativeA

def run():
 checks=[];samples=[]
 def ck(name,p):
  assert bool(p),name;checks.append(name)
 for port in [1,-1]:
  g,R=fixture(port);ck(f'{port}:R-skew',all(R[i][j].T*g+g*R[i][j]==s.zeros(n)for i in range(n)for j in range(n)))
  ck(f'{port}:Ricci-flat-fixture',all(sum(R[k][i][k,j]for k in range(n))==0 for i in range(n)for j in range(n)))
  ck(f'{port}:first-Bianchi',all(R[i][j][:,k]+R[j][k][:,i]+R[k][i][:,j]==s.zeros(n,1)for i in range(n)for j in range(n)for k in range(n)))
  ys=[('section',g),('normal',g+Q(1,4)*E[0]),('shear',g+Q(1,5)*E[1]+Q(1,7)*E[4]),('conformal',Q(3,2)*g)]
  for label,y in ys:
   P,K,F,O,II,L0,A,L,H,V,bh,dA=blocks(y,R);prefix=f'{port}:{label}'
   ck(prefix+':raw-HH-versus-contracted',H+V==bh)
   ck(prefix+':II-duality',all(K(II[i][j],U)==-U[i,j]/2 for i in range(n)for j in range(n)for U in E))
   ck(prefix+':A-skew',all(a.T*y+y*a==s.zeros(n)for a in A))
   ck(prefix+':cross-traces-zero',all(tr(L0[a]*A[b])==0 for a in range(10)for b in range(10)))
   for ai,bi in [(0,0),(1,1),(0,4),(2,7)]:
    U,W=E[ai],E[bi];fw=F(U,W);ac=sum((c*a for c,a in zip(coords(fw),A)),s.zeros(n))
    raw=tr(ac)-tr(dA(U,W))-tr(L[ai]*L[bi]-L0[ai]*L0[bi])
    ck(prefix+f':raw-VV-{ai}-{bi}',raw==-tr(A[ai]*A[bi]))
   if label in ['section','conformal']:ck(prefix+':zero-response',bh==s.zeros(n)and all(a==s.zeros(n)for a in A))
   if label=='shear':ck(prefix+':omitted-vertical-false-result',H!=bh)
   if label=='normal':
    expected=port*6*Q(1,4)**2/(1-port*Q(1,4));ck(prefix+':Ric00',bh[0,0]==expected)
    gram=s.Matrix(10,10,lambda a,b:K(E[a],E[b]));ginv=gram.inv();vv=s.Matrix(10,10,lambda a,b:-tr(A[a]*A[b]));scalar=tr(P*bh)+sum(ginv[a,b]*vv[a,b]for a in range(10)for b in range(10))
    ck(prefix+':scalar',scalar==-6*Q(1,4)**2/(1-port*Q(1,4))**2)
    ck(prefix+':Einstein00',bh[0,0]-y[0,0]*scalar/2==expected/2)
    samples.append({'port':'K95(-+++)'if port==1 else'K77-flipped(+---)','s':'1/4','delta_Ric00':str(bh[0,0]),'delta_scalar':str(scalar),'delta_Einstein00':str(expected/2)})
 z=s.symbols('s',real=True)
 for port in [1,-1]:
  f=port*6*z*z/(1-port*z);ck(f'{port}:value-first-zero',f.subs(z,0)==0 and s.diff(f,z).subs(z,0)==0);ck(f'{port}:second-jet',s.diff(f,z,2).subs(z,0)==port*12)
 # Native n=2 trace reversal is degenerate, so it cannot calibrate the n=4 metric.
 ck('n2-native-degeneracy',2-Q(1,2)*4==0)
 return {'status':'PASS','checks':len(checks),'check_names':checks,'samples':samples,'verification_scope':'Exact rational full symmetric-basis Koszul trace comparisons at eight native4 fixtures; written proof owns all-base/mixed-derivative theorem. No full printed residual, PDE or physical black-hole test.','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy_version':s.__version__}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--output',type=Path);args=a.parse_args();out=run();txt=json.dumps(out,indent=2)+'\n'
 if args.output:args.output.write_text(txt)
 print(json.dumps({'status':out['status'],'checks':out['checks'],'samples':out['samples']}))
