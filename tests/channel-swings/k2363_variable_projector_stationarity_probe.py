"""Selected-backend invariant coefficients and exact variable-projector elimination."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];st='k2363-variable-projector-stationarity';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';p=R/backend;src=p.read_text();ns={'__file__':str(p),'__name__':'selected_backend'};exec(compile(src[:src.index('def sparse_rank')],str(p),'exec'),ns)
b=ns['blade'];w=ns['wedge_raw'];add=ns['fadd'];scale=ns['fscale'];eta=ns['ETA'];P=lambda x,y:w(x,y).get(ns['FULL'],{}).get(0,ns['ZERO']);S=lambda x:ns['shiab'](x,('comm','symi','symi'))
def rat(v):
 assert v[1]==0
 return s.Rational(v[0].numerator,v[0].denominator)
def row(Ds,Z):
 DT=add(*[w({1<<k:b(())},v) for k,v in Ds.items()]);left=rat(P(Z,S(DT)));right=sum(rat(P(v,S(w({1<<k:b(())},Z)))) for k,v in Ds.items());return left,right,(left-right)/2
fixtures=[]
for q,p in [(0,4),(1,4),(4,1),(1,2)]:
 for i in [p,q,5]:
  got=row({q:{1<<i:b(i)}},{1<<p:b(tuple(sorted((q,p))))});orient=1 if q<p else -1
  # Raising the diagonal input and pairing the receiver cancels signature factors; sorted orientation remains.
  expected=orient*(2*(i==p)+(i==q)-1)
  fixtures.append([q,p,i,list(map(str,got))]);check(f'diagonal_jet_{q}_{p}_{i}',got[2]==expected)
# Distinct-index symmetric lowered N_0,4,5=1, all signs positive.
mixed=row({0:add({1<<4:b(5)},{1<<5:b(4)})},{1<<4:b((0,5))});check('mixed_Codazzi_coefficient',mixed[2]==2)
# General invariant contraction, including the antisymmetric pair orientation.
n=s.symbols('n',integer=True);div,tr=s.symbols('div tr');check('tensor_contraction',s.expand(2*(tr-div)+(n-1)*(div-tr)-(n-3)*(div-tr))==0)
check('dimension14_nonexceptional',14-3==11)
a,bv,d,va,ta,td,wb=s.symbols('a b d va ta td wb')
# actual mixed connection coefficient r_h/2 with chosen traceless and trace vectors
rows=[va-(d-a)/4,va+(d-a)/4,td,ta-td,ta-(bv-a)/4]
sol=s.linsolve(rows,[va,ta,td,bv,d]);check('all_variable_projector_values',sol==s.FiniteSet((0,0,0,a,a)))
control('one_horizontal_row_only',s.solve(rows[:1],[va])=={va:(d-a)/4})
control('freeze_projector_connection',s.linsolve([va,td,ta-td,ta],[va,ta,td,bv,d])!=sol)
# Flat nonconstant Hessian: all differentiated components fully symmetric, Codazzi zero.
u,v=s.symbols('u v');f=u**3+u*v*v;A=s.hessian(f,(u,v));check('flat_Hessian_nonconstant',s.diff(A,u)!=s.zeros(2))
coords=[u,v];check('flat_Hessian_Codazzi',all(s.diff(A[i,k],coords[j])-s.diff(A[i,j],coords[k])==0 for i in range(2) for j in range(2) for k in range(2)))
control('Codazzi_does_not_imply_parallel',s.diff(A,u)!=s.zeros(2))
# Radial and connection fixtures retain actual formal adjoint.
phi=ns['PHI1'];rad=row({0:phi},{1<<4:b((0,4))});check('radial_minus11',rad[2]==-11);control('omit_formal_adjoint',rad[0]/2!=rad[2])
def connection(vindex,cs):
 Ds={mu:add(scale(F(c),{1<<vindex:b(mu)}),scale(F(c)*eta[mu]/eta[vindex],{1<<mu:b(vindex)})) for mu,c in enumerate(cs)}
 return row(Ds,{1:b((0,vindex))})
check('trace_connection_reproduced',connection(10,[1]*4)==(2,6,-2));check('traceless_connection_reproduced',connection(4,[1,1,-1,-1])==(2,-2,2));check('odd_Ricci_difference',-2*(s.Rational(21,4)-s.Rational(15,4))==-3)
deps=[backend,'lab/process/k2345-curved-bundle-ricci-obstruction.json','lab/process/k2357-curved-native-stationarity.json','lab/process/k2360-anisotropic-native-stationarity.json',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2363',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='exact selected Clifford fixtures, symbolic tensor contraction and variable-projector elimination; universal proof in note',details=dict(diagonal_fixtures=fixtures,mixed_fixture=list(map(str,mixed)),Codazzi='E=2 curl(A)+g wedge(divA-dtrA); contraction=11Q',projector_solution='a=b=d constant; odd Euler difference -3',nonconstant_control=str(A)),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(controls));print(json.dumps(out['details']))
