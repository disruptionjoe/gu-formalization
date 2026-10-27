#!/usr/bin/env python3
"""Original-map mixed Clifford projections; universal proof is in companion note."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from k2159_commutant_equation_adapters_probe import G,I,ETA,W,N,mm,add,scale,C,R,kernel
from k2161_noncentral_adapter_obstruction_probe import blade,port,comm
ROOT=Path(__file__).resolve().parents[2];WM=sum(1<<i for i in W);NM=sum(1<<i for i in N);omega=blade(W)
def pick(a,wd=None,np=None):return {k:v for k,v in a.items() if (wd is None or (k&WM).bit_count()==wd) and (np is None or (k&NM).bit_count()%2==np)}
def interior(g,x):return scale(add(mm(g,x),scale(mm(x,g),-1)),F(1,2))
def exterior(g,x):return scale(add(mm(g,x),mm(x,g)),F(1,2))
def trace(d):return add(*(scale(mm(G[i],d[i]),ETA[i]) for i in W))
def controls(fault=None):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v))
 ck('tangent_volume_square',mm(omega,omega)==scale(I,-1))
 z0=add(blade([3,4,5,6,8,9,10]),scale(blade([4,5,6,8,9,12,13]),F(2,3)))
 z2=add(blade([0,1,3,4,5,6,8]),scale(blade([2,7,3,4,9,10,11]),F(-2)))
 z4=mm(omega,add(blade([3,4,5]),scale(blade([8,9,10]),F(3))))
 # Every summand has a common null normal factor on the left, so the mixture is singular.
 null=add(G[3],G[8]);zs={0:mm(null,blade([4,5,6,9,10,11])),2:mm(blade([0,1]),mm(null,blade([4,5,6,9]))),4:mm(omega,mm(null,blade([4,5])))}
 ck('singular_mixed_fixture',bool(add(*zs.values())) and not mm(null,add(*zs.values())))
 A={j:scale(blade([4,5]),F(j+1,7)) for j in N};B={j:add(scale(G[6],F(j-2,5)),blade([3,4,8])) for j in N};T={j:add(A[j],mm(omega,B[j])) for j in N}
 if fault=='noncommutant':T[3]=add(T[3],G[0])
 ck('full_noncentral_commutant',all(not comm(T[j],G[i]) for j in N for i in W))
 original=proj=traces=parity=smooth=normal=True
 for Z in [{0:z0,2:z2,4:z4},zs]:
  z=add(*Z.values());aa={r:port(zz) for r,zz in Z.items()};a=port(z)
  if fault=='missing_normal_coefficient':a[3]={}
  for j in N:
   e,f=C(a,*kernel(T,j),lower_sign=1 if fault=='reverse_sign' else -1);rr,rv=R(T,e,f)
   L={i:add(e[i],scale(mm(G[i],f),-1)) for i in W}
   pure={i:add(*(add(mm(add(scale(mm(G[i],Z[r]),7-r),scale(aa[r][i],-10-2*r)),T[j]),scale(add(comm(G[i],aa[r][j]),mm(G[i],aa[r][j])),ETA[j])) for r in Z)) for i in W}
   original &= L==pure
   X={r:mm(mm(Z[r],omega),B[j]) for r in Z};Nr={r:scale(aa[r][j],ETA[j]) for r in Z}
   P=add(Nr[0],scale(X[4],-15));Q=add(scale(X[2],5),scale(Nr[2],3));U=add(scale(X[0],7),scale(Nr[4],3));V=add(Nr[2],scale(X[2],-8 if fault=='projection_coefficient' else -9))
   Y={i:add(mm(G[i],P),interior(G[i],Q)) for i in W};V3={i:add(interior(G[i],U),exterior(G[i],V)) for i in W}
   proj &= all(pick(L[i],1,0)==Y[i] and pick(L[i],3,0)==V3[i] for i in W)
   traces &= trace(Y)==add(scale(P,4),scale(Q,2)) and trace(V3)==add(scale(U,4),scale(V,2))
   parity &= all(pick(L[i],np=0)==add(Y[i],V3[i]) for i in W)
   H=add(mm(G[0],T[3]),mm(G[7],T[8]))
   smooth &= all(add(rr[i],mm(G[i],H),scale(mm(G[i],add(rv,H)),-1))==L[i] for i in W)
  normal &= all(add(*(scale(mm(aa[r][j],G[j]),ETA[j]) for j in N))==scale(Z[r],7-r) for r in Z)
 ck('original_coupled_maps',original);ck('mixed_projection_identity',proj);ck('projection_trace_certificates',traces);ck('normal_parity_separation',parity);ck('moving_adapter_cancellation',smooth);ck('right_contraction_degrees',normal)
 # Recover exactly the0+4 equations from trace brackets, including negative metric slots.
 u=add(blade([3,4,5]),blade([8,9,10]));v=z0;ok=True
 for j in N:
  du=exterior(G[j],u);dv=exterior(G[j],v);x0=mm(mm(v,omega),B[j]);x4=mm(mm(mm(omega,u),omega),B[j]);n0=scale(dv,ETA[j]);n4=scale(mm(omega,du),ETA[j])
  ok &= add(n0,scale(x4,-15))==add(scale(dv,ETA[j]),scale(mm(u,B[j]),15))
  ok &= add(scale(x0,7),scale(n4,3))==mm(omega,add(scale(mm(v,B[j]),7),scale(du,3*ETA[j])))
 ck('remaining_0_4_equations',ok)
 # Independently check simplicity's conjugation-character separation on all normal basis blades.
 chars=[]
 for mask in range(1<<len(N)):
  full=sum(1<<j for k,j in enumerate(N) if mask>>k&1);b={full:F(1)};c=[]
  for j in N:
   conjugate=scale(mm(mm(G[j],b),G[j]),ETA[j]);assert list(conjugate)==[full];c.append(conjugate[full])
  chars.append(tuple(c))
 ck('all1024_conjugation_characters_distinct',len(set(chars))==1024 and sum(all(x==1 for x in c) for c in chars)==1)
 # Algebraic constants in the hypothetical invertible branch, not a falsely manufactured solution.
 c2=F(3,5) if fault!='involution_constant' else F(5,3)
 ck('involution_elimination_constants',F(7,15)*F(9,7)==c2 and F(14,10)-c2==F(4,5) and F(14,10)==F(7,5))
 ck('representation_split_nonzero_factor',F(25,4)-1==F(21,4))
 for name,a in [('zero',[{} for _ in G]),('scalar',[scale(I,F(i+1,3)) if i in W else {} for i in range(14)])]:
  ck(name+'_positive_control',all(R(T,*C(a,*kernel(T,j)))==({i:{} for i in W},{}) for j in N))
 return out
FAULTS=['noncommutant','missing_normal_coefficient','reverse_sign','projection_coefficient','involution_constant']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2163-mixed-degree-adapter-obstruction-2026-10-27.md','tests/channel-swings/k2161_noncentral_adapter_obstruction_probe.py','tests/channel-swings/k2159_commutant_equation_adapters_probe.py','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2163',status='conditional_exact_controls',exact_checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Mixed degree projection, right-ideal simplicity, forced invertibility and impossible full Clifford representation proof separately reviewed. Finite fixture controls do not replace universal proof.')
 p=ROOT/'lab/process/k2163-mixed-degree-adapter-obstruction.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2163',checks=len(checks),faults=faults)))
if __name__=='__main__':main()
