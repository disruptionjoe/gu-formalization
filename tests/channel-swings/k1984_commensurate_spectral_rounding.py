"""Exact protocol-preserving spectral rounding and finite physical templates."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import argparse,json,hashlib
from k1981_wide_spacing_thermal_frontier import shell_rank
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1984-commensurate-spectral-rounding.json'
def rounded(spec,h):return [h*(e//h) for e in spec]
def compressed(spec):
 out=[F(0)]
 for a,b in zip(spec,spec[1:]):out.append(out[-1]+min(F(3),b-a))
 return out
def transitions(spec,bath):
 return {(i,b,j,c) for i,e in enumerate(spec) for j,f in enumerate(spec) for b,x in enumerate(bath) for c,y in enumerate(bath) if e+x==f+y}
def five_level_frontier(t,E):
 q=t*t
 if E<1:return None
 ec=(1+2*q)/(1+q);es=(1+4*q)/(1+q);ea=(2+3*q)/(1+q)
 if E<=ec:return (3-E)/4
 if E<=es:return (2+q)/(4*(1+q))
 if E<=ea:return (3-E)/4+q/(2*(1+q))
 return (1+2*q)/(4*(1+q))
def five_controls():
 cases=[]
 for t in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
  q=t*t;a=1/(2*(1+q));b=1/(1+q);c=(2+q)/(2*(1+q))
  ec=3-2*c;es=(1+4*q)/(1+q);ea=3-2*a
  assert 1<ec<es<ea<3 and 0<a<b<c<1
  for E in [F(1),(1+ec)/2,ec,(ec+es)/2,es,(es+ea)/2,ea,F(3),F(4)]:
   lower=max(F(0),(3-E)/2);points={lower,F(1)}|{v for v in [a,b,c] if v>=lower}
   vals=[shell_return(t,[F(1),F(3)],[p,1-p]) for p in points]
   val=min(vals);assert val==five_level_frontier(t,E)
   cases.append(dict(t=str(t),energy=str(E),optimum=str(val)))
 return cases
def produce():
 bath=list(map(F,range(4)));records=[];count=0
 for m in [1,2,3,4]:
  h=F(1,m)
  for shift in [F(53,10),F(57,10),F(101,10)]:
   spec=list(map(F,range(5)))+[shift+i for i in range(5)]
   assert min(b-a for a,b in zip(spec,spec[1:]))>=h
   q=rounded(spec,h);c=compressed(q)
   assert all(a<=b for a,b in zip(c,q)) and all(a<=b for a,b in zip(q,spec))
   assert min(b-a for a,b in zip(c,c[1:]))>=h and c[-1]<=3*(len(c)-1)
   assert transitions(spec,bath)<=transitions(q,bath)<=transitions(c,bath)
   support=[spec[i] for i in [1,3,6,8]];qs=[q[i] for i in [1,3,6,8]];cs=[c[i] for i in [1,3,6,8]];p=[F(1,10),F(2,10),F(3,10),F(4,10)]
   assert shell_rank(spec,support) and shell_rank(q,qs) and shell_rank(c,cs)
   energies=[sum(e*w for e,w in zip(s,p)) for s in [support,qs,cs]]
   returns=[shell_return(F(1,2),s,p) for s in [support,qs,cs]]
   assert energies[2]<=energies[1]<=energies[0] and returns[2]<=returns[1]<=returns[0]
   records.append(dict(h=str(h),original=list(map(str,spec)),rounded=list(map(str,q)),compressed=list(map(str,c)),mean_energies=list(map(str,energies)),optimized_returns=list(map(str,returns))))
   count+=1
 # Exhaust small arbitrary rational spectra; no physical-channel inference from infeasible samples.
 for m in [1,2,3]:
  h=F(1,m)
  for tail in combinations([F(i,6) for i in range(1,31)],3):
   s=[F(0)]+list(tail)
   if min(b-a for a,b in zip(s,s[1:]))<h:continue
   q=rounded(s,h);c=compressed(q)
   assert len(set(q))==len(s) and transitions(s,bath)<=transitions(q,bath)<=transitions(c,bath)
   assert all((b-a)/h>=1 for a,b in zip(c,c[1:])) and c[-1]<=9
   count+=1
 # Sharp hypothesis controls: neither conservation off the bath lattice nor a larger requested spacing survives.
 off_s=[F(0),F(3,2)];off_b=off_s[:];assert not transitions(off_s,off_b)<=transitions(rounded(off_s,F(1)),off_b)
 s=[F(0),F(7,10),F(14,10)];q=rounded(s,F(1,2));assert min(b-a for a,b in zip(q,q[1:]))<F(7,10)
 return dict(result_id='K1984',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=count,physical_families=records,five_level_frontier_controls=five_controls(),scope='Bath energies0,1,2,3 and minimum spacing h=1/m: every real finite spectrum can be rounded to hZ and compressed to gaps in{h,...,3}, preserving any original conserving unitary, exact channel and its return, while lowering mean energy. Finite exact physical template minimization for fixed dimension and budget, and the complete spacing1 at-most-five-level frontier for all0<t<1; no general-dimensional full frontier or exact-energy equivalence.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1978-thermal-spectral-spacing-2026-10-23.md','explorations/conditional-build/k1981-wide-spacing-thermal-frontier-2026-10-23.md','tests/channel-swings/k1950_global_catalyst_energy_certificates_probe.py']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1984',r['exact_controls'],'exact lattice/transition controls;',len(r['physical_families']),'physical families')
