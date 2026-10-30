#!/usr/bin/env python3
"""Exact controls and separately typed certificates; universal proofs in companion note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
checks={}
STEM='k2283-global-quadratic-cosmology'
NOTE=f'explorations/conditional-build/{STEM}-2026-10-30.md'
DEPS=['explorations/conditional-build/k2280-shared-coefficient-cosmology-survivor-2026-10-29.md', 'explorations/conditional-build/k2271-forward-cosmology-domain-2026-10-29.md', 'lab/process/k2277-multibin-pure-r2-test.json']

from flint import arb,arb_mat,ctx
from fractions import Fraction as F
ctx.prec=120
u,p,A,B=s.symbols('u p A B',positive=True);a,rr=s.symbols('a rr',real=True)
force=a/(36*u**R(1,3))-rr/(216*u**R(5,3))
def flow(expr):return s.diff(expr,u)*p+s.diff(expr,p)*(p+force)
FF=12*u**R(1,3)*(u-p)-a
coef=p/(3*u)-a/(36*u**R(4,3));delta=a*a-2*rr
E=p*p/2+A*u**R(2,3)/24+B*u**(-R(2,3))/144
Es=flow(E).subs({a:-A,rr:-B})
checks['energy_growth_identity']=s.simplify(Es-p*p)==0
checks['F_integrating_factor_identity']=s.simplify(flow(FF)-coef*FF+delta/(36*u**R(4,3)))==0
checks['coercive_potential_minimum']=s.simplify(2*s.sqrt(A*B/(24*144))-s.sqrt(6*A*B)/72)==0
checks['initial_positive_F_threshold']=s.simplify(FF.subs({u:2,a:-A,p:2+A/(12*2**R(1,3))}))==0
for dval,rval in [(1,R(0)),(0,R(1,2)),(-1,R(1))]:
 checks[f'crossing_sign_{dval}']=delta.subs({a:1,rr:rval})==dval
source=json.loads((ROOT/DEPS[-1]).read_text())['source_inputs']
for i,row in enumerate(source['files']):checks[f'source_hash_{i}']=hashlib.sha256(row['text'].encode()).hexdigest()==row['sha256']
rows=[l.split() for l in source['files'][0]['text'].splitlines() if l and not l.startswith('#')]
cs=[l.split() for l in source['files'][1]['text'].splitlines()]
Cexact=s.Matrix([[R(v) for v in row] for row in cs])
checks['all_observable_labels']=[(x[0],x[2]) for x in rows]==[('0.29500000', 'DV_over_rs'), ('0.51000000', 'DM_over_rs'), ('0.51000000', 'DH_over_rs'), ('0.70600000', 'DM_over_rs'), ('0.70600000', 'DH_over_rs'), ('0.93400000', 'DM_over_rs'), ('0.93400000', 'DH_over_rs'), ('1.32100000', 'DM_over_rs'), ('1.32100000', 'DH_over_rs'), ('1.48400000', 'DM_over_rs'), ('1.48400000', 'DH_over_rs'), ('2.33', 'DH_over_rs'), ('2.33', 'DM_over_rs')]
checks['full13_rows']=len(rows)==13 and len(cs)==13
for n in range(1,14):checks[f'covariance_SPD_{n}']=bool(Cexact[:n,:n].det()>0)
checks['covariance_symmetric']=Cexact==Cexact.T
checks['cross_covariance_retained']=Cexact[1,2]==R('-.0326062007') and Cexact[3,4]==R('-.0237445646')
t=s.symbols('t',positive=True);g=a/(36*t*t*u**R(1,3))-rr/(216*t*t*u**R(5,3));gu=s.diff(g,u);k=1/(3*(t*u)**R(2,3));kp=-R(2,3)*k*(1/t+p/u)
checks['quadrature_remainder_identity']=s.simplify(s.diff(k,t)+s.diff(k,u)*p-kp)==0
checks['full00_identity']=s.simplify(-108*t*t*u**R(5,3)*g+3*a*u**R(4,3)-rr/2)==0
# The same mathematical predicates test baseline and changed formulas/data.
def oracle(force_term=force,F_coefficient=coef,delta_term=delta,energy=E,jacobian=k,cov=Cexact):
 es=s.diff(energy,u)*p+s.diff(energy,p)*(p+force_term)
 fd=s.diff(FF,u)*p+s.diff(FF,p)*(p+force_term)
 return {'energy':s.simplify(es.subs({a:-A,rr:-B})-p*p)==0,
 'F_identity':s.simplify(fd-F_coefficient*FF+delta_term/(36*u**R(4,3)))==0,
 'distance':s.simplify(jacobian*3*t**R(2,3)*u**R(2,3)-1)==0,
 'cross_covariance':cov[1,2]==R('-.0326062007')}
checks.update({'oracle_'+k:bool(v) for k,v in oracle().items()});assert all(checks.values())
badc=Cexact.copy();badc[1,2]=badc[2,1]=0
mutants={'rho_force_sign':dict(force_term=force+rr/(108*u**R(5,3))), 'wrong_F_crossing':dict(delta_term=a*a+2*rr), 'missing_F_coefficient':dict(F_coefficient=p/(3*u)), 'missing_energy_barrier':dict(energy=E-B*u**(-R(2,3))/144),'missing_distance_jacobian':dict(jacobian=u**(-R(2,3))),'dropped_covariance':dict(cov=badc)}
failed_checks={name:[k for k,v in oracle(**kw).items() if not v] for name,kw in mutants.items()};faults={k:bool(v) for k,v in failed_checks.items()}
def cert(av, rv, sv, lv, radius='0', full=False):
    datarows = [l.split() for l in source['files'][0]['text'].splitlines() if l and (not l.startswith('#'))] if full else rows
    fullcs = [l.split() for l in source['files'][1]['text'].splitlines()]
    covariance = s.Matrix([[R(v) for v in row] for row in fullcs]) if full else Cexact
    A = arb(av, radius)
    RR = arb(rv, radius)
    UU = arb(2)
    VV = arb(sv, radius)
    M = arb(0)
    lam = arb(lv, radius)
    third = arb(1) / 3

    def g(t, u):
        return A / (36 * t * t * u ** third) - RR / (216 * t * t * u ** (5 * third))

    def gu(t, u):
        return -A / (108 * t * t * u ** (4 * third)) + 5 * RR / (648 * t * t * u ** (8 * third))

    def k(t, u):
        return 1 / (3 * (t * u) ** (2 * third))
    left = F(1)
    res = {}
    steps = 0
    for end in sorted(set([(1 + F(row[0])) ** 3 for row in datarows] + [F(8)])):
        n = int((end - left) * 2000) + 1
        hq = (end - left) / n
        h = arb(hq.numerator) / hq.denominator
        for i in range(n):
            tq = left + i * hq
            t = arb(tq.numerator) / tq.denominator
            T = t + arb(0).union(h)
            Uy = (UU - 4 * h).union(UU + 4 * h)
            Vy = (VV - 20 * h).union(VV + 20 * h)
            assert Uy > 1 and Vy > -4 and (Vy < 4), 'positive solution/velocity tube failure'
            gg = g(T, Uy)
            assert gg > -20 and gg < 20, 'acceleration first-exit failure'
            UU, VV, M = (UU + h * VV + h * h * gg / 2, VV + h * g(t, UU) + h * h * (-2 * gg / T + gu(T, Uy) * Vy) / 2, M + h * k(t, UU) - h * h * third * k(T, Uy) * (1 / T + Vy / Uy))
            steps += 1
        left = end
        res[end] = (UU, VV, M, lam * UU ** (-2 * third))
    pred = []
    for zz, value, tag in datarows:
        U, V, m, hh = res[(1 + F(zz)) ** 3]
        mm = lam * m
        pred.append({'DM_over_rs': mm, 'DH_over_rs': hh, 'DV_over_rs': (arb(zz) * mm * mm * hh) ** third}[tag])

    def discrepancy(ids):
        mat = arb_mat([[arb(str(covariance[i, j])) for j in ids] for i in ids])
        residual = arb_mat([[pred[i] - arb(datarows[i][1])] for i in ids])
        return (residual.transpose() * mat.inv() * residual)[0, 0]
    ids = list(range(len(datarows)))
    endpointF=12*UU**third*(UU-arb(str(end))*VV)-A
    assert endpointF>0 and A<0 and RR<0, 'positive-F sign-domain certificate'
    return discrepancy(ids),steps,endpointF

def finish(extra):
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    assert all(faults.values()),faults
    paths=[NOTE,str(Path(__file__).relative_to(ROOT)),*DEPS]
    data=dict(schema_version='1.0',result_id=STEM.split('-')[0].upper(),claim_ceiling='conditional supplied model; no native GU, empirical confidence or hardware claim',evidence_kind='exact algebra/finite matrix controls; interval/resource certificates separately typed; universal proofs in companion note',checks=len(checks),check_names=list(checks),faults_caught=list(faults),mutation_failed_checks=failed_checks,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{STEM}.json'
    if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),certificates=extra)))

q,steps,ff=cert('-33.8','-1','.9303','50.04185',full=True)
qb,stepsb,fb=cert('-33.8','-1','.9303','50.04185',radius='1e-8',full=True)
checks['full13_rational_witness']=bool(q>arb('5.87') and q<arb('5.90'))
checks['full13_parameter_box']=bool(qb<6 and fb>123)
checks['endpoint_positive_F']=bool(ff>123)
checks['does_not_meet_radius4']=bool(q>4)
finish(dict(interval_certificates=dict(Q13=str(q),Q13_box=str(qb),endpoint_F=str(ff),box_endpoint_F=str(fb),cells=steps,box_cells=stepsb,parameter_radius='1e-8',precision_bits=120,criterion_squared_radius=6),source_commit=source['commit']))
