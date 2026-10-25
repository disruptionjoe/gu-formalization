"""Independent bath-label return and actual tail erasure, without producer import."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
def raw_return(s,p,t):
 w=[t**j/sum(t**k for k in range(4)) for j in range(4)]
 return sum(max(F(0),q-sum(max((r*w[int(x+b-y)] for y,r in zip(s,p) if x+b-y in range(4)),default=F(0)) for b in range(4))/2) for x,q in zip(s,p))
def check_boundary(r,full):
 c=r['boundary_certificate'];bank=json.loads((ROOT/c['bank_ref']).read_text())['bank'];assert hashlib.sha256((ROOT/c['bank_ref']).read_bytes()).hexdigest()==c['bank_sha256'],'bank hash'
 assert len(c['assignments'])==len(bank),'cell coverage';unique=set();E=F(c['energy']);lower=F(c['lower']);al,sl=map(F,c['lower_line']);left,right=map(F,c['interval']);vals=[];records=0
 for cell,line in zip(bank,c['assignments']):
  a,s,t=map(F,line);assert 0<=t<=F(9,50) and s<0,'boundary theta range'
  vv=[]
  for v in cell['vertices']:
   e,ret=F(v['energy']),F(v['value']);b=F(v['p'][-1]) if cell['s'][-1]>=9 else F(0)
   if full:assert raw_return(cell['s'],list(map(F,v['p'])),F(1,2))==ret,'actual bath bank'
   assert ret-t*F(7,29)*b>=a+s*e,'boundary low cell';vv.append((e,ret,b));records+=1
  vals.extend(vv);assert a+s*E>=lower,'new point lower';assert all(a+s*x>=al+sl*x for x in [left,right]),'whole interval order'
  assert all(a+n*s<=t*F(22,29) for n in [12,13]),'boundary tail contacts';unique.add((a,s,t))
 for a,s,t in unique:
  assert all(ret-t*F(7,29)*b>=a+s*(e+1) for e,ret,b in vals),'all high cells'
 assert al+sl*E==lower and lower>F(124659,450796),'strict improvement'
 assert F(c['gain_over_K2053'])==lower-F(124659,450796),'improvement arithmetic'
 upper=json.loads((ROOT/c['upper_evidence']).read_text());assert upper['upper']==c['upper'],'retained upper witness'
 assert F(c['width'])==F(c['upper'])-lower>0,'remaining gap'
 assert F(upper['interval_bracket']['endpoints'][0]['energy'])<=left<=right<=F(upper['interval_bracket']['endpoints'][1]['energy']),'upper family domain'
 print('Boundary certificate',records,'vertex records,',len(unique),'lines; improved lower',lower,flush=True)

def replay(r,full=True):
 count=0
 for row in r['rows']:
  t=F(row['t']);d=row['gap'];w=[t**j/sum(t**k for k in range(4)) for j in range(4)]
  L=sum(w[:4-d]);H=sum(w[d:]);k=F(row['threshold']);c=F(row['sharp_excess_coefficient'])
  assert F(row['L'])==L and F(row['H'])==H,'bath edge coefficients'
  assert k==H/(1+L),'flat threshold'
  p=F(1);u=F(row['sharp_u_over_p']);root=max(1,3-d)
  delta=raw_return([root,root+d],[p,u],t)-raw_return([root],[p],t)
  assert delta==c*(u-k*p),'sharp physical response'
  assert raw_return([root,root+d],[p,k*p],t)==raw_return([root],[p],t),'flat physical equality'
 h=r['half_temperature'];K=F(h['k_max']);c=F(h['c_min'])
 assert K==F(7,29) and c==F(9,50),'uniform constants'
 assert F(h['boundary_factor'])==K/(1-K),'boundary rearrangement'
 assert F(h['loss_factor'])==1/(c*(1-K)),'loss rearrangement'
 assert F(h['gap2_boundary_factor'])==F(1,8) and F(h['gap2_loss_factor'])==F(25,4),'gap2 rearrangement'
 if full:
  for gaps in product([1,2,3],repeat=3):
   if any(x+y<4 for x,y in zip(gaps,gaps[1:])):continue
   root=max(1,3-gaps[0]);ss=[root]
   for d in gaps:ss.append(ss[-1]+d)
   for numer in [(8,12,3,1),(9,1,1,1),(1,2,4,8),(81,9,1,1),(3,0,5,0),(1,1,1,1)]:
    p=[F(x,sum(numer)) for x in numer];base=raw_return(ss,p,F(1,2))
    for cut in [1,2,3]:
     retained=raw_return(ss[:cut],p[:cut],F(1,2));loss=base-retained;q=sum(p[cut:]);b=p[cut-1]
     excess=F(0)
     for i in range(cut,4):
      d=gaps[i-1];w=[F(8,15),F(4,15),F(2,15),F(1,15)];Li=sum(w[:4-d]);Hi=sum(w[d:]);excess+=max(F(0),p[i]-Hi/(1+Li)*p[i-1])
     assert loss>=c*excess,'physical attached excess'
     assert q<=F(h['boundary_factor'])*b+F(h['loss_factor'])*loss,'physical tail bound'
     assert (loss==0)==(excess==0),'zero-loss characterization';count+=1
  # Pure gap2 geometric tails saturate exact erasure and approach b/8.
  for n in range(2,13):
   p=[F(1,9)**i for i in range(n)];ss=list(range(1,2*n,2));b=p[0]
   assert raw_return(ss,p,F(1,2))==b/2,'geometric zero loss'
   assert sum(p[1:])==b*(1-F(1,9)**(n-1))/8,'geometric tail sum';count+=1
  # An isolated removed component cannot be hidden at zero cost.
  assert raw_return([1,10],[F(3,4),F(1,4)],F(1,2))-raw_return([1],[F(3,4)],F(1,2))==F(1,8),'isolated component'
 return count
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2054-quantitative-terminal-erasure.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE physical tail controls',replay(r),flush=True);check_boundary(r,True);caught=[]
 for name in ['threshold','sharp','boundary','loss','gap2']:
  b=copy.deepcopy(r)
  if name=='threshold':b['rows'][0]['threshold']='0'
  elif name=='sharp':b['rows'][0]['sharp_excess_coefficient']='1/2'
  elif name=='boundary':b['half_temperature']['boundary_factor']='1/4'
  elif name=='loss':b['half_temperature']['loss_factor']='1'
  else:b['half_temperature']['gap2_loss_factor']='5'
  try:replay(b,False)
  except AssertionError as e:assert str(e);caught.append([name,str(e)])
  else:raise AssertionError('missed coefficient fault '+name)
 print('PASS coefficient faults',caught)
 c=r['boundary_certificate'];a,s,t=map(F,c['assignments'][0]);assert a+12*s<=t*F(22,29)
 try:
  assert a+100+12*s<=t*F(22,29),'boundary tail support'
 except AssertionError as e:assert str(e);print('PASS boundary intercept fault',str(e))
 else:raise AssertionError('missed boundary support fault')
