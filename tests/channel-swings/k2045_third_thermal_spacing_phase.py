"""Exact third-phase support certificate; no spacing-grid inference."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
from itertools import product,combinations
from k2015_finite_thermal_ray_separation import supports,matrices,vertex,rate
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2045-third-thermal-spacing-phase.json'
A=(F(1575,653),F(729,2612));B=(F(675,181),F(81,362));D=(F(349,145),F(81,290));Q=(F(37,10),F(9,40));LO=F(2,145);HI=F(628,1629);END=F(2,5);T=(F(28361,11755),F(6561,23510))
def ends(side,d):
 if side=='AT':return A,T
 if side=='TB':return T,(B[0]+d,B[1])
 if side=='A':return A,(B[0]+d,B[1])
 if side=='DQ':return (D[0]+d,D[1]),Q
 return Q,B
def res(side,d,e,r):
 (x,y),(z,w)=ends(side,d);assert z>x
 return (z-x)*(r-y)-(w-y)*(e-x)
def line(side,d,e):
 (x,y),(z,w)=ends(side,d);return y+(w-y)*(e-x)/(z-x)
def generate_bank():
 cells=[];bases=0
 for ss in supports(11):
  for o in product((-1,1),repeat=len(ss)-1):
   ed,df,planes=matrices(ss,o);vs=set()
   for bs in combinations(planes,len(ss)-1):
    bases+=1;p=vertex(bs,len(ss))
    if p is not None and all(sum(a*b for a,b in zip(row,p))>=0 for row in ed):vs.add(p)
   assert vs
   cells.append(dict(s=list(ss),o=list(o),vertices=[dict(p=list(map(str,p)),energy=str(sum(x*y for x,y in zip(ss,p))),value=str(rate(ss,p))) for p in sorted(vs)]))
 return cells,bases

def certify(bank,lo,hi,pairs):
 labels={}
 for sides in pairs:
  out=[]
  for c in bank:
   good=[side for side in sides if all(res(side,d,F(v['energy']),F(v['value']))>=0 for d in [lo,hi] for v in c['vertices'])]
   assert good,'low-cell coverage';out.append(good)
  labels['+'.join(sides)]=out
 all_sides=sorted({s for p in pairs for s in p})
 for d in [lo,hi]:
  for side in all_sides:
   assert all(res(side,d,F(v['energy'])+d,F(v['value']))>=0 for c in bank for v in c['vertices']),'high support'
   assert res(side,d,F(12),F(0))>0,'strict tail support'
 return dict(interval=list(map(str,[lo,hi])),assignments=labels)

def produce():
 bank,bases=generate_bank();oldpath='lab/process/k2037-thermal-seven-level-boundary.json';old=json.loads((ROOT/oldpath).read_text())['banks']['9']
 assert [c for c in bank if max(c['s'])<=9]==old,'unchanged cutoff-nine replay'
 phases=[certify(bank,LO,HI,[('A','DQ'),('A','QB')]),certify(bank,HI,END,[('AT','DQ'),('AT','QB'),('TB','DQ'),('TB','QB')])]
 # All feasibility/ordering residues are affine after denominator clearing.
 for lo,hi,left in [(LO,HI,'A'),(HI,END,'TB')]:
  for d in [lo,hi]:
   assert line(left,d,D[0]+d)<=D[1]
   assert line(left,d,Q[0])>Q[1]
   assert line('DQ',d,B[0])<=B[1]
   assert line('QB',d,A[0])>A[1]
 for d in [HI,END]:assert line('AT',d,A[0])==A[1] and line('AT',d,T[0])==T[1]
 assert line('A',HI,T[0])==T[1]
 equality={}
 for side in ['A','AT','TB','DQ','QB']:
  for shift in [0,1]:
   ds=[F(1,10),F(1,3)] if side=='A' else ([HI,END] if side in ['AT','TB'] else [F(1,10),F(1,3)])
   points={tuple((int(x),str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)) for c in bank for v in c['vertices'] if all(res(side,d,F(v['energy'])+shift*d,F(v['value']))==0 for d in ds)}
   equality[side+('_high' if shift else '_low')]=[[list(x) for x in p] for p in sorted(points)]
 # Actual competing channels, not a failed relaxation coefficient.
 d=HI+F(1,10**6);old=min(line('A',d,T[0]),max(line('DQ',d,T[0]),line('QB',d,T[0])));assert T[1]<old
 C=(F(19,8),F(9,32));assert (D[1]-Q[1])*(Q[0]-C[0]-END)==(C[1]-Q[1])*(Q[0]-D[0]-END) and C[1]>D[1]
 assert line('DQ',HI,T[0])>T[1] and line('QB',HI,T[0])>T[1] and A[1]>T[1]
 d2=END+F(1,10**6);e=F(7,2);m=(Q[0]-e)/(Q[0]-C[0]-d2);val=Q[1]+m*(C[1]-Q[1]);old2=min(max(line('AT',d2,e),line('TB',d2,e)),max(line('DQ',d2,e),line('QB',d2,e)));assert 0<m<1 and val<old2
 inputs=[oldpath,'explorations/conditional-build/k2043-chamber-offset-frontier-2026-10-25.md','tests/channel-swings/k2015_finite_thermal_ray_separation.py']
 return dict(result_id='K2045',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',phases=phases,energy_interval=[str(A[0]),str(B[0])],formula={'phase3':'min(f_A,max(f_DQ,f_QB))','phase4':'min(max(f_AT,f_TB),max(f_DQ,f_QB))'},endpoints={n:list(map(str,v)) for n,v in [('A',A),('B',B),('D',D),('Q',Q),('T',T),('C',C)]},bank=bank,basis_count=bases,records=sum(len(c['vertices']) for c in bank),strict_equalities=equality,resources='Strict spacing/energy interiors: phase3 left22, middle18, Q9, aboveQ11; phase4 A-toT13, T-to-switch24, switch-toQ18, Q9, aboveQ11; endpoints A,B11. At the left/right switch minimum18. Critical spacing equality not fully classified.',boundary_rivals=[dict(delta=str(d),energy=str(T[0]),value=str(T[1]),previous=str(old),kind='unshifted T'),dict(delta=str(d2),energy=str(e),value=str(val),previous=str(old2),shifted_C_mass=str(m),kind='low Q high C')],upper_endpoint_kind='sharp fourth-phase boundary, physical shifted-C rival immediately beyond2/5',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2045',r['records'],'vertices, third/fourth whole-interval certificates, physical transition rivals')
