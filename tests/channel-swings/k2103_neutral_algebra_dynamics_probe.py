"""Exact finite neutral algebra, coherent leakage and nuclear-norm controls."""
import sympy as s
I=s.I

def zero(a): return all(s.simplify(x)==0 for x in a)
def comm(a,b): return a*b-b*a
def car(n):
    Z=s.diag(1,-1);a=s.Matrix([[0,1],[0,0]])
    return [s.kronecker_product(*[Z if j<k else a if j==k else s.eye(2) for j in range(n)]) for k in range(n)]
def dg(h,a): return sum((h[j,k]*a[j].H*a[k] for j in range(len(a)) for k in range(len(a))),s.zeros(a[0].rows))
def check(fault):
    a=car(3);n=[x.H*x for x in a];N=n[0]+n[1];G=N*n[2]
    if fault=='hidden_hopping_in_invisible': G+=a[0].H*a[2]+a[2].H*a[0]
    # Every neutral matrix unit (2 one-dimensional and one two-dimensional block).
    for r in range(4):
        for c in range(4):
            if r.bit_count()==c.bit_count():
                E=s.zeros(4);E[r,c]=1
                assert zero(comm(G,s.kronecker_product(E,s.eye(2)))), 'neutral closure'
    pair=a[0]*a[1]
    assert zero(comm(N*n[2],pair)+2*pair*n[2]) and not zero(comm(N*n[2],pair)), 'even versus neutral'
    # All-state closure fails even in one fixed total-number sector.
    t=s.symbols('t',real=True);h=s.Matrix([[0,1],[1,0]]);U=s.cos(t)*s.eye(2)-I*s.sin(t)*h
    plus=s.Matrix([1,I])/s.sqrt(2);minus=s.Matrix([1,-I])/s.sqrt(2)
    if fault=='coherent_input_replaced': minus=plus
    p=(U*plus)[0];m=(U*minus)[0]
    assert s.simplify(s.expand_complex(p*s.conjugate(p)-m*s.conjugate(m))-s.sin(2*t))==0, 'fixed-charge witness'
    # Full Fock residual with two singular values 2,3: largest singular value is insufficient.
    b=car(4);h=s.zeros(4);h[0,2]=h[2,0]=2;h[1,3]=h[3,1]=3
    if fault=='lost_second_leakage': h[1,3]=h[3,1]=0
    GG=dg(h,b);NN=b[0].H*b[0]+b[1].H*b[1];C=I*comm(GG,NN)
    assert max(abs(e) for e in C.eigenvals())==5, 'nuclear-norm defect'
    Z=(s.eye(16)-2*b[0].H*b[0])*(s.eye(16)-2*b[1].H*b[1])
    assert zero(Z*C*Z+C), 'parity odd residual'
    assert s.cos(s.pi/4)**4==s.Rational(1,4) and s.cos(s.pi/2)**2==0, 'fresh bath is not semigroup'

FAULTS=['hidden_hopping_in_invisible','coherent_input_replaced','lost_second_leakage']


def main():
    check(None)
    print('PASS clean exact baseline')
    for fault in FAULTS:
        try:
            check(fault)
        except AssertionError as exc:
            print('DETECTED', fault, str(exc))
        else:
            raise AssertionError('undetected actual fault: '+fault)
    print('PASS', len(FAULTS), 'genuine faults rejected; universal claims require written proof')

if __name__ == '__main__':
    main()
