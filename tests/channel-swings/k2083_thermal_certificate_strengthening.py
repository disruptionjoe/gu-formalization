"""Selective exact terminal expansion for the two K2074 endpoint competitors."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('k2074',ROOT/'tests/channel-swings/k2074_subdivided_incoming_thermal_bound.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
o=p.o
PREFIXES={(2,2,2),(2,2,3),(2,3,2),(3,1,3),(3,2,2)}

def setup():
 prev=json.loads((ROOT/'lab/process/k2074-subdivided-incoming-thermal-bound.json').read_text())
 q2=json.loads((ROOT/'lab/process/k2072-compulsory-ladder-thermal-bound.json').read_text());q0=json.loads((ROOT/'lab/process/k2070-joint-terminal-thermal-bound.json').read_text())
 for doc in [prev,q2,q0]:
  for path,digest in doc['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'inherited input changed'
 q4=p.decode(q2['quad_arrangements']);q4.update(p.decode(prev['quad_arrangements']))
 for ds in sorted(PREFIXES):
  for h in o.b.K:
   g=(*ds,h)
   if ds[-1]+h>=4 and g not in q4:
    print('geometry',g,flush=True);q4[g]=p.RAW_FOUR(g)
 p.k.four_geometry=lambda g:q4[tuple(g)]
 g3=p.decode(q0['triple_arrangements']);g2=p.decode(q0['arrangements'])
 o.triple_geometry=lambda g:g3[tuple(g)];o.arrangement=lambda d,e:g2[d,e];o.b.shift=p.k.shift
 p.EXTENDED[188]=PREFIXES
 return prev,q4

def constraints(ci,seed):
 if ci==235:return p.k.BASE_CONSTRAINTS(ci,seed)
 assert ci==188
 return [row for row in p.correlated_constraints(ci,seed) if row[3]!=('fourthpluscap',20,2)]

def produce():
 prev,q4=setup();ass=list(o.one.old['assignments'])
 for slug in ['k2066-thermal-terminal-response','k2070-joint-terminal-thermal-bound','k2072-compulsory-ladder-thermal-bound','k2074-subdivided-incoming-thermal-bound']:
  for ci,v in json.loads((ROOT/f'lab/process/{slug}.json').read_text())['replacements'].items():ass[int(ci)]=v
 o.worst_incoming_constraints=constraints
 replacements={}
 for ci in [235,188]:
  r=o.solve(ci,[F(ass[ci]['a']),-F(ass[ci]['s'])]);r['common_tail_weight']='0' if ci==235 else str(p.THETA);r.pop('mixture');print('certified',ci,r['a'],r['s'],r['active_tag'],flush=True)
  replacements[str(ci)]=r;ass[ci]=r
 a,s=map(F,prev['lower_line']);low,high=F(0),F(100)
 for v in ass:
  da,ds=F(v['a'])-a,F(v['s'])-s
  if ds>0:low=max(low,-da/ds)
  elif ds<0:high=min(high,-da/ds)
  else:assert da>=0
 # Intersection with physically feasible N20 population chamber is checked separately.
 refs=['lab/process/k2074-subdivided-incoming-thermal-bound.json','lab/process/k2078-thermal-certificate-endpoints.json','tests/channel-swings/k2074_subdivided_incoming_thermal_bound.py','tests/channel-swings/k2072_compulsory_ladder_thermal_bound.py','tests/channel-swings/k2070_joint_terminal_thermal_bound.py']
 return dict(id='K2083',endpoint164_necessary_energy='315423877546504164721789670/130753497002473473165359039',endpoint185_boundary_factor='1/8',inputs={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in refs},prefixes188=[list(x) for x in sorted(PREFIXES)],removed_caps188=[[18,2],[19,2],[20,2]],replacements=replacements,quad_arrangements={','.join(map(str,g)):dict(vertices=[[str(x) for x in r] for r in vs],rays=[[str(x) for x in r] for r in rs]) for g,(vs,rs) in q4.items()},lower_line=prev['lower_line'],interval=list(map(str,[low,high])),previous_interval=prev['interval'],scope='conditional quantitative certificate; independent probe and internal analytic review accepted; no external certification')
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();d=json.loads(json.dumps(produce()));dest=ROOT/'lab/process/k2083-thermal-certificate-strengthening.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS candidate interval',d['interval'])
