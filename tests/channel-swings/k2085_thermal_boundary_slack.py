"""Exact threshold-13 uniform certificates; reuse certified arrangement geometry."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
BREF='lab/process/k2045-third-thermal-spacing-phase.json'
# Fixed inherited assignment file; no ambiguous filename fallback.
def inputs():
 refs=['lab/process/k2059-energy-aware-thermal-tail.json']
 refs += ['lab/process/'+s+'.json' for s in ['k2066-thermal-terminal-response','k2070-joint-terminal-thermal-bound','k2072-compulsory-ladder-thermal-bound','k2074-subdivided-incoming-thermal-bound','k2083-thermal-certificate-strengthening']]
 first=json.loads((ROOT/refs[0]).read_text());ass=list(first['assignments'])
 for ref in refs[1:]:
  d=json.loads((ROOT/ref).read_text())
  for ci,v in d['replacements'].items():ass[int(ci)]=v
 return json.loads((ROOT/BREF).read_text())['bank'],ass,d,refs
A={1:F(14,55),2:F(1,8),3:F(3,55)}
def beta(s):
 r=s[-1]-s[-2] if len(s)>1 else 4
 return max([F(0)]+[A[g] for g in A if s[-1]+g>=12 and r+g>=4])
def verify(ci,v,bank):
 a,t,eta=F(v['a']),-F(v['s']),F(v['eta']);ell=F(v['shift']);tail=F(v['tail_floor'])
 assert bank[ci]['s']==([1,3,5,7,9] if ci==163 else [1,3,5,7,9,11]) and ell==(8 if ci==163 else 10),'fixed support/offset'
 assert tail==min(bank[ci]['s'][-1]+g for g in A if bank[ci]['s'][-1]+g>=12 and 2+g>=4),'true low erased energy'
 assert ci!=163 or F(v['boundary_shift'])==F(14,1265),'gap3 boundary shift'
 assert 0<=eta<=F(4,25) and 0<t<eta and a-tail*t<=eta and a-(12+ell)*t<=eta,'tail transfer'
 low=[F(x['value'])-eta*beta(bank[ci]['s'])*F(x['p'][-1])-a+t*(F(x['energy'])+F(v.get('boundary_shift','0'))*F(x['p'][-1])) for x in bank[ci]['vertices']]
 high=[F(x['value'])-eta*beta(c['s'])*F(x['p'][-1])-a+t*(F(x['energy'])+ell) for c in bank for x in c['vertices']]
 assert min(low)>=0 and min(high)>=0,'all low/high vertex inequalities'
 return dict(low_vertices=len(low),high_vertices=len(high),minimum_high_slack=str(min(high)),low_contacts=[i for i,x in enumerate(low) if not x])
def produce():
 bank,ass,prev,refs=inputs();rep={};counts={}
 for ci,a,t in [(163,F(54556082,176056025),F(4397853,352112050)),(185,F(47198,153775),F(1738,153775)),(186,F(212341,691675),F(7821,691675))]:
  v=dict(kind='uniform_true_tail',a=str(a),s=str(-t),eta='4/25',shift=(8 if ci==163 else 10),tail_floor=(12 if ci==163 else 13),boundary_shift=('14/1265' if ci==163 else '0'));counts[str(ci)]=verify(ci,v,bank);rep[str(ci)]=v;ass[ci]=v
 a,s=map(F,prev['lower_line']);left,right=F(0),F(100)
 for v in ass:
  da,ds=F(v['a'])-a,F(v['s'])-s
  if ds>0:left=max(left,-da/ds)
  elif ds<0:right=min(right,-da/ds)
  else:assert da>=0
 return dict(id='K2085',scope='conditional thermal certificate; analytic transfer and independent review required',inputs={r:hashlib.sha256((ROOT/r).read_bytes()).hexdigest() for r in refs+[BREF,'lab/process/k2068-thermal-population-construction.json','lab/process/k2075-thermal-equality-rigidity.json']},replacements=rep,counts=counts,lower_line=prev['lower_line'],previous_interval=prev['interval'],interval=list(map(str,[left,right])),ties=[[i for i,v in enumerate(ass) if F(v['a'])+E*F(v['s'])==a+E*s] for E in [left,right]])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=produce();out=ROOT/'lab/process/k2085-thermal-boundary-slack.json'
 if args.write:out.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(out.read_text())==d
 print('PASS',d['interval'],d['ties'],d['counts'])
