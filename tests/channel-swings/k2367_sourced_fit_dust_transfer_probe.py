"""Same fitted sourced background, exact constrained dust matrix, numerical transfer."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
import sympy as S
from scipy.integrate import solve_ivp
R=Path(__file__).resolve().parents[2];st='k2367-sourced-fit-dust-transfer';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('ineffective control '+k)
alpha,rho,U0,p0,Om,lam=775.88047141,8540.41820373,2.,.3175541986,.3,48.4745294
F0=alpha+12*U0**(1/3)*(U0-p0);h0=U0**(2/3);q0=3*F0*h0*h0*Om;end=3*np.log(3.33);b=-1/np.sqrt(6)
# Differentiate explicit conformal background independently of Einstein field equations.
s,u,p=S.symbols('s U p',real=True);a0,r0,f0,q00=S.symbols('alpha rho F0 q0',positive=True)
f=a0+12*u**S.Rational(1,3)*(u-p);h=u**S.Rational(2,3);q=q00*S.exp(s);force=p-a0/(36*u**S.Rational(1,3))+(r0+2*q)/(216*u**S.Rational(5,3))
def ds(z):return S.diff(z,s)+S.diff(z,u)*p+S.diff(z,p)*force
fs=ds(f);run=-3*fs/f;c=f/f0;dt=-S.sqrt(c)/(3*h);ae=S.exp(-s/3)*S.sqrt(c);he=h*(1+run/2)/S.sqrt(c);uu=S.sqrt(S.Rational(3,2))*h*run/S.sqrt(c);dd=q*f0/f**2
vv=f0/S.Integer(4)*(1-2*a0/f+(a0*a0+2*r0)/f**2);vp=f0/S.sqrt(6)*(a0/f-(a0*a0+2*r0)/f**2);vpp=f0/3*(-a0/f+2*(a0*a0+2*r0)/f**2)
expr=[ae,he,uu,dd,vv,vp,vpp,dt,f,ds(he)/dt,ds(uu)/dt,ds(dd)/dt]
bgf=S.lambdify((s,u,p,a0,r0,f0,q00),expr,'numpy',cse=True)
def rhs(t,y):
 U,P=y
 return [P,P-alpha/(36*U**(1/3))+(rho+2*q0*np.exp(t))/(216*U**(5/3))]
def solvebg(method,tol):return solve_ivp(rhs,(0,end),[U0,p0],method=method,rtol=tol,atol=tol*.01,dense_output=True)
bg=solvebg('DOP853',2e-13);bgi=solvebg('RK45',2e-12);check('background_integrators_success',bg.success and bgi.success)
grid=np.linspace(0,end,257);check('independent_background',np.max(abs(bg.sol(grid)-bgi.sol(grid)))<2e-8)
def back(t,sol=bg):return np.array(bgf(t,*sol.sol(t),alpha,rho,F0,q0),dtype=float)
vals=np.array([back(t) for t in grid]);ae0,H,us,d,V,V1,V2,ts,F,Hd,ud,ddot=vals.T
check('sampled_domain',min(F)>0 and np.min(bg.sol(grid)[0])>0)
errors={'friedmann':np.max(abs(3*H*H-us*us/2-V-d)), 'acceleration':np.max(abs(Hd+(us*us+d)/2)), 'scalar':np.max(abs(ud+3*H*us+V1+b*d)), 'dust':np.max(abs(ddot-(-3*H+b*us)*d))}
for k,v in errors.items():check('background_'+k,v<2e-9)
control('omit_F0_in_density',abs(3*H[0]**2-us[0]**2/2-V[0]-d[0]/F0)>1)
control('wrong_dust_coupling_sign',max(abs(ud+3*H*us+V1-b*d))>1)
# Independent symbolic original-system constraint and reduced trace.
HH,UU,DD,Q,VP,VPP,B=S.symbols('H u d Q Vp Vpp b');PH,CH,PI,VE,NN=S.symbols('Phi chi pi v n')
P=-HH*PH+(UU*CH-DD*VE)/2
pid=-3*HH*PI-(Q+VPP+B*B*DD)*CH+4*UU*P-2*(VP+B*DD)*PH-B*DD*NN
nd=3*P+Q*VE;vd=-PH-B*CH-B*UU*VE
C=Q*PH+3*HH*(P+HH*PH)+(UU*PI-UU*UU*PH+VP*CH+DD*(NN+B*CH))/2
Ds={HH:-(UU*UU+DD)/2,UU:-3*HH*UU-VP-B*DD,DD:(-3*HH+B*UU)*DD,Q:-2*HH*Q,VP:VPP*UU,PH:P,CH:PI,PI:pid,VE:vd,NN:nd}
cd=sum(S.diff(C,k)*v for k,v in Ds.items());check('exact_constraint_propagation',S.expand(cd+3*HH*C)==0)
mutated_cd=cd+S.diff(C,PI)*B*B*DD*CH
control('omitted_force_fails_same_constraint',S.expand(mutated_cd+3*HH*C)==UU*B*B*DD*CH/2 and S.expand(mutated_cd+3*HH*C)!=0)
ns=(-(2*Q-UU*UU)*PH-(3*HH*UU+VP+B*DD)*CH+3*HH*DD*VE-UU*PI)/DD
reds=[P,PI,S.expand(pid.subs(NN,ns)),vd];J=S.Matrix(reds).jacobian([PH,CH,PI,VE]);check('exact_reduced_trace',S.simplify(S.trace(J)+4*HH)==0)
check('exact_number_reconstruction',S.expand(C.subs(NN,ns))==0)
check('exact_reconstructed_number_evolution',S.simplify(sum(S.diff(ns,k)*v.subs(NN,ns) if hasattr(v,'subs') else S.diff(ns,k)*v for k,v in Ds.items() if k!=NN)-nd.subs(NN,ns))==0)
Jf=S.lambdify((HH,UU,DD,Q,VP,VPP,B),J,'numpy')
def matrix(t,k,sol=bg,wrong=False):
 a,H,u,d,V,Vp,Vpp,dt,F,*_=back(t,sol);Q=k*k/a**2
 j=np.array(Jf(H,u,d,Q,Vp,Vpp,b),float)
 if wrong:j[2,1]+=b*b*d # actually omit beta²d from the original scalar equation
 return j,dt

def evolve(k,method='DOP853',tol=2e-10,sol=bg,wrong=False):
 def rhs(t,y):
  j,dt=matrix(t,k,sol,wrong);return (dt*j@y.reshape(4,4)).ravel()
 z=solve_ivp(rhs,(end,0),np.eye(4).ravel(),method=method,rtol=tol,atol=tol*.01,dense_output=True)
 check(f'transfer_success_{k}_{method}_{wrong}',z.success);return z

def readout(t,k,x):
 a,H,u,d,V,Vp,Vpp,dt,F,*_=back(t);Q=k*k/a**2;ph,ch,pi,v=x
 n=(-(2*Q-u*u)*ph-(3*H*u+Vp+b*d)*ch+3*H*d*v-u*pi)/d
 return np.array([n-3*b*ch,2*ph,2*b*ch])
results=[]
for kap in [.1,1.,10.]:
 k=lam*kap;z=evolve(k);zi=evolve(k,'RK45',2e-11,bgi);T=z.y[:,-1].reshape(4,4);Ti=zi.y[:,-1].reshape(4,4)
 err=float(np.max(abs(T-Ti))/max(1,np.max(abs(T))))
 check('independent_transfer_'+str(kap),err<2e-7)
 determinant=float(np.linalg.det(T));expected=back(end)[0]**4
 check('Liouville_determinant_'+str(kap),abs(determinant/expected-1)<2e-7)
 a,H,u,d,V,Vp,Vpp,dt,F,*_=back(end);Q=k*k/a**2;den=2*Q-u*u;check('seed_chart_'+str(kap),abs(den)>1e-6)
 seeds=[]
 for label,nj,vel in [('density',1.,0.),('velocity',0.,1/np.sqrt(Q))]:
  x=np.array([d*(3*H*vel-nj)/den,0.,0.,vel]);check('initial_readout_'+str(kap)+label,abs(readout(end,k,x)[0]-nj)<1e-9)
  obs=readout(0,k,T@x);obsi=readout(0,k,Ti@x)
  check('independent_readout_'+str(kap)+label,np.max(abs(obs-obsi))/max(1,np.max(abs(obs)))<2e-7)
  seeds.append(dict(label=label,initial=x.tolist(),today_density_lensing_slip=obs.tolist(),initial_unit_velocity=vel))
 density=np.array(seeds[0]['today_density_lensing_slip']);velocity=np.array(seeds[1]['today_density_lensing_slip']);eta=-density[0]/velocity[0]
 cancelled=density+eta*velocity;check('same_initial_density_different_response_'+str(kap),abs(cancelled[0])<1e-12 and np.max(abs(cancelled[1:]))>1e-12)
 wrong=evolve(k,wrong=True);Tw=wrong.y[:,-1].reshape(4,4)
 delta=float(np.max(abs(Tw-T)));control('omitted_scalar_dust_force_changes_transfer_'+str(kap),delta>1e-5)
 results.append(dict(k_rd=kap,k_over_Hstar=k,transfer=T.tolist(),singular_values=np.linalg.svd(T,compute_uv=False).tolist(),determinant=determinant,determinant_expected=expected,relative_independent_error=err,seeds=seeds,wrong_force_transfer_max_difference=delta,cancelling_velocity_seed_coefficient=float(eta),cancelled_today_density_lensing_slip=cancelled.tolist()))
deps=['lab/process/k2364-sourced-shared-history.json','explorations/conditional-build/k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md','tests/channel-swings/k2308_inhomogeneous_constrained_dust_transfer_probe.py',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2367',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='symbolic exact constraint/reduction identities plus finite double-precision same-fit transfers and independent integrator checks; no interval domain, physical covariance or stability certificate',details=dict(parameters=dict(alpha=alpha,rho=rho,U0=U0,p0=p0,Omega=Om,ruler=lam,F0=F0),background_max_residuals=errors,numerical_F_min=float(min(vals[:,8])),background_today=vals[0].tolist(),trace_mass_times_ruler=float(np.sqrt(alpha/3)/lam),normalized_density_times_ruler_squared=float(3*Om*(h0/lam)**2),transfers=results),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:
 saved=json.loads(p.read_text());check('saved_dependency_hashes',saved['dependencies']==out['dependencies'])
 def eq(a,b):
  if isinstance(a,dict):return a.keys()==b.keys() and all(eq(a[k],b[k]) for k in a)
  if isinstance(a,list):return len(a)==len(b) and all(eq(x,y) for x,y in zip(a,b))
  if isinstance(a,float):return abs(a-b)<2e-7*max(1,abs(a))
  return a==b
 assert eq(saved,out)
print('PASS',out['checks'],len(controls));print(json.dumps(out['details'],indent=2))
