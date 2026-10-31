"""Exact retuning rigidity and numerical constrained transfer of K2358's same history."""
from pathlib import Path
import json,hashlib,sys
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
R=Path(__file__).resolve().parents[2];st='k2361-shared-history-dynamics-and-matter';checks={};controls={};numerical={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def num(k,v):
 numerical[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
x=s.symbols('x',positive=True);c0,c3,c4,alpha,rho,beta=s.symbols('c0 c3 c4 alpha rho beta',real=True);y=c0+c3*x**3+c4*x**4;Ric=12*y-3*x*s.diff(y,x);Q=s.expand(Ric**2/4-3*y*Ric+3*x*y*s.diff(Ric,x));expected=s.Rational(81,4)*c3*c3*x**6+18*c3*c4*x**7-36*c0*c4*x**4
check('actual_full00_polynomial',s.expand(Q-expected)==0)
E=s.Poly(-beta*Q+3*alpha*y-rho/2,x);check('dust_square_obstruction',E.coeff_monomial(x**6)==-s.Rational(81,4)*beta*c3*c3)
check('radiation_Fzero',s.simplify((alpha+beta*Ric).subs({c3:0,c0:-alpha/(12*beta)}))==0)
check('degenerate_radiation_control',s.simplify(E.as_expr().subs({c3:0,c0:-alpha/(12*beta),rho:-alpha*alpha/(2*beta)}))==0)
a0,a1,r0,r1,b0,b1,q,Qsym,Y=s.symbols('a0 a1 r0 r1 b0 b1 q Q Y');old=-b0*Qsym+3*a0*Y-r0/2;new=-b1*Qsym+3*a1*Y-r1/2-q
check('all_constant_retuning_eliminates_Q',s.expand(new-b1/b0*old-(3*(a1-b1*a0/b0)*Y-(r1-b1*r0/b0)/2-q))==0)
control('ignore_x6_obstruction',E.coeff_monomial(x**6).subs({beta:1,c3:1})!=0)
control('Fzero_exception_is_real',s.simplify(E.as_expr().subs({c3:0,c0:-alpha/(12*beta),rho:-alpha*alpha/(2*beta)}))==0)
# Pump independently expanded before applying acceleration equation.
H,Hd,F,Fd,Fdd,k,rm,pm,aa=s.symbols('H Hd F Fd Fdd k rm pm aa',nonzero=True)
pump=aa**2*(2*H**2+Hd+s.Rational(3,2)*H*Fd/F+Fdd/(2*F)-Fd**2/(4*F**2));closed=aa**2*(2*H**2+2*H*Fd/F-Fd**2/(4*F**2)-k*(rm+pm)/(2*F))
check('matter_tensor_pump',s.simplify(pump.subs(Fdd,H*Fd-2*F*Hd-k*(rm+pm))-closed)==0)
control('radiation_not_absent_from_tensor_pump',s.simplify((closed-closed.subs({rm:0,pm:0})).subs(pm,rm/3))!=0)
# K2291 regular constrained scalar expression, evaluate NEW K2358 parameters.
u,p,A,B=s.symbols('u p A B',positive=True);flow=lambda e:s.diff(e,u)*p/(3*u*u)+s.diff(e,p)*(p-A/(36*u)+B/(216*u**5));FF=12*u*(u**3-p)+A;bb=-3*flow(FF)/FF;j=bb/(bb+2);ell=-6/(bb+2);D=A*A+2*B;X=s.sqrt(6)*j;Yp=(A-D/FF)/(s.sqrt(6)*u**4*(1+bb/2)**2);W=(-A+2*D/FF)/(3*u**4*(1+bb/2)**2);mass=W+2*X*Yp+3*X*X-X**4/2
fun=s.lambdify((u,p,A,B),(FF,bb,mass,W,ell,3*j*j,X,ell*flow(X)),'numpy',cse=True)
alpha0=55.85236076;rho0=929.86045772;p0=.4885325972;smax=3*np.log(3.33)
def rhs(t,v):
 U,P=v;return [P,P-alpha0/(36*U**(1/3))+rho0/(216*U**(5/3))]
def history(method,tol):
 sol=solve_ivp(rhs,(0,smax),[2,p0],method=method,rtol=tol,atol=tol*.01,dense_output=True);assert sol.success;return sol
h=history('DOP853',2e-12);h2=history('RK45',2e-12)
def coeff(t,sol=h):
 U,P=sol.sol(t);return fun(U**(1/3),P,alpha0,rho0)
vals=np.array([coeff(t) for t in np.linspace(0,smax,2001)])
num('new_present_mass',abs(vals[0,2]-9.3387633286)<2e-9);num('sampled_positive_F_and_mass',np.min(vals[:,0])>78 and np.min(vals[:,2])>2);num('independent_background_method',np.max(np.abs(h.sol(np.linspace(0,smax,31))-h2.sol(np.linspace(0,smax,31))))<2e-8)
turn=brentq(lambda t:coeff(t)[1],0,.01,xtol=1e-14);num('turning_point_regular_Q',0<turn<.01 and np.isfinite(coeff(turn)).all() and abs(coeff(turn)[1])<1e-12)
def transfer(kbar,sol=h,method='DOP853',tol=2e-11,potential=False):
 def rr(t,v):
  U,P=sol.sol(t);f,b,m,w,l,ep,_,_=coeff(t,sol);K2=kbar*kbar*np.exp(2*t/3)/(U**(4/3)*(1+b/2)**2);M=np.array([[0,1],[-(K2+(w if potential else m)),-(3-ep)]])/l;return (M@v.reshape(2,2)).ravel()
 out=solve_ivp(rr,(smax,0),np.eye(2).ravel(),method=method,rtol=tol,atol=tol*.01);assert out.success;return out.y[:,-1].reshape(2,2)
matrices={};maxdiff=0
for kb in [0,.1,1,10]:
 T=transfer(kb);T2=transfer(kb,h2,'RK45',2e-12);err=np.max(np.abs(T-T2));maxdiff=max(maxdiff,err);num('independent_transfer_'+str(kb),err<2e-8)
 determinant=np.exp(quad(lambda t:-(3-coeff(t)[5])/coeff(t)[4],smax,0,epsabs=1e-11,epsrel=1e-11)[0]);num('Liouville_'+str(kb),abs(np.linalg.det(T)-determinant)<2e-9)
 matrices[str(kb)]=dict(matrix=np.round(T,8).tolist(),singular_values=np.round(np.linalg.svd(T,compute_uv=False),8).tolist(),determinant=round(float(np.linalg.det(T)),10))
initial=np.array(coeff(smax)[6:8]);final=np.array(coeff(0)[6:8]);num('independent_adiabatic_solution',np.max(np.abs(transfer(0)@initial-final))<1e-9)
control('potential_only_changes_transfer',np.linalg.norm(transfer(1,potential=True)-transfer(1))>.01)
control('old_mass_does_not_transfer',fun(2**(1/3),.9303,33.8,1)[2]<-8 and coeff(0)[2]>9)
control('comoving_variable_divides_by_zero',abs(coeff(turn)[6])<1e-12)
deps=['lab/process/k2358-shared-history-supernova-test.json','lab/process/k2291-rolling-scalar-applicability.json','lab/process/k2292-conserved-matter-cosmology.json',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2361',exact_checks=len(checks),exact_check_names=list(checks),numerical_checks=len(numerical),numerical_check_names=list(numerical),altered_input_controls=controls,evidence_kind='exact polynomial/matter identities and double precision ODE transfer with independent method; mass grid is not interval proof',details=dict(coefficients=[alpha0,rho0,2,p0],present=dict(F=round(float(coeff(0)[0]),10),beta=round(float(coeff(0)[1]),12),constrained_mass=round(float(coeff(0)[2]),10)),sampled_mass_range=[round(float(np.min(vals[:,2])),8),round(float(np.max(vals[:,2])),8)],turning_redshift=round(float(np.expm1(turn/3)),12),transfers=matrices,maximum_method_matrix_discrepancy=round(float(maxdiff),12),phase_norm='Euclidean (Q,dQ/dN_E), no primordial spectrum or energy interpretation',retuning='no regular positive-F vacuum history retained after nonzero conserved dust/radiation, even constant coefficient changes',controls='F=0 exception retained; no finite-distance exclusion'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(numerical),len(controls));print(json.dumps(out['details']))
