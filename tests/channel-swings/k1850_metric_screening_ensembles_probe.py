#!/usr/bin/env python3
"""Independent Fraction stationary families and coefficient faults; no producer import."""
from pathlib import Path
from fractions import Fraction as F
import copy
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
r=json.loads((ROOT/'lab/process/k1850-metric-screening-ensembles.json').read_text())
n=0

def ck(value):
    global n
    assert value
    n+=1

def polynomial(coeff,x):
    y=F(0)
    for a in reversed(coeff): y=y*x+a
    return y

def derivative(coeff):
    return [i*a for i,a in enumerate(coeff)][1:]

def certificate(q):
    co={k:F(v) for k,v in q['action_coefficients'].items()}
    a=F(q['affine']['alpha']);h=F(q['affine']['shift_action_flux_factor'])
    z={k:F(v) for k,v in q['rational_control'].items()}
    den=z['rho']+3*z['c']*z['s']**2/z['nonlinear_flux']
    return (co=={'matter_vacuum':F(-1),'multiplier':F(-1),'top_form':F(1)}
        and a!=0 and h==-a
        and q['geometry']['dimension']==4
        and F(q['geometry']['ricci_factor'])==3
        and F(q['geometry']['scalar_factor'])==12
        and all(z[k]>0 for k in ['s','c','K','lambda','affine_flux','nonlinear_flux'])
        and z['rho']>=0
        and z['lambda']+z['rho']==3*z['K']/z['s']
        and z['c']*z['s']**2==a*z['affine_flux']
        and z['c']*z['s']**2==z['lambda']*z['nonlinear_flux']
        and z['nonlinear_ds_drho']==-z['s']/den
        and z['nonlinear_dR_drho']==12/(z['s']*den))

ck(certificate(r))
# Independent family construction, with K solved from the actual metric row.
for s0 in [F(1,2),F(2),F(7,3)]:
    for c0 in [F(1),F(3,2)]:
        for rho0 in [F(0),F(1),F(5,4)]:
            lam=F(2,3);K=(lam+rho0)*s0/3;V=c0*s0*s0
            alpha=F(3,2);phi_a=V/alpha;phi_n=V/lam
            ck(3*K/s0==rho0+lam)
            for C in [F(-1,4),F(1,3)]:
                ck(rho0+C+lam-C==3*K/s0)
                ck(alpha*phi_a==V)
                ck((lam-C)*phi_n!=V)
                # Evaluate actions directly, with arbitrary off-shell volume density.
                volume=F(7,5);flux=F(4,3);beta=F(2,5)
                old=-(rho0+lam)*volume+(alpha*lam+beta)*flux
                new=-(rho0+C+lam-C)*volume+(alpha*(lam-C)+beta)*flux
                ck(new-old==-alpha*C*flux)
                old2=-(rho0+lam)*volume+lam*lam*flux/2
                new2=-(rho0+C+lam-C)*volume+(lam-C)**2*flux/2
                ck(new2-old2==(-lam*C+C*C/2)*flux)
            # Differentiate the cubic independently by its coefficient list.
            cubic=[-3*K,rho0,F(0),c0/phi_n]
            ck(polynomial(cubic,s0)==0)
            denom=polynomial(derivative(cubic),s0)
            dx=-s0/denom;dR=-12*dx/s0**2
            ck(denom>0 and dx<0 and dR>0)
            ck(s0+denom*dx==0)
            ck(dR==12/(s0*(rho0+3*c0*s0*s0/phi_n)))
# Translate derivatives of polynomial couplings. Affine survives every fixture;
# each genuine quadratic/cubic example fails at least one small shift.
for coeff in [[F(2),F(3)], [F(2),F(3),F(1)], [F(2),F(3),F(0),F(1)]]:
    d=derivative(coeff)
    equal=[polynomial(d,x-C)==polynomial(d,x)
           for x in [F(1),F(2)] for C in [F(1,5),F(-1,4)]]
    ck(all(equal) if len(coeff)==2 else not all(equal))
# The Legendre term cancels delta A, leaving a nonzero delta lambda coefficient.
for a in [F(1,3),F(2)]:
    l=F(7,4);A=F(5,3);dA=F(1,2);dl=F(-2,3);b=F(3)
    bulk=(a*l+b)*dA
    boundary=-(a*l+b)*dA-a*A*dl
    ck(bulk+boundary==-a*A*dl)
# Input faults must be detected after the clean baseline. These change equations,
# geometric normalization or exact stationary/response data, not reporting flags.
faults=[('action_coefficients','multiplier','1'),
        ('action_coefficients','top_form','-1'),
        ('affine','shift_action_flux_factor','3/2'),
        ('geometry','scalar_factor','6'),
        ('geometry','ricci_factor','4'),
        ('rational_control','affine_flux','7'),
        ('rational_control','nonlinear_flux','5'),
        ('rational_control','lambda','3'),
        ('rational_control','nonlinear_ds_drho','2/7'),
        ('rational_control','nonlinear_dR_drho','3/7')]
for group,key,value in faults:
    q=copy.deepcopy(r);q[group][key]=value;ck(not certificate(q))
for dep in r['dependencies']:
    ck(hashlib.sha256((ROOT/dep['path']).read_bytes()).hexdigest()==dep['sha256'])
# These only guard declared scope; they are not mathematical fault detections.
flags=['fixed_lambda_shift_map_admissible','globally_exact_closed_positive_volume_possible',
       'quantum_radiative_theorem','lorentzian_relaxation','GU_metric_adapter',
       'magnitude_prediction_without_flux_data','source_top_form_identity']
ck(not any(r[k] for k in flags))
for key in flags:
    q=copy.deepcopy(r);q[key]=True;ck(any(q[k] for k in flags))
print('K1850 independent rational controls',n,'including',len(faults),'input faults and',len(flags),'separate reporting faults')
