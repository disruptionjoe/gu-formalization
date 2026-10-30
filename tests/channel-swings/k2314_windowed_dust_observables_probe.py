"""Exact transfer/covariance controls; infinite Gaussian theorems are proved in note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def zero(x):return s.simplify(x)==0
def check(n,x):
 checks[n]=bool(x)
 if not x:raise AssertionError('[FAIL] '+n)
H,u,d,q,m,b,V1,a,N=s.symbols('H u d q m beta V1 a N',nonzero=True,real=True)
Phi,chi,pi,n,v=s.symbols('Phi chi pi n v');fPhi=-H*Phi+(u*chi-d*v)/(2*m)
constraint=q*Phi+3*H*(fPhi+H*Phi)+(u*pi-u*u*Phi+V1*chi+d*(n+b*chi))/(2*m)
nsol=s.solve(constraint,n)[0]
L=2*Phi;nJ=n-3*b*chi;C=nJ+m*q*L/d
rhs=u*u*Phi-(3*H*u+V1+4*b*d)*chi+3*H*d*v-u*pi
check('compensated_constraint',zero((d*C-rhs).subs(n,nsol)))
check('off_shell_defect',zero(d*C-rhs-2*m*constraint))
check('frame_potential_sum',zero((Phi+b*chi)+(Phi-b*chi)-L))
seed={H:0,Phi:0,chi:0,pi:0,n:0,v:1/N,q:N*N/a**2}
check('seed_constraint',zero(constraint.subs(seed)))
check('physical_velocity_normalization',zero((N*v/a).subs(seed)-1/a))
r,ss,W,p=s.symbols('r ss W p');alpha=u/(2*m)
ph=(r-alpha*p)/q;vel=(ss+b*p)/q;ch=W+2*b*m*ph
pip=p+2*b*m*(-H*ph+(u*ch-d*vel)/(2*m))
rep={Phi:ph,v:vel,chi:ch,pi:pip,q:N*N/a**2}
# Slow-normalized variables r=N*r0,ss=N*s0, p=O(1/N), W=O(1/N²).
r0,s0,p0,w0=s.symbols('r0 s0 p0 w0')
sub={r:N*r0,ss:N*s0,p:p0/N,W:w0/N**2}
phys={key:s.simplify(val.subs(q,N*N/a**2).subs(sub)) for key,val in rep.items() if key!=q}
nexpr=s.simplify(nsol.subs(phys,simultaneous=True).subs(q,N*N/a**2));cexpr=s.simplify((rhs/d).subs(phys,simultaneous=True))
delta=-2*m*r0/d
check('density_limit',zero(s.limit(nexpr/N,N,s.oo)-delta))
check('potential_limit',zero(s.limit(N*2*phys[Phi],N,s.oo)+a*a*d*delta/m))
check('scalar_limit',zero(s.limit(N*phys[chi],N,s.oo)+b*a*a*d*delta))
check('compensated_N_limit_zero',zero(s.limit(cexpr/N,N,s.oo)))
check('compensated_inverse_N_bound',not s.limit(N*cexpr,N,s.oo).has(s.oo,-s.oo,s.zoo))
check('density_remainder_inverse_N',not s.limit(N*(nexpr-N*delta),N,s.oo).has(s.oo,-s.oo,s.zoo))
# Two independent conjugate mode pairs with real transfer and complex windows.
P=[s.Rational(2),s.Rational(3)];w=[s.Rational(1)+s.I,s.Rational(2)-s.I];t=[s.Rational(2),s.Rational(5)]
# O=2Re(conj(w)T V), Re/Im V independent each with variance P/2.
realvar=sum((2*s.re(s.conjugate(ww)*tt))**2*pp/2+(2*s.re(s.I*s.conjugate(ww)*tt))**2*pp/2 for ww,tt,pp in zip(w,t,P))
fullsum=2*sum(s.conjugate(ww)*ww*tt*tt*pp for ww,tt,pp in zip(w,t,P))
check('conjugate_pair_variance',zero(realvar-fullsum))
# Each rank1 covariance is PSD, but their sum need not be rank1.
x=s.Matrix([1,2]);y=s.Matrix([2,1]);Cx=x*x.T;Cy=y*y.T
check('mode_rank_one',Cx.det()==Cy.det()==0)
check('summed_rank_two',(Cx+Cy).det()==9)
check('cross_covariance_psd',(Cx+Cy)[0,0]>0 and (Cx+Cy).det()>0)
# Exact two-mode change to compensated readout, from genuine paired covariance.
A=s.Matrix([[1,2],[1,-1]]);cov=s.diag(2,3);covout=A*cov*A.T
check('joint_cancellation_variance',(s.Matrix([[1,-1]])*covout*s.Matrix([1,-1]))[0]==27)
check('covariance_not_independent',covout[0,1]==-4)
# Exponent arithmetic is a consistency control; the lattice/series proof is prose.
power,reg=s.symbols('power reg');check('density_shell_exponent',s.expand(2+2+2*reg-power)==2*reg+4-power)
check('potential_shell_exponent',s.expand(2-2+2*reg-power)==2*reg-power)
check('p4_velocity_finite_density_not',2-4 < -1 and 4-4 >= -1)
gamma,Snn,SnL,SLL,dg=s.symbols('gamma Snn SnL SLL dg',real=True)
row=s.Matrix([[1,gamma*q]]);noise=s.Matrix([[Snn,SnL],[SnL,SLL]])
noisevar=(row*noise*row.T)[0]
check('noise_covariance_exact',s.expand(noisevar)==Snn+2*gamma*q*SnL+gamma**2*q*q*SLL)
check('anticorrelated_noise_zero',zero(noisevar.subs({Snn:gamma**2*q*q*SLL,SnL:-gamma*q*SLL})))
check('white_potential_noise_order4',s.degree(noisevar.subs({SnL:0,q:N*N/a**2}),N)==4)
error=dg*(N*N/a**2)*2*phys[Phi]
check('calibration_error_leading',zero(s.limit(error/N,N,s.oo)+dg*d*delta/m))
check('frequency_decaying_repair',not s.limit(N*error.subs(dg,dg/N**2),N,s.oo).has(s.oo,-s.oo,s.zoo))
assert all(checks.values())
faults={
 'wrong_Jordan_density':not zero((d*(n-b*chi+m*q*L/d)-rhs).subs(n,nsol)),
 'omit_scalar_charge':not zero((d*C-(rhs+4*b*d*chi)).subs(n,nsol)),
 'wrong_potential_coefficient':not zero((d*(nJ+m*q*Phi/d)-rhs).subs(n,nsol)),
 'omit_conjugate_pair':not zero(realvar-fullsum/2),
 'omit_cross_covariance':(s.Matrix([[1,-1]])*s.diag(covout[0,0],covout[1,1])*s.Matrix([1,-1]))[0]!=27,
 'assume_summed_rank_one':(Cx+Cy).det()!=0,
 'omit_q_in_potential_noise':not zero(noisevar-(Snn+2*gamma*SnL+gamma**2*SLL)),
 'constant_error_as_decaying':not zero(s.limit(error/N,N,s.oo))}
assert all(faults.values()),'[FAIL] mutation not detected'
stem='k2314-windowed-dust-observables';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2311-uniform-constrained-dust-evolution-2026-10-30.md','tests/channel-swings/k2311_uniform_constrained_dust_evolution_probe.py','explorations/conditional-build/k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2314',checks=len(checks),check_names=list(checks),mutation_failed_checks={n:['constraint_or_covariance'] for n in faults},evidence_kind='exact symbolic constraint/asymptotic coefficients and finite covariance; exponent arithmetic consistency; infinite Gaussian/domain proof in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'compensated_constraint_rhs':str(rhs),'compensated_scaled_limit':str(s.limit(N*cexpr,N,s.oo)),'white_density_window':'H1','generic_compensated_window_sufficient':'H^(-1-p/2)'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2314',checks=len(checks),faults=len(faults))))
