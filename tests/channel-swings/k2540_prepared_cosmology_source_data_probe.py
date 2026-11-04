"""Original-equation jet and preparation checks; uniform proof is in companion note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,p):
 bank[name]=bool(p)
 if not p:raise AssertionError('FAIL '+name)
t,O,a,x,y,d=s.symbols('t O a x y d',positive=True);Ds=lambda z:t*s.diff(z,t)
v=3*O/4;L=1-O+O*t;r=L**s.Rational(3,4)
bref=6*a*(1-O)-s.Rational(81,2)*O**2-72*(1-v)*O
b=bref+72*(O-3)*d;y0=v+d;F0=a+12*(1-y0);q0=3*F0*O
N=b+2*q0*t;F=y-a*x**(-s.Rational(1,3))/36+N*x**(-s.Rational(5,3))/216
FG=a+12*x**s.Rational(1,3)*(x-y)
FGs=s.diff(FG,x)*y+s.diff(FG,y)*F
original00=3*FG*x**s.Rational(4,3)-q0*t-(FG-a)**2/4-b/2-9*x**s.Rational(4,3)*FGs
ck(checks,'original00_full_identity',s.simplify(original00)==0)
seed={t:1,x:1,y:y0};rj=[r]
for i in range(4):rj.append(s.factor(Ds(rj[-1])))
rj=[s.factor(z.subs(t,1)) for z in rj]
x2=s.factor(F.subs(seed));x3=s.factor((Ds(F)+s.diff(F,x)*y+F).subs(seed))
x4=s.factor((Ds(Ds(F))+2*Ds(s.diff(F,x))*y+s.diff(F,x,2)*y*y+s.diff(F,x)*F).subs(seed)+x3)
d0=O/3+O**2/8;A=a/27-11*O/12-5*O**2/16;B=2*a/3-9*O-12
ck(checks,'source_normalized_once',s.expand(N-b-6*F0*O*t)==0)
ck(checks,'second_jet_exact',s.factor(x2-rj[2])==0)
third=s.factor(x3-rj[3]);ck(checks,'third_jet_polynomial',s.expand(third-d0+A*d-s.Rational(5,3)*d*d)==0)
# Derive proper-time snap from H=x^(2/3), Dt=-3H Ds.
j=s.symbols('j0:5',positive=True);DS=lambda z:sum(s.diff(z,j[i])*j[i+1] for i in range(4));H=j[0]**s.Rational(2,3);DT=lambda z:s.expand(-3*H*DS(z))
Hd=DT(H);Hdd=DT(Hd);Hddd=DT(Hdd)
snap=s.simplify(1+6*Hd/H**2+3*(Hd/H**2)**2+4*Hdd/H**3+Hddd/H**4)
expected=1-12*j[1]/j[0]+24*j[2]/j[0]+20*j[1]**2/j[0]**2-30*j[1]*j[2]/j[0]**2-18*j[3]/j[0]
ck(checks,'proper_time_snap_formula',s.simplify(snap-expected)==0)
sgap=s.factor(snap.subs(dict(zip(j[:4],[1,y0,x2,x3])))-snap.subs(dict(zip(j[:4],rj[:4]))))
ck(checks,'exact_snap_polynomial',s.expand(sgap+18*d0-B*d+10*d*d)==0)
# Small-root algebra evaluated before rewriting to numerically stable rationalized form.
d3=(A-s.sqrt(A*A-s.Rational(20,3)*d0))/(s.Rational(10,3));dS=(B-s.sqrt(B*B-720*d0))/20
ck(checks,'third_jet_small_root',s.simplify(third.subs(d,d3))==0)
ck(checks,'snap_small_root',s.simplify(sgap.subs(d,dS))==0)
ck(checks,'third_stable_root',s.simplify(d3-2*d0/(A+s.sqrt(A*A-s.Rational(20,3)*d0)))==0)
ck(checks,'snap_stable_root',s.simplify(dS-36*d0/(B+s.sqrt(B*B-720*d0)))==0)
for name,root in [('third',d3),('snap',dS)]:
 ck(checks,name+'_leading_initial_shift',s.limit(a*root,a,s.oo)==27*d0)
# Independent slow-profile identities and residual coefficient cancellations.
g0=(bref-6*a*(1-O))/216+(1-v)*O*t/3
f=(x**(-s.Rational(1,3))-L*x**(-s.Rational(5,3)))/36
h=Ds(r)-Ds(Ds(r))+g0*x**(-s.Rational(5,3));h0=s.factor(h.subs(x,r));c=s.factor(s.diff(f,x).subs(x,r));p=s.factor(h0/c)
kforce=(-1+O*(1-t)/3)*x**(-s.Rational(5,3))
ck(checks,'original_modified_force',s.simplify(s.diff(F,d)-kforce)==0)
ck(checks,'preparation_velocity_matches_slow_profile',s.simplify(Ds(p).subs(t,1)-27*d0)==0)
hu=s.diff(h,x).subs(x,r);fuu=s.diff(f,x,2).subs(x,r);k0=kforce.subs(x,r)
tslow=(hu*p+27*d0*k0-Ds(Ds(p))+Ds(p)-fuu*p*p/2)/c
ck(checks,'second_slow_residual_cancellation',s.simplify(Ds(Ds(p))-Ds(p)+c*tslow+fuu*p*p/2-hu*p-27*d0*k0)==0)
ck(checks,'second_slow_initial_position',s.simplify(tslow.subs(t,1)+27*Ds(Ds(p)).subs(t,1))==0)
e=s.symbols('e',real=True);four=s.factor(s.limit((x4-rj[4]).subs(d,27*d0/a+e/a**2),a,s.oo));target=O*(16+16*O-3*O*O)/48
ck(checks,'fourth_jet_limit_independent_subleading_shift',s.simplify(four-target)==0)
ck(checks,'fourth_jet_vs_fast_profile',s.simplify(four-Ds(Ds(p)).subs(t,1)/27)==0)
ck(checks,'Omega03_fourth_gap',four.subs(O,s.Rational(3,10))==s.Rational(2053,16000))
# Error-budget consumer, not a claim about an instrument.
weights=[1,-4,6,-4,1];ck(checks,'fourth_difference_normalization',sum(weights[i]*i**4 for i in range(5))==24)
ck(checks,'five_sample_error_sharp',sum(abs(x) for x in weights)==16)
ck(checks,'required_noise_scaling',s.simplify(a**(-2)/(a**(-s.Rational(1,2)))**4)==1)
ck(controls,'old_fixed_seed_snap_gap_survives',sgap.subs(d,0)==-18*d0)
ck(controls,'b_fixed_would_change_second_jet',s.simplify(x2-72*(O-3)*d/216-rj[2])!=0)
ck(controls,'dimensionful_source_changes',s.diff(q0,d)==-36*O)
ck(controls,'third_and_snap_roots_are_distinct',s.rem(s.Poly(sgap,d),s.Poly(third,d)).as_expr()!=0)
ck(controls,'C4_not_closed',four.subs(O,s.Rational(3,10))>0)
report={'result':'K2540','exact_checks':checks,'contrary_controls':controls,'scope':'same sourced quadratic family with altered initialization and dimensional source, fixed action-normalized Omega; exact observer snap repair and compact-interval C3 not C4 closure; no empirical/native GU credit','identities':{'third_gap':str(third),'snap_gap':str(sgap),'fourth_gap_limit':str(four),'slow_velocity':str(27*d0),'b_shift':str(72*(O-3)*d)},'dependencies':{q:hashlib.sha256((R/q).read_bytes()).hexdigest() for q in ['tests/channel-swings/k2538_derivative_limit_and_snap_probe.py',str(Path(__file__).relative_to(R))]}}
out=R/'lab/process/k2540-prepared-cosmology-source-data.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print('K2540',len(checks),'exact groups',len(controls),'contrary controls')
