from pathlib import Path
import sys,json,hashlib,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
PIN='lab/process/k1896-local-phase-vacuum-boundary.json'
REPORT=ROOT/'lab/process/k1897-smooth-pulse-energy.json'
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def check(b,label):
    if not b: raise AssertionError('[FAIL] '+label)
def eq(a,b,label): check(s.simplify(a-b)==0,label)

def calculate():
    Q=s.diag(1,1,-1,-1); E=s.diag(2,3,5,7); H=Q*E
    A=s.Matrix([[1,2,3,4],[2,5,6,7],[3,6,8,9],[4,7,9,10]])
    comm=lambda a,b:a*b-b*a
    C=comm(Q,A); alpha=-(E.inv()*C+C*E.inv())/8
    check(alpha.T==-alpha,'anti-Hermitian normal-form generator')
    check(comm(Q,A+comm(H,alpha))==comm(E.inv(),comm(E,C))/4,'order-improving identity')
    # Independent rational unitary mixing only one positive and negative channel.
    U=s.Matrix([[s.Rational(3,5),0,s.Rational(-4,5),0],[0,1,0,0],[s.Rational(4,5),0,s.Rational(3,5),0],[0,0,0,1]])
    check(U.T*U==s.eye(4),'unitary control');P=(s.eye(4)+Q)/2;N=s.eye(4)-P
    J=s.trace(E*(P*U*N*U.T*P+N*U*P*U.T*N))
    eq(J,s.Rational(112,25),'particle plus hole energy')
    eq(J,s.trace(comm(Q,U).T*E*comm(Q,U))/4,'weighted commutator factor')
    # Momentum radial tail r^(2+2s-2p) is integrable iff p>s+3/2.
    z=s.symbols('z',positive=True)
    eq(s.integrate(z**-3,(z,1,s.oo)),s.Rational(1,2),'energy p3 radial tail')
    check(s.integrate(z**-1,(z,1,s.oo))==s.oo,'p2 borderline divergence')
    check(3>s.Rational(1,2)+s.Rational(3,2),'energy weighted order strict')
    # Both x and momentum need L2 decay. Spatial N2 in R3 yields exponent -2.
    eq(s.integrate(z**-2,(z,1,s.oo)),1,'spatial decay integrable')
    b,L,T=s.symbols('b L T',positive=True)
    eq(s.integrate(b*s.exp(L*(T-z)),(z,0,T)),b*(s.exp(L*T)-1)/L,'Gronwall convolution')
    # Same-model plateau consumer: exact two-mode one-occupation density matrix.
    z=s.symbols('z',real=True)
    rho=s.ones(2)/2
    Uplus=s.diag(s.exp(-s.I*z/2),s.exp(s.I*z/2)); Uminus=Uplus.conjugate()
    mean=(Uplus*rho*Uplus.conjugate().T+Uminus*rho*Uminus.conjugate().T)/2
    eq(mean[0,1],s.cos(z)/2,'binary plateau coherence')
    check(mean.subs(z,s.pi/2).applyfunc(s.simplify)==s.eye(2)/2,'full neutral decoherence')
    eq(s.cos(s.pi)**2,1,'phase pi retains coherence modulus')
    eq(1-s.cos(z)**2,s.sin(z)**2,'multiplicative defect')
    return {'artifact':'K1897','coefficients':{'normal_form_denominator':8,'commutator_energy_factor':'1/4','dimension':3,'strict_threshold_offset':'3/2','energy_iteration_order':3,'rational_unitary_energy':'112/25','plateau_visibility_phase':'pi/2','plateau_visibility':0},'evidence_kind':'14 exact finite/analytic controls; continuum proof in exploration uses imported regularization and weighted Duhamel','source_pins':{PIN:sha(PIN)},'scope':'post-pulse one-particle excitation moments; no active-time or total-many-body-moment theorem'}
def main():
    data=calculate()
    if '--write' in sys.argv:REPORT.write_text(json.dumps(data,indent=2)+'\n')
    else:check(json.loads(REPORT.read_text())==data,'serialized report and dependency pin')
    print('PASS K1897: 14 exact controls; report/pin consistency')
if __name__=='__main__':main()
