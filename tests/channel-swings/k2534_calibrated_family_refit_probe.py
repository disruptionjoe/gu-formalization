"""Joint calibrated SN/BAO shape witnesses; exact profiles, numerical search/replay.

No extra SH0ES prior; independent BAO ruler; drift is held out and hypothetical.
"""
from pathlib import Path
import argparse,json,hashlib,sys,warnings
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import solve_triangular
from scipy.optimize import minimize
import sympy as sp
R=Path(__file__).resolve().parents[2];parser=argparse.ArgumentParser();parser.add_argument('--data-dir',type=Path,required=True);parser.add_argument('--write',action='store_true');parser.add_argument('--search',action='store_true');args=parser.parse_args()
exact={};numeric={};controls={}
def ck(bank,name,value):
 bank[name]=bool(value)
 if not value:raise AssertionError(name)
hashes={'data.dat':'1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8','covariance.cov':'abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc'}
for fn,d in hashes.items():ck(numeric,'release_'+fn,hashlib.sha256((args.data_dir/fn).read_bytes()).hexdigest()==d)
cat=np.genfromtxt(args.data_dir/'data.dat',names=True,dtype=None,encoding='utf8');raw=np.loadtxt(args.data_dir/'covariance.cov');nn=int(raw[0]);idx=np.flatnonzero((cat['zHD']>.01)|cat['IS_CALIBRATOR'].astype(bool));cat=cat[idx];Craw=raw[1:].reshape(nn,nn)[np.ix_(idx,idx)];C=(Craw+Craw.T)/2;L=np.linalg.cholesky(C);white=lambda v:solve_triangular(L,v,lower=True,check_finite=False)
cal=cat['IS_CALIBRATOR'].astype(bool);nc=~cal;B=np.column_stack([np.ones(len(cat)),nc.astype(float)]);Bw=white(B);normal=Bw.T@Bw
ck(numeric,'joint_rows',len(cat)==1657 and int(cal.sum())==77);ck(numeric,'rounded_covariance',np.max(abs(Craw-Craw.T))<=3.1e-8)
source=json.loads((R/'lab/process/k2277-multibin-pure-r2-test.json').read_text())['source_inputs']
for i,f in enumerate(source['files']):ck(numeric,'BAO_release_'+str(i),hashlib.sha256(f['text'].encode()).hexdigest()==f['sha256'])
rows=[l.split() for l in source['files'][0]['text'].splitlines() if l and not l.startswith('#')];bz=np.array([float(r[0]) for r in rows]);by=np.array([float(r[1]) for r in rows]);bc=np.array([[float(v) for v in l.split()] for l in source['files'][1]['text'].splitlines()]);bl=np.linalg.cholesky(bc);bw=lambda v:solve_triangular(bl,v,lower=True,check_finite=False);bwy=bw(by)
U0=2.;h0=U0**(2/3);omega=.3;end=3*np.log1p(2.33);sn_s=3*np.log1p(cat['zHD'][nc]);bs=3*np.log1p(bz)
def solve(par,method='DOP853',tol=2e-10,zmax=2.33):
 alpha,rho,p0=par;F0=alpha+12*U0**(1/3)*(U0-p0);q0=3*F0*h0*h0*omega
 if alpha<=0 or rho<0 or F0<=0:return None
 def rhs(s,y):
  u,p=y[:2]
  if u<=0:return [0,0,0]
  return [p,p-alpha/(36*u**(1/3))+(rho+2*q0*np.exp(s))/(216*u**(5/3)),np.exp(s/3)/(3*u**(2/3))]
 def event(s,y):return min(y[0],alpha+12*max(y[0],0)**(1/3)*(y[0]-y[1]))
 event.terminal=True;event.direction=-1
 final=3*np.log1p(zmax)
 sol=solve_ivp(rhs,(0,final),[U0,p0,0.],method=method,rtol=tol,atol=tol*.01,dense_output=True,events=event,max_step=.1)
 if not sol.success or sol.t[-1]!=final:return None
 return sol

def likelihood(par,method='DOP853',tol=2e-10,zmax=2.33):
 sol=solve(par,method,tol,zmax)
 if sol is None:return None
 base=cat['CEPH_DIST'].astype(float).copy();chi=sol.sol(sn_s)[2]
 if np.any(chi<=0):return None
 base[nc]=5*np.log10(299792.458/70*(1+cat['zHEL'][nc])*h0*chi)+25
 rw=white(cat['m_b_corr']-base);th=np.linalg.solve(normal,Bw.T@rw);rs=rw-Bw@th
 u,p,m=sol.sol(bs);vec=np.array([{'DM_over_rs':mm,'DH_over_rs':uu**(-2/3),'DV_over_rs':(zz*mm*mm*uu**(-2/3))**(1/3)}[r[2]] for uu,mm,zz,r in zip(u,m,bz,rows)])
 v=bw(vec);lam=float(v@bwy/(v@v))
 if lam<=0:return None
 rb=bwy-lam*v;sn=float(rs@rs);bao=float(rb@rb)
 return dict(SN=sn,BAO=bao,total=sn+bao,M=float(th[0]),k=float(th[1]),H0=float(70*10**(-th[1]/5)),ruler=lam),sol,rs,rb,v
# Exact normalization and initial-jet identity, not a uniform Einstein-limit claim.
x,y,a,b,o=sp.symbols('x y a b o',positive=True);force=y-a/(36*x**sp.Rational(1,3))+(b+6*(a+12*(1-y))*o)/(216*x**sp.Rational(5,3))
y0=3*o/4;bjet=6*a*(1-o)-sp.Rational(81,2)*o*o-6*(12-9*o)*o
jet=sp.simplify(force.subs({x:1,y:y0,b:bjet}));s=sp.symbols('s');xref=(o*sp.exp(s)+1-o)**sp.Rational(3,4)
ck(exact,'LCDM_first_jet',sp.diff(xref,s).subs(s,0)==y0);ck(exact,'LCDM_second_jet',sp.simplify(jet-sp.diff(xref,s,2).subs(s,0))==0)
t=sp.symbols('t',positive=True);Rbar=3*o*t+12*(1-o);H2=o*t+1-o
qreq=3*(a+Rbar)*H2-Rbar**2/4-bjet/2-27*H2*o*t
residual=sp.factor(qreq-3*(a+12-9*o)*o*t)
ck(exact,'original_LCDM_row_residual',sp.simplify(residual-(1-t)*(3*(12-9*o)*o+sp.Rational(81,4)*o**2*(1+t)))==0)
ck(controls,'matching_two_jets_not_full_LCDM',residual.subs({t:2,o:sp.Rational(3,10)})!=0)

# Shared profile theorem and planted overfitting control.
X=sp.Matrix([[1,0],[1,0],[1,1],[1,1]]);V=sp.diag(1,2,3,4);Q=sp.eye(4)-X*(X.T*V*X).inv()*X.T*V
ck(exact,'joint_profile_projector',Q*Q==Q and Q*X==sp.zeros(4,2) and Q.T*V==V*Q)
ck(controls,'calibrator_removal_loses_H0',X[2:,:].rank()==1);ck(controls,'rowwise_offsets_erase_data',sp.eye(4)-sp.eye(4)*(sp.eye(4).T*V*sp.eye(4)).inv()*sp.eye(4).T*V==sp.zeros(4))
seeds=[('prior_interior',[775.88047141,8540.41820373,.3175541986]),('prior_boundary',[69.86241292,2.175269709e-9,.895216134]),('large_alpha_second_jet',[1e4,6*1e4*U0**(4/3)*.7-20.385*U0**(8/3),.45])]
outpath=R/'lab/process/k2534-calibrated-family-refit.json'
if args.search:
 witnesses=[]
 for name,seed in seeds:
  def fun(v):
   if abs(v[0])>25 or abs(v[1])>40 or abs(v[2])>20:return 1e12
   par=[float(np.exp(v[0])),float(np.exp(v[1])),float(v[2])]
   try:r=likelihood(par,tol=2e-9)
   except (ValueError,FloatingPointError,OverflowError):return 1e12
   return 1e12 if r is None else r[0]['total']
  opt=minimize(fun,[np.log(seed[0]),np.log(seed[1]),seed[2]],method='Nelder-Mead',options=dict(maxiter=1800,xatol=2e-8,fatol=2e-7))
  par=[float(format(np.exp(opt.x[0]),'.12g')),float(format(np.exp(opt.x[1]),'.12g')),float(format(opt.x[2],'.12g'))]
  witnesses.append(dict(label=name,seed=seed,parameters=par,search_success=bool(opt.success),evaluations=int(opt.nfev),search_message=str(opt.message)))
  print(name,par,fun(opt.x),opt.message,flush=True)
else:witnesses=json.loads(outpath.read_text())['witnesses']
records=[]
for w in witnesses:
 name=w['label'];par=w['parameters'];fit,sol,rs,rb,v=likelihood(par,tol=2e-13);other=likelihood(par,'RK45',2e-12)
 ck(numeric,name+'_independent_observables',all(abs(fit[k]-other[0][k])<3e-4 for k in ['SN','BAO','H0','ruler']))
 ck(numeric,name+'_profile_equations',max(np.max(abs(Bw.T@rs)),abs(v@rb))<1e-7)
 grid=np.linspace(0,end,1001);u,p,chi=sol.sol(grid);alpha,rho,p0=par;F=alpha+12*u**(1/3)*(u-p)
 ck(numeric,name+'_sampled_domain',np.min(u)>0 and np.min(F)>0)
 ck(numeric,name+'_independent_states',np.max(abs(sol.sol(grid)-other[1].sol(grid)))<3e-6)
 q0=3*(alpha+12*U0**(1/3)*(U0-p0))*h0*h0*omega;qv=q0*np.exp(grid)
 ps=p-alpha/(36*u**(1/3))+(rho+2*qv)/(216*u**(5/3));Fs=4*(4*u-p)*u**(-2/3)*p-12*u**(1/3)*ps
 original=3*F*u**(4/3)-qv-(F-alpha)**2/4-rho/2-9*u**(4/3)*Fs
 ck(numeric,name+'_original00_algebraic_residual',np.max(abs(original))/(1+np.max(abs(qv))+np.max(abs(3*F*u**(4/3))))<3e-13)
 fit['r_d_Mpc']=299792.458*h0/(fit['H0']*fit['ruler'])
 extended=likelihood(par,tol=2e-13,zmax=4.5)
 forecast=None
 if extended:
  ext_other=solve(par,'RK45',2e-12,zmax=4.5);assert ext_other is not None
  eg=np.linspace(0,3*np.log(5.5),1501);eu,ep,_=extended[1].sol(eg);ef=par[0]+12*eu**(1/3)*(eu-ep)
  ck(numeric,name+'_extended_independent_states',np.max(abs(extended[1].sol(eg)-ext_other.sol(eg)))<5e-6)
  ck(numeric,name+'_extended_sampled_domain',np.min(eu)>0 and np.min(ef)>0)
  z=np.array([2.,2.5,3.,3.5,4.5]);EE=extended[1].sol(3*np.log1p(z))[0]**(2/3)/h0;A70=29979245800*70/3.0856775814913673e19*20*31557600;d=1-EE/(1+z);yref=A70*(1-np.sqrt(.3*(1+z)**3+.7)/(1+z));sig=1.35*(3000/2370)**-1*(6/30)**-.5*((1+z)/5)**np.where(z<=4,-1.7,-.9);rr=yref-A70*fit['H0']/70*d;ww=1/sig**2;off=np.dot(ww,rr)/sum(ww)
  ck(numeric,name+'_extended_drift_agreement',np.max(abs(A70*fit['H0']/70*(EE-ext_other.sol(3*np.log1p(z))[0]**(2/3)/h0)/(1+z)))<1e-5)
  forecast=dict(z=z.tolist(),drift_cm_s=(A70*fit['H0']/70*d).tolist(),fixed_offset_loss=float(np.dot(ww,rr*rr)),free_offset_loss=float(np.dot(ww,(rr-off)**2)),fitted_offset_cm_s=float(off),scope='held-out hypothetical ANDES mean at LCDM Omega .3 H0=70; calibration shape and H0 frozen, free offset comparison only')
 records.append(dict(label=name,fit=fit,positive_domain_sample=dict(nodes=1001,U_min=float(u.min()),F_min=float(F.min()),F_endpoint=float(F[-1])),held_out_forecast=forecast))
# Explicit large-alpha second-jet sequence, no data refit or convergence theorem.
sequence=[]
for alpha in [1e3,1e4,1e5]:
 par=[alpha,6*alpha*U0**(4/3)*.7-20.385*U0**(8/3),.45];rr=likelihood(par,tol=2e-12)
 if rr:
  ind=solve(par,'RK45',2e-12);assert ind is not None
  sg=np.linspace(0,end,1001);ck(numeric,'alpha_sequence_independent_'+str(alpha),np.max(abs(rr[1].sol(sg)-ind.sol(sg)))<5e-6)
  zg=np.linspace(0,2.33,301);E=rr[1].sol(3*np.log1p(zg))[0]**(2/3)/h0;ref=np.sqrt(.3*(1+zg)**3+.7)
  sequence.append(dict(alpha=alpha,parameters=par,fit=rr[0],max_E_LCDM_difference=float(np.max(abs(E-ref)))))
 else:sequence.append(dict(alpha=alpha,parameters=par,admissible=False))
ck(numeric,'large_alpha_control_attempted',len(sequence)==3)
prior=likelihood(seeds[0][1],tol=2e-13)[0];ck(numeric,'refit_improves_calibrated_start',min(r['fit']['total'] for r in records)<prior['total']-1e-4)
ck(numeric,'prior_SN_replays',abs(prior['SN']-1459.5836)<1e-3)
# Numerical results rounded for cross-process equality; no precision certification.
def clean(v):
 if isinstance(v,float):return float(format(v,'.9g'))
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
 if isinstance(v,list):return [clean(x) for x in v]
 return v
report=clean(dict(result='K2534',exact_checks=exact,numerical_checks=numeric,contrary_controls=controls,witnesses=witnesses,results=records,prior_calibrated_fit=prior,large_alpha_second_jet_sequence=sequence,normalization='U0=2 is redundant after alpha/U0^(4/3),rho/U0^(8/3),p0/U0 normalization; Omega_d=.3 fixed; Omega_r=0',search='three-start numerical Nelder-Mead; log alpha/log rho/p0; safeguard abs logs <=25/40 and abs p0<=20; no global optimality claim',release_hashes=hashes,scope='conditional shared Cepheid/SN and BAO likelihood; independent ruler, fixed matter normalization; no native GU inference or empirical family exclusion',dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['lab/process/k2277-multibin-pure-r2-test.json','lab/process/k2532-finite-drift-forecast.json',str(Path(__file__).relative_to(R))]}))
if args.write:outpath.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:
 saved=json.loads(outpath.read_text())
 def eq(a,b):
  if isinstance(a,dict):return a.keys()==b.keys() and all(eq(a[k],b[k]) for k in a)
  if isinstance(a,list):return len(a)==len(b) and all(eq(x,y) for x,y in zip(a,b))
  if isinstance(a,float):return abs(a-b)<2e-7*max(1,abs(a))
  return a==b
 assert eq(saved,report),'report differs'
print(json.dumps(dict(results=records,large_alpha_sequence=sequence),indent=2));print('K2534',len(exact),'exact',len(numeric),'numerical',len(controls),'controls')
