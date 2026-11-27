#!/usr/bin/env python3
"""Exact finite controls for the normal-jet theorem; not a smooth PDE proof.
Variables t,x,y,r: two observed coordinates, a second normal coordinate y,
and the eliminated normal coordinate r. Rational polynomials only. Polynomial
cutoffs below have finite boundary regularity; smooth cutoff existence is written.
"""
from fractions import Fraction as Q
from math import factorial
import json,time

Z=(0,0,0,0)
class P(dict):
 def __init__(self,d=None):super().__init__({tuple(k):Q(v)for k,v in (d or {}).items()if v})
 def __add__(self,b):
  d=dict(self)
  for k,v in b.items():d[k]=d.get(k,Q(0))+v
  return P(d)
 def __neg__(self):return P({k:-v for k,v in self.items()})
 def __sub__(self,b):return self+-b
 def __mul__(self,b):
  d={}
  for k,v in self.items():
   for l,w in b.items():
    m=tuple(a+c for a,c in zip(k,l));d[m]=d.get(m,Q(0))+v*w
  return P(d)
 def __pow__(self,n):
  z=P({Z:1})
  for _ in range(n):z=z*self
  return z
 def scale(self,c):return P({k:c*v for k,v in self.items()})
 def diff(self,i):
  d={}
  for k,v in self.items():
   if k[i]:
    l=list(k);l[i]-=1;d[tuple(l)]=v*k[i]
  return P(d)
 def at(self,i,a):
  d={}
  for k,v in self.items():
   l=list(k);l[i]=0;l=tuple(l);d[l]=d.get(l,Q(0))+v*Q(a)**k[i]
  return P(d)
 def coeff(self,i,j):return P({tuple(0 if a==i else v for a,v in enumerate(k)):c for k,c in self.items()if k[i]==j})
 def integ(self,i):
  d={}
  for k,v in self.items():
   l=list(k);l[i]+=1;d[tuple(l)]=v/Q(l[i])
  return P(d)
 def restrict(self):return self.at(2,0).at(3,0)
 def evaluate(self,point):
  s=Q(0)
  for k,v in self.items():
   for a,m in zip(point,k):v*=Q(a)**m
   s+=v
  return s

def vadd(a,b):return [x+y for x,y in zip(a,b)]
def vneg(v):return [-x for x in v]
def smul(p,v):return [p*x for x in v]
def mv(M,v):return [sum((p*x for p,x in zip(row,v)),P())for row in M]
def vd(v,i):return [p.diff(i)for p in v]
def vc(v,i,j):return [p.coeff(i,j)for p in v]
def va(v,i,j):return [p.at(i,j)for p in v]
def zero(v):return all(not p for p in v)
def record(v):return [[[list(k),str(c)]for k,c in sorted(p.items())]for p in v]

def run():
 start=time.perf_counter();checks={};cert=[]
 def ck(n,b):assert b,n;checks[n]=bool(b)
 one=P({Z:1});vars=[]
 for i in range(4):k=[0]*4;k[i]=1;vars.append(P({tuple(k):1}))
 t,x,y,r=vars;nil=[[P(),one],[P(),P()]];low=[[P(),P()],[one,P()]];diag=[[one,P()],[P(),-one]]
 ck('engine_derivative',(r**3).diff(3)==(r**2).scale(3))
 ck('engine_integral',(x*x).integ(1).diff(1)==x*x)
 ck('engine_mixed_commute',(t*x*y*r**3).diff(2).diff(3)==(t*x*y*r**3).diff(3).diff(2))
 for seed in range(1,5):
  v=[[t*x+(r**seed)*y,x*x+r*t],[y*x+r*r, t*y+r*x],[t+r*y**2, x*y+r**seed]]
  v=[[p.scale(seed)+one.scale(i+1)for p in a]for i,a in enumerate(v)]
  w0=[t*t+y*x, x**2+y**2]
  At=[[P(),P()],[(one+y),P()]]
  Ax=[[(one+x+r),P()],[P(),-(one+x+r)]]
  Ay=[[P(),t],[(r+y),P()]]
  As=[At,Ax,Ay];Ar=[[P(),one+t+r],[P(),P()]];h=r*(one+t)+(r*r).scale(Q(1,2))
  rhs=[P(),P()]
  for a in range(3):rhs=vadd(rhs,vneg(vadd(vd(v[a],a),mv(As[a],v[a]))))
  forcing=vadd(rhs,smul(h,mv(nil,rhs)));inside=vadd(w0,[p.integ(3)for p in forcing]);w=vadd(inside,vneg(smul(h,mv(nil,inside))))
  ck(f'ODE_exact_variable_nonabelian_{seed}',zero(vadd(vd(w,3),vadd(mv(Ar,w),vneg(rhs)))))
  ck(f'initial_datum_{seed}',va(w,3,0)==w0)
  coeff=[w0]
  for m in range(7):
   acc=vc(rhs,3,m)
   for l in range(m+1):acc=vadd(acc,vneg(mv([[p.coeff(3,l)for p in row]for row in Ar],coeff[m-l])))
   coeff.append([p.scale(Q(1,m+1))for p in acc])
   ck(f'recursion_match_seed{seed}_order{m+1}',coeff[-1]==vc(w,3,m+1))
   ck(f'mixed_y_then_x_seed{seed}_order{m+1}',[p.diff(2).diff(1).restrict()for p in coeff[-1]]==[p.diff(2).diff(1).restrict()for p in vc(w,3,m+1)])
  ck(f'planted_wrong_sign_recursion_{seed}',vc(w,3,1)!=vadd(vc(rhs,3,0),mv([[p.at(3,0)for p in row]for row in Ar],w0)))
  mu=one+x*x+y*y+r*r
  for eps in [-1,1]:
   eta=[-1,1,1,eps];flux=v+[w];connection=As+[Ar];num=[P(),P()]
   for i in range(4):
    p=[a.scale(eta[i])for a in flux[i]]
    quotient_der=vadd(smul(mu,vd(p,i)),vneg(smul(mu.diff(i),p)))
    expanded=vadd(quotient_der,vadd(smul(mu.diff(i),p),smul(mu,mv(connection[i],p))))
    num=vadd(num,[a.scale(eta[i])for a in expanded])
   ck(f'weighted_lowered_sign_{seed}_{eps}',zero(num))
  # Readout genuinely uses a normal derivative and a transverse-normal derivative.
  f=w[0].diff(3).restrict()+v[1][1].diff(2).restrict()
  energy=f.diff(1).diff(1);spatial=-f.diff(0).diff(1)
  ck(f'normal_jet_improvement_conserved_{seed}',not energy.diff(0)+spatial.diff(1))
  ck(f'normal_jet_readout_nonzero_{seed}',bool(energy)or bool(spatial))
  cert.append({'seed':seed,'r_coefficients_w': [record(c)for c in coeff[:4]]})
 # Coefficients indexed by all finite normal multiindices are independently realized.
 for order in range(6):
  values={(j,b):(t**(j%2+1)+x**(b%3+1)).scale(1+j+2*b)for j in range(order+1)for b in range(order+1-j)}
  extension=P()
  for (j,b),c in values.items():extension+=c*(r**j)*(y**b)
  recovered={}
  for (j,b),c in values.items():
   p=extension
   for _ in range(j):p=p.diff(3)
   for _ in range(b):p=p.diff(2)
   recovered[(j,b)]=p.restrict().scale(Q(1,factorial(j)*factorial(b)))
  ck(f'independent_normal_coefficients_order{order}',values==recovered)
 # Flat, same-oneform boundary countercontrol: no normal flux => transport is an extra equation.
 f=(one-(x-t)**2)**4;cut=one-t*t;current=[f,f]
 ck('zero_all_normal_flux_transport_conserved',not f.diff(0)+f.diff(1))
 q=(f.at(0,0).integ(1).at(1,1)-f.at(0,0).integ(1).at(1,-1)).evaluate([0,0,0,0])
 ck('transport_compact_positive_charge',q>0)
 broken=(cut*f).diff(0)+(cut*f).diff(1)
 ck('time_cutoff_breaks_zero_flux_domain',bool(broken))
 compensated=-r*broken
 ck('normal_flux_restores_coclosure',not broken+compensated.diff(3))
 ck('compensation_leaves_zero_normal_flux_class',bool(compensated))
 # Compact free normal coefficient produces a nonzero current with zero charge.
 ffree=(one-t*t)**4*(one-x*x)**4
 ej=ffree.diff(1).diff(1);jj=-ffree.diff(0).diff(1)
 ck('compact_normal_data_improvement_divergence',not ej.diff(0)+jj.diff(1))
 qzero=ej.integ(1).at(1,1)-ej.integ(1).at(1,-1)
 ck('compact_normal_data_charge_zero',not qzero)
 ck('compact_normal_data_boundary_zero',all(not jj.at(1,a)for a in [-1,1])and not ej.at(0,1))
 ck('compact_normal_data_both_signs',ej.evaluate([0,0,0,0])<0 and ej.evaluate([0,Q(1,2),0,0])>0)
 return {'status':'PASS','grouped_checks':len(checks),'checks':checks,'variable_connection_certificates':cert,'positive_flux_restricted_charge':str(q),'runtime_seconds':time.perf_counter()-start,'scope':'Rational polynomial controls of finite recursion, mixed jets, variable connection, weights/signs and domain distinction. Universal smooth germ/support theorem is written and reviewed; polynomial cutoffs only finite boundary calibration, no actual source physical admission.'}
if __name__=='__main__':print(json.dumps(run(),indent=2))
