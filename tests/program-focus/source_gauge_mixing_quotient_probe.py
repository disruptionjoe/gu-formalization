#!/usr/bin/env python3
"""Exact controls for the relative grading detector; no physical-mode test.

Small matrices check identities and countercontrols. The accompanying written
argument, not a small-rank sample, supplies the quantified full-carrier result.
Execute serially; mathematical scope is stated in the companion result.
"""
import argparse
import sympy as s

p = argparse.ArgumentParser()
p.add_argument('--mutant', choices=[
    'freeze-grade', 'quotient-all-translations', 'freeze-epsilon-true-gauge',
    'drop-horizontal-readout', 'drop-D0h', 'erase-left-curvature'])
args = p.parse_args()
I = s.I
checks = 0

def norm0(m):
    return m.applyfunc(s.simplify) == s.zeros(*m.shape)

def check(ok, label):
    global checks
    assert bool(ok), label
    checks += 1

def eq(a, b, label):
    check(norm0(a-b), label)

def comm(a, b):
    return a*b-b*a

def sharp(a, k):
    return k.inv()*a.conjugate().T*k

# K95-style neutral graded pairing, reduced to paired one-dimensional halves.
K = s.Matrix([[0,1],[1,0]])
O = s.diag(1,-1)
Q = I*s.Matrix([[0,1],[1,0]])
N = s.Matrix([[0,I],[0,0]])
h = s.eye(2)+N
E = s.eye(2)+2*N
B0 = O
eta = Q+O
kappa = Q+3*O
eq(O*O, s.eye(2), 'involution')
eq(sharp(O,K), -O, 'grade sharp')
for name, a in [('Q',Q),('N',N),('eta',eta),('kappa',kappa),('B0',B0)]:
    eq(sharp(a,K), -a, name+' is parent skew')
for name, g in [('h',h),('epsilon',E)]:
    eq(g.conjugate().T*K*g,K,name+' is K-unitary')

# First jet epsilon'=epsilon eta and constant reference grade.
Oe = E.inv()*O*E
dOe = comm(Oe,eta)
B = E.inv()*B0*E+eta
eq(dOe+comm(B,Oe),s.zeros(2),'transported reference preserves grade')
T = Q + 2*O
A = B+T
detector = dOe+comm(A,Oe)
eq(detector,comm(T,Oe),'relative detector identity')
To = (T-Oe*T*Oe)/2
eq(detector,2*To*Oe,'odd detector identity')
eq(detector*Oe/2,To,'inverse on odd part')
eq(detector*Oe+Oe*detector,s.zeros(2),'detector anticommutes grade')

# First jet h'=h kappa; transforms both connections and the grade derivative.
Ah = h.inv()*A*h+kappa
Bh = h.inv()*B*h+kappa
Oh = Oe if args.mutant=='freeze-grade' else h.inv()*Oe*h
dOh = h.inv()*dOe*h+comm(Oh,kappa)
Kh = dOh+comm(Ah,Oh)
eq(Kh,h.inv()*detector*h,'finite moving-grade gauge covariance')
eq(Ah-Bh,h.inv()*T*h,'relative connection gauge covariance')
eq(dOh+comm(Bh,Oh),s.zeros(2),'moving reference remains parallel')
check(Kh.rank()==detector.rank(),'detector rank transport')

# A complete real basis of u(1,1) in the neutral frame: even2 plus odd2.
parent_basis = [O,I*s.eye(2),s.Matrix([[0,I],[0,0]]),s.Matrix([[0,0],[I,0]])]
for j,a in enumerate(parent_basis):
    eq(sharp(a,K),-a,f'parent basis {j}')
    odd=(a-O*a*O)/2
    eq(comm(a,O),2*odd*O,f'whole parent split {j}')
    eq(comm(a,O)*O/2,odd,f'whole parent inverse {j}')

# At zero relative T, epsilon motion is independent of primitive varpi motion.
lambda_ = Q
dlambda = 2*Q
DBlambda = dlambda+comm(B0,lambda_)
true_alpha = DBlambda
true_deltaT = true_alpha if args.mutant=='freeze-epsilon-true-gauge' else true_alpha-DBlambda
eq(comm(true_deltaT,O),s.zeros(2),'true gauge detector vanishes at T0')
primitive_detector = s.zeros(2) if args.mutant=='quotient-all-translations' else comm(DBlambda,O)
check(not norm0(primitive_detector),'same alpha with epsilon fixed is detected')
eq(comm(Q,O),2*Q*O,'odd translation detected')

# Flat relative connection A=Q dx,B=0: curvature has no two-form term,
# but the grade detector is nonzero. A true gauge first jet moves both A,B.
flat_curvature = comm(Q,Q)
eq(flat_curvature,s.zeros(2),'one-direction constant connection flat')
check(not norm0(comm(Q,O)),'flat relative connection still detected')
pure_A = Q
pure_B = Q
pure_dO = comm(O,Q)
eq(pure_dO+comm(pure_A,O),s.zeros(2),'pure gauge moving-grade control')
eq(pure_A-pure_B,s.zeros(2),'pure gauge has zero relative distortion')

# Exact real Cl(3,1) control. No K77 or full14D reality claim is inferred.
x = s.Matrix([[0,1],[1,0]])
z = s.diag(1,-1)
j = s.Matrix([[0,1],[-1,0]])
one = s.eye(2)
g = [s.kronecker_product(x,one),s.kronecker_product(z,x),
     s.kronecker_product(z,z),s.kronecker_product(z,j)]
signs = [1,1,1,-1]
id4 = s.eye(4)
for a in range(4):
    for b in range(4):
        eq(g[a]*g[b]+g[b]*g[a],2*signs[a]*id4 if a==b else s.zeros(4),
           f'Clifford {a},{b}')
KH = I*g[0]*g[1]*g[2]
omega = g[0]*g[1]*g[2]*g[3]
OH = I*omega
eq(KH.conjugate().T,KH,'horizontal auxiliary Krein form Hermitian')
check(KH.det()!=0,'horizontal Krein nondegenerate')
eq(omega*omega,-id4,'real horizontal volume square')
eq(sharp(omega,KH),omega,'horizontal volume sharp')
eq(OH*OH,id4,'control grading involution')
eq(sharp(OH,KH),-OH,'control grading sharp')

real_alpha=[]
for a in range(4):
    eq(sharp(g[a],KH),g[a],f'Clifford selfadjoint {a}')
    eq(g[a]*omega+omega*g[a],s.zeros(4),f'vector volume anticommutator {a}')
    ar=g[a]*omega
    real_alpha.append(ar)
    eq(sharp(ar,KH),-ar,f'real witness sharp {a}')
    eq(ar.conjugate(),ar,f'real witness conjugation {a}')
    eq(ar*OH+OH*ar,s.zeros(4),f'real witness odd {a}')
    eq(comm(ar,OH),2*ar*OH,f'real witness detector {a}')
    check(ar.rank()==4,f'real witness invertible evaluation {a}')

J = s.Matrix.vstack(*g)
Gamma = s.Matrix.hstack(*[signs[a]*g[a] for a in range(4)])
eq(Gamma*J,4*id4,'actual horizontal trace-section identity')
b = s.zeros(16,4) if args.mutant=='drop-horizontal-readout' else J*omega
tau = 4*omega
sigma = tau-Gamma*b
eq(sigma,s.zeros(4),'actual NE graph sigma cancellation')
eq(Gamma*b,4*omega,'real oneform survives horizontal observation')
check(b.rank()==4,'real oneform graph full support in reduced control')

# Coherent moving observation: arbitrary invertible frame, not fixed gamma.
r = s.eye(4)
r[0,1] = 2
r[2,3] = -1
r4 = s.diag(r,r,r,r)
gp = [r.inv()*ga*r for ga in g]
Jp = s.Matrix.vstack(*gp)
Gp = s.Matrix.hstack(*[signs[a]*gp[a] for a in range(4)])
op = r.inv()*omega*r
eq(Jp*op*r.inv(),r4.inv()*J*omega,'moving observed real graph covariance')
eq(Gp*Jp,4*id4,'moving Clifford trace identity')
check((Jp*op).rank()==4,'moving graph retains rank')

# Source left tilt at fixed reference, including both wrapper derivatives.
# This is a first-jet check of the printed scalar-to-oneform NE block.
dE = E*eta
dh = h*kappa
D0h = dh+comm(B0,h)
ell = h.inv()*D0h
EL = h*E
dEL = dh*E+h*dE
BL = EL.inv()*B0*EL+EL.inv()*dEL
AL = A+E.inv()*ell*E
eq(BL,B+E.inv()*ell*E,'left tilt shifts both connections equally')
eq(AL-BL,T,'left tilt fixes relative distortion')
U = E*T*E.inv()
Dhat = E*A*E.inv()-dE*E.inv()
DhatL = EL*AL*EL.inv()-dEL*EL.inv()
eq(Dhat,B0+U,'wrapped NE reference decomposition')
eq(DhatL,B0+h*U*h.inv(),'left wrapped NE coefficient law')
conjugate_Dhat = h*Dhat*h.inv()-dh*h.inv()
reported_defect = s.zeros(2) if args.mutant=='drop-D0h' else D0h*h.inv()
eq(DhatL-conjugate_Dhat,reported_defect,'left NE differential conjugation defect')
eq(dh+DhatL*h-h*Dhat,D0h,'candidate h-spinor intertwiner defect')
check(not norm0(D0h),'nonparallel local h really fails candidate field law')
check(not norm0(DhatL-Dhat),'noncentral relative coefficient fails fixed-field law')
eq(EL*BL*EL.inv()-dEL*EL.inv(),B0,'zero-distortion fixed-field control')
eq(B0+h*(I*s.eye(2))*h.inv(),B0+I*s.eye(2),'central fixed-field control')
dh_parallel = h*B0-B0*h
eq(dh_parallel+DhatL*h-h*Dhat,s.zeros(2),'reference-parallel transported-field control')

# Finite local counterexample to any same-slot pointwise spinor intertwiner.
# The full-form NE identity symbol fixes independent row/column maps inversely.
# No slot-mixing, differential field law, moving reference or physical quotient.
y = s.Symbol('y',real=True)
hy = s.eye(2)+y*N
hy_inv = s.eye(2)-y*N
eq(N*N,s.zeros(2),'left-curvature nilpotent parent generator')
eq(hy*hy_inv,s.eye(2),'finite polynomial group inverse')
eq(hy.conjugate().T*K*hy,K,'finite local left transformation remains K-unitary')
eq(comm(N,Q),-O,'finite curvature generator noncommutes')
U_left_x = hy*Q*hy_inv
eq(sharp(U_left_x,K),-U_left_x,'left transformed NE coefficient remains parent valued')
initial_F_yx = Q.diff(y)
eq(initial_F_yx,s.zeros(2),'initial isolated NE connection is flat')
actual_F_yx = U_left_x.diff(y)
reported_F_yx = s.zeros(2) if args.mutant=='erase-left-curvature' else actual_F_yx
eq(reported_F_yx,hy*comm(N,Q)*hy_inv,'finite left NE curvature formula')
eq(actual_F_yx.subs(y,0),-O,'finite left curvature nonzero at base point')
check(actual_F_yx.subs(y,0).rank()==2,'finite nonflat control has invertible curvature block')
print(f'PASS {checks} exact gauge/relative-grade/current controls; no physical-mode verdict')
