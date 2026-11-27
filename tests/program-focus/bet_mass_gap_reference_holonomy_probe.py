#!/usr/bin/env python3
"""Exact native curvature/compact-reduction controls, not a quantum-gap test."""
from pathlib import Path
import argparse,json,hashlib,sys,time
sys.dont_write_bytecode=True
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
CERT=ROOT/'lab/process/bet-mass-gap-reference-holonomy-certificates.json'

def build():
 out=[]
 def ck(name,b):
  assert b,name
  out.append(name)
 def comm(a,b):return a*b-b*a
 def basis(n):
  z=[]
  for i in range(n):
   for j in range(i,n):
    a=s.zeros(n);a[i,j]=a[j,i]=1;z.append(a)
  return z
 bs=basis(4);A=s.diag(1,-1,0,0);B=s.zeros(4);B[0,1]=1;B[1,0]=-1;C=A+B
 records={}
 for label,y in [('K95',s.diag(-1,1,1,1)),('flipped-K77',s.diag(1,-1,-1,-1))]:
  yi=y.inv();U=y*A;V=y*B;W=y*C
  F=lambda u,v:-(u*yi*v+v*yi*u)/2
  dF=lambda x,u,v:(u*yi*x*yi*v+v*yi*x*yi*u)/2
  R=lambda u,v,w:s.simplify(dF(u,v,w)-dF(v,u,w)+F(u,F(v,w))-F(v,F(u,w)))
  K=lambda u,v:s.trace(yi*u*yi*v)-s.trace(yi*u)*s.trace(yi*v)/2
  dK=lambda x,u,v:-s.trace(yi*x*yi*u*yi*v+yi*u*yi*x*yi*v)+(s.trace(yi*x*yi*u)*s.trace(yi*v)+s.trace(yi*u)*s.trace(yi*x*yi*v))/2
  ck(label+':symmetric-inputs',all(z==z.T for z in [U,V,W]))
  ck(label+':torsion-free',F(U,V)==F(V,U))
  ck(label+':metric-compatibility',all(dK(U,v,w)==K(F(U,v),w)+K(v,F(U,w))for v in bs for w in bs))
  for j,w in enumerate(bs):ck(label+':raw-curvature:'+str(j),R(U,V,w)==-y*comm(comm(yi*U,yi*V),yi*w)/4)
  ck(label+':nonzero-real-eigenvector',W!=s.zeros(4) and R(U,V,W)==W)
  ck(label+':native-null-witness',K(W,W)==0)
  ck(label+':trace-flat',R(U,V,y)==s.zeros(4))
  fixed_y=s.diag(-1,1,1,1);fixed_U=fixed_y*A;fixed_V=fixed_y*B;fixed_W=fixed_y*C
  ck(label+':same-covariant-signature-flip',R(fixed_U,fixed_V,fixed_W)==fixed_W)
  GR=s.Matrix([[K(v,w)for w in bs]for v in bs]);ev=GR.eigenvals();ck(label+':native-6-4',sum(m for v,m in ev.items()if v>0)==6 and sum(m for v,m in ev.items()if v<0)==4)
  # Coordinates in the ten actual symmetric components.
  coords=lambda z:s.Matrix([z[i,j]for i in range(4)for j in range(i,4)])
  RM=s.Matrix.hstack(*(coords(R(U,V,w))for w in bs));ck(label+':curvature-K-skew',RM.T*GR+GR*RM==s.zeros(10))
  ck(label+':not-positive-identity-skew',RM.T+RM!=s.zeros(10))
  records[label]={'curvature_eigenvalues':{str(k):int(v)for k,v in RM.eigenvals().items()},'witness':[[str(v)for v in row]for row in W.tolist()],'witness_eigenvalue':'1','K_witness_norm':'0'}
 # Same-sign2-plane control in full4D: rotations have imaginary, not boost spectrum.
 y=s.diag(-1,1,1,1);yi=y;Ap=s.diag(0,1,-1,0);Bp=s.zeros(4);Bp[1,2]=Bp[2,1]=1
 rot=comm(Ap,Bp);ck('same-sign-rotation',rot.T==-rot and set(rot.eigenvals())=={0,2*s.I,-2*s.I})
 # Positive-metric-fibre control: the same connection preserves a positive q.
 yi=s.eye(4);qp=lambda u,v:s.trace(u*v);Fp=lambda u,v:-(u*v+v*u)/2
 dq=lambda x,u,v:-s.trace(x*u*v+u*x*v)
 ck('Riemannian-fibre-positive-majorant',all(qp(v,v)>0 for v in bs))
 ck('Riemannian-fibre-parallel-majorant',all(dq(A,v,w)==qp(Fp(A,v),w)+qp(v,Fp(A,w))for v in bs for w in bs))
 # Inherited complete14D Nomizu model independently fixes the native vertical seam.
 import source_action_deep_geometry as g
 for i,j in [(5,10),(5,8),(6,12)]:
  rr=g.curvature(i,j);aa=s.Matrix(g.A[i-4]);bb=s.Matrix(g.A[j-4])
  for k in range(4,14):
   actual=sum((s.Rational(rr[a][k])*s.Matrix(g.A[a-4])for a in range(4,14)),s.zeros(4))
   ck(f'native-Nomizu:{i}:{j}:{k}',actual==-comm(comm(aa,bb),s.Matrix(g.A[k-4])))
   ck(f'native-vertical-invariant:{i}:{j}:{k}',all(rr[a][k]==0 for a in range(4)))
 # Section normal connection rho(L)w=-L^T w-w L: a boost has a real eigenvector.
 eta=s.diag(-1,1,1,1);L=s.zeros(4);L[0,1]=L[1,0]=1;v=s.Matrix([1,-1,0,0]);w=v*v.T
 ck('Lorentz-boost',L.T*eta+eta*L==s.zeros(4))
 ck('Sym2-boost-real-eigenvalue',-L.T*w-w*L==2*w)
 # A Lorentz boost is not positive-Hermitian-unitary on a finite spin fibre.
 # Ordinary Dirac's positive Cauchy norm is separately defined, not a parallel fibre norm.
 spin=s.diag(s.Rational(1,2),-s.Rational(1,2));J=s.Matrix([[0,1],[1,0]])
 ck('Dirac-boost-Krein-control',spin.T*J+J*spin==s.zeros(2))
 ck('Dirac-boost-no-positive-identity',spin.T+spin!=s.zeros(2))
 # Positive section control: rotations preserve Euclidean q and the timelike line.
 L=s.zeros(4);L[1,2]=1;L[2,1]=-1
 ck('ultrastatic-rotation-control',L.T+L==s.zeros(4) and L*s.Matrix([1,0,0,0])==s.zeros(4,1))
 # Scalar-curvature witness must be invariant under simultaneous frame transport.
 H=s.Matrix([[1,1],[0,1]]);R=s.diag(1,-1);z=s.Matrix([1,0]);Rp=H.inv()*R*H;zp=H.inv()*z
 ck('conjugated-curvature-witness',Rp*zp==zp)
 inp=['tests/program-focus/source_action_deep_geometry.py','explorations/conditional-build/source-chimeric-trace-compatibility-2026-11-13.md','explorations/conditional-build/printed-endpoint-analytic-branch-2026-11-27.md']
 return {'status':'PASS','checks':len(out),'check_names':out,'native_ports':records,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in inp},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy_version':s.__version__,'scope':'Exact local curvature and representation controls; holonomy equivalence and perturbation openness are written proofs. No source physical quotient, positive Cauchy norm or quantum gap is inferred.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write-certificate',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t=time.monotonic();d=build()
 if a.write_certificate:CERT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(CERT.read_text())==d,'certificate differs'
 print(json.dumps({'status':'PASS','checks':d['checks'],'ports':d['native_ports'],'seconds':time.monotonic()-t}))
