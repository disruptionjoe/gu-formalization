#!/usr/bin/env python3
"""Independent slab ODE, flux, budget and infrared integral controls."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[2];OUT='lab/process/k1889-coupled-slab-observation-spectrum.json'
COUNT={'exact':0,'numerical':0,'report_pin':0}
def ck(ok,name,kind='exact'):
    if not ok:raise AssertionError('FAIL '+name)
    COUNT[kind]+=1

def matrix(d):
    v={(i,j):s.Rational(x) for i,j,x in d['entries']}
    return s.Matrix(d.get('rows',16),d.get('columns',16),lambda i,j:v.get((i,j),0))
def zero(M):return all(s.expand(x)==0 for x in M)
def boundary_test(M,G,k,p,q):
    return zero(-G[:4,:4]*M+k*G[:4,:4]*s.diag(1,-1,-1,1)-s.I*(p*G[:4,4:8]+q*G[:4,8:]))
def baseline(cert):
    alpha=s.Rational(138,25);beta=s.Rational(1866,625);rho=s.Rational(311,575);c=alpha-beta*beta/alpha
    en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());ob=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text())
    grams=[]
    for e,o in zip(en['blocks'],ob['blocks']):
        H=matrix(e['H']);T=list(map(matrix,o['T']));G=s.zeros(12)
        for i in range(3):
            for j in range(3):G[4*i:4*i+4,4*j:4*j+4]=T[i]*H.inv()*T[j].T
        grams.append(G)
        for k,p,q in [(0,0,0),(1,0,0),(-2,3,4),(1,s.Rational(1,3),s.Rational(-2,5))]:
            M=k*s.diag(1,-1,-1,1)-s.I*(p*G[:4,4:8]+q*G[:4,8:])/alpha
            ck(boundary_test(M,G,k,p,q),'actual flux boundary')
            ck(M==M.conjugate().T,'Hermitian boundary')
            ck(zero(M*M-(k*k+rho*rho*(p*p+q*q))*s.eye(4)),'square actual matrix')
            ck(zero(alpha*((k*k+p*p+q*q)*s.eye(4)-M*M)-c*(p*p+q*q)*s.eye(4)),'actual surface eigenvalue')
    x=s.symbols('x',real=True)
    for length in (s.Rational(1),s.Rational(3,2)):
        for drift in (s.Rational(0),s.Rational(2,3),s.Rational(-7,5)):
            for n in (1,2,3):
                w=n*s.pi/length;u=s.cos(w*x)+drift*s.sin(w*x)/w
                ck(s.simplify((s.diff(u,x)-drift*u).subs(x,0))==0,'left Robin')
                ck(s.simplify((s.diff(u,x)-drift*u).subs(x,length))==0,'right Robin')
                ck(s.simplify(-s.diff(u,x,2)-w*w*u)==0,'bulk ODE')
    # Independent square completion: the exact two-mode feasible minimizer.
    lam=[c,4*c];t=c;z=[1,1];src=[s.sqrt(l)/(l+t) for l in lam]
    E=sum(a*a for a in src);err=sum((s.sqrt(l)*a-1)**2 for a,l in zip(src,lam))
    ck(s.simplify(E-s.Rational(41,100)/c)==0,'two-mode budget')
    ck(s.simplify(err-s.Rational(29,100))==0,'two-mode actual error')
    for a,b in [(0,0),(1,2),(-3,2)]:
        trial=[s.Rational(a),s.Rational(b)]
        lhs=sum((s.sqrt(l)*v-1)**2+t*v*v for l,v in zip(lam,trial))
        rhs=err+t*E+sum((l+t)*(v-v0)**2 for l,v,v0 in zip(lam,trial,src))
        ck(s.simplify(lhs-rhs)==0,'actual optimality square completion')
    mp.mp.dps=50
    for a in [mp.mpf('0.001'),mp.mpf('0.2'),mp.mpf('2')]:
        energy=mp.quad(lambda u:u*mp.exp(-u)/(u+a)**2,[0,a,1,mp.inf]);error=mp.quad(lambda u:a*a*mp.exp(-u)/(u+a)**2,[0,a,1,mp.inf]);F=mp.exp(a)*mp.e1(a)
        ck(abs(energy-((1+a)*F-1))<mp.mpf('1e-44'),'independent radial energy integral','numerical')
        ck(abs(error-(a-a*a*F))<mp.mpf('1e-44'),'independent radial error integral','numerical')
    for key,val in [('alpha',alpha),('beta',beta),('rho',rho),('surface_coefficient',c)]:ck(s.Rational(cert[key])==val,'serialized '+key,'report_pin')
    for p,h in cert['inputs'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin','report_pin')
    ck(cert['scope']['rectangular_box_spectrum'] is False and cert['scope']['native_GU'] is False,'scope','report_pin')
    return grams[0],c

def main():
    cert=json.loads((ROOT/OUT).read_text());G,c=baseline(cert);baseline_counts=COUNT.copy();faults=[];alpha=s.Rational(138,25);K=s.diag(1,-1,-1,1);M=K-s.I*(G[:4,4:8]+2*G[:4,8:])/alpha
    jobs=[('wrong outward sign',lambda:ck(boundary_test(-M,G,1,1,2),'Robin sign')),
          ('scalar Robin substitution',lambda:ck(boundary_test(K,G,1,1,2),'scalar substitution')),
          ('lost cross coupling',lambda:ck(zero(alpha*(6*s.eye(4)-K*K)-5*c*s.eye(4)),'surface coefficient')),
          ('lost complex Fourier factor',lambda:ck((K-(G[:4,4:8]+2*G[:4,8:])/alpha).is_hermitian,'Hermitian Fourier matrix')),
          ('wrong energy denominator',lambda:ck(s.Rational(1,2)+s.Rational(4,5)==s.Rational(41,100),'budget denominator'))]
    for name,job in jobs:
        try:job()
        except AssertionError as e:
            if not str(e).startswith('FAIL '):raise
            faults.append(name)
        else:raise AssertionError('FAIL undetected '+name)
    for key in ('surface_coefficient','rho'):
        bad=copy.deepcopy(cert);bad[key]=str(s.Rational(bad[key])+1)
        try:baseline(bad)
        except AssertionError as e:
            if not str(e).startswith('FAIL serialized'):raise
            faults.append('serialized '+key)
        else:raise AssertionError('FAIL undetected report fault')
    print('PASS K1889 independent baseline',baseline_counts,'rejected',len(faults),'faults:',', '.join(faults))
if __name__=='__main__':main()
