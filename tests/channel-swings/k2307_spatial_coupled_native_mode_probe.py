from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
import ast,json,hashlib,sys
from k77_exact_bank_api import K77Core,load_bank,gadd,gmul,gscale
ROOT=Path(__file__).resolve().parents[2];bank=load_bank();c=K77Core(bank.signature,bank.channels);eta=c.eta;checks={}
def check(n,v):checks[n]=bool(v)
def neg(z):return (-z[0],-z[1])
def es(z,e):return {m:gmul(z,v) for m,v in e.items() if gmul(z,v)!=(0,0)}
def fs(z,f):return {m:es(z,e) for m,e in f.items() if es(z,e)}
def total(fs0):
 out={}
 for f in fs0:out=c.fadd(out,f)
 return out
source='tests/channel-swings/k2298_enlarged_native_companion_probe.py';tree=ast.parse((ROOT/source).read_text());exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'form','Epair','Laxis'}],type_ignores=[]),source,'exec'))
@lru_cache(None)
def unitL(t,fm,J):return Laxis(t,{fm:{J:(Q(1),Q(0))}})
def La(t,f):return total(fs(z,unitL(t,fm,J)) for fm,e in f.items() for J,z in e.items())
# Gaussian rational complex Lorentz boost; form B, Clifford inverse transpose.
cc=Q(3,5);ss=(Q(0),Q(4,5));q=[(cc,Q(0)),ss]+[(Q(0),Q(0))]*12

def boost(f,inverse_gamma=True):
 out={}
 for fm,e in f.items():
  assert fm.bit_count()==1;mu=fm.bit_length()-1
  forms={mu:(Q(1),Q(0))} if mu>1 else {mu:(cc,Q(0)),1-mu:ss}
  for J,z in e.items():
   cl={0:(Q(1),Q(0))}
   for j in range(14):
    if not J>>j&1:continue
    gj=c.blade(j) if j>1 else c.eadd(es((cc,Q(0)),c.blade(j)),es(neg(ss) if inverse_gamma else ss,c.blade(1-j)))
    cl=c.emul(cl,gj)
   for nu,w in forms.items():out=c.fadd(out,{1<<nu:es(gmul(z,w),cl)})
 return out

def curvature(k,h):
 out={}
 for i,j in combinations(range(14),2):
  val={}
  for a,b in combinations(range(14),2):
   terms=[gmul(gmul(k[i],k[a]),h[j][b]),neg(gmul(gmul(k[i],k[b]),h[j][a])),neg(gmul(gmul(k[j],k[a]),h[i][b])),gmul(gmul(k[j],k[b]),h[i][a])]
   z=(Q(0),Q(0))
   for term in terms:z=gadd(z,term)
   z=gscale(-Q(1,2)*eta[a]*eta[b],z)
   if z!=(0,0):val=c.eadd(val,es(z,c.blade((a,b))))
  if val:out[(1<<i)|(1<<j)]=val
 return c.shiab(out)
def metslot(a,b):
 h=[[(Q(0),Q(0)) for _ in range(14)] for _ in range(14)];h[a][b]=h[b][a]=(Q(1),Q(0));return h
h=[[(Q(0),Q(0)) for _ in range(14)] for _ in range(14)];h[0][0]=gmul(ss,ss);h[0][1]=h[1][0]=gscale(cc,ss);h[1][1]=(cc*cc,Q(0));h[2][2]=h[3][3]=(Q(1),Q(0))
h0=[[(Q(int(i==j and i in (1,2,3))),Q(0)) for j in range(14)] for i in range(14)];q0=[(Q(int(i==0)),Q(0)) for i in range(14)]
to=total(c.fscale(Q(17,270)*(5 if i<=3 else -1),form(i,(i,))) for i in range(1,14))
te=total(c.fscale(Q(17,270)*(5 if i<=3 else -7),form(i,(0,i))) for i in range(1,14))
bo=boost(to);be=boost(te);a2=Q(17,113)
def Lq(f,k=q):return total(fs(k[t],La(t,f)) for t in range(14) if k[t]!=(0,0))
A=c.hodge(curvature(q,h))
def residual(o,e,hh=h,ratio=a2):return c.fadd(o,c.fscale(ratio,Lq(e)),c.fscale(ratio,c.hodge(curvature(q,hh)))),c.fadd(e,Lq(o))
check('phi1_fixed',boost(c.phi1)==c.phi1)
check('Lorentz_relation',gadd((cc*cc,Q(0)),neg(gmul(ss,ss)))==(1,0))
check('native_curvature_covariance',A==boost(c.hodge(curvature(q0,h0))))
check('odd_full_companion',not residual(bo,be)[0]);check('even_full_companion',not residual(bo,be)[1])
slots=[(i,j) for i in range(4) for j in range(i,4)]
for slot in slots:
 dual=curvature(q,metslot(*slot));check('metric_row_'+str(slot),c.pair(bo,dual)==(0,0) and c.pair(be,dual)==(0,0))
# Direct linearized scalar curvature for the displayed horizontal h.
ksq=(Q(0),Q(0));tr=(Q(0),Q(0));kkh=(Q(0),Q(0))
for i in range(4):
 ksq=gadd(ksq,gscale(eta[i],gmul(q[i],q[i])));tr=gadd(tr,gscale(eta[i],h[i][i]))
 for j in range(4):kkh=gadd(kkh,gscale(eta[i]*eta[j],gmul(gmul(q[i],q[j]),h[i][j])))
curv=gadd(kkh,neg(gmul(ksq,tr)));check('nongauge_scalar_curvature',curv==(3,0))
check('growth_dispersion',cc*cc+Q(4,5)**2==1 and 0<cc<1)
# Actual source/flux contraction in bank signature (+,-,-,-).
eta4=eta[:4];observer=[Q(5,4),Q(3,4),Q(0),Q(0)];stress=[Q(0),Q(1),Q(1),Q(1)]
def energy(J):return sum(J[i]*observer[i]**2 for i in range(4))
def fluxnorm(J):return sum(eta4[i]*(eta4[i]*J[i]*observer[i])**2 for i in range(4))
check('WEC_timelike_control',sum(eta4[i]*observer[i]**2 for i in range(4))==1 and energy(stress)==Q(9,16))
check('DEC_flux_spacelike_control',fluxnorm(stress)==-Q(9,16))
check('normal_support_retained',any(fm>=1<<4 for fm in bo))
assert all(checks.values()),[n for n,v in checks.items() if not v]
faults={
 'negative_pressure':['WEC_timelike_control'] if energy([Q(0),Q(-1),Q(-1),Q(-1)])<0 else [],
 'same_clifford_boost':['phi1_fixed'] if boost(c.phi1,False)!=c.phi1 else [],
 'metric_only_boost':['odd_full_companion'] if any(residual(to,te)) else [],
 'omit_even_distortion':['odd_full_companion'] if any(residual(bo,{})) else [],
 'wrong_dispersion':['odd_full_companion'] if any(residual(bo,be,ratio=Q(17,112))) else [],
 'delete_time_metric':['odd_full_companion'] if any(residual(bo,be,hh=h0)) else [],
 'drop_normal_distortion':['odd_full_companion'] if any(residual({fm:e for fm,e in bo.items() if fm<1<<4},be)) else []}
assert all(faults.values()),faults
stem='k2307-spatial-coupled-native-mode';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),source,'tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json','lab/process/k2304-coupled-temporal-source-response.json']
data=dict(schema_version='1.0',result_id='K2307',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact native Gaussian-rational full-row witness; general covariance/domain arguments in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'lambda_over_a':'3/5','p_over_a':'4/5','scalar_curvature_over_a2':'3','full_metric_rows':10})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2307',checks=len(checks),faults=len(faults))))
