"""Exact finite operator/state controls; universal claims rest on the linked written proof."""
import sympy as s

def check(value,msg):
    if not bool(value): raise AssertionError(msg)
def zero(M): return all(s.simplify(x)==0 for x in M)
def annihilator(n,j):
    A=s.zeros(2**n)
    for mask in range(2**n):
        if mask&(1<<j): A[mask^(1<<j),mask]=(-1)**sum((mask>>k)&1 for k in range(j))
    return A
def lift(H):
    n=H.rows; a=[annihilator(n,j) for j in range(n)];D=s.zeros(2**n)
    for i in range(n):
        for j in range(n):D+=H[i,j]*a[i].T*a[j]
    return D
def distance(D):return s.simplify(sum(abs(e)*m for e,m in D.eigenvals().items())/2)
def harness(test,faults):
    test(None);print('PASS clean exact baseline')
    for fault in faults:
        try:test(fault)
        except AssertionError as exc:print('DETECTED',fault,str(exc))
        else:raise AssertionError('undetected fault '+fault)
    print('PASS',len(faults),'genuine input/state/gate faults; finite controls are not universal proofs')

def test(fault):
    sig=s.Rational(3,5);g=s.Rational(4,5);omega=s.Integer(2)
    h=s.Matrix([[2,sig],[sig,2]]);f=s.Matrix([1,0]);r=(h-omega*s.eye(2))*f
    V=r*f.T+f*r.T
    if fault=='drop_residual':V=s.zeros(2)
    href=h-V
    check(zero(href*f-omega*f),'compression removes actual dispersion')
    D=lift(V)
    check(sorted(D.eigenvals().keys(),key=float)==[-sig,0,sig],'full Fock residual spectrum')
    check(D.eigenvals()[0]==2,'both occupied cancellation')
    # Full three-mode exact dynamics; A cubed=A for 3/5,4/5 couplings.
    A=s.Matrix([[0,sig,g],[sig,0,0],[g,0,0]])
    if fault=='wrong_memory_coupling':A[0,2]=A[2,0]=s.Rational(3,5)
    t=s.symbols('t',real=True);U=s.eye(3)-s.I*s.sin(t)*A+(s.cos(t)-1)*A*A
    check(zero(A**3-A),'exact three-mode polynomial exponential')
    check(zero(U.conjugate().T*U-s.eye(3)),'actual three-mode unitarity')
    capture=s.simplify(U[2,0]*s.conjugate(U[2,0]))
    check(s.simplify(capture-g*g*s.sin(t)**2)==0,'dispersion-sensitive capture')
    capT=s.simplify(capture.subs(t,s.pi/(2*g)))
    check(s.simplify(capT-(s.Rational(8,25)+4*s.sqrt(2)/25))==0,'exact finite-spread capture at nominal swap')
    check(capT>1-(sig/g)**2,'selected-input variance lower bound control')
    lo=s.Rational(7,5);hi=s.Rational(13,5)
    if fault=='narrow_fake_band':lo=s.Rational(9,5)
    check(sorted(h.eigenvals().keys())==[lo,hi],'actual finite-band endpoints')
    check((hi-lo)**2/4==r.dot(r),'sharp spectral variance example')
    inv=(f.T*h.inv()*f)[0]
    check(inv==s.Rational(50,91),'Schur inverse moment')
    check(omega-g*g*inv>0 and omega-4*inv<0,'stable and unstable pulse controls')
    Delta=s.Rational(3,2);B=s.Matrix([[Delta/2,g],[g,-Delta/2]])
    if fault=='erase_detuning':B[0,0]=B[1,1]=0
    check(zero(B*B-(g*g+Delta*Delta/4)*s.eye(2)),'actual detuned oscillation frequency')
    # Fourier shell coefficient for m=v=1, energies sqrt2..sqrt5, momenta1..2.
    volume=4*s.pi*(2**3-1**3)/3
    check(s.simplify(volume/(2*s.pi)**3-7/(6*s.pi**2))==0,'shell concentration coefficient')
if __name__=='__main__':harness(test,['drop_residual','wrong_memory_coupling','narrow_fake_band','erase_detuning'])
