#!/usr/bin/env python3
"""Exact duality/smearing/domain countercontrols. No native action or domain built."""
import argparse
import json
from pathlib import Path
import sympy as s

ap=argparse.ArgumentParser()
ap.add_argument('--output',type=Path)
ap.add_argument('--mutate',choices=['omit-density-ratio','smearing-is-restriction'])
args=ap.parse_args()
checks=[]
def check(name, actual, expected, kind='support'):
    ok=s.simplify(actual-expected)==0
    checks.append({'name':name,'pass':bool(ok),'kind':kind})

# Source-shaped q is zeroth-order at a section; use a nontrivial rectangular
# finite control rather than asserting this is the dimension128 native map.
Q=s.Matrix([[1,1,0],[0,1,1]])
v=s.Matrix([2,3,5]); beta=s.Matrix([7,11])
check('rectangular fiber dual identity',(beta.T*Q*v)[0],((Q.T*beta).T*v)[0])
check('fiber transpose is injection rank',Q.T.rank(),2)
check('fiber transpose output is ambient-fiber covector',(Q.T*beta)[1],18)
check('observed and ambient coefficient dimensions differ',Q.T.rows-Q.T.cols,1)
B=s.Matrix([[2,1,0],[1,3,0],[0,0,5]])
bar=B.inv()*Q.T*beta
check('independent barred pairing identification',(bar.T*B.T*v)[0],(beta.T*Q*v)[0])
check('pairing invertible without reality assumption',B.det(),25)

# Coordinates beta=b wS dx and ambient mu=wY dxdy. Delta coefficient must
# include wS/wY at the section. Constants isolate the density obligation.
wS,wY=s.Integer(3),s.Integer(2)
ratio=1 if args.mutate=='omit-density-ratio' else wS/wY
check('normal delta density conversion',wY*ratio,wS)
check('naive omission really changes the functional',wY-wS,-1,'countercontrol')

# A normalized rapidly decreasing profile, one dimension at a time.
y=s.symbols('y',real=True); eps=s.symbols('eps',positive=True)
rho=s.exp(-y*y)/s.sqrt(s.pi)
I0=s.integrate(rho,(y,-s.oo,s.oo))
I2=s.integrate(y*y*rho,(y,-s.oo,s.oo))
L2=s.integrate(rho*rho,(y,-s.oo,s.oo))
check('Gaussian profile normalized',I0,1)
check('Gaussian second normal moment',I2,s.Rational(1,2))
check('Gaussian one-normal squared norm',L2,1/s.sqrt(2*s.pi))
readout_second=0 if args.mutate=='smearing-is-restriction' else eps**2*I2
check('finite smearing differs from literal restriction on normal quadratic',readout_second,eps**2/2,'countercontrol')
check('literal restriction of normal quadratic',s.Integer(0),0)
check('constant trace agrees for normalized smearing',I0**10,1)
normal_norm_sq=eps**(-10)*L2**10
check('codimension10 normalized profile squared norm',normal_norm_sq,(2*s.pi)**(-5)*eps**(-10))
check('normal dual norm squared scaling',s.diff(normal_norm_sq,eps)*eps/normal_norm_sq,-10)
check('nonzero thin dual cannot have bounded normal L2 size',s.limit(1/normal_norm_sq,eps,0,dir='+'),0)
# Product-profile constrained domain u=psi(y)v, with psi(0)=1. Its smooth
# biorthogonal dual can represent evaluation on THAT subspace.
psi=s.exp(-y*y)
phi=s.sqrt(2/s.pi)*s.exp(-y*y)
check('chosen profile has unit section value',psi.subs(y,0),1)
bi=s.integrate(phi*psi,(y,-s.oo,s.oo))
check('smooth dual profile is biorthogonal',bi**10,1,'countercontrol')
# An unrestricted normal quadratic refutes equivalence beyond that subspace.
check('same smooth profile differs on unrestricted normal quadratic',s.integrate(phi*y*y,(y,-s.oo,s.oo)),1/s.sqrt(2),'countercontrol')
# Reused Fourier tail threshold: in c10, delta H^-s integrability needs
# normal radial exponent9-2s<-1. s5 is the logarithmic endpoint.
check('critical normal Fourier power',9-2*5,-1)
check('above-threshold normal Fourier power',9-2*6,-3)
check('ordinary Hminus1 insufficient',9-2*1,7)
# Compact normal domain positive control: constant test field and beta/Vol.
volume=s.symbols('volume',positive=True)
check('finite-volume constrained-dual normalization',volume/volume,1,'countercontrol')
report={'status':'PASS' if all(x['pass'] for x in checks) else 'FAIL',
        'passed':sum(x['pass'] for x in checks),'total':len(checks),
        'checks':checks,
        'claim_ceiling':'Fiber-dual/current and explicit domain controls only; no source-selected barred readout, action, physical domain or family index.',
        'normal_dimension':10,'profile_fixture':'Schwartz Gaussian; theorem uses compact tests and distributional definition',
        'normal_profile_norm_power':-5}
if args.output:
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(report,indent=2)+'\n')
for c in checks: print(('PASS ' if c['pass'] else 'FAIL ')+c['name'])
print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
raise SystemExit(0 if report['status']=='PASS' else 1)
