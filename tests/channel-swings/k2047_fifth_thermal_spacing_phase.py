"""Exact fifth/sixth spacing certificates over a pinned complete arrangement."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2047-fifth-thermal-spacing-phase.json'
BANK='lab/process/k2045-third-thermal-spacing-phase.json'
BANK_HASH='6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'
A=(F(1575,653),F(729,2612));B=(F(675,181),F(81,362));T=(F(28361,11755),F(6561,23510));Q=(F(37,10),F(9,40));C=(F(19,8),F(9,32));U=(F(3043,815),F(729,3260));R=(F(67,19),F(9,38))
LO=F(2,5);MID=F(5652,11755);HI=F(1,2)
def ends(side,d):
 return {'AT':(A,T),'TB':(T,(B[0]+d,B[1])),'TU':(T,(U[0]+d,U[1])),'CQ':((C[0]+d,C[1]),Q),'QB':(Q,B)}[side]
def residual(side,d,e,r):
 (x,y),(z,w)=ends(side,d);assert z>x
 return (z-x)*(r-y)-(w-y)*(e-x)
def line(side,d,e):
 (x,y),(z,w)=ends(side,d);return y+(w-y)*(e-x)/(z-x)
def frontier(d,e,left):return min(max(line('AT',d,e),line(left,d,e)),max(line('CQ',d,e),line('QB',d,e)))
def produce():
 assert hashlib.sha256((ROOT/BANK).read_bytes()).hexdigest()==BANK_HASH
 bank=json.loads((ROOT/BANK).read_text())['bank'];phases=[]
 for lo,hi,left in [(LO,MID,'TB'),(MID,HI,'TU')]:
  labels={}
  for pair in [('AT','CQ'),('AT','QB'),(left,'CQ'),(left,'QB')]:
   assigned=[]
   for c in bank:
    good=[s for s in pair if all(residual(s,d,F(v['energy']),F(v['value']))>=0 for v in c['vertices'] for d in [lo,hi])]
    assert good,'low cell';assigned.append(good)
   labels['+'.join(pair)]=assigned
  for s in ['AT',left,'CQ','QB']:
   for d in [lo,hi]:
    assert all(residual(s,d,F(v['energy'])+d,F(v['value']))>=0 for c in bank for v in c['vertices']),'high support'
    assert residual(s,d,F(12),F(0))>0,'tail'
  # Feasible crossing between shifted C and Q, to right of T.
  for d in [lo,hi]:
   assert line(left,d,C[0]+d)<C[1] and line(left,d,Q[0])>Q[1]
   assert line('CQ',d,A[0])>A[1] and line('QB',d,A[0])>A[1]
   assert line(left,d,B[0])>B[1]
   assert line('CQ',d,T[0])>T[1]
   assert line('QB',d,T[0])>T[1]
  phases.append(dict(interval=list(map(str,[lo,hi])),left=left,assignments=labels))
 equality={}
 for s in ['AT','TB','TU','CQ','QB']:
  ds=[LO+(MID-LO)/3,LO+2*(MID-LO)/3] if s=='TB' else [MID+(HI-MID)/3,MID+2*(HI-MID)/3]
  for shift in [0,1]:
   zeros={tuple((x,str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)) for c in bank for v in c['vertices'] if all(residual(s,d,F(v['energy'])+shift*d,F(v['value']))==0 for d in ds)}
   equality[s+('_high' if shift else '_low')]=[[list(q) for q in z] for z in sorted(zeros)]
 half={}
 for shift in [0,1]:
  zeros={tuple((x,str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)) for c in bank for v in c['vertices'] if residual('CQ',HI,F(v['energy'])+shift*HI,F(v['value']))==0}
  half['high' if shift else 'low']=[[list(q) for q in z] for z in sorted(zeros)]
 assert residual('TB',MID,U[0]+MID,U[1])==0
 assert residual('CQ',HI,*R)==0
 d=MID+F(1,10**6);e=F(3);mass=(e-T[0])/(U[0]+d-T[0]);value=T[1]+mass*(U[1]-T[1]);old=frontier(d,e,'TB');assert value<old and 0<mass<1
 return dict(result_id='K2047',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',bank_ref=BANK,bank_sha256=BANK_HASH,bank_reuse='K2045 complete cofactor and independent elimination census; not rerun',phases=phases,energy_interval=[str(A[0]),str(B[0])],endpoints={n:list(map(str,v)) for n,v in [('A',A),('B',B),('T',T),('Q',Q),('C',C),('U',U),('R',R)]},strict_equalities=equality,half_CQ_equalities=half,boundary_rival=dict(delta=str(d),energy=str(e),shifted_U_mass=str(mass),value=str(value),previous=str(old)),formula='min(max(f_AT,f_left),max(f_CQ,f_QB)); left TB then TU',scope='Exact finite/countable thermal model for2/5<=delta<=1/2; no continuation above1/2 asserted',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [BANK,'tests/channel-swings/k2045_third_thermal_spacing_phase_probe.py','explorations/conditional-build/k2045-third-thermal-spacing-phase-2026-10-25.md','explorations/conditional-build/k2043-chamber-offset-frontier-2026-10-25.md']})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2047 fifth/sixth whole-interval supports, strict and half-spacing equality, actual rival')
