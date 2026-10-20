#!/usr/bin/env python3
"""Independent Fraction polynomial/moment/series replay; baseline precedes mutations."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[2]
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([v*c for v in a])
def mul(a,b):
    o=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):o[i+j]+=v*w
    return trim(o)
def deriv(a):return [F(i)*a[i] for i in range(1,len(a))] or [F(0)]
def moment(n):
    if n%2:return F(0)
    v=1
    for j in range(1,n,2):v*=j
    return F(v)
def G(p):return sum((v*moment(i) for i,v in enumerate(p)),F(0))
def hermite(n):
    a,b=[F(1)],[F(0),F(1)]
    if n==0:return a
    for k in range(1,n):a,b=b,add([F(0)]+b,scale(a,-k))
    return b
def hp(entries):
    p=[F(0)]
    for n,c in entries.items():p=add(p,scale(hermite(int(n)),F(c)))
    return p
def jet(a):return (a+[F(0)]*5)[:5]
def jm(a,b):return jet(mul(a,b))
def inv(a):
    a=jet(a);o=[1/a[0]]
    for n in range(1,5):o.append(-sum(a[j]*o[n-j] for j in range(1,n+1))/a[0])
    return o
def power(a,n):
    o=[F(1)]
    for _ in range(n):o=jm(o,a)
    return jet(o)
def check(m):
    u=hp(m['u_hermite']);v=hp(m['v_hermite']);hs=[[F(1)],u,v]
    ss=[[F(0)] for _ in range(5)]
    dd=[[F(0)] for _ in range(5)]
    for i in range(3):
        for j in range(3):
            ss[i+j]=add(ss[i+j],mul(hs[i],hs[j]))
            dd[i+j]=add(dd[i+j],mul(deriv(hs[i]),deriv(hs[j])))
    N=[G(p) for p in ss];B=[G([F(0)]*2+p) for p in ss];C=[G([F(0)]*4+p) for p in ss];D=[G(p) for p in dd]
    q=jet(add([F(3)],scale(jm(jm(C,N),power(inv(B),2)),-1)))
    M=jm(B,inv(N))
    J=jet(add(jm(M,add(add([F(2)],scale(M,-1)),scale(jm(D,inv(N)),4))),[F(-1)]))
    groups=0
    for name,value in {'N':N,'B':B,'C':C,'D':D,'q':q,'J':J}.items():
        assert value==list(map(F,m['jets'][name])),('jet',name,value);groups+=1
    c=F(m['constants']['quartic'])
    defect=jet(add(add(add(J,scale(power(q,2),-F(1,6))),scale(power(q,3),-F(1,4))),scale(power(q,4),-c)))
    assert defect==[0]*5,('quartic_trial',defect);groups+=1
    H3,H4=hermite(3),hermite(4)
    r0=[F(0)]*4+[F(3,2),F(0),F(-1),F(0),F(1,2)]
    r1=[F(0)]*6+[F(-3,2),F(0),F(3,2),F(0),F(-1,2)]
    assert G(r0)==42 and -G(mul(r0,H4))/24==-F(183,2) and G(r1)==-F(675,2);groups+=1
    rq=-G(mul(r0,H4))/24/216+G(r1)/1296
    px=-F(1,6)-F(6,72);p3=-F(9,6)-F(42,72)
    sq=px*px+p3*p3/6
    for name,value in [('residual_quartic',rq),('projection_x',px),('projection_h3',p3),('square_quartic',sq),('quartic',sq+rq)]:
        assert F(m['constants'][name])==value,(name,value);groups+=1
    assert G(mul(add(scale(hermite(1),-F(1,4)),scale(H3,-F(25,72))),add(scale(hermite(1),-F(1,4)),scale(H3,-F(25,72)))))==F(679,864),'score_profile_norm';groups+=1
    assert -G(mul(mul(H3,H3),H4))/24==-9 and G([F(0)]*2+mul(H3,H3))==42;groups+=1
    for n,target in [(6,-15),(8,-210),(10,-3150)]:
        assert -G([F(0)]*n+H4)/24==target,('moment_response',n);groups+=1
    # Inverse with q=sqrt(6)z+bz²+c sqrt(6)z³; coefficient z4 is 2c-317/24.
    assert 2*F(m['constants']['inverse_b32'])==F(317,24),'budget_inverse';groups+=1
    qm=F(m['constants']['q_window'])
    assert 0<qm and 2*qm<=F(1,25) and F(2,3)*(1+4*qm)<1,'window'
    assert 1-6*qm>=F(1,2) and 2*(1+qm*qm*(1+2*qm)/6)<3,'tail_constants'
    e=F(m['constants']['tail_exponent'])
    assert e>0 and F(1,2)-4*e*e>=0,'tail quadratic coefficient'
    assert 4*e-3+9*(F(1,2)-4*e*e)>=0,'exterior supersolution at |x|=3'
    assert F(m['constants']['tail_prefactor_log'])>=9*e,'boundary comparison normalization';groups+=1
    expected={'exact_optimizer_only_for_tail_and_moment_response':True,'quartic_value_asymptotic':True,'finite_q_quartic_error_bound':False,'second_density_profile':False,'gu_physics':False,'novelty':False,'formal_proof':False,'second_score_defect':True}
    assert m['scope']==expected,'reporting_scope'
    return groups
m=json.loads((ROOT/'lab/process/k1859-fisher-optimizer-tail-response.json').read_text())
count=check(m)
print(f'PASS clean independent baseline: {count} rational polynomial/series/constant groups')
faults=[('u_hermite','4','-1/47'),('v_hermite','2','-1/49'),('v_hermite','4','-1/63'),('v_hermite','6','1/217'),('v_hermite','8','1/4609'),('constants','quartic','1/9'),('constants','projection_x','1/4'),('constants','projection_h3','-25/13'),('constants','residual_quartic','197/288'),('constants','inverse_b32','317/47'),('constants','tail_exponent','1/3'),('constants','q_window','1/10')]
for section,key,value in faults:
    bad=deepcopy(m);bad[section][key]=value
    try:check(bad)
    except AssertionError as e:print('DETECTED input fault',section,key,str(e))
    else:raise AssertionError(('undetected_input',section,key))
for flag in ['exact_optimizer_only_for_tail_and_moment_response','finite_q_quartic_error_bound','second_density_profile','gu_physics']:
    bad=deepcopy(m);bad['scope'][flag]=not bad['scope'][flag]
    try:check(bad)
    except AssertionError as e:print('DETECTED reporting fault',flag,str(e))
    else:raise AssertionError(('undetected_reporting',flag))
print(f'PASS {len(faults)} mathematical-input faults and 4 reporting faults; no crashes counted as detection')
