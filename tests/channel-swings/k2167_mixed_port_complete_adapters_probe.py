#!/usr/bin/env python3
"""Original sparse Clifford-map checks for mixed degree elimination."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,hashlib,json
import sympy as S
from k2159_commutant_equation_adapters_probe import G,I,ETA,W,N,mm,add,scale,C,kernel
from k2161_noncentral_adapter_obstruction_probe import blade,port
from k2165_even_clifford_adapter_descent_probe import RR
ROOT=Path(__file__).resolve().parents[2];WM=sum(1<<i for i in W);OM=blade(W)
def proj(v,r):return {m:c for m,c in v.items() if (m&WM).bit_count()==r}
def ep(mu,v,r):return proj(mm(G[mu],v),r+1)
def ip(mu,v,r):return proj(mm(G[mu],v),r-1)
def trace(v):return add(*(scale(mm(G[mu],v[mu]),ETA[mu]) for mu in W))
def originals(T,z,j,fault=None):
 aa=port(z)
 if fault=='missing_port':aa[3]={}
 zz,v=kernel(T,j)
 if fault=='kernel_shift':v=add(v,T[j])
 e,f=C(aa,zz,v,lower_sign=1 if fault=='lower_sign' else -1)
 return {mu:add(e[mu],scale(mm(G[mu],f),-1)) for mu in W},e,f

def pencil_adapter(t,fault=None):
 v=blade(N[:7]);u=scale(blade(N[7:]),t);den=49-225*t*t;T={}
 for j in N:
  dv=port(v)[j];du=port(u)[j]
  a=scale(add(scale(mm(v,dv),-7),scale(mm(u,du),-45)),F(ETA[j],den))
  b=scale(add(scale(mm(v,du),-21),scale(mm(u,dv),15)),F(ETA[j],den))
  if fault=='pencil_sign':b=scale(b,-1)
  T[j]=add(a,mm(OM,b))
 return T,add(v,mm(OM,u)),den

def controls(fault=None,census=False):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v))
 aa={j:add(scale(I,F(j+1,11)),blade([N[j%10]]),scale(blade(N[:2]),F(2,3))) for j in N}
 bb={j:add(scale(blade(N[2:4]),F(j+2,13)),G[N[(j+1)%10]]) for j in N}
 T={j:add(aa[j],mm(OM,bb[j])) for j in N}
 z0=add(blade(N[:7]),scale(blade(N[3:10]),F(2)))
 z2=add(mm(blade(W[:2]),blade(N[:5])),scale(mm(blade(W[2:]),blade(N[5:10])),F(3)),mm(blade([W[0],W[2]]),blade(N[2:7])))
 z4=mm(OM,add(blade(N[:3]),scale(blade(N[5:8]),F(-2))))
 zs={0:z0,2:z2,4:z4};z=add(*zs.values());projected=traced=linear=True
 for j in N:
  L,e,f=originals(T,z,j,fault)
  X={r:mm(v,aa[j]) for r,v in zs.items()};Y={r:mm(mm(v,OM),bb[j]) for r,v in zs.items()};D={r:scale(port(v)[j],ETA[j]) for r,v in zs.items()}
  F0=add(scale(X[0],7),scale(Y[4],-15),D[0])
  F2=add(scale(X[2],-9),scale(Y[2],5),scale(D[2],3))
  F4=add(scale(X[4],-15),scale(Y[0],7),scale(D[4],3))
  G2=add(scale(X[2],5),scale(Y[2],-9),D[2])
  for mu in W:
   projected &= proj(L[mu],1)==add(ep(mu,F0,0),ip(mu,F2,2))
   projected &= proj(L[mu],3)==add(ip(mu,F4,4),ep(mu,G2,2))
  t1=trace({mu:proj(L[mu],1) for mu in W});t3=trace({mu:proj(L[mu],3) for mu in W})
  traced &= t1==add(scale(F0,4),scale(F2,2)) and t3==add(scale(F4,4),scale(G2,2))
  # Invert the actual two-equation elimination with nonzero residual retained.
  linear &= add(scale(F2,-F(9,56)),scale(G2,-F(5,56)),scale(D[2],F(4,7)))==X[2]
  linear &= add(scale(F2,-F(5,56)),scale(G2,-F(9,56)),scale(D[2],F(3,7)))==Y[2]
 ck('mixed_original_projection_all40',projected);ck('mixed_metric_traces_all10',traced);ck('residual_sensitive_linear_elimination',linear)
 odd=True
 for r in [1,3]:
  zr=add(mm(blade(W[:r]),blade(N[:7-r])),scale(mm(blade(W[-r:]),blade(N[-(7-r):])),F(2)))
  for j in N:
   L,_,_=originals(T,zr,j,fault);X=mm(zr,aa[j]);Y=mm(mm(zr,OM),bb[j]);D=scale(port(zr)[j],ETA[j])
   for mu in W:
    expected=add(scale(ep(mu,X,r),7-r),scale(ip(mu,X,r),-3*(1+r)),scale(ep(mu,Y,4-r),-3*(1+r)),scale(ip(mu,Y,4-r),7-r),ep(mu,D,r),scale(ip(mu,D,r),3))
    odd &= L[mu]==expected
 ck('odd_nondecomposable_original_degree_formula',odd)
 ck('real_hodge_square_minus_one',mm(OM,OM)==scale(I,-1))
 middle=list(combinations(W,2));hodge=True
 for inds in middle:
  p=blade(inds);jp=mm(p,OM);hodge &= bool(p) and bool(jp) and not set(p)&set(jp) and mm(jp,OM)==scale(p,-1)
 ck('all6_real_middle_hodge_pairs',hodge)
 ck('normal_reconstruction',add(*(scale(mm(G[j],port(z2)[j]),ETA[j]) for j in N))==scale(z2,5))
 recon=True
 for j in N:
  derivative=port(z2)[j]
  if fault=='derivative_factor':derivative=scale(derivative,2)
  recon &= mm(G[j],z2)==add(scale(derivative,2),scale(mm(z2,G[j]),-1))
 ck('left_ideal_closure_identity',recon)
 # Zero and scalar tangential connections survive original full maps, arbitrary A/B.
 for name,conn in [('zero',[{} for _ in G]),('scalar',[scale(I,F(i+1,3)) if i in W else {} for i in range(14)])]:
  ck(name+'_full_map_positive',all(RR(T,*C(conn,*kernel(T,j)))==({mu:{} for mu in W},{}) for j in N))
 # Existing L-only repairs must still fail the full lower row: prevents sufficiency overclaim.
 full=True
 for r,t,fac in [(0,-F(1,7),-F(24,7)),(4,F(1,5),F(32,25))]:
  q=N[:7-r];zz=mm(OM,blade(q)) if r==4 else blade(q);TT={j:scale(G[j],ETA[j]*t) if j in q else {} for j in N}
  for j in N:
   L,e,f=originals(TT,zz,j,fault);_,q0=RR(TT,e,f,'omit_kappa' if fault=='omit_kappa' else None)
   full &= all(not v for v in L.values()) and q0==scale(port(zz)[j],ETA[j]*fac)
 ck('necessary_not_sufficient_lower_row_controls',full)
 # Null normal support yields a genuinely nonzero singular pure normal form.
 null=add(G[3],G[8]);v=mm(null,blade([4,5,6,9,10,11]));u=mm(null,blade([4,5]))
 ck('degenerate_degree0_and4_singular_witnesses',bool(v) and bool(u) and not mm(v,v) and not mm(u,u))
 # Nondecomposable scalar-square pure normal forms: original FULL lower-row identity.
 x3=add(blade(N[:3]),scale(blade(N[3:6]),2));vol=blade(N);square=True;leak=True
 for r,x in [(4,x3),(0,mm(vol,x3))]:
  xx=mm(x,x);square &= len(x)>1 and set(xx)=={0} and xx[0]!=0
  inv=scale(x,1/xx[0]);al={j:mm(mm(inv,G[j]),x) for j in N}
  if fault=='inverse_sign':al={j:scale(v,-1) for j,v in al.items()}
  TT={j:scale(add(G[j],al[j]),ETA[j]*(F(1,10) if r==4 else -F(1,14))) for j in N}
  zz=mm(OM,x) if r==4 else x
  for j in N:
   L,e,f=originals(TT,zz,j);_,q0=RR(TT,e,f)
   kval=add(*(scale(mm(mm(G[i],al[j]),G[i]),ETA[i]) for i in N))
   rhs=scale(mm(x,add(kval,scale(G[j],-48),scale(al[j],-40))),F(ETA[j],28)) if r==0 else scale(mm(mm(OM,x),add(scale(G[j],64),scale(al[j],24),scale(kval,-5))),F(ETA[j],100))
   leak &= all(not val for val in L.values()) and q0==rhs
  leak &= any(RR(TT,*originals(TT,zz,j)[1:])[1] for j in N)
 ck('nondecomposable_scalar_square_controls',square);ck('scalar_square_full_lower_identity',leak)
 # Invertible nonscalar-square controls test the stronger Euler contraction without scalar-square assumptions.
 a=blade([3,4,5]);b=blade([3,6,9]);xx3=add(a,scale(b,2));iv3=scale(add(scale(a,-1),scale(b,2)),F(1,5));general=True
 for r,x,inv in [(4,xx3,iv3),(0,mm(vol,xx3),mm(vol,iv3))]:
  general &= mm(x,inv)==I and mm(inv,x)==I and len(mm(x,x))>1
  als={j:mm(mm(inv,G[j]),x) for j in N};TT={j:scale(add(G[j],als[j]),ETA[j]*(F(1,10) if r==4 else -F(1,14))) for j in N};zz=mm(OM,x) if r==4 else x
  qsum=add(*(scale(mm(RR(TT,*originals(TT,zz,j)[1:])[1],G[j]),ETA[j] if fault=='euler_weight' else 1) for j in N))
  w=mm(x,x);kw=add(*(scale(mm(mm(G[j],w),G[j]),ETA[j]) for j in N))
  rhs=scale(mm(inv,add(kw,scale(w,18))),-F(6,7)) if r==0 else scale(mm(mm(OM,inv),add(scale(kw,3),scale(w,-14))),F(6,25))
  general &= bool(qsum) and qsum==rhs and all(all(not v for v in originals(TT,zz,j)[0].values()) for j in N)
 ck('nonscalar_square_full_lower_euler_contraction',general)
 TT,zz,den=pencil_adapter(F(1),fault);q=RR(TT,*originals(TT,zz,N[0])[1:])[1]
 ck('coupled_pencil_unique_adapter_and_full_leak',all(all(not a for a in originals(TT,zz,j)[0].values()) for j in N) and q=={14479:F(2379,1936),1904:-F(1653,1936)})
 if census:
  chars=[];eig=True;eveneig=True;anti=[]
  for bits in range(1<<10):
   b=blade([N[i] for i in range(10) if bits>>i&1]);sig=[]
   for j in N:
    conjugate=scale(mm(mm(G[j],b),G[j]),ETA[j]);sig.append(1 if conjugate==b else -1)
    assert conjugate==scale(b,sig[-1])
   chars.append(tuple(sig))
   if all(c==-1 for c in sig):anti.append(bits)
   if not bits.bit_count()%2:
    kval=add(*(scale(mm(mm(G[j],b),G[j]),ETA[j]) for j in N));eveneig &= kval==scale(b,10-2*bits.bit_count())
   if bits.bit_count()%2:
    kval=add(*(scale(mm(mm(G[j],b),G[j]),ETA[j]) for j in N));eig &= kval==scale(b,2*bits.bit_count()-10)
  vals0=[];vals4=[]
  for t in map(F,range(6)):
   TT,zz,den=pencil_adapter(t);q=RR(TT,*originals(TT,zz,N[0])[1:])[1]
   vals0.append((t,q.get(1904,0)*den*den));vals4.append((t,q.get(14479,0)*den*den))
  t=S.symbols('t');p0=S.interpolate(vals0,t);p4=S.interpolate(vals4,t)
  want0=-12*(6075*t**4-4557*t*t+686);want4=12*t*(4005*t*t-833)
  b0=-S.Rational(1330995,3303776)*t*t-S.Rational(1,8232);b4=-S.Rational(2018925,3303776)*t**3+S.Rational(78137,235984)*t
  ck('degree5_exact_interpolation_and_bezout',S.expand(p0-want0)==0 and S.expand(p4-want4)==0 and S.expand(b0*p0+b4*p4)==1)
  TT,zz,den=pencil_adapter(F(1,2));q=RR(TT,*originals(TT,zz,N[0])[1:])[1]
  ck('independent_half_ratio_interpolation_control',q.get(1904,0)*den*den==p0.subs(t,S.Rational(1,2)) and q.get(14479,0)*den*den==p4.subs(t,S.Rational(1,2)))
  v=blade(N[:7]);u0=blade(N[7:]);dv=port(v)[N[0]]
  ck('singular_pencils_fail_left_compatibility',bool(mm(v,dv)) and all(49-225*t*t==0 and bool(add(scale(mm(v,dv),-7))) for t in [F(7,15),-F(7,15)]))
  ck('1024_distinct_normal_conjugation_characters',len(set(chars))==1024)
  ck('all512_even_normal_grade_eigenvalues',eveneig);ck('all512_odd_normal_grade_eigenvalues',eig);ck('unique_full_normal_anticommutant_blade',anti==[1023])
 return out
FAULTS=['missing_port','kernel_shift','lower_sign','derivative_factor','omit_kappa','inverse_sign','euler_weight','pencil_sign']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=controls(census=True);assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2167-mixed-port-complete-adapters-2026-10-27.md','tests/channel-swings/k2165_even_clifford_adapter_descent_probe.py','tests/channel-swings/k2161_noncentral_adapter_obstruction_probe.py','tests/channel-swings/k2159_commutant_equation_adapters_probe.py','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2167',status='conditional_exact_controls',exact_checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written tangent projections, normal-bimodule dimension argument, real Hodge obstruction, pure odd/singular extensions and universal full-row Euler/spectral exclusion and degree-bounded exact polynomial/Bézout mixed-family certificate independently reviewed. Finite fixtures are not arbitrary-matrix exhaustion or source certification.')
 dest=ROOT/'lab/process/k2167-mixed-port-complete-adapters.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2167',checks=len(checks),faults=faults)))
if __name__=='__main__':main()
