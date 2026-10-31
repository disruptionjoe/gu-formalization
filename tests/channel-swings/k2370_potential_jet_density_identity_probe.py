"""K2370 exact model-field density/potential identity; no ODE replay."""
from pathlib import Path
import json, hashlib, sys
import numpy as np
import sympy as S
import mpmath as mp
mp.mp.dps=70
ROOT=Path(__file__).resolve().parents[2]
st='k2370-potential-jet-density-identity';checks={};faults={}
def check(k,v):
    checks[k]=bool(v)
    if not v: raise AssertionError(k)
def reject(k,v):
    faults[k]=bool(v)
    if not v: raise AssertionError('undetected '+k)
H,u,d,Q,Vp,b=S.symbols('H u d Q Vp b', nonzero=True,real=True)
ph,ch,pi,v,n,P=S.symbols('Phi chi pi v n P',real=True)
x=S.Matrix([ph,ch,pi,v])
ns=(-(2*Q-u*u)*ph-(3*H*u+Vp+b*d)*ch+3*H*d*v-u*pi)/d
mom=-H*ph+(u*ch-d*v)/2
L=2*ph; Z=2*b*ch; Ldot=2*mom; Zdot=2*b*pi
delta=ns-3*b*ch
C=Q*ph+3*H*(P+H*ph)+(u*pi-u*u*ph+Vp*ch+d*(n+b*ch))/2
# First derive directly from full Hamiltonian with P left uneliminated.
null_full=2*d*(n-3*b*ch)+(2*Q-u*u+6*H*H)*L+6*H*(2*P)+(Vp/b+4*d)*Z+(u/b)*Zdot
check('exact_null_equals_four_Hamiltonian',S.expand(null_full-4*C)==0)
null=null_full.subs({n:ns,P:mom})
check('exact_all_seed_null',S.expand(null)==0)
O=S.Matrix([L,Z,Ldot,Zdot]).jacobian(x)
check('exact_observability_determinant',S.factor(O.det()-8*b*b*d)==0)
xrec=S.Matrix([L/2,Z/(2*b),Zdot/(2*b),(-Ldot-H*L+u*Z/(2*b))/d])
check('exact_state_recovery',all(S.simplify(v)==0 for v in xrec-x))
R=S.Matrix([delta,L,Z]).jacobian(x)
# On H!=0, construct a right inverse of all three simultaneous readouts.
y0,y1,y2=S.symbols('delta L Z',real=True)
right_x=S.Matrix([y1/2,y2/(2*b),0,(d*y0+(2*Q-u*u)*y1/2+(3*H*u+Vp+4*b*d)*y2/(2*b))/(3*H*d)])
E=right_x.jacobian([y0,y1,y2])
check('exact_three_channel_right_inverse',all(S.simplify(z)==0 for z in R*E-S.eye(3)))
# Actual changes fail the SAME null identity, not just a different numerical output.
reject('omit_background_H_squared',S.expand(null-6*H*H*L)!=0)
reject('flip_lensing_derivative',S.expand(null-12*H*Ldot)!=0)
reject('omit_slip_matter_term',S.expand(null-4*d*Z)!=0)
reject('omit_slip_derivative',S.expand(null-u*Zdot/b)!=0)
reject('omit_velocity_from_momentum',S.expand(null_full.subs({n:ns,P:mom+d*v/2}))!=0)
# Evaluate the identity on every initial state using the existing full matrix T.
path=ROOT/'lab/process/k2367-sourced-fit-dust-transfer.json'
j=json.loads(path.read_text());back=j['details']['background_today'];aa,HH,uu,dd,V,V1,V2,dt,F,*_=back
bb=-1/np.sqrt(6); rows=[]
positive_target=S.Matrix([[2,S.Rational(1,5),S.Rational(1,10)],[S.Rational(1,5),1,S.Rational(3,20)],[S.Rational(1,10),S.Rational(3,20),S.Rational(1,2)]])
for k,want in [(1,S.Integer(2)),(2,S.Rational(49,25)),(3,S.Rational(931,1000))]:
    check('positive_target_principal_minor_'+str(k),positive_target[:k,:k].det()==want and want>0)
for z in j['details']['transfers']:
    k=z['k_over_Hstar']; qq=k*k/(aa*aa); T=np.array(z['transfer']);sub={H:HH,u:uu,d:dd,Q:qq,Vp:V1,b:bb}
    RR=np.array(R.subs(sub),float);OO=np.array(O.subs(sub),float);EE=np.array(E.subs(sub),float)
    # Stack (density, lensing, slip, lensing derivative, slip derivative).
    W=np.vstack([RR,OO[2:]])
    coeff=np.array([2*dd,2*qq-uu*uu+6*HH*HH,V1/bb+4*dd,6*HH,uu/bb])
    response=W@T; terms=coeff[:,None]*response; residual=terms.sum(axis=0)
    scale=max(1.,np.max(abs(terms)))
    check('same_fit_all_four_initial_columns_'+str(z['k_rd']),np.max(abs(residual))/scale<2e-13)
    check('same_fit_observability_'+str(z['k_rd']),abs(np.linalg.det(OO)/(8*bb*bb*dd)-1)<2e-13)
    check('same_fit_three_readout_right_inverse_'+str(z['k_rd']),np.max(abs(RR@EE-np.eye(3)))/max(1.,np.max(abs(RR)@abs(EE)))<2e-13)
    # A concrete positive target covariance, pulled back through actual dynamics.
    target=np.array([[2.,.2,.1],[.2,1.,.15],[.1,.15,.5]])
    exact_sub={key:S.Rational(str(value)) for key,value in sub.items()}
    def to_mp(mat): return mp.matrix([[mp.mpf(str(mat[i,j].evalf(75))) for j in range(mat.cols)] for i in range(mat.rows)])
    rmp=to_mp(R.subs(exact_sub)); emp=to_mp(E.subs(exact_sub)); tmp=mp.matrix([[mp.mpf(str(v)) for v in row] for row in T]); smp=mp.matrix(target.tolist())
    D=tmp**-1*emp; propagated_factor=rmp*(tmp*D); final=propagated_factor*smp*propagated_factor.T
    cov_error=float(max(abs(final[i,j]-smp[i,j]) for i in range(3) for j in range(3))/2)
    check('same_fit_positive_covariance_pullback_'+str(z['k_rd']),cov_error<1e-55)
    rows.append(dict(k_rd=z['k_rd'],all_seed_scaled_residual=float(np.max(abs(residual))/scale),observability_det=float(np.linalg.det(OO)),covariance_pullback_relative_error=float(cov_error)))
deps=['lab/process/k2367-sourced-fit-dust-transfer.json','explorations/conditional-build/k2367-sourced-fit-dust-transfer-2026-10-31.md',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(ROOT))]
out=dict(result_id='K2370',checks=len(checks),check_names=list(checks),changed_equation_controls=faults,details=dict(actual_same_fit_rows=rows),scope='Exact model-field identity and finite all-seed matrix/covariance controls; no observed-null, initial-spectrum, interval-domain or native GU claim',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
p=ROOT/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',out['checks'],len(faults))
