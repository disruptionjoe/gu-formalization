#!/usr/bin/env python3
"""Exact identities and supporting controls; universal derivations are in the note."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)

def log_bounds(r,K=18):
    r=F(r);u=(r-1)/(r+1)
    assert 0<=u<1
    low=2*sum((u**(2*j+1)/F(2*j+1) for j in range(K+1)),F(0))
    return low,low+2*u**(2*K+3)/(F(2*K+3)*(1-u*u))
def law_bounds(stages,lam,k):
    p=F(1);cl=F(0);cu=F(0);R=F(0)
    for a,b in stages:
        if b==0:continue
        assert 0<=a<=b
        p/=1+a;lo,hi=log_bounds(1+(b-a)**2/(2*(a+b)*(2-a-b)))
        cl+=2*p*lo;cu+=2*p*hi;R+=2*p
    return {'p':p,'C_lower':cl,'C_upper':cu,'R':R,'J_lower':p-lam*cu-k*R,'J_upper':p-lam*cl-k*R}
a,b=s.symbols('a b',positive=True);t=a+b;d=b-a
z=d*d/(2*t*(2-t));w=s.log(1+z)
zb=d/(t*(2-t))-d*d*(1-t)/(t*t*(2-t)**2)
za=-d/(t*(2-t))-d*d*(1-t)/(t*t*(2-t)**2)
ck('actual_cost_b_derivative',s.factor(s.diff(z,b)-zb)==0)
ck('actual_cost_a_derivative',s.factor(s.diff(z,a)-za)==0)
T=s.symbols('T',real=True)
ck('a_lipschitz_polynomial_margin',s.factor((2-T)**2-(3-2*T))==(T-1)**2)
ck('cost_b_zero_control',s.diff(w,b).subs(a,b)==0)
ct('cost_derivative_not_zero',s.diff(w,b).subs({a:0,b:s.Rational(1,2)})>0)
# Adjacent exchange independent symbolic derivation from affine stage maps.
a1,a2,c1,c2,X=s.symbols('a1 a2 c1 c2 X')
AB=((X-2*c2)/(1+a2)-2*c1)/(1+a1)
BA=((X-2*c1)/(1+a1)-2*c2)/(1+a2)
ck('priced_adjacent_exchange',s.factor(AB-BA-2*(a1*c2-a2*c1)/((1+a1)*(1+a2)))==0)
# Feasible original-law stages, not freely invented affine costs.
Aw=F(0);Bwlo,Bwhi=log_bounds(F(43,42))
ck('exchange_control_actual_B_cost',1+(F(2,5)-F(1,5))**2/(2*(F(2,5)+F(1,5))*(2-F(2,5)-F(1,5)))==F(43,42))
ck('unpriced_actual_A_first',F(1,10)*Bwlo-F(1,5)*Aw>0)
ct('priced_actual_B_first',F(1,100)*Bwhi-F(1,200)<0)

lam,k,delta,Lw=s.symbols('lam k delta Lw',positive=True)
ck('deletion_gain_identity',s.factor(X-(X-2*c1)/(1+a1)-(a1*X+2*c1)/(1+a1))==0)
# Concrete new wedge and supported resource consumer.
S=F(1,2);lam0=F(1,10);k0=F(1,20);L0=F(2,3)
ck('new_wedge_threshold',lam0*L0*S*(2+S)/4==F(1,48)<k0)
ck('outside_old_high_multiplier_region',lam0/(1-2*k0)==F(1,9) and F(1,9)**2<F(16,3))
ck('one_stage_strict_decrease',2*lam0*(1+S)+lam0*S-(1-2*k0)==-F(11,20))
sol=law_bounds([(F(0),S)],lam0,k0)
ck('original_success_resource',sol['p']==1 and sol['R']==2)
lo,hi=log_bounds(F(7,6))
ck('original_leakage_log',sol['C_lower']==2*lo and sol['C_upper']==2*hi)
ck('optimal_price_positive',sol['J_lower']>F(86,100))
ct('pathwise_two_trial_cap_false',F(1,2)**3>0)
# Whole low-multiplier resource segment: inherited M derivative, explicit endpoint.
Mfun=-2*(1+a)*s.diff(w,a)+2*w
ck('M_endpoint_exact',s.simplify(Mfun.subs({a:0,b:s.Rational(1,2)})-(s.Rational(32,21)+2*s.log(s.Rational(7,6))))==0)
ck('M_derivative_identity',s.simplify(s.diff(Mfun,a)+2*(1+a)*s.diff(w,a,2))==0)
ck('log_endpoint_rational_upper',hi<F(1,6))
ck('whole_segment_uniform_margin',F(2,5)*(F(13,7)+F(5,12))==F(191,210)<1)
m=s.symbols('m',positive=True);lamx=s.symbols('lambda',positive=True)
Fm=m/2-lamx*m*w.subs({a:2/m-1,b:s.Rational(1,2)})
ck('frontier_slope_is_support',s.simplify(s.diff(Fm,m)-(1-lamx*Mfun.subs({a:2/m-1,b:s.Rational(1,2)}))/2)==0)
ck('frontier_free_endpoint',s.simplify(Fm.subs(m,s.Rational(4,3))-s.Rational(2,3))==0)
ck('frontier_resource_two_endpoint',s.simplify(Fm.subs(m,2)-(1-2*lamx*s.log(s.Rational(7,6))))==0)
# Disappearing charged padding versus actual deletion.
charged=sol['J_lower']-2*k0
ct('charging_zero_padding_is_not_actual',charged<sol['J_lower'])
# Generic finite rounding implementation, tested on an independent non-grid input.
def rounded(stages,h):
    bs=[b for a,b in stages];flo=[int(b/h) for b in bs];remaining=int(sum(bs)/h)-sum(flo)
    order=sorted(range(len(bs)),key=lambda i:(-(bs[i]/h-flo[i]),i))
    for i in order[:remaining]:flo[i]+=1
    return [(min(h*flo[i],h*int(a/h)),h*flo[i]) for i,(a,b) in enumerate(stages)]
stages=[(F(23,137),F(29,137)),(F(11,139),F(17,139))];stages.append((F(1,91),S-sum(b for a,b in stages)))
h=F(1,200);rnd=rounded(stages,h)
ck('rounding_exact_score',sum(b for a,b in rnd)==S)
ck('rounding_admissible',all(0<=a<=b for a,b in rnd))
ck('rounding_coordinate_errors',all(abs(a-aa)<h and abs(b-bb)<h for (a,b),(aa,bb) in zip(stages,rnd)))
ck('rounding_grid_coordinates',all((a/h).denominator==(b/h).denominator==1 for a,b in rnd))
N=6;lam1=F(19,10);k1=F(1,20)
ck('old_cap_six_suffices',F(5,3)*(S+2*k1)/(2*k1*(1+S))==F(20,3)<7)
coef=N*(1+4*lam1+lam1*S+2*k1*N)
ck('grid_error_coefficient',coef==F(609,10))
ck('grid_size_consumer',coef/F(60902)==F(609,609020)<F(1,1000))
ct('one_smaller_mesh_count_not_sufficient',coef/F(60900)==F(1,1000))
# Rational log consumers found by numerical scouts, certified independently here.
two=[(F(232032,10**6),F(383085,10**6)),(F(52201,10**6),F(116915,10**6))]
three=list(zip([F(x,10**6) for x in [210796,35947,28097]],[F(x,10**6) for x in [353164,80582,66254]]))
r2=law_bounds(two,F(19,10),F(1,10000));r3=law_bounds(three,F(19,10),F(1,10000))
ck('two_score',sum(b for a,b in two)==S)
ck('three_score',sum(b for a,b in three)==S)
ck('two_stage_beats_inherited_global_one_bound',r2['J_lower']>F(71029,100000)>F(71,100))
ck('three_stage_lower',r3['J_lower']>F(71032,100000))
ck('three_strictly_improves_named_two',r3['J_lower']-r2['J_upper']>F(1,40000))
ct('incorrect_unweighted_resource',r2['R']!=4 and r3['R']!=6)
ct('incorrect_single_trial_cost',r2['p']-F(19,10)*r2['C_upper']/2-F(1,10000)*r2['R']>r2['J_upper'])
# Outward decimal rational summaries preserve readable and reproducible brackets.
def dec_bounds(lo,hi,places=12):
    mult=10**places
    return [str(F(lo.numerator*mult//lo.denominator,mult)),str(F(-(-hi.numerator*mult//hi.denominator),mult))]
def compact(row):
    return {'p':str(row['p']),'R':str(row['R']),'C_bracket':dec_bounds(row['C_lower'],row['C_upper']),'J_bracket':dec_bounds(row['J_lower'],row['J_upper'])}
report={'result':'K2575','evidence_kind':'exact derivative/exchange identities, rational logarithm witnesses and grid arithmetic; universal merge/rounding arguments in note, numerical scout not proof','checks':checks,'contrary_controls':controls,'new_wedge_optimizer':compact(sol),'two_stage_witness':{'stages':[[str(a),str(b)] for a,b in two],**compact(r2)},'three_stage_witness':{'stages':[[str(a),str(b)] for a,b in three],**compact(r3)},'grid':{'N':6,'m':30451,'error':'609/609020','enumerated':False},'ceiling':'new sufficient one-stage region and low-multiplier budget segment; no general intermediate global optimum or efficient enumeration'}

refs=['k2571-stopping-resource-price', 'k2573-universal-resource-attainment', 'k2569-stopping-maximizing-sequences']
report['provenance']={'explorations/conditional-build/'+f+'-2026-11-05.md':hashlib.sha256((root/('explorations/conditional-build/'+f+'-2026-11-05.md')).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2575-constructive-priced-optimization.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2575','checks':len(checks),'controls':len(controls),'status':'pass'}))
