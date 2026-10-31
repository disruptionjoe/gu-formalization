from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as F
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def fault(k,v):
 faults[k]=bool(v)
 if not v:raise AssertionError('ineffective changed-input control: '+k)
def publish(st,details,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),altered_input_controls=faults,evidence_kind='exact symbolic/rational/native coefficient controls; universal theorems in companion proofs',details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps(dict(result_id=out['result_id'],checks=len(checks),faults=len(faults),details=details)))

backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';src=(R/backend).read_text();ns={'__file__':str(R/backend),'__name__':'selected_native_arithmetic'}
exec(compile(src[:src.index('def sparse_rank')],backend,'exec'),ns)
b=ns['blade'];w=ns['wedge_raw'];add=ns['fadd'];S=lambda v:ns['shiab'](v,('comm','symi','symi'));P=lambda u,v:w(u,v).get(ns['FULL'],{}).get(0,ns['ZERO'])
def scalar(v):
 assert v[1]==0
 return s.Rational(v[0].numerator,v[0].denominator)
dt={1:b(())};Vs=[{1:b((0,1))},{2:b((0,1))},{2:b(1)},{2:b(0)}]
e,h,x,y,ep,hp,xp,yp,xpp,ypp,k=s.symbols('e h x y ep hp xp yp xpp ypp k',real=True);qs=[e,h,x,y];qps=[ep,hp,xp,yp]
M=s.Matrix(4,4,lambda i,j:scalar(P(Vs[i],ns['hodge'](Vs[j]))));D=s.Matrix(4,4,lambda i,j:scalar(P(Vs[i],S(w(dt,Vs[j])))))
C=[[[scalar(P(Vs[i],S(w(Vs[j],Vs[l])))) for l in range(4)] for j in range(4)] for i in range(4)]
L=s.expand((s.Matrix(qs).T*M*s.Matrix(qs))[0]*k/2+(s.Matrix(qs).T*D*s.Matrix(qps))[0]/2+sum(C[i][j][l]*qs[i]*qs[j]*qs[l] for i in range(4) for j in range(4) for l in range(4))/3)
expect=k*(e*e-h*h+x*x-y*y)/2+e*yp+h*xp-s.Rational(4,3)*e*e*x-s.Rational(4,3)*e*h*y
check('all_native_mass_coefficients',M==s.diag(1,-1,1,-1))
check('all_native_derivative_coefficients',D==s.Matrix([[0,0,0,2],[0,0,2,0],[0,0,0,0],[0,0,0,0]]))
check('all64_native_cubic_coefficients_composed',s.expand(L-expect)==0)
def deriv(v):return sum(s.diff(v,a)*ap for a,ap in zip(qs,qps))+s.diff(v,xp)*xpp+s.diff(v,yp)*ypp
Eqs=[s.expand(s.diff(L,q)-deriv(s.diff(L,qp))) for q,qp in zip(qs,qps)]
expected=[(k-8*x/3)*e-4*y*h/3+yp,-k*h-4*y*e/3+xp,k*x-4*e*e/3-hp,-k*y-4*e*h/3-ep]
check('four_Euler_equations',all(s.simplify(a-b)==0 for a,b in zip(Eqs,expected)))
a=k-s.Rational(8,3)*x;A=s.Matrix([[a,-4*y/3],[-4*y/3,-k]]);Delta=s.factor(A.det());bvec=s.Matrix([yp,xp]);sol=s.simplify(-A.inv()*bvec);ee,hh=sol
check('auxiliary_inverse',all(s.simplify(z)==0 for z in A*sol+bvec))
Le=s.factor(L.subs({e:ee,h:hh}));reduced=[s.simplify(s.diff(Le,q)-deriv(s.diff(Le,qp))) for q,qp in [(x,xp),(y,yp)]]
ported=[k*x-4*ee*ee/3-deriv(hh),-k*y-4*ee*hh/3-deriv(ee)]
check('full_reduced_derivative_equivalence',all(s.simplify(v-u)==0 for v,u in zip(reduced,ported)))
principal=s.Matrix(2,2,lambda i,j:s.simplify(s.diff(reduced[i],[xpp,ypp][j])));Pexp=s.Matrix([[a,4*y/3],[4*y/3,-k]])/Delta
check('principal_matrix',principal.applyfunc(s.factor)==Pexp.applyfunc(s.factor))
check('principal_determinant',s.simplify(principal.det()-1/Delta)==0)
v={k:1,x:s.Rational(3,8),y:s.Rational(3,4)}
check('line_zero_full_block_regular',a.subs(v)==0 and Delta.subs(v)==-1 and A.subs(v)==s.Matrix([[0,-1],[-1,-1]]))
def transverse(Z):
 mass=k*sum(scalar(P(Z,ns['hodge'](Vi)))*qi for Vi,qi in zip(Vs,qs))
 dd=sum((scalar(P(Z,S(w(dt,Vi))))-scalar(P(Vi,S(w(dt,Z)))))*qpi/2 for Vi,qpi in zip(Vs,qps))
 cubic=sum((scalar(P(Z,S(w(Vi,Vj))))+scalar(P(Vi,S(add(w(Z,Vj),w(Vj,Z))))))*qi*qj/3 for Vi,qi in zip(Vs,qs) for Vj,qj in zip(Vs,qs))
 return s.expand(mass+dd+cubic)
Rz1=transverse({1:b(1)});Rz=transverse({1:b(0)});Rz2=transverse({4:b(2)});Rf=transverse({4:b((1,2))});Rg=transverse({4:b((0,2))})
check('native_transverse_hsquare',Rz==s.Rational(4,3)*h*h)
check('native_transverse_y_square',Rz2==hp+s.Rational(4,3)*y*y)
check('native_transverse_ex_hy',Rf==-s.Rational(4,3)*(e*x+h*y))
check('native_transverse_xprime',Rg==-xp)
const={k:4,e:3,h:3,x:3,y:-3,ep:0,hp:0,xp:0,yp:0}
check('rational_singular_restricted_stationarity',all(eq.subs(const)==0 for eq in Eqs) and Delta.subs(const)==0)
check('rational_full_Euler_failure',Rz.subs(const)==Rz2.subs(const)==12)
check('third_native_transverse_control',Rz1==s.Rational(4,3)*e*h and Rz1.subs(const)==12)
# Smooth pulse via rational hyperbolic parametrization z=exp(kt)>0.
z=s.symbols('z',positive=True);sech=2*z/(1+z*z);tanh=(z*z-1)/(z*z+1);pulse=[3*k*sech/4,0,3*k*sech**2/4,3*k*sech*tanh/4];pp=[s.diff(q,z)*k*z for q in pulse];subs=dict(zip(qs+qps,pulse+pp))
check('three_field_pulse_stationary',all(s.factor(Eqs[i].subs(subs))==0 for i in [0,2,3]))
check('pulse_h_transverse_nonzero',s.factor(Eqs[1].subs(subs))!=0)
point={k:1,z:2};res=s.factor(Eqs[1].subs(subs));check('rational_pulse_residual',res.subs(point)==-s.Rational(108,125))
check('pulse_line_singular_crossing',s.simplify((1-2*sech**2).subs(z,1+s.sqrt(2)))==0)
# Polynomial ideal consequence: after h=y=0, ex=0 and kx=4e²/3 imply4e³/3=0 for k!=0.
check('nonzero_kappa_slice_exclusion',s.expand(k*(e*x)-e*(k*x-s.Rational(4,3)*e*e))==s.Rational(4,3)*e**3)
fault('drop_even_cross_coupling',s.diag(a,-k).subs(v).det()==0 and A.subs(v).det()!=0)
fault('discard_singular_restricted_branch',Delta.subs(const)==0 and all(eq.subs(const)==0 for eq in Eqs))
fault('suppress_transverse_receivers',all(eq.subs(const)==0 for eq in Eqs) and Rz.subs(const)!=0)
fault('promote_three_field_pulse',res.subs(point)!=0)
# Freeze inverse coefficients when differentiating e*,h*; real derivative debt remains.
freeze_h=s.diff(hh,xp)*xpp+s.diff(hh,yp)*ypp
fault('freeze_inverse_derivatives',s.simplify(deriv(hh)-freeze_h).subs({k:1,x:0,y:1,xp:1,yp:2})!=0)
fault('erase_native_cubic',s.expand(L-(k*(e*e-h*h+x*x-y*y)/2+e*yp+h*xp))!=0)
publish('k2354-native-mixed-euler-slice',dict(density=str(L),Delta=str(Delta),even_solution=[str(v) for v in sol],principal=str(principal),transverse_rows=[str(Rz),str(Rz2),str(Rf),str(Rg),str(Rz1)],rational_restricted_stationary={'kappa':4,'e':3,'h':3,'x':3,'y':-3},full_missing_row=12,scope='only zero full fixed-geometry stationary field in this real four-component flat slice for kappa!=0'),[backend,'explorations/conditional-build/k2351-mixed-parity-auxiliary-reduction-2026-10-30.md','lab/process/k2351-mixed-parity-auxiliary-reduction.json'])
