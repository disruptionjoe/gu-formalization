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
    e=s.Rational(9,25);psi=s.Matrix([s.Rational(4,5),0,0,s.Rational(3,5)]);rho=psi*psi.T
    if fault=='dephase_correlated_pair':rho=s.diag(1-e,0,0,e)
    target=s.diag(1-e,e,0,0);D=rho-target
    expected=(e+s.sqrt(4*e-3*e*e))/2
    check(s.simplify(distance(D)-expected)==0,'actual reference-sensitive distance')
    check(expected>e and expected<=e+s.sqrt(e*(1-e)),'sqrt order and block bound')
    diagonal=s.diag(1-e,0,0,e)
    check(distance(diagonal-target)==e,'classical versus coherent reference control')
    # Physical sea mode is mixed even when excitation pair is exactly vacuum.
    a=annihilator(2,0);b=annihilator(2,1);c=(a+b.T)/s.sqrt(2)
    if fault=='drop_hole_component':c=a
    vac=s.diag(1,0,0,0)
    check(zero(c*c.T+c.T*c-s.eye(4)),'physical CAR normalization')
    check(s.trace(vac*c.T*c)==s.Rational(1,2),'mixed physical mode in pure excitation vacuum')
    nu=s.Rational(3,4);tau=s.diag(1-nu,nu)
    if fault=='silently_purify_physical_state':tau=s.diag(1,0)
    check(distance(tau-s.diag(1,0))==nu,'fixed-even-vacuum reset floor')
    check(1-max(tau.eigenvals().keys())==s.Rational(1,4),'unrestricted pure target floor')
    # Actual signed fermionic swap on adjacent L, M, with a third reference mode.
    swap=s.zeros(8)
    for mask in range(8):
        l=mask&1;m=(mask>>1)&1;dest=(mask&4)|(m)|(l<<1)
        sign=(-1)**(l*m)
        swap[dest,mask]=sign
    if fault=='wrong_reset_register':swap=s.eye(8)
    vin=s.zeros(8,1);vin[0]=s.Rational(4,5);vin[6]=s.Rational(3,5)
    vout=swap*vin;expectedv=s.zeros(8,1);expectedv[0]=s.Rational(4,5);expectedv[5]=s.Rational(3,5)
    check(zero(vout-expectedv),'vacuum reset and relabelled original memory-reference state')
    parity=s.diag(*[(-1)**mask.bit_count() for mask in range(8)])
    check(zero(swap*parity-parity*swap),'swap even parity')
    check(zero(swap.T*swap-s.eye(8)),'full signed swap unitarity')
    # Product spectrum and parity-constrained top eigenvalue are distinct.
    tau2=s.kronecker_product(s.diag(s.Rational(1,4),s.Rational(3,4)),s.diag(s.Rational(2,3),s.Rational(1,3)))
    check(max(tau2.eigenvals().keys())==s.Rational(1,2),'two-mode product eigenvalue')
    check(max(tau2[0,0],tau2[3,3])==s.Rational(1,4),'even-block top eigenvalue')
if __name__=='__main__':harness(test,['dephase_correlated_pair','drop_hole_component','silently_purify_physical_state','wrong_reset_register'])
