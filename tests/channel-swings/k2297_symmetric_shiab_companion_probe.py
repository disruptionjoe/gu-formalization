from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib,sys
import sympy as s
from k77_exact_bank_api import K77Core,load_bank
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):checks[n]=bool(v)
bank=load_bank();c=K77Core(bank.signature,bank.channels);eta=c.eta
slots=[(a,b) for a in range(4) for b in range(a,4)]
def metric(slot,i,j):return int((i,j)==slot or (j,i)==slot)
def inj(slot):return {1<<i:{1<<j:(Q(eta[j]*metric(slot,i,j)),Q(0)) for j in range(4) if metric(slot,i,j)} for i in range(4) if any(metric(slot,i,j) for j in range(4))}
js=[inj(z) for z in slots]
Gram=s.Matrix([[c.pair(u,c.hodge(v))[0] for v in js] for u in js]);expected=s.diag(*[(1 if a==b else 2)*eta[a]*eta[b] for a,b in slots]);check('symmetric_trace_Hodge_Gram',Gram==expected)
# Ten covectors span all quadratic monomials; all ten metric columns independently.
ks=[[int(i==t) for i in range(14)] for t in range(4)]
ks += [[int(i in (a,b)) for i in range(14)] for a,b in combinations(range(4),2)]
full_pair=True;full_image=True;gauge=True;Afixture=None;Gfixture=None
for k in ks:
 for slot in slots:
  def tens(i,j,a,b):return -Q(1,2)*(k[i]*k[a]*metric(slot,j,b)-k[i]*k[b]*metric(slot,j,a)-k[j]*k[a]*metric(slot,i,b)+k[j]*k[b]*metric(slot,i,a))
  f={}
  for i,j in combinations(range(14),2):
   coeff={}
   for a,b in combinations(range(14),2):
    z=eta[a]*eta[b]*tens(i,j,a,b)
    if z:coeff=c.eadd(coeff,c.escale(z,c.blade((a,b))))
   if coeff:f[(1<<i)|(1<<j)]=coeff
  A=c.shiab(f);ric=[[sum(eta[a]*tens(a,i,a,j) for a in range(14)) for j in range(14)] for i in range(14)];scal=sum(eta[i]*ric[i][i] for i in range(14));G=[[ric[i][j]-Q(1,2)*eta[i]*scal*int(i==j) for j in range(14)] for i in range(14)]
  jg={1<<i:{1<<j:(eta[j]*G[i][j],Q(0)) for j in range(14) if G[i][j]} for i in range(14) if any(G[i])}
  full_image &= A==c.fscale(-2,c.hodge(jg))
  for us,u in zip(slots,js):full_pair &= c.pair(u,A)==(-2*sum(eta[i]*eta[j]*metric(us,i,j)*G[i][j] for i in range(4) for j in range(4)),Q(0))
  if any(A.values()):Afixture=A;Gfixture=c.fscale(-2,c.hodge(jg))
check('all100_full_curvature_columns',full_image);check('all1000_dual_pairing_coefficients',full_pair)
receivers=[(i,a,b) for i in range(14) for a,b in combinations(range(14),2)];vs=[{1<<i:c.blade((a,b))} for i,a,b in receivers];mats=[];raws=[];rev=[]
for t in range(4):
 k={1<<t:{0:(Q(1),Q(0))}};im=[c.shiab(c.wedge_raw(k,u)) for u in js];rows=[];forward=[];back=[]
 for v in vs:
  ri=c.shiab(c.wedge_raw(k,v));rr=[];rf=[];rb=[]
  for u,ai in zip(js,im):
   f,b=c.pair(v,ai),c.pair(u,ri);assert f[1]==b[1]==0
   rr.append((f[0]-b[0])/2);rf.append(f[0]);rb.append(b[0])
  rows.append(rr);forward.append(rf);back.append(rb)
 mat=s.Matrix(rows);mats.append(mat);raws.append(s.Matrix(forward));rev.append(s.Matrix(back));kernel=s.zeros(10,1);kernel[slots.index((t,t))]=1
 check('axis_'+str(t)+'_rank_and_kernel',mat.rank()==9 and mat*kernel==s.zeros(1274,1))
 check('axis_'+str(t)+'_full_receiver_support',sum(any(row) for row in rows)==58)
check('four_axis_common_kernel',s.Matrix.vstack(*mats).rank()==10)
for name,k in [('null',[1,0,0,1]),('generic',[2,1,3,0])]:
 mat=s.zeros(1274,10)
 for t in range(4):mat+=k[t]*mats[t]
 kk=s.Matrix([k[a]*k[b] for a,b in slots]);check(name+'_rank9_kernel_kk',mat.rank()==9 and mat*kk==s.zeros(1274,1))
Eall=s.Matrix.hstack(*mats);live=[i for i in range(1274) if any(Eall.row(i))];Et=Eall[live,:]
B=[]
for a,b in combinations(range(4),2):
 for cc in range(4):
  row=[0]*40;row[10*a+slots.index(tuple(sorted((b,cc))))]+=1;row[10*b+slots.index(tuple(sorted((a,cc))))]-=1;B.append(row)
B=s.Matrix(B);er=Et.rref()[0];br=B.rref()[0]
check('complete_firstjet_rowspace',Et.rank()==20 and B.rank()==20 and Et.col_join(B).rank()==20)
check('union_receiver_rows',len(live)==64)
# Independent Sym3 kernel basis: all20 unordered triples.
triples=list(__import__('itertools').combinations_with_replacement(range(4),3));T=s.Matrix([[int(tuple(sorted((t,a,b)))==tr) for tr in triples] for t in range(4) for a,b in slots]);check('symmetric_thirdjet_exact_kernel',T.rank()==20 and Et*T==s.zeros(len(live),20))
i=receivers.index((1,0,1));diag=s.zeros(10,1);diag[slots.index((1,1))]=1;diag[slots.index((2,2))]=-1
check('explicit_TT_leakage', (raws[0]*diag)[i]==-2 and (rev[0]*diag)[i]==2 and (mats[0]*diag)[i]==-2)
j=receivers.index((4,1,4));slot01=slots.index((0,1));check('vertical_transpose_witness',raws[0][j,slot01]==0 and rev[0][j,slot01]==-2 and mats[0][j,slot01]==1)
# Einstein symbol on a scalar Hessian vanishes as an exact polynomial, including null.
k=s.symbols('k0:4');k2=sum(eta[a]*k[a]*k[a] for a in range(4));h=s.Matrix([[k[a]*k[b] for b in range(4)] for a in range(4)])
Ric=s.Matrix([[s.Rational(1,2)*(sum(eta[c]*k[c]*(k[a]*h[c,b]+k[b]*h[c,a]) for c in range(4))-k2*h[a,b]-k[a]*k[b]*sum(eta[c]*h[c,c] for c in range(4))) for b in range(4)] for a in range(4)])
check('Hessian_Einstein_zero_all_k',all(s.expand(z)==0 for z in Ric))
# General Fourier polynomial proves the curvature-from-curl differential identity.
hvars=s.symbols('h0:10');hu=s.Matrix([[hvars[slots.index(tuple(sorted((a,b))))] for b in range(4)] for a in range(4)])
curl=lambda a,b,cc:k[a]*hu[b,cc]-k[b]*hu[a,cc]
vb=[sum(eta[a]*curl(a,b,a) for a in range(4)) for b in range(4)]
riccurl=s.Matrix([[s.Rational(1,2)*(-sum(eta[a]*k[a]*curl(a,b,cc) for a in range(4))+k[cc]*vb[b]) for cc in range(4)] for b in range(4)])
ricdirect=s.Matrix([[s.Rational(1,2)*(sum(eta[a]*k[a]*(k[b]*hu[a,cc]+k[cc]*hu[a,b]) for a in range(4))-k2*hu[b,cc]-k[b]*k[cc]*sum(eta[a]*hu[a,a] for a in range(4))) for cc in range(4)] for b in range(4)])
check('metric_source_from_companion_curl',all(s.expand(z)==0 for z in riccurl-ricdirect))
ex=ricdirect.subs({**{k[i]:int(i==0) for i in range(4)},**{hvars[j]:int(slots[j]==(1,1)) for j in range(10)}})
sc=sum(eta[i]*ex[i,i] for i in range(4));ge=ex-s.diag(*eta[:4])*sc/2
check('sourceful_countercontrol',ex==s.diag(s.Rational(1,2),s.Rational(-1,2),0,0) and ge==s.diag(0,0,s.Rational(1,2),s.Rational(1,2)))
faults={
'half_normalized_j':['symmetric_trace_Hodge_Gram'] if Gram/4!=expected else [],
'upper_triangle_orthonormal':['symmetric_trace_Hodge_Gram'] if Gram!=s.diag(*[eta[a]*eta[b] for a,b in slots]) else [],
'raw_without_transpose':['vertical_transpose_witness'] if raws[0][j,slot01]/2!=mats[0][j,slot01] else [],
'symmetric_instead_of_skew':['explicit_TT_leakage'] if ((raws[0]+rev[0])*diag)[i]/2!=(mats[0]*diag)[i] else [],
'drop_vertical_receivers':['vertical_transpose_witness'] if mats[0][j,slot01]!=0 else [],
'K132_rank_normalization_as_A':['all100_full_curvature_columns'] if c.fscale(-2,Afixture)!=Gfixture else []}
assert all(checks.values()),[k for k,v in checks.items() if not v];assert all(faults.values()),faults
stem='k2297-symmetric-shiab-companion';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json','lab/process/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification.json','lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json']
data=dict(schema_version='1.0',result_id='K2297',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact rational native coefficients and symbolic tensor identities; local analytic extension in companion',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},coefficient_column_order=[[t,*slot] for t in range(4) for slot in slots],nonzero_receivers=[list(receivers[i]) for i in live],nonzero_coefficients=[[str(x) for x in Et.row(i)] for i in range(Et.rows)],reduced_row_basis=[[str(x) for x in er.row(i)] for i in range(20)],ranks=dict(firstjet=20,curl=20,stacked=20,axis=9,null=9,common=10),claim_ceiling='flat selected T0 germ and restricted symmetric unsourced-companion lift only; no full I1B exclusion')
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2297',checks=len(checks),faults=len(faults))))
