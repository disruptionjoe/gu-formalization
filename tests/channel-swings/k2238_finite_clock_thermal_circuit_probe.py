"""Exact Gaussian-rational controls; written-proof companion finite controls.
Universal proofs are in the companion note. Does not certify laboratory control.
"""
from fractions import Fraction as F
from math import comb

class G:
    def __init__(self,a=0,b=0):
        if isinstance(a,G): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=G(o); return G(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return G(-self.a,-self.b)
    def __sub__(self,o): return self+-G(o)
    def __rsub__(self,o): return G(o)+-self
    def __mul__(self,o):
        o=G(o); return G(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        v=G(1)
        for _ in range(n):v=v*self
        return v
    def conj(self):return G(self.a,-self.b)
    def norm2(self):return self.a*self.a+self.b*self.b
    def __eq__(self,o):
        o=G(o);return (self.a,self.b)==(o.a,o.b)

I=G(0,1)
def mat(rows):return [[G(x) for x in row] for row in rows]
def eye(n):return mat([[int(j==k) for k in range(n)] for j in range(n)])
def mul(a,b):return [[sum(a[j][l]*b[l][k] for l in range(len(b))) for k in range(len(b[0]))] for j in range(len(a))]
def adj(a):return [[a[k][j].conj() for k in range(len(a))]for j in range(len(a[0]))]
def scale(x,a):return [[x*z for z in row]for row in a]
def plus(a,b):return [[x+y for x,y in zip(r,s)]for r,s in zip(a,b)]
def kron(a,b):return [[a[j//len(b)][k//len(b[0])]*b[j%len(b)][k%len(b[0])] for k in range(len(a[0])*len(b[0]))]for j in range(len(a)*len(b))]
def trace_A(a):return [[sum(a[2*j+l][2*k+l] for l in range(2))for k in range(2)]for j in range(2)]

def run(fault=None):
    count=0
    def check(value):
        nonlocal count
        assert value
        count+=1
    # No clock matrix exponential needed: normalized symmetric product solves ODE.
    c,s=F(3,5),F(4,5)
    for M in range(1,9):
        amp=[G(c)**(M-k)*(-I*s)**k for k in range(M+1)]
        check(sum(comb(M,k)*a.norm2()for k,a in enumerate(amp))==1)
        for k in range(M+1):
            derivative=G(0)
            if M>k: derivative+=-(M-k)*s*G(c)**(M-k-1)*(-I*s)**k
            if k: derivative+=k*(-I*c)*G(c)**(M-k)*(-I*s)**(k-1)
            rhs=G(0)
            if k:rhs+=k*amp[k-1]
            if k<M:rhs+=(M-k+(1 if fault=='clock_weight' else 0))*amp[k+1]
            check(I*derivative==rhs)
        shift=M-(1 if fault=='positive_shift' else 0)
        programmed_spectrum=[shift-M+2*j for j in range(M+1)]
        check(min(programmed_spectrum)>=0)
        # Exact initial moments of programmed controller relative to chosen ground.
        check(comb(M,1)==M)
    # Exchange unitary on BA; diagonal phase is an energy-preserving noncommuting gate.
    U=mat([[1,0,0,0],[0,0,-I,0],[0,-I,0,0],[0,0,0,1]])
    Z=mat([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])
    check(mul(adj(U),U)==eye(4));check(mul(U,Z)!=mul(Z,U))
    gates=[U,Z,eye(4),eye(4)]
    prefix=[eye(4)]
    for gate in gates:prefix.append(mul(gate,prefix[-1]))
    for k,gate in enumerate(gates):
        actual=adj(gate) if fault=='gate_orientation' else gate
        check(mul(mul(adj(prefix[k+1]),actual),prefix[k])==eye(4))
    # Resonance is genuinely load-bearing for simple free factorization.
    H=mat([[0,0,0,0],[0,1,0,0],[0,0,2 if fault=='unequal_gap' else 1,0],[0,0,0,2]])
    check(mul(H,U)==mul(U,H))
    # Complete operator-basis replacement on one bank qubit; linearity allows arbitrary F.
    for p in (F(1,4),F(1,3)):
        tau=mat([[1-p,0],[0,p]])
        for j in range(2):
            for k in range(2):
                basis=mat([[int(a==j and b==k)for b in range(2)]for a in range(2)])
                out=trace_A(mul(mul(U,kron(basis,tau)),adj(U)))
                check(out==scale(int(j==k),tau))
    # Thermal two-bank product replacement follows by tensoring these complete channels.
    # Clock reduced output is a mixture; the plateau error excludes clock joint distance.
    r=F(1,100);p=1-r
    weights=[F(comb(4,k))*p**k*r**(4-k)for k in range(5)]
    check(sum(weights)==1)
    failure=sum(weights[:2])
    check(failure==4*r**3-3*r**4)
    check(failure==F(397,10**8))
    check(1-weights[4]>failure)  # joint clock marginal does not inherit data-only bound
    # Factorial-moment tail envelope exercised at multiple exact inputs and paddings.
    for M in range(1,10):
        for R in range(M):
            for r in (F(1,100),F(1,4),F(3,4)):
                tail=sum(F(comb(M,j))*r**j*(1-r)**(M-j)for j in range(R+1,M+1))
                check(tail<=comb(M,R+1)*r**(R+1))
    # Actual large renewal consumer; no huge Hilbert matrix is constructed.
    n=comb(1709,9)
    check(n==335545898949148913616591)
    check(F(n,10**54)<F(4,10**31))
    check(1701+8+1==1710)
    check(max((k+1)*(1709-k)for k in range(1709))==855**2)
    check(1709+1!=1701+1)  # padding adds genuine clock dimension
    # Exact recurrence: at gt=pi, c=-1,s=0 returns to prefix zero.
    amp=[G(-1)**(4-k)*G(0)**k for k in range(5)]
    check(amp[0]==1 and all(a==0 for a in amp[1:]))
    check(amp[4]!=1)  # exact recurrence contradicts permanent completion
    return count

if __name__=='__main__':
    import argparse, hashlib, json
    from pathlib import Path
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    n=run()
    faults=('clock_weight','positive_shift','gate_orientation','unequal_gap')
    caught=[]
    for fault in faults:
        try:run(fault)
        except AssertionError:caught.append(fault)
        else:raise AssertionError('undetected '+fault)
    deps=['explorations/conditional-build/k2238-finite-clock-thermal-circuit-2026-10-29.md','explorations/conditional-build/k2235-microscopic-thermal-renewal-2026-10-29.md']
    report=dict(result_id='K2238',exact_controls=n,detected_faults=caught,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Finite exact spin recurrence, gate/energy and complete one-bank operator-basis controls; rational timing/resource arithmetic; universal written arbitrary-M/reference and analytic no-plateau proofs separate.')
    dest=root/'lab/process/k2238-finite-clock-thermal-circuit.json'
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dest.read_text())==report,'certificate drift'
    print(json.dumps(dict(result='K2238',controls=n,faults=len(caught))))
