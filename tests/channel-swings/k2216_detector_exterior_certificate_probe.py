#!/usr/bin/env python3
"""Global minimizer localization and exact all-tail exterior tile consumer."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import k2196_detector_primal_dual_certificates_probe as old
ROOT=Path(__file__).resolve().parents[2]
G=(F(9,10),F(111,100),F(17,25),F(91,100))
def ap(s):return F(41,3)*s-3/s**3
def app(s):return F(41,3)+9/s**4
def correction(h1,h0,fault=None):return (2 if fault=='halfwidth' else 8)*h1*h1+16*h0*h0
def area(q):return (q[1]-q[0])*(q[3]-q[2])
def cover(rects):
 if any(not(G[0]<=a<b<=G[1] and G[2]<=c<d<=G[3]) for a,b,c,d in rects):return False
 for i,a in enumerate(rects):
  for b in rects[i+1:]:
   if max(a[0],b[0])<min(a[1],b[1]) and max(a[2],b[2])<min(a[3],b[3]):return False
 return sum(map(area,rects))==area(G)
def constants(fault=None):
 c={};ck=lambda k,v:c.__setitem__(k,bool(v))
 tail_constant=F(0) if fault=='tail_offset' else old.tail(3,-3,2)
 claimed_w_lower=(F(1,2)-tail_constant)/2
 ck('tail_mass_offset',old.tail(3,-3,2)==F(1,4))
 ck('moment_range',F(1,6)+F(5,6)*F(1,8)==F(13,48) and F(1,6)+F(5,6)*F(1,2)==F(7,12))
 ck('complement_moment_range',F(5,6)-F(7,12)==F(1,4) and F(5,6)-F(13,48)==F(9,16))
 ck('coherence_ratios',1-F(3,13)**2==F(160,169) and 1-F(7,9)**2==F(32,81))
 ck('squeeze_lower',F(17,25)**4<F(9,41))
 ck('squeeze_upper_x',ap(F(111,100))>0 and ap(F(111,100))**2>F(256000,1521))
 ck('squeeze_upper_y',ap(F(91,100))>0 and ap(F(91,100))**2>F(51200,729))
 ck('monotone_lower_x',ap(F(9,10))<F(320,39))
 ck('Hessian_x',F(7,12)*app(G[0])<16)
 ck('Hessian_y',F(9,16)*app(G[2])<32)
 h1,h0=F(1,50),F(1,70)
 # Independent stationary quadratic at a tile corner attains Taylor loss.
 ck('stationary_quadratic_Taylor',correction(h1,h0,fault)==F(1,2)*(16*h1*h1+32*h0*h0))
 # Moment inequality countercontrol e0=0,e1=1/3,e_n=1 thereafter.
 w=old.p(1)/3+F(1,16);d=2*old.p(1)/3+old.tail(3,-1,2)
 ck('mass_lower_attained',w==F(1,8) and d==F(1,2))
 ck('derived_bound_keeps_feasible_profile',claimed_w_lower<=w)
 return c
def consume():
 prior=json.loads((ROOT/'lab/process/k2210-detector-stationary-certificate.json').read_text())
 for p,h in prior['dependency_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
 assert hashlib.sha256((ROOT/'tests/channel-swings/k2210_detector_stationary_certificate_probe.py').read_bytes()).hexdigest()==prior['probe_sha256']
 U=F(prior['certificate']['feasible_energy_upper']);rows=[]
 lo=F(2,3);span=F(113,100)-lo
 assert old.prior.cover_ok(old.prior.INPUTS)
 for idx,row in enumerate(old.prior.INPUTS):
  a,b,c,d=[lo+span*F(v,2**20) for v in row[0]]
  q=(max(a,G[0]),min(b,G[1]),max(c,G[2]),min(d,G[3]))
  if q[0]>=q[1] or q[2]>=q[3]:continue
  e=[F(v,10**15) for v in row[1]]
  u1=[old.root_down(e[n+1]/e[n])/2 for n in range(len(e)-1)]
  u0=[old.root_down((1-e[n+1])/(1-e[n]))/2 for n in range(len(e)-1)]
  eta=F(row[2],10**12);center=((q[0]+q[1])/2,(q[2]+q[3])/2)
  bound=old.dual(*center,u1,u0,eta,F(1,2))-correction((q[1]-q[0])/2,(q[3]-q[2])/2)
  rows.append(dict(source_row=idx,rectangle=list(map(str,q)),stationary_lower=str(bound),margin_over_U=str(bound-U),excluded=bound>U))
 rects=[tuple(map(F,row['rectangle'])) for row in rows];assert cover(rects)
 excluded=[tuple(map(F,row['rectangle'])) for row in rows if row['excluded']]
 remain=[tuple(map(F,row['rectangle'])) for row in rows if not row['excluded']]
 assert remain # A certified existing minimizer prevents an empty candidate region.
 return dict(upper=str(U),G=list(map(str,G)),tiles=rows,excluded_count=len(excluded),retained_count=len(remain),excluded_area=str(sum(map(area,excluded))),retained_area=str(sum(map(area,remain))),retained_hull=list(map(str,[min(q[0] for q in remain),max(q[1] for q in remain),min(q[2] for q in remain),max(q[3] for q in remain)])),global_uniqueness_certified=False)
def main():
 ap0=argparse.ArgumentParser();ap0.add_argument('--write',action='store_true');args=ap0.parse_args()
 c=constants();assert all(c.values()),[k for k,v in c.items() if not v]
 result=consume();rects=[tuple(map(F,r['rectangle'])) for r in result['tiles']]
 c['exact_complete_cover']=cover(rects);c['reject_missing_tile']=not cover(rects[:-1]);c['reject_duplicate_tile']=not cover(rects+[rects[0]])
 faults={}
 for f in ['tail_offset','halfwidth']:
  faults[f]=[k for k,v in constants(f).items() if not v];assert faults[f],f
 faults['missing_exterior_tile']=['exact_complete_cover'] if not cover(rects[:-1]) else []
 assert all(c.values()) and all(faults.values())
 deps=['tests/channel-swings/k2196_detector_primal_dual_certificates_probe.py','tests/channel-swings/k2176_detector_certified_convergence_probe.py','lab/process/k2210-detector-stationary-certificate.json','lab/process/k2213-detector-convex-uniqueness.json','explorations/conditional-build/k2194-detector-optimizer-structure-2026-10-28.md','explorations/conditional-build/k2216-detector-exterior-certificate-2026-10-28.md']
 report=dict(result_id='K2216',status='conditional_global_localization_and_partial_exterior_exclusion',controls=len(c),checks=c,fault_failures=faults,certificate=result,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal all-tail moment/stationarity localization and Taylor minimizer-exclusion theorem; fresh exact consumption of inherited dual inputs on a complete clipped cover; no completed exterior separation or global uniqueness.')
 dst=ROOT/'lab/process/k2216-detector-exterior-certificate.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2216',controls=len(c),excluded=result['excluded_count'],retained=result['retained_count'],retained_hull=result['retained_hull'],faults=faults)))
if __name__=='__main__':main()
