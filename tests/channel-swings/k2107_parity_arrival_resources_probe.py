"""Exact Gaussian, resource and finite-space isometry controls."""
import sympy as s
I=s.I

def check(fault):
    x=s.symbols('x',real=True);sigma,T,m=s.symbols('sigma T m',positive=True)
    density=s.exp(-x*x/(2*sigma**2))/(s.sqrt(2*s.pi)*sigma)
    assert s.integrate(density,(x,-s.oo,s.oo))==1
    assert s.integrate(x*x*density,(x,-s.oo,s.oo))==sigma**2
    # Independent momentum variance from differentiating the normalized Gaussian.
    f=s.exp(-x*x/(4*sigma**2))/(2*s.pi*sigma**2)**s.Rational(1,4)
    vp=s.integrate(s.diff(f,x)**2,(x,-s.oo,s.oo))
    spread=sigma**2+T**2/((4 if fault!='wrong_spreading' else 2)*m*m*sigma**2)
    assert s.simplify(spread-sigma**2-T*T*vp/(m*m))==0,'free variance'
    p0=s.symbols('p0',positive=True)
    assert s.simplify(s.limit((p0*T/m)/s.sqrt(2*spread),T,s.oo)-s.sqrt(2)*sigma*p0)==0,'waiting limit'
    u=s.symbols('u',positive=True);var=u+T*T/(4*m*m*u)
    assert s.simplify(s.diff(var,u).subs(u,T/(2*m)))==0
    assert s.simplify(var.subs(u,T/(2*m))-T/m)==0
    Efree=p0*p0/(2*m)+(1 if fault!='lost_preparation_variance' else 0)/(8*m*sigma*sigma)
    assert s.simplify(Efree-(p0*p0+vp)/(2*m))==0,'kinetic preparation energy'
    # Smoothstep profile (C1 after constant extension): honest finite control, not C-infinity assertion.
    v=s.symbols('v',real=True);ell=s.symbols('ell',positive=True)
    theta=s.pi/2*(3*v*v-2*v**3)
    if fault=='half_profile_area':theta/=2
    A=2*s.diff(theta,v)/ell
    assert s.integrate(A*ell,(v,0,1))==s.pi,'flip area'
    assert s.simplify(s.integrate(A*A*ell,(v,0,1))-6*s.pi**2/(5*ell))==0,'coefficient integral'
    # A concrete unbounded A=2x control of covariant energy (distinct from compact-bound theorem).
    Df=-I*s.diff(f,x)+2*x*f
    Eactual=s.integrate(s.expand_complex(s.conjugate(Df)*Df),(x,-s.oo,s.oo))/(2*m)
    assert s.simplify(Eactual-(1/(8*m*sigma**2)+2*sigma**2/m))==0,'actual covariant energy'
    # Three spatial sites; exact orthogonal free transport. Pointer X eigenbasis.
    # left->right, middle->left, right->middle. Weights98/100,1/100,1/100.
    weights=[s.Rational(98,100),s.Rational(1,100),s.Rational(1,100)];dest=[2,0,1]
    norm2=[]
    for n1 in [0,1]:
      for n2 in [0,1]:
       for pointer_minus in [0,1]:
        W=(-1)**((n1+n2)*pointer_minus)
        gs=[s.Integer(1),s.exp(-I*s.pi*n1*pointer_minus/2),s.Integer(W)]
        errs=[]
        for j in range(3):
            actual=gs[dest[j]]*(s.conjugate(gs[j]) if fault!='omit_initial_gauge' else 1)
            expected=gs[dest[j]]/gs[j]
            assert s.simplify(actual-expected)==0,'two-sided gauge evolution'
            errs.append(s.expand_complex(abs(actual-W)**2)*weights[j])
        norm2.append(s.simplify(sum(errs)))
    ei=ef=s.Rational(2,100)
    delta=2*(s.sqrt(ei)+s.sqrt(ef)) if fault!='squared_tail_bound' else 2*(ei+ef)
    assert max(norm2)<=delta**2,'uniform isometry tail bound'
    assert max(norm2)>0,'nontrivial spatial error control'
    # Full recorded mixture from orthogonal left/right spatial sectors, every matrix unit.
    q=s.Rational(2,7);Pe=s.diag(1,0,0,1);Po=s.eye(4)-Pe
    for a in range(4):
      for b in range(4):
        e=s.zeros(4);e[a,b]=1
        spatial_right=[Pe*e*Pe,Po*e*Po]
        spatial_left=[e,s.zeros(4)]
        if fault=='lost_blank_branch': spatial_left=spatial_right
        actual=[(1-q)*spatial_right[j]+q*spatial_left[j] for j in range(2)]
        expected=[(1-q)*Pe*e*Pe+q*e,(1-q)*Po*e*Po]
        assert all(s.simplify(v)==0 for j in range(2) for v in actual[j]-expected[j]),'full waiting mixture'
    odd=s.diag(0,1,0,0);difference=s.diag(q*odd,-q*odd)
    assert sum(abs(e)*mult for e,mult in difference.eigenvals().items())/2==q,'sharp recorded error floor'


FAULTS=['wrong_spreading','lost_preparation_variance','half_profile_area','omit_initial_gauge','squared_tail_bound','lost_blank_branch']


def main():
    check(None)
    print('PASS clean exact baseline')
    for fault in FAULTS:
        try: check(fault)
        except AssertionError as e: print('DETECTED',fault,str(e))
        else: raise AssertionError('undetected changed-data fault: '+fault)
    print('PASS',len(FAULTS),'genuine faults; analytic continuum proofs are separate')

if __name__=='__main__': main()
