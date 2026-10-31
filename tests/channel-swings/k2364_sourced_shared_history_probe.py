"""Actual fixed-coefficient conserved-fluid continuation and independent source tangent."""
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import sympy as S
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];st='k2364-sourced-shared-history';checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
A,B,U0,P0=55.85236076,929.86045772,2.,.4885325972
F0=12*U0**(1/3)*(U0-P0)+A;h0=U0**(2/3);norm=3*F0*h0*h0
smax=3*np.log(3.33);zs=np.array([.01,.1,.5,1.,2.,2.33]);ss=3*np.log1p(zs)
def rhs(s,y,od,orr,lam=1.,tangent=False,force_factor=2.):
 u,p,chi=y[:3];qbar=norm*(od*np.exp(s)+orr*np.exp(4*s/3));q=lam*qbar
 ret=[p,p-A/(36*u**(1/3))+(B+force_factor*q)/(216*u**(5/3)),np.exp(s/3)/(3*u**(2/3))]
 if tangent:
  v,w,c=y[3:];ret += [w,w+(A/(108*u**(4/3))-5*(B+2*q)/(648*u**(8/3)))*v+qbar/(108*u**(5/3)),-2*np.exp(s/3)*v/(9*u**(5/3))]
 return ret
def fval(y):
 u,p=y[:2];return 12*u**(1/3)*(u-p)+A
def solve(od,orr,lam=1.,tol=2e-11,method='DOP853',tangent=False,force_factor=2.):
 event=lambda s,y:fval(y);event.terminal=False;event.direction=0
 sol=solve_ivp(lambda s,y:rhs(s,y,od,orr,lam,tangent,force_factor),(0,smax),[U0,P0,0]+([0,0,0] if tangent else []),rtol=tol,atol=tol*.01,method=method,dense_output=True,events=event)
 if not sol.success:raise RuntimeError(sol.message)
 return sol
u,p,alpha,rho,q,omega=S.symbols('u p alpha rho q omega',positive=True)
F=12*u**S.Rational(1,3)*(u-p)+alpha;force=p-alpha/(36*u**S.Rational(1,3))+(rho+2*q)/(216*u**S.Rational(5,3))
Fs=S.diff(F,u)*p+S.diff(F,p)*force;hv=u**S.Rational(2,3)
check('exact_full00',S.simplify(3*F*hv**2-q-(F-alpha)**2/4-rho/2-9*hv**2*Fs)==0)
check('exact_delta_beta',S.simplify((-3*(Fs-Fs.subs(q,0))/F).subs(q,3*F*hv**2*omega)-omega)==0)
# At s=0, d/dz=3d/ds and h_s unchanged; delta h_zz=9*h_U*delta p_s.
check('exact_h_second_derivative',S.simplify(9*S.diff(hv,u)*q/(108*u**S.Rational(5,3))-q/(18*u*u))==0)
check('exact_distance_cubic',S.simplify(-q/(18*u*u)/(6*hv**2)+q/(108*u**S.Rational(10,3)))==0)
check('exact_force_U_tangent',S.simplify(S.diff(force,u)-(alpha/(108*u**S.Rational(4,3))-5*(rho+2*q)/(648*u**S.Rational(8,3))))==0)
check('exact_F_tangent',S.simplify(S.diff(F,u)-4*(4*u-p)*u**S.Rational(-2,3))==0)
vac=solve(0,0);vbase=vac.sol(ss);details=[];maxdiff=0.
for od,orr in [(0.,0.),(.01,0.),(.1,0.),(.3,0.),(.3,.0001)]:
 sol=solve(od,orr,tangent=True);fine=solve(od,orr,tol=2e-13,tangent=True);ind=solve(od,orr,tol=2e-12,method='RK45',tangent=True)
 y=sol.sol(ss);yy=fine.sol(ss);yyy=ind.sol(ss);err=float(max(np.max(abs(y-yy)),np.max(abs(y-yyy))));maxdiff=max(maxdiff,err);check(f'independent_convergence_{od}_{orr}',err<2e-6)
 U,P,chi=y[:3];f=fval(y);hh=U**(2/3)
 qv=norm*(od*np.exp(ss)+orr*np.exp(4*ss/3));ps=np.array([rhs(s,y[:,i],od,orr,tangent=True)[1] for i,s in enumerate(ss)])
 fs=4*(4*U-P)*U**(-2/3)*P-12*U**(1/3)*ps
 res=3*f*hh*hh-qv-(f-A)**2/4-B/2-9*hh*hh*fs
 check(f'full00_numeric_{od}_{orr}',np.max(abs(res))/(1+np.max(abs(qv))+np.max(abs(3*f*hh*hh)))<2e-13)
 eps=2e-4;yp=solve(od,orr,lam=1+eps,tol=2e-13).sol(ss);ym=solve(od,orr,lam=1-eps,tol=2e-13).sol(ss);fd=(yp-ym)/(2*eps);terr=float(np.max(abs(fd-y[3:])));check(f'tangent_difference_{od}_{orr}',terr<2e-5)
 ps0=rhs(0,[U0,P0,0],od,orr)[1];psv=rhs(0,[U0,P0,0],0,0)[1];fs0=4*(4*U0-P0)*U0**(-2/3)*P0-12*U0**(1/3)*ps0;fsv=4*(4*U0-P0)*U0**(-2/3)*P0-12*U0**(1/3)*psv;check(f'present_beta_shift_{od}_{orr}',abs(-3*(fs0-fsv)/F0-od-orr)<1e-14)
 details.append(dict(Omega_d=od,Omega_r=orr,beta0=float(-3*fs0/F0),F_endpoint=float(f[-1]),F_crossings_z=[float(np.expm1(t/3)) for t in sol.t_events[0]],h=hh.tolist(),chi=chi.tolist(),relative_distance_change=(chi/vbase[2]-1).tolist(),source_tangent_chi=y[5].tolist(),tangent_max_difference=terr,integrator_max_difference=err))
# Exact local expansion tested independently at a finite sequence, not claimed interval certificate.
mat=solve(.3,0,tol=3e-14);vacfine=solve(0,0,tol=3e-14);small=np.array([.01,.005,.002]);sm=3*np.log1p(small);delta=mat.sol(sm)[2]-vacfine.sol(sm)[2];coef=-F0*.3/(36*U0*U0);rat=delta/(coef*small**3)
check('local_cubic_convergence',abs(rat[-1]-1)<.01 and abs(rat[-1]-1)<abs(rat[0]-1))
wrong=solve(.3,0,force_factor=0).sol(ss);good=mat.sol(ss);faults['omit_source_force']=['sourced_distance'] if np.max(abs(wrong[2]-good[2]))>1e-4 else []
rad=solve(.3,.0001).sol(ss);dust=solve(.3,0).sol(ss);faults['omit_tracefree_radiation']=['sourced_distance'] if np.max(abs(rad[2]-dust[2]))>1e-7 else []
# Flip source tangent forcing; actual derivative oracle is nonzero.
faults['zero_source_tangent']=['tangent_difference_0.3_0.0'] if max(abs(v) for v in details[3]['source_tangent_chi'])>1e-4 else []
faults['freeze_scalar_velocity']=['exact_delta_beta'] if abs(details[3]['beta0']-details[0]['beta0'])>.29 else []
assert all(faults.values())
# Consume the same released covariance operators as K2358, profiling only their original intercept/ruler.
import argparse
from scipy.linalg import solve_triangular
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--data-dir',type=Path,required=True);args=parser.parse_args()
input_hashes={'data.dat':'1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8','covariance.cov':'abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc'}
for fn,digest in input_hashes.items():check('release_hash_'+fn,hashlib.sha256((args.data_dir/fn).read_bytes()).hexdigest()==digest)
cat=np.genfromtxt(args.data_dir/'data.dat',names=True,dtype=None,encoding='utf8');raw=np.loadtxt(args.data_dir/'covariance.cov');nn=int(raw[0]);idx=np.flatnonzero(cat['zHD']>.01);cat=cat[idx];C=raw[1:].reshape(nn,nn)[np.ix_(idx,idx)];L=np.linalg.cholesky(C);white=lambda v:solve_triangular(L,v,lower=True);one=white(np.ones(len(cat)));wy=white(cat['m_b_corr']);den=one@one
source=json.loads((R/'lab/process/k2277-multibin-pure-r2-test.json').read_text())['source_inputs']
for i,f in enumerate(source['files']):check('BAO_source_hash_'+str(i),hashlib.sha256(f['text'].encode()).hexdigest()==f['sha256'])
rows=[l.split() for l in source['files'][0]['text'].splitlines() if l and not l.startswith('#')];bz=np.array([float(row[0]) for row in rows]);by=np.array([float(row[1]) for row in rows]);bc=np.array([[float(v) for v in l.split()] for l in source['files'][1]['text'].splitlines()]);bl=np.linalg.cholesky(bc);bw=lambda v:solve_triangular(bl,v,lower=True);bwy=bw(by)
check('released_counts',len(cat)==1590 and len(rows)==13);check('data_inside_solved_interval',max(cat['zHD'].max(),bz.max())<=2.33)
def likelihood(od,orr,method='DOP853',tol=2e-11):
 sol=solve(od,orr,method=method,tol=tol);sn=sol.sol(3*np.log1p(cat['zHD']));f=5*np.log10((1+cat['zHEL'])*sn[2]);sr=wy-white(f);sr-=one*(one@sr)/den
 u,p,m=sol.sol(3*np.log1p(bz));bf=np.array([{'DM_over_rs':mm,'DH_over_rs':uu**(-2/3),'DV_over_rs':(zz*mm*mm*uu**(-2/3))**(1/3)}[row[2]] for uu,mm,zz,row in zip(u,m,bz,rows)]);br=bw(bf);lam=float(br@bwy/(br@br));rr=bwy-lam*br
 return dict(SN_chi2=float(sr@sr),BAO_chi2=float(rr@rr),ruler=lam)
for item in details:
 od,orr=item['Omega_d'],item['Omega_r'];item['fixed_shape_likelihood']=likelihood(od,orr);other=likelihood(od,orr,'RK45',2e-12);check(f'likelihood_convergence_{od}_{orr}',max(abs(item['fixed_shape_likelihood'][k]-other[k]) for k in other)<2e-4)
check('prior_vacuum_likelihood_reproduced',abs(details[0]['fixed_shape_likelihood']['SN_chi2']-1402.46614609)<2e-4 and abs(details[0]['fixed_shape_likelihood']['BAO_chi2']-7.00625354)<2e-4)
check('dust_fixed_shape_changes_likelihood',details[3]['fixed_shape_likelihood']['SN_chi2']>details[0]['fixed_shape_likelihood']['SN_chi2']+10)

# Replay rounded existence witnesses from two-start Nelder-Mead search, not an optimality certificate.
original=(A,B,U0,P0,F0,norm)
refits=[]
for label,aa,bb,pp,seed,nfev in [
 ('near_zero_rho_basin',69.86241292,2.175269709e-9,.895216134,[55.85236076,929.86045772,.4885325972],567),
 ('better_interior_witness',775.88047141,8540.41820373,.3175541986,[200.,2000.,.7],332)]:
 A,B,P0=aa,bb,pp;F0=12*U0**(1/3)*(U0-P0)+A
 check('refit_positive_coefficients_and_F0_'+label,A>0 and B>0 and F0>0)
 norm=3*F0*h0*h0 # fixed TODAY normalization for each candidate; physical density changes.
 sol=solve(.3,0,tol=2e-13);ind=solve(.3,0,tol=2e-12,method='RK45');grid=np.linspace(0,smax,1001);y=sol.sol(grid);other=ind.sol(grid)
 err=float(np.max(abs(y-other)));check('refit_independent_state_'+label,err<2e-7)
 fv=fval(y);check('refit_numerical_domain_'+label,np.min(y[0])>0 and np.min(fv)>0 and not len(sol.t_events[0]))
 U,P,chi=y;hh=U**(2/3);qv=norm*.3*np.exp(grid);ps=np.array([rhs(s,y[:,i],.3,0)[1] for i,s in enumerate(grid)]);fs=4*(4*U-P)*U**(-2/3)*P-12*U**(1/3)*ps
 residual=3*fv*hh*hh-qv-(fv-A)**2/4-B/2-9*hh*hh*fs;scaled=float(np.max(abs(residual))/(1+np.max(abs(qv))+np.max(abs(3*fv*hh*hh))))
 check('refit_full00_'+label,scaled<2e-13)
 fit=likelihood(.3,0,tol=2e-13);indfit=likelihood(.3,0,method='RK45',tol=2e-12)
 check('refit_independent_likelihood_'+label,max(abs(fit[k]-indfit[k]) for k in fit)<2e-4)
 refits.append(dict(label=label,parameters=[A,B,U0,P0],seed=seed,search_nfev=nfev,F0=F0,q_d0=norm*.3,numerical_U_min=float(np.min(U)),numerical_F_min=float(np.min(fv)),F_endpoint=float(fv[-1]),F_crossings_z=[float(np.expm1(v/3)) for v in sol.t_events[0]],domain_grid_nodes=len(grid),integrator_max_difference=err,full00_scaled_residual=scaled,likelihood=fit))
check('sourced_refit_repairs_fixed_parameter_BAO',refits[1]['likelihood']['BAO_chi2']<11 and refits[1]['likelihood']['SN_chi2']<1410)
A,B,U0,P0,F0,norm=original

deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2277-multibin-pure-r2-test.json','lab/process/k2292-conserved-matter-cosmology.json','lab/process/k2358-shared-history-supernova-test.json','lab/process/k2361-shared-history-dynamics-and-matter.json']
out=dict(result_id='K2364',checks=len(checks),check_names=list(checks),altered_input_and_algebraic_scope_controls=faults,evidence_kind='six symbolic identities plus finite double-precision trajectory/convergence/tangent controls; local Taylor proof in note; two changed-source solves and two algebraic scope controls, no interval F or observational fit certificate',details=dict(parameters=[A,B,U0,P0],F0=F0,source_normalization=norm,redshifts=zs.tolist(),trajectories=details,local_cubic_coefficient=coef,local_cubic_ratios=rat.tolist(),max_integrator_difference=maxdiff,external_input_sha256=input_hashes,sourced_refit_witnesses=refits,refit_search=dict(method="Nelder-Mead",coordinates="log(alpha), log(rho), p0; U0=2; Omega_d=.3; Omega_r=0",objective="SN_chi2+BAO_chi2 with original intercept and ruler profiled",bounds="alpha,rho>0 via logs; p0 unrestricted; reject F0<=0, failed integration or nonpositive endpoint F",rtol=2e-9,maxiter=3000,xatol=1e-8,fatol=1e-7,scope="two numerical starts; replay rounded witnesses; no global optimum, physical-density calibration, or held-out prediction")),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:
 saved=json.loads(p.read_text());assert saved['dependencies']==out['dependencies']
 def eq(a,b):
  if isinstance(a,dict):return a.keys()==b.keys() and all(eq(a[k],b[k]) for k in a)
  if isinstance(a,list):return len(a)==len(b) and all(eq(x,y) for x,y in zip(a,b))
  if isinstance(a,float):return abs(a-b)<1e-8*max(1,abs(a))
  return a==b
 assert eq(saved,out)
print('PASS',len(checks),len(faults));print(json.dumps(out['details'],indent=2))
