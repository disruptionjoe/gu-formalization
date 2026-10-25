"""Exact terminal-response coefficients; universal claims use accompanying proof."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def coefficients(t,d):
 Z=sum(t**j for j in range(4));L=sum(t**j for j in range(4-d))/Z;H=t**d*L
 return L,H,H/(1+L),(1+H-L)*(1+L)/(2*(1+H+L))
def response(p,u,c0,L,H):
 pos=lambda x:max(F(0),x)
 return (pos(p-c0-pos(L*u-H*p))+pos(u-pos(H*p-L*u))-pos(p-c0))/2

def boundary_certificate():
 from k2049_wide_spacing_packing import hull
 bank_ref='lab/process/k2045-third-thermal-spacing-phase.json';bank_hash='6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'
 assert hashlib.sha256((ROOT/bank_ref).read_bytes()).hexdigest()==bank_hash
 bank=json.loads((ROOT/bank_ref).read_text())['bank'];E=F(5,2);best=[None]*len(bank)
 for theta in [F(0),F(1,100),F(1,50),F(1,25),F(2,25),F(3,25),F(9,50)]:
  vals=[[(F(v['energy']),F(v['value'])-theta*F(7,29)*F(v['p'][-1])*(c['s'][-1]>=9)) for v in c['vertices']] for c in bank]
  tau=theta*F(22,29);high=hull([(e+1,r) for vs in vals for e,r in vs]+[(F(13),tau)])
  for i,vs in enumerate(vals):
   h=hull(vs+high+[(F(12),tau)]);candidates=[]
   for (x,y),(z,w) in zip(h,h[1:]):
    slope=(w-y)/(z-x);a=y-slope*x
    if slope<0 and all(r>=a+slope*e for e,r in vs+high) and a+12*slope<=tau:candidates.append((a+slope*E,a,slope,theta))
   if candidates:
    value=max(candidates)
    if best[i] is None or value>best[i]:best[i]=value
 lower,a,slope,theta=min(best);left=F(2843,1165);right=F(789,275)
 for _,aa,ss,_ in best:
  d=ss-slope;c=aa-a
  if d>0:left=max(left,-c/d)
  elif d<0:right=min(right,-c/d)
  else:assert c>=0
 assert lower==F(439997389,1588579400)
 return dict(bank_ref=bank_ref,bank_sha256=bank_hash,energy=str(E),lower=str(lower),upper='7671/27472',gain_over_K2053=str(lower-F(124659,450796)),width=str(F(7671,27472)-lower),assignments=[[str(a),str(s),str(t)] for _,a,s,t in best],lower_line=[str(a),str(slope)],interval=[str(left),str(right)],upper_evidence='lab/process/k2053-zero-loss-effective-thermal-brackets.json')

def produce():
 rows=[];checks=0
 for t in [F(1,4),F(1,2),F(3,4),F(9,10)]:
  for d in [1,2,3]:
   L,H,k,c=coefficients(t,d)
   for p in [F(0),F(1,7),F(1),F(3)]:
    knots=sorted({F(0),k*p,H*p/L,(1+H)*p/L,2*(1+H)*p/L})
    for u in knots+[(x+y)/2 for x,y in zip(knots,knots[1:])]:
     for c0 in [F(0),p/3,p,2*p]:
      delta=response(p,u,c0,L,H);assert delta>=c*max(F(0),u-k*p)
      assert (delta==0)==(u<=k*p);checks+=1
   p=F(1);u=(1+H)*p/L
   assert response(p,u,F(0),L,H)==c*(u-k*p)
   rows.append(dict(t=str(t),gap=d,L=str(L),H=str(H),threshold=str(k),sharp_excess_coefficient=str(c),sharp_u_over_p=str((1+H)/L)))
 paths=['explorations/conditional-build/k2020-posttransition-tail-and-resources-2026-10-24.md','explorations/conditional-build/k2053-zero-loss-effective-thermal-brackets-2026-10-25.md']
 return dict(result_id='K2054',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',rows=rows,terminal_controls=checks,boundary_certificate=boundary_certificate(),half_temperature=dict(k_max='7/29',c_min='9/50',boundary_factor='7/22',loss_factor='725/99',gap2_boundary_factor='1/8',gap2_loss_factor='25/4'),scope='Sharp terminal coefficient, finite/countable erasure and improved low-energy bracket; not exact optimum or sharp general-path constants.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce();out=ROOT/'lab/process/k2054-quantitative-terminal-erasure.json'
 if a.write:out.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(out.read_text())
 print('PASS K2054 terminal controls',r['terminal_controls'],'sharp coefficients',len(r['rows']))
