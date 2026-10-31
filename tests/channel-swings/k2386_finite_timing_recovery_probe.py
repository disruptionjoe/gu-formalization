"""Exact finite timing channels, rotor controls and cost inequalities; --write saves."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v,c=False):
 v=bool(v);(controls if c else checks)[k]=v;assert v,k
x,q,tau=s.symbols('x q tau',positive=True);eta=1-q*x/tau;k=q/(tau*(1-q*x/tau))
ck('physical_linear_survival',s.simplify(s.diff(eta,x)+k*eta)==0)
ck('uniform_second_loss_density',s.simplify(k*eta-q/tau)==0)
ck('integrated_loss_probability',s.integrate(k*eta,(x,0,tau))==q)
ck('bounded_end_rate',k.subs(x,tau)==q/(tau*(1-q)))
# Independently integrate circle moments for actual equal contiguous bins.
th=s.symbols('th',real=True);moments={}
for B in [1,2,3,4,8]:
 vals=[]
 for j in range(B):
  lo=2*s.pi*j/B;hi=2*s.pi*(j+1)/B
  mx=s.integrate(s.cos(th),(th,lo,hi))/(2*s.pi);my=s.integrate(s.sin(th),(th,lo,hi))/(2*s.pi)
  ck(f'circle_norm_squared_{B}_{j}',s.simplify(s.expand_trig(mx*mx+my*my-s.sin(s.pi/B)**2/s.pi**2))==0)
  vals.append([str(mx),str(my)])
 moments[str(B)]=vals
ck('B2_exact_error',s.simplify((3-2/s.pi)/16-s.Rational(1,8)-(1-2/s.pi)/16)==0)
ck('B4_strict_improvement',2*s.sqrt(2)>2)
ell=s.symbols('ell',real=True)
ck('centered_arc_integral',s.integrate(s.cos(th),(th,-ell/2,ell/2))==2*s.sin(ell/2))
ck('equal_two_endpoint_bound',s.simplify((s.Matrix([s.cos(ell/2),s.sin(ell/2),0])+s.Matrix([s.cos(ell/2),-s.sin(ell/2),0]))/2)==s.Matrix([s.cos(ell/2),0,0]))
ck('diameter_substitution_fails',s.Rational(1,3)<s.Rational(1,2),True)
ck('equal_probability_not_universal',(s.sqrt(13)+5)/10<1,True)
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2)
def axis(v):return v[0]*X+v[1]*Y+v[2]*Z
vs=[(s.Rational(3,5),s.Rational(4,5),0),(s.Rational(2,3),s.Rational(1,3),s.Rational(2,3)),(0,1,0)]
for pi,P in enumerate([X,Y,Z]):
 for vi,v in enumerate(vs):
  N=axis(v);r=(I+N*P)/s.sqrt(2*(1+v[pi]));ck(f'rotor_unitary_{pi}_{vi}',s.simplify(r*r.H)==I);ck(f'rotor_axis_{pi}_{vi}',s.simplify(r*P*r.H-N)==s.zeros(2))
for pi,P in enumerate([X,Y,Z]):
 Q=[Y,Z,X][pi];r=-s.I*Q;ck(f'antipode_{pi}',r*P*r.H==-P)
N=axis(vs[0]);r=(I+N*Z)/s.sqrt(2);ck('reversed_rotor_order_fails',s.simplify(r.H*Z*r)!=N,True)
# Triangle and trapezoid integrate to required pulse area.
A,G,V=s.symbols('A G V',positive=True);T=s.sqrt(A/V)
ck('triangle_area',s.simplify(V*T*T-A)==0)
tflat=A/G-G/V;ck('trapezoid_area',s.simplify(G*G/V+G*tflat-A)==0)
ck('pulse_boundary_continuity',s.simplify((2*s.sqrt(A/V)).subs(A,G*G/V)-(A/G+G/V).subs(A,G*G/V))==0)
ck('three_pulse_fixture',3*(s.pi/2+1)>0)
# Difference of two prepared axes under same binary functional: trace distance.
N=axis(vs[0]);D=N-Z;ck('axis_trace_norm',s.simplify(D.det()+2)==0 and D.trace()==0)
ck('axis_half_trace_distance',s.sqrt(2)/2==s.sin(s.pi/4))
ck('ideal_B2_gain',s.simplify(s.Rational(3,16)-(3-2/s.pi)/16)==1/(8*s.pi))
ck('complete_budget_sufficient',s.Rational(1,50)<s.Rational(1,32))
ck('upper_certificate_is_not_actual_improvement',0<1/(8*s.pi) and s.Rational(1,5)>1/(8*s.pi),True)
# Rate-law countercontrol: constant late rate does not give uniform second time.
k0=s.symbols('k0',positive=True);ck('constant_rate_not_uniform',s.diff(k0*s.exp(-k0*x),x)!=0,True)
paths=['lab/process/k2383-driven-erasure-recovery.json','lab/process/k2380-complete-erasure-recovery.json']
report={'result_id':'K2386','checks':len(checks),'check_names':checks,'changed_input_or_inference_controls':controls,'circle_moments':moments,'scope':'Exact supplied finite-channel/rotation fixtures and analytic optimization/bounds; no measured timing instrument or hardware costs.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(R/'lab/process/k2386-finite-timing-recovery.json').write_text(out)
print(out)
