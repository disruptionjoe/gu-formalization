"""Pinned Pantheon+ fixed-release likelihood diagnostic, not a GU prediction.
Run with --data-dir containing data.dat and covariance.cov from the note.
BLAS thread counts must be one. No network access, no silently diagonal errors.
"""
from pathlib import Path
import argparse, hashlib, json, platform
import numpy as np
import scipy
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize_scalar, brentq
from scipy.special import log_ndtr
R=Path(__file__).resolve().parents[2]
st='k2355-released-supernova-shape'
p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);p.add_argument('--write',action='store_true');args=p.parse_args()
hashes={'data.dat':'1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8','covariance.cov':'abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc','statonly.cov':'9f177129a332735d3637affd20054080d5260815f3ca0809120c05b2c902297f'}
checks={};controls={}
def check(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
def control(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('ineffective changed-input control: '+k)
for f,h in hashes.items():check('pinned_'+f,hashlib.sha256((args.data_dir/f).read_bytes()).hexdigest()==h)
a=np.genfromtxt(args.data_dir/'data.dat',names=True,dtype=None,encoding='utf8');raw=np.loadtxt(args.data_dir/'covariance.cov');n=int(raw[0]);check('full_dimensions',len(a)==n==1701 and len(raw)==1+n*n)
full=raw[1:].reshape(n,n);mask=a['zHD']>.01;ind=np.flatnonzero(mask);a=a[mask];C=full[np.ix_(ind,ind)];y=a['m_b_corr'];z=a['zHD'];zh=a['zHEL'];n=len(y);one=np.ones(n)
check('symmetric_covariance',np.max(np.abs(C-C.T))<1e-12);fac=cho_factor(C,lower=True);check('positive_Cholesky',np.all(np.diag(fac[0])>0));c1=cho_solve(fac,one);den=one@c1
solve=lambda b:cho_solve(fac,b)
def proj(b):return solve(b)-c1*(one@solve(b))/den
def profile(f,yy=y):
 r=yy-f;b=(c1@r)/den;e=r-b;return float(e@solve(e)),float(b)
def shape(om,order=64,red=z):
 nodes,weights=np.polynomial.legendre.leggauss(order);u=red[:,None]*(nodes+1)/2
 chi=red/2*np.sum(weights/np.sqrt(om*(1+u)**3+1-om),axis=1)
 return 5*np.log10((1+zh)*chi)
fds=5*np.log10((1+zh)*z);feds=5*np.log10((1+zh)*2*(1-1/np.sqrt(1+z)))
check('quadrature_endpoint_dS',np.max(abs(shape(0)-fds))<1e-11);check('quadrature_endpoint_EdS',np.max(abs(shape(1)-feds))<1e-11)
opt=minimize_scalar(lambda om:profile(shape(om))[0],bounds=(0,1),method='bounded',options={'xatol':1e-11});om=float(opt.x);qmin,bestb=profile(shape(om));check('fit_converged_interior',opt.success and .05<om<.95)
check('released_LCDM_positive_control',.32<om<.35)
lo=brentq(lambda x:profile(shape(x))[0]-qmin-1,.01,om);hi=brentq(lambda x:profile(shape(x))[0]-qmin-1,om,.99)
check('quadrature_32_64_128_convergence',max(np.max(abs(shape(om,32)-shape(om,64))),np.max(abs(shape(om,128)-shape(om,64))))<1e-10)
q0,b0=profile(fds);q1,b1=profile(feds);v=feds-fds;w=proj(v);D2=float(v@w);T=float(w@(y-(fds+feds)/2));check('fixed_shape_delta_chi_identity',abs(q0-q1-2*T)<1e-7)
check('zero_point_invariance',abs(profile(shape(om),y+7)[0]-qmin)<1e-7 and abs(profile(shape(om),y+7)[1]-bestb-7)<1e-10)
check('intercept_annihilation',abs(w@one)<1e-8)
# Independent reversed-order factorization exercises the full covariance, not a reordered scalar.
ix=np.arange(n)[::-1];Cp=C[np.ix_(ix,ix)];fp=cho_factor(Cp,lower=True);rp=(y-feds)[ix];ones=one[ix];sp=cho_solve(fp,ones);bp=(sp@rp)/(ones@sp);qp=(rp-bp)@cho_solve(fp,rp-bp)
check('joint_row_covariance_permutation',abs(qp-q1)<1e-7)
diag=1/np.diag(C)
def diagonal_profile(f):
 r=y-f;b=(diag@r)/sum(diag);return float((r-b)@(diag*(r-b)))
diagq=diagonal_profile(shape(om));control('replace_full_covariance_by_diagonal',abs(diagq-qmin)>1)
wrong=shape(om,red=zh);wrongq=profile(wrong)[0];control('swap_Hubble_and_heliocentric_redshifts',abs(wrongq-qmin)>1)
# An arbitrary supplied evolution exactly mimics the other mean after intercept profiling.
shift=v-(float(v.max())+float(v.min()))/2
check('exact_mean_mimic_numerical',np.max(abs((fds+shift)-feds+float(v.max()+v.min())/2))<1e-12)
control('unrestricted_luminosity_evolution_removes_fixed_shape_separation',abs(float((v-shift)@proj(v-shift)))<1e-8)
# Box perturbation support function: maximum of w.delta for |delta_i|<=beta.
beta=.01;worst=beta*np.sign(w);support=float(np.sum(abs(w)));check('adversarial_box_attainment',abs(w@worst-beta*support)<1e-10)
check('repeated_CID_rows_present',len(np.unique(a['CID']))<n)
check('both_extremes_worse_than_fitted_control',q0>qmin and q1>qmin)
check('profile_CI_one_unit',abs(profile(shape(lo))[0]-qmin-1)<1e-7 and abs(profile(shape(hi))[0]-qmin-1)<1e-7)
# Actual released covariance variant, still with shared corrected data and its assumptions.
statraw=np.loadtxt(args.data_dir/'statonly.cov');check('statonly_dimensions',int(statraw[0])==1701 and len(statraw)==1+1701**2)
Cs=statraw[1:].reshape(1701,1701)[np.ix_(ind,ind)];check('statonly_symmetry',np.max(abs(Cs-Cs.T))<1e-12);Fs=cho_factor(Cs,lower=True);os=cho_solve(Fs,one)
def statprofile(f):
 rr=y-f;bb=(os@rr)/(one@os);rr=rr-bb;return float(rr@cho_solve(Fs,rr))
statopt=minimize_scalar(lambda x:statprofile(shape(x)),bounds=(0,1),method='bounded',options={'xatol':1e-11})
check('statonly_interior_fit',statopt.success and 0<statopt.x<1)
statresult={'Omega_m':float(statopt.x),'chi2':float(statopt.fun),'deSitter_chi2':statprofile(fds),'Einstein_deSitter_chi2':statprofile(feds),'extreme_delta_chi2':statprofile(fds)-statprofile(feds),'scope':'released STATONLY still includes duplicate-lightcurve intrinsic covariance; no removal of mean bias corrections'}
info={'release_revision':'c447f0fea703fcd0fff57de5000947b5ca81286b','full_rows':1701,'selected_rows':n,'literal_distinct_selected_CID':len(np.unique(a['CID'])),'selection':'zHD > 0.01; all lightcurves retained with full selected covariance','observable':'m_b_corr; free intercept; no SH0ES absolute calibration','lcdm':{'Omega_m':om,'profile_delta_chi2_1':[lo,hi],'chi2':qmin,'intercept':bestb,'nominal_dof':n-2},'deSitter':{'chi2':q0,'intercept':b0,'nominal_dof':n-1},'Einstein_deSitter':{'chi2':q1,'intercept':b1,'nominal_dof':n-1},'fixed_extreme_pair':{'D2':D2,'T':T,'delta_chi2':q0-q1,'conditional_Gaussian_log10_error':float(log_ndtr(-np.sqrt(D2)/2)/np.log(10)),'infinity_bias_halfseparation':D2/(2*support),'observed_sign_bias_radius':abs(T)/support,'one_sided_exact_mimic_radius':float(np.ptp(v)/2),'symmetric_two_class_overlap_radius':float(np.ptp(v)/4)},'altered_diagonal_chi2_at_full_fit':diagq,'altered_redshift_chi2_at_full_fit':wrongq,'statistical_only_release_sensitivity':statresult,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__}}
def rounder(o):
 if isinstance(o,dict):return {k:rounder(v) for k,v in o.items()}
 if isinstance(o,list):return [rounder(v) for v in o]
 if isinstance(o,float):return round(o,8)
 return o
info=rounder(info)
deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2352-calibrated-flrw-identifiability.json']
out={'result_id':'K2355','checks':len(checks),'check_names':list(checks),'altered_input_controls':controls,'evidence_kind':'double-precision numerical fixed-release diagnostics; exact profiling and perturbation proofs in companion note','details':info,'external_input_sha256':hashes,'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in deps}}
target=R/f'lab/process/{st}.json'
if args.write:target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:
 old=json.loads(target.read_text());assert old['dependencies']==out['dependencies'] and old['external_input_sha256']==hashes
 # Avoid a cross-platform bitwise floating-point requirement; scientific thresholds above remain fixed.
 def compare(a,b):
  if isinstance(a,dict):return a.keys()==b.keys() and all(compare(a[k],b[k]) for k in a if k!='versions')
  if isinstance(a,list):return len(a)==len(b) and all(compare(x,y) for x,y in zip(a,b))
  if isinstance(a,(float,int)) and not isinstance(a,bool):return abs(a-b)<=1e-6*max(1,abs(a))
  return a==b
 assert compare(old,out)
print(json.dumps(out['details'],indent=2));print('PASS',len(checks),'numerical/integrity checks;',len(controls),'changed-input controls')
