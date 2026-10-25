"""Cellwise supporting certificate for the wide-spacing physical regime."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2049-wide-spacing-packing.json'
BANK='lab/process/k2045-third-thermal-spacing-phase.json';HASH='6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'
P={'X':[F(8,23),F(12,23),F(3,23)],'R':[F(4,19),F(6,19),F(9,19)],'Q':[F(1,5),F(3,10),F(9,20),F(1,20)],'B':[F(x,181) for x in [36,54,81,9,1]]}
def hull(pts):
 d={}
 for e,r in pts:
  if e not in d or r<d[e]:d[e]=r
 h=[]
 for e,r in sorted(d.items()):
  while len(h)>1 and (h[-1][0]-h[-2][0])*(r-h[-1][1])-(h[-1][1]-h[-2][1])*(e-h[-1][0])<=0:h.pop()
  h.append((e,r))
 return h

def produce():
 assert hashlib.sha256((ROOT/BANK).read_bytes()).hexdigest()==HASH
 bank=json.loads((ROOT/BANK).read_text())['bank']
 vals=[[(F(v['energy']),F(v['value'])) for v in c['vertices']] for c in bank]
 high=hull([(e+1,r) for vs in vals for e,r in vs]+[(F(13),F(0))])
 hulls=[hull(vs+high+[(F(12),F(0))]) for vs in vals]
 pieces=[]
 for name,lo,hi,alpha,slope in [('XR',F(17,5),F(67,19),F(79,140),-F(13,140)),('RQ',F(67,19),F(37,10),F(21,44),-F(3,44)),('QB',F(37,10),F(675,181),F(81,212),-F(9,212))]:
  assignments=[]
  for vs,h in zip(vals,hulls):
   good=[]
   for (x,y),(z,w) in zip(h,h[1:]):
    s=(w-y)/(z-x);a=y-s*x
    if s<0 and all(a+s*e>=alpha+slope*e for e in [lo,hi]):good.append((a,s))
   assert good,'no common whole-segment support'
   a,s=good[0];assert all(r>=a+s*e for e,r in vs);assert all(r>=a+s*e for e,r in high);assert a+s*12<=0
   assignments.append([str(a),str(s)])
  eq=set()
  for vs,c in zip(vals,bank):
   if all(r>=alpha+slope*e for e,r in vs):
    for v in c['vertices']:
     if F(v['value'])==alpha+slope*F(v['energy']):eq.add(tuple((x,str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)))
  assert min(r-alpha-slope*e for e,r in high)>0
  pieces.append(dict(name=name,interval=list(map(str,[lo,hi])),line=list(map(str,[alpha,slope])),assignments=assignments,low_equality_vertices=[list(map(list,v)) for v in sorted(eq)]))
 return dict(result_id='K2049',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',bank_ref=BANK,bank_sha256=HASH,spacing='1/2 < delta <= 1',energy_interval=['17/5','675/181'],pieces=pieces,populations={k:list(map(str,v)) for k,v in P.items()},jump_at_energy_7_over_2={'half_spacing':'21/88','above_half':'67/280','jump':'1/1540','physical_levels_at_half':14,'physical_levels_above_half':7},scope='Unrestricted finite/countable exact-shell thermal model on the declared rectangle. Lower energies and spacing above1 remain open.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [BANK,'explorations/conditional-build/k2043-chamber-offset-frontier-2026-10-25.md','explorations/conditional-build/k2047-fifth-thermal-spacing-phase-2026-10-25.md']})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2049 three whole-energy interval certificates; high offset1; exact jump')
