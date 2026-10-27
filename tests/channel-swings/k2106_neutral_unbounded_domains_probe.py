"""Finite algebra and exact boundary witnesses, not an infinite-domain certification."""
import sympy as s
I=s.I

def zero(a): return all(s.simplify(v)==0 for v in a)
def check(fault):
    h=s.Matrix([[0,1],[1,0]]);K=s.diag(0,-1,-4)
    H=s.kronecker_product(h,s.eye(3))+s.kronecker_product(s.eye(2),K)
    if fault=='hidden_dependent_visible_drift': H+=s.kronecker_product(s.diag(1,-1),K)
    for a in range(2):
        for b in range(2):
            e=s.zeros(2);e[a,b]=1;A=s.kronecker_product(e,s.eye(3))
            assert zero(H*A-A*H-s.kronecker_product(h*e-e*h,s.eye(3))),'visible drift independent of hidden state'
    N=s.diag(0,1,2,3);S=s.eye(4);S.col_swap(0,3);vac=s.eye(4)[:,0]
    energy=-N if fault!='stable_replaces_unstable' else N
    assert (vac.T*S.T*energy*S*vac)[0]==-3,'hidden swap extracts specified energy'
    # Nonselfadjoint unitary B distinguishes B a B* from B* a B.
    B=s.diag(1,I);a=s.Matrix([[0,1],[1,0]])
    crossing=B*a*B.H if fault!='inverse_boundary_conjugation' else B.H*a*B
    assert zero(crossing-s.Matrix([[0,-I],[I,0]])),'twisted Heisenberg orientation'
    B=s.Matrix([[0,1],[1,0]]);P=s.diag(1,0)
    if fault=='unmixed_boundary': B=s.eye(2)
    assert zero(B*P*B.H-(s.eye(2)-P)),'boundary changes visible charge'
    left=P;right=B*P*B.H;mid=s.eye(2)/2
    assert max(abs(e) for e in (right-left).eigenvals())==1,'norm discontinuity'
    assert max(abs(e) for e in (left-mid).eigenvals())==s.Rational(1,2)
    assert max(abs(e) for e in (right-mid).eigenvals())==s.Rational(1,2)
    # At each diagonal entry the two endpoint errors differ by1, giving minimax >=1/2.
    for j in range(2): assert abs(left[j,j]-right[j,j])==1,'minimax lower bound'
    x=s.symbols('x',real=True);eta=3*x*x-2*x**3
    f=s.Matrix([1-eta,eta]);f0=f.subs(x,0);f1=f.subs(x,1)
    if fault=='bad_squared_domain': f+=s.Matrix([x*(1-x),0])
    assert zero(f.subs(x,1)-B*f.subs(x,0)),'squared domain value trace'
    assert zero(s.diff(f,x).subs(x,1)-B*s.diff(f,x).subs(x,0)),'squared domain derivative trace'
    assert not zero(P*f1-B*P*f0),'P breaks squared domain'
    # Actual fixed-vector leakage measure t tends0 although norm remains1.
    t=s.symbols('t',positive=True);assert s.integrate(1,(x,1-t,1))==t

FAULTS=['hidden_dependent_visible_drift','stable_replaces_unstable','inverse_boundary_conjugation','unmixed_boundary','bad_squared_domain']


def main():
    check(None)
    print('PASS clean exact baseline')
    for fault in FAULTS:
        try: check(fault)
        except AssertionError as e: print('DETECTED',fault,str(e))
        else: raise AssertionError('undetected changed-data fault: '+fault)
    print('PASS',len(FAULTS),'genuine faults; analytic continuum proofs are separate')

if __name__=='__main__': main()
