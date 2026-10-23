"""Exact d9 small-spacing templates, component classification and budget curve."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product,combinations
import argparse,json,hashlib
import k1968_joint_thermal_finite_dimension_program as k
from k1981_wide_spacing_thermal_frontier import shell_rank
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1994-nine-level-thermal-reduction.json'
TYPES=[((1,3),tuple(range(5))),((2,3),tuple(range(6))),((1,4),tuple(range(6)))]
def improving_census():
 rows=[]
 for n in [5,6]:
  for gaps in product((1,2,3),repeat=n-1):
   A=[0]
   for g in gaps:A.append(A[-1]+g)
   for S in combinations(A[1:-1],2):
    if S[1]-S[0]<=3 and shell_rank(A,S):
     target=next(s for s,a in TYPES if s[1]-s[0]==S[1]-S[0]);assert target[0]<=S[0]
     rows.append(dict(spectrum=A,support=S,dominating_support=target))
 return rows

def compute(bs,delta,t=F(1,2)):
 op,orr=k.patterns,k.rates
 try:
  def rates(g):
   assert F(g).denominator==1 and 1<=g<=3
   return orr(int(g),t)
  k.rates=rates;k.patterns=lambda d,b:((i,) for i in range(len(b)))
  seg,count=k.segments_for(9,bs);connected=k.envelope(seg);extra=[]
  for S,A in TYPES:
   for shift in [False,True]:
    aa,bb=(delta,F(0)) if shift else (F(0),delta)
    tagged=[(tuple(aa+s for s in S),tuple(aa+a for a in A)),((bb+1,),(bb,bb+1,bb+2))]
    spec=sorted(tagged[0][1]+tagged[1][1]);support=sorted(tagged[0][0]+tagged[1][0])
    assert len(spec)<=9 and len(set(spec))==len(spec) and min(b-a for a,b in zip(spec,spec[1:]))>=delta and shell_rank(spec,support)
    k.patterns=lambda d,b:[(0,1)];ss,cc=k.segments_for(9,tagged);seg.update(ss);extra.append(dict(support=list(map(str,tagged[0][0]+tagged[1][0])),spectrum=list(map(str,spec)),counts=cc))
  return k.envelope(seg),connected,count,extra
 finally:k.patterns=op;k.rates=orr

def produce():
 rows=improving_census();assert len(rows)==17
 bs,census,raw=k.blocks(9);print('census',census,raw,len(bs),flush=True)
 curve,connected,count,templates=compute(bs,F(1,20));print('curve solved',len(curve),flush=True)
 prior=json.loads((ROOT/'lab/process/k1990-small-dimension-thermal-frontier.json').read_text())['delta_one_twentieth_energy_curve']
 old=[{q:(None if v is None else F(v)) for q,v in p.items()} for p in prior]
 cuts=sorted({p['lo'] for p in curve+old}|{p['hi'] for p in curve+old if p['hi'] is not None})
 comparison=[]
 for l,h in zip(cuts,cuts[1:]+[None]):
  x=l+1 if h is None else (l+h)/2
  a=next(p for p in curve if p['lo']<=x and(p['hi'] is None or x<=p['hi']))
  b=next(p for p in old if p['lo']<=x and(p['hi'] is None or x<=p['hi']))
  m=b['slope']-a['slope'];q=b['intercept']-a['intercept']
  assert m*x+q>=0 and m*l+q>=0 and(h is None or m*h+q>=0)
  comparison.append(dict(lo=l,hi=h,benefit_slope=m,benefit_intercept=q))
 return dict(result_id='K1994',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',improving_small_components=rows,connected_shape_count=census,distinct_support_count=raw,pareto_blocks=[dict(S=S,A=A) for S,A in bs],connected_curve=k.encode(connected),small_spacing_curve=k.encode(curve),temperature='1/2',spacing='1/20',curve_census=count,shifted_templates=templates,dimension8_benefit=k.encode(comparison),budget_controls=[dict(energy=str(E),value=str(k.evaluate(curve,E)),connected=str(k.evaluate(connected,E))) for E in [F(1),F(7,5),F(18,11),F(2),F(3),F(4),F(5)]],scope='For every0<t<1,E>=1,0<delta<=1/2, exact dimension9 optimum is minimum of connected integer templates and six actual shifted templates with improving supports1,3 on5 levels;2,3 or1,4 on6 levels; plus pure0,1,2. Complete t1/2 delta1/20 budget curve executed. No delta>1/2 or arbitrary-d claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py','explorations/conditional-build/k1990-small-dimension-thermal-frontier-2026-10-23.md','tests/channel-swings/k1981_wide_spacing_thermal_frontier.py']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=k.encode(produce())
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert d==json.loads(OUT.read_text())
 print('PASS K1994',d['connected_shape_count'],'connected spectra;17 small improving types;six shifted templates;curve',len(d['small_spacing_curve']))
