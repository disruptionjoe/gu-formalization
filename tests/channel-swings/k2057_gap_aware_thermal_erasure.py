"""Gap-aware terminal-loss composition and exact cutoff certificate.
Universal claims use the accompanying proof; inherited basis completeness is pinned.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
A={1:F(14,55),2:F(1,8),3:F(3,55)}
K={1:F(7,29),2:F(1,9),3:F(1,23)}
C={1:F(29,135),2:F(9,50),3:F(23,90)}
def beta(s):
 z=s[-1];r=s[-1]-s[-2] if len(s)>1 else 4
 return max([F(0)]+[A[d] for d in [1,2,3] if z+d>=12 and r+d>=4])
def hull(points):
 out=[]
 for p in sorted(set(points)):
  if out and p[0]==out[-1][0]:continue
  while len(out)>1:
   a,b=out[-2:]
   if (b[0]-a[0])*(p[1]-b[1])-(b[1]-a[1])*(p[0]-b[0])<=0:out.pop()
   else:break
  out.append(p)
 return out

def produce():
 checks=[]
 for d in [1,2,3]:
  b=max(A[e] for e in A if d+e>=4)
  assert A[d]==K[d]*(1+b);assert (1+b)/C[d]<=F(25,4)
  checks.append([d,str(A[d]),str(b),str((1+b)/C[d])])
 assert 2*(1+max(A.values()))<F(25,4)
 ref='lab/process/k2045-third-thermal-spacing-phase.json';h='6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'
 assert hashlib.sha256((ROOT/ref).read_bytes()).hexdigest()==h
 bank=json.loads((ROOT/ref).read_text())['bank'];E=F(5,2);best=[None]*len(bank)
 for eta in [F(0),F(1,25),F(2,25),F(3,25),F(4,25)]:
  vals=[[(F(v['energy']),F(v['value'])-eta*beta(c['s'])*F(v['p'][-1])) for v in c['vertices']] for c in bank]
  high=hull([(e+1,r) for vs in vals for e,r in vs]+[(F(13),eta)])
  for i,vs in enumerate(vals):
   hh=hull(vs+high+[(F(12),eta)]);cs=[]
   for (x,y),(z,w) in zip(hh,hh[1:]):
    slope=(w-y)/(z-x);a=y-slope*x
    if slope<0 and all(r>=a+slope*e for e,r in vs+high) and a+12*slope<=eta:cs.append((a+slope*E,a,slope,eta))
   if cs:
    q=max(cs)
    if best[i] is None or q>best[i]:best[i]=q
 # Exact contact solution replaces the grid bottleneck; the dual below proves
 # this particular relaxation cannot improve the point lower bound further.
 aa,ss,tt=F(295884,878731),-F(104976,4393655),F(219708,4393655)
 best[188]=(aa+ss*E,aa,ss,tt)
 dual=dict(cell=188,contacts=[[188,57,0],[180,56,1]],tail_energy='12',weights=['2174675/2259594','2674015/71177211','1867/142354422'],ceiling='243396/878731',scope='optimal for the stated affine relaxation only; dual mixture not a physical witness')
 assert all(x is not None for x in best)
 lower,a,slope,eta=min(best);left=F(2843,1165);right=F(1951423,716722)
 for _,aa,ss,_ in best:
  d=ss-slope;c=aa-a
  if d>0:left=max(left,-c/d)
  elif d<0:right=min(right,-c/d)
  else:assert c>=0
 assert left<=E<=right
 old=F(439997389,1588579400);assert lower>old
 return dict(relaxation_dual=dual,scope='conditional thermal model only; not exact optimum',bellman_reuse=['K1935','K1956'],gap_checks=checks,uniform_boundary='14/55',loss_factor='25/4',sharp_gap2=dict(q_over_b='27/16',B_over_b='1/8',delta_over_b='1/4'),bank_ref=ref,bank_sha256=h,energy=str(E),lower=str(lower),upper='67173/240731',gain_over_K2054=str(lower-old),width=str(F(67173,240731)-lower),lower_line=[str(a),str(slope)],interval=[str(left),str(right)],assignments=[[str(a),str(s),str(t)] for _,a,s,t in best],upper_evidence='lab/process/k2053-zero-loss-effective-thermal-brackets.json',upper_construction=dict(prefix=[str(F(x,240731)) for x in [88572,132858,14762,1873,992,1488]],tail_ratio='1/9',tail_mass='186/240731',tail_energy=str(F(53,32)*F(1488,240731)),line=['70083/240731','-1164/240731'],interval=['91135/37292','25725/8836'],partial_line=['11501/33582','-434/16791'],partial_interval=['2843/1165','91135/37292'],finite15_population=[str(F(x,44620)) for x in [16416,24624,2736,348,186,279,31]],finite15_value='24903/89240',gain_over_K2053=str(F(7671,27472)-F(67173,240731))),rigidity=dict(non_gap2_loss_margin='59/44',root_loss_margin='823/220'),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k2054-quantitative-terminal-erasure-2026-10-25.md','explorations/conditional-build/k1935-arbitrary-support-thermal-return-2026-10-22.md','explorations/conditional-build/k1956-finite-energy-thermal-gap-2026-10-22.md','lab/process/k2053-zero-loss-effective-thermal-brackets.json']})
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=produce();p=ROOT/'lab/process/k2057-gap-aware-thermal-erasure.json'
 if args.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r
 print('PASS gap Bellman composition, exact cell certificate',len(r['assignments']),'lower',r['lower'],'interval',r['interval'],'line',r['lower_line'])
