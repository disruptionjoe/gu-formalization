"""Fixed sourced-history ANDES forecast: numerical trajectories, exact nuisance algebra."""
from pathlib import Path
import hashlib,json,sys
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import sympy as S
R=Path(__file__).resolve().parents[2]; exact={};numeric={};controls={}
def ck(bank,name,value):
 bank[name]=bool(value)
 if not bank[name]:raise AssertionError(name)
alpha,rho,U0,P0,omega=775.88047141,8540.41820373,2.,.3175541986,.3
h0=U0**(2/3);F0=alpha+12*U0**(1/3)*(U0-P0);q0=3*F0*h0*h0*omega
z=np.array([2.,2.5,3.,3.5,4.5]);times=3*np.log1p(z);end=times[-1]
def rhs(t,y,source_multiplier=1.):
 u,p=y[:2]
 return [p,p-alpha/(36*u**(1/3))+(rho+2*source_multiplier*q0*np.exp(t))/(216*u**(5/3)),np.exp(t/3)/(3*u**(2/3))]
def fval(y):
 u,p=y[:2];return alpha+12*u**(1/3)*(u-p)
def solve(method,tol,mult=1.):
 def event(t,y):return fval(y)
 event.direction=0;event.terminal=True
 sol=solve_ivp(lambda t,y:rhs(t,y,mult),(0,end),[U0,P0,0.],rtol=tol,atol=tol*.01,method=method,dense_output=True,events=event,max_step=.05)
 ck(numeric,'integration_'+method+'_'+str(tol)+'_'+str(mult),sol.success and sol.t[-1]==end)
 return sol
u,p,a,r,q=S.symbols('u p a r q',positive=True);ff=a+12*u**S.Rational(1,3)*(u-p);force=p-a/(36*u**S.Rational(1,3))+(r+2*q)/(216*u**S.Rational(5,3));fs=S.diff(ff,u)*p+S.diff(ff,p)*force
original=3*ff*u**S.Rational(4,3)-q-(ff-a)**2/4-r/2-9*u**S.Rational(4,3)*fs
ck(exact,'original_full00_identity',S.simplify(original)==0)
wrongfs=S.diff(ff,u)*p+S.diff(ff,p)*force.subs(q,0)
ck(controls,'omitted_dust_fails_original00',S.simplify(3*ff*u**S.Rational(4,3)-q-(ff-a)**2/4-r/2-9*u**S.Rational(4,3)*wrongfs)==-q)
sol=solve('DOP853',2e-12);fine=solve('DOP853',3e-14);ind=solve('RK45',2e-12)
grid=np.linspace(0,end,2001);yy=fine.sol(grid);U,P=yy[:2];F=fval(yy)
maxerr=max(float(np.max(abs(sol.sol(grid)-yy))),float(np.max(abs(ind.sol(grid)-yy))))
ck(numeric,'independent_trajectory_agreement',maxerr<2e-7)
ck(numeric,'sampled_positive_U_F',np.min(U)>0 and np.min(F)>0)
ps=np.array([rhs(t,yy[:,i])[1] for i,t in enumerate(grid)]);Fs=4*(4*U-P)*U**(-2/3)*P-12*U**(1/3)*ps;qv=q0*np.exp(grid);h=U**(2/3)
res=3*F*h*h-qv-(F-alpha)**2/4-rho/2-9*h*h*Fs
scaled=float(np.max(abs(res))/(1+np.max(abs(qv))+np.max(abs(3*F*h*h))))
ck(numeric,'full00_numeric',scaled<2e-13)
# All dimensional choices stated: Julian year, standard parsec conversion, H0=70.
ccm=29979245800.;seconds_year=31557600.;mpc_km=3.0856775814913673e19
A70=ccm*70/mpc_km*20*seconds_year
E=fine.sol(times)[0]**(2/3)/h0;d=1-E/(1+z);dref=1-np.sqrt(.3*(1+z)**3+.7)/(1+z);y=A70*dref
sigma=1.35*(3000/2370)**-1*(6/30)**-.5*((1+z)/5)**np.where(z<=4,-1.7,-.9);W=1/sigma**2
ck(numeric,'forecast_sigma_replay',np.max(abs(sigma-np.array([5.683145,4.372997,3.484921,2.852552,2.188731])))<6e-7)
def profile(d,y,W,offset):
 X=np.column_stack([d,np.ones(len(d))]) if offset else d[:,None]
 theta=np.linalg.solve(X.T@(W[:,None]*X),X.T@(W*y))
 # A>=0 closure; an A=0 minimizer is infimum for strictly positive scales.
 boundary=bool(theta[0]<=0)
 if boundary:theta=np.array([0.,np.sum(W*y)/sum(W)]) if offset else np.array([0.])
 residual=y-X@theta
 return dict(A=float(theta[0]),H0=float(theta[0]/A70*70),offset=float(theta[1]) if offset else 0.,chi2=float(np.dot(W,residual**2)),boundary=boundary,residual=residual.tolist())
fixed={'A':A70,'H0':70.,'offset':0.,'chi2':float(np.dot(W,(y-A70*d)**2))}
scale=profile(d,y,W,False);both=profile(d,y,W,True)
ck(numeric,'profiling_never_increases_loss',both['chi2']<=scale['chi2']+1e-10 and scale['chi2']<=fixed['chi2']+1e-10)
X=np.column_stack([d,np.ones(5)]);resid=np.array(both['residual']);ck(numeric,'profile_normal_equations',np.max(abs(X.T@(W*resid)))<1e-10)
# Exact separate fixture checks projection identities, not the numerical cosmology.
D=S.Matrix([[1,1],[2,1],[4,1],[5,1]]);WW=S.diag(1,2,3,4);Q=S.eye(4)-D*(D.T*WW*D).inv()*D.T*WW
ck(exact,'weighted_projection_idempotent',Q*Q==Q)
ck(exact,'weighted_projection_annihilates_shared_nuisances',Q*D==S.zeros(4,2))
ck(exact,'weighted_selfadjoint',Q.T*WW==WW*Q)
plant=S.Matrix([1,0,0,0]);ck(controls,'one_nonaffine_bin_survives_shared_nuisance',Q*plant!=S.zeros(4,1))
ck(controls,'independent_bin_offsets_erase_all_information',S.eye(4)-S.eye(4)*(S.eye(4).T*WW*S.eye(4)).inv()*S.eye(4).T*WW==S.zeros(4))
# Explicit common-mode covariance; profiling an unconstrained constant absorbs it.
common_sigma=10.;C=np.diag(sigma**2)+common_sigma**2*np.ones((5,5));Winv=np.linalg.inv(C);theta=np.linalg.solve(X.T@Winv@X,X.T@Winv@y);rr=y-X@theta
ck(numeric,'common_mode_variance_absorbed_by_free_offset',abs(float(rr@Winv@rr)-both['chi2'])<1e-9)
# Weighted shape contrast is insensitive to d and constant; it is designed from this witness.
cvec=W*resid;ck(numeric,'contrast_removes_both_nuisances',abs(cvec@d)<1e-10 and abs(cvec@np.ones(5))<1e-10)
ck(numeric,'contrast_matches_profile_information',abs(float((cvec@y)**2/(cvec@np.diag(sigma**2)@cvec))-both['chi2'])<1e-8)
# Altered source is checked against original equations above, then evaluated separately.
wrong=solve('DOP853',2e-12,0.);wrongd=1-wrong.sol(times)[0]**(2/3)/h0/(1+z)
ck(controls,'actual_source_omission_changes_forecast',np.max(abs(A70*(wrongd-d)))>1e-3)
ck(controls,'missing_present_normalization_changes_forecast',np.max(abs(A70*(1-fine.sol(times)[0]**(2/3)/(1+z))-A70*d))>1.)
# Same fitted dimensionless BAO ruler transports dimensional-scale freedom.
ruler_lambda=48.4745294
h0rd_over_c=h0/ruler_lambda
for result in [fixed,scale,both]:result['r_d_Mpc']=299792.458*h0rd_over_c/result['H0']
# Profile b at fixed H; Q(H)=Q_min+K(H-Hhat)^2 exactly for fixed shape.
one=np.ones(5);dc=d-np.dot(W,d)/sum(W);yc=y-np.dot(W,y)/sum(W)
Kscale=float(np.dot(W,dc*dc)*(A70/70)**2)
Q70offset=float(np.dot(W,(yc-(A70/70)*70*dc)**2));b70=float(np.dot(W,y-A70*d)/sum(W))
ck(numeric,'fixed_scale_offset_quadratic_profile',abs(Q70offset-both['chi2']-Kscale*(70-both['H0'])**2)<1e-9)
# Supplied Gaussian H0 calibration centered on reference; not an actual data prior.
prior_table=[]
for width in [1.,5.,10.,20.]:
 Hhat=(Kscale*both['H0']+70/width**2)/(Kscale+1/width**2)
 value=both['chi2']+Kscale*(70-both['H0'])**2/(1+Kscale*width**2)
 direct=both['chi2']+Kscale*(Hhat-both['H0'])**2+(Hhat-70)**2/width**2
 ck(numeric,'scale_prior_profile_'+str(width),abs(value-direct)<1e-9)
 prior_table.append(dict(supplied_H0_sigma=width,profiled_H0=Hhat,quadratic_loss=value))
# Consume joint calibrated release ONCE, replacing the old uncalibrated SN likelihood.
import argparse
from scipy.linalg import solve_triangular
from scipy.optimize import brentq
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--data-dir',type=Path,required=True);args=parser.parse_args()
release_hashes={'data.dat':'1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8','covariance.cov':'abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc'}
for file,digest in release_hashes.items():ck(numeric,'pinned_'+file,hashlib.sha256((args.data_dir/file).read_bytes()).hexdigest()==digest)
cat=np.genfromtxt(args.data_dir/'data.dat',names=True,dtype=None,encoding='utf8');raw=np.loadtxt(args.data_dir/'covariance.cov');count=int(raw[0]);ck(numeric,'raw_covariance_size',count==len(cat)==1701 and raw.size==count*count+1)
mask=(cat['zHD']>.01)|(cat['IS_CALIBRATOR'].astype(bool));indices=np.flatnonzero(mask);cat=cat[indices];Csn=raw[1:].reshape(count,count)[np.ix_(indices,indices)]
Craw=Csn.copy();asym=float(np.max(abs(Craw-Craw.T)));ck(numeric,'pinned_release_rounding_asymmetry',asym<=3.1e-8);Csn=(Craw+Craw.T)/2;Ls=np.linalg.cholesky(Csn);white=lambda v:solve_triangular(Ls,v,lower=True)
cal=cat['IS_CALIBRATOR'].astype(bool);noncal=~cal;Bmat=np.column_stack([np.ones(len(cat)),noncal.astype(float)]);Bw=white(Bmat);normal=Bw.T@Bw;covtheta=np.linalg.inv(normal)
ck(numeric,'joint_design_identifies_scale',np.linalg.matrix_rank(Bw)==2 and np.sum(cal)>0)
ck(controls,'shape_only_without_calibrators_has_rank_one',np.linalg.matrix_rank(Bmat[noncal])==1)
ck(numeric,'release_rows_inside_extension',cat['zHD'][noncal].max()<4.5 and cat['zHD'][noncal].min()>0)
def fit_sn(soln):
 chi=soln.sol(3*np.log1p(cat['zHD'][noncal]))[2]
 base=cat['CEPH_DIST'].astype(float).copy()
 base[noncal]=5*np.log10(299792.458/70*(1+cat['zHEL'][noncal])*h0*chi)+25
 rr=cat['m_b_corr']-base;rw=white(rr);th=np.linalg.solve(normal,Bw.T@rw);res=rw-Bw@th
 return th,float(res@res),rw
th,snloss,rw=fit_sn(fine);oth,otherloss,_=fit_sn(ind)
ck(numeric,'joint_calibration_independent_trajectory',np.max(abs(th-oth))<2e-8 and abs(snloss-otherloss)<2e-5)
# Check both triangular completions against the explicitly symmetric central matrix.
rounding_controls=[]
base_residual=Ls@rw
for tri in ['lower','upper']:
 CC=(np.tril(Craw)+np.tril(Craw,-1).T) if tri=='lower' else (np.triu(Craw)+np.triu(Craw,1).T)
 LL=np.linalg.cholesky(CC);ww=lambda v:solve_triangular(LL,v,lower=True);bb=ww(Bmat);zz=ww(base_residual);tt=np.linalg.solve(bb.T@bb,bb.T@zz);loss=float((zz-bb@tt)@(zz-bb@tt))
 ck(numeric,'covariance_rounding_control_'+tri,np.max(abs(tt-th))<1e-5 and abs(loss-snloss)<1e-3)
 rounding_controls.append(dict(completion=tri,max_parameter_change=float(np.max(abs(tt-th))),loss_change=loss-snloss))
Hsn=float(70*10**(-th[1]/5));sigk=float(np.sqrt(covtheta[1,1]));sigmaH=float(Hsn*np.log(10)/5*sigk)
ck(numeric,'joint_fit_normal_equations',np.max(abs(Bw.T@(rw-Bw@th)))<1e-8)
def penalty(H):return float((-5*np.log10(H/70)-th[1])**2/covtheta[1,1])
# Check explicit M-profile against analytic kappa penalty at a remote scale.
remote=both['H0'];kk=-5*np.log10(remote/70);wm=Bw[:,0];rr=rw-Bw[:,1]*kk;mm=float(wm@rr/(wm@wm));remote_loss=float((rr-wm*mm)@(rr-wm*mm))
ck(numeric,'remote_scale_penalty_matches_direct_joint_fit',abs(remote_loss-snloss-penalty(remote))<1e-7)
# Flat LCDM fixed shape supplies a distinct release/calibration convention cross-check.
from numpy.polynomial.legendre import leggauss
nodes,weightsq=leggauss(96);zz=cat['zHD'][noncal];xx=zz[:,None]*(nodes[None,:]+1)/2
chiref=np.sum(weightsq[None,:]/np.sqrt(.33157578*(1+xx)**3+1-.33157578),axis=1)*zz/2
base=cat['CEPH_DIST'].astype(float).copy();base[noncal]=5*np.log10(299792.458/70*(1+cat['zHEL'][noncal])*chiref)+25
rref=white(cat['m_b_corr']-base);tref=np.linalg.solve(normal,Bw.T@rref);Href=float(70*10**(-tref[1]/5));reference_SN_loss=float((rref-Bw@tref)@(rref-Bw@tref))
ck(numeric,'released_calibration_broad_positive_control',70<Href<77 and -19.5<tref[0]<-19.)
# Add forecast only under explicit hypothetical-independent future experiment convention.
def future_loss(H,free_offset):
 rvel=y-(A70/70)*H*d
 if free_offset:rvel-=np.sum(W*rvel)/sum(W)
 return float(np.dot(W,rvel*rvel))
combined=[]
for off in [False,True]:
 fun=lambda H:penalty(H)+future_loss(H,off)
 Hd=both['H0'] if off else scale['H0'];K=Kscale if off else float(np.dot(W,d*d)*(A70/70)**2);Alog=25/(np.log(10)**2*covtheta[1,1])
 derivative=lambda H:2*Alog*np.log(H/Hsn)/H+2*K*(H-Hd)
 ck(numeric,'joint_scalar_bracket_'+str(off),0<Hd<Hsn and derivative(Hd)<0<derivative(Hsn))
 opt=brentq(derivative,Hd,Hsn,xtol=1e-12)
 ck(numeric,'joint_scalar_stationarity_'+str(off),abs(derivative(opt))<1e-9)
 combined.append(dict(free_common_offset=off,H0=float(opt),SN_delta_loss=penalty(opt),forecast_loss=future_loss(opt,off),added_total_loss=float(fun(opt)),unique_global_scalar_minimum_bracket=[Hd,Hsn]))
calibrated=dict(covariance_max_asymmetry=asym,covariance_convention='symmetric average of pinned rounded matrix; both triangular completions checked',covariance_rounding_controls=rounding_controls,release_revision='c447f0fea703fcd0fff57de5000947b5ca81286b',hashes=release_hashes,rows=len(cat),calibrator_rows=int(sum(cal)),noncalibrator_rows=int(sum(noncal)),literal_calibrator_CIDs=len(set(cat['CID'][cal])),M=float(th[0]),kappa=float(th[1]),H0=Hsn,H0_linear_sigma=sigmaH,H0_profile_delta1=[float(Hsn*10**(-sigk/5)),float(Hsn*10**(sigk/5))],kappa_variance=float(covtheta[1,1]),SN_loss=snloss,r_d_Mpc=299792.458*h0rd_over_c/Hsn,drift_scale_remote_SN_delta=penalty(remote),reference_LCDM_H0=Href,reference_LCDM_M=float(tref[0]),reference_LCDM_SN_loss=reference_SN_loss,independent_SN_loss_difference=abs(snloss-otherloss),future_drift_at_calibrated_H0=[dict(free_common_offset=off,loss=future_loss(Hsn,off)) for off in [False,True]],hypothetical_joint_forecast=combined,scope='fixed dimensionless shape with released Cepheid/SN calibration and full joint covariance transported; replaces previous uncalibrated SN likelihood; no independent SH0ES prior added')
print('joint calibration',json.dumps(calibrated,indent=2))

# Stable descriptive output; tolerances are validated separately above.
def clean(v):
 if isinstance(v,float):return float(format(v,'.10g'))
 if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
 if isinstance(v,list):return [clean(x) for x in v]
 return v
paths=['explorations/conditional-build/k2364-sourced-shared-history-2026-10-31.md','lab/process/k2364-sourced-shared-history.json','explorations/conditional-build/k2528-observation-forecast-feasibility-2026-11-04.md',str(Path(__file__).relative_to(R))]
report=clean(dict(result='K2532',exact_checks=exact,numerical_checks=numeric,contrary_controls=controls,calibrated_release=calibrated,parameters=dict(alpha=alpha,rho=rho,U0=U0,P0=P0,Omega_d=omega,q0=q0,F0=F0),forecast_source='https://arxiv.org/pdf/2305.01446 section2 equations1-3',forecast_assumptions='comoving tracers; 20 Julian years; SN3000; six quasars per bin; diagonal marginal statistical covariance supplied',z=z.tolist(),sigma_cm_s=sigma.tolist(),E=E.tolist(),fixed_H0_drift_cm_s=(A70*d).tolist(),reference_drift_cm_s=y.tolist(),fixed=fixed,free_scale=scale,free_scale_offset=both,scale_information=Kscale,fixed70_free_offset_loss=Q70offset,fixed70_offset_cm_s=b70,supplied_scale_prior=prior_table,H0_r_d_over_c=h0rd_over_c,contrast_weights=cvec.tolist(),domain=dict(z_max=4.5,grid=2001,U_min=float(np.min(U)),F_min=float(np.min(F)),F_endpoint=float(F[-1]),independent_max_difference=maxerr,full00_scaled_residual=scaled),evidence_kinds=dict(exact='weighted projection and original sourced00 algebra; universal argument in note',numerical='DOP853 and RK45 trajectory/forecast, not interval enclosure',provenance='input hashes and report replay'),versions=dict(numpy=np.__version__,scipy=scipy.__version__,sympy=S.__version__),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths},empirical_exclusion_or_native_GU_credit=False))
out=R/'lab/process/k2532-finite-drift-forecast.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report,'report differs'
print(json.dumps({k:report[k] for k in ['fixed_H0_drift_cm_s','reference_drift_cm_s','fixed','free_scale','free_scale_offset','domain']},indent=2))
print('K2532:',len(exact),'exact,',len(numeric),'numerical,',len(controls),'contrary controls pass')
