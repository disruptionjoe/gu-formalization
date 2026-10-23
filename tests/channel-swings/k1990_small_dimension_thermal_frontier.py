"""Small-dimension spacing rigidity and the first actual subunit-spacing advantage."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
import k1968_joint_thermal_finite_dimension_program as k
from k1984_commensurate_spectral_rounding import five_level_frontier
from k1981_wide_spacing_thermal_frontier import shell_rank
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1990-small-dimension-thermal-frontier.json'
def produce():
 bs,census,raw=k.blocks(8)
 original=k.patterns
 try:
  k.patterns=lambda d,bs: ((i,) for i,b in enumerate(bs) if len(b[1])<=d)
  seg,counts=k.segments_for(8,bs);curve=k.envelope(seg)
 finally:k.patterns=original
 v=k.evaluate(curve,F(7,5));assert v==F(81,182)
 controls=[]
 for t in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
  for delta in [F(1,100),F(1,2),F(9,10),F(1)]:
   for E in [F(1),F(6,5),F(7,5),F(2),F(3)]:
    q=t*t;lo=max(F(0),(3-E)/2);candidates={lo,F(1)}|{p for p in [1/(2*(1+q)),1/(1+q),(2+q)/(2*(1+q))] if p>=lo}
    val=min(shell_return(t,[F(1),F(3)],[p,1-p]) for p in candidates)
    assert val==five_level_frontier(t,E)
    controls.append(dict(t=str(t),spacing=str(delta),budget=str(E),five_level_optimum=str(val)))
 witness=[]
 for delta in [F(1,100),F(1,20),F(9,100),F(16,165)]:
  alpha=(F(2,5)-delta)/(F(6,5)-delta);spec=sorted(list(map(F,range(5)))+[delta,1+delta,2+delta]);support=[F(1),F(3),1+delta];weights=[F(2,5)*alpha,F(3,5)*alpha,1-alpha]
  assert len(set(spec))==8 and min(b-a for a,b in zip(spec,spec[1:]))==delta and shell_rank(spec,support)
  energy=sum(e*p for e,p in zip(support,weights));ret=shell_return(F(1,2),support,weights)
  assert energy==F(7,5) and ret==F(1,2)-alpha/5 and ret<=v
  witness.append(dict(spacing=str(delta),spectrum=list(map(str,spec)),support=list(map(str,support)),weights=list(map(str,weights)),energy=str(energy),return_error=str(ret),spacing_one_optimum=str(v),strict=ret<v))
 # Actual two-template reduction at delta1/20; compose the full budget curve.
 delta=F(1,20);allseg=dict(seg);extra=[]
 for shifted in [True,False]:
  aa=delta if shifted else F(0);bb=F(0) if shifted else delta
  tagged=[((1+aa,3+aa),tuple(aa+i for i in range(5))),((1+bb,),tuple(bb+i for i in range(3)))]
  original=k.patterns;original_rates=k.rates
  def lattice_rate(g):
   assert F(g).denominator==1 and 1<=g<=3
   return original_rates(int(g))
  try:
   k.rates=lattice_rate
   k.patterns=lambda d,bs: [(0,1)]
   ss,cc=k.segments_for(8,tagged)
  finally:k.patterns=original;k.rates=original_rates
  allseg.update(ss);extra.append(cc)
 fullcurve=k.envelope(allseg)
 assert k.evaluate(fullcurve,F(7,5))==F(109,250)
 optimal=[]
 for delta in [F(1,1000),F(1,100),F(1,20),F(1,4),F(32,125),F(1,3),F(1,2),F(3,4),F(1)]:
  value=min(F(81,182),F(1,2)-F(2,5)/(6+5*delta))
  if delta<=F(32,125):
   alpha=F(2,5)/(F(6,5)+delta);spec=sorted([F(0),F(1),F(2)]+[delta+i for i in range(5)]);support=[1+delta,3+delta,F(1)];weights=[F(2,5)*alpha,F(3,5)*alpha,1-alpha]
   assert shell_rank(spec,support) and min(b-a for a,b in zip(spec,spec[1:]))==delta
   assert sum(e*w for e,w in zip(support,weights))==F(7,5)
   assert shell_return(F(1,2),support,weights)==value
   optimal.append(dict(spacing=str(delta),value=str(value),spectrum=list(map(str,spec)),support=list(map(str,support)),weights=list(map(str,weights))))
  else:optimal.append(dict(spacing=str(delta),value=str(value),attainment='connected spacing1 optimizer from exact curve'))
 return dict(result_id='K1990',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',connected_shape_count=census,distinct_valid_support_count=raw,pareto_blocks=[dict(S=list(s),A=list(a)) for s,a in bs],connected_eight_level_curve=k.encode(curve),exact_curve_census=counts,five_level_controls=controls,eight_level_witnesses=witness,sharp_spacing_transition='32/125',optimal_spacing_controls=optimal,delta_one_twentieth_energy_curve=k.encode(fullcurve),tagged_curve_censuses=extra,scope='For all temperatures0<t<1, every dimension bound3<=d<=7 and0<delta<=1 has the same exact budget optimum as spacing1. Complete all-temperature d<=5 frontier; t=1/2 d6/7 curves transfer from K1968. Dimension8 is sharp: at t=1/2,E=7/5 the complete0<delta<=1 optimum is min(81/182,1/2-2/[5(6+5delta)]), transition32/125, and actual delta1/20 optimum109/250. Complete t=1/2,delta1/20 energy curve executed; all-temperature0<delta<=1/2 reduces to connected spacing1 templates plus two explicit shifted5+3 spectra. No general-temperature closed formula or all-d rate claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py','lab/process/k1968-joint-thermal-finite-dimension-program.json','explorations/conditional-build/k1984-commensurate-spectral-rounding-2026-10-23.md','explorations/conditional-build/k1987-thermal-spacing-parametric-frontier-2026-10-23.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1990',r['connected_shape_count'],'connected shapes;',r['exact_curve_census'],';',len(r['eight_level_witnesses']),'actual noninteger witnesses')
