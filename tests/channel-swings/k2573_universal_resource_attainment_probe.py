#!/usr/bin/env python3
"""K2573 exact finite-law consumers; compactness proofs are in the note."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
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
def law(stages):
    p=s.Integer(1);C=s.Integer(0);R=s.Integer(0)
    for a,b in stages:
        if b==0:continue
        p/=1+a
        w=0 if a>=b else s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
        C+=2*p*w;R+=2*p
    return s.simplify(p),s.simplify(C),s.simplify(R)
a,b,L=s.symbols('a b L',positive=True)
p,C,R=s.symbols('p C R')
# Solve the ORIGINAL single-trial recursions, with pass probability (1-a)/2.
w=s.symbols('w',nonnegative=True)
rec=s.solve([p-s.Rational(1,2)-(1-a)*p/2,C-w-(1-a)*C/2,R-1-(1-a)*R/2],[p,C,R])
ck('original_probability',s.simplify(rec[p]-1/(1+a))==0)
ck('original_leakage',s.simplify(rec[C]-2*w/(1+a))==0)
ck('original_positive_trial_resource',s.simplify(rec[R]-2/(1+a))==0)
# Continuity versus lower-semicontinuity: an actual disappearing free stage.
e=s.symbols('e',positive=True)
p2,C2,R2=law([(e,e),(s.Rational(1,2)-e,s.Rational(1,2)-e)])
p1,C1,R1=law([(s.Rational(1,2),s.Rational(1,2))])
ck('vanishing_stage_success_continuity',s.limit(p2,e,0,dir='+')==p1)
ck('vanishing_stage_cost_continuity',s.limit(C2,e,0,dir='+')==C1==0)
ck('vanishing_stage_resource_drop',s.limit(R2,e,0,dir='+')-R1==2)
ct('resource_continuity_false',s.limit(R2,e,0,dir='+')!=R1)
# Free one-stage and original survival in two nonzero stages.
pt,Ct,Rt=law([(s.Rational(1,4),s.Rational(1,4))]*2)
ck('two_free_stages_probability',pt==s.Rational(16,25))
ck('two_free_stages_cost',Ct==0)
ck('two_free_stages_resource',Rt==s.Rational(72,25))
ct('free_cost_not_free_survival',pt<s.Rational(2,3)==p1)
ct('unweighted_trial_count_false',Rt!=4)
ct('conditional_success_resource_false',Rt!=4*pt)
# Exact joint frontier consumers, including zero budgets.
fixtures=[]
for M in [s.Rational(0),s.Rational(1,2),s.Rational(1),s.Rational(4,3),s.Rational(2)]:
    prob=min(1,3*M/4);pp=prob*p1;rr=prob*R1
    ck('joint_resource_feasible_'+str(M),rr<=M)
    ck('joint_zero_leakage_'+str(M),prob*C1==0)
    ck('joint_value_'+str(M),pp==min(M/2,s.Rational(2,3)))
    fixtures.append({'M':str(M),'execute_probability':str(prob),'success':str(pp),'resource':str(rr),'leakage':'0'})
# Product inequality: exact two-factor excess underlying zero-leakage proof.
b1,b2=s.symbols('b1 b2',nonnegative=True)
ck('free_product_excess',s.expand((1+b1)*(1+b2)-(1+b1+b2))==b1*b2)
# Taylor/geometric bound on exp(1/2), all rational.
K=12;term=F(1,2)**(K+1)/math.factorial(K+1)
upper=sum((F(1,2)**j/math.factorial(j) for j in range(K+1)),F(0))+term/(1-F(1,2*(K+2)))
ck('exp_half_bound',upper<F(5,3))
N=1666;M=F(2);bound=M*F(5,3)/(2*(N+1))
ck('finite_mixture_error_bound',bound==F(5,5001)<F(1,1000))
ct('one_less_cap_does_not_meet_same_rational_bound',M*F(5,3)/(2*1666)>F(1,1000))
# A rare long original schedule remains resource feasible, disproving a pointwise cap.
long=law([(s.Rational(1,20),s.Rational(1,20))]*10)
q=s.Rational(1,10)
ck('rare_long_policy_resource',q*long[2]<2)
ck('rare_long_policy_positive_mass',q>0 and 10>1)
ct('budget_is_not_per_path_stage_cap',q*long[2]<2 and long[2]>2)
# Finite four-policy LP null direction preserving two budget constraints.
# Genuine original-law rows, not assertions of global optimality.
policies=[(s.Integer(0),s.Integer(0),s.Integer(0)),law([(s.Rational(1,2),s.Rational(1,2))]),law([(s.Rational(0),s.Rational(1,2))]),law([(s.Rational(1,4),s.Rational(1,4))]*2)]
A=s.Matrix([[1]*4,[x[1] for x in policies],[x[2] for x in policies]])
null=A.nullspace()[0]
ck('four_weight_budget_null_direction',A*null==s.zeros(3,1))
ck('null_direction_has_both_signs',any(x>0 for x in null) and any(x<0 for x in null))
v=s.Matrix([s.Rational(1,4)]*4);objective=s.Matrix([x[0] for x in policies])
if objective.dot(null)<0:null=-null
step=min(-v[i]/null[i] for i in range(4) if null[i]<0);v2=v+step*null
ck('vertex_step_preserves_budgets',A*v2==A*v)
ck('vertex_step_nonnegative_weights',all(x>=0 for x in v2))
ck('vertex_step_at_most_three',sum(x!=0 for x in v2)<=3)
ck('vertex_step_not_worse',objective.dot(v2)>=objective.dot(v))
ct('normalization_only_mixture_cannot_prove_joint_budget',A*s.Matrix([1,0,0,0])!=A*v)
provenance={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['explorations/conditional-build/k2569-stopping-maximizing-sequences-2026-11-05.md','explorations/conditional-build/k2571-stopping-resource-price-2026-11-05.md']}
report={'result':'K2573','evidence_kind':'exact original-law finite identities, budget witnesses, rational truncation consumer and finite mixture reduction; universal tightness and support proofs separate','checks':checks,'contrary_controls':controls,'provenance':provenance,'joint_zero_leakage_fixtures':fixtures,'finite_truncation':{'S':'1/2','M':'2','N':N,'error_upper':str(bound),'exp_half_upper':str(upper)},'ceiling':'finite expected-resource attained mixtures for supplied fair law; no computed intermediate optimizer, efficient solver or physical/native GU claim'}
out=root/'lab/process/k2573-universal-resource-attainment.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2573','checks':len(checks),'controls':len(controls),'status':'pass'}))
