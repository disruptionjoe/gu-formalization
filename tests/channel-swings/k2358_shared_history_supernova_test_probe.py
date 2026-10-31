"""Numerical common-history consumer. No confidence or global minimum certificate."""
from pathlib import Path
import argparse,json,hashlib
import numpy as np
from scipy.linalg import cho_factor,cho_solve,solve_triangular
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares, minimize
R=Path(__file__).resolve().parents[2];st='k2358-shared-history-supernova-test'
p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);p.add_argument('--write',action='store_true');p.add_argument('--scout',action='store_true');args=p.parse_args()
checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('ineffective control '+k)
hashes={'data.dat':'1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8','covariance.cov':'abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc'}
for f,h in hashes.items():check('input_'+f,hashlib.sha256((args.data_dir/f).read_bytes()).hexdigest()==h)
a=np.genfromtxt(args.data_dir/'data.dat',names=True,dtype=None,encoding='utf8');raw=np.loadtxt(args.data_dir/'covariance.cov');n=int(raw[0]);mask=a['zHD']>.01;idx=np.flatnonzero(mask);a=a[mask];C=raw[1:].reshape(n,n)[np.ix_(idx,idx)];z=a['zHD'];zh=a['zHEL'];y=a['m_b_corr'];L=np.linalg.cholesky(C);white=lambda v:solve_triangular(L,v,lower=True);one=white(np.ones(len(z)));den=one@one;wy=white(y)
def sn_res(shape):
 rr=wy-white(shape);return rr-one*(one@rr)/den
source=json.loads((R/'lab/process/k2277-multibin-pure-r2-test.json').read_text())['source_inputs']
for i,f in enumerate(source['files']):check('DESI_source_'+str(i),hashlib.sha256(f['text'].encode()).hexdigest()==f['sha256'])
rows=[l.split() for l in source['files'][0]['text'].splitlines() if l and not l.startswith('#')];bz=np.array([float(x[0]) for x in rows]);by=np.array([float(x[1]) for x in rows]);bc=np.array([[float(x) for x in l.split()] for l in source['files'][1]['text'].splitlines()]);bl=np.linalg.cholesky(bc);bw=lambda v:solve_triangular(bl,v,lower=True);bwy=bw(by)
zmax=max(float(z.max()),float(bz.max()));tmax=(1+zmax)**3
# a=-A,r=-B, positive A,B. Three shared shape coordinates, U1=2 fixes scale convention.
def history(par,rtol=2e-10,method='DOP853'):
 A,B,V=par
 def rhs(t,q):
  u,v,m=q
  if u<=0:raise ValueError('nonpositive numerical trajectory')
  return [v,-A/(36*t*t*u**(1/3))+B/(216*t*t*u**(5/3)),1/(3*(t*u)**(2/3))]
 sol=solve_ivp(rhs,(1,tmax),[2,V,0],rtol=rtol,atol=rtol*.01,method=method,dense_output=True)
 if not sol.success:raise ValueError(sol.message)
 u,v,_=sol.y[:,-1];F=12*u**(1/3)*(u-tmax*v)+A
 if F<=0:raise ValueError('nonpositive endpoint F')
 us,vs,ms=sol.sol((1+z)**3);ub,vb,mb=sol.sol((1+bz)**3)
 f=5*np.log10((1+zh)*ms)
 bf=np.array([{'DM_over_rs':m,'DH_over_rs':u**(-2/3),'DV_over_rs':(zz*m*m*u**(-2/3))**(1/3)}[tag] for zz,u,m,(_,_,tag) in zip(bz,ub,mb,rows)])
 return f,bf,float(F),sol

def residual(par,which='joint',rtol=2e-10,method='DOP853'):
 f,bf,F,sol=history(par,rtol,method);br=bw(bf);lam=float(br@bwy/(br@br));sr=sn_res(f);rr=bwy-lam*br
 return np.r_[sr,rr] if which=='joint' else sr,(float(sr@sr),float(rr@rr),lam,F)
old=[33.8,1,.9303]
oldr,oldvals=residual(old);check('DESI_old_witness_reproduced',5.87<oldvals[1]<5.90)
if args.scout:
 results=[]
 for which in ['sn','joint']:
  for init in [old,[69,100,.8],[258.39,5000,-.39968]]:
   def fun(x):
    try:return residual([np.exp(x[0]),np.exp(x[1]),x[2]],which)[0]
    except (ValueError,OverflowError):return np.ones(len(z)+(13 if which=='joint' else 0))*1e6
   objective=lambda x:float(fun(x)@fun(x))
   fit=minimize(objective,[np.log(init[0]),np.log(init[1]),init[2]],method='Nelder-Mead',options={'maxiter':450,'xatol':1e-7,'fatol':1e-6})
   par=[float(np.exp(fit.x[0])),float(np.exp(fit.x[1])),float(fit.x[2])]
   try: diag=residual(par)[1]
   except ValueError: diag='invalid endpoint F'
   results.append(dict(which=which,start=init,success=bool(fit.success),nfev=int(fit.nfev),parameters=par,diagnostic=diag));print(json.dumps(results[-1]),flush=True)
 print('SCOUT',json.dumps(results));raise SystemExit
# Frozen rounded output of the separately reported scout; deterministic replay does not refit.
witness=[55.85236076,929.86045772,.4885325972]
snwitness=[57.47501734,940.15711289,.4923669240]
snr,snvals=residual(snwitness)
rr,vals=residual(witness);fine,finevals=residual(witness,rtol=2e-12);ind,indvals=residual(witness,rtol=2e-11,method='RK45')
check('tight_tolerance_quadratic_convergence',max(abs(np.array(vals[:2])-np.array(finevals[:2])))<2e-4)
check('independent_RK45_convergence',max(abs(np.array(vals[:2])-np.array(indvals[:2])))<2e-4)
f,bf,endpoint,sol=history(witness);check('common_domain_endpoint_positive',endpoint>1 and sol.success)
check('positive_common_ruler',vals[2]>0);check('joint_tradeoff',snvals[0]<vals[0] and snvals[1]>vals[1]);check('joint_improves_old_combination',sum(vals[:2])<sum(oldvals[:2]));check('full_counts',len(z)==1590 and len(bz)==13)
check('profile_intercept_invariance',abs(np.linalg.norm(sn_res(f+8))**2-vals[0])<1e-6)
# Changed equations/data, not altered checks.
wrong=f+5*np.log10((1+z)/(1+zh));control('wrong_redshift_prefactor',abs(np.linalg.norm(sn_res(wrong))**2-vals[0])>.01)
wd=1/np.diag(C);r=y-f;r-=wd@r/wd.sum();control('diagonal_covariance',abs(r@(wd*r)-vals[0])>1)
control('per_coordinate_BAO_rulers_erase_residual',np.max(abs((by/bf)*bf-by))<1e-12 and vals[1]>1)
# An exact model-shift nuisance can always remove finite-row distance differences: no inference against arbitrary evolution.
control('arbitrary_evolution_mimic',np.linalg.norm(sn_res(f+(y-f)))<1e-9)
info=dict(model='flat vacuum f(R),b=-1,a=-A,r=-B,U1=2',old_DESI_witness=dict(parameters=old,SN_chi2=oldvals[0],BAO_chi2=oldvals[1],ruler=oldvals[2],endpoint_F=oldvals[3]),joint_witness=dict(parameters=witness,SN_chi2=vals[0],BAO_chi2=vals[1],sum_chi2=sum(vals[:2]),ruler=vals[2],endpoint_F=vals[3]),SN_only_witness=dict(parameters=snwitness,SN_chi2=snvals[0],BAO_chi2=snvals[1]),zmax=zmax,convergence=dict(tighter=finevals[:2],RK45=indvals[:2]),scope='fixed released covariance, assumed block-diagonal inter-survey covariance; numerical witness only; no global optimum, calibrated confidence, selection robustness or GU prediction')
deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2277-multibin-pure-r2-test.json','lab/process/k2355-released-supernova-shape.json']
info['search_log']=[{'which': 'sn', 'start': [33.8, 1, 0.9303], 'success': True, 'nfev': 766, 'parameters': [57.47501733995236, 940.1571128929605, 0.4923669239689277], 'diagnostic': [1402.3580026313437, 13.810217878176182, 47.33003176088679, 146.12531492159394]}, {'which': 'sn', 'start': [69, 100, 0.8], 'success': True, 'nfev': 356, 'parameters': [57.47498737242934, 940.1569862013826, 0.49236678266717837], 'diagnostic': [1402.3580026313728, 13.80996208131283, 47.33003809637649, 146.12526917737273]}, {'which': 'sn', 'start': [258.39, 5000, -0.39968], 'success': True, 'nfev': 362, 'parameters': [57.47480681825978, 940.1524394299814, 0.4923676449747506], 'diagnostic': [1402.3580026313523, 13.809960409574591, 47.33003760839223, 146.125011131601]}, {'which': 'joint', 'start': [33.8, 1, 0.9303], 'success': True, 'nfev': 721, 'parameters': [55.85236076159667, 929.8604577217758, 0.4885325972086481], 'diagnostic': [1402.4661460848029, 7.00625353726258, 47.691224426918644, 143.74230978509394]}, {'which': 'joint', 'start': [69, 100, 0.8], 'success': True, 'nfev': 359, 'parameters': [380.40213977391204, 1.4607989477673215e-05, 4.205031562876471], 'diagnostic': [3386.0550841982918, 11136.954116069735, 36.88039667463819, 329.7760464239111]}, {'which': 'joint', 'start': [258.39, 5000, -0.39968], 'success': True, 'nfev': 306, 'parameters': [55.85237303035754, 929.8610068263101, 0.4885322653712134], 'diagnostic': [1402.466144278765, 7.006255343306222, 47.6912224708751, 143.74231732628272]}]
info=json.loads(json.dumps(info));out=dict(result_id='K2358',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='double precision likelihood and ODE diagnostics; prior exact domain theorem explicitly reused',details=info,external_input_sha256=hashes,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
target=R/f'lab/process/{st}.json'
if args.write:target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:
 oldout=json.loads(target.read_text());assert oldout['dependencies']==out['dependencies']
 def same(a,b):
  if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
  if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
  if isinstance(a,float):return abs(a-b)<1e-5*max(1,abs(a))
  return a==b
 assert same(oldout,out)
print(json.dumps(info,indent=2));print('PASS',len(checks),len(controls))
