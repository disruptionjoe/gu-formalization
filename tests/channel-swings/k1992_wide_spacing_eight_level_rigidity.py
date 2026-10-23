"""Complete d8 spacing reduction; exact rational-temperature budget consumers."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json,argparse,hashlib
import k1968_joint_thermal_finite_dimension_program as k
from k1981_wide_spacing_thermal_frontier import shell_rank
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1992-wide-spacing-eight-level-rigidity.json'
def compute(t,delta,blocks):
 oldp,oldr=k.patterns,k.rates
 def rates(g):
  assert F(g).denominator==1 and 1<=g<=3
  return oldr(int(g),t)
 try:
  k.rates=rates;k.patterns=lambda d,bs:((i,) for i in range(len(bs)))
  seg,counts=k.segments_for(8,blocks);connected=k.envelope(seg)
  if delta<=F(1,2):
   for shift in [True,False]:
    a,b=(delta,F(0)) if shift else (F(0),delta)
    tagged=[((1+a,3+a),tuple(a+i for i in range(5))),((1+b,),tuple(b+i for i in range(3)))]
    k.patterns=lambda d,bs:[(0,1)];ss,_=k.segments_for(8,tagged);seg.update(ss)
  return k.envelope(seg),connected,counts
 finally:k.patterns=oldp;k.rates=oldr

def produce():
 prior=json.loads((ROOT/'lab/process/k1990-small-dimension-thermal-frontier.json').read_text());blocks=[(tuple(b['S']),tuple(b['A'])) for b in prior['pareto_blocks']]
 three=[]
 for a,b in product(range(1,4),repeat=2):
  A=[0,a,a+b]
  if shell_rank(A,[a]):three.append(dict(spectrum=A,occupied=a))
 assert len(three)==6
 checks=0
 for t in [F(1,4),F(1,2),F(3,4)]:
  for alpha,p in product([F(i,8) for i in range(9)],repeat=2):
   weights=[1-alpha,alpha*p,alpha*(1-p)]
   tagged=(1-alpha)/2+alpha*shell_return(t,[F(1),F(3)],[p,1-p])
   dense=shell_return(t,[F(1),F(3),F(5)],weights)
   assert shell_rank(list(range(7)),[1,3,5]) and dense<=tagged;checks+=1
   for shape in three:
    offset=F(shape['spectrum'][-1])+F(3,4)
    old_energy=(1-alpha)*shape['occupied']+alpha*(offset+3-2*p)
    new_energy=weights[0]+3*weights[1]+5*weights[2]
    assert new_energy<=old_energy;checks+=1
 curves=[]
 for t in [F(1,3),F(1,2),F(2,3)]:
  for delta in [F(1,2),F(3,4)]:
   curve,connected,count=compute(t,delta,blocks)
   curves.append(dict(temperature=str(t),spacing=str(delta),pieces=k.encode(curve),census=count))
   if t==F(1,2):
    val=k.evaluate(curve,F(18,11))
    assert val==(F(159,374) if delta==F(1,2) else F(97,220))
    assert k.encode(connected)==prior['connected_eight_level_curve']
 E=F(18,11);alpha=F(70,187);spec=sorted([F(0),F(1),F(2)]+[F(1,2)+i for i in range(5)]);S=[F(1),F(3,2),F(7,2)];p=[F(117,187),F(28,187),F(42,187)]
 assert shell_rank(spec,S) and min(b-a for a,b in zip(spec,spec[1:]))==F(1,2)
 assert sum(e*x for e,x in zip(S,p))==E and shell_return(F(1,2),S,p)==F(159,374)
 return dict(result_id='K1992',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',three_level_types=three,dominance_controls=checks,curves=curves,sharp_boundary_witness=dict(temperature='1/2',spacing='1/2',budget=str(E),spectrum=list(map(str,spec)),support=list(map(str,S)),weights=list(map(str,p)),optimum='159/374',right_limit='97/220',right_jump='59/3740'),scope='For every0<t<1, E>=1 and1/2<delta<=1, F8(delta,E,t)=F8(1,E,t). At t1/2,E18/11, delta1/2 optimum159/374 has exact right jump59/3740. Together with K1990 low-spacing templates and K1981 wide spacing, this gives a finite exact program for every d<=8, positive spacing, temperature and budget in the known feasible domain. Rational inputs have attained rational optima. No all-d or symbolic-temperature closed formula claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1990-small-dimension-thermal-frontier.json','tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py','explorations/conditional-build/k1984-commensurate-spectral-rounding-2026-10-23.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1992',r['dominance_controls'],'physical dominance controls;',len(r['curves']),'complete rational budget curves; sharp half-spacing jump',r['sharp_boundary_witness']['right_jump'])
