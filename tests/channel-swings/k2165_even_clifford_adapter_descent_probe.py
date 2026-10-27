#!/usr/bin/env python3
"""Exact original-map controls for normalized even-Clifford adapters."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,hashlib,json
from k2159_commutant_equation_adapters_probe import G,I,ETA,W,N,mm,add,scale,D,A,kernel,C
from k2161_noncentral_adapter_obstruction_probe import blade,port,comm
ROOT=Path(__file__).resolve().parents[2];WM=sum(1<<i for i in W)
def kap(t,mu=0):return scale(mm(mm(G[mu],t),G[mu]),ETA[mu])
def RR(T,e,f,fault=None):
 h=add(*(mm(T[j] if fault=='omit_kappa' else kap(T[j]),e[j]) for j in N))
 return {i:add(e[i],scale(mm(G[i],h),-1)) for i in W},add(f,scale(h,-1))
def Loriginal(T,z,j,fault=None):
 aa=port(z)
 if fault=='missing_normal_port':aa[3]={}
 e,f=C(aa,*kernel(T,j),lower_sign=1 if fault=='reverse_sign' else -1)
 return {i:add(e[i],scale(mm(G[i],f),-1)) for i in W},e,f

def controls(fault=None,census=False):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v));omega=blade(W)
 T={j:{} for j in N};T[3]=add(scale(G[4],F(2,3)),blade([4,5]));T[8]=add(scale(mm(omega,G[9]),F(-1,2)),scale(omega,F(3,7)))
 if fault=='outside_centralizer':T[3]=add(T[3],G[0])
 ck('even_centralizer_and_kappa',all(not comm(T[j],mm(G[a],G[b])) and kap(T[j],a)==kap(T[j],b) for j in N for a,b in combinations(W,2)))
 ck('new_anticommuting_part_present',any(kap(t)!=t for t in T.values()))
 ck('kappa_involutive_multiplicative',all(kap(kap(t))==t for t in T.values()) and kap(mm(T[3],T[8]))==mm(kap(T[3]),kap(T[8])))
 good=section=True
 for mu in W:
  for col in range(15):
   z={i:(I if i==col else {}) for i in range(14)};v=I if col==14 else {}
   good &= D(*A(T,z,v),{mu:1},W)==RR(T,*D(z,v,{mu:1},range(14)),fault)
   if col in W+[14]:section &= A(T,z,v)==({i:z[i] for i in W},v)
 ck('all60_principal_blocks',good);ck('section_right_inverse',section)
 ck('kernel_all10_columns',all(A(T,*kernel(T,j))==({i:{} for i in W},{}) for j in N))
 # Derivative of A computed from original principal operator.
 dT={mu:{} for mu in W};dT[0]=G[3];dT[7]=omega
 H=add(*(scale(mm(G[mu],dT[mu]),ETA[mu]) for mu in W));terms=[]
 for mu in W:terms.append(D({i:mm(G[i],dT[mu]) for i in W},scale(dT[mu],2),{mu:1},W))
 actual=({i:add(*(t[0][i] for t in terms)) for i in W},add(*(t[1] for t in terms)))
 if fault=='omit_derivative':actual=({i:{} for i in W},{})
 ck('moving_product_rule',actual==({i:scale(mm(G[i],H),-1) for i in W},scale(H,-1)) and bool(H))
 # General original-map L identity, including odd r and parameters outside old commutant.
 original=True;parity=True
 for r in range(5):
  z=blade(W[:r]+N[:7-r]);aa=port(z)
  for j in N:
   ll,e,f=Loriginal(T,z,j,fault)
   for mu in W:
    expected=add(mm(add(scale(mm(G[mu],z),7-r),scale(aa[mu],-10-2*r)),T[j]),scale(add(comm(G[mu],aa[j]),mm(G[mu],aa[j])),ETA[j]))
    original &= ll[mu]==expected
   if r%2==0:
    _,q0=RR(T,e,f);parity &= all((mask&WM).bit_count()%2==0 for mask in q0)
 ck('original_L_identity_all_degrees',original);ck('mixed_even_lower_parity',parity and all((m&WM).bit_count()%2==1 for m in H))
 # Full lower-row failure of the necessary-condition repairs, including all normal slots.
 lower=necessary=oddconflict=True
 for r,t,want in [(0,F(-1,7),F(-24,7)),(4,F(1,5),F(32,25))]:
  Q=N[:7-r];z=blade(W[:r]+Q);aa=port(z);TT={j:scale(G[j],t*ETA[j]) if j in Q else {} for j in N}
  for j in N:
   ll,e,f=Loriginal(TT,z,j,fault);necessary &= all(not v for v in ll.values())
   _,q0=RR(TT,e,f,fault);lower &= q0==scale(aa[j],want*ETA[j])
   if j in Q:lower &= bool(q0) and list(mm(q0,q0))==[0]
 ck('r0_r4_pass_necessary_L',necessary);ck('r0_r4_full_lower_leak',lower)
 for r in [1,2,3]:
  z=blade(W[:r]+N[:7-r]);j=N[0];TT={i:{} for i in N};TT[j]=scale(G[j],-F(ETA[j],7-r))
  ll,_,_=Loriginal(TT,z,j,fault);oddconflict &= not ll[W[r]] and bool(ll[W[0]])
 ck('r1_r2_r3_incompatible_forced_values',oddconflict)
 for name,aa in [('zero',[{} for _ in G]),('scalar',[scale(I,F(i+1,3)) if i in W else {} for i in range(14)])]:
  ck(name+'_full_positive_control',all(RR(T,*C(aa,*kernel(T,j)))==({i:{} for i in W},{}) for j in N))
 if census:
  actual=[];plus=minus=0
  for mask in range(1<<14):
   b={mask:F(1)};central=all(not comm(b,mm(G[a],G[c])) for a,c in combinations(W,2))
   want=(mask&WM).bit_count() in (0,4)
   if central:actual.append(mask);plus+=kap(b)==b;minus+=kap(b)==scale(b,-1)
   assert central==want,'centralizer classification'
  ck('complete16384_blade_centralizer',len(actual)==2048 and plus==minus==1024)
  # Every coordinate port: test both original maps at the forced normal column.
  ok=True;count=0
  for inds in combinations(range(14),7):
   count+=1;P=[i for i in inds if i in W];Q=[i for i in inds if i in N];r=len(P);j=Q[0];z=blade(list(inds));aa=port(z)
   t=F(1,5) if r==4 else -F(1,7-r)
   TT={i:scale(G[i],t*ETA[i]) if i in Q else {} for i in N};ll,e,f=Loriginal(TT,z,j)
   if 0<r<4:ok &= any(ll[i] for i in P) and all(not ll[i] for i in W if i not in P)
   else:
    _,q0=RR(TT,e,f);want=F(-24,7) if r==0 else F(32,25)
    ok &= all(not val for val in ll.values()) and q0==scale(aa[j],want*ETA[j]) and bool(q0)
  ck('all3432_coordinate_ports_original_maps',count==3432 and ok)
 return out
FAULTS=['omit_kappa','outside_centralizer','missing_normal_port','reverse_sign','omit_derivative']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=controls(census=True);assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2165-even-clifford-adapter-descent-2026-10-27.md','tests/channel-swings/k2159_commutant_equation_adapters_probe.py','tests/channel-swings/k2161_noncentral_adapter_obstruction_probe.py','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2165',status='conditional_exact_controls',exact_checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Normalized principal classification, product-orthogonal pure-port obstruction and smooth even-parity separation are separately written/reviewed proofs. Exact basis census is not source-operator or physical certification.')
 p=ROOT/'lab/process/k2165-even-clifford-adapter-descent.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2165',checks=len(checks),faults=faults)))
if __name__=='__main__':main()
