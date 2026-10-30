#!/usr/bin/env python3
"""Reproducible conditional controls; universal proof boundaries in companion note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]

from flint import arb,arb_mat,ctx
from fractions import Fraction as F
ctx.prec=120
STEM='k2280-shared-coefficient-cosmology-survivor'
NOTE=f'explorations/conditional-build/{STEM}-2026-10-29.md'
DEPS=['explorations/conditional-build/k2271-forward-cosmology-domain-2026-10-29.md','explorations/conditional-build/k2277-multibin-pure-r2-test-2026-10-29.md','lab/process/k2277-multibin-pure-r2-test.json']
source=json.loads((ROOT/DEPS[-1]).read_text())['source_inputs']
checks={}
for i,row in enumerate(source['files']):checks[f'source_hash_{i}']=hashlib.sha256(row['text'].encode()).hexdigest()==row['sha256']
rows=[l.split() for l in source['files'][0]['text'].splitlines() if l and not l.startswith('#')][:7]
expected=[('.295','DV_over_rs'),('.510','DM_over_rs'),('.510','DH_over_rs'),('.706','DM_over_rs'),('.706','DH_over_rs'),('.934','DM_over_rs'),('.934','DH_over_rs')]
def labels_ok(rr):return all(R(x[0])==R(e[0]) and x[2]==e[1] for x,e in zip(rr,expected))
checks['seven_data_labels']=labels_ok(rows)
cs=[l.split() for l in source['files'][1]['text'].splitlines()][:7]
Cexact=s.Matrix([[R(v) for v in row[:7]] for row in cs])
for n in range(1,8):checks[f'covariance_SPD_{n}']=bool(Cexact[:n,:n].det()>0)
checks['cross_covariance_retained']=Cexact[1,2]==R('-.0326062007') and Cexact[3,4]==R('-.0237445646')
t,u,v,a,rr=s.symbols('t u v a rr',positive=True)
g=a/(36*t*t*u**R(1,3))-rr/(216*t*t*u**R(5,3))
gu=-a/(108*t*t*u**R(4,3))+5*rr/(648*t*t*u**R(8,3))
k=1/(3*(t*u)**R(2,3));kp=-R(2,3)*k*(1/t+v/u)
checks['general_g_derivative']=s.simplify(s.diff(g,u)-gu)==0
checks['g_time_derivative']=s.simplify(s.diff(g,t)+2*g/t)==0
checks['distance_second_derivative']=s.simplify(s.diff(k,t)+s.diff(k,u)*v-kp)==0
x=s.symbols('x',positive=True);f=s.Function('U');y=f(x**3)**R(4,3)
Q=18*x*y*s.diff(y,x)+R(9,4)*x*x*s.diff(y,x)**2-9*x*x*y*s.diff(y,x,2)
checks['full_constraint_substitution']=s.simplify(Q+108*x**6*f(x**3)**R(5,3)*s.Subs(s.diff(f(t),t,2),t,x**3))==0
checks['general_full00_RHS']=s.simplify(-108*t*t*u**R(5,3)*g+3*a*u**R(4,3)-rr/2)==0
# Same independent predicates on baseline and genuinely changed mathematical inputs.
z,mm,hh=s.symbols('z mm hh',positive=True)
def algebra_checks(g_in=g,gu_in=gu,k_in=k,C_in=Cexact,rows_in=rows,dv_cube=z*mm**2*hh):
    return dict(full00=s.simplify(-108*t*t*u**R(5,3)*g_in+3*a*u**R(4,3)-rr/2)==0,
      general_derivative=s.simplify(s.diff(g,u)-gu_in)==0,
      distance_jacobian=s.simplify(k_in*3*t**R(2,3)*u**R(2,3)-1)==0,
      covariance=C_in[1,2]==R('-.0326062007'),labels=labels_ok(rows_in),
      volume_distance=s.simplify(dv_cube-z*mm**2*hh)==0)
checks.update({'oracle_'+key:bool(value) for key,value in algebra_checks().items()})
assert all(checks.values()),checks
badC=Cexact.copy();badC[1,2]=badC[2,1]=0
wrong=[list(row) for row in rows];wrong[1][2]='DH_over_rs'
mutants={
 'wrong_rho_sign':dict(g_in=g+rr/(108*t*t*u**R(5,3))),
 'lost_general_derivative_term':dict(gu_in=gu-5*rr/(648*t*t*u**R(8,3))),
 'lost_distance_Jacobian':dict(k_in=u**(-R(2,3))),
 'shifted_observable_label':dict(rows_in=wrong),
 'dropped_covariance_cross_term':dict(C_in=badC),
 'wrong_DV_formula':dict(dv_cube=z*mm*hh)}
failed_checks={name:[key for key,value in algebra_checks(**args).items() if not value] for name,args in mutants.items()}
faults={name:bool(failed) for name,failed in failed_checks.items()}

def cert(av,rv,sv,lv,radius='0',full=False):
    datarows=([l.split() for l in source['files'][0]['text'].splitlines() if l and not l.startswith('#')] if full else rows)
    fullcs=[l.split() for l in source['files'][1]['text'].splitlines()]
    covariance=s.Matrix([[R(v) for v in row] for row in fullcs]) if full else Cexact
    A=arb(av,radius);RR=arb(rv,radius);UU=arb(2);VV=arb(sv,radius);M=arb(0);lam=arb(lv,radius);third=arb(1)/3
    def g(t,u):return A/(36*t*t*u**third)-RR/(216*t*t*u**(5*third))
    def gu(t,u):return -A/(108*t*t*u**(4*third))+5*RR/(648*t*t*u**(8*third))
    def k(t,u):return 1/(3*(t*u)**(2*third))
    left=F(1);res={};steps=0
    for end in sorted(set([(1+F(row[0]))**3 for row in datarows]+[F(8)])):
        n=int((end-left)*2000)+1;hq=(end-left)/n;h=arb(hq.numerator)/hq.denominator
        for i in range(n):
            tq=left+i*hq;t=arb(tq.numerator)/tq.denominator;T=t+arb(0).union(h)
            Uy=(UU-4*h).union(UU+4*h);Vy=(VV-20*h).union(VV+20*h)
            assert Uy>1 and Vy>-4 and Vy<4,'positive solution/velocity tube failure'
            gg=g(T,Uy);assert gg>-20 and gg<20,'acceleration first-exit failure'
            Fb=12*Uy**third*(Uy-T*Vy)-A;assert Fb>0,'whole-cell F failure'
            UU,VV,M=UU+h*VV+h*h*gg/2,VV+h*g(t,UU)+h*h*(-2*gg/T+gu(T,Uy)*Vy)/2,M+h*k(t,UU)-h*h*third*k(T,Uy)*(1/T+Vy/Uy)
            steps+=1
        left=end;res[end]=(UU,VV,M,lam*UU**(-2*third))
    pred=[]
    for zz,value,tag in datarows:
        U,V,m,hh=res[(1+F(zz))**3];mm=lam*m
        pred.append({'DM_over_rs':mm,'DH_over_rs':hh,'DV_over_rs':(arb(zz)*mm*mm*hh)**third}[tag])
    def discrepancy(ids):
        mat=arb_mat([[arb(str(covariance[i,j])) for j in ids] for i in ids]);residual=arb_mat([[pred[i]-arb(datarows[i][1])] for i in ids])
        return (residual.transpose()*mat.inv()*residual)[0,0]
    ids=list(range(len(datarows)))
    mat=arb_mat([[arb(str(covariance[i,j])) for j in ids] for i in ids]);inv=mat.inv()
    data=arb_mat([[arb(row[1])] for row in datarows]);shape=arb_mat([[v] for v in pred])
    cross=(shape.transpose()*inv*data)[0,0];norm=(shape.transpose()*inv*shape)[0,0]
    assert cross>0 and norm>0,'positive common-ruler minimizer'
    prof=(data.transpose()*inv*data)[0,0]-cross*cross/norm
    return discrepancy(ids),discrepancy([1,2,6]),steps,prof
q7,q3,steps,_=cert('-258.39','-5000','-.39968','44.1733')
checks['seven_coordinate_interval_survivor']=bool(q7>3 and q7<arb(16)/5)
qn,_,stepsn,_=cert('-258.39','-5000','-.39968','44.1733','1e-8')
checks['shared_parameter_box_survivor']=bool(qn<arb(16)/5)
qo,qold,stepso,_=cert('-69','0','1.48','54.3')
checks['original_three_survivor']=bool(qold<arb(1)/50)
checks['additional_data_discriminate_old_witness']=bool(qo>17)

fullcs=[l.split() for l in source['files'][1]['text'].splitlines()]
fullC=s.Matrix([[R(v) for v in row] for row in fullcs])
for n in range(8,14):checks[f'full_covariance_SPD_{n}']=bool(fullC[:n,:n].det()>0)
qfull,_,stepsfull,prof=cert('-258.39','-5000','-.39968','44.1733',full=True)
checks['full_domain_fixed_shape_rejected']=bool(qfull>10000)
checks['all_ruler_fixed_shape_rejected']=bool(prof>7000)

def finish(result_id,stem,note,deps,checks,faults,extra):
    assert all(checks.values()), [k for k,v in checks.items() if not v]
    assert all(faults.values()), [k for k,v in faults.items() if not v]
    paths=[note,str(Path(__file__).relative_to(ROOT)),*deps]
    data=dict(schema_version='1.0',result_id=result_id,claim_ceiling='conditional supplied model; no native GU, empirical confidence or hardware claim',evidence_kind='exact algebra/finite operator controls plus separately identified interval and resource certificates; universal proofs in note',checks=len(checks),check_names=list(checks),faults_caught=list(faults),dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{stem}.json'
    if '--write' in sys.argv: out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else: assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=result_id,checks=len(checks),faults=len(faults),certificates=extra),default=str))

finish('K2280',STEM,NOTE,DEPS,checks,faults,dict(interval_certificates={'cells_per_run':steps,'parameter_box_cells':stepsn,'comparison_cells':stepso,'parameter_box_radius':'1e-8','Q7':str(q7),'Q7_box':str(qn),'comparison_Q7':str(qo),'comparison_Q3':str(qold),'precision_bits':120,'full_data_cells':stepsfull,'full_data_Q':str(qfull),'full_data_profiled_Q':str(prof),'full_domain_z_max':'2.33'},source_commit=source['commit'],mutation_failed_checks=failed_checks))
