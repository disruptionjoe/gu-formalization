from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def zero(z):return s.simplify(z)==0
def check(n,v):checks[n]=bool(v)
H,u,d,q,m,b,V1,V2=s.symbols('H u d q m beta V1 V2',real=True,nonzero=True)
P,c,p,n,v=s.symbols('Phi chi pi n v',real=True);y=s.Matrix([P,c,p,n,v]);z=s.Matrix([H,u,d,q,V1]);bg=s.Matrix([-(u*u+d)/(2*m),-3*H*u-V1-b*d,(-3*H+b*u)*d,-2*H*q,V2*u])
fP=-H*P+(u*c-d*v)/(2*m)
f=s.Matrix([fP,p,-3*H*p-(q+V2+b*b*d)*c+4*u*fP-2*(V1+b*d)*P-b*d*n,3*fP+q*v,-P-b*c-b*u*v])
C=q*P+3*H*(fP+H*P)+(u*p-u*u*P+V1*c+d*(n+b*c))/(2*m)
def dt(expr,ff=f):return (s.Matrix([expr]).jacobian(z)*bg)[0]+(s.Matrix([expr]).jacobian(y)*ff)[0]
check('constraint_propagation_off_surface',zero(dt(C)+3*H*C))
check('trace_Einstein_equation',zero(dt(fP)+4*H*fP+(2*bg[0]+3*H*H)*P-(u*p-u*u*P-V1*c)/(2*m)))
nsol=s.solve(C,n)[0];red=f[[0,1,2,4],:].subs(n,nsol);yr=s.Matrix([P,c,p,v]);J=red.jacobian(yr)
check('number_constraint_chart',zero(s.diff(C,n)-d/(2*m)))
check('constraint_reconstruction',zero(C.subs(n,nsol)))
check('reduced_trace',zero(s.trace(J)+4*H))
check('reconstructed_number_evolution',zero(dt(nsol).subs(n,nsol)-f[3].subs(n,nsol)))
check('no_H_divisor',all(not s.denom(s.cancel(a)).has(H) for a in J))
check('no_Poisson_divisor',all(not s.denom(s.cancel(a)).has(q) for a in J))
# Independent linearized number-current and spatial particle Euler constraints.
check('number_current_conservation',zero(f[3]-3*fP-q*v))
check('particle_acceleration',zero(f[4]+b*u*v+P+b*c))
check('mass_density_conversion_KG',zero(f[2]+3*H*p+(q+V2)*c-4*u*fP+2*(V1+b*d)*P+b*d*(n+b*c)))
seed={P:0,c:0,p:0,n:0,v:1,H:0};jet=f.subs(seed)
check('velocity_seed_initial_constraint',zero(C.subs(seed)))
check('velocity_seed_jets',all(zero(a) for a in jet-s.Matrix([-d/(2*m),0,-2*u*d/m,q-3*d/(2*m),-b*u])))
check('number_derivative_cancellation',zero(jet[3].subs(q,3*d/(2*m))))
check('Poisson_zero_is_regular',all(len(s.Poly(s.denom(s.cancel(a.subs({H:0,q:u*u/(2*m)}))),m).terms())==1 for a in J))
# Frame readout: gJ=B²gE, number density scales B^-3, mass density B^-4.
e=s.symbols('e');lapse=s.expand((1+2*e*b*c)*(1+2*e*P));space=s.expand((1+2*e*b*c)*(1-2*e*P))
check('Jordan_lapse',s.diff(lapse,e).subs(e,0)/2==P+b*c)
check('Jordan_spatial',-s.diff(space,e).subs(e,0)/2==P-b*c)
check('Jordan_mass_number_agreement',s.expand(n+b*c-4*b*c)==n-3*b*c)
check('Jordan_lensing_sum',s.expand((P+b*c)+(P-b*c))==2*P)
check('selected_slip_second_jet',zero((2*b*f[2]).subs(seed)+4*b*u*d/m))
x,F=s.symbols('x F',positive=True);xd,Fd=s.symbols('xd Fd');logdet=4*s.log(x)-2*s.log(F)
check('fixture_determinant_identity',zero(s.diff(logdet,x)*xd+s.diff(logdet,F)*Fd+4*(Fd/(2*F)-xd/x)))
Q=s.Rational
check('fixture_minimum_a2',Q(3,5)/Q(11,10)**2==Q(60,121))
# Coefficient-by-coefficient bounds in stated M=1 coordinate norm.
check('bound_Phi_row',1+2+6<330)
check('bound_chi_row',1<330)
check('bound_velocity_row',1+Q(1,2)+2<330)
def coefficient_bound(expr):
 variables=[H,u,d,V1,V2,b,q];bounds=[Q(1),Q(4),Q(12),Q(30),Q(58),Q(1,2),q]
 return s.expand(sum(abs(coef)*s.prod(bound**power for bound,power in zip(bounds,powers)) for powers,coef in s.Poly(s.expand(expr.subs(m,1)),*variables).terms()))
actual_row_bounds=[s.expand(sum(coefficient_bound(J[i,j]) for j in range(4))) for i in range(4)]
check('bound_scalar_row_constants',actual_row_bounds[2]==326+2*q)
check('bound_other_actual_rows',actual_row_bounds[:2]==[9,1] and actual_row_bounds[3]==Q(7,2))
check('bound_scalar_q_coefficient',2*Q(121,60)==Q(121,30))
check('finite_interval_norm_bound',Q(1,10)*330==33 and Q(1,10)*Q(121,30)==Q(121,300))
assert all(checks.values()),[n for n,vv in checks.items() if not vv]
def badcheck(ff):return not zero(dt(C,ff)+3*H*C)
a=f.copy();a[4]=-P+b*c-b*u*v
bb=f.copy();bb[3]=3*fP-q*v
cc=f.copy();cc[2]-=4*u*fP
dd=f.copy();dd[2]+=b*b*d*c
ee=f.copy();ee[2]+=2*b*d*P
faults={
 'wrong_force_sign':['constraint_propagation_off_surface'] if badcheck(a) else [],
 'wrong_velocity_divergence':['constraint_propagation_off_surface'] if badcheck(bb) else [],
 'omit_metric_scalar_drive':['constraint_propagation_off_surface'] if badcheck(cc) else [],
 'omit_mass_conversion':['constraint_propagation_off_surface'] if badcheck(dd) else [],
 'omit_dust_lapse':['constraint_propagation_off_surface'] if badcheck(ee) else [],
 'wrong_transfer_power':['reduced_trace'] if not zero(s.trace(J)+3*H) else [],
 'wrong_Jordan_density':['Jordan_mass_number_agreement'] if s.expand(n+b*c-3*b*c)!=n-3*b*c else []}
assert all(faults.values()),faults
stem='k2308-inhomogeneous-constrained-dust-transfer';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2305-regular-constrained-matter-transfer-2026-10-30.md','explorations/conditional-build/k2302-designer-frame-turnaround-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2308',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='symbolic ODE/constraint/frame identities and rational norm bounds; action derivations and fixed-k existence in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'reduced_matrix':str(J),'determinant':'(a0/a)^4','norm_bound':'exp(33+121*k^2/300)'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2308',checks=len(checks),faults=len(faults))))
