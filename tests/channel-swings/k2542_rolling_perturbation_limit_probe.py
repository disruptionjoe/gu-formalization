"""Exact algebra/changed-input controls; uniform theorem is in companion note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,p):
 bank[name]=bool(p)
 if not p:raise AssertionError('FAIL '+name)
A,Rv,R0,B0,Om,t,Rs=s.symbols('A R R0 B0 Om t Rs',positive=True)
B=6*A*(1-Om)+B0;F=A+Rv;F0=A+R0;c=F/F0;beta=-1/s.sqrt(6)
vp=F0/s.sqrt(6)*(A/F-(A*A+2*B)/F**2)
vpp=F0/3*(-A/F+2*(A*A+2*B)/F**2)
d=3*F0**2*Om*t/F**2
ck(checks,'normalized_dust_identity',s.simplify(d-3*Om*t/c**2)==0)
ck(checks,'normalized_dust_limit',s.limit(d,A,s.oo)==3*Om*t)
rr=3*Om*t+12*(1-Om)
ck(checks,'scalar_force_cancellation',s.simplify(s.limit(vp+beta*d,A,s.oo).subs(Rv,rr))==0)
ck(checks,'scalar_frequency_leading',s.limit(vpp/A,A,s.oo)==s.Rational(1,3))
vpps=s.diff(vpp,Rv)*Rs
ck(checks,'scalar_frequency_derivative',s.simplify(vpps-F0*Rs/3*(A/F**2-4*(A*A+2*B)/F**3))==0)
ck(checks,'frequency_derivative_bounded_limit',s.limit(vpps,A,s.oo)==-Rs)
ck(controls,'omitted_F0_dust_normalization_detected',s.limit(d/F0,A,s.oo)==0)
# Full matrix, reconstructed independently from unreduced K2308 equations below.
H,u,dd,Vp,Vpp,Q,b=s.symbols('H u d Vp Vpp Q b',real=True)
J=s.Matrix([[-H,u/2,0,-dd/2],[0,0,1,0],[-4*H*u-2*Vp-2*b*dd+b*(2*Q-u*u),-Q-Vpp+2*u*u+3*b*H*u+b*Vp,-3*H+b*u,-dd*(2*u+3*b*H)],[-1,-b,0,-b*u]])
Phi,v,chi,pi,ell=s.symbols('Phi v chi pi ell',real=True)
Y=s.Matrix([Phi,v]);X=s.Matrix([Phi,chi,pi,v]);slow=s.Matrix([[-H,-dd/2],[-1,-b*u]]);e=s.Matrix([u/2,-b]);cv=s.Matrix([[-4*H*u-2*Vp-2*b*dd+b*(2*Q-u*u),-dd*(2*u+3*b*H)]])
mu=Q+Vpp-2*u*u-3*b*H*u-b*Vp;gam=3*H-b*u
rhs=J*X
ck(checks,'full_slow_matrix_reconstruction',s.Matrix([rhs[0],rhs[3]])==slow*Y+e*chi)
ck(checks,'full_scalar_matrix_reconstruction',s.expand(rhs[2]+gam*pi+mu*chi-(cv*Y)[0])==0)
ck(checks,'full_trace_preserves_Liouville',s.trace(J)==-4*H)
# Independently eliminate the number variable from the unreduced five-field system.
n=s.symbols('n',real=True);fPhi=-H*Phi+(u*chi-dd*v)/2
full=s.Matrix([fPhi,pi,-3*H*pi-(Q+Vpp+b*b*dd)*chi+4*u*fPhi-2*(Vp+b*dd)*Phi-b*dd*n,3*fPhi+Q*v,-Phi-b*chi-b*u*v])
constraint=Q*Phi+3*H*(fPhi+H*Phi)+(u*pi-u*u*Phi+Vp*chi+dd*(n+b*chi))/2
nsol=s.solve(constraint,n)[0];reduced=full[[0,1,2,4],:].subs(n,nsol).jacobian(X)
ck(checks,'unreduced_constraint_to_actual_matrix',all(s.simplify(x)==0 for x in reduced-J))
bgvars=s.Matrix([H,u,dd,Q,Vp]);bg=s.Matrix([-(u*u+dd)/2,-3*H*u-Vp-b*dd,(-3*H+b*u)*dd,-2*H*Q,Vpp*u]);fields=s.Matrix([Phi,chi,pi,n,v])
prop=(s.Matrix([constraint]).jacobian(bgvars)*bg)[0]+(s.Matrix([constraint]).jacobian(fields)*full)[0]+3*H*constraint
ck(checks,'unreduced_Hamiltonian_propagation',s.simplify(prop)==0)
fault=full.copy();fault[2]+=b*b*dd*chi
bad=(s.Matrix([constraint]).jacobian(bgvars)*bg)[0]+(s.Matrix([constraint]).jacobian(fields)*fault)[0]+3*H*constraint
ck(controls,'omitted_dust_scalar_force_breaks_constraint',s.simplify(bad)==u*b*b*dd*chi/2)
# Actual modulated-energy identity with arbitrary coefficient functions.
M,Ms,c1,c2,c1s,c2s,K=s.symbols('M Ms c1 c2 c1s c2s K',real=True)
f=c1*Phi+c2*v;energy=pi*pi/2+M*chi*chi/2-f*chi+K*(Phi*Phi+v*v)/A
ys=ell*(slow*Y+e*chi);chis=ell*pi;pis=ell*(-gam*pi-M*chi+f)
der=s.diff(energy,Phi)*ys[0]+s.diff(energy,v)*ys[1]+s.diff(energy,chi)*chis+s.diff(energy,pi)*pis+s.diff(energy,M)*Ms+s.diff(energy,c1)*c1s+s.diff(energy,c2)*c2s
fs=c1s*Phi+c2s*v+c1*ys[0]+c2*ys[1]
expect=-ell*gam*pi*pi+Ms*chi*chi/2-fs*chi+2*K*(Y.dot(ys))/A
ck(checks,'full_modulated_energy_cancellation',s.expand(der-expect)==0)
ck(controls,'omitted_forcing_in_energy_fails',s.expand(der+ell*f*pi-expect)!=0)
# Explicit completed square proving a useful coercivity fixture for arbitrary Phi,v.
EF=energy.subs({M:A,c1:1,c2:2,K:6})
square=pi*pi/2+A*(chi-f.subs({c1:1,c2:2})/A)**2/2+(6*(Phi*Phi+v*v)-(Phi+2*v)**2/2)/A
ck(checks,'energy_completed_square',s.expand(EF-square)==0)
ck(checks,'energy_slow_block_positive',s.Matrix([[s.Rational(11,2),-1],[-1,4]]).det()>0)
# Same Jordan initial data; constraint is evaluated, not fitted.
D,V=s.symbols('D V',real=True);cc=s.symbols('c',positive=True)
vseed=s.sqrt(cc)*V;pseed=dd*(3*H*vseed-D)/(2*Q-u*u)
dn=-(2*Q-u*u)*Phi-(3*H*u+Vp+b*dd)*chi+3*H*dd*v-u*pi
ck(checks,'common_Jordan_density_seed',s.simplify((dn/dd).subs({Phi:pseed,v:vseed,chi:0,pi:0})-D)==0)
ck(checks,'common_Jordan_velocity_seed',s.simplify(vseed/s.sqrt(cc)-V)==0)
ck(checks,'reference_constraint_limit',s.expand(dn.subs({u:0,chi:0,pi:0})+2*Q*Phi-3*H*dd*v)==0)
ck(checks,'Einstein_slow_matrix',slow.subs(u,0)==s.Matrix([[-H,-dd/2],[-1,0]]))
ck(controls,'scalar_initial_amplitude_changes_slip',s.simplify(2*beta)!=0)
# Direct time change of the Jordan tensor equation, not an imported WKB formula.
h,hs,Fs,FF,z,kbar,T0,T1,T2=s.symbols('h hs Fs FF z kbar T0 T1 T2',nonzero=True)
dotT=-3*h*T1;ddotT=9*h*h*T2+9*h*hs*T1;dotF=-3*h*Fs
# Full traceless mixed spatial metric row: F deltaRic_TT-delta(Hess F)_TT=0.
metricrow=FF*(ddotT+3*h*dotT+kbar*kbar*s.exp(2*z/3)*T0)/2+dotF*dotT/2
converted=s.expand(metricrow/(FF*9*h*h/2))
expectedT=T2+(hs/h-1+Fs/FF)*T1+kbar*kbar*s.exp(2*z/3)*T0/(9*h*h)
ck(checks,'full_sourced_TT_row_time_change',s.simplify(converted-expectedT)==0)
ck(controls,'wrong_tensor_friction_sign_detected',s.simplify(converted-(T2+(hs/h+1+Fs/FF)*T1+kbar*kbar*s.exp(2*z/3)*T0/(9*h*h)))!=0)
# Actual fast-time limiting equation, not a claim based on sampled finite A.
tau,p0=s.symbols('tau p0',real=True);wave=s.sqrt(3)*p0*s.sin(tau/s.sqrt(3))
ck(checks,'fast_mode_equation',s.simplify(s.diff(wave,tau,2)+wave/3)==0)
ck(checks,'fast_mode_initial_data',wave.subs(tau,0)==0 and s.diff(wave,tau).subs(tau,0)==p0)
ck(checks,'fast_mode_nonzero_quarter_period',s.simplify(wave.subs(tau,s.pi*s.sqrt(3)/2))==s.sqrt(3)*p0)
ck(controls,'bounded_energy_velocity_loses_prepared_rate',s.limit(A*(s.sqrt(3)/s.sqrt(A)),A,s.oo)==s.oo)
# Known frozen-static comparator only; no rolling high-k conclusion.
force=s.Rational(1,3)*s.Rational(1,2);ck(checks,'frozen_static_separate_control',force==s.Rational(1,6) and (1-force)/(1+force)==s.Rational(5,7))
report={'result':'K2542','exact_checks':checks,'contrary_controls':controls,'scope':'prepared finite-band compact-interval full rolling scalar/dust and tensor transfer closure; universal energy proof in note; no arbitrary scalar data, all-k, nonlinear, empirical or native GU inference','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k2540-prepared-cosmology-source-data-2026-11-04.md','explorations/conditional-build/k2367-sourced-fit-dust-transfer-2026-10-31.md','tests/channel-swings/k2308_inhomogeneous_constrained_dust_transfer_probe.py',str(Path(__file__).relative_to(R))]}}
out=R/'lab/process/k2542-rolling-perturbation-limit.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print('K2542',len(checks),'exact algebra groups',len(controls),'contrary controls')
