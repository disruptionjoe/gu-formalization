#!/usr/bin/env python3
"""Independent Pauli representation and direct momentum-integral controls."""
import hashlib,json,math
from pathlib import Path
import sympy as s
import scipy.integrate as integrate
ROOT=Path(__file__).resolve().parents[2]
def checks(fault=None):
    out={}
    def ck(n,b):out[n]=bool(b)
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2)
    G=[s.kronecker_product(X,A) for A in [X,Y,Z]]+[s.kronecker_product(Z,I)]
    points=[(3,0,0,4),(0,0,0,5),(0,3,4,0),(4,0,0,3)]
    for ii,p in enumerate(points):
        P=(s.eye(4)+sum((p[j]*G[j] for j in range(4)),s.zeros(4))/5)/2
        ck('projector_'+str(ii),P*P==P and s.trace(P)==2)
        for jj,q in enumerate(points):
            Q=(s.eye(4)-sum((q[j]*G[j] for j in range(4)),s.zeros(4))/5)/2
            formula=1-s.Rational(sum(p[j]*q[j] for j in range(4)),25)
            if fault=='wrong_overlap':formula/=2
            ck(f'overlap_{ii}_{jj}',s.trace(P*Q)==formula)
    # Numerically integrate the exact massless fixed-|k|=1 radial overlap.
    # This is a convergence control, NOT the proof of divergence.
    def shell(r):
        # Integrating over z analytically avoids cancellation in the angular integrator.
        # Exact sphere integral is 4*pi/(3*r^2) for r>=1, and 4*pi*(1-2*r/3) for r<=1.
        return 4*math.pi/(3*r*r) if r>=1 else 4*math.pi*(1-2*r/3)
    for r in [.25,.5,1.,2.,5.]:
        f=lambda z:1-(r+z)/math.sqrt(r*r+2*r*z+1)
        actual=2*math.pi*integrate.quad(f,-1,1,epsabs=1e-11)[0]
        ck('numeric_shell_'+str(r),abs(actual-shell(r))<1e-9)
    for L in [2,4,8]:
        actual=integrate.quad(lambda r:r*r*shell(r),0,L,points=[1])[0]/(2*math.pi)**3
        expected=L/(6*math.pi**2)-1/(12*math.pi**2)
        if fault=='wrong_cutoff_coefficient':expected*=2
        ck('numeric_integrated_cutoff_'+str(L),abs(actual-expected)<1e-10)
    k=s.symbols('k',positive=True);p=s.symbols('p',real=True)
    ck('1d_direct_crossing_number',s.integrate(2,(p,0,k))/(2*s.pi)==k/s.pi)
    ck('1d_direct_particle_energy',s.integrate(2*p,(p,0,k))/(2*s.pi)==k*k/(2*s.pi))
    # Independent elementary Laplace moments for the rational phase profile.
    ck('1d_Laplace_number',s.integrate(8*k*s.exp(-2*k),(k,0,s.oo))==2)
    ck('1d_Laplace_energy',s.integrate(8*k*k*s.exp(-2*k),(k,0,s.oo))==2)
    # Noncommuting free Hamiltonian: sign averaging cancels mixed terms,
    # leaving the double-potential derivation, not a first-order Markov term.
    comm=lambda a,b:a*b-b*a
    for i in range(2):
        for j in range(2):
            A=s.zeros(2);A[i,j]=1
            actual=(-comm(X+Z,comm(X+Z,A))-comm(X-Z,comm(X-Z,A)))/2+comm(X,comm(X,A))
            expected=-comm(Z,comm(Z,A))
            if fault=='pulse_curvature':expected/=2
            ck(f'pulse_curvature_{i}{j}',actual==expected)
    d=json.loads((ROOT/'lab/process/k1896-local-phase-vacuum-boundary.json').read_text())
    if fault=='report':d['one_dimension']['rational_phase_number']=1
    ck('report_number',d['one_dimension']['rational_phase_number']==2)
    if fault=='pin':d['inputs'][next(iter(d['inputs']))]='wrong'
    for path,h in d['inputs'].items():ck('pin_'+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h)
    return out
if __name__=='__main__':
    baseline=checks();assert all(baseline.values()),'FAIL baseline '+str([k for k,v in baseline.items() if not v])
    print('PASS baseline 28 exact matrix/integral checks; 8 numerical convergence controls; 1 report + 3 pins')
    for fault in ['wrong_overlap','wrong_cutoff_coefficient','pulse_curvature','report','pin']:
        bad=[k for k,v in checks(fault).items() if not v]
        assert bad,'FAIL mutant survived '+fault
        print('CAUGHT',fault,'FAIL',bad[0])
