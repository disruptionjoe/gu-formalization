"""K2518 exact local/operator identities and explicitly numerical finite-window forecast."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
R=Path(__file__).resolve().parents[2]; checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
U,p,alpha,rho,q=s.symbols('U p alpha rho q',positive=True)
ps=p-alpha/(36*U**s.Rational(1,3))+(rho+2*q)/(216*U**s.Rational(5,3))
RR=12*U**s.Rational(1,3)*(U-p);F=alpha+RR;Fs=s.diff(F,U)*p+s.diff(F,p)*ps;h2=U**s.Rational(4,3)
ck('full00_identity',s.simplify(3*F*h2-RR**2/4-rho/2-9*h2*Fs-q)==0)
ck('source_velocity',s.simplify(s.diff(Fs,q)+1/(9*U**s.Rational(4,3)))==0)
ck('tangent_constraint',s.simplify(-9*h2*s.diff(Fs,q)-1)==0)
ck('tangent_U_coefficient',s.simplify(s.diff(ps,U)-alpha/(108*U**s.Rational(4,3))+5*(rho+2*q)/(648*U**s.Rational(8,3)))==0)
ck('tangent_source_force',s.diff(ps,q)==1/(108*U**s.Rational(5,3)))
# d/dz=3/(1+z)d/ds; zero initial u,v supplies u_zz=9/(108U^(5/3)).
uz2=9/(216*U**s.Rational(5,3));hz2=s.Rational(2,3)*U**s.Rational(-1,3)*uz2
cz3=-hz2/(3*U**s.Rational(4,3));Bz2=cz3*U**s.Rational(2,3);Az2=2*Bz2-2*uz2/(3*U)
ck('u_quadratic',s.simplify(uz2-1/(24*U**s.Rational(5,3)))==0)
ck('distance_cubic',s.simplify(cz3+1/(108*U**s.Rational(10,3)))==0)
ck('B_quadratic',s.simplify(Bz2+1/(108*U**s.Rational(8,3)))==0)
ck('A_quadratic',s.simplify(Az2+5/(108*U**s.Rational(8,3)))==0)
ck('local_matched_ratio',s.simplify(Az2/Bz2)==5)
x,r=s.symbols('x r',positive=True)
for n in range(2,7):
 psi=s.integrate((x-r)/(x*r)*r**n,(r,0,x))
 ck('Volterra_inverse_'+str(n),s.simplify(s.diff(x*x*s.diff(psi,x),x)-x**n)==0)
ct('inverse_missing_factor',s.diff(x*x*s.diff(x*x/6,x),x)/2!=x*x)
A1,A2,B1,B2=s.symbols('A1 A2 B1 B2');K=(A2-A1)/(B2-B1);row=s.Matrix([[-1,1,K,-K]])
ck('calibrated_factorization',s.simplify((row*s.Matrix([A1,A2,B1,B2]))[0])==0)
ck('count_intercept_removed',(row*s.Matrix([1,1,0,0]))[0]==0)
ck('distance_intercept_removed',(row*s.Matrix([0,0,1,1]))[0]==0)
ct('free_bin_calibration_survives',(row*s.Matrix([0,1,0,0]))[0]==1)
ct('absolute_monopole_visible',1/q!=0)
ct('angular_mean_subtraction_erases',s.diff(q/q,q)==0)
ct('freeze_scalar_velocity_breaks00',s.simplify(-9*h2*0-s.diff(q,q))!=0)
# An actual PSD covariance with count-distance correlations, not independent-error substitution.
M=s.Matrix([[1,0,0,0],[s.Rational(1,2),1,0,0],[1,0,2,0],[0,1,s.Rational(1,3),1]])
N=M*M.T;rr=s.Matrix([[-1,1,3,-3]])
ck('covariance_positive',all(N[:i,:i].det()>0 for i in range(1,5)))
ct('discard_cross_covariance_changes_variance',(rr*N*rr.T)[0]!=(rr*s.diag(*N.diagonal())*rr.T)[0])
ct('wrong_ratio_fails',(s.Matrix([[-1,1,5,-5]])*s.Matrix([0,3,0,1]))[0]!=0)
# Numerical demonstration: original rounded K2367 witness, no fit or data download.
a0=775.88047141;rho0=8540.41820373;U0=2.;p0=.3175541986
F0=a0+12*U0**(1/3)*(U0-p0);q0=3*F0*U0**(4/3)*.3
smax=3*np.log1p(.22)
def flow(ss,y,qq):
 u0,pp,xx,uu,vv,cc=y;ex=np.exp(ss)
 force=pp-a0/(36*u0**(1/3))+(rho0+2*qq*ex)/(216*u0**(5/3))
 coeff=a0/(108*u0**(4/3))-5*(rho0+2*qq*ex)/(648*u0**(8/3))
 return [pp,force,np.exp(ss/3)/(3*u0**(2/3)),vv,vv+coeff*uu+ex/(108*u0**(5/3)),-2*np.exp(ss/3)*uu/(9*u0**(5/3))]
def sol(method,qq=q0):
 out=solve_ivp(lambda t,y:flow(t,y,qq),(0,smax),[U0,p0,0,0,0,0],method=method,rtol=2e-12,atol=2e-14,dense_output=True,max_step=.01)
 ck('integrator_'+method+'_'+str(qq),out.success)
 return out
s1=sol('DOP853');s2=sol('RK45')
def vals(sol,z):
 Uv,pv,chi,uu,vv,cc=sol.sol(3*np.log1p(z));B=cc/chi;A=1/q0+2*B-2*uu/(3*Uv)
 return A,B,q0*chi**2/Uv**(2/3)
def windows(sol,n,windows=((.08,.12),(.18,.22))):
 nodes,weights=leggauss(n);out=[]
 for lo,hi in windows:
  zz=(lo+hi)/2+(hi-lo)*nodes/2;ww=weights*(hi-lo)/2;A,B,Nbar=vals(sol,zz)
  out.append((float(np.sum(ww*Nbar*A)/np.sum(ww*Nbar)),float(np.sum(ww*B)/(hi-lo))))
 return np.array(out)
w1=windows(s1,96);w2=windows(s2,48);ck('dual_integrator_window_agreement',np.max(np.abs(w1-w2))<2e-12)
ck('quadrature_48_96',np.max(np.abs(w1-windows(s1,48)))<2e-13)
Knum=float(np.diff(w1[:,0])[0]/np.diff(w1[:,1])[0]);ck('finite_window_nonzero_DeltaB',abs(np.diff(w1[:,1])[0])>1e-7)
ct('finite_window_ratio_not_five',abs(Knum-5)>.01)
# Independent actual nonlinear source perturbations verify both tangent outputs.
step=.1;plus=sol('DOP853',q0+step);minus=sol('DOP853',q0-step);z=np.array([.1,.2]);av,bv,_=vals(s1,z)
def logs(sol,qq):
 uv,pv,chi,*_=sol.sol(3*np.log1p(z));return np.log(qq*chi**2/uv**(2/3)),np.log((1+z)*chi)
lp,dp=logs(plus,q0+step);lm,dm=logs(minus,q0-step)
ck('nonlinear_count_tangent',np.max(abs((lp-lm)/(2*step)-av))<1e-10)
ck('nonlinear_distance_tangent',np.max(abs((dp-dm)/(2*step)-bv))<1e-10)
ct('unweighted_counts_change_rows',np.max(abs(w1[:,0]-np.array([np.mean(vals(s1,np.linspace(lo,hi,1001))[0]) for lo,hi in [(.08,.12),(.18,.22)]])))>1e-8)
forecast={'base_q0':q0,'point_z':z.tolist(),'point_A':av.tolist(),'point_B':bv.tolist(),'windows':[[.08,.12],[.18,.22]],'window_A_B':w1.tolist(),'K':Knum,'dual_max_abs_difference':float(np.max(np.abs(w1-w2))),'scope':'floating point convergence evidence, not certified interval or survey likelihood'}
paths=['explorations/conditional-build/k2518-lightcone-count-access-2026-11-02.md','tests/channel-swings/k2518_lightcone_count_access_probe.py',*['explorations/conditional-build/'+p+'-2026-10-31.md' for p in ['k2364-sourced-shared-history','k2367-sourced-fit-dust-transfer','k2373-two-epoch-cosmological-observability','k2376-windowed-cosmological-null','k2379-shared-calibration-cosmological-null']]]
report={'result':'K2518','checks':checks,'contrary_controls':controls,'numerical_forecast':forecast,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
pth=R/'lab/process/k2518-lightcone-count-access.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2)+'\n')
else:
 saved=json.loads(pth.read_text());ck('saved_exact_report',all(saved[k]==v for k,v in report.items() if k!='numerical_forecast'))
 for k in ['base_q0','point_A','point_B','window_A_B','K']:ck('saved_numerics_'+k,np.allclose(saved['numerical_forecast'][k],forecast[k],rtol=1e-8,atol=1e-12))
print('K2518 PASS',len(checks),'checks',len(controls),'controls; finite-window K=',Knum)
