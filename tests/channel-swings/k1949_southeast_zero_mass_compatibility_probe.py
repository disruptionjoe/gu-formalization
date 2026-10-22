"""Independent raw-return reconstruction and polynomial-identity certificate replay."""
import json,hashlib
from copy import deepcopy
from pathlib import Path
from sage.all import QQ,GF,matrix,vector,identity_matrix,block_matrix,PolynomialRing
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'lab/process/k1949-southeast-zero-mass-compatibility.json'
def m(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def audit(v,math_only=False):
 count=0
 def ck(x,msg):
  nonlocal count
  assert x,msg
  count+=1
 if not math_only:
  ck(v['result_id']=='K1949','identity')
  for p,h in v['inputs'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin')
 r=json.loads((ROOT/'lab/process/k1945-energy-compatible-raw-columns.json').read_text());mass=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());obs=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());d=[m(x)/24 for x in obs['target_D']]
 # Independent bit-index Clifford construction.
 gs=[]
 for family in range(2):
  for pos in range(7):
   entries={}
   for col in range(128):
    bit=1<<(6-pos);sign=(-1)**(col>>(7-pos)).bit_count()
    if family:sign*=1 if col&bit else -1
    entries[(col^bit,col)]=sign
   gs.append(matrix(QQ,128,128,entries))
 I=identity_matrix(QQ,128);vol=I
 for g in gs:vol*=g
 tr=gs[0]*(11*(I+vol)/48+11*(I-vol)/24);ck(tr==m(r['Traw']) and tr.change_ring(GF(1009)).rank()==128,'actual nonzero SE derivative coefficient')
 Fg=m(r['basis']);Rg=-Fg[:128,:]+tr*Fg[512:,:]
 for rec in v['blocks']:
  typ=rec['type'];old=next(x for x in r['blocks'] if x['type']==typ);ix=r['blocks'].index(old);F=m(old['basis']);H=m(old['H']);ts=list(map(m,old['T']));A=list(map(m,en['blocks'][typ]['matrices']));V=m(rec['auxiliary_inclusion']);K=m(rec['invisible_carrier']);R=m(rec['raw_return']);outrows=[x for x in old['coordinates'] if x<128]
  ck(R==Rg.matrix_from_rows(outrows)[:,16*ix:16*(ix+1)],'raw return with actual output permutation')
  ck(F*V==matrix(QQ,20,4,{(i+16,i):1 for i in range(4)}),'pure raw auxiliary injection')
  for j in range(3):ck((F[16:20,:]*A[j]).change_ring(GF(1013)).rank()==4,'principal surgery actual auxiliary rank4')
  ck(K.rank()==4 and all(t*K==0 for t in ts) and block_matrix([[t] for t in ts]).change_ring(GF(1009)).rank()==12,'complete invisible carrier')
  ck((R*K).det()!=0 and (K.transpose()*H*V).det()!=0,'global uniqueness factors')
  for a,repair in enumerate(rec['repairs']):
   C=m(repair['C']);Z=m(repair['Z']);prev=mass['blocks'][typ]['repairs'][a];B,S=m(prev['B']),m(prev['S'])
   ck(C==m(prev['C'])+K*Z*K.transpose()*H,'actual invisible correction')
   ck(Z+Z.transpose()==0 and H*C+C.transpose()*H==0,'fixed energy')
   ck(R*C*V==0,'raw zero SE')
   ck(all(ts[i]*C-B*ts[i]+S*A[i]-d[i]*S==0 for i in range(3)),'first order')
   ck(ts[0]*C==d[0]*S and S*C==B*S,'full arbitrary profile equation')
   for factor in repair['factors']:
    Q=F.matrix_from_rows([i for i,g in enumerate(old['coordinates']) if factor['mask']&(1<<(g//128))]);ck(m(factor['factor'])*Q==C,'actual raw input factor')
  C1,C2=[m(x['C']) for x in rec['repairs']];S1,S2=[m(x['S']) for x in mass['blocks'][typ]['repairs']];Bs=[m(x['B']) for x in mass['blocks'][typ]['repairs']]
  ck(S1*C2+S2*C1==Bs[0]*S2+Bs[1]*S1,'cross-profile equation')
  # Rebuild the entire two-slot first-order and SE system without the upstream kernel.
  Q=F.matrix_from_rows([i for i,g in enumerate(old['coordinates']) if g//128 in [0,4]]);N=H.inverse()*Q.transpose();cb=[]
  for i in range(8):
   for j in range(i+1,8):
    z=matrix(QQ,8,8);z[i,j]=1;z[j,i]=-1;cb.append(N*z*Q)
  cols=[sum([(t*c).list() for t in ts],[])+(R*c*V).list() for c in cb]
  for i in range(4):
   for j in range(16):
    S=matrix(QQ,4,16);S[i,j]=1;cols.append(sum([(S*A[h]-d[h]*S).list() for h in range(3)],[])+[0]*16)
  cols += [sum([(-B*t).list() for t in ts],[])+[0]*16 for B in Bs]
  equations=matrix(QQ,cols).transpose();ker=m(rec['two_slot_zero_SE']['kernel']);ck(equations*ker.transpose()==0 and ker.change_ring(GF(1013)).rank()==5,'five exact independent kernel directions')
  ck(equations.change_ring(GF(1009)).rank()==89,'complete five-dimensional kernel')
  PR=PolynomialRing(QQ,5,'x');x=PR.gens();params=vector(PR,x)*ker;C=sum((params[i]*cb[i] for i in range(28)),matrix(PR,16,16));S=matrix(PR,4,16,params[28:92]);B=params[92]*Bs[0]+params[93]*Bs[1];res=(S*C-B*S).list();cert=rec['two_slot_zero_SE']
  def dec(data):return sum(QQ(a)*PR.monomial(*e) for e,a in data)
  lhs=sum(dec(h)*res[j] for h,j in zip(cert['multipliers'],cert['residual_indices']));rhs=(params[92]**2+params[93]**2)**2
  ck(lhs==rhs==dec(cert['mass_fourth_power']) and rhs!=0,'actual quartic residual identity')
 times=[];aux=[]
 for ix,old in enumerate(r['blocks']):
  rec=v['blocks'][old['type']];rep=next(b for b in r['blocks'] if b['type']==old['type']);ids=[x for x in old['coordinates'] if x<128]
  ck(m(old['basis'])==m(rep['basis']) and old['H']==rep['H'] and old['T']==rep['T'] and Rg.matrix_from_rows(ids)[:,16*ix:16*(ix+1)]==m(rec['raw_return']),'all32 actual copy equations')
  times+=ids;aux += [x-512 for x in old['coordinates'] if x>=512]
 ck(sorted(times)==list(range(128))==sorted(aux),'full128 global input output permutations')
 return count

def main():
 v=json.loads(P.read_text());print('PASS K1949 independent baseline',audit(v),'exact controls');faults=[]
 for fault in ['repair','raw','multiplier','kernel']:
  w=deepcopy(v);r=w['blocks'][0]
  if fault=='repair':r['repairs'][0]['C']['entries'][0][2]=str(QQ(r['repairs'][0]['C']['entries'][0][2])+1)
  if fault=='raw':r['raw_return']['entries'][0][2]=str(QQ(r['raw_return']['entries'][0][2])+1)
  if fault=='multiplier':
   term=next(h for h in r['two_slot_zero_SE']['multipliers'] if h)[0];term[1]=str(QQ(term[1])+1)
  if fault=='kernel':r['two_slot_zero_SE']['kernel']['entries'][0][2]=str(QQ(r['two_slot_zero_SE']['kernel']['entries'][0][2])+1)
  try:audit(w,True)
  except AssertionError as ex:faults.append(str(ex))
  else:raise AssertionError('undetected math fault '+fault)
 reporting=[]
 for fault in ['identity','pin']:
  w=deepcopy(v)
  if fault=='identity':w['result_id']='K0'
  else:w['inputs'][next(iter(w['inputs']))]='0'*64
  try:audit(w)
  except AssertionError as ex:reporting.append(str(ex))
  else:raise AssertionError('undetected reporting fault')
 print('PASS mathematical faults',faults,'; report/pin faults',reporting)
if __name__=='__main__':main()
