#!/usr/bin/env python3
"""Reduced exact Cl(2,2) controls, not a native S128 assembly.
Complex 4x4 matrices are doubled to rational real 8x8 matrices. The Hermitian
pairing is represented by its real part. All tested unitary F/U spaces in this
small comparator are solved by exact rational elimination. The universal
Clifford theorem and native rank transfer remain written/reviewed inputs.
Run with python-flint available; no sympy dependency.
"""
import argparse,itertools,json,time
from flint import fmpq_mat as M

def eye(n):return M([[int(i==j)for j in range(n)]for i in range(n)])
def kron(a,b):return M([[a[i//b.nrows(),j//b.ncols()]*b[i%b.nrows(),j%b.ncols()]for j in range(a.ncols()*b.ncols())]for i in range(a.nrows()*b.nrows())])
def block(a,b,c,d):return M([[ (a if i<a.nrows() and j<a.ncols() else b if i<a.nrows() else c if j<a.ncols() else d)[i%a.nrows(),j%a.ncols()]for j in range(a.ncols()*2)]for i in range(a.nrows()*2)])
def total(v):return sum(v[1:],v[0])
def flat(a):return [a[i,j]for i in range(a.nrows())for j in range(a.ncols())]
def kernel(a):
 rr,rank=a.rref();piv=[next(j for j in range(rr.ncols())if rr[i,j])for i in range(rank)];free=[j for j in range(rr.ncols())if j not in piv];out=[]
 for j in free:
  v=[0]*rr.ncols();v[j]=1
  for i,p in enumerate(piv):v[p]=-rr[i,j]
  out.append(v)
 return out

def run():
 checks={}
 def ok(name,value):
  checks[name]=bool(value)
  if not value:raise AssertionError(name)
 I2=eye(2);X=M([[0,1],[1,0]]);Z=M([[1,0],[0,-1]]);J=M([[0,1],[-1,0]])
 real=[kron(X,I2),kron(Z,X),kron(Z,J),kron(J,I2)];z4=M(4,4);I4=eye(4)
 gam=[block(a,z4,z4,a)for a in real];I=eye(8);zi=M(8,8);ii=block(z4,-I4,I4,z4);eta=[1,1,-1,-1];H=[0,1];N=[2,3];m=2
 omega=gam[0]*gam[1]*gam[2]*gam[3];P=(I+omega)/2;Q=(I-omega)/2
 B=real[2]*real[3];pair=block(z4,-B,B,z4)
 ok('Clifford relations',all(gam[i]*gam[j]+gam[j]*gam[i]==(2*eta[i]*I if i==j else zi)for i in range(4)for j in range(4)))
 ok('complex doubling',ii*ii==-I and all(ii*g==g*ii for g in gam))
 ok('chirality',omega*omega==I and all(omega*g==-g*omega for g in gam))
 # All observed columns: two horizontal spinors, one normal insertion,
 # one scalar. Independent real/imaginary coordinates are included.
 cols=32;z=[]
 for a in range(4):
  v=M(8,cols)
  if a in H:
   for i in range(8):v[i,8*a+i]=1
  else:
   for i in range(8):
    for j in range(8):v[i,16+j]=gam[a][i,j]
  z.append(v)
 nu=M(8,cols)
 for i in range(8):nu[i,24+i]=1
 def gamma(zz):return total([eta[j]*gam[j]*zz[j]for j in range(4)])
 def pk(out):
  tr=total([eta[j]*gam[j]*out[j]for j in N])
  return [out[j]-gam[j]*tr/m for j in N]
 def response(K,W):
  result=[M(8,cols)for _ in range(4)]
  for i in range(4):
   v=[K[i]*a for a in z];vnu=K[i]*nu;gv=gamma([W*a for a in v]);cx=eta[i]*gam[i]
   for a in range(4):
    result[a]+=cx*W*v[a]-(gv if a==i else M(8,cols))+gam[a]*(cx*gv-eta[i]*W*v[i])+(vnu if a==i else M(8,cols))
  return pk(result)
 cliff=[]
 for bits in itertools.product([0,1],repeat=4):
  a=I
  for j,b in enumerate(bits):
   if b:a=a*gam[j]
  cliff.extend([a,ii*a])
 ok('full complex endomorphism basis',M([flat(a)for a in cliff]).rank()==32)
 dimensions={}; cases=0
 for kap,form in [(1,pair),(-1,pair*omega)]:
  inv=form.inv()
  def dag(a):return inv*a.transpose()*form
  ok(f'Hermitian Clifford convention {kap}',form.transpose()==form and all(dag(a)==kap*a for a in gam))
  columns=[sum([flat(a*gam[r]+kap*gam[r]*dag(a))for r in N],[])for a in cliff]
  cf=M(columns).transpose();fb=[total([a*v for a,v in zip(cliff,c)])for c in kernel(cf)]
  columns=[flat(dag(a)+a)+flat(a*gam[2]*gam[3]-gam[2]*gam[3]*a)for a in cliff]
  cb=M(columns).transpose();ub=[total([a*v for a,v in zip(cliff,c)])for c in kernel(cb)]
  dimensions[str(kap)]={'normal_F_real_dimension':len(fb),'tangent_U_real_dimension':len(ub)}
  ok(f'nontrivial full homogeneous spaces {kap}',bool(fb) and bool(ub))
  ok(f'F even-normal commutant {kap}',all(a*gam[2]*gam[3]==gam[2]*gam[3]*a for a in fb))
  ok(f'F dagger second relation {kap}',all(dag(a)*gam[r]==-kap*gam[r]*a for a in fb for r in N))
  families=[]
  for f in fb:
   K=[zi,zi,f*gam[2],f*gam[3]];families.append(K)
   ok(f'normal unitary {kap} {len(families)}',all(dag(a)==-a for a in K))
  for h in H:
   for u in ub:
    K=[zi,zi,zi,zi];K[h]=u;families.append(K)
  witness=ii if kap==1 else I
  ok(f'explicit non-Spin F witness {kap}',all(witness*gam[r]+kap*gam[r]*dag(witness)==zi for r in N))
  ok(f'contains beyond metric-spin {kap}',any(any(a*omega!=omega*a for a in K)for K in families))
  for wi,(wp,wm) in enumerate([(1,1),(2,3),(1,-2)]):
   W=wp*P+wm*Q
   for k,K in enumerate(families):
    actual=response(K,W);ok(f'all observed columns killed {kap} W{wi} K{k}',all(a==M(8,cols)for a in actual));cases+=1
 # Outside the classified one-way survivor: an isolated unitary normal value.
 K=[zi,zi,ii,zi];mut=response(K,2*P+3*Q)
 ok('outside survivor mutation detected',any(a!=M(8,cols)for a in mut))
 # Shape control with tracefree nonzero II; H=0 is not total geodesicity.
 A=[M(8,16),M(8,16)]
 for i in range(8):
  for j in range(8):A[0][i,j]=gam[0][i,j];A[0][i,8+j]=-gam[1][i,j]
 tr=eta[2]*gam[2]*A[0]+eta[3]*gam[3]*A[1];shape=[A[r]-gam[N[r]]*tr/m for r in range(2)]
 mat=M([list(a[i,j]for j in range(16))for a in shape for i in range(8)])
 ok('tracefree nonzero shape remains',mat.rank()>0)
 # The same shape projection must kill pure normal insertion, while it
 # retains the tracefree shape above. This also checks the eta signs.
 insertion=[gam[r]*eye(8) for r in N]
 itr=total([eta[r]*gam[r]*insertion[j] for j,r in enumerate(N)])
 ok('pure insertion zero shape control',all(insertion[j]-gam[r]*itr/m==zi for j,r in enumerate(N)))
 return {'checks':checks,'grouped_checks':len(checks),'full_observed_input_cases':cases,'homogeneous_space_dimensions':dimensions,'tracefree_shape_real_rank':mat.rank(),'scope':'Exact small Cl(2,2) comparator; no native128 operator or physical barred-domain certificate.'}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');p.parse_args();start=time.perf_counter();d=run();d['runtime_seconds']=time.perf_counter()-start;print(json.dumps(d,indent=2))
