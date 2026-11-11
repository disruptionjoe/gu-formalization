#!/usr/bin/env python3
"""Fixed-action, initial-state-calibrated cosmology diagnostics (not interval proof).
Run from repository root. --write-report stores the deterministic native evidence.
Only two speculative potentials; coefficients never optimized. See accompanying note.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, math, platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq, minimize_scalar

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / 'tests/wave29/H46_de_raw_bao_likelihood.py'
spec = importlib.util.spec_from_file_location('held_bao_data', DATA_PATH)
DATA = importlib.util.module_from_spec(spec)
spec.loader.exec_module(DATA)
WM = .1430
WR = 2.4728e-5 * (1 + .2271 * 3.046)
HREF = .6736
USTAR = HREF**2 - WM - WR  # frozen ONCE, also for nuisance tests
C100 = 299792.458 / 100
RSTAR, RD, ZSTAR, THETA100 = 144.43, 147.09, 1089.92, 1.04110
REPORT = ROOT / 'lab/process/bet-cosmology-fixed-potentials.json'


def potential(kind, x):
    if kind == 'EXP':
        u = USTAR * np.exp(-np.sqrt(2) * x)
        return u, -np.sqrt(2)*u, 2*u
    if kind == 'COS':
        return USTAR*(1+np.cos(x)), -USTAR*np.sin(x), -USTAR*np.cos(x)
    raise ValueError(kind)


class Background:
    def __init__(self, kind, initial_x, wm=WM, ai=1e-6, method='DOP853', rtol=2e-10):
        self.kind, self.initial_x, self.wm, self.ai = kind, initial_x, wm, ai
        def rhs(n, y):
            x, p = y
            u, ux, _ = potential(kind, x)
            q = wm*np.exp(-3*n) + WR*np.exp(-4*n) + p*p/6 + u
            return [p/np.sqrt(q), -3*p-3*ux/np.sqrt(q)]
        self.rhs = rhs
        self.sol = solve_ivp(rhs, (np.log(ai), 0), [initial_x, 0.], method=method,
                             dense_output=True, rtol=rtol, atol=rtol*.01, max_step=.12)
        if not self.sol.success:
            raise RuntimeError(self.sol.message)
    def values(self, n):
        x,p = self.sol.sol(n)
        u, ux, uxx = potential(self.kind,x)
        q = self.wm*np.exp(-3*n)+WR*np.exp(-4*n)+p*p/6+u
        return x,p,u,q
    def distance(self,z):
        integral,error = quad(lambda n: float(np.exp(-n)/np.sqrt(self.values(n)[3])),
                              -np.log1p(z),0,epsabs=2e-10,epsrel=2e-10,limit=150)
        return C100*integral
    def theta(self,rstar=RSTAR):
        return 100*rstar/self.distance(ZSTAR)
    def summary(self,rd=RD):
        x,p,u,q=self.values(0)
        rho=p*p/6+u
        ns=-np.log1p(ZSTAR)
        early=self.values(ns)
        vector=bao_vector(self,rd)
        return dict(initial_x=float(self.initial_x),x0=float(x),p0=float(p),h=float(np.sqrt(q)),
                    w0=float((p*p/6-u)/rho),omega_phi_star=float((early[1]**2/6+early[2])/early[3]),
                    theta100=float(self.theta()),chi2=chi2(vector),bao=vector.tolist(),
                    scalar_mass2_over_H0sq=float(3*potential(self.kind,x)[2]/q))


class LCDM:
    def __init__(self,u,wm=WM):self.u,self.wm=u,wm
    def values(self,n):return 0.,0.,self.u,self.wm*np.exp(-3*n)+WR*np.exp(-4*n)+self.u
    def distance(self,z):
        return C100*quad(lambda n: float(np.exp(-n)/np.sqrt(self.values(n)[3])),
                         -np.log1p(z),0,epsabs=2e-11,epsrel=2e-11)[0]
    def theta(self,rstar=RSTAR):return 100*rstar/self.distance(ZSTAR)


def bao_vector(bg,rd=RD):
    out=[]
    for z,kind in DATA.DESI_ROWS:
        dm=bg.distance(z)/rd
        dh=C100/np.sqrt(bg.values(-np.log1p(z))[3])/rd
        out.append(dm if kind=='DM' else dh if kind=='DH' else (z*dm*dm*dh)**(1/3))
    return np.array(out)


def chi2(v,cov=DATA.DESI_COV):
    residual=v-DATA.DESI_MEAN
    return float(residual@np.linalg.solve(cov,residual))


def calibrate(kind,wm=WM,theta=THETA100,rstar=RSTAR,**kwargs):
    # Endpoint-bracketed branch, independent of BAO. No all-root assertion.
    bracket=(-2.,3.) if kind=='EXP' else (0.,math.pi)
    f=lambda x: Background(kind,x,wm=wm,**kwargs).theta(rstar)-theta
    x=brentq(f,*bracket,xtol=2e-11)
    return Background(kind,x,wm=wm,**kwargs)


def lcdm_calibrate(wm=WM,theta=THETA100,rstar=RSTAR):
    u=brentq(lambda u: LCDM(u,wm).theta(rstar)-theta,.01,1.,xtol=2e-12)
    return LCDM(u,wm)


def assert_replay(expected,actual,path='root'):
    """Compare decisive saved science recursively, not just its central summary."""
    if isinstance(expected,dict):
        assert set(expected)==set(actual),path
        for key in expected:assert_replay(expected[key],actual[key],path+'.'+key)
    elif isinstance(expected,list):
        assert len(expected)==len(actual),path
        for i,(left,right) in enumerate(zip(expected,actual)):assert_replay(left,right,path+str(i))
    elif isinstance(expected,float):
        tiny = any(token in path for token in ['bound','epsilon','deficit','omega_phi_star','integrator_delta'])
        assert math.isclose(expected,actual,rel_tol=2e-7,abs_tol=1e-15 if tiny else 2e-6),(path,expected,actual)
    else:assert expected==actual,(path,expected,actual)


def main():
    checks=[];controls=[]
    def check(name,ok):
        if not bool(ok):raise AssertionError(name)
        checks.append(name)
    def contrary(name,ok):
        if not bool(ok):raise AssertionError(name)
        controls.append(name)
    check('official 13-vector and positive full covariance',len(DATA.DESI_MEAN)==13 and np.linalg.eigvalsh(DATA.DESI_COV).min()>0)
    # Independently verified mathematical identities; finite arithmetic is support only.
    import sympy as s
    p,u,ux,q,m,r=s.symbols('p u ux q m r', positive=True)
    xp=p/s.sqrt(q); pp=-3*p-3*ux/s.sqrt(q)
    check('scalar conservation identity',s.simplify(p*pp/3+ux*xp+p*p)==0)
    check('Friedmann derivative identity',s.simplify(-3*m-4*r+p*pp/3+ux*xp-(-3*m-4*r-p*p))==0)
    x=s.symbols('x',real=True)
    for pot in [s.exp(-s.sqrt(2)*x),1+s.cos(x)]:
        check('potential derivative '+str(pot),s.simplify(s.diff(pot,x,2)-(2*pot if pot.func==s.exp else -s.cos(x)))==0)
    a,beta=s.symbols('a beta',positive=True)
    check('exact stiff tail antiderivative',s.simplify(s.diff(a-s.sqrt(a*a+beta*beta),a)-(1-a/s.sqrt(a*a+beta*beta)))==0)
    # Positive stiff energy saturates the growth bound. This mathematical
    # comparison is not a third guessed dark-energy action.
    import mpmath as mp
    with mp.workdps(50):
        bv=mp.mpf('0.02'); av=mp.mpf('0.1')
        integ=mp.quad(lambda t:1-t/mp.sqrt(t*t+bv*bv),[0,av])
        check('stiff/radiation exact-tail control',abs(integ-(av-mp.sqrt(av*av+bv*bv)+bv))<mp.mpf('1e-40'))
    contrary('uniform early-negligibility inference fails',1e-9*(1e-6/1e-12)**2>1)
    from fractions import Fraction as F
    check('uniform raw ruler bound epsilon', F(7,170000000)*274/2 + F(12,100000000000) < F(6,1000000))
    check('uniform raw ruler bound geometric factor', F(3000**2,1000**2)/(3*F(4,100000)) < 274**2)
    lc=lcdm_calibrate(); lv=bao_vector(lc); lcchi=chi2(lv); h_lc=float(np.sqrt(lc.values(0)[3]))
    check('LCDM actual theta calibration',abs(lc.theta()-THETA100)<1e-9)
    check('LCDM shared early approximation close to reference',abs(h_lc/HREF-1)<.003)
    out=dict(schema_version='1.0',program_target='BET-COSMOLOGY',tier='T2',classification='CONVENTIONAL_COMPARATOR',
             status='conditional_numerical_diagnostics',claim_effect='none; no source, ledger or matrix verdict',
             coefficients=dict(omega_m=WM,omega_r=WR,h_ref=HREF,Ustar=USTAR,lambda_exponential=math.sqrt(2),f_over_Mpl=1),
             calibration=dict(theta100=THETA100,rstar=RSTAR,rd=RD,zstar=ZSTAR,ai=1e-6,
                              policy='initial position only; frozen p_i=0; no BAO selection or coefficient tuning; h is output'),
             lcdm=dict(h=h_lc,chi2=lcchi,theta100=lc.theta(),bao=lv.tolist()),variants={})
    models={}
    for kind in ['EXP','COS']:
        bg=calibrate(kind);models[kind]=bg;row=bg.summary();row['delta_chi2']=row['chi2']-lcchi
        check(kind+' acoustic root',abs(row['theta100']-THETA100)<2e-9)
        check(kind+' canonical acoustic ordering',row['h']<h_lc)
        check(kind+' finite physical background',-1<row['w0']<1 and row['h']>np.sqrt(WM+WR))
        check(kind+' recombination scalar fraction',row['omega_phi_star']<1e-7)
        # An independent integrator and tighter tolerances, same scientific object.
        alt=calibrate(kind,method='RK45',rtol=2e-11).summary()
        row['integrator_delta']=dict(h=abs(alt['h']-row['h']),chi2=abs(alt['chi2']-row['chi2']))
        check(kind+' independent integrator',row['integrator_delta']['h']<2e-8 and row['integrator_delta']['chi2']<2e-5)
        row['initial_time_controls']=[]
        for ai in [1e-5,1e-7,1e-9]:
            other=calibrate(kind,ai=ai).summary();row['initial_time_controls'].append(dict(ai=ai,h=other['h'],chi2=other['chi2']))
            check(kind+' initial-time '+str(ai),abs(other['chi2']-row['chi2'])<2e-4)
        # Error in inherited radiation/neutrino approximation: alternate calibration target,
        # never post-solve H0 rescaling.
        theta_matched=LCDM(USTAR).theta()
        matched=calibrate(kind,theta=theta_matched).summary()
        matched_lcdm_chi=chi2(bao_vector(LCDM(USTAR)))
        row['baseline_matched_control']=dict(theta_target=theta_matched,**matched,delta_chi2=matched['chi2']-matched_lcdm_chi)
        check(kind+' alternative baseline actual recalibration',abs(matched['theta100']-theta_matched)<2e-9)
        same=LCDM(bg.values(0)[3]-WM-WR)
        check(kind+' same-h distance inequality',all(bg.distance(z)<=same.distance(z)+1e-6 for z in [.295,.706,2.33,ZSTAR]))
        row['diagonal_covariance_delta_chi2']=chi2(np.array(row['bao']),np.diag(np.diag(DATA.DESI_COV)))-chi2(lv,np.diag(np.diag(DATA.DESI_COV)))
        contrary(kind+' dropped covariance changes decision statistic',abs(row['diagonal_covariance_delta_chi2']-row['delta_chi2'])>.1)
        uncal=Background(kind,0 if kind=='EXP' else math.pi/2)
        row['uncalibrated_control']=uncal.summary()
        contrary(kind+' preset initial state is not acoustic-calibrated',abs(uncal.theta()-THETA100)>1e-4)
        # Exact positive-energy backward-growth bound, NOT uniformly small
        # pre-ai scalar fraction. Recombination/drag events are held fixed.
        rhoi=float(potential(kind,bg.initial_x)[0]); ai=bg.ai
        beta=ai**3*math.sqrt(rhoi/WR)
        tail=C100/math.sqrt(3*WR)*(beta-beta*beta/(math.sqrt(ai*ai+beta*beta)+ai))
        bounds={}
        for label,z,ruler in [('star',ZSTAR,RSTAR),('drag',1059.94,RD)]:
            epsilon=rhoi/(WM*(1+z)**3+WR*(1+z)**4)
            # Use independently integrated no-scalar ruler in the upper bound,
            # not the imported observational central value.
            rb=3*.02237/(4*2.4728e-5)
            base=C100/math.sqrt(3)*quad(lambda a:1/math.sqrt((WR+WM*a)*(1+rb*a)),0,1/(1+z),epsabs=1e-10)[0]
            bounds[label]=dict(epsilon=epsilon,tail_deficit_Mpc=tail,late_deficit_Mpc=epsilon*base/2,
                               full_deficit_Mpc_upper_bound=tail+epsilon*base/2)
        row['early_fraction_upper_bound']=bounds['star']['epsilon']
        row['fixed_event_sound_deficit_bounds']=bounds
        row['early_scope']='nonnegative potential; backward energy growth bounded, not uniformly small; no full CMB, BBN, recombination-event or primordial-state certification'
        check(kind+' actual early fraction obeys energy bound',row['omega_phi_star']<=bounds['star']['epsilon'])
        check(kind+' tail bound positive and below coarse bound',0<tail<C100*ai/math.sqrt(3*WR))
        out['variants'][kind]=row
    # COS branch search is explicitly finite. Does not certify global uniqueness.
    cos_scan=[]
    for initial_x in np.linspace(0,math.pi,65):
        bg=Background('COS',float(initial_x));cos_scan.append([float(initial_x),bg.theta()-THETA100])
    brackets=[[a[0],b[0]] for a,b in zip(cos_scan,cos_scan[1:]) if a[1]*b[1]<0]
    out['cosine_root_search']=dict(grid=cos_scan,sign_change_brackets=brackets,all_roots_certified=False)
    check('COS finite search found calibrated bracket',len(brackets)>=1)
    # Opposite null and local-derivative traps.
    check('cosine frozen hilltop is exact Lambda',np.max(np.abs(Background('COS',0).sol.y[1]))==0)
    check('cosine minimum is matter-radiation control',abs(Background('COS',math.pi).values(0)[3]-WM-WR)<1e-13)
    contrary('swap final DH/DM rejected by likelihood',chi2(lv[:-2].tolist()+[lv[-1],lv[-2]])>lcchi+1000)
    contrary('phantom kinetic breaks monotone energy premise',-(-1)*2**2>0)
    # Released successor: extend edge minima and replace power-law rulers by
    # the explicit baryon-photon integral, with both variants' coefficients fixed.
    wb=.02237; wg=2.4728e-5; zdrag=1059.94
    def sound_integral(wm,z):
        abar=1/(1+z); rb=3*wb/(4*wg)
        return C100/math.sqrt(3)*quad(lambda a: 1/math.sqrt((WR+wm*a)*(1+rb*a)),
                                     0,abar,epsabs=2e-11,epsrel=2e-11)[0]
    def rulers(wm,method):
        if method=='powerlaw':return RSTAR*(wm/WM)**(-.25),RD*(wm/WM)**(-.25)
        return RSTAR*sound_integral(wm,ZSTAR)/sound_integral(WM,ZSTAR),RD*sound_integral(wm,zdrag)/sound_integral(WM,zdrag)
    def nuisance_row(n,rule='powerlaw',kind=None,integrator='DOP853'):
        wm=WM+n*.0011;rs,rd=rulers(wm,rule)
        if kind=='LCDM':
            bg=lcdm_calibrate(wm=wm,rstar=rs);v=bao_vector(bg,rd)
            return dict(chi2=chi2(v),total=chi2(v)+n*n,h=float(np.sqrt(bg.values(0)[3])))
        bg=calibrate(kind,wm=wm,rstar=rs,method=integrator);v=bao_vector(bg,rd);row=bg.summary(rd)
        return dict(chi2=chi2(v),total=chi2(v)+n*n,h=row['h'],w0=row['w0'],initial_x=bg.initial_x,theta100=bg.theta(rs))
    scans={}
    for rule in ['powerlaw','sound_integral']:
        nuisance=[]
        for n in np.arange(-6,3.01,.5):
            rec=dict(n=float(n),omega_m=WM+n*.0011)
            for kind in ['LCDM','EXP','COS']:
                rec[kind]=nuisance_row(float(n),rule,kind)
                if kind!='LCDM':check(kind+' '+rule+' nuisance calibration '+str(n),abs(rec[kind]['theta100']-THETA100)<2e-8)
            nuisance.append(rec)
        minima={}
        for kind in ['LCDM','EXP','COS']:
            opt=minimize_scalar(lambda n:nuisance_row(float(n),rule,kind)['total'],bounds=(-6.,3.),method='bounded',options={'xatol':2e-5})
            row=nuisance_row(float(opt.x),rule,kind)
            minima[kind]=dict(n=float(opt.x),**row)
            check(kind+' '+rule+' interior numerical optimum',opt.success and -5.99<opt.x<2.99)
            if kind!='LCDM':
                alt=nuisance_row(float(opt.x),rule,kind,integrator='RK45')
                check(kind+' '+rule+' optimum independent integrator',abs(alt['total']-row['total'])<2e-5)
        scans[rule]=dict(rows=nuisance,numerical_minima=minima,delta_minima={k:minima[k]['total']-minima['LCDM']['total'] for k in ['EXP','COS']},global_minimum_certified=False)
    out['nuisance_scan']=dict(scans=scans,coefficient_policy='Ustar stays frozen at central value; only wm, rulers and initial state vary',
                              prior='n=(omega_m-.1430)/.0011; add n^2 to both models',range=[-6,3],
                              sound_integral=dict(omega_b=wb,zdrag=zdrag,formula='c/(100 sqrt3) integral_0^a da/sqrt((omega_r+omega_m*a)*(1+3*omega_b*a/(4*omega_gamma)))',
                                                  central_rstar=sound_integral(WM,ZSTAR),central_rd=sound_integral(WM,zdrag),
                                                  normalization='ruler RATIOS anchored to Planck central values; fixed recombination/drag redshifts; not full recombination or massive-neutrino physics'),
                              continuous_profile_certified=False)
    contrary('ruler scaling is not exactly quarter-power',abs(rulers(WM-3*.0011,'powerlaw')[0]/rulers(WM-3*.0011,'sound_integral')[0]-1)>1e-5)
    # Exact quadratic statistic error budget, not a bound on the actual omitted physics.
    for kind,row in out['variants'].items():
        margin=row['delta_chi2']-10
        row['equal_whitened_model_error_radius_to_threshold']=float((np.sqrt(row['chi2'])-np.sqrt(lcchi)-10/(np.sqrt(row['chi2'])+np.sqrt(lcchi)))/2) if margin>0 else None
    out['validation']=dict(supporting_checks=len(checks),supporting=checks,contrary_controls=len(controls),contrary=controls,
                           evidence_kind='written analytic identities plus floating ODE, quadrature and likelihood diagnostics; not interval or Lean certification')
    out['reproduction']=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
                             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                             reused_data_module=str(DATA_PATH.relative_to(ROOT)),data_module_sha256=hashlib.sha256(DATA_PATH.read_bytes()).hexdigest(),
                             upstream_snapshot='CobayaSampler/bao_data@bb0c1c9009dc76d1391300e169e8df38fd1096db',
                             primary_sources=['https://arxiv.org/abs/2503.14738','https://arxiv.org/abs/1807.06209'])
    if args.write_report:REPORT.write_text(json.dumps(out,indent=2)+'\n')
    elif REPORT.exists():
        expected=json.loads(REPORT.read_text())
        # Environment versions are provenance, not scientific equality; hashes are.
        for key in out:
            if key!='reproduction':assert_replay(expected[key],out[key],key)
        for key in ['script_sha256','data_module_sha256','upstream_snapshot']:
            assert expected['reproduction'][key]==out['reproduction'][key],key
    print(json.dumps(dict(lcdm=out['lcdm'],variants={k:{x:v[x] for x in ['h','w0','chi2','delta_chi2','initial_x','early_fraction_upper_bound','scalar_mass2_over_H0sq']} for k,v in out['variants'].items()},nuisance={k:v['delta_minima'] for k,v in scans.items()},checks=len(checks),controls=len(controls)),indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write-report',action='store_true');args=parser.parse_args();main()
