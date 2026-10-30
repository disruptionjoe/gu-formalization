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
# Reuse the exact general-curvature map, never predecessor result assertions.
tree=ast.parse((ROOT/'tests/channel-swings/k2307_spatial_coupled_native_mode_probe.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'curvature','metslot'}],type_ignores=[]),'k2307_curvature','exec'))
cc=Q(3,5);ss=(Q(0),Q(4,5));normal=10
q=[(Q(0),Q(0))]*14;q[0]=(cc,Q(0));q[normal]=ss
q0=[(Q(int(i==0)),Q(0)) for i in range(14)]
def boost(f,inverse_gamma=True):
 out={}
 for fm,e in f.items():
  assert fm.bit_count()==1;mu=fm.bit_length()-1
  other=normal if mu==0 else 0
  forms={mu:(Q(1),Q(0))} if mu not in (0,normal) else {mu:(cc,Q(0)),other:ss}
  for J,z in e.items():
   cl={0:(Q(1),Q(0))}
   for j in range(14):
    if J>>j&1:
     other=normal if j==0 else 0
     gj=c.blade(j) if j not in (0,normal) else c.eadd(es((cc,Q(0)),c.blade(j)),es(neg(ss) if inverse_gamma else ss,c.blade(other)))
     cl=c.emul(cl,gj)
   for nu,w in forms.items():out=c.fadd(out,{1<<nu:es(gmul(z,w),cl)})
 return out
P={1,2,3,normal}
to=total(c.fscale(Q(5,36)*(3 if i in P else -1),form(i,(i,))) for i in range(1,14))
te=total(c.fscale(Q(5,36)*(3 if i in P else -5),form(i,(0,i))) for i in range(1,14))
bo=boost(to);be=boost(te);ratio=Q(5,29)
h=metslot(1,1);h[2][2]=h[3][3]=(Q(1),Q(0));h[0][0]=(-Q(25,16),Q(0))
hseed=metslot(1,1);hseed[2][2]=hseed[3][3]=hseed[normal][normal]=(Q(1),Q(0))
def Lq(f,k=q):return total(fs(k[t],La(t,f)) for t in range(14) if k[t]!=(0,0))
def residual(o,e,hh=h,r=ratio):return c.fadd(o,c.fscale(r,Lq(e)),c.fscale(r,c.hodge(curvature(q,hh)))),c.fadd(e,Lq(o))
check('normal_is_negative',eta[normal]==-1)
check('phi1_fixed',boost(c.phi1)==c.phi1)
check('odd_companion_full',not residual(bo,be)[0]);check('even_companion_full',not residual(bo,be)[1])
slots=[(i,j) for i in range(4) for j in range(i,4)]
for slot in slots:
 dual=curvature(q,metslot(*slot));check('horizontal_metric_'+str(slot),c.pair(bo,dual)==(0,0) and c.pair(be,dual)==(0,0))
# Boost seed metric explicitly, then remove normal slots by a pure gauge.
hboost=metslot(1,1);hboost[2][2]=hboost[3][3]=(Q(1),Q(0));hboost[0][0]=gmul(ss,ss);hboost[0][normal]=hboost[normal][0]=gscale(cc,ss);hboost[normal][normal]=(cc*cc,Q(0))
v=[(Q(0),Q(0))]*14;v[0]=(-Q(123,160),Q(0));v[normal]=(Q(0),Q(9,40))
gauge=[[gadd(gmul(q[i],v[j]),gmul(v[i],q[j])) for j in range(14)] for i in range(14)]
check('gauge_adjustment_metric',all(gadd(hboost[i][j],gauge[i][j])==h[i][j] for i in range(14) for j in range(14)))
check('gauge_curvature_zero',not curvature(q,gauge))
check('native_covariance',c.hodge(curvature(q,h))==boost(c.hodge(curvature(q0,hseed))))
# Curvature scalar uses all ambient covector entries and only declared metric slots.
def scalar(hh):
 ks=tr=kh=(Q(0),Q(0))
 for i in range(14):
  ks=gadd(ks,gscale(eta[i],gmul(q[i],q[i])));tr=gadd(tr,gscale(eta[i],hh[i][i]))
  for j in range(14):kh=gadd(kh,gscale(eta[i]*eta[j],gmul(gmul(q[i],q[j]),hh[i][j])))
 return gadd(kh,neg(gmul(ks,tr)))
check('nongauge_curvature_four',scalar(h)==(4,0))
check('full105_not_solved',c.pair(bo,curvature(q,metslot(11,11)))!=(0,0))
# The old rank-three seed is not a solution after time-normal boosting.
old_o=total(c.fscale(Q(17,270)*(5 if i<=3 else -1),form(i,(i,))) for i in range(1,14))
check('old_boost_horizontal_row_fails',c.pair(boost(old_o),curvature(q,metslot(0,0)))!=(0,0))
# Rank formula derived from two independent transverse response coefficients.
def rank_root(m):return Q(1+11*m,121+35*m)
check('rank3_inherited',rank_root(3)==Q(17,113));check('rank4_new',rank_root(4)==ratio)
check('pole_avoidance',1-4*ratio!=0 and 1-121*ratio!=0)
check('patch_positive',Q(1)-Q(16,25)==Q(9,25))
assert all(checks.values()),[k for k,vv in checks.items() if not vv]
no_time=[row[:] for row in h];no_time[0][0]=(Q(0),Q(0))
faults={
 'old_root':['odd_companion_full'] if any(residual(bo,be,r=Q(17,113))) else [],
 'omit_even':['odd_companion_full'] if any(residual(bo,{})) else [],
 'omit_distortion_boost':['odd_companion_full'] if any(residual(to,te)) else [],
 'wrong_Clifford_transform':['phi1_fixed'] if boost(c.phi1,False)!=c.phi1 else [],
 'delete_time_metric':['odd_companion_full'] if any(residual(bo,be,hh=no_time)) else [],
 'drop_normal_distortion':['odd_companion_full'] if any(residual({fm:e for fm,e in bo.items() if fm<16},be)) else []}
assert all(faults.values()),faults
stem='k2310-normal-localized-coupled-branch'
deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),source,'tests/channel-swings/k2307_spatial_coupled_native_mode_probe.py','tests/channel-swings/k77_exact_bank_api.py','tests/fixtures/k77_exact_coefficient_bank_v1.json']
data=dict(schema_version='1.0',result_id='K2310',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact native Gaussian-rational witness and altered-input failures; universal patch and restriction proofs in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'root':'5/29','old_root':'17/113','selected_metric_rows':10,'full105_not_solved':True,'curvature_over_b2':'4'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2310',checks=len(checks),faults=len(faults))))
